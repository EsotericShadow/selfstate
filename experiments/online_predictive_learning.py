#!/usr/bin/env python3
"""Online learned predictive-control experiment.

Agents receive no labels such as self, world, gain, wind, body, or actuator.
They only observe action/effect prediction error and update generic predictive
parameters. The experiment then probes whether learned latent state contains
agent-state information and whether ablating the action-dependent component
harms control.
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

from self_world_attribution import DriftWorld, choose_best_action, stable_episode_seed


@dataclass(frozen=True)
class OnlineConfig:
    episodes: int = 500
    max_action: int = 15
    calibration_steps: int = 14
    control_steps: int = 12
    target_abs: float = 30.0
    tolerance: float = 2.0
    seed: int = 20260530


@dataclass
class EpisodeResult:
    scenario: str
    model: str
    policy: str
    success: bool
    final_distance: float
    total_loss: float
    prediction_mae: float
    latent_gain: Optional[float]
    latent_bias: Optional[float]
    true_gain: float
    true_wind: float


class OnlineModel:
    name = "base"

    def reset(self, max_action: int) -> None:
        self.max_action = max_action

    def predict(self, action: int) -> float:
        raise NotImplementedError

    def update(self, action: int, actual_delta: float) -> None:
        raise NotImplementedError

    def latent(self) -> Tuple[Optional[float], Optional[float]]:
        return None, None


class BiasOnlyModel(OnlineModel):
    name = "bias_only_world"

    def reset(self, max_action: int) -> None:
        super().reset(max_action)
        self.bias = 0.0
        self.lr = 0.22

    def predict(self, action: int) -> float:
        return action + self.bias

    def update(self, action: int, actual_delta: float) -> None:
        error = actual_delta - self.predict(action)
        self.bias += self.lr * error

    def latent(self) -> Tuple[Optional[float], Optional[float]]:
        return 1.0, self.bias


class GainOnlyModel(OnlineModel):
    name = "gain_only_action_effect"

    def reset(self, max_action: int) -> None:
        super().reset(max_action)
        self.gain = 1.0
        self.lr = 0.018

    def predict(self, action: int) -> float:
        return self.gain * action

    def update(self, action: int, actual_delta: float) -> None:
        error = actual_delta - self.predict(action)
        self.gain += self.lr * error * normalized(action, self.max_action)

    def latent(self) -> Tuple[Optional[float], Optional[float]]:
        return self.gain, 0.0


class AffineOnlineModel(OnlineModel):
    name = "affine_predictive_state"

    def reset(self, max_action: int) -> None:
        super().reset(max_action)
        self.gain = 1.0
        self.bias = 0.0
        self.gain_lr = 0.018
        self.bias_lr = 0.22

    def predict(self, action: int) -> float:
        return self.gain * action + self.bias

    def update(self, action: int, actual_delta: float) -> None:
        error = actual_delta - self.predict(action)
        self.gain += self.gain_lr * error * normalized(action, self.max_action)
        self.bias += self.bias_lr * error

    def latent(self) -> Tuple[Optional[float], Optional[float]]:
        return self.gain, self.bias


class ActionTableOnlineModel(OnlineModel):
    name = "action_table_memory"

    def reset(self, max_action: int) -> None:
        super().reset(max_action)
        self.effects: Dict[int, float] = {}
        self.lr = 0.55

    def predict(self, action: int) -> float:
        if action in self.effects:
            return self.effects[action]
        if not self.effects:
            return float(action)
        nearest = min(self.effects, key=lambda known: (abs(known - action), known))
        return self.effects[nearest]

    def update(self, action: int, actual_delta: float) -> None:
        previous = self.predict(action)
        self.effects[action] = previous + self.lr * (actual_delta - previous)


def normalized(action: int, max_action: int) -> float:
    return action / max(1, max_action)


def calibration_actions(cfg: OnlineConfig, rng: random.Random) -> List[int]:
    anchors = [
        -cfg.max_action,
        cfg.max_action,
        0,
        -(cfg.max_action // 2),
        cfg.max_action // 2,
    ]
    actions = list(anchors)
    all_actions = list(range(-cfg.max_action, cfg.max_action + 1))
    while len(actions) < cfg.calibration_steps:
        actions.append(rng.choice(all_actions))
    return actions[: cfg.calibration_steps]


def post_perturb_world(scenario: str, seed: int) -> DriftWorld:
    rng = random.Random(seed)
    world = DriftWorld(scenario, rng)
    world.perturb()
    return world


def train_model(model: OnlineModel, scenario: str, episode: int, cfg: OnlineConfig) -> Tuple[float, float, float]:
    seed = stable_episode_seed(cfg.seed, scenario, episode)
    rng = random.Random(seed)
    world = post_perturb_world(scenario, seed)
    model.reset(cfg.max_action)
    errors = []
    for action in calibration_actions(cfg, rng):
        actual_delta = world.gain * action + world.wind
        predicted_delta = model.predict(action)
        errors.append(abs(actual_delta - predicted_delta))
        model.update(action, actual_delta)
    return world.gain, world.wind, statistics.fmean(errors)


def policy_prediction(model: OnlineModel, policy: str, action: int) -> float:
    gain, bias = model.latent()
    if policy == "full_model":
        return model.predict(action)
    if policy == "no_state_identity":
        return float(action)
    if policy == "action_component_ablation":
        return float(action) + (bias or 0.0)
    if policy == "bias_component_ablation":
        return (gain if gain is not None else 1.0) * action
    raise ValueError(f"unknown policy: {policy}")


def run_control(
    model: OnlineModel,
    scenario: str,
    episode: int,
    cfg: OnlineConfig,
    true_gain: float,
    true_wind: float,
    prediction_mae: float,
    policy: str,
) -> EpisodeResult:
    actions = list(range(-cfg.max_action, cfg.max_action + 1))
    position = 0.0
    target = cfg.target_abs
    total_loss = 0.0
    for _ in range(cfg.control_steps):
        action = choose_best_action(
            actions,
            position,
            target,
            lambda candidate: policy_prediction(model, policy, candidate),
        )
        position += true_gain * action + true_wind
        total_loss += abs(target - position) + 0.05 * abs(action)
    final_distance = abs(target - position)
    latent_gain, latent_bias = model.latent()
    return EpisodeResult(
        scenario=scenario,
        model=model.name,
        policy=policy,
        success=final_distance <= cfg.tolerance,
        final_distance=final_distance,
        total_loss=total_loss,
        prediction_mae=prediction_mae,
        latent_gain=latent_gain,
        latent_bias=latent_bias,
        true_gain=true_gain,
        true_wind=true_wind,
    )


def run_episode(model_factory, scenario: str, episode: int, cfg: OnlineConfig) -> List[EpisodeResult]:
    model = model_factory()
    true_gain, true_wind, prediction_mae = train_model(model, scenario, episode, cfg)
    policies = ["full_model", "no_state_identity"]
    if model.name in {"gain_only_action_effect", "affine_predictive_state"}:
        policies.append("action_component_ablation")
    if model.name in {"bias_only_world", "affine_predictive_state"}:
        policies.append("bias_component_ablation")
    return [
        run_control(model, scenario, episode, cfg, true_gain, true_wind, prediction_mae, policy)
        for policy in policies
    ]


def summarize(results: Sequence[EpisodeResult]) -> List[Dict[str, object]]:
    grouped: Dict[Tuple[str, str, str], List[EpisodeResult]] = {}
    for result in results:
        grouped.setdefault((result.scenario, result.model, result.policy), []).append(result)
    rows = []
    for (scenario, model, policy), items in sorted(grouped.items()):
        gain_errors = [
            abs(item.latent_gain - item.true_gain)
            for item in items
            if item.latent_gain is not None
        ]
        bias_errors = [
            abs(item.latent_bias - item.true_wind)
            for item in items
            if item.latent_bias is not None
        ]
        rows.append(
            {
                "scenario": scenario,
                "model": model,
                "policy": policy,
                "episodes": len(items),
                "success_rate": rate(item.success for item in items),
                "mean_final_distance": statistics.fmean(item.final_distance for item in items),
                "mean_total_loss": statistics.fmean(item.total_loss for item in items),
                "mean_prediction_mae": statistics.fmean(item.prediction_mae for item in items),
                "mean_gain_abs_error": mean_or_none(gain_errors),
                "mean_bias_abs_error": mean_or_none(bias_errors),
            }
        )
    return rows


def rate(values: Iterable[bool]) -> float:
    values = list(values)
    return sum(1 for value in values if value) / len(values)


def mean_or_none(values: Sequence[float]) -> Optional[float]:
    if not values:
        return None
    return statistics.fmean(values)


def write_outputs(rows: Sequence[Dict[str, object]], cfg: OnlineConfig, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "online_predictive_learning_results.json"
    csv_path = output_dir / "online_predictive_learning_summary.csv"

    with json_path.open("w", encoding="utf-8") as handle:
        json.dump({"config": asdict(cfg), "summary": list(rows)}, handle, indent=2)
        handle.write("\n")

    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def print_summary(rows: Sequence[Dict[str, object]]) -> None:
    columns = [
        "scenario",
        "model",
        "policy",
        "success_rate",
        "mean_final_distance",
        "mean_prediction_mae",
        "mean_gain_abs_error",
        "mean_bias_abs_error",
    ]
    widths = {
        column: max(len(column), *(len(format_value(row[column])) for row in rows))
        for column in columns
    }
    print(" | ".join(column.ljust(widths[column]) for column in columns))
    print("-+-".join("-" * widths[column] for column in columns))
    for row in rows:
        print(" | ".join(format_value(row[column]).ljust(widths[column]) for column in columns))


def format_value(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=OnlineConfig.episodes)
    parser.add_argument("--max-action", type=int, default=OnlineConfig.max_action)
    parser.add_argument("--calibration-steps", type=int, default=OnlineConfig.calibration_steps)
    parser.add_argument("--control-steps", type=int, default=OnlineConfig.control_steps)
    parser.add_argument("--seed", type=int, default=OnlineConfig.seed)
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = OnlineConfig(
        episodes=args.episodes,
        max_action=args.max_action,
        calibration_steps=args.calibration_steps,
        control_steps=args.control_steps,
        seed=args.seed,
    )
    scenarios = ["static_goal_switch", "world_drift", "self_drift", "mixed_hidden"]
    model_factories = [BiasOnlyModel, GainOnlyModel, AffineOnlineModel, ActionTableOnlineModel]
    results: List[EpisodeResult] = []
    for scenario in scenarios:
        for episode in range(cfg.episodes):
            for model_factory in model_factories:
                results.extend(run_episode(model_factory, scenario, episode, cfg))
    rows = summarize(results)
    write_outputs(rows, cfg, args.output_dir)
    print_summary(rows)


if __name__ == "__main__":
    main()
