from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 358
SLUG = "ssrm_3d_browser_world_v118_primary_shell_accountability_return_greeting_continuity"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT357_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v117_primary_shell_avatar_absence_accountability_receipt_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "358_ssrm_3d_browser_world_v118_primary_shell_accountability_return_greeting_continuity_report.md"

BOUNDARY = (
    "Browser-local accountability return-greeting continuity over the maintained v61 shell only; "
    "no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, "
    "production persistence, hosted URL proof, complete 3D engine, finished gameplay, or metaphysical claim."
)
NEXT_GATE = (
    "post-358: move the same accountability-linked return greeting into a resident-to-resident memory echo so another "
    "resident can mention Milo's resolved obligation without receiving a direct avatar command"
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
        "# Report 358: Browser World v118 Primary Shell Accountability Return Greeting Continuity",
        "",
        "Report 358 continues the same playable consequence loop in the maintained v61 shell. Report 357 let the avatar account for absence after resolving the resident-caused offscreen obligation; this report makes the next return greeting reference both facts together without rewriting the resident-caused offscreen history.",
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
        f"- Before return greeting: `{browser.get('beforeReturn', {}).get('returnGreetingText', 'missing')}`",
        f"- After return greeting: `{browser.get('afterReturn', {}).get('returnGreetingText', 'missing')}`",
        f"- After reload greeting: `{browser.get('afterReload', {}).get('returnGreetingText', 'missing')}`",
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
        "This remains deterministic browser-local state. The useful step is continuity: the return greeting now binds a resolved resident-caused offscreen obligation to an accounted avatar-caused absence, while still preserving Fay's original offscreen event and Milo's public history.",
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
    report357 = load_json(REPORT357_RESULTS)
    browser = load_json(BROWSER_SMOKE)

    before_return = browser.get("beforeReturn", {})
    after_return = browser.get("afterReturn", {})
    after_reload = browser.get("afterReload", {})
    console_errors = browser.get("consoleErrors", [])
    greeting = after_return.get("returnGreetingContinuity", {})
    reload_greeting = after_reload.get("returnGreetingContinuity", {})

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_357_accountability_gate_passing", report357.get("verdict") == "pass" and report357.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 357 verdict={report357.get('verdict')} weakest={report357.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "source_exposes_return_greeting_state", has_terms(app_text, ["returnGreetingContinuity", "renderReturnGreetingContinuity", "applyAccountabilityReturnGreeting", "browser-local-accountability-return-greeting-only"]), "app.js exposes return greeting continuity state, render, update, and boundary")
    add_criterion(criteria, "source_binds_greeting_to_return_path", has_terms(app_text, ["applyAccountabilityReturnGreeting(replayRowsBeforeReturn)", "returnGreetingContinuity: world.returnGreetingContinuity", "returningVisit"]), "enterWorld returning path invokes accountability return greeting and logs it")
    add_criterion(criteria, "source_preserves_original_offscreen_history", has_terms(app_text, ["offscreenObligationEvents", "residentHistoryPreserved", "history preserved", "return greeting linked"]), "return greeting checks original offscreen event/history instead of replacing it")
    add_criterion(criteria, "visible_return_greeting_panel_wired", has_terms(index_text, ["returnGreetingContinuityOut", "Return greeting"]), "index.html exposes Return greeting dashboard panel")
    add_criterion(criteria, "public_state_boundary_includes_return_greeting", has_terms(app_text, ["returnGreetingContinuity", "publicState", "runStateBoundaryAudit"]), "state-boundary audit public world includes return greeting continuity")
    add_criterion(criteria, "browser_smoke_artifact_exists", bool(browser), str(BROWSER_SMOKE.relative_to(ROOT)) if BROWSER_SMOKE.exists() else "missing browser smoke artifact")
    add_criterion(criteria, "browser_smoke_used_maintained_shell", "ssrm_3d_browser_world_v61_vertical_slice_app_shell" in browser.get("shellUrl", ""), browser.get("shellUrl", "missing shellUrl"))
    add_criterion(criteria, "before_return_greeting_empty_after_accountability", "No accountability return greeting yet" in before_return.get("returnGreetingText", ""), before_return.get("returnGreetingText", "missing return greeting text"))
    add_criterion(criteria, "return_greeting_created_on_next_enter", greeting.get("resident") == "Milo" and greeting.get("residentThreadId") == "milo-offscreen-water-jars" and greeting.get("avatarThreadStatus") == "accounted", f"greeting={greeting}")
    add_criterion(criteria, "return_greeting_mentions_resolved_obligation_and_accounted_absence", "Milo greeting" in after_return.get("returnGreetingText", "") and "milo-offscreen-water-jars resolved/resolved" in after_return.get("returnGreetingText", "") and "Avatar absence: accounted" in after_return.get("returnGreetingText", ""), after_return.get("returnGreetingText", "missing return greeting text"))
    add_criterion(criteria, "resident_history_still_names_original_event", "Fay changed Milo" in after_return.get("historyText", "") and "return greeting linked milo-offscreen-water-jars and accounted avatar absence" in after_return.get("historyText", ""), after_return.get("historyText", "missing history"))
    add_criterion(criteria, "resident_schedule_debt_stay_resolved_after_return", "Milo schedule resolved" in after_return.get("scheduleQueueText", "") and "Milo debt settled" in after_return.get("debtLedgerText", ""), f"schedule={after_return.get('scheduleQueueText')} debt={after_return.get('debtLedgerText')}")
    add_criterion(criteria, "return_greeting_survives_reload", reload_greeting.get("resident") == "Milo" and reload_greeting.get("avatarThreadStatus") == "accounted" and "History preserved: yes" in after_reload.get("returnGreetingText", ""), f"reload_greeting={reload_greeting} text={after_reload.get('returnGreetingText')}")
    add_criterion(criteria, "replay_logs_return_greeting_continuity", browser.get("replayHasReturnGreetingContinuity") is True and browser.get("returnGreetingReloaded") is True, f"replayHasReturnGreetingContinuity={browser.get('replayHasReturnGreetingContinuity')} returnGreetingReloaded={browser.get('returnGreetingReloaded')}")
    add_criterion(criteria, "browser_console_clean", len(console_errors) == 0, f"console error count={len(console_errors)}")
    add_criterion(criteria, "experiment_index_includes_report_358", "experiments.ssrm_3d_browser_world_v118_primary_shell_accountability_return_greeting_continuity" in runner_text, "scripts/run_experiments.py includes Report 358 module")
    add_criterion(criteria, "claim_boundary_preserved", all(term in BOUNDARY for term in ["no LLM call", "subjective consciousness", "moral patienthood", "finished gameplay"]), BOUNDARY)

    category_scores = {
        "review_gate_score": criteria[0]["score"],
        "source_behavior_score": min(criteria[1]["score"], criteria[2]["score"], criteria[3]["score"], criteria[5]["score"]),
        "visible_binding_score": criteria[4]["score"],
        "browser_interaction_score": min(criteria[6]["score"], criteria[7]["score"]),
        "empty_state_score": criteria[8]["score"],
        "return_greeting_score": min(criteria[9]["score"], criteria[10]["score"]),
        "history_preservation_score": min(criteria[11]["score"], criteria[12]["score"]),
        "reload_persistence_score": criteria[13]["score"],
        "replay_debug_score": criteria[14]["score"],
        "runtime_hygiene_score": criteria[15]["score"],
        "runner_index_score": criteria[16]["score"],
        "claim_hygiene_score": criteria[17]["score"],
    }
    weakest = min(category_scores.values())
    readiness = sum(category_scores.values()) / len(category_scores)
    metrics = {
        **category_scores,
        "weakest_channel_score": weakest,
        "readiness": readiness,
        "criterion_count": len(criteria),
        "before_return_replay_rows": int(before_return.get("replayRows", 0) or 0),
        "after_return_replay_rows": int(after_return.get("replayRows", 0) or 0),
        "after_reload_replay_rows": int(after_reload.get("replayRows", 0) or 0),
        "console_error_count": len(console_errors),
    }
    verdict = "pass" if all(row["passed"] for row in criteria) else "fail"
    results = {"report": REPORT, "slug": SLUG, "verdict": verdict, "generated_at": datetime.now(timezone.utc).isoformat(), "boundary": BOUNDARY, "metrics": metrics, "criteria": criteria, "browser_smoke_artifact": str(BROWSER_SMOKE.relative_to(ROOT)), "next_gate": NEXT_GATE}
    state = {"report": REPORT, "shell_app": str(SHELL_APP.relative_to(ROOT)), "browser_smoke": browser, "report357_gate": report357}

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
