#!/usr/bin/env python3
"""Active consequence optimization for SSRM-3D coupled crises.

Report 129 showed that direct supervised labels from cloned counterfactual
windows still fail online transfer. Validation selected direct bias 0.0, and
held-out crisis/coupled repair remained collapsed.

This benchmark tests the next narrower claim: initialize from the strongest
post-planner learned recovery baseline, then fine-tune that same recurrent
crisis policy from consequences produced by its own closed-loop interventions.

The benchmark remains bounded. The crisis action candidates are supplied, the
base controller is imitation trained, the crisis families are structured, and
the reward is an abstract simulator return. This is not open-ended
civilization, subjective consciousness, or real-world competence.
"""

from __future__ import annotations

import argparse
import copy
import json
import random
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import torch
import torch.nn.functional as F

import ssrm_3d_coupled_crisis_active_policy_controller as report119
import ssrm_3d_coupled_crisis_active_state_value_controller as report117
import ssrm_3d_coupled_crisis_consequence_recovery_controller as report126
import ssrm_3d_coupled_crisis_joint_arbitration_controller as report113
import ssrm_3d_coupled_crisis_memory_policy_controller as report121
import ssrm_3d_coupled_crisis_min_channel_planner_controller as report123
import ssrm_3d_coupled_crisis_planner_distillation_controller as report124
import ssrm_3d_coupled_crisis_randomized_transfer_controller as report114
import ssrm_3d_coupled_crisis_rollout_window_controller as report111
import ssrm_3d_coupled_social_environment_maturation_controller as coupled
import ssrm_3d_learned_multiday_maturation_controller as base
import ssrm_3d_return_selected_multiday_maturation_controller as report105
from ssrm_maturation.agents import make_agents
from ssrm_maturation.benchmark import Trace
from ssrm_maturation.environment import living
from ssrm_maturation.models import CONDITIONS, Agent, Condition, World


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_active_consequence_optimization"
ACTIVE_CONSEQUENCE_SEED = 20262517
ACTION_CANDIDATES = report126.ACTION_CANDIDATES
ACTION_TO_INDEX = report126.ACTION_TO_INDEX


@dataclass(frozen=True)
class Config:
    train_seeds: Sequence[int]
    tune_seeds: Sequence[int]
    eval_seeds: Sequence[int]
    hours: float = 96.0
    step_hours: float = 0.10
    population: int = 14
    epochs: int = 14
    hidden_size: int = 48
    learning_rate: float = 0.004
    action_epochs: int = 18
    action_hidden_size: int = 48
    action_learning_rate: float = 0.004
    consequence_epochs: int = 8
    consequence_hidden_size: int = 48
    consequence_learning_rate: float = 0.003
    consequence_return_scale: float = 1.15
    student_iterations: int = 0
    student_collection_bias: float = 0.70
    active_epochs: int = 3
    active_learning_rate: float = 0.0018
    active_entropy_coef: float = 0.006
    active_training_bias: float = 0.40
    active_return_scale: float = 1.0
    action_value_epochs: int = 8
    action_value_hidden_size: int = 64
    action_value_learning_rate: float = 0.003
    policy_temperature: float = 1.0
    policy_bias_candidates: Sequence[float] = (0.0, 0.40, 0.80)
    active_bias_candidates: Sequence[float] = (0.0, 0.40, 0.80)
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class ActiveConsequenceTrainingRow:
    episodes: int
    crises: int
    epochs: int
    final_loss: float
    mean_return: float
    return_std: float
    moving_baseline: float
    mean_sequence_length: float
    mean_entropy: float
    active_training_bias: float
    active_entropy_coef: float
    active_learning_rate: float
    device_used: str
    parameter_count: int


@dataclass(frozen=True)
class ActiveConsequenceSelectionRow:
    active_bias: float
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
class ActionValueTrainingRow:
    source_sequences: int
    examples: int
    epochs: int
    final_loss: float
    mean_target_return: float
    target_return_std: float
    positive_target_rate: float
    train_mae: float
    weighted_train_mae: float
    mean_weight: float
    max_weight: float
    env_action_fraction: float
    social_action_fraction: float
    none_fraction: float
    device_used: str
    parameter_count: int


