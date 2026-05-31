#!/usr/bin/env python3
"""Learned sensor-subspace recurrent filter precursor.

This is a stricter companion to mixed_sensor_recurrent_filter.py. The previous
mixed-sensor test removed self-aligned input channels, but its causal ablation
still removed known latent sources before mixing. This version learns the
destructive intervention direction in sensor space from training outcomes.

Boundary interventions are still supplied only to classify the dependency as
agent-bounded or external. They are not used to choose the ablated direction.

Prediction:

- random-start recurrent search should still win when one mixed latent controls
  future action;
- ablating the learned sensor-space direction should selectively damage the
  recurrent policy in shared self/world regimes;
- boundary interventions should classify that damaged dependency as
  agent-bounded for self-hidden regimes and external for world-hidden regimes;
- local probing or no-state control should still win in independent/no-hidden
  controls.
"""

from __future__ import annotations

import argparse
import json
import math
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import mixed_sensor_recurrent_filter as mixed


ARTIFACT_DIR = Path("artifacts")
MIN_LEARNED_DIRECTION_LOSS = 30.0
MIN_BOUNDARY_EFFECT = 0.20


@dataclass(frozen=True)
class DirectionRow:
    scenario: str
    dependency_signature: str
    learned_direction_x: float
    learned_direction_y: float
    learned_direction_strength: float
    learned_direction_ablation_loss: float
    intact_recurrent_reward: float
    learned_direction_ablated_reward: float
    source_a_intervention_effect: float
    source_b_intervention_effect: float


def mean_sensor_vector(state: mixed.EpisodeState) -> Tuple[float, float]:
    return (
        statistics.fmean(sensor_1 for sensor_1, _ in state.mixed_observations),
        statistics.fmean(sensor_2 for _, sensor_2 in state.mixed_observations),
    )


def outcome_rate(state: mixed.EpisodeState) -> float:
    return sum(1 for success in state.step_success if success) / len(state.step_success)


def learn_sensor_direction(
    states: Sequence[mixed.EpisodeState],
) -> Tuple[Tuple[float, float], float]:
    """Learn an outcome-predictive direction in observed sensor space.

    The direction is a simple covariance-like contrast between episode outcome
    rates and mixed sensor means. It uses no source labels and no source
    ablations. A zero-variance outcome stream returns a zero direction.
    """

    if not states:
        return (0.0, 0.0), 0.0
    baseline = statistics.fmean(outcome_rate(state) for state in states)
    weighted_x = 0.0
    weighted_y = 0.0
    total_abs_weight = 0.0
    for state in states:
        weight = outcome_rate(state) - baseline
        sensor_x, sensor_y = mean_sensor_vector(state)
        weighted_x += weight * sensor_x
        weighted_y += weight * sensor_y
        total_abs_weight += abs(weight)
    norm = math.hypot(weighted_x, weighted_y)
    if norm < 1e-12 or total_abs_weight < 1e-12:
        return (0.0, 0.0), 0.0
    return (weighted_x / norm, weighted_y / norm), norm / total_abs_weight


def remove_projection(
    observation: Tuple[float, float],
    direction: Tuple[float, float],
) -> Tuple[float, float]:
    dot = observation[0] * direction[0] + observation[1] * direction[1]
    return observation[0] - dot * direction[0], observation[1] - dot * direction[1]


def ablate_learned_direction(
    observations: Sequence[Tuple[float, float]],
    direction: Tuple[float, float],
) -> Tuple[Tuple[float, float], ...]:
    if math.hypot(direction[0], direction[1]) < 1e-12:
        return tuple(observations)
    return tuple(remove_projection(observation, direction) for observation in observations)


def evaluate_recurrent_with_learned_ablation(
    state: mixed.EpisodeState,
    candidate: mixed.Candidate,
    cfg: mixed.MixedSensorConfig,
    direction: Tuple[float, float],
) -> Tuple[float, int, int, int, int, int, int]:
    observations = ablate_learned_direction(state.mixed_observations, direction)
    logit = mixed.recurrent_logit(candidate, observations)
    choice = "risky" if logit >= 0.0 else "safe"
    total_reward = -cfg.shared_cue_cost
    risky_count = 0
    safe_count = 0
    failed_count = 0
    successes = 0
    for hidden_success in state.step_success:
        reward, success = mixed.action_reward(choice, hidden_success)
        total_reward += reward
        if choice == "risky":
            risky_count += 1
            if not success:
                failed_count += 1
        else:
            safe_count += 1
        if success:
            successes += 1
    return total_reward, cfg.evidence_samples, 0, risky_count, safe_count, failed_count, successes


