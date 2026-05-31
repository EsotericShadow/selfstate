#!/usr/bin/env python3
"""Architecture hard-return audit.

This is a limitation audit for architecture_soft_return_optimizer.py. Report 52
showed that a smooth expected-return surrogate can discover the expected
boundary signatures without source-direction seeds or boundary-aware restart
selection. This experiment removes that smooth surrogate.

Each recurrent architecture is optimized from Gaussian starts with a
cross-entropy method ranked only by realized recurrent training return. Restarts
are also selected only by realized recurrent return. The boundary classifier is
applied after training. The purpose is to test whether ordinary hard return is
enough to recover the same causal boundary abstraction, or whether high-return
controllers can solve the task while leaving the boundary signature underformed.
"""

from __future__ import annotations

import argparse
import json
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

import architecture_boundary_stress as stress
import architecture_soft_return_optimizer as soft
import end_to_end_boundary_probe as end_to_end
import mixed_sensor_recurrent_filter as mixed
import persistent_action_boundary_probe as persistent


ARTIFACT_DIR = Path("artifacts")
SEED_OFFSET = 9091
ELITE_FRACTION = 0.12
STD_DECAY = 0.8
MIN_STD = 0.04


@dataclass(frozen=True)
class HardReturnConfig:
    episodes: int = 300
    training_episodes: int = 400
    seed: int = 20260603
    horizon: int = 8
    evidence_samples: int = 9
    cue_accuracy: float = 0.85
    shared_cue_cost: float = 1.0
    local_probe_cost: float = 1.0
    iterations: int = 16
    population: int = 220
    restarts: int = 10
    initial_std: float = 1.4


@dataclass(frozen=True)
class HardReturnRow:
    scenario: str
    architecture: str
    selected_policy: str
    dependency_signature: str
    expected_signature: str
    best_restart: int
    best_iteration: int
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
    selected_weights: str


@dataclass(frozen=True)
class HardReturnVerdict:
    scenario: str
    expected_signature: str
    converged_architectures: int
    architecture_count: int
    strict_hard_return_convergence: bool
    sum_rnn_signature: str
    scalar_rnn_signature: str
    two_unit_rnn_signature: str
    recurrent_winners: int
    local_winners: int
    greedy_winners: int
    mean_recurrent_reward: float
    mean_local_reward: float
    hard_return_result: str
    supports_architecture_hard_return_audit: bool


def as_mixed_cfg(cfg: HardReturnConfig) -> mixed.MixedSensorConfig:
    return mixed.MixedSensorConfig(
        episodes=cfg.episodes,
        training_episodes=cfg.training_episodes,
        seed=cfg.seed,
        horizon=cfg.horizon,
        evidence_samples=cfg.evidence_samples,
        cue_accuracy=cfg.cue_accuracy,
        shared_cue_cost=cfg.shared_cue_cost,
        local_probe_cost=cfg.local_probe_cost,
        random_candidates=1,
    )


def hard_return_restart(
    architecture: str,
    scenario_name: str,
    restart: int,
    states: Sequence[mixed.EpisodeState],
    cfg: HardReturnConfig,
) -> Tuple[mixed.Candidate, int]:
    rng = random.Random(mixed.stable_name_seed(cfg.seed + SEED_OFFSET + restart * 97, scenario_name, architecture))
    dimensions = soft.parameter_count(architecture)
    mean = [0.0 for _ in range(dimensions)]
    std = [cfg.initial_std for _ in range(dimensions)]
    mixed_cfg = as_mixed_cfg(cfg)
    best: Tuple[float, Tuple[float, ...], int] | None = None

    for iteration in range(cfg.iterations):
        scored = []
        for _ in range(cfg.population):
            weights = soft.clamp_weights(rng.gauss(mean[index], std[index]) for index in range(dimensions))
            candidate = mixed.Candidate(architecture, weights, 0.0)
            hard_reward = mixed.mean_recurrent_reward(states, candidate, mixed_cfg)
            scored.append((hard_reward, weights, iteration))
            if best is None or hard_reward > best[0]:
                best = (hard_reward, weights, iteration)
        scored.sort(reverse=True, key=lambda item: item[0])
        elite_count = max(3, int(cfg.population * ELITE_FRACTION))
        elites = [weights for _score, weights, _iteration in scored[:elite_count]]
        mean = [statistics.fmean(weights[index] for weights in elites) for index in range(dimensions)]
        std = [
            max(MIN_STD, statistics.pstdev(weights[index] for weights in elites) * STD_DECAY)
            for index in range(dimensions)
        ]

    if best is None:
        raise RuntimeError(f"no hard-return candidate for {scenario_name}:{architecture}:{restart}")
    hard_reward, weights, best_iteration = best
    return mixed.Candidate(architecture, weights, hard_reward), best_iteration


