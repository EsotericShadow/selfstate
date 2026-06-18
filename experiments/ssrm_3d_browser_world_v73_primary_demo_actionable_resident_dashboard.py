"""Report 313: SSRM-3D browser world v73 primary demo actionable resident dashboard.

This report hardens the maintained primary demo by making the unified resident dashboard
actionable. It adds per-resident Select/Help/Borrow/Return controls that route through
the existing selected-resident and consequence functions, so dashboard actions update the
same public trust/debt/history loop rather than creating a parallel mechanic.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 313
PREFIX = "ssrm_3d_browser_world_v73_primary_demo_actionable_resident_dashboard"
DEFAULT_SEED = 20270711

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V61_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening.py"
V61_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
V61_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local actionable-dashboard hardening only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, no "
    "complete 3D engine, and no finished gameplay claim."
)

NEXT_GATE = (
    "post-313: use the actionable resident dashboard for a full reviewer pass; if it is usable, the next "
    "consolidation should focus on clearer recoverable-harm/trust-repair scenarios within the same shell"
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
            "dashboard_actions_panel_present",
            "residentActionButtons" in index and "Dashboard actions" in index,
            "maintained shell exposes dashboard action controls",
            "dashboard would remain read-only and force reviewers back to separate controls",
        ),
        _criterion(
            "generated_source_of_truth",
            all(term in gen for term in ["formatResidentActionButtons", "runDashboardResidentAction", "data-dashboard-help"]),
            "actionable dashboard logic lives in the v61 generator",
            "regeneration would erase the actionable dashboard",
        ),
        _criterion(
            "routes_to_existing_mechanics",
            all(term in app for term in ["return offerHelp()", "return borrowTool()", "return returnTool()", "world.selected = name"]),
            "dashboard actions route through existing selected-resident consequence functions",
            "dashboard actions could become parallel mechanics",
        ),
        _criterion(
            "all_action_buttons_rendered",
            all(term in app for term in ["data-dashboard-select", "data-dashboard-help", "data-dashboard-borrow", "data-dashboard-return"]),
            "dashboard renders Select/Help/Borrow/Return for each resident",
            "reviewers would not be able to act from the dashboard across all consequence types",
        ),
        _criterion(
            "browser_workflow",
            browser.get("workflow_pass") is True,
            f"browser workflow pass recorded as {browser.get('workflow_pass')}",
            "source checks alone would not prove the dashboard actions work in a browser",
        ),
        _criterion(
            "browser_select_action",
            browser.get("select_action_pass") is True,
            str(browser.get("select_action_evidence", "missing select action evidence")),
            "dashboard Select would not update selected resident visibly",
        ),
        _criterion(
            "browser_help_action",
            browser.get("help_action_pass") is True,
            str(browser.get("help_action_evidence", "missing help action evidence")),
            "dashboard Help would not affect resident progress/trust/history through the existing loop",
        ),
        _criterion(
            "browser_borrow_return_action",
            browser.get("borrow_return_action_pass") is True,
            str(browser.get("borrow_return_action_evidence", "missing borrow/return action evidence")),
            "dashboard Borrow/Return would not affect debt/trust/history through the existing loop",
        ),
        _criterion(
            "browser_resume_persistence",
            browser.get("resume_action_pass") is True,
            str(browser.get("resume_action_evidence", "missing resume evidence")),
            "dashboard action consequences would not persist through leave/return",
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
        "dashboard_actions_score": next(row.score for row in criteria if row.channel == "dashboard_actions_panel_present"),
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
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v73_primary_demo_actionable_resident_dashboard_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 313: SSRM-3D Browser World v73 Primary Demo Actionable Resident Dashboard

## Purpose

Report 313 keeps consolidating the primary browser demo into one usable surface. Report 312 made schedule/debt/care state readable; this report makes it actionable from the same dashboard.

The new dashboard actions do not create a new mechanic. They route to the existing selected-resident `offerHelp`, `borrowTool`, and `returnTool` functions.

## Boundary

{results['boundary']}

## What changed

- Added a visible `Dashboard actions` panel to the maintained v61 shell.
- Rendered Select/Help/Borrow/Return controls for every resident.
- Routed dashboard actions through existing selected-resident consequence functions.
- Verified dashboard actions update the existing resident dashboard and resident-history lane.
- Verified consequences persist through primary-demo resume.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| dashboard_actions_score | {metrics['dashboard_actions_score']:.6f} |
| browser_workflow_score | {metrics['browser_workflow_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- workflow_pass: `{browser.get('workflow_pass')}`
- select_action_pass: `{browser.get('select_action_pass')}`
- help_action_pass: `{browser.get('help_action_pass')}`
- borrow_return_action_pass: `{browser.get('borrow_return_action_pass')}`
- resume_action_pass: `{browser.get('resume_action_pass')}`
- console_errors: `{browser.get('console_errors')}`
- select evidence: `{browser.get('select_action_evidence')}`
- help evidence: `{browser.get('help_action_evidence')}`
- borrow/return evidence: `{browser.get('borrow_return_action_evidence')}`
- resume evidence: `{browser.get('resume_action_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

This is dashboard/actionability consolidation only. It does not imply subjective experience, autonomous language, or finished gameplay.

## Next gate

{results['next_gate']}
"""
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v73_primary_demo_actionable_resident_dashboard_report.md").write_text(report, encoding="utf-8")


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
