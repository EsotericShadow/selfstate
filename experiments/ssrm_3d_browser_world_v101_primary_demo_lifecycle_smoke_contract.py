"""Report 341: SSRM-3D Browser World v101 primary-demo lifecycle smoke contract.

This module consolidates the browser handoff lifecycle evidence from Reports 335-340
into one deterministic smoke contract. It does not add another browser behavior
variant; it defines the maintained lifecycle surface future handoff changes should
exercise.
"""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 341
SEED = 20270739
PREFIX = "ssrm_3d_browser_world_v101_primary_demo_lifecycle_smoke_contract"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"


@dataclass(frozen=True)
class InputReport:
    report: int
    phase: str
    path: Path
    required_metrics: tuple[str, ...]
    role: str


INPUT_REPORTS: tuple[InputReport, ...] = (
    InputReport(
        335,
        "cross_tab_prepared_resume_visible",
        ARTIFACTS / "ssrm_3d_browser_world_v95_primary_demo_cross_tab_handoff_continuity_bridge_results.json",
        ("readiness", "weakest_channel_score"),
        "fresh prepared handoff can be resumed from a second tab",
    ),
    InputReport(
        336,
        "closed_origin_tab_continuity",
        ARTIFACTS / "ssrm_3d_browser_world_v96_primary_demo_closed_origin_tab_handoff_continuity_bridge_results.json",
        ("readiness", "weakest_channel_score"),
        "closed origin tab does not strand the prepared handoff",
    ),
    InputReport(
        337,
        "hard_reload_continuity",
        ARTIFACTS / "ssrm_3d_browser_world_v97_primary_demo_closed_origin_tab_hard_reload_handoff_continuity_bridge_results.json",
        ("readiness", "weakest_channel_score"),
        "hard reload keeps the closed-origin handoff visible and usable",
    ),
    InputReport(
        338,
        "stale_supersession_calibration",
        ARTIFACTS / "ssrm_3d_browser_world_v98_primary_demo_stale_prepared_handoff_calibration_bridge_results.json",
        ("readiness", "weakest_channel_score"),
        "stale prepared handoff is recognized as stale instead of blindly trusted",
    ),
    InputReport(
        339,
        "stale_reprepare_repair",
        ARTIFACTS / "ssrm_3d_browser_world_v99_primary_demo_stale_handoff_repair_reprepare_bridge_results.json",
        ("readiness", "weakest_channel_score"),
        "stale mismatch can be repaired by re-preparing a clean handoff",
    ),
    InputReport(
        340,
        "repaired_continue_return_refresh",
        ARTIFACTS / "ssrm_3d_browser_world_v100_primary_demo_repaired_handoff_continue_return_freshness_bridge_results.json",
        ("readiness", "weakest_channel_score", "repaired_continue_return_score", "post_return_freshness_score"),
        "repaired clean handoff remains fresh after continue, reviewer pass, return, refresh, and reload",
    ),
)

SOURCE_EXPECTATIONS: dict[Path, tuple[str, ...]] = {
    ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/demo.js": (
        "handoffPayloadFreshnessState",
        "renderOutsideReviewHandoffActions",
        "preparedHandoffHref",
        "readableHandoffSummary",
        "outsideReviewHandoffStatus",
    ),
    ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/index.html": (
        "outsideReviewHandoffStatus",
        "outsideReviewHandoffActions",
    ),
    ROOT / "experiments/ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py": (
        "outsideReviewHandoffStatus",
        "outsideReviewHandoffActions",
    ),
}

BOUNDARIES = (
    "browser-local lifecycle contract only",
    "no LLM calls",
    "no subjective-consciousness claim",
    "no moral-patienthood claim",
    "no production persistence claim",
    "no complete 3D engine claim",
    "no finished gameplay claim",
)

NEXT_GATE = (
    "post-341: replace one-off lifecycle report generation with a single reusable "
    "primary-demo lifecycle smoke runner whenever future handoff changes are made"
)


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _metric(data: dict[str, Any], name: str, default: float = 0.0) -> float:
    metrics = data.get("metrics", {})
    value = metrics.get(name, default)
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _console_errors(data: dict[str, Any]) -> int:
    metrics = data.get("metrics", {})
    for key in ("console_errors", "browser_console_errors", "console_error_count"):
        if key in metrics:
            try:
                return int(metrics[key])
            except (TypeError, ValueError):
                return 0
    return 0


