"""Report 325: SSRM-3D browser world v85 primary demo handoff payload preview.

This report fixes a reviewer-comprehension defect in the outside-review launcher:
after preparing the handoff export, reviewers can now inspect the actual handoff
payload in the page instead of needing downloads or localStorage inspection.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 325
PREFIX = "ssrm_3d_browser_world_v85_primary_demo_handoff_payload_preview"
DEFAULT_SEED = 20270723

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V63_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
PRIMARY_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo"
PRIMARY_INDEX = PRIMARY_DIR / "index.html"
PRIMARY_JS = PRIMARY_DIR / "demo.js"
PRIMARY_QA = PRIMARY_DIR / "qa_manifest.json"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local handoff-payload preview only; no LLM calls, no subjective consciousness, "
    "no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, "
    "and no finished gameplay claim. The preview exposes local review payload contents; it is not external validation, "
    "autonomous review, or evidence of inner experience."
)

NEXT_GATE = (
    "post-325: use the visible handoff payload to run a complete reviewer walkthrough and fix the next concrete "
    "comprehension defect in the same launcher or maintained shell"
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
    gen = _read(V63_GEN)
    index = _read(PRIMARY_INDEX)
    js = _read(PRIMARY_JS)
    qa = _load_json(PRIMARY_QA)
    browser = _load_json(BROWSER_EVIDENCE)
    source_terms = [
        "outsideReviewHandoffOut",
        "outsideReviewHandoffStatus",
        "readOutsideReviewHandoffPayload",
        "renderOutsideReviewHandoffPreview",
        "Outside-review handoff payload visible below.",
    ]
    state_keys = qa.get("state_keys", []) if isinstance(qa.get("state_keys"), list) else []
    criteria = [
        _criterion(
            "handoff_preview_generated_from_source",
            all(term in gen for term in source_terms) and all(term in js for term in source_terms[2:5]),
            "handoff payload preview is generated from the Report 303 launcher source",
            "regeneration would erase the visible payload preview",
        ),
        _criterion(
            "launcher_preview_panel_visible",
            "outsideReviewHandoffOut" in index and "outsideReviewHandoffStatus" in index,
            "primary launcher contains a visible handoff payload status and preview panel",
            "reviewers would still need downloads or localStorage to inspect handoff contents",
        ),
        _criterion(
            "export_wires_preview",
            "renderOutsideReviewHandoffPreview('Outside-review handoff payload visible below.');" in js and "renderOutsideReviewHandoffPreview();" in js,
            "handoff export and page load both render the visible payload preview",
            "prepared exports would remain invisible in-page",
        ),
        _criterion(
            "handoff_key_still_registered",
            "ssrm_primary_demo_outside_review_handoff" in state_keys,
            "QA manifest still registers the outside-review handoff local state key",
            "preview would point at unregistered browser-local state",
        ),
        _criterion(
            "browser_preview_empty_before_export",
            browser.get("preview_empty_before_export_pass") is True,
            str(browser.get("preview_empty_before_export_evidence", "missing pre-export evidence")),
            "browser did not show an explicit empty preview before export",
        ),
        _criterion(
            "browser_preview_after_export",
            browser.get("preview_after_export_pass") is True,
            str(browser.get("preview_after_export_evidence", "missing post-export evidence")),
            "browser did not show handoff payload contents after export",
        ),
        _criterion(
            "browser_preview_persists_reload",
            browser.get("preview_persists_reload_pass") is True,
            str(browser.get("preview_persists_reload_evidence", "missing reload evidence")),
            "handoff payload preview did not persist through launcher reload",
        ),
        _criterion(
            "browser_clear_resets_preview",
            browser.get("clear_resets_preview_pass") is True,
            str(browser.get("clear_resets_preview_evidence", "missing clear evidence")),
            "clearing the outside-review checklist did not clear visible handoff payload preview",
        ),
        _criterion(
            "browser_clean_resume_preserved",
            browser.get("clean_resume_preserved_pass") is True,
            str(browser.get("clean_resume_preserved_evidence", "missing clean/resume evidence")),
            "payload preview work broke clean/resume handoff to the maintained shell",
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
        "preview_source_score": next(row.score for row in criteria if row.channel == "handoff_preview_generated_from_source"),
        "browser_preview_score": next(row.score for row in criteria if row.channel == "browser_preview_after_export"),
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
        "required_terms": source_terms,
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "browser_evidence": browser,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "state": f"artifacts/{PREFIX}_state.json",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v85_primary_demo_handoff_payload_preview_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 325: SSRM-3D Browser World v85 Primary Demo Handoff Payload Preview

## Purpose

Report 325 fixes a concrete reviewer-comprehension defect in the outside-review launcher. Report 324 made the handoff export evidence-bearing, but a cold reviewer still had to download the file or inspect localStorage to see the final payload. The launcher now renders the prepared outside-review handoff payload in-page.

This is another consolidation pass over the same primary demo path, not a new world system.

## Boundary

{results['boundary']}

## What changed

- Added `outsideReviewHandoffStatus` and `outsideReviewHandoffOut` to the launcher.
- Added `readOutsideReviewHandoffPayload` and `renderOutsideReviewHandoffPreview`.
- The handoff export action now renders the full payload preview in-page.
- Page load restores any prepared handoff preview from local browser state.
- Clearing the outside-review checklist clears the visible handoff preview.
- Verified empty state, post-export payload preview, reload persistence, clear reset, clean/resume preservation, and console cleanliness in browser.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| preview_source_score | {metrics['preview_source_score']:.6f} |
| browser_preview_score | {metrics['browser_preview_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- preview_empty_before_export_pass: `{browser.get('preview_empty_before_export_pass')}`
- preview_after_export_pass: `{browser.get('preview_after_export_pass')}`
- preview_persists_reload_pass: `{browser.get('preview_persists_reload_pass')}`
- clear_resets_preview_pass: `{browser.get('clear_resets_preview_pass')}`
- clean_resume_preserved_pass: `{browser.get('clean_resume_preserved_pass')}`
- console_errors: `{browser.get('console_errors')}`
- empty evidence: `{browser.get('preview_empty_before_export_evidence')}`
- export evidence: `{browser.get('preview_after_export_evidence')}`
- reload evidence: `{browser.get('preview_persists_reload_evidence')}`
- clear evidence: `{browser.get('clear_resets_preview_evidence')}`
- clean/resume evidence: `{browser.get('clean_resume_preserved_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

The honest limit remains: this is local handoff readability, not an outside reviewer cohort or production deployment.

## Next gate

{results['next_gate']}
"""
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v85_primary_demo_handoff_payload_preview_report.md").write_text(report, encoding="utf-8")


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
            "preview_element_ids": ["outsideReviewHandoffStatus", "outsideReviewHandoffOut"],
            "target_shell": "visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html",
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
