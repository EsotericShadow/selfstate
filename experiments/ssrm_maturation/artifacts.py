"""Artifact writers for multi-day maturation runs."""

from __future__ import annotations

import csv
import json
from dataclasses import asdict
from pathlib import Path
from typing import Sequence

from .models import Config, EpisodeRow, SummaryRow, Trace, VerdictRow


ROOT = Path(__file__).resolve().parents[2]
ARTIFACT_DIR = ROOT / "artifacts"


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = [asdict(row) for row in rows]
    if not data:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(data[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def write_js(path: Path, variable: str, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"window.{variable} = {json.dumps(payload, indent=2)};\n", encoding="utf-8")


def write_artifacts(rows: Sequence[EpisodeRow], summary: Sequence[SummaryRow], verdict: VerdictRow, trace: Trace, cfg: Config) -> dict[str, object]:
    payload = {
        "config": {
            "seeds": list(cfg.seeds),
            "hours": cfg.hours,
            "step_hours": cfg.step_hours,
            "population": cfg.population,
            "trace_seed": cfg.trace_seed,
        },
        "summary": [asdict(row) for row in summary],
        "verdict": asdict(verdict),
        "trace": asdict(trace),
        "notes": {
            "claim": "designed multi-day maturation pressure verifier",
            "not_claimed": "subjective consciousness, unconstrained open-ended civilization, or trained deep RL policy",
        },
    }
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_multiday_maturation_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_multiday_maturation_summary.csv", summary)
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_multiday_maturation_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / "ssrm_3d_multiday_maturation_results.json", payload)
    write_json(ARTIFACT_DIR / "ssrm_3d_multiday_maturation_trace.json", asdict(trace))
    write_js(ARTIFACT_DIR / "ssrm_3d_multiday_maturation_results.js", "SSRM_3D_MULTIDAY_MATURATION_RESULTS", payload)
    write_js(ARTIFACT_DIR / "ssrm_3d_multiday_maturation_trace.js", "SSRM_3D_MULTIDAY_MATURATION_TRACE", asdict(trace))
    return payload
