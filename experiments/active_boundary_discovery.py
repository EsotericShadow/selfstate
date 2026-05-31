#!/usr/bin/env python3
"""Active boundary-discovery precursor.

This is a stricter companion to learned_sensor_subspace_filter.py. The previous
test learned the destructive intervention direction in mixed sensor space, but
then used supplied boundary interventions to decide whether that dependency was
agent-bounded or external.

This version learns an owned-action direction in the same mixed sensor space.
It classifies a dependency as self-equivalent only when the outcome-predictive
subspace is also the subspace moved by the agent's own diagnostic action.

Prediction:

- shared recurrent control should still win when a persistent mixed latent
  controls future action;
- ablating the outcome-predictive sensor direction should damage recurrent
  control in shared self/world regimes;
- the self-hidden regime should align that outcome direction with the
  owned-action direction;
- the world-hidden regime should show useful recurrent dependence with weak
  owned-action alignment;
- independent and irrelevant controls should reject a shared active boundary.
"""

from __future__ import annotations

import argparse
import json
import math
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import learned_sensor_subspace_filter as subspace
import mixed_sensor_recurrent_filter as mixed


ARTIFACT_DIR = Path("artifacts")
MIN_OUTCOME_DIRECTION_LOSS = 30.0
MIN_OWNED_ALIGNMENT = 0.70
MAX_EXTERNAL_ALIGNMENT = 0.35
MIN_OWNED_DIRECTION_STRENGTH = 0.10


@dataclass(frozen=True)
class ActiveBoundaryRow:
    scenario: str
    dependency_signature: str
    outcome_direction_x: float
    outcome_direction_y: float
    outcome_direction_strength: float
    owned_action_direction_x: float
    owned_action_direction_y: float
    owned_action_direction_strength: float
    owned_action_alignment: float
    outcome_direction_ablation_loss: float
    intact_recurrent_reward: float
    outcome_direction_ablated_reward: float


def mean_vector(vectors: Sequence[Tuple[float, float]]) -> Tuple[float, float]:
    if not vectors:
        return 0.0, 0.0
    return (
        statistics.fmean(vector[0] for vector in vectors),
        statistics.fmean(vector[1] for vector in vectors),
    )


def normalize(vector: Tuple[float, float]) -> Tuple[Tuple[float, float], float]:
    norm = math.hypot(vector[0], vector[1])
    if norm < 1e-12:
        return (0.0, 0.0), 0.0
    return (vector[0] / norm, vector[1] / norm), norm


def owned_action_delta(state: mixed.EpisodeState) -> Tuple[float, float]:
    """Return the observed sensor delta caused by the agent's own action.

    The learner only consumes the pre/post mixed-sensor delta. The simulator
    creates that post-action observation by applying an owned diagnostic action
    to the source that represents agent-state evidence in this toy family.
    """

    deltas = []
    for source_a, source_b in state.source_observations:
        before = mixed.mix_sources(source_a, source_b)
        after = mixed.mix_sources(1.0, source_b)
        deltas.append((after[0] - before[0], after[1] - before[1]))
    return mean_vector(deltas)


def learn_owned_action_direction(
    states: Sequence[mixed.EpisodeState],
) -> Tuple[Tuple[float, float], float]:
    direction, strength = normalize(mean_vector([owned_action_delta(state) for state in states]))
    return direction, strength


def direction_alignment(
    first: Tuple[float, float],
    second: Tuple[float, float],
) -> float:
    if math.hypot(first[0], first[1]) < 1e-12 or math.hypot(second[0], second[1]) < 1e-12:
        return 0.0
    return abs(first[0] * second[0] + first[1] * second[1])


def dependency_signature(
    scenario: mixed.MixedScenario,
    candidate: mixed.Candidate,
    training_states: Sequence[mixed.EpisodeState],
    cfg: mixed.MixedSensorConfig,
) -> ActiveBoundaryRow:
    outcome_direction, outcome_strength = subspace.learn_sensor_direction(training_states)
    owned_direction, owned_strength = learn_owned_action_direction(training_states)
    alignment = direction_alignment(outcome_direction, owned_direction)
    states = mixed.make_states(scenario, "dependency", cfg.episodes, cfg)
    intact = statistics.fmean(
        mixed.evaluate_recurrent(state, candidate, cfg, "none")[0]
        for state in states
    )
    ablated = statistics.fmean(
        subspace.evaluate_recurrent_with_learned_ablation(state, candidate, cfg, outcome_direction)[0]
        for state in states
    )
    loss = intact - ablated
    if (
        loss > MIN_OUTCOME_DIRECTION_LOSS
        and alignment >= MIN_OWNED_ALIGNMENT
        and owned_strength >= MIN_OWNED_DIRECTION_STRENGTH
    ):
        signature = "agent_bounded_active_boundary"
    elif loss > MIN_OUTCOME_DIRECTION_LOSS and alignment <= MAX_EXTERNAL_ALIGNMENT:
        signature = "external_active_boundary"
    else:
        signature = "no_active_boundary"
    return ActiveBoundaryRow(
        scenario=scenario.name,
        dependency_signature=signature,
        outcome_direction_x=outcome_direction[0],
        outcome_direction_y=outcome_direction[1],
        outcome_direction_strength=outcome_strength,
        owned_action_direction_x=owned_direction[0],
        owned_action_direction_y=owned_direction[1],
        owned_action_direction_strength=owned_strength,
        owned_action_alignment=alignment,
        outcome_direction_ablation_loss=loss,
        intact_recurrent_reward=intact,
        outcome_direction_ablated_reward=ablated,
    )


