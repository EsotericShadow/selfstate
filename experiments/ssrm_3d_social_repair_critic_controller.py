#!/usr/bin/env python3
"""Social repair critic controller for SSRM-3D.

Report 99 showed a specific failure: the learned controller responded to hidden
social shocks, but often spent the recovery window on the wrong repair class.
This follow-up keeps the same hidden-variant, no-label world and adds a learned
repair critic that scores inspect/teach/mediate actions from observation traces.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import statistics
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import torch
from torch import nn


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
REPORT99_PATH = ROOT / "experiments" / "ssrm_3d_social_credit_assignment_controller.py"


def load_report99_module():
    spec = importlib.util.spec_from_file_location("ssrm_social_credit_99", REPORT99_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {REPORT99_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


r99 = load_report99_module()
p96 = r99.p96
p95 = r99.p95

ACTIONS = r99.ACTIONS
ACTION_TO_INDEX = r99.ACTION_TO_INDEX
INDEX_TO_ACTION = r99.INDEX_TO_ACTION
REPAIR_CLASSES = ("none", "inspect", "teach", "mediate")
REPAIR_TO_INDEX = {name: index for index, name in enumerate(REPAIR_CLASSES)}
REPAIR_ACTIONS = ("inspect", "teach", "mediate")


@dataclass(frozen=True)
class Config:
    train_seeds: Sequence[int]
    tune_seeds: Sequence[int]
    eval_seeds: Sequence[int]
    base_bias_candidates: Sequence[float]
    repair_bias_candidates: Sequence[float]
    hours: float = 16.0
    step_hours: float = 0.08
    population: int = 10
    epochs: int = 110
    hidden_size: int = 64
    learning_rate: float = 0.004
    option_loss_weight: float = 0.62
    repair_epochs: int = 80
    repair_hidden_size: int = 40
    repair_learning_rate: float = 0.003
    device: str = "auto"
    trace_seed: int = 20260853


@dataclass(frozen=True)
class RepairTrainingRow:
    architecture: str
    train_loss: float
    repair_accuracy: float
    active_repair_accuracy: float
    non_none_repair_accuracy: float
    device_used: str
    parameter_count: int


@dataclass(frozen=True)
class RepairBiasSelectionRow:
    repair_bias: float
    mean_score: float
    mean_credit_response_score: float
    mean_targeted_repair_rate: float
    mean_wrong_repair_rate: float
    mean_opportunity_score: float
    selection_objective: float
    selected: bool


@dataclass(frozen=True)
class VerdictRow:
    selected_base_option_bias: float
    selected_repair_bias: float
    repair_critic_score: float
    report99_baseline_score: float
    fixed_bias_score: float
    option_frame_score: float
    reactive_score: float
    gain_over_report99_baseline: float
    gain_over_fixed_bias: float
    gain_over_frame: float
    gain_over_reactive: float
    social_culture_ablation_loss: float
    social_culture_response_loss: float
    social_culture_targeted_loss: float
    social_culture_opportunity_loss: float
    regime_signal_response_loss: float
    memory_ablation_loss: float
    credit_response_score: float
    targeted_repair_rate: float
    wrong_repair_rate: float
    opportunity_score: float
    shock_gate_pass_rate: float
    hidden_regime_rate: float
    supports_repair_critic_controller: bool
    supports_social_culture_ablation: bool
    verdict: str


class RepairCriticNet(nn.Module):
    def __init__(self, input_size: int, hidden_size: int) -> None:
        super().__init__()
        self.recurrent = nn.GRU(input_size, hidden_size, batch_first=True)
        self.head = nn.Linear(hidden_size, len(REPAIR_CLASSES))

    def forward(self, x: torch.Tensor, state: torch.Tensor | None = None) -> Tuple[torch.Tensor, torch.Tensor | None]:
        hidden, next_state = self.recurrent(x, state)
        return self.head(hidden), next_state

    def step(self, x: torch.Tensor, state: torch.Tensor | None = None) -> Tuple[torch.Tensor, torch.Tensor | None]:
        logits, next_state = self.forward(x.unsqueeze(1), state)
        return logits[:, -1, :], next_state


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def parse_seed_list(raw: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in raw.split(",") if part.strip())


def parse_float_list(raw: str) -> Tuple[float, ...]:
    return tuple(float(part.strip()) for part in raw.split(",") if part.strip())


def to_r99_config(cfg: Config) -> object:
    return r99.Config(
        train_seeds=cfg.train_seeds,
        tune_seeds=cfg.tune_seeds,
        eval_seeds=cfg.eval_seeds,
        bias_candidates=cfg.base_bias_candidates,
        hours=cfg.hours,
        step_hours=cfg.step_hours,
        population=cfg.population,
        epochs=cfg.epochs,
        hidden_size=cfg.hidden_size,
        learning_rate=cfg.learning_rate,
        option_loss_weight=cfg.option_loss_weight,
        device=cfg.device,
        trace_seed=cfg.trace_seed,
    )


def repair_target_for_sample(features: Sequence[float], action_index: int) -> int:
    social_signal = float(features[40])
    action = INDEX_TO_ACTION[int(action_index)]
    if social_signal >= 0.12 and action in REPAIR_ACTIONS:
        return REPAIR_TO_INDEX[action]
    return REPAIR_TO_INDEX["none"]


def derive_repair_targets(train_x_raw: torch.Tensor, train_y: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
    repair_y = torch.zeros(train_y.shape, dtype=torch.long)
    weights = torch.full(train_y.shape, 0.20, dtype=torch.float32)
    for seq in range(train_y.shape[0]):
        for step in range(train_y.shape[1]):
            features = train_x_raw[seq, step].tolist()
            action_index = int(train_y[seq, step].item())
            target = repair_target_for_sample(features, action_index)
            social_signal = float(features[40])
            repair_y[seq, step] = target
            weights[seq, step] = 0.20 + social_signal * 3.5
            if target != REPAIR_TO_INDEX["none"]:
                weights[seq, step] *= 5.0
            elif social_signal >= 0.12:
                weights[seq, step] *= 1.8
    return repair_y, weights


def train_repair_critic(
    cfg: Config,
    train_x_raw: torch.Tensor,
    train_x: torch.Tensor,
    train_y: torch.Tensor,
    device: torch.device,
) -> Tuple[RepairCriticNet, RepairTrainingRow]:
    torch.manual_seed(20260901)
    repair_y, weights = derive_repair_targets(train_x_raw, train_y)
    model = RepairCriticNet(train_x.shape[-1], cfg.repair_hidden_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.repair_learning_rate)
    x = train_x.to(device)
    targets = repair_y.to(device)
    sample_weights = weights.to(device)
    loss_fn = nn.CrossEntropyLoss(reduction="none")
    last_loss = 0.0
    for _ in range(cfg.repair_epochs):
        optimizer.zero_grad(set_to_none=True)
        logits, _ = model(x)
        loss = loss_fn(logits.reshape(-1, logits.shape[-1]), targets.reshape(-1)).reshape_as(targets)
        weighted = (loss * sample_weights).sum() / sample_weights.sum().clamp_min(1.0)
        weighted.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 2.0)
        optimizer.step()
        last_loss = float(weighted.detach().cpu().item())
    model.eval()
    with torch.no_grad():
        logits, _ = model(x)
        predicted = logits.argmax(dim=-1)
        accuracy = float((predicted == targets).float().mean().detach().cpu().item())
        active_mask = train_x_raw[:, :, 40].to(device) >= 0.12
        active_accuracy = float((predicted[active_mask] == targets[active_mask]).float().mean().detach().cpu().item()) if bool(active_mask.any()) else 0.0
        repair_mask = targets != REPAIR_TO_INDEX["none"]
        repair_accuracy = float((predicted[repair_mask] == targets[repair_mask]).float().mean().detach().cpu().item()) if bool(repair_mask.any()) else 0.0
    return model, RepairTrainingRow(
        architecture="repair_gru",
        train_loss=last_loss,
        repair_accuracy=accuracy,
        active_repair_accuracy=active_accuracy,
        non_none_repair_accuracy=repair_accuracy,
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in model.parameters()),
    )


def repair_action_bias(repair_logits: torch.Tensor, raw_features: Sequence[float], repair_bias: float) -> torch.Tensor:
    social_gate = r99.clamp((float(raw_features[40]) - 0.08) * 3.2)
    probabilities = torch.softmax(repair_logits, dim=-1)
    bias = torch.zeros((repair_logits.shape[0], len(ACTIONS)), dtype=repair_logits.dtype, device=repair_logits.device)
    for repair_action in REPAIR_ACTIONS:
        class_index = REPAIR_TO_INDEX[repair_action]
        action_index = ACTION_TO_INDEX[repair_action]
        bias[:, action_index] += probabilities[:, class_index] * repair_bias * social_gate
    return bias


def choose_repair_critic_action(
    base_model,
    repair_model,
    device: torch.device,
    feature_mean: torch.Tensor,
    feature_std: torch.Tensor,
    agent,
    world,
    signals,
    previous_action: int,
    state,
    cfg: Config,
    base_option_bias: float,
    repair_bias: float,
    ablation: str,
):
    base_state = None
    repair_state = None
    if isinstance(state, tuple):
        base_state, repair_state = state
    raw = r99.apply_feature_ablation(p95.observation(agent, world, signals, previous_action), ablation)
    x = torch.tensor(raw, dtype=torch.float32).unsqueeze(0)
    x = (x - feature_mean) / feature_std
    x = x.to(device)
    with torch.no_grad():
        action_logits, option_logits, next_base_state = base_model.step(x, base_state)
        repair_logits, next_repair_state = repair_model.step(x, repair_state)
    scores = (
        action_logits
        + p96.option_action_bias(option_logits, r99.to_p96_config(to_r99_config(cfg), base_option_bias))
        + repair_action_bias(repair_logits, raw, repair_bias)
    )
    action_index = int(scores.argmax(dim=-1).item())
    repair_index = int(repair_logits.argmax(dim=-1).item())
    return INDEX_TO_ACTION[action_index], action_index, REPAIR_CLASSES[repair_index], (next_base_state, next_repair_state)


def run_repair_critic_episode(
    seed: int,
    architecture: str,
    base_model,
    repair_model,
    device: torch.device,
    feature_mean: torch.Tensor,
    feature_std: torch.Tensor,
    cfg: Config,
    base_option_bias: float,
    repair_bias: float,
    *,
    ablation: str = "none",
    trace: bool = False,
):
    def actor(agent, world, signals, previous_action, state, rng):
        return choose_repair_critic_action(
            base_model,
            repair_model,
            device,
            feature_mean,
            feature_std,
            agent,
            world,
            signals,
            previous_action,
            state,
            cfg,
            base_option_bias,
            repair_bias,
            ablation,
        )

    return r99.run_world_loop(seed, to_r99_config(cfg), actor, r99.teacher_condition(), architecture, ablation, trace=trace)


def selection_objective(rows: Sequence[object]) -> Tuple[float, float, float, float, float, float]:
    score = mean(row.long_horizon_score for row in rows)
    response = mean(row.credit_response_score for row in rows)
    targeted = mean(row.targeted_repair_rate for row in rows)
    wrong = mean(row.wrong_repair_rate for row in rows)
    opportunity = mean(row.opportunity_score for row in rows)
    objective = score + response * 0.14 + targeted * 0.34 + opportunity * 0.10 - wrong * 0.16
    return score, response, targeted, wrong, opportunity, objective


def select_repair_bias(
    cfg: Config,
    base_model,
    repair_model,
    device: torch.device,
    feature_mean: torch.Tensor,
    feature_std: torch.Tensor,
    base_option_bias: float,
) -> Tuple[float, List[RepairBiasSelectionRow]]:
    best_bias = cfg.repair_bias_candidates[0]
    best_objective = -1e9
    rows: List[RepairBiasSelectionRow] = []
    for repair_bias in cfg.repair_bias_candidates:
        eval_rows = [
            run_repair_critic_episode(seed, "repair_critic_gru", base_model, repair_model, device, feature_mean, feature_std, cfg, base_option_bias, repair_bias)[0]
            for seed in cfg.tune_seeds
        ]
        score, response, targeted, wrong, opportunity, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_bias = repair_bias
            best_objective = objective
        rows.append(RepairBiasSelectionRow(repair_bias, score, response, targeted, wrong, opportunity, objective, False))
    return best_bias, [
        RepairBiasSelectionRow(
            row.repair_bias,
            row.mean_score,
            row.mean_credit_response_score,
            row.mean_targeted_repair_rate,
            row.mean_wrong_repair_rate,
            row.mean_opportunity_score,
            row.selection_objective,
            row.repair_bias == best_bias,
        )
        for row in rows
    ]


def row_lookup(summary: Sequence[object], architecture: str, condition: str):
    for row in summary:
        if row.architecture == architecture and row.condition == condition:
            return row
    raise KeyError((architecture, condition))


def make_repair_ablations(summary: Sequence[object]) -> List[object]:
    full = row_lookup(summary, "repair_critic_gru", "none")
    rows = []
    for ablation in ("regime_signal", "social_culture", "memory", "body"):
        row = row_lookup(summary, "repair_critic_gru", ablation)
        rows.append(
            r99.AblationRow(
                architecture="repair_critic_gru",
                ablation=ablation,
                mean_score=row.mean_long_horizon_score,
                score_loss=full.mean_long_horizon_score - row.mean_long_horizon_score,
                mean_credit_response_score=row.mean_credit_response_score,
                credit_response_loss=full.mean_credit_response_score - row.mean_credit_response_score,
                mean_targeted_repair_rate=row.mean_targeted_repair_rate,
                targeted_repair_loss=full.mean_targeted_repair_rate - row.mean_targeted_repair_rate,
                mean_opportunity_score=row.mean_opportunity_score,
                opportunity_loss=full.mean_opportunity_score - row.mean_opportunity_score,
                mean_culture_score=row.mean_culture_score,
                culture_loss=full.mean_culture_score - row.mean_culture_score,
            )
        )
    return rows


def verdict_from_summary(summary: Sequence[object], ablations: Sequence[object], base_bias: float, repair_bias: float) -> VerdictRow:
    selected = row_lookup(summary, "repair_critic_gru", "none")
    baseline = row_lookup(summary, "report99_credit_gru", "none")
    fixed = row_lookup(summary, "fixed_credit_gru", "none")
    frame = row_lookup(summary, "credit_frame", "none")
    reactive = row_lookup(summary, "scripted", "reactive_survival_only")
    by_ablation = {row.ablation: row for row in ablations}
    supports_controller = (
        selected.no_major_regime_before_12h_rate == 1.0
        and selected.hidden_regime_after_12h_rate == 1.0
        and selected.mean_alive_at_12h >= 8.0
        and selected.mean_final_alive >= 7.0
        and selected.mean_long_horizon_score >= 0.58
        and selected.mean_credit_response_score >= 0.58
        and selected.mean_targeted_repair_rate >= 0.42
        and selected.mean_wrong_repair_rate <= 0.58
        and selected.mean_long_horizon_score - baseline.mean_long_horizon_score >= 0.015
    )
    supports_ablation = (
        by_ablation["social_culture"].score_loss >= 0.020
        and by_ablation["social_culture"].credit_response_loss >= 0.020
        and by_ablation["social_culture"].targeted_repair_loss >= 0.050
    )
    verdict = "pass" if supports_controller and supports_ablation else "partial" if supports_controller else "failed"
    return VerdictRow(
        selected_base_option_bias=base_bias,
        selected_repair_bias=repair_bias,
        repair_critic_score=selected.mean_long_horizon_score,
        report99_baseline_score=baseline.mean_long_horizon_score,
        fixed_bias_score=fixed.mean_long_horizon_score,
        option_frame_score=frame.mean_long_horizon_score,
        reactive_score=reactive.mean_long_horizon_score,
        gain_over_report99_baseline=selected.mean_long_horizon_score - baseline.mean_long_horizon_score,
        gain_over_fixed_bias=selected.mean_long_horizon_score - fixed.mean_long_horizon_score,
        gain_over_frame=selected.mean_long_horizon_score - frame.mean_long_horizon_score,
        gain_over_reactive=selected.mean_long_horizon_score - reactive.mean_long_horizon_score,
        social_culture_ablation_loss=by_ablation["social_culture"].score_loss,
        social_culture_response_loss=by_ablation["social_culture"].credit_response_loss,
        social_culture_targeted_loss=by_ablation["social_culture"].targeted_repair_loss,
        social_culture_opportunity_loss=by_ablation["social_culture"].opportunity_loss,
        regime_signal_response_loss=by_ablation["regime_signal"].credit_response_loss,
        memory_ablation_loss=by_ablation["memory"].score_loss,
        credit_response_score=selected.mean_credit_response_score,
        targeted_repair_rate=selected.mean_targeted_repair_rate,
        wrong_repair_rate=selected.mean_wrong_repair_rate,
        opportunity_score=selected.mean_opportunity_score,
        shock_gate_pass_rate=selected.no_major_regime_before_12h_rate,
        hidden_regime_rate=selected.hidden_regime_after_12h_rate,
        supports_repair_critic_controller=supports_controller,
        supports_social_culture_ablation=supports_ablation,
        verdict=verdict,
    )


def train_all(cfg: Config):
    r99_cfg = to_r99_config(cfg)
    device = p96.resolve_device(cfg.device)
    train_x_raw, train_y = r99.generate_teacher_sequences(r99_cfg)
    option_y, sample_weights = p96.derive_option_targets(train_x_raw, train_y)
    sample_weights = r99.boost_credit_sample_weights(train_x_raw, train_y, sample_weights)
    train_x, feature_mean, feature_std = p96.standardize(train_x_raw)
    models = {}
    training_rows = []
    for architecture in ("option_frame", "option_gru"):
        model, row = p96.train_option_controller(
            architecture,
            train_x,
            train_y,
            option_y,
            sample_weights,
            r99.to_p96_config(r99_cfg, option_bias=1.0),
            device,
        )
        models[architecture] = model
        training_rows.append(row)
    repair_model, repair_training = train_repair_critic(cfg, train_x_raw, train_x, train_y, device)
    return device, feature_mean, feature_std, models, repair_model, training_rows, repair_training


def run_benchmark(cfg: Config) -> Dict[str, object]:
    r99_cfg = to_r99_config(cfg)
    device, feature_mean, feature_std, models, repair_model, base_training_rows, repair_training = train_all(cfg)
    selected_base_bias, base_bias_rows = r99.select_option_bias(r99_cfg, models["option_gru"], device, feature_mean, feature_std)
    selected_repair_bias, repair_bias_rows = select_repair_bias(
        cfg,
        models["option_gru"],
        repair_model,
        device,
        feature_mean,
        feature_std,
        selected_base_bias,
    )
    eval_rows = []
    trace = []
    for seed in cfg.eval_seeds:
        eval_rows.append(r99.run_reactive_episode(seed, r99_cfg))
        repair_row, maybe_trace = run_repair_critic_episode(
            seed,
            "repair_critic_gru",
            models["option_gru"],
            repair_model,
            device,
            feature_mean,
            feature_std,
            cfg,
            selected_base_bias,
            selected_repair_bias,
            trace=(seed == cfg.trace_seed),
        )
        eval_rows.append(repair_row)
        if maybe_trace:
            trace = maybe_trace
        baseline_row, _ = r99.run_model_episode(seed, "report99_credit_gru", models["option_gru"], device, feature_mean, feature_std, r99_cfg, selected_base_bias)
        eval_rows.append(baseline_row)
        fixed_row, _ = r99.run_model_episode(seed, "fixed_credit_gru", models["option_gru"], device, feature_mean, feature_std, r99_cfg, 1.35)
        eval_rows.append(fixed_row)
        frame_row, _ = r99.run_model_episode(seed, "credit_frame", models["option_frame"], device, feature_mean, feature_std, r99_cfg, selected_base_bias)
        eval_rows.append(frame_row)
        for ablation in ("regime_signal", "social_culture", "memory", "body"):
            row, _ = run_repair_critic_episode(
                seed,
                "repair_critic_gru",
                models["option_gru"],
                repair_model,
                device,
                feature_mean,
                feature_std,
                cfg,
                selected_base_bias,
                selected_repair_bias,
                ablation=ablation,
            )
            eval_rows.append(row)

    summary = r99.summarize(eval_rows)
    variant_summary = r99.summarize_variants(eval_rows)
    ablations = make_repair_ablations(summary)
    verdict = verdict_from_summary(summary, ablations, selected_base_bias, selected_repair_bias)
    payload = {
        "config": {
            "train_seeds": list(cfg.train_seeds),
            "tune_seeds": list(cfg.tune_seeds),
            "eval_seeds": list(cfg.eval_seeds),
            "base_bias_candidates": list(cfg.base_bias_candidates),
            "repair_bias_candidates": list(cfg.repair_bias_candidates),
            "credit_variants": list(r99.CREDIT_VARIANTS),
            "repair_classes": list(REPAIR_CLASSES),
            "hours": cfg.hours,
            "step_hours": cfg.step_hours,
            "population": cfg.population,
            "epochs": cfg.epochs,
            "hidden_size": cfg.hidden_size,
            "repair_epochs": cfg.repair_epochs,
            "repair_hidden_size": cfg.repair_hidden_size,
            "device": str(device),
            "trace_seed": cfg.trace_seed,
        },
        "base_training": [asdict(row) for row in base_training_rows],
        "repair_training": asdict(repair_training),
        "base_bias_selection": [asdict(row) for row in base_bias_rows],
        "repair_bias_selection": [asdict(row) for row in repair_bias_rows],
        "eval": [asdict(row) for row in eval_rows],
        "summary": [asdict(row) for row in summary],
        "variant_summary": [asdict(row) for row in variant_summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace,
        "notes": {
            "claim": "social repair critic controller precursor",
            "not_claimed": "subjective consciousness, open-ended civilization, or full deep reinforcement learning",
            "label_discipline": "repair critic sees observations, not credit variant labels",
            "purpose": "tests whether a learned repair critic improves the Report 99 wrong-repair failure under opportunity cost",
        },
    }
    prefix = ARTIFACT_DIR / "ssrm_3d_social_repair_critic_controller"
    r99.rows_to_csv(Path(f"{prefix}_base_training.csv"), base_training_rows)
    r99.rows_to_csv(Path(f"{prefix}_repair_training.csv"), [repair_training])
    r99.rows_to_csv(Path(f"{prefix}_base_bias_selection.csv"), base_bias_rows)
    r99.rows_to_csv(Path(f"{prefix}_repair_bias_selection.csv"), repair_bias_rows)
    r99.rows_to_csv(Path(f"{prefix}_eval.csv"), eval_rows)
    r99.rows_to_csv(Path(f"{prefix}_summary.csv"), summary)
    r99.rows_to_csv(Path(f"{prefix}_variant_summary.csv"), variant_summary)
    r99.rows_to_csv(Path(f"{prefix}_ablations.csv"), ablations)
    r99.rows_to_csv(Path(f"{prefix}_verdict.csv"), [verdict])
    r99.write_json(Path(f"{prefix}_results.json"), payload)
    r99.write_json(Path(f"{prefix}_trace.json"), trace)
    r99.write_js(Path(f"{prefix}_results.js"), "SSRM_3D_SOCIAL_REPAIR_CRITIC_CONTROLLER_RESULTS", payload)
    r99.write_js(Path(f"{prefix}_trace.js"), "SSRM_3D_SOCIAL_REPAIR_CRITIC_CONTROLLER_TRACE", trace)
    return payload


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-seeds", default="20260838,20260839,20260840,20260841,20260842,20260843,20260844,20260845")
    parser.add_argument("--tune-seeds", default="20260848,20260849,20260850,20260851,20260852")
    parser.add_argument("--eval-seeds", default="20260853,20260854,20260855,20260856,20260857")
    parser.add_argument("--base-bias-candidates", default="0.50,0.70,1.00,1.35,1.70")
    parser.add_argument("--repair-bias-candidates", default="0.00,0.75,1.25,1.75,2.50,3.50")
    parser.add_argument("--hours", type=float, default=16.0)
    parser.add_argument("--step-hours", type=float, default=0.08)
    parser.add_argument("--population", type=int, default=10)
    parser.add_argument("--epochs", type=int, default=110)
    parser.add_argument("--hidden-size", type=int, default=64)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--option-loss-weight", type=float, default=0.62)
    parser.add_argument("--repair-epochs", type=int, default=80)
    parser.add_argument("--repair-hidden-size", type=int, default=40)
    parser.add_argument("--repair-learning-rate", type=float, default=0.003)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--trace-seed", type=int, default=20260853)
    args = parser.parse_args()
    return Config(
        train_seeds=parse_seed_list(args.train_seeds),
        tune_seeds=parse_seed_list(args.tune_seeds),
        eval_seeds=parse_seed_list(args.eval_seeds),
        base_bias_candidates=parse_float_list(args.base_bias_candidates),
        repair_bias_candidates=parse_float_list(args.repair_bias_candidates),
        hours=args.hours,
        step_hours=args.step_hours,
        population=args.population,
        epochs=args.epochs,
        hidden_size=args.hidden_size,
        learning_rate=args.learning_rate,
        option_loss_weight=args.option_loss_weight,
        repair_epochs=args.repair_epochs,
        repair_hidden_size=args.repair_hidden_size,
        repair_learning_rate=args.repair_learning_rate,
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({"repair_bias_selection": payload["repair_bias_selection"], "verdict": payload["verdict"], "summary": payload["summary"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
