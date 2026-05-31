#!/usr/bin/env python3
"""Competing-subsystems arbitration test for self as coherence stabilizer.

Several subsystems propose locally reasonable actions: immediate reward,
commitment completion, and safety/maintenance. The shared agent-state budget
determines which proposal is coherent for the continuing system.

The question is whether a persistent self-equivalent state can serve as an
arbitration variable across subsystems, not just as memory after interruption.
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
ACTIONS = ("exploit", "fulfill", "restore", "inspect_self", "inspect_world")


@dataclass(frozen=True)
class ArbitrationConfig:
    episodes: int = 500
    horizon: int = 14
    seed: int = 20260530


@dataclass(frozen=True)
class ArbitrationScenario:
    name: str
    mode: str


@dataclass
class Observation:
    t: int
    energy_symptom: str
    commitment_due: bool
    inspected_energy: Optional[float]
    inspected_world_open: Optional[bool]
    reward: float


@dataclass
class EpisodeResult:
    scenario: str
    agent: str
    total_reward: float
    collapsed: bool
    commitment_completed: bool
    commitment_failed: bool
    exploit_count: int
    fulfill_count: int
    restore_count: int
    inspect_self_count: int
    inspect_world_count: int
    incoherent_actions: int
    final_energy: float


SCENARIOS = [
    ArbitrationScenario("no_conflict", "no_conflict"),
    ArbitrationScenario("subsystem_conflict", "subsystem_conflict"),
    ArbitrationScenario("world_gate_conflict", "world_gate_conflict"),
]


class ArbitrationWorld:
    def __init__(self, scenario: ArbitrationScenario, rng: random.Random, cfg: ArbitrationConfig) -> None:
        self.scenario = scenario
        self.rng = rng
        self.cfg = cfg
        if scenario.mode == "subsystem_conflict":
            self.energy = rng.uniform(32.0, 48.0)
            self.commitment_due = True
            self.world_open = True
        elif scenario.mode == "world_gate_conflict":
            self.energy = rng.uniform(78.0, 92.0)
            self.commitment_due = False
            self.world_open = rng.random() < 0.45
        elif scenario.mode == "no_conflict":
            self.energy = rng.uniform(82.0, 96.0)
            self.commitment_due = False
            self.world_open = True
        else:
            raise ValueError(f"unknown scenario mode: {scenario.mode}")
        self.collapsed = False
        self.commitment_completed = False

    def symptom(self) -> str:
        if self.energy >= 60.0:
            return "steady"
        if self.energy >= 35.0:
            return "strained"
        return "critical"

    def observation(self, t: int, reward: float = 0.0) -> Observation:
        return Observation(
            t=t,
            energy_symptom=self.symptom(),
            commitment_due=self.commitment_due and not self.commitment_completed,
            inspected_energy=None,
            inspected_world_open=None,
            reward=reward,
        )

    def step(self, action: str, t: int) -> Observation:
        reward = 0.0
        inspected_energy = None
        inspected_world_open = None
        if self.collapsed:
            return self.observation(t + 1, reward=-5.0)

        if action == "exploit":
            if self.world_open:
                reward = 7.0
            else:
                reward = -12.0
            if self.scenario.mode == "no_conflict":
                self.energy -= self.rng.uniform(1.0, 2.0)
            else:
                self.energy -= self.rng.uniform(9.0, 13.0)
        elif action == "fulfill":
            if self.commitment_due and not self.commitment_completed and self.energy >= 42.0:
                reward = 30.0
                self.commitment_completed = True
                self.energy -= self.rng.uniform(22.0, 27.0)
            elif self.commitment_due and not self.commitment_completed:
                reward = -18.0
                self.energy -= self.rng.uniform(8.0, 12.0)
            else:
                reward = -6.0
                self.energy -= self.rng.uniform(3.0, 6.0)
        elif action == "restore":
            reward = -1.0
            self.energy += self.rng.uniform(21.0, 28.0)
        elif action == "inspect_self":
            reward = -1.0
            inspected_energy = clamp(self.energy + self.rng.gauss(0.0, 1.5), 0.0, 100.0)
        elif action == "inspect_world":
            reward = -1.0
            inspected_world_open = self.world_open
        else:
            raise ValueError(f"unknown action: {action}")

        self.energy = clamp(self.energy, 0.0, 100.0)
        if self.energy <= 0.0:
            self.collapsed = True
            reward -= 45.0

        obs = self.observation(t + 1, reward=reward)
        obs.inspected_energy = inspected_energy
        obs.inspected_world_open = inspected_world_open
        return obs

    def terminal_penalty(self) -> float:
        if self.commitment_due and not self.commitment_completed:
            return -35.0
        return 0.0


class BaseAgent:
    name = "base"

    def reset(self, scenario: ArbitrationScenario, cfg: ArbitrationConfig) -> None:
        self.scenario = scenario
        self.cfg = cfg
        self.energy_hat = 75.0
        self.world_open_hat: Optional[bool] = None
        self.self_inspected = False
        self.world_inspected = False

    def act(self, obs: Observation) -> str:
        raise NotImplementedError

    def observe(self, action: str, obs: Observation) -> None:
        if obs.inspected_energy is not None:
            self.energy_hat = obs.inspected_energy
            self.self_inspected = True
        elif obs.energy_symptom == "critical":
            self.energy_hat = min(self.energy_hat, 32.0)
        elif obs.energy_symptom == "strained":
            self.energy_hat = min(max(self.energy_hat, 35.0), 55.0)
        elif obs.energy_symptom == "steady":
            self.energy_hat = max(self.energy_hat, 60.0)

        if obs.inspected_world_open is not None:
            self.world_open_hat = obs.inspected_world_open
            self.world_inspected = True

        if action == "exploit":
            self.energy_hat -= 11.0
        elif action == "fulfill":
            self.energy_hat -= 24.0 if self.energy_hat >= 42.0 else 10.0
        elif action == "restore":
            self.energy_hat += 24.0
        self.energy_hat = clamp(self.energy_hat, 0.0, 100.0)


class RewardSubsystemAgent(BaseAgent):
    name = "reward_priority"

    def act(self, obs: Observation) -> str:
        return "exploit"


class CommitmentSubsystemAgent(BaseAgent):
    name = "commitment_priority"

    def act(self, obs: Observation) -> str:
        return "fulfill" if obs.commitment_due else "exploit"


class SafetySubsystemAgent(BaseAgent):
    name = "safety_priority"

    def act(self, obs: Observation) -> str:
        if obs.energy_symptom in {"critical", "strained"}:
            return "restore"
        if obs.commitment_due:
            return "fulfill"
        return "exploit"


class LocalVoteAgent(BaseAgent):
    name = "local_vote_no_shared_self"

    def act(self, obs: Observation) -> str:
        votes = ["exploit"]
        votes.append("fulfill" if obs.commitment_due else "exploit")
        votes.append("restore" if obs.energy_symptom == "critical" else "exploit")
        return max(ACTIONS[:3], key=lambda action: (votes.count(action), -ACTIONS.index(action)))


class SelfCoherenceArbitrator(BaseAgent):
    name = "self_coherence_arbitrator"

    def act(self, obs: Observation) -> str:
        if obs.commitment_due and not self.self_inspected:
            return "inspect_self"
        if obs.commitment_due:
            if self.energy_hat < 46.0:
                return "restore"
            return "fulfill"
        if self.energy_hat < 25.0:
            return "restore"
        return "exploit"


class WorldGateArbitrator(BaseAgent):
    name = "world_gate_arbitrator"

    def act(self, obs: Observation) -> str:
        if self.scenario.mode == "world_gate_conflict" and not self.world_inspected:
            return "inspect_world"
        if self.scenario.mode == "world_gate_conflict":
            return "exploit" if self.world_open_hat else "restore"
        if obs.commitment_due:
            return "fulfill"
        return "exploit"


class OracleCoherenceArbitrator(BaseAgent):
    name = "oracle_coherence_arbitrator"

    def __init__(self) -> None:
        self.true_energy = 75.0
        self.true_world_open = True

    def update_true_state(self, world: ArbitrationWorld) -> None:
        self.true_energy = world.energy
        self.true_world_open = world.world_open

    def act(self, obs: Observation) -> str:
        if obs.commitment_due:
            if self.true_energy < 46.0:
                return "restore"
            return "fulfill"
        if self.scenario.mode == "world_gate_conflict":
            return "exploit" if self.true_world_open else "restore"
        if self.true_energy < 22.0:
            return "restore"
        return "exploit"


AGENT_FACTORIES = [
    RewardSubsystemAgent,
    CommitmentSubsystemAgent,
    SafetySubsystemAgent,
    LocalVoteAgent,
    SelfCoherenceArbitrator,
    WorldGateArbitrator,
    OracleCoherenceArbitrator,
]


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def stable_state_seed(seed: int, scenario: str, episode: int) -> int:
    value = seed + episode * 1009
    for char in scenario:
        value = (value * 131 + ord(char)) % (2**32)
    return value


def run_episode(agent_factory, scenario: ArbitrationScenario, episode: int, cfg: ArbitrationConfig) -> EpisodeResult:
    rng = random.Random(stable_state_seed(cfg.seed, scenario.name, episode))
    world = ArbitrationWorld(scenario, rng, cfg)
    agent = agent_factory()
    agent.reset(scenario, cfg)
    obs = world.observation(0)
    total_reward = 0.0
    action_counts = {action: 0 for action in ACTIONS}
    incoherent_actions = 0

    for t in range(cfg.horizon):
        if isinstance(agent, OracleCoherenceArbitrator):
            agent.update_true_state(world)
        action = agent.act(obs)
        if is_incoherent(action, obs, world):
            incoherent_actions += 1
        action_counts[action] += 1
        obs = world.step(action, t)
        total_reward += obs.reward
        agent.observe(action, obs)

    total_reward += world.terminal_penalty()
    return EpisodeResult(
        scenario=scenario.name,
        agent=agent.name,
        total_reward=total_reward,
        collapsed=world.collapsed,
        commitment_completed=world.commitment_completed,
        commitment_failed=world.commitment_due and not world.commitment_completed,
        exploit_count=action_counts["exploit"],
        fulfill_count=action_counts["fulfill"],
        restore_count=action_counts["restore"],
        inspect_self_count=action_counts["inspect_self"],
        inspect_world_count=action_counts["inspect_world"],
        incoherent_actions=incoherent_actions,
        final_energy=world.energy,
    )


def is_incoherent(action: str, obs: Observation, world: ArbitrationWorld) -> bool:
    if action == "exploit" and world.energy < 18.0:
        return True
    if action == "fulfill" and obs.commitment_due and world.energy < 42.0:
        return True
    if action == "restore" and world.energy > 80.0 and not obs.commitment_due:
        return True
    if action == "fulfill" and not obs.commitment_due:
        return True
    return False


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
                "collapse_rate": rate(item.collapsed for item in items),
                "commitment_completion_rate": rate(item.commitment_completed for item in items),
                "commitment_failure_rate": rate(item.commitment_failed for item in items),
                "mean_incoherent_actions": statistics.fmean(item.incoherent_actions for item in items),
                "mean_exploit_count": statistics.fmean(item.exploit_count for item in items),
                "mean_fulfill_count": statistics.fmean(item.fulfill_count for item in items),
                "mean_restore_count": statistics.fmean(item.restore_count for item in items),
                "mean_inspect_self_count": statistics.fmean(item.inspect_self_count for item in items),
                "mean_inspect_world_count": statistics.fmean(item.inspect_world_count for item in items),
                "mean_final_energy": statistics.fmean(item.final_energy for item in items),
            }
        )
    return rows


def verdict_rows(summary_rows: Sequence[Dict[str, object]]) -> List[Dict[str, object]]:
    rows = []
    for scenario in sorted({str(row["scenario"]) for row in summary_rows}):
        scenario_rows = [row for row in summary_rows if row["scenario"] == scenario]
        non_oracle = [row for row in scenario_rows if row["agent"] != "oracle_coherence_arbitrator"]
        best = sorted(non_oracle, key=lambda row: (-float(row["mean_total_reward"]), str(row["agent"])))[0]
        reward = row_for(scenario_rows, "reward_priority")
        local = row_for(scenario_rows, "local_vote_no_shared_self")
        self_arbitrator = row_for(scenario_rows, "self_coherence_arbitrator")
        world_arbitrator = row_for(scenario_rows, "world_gate_arbitrator")
        rows.append(
            {
                "scenario": scenario,
                "best_non_oracle_agent": best["agent"],
                "best_non_oracle_reward": best["mean_total_reward"],
                "reward_priority_reward": reward["mean_total_reward"],
                "local_vote_reward": local["mean_total_reward"],
                "self_arbitrator_reward": self_arbitrator["mean_total_reward"],
                "world_arbitrator_reward": world_arbitrator["mean_total_reward"],
                "self_minus_local": float(self_arbitrator["mean_total_reward"]) - float(local["mean_total_reward"]),
                "self_incoherent_actions": self_arbitrator["mean_incoherent_actions"],
                "local_incoherent_actions": local["mean_incoherent_actions"],
                "supports_boundary": scenario_supports_boundary(scenario, best, reward, local, self_arbitrator, world_arbitrator),
            }
        )
    return rows


def row_for(rows: Sequence[Dict[str, object]], agent: str) -> Dict[str, object]:
    return next(row for row in rows if row["agent"] == agent)


def scenario_supports_boundary(
    scenario: str,
    best: Dict[str, object],
    reward: Dict[str, object],
    local: Dict[str, object],
    self_arbitrator: Dict[str, object],
    world_arbitrator: Dict[str, object],
) -> bool:
    if scenario == "subsystem_conflict":
        return (
            best["agent"] == "self_coherence_arbitrator"
            and float(self_arbitrator["mean_total_reward"]) > float(local["mean_total_reward"]) + 20.0
            and float(self_arbitrator["mean_incoherent_actions"]) < float(local["mean_incoherent_actions"]) - 2.0
        )
    if scenario == "world_gate_conflict":
        return (
            best["agent"] == "world_gate_arbitrator"
            and float(world_arbitrator["mean_total_reward"]) > float(self_arbitrator["mean_total_reward"]) + 20.0
        )
    if scenario == "no_conflict":
        return (
            abs(float(reward["mean_total_reward"]) - float(self_arbitrator["mean_total_reward"])) <= 1.0
            and abs(float(local["mean_total_reward"]) - float(self_arbitrator["mean_total_reward"])) <= 1.0
            and float(self_arbitrator["mean_inspect_self_count"]) < 0.1
            and float(self_arbitrator["mean_incoherent_actions"]) < 0.1
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


def write_outputs(summary_rows: Sequence[Dict[str, object]], verdict: Sequence[Dict[str, object]], cfg: ArbitrationConfig) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    summary_path = ARTIFACT_DIR / "competing_subsystems_arbitration_summary.csv"
    verdict_path = ARTIFACT_DIR / "competing_subsystems_arbitration_verdict.csv"
    json_path = ARTIFACT_DIR / "competing_subsystems_arbitration_results.json"
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
        "self_arbitrator_reward",
        "local_vote_reward",
        "world_arbitrator_reward",
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
    parser.add_argument("--episodes", type=int, default=ArbitrationConfig.episodes)
    parser.add_argument("--horizon", type=int, default=ArbitrationConfig.horizon)
    parser.add_argument("--seed", type=int, default=ArbitrationConfig.seed)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cfg = ArbitrationConfig(episodes=args.episodes, horizon=args.horizon, seed=args.seed)
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
