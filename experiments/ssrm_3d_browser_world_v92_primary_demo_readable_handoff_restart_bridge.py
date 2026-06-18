"""Report 332: SSRM-3D browser world v92 readable handoff restart bridge.

This report fixes cold-reviewer restart friction after Report 331: a persisted,
re-prepared resume handoff remained inspectable, but the human-readable status did
not say it was resume-bound. The page could still force reviewers into raw JSON
inspection for a critical restart fact.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 332
PREFIX = "ssrm_3d_browser_world_v92_primary_demo_readable_handoff_restart_bridge"
DEFAULT_SEED = 20270730

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V63_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
PRIMARY_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo"
PRIMARY_JS = PRIMARY_DIR / "demo.js"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"
PRE_PATCH_EVIDENCE = ARTIFACTS / f"{PREFIX}_pre_patch_evidence.json"
REPORT_331_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v91_primary_demo_reprepared_handoff_reload_persistence_results.json"

BOUNDARY = (
    "Deterministic browser-local readable handoff restart bridge only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, no "
    "complete 3D engine, and no finished gameplay claim. This is local review UX and evidence readability "
    "hygiene, not external validation or evidence of inner experience."
)

NEXT_GATE = (
    "post-332: run a cold reviewer restart from the readable handoff card and verify the reviewer can "
    "continue using visible controls/status text only, without raw JSON or localStorage inspection"
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


def _safe_get(value: Any, *path: str) -> Any:
    current = value
    for key in path:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def _evaluate(seed: int) -> dict[str, Any]:
    generator = _read(V63_GEN)
    js = _read(PRIMARY_JS)
    browser = _load_json(BROWSER_EVIDENCE)
    pre_patch = _load_json(PRE_PATCH_EVIDENCE)
    report_331 = _load_json(REPORT_331_RESULTS)
    checks = browser.get("checks", {}) if isinstance(browser.get("checks"), dict) else {}
    persisted = browser.get("persistedVisibleAfterReload", {}) if isinstance(browser.get("persistedVisibleAfterReload"), dict) else {}
    stale = browser.get("staleVisibleBeforeReprepare", {}) if isinstance(browser.get("staleVisibleBeforeReprepare"), dict) else {}
    pre_visible = pre_patch.get("prePatchVisible", {}) if isinstance(pre_patch.get("prePatchVisible"), dict) else {}
    pre_checks = pre_visible.get("readableChecks", {}) if isinstance(pre_visible.get("readableChecks"), dict) else {}
    blockers = pre_patch.get("blockers", []) if isinstance(pre_patch.get("blockers"), list) else []
    required_terms = [
        "readableHandoffSummary",
        "Outside-review handoff ready:",
        "freshnessText",
        "handoff.kind || 'unknown'",
        "checklist ${checklistDone}",
        "previewReadableSummary",
        "Payload is ${freshness.payloadHandoffKind",
    ]
    criteria = [
        _criterion(
            "report_331_reload_persistence_gate_passed",
            report_331.get("verdict") == "pass" and _safe_get(report_331, "metrics", "weakest_channel_score") == 1.0,
            f"Report 331 verdict={report_331.get('verdict')} weakest={_safe_get(report_331, 'metrics', 'weakest_channel_score')}",
            "Report 332 would not be grounded in a passing reload-persistence gate",
        ),
        _criterion(
            "pre_patch_readability_defect_found",
            pre_visible.get("readableScore", 1) < 1 and pre_checks.get("hasReadableResume") is False,
            "; ".join(blockers) or str(pre_visible),
            "Report 332 would not be tied to an observed visible-readability defect",
        ),
        _criterion(
            "readable_summary_source_generated",
            all(term in generator for term in required_terms) and all(term in js for term in required_terms),
            "primary launcher generator and emitted JS contain readableHandoffSummary and exported previewReadableSummary",
            "regeneration would remove the readable restart summary",
        ),
        _criterion(
            "stale_warning_explains_payload_and_current_kinds",
            checks.get("stale_warning_mentions_payload_and_current_kinds") is True,
            str(stale.get("statusText", "missing stale status")),
            "stale recovery warning does not explain clean-vs-resume mismatch in visible text",
        ),
        _criterion(
            "visible_summary_mentions_fresh",
            checks.get("visible_summary_mentions_fresh") is True,
            str(persisted.get("statusText", "missing status")),
            "visible handoff summary does not say the payload is fresh",
        ),
        _criterion(
            "visible_summary_mentions_resume",
            checks.get("visible_summary_mentions_resume") is True,
            str(persisted.get("statusText", "missing status")),
            "visible handoff summary does not say the payload is resume-bound",
        ),
        _criterion(
            "visible_summary_mentions_checklist",
            checks.get("visible_summary_mentions_checklist") is True,
            str(persisted.get("statusText", "missing status")),
            "visible handoff summary does not summarize checklist completion",
        ),
        _criterion(
            "visible_summary_mentions_recorder",
            checks.get("visible_summary_mentions_recorder") is True,
            str(persisted.get("statusText", "missing status")),
            "visible handoff summary does not summarize manual recorder/export evidence",
        ),
        _criterion(
            "visible_summary_mentions_shell_evidence",
            checks.get("visible_summary_mentions_shell_evidence") is True,
            str(persisted.get("statusText", "missing status")),
            "visible handoff summary does not summarize shell reviewer-pass/receipt/replay evidence",
        ),
        _criterion(
            "visible_summary_mentions_next_action",
            checks.get("visible_summary_mentions_next_action") is True,
            str(persisted.get("statusText", "missing status")),
            "visible handoff summary does not give a reviewer an actionable next step",
        ),
        _criterion(
            "visible_summary_complete_without_json",
            checks.get("visible_summary_complete_without_json") is True and persisted.get("readableScore") == 1,
            f"readableScore={persisted.get('readableScore')} checks={persisted.get('readableChecks')}",
            "cold reviewer still needs raw JSON to recover one or more restart facts",
        ),
        _criterion(
            "raw_json_preview_still_available",
            checks.get("raw_json_preview_still_available") is True,
            str(persisted.get("parsedPayloadPreviewFreshness", "missing preview freshness")),
            "readable summary replaced the inspectable raw JSON audit payload",
        ),
        _criterion(
            "preview_readable_summary_exported",
            checks.get("preview_readable_summary_exported") is True,
            str(persisted.get("parsedPayloadPreviewReadableSummary", "missing exported readable summary")),
            "raw preview does not preserve the same readable summary for audit/export inspection",
        ),
        _criterion(
            "browser_console_clean",
            checks.get("no_console_errors") is True and browser.get("consoleErrors") == 0,
            f"consoleErrors={browser.get('consoleErrors')} messages={browser.get('consoleErrorMessages', [])}",
            "readable restart browser flow produced console errors",
        ),
        _criterion(
            "boundary_preserved",
            "no subjective consciousness" in BOUNDARY and "no LLM calls" in BOUNDARY,
            BOUNDARY,
            "report boundary implies more than browser-local review-readability hardening",
        ),
    ]
    scores = [row.score for row in criteria]
    readiness = mean(scores)
    weakest = min(scores)
    visible_channels = [
        "visible_summary_mentions_fresh",
        "visible_summary_mentions_resume",
        "visible_summary_mentions_checklist",
        "visible_summary_mentions_recorder",
        "visible_summary_mentions_shell_evidence",
        "visible_summary_mentions_next_action",
    ]
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "pre_patch_readable_score": pre_visible.get("readableScore", -1),
        "post_patch_readable_score": persisted.get("readableScore", -1),
        "visible_restart_fact_score": mean([next(row.score for row in criteria if row.channel == name) for name in visible_channels]),
        "json_audit_preservation_score": next(row.score for row in criteria if row.channel == "raw_json_preview_still_available"),
        "console_errors": browser.get("consoleErrors", -1),
        "criterion_count": len(criteria),
    }
    verdict = "pass" if readiness >= 0.95 and weakest >= 0.9 and all(row.passed for row in criteria) else "needs_followup"
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
        "report_331_results_path": str(REPORT_331_RESULTS.relative_to(ROOT)),
        "pre_patch_evidence": pre_patch,
        "browser_evidence": browser,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "state": f"artifacts/{PREFIX}_state.json",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "pre_patch_evidence": f"artifacts/{PREFIX}_pre_patch_evidence.json",
            "report": f"docs/{REPORT}_{PREFIX}_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    pre_patch = results["pre_patch_evidence"]
    persisted = browser.get("persistedVisibleAfterReload", {}) if isinstance(browser.get("persistedVisibleAfterReload"), dict) else {}
    stale = browser.get("staleVisibleBeforeReprepare", {}) if isinstance(browser.get("staleVisibleBeforeReprepare"), dict) else {}
    blocker_rows = "\n".join(f"- {blocker}" for blocker in pre_patch.get("blockers", [])) or "- No pre-patch readability blocker was recorded."
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 332: SSRM-3D Browser World v92 Primary Demo Readable Handoff Restart Bridge

## Purpose

Report 332 fixes the next restart-friction defect in the consolidated primary demo. Report 331 proved that a re-prepared `resume` handoff persists after another launcher reload, but the visible status line still only said `Outside-review handoff payload visible below.` The `resume` binding was present in the raw JSON, so a cold reviewer had to inspect JSON for a critical restart fact.

The primary launcher now renders a concise readable handoff summary whenever the prepared payload is fresh. The summary names freshness, launch kind, checklist completion, shell evidence readiness, recorder/export evidence, and the next action. The raw JSON preview remains visible and now includes `previewReadableSummary` alongside `previewFreshness`.

## Boundary

{results['boundary']}

## Pre-patch blocker

{blocker_rows}

## What changed

- Added `readableHandoffSummary(payload, freshness)` to the primary launcher and generator.
- Fresh prepared handoffs now show a readable status line such as: `{persisted.get('statusText')}`
- Stale prepared handoffs now explain payload kind versus current shell kind, for example: `{stale.get('statusText')}`
- Raw JSON preview remains available and includes both `previewFreshness` and `previewReadableSummary`.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| pre_patch_readable_score | {metrics['pre_patch_readable_score']:.6f} |
| post_patch_readable_score | {metrics['post_patch_readable_score']:.6f} |
| visible_restart_fact_score | {metrics['visible_restart_fact_score']:.6f} |
| json_audit_preservation_score | {metrics['json_audit_preservation_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence summary

- stale_warning_mentions_payload_and_current_kinds: `{browser.get('checks', {}).get('stale_warning_mentions_payload_and_current_kinds')}`
- visible_summary_mentions_fresh: `{browser.get('checks', {}).get('visible_summary_mentions_fresh')}`
- visible_summary_mentions_resume: `{browser.get('checks', {}).get('visible_summary_mentions_resume')}`
- visible_summary_mentions_checklist: `{browser.get('checks', {}).get('visible_summary_mentions_checklist')}`
- visible_summary_mentions_recorder: `{browser.get('checks', {}).get('visible_summary_mentions_recorder')}`
- visible_summary_mentions_shell_evidence: `{browser.get('checks', {}).get('visible_summary_mentions_shell_evidence')}`
- visible_summary_mentions_next_action: `{browser.get('checks', {}).get('visible_summary_mentions_next_action')}`
- visible_summary_complete_without_json: `{browser.get('checks', {}).get('visible_summary_complete_without_json')}`
- raw_json_preview_still_available: `{browser.get('checks', {}).get('raw_json_preview_still_available')}`
- preview_readable_summary_exported: `{browser.get('checks', {}).get('preview_readable_summary_exported')}`
- no_console_errors: `{browser.get('checks', {}).get('no_console_errors')}`

## Persisted visible summary after reload

```text
{persisted.get('statusText', '')}
```

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
    (DOCS / f"{REPORT}_{PREFIX}_report.md").write_text(report, encoding="utf-8")


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
        "pre_patch_evidence_path": results["pre_patch_evidence_path"],
        "browser_evidence_path": results["browser_evidence_path"],
        "report_331_results_path": results["report_331_results_path"],
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
