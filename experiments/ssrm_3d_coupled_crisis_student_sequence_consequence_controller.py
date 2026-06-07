#!/usr/bin/env python3
"""Student-created sequence consequence control for SSRM-3D coupled crises.

Reports 132 and 133 show the current learned-transfer failure: an MPC sequence
teacher can repair coupled environmental/social crises, but recurrent students
trained from teacher labels lose that coupled behavior once rollout scoring is
removed.

This benchmark tests the next narrower claim. A consequence-trained student acts
in training worlds. At the active-crisis states the student actually creates, an
MPC teacher supplies counterfactual multi-action labels and plan values. The
final recurrent policy is trained on those student-created sequence windows with
consequence weighting, then evaluated without MPC, rollout scoring, supplied
plan templates, or planner calls.

This is still bounded evidence. It uses supplied active-crisis action
candidates and a simulator teacher during data generation. It is not open-ended
civilization, subjective consciousness, unsupplied action discovery, or mature
deep reinforcement learning.
"""

from __future__ import annotations

import argparse
import json
import random
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import torch

import ssrm_3d_coupled_crisis_active_policy_controller as report119
import ssrm_3d_coupled_crisis_active_state_value_controller as report117
import ssrm_3d_coupled_crisis_consequence_recovery_controller as report126
import ssrm_3d_coupled_crisis_joint_arbitration_controller as report113
import ssrm_3d_coupled_crisis_memory_policy_controller as report121
import ssrm_3d_coupled_crisis_min_channel_planner_controller as report123
import ssrm_3d_coupled_crisis_mpc_sequence_optimizer_controller as report131
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
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_student_sequence_consequence"
STUDENT_SEQUENCE_SEED = 20262941
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
    student_sequence_iterations: int = 1
    student_sequence_epochs: int = 8
    student_sequence_return_scale: float = 1.35
    student_collection_bias: float = 0.70
    counterfactual_collection_bias: float = 0.80
    teacher_commit_actions: int = 14
    policy_temperature: float = 1.0
    policy_bias_candidates: Sequence[float] = (0.0, 0.40, 0.80, 1.20)
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class StudentWindowRow:
    iteration: int
    seed: int
    sequences: int
    examples: int
    mean_actual_return: float
    mean_counterfactual_return: float
    mean_plan_value: float
    mean_plan_margin: float
    positive_return_rate: float
    env_action_fraction: float
    social_action_fraction: float
    none_fraction: float
    mean_sequence_length: float
    teacher_commit_actions: int
    collection_policy_bias: float


@dataclass(frozen=True)
class StudentSequenceSelectionRow:
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
class StudentSequenceVerdictRow:
    selected_router: str
    selected_planner: str
    selected_consequence_bias: float
    selected_student_bias: float
    teacher_commit_actions: int
    source_sequences: int
    student_counterfactual_sequences: int
    aggregate_examples: int
    initial_train_accuracy: float
    final_train_accuracy: float
    final_weighted_train_accuracy: float
    student_total_score: float
    mpc_teacher_total_score: float
    consequence_total_score: float
    min_channel_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    student_crisis_score: float
    mpc_teacher_crisis_score: float
    consequence_crisis_score: float
    min_channel_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    student_resolved_rate: float
    mpc_teacher_resolved_rate: float
    consequence_resolved_rate: float
    return_selected_resolved_rate: float
    student_coupled_response: float
    mpc_teacher_coupled_response: float
    consequence_coupled_response: float
    return_selected_coupled_response: float
    student_gain_over_consequence: float
    student_gain_over_return_selected: float
    student_gap_to_mpc_teacher: float
    social_culture_crisis_loss: float
    environment_crisis_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    mean_crisis_count: float
    supports_student_sequence_consequence: bool
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


def bounded(value: float, low: float = -1.2, high: float = 1.8) -> float:
    return max(low, min(high, value))


