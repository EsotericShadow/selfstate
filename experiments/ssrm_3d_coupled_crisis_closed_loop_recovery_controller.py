#!/usr/bin/env python3
"""Closed-loop recovery training for SSRM-3D coupled crises.

Report 124 showed that high offline imitation of the minimum-channel planner
does not preserve held-out crisis repair after the planner is removed. This
benchmark adds a narrow DAgger-style recovery step: the student policy acts in
training worlds, the successful planner relabels the states the student
actually visits, and the recurrent policy retrains on the aggregate.

The planner is still removed at evaluation. This is bounded closed-loop
recovery evidence, not open-ended civilization, unsupplied action discovery,
subjective consciousness, or mature deep reinforcement learning.
"""

from __future__ import annotations

import argparse
import json
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
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_closed_loop_recovery"
RECOVERY_SEED = 20262031
ACTION_CANDIDATES = report121.ACTION_CANDIDATES
ACTION_TO_INDEX = report121.ACTION_TO_INDEX


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
    distill_epochs: int = 12
    distill_hidden_size: int = 64
    distill_learning_rate: float = 0.003
    recovery_iterations: int = 2
    recovery_epochs: int = 6
    recovery_hidden_size: int = 64
    recovery_learning_rate: float = 0.003
    recovery_collection_bias: float = 0.70
    policy_temperature: float = 1.0
    policy_bias_candidates: Sequence[float] = (0.0, 0.20, 0.40, 0.70, 1.00)
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class RecoveryTrainingRow:
    iteration: int
    source: str
    collected_sequences: int
    collected_examples: int
    aggregate_sequences: int
    aggregate_examples: int
    epochs: int
    final_loss: float
    train_accuracy: float
    env_action_fraction: float
    social_action_fraction: float
    none_fraction: float
    mean_sequence_length: float
    collection_policy_bias: float
    device_used: str
    parameter_count: int


@dataclass(frozen=True)
class RecoverySelectionRow:
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
class VerdictRow:
    selected_router: str
    selected_planner: str
    selected_policy_bias: float
    teacher_sequences: int
    recovery_sequences: int
    aggregate_examples: int
    final_recovery_train_accuracy: float
    recovery_total_score: float
    min_channel_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    recovery_crisis_score: float
    min_channel_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    recovery_resolved_rate: float
    min_channel_resolved_rate: float
    fixed_joint_resolved_rate: float
    return_selected_resolved_rate: float
    recovery_coupled_response: float
    min_channel_coupled_response: float
    fixed_joint_coupled_response: float
    return_selected_coupled_response: float
    recovery_gain_over_return_selected: float
    recovery_gap_to_teacher: float
    recovery_gap_to_fixed_joint: float
    social_culture_crisis_loss: float
    environment_crisis_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    mean_crisis_count: float
    supports_closed_loop_recovery: bool
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


def sequence_stats(sequences: Sequence[Sequence[Tuple[List[float], int]]]) -> Tuple[int, int, float, float, float, float]:
    counts = {action: 0 for action in ACTION_CANDIDATES}
    total = 0
    for sequence in sequences:
        for _, index in sequence:
            counts[ACTION_CANDIDATES[index]] += 1
            total += 1
    env_count = sum(counts.get(action, 0) for action in report111.ENV_RESPONSE_ACTIONS)
    social_count = sum(counts.get(action, 0) for action in report111.SOCIAL_RESPONSE_ACTIONS)
    none_count = counts.get("none", 0)
    return (
        len(sequences),
        total,
        env_count / max(1, total),
        social_count / max(1, total),
        none_count / max(1, total),
        mean(len(sequence) for sequence in sequences),
    )


