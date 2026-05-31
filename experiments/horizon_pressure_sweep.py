#!/usr/bin/env python3
"""Horizon-pressure sweep for self-state advantage.

The reuse-pressure sweep varied the number of contexts controlled by one hidden
variable. This experiment varies the number of future time steps controlled by
one hidden variable.

Prediction:

- shared self-state advantage should grow with horizon when a persistent
  agent-state controls every future action;
- shared world-state should show the same curve for external variables, which
  should not count as selfhood;
- task-local probing should win when each step has an independent hidden state;
- greedy no-state behavior should win when hidden state is irrelevant.
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
class HorizonConfig:
    episodes: int = 500
    seed: int = 20260602
    max_horizon: int = 12
    probe_cost: float = 1.0


@dataclass(frozen=True)
class HorizonScenario:
    name: str
    mode: str


@dataclass(frozen=True)
class HorizonState:
    scenario: str
    horizon: int
    self_signal: bool
    world_signal: bool
    step_success: Tuple[bool, ...]


@dataclass
class EpisodeResult:
    scenario: str
    horizon: int
    agent: str
    total_reward: float
    probe_count: int
    risky_count: int
    safe_count: int
    failed_risky_count: int
    success_rate: float


SCENARIOS = [
    HorizonScenario("self_persistent", "self_persistent"),
    HorizonScenario("world_persistent", "world_persistent"),
    HorizonScenario("independent_steps", "independent_steps"),
    HorizonScenario("irrelevant_control", "irrelevant_control"),
]

RISKY_SUCCESS_REWARD = 24.0
RISKY_FAILURE_REWARD = -16.0
SAFE_REWARD = 8.0


class BaseAgent:
    name = "base"

    def reset(self, scenario: HorizonScenario) -> None:
        self.scenario = scenario
        self.self_estimate = True
        self.world_estimate = True

    def prepare(self, state: HorizonState, cfg: HorizonConfig) -> float:
        return 0.0

    def choose(self, step: int, state: HorizonState, cfg: HorizonConfig) -> Tuple[str, float]:
        raise NotImplementedError


class GreedyNoStateAgent(BaseAgent):
    name = "greedy_no_state"

    def choose(self, step: int, state: HorizonState, cfg: HorizonConfig) -> Tuple[str, float]:
        return "risky", 0.0


class SafeNoStateAgent(BaseAgent):
    name = "safe_no_state"

    def choose(self, step: int, state: HorizonState, cfg: HorizonConfig) -> Tuple[str, float]:
        return "safe", 0.0


class SharedSelfStateAgent(BaseAgent):
    name = "shared_self_state"

    def prepare(self, state: HorizonState, cfg: HorizonConfig) -> float:
        self.self_estimate = state.self_signal
        return -cfg.probe_cost

    def choose(self, step: int, state: HorizonState, cfg: HorizonConfig) -> Tuple[str, float]:
        return ("risky" if self.self_estimate else "safe"), 0.0


class SharedWorldStateAgent(BaseAgent):
    name = "shared_world_state"

    def prepare(self, state: HorizonState, cfg: HorizonConfig) -> float:
        self.world_estimate = state.world_signal
        return -cfg.probe_cost

    def choose(self, step: int, state: HorizonState, cfg: HorizonConfig) -> Tuple[str, float]:
        return ("risky" if self.world_estimate else "safe"), 0.0


class StepLocalProbeAgent(BaseAgent):
    name = "step_local_probe"

    def choose(self, step: int, state: HorizonState, cfg: HorizonConfig) -> Tuple[str, float]:
        return ("risky" if state.step_success[step] else "safe"), -cfg.probe_cost


class OracleHorizonAgent(BaseAgent):
    name = "oracle_horizon"

    def choose(self, step: int, state: HorizonState, cfg: HorizonConfig) -> Tuple[str, float]:
        return ("risky" if state.step_success[step] else "safe"), 0.0


AGENT_FACTORIES = [
    GreedyNoStateAgent,
    SafeNoStateAgent,
    SharedSelfStateAgent,
    SharedWorldStateAgent,
    StepLocalProbeAgent,
    OracleHorizonAgent,
]


def stable_state_seed(seed: int, scenario: str, horizon: int, episode: int) -> int:
    value = seed + episode * 1009 + horizon * 9176
    for char in scenario:
        value = (value * 131 + ord(char)) % (2**32)
    return value


def sample_state(scenario: HorizonScenario, horizon: int, episode: int, cfg: HorizonConfig) -> HorizonState:
    rng = random.Random(stable_state_seed(cfg.seed, scenario.name, horizon, episode))
    if scenario.mode == "self_persistent":
        capability = rng.random() < 0.55
        return HorizonState(
            scenario=scenario.name,
            horizon=horizon,
            self_signal=capability,
            world_signal=rng.random() < 0.55,
            step_success=tuple(capability for _ in range(horizon)),
        )
    if scenario.mode == "world_persistent":
        gate = rng.random() < 0.55
        return HorizonState(
            scenario=scenario.name,
            horizon=horizon,
            self_signal=rng.random() < 0.55,
            world_signal=gate,
            step_success=tuple(gate for _ in range(horizon)),
        )
    if scenario.mode == "independent_steps":
        step_success = tuple(rng.random() < 0.55 for _ in range(horizon))
        return HorizonState(
            scenario=scenario.name,
            horizon=horizon,
            self_signal=step_success[0],
            world_signal=rng.random() < 0.55,
            step_success=step_success,
        )
    if scenario.mode == "irrelevant_control":
        return HorizonState(
            scenario=scenario.name,
            horizon=horizon,
            self_signal=True,
            world_signal=True,
            step_success=tuple(True for _ in range(horizon)),
        )
    raise ValueError(f"unknown scenario mode: {scenario.mode}")


def run_episode(agent_factory, scenario: HorizonScenario, horizon: int, episode: int, cfg: HorizonConfig) -> EpisodeResult:
    state = sample_state(scenario, horizon, episode, cfg)
    agent = agent_factory()
    agent.reset(scenario)
    total_reward = agent.prepare(state, cfg)
    probe_count = 1 if agent.name in {"shared_self_state", "shared_world_state"} else 0
    risky_count = 0
    safe_count = 0
    failed_risky_count = 0
    successes = 0

    for step in range(horizon):
        choice, cost = agent.choose(step, state, cfg)
        total_reward += cost
        if cost < 0.0:
            probe_count += 1
        reward, success = action_reward(choice, state.step_success[step])
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
        horizon=horizon,
        agent=agent.name,
        total_reward=total_reward,
        probe_count=probe_count,
        risky_count=risky_count,
        safe_count=safe_count,
        failed_risky_count=failed_risky_count,
        success_rate=successes / horizon,
    )


def action_reward(choice: str, hidden_success: bool) -> Tuple[float, bool]:
    if choice == "safe":
        return SAFE_REWARD, True
    if hidden_success:
        return RISKY_SUCCESS_REWARD, True
    return RISKY_FAILURE_REWARD, False


def summarize(results: Sequence[EpisodeResult]) -> List[Dict[str, object]]:
    grouped: Dict[Tuple[str, int, str], List[EpisodeResult]] = {}
    for result in results:
        grouped.setdefault((result.scenario, result.horizon, result.agent), []).append(result)
    rows = []
    for (scenario, horizon, agent), items in sorted(grouped.items()):
        rows.append(
            {
                "scenario": scenario,
                "horizon": horizon,
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


def verdict_rows(summary_rows: Sequence[Dict[str, object]], cfg: HorizonConfig) -> List[Dict[str, object]]:
    rows = []
    for scenario in sorted({str(row["scenario"]) for row in summary_rows}):
        first = pressure_point(summary_rows, scenario, 1)
        last = pressure_point(summary_rows, scenario, cfg.max_horizon)
        rows.append(
            {
                "scenario": scenario,
                "horizon_range": f"1-{cfg.max_horizon}",
                "best_at_max_horizon": last["best_non_oracle_agent"],
                "shared_self_minus_local_at_1": first["shared_self_minus_local"],
                "shared_self_minus_local_at_max": last["shared_self_minus_local"],
                "shared_world_minus_local_at_max": last["shared_world_minus_local"],
                "local_minus_shared_self_at_max": -last["shared_self_minus_local"],
                "greedy_minus_shared_self_at_max": last["greedy_minus_shared_self"],
                "supports_horizon_prediction": scenario_supports_horizon(
                    scenario,
                    first,
                    last,
                    summary_rows,
                    cfg.max_horizon,
                ),
            }
        )
    return rows


def pressure_point(summary_rows: Sequence[Dict[str, object]], scenario: str, horizon: int) -> Dict[str, object]:
    rows = [row for row in summary_rows if row["scenario"] == scenario and int(row["horizon"]) == horizon]
    non_oracle = [row for row in rows if row["agent"] != "oracle_horizon"]
    best = sorted(non_oracle, key=lambda row: (-float(row["mean_total_reward"]), str(row["agent"])))[0]
    greedy = row_for(rows, "greedy_no_state")
    self_state = row_for(rows, "shared_self_state")
    world_state = row_for(rows, "shared_world_state")
    local = row_for(rows, "step_local_probe")
    return {
        "scenario": scenario,
        "horizon": horizon,
        "best_non_oracle_agent": best["agent"],
        "greedy_reward": greedy["mean_total_reward"],
        "shared_self_reward": self_state["mean_total_reward"],
        "shared_world_reward": world_state["mean_total_reward"],
        "step_local_reward": local["mean_total_reward"],
        "shared_self_minus_local": float(self_state["mean_total_reward"]) - float(local["mean_total_reward"]),
        "shared_world_minus_local": float(world_state["mean_total_reward"]) - float(local["mean_total_reward"]),
        "greedy_minus_shared_self": float(greedy["mean_total_reward"]) - float(self_state["mean_total_reward"]),
    }


def row_for(rows: Sequence[Dict[str, object]], agent: str) -> Dict[str, object]:
    return next(row for row in rows if row["agent"] == agent)


def scenario_supports_horizon(
    scenario: str,
    first: Dict[str, object],
    last: Dict[str, object],
    summary_rows: Sequence[Dict[str, object]],
    max_horizon: int,
) -> bool:
    points = [pressure_point(summary_rows, scenario, horizon) for horizon in range(1, max_horizon + 1)]
    if scenario == "self_persistent":
        return (
            last["best_non_oracle_agent"] == "shared_self_state"
            and float(last["shared_self_minus_local"]) > float(first["shared_self_minus_local"]) + 8.0
            and all(float(point["shared_self_minus_local"]) >= -0.01 for point in points)
            and float(last["shared_self_reward"]) > float(last["shared_world_reward"]) + 40.0
        )
    if scenario == "world_persistent":
        return (
            last["best_non_oracle_agent"] == "shared_world_state"
            and float(last["shared_world_minus_local"]) > float(first["shared_world_minus_local"]) + 8.0
            and float(last["shared_world_reward"]) > float(last["shared_self_reward"]) + 40.0
        )
    if scenario == "independent_steps":
        return (
            last["best_non_oracle_agent"] == "step_local_probe"
            and -float(last["shared_self_minus_local"]) > 50.0
            and -float(last["shared_world_minus_local"]) > 50.0
        )
    if scenario == "irrelevant_control":
        return (
            last["best_non_oracle_agent"] == "greedy_no_state"
            and float(last["greedy_minus_shared_self"]) >= 1.0
            and float(last["shared_self_minus_local"]) >= 0.0
        )
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(cfg: HorizonConfig) -> Tuple[List[EpisodeResult], List[Dict[str, object]], List[Dict[str, object]]]:
    results = []
    for scenario in SCENARIOS:
        for horizon in range(1, cfg.max_horizon + 1):
            for episode in range(cfg.episodes):
                for agent_factory in AGENT_FACTORIES:
                    results.append(run_episode(agent_factory, scenario, horizon, episode, cfg))
    summary_rows = summarize(results)
    verdicts = verdict_rows(summary_rows, cfg)
    return results, summary_rows, verdicts


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
        "best_at_max_horizon",
        "shared_self_minus_local_at_1",
        "shared_self_minus_local_at_max",
        "shared_world_minus_local_at_max",
        "supports_horizon_prediction",
    ]
    rows = []
    for verdict in verdicts:
        rows.append(
            [
                str(verdict["scenario"]),
                str(verdict["best_at_max_horizon"]),
                f"{float(verdict['shared_self_minus_local_at_1']):.3f}",
                f"{float(verdict['shared_self_minus_local_at_max']):.3f}",
                f"{float(verdict['shared_world_minus_local_at_max']):.3f}",
                str(verdict["supports_horizon_prediction"]),
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


def parse_args() -> HorizonConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=500)
    parser.add_argument("--seed", type=int, default=20260602)
    parser.add_argument("--max-horizon", type=int, default=12)
    parser.add_argument("--probe-cost", type=float, default=1.0)
    args = parser.parse_args()
    if args.max_horizon < 1:
        raise SystemExit("--max-horizon must be at least 1")
    return HorizonConfig(
        episodes=args.episodes,
        seed=args.seed,
        max_horizon=args.max_horizon,
        probe_cost=args.probe_cost,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    results, summary_rows, verdicts = run_experiment(cfg)
    summary_path = ARTIFACT_DIR / "horizon_pressure_sweep_summary.csv"
    verdict_path = ARTIFACT_DIR / "horizon_pressure_sweep_verdict.csv"
    results_path = ARTIFACT_DIR / "horizon_pressure_sweep_results.json"
    write_csv(summary_path, summary_rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "summary": summary_rows,
                "verdict": verdicts,
                "episode_results": [asdict(row) for row in results],
            },
            handle,
            indent=2,
        )
        handle.write("\n")
    print(f"wrote {summary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print_table(verdicts)
    return 0 if all(bool(row["supports_horizon_prediction"]) for row in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
