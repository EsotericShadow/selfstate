#!/usr/bin/env python3
"""SSRM-3D recurrent-observer precursor.

The first SSRM-3D experiment used a hand-built self-state layer. This follow-up
asks a narrower question: if recurrent observers watch embodied
action-observation traces from the same 3D world, do their hidden states recover
agent-bounded variables, and do those variables matter for future viability
prediction?

This is still not a consciousness experiment. It also does not make the LLM the
brain. The language module remains part of the trace-generating controller only;
the learned observer receives action-observation packets and is tested by
decodability and causal hidden-state ablation.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import torch
from torch import nn

import ssrm_3d_embodied_world as ssrm


ARTIFACT_DIR = Path("artifacts")
ARCHITECTURES = ("frame_mlp", "torch_rnn", "torch_gru", "torch_lstm")
RECURRENT_ARCHITECTURES = ("torch_rnn", "torch_gru", "torch_lstm")
MODES = (
    "avoid_hazard",
    "reach_shelter",
    "honor_commitment",
    "collect_resource",
    "explore_reduce_uncertainty",
)
EPS = 1e-12


@dataclass(frozen=True)
class ObserverConfig:
    episodes_per_stage: int = 42
    ticks: int = 540
    seed: int = 20260608
    stage_min: int = 0
    stage_max: int = 6
    world_size: float = 80.0
    perception_hz: int = 10
    goal_hz: int = 2
    reasoning_hz: float = 0.5
    hidden_size: int = 32
    future_window_frames: int = 8
    epochs: int = 180
    batch_size: int = 64
    learning_rate: float = 0.004
    train_fraction: float = 0.72
    ridge: float = 1e-3
    device: str = "auto"
    source_agents: Tuple[str, ...] = ssrm.AGENTS


@dataclass
class SequenceRecord:
    stage: int
    stage_name: str
    agent: str
    episode: int
    inputs: List[List[float]]
    self_targets: List[List[float]]
    world_targets: List[List[float]]
    future_targets: List[float]


@dataclass(frozen=True)
class ObserverSummaryRow:
    stage: int
    stage_name: str
    architecture: str
    sequence_count: int
    self_probe_r2: float
    world_probe_r2: float
    future_mse: float
    self_ablation_future_mse: float
    world_ablation_future_mse: float
    random_ablation_future_mse: float
    self_ablation_penalty: float
    world_ablation_penalty: float
    random_ablation_penalty: float
    self_edit_future_swing: float
    recurrent_self_gain_over_frame: float
    device_used: str
    parameter_count: int


@dataclass(frozen=True)
class ObserverVerdictRow:
    stage: int
    stage_name: str
    expected_pressure: str
    best_recurrent_architecture: str
    frame_self_r2: float
    recurrent_self_r2: float
    recurrent_world_r2: float
    recurrent_self_gain_over_frame: float
    recurrent_future_mse: float
    recurrent_self_ablation_penalty: float
    recurrent_world_ablation_penalty: float
    recurrent_self_edit_future_swing: float
    supports_recurrent_observer_precursor: bool
    verdict: str


class ObserverNet(nn.Module):
    def __init__(self, architecture: str, input_size: int, hidden_size: int) -> None:
        super().__init__()
        self.architecture = architecture
        self.hidden_size = hidden_size
        if architecture == "frame_mlp":
            self.encoder = nn.Sequential(
                nn.Linear(input_size, hidden_size),
                nn.Tanh(),
                nn.Linear(hidden_size, hidden_size),
                nn.Tanh(),
            )
        elif architecture == "torch_rnn":
            self.recurrent = nn.RNN(input_size, hidden_size, batch_first=True, nonlinearity="tanh")
        elif architecture == "torch_gru":
            self.recurrent = nn.GRU(input_size, hidden_size, batch_first=True)
        elif architecture == "torch_lstm":
            self.recurrent = nn.LSTM(input_size, hidden_size, batch_first=True)
        else:
            raise ValueError(f"unknown architecture: {architecture}")
        self.self_head = nn.Linear(hidden_size, 4)
        self.world_head = nn.Linear(hidden_size, 4)
        self.future_head = nn.Linear(hidden_size, 1)

    def encode(self, inputs: torch.Tensor) -> torch.Tensor:
        if self.architecture == "frame_mlp":
            return self.encoder(inputs)
        outputs, _hidden = self.recurrent(inputs)
        return outputs

    def heads(self, hidden: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        return self.self_head(hidden), self.world_head(hidden), self.future_head(hidden)

    def forward(self, inputs: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
        hidden = self.encode(inputs)
        self_pred, world_pred, future_pred = self.heads(hidden)
        return hidden, self_pred, world_pred, future_pred


def resolve_device(requested: str) -> torch.device:
    if requested == "auto":
        if torch.backends.mps.is_available():
            return torch.device("mps")
        return torch.device("cpu")
    if requested == "mps":
        if not torch.backends.mps.is_available():
            raise SystemExit("requested MPS device, but torch.backends.mps.is_available() is false")
        return torch.device("mps")
    if requested == "cpu":
        return torch.device("cpu")
    raise SystemExit("--device must be one of auto, mps, cpu")


def mode_one_hot(mode: str) -> List[float]:
    return [1.0 if mode == item else 0.0 for item in MODES]


def object_distance(frame: Dict[str, object], objects: Sequence[Dict[str, object]], active_ids: Optional[set[str]] = None) -> float:
    x = float(frame["x"])
    z = float(frame["z"])
    distances = []
    for obj in objects:
        if active_ids is not None and str(obj["id"]) not in active_ids:
            continue
        if not bool(obj.get("active", True)):
            continue
        distances.append(ssrm.distance(x, z, float(obj["x"]), float(obj["z"])))
    return min(distances) if distances else float("inf")


def closeness(value: float, world_size: float) -> float:
    if math.isinf(value):
        return 0.0
    return ssrm.clamp(1.0 - value / max(world_size, EPS), 0.0, 1.0)


def frame_features(
    trace: Dict[str, object],
    frame: Dict[str, object],
    previous_frame: Optional[Dict[str, object]],
    cfg: ObserverConfig,
) -> Tuple[List[float], List[float]]:
    stage = ssrm.StageSpec(**trace["stage"])
    world = trace["world"]
    tick = int(frame["tick"])
    active_ids = set(str(item) for item in frame["active_resources"])
    resource_distance = object_distance(frame, world["resources"], active_ids)
    hazard_distance = object_distance(frame, world["hazards"])
    shelter_distance = object_distance(frame, world["shelters"])
    daylight = 0.5 + 0.5 * math.cos((tick / max(cfg.ticks - 1, 1)) * math.tau)
    weather = ssrm.clamp(stage.weather_amp * (0.55 + 0.45 * math.sin(tick * 0.017 + stage.index)), 0.0, 1.0)
    competitor = frame["competitor"]
    competitor_distance = (
        ssrm.distance(float(frame["x"]), float(frame["z"]), float(competitor["x"]), float(competitor["z"]))
        if bool(competitor["active"])
        else float("inf")
    )
    if previous_frame is None:
        dx = 0.0
        dz = 0.0
    else:
        dx = (float(frame["x"]) - float(previous_frame["x"])) / max(cfg.world_size, EPS)
        dz = (float(frame["z"]) - float(previous_frame["z"])) / max(cfg.world_size, EPS)
    heading = float(frame["heading"])
    features = [
        float(frame["x"]) / (cfg.world_size * 0.5),
        float(frame["z"]) / (cfg.world_size * 0.5),
        dx * 15.0,
        dz * 15.0,
        min(1.0, math.hypot(dx, dz) * 75.0),
        math.sin(heading),
        math.cos(heading),
        ssrm.clamp((float(frame["y"]) + 2.0) / 4.0, 0.0, 1.0),
        closeness(resource_distance, cfg.world_size),
        closeness(hazard_distance, cfg.world_size),
        closeness(shelter_distance, cfg.world_size),
        daylight,
        weather,
        len(active_ids) / max(len(world["resources"]), 1),
        float(frame["resources_collected"]) / max(len(world["resources"]), 1),
        closeness(competitor_distance, cfg.world_size),
    ]
    features.extend(mode_one_hot(str(frame["mode"])))
    world_targets = [
        closeness(resource_distance, cfg.world_size),
        closeness(hazard_distance, cfg.world_size),
        daylight,
        weather,
    ]
    return features, world_targets


def trace_to_record(
    trace: Dict[str, object],
    stage: ssrm.StageSpec,
    agent: str,
    episode: int,
    cfg: ObserverConfig,
) -> SequenceRecord:
    frames = trace["frames"]
    inputs: List[List[float]] = []
    self_targets: List[List[float]] = []
    world_targets: List[List[float]] = []
    previous_frame: Optional[Dict[str, object]] = None
    for frame in frames:
        features, world = frame_features(trace, frame, previous_frame, cfg)
        inputs.append(features)
        world_targets.append(world)
        self_targets.append(
            [
                float(frame["energy"]),
                float(frame["integrity"]),
                float(frame["mobility"]),
                float(frame["sensor"]),
            ]
        )
        previous_frame = frame
    future_targets: List[float] = []
    for index in range(len(self_targets)):
        future = self_targets[index : min(len(self_targets), index + cfg.future_window_frames + 1)]
        viability_values = [
            0.44 * row[0] + 0.32 * row[1] + 0.18 * row[2] + 0.06 * row[3]
            for row in future
        ]
        future_targets.append(min(viability_values) if viability_values else 0.0)
    return SequenceRecord(
        stage=stage.index,
        stage_name=stage.name,
        agent=agent,
        episode=episode,
        inputs=inputs,
        self_targets=self_targets,
        world_targets=world_targets,
        future_targets=future_targets,
    )


def generate_records(cfg: ObserverConfig) -> List[SequenceRecord]:
    records: List[SequenceRecord] = []
    base_cfg = ssrm.SSRM3DConfig(
        episodes=1,
        ticks=cfg.ticks,
        seed=cfg.seed,
        stage_min=cfg.stage_min,
        stage_max=cfg.stage_max,
        world_size=cfg.world_size,
        perception_hz=cfg.perception_hz,
        goal_hz=cfg.goal_hz,
        reasoning_hz=cfg.reasoning_hz,
        trace_stage=cfg.stage_max,
        trace_episode=0,
    )
    stages = [stage for stage in ssrm.STAGES if cfg.stage_min <= stage.index <= cfg.stage_max]
    for stage in stages:
        for episode in range(cfg.episodes_per_stage):
            agent = cfg.source_agents[episode % len(cfg.source_agents)]
            _metrics, trace = ssrm.run_episode(stage, agent, episode, base_cfg, collect_trace=True)
            if trace is None:
                continue
            records.append(trace_to_record(trace, stage, agent, episode, cfg))
    return records


def split_indices(records: Sequence[SequenceRecord], cfg: ObserverConfig) -> Tuple[List[int], List[int]]:
    rng = random.Random(cfg.seed + 37)
    train: List[int] = []
    test: List[int] = []
    for stage in sorted({record.stage for record in records}):
        indices = [index for index, record in enumerate(records) if record.stage == stage]
        rng.shuffle(indices)
        train_count = max(1, min(len(indices) - 1, round(len(indices) * cfg.train_fraction)))
        train.extend(indices[:train_count])
        test.extend(indices[train_count:])
    return train, test


def build_tensors(
    records: Sequence[SequenceRecord],
    device: torch.device,
) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    max_len = max(len(record.inputs) for record in records)
    input_size = len(records[0].inputs[0])
    inputs = torch.zeros((len(records), max_len, input_size), dtype=torch.float32)
    self_targets = torch.zeros((len(records), max_len, 4), dtype=torch.float32)
    world_targets = torch.zeros((len(records), max_len, 4), dtype=torch.float32)
    future_targets = torch.zeros((len(records), max_len, 1), dtype=torch.float32)
    mask = torch.zeros((len(records), max_len), dtype=torch.float32)
    all_future = [value for record in records for value in record.future_targets]
    future_min = min(all_future)
    future_span = max(max(all_future) - future_min, EPS)
    for index, record in enumerate(records):
        length = len(record.inputs)
        inputs[index, :length] = torch.tensor(record.inputs, dtype=torch.float32)
        self_targets[index, :length] = torch.tensor(record.self_targets, dtype=torch.float32)
        world_targets[index, :length] = torch.tensor(record.world_targets, dtype=torch.float32)
        normalized_future = [((value - future_min) / future_span) for value in record.future_targets]
        future_targets[index, :length, 0] = torch.tensor(normalized_future, dtype=torch.float32)
        mask[index, :length] = 1.0
    return (
        inputs.to(device),
        self_targets.to(device),
        world_targets.to(device),
        future_targets.to(device),
        mask.to(device),
    )


def masked_mse(prediction: torch.Tensor, target: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    weights = mask.unsqueeze(-1)
    return ((prediction - target) ** 2 * weights).sum() / (weights.sum() * prediction.shape[-1] + EPS)


def train_model(
    architecture: str,
    cfg: ObserverConfig,
    tensors: Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor],
    train_indices: Sequence[int],
    device: torch.device,
) -> ObserverNet:
    inputs, self_targets, world_targets, future_targets, mask = tensors
    torch.manual_seed(cfg.seed + 101 * (ARCHITECTURES.index(architecture) + 1))
    model = ObserverNet(architecture, inputs.shape[-1], cfg.hidden_size).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=cfg.learning_rate, weight_decay=1e-4)
    train_indices_tensor = torch.tensor(list(train_indices), dtype=torch.long, device=device)
    generator = torch.Generator(device="cpu")
    generator.manual_seed(cfg.seed + 501 * (ARCHITECTURES.index(architecture) + 1))
    for _epoch in range(cfg.epochs):
        permutation = torch.randperm(len(train_indices), generator=generator).tolist()
        for start in range(0, len(permutation), cfg.batch_size):
            batch_positions = permutation[start : start + cfg.batch_size]
            batch = train_indices_tensor[torch.tensor(batch_positions, dtype=torch.long, device=device)]
            optimizer.zero_grad(set_to_none=True)
            _hidden, self_pred, world_pred, future_pred = model(inputs[batch])
            batch_mask = mask[batch]
            loss = (
                1.15 * masked_mse(self_pred, self_targets[batch], batch_mask)
                + 0.75 * masked_mse(future_pred, future_targets[batch], batch_mask)
                + 0.25 * masked_mse(world_pred, world_targets[batch], batch_mask)
            )
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 2.5)
            optimizer.step()
    return model


def flatten_masked(values: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    return values[mask > 0.5].detach().float().cpu()


def fit_probe(hidden: torch.Tensor, target: torch.Tensor, mask: torch.Tensor, ridge: float) -> torch.Tensor:
    x = flatten_masked(hidden, mask)
    y = flatten_masked(target, mask)
    ones = torch.ones((x.shape[0], 1), dtype=x.dtype)
    design = torch.cat([x, ones], dim=1)
    penalty = torch.eye(design.shape[1], dtype=x.dtype) * ridge
    penalty[-1, -1] = 0.0
    lhs = design.T @ design + penalty
    rhs = design.T @ y
    return torch.linalg.solve(lhs, rhs)


def predict_probe(hidden: torch.Tensor, weights: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    x = flatten_masked(hidden, mask)
    ones = torch.ones((x.shape[0], 1), dtype=x.dtype)
    return torch.cat([x, ones], dim=1) @ weights


def r2_score(prediction: torch.Tensor, target: torch.Tensor) -> float:
    scores: List[float] = []
    for column in range(target.shape[1]):
        y = target[:, column]
        variance = ((y - y.mean()) ** 2).sum()
        if float(variance) < 1e-8:
            continue
        residual = ((prediction[:, column] - y) ** 2).sum()
        scores.append(float(1.0 - residual / variance))
    if not scores:
        return 0.0
    return max(-1.0, min(1.0, statistics.fmean(scores)))


def basis_from_probe(weights: torch.Tensor) -> torch.Tensor:
    directions = weights[:-1, :]
    if torch.linalg.norm(directions) < 1e-8:
        return torch.zeros((directions.shape[0], 0), dtype=torch.float32)
    q, r = torch.linalg.qr(directions, mode="reduced")
    keep = torch.abs(torch.diag(r)) > 1e-5
    return q[:, keep].float()


def remove_subspace(hidden: torch.Tensor, basis: torch.Tensor) -> torch.Tensor:
    if basis.numel() == 0:
        return hidden
    basis = basis.to(hidden.device, dtype=hidden.dtype)
    return hidden - (hidden @ basis) @ basis.T


def random_basis(hidden_size: int, dimension: int, seed: int) -> torch.Tensor:
    if dimension <= 0:
        return torch.zeros((hidden_size, 0), dtype=torch.float32)
    generator = torch.Generator(device="cpu")
    generator.manual_seed(seed)
    raw = torch.randn((hidden_size, dimension), generator=generator)
    q, _r = torch.linalg.qr(raw, mode="reduced")
    return q.float()


def self_edit_swing(
    model: ObserverNet,
    hidden: torch.Tensor,
    self_probe: torch.Tensor,
    mask: torch.Tensor,
    scale: float = 0.45,
) -> float:
    directions = self_probe[:-1, :3]
    if torch.linalg.norm(directions) < 1e-8:
        return 0.0
    direction = 0.45 * directions[:, 0] + 0.35 * directions[:, 1] + 0.20 * directions[:, 2]
    direction = direction / (torch.linalg.norm(direction) + EPS)
    direction = direction.to(hidden.device, dtype=hidden.dtype)
    low_hidden = hidden - scale * direction
    high_hidden = hidden + scale * direction
    _self_low, _world_low, future_low = model.heads(low_hidden)
    _self_high, _world_high, future_high = model.heads(high_hidden)
    weights = mask.unsqueeze(-1)
    swing = (torch.abs(future_high - future_low) * weights).sum() / (weights.sum() + EPS)
    return float(swing.detach().cpu())


def stage_mask(records: Sequence[SequenceRecord], indices: Sequence[int], base_mask: torch.Tensor, stage: int) -> torch.Tensor:
    selected = torch.zeros_like(base_mask)
    for index in indices:
        if records[index].stage == stage:
            selected[index] = base_mask[index]
    return selected


def future_mse_from_hidden(
    model: ObserverNet,
    hidden: torch.Tensor,
    future_targets: torch.Tensor,
    mask: torch.Tensor,
    basis: Optional[torch.Tensor] = None,
) -> float:
    edited = remove_subspace(hidden, basis) if basis is not None else hidden
    _self_pred, _world_pred, future_pred = model.heads(edited)
    return float(masked_mse(future_pred, future_targets, mask).detach().cpu())


def evaluate_models(
    models: Dict[str, ObserverNet],
    cfg: ObserverConfig,
    records: Sequence[SequenceRecord],
    tensors: Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor],
    train_indices: Sequence[int],
    test_indices: Sequence[int],
    device: torch.device,
) -> Tuple[List[ObserverSummaryRow], List[ObserverVerdictRow], Dict[str, object]]:
    inputs, self_targets, world_targets, future_targets, mask = tensors
    stages = [stage for stage in ssrm.STAGES if cfg.stage_min <= stage.index <= cfg.stage_max]
    summary_rows: List[ObserverSummaryRow] = []
    diagnostics: Dict[str, object] = {"architectures": {}}
    frame_self_by_stage: Dict[int, float] = {}

    train_mask_all = torch.zeros_like(mask)
    test_mask_all = torch.zeros_like(mask)
    for index in train_indices:
        train_mask_all[index] = mask[index]
    for index in test_indices:
        test_mask_all[index] = mask[index]

    for architecture, model in models.items():
        model.eval()
        with torch.no_grad():
            hidden, _self_pred, _world_pred, _future_pred = model(inputs)
        self_probe = fit_probe(hidden, self_targets, train_mask_all, cfg.ridge)
        world_probe = fit_probe(hidden, world_targets, train_mask_all, cfg.ridge)
        self_basis = basis_from_probe(self_probe)
        world_basis = basis_from_probe(world_probe)
        random_dim = max(1, min(self_basis.shape[1], hidden.shape[-1]))
        random_subspace = random_basis(hidden.shape[-1], random_dim, cfg.seed + 701 + ARCHITECTURES.index(architecture))
        parameter_count = sum(parameter.numel() for parameter in model.parameters())
        diagnostics["architectures"][architecture] = {
            "parameter_count": parameter_count,
            "self_subspace_dimension": int(self_basis.shape[1]),
            "world_subspace_dimension": int(world_basis.shape[1]),
        }
        for stage in stages:
            current_mask = stage_mask(records, test_indices, mask, stage.index)
            if float(current_mask.sum().detach().cpu()) <= 0.0:
                continue
            self_prediction = predict_probe(hidden, self_probe, current_mask)
            world_prediction = predict_probe(hidden, world_probe, current_mask)
            self_target = flatten_masked(self_targets, current_mask)
            world_target = flatten_masked(world_targets, current_mask)
            self_r2 = r2_score(self_prediction, self_target)
            world_r2 = r2_score(world_prediction, world_target)
            full_mse = future_mse_from_hidden(model, hidden, future_targets, current_mask)
            self_mse = future_mse_from_hidden(model, hidden, future_targets, current_mask, self_basis)
            world_mse = future_mse_from_hidden(model, hidden, future_targets, current_mask, world_basis)
            random_mse = future_mse_from_hidden(model, hidden, future_targets, current_mask, random_subspace)
            edit_swing = self_edit_swing(model, hidden, self_probe, current_mask)
            if architecture == "frame_mlp":
                frame_self_by_stage[stage.index] = self_r2
            recurrent_gain = self_r2 - frame_self_by_stage.get(stage.index, self_r2)
            sequence_count = sum(1 for index in test_indices if records[index].stage == stage.index)
            summary_rows.append(
                ObserverSummaryRow(
                    stage=stage.index,
                    stage_name=stage.name,
                    architecture=architecture,
                    sequence_count=sequence_count,
                    self_probe_r2=self_r2,
                    world_probe_r2=world_r2,
                    future_mse=full_mse,
                    self_ablation_future_mse=self_mse,
                    world_ablation_future_mse=world_mse,
                    random_ablation_future_mse=random_mse,
                    self_ablation_penalty=self_mse - full_mse,
                    world_ablation_penalty=world_mse - full_mse,
                    random_ablation_penalty=random_mse - full_mse,
                    self_edit_future_swing=edit_swing,
                    recurrent_self_gain_over_frame=recurrent_gain,
                    device_used=str(device),
                    parameter_count=parameter_count,
                )
            )
    verdicts = build_verdicts(summary_rows)
    return summary_rows, verdicts, diagnostics


def build_verdicts(summary_rows: Sequence[ObserverSummaryRow]) -> List[ObserverVerdictRow]:
    verdicts: List[ObserverVerdictRow] = []
    for stage in ssrm.STAGES:
        rows = [row for row in summary_rows if row.stage == stage.index]
        if not rows:
            continue
        by_architecture = {row.architecture: row for row in rows}
        frame = by_architecture["frame_mlp"]
        recurrent_rows = [by_architecture[name] for name in RECURRENT_ARCHITECTURES]
        best = max(
            recurrent_rows,
            key=lambda row: (
                row.self_probe_r2,
                row.self_ablation_penalty,
                -row.future_mse,
            ),
        )
        gain = best.self_probe_r2 - frame.self_probe_r2
        if stage.index == 0:
            supports = best.self_probe_r2 > 0.60 and gain < 0.08 and best.self_edit_future_swing < 0.03
            verdict = "body_state_decodable_without_recurrent_advantage_in_low_pressure_task" if supports else "stage_0_body_state_control_not_clean"
        elif stage.index == 1:
            supports = best.self_probe_r2 > 0.55 and best.self_edit_future_swing > 0.02
            verdict = "hidden_energy_self_state_decodable_and_editable" if supports else "hidden_energy_recurrent_observer_not_sufficient"
        elif stage.index in {2, 3}:
            supports = best.self_probe_r2 > 0.58 and gain > 0.03 and best.self_edit_future_swing > 0.02
            verdict = "body_or_option_pressure_recruits_recurrent_self_state" if supports else "body_or_option_pressure_not_sufficient"
        else:
            supports = best.self_probe_r2 > 0.60 and gain > 0.03 and best.self_edit_future_swing > 0.02
            verdict = "commitment_arbitration_social_pressure_recruits_self_state" if supports else "high_pressure_recurrent_observer_not_sufficient"
        verdicts.append(
            ObserverVerdictRow(
                stage=stage.index,
                stage_name=stage.name,
                expected_pressure=stage.pressure,
                best_recurrent_architecture=best.architecture,
                frame_self_r2=frame.self_probe_r2,
                recurrent_self_r2=best.self_probe_r2,
                recurrent_world_r2=best.world_probe_r2,
                recurrent_self_gain_over_frame=gain,
                recurrent_future_mse=best.future_mse,
                recurrent_self_ablation_penalty=best.self_ablation_penalty,
                recurrent_world_ablation_penalty=best.world_ablation_penalty,
                recurrent_self_edit_future_swing=best.self_edit_future_swing,
                supports_recurrent_observer_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def run_experiment(
    cfg: ObserverConfig,
) -> Tuple[List[ObserverSummaryRow], List[ObserverVerdictRow], Dict[str, object]]:
    random.seed(cfg.seed)
    torch.manual_seed(cfg.seed)
    device = resolve_device(cfg.device)
    records = generate_records(cfg)
    train_indices, test_indices = split_indices(records, cfg)
    tensors = build_tensors(records, device)
    models = {
        architecture: train_model(architecture, cfg, tensors, train_indices, device)
        for architecture in ARCHITECTURES
    }
    summary_rows, verdicts, diagnostics = evaluate_models(models, cfg, records, tensors, train_indices, test_indices, device)
    diagnostics.update(
        {
            "record_count": len(records),
            "train_sequences": len(train_indices),
            "test_sequences": len(test_indices),
            "source_agents": list(cfg.source_agents),
            "device": str(device),
            "torch_version": torch.__version__,
            "mps_available": torch.backends.mps.is_available(),
            "note": (
                "The observer is trained on embodied traces. Selfhood is counted only "
                "when recurrent hidden state recovers agent-state variables and "
                "self-state edits move future-viability prediction. Ablation penalties "
                "are reported as a stricter, currently brittle causal check."
            ),
        }
    )
    return summary_rows, verdicts, diagnostics


def write_csv(path: Path, rows: Iterable[object]) -> None:
    rows = list(rows)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def print_table(verdicts: Sequence[ObserverVerdictRow]) -> None:
    headers = [
        "stage",
        "stage_name",
        "best_recurrent",
        "frame_self_r2",
        "recurrent_self_r2",
        "self_gain",
        "self_ablation_penalty",
        "self_edit_future_swing",
        "supports_recurrent_observer_precursor",
    ]
    rows = []
    for verdict in verdicts:
        rows.append(
            [
                str(verdict.stage),
                verdict.stage_name,
                verdict.best_recurrent_architecture,
                f"{verdict.frame_self_r2:.3f}",
                f"{verdict.recurrent_self_r2:.3f}",
                f"{verdict.recurrent_self_gain_over_frame:.3f}",
                f"{verdict.recurrent_self_ablation_penalty:.5f}",
                f"{verdict.recurrent_self_edit_future_swing:.5f}",
                str(verdict.supports_recurrent_observer_precursor),
            ]
        )
    widths = [
        max(len(header), *(len(row[index]) for row in rows))
        for index, header in enumerate(headers)
    ]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_source_agents(value: str) -> Tuple[str, ...]:
    agents = tuple(item.strip() for item in value.split(",") if item.strip())
    unknown = [agent for agent in agents if agent not in ssrm.AGENTS]
    if unknown:
        raise argparse.ArgumentTypeError(f"unknown source agent(s): {', '.join(unknown)}")
    if not agents:
        raise argparse.ArgumentTypeError("at least one source agent is required")
    return agents


def parse_args() -> ObserverConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes-per-stage", type=int, default=42)
    parser.add_argument("--ticks", type=int, default=540)
    parser.add_argument("--seed", type=int, default=20260608)
    parser.add_argument("--stage-min", type=int, default=0)
    parser.add_argument("--stage-max", type=int, default=6)
    parser.add_argument("--world-size", type=float, default=80.0)
    parser.add_argument("--perception-hz", type=int, default=10)
    parser.add_argument("--goal-hz", type=int, default=2)
    parser.add_argument("--reasoning-hz", type=float, default=0.5)
    parser.add_argument("--hidden-size", type=int, default=32)
    parser.add_argument("--future-window-frames", type=int, default=8)
    parser.add_argument("--epochs", type=int, default=180)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--train-fraction", type=float, default=0.72)
    parser.add_argument("--ridge", type=float, default=1e-3)
    parser.add_argument("--device", choices=("auto", "mps", "cpu"), default="auto")
    parser.add_argument(
        "--source-agents",
        type=parse_source_agents,
        default=",".join(ssrm.AGENTS),
        help="comma-separated SSRM-3D trace-generating agents",
    )
    args = parser.parse_args()
    if args.episodes_per_stage < 8:
        raise SystemExit("--episodes-per-stage must be at least 8")
    if args.ticks < 60:
        raise SystemExit("--ticks must be at least 60")
    if args.stage_min < 0 or args.stage_max > max(stage.index for stage in ssrm.STAGES):
        raise SystemExit("--stage-min/--stage-max out of range")
    if args.stage_min > args.stage_max:
        raise SystemExit("--stage-min must be <= --stage-max")
    if not 0.1 <= args.train_fraction <= 0.9:
        raise SystemExit("--train-fraction must be between 0.1 and 0.9")
    return ObserverConfig(
        episodes_per_stage=args.episodes_per_stage,
        ticks=args.ticks,
        seed=args.seed,
        stage_min=args.stage_min,
        stage_max=args.stage_max,
        world_size=args.world_size,
        perception_hz=args.perception_hz,
        goal_hz=args.goal_hz,
        reasoning_hz=args.reasoning_hz,
        hidden_size=args.hidden_size,
        future_window_frames=args.future_window_frames,
        epochs=args.epochs,
        batch_size=args.batch_size,
        learning_rate=args.learning_rate,
        train_fraction=args.train_fraction,
        ridge=args.ridge,
        device=args.device,
        source_agents=args.source_agents,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    summary_rows, verdicts, diagnostics = run_experiment(cfg)
    summary_path = ARTIFACT_DIR / "ssrm_3d_recurrent_observer_summary.csv"
    verdict_path = ARTIFACT_DIR / "ssrm_3d_recurrent_observer_verdict.csv"
    results_path = ARTIFACT_DIR / "ssrm_3d_recurrent_observer_results.json"
    write_csv(summary_path, summary_rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": {
                    **asdict(cfg),
                    "source_agents": list(cfg.source_agents),
                },
                "summary": [asdict(row) for row in summary_rows],
                "verdict": [asdict(row) for row in verdicts],
                "diagnostics": diagnostics,
            },
            handle,
            indent=2,
        )
        handle.write("\n")
    print(f"wrote {summary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print(
        "device",
        diagnostics["device"],
        "torch",
        diagnostics["torch_version"],
        "mps_available",
        diagnostics["mps_available"],
    )
    print_table(verdicts)
    return 0 if all(row.supports_recurrent_observer_precursor for row in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
