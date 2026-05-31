#!/usr/bin/env python3
"""Unseeded recurrent noisy-observation filter precursor.

This is a stricter companion to recurrent_observation_filter.py. It uses the
same recurrent policy families and matched controls, but removes seeded
accumulator candidates. Candidate controllers are sampled randomly and selected
only by training return.

Prediction:

- random-start recurrent search should still find an agent-channel filter when
  channel A tracks persistent agent-state;
- it should find a world-channel filter when channel B tracks external state;
- it should choose local probing or greedy no-state behavior in matched
  controls where shared recurrent state is not useful.
"""

from __future__ import annotations

import argparse
import json
import random
from dataclasses import asdict
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

import recurrent_observation_filter as recurrent


ARTIFACT_DIR = Path("artifacts")


def train_unseeded_recurrent(
    scenario: recurrent.RecurrentScenario,
    states: Sequence[recurrent.EpisodeState],
    cfg: recurrent.RecurrentFilterConfig,
) -> recurrent.RecurrentCandidate:
    candidates = []
    for architecture in recurrent.ARCHITECTURES:
        rng = random.Random(recurrent.stable_name_seed(cfg.seed + 99, scenario.name, architecture))
        for _ in range(cfg.random_candidates):
            candidate = recurrent.random_candidate(architecture, rng)
            candidates.append(
                recurrent.RecurrentCandidate(
                    architecture=candidate.architecture,
                    weights=candidate.weights,
                    training_reward=recurrent.mean_recurrent_reward(states, candidate, cfg),
                )
            )
    return max(candidates, key=lambda candidate: candidate.training_reward)


def run_experiment(
    cfg: recurrent.RecurrentFilterConfig,
) -> Tuple[
    List[recurrent.AgentResult],
    List[Dict[str, object]],
    List[recurrent.TrainingRow],
    List[Dict[str, object]],
    List[Dict[str, object]],
]:
    results = []
    training_rows = []
    dependency_rows = []
    for scenario in recurrent.SCENARIOS:
        training_states = recurrent.make_states(scenario, "train", cfg.training_episodes, cfg)
        candidate = train_unseeded_recurrent(scenario, training_states, cfg)
        selected_policy, rewards = recurrent.select_policy(candidate, training_states, cfg)
        signature, dependency = recurrent.dependency_signature(scenario, candidate, cfg)
        training_rows.append(
            recurrent.TrainingRow(
                scenario=scenario.name,
                selected_policy=selected_policy,
                selected_architecture=candidate.architecture,
                recurrent_training_reward=rewards["recurrent_controller"],
                local_training_reward=rewards["task_local_probe"],
                greedy_training_reward=rewards["greedy_no_state"],
                safe_training_reward=rewards["safe_no_state"],
                selected_weights=recurrent.format_weights(candidate.weights),
            )
        )
        dependency_rows.append({"scenario": scenario.name, "dependency_signature": signature, **dependency})
        test_states = recurrent.make_states(scenario, "test", cfg.episodes, cfg)
        for state in test_states:
            for agent in recurrent.AGENTS:
                results.append(
                    recurrent.run_agent(
                        scenario,
                        state,
                        agent,
                        selected_policy,
                        candidate,
                        signature,
                        cfg,
                    )
                )
    summary_rows = recurrent.summarize(results)
    verdicts = recurrent.verdict_rows(summary_rows, training_rows, dependency_rows)
    return results, summary_rows, training_rows, dependency_rows, verdicts


def parse_args() -> recurrent.RecurrentFilterConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=500)
    parser.add_argument("--training-episodes", type=int, default=800)
    parser.add_argument("--seed", type=int, default=20260603)
    parser.add_argument("--horizon", type=int, default=8)
    parser.add_argument("--evidence-samples", type=int, default=9)
    parser.add_argument("--cue-accuracy", type=float, default=0.85)
    parser.add_argument("--shared-cue-cost", type=float, default=1.0)
    parser.add_argument("--local-probe-cost", type=float, default=1.0)
    parser.add_argument("--random-candidates", type=int, default=1500)
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
    return recurrent.RecurrentFilterConfig(
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
    results, summary_rows, training_rows, dependency_rows, verdicts = run_experiment(cfg)
    summary_path = ARTIFACT_DIR / "unseeded_recurrent_filter_summary.csv"
    training_path = ARTIFACT_DIR / "unseeded_recurrent_filter_training.csv"
    dependency_path = ARTIFACT_DIR / "unseeded_recurrent_filter_dependency.csv"
    verdict_path = ARTIFACT_DIR / "unseeded_recurrent_filter_verdict.csv"
    results_path = ARTIFACT_DIR / "unseeded_recurrent_filter_results.json"
    recurrent.write_csv(summary_path, summary_rows)
    recurrent.write_csv(training_path, training_rows)
    recurrent.write_csv(dependency_path, dependency_rows)
    recurrent.write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "training": [asdict(row) for row in training_rows],
                "dependency": dependency_rows,
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
    print(f"wrote {dependency_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    recurrent.print_table(verdicts)
    return 0 if all(bool(row["supports_recurrent_filter_prediction"]) for row in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
