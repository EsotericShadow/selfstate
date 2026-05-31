#!/usr/bin/env python3
"""Architecture online return-learner audit.

This is a stricter companion to architecture_hard_return_horizon_sweep.py.
The hard-return audit and horizon sweep showed that realized task return and
temporal pressure can select useful recurrent controllers without forcing the
self/tool boundary signature across architectures.

This experiment replaces batch cross-entropy search with an online-style
antithetic evolution-strategy learner. It updates weights from paired
perturbations ranked only by sampled episode return, uses fresh sampled batches
through training, selects restarts only by validation return, and applies the
same end-to-end boundary classifier afterward.

The purpose is not to prove that online RL cannot discover the boundary. It is
to test whether a minimal objective-only online return learner repairs the
hard-return failure without source-direction seeds, a smooth expected-return
surrogate, or boundary-aware selection.
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
SEED_OFFSET = 8111


@dataclass(frozen=True)
class OnlineReturnConfig:
    episodes: int = 160
    training_episodes: int = 220
    validation_episodes: int = 120
    batch_episodes: int = 90
    seed: int = 20260604
    horizon: int = 8
    evidence_samples: int = 9
    cue_accuracy: float = 0.85
    shared_cue_cost: float = 1.0
    local_probe_cost: float = 1.0
    epochs: int = 16
    perturbations: int = 50
    restarts: int = 4
    sigma: float = 0.45
    learning_rate: float = 0.07
    initial_std: float = 0.8
    lr_decay: float = 0.94
    sigma_decay: float = 0.96
    min_sigma: float = 0.06


@dataclass(frozen=True)
class OnlineReturnRow:
    scenario: str
    architecture: str
    selected_policy: str
    dependency_signature: str
    expected_signature: str
    best_restart: int
    online_training_objective: float
    validation_objective: float
    recurrent_training_reward: float
    local_training_reward: float
    greedy_training_reward: float
    safe_training_reward: float
    recurrent_local_gap: float
    latent_self_accuracy: float
    latent_world_accuracy: float
    action_0_positive_present_effect: float
    action_0_persistence: float
    action_1_positive_present_effect: float
    action_1_persistence: float
    matches_expected_signature: bool
    selected_weights: str


@dataclass(frozen=True)
class OnlineReturnVerdict:
    scenario: str
    expected_signature: str
    converged_architectures: int
    architecture_count: int
    strict_online_return_convergence: bool
    sum_rnn_signature: str
    scalar_rnn_signature: str
    two_unit_rnn_signature: str
    recurrent_winners: int
    local_winners: int
    greedy_winners: int
    mean_recurrent_reward: float
    mean_local_reward: float
    online_return_result: str
    supports_architecture_online_return_learner: bool


def as_mixed_cfg(cfg: OnlineReturnConfig) -> mixed.MixedSensorConfig:
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


def clamp_weights(weights: Sequence[float]) -> Tuple[float, ...]:
    return soft.clamp_weights(weights)


def reward_for_weights(
    states: Sequence[mixed.EpisodeState],
    architecture: str,
    weights: Sequence[float],
    cfg: OnlineReturnConfig,
) -> float:
    candidate = mixed.Candidate(architecture, tuple(weights), 0.0)
    return mixed.mean_recurrent_reward(states, candidate, as_mixed_cfg(cfg))


def online_restart(
    architecture: str,
    scenario: persistent.BoundaryScenario,
    restart: int,
    cfg: OnlineReturnConfig,
) -> Tuple[mixed.Candidate, float]:
    mixed_cfg = as_mixed_cfg(cfg)
    mixed_scenario = persistent.as_mixed_scenario(scenario)
    rng = random.Random(
        mixed.stable_name_seed(cfg.seed + SEED_OFFSET + restart * 173, scenario.name, architecture)
    )
    dimensions = soft.parameter_count(architecture)
    weights = [rng.gauss(0.0, cfg.initial_std) for _ in range(dimensions)]
    sigma = cfg.sigma
    learning_rate = cfg.learning_rate

    for epoch in range(cfg.epochs):
        batch_states = mixed.make_states(
            mixed_scenario,
            f"online_return_batch_{restart}_{epoch}",
            cfg.batch_episodes,
            mixed_cfg,
        )
        perturbation_vectors: List[List[float]] = []
        deltas = []
        for _ in range(cfg.perturbations):
            epsilon = [rng.gauss(0.0, 1.0) for _index in range(dimensions)]
            plus = clamp_weights(
                [weight + sigma * value for weight, value in zip(weights, epsilon)]
            )
            minus = clamp_weights(
                [weight - sigma * value for weight, value in zip(weights, epsilon)]
            )
            reward_plus = reward_for_weights(batch_states, architecture, plus, cfg)
            reward_minus = reward_for_weights(batch_states, architecture, minus, cfg)
            perturbation_vectors.append(epsilon)
            deltas.append(reward_plus - reward_minus)

        scale = statistics.pstdev(deltas) or 1.0
        gradient = [0.0 for _index in range(dimensions)]
        for epsilon, delta in zip(perturbation_vectors, deltas):
            normalized_delta = delta / scale
            for index, value in enumerate(epsilon):
                gradient[index] += normalized_delta * value
        gradient = [value / (cfg.perturbations * sigma) for value in gradient]
        weights = list(
            clamp_weights(
                [
                    weight + learning_rate * gradient_value
                    for weight, gradient_value in zip(weights, gradient)
                ]
            )
        )
        sigma = max(cfg.min_sigma, sigma * cfg.sigma_decay)
        learning_rate *= cfg.lr_decay

    training_states = mixed.make_states(
        mixed_scenario,
        "online_return_training_eval",
        cfg.training_episodes,
        mixed_cfg,
    )
    validation_states = mixed.make_states(
        mixed_scenario,
        "online_return_validation",
        cfg.validation_episodes,
        mixed_cfg,
    )
    training_reward = reward_for_weights(training_states, architecture, weights, cfg)
    validation_reward = reward_for_weights(validation_states, architecture, weights, cfg)
    return mixed.Candidate(architecture, tuple(weights), training_reward), validation_reward


def optimize_architecture(
    architecture: str,
    scenario: persistent.BoundaryScenario,
    cfg: OnlineReturnConfig,
) -> Tuple[mixed.Candidate, int, float]:
    best: Tuple[Tuple[float, float, int], int, mixed.Candidate, float] | None = None
    for restart in range(cfg.restarts):
        candidate, validation_reward = online_restart(architecture, scenario, restart, cfg)
        rank = (validation_reward, candidate.training_reward, -restart)
        if best is None or rank > best[0]:
            best = (rank, restart, candidate, validation_reward)
    if best is None:
        raise RuntimeError(f"no online return candidate for {scenario.name}:{architecture}")
    _rank, restart, candidate, validation_reward = best
    return candidate, restart, validation_reward


def online_return_row(
    scenario: persistent.BoundaryScenario,
    architecture: str,
    cfg: OnlineReturnConfig,
) -> OnlineReturnRow:
    mixed_cfg = as_mixed_cfg(cfg)
    mixed_scenario = persistent.as_mixed_scenario(scenario)
    training_states = mixed.make_states(
        mixed_scenario,
        "online_return_training_eval",
        cfg.training_episodes,
        mixed_cfg,
    )
    candidate, restart, validation_reward = optimize_architecture(architecture, scenario, cfg)
    selected_policy, rewards = mixed.select_policy(candidate, training_states, mixed_cfg)
    boundary = end_to_end.build_boundary_row(scenario, candidate, selected_policy, rewards, mixed_cfg)
    expected = stress.EXPECTED_SIGNATURES[scenario.name]
    return OnlineReturnRow(
        scenario=scenario.name,
        architecture=architecture,
        selected_policy=selected_policy,
        dependency_signature=boundary.dependency_signature,
        expected_signature=expected,
        best_restart=restart,
        online_training_objective=candidate.training_reward,
        validation_objective=validation_reward,
        recurrent_training_reward=rewards["recurrent_controller"],
        local_training_reward=rewards["task_local_probe"],
        greedy_training_reward=rewards["greedy_no_state"],
        safe_training_reward=rewards["safe_no_state"],
        recurrent_local_gap=rewards["recurrent_controller"] - rewards["task_local_probe"],
        latent_self_accuracy=boundary.latent_self_accuracy,
        latent_world_accuracy=boundary.latent_world_accuracy,
        action_0_positive_present_effect=boundary.action_0_positive_present_effect,
        action_0_persistence=boundary.action_0_persistence,
        action_1_positive_present_effect=boundary.action_1_positive_present_effect,
        action_1_persistence=boundary.action_1_persistence,
        matches_expected_signature=boundary.dependency_signature == expected,
        selected_weights=mixed.format_weights(candidate.weights),
    )


def verdict_rows(rows: Sequence[OnlineReturnRow]) -> List[OnlineReturnVerdict]:
    verdicts = []
    for scenario in sorted({row.scenario for row in rows}):
        scenario_rows = [row for row in rows if row.scenario == scenario]
        expected = stress.EXPECTED_SIGNATURES[scenario]
        converged = sum(1 for row in scenario_rows if row.matches_expected_signature)
        architecture_count = len(scenario_rows)
        strict = converged == architecture_count
        result = classify_online_result(scenario, converged, architecture_count)
        verdicts.append(
            OnlineReturnVerdict(
                scenario=scenario,
                expected_signature=expected,
                converged_architectures=converged,
                architecture_count=architecture_count,
                strict_online_return_convergence=strict,
                sum_rnn_signature=signature_for(scenario_rows, "sum_rnn"),
                scalar_rnn_signature=signature_for(scenario_rows, "scalar_rnn"),
                two_unit_rnn_signature=signature_for(scenario_rows, "two_unit_rnn"),
                recurrent_winners=sum(1 for row in scenario_rows if row.selected_policy == "recurrent_controller"),
                local_winners=sum(1 for row in scenario_rows if row.selected_policy == "task_local_probe"),
                greedy_winners=sum(1 for row in scenario_rows if row.selected_policy == "greedy_no_state"),
                mean_recurrent_reward=statistics.fmean(row.recurrent_training_reward for row in scenario_rows),
                mean_local_reward=statistics.fmean(row.local_training_reward for row in scenario_rows),
                online_return_result=result,
                supports_architecture_online_return_learner=supports_online_result(
                    scenario,
                    converged,
                    architecture_count,
                    scenario_rows,
                    result,
                ),
            )
        )
    return verdicts


def signature_for(rows: Sequence[OnlineReturnRow], architecture: str) -> str:
    return next(row.dependency_signature for row in rows if row.architecture == architecture)


def classify_online_result(scenario: str, converged: int, architecture_count: int) -> str:
    if scenario in stress.SHARED_REGIMES:
        if converged == architecture_count:
            return "strict_online_return_boundary_convergence"
        if converged > 0:
            return "partial_online_return_boundary_convergence"
        return "no_online_return_boundary_convergence"
    if scenario == "independent_hidden":
        if converged == architecture_count:
            return "online_return_rejects_shared_recurrence"
        return "online_return_control_false_positive"
    if scenario == "irrelevant_control":
        if converged == architecture_count:
            return "online_return_rejects_hidden_state"
        return "online_return_control_false_positive"
    raise ValueError(f"unknown scenario: {scenario}")


def supports_online_result(
    scenario: str,
    converged: int,
    architecture_count: int,
    rows: Sequence[OnlineReturnRow],
    result: str,
) -> bool:
    if scenario in stress.SHARED_REGIMES:
        return (
            result == "partial_online_return_boundary_convergence"
            and 0 < converged < architecture_count
            and any(row.selected_policy == "recurrent_controller" for row in rows)
        )
    if scenario == "independent_hidden":
        return (
            result == "online_return_rejects_shared_recurrence"
            and all(row.selected_policy == "task_local_probe" for row in rows)
        )
    if scenario == "irrelevant_control":
        return (
            result == "online_return_rejects_hidden_state"
            and all(row.selected_policy == "greedy_no_state" for row in rows)
        )
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: OnlineReturnConfig,
) -> Tuple[List[OnlineReturnRow], List[OnlineReturnVerdict]]:
    rows = [
        online_return_row(scenario, architecture, cfg)
        for scenario in persistent.SCENARIOS
        for architecture in mixed.ARCHITECTURES
    ]
    return rows, verdict_rows(rows)


def write_csv(path: Path, rows: Iterable[object]) -> None:
    mixed.write_csv(path, rows)


def print_table(verdicts: Sequence[OnlineReturnVerdict]) -> None:
    headers = [
        "scenario",
        "converged_architectures",
        "architecture_count",
        "strict_online_return_convergence",
        "online_return_result",
        "supports_architecture_online_return_learner",
    ]
    table_rows = []
    for verdict in verdicts:
        table_rows.append(
            [
                verdict.scenario,
                str(verdict.converged_architectures),
                str(verdict.architecture_count),
                str(verdict.strict_online_return_convergence),
                verdict.online_return_result,
                str(verdict.supports_architecture_online_return_learner),
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


def supports_overall_audit(verdicts: Sequence[OnlineReturnVerdict]) -> bool:
    shared = [verdict for verdict in verdicts if verdict.scenario in stress.SHARED_REGIMES]
    return (
        all(verdict.supports_architecture_online_return_learner for verdict in verdicts)
        and any(not verdict.strict_online_return_convergence for verdict in shared)
    )


def parse_args() -> OnlineReturnConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=160)
    parser.add_argument("--training-episodes", type=int, default=220)
    parser.add_argument("--validation-episodes", type=int, default=120)
    parser.add_argument("--batch-episodes", type=int, default=90)
    parser.add_argument("--seed", type=int, default=20260604)
    parser.add_argument("--horizon", type=int, default=8)
    parser.add_argument("--evidence-samples", type=int, default=9)
    parser.add_argument("--cue-accuracy", type=float, default=0.85)
    parser.add_argument("--shared-cue-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    parser.add_argument("--epochs", type=int, default=16)
    parser.add_argument("--perturbations", type=int, default=50)
    parser.add_argument("--restarts", type=int, default=4)
    parser.add_argument("--sigma", type=float, default=0.45)
    parser.add_argument("--learning-rate", type=float, default=0.07)
    parser.add_argument("--initial-std", type=float, default=0.8)
    parser.add_argument("--lr-decay", type=float, default=0.94)
    parser.add_argument("--sigma-decay", type=float, default=0.96)
    parser.add_argument("--min-sigma", type=float, default=0.06)
    args = parser.parse_args()
    if args.episodes < 1:
        raise SystemExit("--episodes must be at least 1")
    if args.training_episodes < 1:
        raise SystemExit("--training-episodes must be at least 1")
    if args.validation_episodes < 1:
        raise SystemExit("--validation-episodes must be at least 1")
    if args.batch_episodes < 1:
        raise SystemExit("--batch-episodes must be at least 1")
    if args.horizon < 1:
        raise SystemExit("--horizon must be at least 1")
    if args.evidence_samples < 1:
        raise SystemExit("--evidence-samples must be at least 1")
    if not 0.5 <= args.cue_accuracy <= 1.0:
        raise SystemExit("--cue-accuracy must be in [0.5, 1.0]")
    if args.epochs < 1:
        raise SystemExit("--epochs must be positive")
    if args.perturbations < 1:
        raise SystemExit("--perturbations must be positive")
    if args.restarts < 1:
        raise SystemExit("--restarts must be positive")
    if args.sigma <= 0.0:
        raise SystemExit("--sigma must be positive")
    if args.learning_rate <= 0.0:
        raise SystemExit("--learning-rate must be positive")
    if args.initial_std < 0.0:
        raise SystemExit("--initial-std must be nonnegative")
    if not 0.0 < args.lr_decay <= 1.0:
        raise SystemExit("--lr-decay must be in (0, 1]")
    if not 0.0 < args.sigma_decay <= 1.0:
        raise SystemExit("--sigma-decay must be in (0, 1]")
    if args.min_sigma <= 0.0:
        raise SystemExit("--min-sigma must be positive")
    return OnlineReturnConfig(
        episodes=args.episodes,
        training_episodes=args.training_episodes,
        validation_episodes=args.validation_episodes,
        batch_episodes=args.batch_episodes,
        seed=args.seed,
        horizon=args.horizon,
        evidence_samples=args.evidence_samples,
        cue_accuracy=args.cue_accuracy,
        shared_cue_cost=args.shared_cue_cost,
        local_probe_cost=args.local_probe_cost,
        epochs=args.epochs,
        perturbations=args.perturbations,
        restarts=args.restarts,
        sigma=args.sigma,
        learning_rate=args.learning_rate,
        initial_std=args.initial_std,
        lr_decay=args.lr_decay,
        sigma_decay=args.sigma_decay,
        min_sigma=args.min_sigma,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows, verdicts = run_experiment(cfg)
    summary_path = ARTIFACT_DIR / "architecture_online_return_learner_summary.csv"
    verdict_path = ARTIFACT_DIR / "architecture_online_return_learner_verdict.csv"
    results_path = ARTIFACT_DIR / "architecture_online_return_learner_results.json"
    write_csv(summary_path, rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "summary": [asdict(row) for row in rows],
                "verdict": [asdict(row) for row in verdicts],
                "note": (
                    "Online-style antithetic evolution-strategy learner. Updates, "
                    "restart selection, and policy selection use realized return only; "
                    "no source-direction seeds, smooth expected-return surrogate, or "
                    "boundary-aware selection are used."
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
