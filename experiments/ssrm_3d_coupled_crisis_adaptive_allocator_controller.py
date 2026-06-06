#!/usr/bin/env python3
"""Return-trained adaptive allocation for SSRM-3D randomized coupled crises.

Report 114 showed that fixed validation-selected quotas can keep environmental
and social repair active across randomized post-12h crisis schedules. This
benchmark removes the fixed quota grid and trains a compact continuous allocator
by closed-loop return search over the same 96h randomized world.

The allocator still sits around learned environmental/social action heads, so
this is not actor-critic RL or open-ended civilization. It is a bounded step
toward direct consequence-trained allocation.
"""

from __future__ import annotations

import argparse
import contextlib
import csv
import json
import math
import random
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Callable, Dict, Iterable, Iterator, List, Sequence, Tuple

import torch

import ssrm_3d_coupled_crisis_joint_arbitration_controller as report113
import ssrm_3d_coupled_crisis_randomized_transfer_controller as report114
import ssrm_3d_coupled_crisis_rollout_window_controller as report111
import ssrm_3d_coupled_social_environment_maturation_controller as coupled
import ssrm_3d_learned_multiday_maturation_controller as base
import ssrm_3d_return_selected_multiday_maturation_controller as report105
from ssrm_maturation.agents import Agent
from ssrm_maturation.environment import clamp


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_adaptive_allocator"

ALLOC_INPUTS = (
    "bias",
    "post_gate",
    "major_shocks",
    "env_pressure",
    "social_pressure",
    "infrastructure_need",
    "tool_need",
    "teaching_need",
    "body_need",
    "weather_pressure",
    "resource_need",
    "env_fraction",
    "social_fraction",
    "response_imbalance",
)
ALLOC_INPUT_SIZE = len(ALLOC_INPUTS)
PARAM_COUNT = ALLOC_INPUT_SIZE * 3
FIXED_JOINT = (0.14, 0.14, 0.90)
ORIGINAL_COORDINATOR = report113.coordinator_action
CURRENT_ALLOCATOR: Tuple[float, ...] = tuple([0.0] * PARAM_COUNT)


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
    allocator_iterations: int = 2
    allocator_population: int = 7
    allocator_elites: int = 3
    allocator_sigma: float = 0.42
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class AllocatorSelectionRow:
    iteration: int
    candidate: int
    tune_total_score: float
    tune_maturation_score: float
    tune_crisis_score: float
    tune_resolved_rate: float
    tune_env_response: float
    tune_social_response: float
    tune_coupled_response: float
    tune_damage: float
    objective: float
    selected: bool
    env_bias: float
    social_bias: float
    strength_bias: float
    env_pressure_weight: float
    social_pressure_weight: float
    infrastructure_weight: float
    response_imbalance_weight: float


@dataclass(frozen=True)
class AllocatorProbeRow:
    seed: int
    hour: float
    env_target: float
    social_target: float
    strength: float
    env_pressure: float
    social_pressure: float
    infrastructure_need: float
    resource_need: float