def _input_phase_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for spec in INPUT_REPORTS:
        exists = spec.path.exists()
        data = _load_json(spec.path) if exists else {}
        metric_values = {name: _metric(data, name) for name in spec.required_metrics}
        rows.append(
            {
                "report": spec.report,
                "phase": spec.phase,
                "role": spec.role,
                "artifact": str(spec.path.relative_to(ROOT)),
                "exists": exists,
                "verdict": data.get("verdict", "missing"),
                "passed": exists and data.get("verdict") == "pass",
                "weakest_channel_score": _metric(data, "weakest_channel_score"),
                "readiness": _metric(data, "readiness"),
                "console_errors": _console_errors(data),
                "required_metric_min": min(metric_values.values()) if metric_values else 0.0,
                "required_metrics": metric_values,
            }
        )
    return rows


def _source_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path, terms in SOURCE_EXPECTATIONS.items():
        exists = path.exists()
        text = path.read_text(encoding="utf-8") if exists else ""
        present = {term: (term in text) for term in terms}
        rows.append(
            {
                "path": str(path.relative_to(ROOT)),
                "exists": exists,
                "required_terms": present,
                "passed": exists and all(present.values()),
            }
        )
    return rows


def _criterion(name: str, passed: bool, detail: str, channel: str) -> dict[str, Any]:
    return {
        "name": name,
        "passed": bool(passed),
        "score": 1.0 if passed else 0.0,
        "channel": channel,
        "detail": detail,
    }


