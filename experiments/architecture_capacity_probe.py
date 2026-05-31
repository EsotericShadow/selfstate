#!/usr/bin/env python3
"""Architecture capacity probe.

This is a diagnostic companion to architecture_boundary_stress.py and
architecture_horizon_pressure_sweep.py. Those tests showed that random-start
training produces only partial convergence across recurrent architectures. This
probe asks whether that failure is a capacity limit or a training-search limit.

The probe supplies a small set of source-direction recurrent seeds to each
architecture, then still selects by return and applies the same end-to-end
boundary test. A positive result does not count as natural emergence because
the useful basis directions are supplied. It only shows that the weaker
architectures can represent and use the boundary when search is not the
bottleneck.
"""

from __future__ import annotations

import argparse
import json
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import architecture_boundary_stress as stress
import end_to_end_boundary_probe as end_to_end
import mixed_sensor_recurrent_filter as mixed
import persistent_action_boundary_probe as persistent


ARTIFACT_DIR = Path("artifacts")

SOURCE_DIRECTIONS = {
    "source_a": (0.8, -0.6),
    "source_b": (0.6, 0.8),
    "neg_source_a": (-0.8, 0.6),
    "neg_source_b": (-0.6, -0.8),
}

ALPHAS = (0.2, 0.4, 0.8, 1.2)
RECURRENCES = (0.0, 0.4, 0.8, 0.95)
OUTPUT_WEIGHTS = (4.0, 8.0, 16.0)


@dataclass(frozen=True)
class CapacityProbeRow:
    scenario: str
    architecture: str
    selected_policy: str
    dependency_signature: str
    expected_signature: str
    selected_seed_direction: str
    selected_alpha: float
    selected_recurrence: float
    selected_output_weight: float
    recurrent_training_reward: float
    local_training_reward: float
    greedy_training_reward: float
    safe_training_reward: float
    recurrent_local_gap: float
    action_0_positive_present_effect: float
    action_0_persistence: float
    action_1_positive_present_effect: float
    action_1_persistence: float
    matches_expected_signature: bool
    selected_weights: str


@dataclass(frozen=True)
class CapacityProbeVerdict:
    scenario: str
    expected_signature: str
    converged_architectures: int
    architecture_count: int
    strict_capacity_convergence: bool
    sum_rnn_signature: str
    scalar_rnn_signature: str
    two_unit_rnn_signature: str
    recurrent_winners: int
    local_winners: int
    greedy_winners: int
    mean_recurrent_reward: float
    mean_local_reward: float
    capacity_result: str
    supports_architecture_capacity_result: bool


def seed_candidate(
    architecture: str,
    direction_name: str,
    alpha: float,
    recurrence: float,
    output_weight: float,
) -> mixed.Candidate:
    weight_1, weight_2 = SOURCE_DIRECTIONS[direction_name]
    if architecture == "sum_rnn":
        return mixed.Candidate(
            architecture,
            (0.0, alpha * weight_1, alpha * weight_2, output_weight, 0.0),
            0.0,
        )
    if architecture == "scalar_rnn":
        return mixed.Candidate(
            architecture,
            (0.0, recurrence, alpha * weight_1, alpha * weight_2, output_weight, 0.0),
            0.0,
        )
    if architecture == "two_unit_rnn":
        return mixed.Candidate(
            architecture,
            (
                0.0,
                recurrence,
                alpha * weight_1,
                alpha * weight_2,
                0.0,
                0.0,
                0.0,
                0.0,
                output_weight,
                0.0,
                0.0,
            ),
            0.0,
        )
    raise ValueError(f"unknown architecture: {architecture}")


def train_capacity_candidate(
    architecture: str,
    states: Sequence[mixed.EpisodeState],
    cfg: mixed.MixedSensorConfig,
) -> Tuple[mixed.Candidate, str, float, float, float]:
    best: Tuple[float, str, float, float, float, mixed.Candidate] | None = None
    recurrences = (0.0,) if architecture == "sum_rnn" else RECURRENCES
    for direction_name in SOURCE_DIRECTIONS:
        for alpha in ALPHAS:
            for recurrence in recurrences:
                for output_weight in OUTPUT_WEIGHTS:
                    candidate = seed_candidate(architecture, direction_name, alpha, recurrence, output_weight)
                    reward = mixed.mean_recurrent_reward(states, candidate, cfg)
                    scored = mixed.Candidate(
                        architecture=candidate.architecture,
                        weights=candidate.weights,
                        training_reward=reward,
                    )
                    if best is None or reward > best[0]:
                        best = (reward, direction_name, alpha, recurrence, output_weight, scored)
    if best is None:
        raise RuntimeError(f"no capacity candidate trained for {architecture}")
    reward, direction_name, alpha, recurrence, output_weight, candidate = best
    return candidate, direction_name, alpha, recurrence, output_weight


