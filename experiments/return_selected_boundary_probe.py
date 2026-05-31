#!/usr/bin/env python3
"""Return-selected persistent boundary probe.

This is a stricter companion to persistent_action_boundary_probe.py. The
previous test still learned an outcome-predictive direction from observed
success rates, then compared it with persistent and transient action effects.

This version removes that outcome-supervised direction. It learns generic
action-effect directions from action-observation deltas, turns those directions
into candidate policies, and selects among them by training return after action.
The question is whether return selection favors a persistent action boundary
only in the self regime, a transient action boundary in a detachable-tool
external regime, recurrent world filtering in passive-world regimes, and local
or no-state policies in matched controls.
"""

from __future__ import annotations

import argparse
import json
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import mixed_sensor_recurrent_filter as mixed
import persistent_action_boundary_probe as persistent


ARTIFACT_DIR = Path("artifacts")
MIN_ACTION_ADVANTAGE = 1.0
MIN_RECURRENT_ADVANTAGE = 1.0
MIN_PERSISTENCE = 0.70
MAX_TRANSIENT_PERSISTENCE = 0.35


@dataclass(frozen=True)
class ReturnBoundaryRow:
    scenario: str
    selected_policy: str
    selected_boundary_policy: str
    selected_architecture: str
    dependency_signature: str
    selected_training_reward: float
    selected_boundary_training_reward: float
    recurrent_training_reward: float
    action_0_training_reward: float
    action_1_training_reward: float
    local_training_reward: float
    greedy_training_reward: float
    safe_training_reward: float
    action_0_persistence: float
    action_1_persistence: float
    action_0_present_strength: float
    action_1_present_strength: float
    selected_weights: str


POLICY_PRIORITY = {
    "action_0_boundary_policy": 0,
    "action_1_boundary_policy": 1,
    "recurrent_controller": 2,
    "task_local_probe": 3,
    "greedy_no_state": 4,
    "safe_no_state": 5,
}


AGENTS = [
    "greedy_no_state",
    "safe_no_state",
    "recurrent_controller",
    "action_0_boundary_policy",
    "action_1_boundary_policy",
    "task_local_probe",
    "learned_structure_selector",
    "oracle_observation",
]


def action_direction(
    scenario: persistent.BoundaryScenario,
    states: Sequence[mixed.EpisodeState],
    action_index: int,
    context: str,
) -> Tuple[Tuple[float, float], float]:
    return persistent.active.normalize(
        persistent.active.mean_vector(
            [persistent.effect_delta(scenario, state, action_index, context) for state in states]
        )
    )


def action_profile(
    scenario: persistent.BoundaryScenario,
    states: Sequence[mixed.EpisodeState],
    action_index: int,
) -> Tuple[Tuple[float, float], float, float]:
    present_direction, present_strength = action_direction(scenario, states, action_index, "present")
    transfer_direction, transfer_strength = action_direction(scenario, states, action_index, "transfer")
    if max(present_strength, transfer_strength) < 1e-12:
        persistence_score = 0.0
    else:
        strength_ratio = min(present_strength, transfer_strength) / max(present_strength, transfer_strength)
        persistence_score = (
            persistent.active.direction_alignment(present_direction, transfer_direction)
            * strength_ratio
        )
    return present_direction, present_strength, persistence_score


def evaluate_action_policy(
    state: mixed.EpisodeState,
    direction: Tuple[float, float],
    cfg: mixed.MixedSensorConfig,
) -> Tuple[float, int, int, int, int, int, int]:
    logit = statistics.fmean(
        sensor_1 * direction[0] + sensor_2 * direction[1]
        for sensor_1, sensor_2 in state.mixed_observations
    )
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


def mean_action_reward(
    states: Sequence[mixed.EpisodeState],
    direction: Tuple[float, float],
    cfg: mixed.MixedSensorConfig,
) -> float:
    return statistics.fmean(evaluate_action_policy(state, direction, cfg)[0] for state in states)


def select_policy(rewards: Dict[str, float]) -> str:
    return min(rewards, key=lambda policy: (-rewards[policy], POLICY_PRIORITY[policy]))


