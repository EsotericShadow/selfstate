#!/usr/bin/env python3
"""Latent causal ablation precursor.

The current attractor stack shows that several learners converge on the same
latent signatures. This experiment tests whether the learned latent is causally
used, not merely decodable.

It trains the model-based planners, evaluates them intact, then evaluates the
same planners with the probe-derived latent ablated and replaced by their
unconditional marginal reward model. The causal boundary test still decides
whether a harmful ablation concerns agent-state, external world-state, local
state, or no hidden state.
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
    risky_reward,
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
CAUSAL_LOSS_THRESHOLD = 1000.0


@dataclass(frozen=True)
class AblationConfig:
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
class AblationResult:
    environment: str
    surface: str
    scenario: str
    planner: str
    family: str
    boundary_signature: str
    causal_signature: str
    intact_reward: float
    ablated_reward: float
    reward_loss: float
    intact_mean_reward: float
    ablated_mean_reward: float
    intact_probe_rate: float
    ablated_probe_rate: float
    intact_risky_count: int
    ablated_risky_count: int
    intact_safe_count: int
    ablated_safe_count: int
    intact_failed_risky_count: int
    ablated_failed_risky_count: int
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
    expected_causal_signature: str
    boundary_signature: str
    converged_planners: int
    planner_count: int
    mean_intact_reward: float
    mean_ablated_reward: float
    mean_reward_loss: float
    planner_signatures: str
    supports_latent_causal_ablation: bool


@dataclass
class ScenarioVerdict:
    scenario: str
    expected_causal_signature: str
    supporting_environments: int
    environment_count: int
    mean_intact_reward: float
    mean_ablated_reward: float
    mean_reward_loss: float
    environment_signatures: str
    supports_latent_causal_ablation: bool


def as_model_cfg(cfg: AblationConfig) -> ModelBasedConfig:
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


def as_ablation_cross_cfg(cfg: AblationConfig) -> CrossEnvConfig:
    return CrossEnvConfig(
        episodes=cfg.episodes,
        training_episodes=cfg.training_episodes,
        seed=cfg.seed,
        calibration_contexts=cfg.calibration_contexts,
        calibration_cost=cfg.calibration_cost,
        local_probe_cost=cfg.local_probe_cost,
    )


def evaluate_ablation(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    planner: RewardModelPlanner,
    cfg: AblationConfig,
    signature: str,
) -> AblationResult:
    cross_cfg = as_ablation_cross_cfg(cfg)
    intact_reward = 0.0
    ablated_reward = 0.0
    intact_probe_uses = 0
    intact_risky = 0
    ablated_risky = 0
    intact_safe = 0
    ablated_safe = 0
    intact_failed_risky = 0
    ablated_failed_risky = 0
    latents = []
    self_labels = []
    world_labels = []
    control_labels = []

    for episode in range(cfg.episodes):
        state = sample_state(environment, scenario, episode + cfg.training_episodes * 3, cross_cfg)
        probe_rewards = tuple(
            probe_reward(state.local_success[profile.name], cfg)
            for profile in environment.contexts[: cfg.calibration_contexts]
        )
        if planner.uses_probe_history(probe_rewards):
            intact_reward -= cfg.calibration_cost
            intact_probe_uses += 1
        latents.append(planner.latent_value(probe_rewards))
        self_labels.append(state.self_signal)
        world_labels.append(state.world_signal)
        control_labels.append(majority_control_success(state.local_success, environment, cfg))

        for profile in environment.contexts[cfg.calibration_contexts :]:
            intact_choice = planned_choice(profile, planner.predict_success(probe_rewards, profile))
            ablated_choice = planned_choice(profile, ablated_success_probability(planner, profile))

            intact_delta, intact_failed = score_choice(profile, intact_choice, state.local_success[profile.name])
            ablated_delta, ablated_failed = score_choice(profile, ablated_choice, state.local_success[profile.name])
            intact_reward += intact_delta
            ablated_reward += ablated_delta

            if intact_choice == "risky":
                intact_risky += 1
                if intact_failed:
                    intact_failed_risky += 1
            else:
                intact_safe += 1
            if ablated_choice == "risky":
                ablated_risky += 1
                if ablated_failed:
                    ablated_failed_risky += 1
            else:
                ablated_safe += 1

    self_accuracy = threshold_accuracy(latents, self_labels)
    world_accuracy = threshold_accuracy(latents, world_labels)
    control_accuracy = threshold_accuracy(latents, control_labels)
    reward_loss = intact_reward - ablated_reward
    causal_signature = classify_causal_signature(
        scenario=scenario,
        boundary=signature,
        reward_loss=reward_loss,
        latent_std=sample_std(latents),
        self_accuracy=self_accuracy,
        world_accuracy=world_accuracy,
        intact_probe_rate=intact_probe_uses / cfg.episodes,
    )
    return AblationResult(
        environment=environment.name,
        surface=environment.surface,
        scenario=scenario.name,
        planner=planner.name,
        family=planner.family,
        boundary_signature=signature,
        causal_signature=causal_signature,
        intact_reward=intact_reward,
        ablated_reward=ablated_reward,
        reward_loss=reward_loss,
        intact_mean_reward=intact_reward / cfg.episodes,
        ablated_mean_reward=ablated_reward / cfg.episodes,
        intact_probe_rate=intact_probe_uses / cfg.episodes,
        ablated_probe_rate=0.0,
        intact_risky_count=intact_risky,
        ablated_risky_count=ablated_risky,
        intact_safe_count=intact_safe,
        ablated_safe_count=ablated_safe,
        intact_failed_risky_count=intact_failed_risky,
        ablated_failed_risky_count=ablated_failed_risky,
        latent_mean=statistics.fmean(latents),
        latent_std=sample_std(latents),
        latent_self_accuracy=self_accuracy,
        latent_world_accuracy=world_accuracy,
        latent_control_accuracy=control_accuracy,
        selected_model=planner.selected_model,
    )


def ablated_success_probability(planner: RewardModelPlanner, profile) -> float:
    if hasattr(planner, "context_marginals"):
        return planner.context_marginals[profile.name]
    return planner.marginal_success


def score_choice(profile, choice: str, success: bool) -> Tuple[float, bool]:
    if choice == "risky":
        return risky_reward(profile, success), not success
    return profile.safe_reward, False


def classify_causal_signature(
    scenario: ScenarioSpec,
    boundary: str,
    reward_loss: float,
    latent_std: float,
    self_accuracy: float,
    world_accuracy: float,
    intact_probe_rate: float,
) -> str:
    if scenario.mode == "irrelevant_control" and abs(reward_loss) <= EPS and intact_probe_rate <= EPS:
        return "no_hidden_needed"
    if reward_loss >= CAUSAL_LOSS_THRESHOLD:
        if boundary == "agent_bounded_cross_env" and self_accuracy >= 0.80 and world_accuracy < 0.70:
            return "agent_latent_causal"
        if boundary == "external_cross_env" and world_accuracy >= 0.80 and self_accuracy < 0.70:
            return "external_latent_causal"
        return "latent_causal_wrong_boundary"
    if boundary == "no_shared_agent_boundary" and latent_std < 0.05:
        return "no_shared_latent_causal"
    if scenario.mode == "independent_hidden" and abs(reward_loss) < CAUSAL_LOSS_THRESHOLD:
        return "no_shared_latent_causal"
    return "latent_not_causal"


def expected_causal_signature(scenario: ScenarioSpec) -> str:
    if scenario.mode == "agent_shared":
        return "agent_latent_causal"
    if scenario.mode == "world_shared":
        return "external_latent_causal"
    if scenario.mode == "independent_hidden":
        return "no_shared_latent_causal"
    if scenario.mode == "irrelevant_control":
        return "no_hidden_needed"
    raise ValueError(f"unknown scenario mode: {scenario.mode}")


def build_environment_verdicts(results: Sequence[AblationResult]) -> List[EnvironmentVerdict]:
    verdicts = []
    for environment in ENVIRONMENTS:
        for scenario in SCENARIOS:
            rows = [
                row
                for row in results
                if row.environment == environment.name and row.scenario == scenario.name
            ]
            expected = expected_causal_signature(scenario)
            converged = sum(1 for row in rows if row.causal_signature == expected)
            signatures = ";".join(f"{row.planner}:{row.causal_signature}" for row in rows)
            mean_loss = statistics.fmean(row.reward_loss for row in rows)
            supports = supports_environment(
                scenario=scenario,
                expected=expected,
                converged=converged,
                planner_count=len(rows),
                mean_loss=mean_loss,
            )
            verdicts.append(
                EnvironmentVerdict(
                    environment=environment.name,
                    surface=environment.surface,
                    scenario=scenario.name,
                    expected_causal_signature=expected,
                    boundary_signature=rows[0].boundary_signature,
                    converged_planners=converged,
                    planner_count=len(rows),
                    mean_intact_reward=statistics.fmean(row.intact_reward for row in rows),
                    mean_ablated_reward=statistics.fmean(row.ablated_reward for row in rows),
                    mean_reward_loss=mean_loss,
                    planner_signatures=signatures,
                    supports_latent_causal_ablation=supports,
                )
            )
    return verdicts


def supports_environment(
    scenario: ScenarioSpec,
    expected: str,
    converged: int,
    planner_count: int,
    mean_loss: float,
) -> bool:
    majority = converged >= max(2, math.ceil(planner_count * 0.6))
    if not majority:
        return False
    if expected in {"agent_latent_causal", "external_latent_causal"}:
        return mean_loss >= CAUSAL_LOSS_THRESHOLD
    if scenario.mode in {"independent_hidden", "irrelevant_control"}:
        return abs(mean_loss) < CAUSAL_LOSS_THRESHOLD
    return False


def build_scenario_verdicts(environment_verdicts: Sequence[EnvironmentVerdict]) -> List[ScenarioVerdict]:
    verdicts = []
    for scenario in SCENARIOS:
        rows = [row for row in environment_verdicts if row.scenario == scenario.name]
        supporting = sum(1 for row in rows if row.supports_latent_causal_ablation)
        signatures = ";".join(
            f"{row.environment}:{row.converged_planners}/{row.planner_count}:{row.expected_causal_signature}"
            for row in rows
        )
        verdicts.append(
            ScenarioVerdict(
                scenario=scenario.name,
                expected_causal_signature=expected_causal_signature(scenario),
                supporting_environments=supporting,
                environment_count=len(rows),
                mean_intact_reward=statistics.fmean(row.mean_intact_reward for row in rows),
                mean_ablated_reward=statistics.fmean(row.mean_ablated_reward for row in rows),
                mean_reward_loss=statistics.fmean(row.mean_reward_loss for row in rows),
                environment_signatures=signatures,
                supports_latent_causal_ablation=supporting == len(rows),
            )
        )
    return verdicts


def run_experiment(
    cfg: AblationConfig,
) -> Tuple[List[AblationResult], List[EnvironmentVerdict], List[ScenarioVerdict], Dict[str, object]]:
    model_cfg = as_model_cfg(cfg)
    results: List[AblationResult] = []
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
                results.append(evaluate_ablation(environment, scenario, planner, cfg, signature))
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
        "expected_causal_signature",
        "supporting_environments",
        "mean_intact_reward",
        "mean_ablated_reward",
        "mean_reward_loss",
        "supports_latent_causal_ablation",
    ]
    rows = []
    for verdict in verdicts:
        rows.append(
            [
                verdict.scenario,
                verdict.expected_causal_signature,
                f"{verdict.supporting_environments}/{verdict.environment_count}",
                f"{verdict.mean_intact_reward:.3f}",
                f"{verdict.mean_ablated_reward:.3f}",
                f"{verdict.mean_reward_loss:.3f}",
                str(verdict.supports_latent_causal_ablation),
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


def parse_args() -> AblationConfig:
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
    return AblationConfig(
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

    summary_path = ARTIFACT_DIR / "latent_causal_ablation_summary.csv"
    environment_verdict_path = ARTIFACT_DIR / "latent_causal_ablation_environment_verdict.csv"
    scenario_verdict_path = ARTIFACT_DIR / "latent_causal_ablation_scenario_verdict.csv"
    results_path = ARTIFACT_DIR / "latent_causal_ablation_results.json"
    write_csv(summary_path, results)
    write_csv(environment_verdict_path, environment_verdicts)
    write_csv(scenario_verdict_path, scenario_verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "diagnostics": diagnostics,
                "ablation_summary": [asdict(row) for row in results],
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
    return 0 if all(row.supports_latent_causal_ablation for row in scenario_verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
