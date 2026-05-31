#!/usr/bin/env python3
"""Architecture policy-gradient seed sweep.

This is a robustness audit for architecture_policy_gradient_learner.py. Report
56 showed strict boundary convergence for one seed. This sweep repeats the same
policy-gradient learner across several independent seeds and asks whether that
convergence is seed-stable.

The audit uses the same end-to-end boundary classifier. It is deliberately not
allowed to pass by averaging away failures: each scenario reports convergence
by seed and whether every seed reaches strict architecture convergence.
"""

from __future__ import annotations

import argparse
import json
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

import architecture_boundary_stress as stress
import architecture_policy_gradient_learner as pg
import mixed_sensor_recurrent_filter as mixed


ARTIFACT_DIR = Path("artifacts")
DEFAULT_SEEDS = (20260605, 20260606, 20260607, 20260608, 20260609)


@dataclass(frozen=True)
class PolicyGradientSeedConfig:
    seeds: Tuple[int, ...] = DEFAULT_SEEDS
    episodes: int = 200
    training_episodes: int = 400
    validation_episodes: int = 240
    batch_episodes: int = 128
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
class PolicyGradientSeedRow:
    seed: int
    scenario: str
    architecture: str
    selected_policy: str
    dependency_signature: str
    expected_signature: str
    sampled_validation_return: float
    deterministic_training_reward: float
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
class PolicyGradientSeedVerdict:
    scenario: str
    expected_signature: str
    seed_count: int
    architecture_count: int
    strict_seed_count: int
    total_converged_architectures: int
    total_architecture_count: int
    strict_all_seeds: bool
    convergence_by_seed: str
    sum_rnn_signature_by_seed: str
    scalar_signature_by_seed: str
    two_unit_signature_by_seed: str
    mean_recurrent_reward: float
    mean_local_reward: float
    policy_gradient_seed_result: str
    supports_architecture_policy_gradient_seed_sweep: bool


def parse_seeds(raw: str) -> Tuple[int, ...]:
    seeds = tuple(int(part.strip()) for part in raw.split(",") if part.strip())
    if not seeds:
        raise SystemExit("--seeds must contain at least one integer")
    if len(set(seeds)) != len(seeds):
        raise SystemExit("--seeds must not contain duplicates")
    return seeds


def pg_cfg_for_seed(seed: int, base: PolicyGradientSeedConfig) -> pg.PolicyGradientConfig:
    return pg.PolicyGradientConfig(
        episodes=base.episodes,
        training_episodes=base.training_episodes,
        validation_episodes=base.validation_episodes,
        batch_episodes=base.batch_episodes,
        seed=seed,
        horizon=base.horizon,
        evidence_samples=base.evidence_samples,
        cue_accuracy=base.cue_accuracy,
        shared_cue_cost=base.shared_cue_cost,
        local_probe_cost=base.local_probe_cost,
        epochs=base.epochs,
        restarts=base.restarts,
        temperature=base.temperature,
        learning_rate=base.learning_rate,
        lr_decay=base.lr_decay,
        initial_std=base.initial_std,
        finite_diff_epsilon=base.finite_diff_epsilon,
        max_grad_norm=base.max_grad_norm,
    )


