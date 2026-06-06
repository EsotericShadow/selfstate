#!/usr/bin/env python3
"""Randomized transfer stress for SSRM-3D coupled crisis joint arbitration.

Report 113 produced a bounded positive result, but it still used the standard
post-12h crisis schedule. This benchmark keeps the learned joint-arbitration
controller and asks whether it survives randomized post-gate crisis timing,
ordering, repetition, and initial world pressure.

The schedule remains gated: no major crisis is allowed before 12h. The result is
still a structured learned-coordination precursor, not actor-critic RL or
open-ended civilization.
"""

from __future__ import annotations

import argparse
import contextlib
import csv
import json
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Dict, Iterable, Iterator, List, Sequence, Tuple

import torch

import ssrm_3d_coupled_crisis_joint_arbitration_controller as report113
import ssrm_3d_coupled_social_environment_maturation_controller as coupled
import ssrm_3d_learned_multiday_maturation_controller as base
import ssrm_3d_return_selected_multiday_maturation_controller as report105
from ssrm_maturation.benchmark import make_world
from ssrm_maturation.environment import clamp
from ssrm_maturation.models import Trace, World


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_randomized_transfer"

ScheduleBuilder = Callable[[int], List[Tuple[float, coupled.CrisisProfile]]]
PrepareWorld = Callable[[random.Random, object], World]


@dataclass(frozen=True)
class Config:
    train_seeds: Sequence[int]
    tune_seeds: Sequence[int]
    eval_seeds: Sequence[int]
    hours: float = 96.0
    step_hours: float = 0.10
    population: int = 14
    epochs: int = 42
    hidden_size: int = 64
    learning_rate: float = 0.004
    action_epochs: int = 64
    action_hidden_size: int = 64
    action_learning_rate: float = 0.004
    joint_candidates: Sequence[Tuple[float, float, float]] = (
        (0.0, 0.0, 0.0),
        (0.10, 0.10, 0.70),
        (0.12, 0.12, 0.80),
        (0.14, 0.14, 0.90),
        (0.16, 0.14, 1.00),
        (0.14, 0.16, 1.00),
        (0.18, 0.16, 1.10),
        (0.16, 0.18, 1.10),
        (0.20, 0.18, 1.20),
    )
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class ScheduleRow:
    phase: str
    seed: int
    crisis_count: int
    first_crisis_hour: float
    last_crisis_hour: float
    profile_sequence: str


