#!/usr/bin/env python3
"""Long-horizon hidden-viability experiment.

The task tests self as a control variable. The agent can earn external reward
by working, but working consumes hidden energy and degrades hidden integrity.
Rest and repair preserve future ability to act. Exact internal state is only
available through an explicit inspect action.

The experiment asks whether a persistent estimate of "my future viability"
improves long-horizon survival and reward under partial observability.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import statistics
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Counter as CounterType, Dict, Iterable, List, Optional, Sequence, Tuple

from self_world_attribution import stable_episode_seed


ACTIONS = ["work", "rest", "repair", "inspect"]


@dataclass(frozen=True)
class ViabilityConfig:
    episodes: int = 500
    horizon: int = 80
    seed: int = 20260530
    death_penalty: float = 100.0
    tolerance: float = 1e-9


@dataclass(frozen=True)
class ScenarioParams:
    work_energy: float
    work_damage: float
    drift_step: Optional[int] = None
    drift_work_energy: Optional[float] = None
    drift_work_damage: Optional[float] = None


SCENARIOS: Dict[str, ScenarioParams] = {
    "low_stress": ScenarioParams(work_energy=0.8, work_damage=0.1),
    "energy_stress": ScenarioParams(work_energy=8.0, work_damage=0.4),
    "damage_stress": ScenarioParams(work_energy=2.0, work_damage=5.0),
    "combined_drift": ScenarioParams(
        work_energy=4.5,
        work_damage=2.0,
        drift_step=35,
        drift_work_energy=8.5,
        drift_work_damage=4.5,
    ),
}


@dataclass
class Observation:
    reward: float
    survived: bool
    low_energy_signal: bool
    low_integrity_signal: bool
    inspected_energy: Optional[float]
    inspected_integrity: Optional[float]


@dataclass
class EpisodeResult:
    scenario: str
    agent: str
    survived: bool
    steps_survived: int
    external_reward: float
    total_value: float
    work_count: int
    rest_count: int
    repair_count: int
    inspect_count: int
    mean_energy_mae: Optional[float]
    mean_integrity_mae: Optional[float]


class ViabilityWorld:
    def __init__(self, scenario: str, rng: random.Random) -> None:
        self.scenario = scenario
        self.params = SCENARIOS[scenario]
        self.rng = rng
        self.energy = rng.uniform(82.0, 92.0)
        self.integrity = rng.uniform(84.0, 94.0)
        self.work_energy = self.params.work_energy
        self.work_damage = self.params.work_damage
        self.alive = True

    def maybe_drift(self, t: int) -> None:
        if self.params.drift_step is None or t != self.params.drift_step:
            return
        assert self.params.drift_work_energy is not None
        assert self.params.drift_work_damage is not None
        self.work_energy = self.params.drift_work_energy
        self.work_damage = self.params.drift_work_damage

    def step(self, action: str, t: int) -> Observation:
        self.maybe_drift(t)
        reward = 0.0
        inspected_energy = None
        inspected_integrity = None

        if action == "work":
            reward = 10.0
            if self.energy < 20.0 or self.integrity < 20.0:
                reward *= 0.35
            self.energy -= self.work_energy
            self.integrity -= self.work_damage
        elif action == "rest":
            self.energy += 24.0
            self.integrity -= 0.2
        elif action == "repair":
            self.energy -= 3.0
            self.integrity += 26.0
        elif action == "inspect":
            self.energy -= 0.5
            inspected_energy = clamp(self.energy + self.rng.gauss(0.0, 2.0), 0.0, 100.0)
            inspected_integrity = clamp(self.integrity + self.rng.gauss(0.0, 2.0), 0.0, 100.0)
        else:
            raise ValueError(f"unknown action: {action}")

        self.energy = clamp(self.energy, -100.0, 100.0)
        self.integrity = clamp(self.integrity, -100.0, 100.0)
        self.alive = self.energy > 0.0 and self.integrity > 0.0

        return Observation(
            reward=reward if self.alive else 0.0,
            survived=self.alive,
            low_energy_signal=self.energy < 8.0,
            low_integrity_signal=self.integrity < 8.0,
            inspected_energy=inspected_energy,
            inspected_integrity=inspected_integrity,
        )


class BaseAgent:
    name = "base"

    def reset(self, cfg: ViabilityConfig) -> None:
        self.cfg = cfg

    def set_world(self, world: ViabilityWorld) -> None:
        pass

    def act(self, t: int) -> str:
        raise NotImplementedError

    def observe(self, action: str, obs: Observation) -> None:
        pass

    def estimates(self) -> Tuple[Optional[float], Optional[float]]:
        return None, None


class TaskOnlyAgent(BaseAgent):
    name = "task_only_world_reward"

    def act(self, t: int) -> str:
        return "work"


class FixedScheduleAgent(BaseAgent):
    name = "fixed_schedule_memory"

    def act(self, t: int) -> str:
        cycle = t % 10
        if cycle == 8:
            return "repair"
        if cycle in {4, 9}:
            return "rest"
        return "work"


class SymptomReactiveAgent(BaseAgent):
    name = "symptom_reactive"

    def reset(self, cfg: ViabilityConfig) -> None:
        super().reset(cfg)
        self.resting = 0
        self.repairing = 0

    def act(self, t: int) -> str:
        if self.repairing > 0:
            self.repairing -= 1
            return "repair"
        if self.resting > 0:
            self.resting -= 1
            return "rest"
        return "work"

    def observe(self, action: str, obs: Observation) -> None:
        if obs.low_integrity_signal:
            self.repairing = max(self.repairing, 2)
        if obs.low_energy_signal:
            self.resting = max(self.resting, 1)


class SelfStateAgent(BaseAgent):
    name = "persistent_self_state"

    def reset(self, cfg: ViabilityConfig) -> None:
        super().reset(cfg)
        self.energy_hat = 86.0
        self.integrity_hat = 88.0
        self.uncertainty = 10.0
        self.last_inspect = -999

    def act(self, t: int) -> str:
        if t == 0 or self.uncertainty > 28.0 or t - self.last_inspect > 19:
            self.last_inspect = t
            return "inspect"
        if self.integrity_hat < 55.0 or self.integrity_hat - 3 * 3.0 < 42.0:
            return "repair"
        if self.energy_hat < 45.0 or self.energy_hat - 3 * 6.0 < 30.0:
            return "rest"
        return "work"

    def observe(self, action: str, obs: Observation) -> None:
        self.apply_nominal_transition(action)
        if obs.inspected_energy is not None and obs.inspected_integrity is not None:
            self.energy_hat = obs.inspected_energy
            self.integrity_hat = obs.inspected_integrity
            self.uncertainty = 2.0
        else:
            self.uncertainty += 2.0
            if obs.low_energy_signal:
                self.energy_hat = min(self.energy_hat, 24.0)
            if obs.low_integrity_signal:
                self.integrity_hat = min(self.integrity_hat, 24.0)

        self.energy_hat = clamp(self.energy_hat, 0.0, 100.0)
        self.integrity_hat = clamp(self.integrity_hat, 0.0, 100.0)

    def apply_nominal_transition(self, action: str) -> None:
        if action == "work":
            self.energy_hat -= 5.5
            self.integrity_hat -= 2.4
        elif action == "rest":
            self.energy_hat += 24.0
            self.integrity_hat -= 0.2
        elif action == "repair":
            self.energy_hat -= 3.0
            self.integrity_hat += 26.0
        elif action == "inspect":
            self.energy_hat -= 0.5

    def estimates(self) -> Tuple[Optional[float], Optional[float]]:
        return self.energy_hat, self.integrity_hat


class SelfStateAblationAgent(SelfStateAgent):
    name = "self_state_ablation"

    def act(self, t: int) -> str:
        if t == 0 or t - self.last_inspect > 13:
            self.last_inspect = t
            return "inspect"
        return "work"


class OracleSelfStateAgent(BaseAgent):
    name = "oracle_self_state"

    def set_world(self, world: ViabilityWorld) -> None:
        self.world = world

    def act(self, t: int) -> str:
        energy = self.world.energy
        integrity = self.world.integrity
        work_energy = self.world.work_energy
        work_damage = self.world.work_damage
        if integrity < 45.0 or integrity - 4 * work_damage < 22.0:
            return "repair"
        if energy < 40.0 or energy - 4 * work_energy < 20.0:
            return "rest"
        return "work"

    def estimates(self) -> Tuple[Optional[float], Optional[float]]:
        return self.world.energy, self.world.integrity


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def run_episode(agent: BaseAgent, scenario: str, episode: int, cfg: ViabilityConfig) -> EpisodeResult:
    seed = stable_episode_seed(cfg.seed, scenario, episode)
    rng = random.Random(seed)
    world = ViabilityWorld(scenario, rng)
    agent.reset(cfg)
    agent.set_world(world)
    action_counts: CounterType[str] = Counter()
    energy_errors: List[float] = []
    integrity_errors: List[float] = []
    reward_total = 0.0
    steps_survived = 0

    for t in range(cfg.horizon):
        if not world.alive:
            break
        action = agent.act(t)
        action_counts[action] += 1
        obs = world.step(action, t)
        reward_total += obs.reward
        agent.observe(action, obs)
        energy_hat, integrity_hat = agent.estimates()
        if energy_hat is not None:
            energy_errors.append(abs(energy_hat - world.energy))
        if integrity_hat is not None:
            integrity_errors.append(abs(integrity_hat - world.integrity))
        if obs.survived:
            steps_survived += 1
        else:
            break

    total_value = reward_total if world.alive else reward_total - cfg.death_penalty
    return EpisodeResult(
        scenario=scenario,
        agent=agent.name,
        survived=world.alive,
        steps_survived=steps_survived,
        external_reward=reward_total,
        total_value=total_value,
        work_count=action_counts["work"],
        rest_count=action_counts["rest"],
        repair_count=action_counts["repair"],
        inspect_count=action_counts["inspect"],
        mean_energy_mae=statistics.fmean(energy_errors) if energy_errors else None,
        mean_integrity_mae=statistics.fmean(integrity_errors) if integrity_errors else None,
    )


def summarize(results: Sequence[EpisodeResult]) -> List[Dict[str, object]]:
    grouped: Dict[Tuple[str, str], List[EpisodeResult]] = {}
    for result in results:
        grouped.setdefault((result.scenario, result.agent), []).append(result)

    rows: List[Dict[str, object]] = []
    for (scenario, agent), items in sorted(grouped.items()):
        energy_errors = [item.mean_energy_mae for item in items if item.mean_energy_mae is not None]
        integrity_errors = [
            item.mean_integrity_mae for item in items if item.mean_integrity_mae is not None
        ]
        rows.append(
            {
                "scenario": scenario,
                "agent": agent,
                "episodes": len(items),
                "survival_rate": rate(item.survived for item in items),
                "mean_steps_survived": statistics.fmean(item.steps_survived for item in items),
                "mean_external_reward": statistics.fmean(item.external_reward for item in items),
                "mean_total_value": statistics.fmean(item.total_value for item in items),
                "mean_work_count": statistics.fmean(item.work_count for item in items),
                "mean_rest_count": statistics.fmean(item.rest_count for item in items),
                "mean_repair_count": statistics.fmean(item.repair_count for item in items),
                "mean_inspect_count": statistics.fmean(item.inspect_count for item in items),
                "mean_energy_mae": mean_or_none(energy_errors),
                "mean_integrity_mae": mean_or_none(integrity_errors),
            }
        )
    return rows


def rate(values: Iterable[bool]) -> float:
    values = list(values)
    return sum(1 for value in values if value) / len(values)


def mean_or_none(values: Sequence[float]) -> Optional[float]:
    if not values:
        return None
    return statistics.fmean(values)


def write_outputs(rows: Sequence[Dict[str, object]], cfg: ViabilityConfig, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "hidden_viability_results.json"
    csv_path = output_dir / "hidden_viability_summary.csv"

    with json_path.open("w", encoding="utf-8") as handle:
        json.dump({"config": asdict(cfg), "summary": list(rows)}, handle, indent=2)
        handle.write("\n")

    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def print_summary(rows: Sequence[Dict[str, object]]) -> None:
    columns = [
        "scenario",
        "agent",
        "survival_rate",
        "mean_steps_survived",
        "mean_external_reward",
        "mean_total_value",
        "mean_work_count",
        "mean_rest_count",
        "mean_repair_count",
        "mean_inspect_count",
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
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=ViabilityConfig.episodes)
    parser.add_argument("--horizon", type=int, default=ViabilityConfig.horizon)
    parser.add_argument("--seed", type=int, default=ViabilityConfig.seed)
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = ViabilityConfig(episodes=args.episodes, horizon=args.horizon, seed=args.seed)
    agent_factories = [
        TaskOnlyAgent,
        FixedScheduleAgent,
        SymptomReactiveAgent,
        SelfStateAblationAgent,
        SelfStateAgent,
        OracleSelfStateAgent,
    ]
    results: List[EpisodeResult] = []
    for scenario in SCENARIOS:
        for agent_factory in agent_factories:
            for episode in range(cfg.episodes):
                results.append(run_episode(agent_factory(), scenario, episode, cfg))
    rows = summarize(results)
    write_outputs(rows, cfg, args.output_dir)
    print_summary(rows)


if __name__ == "__main__":
    main()