def classify_signature(
    selected_boundary_policy: str,
    selected_boundary_reward: float,
    selected_controller_policy: str,
    local_reward: float,
    greedy_reward: float,
    recurrent_reward: float,
    action_0_persistence: float,
    action_1_persistence: float,
) -> str:
    if selected_controller_policy == "task_local_probe":
        return "return_selected_local_probe"
    if selected_controller_policy == "greedy_no_state":
        return "return_selected_no_hidden_needed"
    if selected_boundary_policy == "action_0_boundary_policy":
        if action_0_persistence >= MIN_PERSISTENCE and selected_boundary_reward > local_reward + MIN_ACTION_ADVANTAGE:
            return "return_selected_persistent_agent_boundary"
        if action_0_persistence <= MAX_TRANSIENT_PERSISTENCE and selected_boundary_reward > local_reward + MIN_ACTION_ADVANTAGE:
            return "return_selected_detachable_external_boundary"
    if selected_boundary_policy == "action_1_boundary_policy":
        if action_1_persistence >= MIN_PERSISTENCE and selected_boundary_reward > local_reward + MIN_ACTION_ADVANTAGE:
            return "return_selected_persistent_agent_boundary"
        if action_1_persistence <= MAX_TRANSIENT_PERSISTENCE and selected_boundary_reward > local_reward + MIN_ACTION_ADVANTAGE:
            return "return_selected_detachable_external_boundary"
    if selected_controller_policy == "recurrent_controller" and recurrent_reward > local_reward + MIN_RECURRENT_ADVANTAGE:
        return "return_selected_passive_external_boundary"
    return "return_selected_no_boundary"


def run_training(
    scenario: persistent.BoundaryScenario,
    cfg: mixed.MixedSensorConfig,
) -> Tuple[mixed.Candidate, ReturnBoundaryRow, Tuple[float, float], Tuple[float, float]]:
    mixed_scenario = persistent.as_mixed_scenario(scenario)
    training_states = mixed.make_states(mixed_scenario, "train", cfg.training_episodes, cfg)
    candidate = mixed.train_recurrent(mixed_scenario, training_states, cfg)
    action_0_direction, action_0_strength, action_0_persistence = action_profile(
        scenario,
        training_states,
        0,
    )
    action_1_direction, action_1_strength, action_1_persistence = action_profile(
        scenario,
        training_states,
        1,
    )
    rewards = {
        "recurrent_controller": candidate.training_reward,
        "action_0_boundary_policy": mean_action_reward(training_states, action_0_direction, cfg),
        "action_1_boundary_policy": mean_action_reward(training_states, action_1_direction, cfg),
        "task_local_probe": statistics.fmean(
            mixed.evaluate_baseline(state, "task_local_probe", cfg)[0]
            for state in training_states
        ),
        "greedy_no_state": statistics.fmean(
            mixed.evaluate_baseline(state, "greedy_no_state", cfg)[0]
            for state in training_states
        ),
        "safe_no_state": statistics.fmean(
            mixed.evaluate_baseline(state, "safe_no_state", cfg)[0]
            for state in training_states
        ),
    }
    selected_policy = select_policy(rewards)
    selected_boundary_policy = select_policy(
        {
            "action_0_boundary_policy": rewards["action_0_boundary_policy"],
            "action_1_boundary_policy": rewards["action_1_boundary_policy"],
        }
    )
    signature = classify_signature(
        selected_boundary_policy=selected_boundary_policy,
        selected_boundary_reward=rewards[selected_boundary_policy],
        selected_controller_policy=selected_policy,
        local_reward=rewards["task_local_probe"],
        greedy_reward=rewards["greedy_no_state"],
        recurrent_reward=rewards["recurrent_controller"],
        action_0_persistence=action_0_persistence,
        action_1_persistence=action_1_persistence,
    )
    return (
        candidate,
        ReturnBoundaryRow(
            scenario=scenario.name,
            selected_policy=selected_policy,
            selected_boundary_policy=selected_boundary_policy,
            selected_architecture=candidate.architecture,
            dependency_signature=signature,
            selected_training_reward=rewards[selected_policy],
            selected_boundary_training_reward=rewards[selected_boundary_policy],
            recurrent_training_reward=rewards["recurrent_controller"],
            action_0_training_reward=rewards["action_0_boundary_policy"],
            action_1_training_reward=rewards["action_1_boundary_policy"],
            local_training_reward=rewards["task_local_probe"],
            greedy_training_reward=rewards["greedy_no_state"],
            safe_training_reward=rewards["safe_no_state"],
            action_0_persistence=action_0_persistence,
            action_1_persistence=action_1_persistence,
            action_0_present_strength=action_0_strength,
            action_1_present_strength=action_1_strength,
            selected_weights=mixed.format_weights(candidate.weights),
        ),
        action_0_direction,
        action_1_direction,
    )