def capacity_row(
    scenario: persistent.BoundaryScenario,
    architecture: str,
    cfg: mixed.MixedSensorConfig,
) -> CapacityProbeRow:
    mixed_scenario = persistent.as_mixed_scenario(scenario)
    training_states = mixed.make_states(mixed_scenario, "train", cfg.training_episodes, cfg)
    candidate, direction_name, alpha, recurrence, output_weight = train_capacity_candidate(
        architecture,
        training_states,
        cfg,
    )
    selected_policy, rewards = mixed.select_policy(candidate, training_states, cfg)
    boundary = end_to_end.build_boundary_row(scenario, candidate, selected_policy, rewards, cfg)
    expected = stress.EXPECTED_SIGNATURES[scenario.name]
    return CapacityProbeRow(
        scenario=scenario.name,
        architecture=architecture,
        selected_policy=selected_policy,
        dependency_signature=boundary.dependency_signature,
        expected_signature=expected,
        selected_seed_direction=direction_name,
        selected_alpha=alpha,
        selected_recurrence=recurrence,
        selected_output_weight=output_weight,
        recurrent_training_reward=rewards["recurrent_controller"],
        local_training_reward=rewards["task_local_probe"],
        greedy_training_reward=rewards["greedy_no_state"],
        safe_training_reward=rewards["safe_no_state"],
        recurrent_local_gap=rewards["recurrent_controller"] - rewards["task_local_probe"],
        action_0_positive_present_effect=boundary.action_0_positive_present_effect,
        action_0_persistence=boundary.action_0_persistence,
        action_1_positive_present_effect=boundary.action_1_positive_present_effect,
        action_1_persistence=boundary.action_1_persistence,
        matches_expected_signature=boundary.dependency_signature == expected,
        selected_weights=mixed.format_weights(candidate.weights),
    )


def verdict_rows(rows: Sequence[CapacityProbeRow]) -> List[CapacityProbeVerdict]:
    verdicts = []
    for scenario in sorted({row.scenario for row in rows}):
        scenario_rows = [row for row in rows if row.scenario == scenario]
        expected = stress.EXPECTED_SIGNATURES[scenario]
        converged = sum(1 for row in scenario_rows if row.matches_expected_signature)
        architecture_count = len(scenario_rows)
        strict = converged == architecture_count
        capacity_result = classify_capacity_result(scenario, strict, scenario_rows)
        verdicts.append(
            CapacityProbeVerdict(
                scenario=scenario,
                expected_signature=expected,
                converged_architectures=converged,
                architecture_count=architecture_count,
                strict_capacity_convergence=strict,
                sum_rnn_signature=signature_for(scenario_rows, "sum_rnn"),
                scalar_rnn_signature=signature_for(scenario_rows, "scalar_rnn"),
                two_unit_rnn_signature=signature_for(scenario_rows, "two_unit_rnn"),
                recurrent_winners=sum(1 for row in scenario_rows if row.selected_policy == "recurrent_controller"),
                local_winners=sum(1 for row in scenario_rows if row.selected_policy == "task_local_probe"),
                greedy_winners=sum(1 for row in scenario_rows if row.selected_policy == "greedy_no_state"),
                mean_recurrent_reward=statistics.fmean(row.recurrent_training_reward for row in scenario_rows),
                mean_local_reward=statistics.fmean(row.local_training_reward for row in scenario_rows),
                capacity_result=capacity_result,
                supports_architecture_capacity_result=supports_capacity_result(
                    scenario,
                    strict,
                    scenario_rows,
                    capacity_result,
                ),
            )
        )
    return verdicts


def signature_for(rows: Sequence[CapacityProbeRow], architecture: str) -> str:
    return next(row.dependency_signature for row in rows if row.architecture == architecture)


