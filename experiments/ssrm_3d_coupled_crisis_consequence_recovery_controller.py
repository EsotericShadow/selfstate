#!/usr/bin/env python3
"""Consequence-weighted recovery control for SSRM-3D coupled crises.

Reports 124 and 125 showed that planner labels alone are not enough: offline
planner imitation and DAgger-style relabeling of student-visited states both
failed after the engineered planner was removed. This benchmark moves one step
closer to the real objective by weighting recurrent crisis-policy training by
completed crisis consequences.

The policy is still bounded. It receives supplied active-crisis action
candidates and learns from behavior-policy traces in the existing 96h
post-12h-crisis world. It is not open-ended civilization, subjective
consciousness, unsupplied action discovery, or mature deep reinforcement
learning.
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
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_consequence_recovery"
CONSEQUENCE_SEED = 20262141
ACTION_CANDIDATES = report121.ACTION_CANDIDATES
ACTION_TO_INDEX = report121.ACTION_TO_INDEX
SOURCE_POLICIES: Tuple[Tuple[str, float, float, float], ...] = (
    ("return_selected", 0.0, 0.0, 0.0),
    ("fixed_joint", 0.14, 0.14, 0.90),
    ("high_env_joint", 0.22, 0.12, 1.10),
    ("high_social_joint", 0.12, 0.22, 1.10),
    ("balanced_strong_joint", 0.18, 0.18, 1.25),
    ("min_channel_planner", 0.0, 0.0, 1.0),
)
SOURCE_OFFSETS = {name: index * 101 for index, (name, _, _, _) in enumerate(SOURCE_POLICIES)}


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
    student_iterations: int = 1
    student_collection_bias: float = 0.70
    policy_temperature: float = 1.0
    policy_bias_candidates: Sequence[float] = (0.0, 0.20, 0.40, 0.70, 1.00)
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class ConsequenceSequence:
    source_policy: str
    sequence_return: float
    sequence: Sequence[Tuple[List[float], int]]


@dataclass(frozen=True)
class ConsequenceSourceRow:
    source_policy: str
    sequences: int
    examples: int
    mean_return: float
    min_return: float
    max_return: float
    positive_return_rate: float
    env_action_fraction: float
    social_action_fraction: float
    none_fraction: float
    mean_sequence_length: float


@dataclass(frozen=True)
class ConsequenceTrainingRow:
    iteration: int
    source: str
    aggregate_sequences: int
    aggregate_examples: int
    epochs: int
    final_loss: float
    train_accuracy: float
    weighted_train_accuracy: float
    mean_return: float
    positive_return_rate: float
    mean_weight: float
    max_weight: float
    env_action_fraction: float
    social_action_fraction: float
    none_fraction: float
    device_used: str
    parameter_count: int


@dataclass(frozen=True)
class ConsequenceSelectionRow:
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
class ConsequenceVerdictRow:
    selected_router: str
    selected_planner: str
    selected_policy_bias: float
    source_sequences: int
    student_sequences: int
    aggregate_examples: int
    final_train_accuracy: float
    final_weighted_train_accuracy: float
    consequence_total_score: float
    min_channel_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    consequence_crisis_score: float
    min_channel_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    consequence_resolved_rate: float
    min_channel_resolved_rate: float
    fixed_joint_resolved_rate: float
    return_selected_resolved_rate: float
    consequence_coupled_response: float
    min_channel_coupled_response: float
    fixed_joint_coupled_response: float
    return_selected_coupled_response: float
    consequence_gain_over_return_selected: float
    consequence_gap_to_teacher: float
    consequence_gap_to_fixed_joint: float
    social_culture_crisis_loss: float
    environment_crisis_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    mean_crisis_count: float
    supports_consequence_recovery: bool
    supports_teacher_transfer: bool
    supports_social_environment_dependency: bool
    verdict: str


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def parse_ints(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def parse_floats(value: str) -> Tuple[float, ...]:
    return tuple(float(part.strip()) for part in value.split(",") if part.strip())


def sequence_weight(value: float, scale: float) -> float:
    return max(0.05, min(8.0, math.exp(scale * value)))


def sequence_stats(sequences: Sequence[ConsequenceSequence]) -> Tuple[int, int, float, float, float, float, float, float, float]:
    returns = [item.sequence_return for item in sequences]
    counts = {action: 0 for action in ACTION_CANDIDATES}
    total = 0
    for item in sequences:
        for _, index in item.sequence:
            counts[ACTION_CANDIDATES[index]] += 1
            total += 1
    env_count = sum(counts.get(action, 0) for action in report111.ENV_RESPONSE_ACTIONS)
    social_count = sum(counts.get(action, 0) for action in report111.SOCIAL_RESPONSE_ACTIONS)
    return (
        len(sequences),
        total,
        mean(returns),
        min(returns) if returns else 0.0,
        max(returns) if returns else 0.0,
        sum(1 for value in returns if value > 0.0) / max(1, len(returns)),
        env_count / max(1, total),
        social_count / max(1, total),
        counts.get("none", 0) / max(1, total),
    )


def source_rows(sequences: Sequence[ConsequenceSequence]) -> List[ConsequenceSourceRow]:
    grouped: Dict[str, List[ConsequenceSequence]] = {}
    for sequence in sequences:
        grouped.setdefault(sequence.source_policy, []).append(sequence)
    rows: List[ConsequenceSourceRow] = []
    for source, items in sorted(grouped.items()):
        seqs, examples, avg, low, high, positive, env_fraction, social_fraction, none_fraction = sequence_stats(items)
        rows.append(ConsequenceSourceRow(
            source_policy=source,
            sequences=seqs,
            examples=examples,
            mean_return=avg,
            min_return=low,
            max_return=high,
            positive_return_rate=positive,
            env_action_fraction=env_fraction,
            social_action_fraction=social_fraction,
            none_fraction=none_fraction,
            mean_sequence_length=examples / max(1, seqs),
        ))
    return rows


def train_consequence_policy(
    cfg: Config,
    sequences: Sequence[ConsequenceSequence],
    device: torch.device,
    iteration: int,
    source: str,
) -> Tuple[report121.CrisisMemoryPolicyNet, ConsequenceTrainingRow]:
    if not sequences:
        raise RuntimeError("no consequence sequences collected")
    torch.manual_seed(CONSEQUENCE_SEED + iteration * 211)
    model = report121.CrisisMemoryPolicyNet(cfg.consequence_hidden_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.consequence_learning_rate)
    weights = [sequence_weight(item.sequence_return, cfg.consequence_return_scale) for item in sequences]
    final_loss = 0.0
    for _ in range(cfg.consequence_epochs):
        for item, weight in zip(sequences, weights):
            x = torch.tensor([[pair[0] for pair in item.sequence]], dtype=torch.float32, device=device)
            y = torch.tensor([pair[1] for pair in item.sequence], dtype=torch.long, device=device)
            logits, _ = model.forward_sequence(x)
            logits = report119.masked_logits(logits.squeeze(0), "none", 0.0)
            per_item = F.cross_entropy(logits, y, reduction="none")
            loss = per_item.mean() * weight
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 2.0)
            optimizer.step()
            final_loss = float(loss.detach().cpu().item())
    correct = 0
    total = 0
    weighted_correct = 0.0
    weighted_total = 0.0
    with torch.no_grad():
        for item, weight in zip(sequences, weights):
            x = torch.tensor([[pair[0] for pair in item.sequence]], dtype=torch.float32, device=device)
            y = torch.tensor([pair[1] for pair in item.sequence], dtype=torch.long, device=device)
            logits, _ = model.forward_sequence(x)
            pred = report119.masked_logits(logits.squeeze(0), "none", 0.0).argmax(dim=-1)
            matches = (pred == y)
            correct += int(matches.sum().item())
            total += int(y.numel())
            weighted_correct += float(matches.float().sum().item()) * weight
            weighted_total += float(y.numel()) * weight
    seqs, examples, avg, _, _, positive, env_fraction, social_fraction, none_fraction = sequence_stats(sequences)
    return model, ConsequenceTrainingRow(
        iteration=iteration,
        source=source,
        aggregate_sequences=seqs,
        aggregate_examples=examples,
        epochs=cfg.consequence_epochs,
        final_loss=final_loss,
        train_accuracy=correct / max(1, total),
        weighted_train_accuracy=weighted_correct / max(1e-6, weighted_total),
        mean_return=avg,
        positive_return_rate=positive,
        mean_weight=mean(weights),
        max_weight=max(weights) if weights else 0.0,
        env_action_fraction=env_fraction,
        social_action_fraction=social_fraction,
        none_fraction=none_fraction,
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in model.parameters()),
    )


def choose_source_action(
    source_policy: str,
    agent: Agent,
    features: Sequence[float],
    action_counts: Dict[str, int],
    alive_count: int,
    base_model: base.ControllerNet,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    recurrent_states: Dict[str, torch.Tensor],
    env_states: Dict[str, torch.Tensor],
    social_states: Dict[str, torch.Tensor],
    router: report105.PressureRouter,
    planner: report123.PlannerCandidate,
    env_quota: float,
    social_quota: float,
    strength: float,
    device: torch.device,
) -> str:
    if source_policy == "min_channel_planner":
        with report123.patched_min_channel_planner(planner):
            action = report124.teacher_action(
                agent.ident,
                features,
                action_counts,
                alive_count,
                env_model,
                social_model,
                env_states,
                social_states,
                device,
            )
            if action is not None:
                return action
    elif source_policy != "return_selected":
        action = report113.coordinator_action(
            agent,
            features,
            action_counts,
            alive_count,
            env_model,
            social_model,
            env_states,
            social_states,
            env_quota,
            social_quota,
            strength,
            device,
            "none",
        )
        if action is not None:
            return action
    return report117.learned_policy_action(agent, features, base_model, recurrent_states, router, device, "none")


def collect_behavior_sequences(
    cfg: Config,
    base_model: base.ControllerNet,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
    planner: report123.PlannerCandidate,
) -> List[ConsequenceSequence]:
    sequences: List[ConsequenceSequence] = []
    for source_policy, env_quota, social_quota, strength in SOURCE_POLICIES:
        for seed in cfg.train_seeds:
            sequences.extend(collect_policy_episode(
                seed,
                cfg,
                source_policy,
                base_model,
                env_model,
                social_model,
                device,
                router,
                planner,
                env_quota,
                social_quota,
                strength,
            ))
    return sequences


def collect_policy_episode(
    seed: int,
    cfg: Config,
    source_policy: str,
    base_model: base.ControllerNet,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
    planner: report123.PlannerCandidate,
    env_quota: float,
    social_quota: float,
    strength: float,
) -> List[ConsequenceSequence]:
    rng = random.Random(seed * 223 + CONSEQUENCE_SEED + SOURCE_OFFSETS[source_policy])
    agents = make_agents(rng, cfg.population)
    world = coupled.prepare_world(rng, cfg)
    condition = CONDITIONS[0]
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    env_states: Dict[str, torch.Tensor] = {}
    social_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
    active_key: Optional[float] = None
    pending: List[Tuple[List[float], int]] = []
    damage_start = 0.0
    sequences: List[ConsequenceSequence] = []

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        action_counts: Dict[str, int] = {}
        coupled.maybe_start_crisis(world, tracker, rng, events)
        if tracker.active is not None and active_key != tracker.active.start:
            pending = []
            damage_start = tracker.damage_integral
            active_key = tracker.active.start
            env_states = {}
            social_states = {}
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
            action = report117.learned_policy_action(agent, features, base_model, recurrent_states, router, device, "none")
            if active is not None and current_world.time >= 12.0:
                action = choose_source_action(
                    source_policy,
                    agent,
                    features,
                    action_counts,
                    len(living(agents)),
                    base_model,
                    env_model,
                    social_model,
                    recurrent_states,
                    env_states,
                    social_states,
                    router,
                    planner,
                    env_quota,
                    social_quota,
                    strength,
                    device,
                )
                values = report119.policy_features(
                    features,
                    active,
                    action_counts,
                    len(living(agents)),
                    current_world.time,
                    "none",
                )
                pending.append((values, ACTION_TO_INDEX.get(action, ACTION_TO_INDEX["none"])))
            action_counts[action] = action_counts.get(action, 0) + 1
            return action

        base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
        active_before_completion = tracker.active
        report111.update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
        coupled.complete_crisis_if_due(world, agents, tracker, events)
        if active_before_completion is not None and tracker.active is None and pending:
            window_return = report119.crisis_window_return(
                active_before_completion,
                tracker.damage_integral - damage_start,
            )
            sequences.append(ConsequenceSequence(source_policy, window_return, tuple(pending)))
            pending = []
            active_key = None
    if tracker.active is not None:
        active_before_completion = tracker.active
        coupled.complete_crisis_if_due(world, agents, tracker, events)
        if pending:
            window_return = report119.crisis_window_return(active_before_completion, tracker.damage_integral - damage_start)
            sequences.append(ConsequenceSequence(source_policy, window_return, tuple(pending)))
    return sequences


def collect_student_sequences(
    cfg: Config,
    base_model: base.ControllerNet,
    policy_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
    iteration: int,
) -> List[ConsequenceSequence]:
    sequences: List[ConsequenceSequence] = []
    policy_model.eval()
    for seed in cfg.train_seeds:
        rng = random.Random(seed * 239 + CONSEQUENCE_SEED + iteration * 131)
        agents = make_agents(rng, cfg.population)
        world = coupled.prepare_world(rng, cfg)
        condition = CONDITIONS[0]
        previous_actions: Dict[str, int] = {}
        recurrent_states: Dict[str, torch.Tensor] = {}
        events: List[str] = []
        tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
        active_key: Optional[float] = None
        memory_state: Optional[torch.Tensor] = None
        pending: List[Tuple[List[float], int]] = []
        damage_start = 0.0

        while world.time < cfg.hours - 1e-9:
            dt = min(cfg.step_hours, cfg.hours - world.time)
            action_counts: Dict[str, int] = {}
            coupled.maybe_start_crisis(world, tracker, rng, events)
            if tracker.active is not None and active_key != tracker.active.start:
                pending = []
                memory_state = None
                damage_start = tracker.damage_integral
                active_key = tracker.active.start
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
                    values = report119.policy_features(
                        features,
                        active,
                        action_counts,
                        len(living(agents)),
                        current_world.time,
                        "none",
                    )
                    action, memory_state = report121.choose_memory_candidate(
                        policy_model,
                        features,
                        active,
                        action_counts,
                        len(living(agents)),
                        current_world.time,
                        memory_state,
                        device,
                        "none",
                        cfg.policy_temperature,
                        cfg.student_collection_bias,
                    )
                    pending.append((values, ACTION_TO_INDEX.get(action, ACTION_TO_INDEX["none"])))
                if action is None or action == "none":
                    action = report117.learned_policy_action(agent, features, base_model, recurrent_states, router, device, "none")
                action_counts[action] = action_counts.get(action, 0) + 1
                return action

            base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
            active_before_completion = tracker.active
            report111.update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
            coupled.complete_crisis_if_due(world, agents, tracker, events)
            if active_before_completion is not None and tracker.active is None and pending:
                window_return = report119.crisis_window_return(
                    active_before_completion,
                    tracker.damage_integral - damage_start,
                )
                sequences.append(ConsequenceSequence(f"student_iteration_{iteration}", window_return, tuple(pending)))
                pending = []
                memory_state = None
                active_key = None
        if tracker.active is not None and pending:
            active_before_completion = tracker.active
            coupled.complete_crisis_if_due(world, agents, tracker, events)
            window_return = report119.crisis_window_return(active_before_completion, tracker.damage_integral - damage_start)
            sequences.append(ConsequenceSequence(f"student_iteration_{iteration}", window_return, tuple(pending)))
    return sequences


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
    objective = total * 0.40 + crisis * 1.30 + resolved * 0.82 + coupled_response * 1.05 + balance * 0.16 - damage * 0.36
    return total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective


def run_consequence_episode(
    seed: int,
    cfg: Config,
    base_model: base.ControllerNet,
    consequence_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
    policy_bias: float,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, Trace, coupled.CrisisTracker]:
    row, trace_out, tracker = report124.run_distilled_episode(
        seed,
        cfg,
        base_model,
        consequence_model,
        device,
        router,
        policy_bias,
        ablation=ablation,
        trace=trace,
    )
    row = replace(row, controller="consequence_recovery_gru")
    trace_out.condition = f"consequence_recovery_gru:{router.name}:bias_{policy_bias:g}:{ablation}"
    return row, trace_out, tracker


def select_policy_bias(
    cfg: Config,
    base_model: base.ControllerNet,
    consequence_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[float, List[ConsequenceSelectionRow]]:
    best_bias = 0.0
    best_objective = -1e9
    rows: List[ConsequenceSelectionRow] = []
    for bias in cfg.policy_bias_candidates:
        eval_rows = [
            run_consequence_episode(seed, cfg, base_model, consequence_model, device, router, bias)[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_objective = objective
            best_bias = bias
        rows.append(ConsequenceSelectionRow(
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
    base_row = coupled.row_lookup(summary, "consequence_recovery_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = coupled.row_lookup(summary, "consequence_recovery_gru", ablation)
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
    schedules: Sequence[report114.ScheduleRow],
    training_rows: Sequence[ConsequenceTrainingRow],
    source_summary: Sequence[ConsequenceSourceRow],
) -> ConsequenceVerdictRow:
    consequence = coupled.row_lookup(summary, "consequence_recovery_gru", "none")
    teacher = coupled.row_lookup(summary, "min_channel_planner_gru", "none")
    fixed = coupled.row_lookup(summary, "fixed_joint_gru", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    final_training = training_rows[-1]
    source_sequences = sum(row.sequences for row in source_summary if not row.source_policy.startswith("student_iteration"))
    student_sequences = sum(row.sequences for row in source_summary if row.source_policy.startswith("student_iteration"))
    supports_recovery = (
        final_training.weighted_train_accuracy >= 0.55
        and mean_crisis_count >= 4.0
        and consequence.mean_total_score - returned.mean_total_score >= 0.010
        and consequence.mean_crisis_score - returned.mean_crisis_score >= 0.040
        and consequence.mean_resolved_rate - returned.mean_resolved_rate >= 0.080
        and consequence.mean_coupled_response_rate - returned.mean_coupled_response_rate >= 0.080
        and consequence.mean_alive_at_12h >= 12.0
        and consequence.shock_gate_pass_rate == 1.0
        and consequence.post_gate_shock_rate == 1.0
    )
    supports_teacher = (
        consequence.mean_crisis_score >= 0.35
        and consequence.mean_coupled_response_rate >= 0.40
        and teacher.mean_crisis_score - consequence.mean_crisis_score <= 0.30
    )
    supports_dependency = (
        consequence.mean_crisis_score > 0.0
        and social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    return ConsequenceVerdictRow(
        selected_router=router.name,
        selected_planner=planner.name,
        selected_policy_bias=policy_bias,
        source_sequences=source_sequences,
        student_sequences=student_sequences,
        aggregate_examples=final_training.aggregate_examples,
        final_train_accuracy=final_training.train_accuracy,
        final_weighted_train_accuracy=final_training.weighted_train_accuracy,
        consequence_total_score=consequence.mean_total_score,
        min_channel_total_score=teacher.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        consequence_crisis_score=consequence.mean_crisis_score,
        min_channel_crisis_score=teacher.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        consequence_resolved_rate=consequence.mean_resolved_rate,
        min_channel_resolved_rate=teacher.mean_resolved_rate,
        fixed_joint_resolved_rate=fixed.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        consequence_coupled_response=consequence.mean_coupled_response_rate,
        min_channel_coupled_response=teacher.mean_coupled_response_rate,
        fixed_joint_coupled_response=fixed.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        consequence_gain_over_return_selected=consequence.mean_total_score - returned.mean_total_score,
        consequence_gap_to_teacher=teacher.mean_total_score - consequence.mean_total_score,
        consequence_gap_to_fixed_joint=fixed.mean_total_score - consequence.mean_total_score,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=consequence.shock_gate_pass_rate,
        post_gate_shock_rate=consequence.post_gate_shock_rate,
        survival_at_12h=consequence.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_consequence_recovery=supports_recovery,
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
        aggregate = collect_behavior_sequences(
            cfg,
            models["gru"],
            env_model,
            social_model,
            device,
            selected_router,
            selected_planner,
        )
        consequence_model, consequence_training = train_consequence_policy(
            cfg,
            aggregate,
            device,
            0,
            "behavior_sources",
        )
        consequence_training_rows = [consequence_training]
        for iteration in range(1, cfg.student_iterations + 1):
            student_sequences = collect_student_sequences(
                cfg,
                models["gru"],
                consequence_model,
                device,
                selected_router,
                iteration,
            )
            aggregate.extend(student_sequences)
            consequence_model, row = train_consequence_policy(
                cfg,
                aggregate,
                device,
                iteration,
                f"student_iteration_{iteration}",
            )
            consequence_training_rows.append(row)
        source_summary = source_rows(aggregate)
        selected_bias, policy_selection = select_policy_bias(
            cfg,
            models["gru"],
            consequence_model,
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
            consequence_row, maybe_trace, consequence_tracker = run_consequence_episode(
                seed,
                cfg,
                models["gru"],
                consequence_model,
                device,
                selected_router,
                selected_bias,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(consequence_row)
            crisis_logs[f"{seed}:consequence_recovery_gru:none"] = consequence_tracker.response_log
            if seed == cfg.trace_seed:
                trace_out = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker = run_consequence_episode(
                    seed,
                    cfg,
                    models["gru"],
                    consequence_model,
                    device,
                    selected_router,
                    selected_bias,
                    ablation=ablation,
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:consequence_recovery_gru:{ablation}"] = tracker.response_log

        summary = coupled.summarize(eval_rows)
        ablations = ablations_from_summary(summary)
        verdict = transfer_verdict(
            summary,
            ablations,
            selected_router,
            selected_planner,
            selected_bias,
            schedules,
            consequence_training_rows,
            source_summary,
        )

    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "consequence_recovery_gru", "frames": []}
    trace_payload["condition"] = "consequence_recovery_gru"
    payload = {
        "experiment": "ssrm_3d_coupled_crisis_consequence_recovery",
        "config": asdict(cfg),
        "claim": {
            "tested": "completed-crisis consequence weighting can train a recurrent recovery policy that preserves coupled crisis repair after engineered planner removal",
            "remaining_structure": "active crisis candidates and behavior sources are supplied; this is bounded offline/closed-loop consequence training, not open-ended deep RL",
        },
        "action_candidates": list(ACTION_CANDIDATES),
        "source_policies": [
            {"name": name, "env_quota": env, "social_quota": social, "strength": strength}
            for name, env, social, strength in SOURCE_POLICIES
        ],
        "schedule": [asdict(row) for row in schedules],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "router_selection": [asdict(row) for row in router_selection],
        "planner_selection": [asdict(row) for row in planner_selection],
        "source_summary": [asdict(row) for row in source_summary],
        "consequence_training": [asdict(row) for row in consequence_training_rows],
        "policy_selection": [asdict(row) for row in policy_selection],
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
    report124.rows_to_csv(Path(f"{PREFIX}_policy_selection.csv"), policy_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    report124.rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    report124.rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    report124.write_json(Path(f"{PREFIX}_results.json"), payload)
    report124.write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    report124.write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_CONSEQUENCE_RECOVERY_RESULTS", payload)
    report124.write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_CONSEQUENCE_RECOVERY_TRACE", trace_payload)
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
    parser.add_argument("--student-iterations", type=int, default=1)
    parser.add_argument("--student-collection-bias", type=float, default=0.70)
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
        consequence_epochs=args.consequence_epochs,
        consequence_hidden_size=args.consequence_hidden_size,
        consequence_learning_rate=args.consequence_learning_rate,
        consequence_return_scale=args.consequence_return_scale,
        student_iterations=args.student_iterations,
        student_collection_bias=args.student_collection_bias,
        policy_temperature=args.policy_temperature,
        policy_bias_candidates=parse_floats(args.policy_bias_candidates),
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "source_summary": payload["source_summary"],
        "consequence_training": payload["consequence_training"],
        "policy_selection": payload["policy_selection"],
        "verdict": payload["verdict"],
        "summary": payload["summary"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