@dataclass(frozen=True)
class ActionValueSelectionRow:
    action_value_bias: float
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
class ActiveConsequenceVerdictRow:
    selected_router: str
    selected_planner: str
    selected_consequence_bias: float
    selected_active_bias: float
    selected_action_value_bias: float
    source_sequences: int
    student_sequences: int
    aggregate_examples: int
    active_training_crises: int
    consequence_train_accuracy: float
    consequence_weighted_accuracy: float
    active_mean_return: float
    action_value_train_mae: float
    action_value_weighted_train_mae: float
    active_consequence_total_score: float
    action_value_total_score: float
    consequence_total_score: float
    min_channel_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    active_consequence_crisis_score: float
    action_value_crisis_score: float
    consequence_crisis_score: float
    min_channel_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    active_consequence_resolved_rate: float
    action_value_resolved_rate: float
    consequence_resolved_rate: float
    min_channel_resolved_rate: float
    fixed_joint_resolved_rate: float
    return_selected_resolved_rate: float
    active_consequence_coupled_response: float
    action_value_coupled_response: float
    consequence_coupled_response: float
    min_channel_coupled_response: float
    fixed_joint_coupled_response: float
    return_selected_coupled_response: float
    active_gain_over_consequence: float
    active_gain_over_return_selected: float
    action_value_gain_over_consequence: float
    action_value_gain_over_return_selected: float
    active_gap_to_teacher: float
    action_value_gap_to_teacher: float
    active_gap_to_fixed_joint: float
    action_value_gap_to_fixed_joint: float
    social_culture_crisis_loss: float
    environment_crisis_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    mean_crisis_count: float
    supports_active_consequence_optimization: bool
    supports_learned_action_value_control: bool
    supports_teacher_transfer: bool
    supports_social_environment_dependency: bool
    verdict: str


class CrisisActionValueNet(torch.nn.Module):
    def __init__(self, hidden_size: int) -> None:
        super().__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(report119.POLICY_INPUT_SIZE, hidden_size),
            torch.nn.LayerNorm(hidden_size),
            torch.nn.Tanh(),
            torch.nn.Linear(hidden_size, hidden_size),
            torch.nn.Tanh(),
            torch.nn.Linear(hidden_size, len(ACTION_CANDIDATES)),
        )

    def forward_sequence(
        self,
        x: torch.Tensor,
        state: Optional[torch.Tensor] = None,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        batch, steps, width = x.shape
        values = self.net(x.reshape(batch * steps, width)).reshape(batch, steps, len(ACTION_CANDIDATES))
        dummy_state = torch.zeros(1, batch, 1, dtype=x.dtype, device=x.device)
        return values, dummy_state

    def step(
        self,
        x: torch.Tensor,
        state: Optional[torch.Tensor],
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        values, next_state = self.forward_sequence(x, state)
        return values[:, -1, :], next_state


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


def bounded(value: float, low: float = -2.5, high: float = 3.5) -> float:
    return max(low, min(high, value))


def active_consequence_return(active: coupled.ActiveCrisis, damage_delta: float, scale: float) -> float:
    env_fraction, social_fraction, coupled_fraction = report119.crisis_fraction(active)
    resolved = 1.0 if coupled_fraction >= 0.92 else 0.0
    env_rate = active.env_response_steps / max(1, active.steps)
    social_rate = active.social_response_steps / max(1, active.steps)
    coupled_rate = active.coupled_response_steps / max(1, active.steps)
    min_rate = min(env_rate, social_rate)
    progress_balance = 1.0 - min(1.0, abs(env_fraction - social_fraction))
    response_balance = 1.0 - min(1.0, abs(env_rate - social_rate))
    one_channel = max(env_rate, social_rate) if min_rate < 0.05 else 0.0
    unresolved = max(0.0, 0.92 - coupled_fraction)
    reward = (
        coupled_fraction * 1.70
        + resolved * 1.10
        + coupled_rate * 1.15
        + min_rate * 0.70
        + progress_balance * 0.22
        + response_balance * 0.16
        - unresolved * 1.05
        - one_channel * 1.00
        - max(0.0, damage_delta) * 1.45
    )
    return bounded(reward * scale)


def sample_active_candidate(
    model: report121.CrisisMemoryPolicyNet,
    features: Sequence[float],
    active: coupled.ActiveCrisis,
    action_counts: Dict[str, int],
    alive_count: int,
    world_time: float,
    state: Optional[torch.Tensor],
    device: torch.device,
    cfg: Config,
) -> Tuple[str, List[float], int, float, torch.Tensor]:
    values = report119.policy_features(features, active, action_counts, alive_count, world_time, "none")
    with torch.no_grad():
        x = torch.tensor([[values]], dtype=torch.float32, device=device)
        logits, next_state = model.step(x, state)
        logits = report119.masked_logits(
            logits / max(0.05, cfg.policy_temperature),
            "none",
            cfg.active_training_bias,
        )
        dist = torch.distributions.Categorical(logits=logits.squeeze(0))
        index = dist.sample()
        entropy = float(dist.entropy().detach().cpu().item())
    action_index = int(index.item())
    return ACTION_CANDIDATES[action_index], values, action_index, entropy, next_state.detach()


def update_active_model_from_sequence(
    model: report121.CrisisMemoryPolicyNet,
    optimizer: torch.optim.Optimizer,
    sequence: Sequence[Tuple[List[float], int]],
    reward: float,
    moving_baseline: float,
    cfg: Config,
    device: torch.device,
) -> float:
    if not sequence:
        return 0.0
    x = torch.tensor([[item[0] for item in sequence]], dtype=torch.float32, device=device)
    actions = torch.tensor([item[1] for item in sequence], dtype=torch.long, device=device)
    logits, _ = model.forward_sequence(x)
    logits = report119.masked_logits(
        logits.squeeze(0) / max(0.05, cfg.policy_temperature),
        "none",
        cfg.active_training_bias,
    )
    dist = torch.distributions.Categorical(logits=logits)
    advantage = reward - moving_baseline
    policy_loss = -float(advantage) * dist.log_prob(actions).mean()
    entropy_loss = dist.entropy().mean()
    loss = policy_loss - cfg.active_entropy_coef * entropy_loss
    optimizer.zero_grad()
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), 2.0)
    optimizer.step()
    return float(loss.detach().cpu().item())