def plan_margin(scores: Dict[str, float]) -> float:
    values = sorted((float(value) for value in scores.values()), reverse=True)
    if len(values) < 2:
        return 0.0
    return max(0.0, values[0] - values[1])


def action_fractions(sequence: Sequence[Tuple[List[float], int]]) -> Tuple[float, float, float]:
    total = max(1, len(sequence))
    env_count = 0
    social_count = 0
    none_count = 0
    for _, index in sequence:
        action = ACTION_CANDIDATES[index]
        if action in report111.ENV_RESPONSE_ACTIONS:
            env_count += 1
        if action in report111.SOCIAL_RESPONSE_ACTIONS:
            social_count += 1
        if action == "none":
            none_count += 1
    return env_count / total, social_count / total, none_count / total


def counterfactual_sequence_return(
    actual_return: float,
    plan_values: Sequence[float],
    margins: Sequence[float],
    sequence: Sequence[Tuple[List[float], int]],
) -> float:
    plan_value = bounded(mean(plan_values))
    margin = min(1.0, mean(margins))
    env_fraction, social_fraction, _ = action_fractions(sequence)
    balance_bonus = 0.12 * (1.0 - abs(env_fraction - social_fraction))
    value = 0.52 * plan_value + 0.22 * actual_return + 0.16 * margin + balance_bonus
    return bounded(value)


def make_student_window_row(
    iteration: int,
    seed: int,
    sequences: Sequence[report126.ConsequenceSequence],
    actual_returns: Sequence[float],
    plan_values: Sequence[float],
    margins: Sequence[float],
    cfg: Config,
) -> StudentWindowRow:
    _, examples, mean_return, _, _, positive, env_fraction, social_fraction, none_fraction = report126.sequence_stats(sequences)
    return StudentWindowRow(
        iteration=iteration,
        seed=seed,
        sequences=len(sequences),
        examples=examples,
        mean_actual_return=mean(actual_returns),
        mean_counterfactual_return=mean_return,
        mean_plan_value=mean(plan_values),
        mean_plan_margin=mean(margins),
        positive_return_rate=positive,
        env_action_fraction=env_fraction,
        social_action_fraction=social_fraction,
        none_fraction=none_fraction,
        mean_sequence_length=examples / max(1, len(sequences)),
        teacher_commit_actions=cfg.teacher_commit_actions,
        collection_policy_bias=cfg.counterfactual_collection_bias,
    )


