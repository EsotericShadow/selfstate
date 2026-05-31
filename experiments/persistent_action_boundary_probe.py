#!/usr/bin/env python3
"""Persistent action-boundary probe.

This is a stricter companion to action_effect_boundary_probe.py. The previous
test rejected controllable external state when it aligned with a tool action
rather than the body/action-effect direction. The remaining shortcut is that
the body and tool diagnostic actions are supplied as named probes.

This version compares generic action-effect directions across two contexts. A
candidate self boundary must align with an action-effect direction that persists
across contexts. A detachable tool-like effect can be useful and controllable in
one context, but it disappears in transfer and should remain external.
"""

from __future__ import annotations

import argparse
import json
import math
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import active_boundary_discovery as active
import learned_sensor_subspace_filter as subspace
import mixed_sensor_recurrent_filter as mixed


ARTIFACT_DIR = Path("artifacts")
MIN_OUTCOME_DIRECTION_LOSS = 30.0
MIN_ACTION_ALIGNMENT = 0.70
MIN_PERSISTENCE = 0.70
MAX_TRANSIENT_PERSISTENCE = 0.35
MAX_EXTERNAL_PERSISTENT_ALIGNMENT = 0.35


@dataclass(frozen=True)
class BoundaryScenario:
    name: str
    mode: str
    detachable_tool_available: bool


@dataclass(frozen=True)
class ActionProfile:
    present_direction: Tuple[float, float]
    transfer_direction: Tuple[float, float]
    present_strength: float
    transfer_strength: float
    outcome_alignment: float
    persistence_score: float


@dataclass(frozen=True)
class PersistentBoundaryRow:
    scenario: str
    dependency_signature: str
    outcome_direction_x: float
    outcome_direction_y: float
    outcome_direction_strength: float
    action_0_alignment: float
    action_0_persistence: float
    action_0_present_strength: float
    action_0_transfer_strength: float
    action_1_alignment: float
    action_1_persistence: float
    action_1_present_strength: float
    action_1_transfer_strength: float
    best_persistent_alignment: float
    best_transient_alignment: float
    outcome_direction_ablation_loss: float
    intact_recurrent_reward: float
    outcome_direction_ablated_reward: float


SCENARIOS = [
    BoundaryScenario("self_persistent_boundary", "self_mixed_hidden", False),
    BoundaryScenario("detachable_tool_world", "world_mixed_hidden", True),
    BoundaryScenario("passive_world_boundary", "world_mixed_hidden", False),
    BoundaryScenario("independent_hidden", "independent_hidden", False),
    BoundaryScenario("irrelevant_control", "irrelevant_control", False),
]


def as_mixed_scenario(scenario: BoundaryScenario) -> mixed.MixedScenario:
    return mixed.MixedScenario(scenario.name, scenario.mode)


def effect_delta(
    scenario: BoundaryScenario,
    state: mixed.EpisodeState,
    action_index: int,
    context: str,
) -> Tuple[float, float]:
    deltas = []
    for source_a, source_b in state.source_observations:
        before = mixed.mix_sources(source_a, source_b)
        if action_index == 0:
            after = mixed.mix_sources(1.0, source_b)
        elif action_index == 1 and scenario.detachable_tool_available and context == "present":
            after = mixed.mix_sources(source_a, 1.0)
        elif action_index == 1:
            after = before
        else:
            raise ValueError(f"unknown action index: {action_index}")
        deltas.append((after[0] - before[0], after[1] - before[1]))
    return active.mean_vector(deltas)


