#!/usr/bin/env python3
"""Recurrent noisy-observation filter precursor.

This experiment moves beyond empirical cue-count tables. Candidate controllers
are small recurrent policies that process noisy observation streams and are
selected by training return. The learned recurrent state is then tested by input
channel ablation.

Prediction:

- recurrent control should depend on channel A when A tracks persistent
  agent-state;
- recurrent control should depend on channel B when B tracks persistent
  external state;
- local probing should win when future steps have independent hidden states;
- greedy no-state control should win when hidden state is irrelevant.
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
EPS = 1e-12


@dataclass(frozen=True)
class RecurrentFilterConfig:
    episodes: int = 500
    training_episodes: int = 800
    seed: int = 20260603
    horizon: int = 8
    evidence_samples: int = 9
    cue_accuracy: float = 0.85
    shared_cue_cost: float = 1.0
    local_probe_cost: float = 1.0
    random_candidates: int = 500


@dataclass(frozen=True)
class RecurrentScenario:
    name: str
    mode: str


@dataclass(frozen=True)
class EpisodeState:
    scenario: str
    channel_a_signal: bool
    channel_b_signal: bool
    observations: Tuple[Tuple[bool, bool], ...]
    step_success: Tuple[bool, ...]


@dataclass(frozen=True)
class RecurrentCandidate:
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
    RecurrentScenario("self_noisy_hidden", "self_noisy_hidden"),
    RecurrentScenario("world_noisy_hidden", "world_noisy_hidden"),
    RecurrentScenario("independent_hidden", "independent_hidden"),
    RecurrentScenario("irrelevant_control", "irrelevant_control"),
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
    scenario: RecurrentScenario,
    phase: str,
    episode: int,
    cfg: RecurrentFilterConfig,
) -> EpisodeState:
    rng = random.Random(stable_state_seed(cfg.seed, scenario.name, phase, episode))
    channel_a_signal = rng.random() < PRIOR_TRUE
    channel_b_signal = rng.random() < PRIOR_TRUE
    if scenario.mode == "self_noisy_hidden":
        step_success = tuple(channel_a_signal for _ in range(cfg.horizon))
    elif scenario.mode == "world_noisy_hidden":
        step_success = tuple(channel_b_signal for _ in range(cfg.horizon))
    elif scenario.mode == "independent_hidden":
        step_success = tuple(rng.random() < PRIOR_TRUE for _ in range(cfg.horizon))
    elif scenario.mode == "irrelevant_control":
        step_success = tuple(True for _ in range(cfg.horizon))
    else:
        raise ValueError(f"unknown scenario mode: {scenario.mode}")
    observations = tuple(
        (
            noisy_cue(channel_a_signal, cfg.cue_accuracy, rng),
            noisy_cue(channel_b_signal, cfg.cue_accuracy, rng),
        )
        for _ in range(cfg.evidence_samples)
    )
    return EpisodeState(
        scenario=scenario.name,
        channel_a_signal=channel_a_signal,
        channel_b_signal=channel_b_signal,
        observations=observations,
        step_success=step_success,
    )


def noisy_cue(value: bool, accuracy: float, rng: random.Random) -> bool:
    return value if rng.random() < accuracy else not value


def make_states(
    scenario: RecurrentScenario,
    phase: str,
    count: int,
    cfg: RecurrentFilterConfig,
) -> List[EpisodeState]:
    return [sample_state(scenario, phase, episode, cfg) for episode in range(count)]


def train_recurrent(
    scenario: RecurrentScenario,
    states: Sequence[EpisodeState],
    cfg: RecurrentFilterConfig,
) -> RecurrentCandidate:
    candidates = []
    for architecture in ARCHITECTURES:
        candidates.extend(seed_candidates(architecture))
        rng = random.Random(stable_name_seed(cfg.seed, scenario.name, architecture))
        for _ in range(cfg.random_candidates):
            candidates.append(random_candidate(architecture, rng))
    scored = [
        RecurrentCandidate(
            architecture=candidate.architecture,
            weights=candidate.weights,
            training_reward=mean_recurrent_reward(states, candidate, cfg),
        )
        for candidate in candidates
    ]
    return max(scored, key=lambda candidate: candidate.training_reward)


def seed_candidates(architecture: str) -> List[RecurrentCandidate]:
    if architecture == "sum_rnn":
        return [
            RecurrentCandidate(architecture, (0.0, 1.0, 0.0, 1.0, 0.0), 0.0),
            RecurrentCandidate(architecture, (0.0, 0.0, 1.0, 1.0, 0.0), 0.0),
            RecurrentCandidate(architecture, (0.0, 0.5, 0.5, 1.0, 0.0), 0.0),
            RecurrentCandidate(architecture, (0.0, 0.0, 0.0, 0.0, 6.0), 0.0),
            RecurrentCandidate(architecture, (0.0, 0.0, 0.0, 0.0, -6.0), 0.0),
        ]
    if architecture == "scalar_rnn":
        return [
            RecurrentCandidate(architecture, (0.0, 0.75, 1.0, 0.0, 4.0, 0.0), 0.0),
            RecurrentCandidate(architecture, (0.0, 0.75, 0.0, 1.0, 4.0, 0.0), 0.0),
            RecurrentCandidate(architecture, (0.0, 0.75, 0.5, 0.5, 4.0, 0.0), 0.0),
            RecurrentCandidate(architecture, (0.0, 0.0, 0.0, 0.0, 0.0, 6.0), 0.0),
            RecurrentCandidate(architecture, (0.0, 0.0, 0.0, 0.0, 0.0, -6.0), 0.0),
        ]
    if architecture == "two_unit_rnn":
        return [
            RecurrentCandidate(
                architecture,
                (0.0, 0.75, 1.0, 0.0, 0.0, 0.75, 0.0, 1.0, 4.0, 0.0, 0.0),
                0.0,
            ),
            RecurrentCandidate(
                architecture,
                (0.0, 0.75, 1.0, 0.0, 0.0, 0.75, 0.0, 1.0, 0.0, 4.0, 0.0),
                0.0,
            ),
            RecurrentCandidate(
                architecture,
                (0.0, 0.75, 1.0, 0.0, 0.0, 0.75, 0.0, 1.0, 2.0, 2.0, 0.0),
                0.0,
            ),
        ]
    raise ValueError(f"unknown architecture: {architecture}")


def random_candidate(architecture: str, rng: random.Random) -> RecurrentCandidate:
    if architecture == "sum_rnn":
        return RecurrentCandidate(
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
        return RecurrentCandidate(
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
        return RecurrentCandidate(
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


def mean_recurrent_reward(
    states: Sequence[EpisodeState],
    candidate: RecurrentCandidate,
    cfg: RecurrentFilterConfig,
) -> float:
    return statistics.fmean(
        evaluate_recurrent(state, candidate, cfg, ablate_channel="none")[0]
        for state in states
    )


def evaluate_recurrent(
    state: EpisodeState,
    candidate: RecurrentCandidate,
    cfg: RecurrentFilterConfig,
    ablate_channel: str,
) -> Tuple[float, int, int, int, int, int, int]:
    logit = recurrent_logit(candidate, state.observations, ablate_channel)
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
    candidate: RecurrentCandidate,
    observations: Sequence[Tuple[bool, bool]],
    ablate_channel: str,
) -> float:
    if candidate.architecture == "sum_rnn":
        input_bias, weight_a, weight_b, output_weight, output_bias = candidate.weights
        hidden = 0.0
        for cue_a, cue_b in observations:
            obs_a, obs_b = observation_values(cue_a, cue_b, ablate_channel)
            hidden += input_bias + weight_a * obs_a + weight_b * obs_b
        return output_weight * hidden + output_bias
    if candidate.architecture == "scalar_rnn":
        bias, recurrent, weight_a, weight_b, output_weight, output_bias = candidate.weights
        hidden = 0.0
        for cue_a, cue_b in observations:
            obs_a, obs_b = observation_values(cue_a, cue_b, ablate_channel)
            hidden = math.tanh(bias + recurrent * hidden + weight_a * obs_a + weight_b * obs_b)
        return output_weight * hidden + output_bias
    if candidate.architecture == "two_unit_rnn":
        (
            bias_1,
            recurrent_1,
            weight_a_1,
            weight_b_1,
            bias_2,
            recurrent_2,
            weight_a_2,
            weight_b_2,
            output_1,
            output_2,
            output_bias,
        ) = candidate.weights
        hidden_1 = 0.0
        hidden_2 = 0.0
        for cue_a, cue_b in observations:
            obs_a, obs_b = observation_values(cue_a, cue_b, ablate_channel)
            hidden_1 = math.tanh(bias_1 + recurrent_1 * hidden_1 + weight_a_1 * obs_a + weight_b_1 * obs_b)
            hidden_2 = math.tanh(bias_2 + recurrent_2 * hidden_2 + weight_a_2 * obs_a + weight_b_2 * obs_b)
        return output_1 * hidden_1 + output_2 * hidden_2 + output_bias
    raise ValueError(f"unknown architecture: {candidate.architecture}")


def observation_values(cue_a: bool, cue_b: bool, ablate_channel: str) -> Tuple[float, float]:
    obs_a = 1.0 if cue_a else -1.0
    obs_b = 1.0 if cue_b else -1.0
    if ablate_channel == "a":
        obs_a = 0.0
    elif ablate_channel == "b":
        obs_b = 0.0
    elif ablate_channel != "none":
        raise ValueError(f"unknown ablation channel: {ablate_channel}")
    return obs_a, obs_b


def evaluate_baseline(
    state: EpisodeState,
    policy: str,
    cfg: RecurrentFilterConfig,
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
    recurrent: RecurrentCandidate,
    training_states: Sequence[EpisodeState],
    cfg: RecurrentFilterConfig,
) -> Tuple[str, Dict[str, float]]:
    rewards = {
        "recurrent_controller": recurrent.training_reward,
    }
    for policy in BASELINE_POLICIES:
        rewards[policy] = statistics.fmean(
            evaluate_baseline(state, policy, cfg)[0]
            for state in training_states
        )
    selected = sorted(rewards, key=lambda policy: (-rewards[policy], policy))[0]
    return selected, rewards


def dependency_signature(
    scenario: RecurrentScenario,
    recurrent: RecurrentCandidate,
    cfg: RecurrentFilterConfig,
) -> Tuple[str, Dict[str, float]]:
    states = make_states(scenario, "dependency", cfg.episodes, cfg)
    intact = statistics.fmean(evaluate_recurrent(state, recurrent, cfg, "none")[0] for state in states)
    ablate_a = statistics.fmean(evaluate_recurrent(state, recurrent, cfg, "a")[0] for state in states)
    ablate_b = statistics.fmean(evaluate_recurrent(state, recurrent, cfg, "b")[0] for state in states)
    loss_a = intact - ablate_a
    loss_b = intact - ablate_b
    effect_a, effect_b = intervention_effects(scenario, states)
    if effect_a > 0.20 and loss_a > loss_b + 30.0 and loss_a > 30.0:
        signature = "agent_bounded_recurrent"
    elif effect_b > 0.20 and loss_b > loss_a + 30.0 and loss_b > 30.0:
        signature = "external_recurrent"
    else:
        signature = "no_shared_recurrent_boundary"
    return (
        signature,
        {
            "intact_recurrent_reward": intact,
            "ablate_channel_a_reward": ablate_a,
            "ablate_channel_b_reward": ablate_b,
            "channel_a_ablation_loss": loss_a,
            "channel_b_ablation_loss": loss_b,
            "channel_a_intervention_effect": effect_a,
            "channel_b_intervention_effect": effect_b,
        },
    )


def intervention_effects(
    scenario: RecurrentScenario,
    states: Sequence[EpisodeState],
) -> Tuple[float, float]:
    effect_a = []
    effect_b = []
    for state in states:
        baseline = success_rate(state.step_success)
        effect_a.append(success_rate(intervene_channel_a(scenario, state).step_success) - baseline)
        effect_b.append(success_rate(intervene_channel_b(scenario, state).step_success) - baseline)
    return statistics.fmean(effect_a), statistics.fmean(effect_b)


def intervene_channel_a(scenario: RecurrentScenario, state: EpisodeState) -> EpisodeState:
    if scenario.mode == "self_noisy_hidden":
        return replace_step_success(state, True)
    return state


def intervene_channel_b(scenario: RecurrentScenario, state: EpisodeState) -> EpisodeState:
    if scenario.mode == "world_noisy_hidden":
        return replace_step_success(state, True)
    return state


def replace_step_success(state: EpisodeState, value: bool) -> EpisodeState:
    return EpisodeState(
        scenario=state.scenario,
        channel_a_signal=state.channel_a_signal,
        channel_b_signal=state.channel_b_signal,
        observations=state.observations,
        step_success=tuple(value for _ in state.step_success),
    )


def success_rate(step_success: Sequence[bool]) -> float:
    return sum(1 for success in step_success if success) / len(step_success)


def run_agent(
    scenario: RecurrentScenario,
    state: EpisodeState,
    agent: str,
    selected_policy: str,
    recurrent: RecurrentCandidate,
    signature: str,
    cfg: RecurrentFilterConfig,
) -> AgentResult:
    policy = selected_policy if agent == "learned_structure_selector" else agent
    if policy == "recurrent_controller":
        total, shared_cues, local_probes, risky, safe, failed, successes = evaluate_recurrent(
            state,
            recurrent,
            cfg,
            "none",
        )
    else:
        total, shared_cues, local_probes, risky, safe, failed, successes = evaluate_baseline(state, policy, cfg)
    return AgentResult(
        scenario=scenario.name,
        agent=agent,
        selected_policy=selected_policy,
        selected_architecture=recurrent.architecture,
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
                "channel_a_ablation_loss": dependency["channel_a_ablation_loss"],
                "channel_b_ablation_loss": dependency["channel_b_ablation_loss"],
                "supports_recurrent_filter_prediction": scenario_supports_prediction(
                    scenario,
                    training.selected_policy,
                    str(dependency["dependency_signature"]),
                    recurrent_reward,
                    local_reward,
                    greedy_reward,
                    float(dependency["channel_a_ablation_loss"]),
                    float(dependency["channel_b_ablation_loss"]),
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
    if scenario == "self_noisy_hidden":
        return (
            selected_policy == "recurrent_controller"
            and signature == "agent_bounded_recurrent"
            and recurrent_reward > local_reward
            and loss_a > loss_b + 30.0
        )
    if scenario == "world_noisy_hidden":
        return (
            selected_policy == "recurrent_controller"
            and signature == "external_recurrent"
            and recurrent_reward > local_reward
            and loss_b > loss_a + 30.0
        )
    if scenario == "independent_hidden":
        return (
            selected_policy == "task_local_probe"
            and signature == "no_shared_recurrent_boundary"
            and local_reward > recurrent_reward + 40.0
        )
    if scenario == "irrelevant_control":
        return (
            selected_policy == "greedy_no_state"
            and signature == "no_shared_recurrent_boundary"
            and greedy_reward > recurrent_reward
        )
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: RecurrentFilterConfig,
) -> Tuple[List[AgentResult], List[Dict[str, object]], List[TrainingRow], List[Dict[str, object]], List[Dict[str, object]]]:
    results = []
    training_rows = []
    dependency_rows = []
    for scenario in SCENARIOS:
        training_states = make_states(scenario, "train", cfg.training_episodes, cfg)
        recurrent = train_recurrent(scenario, training_states, cfg)
        selected_policy, rewards = select_policy(recurrent, training_states, cfg)
        signature, dependency = dependency_signature(scenario, recurrent, cfg)
        training_rows.append(
            TrainingRow(
                scenario=scenario.name,
                selected_policy=selected_policy,
                selected_architecture=recurrent.architecture,
                recurrent_training_reward=rewards["recurrent_controller"],
                local_training_reward=rewards["task_local_probe"],
                greedy_training_reward=rewards["greedy_no_state"],
                safe_training_reward=rewards["safe_no_state"],
                selected_weights=format_weights(recurrent.weights),
            )
        )
        dependency_rows.append({"scenario": scenario.name, "dependency_signature": signature, **dependency})
        test_states = make_states(scenario, "test", cfg.episodes, cfg)
        for state in test_states:
            for agent in AGENTS:
                results.append(run_agent(scenario, state, agent, selected_policy, recurrent, signature, cfg))
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
        "supports_recurrent_filter_prediction",
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
                str(verdict["supports_recurrent_filter_prediction"]),
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


def parse_args() -> RecurrentFilterConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=500)
    parser.add_argument("--training-episodes", type=int, default=800)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--horizon", type=int, default=8)
    parser.add_argument("--evidence-samples", type=int, default=9)
    parser.add_argument("--cue-accuracy", type=float, default=0.85)
    parser.add_argument("--shared-cue-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    parser.add_argument("--random-candidates", type=int, default=500)
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
    if args.random_candidates < 0:
        raise SystemExit("--random-candidates must be non-negative")
    return RecurrentFilterConfig(
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
    summary_path = ARTIFACT_DIR / "recurrent_observation_filter_summary.csv"
    training_path = ARTIFACT_DIR / "recurrent_observation_filter_training.csv"
    dependency_path = ARTIFACT_DIR / "recurrent_observation_filter_dependency.csv"
    verdict_path = ARTIFACT_DIR / "recurrent_observation_filter_verdict.csv"
    results_path = ARTIFACT_DIR / "recurrent_observation_filter_results.json"
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
    return 0 if all(bool(row["supports_recurrent_filter_prediction"]) for row in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
