#!/usr/bin/env python3
"""Minimal self/world attribution experiment.

The task is intentionally small. It tests whether a controller benefits from
factorizing prediction error into:

- a world term: external drift/wind;
- a self term: the agent's own actuator gain.

The factorized agent is not evidence of consciousness and is not evidence that
selfhood has emerged naturally. It is a controlled toy model for the weaker
claim in docs/05_formal_core.md: when hidden agent-state variables affect future
outcomes, policies need information equivalent to those variables.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
import statistics
from collections import deque
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Deque, Dict, Iterable, List, Optional, Sequence, Tuple


@dataclass(frozen=True)
class ExperimentConfig:
    episodes: int = 500
    horizon: int = 36
    perturb_step: int = 12
    target_abs: float = 30.0
    max_action: int = 5
    tolerance: float = 2.0
    action_cost: float = 0.05
    estimate_window: int = 8
    error_threshold: float = 2.5
    seed: int = 20260530


@dataclass
class StepRecord:
    t: int
    target: float
    action: int
    position: float
    distance: float
    gain: float
    wind: float
    gain_hat: Optional[float]
    wind_hat: Optional[float]


@dataclass
class EpisodeResult:
    agent: str
    scenario: str
    pre_success: bool
    post_success: bool
    post_recovery_steps: Optional[int]
    final_distance: float
    mean_post_distance: float
    total_loss: float
    gain_mae: Optional[float]
    wind_mae: Optional[float]


class DriftWorld:
    def __init__(self, scenario: str, rng: random.Random) -> None:
        self.scenario = scenario
        self.rng = rng
        self.position = 0.0
        self.gain = 1.0
        self.wind = 0.0
        self.perturbed = False

        if scenario == "mixed_hidden":
            self.gain = rng.choice([-1.0, 0.5, 1.0, 1.5])
            self.wind = rng.choice([-1.5, 0.0, 1.5])

    def perturb(self) -> None:
        if self.perturbed:
            return
        self.perturbed = True

        if self.scenario == "static_goal_switch":
            return

        if self.scenario == "world_drift":
            self.wind = self.rng.choice([-2.0, -1.0, 1.0, 2.0])
            return

        if self.scenario == "self_drift":
            self.gain = self.rng.choice([-1.0, 0.5, 1.5])
            return

        if self.scenario == "mixed_hidden":
            change = self.rng.choice(["self", "world", "both"])
            if change in {"self", "both"}:
                self.gain = choose_different(self.rng, [-1.0, 0.5, 1.0, 1.5], self.gain)
            if change in {"world", "both"}:
                self.wind = choose_different(self.rng, [-1.5, 0.0, 1.5], self.wind)
            return

        raise ValueError(f"unknown scenario: {self.scenario}")

    def step(self, action: int) -> Tuple[float, float]:
        delta = self.gain * action + self.wind
        self.position += delta
        return self.position, delta


class BaseAgent:
    name = "base"

    def reset(self, cfg: ExperimentConfig) -> None:
        self.cfg = cfg
        self.actions = list(range(-cfg.max_action, cfg.max_action + 1))
        self._last_predicted_delta = 0.0

    def act(self, position: float, target: float, t: int) -> int:
        raise NotImplementedError

    def observe(self, old_position: float, action: int, new_position: float, target: float, t: int) -> None:
        pass

    def estimates(self) -> Tuple[Optional[float], Optional[float]]:
        return None, None


class ReactiveAgent(BaseAgent):
    name = "reactive_world_only"

    def act(self, position: float, target: float, t: int) -> int:
        desired = target - position
        action = int(round(clamp(desired, -self.cfg.max_action, self.cfg.max_action)))
        self._last_predicted_delta = float(action)
        return action


class AdaptiveAgent(BaseAgent):
    probe_template: Sequence[int]

    def reset(self, cfg: ExperimentConfig) -> None:
        super().reset(cfg)
        m = cfg.max_action
        half = max(1, m // 2)
        self.probe_template = [0, m, -m, half, -half]
        self.probe_queue: Deque[int] = deque(self.probe_template[:3])
        self._last_action_was_probe = False

    def next_probe(self) -> Optional[int]:
        while self.probe_queue:
            action = self.probe_queue.popleft()
            if action in self.actions:
                self._last_action_was_probe = True
                return action
        self._last_action_was_probe = False
        return None

    def recalibrate(self, first_action: Optional[int] = None) -> None:
        probes = list(self.probe_template[:3])
        if first_action is not None and first_action in probes:
            probes.remove(first_action)
        self.probe_queue = deque(probes)


class WorldDriftAgent(AdaptiveAgent):
    name = "world_drift_only"

    def reset(self, cfg: ExperimentConfig) -> None:
        super().reset(cfg)
        self.wind_samples: Deque[float] = deque(maxlen=cfg.estimate_window)

    @property
    def wind_hat(self) -> float:
        if not self.wind_samples:
            return 0.0
        return statistics.fmean(self.wind_samples)

    def act(self, position: float, target: float, t: int) -> int:
        probe = self.next_probe()
        if probe is not None:
            self._last_predicted_delta = probe + self.wind_hat
            return probe
        action = choose_best_action(
            self.actions,
            position,
            target,
            lambda a: a + self.wind_hat,
        )
        self._last_predicted_delta = action + self.wind_hat
        return action

    def observe(self, old_position: float, action: int, new_position: float, target: float, t: int) -> None:
        delta = new_position - old_position
        prediction_error = abs(delta - self._last_predicted_delta)
        if prediction_error > self.cfg.error_threshold and not self._last_action_was_probe:
            self.wind_samples.clear()
            self.recalibrate(first_action=action)
        self.wind_samples.append(delta - action)

    def estimates(self) -> Tuple[Optional[float], Optional[float]]:
        return 1.0, self.wind_hat


class ActionTableAgent(AdaptiveAgent):
    name = "history_action_table"

    def reset(self, cfg: ExperimentConfig) -> None:
        super().reset(cfg)
        self.effects: Dict[int, Deque[float]] = {}

    def predicted_effect(self, action: int) -> Optional[float]:
        samples = self.effects.get(action)
        if not samples:
            return None
        return statistics.fmean(samples)

    def act(self, position: float, target: float, t: int) -> int:
        probe = self.next_probe()
        if probe is not None:
            self._last_predicted_delta = self.predicted_effect(probe)
            if self._last_predicted_delta is None:
                self._last_predicted_delta = float(probe)
            return probe

        known_actions = [a for a in self.actions if self.predicted_effect(a) is not None]
        if not known_actions:
            action = int(round(clamp(target - position, -self.cfg.max_action, self.cfg.max_action)))
            self._last_predicted_delta = float(action)
            return action

        action = choose_best_action(
            known_actions,
            position,
            target,
            lambda a: self.predicted_effect(a) or 0.0,
        )
        self._last_predicted_delta = self.predicted_effect(action) or 0.0
        return action

    def observe(self, old_position: float, action: int, new_position: float, target: float, t: int) -> None:
        delta = new_position - old_position
        prediction_error = abs(delta - self._last_predicted_delta)
        if (
            prediction_error > self.cfg.error_threshold
            and action in self.effects
            and not self._last_action_was_probe
        ):
            self.effects.clear()
            self.recalibrate(first_action=action)
        self.effects.setdefault(action, deque(maxlen=self.cfg.estimate_window)).append(delta)


class FactorizedSelfWorldAgent(AdaptiveAgent):
    name = "factorized_self_world"

    def reset(self, cfg: ExperimentConfig) -> None:
        super().reset(cfg)
        self.samples: Deque[Tuple[int, float]] = deque(maxlen=cfg.estimate_window)
        self._gain_hat = 1.0
        self._wind_hat = 0.0

    def fit(self) -> None:
        if not self.samples:
            self._gain_hat = 1.0
            self._wind_hat = 0.0
            return

        xs = [float(a) for a, _delta in self.samples]
        ys = [float(delta) for _a, delta in self.samples]
        n = len(xs)
        mean_y = statistics.fmean(ys)

        if len(set(xs)) < 2:
            self._gain_hat = 1.0
            self._wind_hat = mean_y - self._gain_hat * statistics.fmean(xs)
            return

        sum_x = sum(xs)
        sum_y = sum(ys)
        sum_xx = sum(x * x for x in xs)
        sum_xy = sum(x * y for x, y in zip(xs, ys))
        denominator = n * sum_xx - sum_x * sum_x
        if abs(denominator) < 1e-9:
            self._gain_hat = 1.0
            self._wind_hat = mean_y - self._gain_hat * statistics.fmean(xs)
            return

        self._gain_hat = (n * sum_xy - sum_x * sum_y) / denominator
        self._wind_hat = (sum_y - self._gain_hat * sum_x) / n

    def predicted_delta(self, action: int) -> float:
        return self._gain_hat * action + self._wind_hat

    def act(self, position: float, target: float, t: int) -> int:
        probe = self.next_probe()
        if probe is not None:
            self._last_predicted_delta = self.predicted_delta(probe)
            return probe
        action = choose_best_action(
            self.actions,
            position,
            target,
            self.predicted_delta,
        )
        self._last_predicted_delta = self.predicted_delta(action)
        return action

    def observe(self, old_position: float, action: int, new_position: float, target: float, t: int) -> None:
        delta = new_position - old_position
        prediction_error = abs(delta - self._last_predicted_delta)
        if prediction_error > self.cfg.error_threshold and self.samples and not self._last_action_was_probe:
            self.samples.clear()
            self.recalibrate(first_action=action)
        self.samples.append((action, delta))
        self.fit()

    def estimates(self) -> Tuple[Optional[float], Optional[float]]:
        return self._gain_hat, self._wind_hat


class SelfAblatedFactorizedAgent(FactorizedSelfWorldAgent):
    name = "self_state_ablation"

    def predicted_delta(self, action: int) -> float:
        return action + self._wind_hat


class OracleAgent(BaseAgent):
    name = "oracle_hidden_state"

    def set_world(self, world: DriftWorld) -> None:
        self.world = world

    def act(self, position: float, target: float, t: int) -> int:
        action = choose_best_action(
            self.actions,
            position,
            target,
            lambda a: self.world.gain * a + self.world.wind,
        )
        self._last_predicted_delta = self.world.gain * action + self.world.wind
        return action

    def estimates(self) -> Tuple[Optional[float], Optional[float]]:
        return self.world.gain, self.world.wind


def choose_different(rng: random.Random, choices: Sequence[float], current: float) -> float:
    options = [choice for choice in choices if choice != current]
    return rng.choice(options)


def clamp(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def choose_best_action(
    actions: Iterable[int],
    position: float,
    target: float,
    predict_delta,
) -> int:
    return min(
        actions,
        key=lambda action: (
            abs(target - (position + predict_delta(action))),
            abs(action),
            action,
        ),
    )


def run_episode(agent: BaseAgent, scenario: str, cfg: ExperimentConfig, rng: random.Random) -> EpisodeResult:
    world = DriftWorld(scenario, rng)
    agent.reset(cfg)
    if isinstance(agent, OracleAgent):
        agent.set_world(world)

    initial_target = rng.choice([-cfg.target_abs, cfg.target_abs])
    records: List[StepRecord] = []
    total_loss = 0.0

    for t in range(cfg.horizon):
        if t == cfg.perturb_step:
            world.perturb()
            if isinstance(agent, OracleAgent):
                agent.set_world(world)

        target = initial_target if t < cfg.perturb_step else -initial_target
        old_position = world.position
        action = agent.act(world.position, target, t)
        new_position, _delta = world.step(action)
        agent.observe(old_position, action, new_position, target, t)
        gain_hat, wind_hat = agent.estimates()
        distance = abs(target - new_position)
        total_loss += distance + cfg.action_cost * abs(action)
        records.append(
            StepRecord(
                t=t,
                target=target,
                action=action,
                position=new_position,
                distance=distance,
                gain=world.gain,
                wind=world.wind,
                gain_hat=gain_hat,
                wind_hat=wind_hat,
            )
        )

    pre_records = [record for record in records if record.t < cfg.perturb_step]
    post_records = [record for record in records if record.t >= cfg.perturb_step]
    pre_success = any(record.distance <= cfg.tolerance for record in pre_records)
    post_success_records = [record for record in post_records if record.distance <= cfg.tolerance]
    post_success = bool(post_success_records)
    post_recovery_steps = None
    if post_success_records:
        post_recovery_steps = post_success_records[0].t - cfg.perturb_step + 1

    gain_errors = [
        abs(record.gain_hat - record.gain)
        for record in records
        if record.gain_hat is not None and record.t >= cfg.perturb_step
    ]
    wind_errors = [
        abs(record.wind_hat - record.wind)
        for record in records
        if record.wind_hat is not None and record.t >= cfg.perturb_step
    ]

    return EpisodeResult(
        agent=agent.name,
        scenario=scenario,
        pre_success=pre_success,
        post_success=post_success,
        post_recovery_steps=post_recovery_steps,
        final_distance=records[-1].distance,
        mean_post_distance=statistics.fmean(record.distance for record in post_records),
        total_loss=total_loss,
        gain_mae=statistics.fmean(gain_errors) if gain_errors else None,
        wind_mae=statistics.fmean(wind_errors) if wind_errors else None,
    )


def summarize(results: Sequence[EpisodeResult]) -> List[Dict[str, object]]:
    grouped: Dict[Tuple[str, str], List[EpisodeResult]] = {}
    for result in results:
        grouped.setdefault((result.scenario, result.agent), []).append(result)

    rows: List[Dict[str, object]] = []
    for (scenario, agent), items in sorted(grouped.items()):
        successful_recoveries = [
            item.post_recovery_steps for item in items if item.post_recovery_steps is not None
        ]
        gain_maes = [item.gain_mae for item in items if item.gain_mae is not None]
        wind_maes = [item.wind_mae for item in items if item.wind_mae is not None]
        rows.append(
            {
                "scenario": scenario,
                "agent": agent,
                "episodes": len(items),
                "pre_success_rate": rate(item.pre_success for item in items),
                "post_success_rate": rate(item.post_success for item in items),
                "mean_recovery_steps_successes": mean_or_none(successful_recoveries),
                "mean_post_distance": statistics.fmean(item.mean_post_distance for item in items),
                "mean_final_distance": statistics.fmean(item.final_distance for item in items),
                "mean_total_loss": statistics.fmean(item.total_loss for item in items),
                "post_gain_mae": mean_or_none(gain_maes),
                "post_wind_mae": mean_or_none(wind_maes),
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


def print_summary(rows: Sequence[Dict[str, object]]) -> None:
    columns = [
        "scenario",
        "agent",
        "post_success_rate",
        "mean_recovery_steps_successes",
        "mean_post_distance",
        "mean_total_loss",
        "post_gain_mae",
        "post_wind_mae",
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
        if math.isnan(value):
            return ""
        return f"{value:.3f}"
    return str(value)


def write_outputs(rows: Sequence[Dict[str, object]], cfg: ExperimentConfig, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "self_world_attribution_results.json"
    csv_path = output_dir / "self_world_attribution_summary.csv"

    with json_path.open("w", encoding="utf-8") as handle:
        json.dump({"config": asdict(cfg), "summary": list(rows)}, handle, indent=2)
        handle.write("\n")

    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def stable_episode_seed(seed: int, scenario: str, episode: int) -> int:
    payload = f"{seed}:{scenario}:{episode}".encode("utf-8")
    digest = hashlib.sha256(payload).digest()
    return int.from_bytes(digest[:8], "big")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=ExperimentConfig.episodes)
    parser.add_argument("--seed", type=int, default=ExperimentConfig.seed)
    parser.add_argument("--horizon", type=int, default=ExperimentConfig.horizon)
    parser.add_argument("--perturb-step", type=int, default=ExperimentConfig.perturb_step)
    parser.add_argument("--target-abs", type=float, default=ExperimentConfig.target_abs)
    parser.add_argument("--max-action", type=int, default=ExperimentConfig.max_action)
    parser.add_argument("--output-dir", type=Path, default=Path("artifacts"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = ExperimentConfig(
        episodes=args.episodes,
        horizon=args.horizon,
        perturb_step=args.perturb_step,
        target_abs=args.target_abs,
        max_action=args.max_action,
        seed=args.seed,
    )
    scenarios = ["static_goal_switch", "world_drift", "self_drift", "mixed_hidden"]
    agent_factories = [
        ReactiveAgent,
        WorldDriftAgent,
        ActionTableAgent,
        SelfAblatedFactorizedAgent,
        FactorizedSelfWorldAgent,
        OracleAgent,
    ]

    results: List[EpisodeResult] = []
    for scenario in scenarios:
        for agent_factory in agent_factories:
            for episode in range(cfg.episodes):
                episode_seed = stable_episode_seed(cfg.seed, scenario, episode)
                rng = random.Random(episode_seed)
                results.append(run_episode(agent_factory(), scenario, cfg, rng))

    rows = summarize(results)
    write_outputs(rows, cfg, args.output_dir)
    print_summary(rows)


if __name__ == "__main__":
    main()
