"""Report 323: SSRM-3D browser world v83 primary demo outside-review checklist.

This report packages the launcher, boundary, reviewer landing, integrated receipt,
observation triage, manual recorder, and export path into one browser-local
outside-review checklist.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 323
PREFIX = "ssrm_3d_browser_world_v83_primary_demo_outside_review_checklist"
DEFAULT_SEED = 20270721

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V63_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
PRIMARY_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo"
PRIMARY_INDEX = PRIMARY_DIR / "index.html"
PRIMARY_JS = PRIMARY_DIR / "demo.js"
PRIMARY_CSS = PRIMARY_DIR / "styles.css"
PRIMARY_MANUAL = PRIMARY_DIR / "manual_playtest.md"
PRIMARY_QA = PRIMARY_DIR / "qa_manifest.json"
PRIMARY_LAUNCH = PRIMARY_DIR / "launch_manifest.json"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local outside-review checklist packaging only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, "
    "no complete 3D engine, and no finished gameplay claim. The checklist is a handoff workflow over "
    "public launcher and shell state, not external validation or evidence of inner experience."
)

NEXT_GATE = (
    "post-323: use the outside-review checklist for a complete reviewer walkthrough, then harden any "
    "real defects found in the same maintained primary shell instead of adding parallel demo surfaces"
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
    css = _read(PRIMARY_CSS)
    manual = _read(PRIMARY_MANUAL)
    qa = _load_json(PRIMARY_QA)
    launch = _load_json(PRIMARY_LAUNCH)
    browser = _load_json(BROWSER_EVIDENCE)
    source_terms = [
        "OUTSIDE_REVIEW_CHECKLIST",
        "OUTSIDE_REVIEW_KEY",
        "outsideReviewChecklist",
        "exportOutsideReviewHandoff",
        "ssrm_primary_demo_outside_review_handoff",
    ]
    checklist_ids = [f"OR-0{index}" for index in range(1, 8)]
    state_keys = qa.get("state_keys", []) if isinstance(qa.get("state_keys"), list) else []
    criteria = [
        _criterion(
            "checklist_generated_from_source",
            all(term in gen for term in source_terms) and all(term in js for term in ["OUTSIDE_REVIEW_KEY", "exportOutsideReviewHandoff"]),
            "outside-review checklist and export logic are generated from the Report 303 package source",
            "regeneration would erase the handoff checklist",
        ),
        _criterion(
            "launcher_checklist_visible",
            "Outside-review checklist" in index and all(item_id in index for item_id in checklist_ids) and "Prepare outside-review handoff" in index,
            "primary launcher renders OR-01..OR-07 and the handoff export action",
            "reviewers would still need to infer the handoff path from scattered panels",
        ),
        _criterion(
            "manifest_state_keys_registered",
            "ssrm_primary_demo_outside_review_checklist" in state_keys and "ssrm_primary_demo_outside_review_handoff" in state_keys and qa.get("outside_review_checklist_items") == 7,
            "QA manifest lists checklist and handoff state keys with 7 checklist items",
            "outside-review state would not be inspectable in the launcher manifest",
        ),
        _criterion(
            "manual_script_mentions_checklist",
            "Outside-review checklist" in manual and "ssrm_primary_demo_outside_review_checklist" in manual,
            "manual playtest explains the outside-review checklist and browser-local state key",
            "manual reviewers would not know the checklist exists or where it persists",
        ),
        _criterion(
            "one_shell_policy_preserved",
            "../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html" in index and launch.get("target_shell") == "../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html",
            "launcher still targets the maintained v61 shell instead of a parallel world",
            "handoff checklist would fragment the primary demo into another surface",
        ),
        _criterion(
            "browser_checklist_visible",
            browser.get("checklist_visible_pass") is True,
            str(browser.get("checklist_visible_evidence", "missing checklist visibility evidence")),
            "browser did not show the outside-review checklist and core links",
        ),
        _criterion(
            "browser_mark_persistence",
            browser.get("mark_persistence_pass") is True,
            str(browser.get("mark_persistence_evidence", "missing mark persistence evidence")),
            "checklist mark-done state did not persist through reload",
        ),
        _criterion(
            "browser_handoff_export",
            browser.get("handoff_export_pass") is True,
            str(browser.get("handoff_export_evidence", "missing handoff export evidence")),
            "browser did not prepare an outside-review handoff export",
        ),
        _criterion(
            "browser_shell_link_handoff",
            browser.get("shell_link_handoff_pass") is True,
            str(browser.get("shell_link_handoff_evidence", "missing shell handoff evidence")),
            "launcher did not preserve clean/resume handoff to the maintained shell",
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
        "checklist_source_score": next(row.score for row in criteria if row.channel == "checklist_generated_from_source"),
        "browser_handoff_score": next(row.score for row in criteria if row.channel == "browser_handoff_export"),
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
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v83_primary_demo_outside_review_checklist_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 323: SSRM-3D Browser World v83 Primary Demo Outside-Review Checklist

## Purpose

Report 323 packages the reviewer-first primary demo into one outside-review checklist. A cold reviewer now has a single launcher path that names the boundary, clean launch, reviewer pass, receipt, observation triage, optional diagnostics, manual notes, and exportable handoff evidence.

This is handoff consolidation over the existing maintained shell, not a new simulation feature.

## Boundary

{results['boundary']}

## What changed

- Added `Outside-review checklist` to the stable primary demo launcher.
- Added OR-01 through OR-07, covering boundary, clean launch, reviewer pass, receipt/triage, failure audit, optional diagnostics, manual notes, and handoff export.
- Added browser-local checklist progress under `ssrm_primary_demo_outside_review_checklist`.
- Added `Prepare outside-review handoff`, which exports checklist state, launch handoff, manual records, defects, target shell, launch URL, and boundary.
- Registered the checklist and export state keys in the launcher QA manifest.
- Verified checklist visibility, mark-done persistence, handoff export preparation, maintained-shell clean/resume handoff, and console cleanliness in browser.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| checklist_source_score | {metrics['checklist_source_score']:.6f} |
| browser_handoff_score | {metrics['browser_handoff_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- checklist_visible_pass: `{browser.get('checklist_visible_pass')}`
- mark_persistence_pass: `{browser.get('mark_persistence_pass')}`
- handoff_export_pass: `{browser.get('handoff_export_pass')}`
- shell_link_handoff_pass: `{browser.get('shell_link_handoff_pass')}`
- console_errors: `{browser.get('console_errors')}`
- checklist evidence: `{browser.get('checklist_visible_evidence')}`
- mark evidence: `{browser.get('mark_persistence_evidence')}`
- export evidence: `{browser.get('handoff_export_evidence')}`
- shell handoff evidence: `{browser.get('shell_link_handoff_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

The honest limit remains: this is not an outside reviewer cohort. It is a stronger handoff path for one maintained deterministic browser-local demo.

## Next gate

{results['next_gate']}
"""
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v83_primary_demo_outside_review_checklist_report.md").write_text(report, encoding="utf-8")


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
            "outside_review_items": ["OR-01", "OR-02", "OR-03", "OR-04", "OR-05", "OR-06", "OR-07"],
            "state_keys": ["ssrm_primary_demo_outside_review_checklist", "ssrm_primary_demo_outside_review_handoff"],
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
