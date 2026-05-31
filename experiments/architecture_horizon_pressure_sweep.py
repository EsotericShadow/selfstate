#!/usr/bin/env python3
"""Architecture horizon-pressure sweep.

This is a follow-up to architecture_boundary_stress.py. The stress test showed
partial, not strict, convergence across independently trained recurrent
architectures. This sweep asks whether increasing temporal horizon removes that
architecture dependence.

The current expected result is deliberately mixed:

- shared regimes become recoverable for at least one architecture as horizon
  increases;
- controls continue to reject shared recurrence;
- strict convergence across all recurrent architectures still does not appear.

That is useful negative evidence: longer horizons increase pressure for
self-equivalent state where the architecture/training setup can exploit it, but
they do not by themselves prove that selfhood is an architecture-independent
attractor.
"""

from __future__ import annotations

import argparse
import json
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

import architecture_boundary_stress as stress
import mixed_sensor_recurrent_filter as mixed
import persistent_action_boundary_probe as persistent


ARTIFACT_DIR = Path("artifacts")
DEFAULT_HORIZONS = (2, 4, 8, 16)
MIN_GAP_DELTA = 1.0


@dataclass(frozen=True)
class HorizonArchitectureRow:
    horizon: int
    scenario: str
    architecture: str
    selected_policy: str
    dependency_signature: str
    expected_signature: str
    recurrent_training_reward: float
    local_training_reward: float
    greedy_training_reward: float
    recurrent_local_gap: float
    action_0_positive_present_effect: float
    action_0_persistence: float
    action_1_positive_present_effect: float
    action_1_persistence: float
    matches_expected_signature: bool


@dataclass(frozen=True)
class HorizonScenarioVerdict:
    scenario: str
    expected_signature: str
    first_horizon: int
    last_horizon: int
    first_converged_architectures: int
    last_converged_architectures: int
    max_converged_architectures: int
    architecture_count: int
    strict_convergence_at_any_horizon: bool
    sum_rnn_gap_first: float
    sum_rnn_gap_last: float
    sum_rnn_gap_delta: float
    convergence_by_horizon: str
    sum_rnn_signature_by_horizon: str
    scalar_signature_by_horizon: str
    two_unit_signature_by_horizon: str
    horizon_pressure_result: str
    supports_architecture_horizon_pressure_result: bool


def parse_horizons(raw: str) -> Tuple[int, ...]:
    values = tuple(int(part.strip()) for part in raw.split(",") if part.strip())
    if not values:
        raise SystemExit("--horizons must contain at least one integer")
    if any(value < 1 for value in values):
        raise SystemExit("--horizons must be positive")
    if tuple(sorted(values)) != values:
        raise SystemExit("--horizons must be sorted ascending")
    return values


def cfg_for_horizon(base: mixed.MixedSensorConfig, horizon: int) -> mixed.MixedSensorConfig:
    return mixed.MixedSensorConfig(
        episodes=base.episodes,
        training_episodes=base.training_episodes,
        seed=base.seed,
        horizon=horizon,
        evidence_samples=base.evidence_samples,
        cue_accuracy=base.cue_accuracy,
        shared_cue_cost=base.shared_cue_cost,
        local_probe_cost=base.local_probe_cost,
        random_candidates=base.random_candidates,
    )


def run_horizon(
    horizon: int,
    base_cfg: mixed.MixedSensorConfig,
) -> List[HorizonArchitectureRow]:
    cfg = cfg_for_horizon(base_cfg, horizon)
    rows: List[HorizonArchitectureRow] = []
    for scenario in persistent.SCENARIOS:
        mixed_scenario = persistent.as_mixed_scenario(scenario)
        training_states = mixed.make_states(mixed_scenario, "train", cfg.training_episodes, cfg)
        for architecture in mixed.ARCHITECTURES:
            candidate = stress.train_architecture(mixed_scenario, architecture, training_states, cfg)
            selected_policy, rewards = mixed.select_policy(candidate, training_states, cfg)
            boundary_row = stress.architecture_row(
                scenario=scenario,
                architecture=architecture,
                candidate=candidate,
                selected_policy=selected_policy,
                rewards=rewards,
                cfg=cfg,
            )
            rows.append(
                HorizonArchitectureRow(
                    horizon=horizon,
                    scenario=boundary_row.scenario,
                    architecture=architecture,
                    selected_policy=selected_policy,
                    dependency_signature=boundary_row.dependency_signature,
                    expected_signature=boundary_row.expected_signature,
                    recurrent_training_reward=boundary_row.recurrent_training_reward,
                    local_training_reward=boundary_row.local_training_reward,
                    greedy_training_reward=boundary_row.greedy_training_reward,
                    recurrent_local_gap=(
                        boundary_row.recurrent_training_reward - boundary_row.local_training_reward
                    ),
                    action_0_positive_present_effect=boundary_row.action_0_positive_present_effect,
                    action_0_persistence=boundary_row.action_0_persistence,
                    action_1_positive_present_effect=boundary_row.action_1_positive_present_effect,
                    action_1_persistence=boundary_row.action_1_persistence,
                    matches_expected_signature=boundary_row.matches_expected_signature,
                )
            )
    return rows


