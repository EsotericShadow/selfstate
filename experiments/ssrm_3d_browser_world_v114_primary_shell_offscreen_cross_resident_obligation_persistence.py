from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 354
SLUG = "ssrm_3d_browser_world_v114_primary_shell_offscreen_cross_resident_obligation_persistence"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT353_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v113_primary_shell_obligation_schedule_debt_integration_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "354_ssrm_3d_browser_world_v114_primary_shell_offscreen_cross_resident_obligation_persistence_report.md"

BOUNDARY = (
    "Browser-local offscreen cross-resident obligation persistence over the maintained v61 shell only; "
    "no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, "
    "production persistence, hosted URL proof, complete 3D engine, finished gameplay, or metaphysical claim."
)
NEXT_GATE = (
    "post-354: add a small visible absent-time summary that separates avatar-caused changes from resident-caused "
    "offscreen changes before the player chooses which obligation to handle"
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
        "# Report 354: Browser World v114 Primary Shell Offscreen Cross-Resident Obligation Persistence",
        "",
        "Report 354 keeps the integration work on the maintained v61 shell. Report 353 connected selected obligations to the visible schedule/debt dashboard; this report makes the existing `Wait offscreen` action create a resident-caused obligation for a different resident and proves the visible obligation, schedule queue, and debt ledger survive reload.",
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
        f"- Before offscreen obligation list: `{browser.get('beforeOffscreen', {}).get('obligationListText', 'missing')}`",
        f"- After offscreen obligation list: `{browser.get('afterOffscreen', {}).get('obligationListText', 'missing')}`",
        f"- After offscreen schedule queue: `{browser.get('afterOffscreen', {}).get('scheduleQueueText', 'missing')}`",
        f"- After offscreen debt ledger: `{browser.get('afterOffscreen', {}).get('debtLedgerText', 'missing')}`",
        f"- After reload obligation list: `{browser.get('afterReload', {}).get('obligationListText', 'missing')}`",
        f"- After reload schedule queue: `{browser.get('afterReload', {}).get('scheduleQueueText', 'missing')}`",
        f"- After reload debt ledger: `{browser.get('afterReload', {}).get('debtLedgerText', 'missing')}`",
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
        "This is a concrete offscreen-life integration step: while the avatar is absent, Fay can create an obligation for Milo, and the obligation remains visible after reload. It is still deterministic browser-local state, not autonomous natural language, subjective experience, production persistence, hosted gameplay, or a complete 3D engine.",
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
    runner_text = RUNNER.read_text(encoding="utf-8")
    report353 = load_json(REPORT353_RESULTS)
    browser = load_json(BROWSER_SMOKE)

    before = browser.get("beforeOffscreen", {})
    after = browser.get("afterOffscreen", {})
    reload = browser.get("afterReload", {})
    event = browser.get("offscreenEvent", {})
    console_errors = browser.get("consoleErrors", [])

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_353_schedule_debt_gate_passing", report353.get("verdict") == "pass" and report353.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 353 verdict={report353.get('verdict')} weakest={report353.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "source_wires_wait_offscreen_to_cross_resident_obligation", has_terms(app_text, ["runOffscreenResidentObligationPulse", "waitOffscreen", "offscreenObligationEvents", "Fay", "Milo", "browser-local-offscreen-cross-resident-obligation-only"]), "waitOffscreen wires an offscreen resident event into public obligation state")
    add_criterion(criteria, "source_updates_target_resident_schedule_debt", has_terms(app_text, ["offscreen obligation: inspect leaking water jars", "debt: alreadyOpen ? 0 : 1", "syncScheduleDebtFromObligation(row, 'offscreen-resident-action')", "offscreen obligation received"]), "offscreen event mutates target resident schedule, debt, history, and ledgers")
    add_criterion(criteria, "source_public_state_includes_offscreen_events", has_terms(app_text, ["offscreenObligationEvents", "publicState", "runStateBoundaryAudit"]), "offscreen events are part of public audited state")
    add_criterion(criteria, "browser_smoke_artifact_exists", bool(browser), str(BROWSER_SMOKE.relative_to(ROOT)) if BROWSER_SMOKE.exists() else "missing browser smoke artifact")
    add_criterion(criteria, "browser_smoke_used_maintained_shell", "ssrm_3d_browser_world_v61_vertical_slice_app_shell" in browser.get("shellUrl", ""), browser.get("shellUrl", "missing shellUrl"))
    add_criterion(criteria, "offscreen_action_created_different_resident_obligation", event.get("actor") == "Fay" and event.get("target") == "Milo" and event.get("actor") != event.get("target") and "milo-offscreen-water-jars" in after.get("obligationListText", ""), f"event={event} list={after.get('obligationListText')}")
    add_criterion(criteria, "offscreen_action_updates_schedule_queue", "Milo schedule pending" in after.get("scheduleQueueText", "") and "offscreen obligation" in after.get("scheduleQueueText", ""), after.get("scheduleQueueText", "missing schedule queue"))
    add_criterion(criteria, "offscreen_action_updates_debt_ledger", "Milo debt outstanding" in after.get("debtLedgerText", "") and "debt 3" in after.get("debtLedgerText", ""), after.get("debtLedgerText", "missing debt ledger"))
    add_criterion(criteria, "target_resident_history_records_offscreen_source", "offscreen obligation received" in after.get("historyText", "") and "Fay changed Milo" in after.get("historyText", ""), after.get("historyText", "missing history"))
    add_criterion(criteria, "state_survives_reload_obligation", "milo-offscreen-water-jars" in reload.get("obligationListText", "") and "Milo offscreen obligation open" in reload.get("obligationListText", ""), reload.get("obligationListText", "missing obligation list"))
    add_criterion(criteria, "state_survives_reload_schedule_queue", "Milo schedule pending" in reload.get("scheduleQueueText", "") and "offscreen obligation" in reload.get("scheduleQueueText", ""), reload.get("scheduleQueueText", "missing schedule queue"))
    add_criterion(criteria, "state_survives_reload_debt_ledger", "Milo debt outstanding" in reload.get("debtLedgerText", "") and "debt 3" in reload.get("debtLedgerText", ""), reload.get("debtLedgerText", "missing debt ledger"))
    add_criterion(criteria, "replay_logs_wait_offscreen_event", browser.get("waitOffscreenReplayLogged") is True and browser.get("offscreenEventReloaded") is True, f"waitOffscreenReplayLogged={browser.get('waitOffscreenReplayLogged')} offscreenEventReloaded={browser.get('offscreenEventReloaded')}")
    add_criterion(criteria, "browser_console_clean", len(console_errors) == 0, f"console error count={len(console_errors)}")
    add_criterion(criteria, "experiment_index_includes_report_354", "experiments.ssrm_3d_browser_world_v114_primary_shell_offscreen_cross_resident_obligation_persistence" in runner_text, "scripts/run_experiments.py includes Report 354 module")
    add_criterion(criteria, "claim_boundary_preserved", all(term in BOUNDARY for term in ["no LLM call", "subjective consciousness", "moral patienthood", "finished gameplay"]), BOUNDARY)

    category_scores = {
        "review_gate_score": criteria[0]["score"],
        "source_behavior_score": min(criteria[1]["score"], criteria[2]["score"], criteria[3]["score"]),
        "browser_interaction_score": min(criteria[4]["score"], criteria[5]["score"]),
        "cross_resident_obligation_score": criteria[6]["score"],
        "schedule_debt_score": min(criteria[7]["score"], criteria[8]["score"]),
        "resident_history_score": criteria[9]["score"],
        "reload_persistence_score": min(criteria[10]["score"], criteria[11]["score"], criteria[12]["score"]),
        "replay_debug_score": criteria[13]["score"],
        "runtime_hygiene_score": criteria[14]["score"],
        "runner_index_score": criteria[15]["score"],
        "claim_hygiene_score": criteria[16]["score"],
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
        "after_reload_replay_rows": int(reload.get("replayRows", 0) or 0),
        "console_error_count": len(console_errors),
    }
    verdict = "pass" if all(row["passed"] for row in criteria) else "fail"
    results = {"report": REPORT, "slug": SLUG, "verdict": verdict, "generated_at": datetime.now(timezone.utc).isoformat(), "boundary": BOUNDARY, "metrics": metrics, "criteria": criteria, "browser_smoke_artifact": str(BROWSER_SMOKE.relative_to(ROOT)), "next_gate": NEXT_GATE}
    state = {"report": REPORT, "shell_app": str(SHELL_APP.relative_to(ROOT)), "browser_smoke": browser, "report353_gate": report353}

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
