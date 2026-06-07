#!/usr/bin/env python3
"""Model-predictive sequence optimization for SSRM-3D coupled crises.

Report 130 showed that delayed policy-gradient fine-tuning and a learned
single-action consequence-value controller still fail robust coupled repair.
The learned value signal improves over a weak return-selected baseline, but it
does not preserve the environmental/social sequence needed after the engineered
planner is removed.

This benchmark tests the next narrower control shape as a bounded upper-bound:
choose short action-sequence commitments by cloning the current simulator state
and scoring candidate plan templates with actual downstream consequence
rollouts. The evaluated controller does not call the weakest-channel planner,
does not receive scenario IDs, and does not claim open-ended learned
civilization. It asks whether multi-step consequence planning is enough to
recover the missing coupled repair shape.
"""

from __future__ import annotations

import argparse
import json
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import torch

import ssrm_3d_coupled_crisis_active_state_value_controller as report117
import ssrm_3d_coupled_crisis_consequence_recovery_controller as report126
import ssrm_3d_coupled_crisis_joint_arbitration_controller as report113
import ssrm_3d_coupled_crisis_min_channel_planner_controller as report123
import ssrm_3d_coupled_crisis_planner_distillation_controller as report124
import ssrm_3d_coupled_crisis_randomized_transfer_controller as report114
import ssrm_3d_coupled_crisis_rollout_window_controller as report111
import ssrm_3d_coupled_social_environment_maturation_controller as coupled
import ssrm_3d_learned_multiday_maturation_controller as base
import ssrm_3d_return_selected_multiday_maturation_controller as report105
from ssrm_maturation.agents import make_agents
from ssrm_maturation.benchmark import TRACE_CHECKPOINTS, Trace, score_episode, snapshot
from ssrm_maturation.environment import clamp, living
from ssrm_maturation.models import CONDITIONS, Agent, Condition, World


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_mpc_sequence_optimizer"
MPC_SEQUENCE_SEED = 20262631


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
    policy_temperature: float = 1.0
    policy_bias_candidates: Sequence[float] = (0.0, 0.40, 0.80)
    commit_candidates: Sequence[int] = (14, 42)
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class MpcSequenceSelectionRow:
    commit_actions: int
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
class MpcPlanUseRow:
    seed: int
    ablation: str
    plan: str
    count: int
    mean_value: float
    max_value: float


@dataclass(frozen=True)
class MpcSequenceVerdictRow:
    selected_router: str
    selected_planner: str
    selected_consequence_bias: float
    selected_commit_actions: int
    source_sequences: int
    student_sequences: int
    aggregate_examples: int
    consequence_train_accuracy: float
    consequence_weighted_accuracy: float
    mpc_total_score: float
    consequence_total_score: float
    min_channel_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    mpc_crisis_score: float
    consequence_crisis_score: float
    min_channel_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    mpc_resolved_rate: float
    consequence_resolved_rate: float
    min_channel_resolved_rate: float
    fixed_joint_resolved_rate: float
    return_selected_resolved_rate: float
    mpc_coupled_response: float
    consequence_coupled_response: float
    min_channel_coupled_response: float
    fixed_joint_coupled_response: float
    return_selected_coupled_response: float
    mpc_gain_over_consequence: float
    mpc_gain_over_return_selected: float
    mpc_gap_to_teacher: float
    mpc_gap_to_fixed_joint: float
    social_culture_crisis_loss: float
    environment_crisis_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    mean_crisis_count: float
    supports_mpc_sequence_optimization: bool
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


