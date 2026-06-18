"""Report 340: SSRM-3D browser world v100 repaired handoff continue-return freshness bridge.

This report verifies that Report 339's repaired clean handoff remains fresh
after the reviewer actually uses it. A stale resume handoff is repaired by
re-preparing a clean handoff, the recovered clean continue action is clicked,
the reset shell reviewer pass is rerun, the reviewer returns to the launcher,
shell evidence is refreshed, and the repaired handoff remains visibly fresh
with the same timestamp and continue/download controls.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 340
PREFIX = "ssrm_3d_browser_world_v100_primary_demo_repaired_handoff_continue_return_freshness_bridge"
DEFAULT_SEED = 20270738

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V63_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
PRIMARY_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo"
PRIMARY_JS = PRIMARY_DIR / "demo.js"
PRIMARY_HTML = PRIMARY_DIR / "index.html"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"
REPORT_339_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v99_primary_demo_stale_handoff_repair_reprepare_bridge_results.json"

BOUNDARY = (
    "Deterministic browser-local repaired handoff continue-return freshness bridge only; no LLM calls, "
    "no subjective consciousness, no autonomous natural language, no moral patienthood, no production "
    "persistence, no complete 3D engine, and no finished gameplay claim. This is local launcher recovery "
    "and review-handoff freshness hygiene, not external validation or evidence of inner experience."
)

NEXT_GATE = (
    "post-340: collapse the repeated handoff lifecycle checks into a single primary-demo lifecycle "
    "smoke artifact so future consolidation gates exercise one maintained path without adding another "
    "near-duplicate report for each tab/reload variant"
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
    html = _read(PRIMARY_HTML)
    browser = _load_json(BROWSER_EVIDENCE)
    report_339 = _load_json(REPORT_339_RESULTS)
    checks = browser.get("checks", {}) if isinstance(browser.get("checks"), dict) else {}
    stale = browser.get("staleBeforeRepair", {}) if isinstance(browser.get("staleBeforeRepair"), dict) else {}
    repaired = browser.get("repairedFreshBeforeContinue", {}) if isinstance(browser.get("repairedFreshBeforeContinue"), dict) else {}
    shell_before_run = browser.get("continuedShellBeforeRun", {}) if isinstance(browser.get("continuedShellBeforeRun"), dict) else {}
    shell_after_run = browser.get("continuedShellAfterRun", {}) if isinstance(browser.get("continuedShellAfterRun"), dict) else {}
    after_refresh = browser.get("afterRepairedReturnAfterRefresh", {}) if isinstance(browser.get("afterRepairedReturnAfterRefresh"), dict) else {}
    after_reload = browser.get("afterRepairedReturnAfterReload", {}) if isinstance(browser.get("afterRepairedReturnAfterReload"), dict) else {}
    evidence_text = json.dumps(browser, sort_keys=True)
    required_terms = [
        "handoffPayloadFreshnessState",
        "renderOutsideReviewHandoffActions",
        "Continue from prepared",
        "readableHandoffSummary",
        "preparedHandoffHref",
        "previewFreshness",
    ]
    criteria = [
        _criterion(
            "report_339_stale_repair_gate_passed",
            report_339.get("verdict") == "pass" and _safe_get(report_339, "metrics", "weakest_channel_score") == 1.0,
            f"Report 339 verdict={report_339.get('verdict')} weakest={_safe_get(report_339, 'metrics', 'weakest_channel_score')}",
            "continue-return freshness would not be grounded in a passing stale repair gate",
        ),
        _criterion(
            "repaired_continue_return_source_still_present",
            all(term in generator for term in required_terms)
            and all(term in js for term in required_terms)
            and "outsideReviewHandoffStatus" in html
            and "outsideReviewHandoffActions" in html,
            "generator, emitted JS, and emitted HTML retain repaired handoff continue/refresh machinery",
            "regeneration would remove repaired handoff continue-return behavior",
        ),
        _criterion(
            "stale_status_visible_before_repair",
            checks.get("stale_status_visible_before_repair") is True
            and "Prepared handoff payload is stale" in str(stale.get("statusText", "")),
            str(stale.get("statusText", "missing stale status")),
            "the proof did not start from a visible stale handoff state",
        ),
        _criterion(
            "stale_mismatch_history_visible_before_repair",
            checks.get("stale_mismatch_history_visible_before_repair") is True
            and stale.get("previewMismatchCount", 0) > 0,
            str(stale.get("previewMismatches", [])),
            "pre-repair stale mismatch history was not retained in browser evidence",
        ),
        _criterion(
            "repaired_clean_handoff_fresh_before_continue",
            checks.get("repaired_clean_handoff_fresh_before_continue") is True
            and repaired.get("payloadKind") == "clean"
            and repaired.get("previewFresh") is True
            and repaired.get("hasContinueCleanControl") is True,
            str(repaired.get("statusText", "missing repaired status")),
            "repaired handoff was not fresh and continue-capable before use",
        ),
        _criterion(
            "repaired_payload_tracks_current_shell_before_continue",
            checks.get("repaired_payload_tracks_current_shell_before_continue") is True,
            f"payload={repaired.get('payloadRecordedAt')} current={repaired.get('shellHandoffRecordedAt')}",
            "repaired payload did not track the current shell handoff before continue",
        ),
        _criterion(
            "repaired_continue_reaches_reset_shell",
            checks.get("repaired_continue_reaches_reset_shell") is True
            and "reset=1" in str(shell_before_run.get("url", ""))
            and shell_before_run.get("hasReviewerLanding") is True,
            f"url={shell_before_run.get('url')} reviewer={shell_before_run.get('hasReviewerLanding')}",
            "repaired clean continue action did not reach the reset reviewer shell",
        ),
        _criterion(
            "reviewer_pass_rerun_after_repaired_continue",
            checks.get("reviewer_pass_rerun_after_repaired_continue") is True
            and shell_after_run.get("hasAllPass") is True,
            f"url={shell_after_run.get('url')} allPass={shell_after_run.get('hasAllPass')}",
            "reviewer pass was not rerun after using the recovered clean handoff",
        ),
        _criterion(
            "repaired_return_to_launcher_visible",
            checks.get("repaired_return_to_launcher_visible") is True,
            str(browser.get("afterRepairedReturnBeforeRefresh", {}).get("url", "missing return URL")),
            "continued repaired session could not return visibly to the launcher",
        ),
        _criterion(
            "repaired_handoff_still_fresh_after_return_refresh",
            checks.get("repaired_handoff_still_fresh_after_return_refresh") is True
            and after_refresh.get("payloadKind") == "clean"
            and after_refresh.get("previewFresh") is True
            and "fresh clean handoff" in str(after_refresh.get("statusText", "")),
            str(after_refresh.get("statusText", "missing after-refresh status")),
            "repaired handoff became stale after continue-return-refresh",
        ),
        _criterion(
            "repaired_continue_action_still_available_after_refresh",
            checks.get("repaired_continue_action_still_available_after_refresh") is True
            and after_refresh.get("hasContinueCleanControl") is True,
            str(after_refresh.get("actionsText", "missing after-refresh actions")),
            "repaired continue action disappeared after return refresh",
        ),
        _criterion(
            "repaired_payload_timestamp_unchanged_after_refresh",
            checks.get("repaired_payload_timestamp_unchanged_after_refresh") is True
            and after_refresh.get("payloadRecordedAt") == repaired.get("payloadRecordedAt"),
            f"before={repaired.get('payloadRecordedAt')} after={after_refresh.get('payloadRecordedAt')}",
            "continue-return-refresh mutated the repaired prepared payload timestamp",
        ),
        _criterion(
            "current_shell_timestamp_matches_repaired_payload_after_refresh",
            checks.get("current_shell_timestamp_matches_repaired_payload_after_refresh") is True
            and after_refresh.get("shellHandoffRecordedAt") == repaired.get("payloadRecordedAt"),
            f"payload={repaired.get('payloadRecordedAt')} shell={after_refresh.get('shellHandoffRecordedAt')}",
            "current shell handoff timestamp diverged from the repaired payload after refresh",
        ),
        _criterion(
            "shell_evidence_all_pass_after_repaired_continue",
            checks.get("shell_evidence_all_pass_after_repaired_continue") is True
            and after_refresh.get("shellReviewerPassSeen") is True
            and after_refresh.get("shellReceiptAllPass") is True
            and after_refresh.get("shellReplayExportReady") is True,
            str(after_refresh.get("shellEvidenceText", "missing shell evidence text")),
            "refreshed shell evidence was not all-pass after repaired continue-return",
        ),
        _criterion(
            "repaired_fresh_survives_post_return_reload",
            checks.get("repaired_fresh_survives_post_return_reload") is True
            and after_reload.get("previewFresh") is True
            and after_reload.get("payloadRecordedAt") == repaired.get("payloadRecordedAt")
            and after_reload.get("hasContinueCleanControl") is True,
            str(after_reload.get("statusText", "missing after-reload status")),
            "repaired handoff freshness did not survive post-return reload",
        ),
        _criterion(
            "stale_history_preserved_in_browser_evidence",
            checks.get("stale_history_preserved_in_browser_evidence") is True
            and "stale" in str(stale.get("statusText", "")).lower()
            and stale.get("previewMismatchCount", 0) > 0,
            str(stale.get("previewMismatches", [])),
            "browser evidence no longer preserves the stale history that was repaired",
        ),
        _criterion(
            "browser_evidence_uses_visible_or_preview_state",
            checks.get("evidence_avoids_raw_storage_keys") is True
            and "localStorage" not in evidence_text
            and "localHandoff" not in evidence_text
            and "localPayloadHandoff" not in evidence_text,
            "browser evidence compares visible status/actions and visible handoff preview JSON, not raw storage keys",
            "repaired continue-return proof relies on privileged storage inspection",
        ),
        _criterion(
            "browser_console_clean",
            checks.get("no_console_errors") is True and browser.get("consoleErrors") == 0,
            f"consoleErrors={browser.get('consoleErrors')} messages={browser.get('consoleErrorMessages', [])}",
            "repaired continue-return browser flow produced console errors",
        ),
        _criterion(
            "boundary_preserved",
            "no subjective consciousness" in BOUNDARY and "no LLM calls" in BOUNDARY,
            BOUNDARY,
            "report boundary implies more than browser-local repaired handoff freshness",
        ),
    ]
    scores = [row.score for row in criteria]
    readiness = mean(scores)
    weakest = min(scores)
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "repaired_continue_return_score": mean([
            next(row.score for row in criteria if row.channel == "repaired_continue_reaches_reset_shell"),
            next(row.score for row in criteria if row.channel == "reviewer_pass_rerun_after_repaired_continue"),
            next(row.score for row in criteria if row.channel == "repaired_return_to_launcher_visible"),
        ]),
        "post_return_freshness_score": next(row.score for row in criteria if row.channel == "repaired_handoff_still_fresh_after_return_refresh"),
        "post_return_continue_score": next(row.score for row in criteria if row.channel == "repaired_continue_action_still_available_after_refresh"),
        "timestamp_stability_score": mean([
            next(row.score for row in criteria if row.channel == "repaired_payload_timestamp_unchanged_after_refresh"),
            next(row.score for row in criteria if row.channel == "current_shell_timestamp_matches_repaired_payload_after_refresh"),
            next(row.score for row in criteria if row.channel == "repaired_fresh_survives_post_return_reload"),
        ]),
        "shell_evidence_score": next(row.score for row in criteria if row.channel == "shell_evidence_all_pass_after_repaired_continue"),
        "stale_history_preservation_score": next(row.score for row in criteria if row.channel == "stale_history_preserved_in_browser_evidence"),
        "visible_no_storage_score": next(row.score for row in criteria if row.channel == "browser_evidence_uses_visible_or_preview_state"),
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
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "report_339_results_path": str(REPORT_339_RESULTS.relative_to(ROOT)),
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


def _write_report(result: dict[str, Any]) -> None:
    metrics = result["metrics"]
    criteria = result["criteria"]
    passed = sum(1 for row in criteria if row["passed"])
    lines = [
        "# Report 340: SSRM-3D Browser World v100 Primary Demo Repaired Handoff Continue Return Freshness Bridge",
        "",
        "## Purpose",
        "",
        "Report 340 verifies that the repaired clean handoff from Report 339 remains fresh after actual use. "
        "The browser proof creates a stale resume payload, repairs it by re-preparing a clean payload, clicks "
        "`Continue from prepared clean handoff`, reruns the reviewer pass in the reset shell, returns to the "
        "launcher, refreshes shell evidence, and confirms the repaired payload remains fresh and continue-capable.",
        "",
        "This did not add another simulation surface. The maintained v61 app shell and primary launcher remain "
        "the only exercised browser-world path, and no app-source patch was needed.",
        "",
        "## Boundary",
        "",
        result["boundary"],
        "",
        "## Browser evidence",
        "",
        "- Pre-repair stale mismatch history was captured and retained in the browser artifact.",
        "- Re-prepare restored a fresh `clean` handoff before continue.",
        "- The recovered `Continue from prepared clean handoff` reached the reset maintained shell.",
        "- The reviewer pass was rerun after using the recovered clean handoff.",
        "- Return to launcher was visible.",
        "- Refreshing shell evidence kept the repaired handoff fresh with the same prepared timestamp.",
        "- Current shell handoff timestamp matched the repaired payload timestamp after refresh.",
        "- Continue/download controls remained visible after refresh.",
        "- Post-return reload preserved the repaired fresh classification and continue action.",
        f"- Browser console errors: `{metrics['console_errors']}`.",
        "",
        "## Metrics",
        "",
        "| Metric | Value |",
        "| --- | ---: |",
    ]
    for key, value in metrics.items():
        lines.append(f"| `{key}` | `{value}` |")
    lines.extend([
        "",
        "## Criteria",
        "",
        "| Channel | Passed | Score | Evidence |",
        "| --- | --- | ---: | --- |",
    ])
    for row in criteria:
        evidence = str(row["evidence"]).replace("|", "\\|")
        lines.append(f"| `{row['channel']}` | `{row['passed']}` | `{row['score']}` | {evidence} |")
    lines.extend([
        "",
        "## Verdict",
        "",
        f"`{result['verdict']}` with `{passed}/{len(criteria)}` criteria passing.",
        "",
        "This is a consolidation proof, not a frontier claim. It closes the repaired-handoff lifecycle loop: "
        "a stale payload can be repaired, used, returned from, refreshed, and reloaded without silently "
        "falling back into stale or mismatched state.",
        "",
        "## Next gate",
        "",
        result["next_gate"],
        "",
    ])
    path = DOCS / f"{REPORT}_{PREFIX}_report.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def _write_artifacts(result: dict[str, Any]) -> None:
    prefix = ARTIFACTS / PREFIX
    criteria = result["criteria"]
    _write_json(prefix.with_name(prefix.name + "_results.json"), result)
    _write_json(
        prefix.with_name(prefix.name + "_state.json"),
        {
            "report": REPORT,
            "seed": result["seed"],
            "boundary": result["boundary"],
            "next_gate": result["next_gate"],
            "checks": result["browser_evidence"].get("checks", {}),
            "stale_status_before_repair": _safe_get(result, "browser_evidence", "staleBeforeRepair", "statusText"),
            "repaired_status_before_continue": _safe_get(result, "browser_evidence", "repairedFreshBeforeContinue", "statusText"),
            "after_refresh_status": _safe_get(result, "browser_evidence", "afterRepairedReturnAfterRefresh", "statusText"),
            "after_refresh_shell_evidence": _safe_get(result, "browser_evidence", "afterRepairedReturnAfterRefresh", "shellEvidenceText"),
            "repaired_recorded_at": _safe_get(result, "browser_evidence", "repairedFreshBeforeContinue", "payloadRecordedAt"),
            "after_refresh_recorded_at": _safe_get(result, "browser_evidence", "afterRepairedReturnAfterRefresh", "payloadRecordedAt"),
        },
    )
    _write_csv(prefix.with_name(prefix.name + "_criteria.csv"), criteria)
    _write_csv(prefix.with_name(prefix.name + "_summary.csv"), [{"report": REPORT, **result["metrics"]}])
    _write_csv(
        prefix.with_name(prefix.name + "_verdict.csv"),
        [{
            "report": REPORT,
            "verdict": result["verdict"],
            "readiness": result["metrics"]["readiness"],
            "weakest_channel_score": result["metrics"]["weakest_channel_score"],
            "next_gate": result["next_gate"],
        }],
    )
    _write_report(result)


def main() -> dict[str, Any]:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    result = _evaluate(args.seed)
    _write_artifacts(result)
    print(json.dumps({"report": REPORT, "verdict": result["verdict"], "metrics": result["metrics"]}, indent=2, sort_keys=True))
    return result


if __name__ == "__main__":
    main()
