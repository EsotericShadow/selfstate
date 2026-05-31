#!/usr/bin/env python3
"""Model-based planning precursor.

Earlier recurrent precursors selected policies directly by return. This
experiment separates representation learning from action choice: small planners
first learn a reward model from probe histories, then choose held-out actions by
planning over predicted risky/safe value.

The planners receive no self/world labels. The causal boundary probe still
decides whether a useful latent is agent-bounded, external, local-only, or
unnecessary.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

from cross_environment_attractor import (
    ENVIRONMENTS,
    SCENARIOS,
    ContextProfile,
    CrossEnvConfig,
    EnvironmentFamily,
    ScenarioSpec,
    boundary_signature,
    expected_signature,
    sample_state,
    should_risk,
)
from evolved_recurrent_policy import (
    classify_latent_signature,
    majority_control_success,
    probe_reward,
    risky_reward,
    sample_std,
    sigmoid,
    threshold_accuracy,
)


ARTIFACT_DIR = Path("artifacts")
EPS = 1e-12


@dataclass(frozen=True)
class ModelBasedConfig:
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


@dataclass(frozen=True)
class EpisodeTrace:
    probe_rewards: Tuple[float, ...]
    self_signal: bool
    world_signal: bool
    local_success: Dict[str, bool]


@dataclass
class PlannerResult:
    environment: str
    surface: str
    scenario: str
    planner: str
    family: str
    boundary_signature: str
    latent_signature: str
    total_reward: float
    mean_reward: float
    risky_count: int
    safe_count: int
    failed_risky_count: int
    success_rate: float
    latent_mean: float
    latent_std: float
    latent_self_accuracy: float
    latent_world_accuracy: float
    latent_control_accuracy: float
    parameter_count: int
    memory_slots: int
    uses_probe_rate: float
    selected_model: str


@dataclass
class BaselineResult:
    environment: str
    surface: str
    scenario: str
    baseline: str
    total_reward: float


@dataclass
class EnvironmentVerdict:
    environment: str
    surface: str
    scenario: str
    expected_signature: str
    boundary_signature: str
    converged_planners: int
    planner_count: int
    best_planner: str
    best_planner_reward: float
    marginal_reward: float
    local_probe_reward: float
    planner_signatures: str
    supports_model_based_precursor: bool


@dataclass
class ScenarioVerdict:
    scenario: str
    expected_signature: str
    supporting_environments: int
    environment_count: int
    mean_best_planner_reward: float
    mean_local_probe_reward: float
    mean_marginal_reward: float
    environment_signatures: str
    supports_model_based_precursor: bool


class RewardModelPlanner:
    name = "base"
    family = "base"
    parameter_count = 0

    def fit(
        self,
        traces: Sequence[EpisodeTrace],
        environment: EnvironmentFamily,
        cfg: ModelBasedConfig,
    ) -> None:
        self.environment = environment
        self.cfg = cfg
        self.marginal_success = mean_control_success(traces, environment, cfg)
        self.no_hidden = self.marginal_success > 0.95
        self.selected_model = "no_hidden" if self.no_hidden else "marginal"

    def predict_success(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> float:
        raise NotImplementedError

    def latent_value(self, probe_rewards: Tuple[float, ...]) -> float:
        raise NotImplementedError

    def uses_probe_history(self, probe_rewards: Tuple[float, ...]) -> bool:
        return not getattr(self, "no_hidden", False)

    def memory_slots(self) -> int:
        return 0


class BayesianTablePlanner(RewardModelPlanner):
    name = "bayesian_table_planner"
    family = "tabular_world_model"
    parameter_count = 4

    def fit(
        self,
        traces: Sequence[EpisodeTrace],
        environment: EnvironmentFamily,
        cfg: ModelBasedConfig,
    ) -> None:
        super().fit(traces, environment, cfg)
        self.context_marginals = context_marginals(traces, environment, cfg)
        self.table: Dict[Tuple[int, ...], Dict[str, float]] = {}
        grouped: Dict[Tuple[int, ...], List[EpisodeTrace]] = {}
        for trace in traces:
            grouped.setdefault(probe_key(trace.probe_rewards), []).append(trace)
        for key, items in grouped.items():
            self.table[key] = {}
            for profile in environment.contexts[cfg.calibration_contexts :]:
                successes = sum(1 for item in items if item.local_success[profile.name])
                self.table[key][profile.name] = (successes + 1.0) / (len(items) + 2.0)
        values = [
            statistics.fmean(row.values())
            for row in self.table.values()
            if row
        ]
        self.probe_sensitive = (not self.no_hidden) and sample_std(values) > 0.05
        self.selected_model = "probe_key_table" if self.probe_sensitive else self.selected_model

    def predict_success(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> float:
        if self.no_hidden:
            return self.context_marginals[profile.name]
        if not self.probe_sensitive:
            return self.context_marginals[profile.name]
        return self.table.get(probe_key(probe_rewards), {}).get(profile.name, self.context_marginals[profile.name])

    def latent_value(self, probe_rewards: Tuple[float, ...]) -> float:
        control_profiles = self.environment.contexts[self.cfg.calibration_contexts :]
        return statistics.fmean(self.predict_success(probe_rewards, profile) for profile in control_profiles)

    def uses_probe_history(self, probe_rewards: Tuple[float, ...]) -> bool:
        return self.probe_sensitive

    def memory_slots(self) -> int:
        return len(self.table) if self.probe_sensitive else 0


class LinearBeliefPlanner(RewardModelPlanner):
    name = "linear_belief_planner"
    family = "linear_reward_model"
    parameter_count = 2

    def fit(
        self,
        traces: Sequence[EpisodeTrace],
        environment: EnvironmentFamily,
        cfg: ModelBasedConfig,
    ) -> None:
        super().fit(traces, environment, cfg)
        self.bias = logit(clamp_probability(self.marginal_success))
        self.slope = 0.0
        if self.no_hidden:
            return
        train, validation = split_traces(traces, cfg)
        best = (validation_log_loss(validation, environment, cfg, self.predict_constant), self.bias, 0.0)
        for slope in [-4.0, -3.0, -2.0, -1.4, -1.0, -0.6, 0.0, 0.6, 1.0, 1.4, 2.0, 3.0, 4.0]:
            bias = fit_bias_for_slope(train, environment, cfg, slope)
            loss = validation_log_loss(
                validation,
                environment,
                cfg,
                lambda rewards, profile, b=bias, s=slope: sigmoid(b + s * sum(rewards)),
            )
            if loss < best[0]:
                best = (loss, bias, slope)
        constant_loss = validation_log_loss(validation, environment, cfg, self.predict_constant)
        if constant_loss - best[0] > 0.02 and abs(best[2]) > 0.1:
            self.bias = best[1]
            self.slope = best[2]
            self.selected_model = "linear_probe_belief"

    def predict_constant(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> float:
        return self.marginal_success

    def predict_success(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> float:
        if self.no_hidden or abs(self.slope) <= EPS:
            return self.marginal_success
        return sigmoid(self.latent_value(probe_rewards))

    def latent_value(self, probe_rewards: Tuple[float, ...]) -> float:
        return self.bias + self.slope * sum(probe_rewards)

    def uses_probe_history(self, probe_rewards: Tuple[float, ...]) -> bool:
        return (not self.no_hidden) and abs(self.slope) > EPS


class RecurrentBeliefPlanner(RewardModelPlanner):
    name = "recurrent_belief_planner"
    family = "recurrent_reward_model"
    parameter_count = 4

    def fit(
        self,
        traces: Sequence[EpisodeTrace],
        environment: EnvironmentFamily,
        cfg: ModelBasedConfig,
    ) -> None:
        super().fit(traces, environment, cfg)
        self.weights = (0.0, 0.0, 0.0, logit(clamp_probability(self.marginal_success)))
        if self.no_hidden:
            return
        train, validation = split_traces(traces, cfg)
        rng = random.Random(stable_name_seed(cfg.seed, environment.name, "model_based_recurrent"))
        candidates = [
            self.weights,
            (0.0, 0.0, 1.8, 0.0),
            (0.0, 0.5, 2.0, 0.0),
            (0.0, -0.5, 2.0, 0.0),
        ]
        for _ in range(cfg.recurrent_candidates):
            candidates.append(
                (
                    rng.uniform(-1.2, 1.2),
                    rng.uniform(-1.2, 1.2),
                    rng.uniform(-3.0, 3.0),
                    rng.uniform(-2.0, 2.0),
                )
            )
        constant_loss = validation_log_loss(validation, environment, cfg, self.predict_constant)
        best_loss = constant_loss
        best_weights = self.weights
        for weights in candidates:
            loss = validation_log_loss(
                validation,
                environment,
                cfg,
                lambda rewards, profile, w=weights: sigmoid(recurrent_score(rewards, w)),
            )
            if loss < best_loss:
                best_loss = loss
                best_weights = weights
        if constant_loss - best_loss > 0.02 and abs(best_weights[2]) > 0.1:
            self.weights = best_weights
            self.selected_model = "recurrent_probe_belief"

    def predict_constant(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> float:
        return self.marginal_success

    def predict_success(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> float:
        if self.no_hidden or abs(self.weights[2]) <= EPS:
            return self.marginal_success
        return sigmoid(self.latent_value(probe_rewards))

    def latent_value(self, probe_rewards: Tuple[float, ...]) -> float:
        return recurrent_score(probe_rewards, self.weights)

    def uses_probe_history(self, probe_rewards: Tuple[float, ...]) -> bool:
        return (not self.no_hidden) and abs(self.weights[2]) > EPS


PLANNER_TYPES = [BayesianTablePlanner, LinearBeliefPlanner, RecurrentBeliefPlanner]


def as_cross_cfg(cfg: ModelBasedConfig) -> CrossEnvConfig:
    return CrossEnvConfig(
        episodes=cfg.episodes,
        training_episodes=cfg.training_episodes,
        seed=cfg.seed,
        calibration_contexts=cfg.calibration_contexts,
        calibration_cost=cfg.calibration_cost,
        local_probe_cost=cfg.local_probe_cost,
    )


def make_traces(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    cfg: ModelBasedConfig,
) -> List[EpisodeTrace]:
    cross_cfg = as_cross_cfg(cfg)
    traces = []
    for episode in range(cfg.training_episodes):
        state = sample_state(environment, scenario, episode, cross_cfg)
        traces.append(
            EpisodeTrace(
                probe_rewards=tuple(
                    probe_reward(state.local_success[profile.name], cfg)
                    for profile in environment.contexts[: cfg.calibration_contexts]
                ),
                self_signal=state.self_signal,
                world_signal=state.world_signal,
                local_success=state.local_success,
            )
        )
    return traces


def evaluate_planner(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    planner: RewardModelPlanner,
    cfg: ModelBasedConfig,
    signature: str,
) -> PlannerResult:
    cross_cfg = as_cross_cfg(cfg)
    total_reward = 0.0
    risky_count = 0
    safe_count = 0
    failed_risky_count = 0
    risky_success_count = 0
    probe_uses = 0
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
        uses_probe = planner.uses_probe_history(probe_rewards)
        if uses_probe:
            total_reward -= cfg.calibration_cost
            probe_uses += 1
        latents.append(planner.latent_value(probe_rewards))
        self_labels.append(state.self_signal)
        world_labels.append(state.world_signal)
        control_labels.append(majority_control_success(state.local_success, environment, cfg))
        for profile in environment.contexts[cfg.calibration_contexts :]:
            success_probability = planner.predict_success(probe_rewards, profile)
            choice = planned_choice(profile, success_probability)
            if choice == "risky":
                risky_count += 1
                if state.local_success[profile.name]:
                    risky_success_count += 1
                    total_reward += profile.risky_success_reward
                else:
                    failed_risky_count += 1
                    total_reward += profile.risky_failure_reward
            else:
                safe_count += 1
                total_reward += profile.safe_reward
    self_accuracy = threshold_accuracy(latents, self_labels)
    world_accuracy = threshold_accuracy(latents, world_labels)
    control_accuracy = threshold_accuracy(latents, control_labels)
    latent_signature = classify_latent_signature(
        scenario=scenario,
        boundary=signature,
        latent_std=sample_std(latents),
        self_accuracy=self_accuracy,
        world_accuracy=world_accuracy,
        control_accuracy=control_accuracy,
    )
    return PlannerResult(
        environment=environment.name,
        surface=environment.surface,
        scenario=scenario.name,
        planner=planner.name,
        family=planner.family,
        boundary_signature=signature,
        latent_signature=latent_signature,
        total_reward=total_reward,
        mean_reward=total_reward / cfg.episodes,
        risky_count=risky_count,
        safe_count=safe_count,
        failed_risky_count=failed_risky_count,
        success_rate=(risky_success_count / risky_count) if risky_count else 0.0,
        latent_mean=statistics.fmean(latents),
        latent_std=sample_std(latents),
        latent_self_accuracy=self_accuracy,
        latent_world_accuracy=world_accuracy,
        latent_control_accuracy=control_accuracy,
        parameter_count=planner.parameter_count,
        memory_slots=planner.memory_slots(),
        uses_probe_rate=probe_uses / cfg.episodes,
        selected_model=planner.selected_model,
    )


def evaluate_baseline(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    cfg: ModelBasedConfig,
    baseline: str,
) -> BaselineResult:
    cross_cfg = as_cross_cfg(cfg)
    traces = make_traces(environment, scenario, cfg)
    marginal_success = mean_control_success(traces, environment, cfg)
    total_reward = 0.0
    for episode in range(cfg.episodes):
        state = sample_state(environment, scenario, episode + cfg.training_episodes * 3, cross_cfg)
        for profile in environment.contexts[cfg.calibration_contexts :]:
            if baseline == "marginal_no_memory":
                choice = "risky" if should_risk(profile, marginal_success) else "safe"
            elif baseline == "task_local_probe":
                total_reward -= cfg.local_probe_cost
                choice = "risky" if state.local_success[profile.name] else "safe"
            elif baseline == "oracle":
                choice = "risky" if state.local_success[profile.name] else "safe"
            else:
                raise ValueError(f"unknown baseline: {baseline}")
            if choice == "risky":
                total_reward += risky_reward(profile, state.local_success[profile.name])
            else:
                total_reward += profile.safe_reward
    return BaselineResult(
        environment=environment.name,
        surface=environment.surface,
        scenario=scenario.name,
        baseline=baseline,
        total_reward=total_reward,
    )


def planned_choice(profile: ContextProfile, success_probability: float) -> str:
    expected_risky = success_probability * profile.risky_success_reward
    expected_risky += (1.0 - success_probability) * profile.risky_failure_reward
    return "risky" if expected_risky >= profile.safe_reward else "safe"


def build_environment_verdicts(
    planner_results: Sequence[PlannerResult],
    baseline_results: Sequence[BaselineResult],
) -> List[EnvironmentVerdict]:
    verdicts = []
    for environment in ENVIRONMENTS:
        for scenario in SCENARIOS:
            rows = [
                row
                for row in planner_results
                if row.environment == environment.name and row.scenario == scenario.name
            ]
            baselines = [
                row
                for row in baseline_results
                if row.environment == environment.name and row.scenario == scenario.name
            ]
            expected = expected_signature(scenario)
            converged = sum(1 for row in rows if row.latent_signature == expected)
            best = max(rows, key=lambda row: row.total_reward)
            marginal = next(row for row in baselines if row.baseline == "marginal_no_memory")
            local = next(row for row in baselines if row.baseline == "task_local_probe")
            signatures = ";".join(f"{row.planner}:{row.latent_signature}" for row in rows)
            supports = supports_environment(
                scenario=scenario,
                converged=converged,
                planner_count=len(rows),
                best=best,
                marginal=marginal,
                local=local,
            )
            verdicts.append(
                EnvironmentVerdict(
                    environment=environment.name,
                    surface=environment.surface,
                    scenario=scenario.name,
                    expected_signature=expected,
                    boundary_signature=rows[0].boundary_signature,
                    converged_planners=converged,
                    planner_count=len(rows),
                    best_planner=best.planner,
                    best_planner_reward=best.total_reward,
                    marginal_reward=marginal.total_reward,
                    local_probe_reward=local.total_reward,
                    planner_signatures=signatures,
                    supports_model_based_precursor=supports,
                )
            )
    return verdicts


def supports_environment(
    scenario: ScenarioSpec,
    converged: int,
    planner_count: int,
    best: PlannerResult,
    marginal: BaselineResult,
    local: BaselineResult,
) -> bool:
    majority = converged >= max(2, math.ceil(planner_count * 0.6))
    if not majority:
        return False
    if scenario.mode in {"agent_shared", "world_shared"}:
        return best.total_reward > local.total_reward + 1.0
    if scenario.mode == "independent_hidden":
        return local.total_reward > best.total_reward + 10.0
    if scenario.mode == "irrelevant_control":
        return best.total_reward >= marginal.total_reward - EPS
    return False


def build_scenario_verdicts(environment_verdicts: Sequence[EnvironmentVerdict]) -> List[ScenarioVerdict]:
    verdicts = []
    for scenario in SCENARIOS:
        rows = [row for row in environment_verdicts if row.scenario == scenario.name]
        supporting = sum(1 for row in rows if row.supports_model_based_precursor)
        signatures = ";".join(
            f"{row.environment}:{row.converged_planners}/{row.planner_count}:{row.expected_signature}"
            for row in rows
        )
        verdicts.append(
            ScenarioVerdict(
                scenario=scenario.name,
                expected_signature=expected_signature(scenario),
                supporting_environments=supporting,
                environment_count=len(rows),
                mean_best_planner_reward=statistics.fmean(row.best_planner_reward for row in rows),
                mean_local_probe_reward=statistics.fmean(row.local_probe_reward for row in rows),
                mean_marginal_reward=statistics.fmean(row.marginal_reward for row in rows),
                environment_signatures=signatures,
                supports_model_based_precursor=supporting == len(rows),
            )
        )
    return verdicts


def run_experiment(
    cfg: ModelBasedConfig,
) -> Tuple[List[PlannerResult], List[BaselineResult], List[EnvironmentVerdict], List[ScenarioVerdict], Dict[str, object]]:
    planner_results: List[PlannerResult] = []
    baseline_results: List[BaselineResult] = []
    diagnostics: Dict[str, object] = {}
    cross_cfg = as_cross_cfg(cfg)
    for environment in ENVIRONMENTS:
        for scenario in SCENARIOS:
            traces = make_traces(environment, scenario, cfg)
            signature, agent_effect, world_effect = boundary_signature(environment, scenario, cross_cfg)
            diagnostics[f"{environment.name}:{scenario.name}"] = {
                "boundary_signature": signature,
                "agent_intervention_effect": agent_effect,
                "world_intervention_effect": world_effect,
                "training_marginal_success": mean_control_success(traces, environment, cfg),
            }
            for planner_type in PLANNER_TYPES:
                planner = planner_type()
                planner.fit(traces, environment, cfg)
                planner_results.append(evaluate_planner(environment, scenario, planner, cfg, signature))
            for baseline in ["marginal_no_memory", "task_local_probe", "oracle"]:
                baseline_results.append(evaluate_baseline(environment, scenario, cfg, baseline))
    environment_verdicts = build_environment_verdicts(planner_results, baseline_results)
    scenario_verdicts = build_scenario_verdicts(environment_verdicts)
    return planner_results, baseline_results, environment_verdicts, scenario_verdicts, diagnostics


def mean_control_success(
    traces: Sequence[EpisodeTrace],
    environment: EnvironmentFamily,
    cfg: ModelBasedConfig,
) -> float:
    return statistics.fmean(
        1.0 if trace.local_success[profile.name] else 0.0
        for trace in traces
        for profile in environment.contexts[cfg.calibration_contexts :]
    )


def context_marginals(
    traces: Sequence[EpisodeTrace],
    environment: EnvironmentFamily,
    cfg: ModelBasedConfig,
) -> Dict[str, float]:
    values = {}
    for profile in environment.contexts[cfg.calibration_contexts :]:
        successes = sum(1 for trace in traces if trace.local_success[profile.name])
        values[profile.name] = (successes + 1.0) / (len(traces) + 2.0)
    return values


def split_traces(
    traces: Sequence[EpisodeTrace],
    cfg: ModelBasedConfig,
) -> Tuple[Sequence[EpisodeTrace], Sequence[EpisodeTrace]]:
    split_index = max(1, int(len(traces) * (1.0 - cfg.validation_fraction)))
    return traces[:split_index], traces[split_index:]


def fit_bias_for_slope(
    traces: Sequence[EpisodeTrace],
    environment: EnvironmentFamily,
    cfg: ModelBasedConfig,
    slope: float,
) -> float:
    candidates = [value * 0.25 for value in range(-24, 25)]
    return min(
        candidates,
        key=lambda bias: validation_log_loss(
            traces,
            environment,
            cfg,
            lambda rewards, profile, b=bias, s=slope: sigmoid(b + s * sum(rewards)),
        ),
    )


def validation_log_loss(
    traces: Sequence[EpisodeTrace],
    environment: EnvironmentFamily,
    cfg: ModelBasedConfig,
    predictor,
) -> float:
    total = 0.0
    count = 0
    for trace in traces:
        for profile in environment.contexts[cfg.calibration_contexts :]:
            probability = clamp_probability(predictor(trace.probe_rewards, profile))
            label = 1.0 if trace.local_success[profile.name] else 0.0
            total -= label * math.log(probability) + (1.0 - label) * math.log(1.0 - probability)
            count += 1
    return total / max(1, count)


def recurrent_score(probe_rewards: Tuple[float, ...], weights: Tuple[float, ...]) -> float:
    bias, recurrent, input_weight, output_bias = weights
    hidden = 0.0
    for reward in probe_rewards:
        hidden = math.tanh(bias + recurrent * hidden + input_weight * reward)
    return output_bias + 3.0 * hidden


def probe_key(probe_rewards: Tuple[float, ...]) -> Tuple[int, ...]:
    return tuple(1 if reward > 0.0 else 0 for reward in probe_rewards)


def clamp_probability(value: float) -> float:
    return min(1.0 - 1e-6, max(1e-6, value))


def logit(value: float) -> float:
    value = clamp_probability(value)
    return math.log(value / (1.0 - value))


def stable_name_seed(seed: int, left: str, right: str) -> int:
    value = seed
    for char in f"{left}:{right}":
        value = (value * 131 + ord(char)) % (2**32)
    return value


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
        "expected_signature",
        "supporting_environments",
        "mean_best_planner_reward",
        "mean_local_probe_reward",
        "supports_model_based_precursor",
    ]
    rows = []
    for verdict in verdicts:
        rows.append(
            [
                verdict.scenario,
                verdict.expected_signature,
                f"{verdict.supporting_environments}/{verdict.environment_count}",
                f"{verdict.mean_best_planner_reward:.3f}",
                f"{verdict.mean_local_probe_reward:.3f}",
                str(verdict.supports_model_based_precursor),
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


def parse_args() -> ModelBasedConfig:
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
    return ModelBasedConfig(
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
    planner_results, baseline_results, environment_verdicts, scenario_verdicts, diagnostics = run_experiment(cfg)

    summary_path = ARTIFACT_DIR / "model_based_planning_summary.csv"
    baseline_path = ARTIFACT_DIR / "model_based_planning_baselines.csv"
    environment_verdict_path = ARTIFACT_DIR / "model_based_planning_environment_verdict.csv"
    scenario_verdict_path = ARTIFACT_DIR / "model_based_planning_scenario_verdict.csv"
    results_path = ARTIFACT_DIR / "model_based_planning_results.json"
    write_csv(summary_path, planner_results)
    write_csv(baseline_path, baseline_results)
    write_csv(environment_verdict_path, environment_verdicts)
    write_csv(scenario_verdict_path, scenario_verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "diagnostics": diagnostics,
                "planner_summary": [asdict(row) for row in planner_results],
                "baseline_summary": [asdict(row) for row in baseline_results],
                "environment_verdict": [asdict(row) for row in environment_verdicts],
                "scenario_verdict": [asdict(row) for row in scenario_verdicts],
            },
            handle,
            indent=2,
        )
        handle.write("\n")

    print(f"wrote {summary_path}")
    print(f"wrote {baseline_path}")
    print(f"wrote {environment_verdict_path}")
    print(f"wrote {scenario_verdict_path}")
    print(f"wrote {results_path}")
    print_table(scenario_verdicts)
    return 0 if all(row.supports_model_based_precursor for row in scenario_verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
