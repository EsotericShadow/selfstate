"""Report 315: SSRM-3D browser world v75 primary demo continuity loop.

This report consolidates the primary demo around one playable continuity walkthrough:
arrival, schedule inspection, debt consequence, offscreen activity, bounded trust wound,
non-magical trust repair, save/resume continuity, and replay/export visibility on the
same maintained browser shell.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 315
PREFIX = "ssrm_3d_browser_world_v75_primary_demo_continuity_loop"
DEFAULT_SEED = 20270713

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V61_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening.py"
V61_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
V61_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local continuity-loop consolidation only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, "
    "no complete 3D engine, and no finished gameplay claim. The loop demonstrates public state "
    "continuity, not inner experience."
)

NEXT_GATE = (
    "post-315: keep folding review affordances into the single primary shell until a reviewer can use "
    "one URL to enter, affect residents, leave, resume, inspect history, inspect replay, and understand "
    "what changed without reading raw JSON"
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
    required_events = [
        "enterWorld",
        "askSchedule",
        "borrowTool",
        "waitOffscreen",
        "interruptWork",
        "apologizeToResident",
        "giveSpace",
        "completeTrustRepair",
        "saveWorld",
        "exportReplay",
        "runContinuityLoop",
    ]

    criteria = [
        _criterion(
            "continuity_loop_panel_present",
            "continuityLoopOut" in index and "Continuity loop" in index,
            "maintained shell exposes a visible continuity-loop panel",
            "reviewers would still need to stitch the whole loop together manually",
        ),
        _criterion(
            "generated_source_of_truth",
            all(term in gen for term in ["runContinuityLoop", "formatContinuityLoopStatus", "continuityLoopOut"]),
            "continuity loop is generated from the maintained v61 source",
            "regeneration would erase the continuity-loop surface",
        ),
        _criterion(
            "same_surface_integration",
            all(term in app for term in required_events),
            "loop routes through existing arrival, schedule, debt, offscreen, repair, save, and replay functions",
            "loop would be another isolated bridge instead of a single playable surface",
        ),
        _criterion(
            "public_continuity_signals",
            all(term in app for term in ["Loop coverage", "Continuity signals", "export bytes", "Recent selected-resident history"]),
            "loop status summarizes coverage, history, checkpoints, replay rows, and export bytes in public UI",
            "reviewers would still need raw JSON to know whether the full loop happened",
        ),
        _criterion(
            "browser_loop_coverage",
            browser.get("loop_coverage_pass") is True,
            str(browser.get("loop_coverage_evidence", "missing loop coverage evidence")),
            "continuity loop did not visibly run all required events in browser",
        ),
        _criterion(
            "browser_consequence_repair",
            browser.get("consequence_repair_pass") is True,
            str(browser.get("consequence_repair_evidence", "missing consequence/repair evidence")),
            "debt, trust wound, and repair did not stay visible after the integrated loop",
        ),
        _criterion(
            "browser_dashboard_history_sync",
            browser.get("dashboard_history_sync_pass") is True,
            str(browser.get("dashboard_history_sync_evidence", "missing dashboard/history sync evidence")),
            "dashboard/history panels did not agree after the continuity loop",
        ),
        _criterion(
            "browser_replay_export_visible",
            browser.get("replay_export_pass") is True,
            str(browser.get("replay_export_evidence", "missing replay/export evidence")),
            "replay/export continuity was not visible after the loop",
        ),
        _criterion(
            "browser_resume_persistence",
            browser.get("resume_persistence_pass") is True,
            str(browser.get("resume_persistence_evidence", "missing resume evidence")),
            "continuity-loop state did not survive leave/resume",
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
        "continuity_loop_panel_score": next(row.score for row in criteria if row.channel == "continuity_loop_panel_present"),
        "browser_loop_coverage_score": next(row.score for row in criteria if row.channel == "browser_loop_coverage"),
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
        "required_events": required_events,
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "browser_evidence": browser,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "state": f"artifacts/{PREFIX}_state.json",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v75_primary_demo_continuity_loop_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    required_events = ", ".join(results["required_events"])
    report = f"""# Report 315: SSRM-3D Browser World v75 Primary Demo Continuity Loop

## Purpose

Report 315 makes the primary browser demo less toy-like by proving a whole reviewer-facing loop on one maintained URL: arrival, schedule inspection, debt consequence, offscreen activity, bounded trust wound, non-magical trust repair, save/resume continuity, and replay/export visibility.

This is consolidation, not a new simulation branch.

## Boundary

{results['boundary']}

## What changed

- Added a visible `Continuity loop` panel to the maintained v61 shell.
- Added `Run continuity loop`, which routes through existing shell actions instead of duplicating mechanics.
- Made the loop summarize event coverage, resident debt/trust/progress/memory, history rows, checkpoints, replay rows, and export bytes.
- Verified the loop through the primary demo clean/resume path in a browser.

## Required event spine

`{required_events}`

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| continuity_loop_panel_score | {metrics['continuity_loop_panel_score']:.6f} |
| browser_loop_coverage_score | {metrics['browser_loop_coverage_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- loop_coverage_pass: `{browser.get('loop_coverage_pass')}`
- consequence_repair_pass: `{browser.get('consequence_repair_pass')}`
- dashboard_history_sync_pass: `{browser.get('dashboard_history_sync_pass')}`
- replay_export_pass: `{browser.get('replay_export_pass')}`
- resume_persistence_pass: `{browser.get('resume_persistence_pass')}`
- console_errors: `{browser.get('console_errors')}`
- loop evidence: `{browser.get('loop_coverage_evidence')}`
- consequence/repair evidence: `{browser.get('consequence_repair_evidence')}`
- replay/export evidence: `{browser.get('replay_export_evidence')}`
- resume evidence: `{browser.get('resume_persistence_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

The result is still deterministic browser-local public-state continuity. It does not claim subjective experience, moral status, autonomous language, production persistence, complete gameplay, or a complete 3D engine.

## Next gate

{results['next_gate']}
"""
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v75_primary_demo_continuity_loop_report.md").write_text(report, encoding="utf-8")


def run(seed: int) -> dict[str, Any]:
    results = _evaluate(seed)
    _write_json(ARTIFACTS / f"{PREFIX}_results.json", results)
    _write_json(
        ARTIFACTS / f"{PREFIX}_state.json",
        {
            "report": REPORT,
            "seed": seed,
            "boundary": BOUNDARY,
            "maintained_shell": "visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html",
            "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
            "required_events": results["required_events"],
        },
    )
    _write_csv(ARTIFACTS / f"{PREFIX}_criteria.csv", results["criteria"])
    _write_csv(ARTIFACTS / f"{PREFIX}_summary.csv", [{"metric": key, "value": value} for key, value in results["metrics"].items()])
    _write_csv(
        ARTIFACTS / f"{PREFIX}_verdict.csv",
        [
            {
                "report": REPORT,
                "verdict": results["verdict"],
                "readiness": results["metrics"]["readiness"],
                "weakest_channel_score": results["metrics"]["weakest_channel_score"],
                "browser_loop_coverage_score": results["metrics"]["browser_loop_coverage_score"],
                "next_gate": NEXT_GATE,
            }
        ],
    )
    _write_report(results)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    print(
        json.dumps(
            {
                "report": results["report"],
                "verdict": results["verdict"],
                "readiness": round(results["metrics"]["readiness"], 6),
                "weakest_channel_score": round(results["metrics"]["weakest_channel_score"], 6),
                "browser_loop_coverage_score": round(results["metrics"]["browser_loop_coverage_score"], 6),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