def run_seed(seed: int, cfg: PolicyGradientSeedConfig) -> List[PolicyGradientSeedRow]:
    rows, _verdicts = pg.run_experiment(pg_cfg_for_seed(seed, cfg))
    return [
        PolicyGradientSeedRow(
            seed=seed,
            scenario=row.scenario,
            architecture=row.architecture,
            selected_policy=row.selected_policy,
            dependency_signature=row.dependency_signature,
            expected_signature=row.expected_signature,
            sampled_validation_return=row.sampled_validation_return,
            deterministic_training_reward=row.deterministic_training_reward,
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


def verdict_rows(rows: Sequence[PolicyGradientSeedRow]) -> List[PolicyGradientSeedVerdict]:
    verdicts = []
    seeds = tuple(sorted({row.seed for row in rows}))
    for scenario in sorted({row.scenario for row in rows}):
        scenario_rows = [row for row in rows if row.scenario == scenario]
        expected = stress.EXPECTED_SIGNATURES[scenario]
        architecture_count = len({row.architecture for row in scenario_rows})
        counts = {
            seed: sum(
                1
                for row in scenario_rows
                if row.seed == seed and row.matches_expected_signature
            )
            for seed in seeds
        }
        strict_seed_count = sum(1 for count in counts.values() if count == architecture_count)
        total_converged = sum(counts.values())
        total_architectures = architecture_count * len(seeds)
        strict_all = strict_seed_count == len(seeds)
        result = classify_seed_result(scenario, strict_seed_count, len(seeds), total_converged, total_architectures)
        verdicts.append(
            PolicyGradientSeedVerdict(
                scenario=scenario,
                expected_signature=expected,
                seed_count=len(seeds),
                architecture_count=architecture_count,
                strict_seed_count=strict_seed_count,
                total_converged_architectures=total_converged,
                total_architecture_count=total_architectures,
                strict_all_seeds=strict_all,
                convergence_by_seed=";".join(f"{seed}:{counts[seed]}/{architecture_count}" for seed in seeds),
                sum_rnn_signature_by_seed=signature_series(scenario_rows, seeds, "sum_rnn"),
                scalar_signature_by_seed=signature_series(scenario_rows, seeds, "scalar_rnn"),
                two_unit_signature_by_seed=signature_series(scenario_rows, seeds, "two_unit_rnn"),
                mean_recurrent_reward=statistics.fmean(row.recurrent_training_reward for row in scenario_rows),
                mean_local_reward=statistics.fmean(row.local_training_reward for row in scenario_rows),
                policy_gradient_seed_result=result,
                supports_architecture_policy_gradient_seed_sweep=supports_seed_result(
                    scenario,
                    strict_seed_count,
                    len(seeds),
                    total_converged,
                    total_architectures,
                    result,
                ),
            )
        )
    return verdicts


def signature_series(
    rows: Sequence[PolicyGradientSeedRow],
    seeds: Sequence[int],
    architecture: str,
) -> str:
    return ";".join(
        f"{seed}:{next(row.dependency_signature for row in rows if row.seed == seed and row.architecture == architecture)}"
        for seed in seeds
    )


def classify_seed_result(
    scenario: str,
    strict_seed_count: int,
    seed_count: int,
    total_converged: int,
    total_architectures: int,
) -> str:
    if scenario in stress.SHARED_REGIMES:
        if strict_seed_count == seed_count:
            return "policy_gradient_seed_stable_shared_boundary"
        if strict_seed_count > 0 and total_converged > total_architectures / 2:
            return "policy_gradient_seed_partial_shared_robustness"
        return "policy_gradient_seed_unstable_shared_boundary"
    if scenario == "independent_hidden":
        if strict_seed_count == seed_count:
            return "policy_gradient_seed_stable_rejects_shared_recurrence"
        return "policy_gradient_seed_control_false_positive"
    if scenario == "irrelevant_control":
        if strict_seed_count == seed_count:
            return "policy_gradient_seed_stable_rejects_hidden_state"
        return "policy_gradient_seed_control_false_positive"
    raise ValueError(f"unknown scenario: {scenario}")


def supports_seed_result(
    scenario: str,
    strict_seed_count: int,
    seed_count: int,
    total_converged: int,
    total_architectures: int,
    result: str,
) -> bool:
    if scenario in stress.SHARED_REGIMES:
        return (
            strict_seed_count > 0
            and total_converged > total_architectures / 2
            and result
            in {
                "policy_gradient_seed_stable_shared_boundary",
                "policy_gradient_seed_partial_shared_robustness",
            }
        )
    if scenario == "independent_hidden":
        return result == "policy_gradient_seed_stable_rejects_shared_recurrence"
    if scenario == "irrelevant_control":
        return result == "policy_gradient_seed_stable_rejects_hidden_state"
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: PolicyGradientSeedConfig,
) -> Tuple[List[PolicyGradientSeedRow], List[PolicyGradientSeedVerdict]]:
    rows = [row for seed in cfg.seeds for row in run_seed(seed, cfg)]
    return rows, verdict_rows(rows)


def write_csv(path: Path, rows: Iterable[object]) -> None:
    mixed.write_csv(path, rows)


def print_table(verdicts: Sequence[PolicyGradientSeedVerdict]) -> None:
    headers = [
        "scenario",
        "convergence_by_seed",
        "strict_seed_count",
        "seed_count",
        "policy_gradient_seed_result",
        "supports_architecture_policy_gradient_seed_sweep",
    ]
    table_rows = []
    for verdict in verdicts:
        table_rows.append(
            [
                verdict.scenario,
                verdict.convergence_by_seed,
                str(verdict.strict_seed_count),
                str(verdict.seed_count),
                verdict.policy_gradient_seed_result,
                str(verdict.supports_architecture_policy_gradient_seed_sweep),
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


def parse_args() -> PolicyGradientSeedConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", type=str, default=",".join(str(seed) for seed in DEFAULT_SEEDS))
    parser.add_argument("--episodes", type=int, default=200)
    parser.add_argument("--training-episodes", type=int, default=400)
    parser.add_argument("--validation-episodes", type=int, default=240)
    parser.add_argument("--batch-episodes", type=int, default=128)
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
    seeds = parse_seeds(args.seeds)
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
    return PolicyGradientSeedConfig(
        seeds=seeds,
        episodes=args.episodes,
        training_episodes=args.training_episodes,
        validation_episodes=args.validation_episodes,
        batch_episodes=args.batch_episodes,
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
    summary_path = ARTIFACT_DIR / "architecture_policy_gradient_seed_sweep_summary.csv"
    verdict_path = ARTIFACT_DIR / "architecture_policy_gradient_seed_sweep_verdict.csv"
    results_path = ARTIFACT_DIR / "architecture_policy_gradient_seed_sweep_results.json"
    write_csv(summary_path, rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "summary": [asdict(row) for row in rows],
                "verdict": [asdict(row) for row in verdicts],
                "note": (
                    "Seed sweep for the stochastic policy-gradient learner. "
                    "Reports strict convergence by seed instead of averaging "
                    "away failed architecture-boundary cells."
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
    return 0 if all(verdict.supports_architecture_policy_gradient_seed_sweep for verdict in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
