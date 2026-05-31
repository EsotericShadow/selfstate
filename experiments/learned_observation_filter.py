#!/usr/bin/env python3
"""Learned noisy-observation filter precursor.

The previous partial-observability sweep supplied the Bayesian posterior. This
experiment removes that shortcut. Learners receive noisy cue histories during
training and estimate, empirically, whether a cue channel predicts future
control outcomes.

Prediction:

- channel A should be selected when it tracks persistent agent-state;
- channel B should be selected when it tracks persistent external state;
- local probing should win when future steps have independent hidden states;
- no-state greedy control should win when hidden state is irrelevant.
"""

from __future__ import annotations

import argparse
import csv
import json
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
class FilterConfig:
    episodes: int = 500
    training_episodes: int = 800
    seed: int = 20260603
    horizon: int = 8
    evidence_samples: int = 7
    cue_accuracy: float = 0.85
    shared_cue_cost: float = 1.0
    local_probe_cost: float = 1.0


@dataclass(frozen=True)
class FilterScenario:
    name: str
    mode: str


@dataclass(frozen=True)
class EpisodeState:
    scenario: str
    channel_a_signal: bool
    channel_b_signal: bool
    channel_a_cues: Tuple[bool, ...]
    channel_b_cues: Tuple[bool, ...]
    step_success: Tuple[bool, ...]


@dataclass(frozen=True)
class TrainingStats:
    scenario: str
    selected_policy: str
    marginal_success_probability: float
    channel_a_success_by_count: Tuple[float, ...]
    channel_b_success_by_count: Tuple[float, ...]
    channel_a_training_reward: float
    channel_b_training_reward: float
    local_training_reward: float
    greedy_training_reward: float
    safe_training_reward: float


@dataclass
class AgentResult:
    scenario: str
    agent: str
    selected_policy: str
    boundary_signature: str
    total_reward: float
    shared_cue_count: int
    local_probe_count: int
    risky_count: int
    safe_count: int
    failed_risky_count: int
    success_rate: float


SCENARIOS = [
    FilterScenario("self_noisy_hidden", "self_noisy_hidden"),
    FilterScenario("world_noisy_hidden", "world_noisy_hidden"),
    FilterScenario("independent_hidden", "independent_hidden"),
    FilterScenario("irrelevant_control", "irrelevant_control"),
]

AGENTS = [
    "greedy_no_state",
    "safe_no_state",
    "channel_a_filter",
    "channel_b_filter",
    "task_local_probe",
    "learned_structure_selector",
    "oracle_observation",
]

CANDIDATE_POLICIES = [
    "greedy_no_state",
    "safe_no_state",
    "channel_a_filter",
    "channel_b_filter",
    "task_local_probe",
]


def stable_state_seed(seed: int, scenario: str, phase: str, episode: int) -> int:
    value = seed + episode * 1009
    for char in f"{scenario}:{phase}":
        value = (value * 131 + ord(char)) % (2**32)
    return value