def run_active_training_episode(
    seed: int,
    cfg: Config,
    base_model: base.ControllerNet,
    active_model: report121.CrisisMemoryPolicyNet,
    optimizer: torch.optim.Optimizer,
    device: torch.device,
    router: report105.PressureRouter,
    moving_baseline: float,
) -> Tuple[int, List[float], List[float], List[int], float, float]:
    rng = random.Random(seed * 271 + ACTIVE_CONSEQUENCE_SEED)
    agents = make_agents(rng, cfg.population)
    world = coupled.prepare_world(rng, cfg)
    condition = CONDITIONS[0]
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
    active_key: Optional[float] = None
    memory_state: Optional[torch.Tensor] = None
    pending_sequence: List[Tuple[List[float], int]] = []
    pending_damage_start = 0.0
    returns: List[float] = []
    entropies: List[float] = []
    sequence_lengths: List[int] = []
    final_loss = 0.0
    crises = 0
    active_model.train()

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        action_counts: Dict[str, int] = {}
        coupled.maybe_start_crisis(world, tracker, rng, events)
        if tracker.active is not None and active_key != tracker.active.start:
            active_key = tracker.active.start
            memory_state = None
            pending_sequence = []
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
            nonlocal memory_state
            active = tracker.active
            action: Optional[str] = None
            if active is not None and current_world.time >= 12.0:
                action, values, action_index, entropy, next_state = sample_active_candidate(
                    active_model,
                    features,
                    active,
                    action_counts,
                    len(living(agents)),
                    current_world.time,
                    memory_state,
                    device,
                    cfg,
                )
                memory_state = next_state
                pending_sequence.append((values, action_index))
                entropies.append(entropy)
            if action is None or action == "none":
                action = report117.learned_policy_action(agent, features, base_model, recurrent_states, router, device, "none")
            action_counts[action] = action_counts.get(action, 0) + 1
            return action

        base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
        active_before_completion = tracker.active
        report111.update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
        coupled.complete_crisis_if_due(world, agents, tracker, events)
        if active_before_completion is not None and tracker.active is None and pending_sequence:
            reward = active_consequence_return(
                active_before_completion,
                tracker.damage_integral - pending_damage_start,
                cfg.active_return_scale,
            )
            returns.append(reward)
            crises += 1
            sequence_lengths.append(len(pending_sequence))
            final_loss = update_active_model_from_sequence(
                active_model,
                optimizer,
                pending_sequence,
                reward,
                moving_baseline,
                cfg,
                device,
            )
            moving_baseline = moving_baseline * 0.86 + reward * 0.14
            pending_sequence = []
            memory_state = None
            active_key = None
    if tracker.active is not None and pending_sequence:
        active_before_completion = tracker.active
        coupled.complete_crisis_if_due(world, agents, tracker, events)
        reward = active_consequence_return(
            active_before_completion,
            tracker.damage_integral - pending_damage_start,
            cfg.active_return_scale,
        )
        returns.append(reward)
        crises += 1
        sequence_lengths.append(len(pending_sequence))
        final_loss = update_active_model_from_sequence(
            active_model,
            optimizer,
            pending_sequence,
            reward,
            moving_baseline,
            cfg,
            device,
        )
        moving_baseline = moving_baseline * 0.86 + reward * 0.14
    return crises, returns, entropies, sequence_lengths, moving_baseline, final_loss


