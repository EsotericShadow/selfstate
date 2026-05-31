#!/usr/bin/env python3
"""Partial-observability sweep for self-state advantage.

This experiment varies the reliability of noisy evidence about hidden state.

Prediction:

- shared self-belief should become valuable when noisy evidence reveals a
  persistent agent-state that controls future action;
- shared world-belief should show the same curve for external variables, which
  should not count as selfhood;
- task-local probing should win when future steps have independent hidden
  states;
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
PRIOR_TRUE = 0.55
RISKY_SUCCESS_REWARD = 24.0
RISKY_FAILURE_REWARD = -16.0
SAFE_REWARD = 8.0
EPS = 1e-12


@dataclass(frozen=True)
class ObservabilityConfig:
    episodes: int = 500
    seed: int = 20260602
    horizon: int = 6
    evidence_samples: int = 3
    cue_cost: float = 1.0
    min_accuracy: float = 0.50
    max_accuracy: float = 0.95
    accuracy_step: float = 0.05


@dataclass(frozen=True)
class ObservabilityScenario:
    name: str
    mode: str


@dataclass(frozen=True)
class ObservabilityState:
    scenario: str
    accuracy: float
    self_signal: bool
    world_signal: bool
    self_cues: Tuple[bool, ...]
    world_cues: Tuple[bool, ...]
    step_success: Tuple[bool, ...]


@dataclass
class EpisodeResult:
    scenario: str
    accuracy: float
    agent: str
    total_reward: float
    cue_count: int
    risky_count: int
    safe_count: int
    failed_risky_count: int
    success_rate: float


SCENARIOS = [
    ObservabilityScenario("self_hidden", "self_hidden"),
    ObservabilityScenario("world_hidden", "world_hidden"),
    ObservabilityScenario("independent_hidden", "independent_hidden"),
    ObservabilityScenario("irrelevant_control", "irrelevant_control"),
]


class BaseAgent:
    name = "base"

    def reset(self, scenario: ObservabilityScenario) -> None:
        self.scenario = scenario
        self.risk_probability = PRIOR_TRUE

    def prepare(self, state: ObservabilityState, cfg: ObservabilityConfig) -> float:
        return 0.0

    def choose(self, step: int, state: ObservabilityState, cfg: ObservabilityConfig) -> Tuple[str, float]:
        raise NotImplementedError


class GreedyNoStateAgent(BaseAgent):
    name = "greedy_no_state"

    def choose(self, step: int, state: ObservabilityState, cfg: ObservabilityConfig) -> Tuple[str, float]:
        return "risky", 0.0


class SafeNoStateAgent(BaseAgent):
    name = "safe_no_state"

    def choose(self, step: int, state: ObservabilityState, cfg: ObservabilityConfig) -> Tuple[str, float]:
        return "safe", 0.0


class SharedSelfBeliefAgent(BaseAgent):
    name = "shared_self_belief"

    def prepare(self, state: ObservabilityState, cfg: ObservabilityConfig) -> float:
        self.risk_probability = posterior_probability(state.self_cues, state.accuracy)
        return -cfg.cue_cost

    def choose(self, step: int, state: ObservabilityState, cfg: ObservabilityConfig) -> Tuple[str, float]:
        return ("risky" if should_risk(self.risk_probability) else "safe"), 0.0


class SharedWorldBeliefAgent(BaseAgent):
    name = "shared_world_belief"

    def prepare(self, state: ObservabilityState, cfg: ObservabilityConfig) -> float:
        self.risk_probability = posterior_probability(state.world_cues, state.accuracy)
        return -cfg.cue_cost

    def choose(self, step: int, state: ObservabilityState, cfg: ObservabilityConfig) -> Tuple[str, float]:
        return ("risky" if should_risk(self.risk_probability) else "safe"), 0.0


class StepLocalProbeAgent(BaseAgent):
    name = "step_local_probe"

    def choose(self, step: int, state: ObservabilityState, cfg: ObservabilityConfig) -> Tuple[str, float]:
        return ("risky" if state.step_success[step] else "safe"), -cfg.cue_cost


class OracleObservationAgent(BaseAgent):
    name = "oracle_observation"

    def choose(self, step: int, state: ObservabilityState, cfg: ObservabilityConfig) -> Tuple[str, float]:
        return ("risky" if state.step_success[step] else "safe"), 0.0


AGENT_FACTORIES = [
    GreedyNoStateAgent,
    SafeNoStateAgent,
    SharedSelfBeliefAgent,
    SharedWorldBeliefAgent,
    StepLocalProbeAgent,
    OracleObservationAgent,
]


def accuracy_values(cfg: ObservabilityConfig) -> List[float]:
    values = []
    current = cfg.min_accuracy
    while current <= cfg.max_accuracy + EPS:
        values.append(round(current, 2))
        current += cfg.accuracy_step
    return values


def stable_state_seed(seed: int, scenario: str, accuracy: float, episode: int) -> int:
    value = seed + episode * 1009 + int(round(accuracy * 100.0)) * 9176
    for char in scenario:
        value = (value * 131 + ord(char)) % (2**32)
    return value


def sample_state(
    scenario: ObservabilityScenario,
    accuracy: float,
    episode: int,
    cfg: ObservabilityConfig,
) -> ObservabilityState:
    rng = random.Random(stable_state_seed(cfg.seed, scenario.name, accuracy, episode))
    self_signal = rng.random() < PRIOR_TRUE
    world_signal = rng.random() < PRIOR_TRUE
    if scenario.mode == "self_hidden":
        step_success = tuple(self_signal for _ in range(cfg.horizon))
    elif scenario.mode == "world_hidden":
        step_success = tuple(world_signal for _ in range(cfg.horizon))
    elif scenario.mode == "independent_hidden":
        step_success = tuple(rng.random() < PRIOR_TRUE for _ in range(cfg.horizon))
    elif scenario.mode == "irrelevant_control":
        step_success = tuple(True for _ in range(cfg.horizon))
    else:
        raise ValueError(f"unknown scenario mode: {scenario.mode}")
    return ObservabilityState(
        scenario=scenario.name,
        accuracy=accuracy,
        self_signal=self_signal,
        world_signal=world_signal,
        self_cues=tuple(noisy_cue(self_signal, accuracy, rng) for _ in range(cfg.evidence_samples)),
        world_cues=tuple(noisy_cue(world_signal, accuracy, rng) for _ in range(cfg.evidence_samples)),
        step_success=step_success,
    )


def noisy_cue(value: bool, accuracy: float, rng: random.Random) -> bool:
    return value if rng.random() < accuracy else not value


def posterior_probability(cues: Tuple[bool, ...], accuracy: float) -> float:
    if abs(accuracy - 0.5) <= EPS:
        return PRIOR_TRUE
    positives = sum(1 for cue in cues if cue)
    negatives = len(cues) - positives
    true_likelihood = (accuracy**positives) * ((1.0 - accuracy) ** negatives)
    false_likelihood = ((1.0 - accuracy) ** positives) * (accuracy**negatives)
    numerator = PRIOR_TRUE * true_likelihood
    denominator = numerator + (1.0 - PRIOR_TRUE) * false_likelihood
    return numerator / denominator


def should_risk(success_probability: float) -> bool:
    threshold = (SAFE_REWARD - RISKY_FAILURE_REWARD) / (RISKY_SUCCESS_REWARD - RISKY_FAILURE_REWARD)
    return success_probability >= threshold


def run_episode(
    agent_factory,
    scenario: ObservabilityScenario,
    accuracy: float,
    episode: int,
    cfg: ObservabilityConfig,
) -> EpisodeResult:
    state = sample_state(scenario, accuracy, episode, cfg)
    agent = agent_factory()
    agent.reset(scenario)
    total_reward = agent.prepare(state, cfg)
    cue_count = cfg.evidence_samples if agent.name in {"shared_self_belief", "shared_world_belief"} else 0
    risky_count = 0
    safe_count = 0
    failed_risky_count = 0
    successes = 0

    for step in range(cfg.horizon):
        choice, cost = agent.choose(step, state, cfg)
        total_reward += cost
        if cost < 0.0:
            cue_count += 1
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
        accuracy=accuracy,
        agent=agent.name,
        total_reward=total_reward,
        cue_count=cue_count,
        risky_count=risky_count,
        safe_count=safe_count,
        failed_risky_count=failed_risky_count,
        success_rate=successes / cfg.horizon,
    )


def action_reward(choice: str, hidden_success: bool) -> Tuple[float, bool]:
    if choice == "safe":
        return SAFE_REWARD, True
    if hidden_success:
        return RISKY_SUCCESS_REWARD, True
    return RISKY_FAILURE_REWARD, False


def summarize(results: Sequence[EpisodeResult]) -> List[Dict[str, object]]:
    grouped: Dict[Tuple[str, float, str], List[EpisodeResult]] = {}
    for result in results:
        grouped.setdefault((result.scenario, result.accuracy, result.agent), []).append(result)
    rows = []
    for (scenario, accuracy, agent), items in sorted(grouped.items()):
        rows.append(
            {
                "scenario": scenario,
                "accuracy": accuracy,
                "agent": agent,
                "episodes": len(items),
                "mean_total_reward": statistics.fmean(item.total_reward for item in items),
                "mean_cue_count": statistics.fmean(item.cue_count for item in items),
                "mean_risky_count": statistics.fmean(item.risky_count for item in items),
                "mean_safe_count": statistics.fmean(item.safe_count for item in items),
                "mean_failed_risky_count": statistics.fmean(item.failed_risky_count for item in items),
                "mean_success_rate": statistics.fmean(item.success_rate for item in items),
            }
        )
    return rows


def verdict_rows(summary_rows: Sequence[Dict[str, object]], cfg: ObservabilityConfig) -> List[Dict[str, object]]:
    rows = []
    accuracies = accuracy_values(cfg)
    first_accuracy = accuracies[0]
    last_accuracy = accuracies[-1]
    for scenario in sorted({str(row["scenario"]) for row in summary_rows}):
        first = pressure_point(summary_rows, scenario, first_accuracy)
        last = pressure_point(summary_rows, scenario, last_accuracy)
        rows.append(
            {
                "scenario": scenario,
                "accuracy_range": f"{first_accuracy:.2f}-{last_accuracy:.2f}",
                "best_at_max_accuracy": last["best_non_oracle_agent"],
                "shared_self_minus_safe_at_min": first["shared_self_minus_safe"],
                "shared_self_minus_safe_at_max": last["shared_self_minus_safe"],
                "shared_world_minus_safe_at_max": last["shared_world_minus_safe"],
                "shared_self_minus_local_at_max": last["shared_self_minus_local"],
                "local_minus_shared_self_at_max": -last["shared_self_minus_local"],
                "greedy_minus_shared_self_at_max": last["greedy_minus_shared_self"],
                "supports_observability_prediction": scenario_supports_observability(scenario, first, last),
            }
        )
    return rows


def pressure_point(summary_rows: Sequence[Dict[str, object]], scenario: str, accuracy: float) -> Dict[str, object]:
    rows = [
        row
        for row in summary_rows
        if row["scenario"] == scenario and abs(float(row["accuracy"]) - accuracy) <= EPS
    ]
    non_oracle = [row for row in rows if row["agent"] != "oracle_observation"]
    best = sorted(non_oracle, key=lambda row: (-float(row["mean_total_reward"]), str(row["agent"])))[0]
    greedy = row_for(rows, "greedy_no_state")
    safe = row_for(rows, "safe_no_state")
    self_belief = row_for(rows, "shared_self_belief")
    world_belief = row_for(rows, "shared_world_belief")
    local = row_for(rows, "step_local_probe")
    return {
        "scenario": scenario,
        "accuracy": accuracy,
        "best_non_oracle_agent": best["agent"],
        "greedy_reward": greedy["mean_total_reward"],
        "safe_reward": safe["mean_total_reward"],
        "shared_self_reward": self_belief["mean_total_reward"],
        "shared_world_reward": world_belief["mean_total_reward"],
        "local_reward": local["mean_total_reward"],
        "shared_self_minus_safe": float(self_belief["mean_total_reward"]) - float(safe["mean_total_reward"]),
        "shared_world_minus_safe": float(world_belief["mean_total_reward"]) - float(safe["mean_total_reward"]),
        "shared_self_minus_local": float(self_belief["mean_total_reward"]) - float(local["mean_total_reward"]),
        "shared_world_minus_local": float(world_belief["mean_total_reward"]) - float(local["mean_total_reward"]),
        "greedy_minus_shared_self": float(greedy["mean_total_reward"]) - float(self_belief["mean_total_reward"]),
    }


def row_for(rows: Sequence[Dict[str, object]], agent: str) -> Dict[str, object]:
    return next(row for row in rows if row["agent"] == agent)


def scenario_supports_observability(
    scenario: str,
    first: Dict[str, object],
    last: Dict[str, object],
) -> bool:
    if scenario == "self_hidden":
        return (
            last["best_non_oracle_agent"] == "shared_self_belief"
            and float(last["shared_self_minus_safe"]) > float(first["shared_self_minus_safe"]) + 40.0
            and float(last["shared_self_reward"]) > float(last["shared_world_reward"]) + 40.0
            and float(last["shared_self_minus_local"]) > 0.0
        )
    if scenario == "world_hidden":
        return (
            last["best_non_oracle_agent"] == "shared_world_belief"
            and float(last["shared_world_minus_safe"]) > float(first["shared_world_minus_safe"]) + 40.0
            and float(last["shared_world_reward"]) > float(last["shared_self_reward"]) + 40.0
        )
    if scenario == "independent_hidden":
        return (
            last["best_non_oracle_agent"] == "step_local_probe"
            and -float(last["shared_self_minus_local"]) > 20.0
            and -float(last["shared_world_minus_local"]) > 20.0
        )
    if scenario == "irrelevant_control":
        return (
            last["best_non_oracle_agent"] == "greedy_no_state"
            and float(last["greedy_minus_shared_self"]) >= 1.0
            and float(last["greedy_reward"]) > float(last["local_reward"]) + 1.0
        )
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: ObservabilityConfig,
) -> Tuple[List[EpisodeResult], List[Dict[str, object]], List[Dict[str, object]]]:
    results = []
    for scenario in SCENARIOS:
        for accuracy in accuracy_values(cfg):
            for episode in range(cfg.episodes):
                for agent_factory in AGENT_FACTORIES:
                    results.append(run_episode(agent_factory, scenario, accuracy, episode, cfg))
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
        "best_at_max_accuracy",
        "shared_self_minus_safe_at_min",
        "shared_self_minus_safe_at_max",
        "shared_world_minus_safe_at_max",
        "supports_observability_prediction",
    ]
    rows = []
    for verdict in verdicts:
        rows.append(
            [
                str(verdict["scenario"]),
                str(verdict["best_at_max_accuracy"]),
                f"{float(verdict['shared_self_minus_safe_at_min']):.3f}",
                f"{float(verdict['shared_self_minus_safe_at_max']):.3f}",
                f"{float(verdict['shared_world_minus_safe_at_max']):.3f}",
                str(verdict["supports_observability_prediction"]),
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


def parse_args() -> ObservabilityConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=500)
    parser.add_argument("--seed", type=int, default=20260602)
    parser.add_argument("--horizon", type=int, default=6)
    parser.add_argument("--evidence-samples", type=int, default=3)
    parser.add_argument("--cue-cost", type=float, default=1.0)
    parser.add_argument("--min-accuracy", type=float, default=0.50)
    parser.add_argument("--max-accuracy", type=float, default=0.95)
    parser.add_argument("--accuracy-step", type=float, default=0.05)
    args = parser.parse_args()
    if args.horizon < 1:
        raise SystemExit("--horizon must be at least 1")
    if args.evidence_samples < 1:
        raise SystemExit("--evidence-samples must be at least 1")
    if not 0.5 <= args.min_accuracy <= args.max_accuracy <= 1.0:
        raise SystemExit("--min-accuracy and --max-accuracy must be in [0.5, 1.0]")
    if args.accuracy_step <= 0.0:
        raise SystemExit("--accuracy-step must be positive")
    return ObservabilityConfig(
        episodes=args.episodes,
        seed=args.seed,
        horizon=args.horizon,
        evidence_samples=args.evidence_samples,
        cue_cost=args.cue_cost,
        min_accuracy=args.min_accuracy,
        max_accuracy=args.max_accuracy,
        accuracy_step=args.accuracy_step,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    results, summary_rows, verdicts = run_experiment(cfg)
    summary_path = ARTIFACT_DIR / "partial_observability_sweep_summary.csv"
    verdict_path = ARTIFACT_DIR / "partial_observability_sweep_verdict.csv"
    results_path = ARTIFACT_DIR / "partial_observability_sweep_results.json"
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
    return 0 if all(bool(row["supports_observability_prediction"]) for row in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
