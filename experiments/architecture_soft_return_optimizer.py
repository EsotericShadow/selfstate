#!/usr/bin/env python3
"""Architecture soft-return optimizer.

This is a stricter companion to architecture_capacity_probe.py. The capacity
probe showed that weaker recurrent architectures can represent the boundary
when source-direction seeds are supplied. This experiment removes those seeds.

Each architecture is optimized from random Gaussian starts with a cross-entropy
method ranked mainly by a differentiable expected-return surrogate, with a small
realized-return term. The optimizer is still toy and simulator-facing, not full
online RL, but it is not handed the source A or source B directions. The
question is whether a stronger training method can discover the same boundary
signatures that random-start search missed. Restarts are selected by optimizer
objective, not by the post-hoc boundary signature.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

import architecture_boundary_stress as stress
import end_to_end_boundary_probe as end_to_end
import mixed_sensor_recurrent_filter as mixed
import persistent_action_boundary_probe as persistent


ARTIFACT_DIR = Path("artifacts")
SEED_OFFSET = 1221
CLAMP = 4.0
ELITE_FRACTION = 0.12
STD_DECAY = 0.8
MIN_STD = 0.04


@dataclass(frozen=True)
class SoftOptimizerConfig:
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
    temperature: float = 2.5
    initial_std: float = 1.4


@dataclass(frozen=True)
class SoftOptimizerRow:
    scenario: str
    architecture: str
    selected_policy: str
    dependency_signature: str
    expected_signature: str
    best_restart: int
    best_iteration: int
    soft_training_objective: float
    restart_selection_objective: float
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
class SoftOptimizerVerdict:
    scenario: str
    expected_signature: str
    converged_architectures: int
    architecture_count: int
    strict_optimizer_convergence: bool
    sum_rnn_signature: str
    scalar_rnn_signature: str
    two_unit_rnn_signature: str
    recurrent_winners: int
    local_winners: int
    greedy_winners: int
    mean_recurrent_reward: float
    mean_local_reward: float
    optimizer_result: str
    supports_architecture_soft_optimizer_result: bool


def as_mixed_cfg(cfg: SoftOptimizerConfig) -> mixed.MixedSensorConfig:
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


def parameter_count(architecture: str) -> int:
    if architecture == "sum_rnn":
        return 5
    if architecture == "scalar_rnn":
        return 6
    if architecture == "two_unit_rnn":
        return 11
    raise ValueError(f"unknown architecture: {architecture}")


def candidate_from_weights(architecture: str, weights: Sequence[float]) -> mixed.Candidate:
    return mixed.Candidate(architecture, tuple(weights), 0.0)


def clamp_weights(weights: Sequence[float]) -> Tuple[float, ...]:
    return tuple(max(-CLAMP, min(CLAMP, weight)) for weight in weights)


def sigmoid(value: float) -> float:
    if value >= 0.0:
        z = math.exp(-value)
        return 1.0 / (1.0 + z)
    z = math.exp(value)
    return z / (1.0 + z)


def soft_expected_return(
    states: Sequence[mixed.EpisodeState],
    candidate: mixed.Candidate,
    cfg: SoftOptimizerConfig,
) -> float:
    total = 0.0
    for state in states:
        probability_risky = sigmoid(mixed.recurrent_logit(candidate, state.mixed_observations) / cfg.temperature)
        reward = -cfg.shared_cue_cost
        for success in state.step_success:
            risky_reward = mixed.RISKY_SUCCESS_REWARD if success else mixed.RISKY_FAILURE_REWARD
            reward += probability_risky * risky_reward + (1.0 - probability_risky) * mixed.SAFE_REWARD
        total += reward
    return total / len(states)


def optimize_restart(
    architecture: str,
    scenario_name: str,
    restart: int,
    states: Sequence[mixed.EpisodeState],
    cfg: SoftOptimizerConfig,
) -> Tuple[mixed.Candidate, float, int]:
    rng = random.Random(mixed.stable_name_seed(cfg.seed + SEED_OFFSET + restart * 97, scenario_name, architecture))
    dimensions = parameter_count(architecture)
    mean = [0.0 for _ in range(dimensions)]
    std = [cfg.initial_std for _ in range(dimensions)]
    best: Tuple[float, Tuple[float, ...], float, int] | None = None

    for iteration in range(cfg.iterations):
        scored = []
        for _ in range(cfg.population):
            weights = clamp_weights(rng.gauss(mean[index], std[index]) for index in range(dimensions))
            candidate = candidate_from_weights(architecture, weights)
            soft_score = soft_expected_return(states, candidate, cfg)
            hard_reward = mixed.mean_recurrent_reward(states, candidate, as_mixed_cfg(cfg))
            ranking_score = soft_score + 0.05 * hard_reward
            scored.append((ranking_score, weights, soft_score, hard_reward))
            if best is None or ranking_score > best[0]:
                best = (ranking_score, weights, soft_score, iteration)
        scored.sort(reverse=True, key=lambda item: item[0])
        elite_count = max(3, int(cfg.population * ELITE_FRACTION))
        elites = [weights for _score, weights, _soft, _hard in scored[:elite_count]]
        mean = [statistics.fmean(weights[index] for weights in elites) for index in range(dimensions)]
        std = [
            max(MIN_STD, statistics.pstdev(weights[index] for weights in elites) * STD_DECAY)
            for index in range(dimensions)
        ]

    if best is None:
        raise RuntimeError(f"no soft optimizer candidate for {scenario_name}:{architecture}:{restart}")
    _rank, weights, soft_score, best_iteration = best
    hard_reward = mixed.mean_recurrent_reward(states, candidate_from_weights(architecture, weights), as_mixed_cfg(cfg))
    return mixed.Candidate(architecture, weights, hard_reward), soft_score, best_iteration


def optimizer_selection_objective(soft_score: float, recurrent_reward: float) -> float:
    return soft_score + 0.05 * recurrent_reward


def optimize_architecture(
    architecture: str,
    scenario_name: str,
    states: Sequence[mixed.EpisodeState],
    cfg: SoftOptimizerConfig,
) -> Tuple[mixed.Candidate, int, float, float, int]:
    best: Tuple[Tuple[float, float, int], int, mixed.Candidate, float, float, int] | None = None
    mixed_cfg = as_mixed_cfg(cfg)
    for restart in range(cfg.restarts):
        candidate, soft_score, best_iteration = optimize_restart(architecture, scenario_name, restart, states, cfg)
        selected_policy, rewards = mixed.select_policy(candidate, states, mixed_cfg)
        selection_objective = optimizer_selection_objective(soft_score, rewards["recurrent_controller"])
        rank = (selection_objective, rewards["recurrent_controller"], -restart)
        if best is None or rank > best[0]:
            best = (rank, restart, candidate, soft_score, selection_objective, best_iteration)
    if best is None:
        raise RuntimeError(f"no optimized candidate for {scenario_name}:{architecture}")
    _rank, restart, candidate, soft_score, selection_objective, best_iteration = best
    return candidate, restart, soft_score, selection_objective, best_iteration


def optimizer_row(
    scenario: persistent.BoundaryScenario,
    architecture: str,
    cfg: SoftOptimizerConfig,
) -> SoftOptimizerRow:
    mixed_cfg = as_mixed_cfg(cfg)
    mixed_scenario = persistent.as_mixed_scenario(scenario)
    training_states = mixed.make_states(mixed_scenario, "train", cfg.training_episodes, mixed_cfg)
    candidate, restart, soft_score, selection_objective, best_iteration = optimize_architecture(
        architecture,
        scenario.name,
        training_states,
        cfg,
    )
    selected_policy, rewards = mixed.select_policy(candidate, training_states, mixed_cfg)
    boundary = end_to_end.build_boundary_row(scenario, candidate, selected_policy, rewards, mixed_cfg)
    expected = stress.EXPECTED_SIGNATURES[scenario.name]
    return SoftOptimizerRow(
        scenario=scenario.name,
        architecture=architecture,
        selected_policy=selected_policy,
        dependency_signature=boundary.dependency_signature,
        expected_signature=expected,
        best_restart=restart,
        best_iteration=best_iteration,
        soft_training_objective=soft_score,
        restart_selection_objective=selection_objective,
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


def verdict_rows(rows: Sequence[SoftOptimizerRow]) -> List[SoftOptimizerVerdict]:
    verdicts = []
    for scenario in sorted({row.scenario for row in rows}):
        scenario_rows = [row for row in rows if row.scenario == scenario]
        expected = stress.EXPECTED_SIGNATURES[scenario]
        converged = sum(1 for row in scenario_rows if row.matches_expected_signature)
        architecture_count = len(scenario_rows)
        strict = converged == architecture_count
        optimizer_result = classify_optimizer_result(scenario, strict, scenario_rows)
        verdicts.append(
            SoftOptimizerVerdict(
                scenario=scenario,
                expected_signature=expected,
                converged_architectures=converged,
                architecture_count=architecture_count,
                strict_optimizer_convergence=strict,
                sum_rnn_signature=signature_for(scenario_rows, "sum_rnn"),
                scalar_rnn_signature=signature_for(scenario_rows, "scalar_rnn"),
                two_unit_rnn_signature=signature_for(scenario_rows, "two_unit_rnn"),
                recurrent_winners=sum(1 for row in scenario_rows if row.selected_policy == "recurrent_controller"),
                local_winners=sum(1 for row in scenario_rows if row.selected_policy == "task_local_probe"),
                greedy_winners=sum(1 for row in scenario_rows if row.selected_policy == "greedy_no_state"),
                mean_recurrent_reward=statistics.fmean(row.recurrent_training_reward for row in scenario_rows),
                mean_local_reward=statistics.fmean(row.local_training_reward for row in scenario_rows),
                optimizer_result=optimizer_result,
                supports_architecture_soft_optimizer_result=supports_optimizer_result(
                    scenario,
                    strict,
                    scenario_rows,
                    optimizer_result,
                ),
            )
        )
    return verdicts


def signature_for(rows: Sequence[SoftOptimizerRow], architecture: str) -> str:
    return next(row.dependency_signature for row in rows if row.architecture == architecture)


def classify_optimizer_result(
    scenario: str,
    strict: bool,
    rows: Sequence[SoftOptimizerRow],
) -> str:
    if scenario in stress.SHARED_REGIMES and strict:
        return "soft_optimizer_discovers_shared_boundary"
    if scenario == "independent_hidden" and strict:
        return "soft_optimizer_rejects_shared_recurrence"
    if scenario == "irrelevant_control" and strict:
        return "soft_optimizer_rejects_hidden_state"
    return "soft_optimizer_partial_or_failed_discovery"


def supports_optimizer_result(
    scenario: str,
    strict: bool,
    rows: Sequence[SoftOptimizerRow],
    optimizer_result: str,
) -> bool:
    if scenario in stress.SHARED_REGIMES:
        return (
            strict
            and optimizer_result == "soft_optimizer_discovers_shared_boundary"
            and all(row.selected_policy == "recurrent_controller" for row in rows)
        )
    if scenario == "independent_hidden":
        return (
            strict
            and optimizer_result == "soft_optimizer_rejects_shared_recurrence"
            and all(row.selected_policy == "task_local_probe" for row in rows)
        )
    if scenario == "irrelevant_control":
        return (
            strict
            and optimizer_result == "soft_optimizer_rejects_hidden_state"
            and all(row.selected_policy == "greedy_no_state" for row in rows)
        )
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: SoftOptimizerConfig,
) -> Tuple[List[SoftOptimizerRow], List[SoftOptimizerVerdict]]:
    rows = [
        optimizer_row(scenario, architecture, cfg)
        for scenario in persistent.SCENARIOS
        for architecture in mixed.ARCHITECTURES
    ]
    return rows, verdict_rows(rows)


def write_csv(path: Path, rows: Iterable[object]) -> None:
    mixed.write_csv(path, rows)


def print_table(verdicts: Sequence[SoftOptimizerVerdict]) -> None:
    headers = [
        "scenario",
        "converged_architectures",
        "architecture_count",
        "strict_optimizer_convergence",
        "optimizer_result",
        "supports_architecture_soft_optimizer_result",
    ]
    table_rows = []
    for verdict in verdicts:
        table_rows.append(
            [
                verdict.scenario,
                str(verdict.converged_architectures),
                str(verdict.architecture_count),
                str(verdict.strict_optimizer_convergence),
                verdict.optimizer_result,
                str(verdict.supports_architecture_soft_optimizer_result),
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


def parse_args() -> SoftOptimizerConfig:
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
    parser.add_argument("--temperature", type=float, default=2.5)
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
    if args.temperature <= 0.0:
        raise SystemExit("--temperature must be positive")
    if args.initial_std <= 0.0:
        raise SystemExit("--initial-std must be positive")
    return SoftOptimizerConfig(
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
        temperature=args.temperature,
        initial_std=args.initial_std,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows, verdicts = run_experiment(cfg)
    summary_path = ARTIFACT_DIR / "architecture_soft_return_optimizer_summary.csv"
    verdict_path = ARTIFACT_DIR / "architecture_soft_return_optimizer_verdict.csv"
    results_path = ARTIFACT_DIR / "architecture_soft_return_optimizer_results.json"
    write_csv(summary_path, rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "summary": [asdict(row) for row in rows],
                "verdict": [asdict(row) for row in verdicts],
                "note": (
                    "No source-direction seeds; optimized with a differentiable "
                    "expected-return surrogate plus a small realized-return ranking term. "
                    "Restarts are selected by optimizer objective, not by boundary signature."
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
    return 0 if all(verdict.supports_architecture_soft_optimizer_result for verdict in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
