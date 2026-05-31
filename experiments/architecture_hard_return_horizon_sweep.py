#!/usr/bin/env python3
"""Architecture hard-return horizon sweep.

This is a pressure audit for architecture_hard_return_audit.py. Report 53 showed
that hard realized-return optimization keeps controls clean but only partially
recovers the self and detachable boundary signatures at horizon 8.

This sweep asks whether longer temporal dependence repairs that hard-return
failure. It intentionally uses a bounded optimizer budget so the question is not
"can unlimited search find the boundary?" but "does horizon pressure improve
realized-return discovery under the same objective?"
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

import architecture_boundary_stress as stress
import architecture_hard_return_audit as hard


ARTIFACT_DIR = Path("artifacts")
DEFAULT_HORIZONS = (2, 4, 8, 16)


@dataclass(frozen=True)
class HardReturnHorizonConfig:
    horizons: Tuple[int, ...] = DEFAULT_HORIZONS
    episodes: int = 180
    training_episodes: int = 240
    seed: int = 20260603
    evidence_samples: int = 9
    cue_accuracy: float = 0.85
    shared_cue_cost: float = 1.0
    local_probe_cost: float = 1.0
    iterations: int = 8
    population: int = 120
    restarts: int = 5
    initial_std: float = 1.4


@dataclass(frozen=True)
class HardReturnHorizonRow:
    horizon: int
    scenario: str
    architecture: str
    selected_policy: str
    dependency_signature: str
    expected_signature: str
    hard_training_objective: float
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


@dataclass(frozen=True)
class HardReturnHorizonVerdict:
    scenario: str
    expected_signature: str
    first_horizon: int
    last_horizon: int
    first_converged_architectures: int
    last_converged_architectures: int
    max_converged_architectures: int
    architecture_count: int
    strict_convergence_at_any_horizon: bool
    convergence_by_horizon: str
    sum_rnn_signature_by_horizon: str
    scalar_signature_by_horizon: str
    two_unit_signature_by_horizon: str
    hard_return_horizon_result: str
    supports_architecture_hard_return_horizon_sweep: bool


def parse_horizons(raw: str) -> Tuple[int, ...]:
    values = tuple(int(part.strip()) for part in raw.split(",") if part.strip())
    if not values:
        raise SystemExit("--horizons must contain at least one integer")
    if any(value < 1 for value in values):
        raise SystemExit("--horizons must be positive")
    if tuple(sorted(values)) != values:
        raise SystemExit("--horizons must be sorted ascending")
    return values


def hard_cfg_for_horizon(base: HardReturnHorizonConfig, horizon: int) -> hard.HardReturnConfig:
    return hard.HardReturnConfig(
        episodes=base.episodes,
        training_episodes=base.training_episodes,
        seed=base.seed,
        horizon=horizon,
        evidence_samples=base.evidence_samples,
        cue_accuracy=base.cue_accuracy,
        shared_cue_cost=base.shared_cue_cost,
        local_probe_cost=base.local_probe_cost,
        iterations=base.iterations,
        population=base.population,
        restarts=base.restarts,
        initial_std=base.initial_std,
    )


def run_horizon(horizon: int, base_cfg: HardReturnHorizonConfig) -> List[HardReturnHorizonRow]:
    rows, _verdicts = hard.run_experiment(hard_cfg_for_horizon(base_cfg, horizon))
    return [
        HardReturnHorizonRow(
            horizon=horizon,
            scenario=row.scenario,
            architecture=row.architecture,
            selected_policy=row.selected_policy,
            dependency_signature=row.dependency_signature,
            expected_signature=row.expected_signature,
            hard_training_objective=row.hard_training_objective,
            recurrent_training_reward=row.recurrent_training_reward,
            local_training_reward=row.local_training_reward,
            greedy_training_reward=row.greedy_training_reward,
            safe_training_reward=row.safe_training_reward,
            recurrent_local_gap=row.recurrent_local_gap,
            action_0_positive_present_effect=row.action_0_positive_present_effect,
            action_0_persistence=row.action_0_persistence,
            action_1_positive_present_effect=row.action_1_positive_present_effect,
            action_1_persistence=row.action_1_persistence,
            matches_expected_signature=row.matches_expected_signature,
        )
        for row in rows
    ]


def verdict_rows(rows: Sequence[HardReturnHorizonRow]) -> List[HardReturnHorizonVerdict]:
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
        result = classify_horizon_result(scenario, counts, architecture_count, strict_any)
        verdicts.append(
            HardReturnHorizonVerdict(
                scenario=scenario,
                expected_signature=expected,
                first_horizon=first_horizon,
                last_horizon=last_horizon,
                first_converged_architectures=counts[first_horizon],
                last_converged_architectures=counts[last_horizon],
                max_converged_architectures=max(counts.values()),
                architecture_count=architecture_count,
                strict_convergence_at_any_horizon=strict_any,
                convergence_by_horizon=";".join(f"{h}:{counts[h]}/{architecture_count}" for h in horizons),
                sum_rnn_signature_by_horizon=signature_series(scenario_rows, horizons, "sum_rnn"),
                scalar_signature_by_horizon=signature_series(scenario_rows, horizons, "scalar_rnn"),
                two_unit_signature_by_horizon=signature_series(scenario_rows, horizons, "two_unit_rnn"),
                hard_return_horizon_result=result,
                supports_architecture_hard_return_horizon_sweep=supports_horizon_result(
                    scenario,
                    counts,
                    architecture_count,
                    strict_any,
                    result,
                ),
            )
        )
    return verdicts


def signature_series(
    rows: Sequence[HardReturnHorizonRow],
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
) -> str:
    first = counts[min(counts)]
    last = counts[max(counts)]
    if scenario in {"self_persistent_boundary", "detachable_tool_world"}:
        if strict_any:
            return "hard_return_horizon_produces_strict_self_tool_convergence"
        if last > first and max(counts.values()) < architecture_count:
            return "hard_return_horizon_improves_partial_self_tool_convergence"
        return "hard_return_horizon_does_not_improve_self_tool_convergence"
    if scenario == "passive_world_boundary":
        if last == architecture_count and first < last:
            return "hard_return_horizon_recovers_passive_external_boundary"
        return "hard_return_horizon_does_not_recover_passive_external_boundary"
    if scenario == "independent_hidden":
        if all(count == architecture_count for count in counts.values()):
            return "hard_return_horizon_rejects_shared_recurrence"
        return "hard_return_horizon_control_false_positive"
    if scenario == "irrelevant_control":
        if all(count == architecture_count for count in counts.values()):
            return "hard_return_horizon_rejects_hidden_state"
        return "hard_return_horizon_control_false_positive"
    raise ValueError(f"unknown scenario: {scenario}")


def supports_horizon_result(
    scenario: str,
    counts: dict[int, int],
    architecture_count: int,
    strict_any: bool,
    result: str,
) -> bool:
    first = counts[min(counts)]
    last = counts[max(counts)]
    if scenario in {"self_persistent_boundary", "detachable_tool_world"}:
        return (
            result == "hard_return_horizon_improves_partial_self_tool_convergence"
            and last > first
            and max(counts.values()) < architecture_count
            and not strict_any
        )
    if scenario == "passive_world_boundary":
        return (
            result == "hard_return_horizon_recovers_passive_external_boundary"
            and first < last == architecture_count
        )
    if scenario == "independent_hidden":
        return result == "hard_return_horizon_rejects_shared_recurrence"
    if scenario == "irrelevant_control":
        return result == "hard_return_horizon_rejects_hidden_state"
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: HardReturnHorizonConfig,
) -> Tuple[List[HardReturnHorizonRow], List[HardReturnHorizonVerdict]]:
    rows = [row for horizon in cfg.horizons for row in run_horizon(horizon, cfg)]
    return rows, verdict_rows(rows)


def write_csv(path: Path, rows: Iterable[object]) -> None:
    hard.mixed.write_csv(path, rows)


def print_table(verdicts: Sequence[HardReturnHorizonVerdict]) -> None:
    headers = [
        "scenario",
        "convergence_by_horizon",
        "strict_convergence_at_any_horizon",
        "hard_return_horizon_result",
        "supports_architecture_hard_return_horizon_sweep",
    ]
    table_rows = []
    for verdict in verdicts:
        table_rows.append(
            [
                verdict.scenario,
                verdict.convergence_by_horizon,
                str(verdict.strict_convergence_at_any_horizon),
                verdict.hard_return_horizon_result,
                str(verdict.supports_architecture_hard_return_horizon_sweep),
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


def parse_args() -> HardReturnHorizonConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--horizons", default=",".join(str(value) for value in DEFAULT_HORIZONS))
    parser.add_argument("--episodes", type=int, default=180)
    parser.add_argument("--training-episodes", type=int, default=240)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--evidence-samples", type=int, default=9)
    parser.add_argument("--cue-accuracy", type=float, default=0.85)
    parser.add_argument("--shared-cue-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    parser.add_argument("--iterations", type=int, default=8)
    parser.add_argument("--population", type=int, default=120)
    parser.add_argument("--restarts", type=int, default=5)
    parser.add_argument("--initial-std", type=float, default=1.4)
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
    if args.iterations < 1:
        raise SystemExit("--iterations must be positive")
    if args.population < 3:
        raise SystemExit("--population must be at least 3")
    if args.restarts < 1:
        raise SystemExit("--restarts must be positive")
    if args.initial_std <= 0.0:
        raise SystemExit("--initial-std must be positive")
    return HardReturnHorizonConfig(
        horizons=horizons,
        episodes=args.episodes,
        training_episodes=args.training_episodes,
        seed=args.seed,
        evidence_samples=args.evidence_samples,
        cue_accuracy=args.cue_accuracy,
        shared_cue_cost=args.shared_cue_cost,
        local_probe_cost=args.local_probe_cost,
        iterations=args.iterations,
        population=args.population,
        restarts=args.restarts,
        initial_std=args.initial_std,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows, verdicts = run_experiment(cfg)
    summary_path = ARTIFACT_DIR / "architecture_hard_return_horizon_summary.csv"
    verdict_path = ARTIFACT_DIR / "architecture_hard_return_horizon_verdict.csv"
    results_path = ARTIFACT_DIR / "architecture_hard_return_horizon_results.json"
    write_csv(summary_path, rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "summary": [asdict(row) for row in rows],
                "verdict": [asdict(row) for row in verdicts],
                "note": (
                    "Hard realized-return horizon sweep with no smooth expected-return "
                    "surrogate and no boundary-aware selection. Uses a bounded optimizer budget."
                ),
            },
            handle,
            indent=2,
        )
        handle.write("\n")
    print(f"wrote {summary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print_table(verdicts)
    return 0 if all(verdict.supports_architecture_hard_return_horizon_sweep for verdict in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
