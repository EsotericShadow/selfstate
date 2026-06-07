#!/usr/bin/env python3
"""Completed-window process-value recovery for SSRM-3D coupled crises.

Report 126 showed that consequence-weighted recurrent imitation recovers a
nonzero coupled response after planner removal, but the learned policy remains
far below the structured minimum-channel planner. This benchmark tests the next
narrower step: train a process-value critic from completed crisis windows and
use it to rerank active-crisis actions from the consequence policy.

The critic sees current crisis-window features plus a candidate action and is
trained against the completed crisis return for the whole window. It does not
receive a scenario label, does not call the engineered planner during
sequence-value evaluation, and does not discover new actions. This is bounded
process-value evidence, not open-ended deep RL, subjective consciousness, or a
solved civilization simulation.
"""

from __future__ import annotations

import argparse
import json
import math
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
from ssrm_maturation.agents import choose_action, make_agents
from ssrm_maturation.benchmark import TRACE_CHECKPOINTS, Trace, score_episode, snapshot
from ssrm_maturation.environment import clamp, living
from ssrm_maturation.models import CONDITIONS, Agent, Condition, World


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_sequence_value_recovery"
PROCESS_VALUE_SEED = 20262271
ACTION_CANDIDATES = report126.ACTION_CANDIDATES
ACTION_TO_INDEX = report126.ACTION_TO_INDEX
PROCESS_VALUE_INPUT_SIZE = report119.POLICY_INPUT_SIZE + len(ACTION_CANDIDATES)


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
    consequence_epochs: int = 14
    consequence_hidden_size: int = 64
    consequence_learning_rate: float = 0.003
    consequence_return_scale: float = 1.15
    process_value_epochs: int = 18
    process_value_hidden_size: int = 64
    process_value_learning_rate: float = 0.003
    process_value_return_scale: float = 1.10
    max_process_value_examples: int = 180000
    student_iterations: int = 1
    student_collection_bias: float = 0.70
    policy_temperature: float = 1.0
    policy_bias_candidates: Sequence[float] = (0.0, 0.20, 0.40, 0.70, 1.00)
    process_value_bias_candidates: Sequence[float] = (0.0, 0.25, 0.50, 0.80, 1.10, 1.50)
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class ProcessValueTrainingRow:
    train_examples: int
    source_sequences: int
    process_value_epochs: int
    final_loss: float
    train_mae: float
    pairwise_accuracy: float
    positive_example_rate: float
    mean_return: float
    mean_weight: float
    max_weight: float
    env_action_fraction: float
    social_action_fraction: float
    none_fraction: float
    device_used: str
    parameter_count: int


@dataclass(frozen=True)
class ProcessValueSelectionRow:
    process_value_bias: float
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
class ProcessValueVerdictRow:
    selected_router: str
    selected_planner: str
    selected_policy_bias: float
    selected_process_value_bias: float
    source_sequences: int
    student_sequences: int
    aggregate_examples: int
    process_value_examples: int
    final_consequence_train_accuracy: float
    final_consequence_weighted_accuracy: float
    process_value_pairwise_accuracy: float
    sequence_value_total_score: float
    consequence_total_score: float
    min_channel_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    sequence_value_crisis_score: float
    consequence_crisis_score: float
    min_channel_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    sequence_value_resolved_rate: float
    consequence_resolved_rate: float
    min_channel_resolved_rate: float
    fixed_joint_resolved_rate: float
    return_selected_resolved_rate: float
    sequence_value_coupled_response: float
    consequence_coupled_response: float
    min_channel_coupled_response: float
    fixed_joint_coupled_response: float
    return_selected_coupled_response: float
    sequence_value_gain_over_consequence: float
    sequence_value_gain_over_return_selected: float
    sequence_value_gap_to_teacher: float
    sequence_value_gap_to_fixed_joint: float
    social_culture_crisis_loss: float
    environment_crisis_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    mean_crisis_count: float
    supports_process_value_recovery: bool
    supports_teacher_transfer: bool
    supports_social_environment_dependency: bool
    verdict: str


class ProcessValueNet(torch.nn.Module):
    def __init__(self, hidden_size: int) -> None:
        super().__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(PROCESS_VALUE_INPUT_SIZE, hidden_size),
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


