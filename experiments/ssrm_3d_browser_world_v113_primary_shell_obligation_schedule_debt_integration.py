from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 353
SLUG = "ssrm_3d_browser_world_v113_primary_shell_obligation_schedule_debt_integration"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT352_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v112_primary_shell_selectable_obligation_resolution_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "353_ssrm_3d_browser_world_v113_primary_shell_obligation_schedule_debt_integration_report.md"

BOUNDARY = (
    "Browser-local obligation schedule/debt integration over the maintained v61 shell only; "
    "no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, "
    "production persistence, hosted URL proof, complete 3D engine, finished gameplay, or metaphysical claim."
)
NEXT_GATE = (
    "post-353: make one offscreen resident action change a different resident's visible obligation, schedule queue, "
    "and debt ledger while the avatar is absent, then prove it survives reload"
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
        "# Report 353: Browser World v113 Primary Shell Obligation Schedule/Debt Integration",
        "",
        "Report 353 keeps the work on one maintained playable shell. Report 352 made remembered obligations selectable and resolvable; this report connects those obligations to the visible schedule queue and debt ledger so the player sees consequences in the resident dashboard, not only in the obligation row.",
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
        f"- Pending schedule queue: `{browser.get('afterSecondReturn', {}).get('scheduleQueueText', 'missing')}`",
        f"- Pending debt ledger: `{browser.get('afterSecondReturn', {}).get('debtLedgerText', 'missing')}`",
        f"- Deferred schedule queue: `{browser.get('afterDefer', {}).get('scheduleQueueText', 'missing')}`",
        f"- Resolved schedule queue: `{browser.get('afterResolve', {}).get('scheduleQueueText', 'missing')}`",
        f"- Resolved debt ledger: `{browser.get('afterResolve', {}).get('debtLedgerText', 'missing')}`",
        f"- Schedule dashboard: `{browser.get('afterResolve', {}).get('schedule', 'missing')}`",
        f"- Debt dashboard: `{browser.get('afterResolve', {}).get('debt', 'missing')}`",
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
        "This is still a deterministic browser-local prototype, but it closes a real integration gap: a selected obligation now touches schedule and debt surfaces that reviewers already inspect. It is not subjective experience, autonomous language, production persistence, a hosted game, or a complete 3D engine.",
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
    report352 = load_json(REPORT352_RESULTS)
    browser = load_json(BROWSER_SMOKE)

    before = browser.get("beforeFirstReturn", {})
    pending = browser.get("afterSecondReturn", {})
    deferred = browser.get("afterDefer", {})
    resolved = browser.get("afterResolve", {})
    console_errors = browser.get("consoleErrors", [])

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_352_selectable_obligation_gate_passing", report352.get("verdict") == "pass" and report352.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 352 verdict={report352.get('verdict')} weakest={report352.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "source_exposes_schedule_queue_and_debt_ledger", has_terms(app_text, ["scheduleQueue", "debtLedger", "browser-local-obligation-schedule-queue-only", "browser-local-obligation-debt-ledger-only", "syncScheduleDebtFromObligation"]), "app.js exposes public scheduleQueue/debtLedger and sync function")
    add_criterion(criteria, "visible_schedule_debt_panels_wired", has_terms(index_text, ["scheduleQueueOut", "debtLedgerOut", "Schedule queue", "Debt ledger"]), "index.html exposes visible schedule queue and debt ledger panels")
    add_criterion(criteria, "bounded_actions_link_to_schedule_debt", has_terms(app_text, ["linkedLedger", "follow-up resolved: awning repair checked", "follow-up deferred: awning repair check queued", "syncScheduleDebtFromObligation(obligation, 'resolve')", "syncScheduleDebtFromObligation(obligation, 'defer')"]), "resolve/defer actions update resident schedule plus schedule/debt ledgers")
    add_criterion(criteria, "browser_smoke_artifact_exists", bool(browser), str(BROWSER_SMOKE.relative_to(ROOT)) if BROWSER_SMOKE.exists() else "missing browser smoke artifact")
    add_criterion(criteria, "browser_smoke_used_maintained_shell", "ssrm_3d_browser_world_v61_vertical_slice_app_shell" in browser.get("shellUrl", ""), browser.get("shellUrl", "missing shellUrl"))
    add_criterion(criteria, "pending_obligation_updates_schedule_queue", "pending" in pending.get("scheduleQueueText", "") and "follow-up advanced" in pending.get("scheduleQueueText", "") and "follow-up advanced" in pending.get("schedule", ""), f"schedule={pending.get('schedule')} queue={pending.get('scheduleQueueText')}")
    add_criterion(criteria, "pending_obligation_updates_debt_ledger", "outstanding" in pending.get("debtLedgerText", "") and "debt 1" in pending.get("debtLedgerText", "") and "1 / trust" in pending.get("debt", ""), f"debt={pending.get('debt')} ledger={pending.get('debtLedgerText')}")
    add_criterion(criteria, "defer_action_updates_schedule_queue_and_dashboard", "deferred" in deferred.get("scheduleQueueText", "") and "follow-up deferred" in deferred.get("schedule", ""), f"schedule={deferred.get('schedule')} queue={deferred.get('scheduleQueueText')}")
    add_criterion(criteria, "defer_action_updates_debt_ledger", "deferred" in deferred.get("debtLedgerText", "") and "debt 1" in deferred.get("debtLedgerText", ""), deferred.get("debtLedgerText", "missing debt ledger"))
    add_criterion(criteria, "resolve_action_updates_schedule_queue_and_dashboard", "resolved" in resolved.get("scheduleQueueText", "") and "follow-up resolved" in resolved.get("schedule", ""), f"schedule={resolved.get('schedule')} queue={resolved.get('scheduleQueueText')}")
    add_criterion(criteria, "resolve_action_updates_debt_ledger_and_dashboard", "settled" in resolved.get("debtLedgerText", "") and "debt 0" in resolved.get("debtLedgerText", "") and "0 / trust" in resolved.get("debt", ""), f"debt={resolved.get('debt')} ledger={resolved.get('debtLedgerText')}")
    add_criterion(criteria, "replay_history_include_linked_ledger", browser.get("resolveReplayLinkedLedger") is True and "obligation resolved" in browser.get("historyEvidence", ""), browser.get("historyEvidence", "missing history"))
    add_criterion(criteria, "browser_console_clean", len(console_errors) == 0, f"console error count={len(console_errors)}")
    add_criterion(criteria, "experiment_index_includes_report_353", "experiments.ssrm_3d_browser_world_v113_primary_shell_obligation_schedule_debt_integration" in runner_text, "scripts/run_experiments.py includes Report 353 module")
    add_criterion(criteria, "claim_boundary_preserved", all(term in BOUNDARY for term in ["no LLM call", "subjective consciousness", "moral patienthood", "finished gameplay"]), BOUNDARY)

    category_scores = {
        "review_gate_score": criteria[0]["score"],
        "source_behavior_score": min(criteria[1]["score"], criteria[2]["score"], criteria[3]["score"]),
        "browser_interaction_score": min(criteria[4]["score"], criteria[5]["score"]),
        "pending_schedule_debt_score": min(criteria[6]["score"], criteria[7]["score"]),
        "defer_schedule_debt_score": min(criteria[8]["score"], criteria[9]["score"]),
        "resolve_schedule_debt_score": min(criteria[10]["score"], criteria[11]["score"]),
        "replay_debug_score": criteria[12]["score"],
        "runtime_hygiene_score": criteria[13]["score"],
        "runner_index_score": criteria[14]["score"],
        "claim_hygiene_score": criteria[15]["score"],
    }
    weakest = min(category_scores.values())
    readiness = sum(category_scores.values()) / len(category_scores)
    metrics = {
        **category_scores,
        "weakest_channel_score": weakest,
        "readiness": readiness,
        "criterion_count": len(criteria),
        "before_replay_rows": int(before.get("replayRows", 0) or 0),
        "pending_replay_rows": int(pending.get("replayRows", 0) or 0),
        "deferred_replay_rows": int(deferred.get("replayRows", 0) or 0),
        "resolved_replay_rows": int(resolved.get("replayRows", 0) or 0),
        "before_trust": float(before.get("trust", 0.0) or 0.0),
        "resolved_trust": float(resolved.get("trust", 0.0) or 0.0),
        "before_progress": float(before.get("progress", 0.0) or 0.0),
        "resolved_progress": float(resolved.get("progress", 0.0) or 0.0),
        "console_error_count": len(console_errors),
    }
    verdict = "pass" if all(row["passed"] for row in criteria) else "fail"
    results = {"report": REPORT, "slug": SLUG, "verdict": verdict, "generated_at": datetime.now(timezone.utc).isoformat(), "boundary": BOUNDARY, "metrics": metrics, "criteria": criteria, "browser_smoke_artifact": str(BROWSER_SMOKE.relative_to(ROOT)), "next_gate": NEXT_GATE}
    state = {"report": REPORT, "shell_app": str(SHELL_APP.relative_to(ROOT)), "shell_index": str(SHELL_INDEX.relative_to(ROOT)), "browser_smoke": browser, "report352_gate": report352}

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