def learn_action_profile(
    scenario: BoundaryScenario,
    states: Sequence[mixed.EpisodeState],
    action_index: int,
    outcome_direction: Tuple[float, float],
) -> ActionProfile:
    present_direction, present_strength = active.normalize(
        active.mean_vector([effect_delta(scenario, state, action_index, "present") for state in states])
    )
    transfer_direction, transfer_strength = active.normalize(
        active.mean_vector([effect_delta(scenario, state, action_index, "transfer") for state in states])
    )
    if max(present_strength, transfer_strength) < 1e-12:
        persistence = 0.0
    else:
        strength_ratio = min(present_strength, transfer_strength) / max(present_strength, transfer_strength)
        persistence = active.direction_alignment(present_direction, transfer_direction) * strength_ratio
    return ActionProfile(
        present_direction=present_direction,
        transfer_direction=transfer_direction,
        present_strength=present_strength,
        transfer_strength=transfer_strength,
        outcome_alignment=active.direction_alignment(outcome_direction, present_direction),
        persistence_score=persistence,
    )


def dependency_signature(
    scenario: BoundaryScenario,
    candidate: mixed.Candidate,
    training_states: Sequence[mixed.EpisodeState],
    cfg: mixed.MixedSensorConfig,
) -> PersistentBoundaryRow:
    outcome_direction, outcome_strength = subspace.learn_sensor_direction(training_states)
    action_0 = learn_action_profile(scenario, training_states, 0, outcome_direction)
    action_1 = learn_action_profile(scenario, training_states, 1, outcome_direction)
    profiles = [action_0, action_1]
    persistent_alignments = [
        profile.outcome_alignment
        for profile in profiles
        if profile.persistence_score >= MIN_PERSISTENCE
    ]
    transient_alignments = [
        profile.outcome_alignment
        for profile in profiles
        if profile.persistence_score <= MAX_TRANSIENT_PERSISTENCE
    ]
    best_persistent_alignment = max(persistent_alignments, default=0.0)
    best_transient_alignment = max(transient_alignments, default=0.0)
    mixed_scenario = as_mixed_scenario(scenario)
    states = mixed.make_states(mixed_scenario, "dependency", cfg.episodes, cfg)
    intact = statistics.fmean(
        mixed.evaluate_recurrent(state, candidate, cfg, "none")[0]
        for state in states
    )
    ablated = statistics.fmean(
        subspace.evaluate_recurrent_with_learned_ablation(state, candidate, cfg, outcome_direction)[0]
        for state in states
    )
    loss = intact - ablated
    if loss > MIN_OUTCOME_DIRECTION_LOSS and best_persistent_alignment >= MIN_ACTION_ALIGNMENT:
        signature = "persistent_agent_action_boundary"
    elif (
        loss > MIN_OUTCOME_DIRECTION_LOSS
        and best_transient_alignment >= MIN_ACTION_ALIGNMENT
        and best_persistent_alignment <= MAX_EXTERNAL_PERSISTENT_ALIGNMENT
    ):
        signature = "detachable_external_action_boundary"
    elif loss > MIN_OUTCOME_DIRECTION_LOSS and best_persistent_alignment <= MAX_EXTERNAL_PERSISTENT_ALIGNMENT:
        signature = "passive_external_persistent_boundary"
    else:
        signature = "no_persistent_action_boundary"
    return PersistentBoundaryRow(
        scenario=scenario.name,
        dependency_signature=signature,
        outcome_direction_x=outcome_direction[0],
        outcome_direction_y=outcome_direction[1],
        outcome_direction_strength=outcome_strength,
        action_0_alignment=action_0.outcome_alignment,
        action_0_persistence=action_0.persistence_score,
        action_0_present_strength=action_0.present_strength,
        action_0_transfer_strength=action_0.transfer_strength,
        action_1_alignment=action_1.outcome_alignment,
        action_1_persistence=action_1.persistence_score,
        action_1_present_strength=action_1.present_strength,
        action_1_transfer_strength=action_1.transfer_strength,
        best_persistent_alignment=best_persistent_alignment,
        best_transient_alignment=best_transient_alignment,
        outcome_direction_ablation_loss=loss,
        intact_recurrent_reward=intact,
        outcome_direction_ablated_reward=ablated,
    )


