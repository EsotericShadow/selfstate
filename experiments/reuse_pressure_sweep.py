#!/usr/bin/env python3
"""Reuse-pressure sweep for self-state advantage.

The cross-context reuse experiment asks whether one persistent agent-state
estimate can transfer across several contexts. This sweep varies how many
contexts reuse the same hidden variable.

Prediction:

- shared self-state advantage should grow with the number of contexts only when
  the reused variable is agent-bounded;
- shared world-state should show the same reuse curve for external variables,
  which should not count as selfhood;
- task-local probing should win when hidden variables are independent;
- no-state greedy behavior should win when hidden state is irrelevant.
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


@dataclass(frozen=True)
class ContextProfile:
    name: str
    risky_success_reward: float
    risky_failure_reward: float
    safe_reward: float


CONTEXT_PROFILES = [
    ContextProfile("goal", 24.0, -16.0, 8.0),
    ContextProfile("option", 34.0, -30.0, 14.0),
    ContextProfile("commitment", 22.0, -18.0, 12.0),
    ContextProfile("adaptation", 28.0, -22.0, 11.0),
    ContextProfile("prediction", 18.0, -14.0, 7.0),
    ContextProfile("arbitration", 26.0, -20.0, 10.0),
]


@dataclass(frozen=True)
class SweepConfig:
    episodes: int = 500
    seed: int = 20260531
    max_contexts: int = len(CONTEXT_PROFILES)


@dataclass(frozen=True)
class SweepScenario:
    name: str
    mode: str


@dataclass(frozen=True)
class SweepState:
    scenario: str
    context_count: int
    self_signal: bool
    world_signal: bool
    local_success: Dict[str, bool]


@dataclass
class EpisodeResult:
    scenario: str
    context_count: int
    agent: str
    total_reward: float
    probe_count: int
    risky_count: int
    safe_count: int
    failed_risky_count: int
    success_rate: float


SCENARIOS = [
    SweepScenario("self_reuse", "self_reuse"),
    SweepScenario("world_reuse", "world_reuse"),
    SweepScenario("independent_hidden", "independent_hidden"),
    SweepScenario("irrelevant_control", "irrelevant_control"),
]


class BaseAgent:
    name = "base"

    def reset(self, scenario: SweepScenario) -> None:
        self.scenario = scenario
        self.self_estimate = True
        self.world_estimate = True

    def prepare(self, state: SweepState) -> float:
        return 0.0

    def choose(self, profile: ContextProfile, state: SweepState) -> Tuple[str, float]:
        raise NotImplementedError


class GreedyNoStateAgent(BaseAgent):
    name = "greedy_no_state"

    def choose(self, profile: ContextProfile, state: SweepState) -> Tuple[str, float]:
        return "risky", 0.0


class SafeNoStateAgent(BaseAgent):
    name = "safe_no_state"

    def choose(self, profile: ContextProfile, state: SweepState) -> Tuple[str, float]:
        return "safe", 0.0


class SharedSelfReuseAgent(BaseAgent):
    name = "shared_self_reuse"

    def prepare(self, state: SweepState) -> float:
        self.self_estimate = state.self_signal
        return -1.0

    def choose(self, profile: ContextProfile, state: SweepState) -> Tuple[str, float]:
        return ("risky" if self.self_estimate else "safe"), 0.0


class SharedWorldReuseAgent(BaseAgent):
    name = "shared_world_reuse"

    def prepare(self, state: SweepState) -> float:
        self.world_estimate = state.world_signal
        return -1.0

    def choose(self, profile: ContextProfile, state: SweepState) -> Tuple[str, float]:
        return ("risky" if self.world_estimate else "safe"), 0.0


class TaskLocalProbeAgent(BaseAgent):
    name = "task_local_probe"

    def choose(self, profile: ContextProfile, state: SweepState) -> Tuple[str, float]:
        return ("risky" if state.local_success[profile.name] else "safe"), -1.0


class OracleReuseAgent(BaseAgent):
    name = "oracle_reuse"

    def choose(self, profile: ContextProfile, state: SweepState) -> Tuple[str, float]:
        return ("risky" if state.local_success[profile.name] else "safe"), 0.0


AGENT_FACTORIES = [
    GreedyNoStateAgent,
    SafeNoStateAgent,
    SharedSelfReuseAgent,
    SharedWorldReuseAgent,
    TaskLocalProbeAgent,
    OracleReuseAgent,
]


def stable_state_seed(seed: int, scenario: str, context_count: int, episode: int) -> int:
    value = seed + episode * 1009 + context_count * 9176
    for char in scenario:
        value = (value * 131 + ord(char)) % (2**32)
    return value


def sample_state(scenario: SweepScenario, context_count: int, episode: int, cfg: SweepConfig) -> SweepState:
    rng = random.Random(stable_state_seed(cfg.seed, scenario.name, context_count, episode))
    profiles = CONTEXT_PROFILES[:context_count]
    if scenario.mode == "self_reuse":
        capability = rng.random() < 0.55
        return SweepState(
            scenario=scenario.name,
            context_count=context_count,
            self_signal=capability,
            world_signal=True,
            local_success={profile.name: capability for profile in profiles},
        )
    if scenario.mode == "world_reuse":
        gate = rng.random() < 0.55
        diagnostic = rng.random() < 0.55
        return SweepState(
            scenario=scenario.name,
            context_count=context_count,
            self_signal=diagnostic,
            world_signal=gate,
            local_success={profile.name: gate for profile in profiles},
        )
    if scenario.mode == "independent_hidden":
        local_success = {profile.name: rng.random() < 0.55 for profile in profiles}
        return SweepState(
            scenario=scenario.name,
            context_count=context_count,
            self_signal=local_success[profiles[0].name],
            world_signal=True,
            local_success=local_success,
        )
    if scenario.mode == "irrelevant_control":
        return SweepState(
            scenario=scenario.name,
            context_count=context_count,
            self_signal=True,
            world_signal=True,
            local_success={profile.name: True for profile in profiles},
        )
    raise ValueError(f"unknown scenario mode: {scenario.mode}")


def run_episode(agent_factory, scenario: SweepScenario, context_count: int, episode: int, cfg: SweepConfig) -> EpisodeResult:
    state = sample_state(scenario, context_count, episode, cfg)
    agent = agent_factory()
    agent.reset(scenario)
    total_reward = agent.prepare(state)
    probe_count = 1 if agent.name in {"shared_self_reuse", "shared_world_reuse"} else 0
    risky_count = 0
    safe_count = 0
    failed_risky_count = 0
    successes = 0

    for profile in CONTEXT_PROFILES[:context_count]:
        choice, cost = agent.choose(profile, state)
        total_reward += cost
        if cost < 0.0:
            probe_count += 1
        reward, success = context_reward(profile, choice, state.local_success[profile.name])
        total_reward += reward
        if choice == "risky":
            risky_count += 1
            if not success:
                failed_risky_count += 1
        else:
            safe_count += 1
        if success:
            successes += 1

    return EpisodeResult(
        scenario=scenario.name,
        context_count=context_count,
        agent=agent.name,
        total_reward=total_reward,
        probe_count=probe_count,
        risky_count=risky_count,
        safe_count=safe_count,
        failed_risky_count=failed_risky_count,
        success_rate=successes / context_count,
    )


def context_reward(profile: ContextProfile, choice: str, hidden_success: bool) -> Tuple[float, bool]:
    if choice == "safe":
        return profile.safe_reward, True
    if hidden_success:
        return profile.risky_success_reward, True
    return profile.risky_failure_reward, False


def summarize(results: Sequence[EpisodeResult]) -> List[Dict[str, object]]:
    grouped: Dict[Tuple[str, int, str], List[EpisodeResult]] = {}
    for result in results:
        grouped.setdefault((result.scenario, result.context_count, result.agent), []).append(result)
    rows = []
    for (scenario, context_count, agent), items in sorted(grouped.items()):
        rows.append(
            {
                "scenario": scenario,
                "context_count": context_count,
                "agent": agent,
                "episodes": len(items),
                "mean_total_reward": statistics.fmean(item.total_reward for item in items),
                "mean_probe_count": statistics.fmean(item.probe_count for item in items),
                "mean_risky_count": statistics.fmean(item.risky_count for item in items),
                "mean_safe_count": statistics.fmean(item.safe_count for item in items),
                "mean_failed_risky_count": statistics.fmean(item.failed_risky_count for item in items),
                "mean_success_rate": statistics.fmean(item.success_rate for item in items),
            }
        )
    return rows


def pressure_rows(summary_rows: Sequence[Dict[str, object]], cfg: SweepConfig) -> List[Dict[str, object]]:
    rows = []
    for scenario in sorted({str(row["scenario"]) for row in summary_rows}):
        first = pressure_point(summary_rows, scenario, 1)
        last = pressure_point(summary_rows, scenario, cfg.max_contexts)
        rows.append(
            {
                "scenario": scenario,
                "context_range": f"1-{cfg.max_contexts}",
                "best_at_max_contexts": last["best_non_oracle_agent"],
                "shared_self_minus_local_at_1": first["shared_self_minus_local"],
                "shared_self_minus_local_at_max": last["shared_self_minus_local"],
                "shared_world_minus_local_at_max": last["shared_world_minus_local"],
                "local_minus_shared_self_at_max": -last["shared_self_minus_local"],
                "greedy_minus_shared_self_at_max": last["greedy_minus_shared_self"],
                "supports_pressure_prediction": scenario_supports_pressure(scenario, first, last, summary_rows, cfg.max_contexts),
            }
        )
    return rows


def pressure_point(summary_rows: Sequence[Dict[str, object]], scenario: str, context_count: int) -> Dict[str, object]:
    rows = [row for row in summary_rows if row["scenario"] == scenario and int(row["context_count"]) == context_count]
    non_oracle = [row for row in rows if row["agent"] != "oracle_reuse"]
    best = sorted(non_oracle, key=lambda row: (-float(row["mean_total_reward"]), str(row["agent"])))[0]
    greedy = row_for(rows, "greedy_no_state")
    self_reuse = row_for(rows, "shared_self_reuse")
    world_reuse = row_for(rows, "shared_world_reuse")
    task_local = row_for(rows, "task_local_probe")
    return {
        "scenario": scenario,
        "context_count": context_count,
        "best_non_oracle_agent": best["agent"],
        "greedy_reward": greedy["mean_total_reward"],
        "shared_self_reward": self_reuse["mean_total_reward"],
        "shared_world_reward": world_reuse["mean_total_reward"],
        "task_local_reward": task_local["mean_total_reward"],
        "shared_self_minus_local": float(self_reuse["mean_total_reward"]) - float(task_local["mean_total_reward"]),
        "shared_world_minus_local": float(world_reuse["mean_total_reward"]) - float(task_local["mean_total_reward"]),
        "greedy_minus_shared_self": float(greedy["mean_total_reward"]) - float(self_reuse["mean_total_reward"]),
    }


def row_for(rows: Sequence[Dict[str, object]], agent: str) -> Dict[str, object]:
    return next(row for row in rows if row["agent"] == agent)


def scenario_supports_pressure(
    scenario: str,
    first: Dict[str, object],
    last: Dict[str, object],
    summary_rows: Sequence[Dict[str, object]],
    max_contexts: int,
) -> bool:
    points = [pressure_point(summary_rows, scenario, count) for count in range(1, max_contexts + 1)]
    if scenario == "self_reuse":
        return (
            last["best_non_oracle_agent"] == "shared_self_reuse"
            and float(last["shared_self_minus_local"]) > float(first["shared_self_minus_local"]) + 3.0
            and all(float(point["shared_self_minus_local"]) >= -0.01 for point in points)
            and float(last["shared_self_reward"]) > float(last["shared_world_reward"]) + 20.0
        )
    if scenario == "world_reuse":
        return (
            last["best_non_oracle_agent"] == "shared_world_reuse"
            and float(last["shared_world_minus_local"]) > float(first["shared_world_minus_local"]) + 3.0
            and float(last["shared_world_reward"]) > float(last["shared_self_reward"]) + 20.0
        )
    if scenario == "independent_hidden":
        return (
            last["best_non_oracle_agent"] == "task_local_probe"
            and -float(last["shared_self_minus_local"]) > 25.0
        )
    if scenario == "irrelevant_control":
        return (
            last["best_non_oracle_agent"] == "greedy_no_state"
            and float(last["greedy_minus_shared_self"]) > 0.5
        )
    return False


def write_csv(path: Path, rows: Sequence[Dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_outputs(summary_rows: Sequence[Dict[str, object]], pressure: Sequence[Dict[str, object]], cfg: SweepConfig) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    summary_path = ARTIFACT_DIR / "reuse_pressure_sweep_summary.csv"
    pressure_path = ARTIFACT_DIR / "reuse_pressure_sweep_verdict.csv"
    json_path = ARTIFACT_DIR / "reuse_pressure_sweep_results.json"
    write_csv(summary_path, summary_rows)
    write_csv(pressure_path, pressure)
    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "summary": list(summary_rows),
                "verdict": list(pressure),
            },
            handle,
            indent=2,
        )
        handle.write("\n")
    print(f"wrote {summary_path}")
    print(f"wrote {pressure_path}")
    print(f"wrote {json_path}")


def print_verdict(rows: Sequence[Dict[str, object]]) -> None:
    columns = [
        "scenario",
        "best_at_max_contexts",
        "shared_self_minus_local_at_1",
        "shared_self_minus_local_at_max",
        "shared_world_minus_local_at_max",
        "supports_pressure_prediction",
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
    parser.add_argument("--episodes", type=int, default=SweepConfig.episodes)
    parser.add_argument("--seed", type=int, default=SweepConfig.seed)
    parser.add_argument("--max-contexts", type=int, default=SweepConfig.max_contexts)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.max_contexts < 1 or args.max_contexts > len(CONTEXT_PROFILES):
        raise ValueError(f"--max-contexts must be between 1 and {len(CONTEXT_PROFILES)}")
    cfg = SweepConfig(episodes=args.episodes, seed=args.seed, max_contexts=args.max_contexts)
    results = [
        run_episode(agent_factory, scenario, context_count, episode, cfg)
        for scenario in SCENARIOS
        for context_count in range(1, cfg.max_contexts + 1)
        for episode in range(cfg.episodes)
        for agent_factory in AGENT_FACTORIES
    ]
    summary_rows = summarize(results)
    pressure = pressure_rows(summary_rows, cfg)
    write_outputs(summary_rows, pressure, cfg)
    print_verdict(pressure)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
