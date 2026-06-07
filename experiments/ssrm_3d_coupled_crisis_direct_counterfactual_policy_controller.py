#!/usr/bin/env python3
"""Direct counterfactual-policy recovery for SSRM-3D coupled crises.

Report 128 showed that cloned short-window counterfactuals are not enough when
they are used only as a runtime action-logit overlay: validation selected plan
bias 0.0. This benchmark moves the counterfactual target into the recurrent
policy itself. During training, active-crisis states are visited by consequence
and plan-following source policies. At selected windows, cloned simulator
rollouts choose the best supplied plan template; that plan is converted into
direct action labels for the recurrent crisis policy.

The benchmark remains bounded. The action set and plan templates are supplied,
the base controller is still imitation trained, and cloned rollouts provide
training labels rather than open-ended exploration. It is not mature deep RL,
open-ended civilization, subjective consciousness, or real-world competence.
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
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_direct_counterfactual_policy"
DIRECT_COUNTERFACTUAL_SEED = 20262411
ACTION_CANDIDATES = report126.ACTION_CANDIDATES
ACTION_TO_INDEX = report126.ACTION_TO_INDEX
SOURCE_POLICIES = ("counterfactual_teacher", "consequence_policy")
SOURCE_OFFSETS = {name: index * 1009 for index, name in enumerate(SOURCE_POLICIES)}


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
    direct_epochs: int = 8
    direct_hidden_size: int = 48
    direct_learning_rate: float = 0.003
    direct_return_scale: float = 1.15
    counterfactual_windows_per_source: int = 32
    plan_commit_actions: int = 42
    student_iterations: int = 0
    student_collection_bias: float = 0.70
    policy_temperature: float = 1.0
    policy_bias_candidates: Sequence[float] = (0.0, 0.40, 0.80)
    direct_bias_candidates: Sequence[float] = (0.0, 0.40, 0.80)
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class CounterfactualProbeRow:
    source_policy: str
    seed: int
    hour: float
    crisis: str
    selected_plan: str
    selected_value: float
    second_plan: str
    second_value: float
    value_margin: float
    env_fraction: float
    social_fraction: float
    labels_added: int


@dataclass(frozen=True)
class DirectPolicySelectionRow:
    direct_bias: float
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
class DirectCounterfactualVerdictRow:
    selected_router: str
    selected_planner: str
    selected_consequence_bias: float
    selected_direct_bias: float
    source_sequences: int
    student_sequences: int
    counterfactual_sequences: int
    counterfactual_examples: int
    counterfactual_windows: int
    mean_plan_value_margin: float
    consequence_train_accuracy: float
    consequence_weighted_accuracy: float
    direct_train_accuracy: float
    direct_weighted_accuracy: float
    direct_total_score: float
    consequence_total_score: float
    min_channel_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    direct_crisis_score: float
    consequence_crisis_score: float
    min_channel_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    direct_resolved_rate: float
    consequence_resolved_rate: float
    min_channel_resolved_rate: float
    fixed_joint_resolved_rate: float
    return_selected_resolved_rate: float
    direct_coupled_response: float
    consequence_coupled_response: float
    min_channel_coupled_response: float
    fixed_joint_coupled_response: float
    return_selected_coupled_response: float
    direct_gain_over_consequence: float
    direct_gain_over_return_selected: float
    direct_gap_to_teacher: float
    direct_gap_to_fixed_joint: float
    social_culture_crisis_loss: float
    environment_crisis_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    mean_crisis_count: float
    supports_direct_counterfactual_policy: bool
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


def choose_best_rollout_plan(
    world: World,
    agents: List[Agent],
    tracker: coupled.CrisisTracker,
    previous_actions: Dict[str, int],
    cfg: Config,
    seed: int,
) -> Tuple[report111.PlanTemplate, float, report111.PlanTemplate, float, float]:
    scored: List[Tuple[report111.PlanTemplate, float]] = []
    for index, plan in enumerate(report111.PLAN_TEMPLATES):
        value = report111.rollout_plan_value(
            plan,
            world,
            agents,
            tracker,
            previous_actions,
            cfg,
            seed + index * 37,
        )
        scored.append((plan, value))
    scored.sort(key=lambda item: item[1], reverse=True)
    best_plan, best_value = scored[0]
    second_plan, second_value = scored[1] if len(scored) > 1 else scored[0]
    return best_plan, best_value, second_plan, second_value, best_value - second_value


def target_action_from_plan(
    plan: report111.PlanTemplate,
    active: coupled.ActiveCrisis,
    features: Sequence[float],
    rng: random.Random,
) -> str:
    action = report111.plan_forced_action(plan, active, features, rng)
    return action if action in ACTION_TO_INDEX else "none"


def run_direct_policy_episode(
    seed: int,
    cfg: Config,
    base_model: base.ControllerNet,
    direct_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
    direct_bias: float,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, Trace, coupled.CrisisTracker]:
    row, trace_out, tracker = report124.run_distilled_episode(
        seed,
        cfg,
        base_model,
        direct_model,
        device,
        router,
        direct_bias,
        ablation=ablation,
        trace=trace,
    )
    row = replace(row, controller="direct_counterfactual_policy_gru")
    trace_out.condition = f"direct_counterfactual_policy_gru:{router.name}:bias_{direct_bias:g}:{ablation}"
    return row, trace_out, tracker


def collect_counterfactual_policy_sequences(
    cfg: Config,
    base_model: base.ControllerNet,
    consequence_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
    consequence_bias: float,
) -> Tuple[List[report126.ConsequenceSequence], List[CounterfactualProbeRow]]:
    sequences: List[report126.ConsequenceSequence] = []
    probes: List[CounterfactualProbeRow] = []
    for source_policy in SOURCE_POLICIES:
        windows_used = 0
        for seed in cfg.train_seeds:
            if windows_used >= cfg.counterfactual_windows_per_source:
                break
            collected, rows, windows_used = collect_counterfactual_policy_episode(
                seed,
                cfg,
                source_policy,
                base_model,
                consequence_model,
                device,
                router,
                consequence_bias,
                windows_used,
            )
            sequences.extend(collected)
            probes.extend(rows)
    return sequences, probes


def collect_counterfactual_policy_episode(
    seed: int,
    cfg: Config,
    source_policy: str,
    base_model: base.ControllerNet,
    consequence_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
    consequence_bias: float,
    windows_used: int,
) -> Tuple[List[report126.ConsequenceSequence], List[CounterfactualProbeRow], int]:
    rng = random.Random(seed * 257 + DIRECT_COUNTERFACTUAL_SEED + SOURCE_OFFSETS[source_policy])
    label_rng = random.Random(seed * 263 + DIRECT_COUNTERFACTUAL_SEED + SOURCE_OFFSETS[source_policy])
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
    pending_plan_values: List[float] = []
    damage_start = 0.0
    plan_state: Dict[str, object] = {}
    sequences: List[report126.ConsequenceSequence] = []
    probes: List[CounterfactualProbeRow] = []

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        action_counts: Dict[str, int] = {}
        coupled.maybe_start_crisis(world, tracker, rng, events)
        if tracker.active is not None and active_key != tracker.active.start:
            pending = []
            pending_plan_values = []
            damage_start = tracker.damage_integral
            active_key = tracker.active.start
            memory_state = None
            plan_state = {}
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
            nonlocal memory_state, plan_state, windows_used
            active = tracker.active
            action = report117.learned_policy_action(agent, features, base_model, recurrent_states, router, device, "none")
            if active is not None and current_world.time >= 12.0:
                remaining = int(plan_state.get("remaining", 0))
                if remaining <= 0 and windows_used < cfg.counterfactual_windows_per_source:
                    best_plan, best_value, second_plan, second_value, margin = choose_best_rollout_plan(
                        current_world,
                        agents,
                        tracker,
                        previous_actions,
                        cfg,
                        seed * 100000 + windows_used * 997 + len(pending),
                    )
                    env_fraction = min(1.0, active.env_progress / active.profile.env_need)
                    social_fraction = min(1.0, active.social_progress / active.profile.social_need)
                    plan_state = {
                        "plan": best_plan,
                        "value": best_value,
                        "remaining": max(1, cfg.plan_commit_actions),
                    }
                    probes.append(CounterfactualProbeRow(
                        source_policy=source_policy,
                        seed=seed,
                        hour=current_world.time,
                        crisis=active.profile.name,
                        selected_plan=best_plan.name,
                        selected_value=best_value,
                        second_plan=second_plan.name,
                        second_value=second_value,
                        value_margin=margin,
                        env_fraction=env_fraction,
                        social_fraction=social_fraction,
                        labels_added=0,
                    ))
                    windows_used += 1
                plan = plan_state.get("plan")
                if plan is not None:
                    target_action = target_action_from_plan(plan, active, features, label_rng)
                    values = report119.policy_features(
                        features,
                        active,
                        action_counts,
                        len(living(agents)),
                        current_world.time,
                        "none",
                    )
                    pending.append((values, ACTION_TO_INDEX[target_action]))
                    pending_plan_values.append(float(plan_state.get("value", 0.0)))
                    if probes:
                        last = probes[-1]
                        probes[-1] = replace(last, labels_added=last.labels_added + 1)
                    plan_state["remaining"] = int(plan_state.get("remaining", 1)) - 1
                    if source_policy == "counterfactual_teacher":
                        action = target_action
                    else:
                        action, memory_state = report121.choose_memory_candidate(
                            consequence_model,
                            features,
                            active,
                            action_counts,
                            len(living(agents)),
                            current_world.time,
                            memory_state,
                            device,
                            "none",
                            cfg.policy_temperature,
                            consequence_bias,
                        )
                if action == "none":
                    action = report117.learned_policy_action(agent, features, base_model, recurrent_states, router, device, "none")
            action_counts[action] = action_counts.get(action, 0) + 1
            return action

        base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
        active_before_completion = tracker.active
        report111.update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
        coupled.complete_crisis_if_due(world, agents, tracker, events)
        if active_before_completion is not None and tracker.active is None and pending:
            actual_return = report119.crisis_window_return(active_before_completion, tracker.damage_integral - damage_start)
            sequence_return = actual_return if source_policy == "counterfactual_teacher" else mean(pending_plan_values)
            sequences.append(report126.ConsequenceSequence(source_policy, sequence_return, tuple(pending)))
            pending = []
            pending_plan_values = []
            memory_state = None
            active_key = None
            plan_state = {}
    if tracker.active is not None and pending:
        active_before_completion = tracker.active
        coupled.complete_crisis_if_due(world, agents, tracker, events)
        actual_return = report119.crisis_window_return(active_before_completion, tracker.damage_integral - damage_start)
        sequence_return = actual_return if source_policy == "counterfactual_teacher" else mean(pending_plan_values)
        sequences.append(report126.ConsequenceSequence(source_policy, sequence_return, tuple(pending)))
    return sequences, probes, windows_used


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
    objective = total * 0.38 + crisis * 1.42 + resolved * 0.88 + coupled_response * 1.16 + balance * 0.18 - damage * 0.38
    return total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective


def select_direct_bias(
    cfg: Config,
    base_model: base.ControllerNet,
    direct_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[float, List[DirectPolicySelectionRow]]:
    rows: List[DirectPolicySelectionRow] = []
    best_bias = 0.0
    best_objective = -1e9
    for bias in cfg.direct_bias_candidates:
        eval_rows = [
            run_direct_policy_episode(seed, cfg, base_model, direct_model, device, router, bias)[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_objective = objective
            best_bias = bias
        rows.append(DirectPolicySelectionRow(
            direct_bias=bias,
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
    return best_bias, [replace(row, selected=(row.direct_bias == best_bias)) for row in rows]


def ablations_from_summary(summary: Sequence[coupled.SummaryRow]) -> List[coupled.AblationRow]:
    base_row = coupled.row_lookup(summary, "direct_counterfactual_policy_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = coupled.row_lookup(summary, "direct_counterfactual_policy_gru", ablation)
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
    direct_bias: float,
    schedules: Sequence[report114.ScheduleRow],
    consequence_training_rows: Sequence[report126.ConsequenceTrainingRow],
    direct_training: report126.ConsequenceTrainingRow,
    source_summary: Sequence[report126.ConsequenceSourceRow],
    direct_source_summary: Sequence[report126.ConsequenceSourceRow],
    probes: Sequence[CounterfactualProbeRow],
) -> DirectCounterfactualVerdictRow:
    direct = coupled.row_lookup(summary, "direct_counterfactual_policy_gru", "none")
    consequence = coupled.row_lookup(summary, "consequence_recovery_gru", "none")
    teacher = coupled.row_lookup(summary, "min_channel_planner_gru", "none")
    fixed = coupled.row_lookup(summary, "fixed_joint_gru", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    consequence_final = consequence_training_rows[-1]
    source_sequences = sum(row.sequences for row in source_summary if not row.source_policy.startswith("student_iteration"))
    student_sequences = sum(row.sequences for row in source_summary if row.source_policy.startswith("student_iteration"))
    counterfactual_sequences = sum(row.sequences for row in direct_source_summary)
    counterfactual_examples = sum(row.examples for row in direct_source_summary)
    supports_direct = (
        direct_training.weighted_train_accuracy >= 0.55
        and mean_crisis_count >= 4.0
        and direct.mean_total_score - consequence.mean_total_score >= 0.010
        and direct.mean_crisis_score - consequence.mean_crisis_score >= 0.020
        and direct.mean_crisis_score - returned.mean_crisis_score >= 0.040
        and direct.mean_resolved_rate - returned.mean_resolved_rate >= 0.080
        and direct.mean_coupled_response_rate - returned.mean_coupled_response_rate >= 0.080
        and direct.mean_alive_at_12h >= 12.0
        and direct.shock_gate_pass_rate == 1.0
        and direct.post_gate_shock_rate == 1.0
    )
    supports_teacher = (
        direct.mean_crisis_score >= 0.35
        and direct.mean_coupled_response_rate >= 0.40
        and teacher.mean_crisis_score - direct.mean_crisis_score <= 0.30
    )
    supports_dependency = (
        direct.mean_crisis_score > 0.0
        and social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    return DirectCounterfactualVerdictRow(
        selected_router=router.name,
        selected_planner=planner.name,
        selected_consequence_bias=consequence_bias,
        selected_direct_bias=direct_bias,
        source_sequences=source_sequences,
        student_sequences=student_sequences,
        counterfactual_sequences=counterfactual_sequences,
        counterfactual_examples=counterfactual_examples,
        counterfactual_windows=len(probes),
        mean_plan_value_margin=mean(row.value_margin for row in probes),
        consequence_train_accuracy=consequence_final.train_accuracy,
        consequence_weighted_accuracy=consequence_final.weighted_train_accuracy,
        direct_train_accuracy=direct_training.train_accuracy,
        direct_weighted_accuracy=direct_training.weighted_train_accuracy,
        direct_total_score=direct.mean_total_score,
        consequence_total_score=consequence.mean_total_score,
        min_channel_total_score=teacher.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        direct_crisis_score=direct.mean_crisis_score,
        consequence_crisis_score=consequence.mean_crisis_score,
        min_channel_crisis_score=teacher.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        direct_resolved_rate=direct.mean_resolved_rate,
        consequence_resolved_rate=consequence.mean_resolved_rate,
        min_channel_resolved_rate=teacher.mean_resolved_rate,
        fixed_joint_resolved_rate=fixed.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        direct_coupled_response=direct.mean_coupled_response_rate,
        consequence_coupled_response=consequence.mean_coupled_response_rate,
        min_channel_coupled_response=teacher.mean_coupled_response_rate,
        fixed_joint_coupled_response=fixed.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        direct_gain_over_consequence=direct.mean_total_score - consequence.mean_total_score,
        direct_gain_over_return_selected=direct.mean_total_score - returned.mean_total_score,
        direct_gap_to_teacher=teacher.mean_total_score - direct.mean_total_score,
        direct_gap_to_fixed_joint=fixed.mean_total_score - direct.mean_total_score,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=direct.shock_gate_pass_rate,
        post_gate_shock_rate=direct.post_gate_shock_rate,
        survival_at_12h=direct.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_direct_counterfactual_policy=supports_direct,
        supports_teacher_transfer=supports_teacher,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_direct and supports_teacher and supports_dependency else "partial_or_failed",
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
        selected_consequence_bias, consequence_selection = report126.select_policy_bias(
            cfg,
            models["gru"],
            consequence_model,
            device,
            selected_router,
        )
        direct_sequences, probes = collect_counterfactual_policy_sequences(
            cfg,
            models["gru"],
            consequence_model,
            device,
            selected_router,
            selected_consequence_bias,
        )
        direct_source_summary = report126.source_rows(direct_sequences)
        direct_model, direct_training = report126.train_consequence_policy(
            replace(
                cfg,
                consequence_epochs=cfg.direct_epochs,
                consequence_hidden_size=cfg.direct_hidden_size,
                consequence_learning_rate=cfg.direct_learning_rate,
                consequence_return_scale=cfg.direct_return_scale,
            ),
            direct_sequences,
            device,
            0,
            "direct_counterfactual_labels",
        )
        selected_direct_bias, direct_selection = select_direct_bias(
            cfg,
            models["gru"],
            direct_model,
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
            direct_row, maybe_trace, direct_tracker = run_direct_policy_episode(
                seed,
                cfg,
                models["gru"],
                direct_model,
                device,
                selected_router,
                selected_direct_bias,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(direct_row)
            crisis_logs[f"{seed}:direct_counterfactual_policy_gru:none"] = direct_tracker.response_log
            if seed == cfg.trace_seed:
                trace_out = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker = run_direct_policy_episode(
                    seed,
                    cfg,
                    models["gru"],
                    direct_model,
                    device,
                    selected_router,
                    selected_direct_bias,
                    ablation=ablation,
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:direct_counterfactual_policy_gru:{ablation}"] = tracker.response_log

        summary = coupled.summarize(eval_rows)
        ablations = ablations_from_summary(summary)
        verdict = transfer_verdict(
            summary,
            ablations,
            selected_router,
            selected_planner,
            selected_consequence_bias,
            selected_direct_bias,
            schedules,
            consequence_training_rows,
            direct_training,
            source_summary,
            direct_source_summary,
            probes,
        )

    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "direct_counterfactual_policy_gru", "frames": []}
    trace_payload["condition"] = "direct_counterfactual_policy_gru"
    payload = {
        "experiment": "ssrm_3d_coupled_crisis_direct_counterfactual_policy",
        "config": asdict(cfg),
        "claim": {
            "tested": "cloned-rollout multi-action counterfactual windows can train the recurrent crisis policy directly after the engineered planner is removed",
        "remaining_structure": "short-window plan templates and active-crisis action candidates are supplied; this is bounded direct counterfactual policy learning, not open-ended deep RL",
        },
        "action_candidates": list(ACTION_CANDIDATES),
        "source_policies": list(SOURCE_POLICIES),
        "plan_templates": [asdict(plan) for plan in report111.PLAN_TEMPLATES],
        "schedule": [asdict(row) for row in schedules],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "router_selection": [asdict(row) for row in router_selection],
        "planner_selection": [asdict(row) for row in planner_selection],
        "source_summary": [asdict(row) for row in source_summary],
        "consequence_training": [asdict(row) for row in consequence_training_rows],
        "consequence_selection": [asdict(row) for row in consequence_selection],
        "counterfactual_probes": [asdict(row) for row in probes],
        "direct_source_summary": [asdict(row) for row in direct_source_summary],
        "direct_training": asdict(direct_training),
        "direct_selection": [asdict(row) for row in direct_selection],
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
    report124.rows_to_csv(Path(f"{PREFIX}_counterfactual_probes.csv"), probes)
    report124.rows_to_csv(Path(f"{PREFIX}_direct_source_summary.csv"), direct_source_summary)
    report124.rows_to_csv(Path(f"{PREFIX}_direct_training.csv"), [direct_training])
    report124.rows_to_csv(Path(f"{PREFIX}_direct_selection.csv"), direct_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    report124.rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    report124.rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    report124.write_json(Path(f"{PREFIX}_results.json"), payload)
    report124.write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    report124.write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_DIRECT_COUNTERFACTUAL_POLICY_RESULTS", payload)
    report124.write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_DIRECT_COUNTERFACTUAL_POLICY_TRACE", trace_payload)
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
    parser.add_argument("--direct-epochs", type=int, default=8)
    parser.add_argument("--direct-hidden-size", type=int, default=48)
    parser.add_argument("--direct-learning-rate", type=float, default=0.003)
    parser.add_argument("--direct-return-scale", type=float, default=1.15)
    parser.add_argument("--counterfactual-windows-per-source", type=int, default=32)
    parser.add_argument("--plan-commit-actions", type=int, default=42)
    parser.add_argument("--student-iterations", type=int, default=0)
    parser.add_argument("--student-collection-bias", type=float, default=0.70)
    parser.add_argument("--policy-temperature", type=float, default=1.0)
    parser.add_argument("--policy-bias-candidates", default="0.0,0.40,0.80")
    parser.add_argument("--direct-bias-candidates", default="0.0,0.40,0.80")
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
        direct_epochs=args.direct_epochs,
        direct_hidden_size=args.direct_hidden_size,
        direct_learning_rate=args.direct_learning_rate,
        direct_return_scale=args.direct_return_scale,
        counterfactual_windows_per_source=args.counterfactual_windows_per_source,
        plan_commit_actions=args.plan_commit_actions,
        student_iterations=args.student_iterations,
        student_collection_bias=args.student_collection_bias,
        policy_temperature=args.policy_temperature,
        policy_bias_candidates=parse_floats(args.policy_bias_candidates),
        direct_bias_candidates=parse_floats(args.direct_bias_candidates),
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "direct_source_summary": payload["direct_source_summary"],
        "direct_training": payload["direct_training"],
        "direct_selection": payload["direct_selection"],
        "verdict": payload["verdict"],
        "summary": payload["summary"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
