from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 357
SLUG = "ssrm_3d_browser_world_v117_primary_shell_avatar_absence_accountability_receipt"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT356_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v116_primary_shell_absent_time_choice_receipt_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "357_ssrm_3d_browser_world_v117_primary_shell_avatar_absence_accountability_receipt_report.md"

BOUNDARY = (
    "Browser-local avatar absence accountability receipt over the maintained v61 shell only; "
    "no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, "
    "production persistence, hosted URL proof, complete 3D engine, finished gameplay, or metaphysical claim."
)
NEXT_GATE = (
    "post-357: make the accountability receipt affect the next return greeting so residents can reference both "
    "the resolved offscreen obligation and the accounted avatar absence without rewriting history"
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
        "# Report 357: Browser World v117 Primary Shell Avatar Absence Accountability Receipt",
        "",
        "Report 357 continues the playable-loop consolidation in the maintained v61 shell. Report 356 made absent-time consequences into two explicit causal threads; this report adds the small accountability action for the avatar-caused absence thread after the resident-caused obligation has been handled, while preserving the resident-caused offscreen event, obligation, schedule/debt outcome, and history.",
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
        f"- Before accountability: `{browser.get('beforeAccount', {}).get('avatarAbsenceAccountabilityText', 'missing')}`",
        f"- After resident resolve: `{browser.get('afterResolve', {}).get('absentTimeChoiceText', 'missing')}`",
        f"- After account action: `{browser.get('afterAccount', {}).get('avatarAbsenceAccountabilityText', 'missing')}`",
        f"- After reload account receipt: `{browser.get('afterReload', {}).get('avatarAbsenceAccountabilityText', 'missing')}`",
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
        "This is still deterministic browser-local behavior, not subjective feeling or autonomous language. The improvement is that the loop now supports causal follow-through: resolving a resident-caused offscreen obligation is not allowed to silently close the avatar-caused absence thread, and accounting for absence does not erase the resident-caused history.",
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
    report356 = load_json(REPORT356_RESULTS)
    browser = load_json(BROWSER_SMOKE)

    before_account = browser.get("beforeAccount", {})
    after_resolve = browser.get("afterResolve", {})
    after_account = browser.get("afterAccount", {})
    after_reload = browser.get("afterReload", {})
    console_errors = browser.get("consoleErrors", [])

    account_receipt = after_account.get("avatarAbsenceAccountabilityReceipt", {})
    reload_receipt = after_reload.get("avatarAbsenceAccountabilityReceipt", {})
    after_account_threads = after_account.get("absentTimeThreads", [])

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_356_choice_receipt_gate_passing", report356.get("verdict") == "pass" and report356.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 356 verdict={report356.get('verdict')} weakest={report356.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "source_exposes_accountability_receipt_state", has_terms(app_text, ["avatarAbsenceAccountabilityReceipt", "renderAvatarAbsenceAccountability", "accountForAvatarAbsence", "browser-local-avatar-absence-accountability-receipt-only"]), "app.js exposes avatar absence accountability state, render, action, and boundary")
    add_criterion(criteria, "source_preserves_resident_history", has_terms(app_text, ["residentHistoryPreserved", "offscreenObligationEvents", "avatar acknowledged absence without erasing", "recordResidentHistory"]), "app.js records accountability without deleting offscreen resident event/history")
    add_criterion(criteria, "visible_accountability_panel_wired", has_terms(index_text, ["avatarAbsenceAccountabilityOut", "Avatar accountability", "accountForAvatarAbsence", "Account for avatar absence"]), "index.html exposes Avatar accountability panel and action")
    add_criterion(criteria, "public_state_boundary_includes_accountability", has_terms(app_text, ["avatarAbsenceAccountabilityReceipt", "publicState", "runStateBoundaryAudit"]), "state-boundary audit public world includes accountability receipt")
    add_criterion(criteria, "browser_smoke_artifact_exists", bool(browser), str(BROWSER_SMOKE.relative_to(ROOT)) if BROWSER_SMOKE.exists() else "missing browser smoke artifact")
    add_criterion(criteria, "browser_smoke_used_maintained_shell", "ssrm_3d_browser_world_v61_vertical_slice_app_shell" in browser.get("shellUrl", ""), browser.get("shellUrl", "missing shellUrl"))
    add_criterion(criteria, "before_accountability_receipt_empty", "No avatar absence accountability receipt yet" in before_account.get("avatarAbsenceAccountabilityText", ""), before_account.get("avatarAbsenceAccountabilityText", "missing accountability text"))
    add_criterion(criteria, "resident_thread_resolved_before_accountability", "milo-offscreen-water-jars resident-caused resolved" in after_resolve.get("absentTimeChoiceText", "") and "avatar-absence-thread avatar-caused pending" in after_resolve.get("absentTimeChoiceText", ""), after_resolve.get("absentTimeChoiceText", "missing choice text"))
    add_criterion(criteria, "accountability_marks_avatar_thread_accounted", account_receipt.get("phase") == "avatar-absence-accounted" and account_receipt.get("avatarThreadStatus") == "accounted" and any(thread.get("id") == "avatar-absence-thread" and thread.get("status") == "accounted" for thread in after_account_threads), f"receipt={account_receipt} threads={after_account_threads}")
    add_criterion(criteria, "resident_thread_history_preserved", account_receipt.get("residentThreadId") == "milo-offscreen-water-jars" and account_receipt.get("residentThreadStatus") == "resolved" and account_receipt.get("residentHistoryPreserved") is True, f"receipt={account_receipt}")
    add_criterion(criteria, "visible_accountability_receipt_names_preservation", "Avatar thread: accounted" in after_account.get("avatarAbsenceAccountabilityText", "") and "Resident thread: milo-offscreen-water-jars resolved" in after_account.get("avatarAbsenceAccountabilityText", "") and "History preserved: yes" in after_account.get("avatarAbsenceAccountabilityText", ""), after_account.get("avatarAbsenceAccountabilityText", "missing accountability text"))
    add_criterion(criteria, "resident_schedule_debt_remain_resolved", "Milo schedule resolved" in after_account.get("scheduleQueueText", "") and "Milo debt settled" in after_account.get("debtLedgerText", ""), f"schedule={after_account.get('scheduleQueueText')} debt={after_account.get('debtLedgerText')}")
    add_criterion(criteria, "resident_history_names_non_erasure", "Fay changed Milo" in after_account.get("historyText", "") and "avatar acknowledged absence without erasing milo-offscreen-water-jars" in after_account.get("historyText", ""), after_account.get("historyText", "missing history"))
    add_criterion(criteria, "accountability_survives_reload", reload_receipt.get("phase") == "avatar-absence-accounted" and reload_receipt.get("avatarThreadStatus") == "accounted" and reload_receipt.get("residentHistoryPreserved") is True and "History preserved: yes" in after_reload.get("avatarAbsenceAccountabilityText", ""), f"receipt={reload_receipt} text={after_reload.get('avatarAbsenceAccountabilityText')}")
    add_criterion(criteria, "replay_logs_accountability_receipt", browser.get("replayHasAccountabilityReceipt") is True and browser.get("accountabilityReloaded") is True, f"replayHasAccountabilityReceipt={browser.get('replayHasAccountabilityReceipt')} accountabilityReloaded={browser.get('accountabilityReloaded')}")
    add_criterion(criteria, "browser_console_clean", len(console_errors) == 0, f"console error count={len(console_errors)}")
    add_criterion(criteria, "experiment_index_includes_report_357", "experiments.ssrm_3d_browser_world_v117_primary_shell_avatar_absence_accountability_receipt" in runner_text, "scripts/run_experiments.py includes Report 357 module")
    add_criterion(criteria, "claim_boundary_preserved", all(term in BOUNDARY for term in ["no LLM call", "subjective consciousness", "moral patienthood", "finished gameplay"]), BOUNDARY)

    category_scores = {
        "review_gate_score": criteria[0]["score"],
        "source_behavior_score": min(criteria[1]["score"], criteria[2]["score"], criteria[4]["score"]),
        "visible_binding_score": criteria[3]["score"],
        "browser_interaction_score": min(criteria[5]["score"], criteria[6]["score"]),
        "empty_state_score": criteria[7]["score"],
        "precondition_thread_score": criteria[8]["score"],
        "accountability_receipt_score": min(criteria[9]["score"], criteria[10]["score"], criteria[11]["score"]),
        "resident_history_preservation_score": min(criteria[12]["score"], criteria[13]["score"]),
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
        "before_account_replay_rows": int(before_account.get("replayRows", 0) or 0),
        "after_resolve_replay_rows": int(after_resolve.get("replayRows", 0) or 0),
        "after_account_replay_rows": int(after_account.get("replayRows", 0) or 0),
        "after_reload_replay_rows": int(after_reload.get("replayRows", 0) or 0),
        "console_error_count": len(console_errors),
    }
    verdict = "pass" if all(row["passed"] for row in criteria) else "fail"
    results = {"report": REPORT, "slug": SLUG, "verdict": verdict, "generated_at": datetime.now(timezone.utc).isoformat(), "boundary": BOUNDARY, "metrics": metrics, "criteria": criteria, "browser_smoke_artifact": str(BROWSER_SMOKE.relative_to(ROOT)), "next_gate": NEXT_GATE}
    state = {"report": REPORT, "shell_app": str(SHELL_APP.relative_to(ROOT)), "browser_smoke": browser, "report356_gate": report356}

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