def action_one_hot(action_index: int) -> List[float]:
    return [1.0 if index == action_index else 0.0 for index in range(len(ACTION_CANDIDATES))]


def process_value_input(features: Sequence[float], action_index: int) -> List[float]:
    values = list(features) + action_one_hot(action_index)
    if len(values) != PROCESS_VALUE_INPUT_SIZE:
        raise RuntimeError(f"process-value feature mismatch: {len(values)} != {PROCESS_VALUE_INPUT_SIZE}")
    return values


def process_value_weight(value: float, scale: float) -> float:
    return max(0.05, min(8.0, math.exp(scale * value)))


def build_process_value_examples(
    sequences: Sequence[report126.ConsequenceSequence],
    cfg: Config,
) -> Tuple[List[List[float]], List[float], List[float], Dict[str, float]]:
    examples: List[List[float]] = []
    targets: List[float] = []
    weights: List[float] = []
    counts = {action: 0 for action in ACTION_CANDIDATES}
    rng = random.Random(PROCESS_VALUE_SEED + len(sequences))
    pairs: List[Tuple[List[float], int, float]] = []
    for sequence in sequences:
        for features, action_index in sequence.sequence:
            pairs.append((features, action_index, sequence.sequence_return))
    if len(pairs) > cfg.max_process_value_examples:
        pairs = rng.sample(pairs, cfg.max_process_value_examples)
    for features, action_index, sequence_return in pairs:
        examples.append(process_value_input(features, action_index))
        targets.append(sequence_return)
        weights.append(process_value_weight(sequence_return, cfg.process_value_return_scale))
        counts[ACTION_CANDIDATES[action_index]] += 1
    total = max(1, len(examples))
    env_count = sum(counts.get(action, 0) for action in report111.ENV_RESPONSE_ACTIONS)
    social_count = sum(counts.get(action, 0) for action in report111.SOCIAL_RESPONSE_ACTIONS)
    stats = {
        "positive_example_rate": sum(1 for target in targets if target > 0.0) / total,
        "mean_return": mean(targets),
        "mean_weight": mean(weights),
        "max_weight": max(weights) if weights else 0.0,
        "env_action_fraction": env_count / total,
        "social_action_fraction": social_count / total,
        "none_fraction": counts.get("none", 0) / total,
    }
    return examples, targets, weights, stats


def train_process_value_model(
    cfg: Config,
    sequences: Sequence[report126.ConsequenceSequence],
    device: torch.device,
) -> Tuple[ProcessValueNet, ProcessValueTrainingRow]:
    examples, targets, weights, stats = build_process_value_examples(sequences, cfg)
    if not examples:
        raise RuntimeError("no process-value examples collected")
    torch.manual_seed(PROCESS_VALUE_SEED)
    x = torch.tensor(examples, dtype=torch.float32, device=device)
    y = torch.tensor(targets, dtype=torch.float32, device=device)
    w = torch.tensor(weights, dtype=torch.float32, device=device)
    model = ProcessValueNet(cfg.process_value_hidden_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.process_value_learning_rate)
    final_loss = 0.0
    for _ in range(cfg.process_value_epochs):
        model.train()
        optimizer.zero_grad()
        prediction = model(x)
        loss = (((prediction - y) ** 2) * w).sum() / w.sum()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 2.0)
        optimizer.step()
        final_loss = float(loss.detach().cpu().item())
    model.eval()
    with torch.no_grad():
        prediction = model(x)
        train_mae = torch.mean(torch.abs(prediction - y)).item()
        if x.shape[0] > 1:
            sample_size = min(6000, x.shape[0])
            sample = torch.randperm(x.shape[0], device=device)[:sample_size]
            shifted = sample.roll(1)
            target_order = y[sample] > y[shifted]
            pred_order = prediction[sample] > prediction[shifted]
            pairwise = (target_order == pred_order).float().mean().item()
        else:
            pairwise = 0.0
    return model, ProcessValueTrainingRow(
        train_examples=len(examples),
        source_sequences=len(sequences),
        process_value_epochs=cfg.process_value_epochs,
        final_loss=final_loss,
        train_mae=train_mae,
        pairwise_accuracy=pairwise,
        positive_example_rate=stats["positive_example_rate"],
        mean_return=stats["mean_return"],
        mean_weight=stats["mean_weight"],
        max_weight=stats["max_weight"],
        env_action_fraction=stats["env_action_fraction"],
        social_action_fraction=stats["social_action_fraction"],
        none_fraction=stats["none_fraction"],
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in model.parameters()),
    )


