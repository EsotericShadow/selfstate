"""Report 327: SSRM-3D browser world v87 primary demo full handoff loop completion.

This report hardens the complete outside-review handoff loop. It adds a gated
reviewed-handoff completion action that requires refreshed shell evidence and a
visible recorder export before the launcher can claim the checklist is complete.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 327
PREFIX = "ssrm_3d_browser_world_v87_primary_demo_full_handoff_loop_completion"
DEFAULT_SEED = 20270725

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V63_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
PRIMARY_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo"
PRIMARY_INDEX = PRIMARY_DIR / "index.html"
PRIMARY_JS = PRIMARY_DIR / "demo.js"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"
PRE_PATCH_EVIDENCE = ARTIFACTS / "ssrm_3d_browser_world_v87_primary_demo_full_handoff_loop_pre_patch_evidence.json"

BOUNDARY = (
    "Deterministic browser-local outside-review workflow hardening only; no LLM calls, no subjective consciousness, "
    "no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, "
    "and no finished gameplay claim. The completion gate is a review integrity guard, not external validation "
    "or evidence of inner experience."
)

NEXT_GATE = (
    "post-327: run a cold outside-reviewer handoff from one URL without privileged localStorage inspection, "
    "then fix the first remaining place where review evidence, recorder evidence, or handoff payload state can diverge"
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
    generator = _read(V63_GEN)
    index = _read(PRIMARY_INDEX)
    js = _read(PRIMARY_JS)
    browser = _load_json(BROWSER_EVIDENCE)
    pre_patch = _load_json(PRE_PATCH_EVIDENCE)
    required_terms = [
        "completeReviewedHandoff",
        "reviewedHandoffCompletionState",
        "Complete reviewed handoff",
        "manual recorder outcome",
        "reviewedHandoffCompletion",
        "recordCount",
        "recorderExport: readRecorderExportPayload()",
    ]
    criteria = [
        _criterion(
            "pre_patch_loop_found_real_blocker",
            bool(pre_patch.get("blockers")),
            "; ".join(pre_patch.get("blockers", [])) or "missing pre-patch blocker evidence",
            "Report 327 would be speculative rather than defect-driven",
        ),
        _criterion(
            "completion_button_generated_from_source",
            all(term in generator for term in required_terms) and "completeReviewedHandoff" in js,
            "primary launcher generator and emitted JS contain the reviewed handoff completion gate",
            "regeneration would erase the handoff-completion guard",
        ),
        _criterion(
            "completion_button_visible_in_launcher",
            "completeReviewedHandoff" in index and "Complete reviewed handoff" in index,
            "launcher exposes a first-class completion action in the outside-review controls",
            "cold reviewers still need to infer how to complete the handoff",
        ),
        _criterion(
            "recorder_export_visible_payload",
            "recorderExport: readRecorderExportPayload()" in js and "primary-demo-recorder-export-public-local-only" in js,
            "recorder panel now renders the prepared recorder export payload and boundary",
            "recorder export can still be prepared invisibly or without visible boundary evidence",
        ),
        _criterion(
            "browser_completion_blocks_without_recorder",
            browser.get("completion_blocks_without_recorder") is True,
            str(browser.get("completion_blocks_without_recorder_evidence", "missing block evidence")),
            "completion succeeds even when recorder evidence is missing",
        ),
        _criterion(
            "browser_recorder_export_visible_with_boundary",
            browser.get("recorder_export_visible_with_boundary") is True,
            str(browser.get("recorder_export_visible_evidence", "missing recorder export evidence")),
            "prepared recorder export is not visible with boundary and record counts",
        ),
        _criterion(
            "browser_completion_succeeds_after_record_and_export",
            browser.get("completion_succeeds_after_record_and_export") is True,
            str(browser.get("completion_success_evidence", "missing completion success evidence")),
            "reviewed handoff does not complete after all required evidence is present",
        ),
        _criterion(
            "browser_handoff_payload_carries_completion",
            browser.get("handoff_payload_carries_completion") is True,
            str(browser.get("handoff_completion_evidence", "missing handoff completion evidence")),
            "final handoff payload does not carry reviewed completion state",
        ),
        _criterion(
            "browser_full_loop_console_clean",
            browser.get("console_errors") == 0,
            f"browser console error count was {browser.get('console_errors')}",
            "full handoff loop produced browser console errors",
        ),
        _criterion(
            "boundary_preserved",
            "no subjective consciousness" in BOUNDARY and "no LLM calls" in BOUNDARY,
            BOUNDARY,
            "report boundary implies more than browser-local review workflow hardening",
        ),
    ]
    scores = [row.score for row in criteria]
    readiness = mean(scores)
    weakest = min(scores)
    verdict = "pass" if readiness >= 0.95 and weakest >= 0.9 and all(row.passed for row in criteria) else "needs_browser_evidence"
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "completion_source_score": next(row.score for row in criteria if row.channel == "completion_button_generated_from_source"),
        "browser_completion_score": next(row.score for row in criteria if row.channel == "browser_completion_succeeds_after_record_and_export"),
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
        "required_terms": required_terms,
        "pre_patch_evidence_path": str(PRE_PATCH_EVIDENCE.relative_to(ROOT)),
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "pre_patch_evidence": pre_patch,
        "browser_evidence": browser,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "state": f"artifacts/{PREFIX}_state.json",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "pre_patch_evidence": f"artifacts/ssrm_3d_browser_world_v87_primary_demo_full_handoff_loop_pre_patch_evidence.json",
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v87_primary_demo_full_handoff_loop_completion_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    blockers = results["pre_patch_evidence"].get("blockers", [])
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    blocker_rows = "\n".join(f"- {blocker}" for blocker in blockers) or "- No pre-patch blocker evidence was available."
    report = f"""# Report 327: SSRM-3D Browser World v87 Primary Demo Full Handoff Loop Completion