def choose_mpc_plan(
    world: World,
    agents: List[Agent],
    tracker: coupled.CrisisTracker,
    previous_actions: Dict[str, int],
    cfg: Config,
    seed: int,
) -> Tuple[report111.PlanTemplate, float, Dict[str, float]]:
    if tracker.active is None:
        return report111.PLAN_TEMPLATES[0], 0.0, {}
    scores: Dict[str, float] = {}
    best_plan = report111.PLAN_TEMPLATES[0]
    best_value = -1e9
    for index, plan in enumerate(report111.PLAN_TEMPLATES):
        value = report111.rollout_plan_value(
            plan,
            world,
            agents,
            tracker,
            previous_actions,
            cfg,
            seed * 100003 + index * 917 + int(world.time * 100),
        )
        scores[plan.name] = value
        if value > best_value:
            best_value = value
            best_plan = plan
    return best_plan, best_value, scores


def update_plan_state(
    plan_state: Dict[str, object],
    seed: int,
    world: World,
    agents: List[Agent],
    tracker: coupled.CrisisTracker,
    previous_actions: Dict[str, int],
    cfg: Config,
    commit_actions: int,
    ablation: str,
    plan_log: List[dict[str, object]],
) -> report111.PlanTemplate:
    plan = plan_state.get("plan")
    remaining = int(plan_state.get("remaining", 0))
    if plan is not None and remaining > 0:
        return plan  # type: ignore[return-value]
    selected, value, scores = choose_mpc_plan(world, agents, tracker, previous_actions, cfg, seed)
    plan_state["plan"] = selected
    plan_state["value"] = value
    plan_state["scores"] = scores
    plan_state["remaining"] = max(1, commit_actions)
    plan_log.append({
        "hour": world.time,
        "crisis": tracker.active.profile.name if tracker.active else None,
        "plan": selected.name,
        "value": value,
        "ablation": ablation,
        "scores": scores,
    })
    return selected


def masked_plan_action(
    plan: report111.PlanTemplate,
    active: coupled.ActiveCrisis,
    features: Sequence[float],
    rng: random.Random,
    ablation: str,
) -> str:
    masked = report111.diagnostic_features(features, ablation)
    action = report111.plan_forced_action(plan, active, masked, rng)
    if ablation == "environment" and action in report111.ENV_RESPONSE_ACTIONS:
        return "rest"
    if ablation == "social_culture" and action in report111.SOCIAL_RESPONSE_ACTIONS:
        return "rest"
    return action