def optimize_architecture(
    architecture: str,
    scenario_name: str,
    states: Sequence[mixed.EpisodeState],
    cfg: HardReturnConfig,
) -> Tuple[mixed.Candidate, int, int]:
    best: Tuple[Tuple[float, int], int, mixed.Candidate, int] | None = None
    for restart in range(cfg.restarts):
        candidate, best_iteration = hard_return_restart(architecture, scenario_name, restart, states, cfg)
        rank = (candidate.training_reward, -restart)
        if best is None or rank > best[0]:
            best = (rank, restart, candidate, best_iteration)
    if best is None:
        raise RuntimeError(f"no optimized candidate for {scenario_name}:{architecture}")
    _rank, restart, candidate, best_iteration = best
    return candidate, restart, best_iteration


def hard_return_row(
    scenario: persistent.BoundaryScenario,
    architecture: str,
    cfg: HardReturnConfig,
) -> HardReturnRow:
    mixed_cfg = as_mixed_cfg(cfg)
    mixed_scenario = persistent.as_mixed_scenario(scenario)
    training_states = mixed.make_states(mixed_scenario, "hard_train", cfg.training_episodes, mixed_cfg)
    candidate, restart, best_iteration = optimize_architecture(architecture, scenario.name, training_states, cfg)
    selected_policy, rewards = mixed.select_policy(candidate, training_states, mixed_cfg)
    boundary = end_to_end.build_boundary_row(scenario, candidate, selected_policy, rewards, mixed_cfg)
    expected = stress.EXPECTED_SIGNATURES[scenario.name]
    return HardReturnRow(
        scenario=scenario.name,
        architecture=architecture,
        selected_policy=selected_policy,
        dependency_signature=boundary.dependency_signature,
        expected_signature=expected,
        best_restart=restart,
        best_iteration=best_iteration,
        hard_training_objective=candidate.training_reward,
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


def verdict_rows(rows: Sequence[HardReturnRow]) -> List[HardReturnVerdict]:
    verdicts = []
    for scenario in sorted({row.scenario for row in rows}):
        scenario_rows = [row for row in rows if row.scenario == scenario]
        expected = stress.EXPECTED_SIGNATURES[scenario]
        converged = sum(1 for row in scenario_rows if row.matches_expected_signature)
        architecture_count = len(scenario_rows)
        strict = converged == architecture_count
        hard_return_result = classify_hard_return_result(scenario, converged, architecture_count)
        verdicts.append(
            HardReturnVerdict(
                scenario=scenario,
                expected_signature=expected,
                converged_architectures=converged,
                architecture_count=architecture_count,
                strict_hard_return_convergence=strict,
                sum_rnn_signature=signature_for(scenario_rows, "sum_rnn"),
                scalar_rnn_signature=signature_for(scenario_rows, "scalar_rnn"),
                two_unit_rnn_signature=signature_for(scenario_rows, "two_unit_rnn"),
                recurrent_winners=sum(1 for row in scenario_rows if row.selected_policy == "recurrent_controller"),
                local_winners=sum(1 for row in scenario_rows if row.selected_policy == "task_local_probe"),
                greedy_winners=sum(1 for row in scenario_rows if row.selected_policy == "greedy_no_state"),
                mean_recurrent_reward=statistics.fmean(row.recurrent_training_reward for row in scenario_rows),
                mean_local_reward=statistics.fmean(row.local_training_reward for row in scenario_rows),
                hard_return_result=hard_return_result,
                supports_architecture_hard_return_audit=supports_hard_return_audit(
                    scenario,
                    converged,
                    architecture_count,
                    scenario_rows,
                    hard_return_result,
                ),
            )
        )
    return verdicts


def signature_for(rows: Sequence[HardReturnRow], architecture: str) -> str:
    return next(row.dependency_signature for row in rows if row.architecture == architecture)


def classify_hard_return_result(scenario: str, converged: int, architecture_count: int) -> str:
    if scenario in stress.SHARED_REGIMES:
        if converged == architecture_count:
            return "strict_hard_return_boundary_convergence"
        if converged > 0:
            return "partial_hard_return_boundary_convergence"
        return "no_hard_return_boundary_convergence"
    if scenario == "independent_hidden":
        if converged == architecture_count:
            return "hard_return_rejects_shared_recurrence"
        return "hard_return_control_false_positive"
    if scenario == "irrelevant_control":
        if converged == architecture_count:
            return "hard_return_rejects_hidden_state"
        return "hard_return_control_false_positive"
    raise ValueError(f"unknown scenario: {scenario}")


def supports_hard_return_audit(
    scenario: str,
    converged: int,
    architecture_count: int,
    rows: Sequence[HardReturnRow],
    hard_return_result: str,
) -> bool:
    if scenario in stress.SHARED_REGIMES:
        return (
            0 < converged <= architecture_count
            and all(row.selected_policy == "recurrent_controller" for row in rows)
            and hard_return_result
            in {
                "strict_hard_return_boundary_convergence",
                "partial_hard_return_boundary_convergence",
            }
        )
    if scenario == "independent_hidden":
        return (
            hard_return_result == "hard_return_rejects_shared_recurrence"
            and all(row.selected_policy == "task_local_probe" for row in rows)
        )
    if scenario == "irrelevant_control":
        return (
            hard_return_result == "hard_return_rejects_hidden_state"
            and all(row.selected_policy == "greedy_no_state" for row in rows)
        )
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(cfg: HardReturnConfig) -> Tuple[List[HardReturnRow], List[HardReturnVerdict]]:
    rows = [
        hard_return_row(scenario, architecture, cfg)
        for scenario in persistent.SCENARIOS
        for architecture in mixed.ARCHITECTURES
    ]
    return rows, verdict_rows(rows)


def write_csv(path: Path, rows: Iterable[object]) -> None:
    mixed.write_csv(path, rows)


def print_table(verdicts: Sequence[HardReturnVerdict]) -> None:
    headers = [
        "scenario",
        "converged_architectures",
        "architecture_count",
        "strict_hard_return_convergence",
        "hard_return_result",
        "supports_architecture_hard_return_audit",
    ]
    table_rows = []
    for verdict in verdicts:
        table_rows.append(
            [
                verdict.scenario,
                str(verdict.converged_architectures),
                str(verdict.architecture_count),
                str(verdict.strict_hard_return_convergence),
                verdict.hard_return_result,
                str(verdict.supports_architecture_hard_return_audit),
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


def supports_overall_audit(verdicts: Sequence[HardReturnVerdict]) -> bool:
    shared = [verdict for verdict in verdicts if verdict.scenario in stress.SHARED_REGIMES]
    return (
        all(verdict.supports_architecture_hard_return_audit for verdict in verdicts)
        and any(not verdict.strict_hard_return_convergence for verdict in shared)
    )


def parse_args() -> HardReturnConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=300)
    parser.add_argument("--training-episodes", type=int, default=400)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--horizon", type=int, default=8)
    parser.add_argument("--evidence-samples", type=int, default=9)
    parser.add_argument("--cue-accuracy", type=float, default=0.85)
    parser.add_argument("--shared-cue-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    parser.add_argument("--iterations", type=int, default=16)
    parser.add_argument("--population", type=int, default=220)
    parser.add_argument("--restarts", type=int, default=10)
    parser.add_argument("--initial-std", type=float, default=1.4)
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
    if args.iterations < 1:
        raise SystemExit("--iterations must be positive")
    if args.population < 3:
        raise SystemExit("--population must be at least 3")
    if args.restarts < 1:
        raise SystemExit("--restarts must be positive")
    if args.initial_std <= 0.0:
        raise SystemExit("--initial-std must be positive")
    return HardReturnConfig(
        episodes=args.episodes,
        training_episodes=args.training_episodes,
        seed=args.seed,
        horizon=args.horizon,
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
    summary_path = ARTIFACT_DIR / "architecture_hard_return_audit_summary.csv"
    verdict_path = ARTIFACT_DIR / "architecture_hard_return_audit_verdict.csv"
    results_path = ARTIFACT_DIR / "architecture_hard_return_audit_results.json"
    write_csv(summary_path, rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "summary": [asdict(row) for row in rows],
                "verdict": [asdict(row) for row in verdicts],
                "note": (
                    "No source-direction seeds, no smooth expected-return surrogate, "
                    "and no boundary-aware restart selection. Candidates and restarts "
                    "are ranked by realized recurrent training return only."
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
    return 0 if supports_overall_audit(verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
