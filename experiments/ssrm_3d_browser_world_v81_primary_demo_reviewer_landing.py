"""Report 321: SSRM-3D browser world v81 primary demo reviewer landing.

This report condenses the maintained primary browser demo into an outside-reviewer
landing path that foregrounds the boundary, transcript, integrated loop, receipt,
and observation triage before optional deep panels.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 321
PREFIX = "ssrm_3d_browser_world_v81_primary_demo_reviewer_landing"
DEFAULT_SEED = 20270719

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V61_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening.py"
V61_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
V61_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
V61_CSS = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "styles.css"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local reviewer-landing consolidation only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, "
    "no complete 3D engine, and no finished gameplay claim. The landing path is a review workflow "
    "over public shell state, not proof of inner experience."
)

NEXT_GATE = (
    "post-321: keep the primary shell reviewer-first by making landing-path failures actionable "
    "without hiding the deeper diagnostic panels or weakening the no-consciousness boundary"
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
    css = _read(V61_CSS)
    browser = _load_json(BROWSER_EVIDENCE)
    core_terms = [
        "reviewerLandingOut",
        "runReviewerLandingPass",
        "toggleDeepPanels",
        "formatReviewerLanding",
        "body class=\"reviewer-focus\"",
        "deep-panel",
    ]
    criteria = [
        _criterion(
            "reviewer_landing_panel_present",
            "reviewerLandingOut" in index and "Reviewer landing" in index,
            "maintained shell exposes a reviewer landing panel above the diagnostic grid",
            "outside reviewers would still enter through scattered diagnostic panels",
        ),
        _criterion(
            "default_reviewer_focus",
            "body class=\"reviewer-focus\"" in index and "body.reviewer-focus .deep-panel" in css,
            "primary shell starts in reviewer-focus mode and hides optional deep panels by default",
            "reviewers would see the full debug surface before the core path",
        ),
        _criterion(
            "deep_panels_marked_optional",
            index.count("deep-panel") >= 8 and all(term in index for term in ["Session transcript", "Continuity loop", "Integrated scenario receipt", "Observation triage"]),
            "diagnostic panels are marked optional while transcript, continuity loop, receipt, and triage stay visible",
            "focus mode would either hide core evidence or fail to distinguish optional diagnostics",
        ),
        _criterion(
            "landing_actions_generated",
            all(term in gen for term in core_terms) and all(term in app for term in ["runReviewerLandingPass", "toggleDeepPanels", "formatReviewerLanding"]),
            "reviewer landing actions are generated from the maintained source and present in app.js",
            "regeneration would erase the reviewer-first path",
        ),
        _criterion(
            "browser_landing_pass",
            browser.get("landing_pass") is True,
            str(browser.get("landing_evidence", "missing landing pass evidence")),
            "browser flow did not produce a passable reviewer landing path",
        ),
        _criterion(
            "browser_focus_default",
            browser.get("focus_default_pass") is True,
            str(browser.get("focus_default_evidence", "missing default focus evidence")),
            "browser did not start in reviewer focus mode",
        ),
        _criterion(
            "browser_deep_toggle",
            browser.get("deep_toggle_pass") is True,
            str(browser.get("deep_toggle_evidence", "missing deep toggle evidence")),
            "browser could not reveal optional deep panels on demand",
        ),
        _criterion(
            "browser_core_path_visible",
            browser.get("core_path_visible_pass") is True,
            str(browser.get("core_path_visible_evidence", "missing core path visibility evidence")),
            "boundary, transcript, continuity loop, receipt, and triage were not simultaneously visible",
        ),
        _criterion(
            "browser_resume_persistence",
            browser.get("resume_persistence_pass") is True,
            str(browser.get("resume_persistence_evidence", "missing resume persistence evidence")),
            "reviewer landing evidence did not survive launcher resume",
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
    verdict = "pass" if readiness >= 0.95 and weakest >= 0.9 and all(row.passed for row in criteria) else "needs_browser_evidence"
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "landing_panel_score": next(row.score for row in criteria if row.channel == "reviewer_landing_panel_present"),
        "browser_landing_score": next(row.score for row in criteria if row.channel == "browser_landing_pass"),
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
        "required_terms": core_terms,
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "browser_evidence": browser,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "state": f"artifacts/{PREFIX}_state.json",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v81_primary_demo_reviewer_landing_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 321: SSRM-3D Browser World v81 Primary Demo Reviewer Landing

## Purpose

Report 321 condenses the maintained primary browser demo into an outside-reviewer landing path. The default view now foregrounds boundary, session transcript, continuity-loop status, integrated scenario receipt, and observation triage before optional deep diagnostics.

This is consolidation of the playable review surface, not a new claim about agency or experience.

## Boundary

{results['boundary']}

## What changed

- Added a `Reviewer landing` panel above the primary shell diagnostic grid.
- Started the shell in `reviewer-focus` mode so optional deep panels are hidden by default.
- Added `Run reviewer pass` to execute the continuity loop, generate the scenario receipt, reset observation triage to all, and record the action in transcript/checkpoints.
- Added `Toggle deep panels` so reviewers can reveal trace, checkpoint, resident-history, social-memory, receipt-observation, playtest, and QA-manifest diagnostics without losing the core path.
- Verified the default focus mode, landing pass, optional-panel reveal, core-path visibility, launcher resume, and console cleanliness in browser.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| landing_panel_score | {metrics['landing_panel_score']:.6f} |
| browser_landing_score | {metrics['browser_landing_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- landing_pass: `{browser.get('landing_pass')}`
- focus_default_pass: `{browser.get('focus_default_pass')}`
- deep_toggle_pass: `{browser.get('deep_toggle_pass')}`
- core_path_visible_pass: `{browser.get('core_path_visible_pass')}`
- resume_persistence_pass: `{browser.get('resume_persistence_pass')}`
- console_errors: `{browser.get('console_errors')}`
- landing evidence: `{browser.get('landing_evidence')}`
- focus evidence: `{browser.get('focus_default_evidence')}`
- deep toggle evidence: `{browser.get('deep_toggle_evidence')}`
- core path evidence: `{browser.get('core_path_visible_evidence')}`
- resume evidence: `{browser.get('resume_persistence_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

The result is intentionally modest: it makes the existing primary demo easier for an outside reviewer to enter and audit. It does not claim subjective consciousness, moral status, autonomous language, production readiness, complete gameplay, or a complete 3D engine.

## Next gate

{results['next_gate']}
"""
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v81_primary_demo_reviewer_landing_report.md").write_text(report, encoding="utf-8")