@dataclass(frozen=True)
class VerdictRow:
    selected_router: str
    allocator_iterations: int
    allocator_population: int
    adaptive_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    adaptive_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    adaptive_resolved_rate: float
    fixed_joint_resolved_rate: float
    return_selected_resolved_rate: float
    adaptive_coupled_response: float
    fixed_joint_coupled_response: float
    return_selected_coupled_response: float
    adaptive_gain_over_return_selected: float
    adaptive_gap_to_fixed_joint: float
    social_culture_crisis_loss: float
    environment_crisis_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    mean_crisis_count: float
    supports_adaptive_allocation: bool
    supports_non_fixed_transfer: bool
    supports_social_environment_dependency: bool
    verdict: str


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def parse_ints(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def sigmoid(value: float) -> float:
    value = max(-20.0, min(20.0, value))
    return 1.0 / (1.0 + math.exp(-value))


def initial_allocator() -> Tuple[float, ...]:
    params = [0.0] * PARAM_COUNT
    env_offset = 0
    social_offset = ALLOC_INPUT_SIZE
    strength_offset = ALLOC_INPUT_SIZE * 2
    params[env_offset + 0] = -0.25
    params[social_offset + 0] = -0.25
    params[strength_offset + 0] = 0.22
    params[env_offset + ALLOC_INPUTS.index("env_pressure")] = 0.32
    params[env_offset + ALLOC_INPUTS.index("infrastructure_need")] = 0.18
    params[env_offset + ALLOC_INPUTS.index("resource_need")] = 0.10
    params[social_offset + ALLOC_INPUTS.index("social_pressure")] = 0.34
    params[social_offset + ALLOC_INPUTS.index("teaching_need")] = 0.16
    params[strength_offset + ALLOC_INPUTS.index("response_imbalance")] = 0.20
    params[strength_offset + ALLOC_INPUTS.index("major_shocks")] = 0.12
    return tuple(params)


def allocation_inputs(features: Sequence[float], action_counts: Dict[str, int], alive_count: int) -> List[float]:
    feature = report111.FEATURE
    denom = max(1, alive_count)
    env_fraction = sum(action_counts.get(action, 0) for action in report111.ENV_RESPONSE_ACTIONS) / denom
    social_fraction = sum(action_counts.get(action, 0) for action in report111.SOCIAL_RESPONSE_ACTIONS) / denom
    env_pressure = clamp(
        features[feature["contamination"]] * 0.22
        + features[feature["disease"]] * 0.24
        + features[feature["route_hazard"]] * 0.18
        + features[feature["resource_migration"]] * 0.12
        + features[feature["predators"]] * 0.12
        + abs(features[feature["temperature"]] - 0.55) * 0.12
    )
    social_pressure = clamp(
        features[feature["conflict"]] * 0.45
        + max(0.0, 0.58 - features[feature["social_trust"]]) * 0.32
        + max(0.0, 0.60 - features[feature["culture"]]) * 0.14
        + max(0.0, 0.54 - features[feature["symbols"]]) * 0.10
    )
    infrastructure_need = clamp(
        max(0.0, 0.62 - features[feature["shelter"]]) * 0.28
        + max(0.0, 0.62 - features[feature["architecture"]]) * 0.28
        + max(0.0, 0.55 - features[feature["waterworks"]]) * 0.18
        + max(0.0, 0.50 - features[feature["paths"]]) * 0.12
        + max(0.0, 0.50 - features[feature["sanitation"]]) * 0.14
    )
    tool_need = clamp(
        max(0.0, 0.72 - features[feature["tools"]]) * 0.50
        + max(0.0, 0.58 - features[feature["workshop"]]) * 0.30
        + max(0.0, 0.70 - features[feature["tool_tier"]]) * 0.20
    )
    teaching_need = clamp(
        max(0.0, 0.72 - features[feature["knowledge_transfer"]]) * 0.38
        + max(0.0, 0.66 - features[feature["culture"]]) * 0.24
        + max(0.0, 0.58 - features[feature["risk_memory"]]) * 0.20
        + max(0.0, 0.52 - features[feature["symbols"]]) * 0.18
    )
    body_need = clamp(
        max(0.0, 0.45 - features[feature["health"]]) * 0.36
        + max(0.0, 0.36 - features[feature["energy"]]) * 0.28
        + features[feature["illness"]] * 0.18
        + features[feature["injury"]] * 0.18
    )
    weather_pressure = clamp(
        features[feature["rainfall"]] * 0.30
        + features[feature["wind"]] * 0.22
        + max(0.0, 0.58 - features[feature["visibility"]]) * 0.20
        + abs(features[feature["temperature"]] - 0.55) * 0.20
    )
    resource_need = clamp(
        max(0.0, 0.54 - features[feature["water"]]) * 0.36
        + max(0.0, 0.54 - features[feature["food"]]) * 0.30
        + features[feature["resource_migration"]] * 0.18
        + features[feature["resource_depletion"]] * 0.16
    )
    return [
        1.0,
        features[feature["post_gate"]],
        features[feature["major_shocks"]],
        env_pressure,
        social_pressure,
        infrastructure_need,
        tool_need,
        teaching_need,
        body_need,
        weather_pressure,
        resource_need,
        env_fraction,
        social_fraction,
        abs(env_fraction - social_fraction),
    ]


def allocation_targets(
    params: Sequence[float],
    features: Sequence[float],
    action_counts: Dict[str, int],
    alive_count: int,
    ablation: str = "none",
) -> Tuple[float, float, float, List[float]]:
    inputs = allocation_inputs(features, action_counts, alive_count)
    env_score = sum(params[index] * inputs[index] for index in range(ALLOC_INPUT_SIZE))
    social_score = sum(params[ALLOC_INPUT_SIZE + index] * inputs[index] for index in range(ALLOC_INPUT_SIZE))
    strength_score = sum(params[ALLOC_INPUT_SIZE * 2 + index] * inputs[index] for index in range(ALLOC_INPUT_SIZE))
    env_target = 0.0 if ablation == "environment" else sigmoid(env_score) * 0.32
    social_target = 0.0 if ablation == "social_culture" else sigmoid(social_score) * 0.32
    strength = 0.40 + sigmoid(strength_score) * 0.90
    return env_target, social_target, strength, inputs


def adaptive_coordinator_action(
    agent: Agent,
    features: Sequence[float],
    action_counts: Dict[str, int],
    alive_count: int,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    env_states: Dict[str, torch.Tensor],
    social_states: Dict[str, torch.Tensor],
    env_quota: float,
    social_quota: float,
    strength: float,
    device: torch.device,
    ablation: str,
) -> str | None:
    del env_quota, social_quota, strength
    env_target, social_target, learned_strength, _ = allocation_targets(
        CURRENT_ALLOCATOR,
        features,
        action_counts,
        alive_count,
        ablation,
    )
    return ORIGINAL_COORDINATOR(
        agent,
        features,
        action_counts,
        alive_count,
        env_model,
        social_model,
        env_states,
        social_states,
        env_target,
        social_target,
        learned_strength,
        device,
        ablation,
    )


@contextlib.contextmanager
def patched_adaptive_allocator(params: Sequence[float]) -> Iterator[None]:
    global CURRENT_ALLOCATOR
    previous_params = CURRENT_ALLOCATOR
    previous_coordinator = report113.coordinator_action
    CURRENT_ALLOCATOR = tuple(params)
    report113.coordinator_action = adaptive_coordinator_action
    try:
        yield
    finally:
        CURRENT_ALLOCATOR = previous_params
        report113.coordinator_action = previous_coordinator


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


def selection_objective(rows: Sequence[coupled.EvalRow]) -> Tuple[float, float, float, float, float, float, float, float, float]:
    total = mean(row.total_score for row in rows)
    maturation = mean(row.maturation_score for row in rows)
    crisis = mean(row.crisis_score for row in rows)
    resolved = mean(row.resolved_rate for row in rows)
    env_response = mean(row.env_response_rate for row in rows)
    social_response = mean(row.social_response_rate for row in rows)
    coupled_response = mean(row.coupled_response_rate for row in rows)
    damage = mean(row.crisis_damage for row in rows)
    objective = total * 0.52 + crisis * 1.10 + resolved * 0.66 + coupled_response * 0.78 - damage * 0.32
    return total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective


def run_adaptive_episode(
    seed: int,
    cfg: Config,
    model: base.ControllerNet,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
    params: Sequence[float],
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, object, coupled.CrisisTracker]:
    with patched_adaptive_allocator(params):
        row, trace_out, tracker = report113.run_episode(
            seed,
            cfg,
            "joint_arbitration_gru",
            model,
            env_model,
            social_model,
            device,
            router,
            0.0,
            0.0,
            1.0,
            ablation=ablation,
            trace=trace,
        )
    return replace(row, controller="adaptive_allocator_gru"), trace_out, tracker


def run_fixed_joint_episode(
    seed: int,
    cfg: Config,
    model: base.ControllerNet,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> coupled.EvalRow:
    row, _, _ = report113.run_episode(
        seed,
        cfg,
        "joint_arbitration_gru",
        model,
        env_model,
        social_model,
        device,
        router,
        FIXED_JOINT[0],
        FIXED_JOINT[1],
        FIXED_JOINT[2],
    )
    return replace(row, controller="fixed_joint_gru")


def row_lookup(summary: Sequence[coupled.SummaryRow], controller: str, ablation: str) -> coupled.SummaryRow:
    return coupled.row_lookup(summary, controller, ablation)


def ablations_from_summary(summary: Sequence[coupled.SummaryRow]) -> List[coupled.AblationRow]:
    base_row = row_lookup(summary, "adaptive_allocator_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = row_lookup(summary, "adaptive_allocator_gru", ablation)
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


def candidate_row(
    iteration: int,
    candidate: int,
    rows: Sequence[coupled.EvalRow],
    params: Sequence[float],
    selected: bool = False,
) -> AllocatorSelectionRow:
    total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective = selection_objective(rows)
    return AllocatorSelectionRow(
        iteration=iteration,
        candidate=candidate,
        tune_total_score=total,
        tune_maturation_score=maturation,
        tune_crisis_score=crisis,
        tune_resolved_rate=resolved,
        tune_env_response=env_response,
        tune_social_response=social_response,
        tune_coupled_response=coupled_response,
        tune_damage=damage,
        objective=objective,
        selected=selected,
        env_bias=params[0],
        social_bias=params[ALLOC_INPUT_SIZE],
        strength_bias=params[ALLOC_INPUT_SIZE * 2],
        env_pressure_weight=params[ALLOC_INPUTS.index("env_pressure")],
        social_pressure_weight=params[ALLOC_INPUT_SIZE + ALLOC_INPUTS.index("social_pressure")],
        infrastructure_weight=params[ALLOC_INPUTS.index("infrastructure_need")],
        response_imbalance_weight=params[ALLOC_INPUT_SIZE * 2 + ALLOC_INPUTS.index("response_imbalance")],
    )


def optimize_allocator(
    cfg: Config,
    model: base.ControllerNet,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[Tuple[float, ...], List[AllocatorSelectionRow]]:
    rng = random.Random(20261231)
    mean_params = list(initial_allocator())
    sigma = cfg.allocator_sigma
    best_params = tuple(mean_params)
    best_objective = -1e9
    history: List[Tuple[float, Tuple[float, ...], AllocatorSelectionRow]] = []
    rows: List[AllocatorSelectionRow] = []
    population = max(2, cfg.allocator_population)
    elites = max(1, min(cfg.allocator_elites, population))
    for iteration in range(cfg.allocator_iterations):
        candidates: List[Tuple[float, ...]] = [tuple(mean_params)]
        while len(candidates) < population:
            candidates.append(tuple(
                mean_params[index] + rng.gauss(0.0, sigma)
                for index in range(PARAM_COUNT)
            ))
        scored: List[Tuple[float, Tuple[float, ...], AllocatorSelectionRow]] = []
        for candidate_index, params in enumerate(candidates):
            eval_rows = [
                run_adaptive_episode(seed, cfg, model, env_model, social_model, device, router, params)[0]
                for seed in cfg.tune_seeds
            ]
            row = candidate_row(iteration, candidate_index, eval_rows, params)
            scored.append((row.objective, params, row))
            rows.append(row)
            if row.objective > best_objective:
                best_objective = row.objective
                best_params = params
        scored.sort(key=lambda item: item[0], reverse=True)
        elite_params = [params for _, params, _ in scored[:elites]]
        mean_params = [
            mean(params[index] for params in elite_params)
            for index in range(PARAM_COUNT)
        ]
        sigma *= 0.66
        history.extend(scored)
    return best_params, [
        replace(row, selected=(tuple(row_params) == tuple(best_params)))
        for _, row_params, row in history
    ]


def allocator_probes(params: Sequence[float], schedules: Sequence[report114.ScheduleRow]) -> List[AllocatorProbeRow]:
    probes: List[AllocatorProbeRow] = []
    for row in schedules:
        if row.phase != "eval":
            continue
        for hour in (row.first_crisis_hour, min(95.0, row.first_crisis_hour + 4.0), row.last_crisis_hour):
            feature_values = [0.55] * base.FEATURE_COUNT
            feature = report111.FEATURE
            feature_values[feature["post_gate"]] = 1.0
            feature_values[feature["major_shocks"]] = clamp(hour / 96.0)
            feature_values[feature["contamination"]] = 0.40 if "contaminated" in row.profile_sequence else 0.18
            feature_values[feature["disease"]] = 0.36 if "quarantine" in row.profile_sequence else 0.16
            feature_values[feature["route_hazard"]] = 0.40 if "route" in row.profile_sequence else 0.18
            feature_values[feature["rainfall"]] = 0.46 if "storm" in row.profile_sequence else 0.18
            feature_values[feature["wind"]] = 0.44 if "storm" in row.profile_sequence else 0.18
            feature_values[feature["conflict"]] = 0.38
            feature_values[feature["social_trust"]] = 0.50
            env, social, strength, inputs = allocation_targets(params, feature_values, {}, 14)
            probes.append(AllocatorProbeRow(
                seed=row.seed,
                hour=hour,
                env_target=env,
                social_target=social,
                strength=strength,
                env_pressure=inputs[ALLOC_INPUTS.index("env_pressure")],
                social_pressure=inputs[ALLOC_INPUTS.index("social_pressure")],
                infrastructure_need=inputs[ALLOC_INPUTS.index("infrastructure_need")],
                resource_need=inputs[ALLOC_INPUTS.index("resource_need")],
            ))
    return probes


def transfer_verdict(
    summary: Sequence[coupled.SummaryRow],
    ablations: Sequence[coupled.AblationRow],
    router: report105.PressureRouter,
    schedules: Sequence[report114.ScheduleRow],
    cfg: Config,
) -> VerdictRow:
    adaptive = row_lookup(summary, "adaptive_allocator_gru", "none")
    fixed = row_lookup(summary, "fixed_joint_gru", "none")
    returned = row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    supports_adaptive = (
        mean_crisis_count >= 4.0
        and adaptive.mean_total_score - returned.mean_total_score >= 0.010
        and adaptive.mean_crisis_score - returned.mean_crisis_score >= 0.040
        and adaptive.mean_resolved_rate - returned.mean_resolved_rate >= 0.080
        and adaptive.mean_coupled_response_rate - returned.mean_coupled_response_rate >= 0.080
        and adaptive.mean_alive_at_12h >= 12.0
        and adaptive.shock_gate_pass_rate == 1.0
        and adaptive.post_gate_shock_rate == 1.0
    )
    supports_non_fixed = (
        adaptive.mean_crisis_score >= 0.45
        and adaptive.mean_coupled_response_rate >= 0.55
        and fixed.mean_crisis_score - adaptive.mean_crisis_score <= 0.18
        and fixed.mean_total_score - adaptive.mean_total_score <= 0.12
    )
    supports_dependency = (
        social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    return VerdictRow(
        selected_router=router.name,
        allocator_iterations=cfg.allocator_iterations,
        allocator_population=cfg.allocator_population,
        adaptive_total_score=adaptive.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        adaptive_crisis_score=adaptive.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        adaptive_resolved_rate=adaptive.mean_resolved_rate,
        fixed_joint_resolved_rate=fixed.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        adaptive_coupled_response=adaptive.mean_coupled_response_rate,
        fixed_joint_coupled_response=fixed.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        adaptive_gain_over_return_selected=adaptive.mean_total_score - returned.mean_total_score,
        adaptive_gap_to_fixed_joint=fixed.mean_total_score - adaptive.mean_total_score,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=adaptive.shock_gate_pass_rate,
        post_gate_shock_rate=adaptive.post_gate_shock_rate,
        survival_at_12h=adaptive.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_adaptive_allocation=supports_adaptive,
        supports_non_fixed_transfer=supports_non_fixed,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_adaptive and supports_non_fixed and supports_dependency else "partial_or_failed",
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
            20261331,
        )
        social_model, social_training = report113.train_action_model(
            cfg,
            device,
            "social",
            social_sequences,
            social_labels,
            flags,
            20261332,
        )
        selected_allocator, allocator_selection = optimize_allocator(
            cfg,
            models["gru"],
            env_model,
            social_model,
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
            fixed_row = run_fixed_joint_episode(seed, cfg, models["gru"], env_model, social_model, device, selected_router)
            eval_rows.append(fixed_row)
            adaptive_row, maybe_trace, tracker = run_adaptive_episode(
                seed,
                cfg,
                models["gru"],
                env_model,
                social_model,
                device,
                selected_router,
                selected_allocator,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(adaptive_row)
            crisis_logs[f"{seed}:fixed_joint_gru:none"] = []
            crisis_logs[f"{seed}:adaptive_allocator_gru:none"] = tracker.response_log
            if maybe_trace.frames:
                trace_out = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker = run_adaptive_episode(
                    seed,
                    cfg,
                    models["gru"],
                    env_model,
                    social_model,
                    device,
                    selected_router,
                    selected_allocator,
                    ablation=ablation,
                )
                eval_rows.append(replace(row, ablation=ablation))
                crisis_logs[f"{seed}:adaptive_allocator_gru:{ablation}"] = tracker.response_log

    summary = coupled.summarize(eval_rows)
    ablations = ablations_from_summary(summary)
    probes = allocator_probes(selected_allocator, schedules)
    verdict = transfer_verdict(summary, ablations, selected_router, schedules, cfg)
    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "adaptive_allocator", "frames": []}
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
            "allocator_iterations": cfg.allocator_iterations,
            "allocator_population": cfg.allocator_population,
            "allocator_elites": cfg.allocator_elites,
            "allocator_sigma": cfg.allocator_sigma,
            "device": cfg.device,
            "trace_seed": cfg.trace_seed,
        },
        "allocation_inputs": list(ALLOC_INPUTS),
        "selected_allocator": list(selected_allocator),
        "fixed_joint_baseline": list(FIXED_JOINT),
        "schedule": [asdict(row) for row in schedules],
        "router_selection": [asdict(row) for row in router_selection],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "allocator_selection": [asdict(row) for row in allocator_selection],
        "allocator_probes": [asdict(row) for row in probes],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace_payload,
        "crisis_logs": crisis_logs,
        "notes": {
            "claim": "closed-loop return search can train a compact adaptive allocator around learned environmental/social action heads",
            "not_claimed": "actor-critic reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
            "remaining_structure": "allocator features are engineered summaries and action heads remain supervised; this reduces fixed quota selection but does not remove structured arbitration",
        },
    }
    rows_to_csv(Path(f"{PREFIX}_schedule.csv"), schedules)
    rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    rows_to_csv(Path(f"{PREFIX}_action_training.csv"), [env_training, social_training])
    rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    rows_to_csv(Path(f"{PREFIX}_allocator_selection.csv"), allocator_selection)
    rows_to_csv(Path(f"{PREFIX}_allocator_probes.csv"), probes)
    rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    write_json(Path(f"{PREFIX}_results.json"), payload)
    write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_ADAPTIVE_ALLOCATOR_RESULTS", payload)
    write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_ADAPTIVE_ALLOCATOR_TRACE", trace_payload)
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
    parser.add_argument("--allocator-iterations", type=int, default=2)
    parser.add_argument("--allocator-population", type=int, default=7)
    parser.add_argument("--allocator-elites", type=int, default=3)
    parser.add_argument("--allocator-sigma", type=float, default=0.42)
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
        allocator_iterations=args.allocator_iterations,
        allocator_population=args.allocator_population,
        allocator_elites=args.allocator_elites,
        allocator_sigma=args.allocator_sigma,
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "allocator_selection": payload["allocator_selection"],
        "verdict": payload["verdict"],
        "summary": payload["summary"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
