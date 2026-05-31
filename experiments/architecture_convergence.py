#!/usr/bin/env python3
"""Architecture-convergence test for self-equivalent action state.

Learners receive only action/effect samples. They are not given labels such as
self, world, body, actuator, gain, or wind. Several predictor families then
compete on prediction and control. After training, the analysis probes whether
the learned prediction function contains a causally necessary action-effect
component.

This is still a toy linear environment. Its purpose is narrower: test whether
multiple independent unlabeled learner families converge on an action-mediated
agent-state component when self drift is the pressure, and not when a world-only
explanation is enough.
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
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Tuple

from self_world_attribution import DriftWorld, choose_best_action, stable_episode_seed


ARTIFACT_DIR = Path("artifacts")
EPS = 1e-12
COMPONENT_LOSS_THRESHOLD = 5.0


@dataclass(frozen=True)
class ConvergenceConfig:
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
    effective_slope: float
    effective_bias: float
    true_gain: float
    true_wind: float


class Predictor:
    name = "base"
    parameter_count = 0

    def reset(self, cfg: ConvergenceConfig, rng: random.Random) -> None:
        self.cfg = cfg
        self.rng = rng

    def update(self, action: int, effect: float) -> None:
        raise NotImplementedError

    def predict(self, action: int) -> float:
        raise NotImplementedError

    def effective_components(self) -> Tuple[float, float]:
        max_action = self.cfg.max_action
        slope = (self.predict(max_action) - self.predict(-max_action)) / (2 * max_action)
        bias = self.predict(0)
        return slope, bias


class MeanDeltaLearner(Predictor):
    name = "mean_delta_memory"
    parameter_count = 1

    def reset(self, cfg: ConvergenceConfig, rng: random.Random) -> None:
        super().reset(cfg, rng)
        self.mean = 0.0
        self.count = 0

    def update(self, action: int, effect: float) -> None:
        self.count += 1
        self.mean += (effect - self.mean) / self.count

    def predict(self, action: int) -> float:
        return self.mean if self.count else float(action)


class BiasSgdLearner(Predictor):
    name = "bias_sgd_world"
    parameter_count = 1

    def reset(self, cfg: ConvergenceConfig, rng: random.Random) -> None:
        super().reset(cfg, rng)
        self.bias = 0.0
        self.lr = 0.22

    def update(self, action: int, effect: float) -> None:
        error = effect - self.predict(action)
        self.bias += self.lr * error

    def predict(self, action: int) -> float:
        return action + self.bias


class GainSgdLearner(Predictor):
    name = "gain_sgd_action_effect"
    parameter_count = 1

    def reset(self, cfg: ConvergenceConfig, rng: random.Random) -> None:
        super().reset(cfg, rng)
        self.gain = 1.0
        self.lr = 0.018

    def update(self, action: int, effect: float) -> None:
        error = effect - self.predict(action)
        self.gain += self.lr * error * normalized(action, self.cfg.max_action)

    def predict(self, action: int) -> float:
        return self.gain * action


class AffineSgdLearner(Predictor):
    name = "affine_sgd_predictive_state"
    parameter_count = 2

    def reset(self, cfg: ConvergenceConfig, rng: random.Random) -> None:
        super().reset(cfg, rng)
        self.gain = 1.0
        self.bias = 0.0
        self.gain_lr = 0.018
        self.bias_lr = 0.22

    def update(self, action: int, effect: float) -> None:
        error = effect - self.predict(action)
        self.gain += self.gain_lr * error * normalized(action, self.cfg.max_action)
        self.bias += self.bias_lr * error

    def predict(self, action: int) -> float:
        return self.gain * action + self.bias


class LeastSquaresLearner(Predictor):
    name = "least_squares_predictive_state"
    parameter_count = 2

    def reset(self, cfg: ConvergenceConfig, rng: random.Random) -> None:
        super().reset(cfg, rng)
        self.samples: List[Tuple[float, float]] = []
        self.gain = 1.0
        self.bias = 0.0

    def update(self, action: int, effect: float) -> None:
        self.samples.append((float(action), float(effect)))
        self._fit()

    def _fit(self) -> None:
        if len(self.samples) < 2:
            self.gain = 1.0
            self.bias = self.samples[0][1] - self.samples[0][0] if self.samples else 0.0
            return
        xs = [sample[0] for sample in self.samples]
        ys = [sample[1] for sample in self.samples]
        n = len(xs)
        sum_x = sum(xs)
        sum_y = sum(ys)
        sum_xx = sum(x * x for x in xs)
        sum_xy = sum(x * y for x, y in self.samples)
        denominator = n * sum_xx - sum_x * sum_x
        if abs(denominator) < EPS:
            self.gain = 1.0
            self.bias = statistics.fmean(ys) - self.gain * statistics.fmean(xs)
            return
        self.gain = (n * sum_xy - sum_x * sum_y) / denominator
        self.bias = (sum_y - self.gain * sum_x) / n

    def predict(self, action: int) -> float:
        return self.gain * action + self.bias


class SymmetricProbeLearner(Predictor):
    name = "symmetric_probe_predictive_state"
    parameter_count = 2

    def reset(self, cfg: ConvergenceConfig, rng: random.Random) -> None:
        super().reset(cfg, rng)
        self.samples: Dict[int, List[float]] = {}

    def update(self, action: int, effect: float) -> None:
        self.samples.setdefault(action, []).append(effect)

    def predict(self, action: int) -> float:
        max_action = self.cfg.max_action
        pos = mean_sample(self.samples.get(max_action))
        neg = mean_sample(self.samples.get(-max_action))
        zero = mean_sample(self.samples.get(0))
        if pos is not None and neg is not None:
            gain = (pos - neg) / (2 * max_action)
            bias = zero if zero is not None else (pos + neg) / 2
            return gain * action + bias
        if zero is not None:
            return action + zero
        return float(action)


class ActionTableLearner(Predictor):
    name = "action_table_memory"
    parameter_count = 14

    def reset(self, cfg: ConvergenceConfig, rng: random.Random) -> None:
        super().reset(cfg, rng)
        self.effects: Dict[int, float] = {}
        self.counts: Dict[int, int] = {}

    def update(self, action: int, effect: float) -> None:
        count = self.counts.get(action, 0) + 1
        previous = self.effects.get(action, float(action))
        self.effects[action] = previous + (effect - previous) / count
        self.counts[action] = count

    def predict(self, action: int) -> float:
        if action in self.effects:
            return self.effects[action]
        if not self.effects:
            return float(action)
        nearest = min(self.effects, key=lambda known: (abs(known - action), known))
        return self.effects[nearest]


class RandomFeatureLearner(Predictor):
    name = "random_feature_predictive_state"
    parameter_count = 8

    def reset(self, cfg: ConvergenceConfig, rng: random.Random) -> None:
        super().reset(cfg, rng)
        self.feature_params = [(rng.uniform(-2.5, 2.5), rng.uniform(-1.0, 1.0)) for _ in range(6)]
        self.weights = [0.0 for _ in range(8)]
        self.lr = 0.08

    def features(self, action: int) -> List[float]:
        x = normalized(action, self.cfg.max_action)
        values = [1.0, x]
        values.extend(math.tanh(weight * x + bias) for weight, bias in self.feature_params)
        return values

    def update(self, action: int, effect: float) -> None:
        prediction = self.predict(action)
        error = effect - prediction
        features = self.features(action)
        norm = sum(value * value for value in features) + 1.0
        for index, value in enumerate(features):
            self.weights[index] += self.lr * error * value / norm

    def predict(self, action: int) -> float:
        features = self.features(action)
        return sum(weight * value for weight, value in zip(self.weights, features))


def mean_sample(values: Optional[Sequence[float]]) -> Optional[float]:
    if not values:
        return None
    return statistics.fmean(values)


def normalized(action: int, max_action: int) -> float:
    return action / max(1, max_action)


def calibration_actions(cfg: ConvergenceConfig, rng: random.Random) -> List[int]:
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


def train_model(
    model_factory: Callable[[], Predictor],
    scenario: str,
    episode: int,
    cfg: ConvergenceConfig,
) -> Tuple[Predictor, float, float, float]:
    seed = stable_episode_seed(cfg.seed, scenario, episode)
    rng = random.Random(seed)
    model = model_factory()
    model.reset(cfg, random.Random(seed + 17))
    world = post_perturb_world(scenario, seed)
    errors = []
    for action in calibration_actions(cfg, rng):
        effect = world.gain * action + world.wind
        errors.append(abs(effect - model.predict(action)))
        model.update(action, effect)
    return model, world.gain, world.wind, statistics.fmean(errors)


def prediction_for_policy(model: Predictor, policy: str, action: int) -> float:
    slope, bias = model.effective_components()
    if policy == "full_model":
        return model.predict(action)
    if policy == "identity_no_state":
        return float(action)
    if policy == "action_component_ablation":
        return float(action) + bias
    if policy == "bias_component_ablation":
        return slope * action
    raise ValueError(f"unknown policy: {policy}")


def prediction_mae(model: Predictor, true_gain: float, true_wind: float, cfg: ConvergenceConfig) -> float:
    actions = list(range(-cfg.max_action, cfg.max_action + 1))
    return statistics.fmean(
        abs(model.predict(action) - (true_gain * action + true_wind))
        for action in actions
    )


def run_control(
    model: Predictor,
    scenario: str,
    policy: str,
    cfg: ConvergenceConfig,
    true_gain: float,
    true_wind: float,
    test_mae: float,
) -> EpisodeResult:
    actions = list(range(-cfg.max_action, cfg.max_action + 1))
    position = 0.0
    total_loss = 0.0
    for _ in range(cfg.control_steps):
        action = choose_best_action(
            actions,
            position,
            cfg.target_abs,
            lambda candidate: prediction_for_policy(model, policy, candidate),
        )
        position += true_gain * action + true_wind
        total_loss += abs(cfg.target_abs - position) + 0.05 * abs(action)
    final_distance = abs(cfg.target_abs - position)
    slope, bias = model.effective_components()
    return EpisodeResult(
        scenario=scenario,
        model=model.name,
        policy=policy,
        success=final_distance <= cfg.tolerance,
        final_distance=final_distance,
        total_loss=total_loss,
        prediction_mae=test_mae,
        effective_slope=slope,
        effective_bias=bias,
        true_gain=true_gain,
        true_wind=true_wind,
    )


def run_episode(
    model_factory: Callable[[], Predictor],
    scenario: str,
    episode: int,
    cfg: ConvergenceConfig,
) -> List[EpisodeResult]:
    model, true_gain, true_wind, _train_mae = train_model(model_factory, scenario, episode, cfg)
    test_mae = prediction_mae(model, true_gain, true_wind, cfg)
    policies = [
        "full_model",
        "identity_no_state",
        "action_component_ablation",
        "bias_component_ablation",
    ]
    return [
        run_control(model, scenario, policy, cfg, true_gain, true_wind, test_mae)
        for policy in policies
    ]


def summarize(results: Sequence[EpisodeResult]) -> List[Dict[str, object]]:
    grouped: Dict[Tuple[str, str, str], List[EpisodeResult]] = {}
    for result in results:
        grouped.setdefault((result.scenario, result.model, result.policy), []).append(result)
    rows = []
    for (scenario, model, policy), items in sorted(grouped.items()):
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
                "mean_effective_slope": statistics.fmean(item.effective_slope for item in items),
                "mean_effective_bias": statistics.fmean(item.effective_bias for item in items),
                "mean_slope_abs_error": statistics.fmean(abs(item.effective_slope - item.true_gain) for item in items),
                "mean_bias_abs_error": statistics.fmean(abs(item.effective_bias - item.true_wind) for item in items),
            }
        )
    return rows


def convergence_verdict(summary_rows: Sequence[Dict[str, object]]) -> List[Dict[str, object]]:
    by_scenario_model: Dict[Tuple[str, str], Dict[str, Dict[str, object]]] = {}
    for row in summary_rows:
        by_scenario_model.setdefault((str(row["scenario"]), str(row["model"])), {})[str(row["policy"])] = row

    scenario_rows: Dict[str, List[Dict[str, object]]] = {}
    for (scenario, model), policies in by_scenario_model.items():
        full = policies["full_model"]
        action_ablation = policies["action_component_ablation"]
        bias_ablation = policies["bias_component_ablation"]
        scenario_rows.setdefault(scenario, []).append(
            {
                "scenario": scenario,
                "model": model,
                "full_loss": float(full["mean_total_loss"]),
                "action_ablation_loss_delta": float(action_ablation["mean_total_loss"]) - float(full["mean_total_loss"]),
                "bias_ablation_loss_delta": float(bias_ablation["mean_total_loss"]) - float(full["mean_total_loss"]),
                "full_success_rate": float(full["success_rate"]),
                "mean_slope_abs_error": float(full["mean_slope_abs_error"]),
                "mean_bias_abs_error": float(full["mean_bias_abs_error"]),
            }
        )

    verdict_rows = []
    for scenario, rows in sorted(scenario_rows.items()):
        ranked = sorted(rows, key=lambda row: (row["full_loss"], -row["full_success_rate"], row["model"]))
        top_rows = ranked[:3]
        action_models = [
            row for row in top_rows if row["action_ablation_loss_delta"] > COMPONENT_LOSS_THRESHOLD
        ]
        bias_models = [
            row for row in top_rows if row["bias_ablation_loss_delta"] > COMPONENT_LOSS_THRESHOLD
        ]
        verdict_rows.append(
            {
                "scenario": scenario,
                "top_models": ";".join(row["model"] for row in top_rows),
                "top_action_component_count": len(action_models),
                "top_bias_component_count": len(bias_models),
                "best_full_loss": ranked[0]["full_loss"],
                "best_full_success_rate": ranked[0]["full_success_rate"],
                "best_action_ablation_loss_delta": ranked[0]["action_ablation_loss_delta"],
                "best_bias_ablation_loss_delta": ranked[0]["bias_ablation_loss_delta"],
                "expected_self_pressure": scenario in {"self_drift", "mixed_hidden"},
                "expected_world_pressure": scenario in {"world_drift", "mixed_hidden"},
                "supports_boundary": supports_boundary(scenario, action_models, bias_models),
            }
        )
    return verdict_rows


def supports_boundary(scenario: str, action_models: Sequence[object], bias_models: Sequence[object]) -> bool:
    has_action = len(action_models) > 0
    has_bias = len(bias_models) > 0
    if scenario == "static_goal_switch":
        return not has_action and not has_bias
    if scenario == "world_drift":
        return not has_action and has_bias
    if scenario == "self_drift":
        return has_action and not has_bias
    if scenario == "mixed_hidden":
        return has_action and has_bias
    return False


def rate(values: Iterable[bool]) -> float:
    values = list(values)
    return sum(1 for value in values if value) / len(values)


def write_csv(path: Path, rows: Sequence[Dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_outputs(
    summary_rows: Sequence[Dict[str, object]],
    verdict_rows: Sequence[Dict[str, object]],
    cfg: ConvergenceConfig,
    output_dir: Path,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    summary_path = output_dir / "architecture_convergence_summary.csv"
    verdict_path = output_dir / "architecture_convergence_verdict.csv"
    json_path = output_dir / "architecture_convergence_results.json"
    write_csv(summary_path, summary_rows)
    write_csv(verdict_path, verdict_rows)
    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "summary": list(summary_rows),
                "verdict": list(verdict_rows),
            },
            handle,
            indent=2,
        )
        handle.write("\n")
    print(f"wrote {summary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {json_path}")


def print_verdict(rows: Sequence[Dict[str, object]]) -> None:
    columns = [
        "scenario",
        "top_models",
        "top_action_component_count",
        "top_bias_component_count",
        "supports_boundary",
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
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=ConvergenceConfig.episodes)
    parser.add_argument("--max-action", type=int, default=ConvergenceConfig.max_action)
    parser.add_argument("--calibration-steps", type=int, default=ConvergenceConfig.calibration_steps)
    parser.add_argument("--control-steps", type=int, default=ConvergenceConfig.control_steps)
    parser.add_argument("--seed", type=int, default=ConvergenceConfig.seed)
    parser.add_argument("--output-dir", type=Path, default=ARTIFACT_DIR)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cfg = ConvergenceConfig(
        episodes=args.episodes,
        max_action=args.max_action,
        calibration_steps=args.calibration_steps,
        control_steps=args.control_steps,
        seed=args.seed,
    )
    scenarios = ["static_goal_switch", "world_drift", "self_drift", "mixed_hidden"]
    model_factories: List[Callable[[], Predictor]] = [
        MeanDeltaLearner,
        BiasSgdLearner,
        GainSgdLearner,
        AffineSgdLearner,
        LeastSquaresLearner,
        SymmetricProbeLearner,
        ActionTableLearner,
        RandomFeatureLearner,
    ]
    results: List[EpisodeResult] = []
    for scenario in scenarios:
        for episode in range(cfg.episodes):
            for model_factory in model_factories:
                results.extend(run_episode(model_factory, scenario, episode, cfg))
    summary_rows = summarize(results)
    verdict_rows = convergence_verdict(summary_rows)
    write_outputs(summary_rows, verdict_rows, cfg, args.output_dir)
    print_verdict(verdict_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
