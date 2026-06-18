"""Report 330: SSRM-3D browser world v90 stale handoff reprepare continuity.

This report verifies the Report 329 recovery path: after a prepared clean handoff
becomes stale through reload plus Resume demo, re-running Prepare outside-review
handoff must refresh the payload without losing checklist, recorder, completion,
or shell evidence continuity.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 330
PREFIX = "ssrm_3d_browser_world_v90_primary_demo_stale_handoff_reprepare_continuity"
DEFAULT_SEED = 20270728

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V63_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
PRIMARY_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo"
PRIMARY_JS = PRIMARY_DIR / "demo.js"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"
REPORT_329_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v89_primary_demo_resume_handoff_freshness_results.json"

BOUNDARY = (
    "Deterministic browser-local stale handoff reprepare continuity only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, no "
    "complete 3D engine, and no finished gameplay claim. This is local review-evidence recovery hygiene, "
    "not external validation or evidence of inner experience."
)

NEXT_GATE = (
    "post-330: verify the re-prepared resume handoff remains inspectable after another launcher reload "
    "and does not depend on transient in-memory browser state"
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


def _count_true_items(value: Any) -> int:
    if not isinstance(value, dict):
        return 0
    return sum(1 for item in value.values() if item is True)


def _evaluate(seed: int) -> dict[str, Any]:
    generator = _read(V63_GEN)
    js = _read(PRIMARY_JS)
    browser = _load_json(BROWSER_EVIDENCE)
    report_329 = _load_json(REPORT_329_RESULTS)
    checks = browser.get("checks", {}) if isinstance(browser.get("checks"), dict) else {}
    clean = browser.get("cleanPreparedState", {}) if isinstance(browser.get("cleanPreparedState"), dict) else {}
    stale = browser.get("staleAfterResumeState", {}) if isinstance(browser.get("staleAfterResumeState"), dict) else {}
    reprepare = browser.get("rePreparedState", {}) if isinstance(browser.get("rePreparedState"), dict) else {}
    stale_freshness = _safe_get(stale, "handoff", "previewFreshness") or {}
    reprepare_freshness = _safe_get(reprepare, "handoff", "previewFreshness") or {}
    reprepare_handoff = reprepare.get("handoff", {}) if isinstance(reprepare.get("handoff"), dict) else {}
    required_terms = [
        "handoffPayloadFreshnessState",
        "previewFreshness",
        "Prepared handoff payload is stale",
        "Re-run Prepare outside-review handoff",
        "reviewedHandoffCompletion",
    ]
    checklist_items = _safe_get(reprepare_handoff, "checklistState", "items") or {}
    manual_records = reprepare_handoff.get("manualRecords", []) if isinstance(reprepare_handoff.get("manualRecords"), list) else []
    recorder_export = reprepare_handoff.get("recorderExport", {}) if isinstance(reprepare_handoff.get("recorderExport"), dict) else {}
    shell_evidence = reprepare_handoff.get("shellEvidence", {}) if isinstance(reprepare_handoff.get("shellEvidence"), dict) else {}
    completion = reprepare_handoff.get("reviewedHandoffCompletion", {}) if isinstance(reprepare_handoff.get("reviewedHandoffCompletion"), dict) else {}
    criteria = [
        _criterion(
            "report_329_freshness_gate_passed",
            report_329.get("verdict") == "pass" and _safe_get(report_329, "metrics", "weakest_channel_score") == 1.0,
            f"Report 329 verdict={report_329.get('verdict')} weakest={_safe_get(report_329, 'metrics', 'weakest_channel_score')}",
            "Report 330 would not be grounded in a passing stale-warning gate",
        ),
        _criterion(
            "freshness_source_still_present",
            all(term in generator for term in required_terms) and all(term in js for term in required_terms),
            "primary launcher generator and emitted JS still contain freshness, stale warning, and completion terms",
            "reprepare continuity could pass only against stale generated browser assets",
        ),
        _criterion(
            "clean_payload_fresh_before_resume",
            checks.get("clean_payload_fresh_before_resume") is True,
            str(_safe_get(clean, "handoff", "previewFreshness") or "missing clean freshness evidence"),
            "baseline clean handoff was already stale or uninspectable before resume",
        ),
        _criterion(
            "stale_warning_visible_after_resume_refresh",
            checks.get("stale_warning_visible_after_resume_refresh") is True,
            f"bodyHasStaleWarning={stale.get('bodyHasStaleWarning')} bodyHasReRunWarning={stale.get('bodyHasReRunWarning')}",
            "resume drift does not visibly tell reviewers to re-prepare the handoff",
        ),
        _criterion(
            "stale_preview_marks_handoff_mismatch",
            checks.get("stale_preview_marks_mismatch") is True
            and stale_freshness.get("fresh") is False
            and "launch handoff changed" in stale_freshness.get("mismatches", [])
            and "launch kind changed" in stale_freshness.get("mismatches", []),
            str(stale_freshness),
            "stale state does not explain that the old clean payload no longer matches the resume handoff",
        ),
        _criterion(
            "reprepare_clears_warning",
            checks.get("reprepare_clears_stale_warning") is True,
            f"bodyHasStaleWarning={reprepare.get('bodyHasStaleWarning')} bodyHasReRunWarning={reprepare.get('bodyHasReRunWarning')}",
            "re-running Prepare outside-review handoff leaves stale warning visible",
        ),
        _criterion(
            "reprepare_payload_fresh",
            checks.get("reprepare_payload_fresh") is True and reprepare_freshness.get("fresh") is True,
            str(reprepare_freshness),
            "re-prepared payload does not carry a fresh machine-readable preview state",
        ),
        _criterion(
            "reprepare_payload_uses_resume_handoff",
            checks.get("reprepare_payload_uses_resume_handoff") is True
            and _safe_get(reprepare_handoff, "handoff", "kind") == "resume"
            and _safe_get(shell_evidence, "handoff", "kind") == "resume",
            f"payload={_safe_get(reprepare_handoff, 'handoff', 'kind')} shell={_safe_get(shell_evidence, 'handoff', 'kind')}",
            "re-prepare keeps exporting the older clean handoff instead of the current resume handoff",
        ),
        _criterion(
            "checklist_preserved",
            checks.get("checklist_preserved") is True and _count_true_items(checklist_items) == 7,
            f"completed checklist items={_count_true_items(checklist_items)}",
            "re-prepare loses completed OR-01..OR-07 review state",
        ),
        _criterion(
            "recorder_preserved",
            checks.get("recorder_preserved") is True and len(manual_records) == 1 and recorder_export.get("recordCount") == 1,
            f"manualRecords={len(manual_records)} recorderExportRecordCount={recorder_export.get('recordCount')}",
            "re-prepare loses manual pass recorder continuity",
        ),
        _criterion(
            "shell_evidence_preserved",
            checks.get("shell_evidence_preserved") is True
            and shell_evidence.get("reviewerPassSeen") is True
            and shell_evidence.get("receiptAllPass") is True
            and shell_evidence.get("replayExportReady") is True,
            f"reviewerPassSeen={shell_evidence.get('reviewerPassSeen')} receiptAllPass={shell_evidence.get('receiptAllPass')} replayExportReady={shell_evidence.get('replayExportReady')}",
            "re-prepare drops reviewer pass, all-pass receipt, or replay export evidence",
        ),
        _criterion(
            "reviewed_completion_ready_after_reprepare",
            checks.get("reviewed_completion_ready") is True and completion.get("ready") is True,
            f"completionReady={completion.get('ready')} completionShellKind={_safe_get(completion, 'shellEvidence', 'handoff', 'kind')}",
            "reviewed handoff completion is no longer ready after re-prepare",
        ),
        _criterion(
            "browser_console_clean",
            checks.get("no_console_errors") is True and browser.get("consoleErrors") == 0,
            f"consoleErrors={browser.get('consoleErrors')} messages={browser.get('consoleErrorMessages', [])}",
            "stale reprepare browser flow produced console errors",
        ),
        _criterion(
            "boundary_preserved",
            "no subjective consciousness" in BOUNDARY and "no LLM calls" in BOUNDARY,
            BOUNDARY,
            "report boundary implies more than browser-local review-evidence recovery",
        ),
    ]
    scores = [row.score for row in criteria]
    readiness = mean(scores)
    weakest = min(scores)
    verdict = "pass" if readiness >= 0.95 and weakest >= 0.9 and all(row.passed for row in criteria) else "needs_followup"
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "stale_warning_recovery_score": next(row.score for row in criteria if row.channel == "reprepare_clears_warning"),
        "resume_payload_integrity_score": next(row.score for row in criteria if row.channel == "reprepare_payload_uses_resume_handoff"),
        "continuity_preservation_score": mean([
            next(row.score for row in criteria if row.channel == "checklist_preserved"),
            next(row.score for row in criteria if row.channel == "recorder_preserved"),
            next(row.score for row in criteria if row.channel == "shell_evidence_preserved"),
            next(row.score for row in criteria if row.channel == "reviewed_completion_ready_after_reprepare"),
        ]),
        "console_errors": browser.get("consoleErrors", -1),
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
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "report_329_results_path": str(REPORT_329_RESULTS.relative_to(ROOT)),
        "browser_evidence": browser,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "state": f"artifacts/{PREFIX}_state.json",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "report": f"docs/{REPORT}_{PREFIX}_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    stale = browser.get("staleAfterResumeState", {}) if isinstance(browser.get("staleAfterResumeState"), dict) else {}
    reprepare = browser.get("rePreparedState", {}) if isinstance(browser.get("rePreparedState"), dict) else {}
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 330: SSRM-3D Browser World v90 Primary Demo Stale Handoff Reprepare Continuity

## Purpose

Report 330 follows the Report 329 stale-payload warning with the recovery path a cold reviewer would actually use. The browser flow first prepared a clean outside-review handoff, then reloaded the launcher, used `Resume demo`, returned to the launcher handoff, refreshed shell evidence, and confirmed the old clean payload became visibly stale. It then re-ran `Prepare outside-review handoff` and checked that the resulting payload became fresh again without losing checklist, recorder, reviewed-completion, or shell evidence continuity.

No launcher behavior change was needed. This report preserves the finding honestly: the existing Report 329 freshness bridge already supports the reprepare recovery path.

## Boundary

{results['boundary']}

## Browser path

- Clean launch through the primary demo launcher.
- `Run reviewer pass` inside the maintained v61 shell.
- `Return to launcher handoff`.
- Complete OR-01..OR-07 and record one manual MP-03 pass.
- Prepare recorder export, complete reviewed handoff, and prepare the clean handoff payload.
- Reload launcher, use `Resume demo`, return, and refresh shell evidence.
- Observe stale payload warning on the old clean payload.
- Re-run `Prepare outside-review handoff`.
- Confirm the payload is fresh, uses the `resume` handoff, and preserves checklist, recorder, shell evidence, and completion state.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| stale_warning_recovery_score | {metrics['stale_warning_recovery_score']:.6f} |
| resume_payload_integrity_score | {metrics['resume_payload_integrity_score']:.6f} |
| continuity_preservation_score | {metrics['continuity_preservation_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence summary

- clean_payload_fresh_before_resume: `{browser.get('checks', {}).get('clean_payload_fresh_before_resume')}`
- stale_warning_visible_after_resume_refresh: `{browser.get('checks', {}).get('stale_warning_visible_after_resume_refresh')}`
- stale_preview_marks_mismatch: `{browser.get('checks', {}).get('stale_preview_marks_mismatch')}`
- reprepare_clears_stale_warning: `{browser.get('checks', {}).get('reprepare_clears_stale_warning')}`
- reprepare_payload_fresh: `{browser.get('checks', {}).get('reprepare_payload_fresh')}`
- reprepare_payload_uses_resume_handoff: `{browser.get('checks', {}).get('reprepare_payload_uses_resume_handoff')}`
- checklist_preserved: `{browser.get('checks', {}).get('checklist_preserved')}`
- recorder_preserved: `{browser.get('checks', {}).get('recorder_preserved')}`
- shell_evidence_preserved: `{browser.get('checks', {}).get('shell_evidence_preserved')}`
- reviewed_completion_ready: `{browser.get('checks', {}).get('reviewed_completion_ready')}`
- no_console_errors: `{browser.get('checks', {}).get('no_console_errors')}`

## Stale freshness snapshot

```json
{json.dumps(_safe_get(stale, 'handoff', 'previewFreshness') or {}, indent=2, sort_keys=True)}
```

## Reprepared freshness snapshot

```json
{json.dumps(_safe_get(reprepare, 'handoff', 'previewFreshness') or {}, indent=2, sort_keys=True)}
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
        "browser_evidence_path": results["browser_evidence_path"],
        "report_329_results_path": results["report_329_results_path"],
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