def run(seed: int) -> dict[str, Any]:
    results = _evaluate(seed)
    _write_json(ARTIFACTS / f"{PREFIX}_results.json", results)
    _write_json(
        ARTIFACTS / f"{PREFIX}_state.json",
        {
            "report": REPORT,
            "seed": seed,
            "prefix": PREFIX,
            "boundary": BOUNDARY,
            "next_gate": NEXT_GATE,
            "core_reviewer_path": [
                "boundary",
                "reviewerLandingOut",
                "sessionTranscriptOut",
                "continuityLoopOut",
                "scenarioReceiptOut",
                "observationTriageOut",
            ],
            "optional_deep_panels": [
                "traceOut",
                "checkpointOut",
                "residentHistoryOut",
                "residentDashboardOut",
                "residentActionButtons",
                "trustRepairOut",
                "relationshipMemoryOut",
                "receiptObservationOut",
                "taskList",
                "qaManifestOut",
            ],
        },
    )
    _write_csv(ARTIFACTS / f"{PREFIX}_criteria.csv", results["criteria"])
    _write_csv(ARTIFACTS / f"{PREFIX}_summary.csv", [{**results["metrics"], "report": REPORT, "seed": seed, "verdict": results["verdict"]}])
    _write_csv(ARTIFACTS / f"{PREFIX}_verdict.csv", [{"report": REPORT, "seed": seed, "verdict": results["verdict"], "boundary": BOUNDARY, "next_gate": NEXT_GATE}])
    _write_report(results)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    print(json.dumps({"report": REPORT, "prefix": PREFIX, "verdict": results["verdict"], "metrics": results["metrics"]}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
