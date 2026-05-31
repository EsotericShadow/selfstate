#!/usr/bin/env python3
"""Boundary-control probe for hidden-state tracking versus selfhood.

This experiment deliberately includes useful hidden variables that should not
count as selfhood. The question is not whether a hidden variable helps. The
question is whether the hidden variable is agent-bounded, action-mediated,
control/value relevant, counterfactually active, and reused across prediction
or control.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"


@dataclass(frozen=True)
class BoundaryConfig:
    episodes: int = 500
    horizon: int = 24
    seed: int = 20260530


@dataclass(frozen=True)
class BoundaryCriteria:
    agent_bounded: bool
    persistent: bool
    action_mediated: bool
    control_value_relevant: bool
    counterfactual_self_intervention: bool
    integrated: bool
    continuity_index: bool
    verdict: str
    counts_as_self_equivalent: bool


@dataclass
class ScenarioSummary:
    scenario: str
    metric: str
    baseline_mean: float
    hidden_tracker_mean: float
    gain: float
    agent_bounded: bool
    persistent: bool
    action_mediated: bool
    control_value_relevant: bool
    counterfactual_self_intervention: bool
    integrated: bool
    continuity_index: bool
    verdict: str
    counts_as_self_equivalent: bool


def episode_seed(seed: int, scenario: str, episode: int) -> int:
    value = seed + episode * 1009
    for char in scenario:
        value = (value * 131 + ord(char)) % (2**32)
    return value


def clip(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def hidden_world_bias(rng: random.Random, cfg: BoundaryConfig) -> Tuple[float, float]:
    """A useful hidden external variable. This is world modeling, not selfhood."""

    wind = rng.choice([-4.0, -2.0, 2.0, 4.0])
    targets = [rng.uniform(-8.0, 8.0) for _ in range(cfg.horizon)]
    baseline_score = 0.0
    tracker_score = 0.0
    for target in targets:
        baseline_action = clip(target, -10.0, 10.0)
        baseline_outcome = baseline_action + wind
        baseline_score -= abs(baseline_outcome - target)

        tracker_action = clip(target - wind, -10.0, 10.0)
        tracker_outcome = tracker_action + wind
        tracker_score -= abs(tracker_outcome - target)
    return baseline_score / cfg.horizon, tracker_score / cfg.horizon


def internal_report_only(rng: random.Random, cfg: BoundaryConfig) -> Tuple[float, float]:
    """A hidden internal variable that helps passive report prediction only."""

    diagnostic = rng.choice([-1, 1])
    baseline_correct = 0
    tracker_correct = 0
    for _ in range(cfg.horizon):
        noisy_cue = diagnostic if rng.random() > 0.15 else -diagnostic
        baseline_prediction = 1
        tracker_prediction = noisy_cue
        baseline_correct += int(baseline_prediction == diagnostic)
        tracker_correct += int(tracker_prediction == diagnostic)
    return baseline_correct / cfg.horizon, tracker_correct / cfg.horizon


def action_effect_state(rng: random.Random, cfg: BoundaryConfig) -> Tuple[float, float]:
    """A hidden internal action-effect variable. This is minimal self-equivalent."""

    gain = rng.choice([0.45, 0.65, 1.35, 1.6])
    targets = [rng.uniform(-8.0, 8.0) for _ in range(cfg.horizon)]
    baseline_score = 0.0
    tracker_score = 0.0
    for target in targets:
        baseline_action = clip(target, -10.0, 10.0)
        baseline_outcome = gain * baseline_action
        baseline_score -= abs(baseline_outcome - target)

        tracker_action = clip(target / gain, -10.0, 10.0)
        tracker_outcome = gain * tracker_action
        tracker_score -= abs(tracker_outcome - target)
    return baseline_score / cfg.horizon, tracker_score / cfg.horizon


def viability_state(rng: random.Random, cfg: BoundaryConfig) -> Tuple[float, float]:
    """A hidden internal state that controls future options and survival."""

    start_energy = rng.uniform(28.0, 72.0)
    work_costs = [rng.uniform(8.0, 14.0) for _ in range(cfg.horizon)]
    rest_gains = [rng.uniform(10.0, 16.0) for _ in range(cfg.horizon)]

    def run_policy(track_energy: bool) -> float:
        energy = start_energy
        score = 0.0
        for step in range(cfg.horizon):
            if track_energy:
                action = "rest" if energy < 24.0 else "work"
            else:
                action = "work"

            if action == "work":
                if energy < 9.0:
                    return score - 40.0
                score += 2.5
                energy -= work_costs[step]
            else:
                score -= 0.4
                energy = min(80.0, energy + rest_gains[step])

            if energy < 0.0:
                return score - 40.0
        return score

    baseline_score = run_policy(track_energy=False)

    tracker_score = run_policy(track_energy=True)
    return baseline_score, tracker_score


def continuity_state(rng: random.Random, cfg: BoundaryConfig) -> Tuple[float, float]:
    """Owner/current-epoch metadata filters what belongs to this agent."""

    owner = "agent_a"
    epoch = rng.randint(2, 5)
    budget = 7
    memories: List[Dict[str, object]] = []
    for idx in range(6):
        memories.append(
            {
                "owner": owner,
                "epoch": epoch,
                "status": "pending",
                "priority": 10 - idx,
            }
        )
    for idx in range(4):
        memories.append(
            {
                "owner": "other_agent",
                "epoch": epoch,
                "status": "pending",
                "priority": 9 - idx,
            }
        )
    for idx in range(3):
        memories.append(
            {
                "owner": owner,
                "epoch": epoch - 1,
                "status": "pending",
                "priority": 8 - idx,
            }
        )
    for idx in range(3):
        memories.append(
            {
                "owner": owner,
                "epoch": epoch,
                "status": rng.choice(["done", "canceled"]),
                "priority": 7 - idx,
            }
        )
    rng.shuffle(memories)

    generic_choices = sorted(
        [memory for memory in memories if memory["status"] == "pending"],
        key=lambda memory: int(memory["priority"]),
        reverse=True,
    )[:budget]
    continuity_choices = sorted(
        [
            memory
            for memory in memories
            if memory["owner"] == owner and memory["epoch"] == epoch and memory["status"] == "pending"
        ],
        key=lambda memory: int(memory["priority"]),
        reverse=True,
    )[:budget]

    def score(choices: Iterable[Dict[str, object]]) -> float:
        total = 0.0
        for memory in choices:
            is_current_own = memory["owner"] == owner and memory["epoch"] == epoch and memory["status"] == "pending"
            total += 1.0 if is_current_own else -1.0
        return total

    return score(generic_choices), score(continuity_choices)


SCENARIOS: Dict[str, Tuple[str, Callable[[random.Random, BoundaryConfig], Tuple[float, float]], BoundaryCriteria]] = {
    "hidden_world_bias": (
        "control_reward",
        hidden_world_bias,
        BoundaryCriteria(
            agent_bounded=False,
            persistent=True,
            action_mediated=True,
            control_value_relevant=True,
            counterfactual_self_intervention=False,
            integrated=True,
            continuity_index=False,
            verdict="world_model_not_self",
            counts_as_self_equivalent=False,
        ),
    ),
    "internal_report_only": (
        "report_accuracy",
        internal_report_only,
        BoundaryCriteria(
            agent_bounded=True,
            persistent=True,
            action_mediated=False,
            control_value_relevant=False,
            counterfactual_self_intervention=False,
            integrated=False,
            continuity_index=False,
            verdict="passive_internal_state_not_self",
            counts_as_self_equivalent=False,
        ),
    ),
    "action_effect_state": (
        "control_reward",
        action_effect_state,
        BoundaryCriteria(
            agent_bounded=True,
            persistent=True,
            action_mediated=True,
            control_value_relevant=True,
            counterfactual_self_intervention=True,
            integrated=True,
            continuity_index=False,
            verdict="minimal_self_equivalent",
            counts_as_self_equivalent=True,
        ),
    ),
    "viability_state": (
        "survival_value",
        viability_state,
        BoundaryCriteria(
            agent_bounded=True,
            persistent=True,
            action_mediated=True,
            control_value_relevant=True,
            counterfactual_self_intervention=True,
            integrated=True,
            continuity_index=False,
            verdict="long_horizon_control_self",
            counts_as_self_equivalent=True,
        ),
    ),
    "continuity_state": (
        "coherence_score",
        continuity_state,
        BoundaryCriteria(
            agent_bounded=True,
            persistent=True,
            action_mediated=True,
            control_value_relevant=True,
            counterfactual_self_intervention=True,
            integrated=True,
            continuity_index=True,
            verdict="identity_like_self",
            counts_as_self_equivalent=True,
        ),
    ),
}


def summarize_scenario(name: str, cfg: BoundaryConfig) -> ScenarioSummary:
    metric, runner, criteria = SCENARIOS[name]
    baseline_scores = []
    tracker_scores = []
    for episode in range(cfg.episodes):
        seed = episode_seed(cfg.seed, name, episode)
        baseline, tracker = runner(random.Random(seed), cfg)
        baseline_scores.append(baseline)
        tracker_scores.append(tracker)

    baseline_mean = statistics.fmean(baseline_scores)
    tracker_mean = statistics.fmean(tracker_scores)
    return ScenarioSummary(
        scenario=name,
        metric=metric,
        baseline_mean=baseline_mean,
        hidden_tracker_mean=tracker_mean,
        gain=tracker_mean - baseline_mean,
        **asdict(criteria),
    )


def write_csv(path: Path, rows: List[ScenarioSummary]) -> None:
    fieldnames = list(asdict(rows[0]).keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=BoundaryConfig.episodes)
    parser.add_argument("--horizon", type=int, default=BoundaryConfig.horizon)
    parser.add_argument("--seed", type=int, default=BoundaryConfig.seed)
    args = parser.parse_args()

    cfg = BoundaryConfig(episodes=args.episodes, horizon=args.horizon, seed=args.seed)
    summaries = [summarize_scenario(name, cfg) for name in SCENARIOS]

    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = ARTIFACT_DIR / "selfhood_boundary_summary.csv"
    json_path = ARTIFACT_DIR / "selfhood_boundary_results.json"
    write_csv(csv_path, summaries)
    payload = {
        "config": asdict(cfg),
        "summaries": [asdict(row) for row in summaries],
    }
    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")

    print(f"wrote {csv_path}")
    print(f"wrote {json_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
