from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 361
SLUG = "ssrm_3d_browser_world_v121_primary_shell_echo_influenced_choice_refusal"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT360_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v120_primary_shell_bounded_fay_echo_conversation_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "361_ssrm_3d_browser_world_v121_primary_shell_echo_influenced_choice_refusal_report.md"

BOUNDARY = (
    "Browser-local echo-influenced choice/refusal over the maintained v61 shell only; "
    "phrasebook-only receipts, no LLM call, no autonomous natural language, no subjective consciousness, "
    "no real consent, no moral patienthood, no production persistence, no hosted URL proof, no complete 3D engine, "
    "no finished gameplay, and no metaphysical claim."
)
NEXT_GATE = (
    "post-361: make the source-bounded refusal/choice affect one later recoverable trust or task branch while keeping "
    "history attribution, replay audit, and no-LLM boundaries visible"
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
        "# Report 361: Browser World v121 Primary Shell Echo-Influenced Choice Refusal",
        "",
        "Report 361 keeps the work in the maintained v61 browser shell and makes Fay's bounded echo conversation affect a later resident-facing choice. After Fay carries Milo's accountability echo and answers through the phrasebook-only `Talk` path, `Offer help` now creates an Echo choice receipt: Fay accepts source-bounded help for the remembered obligation while refusing to rewrite the original cause chain or treat the avatar as a direct source command.",
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
        f"- Before choice: `{browser.get('beforeChoice', {}).get('echoInfluencedChoiceText', 'missing')}`",
        f"- After choice: `{browser.get('afterChoice', {}).get('echoInfluencedChoiceText', 'missing')}`",
        f"- After reload: `{browser.get('afterReload', {}).get('echoInfluencedChoiceText', 'missing')}`",
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
        "This is still deterministic browser-local state. The useful integration step is that resident memory now changes a later action affordance: Fay can accept help in a constrained way and refuse history rewriting, with the refusal visible as a recoverable receipt rather than hidden agent interior or autonomous language.",
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
    report360 = load_json(REPORT360_RESULTS)
    browser = load_json(BROWSER_SMOKE)

    before = browser.get("beforeChoice", {})
    after = browser.get("afterChoice", {})
    reload = browser.get("afterReload", {})
    console_errors = browser.get("consoleErrors", [])
    choice = after.get("echoInfluencedChoiceReceipt", {})
    reload_choice = reload.get("echoInfluencedChoiceReceipt", {})
    choice_text = after.get("echoInfluencedChoiceText", "")
    reload_text = reload.get("echoInfluencedChoiceText", "")
    trace_text = after.get("traceText", "")
    history_text = after.get("residentHistoryText", "")
    relationship_text = after.get("relationshipMemoryText", "")

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_360_bounded_conversation_gate_passing", report360.get("verdict") == "pass" and report360.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 360 verdict={report360.get('verdict')} weakest={report360.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "source_exposes_echo_choice_state", has_terms(app_text, ["echoInfluencedChoiceReceipt", "renderEchoInfluencedChoiceReceipt", "applyEchoInfluencedChoiceReceipt", "browser-local-echo-influenced-choice-refusal-only"]), "app.js exposes echo-influenced choice state, renderer, builder, and boundary")
    add_criterion(criteria, "source_binds_choice_to_offer_help", has_terms(app_text, ["const echoInfluencedChoiceReceipt = applyEchoInfluencedChoiceReceipt('offer_help')", "offerHelp", "accepted source-bounded help", "phrasebookOnly: true"]), "offerHelp creates a source-aware receipt when the bounded conversation exists")
    add_criterion(criteria, "source_preserves_attribution_and_refusal", has_terms(app_text, ["sourceAttributionPreserved", "directAvatarCommand: false", "recoverable: true", "refuses to rewrite", "echo.sourceResident"]), "choice receipt preserves source attribution and records bounded refusal")
    add_criterion(criteria, "visible_echo_choice_panel_wired", has_terms(index_text, ["echoInfluencedChoiceReceiptOut", "Echo choice"]), "index.html exposes Echo choice dashboard panel")
    add_criterion(criteria, "public_state_boundary_includes_echo_choice", has_terms(app_text, ["echoInfluencedChoiceReceipt", "publicState", "runStateBoundaryAudit"]), "state-boundary audit public world includes echo choice receipt")
    add_criterion(criteria, "browser_smoke_artifact_exists", bool(browser), str(BROWSER_SMOKE.relative_to(ROOT)) if BROWSER_SMOKE.exists() else "missing browser smoke artifact")
    add_criterion(criteria, "browser_smoke_used_maintained_shell", "ssrm_3d_browser_world_v61_vertical_slice_app_shell" in browser.get("shellUrl", ""), browser.get("shellUrl", "missing shellUrl"))
    add_criterion(criteria, "before_choice_empty_after_conversation", "No echo-influenced choice yet" in before.get("echoInfluencedChoiceText", ""), before.get("echoInfluencedChoiceText", "missing choice text"))
    add_criterion(criteria, "choice_created_by_fay_offer_help", choice.get("resident") == "Fay" and choice.get("action") == "offer_help" and choice.get("sourceEchoId") == "milo-offscreen-water-jars", f"choice={choice}")
    add_criterion(criteria, "visible_choice_accepts_help_and_refuses_rewrite", "Choice: accept_source_bounded_help" in choice_text and "Refusal:" in choice_text and "refuses to rewrite" in choice_text and "Source echo: milo-offscreen-water-jars" in choice_text, choice_text or "missing choice text")
    add_criterion(criteria, "visible_choice_preserves_source_and_not_command", "Source preserved: yes" in choice_text and "Direct avatar command: no" in choice_text and "Recoverable: yes" in choice_text, choice_text or "missing source/refusal text")
    add_criterion(criteria, "choice_boundary_flags_preserved", choice.get("noLLM") is True and choice.get("autonomousLanguage") is False and choice.get("phrasebookOnly") is True and choice.get("recoverable") is True, f"choice={choice}")
    add_criterion(criteria, "resident_history_records_choice_refusal", "echo-influenced choice/refusal" in history_text and "accepted source-bounded help" in history_text and "refused history rewrite" in history_text, history_text or "missing resident history")
    add_criterion(criteria, "relationship_memory_still_carries_original_echo", "Fay heard Milo" in relationship_text and "Fay changed Milo" in relationship_text and "milo-offscreen-water-jars" in relationship_text, relationship_text or "missing relationship memory")
    add_criterion(criteria, "replay_logs_offer_help_payload", browser.get("replayHasEchoChoice") is True and "offerHelp" in trace_text and "echoInfluencedChoiceReceipt" in trace_text and "phrasebookOnly" in trace_text, f"replayHasEchoChoice={browser.get('replayHasEchoChoice')} trace={trace_text}")
    add_criterion(criteria, "echo_choice_survives_reload", reload_choice.get("resident") == "Fay" and reload_choice.get("sourceEchoId") == "milo-offscreen-water-jars" and "Recoverable: yes" in reload_text, f"reload_choice={reload_choice} text={reload_text}")
    add_criterion(criteria, "browser_console_clean", len(console_errors) == 0, f"console error count={len(console_errors)}")
    add_criterion(criteria, "experiment_index_includes_report_361", "experiments.ssrm_3d_browser_world_v121_primary_shell_echo_influenced_choice_refusal" in runner_text, "scripts/run_experiments.py includes Report 361 module")
    add_criterion(criteria, "claim_boundary_preserved", all(term in BOUNDARY for term in ["phrasebook-only", "no LLM call", "subjective consciousness", "moral patienthood", "finished gameplay"]), BOUNDARY)

    category_scores = {
        "review_gate_score": criteria[0]["score"],
        "source_behavior_score": min(criteria[1]["score"], criteria[2]["score"], criteria[3]["score"], criteria[5]["score"]),
        "visible_binding_score": criteria[4]["score"],
        "browser_interaction_score": min(criteria[6]["score"], criteria[7]["score"]),
        "empty_state_score": criteria[8]["score"],
        "choice_generation_score": min(criteria[9]["score"], criteria[10]["score"], criteria[11]["score"], criteria[12]["score"]),
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
    state = {"report": REPORT, "shell_app": str(SHELL_APP.relative_to(ROOT)), "browser_smoke": browser, "report360_gate": report360}

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
