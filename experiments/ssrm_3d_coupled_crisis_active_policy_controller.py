#!/usr/bin/env python3
"""Active crisis-window policy learning for SSRM-3D coupled crises.

Reports 117 and 118 trained value heads around active crisis candidates. They
found useful labels, but held-out repair still did not become a robust learned
action loop. This benchmark moves the learning target from passive value
labels to sampled crisis-window actions: the policy chooses repair candidates
during active crises and is updated from the later crisis outcome.

This is still bounded policy-gradient evidence, not open-ended civilization or
subjective consciousness. The candidate action set is supplied, the base GRU is
still imitation trained, and the environmental/social action heads remain only
as comparison baselines.
"""

from __future__ import annotations

import argparse
import json
import random
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import torch

import ssrm_3d_coupled_crisis_active_state_value_controller as report117
import ssrm_3d_coupled_crisis_joint_arbitration_controller as report113
import ssrm_3d_coupled_crisis_randomized_transfer_controller as report114
import ssrm_3d_coupled_crisis_rollout_window_controller as report111
import ssrm_3d_coupled_social_environment_maturation_controller as coupled
import ssrm_3d_learned_multiday_maturation_controller as base
import ssrm_3d_return_selected_multiday_maturation_controller as report105
from ssrm_maturation.agents import choose_action, make_agents
from ssrm_maturation.benchmark import TRACE_CHECKPOINTS, score_episode, snapshot
from ssrm_maturation.environment import clamp, living
from ssrm_maturation.models import CONDITIONS, Agent, Condition, Trace, World


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_active_policy"
POLICY_SEED = 20261621
ACTION_CANDIDATES = report117.ACTION_CANDIDATES
ACTION_TO_INDEX = {name: index for index, name in enumerate(ACTION_CANDIDATES)}
POLICY_CONTEXT_NAMES = (
    "elapsed_fraction",
    "remaining_fraction",
    "env_progress",
    "social_progress",
    "env_response_rate",
    "social_response_rate",
    "current_env_fraction",
    "current_social_fraction",
)
POLICY_INPUT_SIZE = base.FEATURE_COUNT + len(POLICY_CONTEXT_NAMES)
FIXED_JOINT = report117.FIXED_JOINT


@dataclass(frozen=True)
class Config:
    train_seeds: Sequence[int]
    tune_seeds: Sequence[int]
    eval_seeds: Sequence[int]
    hours: float = 96.0
    step_hours: float = 0.10
    population: int = 14
    epochs: int = 24
    hidden_size: int = 64
    learning_rate: float = 0.004
    action_epochs: int = 32
    action_hidden_size: int = 64
    action_learning_rate: float = 0.004
    policy_epochs: int = 4
    policy_hidden_size: int = 64
    policy_learning_rate: float = 0.003
    entropy_coef: float = 0.008
    policy_temperature: float = 1.0
    policy_bias_candidates: Sequence[float] = (0.0, 0.20, 0.40, 0.70, 1.00)
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class PolicyTrainingRow:
    episodes: int
    crises: int
    epochs: int
    final_loss: float
    mean_return: float
    return_std: float
    moving_baseline: float
    mean_entropy: float
    policy_temperature: float
    entropy_coef: float
    device_used: str
    parameter_count: int


@dataclass(frozen=True)
class PolicySelectionRow:
    policy_bias: float
    tune_total_score: float
    tune_maturation_score: float
    tune_crisis_score: float
    tune_resolved_rate: float
    tune_env_response: float
    tune_social_response: float
    tune_coupled_response: float
    tune_damage: float
    selection_objective: float
    selected: bool


@dataclass(frozen=True)
class PolicyVerdictRow:
    selected_router: str
    selected_policy_bias: float
    training_crises: int
    active_policy_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    active_policy_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    active_policy_resolved_rate: float
    fixed_joint_resolved_rate: float
    return_selected_resolved_rate: float
    active_policy_coupled_response: float
    fixed_joint_coupled_response: float
    return_selected_coupled_response: float
    gain_over_return_selected: float
    gain_over_fixed_joint: float
    social_culture_crisis_loss: float
    environment_crisis_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    mean_crisis_count: float
    supports_return_baseline_improvement: bool
    supports_fixed_joint_improvement: bool
    supports_active_policy_learning: bool
    supports_social_environment_dependency: bool
    verdict: str