def build_results() -> dict[str, Any]:
    phase_rows = _input_phase_rows()
    source_rows = _source_rows()
    phase_by_report = {row["report"]: row for row in phase_rows}
    phase_names = {row["phase"] for row in phase_rows if row["passed"]}

    console_total = sum(int(row["console_errors"]) for row in phase_rows)
    input_pass_rate = mean(1.0 if row["passed"] else 0.0 for row in phase_rows)
    input_weakest_min = min(float(row["weakest_channel_score"]) for row in phase_rows)
    input_required_metric_min = min(float(row["required_metric_min"]) for row in phase_rows)
    source_pass_rate = mean(1.0 if row["passed"] else 0.0 for row in source_rows)

    required_phases = {spec.phase for spec in INPUT_REPORTS}
    fresh_phases = {
        "cross_tab_prepared_resume_visible",
        "closed_origin_tab_continuity",
        "hard_reload_continuity",
    }
    stale_phases = {"stale_supersession_calibration", "stale_reprepare_repair"}
    post_repair_phases = {"repaired_continue_return_refresh"}

    contract = {
        "name": "primary_demo_handoff_lifecycle_smoke_contract",
        "report": REPORT,
        "seed": SEED,
        "scope": "single maintained smoke surface for future primary-demo handoff lifecycle changes",
        "phases": [
            {
                "phase": row["phase"],
                "source_report": row["report"],
                "role": row["role"],
                "artifact": row["artifact"],
                "passed": row["passed"],
                "required_metric_min": row["required_metric_min"],
            }
            for row in phase_rows
        ],
        "future_smoke_requirements": [
            "prepare a clean handoff in the primary launcher",
            "resume from a separate context without relying on hidden storage",
            "survive closed-origin and hard-reload continuity checks",
            "detect stale prepared handoffs as stale, not fresh",
            "repair stale handoffs by re-preparing a clean payload",
            "use the repaired continue path, return to launcher, refresh evidence, and reload",
            "preserve visible status, continue/download controls, timestamp freshness, and console cleanliness",
        ],
        "boundaries": BOUNDARIES,
    }

    criteria = [
        _criterion(
            "report_335_cross_tab_continuity_passed",
            phase_by_report[335]["passed"],
            "Report 335 fresh cross-tab prepared-resume evidence is present and passing.",
            "fresh continuity",
        ),
        _criterion(
            "report_336_closed_origin_tab_continuity_passed",
            phase_by_report[336]["passed"],
            "Report 336 closed-origin-tab continuity evidence is present and passing.",
            "fresh continuity",
        ),
        _criterion(
            "report_337_hard_reload_continuity_passed",
            phase_by_report[337]["passed"],
            "Report 337 hard-reload continuity evidence is present and passing.",
            "fresh continuity",
        ),
        _criterion(
            "report_338_stale_calibration_passed",
            phase_by_report[338]["passed"],
            "Report 338 stale-handoff calibration evidence is present and passing.",
            "stale calibration",
        ),
        _criterion(
            "report_339_stale_repair_passed",
            phase_by_report[339]["passed"],
            "Report 339 stale-handoff repair evidence is present and passing.",
            "repair path",
        ),
        _criterion(
            "report_340_repaired_continue_return_passed",
            phase_by_report[340]["passed"],
            "Report 340 repaired continue-return freshness evidence is present and passing.",
            "post-repair use",
        ),
        _criterion(
            "all_inputs_browser_console_clean",
            console_total == 0,
            f"Aggregated browser console errors across input reports: {console_total}.",
            "runtime hygiene",
        ),
        _criterion(
            "all_inputs_weakest_channel_full",
            input_weakest_min >= 1.0,
            f"Minimum input weakest-channel score is {input_weakest_min:.3f}.",
            "evidence quality",
        ),
        _criterion(
            "all_required_metrics_full",
            input_required_metric_min >= 1.0,
            f"Minimum required metric across lifecycle sources is {input_required_metric_min:.3f}.",
            "evidence quality",
        ),
        _criterion(
            "continuity_contract_covers_fresh_path",
            fresh_phases.issubset(phase_names),
            "Fresh continuity path covers cross-tab, closed-origin, and hard-reload phases.",
            "contract coverage",
        ),
        _criterion(
            "continuity_contract_covers_stale_path",
            stale_phases.issubset(phase_names),
            "Stale lifecycle path covers stale calibration and clean reprepare repair.",
            "contract coverage",
        ),
        _criterion(
            "continuity_contract_covers_repair_path",
            "stale_reprepare_repair" in phase_names,
            "Repair path includes re-preparing a clean payload after stale mismatch detection.",
            "contract coverage",
        ),
        _criterion(
            "continuity_contract_covers_post_repair_use",
            post_repair_phases.issubset(phase_names),
            "Post-repair path includes actual continue, return, refresh, and reload use.",
            "contract coverage",
        ),
        _criterion(
            "contract_has_single_future_smoke_surface",
            required_phases == phase_names,
            "The contract defines one complete lifecycle surface instead of one-off future variants.",
            "maintainability",
        ),
        _criterion(
            "source_preserves_primary_demo_controls",
            all(row["passed"] for row in source_rows),
            "Primary demo source still exposes the handoff status/action controls required by the contract.",
            "source binding",
        ),
        _criterion(
            "boundary_preserved",
            all("claim" in boundary or "browser-local" in boundary or "no LLM" in boundary for boundary in BOUNDARIES),
            "The contract states browser-local/no-consciousness/no-production-persistence boundaries.",
            "claim hygiene",
        ),
    ]

    weakest_channel_score = min(item["score"] for item in criteria)
    lifecycle_coverage_score = mean(
        item["score"]
        for item in criteria
        if item["channel"] in {"fresh continuity", "stale calibration", "repair path", "post-repair use", "contract coverage"}
    )
    stale_repair_coverage_score = mean(
        item["score"]
        for item in criteria
        if item["channel"] in {"stale calibration", "repair path", "post-repair use"}
    )
    readiness = mean(item["score"] for item in criteria)

    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest_channel_score,
        "lifecycle_coverage_score": lifecycle_coverage_score,
        "stale_repair_coverage_score": stale_repair_coverage_score,
        "post_repair_use_score": phase_by_report[340]["required_metric_min"],
        "input_report_pass_rate": input_pass_rate,
        "input_weakest_channel_min": input_weakest_min,
        "input_required_metric_min": input_required_metric_min,
        "source_binding_score": source_pass_rate,
        "console_errors_total": console_total,
        "criterion_count": len(criteria),
    }

    verdict = "pass" if weakest_channel_score >= 1.0 else "fail"

    return {
        "report": REPORT,
        "seed": SEED,
        "prefix": PREFIX,
        "verdict": verdict,
        "metrics": metrics,
        "criteria": criteria,
        "input_reports": phase_rows,
        "source_bindings": source_rows,
        "contract": contract,
        "boundaries": BOUNDARIES,
        "next_gate": NEXT_GATE,
    }