def sample_state(
    scenario: FilterScenario,
    phase: str,
    episode: int,
    cfg: FilterConfig,
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

    return EpisodeState(
        scenario=scenario.name,
        channel_a_signal=channel_a_signal,
        channel_b_signal=channel_b_signal,
        channel_a_cues=tuple(noisy_cue(channel_a_signal, cfg.cue_accuracy, rng) for _ in range(cfg.evidence_samples)),
        channel_b_cues=tuple(noisy_cue(channel_b_signal, cfg.cue_accuracy, rng) for _ in range(cfg.evidence_samples)),
        step_success=step_success,
    )


def noisy_cue(value: bool, accuracy: float, rng: random.Random) -> bool:
    return value if rng.random() < accuracy else not value


def learn_training_stats(scenario: FilterScenario, cfg: FilterConfig) -> TrainingStats:
    states = [
        sample_state(scenario, "train", episode, cfg)
        for episode in range(cfg.training_episodes)
    ]
    marginal_success = statistics.fmean(
        1.0 if success else 0.0
        for state in states
        for success in state.step_success
    )
    channel_a_success = estimate_success_by_cue_count(states, "a", cfg)
    channel_b_success = estimate_success_by_cue_count(states, "b", cfg)
    preliminary = TrainingStats(
        scenario=scenario.name,
        selected_policy="unselected",
        marginal_success_probability=marginal_success,
        channel_a_success_by_count=tuple(channel_a_success),
        channel_b_success_by_count=tuple(channel_b_success),
        channel_a_training_reward=0.0,
        channel_b_training_reward=0.0,
        local_training_reward=0.0,
        greedy_training_reward=0.0,
        safe_training_reward=0.0,
    )
    training_rewards = {
        policy: mean_policy_reward(states, policy, preliminary, cfg)
        for policy in CANDIDATE_POLICIES
    }
    selected_policy = sorted(
        training_rewards,
        key=lambda policy: (-training_rewards[policy], policy),
    )[0]
    return TrainingStats(
        scenario=scenario.name,
        selected_policy=selected_policy,
        marginal_success_probability=marginal_success,
        channel_a_success_by_count=tuple(channel_a_success),
        channel_b_success_by_count=tuple(channel_b_success),
        channel_a_training_reward=training_rewards["channel_a_filter"],
        channel_b_training_reward=training_rewards["channel_b_filter"],
        local_training_reward=training_rewards["task_local_probe"],
        greedy_training_reward=training_rewards["greedy_no_state"],
        safe_training_reward=training_rewards["safe_no_state"],
    )


def estimate_success_by_cue_count(
    states: Sequence[EpisodeState],
    channel: str,
    cfg: FilterConfig,
) -> List[float]:
    successes = [PRIOR_TRUE for _ in range(cfg.evidence_samples + 1)]
    totals = [1.0 for _ in range(cfg.evidence_samples + 1)]
    for state in states:
        cues = state.channel_a_cues if channel == "a" else state.channel_b_cues
        cue_count = sum(1 for cue in cues if cue)
        successes[cue_count] += sum(1 for success in state.step_success if success)
        totals[cue_count] += len(state.step_success)
    return [successes[index] / totals[index] for index in range(cfg.evidence_samples + 1)]


def mean_policy_reward(
    states: Sequence[EpisodeState],
    policy: str,
    stats: TrainingStats,
    cfg: FilterConfig,
) -> float:
    return statistics.fmean(evaluate_policy(state, policy, stats, cfg)[0] for state in states)


def boundary_signature(scenario: FilterScenario, cfg: FilterConfig) -> Tuple[str, float, float]:
    states = [
        sample_state(scenario, "boundary", episode, cfg)
        for episode in range(cfg.training_episodes)
    ]
    effect_a_values = []
    effect_b_values = []
    for state in states:
        baseline = success_rate(state.step_success)
        effect_a_values.append(success_rate(intervene_channel_a(scenario, state).step_success) - baseline)
        effect_b_values.append(success_rate(intervene_channel_b(scenario, state).step_success) - baseline)
    effect_a = statistics.fmean(effect_a_values)
    effect_b = statistics.fmean(effect_b_values)
    if effect_a > 0.20 and effect_b < 0.05:
        return "agent_bounded_filter", effect_a, effect_b
    if effect_b > 0.20 and effect_a < 0.05:
        return "external_filter", effect_a, effect_b
    return "no_shared_boundary", effect_a, effect_b


def intervene_channel_a(scenario: FilterScenario, state: EpisodeState) -> EpisodeState:
    if scenario.mode == "self_noisy_hidden":
        return replace_step_success(state, True)
    return state


def intervene_channel_b(scenario: FilterScenario, state: EpisodeState) -> EpisodeState:
    if scenario.mode == "world_noisy_hidden":
        return replace_step_success(state, True)
    return state


def replace_step_success(state: EpisodeState, value: bool) -> EpisodeState:
    return EpisodeState(
        scenario=state.scenario,
        channel_a_signal=state.channel_a_signal,
        channel_b_signal=state.channel_b_signal,
        channel_a_cues=state.channel_a_cues,
        channel_b_cues=state.channel_b_cues,
        step_success=tuple(value for _ in state.step_success),
    )


def run_agent(
    scenario: FilterScenario,
    episode: int,
    agent: str,
    stats: TrainingStats,
    signature: str,
    cfg: FilterConfig,
) -> AgentResult:
    state = sample_state(scenario, "test", episode, cfg)
    policy = stats.selected_policy if agent == "learned_structure_selector" else agent
    total_reward, shared_cue_count, local_probe_count, risky_count, safe_count, failed_count, successes = evaluate_policy(
        state,
        policy,
        stats,
        cfg,
    )
    return AgentResult(
        scenario=scenario.name,
        agent=agent,
        selected_policy=stats.selected_policy,
        boundary_signature=signature,
        total_reward=total_reward,
        shared_cue_count=shared_cue_count,
        local_probe_count=local_probe_count,
        risky_count=risky_count,
        safe_count=safe_count,
        failed_risky_count=failed_count,
        success_rate=successes / cfg.horizon,
    )


def evaluate_policy(
    state: EpisodeState,
    policy: str,
    stats: TrainingStats,
    cfg: FilterConfig,
) -> Tuple[float, int, int, int, int, int, int]:
    total_reward = 0.0
    shared_cue_count = 0
    local_probe_count = 0
    risky_count = 0
    safe_count = 0
    failed_count = 0
    successes = 0

    shared_choice = None
    if policy == "channel_a_filter":
        total_reward -= cfg.shared_cue_cost
        shared_cue_count = cfg.evidence_samples
        probability = stats.channel_a_success_by_count[sum(1 for cue in state.channel_a_cues if cue)]
        shared_choice = "risky" if should_risk(probability) else "safe"
    elif policy == "channel_b_filter":
        total_reward -= cfg.shared_cue_cost
        shared_cue_count = cfg.evidence_samples
        probability = stats.channel_b_success_by_count[sum(1 for cue in state.channel_b_cues if cue)]
        shared_choice = "risky" if should_risk(probability) else "safe"
    elif policy == "greedy_no_state":
        shared_choice = "risky"
    elif policy == "safe_no_state":
        shared_choice = "safe"
    elif policy == "oracle_observation":
        shared_choice = None
    elif policy != "task_local_probe":
        raise ValueError(f"unknown policy: {policy}")

    for step, hidden_success in enumerate(state.step_success):
        if policy == "task_local_probe":
            total_reward -= cfg.local_probe_cost
            local_probe_count += 1
            choice = "risky" if hidden_success else "safe"
        elif policy == "oracle_observation":
            choice = "risky" if hidden_success else "safe"
        else:
            choice = str(shared_choice)

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

    return total_reward, shared_cue_count, local_probe_count, risky_count, safe_count, failed_count, successes


def should_risk(success_probability: float) -> bool:
    threshold = (SAFE_REWARD - RISKY_FAILURE_REWARD) / (RISKY_SUCCESS_REWARD - RISKY_FAILURE_REWARD)
    return success_probability >= threshold


def action_reward(choice: str, hidden_success: bool) -> Tuple[float, bool]:
    if choice == "safe":
        return SAFE_REWARD, True
    if hidden_success:
        return RISKY_SUCCESS_REWARD, True
    return RISKY_FAILURE_REWARD, False


def success_rate(step_success: Sequence[bool]) -> float:
    return sum(1 for success in step_success if success) / len(step_success)


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
                "boundary_signature": items[0].boundary_signature,
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
    training_rows: Sequence[TrainingStats],
    boundary_rows: Sequence[Dict[str, object]],
) -> List[Dict[str, object]]:
    rows = []
    for scenario in sorted({str(row["scenario"]) for row in summary_rows}):
        selected = training_for(training_rows, scenario).selected_policy
        boundary = next(row for row in boundary_rows if row["scenario"] == scenario)
        channel_a_reward = reward_for(summary_rows, scenario, "channel_a_filter")
        channel_b_reward = reward_for(summary_rows, scenario, "channel_b_filter")
        local_reward = reward_for(summary_rows, scenario, "task_local_probe")
        greedy_reward = reward_for(summary_rows, scenario, "greedy_no_state")
        selector_reward = reward_for(summary_rows, scenario, "learned_structure_selector")
        rows.append(
            {
                "scenario": scenario,
                "selected_policy": selected,
                "boundary_signature": boundary["boundary_signature"],
                "channel_a_reward": channel_a_reward,
                "channel_b_reward": channel_b_reward,
                "local_probe_reward": local_reward,
                "greedy_reward": greedy_reward,
                "selector_reward": selector_reward,
                "channel_a_minus_local": channel_a_reward - local_reward,
                "channel_b_minus_local": channel_b_reward - local_reward,
                "local_minus_best_channel": local_reward - max(channel_a_reward, channel_b_reward),
                "greedy_minus_best_filter": greedy_reward - max(channel_a_reward, channel_b_reward),
                "supports_learned_filter_prediction": scenario_supports_prediction(
                    scenario,
                    selected,
                    str(boundary["boundary_signature"]),
                    channel_a_reward,
                    channel_b_reward,
                    local_reward,
                    greedy_reward,
                ),
            }
        )
    return rows


