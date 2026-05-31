#!/usr/bin/env python3
"""Heterogeneous learner precursor for the selfhood attractor test.

This experiment asks whether several different small learner families converge
on the same causal abstraction from raw outcome streams. Learners receive no
labels such as self, world, body, ownership, or identity. They only observe
which calibration actions succeeded and learn how that evidence should affect
later control contexts.

The result is intentionally still a precursor, not the full Attractor Test. The
learners are simple and the environment family is compact. The stronger point is
that the same analysis is applied across different update rules:

- Bayesian shared-state filtering.
- Predictive-state table lookup.
- Recurrent error-state update.
- Evolutionary rule search.
- Bottleneck clustering over outcome vectors.

A learned latent only counts as self-equivalent if it has an agent-bounded
causal signature. Shared transfer alone can also be world-state.
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


ARTIFACT_DIR = Path("artifacts")
EPS = 1e-12


@dataclass(frozen=True)
class ContextProfile:
    name: str
    risky_success_reward: float
    risky_failure_reward: float
    safe_reward: float


CONTEXTS = [
    ContextProfile("goal", 24.0, -16.0, 8.0),
    ContextProfile("option", 34.0, -30.0, 14.0),
    ContextProfile("commitment", 22.0, -18.0, 12.0),
    ContextProfile("adaptation", 28.0, -22.0, 11.0),
    ContextProfile("prediction", 18.0, -14.0, 7.0),
    ContextProfile("arbitration", 26.0, -20.0, 10.0),
]


@dataclass(frozen=True)
class AttractorConfig:
    episodes: int = 500
    training_episodes: int = 600
    seed: int = 20260601
    calibration_contexts: int = 2
    calibration_cost: float = 1.0
    local_probe_cost: float = 1.0
    evolutionary_candidates: int = 600


@dataclass(frozen=True)
class AttractorScenario:
    name: str
    mode: str


@dataclass(frozen=True)
class EpisodeState:
    scenario: str
    self_signal: bool
    world_signal: bool
    local_success: Dict[str, bool]


@dataclass(frozen=True)
class TrainingTrace:
    calibration: Tuple[bool, ...]
    outcomes: Dict[str, bool]


@dataclass
class LearnerResult:
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
    uses_calibration_rate: float


@dataclass
class ScenarioVerdict:
    scenario: str
    boundary_signature: str
    expected_convergence: str
    best_architecture: str
    best_architecture_reward: float
    marginal_reward: float
    local_probe_reward: float
    converged_architectures: int
    architecture_count: int
    architecture_signatures: str
    supports_attractor_precursor: bool


SCENARIOS = [
    AttractorScenario("self_shared_stream", "self_shared_stream"),
    AttractorScenario("world_shared_stream", "world_shared_stream"),
    AttractorScenario("independent_stream", "independent_stream"),
    AttractorScenario("irrelevant_stream", "irrelevant_stream"),
]


class StreamLearner:
    name = "base"
    family = "base"
    parameter_count = 0

    def fit(self, traces: Sequence[TrainingTrace], cfg: AttractorConfig) -> None:
        self.cfg = cfg
        self.marginal_success = mean_outcome_success(traces)
        self.no_hidden = self.marginal_success > 0.95

    def predict_success(self, calibration: Tuple[bool, ...], profile: ContextProfile) -> float:
        raise NotImplementedError

    def latent_value(self, calibration: Tuple[bool, ...]) -> float:
        raise NotImplementedError

    def uses_calibration(self, calibration: Tuple[bool, ...]) -> bool:
        return not getattr(self, "no_hidden", False)

    def memory_slots(self) -> int:
        return 0


class BayesianSharedFilter(StreamLearner):
    name = "bayesian_shared_filter"
    family = "bayesian"
    parameter_count = 2

    def predict_success(self, calibration: Tuple[bool, ...], profile: ContextProfile) -> float:
        if self.no_hidden:
            return self.marginal_success
        successes = sum(1 for outcome in calibration if outcome)
        return (successes + 1.0) / (len(calibration) + 2.0)

    def latent_value(self, calibration: Tuple[bool, ...]) -> float:
        return self.predict_success(calibration, CONTEXTS[-1])


class PredictiveStateTable(StreamLearner):
    name = "predictive_state_table"
    family = "predictive_state"
    parameter_count = 4

    def fit(self, traces: Sequence[TrainingTrace], cfg: AttractorConfig) -> None:
        super().fit(traces, cfg)
        self.table: Dict[Tuple[bool, ...], Dict[str, float]] = {}
        grouped: Dict[Tuple[bool, ...], List[TrainingTrace]] = {}
        for trace in traces:
            grouped.setdefault(trace.calibration, []).append(trace)
        for calibration, items in grouped.items():
            self.table[calibration] = {}
            for profile in CONTEXTS[cfg.calibration_contexts :]:
                successes = sum(1 for item in items if item.outcomes[profile.name])
                self.table[calibration][profile.name] = (successes + 1.0) / (len(items) + 2.0)
        latent_values = [
            statistics.fmean(values.values())
            for values in self.table.values()
            if values
        ]
        self.calibration_sensitive = sample_std(latent_values) > 0.05

    def predict_success(self, calibration: Tuple[bool, ...], profile: ContextProfile) -> float:
        if self.no_hidden:
            return self.marginal_success
        return self.table.get(calibration, {}).get(profile.name, self.marginal_success)

    def latent_value(self, calibration: Tuple[bool, ...]) -> float:
        if self.no_hidden:
            return self.marginal_success
        values = self.table.get(calibration)
        if not values:
            return self.marginal_success
        return statistics.fmean(values.values())

    def memory_slots(self) -> int:
        return len(self.table)

    def uses_calibration(self, calibration: Tuple[bool, ...]) -> bool:
        return not self.no_hidden and self.calibration_sensitive


class RecurrentErrorState(StreamLearner):
    name = "recurrent_error_state"
    family = "recurrent"
    parameter_count = 3

    def fit(self, traces: Sequence[TrainingTrace], cfg: AttractorConfig) -> None:
        super().fit(traces, cfg)
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
                    traces,
                    cfg,
                    lambda calibration, profile, s=self.start, a=step, l=leak: sigmoid(
                        recurrent_latent(calibration, s, a, l)
                    ),
                    uses_calibration=abs(step) > EPS,
                )
                if score > best_score:
                    best_score = score
                    best_params = (self.start, step, leak)
        self.start, self.step, self.leak = best_params

    def predict_success(self, calibration: Tuple[bool, ...], profile: ContextProfile) -> float:
        if self.no_hidden:
            return self.marginal_success
        return sigmoid(self.latent_value(calibration))

    def latent_value(self, calibration: Tuple[bool, ...]) -> float:
        if self.no_hidden:
            return logit(clamp_probability(self.marginal_success))
        return recurrent_latent(calibration, self.start, self.step, self.leak)

    def uses_calibration(self, calibration: Tuple[bool, ...]) -> bool:
        return not self.no_hidden and abs(self.step) > EPS


class EvolvedRuleController(StreamLearner):
    name = "evolved_rule_controller"
    family = "evolutionary"
    parameter_count = 4

    def fit(self, traces: Sequence[TrainingTrace], cfg: AttractorConfig) -> None:
        super().fit(traces, cfg)
        self.weights = (logit(clamp_probability(self.marginal_success)), 0.0, 0.0, 0.0)
        if self.no_hidden:
            return
        rng = random.Random(cfg.seed + 7919)
        candidates = [
            self.weights,
            (-1.0, 2.0, -2.0, 0.0),
            (-0.5, 1.7, -1.7, 0.4),
            (0.0, 1.4, -1.4, 0.8),
            (logit(clamp_probability(self.marginal_success)), 0.0, 0.0, 0.0),
        ]
        for _ in range(cfg.evolutionary_candidates):
            candidates.append(
                (
                    rng.uniform(-2.5, 2.5),
                    rng.uniform(-3.0, 3.0),
                    rng.uniform(-3.0, 3.0),
                    rng.uniform(-1.5, 1.5),
                )
            )

        best_score = -float("inf")
        best_weights = self.weights
        for weights in candidates:
            score = score_predictor(
                traces,
                cfg,
                lambda calibration, profile, w=weights: sigmoid(rule_score(calibration, w)),
                uses_calibration=any(abs(weight) > EPS for weight in weights[1:]),
            )
            if score > best_score:
                best_score = score
                best_weights = weights
        self.weights = best_weights

    def predict_success(self, calibration: Tuple[bool, ...], profile: ContextProfile) -> float:
        if self.no_hidden:
            return self.marginal_success
        return sigmoid(self.latent_value(calibration))

    def latent_value(self, calibration: Tuple[bool, ...]) -> float:
        if self.no_hidden:
            return logit(clamp_probability(self.marginal_success))
        return rule_score(calibration, self.weights)

    def uses_calibration(self, calibration: Tuple[bool, ...]) -> bool:
        return not self.no_hidden and any(abs(weight) > EPS for weight in self.weights[1:])


class BottleneckClusterModel(StreamLearner):
    name = "bottleneck_cluster_model"
    family = "bottleneck_world_model"
    parameter_count = 12

    def fit(self, traces: Sequence[TrainingTrace], cfg: AttractorConfig) -> None:
        super().fit(traces, cfg)
        self.context_names = [profile.name for profile in CONTEXTS]
        self.centroids: List[List[float]] = []
        if self.no_hidden:
            return
        vectors = [
            [1.0 if trace.outcomes[name] else 0.0 for name in self.context_names]
            for trace in traces
        ]
        low = min(vectors, key=sum)
        high = max(vectors, key=sum)
        self.centroids = [low[:], high[:]]
        for _ in range(8):
            groups = [[], []]
            for vector in vectors:
                index = nearest_centroid(vector, self.centroids, len(self.context_names))
                groups[index].append(vector)
            for index, group in enumerate(groups):
                if not group:
                    continue
                self.centroids[index] = [
                    statistics.fmean(vector[position] for vector in group)
                    for position in range(len(self.context_names))
                ]
        control_indices = range(cfg.calibration_contexts, len(self.context_names))
        cluster_values = [
            statistics.fmean(centroid[index] for index in control_indices)
            for centroid in self.centroids
        ]
        self.calibration_sensitive = sample_std(cluster_values) > 0.05

    def predict_success(self, calibration: Tuple[bool, ...], profile: ContextProfile) -> float:
        if self.no_hidden:
            return self.marginal_success
        cluster = self._cluster_from_calibration(calibration)
        if cluster is None:
            return self.marginal_success
        index = self.context_names.index(profile.name)
        return clamp_probability(self.centroids[cluster][index])

    def latent_value(self, calibration: Tuple[bool, ...]) -> float:
        if self.no_hidden:
            return self.marginal_success
        cluster = self._cluster_from_calibration(calibration)
        if cluster is None:
            return self.marginal_success
        control_indices = range(self.cfg.calibration_contexts, len(self.context_names))
        return statistics.fmean(self.centroids[cluster][index] for index in control_indices)

    def _cluster_from_calibration(self, calibration: Tuple[bool, ...]) -> Optional[int]:
        if not self.centroids:
            return None
        vector = [1.0 if outcome else 0.0 for outcome in calibration]
        distances = []
        for centroid in self.centroids:
            distances.append(sum(abs(vector[index] - centroid[index]) for index in range(len(vector))))
        return min(range(len(distances)), key=lambda index: (distances[index], index))

    def memory_slots(self) -> int:
        return len(self.centroids)

    def uses_calibration(self, calibration: Tuple[bool, ...]) -> bool:
        return not self.no_hidden and self.calibration_sensitive


LEARNER_TYPES = [
    BayesianSharedFilter,
    PredictiveStateTable,
    RecurrentErrorState,
    EvolvedRuleController,
    BottleneckClusterModel,
]


def stable_state_seed(seed: int, scenario: str, episode: int) -> int:
    value = seed + episode * 1009
    for char in scenario:
        value = (value * 131 + ord(char)) % (2**32)
    return value


def sample_state(scenario: AttractorScenario, episode: int, cfg: AttractorConfig) -> EpisodeState:
    rng = random.Random(stable_state_seed(cfg.seed, scenario.name, episode))
    if scenario.mode == "self_shared_stream":
        capability = rng.random() < 0.55
        diagnostic_world = rng.random() < 0.55
        return EpisodeState(
            scenario=scenario.name,
            self_signal=capability,
            world_signal=diagnostic_world,
            local_success={profile.name: capability for profile in CONTEXTS},
        )
    if scenario.mode == "world_shared_stream":
        diagnostic_self = rng.random() < 0.55
        gate = rng.random() < 0.55
        return EpisodeState(
            scenario=scenario.name,
            self_signal=diagnostic_self,
            world_signal=gate,
            local_success={profile.name: gate for profile in CONTEXTS},
        )
    if scenario.mode == "independent_stream":
        return EpisodeState(
            scenario=scenario.name,
            self_signal=rng.random() < 0.55,
            world_signal=rng.random() < 0.55,
            local_success={profile.name: rng.random() < 0.55 for profile in CONTEXTS},
        )
    if scenario.mode == "irrelevant_stream":
        return EpisodeState(
            scenario=scenario.name,
            self_signal=rng.random() < 0.55,
            world_signal=rng.random() < 0.55,
            local_success={profile.name: True for profile in CONTEXTS},
        )
    raise ValueError(f"unknown scenario mode: {scenario.mode}")


def make_training_traces(scenario: AttractorScenario, cfg: AttractorConfig) -> List[TrainingTrace]:
    traces = []
    for episode in range(cfg.training_episodes):
        state = sample_state(scenario, episode, cfg)
        calibration = tuple(
            state.local_success[profile.name]
            for profile in CONTEXTS[: cfg.calibration_contexts]
        )
        traces.append(TrainingTrace(calibration=calibration, outcomes=state.local_success))
    return traces


def boundary_signature(scenario: AttractorScenario, cfg: AttractorConfig) -> Tuple[str, float, float]:
    states = [
        sample_state(scenario, episode + cfg.training_episodes, cfg)
        for episode in range(cfg.training_episodes)
    ]
    effect_a_values = []
    effect_b_values = []
    for state in states:
        before = success_rate(state.local_success)
        after_a = success_rate(intervene_a(scenario, state).local_success)
        after_b = success_rate(intervene_b(scenario, state).local_success)
        effect_a_values.append(after_a - before)
        effect_b_values.append(after_b - before)
    effect_a = statistics.fmean(effect_a_values)
    effect_b = statistics.fmean(effect_b_values)
    if effect_a > 0.20 and effect_b < 0.05:
        return "agent_bounded_stream", effect_a, effect_b
    if effect_b > 0.20 and effect_a < 0.05:
        return "external_stream", effect_a, effect_b
    return "no_shared_agent_boundary", effect_a, effect_b


def intervene_a(scenario: AttractorScenario, state: EpisodeState) -> EpisodeState:
    if scenario.mode == "self_shared_stream":
        return EpisodeState(
            scenario=state.scenario,
            self_signal=True,
            world_signal=state.world_signal,
            local_success={profile.name: True for profile in CONTEXTS},
        )
    return state


def intervene_b(scenario: AttractorScenario, state: EpisodeState) -> EpisodeState:
    if scenario.mode == "world_shared_stream":
        return EpisodeState(
            scenario=state.scenario,
            self_signal=state.self_signal,
            world_signal=True,
            local_success={profile.name: True for profile in CONTEXTS},
        )
    return state


def evaluate_learner(
    scenario: AttractorScenario,
    learner: StreamLearner,
    cfg: AttractorConfig,
    signature: str,
) -> LearnerResult:
    total_reward = 0.0
    risky_count = 0
    safe_count = 0
    failed_risky_count = 0
    risky_success_count = 0
    calibration_uses = 0
    latents = []
    self_labels = []
    world_labels = []
    control_labels = []

    for episode in range(cfg.episodes):
        state = sample_state(scenario, episode + cfg.training_episodes * 3, cfg)
        calibration = tuple(
            state.local_success[profile.name]
            for profile in CONTEXTS[: cfg.calibration_contexts]
        )
        if learner.uses_calibration(calibration):
            total_reward -= cfg.calibration_cost
            calibration_uses += 1
        latents.append(learner.latent_value(calibration))
        self_labels.append(state.self_signal)
        world_labels.append(state.world_signal)
        control_labels.append(majority_success(state.local_success, cfg.calibration_contexts))

        for profile in CONTEXTS[cfg.calibration_contexts :]:
            predicted_success = learner.predict_success(calibration, profile)
            if should_risk(profile, predicted_success):
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
        uses_calibration_rate=calibration_uses / cfg.episodes,
    )


def evaluate_baseline(
    scenario: AttractorScenario,
    cfg: AttractorConfig,
    baseline: str,
    signature: str,
) -> LearnerResult:
    total_reward = 0.0
    risky_count = 0
    safe_count = 0
    failed_risky_count = 0
    risky_success_count = 0
    calibration_uses = 0
    traces = make_training_traces(scenario, cfg)
    marginal_success = mean_outcome_success(traces)

    for episode in range(cfg.episodes):
        state = sample_state(scenario, episode + cfg.training_episodes * 3, cfg)
        if baseline == "calibration_memory_no_transfer":
            total_reward -= cfg.calibration_cost
            calibration_uses += 1
        for profile in CONTEXTS[cfg.calibration_contexts :]:
            if baseline == "marginal_no_memory":
                choice = "risky" if should_risk(profile, marginal_success) else "safe"
            elif baseline == "calibration_memory_no_transfer":
                choice = "risky" if should_risk(profile, marginal_success) else "safe"
            elif baseline == "task_local_probe":
                total_reward -= cfg.local_probe_cost
                choice = "risky" if state.local_success[profile.name] else "safe"
            elif baseline == "oracle":
                choice = "risky" if state.local_success[profile.name] else "safe"
            else:
                raise ValueError(f"unknown baseline: {baseline}")

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

    return LearnerResult(
        scenario=scenario.name,
        learner=baseline,
        family="baseline",
        boundary_signature=signature,
        latent_signature="baseline",
        total_reward=total_reward,
        mean_reward=total_reward / cfg.episodes,
        risky_count=risky_count,
        safe_count=safe_count,
        failed_risky_count=failed_risky_count,
        success_rate=(risky_success_count / risky_count) if risky_count else 0.0,
        latent_mean=0.0,
        latent_std=0.0,
        latent_self_accuracy=0.5,
        latent_world_accuracy=0.5,
        latent_control_accuracy=0.5,
        parameter_count=0,
        memory_slots=0,
        uses_calibration_rate=calibration_uses / cfg.episodes,
    )


def classify_latent_signature(
    scenario: AttractorScenario,
    boundary: str,
    latent_std: float,
    self_accuracy: float,
    world_accuracy: float,
    control_accuracy: float,
) -> str:
    if scenario.mode == "irrelevant_stream" and latent_std < 0.05:
        return "no_hidden_needed"
    if boundary == "agent_bounded_stream" and self_accuracy >= 0.80 and world_accuracy < 0.70:
        return "agent_bounded_candidate"
    if boundary == "external_stream" and world_accuracy >= 0.80 and self_accuracy < 0.70:
        return "external_candidate"
    if control_accuracy >= 0.80 and latent_std >= 0.05:
        return "unbounded_transfer_candidate"
    if boundary == "no_shared_agent_boundary":
        return "no_shared_agent_boundary"
    if latent_std < 0.05:
        return "no_transfer_latent"
    return "task_or_noise_latent"


def build_verdicts(results: Sequence[LearnerResult], cfg: AttractorConfig) -> List[ScenarioVerdict]:
    verdicts = []
    for scenario in SCENARIOS:
        rows = [row for row in results if row.scenario == scenario.name]
        architecture_rows = [row for row in rows if row.family != "baseline"]
        best_architecture = max(architecture_rows, key=lambda row: row.total_reward)
        marginal = next(row for row in rows if row.learner == "marginal_no_memory")
        local_probe = next(row for row in rows if row.learner == "task_local_probe")
        expected = expected_convergence(scenario)
        converged = sum(1 for row in architecture_rows if row.latent_signature == expected)
        signatures = ";".join(f"{row.learner}:{row.latent_signature}" for row in architecture_rows)
        supports = supports_scenario(
            scenario=scenario,
            expected=expected,
            converged=converged,
            architecture_count=len(architecture_rows),
            best_architecture=best_architecture,
            marginal=marginal,
            local_probe=local_probe,
        )
        verdicts.append(
            ScenarioVerdict(
                scenario=scenario.name,
                boundary_signature=rows[0].boundary_signature,
                expected_convergence=expected,
                best_architecture=best_architecture.learner,
                best_architecture_reward=best_architecture.total_reward,
                marginal_reward=marginal.total_reward,
                local_probe_reward=local_probe.total_reward,
                converged_architectures=converged,
                architecture_count=len(architecture_rows),
                architecture_signatures=signatures,
                supports_attractor_precursor=supports,
            )
        )
    return verdicts


def expected_convergence(scenario: AttractorScenario) -> str:
    if scenario.mode == "self_shared_stream":
        return "agent_bounded_candidate"
    if scenario.mode == "world_shared_stream":
        return "external_candidate"
    if scenario.mode == "irrelevant_stream":
        return "no_hidden_needed"
    return "no_shared_agent_boundary"


def supports_scenario(
    scenario: AttractorScenario,
    expected: str,
    converged: int,
    architecture_count: int,
    best_architecture: LearnerResult,
    marginal: LearnerResult,
    local_probe: LearnerResult,
) -> bool:
    majority = converged >= max(3, math.ceil(architecture_count * 0.6))
    if scenario.mode in {"self_shared_stream", "world_shared_stream"}:
        return majority and best_architecture.total_reward > local_probe.total_reward + 1.0
    if scenario.mode == "independent_stream":
        return majority and local_probe.total_reward > best_architecture.total_reward + 10.0
    if scenario.mode == "irrelevant_stream":
        return majority and marginal.total_reward >= best_architecture.total_reward - EPS
    return False


def run_experiment(cfg: AttractorConfig) -> Tuple[List[LearnerResult], List[ScenarioVerdict], Dict[str, object]]:
    results: List[LearnerResult] = []
    diagnostics: Dict[str, object] = {}
    for scenario in SCENARIOS:
        traces = make_training_traces(scenario, cfg)
        signature, effect_a, effect_b = boundary_signature(scenario, cfg)
        diagnostics[scenario.name] = {
            "boundary_signature": signature,
            "intervention_a_effect": effect_a,
            "intervention_b_effect": effect_b,
            "training_marginal_success": mean_outcome_success(traces),
        }
        for learner_type in LEARNER_TYPES:
            learner = learner_type()
            learner.fit(traces, cfg)
            results.append(evaluate_learner(scenario, learner, cfg, signature))
        for baseline in ["marginal_no_memory", "calibration_memory_no_transfer", "task_local_probe", "oracle"]:
            results.append(evaluate_baseline(scenario, cfg, baseline, signature))
    verdicts = build_verdicts(results, cfg)
    return results, verdicts, diagnostics


def score_predictor(
    traces: Sequence[TrainingTrace],
    cfg: AttractorConfig,
    predictor,
    uses_calibration: bool = True,
) -> float:
    score = 0.0
    for trace in traces:
        if uses_calibration:
            score -= cfg.calibration_cost
        for profile in CONTEXTS[cfg.calibration_contexts :]:
            predicted = predictor(trace.calibration, profile)
            if should_risk(profile, predicted):
                score += (
                    profile.risky_success_reward
                    if trace.outcomes[profile.name]
                    else profile.risky_failure_reward
                )
            else:
                score += profile.safe_reward
    return score / len(traces)


def mean_outcome_success(traces: Sequence[TrainingTrace]) -> float:
    values = [
        1.0 if trace.outcomes[profile.name] else 0.0
        for trace in traces
        for profile in CONTEXTS
    ]
    return statistics.fmean(values)


def should_risk(profile: ContextProfile, success_probability: float) -> bool:
    risky_value = (
        success_probability * profile.risky_success_reward
        + (1.0 - success_probability) * profile.risky_failure_reward
    )
    return risky_value >= profile.safe_reward


def success_rate(local_success: Dict[str, bool]) -> float:
    return sum(1 for value in local_success.values() if value) / len(local_success)


def majority_success(local_success: Dict[str, bool], calibration_contexts: int) -> bool:
    values = [
        local_success[profile.name]
        for profile in CONTEXTS[calibration_contexts:]
    ]
    return sum(1 for value in values if value) >= math.ceil(len(values) / 2)


def threshold_accuracy(values: Sequence[float], labels: Sequence[bool]) -> float:
    if not values:
        return 0.5
    if all(label == labels[0] for label in labels):
        return 0.5
    unique_values = sorted(set(values))
    thresholds = [unique_values[0] - EPS, unique_values[-1] + EPS]
    thresholds.extend(
        (left + right) / 2.0
        for left, right in zip(unique_values, unique_values[1:])
    )
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


def recurrent_latent(calibration: Tuple[bool, ...], start: float, step: float, leak: float) -> float:
    value = start
    for outcome in calibration:
        error_direction = 1.0 if outcome else -1.0
        value = leak * value + step * error_direction
    return value


def rule_score(calibration: Tuple[bool, ...], weights: Tuple[float, float, float, float]) -> float:
    intercept, success_weight, failure_weight, agreement_weight = weights
    successes = sum(1 for outcome in calibration if outcome)
    failures = len(calibration) - successes
    agreement = 1.0 if successes in {0, len(calibration)} else 0.0
    return intercept + success_weight * successes + failure_weight * failures + agreement_weight * agreement


def nearest_centroid(vector: Sequence[float], centroids: Sequence[Sequence[float]], width: int) -> int:
    distances = []
    for centroid in centroids:
        distances.append(sum(abs(vector[index] - centroid[index]) for index in range(width)))
    return min(range(len(distances)), key=lambda index: (distances[index], index))


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
        "boundary_signature",
        "expected_convergence",
        "best_architecture",
        "converged_architectures",
        "best_architecture_reward",
        "local_probe_reward",
        "supports_attractor_precursor",
    ]
    rows = []
    for verdict in verdicts:
        rows.append(
            [
                verdict.scenario,
                verdict.boundary_signature,
                verdict.expected_convergence,
                verdict.best_architecture,
                f"{verdict.converged_architectures}/{verdict.architecture_count}",
                f"{verdict.best_architecture_reward:.3f}",
                f"{verdict.local_probe_reward:.3f}",
                str(verdict.supports_attractor_precursor),
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


def parse_args() -> AttractorConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=500)
    parser.add_argument("--training-episodes", type=int, default=600)
    parser.add_argument("--seed", type=int, default=20260601)
    parser.add_argument("--calibration-contexts", type=int, default=2)
    parser.add_argument("--calibration-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    parser.add_argument("--evolutionary-candidates", type=int, default=600)
    args = parser.parse_args()
    if args.calibration_contexts < 1 or args.calibration_contexts >= len(CONTEXTS):
        raise SystemExit("--calibration-contexts must leave at least one held-out context")
    return AttractorConfig(
        episodes=args.episodes,
        training_episodes=args.training_episodes,
        seed=args.seed,
        calibration_contexts=args.calibration_contexts,
        calibration_cost=args.calibration_cost,
        local_probe_cost=args.local_probe_cost,
        evolutionary_candidates=args.evolutionary_candidates,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    results, verdicts, diagnostics = run_experiment(cfg)

    summary_path = ARTIFACT_DIR / "heterogeneous_attractor_precursor_summary.csv"
    verdict_path = ARTIFACT_DIR / "heterogeneous_attractor_precursor_verdict.csv"
    results_path = ARTIFACT_DIR / "heterogeneous_attractor_precursor_results.json"
    write_csv(summary_path, results)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "diagnostics": diagnostics,
                "summary": [asdict(row) for row in results],
                "verdict": [asdict(row) for row in verdicts],
            },
            handle,
            indent=2,
        )
        handle.write("\n")

    print(f"wrote {summary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print_table(verdicts)
    return 0 if all(verdict.supports_attractor_precursor for verdict in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