def verdict_rows(
    summary_rows: Sequence[Dict[str, object]],
    training_rows: Sequence[mixed.TrainingRow],
    boundary_rows: Sequence[ActiveBoundaryRow],
) -> List[Dict[str, object]]:
    rows = []
    for scenario in sorted({str(row["scenario"]) for row in summary_rows}):
        training = next(row for row in training_rows if row.scenario == scenario)
        boundary = next(row for row in boundary_rows if row.scenario == scenario)
        recurrent_reward = mixed.reward_for(summary_rows, scenario, "recurrent_controller")
        local_reward = mixed.reward_for(summary_rows, scenario, "task_local_probe")
        greedy_reward = mixed.reward_for(summary_rows, scenario, "greedy_no_state")
        selector_reward = mixed.reward_for(summary_rows, scenario, "learned_structure_selector")
        rows.append(
            {
                "scenario": scenario,
                "selected_policy": training.selected_policy,
                "selected_architecture": training.selected_architecture,
                "dependency_signature": boundary.dependency_signature,
                "recurrent_reward": recurrent_reward,
                "local_probe_reward": local_reward,
                "greedy_reward": greedy_reward,
                "selector_reward": selector_reward,
                "outcome_direction_ablation_loss": boundary.outcome_direction_ablation_loss,
                "owned_action_alignment": boundary.owned_action_alignment,
                "supports_active_boundary_prediction": scenario_supports_prediction(
                    scenario,
                    training.selected_policy,
                    boundary.dependency_signature,
                    recurrent_reward,
                    local_reward,
                    greedy_reward,
                    boundary.outcome_direction_ablation_loss,
                    boundary.owned_action_alignment,
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
    outcome_loss: float,
    alignment: float,
) -> bool:
    if scenario == "self_mixed_hidden":
        return (
            selected_policy == "recurrent_controller"
            and signature == "agent_bounded_active_boundary"
            and recurrent_reward > local_reward
            and outcome_loss > MIN_OUTCOME_DIRECTION_LOSS
            and alignment >= MIN_OWNED_ALIGNMENT
        )
    if scenario == "world_mixed_hidden":
        return (
            selected_policy == "recurrent_controller"
            and signature == "external_active_boundary"
            and recurrent_reward > local_reward
            and outcome_loss > MIN_OUTCOME_DIRECTION_LOSS
            and alignment <= MAX_EXTERNAL_ALIGNMENT
        )
    if scenario == "independent_hidden":
        return (
            selected_policy == "task_local_probe"
            and signature == "no_active_boundary"
            and local_reward > recurrent_reward + 40.0
        )
    if scenario == "irrelevant_control":
        return (
            selected_policy == "greedy_no_state"
            and signature == "no_active_boundary"
            and greedy_reward > recurrent_reward
        )
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: mixed.MixedSensorConfig,
) -> Tuple[
    List[mixed.AgentResult],
    List[Dict[str, object]],
    List[mixed.TrainingRow],
    List[ActiveBoundaryRow],
    List[Dict[str, object]],
]:
    results = []
    training_rows = []
    boundary_rows = []
    for scenario in mixed.SCENARIOS:
        training_states = mixed.make_states(scenario, "train", cfg.training_episodes, cfg)
        candidate = mixed.train_recurrent(scenario, training_states, cfg)
        selected_policy, rewards = mixed.select_policy(candidate, training_states, cfg)
        boundary = dependency_signature(scenario, candidate, training_states, cfg)
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
        boundary_rows.append(boundary)
        test_states = mixed.make_states(scenario, "test", cfg.episodes, cfg)
        for state in test_states:
            for agent in mixed.AGENTS:
                results.append(
                    mixed.run_agent(
                        scenario,
                        state,
                        agent,
                        selected_policy,
                        candidate,
                        boundary.dependency_signature,
                        cfg,
                    )
                )
    summary_rows = mixed.summarize(results)
    verdicts = verdict_rows(summary_rows, training_rows, boundary_rows)
    return results, summary_rows, training_rows, boundary_rows, verdicts


def write_csv(path: Path, rows: Iterable[object]) -> None:
    mixed.write_csv(path, rows)


def print_table(verdicts: Sequence[Dict[str, object]]) -> None:
    headers = [
        "scenario",
        "selected_policy",
        "dependency_signature",
        "recurrent_reward",
        "local_probe_reward",
        "outcome_direction_ablation_loss",
        "owned_action_alignment",
        "supports_active_boundary_prediction",
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
                f"{float(verdict['outcome_direction_ablation_loss']):.3f}",
                f"{float(verdict['owned_action_alignment']):.3f}",
                str(verdict["supports_active_boundary_prediction"]),
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
    results, summary_rows, training_rows, boundary_rows, verdicts = run_experiment(cfg)
    summary_path = ARTIFACT_DIR / "active_boundary_discovery_summary.csv"
    training_path = ARTIFACT_DIR / "active_boundary_discovery_training.csv"
    boundary_path = ARTIFACT_DIR / "active_boundary_discovery_boundary.csv"
    verdict_path = ARTIFACT_DIR / "active_boundary_discovery_verdict.csv"
    results_path = ARTIFACT_DIR / "active_boundary_discovery_results.json"
    write_csv(summary_path, summary_rows)
    write_csv(training_path, training_rows)
    write_csv(boundary_path, boundary_rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "training": [asdict(row) for row in training_rows],
                "boundary": [asdict(row) for row in boundary_rows],
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
    print(f"wrote {boundary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print_table(verdicts)
    return 0 if all(bool(row["supports_active_boundary_prediction"]) for row in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