def train_policy_model(
    cfg: Config,
    sequences: Sequence[Sequence[Tuple[List[float], int]]],
    device: torch.device,
    epochs: int,
    seed: int,
) -> Tuple[report121.CrisisMemoryPolicyNet, float, float]:
    if not sequences:
        raise RuntimeError("no recovery sequences collected")
    torch.manual_seed(seed)
    model = report121.CrisisMemoryPolicyNet(cfg.recovery_hidden_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.recovery_learning_rate)
    final_loss = 0.0
    for _ in range(epochs):
        for sequence in sequences:
            x = torch.tensor([[item[0] for item in sequence]], dtype=torch.float32, device=device)
            y = torch.tensor([item[1] for item in sequence], dtype=torch.long, device=device)
            logits, _ = model.forward_sequence(x)
            logits = report119.masked_logits(logits.squeeze(0), "none", 0.0)
            loss = F.cross_entropy(logits, y)
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 2.0)
            optimizer.step()
            final_loss = float(loss.detach().cpu().item())
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for sequence in sequences:
            x = torch.tensor([[item[0] for item in sequence]], dtype=torch.float32, device=device)
            y = torch.tensor([item[1] for item in sequence], dtype=torch.long, device=device)
            logits, _ = model.forward_sequence(x)
            pred = report119.masked_logits(logits.squeeze(0), "none", 0.0).argmax(dim=-1)
            correct += int((pred == y).sum().item())
            total += int(y.numel())
    return model, final_loss, correct / max(1, total)


def train_recovery_policy(
    cfg: Config,
    aggregate: Sequence[Sequence[Tuple[List[float], int]]],
    collected: Sequence[Sequence[Tuple[List[float], int]]],
    device: torch.device,
    iteration: int,
    source: str,
) -> Tuple[report121.CrisisMemoryPolicyNet, RecoveryTrainingRow]:
    model, final_loss, train_accuracy = train_policy_model(
        cfg,
        aggregate,
        device,
        cfg.recovery_epochs,
        RECOVERY_SEED + iteration * 97,
    )
    collected_sequences, collected_examples, _, _, _, _ = sequence_stats(collected)
    aggregate_sequences, aggregate_examples, env_fraction, social_fraction, none_fraction, mean_length = sequence_stats(aggregate)
    return model, RecoveryTrainingRow(
        iteration=iteration,
        source=source,
        collected_sequences=collected_sequences,
        collected_examples=collected_examples,
        aggregate_sequences=aggregate_sequences,
        aggregate_examples=aggregate_examples,
        epochs=cfg.recovery_epochs,
        final_loss=final_loss,
        train_accuracy=train_accuracy,
        env_action_fraction=env_fraction,
        social_action_fraction=social_fraction,
        none_fraction=none_fraction,
        mean_sequence_length=mean_length,
        collection_policy_bias=cfg.recovery_collection_bias,
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in model.parameters()),
    )


def collect_recovery_sequences(
    cfg: Config,
    base_model: base.ControllerNet,
    student_model: report121.CrisisMemoryPolicyNet,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
    planner: report123.PlannerCandidate,
    iteration: int,
) -> List[List[Tuple[List[float], int]]]:
    sequences: List[List[Tuple[List[float], int]]] = []
    condition = CONDITIONS[0]
    student_model.eval()
    with report123.patched_min_channel_planner(planner):
        for seed in cfg.train_seeds:
            rng = random.Random(seed * 191 + RECOVERY_SEED + iteration * 1009)
            agents = make_agents(rng, cfg.population)
            world = coupled.prepare_world(rng, cfg)
            previous_actions: Dict[str, int] = {}
            recurrent_states: Dict[str, torch.Tensor] = {}
            env_states: Dict[str, torch.Tensor] = {}
            social_states: Dict[str, torch.Tensor] = {}
            events: List[str] = []
            tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
            active_key: Optional[float] = None
            memory_state: Optional[torch.Tensor] = None
            pending: List[Tuple[List[float], int]] = []

            while world.time < cfg.hours - 1e-9:
                dt = min(cfg.step_hours, cfg.hours - world.time)
                action_counts: Dict[str, int] = {}
                coupled.maybe_start_crisis(world, tracker, rng, events)
                if tracker.active is not None and active_key != tracker.active.start:
                    if pending:
                        sequences.append(pending)
                    pending = []
                    memory_state = None
                    env_states = {}
                    social_states = {}
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
                        label_action = report124.teacher_action(
                            agent.ident,
                            features,
                            action_counts,
                            len(living(agents)),
                            env_model,
                            social_model,
                            env_states,
                            social_states,
                            device,
                        )
                        label = label_action if label_action in ACTION_TO_INDEX else "none"
                        pending.append((values, ACTION_TO_INDEX[label]))
                        action, next_state = report121.choose_memory_candidate(
                            student_model,
                            features,
                            active,
                            action_counts,
                            len(living(agents)),
                            current_world.time,
                            memory_state,
                            device,
                            "none",
                            cfg.policy_temperature,
                            cfg.recovery_collection_bias,
                        )
                        memory_state = next_state
                    if action is None or action == "none":
                        action = report117.learned_policy_action(
                            agent,
                            features,
                            base_model,
                            recurrent_states,
                            router,
                            device,
                            "none",
                        )
                    action_counts[action] = action_counts.get(action, 0) + 1
                    return action

                base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
                report111.update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
                coupled.complete_crisis_if_due(world, agents, tracker, events)
                if tracker.active is None and pending:
                    sequences.append(pending)
                    pending = []
                    memory_state = None
                    active_key = None
            if pending:
                sequences.append(pending)
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
    objective = total * 0.44 + crisis * 1.20 + resolved * 0.72 + coupled_response * 0.90 + balance * 0.14 - damage * 0.34
    return total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective


def run_recovery_episode(
    seed: int,
    cfg: Config,
    base_model: base.ControllerNet,
    recovery_model: report121.CrisisMemoryPolicyNet,
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
        recovery_model,
        device,
        router,
        policy_bias,
        ablation=ablation,
        trace=trace,
    )
    row = replace(row, controller="planner_recovery_gru")
    trace_out.condition = f"planner_recovery_gru:{router.name}:bias_{policy_bias:g}:{ablation}"
    return row, trace_out, tracker


def select_policy_bias(
    cfg: Config,
    base_model: base.ControllerNet,
    recovery_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[float, List[RecoverySelectionRow]]:
    best_bias = 0.0
    best_objective = -1e9
    rows: List[RecoverySelectionRow] = []
    for bias in cfg.policy_bias_candidates:
        eval_rows = [
            run_recovery_episode(seed, cfg, base_model, recovery_model, device, router, bias)[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_objective = objective
            best_bias = bias
        rows.append(RecoverySelectionRow(
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
    base_row = coupled.row_lookup(summary, "planner_recovery_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = coupled.row_lookup(summary, "planner_recovery_gru", ablation)
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
    training_rows: Sequence[RecoveryTrainingRow],
) -> VerdictRow:
    recovery = coupled.row_lookup(summary, "planner_recovery_gru", "none")
    teacher = coupled.row_lookup(summary, "min_channel_planner_gru", "none")
    fixed = coupled.row_lookup(summary, "fixed_joint_gru", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    final_training = training_rows[-1]
    teacher_sequences = training_rows[0].collected_sequences
    recovery_sequences = sum(row.collected_sequences for row in training_rows[1:])
    supports_recovery = (
        final_training.train_accuracy >= 0.55
        and recovery_sequences > 0
        and mean_crisis_count >= 4.0
        and recovery.mean_total_score - returned.mean_total_score >= 0.010
        and recovery.mean_crisis_score - returned.mean_crisis_score >= 0.040
        and recovery.mean_resolved_rate - returned.mean_resolved_rate >= 0.080
        and recovery.mean_coupled_response_rate - returned.mean_coupled_response_rate >= 0.080
        and recovery.mean_alive_at_12h >= 12.0
        and recovery.shock_gate_pass_rate == 1.0
        and recovery.post_gate_shock_rate == 1.0
    )
    supports_teacher = (
        recovery.mean_crisis_score >= 0.35
        and recovery.mean_coupled_response_rate >= 0.40
        and teacher.mean_crisis_score - recovery.mean_crisis_score <= 0.30
    )
    supports_dependency = (
        recovery.mean_crisis_score > 0.0
        and social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    return VerdictRow(
        selected_router=router.name,
        selected_planner=planner.name,
        selected_policy_bias=policy_bias,
        teacher_sequences=teacher_sequences,
        recovery_sequences=recovery_sequences,
        aggregate_examples=final_training.aggregate_examples,
        final_recovery_train_accuracy=final_training.train_accuracy,
        recovery_total_score=recovery.mean_total_score,
        min_channel_total_score=teacher.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        recovery_crisis_score=recovery.mean_crisis_score,
        min_channel_crisis_score=teacher.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        recovery_resolved_rate=recovery.mean_resolved_rate,
        min_channel_resolved_rate=teacher.mean_resolved_rate,
        fixed_joint_resolved_rate=fixed.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        recovery_coupled_response=recovery.mean_coupled_response_rate,
        min_channel_coupled_response=teacher.mean_coupled_response_rate,
        fixed_joint_coupled_response=fixed.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        recovery_gain_over_return_selected=recovery.mean_total_score - returned.mean_total_score,
        recovery_gap_to_teacher=teacher.mean_total_score - recovery.mean_total_score,
        recovery_gap_to_fixed_joint=fixed.mean_total_score - recovery.mean_total_score,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=recovery.shock_gate_pass_rate,
        post_gate_shock_rate=recovery.post_gate_shock_rate,
        survival_at_12h=recovery.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_closed_loop_recovery=supports_recovery,
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
        teacher_sequences = report124.collect_teacher_sequences(
            cfg,
            models["gru"],
            env_model,
            social_model,
            device,
            selected_router,
            selected_planner,
        )
        aggregate: List[List[Tuple[List[float], int]]] = list(teacher_sequences)
        student_model, initial_loss, initial_accuracy = train_policy_model(
            cfg,
            aggregate,
            device,
            cfg.distill_epochs,
            RECOVERY_SEED,
        )
        teacher_sequence_count, teacher_examples, env_fraction, social_fraction, none_fraction, mean_length = sequence_stats(teacher_sequences)
        recovery_rows: List[RecoveryTrainingRow] = [
            RecoveryTrainingRow(
                iteration=0,
                source="planner_teacher",
                collected_sequences=teacher_sequence_count,
                collected_examples=teacher_examples,
                aggregate_sequences=teacher_sequence_count,
                aggregate_examples=teacher_examples,
                epochs=cfg.distill_epochs,
                final_loss=initial_loss,
                train_accuracy=initial_accuracy,
                env_action_fraction=env_fraction,
                social_action_fraction=social_fraction,
                none_fraction=none_fraction,
                mean_sequence_length=mean_length,
                collection_policy_bias=0.0,
                device_used=str(device),
                parameter_count=sum(parameter.numel() for parameter in student_model.parameters()),
            )
        ]
        for iteration in range(1, cfg.recovery_iterations + 1):
            collected = collect_recovery_sequences(
                cfg,
                models["gru"],
                student_model,
                env_model,
                social_model,
                device,
                selected_router,
                selected_planner,
                iteration,
            )
            aggregate.extend(collected)
            student_model, row = train_recovery_policy(
                cfg,
                aggregate,
                collected,
                device,
                iteration,
                "student_recovery",
            )
            recovery_rows.append(row)

        selected_bias, policy_selection = select_policy_bias(cfg, models["gru"], student_model, device, selected_router)

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
                row, maybe_trace, tracker = report113.run_episode(
                    seed,
                    cfg,
                    controller,
                    model,
                    env_model,
                    social_model,
                    device,
                    router,
                    0.0,
                    0.0,
                    0.0,
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:{controller}:none"] = tracker.response_log
                if maybe_trace.frames:
                    trace_out = maybe_trace
            fixed_row = report123.run_fixed_joint_episode(seed, cfg, models["gru"], env_model, social_model, device, selected_router)
            eval_rows.append(fixed_row)
            teacher_row, maybe_trace, tracker = report123.run_min_channel_episode(
                seed,
                cfg,
                models["gru"],
                env_model,
                social_model,
                device,
                selected_router,
                selected_planner,
            )
            eval_rows.append(teacher_row)
            crisis_logs[f"{seed}:fixed_joint_gru:none"] = []
            crisis_logs[f"{seed}:min_channel_planner_gru:none"] = tracker.response_log
            recovery_row, maybe_trace, tracker = run_recovery_episode(
                seed,
                cfg,
                models["gru"],
                student_model,
                device,
                selected_router,
                selected_bias,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(recovery_row)
            crisis_logs[f"{seed}:planner_recovery_gru:none"] = tracker.response_log
            if maybe_trace.frames:
                trace_out = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker = run_recovery_episode(
                    seed,
                    cfg,
                    models["gru"],
                    student_model,
                    device,
                    selected_router,
                    selected_bias,
                    ablation=ablation,
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:planner_recovery_gru:{ablation}"] = tracker.response_log

    summary = coupled.summarize(eval_rows)
    ablations = ablations_from_summary(summary)
    verdict = transfer_verdict(summary, ablations, selected_router, selected_planner, selected_bias, schedules, recovery_rows)
    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "planner_recovery", "frames": []}
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
            "distill_epochs": cfg.distill_epochs,
            "distill_hidden_size": cfg.distill_hidden_size,
            "recovery_iterations": cfg.recovery_iterations,
            "recovery_epochs": cfg.recovery_epochs,
            "recovery_hidden_size": cfg.recovery_hidden_size,
            "recovery_collection_bias": cfg.recovery_collection_bias,
            "policy_bias_candidates": list(cfg.policy_bias_candidates),
            "device": cfg.device,
            "trace_seed": cfg.trace_seed,
        },
        "schedule": [asdict(row) for row in schedules],
        "router_selection": [asdict(row) for row in router_selection],
        "planner_selection": [asdict(row) for row in planner_selection],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "recovery_training": [asdict(row) for row in recovery_rows],
        "policy_selection": [asdict(row) for row in policy_selection],
        "action_candidates": list(ACTION_CANDIDATES),
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace_payload,
        "crisis_logs": crisis_logs,
        "notes": {
            "claim": "student-visited active-crisis states can be relabeled by the planner to improve closed-loop planner removal",
            "not_claimed": "open-ended civilization, subjective consciousness, unsupplied action discovery, or mature deep reinforcement learning",
            "remaining_structure": "candidate crisis actions and the relabeling planner remain supplied; the planner is removed only at evaluation",
        },
    }
    report124.rows_to_csv(Path(f"{PREFIX}_schedule.csv"), schedules)
    report124.rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_action_training.csv"), [env_training, social_training])
    report124.rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_planner_selection.csv"), planner_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_recovery_training.csv"), recovery_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_policy_selection.csv"), policy_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    report124.rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    report124.rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    report124.write_json(Path(f"{PREFIX}_results.json"), payload)
    report124.write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    report124.write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_CLOSED_LOOP_RECOVERY_RESULTS", payload)
    report124.write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_CLOSED_LOOP_RECOVERY_TRACE", trace_payload)
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
    parser.add_argument("--distill-epochs", type=int, default=12)
    parser.add_argument("--distill-hidden-size", type=int, default=64)
    parser.add_argument("--distill-learning-rate", type=float, default=0.003)
    parser.add_argument("--recovery-iterations", type=int, default=2)
    parser.add_argument("--recovery-epochs", type=int, default=6)
    parser.add_argument("--recovery-hidden-size", type=int, default=64)
    parser.add_argument("--recovery-learning-rate", type=float, default=0.003)
    parser.add_argument("--recovery-collection-bias", type=float, default=0.70)
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
        distill_epochs=args.distill_epochs,
        distill_hidden_size=args.distill_hidden_size,
        distill_learning_rate=args.distill_learning_rate,
        recovery_iterations=args.recovery_iterations,
        recovery_epochs=args.recovery_epochs,
        recovery_hidden_size=args.recovery_hidden_size,
        recovery_learning_rate=args.recovery_learning_rate,
        recovery_collection_bias=args.recovery_collection_bias,
        policy_temperature=args.policy_temperature,
        policy_bias_candidates=parse_floats(args.policy_bias_candidates),
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "recovery_training": payload["recovery_training"],
        "policy_selection": payload["policy_selection"],
        "verdict": payload["verdict"],
        "summary": payload["summary"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