def process_value_bias(
    features: Sequence[float],
    value_model: ProcessValueNet,
    device: torch.device,
    dtype: torch.dtype,
    ablation: str,
    process_value_bias_weight: float,
) -> torch.Tensor:
    if process_value_bias_weight <= 0.0:
        return torch.zeros((1, len(ACTION_CANDIDATES)), dtype=dtype, device=device)
    rows: List[List[float]] = []
    allowed = set(report119.allowed_indices(ablation))
    for action_index in range(len(ACTION_CANDIDATES)):
        if action_index in allowed:
            rows.append(process_value_input(features, action_index))
        else:
            rows.append(process_value_input(features, ACTION_TO_INDEX["none"]))
    with torch.no_grad():
        x = torch.tensor(rows, dtype=torch.float32, device=device)
        values = value_model(x)
        values = values - values.mean()
        values = values / (values.std(unbiased=False) + 1e-4)
        values = torch.clamp(values, -1.8, 1.8)
    return values.reshape(1, -1).to(dtype=dtype) * process_value_bias_weight


def choose_sequence_value_candidate(
    consequence_model: report121.CrisisMemoryPolicyNet,
    value_model: ProcessValueNet,
    features: Sequence[float],
    active: coupled.ActiveCrisis,
    action_counts: Dict[str, int],
    alive_count: int,
    world_time: float,
    state: Optional[torch.Tensor],
    device: torch.device,
    ablation: str,
    temperature: float,
    policy_bias: float,
    process_value_bias_weight: float,
) -> Tuple[str, torch.Tensor]:
    values = report119.policy_features(features, active, action_counts, alive_count, world_time, ablation)
    with torch.no_grad():
        x = torch.tensor([[values]], dtype=torch.float32, device=device)
        logits, next_state = consequence_model.step(x, state)
        policy_logits = report119.masked_logits(logits / max(0.05, temperature), ablation, policy_bias)
        value_logits = process_value_bias(
            values,
            value_model,
            device,
            logits.dtype,
            ablation,
            process_value_bias_weight,
        )
        combined = report119.masked_logits(policy_logits + value_logits, ablation, 0.0)
        index = int(combined.argmax(dim=-1).item())
    return ACTION_CANDIDATES[index], next_state.detach()


def run_sequence_value_episode(
    seed: int,
    cfg: Config,
    base_model: base.ControllerNet,
    consequence_model: report121.CrisisMemoryPolicyNet,
    value_model: ProcessValueNet,
    device: torch.device,
    router: report105.PressureRouter,
    policy_bias: float,
    process_value_bias_weight: float,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, Trace, coupled.CrisisTracker]:
    condition = CONDITIONS[0]
    rng = random.Random(
        seed * 127
        + sum(ord(ch) for ch in "sequence_value_recovery_gru" + router.name + ablation)
        + int(policy_bias * 1000)
        + int(process_value_bias_weight * 1000)
        + 9187
    )
    agents = make_agents(rng, cfg.population)
    world = coupled.prepare_world(rng, cfg)
    baseline = base.initial_baseline(world, cfg.population)
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
    trace_out = Trace(seed=seed, condition=f"sequence_value_recovery_gru:{router.name}:bias_{policy_bias:g}:value_{process_value_bias_weight:g}:{ablation}")
    checkpoints = list(TRACE_CHECKPOINTS)
    no_pre_gate_shock = True
    alive_at_12h = cfg.population
    at_12: dict[str, float] = {}
    memory_state: Optional[torch.Tensor] = None
    active_key: Optional[float] = None
    if trace:
        trace_out.frames.append(snapshot(world, agents, "0h", events))
        if checkpoints and checkpoints[0] == 0.0:
            checkpoints.pop(0)

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        action_counts: Dict[str, int] = {}
        coupled.maybe_start_crisis(world, tracker, rng, events)
        if tracker.active is not None and active_key != tracker.active.start:
            active_key = tracker.active.start
            memory_state = None
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
            if active is not None:
                action, next_state = choose_sequence_value_candidate(
                    consequence_model,
                    value_model,
                    features,
                    active,
                    action_counts,
                    len(living(agents)),
                    current_world.time,
                    memory_state,
                    device,
                    ablation,
                    cfg.policy_temperature,
                    policy_bias,
                    process_value_bias_weight,
                )
                memory_state = next_state
                if action == "none":
                    action = report117.learned_policy_action(agent, features, base_model, recurrent_states, router, device, ablation)
            else:
                action = report117.learned_policy_action(agent, features, base_model, recurrent_states, router, device, ablation)
            if ablation == "environment" and action in report111.ENV_RESPONSE_ACTIONS:
                action = "rest"
            if ablation == "social_culture" and action in report111.SOCIAL_RESPONSE_ACTIONS:
                action = "rest"
            action_counts[action] = action_counts.get(action, 0) + 1
            return action

        base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
        report111.update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
        coupled.complete_crisis_if_due(world, agents, tracker, events)
        if tracker.active is None:
            memory_state = None
            active_key = None
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
        controller="sequence_value_recovery_gru",
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
    balance = 1.0 - abs(env_response - social_response)
    objective = total * 0.38 + crisis * 1.38 + resolved * 0.86 + coupled_response * 1.12 + balance * 0.18 - damage * 0.38
    return total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective


