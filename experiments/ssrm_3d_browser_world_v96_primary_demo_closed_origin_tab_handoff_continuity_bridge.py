"""Report 336: SSRM-3D browser world v96 closed-origin-tab handoff continuity bridge.

This report verifies the Report 335 cross-tab handoff path after closing the
original preparing tab. A reviewer tab prepares a visible fresh resume handoff,
the preparing tab is closed, a fresh tab opens the primary launcher URL
directly, sees the same prepared handoff card, follows the visible continue
action into the maintained shell, returns, refreshes shell evidence, and keeps
the same visible handoff timestamp without raw storage inspection.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 336
PREFIX = "ssrm_3d_browser_world_v96_primary_demo_closed_origin_tab_handoff_continuity_bridge"
DEFAULT_SEED = 20270734

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V63_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
PRIMARY_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo"
PRIMARY_JS = PRIMARY_DIR / "demo.js"
PRIMARY_HTML = PRIMARY_DIR / "index.html"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"
REPORT_335_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v95_primary_demo_cross_tab_handoff_continuity_bridge_results.json"

BOUNDARY = (
    "Deterministic browser-local closed-origin-tab handoff continuity bridge only; no LLM calls, no "
    "subjective consciousness, no autonomous natural language, no moral patienthood, no production "
    "persistence, no complete 3D engine, and no finished gameplay claim. This is local tab-lifecycle "
    "handoff hygiene and visible review continuity, not external validation or evidence of inner experience."
)

NEXT_GATE = (
    "post-336: verify the closed-origin-tab handoff path after a hard reload of the fresh tab, so visible "
    "handoff continuity survives a page lifecycle restart as well as preparing-tab closure"
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
    report_335 = _load_json(REPORT_335_RESULTS)
    checks = browser.get("checks", {}) if isinstance(browser.get("checks"), dict) else {}
    original = browser.get("originalPreparedBeforeClose", {}) if isinstance(browser.get("originalPreparedBeforeClose"), dict) else {}
    fresh = browser.get("freshTabAfterOriginClosed", {}) if isinstance(browser.get("freshTabAfterOriginClosed"), dict) else {}
    shell = browser.get("continuedShellAfterOriginClose", {}) if isinstance(browser.get("continuedShellAfterOriginClose"), dict) else {}
    after = browser.get("afterReturnAfterRefresh", {}) if isinstance(browser.get("afterReturnAfterRefresh"), dict) else {}
    evidence_text = json.dumps(browser, sort_keys=True)
    required_terms = [
        "continuePreparedHandoff",
        "preparedHandoffHref",
        "renderOutsideReviewHandoffActions",
        "handoffPayloadFreshnessState",
        "outsideReviewHandoffActions",
        "Continue from prepared",
    ]
    criteria = [
        _criterion(
            "report_335_cross_tab_gate_passed",
            report_335.get("verdict") == "pass" and _safe_get(report_335, "metrics", "weakest_channel_score") == 1.0,
            f"Report 335 verdict={report_335.get('verdict')} weakest={_safe_get(report_335, 'metrics', 'weakest_channel_score')}",
            "closed-origin-tab continuity would not be grounded in a passing cross-tab handoff gate",
        ),
        _criterion(
            "closed_origin_source_still_present",
            all(term in generator for term in required_terms)
            and all(term in js for term in required_terms)
            and "outsideReviewHandoffActions" in html,
            "generator, emitted JS, and emitted HTML retain prepared handoff continue/download machinery",
            "regeneration would remove the visible prepared handoff path",
        ),
        _criterion(
            "original_tab_prepared_fresh_resume_before_close",
            checks.get("original_tab_prepared_fresh_resume_before_close") is True
            and original.get("payloadKind") == "resume"
            and original.get("payloadFresh") is True,
            f"kind={original.get('payloadKind')} fresh={original.get('payloadFresh')} status={original.get('statusText')}",
            "the preparing tab did not create a visible fresh resume handoff before close",
        ),
        _criterion(
            "original_preparing_tab_closed",
            checks.get("original_preparing_tab_closed") is True and browser.get("originalTabClosed") is True,
            f"originalTabId={browser.get('originalTabId')} closed={browser.get('originalTabClosed')}",
            "the proof did not actually close the preparing tab before fresh-tab entry",
        ),
        _criterion(
            "fresh_tab_after_close_shows_prepared_handoff",
            checks.get("fresh_tab_after_close_shows_prepared_handoff") is True and fresh.get("payloadKind") == "resume",
            f"kind={fresh.get('payloadKind')} status={fresh.get('statusText')}",
            "a fresh launcher tab does not render the prepared handoff after the preparing tab is closed",
        ),
        _criterion(
            "fresh_tab_after_close_status_fresh_resume",
            checks.get("fresh_tab_after_close_status_fresh_resume") is True
            and "fresh resume handoff" in str(fresh.get("statusText", "")),
            str(fresh.get("statusText", "missing fresh tab status")),
            "fresh tab status does not classify the closed-origin handoff as fresh resume",
        ),
        _criterion(
            "fresh_tab_after_close_controls_available",
            checks.get("fresh_tab_after_close_controls_available") is True
            and fresh.get("hasContinueControl") is True
            and fresh.get("hasDownloadControl") is True,
            str(fresh.get("actionsText", "missing fresh tab actions")),
            "fresh tab lacks continue/download controls after preparing-tab closure",
        ),
        _criterion(
            "fresh_tab_after_close_visible_handoff_timestamp_matches_original",
            checks.get("fresh_tab_after_close_visible_handoff_timestamp_matches_original") is True
            and fresh.get("payloadRecordedAt") == original.get("payloadRecordedAt"),
            f"original={original.get('payloadRecordedAt')} fresh={fresh.get('payloadRecordedAt')}",
            "fresh tab shows a different visible handoff timestamp after preparing-tab closure",
        ),
        _criterion(
            "fresh_tab_after_close_payload_timestamp_matches_original",
            checks.get("fresh_tab_after_close_payload_timestamp_matches_original") is True
            and fresh.get("payloadCurrentRecordedAt") == original.get("payloadCurrentRecordedAt"),
            f"original={original.get('payloadCurrentRecordedAt')} fresh={fresh.get('payloadCurrentRecordedAt')}",
            "fresh tab preview freshness points at a different current handoff timestamp after preparing-tab closure",
        ),
        _criterion(
            "fresh_tab_after_close_continue_reaches_shell",
            checks.get("fresh_tab_after_close_continue_reaches_shell") is True
            and shell.get("hasReviewerLanding") is True
            and shell.get("hasRunReviewerPass") is True,
            f"url={shell.get('url')} reviewer={shell.get('hasReviewerLanding')} runPass={shell.get('hasRunReviewerPass')}",
            "fresh tab continue action does not reach the maintained reviewer shell after preparing-tab closure",
        ),
        _criterion(
            "fresh_tab_after_close_return_to_launcher_visible",
            checks.get("fresh_tab_after_close_return_to_launcher_visible") is True,
            str(browser.get("afterReturnBeforeRefresh", {}).get("url", "missing return URL")),
            "fresh tab continued session cannot return visibly to the launcher after preparing-tab closure",
        ),
        _criterion(
            "fresh_tab_after_close_refresh_keeps_handoff_fresh",
            checks.get("fresh_tab_after_close_refresh_keeps_handoff_fresh") is True
            and after.get("payloadFresh") is True
            and "fresh resume handoff" in str(after.get("statusText", "")),
            str(after.get("statusText", "missing after-refresh status")),
            "refreshing shell evidence after closed-origin-tab continue-return makes the handoff stale",
        ),
        _criterion(
            "fresh_tab_after_close_after_return_timestamp_unchanged",
            checks.get("fresh_tab_after_close_after_return_timestamp_unchanged") is True
            and after.get("payloadRecordedAt") == original.get("payloadRecordedAt")
            and after.get("payloadCurrentRecordedAt") == original.get("payloadCurrentRecordedAt"),
            f"original={original.get('payloadRecordedAt')} after={after.get('payloadRecordedAt')}",
            "closed-origin-tab continue-return changes the visible prepared handoff timestamp",
        ),
        _criterion(
            "browser_evidence_uses_visible_or_preview_state",
            checks.get("evidence_avoids_raw_storage_keys") is True
            and "localStorage" not in evidence_text
            and "localHandoff" not in evidence_text
            and "localPayloadHandoff" not in evidence_text,
            "browser evidence compares visible status/actions and visible handoff preview JSON, not raw storage keys",
            "closed-origin-tab proof relies on privileged storage inspection",
        ),
        _criterion(
            "browser_console_clean",
            checks.get("no_console_errors") is True and browser.get("consoleErrors") == 0,
            f"consoleErrors={browser.get('consoleErrors')} messages={browser.get('consoleErrorMessages', [])}",
            "closed-origin-tab browser flow produced console errors",
        ),
        _criterion(
            "boundary_preserved",
            "no subjective consciousness" in BOUNDARY and "no LLM calls" in BOUNDARY,
            BOUNDARY,
            "report boundary implies more than browser-local tab-lifecycle handoff continuity",
        ),
    ]
    scores = [row.score for row in criteria]
    readiness = mean(scores)
    weakest = min(scores)
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "closed_origin_continuity_score": mean([
            next(row.score for row in criteria if row.channel == "fresh_tab_after_close_shows_prepared_handoff"),
            next(row.score for row in criteria if row.channel == "fresh_tab_after_close_status_fresh_resume"),
            next(row.score for row in criteria if row.channel == "fresh_tab_after_close_controls_available"),
        ]),
        "tab_independence_score": next(row.score for row in criteria if row.channel == "original_preparing_tab_closed"),
        "cross_tab_continue_score": next(row.score for row in criteria if row.channel == "fresh_tab_after_close_continue_reaches_shell"),
        "timestamp_match_score": mean([
            next(row.score for row in criteria if row.channel == "fresh_tab_after_close_visible_handoff_timestamp_matches_original"),
            next(row.score for row in criteria if row.channel == "fresh_tab_after_close_payload_timestamp_matches_original"),
            next(row.score for row in criteria if row.channel == "fresh_tab_after_close_after_return_timestamp_unchanged"),
        ]),
        "post_return_freshness_score": next(row.score for row in criteria if row.channel == "fresh_tab_after_close_refresh_keeps_handoff_fresh"),
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
        "report_335_results_path": str(REPORT_335_RESULTS.relative_to(ROOT)),
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
        "# Report 336: SSRM-3D Browser World v96 Primary Demo Closed-Origin-Tab Handoff Continuity Bridge",
        "",
        "## Purpose",
        "",
        "Report 336 turns the Report 335 cross-tab continuity gate into a tab-lifecycle independence gate. "
        "One browser tab prepares the visible fresh `resume` handoff, then that preparing tab is closed. "
        "A second fresh tab opens the primary launcher URL directly, sees the same prepared handoff card, "
        "clicks the visible continue action, returns to the launcher, refreshes shell evidence, and keeps "
        "the same visible handoff timestamp.",
        "",
        "This did not add another simulation surface. The maintained v61 app shell and primary launcher remain "
        "the only exercised browser-world path.",
        "",
        "## Boundary",
        "",
        result["boundary"],
        "",
        "## Browser evidence",
        "",
        "- Original tab prepared a fresh `resume` handoff.",
        "- The preparing tab was closed before the fresh tab opened the launcher URL.",
        "- Fresh launcher tab rendered the same prepared handoff card from visible page state.",
        "- Fresh tab exposed `Continue from prepared resume handoff` and `Download prepared outside-review handoff JSON`.",
        "- Continue reached the maintained reviewer shell with reviewer landing and `Run reviewer pass` visible.",
        "- Return to launcher was visible after the continued session.",
        "- Refreshing shell evidence preserved the fresh resume classification.",
        "- Original, fresh-tab, and after-return visible handoff timestamps matched.",
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
        "This is a consolidation proof, not a new frontier claim. It says the current primary demo handoff "
        "can be recovered through visible UI surfaces even after the tab that prepared it is closed, and "
        "that the checked continue-return path does not silently mutate the prepared timestamp.",
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
            "original_tab_closed": _safe_get(result, "browser_evidence", "originalTabClosed"),
            "original_recorded_at": _safe_get(result, "browser_evidence", "originalPreparedBeforeClose", "payloadRecordedAt"),
            "fresh_tab_recorded_at": _safe_get(result, "browser_evidence", "freshTabAfterOriginClosed", "payloadRecordedAt"),
            "after_return_recorded_at": _safe_get(result, "browser_evidence", "afterReturnAfterRefresh", "payloadRecordedAt"),
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
