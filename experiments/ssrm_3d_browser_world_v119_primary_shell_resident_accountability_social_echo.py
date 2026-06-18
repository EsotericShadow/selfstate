from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 359
SLUG = "ssrm_3d_browser_world_v119_primary_shell_resident_accountability_social_echo"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT358_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v118_primary_shell_accountability_return_greeting_continuity_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "359_ssrm_3d_browser_world_v119_primary_shell_resident_accountability_social_echo_report.md"

BOUNDARY = (
    "Browser-local resident-to-resident accountability social echo over the maintained v61 shell only; "
    "no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, "
    "production persistence, hosted URL proof, complete 3D engine, finished gameplay, or metaphysical claim."
)
NEXT_GATE = (
    "post-359: make the echoed accountability memory influence a later bounded conversation answer from Fay while "
    "keeping phrasebook-only language and the no-LLM boundary explicit"
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
        "# Report 359: Browser World v119 Primary Shell Resident Accountability Social Echo",
        "",
        "Report 359 keeps the work in the maintained v61 shell and moves the Report 358 return greeting into resident-to-resident memory. After Milo links the resolved offscreen obligation with the accounted avatar absence, `Run social pulse` lets Fay hear and retain that echo without a direct avatar command, while the original offscreen cause chain remains visible.",
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
        f"- Before social pulse: `{browser.get('beforeSocialPulse', {}).get('accountabilitySocialEchoText', 'missing')}`",
        f"- After social pulse: `{browser.get('afterSocialPulse', {}).get('accountabilitySocialEchoText', 'missing')}`",
        f"- After reload echo: `{browser.get('afterReload', {}).get('accountabilitySocialEchoText', 'missing')}`",
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
        "This remains deterministic browser-local state, not autonomous social understanding. The useful step is integration: another resident can carry forward the consequence chain through resident social memory, and the receipt explicitly says it was not caused by a direct avatar command.",
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
    report358 = load_json(REPORT358_RESULTS)
    browser = load_json(BROWSER_SMOKE)

    before_social = browser.get("beforeSocialPulse", {})
    after_social = browser.get("afterSocialPulse", {})
    after_reload = browser.get("afterReload", {})
    console_errors = browser.get("consoleErrors", [])
    echo = after_social.get("accountabilitySocialEcho", {})
    reload_echo = after_reload.get("accountabilitySocialEcho", {})

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_358_return_greeting_gate_passing", report358.get("verdict") == "pass" and report358.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 358 verdict={report358.get('verdict')} weakest={report358.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "source_exposes_social_echo_state", has_terms(app_text, ["accountabilitySocialEcho", "renderAccountabilitySocialEcho", "propagateAccountabilitySocialEcho", "browser-local-accountability-social-echo-only"]), "app.js exposes accountability social echo state, render, propagation, and boundary")
    add_criterion(criteria, "source_binds_echo_to_social_pulse", has_terms(app_text, ["const accountabilitySocialEcho = propagateAccountabilitySocialEcho()", "runSocialMemoryPulse", "directAvatarCommand: false"]), "runSocialMemoryPulse propagates echo with directAvatarCommand false")
    add_criterion(criteria, "source_preserves_original_offscreen_history", has_terms(app_text, ["offscreenObligationEvents", "residentHistoryPreserved", "Fay", "Milo", "resident-to-resident accountability echo"]), "social echo checks original offscreen event/history and records Fay/Milo history")
    add_criterion(criteria, "visible_social_echo_panel_wired", has_terms(index_text, ["accountabilitySocialEchoOut", "Resident echo"]), "index.html exposes Resident echo dashboard panel")
    add_criterion(criteria, "public_state_boundary_includes_social_echo", has_terms(app_text, ["accountabilitySocialEcho", "publicState", "runStateBoundaryAudit"]), "state-boundary audit public world includes accountability social echo")
    add_criterion(criteria, "browser_smoke_artifact_exists", bool(browser), str(BROWSER_SMOKE.relative_to(ROOT)) if BROWSER_SMOKE.exists() else "missing browser smoke artifact")
    add_criterion(criteria, "browser_smoke_used_maintained_shell", "ssrm_3d_browser_world_v61_vertical_slice_app_shell" in browser.get("shellUrl", ""), browser.get("shellUrl", "missing shellUrl"))
    add_criterion(criteria, "before_social_echo_empty_after_return", "No resident-to-resident accountability echo yet" in before_social.get("accountabilitySocialEchoText", ""), before_social.get("accountabilitySocialEchoText", "missing echo text"))
    add_criterion(criteria, "social_pulse_creates_fay_echo", echo.get("sourceResident") == "Milo" and echo.get("echoResident") == "Fay" and echo.get("residentThreadId") == "milo-offscreen-water-jars", f"echo={echo}")
    add_criterion(criteria, "echo_mentions_resolved_obligation_and_accounted_absence", "Fay heard Milo" in after_social.get("accountabilitySocialEchoText", "") and "milo-offscreen-water-jars resolved/resolved" in after_social.get("accountabilitySocialEchoText", "") and "avatar absence accounted" in after_social.get("accountabilitySocialEchoText", ""), after_social.get("accountabilitySocialEchoText", "missing echo text"))
    add_criterion(criteria, "echo_not_direct_avatar_command", echo.get("directAvatarCommand") is False and "Direct avatar command: no" in after_social.get("accountabilitySocialEchoText", ""), f"echo={echo} text={after_social.get('accountabilitySocialEchoText')}")
    add_criterion(criteria, "visible_echo_still_names_original_event", "Fay changed Milo" in after_social.get("accountabilitySocialEchoText", "") and "Direct avatar command: no" in after_social.get("accountabilitySocialEchoText", ""), after_social.get("accountabilitySocialEchoText", "missing echo text"))
    add_criterion(criteria, "relationship_memory_carries_echo", "Milo" in after_social.get("relationshipMemoryText", "") and "Fay heard Milo" in after_social.get("relationshipMemoryText", "") and "Fay changed Milo" in after_social.get("relationshipMemoryText", ""), after_social.get("relationshipMemoryText", "missing relationship memory"))
    add_criterion(criteria, "schedule_debt_stay_resolved_after_echo", "Milo schedule resolved" in after_social.get("scheduleQueueText", "") and "Milo debt settled" in after_social.get("debtLedgerText", ""), f"schedule={after_social.get('scheduleQueueText')} debt={after_social.get('debtLedgerText')}")
    add_criterion(criteria, "social_echo_survives_reload", reload_echo.get("sourceResident") == "Milo" and reload_echo.get("echoResident") == "Fay" and reload_echo.get("directAvatarCommand") is False and "Direct avatar command: no" in after_reload.get("accountabilitySocialEchoText", ""), f"reload_echo={reload_echo} text={after_reload.get('accountabilitySocialEchoText')}")
    add_criterion(criteria, "replay_logs_social_echo", browser.get("replayHasSocialEcho") is True and browser.get("socialEchoReloaded") is True, f"replayHasSocialEcho={browser.get('replayHasSocialEcho')} socialEchoReloaded={browser.get('socialEchoReloaded')}")
    add_criterion(criteria, "browser_console_clean", len(console_errors) == 0, f"console error count={len(console_errors)}")
    add_criterion(criteria, "experiment_index_includes_report_359", "experiments.ssrm_3d_browser_world_v119_primary_shell_resident_accountability_social_echo" in runner_text, "scripts/run_experiments.py includes Report 359 module")
    add_criterion(criteria, "claim_boundary_preserved", all(term in BOUNDARY for term in ["no LLM call", "subjective consciousness", "moral patienthood", "finished gameplay"]), BOUNDARY)

    category_scores = {
        "review_gate_score": criteria[0]["score"],
        "source_behavior_score": min(criteria[1]["score"], criteria[2]["score"], criteria[3]["score"], criteria[5]["score"]),
        "visible_binding_score": criteria[4]["score"],
        "browser_interaction_score": min(criteria[6]["score"], criteria[7]["score"]),
        "empty_state_score": criteria[8]["score"],
        "social_echo_score": min(criteria[9]["score"], criteria[10]["score"], criteria[11]["score"]),
        "history_preservation_score": min(criteria[12]["score"], criteria[13]["score"], criteria[14]["score"]),
        "reload_persistence_score": criteria[15]["score"],
        "replay_debug_score": criteria[16]["score"],
        "runtime_hygiene_score": criteria[17]["score"],
        "runner_index_score": criteria[18]["score"],
        "claim_hygiene_score": criteria[19]["score"],
    }
    weakest = min(category_scores.values())
    readiness = sum(category_scores.values()) / len(category_scores)
    metrics = {
        **category_scores,
        "weakest_channel_score": weakest,
        "readiness": readiness,
        "criterion_count": len(criteria),
        "before_social_replay_rows": int(before_social.get("replayRows", 0) or 0),
        "after_social_replay_rows": int(after_social.get("replayRows", 0) or 0),
        "after_reload_replay_rows": int(after_reload.get("replayRows", 0) or 0),
        "console_error_count": len(console_errors),
    }
    verdict = "pass" if all(row["passed"] for row in criteria) else "fail"
    results = {"report": REPORT, "slug": SLUG, "verdict": verdict, "generated_at": datetime.now(timezone.utc).isoformat(), "boundary": BOUNDARY, "metrics": metrics, "criteria": criteria, "browser_smoke_artifact": str(BROWSER_SMOKE.relative_to(ROOT)), "next_gate": NEXT_GATE}
    state = {"report": REPORT, "shell_app": str(SHELL_APP.relative_to(ROOT)), "browser_smoke": browser, "report358_gate": report358}

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