def training_for(training_rows: Sequence[TrainingStats], scenario: str) -> TrainingStats:
    return next(row for row in training_rows if row.scenario == scenario)


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
    boundary: str,
    channel_a_reward: float,
    channel_b_reward: float,
    local_reward: float,
    greedy_reward: float,
) -> bool:
    if scenario == "self_noisy_hidden":
        return (
            selected_policy == "channel_a_filter"
            and boundary == "agent_bounded_filter"
            and channel_a_reward > local_reward
            and channel_a_reward > channel_b_reward + 40.0
        )
    if scenario == "world_noisy_hidden":
        return (
            selected_policy == "channel_b_filter"
            and boundary == "external_filter"
            and channel_b_reward > local_reward
            and channel_b_reward > channel_a_reward + 40.0
        )
    if scenario == "independent_hidden":
        return (
            selected_policy == "task_local_probe"
            and boundary == "no_shared_boundary"
            and local_reward > max(channel_a_reward, channel_b_reward) + 40.0
        )
    if scenario == "irrelevant_control":
        return (
            selected_policy == "greedy_no_state"
            and boundary == "no_shared_boundary"
            and greedy_reward > max(channel_a_reward, channel_b_reward)
        )
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: FilterConfig,
) -> Tuple[List[AgentResult], List[Dict[str, object]], List[TrainingStats], List[Dict[str, object]], List[Dict[str, object]]]:
    results = []
    training_rows = []
    boundary_rows = []
    for scenario in SCENARIOS:
        stats = learn_training_stats(scenario, cfg)
        signature, effect_a, effect_b = boundary_signature(scenario, cfg)
        training_rows.append(stats)
        boundary_rows.append(
            {
                "scenario": scenario.name,
                "boundary_signature": signature,
                "channel_a_intervention_effect": effect_a,
                "channel_b_intervention_effect": effect_b,
            }
        )
        for episode in range(cfg.episodes):
            for agent in AGENTS:
                results.append(run_agent(scenario, episode, agent, stats, signature, cfg))
    summary_rows = summarize(results)
    verdicts = verdict_rows(summary_rows, training_rows, boundary_rows)
    return results, summary_rows, training_rows, boundary_rows, verdicts


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
        "boundary_signature",
        "selector_reward",
        "local_probe_reward",
        "supports_learned_filter_prediction",
    ]
    rows = []
    for verdict in verdicts:
        rows.append(
            [
                str(verdict["scenario"]),
                str(verdict["selected_policy"]),
                str(verdict["boundary_signature"]),
                f"{float(verdict['selector_reward']):.3f}",
                f"{float(verdict['local_probe_reward']):.3f}",
                str(verdict["supports_learned_filter_prediction"]),
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


def parse_args() -> FilterConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=500)
    parser.add_argument("--training-episodes", type=int, default=800)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--horizon", type=int, default=8)
    parser.add_argument("--evidence-samples", type=int, default=7)
    parser.add_argument("--cue-accuracy", type=float, default=0.85)
    parser.add_argument("--shared-cue-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
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
    return FilterConfig(
        episodes=args.episodes,
        training_episodes=args.training_episodes,
        seed=args.seed,
        horizon=args.horizon,
        evidence_samples=args.evidence_samples,
        cue_accuracy=args.cue_accuracy,
        shared_cue_cost=args.shared_cue_cost,
        local_probe_cost=args.local_probe_cost,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    results, summary_rows, training_rows, boundary_rows, verdicts = run_experiment(cfg)
    summary_path = ARTIFACT_DIR / "learned_observation_filter_summary.csv"
    training_path = ARTIFACT_DIR / "learned_observation_filter_training.csv"
    boundary_path = ARTIFACT_DIR / "learned_observation_filter_boundary.csv"
    verdict_path = ARTIFACT_DIR / "learned_observation_filter_verdict.csv"
    results_path = ARTIFACT_DIR / "learned_observation_filter_results.json"
    write_csv(summary_path, summary_rows)
    write_csv(training_path, training_rows)
    write_csv(boundary_path, boundary_rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "training": [asdict(row) for row in training_rows],
                "boundary": boundary_rows,
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
    print(f"wrote {boundary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print_table(verdicts)
    return 0 if all(bool(row["supports_learned_filter_prediction"]) for row in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