def classify_capacity_result(
    scenario: str,
    strict: bool,
    rows: Sequence[CapacityProbeRow],
) -> str:
    if scenario in stress.SHARED_REGIMES and strict:
        return "seeded_capacity_recovers_shared_boundary"
    if scenario == "independent_hidden" and strict:
        return "seeded_capacity_rejects_shared_recurrence"
    if scenario == "irrelevant_control" and strict:
        return "seeded_capacity_rejects_hidden_state"
    return "seeded_capacity_failure"


def supports_capacity_result(
    scenario: str,
    strict: bool,
    rows: Sequence[CapacityProbeRow],
    capacity_result: str,
) -> bool:
    if scenario in stress.SHARED_REGIMES:
        return (
            strict
            and capacity_result == "seeded_capacity_recovers_shared_boundary"
            and all(row.selected_policy == "recurrent_controller" for row in rows)
        )
    if scenario == "independent_hidden":
        return (
            strict
            and capacity_result == "seeded_capacity_rejects_shared_recurrence"
            and all(row.selected_policy == "task_local_probe" for row in rows)
        )
    if scenario == "irrelevant_control":
        return (
            strict
            and capacity_result == "seeded_capacity_rejects_hidden_state"
            and all(row.selected_policy == "greedy_no_state" for row in rows)
        )
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: mixed.MixedSensorConfig,
) -> Tuple[List[CapacityProbeRow], List[CapacityProbeVerdict]]:
    rows = [
        capacity_row(scenario, architecture, cfg)
        for scenario in persistent.SCENARIOS
        for architecture in mixed.ARCHITECTURES
    ]
    return rows, verdict_rows(rows)


def write_csv(path: Path, rows: Iterable[object]) -> None:
    mixed.write_csv(path, rows)


def print_table(verdicts: Sequence[CapacityProbeVerdict]) -> None:
    headers = [
        "scenario",
        "converged_architectures",
        "architecture_count",
        "strict_capacity_convergence",
        "capacity_result",
        "supports_architecture_capacity_result",
    ]
    table_rows = []
    for verdict in verdicts:
        table_rows.append(
            [
                verdict.scenario,
                str(verdict.converged_architectures),
                str(verdict.architecture_count),
                str(verdict.strict_capacity_convergence),
                verdict.capacity_result,
                str(verdict.supports_architecture_capacity_result),
            ]
        )
    widths = [
        max(len(header), *(len(row[index]) for row in table_rows))
        for index, header in enumerate(headers)
    ]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in table_rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> mixed.MixedSensorConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=500)
    parser.add_argument("--training-episodes", type=int, default=800)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--horizon", type=int, default=8)
    parser.add_argument("--evidence-samples", type=int, default=9)
    parser.add_argument("--cue-accuracy", type=float, default=0.85)
    parser.add_argument("--shared-cue-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    args = parser.parse_args()
    if args.episodes < 1:
        raise SystemExit("--episodes must be at least 1")
    if args.training_episodes < 1:
        raise SystemExit("--training-episodes must be at least 1")
    if args.horizon < 1:
        raise SystemExit("--horizon must be at least 1")
    if args.evidence_samples < 1:
        raise SystemExit("--evidence-samples must be at least 1")
    if not 0.5 <= args.cue_accuracy <= 1.0:
        raise SystemExit("--cue-accuracy must be in [0.5, 1.0]")
    return mixed.MixedSensorConfig(
        episodes=args.episodes,
        training_episodes=args.training_episodes,
        seed=args.seed,
        horizon=args.horizon,
        evidence_samples=args.evidence_samples,
        cue_accuracy=args.cue_accuracy,
        shared_cue_cost=args.shared_cue_cost,
        local_probe_cost=args.local_probe_cost,
        random_candidates=1,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows, verdicts = run_experiment(cfg)
    summary_path = ARTIFACT_DIR / "architecture_capacity_probe_summary.csv"
    verdict_path = ARTIFACT_DIR / "architecture_capacity_probe_verdict.csv"
    results_path = ARTIFACT_DIR / "architecture_capacity_probe_results.json"
    write_csv(summary_path, rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "summary": [asdict(row) for row in rows],
                "verdict": [asdict(row) for row in verdicts],
                "note": "Capacity diagnostic only: source-direction seed candidates are supplied.",
            },
            handle,
            indent=2,
        )
        handle.write("\n")
    print(f"wrote {summary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print_table(verdicts)
    return 0 if all(verdict.supports_architecture_capacity_result for verdict in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
