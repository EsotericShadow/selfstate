"""Report 311: SSRM-3D browser world v71 primary demo resident history lane.

This report hardens the maintained primary demo by adding a compact resident-history
lane. The lane shows public trust/debt/progress/memory continuity per resident, derived
from browser-local interaction state, so reviewers can see resident continuity without
parsing raw world JSON.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 311
PREFIX = "ssrm_3d_browser_world_v71_primary_demo_resident_history_lane"
DEFAULT_SEED = 20270709

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V61_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening.py"
V61_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
V61_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local resident-history readability hardening only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, no "
    "complete 3D engine, and no finished gameplay claim."
)

NEXT_GATE = (
    "post-311: run another primary-demo pass focused on leave/return continuity across selected residents; "
    "if the resident lane is readable, the next consolidation should improve the unified schedule/debt/care "
    "dashboard rather than add a separate world organ"
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
            "resident_history_panel_present",
            "residentHistoryOut" in index and "Resident history" in index,
            "maintained shell exposes a visible Resident history panel",
            "reviewers would still need raw trace JSON for resident continuity",
        ),
        _criterion(
            "generated_source_of_truth",
            all(term in gen for term in ["readResidentHistory", "recordResidentHistory", "formatResidentHistory"]),
            "resident-history lane logic lives in the v61 generator",
            "regeneration would erase resident-history UI hardening",
        ),
        _criterion(
            "history_storage_registered",
            "ssrm_v61_app_shell_resident_history" in app and "HISTORY_KEY" in app,
            "resident history has a named browser-local storage key",
            "history continuity would be implicit or non-persistent",
        ),
        _criterion(
            "history_bounded",
            "slice(-14)" in app and "slice(-4)" in app,
            "history recording and visible display are bounded",
            "resident history could grow unbounded or overwhelm the reviewer lane",
        ),
        _criterion(
            "public_state_only",
            all(term in app for term in ["debt", "trust", "progress", "memory"]) and all(term in app for term in ["privateWorkspace", "subjectiveFeeling", "llmTranscript"]),
            "history rows use public resident summaries while existing audit forbids private/LLM keys",
            "history lane might weaken the source-boundary discipline",
        ),
        _criterion(
            "browser_workflow",
            browser.get("workflow_pass") is True,
            f"browser workflow pass recorded as {browser.get('workflow_pass')}",
            "source checks alone would not prove the lane updates in a browser",
        ),
        _criterion(
            "browser_selected_resident_history",
            browser.get("selected_resident_history_pass") is True,
            str(browser.get("selected_resident_history_evidence", "missing selected resident evidence")),
            "selected resident interactions would not be readable in the lane",
        ),
        _criterion(
            "browser_offscreen_resident_history",
            browser.get("offscreen_history_pass") is True,
            str(browser.get("offscreen_history_evidence", "missing offscreen resident evidence")),
            "offscreen resident progress would not be visible as continuity evidence",
        ),
        _criterion(
            "browser_resume_persistence",
            browser.get("resume_history_pass") is True,
            str(browser.get("resume_history_evidence", "missing resume evidence")),
            "resident history would not survive leave/return through the primary demo",
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
        "resident_history_panel_score": next(row.score for row in criteria if row.channel == "resident_history_panel_present"),
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
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v71_primary_demo_resident_history_lane_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 311: SSRM-3D Browser World v71 Primary Demo Resident History Lane

## Purpose

Report 311 continues consolidation of the single playable browser world. Report 310 made the session readable; this report makes resident continuity readable. The maintained v61 shell now exposes a compact resident-history lane showing public trust, debt, progress, and memory changes per resident.

No new simulation organ was added. The lane records and displays public interaction continuity that already matters to the playable loop.

## Boundary

{results['boundary']}

## What changed

- Added a `Resident history` panel to the maintained v61 shell.
- Added bounded browser-local `ssrm_v61_app_shell_resident_history` storage.
- Recorded public resident-history rows when trust, debt, progress, schedule, or memory changes.
- Displayed current resident summaries plus recent public interactions for each resident.
- Preserved the existing no-private-workspace/no-subjective-feeling/no-LLM-transcript audit boundary.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| resident_history_panel_score | {metrics['resident_history_panel_score']:.6f} |
| browser_workflow_score | {metrics['browser_workflow_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- workflow_pass: `{browser.get('workflow_pass')}`
- selected_resident_history_pass: `{browser.get('selected_resident_history_pass')}`
- offscreen_history_pass: `{browser.get('offscreen_history_pass')}`
- resume_history_pass: `{browser.get('resume_history_pass')}`
- console_errors: `{browser.get('console_errors')}`
- selected evidence: `{browser.get('selected_resident_history_evidence')}`
- offscreen evidence: `{browser.get('offscreen_history_evidence')}`
- resume evidence: `{browser.get('resume_history_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

This is readability and continuity hardening only. It does not imply subjective experience, autonomous language, or moral patienthood.

## Next gate

{results['next_gate']}
"""
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v71_primary_demo_resident_history_lane_report.md").write_text(report, encoding="utf-8")


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
