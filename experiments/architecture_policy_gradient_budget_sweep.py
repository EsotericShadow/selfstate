#!/usr/bin/env python3
"""Architecture policy-gradient budget sweep.

Report 57 showed that the stochastic policy-gradient learner is recoverable but
not seed-stable at the standard budget. This pressure test asks whether that
failure is merely an optimization-budget artifact.

The sweep repeats the same learner across independent seeds and compares a
standard budget against one or more larger budgets. It keeps the same
end-to-end boundary classifier and reports whether larger budgets repair strict
seed stability, preserve only partial robustness, or introduce control false
positives.
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
class BudgetSetting:
    label: str
    epochs: int
    restarts: int
    batch_episodes: int


DEFAULT_BUDGETS = (
    BudgetSetting("standard", 32, 5, 128),
    BudgetSetting("larger", 64, 8, 192),
)


@dataclass(frozen=True)
class PolicyGradientBudgetConfig:
    seeds: Tuple[int, ...] = DEFAULT_SEEDS
    budgets: Tuple[BudgetSetting, ...] = DEFAULT_BUDGETS
    episodes: int = 200
    training_episodes: int = 400
    validation_episodes: int = 240
    horizon: int = 8
    evidence_samples: int = 9
    cue_accuracy: float = 0.85
    shared_cue_cost: float = 1.0
    local_probe_cost: float = 1.0
    temperature: float = 1.8
    learning_rate: float = 0.12
    lr_decay: float = 0.96
    initial_std: float = 0.8
    finite_diff_epsilon: float = 0.02
    max_grad_norm: float = 4.0


@dataclass(frozen=True)
class PolicyGradientBudgetRow:
    budget_label: str
    budget_epochs: int
    budget_restarts: int
    budget_batch_episodes: int
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
class PolicyGradientBudgetVerdict:
    scenario: str
    expected_signature: str
    seed_count: int
    architecture_count: int
    budget_count: int
    first_budget: str
    last_budget: str
    first_strict_seed_count: int
    last_strict_seed_count: int
    max_strict_seed_count: int
    first_total_converged_architectures: int
    last_total_converged_architectures: int
    max_total_converged_architectures: int
    total_architecture_count_per_budget: int
    strict_at_any_budget: bool
    strict_at_last_budget: bool
    convergence_by_budget: str
    sum_rnn_signature_by_budget: str
    scalar_signature_by_budget: str
    two_unit_signature_by_budget: str
    first_mean_recurrent_reward: float
    last_mean_recurrent_reward: float
    first_mean_local_reward: float
    last_mean_local_reward: float
    policy_gradient_budget_result: str
    strengthens_seed_stability_claim: bool
    valid_architecture_policy_gradient_budget_sweep: bool


def parse_seeds(raw: str) -> Tuple[int, ...]:
    seeds = tuple(int(part.strip()) for part in raw.split(",") if part.strip())
    if not seeds:
        raise SystemExit("--seeds must contain at least one integer")
    if len(set(seeds)) != len(seeds):
        raise SystemExit("--seeds must not contain duplicates")
    return seeds


def parse_budgets(raw: str) -> Tuple[BudgetSetting, ...]:
    budgets = []
    for spec in (part.strip() for part in raw.split(";") if part.strip()):
        pieces = spec.split(":")
        if len(pieces) != 4:
            raise SystemExit(
                "--budgets entries must use label:epochs:restarts:batch_episodes"
            )
        label, epochs, restarts, batch_episodes = pieces
        label = label.strip()
        if not label:
            raise SystemExit("budget labels must be nonempty")
        if any(character in label for character in ":;,|"):
            raise SystemExit("budget labels must not contain ':', ';', ',', or '|'")
        budgets.append(
            BudgetSetting(
                label=label,
                epochs=int(epochs),
                restarts=int(restarts),
                batch_episodes=int(batch_episodes),
            )
        )
    if not budgets:
        raise SystemExit("--budgets must contain at least one budget setting")
    if len({budget.label for budget in budgets}) != len(budgets):
        raise SystemExit("budget labels must be unique")
    for budget in budgets:
        if budget.epochs < 1:
            raise SystemExit("budget epochs must be positive")
        if budget.restarts < 1:
            raise SystemExit("budget restarts must be positive")
        if budget.batch_episodes < 1:
            raise SystemExit("budget batch_episodes must be positive")
    return tuple(budgets)


def budget_spec(budgets: Sequence[BudgetSetting]) -> str:
    return ";".join(
        f"{budget.label}:{budget.epochs}:{budget.restarts}:{budget.batch_episodes}"
        for budget in budgets
    )


def pg_cfg_for_budget(
    seed: int,
    budget: BudgetSetting,
    base: PolicyGradientBudgetConfig,
) -> pg.PolicyGradientConfig:
    return pg.PolicyGradientConfig(
        episodes=base.episodes,
        training_episodes=base.training_episodes,
        validation_episodes=base.validation_episodes,
        batch_episodes=budget.batch_episodes,
        seed=seed,
        horizon=base.horizon,
        evidence_samples=base.evidence_samples,
        cue_accuracy=base.cue_accuracy,
        shared_cue_cost=base.shared_cue_cost,
        local_probe_cost=base.local_probe_cost,
        epochs=budget.epochs,
        restarts=budget.restarts,
        temperature=base.temperature,
        learning_rate=base.learning_rate,
        lr_decay=base.lr_decay,
        initial_std=base.initial_std,
        finite_diff_epsilon=base.finite_diff_epsilon,
        max_grad_norm=base.max_grad_norm,
    )


def run_budget_seed(
    budget: BudgetSetting,
    seed: int,
    cfg: PolicyGradientBudgetConfig,
) -> List[PolicyGradientBudgetRow]:
    rows, _verdicts = pg.run_experiment(pg_cfg_for_budget(seed, budget, cfg))
    return [
        PolicyGradientBudgetRow(
            budget_label=budget.label,
            budget_epochs=budget.epochs,
            budget_restarts=budget.restarts,
            budget_batch_episodes=budget.batch_episodes,
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


def verdict_rows(
    rows: Sequence[PolicyGradientBudgetRow],
    budgets: Sequence[BudgetSetting],
) -> List[PolicyGradientBudgetVerdict]:
    verdicts = []
    labels = tuple(budget.label for budget in budgets)
    seeds = tuple(sorted({row.seed for row in rows}))
    for scenario in sorted({row.scenario for row in rows}):
        scenario_rows = [row for row in rows if row.scenario == scenario]
        expected = stress.EXPECTED_SIGNATURES[scenario]
        architecture_count = len({row.architecture for row in scenario_rows})
        counts = {
            label: {
                seed: sum(
                    1
                    for row in scenario_rows
                    if row.budget_label == label
                    and row.seed == seed
                    and row.matches_expected_signature
                )
                for seed in seeds
            }
            for label in labels
        }
        strict_seed_counts = {
            label: sum(1 for count in seed_counts.values() if count == architecture_count)
            for label, seed_counts in counts.items()
        }
        total_converged = {
            label: sum(seed_counts.values())
            for label, seed_counts in counts.items()
        }
        total_architectures = len(seeds) * architecture_count
        first_label = labels[0]
        last_label = labels[-1]
        strict_any = any(value == len(seeds) for value in strict_seed_counts.values())
        strict_last = strict_seed_counts[last_label] == len(seeds)
        result = classify_budget_result(
            scenario,
            strict_seed_counts[first_label],
            strict_seed_counts[last_label],
            max(strict_seed_counts.values()),
            total_converged[first_label],
            total_converged[last_label],
            max(total_converged.values()),
            len(seeds),
            total_architectures,
            strict_any,
        )
        verdicts.append(
            PolicyGradientBudgetVerdict(
                scenario=scenario,
                expected_signature=expected,
                seed_count=len(seeds),
                architecture_count=architecture_count,
                budget_count=len(labels),
                first_budget=first_label,
                last_budget=last_label,
                first_strict_seed_count=strict_seed_counts[first_label],
                last_strict_seed_count=strict_seed_counts[last_label],
                max_strict_seed_count=max(strict_seed_counts.values()),
                first_total_converged_architectures=total_converged[first_label],
                last_total_converged_architectures=total_converged[last_label],
                max_total_converged_architectures=max(total_converged.values()),
                total_architecture_count_per_budget=total_architectures,
                strict_at_any_budget=strict_any,
                strict_at_last_budget=strict_last,
                convergence_by_budget=convergence_series(counts, labels, seeds, architecture_count),
                sum_rnn_signature_by_budget=signature_series(scenario_rows, labels, seeds, "sum_rnn"),
                scalar_signature_by_budget=signature_series(scenario_rows, labels, seeds, "scalar_rnn"),
                two_unit_signature_by_budget=signature_series(scenario_rows, labels, seeds, "two_unit_rnn"),
                first_mean_recurrent_reward=mean_reward(scenario_rows, first_label, "recurrent"),
                last_mean_recurrent_reward=mean_reward(scenario_rows, last_label, "recurrent"),
                first_mean_local_reward=mean_reward(scenario_rows, first_label, "local"),
                last_mean_local_reward=mean_reward(scenario_rows, last_label, "local"),
                policy_gradient_budget_result=result,
                strengthens_seed_stability_claim=strengthens_seed_stability(
                    scenario,
                    result,
                    strict_any,
                ),
                valid_architecture_policy_gradient_budget_sweep=True,
            )
        )
    return verdicts


def convergence_series(
    counts: dict[str, dict[int, int]],
    labels: Sequence[str],
    seeds: Sequence[int],
    architecture_count: int,
) -> str:
    return "|".join(
        f"{label}="
        + ";".join(f"{seed}:{counts[label][seed]}/{architecture_count}" for seed in seeds)
        for label in labels
    )


def signature_series(
    rows: Sequence[PolicyGradientBudgetRow],
    labels: Sequence[str],
    seeds: Sequence[int],
    architecture: str,
) -> str:
    return "|".join(
        f"{label}="
        + ";".join(
            f"{seed}:{next(row.dependency_signature for row in rows if row.budget_label == label and row.seed == seed and row.architecture == architecture)}"
            for seed in seeds
        )
        for label in labels
    )


def mean_reward(
    rows: Sequence[PolicyGradientBudgetRow],
    label: str,
    reward_kind: str,
) -> float:
    if reward_kind == "recurrent":
        return statistics.fmean(
            row.recurrent_training_reward for row in rows if row.budget_label == label
        )
    if reward_kind == "local":
        return statistics.fmean(
            row.local_training_reward for row in rows if row.budget_label == label
        )
    raise ValueError(f"unknown reward kind: {reward_kind}")


def classify_budget_result(
    scenario: str,
    first_strict_seed_count: int,
    last_strict_seed_count: int,
    max_strict_seed_count: int,
    first_total_converged: int,
    last_total_converged: int,
    max_total_converged: int,
    seed_count: int,
    total_architectures: int,
    strict_any: bool,
) -> str:
    if scenario in stress.SHARED_REGIMES:
        if strict_any:
            return "policy_gradient_budget_repairs_seed_instability"
        if (
            last_strict_seed_count > first_strict_seed_count
            or last_total_converged > first_total_converged
            or max_strict_seed_count > first_strict_seed_count
            or max_total_converged > first_total_converged
        ):
            return "policy_gradient_budget_improves_but_not_seed_stable"
        if last_total_converged < first_total_converged:
            return "policy_gradient_budget_reduces_shared_recovery"
        if max_total_converged > total_architectures / 2:
            return "policy_gradient_budget_preserves_partial_instability"
        return "policy_gradient_budget_uninformative_shared_boundary"
    if scenario == "independent_hidden":
        if first_strict_seed_count == seed_count and last_strict_seed_count == seed_count:
            return "policy_gradient_budget_stable_rejects_shared_recurrence"
        return "policy_gradient_budget_control_false_positive"
    if scenario == "irrelevant_control":
        if first_strict_seed_count == seed_count and last_strict_seed_count == seed_count:
            return "policy_gradient_budget_stable_rejects_hidden_state"
        return "policy_gradient_budget_control_false_positive"
    raise ValueError(f"unknown scenario: {scenario}")


def strengthens_seed_stability(
    scenario: str,
    result: str,
    strict_any: bool,
) -> bool:
    if scenario in stress.SHARED_REGIMES:
        return strict_any and result == "policy_gradient_budget_repairs_seed_instability"
    if scenario == "independent_hidden":
        return result == "policy_gradient_budget_stable_rejects_shared_recurrence"
    if scenario == "irrelevant_control":
        return result == "policy_gradient_budget_stable_rejects_hidden_state"
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: PolicyGradientBudgetConfig,
) -> Tuple[List[PolicyGradientBudgetRow], List[PolicyGradientBudgetVerdict]]:
    rows = [
        row
        for budget in cfg.budgets
        for seed in cfg.seeds
        for row in run_budget_seed(budget, seed, cfg)
    ]
    return rows, verdict_rows(rows, cfg.budgets)


def write_csv(path: Path, rows: Iterable[object]) -> None:
    mixed.write_csv(path, rows)


def print_table(verdicts: Sequence[PolicyGradientBudgetVerdict]) -> None:
    headers = [
        "scenario",
        "convergence_by_budget",
        "first_strict_seed_count",
        "last_strict_seed_count",
        "max_strict_seed_count",
        "policy_gradient_budget_result",
        "strengthens_seed_stability_claim",
    ]
    table_rows = []
    for verdict in verdicts:
        table_rows.append(
            [
                verdict.scenario,
                verdict.convergence_by_budget,
                str(verdict.first_strict_seed_count),
                str(verdict.last_strict_seed_count),
                str(verdict.max_strict_seed_count),
                verdict.policy_gradient_budget_result,
                str(verdict.strengthens_seed_stability_claim),
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


def parse_args() -> PolicyGradientBudgetConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", type=str, default=",".join(str(seed) for seed in DEFAULT_SEEDS))
    parser.add_argument("--budgets", type=str, default=budget_spec(DEFAULT_BUDGETS))
    parser.add_argument("--episodes", type=int, default=200)
    parser.add_argument("--training-episodes", type=int, default=400)
    parser.add_argument("--validation-episodes", type=int, default=240)
    parser.add_argument("--horizon", type=int, default=8)
    parser.add_argument("--evidence-samples", type=int, default=9)
    parser.add_argument("--cue-accuracy", type=float, default=0.85)
    parser.add_argument("--shared-cue-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    parser.add_argument("--temperature", type=float, default=1.8)
    parser.add_argument("--learning-rate", type=float, default=0.12)
    parser.add_argument("--lr-decay", type=float, default=0.96)
    parser.add_argument("--initial-std", type=float, default=0.8)
    parser.add_argument("--finite-diff-epsilon", type=float, default=0.02)
    parser.add_argument("--max-grad-norm", type=float, default=4.0)
    args = parser.parse_args()
    seeds = parse_seeds(args.seeds)
    budgets = parse_budgets(args.budgets)
    if args.episodes < 1:
        raise SystemExit("--episodes must be at least 1")
    if args.training_episodes < 1:
        raise SystemExit("--training-episodes must be at least 1")
    if args.validation_episodes < 1:
        raise SystemExit("--validation-episodes must be at least 1")
    if args.horizon < 1:
        raise SystemExit("--horizon must be at least 1")
    if args.evidence_samples < 1:
        raise SystemExit("--evidence-samples must be at least 1")
    if not 0.5 <= args.cue_accuracy <= 1.0:
        raise SystemExit("--cue-accuracy must be in [0.5, 1.0]")
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
    return PolicyGradientBudgetConfig(
        seeds=seeds,
        budgets=budgets,
        episodes=args.episodes,
        training_episodes=args.training_episodes,
        validation_episodes=args.validation_episodes,
        horizon=args.horizon,
        evidence_samples=args.evidence_samples,
        cue_accuracy=args.cue_accuracy,
        shared_cue_cost=args.shared_cue_cost,
        local_probe_cost=args.local_probe_cost,
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
    summary_path = ARTIFACT_DIR / "architecture_policy_gradient_budget_sweep_summary.csv"
    verdict_path = ARTIFACT_DIR / "architecture_policy_gradient_budget_sweep_verdict.csv"
    results_path = ARTIFACT_DIR / "architecture_policy_gradient_budget_sweep_results.json"
    write_csv(summary_path, rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "summary": [asdict(row) for row in rows],
                "verdict": [asdict(row) for row in verdicts],
                "note": (
                    "Budget-pressure audit for the stochastic policy-gradient learner. "
                    "It tests whether larger budgets repair seed instability without "
                    "creating control false positives."
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
    return 0 if all(verdict.valid_architecture_policy_gradient_budget_sweep for verdict in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
