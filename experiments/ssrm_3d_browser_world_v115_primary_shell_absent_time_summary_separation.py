from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 355
SLUG = "ssrm_3d_browser_world_v115_primary_shell_absent_time_summary_separation"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT354_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v114_primary_shell_offscreen_cross_resident_obligation_persistence_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "355_ssrm_3d_browser_world_v115_primary_shell_absent_time_summary_separation_report.md"

BOUNDARY = (
    "Browser-local absent-time summary separation over the maintained v61 shell only; "
    "no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, "
    "production persistence, hosted URL proof, complete 3D engine, finished gameplay, or metaphysical claim."
)
NEXT_GATE = (
    "post-355: add one bounded player choice from the absent-time summary that selects whether to handle the "
    "avatar-caused thread or the resident-caused offscreen thread first, then prove the unchosen thread remains pending"
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
        "# Report 355: Browser World v115 Primary Shell Absent-Time Summary Separation",
        "",
        "Report 355 keeps the integration work inside the maintained v61 shell. Report 354 made offscreen resident activity create a persistent cross-resident obligation; this report adds a small visible absent-time summary that separates avatar-caused absence from resident-caused offscreen changes before the player chooses which obligation to handle.",
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
        f"- Before summary: `{browser.get('beforeOffscreen', {}).get('absentTimeSummaryText', 'missing')}`",
        f"- After summary: `{browser.get('afterOffscreen', {}).get('absentTimeSummaryText', 'missing')}`",
        f"- After reload summary: `{browser.get('afterReload', {}).get('absentTimeSummaryText', 'missing')}`",
        f"- Obligation list before choice: `{browser.get('afterOffscreen', {}).get('obligationListText', 'missing')}`",
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
        "This improves readability of offscreen life: the player can see what they caused by waiting separately from what residents did while absent. It remains deterministic browser-local UI/state, not subjective experience, autonomous language, production persistence, hosted gameplay, or a complete 3D engine.",
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
    report354 = load_json(REPORT354_RESULTS)
    browser = load_json(BROWSER_SMOKE)

    before = browser.get("beforeOffscreen", {})
    after = browser.get("afterOffscreen", {})
    reload = browser.get("afterReload", {})
    summary = after.get("absentTimeSummary", {})
    reload_summary = reload.get("absentTimeSummary", {})
    console_errors = browser.get("consoleErrors", [])

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_354_offscreen_gate_passing", report354.get("verdict") == "pass" and report354.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 354 verdict={report354.get('verdict')} weakest={report354.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "source_exposes_absent_time_summary", has_terms(app_text, ["absentTimeSummary", "renderAbsentTimeSummary", "updateAbsentTimeSummary", "browser-local-absent-time-summary-only"]), "app.js exposes absentTimeSummary state, render, update, and boundary")
    add_criterion(criteria, "visible_absent_time_panel_wired", has_terms(index_text, ["absentTimeSummaryOut", "Absent time"]), "index.html exposes Absent time dashboard panel")
    add_criterion(criteria, "wait_offscreen_updates_summary_before_log", has_terms(app_text, ["updateAbsentTimeSummary(offscreenObligation)", "absentTimeSummary: world.absentTimeSummary", "before-obligation-choice"]), "waitOffscreen updates summary before replay log")
    add_criterion(criteria, "browser_smoke_artifact_exists", bool(browser), str(BROWSER_SMOKE.relative_to(ROOT)) if BROWSER_SMOKE.exists() else "missing browser smoke artifact")
    add_criterion(criteria, "browser_smoke_used_maintained_shell", "ssrm_3d_browser_world_v61_vertical_slice_app_shell" in browser.get("shellUrl", ""), browser.get("shellUrl", "missing shellUrl"))
    add_criterion(criteria, "before_offscreen_summary_empty", "No absent-time summary yet" in before.get("absentTimeSummaryText", ""), before.get("absentTimeSummaryText", "missing summary text"))
    add_criterion(criteria, "summary_separates_avatar_caused_changes", "Avatar-caused:" in after.get("absentTimeSummaryText", "") and "avatar chose Wait offscreen" in after.get("absentTimeSummaryText", "") and "avatar did not choose the new obligation target" in after.get("absentTimeSummaryText", ""), after.get("absentTimeSummaryText", "missing summary text"))
    add_criterion(criteria, "summary_separates_resident_caused_changes", "Resident-caused:" in after.get("absentTimeSummaryText", "") and "Fay changed Milo" in after.get("absentTimeSummaryText", "") and "milo-offscreen-water-jars" in after.get("absentTimeSummaryText", ""), after.get("absentTimeSummaryText", "missing summary text"))
    add_criterion(criteria, "summary_marks_before_obligation_choice", summary.get("phase") == "before-obligation-choice" and "Before choosing:" in after.get("absentTimeSummaryText", "") and "selectable before resolve/defer" in after.get("absentTimeSummaryText", ""), f"phase={summary.get('phase')} text={after.get('absentTimeSummaryText')}")
    add_criterion(criteria, "summary_links_to_visible_obligation", summary.get("obligationId") == "milo-offscreen-water-jars" and "milo-offscreen-water-jars" in after.get("obligationListText", ""), f"summary obligation={summary.get('obligationId')} list={after.get('obligationListText')}")
    add_criterion(criteria, "summary_links_to_schedule_and_debt_status", summary.get("scheduleQueueStatus") == "pending" and summary.get("debtLedgerStatus") == "outstanding" and "Milo schedule pending" in after.get("scheduleQueueText", "") and "Milo debt outstanding" in after.get("debtLedgerText", ""), f"summary={summary} schedule={after.get('scheduleQueueText')} debt={after.get('debtLedgerText')}")
    add_criterion(criteria, "summary_survives_reload", reload_summary.get("phase") == "before-obligation-choice" and "Avatar-caused:" in reload.get("absentTimeSummaryText", "") and "Resident-caused:" in reload.get("absentTimeSummaryText", "") and "milo-offscreen-water-jars" in reload.get("absentTimeSummaryText", ""), reload.get("absentTimeSummaryText", "missing reload summary"))
    add_criterion(criteria, "replay_logs_absent_summary", browser.get("waitOffscreenReplayHasAbsentSummary") is True and browser.get("summaryReloaded") is True, f"waitOffscreenReplayHasAbsentSummary={browser.get('waitOffscreenReplayHasAbsentSummary')} summaryReloaded={browser.get('summaryReloaded')}")
    add_criterion(criteria, "browser_console_clean", len(console_errors) == 0, f"console error count={len(console_errors)}")
    add_criterion(criteria, "experiment_index_includes_report_355", "experiments.ssrm_3d_browser_world_v115_primary_shell_absent_time_summary_separation" in runner_text, "scripts/run_experiments.py includes Report 355 module")
    add_criterion(criteria, "claim_boundary_preserved", all(term in BOUNDARY for term in ["no LLM call", "subjective consciousness", "moral patienthood", "finished gameplay"]), BOUNDARY)

    category_scores = {
        "review_gate_score": criteria[0]["score"],
        "source_behavior_score": min(criteria[1]["score"], criteria[2]["score"], criteria[3]["score"]),
        "browser_interaction_score": min(criteria[4]["score"], criteria[5]["score"]),
        "empty_state_score": criteria[6]["score"],
        "separation_score": min(criteria[7]["score"], criteria[8]["score"]),
        "before_choice_score": criteria[9]["score"],
        "visible_binding_score": min(criteria[10]["score"], criteria[11]["score"]),
        "reload_persistence_score": criteria[12]["score"],
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
    state = {"report": REPORT, "shell_app": str(SHELL_APP.relative_to(ROOT)), "browser_smoke": browser, "report354_gate": report354}

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
