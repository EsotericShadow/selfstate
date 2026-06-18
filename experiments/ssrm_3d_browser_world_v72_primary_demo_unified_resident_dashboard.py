"""Report 312: SSRM-3D browser world v72 primary demo unified resident dashboard.

This report hardens the maintained primary demo with a compact unified resident dashboard.
The dashboard makes schedules, debts, trust, progress, memory, recent-history counts, and
care/resource pressure readable on one surface, instead of requiring raw JSON inspection.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 312
PREFIX = "ssrm_3d_browser_world_v72_primary_demo_unified_resident_dashboard"
DEFAULT_SEED = 20270710

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V61_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening.py"
V61_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
V61_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local unified resident-dashboard hardening only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, no "
    "complete 3D engine, and no finished gameplay claim."
)

NEXT_GATE = (
    "post-312: run a reviewer pass focused on whether the primary demo now communicates schedule/debt/care "
    "state without raw JSON; if readable, the next consolidation should make consequences actionable from "
    "the dashboard rather than add another parallel report organ"
)


@dataclass(frozen=True)
class Criterion:
    channel: str
    passed: bool
    score: float
    evidence: str
    failure_if_false: str


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"missing": str(path)}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"unreadable": str(path), "error": str(exc)}


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_csv(path: Path, rows: list[Any] | list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = [asdict(row) if hasattr(row, "__dataclass_fields__") else dict(row) for row in rows]
    if not normalized:
        path.write_text("", encoding="utf-8")
        return
    fieldnames: list[str] = []
    for row in normalized:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(normalized)


def _criterion(channel: str, passed: bool, evidence: str, failure_if_false: str, partial: float = 0.0) -> Criterion:
    return Criterion(channel, passed, 1.0 if passed else partial, evidence, failure_if_false)


def _evaluate(seed: int) -> dict[str, Any]:
    gen = _read(V61_GEN)
    app = _read(V61_APP)
    index = _read(V61_INDEX)
    browser = _load_json(BROWSER_EVIDENCE)

    criteria = [
        _criterion(
            "dashboard_panel_present",
            "residentDashboardOut" in index and "Resident dashboard" in index,
            "maintained shell exposes a visible Resident dashboard panel",
            "reviewers would still need raw JSON for cross-resident schedule/debt/care state",
        ),
        _criterion(
            "generated_source_of_truth",
            "formatResidentDashboard" in gen and "formatResidentDashboard" in app,
            "dashboard rendering lives in the v61 generator and generated app",
            "regeneration would erase dashboard hardening",
        ),
        _criterion(
            "dashboard_uses_public_state",
            all(term in app for term in ["world.residents", "world.resources", "readResidentHistory"]),
            "dashboard derives from public residents/resources/history state",
            "dashboard could become a parallel hidden-state view",
        ),
        _criterion(
            "dashboard_covers_required_channels",
            all(term in app for term in ["schedule", "progress", "debt", "trust", "memory", "care", "Resources:"]),
            "dashboard covers schedule, progress, debt, trust, memory, and care/resource pressure",
            "the panel would not satisfy the unified schedule/debt/care dashboard gate",
        ),
        _criterion(
            "dashboard_pressure_labels",
            all(term in app for term in ["debt pressure", "trust fragile", "work lagging", "stable"]),
            "dashboard adds simple reviewer-readable pressure labels without changing mechanics",
            "reviewers would still need to infer pressure from raw numbers",
        ),
        _criterion(
            "browser_workflow",
            browser.get("workflow_pass") is True,
            f"browser workflow pass recorded as {browser.get('workflow_pass')}",
            "source checks alone would not prove the dashboard updates in a browser",
        ),
        _criterion(
            "browser_initial_dashboard",
            browser.get("initial_dashboard_pass") is True,
            str(browser.get("initial_dashboard_evidence", "missing initial dashboard evidence")),
            "dashboard would not show all residents and resources on initial load",
        ),
        _criterion(
            "browser_consequence_dashboard",
            browser.get("consequence_dashboard_pass") is True,
            str(browser.get("consequence_dashboard_evidence", "missing consequence dashboard evidence")),
            "dashboard would not reflect borrow/return and history changes",
        ),
        _criterion(
            "browser_offscreen_dashboard",
            browser.get("offscreen_dashboard_pass") is True,
            str(browser.get("offscreen_dashboard_evidence", "missing offscreen dashboard evidence")),
            "dashboard would not reflect offscreen progress/care pressure across residents",
        ),
        _criterion(
            "browser_resume_dashboard",
            browser.get("resume_dashboard_pass") is True,
            str(browser.get("resume_dashboard_evidence", "missing resume dashboard evidence")),
            "dashboard state would not persist through leave/return via primary demo",
        ),
        _criterion(
            "console_clean",
            browser.get("console_errors") == 0,
            f"browser console error count was {browser.get('console_errors')}",
            "browser workflow produced runtime console errors",
        ),
    ]

    scores = [row.score for row in criteria]
    readiness = mean(scores)
    weakest = min(scores)
    verdict = "pass" if readiness >= 0.94 and weakest >= 0.9 and all(row.passed for row in criteria) else "needs_browser_evidence"
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "dashboard_panel_score": next(row.score for row in criteria if row.channel == "dashboard_panel_present"),
        "browser_workflow_score": next(row.score for row in criteria if row.channel == "browser_workflow"),
        "console_errors": browser.get("console_errors", -1),
        "criterion_count": len(criteria),
    }
    return {
        "report": REPORT,
        "prefix": PREFIX,
        "seed": seed,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "verdict": verdict,
        "metrics": metrics,
        "criteria": [asdict(row) for row in criteria],
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "browser_evidence": browser,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "state": f"artifacts/{PREFIX}_state.json",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v72_primary_demo_unified_resident_dashboard_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 312: SSRM-3D Browser World v72 Primary Demo Unified Resident Dashboard

## Purpose

Report 312 continues consolidation of the single playable browser world. Report 311 made resident history readable; this report puts the resident schedule/debt/care state into one reviewer-readable dashboard.

No new simulation organ was added. The dashboard formats existing public resident, resource, and history state.

## Boundary

{results['boundary']}

## What changed

- Added a visible `Resident dashboard` panel to the maintained v61 shell.
- Shows global resources including `care`.
- Shows every resident's schedule, progress, debt, trust, recent history count, pressure label, and memory.
- Uses public `world.residents`, `world.resources`, and resident-history rows only.
- Preserves the existing no-private-workspace/no-subjective-feeling/no-LLM-transcript audit boundary.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| dashboard_panel_score | {metrics['dashboard_panel_score']:.6f} |
| browser_workflow_score | {metrics['browser_workflow_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- workflow_pass: `{browser.get('workflow_pass')}`
- initial_dashboard_pass: `{browser.get('initial_dashboard_pass')}`
- consequence_dashboard_pass: `{browser.get('consequence_dashboard_pass')}`
- offscreen_dashboard_pass: `{browser.get('offscreen_dashboard_pass')}`
- resume_dashboard_pass: `{browser.get('resume_dashboard_pass')}`
- console_errors: `{browser.get('console_errors')}`
- initial evidence: `{browser.get('initial_dashboard_evidence')}`
- consequence evidence: `{browser.get('consequence_dashboard_evidence')}`
- offscreen evidence: `{browser.get('offscreen_dashboard_evidence')}`
- resume evidence: `{browser.get('resume_dashboard_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

This is dashboard/readability consolidation only. It does not imply subjective experience, autonomous language, or finished gameplay.

## Next gate

{results['next_gate']}
"""
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v72_primary_demo_unified_resident_dashboard_report.md").write_text(report, encoding="utf-8")


def run(seed: int) -> dict[str, Any]:
    results = _evaluate(seed)
    _write_json(ARTIFACTS / f"{PREFIX}_results.json", results)
    _write_json(ARTIFACTS / f"{PREFIX}_state.json", {
        "report": REPORT,
        "seed": seed,
        "boundary": BOUNDARY,
        "maintained_shell": "visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html",
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
    })
    _write_csv(ARTIFACTS / f"{PREFIX}_criteria.csv", results["criteria"])
    _write_csv(ARTIFACTS / f"{PREFIX}_summary.csv", [{"metric": key, "value": value} for key, value in results["metrics"].items()])
    _write_csv(ARTIFACTS / f"{PREFIX}_verdict.csv", [{
        "report": REPORT,
        "verdict": results["verdict"],
        "readiness": results["metrics"]["readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "browser_workflow_score": results["metrics"]["browser_workflow_score"],
        "next_gate": NEXT_GATE,
    }])
    _write_report(results)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    print(json.dumps({
        "report": REPORT,
        "verdict": results["verdict"],
        "readiness": results["metrics"]["readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "browser_workflow_score": results["metrics"]["browser_workflow_score"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
