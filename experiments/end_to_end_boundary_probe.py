#!/usr/bin/env python3
"""End-to-end recurrent boundary probe.

This is a stricter companion to return_selected_boundary_probe.py. The previous
test proposed explicit action-boundary policies from action-observation deltas
and selected among them by return. This version removes those supplied boundary
policies. It trains a recurrent controller by return, then probes whether the
controller's own policy state moves under persistent body-action interventions
or only under detachable external-tool interventions.

The test is still toy-scale. Its purpose is to separate "a hidden state is
useful" from "the learned hidden state has a persistent agent-boundary role."
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
import persistent_action_boundary_probe as persistent


ARTIFACT_DIR = Path("artifacts")
MIN_RECURRENT_ADVANTAGE = 1.0
MIN_POLICY_EFFECT = 2.0
MIN_EFFECT_DOMINANCE = 2.0
MIN_LOCAL_ADVANTAGE = 40.0
MIN_PERSISTENCE = 0.70
MAX_TRANSIENT_PERSISTENCE = 0.35
EPS = 1e-12


@dataclass(frozen=True)
class ActionPolicyEffect:
    present_logit_effect: float
    transfer_logit_effect: float
    present_abs_effect: float
    transfer_abs_effect: float
    present_flip_rate: float
    transfer_flip_rate: float
    positive_present_effect: float
    positive_transfer_effect: float
    persistence_score: float


@dataclass(frozen=True)
class EndToEndBoundaryRow:
    scenario: str
    selected_policy: str
    selected_architecture: str
    dependency_signature: str
    recurrent_training_reward: float
    local_training_reward: float
    greedy_training_reward: float
    safe_training_reward: float
    latent_mean: float
    latent_std: float
    latent_self_accuracy: float
    latent_world_accuracy: float
    action_0_present_logit_effect: float
    action_0_transfer_logit_effect: float
    action_0_positive_present_effect: float
    action_0_persistence: float
    action_0_present_flip_rate: float
    action_1_present_logit_effect: float
    action_1_transfer_logit_effect: float
    action_1_positive_present_effect: float
    action_1_persistence: float
    action_1_present_flip_rate: float
    best_persistent_action: str
    best_transient_action: str
    best_persistent_score: float
    best_transient_score: float
    selected_weights: str


AGENTS = [
    "greedy_no_state",
    "safe_no_state",
    "recurrent_controller",
    "task_local_probe",
    "learned_structure_selector",
    "oracle_observation",
]


def intervened_observations(
    scenario: persistent.BoundaryScenario,
    state: mixed.EpisodeState,
    action_index: int,
    context: str,
) -> Tuple[Tuple[float, float], ...]:
    observations = []
    for source_a, source_b in state.source_observations:
        if action_index == 0:
            observations.append(mixed.mix_sources(1.0, source_b))
        elif action_index == 1 and scenario.detachable_tool_available and context == "present":
            observations.append(mixed.mix_sources(source_a, 1.0))
        elif action_index == 1:
            observations.append(mixed.mix_sources(source_a, source_b))
        else:
            raise ValueError(f"unknown action index: {action_index}")
    return tuple(observations)


def logit_effect(
    scenario: persistent.BoundaryScenario,
    candidate: mixed.Candidate,
    states: Sequence[mixed.EpisodeState],
    action_index: int,
    context: str,
) -> Tuple[float, float, float]:
    signed_effects = []
    abs_effects = []
    flips = 0
    for state in states:
        before = mixed.recurrent_logit(candidate, state.mixed_observations)
        after = mixed.recurrent_logit(
            candidate,
            intervened_observations(scenario, state, action_index, context),
        )
        signed_effects.append(after - before)
        abs_effects.append(abs(after - before))
        if (before >= 0.0) != (after >= 0.0):
            flips += 1
    return (
        statistics.fmean(signed_effects),
        statistics.fmean(abs_effects),
        flips / len(states),
    )


def action_policy_effect(
    scenario: persistent.BoundaryScenario,
    candidate: mixed.Candidate,
    states: Sequence[mixed.EpisodeState],
    action_index: int,
) -> ActionPolicyEffect:
    present_effect, present_abs, present_flip = logit_effect(
        scenario,
        candidate,
        states,
        action_index,
        "present",
    )
    transfer_effect, transfer_abs, transfer_flip = logit_effect(
        scenario,
        candidate,
        states,
        action_index,
        "transfer",
    )
    positive_present = max(0.0, present_effect)
    positive_transfer = max(0.0, transfer_effect)
    if max(positive_present, positive_transfer) <= EPS:
        persistence = 0.0
    else:
        persistence = min(positive_present, positive_transfer) / max(positive_present, positive_transfer)
    return ActionPolicyEffect(
        present_logit_effect=present_effect,
        transfer_logit_effect=transfer_effect,
        present_abs_effect=present_abs,
        transfer_abs_effect=transfer_abs,
        present_flip_rate=present_flip,
        transfer_flip_rate=transfer_flip,
        positive_present_effect=positive_present,
        positive_transfer_effect=positive_transfer,
        persistence_score=persistence,
    )


def classify_boundary(
    selected_policy: str,
    recurrent_reward: float,
    local_reward: float,
    greedy_reward: float,
    action_0: ActionPolicyEffect,
    action_1: ActionPolicyEffect,
) -> str:
    if selected_policy == "task_local_probe":
        return "end_to_end_local_probe"
    if selected_policy == "greedy_no_state":
        return "end_to_end_no_hidden_needed"
    if selected_policy != "recurrent_controller":
        return "end_to_end_no_boundary"

    persistent_scores = {
        "action_0": action_0.positive_present_effect if action_0.persistence_score >= MIN_PERSISTENCE else 0.0,
        "action_1": action_1.positive_present_effect if action_1.persistence_score >= MIN_PERSISTENCE else 0.0,
    }
    transient_scores = {
        "action_0": action_0.positive_present_effect if action_0.persistence_score <= MAX_TRANSIENT_PERSISTENCE else 0.0,
        "action_1": action_1.positive_present_effect if action_1.persistence_score <= MAX_TRANSIENT_PERSISTENCE else 0.0,
    }
    best_persistent_action, best_persistent_score = best_score(persistent_scores)
    best_transient_action, best_transient_score = best_score(transient_scores)

    if (
        recurrent_reward > local_reward + MIN_RECURRENT_ADVANTAGE
        and best_persistent_action == "action_0"
        and best_persistent_score >= MIN_POLICY_EFFECT
        and best_persistent_score > best_transient_score + MIN_EFFECT_DOMINANCE
    ):
        return "end_to_end_persistent_agent_boundary"
    if (
        recurrent_reward > local_reward + MIN_RECURRENT_ADVANTAGE
        and best_transient_action == "action_1"
        and best_transient_score >= MIN_POLICY_EFFECT
        and best_transient_score > best_persistent_score + MIN_EFFECT_DOMINANCE
    ):
        return "end_to_end_detachable_external_boundary"
    if (
        recurrent_reward > local_reward + MIN_RECURRENT_ADVANTAGE
        and max(best_persistent_score, best_transient_score) < MIN_POLICY_EFFECT
    ):
        return "end_to_end_passive_external_boundary"
    if greedy_reward >= recurrent_reward - EPS:
        return "end_to_end_no_hidden_needed"
    return "end_to_end_unclassified_recurrent_boundary"


def best_score(scores: Dict[str, float]) -> Tuple[str, float]:
    return max(scores.items(), key=lambda item: (item[1], -int(item[0].split("_")[1])))


def build_boundary_row(
    scenario: persistent.BoundaryScenario,
    candidate: mixed.Candidate,
    selected_policy: str,
    rewards: Dict[str, float],
    cfg: mixed.MixedSensorConfig,
) -> EndToEndBoundaryRow:
    mixed_scenario = persistent.as_mixed_scenario(scenario)
    dependency_states = mixed.make_states(mixed_scenario, "end_to_end_dependency", cfg.episodes, cfg)
    latents = [mixed.recurrent_logit(candidate, state.mixed_observations) for state in dependency_states]
    action_0 = action_policy_effect(scenario, candidate, dependency_states, 0)
    action_1 = action_policy_effect(scenario, candidate, dependency_states, 1)
    persistent_scores = {
        "action_0": action_0.positive_present_effect if action_0.persistence_score >= MIN_PERSISTENCE else 0.0,
        "action_1": action_1.positive_present_effect if action_1.persistence_score >= MIN_PERSISTENCE else 0.0,
    }
    transient_scores = {
        "action_0": action_0.positive_present_effect if action_0.persistence_score <= MAX_TRANSIENT_PERSISTENCE else 0.0,
        "action_1": action_1.positive_present_effect if action_1.persistence_score <= MAX_TRANSIENT_PERSISTENCE else 0.0,
    }
    best_persistent_action, best_persistent_score = best_score(persistent_scores)
    best_transient_action, best_transient_score = best_score(transient_scores)
    signature = classify_boundary(
        selected_policy=selected_policy,
        recurrent_reward=rewards["recurrent_controller"],
        local_reward=rewards["task_local_probe"],
        greedy_reward=rewards["greedy_no_state"],
        action_0=action_0,
        action_1=action_1,
    )
    return EndToEndBoundaryRow(
        scenario=scenario.name,
        selected_policy=selected_policy,
        selected_architecture=candidate.architecture,
        dependency_signature=signature,
        recurrent_training_reward=rewards["recurrent_controller"],
        local_training_reward=rewards["task_local_probe"],
        greedy_training_reward=rewards["greedy_no_state"],
        safe_training_reward=rewards["safe_no_state"],
        latent_mean=statistics.fmean(latents),
        latent_std=sample_std(latents),
        latent_self_accuracy=threshold_accuracy(latents, [state.source_a_signal for state in dependency_states]),
        latent_world_accuracy=threshold_accuracy(latents, [state.source_b_signal for state in dependency_states]),
        action_0_present_logit_effect=action_0.present_logit_effect,
        action_0_transfer_logit_effect=action_0.transfer_logit_effect,
        action_0_positive_present_effect=action_0.positive_present_effect,
        action_0_persistence=action_0.persistence_score,
        action_0_present_flip_rate=action_0.present_flip_rate,
        action_1_present_logit_effect=action_1.present_logit_effect,
        action_1_transfer_logit_effect=action_1.transfer_logit_effect,
        action_1_positive_present_effect=action_1.positive_present_effect,
        action_1_persistence=action_1.persistence_score,
        action_1_present_flip_rate=action_1.present_flip_rate,
        best_persistent_action=best_persistent_action,
        best_transient_action=best_transient_action,
        best_persistent_score=best_persistent_score,
        best_transient_score=best_transient_score,
        selected_weights=mixed.format_weights(candidate.weights),
    )


def threshold_accuracy(values: Sequence[float], labels: Sequence[bool]) -> float:
    if not values or not labels:
        return 0.5
    if all(label == labels[0] for label in labels):
        return 0.5
    unique_values = sorted(set(values))
    thresholds = [unique_values[0] - EPS, unique_values[-1] + EPS]
    thresholds.extend((left + right) / 2.0 for left, right in zip(unique_values, unique_values[1:]))
    best = 0.0
    for threshold in thresholds:
        for direction in [1, -1]:
            correct = 0
            for value, label in zip(values, labels):
                predicted = value >= threshold if direction == 1 else value <= threshold
                if predicted == label:
                    correct += 1
            best = max(best, correct / len(values))
    return best


def sample_std(values: Sequence[float]) -> float:
    if len(values) < 2:
        return 0.0
    return statistics.pstdev(values)


def run_agent(
    scenario: persistent.BoundaryScenario,
    state: mixed.EpisodeState,
    agent: str,
    boundary: EndToEndBoundaryRow,
    candidate: mixed.Candidate,
    cfg: mixed.MixedSensorConfig,
) -> mixed.AgentResult:
    mixed_scenario = persistent.as_mixed_scenario(scenario)
    return mixed.run_agent(
        mixed_scenario,
        state,
        agent,
        boundary.selected_policy,
        candidate,
        boundary.dependency_signature,
        cfg,
    )


def verdict_rows(
    summary_rows: Sequence[Dict[str, object]],
    training_rows: Sequence[mixed.TrainingRow],
    boundary_rows: Sequence[EndToEndBoundaryRow],
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
                "selector_reward": selector_reward,
                "recurrent_reward": recurrent_reward,
                "local_probe_reward": local_reward,
                "greedy_reward": greedy_reward,
                "latent_self_accuracy": boundary.latent_self_accuracy,
                "latent_world_accuracy": boundary.latent_world_accuracy,
                "action_0_positive_present_effect": boundary.action_0_positive_present_effect,
                "action_0_persistence": boundary.action_0_persistence,
                "action_1_positive_present_effect": boundary.action_1_positive_present_effect,
                "action_1_persistence": boundary.action_1_persistence,
                "best_persistent_score": boundary.best_persistent_score,
                "best_transient_score": boundary.best_transient_score,
                "supports_end_to_end_boundary_prediction": scenario_supports_prediction(
                    scenario=scenario,
                    selected_policy=training.selected_policy,
                    signature=boundary.dependency_signature,
                    selector_reward=selector_reward,
                    recurrent_reward=recurrent_reward,
                    local_reward=local_reward,
                    greedy_reward=greedy_reward,
                    boundary=boundary,
                ),
            }
        )
    return rows


def scenario_supports_prediction(
    scenario: str,
    selected_policy: str,
    signature: str,
    selector_reward: float,
    recurrent_reward: float,
    local_reward: float,
    greedy_reward: float,
    boundary: EndToEndBoundaryRow,
) -> bool:
    if scenario == "self_persistent_boundary":
        return (
            selected_policy == "recurrent_controller"
            and signature == "end_to_end_persistent_agent_boundary"
            and selector_reward > local_reward
            and boundary.action_0_positive_present_effect >= MIN_POLICY_EFFECT
            and boundary.action_0_persistence >= MIN_PERSISTENCE
            and boundary.best_persistent_score > boundary.best_transient_score + MIN_EFFECT_DOMINANCE
        )
    if scenario == "detachable_tool_world":
        return (
            selected_policy == "recurrent_controller"
            and signature == "end_to_end_detachable_external_boundary"
            and selector_reward > local_reward
            and boundary.action_1_positive_present_effect >= MIN_POLICY_EFFECT
            and boundary.action_1_persistence <= MAX_TRANSIENT_PERSISTENCE
            and boundary.best_transient_score > boundary.best_persistent_score + MIN_EFFECT_DOMINANCE
        )
    if scenario == "passive_world_boundary":
        return (
            selected_policy == "recurrent_controller"
            and signature == "end_to_end_passive_external_boundary"
            and recurrent_reward > local_reward
            and max(boundary.best_persistent_score, boundary.best_transient_score) < MIN_POLICY_EFFECT
        )
    if scenario == "independent_hidden":
        return (
            selected_policy == "task_local_probe"
            and signature == "end_to_end_local_probe"
            and local_reward > recurrent_reward + MIN_LOCAL_ADVANTAGE
        )
    if scenario == "irrelevant_control":
        return (
            selected_policy == "greedy_no_state"
            and signature == "end_to_end_no_hidden_needed"
            and greedy_reward >= selector_reward - EPS
        )
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: mixed.MixedSensorConfig,
) -> Tuple[
    List[mixed.AgentResult],
    List[Dict[str, object]],
    List[mixed.TrainingRow],
    List[EndToEndBoundaryRow],
    List[Dict[str, object]],
]:
    results: List[mixed.AgentResult] = []
    training_rows: List[mixed.TrainingRow] = []
    boundary_rows: List[EndToEndBoundaryRow] = []
    for scenario in persistent.SCENARIOS:
        mixed_scenario = persistent.as_mixed_scenario(scenario)
        training_states = mixed.make_states(mixed_scenario, "train", cfg.training_episodes, cfg)
        candidate = mixed.train_recurrent(mixed_scenario, training_states, cfg)
        selected_policy, rewards = mixed.select_policy(candidate, training_states, cfg)
        boundary = build_boundary_row(scenario, candidate, selected_policy, rewards, cfg)
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
            for agent in AGENTS:
                results.append(run_agent(scenario, state, agent, boundary, candidate, cfg))
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
        "selector_reward",
        "local_probe_reward",
        "action_0_positive_present_effect",
        "action_0_persistence",
        "action_1_positive_present_effect",
        "action_1_persistence",
        "supports_end_to_end_boundary_prediction",
    ]
    rows = []
    for verdict in verdicts:
        rows.append(
            [
                str(verdict["scenario"]),
                str(verdict["selected_policy"]),
                str(verdict["dependency_signature"]),
                f"{float(verdict['selector_reward']):.3f}",
                f"{float(verdict['local_probe_reward']):.3f}",
                f"{float(verdict['action_0_positive_present_effect']):.3f}",
                f"{float(verdict['action_0_persistence']):.3f}",
                f"{float(verdict['action_1_positive_present_effect']):.3f}",
                f"{float(verdict['action_1_persistence']):.3f}",
                str(verdict["supports_end_to_end_boundary_prediction"]),
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
    summary_path = ARTIFACT_DIR / "end_to_end_boundary_probe_summary.csv"
    training_path = ARTIFACT_DIR / "end_to_end_boundary_probe_training.csv"
    boundary_path = ARTIFACT_DIR / "end_to_end_boundary_probe_boundary.csv"
    verdict_path = ARTIFACT_DIR / "end_to_end_boundary_probe_verdict.csv"
    results_path = ARTIFACT_DIR / "end_to_end_boundary_probe_results.json"
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
    return 0 if all(bool(row["supports_end_to_end_boundary_prediction"]) for row in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