def dependency_signature(
    scenario: mixed.MixedScenario,
    candidate: mixed.Candidate,
    training_states: Sequence[mixed.EpisodeState],
    cfg: mixed.MixedSensorConfig,
) -> DirectionRow:
    direction, strength = learn_sensor_direction(training_states)
    states = mixed.make_states(scenario, "dependency", cfg.episodes, cfg)
    intact = statistics.fmean(
        mixed.evaluate_recurrent(state, candidate, cfg, "none")[0]
        for state in states
    )
    ablated = statistics.fmean(
        evaluate_recurrent_with_learned_ablation(state, candidate, cfg, direction)[0]
        for state in states
    )
    loss = intact - ablated
    effect_a, effect_b = mixed.intervention_effects(scenario, states)
    if loss > MIN_LEARNED_DIRECTION_LOSS and effect_a > MIN_BOUNDARY_EFFECT and effect_a > effect_b:
        signature = "agent_bounded_learned_subspace"
    elif loss > MIN_LEARNED_DIRECTION_LOSS and effect_b > MIN_BOUNDARY_EFFECT and effect_b > effect_a:
        signature = "external_learned_subspace"
    else:
        signature = "no_learned_subspace_boundary"
    return DirectionRow(
        scenario=scenario.name,
        dependency_signature=signature,
        learned_direction_x=direction[0],
        learned_direction_y=direction[1],
        learned_direction_strength=strength,
        learned_direction_ablation_loss=loss,
        intact_recurrent_reward=intact,
        learned_direction_ablated_reward=ablated,
        source_a_intervention_effect=effect_a,
        source_b_intervention_effect=effect_b,
    )


def run_agent(
    scenario: mixed.MixedScenario,
    state: mixed.EpisodeState,
    agent: str,
    selected_policy: str,
    candidate: mixed.Candidate,
    signature: str,
    cfg: mixed.MixedSensorConfig,
) -> mixed.AgentResult:
    return mixed.run_agent(scenario, state, agent, selected_policy, candidate, signature, cfg)


def reward_for(summary_rows: Sequence[Dict[str, object]], scenario: str, agent: str) -> float:
    return mixed.reward_for(summary_rows, scenario, agent)


def verdict_rows(
    summary_rows: Sequence[Dict[str, object]],
    training_rows: Sequence[mixed.TrainingRow],
    direction_rows: Sequence[DirectionRow],
) -> List[Dict[str, object]]:
    rows = []
    for scenario in sorted({str(row["scenario"]) for row in summary_rows}):
        training = next(row for row in training_rows if row.scenario == scenario)
        direction = next(row for row in direction_rows if row.scenario == scenario)
        recurrent_reward = reward_for(summary_rows, scenario, "recurrent_controller")
        local_reward = reward_for(summary_rows, scenario, "task_local_probe")
        greedy_reward = reward_for(summary_rows, scenario, "greedy_no_state")
        selector_reward = reward_for(summary_rows, scenario, "learned_structure_selector")
        rows.append(
            {
                "scenario": scenario,
                "selected_policy": training.selected_policy,
                "selected_architecture": training.selected_architecture,
                "dependency_signature": direction.dependency_signature,
                "recurrent_reward": recurrent_reward,
                "local_probe_reward": local_reward,
                "greedy_reward": greedy_reward,
                "selector_reward": selector_reward,
                "learned_direction_ablation_loss": direction.learned_direction_ablation_loss,
                "learned_direction_strength": direction.learned_direction_strength,
                "supports_learned_subspace_prediction": scenario_supports_prediction(
                    scenario,
                    training.selected_policy,
                    direction.dependency_signature,
                    recurrent_reward,
                    local_reward,
                    greedy_reward,
                    direction.learned_direction_ablation_loss,
                ),
            }
        )
    return rows


def scenario_supports_prediction(
    scenario: str,
    selected_policy: str,
    signature: str,
    recurrent_reward: float,
    local_reward: float,
    greedy_reward: float,
    learned_loss: float,
) -> bool:
    if scenario == "self_mixed_hidden":
        return (
            selected_policy == "recurrent_controller"
            and signature == "agent_bounded_learned_subspace"
            and recurrent_reward > local_reward
            and learned_loss > MIN_LEARNED_DIRECTION_LOSS
        )
    if scenario == "world_mixed_hidden":
        return (
            selected_policy == "recurrent_controller"
            and signature == "external_learned_subspace"
            and recurrent_reward > local_reward
            and learned_loss > MIN_LEARNED_DIRECTION_LOSS
        )
    if scenario == "independent_hidden":
        return (
            selected_policy == "task_local_probe"
            and signature == "no_learned_subspace_boundary"
            and local_reward > recurrent_reward + 40.0
        )
    if scenario == "irrelevant_control":
        return (
            selected_policy == "greedy_no_state"
            and signature == "no_learned_subspace_boundary"
            and greedy_reward > recurrent_reward
        )
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: mixed.MixedSensorConfig,
) -> Tuple[
    List[mixed.AgentResult],
    List[Dict[str, object]],
    List[mixed.TrainingRow],
    List[DirectionRow],
    List[Dict[str, object]],
]:
    results = []
    training_rows = []
    direction_rows = []
    for scenario in mixed.SCENARIOS:
        training_states = mixed.make_states(scenario, "train", cfg.training_episodes, cfg)
        candidate = mixed.train_recurrent(scenario, training_states, cfg)
        selected_policy, rewards = mixed.select_policy(candidate, training_states, cfg)
        direction = dependency_signature(scenario, candidate, training_states, cfg)
        training_rows.append(
            mixed.TrainingRow(
                scenario=scenario.name,
                selected_policy=selected_policy,
                selected_architecture=candidate.architecture,
                recurrent_training_reward=rewards["recurrent_controller"],
                local_training_reward=rewards["task_local_probe"],
                greedy_training_reward=rewards["greedy_no_state"],
                safe_training_reward=rewards["safe_no_state"],
                selected_weights=mixed.format_weights(candidate.weights),
            )
        )
        direction_rows.append(direction)
        test_states = mixed.make_states(scenario, "test", cfg.episodes, cfg)
        for state in test_states:
            for agent in mixed.AGENTS:
                results.append(
                    run_agent(
                        scenario,
                        state,
                        agent,
                        selected_policy,
                        candidate,
                        direction.dependency_signature,
                        cfg,
                    )
                )
    summary_rows = mixed.summarize(results)
    verdicts = verdict_rows(summary_rows, training_rows, direction_rows)
    return results, summary_rows, training_rows, direction_rows, verdicts


