#!/usr/bin/env python3
"""Representation-search test for self-state as compression.

This experiment does not give the learner labels such as "self" or "world".
It gives only action/effect samples after a hidden-state change and asks which
predictive representation is the most compact model of the data.

The decisive question is whether an adjustable action-effect variable, `gain`,
is selected when the agent's own actuator state changes, and not selected when a
fixed-body or world-only explanation is enough.
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

from self_world_attribution import DriftWorld, ExperimentConfig, stable_episode_seed


EPS = 1e-12


@dataclass(frozen=True)
class SearchConfig:
    episodes: int = 500
    calibration_samples: int = 8
    max_action: int = 15
    seed: int = 20260530


@dataclass
class FitResult:
    scenario: str
    episode: int
    model: str
    selected: bool
    train_bic: float
    train_mse: float
    test_mae: float
    k_params: int
    gain_hat: Optional[float]
    wind_hat: Optional[float]
    true_gain: float
    true_wind: float
    category: str


def action_grid(max_action: int) -> List[int]:
    return list(range(-max_action, max_action + 1))


def calibration_actions(cfg: SearchConfig, rng: random.Random) -> List[int]:
    actions = action_grid(cfg.max_action)
    anchors = [0, cfg.max_action, -cfg.max_action, cfg.max_action // 2, -(cfg.max_action // 2)]
    chosen = [action for action in anchors if action in actions]
    while len(chosen) < cfg.calibration_samples:
        chosen.append(rng.choice(actions))
    return chosen[: cfg.calibration_samples]


def post_perturb_state(scenario: str, seed: int) -> Tuple[float, float]:
    rng = random.Random(seed)
    world = DriftWorld(scenario, rng)
    world.perturb()
    return world.gain, world.wind


def deltas(actions: Sequence[int], gain: float, wind: float) -> List[float]:
    return [gain * action + wind for action in actions]


def mse(actual: Sequence[float], predicted: Sequence[float]) -> float:
    return statistics.fmean((y - y_hat) ** 2 for y, y_hat in zip(actual, predicted))


def mae(actual: Sequence[float], predicted: Sequence[float]) -> float:
    return statistics.fmean(abs(y - y_hat) for y, y_hat in zip(actual, predicted))


def bic(n: int, model_mse: float, k_params: int) -> float:
    return n * math.log(max(model_mse, EPS)) + k_params * math.log(n)


def fit_identity(train_actions: Sequence[int], train_y: Sequence[float]):
    return {"gain": 1.0, "wind": 0.0, "k": 0, "category": "no_self"}


def fit_world_bias(train_actions: Sequence[int], train_y: Sequence[float]):
    wind = statistics.fmean(y - action for action, y in zip(train_actions, train_y))
    return {"gain": 1.0, "wind": wind, "k": 1, "category": "world_only"}


def fit_self_gain(train_actions: Sequence[int], train_y: Sequence[float]):
    denominator = sum(action * action for action in train_actions)
    gain = 0.0 if denominator == 0 else sum(action * y for action, y in zip(train_actions, train_y)) / denominator
    return {"gain": gain, "wind": 0.0, "k": 1, "category": "self_equivalent"}


def fit_factorized_linear(train_actions: Sequence[int], train_y: Sequence[float]):
    xs = [float(action) for action in train_actions]
    ys = [float(y) for y in train_y]
    n = len(xs)
    sum_x = sum(xs)
    sum_y = sum(ys)
    sum_xx = sum(x * x for x in xs)
    sum_xy = sum(x * y for x, y in zip(xs, ys))
    denominator = n * sum_xx - sum_x * sum_x
    if abs(denominator) < EPS:
        gain = 1.0
        wind = statistics.fmean(ys) - gain * statistics.fmean(xs)
    else:
        gain = (n * sum_xy - sum_x * sum_y) / denominator
        wind = (sum_y - gain * sum_x) / n
    return {"gain": gain, "wind": wind, "k": 2, "category": "self_equivalent"}


def fit_action_memory(train_actions: Sequence[int], train_y: Sequence[float]):
    buckets: Dict[int, List[float]] = {}
    for action, y in zip(train_actions, train_y):
        buckets.setdefault(action, []).append(y)
    table = {action: statistics.fmean(values) for action, values in buckets.items()}
    return {"table": table, "k": len(table), "category": "implicit_action_memory"}


def predict_linear(params: Dict[str, object], actions: Sequence[int]) -> List[float]:
    gain = float(params["gain"])
    wind = float(params["wind"])
    return [gain * action + wind for action in actions]


def predict_action_memory(params: Dict[str, object], actions: Sequence[int]) -> List[float]:
    table = params["table"]
    assert isinstance(table, dict)
    known = sorted(table)
    fallback = statistics.fmean(table.values()) if table else 0.0
    predictions = []
    for action in actions:
        if action in table:
            predictions.append(float(table[action]))
            continue
        if not known:
            predictions.append(fallback)
            continue
        nearest = min(known, key=lambda known_action: (abs(known_action - action), known_action))
        predictions.append(float(table[nearest]))
    return predictions


MODEL_FITTERS = {
    "identity_fixed_body": fit_identity,
    "world_bias": fit_world_bias,
    "self_gain": fit_self_gain,
    "factorized_gain_wind": fit_factorized_linear,
    "action_memory": fit_action_memory,
}


def evaluate_model(
    model_name: str,
    params: Dict[str, object],
    train_actions: Sequence[int],
    train_y: Sequence[float],
    test_actions: Sequence[int],
    test_y: Sequence[float],
) -> Tuple[float, float, float]:
    if model_name == "action_memory":
        train_pred = predict_action_memory(params, train_actions)
        test_pred = predict_action_memory(params, test_actions)
    else:
        train_pred = predict_linear(params, train_actions)
        test_pred = predict_linear(params, test_actions)
    train_mse = mse(train_y, train_pred)
    train_bic = bic(len(train_y), train_mse, int(params["k"]))
    test_mae = mae(test_y, test_pred)
    return train_bic, train_mse, test_mae


def run_episode(scenario: str, episode: int, cfg: SearchConfig) -> List[FitResult]:
    seed = stable_episode_seed(cfg.seed, scenario, episode)
    rng = random.Random(seed)
    gain, wind = post_perturb_state(scenario, seed)
    train_actions = calibration_actions(cfg, rng)
    train_y = deltas(train_actions, gain, wind)
    test_actions = action_grid(cfg.max_action)
    test_y = deltas(test_actions, gain, wind)

    episode_results = []
    fitted = {}
    for model_name, fitter in MODEL_FITTERS.items():
        params = fitter(train_actions, train_y)
        train_bic, train_mse, test_mae = evaluate_model(
            model_name,
            params,
            train_actions,
            train_y,
            test_actions,
            test_y,
        )
        fitted[model_name] = (params, train_bic, train_mse, test_mae)

    selected_name = min(fitted, key=lambda name: (fitted[name][1], fitted[name][3], name))
    for model_name, (params, train_bic, train_mse, test_mae) in fitted.items():
        episode_results.append(
            FitResult(
                scenario=scenario,
                episode=episode,
                model=model_name,
                selected=model_name == selected_name,
                train_bic=train_bic,
                train_mse=train_mse,
                test_mae=test_mae,
                k_params=int(params["k"]),
                gain_hat=float(params["gain"]) if "gain" in params else None,
                wind_hat=float(params["wind"]) if "wind" in params else None,
                true_gain=gain,
                true_wind=wind,
                category=str(params["category"]),
            )
        )
    return episode_results


def summarize(results: Sequence[FitResult]) -> List[Dict[str, object]]:
    grouped: Dict[Tuple[str, str], List[FitResult]] = {}
    for result in results:
        grouped.setdefault((result.scenario, result.model), []).append(result)

    rows: List[Dict[str, object]] = []
    for (scenario, model), items in sorted(grouped.items()):
        gain_errors = [
            abs(item.gain_hat - item.true_gain)
            for item in items
            if item.gain_hat is not None
        ]
        wind_errors = [
            abs(item.wind_hat - item.true_wind)
            for item in items
            if item.wind_hat is not None
        ]
        rows.append(
            {
                "scenario": scenario,
                "model": model,
                "category": items[0].category,
                "episodes": len(items),
                "selection_rate": rate(item.selected for item in items),
                "mean_train_bic": statistics.fmean(item.train_bic for item in items),
                "mean_train_mse": statistics.fmean(item.train_mse for item in items),
                "mean_test_mae": statistics.fmean(item.test_mae for item in items),
                "mean_k_params": statistics.fmean(item.k_params for item in items),
                "mean_gain_abs_error": mean_or_none(gain_errors),
                "mean_wind_abs_error": mean_or_none(wind_errors),
            }
        )
    return rows


def summarize_categories(results: Sequence[FitResult]) -> List[Dict[str, object]]:
    selected = [result for result in results if result.selected]
    grouped: Dict[Tuple[str, str], List[FitResult]] = {}
    for result in selected:
        grouped.setdefault((result.scenario, result.category), []).append(result)

    scenarios = sorted({result.scenario for result in results})
    categories = sorted({result.category for result in results})
    rows: List[Dict[str, object]] = []
    for scenario in scenarios:
        scenario_total = sum(1 for result in selected if result.scenario == scenario)
        for category in categories:
            items = grouped.get((scenario, category), [])
            rows.append(
                {
                    "scenario": scenario,
                    "category": category,
                    "selected_episodes": len(items),
                    "selection_rate": len(items) / scenario_total if scenario_total else 0.0,
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


def write_outputs(
    model_rows: Sequence[Dict[str, object]],
    category_rows: Sequence[Dict[str, object]],
    cfg: SearchConfig,
    output_dir: Path,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "representation_search_results.json"
    model_csv_path = output_dir / "representation_search_model_summary.csv"
    category_csv_path = output_dir / "representation_search_category_summary.csv"

    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "model_summary": list(model_rows),
                "category_summary": list(category_rows),
            },
            handle,
            indent=2,
        )
        handle.write("\n")

    with model_csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(model_rows[0].keys()))
        writer.writeheader()
        writer.writerows(model_rows)

    with category_csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(category_rows[0].keys()))
        writer.writeheader()
        writer.writerows(category_rows)


def print_model_summary(rows: Sequence[Dict[str, object]]) -> None:
    columns = [
        "scenario",
        "model",
        "category",
        "selection_rate",
        "mean_test_mae",
        "mean_gain_abs_error",
        "mean_wind_abs_error",
    ]
    print_table(rows, columns)


def print_table(rows: Sequence[Dict[str, object]], columns: Sequence[str]) -> None:
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
    parser.add_argument("--episodes", type=int, default=SearchConfig.episodes)
    parser.add_argument("--calibration-samples", type=int, default=SearchConfig.calibration_samples)
    parser.add_argument("--max-action", type=int, default=SearchConfig.max_action)
    parser.add_argument("--seed", type=int, default=SearchConfig.seed)
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = SearchConfig(
        episodes=args.episodes,
        calibration_samples=args.calibration_samples,
        max_action=args.max_action,
        seed=args.seed,
    )
    scenarios = ["static_goal_switch", "world_drift", "self_drift", "mixed_hidden"]
    results: List[FitResult] = []
    for scenario in scenarios:
        for episode in range(cfg.episodes):
            results.extend(run_episode(scenario, episode, cfg))

    model_rows = summarize(results)
    category_rows = summarize_categories(results)
    write_outputs(model_rows, category_rows, cfg, args.output_dir)
    print_model_summary(model_rows)
    print()
    print_table(category_rows, ["scenario", "category", "selection_rate"])


if __name__ == "__main__":
    main()
