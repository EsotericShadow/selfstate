#!/usr/bin/env python3
"""Mixed-sensor recurrent filter precursor.

This is a stricter companion to unseeded_recurrent_filter.py. The controller no
longer receives a channel that directly corresponds to agent-state or
world-state evidence. Instead, noisy self/world evidence is linearly mixed into
two sensor channels. Candidate recurrent controllers are random-start policies
selected by return. Causal tests ablate the latent source before mixing.

Prediction:

- random-start recurrent search should recover a useful projection of mixed
  sensors when latent source A tracks persistent agent-state;
- it should recover the other projection when latent source B tracks external
  state;
- local probing or no-state control should win when no shared latent source
  helps.
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


ARTIFACT_DIR = Path("artifacts")
PRIOR_TRUE = 0.55
RISKY_SUCCESS_REWARD = 24.0
RISKY_FAILURE_REWARD = -16.0
SAFE_REWARD = 8.0


@dataclass(frozen=True)
class MixedSensorConfig:
    episodes: int = 500
    training_episodes: int = 800
    seed: int = 20260603
    horizon: int = 8
    evidence_samples: int = 9
    cue_accuracy: float = 0.85
    shared_cue_cost: float = 1.0
    local_probe_cost: float = 1.0
    random_candidates: int = 1800


@dataclass(frozen=True)
class MixedScenario:
    name: str
    mode: str


@dataclass(frozen=True)
class EpisodeState:
    scenario: str
    source_a_signal: bool
    source_b_signal: bool
    source_observations: Tuple[Tuple[float, float], ...]
    mixed_observations: Tuple[Tuple[float, float], ...]
    step_success: Tuple[bool, ...]


@dataclass(frozen=True)
class Candidate:
    architecture: str
    weights: Tuple[float, ...]
    training_reward: float


@dataclass(frozen=True)
class TrainingRow:
    scenario: str
    selected_policy: str
    selected_architecture: str
    recurrent_training_reward: float
    local_training_reward: float
    greedy_training_reward: float
    safe_training_reward: float
    selected_weights: str


@dataclass
class AgentResult:
    scenario: str
    agent: str
    selected_policy: str
    selected_architecture: str
    dependency_signature: str
    total_reward: float
    shared_cue_count: int
    local_probe_count: int
    risky_count: int
    safe_count: int
    failed_risky_count: int
    success_rate: float


SCENARIOS = [
    MixedScenario("self_mixed_hidden", "self_mixed_hidden"),
    MixedScenario("world_mixed_hidden", "world_mixed_hidden"),
    MixedScenario("independent_hidden", "independent_hidden"),
    MixedScenario("irrelevant_control", "irrelevant_control"),
]

ARCHITECTURES = ["sum_rnn", "scalar_rnn", "two_unit_rnn"]

AGENTS = [
    "greedy_no_state",
    "safe_no_state",
    "recurrent_controller",
    "task_local_probe",
    "learned_structure_selector",
    "oracle_observation",
]

BASELINE_POLICIES = ["greedy_no_state", "safe_no_state", "task_local_probe"]


def stable_state_seed(seed: int, scenario: str, phase: str, episode: int) -> int:
    value = seed + episode * 1009
    for char in f"{scenario}:{phase}":
        value = (value * 131 + ord(char)) % (2**32)
    return value


def stable_name_seed(seed: int, scenario: str, architecture: str) -> int:
    value = seed
    for char in f"{scenario}:{architecture}":
        value = (value * 131 + ord(char)) % (2**32)
    return value


def sample_state(
    scenario: MixedScenario,
    phase: str,
    episode: int,
    cfg: MixedSensorConfig,
) -> EpisodeState:
    rng = random.Random(stable_state_seed(cfg.seed, scenario.name, phase, episode))
    source_a_signal = rng.random() < PRIOR_TRUE
    source_b_signal = rng.random() < PRIOR_TRUE
    if scenario.mode == "self_mixed_hidden":
        step_success = tuple(source_a_signal for _ in range(cfg.horizon))
    elif scenario.mode == "world_mixed_hidden":
        step_success = tuple(source_b_signal for _ in range(cfg.horizon))
    elif scenario.mode == "independent_hidden":
        step_success = tuple(rng.random() < PRIOR_TRUE for _ in range(cfg.horizon))
    elif scenario.mode == "irrelevant_control":
        step_success = tuple(True for _ in range(cfg.horizon))
    else:
        raise ValueError(f"unknown scenario mode: {scenario.mode}")
    source_observations = tuple(
        (
            noisy_source_value(source_a_signal, cfg.cue_accuracy, rng),
            noisy_source_value(source_b_signal, cfg.cue_accuracy, rng),
        )
        for _ in range(cfg.evidence_samples)
    )
    mixed_observations = tuple(mix_sources(source_a, source_b) for source_a, source_b in source_observations)
    return EpisodeState(
        scenario=scenario.name,
        source_a_signal=source_a_signal,
        source_b_signal=source_b_signal,
        source_observations=source_observations,
        mixed_observations=mixed_observations,
        step_success=step_success,
    )


def noisy_source_value(value: bool, accuracy: float, rng: random.Random) -> float:
    cue = value if rng.random() < accuracy else not value
    return 1.0 if cue else -1.0


def mix_sources(source_a: float, source_b: float) -> Tuple[float, float]:
    return 0.8 * source_a + 0.6 * source_b, -0.6 * source_a + 0.8 * source_b


def ablated_observations(
    state: EpisodeState,
    source: str,
) -> Tuple[Tuple[float, float], ...]:
    rows = []
    for source_a, source_b in state.source_observations:
        if source == "a":
            rows.append(mix_sources(0.0, source_b))
        elif source == "b":
            rows.append(mix_sources(source_a, 0.0))
        elif source == "none":
            rows.append(mix_sources(source_a, source_b))
        else:
            raise ValueError(f"unknown source ablation: {source}")
    return tuple(rows)


def make_states(
    scenario: MixedScenario,
    phase: str,
    count: int,
    cfg: MixedSensorConfig,
) -> List[EpisodeState]:
    return [sample_state(scenario, phase, episode, cfg) for episode in range(count)]


def random_candidate(architecture: str, rng: random.Random) -> Candidate:
    if architecture == "sum_rnn":
        return Candidate(
            architecture,
            (
                rng.uniform(-0.15, 0.15),
                rng.uniform(-2.0, 2.0),
                rng.uniform(-2.0, 2.0),
                rng.uniform(-2.0, 2.0),
                rng.uniform(-2.0, 2.0),
            ),
            0.0,
        )
    if architecture == "scalar_rnn":
        return Candidate(
            architecture,
            (
                rng.uniform(-0.5, 0.5),
                rng.uniform(-1.0, 1.0),
                rng.uniform(-2.5, 2.5),
                rng.uniform(-2.5, 2.5),
                rng.uniform(-5.0, 5.0),
                rng.uniform(-1.5, 1.5),
            ),
            0.0,
        )
    if architecture == "two_unit_rnn":
        return Candidate(
            architecture,
            (
                rng.uniform(-0.5, 0.5),
                rng.uniform(-1.0, 1.0),
                rng.uniform(-2.5, 2.5),
                rng.uniform(-2.5, 2.5),
                rng.uniform(-0.5, 0.5),
                rng.uniform(-1.0, 1.0),
                rng.uniform(-2.5, 2.5),
                rng.uniform(-2.5, 2.5),
                rng.uniform(-5.0, 5.0),
                rng.uniform(-5.0, 5.0),
                rng.uniform(-1.5, 1.5),
            ),
            0.0,
        )
    raise ValueError(f"unknown architecture: {architecture}")


def train_recurrent(
    scenario: MixedScenario,
    states: Sequence[EpisodeState],
    cfg: MixedSensorConfig,
) -> Candidate:
    candidates = []
    for architecture in ARCHITECTURES:
        rng = random.Random(stable_name_seed(cfg.seed + 123, scenario.name, architecture))
        for _ in range(cfg.random_candidates):
            candidate = random_candidate(architecture, rng)
            candidates.append(
                Candidate(
                    architecture=candidate.architecture,
                    weights=candidate.weights,
                    training_reward=mean_recurrent_reward(states, candidate, cfg),
                )
            )
    return max(candidates, key=lambda candidate: candidate.training_reward)


def mean_recurrent_reward(
    states: Sequence[EpisodeState],
    candidate: Candidate,
    cfg: MixedSensorConfig,
) -> float:
    return statistics.fmean(
        evaluate_recurrent(state, candidate, cfg, ablate_source="none")[0]
        for state in states
    )


def evaluate_recurrent(
    state: EpisodeState,
    candidate: Candidate,
    cfg: MixedSensorConfig,
    ablate_source: str,
) -> Tuple[float, int, int, int, int, int, int]:
    observations = ablated_observations(state, ablate_source)
    logit = recurrent_logit(candidate, observations)
    choice = "risky" if logit >= 0.0 else "safe"
    total_reward = -cfg.shared_cue_cost
    risky_count = 0
    safe_count = 0
    failed_count = 0
    successes = 0
    for hidden_success in state.step_success:
        reward, success = action_reward(choice, hidden_success)
        total_reward += reward
        if choice == "risky":
            risky_count += 1
            if not success:
                failed_count += 1
        else:
            safe_count += 1
        if success:
            successes += 1
    return total_reward, cfg.evidence_samples, 0, risky_count, safe_count, failed_count, successes


def recurrent_logit(
    candidate: Candidate,
    observations: Sequence[Tuple[float, float]],
) -> float:
    if candidate.architecture == "sum_rnn":
        input_bias, weight_1, weight_2, output_weight, output_bias = candidate.weights
        hidden = 0.0
        for sensor_1, sensor_2 in observations:
            hidden += input_bias + weight_1 * sensor_1 + weight_2 * sensor_2
        return output_weight * hidden + output_bias
    if candidate.architecture == "scalar_rnn":
        bias, recurrent, weight_1, weight_2, output_weight, output_bias = candidate.weights
        hidden = 0.0
        for sensor_1, sensor_2 in observations:
            hidden = math.tanh(bias + recurrent * hidden + weight_1 * sensor_1 + weight_2 * sensor_2)
        return output_weight * hidden + output_bias
    if candidate.architecture == "two_unit_rnn":
        (
            bias_1,
            recurrent_1,
            weight_1a,
            weight_1b,
            bias_2,
            recurrent_2,
            weight_2a,
            weight_2b,
            output_1,
            output_2,
            output_bias,
        ) = candidate.weights
        hidden_1 = 0.0
        hidden_2 = 0.0
        for sensor_1, sensor_2 in observations:
            hidden_1 = math.tanh(bias_1 + recurrent_1 * hidden_1 + weight_1a * sensor_1 + weight_1b * sensor_2)
            hidden_2 = math.tanh(bias_2 + recurrent_2 * hidden_2 + weight_2a * sensor_1 + weight_2b * sensor_2)
        return output_1 * hidden_1 + output_2 * hidden_2 + output_bias
    raise ValueError(f"unknown architecture: {candidate.architecture}")


def evaluate_baseline(
    state: EpisodeState,
    policy: str,
    cfg: MixedSensorConfig,
) -> Tuple[float, int, int, int, int, int, int]:
    total_reward = 0.0
    local_probe_count = 0
    risky_count = 0
    safe_count = 0
    failed_count = 0
    successes = 0
    for hidden_success in state.step_success:
        if policy == "greedy_no_state":
            choice = "risky"
        elif policy == "safe_no_state":
            choice = "safe"
        elif policy == "task_local_probe":
            total_reward -= cfg.local_probe_cost
            local_probe_count += 1
            choice = "risky" if hidden_success else "safe"
        elif policy == "oracle_observation":
            choice = "risky" if hidden_success else "safe"
        else:
            raise ValueError(f"unknown baseline policy: {policy}")
        reward, success = action_reward(choice, hidden_success)
        total_reward += reward
        if choice == "risky":
            risky_count += 1
            if not success:
                failed_count += 1
        else:
            safe_count += 1
        if success:
            successes += 1
    return total_reward, 0, local_probe_count, risky_count, safe_count, failed_count, successes


def action_reward(choice: str, hidden_success: bool) -> Tuple[float, bool]:
    if choice == "safe":
        return SAFE_REWARD, True
    if hidden_success:
        return RISKY_SUCCESS_REWARD, True
    return RISKY_FAILURE_REWARD, False


def select_policy(
    candidate: Candidate,
    training_states: Sequence[EpisodeState],
    cfg: MixedSensorConfig,
) -> Tuple[str, Dict[str, float]]:
    rewards = {"recurrent_controller": candidate.training_reward}
    for policy in BASELINE_POLICIES:
        rewards[policy] = statistics.fmean(
            evaluate_baseline(state, policy, cfg)[0]
            for state in training_states
        )
    selected = sorted(rewards, key=lambda policy: (-rewards[policy], policy))[0]
    return selected, rewards


def dependency_signature(
    scenario: MixedScenario,
    candidate: Candidate,
    cfg: MixedSensorConfig,
) -> Tuple[str, Dict[str, float]]:
    states = make_states(scenario, "dependency", cfg.episodes, cfg)
    intact = statistics.fmean(evaluate_recurrent(state, candidate, cfg, "none")[0] for state in states)
    ablate_a = statistics.fmean(evaluate_recurrent(state, candidate, cfg, "a")[0] for state in states)
    ablate_b = statistics.fmean(evaluate_recurrent(state, candidate, cfg, "b")[0] for state in states)
    loss_a = intact - ablate_a
    loss_b = intact - ablate_b
    effect_a, effect_b = intervention_effects(scenario, states)
    if effect_a > 0.20 and loss_a > loss_b + 30.0 and loss_a > 30.0:
        signature = "agent_bounded_mixed_recurrent"
    elif effect_b > 0.20 and loss_b > loss_a + 30.0 and loss_b > 30.0:
        signature = "external_mixed_recurrent"
    else:
        signature = "no_shared_mixed_boundary"
    return (
        signature,
        {
            "intact_recurrent_reward": intact,
            "ablate_source_a_reward": ablate_a,
            "ablate_source_b_reward": ablate_b,
            "source_a_ablation_loss": loss_a,
            "source_b_ablation_loss": loss_b,
            "source_a_intervention_effect": effect_a,
            "source_b_intervention_effect": effect_b,
        },
    )


def intervention_effects(
    scenario: MixedScenario,
    states: Sequence[EpisodeState],
) -> Tuple[float, float]:
    effect_a = []
    effect_b = []
    for state in states:
        baseline = success_rate(state.step_success)
        effect_a.append(success_rate(intervene_source_a(scenario, state).step_success) - baseline)
        effect_b.append(success_rate(intervene_source_b(scenario, state).step_success) - baseline)
    return statistics.fmean(effect_a), statistics.fmean(effect_b)


def intervene_source_a(scenario: MixedScenario, state: EpisodeState) -> EpisodeState:
    if scenario.mode == "self_mixed_hidden":
        return replace_step_success(state, True)
    return state


def intervene_source_b(scenario: MixedScenario, state: EpisodeState) -> EpisodeState:
    if scenario.mode == "world_mixed_hidden":
        return replace_step_success(state, True)
    return state


def replace_step_success(state: EpisodeState, value: bool) -> EpisodeState:
    return EpisodeState(
        scenario=state.scenario,
        source_a_signal=state.source_a_signal,
        source_b_signal=state.source_b_signal,
        source_observations=state.source_observations,
        mixed_observations=state.mixed_observations,
        step_success=tuple(value for _ in state.step_success),
    )


def success_rate(step_success: Sequence[bool]) -> float:
    return sum(1 for success in step_success if success) / len(step_success)


def run_agent(
    scenario: MixedScenario,
    state: EpisodeState,
    agent: str,
    selected_policy: str,
    candidate: Candidate,
    signature: str,
    cfg: MixedSensorConfig,
) -> AgentResult:
    policy = selected_policy if agent == "learned_structure_selector" else agent
    if policy == "recurrent_controller":
        total, shared_cues, local_probes, risky, safe, failed, successes = evaluate_recurrent(
            state,
            candidate,
            cfg,
            "none",
        )
    else:
        total, shared_cues, local_probes, risky, safe, failed, successes = evaluate_baseline(state, policy, cfg)
    return AgentResult(
        scenario=scenario.name,
        agent=agent,
        selected_policy=selected_policy,
        selected_architecture=candidate.architecture,
        dependency_signature=signature,
        total_reward=total,
        shared_cue_count=shared_cues,
        local_probe_count=local_probes,
        risky_count=risky,
        safe_count=safe,
        failed_risky_count=failed,
        success_rate=successes / cfg.horizon,
    )


def summarize(results: Sequence[AgentResult]) -> List[Dict[str, object]]:
    grouped: Dict[Tuple[str, str], List[AgentResult]] = {}
    for result in results:
        grouped.setdefault((result.scenario, result.agent), []).append(result)
    rows = []
    for (scenario, agent), items in sorted(grouped.items()):
        rows.append(
            {
                "scenario": scenario,
                "agent": agent,
                "selected_policy": items[0].selected_policy,
                "selected_architecture": items[0].selected_architecture,
                "dependency_signature": items[0].dependency_signature,
                "episodes": len(items),
                "mean_total_reward": statistics.fmean(item.total_reward for item in items),
                "mean_shared_cue_count": statistics.fmean(item.shared_cue_count for item in items),
                "mean_local_probe_count": statistics.fmean(item.local_probe_count for item in items),
                "mean_risky_count": statistics.fmean(item.risky_count for item in items),
                "mean_safe_count": statistics.fmean(item.safe_count for item in items),
                "mean_failed_risky_count": statistics.fmean(item.failed_risky_count for item in items),
                "mean_success_rate": statistics.fmean(item.success_rate for item in items),
            }
        )
    return rows


def verdict_rows(
    summary_rows: Sequence[Dict[str, object]],
    training_rows: Sequence[TrainingRow],
    dependency_rows: Sequence[Dict[str, object]],
) -> List[Dict[str, object]]:
    rows = []
    for scenario in sorted({str(row["scenario"]) for row in summary_rows}):
        training = next(row for row in training_rows if row.scenario == scenario)
        dependency = next(row for row in dependency_rows if row["scenario"] == scenario)
        recurrent_reward = reward_for(summary_rows, scenario, "recurrent_controller")
        local_reward = reward_for(summary_rows, scenario, "task_local_probe")
        greedy_reward = reward_for(summary_rows, scenario, "greedy_no_state")
        selector_reward = reward_for(summary_rows, scenario, "learned_structure_selector")
        rows.append(
            {
                "scenario": scenario,
                "selected_policy": training.selected_policy,
                "selected_architecture": training.selected_architecture,
                "dependency_signature": dependency["dependency_signature"],
                "recurrent_reward": recurrent_reward,
                "local_probe_reward": local_reward,
                "greedy_reward": greedy_reward,
                "selector_reward": selector_reward,
                "source_a_ablation_loss": dependency["source_a_ablation_loss"],
                "source_b_ablation_loss": dependency["source_b_ablation_loss"],
                "supports_mixed_sensor_prediction": scenario_supports_prediction(
                    scenario,
                    training.selected_policy,
                    str(dependency["dependency_signature"]),
                    recurrent_reward,
                    local_reward,
                    greedy_reward,
                    float(dependency["source_a_ablation_loss"]),
                    float(dependency["source_b_ablation_loss"]),
                ),
            }
        )
    return rows


def reward_for(summary_rows: Sequence[Dict[str, object]], scenario: str, agent: str) -> float:
    return float(
        next(
            row["mean_total_reward"]
            for row in summary_rows
            if row["scenario"] == scenario and row["agent"] == agent
        )
    )


def scenario_supports_prediction(
    scenario: str,
    selected_policy: str,
    signature: str,
    recurrent_reward: float,
    local_reward: float,
    greedy_reward: float,
    loss_a: float,
    loss_b: float,
) -> bool:
    if scenario == "self_mixed_hidden":
        return (
            selected_policy == "recurrent_controller"
            and signature == "agent_bounded_mixed_recurrent"
            and recurrent_reward > local_reward
            and loss_a > loss_b + 30.0
        )
    if scenario == "world_mixed_hidden":
        return (
            selected_policy == "recurrent_controller"
            and signature == "external_mixed_recurrent"
            and recurrent_reward > local_reward
            and loss_b > loss_a + 30.0
        )
    if scenario == "independent_hidden":
        return (
            selected_policy == "task_local_probe"
            and signature == "no_shared_mixed_boundary"
            and local_reward > recurrent_reward + 40.0
        )
    if scenario == "irrelevant_control":
        return (
            selected_policy == "greedy_no_state"
            and signature == "no_shared_mixed_boundary"
            and greedy_reward > recurrent_reward
        )
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: MixedSensorConfig,
) -> Tuple[List[AgentResult], List[Dict[str, object]], List[TrainingRow], List[Dict[str, object]], List[Dict[str, object]]]:
    results = []
    training_rows = []
    dependency_rows = []
    for scenario in SCENARIOS:
        training_states = make_states(scenario, "train", cfg.training_episodes, cfg)
        candidate = train_recurrent(scenario, training_states, cfg)
        selected_policy, rewards = select_policy(candidate, training_states, cfg)
        signature, dependency = dependency_signature(scenario, candidate, cfg)
        training_rows.append(
            TrainingRow(
                scenario=scenario.name,
                selected_policy=selected_policy,
                selected_architecture=candidate.architecture,
                recurrent_training_reward=rewards["recurrent_controller"],
                local_training_reward=rewards["task_local_probe"],
                greedy_training_reward=rewards["greedy_no_state"],
                safe_training_reward=rewards["safe_no_state"],
                selected_weights=format_weights(candidate.weights),
            )
        )
        dependency_rows.append({"scenario": scenario.name, "dependency_signature": signature, **dependency})
        test_states = make_states(scenario, "test", cfg.episodes, cfg)
        for state in test_states:
            for agent in AGENTS:
                results.append(run_agent(scenario, state, agent, selected_policy, candidate, signature, cfg))
    summary_rows = summarize(results)
    verdicts = verdict_rows(summary_rows, training_rows, dependency_rows)
    return results, summary_rows, training_rows, dependency_rows, verdicts


def format_weights(weights: Sequence[float]) -> str:
    return ",".join(f"{weight:.4f}" for weight in weights)


def write_csv(path: Path, rows: Iterable[object]) -> None:
    rows = list(rows)
    if not rows:
        return
    first = rows[0]
    if isinstance(first, dict):
        fieldnames = list(first.keys())
        serialize = lambda row: row
    else:
        fieldnames = list(asdict(first).keys())
        serialize = asdict
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(serialize(row))


def print_table(verdicts: Sequence[Dict[str, object]]) -> None:
    headers = [
        "scenario",
        "selected_policy",
        "dependency_signature",
        "recurrent_reward",
        "local_probe_reward",
        "supports_mixed_sensor_prediction",
    ]
    rows = []
    for verdict in verdicts:
        rows.append(
            [
                str(verdict["scenario"]),
                str(verdict["selected_policy"]),
                str(verdict["dependency_signature"]),
                f"{float(verdict['recurrent_reward']):.3f}",
                f"{float(verdict['local_probe_reward']):.3f}",
                str(verdict["supports_mixed_sensor_prediction"]),
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


def parse_args() -> MixedSensorConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=500)
    parser.add_argument("--training-episodes", type=int, default=800)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--horizon", type=int, default=8)
    parser.add_argument("--evidence-samples", type=int, default=9)
    parser.add_argument("--cue-accuracy", type=float, default=0.85)
    parser.add_argument("--shared-cue-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    parser.add_argument("--random-candidates", type=int, default=1800)
    args = parser.parse_args()
    if args.episodes < 1:
        raise SystemExit("--episodes must be at least 1")
    if args.training_episodes < 1:
        raise SystemExit("--training-episodes must be at least 1")
    if args.horizon < 1:
        raise SystemExit("--horizon must be at least 1")
    if args.evidence_samples < 1:
        raise SystemExit("--evidence-samples must be at least 1")
    if not 0.5 <= args.cue_accuracy <= 1.0:
        raise SystemExit("--cue-accuracy must be in [0.5, 1.0]")
    if args.random_candidates < 1:
        raise SystemExit("--random-candidates must be positive")
    return MixedSensorConfig(
        episodes=args.episodes,
        training_episodes=args.training_episodes,
        seed=args.seed,
        horizon=args.horizon,
        evidence_samples=args.evidence_samples,
        cue_accuracy=args.cue_accuracy,
        shared_cue_cost=args.shared_cue_cost,
        local_probe_cost=args.local_probe_cost,
        random_candidates=args.random_candidates,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    results, summary_rows, training_rows, dependency_rows, verdicts = run_experiment(cfg)
    summary_path = ARTIFACT_DIR / "mixed_sensor_recurrent_filter_summary.csv"
    training_path = ARTIFACT_DIR / "mixed_sensor_recurrent_filter_training.csv"
    dependency_path = ARTIFACT_DIR / "mixed_sensor_recurrent_filter_dependency.csv"
    verdict_path = ARTIFACT_DIR / "mixed_sensor_recurrent_filter_verdict.csv"
    results_path = ARTIFACT_DIR / "mixed_sensor_recurrent_filter_results.json"
    write_csv(summary_path, summary_rows)
    write_csv(training_path, training_rows)
    write_csv(dependency_path, dependency_rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "training": [asdict(row) for row in training_rows],
                "dependency": dependency_rows,
                "summary": summary_rows,
                "verdict": verdicts,
                "episode_results": [asdict(row) for row in results],
            },
            handle,
            indent=2,
        )
        handle.write("\n")
    print(f"wrote {summary_path}")
    print(f"wrote {training_path}")
    print(f"wrote {dependency_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print_table(verdicts)
    return 0 if all(bool(row["supports_mixed_sensor_prediction"]) for row in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