def _write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    criteria = results["criteria"]
    inputs = results["input_reports"]
    report_path = DOCS / f"{REPORT}_{PREFIX}_report.md"

    criterion_lines = "\n".join(
        f"- {'PASS' if item['passed'] else 'FAIL'} `{item['name']}` ({item['channel']}): {item['detail']}"
        for item in criteria
    )
    phase_lines = "\n".join(
        f"- Report {row['report']} `{row['phase']}`: {row['role']} -> {row['verdict']} "
        f"(weakest {float(row['weakest_channel_score']):.3f}, required min {float(row['required_metric_min']):.3f})"
        for row in inputs
    )
    boundary_lines = "\n".join(f"- {boundary}" for boundary in results["boundaries"])

    report_path.write_text(
        f"# Report {REPORT}: SSRM-3D Browser World v101 Primary Demo Lifecycle Smoke Contract\n\n"
        "## Purpose\n\n"
        "Report 341 consolidates the repeated primary-demo handoff lifecycle checks from Reports 335 through 340 into one deterministic smoke contract. "
        "This is intentionally not another near-duplicate browser variant. It is the maintained contract future handoff changes should satisfy before new report-specific lifecycle branches are added.\n\n"
        "## What changed\n\n"
        "- Added a deterministic lifecycle contract generator for the primary demo handoff path.\n"
        "- Aggregated fresh continuity, closed-origin continuity, hard-reload continuity, stale calibration, stale repair, and repaired continue-return freshness evidence.\n"
        "- Bound the future smoke surface to visible handoff controls, freshness status, continue/download affordances, shell evidence refresh, and console cleanliness.\n"
        "- Preserved the claim boundary: browser-local lifecycle hygiene only, with no subjective-consciousness, moral-patienthood, production-persistence, or finished-gameplay claim.\n\n"
        "## Lifecycle phases\n\n"
        f"{phase_lines}\n\n"
        "## Metrics\n\n"
        f"- verdict: `{results['verdict']}`\n"
        f"- readiness: `{metrics['readiness']:.3f}`\n"
        f"- weakest_channel_score: `{metrics['weakest_channel_score']:.3f}`\n"
        f"- lifecycle_coverage_score: `{metrics['lifecycle_coverage_score']:.3f}`\n"
        f"- stale_repair_coverage_score: `{metrics['stale_repair_coverage_score']:.3f}`\n"
        f"- post_repair_use_score: `{metrics['post_repair_use_score']:.3f}`\n"
        f"- input_report_pass_rate: `{metrics['input_report_pass_rate']:.3f}`\n"
        f"- input_weakest_channel_min: `{metrics['input_weakest_channel_min']:.3f}`\n"
        f"- source_binding_score: `{metrics['source_binding_score']:.3f}`\n"
        f"- console_errors_total: `{metrics['console_errors_total']}`\n"
        f"- criterion_count: `{metrics['criterion_count']}`\n\n"
        "## Criteria\n\n"
        f"{criterion_lines}\n\n"
        "## Contract boundary\n\n"
        f"{boundary_lines}\n\n"
        "## Interpretation\n\n"
        "The result says the primary demo has one coherent handoff lifecycle contract spanning fresh, stale, repaired, and post-repair use paths. "
        "It does not say the browser world is a finished product. The useful shift is maintenance discipline: future handoff work should run the lifecycle contract instead of adding another isolated report for every tab, reload, or return variant.\n\n"
        "## Next gate\n\n"
        f"{results['next_gate']}\n",
        encoding="utf-8",
    )


def write_artifacts(results: dict[str, Any]) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    DOCS.mkdir(exist_ok=True)

    (ARTIFACTS / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACTS / f"{PREFIX}_state.json").write_text(
        json.dumps(
            {
                "report": REPORT,
                "seed": SEED,
                "verdict": results["verdict"],
                "metrics": results["metrics"],
                "input_reports": results["input_reports"],
                "source_bindings": results["source_bindings"],
                "next_gate": results["next_gate"],
            },
            indent=2,
            sort_keys=True,
        ),
        encoding="utf-8",
    )
    (ARTIFACTS / f"{PREFIX}_contract.json").write_text(json.dumps(results["contract"], indent=2, sort_keys=True), encoding="utf-8")

    _write_csv(
        ARTIFACTS / f"{PREFIX}_summary.csv",
        [
            {
                "report": REPORT,
                "seed": SEED,
                "verdict": results["verdict"],
                **results["metrics"],
            }
        ],
        ["report", "seed", "verdict", *results["metrics"].keys()],
    )
    _write_csv(
        ARTIFACTS / f"{PREFIX}_verdict.csv",
        [
            {
                "report": REPORT,
                "verdict": results["verdict"],
                "weakest_channel_score": results["metrics"]["weakest_channel_score"],
                "next_gate": results["next_gate"],
            }
        ],
        ["report", "verdict", "weakest_channel_score", "next_gate"],
    )
    _write_csv(
        ARTIFACTS / f"{PREFIX}_criteria.csv",
        results["criteria"],
        ["name", "passed", "score", "channel", "detail"],
    )
    _write_report(results)


def main() -> dict[str, Any]:
    results = build_results()
    write_artifacts(results)
    print(json.dumps({"report": REPORT, "verdict": results["verdict"], "metrics": results["metrics"]}, indent=2, sort_keys=True))
    return results


if __name__ == "__main__":
    main()