def verdict_rows(rows: Sequence[HorizonArchitectureRow]) -> List[HorizonScenarioVerdict]:
    verdicts = []
    horizons = sorted({row.horizon for row in rows})
    for scenario in sorted({row.scenario for row in rows}):
        scenario_rows = [row for row in rows if row.scenario == scenario]
        expected = stress.EXPECTED_SIGNATURES[scenario]
        counts = {
            horizon: sum(
                1
                for row in scenario_rows
                if row.horizon == horizon and row.matches_expected_signature
            )
            for horizon in horizons
        }
        architecture_count = len({row.architecture for row in scenario_rows})
        first_horizon = horizons[0]
        last_horizon = horizons[-1]
        strict_any = any(count == architecture_count for count in counts.values())
        sum_first = recurrent_gap(scenario_rows, first_horizon, "sum_rnn")
        sum_last = recurrent_gap(scenario_rows, last_horizon, "sum_rnn")
        result = classify_horizon_result(scenario, counts, architecture_count, strict_any, sum_last - sum_first)
        verdicts.append(
            HorizonScenarioVerdict(
                scenario=scenario,
                expected_signature=expected,
                first_horizon=first_horizon,
                last_horizon=last_horizon,
                first_converged_architectures=counts[first_horizon],
                last_converged_architectures=counts[last_horizon],
                max_converged_architectures=max(counts.values()),
                architecture_count=architecture_count,
                strict_convergence_at_any_horizon=strict_any,
                sum_rnn_gap_first=sum_first,
                sum_rnn_gap_last=sum_last,
                sum_rnn_gap_delta=sum_last - sum_first,
                convergence_by_horizon=";".join(f"{h}:{counts[h]}/{architecture_count}" for h in horizons),
                sum_rnn_signature_by_horizon=signature_series(scenario_rows, horizons, "sum_rnn"),
                scalar_signature_by_horizon=signature_series(scenario_rows, horizons, "scalar_rnn"),
                two_unit_signature_by_horizon=signature_series(scenario_rows, horizons, "two_unit_rnn"),
                horizon_pressure_result=result,
                supports_architecture_horizon_pressure_result=supports_horizon_result(
                    scenario,
                    counts,
                    architecture_count,
                    strict_any,
                    sum_last - sum_first,
                    result,
                ),
            )
        )
    return verdicts


def recurrent_gap(rows: Sequence[HorizonArchitectureRow], horizon: int, architecture: str) -> float:
    return next(
        row.recurrent_local_gap
        for row in rows
        if row.horizon == horizon and row.architecture == architecture
    )


def signature_series(
    rows: Sequence[HorizonArchitectureRow],
    horizons: Sequence[int],
    architecture: str,
) -> str:
    return ";".join(
        f"{h}:{next(row.dependency_signature for row in rows if row.horizon == h and row.architecture == architecture)}"
        for h in horizons
    )


def classify_horizon_result(
    scenario: str,
    counts: dict[int, int],
    architecture_count: int,
    strict_any: bool,
    sum_rnn_gap_delta: float,
) -> str:
    if scenario in stress.SHARED_REGIMES:
        if strict_any:
            return "horizon_produces_strict_architecture_convergence"
        if max(counts.values()) > min(counts.values()) and sum_rnn_gap_delta > MIN_GAP_DELTA:
            return "horizon_improves_recoverability_not_strict_convergence"
        return "horizon_does_not_improve_shared_boundary_recovery"
    if scenario in stress.CONTROL_REGIMES:
        if all(count == architecture_count for count in counts.values()):
            return "controls_reject_shared_recurrence_across_horizons"
        return "control_false_positive_across_horizons"
    raise ValueError(f"unknown scenario: {scenario}")


