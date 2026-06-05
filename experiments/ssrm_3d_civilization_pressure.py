#!/usr/bin/env python3
"""SSRM-3D settlement/civilization pressure precursor.

This report addresses the visible limitation of the first physics benchmark:
one agent can loop between water and shelter. This experiment adds a separate
multi-agent settlement layer with shared infrastructure, role memory, social
memory, norms, emotion-like control summaries, and future planning.

It is still a designed precursor. It does not claim open-ended civilization,
subjective consciousness, or closed-loop deep RL.
"""

from __future__ import annotations

import argparse
from dataclasses import asdict
from typing import List

from ssrm_civilization.artifacts import summarize, verdict_from_summary, write_artifacts
from ssrm_civilization.models import CivilizationConfig, EpisodeMetrics, Trace
from ssrm_civilization.simulation import run_episode
from ssrm_civilization.world import POLICIES, SCENARIOS


def run_benchmark(cfg: CivilizationConfig) -> dict[str, object]:
    metrics: List[EpisodeMetrics] = []
    trace: Trace | None = None
    for scenario in SCENARIOS:
        for policy in POLICIES:
            for episode in range(cfg.eval_episodes):
                want_trace = (
                    scenario.name == "storm_illness_settlement"
                    and policy.name == "integrated_settlement_self"
                    and episode == cfg.trace_episode
                )
                row, maybe_trace = run_episode(cfg, scenario, policy, episode, trace=want_trace)
                metrics.append(row)
                if maybe_trace is not None:
                    trace = maybe_trace
    if trace is None:
        raise RuntimeError("trace was not generated")
    summary = summarize(metrics)
    verdict = verdict_from_summary(summary)
    payload = write_artifacts(metrics, summary, verdict, trace)
    return {
        "config": asdict(cfg),
        "verdict": asdict(verdict),
        "summary": [asdict(row) for row in summary],
        "artifact_notes": payload["notes"],
    }


def parse_args() -> CivilizationConfig:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=20260706)
    parser.add_argument("--ticks", type=int, default=96)
    parser.add_argument("--eval-episodes", type=int, default=48)
    parser.add_argument("--trace-episode", type=int, default=3)
    args = parser.parse_args()
    return CivilizationConfig(
        seed=args.seed,
        ticks=args.ticks,
        eval_episodes=args.eval_episodes,
        trace_episode=args.trace_episode,
    )


def main() -> None:
    cfg = parse_args()
    result = run_benchmark(cfg)
    import json

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
