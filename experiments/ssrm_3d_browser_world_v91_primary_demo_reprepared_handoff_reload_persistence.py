"""Report 331: SSRM-3D browser world v91 re-prepared handoff reload persistence.

This report verifies that a resume handoff re-prepared after stale-payload recovery
survives another launcher reload and remains inspectable from persisted browser-local
state rather than only transient page memory.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 331
PREFIX = "ssrm_3d_browser_world_v91_primary_demo_reprepared_handoff_reload_persistence"
DEFAULT_SEED = 20270729

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V63_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
PRIMARY_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo"
PRIMARY_JS = PRIMARY_DIR / "demo.js"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"
REPORT_330_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v90_primary_demo_stale_handoff_reprepare_continuity_results.json"

BOUNDARY = (
    "Deterministic browser-local re-prepared handoff reload persistence only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, no "
    "complete 3D engine, and no finished gameplay claim. This is local review-evidence persistence hygiene, "
    "not external validation or evidence of inner experience."
)

NEXT_GATE = (
    "post-331: reduce cold-reviewer restart friction by checking whether the persisted re-prepared handoff "
    "is readable and actionable without requiring privileged JSON inspection"
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
    report_330 = _load_json(REPORT_330_RESULTS)
    checks = browser.get("checks", {}) if isinstance(browser.get("checks"), dict) else {}
    stale = browser.get("staleAfterResumeState", {}) if isinstance(browser.get("staleAfterResumeState"), dict) else {}
    reprepare_before = browser.get("rePreparedBeforeReloadState", {}) if isinstance(browser.get("rePreparedBeforeReloadState"), dict) else {}
    persisted = browser.get("persistedAfterReloadState", {}) if isinstance(browser.get("persistedAfterReloadState"), dict) else {}
    persisted_handoff = persisted.get("handoff", {}) if isinstance(persisted.get("handoff"), dict) else {}
    persisted_freshness = persisted_handoff.get("previewFreshness", {}) if isinstance(persisted_handoff.get("previewFreshness"), dict) else {}
    shell_evidence = persisted_handoff.get("shellEvidence", {}) if isinstance(persisted_handoff.get("shellEvidence"), dict) else {}
    completion = persisted_handoff.get("reviewedHandoffCompletion", {}) if isinstance(persisted_handoff.get("reviewedHandoffCompletion"), dict) else {}
    recorder_export = persisted_handoff.get("recorderExport", {}) if isinstance(persisted_handoff.get("recorderExport"), dict) else {}
    manual_records = persisted_handoff.get("manualRecords", []) if isinstance(persisted_handoff.get("manualRecords"), list) else []
    checklist_items = _safe_get(persisted_handoff, "checklistState", "items") or {}
    required_terms = [
        "handoffPayloadFreshnessState",
        "previewFreshness",
        "Prepared handoff payload is stale",
        "renderOutsideReviewHandoffPreview",
        "reviewedHandoffCompletion",
    ]
    criteria = [
        _criterion(
            "report_330_reprepare_gate_passed",
            report_330.get("verdict") == "pass" and _safe_get(report_330, "metrics", "weakest_channel_score") == 1.0,
            f"Report 330 verdict={report_330.get('verdict')} weakest={_safe_get(report_330, 'metrics', 'weakest_channel_score')}",
            "Report 331 would not be grounded in a passing reprepare-continuity gate",
        ),
        _criterion(
            "freshness_source_still_present",
            all(term in generator for term in required_terms) and all(term in js for term in required_terms),
            "primary launcher generator and emitted JS still contain freshness preview and completion terms",
            "reload persistence evidence could be tied to stale generated assets",
        ),
        _criterion(
            "clean_payload_fresh_before_resume",
            checks.get("clean_payload_fresh_before_resume") is True,
            str(_safe_get(browser, "cleanPreparedState", "handoff", "previewFreshness") or "missing clean freshness evidence"),
            "the baseline clean handoff was not fresh before the reload/resume path",
        ),
        _criterion(
            "stale_warning_seen_before_reprepare",
            checks.get("stale_warning_visible_after_resume_refresh") is True and stale.get("bodyHasStaleWarning") is True,
            f"bodyHasStaleWarning={stale.get('bodyHasStaleWarning')} bodyHasReRunWarning={stale.get('bodyHasReRunWarning')}",
            "the test did not actually pass through the stale-payload recovery path",
        ),
        _criterion(
            "reprepare_fresh_before_reload",
            checks.get("reprepare_payload_fresh_before_reload") is True
            and _safe_get(reprepare_before, "handoff", "previewFreshness", "fresh") is True,
            str(_safe_get(reprepare_before, "handoff", "previewFreshness") or "missing reprepare freshness"),
            "the payload was not fresh before the persistence reload",
        ),
        _criterion(
            "reprepare_resume_before_reload",
            checks.get("reprepare_payload_uses_resume_before_reload") is True
            and _safe_get(reprepare_before, "handoff", "handoff", "kind") == "resume",
            f"handoffKind={_safe_get(reprepare_before, 'handoff', 'handoff', 'kind')} shellKind={_safe_get(reprepare_before, 'handoff', 'shellEvidence', 'handoff', 'kind')}",
            "the re-prepared payload was not the current resume handoff before reload",
        ),
        _criterion(
            "persisted_payload_visible_after_reload",
            checks.get("persisted_payload_visible_after_reload") is True and isinstance(persisted_handoff, dict) and bool(persisted_handoff),
            f"bodyHasNoHandoffText={persisted.get('bodyHasNoHandoffText')} parsedBoundaryCount={persisted.get('parsedBoundaryCount')}",
            "another launcher reload loses the prepared handoff preview",
        ),
        _criterion(
            "persisted_payload_fresh_after_reload",
            checks.get("persisted_payload_fresh_after_reload") is True
            and persisted_freshness.get("fresh") is True
            and persisted_freshness.get("mismatches") == [],
            str(persisted_freshness),
            "the reloaded persisted payload is stale or carries freshness mismatches",
        ),
        _criterion(
            "persisted_payload_uses_resume_after_reload",
            checks.get("persisted_payload_uses_resume_after_reload") is True
            and _safe_get(persisted_handoff, "handoff", "kind") == "resume"
            and _safe_get(shell_evidence, "handoff", "kind") == "resume",
            f"payload={_safe_get(persisted_handoff, 'handoff', 'kind')} shell={_safe_get(shell_evidence, 'handoff', 'kind')}",
            "the persisted payload falls back to the old clean handoff after reload",
        ),
        _criterion(
            "persisted_completion_ready_after_reload",
            checks.get("persisted_completion_ready_after_reload") is True and completion.get("ready") is True,
            f"completionReady={completion.get('ready')} completionShellKind={_safe_get(completion, 'shellEvidence', 'handoff', 'kind')}",
            "reviewed handoff completion readiness is lost after reload",
        ),
        _criterion(
            "persisted_checklist_after_reload",
            checks.get("persisted_checklist_after_reload") is True and _count_true_items(checklist_items) == 7,
            f"completed checklist items={_count_true_items(checklist_items)}",
            "completed outside-review checklist state is lost after reload",
        ),
        _criterion(
            "persisted_recorder_after_reload",
            checks.get("persisted_recorder_after_reload") is True and len(manual_records) == 1 and recorder_export.get("recordCount") == 1,
            f"manualRecords={len(manual_records)} recorderExportRecordCount={recorder_export.get('recordCount')}",
            "manual recorder evidence is lost after reload",
        ),
        _criterion(
            "persisted_shell_evidence_after_reload",
            checks.get("persisted_shell_evidence_after_reload") is True
            and shell_evidence.get("reviewerPassSeen") is True
            and shell_evidence.get("receiptAllPass") is True
            and shell_evidence.get("replayExportReady") is True,
            f"reviewerPassSeen={shell_evidence.get('reviewerPassSeen')} receiptAllPass={shell_evidence.get('receiptAllPass')} replayExportReady={shell_evidence.get('replayExportReady')}",
            "reviewer pass, all-pass receipt, or replay export evidence is lost after reload",
        ),
        _criterion(
            "no_stale_warning_after_reload",
            checks.get("no_stale_warning_after_reload") is True
            and persisted.get("bodyHasStaleWarning") is False
            and persisted.get("bodyHasReRunWarning") is False,
            f"bodyHasStaleWarning={persisted.get('bodyHasStaleWarning')} bodyHasReRunWarning={persisted.get('bodyHasReRunWarning')}",
            "a successful reprepare still looks stale after another reload",
        ),
        _criterion(
            "browser_console_clean",
            checks.get("no_console_errors") is True and browser.get("consoleErrors") == 0,
            f"consoleErrors={browser.get('consoleErrors')} messages={browser.get('consoleErrorMessages', [])}",
            "reload-persistence browser flow produced console errors",
        ),
        _criterion(
            "boundary_preserved",
            "no subjective consciousness" in BOUNDARY and "no LLM calls" in BOUNDARY,
            BOUNDARY,
            "report boundary implies more than browser-local review-evidence persistence",
        ),
    ]
    scores = [row.score for row in criteria]
    readiness = mean(scores)
    weakest = min(scores)
    verdict = "pass" if readiness >= 0.95 and weakest >= 0.9 and all(row.passed for row in criteria) else "needs_followup"
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "reload_persistence_score": next(row.score for row in criteria if row.channel == "persisted_payload_fresh_after_reload"),
        "resume_payload_integrity_score": next(row.score for row in criteria if row.channel == "persisted_payload_uses_resume_after_reload"),
        "continuity_persistence_score": mean([
            next(row.score for row in criteria if row.channel == "persisted_completion_ready_after_reload"),
            next(row.score for row in criteria if row.channel == "persisted_checklist_after_reload"),
            next(row.score for row in criteria if row.channel == "persisted_recorder_after_reload"),
            next(row.score for row in criteria if row.channel == "persisted_shell_evidence_after_reload"),
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
        "report_330_results_path": str(REPORT_330_RESULTS.relative_to(ROOT)),
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
    persisted = browser.get("persistedAfterReloadState", {}) if isinstance(browser.get("persistedAfterReloadState"), dict) else {}
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 331: SSRM-3D Browser World v91 Primary Demo Reprepared Handoff Reload Persistence

## Purpose

Report 331 follows the Report 330 recovery path with one more persistence check. A cold browser run prepared a clean handoff, forced the stale state through reload plus `Resume demo`, re-ran `Prepare outside-review handoff`, then reloaded the launcher again. The persisted re-prepared payload remained visible, fresh, and bound to the current `resume` launch handoff after the final reload.

No launcher behavior change was needed. The existing handoff persistence and freshness preview now have browser evidence for the full recovery path across a second reload.

## Boundary

{results['boundary']}

## Browser path

- Clean launch through the primary demo launcher on a fresh localhost origin.
- `Run reviewer pass` inside the maintained v61 shell.
- Return to launcher handoff, complete OR-01..OR-07, record one MP-03 pass, prepare recorder export, complete reviewed handoff, and prepare the clean payload.
- Reload, use `Resume demo`, return, refresh shell evidence, and observe stale clean-payload warning.
- Re-run `Prepare outside-review handoff` so the payload switches to the current resume handoff.
- Reload the launcher again.
- Confirm the persisted payload is still visible, fresh, resume-bound, checklist-complete, recorder-preserving, shell-evidence-preserving, completion-ready, and console-clean.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| reload_persistence_score | {metrics['reload_persistence_score']:.6f} |
| resume_payload_integrity_score | {metrics['resume_payload_integrity_score']:.6f} |
| continuity_persistence_score | {metrics['continuity_persistence_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence summary

- clean_payload_fresh_before_resume: `{browser.get('checks', {}).get('clean_payload_fresh_before_resume')}`
- stale_warning_visible_after_resume_refresh: `{browser.get('checks', {}).get('stale_warning_visible_after_resume_refresh')}`
- reprepare_payload_fresh_before_reload: `{browser.get('checks', {}).get('reprepare_payload_fresh_before_reload')}`
- reprepare_payload_uses_resume_before_reload: `{browser.get('checks', {}).get('reprepare_payload_uses_resume_before_reload')}`
- persisted_payload_visible_after_reload: `{browser.get('checks', {}).get('persisted_payload_visible_after_reload')}`
- persisted_payload_fresh_after_reload: `{browser.get('checks', {}).get('persisted_payload_fresh_after_reload')}`
- persisted_payload_uses_resume_after_reload: `{browser.get('checks', {}).get('persisted_payload_uses_resume_after_reload')}`
- persisted_completion_ready_after_reload: `{browser.get('checks', {}).get('persisted_completion_ready_after_reload')}`
- persisted_checklist_after_reload: `{browser.get('checks', {}).get('persisted_checklist_after_reload')}`
- persisted_recorder_after_reload: `{browser.get('checks', {}).get('persisted_recorder_after_reload')}`
- persisted_shell_evidence_after_reload: `{browser.get('checks', {}).get('persisted_shell_evidence_after_reload')}`
- no_stale_warning_after_reload: `{browser.get('checks', {}).get('no_stale_warning_after_reload')}`
- no_console_errors: `{browser.get('checks', {}).get('no_console_errors')}`

## Persisted freshness after reload

```json
{json.dumps(_safe_get(persisted, 'handoff', 'previewFreshness') or {}, indent=2, sort_keys=True)}
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
        "report_330_results_path": results["report_330_results_path"],
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
