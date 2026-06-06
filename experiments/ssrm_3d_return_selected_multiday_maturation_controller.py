#!/usr/bin/env python3
"""Return-selected pressure router for the SSRM-3D multi-day maturation world.

Report 104 showed that a GRU imitation controller can run the 72h world
closed-loop, but several ablations remained weak. This experiment adds a small
return-selected layer around the GRU: candidate pressure routers bias action
logits from sensed social, environmental, infrastructure, tool, and teaching
pressure, then validation-world return selects the candidate before held-out
evaluation.

This is still not deep reinforcement learning. It is a bounded return-selection
precursor: the learned model proposes actions, and closed-loop validation
selects the pressure-bias setting.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import torch

import ssrm_3d_learned_multiday_maturation_controller as base
from ssrm_maturation.agents import choose_action, make_agents
from ssrm_maturation.benchmark import TRACE_CHECKPOINTS, make_world, score_episode, snapshot
from ssrm_maturation.environment import clamp, living
from ssrm_maturation.models import CONDITIONS, Agent, Condition, Trace, World


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"


@dataclass(frozen=True)
class Config:
    train_seeds: Sequence[int]
    tune_seeds: Sequence[int]
    eval_seeds: Sequence[int]
    hours: float = 72.0
    step_hours: float = 0.10
    population: int = 14
    epochs: int = 42
    hidden_size: int = 64
    learning_rate: float = 0.004
    device: str = "auto"
    trace_seed: int = 20260941


@dataclass(frozen=True)
class PressureRouter:
    name: str
    social_bias: float
    environment_bias: float
    infrastructure_bias: float
    tool_bias: float
    teaching_bias: float


ROUTERS = (
    PressureRouter("none", 0.0, 0.0, 0.0, 0.0, 0.0),
    PressureRouter("balanced", 1.00, 1.00, 1.00, 1.00, 1.00),
    PressureRouter("social_env", 1.55, 1.45, 0.75, 0.70, 1.20),
    PressureRouter("environment_first", 0.55, 2.00, 0.70, 0.65, 0.55),
    PressureRouter("social_first", 2.00, 0.55, 0.60, 0.60, 1.35),
    PressureRouter("build_tool", 0.45, 0.70, 1.65, 1.70, 0.55),
    PressureRouter("teaching_tradition", 1.10, 0.75, 0.70, 0.70, 2.00),
    PressureRouter("high_pressure", 1.80, 1.60, 1.30, 1.25, 1.50),
)


@dataclass(frozen=True)
class SelectionRow:
    router: str
    social_bias: float
    environment_bias: float
    infrastructure_bias: float
    tool_bias: float
    teaching_bias: float
    tune_score: float
    tune_development: float
    tune_knowledge: float
    tune_recovery: float
    tune_births: float
    selection_objective: float
    selected: bool


@dataclass(frozen=True)
class VerdictRow:
    selected_router: str
    selected_score: float
    base_gru_score: float
    designed_score: float
    frame_score: float
    reactive_score: float
    gain_over_base_gru: float
    gain_over_frame: float
    gain_over_reactive: float
    gap_to_designed: float
    body_ablation_loss: float
    infrastructure_ablation_loss: float
    tools_ablation_loss: float
    social_culture_ablation_loss: float
    environment_ablation_loss: float
    previous_action_ablation_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    supports_return_selection: bool
    supports_pressure_ablation_specificity: bool
    verdict: str


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def idx(name: str) -> int:
    return base.FEATURE_NAMES.index(name)


FEATURE = {name: idx(name) for name in base.FEATURE_NAMES}


def pressure_value(features: Sequence[float], ablation: str) -> Dict[str, float]:
    masked = base.mask_features(list(features), ablation)
    social = clamp(
        masked[FEATURE["conflict"]] * 0.44
        + max(0.0, 0.58 - masked[FEATURE["social_trust"]]) * 0.30
        + max(0.0, 0.62 - masked[FEATURE["culture"]]) * 0.18
        + max(0.0, 0.54 - masked[FEATURE["symbols"]]) * 0.14
    )
    environment = clamp(
        masked[FEATURE["contamination"]] * 0.22
        + masked[FEATURE["disease"]] * 0.24
        + masked[FEATURE["predators"]] * 0.18
        + masked[FEATURE["route_hazard"]] * 0.18
        + masked[FEATURE["resource_migration"]] * 0.12
        + masked[FEATURE["resource_depletion"]] * 0.12
        + abs(masked[FEATURE["temperature"]] - 0.55) * 0.14
        + max(0.0, 0.52 - masked[FEATURE["visibility"]]) * 0.10
    )
    infrastructure = clamp(
        max(0.0, 0.62 - masked[FEATURE["shelter"]]) * 0.22
        + max(0.0, 0.62 - masked[FEATURE["architecture"]]) * 0.22
        + max(0.0, 0.56 - masked[FEATURE["waterworks"]]) * 0.18
        + max(0.0, 0.52 - masked[FEATURE["granary"]]) * 0.14
        + max(0.0, 0.52 - masked[FEATURE["paths"]]) * 0.14
        + max(0.0, 0.50 - masked[FEATURE["sanitation"]]) * 0.12
    )
    tools = clamp(
        max(0.0, 0.76 - masked[FEATURE["tools"]]) * 0.36
        + max(0.0, 0.62 - masked[FEATURE["workshop"]]) * 0.24
        + max(0.0, 0.48 - masked[FEATURE["fire_control"]]) * 0.14
        + max(0.0, 0.75 - masked[FEATURE["tool_tier"]]) * 0.18
    )
    teaching = clamp(
        max(0.0, 0.72 - masked[FEATURE["knowledge_transfer"]]) * 0.34
        + max(0.0, 0.66 - masked[FEATURE["culture"]]) * 0.22
        + max(0.0, 0.58 - masked[FEATURE["risk_memory"]]) * 0.18
        + max(0.0, 0.52 - masked[FEATURE["symbols"]]) * 0.12
    )
    return {
        "social": social,
        "environment": environment,
        "infrastructure": infrastructure,
        "tools": tools,
        "teaching": teaching,
    }


def router_bias(features: Sequence[float], router: PressureRouter, device: torch.device, dtype: torch.dtype, ablation: str) -> torch.Tensor:
    pressure = pressure_value(features, ablation)
    bias = torch.zeros((1, len(base.ACTIONS)), dtype=dtype, device=device)
    bias[:, base.ACTION_TO_INDEX["social_repair"]] += pressure["social"] * router.social_bias
    bias[:, base.ACTION_TO_INDEX["teach"]] += pressure["social"] * router.social_bias * 0.38
    bias[:, base.ACTION_TO_INDEX["sanitize"]] += pressure["environment"] * router.environment_bias * 0.65
    bias[:, base.ACTION_TO_INDEX["treat"]] += pressure["environment"] * router.environment_bias * 0.42
    bias[:, base.ACTION_TO_INDEX["scout"]] += pressure["environment"] * router.environment_bias * 0.72
    bias[:, base.ACTION_TO_INDEX["construct"]] += pressure["infrastructure"] * router.infrastructure_bias
    bias[:, base.ACTION_TO_INDEX["improve_tools"]] += pressure["tools"] * router.tool_bias
    bias[:, base.ACTION_TO_INDEX["teach"]] += pressure["teaching"] * router.teaching_bias
    bias[:, base.ACTION_TO_INDEX["learn"]] += pressure["teaching"] * router.teaching_bias * 0.30
    return bias


def initial_baseline(world: World, population: int) -> dict[str, float]:
    return base.initial_baseline(world, population)


def run_episode(
    seed: int,
    cfg: Config,
    controller: str,
    model: Optional[base.ControllerNet],
    device: torch.device,
    router: PressureRouter,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[base.EvalRow, Trace]:
    condition = CONDITIONS[1] if controller == "reactive" else CONDITIONS[0]
    rng = random.Random(seed * 97 + sum(ord(ch) for ch in controller + router.name + ablation))
    agents = make_agents(rng, cfg.population)
    world = make_world(rng)
    baseline = initial_baseline(world, cfg.population)
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    trace_out = Trace(seed=seed, condition=f"{controller}:{router.name}:{ablation}")
    checkpoints = list(TRACE_CHECKPOINTS)
    no_pre_gate_shock = True
    alive_at_12h = cfg.population
    at_12: dict[str, float] = {}
    if trace:
        trace_out.frames.append(snapshot(world, agents, "0h", events))
        if checkpoints and checkpoints[0] == 0.0:
            checkpoints.pop(0)

    def selector(agent: Agent, current_world: World, current_condition: Condition, current_rng: random.Random, features: List[float], previous: int) -> str:
        if controller == "designed":
            return choose_action(agent, current_world, current_condition, current_rng)
        if controller == "reactive":
            return choose_action(agent, current_world, current_condition, current_rng)
        if model is None:
            return "rest"
        model_features = torch.tensor([base.mask_features(features, ablation)], dtype=torch.float32, device=device)
        with torch.no_grad():
            if model.architecture == "gru":
                state = recurrent_states.get(agent.ident)
                logits, next_state = model.step(model_features, state)
                if next_state is not None:
                    recurrent_states[agent.ident] = next_state.detach()
            else:
                logits, _ = model.step(model_features, None)
            if controller == "return_selected_gru":
                logits = logits + router_bias(features, router, device, logits.dtype, ablation)
            return base.INDEX_TO_ACTION[int(logits.argmax(dim=-1).item())]

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
        if world.time < 12.0 and world.major_shocks > 0:
            no_pre_gate_shock = False
        if world.time >= 12.0 and not at_12:
            alive_at_12h = len(living(agents))
            at_12 = {
                "development": clamp((world.architecture - baseline["architecture"]) * 0.48 + (world.tools + world.workshop * 0.45 + world.fire_control * 0.30 - baseline["tool_system"]) * 0.34 + (world.paths - baseline["paths"]) * 0.16),
                "knowledge": clamp(world.knowledge_transfer * 0.80 + (world.culture + world.symbols * 0.50 - baseline["culture_system"]) * 0.45),
            }
        while trace and checkpoints and world.time >= checkpoints[0] - 1e-9:
            hour = checkpoints.pop(0)
            trace_out.frames.append(snapshot(world, agents, f"{hour:g}h", events))

    row = score_episode(world, agents, baseline, at_12, seed, condition, alive_at_12h, no_pre_gate_shock)
    eval_row = base.EvalRow(
        seed=seed,
        controller=controller,
        ablation=ablation,
        final_alive=row.final_alive,
        total_agents=row.total_agents,
        alive_at_12h=row.alive_at_12h,
        no_major_shock_before_12h=row.no_major_shock_before_12h,
        post_gate_shock=row.post_gate_shock,
        births=row.births,
        deaths=row.deaths,
        architecture_tier=row.architecture_tier,
        tool_tier=row.tool_tier,
        architecture_delta=row.architecture_delta,
        tool_delta=row.tool_delta,
        culture_delta=row.culture_delta,
        risk_memory_delta=row.risk_memory_delta,
        knowledge_transfer=row.knowledge_transfer,
        adaptation_evidence=row.adaptation_evidence,
        pressure_integral=row.pressure_integral,
        survival_score=row.survival_score,
        development_score=row.development_score,
        knowledge_score=row.knowledge_score,
        recovery_score=row.recovery_score,
        maturation_score=row.maturation_score,
    )
    if trace and (not trace_out.frames or trace_out.frames[-1]["hours"] < cfg.hours):
        trace_out.frames.append(snapshot(world, agents, f"{cfg.hours:g}h", events))
    return eval_row, trace_out


def selection_objective(rows: Sequence[base.EvalRow]) -> Tuple[float, float, float, float, float]:
    score = mean(row.maturation_score for row in rows)
    development = mean(row.development_score for row in rows)
    knowledge = mean(row.knowledge_score for row in rows)
    recovery = mean(row.recovery_score for row in rows)
    births = mean(row.births for row in rows)
    objective = score + development * 0.025 + knowledge * 0.035 + recovery * 0.025 + min(4.0, births) * 0.006
    return score, development, knowledge, recovery, objective


def select_router(cfg: Config, model: base.ControllerNet, device: torch.device) -> Tuple[PressureRouter, List[SelectionRow]]:
    rows: List[SelectionRow] = []
    best = ROUTERS[0]
    best_objective = -1.0
    for router in ROUTERS:
        eval_rows = [run_episode(seed, cfg, "return_selected_gru", model, device, router)[0] for seed in cfg.tune_seeds]
        score, development, knowledge, recovery, objective = selection_objective(eval_rows)
        births = mean(row.births for row in eval_rows)
        if objective > best_objective:
            best = router
            best_objective = objective
        rows.append(
            SelectionRow(
                router=router.name,
                social_bias=router.social_bias,
                environment_bias=router.environment_bias,
                infrastructure_bias=router.infrastructure_bias,
                tool_bias=router.tool_bias,
                teaching_bias=router.teaching_bias,
                tune_score=score,
                tune_development=development,
                tune_knowledge=knowledge,
                tune_recovery=recovery,
                tune_births=births,
                selection_objective=objective,
                selected=False,
            )
        )
    return best, [
        SelectionRow(
            row.router,
            row.social_bias,
            row.environment_bias,
            row.infrastructure_bias,
            row.tool_bias,
            row.teaching_bias,
            row.tune_score,
            row.tune_development,
            row.tune_knowledge,
            row.tune_recovery,
            row.tune_births,
            row.selection_objective,
            row.router == best.name,
        )
        for row in rows
    ]


def summarize(rows: Sequence[base.EvalRow]) -> List[base.SummaryRow]:
    return base.summarize(rows)


def row_lookup(summary: Sequence[base.SummaryRow], controller: str, ablation: str) -> base.SummaryRow:
    for row in summary:
        if row.controller == controller and row.ablation == ablation:
            return row
    raise KeyError((controller, ablation))


def ablations_from_summary(summary: Sequence[base.SummaryRow]) -> List[base.AblationRow]:
    base_row = row_lookup(summary, "return_selected_gru", "none")
    rows: List[base.AblationRow] = []
    for ablation in ("body", "infrastructure", "tools", "social_culture", "environment", "previous_action"):
        row = row_lookup(summary, "return_selected_gru", ablation)
        rows.append(
            base.AblationRow(
                controller="return_selected_gru",
                ablation=ablation,
                mean_score=row.mean_maturation_score,
                score_loss=base_row.mean_maturation_score - row.mean_maturation_score,
                mean_development_score=row.mean_development_score,
                development_loss=base_row.mean_development_score - row.mean_development_score,
                mean_knowledge_score=row.mean_knowledge_score,
                knowledge_loss=base_row.mean_knowledge_score - row.mean_knowledge_score,
                mean_recovery_score=row.mean_recovery_score,
                recovery_loss=base_row.mean_recovery_score - row.mean_recovery_score,
            )
        )
    return rows


def verdict_from_summary(summary: Sequence[base.SummaryRow], ablations: Sequence[base.AblationRow], selected: PressureRouter) -> VerdictRow:
    selected_row = row_lookup(summary, "return_selected_gru", "none")
    base_gru = row_lookup(summary, "gru", "none")
    designed = row_lookup(summary, "designed", "none")
    frame = row_lookup(summary, "frame_mlp", "none")
    reactive = row_lookup(summary, "reactive", "none")
    losses = {row.ablation: row.score_loss for row in ablations}
    supports_return = (
        selected_row.shock_gate_pass_rate == 1.0
        and selected_row.post_gate_shock_rate == 1.0
        and selected_row.mean_alive_at_12h >= 12.0
        and selected_row.mean_maturation_score >= 0.70
        and selected_row.mean_maturation_score - reactive.mean_maturation_score >= 0.14
        and designed.mean_maturation_score - selected_row.mean_maturation_score <= 0.24
        and selected.name != "none"
    )
    supports_ablation = (
        losses["body"] >= 0.020
        and losses["infrastructure"] >= 0.020
        and losses["tools"] >= 0.020
        and losses["social_culture"] >= 0.020
        and losses["environment"] >= 0.020
    )
    return VerdictRow(
        selected_router=selected.name,
        selected_score=selected_row.mean_maturation_score,
        base_gru_score=base_gru.mean_maturation_score,
        designed_score=designed.mean_maturation_score,
        frame_score=frame.mean_maturation_score,
        reactive_score=reactive.mean_maturation_score,
        gain_over_base_gru=selected_row.mean_maturation_score - base_gru.mean_maturation_score,
        gain_over_frame=selected_row.mean_maturation_score - frame.mean_maturation_score,
        gain_over_reactive=selected_row.mean_maturation_score - reactive.mean_maturation_score,
        gap_to_designed=designed.mean_maturation_score - selected_row.mean_maturation_score,
        body_ablation_loss=losses["body"],
        infrastructure_ablation_loss=losses["infrastructure"],
        tools_ablation_loss=losses["tools"],
        social_culture_ablation_loss=losses["social_culture"],
        environment_ablation_loss=losses["environment"],
        previous_action_ablation_loss=losses["previous_action"],
        shock_gate_pass_rate=selected_row.shock_gate_pass_rate,
        post_gate_shock_rate=selected_row.post_gate_shock_rate,
        survival_at_12h=selected_row.mean_alive_at_12h,
        supports_return_selection=supports_return,
        supports_pressure_ablation_specificity=supports_ablation,
        verdict="pass" if supports_return and supports_ablation else "partial_or_failed",
    )


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


def run_benchmark(cfg: Config) -> dict[str, object]:
    device = base.resolve_device(cfg.device)
    sequences, labels = base.collect_sequences(cfg)
    x, y, mask = base.build_tensors(sequences, labels, device)
    training_rows: List[base.TrainingRow] = []
    models: Dict[str, base.ControllerNet] = {}
    for architecture in ("frame_mlp", "gru"):
        model, row = base.train_model(architecture, x, y, mask, cfg, device)
        models[architecture] = model
        training_rows.append(row)
    selected, selection_rows = select_router(cfg, models["gru"], device)
    eval_rows: List[base.EvalRow] = []
    trace = Trace(seed=cfg.trace_seed, condition=f"return_selected_gru:{selected.name}:none")
    for seed in cfg.eval_seeds:
        for controller, model, router in (
            ("designed", None, ROUTERS[0]),
            ("reactive", None, ROUTERS[0]),
            ("frame_mlp", models["frame_mlp"], ROUTERS[0]),
            ("gru", models["gru"], ROUTERS[0]),
            ("return_selected_gru", models["gru"], selected),
        ):
            row, maybe_trace = run_episode(
                seed,
                cfg,
                controller,
                model,
                device,
                router,
                trace=(seed == cfg.trace_seed and controller == "return_selected_gru"),
            )
            eval_rows.append(row)
            if maybe_trace.frames:
                trace = maybe_trace
        for ablation in ("body", "infrastructure", "tools", "social_culture", "environment", "previous_action"):
            row, _ = run_episode(seed, cfg, "return_selected_gru", models["gru"], device, selected, ablation=ablation)
            eval_rows.append(row)
    summary = summarize(eval_rows)
    ablations = ablations_from_summary(summary)
    verdict = verdict_from_summary(summary, ablations, selected)
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
            "device": cfg.device,
            "trace_seed": cfg.trace_seed,
        },
        "routers": [asdict(router) for router in ROUTERS],
        "selection": [asdict(row) for row in selection_rows],
        "training": [asdict(row) for row in training_rows],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": asdict(trace),
        "notes": {
            "claim": "return-selected pressure-router precursor for learned multi-day maturation control",
            "not_claimed": "deep reinforcement learning, subjective consciousness, or open-ended civilization",
        },
    }
    prefix = ARTIFACT_DIR / "ssrm_3d_return_selected_multiday_maturation"
    rows_to_csv(Path(f"{prefix}_training.csv"), training_rows)
    rows_to_csv(Path(f"{prefix}_selection.csv"), selection_rows)
    rows_to_csv(Path(f"{prefix}_eval.csv"), eval_rows)
    rows_to_csv(Path(f"{prefix}_summary.csv"), summary)
    rows_to_csv(Path(f"{prefix}_ablations.csv"), ablations)
    rows_to_csv(Path(f"{prefix}_verdict.csv"), [verdict])
    write_json(Path(f"{prefix}_results.json"), payload)
    write_json(Path(f"{prefix}_trace.json"), asdict(trace))
    write_js(Path(f"{prefix}_results.js"), "SSRM_3D_RETURN_SELECTED_MULTIDAY_MATURATION_RESULTS", payload)
    write_js(Path(f"{prefix}_trace.js"), "SSRM_3D_RETURN_SELECTED_MULTIDAY_MATURATION_TRACE", asdict(trace))
    return payload


def parse_ints(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-seeds", default="20260911,20260912,20260913,20260914,20260915,20260916")
    parser.add_argument("--tune-seeds", default="20260931,20260932,20260933")
    parser.add_argument("--eval-seeds", default="20260941,20260942,20260943,20260944,20260945")
    parser.add_argument("--hours", type=float, default=72.0)
    parser.add_argument("--step-hours", type=float, default=0.10)
    parser.add_argument("--population", type=int, default=14)
    parser.add_argument("--epochs", type=int, default=42)
    parser.add_argument("--hidden-size", type=int, default=64)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--trace-seed", type=int, default=20260941)
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
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({"selection": payload["selection"], "verdict": payload["verdict"], "summary": payload["summary"]}, indent=2))
    return 0 if payload["verdict"]["supports_return_selection"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