def run_mpc_sequence_episode(
    seed: int,
    cfg: Config,
    base_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
    commit_actions: int,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, Trace, coupled.CrisisTracker, List[dict[str, object]]]:
    rng = random.Random(
        seed * 149
        + sum(ord(ch) for ch in "mpc_sequence_optimizer_gru" + router.name + ablation)
        + commit_actions * 37
        + MPC_SEQUENCE_SEED
    )
    agents = make_agents(rng, cfg.population)
    world = coupled.prepare_world(rng, cfg)
    baseline = base.initial_baseline(world, cfg.population)
    condition = CONDITIONS[0]
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
    trace_out = Trace(seed=seed, condition=f"mpc_sequence_optimizer_gru:{router.name}:commit_{commit_actions}:{ablation}")
    checkpoints = list(TRACE_CHECKPOINTS)
    no_pre_gate_shock = True
    alive_at_12h = cfg.population
    at_12: Dict[str, float] = {}
    active_key: Optional[float] = None
    plan_state: Dict[str, object] = {}
    plan_log: List[dict[str, object]] = []

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
            active = tracker.active
            if active is not None and current_world.time >= 12.0:
                plan = update_plan_state(
                    plan_state,
                    seed,
                    current_world,
                    agents,
                    tracker,
                    previous_actions,
                    cfg,
                    commit_actions,
                    ablation,
                    plan_log,
                )
                action = masked_plan_action(plan, active, features, current_rng, ablation)
                plan_state["remaining"] = int(plan_state.get("remaining", 1)) - 1
                if action == "none":
                    action = report117.learned_policy_action(
                        agent,
                        features,
                        base_model,
                        recurrent_states,
                        router,
                        device,
                        ablation,
                    )
            else:
                action = report117.learned_policy_action(
                    agent,
                    features,
                    base_model,
                    recurrent_states,
                    router,
                    device,
                    ablation,
                )
            action_counts[action] = action_counts.get(action, 0) + 1
            return action

        base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
        report111.update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
        coupled.complete_crisis_if_due(world, agents, tracker, events)
        if tracker.active is None:
            active_key = None
            plan_state = {}
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
                "knowledge": clamp(
                    world.knowledge_transfer * 0.80
                    + (world.culture + world.symbols * 0.50 - baseline["culture_system"]) * 0.45
                ),
            }
        while trace and checkpoints and world.time >= checkpoints[0] - 1e-9:
            hour = checkpoints.pop(0)
            frame = snapshot(world, agents, f"{hour:g}h", events)
            frame["active_crisis"] = tracker.active.profile.name if tracker.active else None
            frame["crisis_resolved"] = tracker.resolved
            frame["crisis_unresolved"] = tracker.unresolved
            frame["crisis_damage"] = tracker.damage_integral
            frame["recent_mpc_plan"] = plan_log[-1]["plan"] if plan_log else None
            trace_out.frames.append(frame)

    if tracker.active is not None:
        coupled.complete_crisis_if_due(world, agents, tracker, events)
    episode = score_episode(world, agents, baseline, at_12, seed, condition, alive_at_12h, no_pre_gate_shock)
    crisis_score, resolved_rate, env_response, social_response, coupled_response = coupled.crisis_metrics(tracker)
    total_score = clamp(episode.maturation_score * 0.52 + crisis_score * 0.48)
    row = coupled.EvalRow(
        seed=seed,
        controller="mpc_sequence_optimizer_gru",
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
        frame["recent_mpc_plan"] = plan_log[-1]["plan"] if plan_log else None
        trace_out.frames.append(frame)
    return row, trace_out, tracker, plan_log


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
    objective = total * 0.30 + crisis * 1.55 + resolved * 0.90 + coupled_response * 1.35 + balance * 0.18 - damage * 0.42
    return total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective


def select_commit_actions(
    cfg: Config,
    base_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[int, List[MpcSequenceSelectionRow]]:
    rows: List[MpcSequenceSelectionRow] = []
    best_commit = cfg.commit_candidates[0]
    best_objective = -1e9
    for commit in cfg.commit_candidates:
        eval_rows = [
            run_mpc_sequence_episode(seed, cfg, base_model, device, router, commit)[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_objective = objective
            best_commit = commit
        rows.append(MpcSequenceSelectionRow(
            commit_actions=commit,
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
    return best_commit, [MpcSequenceSelectionRow(**{**asdict(row), "selected": row.commit_actions == best_commit}) for row in rows]


def ablations_from_summary(summary: Sequence[coupled.SummaryRow]) -> List[coupled.AblationRow]:
    base_row = coupled.row_lookup(summary, "mpc_sequence_optimizer_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = coupled.row_lookup(summary, "mpc_sequence_optimizer_gru", ablation)
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


def plan_use_rows(plan_logs: Dict[str, object]) -> List[MpcPlanUseRow]:
    grouped: Dict[Tuple[int, str, str], List[float]] = {}
    for key, value in plan_logs.items():
        seed_s, _, ablation = key.split(":")
        seed = int(seed_s)
        for item in value:  # type: ignore[assignment]
            grouped.setdefault((seed, ablation, str(item["plan"])), []).append(float(item["value"]))
    rows: List[MpcPlanUseRow] = []
    for (seed, ablation, plan), values in sorted(grouped.items()):
        rows.append(MpcPlanUseRow(
            seed=seed,
            ablation=ablation,
            plan=plan,
            count=len(values),
            mean_value=mean(values),
            max_value=max(values) if values else 0.0,
        ))
    return rows


def transfer_verdict(
    summary: Sequence[coupled.SummaryRow],
    ablations: Sequence[coupled.AblationRow],
    router: report105.PressureRouter,
    planner: report123.PlannerCandidate,
    consequence_bias: float,
    commit_actions: int,
    schedules: Sequence[report114.ScheduleRow],
    consequence_training_rows: Sequence[report126.ConsequenceTrainingRow],
    source_summary: Sequence[report126.ConsequenceSourceRow],
) -> MpcSequenceVerdictRow:
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
    final_training = consequence_training_rows[-1]
    source_sequences = sum(row.sequences for row in source_summary if not row.source_policy.startswith("student_iteration"))
    student_sequences = sum(row.sequences for row in source_summary if row.source_policy.startswith("student_iteration"))
    supports_mpc = (
        mean_crisis_count >= 4.0
        and mpc.mean_total_score - consequence.mean_total_score >= 0.010
        and mpc.mean_crisis_score - consequence.mean_crisis_score >= 0.050
        and mpc.mean_resolved_rate - consequence.mean_resolved_rate >= 0.080
        and mpc.mean_coupled_response_rate - consequence.mean_coupled_response_rate >= 0.080
        and mpc.mean_alive_at_12h >= 12.0
        and mpc.shock_gate_pass_rate == 1.0
        and mpc.post_gate_shock_rate == 1.0
    )
    supports_teacher = (
        mpc.mean_crisis_score >= 0.35
        and mpc.mean_coupled_response_rate >= 0.40
        and teacher.mean_crisis_score - mpc.mean_crisis_score <= 0.30
    )
    supports_dependency = (
        mpc.mean_crisis_score > 0.0
        and social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    return MpcSequenceVerdictRow(
        selected_router=router.name,
        selected_planner=planner.name,
        selected_consequence_bias=consequence_bias,
        selected_commit_actions=commit_actions,
        source_sequences=source_sequences,
        student_sequences=student_sequences,
        aggregate_examples=final_training.aggregate_examples,
        consequence_train_accuracy=final_training.train_accuracy,
        consequence_weighted_accuracy=final_training.weighted_train_accuracy,
        mpc_total_score=mpc.mean_total_score,
        consequence_total_score=consequence.mean_total_score,
        min_channel_total_score=teacher.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        mpc_crisis_score=mpc.mean_crisis_score,
        consequence_crisis_score=consequence.mean_crisis_score,
        min_channel_crisis_score=teacher.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        mpc_resolved_rate=mpc.mean_resolved_rate,
        consequence_resolved_rate=consequence.mean_resolved_rate,
        min_channel_resolved_rate=teacher.mean_resolved_rate,
        fixed_joint_resolved_rate=fixed.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        mpc_coupled_response=mpc.mean_coupled_response_rate,
        consequence_coupled_response=consequence.mean_coupled_response_rate,
        min_channel_coupled_response=teacher.mean_coupled_response_rate,
        fixed_joint_coupled_response=fixed.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        mpc_gain_over_consequence=mpc.mean_total_score - consequence.mean_total_score,
        mpc_gain_over_return_selected=mpc.mean_total_score - returned.mean_total_score,
        mpc_gap_to_teacher=teacher.mean_total_score - mpc.mean_total_score,
        mpc_gap_to_fixed_joint=fixed.mean_total_score - mpc.mean_total_score,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=mpc.shock_gate_pass_rate,
        post_gate_shock_rate=mpc.post_gate_shock_rate,
        survival_at_12h=mpc.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_mpc_sequence_optimization=supports_mpc,
        supports_teacher_transfer=supports_teacher,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_mpc and supports_teacher and supports_dependency else "partial_or_failed",
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
            20262641,
        )
        social_model, social_training = report113.train_action_model(
            cfg,
            device,
            "social",
            social_sequences,
            social_labels,
            flags,
            20262642,
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
        selected_commit, commit_selection = select_commit_actions(cfg, models["gru"], device, selected_router)

        eval_rows: List[coupled.EvalRow] = []
        crisis_logs: Dict[str, object] = {}
        plan_logs: Dict[str, object] = {}
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
            mpc_row, maybe_trace, mpc_tracker, mpc_plan_log = run_mpc_sequence_episode(
                seed,
                cfg,
                models["gru"],
                device,
                selected_router,
                selected_commit,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(mpc_row)
            crisis_logs[f"{seed}:mpc_sequence_optimizer_gru:none"] = mpc_tracker.response_log
            plan_logs[f"{seed}:mpc_sequence_optimizer_gru:none"] = mpc_plan_log
            if maybe_trace.frames:
                trace_out = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker, log = run_mpc_sequence_episode(
                    seed,
                    cfg,
                    models["gru"],
                    device,
                    selected_router,
                    selected_commit,
                    ablation=ablation,
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:mpc_sequence_optimizer_gru:{ablation}"] = tracker.response_log
                plan_logs[f"{seed}:mpc_sequence_optimizer_gru:{ablation}"] = log

        summary = coupled.summarize(eval_rows)
        ablations = ablations_from_summary(summary)
        plan_use = plan_use_rows(plan_logs)
        verdict = transfer_verdict(
            summary,
            ablations,
            selected_router,
            selected_planner,
            selected_consequence_bias,
            selected_commit,
            schedules,
            consequence_training_rows,
            source_summary,
        )

    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "mpc_sequence_optimizer_gru", "frames": []}
    trace_payload["condition"] = "mpc_sequence_optimizer_gru"
    payload = {
        "experiment": "ssrm_3d_coupled_crisis_mpc_sequence_optimizer",
        "config": asdict(cfg),
        "claim": {
            "tested": "online model-predictive sequence commitment can recover coupled repair after single-action consequence learning fails",
            "remaining_structure": "plan templates and cloned simulator rollout scoring are supplied; this is a bounded planning upper bound, not open-ended learned civilization",
        },
        "plan_templates": [asdict(plan) for plan in report111.PLAN_TEMPLATES],
        "schedule": [asdict(row) for row in schedules],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "router_selection": [asdict(row) for row in router_selection],
        "planner_selection": [asdict(row) for row in planner_selection],
        "source_summary": [asdict(row) for row in source_summary],
        "consequence_training": [asdict(row) for row in consequence_training_rows],
        "consequence_selection": [asdict(row) for row in consequence_selection],
        "commit_selection": [asdict(row) for row in commit_selection],
        "plan_use": [asdict(row) for row in plan_use],
        "eval": [asdict(row) for row in eval_rows],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace_payload,
        "crisis_logs": crisis_logs,
        "plan_logs": plan_logs,
    }
    report124.rows_to_csv(Path(f"{PREFIX}_schedule.csv"), schedules)
    report124.rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_action_training.csv"), [env_training, social_training])
    report124.rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_planner_selection.csv"), planner_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_source_summary.csv"), source_summary)
    report124.rows_to_csv(Path(f"{PREFIX}_consequence_training.csv"), consequence_training_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_consequence_selection.csv"), consequence_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_commit_selection.csv"), commit_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_plan_use.csv"), plan_use)
    report124.rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    report124.rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    report124.rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    report124.write_json(Path(f"{PREFIX}_results.json"), payload)
    report124.write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    report124.write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_MPC_SEQUENCE_OPTIMIZER_RESULTS", payload)
    report124.write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_MPC_SEQUENCE_OPTIMIZER_TRACE", trace_payload)
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
    parser.add_argument("--policy-temperature", type=float, default=1.0)
    parser.add_argument("--policy-bias-candidates", default="0.0,0.40,0.80")
    parser.add_argument("--commit-candidates", default="14,42")
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
        commit_candidates=parse_ints(args.commit_candidates),
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "commit_selection": payload["commit_selection"],
        "verdict": payload["verdict"],
        "summary": payload["summary"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