def verdict_rows(
    summary_rows: Sequence[Dict[str, object]],
    training_rows: Sequence[mixed.TrainingRow],
    boundary_rows: Sequence[PersistentBoundaryRow],
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
                "best_persistent_alignment": boundary.best_persistent_alignment,
                "best_transient_alignment": boundary.best_transient_alignment,
                "supports_persistent_action_boundary_prediction": scenario_supports_prediction(
                    scenario,
                    training.selected_policy,
                    boundary.dependency_signature,
                    recurrent_reward,
                    local_reward,
                    greedy_reward,
                    boundary.outcome_direction_ablation_loss,
                    boundary.best_persistent_alignment,
                    boundary.best_transient_alignment,
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
    persistent_alignment: float,
    transient_alignment: float,
) -> bool:
    if scenario == "self_persistent_boundary":
        return (
            selected_policy == "recurrent_controller"
            and signature == "persistent_agent_action_boundary"
            and recurrent_reward > local_reward
            and outcome_loss > MIN_OUTCOME_DIRECTION_LOSS
            and persistent_alignment >= MIN_ACTION_ALIGNMENT
        )
    if scenario == "detachable_tool_world":
        return (
            selected_policy == "recurrent_controller"
            and signature == "detachable_external_action_boundary"
            and recurrent_reward > local_reward
            and outcome_loss > MIN_OUTCOME_DIRECTION_LOSS
            and transient_alignment >= MIN_ACTION_ALIGNMENT
            and persistent_alignment <= MAX_EXTERNAL_PERSISTENT_ALIGNMENT
        )
    if scenario == "passive_world_boundary":
        return (
            selected_policy == "recurrent_controller"
            and signature == "passive_external_persistent_boundary"
            and recurrent_reward > local_reward
            and outcome_loss > MIN_OUTCOME_DIRECTION_LOSS
            and persistent_alignment <= MAX_EXTERNAL_PERSISTENT_ALIGNMENT
        )
    if scenario == "independent_hidden":
        return (
            selected_policy == "task_local_probe"
            and signature == "no_persistent_action_boundary"
            and local_reward > recurrent_reward + 40.0
        )
    if scenario == "irrelevant_control":
        return (
            selected_policy == "greedy_no_state"
            and signature == "no_persistent_action_boundary"
            and greedy_reward > recurrent_reward
        )
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: mixed.MixedSensorConfig,
) -> Tuple[
    List[mixed.AgentResult],
    List[Dict[str, object]],
    List[mixed.TrainingRow],
    List[PersistentBoundaryRow],
    List[Dict[str, object]],
]:
    results = []
    training_rows = []
    boundary_rows = []
    for scenario in SCENARIOS:
        mixed_scenario = as_mixed_scenario(scenario)
        training_states = mixed.make_states(mixed_scenario, "train", cfg.training_episodes, cfg)
        candidate = mixed.train_recurrent(mixed_scenario, training_states, cfg)
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
        test_states = mixed.make_states(mixed_scenario, "test", cfg.episodes, cfg)
        for state in test_states:
            for agent in mixed.AGENTS:
                results.append(
                    mixed.run_agent(
                        mixed_scenario,
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
        "best_persistent_alignment",
        "best_transient_alignment",
        "supports_persistent_action_boundary_prediction",
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
                f"{float(verdict['best_persistent_alignment']):.3f}",
                f"{float(verdict['best_transient_alignment']):.3f}",
                str(verdict["supports_persistent_action_boundary_prediction"]),
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
    summary_path = ARTIFACT_DIR / "persistent_action_boundary_probe_summary.csv"
    training_path = ARTIFACT_DIR / "persistent_action_boundary_probe_training.csv"
    boundary_path = ARTIFACT_DIR / "persistent_action_boundary_probe_boundary.csv"
    verdict_path = ARTIFACT_DIR / "persistent_action_boundary_probe_verdict.csv"
    results_path = ARTIFACT_DIR / "persistent_action_boundary_probe_results.json"
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
    return 0 if all(bool(row["supports_persistent_action_boundary_prediction"]) for row in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