def train_active_consequence_model(
    cfg: Config,
    base_model: base.ControllerNet,
    consequence_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[report121.CrisisMemoryPolicyNet, ActiveConsequenceTrainingRow]:
    torch.manual_seed(ACTIVE_CONSEQUENCE_SEED)
    active_model = copy.deepcopy(consequence_model).to(device)
    optimizer = torch.optim.Adam(active_model.parameters(), lr=cfg.active_learning_rate)
    moving_baseline = 0.0
    all_returns: List[float] = []
    all_entropies: List[float] = []
    all_lengths: List[int] = []
    total_crises = 0
    episodes = 0
    final_loss = 0.0
    for epoch in range(cfg.active_epochs):
        for seed in cfg.train_seeds:
            crises, returns, entropies, lengths, moving_baseline, final_loss = run_active_training_episode(
                seed + epoch * 1019,
                cfg,
                base_model,
                active_model,
                optimizer,
                device,
                router,
                moving_baseline,
            )
            total_crises += crises
            all_returns.extend(returns)
            all_entropies.extend(entropies)
            all_lengths.extend(lengths)
            episodes += 1
    active_model.eval()
    return active_model, ActiveConsequenceTrainingRow(
        episodes=episodes,
        crises=total_crises,
        epochs=cfg.active_epochs,
        final_loss=final_loss,
        mean_return=mean(all_returns),
        return_std=stdev(all_returns),
        moving_baseline=moving_baseline,
        mean_sequence_length=mean(all_lengths),
        mean_entropy=mean(all_entropies),
        active_training_bias=cfg.active_training_bias,
        active_entropy_coef=cfg.active_entropy_coef,
        active_learning_rate=cfg.active_learning_rate,
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in active_model.parameters()),
    )


def train_action_value_model(
    cfg: Config,
    sequences: Sequence[report126.ConsequenceSequence],
    device: torch.device,
) -> Tuple[CrisisActionValueNet, ActionValueTrainingRow]:
    examples: List[Tuple[List[float], int, float, float]] = []
    action_counts = {action: 0 for action in ACTION_CANDIDATES}
    sequence_returns = [item.sequence_return for item in sequences]
    for item in sequences:
        weight = report126.sequence_weight(item.sequence_return, cfg.consequence_return_scale)
        for values, action_index in item.sequence:
            examples.append((list(values), action_index, item.sequence_return, weight))
            action_counts[ACTION_CANDIDATES[action_index]] += 1
    if not examples:
        raise RuntimeError("no action-value examples collected")

    torch.manual_seed(ACTIVE_CONSEQUENCE_SEED + 97)
    model = CrisisActionValueNet(cfg.action_value_hidden_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.action_value_learning_rate)
    x = torch.tensor([item[0] for item in examples], dtype=torch.float32, device=device)
    actions = torch.tensor([item[1] for item in examples], dtype=torch.long, device=device)
    targets = torch.tensor([item[2] for item in examples], dtype=torch.float32, device=device)
    weights = torch.tensor([item[3] for item in examples], dtype=torch.float32, device=device)
    batch_size = min(8192, max(512, len(examples)))
    final_loss = 0.0
    for _ in range(cfg.action_value_epochs):
        permutation = torch.randperm(x.shape[0], device=device)
        for start in range(0, x.shape[0], batch_size):
            index = permutation[start:start + batch_size]
            batch_x = x[index]
            batch_actions = actions[index]
            batch_targets = targets[index]
            batch_weights = weights[index]
            predicted = model.net(batch_x).gather(1, batch_actions.unsqueeze(1)).squeeze(1)
            per_item = F.smooth_l1_loss(predicted, batch_targets, reduction="none")
            loss = (per_item * batch_weights).mean()
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 2.0)
            optimizer.step()
            final_loss = float(loss.detach().cpu().item())

    model.eval()
    with torch.no_grad():
        predicted = model.net(x).gather(1, actions.unsqueeze(1)).squeeze(1)
        errors = torch.abs(predicted - targets)
        train_mae = float(errors.mean().detach().cpu().item())
        weighted_mae = float(((errors * weights).sum() / weights.sum().clamp_min(1e-6)).detach().cpu().item())
    total_actions = max(1, sum(action_counts.values()))
    env_count = sum(action_counts.get(action, 0) for action in report111.ENV_RESPONSE_ACTIONS)
    social_count = sum(action_counts.get(action, 0) for action in report111.SOCIAL_RESPONSE_ACTIONS)
    return model, ActionValueTrainingRow(
        source_sequences=len(sequences),
        examples=len(examples),
        epochs=cfg.action_value_epochs,
        final_loss=final_loss,
        mean_target_return=mean(sequence_returns),
        target_return_std=stdev(sequence_returns),
        positive_target_rate=sum(1 for value in sequence_returns if value > 0.0) / max(1, len(sequence_returns)),
        train_mae=train_mae,
        weighted_train_mae=weighted_mae,
        mean_weight=float(weights.mean().detach().cpu().item()),
        max_weight=float(weights.max().detach().cpu().item()),
        env_action_fraction=env_count / total_actions,
        social_action_fraction=social_count / total_actions,
        none_fraction=action_counts.get("none", 0) / total_actions,
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in model.parameters()),
    )


