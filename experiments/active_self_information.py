#!/usr/bin/env python3
"""Active information-seeking test for self-state.

This experiment asks whether an agent should actively inspect agent-state when
agent-state is control relevant. It separates that from hidden world-state and
irrelevant internal diagnostics.

The learned agent is a bandit over information-gathering plans. It is not told
which plan is "self"; it only receives reward after choosing what to inspect and
then acting under partial observability.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


ARTIFACT_DIR = Path("artifacts")
CHANNELS = ("agent", "world", "diagnostic")
PLANS: Tuple[Tuple[str, ...], ...] = (
    (),
    ("agent",),
    ("world",),
    ("diagnostic",),
    ("agent", "world"),
    ("agent", "diagnostic"),
    ("world", "diagnostic"),
    ("agent", "world", "diagnostic"),
)
PLAN_NAMES = {
    (): "none",
    ("agent",): "inspect_agent",
    ("world",): "inspect_world",
    ("diagnostic",): "inspect_diagnostic",
    ("agent", "world"): "inspect_agent_world",
    ("agent", "diagnostic"): "inspect_agent_diagnostic",
    ("world", "diagnostic"): "inspect_world_diagnostic",
    ("agent", "world", "diagnostic"): "inspect_all",
}
EXPECTED_BEST_PLAN = {
    "agent_relevant": "inspect_agent",
    "world_relevant": "inspect_world",
    "both_relevant": "inspect_agent_world",
    "irrelevant_control": "none",
}


@dataclass(frozen=True)
class InfoConfig:
    replicates: int = 300
    bandit_episodes: int = 1000
    value_samples: int = 4000
    final_window: int = 200
    inspect_cost: float = 1.0
    epsilon_start: float = 0.28
    epsilon_floor: float = 0.03
    seed: int = 20260530


@dataclass(frozen=True)
class HiddenState:
    agent_strong: bool
    world_open: bool
    diagnostic_on: bool


@dataclass
class PlanValueRow:
    scenario: str
    plan: str
    mean_reward: float
    inspect_agent: bool
    inspect_world: bool
    inspect_diagnostic: bool
    expected_best_plan: bool


@dataclass
class BanditRow:
    scenario: str
    expected_best_plan: str
    bandit_top_plan: str
    expected_best_final_rate: float
    agent_inspection_final_rate: float
    world_inspection_final_rate: float
    diagnostic_inspection_final_rate: float
    mean_reward_last_window: float
    supports_boundary: bool


def plan_name(plan: Tuple[str, ...]) -> str:
    return PLAN_NAMES[plan]


def sample_hidden(rng: random.Random) -> HiddenState:
    return HiddenState(
        agent_strong=rng.random() < 0.5,
        world_open=rng.random() < 0.5,
        diagnostic_on=rng.random() < 0.5,
    )


def exploit_reward(scenario: str, state: HiddenState) -> float:
    if scenario == "agent_relevant":
        return 10.0 if state.agent_strong else -20.0
    if scenario == "world_relevant":
        return 10.0 if state.world_open else -20.0
    if scenario == "both_relevant":
        return 16.0 if state.agent_strong and state.world_open else -20.0
    if scenario == "irrelevant_control":
        return 6.0
    raise ValueError(f"unknown scenario: {scenario}")


def conserve_reward(scenario: str, state: HiddenState) -> float:
    return 2.0


def states_consistent_with(observations: Mapping[str, bool]) -> List[HiddenState]:
    states = []
    for agent_strong in [False, True]:
        if "agent" in observations and observations["agent"] != agent_strong:
            continue
        for world_open in [False, True]:
            if "world" in observations and observations["world"] != world_open:
                continue
            for diagnostic_on in [False, True]:
                if "diagnostic" in observations and observations["diagnostic"] != diagnostic_on:
                    continue
                states.append(
                    HiddenState(
                        agent_strong=agent_strong,
                        world_open=world_open,
                        diagnostic_on=diagnostic_on,
                    )
                )
    return states


def choose_action(scenario: str, observations: Mapping[str, bool]) -> str:
    possible_states = states_consistent_with(observations)
    expected_exploit = statistics.fmean(exploit_reward(scenario, state) for state in possible_states)
    expected_conserve = statistics.fmean(conserve_reward(scenario, state) for state in possible_states)
    return "exploit" if expected_exploit > expected_conserve else "conserve"


def observe_channels(plan: Tuple[str, ...], state: HiddenState) -> Dict[str, bool]:
    observations = {}
    for channel in plan:
        if channel == "agent":
            observations[channel] = state.agent_strong
        elif channel == "world":
            observations[channel] = state.world_open
        elif channel == "diagnostic":
            observations[channel] = state.diagnostic_on
        else:
            raise ValueError(f"unknown channel: {channel}")
    return observations


def run_episode(scenario: str, plan: Tuple[str, ...], rng: random.Random, inspect_cost: float) -> float:
    state = sample_hidden(rng)
    observations = observe_channels(plan, state)
    action = choose_action(scenario, observations)
    if action == "exploit":
        reward = exploit_reward(scenario, state)
    else:
        reward = conserve_reward(scenario, state)
    return reward - inspect_cost * len(plan)


def estimate_plan_values(scenario: str, cfg: InfoConfig) -> List[PlanValueRow]:
    rows = []
    expected_best = EXPECTED_BEST_PLAN[scenario]
    for plan in PLANS:
        rng = random.Random(stable_seed(cfg.seed, scenario, plan_name(plan), "value"))
        rewards = [run_episode(scenario, plan, rng, cfg.inspect_cost) for _ in range(cfg.value_samples)]
        rows.append(
            PlanValueRow(
                scenario=scenario,
                plan=plan_name(plan),
                mean_reward=statistics.fmean(rewards),
                inspect_agent="agent" in plan,
                inspect_world="world" in plan,
                inspect_diagnostic="diagnostic" in plan,
                expected_best_plan=plan_name(plan) == expected_best,
            )
        )
    return rows


def run_bandit_replicate(scenario: str, replicate: int, cfg: InfoConfig) -> Tuple[List[str], List[float]]:
    rng = random.Random(stable_seed(cfg.seed, scenario, str(replicate), "bandit"))
    q_values = {plan: 0.0 for plan in PLANS}
    counts = {plan: 0 for plan in PLANS}
    chosen_plans = []
    rewards = []
    for episode in range(cfg.bandit_episodes):
        epsilon = max(
            cfg.epsilon_floor,
            cfg.epsilon_start * (1.0 - episode / max(1, cfg.bandit_episodes - 1)),
        )
        if rng.random() < epsilon:
            plan = rng.choice(PLANS)
        else:
            best_value = max(q_values.values())
            best_plans = [candidate for candidate, value in q_values.items() if value == best_value]
            plan = rng.choice(best_plans)
        reward = run_episode(scenario, plan, rng, cfg.inspect_cost)
        counts[plan] += 1
        q_values[plan] += (reward - q_values[plan]) / counts[plan]
        chosen_plans.append(plan_name(plan))
        rewards.append(reward)
    return chosen_plans, rewards


def summarize_bandit(scenario: str, cfg: InfoConfig) -> BanditRow:
    final_choices = []
    final_rewards = []
    for replicate in range(cfg.replicates):
        choices, rewards = run_bandit_replicate(scenario, replicate, cfg)
        final_choices.extend(choices[-cfg.final_window :])
        final_rewards.extend(rewards[-cfg.final_window :])
    expected = EXPECTED_BEST_PLAN[scenario]
    plan_counts = {plan_name(plan): final_choices.count(plan_name(plan)) for plan in PLANS}
    top_plan = max(plan_counts, key=lambda name: (plan_counts[name], name))
    expected_rate = plan_counts[expected] / len(final_choices)
    agent_rate = rate(plan_has_channel(choice, "agent") for choice in final_choices)
    world_rate = rate(plan_has_channel(choice, "world") for choice in final_choices)
    diagnostic_rate = rate(plan_has_channel(choice, "diagnostic") for choice in final_choices)
    return BanditRow(
        scenario=scenario,
        expected_best_plan=expected,
        bandit_top_plan=top_plan,
        expected_best_final_rate=expected_rate,
        agent_inspection_final_rate=agent_rate,
        world_inspection_final_rate=world_rate,
        diagnostic_inspection_final_rate=diagnostic_rate,
        mean_reward_last_window=statistics.fmean(final_rewards),
        supports_boundary=boundary_supported(
            scenario,
            top_plan,
            expected_rate,
            agent_rate,
            world_rate,
            diagnostic_rate,
        ),
    )


def plan_has_channel(plan: str, channel: str) -> bool:
    if plan == "none":
        return False
    return channel in plan.split("_")


def boundary_supported(
    scenario: str,
    top_plan: str,
    expected_rate: float,
    agent_rate: float,
    world_rate: float,
    diagnostic_rate: float,
) -> bool:
    if top_plan != EXPECTED_BEST_PLAN[scenario] or expected_rate < 0.55:
        return False
    if scenario == "agent_relevant":
        return agent_rate > 0.65 and world_rate < 0.25 and diagnostic_rate < 0.20
    if scenario == "world_relevant":
        return world_rate > 0.65 and agent_rate < 0.25 and diagnostic_rate < 0.20
    if scenario == "both_relevant":
        return agent_rate > 0.65 and world_rate > 0.65 and diagnostic_rate < 0.25
    if scenario == "irrelevant_control":
        return agent_rate < 0.25 and world_rate < 0.25 and diagnostic_rate < 0.20
    return False


def rate(values: Iterable[bool]) -> float:
    values = list(values)
    return sum(1 for value in values if value) / len(values)


def stable_seed(seed: int, *parts: str) -> int:
    value = seed
    for part in parts:
        for char in part:
            value = (value * 131 + ord(char)) % (2**32)
    return value


def write_csv(path: Path, rows: Sequence[object]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = list(asdict(rows[0]).keys())
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def write_outputs(plan_rows: Sequence[PlanValueRow], bandit_rows: Sequence[BanditRow], cfg: InfoConfig) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    plan_path = ARTIFACT_DIR / "active_self_information_plan_values.csv"
    bandit_path = ARTIFACT_DIR / "active_self_information_bandit_summary.csv"
    json_path = ARTIFACT_DIR / "active_self_information_results.json"
    write_csv(plan_path, plan_rows)
    write_csv(bandit_path, bandit_rows)
    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "plan_values": [asdict(row) for row in plan_rows],
                "bandit_summary": [asdict(row) for row in bandit_rows],
            },
            handle,
            indent=2,
        )
        handle.write("\n")
    print(f"wrote {plan_path}")
    print(f"wrote {bandit_path}")
    print(f"wrote {json_path}")


def print_summary(rows: Sequence[BanditRow]) -> None:
    columns = [
        "scenario",
        "expected_best_plan",
        "bandit_top_plan",
        "expected_best_final_rate",
        "agent_inspection_final_rate",
        "world_inspection_final_rate",
        "diagnostic_inspection_final_rate",
        "supports_boundary",
    ]
    dict_rows = [asdict(row) for row in rows]
    widths = {
        column: max(len(column), *(len(format_value(row[column])) for row in dict_rows))
        for column in columns
    }
    print(" | ".join(column.ljust(widths[column]) for column in columns))
    print("-+-".join("-" * widths[column] for column in columns))
    for row in dict_rows:
        print(" | ".join(format_value(row[column]).ljust(widths[column]) for column in columns))


def format_value(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replicates", type=int, default=InfoConfig.replicates)
    parser.add_argument("--bandit-episodes", type=int, default=InfoConfig.bandit_episodes)
    parser.add_argument("--value-samples", type=int, default=InfoConfig.value_samples)
    parser.add_argument("--final-window", type=int, default=InfoConfig.final_window)
    parser.add_argument("--inspect-cost", type=float, default=InfoConfig.inspect_cost)
    parser.add_argument("--seed", type=int, default=InfoConfig.seed)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cfg = InfoConfig(
        replicates=args.replicates,
        bandit_episodes=args.bandit_episodes,
        value_samples=args.value_samples,
        final_window=args.final_window,
        inspect_cost=args.inspect_cost,
        seed=args.seed,
    )
    scenarios = ["agent_relevant", "world_relevant", "both_relevant", "irrelevant_control"]
    plan_rows: List[PlanValueRow] = []
    bandit_rows: List[BanditRow] = []
    for scenario in scenarios:
        plan_rows.extend(estimate_plan_values(scenario, cfg))
        bandit_rows.append(summarize_bandit(scenario, cfg))
    write_outputs(plan_rows, bandit_rows, cfg)
    print_summary(bandit_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
