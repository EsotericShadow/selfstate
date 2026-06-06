#!/usr/bin/env python3
"""Return-selected option-gated hidden-regime controller for SSRM-3D.

Report 96 improved the learned hidden-regime controller with an option head,
but the result was still partial. This experiment adds one more serious step:
closed-loop validation return is used to select the option-action bias before
held-out evaluation.

This is not deep RL. The neural controller is still trained from designed
traces. The policy-selection step is return-shaped because it chooses the
closed-loop action-bias setting by validation performance in the simulation.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import statistics
import sys
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import torch


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
REPORT96_PATH = ROOT / "experiments" / "ssrm_3d_option_gated_hidden_regime_controller.py"


def load_report96_module():
    spec = importlib.util.spec_from_file_location("ssrm_option_gated", REPORT96_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {REPORT96_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


p96 = load_report96_module()
p95 = p96.p95


@dataclass(frozen=True)
class Config:
    train_seeds: Sequence[int]
    tune_seeds: Sequence[int]
    eval_seeds: Sequence[int]
    bias_candidates: Sequence[float]
    hours: float = 16.0
    step_hours: float = 0.08
    population: int = 10
    epochs: int = 100
    hidden_size: int = 56
    learning_rate: float = 0.004
    option_loss_weight: float = 0.62
    device: str = "auto"
    trace_seed: int = 20260813


@dataclass(frozen=True)
class TrainingRow:
    architecture: str
    train_loss: float
    action_accuracy: float
    option_accuracy: float
    device_used: str
    parameter_count: int


@dataclass(frozen=True)
class BiasSelectionRow:
    option_bias: float
    mean_score: float
    mean_response_score: float
    mean_targeted_response_rate: float
    selection_objective: float
    selected: bool


@dataclass(frozen=True)
class AblationRow:
    architecture: str
    ablation: str
    mean_score: float
    score_loss: float
    mean_response_score: float
    response_loss: float
    mean_inference_score: float
    inference_loss: float


@dataclass(frozen=True)
class VerdictRow:
    selected_option_bias: float
    return_selected_score: float
    fixed_bias_score: float
    option_frame_score: float
    reactive_score: float
    gain_over_fixed_bias: float
    gain_over_frame: float
    gain_over_reactive: float
    regime_signal_ablation_loss: float
    infrastructure_ablation_loss: float
    social_culture_ablation_loss: float
    body_ablation_loss: float
    response_score: float
    targeted_response_rate: float
    shock_gate_pass_rate: float
    hidden_regime_rate: float
    supports_return_selection: bool
    supports_ablation_specificity: bool
    verdict: str


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def parse_seed_list(raw: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in raw.split(",") if part.strip())


def parse_float_list(raw: str) -> Tuple[float, ...]:
    return tuple(float(part.strip()) for part in raw.split(",") if part.strip())


def to_p96_config(cfg: Config, option_bias: float) -> object:
    return p96.Config(
        train_seeds=cfg.train_seeds,
        eval_seeds=cfg.eval_seeds,
        hours=cfg.hours,
        step_hours=cfg.step_hours,
        population=cfg.population,
        epochs=cfg.epochs,
        hidden_size=cfg.hidden_size,
        learning_rate=cfg.learning_rate,
        option_loss_weight=cfg.option_loss_weight,
        option_bias=option_bias,
        device=cfg.device,
        trace_seed=cfg.trace_seed,
    )


def train_models(cfg: Config):
    device = p96.resolve_device(cfg.device)
    p95_cfg = p95.Config(
        train_seeds=cfg.train_seeds,
        eval_seeds=cfg.eval_seeds,
        hours=cfg.hours,
        step_hours=cfg.step_hours,
        population=cfg.population,
        epochs=cfg.epochs,
        hidden_size=cfg.hidden_size,
        learning_rate=cfg.learning_rate,
        device=cfg.device,
        trace_seed=cfg.trace_seed,
    )
    train_x_raw, train_y = p95.generate_teacher_sequences(p95_cfg)
    option_y, sample_weights = p96.derive_option_targets(train_x_raw, train_y)
    train_x, feature_mean, feature_std = p96.standardize(train_x_raw)
    models = {}
    training_rows: List[TrainingRow] = []
    for architecture in ("option_frame", "option_gru"):
        model, row = p96.train_option_controller(
            architecture,
            train_x,
            train_y,
            option_y,
            sample_weights,
            to_p96_config(cfg, option_bias=1.35),
            device,
        )
        models[architecture] = model
        training_rows.append(TrainingRow(**asdict(row)))
    return device, feature_mean, feature_std, models, training_rows


def selection_objective(rows: Sequence[object]) -> Tuple[float, float, float, float]:
    score = mean(row.long_horizon_score for row in rows)
    response = mean(row.response_score for row in rows)
    targeted = mean(row.targeted_response_rate for row in rows)
    objective = score + response * 0.12 + targeted * 0.08
    return score, response, targeted, objective


def select_option_bias(cfg: Config, model, device, feature_mean: torch.Tensor, feature_std: torch.Tensor) -> Tuple[float, List[BiasSelectionRow]]:
    rows: List[BiasSelectionRow] = []
    best_bias = cfg.bias_candidates[0]
    best_objective = -1.0
    for option_bias in cfg.bias_candidates:
        eval_rows = []
        bias_cfg = to_p96_config(cfg, option_bias)
        for seed in cfg.tune_seeds:
            row, _trace = p96.run_option_episode(
                seed,
                "return_selected_option_gru",
                model,
                device,
                feature_mean,
                feature_std,
                bias_cfg,
            )
            eval_rows.append(row)
        score, response, targeted, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_bias = option_bias
            best_objective = objective
        rows.append(
            BiasSelectionRow(
                option_bias=option_bias,
                mean_score=score,
                mean_response_score=response,
                mean_targeted_response_rate=targeted,
                selection_objective=objective,
                selected=False,
            )
        )
    return best_bias, [
        BiasSelectionRow(
            option_bias=row.option_bias,
            mean_score=row.mean_score,
            mean_response_score=row.mean_response_score,
            mean_targeted_response_rate=row.mean_targeted_response_rate,
            selection_objective=row.selection_objective,
            selected=row.option_bias == best_bias,
        )
        for row in rows
    ]


def summarize(rows: Sequence[object]):
    return p95.summarize(rows)


def row_lookup(summary: Sequence[object], architecture: str, condition: str):
    return p95.row_lookup(summary, architecture, condition)


def make_ablations(summary: Sequence[object]) -> List[AblationRow]:
    full = row_lookup(summary, "return_selected_option_gru", "none")
    rows: List[AblationRow] = []
    for ablation in ("regime_signal", "infrastructure", "social_culture", "body"):
        row = row_lookup(summary, "return_selected_option_gru", ablation)
        rows.append(
            AblationRow(
                architecture="return_selected_option_gru",
                ablation=ablation,
                mean_score=row.mean_long_horizon_score,
                score_loss=full.mean_long_horizon_score - row.mean_long_horizon_score,
                mean_response_score=row.mean_response_score,
                response_loss=full.mean_response_score - row.mean_response_score,
                mean_inference_score=row.mean_inference_score,
                inference_loss=full.mean_inference_score - row.mean_inference_score,
            )
        )
    return rows


def verdict_from_summary(summary: Sequence[object], ablations: Sequence[AblationRow], selected_bias: float) -> VerdictRow:
    selected = row_lookup(summary, "return_selected_option_gru", "none")
    fixed = row_lookup(summary, "fixed_option_gru", "none")
    frame = row_lookup(summary, "option_frame", "none")
    reactive = row_lookup(summary, "scripted", "reactive_survival_only")
    by_ablation = {row.ablation: row for row in ablations}
    gain_over_fixed = selected.mean_long_horizon_score - fixed.mean_long_horizon_score
    supports_return = (
        selected.no_major_regime_before_12h_rate == 1.0
        and selected.hidden_regime_after_12h_rate == 1.0
        and selected.mean_alive_at_12h >= 8.0
        and selected.mean_final_alive >= 7.0
        and selected.mean_long_horizon_score >= 0.60
        and selected.mean_response_score >= 0.54
        and selected.mean_long_horizon_score - reactive.mean_long_horizon_score >= 0.12
    )
    supports_ablation = (
        by_ablation["regime_signal"].response_loss >= 0.025
        and by_ablation["infrastructure"].score_loss >= 0.050
        and by_ablation["body"].response_loss >= 0.025
    )
    if supports_return and supports_ablation and gain_over_fixed >= 0.010:
        verdict = "pass"
    elif supports_return:
        verdict = "partial"
    else:
        verdict = "failed"
    return VerdictRow(
        selected_option_bias=selected_bias,
        return_selected_score=selected.mean_long_horizon_score,
        fixed_bias_score=fixed.mean_long_horizon_score,
        option_frame_score=frame.mean_long_horizon_score,
        reactive_score=reactive.mean_long_horizon_score,
        gain_over_fixed_bias=gain_over_fixed,
        gain_over_frame=selected.mean_long_horizon_score - frame.mean_long_horizon_score,
        gain_over_reactive=selected.mean_long_horizon_score - reactive.mean_long_horizon_score,
        regime_signal_ablation_loss=by_ablation["regime_signal"].score_loss,
        infrastructure_ablation_loss=by_ablation["infrastructure"].score_loss,
        social_culture_ablation_loss=by_ablation["social_culture"].score_loss,
        body_ablation_loss=by_ablation["body"].score_loss,
        response_score=selected.mean_response_score,
        targeted_response_rate=selected.mean_targeted_response_rate,
        shock_gate_pass_rate=selected.no_major_regime_before_12h_rate,
        hidden_regime_rate=selected.hidden_regime_after_12h_rate,
        supports_return_selection=supports_return,
        supports_ablation_specificity=supports_ablation,
        verdict=verdict,
    )


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    p95.rows_to_csv(path, rows)


def write_json(path: Path, payload: object) -> None:
    p95.write_json(path, payload)


def write_js(path: Path, variable: str, payload: object) -> None:
    p95.write_js(path, variable, payload)


def run_benchmark(cfg: Config) -> Dict[str, object]:
    device, feature_mean, feature_std, models, training_rows = train_models(cfg)
    selected_bias, bias_rows = select_option_bias(cfg, models["option_gru"], device, feature_mean, feature_std)
    selected_cfg = to_p96_config(cfg, selected_bias)
    fixed_cfg = to_p96_config(cfg, 1.35)

    eval_rows = []
    trace = []
    for seed in cfg.eval_seeds:
        eval_rows.append(p95.run_scripted_episode(seed, fixed_cfg, p95.reactive_condition(), "scripted", "reactive_survival_only"))
        row, maybe_trace = p96.run_option_episode(
            seed,
            "return_selected_option_gru",
            models["option_gru"],
            device,
            feature_mean,
            feature_std,
            selected_cfg,
            trace=(seed == cfg.trace_seed),
        )
        eval_rows.append(row)
        if maybe_trace:
            trace = maybe_trace
        fixed_row, _ = p96.run_option_episode(
            seed,
            "fixed_option_gru",
            models["option_gru"],
            device,
            feature_mean,
            feature_std,
            fixed_cfg,
        )
        eval_rows.append(fixed_row)
        frame_row, _ = p96.run_option_episode(
            seed,
            "option_frame",
            models["option_frame"],
            device,
            feature_mean,
            feature_std,
            selected_cfg,
        )
        eval_rows.append(frame_row)
        for ablation in ("regime_signal", "infrastructure", "social_culture", "body"):
            row, _ = p96.run_option_episode(
                seed,
                "return_selected_option_gru",
                models["option_gru"],
                device,
                feature_mean,
                feature_std,
                selected_cfg,
                ablation=ablation,
            )
            eval_rows.append(row)

    summary = summarize(eval_rows)
    ablations = make_ablations(summary)
    verdict = verdict_from_summary(summary, ablations, selected_bias)
    payload = {
        "config": {
            "train_seeds": list(cfg.train_seeds),
            "tune_seeds": list(cfg.tune_seeds),
            "eval_seeds": list(cfg.eval_seeds),
            "bias_candidates": list(cfg.bias_candidates),
            "hours": cfg.hours,
            "step_hours": cfg.step_hours,
            "population": cfg.population,
            "epochs": cfg.epochs,
            "hidden_size": cfg.hidden_size,
            "learning_rate": cfg.learning_rate,
            "option_loss_weight": cfg.option_loss_weight,
            "device": str(device),
            "trace_seed": cfg.trace_seed,
        },
        "training": [asdict(row) for row in training_rows],
        "bias_selection": [asdict(row) for row in bias_rows],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace,
        "notes": {
            "claim": "return-selected option-bias hidden-regime controller precursor",
            "not_claimed": "subjective consciousness, open-ended civilization, or gradient deep RL",
            "label_discipline": "validation return selects option bias; hidden regime labels are not model inputs",
        },
    }
    prefix = ARTIFACT_DIR / "ssrm_3d_return_selected_hidden_regime_controller"
    rows_to_csv(Path(f"{prefix}_training.csv"), training_rows)
    rows_to_csv(Path(f"{prefix}_bias_selection.csv"), bias_rows)
    rows_to_csv(Path(f"{prefix}_eval.csv"), eval_rows)
    rows_to_csv(Path(f"{prefix}_summary.csv"), summary)
    rows_to_csv(Path(f"{prefix}_ablations.csv"), ablations)
    rows_to_csv(Path(f"{prefix}_verdict.csv"), [verdict])
    write_json(Path(f"{prefix}_results.json"), payload)
    write_json(Path(f"{prefix}_trace.json"), trace)
    write_js(Path(f"{prefix}_results.js"), "SSRM_3D_RETURN_SELECTED_HIDDEN_REGIME_CONTROLLER_RESULTS", payload)
    write_js(Path(f"{prefix}_trace.js"), "SSRM_3D_RETURN_SELECTED_HIDDEN_REGIME_CONTROLLER_TRACE", trace)
    return payload


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-seeds", default="20260718,20260719,20260720,20260721,20260722,20260723,20260724,20260725")
    parser.add_argument("--tune-seeds", default="20260808,20260809,20260810,20260811,20260812")
    parser.add_argument("--eval-seeds", default="20260813,20260814,20260815,20260816,20260817")
    parser.add_argument("--bias-candidates", default="0.70,1.00,1.35,1.70,2.10")
    parser.add_argument("--hours", type=float, default=16.0)
    parser.add_argument("--step-hours", type=float, default=0.08)
    parser.add_argument("--population", type=int, default=10)
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--hidden-size", type=int, default=56)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--option-loss-weight", type=float, default=0.62)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--trace-seed", type=int, default=20260813)
    args = parser.parse_args()
    return Config(
        train_seeds=parse_seed_list(args.train_seeds),
        tune_seeds=parse_seed_list(args.tune_seeds),
        eval_seeds=parse_seed_list(args.eval_seeds),
        bias_candidates=parse_float_list(args.bias_candidates),
        hours=args.hours,
        step_hours=args.step_hours,
        population=args.population,
        epochs=args.epochs,
        hidden_size=args.hidden_size,
        learning_rate=args.learning_rate,
        option_loss_weight=args.option_loss_weight,
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({"bias_selection": payload["bias_selection"], "verdict": payload["verdict"], "summary": payload["summary"]}, indent=2))
    return 0 if payload["verdict"]["verdict"] in {"pass", "partial"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
