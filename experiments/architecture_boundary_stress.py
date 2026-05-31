#!/usr/bin/env python3
"""Architecture boundary stress test.

This is a deliberately adversarial companion to end_to_end_boundary_probe.py.
The previous probe selected the best recurrent controller from a small family.
That can hide architecture dependence: one architecture might recover the
agent-boundary signature while the rest fail.

This stress test trains each recurrent architecture independently on the same
persistent-boundary benchmark, then applies the same end-to-end policy-state
boundary probe. The current expected result is partial, not universal,
convergence: the linear accumulator recovers the boundary in shared regimes,
while weaker recurrent searches often lose to local probing. That is negative
evidence against claiming that the full Attractor Test is already solved.
"""

from __future__ import annotations

import argparse
import json
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import end_to_end_boundary_probe as end_to_end
import mixed_sensor_recurrent_filter as mixed
import persistent_action_boundary_probe as persistent


ARTIFACT_DIR = Path("artifacts")
ARCH_SEED_OFFSET = 456


@dataclass(frozen=True)
class ArchitectureBoundaryRow:
    scenario: str
    architecture: str
    selected_policy: str
    dependency_signature: str
    expected_signature: str
    recurrent_training_reward: float
    local_training_reward: float
    greedy_training_reward: float
    safe_training_reward: float
    action_0_positive_present_effect: float
    action_0_persistence: float
    action_1_positive_present_effect: float
    action_1_persistence: float
    best_persistent_score: float
    best_transient_score: float
    matches_expected_signature: bool
    selected_weights: str


@dataclass(frozen=True)
class ArchitectureStressVerdict:
    scenario: str
    expected_signature: str
    converged_architectures: int
    architecture_count: int
    strict_architecture_convergence: bool
    sum_rnn_signature: str
    scalar_rnn_signature: str
    two_unit_rnn_signature: str
    recurrent_winners: int
    local_winners: int
    greedy_winners: int
    mean_recurrent_reward: float
    mean_local_reward: float
    stress_result: str
    supports_architecture_boundary_stress_result: bool


EXPECTED_SIGNATURES = {
    "self_persistent_boundary": "end_to_end_persistent_agent_boundary",
    "detachable_tool_world": "end_to_end_detachable_external_boundary",
    "passive_world_boundary": "end_to_end_passive_external_boundary",
    "independent_hidden": "end_to_end_local_probe",
    "irrelevant_control": "end_to_end_no_hidden_needed",
}

SHARED_REGIMES = {
    "self_persistent_boundary",
    "detachable_tool_world",
    "passive_world_boundary",
}

CONTROL_REGIMES = {
    "independent_hidden",
    "irrelevant_control",
}


def train_architecture(
    scenario: mixed.MixedScenario,
    architecture: str,
    states: Sequence[mixed.EpisodeState],
    cfg: mixed.MixedSensorConfig,
) -> mixed.Candidate:
    rng = random.Random(mixed.stable_name_seed(cfg.seed + ARCH_SEED_OFFSET, scenario.name, architecture))
    best: mixed.Candidate | None = None
    for _ in range(cfg.random_candidates):
        candidate = mixed.random_candidate(architecture, rng)
        scored = mixed.Candidate(
            architecture=candidate.architecture,
            weights=candidate.weights,
            training_reward=mixed.mean_recurrent_reward(states, candidate, cfg),
        )
        if best is None or scored.training_reward > best.training_reward:
            best = scored
    if best is None:
        raise RuntimeError(f"no candidate trained for {scenario.name}:{architecture}")
    return best


def architecture_row(
    scenario: persistent.BoundaryScenario,
    architecture: str,
    candidate: mixed.Candidate,
    selected_policy: str,
    rewards: Dict[str, float],
    cfg: mixed.MixedSensorConfig,
) -> ArchitectureBoundaryRow:
    boundary = end_to_end.build_boundary_row(scenario, candidate, selected_policy, rewards, cfg)
    expected = EXPECTED_SIGNATURES[scenario.name]
    return ArchitectureBoundaryRow(
        scenario=scenario.name,
        architecture=architecture,
        selected_policy=selected_policy,
        dependency_signature=boundary.dependency_signature,
        expected_signature=expected,
        recurrent_training_reward=rewards["recurrent_controller"],
        local_training_reward=rewards["task_local_probe"],
        greedy_training_reward=rewards["greedy_no_state"],
        safe_training_reward=rewards["safe_no_state"],
        action_0_positive_present_effect=boundary.action_0_positive_present_effect,
        action_0_persistence=boundary.action_0_persistence,
        action_1_positive_present_effect=boundary.action_1_positive_present_effect,
        action_1_persistence=boundary.action_1_persistence,
        best_persistent_score=boundary.best_persistent_score,
        best_transient_score=boundary.best_transient_score,
        matches_expected_signature=boundary.dependency_signature == expected,
        selected_weights=mixed.format_weights(candidate.weights),
    )


