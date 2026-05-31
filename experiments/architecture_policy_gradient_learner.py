#!/usr/bin/env python3
"""Architecture policy-gradient learner.

This follows architecture_online_return_learner.py. The previous online
return learner used antithetic perturbation updates and still left the shared
boundary regimes only partially convergent. This experiment asks whether a
stochastic policy-gradient learner can recover the missing boundary signatures
without source-direction seeds, a smooth expected-return surrogate, or
boundary-aware selection.

Each architecture is trained as a stochastic recurrent policy. It samples risky
or safe action from the recurrent logit, updates by a score-function gradient
from sampled episode return, selects restarts by sampled validation return, and
then applies the same deterministic end-to-end boundary classifier afterward.
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
import architecture_soft_return_optimizer as soft
import end_to_end_boundary_probe as end_to_end
import mixed_sensor_recurrent_filter as mixed
import persistent_action_boundary_probe as persistent


ARTIFACT_DIR = Path("artifacts")
SEED_OFFSET = 9131
VALIDATION_REPLICATES = 3


@dataclass(frozen=True)
class PolicyGradientConfig:
    episodes: int = 200
    training_episodes: int = 400
    validation_episodes: int = 240
    batch_episodes: int = 128
    seed: int = 20260605
    horizon: int = 8
    evidence_samples: int = 9
    cue_accuracy: float = 0.85
    shared_cue_cost: float = 1.0
    local_probe_cost: float = 1.0
    epochs: int = 32
    restarts: int = 5
    temperature: float = 1.8
    learning_rate: float = 0.12
    lr_decay: float = 0.96
    initial_std: float = 0.8
    finite_diff_epsilon: float = 0.02
    max_grad_norm: float = 4.0


@dataclass(frozen=True)
class PolicyGradientRow:
    scenario: str
    architecture: str
    selected_policy: str
    dependency_signature: str
    expected_signature: str
    best_restart: int
    sampled_validation_return: float
    deterministic_training_reward: float
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
class PolicyGradientVerdict:
    scenario: str
    expected_signature: str
    converged_architectures: int
    architecture_count: int
    strict_policy_gradient_convergence: bool
    sum_rnn_signature: str
    scalar_rnn_signature: str
    two_unit_rnn_signature: str
    recurrent_winners: int
    local_winners: int
    greedy_winners: int
    mean_recurrent_reward: float
    mean_local_reward: float
    policy_gradient_result: str
    supports_architecture_policy_gradient_learner: bool


def as_mixed_cfg(cfg: PolicyGradientConfig) -> mixed.MixedSensorConfig:
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


def candidate_from_weights(architecture: str, weights: Sequence[float]) -> mixed.Candidate:
    return mixed.Candidate(architecture, tuple(weights), 0.0)


def sigmoid(value: float) -> float:
    if value >= 0.0:
        z = math.exp(-value)
        return 1.0 / (1.0 + z)
    z = math.exp(value)
    return z / (1.0 + z)


def stochastic_episode_return(
    state: mixed.EpisodeState,
    risky: bool,
    cfg: PolicyGradientConfig,
) -> float:
    total = -cfg.shared_cue_cost
    for hidden_success in state.step_success:
        if risky:
            total += mixed.RISKY_SUCCESS_REWARD if hidden_success else mixed.RISKY_FAILURE_REWARD
        else:
            total += mixed.SAFE_REWARD
    return total


def logit_gradient(
    architecture: str,
    weights: Sequence[float],
    observations: Sequence[Tuple[float, float]],
    cfg: PolicyGradientConfig,
) -> List[float]:
    gradient = []
    for index in range(len(weights)):
        plus = list(weights)
        minus = list(weights)
        plus[index] += cfg.finite_diff_epsilon
        minus[index] -= cfg.finite_diff_epsilon
        plus_logit = mixed.recurrent_logit(
            candidate_from_weights(architecture, clamp_weights(plus)),
            observations,
        )
        minus_logit = mixed.recurrent_logit(
            candidate_from_weights(architecture, clamp_weights(minus)),
            observations,
        )
        gradient.append((plus_logit - minus_logit) / (2.0 * cfg.finite_diff_epsilon))
    return gradient


def sampled_policy_return(
    states: Sequence[mixed.EpisodeState],
    architecture: str,
    weights: Sequence[float],
    rng: random.Random,
    cfg: PolicyGradientConfig,
) -> float:
    candidate = candidate_from_weights(architecture, weights)
    returns = []
    for state in states:
        logit = mixed.recurrent_logit(candidate, state.mixed_observations)
        probability_risky = sigmoid(logit / cfg.temperature)
        returns.append(stochastic_episode_return(state, rng.random() < probability_risky, cfg))
    return statistics.fmean(returns)


def train_restart(
    architecture: str,
    scenario: persistent.BoundaryScenario,
    restart: int,
    cfg: PolicyGradientConfig,
) -> Tuple[mixed.Candidate, float]:
    mixed_cfg = as_mixed_cfg(cfg)
    mixed_scenario = persistent.as_mixed_scenario(scenario)
    rng = random.Random(
        mixed.stable_name_seed(cfg.seed + SEED_OFFSET + restart * 197, scenario.name, architecture)
    )
    dimensions = soft.parameter_count(architecture)
    weights = list(clamp_weights(rng.gauss(0.0, cfg.initial_std) for _ in range(dimensions)))
    learning_rate = cfg.learning_rate

    for epoch in range(cfg.epochs):
        batch_states = mixed.make_states(
            mixed_scenario,
            f"policy_gradient_batch_{restart}_{epoch}",
            cfg.batch_episodes,
            mixed_cfg,
        )
        samples = []
        candidate = candidate_from_weights(architecture, weights)
        for state in batch_states:
            logit = mixed.recurrent_logit(candidate, state.mixed_observations)
            probability_risky = sigmoid(logit / cfg.temperature)
            risky = rng.random() < probability_risky
            episode_return = stochastic_episode_return(state, risky, cfg)
            samples.append((state, probability_risky, 1.0 if risky else 0.0, episode_return))

        baseline = statistics.fmean(sample[3] for sample in samples)
        gradient = [0.0 for _index in range(dimensions)]
        for state, probability_risky, action, episode_return in samples:
            advantage = episode_return - baseline
            logit_grad = logit_gradient(architecture, weights, state.mixed_observations, cfg)
            coefficient = advantage * (action - probability_risky) / cfg.temperature
            for index, value in enumerate(logit_grad):
                gradient[index] += coefficient * value
        gradient = [value / len(samples) for value in gradient]
        norm = math.sqrt(sum(value * value for value in gradient))
        if norm > cfg.max_grad_norm:
            gradient = [value * cfg.max_grad_norm / norm for value in gradient]
        weights = list(
            clamp_weights(
                [
                    weight + learning_rate * gradient_value
                    for weight, gradient_value in zip(weights, gradient)
                ]
            )
        )
        learning_rate *= cfg.lr_decay

    training_states = mixed.make_states(
        mixed_scenario,
        "policy_gradient_training_eval",
        cfg.training_episodes,
        mixed_cfg,
    )
    validation_states = mixed.make_states(
        mixed_scenario,
        "policy_gradient_validation",
        cfg.validation_episodes,
        mixed_cfg,
    )
    validation_return = statistics.fmean(
        sampled_policy_return(
            validation_states,
            architecture,
            weights,
            random.Random(
                mixed.stable_name_seed(
                    cfg.seed + 12000 + replicate + restart * 17,
                    scenario.name,
                    architecture,
                )
            ),
            cfg,
        )
        for replicate in range(VALIDATION_REPLICATES)
    )
    deterministic_reward = mixed.mean_recurrent_reward(
        training_states,
        candidate_from_weights(architecture, weights),
        mixed_cfg,
    )
    return mixed.Candidate(architecture, tuple(weights), deterministic_reward), validation_return


def optimize_architecture(
    architecture: str,
    scenario: persistent.BoundaryScenario,
    cfg: PolicyGradientConfig,
) -> Tuple[mixed.Candidate, int, float]:
    best: Tuple[Tuple[float, float, int], int, mixed.Candidate, float] | None = None
    for restart in range(cfg.restarts):
        candidate, validation_return = train_restart(architecture, scenario, restart, cfg)
        rank = (validation_return, candidate.training_reward, -restart)
        if best is None or rank > best[0]:
            best = (rank, restart, candidate, validation_return)
    if best is None:
        raise RuntimeError(f"no policy-gradient candidate for {scenario.name}:{architecture}")
    _rank, restart, candidate, validation_return = best
    return candidate, restart, validation_return


def policy_gradient_row(
    scenario: persistent.BoundaryScenario,
    architecture: str,
    cfg: PolicyGradientConfig,
) -> PolicyGradientRow:
    mixed_cfg = as_mixed_cfg(cfg)
    mixed_scenario = persistent.as_mixed_scenario(scenario)
    training_states = mixed.make_states(
        mixed_scenario,
        "policy_gradient_training_eval",
        cfg.training_episodes,
        mixed_cfg,
    )
    candidate, restart, validation_return = optimize_architecture(architecture, scenario, cfg)
    selected_policy, rewards = mixed.select_policy(candidate, training_states, mixed_cfg)
    boundary = end_to_end.build_boundary_row(scenario, candidate, selected_policy, rewards, mixed_cfg)
    expected = stress.EXPECTED_SIGNATURES[scenario.name]
    return PolicyGradientRow(
        scenario=scenario.name,
        architecture=architecture,
        selected_policy=selected_policy,
        dependency_signature=boundary.dependency_signature,
        expected_signature=expected,
        best_restart=restart,
        sampled_validation_return=validation_return,
        deterministic_training_reward=candidate.training_reward,
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


def verdict_rows(rows: Sequence[PolicyGradientRow]) -> List[PolicyGradientVerdict]:
    verdicts = []
    for scenario in sorted({row.scenario for row in rows}):
        scenario_rows = [row for row in rows if row.scenario == scenario]
        expected = stress.EXPECTED_SIGNATURES[scenario]
        converged = sum(1 for row in scenario_rows if row.matches_expected_signature)
        architecture_count = len(scenario_rows)
        strict = converged == architecture_count
        result = classify_policy_gradient_result(scenario, strict)
        verdicts.append(
            PolicyGradientVerdict(
                scenario=scenario,
                expected_signature=expected,
                converged_architectures=converged,
                architecture_count=architecture_count,
                strict_policy_gradient_convergence=strict,
                sum_rnn_signature=signature_for(scenario_rows, "sum_rnn"),
                scalar_rnn_signature=signature_for(scenario_rows, "scalar_rnn"),
                two_unit_rnn_signature=signature_for(scenario_rows, "two_unit_rnn"),
                recurrent_winners=sum(1 for row in scenario_rows if row.selected_policy == "recurrent_controller"),
                local_winners=sum(1 for row in scenario_rows if row.selected_policy == "task_local_probe"),
                greedy_winners=sum(1 for row in scenario_rows if row.selected_policy == "greedy_no_state"),
                mean_recurrent_reward=statistics.fmean(row.recurrent_training_reward for row in scenario_rows),
                mean_local_reward=statistics.fmean(row.local_training_reward for row in scenario_rows),
                policy_gradient_result=result,
                supports_architecture_policy_gradient_learner=supports_policy_gradient_result(
                    scenario,
                    strict,
                    scenario_rows,
                    result,
                ),
            )
        )
    return verdicts


def signature_for(rows: Sequence[PolicyGradientRow], architecture: str) -> str:
    return next(row.dependency_signature for row in rows if row.architecture == architecture)


def classify_policy_gradient_result(scenario: str, strict: bool) -> str:
    if scenario in stress.SHARED_REGIMES and strict:
        return "policy_gradient_discovers_shared_boundary"
    if scenario == "independent_hidden" and strict:
        return "policy_gradient_rejects_shared_recurrence"
    if scenario == "irrelevant_control" and strict:
        return "policy_gradient_rejects_hidden_state"
    return "policy_gradient_partial_or_failed_discovery"


def supports_policy_gradient_result(
    scenario: str,
    strict: bool,
    rows: Sequence[PolicyGradientRow],
    result: str,
) -> bool:
    if scenario in stress.SHARED_REGIMES:
        return (
            strict
            and result == "policy_gradient_discovers_shared_boundary"
            and all(row.selected_policy == "recurrent_controller" for row in rows)
        )
    if scenario == "independent_hidden":
        return (
            strict
            and result == "policy_gradient_rejects_shared_recurrence"
            and all(row.selected_policy == "task_local_probe" for row in rows)
        )
    if scenario == "irrelevant_control":
        return (
            strict
            and result == "policy_gradient_rejects_hidden_state"
            and all(row.selected_policy == "greedy_no_state" for row in rows)
        )
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: PolicyGradientConfig,
) -> Tuple[List[PolicyGradientRow], List[PolicyGradientVerdict]]:
    rows = [
        policy_gradient_row(scenario, architecture, cfg)
        for scenario in persistent.SCENARIOS
        for architecture in mixed.ARCHITECTURES
    ]
    return rows, verdict_rows(rows)


def write_csv(path: Path, rows: Iterable[object]) -> None:
    mixed.write_csv(path, rows)


def print_table(verdicts: Sequence[PolicyGradientVerdict]) -> None:
    headers = [
        "scenario",
        "converged_architectures",
        "architecture_count",
        "strict_policy_gradient_convergence",
        "policy_gradient_result",
        "supports_architecture_policy_gradient_learner",
    ]
    table_rows = []
    for verdict in verdicts:
        table_rows.append(
            [
                verdict.scenario,
                str(verdict.converged_architectures),
                str(verdict.architecture_count),
                str(verdict.strict_policy_gradient_convergence),
                verdict.policy_gradient_result,
                str(verdict.supports_architecture_policy_gradient_learner),
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


def parse_args() -> PolicyGradientConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=200)
    parser.add_argument("--training-episodes", type=int, default=400)
    parser.add_argument("--validation-episodes", type=int, default=240)
    parser.add_argument("--batch-episodes", type=int, default=128)
    parser.add_argument("--seed", type=int, default=20260605)
    parser.add_argument("--horizon", type=int, default=8)
    parser.add_argument("--evidence-samples", type=int, default=9)
    parser.add_argument("--cue-accuracy", type=float, default=0.85)
    parser.add_argument("--shared-cue-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    parser.add_argument("--epochs", type=int, default=32)
    parser.add_argument("--restarts", type=int, default=5)
    parser.add_argument("--temperature", type=float, default=1.8)
    parser.add_argument("--learning-rate", type=float, default=0.12)
    parser.add_argument("--lr-decay", type=float, default=0.96)
    parser.add_argument("--initial-std", type=float, default=0.8)
    parser.add_argument("--finite-diff-epsilon", type=float, default=0.02)
    parser.add_argument("--max-grad-norm", type=float, default=4.0)
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
    if args.restarts < 1:
        raise SystemExit("--restarts must be positive")
    if args.temperature <= 0.0:
        raise SystemExit("--temperature must be positive")
    if args.learning_rate <= 0.0:
        raise SystemExit("--learning-rate must be positive")
    if not 0.0 < args.lr_decay <= 1.0:
        raise SystemExit("--lr-decay must be in (0, 1]")
    if args.initial_std < 0.0:
        raise SystemExit("--initial-std must be nonnegative")
    if args.finite_diff_epsilon <= 0.0:
        raise SystemExit("--finite-diff-epsilon must be positive")
    if args.max_grad_norm <= 0.0:
        raise SystemExit("--max-grad-norm must be positive")
    return PolicyGradientConfig(
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
        restarts=args.restarts,
        temperature=args.temperature,
        learning_rate=args.learning_rate,
        lr_decay=args.lr_decay,
        initial_std=args.initial_std,
        finite_diff_epsilon=args.finite_diff_epsilon,
        max_grad_norm=args.max_grad_norm,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows, verdicts = run_experiment(cfg)
    summary_path = ARTIFACT_DIR / "architecture_policy_gradient_learner_summary.csv"
    verdict_path = ARTIFACT_DIR / "architecture_policy_gradient_learner_verdict.csv"
    results_path = ARTIFACT_DIR / "architecture_policy_gradient_learner_results.json"
    write_csv(summary_path, rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "summary": [asdict(row) for row in rows],
                "verdict": [asdict(row) for row in verdicts],
                "note": (
                    "Stochastic score-function policy-gradient learner. Training "
                    "updates and restart selection use sampled returns; no source-direction "
                    "seeds, smooth expected-return surrogate, or boundary-aware selection "
                    "are used."
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
    return 0 if all(verdict.supports_architecture_policy_gradient_learner for verdict in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