@dataclass(frozen=True)
class VerdictRow:
    selected_router: str
    selected_env_quota: float
    selected_social_quota: float
    selected_coordinator_strength: float
    randomized_total_score: float
    return_selected_total_score: float
    randomized_crisis_score: float
    return_selected_crisis_score: float
    randomized_resolved_rate: float
    return_selected_resolved_rate: float
    randomized_coupled_response: float
    return_selected_coupled_response: float
    social_culture_crisis_loss: float
    environment_crisis_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    mean_crisis_count: float
    supports_randomized_transfer: bool
    supports_social_environment_dependency: bool
    verdict: str


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def parse_ints(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def parse_joint_candidates(value: str) -> Tuple[Tuple[float, float, float], ...]:
    candidates: List[Tuple[float, float, float]] = []
    for part in value.split(","):
        if not part.strip():
            continue
        fields = [float(item.strip()) for item in part.split(":")]
        if len(fields) != 3:
            raise ValueError(f"joint candidate must be env:social:strength, got {part!r}")
        candidates.append((fields[0], fields[1], fields[2]))
    return tuple(candidates)


def randomized_schedule_builder(hours: float) -> ScheduleBuilder:
    def build(seed: int) -> List[Tuple[float, coupled.CrisisProfile]]:
        rng = random.Random(seed * 197 + 114)
        current = 13.0 + rng.random() * 5.0
        schedule: List[Tuple[float, coupled.CrisisProfile]] = []
        previous_name = ""
        while current < hours - 7.5:
            candidates = [profile for profile in coupled.PROFILES if profile.name != previous_name]
            profile = rng.choice(candidates)
            schedule.append((round(current, 3), profile))
            previous_name = profile.name
            current += 8.8 + rng.random() * 8.6
        return schedule

    return build


def randomized_prepare_world(rng: random.Random, cfg: object) -> World:
    world = make_world(rng)
    world.food = clamp(world.food + rng.uniform(-0.12, 0.04))
    world.water = clamp(world.water + rng.uniform(-0.12, 0.04))
    world.materials = clamp(world.materials + rng.uniform(-0.10, 0.08))
    world.medicine = clamp(world.medicine + rng.uniform(-0.08, 0.05))
    world.shelter = clamp(world.shelter + rng.uniform(-0.10, 0.05))
    world.architecture = clamp(world.architecture + rng.uniform(-0.05, 0.06))
    world.tools = clamp(world.tools + rng.uniform(-0.08, 0.06))
    world.waterworks = clamp(world.waterworks + rng.uniform(-0.05, 0.05))
    world.granary = clamp(world.granary + rng.uniform(-0.05, 0.05))
    world.paths = clamp(world.paths + rng.uniform(-0.04, 0.06))
    world.sanitation = clamp(world.sanitation + rng.uniform(-0.06, 0.05))
    world.social_trust = clamp(world.social_trust + rng.uniform(-0.10, 0.05))
    world.conflict = clamp(world.conflict + rng.uniform(0.00, 0.10))
    world.contamination = clamp(world.contamination + rng.uniform(0.00, 0.10))
    world.disease = clamp(world.disease + rng.uniform(0.00, 0.08))
    world.route_hazard = clamp(world.route_hazard + rng.uniform(0.00, 0.10))
    world.resource_migration = clamp(world.resource_migration + rng.uniform(0.00, 0.14))
    world.predators = clamp(world.predators + rng.uniform(0.00, 0.08))
    world.next_shock = cfg.hours + 100.0
    return world


@contextlib.contextmanager
def patched_transfer_world(schedule_builder: ScheduleBuilder, prepare_world: PrepareWorld) -> Iterator[None]:
    original_schedule = coupled.crisis_schedule
    original_prepare = coupled.prepare_world
    coupled.crisis_schedule = schedule_builder
    coupled.prepare_world = prepare_world
    try:
        yield
    finally:
        coupled.crisis_schedule = original_schedule
        coupled.prepare_world = original_prepare


def schedule_rows(cfg: Config, phase: str, seeds: Sequence[int], builder: ScheduleBuilder) -> List[ScheduleRow]:
    rows: List[ScheduleRow] = []
    for seed in seeds:
        schedule = builder(seed)
        starts = [start for start, _ in schedule]
        rows.append(ScheduleRow(
            phase=phase,
            seed=seed,
            crisis_count=len(schedule),
            first_crisis_hour=starts[0] if starts else 0.0,
            last_crisis_hour=starts[-1] if starts else 0.0,
            profile_sequence=";".join(profile.name for _, profile in schedule),
        ))
    return rows


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


def transfer_verdict(
    summary: Sequence[coupled.SummaryRow],
    ablations: Sequence[coupled.AblationRow],
    selected_router: report105.PressureRouter,
    selected_joint: Tuple[float, float, float],
    schedules: Sequence[ScheduleRow],
) -> VerdictRow:
    outcome = coupled.row_lookup(summary, "joint_arbitration_gru", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    env_quota, social_quota, strength = selected_joint
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    supports_transfer = (
        strength > 0.0
        and mean_crisis_count >= 4.0
        and outcome.mean_total_score - returned.mean_total_score >= 0.010
        and outcome.mean_crisis_score - returned.mean_crisis_score >= 0.040
        and outcome.mean_resolved_rate - returned.mean_resolved_rate >= 0.080
        and outcome.mean_coupled_response_rate - returned.mean_coupled_response_rate >= 0.080
        and outcome.mean_alive_at_12h >= 12.0
        and outcome.shock_gate_pass_rate == 1.0
        and outcome.post_gate_shock_rate == 1.0
    )
    supports_dependency = (
        social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    return VerdictRow(
        selected_router=selected_router.name,
        selected_env_quota=env_quota,
        selected_social_quota=social_quota,
        selected_coordinator_strength=strength,
        randomized_total_score=outcome.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        randomized_crisis_score=outcome.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        randomized_resolved_rate=outcome.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        randomized_coupled_response=outcome.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=outcome.shock_gate_pass_rate,
        post_gate_shock_rate=outcome.post_gate_shock_rate,
        survival_at_12h=outcome.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_randomized_transfer=supports_transfer,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_transfer and supports_dependency else "partial_or_failed",
    )


def run_benchmark(cfg: Config) -> dict[str, object]:
    device = base.resolve_device(cfg.device)
    schedule_builder = randomized_schedule_builder(cfg.hours)
    schedules = (
        schedule_rows(cfg, "train", cfg.train_seeds, schedule_builder)
        + schedule_rows(cfg, "tune", cfg.tune_seeds, schedule_builder)
        + schedule_rows(cfg, "eval", cfg.eval_seeds, schedule_builder)
    )
    with patched_transfer_world(schedule_builder, randomized_prepare_world):
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
            20261221,
        )
        social_model, social_training = report113.train_action_model(
            cfg,
            device,
            "social",
            social_sequences,
            social_labels,
            flags,
            20261222,
        )
        selected_joint, joint_selection = report113.select_joint_candidate(
            cfg,
            models["gru"],
            env_model,
            social_model,
            device,
            selected_router,
        )

        eval_rows: List[coupled.EvalRow] = []
        trace = Trace(seed=cfg.trace_seed, condition="randomized_transfer")
        crisis_logs: Dict[str, List[dict[str, object]]] = {}
        env_quota, social_quota, strength = selected_joint
        for seed in cfg.eval_seeds:
            for controller, model, router in (
                ("designed", None, report105.ROUTERS[0]),
                ("reactive", None, report105.ROUTERS[0]),
                ("frame_mlp", models["frame_mlp"], report105.ROUTERS[0]),
                ("gru", models["gru"], report105.ROUTERS[0]),
                ("return_selected_gru", models["gru"], selected_router),
                ("joint_arbitration_gru", models["gru"], selected_router),
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
                    env_quota if controller == "joint_arbitration_gru" else 0.0,
                    social_quota if controller == "joint_arbitration_gru" else 0.0,
                    strength if controller == "joint_arbitration_gru" else 0.0,
                    trace=(seed == cfg.trace_seed and controller == "joint_arbitration_gru"),
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:{controller}:none"] = tracker.response_log
                if maybe_trace.frames:
                    trace = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker = report113.run_episode(
                    seed,
                    cfg,
                    "joint_arbitration_gru",
                    models["gru"],
                    env_model,
                    social_model,
                    device,
                    selected_router,
                    env_quota,
                    social_quota,
                    strength,
                    ablation=ablation,
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:joint_arbitration_gru:{ablation}"] = tracker.response_log

    summary = coupled.summarize(eval_rows)
    ablations = report113.ablations_from_summary(summary)
    verdict = transfer_verdict(summary, ablations, selected_router, selected_joint, schedules)
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
            "joint_candidates": [list(candidate) for candidate in cfg.joint_candidates],
            "device": cfg.device,
            "trace_seed": cfg.trace_seed,
        },
        "crisis_profiles": [asdict(profile) for profile in coupled.PROFILES],
        "schedule": [asdict(row) for row in schedules],
        "routers": [asdict(router) for router in report105.ROUTERS],
        "router_selection": [asdict(row) for row in router_selection],
        "joint_selection": [asdict(row) for row in joint_selection],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": asdict(trace),
        "crisis_logs": crisis_logs,
        "notes": {
            "claim": "randomized post-12h schedule transfer for joint environmental/social crisis arbitration",
            "not_claimed": "actor-critic reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
            "input_discipline": "no active crisis profile labels in learned-controller inputs; schedules and initial world pressure vary by seed",
        },
    }
    rows_to_csv(Path(f"{PREFIX}_schedule.csv"), schedules)
    rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    rows_to_csv(Path(f"{PREFIX}_action_training.csv"), [env_training, social_training])
    rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    rows_to_csv(Path(f"{PREFIX}_joint_selection.csv"), joint_selection)
    rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    write_json(Path(f"{PREFIX}_results.json"), payload)
    write_json(Path(f"{PREFIX}_trace.json"), asdict(trace))
    write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_RANDOMIZED_TRANSFER_RESULTS", payload)
    write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_RANDOMIZED_TRANSFER_TRACE", asdict(trace))
    return payload


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-seeds", default="20260911,20260912,20260913,20260914,20260915,20260916")
    parser.add_argument("--tune-seeds", default="20261111,20261112,20261113")
    parser.add_argument("--eval-seeds", default="20261121,20261122,20261123,20261124,20261125")
    parser.add_argument("--hours", type=float, default=96.0)
    parser.add_argument("--step-hours", type=float, default=0.10)
    parser.add_argument("--population", type=int, default=14)
    parser.add_argument("--epochs", type=int, default=42)
    parser.add_argument("--hidden-size", type=int, default=64)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--action-epochs", type=int, default=64)
    parser.add_argument("--action-hidden-size", type=int, default=64)
    parser.add_argument("--action-learning-rate", type=float, default=0.004)
    parser.add_argument("--joint-candidates", default="0.00:0.00:0.00,0.10:0.10:0.70,0.12:0.12:0.80,0.14:0.14:0.90,0.16:0.14:1.00,0.14:0.16:1.00,0.18:0.16:1.10,0.16:0.18:1.10,0.20:0.18:1.20")
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
        joint_candidates=parse_joint_candidates(args.joint_candidates),
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "schedule": payload["schedule"],
        "joint_selection": payload["joint_selection"],
        "verdict": payload["verdict"],
        "summary": payload["summary"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
