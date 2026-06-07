#!/usr/bin/env python3
"""Minimum-channel planner for SSRM-3D randomized coupled crises.

Report 122 showed that explicit two-channel process supervision can still
collapse into a one-channel policy. This benchmark keeps the successful learned
environmental/social action heads from the joint-arbitration line, but removes
the fixed quota as the primary decision surface. A dynamic planner computes
environmental and social response targets from pressure features plus the
current response balance, then asks the learned action heads to fill the weaker
channel first.

This is bounded model-based arbitration evidence. It is not open-ended
civilization, unsupplied action discovery, subjective consciousness, or mature
deep reinforcement learning.
"""

from __future__ import annotations

import argparse
import contextlib
import csv
import json
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Sequence, Tuple

import torch

import ssrm_3d_coupled_crisis_adaptive_allocator_controller as report115
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
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_min_channel_planner"
FIXED_JOINT = report115.FIXED_JOINT
ORIGINAL_COORDINATOR = report113.coordinator_action


@dataclass(frozen=True)
class PlannerCandidate:
    name: str
    base_target: float
    pressure_weight: float
    imbalance_weight: float
    starvation_weight: float
    max_target: float
    strength: float
    strength_imbalance_weight: float


PLANNER_CANDIDATES = (
    PlannerCandidate("conservative_min", 0.08, 0.08, 0.34, 0.18, 0.22, 0.82, 0.20),
    PlannerCandidate("balanced_min", 0.10, 0.10, 0.46, 0.24, 0.28, 0.96, 0.28),
    PlannerCandidate("urgent_min", 0.12, 0.14, 0.58, 0.30, 0.34, 1.10, 0.36),
    PlannerCandidate("env_social_guard", 0.13, 0.10, 0.62, 0.28, 0.32, 1.04, 0.32),
    PlannerCandidate("high_pressure_guard", 0.14, 0.16, 0.68, 0.36, 0.38, 1.18, 0.42),
)

CURRENT_PLANNER = PLANNER_CANDIDATES[1]


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
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class PlannerSelectionRow:
    planner: str
    base_target: float
    pressure_weight: float
    imbalance_weight: float
    starvation_weight: float
    max_target: float
    strength: float
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
class PlannerProbeRow:
    seed: int
    hour: float
    planner: str
    env_target: float
    social_target: float
    strength: float
    env_pressure: float
    social_pressure: float
    env_fraction: float
    social_fraction: float


