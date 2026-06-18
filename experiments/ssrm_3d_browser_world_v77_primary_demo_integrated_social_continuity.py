"""Report 317: SSRM-3D browser world v77 primary demo integrated social continuity.

This report folds resident-to-resident social memory into the main primary-demo continuity
loop. The goal is one reviewer-facing button that covers avatar arrival, schedule/debt,
offscreen change, bounded trust repair, resident social memory, save/resume continuity,
and replay/export visibility on the same maintained shell.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 317
PREFIX = "ssrm_3d_browser_world_v77_primary_demo_integrated_social_continuity"
DEFAULT_SEED = 20270715

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V61_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening.py"
V61_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
V61_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local integrated continuity-loop consolidation only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, no "
    "complete 3D engine, and no finished gameplay claim. The result demonstrates public continuity across "
    "avatar and resident-to-resident state, not private experience."
)

NEXT_GATE = (
    "post-317: reduce reviewer friction by turning the integrated continuity loop into a compact scenario "
    "receipt with pass/fail fields for movement, schedule, obligations, resident social ties, replay, and resume"
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
    integrated_events = [
        "enterWorld",
        "askSchedule",
        "borrowTool",
        "waitOffscreen",
        "interruptWork",
        "apologizeToResident",
        "giveSpace",
        "completeTrustRepair",
        "runSocialMemoryPulse",
        "settleSelectedRelationship",
        "saveWorld",
        "exportReplay",
        "runContinuityLoop",
    ]

    criteria = [
        _criterion(
            "continuity_and_social_panels_present",
            "continuityLoopOut" in index and "relationshipMemoryOut" in index,
            "maintained shell exposes both continuity-loop and resident social-memory panels",
            "reviewers would not see the integrated loop and relationship state together",
        ),
        _criterion(
            "generated_source_of_truth",
            all(term in gen for term in ["resident-social-memory", "runSocialMemoryPulse();", "settleSelectedRelationship();", "residentToResident: true"]),
            "runContinuityLoop calls resident social-memory actions from the generator",
            "regeneration would drop social memory out of the main loop",
        ),
        _criterion(
            "one_button_required_events",
            all(term in app for term in integrated_events),
            "generated app required-event spine includes avatar, repair, social-memory, save, and replay actions",
            "main continuity loop would still be missing one or more non-toy requirements",
        ),
        _criterion(
            "relationship_excerpt_in_loop_status",
            "Relationship excerpt" in app and "formatRelationshipMemory().split" in app,
            "continuity-loop panel embeds public resident relationship evidence",
            "social memory would remain a separate panel rather than part of the integrated receipt",
        ),
        _criterion(
            "browser_integrated_loop_coverage",
            browser.get("integrated_loop_coverage_pass") is True,
            str(browser.get("integrated_loop_coverage_evidence", "missing integrated loop coverage evidence")),
            "one-button browser run did not cover all integrated events",
        ),
        _criterion(
            "browser_relationship_in_loop",
            browser.get("relationship_in_loop_pass") is True,
            str(browser.get("relationship_in_loop_evidence", "missing relationship-in-loop evidence")),
            "continuity-loop output did not include resident-to-resident relationship state",
        ),
        _criterion(
            "browser_consequence_stack_visible",
            browser.get("consequence_stack_pass") is True,
            str(browser.get("consequence_stack_evidence", "missing consequence stack evidence")),
            "debt, trust repair, social settlement, and history were not visible together",
        ),
        _criterion(
            "browser_replay_export_visible",
            browser.get("replay_export_pass") is True,
            str(browser.get("replay_export_evidence", "missing replay/export evidence")),
            "replay/export did not include the integrated social-continuity loop",
        ),
        _criterion(
            "browser_resume_persistence",
            browser.get("resume_persistence_pass") is True,
            str(browser.get("resume_persistence_evidence", "missing resume evidence")),
            "integrated social continuity did not survive leave/resume",
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
        "integrated_loop_source_score": next(row.score for row in criteria if row.channel == "generated_source_of_truth"),
        "browser_integrated_loop_score": next(row.score for row in criteria if row.channel == "browser_integrated_loop_coverage"),
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
        "integrated_events": integrated_events,
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "browser_evidence": browser,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "state": f"artifacts/{PREFIX}_state.json",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v77_primary_demo_integrated_social_continuity_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    integrated_events = ", ".join(results["integrated_events"])
    report = f"""# Report 317: SSRM-3D Browser World v77 Primary Demo Integrated Social Continuity

## Purpose

Report 317 folds resident-to-resident social memory into the main primary-demo continuity loop. A reviewer can now press one button and see arrival, schedule/debt consequence, offscreen change, bounded trust repair, resident social-memory pulse, selected relationship settlement, save/resume, and replay/export evidence on the same maintained browser shell.

This is consolidation, not a new world branch.

## Boundary

{results['boundary']}

## What changed

- Updated `Run continuity loop` so it calls the resident social-memory pulse and selected relationship settlement.
- Expanded loop coverage from avatar/trust-only continuity to integrated avatar plus resident-to-resident continuity.
- Embedded a relationship excerpt in the continuity-loop status panel.
- Verified the one-button loop through the primary demo clean/resume path in a browser.

## Integrated event spine

`{integrated_events}`

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| integrated_loop_source_score | {metrics['integrated_loop_source_score']:.6f} |
| browser_integrated_loop_score | {metrics['browser_integrated_loop_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- integrated_loop_coverage_pass: `{browser.get('integrated_loop_coverage_pass')}`
- relationship_in_loop_pass: `{browser.get('relationship_in_loop_pass')}`
- consequence_stack_pass: `{browser.get('consequence_stack_pass')}`
- replay_export_pass: `{browser.get('replay_export_pass')}`
- resume_persistence_pass: `{browser.get('resume_persistence_pass')}`
- console_errors: `{browser.get('console_errors')}`
- integrated loop evidence: `{browser.get('integrated_loop_coverage_evidence')}`
- relationship evidence: `{browser.get('relationship_in_loop_evidence')}`
- consequence evidence: `{browser.get('consequence_stack_evidence')}`
- replay/export evidence: `{browser.get('replay_export_evidence')}`
- resume evidence: `{browser.get('resume_persistence_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

The result is still deterministic browser-local public-state continuity. It does not claim subjective memory, subjective distress, moral status, autonomous language, production persistence, complete gameplay, or a complete 3D engine.

## Next gate

{results['next_gate']}
"""
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v77_primary_demo_integrated_social_continuity_report.md").write_text(report, encoding="utf-8")


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
            "integrated_events": results["integrated_events"],
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
                "browser_integrated_loop_score": results["metrics"]["browser_integrated_loop_score"],
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
                "browser_integrated_loop_score": round(results["metrics"]["browser_integrated_loop_score"], 6),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
