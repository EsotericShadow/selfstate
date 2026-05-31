#!/usr/bin/env python3
"""Evolved recurrent policy precursor.

This is a bounded step beyond hand-enumerated delayed-return rules. Candidate
controllers are small continuous recurrent policies. They observe only early
probe rewards, update hidden state, then choose risky or safe actions in held-out
contexts. Parameters are selected by episode return.

The experiment still uses toy environments and evolutionary search, not deep RL.
Its purpose is to ask whether end-to-end recurrent memory states recover the
same agent/world/local/no-hidden boundary pattern.
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


ARTIFACT_DIR = Path("artifacts")
EPS = 1e-12


@dataclass(frozen=True)
class EvolvedRnnConfig:
    episodes: int = 500
    training_episodes: int = 500
    seed: int = 20260601
    calibration_contexts: int = 2
    calibration_cost: float = 1.0
    local_probe_cost: float = 1.0
    probe_success_reward: float = 1.0
    probe_failure_reward: float = -1.0
    random_candidates: int = 700


@dataclass(frozen=True)
class EpisodeTrace:
    probe_rewards: Tuple[float, ...]
    self_signal: bool
    world_signal: bool
    local_success: Dict[str, bool]


@dataclass(frozen=True)
class Candidate:
    architecture: str
    weights: Tuple[float, ...]
    uses_memory: bool


@dataclass
class PolicyResult:
    environment: str
    surface: str
    scenario: str
    architecture: str
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
    uses_probe_rate: float
    selected_weights: str


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
    converged_architectures: int
    architecture_count: int
    best_architecture: str
    best_architecture_reward: float
    marginal_reward: float
    local_probe_reward: float
    architecture_signatures: str
    supports_evolved_rnn_precursor: bool


@dataclass
class ScenarioVerdict:
    scenario: str
    expected_signature: str
    supporting_environments: int
    environment_count: int
    mean_best_architecture_reward: float
    mean_local_probe_reward: float
    mean_marginal_reward: float
    environment_signatures: str
    supports_evolved_rnn_precursor: bool


ARCHITECTURES = ["scalar_rnn", "gated_scalar_rnn", "two_unit_rnn"]


def as_cross_cfg(cfg: EvolvedRnnConfig) -> CrossEnvConfig:
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
    cfg: EvolvedRnnConfig,
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


def train_architecture(
    architecture: str,
    environment: EnvironmentFamily,
    traces: Sequence[EpisodeTrace],
    cfg: EvolvedRnnConfig,
) -> Candidate:
    rng = random.Random(stable_name_seed(cfg.seed, environment.name, architecture))
    candidates = seed_candidates(architecture)
    for _ in range(cfg.random_candidates):
        candidates.append(random_candidate(architecture, rng))
    return max(
        candidates,
        key=lambda candidate: score_candidate(candidate, environment, traces, cfg),
    )


def seed_candidates(architecture: str) -> List[Candidate]:
    if architecture == "scalar_rnn":
        return [
            Candidate(architecture, (0.0, 0.0, 0.0, -999.0), False),
            Candidate(architecture, (0.0, 0.0, 0.0, 999.0), False),
            Candidate(architecture, (0.0, 0.0, 2.0, 0.0), True),
            Candidate(architecture, (0.0, 0.4, 2.0, 0.6), True),
        ]
    if architecture == "gated_scalar_rnn":
        return [
            Candidate(architecture, (0.0, 0.0, 0.0, -999.0), False),
            Candidate(architecture, (0.0, 0.0, 0.0, 999.0), False),
            Candidate(architecture, (0.0, 0.1, 2.0, 0.0), True),
            Candidate(architecture, (0.0, 0.5, 2.0, 0.6), True),
        ]
    if architecture == "two_unit_rnn":
        return [
            Candidate(architecture, (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -999.0), False),
            Candidate(architecture, (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 999.0), False),
            Candidate(architecture, (0.0, 0.0, 2.0, 0.0, 0.0, -2.0, 0.0), True),
            Candidate(architecture, (0.0, 0.4, 2.0, 0.0, 0.2, -2.0, 0.5), True),
        ]
    raise ValueError(f"unknown architecture: {architecture}")


def random_candidate(architecture: str, rng: random.Random) -> Candidate:
    if architecture in {"scalar_rnn", "gated_scalar_rnn"}:
        weights = (
            rng.uniform(-1.5, 1.5),
            rng.uniform(-1.2, 1.2),
            rng.uniform(-3.0, 3.0),
            rng.uniform(-2.0, 2.0),
        )
        return Candidate(architecture, weights, abs(weights[2]) > EPS)
    if architecture == "two_unit_rnn":
        weights = (
            rng.uniform(-1.5, 1.5),
            rng.uniform(-1.2, 1.2),
            rng.uniform(-3.0, 3.0),
            rng.uniform(-1.5, 1.5),
            rng.uniform(-1.2, 1.2),
            rng.uniform(-3.0, 3.0),
            rng.uniform(-2.0, 2.0),
        )
        return Candidate(architecture, weights, abs(weights[2]) + abs(weights[5]) > EPS)
    raise ValueError(f"unknown architecture: {architecture}")


def score_candidate(
    candidate: Candidate,
    environment: EnvironmentFamily,
    traces: Sequence[EpisodeTrace],
    cfg: EvolvedRnnConfig,
) -> float:
    total = 0.0
    for trace in traces:
        hidden = run_recurrent_state(candidate, trace.probe_rewards)
        if candidate.uses_memory:
            total -= cfg.calibration_cost
        for profile in environment.contexts[cfg.calibration_contexts :]:
            choice = choose(candidate, hidden)
            if choice == "risky":
                total += risky_reward(profile, trace.local_success[profile.name])
            else:
                total += profile.safe_reward
    return total / len(traces)


def evaluate_candidate(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    candidate: Candidate,
    cfg: EvolvedRnnConfig,
    signature: str,
) -> PolicyResult:
    cross_cfg = as_cross_cfg(cfg)
    total_reward = 0.0
    risky_count = 0
    safe_count = 0
    failed_risky_count = 0
    risky_success_count = 0
    memory_uses = 0
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
        hidden = run_recurrent_state(candidate, probe_rewards)
        if candidate.uses_memory:
            total_reward -= cfg.calibration_cost
            memory_uses += 1
        latents.append(latent_value(candidate, hidden))
        self_labels.append(state.self_signal)
        world_labels.append(state.world_signal)
        control_labels.append(majority_control_success(state.local_success, environment, cfg))
        for profile in environment.contexts[cfg.calibration_contexts :]:
            choice = choose(candidate, hidden)
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
    signature_label = classify_latent_signature(
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
        architecture=candidate.architecture,
        boundary_signature=signature,
        latent_signature=signature_label,
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
        parameter_count=len(candidate.weights),
        uses_probe_rate=memory_uses / cfg.episodes,
        selected_weights=",".join(f"{weight:.3f}" for weight in candidate.weights),
    )


def evaluate_baseline(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    cfg: EvolvedRnnConfig,
    baseline: str,
) -> BaselineResult:
    cross_cfg = as_cross_cfg(cfg)
    traces = make_traces(environment, scenario, cfg)
    marginal_success = mean_success(traces, environment, cfg)
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


def run_recurrent_state(candidate: Candidate, probe_rewards: Tuple[float, ...]) -> Tuple[float, ...]:
    weights = candidate.weights
    if candidate.architecture == "scalar_rnn":
        bias, recurrent, input_weight, _threshold = weights
        hidden = 0.0
        for reward in probe_rewards:
            hidden = math.tanh(bias + recurrent * hidden + input_weight * reward)
        return (hidden,)
    if candidate.architecture == "gated_scalar_rnn":
        bias, retention, input_weight, _threshold = weights
        hidden = 0.0
        gate = sigmoid(retention)
        for reward in probe_rewards:
            proposal = math.tanh(bias + input_weight * reward)
            hidden = gate * hidden + (1.0 - gate) * proposal
        return (hidden,)
    if candidate.architecture == "two_unit_rnn":
        b1, r1, i1, b2, r2, i2, _threshold = weights
        h1 = 0.0
        h2 = 0.0
        for reward in probe_rewards:
            h1 = math.tanh(b1 + r1 * h1 + i1 * reward)
            h2 = math.tanh(b2 + r2 * h2 + i2 * reward)
        return (h1, h2)
    raise ValueError(f"unknown architecture: {candidate.architecture}")


def choose(candidate: Candidate, hidden: Tuple[float, ...]) -> str:
    threshold = candidate.weights[-1]
    value = latent_value(candidate, hidden)
    return "risky" if value >= threshold else "safe"


def latent_value(candidate: Candidate, hidden: Tuple[float, ...]) -> float:
    if candidate.architecture == "two_unit_rnn":
        return hidden[0] - hidden[1]
    return hidden[0]


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
        return "unbounded_recurrent_candidate"
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
            signatures = ";".join(f"{row.architecture}:{row.latent_signature}" for row in rows)
            supports = supports_environment(
                scenario=scenario,
                converged=converged,
                architecture_count=len(rows),
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
                    converged_architectures=converged,
                    architecture_count=len(rows),
                    best_architecture=best.architecture,
                    best_architecture_reward=best.total_reward,
                    marginal_reward=marginal.total_reward,
                    local_probe_reward=local.total_reward,
                    architecture_signatures=signatures,
                    supports_evolved_rnn_precursor=supports,
                )
            )
    return verdicts


def supports_environment(
    scenario: ScenarioSpec,
    converged: int,
    architecture_count: int,
    best: PolicyResult,
    marginal: BaselineResult,
    local: BaselineResult,
) -> bool:
    majority = converged >= max(2, math.ceil(architecture_count * 0.6))
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
        supporting = sum(1 for row in rows if row.supports_evolved_rnn_precursor)
        signatures = ";".join(
            f"{row.environment}:{row.converged_architectures}/{row.architecture_count}:{row.expected_signature}"
            for row in rows
        )
        verdicts.append(
            ScenarioVerdict(
                scenario=scenario.name,
                expected_signature=expected_signature(scenario),
                supporting_environments=supporting,
                environment_count=len(rows),
                mean_best_architecture_reward=statistics.fmean(row.best_architecture_reward for row in rows),
                mean_local_probe_reward=statistics.fmean(row.local_probe_reward for row in rows),
                mean_marginal_reward=statistics.fmean(row.marginal_reward for row in rows),
                environment_signatures=signatures,
                supports_evolved_rnn_precursor=supporting == len(rows),
            )
        )
    return verdicts


def run_experiment(
    cfg: EvolvedRnnConfig,
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
            for architecture in ARCHITECTURES:
                candidate = train_architecture(architecture, environment, traces, cfg)
                policy_results.append(evaluate_candidate(environment, scenario, candidate, cfg, signature))
            for baseline in ["marginal_no_memory", "task_local_probe", "oracle"]:
                baseline_results.append(evaluate_baseline(environment, scenario, cfg, baseline))
    environment_verdicts = build_environment_verdicts(policy_results, baseline_results)
    scenario_verdicts = build_scenario_verdicts(environment_verdicts)
    return policy_results, baseline_results, environment_verdicts, scenario_verdicts, diagnostics


def probe_reward(success: bool, cfg: EvolvedRnnConfig) -> float:
    return cfg.probe_success_reward if success else cfg.probe_failure_reward


def risky_reward(profile: ContextProfile, success: bool) -> float:
    return profile.risky_success_reward if success else profile.risky_failure_reward


def mean_success(
    traces: Sequence[EpisodeTrace],
    environment: EnvironmentFamily,
    cfg: EvolvedRnnConfig,
) -> float:
    return statistics.fmean(
        1.0 if trace.local_success[profile.name] else 0.0
        for trace in traces
        for profile in environment.contexts[cfg.calibration_contexts :]
    )


def majority_control_success(
    local_success: Dict[str, bool],
    environment: EnvironmentFamily,
    cfg: EvolvedRnnConfig,
) -> bool:
    values = [
        local_success[profile.name]
        for profile in environment.contexts[cfg.calibration_contexts :]
    ]
    return sum(1 for value in values if value) >= math.ceil(len(values) / 2)


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
        "mean_best_architecture_reward",
        "mean_local_probe_reward",
        "supports_evolved_rnn_precursor",
    ]
    rows = []
    for verdict in verdicts:
        rows.append(
            [
                verdict.scenario,
                verdict.expected_signature,
                f"{verdict.supporting_environments}/{verdict.environment_count}",
                f"{verdict.mean_best_architecture_reward:.3f}",
                f"{verdict.mean_local_probe_reward:.3f}",
                str(verdict.supports_evolved_rnn_precursor),
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


def parse_args() -> EvolvedRnnConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=500)
    parser.add_argument("--training-episodes", type=int, default=500)
    parser.add_argument("--seed", type=int, default=20260601)
    parser.add_argument("--calibration-contexts", type=int, default=2)
    parser.add_argument("--calibration-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    parser.add_argument("--probe-success-reward", type=float, default=1.0)
    parser.add_argument("--probe-failure-reward", type=float, default=-1.0)
    parser.add_argument("--random-candidates", type=int, default=700)
    args = parser.parse_args()
    if args.calibration_contexts < 1:
        raise SystemExit("--calibration-contexts must be at least 1")
    if any(args.calibration_contexts >= len(environment.contexts) for environment in ENVIRONMENTS):
        raise SystemExit("--calibration-contexts must leave held-out contexts")
    return EvolvedRnnConfig(
        episodes=args.episodes,
        training_episodes=args.training_episodes,
        seed=args.seed,
        calibration_contexts=args.calibration_contexts,
        calibration_cost=args.calibration_cost,
        local_probe_cost=args.local_probe_cost,
        probe_success_reward=args.probe_success_reward,
        probe_failure_reward=args.probe_failure_reward,
        random_candidates=args.random_candidates,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    policy_results, baseline_results, environment_verdicts, scenario_verdicts, diagnostics = run_experiment(cfg)

    summary_path = ARTIFACT_DIR / "evolved_recurrent_policy_summary.csv"
    baseline_path = ARTIFACT_DIR / "evolved_recurrent_policy_baselines.csv"
    environment_verdict_path = ARTIFACT_DIR / "evolved_recurrent_policy_environment_verdict.csv"
    scenario_verdict_path = ARTIFACT_DIR / "evolved_recurrent_policy_scenario_verdict.csv"
    results_path = ARTIFACT_DIR / "evolved_recurrent_policy_results.json"
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
    return 0 if all(row.supports_evolved_rnn_precursor for row in scenario_verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
