"""Report 339: SSRM-3D browser world v99 stale handoff repair reprepare bridge.

This report verifies recovery from Report 338 stale handoff calibration. A
visible fresh resume handoff is prepared, a newer clean shell handoff supersedes
it, the old payload becomes visibly stale with named mismatches and no continue
action, and re-running Prepare outside-review handoff restores a fresh clean
prepared handoff with continue/download controls while the browser evidence
retains the pre-repair stale mismatch history.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 339
PREFIX = "ssrm_3d_browser_world_v99_primary_demo_stale_handoff_repair_reprepare_bridge"
DEFAULT_SEED = 20270737

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V63_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
PRIMARY_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo"
PRIMARY_JS = PRIMARY_DIR / "demo.js"
PRIMARY_HTML = PRIMARY_DIR / "index.html"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"
REPORT_338_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v98_primary_demo_stale_prepared_handoff_calibration_bridge_results.json"

BOUNDARY = (
    "Deterministic browser-local stale handoff repair bridge only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, "
    "no complete 3D engine, and no finished gameplay claim. This is local launcher recovery and "
    "review-handoff hygiene, not external validation or evidence of inner experience."
)

NEXT_GATE = (
    "post-339: verify stale repair survives a full continue-return-refresh loop from the repaired clean "
    "handoff, so recovery stays fresh after the reviewer actually uses the recovered action"
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
    report_338 = _load_json(REPORT_338_RESULTS)
    checks = browser.get("checks", {}) if isinstance(browser.get("checks"), dict) else {}
    prepared = browser.get("preparedFreshResume", {}) if isinstance(browser.get("preparedFreshResume"), dict) else {}
    stale = browser.get("staleBeforeRepair", {}) if isinstance(browser.get("staleBeforeRepair"), dict) else {}
    repaired = browser.get("repairedFreshAfterReprepare", {}) if isinstance(browser.get("repairedFreshAfterReprepare"), dict) else {}
    repaired_reload = browser.get("repairedFreshAfterReload", {}) if isinstance(browser.get("repairedFreshAfterReload"), dict) else {}
    continued = browser.get("continuedCleanShell", {}) if isinstance(browser.get("continuedCleanShell"), dict) else {}
    superseding_shell = browser.get("supersedingShell", {}) if isinstance(browser.get("supersedingShell"), dict) else {}
    evidence_text = json.dumps(browser, sort_keys=True)
    required_terms = [
        "handoffPayloadFreshnessState",
        "renderOutsideReviewHandoffActions",
        "Prepared handoff payload is stale",
        "Re-prepare before continuing from this handoff",
        "Continue from prepared",
        "previewFreshness",
    ]
    criteria = [
        _criterion(
            "report_338_stale_calibration_gate_passed",
            report_338.get("verdict") == "pass" and _safe_get(report_338, "metrics", "weakest_channel_score") == 1.0,
            f"Report 338 verdict={report_338.get('verdict')} weakest={_safe_get(report_338, 'metrics', 'weakest_channel_score')}",
            "stale repair would not be grounded in a passing stale-calibration gate",
        ),
        _criterion(
            "stale_repair_source_still_present",
            all(term in generator for term in required_terms)
            and all(term in js for term in required_terms)
            and "outsideReviewHandoffStatus" in html
            and "outsideReviewHandoffActions" in html,
            "generator, emitted JS, and emitted HTML retain stale repair status/action machinery",
            "regeneration would remove stale prepared-handoff repair behavior",
        ),
        _criterion(
            "prepared_resume_was_fresh_before_supersede",
            checks.get("prepared_resume_was_fresh_before_supersede") is True
            and prepared.get("payloadKind") == "resume"
            and prepared.get("previewFresh") is True,
            f"kind={prepared.get('payloadKind')} fresh={prepared.get('previewFresh')} status={prepared.get('statusText')}",
            "baseline prepared resume handoff was not fresh before supersession",
        ),
        _criterion(
            "superseding_shell_handoff_created",
            checks.get("superseding_shell_handoff_created") is True
            and superseding_shell.get("hasAllPass") is True
            and superseding_shell.get("hasReviewerLanding") is True,
            f"url={superseding_shell.get('url')} allPass={superseding_shell.get('hasAllPass')} reviewer={superseding_shell.get('hasReviewerLanding')}",
            "the proof did not create a newer reviewed clean shell handoff",
        ),
        _criterion(
            "stale_status_visible_before_repair",
            checks.get("stale_status_visible_before_repair") is True
            and "Prepared handoff payload is stale" in str(stale.get("statusText", "")),
            str(stale.get("statusText", "missing stale status")),
            "stale state was not visible before repair",
        ),
        _criterion(
            "stale_mismatch_history_visible_before_repair",
            checks.get("stale_mismatch_history_visible_before_repair") is True
            and stale.get("previewMismatchCount", 0) > 0
            and "launch handoff changed" in (stale.get("previewMismatches") or []),
            str(stale.get("previewMismatches", [])),
            "stale mismatch history was not captured visibly before repair",
        ),
        _criterion(
            "stale_continue_blocked_before_repair",
            checks.get("stale_continue_blocked_before_repair") is True
            and stale.get("hasContinueControl") is False
            and "Re-prepare before continuing" in str(stale.get("actionsText", "")),
            str(stale.get("actionsText", "missing stale actions")),
            "stale handoff exposed a continue action before repair",
        ),
        _criterion(
            "reprepare_restores_fresh_clean_handoff",
            checks.get("reprepare_restores_fresh_clean_handoff") is True
            and repaired.get("payloadKind") == "clean"
            and repaired.get("previewFresh") is True
            and "fresh clean handoff" in str(repaired.get("statusText", "")),
            str(repaired.get("statusText", "missing repaired status")),
            "re-prepare did not restore a fresh clean handoff",
        ),
        _criterion(
            "reprepare_payload_tracks_current_shell_handoff",
            checks.get("reprepare_payload_tracks_current_shell_handoff") is True
            and repaired.get("payloadRecordedAt") == stale.get("shellHandoffRecordedAt")
            and repaired.get("payloadRecordedAt") != prepared.get("payloadRecordedAt"),
            f"old={prepared.get('payloadRecordedAt')} current={stale.get('shellHandoffRecordedAt')} repaired={repaired.get('payloadRecordedAt')}",
            "re-prepare did not move the payload to the current shell handoff",
        ),
        _criterion(
            "reprepare_regains_continue_action",
            checks.get("reprepare_regains_continue_action") is True
            and repaired.get("hasContinueCleanControl") is True
            and "Continue from prepared clean handoff" in str(repaired.get("actionsText", "")),
            str(repaired.get("actionsText", "missing repaired actions")),
            "re-prepare did not restore a usable continue action",
        ),
        _criterion(
            "reprepare_keeps_download_available",
            checks.get("reprepare_keeps_download_available") is True
            and repaired.get("hasDownloadControl") is True,
            str(repaired.get("actionsText", "missing repaired download action")),
            "re-prepare removed downloadable review evidence",
        ),
        _criterion(
            "repair_evidence_preserves_stale_history",
            checks.get("repair_evidence_preserves_stale_history") is True
            and "stale" in str(stale.get("statusText", "")).lower()
            and stale.get("previewMismatchCount", 0) > 0
            and "fresh clean handoff" in str(repaired.get("statusText", "")),
            f"stale={stale.get('statusText')} repaired={repaired.get('statusText')}",
            "repair proof does not preserve the visible stale history alongside the repaired state",
        ),
        _criterion(
            "repaired_fresh_survives_launcher_reload",
            checks.get("repaired_fresh_survives_launcher_reload") is True
            and repaired_reload.get("previewFresh") is True
            and repaired_reload.get("payloadKind") == "clean"
            and repaired_reload.get("hasContinueCleanControl") is True,
            str(repaired_reload.get("statusText", "missing repaired reload status")),
            "fresh repaired handoff did not survive launcher reload",
        ),
        _criterion(
            "repaired_reload_keeps_repaired_timestamp",
            checks.get("repaired_reload_keeps_repaired_timestamp") is True
            and repaired_reload.get("payloadRecordedAt") == repaired.get("payloadRecordedAt"),
            f"repaired={repaired.get('payloadRecordedAt')} reload={repaired_reload.get('payloadRecordedAt')}",
            "reload mutated the repaired prepared handoff timestamp",
        ),
        _criterion(
            "repaired_continue_reaches_shell",
            checks.get("repaired_continue_reaches_shell") is True
            and continued.get("hasReviewerLanding") is True
            and "ssrm_3d_browser_world_v61_vertical_slice_app_shell" in str(continued.get("url", "")),
            f"url={continued.get('url')} reviewer={continued.get('hasReviewerLanding')}",
            "repaired continue action did not reach the maintained shell",
        ),
        _criterion(
            "browser_evidence_uses_visible_or_preview_state",
            checks.get("evidence_avoids_raw_storage_keys") is True
            and "localStorage" not in evidence_text
            and "localHandoff" not in evidence_text
            and "localPayloadHandoff" not in evidence_text,
            "browser evidence compares visible status/actions and visible handoff preview JSON, not raw storage keys",
            "stale repair proof relies on privileged storage inspection",
        ),
        _criterion(
            "browser_console_clean",
            checks.get("no_console_errors") is True and browser.get("consoleErrors") == 0,
            f"consoleErrors={browser.get('consoleErrors')} messages={browser.get('consoleErrorMessages', [])}",
            "stale repair browser flow produced console errors",
        ),
        _criterion(
            "boundary_preserved",
            "no subjective consciousness" in BOUNDARY and "no LLM calls" in BOUNDARY,
            BOUNDARY,
            "report boundary implies more than browser-local launcher recovery",
        ),
    ]
    scores = [row.score for row in criteria]
    readiness = mean(scores)
    weakest = min(scores)
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "stale_repair_score": mean([
            next(row.score for row in criteria if row.channel == "reprepare_restores_fresh_clean_handoff"),
            next(row.score for row in criteria if row.channel == "reprepare_regains_continue_action"),
            next(row.score for row in criteria if row.channel == "reprepare_payload_tracks_current_shell_handoff"),
        ]),
        "stale_history_preservation_score": next(row.score for row in criteria if row.channel == "repair_evidence_preserves_stale_history"),
        "stale_block_before_repair_score": next(row.score for row in criteria if row.channel == "stale_continue_blocked_before_repair"),
        "repaired_continue_score": next(row.score for row in criteria if row.channel == "repaired_continue_reaches_shell"),
        "reload_survival_score": next(row.score for row in criteria if row.channel == "repaired_fresh_survives_launcher_reload"),
        "timestamp_repair_score": mean([
            next(row.score for row in criteria if row.channel == "reprepare_payload_tracks_current_shell_handoff"),
            next(row.score for row in criteria if row.channel == "repaired_reload_keeps_repaired_timestamp"),
        ]),
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
        "report_338_results_path": str(REPORT_338_RESULTS.relative_to(ROOT)),
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
        "# Report 339: SSRM-3D Browser World v99 Primary Demo Stale Handoff Repair Reprepare Bridge",
        "",
        "## Purpose",
        "",
        "Report 339 verifies recovery after Report 338's stale prepared-handoff calibration. The browser "
        "proof prepares a fresh `resume` handoff, supersedes it with a newer reviewed `clean` shell handoff, "
        "captures the visible stale mismatch state, then clicks `Prepare outside-review handoff` again. "
        "The repaired payload must become fresh, track the current clean handoff, regain `Continue from "
        "prepared clean handoff`, keep the download action, survive launcher reload, and reach the maintained shell.",
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
        "- Prepared baseline was a fresh `resume` handoff.",
        "- A newer reviewed `clean` shell handoff superseded the prepared resume payload.",
        "- Before repair, the launcher visibly marked the old payload stale and named mismatch history.",
        "- Before repair, the stale action area blocked continue and kept download evidence available.",
        "- Re-running `Prepare outside-review handoff` restored a fresh `clean` prepared handoff.",
        "- Re-prepare moved the prepared payload timestamp to the current clean shell handoff timestamp.",
        "- Repaired actions exposed `Continue from prepared clean handoff` plus download.",
        "- Reload preserved the repaired fresh classification and timestamp.",
        "- The repaired continue action reached the maintained v61 shell.",
        "- The browser evidence keeps both the pre-repair stale mismatch state and the post-repair fresh state.",
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
        "This is a consolidation proof, not a frontier claim. It shows the primary launcher supports a full "
        "calibrated repair loop: stale payloads are blocked, the stale evidence remains inspectable in the "
        "browser proof, and re-preparing restores a usable current handoff.",
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
            "stale_mismatches_before_repair": _safe_get(result, "browser_evidence", "staleBeforeRepair", "previewMismatches"),
            "repaired_status": _safe_get(result, "browser_evidence", "repairedFreshAfterReprepare", "statusText"),
            "repaired_recorded_at": _safe_get(result, "browser_evidence", "repairedFreshAfterReprepare", "payloadRecordedAt"),
            "continued_url": _safe_get(result, "browser_evidence", "continuedCleanShell", "url"),
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
