from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 360
SLUG = "ssrm_3d_browser_world_v120_primary_shell_bounded_fay_echo_conversation"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT359_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v119_primary_shell_resident_accountability_social_echo_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "360_ssrm_3d_browser_world_v120_primary_shell_bounded_fay_echo_conversation_report.md"

BOUNDARY = (
    "Browser-local bounded Fay echo conversation over the maintained v61 shell only; "
    "phrasebook-only reply generation, no LLM call, no autonomous natural language, no subjective consciousness, "
    "no real consent, no moral patienthood, no production persistence, no hosted URL proof, no complete 3D engine, "
    "no finished gameplay, and no metaphysical claim."
)
NEXT_GATE = (
    "post-360: let the bounded echoed conversation change one later resident-facing choice or refusal while preserving "
    "source attribution, recoverability, and the no-consciousness/no-LLM boundary"
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
        "# Report 360: Browser World v120 Primary Shell Bounded Fay Echo Conversation",
        "",
        "Report 360 keeps the work inside the maintained v61 browser shell and makes the Report 359 resident-to-resident accountability echo available to a later bounded Fay conversation. Fay does not improvise language. The `Talk` path can only produce a phrasebook-limited reply when Fay is selected and the carried echo already exists, and the visible receipt marks the reply as no-LLM, not autonomous natural language, and phrasebook-only.",
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
        f"- Before conversation: `{browser.get('beforeConversation', {}).get('boundedEchoConversationText', 'missing')}`",
        f"- After conversation: `{browser.get('afterConversation', {}).get('boundedEchoConversationText', 'missing')}`",
        f"- After reload: `{browser.get('afterReload', {}).get('boundedEchoConversationText', 'missing')}`",
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
        "This is still deterministic browser-local state. The useful step is not intelligence or consciousness; it is source-bounded conversational continuity. A resident-facing utterance can now depend on a prior resident social memory while remaining phrasebook-only and inspectable in replay, history, and public receipts.",
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
    report359 = load_json(REPORT359_RESULTS)
    browser = load_json(BROWSER_SMOKE)

    before = browser.get("beforeConversation", {})
    after = browser.get("afterConversation", {})
    reload = browser.get("afterReload", {})
    console_errors = browser.get("consoleErrors", [])
    conversation = after.get("boundedEchoConversation", {})
    reload_conversation = reload.get("boundedEchoConversation", {})
    conversation_text = after.get("boundedEchoConversationText", "")
    reload_text = reload.get("boundedEchoConversationText", "")
    trace_text = after.get("traceText", "")
    history_text = after.get("residentHistoryText", "")
    relationship_text = after.get("relationshipMemoryText", "")

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_359_social_echo_gate_passing", report359.get("verdict") == "pass" and report359.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 359 verdict={report359.get('verdict')} weakest={report359.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "source_exposes_bounded_echo_conversation_state", has_terms(app_text, ["boundedEchoConversation", "renderBoundedEchoConversation", "buildBoundedEchoConversation", "browser-local-bounded-echo-conversation-only"]), "app.js exposes bounded echo conversation state, renderer, builder, and boundary")
    add_criterion(criteria, "source_binds_conversation_to_talk", has_terms(app_text, ["const boundedEchoConversation = buildBoundedEchoConversation(phrase)", "talkBounded", "phrasebookOnly: true", "noLLM: true", "autonomousLanguage: false"]), "talkBounded attempts bounded echo conversation and logs no-LLM phrasebook metadata")
    add_criterion(criteria, "source_limits_conversation_to_fay_echo_and_safe_phrases", has_terms(app_text, ["world.selected !== echo.echoResident", "['greet', 'ask_schedule', 'ask_debt']", "echo.echoResident", "echo.sourceResident"]), "builder requires selected echo resident and a small phrasebook subset")
    add_criterion(criteria, "visible_echo_conversation_panel_wired", has_terms(index_text, ["boundedEchoConversationOut", "Echo conversation"]), "index.html exposes Echo conversation dashboard panel")
    add_criterion(criteria, "public_state_boundary_includes_bounded_conversation", has_terms(app_text, ["boundedEchoConversation", "publicState", "runStateBoundaryAudit"]), "state-boundary audit public world includes bounded conversation receipt")
    add_criterion(criteria, "browser_smoke_artifact_exists", bool(browser), str(BROWSER_SMOKE.relative_to(ROOT)) if BROWSER_SMOKE.exists() else "missing browser smoke artifact")
    add_criterion(criteria, "browser_smoke_used_maintained_shell", "ssrm_3d_browser_world_v61_vertical_slice_app_shell" in browser.get("shellUrl", ""), browser.get("shellUrl", "missing shellUrl"))
    add_criterion(criteria, "before_conversation_empty_after_social_echo", "No bounded echo conversation yet" in before.get("boundedEchoConversationText", ""), before.get("boundedEchoConversationText", "missing conversation text"))
    add_criterion(criteria, "fay_conversation_created_from_echo", conversation.get("resident") == "Fay" and conversation.get("sourceResident") == "Milo" and conversation.get("sourceEchoId") == "milo-offscreen-water-jars", f"conversation={conversation}")
    add_criterion(criteria, "conversation_visible_text_references_source_chain", "Resident: Fay" in conversation_text and "Phrase: greet" in conversation_text and "milo-offscreen-water-jars" in conversation_text and "resolved/resolved" in conversation_text and "avatar absence accounted" in conversation_text, conversation_text or "missing conversation text")
    add_criterion(criteria, "conversation_marks_no_llm_and_phrasebook_only", conversation.get("noLLM") is True and conversation.get("autonomousLanguage") is False and conversation.get("phrasebookOnly") is True and "No LLM: yes" in conversation_text and "Autonomous language: no" in conversation_text and "Phrasebook only: yes" in conversation_text, f"conversation={conversation} text={conversation_text}")
    add_criterion(criteria, "conversation_preserves_not_direct_avatar_command", conversation.get("directAvatarCommand") is False and after.get("accountabilitySocialEcho", {}).get("directAvatarCommand") is False, f"conversation={conversation} echo={after.get('accountabilitySocialEcho')}")
    add_criterion(criteria, "resident_history_records_bounded_echo_reply", "bounded echo conversation" in history_text and "phrasebook only true" in history_text and "bounded echo reply referenced milo-offscreen-water-jars" in history_text, history_text or "missing resident history")
    add_criterion(criteria, "relationship_memory_still_carries_original_echo", "Fay heard Milo" in relationship_text and "Fay changed Milo" in relationship_text and "milo-offscreen-water-jars" in relationship_text, relationship_text or "missing relationship memory")
    add_criterion(criteria, "replay_logs_talk_payload_and_boundary", browser.get("replayHasBoundedConversation") is True and "talkBounded" in trace_text and "phrasebookOnly" in trace_text and "noLLM" in trace_text, f"replayHasBoundedConversation={browser.get('replayHasBoundedConversation')} trace={trace_text}")
    add_criterion(criteria, "bounded_conversation_survives_reload", reload_conversation.get("resident") == "Fay" and reload_conversation.get("sourceEchoId") == "milo-offscreen-water-jars" and "Phrasebook only: yes" in reload_text, f"reload_conversation={reload_conversation} text={reload_text}")
    add_criterion(criteria, "browser_console_clean", len(console_errors) == 0, f"console error count={len(console_errors)}")
    add_criterion(criteria, "experiment_index_includes_report_360", "experiments.ssrm_3d_browser_world_v120_primary_shell_bounded_fay_echo_conversation" in runner_text, "scripts/run_experiments.py includes Report 360 module")
    add_criterion(criteria, "claim_boundary_preserved", all(term in BOUNDARY for term in ["phrasebook-only", "no LLM call", "subjective consciousness", "moral patienthood", "finished gameplay"]), BOUNDARY)

    category_scores = {
        "review_gate_score": criteria[0]["score"],
        "source_behavior_score": min(criteria[1]["score"], criteria[2]["score"], criteria[3]["score"], criteria[5]["score"]),
        "visible_binding_score": criteria[4]["score"],
        "browser_interaction_score": min(criteria[6]["score"], criteria[7]["score"]),
        "empty_state_score": criteria[8]["score"],
        "conversation_generation_score": min(criteria[9]["score"], criteria[10]["score"], criteria[11]["score"], criteria[12]["score"]),
        "memory_continuity_score": min(criteria[13]["score"], criteria[14]["score"]),
        "replay_debug_score": criteria[15]["score"],
        "reload_persistence_score": criteria[16]["score"],
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
        "before_replay_rows": int(before.get("replayRows", 0) or 0),
        "after_replay_rows": int(after.get("replayRows", 0) or 0),
        "after_reload_replay_rows": int(reload.get("replayRows", 0) or 0),
        "console_error_count": len(console_errors),
    }
    verdict = "pass" if all(row["passed"] for row in criteria) else "fail"
    results = {"report": REPORT, "slug": SLUG, "verdict": verdict, "generated_at": datetime.now(timezone.utc).isoformat(), "boundary": BOUNDARY, "metrics": metrics, "criteria": criteria, "browser_smoke_artifact": str(BROWSER_SMOKE.relative_to(ROOT)), "next_gate": NEXT_GATE}
    state = {"report": REPORT, "shell_app": str(SHELL_APP.relative_to(ROOT)), "browser_smoke": browser, "report359_gate": report359}

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