def write_csv(path: Path, rows: Iterable[object]) -> None:
    mixed.write_csv(path, rows)


def print_table(verdicts: Sequence[Dict[str, object]]) -> None:
    headers = [
        "scenario",
        "selected_policy",
        "dependency_signature",
        "recurrent_reward",
        "local_probe_reward",
        "learned_direction_ablation_loss",
        "supports_learned_subspace_prediction",
    ]
    rows = []
    for verdict in verdicts:
        rows.append(
            [
                str(verdict["scenario"]),
                str(verdict["selected_policy"]),
                str(verdict["dependency_signature"]),
                f"{float(verdict['recurrent_reward']):.3f}",
                f"{float(verdict['local_probe_reward']):.3f}",
                f"{float(verdict['learned_direction_ablation_loss']):.3f}",
                str(verdict["supports_learned_subspace_prediction"]),
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


def parse_args() -> mixed.MixedSensorConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=500)
    parser.add_argument("--training-episodes", type=int, default=800)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--horizon", type=int, default=8)
    parser.add_argument("--evidence-samples", type=int, default=9)
    parser.add_argument("--cue-accuracy", type=float, default=0.85)
    parser.add_argument("--shared-cue-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    parser.add_argument("--random-candidates", type=int, default=1800)
    args = parser.parse_args()
    if args.episodes < 1:
        raise SystemExit("--episodes must be at least 1")
    if args.training_episodes < 1:
        raise SystemExit("--training-episodes must be at least 1")
    if args.horizon < 1:
        raise SystemExit("--horizon must be at least 1")
    if args.evidence_samples < 1:
        raise SystemExit("--evidence-samples must be at least 1")
    if not 0.5 <= args.cue_accuracy <= 1.0:
        raise SystemExit("--cue-accuracy must be in [0.5, 1.0]")
    if args.random_candidates < 1:
        raise SystemExit("--random-candidates must be positive")
    return mixed.MixedSensorConfig(
        episodes=args.episodes,
        training_episodes=args.training_episodes,
        seed=args.seed,
        horizon=args.horizon,
        evidence_samples=args.evidence_samples,
        cue_accuracy=args.cue_accuracy,
        shared_cue_cost=args.shared_cue_cost,
        local_probe_cost=args.local_probe_cost,
        random_candidates=args.random_candidates,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    results, summary_rows, training_rows, direction_rows, verdicts = run_experiment(cfg)
    summary_path = ARTIFACT_DIR / "learned_sensor_subspace_filter_summary.csv"
    training_path = ARTIFACT_DIR / "learned_sensor_subspace_filter_training.csv"
    direction_path = ARTIFACT_DIR / "learned_sensor_subspace_filter_dependency.csv"
    verdict_path = ARTIFACT_DIR / "learned_sensor_subspace_filter_verdict.csv"
    results_path = ARTIFACT_DIR / "learned_sensor_subspace_filter_results.json"
    write_csv(summary_path, summary_rows)
    write_csv(training_path, training_rows)
    write_csv(direction_path, direction_rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "training": [asdict(row) for row in training_rows],
                "dependency": [asdict(row) for row in direction_rows],
                "summary": summary_rows,
                "verdict": verdicts,
                "episode_results": [asdict(row) for row in results],
            },
            handle,
            indent=2,
        )
        handle.write("\n")
    print(f"wrote {summary_path}")
    print(f"wrote {training_path}")
    print(f"wrote {direction_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print_table(verdicts)
    return 0 if all(bool(row["supports_learned_subspace_prediction"]) for row in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
