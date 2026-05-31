#!/usr/bin/env python3
"""Predictive-state emergence test.

The learner is not given variables called self, world, gain, or wind. It only
learns a predictive state: expected effects for counterfactual actions.

After learning, probes ask whether hidden agent-state (`gain`) and external
state (`wind`) are decodable from that predictive state, and causal ablations
ask whether the action-effect component is necessary for control.
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

from self_world_attribution import DriftWorld, stable_episode_seed


EPS = 1e-9


@dataclass(frozen=True)
class PredictiveStateConfig:
    episodes: int = 500
    max_action: int = 15
    calibration_samples: int = 7
    control_horizon: int = 10
    target_abs: float = 30.0
    tolerance: float = 2.0
    action_cost: float = 0.05
    seed: int = 20260530


@dataclass
class EpisodeState:
    scenario: str
    episode: int
    true_gain: float
    true_wind: float
    train_actions: List[int]
    train_deltas: List[float]
    predicted_effects: List[float]


@dataclass
class ProbeResult:
    scenario: str
    latent: str
    target: str
    train_episodes: int
    test_episodes: int
    test_mae: float
    test_r2: Optional[float]
    baseline_mae: float


@dataclass
class ControlResult:
    scenario: str
    policy: str
    success: bool
    final_distance: float
    total_loss: float


def action_grid(max_action: int) -> List[int]:
    return list(range(-max_action, max_action + 1))


def post_perturb_state(scenario: str, seed: int) -> Tuple[float, float]:
    rng = random.Random(seed)
    world = DriftWorld(scenario, rng)
    world.perturb()
    return world.gain, world.wind


def calibration_actions(cfg: PredictiveStateConfig, rng: random.Random) -> List[int]:
    anchors = [
        -cfg.max_action,
        0,
        cfg.max_action,
        -(cfg.max_action // 2),
        cfg.max_action // 2,
    ]
    actions = action_grid(cfg.max_action)
    chosen = [action for action in anchors if action in actions]
    while len(chosen) < cfg.calibration_samples:
        candidate = rng.choice(actions)
        if candidate not in chosen:
            chosen.append(candidate)
    return chosen[: cfg.calibration_samples]


def learn_predictive_state(
    train_actions: Sequence[int],
    train_deltas: Sequence[float],
    all_actions: Sequence[int],
) -> List[float]:
    """Return predicted effects for every action in `all_actions`.

    This is deliberately represented as counterfactual predictions, not as
    named gain/wind variables. Linear interpolation is enough for the current
    toy environment and makes the latent state easy to inspect.
    """
    pairs = sorted(zip(train_actions, train_deltas), key=lambda pair: pair[0])
    predictions = []
    for action in all_actions:
        predictions.append(interpolate_effect(action, pairs))
    return predictions


def interpolate_effect(action: int, pairs: Sequence[Tuple[int, float]]) -> float:
    for known_action, known_delta in pairs:
        if action == known_action:
            return known_delta

    lower = None
    upper = None
    for known_action, known_delta in pairs:
        if known_action < action:
            lower = (known_action, known_delta)
        elif known_action > action and upper is None:
            upper = (known_action, known_delta)
            break

    if lower is None:
        a0, y0 = pairs[0]
        a1, y1 = pairs[1]
    elif upper is None:
        a0, y0 = pairs[-2]
        a1, y1 = pairs[-1]
    else:
        a0, y0 = lower
        a1, y1 = upper

    if a1 == a0:
        return y0
    weight = (action - a0) / (a1 - a0)
    return y0 + weight * (y1 - y0)


def run_episode(scenario: str, episode: int, cfg: PredictiveStateConfig) -> EpisodeState:
    seed = stable_episode_seed(cfg.seed, scenario, episode)
    rng = random.Random(seed)
    gain, wind = post_perturb_state(scenario, seed)
    actions = calibration_actions(cfg, rng)
    deltas = [gain * action + wind for action in actions]
    predicted_effects = learn_predictive_state(actions, deltas, action_grid(cfg.max_action))
    return EpisodeState(
        scenario=scenario,
        episode=episode,
        true_gain=gain,
        true_wind=wind,
        train_actions=actions,
        train_deltas=deltas,
        predicted_effects=predicted_effects,
    )


def latent_vector(state: EpisodeState, latent_name: str, cfg: PredictiveStateConfig) -> List[float]:
    actions = action_grid(cfg.max_action)
    if latent_name == "constant":
        return []
    if latent_name == "mean_effect":
        return [statistics.fmean(state.predicted_effects)]
    if latent_name == "three_predictions":
        wanted = [-cfg.max_action, 0, cfg.max_action]
        return [state.predicted_effects[actions.index(action)] for action in wanted]
    if latent_name == "full_predictions":
        return list(state.predicted_effects)
    raise ValueError(f"unknown latent: {latent_name}")


def fit_linear_probe(xs: Sequence[Sequence[float]], ys: Sequence[float]) -> List[float]:
    if not xs:
        return [statistics.fmean(ys)]

    width = len(xs[0]) + 1
    xtx = [[0.0 for _ in range(width)] for _ in range(width)]
    xty = [0.0 for _ in range(width)]
    for x, y in zip(xs, ys):
        row = [1.0, *x]
        for i in range(width):
            xty[i] += row[i] * y
            for j in range(width):
                xtx[i][j] += row[i] * row[j]

    ridge = 1e-6
    for i in range(1, width):
        xtx[i][i] += ridge
    return solve_linear_system(xtx, xty)


def solve_linear_system(matrix: Sequence[Sequence[float]], vector: Sequence[float]) -> List[float]:
    n = len(vector)
    augmented = [list(row) + [vector[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda row: abs(augmented[row][col]))
        if abs(augmented[pivot][col]) < EPS:
            augmented[col][col] += EPS
            pivot = col
        augmented[col], augmented[pivot] = augmented[pivot], augmented[col]
        divisor = augmented[col][col]
        augmented[col] = [value / divisor for value in augmented[col]]
        for row in range(n):
            if row == col:
                continue
            factor = augmented[row][col]
            augmented[row] = [
                value - factor * pivot_value
                for value, pivot_value in zip(augmented[row], augmented[col])
            ]
    return [row[-1] for row in augmented]


def predict_probe(weights: Sequence[float], x: Sequence[float]) -> float:
    return weights[0] + sum(weight * value for weight, value in zip(weights[1:], x))


def score_probe(actual: Sequence[float], predicted: Sequence[float]) -> Tuple[float, Optional[float]]:
    test_mae = statistics.fmean(abs(y - y_hat) for y, y_hat in zip(actual, predicted))
    mean_y = statistics.fmean(actual)
    total = sum((y - mean_y) ** 2 for y in actual)
    if total < EPS:
        return test_mae, None
    residual = sum((y - y_hat) ** 2 for y, y_hat in zip(actual, predicted))
    return test_mae, 1.0 - residual / total


def run_probes(states: Sequence[EpisodeState], cfg: PredictiveStateConfig) -> List[ProbeResult]:
    results: List[ProbeResult] = []
    latents = ["constant", "mean_effect", "three_predictions", "full_predictions"]
    targets = ["true_gain", "true_wind"]
    scenarios = sorted({state.scenario for state in states})

    for scenario in scenarios:
        scenario_states = [state for state in states if state.scenario == scenario]
        split = max(1, int(len(scenario_states) * 0.8))
        train_states = scenario_states[:split]
        test_states = scenario_states[split:]
        if not test_states:
            continue

        for target in targets:
            train_y = [getattr(state, target) for state in train_states]
            test_y = [getattr(state, target) for state in test_states]
            baseline = statistics.fmean(train_y)
            baseline_mae = statistics.fmean(abs(y - baseline) for y in test_y)

            for latent in latents:
                train_x = [latent_vector(state, latent, cfg) for state in train_states]
                test_x = [latent_vector(state, latent, cfg) for state in test_states]
                weights = fit_linear_probe(train_x, train_y)
                predicted = [predict_probe(weights, x) for x in test_x]
                test_mae, test_r2 = score_probe(test_y, predicted)
                results.append(
                    ProbeResult(
                        scenario=scenario,
                        latent=latent,
                        target=target,
                        train_episodes=len(train_states),
                        test_episodes=len(test_states),
                        test_mae=test_mae,
                        test_r2=test_r2,
                        baseline_mae=baseline_mae,
                    )
                )
    return results


def decompose_prediction_vector(predicted_effects: Sequence[float], cfg: PredictiveStateConfig) -> Tuple[float, float]:
    actions = action_grid(cfg.max_action)
    xs = [float(action) for action in actions]
    ys = [float(value) for value in predicted_effects]
    n = len(xs)
    sum_x = sum(xs)
    sum_y = sum(ys)
    sum_xx = sum(x * x for x in xs)
    sum_xy = sum(x * y for x, y in zip(xs, ys))
    denominator = n * sum_xx - sum_x * sum_x
    if abs(denominator) < EPS:
        return 1.0, statistics.fmean(ys)
    slope = (n * sum_xy - sum_x * sum_y) / denominator
    intercept = (sum_y - slope * sum_x) / n
    return slope, intercept


def policy_predictions(state: EpisodeState, policy: str, cfg: PredictiveStateConfig) -> List[float]:
    actions = action_grid(cfg.max_action)
    slope, intercept = decompose_prediction_vector(state.predicted_effects, cfg)
    if policy == "full_predictive_state":
        return list(state.predicted_effects)
    if policy == "no_state_identity":
        return [float(action) for action in actions]
    if policy == "self_component_ablation":
        return [float(action) + intercept for action in actions]
    if policy == "world_component_ablation":
        return [slope * action for action in actions]
    raise ValueError(f"unknown policy: {policy}")


def run_control(state: EpisodeState, policy: str, cfg: PredictiveStateConfig) -> ControlResult:
    actions = action_grid(cfg.max_action)
    predicted = policy_predictions(state, policy, cfg)
    position = 0.0
    target = cfg.target_abs
    total_loss = 0.0
    for _step in range(cfg.control_horizon):
        action = min(
            actions,
            key=lambda candidate: (
                abs(target - (position + predicted[actions.index(candidate)])),
                abs(candidate),
                candidate,
            ),
        )
        position += state.true_gain * action + state.true_wind
        total_loss += abs(target - position) + cfg.action_cost * abs(action)
    final_distance = abs(target - position)
    return ControlResult(
        scenario=state.scenario,
        policy=policy,
        success=final_distance <= cfg.tolerance,
        final_distance=final_distance,
        total_loss=total_loss,
    )


def run_controls(states: Sequence[EpisodeState], cfg: PredictiveStateConfig) -> List[ControlResult]:
    policies = [
        "no_state_identity",
        "self_component_ablation",
        "world_component_ablation",
        "full_predictive_state",
    ]
    return [run_control(state, policy, cfg) for state in states for policy in policies]


def summarize_probes(results: Sequence[ProbeResult]) -> List[Dict[str, object]]:
    return [asdict(result) for result in results]


def summarize_controls(results: Sequence[ControlResult]) -> List[Dict[str, object]]:
    grouped: Dict[Tuple[str, str], List[ControlResult]] = {}
    for result in results:
        grouped.setdefault((result.scenario, result.policy), []).append(result)
    rows = []
    for (scenario, policy), items in sorted(grouped.items()):
        rows.append(
            {
                "scenario": scenario,
                "policy": policy,
                "episodes": len(items),
                "success_rate": rate(item.success for item in items),
                "mean_final_distance": statistics.fmean(item.final_distance for item in items),
                "mean_total_loss": statistics.fmean(item.total_loss for item in items),
            }
        )
    return rows


def rate(values: Iterable[bool]) -> float:
    values = list(values)
    return sum(1 for value in values if value) / len(values)


def write_outputs(
    probe_rows: Sequence[Dict[str, object]],
    control_rows: Sequence[Dict[str, object]],
    cfg: PredictiveStateConfig,
    output_dir: Path,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "predictive_state_emergence_results.json"
    probe_csv_path = output_dir / "predictive_state_probe_summary.csv"
    control_csv_path = output_dir / "predictive_state_control_summary.csv"

    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "probe_summary": list(probe_rows),
                "control_summary": list(control_rows),
            },
            handle,
            indent=2,
        )
        handle.write("\n")

    with probe_csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(probe_rows[0].keys()))
        writer.writeheader()
        writer.writerows(probe_rows)

    with control_csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(control_rows[0].keys()))
        writer.writeheader()
        writer.writerows(control_rows)


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
    parser.add_argument("--episodes", type=int, default=PredictiveStateConfig.episodes)
    parser.add_argument("--max-action", type=int, default=PredictiveStateConfig.max_action)
    parser.add_argument("--calibration-samples", type=int, default=PredictiveStateConfig.calibration_samples)
    parser.add_argument("--control-horizon", type=int, default=PredictiveStateConfig.control_horizon)
    parser.add_argument("--seed", type=int, default=PredictiveStateConfig.seed)
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = PredictiveStateConfig(
        episodes=args.episodes,
        max_action=args.max_action,
        calibration_samples=args.calibration_samples,
        control_horizon=args.control_horizon,
        seed=args.seed,
    )
    scenarios = ["static_goal_switch", "world_drift", "self_drift", "mixed_hidden"]
    states = [
        run_episode(scenario, episode, cfg)
        for scenario in scenarios
        for episode in range(cfg.episodes)
    ]
    probe_rows = summarize_probes(run_probes(states, cfg))
    control_rows = summarize_controls(run_controls(states, cfg))
    write_outputs(probe_rows, control_rows, cfg, args.output_dir)

    print("Probe summary")
    print_table(
        probe_rows,
        ["scenario", "latent", "target", "test_mae", "test_r2", "baseline_mae"],
    )
    print()
    print("Control summary")
    print_table(
        control_rows,
        ["scenario", "policy", "success_rate", "mean_final_distance", "mean_total_loss"],
    )


if __name__ == "__main__":
    main()
