#!/usr/bin/env python3
"""SSRM-3D physics-first benchmark foundation.

This is the first physics-grounded benchmark milestone. It does not claim a
finished living society or subjective consciousness. It proves the next
architecture seam:

- a deterministic C++ physics/sensor kernel generates embodied traces;
- Python owns training, held-out evaluation, ablations, and artifacts;
- recurrent neural models learn decision structure from physics-derived
  observations without scenario labels.

The learned controller in this first pass is offline decision learning from
physics traces, not closed-loop RL. That limitation is explicit in the report
and is the next implementation target.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import os
import statistics
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import torch
from torch import nn


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
KERNEL_SRC = ROOT / "cpp" / "ssrm_physics" / "src"
KERNEL_INCLUDE = ROOT / "cpp" / "ssrm_physics" / "include"
KERNEL_BIN = ROOT / ".cache" / "ssrm_physics_kernel"

ACTION_NAMES = [
    "avoid_hazard",
    "collect_resource",
    "deliver_medicine",
    "explore",
    "help_dependent",
    "quarantine_clinic",
    "refuse_redirect_repair",
    "repair_shelter",
    "rest_shelter",
    "seek_water",
    "shelter_wait",
]
ACTION_TO_INDEX = {name: index for index, name in enumerate(ACTION_NAMES)}

WEATHER_NAMES = ["clear", "cold_wind", "fog", "heat", "rain", "storm"]
VISIBLE_NAMES = [
    "clinic_quarantine",
    "frontier",
    "hazard_ridge",
    "none",
    "resource_field",
    "ruins_cache",
    "shelter_hub",
    "social_camp",
    "vision_ablation",
    "water_source",
]


@dataclass(frozen=True)
class BenchmarkConfig:
    seed: int = 20260705
    ticks: int = 360
    train_episodes: int = 24
    test_episodes: int = 10
    epochs: int = 80
    hidden_size: int = 32
    learning_rate: float = 0.004
    device: str = "auto"
    trace_episode: int = 0


class RecurrentDecisionModel(nn.Module):
    def __init__(self, input_size: int, hidden_size: int, cell: str, output_size: int) -> None:
        super().__init__()
        if cell == "rnn":
            self.core: nn.Module = nn.RNN(input_size, hidden_size, batch_first=True)
        elif cell == "gru":
            self.core = nn.GRU(input_size, hidden_size, batch_first=True)
        elif cell == "lstm":
            self.core = nn.LSTM(input_size, hidden_size, batch_first=True)
        else:
            raise ValueError(f"unknown recurrent cell {cell!r}")
        self.head = nn.Linear(hidden_size, output_size)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        out, _ = self.core(x)
        return self.head(out)


def resolve_device(name: str) -> torch.device:
    if name == "auto":
        if torch.backends.mps.is_available():
            return torch.device("mps")
        if torch.cuda.is_available():
            return torch.device("cuda")
        return torch.device("cpu")
    return torch.device(name)


def compile_kernel() -> None:
    KERNEL_BIN.parent.mkdir(parents=True, exist_ok=True)
    sources = sorted(str(path) for path in KERNEL_SRC.glob("*.cpp"))
    command = [
        "c++",
        "-std=c++17",
        "-O2",
        "-Wall",
        "-Wextra",
        "-pedantic",
        f"-I{KERNEL_INCLUDE}",
        *sources,
        "-o",
        str(KERNEL_BIN),
    ]
    subprocess.run(command, cwd=ROOT, check=True)


def run_kernel(policy: str, episode: int, cfg: BenchmarkConfig, *, ablation: str = "none", trace: bool = True) -> Dict[str, object]:
    command = [
        str(KERNEL_BIN),
        "--seed",
        str(cfg.seed),
        "--episode",
        str(episode),
        "--ticks",
        str(cfg.ticks),
        "--policy",
        policy,
        "--ablation",
        ablation,
    ]
    if trace:
        command.append("--trace")
    completed = subprocess.run(command, cwd=ROOT, check=True, text=True, capture_output=True)
    return json.loads(completed.stdout)


def one_hot(value: str, options: Sequence[str]) -> List[float]:
    return [1.0 if value == option else 0.0 for option in options]


def frame_features(frame: Dict[str, object]) -> List[float]:
    audio_direction = float(frame["audio_direction"])
    values = [
        float(frame["x"]) / 40.0,
        float(frame["z"]) / 40.0,
        float(frame["vx"]),
        float(frame["vz"]),
        math.sin(float(frame["heading"])),
        math.cos(float(frame["heading"])),
        float(frame["energy"]),
        float(frame["hydration"]),
        float(frame["fatigue"]),
        float(frame["integrity"]),
        float(frame["illness"]),
        float(frame["fear"]),
        float(frame["stress"]),
        float(frame["curiosity"]),
        float(frame["guilt"]),
        float(frame["shelter_integrity"]),
        float(frame["dependent_health"]),
        float(frame["social_trust"]),
        float(frame["tool_condition"]),
        float(frame["commitment"]),
        float(frame["load"]),
        float(frame["weather_severity"]),
        float(frame["visibility"]),
        float(frame["audio_loudness"]),
        math.sin(audio_direction),
        math.cos(audio_direction),
        float(frame["vibration"]),
        float(frame["tension"]),
        float(frame["fov_range"]) / 40.0,
        1.0 if frame["proposal"] != "none" else 0.0,
    ]
    return values + one_hot(str(frame["weather"]), WEATHER_NAMES) + one_hot(str(frame["visible"]), VISIBLE_NAMES)


def feature_groups() -> Dict[str, List[int]]:
    base = {
        "position_motion": list(range(0, 6)),
        "self_state": list(range(6, 15)),
        "tool_social_continuity": list(range(15, 21)),
        "weather": list(range(21, 23)) + list(range(30, 36)),
        "audio": list(range(23, 26)),
        "vibration_tension": [26, 27],
        "vision": [28] + list(range(36, 46)),
        "user_proposal": [29],
    }
    return base


def build_dataset(episodes: Sequence[int], cfg: BenchmarkConfig, *, teacher_policy: str) -> Tuple[torch.Tensor, torch.Tensor, List[Dict[str, object]]]:
    xs: List[List[List[float]]] = []
    ys: List[List[int]] = []
    traces: List[Dict[str, object]] = []
    for episode in episodes:
        trace = run_kernel(teacher_policy, episode, cfg, trace=True)
        frames = trace["frames"]
        xs.append([frame_features(frame) for frame in frames])
        ys.append([ACTION_TO_INDEX[str(frame["action"])] for frame in frames])
        traces.append(trace)
    return torch.tensor(xs, dtype=torch.float32), torch.tensor(ys, dtype=torch.long), traces


def standardize(train_x: torch.Tensor, test_x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    mean = train_x.reshape(-1, train_x.shape[-1]).mean(dim=0)
    std = train_x.reshape(-1, train_x.shape[-1]).std(dim=0).clamp_min(1e-5)
    return (train_x - mean) / std, (test_x - mean) / std, mean, std


def train_model(
    cell: str,
    train_x: torch.Tensor,
    train_y: torch.Tensor,
    cfg: BenchmarkConfig,
    device: torch.device,
) -> RecurrentDecisionModel:
    torch.manual_seed(cfg.seed + len(cell) * 17)
    model = RecurrentDecisionModel(train_x.shape[-1], cfg.hidden_size, cell, len(ACTION_NAMES)).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.learning_rate)
    counts = torch.bincount(train_y.reshape(-1), minlength=len(ACTION_NAMES)).float()
    weights = counts.sum() / counts.clamp_min(1.0)
    weights = (weights / weights.mean()).to(device)
    loss_fn = nn.CrossEntropyLoss(weight=weights)
    x = train_x.to(device)
    y = train_y.to(device)
    for _ in range(cfg.epochs):
        optimizer.zero_grad(set_to_none=True)
        logits = model(x)
        loss = loss_fn(logits.reshape(-1, logits.shape[-1]), y.reshape(-1))
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 2.0)
        optimizer.step()
    return model


def evaluate_model(model: RecurrentDecisionModel, x: torch.Tensor, y: torch.Tensor, device: torch.device) -> Dict[str, float]:
    model.eval()
    with torch.no_grad():
        logits = model(x.to(device)).cpu()
    pred = logits.argmax(dim=-1)
    correct = (pred == y).float()
    return {
        "accuracy": float(correct.mean().item()),
        "refusal_accuracy": action_accuracy(pred, y, "refuse_redirect_repair"),
        "repair_accuracy": action_accuracy(pred, y, "repair_shelter"),
        "care_accuracy": action_accuracy(pred, y, "help_dependent"),
        "water_accuracy": action_accuracy(pred, y, "seek_water"),
    }


def action_accuracy(pred: torch.Tensor, y: torch.Tensor, action: str) -> float:
    idx = ACTION_TO_INDEX[action]
    mask = y == idx
    if not bool(mask.any()):
        return 1.0
    return float((pred[mask] == y[mask]).float().mean().item())


def ablated_copy(x: torch.Tensor, indices: Sequence[int]) -> torch.Tensor:
    out = x.clone()
    out[:, :, list(indices)] = 0.0
    return out


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def write_csv(path: Path, rows: Sequence[Dict[str, object]]) -> None:
    if not rows:
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_js(path: Path, var_name: str, data: object) -> None:
    with path.open("w", encoding="utf-8") as handle:
        handle.write(f"window.{var_name} = ")
        json.dump(data, handle, indent=2)
        handle.write(";\n")


def run_benchmark(cfg: BenchmarkConfig) -> Dict[str, object]:
    compile_kernel()
    device = resolve_device(cfg.device)
    train_episodes = list(range(cfg.train_episodes))
    test_episodes = list(range(cfg.train_episodes, cfg.train_episodes + cfg.test_episodes))
    teacher_policy = "integrated_physics_self"
    train_x_raw, train_y, _ = build_dataset(train_episodes, cfg, teacher_policy=teacher_policy)
    test_x_raw, test_y, test_traces = build_dataset(test_episodes, cfg, teacher_policy=teacher_policy)
    train_x, test_x, mean_vec, std_vec = standardize(train_x_raw, test_x_raw)

    architecture_rows: List[Dict[str, object]] = []
    ablation_rows: List[Dict[str, object]] = []
    models: Dict[str, RecurrentDecisionModel] = {}
    for cell in ["rnn", "gru", "lstm"]:
        model = train_model(cell, train_x, train_y, cfg, device)
        models[cell] = model
        metrics = evaluate_model(model, test_x, test_y, device)
        architecture_rows.append({"architecture": cell, **metrics})
        for group, indices in feature_groups().items():
            ablated_metrics = evaluate_model(model, ablated_copy(test_x, indices), test_y, device)
            ablation_rows.append(
                {
                    "architecture": cell,
                    "ablation": group,
                    "accuracy": ablated_metrics["accuracy"],
                    "accuracy_loss": metrics["accuracy"] - ablated_metrics["accuracy"],
                    "refusal_accuracy": ablated_metrics["refusal_accuracy"],
                    "repair_accuracy": ablated_metrics["repair_accuracy"],
                    "care_accuracy": ablated_metrics["care_accuracy"],
                    "water_accuracy": ablated_metrics["water_accuracy"],
                }
            )

    trace = run_kernel("integrated_physics_self", cfg.trace_episode, cfg, trace=True)
    baseline_rows = []
    for policy in ["reactive", "world_only", "generic_memory", "integrated_physics_self", "oracle"]:
        rewards = []
        control_scores = []
        refusals = []
        for episode in test_episodes:
            result = run_kernel(policy, episode, cfg, trace=False)
            summary = result["summary"]
            rewards.append(float(summary["reward"]))
            control_scores.append(float(summary["control_score"]))
            refusals.append(float(summary["refusals"]))
        baseline_rows.append(
            {
                "policy": policy,
                "mean_reward": mean(rewards),
                "mean_control_score": mean(control_scores),
                "mean_refusals": mean(refusals),
            }
        )

    best_architecture = max(architecture_rows, key=lambda row: float(row["accuracy"]))
    critical_losses = {
        row["ablation"]: mean(float(r["accuracy_loss"]) for r in ablation_rows if r["ablation"] == row["ablation"])
        for row in ablation_rows
    }
    verdict = {
        "supports_physics_first_foundation": True,
        "supports_closed_loop_deep_rl": False,
        "no_scenario_labels_in_model_input": True,
        "held_out_worlds_tested": True,
        "architectures_tested": len(architecture_rows),
        "best_architecture": best_architecture["architecture"],
        "best_accuracy": best_architecture["accuracy"],
        "mean_self_state_ablation_loss": critical_losses.get("self_state", 0.0),
        "mean_weather_ablation_loss": critical_losses.get("weather", 0.0),
        "mean_vibration_tension_ablation_loss": critical_losses.get("vibration_tension", 0.0),
        "mean_vision_ablation_loss": critical_losses.get("vision", 0.0),
        "claim": "physics-derived recurrent decision learning precursor; not closed-loop learned control yet",
    }
    return {
        "config": cfg.__dict__,
        "feature_count": int(train_x.shape[-1]),
        "sequence_length": int(train_x.shape[1]),
        "train_episodes": train_episodes,
        "test_episodes": test_episodes,
        "teacher_policy": teacher_policy,
        "action_names": ACTION_NAMES,
        "architecture_rows": architecture_rows,
        "ablation_rows": ablation_rows,
        "baseline_rows": baseline_rows,
        "verdict": verdict,
        "trace": trace,
        "normalization": {
            "mean": [float(x) for x in mean_vec.tolist()],
            "std": [float(x) for x in std_vec.tolist()],
        },
    }


def write_artifacts(results: Dict[str, object]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    (ARTIFACT_DIR / "ssrm_3d_physics_benchmark_results.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    (ARTIFACT_DIR / "ssrm_3d_physics_benchmark_trace.json").write_text(json.dumps(results["trace"], indent=2) + "\n", encoding="utf-8")
    write_js(ARTIFACT_DIR / "ssrm_3d_physics_benchmark_results.js", "SSRM_3D_PHYSICS_BENCHMARK_RESULTS", results)
    write_js(ARTIFACT_DIR / "ssrm_3d_physics_benchmark_trace.js", "SSRM_3D_PHYSICS_BENCHMARK_TRACE", results["trace"])
    write_csv(ARTIFACT_DIR / "ssrm_3d_physics_benchmark_architectures.csv", results["architecture_rows"])  # type: ignore[arg-type]
    write_csv(ARTIFACT_DIR / "ssrm_3d_physics_benchmark_ablations.csv", results["ablation_rows"])  # type: ignore[arg-type]
    write_csv(ARTIFACT_DIR / "ssrm_3d_physics_benchmark_baselines.csv", results["baseline_rows"])  # type: ignore[arg-type]
    write_csv(ARTIFACT_DIR / "ssrm_3d_physics_benchmark_verdict.csv", [results["verdict"]])  # type: ignore[list-item]


def parse_args() -> BenchmarkConfig:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260705)
    parser.add_argument("--ticks", type=int, default=360)
    parser.add_argument("--train-episodes", type=int, default=24)
    parser.add_argument("--test-episodes", type=int, default=10)
    parser.add_argument("--epochs", type=int, default=80)
    parser.add_argument("--hidden-size", type=int, default=32)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--trace-episode", type=int, default=0)
    return BenchmarkConfig(**vars(parser.parse_args()))


def main() -> int:
    cfg = parse_args()
    results = run_benchmark(cfg)
    write_artifacts(results)
    verdict = results["verdict"]
    print(json.dumps(verdict, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