def run_agent(
    scenario: persistent.BoundaryScenario,
    state: mixed.EpisodeState,
    agent: str,
    training: ReturnBoundaryRow,
    candidate: mixed.Candidate,
    action_0_direction: Tuple[float, float],
    action_1_direction: Tuple[float, float],
    cfg: mixed.MixedSensorConfig,
) -> mixed.AgentResult:
    policy = training.selected_policy if agent == "learned_structure_selector" else agent
    if policy == "recurrent_controller":
        total, shared_cues, local_probes, risky, safe, failed, successes = mixed.evaluate_recurrent(
            state,
            candidate,
            cfg,
            "none",
        )
    elif policy == "action_0_boundary_policy":
        total, shared_cues, local_probes, risky, safe, failed, successes = evaluate_action_policy(
            state,
            action_0_direction,
            cfg,
        )
    elif policy == "action_1_boundary_policy":
        total, shared_cues, local_probes, risky, safe, failed, successes = evaluate_action_policy(
            state,
            action_1_direction,
            cfg,
        )
    else:
        total, shared_cues, local_probes, risky, safe, failed, successes = mixed.evaluate_baseline(
            state,
            policy,
            cfg,
        )
    return mixed.AgentResult(
        scenario=scenario.name,
        agent=agent,
        selected_policy=training.selected_policy,
        selected_architecture=training.selected_architecture,
        dependency_signature=training.dependency_signature,
        total_reward=total,
        shared_cue_count=shared_cues,
        local_probe_count=local_probes,
        risky_count=risky,
        safe_count=safe,
        failed_risky_count=failed,
        success_rate=successes / cfg.horizon,
    )


def verdict_rows(
    summary_rows: Sequence[Dict[str, object]],
    training_rows: Sequence[ReturnBoundaryRow],
) -> List[Dict[str, object]]:
    rows = []
    for scenario in sorted({str(row["scenario"]) for row in summary_rows}):
        training = next(row for row in training_rows if row.scenario == scenario)
        action_0_reward = mixed.reward_for(summary_rows, scenario, "action_0_boundary_policy")
        action_1_reward = mixed.reward_for(summary_rows, scenario, "action_1_boundary_policy")
        recurrent_reward = mixed.reward_for(summary_rows, scenario, "recurrent_controller")
        local_reward = mixed.reward_for(summary_rows, scenario, "task_local_probe")
        greedy_reward = mixed.reward_for(summary_rows, scenario, "greedy_no_state")
        selector_reward = mixed.reward_for(summary_rows, scenario, "learned_structure_selector")
        rows.append(
            {
                "scenario": scenario,
                "selected_policy": training.selected_policy,
                "selected_boundary_policy": training.selected_boundary_policy,
                "dependency_signature": training.dependency_signature,
                "selector_reward": selector_reward,
                "action_0_reward": action_0_reward,
                "action_1_reward": action_1_reward,
                "recurrent_reward": recurrent_reward,
                "local_probe_reward": local_reward,
                "greedy_reward": greedy_reward,
                "action_0_persistence": training.action_0_persistence,
                "action_1_persistence": training.action_1_persistence,
                "supports_return_selected_boundary_prediction": scenario_supports_prediction(
                    scenario,
                    training.selected_policy,
                    training.selected_boundary_policy,
                    training.dependency_signature,
                    selector_reward,
                    action_0_reward,
                    action_1_reward,
                    recurrent_reward,
                    local_reward,
                    greedy_reward,
                    training.action_0_persistence,
                    training.action_1_persistence,
                ),
            }
        )
    return rows


