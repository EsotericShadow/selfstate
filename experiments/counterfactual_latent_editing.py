#!/usr/bin/env python3
"""Counterfactual latent editing precursor.

Latent ablation shows that a learned latent is used. This experiment asks
whether editing that latent changes action-centered counterfactuals in the
expected direction.

It trains the model-based planners, then forces their probe-derived latent to
all-good or all-bad evidence before held-out planning. A valid counterfactual
edit should increase risky action under good evidence and suppress risky action
under bad evidence in shared-state regimes, while preserving the agent/world
boundary distinction.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

from cross_environment_attractor import (
    ENVIRONMENTS,
    SCENARIOS,
    CrossEnvConfig,
    EnvironmentFamily,
    ScenarioSpec,
    boundary_signature,
    sample_state,
)
from evolved_recurrent_policy import (
    majority_control_success,
    probe_reward,
    sample_std,
    threshold_accuracy,
)
from model_based_planning import (
    PLANNER_TYPES,
    ModelBasedConfig,
    RewardModelPlanner,
    as_cross_cfg,
    make_traces,
    planned_choice,
)


ARTIFACT_DIR = Path("artifacts")
EPS = 1e-12
EDIT_SWING_THRESHOLD = 0.90


@dataclass(frozen=True)
class EditConfig:
    episodes: int = 500
    training_episodes: int = 500
    seed: int = 20260601
    calibration_contexts: int = 2
    calibration_cost: float = 1.0
    local_probe_cost: float = 1.0
    probe_success_reward: float = 1.0
    probe_failure_reward: float = -1.0
    validation_fraction: float = 0.35
    recurrent_candidates: int = 200


@dataclass
class EditResult:
    environment: str
    surface: str
    scenario: str
    planner: str
    family: str
    boundary_signature: str
    counterfactual_signature: str
    true_risky_rate: float
    forced_good_risky_rate: float
    forced_bad_risky_rate: float
    edit_swing: float
    latent_good_value: float
    latent_bad_value: float
    latent_mean: float
    latent_std: float
    latent_self_accuracy: float
    latent_world_accuracy: float
    latent_control_accuracy: float
    selected_model: str


@dataclass
class EnvironmentVerdict:
    environment: str
    surface: str
    scenario: str
    expected_counterfactual_signature: str
    boundary_signature: str
    converged_planners: int
    planner_count: int
    mean_true_risky_rate: float
    mean_forced_good_risky_rate: float
    mean_forced_bad_risky_rate: float
    mean_edit_swing: float
    planner_signatures: str
    supports_counterfactual_latent_editing: bool


@dataclass
class ScenarioVerdict:
    scenario: str
    expected_counterfactual_signature: str
    supporting_environments: int
    environment_count: int
    mean_true_risky_rate: float
    mean_forced_good_risky_rate: float
    mean_forced_bad_risky_rate: float
    mean_edit_swing: float
    environment_signatures: str
    supports_counterfactual_latent_editing: bool


def as_model_cfg(cfg: EditConfig) -> ModelBasedConfig:
    return ModelBasedConfig(
        episodes=cfg.episodes,
        training_episodes=cfg.training_episodes,
        seed=cfg.seed,
        calibration_contexts=cfg.calibration_contexts,
        calibration_cost=cfg.calibration_cost,
        local_probe_cost=cfg.local_probe_cost,
        probe_success_reward=cfg.probe_success_reward,
        probe_failure_reward=cfg.probe_failure_reward,
        validation_fraction=cfg.validation_fraction,
        recurrent_candidates=cfg.recurrent_candidates,
    )


def as_edit_cross_cfg(cfg: EditConfig) -> CrossEnvConfig:
    return CrossEnvConfig(
        episodes=cfg.episodes,
        training_episodes=cfg.training_episodes,
        seed=cfg.seed,
        calibration_contexts=cfg.calibration_contexts,
        calibration_cost=cfg.calibration_cost,
        local_probe_cost=cfg.local_probe_cost,
    )


def evaluate_editing(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    planner: RewardModelPlanner,
    cfg: EditConfig,
    signature: str,
) -> EditResult:
    cross_cfg = as_edit_cross_cfg(cfg)
    true_risky = 0
    forced_good_risky = 0
    forced_bad_risky = 0
    action_count = 0
    latents = []
    self_labels = []
    world_labels = []
    control_labels = []
    good_rewards = tuple(cfg.probe_success_reward for _ in range(cfg.calibration_contexts))
    bad_rewards = tuple(cfg.probe_failure_reward for _ in range(cfg.calibration_contexts))

    for episode in range(cfg.episodes):
        state = sample_state(environment, scenario, episode + cfg.training_episodes * 3, cross_cfg)
        probe_rewards = tuple(
            probe_reward(state.local_success[profile.name], cfg)
            for profile in environment.contexts[: cfg.calibration_contexts]
        )
        latents.append(planner.latent_value(probe_rewards))
        self_labels.append(state.self_signal)
        world_labels.append(state.world_signal)
        control_labels.append(majority_control_success(state.local_success, environment, cfg))

        for profile in environment.contexts[cfg.calibration_contexts :]:
            true_choice = planned_choice(profile, planner.predict_success(probe_rewards, profile))
            good_choice = planned_choice(profile, planner.predict_success(good_rewards, profile))
            bad_choice = planned_choice(profile, planner.predict_success(bad_rewards, profile))
            true_risky += int(true_choice == "risky")
            forced_good_risky += int(good_choice == "risky")
            forced_bad_risky += int(bad_choice == "risky")
            action_count += 1

    self_accuracy = threshold_accuracy(latents, self_labels)
    world_accuracy = threshold_accuracy(latents, world_labels)
    control_accuracy = threshold_accuracy(latents, control_labels)
    true_rate = true_risky / action_count
    good_rate = forced_good_risky / action_count
    bad_rate = forced_bad_risky / action_count
    edit_swing = good_rate - bad_rate
    counterfactual_signature = classify_counterfactual_signature(
        scenario=scenario,
        boundary=signature,
        edit_swing=edit_swing,
        self_accuracy=self_accuracy,
        world_accuracy=world_accuracy,
        latent_std=sample_std(latents),
        uses_probe=planner.uses_probe_history(good_rewards) or planner.uses_probe_history(bad_rewards),
    )
    return EditResult(
        environment=environment.name,
        surface=environment.surface,
        scenario=scenario.name,
        planner=planner.name,
        family=planner.family,
        boundary_signature=signature,
        counterfactual_signature=counterfactual_signature,
        true_risky_rate=true_rate,
        forced_good_risky_rate=good_rate,
        forced_bad_risky_rate=bad_rate,
        edit_swing=edit_swing,
        latent_good_value=planner.latent_value(good_rewards),
        latent_bad_value=planner.latent_value(bad_rewards),
        latent_mean=statistics.fmean(latents),
        latent_std=sample_std(latents),
        latent_self_accuracy=self_accuracy,
        latent_world_accuracy=world_accuracy,
        latent_control_accuracy=control_accuracy,
        selected_model=planner.selected_model,
    )


def classify_counterfactual_signature(
    scenario: ScenarioSpec,
    boundary: str,
    edit_swing: float,
    self_accuracy: float,
    world_accuracy: float,
    latent_std: float,
    uses_probe: bool,
) -> str:
    if scenario.mode == "irrelevant_control" and abs(edit_swing) <= EPS and not uses_probe:
        return "no_hidden_needed"
    if edit_swing >= EDIT_SWING_THRESHOLD:
        if boundary == "agent_bounded_cross_env" and self_accuracy >= 0.80 and world_accuracy < 0.70:
            return "agent_counterfactual_edit"
        if boundary == "external_cross_env" and world_accuracy >= 0.80 and self_accuracy < 0.70:
            return "external_counterfactual_edit"
        return "counterfactual_edit_wrong_boundary"
    if boundary == "no_shared_agent_boundary" and latent_std < 0.05:
        return "no_shared_counterfactual"
    if scenario.mode == "independent_hidden" and abs(edit_swing) < EDIT_SWING_THRESHOLD:
        return "no_shared_counterfactual"
    return "counterfactual_edit_missing"


def expected_counterfactual_signature(scenario: ScenarioSpec) -> str:
    if scenario.mode == "agent_shared":
        return "agent_counterfactual_edit"
    if scenario.mode == "world_shared":
        return "external_counterfactual_edit"
    if scenario.mode == "independent_hidden":
        return "no_shared_counterfactual"
    if scenario.mode == "irrelevant_control":
        return "no_hidden_needed"
    raise ValueError(f"unknown scenario mode: {scenario.mode}")


def build_environment_verdicts(results: Sequence[EditResult]) -> List[EnvironmentVerdict]:
    verdicts = []
    for environment in ENVIRONMENTS:
        for scenario in SCENARIOS:
            rows = [
                row
                for row in results
                if row.environment == environment.name and row.scenario == scenario.name
            ]
            expected = expected_counterfactual_signature(scenario)
            converged = sum(1 for row in rows if row.counterfactual_signature == expected)
            signatures = ";".join(f"{row.planner}:{row.counterfactual_signature}" for row in rows)
            mean_swing = statistics.fmean(row.edit_swing for row in rows)
            supports = supports_environment(
                scenario=scenario,
                expected=expected,
                converged=converged,
                planner_count=len(rows),
                mean_swing=mean_swing,
            )
            verdicts.append(
                EnvironmentVerdict(
                    environment=environment.name,
                    surface=environment.surface,
                    scenario=scenario.name,
                    expected_counterfactual_signature=expected,
                    boundary_signature=rows[0].boundary_signature,
                    converged_planners=converged,
                    planner_count=len(rows),
                    mean_true_risky_rate=statistics.fmean(row.true_risky_rate for row in rows),
                    mean_forced_good_risky_rate=statistics.fmean(row.forced_good_risky_rate for row in rows),
                    mean_forced_bad_risky_rate=statistics.fmean(row.forced_bad_risky_rate for row in rows),
                    mean_edit_swing=mean_swing,
                    planner_signatures=signatures,
                    supports_counterfactual_latent_editing=supports,
                )
            )
    return verdicts


def supports_environment(
    scenario: ScenarioSpec,
    expected: str,
    converged: int,
    planner_count: int,
    mean_swing: float,
) -> bool:
    majority = converged >= max(2, math.ceil(planner_count * 0.6))
    if not majority:
        return False
    if expected in {"agent_counterfactual_edit", "external_counterfactual_edit"}:
        return mean_swing >= EDIT_SWING_THRESHOLD
    if scenario.mode in {"independent_hidden", "irrelevant_control"}:
        return abs(mean_swing) < EDIT_SWING_THRESHOLD
    return False


def build_scenario_verdicts(environment_verdicts: Sequence[EnvironmentVerdict]) -> List[ScenarioVerdict]:
    verdicts = []
    for scenario in SCENARIOS:
        rows = [row for row in environment_verdicts if row.scenario == scenario.name]
        supporting = sum(1 for row in rows if row.supports_counterfactual_latent_editing)
        signatures = ";".join(
            f"{row.environment}:{row.converged_planners}/{row.planner_count}:{row.expected_counterfactual_signature}"
            for row in rows
        )
        verdicts.append(
            ScenarioVerdict(
                scenario=scenario.name,
                expected_counterfactual_signature=expected_counterfactual_signature(scenario),
                supporting_environments=supporting,
                environment_count=len(rows),
                mean_true_risky_rate=statistics.fmean(row.mean_true_risky_rate for row in rows),
                mean_forced_good_risky_rate=statistics.fmean(row.mean_forced_good_risky_rate for row in rows),
                mean_forced_bad_risky_rate=statistics.fmean(row.mean_forced_bad_risky_rate for row in rows),
                mean_edit_swing=statistics.fmean(row.mean_edit_swing for row in rows),
                environment_signatures=signatures,
                supports_counterfactual_latent_editing=supporting == len(rows),
            )
        )
    return verdicts


def run_experiment(
    cfg: EditConfig,
) -> Tuple[List[EditResult], List[EnvironmentVerdict], List[ScenarioVerdict], Dict[str, object]]:
    model_cfg = as_model_cfg(cfg)
    results: List[EditResult] = []
    diagnostics: Dict[str, object] = {}
    cross_cfg = as_cross_cfg(model_cfg)
    for environment in ENVIRONMENTS:
        for scenario in SCENARIOS:
            traces = make_traces(environment, scenario, model_cfg)
            signature, agent_effect, world_effect = boundary_signature(environment, scenario, cross_cfg)
            diagnostics[f"{environment.name}:{scenario.name}"] = {
                "boundary_signature": signature,
                "agent_intervention_effect": agent_effect,
                "world_intervention_effect": world_effect,
            }
            for planner_type in PLANNER_TYPES:
                planner = planner_type()
                planner.fit(traces, environment, model_cfg)
                results.append(evaluate_editing(environment, scenario, planner, cfg, signature))
    environment_verdicts = build_environment_verdicts(results)
    scenario_verdicts = build_scenario_verdicts(environment_verdicts)
    return results, environment_verdicts, scenario_verdicts, diagnostics


def write_csv(path: Path, rows: Iterable[object]) -> None:
    rows = list(rows)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def print_table(verdicts: Sequence[ScenarioVerdict]) -> None:
    headers = [
        "scenario",
        "expected_counterfactual_signature",
        "supporting_environments",
        "mean_forced_good_risky_rate",
        "mean_forced_bad_risky_rate",
        "mean_edit_swing",
        "supports_counterfactual_latent_editing",
    ]
    rows = []
    for verdict in verdicts:
        rows.append(
            [
                verdict.scenario,
                verdict.expected_counterfactual_signature,
                f"{verdict.supporting_environments}/{verdict.environment_count}",
                f"{verdict.mean_forced_good_risky_rate:.3f}",
                f"{verdict.mean_forced_bad_risky_rate:.3f}",
                f"{verdict.mean_edit_swing:.3f}",
                str(verdict.supports_counterfactual_latent_editing),
            ]
        )
    widths = [
        max(len(header), *(len(row[index]) for row in rows))
        for index, header in enumerate(headers)
    ]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> EditConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=500)
    parser.add_argument("--training-episodes", type=int, default=500)
    parser.add_argument("--seed", type=int, default=20260601)
    parser.add_argument("--calibration-contexts", type=int, default=2)
    parser.add_argument("--calibration-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    parser.add_argument("--probe-success-reward", type=float, default=1.0)
    parser.add_argument("--probe-failure-reward", type=float, default=-1.0)
    parser.add_argument("--validation-fraction", type=float, default=0.35)
    parser.add_argument("--recurrent-candidates", type=int, default=200)
    args = parser.parse_args()
    if args.calibration_contexts < 1:
        raise SystemExit("--calibration-contexts must be at least 1")
    if any(args.calibration_contexts >= len(environment.contexts) for environment in ENVIRONMENTS):
        raise SystemExit("--calibration-contexts must leave held-out contexts")
    if not 0.05 <= args.validation_fraction <= 0.9:
        raise SystemExit("--validation-fraction must be between 0.05 and 0.9")
    if args.recurrent_candidates < 0:
        raise SystemExit("--recurrent-candidates must be non-negative")
    return EditConfig(
        episodes=args.episodes,
        training_episodes=args.training_episodes,
        seed=args.seed,
        calibration_contexts=args.calibration_contexts,
        calibration_cost=args.calibration_cost,
        local_probe_cost=args.local_probe_cost,
        probe_success_reward=args.probe_success_reward,
        probe_failure_reward=args.probe_failure_reward,
        validation_fraction=args.validation_fraction,
        recurrent_candidates=args.recurrent_candidates,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    results, environment_verdicts, scenario_verdicts, diagnostics = run_experiment(cfg)

    summary_path = ARTIFACT_DIR / "counterfactual_latent_editing_summary.csv"
    environment_verdict_path = ARTIFACT_DIR / "counterfactual_latent_editing_environment_verdict.csv"
    scenario_verdict_path = ARTIFACT_DIR / "counterfactual_latent_editing_scenario_verdict.csv"
    results_path = ARTIFACT_DIR / "counterfactual_latent_editing_results.json"
    write_csv(summary_path, results)
    write_csv(environment_verdict_path, environment_verdicts)
    write_csv(scenario_verdict_path, scenario_verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "diagnostics": diagnostics,
                "editing_summary": [asdict(row) for row in results],
                "environment_verdict": [asdict(row) for row in environment_verdicts],
                "scenario_verdict": [asdict(row) for row in scenario_verdicts],
            },
            handle,
            indent=2,
        )
        handle.write("\n")

    print(f"wrote {summary_path}")
    print(f"wrote {environment_verdict_path}")
    print(f"wrote {scenario_verdict_path}")
    print(f"wrote {results_path}")
    print_table(scenario_verdicts)
    return 0 if all(row.supports_counterfactual_latent_editing for row in scenario_verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