## Purpose

Report 327 runs the Report 326 next gate: a full outside-review loop from clean launcher through shell reviewer pass, shell-to-launcher return, checklist completion, shell-evidence refresh, visible handoff preview, and defect-recorder export.

The pre-patch loop found that the final handoff could still be made to look complete while reviewer evidence and recorder evidence diverged. The launcher now has a gated `Complete reviewed handoff` action that only succeeds after refreshed shell evidence shows an all-pass reviewer run, replay export readiness is present, a recorder export exists, at least one manual recorder outcome exists, and no unresolved defects remain.

## Boundary

{results['boundary']}

## Pre-patch blockers

{blocker_rows}

## What changed

- Added `Complete reviewed handoff` to the outside-review controls.
- Added `reviewedHandoffCompletionState` and `completeReviewedHandoff`.
- Completion blocks until shell evidence, recorder export, manual recorder outcome, replay export, and open-defect checks are satisfied.
- Recorder export now carries record/defect counts, `preparedAt`, and a visible export payload in the recorder panel.
- Final handoff payload now embeds `reviewedHandoffCompletion` and `recorderExport` instead of only a boolean export flag.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| completion_source_score | {metrics['completion_source_score']:.6f} |
| browser_completion_score | {metrics['browser_completion_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- completion_blocks_without_recorder: `{browser.get('completion_blocks_without_recorder')}`
- recorder_export_visible_with_boundary: `{browser.get('recorder_export_visible_with_boundary')}`
- completion_succeeds_after_record_and_export: `{browser.get('completion_succeeds_after_record_and_export')}`
- handoff_payload_carries_completion: `{browser.get('handoff_payload_carries_completion')}`
- console_errors: `{browser.get('console_errors')}`
- block evidence: `{browser.get('completion_blocks_without_recorder_evidence')}`
- recorder export evidence: `{browser.get('recorder_export_visible_evidence')}`
- completion evidence: `{browser.get('completion_success_evidence')}`
- handoff evidence: `{browser.get('handoff_completion_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

## Next gate

{results['next_gate']}
"""
    DOCS.mkdir(parents=True, exist_ok=True)
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v87_primary_demo_full_handoff_loop_completion_report.md").write_text(report, encoding="utf-8")


def run(seed: int) -> dict[str, Any]:
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    results = _evaluate(seed)
    _write_report(results)
    _write_json(ARTIFACTS / f"{PREFIX}_results.json", results)
    _write_json(ARTIFACTS / f"{PREFIX}_state.json", {
        "report": REPORT,
        "seed": seed,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "required_terms": results["required_terms"],
        "browser_evidence_path": results["browser_evidence_path"],
        "pre_patch_evidence_path": results["pre_patch_evidence_path"],
        "verdict": results["verdict"],
    })
    _write_csv(ARTIFACTS / f"{PREFIX}_criteria.csv", results["criteria"])
    _write_csv(ARTIFACTS / f"{PREFIX}_summary.csv", [{**results["metrics"], "report": REPORT, "seed": seed, "verdict": results["verdict"]}])
    _write_csv(ARTIFACTS / f"{PREFIX}_verdict.csv", [{"report": REPORT, "seed": seed, "verdict": results["verdict"], "boundary": BOUNDARY, "next_gate": NEXT_GATE}])
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    print(json.dumps({"report": REPORT, "prefix": PREFIX, "verdict": results["verdict"], "metrics": results["metrics"]}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