@dataclass(frozen=True)
class VerdictRow:
    selected_router: str
    selected_planner: str
    min_channel_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    min_channel_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    min_channel_resolved_rate: float
    fixed_joint_resolved_rate: float
    return_selected_resolved_rate: float
    min_channel_env_response: float
    min_channel_social_response: float
    min_channel_coupled_response: float
    fixed_joint_coupled_response: float
    return_selected_coupled_response: float
    min_channel_gain_over_return_selected: float
    min_channel_gap_to_fixed_joint: float
    social_culture_crisis_loss: float
    environment_crisis_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    mean_crisis_count: float
    supports_min_channel_planning: bool
    supports_non_fixed_transfer: bool
    supports_social_environment_dependency: bool
    verdict: str


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def parse_ints(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def response_pressure(inputs: Sequence[float]) -> Tuple[float, float]:
    index = report115.ALLOC_INPUTS.index
    env_pressure = max(
        inputs[index("env_pressure")],
        inputs[index("infrastructure_need")] * 0.90,
        inputs[index("resource_need")] * 0.82,
        inputs[index("weather_pressure")] * 0.72,
        inputs[index("body_need")] * 0.58,
    )
    social_pressure = max(
        inputs[index("social_pressure")],
        inputs[index("teaching_need")] * 0.86,
        inputs[index("body_need")] * 0.34,
    )
    return clamp(env_pressure), clamp(social_pressure)


def planner_targets(
    planner: PlannerCandidate,
    features: Sequence[float],
    action_counts: Dict[str, int],
    alive_count: int,
    ablation: str = "none",
) -> Tuple[float, float, float, List[float]]:
    inputs = report115.allocation_inputs(features, action_counts, alive_count)
    env_pressure, social_pressure = response_pressure(inputs)
    index = report115.ALLOC_INPUTS.index
    env_fraction = inputs[index("env_fraction")]
    social_fraction = inputs[index("social_fraction")]
    env_shortfall = max(0.0, social_fraction - env_fraction)
    social_shortfall = max(0.0, env_fraction - social_fraction)
    starvation = max(0.0, 0.18 - min(env_fraction, social_fraction))
    env_target = planner.base_target + planner.pressure_weight * env_pressure + planner.imbalance_weight * env_shortfall + planner.starvation_weight * starvation
    social_target = planner.base_target + planner.pressure_weight * social_pressure + planner.imbalance_weight * social_shortfall + planner.starvation_weight * starvation
    if ablation == "environment":
        env_target = 0.0
    if ablation == "social_culture":
        social_target = 0.0
    env_target = min(planner.max_target, clamp(env_target))
    social_target = min(planner.max_target, clamp(social_target))
    strength = clamp(
        planner.strength
        + planner.strength_imbalance_weight * abs(env_fraction - social_fraction)
        + starvation * 0.70,
        0.35,
        1.55,
    )
    return env_target, social_target, strength, inputs


def min_channel_coordinator_action(
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
    env_target, social_target, planner_strength, _ = planner_targets(
        CURRENT_PLANNER,
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
        planner_strength,
        device,
        ablation,
    )


@contextlib.contextmanager
def patched_min_channel_planner(planner: PlannerCandidate) -> Iterator[None]:
    global CURRENT_PLANNER
    previous_planner = CURRENT_PLANNER
    previous_coordinator = report113.coordinator_action
    CURRENT_PLANNER = planner
    report113.coordinator_action = min_channel_coordinator_action
    try:
        yield
    finally:
        CURRENT_PLANNER = previous_planner
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
    balance = 1.0 - abs(env_response - social_response)
    objective = total * 0.46 + crisis * 1.16 + resolved * 0.70 + coupled_response * 0.88 + balance * 0.18 - damage * 0.34
    return total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective


def run_min_channel_episode(
    seed: int,
    cfg: Config,
    model: base.ControllerNet,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
    planner: PlannerCandidate,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, object, coupled.CrisisTracker]:
    with patched_min_channel_planner(planner):
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
    if trace and getattr(trace_out, "frames", None):
        trace_out.condition = f"min_channel_planner_gru:{planner.name}:{ablation}"
    return replace(row, controller="min_channel_planner_gru"), trace_out, tracker


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


def select_planner(
    cfg: Config,
    model: base.ControllerNet,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[PlannerCandidate, List[PlannerSelectionRow]]:
    selected = PLANNER_CANDIDATES[0]
    best_objective = -1e9
    rows: List[PlannerSelectionRow] = []
    for planner in PLANNER_CANDIDATES:
        eval_rows = [
            run_min_channel_episode(seed, cfg, model, env_model, social_model, device, router, planner)[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_objective = objective
            selected = planner
        rows.append(PlannerSelectionRow(
            planner=planner.name,
            base_target=planner.base_target,
            pressure_weight=planner.pressure_weight,
            imbalance_weight=planner.imbalance_weight,
            starvation_weight=planner.starvation_weight,
            max_target=planner.max_target,
            strength=planner.strength,
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
    return selected, [replace(row, selected=(row.planner == selected.name)) for row in rows]


def ablations_from_summary(summary: Sequence[coupled.SummaryRow]) -> List[coupled.AblationRow]:
    base_row = coupled.row_lookup(summary, "min_channel_planner_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = coupled.row_lookup(summary, "min_channel_planner_gru", ablation)
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


def planner_probes(planner: PlannerCandidate, schedules: Sequence[report114.ScheduleRow]) -> List[PlannerProbeRow]:
    probes: List[PlannerProbeRow] = []
    feature = report111.FEATURE
    for row in schedules:
        if row.phase != "eval":
            continue
        for hour, env_count, social_count in (
            (row.first_crisis_hour, 0, 0),
            (min(95.0, row.first_crisis_hour + 1.0), 3, 0),
            (min(95.0, row.first_crisis_hour + 2.0), 0, 3),
        ):
            values = [0.55] * base.FEATURE_COUNT
            values[feature["post_gate"]] = 1.0
            values[feature["major_shocks"]] = clamp(hour / 96.0)
            values[feature["contamination"]] = 0.42 if "contaminated" in row.profile_sequence else 0.18
            values[feature["disease"]] = 0.38 if "quarantine" in row.profile_sequence else 0.16
            values[feature["route_hazard"]] = 0.42 if "route" in row.profile_sequence else 0.18
            values[feature["rainfall"]] = 0.48 if "storm" in row.profile_sequence else 0.18
            values[feature["wind"]] = 0.46 if "storm" in row.profile_sequence else 0.18
            values[feature["conflict"]] = 0.38
            values[feature["social_trust"]] = 0.50
            action_counts = {}
            if env_count:
                action_counts["sanitize"] = env_count
            if social_count:
                action_counts["social_repair"] = social_count
            env, social, strength, inputs = planner_targets(planner, values, action_counts, 14)
            env_pressure, social_pressure = response_pressure(inputs)
            index = report115.ALLOC_INPUTS.index
            probes.append(PlannerProbeRow(
                seed=row.seed,
                hour=hour,
                planner=planner.name,
                env_target=env,
                social_target=social,
                strength=strength,
                env_pressure=env_pressure,
                social_pressure=social_pressure,
                env_fraction=inputs[index("env_fraction")],
                social_fraction=inputs[index("social_fraction")],
            ))
    return probes


def transfer_verdict(
    summary: Sequence[coupled.SummaryRow],
    ablations: Sequence[coupled.AblationRow],
    router: report105.PressureRouter,
    schedules: Sequence[report114.ScheduleRow],
    planner: PlannerCandidate,
) -> VerdictRow:
    min_channel = coupled.row_lookup(summary, "min_channel_planner_gru", "none")
    fixed = coupled.row_lookup(summary, "fixed_joint_gru", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    supports_planning = (
        mean_crisis_count >= 4.0
        and min_channel.mean_total_score - returned.mean_total_score >= 0.010
        and min_channel.mean_crisis_score - returned.mean_crisis_score >= 0.040
        and min_channel.mean_resolved_rate - returned.mean_resolved_rate >= 0.080
        and min_channel.mean_coupled_response_rate - returned.mean_coupled_response_rate >= 0.080
        and min_channel.mean_alive_at_12h >= 12.0
        and min_channel.shock_gate_pass_rate == 1.0
        and min_channel.post_gate_shock_rate == 1.0
    )
    supports_non_fixed = (
        min_channel.mean_crisis_score >= 0.45
        and min_channel.mean_coupled_response_rate >= 0.55
        and fixed.mean_crisis_score - min_channel.mean_crisis_score <= 0.18
        and fixed.mean_total_score - min_channel.mean_total_score <= 0.12
    )
    supports_dependency = (
        social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    return VerdictRow(
        selected_router=router.name,
        selected_planner=planner.name,
        min_channel_total_score=min_channel.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        min_channel_crisis_score=min_channel.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        min_channel_resolved_rate=min_channel.mean_resolved_rate,
        fixed_joint_resolved_rate=fixed.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        min_channel_env_response=min_channel.mean_env_response_rate,
        min_channel_social_response=min_channel.mean_social_response_rate,
        min_channel_coupled_response=min_channel.mean_coupled_response_rate,
        fixed_joint_coupled_response=fixed.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        min_channel_gain_over_return_selected=min_channel.mean_total_score - returned.mean_total_score,
        min_channel_gap_to_fixed_joint=fixed.mean_total_score - min_channel.mean_total_score,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=min_channel.shock_gate_pass_rate,
        post_gate_shock_rate=min_channel.post_gate_shock_rate,
        survival_at_12h=min_channel.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_min_channel_planning=supports_planning,
        supports_non_fixed_transfer=supports_non_fixed,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_planning and supports_non_fixed and supports_dependency else "partial_or_failed",
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
        selected_planner, planner_selection = select_planner(
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
            min_row, maybe_trace, tracker = run_min_channel_episode(
                seed,
                cfg,
                models["gru"],
                env_model,
                social_model,
                device,
                selected_router,
                selected_planner,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(min_row)
            crisis_logs[f"{seed}:fixed_joint_gru:none"] = []
            crisis_logs[f"{seed}:min_channel_planner_gru:none"] = tracker.response_log
            if maybe_trace.frames:
                trace_out = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker = run_min_channel_episode(
                    seed,
                    cfg,
                    models["gru"],
                    env_model,
                    social_model,
                    device,
                    selected_router,
                    selected_planner,
                    ablation=ablation,
                )
                eval_rows.append(replace(row, ablation=ablation))
                crisis_logs[f"{seed}:min_channel_planner_gru:{ablation}"] = tracker.response_log

    summary = coupled.summarize(eval_rows)
    ablations = ablations_from_summary(summary)
    probes = planner_probes(selected_planner, schedules)
    verdict = transfer_verdict(summary, ablations, selected_router, schedules, selected_planner)
    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "min_channel_planner", "frames": []}
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
            "device": cfg.device,
            "trace_seed": cfg.trace_seed,
        },
        "planner_candidates": [asdict(row) for row in PLANNER_CANDIDATES],
        "fixed_joint_baseline": list(FIXED_JOINT),
        "schedule": [asdict(row) for row in schedules],
        "router_selection": [asdict(row) for row in router_selection],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "planner_selection": [asdict(row) for row in planner_selection],
        "planner_probes": [asdict(row) for row in probes],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace_payload,
        "crisis_logs": crisis_logs,
        "notes": {
            "claim": "dynamic weakest-channel planning can preserve coupled environmental/social repair across randomized post-12h crises",
            "not_claimed": "actor-critic reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
            "remaining_structure": "the planner uses engineered pressure summaries and learned action heads; this removes fixed quotas but not structured arbitration",
        },
    }
    rows_to_csv(Path(f"{PREFIX}_schedule.csv"), schedules)
    rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    rows_to_csv(Path(f"{PREFIX}_action_training.csv"), [env_training, social_training])
    rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    rows_to_csv(Path(f"{PREFIX}_planner_selection.csv"), planner_selection)
    rows_to_csv(Path(f"{PREFIX}_planner_probes.csv"), probes)
    rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    write_json(Path(f"{PREFIX}_results.json"), payload)
    write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_MIN_CHANNEL_PLANNER_RESULTS", payload)
    write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_MIN_CHANNEL_PLANNER_TRACE", trace_payload)
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
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "planner_selection": payload["planner_selection"],
        "verdict": payload["verdict"],
        "summary": payload["summary"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