class ActiveCrisisPolicyNet(torch.nn.Module):
    def __init__(self, hidden_size: int) -> None:
        super().__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(POLICY_INPUT_SIZE, hidden_size),
            torch.nn.LayerNorm(hidden_size),
            torch.nn.Tanh(),
            torch.nn.Linear(hidden_size, hidden_size),
            torch.nn.Tanh(),
            torch.nn.Linear(hidden_size, len(ACTION_CANDIDATES)),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def stdev(values: Sequence[float]) -> float:
    if len(values) < 2:
        return 0.0
    avg = mean(values)
    return (sum((value - avg) ** 2 for value in values) / len(values)) ** 0.5


def parse_ints(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def parse_floats(value: str) -> Tuple[float, ...]:
    return tuple(float(part.strip()) for part in value.split(",") if part.strip())


def policy_context(
    active: coupled.ActiveCrisis,
    action_counts: Dict[str, int],
    alive_count: int,
    world_time: float,
) -> List[float]:
    elapsed_fraction = clamp((world_time - active.start) / max(1e-6, active.duration))
    remaining_fraction = clamp((active.end - world_time) / max(1e-6, active.duration))
    env_fraction = min(1.0, active.env_progress / active.profile.env_need)
    social_fraction = min(1.0, active.social_progress / active.profile.social_need)
    env_rate = active.env_response_steps / max(1, active.steps)
    social_rate = active.social_response_steps / max(1, active.steps)
    current_env, current_social = report117.response_fractions(action_counts, alive_count)
    return [
        elapsed_fraction,
        remaining_fraction,
        env_fraction,
        social_fraction,
        env_rate,
        social_rate,
        current_env,
        current_social,
    ]


def policy_features(
    features: Sequence[float],
    active: coupled.ActiveCrisis,
    action_counts: Dict[str, int],
    alive_count: int,
    world_time: float,
    ablation: str = "none",
) -> List[float]:
    values = base.mask_features(list(features), ablation) + policy_context(active, action_counts, alive_count, world_time)
    if len(values) != POLICY_INPUT_SIZE:
        raise RuntimeError(f"policy feature mismatch: {len(values)} != {POLICY_INPUT_SIZE}")
    return values


def allowed_indices(ablation: str) -> List[int]:
    actions = list(ACTION_CANDIDATES)
    if ablation == "environment":
        actions = [action for action in actions if action not in report111.ENV_RESPONSE_ACTIONS]
    if ablation == "social_culture":
        actions = [action for action in actions if action not in report111.SOCIAL_RESPONSE_ACTIONS]
    return [ACTION_TO_INDEX[action] for action in actions]


def masked_logits(logits: torch.Tensor, ablation: str, policy_bias: float = 0.0) -> torch.Tensor:
    mask = torch.full_like(logits, -1e9)
    for index in allowed_indices(ablation):
        mask[..., index] = 0.0
    biased = logits + mask
    if policy_bias:
        for action, index in ACTION_TO_INDEX.items():
            if action != "none":
                biased[..., index] = biased[..., index] + policy_bias
    return biased


def choose_policy_candidate(
    policy_model: ActiveCrisisPolicyNet,
    features: Sequence[float],
    active: coupled.ActiveCrisis,
    action_counts: Dict[str, int],
    alive_count: int,
    world_time: float,
    device: torch.device,
    ablation: str,
    temperature: float,
    policy_bias: float = 0.0,
    sample: bool = False,
) -> Tuple[str, Optional[torch.Tensor], Optional[torch.Tensor]]:
    x = torch.tensor(
        [policy_features(features, active, action_counts, alive_count, world_time, ablation)],
        dtype=torch.float32,
        device=device,
    )
    if sample:
        logits = policy_model(x) / max(0.05, temperature)
        logits = masked_logits(logits, ablation, policy_bias)
    else:
        with torch.no_grad():
            logits = policy_model(x) / max(0.05, temperature)
            logits = masked_logits(logits, ablation, policy_bias)
    if sample:
        dist = torch.distributions.Categorical(logits=logits.squeeze(0))
        index = dist.sample()
        return ACTION_CANDIDATES[int(index.item())], dist.log_prob(index), dist.entropy()
    index = int(logits.argmax(dim=-1).item())
    return ACTION_CANDIDATES[index], None, None


def sample_policy_candidate_without_graph(
    policy_model: ActiveCrisisPolicyNet,
    features: Sequence[float],
    active: coupled.ActiveCrisis,
    action_counts: Dict[str, int],
    alive_count: int,
    world_time: float,
    device: torch.device,
    temperature: float,
) -> Tuple[str, List[float], int, float]:
    values = policy_features(features, active, action_counts, alive_count, world_time, "none")
    with torch.no_grad():
        x = torch.tensor([values], dtype=torch.float32, device=device)
        logits = policy_model(x) / max(0.05, temperature)
        logits = masked_logits(logits, "none", 0.0)
        dist = torch.distributions.Categorical(logits=logits.squeeze(0))
        index = dist.sample()
        entropy = float(dist.entropy().detach().cpu().item())
    action_index = int(index.item())
    return ACTION_CANDIDATES[action_index], values, action_index, entropy


def crisis_fraction(active: coupled.ActiveCrisis) -> Tuple[float, float, float]:
    env_fraction = min(1.0, active.env_progress / active.profile.env_need)
    social_fraction = min(1.0, active.social_progress / active.profile.social_need)
    return env_fraction, social_fraction, min(env_fraction, social_fraction)


def bounded(value: float, low: float = -1.5, high: float = 2.5) -> float:
    return max(low, min(high, value))


def crisis_window_return(active: coupled.ActiveCrisis, damage_delta: float) -> float:
    env_fraction, social_fraction, coupled_fraction = crisis_fraction(active)
    resolved = 1.0 if coupled_fraction >= 0.92 else 0.0
    env_rate = active.env_response_steps / max(1, active.steps)
    social_rate = active.social_response_steps / max(1, active.steps)
    coupled_rate = active.coupled_response_steps / max(1, active.steps)
    balance = 1.0 - min(1.0, abs(env_fraction - social_fraction))
    unresolved = max(0.0, 0.92 - coupled_fraction)
    return bounded(
        coupled_fraction * 1.25
        + resolved * 0.82
        + coupled_rate * 0.45
        + min(env_rate, social_rate) * 0.18
        + balance * 0.10
        - unresolved * 0.60
        - max(0.0, damage_delta) * 1.30
    )


def active_policy_candidate(
    agent: Agent,
    features: Sequence[float],
    action_counts: Dict[str, int],
    alive_count: int,
    policy_model: ActiveCrisisPolicyNet,
    device: torch.device,
    ablation: str,
    tracker: coupled.CrisisTracker,
    world: World,
    policy_bias: float,
    temperature: float,
) -> Optional[str]:
    active = tracker.active
    if active is None:
        return None
    action, _, _ = choose_policy_candidate(
        policy_model,
        features,
        active,
        action_counts,
        alive_count,
        world.time,
        device,
        ablation,
        temperature,
        policy_bias,
        sample=False,
    )
    if action == "none":
        return None
    return action


def run_policy_training_episode(
    seed: int,
    cfg: Config,
    base_model: base.ControllerNet,
    policy_model: ActiveCrisisPolicyNet,
    optimizer: torch.optim.Optimizer,
    device: torch.device,
    router: report105.PressureRouter,
    moving_baseline: float,
) -> Tuple[int, List[float], List[float], float, float]:
    condition = CONDITIONS[0]
    rng = random.Random(seed * 139 + POLICY_SEED)
    agents = make_agents(rng, cfg.population)
    world = coupled.prepare_world(rng, cfg)
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
    pending_samples: List[Tuple[List[float], int]] = []
    pending_entropies: List[float] = []
    pending_damage_start = tracker.damage_integral
    returns: List[float] = []
    entropy_values: List[float] = []
    final_loss = 0.0
    crises = 0
    policy_model.train()

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        action_counts: Dict[str, int] = {}
        coupled.maybe_start_crisis(world, tracker, rng, events)
        if tracker.active is not None and not pending_samples:
            pending_damage_start = tracker.damage_integral
        if tracker.active is not None:
            coupled.apply_crisis_symptoms(world, tracker.active, dt)

        def selector(
            agent: Agent,
            current_world: World,
            current_condition: Condition,
            current_rng: random.Random,
            features: List[float],
            previous: int,
        ) -> str:
            active = tracker.active
            if active is None:
                action = report117.learned_policy_action(agent, features, base_model, recurrent_states, router, device, "none")
            else:
                action, sampled_features, action_index, entropy = sample_policy_candidate_without_graph(
                    policy_model,
                    features,
                    active,
                    action_counts,
                    len(living(agents)),
                    current_world.time,
                    device,
                    cfg.policy_temperature,
                )
                if current_world.time >= 12.0:
                    pending_samples.append((sampled_features, action_index))
                    pending_entropies.append(entropy)
                    entropy_values.append(entropy)
                if action == "none":
                    action = report117.learned_policy_action(agent, features, base_model, recurrent_states, router, device, "none")
            action_counts[action] = action_counts.get(action, 0) + 1
            return action

        base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
        active_before_completion = tracker.active
        report111.update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
        coupled.complete_crisis_if_due(world, agents, tracker, events)
        if active_before_completion is not None and tracker.active is None:
            reward = crisis_window_return(active_before_completion, tracker.damage_integral - pending_damage_start)
            returns.append(reward)
            crises += 1
            if pending_samples:
                advantage = reward - moving_baseline
                batch_x = torch.tensor([item[0] for item in pending_samples], dtype=torch.float32, device=device)
                batch_actions = torch.tensor([item[1] for item in pending_samples], dtype=torch.long, device=device)
                logits = policy_model(batch_x) / max(0.05, cfg.policy_temperature)
                logits = masked_logits(logits, "none", 0.0)
                dist = torch.distributions.Categorical(logits=logits)
                log_term = dist.log_prob(batch_actions).mean()
                entropy_term = dist.entropy().mean()
                loss = -float(advantage) * log_term - cfg.entropy_coef * entropy_term
                optimizer.zero_grad()
                loss.backward()
                torch.nn.utils.clip_grad_norm_(policy_model.parameters(), 2.0)
                optimizer.step()
                final_loss = float(loss.detach().cpu().item())
            moving_baseline = moving_baseline * 0.86 + reward * 0.14
            pending_samples = []
            pending_entropies = []
            pending_damage_start = tracker.damage_integral

    return crises, returns, entropy_values, moving_baseline, final_loss


def train_policy_model(
    cfg: Config,
    base_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[ActiveCrisisPolicyNet, PolicyTrainingRow]:
    torch.manual_seed(POLICY_SEED)
    policy_model = ActiveCrisisPolicyNet(cfg.policy_hidden_size).to(device)
    optimizer = torch.optim.Adam(policy_model.parameters(), lr=cfg.policy_learning_rate)
    moving_baseline = 0.0
    all_returns: List[float] = []
    all_entropy: List[float] = []
    total_crises = 0
    final_loss = 0.0
    episodes = 0
    for epoch in range(cfg.policy_epochs):
        for seed in cfg.train_seeds:
            crises, returns, entropies, moving_baseline, final_loss = run_policy_training_episode(
                seed + epoch * 1009,
                cfg,
                base_model,
                policy_model,
                optimizer,
                device,
                router,
                moving_baseline,
            )
            total_crises += crises
            all_returns.extend(returns)
            all_entropy.extend(entropies)
            episodes += 1
    policy_model.eval()
    return policy_model, PolicyTrainingRow(
        episodes=episodes,
        crises=total_crises,
        epochs=cfg.policy_epochs,
        final_loss=final_loss,
        mean_return=mean(all_returns),
        return_std=stdev(all_returns),
        moving_baseline=moving_baseline,
        mean_entropy=mean(all_entropy),
        policy_temperature=cfg.policy_temperature,
        entropy_coef=cfg.entropy_coef,
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in policy_model.parameters()),
    )


def run_active_policy_episode(
    seed: int,
    cfg: Config,
    controller: str,
    model: Optional[base.ControllerNet],
    policy_model: Optional[ActiveCrisisPolicyNet],
    device: torch.device,
    router: report105.PressureRouter,
    policy_bias: float = 0.0,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, Trace, coupled.CrisisTracker]:
    if controller == "active_policy_gru" and (model is None or policy_model is None):
        raise ValueError("active_policy_gru requires base and policy models")
    condition = CONDITIONS[1] if controller == "reactive" else CONDITIONS[0]
    rng = random.Random(seed * 127 + sum(ord(ch) for ch in controller + router.name + ablation) + int(policy_bias * 1000) + 6211)
    agents = make_agents(rng, cfg.population)
    world = coupled.prepare_world(rng, cfg)
    baseline = base.initial_baseline(world, cfg.population)
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
    trace_out = Trace(seed=seed, condition=f"{controller}:{router.name}:policy_{policy_bias:g}:{ablation}")
    checkpoints = list(TRACE_CHECKPOINTS)
    no_pre_gate_shock = True
    alive_at_12h = cfg.population
    at_12: dict[str, float] = {}
    if trace:
        trace_out.frames.append(snapshot(world, agents, "0h", events))
        if checkpoints and checkpoints[0] == 0.0:
            checkpoints.pop(0)

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        action_counts: Dict[str, int] = {}
        coupled.maybe_start_crisis(world, tracker, rng, events)
        if tracker.active is not None:
            coupled.apply_crisis_symptoms(world, tracker.active, dt)

        def selector(
            agent: Agent,
            current_world: World,
            current_condition: Condition,
            current_rng: random.Random,
            features: List[float],
            previous: int,
        ) -> str:
            active = tracker.active
            if controller == "designed":
                action = report111.bottleneck_target_action(active, features) if active is not None else choose_action(agent, current_world, current_condition, current_rng)
            elif controller == "reactive":
                action = choose_action(agent, current_world, current_condition, current_rng)
            elif model is None:
                action = "rest"
            elif controller == "active_policy_gru" and active is not None:
                action = active_policy_candidate(
                    agent,
                    features,
                    action_counts,
                    len(living(agents)),
                    policy_model,
                    device,
                    ablation,
                    tracker,
                    current_world,
                    policy_bias,
                    cfg.policy_temperature,
                )
                if action is None:
                    action = report117.learned_policy_action(agent, features, model, recurrent_states, router, device, ablation)
            else:
                action = report117.learned_policy_action(agent, features, model, recurrent_states, router, device, ablation)
            if controller == "active_policy_gru" and active is not None:
                if ablation == "environment" and action in report111.ENV_RESPONSE_ACTIONS:
                    action = "rest"
                if ablation == "social_culture" and action in report111.SOCIAL_RESPONSE_ACTIONS:
                    action = "rest"
            action_counts[action] = action_counts.get(action, 0) + 1
            return action

        base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
        report111.update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
        coupled.complete_crisis_if_due(world, agents, tracker, events)
        if world.time < 12.0 and world.major_shocks > 0:
            no_pre_gate_shock = False
        if world.time >= 12.0 and not at_12:
            alive_at_12h = len(living(agents))
            at_12 = {
                "development": clamp(
                    (world.architecture - baseline["architecture"]) * 0.48
                    + (world.tools + world.workshop * 0.45 + world.fire_control * 0.30 - baseline["tool_system"]) * 0.34
                    + (world.paths - baseline["paths"]) * 0.16
                ),
                "knowledge": clamp(world.knowledge_transfer * 0.80 + (world.culture + world.symbols * 0.50 - baseline["culture_system"]) * 0.45),
            }
        while trace and checkpoints and world.time >= checkpoints[0] - 1e-9:
            hour = checkpoints.pop(0)
            frame = snapshot(world, agents, f"{hour:g}h", events)
            frame["active_crisis"] = tracker.active.profile.name if tracker.active else None
            frame["crisis_resolved"] = tracker.resolved
            frame["crisis_unresolved"] = tracker.unresolved
            frame["crisis_damage"] = tracker.damage_integral
            trace_out.frames.append(frame)
    if tracker.active is not None:
        coupled.complete_crisis_if_due(world, agents, tracker, events)
    episode = score_episode(world, agents, baseline, at_12, seed, condition, alive_at_12h, no_pre_gate_shock)
    crisis_score, resolved_rate, env_response, social_response, coupled_response = coupled.crisis_metrics(tracker)
    total_score = clamp(episode.maturation_score * 0.52 + crisis_score * 0.48)
    eval_row = coupled.EvalRow(
        seed=seed,
        controller=controller,
        ablation=ablation,
        total_score=total_score,
        maturation_score=episode.maturation_score,
        crisis_score=crisis_score,
        resolved_rate=resolved_rate,
        unresolved_count=tracker.unresolved,
        env_response_rate=env_response,
        social_response_rate=social_response,
        coupled_response_rate=coupled_response,
        crisis_damage=tracker.damage_integral,
        final_alive=episode.final_alive,
        total_agents=episode.total_agents,
        alive_at_12h=episode.alive_at_12h,
        no_major_shock_before_12h=episode.no_major_shock_before_12h,
        post_gate_shock=episode.post_gate_shock,
        births=episode.births,
        deaths=episode.deaths,
        architecture_tier=episode.architecture_tier,
        tool_tier=episode.tool_tier,
        knowledge_transfer=episode.knowledge_transfer,
        adaptation_evidence=episode.adaptation_evidence,
        survival_score=episode.survival_score,
        development_score=episode.development_score,
        knowledge_score=episode.knowledge_score,
        recovery_score=episode.recovery_score,
    )
    if trace and (not trace_out.frames or trace_out.frames[-1]["hours"] < cfg.hours):
        frame = snapshot(world, agents, f"{cfg.hours:g}h", events)
        frame["active_crisis"] = tracker.active.profile.name if tracker.active else None
        frame["crisis_resolved"] = tracker.resolved
        frame["crisis_unresolved"] = tracker.unresolved
        frame["crisis_damage"] = tracker.damage_integral
        trace_out.frames.append(frame)
    return eval_row, trace_out, tracker


def selection_objective(rows: Sequence[coupled.EvalRow]) -> Tuple[float, float, float, float, float, float, float, float, float]:
    total = mean(row.total_score for row in rows)
    maturation = mean(row.maturation_score for row in rows)
    crisis = mean(row.crisis_score for row in rows)
    resolved = mean(row.resolved_rate for row in rows)
    env_response = mean(row.env_response_rate for row in rows)
    social_response = mean(row.social_response_rate for row in rows)
    coupled_response = mean(row.coupled_response_rate for row in rows)
    damage = mean(row.crisis_damage for row in rows)
    objective = total * 0.48 + crisis * 1.25 + resolved * 0.72 + coupled_response * 0.82 - damage * 0.32
    return total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective


def select_policy_bias(
    cfg: Config,
    model: base.ControllerNet,
    policy_model: ActiveCrisisPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[float, List[PolicySelectionRow]]:
    rows: List[PolicySelectionRow] = []
    best_bias = 0.0
    best_objective = -1e9
    for bias in cfg.policy_bias_candidates:
        eval_rows = [
            run_active_policy_episode(
                seed,
                cfg,
                "active_policy_gru",
                model,
                policy_model,
                device,
                router,
                policy_bias=bias,
            )[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_objective = objective
            best_bias = bias
        rows.append(PolicySelectionRow(
            policy_bias=bias,
            tune_total_score=total,
            tune_maturation_score=maturation,
            tune_crisis_score=crisis,
            tune_resolved_rate=resolved,
            tune_env_response=env_response,
            tune_social_response=social_response,
            tune_coupled_response=coupled_response,
            tune_damage=damage,
            selection_objective=objective,
            selected=False,
        ))
    return best_bias, [replace(row, selected=(row.policy_bias == best_bias)) for row in rows]


def ablations_from_summary(summary: Sequence[coupled.SummaryRow]) -> List[coupled.AblationRow]:
    base_row = coupled.row_lookup(summary, "active_policy_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = coupled.row_lookup(summary, "active_policy_gru", ablation)
        rows.append(coupled.AblationRow(
            ablation=ablation,
            mean_total_score=row.mean_total_score,
            total_loss=base_row.mean_total_score - row.mean_total_score,
            crisis_score_loss=base_row.mean_crisis_score - row.mean_crisis_score,
            resolved_rate_loss=base_row.mean_resolved_rate - row.mean_resolved_rate,
            env_response_loss=base_row.mean_env_response_rate - row.mean_env_response_rate,
            social_response_loss=base_row.mean_social_response_rate - row.mean_social_response_rate,
            coupled_response_loss=base_row.mean_coupled_response_rate - row.mean_coupled_response_rate,
            damage_increase=row.mean_crisis_damage - base_row.mean_crisis_damage,
        ))
    return rows


def transfer_verdict(
    summary: Sequence[coupled.SummaryRow],
    ablations: Sequence[coupled.AblationRow],
    router: report105.PressureRouter,
    selected_bias: float,
    schedules: Sequence[report114.ScheduleRow],
    policy_training: PolicyTrainingRow,
) -> PolicyVerdictRow:
    active = coupled.row_lookup(summary, "active_policy_gru", "none")
    fixed = coupled.row_lookup(summary, "fixed_joint_gru", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    supports_return = (
        policy_training.crises > 0
        and mean_crisis_count >= 4.0
        and active.mean_total_score - returned.mean_total_score >= 0.010
        and active.mean_crisis_score - returned.mean_crisis_score >= 0.040
        and active.mean_resolved_rate - returned.mean_resolved_rate >= 0.080
        and active.mean_coupled_response_rate - returned.mean_coupled_response_rate >= 0.080
        and active.mean_alive_at_12h >= 12.0
        and active.shock_gate_pass_rate == 1.0
        and active.post_gate_shock_rate == 1.0
    )
    supports_fixed = (
        active.mean_total_score - fixed.mean_total_score >= 0.005
        and active.mean_crisis_score - fixed.mean_crisis_score >= 0.020
        and active.mean_resolved_rate - fixed.mean_resolved_rate >= 0.020
        and active.mean_coupled_response_rate - fixed.mean_coupled_response_rate >= 0.020
    )
    supports_dependency = (
        active.mean_crisis_score > 0.0
        and social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    supports_policy = policy_training.crises > 0 and supports_return and supports_fixed
    return PolicyVerdictRow(
        selected_router=router.name,
        selected_policy_bias=selected_bias,
        training_crises=policy_training.crises,
        active_policy_total_score=active.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        active_policy_crisis_score=active.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        active_policy_resolved_rate=active.mean_resolved_rate,
        fixed_joint_resolved_rate=fixed.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        active_policy_coupled_response=active.mean_coupled_response_rate,
        fixed_joint_coupled_response=fixed.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        gain_over_return_selected=active.mean_total_score - returned.mean_total_score,
        gain_over_fixed_joint=active.mean_total_score - fixed.mean_total_score,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=active.shock_gate_pass_rate,
        post_gate_shock_rate=active.post_gate_shock_rate,
        survival_at_12h=active.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_return_baseline_improvement=supports_return,
        supports_fixed_joint_improvement=supports_fixed,
        supports_active_policy_learning=supports_policy,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_policy and supports_dependency else "partial_or_failed",
    )


def run_benchmark(cfg: Config) -> dict[str, object]:
    device = base.resolve_device(cfg.device)
    schedule_builder = report114.randomized_schedule_builder(cfg.hours)
    schedules = (
        report114.schedule_rows(cfg, "train", cfg.train_seeds, schedule_builder)
        + report114.schedule_rows(cfg, "tune", cfg.tune_seeds, schedule_builder)
        + report114.schedule_rows(cfg, "eval", cfg.eval_seeds, schedule_builder)
    )
    with report114.patched_transfer_world(schedule_builder, report114.randomized_prepare_world):
        sequences, labels = base.collect_sequences(cfg)
        x, y, mask = base.build_tensors(sequences, labels, device)
        training_rows: List[base.TrainingRow] = []
        models: Dict[str, base.ControllerNet] = {}
        for architecture in ("frame_mlp", "gru"):
            trained_model, row = base.train_model(architecture, x, y, mask, cfg, device)
            models[architecture] = trained_model
            training_rows.append(row)

        selected_router, router_selection = coupled.select_router(cfg, models["gru"], device)
        env_sequences, env_labels, social_sequences, social_labels, flags = report113.collect_joint_sequences(cfg)
        env_model, env_training = report113.train_action_model(
            cfg,
            device,
            "environment",
            env_sequences,
            env_labels,
            flags,
            20261631,
        )
        social_model, social_training = report113.train_action_model(
            cfg,
            device,
            "social",
            social_sequences,
            social_labels,
            flags,
            20261632,
        )
        policy_model, policy_training = train_policy_model(cfg, models["gru"], device, selected_router)
        selected_bias, policy_selection = select_policy_bias(cfg, models["gru"], policy_model, device, selected_router)

        eval_rows: List[coupled.EvalRow] = []
        trace_out = None
        crisis_logs: Dict[str, List[dict[str, object]]] = {}
        for seed in cfg.eval_seeds:
            for controller, model, router in (
                ("designed", None, report105.ROUTERS[0]),
                ("reactive", None, report105.ROUTERS[0]),
                ("frame_mlp", models["frame_mlp"], report105.ROUTERS[0]),
                ("gru", models["gru"], report105.ROUTERS[0]),
                ("return_selected_gru", models["gru"], selected_router),
            ):
                row, maybe_trace, tracker = report117.run_active_value_episode(
                    seed,
                    cfg,
                    controller,
                    model,
                    env_model,
                    social_model,
                    None,
                    0.0,
                    1.0,
                    device,
                    router,
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:{controller}:none"] = tracker.response_log
                if maybe_trace.frames:
                    trace_out = maybe_trace
            fixed_row, _, fixed_tracker = report117.run_active_value_episode(
                seed,
                cfg,
                "fixed_joint_gru",
                models["gru"],
                env_model,
                social_model,
                None,
                0.0,
                1.0,
                device,
                selected_router,
            )
            eval_rows.append(fixed_row)
            crisis_logs[f"{seed}:fixed_joint_gru:none"] = fixed_tracker.response_log
            active_row, maybe_trace, tracker = run_active_policy_episode(
                seed,
                cfg,
                "active_policy_gru",
                models["gru"],
                policy_model,
                device,
                selected_router,
                policy_bias=selected_bias,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(active_row)
            crisis_logs[f"{seed}:active_policy_gru:none"] = tracker.response_log
            if maybe_trace.frames:
                trace_out = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker = run_active_policy_episode(
                    seed,
                    cfg,
                    "active_policy_gru",
                    models["gru"],
                    policy_model,
                    device,
                    selected_router,
                    policy_bias=selected_bias,
                    ablation=ablation,
                )
                eval_rows.append(replace(row, ablation=ablation))
                crisis_logs[f"{seed}:active_policy_gru:{ablation}"] = tracker.response_log

    summary = coupled.summarize(eval_rows)
    ablations = ablations_from_summary(summary)
    verdict = transfer_verdict(summary, ablations, selected_router, selected_bias, schedules, policy_training)
    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "active_policy_gru", "frames": []}
    trace_payload["condition"] = "active_policy_gru"
    payload = {
        "config": {
            "train_seeds": list(cfg.train_seeds),
            "tune_seeds": list(cfg.tune_seeds),
            "eval_seeds": list(cfg.eval_seeds),
            "hours": cfg.hours,
            "step_hours": cfg.step_hours,
            "population": cfg.population,
            "epochs": cfg.epochs,
            "hidden_size": cfg.hidden_size,
            "action_epochs": cfg.action_epochs,
            "action_hidden_size": cfg.action_hidden_size,
            "policy_epochs": cfg.policy_epochs,
            "policy_hidden_size": cfg.policy_hidden_size,
            "policy_learning_rate": cfg.policy_learning_rate,
            "entropy_coef": cfg.entropy_coef,
            "policy_temperature": cfg.policy_temperature,
            "policy_bias_candidates": list(cfg.policy_bias_candidates),
            "device": cfg.device,
            "trace_seed": cfg.trace_seed,
        },
        "policy_context_names": list(POLICY_CONTEXT_NAMES),
        "action_candidates": list(ACTION_CANDIDATES),
        "schedule": [asdict(row) for row in schedules],
        "router_selection": [asdict(row) for row in router_selection],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "policy_training": asdict(policy_training),
        "policy_selection": [asdict(row) for row in policy_selection],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace_payload,
        "crisis_logs": crisis_logs,
        "notes": {
            "claim": "sampled crisis-window policy updates can learn active coupled-crisis repair choices",
            "not_claimed": "subjective consciousness, open-ended civilization, real-world competence, or a full actor-critic stack",
            "remaining_structure": "candidate repair actions are supplied, the base controller is imitation trained, and the environment is still an abstract simulator",
        },
    }
    report117.rows_to_csv(Path(f"{PREFIX}_schedule.csv"), schedules)
    report117.rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    report117.rows_to_csv(Path(f"{PREFIX}_action_training.csv"), [env_training, social_training])
    report117.rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    report117.rows_to_csv(Path(f"{PREFIX}_policy_training.csv"), [policy_training])
    report117.rows_to_csv(Path(f"{PREFIX}_policy_selection.csv"), policy_selection)
    report117.rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    report117.rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    report117.rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    report117.rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    report117.write_json(Path(f"{PREFIX}_results.json"), payload)
    report117.write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    report117.write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_ACTIVE_POLICY_RESULTS", payload)
    report117.write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_ACTIVE_POLICY_TRACE", trace_payload)
    return payload


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-seeds", default="20260911,20260912,20260913")
    parser.add_argument("--tune-seeds", default="20261111,20261112")
    parser.add_argument("--eval-seeds", default="20261121,20261122,20261123")
    parser.add_argument("--hours", type=float, default=96.0)
    parser.add_argument("--step-hours", type=float, default=0.10)
    parser.add_argument("--population", type=int, default=14)
    parser.add_argument("--epochs", type=int, default=24)
    parser.add_argument("--hidden-size", type=int, default=64)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--action-epochs", type=int, default=32)
    parser.add_argument("--action-hidden-size", type=int, default=64)
    parser.add_argument("--action-learning-rate", type=float, default=0.004)
    parser.add_argument("--policy-epochs", type=int, default=4)
    parser.add_argument("--policy-hidden-size", type=int, default=64)
    parser.add_argument("--policy-learning-rate", type=float, default=0.003)
    parser.add_argument("--entropy-coef", type=float, default=0.008)
    parser.add_argument("--policy-temperature", type=float, default=1.0)
    parser.add_argument("--policy-bias-candidates", default="0.0,0.20,0.40,0.70,1.00")
    parser.add_argument("--device", default="auto")
    parser.add_argument("--trace-seed", type=int, default=20261121)
    args = parser.parse_args()
    return Config(
        train_seeds=parse_ints(args.train_seeds),
        tune_seeds=parse_ints(args.tune_seeds),
        eval_seeds=parse_ints(args.eval_seeds),
        hours=args.hours,
        step_hours=args.step_hours,
        population=args.population,
        epochs=args.epochs,
        hidden_size=args.hidden_size,
        learning_rate=args.learning_rate,
        action_epochs=args.action_epochs,
        action_hidden_size=args.action_hidden_size,
        action_learning_rate=args.action_learning_rate,
        policy_epochs=args.policy_epochs,
        policy_hidden_size=args.policy_hidden_size,
        policy_learning_rate=args.policy_learning_rate,
        entropy_coef=args.entropy_coef,
        policy_temperature=args.policy_temperature,
        policy_bias_candidates=parse_floats(args.policy_bias_candidates),
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "experiment": "ssrm_3d_coupled_crisis_active_policy",
        "verdict": payload["verdict"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