def scenario_supports_prediction(
    scenario: str,
    selected_policy: str,
    selected_boundary_policy: str,
    signature: str,
    selector_reward: float,
    action_0_reward: float,
    action_1_reward: float,
    recurrent_reward: float,
    local_reward: float,
    greedy_reward: float,
    action_0_persistence: float,
    action_1_persistence: float,
) -> bool:
    if scenario == "self_persistent_boundary":
        return (
            selected_boundary_policy == "action_0_boundary_policy"
            and signature == "return_selected_persistent_agent_boundary"
            and selector_reward > local_reward
            and action_0_persistence >= MIN_PERSISTENCE
        )
    if scenario == "detachable_tool_world":
        return (
            selected_boundary_policy == "action_1_boundary_policy"
            and signature == "return_selected_detachable_external_boundary"
            and selector_reward > local_reward
            and action_1_persistence <= MAX_TRANSIENT_PERSISTENCE
        )
    if scenario == "passive_world_boundary":
        return (
            selected_policy == "recurrent_controller"
            and signature == "return_selected_passive_external_boundary"
            and recurrent_reward > local_reward
            and action_0_reward < local_reward
            and action_1_reward < local_reward
        )
    if scenario == "independent_hidden":
        return (
            selected_policy == "task_local_probe"
            and signature == "return_selected_local_probe"
            and local_reward > recurrent_reward + 40.0
        )
    if scenario == "irrelevant_control":
        return (
            selected_policy == "greedy_no_state"
            and signature == "return_selected_no_hidden_needed"
            and greedy_reward > selector_reward - 1e-9
        )
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: mixed.MixedSensorConfig,
) -> Tuple[List[mixed.AgentResult], List[Dict[str, object]], List[ReturnBoundaryRow], List[Dict[str, object]]]:
    results = []
    training_rows = []
    for scenario in persistent.SCENARIOS:
        candidate, training, action_0_direction, action_1_direction = run_training(scenario, cfg)
        training_rows.append(training)
        mixed_scenario = persistent.as_mixed_scenario(scenario)
        test_states = mixed.make_states(mixed_scenario, "test", cfg.episodes, cfg)
        for state in test_states:
            for agent in AGENTS:
                results.append(
                    run_agent(
                        scenario,
                        state,
                        agent,
                        training,
                        candidate,
                        action_0_direction,
                        action_1_direction,
                        cfg,
                    )
                )
    summary_rows = mixed.summarize(results)
    verdicts = verdict_rows(summary_rows, training_rows)
    return results, summary_rows, training_rows, verdicts


def write_csv(path: Path, rows: Iterable[object]) -> None:
    mixed.write_csv(path, rows)


def print_table(verdicts: Sequence[Dict[str, object]]) -> None:
    headers = [
        "scenario",
        "selected_policy",
        "selected_boundary_policy",
        "dependency_signature",
        "selector_reward",
        "local_probe_reward",
        "action_0_persistence",
        "action_1_persistence",
        "supports_return_selected_boundary_prediction",
    ]
    rows = []
    for verdict in verdicts:
        rows.append(
            [
                str(verdict["scenario"]),
                str(verdict["selected_policy"]),
                str(verdict["selected_boundary_policy"]),
                str(verdict["dependency_signature"]),
                f"{float(verdict['selector_reward']):.3f}",
                f"{float(verdict['local_probe_reward']):.3f}",
                f"{float(verdict['action_0_persistence']):.3f}",
                f"{float(verdict['action_1_persistence']):.3f}",
                str(verdict["supports_return_selected_boundary_prediction"]),
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
    results, summary_rows, training_rows, verdicts = run_experiment(cfg)
    summary_path = ARTIFACT_DIR / "return_selected_boundary_probe_summary.csv"
    training_path = ARTIFACT_DIR / "return_selected_boundary_probe_training.csv"
    verdict_path = ARTIFACT_DIR / "return_selected_boundary_probe_verdict.csv"
    results_path = ARTIFACT_DIR / "return_selected_boundary_probe_results.json"
    write_csv(summary_path, summary_rows)
    write_csv(training_path, training_rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "training": [asdict(row) for row in training_rows],
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
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print_table(verdicts)
    return 0 if all(bool(row["supports_return_selected_boundary_prediction"]) for row in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
