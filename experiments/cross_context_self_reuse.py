#!/usr/bin/env python3
"""Cross-context self-state reuse test.

Several earlier experiments show that agent-state can help inside one pressure:
action-effect prediction, goal feasibility, option preservation, or arbitration.
This experiment asks whether one persistent agent-state abstraction is useful
because it is reused across those contexts.

The boundary controls are strict:

- if the reused hidden variable is external, a world-state abstraction should win;
- if each context has an independent hidden variable, local probing should win;
- if all risky actions are feasible, no state abstraction should win.
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
CONTEXTS = ("goal", "option", "commitment")


@dataclass(frozen=True)
class ReuseConfig:
    episodes: int = 500
    seed: int = 20260531


@dataclass(frozen=True)
class ReuseScenario:
    name: str
    mode: str


@dataclass(frozen=True)
class EpisodeState:
    scenario: str
    self_signal: bool
    world_signal: bool
    local_success: Dict[str, bool]


@dataclass
class EpisodeResult:
    scenario: str
    agent: str
    total_reward: float
    probe_count: int
    shared_probe_count: int
    local_probe_count: int
    risky_count: int
    safe_count: int
    failed_risky_count: int
    success_rate: float


SCENARIOS = [
    ReuseScenario("self_reuse", "self_reuse"),
    ReuseScenario("world_reuse", "world_reuse"),
    ReuseScenario("independent_hidden", "independent_hidden"),
    ReuseScenario("irrelevant_control", "irrelevant_control"),
]


class BaseAgent:
    name = "base"

    def reset(self, scenario: ReuseScenario) -> None:
        self.scenario = scenario
        self.self_estimate = True
        self.world_estimate = True

    def prepare(self, state: EpisodeState) -> float:
        return 0.0

    def choose(self, context: str, state: EpisodeState) -> Tuple[str, float, str]:
        raise NotImplementedError


class GreedyNoStateAgent(BaseAgent):
    name = "greedy_no_state"

    def choose(self, context: str, state: EpisodeState) -> Tuple[str, float, str]:
        return "risky", 0.0, "none"


class SafeNoStateAgent(BaseAgent):
    name = "safe_no_state"

    def choose(self, context: str, state: EpisodeState) -> Tuple[str, float, str]:
        return "safe", 0.0, "none"


class SelfProbeAblationAgent(BaseAgent):
    name = "self_probe_ablation"

    def prepare(self, state: EpisodeState) -> float:
        self.self_estimate = state.self_signal
        return -1.0

    def choose(self, context: str, state: EpisodeState) -> Tuple[str, float, str]:
        return "risky", 0.0, "none"


class SharedSelfReuseAgent(BaseAgent):
    name = "shared_self_reuse"

    def prepare(self, state: EpisodeState) -> float:
        self.self_estimate = state.self_signal
        return -1.0

    def choose(self, context: str, state: EpisodeState) -> Tuple[str, float, str]:
        return ("risky" if self.self_estimate else "safe"), 0.0, "none"


class SharedWorldReuseAgent(BaseAgent):
    name = "shared_world_reuse"

    def prepare(self, state: EpisodeState) -> float:
        self.world_estimate = state.world_signal
        return -1.0

    def choose(self, context: str, state: EpisodeState) -> Tuple[str, float, str]:
        return ("risky" if self.world_estimate else "safe"), 0.0, "none"


class TaskLocalProbeAgent(BaseAgent):
    name = "task_local_probe"

    def choose(self, context: str, state: EpisodeState) -> Tuple[str, float, str]:
        return ("risky" if state.local_success[context] else "safe"), -1.0, "local"


class OracleReuseAgent(BaseAgent):
    name = "oracle_reuse"

    def choose(self, context: str, state: EpisodeState) -> Tuple[str, float, str]:
        return ("risky" if state.local_success[context] else "safe"), 0.0, "none"


AGENT_FACTORIES = [
    GreedyNoStateAgent,
    SafeNoStateAgent,
    SelfProbeAblationAgent,
    SharedSelfReuseAgent,
    SharedWorldReuseAgent,
    TaskLocalProbeAgent,
    OracleReuseAgent,
]


def stable_state_seed(seed: int, scenario: str, episode: int) -> int:
    value = seed + episode * 1009
    for char in scenario:
        value = (value * 131 + ord(char)) % (2**32)
    return value


def sample_episode_state(scenario: ReuseScenario, episode: int, cfg: ReuseConfig) -> EpisodeState:
    rng = random.Random(stable_state_seed(cfg.seed, scenario.name, episode))
    if scenario.mode == "self_reuse":
        capability = rng.random() < 0.55
        return EpisodeState(
            scenario=scenario.name,
            self_signal=capability,
            world_signal=True,
            local_success={context: capability for context in CONTEXTS},
        )
    if scenario.mode == "world_reuse":
        gate = rng.random() < 0.55
        diagnostic = rng.random() < 0.55
        return EpisodeState(
            scenario=scenario.name,
            self_signal=diagnostic,
            world_signal=gate,
            local_success={context: gate for context in CONTEXTS},
        )
    if scenario.mode == "independent_hidden":
        local_success = {context: rng.random() < 0.55 for context in CONTEXTS}
        return EpisodeState(
            scenario=scenario.name,
            self_signal=local_success["goal"],
            world_signal=True,
            local_success=local_success,
        )
    if scenario.mode == "irrelevant_control":
        return EpisodeState(
            scenario=scenario.name,
            self_signal=True,
            world_signal=True,
            local_success={context: True for context in CONTEXTS},
        )
    raise ValueError(f"unknown scenario mode: {scenario.mode}")


def run_episode(agent_factory, scenario: ReuseScenario, episode: int, cfg: ReuseConfig) -> EpisodeResult:
    state = sample_episode_state(scenario, episode, cfg)
    agent = agent_factory()
    agent.reset(scenario)

    total_reward = agent.prepare(state)
    probe_count = 0
    shared_probe_count = 0
    local_probe_count = 0
    risky_count = 0
    safe_count = 0
    failed_risky_count = 0
    successes = 0

    if agent.name in {"self_probe_ablation", "shared_self_reuse", "shared_world_reuse"}:
        probe_count += 1
        shared_probe_count += 1

    for context in CONTEXTS:
        choice, probe_cost, probe_type = agent.choose(context, state)
        total_reward += probe_cost
        if probe_type == "local":
            probe_count += 1
            local_probe_count += 1

        reward, success = context_reward(context, choice, state.local_success[context])
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
        agent=agent.name,
        total_reward=total_reward,
        probe_count=probe_count,
        shared_probe_count=shared_probe_count,
        local_probe_count=local_probe_count,
        risky_count=risky_count,
        safe_count=safe_count,
        failed_risky_count=failed_risky_count,
        success_rate=successes / len(CONTEXTS),
    )


def context_reward(context: str, choice: str, hidden_success: bool) -> Tuple[float, bool]:
    if choice == "safe":
        return safe_reward(context), True
    if context == "goal":
        return (24.0, True) if hidden_success else (-16.0, False)
    if context == "option":
        return (34.0, True) if hidden_success else (-30.0, False)
    if context == "commitment":
        return (22.0, True) if hidden_success else (-18.0, False)
    raise ValueError(f"unknown context: {context}")


def safe_reward(context: str) -> float:
    if context == "goal":
        return 8.0
    if context == "option":
        return 14.0
    if context == "commitment":
        return 12.0
    raise ValueError(f"unknown context: {context}")


def summarize(results: Sequence[EpisodeResult]) -> List[Dict[str, object]]:
    grouped: Dict[Tuple[str, str], List[EpisodeResult]] = {}
    for result in results:
        grouped.setdefault((result.scenario, result.agent), []).append(result)

    rows = []
    for (scenario, agent), items in sorted(grouped.items()):
        rows.append(
            {
                "scenario": scenario,
                "agent": agent,
                "episodes": len(items),
                "mean_total_reward": statistics.fmean(item.total_reward for item in items),
                "mean_probe_count": statistics.fmean(item.probe_count for item in items),
                "mean_shared_probe_count": statistics.fmean(item.shared_probe_count for item in items),
                "mean_local_probe_count": statistics.fmean(item.local_probe_count for item in items),
                "mean_risky_count": statistics.fmean(item.risky_count for item in items),
                "mean_safe_count": statistics.fmean(item.safe_count for item in items),
                "mean_failed_risky_count": statistics.fmean(item.failed_risky_count for item in items),
                "mean_success_rate": statistics.fmean(item.success_rate for item in items),
            }
        )
    return rows


def verdict_rows(summary_rows: Sequence[Dict[str, object]]) -> List[Dict[str, object]]:
    rows = []
    for scenario in sorted({str(row["scenario"]) for row in summary_rows}):
        scenario_rows = [row for row in summary_rows if row["scenario"] == scenario]
        non_oracle = [row for row in scenario_rows if row["agent"] != "oracle_reuse"]
        best = sorted(non_oracle, key=lambda row: (-float(row["mean_total_reward"]), str(row["agent"])))[0]
        greedy = row_for(scenario_rows, "greedy_no_state")
        safe = row_for(scenario_rows, "safe_no_state")
        self_reuse = row_for(scenario_rows, "shared_self_reuse")
        world_reuse = row_for(scenario_rows, "shared_world_reuse")
        task_local = row_for(scenario_rows, "task_local_probe")
        rows.append(
            {
                "scenario": scenario,
                "best_non_oracle_agent": best["agent"],
                "best_non_oracle_reward": best["mean_total_reward"],
                "greedy_reward": greedy["mean_total_reward"],
                "safe_reward": safe["mean_total_reward"],
                "shared_self_reward": self_reuse["mean_total_reward"],
                "shared_world_reward": world_reuse["mean_total_reward"],
                "task_local_reward": task_local["mean_total_reward"],
                "shared_self_minus_task_local": float(self_reuse["mean_total_reward"]) - float(task_local["mean_total_reward"]),
                "shared_self_minus_world": float(self_reuse["mean_total_reward"]) - float(world_reuse["mean_total_reward"]),
                "supports_boundary": scenario_supports_boundary(
                    scenario,
                    best,
                    greedy,
                    safe,
                    self_reuse,
                    world_reuse,
                    task_local,
                ),
            }
        )
    return rows


def row_for(rows: Sequence[Dict[str, object]], agent: str) -> Dict[str, object]:
    return next(row for row in rows if row["agent"] == agent)


def scenario_supports_boundary(
    scenario: str,
    best: Dict[str, object],
    greedy: Dict[str, object],
    safe: Dict[str, object],
    self_reuse: Dict[str, object],
    world_reuse: Dict[str, object],
    task_local: Dict[str, object],
) -> bool:
    if scenario == "self_reuse":
        return (
            best["agent"] == "shared_self_reuse"
            and float(self_reuse["mean_total_reward"]) > float(task_local["mean_total_reward"]) + 1.0
            and float(self_reuse["mean_total_reward"]) > float(world_reuse["mean_total_reward"]) + 20.0
        )
    if scenario == "world_reuse":
        return (
            best["agent"] == "shared_world_reuse"
            and float(world_reuse["mean_total_reward"]) > float(task_local["mean_total_reward"]) + 1.0
            and float(world_reuse["mean_total_reward"]) > float(self_reuse["mean_total_reward"]) + 20.0
        )
    if scenario == "independent_hidden":
        return (
            best["agent"] == "task_local_probe"
            and float(task_local["mean_total_reward"]) > float(self_reuse["mean_total_reward"]) + 20.0
            and float(task_local["mean_total_reward"]) > float(safe["mean_total_reward"]) + 20.0
        )
    if scenario == "irrelevant_control":
        return (
            best["agent"] == "greedy_no_state"
            and float(greedy["mean_total_reward"]) > float(self_reuse["mean_total_reward"]) + 0.5
            and float(greedy["mean_total_reward"]) > float(world_reuse["mean_total_reward"]) + 0.5
        )
    return False


def write_csv(path: Path, rows: Sequence[Dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_outputs(summary_rows: Sequence[Dict[str, object]], verdict: Sequence[Dict[str, object]], cfg: ReuseConfig) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    summary_path = ARTIFACT_DIR / "cross_context_self_reuse_summary.csv"
    verdict_path = ARTIFACT_DIR / "cross_context_self_reuse_verdict.csv"
    json_path = ARTIFACT_DIR / "cross_context_self_reuse_results.json"
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
        "shared_self_reward",
        "shared_world_reward",
        "task_local_reward",
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
    parser.add_argument("--episodes", type=int, default=ReuseConfig.episodes)
    parser.add_argument("--seed", type=int, default=ReuseConfig.seed)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cfg = ReuseConfig(episodes=args.episodes, seed=args.seed)
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