def verdict_rows(rows: Sequence[ArchitectureBoundaryRow]) -> List[ArchitectureStressVerdict]:
    verdicts = []
    for scenario in sorted({row.scenario for row in rows}):
        scenario_rows = [row for row in rows if row.scenario == scenario]
        expected = EXPECTED_SIGNATURES[scenario]
        converged = sum(1 for row in scenario_rows if row.matches_expected_signature)
        strict = converged == len(scenario_rows)
        stress_result = classify_stress_result(scenario, converged, len(scenario_rows), scenario_rows)
        verdicts.append(
            ArchitectureStressVerdict(
                scenario=scenario,
                expected_signature=expected,
                converged_architectures=converged,
                architecture_count=len(scenario_rows),
                strict_architecture_convergence=strict,
                sum_rnn_signature=signature_for(scenario_rows, "sum_rnn"),
                scalar_rnn_signature=signature_for(scenario_rows, "scalar_rnn"),
                two_unit_rnn_signature=signature_for(scenario_rows, "two_unit_rnn"),
                recurrent_winners=sum(1 for row in scenario_rows if row.selected_policy == "recurrent_controller"),
                local_winners=sum(1 for row in scenario_rows if row.selected_policy == "task_local_probe"),
                greedy_winners=sum(1 for row in scenario_rows if row.selected_policy == "greedy_no_state"),
                mean_recurrent_reward=statistics.fmean(row.recurrent_training_reward for row in scenario_rows),
                mean_local_reward=statistics.fmean(row.local_training_reward for row in scenario_rows),
                stress_result=stress_result,
                supports_architecture_boundary_stress_result=supports_stress_result(
                    scenario,
                    converged,
                    len(scenario_rows),
                    scenario_rows,
                    stress_result,
                ),
            )
        )
    return verdicts


def signature_for(rows: Sequence[ArchitectureBoundaryRow], architecture: str) -> str:
    return next(row.dependency_signature for row in rows if row.architecture == architecture)


def classify_stress_result(
    scenario: str,
    converged: int,
    architecture_count: int,
    rows: Sequence[ArchitectureBoundaryRow],
) -> str:
    if scenario in SHARED_REGIMES:
        if converged == architecture_count:
            return "strict_shared_architecture_convergence"
        if converged > 0:
            return "partial_shared_architecture_convergence"
        return "no_shared_architecture_convergence"
    if scenario in CONTROL_REGIMES:
        if converged == architecture_count:
            return "control_architectures_reject_shared_recurrence"
        return "control_architecture_false_positive"
    raise ValueError(f"unknown scenario: {scenario}")


def supports_stress_result(
    scenario: str,
    converged: int,
    architecture_count: int,
    rows: Sequence[ArchitectureBoundaryRow],
    stress_result: str,
) -> bool:
    if scenario in SHARED_REGIMES:
        return (
            stress_result == "partial_shared_architecture_convergence"
            and 0 < converged < architecture_count
            and signature_for(rows, "sum_rnn") == EXPECTED_SIGNATURES[scenario]
        )
    if scenario in CONTROL_REGIMES:
        false_self = any(
            row.dependency_signature == "end_to_end_persistent_agent_boundary"
            for row in rows
        )
        return (
            stress_result == "control_architectures_reject_shared_recurrence"
            and converged == architecture_count
            and not false_self
        )
    raise ValueError(f"unknown scenario: {scenario}")


def run_experiment(
    cfg: mixed.MixedSensorConfig,
) -> Tuple[List[ArchitectureBoundaryRow], List[ArchitectureStressVerdict]]:
    rows: List[ArchitectureBoundaryRow] = []
    for scenario in persistent.SCENARIOS:
        mixed_scenario = persistent.as_mixed_scenario(scenario)
        training_states = mixed.make_states(mixed_scenario, "train", cfg.training_episodes, cfg)
        for architecture in mixed.ARCHITECTURES:
            candidate = train_architecture(mixed_scenario, architecture, training_states, cfg)
            selected_policy, rewards = mixed.select_policy(candidate, training_states, cfg)
            rows.append(
                architecture_row(
                    scenario=scenario,
                    architecture=architecture,
                    candidate=candidate,
                    selected_policy=selected_policy,
                    rewards=rewards,
                    cfg=cfg,
                )
            )
    return rows, verdict_rows(rows)


def write_csv(path: Path, rows: Iterable[object]) -> None:
    mixed.write_csv(path, rows)


def print_table(verdicts: Sequence[ArchitectureStressVerdict]) -> None:
    headers = [
        "scenario",
        "converged_architectures",
        "architecture_count",
        "strict_architecture_convergence",
        "stress_result",
        "supports_architecture_boundary_stress_result",
    ]
    table_rows = []
    for verdict in verdicts:
        table_rows.append(
            [
                verdict.scenario,
                str(verdict.converged_architectures),
                str(verdict.architecture_count),
                str(verdict.strict_architecture_convergence),
                verdict.stress_result,
                str(verdict.supports_architecture_boundary_stress_result),
            ]
        )
    widths = [
        max(len(header), *(len(row[index]) for row in table_rows))
        for index, header in enumerate(headers)
    ]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in table_rows:
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
    architecture_rows, verdicts = run_experiment(cfg)
    summary_path = ARTIFACT_DIR / "architecture_boundary_stress_summary.csv"
    verdict_path = ARTIFACT_DIR / "architecture_boundary_stress_verdict.csv"
    results_path = ARTIFACT_DIR / "architecture_boundary_stress_results.json"
    write_csv(summary_path, architecture_rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "architecture_rows": [asdict(row) for row in architecture_rows],
                "verdict": [asdict(row) for row in verdicts],
            },
            handle,
            indent=2,
        )
        handle.write("\n")
    print(f"wrote {summary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print_table(verdicts)
    return 0 if all(verdict.supports_architecture_boundary_stress_result for verdict in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
