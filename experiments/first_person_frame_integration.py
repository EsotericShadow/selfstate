#!/usr/bin/env python3
"""First-person frame test for centered observation/action integration.

The agent observes the goal in world-relative coordinates, but its motor
commands are body-relative. A hidden body orientation determines what
"forward", "left", "right", and "back" do in world coordinates.

The question is whether a centered frame variable is useful: not a conscious
point of view, but a persistent estimate of how this body is oriented so
observations can be transformed into actions.
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
COMMANDS = ("forward", "right", "back", "left")
DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))


@dataclass(frozen=True)
class FrameConfig:
    episodes: int = 500
    horizon: int = 36
    drift_step: int = 5
    target_radius: int = 12
    seed: int = 20260530


@dataclass(frozen=True)
class FrameScenario:
    name: str
    orientation_mode: str
    drift: bool


@dataclass
class Observation:
    t: int
    goal_dx: int
    goal_dy: int
    reached: bool


@dataclass
class EpisodeResult:
    scenario: str
    agent: str
    success: bool
    steps_to_goal: Optional[int]
    final_distance: int
    total_loss: float
    calibration_count: int
    prediction_errors: int
    final_orientation_error: Optional[int]


SCENARIOS = [
    FrameScenario("aligned_control", orientation_mode="north", drift=False),
    FrameScenario("hidden_orientation", orientation_mode="random", drift=False),
    FrameScenario("orientation_drift", orientation_mode="random", drift=True),
]


class BodyFrameWorld:
    def __init__(self, scenario: FrameScenario, rng: random.Random, cfg: FrameConfig) -> None:
        self.scenario = scenario
        self.rng = rng
        self.cfg = cfg
        self.x = 0
        self.y = 0
        self.goal_x, self.goal_y = sample_goal(rng, cfg.target_radius)
        self.orientation = 0 if scenario.orientation_mode == "north" else rng.randrange(4)
        self.drifted = False

    def observation(self, t: int) -> Observation:
        return Observation(
            t=t,
            goal_dx=self.goal_x - self.x,
            goal_dy=self.goal_y - self.y,
            reached=self.x == self.goal_x and self.y == self.goal_y,
        )

    def step(self, command: str, t: int) -> Tuple[Observation, Tuple[int, int]]:
        if self.scenario.drift and not self.drifted and t == self.cfg.drift_step:
            self.orientation = choose_different(self.rng, self.orientation)
            self.drifted = True
        dx, dy = command_vector(command, self.orientation)
        self.x += dx
        self.y += dy
        return self.observation(t + 1), (dx, dy)


class BaseAgent:
    name = "base"

    def reset(self, scenario: FrameScenario, cfg: FrameConfig) -> None:
        self.scenario = scenario
        self.cfg = cfg
        self.previous_obs: Optional[Observation] = None
        self.predicted_move: Optional[Tuple[int, int]] = None
        self.calibration_count = 0
        self.prediction_errors = 0

    def act(self, obs: Observation) -> str:
        raise NotImplementedError

    def observe(self, command: str, previous: Observation, current: Observation, actual_move: Tuple[int, int]) -> None:
        pass

    def orientation_error(self, true_orientation: int) -> Optional[int]:
        return None


class NorthAssumptionAgent(BaseAgent):
    name = "north_assumption"

    def act(self, obs: Observation) -> str:
        return command_toward_goal(obs.goal_dx, obs.goal_dy, orientation_hat=0)


class ActionTableAgent(BaseAgent):
    name = "action_table_frame"

    def reset(self, scenario: FrameScenario, cfg: FrameConfig) -> None:
        super().reset(scenario, cfg)
        self.effects: Dict[str, Tuple[int, int]] = {
            "forward": (0, 1),
            "right": (1, 0),
            "back": (0, -1),
            "left": (-1, 0),
        }
        self.next_probe_index = 0
        self.force_probe = scenario.orientation_mode == "random"

    def act(self, obs: Observation) -> str:
        if self.force_probe:
            command = COMMANDS[self.next_probe_index % len(COMMANDS)]
            self.next_probe_index += 1
            self.force_probe = False
            self.calibration_count += 1
            return command
        return min(
            COMMANDS,
            key=lambda command: manhattan(obs.goal_dx - self.effects[command][0], obs.goal_dy - self.effects[command][1]),
        )

    def observe(self, command: str, previous: Observation, current: Observation, actual_move: Tuple[int, int]) -> None:
        predicted = self.effects[command]
        if predicted != actual_move:
            self.prediction_errors += 1
            if self.scenario.drift:
                self.force_probe = True
        self.effects[command] = actual_move


class CenteredFrameAgent(BaseAgent):
    name = "centered_frame"
    recalibrate_on_error = True

    def reset(self, scenario: FrameScenario, cfg: FrameConfig) -> None:
        super().reset(scenario, cfg)
        self.orientation_hat: Optional[int] = 0 if scenario.orientation_mode == "north" else None
        self.need_probe = self.orientation_hat is None

    def act(self, obs: Observation) -> str:
        if self.need_probe:
            self.need_probe = False
            self.calibration_count += 1
            return "forward"
        assert self.orientation_hat is not None
        return command_toward_goal(obs.goal_dx, obs.goal_dy, self.orientation_hat)

    def observe(self, command: str, previous: Observation, current: Observation, actual_move: Tuple[int, int]) -> None:
        if command == "forward" and (self.orientation_hat is None or self.calibration_count > 0):
            observed_orientation = orientation_from_vector(actual_move)
            if observed_orientation is not None:
                self.orientation_hat = observed_orientation
            return

        if self.orientation_hat is None:
            return
        predicted = command_vector(command, self.orientation_hat)
        if predicted != actual_move:
            self.prediction_errors += 1
            if self.recalibrate_on_error:
                self.orientation_hat = None
                self.need_probe = True

    def orientation_error(self, true_orientation: int) -> Optional[int]:
        if self.orientation_hat is None:
            return None
        return circular_error(self.orientation_hat, true_orientation)


class CenteredFrameNoRecalibrationAgent(CenteredFrameAgent):
    name = "centered_frame_no_recalibration"
    recalibrate_on_error = False


class OracleFrameAgent(BaseAgent):
    name = "oracle_frame"

    def reset(self, scenario: FrameScenario, cfg: FrameConfig) -> None:
        super().reset(scenario, cfg)
        self.true_orientation = 0

    def update_true_orientation(self, orientation: int) -> None:
        self.true_orientation = orientation

    def act(self, obs: Observation) -> str:
        return command_toward_goal(obs.goal_dx, obs.goal_dy, self.true_orientation)

    def orientation_error(self, true_orientation: int) -> Optional[int]:
        return 0


AGENT_FACTORIES = [
    NorthAssumptionAgent,
    ActionTableAgent,
    CenteredFrameNoRecalibrationAgent,
    CenteredFrameAgent,
    OracleFrameAgent,
]


def sample_goal(rng: random.Random, radius: int) -> Tuple[int, int]:
    while True:
        x = rng.randint(-radius, radius)
        y = rng.randint(-radius, radius)
        if abs(x) + abs(y) >= radius:
            return x, y


def command_vector(command: str, orientation: int) -> Tuple[int, int]:
    body_index = COMMANDS.index(command)
    return DIRS[(orientation + body_index) % 4]


def command_toward_goal(goal_dx: int, goal_dy: int, orientation_hat: int) -> str:
    desired = desired_world_direction(goal_dx, goal_dy)
    body_index = (desired - orientation_hat) % 4
    return COMMANDS[body_index]


def desired_world_direction(goal_dx: int, goal_dy: int) -> int:
    if abs(goal_dx) >= abs(goal_dy) and goal_dx != 0:
        return 1 if goal_dx > 0 else 3
    if goal_dy != 0:
        return 0 if goal_dy > 0 else 2
    return 0


def orientation_from_vector(vector: Tuple[int, int]) -> Optional[int]:
    if vector not in DIRS:
        return None
    return DIRS.index(vector)


def choose_different(rng: random.Random, current: int) -> int:
    choices = [value for value in range(4) if value != current]
    return rng.choice(choices)


def manhattan(dx: int, dy: int) -> int:
    return abs(dx) + abs(dy)


def circular_error(a: int, b: int) -> int:
    diff = abs(a - b) % 4
    return min(diff, 4 - diff)


def stable_seed(seed: int, scenario: str, agent: str, episode: int) -> int:
    value = seed + episode * 1009
    for part in [scenario, agent]:
        for char in part:
            value = (value * 131 + ord(char)) % (2**32)
    return value


def run_episode(agent_factory, scenario: FrameScenario, episode: int, cfg: FrameConfig) -> EpisodeResult:
    rng = random.Random(stable_seed(cfg.seed, scenario.name, agent_factory.name, episode))
    world = BodyFrameWorld(scenario, rng, cfg)
    agent = agent_factory()
    agent.reset(scenario, cfg)
    obs = world.observation(0)
    total_loss = 0.0
    steps_to_goal: Optional[int] = None

    for t in range(cfg.horizon):
        if obs.reached:
            steps_to_goal = t
            break
        if isinstance(agent, OracleFrameAgent):
            agent.update_true_orientation(world.orientation)
        previous = obs
        command = agent.act(obs)
        obs, actual_move = world.step(command, t)
        agent.observe(command, previous, obs, actual_move)
        total_loss += manhattan(obs.goal_dx, obs.goal_dy)
        if obs.reached:
            steps_to_goal = t + 1
            break

    final_distance = manhattan(obs.goal_dx, obs.goal_dy)
    return EpisodeResult(
        scenario=scenario.name,
        agent=agent.name,
        success=final_distance == 0,
        steps_to_goal=steps_to_goal,
        final_distance=final_distance,
        total_loss=total_loss,
        calibration_count=agent.calibration_count,
        prediction_errors=agent.prediction_errors,
        final_orientation_error=agent.orientation_error(world.orientation),
    )


def summarize(results: Sequence[EpisodeResult]) -> List[Dict[str, object]]:
    grouped: Dict[Tuple[str, str], List[EpisodeResult]] = {}
    for result in results:
        grouped.setdefault((result.scenario, result.agent), []).append(result)
    rows = []
    for (scenario, agent), items in sorted(grouped.items()):
        orientation_errors = [
            item.final_orientation_error for item in items if item.final_orientation_error is not None
        ]
        reached_steps = [item.steps_to_goal for item in items if item.steps_to_goal is not None]
        rows.append(
            {
                "scenario": scenario,
                "agent": agent,
                "episodes": len(items),
                "success_rate": rate(item.success for item in items),
                "mean_steps_to_goal": mean_or_none(reached_steps),
                "mean_final_distance": statistics.fmean(item.final_distance for item in items),
                "mean_total_loss": statistics.fmean(item.total_loss for item in items),
                "mean_calibration_count": statistics.fmean(item.calibration_count for item in items),
                "mean_prediction_errors": statistics.fmean(item.prediction_errors for item in items),
                "mean_final_orientation_error": mean_or_none(orientation_errors),
            }
        )
    return rows


def verdict_rows(summary_rows: Sequence[Dict[str, object]]) -> List[Dict[str, object]]:
    verdict = []
    for scenario in sorted({str(row["scenario"]) for row in summary_rows}):
        rows = [row for row in summary_rows if row["scenario"] == scenario]
        ranked = sorted(rows, key=lambda row: (-float(row["success_rate"]), float(row["mean_final_distance"]), str(row["agent"])))
        best = ranked[0]
        north = next(row for row in rows if row["agent"] == "north_assumption")
        centered = next(row for row in rows if row["agent"] == "centered_frame")
        no_recal = next(row for row in rows if row["agent"] == "centered_frame_no_recalibration")
        verdict.append(
            {
                "scenario": scenario,
                "best_agent": best["agent"],
                "north_success_rate": north["success_rate"],
                "centered_success_rate": centered["success_rate"],
                "no_recalibration_success_rate": no_recal["success_rate"],
                "centered_minus_north": float(centered["success_rate"]) - float(north["success_rate"]),
                "centered_minus_no_recalibration": float(centered["success_rate"]) - float(no_recal["success_rate"]),
                "supports_boundary": scenario_supports_boundary(scenario, north, centered, no_recal),
            }
        )
    return verdict


def scenario_supports_boundary(
    scenario: str,
    north: Dict[str, object],
    centered: Dict[str, object],
    no_recal: Dict[str, object],
) -> bool:
    north_success = float(north["success_rate"])
    centered_success = float(centered["success_rate"])
    no_recal_success = float(no_recal["success_rate"])
    if scenario == "aligned_control":
        return north_success > 0.95 and abs(centered_success - north_success) < 0.05
    if scenario == "hidden_orientation":
        return centered_success > north_success + 0.35 and no_recal_success > north_success + 0.35
    if scenario == "orientation_drift":
        return centered_success > no_recal_success + 0.20 and centered_success > north_success + 0.35
    return False


def rate(values: Iterable[bool]) -> float:
    values = list(values)
    return sum(1 for value in values if value) / len(values)


def mean_or_none(values: Sequence[Optional[float]]) -> Optional[float]:
    filtered = [float(value) for value in values if value is not None]
    if not filtered:
        return None
    return statistics.fmean(filtered)


def write_csv(path: Path, rows: Sequence[Dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_outputs(summary_rows: Sequence[Dict[str, object]], verdict: Sequence[Dict[str, object]], cfg: FrameConfig) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    summary_path = ARTIFACT_DIR / "first_person_frame_summary.csv"
    verdict_path = ARTIFACT_DIR / "first_person_frame_verdict.csv"
    json_path = ARTIFACT_DIR / "first_person_frame_results.json"
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
        "north_success_rate",
        "centered_success_rate",
        "no_recalibration_success_rate",
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
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.3f}"
    return str(value)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=FrameConfig.episodes)
    parser.add_argument("--horizon", type=int, default=FrameConfig.horizon)
    parser.add_argument("--drift-step", type=int, default=FrameConfig.drift_step)
    parser.add_argument("--target-radius", type=int, default=FrameConfig.target_radius)
    parser.add_argument("--seed", type=int, default=FrameConfig.seed)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    cfg = FrameConfig(
        episodes=args.episodes,
        horizon=args.horizon,
        drift_step=args.drift_step,
        target_radius=args.target_radius,
        seed=args.seed,
    )
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
