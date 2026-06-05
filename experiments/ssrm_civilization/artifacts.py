"""Artifact helpers for the settlement benchmark."""

from __future__ import annotations

import csv
import json
import statistics
from dataclasses import asdict
from pathlib import Path
from typing import Dict, Iterable, List, Sequence

from .models import EpisodeMetrics, SummaryRow, Trace, VerdictRow


ARTIFACT_DIR = Path("artifacts")


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    data = [asdict(row) for row in rows]
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


def summarize(metrics: Sequence[EpisodeMetrics]) -> List[SummaryRow]:
    by_condition: Dict[str, List[EpisodeMetrics]] = {}
    for row in metrics:
        by_condition.setdefault(row.condition, []).append(row)
    summaries: List[SummaryRow] = []
    for condition, rows in sorted(by_condition.items()):
        summaries.append(
            SummaryRow(
                condition=condition,
                mean_reward=mean(row.reward for row in rows),
                mean_survival_fraction=mean(row.survival_fraction for row in rows),
                mean_infrastructure_score=mean(row.infrastructure_score for row in rows),
                mean_cohesion_score=mean(row.cohesion_score for row in rows),
                mean_resource_score=mean(row.resource_score for row in rows),
                mean_knowledge_score=mean(row.knowledge_score for row in rows),
                mean_civilization_score=mean(row.civilization_score for row in rows),
                mean_building_actions=mean(row.building_actions for row in rows),
                mean_social_actions=mean(row.social_actions for row in rows),
                mean_care_actions=mean(row.care_actions for row in rows),
                mean_teaching_actions=mean(row.teaching_actions for row in rows),
                mean_conflict_events=mean(row.conflict_events for row in rows),
                mean_migration_events=mean(row.migration_events for row in rows),
                mean_casualties=mean(row.casualties for row in rows),
                mean_completed_projects=mean(row.completed_projects for row in rows),
                mean_refusals=mean(row.refusals for row in rows),
            )
        )
    return summaries


def verdict_from_summary(summary: Sequence[SummaryRow]) -> VerdictRow:
    by_name = {row.condition: row for row in summary}
    full = by_name["integrated_settlement_self"].mean_civilization_score
    reactive = by_name["reactive_individuals"].mean_civilization_score
    social = by_name["no_social_memory"].mean_civilization_score
    building = by_name["no_building_memory"].mean_civilization_score
    role = by_name["no_role_memory"].mean_civilization_score
    affect = by_name["no_affective_control"].mean_civilization_score
    norms = by_name["no_norms"].mean_civilization_score
    planning = by_name["no_future_planning"].mean_civilization_score
    losses = {
        "reactive": full - reactive,
        "social": full - social,
        "building": full - building,
        "role": full - role,
        "affect": full - affect,
        "norms": full - norms,
        "planning": full - planning,
    }
    supports = (
        full >= 0.62
        and losses["reactive"] >= 0.12
        and losses["social"] >= 0.035
        and losses["building"] >= 0.055
        and losses["role"] >= 0.025
        and losses["affect"] >= 0.020
        and losses["norms"] >= 0.025
        and losses["planning"] >= 0.035
    )
    return VerdictRow(
        full_condition="integrated_settlement_self",
        full_civilization_score=full,
        reactive_civilization_score=reactive,
        no_social_memory_score=social,
        no_building_memory_score=building,
        no_role_memory_score=role,
        no_affective_control_score=affect,
        no_norms_score=norms,
        no_future_planning_score=planning,
        reactive_loss=losses["reactive"],
        social_memory_loss=losses["social"],
        building_memory_loss=losses["building"],
        role_memory_loss=losses["role"],
        affective_control_loss=losses["affect"],
        norms_loss=losses["norms"],
        future_planning_loss=losses["planning"],
        supports_civilization_pressure_precursor=supports,
        supports_closed_loop_rl=False,
        verdict="pass" if supports else "partial_or_failed",
    )


def write_artifacts(metrics: Sequence[EpisodeMetrics], summary: Sequence[SummaryRow], verdict: VerdictRow, trace: Trace) -> Dict[str, object]:
    payload = {
        "summary": [asdict(row) for row in summary],
        "verdict": asdict(verdict),
        "trace": asdict(trace),
        "notes": {
            "claim": "settlement/civilization pressure precursor",
            "not_claimed": "closed-loop RL, subjective consciousness, or open-ended civilization emergence",
        },
    }
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_civilization_pressure_eval.csv", metrics)
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_civilization_pressure_summary.csv", summary)
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_civilization_pressure_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / "ssrm_3d_civilization_pressure_results.json", payload)
    write_json(ARTIFACT_DIR / "ssrm_3d_civilization_pressure_trace.json", asdict(trace))
    write_js(ARTIFACT_DIR / "ssrm_3d_civilization_pressure_results.js", "SSRM_3D_CIVILIZATION_PRESSURE_RESULTS", payload)
    write_js(ARTIFACT_DIR / "ssrm_3d_civilization_pressure_trace.js", "SSRM_3D_CIVILIZATION_PRESSURE_TRACE", asdict(trace))
    return payload
