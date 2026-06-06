#!/usr/bin/env python3
"""Active crisis state/action value control for SSRM-3D.

Report 116 showed that a value selector over whole allocator policies can
improve tune-world choice while transferring worse than the seed/fixed
allocator. This benchmark moves the learned value closer to the actual crisis
control point: active crisis observations plus candidate repair actions.

The value model is trained from simulator step consequences during active
crises. It does not receive the crisis profile name at runtime. The benchmark
is still bounded: environmental/social action heads are supervised, the crisis
candidate set is supplied, and the target is a step-consequence label rather
than full actor-critic return.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import torch

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
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_active_state_value"
VALUE_SEED = 20261521
ACTION_CANDIDATES = (
    "none",
    "sanitize",
    "treat",
    "scout",
    "construct",
    "social_repair",
    "teach",
    "learn",
)
ACTION_FEATURE_SIZE = len(ACTION_CANDIDATES)
VALUE_CONTEXT_NAMES = (
    "elapsed_fraction",
    "remaining_fraction",
    "env_progress",
    "social_progress",
    "env_response_rate",
    "social_response_rate",
    "current_env_fraction",
    "current_social_fraction",
    "candidate_is_environment",
    "candidate_is_social",
    "candidate_is_none",
)
VALUE_INPUT_SIZE = base.FEATURE_COUNT + len(VALUE_CONTEXT_NAMES) + ACTION_FEATURE_SIZE
FIXED_JOINT = (0.14, 0.14, 0.90)


@dataclass(frozen=True)
class Config:
    train_seeds: Sequence[int]
    tune_seeds: Sequence[int]
    eval_seeds: Sequence[int]
    hours: float = 96.0
    step_hours: float = 0.10
    population: int = 14
    epochs: int = 36
    hidden_size: int = 64
    learning_rate: float = 0.004
    action_epochs: int = 52
    action_hidden_size: int = 64
    action_learning_rate: float = 0.004
    value_epochs: int = 80
    value_hidden_size: int = 64
    value_learning_rate: float = 0.003
    max_value_examples: int = 120000
    value_bias_candidates: Sequence[float] = (0.0, 0.75, 1.25, 1.75, 2.50)
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class ActiveValueTrainingRow:
    examples: int
    epochs: int
    final_loss: float
    target_mean: float
    target_std: float
    train_mae: float
    positive_rate: float


@dataclass(frozen=True)
class ActiveValueExampleSummaryRow:
    source_policy: str
    examples: int
    mean_target: float
    positive_rate: float


@dataclass(frozen=True)
class ActiveValueSelectionRow:
    value_bias: float
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
class VerdictRow:
    selected_router: str
    selected_value_bias: float
    value_examples: int
    active_value_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    active_value_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    active_value_resolved_rate: float
    fixed_joint_resolved_rate: float
    return_selected_resolved_rate: float
    active_value_coupled_response: float
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
    supports_active_state_value: bool
    supports_social_environment_dependency: bool
    verdict: str


class ActiveStateValueNet(torch.nn.Module):
    def __init__(self, hidden_size: int) -> None:
        super().__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(VALUE_INPUT_SIZE, hidden_size),
            torch.nn.LayerNorm(hidden_size),
            torch.nn.Tanh(),
            torch.nn.Linear(hidden_size, hidden_size),
            torch.nn.Tanh(),
            torch.nn.Linear(hidden_size, 1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x).squeeze(-1)


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def parse_ints(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def parse_floats(value: str) -> Tuple[float, ...]:
    return tuple(float(part.strip()) for part in value.split(",") if part.strip())


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = [asdict(row) for row in rows]
    if not data:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(data[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def write_js(path: Path, variable: str, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"window.{variable} = {json.dumps(payload, indent=2)};\n", encoding="utf-8")


def candidate_one_hot(action: str) -> List[float]:
    return [1.0 if action == candidate else 0.0 for candidate in ACTION_CANDIDATES]


def response_fractions(action_counts: Dict[str, int], alive_count: int) -> Tuple[float, float]:
    denom = max(1, alive_count)
    env = sum(action_counts.get(action, 0) for action in report111.ENV_RESPONSE_ACTIONS) / denom
    social = sum(action_counts.get(action, 0) for action in report111.SOCIAL_RESPONSE_ACTIONS) / denom
    return env, social


def active_context(
    active: coupled.ActiveCrisis,
    tracker: coupled.CrisisTracker,
    action_counts: Dict[str, int],
    alive_count: int,
    world_time: float,
    action: str,
) -> List[float]:
    elapsed_fraction = clamp((world_time - active.start) / max(1e-6, active.duration))
    remaining_fraction = clamp((active.end - world_time) / max(1e-6, active.duration))
    env_fraction = min(1.0, active.env_progress / active.profile.env_need)
    social_fraction = min(1.0, active.social_progress / active.profile.social_need)
    env_rate = active.env_response_steps / max(1, active.steps)
    social_rate = active.social_response_steps / max(1, active.steps)
    current_env, current_social = response_fractions(action_counts, alive_count)
    return [
        elapsed_fraction,
        remaining_fraction,
        env_fraction,
        social_fraction,
        env_rate,
        social_rate,
        current_env,
        current_social,
        1.0 if action in report111.ENV_RESPONSE_ACTIONS else 0.0,
        1.0 if action in report111.SOCIAL_RESPONSE_ACTIONS else 0.0,
        1.0 if action == "none" else 0.0,
    ]


def value_features(
    features: Sequence[float],
    active: coupled.ActiveCrisis,
    tracker: coupled.CrisisTracker,
    action_counts: Dict[str, int],
    alive_count: int,
    world_time: float,
    action: str,
    ablation: str = "none",
) -> List[float]:
    masked = base.mask_features(list(features), ablation)
    values = masked + active_context(active, tracker, action_counts, alive_count, world_time, action) + candidate_one_hot(action)
    if len(values) != VALUE_INPUT_SIZE:
        raise RuntimeError(f"value feature mismatch: {len(values)} != {VALUE_INPUT_SIZE}")
    return values


def candidate_step_target(
    active: coupled.ActiveCrisis,
    action_counts: Dict[str, int],
    alive_count: int,
    action: str,
    dt: float,
) -> float:
    before_env = min(1.0, active.env_progress / active.profile.env_need)
    before_social = min(1.0, active.social_progress / active.profile.social_need)
    before_coupled = min(before_env, before_social)
    next_counts = dict(action_counts)
    if action != "none":
        next_counts[action] = next_counts.get(action, 0) + 1
    denom = max(1, alive_count)
    env_effort = sum(next_counts.get(item, 0) for item in active.profile.env_actions) / denom
    wrong_env_effort = (
        sum(next_counts.get(item, 0) for item in report111.ENV_RESPONSE_ACTIONS if item not in active.profile.env_actions) / denom
    )
    social_effort = sum(next_counts.get(item, 0) for item in active.profile.social_actions) / denom
    env_after = min(1.0, (active.env_progress + env_effort * dt * 1.70) / active.profile.env_need)
    social_after = min(1.0, (active.social_progress + social_effort * dt * 1.65) / active.profile.social_need)
    coupled_after = min(env_after, social_after)
    unresolved_after = 1.0 - coupled_after
    env_hit = 1.0 if env_effort >= 0.10 else 0.0
    social_hit = 1.0 if social_effort >= 0.09 else 0.0
    balanced = 1.0 - min(1.0, abs(env_after - social_after))
    value = (
        (coupled_after - before_coupled) * 3.2
        + (env_after - before_env) * 0.72
        + (social_after - before_social) * 0.72
        + env_hit * 0.080
        + social_hit * 0.080
        + env_hit * social_hit * 0.130
        + balanced * 0.045
        - unresolved_after * 0.045
        - wrong_env_effort * 0.42
    )
    if action == "none":
        value -= 0.040 + unresolved_after * 0.040
    return value


def add_candidate_examples(
    examples: List[List[float]],
    targets: List[float],
    source_counts: Dict[str, int],
    source_policy: str,
    features: Sequence[float],
    active: coupled.ActiveCrisis,
    tracker: coupled.CrisisTracker,
    action_counts: Dict[str, int],
    alive_count: int,
    world_time: float,
    dt: float,
    max_examples: int,
) -> None:
    if len(examples) >= max_examples:
        return
    for action in ACTION_CANDIDATES:
        if len(examples) >= max_examples:
            return
        examples.append(value_features(features, active, tracker, action_counts, alive_count, world_time, action))
        targets.append(candidate_step_target(active, action_counts, alive_count, action, dt))
        source_counts[source_policy] = source_counts.get(source_policy, 0) + 1


def train_value_model(
    examples: Sequence[Sequence[float]],
    targets: Sequence[float],
    cfg: Config,
    device: torch.device,
) -> Tuple[ActiveStateValueNet, ActiveValueTrainingRow, float, float]:
    torch.manual_seed(VALUE_SEED)
    x = torch.tensor(examples, dtype=torch.float32, device=device)
    y = torch.tensor(targets, dtype=torch.float32, device=device)
    target_mean = float(y.mean().item())
    target_std = float(y.std(unbiased=False).item())
    if target_std < 1e-6:
        target_std = 1.0
    y_norm = (y - target_mean) / target_std
    model = ActiveStateValueNet(cfg.value_hidden_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.value_learning_rate)
    final_loss = 0.0
    batch_size = min(4096, max(128, len(examples)))
    generator = torch.Generator(device="cpu")
    generator.manual_seed(VALUE_SEED)
    for _ in range(cfg.value_epochs):
        order = torch.randperm(len(examples), generator=generator).to(device)
        for start in range(0, len(examples), batch_size):
            index = order[start:start + batch_size]
            optimizer.zero_grad()
            pred = model(x[index])
            loss = torch.nn.functional.mse_loss(pred, y_norm[index])
            loss.backward()
            optimizer.step()
            final_loss = float(loss.item())
    with torch.no_grad():
        pred_obj = model(x) * target_std + target_mean
        train_mae = float(torch.mean(torch.abs(pred_obj - y)).item())
    return model, ActiveValueTrainingRow(
        examples=len(examples),
        epochs=cfg.value_epochs,
        final_loss=final_loss,
        target_mean=target_mean,
        target_std=target_std,
        train_mae=train_mae,
        positive_rate=sum(1 for target in targets if target > 0.0) / max(1, len(targets)),
    ), target_mean, target_std


def predict_candidate_value(
    model: ActiveStateValueNet,
    target_mean: float,
    target_std: float,
    features: Sequence[float],
    active: coupled.ActiveCrisis,
    tracker: coupled.CrisisTracker,
    action_counts: Dict[str, int],
    alive_count: int,
    world_time: float,
    action: str,
    device: torch.device,
    ablation: str,
) -> float:
    values = value_features(features, active, tracker, action_counts, alive_count, world_time, action, ablation)
    with torch.no_grad():
        x = torch.tensor([values], dtype=torch.float32, device=device)
        pred = model(x) * target_std + target_mean
    return float(pred.item())


def active_value_action(
    agent: Agent,
    features: Sequence[float],
    action_counts: Dict[str, int],
    alive_count: int,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    env_states: Dict[str, torch.Tensor],
    social_states: Dict[str, torch.Tensor],
    value_model: ActiveStateValueNet,
    value_bias: float,
    target_mean: float,
    target_std: float,
    device: torch.device,
    ablation: str,
    tracker: coupled.CrisisTracker,
    world: World,
) -> Optional[str]:
    active = tracker.active
    if active is None or value_bias <= 0.0:
        return None
    model_features = torch.tensor([base.mask_features(list(features), ablation)], dtype=torch.float32, device=device)
    with torch.no_grad():
        env_state = env_states.get(agent.ident)
        env_logits, next_env = env_model.step(model_features, env_state)
        if next_env is not None:
            env_states[agent.ident] = next_env.detach()
        social_state = social_states.get(agent.ident)
        social_logits, next_social = social_model.step(model_features, social_state)
        if next_social is not None:
            social_states[agent.ident] = next_social.detach()
    env_action, env_confidence = report113.restricted_prediction(env_logits, report111.DIAGNOSTIC_ENV_ACTIONS)
    social_action, social_confidence = report113.restricted_prediction(social_logits, report111.SOCIAL_RESPONSE_ACTIONS)
    allowed = list(ACTION_CANDIDATES)
    if ablation == "environment":
        allowed = [action for action in allowed if action not in report111.ENV_RESPONSE_ACTIONS]
    if ablation == "social_culture":
        allowed = [action for action in allowed if action not in report111.SOCIAL_RESPONSE_ACTIONS]
    scored: List[Tuple[str, float]] = []
    for action in allowed:
        score = predict_candidate_value(
            value_model,
            target_mean,
            target_std,
            features,
            active,
            tracker,
            action_counts,
            alive_count,
            world.time,
            action,
            device,
            ablation,
        )
        if action == env_action:
            score += env_confidence * 0.055
        if action == social_action:
            score += social_confidence * 0.055
        if action == "none":
            score += 0.010
        scored.append((action, score * value_bias))
    best_action, best_score = max(scored, key=lambda item: item[1])
    none_score = next((score for action, score in scored if action == "none"), -1e9)
    if best_action == "none" or best_score <= none_score + 0.010:
        return None
    return best_action


def collect_value_examples(
    cfg: Config,
    base_model: base.ControllerNet,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[List[List[float]], List[float], List[ActiveValueExampleSummaryRow]]:
    examples: List[List[float]] = []
    targets: List[float] = []
    source_counts: Dict[str, int] = {}
    source_targets: Dict[str, List[float]] = {}
    policies = (
        ("return_selected", 0.0, 0.0, 0.0),
        ("fixed_joint", FIXED_JOINT[0], FIXED_JOINT[1], FIXED_JOINT[2]),
        ("high_env_joint", 0.20, 0.14, 1.10),
        ("high_social_joint", 0.14, 0.20, 1.10),
    )
    for policy_name, env_quota, social_quota, strength in policies:
        for seed in cfg.train_seeds:
            if len(examples) >= cfg.max_value_examples:
                break
            run_collection_episode(
                seed,
                cfg,
                policy_name,
                base_model,
                env_model,
                social_model,
                device,
                router,
                env_quota,
                social_quota,
                strength,
                examples,
                targets,
                source_counts,
                source_targets,
            )
    summary = [
        ActiveValueExampleSummaryRow(
            source_policy=source,
            examples=count,
            mean_target=mean(source_targets.get(source, [])),
            positive_rate=sum(1 for target in source_targets.get(source, []) if target > 0.0) / max(1, len(source_targets.get(source, []))),
        )
        for source, count in sorted(source_counts.items())
    ]
    return examples, targets, summary


def run_collection_episode(
    seed: int,
    cfg: Config,
    source_policy: str,
    model: base.ControllerNet,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
    env_quota: float,
    social_quota: float,
    coordinator_strength: float,
    examples: List[List[float]],
    targets: List[float],
    source_counts: Dict[str, int],
    source_targets: Dict[str, List[float]],
) -> None:
    condition = CONDITIONS[0]
    rng = random.Random(seed * 127 + sum(ord(ch) for ch in source_policy) + 6151)
    agents = make_agents(rng, cfg.population)
    world = coupled.prepare_world(rng, cfg)
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    env_states: Dict[str, torch.Tensor] = {}
    social_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
    while world.time < cfg.hours - 1e-9 and len(examples) < cfg.max_value_examples:
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
            if active is not None:
                before = len(targets)
                add_candidate_examples(
                    examples,
                    targets,
                    source_counts,
                    source_policy,
                    features,
                    active,
                    tracker,
                    action_counts,
                    len(living(agents)),
                    current_world.time,
                    dt,
                    cfg.max_value_examples,
                )
                source_targets.setdefault(source_policy, []).extend(targets[before:])
            if source_policy == "return_selected":
                action = learned_policy_action(agent, features, model, recurrent_states, router, device, "none")
            else:
                action = report113.coordinator_action(
                    agent,
                    features,
                    action_counts,
                    len(living(agents)),
                    env_model,
                    social_model,
                    env_states,
                    social_states,
                    env_quota,
                    social_quota,
                    coordinator_strength,
                    device,
                    "none",
                )
                if action is None:
                    action = learned_policy_action(agent, features, model, recurrent_states, router, device, "none")
            action_counts[action] = action_counts.get(action, 0) + 1
            return action

        base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
        report111.update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
        coupled.complete_crisis_if_due(world, agents, tracker, events)
    if tracker.active is not None:
        coupled.complete_crisis_if_due(world, agents, tracker, events)


def learned_policy_action(
    agent: Agent,
    features: Sequence[float],
    model: base.ControllerNet,
    recurrent_states: Dict[str, torch.Tensor],
    router: report105.PressureRouter,
    device: torch.device,
    ablation: str,
) -> str:
    model_features = torch.tensor([base.mask_features(list(features), ablation)], dtype=torch.float32, device=device)
    with torch.no_grad():
        if model.architecture == "gru":
            state = recurrent_states.get(agent.ident)
            logits, next_state = model.step(model_features, state)
            if next_state is not None:
                recurrent_states[agent.ident] = next_state.detach()
        else:
            logits, _ = model.step(model_features, None)
        logits = logits + report105.router_bias(features, router, device, logits.dtype, ablation)
    return base.INDEX_TO_ACTION[int(logits.argmax(dim=-1).item())]


def run_active_value_episode(
    seed: int,
    cfg: Config,
    controller: str,
    model: Optional[base.ControllerNet],
    env_model: Optional[base.ControllerNet],
    social_model: Optional[base.ControllerNet],
    value_model: Optional[ActiveStateValueNet],
    target_mean: float,
    target_std: float,
    device: torch.device,
    router: report105.PressureRouter,
    value_bias: float = 0.0,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, Trace, coupled.CrisisTracker]:
    if controller == "active_state_value_gru" and (model is None or env_model is None or social_model is None or value_model is None):
        raise ValueError("active_state_value_gru requires base, action, and value models")
    condition = CONDITIONS[1] if controller == "reactive" else CONDITIONS[0]
    rng = random.Random(seed * 127 + sum(ord(ch) for ch in controller + router.name + ablation) + int(value_bias * 1000) + 6173)
    agents = make_agents(rng, cfg.population)
    world = coupled.prepare_world(rng, cfg)
    baseline = base.initial_baseline(world, cfg.population)
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    env_states: Dict[str, torch.Tensor] = {}
    social_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
    trace_out = Trace(seed=seed, condition=f"{controller}:{router.name}:value_{value_bias:g}:{ablation}")
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
            elif controller == "fixed_joint_gru" and active is not None:
                action = report113.coordinator_action(
                    agent,
                    features,
                    action_counts,
                    len(living(agents)),
                    env_model,
                    social_model,
                    env_states,
                    social_states,
                    FIXED_JOINT[0],
                    FIXED_JOINT[1],
                    FIXED_JOINT[2],
                    device,
                    ablation,
                )
                if action is None:
                    action = learned_policy_action(agent, features, model, recurrent_states, router, device, ablation)
            elif controller == "active_state_value_gru" and active is not None:
                action = active_value_action(
                    agent,
                    features,
                    action_counts,
                    len(living(agents)),
                    env_model,
                    social_model,
                    env_states,
                    social_states,
                    value_model,
                    value_bias,
                    target_mean,
                    target_std,
                    device,
                    ablation,
                    tracker,
                    current_world,
                )
                if action is None:
                    action = learned_policy_action(agent, features, model, recurrent_states, router, device, ablation)
            else:
                action = learned_policy_action(agent, features, model, recurrent_states, router, device, ablation)
            if controller in {"active_state_value_gru", "fixed_joint_gru"} and active is not None:
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
    objective = total * 0.50 + crisis * 1.12 + resolved * 0.62 + coupled_response * 0.72 - damage * 0.25
    return total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective


def select_value_bias(
    cfg: Config,
    model: base.ControllerNet,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    value_model: ActiveStateValueNet,
    target_mean: float,
    target_std: float,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[float, List[ActiveValueSelectionRow]]:
    rows: List[ActiveValueSelectionRow] = []
    best_bias = 0.0
    best_objective = -1e9
    for bias in cfg.value_bias_candidates:
        eval_rows = [
            run_active_value_episode(
                seed,
                cfg,
                "active_state_value_gru",
                model,
                env_model,
                social_model,
                value_model,
                target_mean,
                target_std,
                device,
                router,
                value_bias=bias,
            )[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_objective = objective
            best_bias = bias
        rows.append(ActiveValueSelectionRow(
            value_bias=bias,
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
    return best_bias, [replace(row, selected=(row.value_bias == best_bias)) for row in rows]


def row_lookup(summary: Sequence[coupled.SummaryRow], controller: str, ablation: str) -> coupled.SummaryRow:
    return coupled.row_lookup(summary, controller, ablation)


def ablations_from_summary(summary: Sequence[coupled.SummaryRow]) -> List[coupled.AblationRow]:
    base_row = row_lookup(summary, "active_state_value_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = row_lookup(summary, "active_state_value_gru", ablation)
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
    value_training: ActiveValueTrainingRow,
) -> VerdictRow:
    active = row_lookup(summary, "active_state_value_gru", "none")
    fixed = row_lookup(summary, "fixed_joint_gru", "none")
    returned = row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    supports_return = (
        selected_bias > 0.0
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
        social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    supports_active = supports_return and supports_fixed
    return VerdictRow(
        selected_router=router.name,
        selected_value_bias=selected_bias,
        value_examples=value_training.examples,
        active_value_total_score=active.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        active_value_crisis_score=active.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        active_value_resolved_rate=active.mean_resolved_rate,
        fixed_joint_resolved_rate=fixed.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        active_value_coupled_response=active.mean_coupled_response_rate,
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
        supports_active_state_value=supports_active,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_active and supports_dependency else "partial_or_failed",
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
            20261531,
        )
        social_model, social_training = report113.train_action_model(
            cfg,
            device,
            "social",
            social_sequences,
            social_labels,
            flags,
            20261532,
        )
        value_examples, value_targets, example_summary = collect_value_examples(
            cfg,
            models["gru"],
            env_model,
            social_model,
            device,
            selected_router,
        )
        value_model, value_training, target_mean, target_std = train_value_model(value_examples, value_targets, cfg, device)
        selected_bias, value_selection = select_value_bias(
            cfg,
            models["gru"],
            env_model,
            social_model,
            value_model,
            target_mean,
            target_std,
            device,
            selected_router,
        )

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
                row, maybe_trace, tracker = run_active_value_episode(
                    seed,
                    cfg,
                    controller,
                    model,
                    env_model,
                    social_model,
                    value_model,
                    target_mean,
                    target_std,
                    device,
                    router,
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:{controller}:none"] = tracker.response_log
                if maybe_trace.frames:
                    trace_out = maybe_trace
            fixed_row, _, fixed_tracker = run_active_value_episode(
                seed,
                cfg,
                "fixed_joint_gru",
                models["gru"],
                env_model,
                social_model,
                value_model,
                target_mean,
                target_std,
                device,
                selected_router,
            )
            eval_rows.append(fixed_row)
            crisis_logs[f"{seed}:fixed_joint_gru:none"] = fixed_tracker.response_log
            active_row, maybe_trace, tracker = run_active_value_episode(
                seed,
                cfg,
                "active_state_value_gru",
                models["gru"],
                env_model,
                social_model,
                value_model,
                target_mean,
                target_std,
                device,
                selected_router,
                value_bias=selected_bias,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(active_row)
            crisis_logs[f"{seed}:active_state_value_gru:none"] = tracker.response_log
            if maybe_trace.frames:
                trace_out = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker = run_active_value_episode(
                    seed,
                    cfg,
                    "active_state_value_gru",
                    models["gru"],
                    env_model,
                    social_model,
                    value_model,
                    target_mean,
                    target_std,
                    device,
                    selected_router,
                    value_bias=selected_bias,
                    ablation=ablation,
                )
                eval_rows.append(replace(row, ablation=ablation))
                crisis_logs[f"{seed}:active_state_value_gru:{ablation}"] = tracker.response_log

    summary = coupled.summarize(eval_rows)
    ablations = ablations_from_summary(summary)
    verdict = transfer_verdict(summary, ablations, selected_router, selected_bias, schedules, value_training)
    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "active_state_value_gru", "frames": []}
    trace_payload["condition"] = "active_state_value_gru"
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
            "value_epochs": cfg.value_epochs,
            "value_hidden_size": cfg.value_hidden_size,
            "max_value_examples": cfg.max_value_examples,
            "value_bias_candidates": list(cfg.value_bias_candidates),
            "device": cfg.device,
            "trace_seed": cfg.trace_seed,
        },
        "value_context_names": list(VALUE_CONTEXT_NAMES),
        "action_candidates": list(ACTION_CANDIDATES),
        "schedule": [asdict(row) for row in schedules],
        "router_selection": [asdict(row) for row in router_selection],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "value_training": asdict(value_training),
        "value_example_summary": [asdict(row) for row in example_summary],
        "value_selection": [asdict(row) for row in value_selection],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace_payload,
        "crisis_logs": crisis_logs,
        "notes": {
            "claim": "active crisis state/action value labels can guide repair choices during coupled crises",
            "not_claimed": "actor-critic reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
            "remaining_structure": "candidate repair actions are supplied, action heads are supervised, and value labels are per-step simulator consequences rather than full delayed-return policy gradients",
        },
    }
    rows_to_csv(Path(f"{PREFIX}_schedule.csv"), schedules)
    rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    rows_to_csv(Path(f"{PREFIX}_action_training.csv"), [env_training, social_training])
    rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    rows_to_csv(Path(f"{PREFIX}_value_example_summary.csv"), example_summary)
    rows_to_csv(Path(f"{PREFIX}_value_training.csv"), [value_training])
    rows_to_csv(Path(f"{PREFIX}_value_selection.csv"), value_selection)
    rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    write_json(Path(f"{PREFIX}_results.json"), payload)
    write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_ACTIVE_STATE_VALUE_RESULTS", payload)
    write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_ACTIVE_STATE_VALUE_TRACE", trace_payload)
    return payload


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-seeds", default="20260911,20260912,20260913,20260914,20260915,20260916")
    parser.add_argument("--tune-seeds", default="20261111,20261112,20261113")
    parser.add_argument("--eval-seeds", default="20261121,20261122,20261123,20261124,20261125")
    parser.add_argument("--hours", type=float, default=96.0)
    parser.add_argument("--step-hours", type=float, default=0.10)
    parser.add_argument("--population", type=int, default=14)
    parser.add_argument("--epochs", type=int, default=36)
    parser.add_argument("--hidden-size", type=int, default=64)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--action-epochs", type=int, default=52)
    parser.add_argument("--action-hidden-size", type=int, default=64)
    parser.add_argument("--action-learning-rate", type=float, default=0.004)
    parser.add_argument("--value-epochs", type=int, default=80)
    parser.add_argument("--value-hidden-size", type=int, default=64)
    parser.add_argument("--value-learning-rate", type=float, default=0.003)
    parser.add_argument("--max-value-examples", type=int, default=120000)
    parser.add_argument("--value-bias-candidates", default="0.0,0.75,1.25,1.75,2.50")
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
        value_epochs=args.value_epochs,
        value_hidden_size=args.value_hidden_size,
        value_learning_rate=args.value_learning_rate,
        max_value_examples=args.max_value_examples,
        value_bias_candidates=parse_floats(args.value_bias_candidates),
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "value_training": payload["value_training"],
        "value_selection": payload["value_selection"],
        "verdict": payload["verdict"],
        "summary": payload["summary"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
