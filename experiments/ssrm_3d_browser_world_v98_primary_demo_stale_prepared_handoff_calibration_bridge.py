"""Report 338: SSRM-3D browser world v98 stale prepared-handoff calibration bridge.

This report verifies that prepared handoff continuity is calibrated rather than
paranoid or blindly permissive. A visible fresh resume handoff is prepared, then
a newer clean shell handoff supersedes it. The launcher must classify the old
prepared payload as stale, expose mismatch evidence, block the stale continue
action, keep download/review evidence available, and preserve the stale
classification after reload without raw storage inspection.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 338
PREFIX = "ssrm_3d_browser_world_v98_primary_demo_stale_prepared_handoff_calibration_bridge"
DEFAULT_SEED = 20270736

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V63_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
PRIMARY_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo"
PRIMARY_JS = PRIMARY_DIR / "demo.js"
PRIMARY_HTML = PRIMARY_DIR / "index.html"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"
REPORT_337_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v97_primary_demo_closed_origin_tab_hard_reload_handoff_continuity_bridge_results.json"

BOUNDARY = (
    "Deterministic browser-local stale prepared-handoff calibration bridge only; no LLM calls, no "
    "subjective consciousness, no autonomous natural language, no moral patienthood, no production "
    "persistence, no complete 3D engine, and no finished gameplay claim. This is local launcher "
    "freshness judgment and review-handoff hygiene, not external validation or evidence of inner experience."
)

NEXT_GATE = (
    "post-338: verify stale prepared handoff repair by re-preparing after supersession, so reviewers can "
    "recover from a stale payload and regain a fresh continue action without losing visible mismatch history"
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
    report_337 = _load_json(REPORT_337_RESULTS)
    checks = browser.get("checks", {}) if isinstance(browser.get("checks"), dict) else {}
    prepared = browser.get("preparedFreshResume", {}) if isinstance(browser.get("preparedFreshResume"), dict) else {}
    stale = browser.get("staleAfterSupersede", {}) if isinstance(browser.get("staleAfterSupersede"), dict) else {}
    stale_reload = browser.get("staleAfterReload", {}) if isinstance(browser.get("staleAfterReload"), dict) else {}
    superseding_shell = browser.get("supersedingShell", {}) if isinstance(browser.get("supersedingShell"), dict) else {}
    evidence_text = json.dumps(browser, sort_keys=True)
    required_terms = [
        "handoffPayloadFreshnessState",
        "renderOutsideReviewHandoffActions",
        "Prepared handoff payload is stale",
        "Re-prepare before continuing from this handoff",
        "freshness.mismatches",
        "previewFreshness",
    ]
    criteria = [
        _criterion(
            "report_337_hard_reload_gate_passed",
            report_337.get("verdict") == "pass" and _safe_get(report_337, "metrics", "weakest_channel_score") == 1.0,
            f"Report 337 verdict={report_337.get('verdict')} weakest={_safe_get(report_337, 'metrics', 'weakest_channel_score')}",
            "stale calibration would not be grounded in a passing hard-reload handoff gate",
        ),
        _criterion(
            "stale_calibration_source_still_present",
            all(term in generator for term in required_terms)
            and all(term in js for term in required_terms)
            and "outsideReviewHandoffStatus" in html
            and "outsideReviewHandoffActions" in html,
            "generator, emitted JS, and emitted HTML retain stale prepared-handoff status/action machinery",
            "regeneration would remove stale prepared-handoff calibration",
        ),
        _criterion(
            "prepared_resume_was_fresh_before_supersede",
            checks.get("prepared_resume_was_fresh_before_supersede") is True
            and prepared.get("payloadKind") == "resume"
            and prepared.get("previewFresh") is True,
            f"kind={prepared.get('payloadKind')} fresh={prepared.get('previewFresh')} status={prepared.get('statusText')}",
            "the baseline prepared resume handoff was not fresh before supersession",
        ),
        _criterion(
            "superseding_shell_handoff_created",
            checks.get("superseding_shell_handoff_created") is True and superseding_shell.get("hasReviewerLanding") is True,
            f"url={superseding_shell.get('url')} reviewer={superseding_shell.get('hasReviewerLanding')}",
            "the proof did not create a newer shell handoff to supersede the prepared payload",
        ),
        _criterion(
            "shell_evidence_refreshed_to_newer_clean_handoff",
            checks.get("shell_evidence_refreshed_to_newer_clean_handoff") is True
            and stale.get("shellHandoffKind") == "clean"
            and stale.get("shellHandoffRecordedAt") != prepared.get("payloadRecordedAt"),
            f"prepared={prepared.get('payloadRecordedAt')} current={stale.get('shellHandoffRecordedAt')} kind={stale.get('shellHandoffKind')}",
            "launcher evidence did not observe a newer current clean handoff",
        ),
        _criterion(
            "prepared_payload_not_overwritten_by_refresh",
            checks.get("prepared_payload_not_overwritten_by_refresh") is True
            and stale.get("payloadKind") == "resume"
            and stale.get("payloadRecordedAt") == prepared.get("payloadRecordedAt"),
            f"prepared={prepared.get('payloadRecordedAt')} stalePayload={stale.get('payloadRecordedAt')} kind={stale.get('payloadKind')}",
            "refresh overwrote the prepared payload instead of calibrating it as stale",
        ),
        _criterion(
            "stale_status_visible_after_supersede",
            checks.get("stale_status_visible_after_supersede") is True
            and "Prepared handoff payload is stale" in str(stale.get("statusText", "")),
            str(stale.get("statusText", "missing stale status")),
            "launcher did not render a human-readable stale prepared-handoff summary",
        ),
        _criterion(
            "freshness_preview_marks_payload_stale",
            checks.get("freshness_preview_marks_payload_stale") is True and stale.get("previewFresh") is False,
            f"previewFresh={stale.get('previewFresh')}",
            "visible preview JSON did not mark the prepared payload stale",
        ),
        _criterion(
            "freshness_preview_names_mismatch",
            checks.get("freshness_preview_names_mismatch") is True
            and stale.get("previewMismatchCount", 0) > 0
            and "launch handoff changed" in (stale.get("previewMismatches") or []),
            str(stale.get("previewMismatches", [])),
            "visible preview JSON did not name the freshness mismatch",
        ),
        _criterion(
            "stale_actions_block_continue",
            checks.get("stale_actions_block_continue") is True
            and stale.get("hasContinueControl") is False
            and "Re-prepare before continuing" in str(stale.get("actionsText", "")),
            str(stale.get("actionsText", "missing stale actions")),
            "stale prepared handoff still exposed a continue action",
        ),
        _criterion(
            "download_remains_available_for_stale_review",
            stale.get("hasDownloadControl") is True and "Download prepared outside-review handoff JSON" in str(stale.get("actionsText", "")),
            str(stale.get("actionsText", "missing download action")),
            "stale calibration removed the downloadable review evidence",
        ),
        _criterion(
            "stale_state_survives_launcher_reload",
            checks.get("stale_state_survives_launcher_reload") is True
            and "Prepared handoff payload is stale" in str(stale_reload.get("statusText", ""))
            and stale_reload.get("previewFresh") is False,
            str(stale_reload.get("statusText", "missing stale reload status")),
            "stale classification did not survive launcher reload",
        ),
        _criterion(
            "stale_reload_keeps_prepared_timestamp",
            checks.get("stale_reload_keeps_prepared_timestamp") is True
            and stale_reload.get("payloadRecordedAt") == prepared.get("payloadRecordedAt"),
            f"prepared={prepared.get('payloadRecordedAt')} reload={stale_reload.get('payloadRecordedAt')}",
            "reload mutated the stale prepared payload timestamp",
        ),
        _criterion(
            "stale_reload_keeps_newer_shell_timestamp",
            checks.get("stale_reload_keeps_newer_shell_timestamp") is True
            and stale_reload.get("shellHandoffRecordedAt") == stale.get("shellHandoffRecordedAt"),
            f"afterSupersede={stale.get('shellHandoffRecordedAt')} reload={stale_reload.get('shellHandoffRecordedAt')}",
            "reload lost the newer shell handoff timestamp used for calibration",
        ),
        _criterion(
            "browser_evidence_uses_visible_or_preview_state",
            checks.get("evidence_avoids_raw_storage_keys") is True
            and "localStorage" not in evidence_text
            and "localHandoff" not in evidence_text
            and "localPayloadHandoff" not in evidence_text,
            "browser evidence compares visible status/actions and visible handoff preview JSON, not raw storage keys",
            "stale calibration proof relies on privileged storage inspection",
        ),
        _criterion(
            "browser_console_clean",
            checks.get("no_console_errors") is True and browser.get("consoleErrors") == 0,
            f"consoleErrors={browser.get('consoleErrors')} messages={browser.get('consoleErrorMessages', [])}",
            "stale calibration browser flow produced console errors",
        ),
        _criterion(
            "boundary_preserved",
            "no subjective consciousness" in BOUNDARY and "no LLM calls" in BOUNDARY,
            BOUNDARY,
            "report boundary implies more than browser-local launcher freshness calibration",
        ),
    ]
    scores = [row.score for row in criteria]
    readiness = mean(scores)
    weakest = min(scores)
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "stale_calibration_score": mean([
            next(row.score for row in criteria if row.channel == "stale_status_visible_after_supersede"),
            next(row.score for row in criteria if row.channel == "freshness_preview_marks_payload_stale"),
            next(row.score for row in criteria if row.channel == "freshness_preview_names_mismatch"),
        ]),
        "stale_action_block_score": next(row.score for row in criteria if row.channel == "stale_actions_block_continue"),
        "stale_review_evidence_score": next(row.score for row in criteria if row.channel == "download_remains_available_for_stale_review"),
        "supersession_score": next(row.score for row in criteria if row.channel == "shell_evidence_refreshed_to_newer_clean_handoff"),
        "reload_survival_score": next(row.score for row in criteria if row.channel == "stale_state_survives_launcher_reload"),
        "timestamp_separation_score": mean([
            next(row.score for row in criteria if row.channel == "prepared_payload_not_overwritten_by_refresh"),
            next(row.score for row in criteria if row.channel == "stale_reload_keeps_prepared_timestamp"),
            next(row.score for row in criteria if row.channel == "stale_reload_keeps_newer_shell_timestamp"),
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
        "report_337_results_path": str(REPORT_337_RESULTS.relative_to(ROOT)),
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
        "# Report 338: SSRM-3D Browser World v98 Primary Demo Stale Prepared-Handoff Calibration Bridge",
        "",
        "## Purpose",
        "",
        "Report 338 verifies calibrated freshness judgment rather than preserving every prepared handoff as "
        "usable forever. The browser proof prepares a visible fresh `resume` handoff, then launches a newer "
        "`clean` shell handoff. The old prepared payload remains downloadable for review, but the launcher "
        "must classify it as stale, name the mismatches, block the continue action, and preserve that stale "
        "classification after reload.",
        "",
        "This did not add another simulation surface. The maintained v61 app shell and primary launcher remain "
        "the only exercised browser-world path, and no app-source patch was needed for the final passing proof.",
        "",
        "## Boundary",
        "",
        result["boundary"],
        "",
        "## Browser evidence",
        "",
        "- Prepared baseline was a fresh `resume` handoff.",
        "- A newer `clean` shell handoff superseded the prepared payload.",
        "- Shell evidence refreshed to the newer clean handoff while the prepared payload stayed the older resume handoff.",
        "- Visible status rendered `Prepared handoff payload is stale...` with named mismatches.",
        "- Visible preview JSON marked `fresh: false` and named `launch handoff changed`.",
        "- Stale actions blocked `Continue from prepared...` and kept the download action available.",
        "- Reload preserved the stale classification, prepared timestamp, and newer shell timestamp.",
        f"- Browser console errors: `{metrics['console_errors']}`.",
        "- Evidence uses visible status/actions plus the visible handoff preview JSON; it does not read raw storage keys.",
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
        "This is a consolidation proof, not a frontier claim. It shows that the current primary launcher can "
        "distinguish valid continuity from stale continuity: old review payloads remain inspectable, but "
        "continuing from them is blocked until the reviewer prepares a fresh handoff.",
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
            "prepared_recorded_at": _safe_get(result, "browser_evidence", "preparedFreshResume", "payloadRecordedAt"),
            "superseding_shell_recorded_at": _safe_get(result, "browser_evidence", "staleAfterSupersede", "shellHandoffRecordedAt"),
            "stale_status": _safe_get(result, "browser_evidence", "staleAfterSupersede", "statusText"),
            "stale_reload_status": _safe_get(result, "browser_evidence", "staleAfterReload", "statusText"),
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