def select_process_value_bias(
    cfg: Config,
    base_model: base.ControllerNet,
    consequence_model: report121.CrisisMemoryPolicyNet,
    value_model: ProcessValueNet,
    device: torch.device,
    router: report105.PressureRouter,
    policy_bias: float,
) -> Tuple[float, List[ProcessValueSelectionRow]]:
    rows: List[ProcessValueSelectionRow] = []
    best_bias = 0.0
    best_objective = -1e9
    for bias in cfg.process_value_bias_candidates:
        eval_rows = [
            run_sequence_value_episode(
                seed,
                cfg,
                base_model,
                consequence_model,
                value_model,
                device,
                router,
                policy_bias,
                bias,
            )[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_objective = objective
            best_bias = bias
        rows.append(ProcessValueSelectionRow(
            process_value_bias=bias,
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
    return best_bias, [replace(row, selected=(row.process_value_bias == best_bias)) for row in rows]


def ablations_from_summary(summary: Sequence[coupled.SummaryRow]) -> List[coupled.AblationRow]:
    base_row = coupled.row_lookup(summary, "sequence_value_recovery_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = coupled.row_lookup(summary, "sequence_value_recovery_gru", ablation)
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
    policy_bias: float,
    process_value_bias_weight: float,
    schedules: Sequence[report114.ScheduleRow],
    consequence_training_rows: Sequence[report126.ConsequenceTrainingRow],
    process_value_training: ProcessValueTrainingRow,
    source_summary: Sequence[report126.ConsequenceSourceRow],
) -> ProcessValueVerdictRow:
    sequence_value = coupled.row_lookup(summary, "sequence_value_recovery_gru", "none")
    consequence = coupled.row_lookup(summary, "consequence_recovery_gru", "none")
    teacher = coupled.row_lookup(summary, "min_channel_planner_gru", "none")
    fixed = coupled.row_lookup(summary, "fixed_joint_gru", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    final_consequence_training = consequence_training_rows[-1]
    source_sequences = sum(row.sequences for row in source_summary if not row.source_policy.startswith("student_iteration"))
    student_sequences = sum(row.sequences for row in source_summary if row.source_policy.startswith("student_iteration"))
    supports_recovery = (
        process_value_training.pairwise_accuracy >= 0.55
        and mean_crisis_count >= 4.0
        and sequence_value.mean_total_score - consequence.mean_total_score >= 0.010
        and sequence_value.mean_crisis_score - consequence.mean_crisis_score >= 0.020
        and sequence_value.mean_crisis_score - returned.mean_crisis_score >= 0.040
        and sequence_value.mean_resolved_rate - returned.mean_resolved_rate >= 0.080
        and sequence_value.mean_coupled_response_rate - returned.mean_coupled_response_rate >= 0.080
        and sequence_value.mean_alive_at_12h >= 12.0
        and sequence_value.shock_gate_pass_rate == 1.0
        and sequence_value.post_gate_shock_rate == 1.0
    )
    supports_teacher = (
        sequence_value.mean_crisis_score >= 0.35
        and sequence_value.mean_coupled_response_rate >= 0.40
        and teacher.mean_crisis_score - sequence_value.mean_crisis_score <= 0.30
    )
    supports_dependency = (
        sequence_value.mean_crisis_score > 0.0
        and social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    return ProcessValueVerdictRow(
        selected_router=router.name,
        selected_planner=planner.name,
        selected_policy_bias=policy_bias,
        selected_process_value_bias=process_value_bias_weight,
        source_sequences=source_sequences,
        student_sequences=student_sequences,
        aggregate_examples=final_consequence_training.aggregate_examples,
        process_value_examples=process_value_training.train_examples,
        final_consequence_train_accuracy=final_consequence_training.train_accuracy,
        final_consequence_weighted_accuracy=final_consequence_training.weighted_train_accuracy,
        process_value_pairwise_accuracy=process_value_training.pairwise_accuracy,
        sequence_value_total_score=sequence_value.mean_total_score,
        consequence_total_score=consequence.mean_total_score,
        min_channel_total_score=teacher.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        sequence_value_crisis_score=sequence_value.mean_crisis_score,
        consequence_crisis_score=consequence.mean_crisis_score,
        min_channel_crisis_score=teacher.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        sequence_value_resolved_rate=sequence_value.mean_resolved_rate,
        consequence_resolved_rate=consequence.mean_resolved_rate,
        min_channel_resolved_rate=teacher.mean_resolved_rate,
        fixed_joint_resolved_rate=fixed.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        sequence_value_coupled_response=sequence_value.mean_coupled_response_rate,
        consequence_coupled_response=consequence.mean_coupled_response_rate,
        min_channel_coupled_response=teacher.mean_coupled_response_rate,
        fixed_joint_coupled_response=fixed.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        sequence_value_gain_over_consequence=sequence_value.mean_total_score - consequence.mean_total_score,
        sequence_value_gain_over_return_selected=sequence_value.mean_total_score - returned.mean_total_score,
        sequence_value_gap_to_teacher=teacher.mean_total_score - sequence_value.mean_total_score,
        sequence_value_gap_to_fixed_joint=fixed.mean_total_score - sequence_value.mean_total_score,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=sequence_value.shock_gate_pass_rate,
        post_gate_shock_rate=sequence_value.post_gate_shock_rate,
        survival_at_12h=sequence_value.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_process_value_recovery=supports_recovery,
        supports_teacher_transfer=supports_teacher,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_recovery and supports_teacher and supports_dependency else "partial_or_failed",
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
            20261851,
        )
        social_model, social_training = report113.train_action_model(
            cfg,
            device,
            "social",
            social_sequences,
            social_labels,
            flags,
            20261852,
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
        process_value_model, process_value_training = train_process_value_model(cfg, aggregate, device)
        selected_policy_bias, policy_selection = report126.select_policy_bias(
            cfg,
            models["gru"],
            consequence_model,
            device,
            selected_router,
        )
        selected_process_value_bias, process_value_selection = select_process_value_bias(
            cfg,
            models["gru"],
            consequence_model,
            process_value_model,
            device,
            selected_router,
            selected_policy_bias,
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
                if seed == cfg.trace_seed and controller == "return_selected_gru":
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
                selected_policy_bias,
            )
            eval_rows.append(consequence_row)
            crisis_logs[f"{seed}:consequence_recovery_gru:none"] = consequence_tracker.response_log
            sequence_value_row, maybe_trace, sequence_value_tracker = run_sequence_value_episode(
                seed,
                cfg,
                models["gru"],
                consequence_model,
                process_value_model,
                device,
                selected_router,
                selected_policy_bias,
                selected_process_value_bias,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(sequence_value_row)
            crisis_logs[f"{seed}:sequence_value_recovery_gru:none"] = sequence_value_tracker.response_log
            if seed == cfg.trace_seed:
                trace_out = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker = run_sequence_value_episode(
                    seed,
                    cfg,
                    models["gru"],
                    consequence_model,
                    process_value_model,
                    device,
                    selected_router,
                    selected_policy_bias,
                    selected_process_value_bias,
                    ablation=ablation,
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:sequence_value_recovery_gru:{ablation}"] = tracker.response_log

        summary = coupled.summarize(eval_rows)
        ablations = ablations_from_summary(summary)
        verdict = transfer_verdict(
            summary,
            ablations,
            selected_router,
            selected_planner,
            selected_policy_bias,
            selected_process_value_bias,
            schedules,
            consequence_training_rows,
            process_value_training,
            source_summary,
        )

    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "sequence_value_recovery_gru", "frames": []}
    trace_payload["condition"] = "sequence_value_recovery_gru"
    payload = {
        "experiment": "ssrm_3d_coupled_crisis_sequence_value_recovery",
        "config": asdict(cfg),
        "claim": {
            "tested": "completed-window process-value critic can rerank consequence-policy actions and preserve coupled crisis repair after engineered planner removal",
            "remaining_structure": "candidate action set, behavior sources, and process-value targets are supplied; this is bounded process-value recovery, not open-ended deep RL",
        },
        "action_candidates": list(ACTION_CANDIDATES),
        "source_policies": [
            {"name": name, "env_quota": env, "social_quota": social, "strength": strength}
            for name, env, social, strength in report126.SOURCE_POLICIES
        ],
        "schedule": [asdict(row) for row in schedules],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "router_selection": [asdict(row) for row in router_selection],
        "planner_selection": [asdict(row) for row in planner_selection],
        "source_summary": [asdict(row) for row in source_summary],
        "consequence_training": [asdict(row) for row in consequence_training_rows],
        "process_value_training": asdict(process_value_training),
        "policy_selection": [asdict(row) for row in policy_selection],
        "process_value_selection": [asdict(row) for row in process_value_selection],
        "eval": [asdict(row) for row in eval_rows],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "crisis_logs": crisis_logs,
    }
    report124.rows_to_csv(Path(f"{PREFIX}_schedule.csv"), schedules)
    report124.rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_action_training.csv"), [env_training, social_training])
    report124.rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_planner_selection.csv"), planner_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_source_summary.csv"), source_summary)
    report124.rows_to_csv(Path(f"{PREFIX}_consequence_training.csv"), consequence_training_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_process_value_training.csv"), [process_value_training])
    report124.rows_to_csv(Path(f"{PREFIX}_policy_selection.csv"), policy_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_process_value_selection.csv"), process_value_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    report124.rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    report124.rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    report124.write_json(Path(f"{PREFIX}_results.json"), payload)
    report124.write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    report124.write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_SEQUENCE_VALUE_RECOVERY_RESULTS", payload)
    report124.write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_SEQUENCE_VALUE_RECOVERY_TRACE", trace_payload)
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
    parser.add_argument("--consequence-epochs", type=int, default=14)
    parser.add_argument("--consequence-hidden-size", type=int, default=64)
    parser.add_argument("--consequence-learning-rate", type=float, default=0.003)
    parser.add_argument("--consequence-return-scale", type=float, default=1.15)
    parser.add_argument("--process-value-epochs", type=int, default=18)
    parser.add_argument("--process-value-hidden-size", type=int, default=64)
    parser.add_argument("--process-value-learning-rate", type=float, default=0.003)
    parser.add_argument("--process-value-return-scale", type=float, default=1.10)
    parser.add_argument("--max-process-value-examples", type=int, default=180000)
    parser.add_argument("--student-iterations", type=int, default=1)
    parser.add_argument("--student-collection-bias", type=float, default=0.70)
    parser.add_argument("--policy-temperature", type=float, default=1.0)
    parser.add_argument("--policy-bias-candidates", default="0.0,0.20,0.40,0.70,1.00")
    parser.add_argument("--process-value-bias-candidates", default="0.0,0.25,0.50,0.80,1.10,1.50")
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
        process_value_epochs=args.process_value_epochs,
        process_value_hidden_size=args.process_value_hidden_size,
        process_value_learning_rate=args.process_value_learning_rate,
        process_value_return_scale=args.process_value_return_scale,
        max_process_value_examples=args.max_process_value_examples,
        student_iterations=args.student_iterations,
        student_collection_bias=args.student_collection_bias,
        policy_temperature=args.policy_temperature,
        policy_bias_candidates=parse_floats(args.policy_bias_candidates),
        process_value_bias_candidates=parse_floats(args.process_value_bias_candidates),
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "source_summary": payload["source_summary"],
        "consequence_training": payload["consequence_training"],
        "process_value_training": payload["process_value_training"],
        "policy_selection": payload["policy_selection"],
        "process_value_selection": payload["process_value_selection"],
        "verdict": payload["verdict"],
        "summary": payload["summary"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
