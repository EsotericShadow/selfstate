#!/usr/bin/env python3
"""Gradient-trained recurrent policy precursor.

This is a narrow step beyond evolved recurrent policies. Candidate controllers
are still tiny recurrent policies over early probe rewards, but their parameters
are optimized by finite-difference gradient ascent on differentiable expected
episode return rather than selected only by random/evolutionary search.

The test asks whether a return-gradient training method recovers the same
agent/world/local/no-hidden boundary pattern.
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
    CrossEnvConfig,
    EnvironmentFamily,
    ScenarioSpec,
    boundary_signature,
    expected_signature,
    sample_state,
)
from evolved_recurrent_policy import (
    ARCHITECTURES,
    BaselineResult,
    EpisodeTrace,
    classify_latent_signature,
    evaluate_baseline,
    majority_control_success,
    probe_reward,
    risky_reward,
    sample_std,
    sigmoid,
    threshold_accuracy,
)


ARTIFACT_DIR = Path("artifacts")
EPS = 1e-12
PRUNE_EPS = 1e-9


@dataclass(frozen=True)
class GradientRnnConfig:
    episodes: int = 500
    training_episodes: int = 500
    seed: int = 20260601
    calibration_contexts: int = 2
    calibration_cost: float = 1.0
    local_probe_cost: float = 1.0
    probe_success_reward: float = 1.0
    probe_failure_reward: float = -1.0
    candidates: int = 2
    gradient_steps: int = 20
    learning_rate: float = 0.35
    finite_diff_epsilon: float = 0.03
    policy_scale: float = 6.0
    memory_cost_scale: float = 12.0


@dataclass(frozen=True)
class GradientCandidate:
    architecture: str
    weights: Tuple[float, ...]
    uses_memory: bool
    training_return: float
    optimized_steps: int


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
    training_return: float
    optimized_steps: int
    selected_weights: str


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
    supports_gradient_rnn_precursor: bool


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
    supports_gradient_rnn_precursor: bool


def as_cross_cfg(cfg: GradientRnnConfig) -> CrossEnvConfig:
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
    cfg: GradientRnnConfig,
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
    cfg: GradientRnnConfig,
) -> GradientCandidate:
    rng = random.Random(stable_name_seed(cfg.seed, environment.name, architecture))
    starts = seed_weights(architecture)
    starts.extend(random_weights(architecture, rng) for _ in range(cfg.candidates))

    trained = []
    for weights in starts:
        optimized, steps = optimize_weights(architecture, weights, environment, traces, cfg)
        pruned = prune_weights(architecture, optimized)
        score = differentiable_return(architecture, pruned, environment, traces, cfg)
        trained.append(
            GradientCandidate(
                architecture=architecture,
                weights=pruned,
                uses_memory=uses_memory(architecture, pruned),
                training_return=score,
                optimized_steps=steps,
            )
        )
    return max(trained, key=lambda candidate: candidate.training_return)


def seed_weights(architecture: str) -> List[Tuple[float, ...]]:
    if architecture == "scalar_rnn":
        return [
            (0.0, 0.0, 0.0, -6.0),
            (0.0, 0.0, 0.0, 6.0),
            (0.0, 0.0, 2.0, 0.0),
            (0.0, 0.4, 2.0, 0.6),
        ]
    if architecture == "gated_scalar_rnn":
        return [
            (0.0, 0.0, 0.0, -6.0),
            (0.0, 0.0, 0.0, 6.0),
            (0.0, 0.1, 2.0, 0.0),
            (0.0, 0.5, 2.0, 0.6),
        ]
    if architecture == "two_unit_rnn":
        return [
            (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -6.0),
            (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.0),
            (0.0, 0.0, 2.0, 0.0, 0.0, -2.0, 0.0),
            (0.0, 0.4, 2.0, 0.0, 0.2, -2.0, 0.5),
        ]
    raise ValueError(f"unknown architecture: {architecture}")


def random_weights(architecture: str, rng: random.Random) -> Tuple[float, ...]:
    if architecture in {"scalar_rnn", "gated_scalar_rnn"}:
        return (
            rng.uniform(-1.2, 1.2),
            rng.uniform(-1.2, 1.2),
            rng.uniform(-2.0, 2.0),
            rng.uniform(-2.0, 2.0),
        )
    if architecture == "two_unit_rnn":
        return (
            rng.uniform(-1.2, 1.2),
            rng.uniform(-1.2, 1.2),
            rng.uniform(-2.0, 2.0),
            rng.uniform(-1.2, 1.2),
            rng.uniform(-1.2, 1.2),
            rng.uniform(-2.0, 2.0),
            rng.uniform(-2.0, 2.0),
        )
    raise ValueError(f"unknown architecture: {architecture}")


def optimize_weights(
    architecture: str,
    start: Tuple[float, ...],
    environment: EnvironmentFamily,
    traces: Sequence[EpisodeTrace],
    cfg: GradientRnnConfig,
) -> Tuple[Tuple[float, ...], int]:
    weights = clamp_weights(architecture, start)
    best_score = differentiable_return(architecture, weights, environment, traces, cfg)
    accepted_steps = 0
    learning_rate = cfg.learning_rate

    for _step in range(cfg.gradient_steps):
        gradient = finite_difference_gradient(architecture, weights, environment, traces, cfg)
        norm = math.sqrt(sum(value * value for value in gradient))
        if norm <= EPS:
            break
        direction = tuple(value / norm for value in gradient)
        candidate = clamp_weights(
            architecture,
            tuple(weight + learning_rate * delta for weight, delta in zip(weights, direction)),
        )
        candidate_score = differentiable_return(architecture, candidate, environment, traces, cfg)
        if candidate_score >= best_score + 1e-9:
            weights = candidate
            best_score = candidate_score
            accepted_steps += 1
            learning_rate = min(cfg.learning_rate, learning_rate * 1.03)
        else:
            learning_rate *= 0.5
            if learning_rate < 1e-4:
                break
    return weights, accepted_steps


def finite_difference_gradient(
    architecture: str,
    weights: Tuple[float, ...],
    environment: EnvironmentFamily,
    traces: Sequence[EpisodeTrace],
    cfg: GradientRnnConfig,
) -> Tuple[float, ...]:
    gradient = []
    for index in range(len(weights)):
        high = list(weights)
        low = list(weights)
        high[index] += cfg.finite_diff_epsilon
        low[index] -= cfg.finite_diff_epsilon
        high_score = differentiable_return(
            architecture,
            clamp_weights(architecture, tuple(high)),
            environment,
            traces,
            cfg,
        )
        low_score = differentiable_return(
            architecture,
            clamp_weights(architecture, tuple(low)),
            environment,
            traces,
            cfg,
        )
        gradient.append((high_score - low_score) / (2.0 * cfg.finite_diff_epsilon))
    return tuple(gradient)


def differentiable_return(
    architecture: str,
    weights: Tuple[float, ...],
    environment: EnvironmentFamily,
    traces: Sequence[EpisodeTrace],
    cfg: GradientRnnConfig,
) -> float:
    total = 0.0
    memory_charge = smooth_memory_charge(architecture, weights, cfg)
    for trace in traces:
        hidden = run_recurrent_state(architecture, weights, trace.probe_rewards)
        total -= memory_charge
        value = latent_value(architecture, hidden)
        threshold = weights[-1]
        risk_probability = sigmoid(cfg.policy_scale * (value - threshold))
        for profile in environment.contexts[cfg.calibration_contexts :]:
            total += risk_probability * risky_reward(profile, trace.local_success[profile.name])
            total += (1.0 - risk_probability) * profile.safe_reward
    return total / len(traces)


def smooth_memory_charge(
    architecture: str,
    weights: Tuple[float, ...],
    cfg: GradientRnnConfig,
) -> float:
    strength = memory_strength(architecture, weights)
    return cfg.calibration_cost * (1.0 - math.exp(-cfg.memory_cost_scale * strength))


def evaluate_candidate(
    environment: EnvironmentFamily,
    scenario: ScenarioSpec,
    candidate: GradientCandidate,
    cfg: GradientRnnConfig,
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
        hidden = run_recurrent_state(candidate.architecture, candidate.weights, probe_rewards)
        if candidate.uses_memory:
            total_reward -= cfg.calibration_cost
            memory_uses += 1
        latents.append(latent_value(candidate.architecture, hidden))
        self_labels.append(state.self_signal)
        world_labels.append(state.world_signal)
        control_labels.append(majority_control_success(state.local_success, environment, cfg))
        for profile in environment.contexts[cfg.calibration_contexts :]:
            choice = choose(candidate.architecture, candidate.weights, hidden)
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
        training_return=candidate.training_return,
        optimized_steps=candidate.optimized_steps,
        selected_weights=",".join(f"{weight:.3f}" for weight in candidate.weights),
    )


def run_recurrent_state(
    architecture: str,
    weights: Tuple[float, ...],
    probe_rewards: Tuple[float, ...],
) -> Tuple[float, ...]:
    if architecture == "scalar_rnn":
        bias, recurrent, input_weight, _threshold = weights
        hidden = 0.0
        for reward in probe_rewards:
            hidden = math.tanh(bias + recurrent * hidden + input_weight * reward)
        return (hidden,)
    if architecture == "gated_scalar_rnn":
        bias, retention, input_weight, _threshold = weights
        hidden = 0.0
        gate = sigmoid(retention)
        for reward in probe_rewards:
            proposal = math.tanh(bias + input_weight * reward)
            hidden = gate * hidden + (1.0 - gate) * proposal
        return (hidden,)
    if architecture == "two_unit_rnn":
        b1, r1, i1, b2, r2, i2, _threshold = weights
        h1 = 0.0
        h2 = 0.0
        for reward in probe_rewards:
            h1 = math.tanh(b1 + r1 * h1 + i1 * reward)
            h2 = math.tanh(b2 + r2 * h2 + i2 * reward)
        return (h1, h2)
    raise ValueError(f"unknown architecture: {architecture}")


def choose(architecture: str, weights: Tuple[float, ...], hidden: Tuple[float, ...]) -> str:
    threshold = weights[-1]
    value = latent_value(architecture, hidden)
    return "risky" if value >= threshold else "safe"


def latent_value(architecture: str, hidden: Tuple[float, ...]) -> float:
    if architecture == "two_unit_rnn":
        return hidden[0] - hidden[1]
    return hidden[0]


def memory_strength(architecture: str, weights: Tuple[float, ...]) -> float:
    if architecture in {"scalar_rnn", "gated_scalar_rnn"}:
        return abs(weights[2])
    if architecture == "two_unit_rnn":
        return abs(weights[2]) + abs(weights[5])
    raise ValueError(f"unknown architecture: {architecture}")


def uses_memory(architecture: str, weights: Tuple[float, ...]) -> bool:
    return memory_strength(architecture, weights) > EPS


def prune_weights(architecture: str, weights: Tuple[float, ...]) -> Tuple[float, ...]:
    values = list(weights)
    if architecture in {"scalar_rnn", "gated_scalar_rnn"}:
        if abs(values[2]) < PRUNE_EPS:
            values[2] = 0.0
    elif architecture == "two_unit_rnn":
        if abs(values[2]) < PRUNE_EPS:
            values[2] = 0.0
        if abs(values[5]) < PRUNE_EPS:
            values[5] = 0.0
    else:
        raise ValueError(f"unknown architecture: {architecture}")
    return tuple(values)


def clamp_weights(architecture: str, weights: Tuple[float, ...]) -> Tuple[float, ...]:
    if architecture not in ARCHITECTURES:
        raise ValueError(f"unknown architecture: {architecture}")
    values = []
    for value in weights:
        values.append(max(-6.0, min(6.0, value)))
    return tuple(values)


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
                    supports_gradient_rnn_precursor=supports,
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
        supporting = sum(1 for row in rows if row.supports_gradient_rnn_precursor)
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
                supports_gradient_rnn_precursor=supporting == len(rows),
            )
        )
    return verdicts


def run_experiment(
    cfg: GradientRnnConfig,
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
                "training_marginal_success": statistics.fmean(
                    1.0 if trace.local_success[profile.name] else 0.0
                    for trace in traces
                    for profile in environment.contexts[cfg.calibration_contexts :]
                ),
            }
            for architecture in ARCHITECTURES:
                candidate = train_architecture(architecture, environment, traces, cfg)
                policy_results.append(evaluate_candidate(environment, scenario, candidate, cfg, signature))
            for baseline in ["marginal_no_memory", "task_local_probe", "oracle"]:
                baseline_results.append(evaluate_baseline(environment, scenario, cfg, baseline))
    environment_verdicts = build_environment_verdicts(policy_results, baseline_results)
    scenario_verdicts = build_scenario_verdicts(environment_verdicts)
    return policy_results, baseline_results, environment_verdicts, scenario_verdicts, diagnostics


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
        "mean_best_architecture_reward",
        "mean_local_probe_reward",
        "supports_gradient_rnn_precursor",
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
                str(verdict.supports_gradient_rnn_precursor),
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


def parse_args() -> GradientRnnConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=500)
    parser.add_argument("--training-episodes", type=int, default=500)
    parser.add_argument("--seed", type=int, default=20260601)
    parser.add_argument("--calibration-contexts", type=int, default=2)
    parser.add_argument("--calibration-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    parser.add_argument("--probe-success-reward", type=float, default=1.0)
    parser.add_argument("--probe-failure-reward", type=float, default=-1.0)
    parser.add_argument("--candidates", type=int, default=2)
    parser.add_argument("--gradient-steps", type=int, default=20)
    parser.add_argument("--learning-rate", type=float, default=0.35)
    parser.add_argument("--finite-diff-epsilon", type=float, default=0.03)
    parser.add_argument("--policy-scale", type=float, default=6.0)
    parser.add_argument("--memory-cost-scale", type=float, default=12.0)
    args = parser.parse_args()
    if args.calibration_contexts < 1:
        raise SystemExit("--calibration-contexts must be at least 1")
    if any(args.calibration_contexts >= len(environment.contexts) for environment in ENVIRONMENTS):
        raise SystemExit("--calibration-contexts must leave held-out contexts")
    if args.candidates < 0:
        raise SystemExit("--candidates must be non-negative")
    if args.gradient_steps < 0:
        raise SystemExit("--gradient-steps must be non-negative")
    return GradientRnnConfig(
        episodes=args.episodes,
        training_episodes=args.training_episodes,
        seed=args.seed,
        calibration_contexts=args.calibration_contexts,
        calibration_cost=args.calibration_cost,
        local_probe_cost=args.local_probe_cost,
        probe_success_reward=args.probe_success_reward,
        probe_failure_reward=args.probe_failure_reward,
        candidates=args.candidates,
        gradient_steps=args.gradient_steps,
        learning_rate=args.learning_rate,
        finite_diff_epsilon=args.finite_diff_epsilon,
        policy_scale=args.policy_scale,
        memory_cost_scale=args.memory_cost_scale,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    policy_results, baseline_results, environment_verdicts, scenario_verdicts, diagnostics = run_experiment(cfg)

    summary_path = ARTIFACT_DIR / "gradient_recurrent_policy_summary.csv"
    baseline_path = ARTIFACT_DIR / "gradient_recurrent_policy_baselines.csv"
    environment_verdict_path = ARTIFACT_DIR / "gradient_recurrent_policy_environment_verdict.csv"
    scenario_verdict_path = ARTIFACT_DIR / "gradient_recurrent_policy_scenario_verdict.csv"
    results_path = ARTIFACT_DIR / "gradient_recurrent_policy_results.json"
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
    return 0 if all(row.supports_gradient_rnn_precursor for row in scenario_verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