def supports_horizon_result(
    scenario: str,
    counts: dict[int, int],
    architecture_count: int,
    strict_any: bool,
    sum_rnn_gap_delta: float,
    result: str,
) -> bool:
    if scenario in stress.SHARED_REGIMES:
        return (
            result == "horizon_improves_recoverability_not_strict_convergence"
            and not strict_any
            and max(counts.values()) < architecture_count
            and max(counts.values()) > min(counts.values())
            and sum_rnn_gap_delta > MIN_GAP_DELTA
        )
    if scenario in stress.CONTROL_REGIMES:
        return (
            result == "controls_reject_shared_recurrence_across_horizons"
            and all(count == architecture_count for count in counts.values())
        )
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    horizons: Sequence[int],
    cfg: mixed.MixedSensorConfig,
) -> Tuple[List[HorizonArchitectureRow], List[HorizonScenarioVerdict]]:
    rows: List[HorizonArchitectureRow] = []
    for horizon in horizons:
        rows.extend(run_horizon(horizon, cfg))
    return rows, verdict_rows(rows)


def write_csv(path: Path, rows: Iterable[object]) -> None:
    mixed.write_csv(path, rows)


def print_table(verdicts: Sequence[HorizonScenarioVerdict]) -> None:
    headers = [
        "scenario",
        "convergence_by_horizon",
        "strict_convergence_at_any_horizon",
        "sum_rnn_gap_delta",
        "horizon_pressure_result",
        "supports_architecture_horizon_pressure_result",
    ]
    table_rows = []
    for verdict in verdicts:
        table_rows.append(
            [
                verdict.scenario,
                verdict.convergence_by_horizon,
                str(verdict.strict_convergence_at_any_horizon),
                f"{verdict.sum_rnn_gap_delta:.3f}",
                verdict.horizon_pressure_result,
                str(verdict.supports_architecture_horizon_pressure_result),
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


def parse_args() -> Tuple[Tuple[int, ...], mixed.MixedSensorConfig]:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--horizons", default=",".join(str(value) for value in DEFAULT_HORIZONS))
    parser.add_argument("--episodes", type=int, default=250)
    parser.add_argument("--training-episodes", type=int, default=400)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--evidence-samples", type=int, default=9)
    parser.add_argument("--cue-accuracy", type=float, default=0.85)
    parser.add_argument("--shared-cue-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    parser.add_argument("--random-candidates", type=int, default=900)
    args = parser.parse_args()
    horizons = parse_horizons(args.horizons)
    if args.episodes < 1:
        raise SystemExit("--episodes must be at least 1")
    if args.training_episodes < 1:
        raise SystemExit("--training-episodes must be at least 1")
    if args.evidence_samples < 1:
        raise SystemExit("--evidence-samples must be at least 1")
    if not 0.5 <= args.cue_accuracy <= 1.0:
        raise SystemExit("--cue-accuracy must be in [0.5, 1.0]")
    if args.random_candidates < 1:
        raise SystemExit("--random-candidates must be positive")
    return (
        horizons,
        mixed.MixedSensorConfig(
            episodes=args.episodes,
            training_episodes=args.training_episodes,
            seed=args.seed,
            horizon=horizons[0],
            evidence_samples=args.evidence_samples,
            cue_accuracy=args.cue_accuracy,
            shared_cue_cost=args.shared_cue_cost,
            local_probe_cost=args.local_probe_cost,
            random_candidates=args.random_candidates,
        ),
    )


def main() -> int:
    horizons, cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows, verdicts = run_experiment(horizons, cfg)
    summary_path = ARTIFACT_DIR / "architecture_horizon_pressure_summary.csv"
    verdict_path = ARTIFACT_DIR / "architecture_horizon_pressure_verdict.csv"
    results_path = ARTIFACT_DIR / "architecture_horizon_pressure_results.json"
    write_csv(summary_path, rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": {**asdict(cfg), "horizons": list(horizons)},
                "summary": [asdict(row) for row in rows],
                "verdict": [asdict(row) for row in verdicts],
            },
            handle,
            indent=2,
        )
        handle.write("\n")
    print(f"wrote {summary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print_table(verdicts)
    return 0 if all(verdict.supports_architecture_horizon_pressure_result for verdict in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
