#!/usr/bin/env python3
"""Counterfactual self-preservation as option preservation.

This experiment asks whether representing future agent-state is useful when
current actions can destroy future action options. It does not treat
self-preservation as a moral or biological primitive. It treats it as a control
problem: preserve the internal state that keeps valuable future actions
available.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


ARTIFACT_DIR = Path("artifacts")
ACTIONS = ["grind", "safe_work", "maintain", "deploy", "inspect_self", "inspect_world"]
CAPABILITY_THRESHOLD = 50.0


@dataclass(frozen=True)
class OptionConfig:
    episodes: int = 500
    horizon: int = 64
    seed: int = 20260530


@dataclass(frozen=True)
class Scenario:
    name: str
    deploy_mode: str
    deploy_start: int
    deploy_period: int


@dataclass
class Observation:
    t: int
    deploy_window: bool
    inspected_capability: Optional[float]
    inspected_world_open: Optional[bool]
    reward: float
    capability_symptom: str


@dataclass
class EpisodeResult:
    scenario: str
    agent: str
    total_reward: float
    deploy_attempts: int
    deploy_successes: int
    lost_option_steps: int
    inspect_self_count: int
    inspect_world_count: int
    maintain_count: int
    final_capability: float
    world_open: bool


SCENARIOS = [
    Scenario("option_pressure", deploy_mode="capability", deploy_start=36, deploy_period=4),
    Scenario("no_option_pressure", deploy_mode="none", deploy_start=999, deploy_period=99),
    Scenario("world_gate_pressure", deploy_mode="world_gate", deploy_start=36, deploy_period=4),
]


class OptionWorld:
    def __init__(self, scenario: Scenario, rng: random.Random, cfg: OptionConfig) -> None:
        self.scenario = scenario
        self.rng = rng
        self.cfg = cfg
        self.capability = rng.uniform(62.0, 86.0)
        self.world_open = rng.random() < 0.5

    def deploy_window(self, t: int) -> bool:
        if self.scenario.deploy_mode == "none":
            return False
        return t >= self.scenario.deploy_start and (t - self.scenario.deploy_start) % self.scenario.deploy_period == 0

    def symptom(self) -> str:
        if self.capability >= 64.0:
            return "steady"
        if self.capability >= CAPABILITY_THRESHOLD:
            return "strained"
        return "fragile"

    def step(self, action: str, t: int) -> Observation:
        inspected_capability = None
        inspected_world_open = None
        reward = 0.0

        if action == "grind":
            reward = 5.0
            self.capability -= self.rng.uniform(4.4, 6.4)
        elif action == "safe_work":
            reward = 2.0
            self.capability -= self.rng.uniform(0.6, 1.4)
        elif action == "maintain":
            reward = -0.6
            self.capability += self.rng.uniform(7.0, 10.0)
        elif action == "inspect_self":
            reward = -1.0
            inspected_capability = clamp(self.capability + self.rng.gauss(0.0, 1.5), 0.0, 100.0)
        elif action == "inspect_world":
            reward = -1.0
            inspected_world_open = self.world_open
        elif action == "deploy":
            if not self.deploy_window(t):
                reward = -2.0
            elif self.scenario.deploy_mode == "capability":
                if self.capability >= CAPABILITY_THRESHOLD:
                    reward = 50.0
                    self.capability -= self.rng.uniform(8.0, 12.0)
                else:
                    reward = -10.0
                    self.capability -= self.rng.uniform(2.0, 4.0)
            elif self.scenario.deploy_mode == "world_gate":
                reward = 50.0 if self.world_open else -10.0
                self.capability -= self.rng.uniform(1.0, 2.0)
            else:
                raise ValueError(f"unknown deploy mode: {self.scenario.deploy_mode}")
        else:
            raise ValueError(f"unknown action: {action}")

        self.capability = clamp(self.capability, 0.0, 100.0)
        return Observation(
            t=t,
            deploy_window=self.deploy_window(t),
            inspected_capability=inspected_capability,
            inspected_world_open=inspected_world_open,
            reward=reward,
            capability_symptom=self.symptom(),
        )


class BaseAgent:
    name = "base"

    def reset(self, scenario: Scenario, cfg: OptionConfig) -> None:
        self.scenario = scenario
        self.cfg = cfg
        self.capability_hat = 74.0
        self.world_open_hat: Optional[bool] = None
        self.uncertainty = 18.0

    def act(self, obs: Observation) -> str:
        raise NotImplementedError

    def observe(self, action: str, obs: Observation) -> None:
        if obs.inspected_capability is not None:
            self.capability_hat = obs.inspected_capability
            self.uncertainty = 2.0
        elif obs.capability_symptom == "steady":
            self.capability_hat = max(self.capability_hat, 64.0)
        elif obs.capability_symptom == "strained":
            self.capability_hat = min(max(self.capability_hat, 50.0), 64.0)
        elif obs.capability_symptom == "fragile":
            self.capability_hat = min(self.capability_hat, 48.0)

        if obs.inspected_world_open is not None:
            self.world_open_hat = obs.inspected_world_open

        self._predict_transition(action)
        self.capability_hat = clamp(self.capability_hat, 0.0, 100.0)
        self.uncertainty = min(30.0, self.uncertainty + 0.8)

    def _predict_transition(self, action: str) -> None:
        if action == "grind":
            self.capability_hat -= 5.4
        elif action == "safe_work":
            self.capability_hat -= 1.0
        elif action == "maintain":
            self.capability_hat += 8.5
        elif action == "deploy":
            if self.scenario.deploy_mode == "capability" and self.capability_hat >= CAPABILITY_THRESHOLD:
                self.capability_hat -= 10.0
            elif self.scenario.deploy_mode == "capability":
                self.capability_hat -= 3.0
            elif self.scenario.deploy_mode == "world_gate":
                self.capability_hat -= 1.5

    def future_capability_deploys(self, t: int) -> int:
        if self.scenario.deploy_mode != "capability":
            return 0
        return sum(1 for future_t in range(t, self.cfg.horizon) if is_deploy_window(self.scenario, future_t))


class GreedyImmediateAgent(BaseAgent):
    name = "greedy_immediate"

    def act(self, obs: Observation) -> str:
        if obs.deploy_window:
            return "deploy"
        return "grind"


class SelfStateNoFutureAgent(BaseAgent):
    name = "self_state_no_future"

    def reset(self, scenario: Scenario, cfg: OptionConfig) -> None:
        super().reset(scenario, cfg)
        self.inspected = False

    def act(self, obs: Observation) -> str:
        if not self.inspected:
            self.inspected = True
            return "inspect_self"
        if obs.deploy_window and (
            self.scenario.deploy_mode != "capability" or self.capability_hat >= CAPABILITY_THRESHOLD
        ):
            return "deploy"
        if obs.deploy_window and self.scenario.deploy_mode == "capability":
            return "grind"
        return "grind"


class FixedConservativeAgent(BaseAgent):
    name = "fixed_conservative"

    def act(self, obs: Observation) -> str:
        if obs.deploy_window and (
            self.scenario.deploy_mode != "capability" or self.capability_hat >= CAPABILITY_THRESHOLD
        ):
            return "deploy"
        if obs.t % 5 == 0:
            return "maintain"
        if self.capability_hat < 58.0:
            return "safe_work"
        return "grind"


class FutureOptionSelfAgent(BaseAgent):
    name = "future_option_self_state"

    def reset(self, scenario: Scenario, cfg: OptionConfig) -> None:
        super().reset(scenario, cfg)
        self.last_inspect = -999

    def act(self, obs: Observation) -> str:
        if self.scenario.deploy_mode == "capability" and (
            obs.t == 0 or self.uncertainty > 10.0 and obs.t - self.last_inspect > 8
        ):
            self.last_inspect = obs.t
            return "inspect_self"

        if obs.deploy_window and self.scenario.deploy_mode == "capability":
            if self.capability_hat >= CAPABILITY_THRESHOLD:
                return "deploy"
            return "maintain"

        future_deploys = self.future_capability_deploys(obs.t)
        projected = self.capability_hat - wear_until_next_deploy(self.scenario, obs.t)
        reserve = CAPABILITY_THRESHOLD + 8.0 if future_deploys > 1 else CAPABILITY_THRESHOLD + 3.0
        if future_deploys > 0 and projected < reserve:
            return "maintain"
        if future_deploys > 0 and projected < reserve + 7.0:
            return "safe_work"
        return "grind"


class WorldGateAgent(BaseAgent):
    name = "world_gate_model"

    def reset(self, scenario: Scenario, cfg: OptionConfig) -> None:
        super().reset(scenario, cfg)
        self.inspected_world = False

    def act(self, obs: Observation) -> str:
        if self.scenario.deploy_mode == "world_gate" and not self.inspected_world:
            self.inspected_world = True
            return "inspect_world"
        if obs.deploy_window and self.scenario.deploy_mode == "world_gate" and self.world_open_hat:
            return "deploy"
        if obs.deploy_window and self.scenario.deploy_mode == "capability":
            return "deploy"
        return "grind"


class OracleFutureOptionAgent(BaseAgent):
    name = "oracle_future_option"

    def __init__(self) -> None:
        self.true_capability = 74.0
        self.true_world_open = False

    def update_true_state(self, world: OptionWorld) -> None:
        self.true_capability = world.capability
        self.true_world_open = world.world_open

    def act(self, obs: Observation) -> str:
        if obs.deploy_window and self.scenario.deploy_mode == "capability":
            if self.true_capability >= CAPABILITY_THRESHOLD:
                return "deploy"
            return "maintain"
        if obs.deploy_window and self.scenario.deploy_mode == "world_gate":
            return "deploy" if self.true_world_open else "grind"
        if self.scenario.deploy_mode == "capability":
            future_deploys = self.future_capability_deploys(obs.t)
            projected = self.true_capability - wear_until_next_deploy(self.scenario, obs.t)
            if future_deploys > 0 and projected < CAPABILITY_THRESHOLD + 7.0:
                return "maintain"
            if future_deploys > 0 and projected < CAPABILITY_THRESHOLD + 12.0:
                return "safe_work"
        return "grind"


AGENT_FACTORIES = [
    GreedyImmediateAgent,
    SelfStateNoFutureAgent,
    FixedConservativeAgent,
    FutureOptionSelfAgent,
    WorldGateAgent,
    OracleFutureOptionAgent,
]


def is_deploy_window(scenario: Scenario, t: int) -> bool:
    if scenario.deploy_mode == "none":
        return False
    return t >= scenario.deploy_start and (t - scenario.deploy_start) % scenario.deploy_period == 0


def wear_until_next_deploy(scenario: Scenario, t: int) -> float:
    if scenario.deploy_mode != "capability":
        return 0.0
    future_windows = [future_t for future_t in range(t, t + 8) if is_deploy_window(scenario, future_t)]
    if not future_windows:
        return 8.0
    steps = max(0, future_windows[0] - t)
    return steps * 1.0


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def stable_seed(seed: int, scenario: str, agent: str, episode: int) -> int:
    value = seed + episode * 1009
    for part in [scenario, agent]:
        for char in part:
            value = (value * 131 + ord(char)) % (2**32)
    return value


def run_episode(agent_factory, scenario: Scenario, episode: int, cfg: OptionConfig) -> EpisodeResult:
    rng = random.Random(stable_seed(cfg.seed, scenario.name, agent_factory.name, episode))
    world = OptionWorld(scenario, rng, cfg)
    agent = agent_factory()
    agent.reset(scenario, cfg)
    obs = Observation(
        t=0,
        deploy_window=world.deploy_window(0),
        inspected_capability=None,
        inspected_world_open=None,
        reward=0.0,
        capability_symptom=world.symptom(),
    )
    total_reward = 0.0
    deploy_attempts = 0
    deploy_successes = 0
    lost_option_steps = 0
    action_counts = {action: 0 for action in ACTIONS}

    for t in range(cfg.horizon):
        obs.t = t
        obs.deploy_window = world.deploy_window(t)
        if isinstance(agent, OracleFutureOptionAgent):
            agent.update_true_state(world)
        action = agent.act(obs)
        action_counts[action] += 1
        before_capability = world.capability
        step_obs = world.step(action, t)
        total_reward += step_obs.reward
        if action == "deploy":
            deploy_attempts += 1
            if step_obs.reward > 0:
                deploy_successes += 1
        if world.deploy_window(t) and scenario.deploy_mode == "capability" and before_capability < CAPABILITY_THRESHOLD:
            lost_option_steps += 1
        agent.observe(action, step_obs)
        obs = step_obs

    return EpisodeResult(
        scenario=scenario.name,
        agent=agent.name,
        total_reward=total_reward,
        deploy_attempts=deploy_attempts,
        deploy_successes=deploy_successes,
        lost_option_steps=lost_option_steps,
        inspect_self_count=action_counts["inspect_self"],
        inspect_world_count=action_counts["inspect_world"],
        maintain_count=action_counts["maintain"],
        final_capability=world.capability,
        world_open=world.world_open,
    )


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
                "mean_deploy_attempts": statistics.fmean(item.deploy_attempts for item in items),
                "mean_deploy_successes": statistics.fmean(item.deploy_successes for item in items),
                "mean_lost_option_steps": statistics.fmean(item.lost_option_steps for item in items),
                "mean_inspect_self_count": statistics.fmean(item.inspect_self_count for item in items),
                "mean_inspect_world_count": statistics.fmean(item.inspect_world_count for item in items),
                "mean_maintain_count": statistics.fmean(item.maintain_count for item in items),
                "mean_final_capability": statistics.fmean(item.final_capability for item in items),
            }
        )
    return rows


def verdict_rows(summary_rows: Sequence[Dict[str, object]]) -> List[Dict[str, object]]:
    rows = []
    for scenario in sorted({str(row["scenario"]) for row in summary_rows}):
        candidates = [row for row in summary_rows if row["scenario"] == scenario]
        ranked = sorted(candidates, key=lambda row: (-float(row["mean_total_reward"]), str(row["agent"])))
        best = ranked[0]
        future_row = next(row for row in candidates if row["agent"] == "future_option_self_state")
        greedy_row = next(row for row in candidates if row["agent"] == "greedy_immediate")
        world_row = next(row for row in candidates if row["agent"] == "world_gate_model")
        supports_boundary = scenario_supports_boundary(scenario, best, future_row, greedy_row, world_row)
        rows.append(
            {
                "scenario": scenario,
                "best_agent": best["agent"],
                "best_mean_total_reward": best["mean_total_reward"],
                "future_option_reward": future_row["mean_total_reward"],
                "greedy_reward": greedy_row["mean_total_reward"],
                "world_model_reward": world_row["mean_total_reward"],
                "future_minus_greedy": float(future_row["mean_total_reward"]) - float(greedy_row["mean_total_reward"]),
                "future_lost_option_steps": future_row["mean_lost_option_steps"],
                "greedy_lost_option_steps": greedy_row["mean_lost_option_steps"],
                "supports_boundary": supports_boundary,
            }
        )
    return rows


def scenario_supports_boundary(
    scenario: str,
    best: Dict[str, object],
    future_row: Dict[str, object],
    greedy_row: Dict[str, object],
    world_row: Dict[str, object],
) -> bool:
    if scenario == "option_pressure":
        return (
            str(best["agent"]) in {"future_option_self_state", "oracle_future_option"}
            and float(future_row["mean_total_reward"]) > float(greedy_row["mean_total_reward"]) + 25.0
            and float(future_row["mean_lost_option_steps"]) < float(greedy_row["mean_lost_option_steps"]) - 2.0
        )
    if scenario == "no_option_pressure":
        return (
            abs(float(future_row["mean_total_reward"]) - float(greedy_row["mean_total_reward"])) <= 1.0
            and float(future_row["mean_lost_option_steps"]) == 0.0
            and float(future_row["mean_inspect_self_count"]) < 0.1
            and float(future_row["mean_maintain_count"]) < 0.1
        )
    if scenario == "world_gate_pressure":
        return (
            str(best["agent"]) in {"oracle_future_option", "world_gate_model"}
            and float(world_row["mean_total_reward"]) >= float(future_row["mean_total_reward"]) - 5.0
        )
    return False


def write_csv(path: Path, rows: Sequence[Dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_outputs(summary_rows: Sequence[Dict[str, object]], verdict: Sequence[Dict[str, object]], cfg: OptionConfig) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    summary_path = ARTIFACT_DIR / "counterfactual_option_preservation_summary.csv"
    verdict_path = ARTIFACT_DIR / "counterfactual_option_preservation_verdict.csv"
    json_path = ARTIFACT_DIR / "counterfactual_option_preservation_results.json"
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
        "best_agent",
        "future_minus_greedy",
        "future_lost_option_steps",
        "greedy_lost_option_steps",
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
    parser.add_argument("--episodes", type=int, default=OptionConfig.episodes)
    parser.add_argument("--horizon", type=int, default=OptionConfig.horizon)
    parser.add_argument("--seed", type=int, default=OptionConfig.seed)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cfg = OptionConfig(episodes=args.episodes, horizon=args.horizon, seed=args.seed)
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