def run_active_consequence_episode(
    seed: int,
    cfg: Config,
    base_model: base.ControllerNet,
    active_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
    active_bias: float,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, Trace, coupled.CrisisTracker]:
    row, trace_out, tracker = report124.run_distilled_episode(
        seed,
        cfg,
        base_model,
        active_model,
        device,
        router,
        active_bias,
        ablation=ablation,
        trace=trace,
    )
    row = replace(row, controller="active_consequence_optimized_gru")
    trace_out.condition = f"active_consequence_optimized_gru:{router.name}:bias_{active_bias:g}:{ablation}"
    return row, trace_out, tracker


def run_action_value_episode(
    seed: int,
    cfg: Config,
    base_model: base.ControllerNet,
    action_value_model: CrisisActionValueNet,
    device: torch.device,
    router: report105.PressureRouter,
    action_value_bias: float,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, Trace, coupled.CrisisTracker]:
    row, trace_out, tracker = report124.run_distilled_episode(
        seed,
        cfg,
        base_model,
        action_value_model,
        device,
        router,
        action_value_bias,
        ablation=ablation,
        trace=trace,
    )
    row = replace(row, controller="active_consequence_value_gru")
    trace_out.condition = f"active_consequence_value_gru:{router.name}:bias_{action_value_bias:g}:{ablation}"
    return row, trace_out, tracker


def selection_objective(rows: Sequence[coupled.EvalRow]) -> Tuple[float, float, float, float, float, float, float, float, float]:
    return report126.selection_objective(rows)


