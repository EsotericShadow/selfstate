#!/usr/bin/env python3
"""Headless multi-day SSRM-3D maturation verifier.

This benchmark extends the 14.5h long-horizon gate into a 72h accelerated
world. It remains a designed verifier, not a claim of subjective consciousness
or open-ended civilization. The test checks whether a population can develop
slowly for 12h before major shocks, then keep maturing through weather,
disease, resource migration, infrastructure decay, births, teaching, tool
improvement, building tiers, and post-gate shocks.
"""

from __future__ import annotations

import argparse
import json

from ssrm_maturation.benchmark import run_benchmark
from ssrm_maturation.models import Config


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", default="20260901,20260902,20260903,20260904,20260905")
    parser.add_argument("--hours", type=float, default=72.0)
    parser.add_argument("--step-hours", type=float, default=0.10)
    parser.add_argument("--population", type=int, default=14)
    parser.add_argument("--trace-seed", type=int, default=20260901)
    args = parser.parse_args()
    seeds = tuple(int(part.strip()) for part in args.seeds.split(",") if part.strip())
    return Config(
        seeds=seeds,
        hours=args.hours,
        step_hours=args.step_hours,
        population=args.population,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({"verdict": payload["verdict"], "summary": payload["summary"]}, indent=2))
    return 0 if payload["verdict"]["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
