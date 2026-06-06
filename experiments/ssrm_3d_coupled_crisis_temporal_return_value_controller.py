#!/usr/bin/env python3
"""Temporal return value control for SSRM-3D coupled crises.

Report 117 moved value learning into active crisis state/action scoring, but
the label was still a single-step consequence. This benchmark keeps the same
96h randomized coupled-crisis world and learned environmental/social action
heads, then trains the value model from Monte Carlo-style crisis-window
outcomes: actions taken during an active crisis are labeled by the later crisis
result.

This is still bounded. It is not actor-critic reinforcement learning,
open-ended civilization, or subjective consciousness. The candidate action set
is supplied, environmental/social action heads are supervised, and the value
model learns from completed crisis windows rather than arbitrary exploration.
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
from ssrm_maturation.agents import make_agents
from ssrm_maturation.benchmark import score_episode, snapshot
from ssrm_maturation.environment import clamp, living
from ssrm_maturation.models import CONDITIONS, Agent, Condition, Trace, World


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_temporal_return_value"
TEMPORAL_VALUE_SEED = 20261571
FIXED_JOINT = report117.FIXED_JOINT


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
    value_bias_candidates: Sequence[float] = (0.0, 0.75, 1.25, 1.75, 2.50, 3.50)
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class TemporalExampleSummaryRow:
    source_policy: str
    examples: int
    mean_target: float
    positive_rate: float


@dataclass(frozen=True)
class TemporalValueSelectionRow:
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
class TemporalVerdictRow:
    selected_router: str
    selected_value_bias: float
    temporal_value_examples: int
    temporal_value_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    temporal_value_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    temporal_value_resolved_rate: float
    fixed_joint_resolved_rate: float
    return_selected_resolved_rate: float
    temporal_value_coupled_response: float
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
    supports_temporal_return_value: bool
    supports_social_environment_dependency: bool
    verdict: str


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def bound(value: float, low: float = -1.25, high: float = 2.25) -> float:
    return max(low, min(high, value))


def parse_ints(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def parse_floats(value: str) -> Tuple[float, ...]:
    return tuple(float(part.strip()) for part in value.split(",") if part.strip())


def crisis_fraction(active: coupled.ActiveCrisis) -> Tuple[float, float, float]:
    env_fraction = min(1.0, active.env_progress / active.profile.env_need)
    social_fraction = min(1.0, active.social_progress / active.profile.social_need)
    return env_fraction, social_fraction, min(env_fraction, social_fraction)


def temporal_window_target(
    final_env: float,
    final_social: float,
    final_coupled: float,
    current_coupled: float,
    damage_delta: float,
) -> float:
    resolved = 1.0 if final_coupled >= 0.92 else 0.0
    progress_gain = max(0.0, final_coupled - current_coupled)
    unresolved = max(0.0, 0.92 - final_coupled)
    balance = 1.0 - min(1.0, abs(final_env - final_social))
    return bound(
        final_coupled * 1.15
        + resolved * 0.72
        + progress_gain * 1.05
        + balance * 0.10
        - unresolved * 0.82
        - damage_delta * 1.35
    )


def finalize_pending_examples(
    pending: List[Tuple[List[float], float, float]],
    active: coupled.ActiveCrisis,
    damage_now: float,
    examples: List[List[float]],
    targets: List[float],
    source_targets: List[float],
    max_examples: int,
) -> None:
    final_env, final_social, final_coupled = crisis_fraction(active)
    for features, current_coupled, damage_at_step in pending:
        if len(examples) >= max_examples:
            break
        target = temporal_window_target(
            final_env,
            final_social,
            final_coupled,
            current_coupled,
            max(0.0, damage_now - damage_at_step),
        )
        examples.append(features)
        targets.append(target)
        source_targets.append(target)
    pending.clear()


def collect_temporal_examples(
    cfg: Config,
    base_model: base.ControllerNet,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[List[List[float]], List[float], List[TemporalExampleSummaryRow]]:
    examples: List[List[float]] = []
    targets: List[float] = []
    source_counts: Dict[str, int] = {}
    source_targets: Dict[str, List[float]] = {}
    policies = (
        ("return_selected", 0.0, 0.0, 0.0),
        ("fixed_joint", FIXED_JOINT[0], FIXED_JOINT[1], FIXED_JOINT[2]),
        ("high_env_joint", 0.22, 0.12, 1.10),
        ("high_social_joint", 0.12, 0.22, 1.10),
        ("balanced_strong_joint", 0.18, 0.18, 1.25),
    )
    for policy_name, env_quota, social_quota, strength in policies:
        for seed in cfg.train_seeds:
            if len(examples) >= cfg.max_value_examples:
                break
            run_temporal_collection_episode(
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
        TemporalExampleSummaryRow(
            source_policy=source,
            examples=count,
            mean_target=mean(source_targets.get(source, [])),
            positive_rate=sum(1 for target in source_targets.get(source, []) if target > 0.0) / max(1, len(source_targets.get(source, []))),
        )
        for source, count in sorted(source_counts.items())
    ]
    return examples, targets, summary


def run_temporal_collection_episode(
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
    rng = random.Random(seed * 131 + sum(ord(ch) for ch in source_policy) + 6197)
    agents = make_agents(rng, cfg.population)
    world = coupled.prepare_world(rng, cfg)
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    env_states: Dict[str, torch.Tensor] = {}
    social_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
    pending: List[Tuple[List[float], float, float]] = []
    source_targets.setdefault(source_policy, [])
    with report114.patched_transfer_world(report114.randomized_schedule_builder(cfg.hours), report114.randomized_prepare_world):
        tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
        world = coupled.prepare_world(rng, cfg)
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
                if source_policy == "return_selected" or active is None:
                    action = report117.learned_policy_action(agent, features, model, recurrent_states, router, device, "none")
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
                        action = report117.learned_policy_action(agent, features, model, recurrent_states, router, device, "none")
                if active is not None and current_world.time >= 12.0:
                    _, _, current_coupled = crisis_fraction(active)
                    pending.append(
                        (
                            report117.value_features(
                                features,
                                active,
                                tracker,
                                action_counts,
                                len(living(agents)),
                                current_world.time,
                                action,
                            ),
                            current_coupled,
                            tracker.damage_integral,
                        )
                    )
                action_counts[action] = action_counts.get(action, 0) + 1
                return action

            base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
            active_before_completion = tracker.active
            report111.update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
            coupled.complete_crisis_if_due(world, agents, tracker, events)
            if active_before_completion is not None and tracker.active is None:
                before = len(examples)
                finalize_pending_examples(
                    pending,
                    active_before_completion,
                    tracker.damage_integral,
                    examples,
                    targets,
                    source_targets[source_policy],
                    cfg.max_value_examples,
                )
                source_counts[source_policy] = source_counts.get(source_policy, 0) + (len(examples) - before)
    if tracker.active is not None and pending:
        before = len(examples)
        finalize_pending_examples(
            pending,
            tracker.active,
            tracker.damage_integral,
            examples,
            targets,
            source_targets[source_policy],
            cfg.max_value_examples,
        )
        source_counts[source_policy] = source_counts.get(source_policy, 0) + (len(examples) - before)


def train_temporal_value_model(
    examples: Sequence[Sequence[float]],
    targets: Sequence[float],
    cfg: Config,
    device: torch.device,
) -> Tuple[report117.ActiveStateValueNet, report117.ActiveValueTrainingRow, float, float]:
    torch.manual_seed(TEMPORAL_VALUE_SEED)
    return report117.train_value_model(examples, targets, cfg, device)


def run_temporal_episode(
    seed: int,
    cfg: Config,
    controller: str,
    model: Optional[base.ControllerNet],
    env_model: Optional[base.ControllerNet],
    social_model: Optional[base.ControllerNet],
    value_model: Optional[report117.ActiveStateValueNet],
    target_mean: float,
    target_std: float,
    device: torch.device,
    router: report105.PressureRouter,
    value_bias: float = 0.0,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, Trace, coupled.CrisisTracker]:
    delegated = "active_state_value_gru" if controller == "temporal_return_value_gru" else controller
    row, trace_out, tracker = report117.run_active_value_episode(
        seed,
        cfg,
        delegated,
        model,
        env_model,
        social_model,
        value_model,
        target_mean,
        target_std,
        device,
        router,
        value_bias=value_bias,
        ablation=ablation,
        trace=trace,
    )
    if controller == "temporal_return_value_gru":
        row = replace(row, controller=controller)
        trace_out.condition = f"{controller}:{router.name}:value_{value_bias:g}:{ablation}"
    return row, trace_out, tracker


def selection_objective(rows: Sequence[coupled.EvalRow]) -> Tuple[float, float, float, float, float, float, float, float, float]:
    total = mean(row.total_score for row in rows)
    maturation = mean(row.maturation_score for row in rows)
    crisis = mean(row.crisis_score for row in rows)
    resolved = mean(row.resolved_rate for row in rows)
    env_response = mean(row.env_response_rate for row in rows)
    social_response = mean(row.social_response_rate for row in rows)
    coupled_response = mean(row.coupled_response_rate for row in rows)
    damage = mean(row.crisis_damage for row in rows)
    objective = total * 0.48 + crisis * 1.20 + resolved * 0.70 + coupled_response * 0.78 - damage * 0.30
    return total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective


def select_temporal_bias(
    cfg: Config,
    model: base.ControllerNet,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    value_model: report117.ActiveStateValueNet,
    target_mean: float,
    target_std: float,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[float, List[TemporalValueSelectionRow]]:
    rows: List[TemporalValueSelectionRow] = []
    best_bias = 0.0
    best_objective = -1e9
    for bias in cfg.value_bias_candidates:
        eval_rows = [
            run_temporal_episode(
                seed,
                cfg,
                "temporal_return_value_gru",
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
        rows.append(TemporalValueSelectionRow(
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


def ablations_from_summary(summary: Sequence[coupled.SummaryRow]) -> List[coupled.AblationRow]:
    base_row = coupled.row_lookup(summary, "temporal_return_value_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = coupled.row_lookup(summary, "temporal_return_value_gru", ablation)
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
    value_training: report117.ActiveValueTrainingRow,
) -> TemporalVerdictRow:
    temporal = coupled.row_lookup(summary, "temporal_return_value_gru", "none")
    fixed = coupled.row_lookup(summary, "fixed_joint_gru", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    supports_return = (
        selected_bias > 0.0
        and mean_crisis_count >= 4.0
        and temporal.mean_total_score - returned.mean_total_score >= 0.010
        and temporal.mean_crisis_score - returned.mean_crisis_score >= 0.040
        and temporal.mean_resolved_rate - returned.mean_resolved_rate >= 0.080
        and temporal.mean_coupled_response_rate - returned.mean_coupled_response_rate >= 0.080
        and temporal.mean_alive_at_12h >= 12.0
        and temporal.shock_gate_pass_rate == 1.0
        and temporal.post_gate_shock_rate == 1.0
    )
    supports_fixed = (
        temporal.mean_total_score - fixed.mean_total_score >= 0.005
        and temporal.mean_crisis_score - fixed.mean_crisis_score >= 0.020
        and temporal.mean_resolved_rate - fixed.mean_resolved_rate >= 0.020
        and temporal.mean_coupled_response_rate - fixed.mean_coupled_response_rate >= 0.020
    )
    supports_dependency = (
        temporal.mean_crisis_score > 0.0
        and social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    supports_temporal = supports_return and supports_fixed
    return TemporalVerdictRow(
        selected_router=router.name,
        selected_value_bias=selected_bias,
        temporal_value_examples=value_training.examples,
        temporal_value_total_score=temporal.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        temporal_value_crisis_score=temporal.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        temporal_value_resolved_rate=temporal.mean_resolved_rate,
        fixed_joint_resolved_rate=fixed.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        temporal_value_coupled_response=temporal.mean_coupled_response_rate,
        fixed_joint_coupled_response=fixed.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        gain_over_return_selected=temporal.mean_total_score - returned.mean_total_score,
        gain_over_fixed_joint=temporal.mean_total_score - fixed.mean_total_score,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=temporal.shock_gate_pass_rate,
        post_gate_shock_rate=temporal.post_gate_shock_rate,
        survival_at_12h=temporal.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_return_baseline_improvement=supports_return,
        supports_fixed_joint_improvement=supports_fixed,
        supports_temporal_return_value=supports_temporal,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_temporal and supports_dependency else "partial_or_failed",
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
            20261581,
        )
        social_model, social_training = report113.train_action_model(
            cfg,
            device,
            "social",
            social_sequences,
            social_labels,
            flags,
            20261582,
        )
        value_examples, value_targets, example_summary = collect_temporal_examples(
            cfg,
            models["gru"],
            env_model,
            social_model,
            device,
            selected_router,
        )
        value_model, value_training, target_mean, target_std = train_temporal_value_model(value_examples, value_targets, cfg, device)
        selected_bias, value_selection = select_temporal_bias(
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
                row, maybe_trace, tracker = run_temporal_episode(
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
            fixed_row, _, fixed_tracker = run_temporal_episode(
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
            temporal_row, maybe_trace, tracker = run_temporal_episode(
                seed,
                cfg,
                "temporal_return_value_gru",
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
            eval_rows.append(temporal_row)
            crisis_logs[f"{seed}:temporal_return_value_gru:none"] = tracker.response_log
            if maybe_trace.frames:
                trace_out = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker = run_temporal_episode(
                    seed,
                    cfg,
                    "temporal_return_value_gru",
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
                eval_rows.append(row)
                crisis_logs[f"{seed}:temporal_return_value_gru:{ablation}"] = tracker.response_log

    summary = coupled.summarize(eval_rows)
    ablations = ablations_from_summary(summary)
    verdict = transfer_verdict(summary, ablations, selected_router, selected_bias, schedules, value_training)
    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "temporal_return_value_gru", "frames": []}
    trace_payload["condition"] = "temporal_return_value_gru"
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
        "value_context_names": list(report117.VALUE_CONTEXT_NAMES),
        "action_candidates": list(report117.ACTION_CANDIDATES),
        "schedule": [asdict(row) for row in schedules],
        "router_selection": [asdict(row) for row in router_selection],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "value_training": asdict(value_training),
        "temporal_example_summary": [asdict(row) for row in example_summary],
        "value_selection": [asdict(row) for row in value_selection],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace_payload,
        "crisis_logs": crisis_logs,
        "notes": {
            "claim": "temporal crisis-window return labels can guide active repair choices during coupled crises",
            "not_claimed": "actor-critic reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
            "remaining_structure": "candidate repair actions are supplied, action heads are supervised, and temporal value labels come from completed crisis rollouts rather than online policy-gradient exploration",
        },
    }
    report117.rows_to_csv(Path(f"{PREFIX}_schedule.csv"), schedules)
    report117.rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    report117.rows_to_csv(Path(f"{PREFIX}_action_training.csv"), [env_training, social_training])
    report117.rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    report117.rows_to_csv(Path(f"{PREFIX}_temporal_example_summary.csv"), example_summary)
    report117.rows_to_csv(Path(f"{PREFIX}_value_training.csv"), [value_training])
    report117.rows_to_csv(Path(f"{PREFIX}_value_selection.csv"), value_selection)
    report117.rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    report117.rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    report117.rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    report117.rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    report117.write_json(Path(f"{PREFIX}_results.json"), payload)
    report117.write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    report117.write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_TEMPORAL_RETURN_VALUE_RESULTS", payload)
    report117.write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_TEMPORAL_RETURN_VALUE_TRACE", trace_payload)
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
    parser.add_argument("--value-bias-candidates", default="0.0,0.75,1.25,1.75,2.50,3.50")
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
        "temporal_example_summary": payload["temporal_example_summary"],
        "value_selection": payload["value_selection"],
        "verdict": payload["verdict"],
        "summary": payload["summary"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