def select_active_bias(
    cfg: Config,
    base_model: base.ControllerNet,
    active_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[float, List[ActiveConsequenceSelectionRow]]:
    rows: List[ActiveConsequenceSelectionRow] = []
    best_bias = 0.0
    best_objective = -1e9
    for bias in cfg.active_bias_candidates:
        eval_rows = [
            run_active_consequence_episode(seed, cfg, base_model, active_model, device, router, bias)[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_objective = objective
            best_bias = bias
        rows.append(ActiveConsequenceSelectionRow(
            active_bias=bias,
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
    return best_bias, [replace(row, selected=(row.active_bias == best_bias)) for row in rows]


def select_action_value_bias(
    cfg: Config,
    base_model: base.ControllerNet,
    action_value_model: CrisisActionValueNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[float, List[ActionValueSelectionRow]]:
    rows: List[ActionValueSelectionRow] = []
    best_bias = 0.0
    best_objective = -1e9
    for bias in cfg.active_bias_candidates:
        eval_rows = [
            run_action_value_episode(seed, cfg, base_model, action_value_model, device, router, bias)[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_objective = objective
            best_bias = bias
        rows.append(ActionValueSelectionRow(
            action_value_bias=bias,
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
    return best_bias, [replace(row, selected=(row.action_value_bias == best_bias)) for row in rows]


def ablations_from_summary(summary: Sequence[coupled.SummaryRow]) -> List[coupled.AblationRow]:
    base_row = coupled.row_lookup(summary, "active_consequence_value_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = coupled.row_lookup(summary, "active_consequence_value_gru", ablation)
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
    planner: report123.PlannerCandidate,
    consequence_bias: float,
    active_bias: float,
    action_value_bias: float,
    schedules: Sequence[report114.ScheduleRow],
    consequence_training_rows: Sequence[report126.ConsequenceTrainingRow],
    source_summary: Sequence[report126.ConsequenceSourceRow],
    active_training: ActiveConsequenceTrainingRow,
    action_value_training: ActionValueTrainingRow,
) -> ActiveConsequenceVerdictRow:
    active = coupled.row_lookup(summary, "active_consequence_optimized_gru", "none")
    action_value = coupled.row_lookup(summary, "active_consequence_value_gru", "none")
    consequence = coupled.row_lookup(summary, "consequence_recovery_gru", "none")
    teacher = coupled.row_lookup(summary, "min_channel_planner_gru", "none")
    fixed = coupled.row_lookup(summary, "fixed_joint_gru", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    final_training = consequence_training_rows[-1]
    source_sequences = sum(row.sequences for row in source_summary if not row.source_policy.startswith("student_iteration"))
    student_sequences = sum(row.sequences for row in source_summary if row.source_policy.startswith("student_iteration"))
    supports_active = (
        active_training.crises > 0
        and final_training.weighted_train_accuracy >= 0.55
        and mean_crisis_count >= 4.0
        and active.mean_total_score - consequence.mean_total_score >= 0.010
        and active.mean_crisis_score - consequence.mean_crisis_score >= 0.020
        and active.mean_resolved_rate - consequence.mean_resolved_rate >= 0.060
        and active.mean_coupled_response_rate - consequence.mean_coupled_response_rate >= 0.060
        and active.mean_total_score - returned.mean_total_score >= 0.010
        and active.mean_alive_at_12h >= 12.0
        and active.shock_gate_pass_rate == 1.0
        and active.post_gate_shock_rate == 1.0
    )
    supports_value = (
        action_value_training.weighted_train_mae <= 0.55
        and mean_crisis_count >= 4.0
        and action_value.mean_total_score - consequence.mean_total_score >= 0.010
        and action_value.mean_crisis_score - consequence.mean_crisis_score >= 0.020
        and action_value.mean_resolved_rate - consequence.mean_resolved_rate >= 0.050
        and action_value.mean_coupled_response_rate - consequence.mean_coupled_response_rate >= 0.050
        and action_value.mean_total_score - returned.mean_total_score >= 0.010
        and action_value.mean_alive_at_12h >= 12.0
        and action_value.shock_gate_pass_rate == 1.0
        and action_value.post_gate_shock_rate == 1.0
    )
    supports_teacher = (
        action_value.mean_crisis_score >= 0.35
        and action_value.mean_coupled_response_rate >= 0.40
        and teacher.mean_crisis_score - action_value.mean_crisis_score <= 0.30
    )
    supports_dependency = (
        action_value.mean_crisis_score > 0.0
        and social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    return ActiveConsequenceVerdictRow(
        selected_router=router.name,
        selected_planner=planner.name,
        selected_consequence_bias=consequence_bias,
        selected_active_bias=active_bias,
        selected_action_value_bias=action_value_bias,
        source_sequences=source_sequences,
        student_sequences=student_sequences,
        aggregate_examples=final_training.aggregate_examples,
        active_training_crises=active_training.crises,
        consequence_train_accuracy=final_training.train_accuracy,
        consequence_weighted_accuracy=final_training.weighted_train_accuracy,
        active_mean_return=active_training.mean_return,
        action_value_train_mae=action_value_training.train_mae,
        action_value_weighted_train_mae=action_value_training.weighted_train_mae,
        active_consequence_total_score=active.mean_total_score,
        action_value_total_score=action_value.mean_total_score,
        consequence_total_score=consequence.mean_total_score,
        min_channel_total_score=teacher.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        active_consequence_crisis_score=active.mean_crisis_score,
        action_value_crisis_score=action_value.mean_crisis_score,
        consequence_crisis_score=consequence.mean_crisis_score,
        min_channel_crisis_score=teacher.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        active_consequence_resolved_rate=active.mean_resolved_rate,
        action_value_resolved_rate=action_value.mean_resolved_rate,
        consequence_resolved_rate=consequence.mean_resolved_rate,
        min_channel_resolved_rate=teacher.mean_resolved_rate,
        fixed_joint_resolved_rate=fixed.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        active_consequence_coupled_response=active.mean_coupled_response_rate,
        action_value_coupled_response=action_value.mean_coupled_response_rate,
        consequence_coupled_response=consequence.mean_coupled_response_rate,
        min_channel_coupled_response=teacher.mean_coupled_response_rate,
        fixed_joint_coupled_response=fixed.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        active_gain_over_consequence=active.mean_total_score - consequence.mean_total_score,
        active_gain_over_return_selected=active.mean_total_score - returned.mean_total_score,
        action_value_gain_over_consequence=action_value.mean_total_score - consequence.mean_total_score,
        action_value_gain_over_return_selected=action_value.mean_total_score - returned.mean_total_score,
        active_gap_to_teacher=teacher.mean_total_score - active.mean_total_score,
        action_value_gap_to_teacher=teacher.mean_total_score - action_value.mean_total_score,
        active_gap_to_fixed_joint=fixed.mean_total_score - active.mean_total_score,
        action_value_gap_to_fixed_joint=fixed.mean_total_score - action_value.mean_total_score,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=active.shock_gate_pass_rate,
        post_gate_shock_rate=active.post_gate_shock_rate,
        survival_at_12h=active.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_active_consequence_optimization=supports_active,
        supports_learned_action_value_control=supports_value,
        supports_teacher_transfer=supports_teacher,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_value and supports_teacher and supports_dependency else "partial_or_failed",
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
            model, row = base.train_model(architecture, x, y, mask, cfg, device)
            models[architecture] = model
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
            20262521,
        )
        social_model, social_training = report113.train_action_model(
            cfg,
            device,
            "social",
            social_sequences,
            social_labels,
            flags,
            20262522,
        )
        selected_planner, planner_selection = report123.select_planner(
            cfg,
            models["gru"],
            env_model,
            social_model,
            device,
            selected_router,
        )
        aggregate = report126.collect_behavior_sequences(
            cfg,
            models["gru"],
            env_model,
            social_model,
            device,
            selected_router,
            selected_planner,
        )
        consequence_model, consequence_training = report126.train_consequence_policy(
            cfg,
            aggregate,
            device,
            0,
            "behavior_sources",
        )
        consequence_training_rows = [consequence_training]
        for iteration in range(1, cfg.student_iterations + 1):
            student_sequences = report126.collect_student_sequences(
                cfg,
                models["gru"],
                consequence_model,
                device,
                selected_router,
                iteration,
            )
            aggregate.extend(student_sequences)
            consequence_model, row = report126.train_consequence_policy(
                cfg,
                aggregate,
                device,
                iteration,
                f"student_iteration_{iteration}",
            )
            consequence_training_rows.append(row)
        source_summary = report126.source_rows(aggregate)
        selected_consequence_bias, consequence_selection = report126.select_policy_bias(
            cfg,
            models["gru"],
            consequence_model,
            device,
            selected_router,
        )
        active_model, active_training = train_active_consequence_model(
            cfg,
            models["gru"],
            consequence_model,
            device,
            selected_router,
        )
        selected_active_bias, active_selection = select_active_bias(
            cfg,
            models["gru"],
            active_model,
            device,
            selected_router,
        )
        action_value_model, action_value_training = train_action_value_model(cfg, aggregate, device)
        selected_action_value_bias, action_value_selection = select_action_value_bias(
            cfg,
            models["gru"],
            action_value_model,
            device,
            selected_router,
        )

        eval_rows: List[coupled.EvalRow] = []
        crisis_logs: Dict[str, object] = {}
        trace_out: Optional[Trace] = None
        for seed in cfg.eval_seeds:
            for controller, model, router in (
                ("designed", None, report105.ROUTERS[0]),
                ("reactive", None, report105.ROUTERS[0]),
                ("frame_mlp", models["frame_mlp"], report105.ROUTERS[0]),
                ("gru", models["gru"], report105.ROUTERS[0]),
                ("return_selected_gru", models["gru"], selected_router),
            ):
                row, maybe_trace, tracker = coupled.run_episode(
                    seed,
                    cfg,
                    controller,
                    model,
                    device,
                    router,
                    trace=(seed == cfg.trace_seed and controller == "return_selected_gru"),
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:{controller}:none"] = tracker.response_log
                if maybe_trace.frames:
                    trace_out = maybe_trace
            fixed_row = report123.run_fixed_joint_episode(
                seed,
                cfg,
                models["gru"],
                env_model,
                social_model,
                device,
                selected_router,
            )
            eval_rows.append(fixed_row)
            min_row, _, min_tracker = report123.run_min_channel_episode(
                seed,
                cfg,
                models["gru"],
                env_model,
                social_model,
                device,
                selected_router,
                selected_planner,
            )
            eval_rows.append(min_row)
            crisis_logs[f"{seed}:min_channel_planner_gru:none"] = min_tracker.response_log
            consequence_row, _, consequence_tracker = report126.run_consequence_episode(
                seed,
                cfg,
                models["gru"],
                consequence_model,
                device,
                selected_router,
                selected_consequence_bias,
            )
            eval_rows.append(consequence_row)
            crisis_logs[f"{seed}:consequence_recovery_gru:none"] = consequence_tracker.response_log
            active_row, maybe_trace, active_tracker = run_active_consequence_episode(
                seed,
                cfg,
                models["gru"],
                active_model,
                device,
                selected_router,
                selected_active_bias,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(active_row)
            crisis_logs[f"{seed}:active_consequence_optimized_gru:none"] = active_tracker.response_log
            if maybe_trace.frames:
                trace_out = maybe_trace
            action_value_row, maybe_trace, action_value_tracker = run_action_value_episode(
                seed,
                cfg,
                models["gru"],
                action_value_model,
                device,
                selected_router,
                selected_action_value_bias,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(action_value_row)
            crisis_logs[f"{seed}:active_consequence_value_gru:none"] = action_value_tracker.response_log
            if maybe_trace.frames:
                trace_out = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker = run_action_value_episode(
                    seed,
                    cfg,
                    models["gru"],
                    action_value_model,
                    device,
                    selected_router,
                    selected_action_value_bias,
                    ablation=ablation,
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:active_consequence_value_gru:{ablation}"] = tracker.response_log

        summary = coupled.summarize(eval_rows)
        ablations = ablations_from_summary(summary)
        verdict = transfer_verdict(
            summary,
            ablations,
            selected_router,
            selected_planner,
            selected_consequence_bias,
            selected_active_bias,
            selected_action_value_bias,
            schedules,
            consequence_training_rows,
            source_summary,
            active_training,
            action_value_training,
        )

    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "active_consequence_optimized_gru", "frames": []}
    trace_payload["condition"] = "active_consequence_optimized_gru"
    payload = {
        "experiment": "ssrm_3d_coupled_crisis_active_consequence_optimization",
        "config": asdict(cfg),
        "claim": {
            "tested": "closed-loop consequence optimization can improve a recurrent crisis policy initialized from consequence recovery",
            "remaining_structure": "candidate actions, crisis families, world variables, and consequence reward are supplied; this is bounded policy/value optimization, not open-ended deep RL",
        },
        "action_candidates": list(ACTION_CANDIDATES),
        "schedule": [asdict(row) for row in schedules],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "router_selection": [asdict(row) for row in router_selection],
        "planner_selection": [asdict(row) for row in planner_selection],
        "source_summary": [asdict(row) for row in source_summary],
        "consequence_training": [asdict(row) for row in consequence_training_rows],
        "consequence_selection": [asdict(row) for row in consequence_selection],
        "active_training": asdict(active_training),
        "active_selection": [asdict(row) for row in active_selection],
        "action_value_training": asdict(action_value_training),
        "action_value_selection": [asdict(row) for row in action_value_selection],
        "eval": [asdict(row) for row in eval_rows],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace_payload,
        "crisis_logs": crisis_logs,
    }
    report124.rows_to_csv(Path(f"{PREFIX}_schedule.csv"), schedules)
    report124.rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_action_training.csv"), [env_training, social_training])
    report124.rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_planner_selection.csv"), planner_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_source_summary.csv"), source_summary)
    report124.rows_to_csv(Path(f"{PREFIX}_consequence_training.csv"), consequence_training_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_consequence_selection.csv"), consequence_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_active_training.csv"), [active_training])
    report124.rows_to_csv(Path(f"{PREFIX}_active_selection.csv"), active_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_action_value_training.csv"), [action_value_training])
    report124.rows_to_csv(Path(f"{PREFIX}_action_value_selection.csv"), action_value_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    report124.rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    report124.rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    report124.write_json(Path(f"{PREFIX}_results.json"), payload)
    report124.write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    report124.write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_ACTIVE_CONSEQUENCE_OPTIMIZATION_RESULTS", payload)
    report124.write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_ACTIVE_CONSEQUENCE_OPTIMIZATION_TRACE", trace_payload)
    return payload


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-seeds", default="20260911,20260912,20260913")
    parser.add_argument("--tune-seeds", default="20261111,20261112")
    parser.add_argument("--eval-seeds", default="20261121,20261122,20261123")
    parser.add_argument("--hours", type=float, default=96.0)
    parser.add_argument("--step-hours", type=float, default=0.10)
    parser.add_argument("--population", type=int, default=14)
    parser.add_argument("--epochs", type=int, default=14)
    parser.add_argument("--hidden-size", type=int, default=48)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--action-epochs", type=int, default=18)
    parser.add_argument("--action-hidden-size", type=int, default=48)
    parser.add_argument("--action-learning-rate", type=float, default=0.004)
    parser.add_argument("--consequence-epochs", type=int, default=8)
    parser.add_argument("--consequence-hidden-size", type=int, default=48)
    parser.add_argument("--consequence-learning-rate", type=float, default=0.003)
    parser.add_argument("--consequence-return-scale", type=float, default=1.15)
    parser.add_argument("--student-iterations", type=int, default=0)
    parser.add_argument("--student-collection-bias", type=float, default=0.70)
    parser.add_argument("--active-epochs", type=int, default=3)
    parser.add_argument("--active-learning-rate", type=float, default=0.0018)
    parser.add_argument("--active-entropy-coef", type=float, default=0.006)
    parser.add_argument("--active-training-bias", type=float, default=0.40)
    parser.add_argument("--active-return-scale", type=float, default=1.0)
    parser.add_argument("--action-value-epochs", type=int, default=8)
    parser.add_argument("--action-value-hidden-size", type=int, default=64)
    parser.add_argument("--action-value-learning-rate", type=float, default=0.003)
    parser.add_argument("--policy-temperature", type=float, default=1.0)
    parser.add_argument("--policy-bias-candidates", default="0.0,0.40,0.80")
    parser.add_argument("--active-bias-candidates", default="0.0,0.40,0.80")
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
        consequence_epochs=args.consequence_epochs,
        consequence_hidden_size=args.consequence_hidden_size,
        consequence_learning_rate=args.consequence_learning_rate,
        consequence_return_scale=args.consequence_return_scale,
        student_iterations=args.student_iterations,
        student_collection_bias=args.student_collection_bias,
        active_epochs=args.active_epochs,
        active_learning_rate=args.active_learning_rate,
        active_entropy_coef=args.active_entropy_coef,
        active_training_bias=args.active_training_bias,
        active_return_scale=args.active_return_scale,
        action_value_epochs=args.action_value_epochs,
        action_value_hidden_size=args.action_value_hidden_size,
        action_value_learning_rate=args.action_value_learning_rate,
        policy_temperature=args.policy_temperature,
        policy_bias_candidates=parse_floats(args.policy_bias_candidates),
        active_bias_candidates=parse_floats(args.active_bias_candidates),
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "active_training": payload["active_training"],
        "active_selection": payload["active_selection"],
        "action_value_training": payload["action_value_training"],
        "action_value_selection": payload["action_value_selection"],
        "verdict": payload["verdict"],
        "summary": payload["summary"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