def collect_student_counterfactual_sequences(
    cfg: Config,
    base_model: base.ControllerNet,
    acting_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
    iteration: int,
) -> Tuple[List[report126.ConsequenceSequence], List[StudentWindowRow], List[report131.MpcPlanUseRow]]:
    sequences: List[report126.ConsequenceSequence] = []
    diagnostics: List[StudentWindowRow] = []
    plan_logs: Dict[str, object] = {}
    condition = CONDITIONS[0]
    acting_model.eval()
    for seed in cfg.train_seeds:
        rng = random.Random(seed * 251 + STUDENT_SEQUENCE_SEED + iteration * 1009)
        agents = make_agents(rng, cfg.population)
        world = coupled.prepare_world(rng, cfg)
        previous_actions: Dict[str, int] = {}
        student_recurrent_states: Dict[str, torch.Tensor] = {}
        teacher_recurrent_states: Dict[str, torch.Tensor] = {}
        events: List[str] = []
        tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
        active_key: Optional[float] = None
        memory_state: Optional[torch.Tensor] = None
        pending: List[Tuple[List[float], int]] = []
        pending_actual_returns: List[float] = []
        pending_plan_values: List[float] = []
        pending_margins: List[float] = []
        seed_sequences: List[report126.ConsequenceSequence] = []
        seed_actual_returns: List[float] = []
        seed_plan_values: List[float] = []
        seed_margins: List[float] = []
        plan_state: Dict[str, object] = {}
        seed_plan_log: List[dict[str, object]] = []
        damage_start = 0.0

        def finish_window(active: coupled.ActiveCrisis) -> None:
            nonlocal pending, pending_actual_returns, pending_plan_values, pending_margins
            if not pending:
                return
            actual_return = report119.crisis_window_return(
                active,
                tracker.damage_integral - damage_start,
            )
            seq_return = counterfactual_sequence_return(
                actual_return,
                pending_plan_values,
                pending_margins,
                pending,
            )
            sequence = report126.ConsequenceSequence(
                f"student_counterfactual_iteration_{iteration}",
                seq_return,
                tuple(pending),
            )
            sequences.append(sequence)
            seed_sequences.append(sequence)
            pending_actual_returns.append(actual_return)
            seed_actual_returns.append(actual_return)
            seed_plan_values.extend(pending_plan_values)
            seed_margins.extend(pending_margins)
            pending = []
            pending_plan_values = []
            pending_margins = []

        while world.time < cfg.hours - 1e-9:
            dt = min(cfg.step_hours, cfg.hours - world.time)
            action_counts: Dict[str, int] = {}
            coupled.maybe_start_crisis(world, tracker, rng, events)
            if tracker.active is not None and active_key != tracker.active.start:
                pending = []
                pending_actual_returns = []
                pending_plan_values = []
                pending_margins = []
                memory_state = None
                active_key = tracker.active.start
                damage_start = tracker.damage_integral
                plan_state = {}
                teacher_recurrent_states = {}
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
                    plan = report131.update_plan_state(
                        plan_state,
                        seed,
                        current_world,
                        agents,
                        tracker,
                        previous_actions,
                        cfg,
                        cfg.teacher_commit_actions,
                        "none",
                        seed_plan_log,
                    )
                    scores = dict(plan_state.get("scores", {}))  # type: ignore[arg-type]
                    pending_plan_values.append(float(plan_state.get("value", 0.0)))
                    pending_margins.append(plan_margin(scores))
                    teacher_action = report131.masked_plan_action(plan, active, features, current_rng, "none")
                    plan_state["remaining"] = int(plan_state.get("remaining", 1)) - 1
                    if teacher_action == "none":
                        teacher_action = report117.learned_policy_action(
                            agent,
                            features,
                            base_model,
                            teacher_recurrent_states,
                            router,
                            device,
                            "none",
                        )
                    label = teacher_action if teacher_action in ACTION_TO_INDEX else "none"
                    pending.append((values, ACTION_TO_INDEX[label]))
                    action, memory_state = report121.choose_memory_candidate(
                        acting_model,
                        features,
                        active,
                        action_counts,
                        len(living(agents)),
                        current_world.time,
                        memory_state,
                        device,
                        "none",
                        cfg.policy_temperature,
                        cfg.counterfactual_collection_bias,
                    )
                if action is None or action == "none":
                    action = report117.learned_policy_action(
                        agent,
                        features,
                        base_model,
                        student_recurrent_states,
                        router,
                        device,
                        "none",
                    )
                action_counts[action] = action_counts.get(action, 0) + 1
                return action

            base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
            active_before_completion = tracker.active
            report111.update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
            coupled.complete_crisis_if_due(world, agents, tracker, events)
            if active_before_completion is not None and tracker.active is None:
                finish_window(active_before_completion)
                active_key = None
                memory_state = None
                plan_state = {}
        if tracker.active is not None and pending:
            active_before_completion = tracker.active
            coupled.complete_crisis_if_due(world, agents, tracker, events)
            finish_window(active_before_completion)
        diagnostics.append(make_student_window_row(
            iteration,
            seed,
            seed_sequences,
            seed_actual_returns,
            seed_plan_values,
            seed_margins,
            cfg,
        ))
        plan_logs[f"{seed}:student_counterfactual_iteration_{iteration}:none"] = seed_plan_log
    return sequences, diagnostics, report131.plan_use_rows(plan_logs)


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
    objective = total * 0.32 + crisis * 1.45 + resolved * 0.88 + coupled_response * 1.20 + balance * 0.18 - damage * 0.38
    return total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective


def run_student_sequence_episode(
    seed: int,
    cfg: Config,
    model: base.ControllerNet,
    policy_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
    policy_bias: float,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, Trace, coupled.CrisisTracker]:
    row, trace_out, tracker = report121.run_memory_policy_episode(
        seed,
        cfg,
        "memory_policy_gru",
        model,
        policy_model,
        device,
        router,
        policy_bias=policy_bias,
        ablation=ablation,
        trace=trace,
    )
    row = replace(row, controller="student_sequence_consequence_gru")
    trace_out.condition = f"student_sequence_consequence_gru:{router.name}:bias_{policy_bias:g}:{ablation}"
    return row, trace_out, tracker


def select_student_policy_bias(
    cfg: Config,
    base_model: base.ControllerNet,
    policy_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[float, List[StudentSequenceSelectionRow]]:
    best_bias = 0.0
    best_objective = -1e9
    rows: List[StudentSequenceSelectionRow] = []
    for bias in cfg.policy_bias_candidates:
        eval_rows = [
            run_student_sequence_episode(seed, cfg, base_model, policy_model, device, router, bias)[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_objective = objective
            best_bias = bias
        rows.append(StudentSequenceSelectionRow(
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
    base_row = coupled.row_lookup(summary, "student_sequence_consequence_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = coupled.row_lookup(summary, "student_sequence_consequence_gru", ablation)
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
    selected_consequence_bias: float,
    selected_student_bias: float,
    teacher_commit_actions: int,
    schedules: Sequence[report114.ScheduleRow],
    training_rows: Sequence[report126.ConsequenceTrainingRow],
    source_summary: Sequence[report126.ConsequenceSourceRow],
) -> StudentSequenceVerdictRow:
    student = coupled.row_lookup(summary, "student_sequence_consequence_gru", "none")
    mpc = coupled.row_lookup(summary, "mpc_sequence_optimizer_gru", "none")
    consequence = coupled.row_lookup(summary, "consequence_recovery_gru", "none")
    teacher = coupled.row_lookup(summary, "min_channel_planner_gru", "none")
    fixed = coupled.row_lookup(summary, "fixed_joint_gru", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    initial_training = training_rows[0]
    final_training = training_rows[-1]
    source_sequences = sum(row.sequences for row in source_summary if not row.source_policy.startswith("student_counterfactual"))
    student_sequences = sum(row.sequences for row in source_summary if row.source_policy.startswith("student_counterfactual"))
    supports_sequence = (
        final_training.weighted_train_accuracy >= 0.55
        and mean_crisis_count >= 4.0
        and student.mean_total_score - consequence.mean_total_score >= 0.005
        and student.mean_crisis_score - consequence.mean_crisis_score >= 0.020
        and student.mean_coupled_response_rate - consequence.mean_coupled_response_rate >= 0.020
        and student.mean_crisis_score > 0.0
        and student.mean_coupled_response_rate > 0.0
        and student.mean_alive_at_12h >= 12.0
        and student.shock_gate_pass_rate == 1.0
        and student.post_gate_shock_rate == 1.0
    )
    supports_teacher = (
        student.mean_crisis_score >= 0.35
        and student.mean_coupled_response_rate >= 0.40
        and mpc.mean_crisis_score - student.mean_crisis_score <= 0.30
    )
    supports_dependency = (
        student.mean_crisis_score > 0.0
        and social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    return StudentSequenceVerdictRow(
        selected_router=router.name,
        selected_planner=planner.name,
        selected_consequence_bias=selected_consequence_bias,
        selected_student_bias=selected_student_bias,
        teacher_commit_actions=teacher_commit_actions,
        source_sequences=source_sequences,
        student_counterfactual_sequences=student_sequences,
        aggregate_examples=final_training.aggregate_examples,
        initial_train_accuracy=initial_training.train_accuracy,
        final_train_accuracy=final_training.train_accuracy,
        final_weighted_train_accuracy=final_training.weighted_train_accuracy,
        student_total_score=student.mean_total_score,
        mpc_teacher_total_score=mpc.mean_total_score,
        consequence_total_score=consequence.mean_total_score,
        min_channel_total_score=teacher.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        student_crisis_score=student.mean_crisis_score,
        mpc_teacher_crisis_score=mpc.mean_crisis_score,
        consequence_crisis_score=consequence.mean_crisis_score,
        min_channel_crisis_score=teacher.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        student_resolved_rate=student.mean_resolved_rate,
        mpc_teacher_resolved_rate=mpc.mean_resolved_rate,
        consequence_resolved_rate=consequence.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        student_coupled_response=student.mean_coupled_response_rate,
        mpc_teacher_coupled_response=mpc.mean_coupled_response_rate,
        consequence_coupled_response=consequence.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        student_gain_over_consequence=student.mean_total_score - consequence.mean_total_score,
        student_gain_over_return_selected=student.mean_total_score - returned.mean_total_score,
        student_gap_to_mpc_teacher=mpc.mean_total_score - student.mean_total_score,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=student.shock_gate_pass_rate,
        post_gate_shock_rate=student.post_gate_shock_rate,
        survival_at_12h=student.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_student_sequence_consequence=supports_sequence,
        supports_teacher_transfer=supports_teacher,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_sequence and supports_teacher and supports_dependency else "partial_or_failed",
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
            20262951,
        )
        social_model, social_training = report113.train_action_model(
            cfg,
            device,
            "social",
            social_sequences,
            social_labels,
            flags,
            20262952,
        )
        selected_planner, planner_selection = report123.select_planner(
            cfg,
            models["gru"],
            env_model,
            social_model,
            device,
            selected_router,
        )
        behavior_sequences = report126.collect_behavior_sequences(
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
            behavior_sequences,
            device,
            0,
            "behavior_sources",
        )
        consequence_training_rows: List[report126.ConsequenceTrainingRow] = [consequence_training]
        selected_consequence_bias, consequence_selection = report126.select_policy_bias(
            cfg,
            models["gru"],
            consequence_model,
            device,
            selected_router,
        )

        aggregate: List[report126.ConsequenceSequence] = list(behavior_sequences)
        student_window_rows: List[StudentWindowRow] = []
        student_plan_use: List[report131.MpcPlanUseRow] = []
        student_model = consequence_model
        student_cfg = replace(
            cfg,
            consequence_epochs=cfg.student_sequence_epochs,
            consequence_return_scale=cfg.student_sequence_return_scale,
        )
        for iteration in range(1, cfg.student_sequence_iterations + 1):
            student_sequences, window_rows, plan_use = collect_student_counterfactual_sequences(
                cfg,
                models["gru"],
                student_model,
                device,
                selected_router,
                iteration,
            )
            aggregate.extend(student_sequences)
            student_window_rows.extend(window_rows)
            student_plan_use.extend(plan_use)
            student_model, student_training = report126.train_consequence_policy(
                student_cfg,
                aggregate,
                device,
                iteration,
                f"student_counterfactual_iteration_{iteration}",
            )
            consequence_training_rows.append(student_training)
        source_summary = report126.source_rows(aggregate)
        selected_student_bias, student_selection = select_student_policy_bias(
            cfg,
            models["gru"],
            student_model,
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
            mpc_row, maybe_trace, mpc_tracker, _ = report131.run_mpc_sequence_episode(
                seed,
                cfg,
                models["gru"],
                device,
                selected_router,
                cfg.teacher_commit_actions,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(mpc_row)
            crisis_logs[f"{seed}:mpc_sequence_optimizer_gru:none"] = mpc_tracker.response_log
            if maybe_trace.frames:
                trace_out = maybe_trace
            student_row, maybe_trace, student_tracker = run_student_sequence_episode(
                seed,
                cfg,
                models["gru"],
                student_model,
                device,
                selected_router,
                selected_student_bias,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(student_row)
            crisis_logs[f"{seed}:student_sequence_consequence_gru:none"] = student_tracker.response_log
            if maybe_trace.frames:
                trace_out = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker = run_student_sequence_episode(
                    seed,
                    cfg,
                    models["gru"],
                    student_model,
                    device,
                    selected_router,
                    selected_student_bias,
                    ablation=ablation,
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:student_sequence_consequence_gru:{ablation}"] = tracker.response_log

    summary = coupled.summarize(eval_rows)
    ablations = ablations_from_summary(summary)
    verdict = transfer_verdict(
        summary,
        ablations,
        selected_router,
        selected_planner,
        selected_consequence_bias,
        selected_student_bias,
        cfg.teacher_commit_actions,
        schedules,
        consequence_training_rows,
        source_summary,
    )
    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "student_sequence_consequence_gru", "frames": []}
    payload = {
        "experiment": "ssrm_3d_coupled_crisis_student_sequence_consequence",
        "config": asdict(cfg),
        "claim": {
            "tested": "student-created active-crisis sequence windows with counterfactual MPC plan values can train a planner-free recurrent policy that preserves coupled repair",
            "remaining_structure": "MPC and simulator rollout scoring are used only during data generation; final evaluation has no planner, rollout scorer, or plan templates but still receives supplied active-crisis action candidates",
        },
        "plan_templates": [asdict(plan) for plan in report111.PLAN_TEMPLATES],
        "schedule": [asdict(row) for row in schedules],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "router_selection": [asdict(row) for row in router_selection],
        "planner_selection": [asdict(row) for row in planner_selection],
        "consequence_selection": [asdict(row) for row in consequence_selection],
        "student_selection": [asdict(row) for row in student_selection],
        "source_summary": [asdict(row) for row in source_summary],
        "student_window_summary": [asdict(row) for row in student_window_rows],
        "student_plan_use": [asdict(row) for row in student_plan_use],
        "consequence_training": [asdict(row) for row in consequence_training_rows],
        "action_candidates": list(ACTION_CANDIDATES),
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
    report124.rows_to_csv(Path(f"{PREFIX}_consequence_selection.csv"), consequence_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_student_selection.csv"), student_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_source_summary.csv"), source_summary)
    report124.rows_to_csv(Path(f"{PREFIX}_student_window_summary.csv"), student_window_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_student_plan_use.csv"), student_plan_use)
    report124.rows_to_csv(Path(f"{PREFIX}_consequence_training.csv"), consequence_training_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    report124.rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    report124.rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    report124.write_json(Path(f"{PREFIX}_results.json"), payload)
    report124.write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    report124.write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_STUDENT_SEQUENCE_CONSEQUENCE_RESULTS", payload)
    report124.write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_STUDENT_SEQUENCE_CONSEQUENCE_TRACE", trace_payload)
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
    parser.add_argument("--student-sequence-iterations", type=int, default=1)
    parser.add_argument("--student-sequence-epochs", type=int, default=8)
    parser.add_argument("--student-sequence-return-scale", type=float, default=1.35)
    parser.add_argument("--student-collection-bias", type=float, default=0.70)
    parser.add_argument("--counterfactual-collection-bias", type=float, default=0.80)
    parser.add_argument("--teacher-commit-actions", type=int, default=14)
    parser.add_argument("--policy-temperature", type=float, default=1.0)
    parser.add_argument("--policy-bias-candidates", default="0.0,0.40,0.80,1.20")
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
        student_sequence_iterations=args.student_sequence_iterations,
        student_sequence_epochs=args.student_sequence_epochs,
        student_sequence_return_scale=args.student_sequence_return_scale,
        student_collection_bias=args.student_collection_bias,
        counterfactual_collection_bias=args.counterfactual_collection_bias,
        teacher_commit_actions=args.teacher_commit_actions,
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
        "student_window_summary": payload["student_window_summary"],
        "consequence_training": payload["consequence_training"],
        "student_selection": payload["student_selection"],
        "verdict": payload["verdict"],
        "summary": payload["summary"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
