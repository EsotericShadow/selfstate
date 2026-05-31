#!/usr/bin/env python3
"""Goal-formation test for self-state as a feasibility filter.

The agent chooses a goal before acting. Some goals are more valuable but require
hidden agent capabilities. Others depend on hidden world opportunities. The
question is whether representing "what I can do" changes which goals should be
formed, not merely how actions are executed after a goal is fixed.
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
FAILURE_REWARD = -14.0
SELF_INSPECT_COST = 0.75
WORLD_INSPECT_COST = 0.75


@dataclass(frozen=True)
class GoalConfig:
    episodes: int = 500
    seed: int = 20260530


@dataclass(frozen=True)
class Goal:
    name: str
    reward: float
    requires_strength: bool = False
    requires_precision: bool = False
    gate: Optional[str] = None


@dataclass(frozen=True)
class GoalState:
    strength: bool
    precision: bool
    gates: Mapping[str, bool]


@dataclass
class EpisodeResult:
    scenario: str
    agent: str
    goal: str
    success: bool
    reward: float
    inspect_self: bool
    inspect_world: bool


GOALS = [
    Goal("routine", 8.0),
    Goal("heavy", 18.0, requires_strength=True, gate="heavy_open"),
    Goal("delicate", 18.0, requires_precision=True, gate="delicate_open"),
    Goal("flagship", 34.0, requires_strength=True, requires_precision=True, gate="flagship_open"),
]


SCENARIOS = [
    "capability_relevant",
    "world_relevant",
    "mixed_relevant",
    "irrelevant_control",
]


class BaseAgent:
    name = "base"

    def choose_goal(self, scenario: str, state: GoalState) -> Tuple[Goal, bool, bool]:
        raise NotImplementedError


class PayoffGreedyAgent(BaseAgent):
    name = "payoff_greedy"

    def choose_goal(self, scenario: str, state: GoalState) -> Tuple[Goal, bool, bool]:
        return max(GOALS, key=lambda goal: (goal.reward, goal.name)), False, False


class FixedSafeAgent(BaseAgent):
    name = "fixed_safe_goal"

    def choose_goal(self, scenario: str, state: GoalState) -> Tuple[Goal, bool, bool]:
        return goal_by_name("routine"), False, False


class SelfStateAblationAgent(BaseAgent):
    name = "self_state_ablation"

    def choose_goal(self, scenario: str, state: GoalState) -> Tuple[Goal, bool, bool]:
        return max(GOALS, key=lambda goal: (goal.reward, goal.name)), True, False


class SelfCapabilitySelectorAgent(BaseAgent):
    name = "self_capability_selector"

    def choose_goal(self, scenario: str, state: GoalState) -> Tuple[Goal, bool, bool]:
        feasible = [
            goal
            for goal in GOALS
            if capability_satisfied(goal, strength=state.strength, precision=state.precision)
        ]
        return max(feasible, key=lambda goal: (goal.reward, goal.name)), True, False


class WorldOpportunitySelectorAgent(BaseAgent):
    name = "world_opportunity_selector"

    def choose_goal(self, scenario: str, state: GoalState) -> Tuple[Goal, bool, bool]:
        open_goals = [goal for goal in GOALS if gate_satisfied(goal, state.gates)]
        return max(open_goals, key=lambda goal: (goal.reward, goal.name)), False, True


class SelfWorldGoalSelectorAgent(BaseAgent):
    name = "self_world_goal_selector"

    def choose_goal(self, scenario: str, state: GoalState) -> Tuple[Goal, bool, bool]:
        possible = [
            goal
            for goal in GOALS
            if capability_satisfied(goal, strength=state.strength, precision=state.precision)
            and gate_satisfied(goal, state.gates)
        ]
        return max(possible, key=lambda goal: (goal.reward, goal.name)), True, True


class OracleGoalSelectorAgent(BaseAgent):
    name = "oracle_goal_selector"

    def choose_goal(self, scenario: str, state: GoalState) -> Tuple[Goal, bool, bool]:
        possible = [
            goal
            for goal in GOALS
            if capability_satisfied(goal, strength=state.strength, precision=state.precision)
            and gate_satisfied(goal, state.gates)
        ]
        return max(possible, key=lambda goal: (goal.reward, goal.name)), False, False


AGENT_FACTORIES = [
    PayoffGreedyAgent,
    FixedSafeAgent,
    SelfStateAblationAgent,
    SelfCapabilitySelectorAgent,
    WorldOpportunitySelectorAgent,
    SelfWorldGoalSelectorAgent,
    OracleGoalSelectorAgent,
]


def goal_by_name(name: str) -> Goal:
    return next(goal for goal in GOALS if goal.name == name)


def capability_satisfied(goal: Goal, strength: bool, precision: bool) -> bool:
    if goal.requires_strength and not strength:
        return False
    if goal.requires_precision and not precision:
        return False
    return True


def gate_satisfied(goal: Goal, gates: Mapping[str, bool]) -> bool:
    if goal.gate is None:
        return True
    return gates[goal.gate]


def goal_success(goal: Goal, state: GoalState) -> bool:
    return capability_satisfied(goal, state.strength, state.precision) and gate_satisfied(goal, state.gates)


def sample_state(scenario: str, rng: random.Random) -> GoalState:
    if scenario == "capability_relevant":
        strength = rng.random() < 0.55
        precision = rng.random() < 0.55
        gates = {"heavy_open": True, "delicate_open": True, "flagship_open": True}
    elif scenario == "world_relevant":
        strength = True
        precision = True
        gates = sample_gates(rng)
    elif scenario == "mixed_relevant":
        strength = rng.random() < 0.55
        precision = rng.random() < 0.55
        gates = sample_gates(rng)
    elif scenario == "irrelevant_control":
        strength = True
        precision = True
        gates = {"heavy_open": True, "delicate_open": True, "flagship_open": True}
    else:
        raise ValueError(f"unknown scenario: {scenario}")
    return GoalState(strength=strength, precision=precision, gates=gates)


def sample_gates(rng: random.Random) -> Dict[str, bool]:
    return {
        "heavy_open": rng.random() < 0.70,
        "delicate_open": rng.random() < 0.70,
        "flagship_open": rng.random() < 0.45,
    }


def stable_state_seed(seed: int, scenario: str, episode: int) -> int:
    value = seed + episode * 1009
    for char in scenario:
        value = (value * 131 + ord(char)) % (2**32)
    return value


def run_episode(agent_factory, scenario: str, episode: int, cfg: GoalConfig) -> EpisodeResult:
    rng = random.Random(stable_state_seed(cfg.seed, scenario, episode))
    state = sample_state(scenario, rng)
    agent = agent_factory()
    goal, inspect_self, inspect_world = agent.choose_goal(scenario, state)
    success = goal_success(goal, state)
    reward = goal.reward if success else FAILURE_REWARD
    if inspect_self:
        reward -= SELF_INSPECT_COST
    if inspect_world:
        reward -= WORLD_INSPECT_COST
    return EpisodeResult(
        scenario=scenario,
        agent=agent.name,
        goal=goal.name,
        success=success,
        reward=reward,
        inspect_self=inspect_self,
        inspect_world=inspect_world,
    )


def summarize(results: Sequence[EpisodeResult]) -> List[Dict[str, object]]:
    grouped: Dict[Tuple[str, str], List[EpisodeResult]] = {}
    for result in results:
        grouped.setdefault((result.scenario, result.agent), []).append(result)
    rows = []
    for (scenario, agent), items in sorted(grouped.items()):
        goal_counts = {goal.name: sum(1 for item in items if item.goal == goal.name) for goal in GOALS}
        rows.append(
            {
                "scenario": scenario,
                "agent": agent,
                "episodes": len(items),
                "success_rate": rate(item.success for item in items),
                "mean_reward": statistics.fmean(item.reward for item in items),
                "inspect_self_rate": rate(item.inspect_self for item in items),
                "inspect_world_rate": rate(item.inspect_world for item in items),
                "routine_rate": goal_counts["routine"] / len(items),
                "heavy_rate": goal_counts["heavy"] / len(items),
                "delicate_rate": goal_counts["delicate"] / len(items),
                "flagship_rate": goal_counts["flagship"] / len(items),
            }
        )
    return rows


def verdict_rows(summary_rows: Sequence[Dict[str, object]]) -> List[Dict[str, object]]:
    rows = []
    for scenario in sorted({str(row["scenario"]) for row in summary_rows}):
        scenario_rows = [row for row in summary_rows if row["scenario"] == scenario]
        non_oracle = [row for row in scenario_rows if row["agent"] != "oracle_goal_selector"]
        best = sorted(non_oracle, key=lambda row: (-float(row["mean_reward"]), str(row["agent"])))[0]
        greedy = row_for(scenario_rows, "payoff_greedy")
        self_selector = row_for(scenario_rows, "self_capability_selector")
        world_selector = row_for(scenario_rows, "world_opportunity_selector")
        self_world = row_for(scenario_rows, "self_world_goal_selector")
        rows.append(
            {
                "scenario": scenario,
                "best_non_oracle_agent": best["agent"],
                "best_non_oracle_reward": best["mean_reward"],
                "greedy_reward": greedy["mean_reward"],
                "self_selector_reward": self_selector["mean_reward"],
                "world_selector_reward": world_selector["mean_reward"],
                "self_world_reward": self_world["mean_reward"],
                "self_minus_greedy": float(self_selector["mean_reward"]) - float(greedy["mean_reward"]),
                "world_minus_greedy": float(world_selector["mean_reward"]) - float(greedy["mean_reward"]),
                "self_world_minus_greedy": float(self_world["mean_reward"]) - float(greedy["mean_reward"]),
                "supports_boundary": scenario_supports_boundary(scenario, best, greedy, self_selector, world_selector, self_world),
            }
        )
    return rows


def row_for(rows: Sequence[Dict[str, object]], agent: str) -> Dict[str, object]:
    return next(row for row in rows if row["agent"] == agent)


def scenario_supports_boundary(
    scenario: str,
    best: Dict[str, object],
    greedy: Dict[str, object],
    self_selector: Dict[str, object],
    world_selector: Dict[str, object],
    self_world: Dict[str, object],
) -> bool:
    if scenario == "capability_relevant":
        return (
            best["agent"] == "self_capability_selector"
            and float(self_selector["mean_reward"]) > float(greedy["mean_reward"]) + 10.0
            and float(self_selector["mean_reward"]) > float(world_selector["mean_reward"]) + 5.0
        )
    if scenario == "world_relevant":
        return (
            best["agent"] == "world_opportunity_selector"
            and float(world_selector["mean_reward"]) > float(self_selector["mean_reward"]) + 10.0
        )
    if scenario == "mixed_relevant":
        return (
            best["agent"] == "self_world_goal_selector"
            and float(self_world["mean_reward"]) > float(self_selector["mean_reward"]) + 3.0
            and float(self_world["mean_reward"]) > float(world_selector["mean_reward"]) + 3.0
        )
    if scenario == "irrelevant_control":
        return (
            best["agent"] == "payoff_greedy"
            and float(greedy["mean_reward"]) > float(self_selector["mean_reward"])
            and float(greedy["mean_reward"]) > float(world_selector["mean_reward"])
        )
    return False


def rate(values: Iterable[bool]) -> float:
    values = list(values)
    return sum(1 for value in values if value) / len(values)


def write_csv(path: Path, rows: Sequence[Dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_outputs(summary_rows: Sequence[Dict[str, object]], verdict: Sequence[Dict[str, object]], cfg: GoalConfig) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    summary_path = ARTIFACT_DIR / "goal_formation_under_capability_summary.csv"
    verdict_path = ARTIFACT_DIR / "goal_formation_under_capability_verdict.csv"
    json_path = ARTIFACT_DIR / "goal_formation_under_capability_results.json"
    write_csv(summary_path, summary_rows)
    write_csv(verdict_path, verdict)
    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "summary": list(summary_rows),
                "verdict": list(verdict),
            },
            handle,
            indent=2,
        )
        handle.write("\n")
    print(f"wrote {summary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {json_path}")


def print_verdict(rows: Sequence[Dict[str, object]]) -> None:
    columns = [
        "scenario",
        "best_non_oracle_agent",
        "greedy_reward",
        "self_selector_reward",
        "world_selector_reward",
        "self_world_reward",
        "supports_boundary",
    ]
    widths = {
        column: max(len(column), *(len(format_value(row[column])) for row in rows))
        for column in columns
    }
    print(" | ".join(column.ljust(widths[column]) for column in columns))
    print("-+-".join("-" * widths[column] for column in columns))
    for row in rows:
        print(" | ".join(format_value(row[column]).ljust(widths[column]) for column in columns))


def format_value(value: object) -> str:
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=GoalConfig.episodes)
    parser.add_argument("--seed", type=int, default=GoalConfig.seed)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cfg = GoalConfig(episodes=args.episodes, seed=args.seed)
    results = [
        run_episode(agent_factory, scenario, episode, cfg)
        for scenario in SCENARIOS
        for episode in range(cfg.episodes)
        for agent_factory in AGENT_FACTORIES
    ]
    summary_rows = summarize(results)
    verdict = verdict_rows(summary_rows)
    write_outputs(summary_rows, verdict, cfg)
    print_verdict(verdict)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
