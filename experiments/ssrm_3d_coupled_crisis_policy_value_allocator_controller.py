#!/usr/bin/env python3
"""Policy/value allocator for SSRM-3D randomized coupled crises.

Report 115 optimized a compact adaptive allocator by direct closed-loop return
search. This benchmark adds a learned value model over candidate allocator
policies: candidate policies are rolled out in the randomized 96h world, their
actual consequences become value labels, and the value model chooses which
additional policies deserve expensive rollout.

This is still not actor-critic RL. The learned environmental/social action
heads and engineered allocation summaries remain. The narrower question is
whether consequence-trained value selection improves allocation beyond a seed
allocator, return-selected control, and fixed-joint coordination.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import torch

import ssrm_3d_coupled_crisis_adaptive_allocator_controller as report115
import ssrm_3d_coupled_crisis_joint_arbitration_controller as report113
import ssrm_3d_coupled_crisis_randomized_transfer_controller as report114
import ssrm_3d_coupled_social_environment_maturation_controller as coupled
import ssrm_3d_learned_multiday_maturation_controller as base
import ssrm_3d_return_selected_multiday_maturation_controller as report105


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_policy_value_allocator"
VALUE_SEED = 20261421


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
    policy_value_samples: int = 12
    policy_value_candidates: int = 48
    policy_value_rollouts: int = 5
    policy_value_epochs: int = 180
    policy_value_hidden_size: int = 64
    policy_value_sigma: float = 0.52
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class PolicyValueSelectionRow:
    phase: str
    candidate: int
    rolled_out: bool
    selected: bool
    tune_total_score: float
    tune_maturation_score: float
    tune_crisis_score: float
    tune_resolved_rate: float
    tune_env_response: float
    tune_social_response: float
    tune_coupled_response: float
    tune_damage: float
    actual_objective: float
    predicted_objective: float
    env_bias: float
    social_bias: float
    strength_bias: float
    env_pressure_weight: float
    social_pressure_weight: float
    infrastructure_weight: float
    response_imbalance_weight: float


@dataclass(frozen=True)
class PolicyValueTrainingRow:
    examples: int
    epochs: int
    final_loss: float
    target_mean: float
    target_std: float
    train_mae: float


@dataclass(frozen=True)
class VerdictRow:
    selected_router: str
    policy_value_samples: int
    policy_value_candidates: int
    policy_value_rollouts: int
    selected_tune_objective: float
    seed_tune_objective: float
    best_sample_tune_objective: float
    policy_value_total_score: float
    seed_allocator_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    policy_value_crisis_score: float
    seed_allocator_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    policy_value_resolved_rate: float
    seed_allocator_resolved_rate: float
    fixed_joint_resolved_rate: float
    return_selected_resolved_rate: float
    policy_value_coupled_response: float
    seed_allocator_coupled_response: float
    fixed_joint_coupled_response: float
    return_selected_coupled_response: float
    gain_over_return_selected: float
    gain_over_seed_allocator: float
    gap_to_fixed_joint: float
    social_culture_crisis_loss: float
    environment_crisis_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    mean_crisis_count: float
    supports_consequence_value_selection: bool
    supports_return_baseline_improvement: bool
    supports_seed_transfer_improvement: bool
    supports_policy_value_allocation: bool
    supports_non_fixed_transfer: bool
    supports_social_environment_dependency: bool
    verdict: str


class AllocationValueNet(torch.nn.Module):
    def __init__(self, hidden_size: int) -> None:
        super().__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(report115.PARAM_COUNT, hidden_size),
            torch.nn.Tanh(),
            torch.nn.Linear(hidden_size, hidden_size),
            torch.nn.Tanh(),
            torch.nn.Linear(hidden_size, 1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x).squeeze(-1)


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def parse_ints(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def clamp_param(value: float) -> float:
    return max(-3.0, min(3.0, value))


def clamp_params(params: Sequence[float]) -> Tuple[float, ...]:
    return tuple(clamp_param(value) for value in params)


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


def selection_metrics(rows: Sequence[coupled.EvalRow]) -> Tuple[float, float, float, float, float, float, float, float, float]:
    return report115.selection_objective(rows)


def evaluate_params(
    seeds: Sequence[int],
    cfg: Config,
    model: base.ControllerNet,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
    params: Sequence[float],
) -> List[coupled.EvalRow]:
    return [
        report115.run_adaptive_episode(seed, cfg, model, env_model, social_model, device, router, params)[0]
        for seed in seeds
    ]


def selection_row(
    phase: str,
    candidate: int,
    params: Sequence[float],
    rows: Sequence[coupled.EvalRow],
    predicted_objective: float = 0.0,
    rolled_out: bool = True,
    selected: bool = False,
) -> PolicyValueSelectionRow:
    if rows:
        total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective = selection_metrics(rows)
    else:
        total = maturation = crisis = resolved = env_response = social_response = coupled_response = damage = objective = 0.0
    return PolicyValueSelectionRow(
        phase=phase,
        candidate=candidate,
        rolled_out=rolled_out,
        selected=selected,
        tune_total_score=total,
        tune_maturation_score=maturation,
        tune_crisis_score=crisis,
        tune_resolved_rate=resolved,
        tune_env_response=env_response,
        tune_social_response=social_response,
        tune_coupled_response=coupled_response,
        tune_damage=damage,
        actual_objective=objective,
        predicted_objective=predicted_objective,
        env_bias=params[0],
        social_bias=params[report115.ALLOC_INPUT_SIZE],
        strength_bias=params[report115.ALLOC_INPUT_SIZE * 2],
        env_pressure_weight=params[report115.ALLOC_INPUTS.index("env_pressure")],
        social_pressure_weight=params[report115.ALLOC_INPUT_SIZE + report115.ALLOC_INPUTS.index("social_pressure")],
        infrastructure_weight=params[report115.ALLOC_INPUTS.index("infrastructure_need")],
        response_imbalance_weight=params[report115.ALLOC_INPUT_SIZE * 2 + report115.ALLOC_INPUTS.index("response_imbalance")],
    )


def heuristic_candidates() -> List[Tuple[float, ...]]:
    base_params = list(report115.initial_allocator())
    candidates = [tuple(base_params)]
    for env_boost, social_boost, strength_boost in (
        (0.32, 0.12, 0.18),
        (0.12, 0.34, 0.18),
        (0.28, 0.28, 0.32),
        (0.42, 0.42, 0.44),
    ):
        params = list(base_params)
        params[report115.ALLOC_INPUTS.index("env_pressure")] += env_boost
        params[report115.ALLOC_INPUT_SIZE + report115.ALLOC_INPUTS.index("social_pressure")] += social_boost
        params[report115.ALLOC_INPUT_SIZE * 2 + report115.ALLOC_INPUTS.index("major_shocks")] += strength_boost
        candidates.append(clamp_params(params))
    return candidates


def sample_policy_params(cfg: Config, rng: random.Random) -> List[Tuple[float, ...]]:
    candidates = heuristic_candidates()
    base_params = list(report115.initial_allocator())
    while len(candidates) < max(1, cfg.policy_value_samples):
        candidates.append(clamp_params(
            base_params[index] + rng.gauss(0.0, cfg.policy_value_sigma)
            for index in range(report115.PARAM_COUNT)
        ))
    return candidates[: cfg.policy_value_samples]


def train_value_model(
    sample_rows: Sequence[PolicyValueSelectionRow],
    sample_params: Sequence[Sequence[float]],
    cfg: Config,
    device: torch.device,
) -> Tuple[AllocationValueNet, PolicyValueTrainingRow, float, float]:
    torch.manual_seed(VALUE_SEED)
    x = torch.tensor(sample_params, dtype=torch.float32, device=device)
    y = torch.tensor([row.actual_objective for row in sample_rows], dtype=torch.float32, device=device)
    target_mean = float(y.mean().item())
    target_std = float(y.std(unbiased=False).item())
    if target_std < 1e-6:
        target_std = 1.0
    y_norm = (y - target_mean) / target_std
    model = AllocationValueNet(cfg.policy_value_hidden_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.003)
    final_loss = 0.0
    for _ in range(cfg.policy_value_epochs):
        optimizer.zero_grad()
        pred = model(x)
        loss = torch.nn.functional.mse_loss(pred, y_norm)
        loss.backward()
        optimizer.step()
        final_loss = float(loss.item())
    with torch.no_grad():
        pred_obj = model(x) * target_std + target_mean
        train_mae = float(torch.mean(torch.abs(pred_obj - y)).item())
    return model, PolicyValueTrainingRow(
        examples=len(sample_rows),
        epochs=cfg.policy_value_epochs,
        final_loss=final_loss,
        target_mean=target_mean,
        target_std=target_std,
        train_mae=train_mae,
    ), target_mean, target_std


def predict_objectives(
    model: AllocationValueNet,
    params: Sequence[Sequence[float]],
    device: torch.device,
    target_mean: float,
    target_std: float,
) -> List[float]:
    with torch.no_grad():
        x = torch.tensor(params, dtype=torch.float32, device=device)
        pred = model(x) * target_std + target_mean
    return [float(value) for value in pred.detach().cpu().tolist()]


def proposal_params(
    cfg: Config,
    rng: random.Random,
    sample_rows: Sequence[PolicyValueSelectionRow],
    sample_params: Sequence[Tuple[float, ...]],
) -> List[Tuple[float, ...]]:
    scored = sorted(zip(sample_rows, sample_params), key=lambda item: item[0].actual_objective, reverse=True)
    elites = [params for _, params in scored[: max(2, min(4, len(scored)))]]
    proposals: List[Tuple[float, ...]] = list(dict.fromkeys(elites))
    mean_params = [
        mean(params[index] for params in elites)
        for index in range(report115.PARAM_COUNT)
    ]
    proposals.append(clamp_params(mean_params))
    while len(proposals) < max(cfg.policy_value_candidates, cfg.policy_value_rollouts):
        center = mean_params if rng.random() < 0.62 else list(rng.choice(elites))
        sigma = cfg.policy_value_sigma * (0.45 + rng.random() * 0.45)
        proposals.append(clamp_params(
            center[index] + rng.gauss(0.0, sigma)
            for index in range(report115.PARAM_COUNT)
        ))
    return list(dict.fromkeys(proposals))[: cfg.policy_value_candidates]


def select_policy_value_allocator(
    cfg: Config,
    model: base.ControllerNet,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[Tuple[float, ...], List[PolicyValueSelectionRow], List[PolicyValueTrainingRow]]:
    rng = random.Random(VALUE_SEED)
    sample_params = sample_policy_params(cfg, rng)
    sample_rows: List[PolicyValueSelectionRow] = []
    for index, params in enumerate(sample_params):
        rows = evaluate_params(cfg.tune_seeds, cfg, model, env_model, social_model, device, router, params)
        sample_rows.append(selection_row("sample", index, params, rows))

    value_model, training_row, target_mean, target_std = train_value_model(sample_rows, sample_params, cfg, device)
    proposals = proposal_params(cfg, rng, sample_rows, sample_params)
    predictions = predict_objectives(value_model, proposals, device, target_mean, target_std)
    ranked = sorted(enumerate(zip(proposals, predictions)), key=lambda item: item[1][1], reverse=True)
    rollout_budget = max(1, min(cfg.policy_value_rollouts, len(ranked)))
    rollout_indices = {index for index, _ in ranked[:rollout_budget]}

    proposal_rows: List[PolicyValueSelectionRow] = []
    actual_by_index: Dict[int, Tuple[float, Tuple[float, ...], PolicyValueSelectionRow]] = {}
    for index, (params, predicted) in enumerate(zip(proposals, predictions)):
        if index in rollout_indices:
            rows = evaluate_params(cfg.tune_seeds, cfg, model, env_model, social_model, device, router, params)
            row = selection_row("value_guided", index, params, rows, predicted_objective=predicted)
            actual_by_index[index] = (row.actual_objective, params, row)
        else:
            row = selection_row("value_candidate", index, params, [], predicted_objective=predicted, rolled_out=False)
        proposal_rows.append(row)

    best_sample = max(zip(sample_rows, sample_params), key=lambda item: item[0].actual_objective)
    best_actual = (best_sample[0].actual_objective, best_sample[1], best_sample[0])
    for actual in actual_by_index.values():
        if actual[0] > best_actual[0]:
            best_actual = actual
    selected_params = tuple(best_actual[1])

    marked_rows: List[PolicyValueSelectionRow] = []
    selected_row = best_actual[2]
    for row in sample_rows + proposal_rows:
        selected = row.phase == selected_row.phase and row.candidate == selected_row.candidate and row.rolled_out
        marked_rows.append(replace(row, selected=selected))
    return selected_params, marked_rows, [training_row]


def row_lookup(summary: Sequence[coupled.SummaryRow], controller: str, ablation: str) -> coupled.SummaryRow:
    return coupled.row_lookup(summary, controller, ablation)


def ablations_from_summary(summary: Sequence[coupled.SummaryRow]) -> List[coupled.AblationRow]:
    base_row = row_lookup(summary, "policy_value_allocator_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = row_lookup(summary, "policy_value_allocator_gru", ablation)
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
    schedules: Sequence[report114.ScheduleRow],
    selection_rows: Sequence[PolicyValueSelectionRow],
    cfg: Config,
) -> VerdictRow:
    policy_value = row_lookup(summary, "policy_value_allocator_gru", "none")
    seed_allocator = row_lookup(summary, "seed_allocator_gru", "none")
    fixed = row_lookup(summary, "fixed_joint_gru", "none")
    returned = row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    sample_actuals = [row.actual_objective for row in selection_rows if row.phase == "sample" and row.rolled_out]
    selected_rows = [row for row in selection_rows if row.selected]
    selected_tune = selected_rows[0].actual_objective if selected_rows else 0.0
    seed_tune = sample_actuals[0] if sample_actuals else 0.0
    best_sample = max(sample_actuals) if sample_actuals else 0.0
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    supports_value_selection = selected_tune >= seed_tune + 0.010 and selected_tune >= best_sample - 1e-9
    supports_return_baseline = (
        mean_crisis_count >= 4.0
        and policy_value.mean_total_score - returned.mean_total_score >= 0.010
        and policy_value.mean_crisis_score - returned.mean_crisis_score >= 0.040
        and policy_value.mean_resolved_rate - returned.mean_resolved_rate >= 0.080
        and policy_value.mean_coupled_response_rate - returned.mean_coupled_response_rate >= 0.080
        and policy_value.mean_alive_at_12h >= 12.0
        and policy_value.shock_gate_pass_rate == 1.0
        and policy_value.post_gate_shock_rate == 1.0
    )
    supports_seed_transfer = (
        policy_value.mean_total_score - seed_allocator.mean_total_score >= 0.005
        and policy_value.mean_crisis_score - seed_allocator.mean_crisis_score >= 0.020
        and policy_value.mean_resolved_rate - seed_allocator.mean_resolved_rate >= 0.020
        and policy_value.mean_coupled_response_rate - seed_allocator.mean_coupled_response_rate >= 0.020
    )
    supports_policy_value = supports_return_baseline and supports_seed_transfer
    supports_non_fixed = (
        policy_value.mean_crisis_score >= 0.45
        and policy_value.mean_coupled_response_rate >= 0.55
        and fixed.mean_crisis_score - policy_value.mean_crisis_score <= 0.18
        and fixed.mean_total_score - policy_value.mean_total_score <= 0.12
    )
    supports_dependency = (
        social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    return VerdictRow(
        selected_router=router.name,
        policy_value_samples=cfg.policy_value_samples,
        policy_value_candidates=cfg.policy_value_candidates,
        policy_value_rollouts=cfg.policy_value_rollouts,
        selected_tune_objective=selected_tune,
        seed_tune_objective=seed_tune,
        best_sample_tune_objective=best_sample,
        policy_value_total_score=policy_value.mean_total_score,
        seed_allocator_total_score=seed_allocator.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        policy_value_crisis_score=policy_value.mean_crisis_score,
        seed_allocator_crisis_score=seed_allocator.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        policy_value_resolved_rate=policy_value.mean_resolved_rate,
        seed_allocator_resolved_rate=seed_allocator.mean_resolved_rate,
        fixed_joint_resolved_rate=fixed.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        policy_value_coupled_response=policy_value.mean_coupled_response_rate,
        seed_allocator_coupled_response=seed_allocator.mean_coupled_response_rate,
        fixed_joint_coupled_response=fixed.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        gain_over_return_selected=policy_value.mean_total_score - returned.mean_total_score,
        gain_over_seed_allocator=policy_value.mean_total_score - seed_allocator.mean_total_score,
        gap_to_fixed_joint=fixed.mean_total_score - policy_value.mean_total_score,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=policy_value.shock_gate_pass_rate,
        post_gate_shock_rate=policy_value.post_gate_shock_rate,
        survival_at_12h=policy_value.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_consequence_value_selection=supports_value_selection,
        supports_return_baseline_improvement=supports_return_baseline,
        supports_seed_transfer_improvement=supports_seed_transfer,
        supports_policy_value_allocation=supports_policy_value,
        supports_non_fixed_transfer=supports_non_fixed,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_value_selection and supports_policy_value and supports_non_fixed and supports_dependency else "partial_or_failed",
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
            20261431,
        )
        social_model, social_training = report113.train_action_model(
            cfg,
            device,
            "social",
            social_sequences,
            social_labels,
            flags,
            20261432,
        )
        selected_allocator, selection_rows, value_training_rows = select_policy_value_allocator(
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
        seed_allocator = report115.initial_allocator()
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
            fixed_row = report115.run_fixed_joint_episode(seed, cfg, models["gru"], env_model, social_model, device, selected_router)
            eval_rows.append(fixed_row)
            seed_row, _, seed_tracker = report115.run_adaptive_episode(
                seed,
                cfg,
                models["gru"],
                env_model,
                social_model,
                device,
                selected_router,
                seed_allocator,
            )
            eval_rows.append(replace(seed_row, controller="seed_allocator_gru"))
            crisis_logs[f"{seed}:fixed_joint_gru:none"] = []
            crisis_logs[f"{seed}:seed_allocator_gru:none"] = seed_tracker.response_log
            policy_row, maybe_trace, tracker = report115.run_adaptive_episode(
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
            eval_rows.append(replace(policy_row, controller="policy_value_allocator_gru"))
            crisis_logs[f"{seed}:policy_value_allocator_gru:none"] = tracker.response_log
            if maybe_trace.frames:
                trace_out = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker = report115.run_adaptive_episode(
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
                eval_rows.append(replace(row, controller="policy_value_allocator_gru", ablation=ablation))
                crisis_logs[f"{seed}:policy_value_allocator_gru:{ablation}"] = tracker.response_log

    summary = coupled.summarize(eval_rows)
    ablations = ablations_from_summary(summary)
    probes = report115.allocator_probes(selected_allocator, schedules)
    verdict = transfer_verdict(summary, ablations, selected_router, schedules, selection_rows, cfg)
    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "policy_value_allocator", "frames": []}
    trace_payload["condition"] = "policy_value_allocator_gru"
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
            "policy_value_samples": cfg.policy_value_samples,
            "policy_value_candidates": cfg.policy_value_candidates,
            "policy_value_rollouts": cfg.policy_value_rollouts,
            "policy_value_epochs": cfg.policy_value_epochs,
            "policy_value_hidden_size": cfg.policy_value_hidden_size,
            "policy_value_sigma": cfg.policy_value_sigma,
            "device": cfg.device,
            "trace_seed": cfg.trace_seed,
        },
        "allocation_inputs": list(report115.ALLOC_INPUTS),
        "selected_allocator": list(selected_allocator),
        "seed_allocator": list(seed_allocator),
        "fixed_joint_baseline": list(report115.FIXED_JOINT),
        "schedule": [asdict(row) for row in schedules],
        "router_selection": [asdict(row) for row in router_selection],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "policy_value_selection": [asdict(row) for row in selection_rows],
        "policy_value_training": [asdict(row) for row in value_training_rows],
        "allocator_probes": [asdict(row) for row in probes],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace_payload,
        "crisis_logs": crisis_logs,
        "notes": {
            "claim": "closed-loop consequence labels can train a value model that selects allocator policies for rollout",
            "not_claimed": "actor-critic reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
            "remaining_structure": "allocator inputs are engineered summaries and environmental/social action heads are still supervised; this tests value-guided allocation selection, not full open policy learning",
        },
    }
    rows_to_csv(Path(f"{PREFIX}_schedule.csv"), schedules)
    rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    rows_to_csv(Path(f"{PREFIX}_action_training.csv"), [env_training, social_training])
    rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    rows_to_csv(Path(f"{PREFIX}_policy_value_selection.csv"), selection_rows)
    rows_to_csv(Path(f"{PREFIX}_policy_value_training.csv"), value_training_rows)
    rows_to_csv(Path(f"{PREFIX}_allocator_probes.csv"), probes)
    rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    write_json(Path(f"{PREFIX}_results.json"), payload)
    write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_POLICY_VALUE_ALLOCATOR_RESULTS", payload)
    write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_POLICY_VALUE_ALLOCATOR_TRACE", trace_payload)
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
    parser.add_argument("--policy-value-samples", type=int, default=12)
    parser.add_argument("--policy-value-candidates", type=int, default=48)
    parser.add_argument("--policy-value-rollouts", type=int, default=5)
    parser.add_argument("--policy-value-epochs", type=int, default=180)
    parser.add_argument("--policy-value-hidden-size", type=int, default=64)
    parser.add_argument("--policy-value-sigma", type=float, default=0.52)
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
        policy_value_samples=args.policy_value_samples,
        policy_value_candidates=args.policy_value_candidates,
        policy_value_rollouts=args.policy_value_rollouts,
        policy_value_epochs=args.policy_value_epochs,
        policy_value_hidden_size=args.policy_value_hidden_size,
        policy_value_sigma=args.policy_value_sigma,
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "policy_value_selection": payload["policy_value_selection"],
        "verdict": payload["verdict"],
        "summary": payload["summary"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
