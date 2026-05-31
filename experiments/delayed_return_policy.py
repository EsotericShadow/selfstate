#!/usr/bin/env python3
"""Delayed-return policy precursor.

Raw-history learning still lets learners estimate later reward from observed
training outcomes. This experiment makes the training signal weaker: candidate
memory policies are selected by delayed episode return after they have already
acted.

Learners observe only early probe rewards during an episode. They choose risky
or safe actions in held-out contexts. During training, policy rules are scored
by the final episode return, not by per-context success labels. The causal
boundary probe still determines whether a useful memory state is agent-bounded
or external.
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
from typing import Callable, Dict, Iterable, List, Sequence, Tuple

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


ARTIFACT_DIR = Path("artifacts")
EPS = 1e-12


@dataclass(frozen=True)
class DelayedConfig:
    episodes: int = 500
    training_episodes: int = 500
    seed: int = 20260601
    calibration_contexts: int = 2
    calibration_cost: float = 1.0
    local_probe_cost: float = 1.0
    probe_success_reward: float = 1.0
    probe_failure_reward: float = -1.0
    evolutionary_candidates: int = 500


@dataclass(frozen=True)
class EpisodeTrace:
    probe_rewards: Tuple[float, ...]
    self_signal: bool
    world_signal: bool
    local_success: Dict[str, bool]


@dataclass
class PolicyResult:
    environment: str
    surface: str
    scenario: str
    learner: str
    family: str
    boundary_signature: str
    latent_signature: str
    selected_rule: str
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
    uses_probe_rate: float


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
    converged_policies: int
    policy_count: int
    best_policy: str
    best_policy_reward: float
    marginal_reward: float
    local_probe_reward: float
    policy_signatures: str
    supports_delayed_return_precursor: bool


@dataclass
class ScenarioVerdict:
    scenario: str
    expected_signature: str
    supporting_environments: int
    environment_count: int
    mean_best_policy_reward: float
    mean_local_probe_reward: float
    mean_marginal_reward: float
    environment_signatures: str
    supports_delayed_return_precursor: bool


class DelayedPolicy:
    name = "base"
    family = "base"
    parameter_count = 0

    def fit(
        self,
        traces: Sequence[EpisodeTrace],
        environment: EnvironmentFamily,
        cfg: DelayedConfig,
    ) -> None:
        self.environment = environment
        self.cfg = cfg
        self.selected_rule = "unfit"

    def choose(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> str:
        raise NotImplementedError

    def latent_value(self, probe_rewards: Tuple[float, ...]) -> float:
        raise NotImplementedError

    def uses_probe_history(self, probe_rewards: Tuple[float, ...]) -> bool:
        return True


class ReturnThresholdPolicy(DelayedPolicy):
    name = "return_threshold_policy"
    family = "threshold_return"
    parameter_count = 2

    def fit(
        self,
        traces: Sequence[EpisodeTrace],
        environment: EnvironmentFamily,
        cfg: DelayedConfig,
    ) -> None:
        super().fit(traces, environment, cfg)
        candidates = [
            ("always_risky", -999.0, False),
            ("always_safe", 999.0, False),
            ("risk_if_any_probe_good", -0.1, True),
            ("risk_if_all_probe_good", 1.1, True),
            ("risk_if_probe_majority_good", 0.0, True),
        ]
        self.selected_rule, self.threshold, self.use_probe = max(
            candidates,
            key=lambda item: score_policy(
                traces,
                environment,
                cfg,
                lambda rewards, profile, threshold=item[1]: "risky" if sum(rewards) >= threshold else "safe",
                lambda rewards, use_probe=item[2]: use_probe,
            ),
        )

    def choose(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> str:
        return "risky" if sum(probe_rewards) >= self.threshold else "safe"

    def latent_value(self, probe_rewards: Tuple[float, ...]) -> float:
        return sum(probe_rewards)

    def uses_probe_history(self, probe_rewards: Tuple[float, ...]) -> bool:
        return self.use_probe


class ReturnTablePolicy(DelayedPolicy):
    name = "return_table_policy"
    family = "table_return"
    parameter_count = 4

    def fit(
        self,
        traces: Sequence[EpisodeTrace],
        environment: EnvironmentFamily,
        cfg: DelayedConfig,
    ) -> None:
        super().fit(traces, environment, cfg)
        keys = possible_probe_keys(cfg.calibration_contexts)
        candidates = []
        for mask in range(2 ** len(keys)):
            mapping = {}
            for index, key in enumerate(keys):
                mapping[key] = "risky" if mask & (1 << index) else "safe"
            candidates.append(mapping)
        self.mapping = max(
            candidates,
            key=lambda mapping: score_policy(
                traces,
                environment,
                cfg,
                lambda rewards, profile, table=mapping: table[probe_key(rewards)],
                lambda rewards, table=mapping: len(set(table.values())) > 1,
            ),
        )
        self.selected_rule = table_rule_name(self.mapping)

    def choose(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> str:
        return self.mapping[probe_key(probe_rewards)]

    def latent_value(self, probe_rewards: Tuple[float, ...]) -> float:
        key = probe_key(probe_rewards)
        return float(sum(key))

    def uses_probe_history(self, probe_rewards: Tuple[float, ...]) -> bool:
        return len(set(self.mapping.values())) > 1


class ReturnRecurrentPolicy(DelayedPolicy):
    name = "return_recurrent_policy"
    family = "recurrent_return"
    parameter_count = 4

    def fit(
        self,
        traces: Sequence[EpisodeTrace],
        environment: EnvironmentFamily,
        cfg: DelayedConfig,
    ) -> None:
        super().fit(traces, environment, cfg)
        starts = [-1.0, 0.0, 1.0]
        steps = [0.0, 0.6, 1.0, 1.6, 2.2, 2.8]
        leaks = [0.0, 0.35, 0.7, 1.0]
        thresholds = [-1.0, 0.0, 1.0]
        candidates = [
            (start, step, leak, threshold)
            for start in starts
            for step in steps
            for leak in leaks
            for threshold in thresholds
        ]
        self.start, self.step, self.leak, self.threshold = max(
            candidates,
            key=lambda params: score_policy(
                traces,
                environment,
                cfg,
                lambda rewards, profile, p=params: "risky"
                if recurrent_state(rewards, p[0], p[1], p[2]) >= p[3]
                else "safe",
                lambda rewards, p=params: abs(p[1]) > EPS,
            ),
        )
        self.selected_rule = f"start={self.start:.1f},step={self.step:.1f},leak={self.leak:.2f},threshold={self.threshold:.1f}"

    def choose(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> str:
        return "risky" if self.latent_value(probe_rewards) >= self.threshold else "safe"

    def latent_value(self, probe_rewards: Tuple[float, ...]) -> float:
        return recurrent_state(probe_rewards, self.start, self.step, self.leak)

    def uses_probe_history(self, probe_rewards: Tuple[float, ...]) -> bool:
        return abs(self.step) > EPS


class EvolvedReturnRule(DelayedPolicy):
    name = "evolved_return_rule"
    family = "evolutionary_return"
    parameter_count = 5

    def fit(
        self,
        traces: Sequence[EpisodeTrace],
        environment: EnvironmentFamily,
        cfg: DelayedConfig,
    ) -> None:
        super().fit(traces, environment, cfg)
        rng = random.Random(stable_name_seed(cfg.seed, environment.name, "delayed_return"))
        candidates = [
            (-999.0, 0.0, 0.0, 0.0, 0.0),
            (999.0, 0.0, 0.0, 0.0, 0.0),
            (-0.5, 1.5, -1.5, 0.5, 0.0),
            (0.0, 1.4, -1.4, 0.8, 0.2),
        ]
        for _ in range(cfg.evolutionary_candidates):
            candidates.append(
                (
                    rng.uniform(-2.5, 2.5),
                    rng.uniform(-3.0, 3.0),
                    rng.uniform(-3.0, 3.0),
                    rng.uniform(-1.5, 1.5),
                    rng.uniform(-1.0, 1.0),
                )
            )
        self.weights = max(
            candidates,
            key=lambda weights: score_policy(
                traces,
                environment,
                cfg,
                lambda rewards, profile, w=weights: "risky" if rule_score(rewards, w) >= 0.0 else "safe",
                lambda rewards, w=weights: any(abs(weight) > EPS for weight in w[1:]),
            ),
        )
        self.selected_rule = "weights=" + ",".join(f"{value:.2f}" for value in self.weights)

    def choose(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> str:
        return "risky" if self.latent_value(probe_rewards) >= 0.0 else "safe"

    def latent_value(self, probe_rewards: Tuple[float, ...]) -> float:
        return rule_score(probe_rewards, self.weights)

    def uses_probe_history(self, probe_rewards: Tuple[float, ...]) -> bool:
        return any(abs(weight) > EPS for weight in self.weights[1:])


class ReturnBottleneckPolicy(DelayedPolicy):
    name = "return_bottleneck_policy"
    family = "bottleneck_return"
    parameter_count = 6

    def fit(
        self,
        traces: Sequence[EpisodeTrace],
        environment: EnvironmentFamily,
        cfg: DelayedConfig,
    ) -> None:
        super().fit(traces, environment, cfg)
        clusters = possible_probe_counts(cfg.calibration_contexts)
        candidates = []
        for mask in range(2 ** len(clusters)):
            mapping = {}
            for index, count in enumerate(clusters):
                mapping[count] = "risky" if mask & (1 << index) else "safe"
            candidates.append(mapping)
        self.mapping = max(
            candidates,
            key=lambda mapping: score_policy(
                traces,
                environment,
                cfg,
                lambda rewards, profile, table=mapping: table[positive_count(rewards)],
                lambda rewards, table=mapping: len(set(table.values())) > 1,
            ),
        )
        self.selected_rule = "clusters=" + ",".join(f"{key}:{value}" for key, value in sorted(self.mapping.items()))

    def choose(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> str:
        return self.mapping[positive_count(probe_rewards)]

    def latent_value(self, probe_rewards: Tuple[float, ...]) -> float:
        return float(positive_count(probe_rewards))

    def uses_probe_history(self, probe_rewards: Tuple[float, ...]) -> bool:
        return len(set(self.mapping.values())) > 1


POLICY_TYPES = [
    ReturnThresholdPolicy,
    ReturnTablePolicy,
    ReturnRecurrentPolicy,
    EvolvedReturnRule,
    ReturnBottleneckPolicy,
]


def as_cross_cfg(cfg: DelayedConfig) -> CrossEnvConfig:
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
    cfg: DelayedConfig,
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


def evaluate_policy(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    policy: DelayedPolicy,
    cfg: DelayedConfig,
    signature: str,
) -> PolicyResult:
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
        if policy.uses_probe_history(probe_rewards):
            total_reward -= cfg.calibration_cost
            probe_uses += 1
        latents.append(policy.latent_value(probe_rewards))
        self_labels.append(state.self_signal)
        world_labels.append(state.world_signal)
        control_labels.append(majority_control_success(state.local_success, environment, cfg))
        for profile in environment.contexts[cfg.calibration_contexts :]:
            choice = policy.choose(probe_rewards, profile)
            if choice == "risky":
                risky_count += 1
                if state.local_success[profile.name]:
                    risky_success_count += 1
                    total_reward += profile.risky_success_reward
                else:
                    failed_risky_count += 1
                    total_reward += profile.risky_failure_reward
            elif choice == "safe":
                safe_count += 1
                total_reward += profile.safe_reward
            else:
                raise ValueError(f"unknown choice: {choice}")
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
    return PolicyResult(
        environment=environment.name,
        surface=environment.surface,
        scenario=scenario.name,
        learner=policy.name,
        family=policy.family,
        boundary_signature=signature,
        latent_signature=latent_signature,
        selected_rule=policy.selected_rule,
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
        parameter_count=policy.parameter_count,
        uses_probe_rate=probe_uses / cfg.episodes,
    )


def evaluate_baseline(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    cfg: DelayedConfig,
    baseline: str,
) -> BaselineResult:
    cross_cfg = as_cross_cfg(cfg)
    traces = make_traces(environment, scenario, cfg)
    marginal_success = mean_success(traces, environment, cfg)
    total_reward = 0.0
    for episode in range(cfg.episodes):
        state = sample_state(environment, scenario, episode + cfg.training_episodes * 3, cross_cfg)
        if baseline == "probe_memory_no_transfer":
            total_reward -= cfg.calibration_cost
        for profile in environment.contexts[cfg.calibration_contexts :]:
            if baseline in {"marginal_no_memory", "probe_memory_no_transfer"}:
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


def score_policy(
    traces: Sequence[EpisodeTrace],
    environment: EnvironmentFamily,
    cfg: DelayedConfig,
    chooser: Callable[[Tuple[float, ...], ContextProfile], str],
    uses_probe: Callable[[Tuple[float, ...]], bool],
) -> float:
    total = 0.0
    for trace in traces:
        if uses_probe(trace.probe_rewards):
            total -= cfg.calibration_cost
        for profile in environment.contexts[cfg.calibration_contexts :]:
            choice = chooser(trace.probe_rewards, profile)
            if choice == "risky":
                total += risky_reward(profile, trace.local_success[profile.name])
            elif choice == "safe":
                total += profile.safe_reward
            else:
                raise ValueError(f"unknown choice: {choice}")
    return total / len(traces)


def classify_latent_signature(
    scenario: ScenarioSpec,
    boundary: str,
    latent_std: float,
    self_accuracy: float,
    world_accuracy: float,
    control_accuracy: float,
) -> str:
    if scenario.mode == "irrelevant_control" and latent_std < 0.05:
        return "no_hidden_needed"
    if boundary == "agent_bounded_cross_env" and self_accuracy >= 0.80 and world_accuracy < 0.70:
        return "agent_bounded_candidate"
    if boundary == "external_cross_env" and world_accuracy >= 0.80 and self_accuracy < 0.70:
        return "external_candidate"
    if boundary == "no_shared_agent_boundary":
        return "no_shared_agent_boundary"
    if control_accuracy >= 0.80:
        return "unbounded_return_memory_candidate"
    return "task_or_noise_latent"


def build_environment_verdicts(
    policy_results: Sequence[PolicyResult],
    baseline_results: Sequence[BaselineResult],
) -> List[EnvironmentVerdict]:
    verdicts = []
    for environment in ENVIRONMENTS:
        for scenario in SCENARIOS:
            rows = [
                row
                for row in policy_results
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
            signatures = ";".join(f"{row.learner}:{row.latent_signature}" for row in rows)
            supports = supports_environment(
                scenario=scenario,
                converged=converged,
                policy_count=len(rows),
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
                    converged_policies=converged,
                    policy_count=len(rows),
                    best_policy=best.learner,
                    best_policy_reward=best.total_reward,
                    marginal_reward=marginal.total_reward,
                    local_probe_reward=local.total_reward,
                    policy_signatures=signatures,
                    supports_delayed_return_precursor=supports,
                )
            )
    return verdicts


def supports_environment(
    scenario: ScenarioSpec,
    converged: int,
    policy_count: int,
    best: PolicyResult,
    marginal: BaselineResult,
    local: BaselineResult,
) -> bool:
    majority = converged >= max(3, math.ceil(policy_count * 0.6))
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
        supporting = sum(1 for row in rows if row.supports_delayed_return_precursor)
        signatures = ";".join(
            f"{row.environment}:{row.converged_policies}/{row.policy_count}:{row.expected_signature}"
            for row in rows
        )
        verdicts.append(
            ScenarioVerdict(
                scenario=scenario.name,
                expected_signature=expected_signature(scenario),
                supporting_environments=supporting,
                environment_count=len(rows),
                mean_best_policy_reward=statistics.fmean(row.best_policy_reward for row in rows),
                mean_local_probe_reward=statistics.fmean(row.local_probe_reward for row in rows),
                mean_marginal_reward=statistics.fmean(row.marginal_reward for row in rows),
                environment_signatures=signatures,
                supports_delayed_return_precursor=supporting == len(rows),
            )
        )
    return verdicts


def run_experiment(
    cfg: DelayedConfig,
) -> Tuple[List[PolicyResult], List[BaselineResult], List[EnvironmentVerdict], List[ScenarioVerdict], Dict[str, object]]:
    policy_results: List[PolicyResult] = []
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
                "training_marginal_success": mean_success(traces, environment, cfg),
            }
            for policy_type in POLICY_TYPES:
                policy = policy_type()
                policy.fit(traces, environment, cfg)
                policy_results.append(evaluate_policy(environment, scenario, policy, cfg, signature))
            for baseline in ["marginal_no_memory", "probe_memory_no_transfer", "task_local_probe", "oracle"]:
                baseline_results.append(evaluate_baseline(environment, scenario, cfg, baseline))
    environment_verdicts = build_environment_verdicts(policy_results, baseline_results)
    scenario_verdicts = build_scenario_verdicts(environment_verdicts)
    return policy_results, baseline_results, environment_verdicts, scenario_verdicts, diagnostics


def probe_reward(success: bool, cfg: DelayedConfig) -> float:
    return cfg.probe_success_reward if success else cfg.probe_failure_reward


def risky_reward(profile: ContextProfile, success: bool) -> float:
    return profile.risky_success_reward if success else profile.risky_failure_reward


def mean_success(
    traces: Sequence[EpisodeTrace],
    environment: EnvironmentFamily,
    cfg: DelayedConfig,
) -> float:
    return statistics.fmean(
        1.0 if trace.local_success[profile.name] else 0.0
        for trace in traces
        for profile in environment.contexts[cfg.calibration_contexts :]
    )


def majority_control_success(
    local_success: Dict[str, bool],
    environment: EnvironmentFamily,
    cfg: DelayedConfig,
) -> bool:
    values = [
        local_success[profile.name]
        for profile in environment.contexts[cfg.calibration_contexts :]
    ]
    return sum(1 for value in values if value) >= math.ceil(len(values) / 2)


def possible_probe_keys(width: int) -> List[Tuple[int, ...]]:
    if width == 0:
        return [()]
    smaller = possible_probe_keys(width - 1)
    return [key + (0,) for key in smaller] + [key + (1,) for key in smaller]


def possible_probe_counts(width: int) -> List[int]:
    return list(range(width + 1))


def probe_key(probe_rewards: Tuple[float, ...]) -> Tuple[int, ...]:
    return tuple(1 if reward > 0.0 else 0 for reward in probe_rewards)


def positive_count(probe_rewards: Tuple[float, ...]) -> int:
    return sum(1 for reward in probe_rewards if reward > 0.0)


def recurrent_state(probe_rewards: Tuple[float, ...], start: float, step: float, leak: float) -> float:
    value = start
    for reward in probe_rewards:
        value = leak * value + step * (1.0 if reward > 0.0 else -1.0)
    return value


def rule_score(probe_rewards: Tuple[float, ...], weights: Tuple[float, float, float, float, float]) -> float:
    intercept, positive_weight, negative_weight, agreement_weight, sum_weight = weights
    positives = positive_count(probe_rewards)
    negatives = len(probe_rewards) - positives
    agreement = 1.0 if positives in {0, len(probe_rewards)} else 0.0
    return (
        intercept
        + positive_weight * positives
        + negative_weight * negatives
        + agreement_weight * agreement
        + sum_weight * sum(probe_rewards)
    )


def table_rule_name(mapping: Dict[Tuple[int, ...], str]) -> str:
    return ";".join(f"{''.join(str(bit) for bit in key)}:{value}" for key, value in sorted(mapping.items()))


def threshold_accuracy(values: Sequence[float], labels: Sequence[bool]) -> float:
    if not values:
        return 0.5
    if all(label == labels[0] for label in labels):
        return 0.5
    unique_values = sorted(set(values))
    thresholds = [unique_values[0] - EPS, unique_values[-1] + EPS]
    thresholds.extend((left + right) / 2.0 for left, right in zip(unique_values, unique_values[1:]))
    best = 0.0
    for threshold in thresholds:
        for direction in [1, -1]:
            correct = 0
            for value, label in zip(values, labels):
                prediction = value >= threshold if direction == 1 else value <= threshold
                if prediction == label:
                    correct += 1
            best = max(best, correct / len(values))
    return best


def sample_std(values: Sequence[float]) -> float:
    if len(values) < 2:
        return 0.0
    return statistics.pstdev(values)


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
        "mean_best_policy_reward",
        "mean_local_probe_reward",
        "supports_delayed_return_precursor",
    ]
    rows = []
    for verdict in verdicts:
        rows.append(
            [
                verdict.scenario,
                verdict.expected_signature,
                f"{verdict.supporting_environments}/{verdict.environment_count}",
                f"{verdict.mean_best_policy_reward:.3f}",
                f"{verdict.mean_local_probe_reward:.3f}",
                str(verdict.supports_delayed_return_precursor),
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


def parse_args() -> DelayedConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=500)
    parser.add_argument("--training-episodes", type=int, default=500)
    parser.add_argument("--seed", type=int, default=20260601)
    parser.add_argument("--calibration-contexts", type=int, default=2)
    parser.add_argument("--calibration-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    parser.add_argument("--probe-success-reward", type=float, default=1.0)
    parser.add_argument("--probe-failure-reward", type=float, default=-1.0)
    parser.add_argument("--evolutionary-candidates", type=int, default=500)
    args = parser.parse_args()
    if args.calibration_contexts < 1:
        raise SystemExit("--calibration-contexts must be at least 1")
    if any(args.calibration_contexts >= len(environment.contexts) for environment in ENVIRONMENTS):
        raise SystemExit("--calibration-contexts must leave held-out contexts")
    return DelayedConfig(
        episodes=args.episodes,
        training_episodes=args.training_episodes,
        seed=args.seed,
        calibration_contexts=args.calibration_contexts,
        calibration_cost=args.calibration_cost,
        local_probe_cost=args.local_probe_cost,
        probe_success_reward=args.probe_success_reward,
        probe_failure_reward=args.probe_failure_reward,
        evolutionary_candidates=args.evolutionary_candidates,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    policy_results, baseline_results, environment_verdicts, scenario_verdicts, diagnostics = run_experiment(cfg)

    summary_path = ARTIFACT_DIR / "delayed_return_policy_summary.csv"
    baseline_path = ARTIFACT_DIR / "delayed_return_policy_baselines.csv"
    environment_verdict_path = ARTIFACT_DIR / "delayed_return_policy_environment_verdict.csv"
    scenario_verdict_path = ARTIFACT_DIR / "delayed_return_policy_scenario_verdict.csv"
    results_path = ARTIFACT_DIR / "delayed_return_policy_results.json"
    write_csv(summary_path, policy_results)
    write_csv(baseline_path, baseline_results)
    write_csv(environment_verdict_path, environment_verdicts)
    write_csv(scenario_verdict_path, scenario_verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "diagnostics": diagnostics,
                "policy_summary": [asdict(row) for row in policy_results],
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
    return 0 if all(row.supports_delayed_return_precursor for row in scenario_verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
