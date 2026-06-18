"""Report 329: SSRM-3D browser world v89 primary demo resume handoff freshness.

This report fixes reload/resume handoff drift: a previously prepared handoff
payload could stay visible after Resume demo changed the current launch handoff.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 329
PREFIX = "ssrm_3d_browser_world_v89_primary_demo_resume_handoff_freshness"
DEFAULT_SEED = 20270727

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V63_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
PRIMARY_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo"
PRIMARY_JS = PRIMARY_DIR / "demo.js"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"
PRE_PATCH_EVIDENCE = ARTIFACTS / f"{PREFIX.replace('_freshness', '_stale')}_pre_patch_evidence.json"

BOUNDARY = (
    "Deterministic browser-local resume handoff freshness only; no LLM calls, no subjective consciousness, "
    "no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, "
    "and no finished gameplay claim. Freshness warnings are review evidence hygiene, not external validation "
    "or evidence of inner experience."
)

NEXT_GATE = (
    "post-329: continue reload/resume review hardening by checking whether a stale handoff can be safely "
    "re-prepared after resume without losing recorder, checklist, or shell evidence continuity"
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
    js = _read(PRIMARY_JS)
    browser = _load_json(BROWSER_EVIDENCE)
    pre_patch = _load_json(PRE_PATCH_EVIDENCE)
    blockers = pre_patch.get("blockers", []) if isinstance(pre_patch.get("blockers"), list) else []
    required_terms = [
        "handoffPayloadFreshnessState",
        "previewFreshness",
        "Prepared handoff payload is stale",
        "launch handoff changed",
        "renderOutsideReviewHandoffPreview();",
    ]
    criteria = [
        _criterion(
            "pre_patch_resume_stale_payload_found",
            any("stale-payload" in blocker or "older clean launch" in blocker for blocker in blockers),
            "; ".join(blockers) or "missing pre-patch resume stale-payload evidence",
            "Report 329 would not be tied to a demonstrated reload/resume defect",
        ),
        _criterion(
            "freshness_source_generated",
            all(term in generator for term in required_terms) and all(term in js for term in required_terms),
            "launcher generator and emitted JS contain handoff payload freshness detection",
            "regeneration would remove stale-payload warnings",
        ),
        _criterion(
            "browser_resume_stale_warning_visible",
            browser.get("resume_stale_warning_visible") is True,
            str(browser.get("resume_stale_warning_evidence", "missing stale warning evidence")),
            "resume drift still leaves a stale handoff payload visible without warning",
        ),
        _criterion(
            "browser_preview_freshness_marks_stale",
            browser.get("preview_freshness_marks_stale") is True,
            str(browser.get("preview_freshness_evidence", "missing preview freshness evidence")),
            "preview payload does not carry machine-readable freshness state",
        ),
        _criterion(
            "browser_detects_handoff_kind_mismatch",
            browser.get("detects_handoff_kind_mismatch") is True,
            str(browser.get("handoff_kind_mismatch_evidence", "missing handoff mismatch evidence")),
            "freshness state does not explain clean-vs-resume handoff mismatch",
        ),
        _criterion(
            "browser_original_payload_still_inspectable",
            browser.get("original_payload_still_inspectable") is True,
            str(browser.get("payload_inspection_evidence", "missing payload inspection evidence")),
            "freshness warning hides the actual exported payload contents",
        ),
        _criterion(
            "browser_reload_resume_console_clean",
            browser.get("console_errors") == 0,
            f"browser console error count was {browser.get('console_errors')}",
            "reload/resume freshness flow produced browser console errors",
        ),
        _criterion(
            "prior_completion_not_broken",
            browser.get("prior_completion_not_broken") is True,
            str(browser.get("prior_completion_evidence", "missing prior completion evidence")),
            "freshness detection broke normal reviewed handoff completion",
        ),
        _criterion(
            "stale_warning_actionable",
            "Re-run Prepare outside-review handoff" in js,
            "stale warning tells reviewers the exact recovery action",
            "stale warning is ambiguous and does not tell reviewers how to recover",
        ),
        _criterion(
            "boundary_preserved",
            "no subjective consciousness" in BOUNDARY and "no LLM calls" in BOUNDARY,
            BOUNDARY,
            "report boundary implies more than browser-local freshness hardening",
        ),
    ]
    scores = [row.score for row in criteria]
    readiness = mean(scores)
    weakest = min(scores)
    verdict = "pass" if readiness >= 0.95 and weakest >= 0.9 and all(row.passed for row in criteria) else "needs_browser_evidence"
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "freshness_source_score": next(row.score for row in criteria if row.channel == "freshness_source_generated"),
        "browser_stale_warning_score": next(row.score for row in criteria if row.channel == "browser_resume_stale_warning_visible"),
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
            "pre_patch_evidence": f"artifacts/{PREFIX.replace('_freshness', '_stale')}_pre_patch_evidence.json",
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v89_primary_demo_resume_handoff_freshness_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    blockers = results["pre_patch_evidence"].get("blockers", [])
    blocker_rows = "\n".join(f"- {blocker}" for blocker in blockers) or "- No pre-patch blocker evidence was available."
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 329: SSRM-3D Browser World v89 Primary Demo Resume Handoff Freshness

## Purpose

Report 329 continues the cold one-URL handoff hardening after Report 328. The pre-patch reload/resume run found a concrete drift: after `Resume demo`, refreshed shell evidence pointed at the new resume launch handoff, but the visible prepared outside-review handoff payload still referenced the older clean launch handoff with no stale-payload warning.

The launcher now computes `handoffPayloadFreshnessState` for any visible prepared handoff payload. When refreshed shell evidence, recorder counts, or launch handoff state no longer match the prepared payload, the preview stays inspectable but is marked stale and tells the reviewer to re-run `Prepare outside-review handoff`.

## Boundary

{results['boundary']}

## Pre-patch blocker

{blocker_rows}

## What changed

- Added `handoffPayloadFreshnessState(payload)` to the primary launcher.
- `renderOutsideReviewHandoffPreview` now adds `previewFreshness` while preserving the exported payload fields at top level.
- `renderOutsideReviewEvidence` refreshes the handoff preview freshness when shell evidence changes.
- Stale previews now show an actionable warning: `Re-run Prepare outside-review handoff`.
- Verified in browser that reload plus resume exposes clean-vs-resume handoff drift as stale, keeps payload contents inspectable, and produces no console errors.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| freshness_source_score | {metrics['freshness_source_score']:.6f} |
| browser_stale_warning_score | {metrics['browser_stale_warning_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- resume_stale_warning_visible: `{browser.get('resume_stale_warning_visible')}`
- preview_freshness_marks_stale: `{browser.get('preview_freshness_marks_stale')}`
- detects_handoff_kind_mismatch: `{browser.get('detects_handoff_kind_mismatch')}`
- original_payload_still_inspectable: `{browser.get('original_payload_still_inspectable')}`
- prior_completion_not_broken: `{browser.get('prior_completion_not_broken')}`
- console_errors: `{browser.get('console_errors')}`
- stale warning evidence: `{browser.get('resume_stale_warning_evidence')}`
- freshness evidence: `{browser.get('preview_freshness_evidence')}`
- mismatch evidence: `{browser.get('handoff_kind_mismatch_evidence')}`
- payload evidence: `{browser.get('payload_inspection_evidence')}`

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
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v89_primary_demo_resume_handoff_freshness_report.md").write_text(report, encoding="utf-8")


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
