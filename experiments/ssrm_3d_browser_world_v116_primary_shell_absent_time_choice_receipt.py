from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 356
SLUG = "ssrm_3d_browser_world_v116_primary_shell_absent_time_choice_receipt"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT355_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v115_primary_shell_absent_time_summary_separation_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "356_ssrm_3d_browser_world_v116_primary_shell_absent_time_choice_receipt_report.md"

BOUNDARY = (
    "Browser-local absent-time choice receipt over the maintained v61 shell only; "
    "no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, "
    "production persistence, hosted URL proof, complete 3D engine, finished gameplay, or metaphysical claim."
)
NEXT_GATE = (
    "post-356: let the player handle the still-pending avatar-caused absence thread with a small accountability action "
    "without erasing the resident-caused offscreen obligation history"
)


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def has_terms(text: str, terms: List[str]) -> bool:
    return all(term in text for term in terms)


def add_criterion(criteria: List[Dict[str, Any]], name: str, passed: bool, evidence: str) -> None:
    criteria.append({"criterion": name, "passed": bool(passed), "score": 1.0 if passed else 0.0, "evidence": evidence})


def write_csv(path: Path, rows: List[Dict[str, Any]], fieldnames: List[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def report_text(results: Dict[str, Any], criteria: List[Dict[str, Any]], browser: Dict[str, Any]) -> str:
    metrics = results["metrics"]
    passed_count = sum(1 for row in criteria if row["passed"])
    lines = [
        "# Report 356: Browser World v116 Primary Shell Absent-Time Choice Receipt",
        "",
        "Report 356 closes the next playable-loop gap in the maintained v61 shell. Report 355 separated avatar-caused waiting from resident-caused offscreen changes before choice; this report records the player's bounded thread choice and keeps the unchosen absent-time thread visibly pending instead of letting a single button erase causal context.",
        "",
        f"Boundary: {BOUNDARY}",
        "",
        "## Result",
        "",
        f"Verdict: `{results['verdict']}`",
        f"Readiness: `{metrics['readiness']:.3f}`",
        f"Weakest channel score: `{metrics['weakest_channel_score']:.3f}`",
        f"Criteria passed: `{passed_count} / {len(criteria)}`",
        "",
        "## Browser-smoke evidence",
        "",
        f"- Maintained shell URL: `{browser.get('shellUrl', 'missing')}`",
        f"- Before choice panel: `{browser.get('beforeOffscreen', {}).get('absentTimeChoiceText', 'missing')}`",
        f"- After offscreen panel: `{browser.get('afterOffscreen', {}).get('absentTimeChoiceText', 'missing')}`",
        f"- After resident-thread choice: `{browser.get('afterChoiceResident', {}).get('absentTimeChoiceText', 'missing')}`",
        f"- After resolve panel: `{browser.get('afterResolve', {}).get('absentTimeChoiceText', 'missing')}`",
        f"- After reload panel: `{browser.get('afterReload', {}).get('absentTimeChoiceText', 'missing')}`",
        f"- Console errors: `{metrics['console_error_count']}`",
        "",
        "## Criteria",
        "",
        "| Criterion | Score | Evidence |",
        "| --- | ---: | --- |",
    ]
    for row in criteria:
        evidence = str(row["evidence"]).replace("|", "/")
        lines.append(f"| `{row['criterion']}` | `{row['score']:.1f}` | {evidence} |")
    lines.extend([
        "",
        "## Honest interpretation",
        "",
        "This is still browser-local deterministic state, but it makes the playable loop less toy-like: absence creates two explicit causal threads, the player chooses which one to handle first, and the unchosen thread remains visible instead of disappearing behind a successful resolution. It does not claim autonomous language, subjective feeling, production persistence, hosted gameplay, or complete game status.",
        "",
        "## Next gate",
        "",
        NEXT_GATE,
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    app_text = SHELL_APP.read_text(encoding="utf-8")
    index_text = SHELL_INDEX.read_text(encoding="utf-8")
    runner_text = RUNNER.read_text(encoding="utf-8")
    report355 = load_json(REPORT355_RESULTS)
    browser = load_json(BROWSER_SMOKE)

    before = browser.get("beforeOffscreen", {})
    after = browser.get("afterOffscreen", {})
    choice = browser.get("afterChoiceResident", {})
    resolved = browser.get("afterResolve", {})
    reload = browser.get("afterReload", {})
    console_errors = browser.get("consoleErrors", [])

    choice_receipt = choice.get("absentTimeChoiceReceipt", {})
    resolved_receipt = resolved.get("absentTimeChoiceReceipt", {})
    reload_receipt = reload.get("absentTimeChoiceReceipt", {})
    choice_threads = choice.get("absentTimeThreads", [])
    resolved_threads = resolved.get("absentTimeThreads", [])

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_355_absent_summary_gate_passing", report355.get("verdict") == "pass" and report355.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 355 verdict={report355.get('verdict')} weakest={report355.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "source_exposes_choice_receipt_state", has_terms(app_text, ["absentTimeThreads", "absentTimeChoiceReceipt", "renderAbsentTimeChoice", "browser-local-absent-time-choice-receipt-only"]), "app.js exposes absent-time threads, receipt state, render, and boundary")
    add_criterion(criteria, "source_exposes_bounded_choice_actions", has_terms(app_text, ["chooseAbsentTimeThread", "handleAvatarAbsenceFirst", "handleResidentOffscreenFirst", "recordObligationChoiceOutcome"]), "app.js exposes bounded thread-choice and outcome hooks")
    add_criterion(criteria, "visible_choice_panel_wired", has_terms(index_text, ["absentTimeChoiceOut", "Absent choice", "handleAvatarAbsenceFirst", "handleResidentOffscreenFirst"]), "index.html exposes Absent choice panel and two bounded buttons")
    add_criterion(criteria, "summary_creates_two_choice_threads", has_terms(app_text, ["buildAbsentTimeThreads(event, obligation)", "avatar-absence-thread", "resident-caused", "world.absentTimeChoiceReceipt = null"]), "updateAbsentTimeSummary creates avatar and resident threads before choice")
    add_criterion(criteria, "resolve_defer_record_choice_outcome", has_terms(app_text, ["recordObligationChoiceOutcome(obligation, 'resolve'", "recordObligationChoiceOutcome(obligation, 'defer'", "avatarAbsenceStatus"]), "resolve/defer updates absent-time choice receipt")
    add_criterion(criteria, "browser_smoke_artifact_exists", bool(browser), str(BROWSER_SMOKE.relative_to(ROOT)) if BROWSER_SMOKE.exists() else "missing browser smoke artifact")
    add_criterion(criteria, "browser_smoke_used_maintained_shell", "ssrm_3d_browser_world_v61_vertical_slice_app_shell" in browser.get("shellUrl", ""), browser.get("shellUrl", "missing shellUrl"))
    add_criterion(criteria, "before_offscreen_choice_empty", "No absent-time choice yet" in before.get("absentTimeChoiceText", ""), before.get("absentTimeChoiceText", "missing choice text"))
    add_criterion(criteria, "after_offscreen_two_pending_threads_visible", "avatar-absence-thread avatar-caused pending" in after.get("absentTimeChoiceText", "") and "milo-offscreen-water-jars resident-caused pending" in after.get("absentTimeChoiceText", ""), after.get("absentTimeChoiceText", "missing choice text"))
    add_criterion(criteria, "resident_thread_choice_records_receipt", choice_receipt.get("phase") == "thread-choice-recorded" and choice_receipt.get("chosenThreadId") == "milo-offscreen-water-jars" and choice_receipt.get("chosenSource") == "resident-caused", f"receipt={choice_receipt}")
    add_criterion(criteria, "unchosen_avatar_thread_remains_pending", any(thread.get("id") == "avatar-absence-thread" and thread.get("status") == "pending" for thread in choice_threads) and "Unchosen pending: avatar-absence-thread" in choice.get("absentTimeChoiceText", ""), f"threads={choice_threads} text={choice.get('absentTimeChoiceText')}")
    add_criterion(criteria, "resolve_records_resident_outcome_without_erasing_avatar_thread", resolved_receipt.get("phase") == "obligation-action-recorded" and resolved_receipt.get("residentThreadStatus") == "resolved" and resolved_receipt.get("avatarAbsenceStatus") == "pending" and any(thread.get("id") == "avatar-absence-thread" and thread.get("status") == "pending" for thread in resolved_threads), f"receipt={resolved_receipt} threads={resolved_threads}")
    add_criterion(criteria, "resolve_links_schedule_debt_status", resolved_receipt.get("scheduleQueueStatus") == "resolved" and resolved_receipt.get("debtLedgerStatus") == "settled" and "Milo schedule resolved" in resolved.get("scheduleQueueText", "") and "Milo debt settled" in resolved.get("debtLedgerText", ""), f"receipt={resolved_receipt} schedule={resolved.get('scheduleQueueText')} debt={resolved.get('debtLedgerText')}")
    add_criterion(criteria, "choice_receipt_survives_reload", reload_receipt.get("phase") == "obligation-action-recorded" and reload_receipt.get("avatarAbsenceStatus") == "pending" and "avatar-caused absence thread pending" in reload.get("absentTimeChoiceText", ""), f"receipt={reload_receipt} text={reload.get('absentTimeChoiceText')}")
    add_criterion(criteria, "replay_logs_choice_and_resolution_receipts", browser.get("replayHasChoiceReceipt") is True and browser.get("summaryReloaded") is True, f"replayHasChoiceReceipt={browser.get('replayHasChoiceReceipt')} summaryReloaded={browser.get('summaryReloaded')}")
    add_criterion(criteria, "browser_console_clean", len(console_errors) == 0, f"console error count={len(console_errors)}")
    add_criterion(criteria, "experiment_index_includes_report_356", "experiments.ssrm_3d_browser_world_v116_primary_shell_absent_time_choice_receipt" in runner_text, "scripts/run_experiments.py includes Report 356 module")
    add_criterion(criteria, "claim_boundary_preserved", all(term in BOUNDARY for term in ["no LLM call", "subjective consciousness", "moral patienthood", "finished gameplay"]), BOUNDARY)

    category_scores = {
        "review_gate_score": criteria[0]["score"],
        "source_behavior_score": min(criteria[1]["score"], criteria[2]["score"], criteria[4]["score"], criteria[5]["score"]),
        "visible_binding_score": criteria[3]["score"],
        "browser_interaction_score": min(criteria[6]["score"], criteria[7]["score"]),
        "empty_state_score": criteria[8]["score"],
        "two_thread_setup_score": criteria[9]["score"],
        "choice_receipt_score": min(criteria[10]["score"], criteria[11]["score"]),
        "outcome_receipt_score": min(criteria[12]["score"], criteria[13]["score"]),
        "reload_persistence_score": criteria[14]["score"],
        "replay_debug_score": criteria[15]["score"],
        "runtime_hygiene_score": criteria[16]["score"],
        "runner_index_score": criteria[17]["score"],
        "claim_hygiene_score": criteria[18]["score"],
    }
    weakest = min(category_scores.values())
    readiness = sum(category_scores.values()) / len(category_scores)
    metrics = {
        **category_scores,
        "weakest_channel_score": weakest,
        "readiness": readiness,
        "criterion_count": len(criteria),
        "before_replay_rows": int(before.get("replayRows", 0) or 0),
        "after_offscreen_replay_rows": int(after.get("replayRows", 0) or 0),
        "after_choice_replay_rows": int(choice.get("replayRows", 0) or 0),
        "after_resolve_replay_rows": int(resolved.get("replayRows", 0) or 0),
        "after_reload_replay_rows": int(reload.get("replayRows", 0) or 0),
        "console_error_count": len(console_errors),
    }
    verdict = "pass" if all(row["passed"] for row in criteria) else "fail"
    results = {"report": REPORT, "slug": SLUG, "verdict": verdict, "generated_at": datetime.now(timezone.utc).isoformat(), "boundary": BOUNDARY, "metrics": metrics, "criteria": criteria, "browser_smoke_artifact": str(BROWSER_SMOKE.relative_to(ROOT)), "next_gate": NEXT_GATE}
    state = {"report": REPORT, "shell_app": str(SHELL_APP.relative_to(ROOT)), "browser_smoke": browser, "report355_gate": report355}

    RESULTS.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    STATE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_csv(SUMMARY, [{"report": REPORT, "verdict": verdict, **metrics}], ["report", "verdict", *metrics.keys()])
    write_csv(VERDICT, [{"report": REPORT, "verdict": verdict, "weakest_channel_score": weakest, "readiness": readiness, "next_gate": NEXT_GATE}], ["report", "verdict", "weakest_channel_score", "readiness", "next_gate"])
    write_csv(CRITERIA, criteria, ["criterion", "passed", "score", "evidence"])
    REPORT_PATH.write_text(report_text(results, criteria, browser), encoding="utf-8")

    print(json.dumps({"report": REPORT, "verdict": verdict, "metrics": metrics}, indent=2, sort_keys=True))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
