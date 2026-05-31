#!/usr/bin/env python3
"""Raw action-observation-reward history precursor.

Earlier attractor precursors gave learners compact calibration outcomes. This
test gives learners only raw reward traces from probe and risky actions:

- context id;
- action type;
- reward value.

The learners receive no self/world labels and no direct hidden-state labels.
They must learn whether early probe rewards predict held-out control rewards.
The boundary test still decides whether a converged latent is agent-bounded,
external, local-only, or unnecessary.
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
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

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
class RawHistoryConfig:
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
class RawTrace:
    probe_rewards: Tuple[float, ...]
    control_rewards: Dict[str, float]
    self_signal: bool
    world_signal: bool


@dataclass
class LearnerResult:
    environment: str
    surface: str
    scenario: str
    learner: str
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
    converged_learners: int
    learner_count: int
    best_learner: str
    best_learner_reward: float
    marginal_reward: float
    local_probe_reward: float
    learner_signatures: str
    supports_raw_history_precursor: bool


@dataclass
class ScenarioVerdict:
    scenario: str
    expected_signature: str
    supporting_environments: int
    environment_count: int
    mean_best_learner_reward: float
    mean_local_probe_reward: float
    mean_marginal_reward: float
    environment_signatures: str
    supports_raw_history_precursor: bool


class RawHistoryLearner:
    name = "base"
    family = "base"
    parameter_count = 0

    def fit(
        self,
        traces: Sequence[RawTrace],
        environment: EnvironmentFamily,
        cfg: RawHistoryConfig,
    ) -> None:
        self.environment = environment
        self.cfg = cfg
        self.marginal_success = mean_control_success(traces)
        self.no_hidden = self.marginal_success > 0.95

    def predict_success(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> float:
        raise NotImplementedError

    def latent_value(self, probe_rewards: Tuple[float, ...]) -> float:
        raise NotImplementedError

    def uses_probe_history(self, probe_rewards: Tuple[float, ...]) -> bool:
        return not getattr(self, "no_hidden", False)

    def memory_slots(self) -> int:
        return 0


class RewardSignFilter(RawHistoryLearner):
    name = "reward_sign_filter"
    family = "bayesian_raw_reward"
    parameter_count = 2

    def predict_success(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> float:
        if self.no_hidden:
            return self.marginal_success
        successes = sum(1 for reward in probe_rewards if reward > 0.0)
        return (successes + 1.0) / (len(probe_rewards) + 2.0)

    def latent_value(self, probe_rewards: Tuple[float, ...]) -> float:
        return self.predict_success(probe_rewards, self.environment.contexts[-1])


class RawSequenceTable(RawHistoryLearner):
    name = "raw_sequence_table"
    family = "table_raw_reward"
    parameter_count = 4

    def fit(
        self,
        traces: Sequence[RawTrace],
        environment: EnvironmentFamily,
        cfg: RawHistoryConfig,
    ) -> None:
        super().fit(traces, environment, cfg)
        self.table: Dict[Tuple[int, ...], Dict[str, float]] = {}
        grouped: Dict[Tuple[int, ...], List[RawTrace]] = {}
        for trace in traces:
            grouped.setdefault(reward_key(trace.probe_rewards), []).append(trace)
        for key, items in grouped.items():
            self.table[key] = {}
            for profile in environment.contexts[cfg.calibration_contexts :]:
                successes = sum(1 for item in items if item.control_rewards[profile.name] > 0.0)
                self.table[key][profile.name] = (successes + 1.0) / (len(items) + 2.0)
        latent_values = [
            statistics.fmean(values.values())
            for values in self.table.values()
            if values
        ]
        self.probe_sensitive = sample_std(latent_values) > 0.05

    def predict_success(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> float:
        if self.no_hidden:
            return self.marginal_success
        return self.table.get(reward_key(probe_rewards), {}).get(profile.name, self.marginal_success)

    def latent_value(self, probe_rewards: Tuple[float, ...]) -> float:
        if self.no_hidden:
            return self.marginal_success
        values = self.table.get(reward_key(probe_rewards))
        if not values:
            return self.marginal_success
        return statistics.fmean(values.values())

    def uses_probe_history(self, probe_rewards: Tuple[float, ...]) -> bool:
        return not self.no_hidden and self.probe_sensitive

    def memory_slots(self) -> int:
        return len(self.table)


class RecurrentRewardState(RawHistoryLearner):
    name = "recurrent_reward_state"
    family = "recurrent_raw_reward"
    parameter_count = 3

    def fit(
        self,
        traces: Sequence[RawTrace],
        environment: EnvironmentFamily,
        cfg: RawHistoryConfig,
    ) -> None:
        super().fit(traces, environment, cfg)
        self.start = logit(clamp_probability(self.marginal_success))
        self.step = 0.0
        self.leak = 0.0
        if self.no_hidden:
            return
        best_score = -float("inf")
        best_params = (self.start, 0.0, 0.0)
        for step in [0.0, 0.6, 1.0, 1.6, 2.2, 2.8]:
            for leak in [0.0, 0.35, 0.7, 1.0]:
                score = score_predictor(
                    traces=traces,
                    environment=environment,
                    cfg=cfg,
                    predictor=lambda rewards, profile, s=self.start, a=step, l=leak: sigmoid(
                        recurrent_latent(rewards, s, a, l)
                    ),
                    uses_probe=abs(step) > EPS,
                )
                if score > best_score:
                    best_score = score
                    best_params = (self.start, step, leak)
        self.start, self.step, self.leak = best_params

    def predict_success(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> float:
        if self.no_hidden:
            return self.marginal_success
        return sigmoid(self.latent_value(probe_rewards))

    def latent_value(self, probe_rewards: Tuple[float, ...]) -> float:
        if self.no_hidden:
            return logit(clamp_probability(self.marginal_success))
        return recurrent_latent(probe_rewards, self.start, self.step, self.leak)

    def uses_probe_history(self, probe_rewards: Tuple[float, ...]) -> bool:
        return not self.no_hidden and abs(self.step) > EPS


class EvolvedRewardRule(RawHistoryLearner):
    name = "evolved_reward_rule"
    family = "evolutionary_raw_reward"
    parameter_count = 5

    def fit(
        self,
        traces: Sequence[RawTrace],
        environment: EnvironmentFamily,
        cfg: RawHistoryConfig,
    ) -> None:
        super().fit(traces, environment, cfg)
        self.weights = (logit(clamp_probability(self.marginal_success)), 0.0, 0.0, 0.0, 0.0)
        if self.no_hidden:
            return
        rng = random.Random(stable_name_seed(cfg.seed, environment.name, "raw_evolution"))
        candidates = [
            self.weights,
            (-1.0, 2.0, -2.0, 0.0, 0.0),
            (-0.5, 1.6, -1.6, 0.5, 0.2),
            (0.0, 1.4, -1.4, 0.8, 0.0),
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
        best_score = -float("inf")
        best_weights = self.weights
        for weights in candidates:
            score = score_predictor(
                traces=traces,
                environment=environment,
                cfg=cfg,
                predictor=lambda rewards, profile, w=weights: sigmoid(rule_score(rewards, w)),
                uses_probe=any(abs(weight) > EPS for weight in weights[1:]),
            )
            if score > best_score:
                best_score = score
                best_weights = weights
        self.weights = best_weights

    def predict_success(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> float:
        if self.no_hidden:
            return self.marginal_success
        return sigmoid(self.latent_value(probe_rewards))

    def latent_value(self, probe_rewards: Tuple[float, ...]) -> float:
        if self.no_hidden:
            return logit(clamp_probability(self.marginal_success))
        return rule_score(probe_rewards, self.weights)

    def uses_probe_history(self, probe_rewards: Tuple[float, ...]) -> bool:
        return not self.no_hidden and any(abs(weight) > EPS for weight in self.weights[1:])


class RewardBottleneckCluster(RawHistoryLearner):
    name = "reward_bottleneck_cluster"
    family = "bottleneck_raw_reward"
    parameter_count = 12

    def fit(
        self,
        traces: Sequence[RawTrace],
        environment: EnvironmentFamily,
        cfg: RawHistoryConfig,
    ) -> None:
        super().fit(traces, environment, cfg)
        self.context_names = [profile.name for profile in environment.contexts]
        self.centroids: List[List[float]] = []
        if self.no_hidden:
            self.probe_sensitive = False
            return
        vectors = [reward_vector(trace, environment, cfg) for trace in traces]
        low = min(vectors, key=sum)
        high = max(vectors, key=sum)
        self.centroids = [low[:], high[:]]
        for _ in range(8):
            groups = [[], []]
            for vector in vectors:
                index = nearest_centroid(vector, self.centroids, len(vector))
                groups[index].append(vector)
            for index, group in enumerate(groups):
                if not group:
                    continue
                self.centroids[index] = [
                    statistics.fmean(vector[position] for vector in group)
                    for position in range(len(group[0]))
                ]
        control_indices = range(cfg.calibration_contexts, len(environment.contexts))
        cluster_values = [
            statistics.fmean(centroid[index] for index in control_indices)
            for centroid in self.centroids
        ]
        self.probe_sensitive = sample_std(cluster_values) > 0.05

    def predict_success(self, probe_rewards: Tuple[float, ...], profile: ContextProfile) -> float:
        if self.no_hidden:
            return self.marginal_success
        cluster = self._cluster_from_probe(probe_rewards)
        if cluster is None:
            return self.marginal_success
        index = self.context_names.index(profile.name)
        return clamp_probability(self.centroids[cluster][index])

    def latent_value(self, probe_rewards: Tuple[float, ...]) -> float:
        if self.no_hidden:
            return self.marginal_success
        cluster = self._cluster_from_probe(probe_rewards)
        if cluster is None:
            return self.marginal_success
        control_indices = range(self.cfg.calibration_contexts, len(self.context_names))
        return statistics.fmean(self.centroids[cluster][index] for index in control_indices)

    def _cluster_from_probe(self, probe_rewards: Tuple[float, ...]) -> Optional[int]:
        if not self.centroids:
            return None
        vector = [1.0 if reward > 0.0 else 0.0 for reward in probe_rewards]
        distances = []
        for centroid in self.centroids:
            distances.append(sum(abs(vector[index] - centroid[index]) for index in range(len(vector))))
        return min(range(len(distances)), key=lambda index: (distances[index], index))

    def uses_probe_history(self, probe_rewards: Tuple[float, ...]) -> bool:
        return not self.no_hidden and self.probe_sensitive

    def memory_slots(self) -> int:
        return len(self.centroids)


LEARNER_TYPES = [
    RewardSignFilter,
    RawSequenceTable,
    RecurrentRewardState,
    EvolvedRewardRule,
    RewardBottleneckCluster,
]


def as_cross_cfg(cfg: RawHistoryConfig) -> CrossEnvConfig:
    return CrossEnvConfig(
        episodes=cfg.episodes,
        training_episodes=cfg.training_episodes,
        seed=cfg.seed,
        calibration_contexts=cfg.calibration_contexts,
        calibration_cost=cfg.calibration_cost,
        local_probe_cost=cfg.local_probe_cost,
    )


def make_raw_traces(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    cfg: RawHistoryConfig,
) -> List[RawTrace]:
    cross_cfg = as_cross_cfg(cfg)
    traces = []
    for episode in range(cfg.training_episodes):
        state = sample_state(environment, scenario, episode, cross_cfg)
        probe_rewards = tuple(
            probe_reward(state.local_success[profile.name], cfg)
            for profile in environment.contexts[: cfg.calibration_contexts]
        )
        control_rewards = {
            profile.name: risky_reward(profile, state.local_success[profile.name])
            for profile in environment.contexts[cfg.calibration_contexts :]
        }
        traces.append(
            RawTrace(
                probe_rewards=probe_rewards,
                control_rewards=control_rewards,
                self_signal=state.self_signal,
                world_signal=state.world_signal,
            )
        )
    return traces


def evaluate_learner(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    learner: RawHistoryLearner,
    cfg: RawHistoryConfig,
    signature: str,
) -> LearnerResult:
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
        if learner.uses_probe_history(probe_rewards):
            total_reward -= cfg.calibration_cost
            probe_uses += 1
        latents.append(learner.latent_value(probe_rewards))
        self_labels.append(state.self_signal)
        world_labels.append(state.world_signal)
        control_labels.append(majority_control_success(state.local_success, environment, cfg))

        for profile in environment.contexts[cfg.calibration_contexts :]:
            predicted = learner.predict_success(probe_rewards, profile)
            if should_risk(profile, predicted):
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
    return LearnerResult(
        environment=environment.name,
        surface=environment.surface,
        scenario=scenario.name,
        learner=learner.name,
        family=learner.family,
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
        parameter_count=learner.parameter_count,
        memory_slots=learner.memory_slots(),
        uses_probe_rate=probe_uses / cfg.episodes,
    )


def evaluate_baseline(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    cfg: RawHistoryConfig,
    baseline: str,
) -> BaselineResult:
    cross_cfg = as_cross_cfg(cfg)
    traces = make_raw_traces(environment, scenario, cfg)
    marginal_success = mean_control_success(traces)
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
        return "unbounded_reward_history_candidate"
    return "task_or_noise_latent"


def build_environment_verdicts(
    learner_results: Sequence[LearnerResult],
    baseline_results: Sequence[BaselineResult],
) -> List[EnvironmentVerdict]:
    verdicts = []
    for environment in ENVIRONMENTS:
        for scenario in SCENARIOS:
            rows = [
                row
                for row in learner_results
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
                learner_count=len(rows),
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
                    converged_learners=converged,
                    learner_count=len(rows),
                    best_learner=best.learner,
                    best_learner_reward=best.total_reward,
                    marginal_reward=marginal.total_reward,
                    local_probe_reward=local.total_reward,
                    learner_signatures=signatures,
                    supports_raw_history_precursor=supports,
                )
            )
    return verdicts


def supports_environment(
    scenario: ScenarioSpec,
    converged: int,
    learner_count: int,
    best: LearnerResult,
    marginal: BaselineResult,
    local: BaselineResult,
) -> bool:
    majority = converged >= max(3, math.ceil(learner_count * 0.6))
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
        supporting = sum(1 for row in rows if row.supports_raw_history_precursor)
        signatures = ";".join(
            f"{row.environment}:{row.converged_learners}/{row.learner_count}:{row.expected_signature}"
            for row in rows
        )
        verdicts.append(
            ScenarioVerdict(
                scenario=scenario.name,
                expected_signature=expected_signature(scenario),
                supporting_environments=supporting,
                environment_count=len(rows),
                mean_best_learner_reward=statistics.fmean(row.best_learner_reward for row in rows),
                mean_local_probe_reward=statistics.fmean(row.local_probe_reward for row in rows),
                mean_marginal_reward=statistics.fmean(row.marginal_reward for row in rows),
                environment_signatures=signatures,
                supports_raw_history_precursor=supporting == len(rows),
            )
        )
    return verdicts


def run_experiment(
    cfg: RawHistoryConfig,
) -> Tuple[List[LearnerResult], List[BaselineResult], List[EnvironmentVerdict], List[ScenarioVerdict], Dict[str, object]]:
    learner_results: List[LearnerResult] = []
    baseline_results: List[BaselineResult] = []
    diagnostics: Dict[str, object] = {}
    cross_cfg = as_cross_cfg(cfg)
    for environment in ENVIRONMENTS:
        for scenario in SCENARIOS:
            traces = make_raw_traces(environment, scenario, cfg)
            signature, agent_effect, world_effect = boundary_signature(environment, scenario, cross_cfg)
            diagnostics[f"{environment.name}:{scenario.name}"] = {
                "boundary_signature": signature,
                "agent_intervention_effect": agent_effect,
                "world_intervention_effect": world_effect,
                "training_marginal_success": mean_control_success(traces),
            }
            for learner_type in LEARNER_TYPES:
                learner = learner_type()
                learner.fit(traces, environment, cfg)
                learner_results.append(evaluate_learner(environment, scenario, learner, cfg, signature))
            for baseline in ["marginal_no_memory", "probe_memory_no_transfer", "task_local_probe", "oracle"]:
                baseline_results.append(evaluate_baseline(environment, scenario, cfg, baseline))
    environment_verdicts = build_environment_verdicts(learner_results, baseline_results)
    scenario_verdicts = build_scenario_verdicts(environment_verdicts)
    return learner_results, baseline_results, environment_verdicts, scenario_verdicts, diagnostics


def score_predictor(
    traces: Sequence[RawTrace],
    environment: EnvironmentFamily,
    cfg: RawHistoryConfig,
    predictor,
    uses_probe: bool = True,
) -> float:
    score = 0.0
    for trace in traces:
        if uses_probe:
            score -= cfg.calibration_cost
        for profile in environment.contexts[cfg.calibration_contexts :]:
            predicted = predictor(trace.probe_rewards, profile)
            if should_risk(profile, predicted):
                score += trace.control_rewards[profile.name]
            else:
                score += profile.safe_reward
    return score / len(traces)


def probe_reward(success: bool, cfg: RawHistoryConfig) -> float:
    return cfg.probe_success_reward if success else cfg.probe_failure_reward


def risky_reward(profile: ContextProfile, success: bool) -> float:
    return profile.risky_success_reward if success else profile.risky_failure_reward


def mean_control_success(traces: Sequence[RawTrace]) -> float:
    return statistics.fmean(
        1.0 if reward > 0.0 else 0.0
        for trace in traces
        for reward in trace.control_rewards.values()
    )


def majority_control_success(
    local_success: Dict[str, bool],
    environment: EnvironmentFamily,
    cfg: RawHistoryConfig,
) -> bool:
    values = [
        local_success[profile.name]
        for profile in environment.contexts[cfg.calibration_contexts :]
    ]
    return sum(1 for value in values if value) >= math.ceil(len(values) / 2)


def reward_key(rewards: Tuple[float, ...]) -> Tuple[int, ...]:
    return tuple(1 if reward > 0.0 else 0 for reward in rewards)


def reward_vector(trace: RawTrace, environment: EnvironmentFamily, cfg: RawHistoryConfig) -> List[float]:
    values = [1.0 if reward > 0.0 else 0.0 for reward in trace.probe_rewards]
    values.extend(
        1.0 if trace.control_rewards[profile.name] > 0.0 else 0.0
        for profile in environment.contexts[cfg.calibration_contexts :]
    )
    return values


def recurrent_latent(probe_rewards: Tuple[float, ...], start: float, step: float, leak: float) -> float:
    value = start
    for reward in probe_rewards:
        value = leak * value + step * (1.0 if reward > 0.0 else -1.0)
    return value


def rule_score(probe_rewards: Tuple[float, ...], weights: Tuple[float, float, float, float, float]) -> float:
    intercept, positive_weight, negative_weight, agreement_weight, sum_weight = weights
    positives = sum(1 for reward in probe_rewards if reward > 0.0)
    negatives = len(probe_rewards) - positives
    agreement = 1.0 if positives in {0, len(probe_rewards)} else 0.0
    reward_sum = sum(probe_rewards)
    return (
        intercept
        + positive_weight * positives
        + negative_weight * negatives
        + agreement_weight * agreement
        + sum_weight * reward_sum
    )


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


def nearest_centroid(vector: Sequence[float], centroids: Sequence[Sequence[float]], width: int) -> int:
    distances = []
    for centroid in centroids:
        distances.append(sum(abs(vector[index] - centroid[index]) for index in range(width)))
    return min(range(len(distances)), key=lambda index: (distances[index], index))


def stable_name_seed(seed: int, left: str, right: str) -> int:
    value = seed
    for char in f"{left}:{right}":
        value = (value * 131 + ord(char)) % (2**32)
    return value


def clamp_probability(value: float) -> float:
    return min(1.0 - EPS, max(EPS, value))


def logit(value: float) -> float:
    value = clamp_probability(value)
    return math.log(value / (1.0 - value))


def sigmoid(value: float) -> float:
    if value >= 0.0:
        scale = math.exp(-value)
        return 1.0 / (1.0 + scale)
    scale = math.exp(value)
    return scale / (1.0 + scale)


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
        "mean_best_learner_reward",
        "mean_local_probe_reward",
        "supports_raw_history_precursor",
    ]
    rows = []
    for verdict in verdicts:
        rows.append(
            [
                verdict.scenario,
                verdict.expected_signature,
                f"{verdict.supporting_environments}/{verdict.environment_count}",
                f"{verdict.mean_best_learner_reward:.3f}",
                f"{verdict.mean_local_probe_reward:.3f}",
                str(verdict.supports_raw_history_precursor),
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


def parse_args() -> RawHistoryConfig:
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
    return RawHistoryConfig(
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
    learner_results, baseline_results, environment_verdicts, scenario_verdicts, diagnostics = run_experiment(cfg)

    summary_path = ARTIFACT_DIR / "raw_history_learning_summary.csv"
    baseline_path = ARTIFACT_DIR / "raw_history_learning_baselines.csv"
    environment_verdict_path = ARTIFACT_DIR / "raw_history_learning_environment_verdict.csv"
    scenario_verdict_path = ARTIFACT_DIR / "raw_history_learning_scenario_verdict.csv"
    results_path = ARTIFACT_DIR / "raw_history_learning_results.json"
    write_csv(summary_path, learner_results)
    write_csv(baseline_path, baseline_results)
    write_csv(environment_verdict_path, environment_verdicts)
    write_csv(scenario_verdict_path, scenario_verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "diagnostics": diagnostics,
                "learner_summary": [asdict(row) for row in learner_results],
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
    return 0 if all(row.supports_raw_history_precursor for row in scenario_verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
