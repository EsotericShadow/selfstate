from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 352
SLUG = "ssrm_3d_browser_world_v112_primary_shell_selectable_obligation_resolution"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT351_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v111_primary_shell_remembered_obligation_return_followup_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "352_ssrm_3d_browser_world_v112_primary_shell_selectable_obligation_resolution_report.md"

BOUNDARY = (
    "Browser-local selectable obligation resolution behavior over the maintained v61 shell only; "
    "no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, "
    "production persistence, hosted URL proof, complete 3D engine, finished gameplay, or metaphysical claim."
)
NEXT_GATE = (
    "post-352: connect selectable obligations to the resident schedule/debt dashboard so resolving one obligation "
    "also changes the visible schedule queue and debt ledger rather than only the obligation row"
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
        "# Report 352: Browser World v112 Primary Shell Selectable Obligation Resolution",
        "",
        "Report 352 keeps consolidation pressure on the maintained v61 playable shell. Report 351 created a remembered follow-up on return; this report exposes that follow-up as a selectable obligation row and requires bounded avatar action to defer or resolve it. Repeated entry can open and advance the obligation, but it does not resolve it by itself.",
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
        f"- Pending before action: `{browser.get('afterSecondReturn', {}).get('obligationListText', 'missing')}`",
        f"- After defer: `{browser.get('afterDefer', {}).get('obligationListText', 'missing')}`",
        f"- After resolve: `{browser.get('afterResolve', {}).get('obligationListText', 'missing')}`",
        f"- Trust: `{metrics['before_trust']:.3f} -> {metrics['after_resolve_trust']:.3f}`",
        f"- Progress: `{metrics['before_progress']:.3f} -> {metrics['after_resolve_progress']:.3f}`",
        f"- Replay rows: `{metrics['before_replay_rows']} -> {metrics['after_resolve_replay_rows']}`",
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
        "This is a small but concrete step from passive memory toward playable obligation handling. The avatar can now select a remembered resident obligation and change it through bounded UI action. It remains deterministic browser-local state, not autonomous language, subjective experience, production persistence, hosted multiplayer, or finished gameplay.",
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
    report351 = load_json(REPORT351_RESULTS)
    browser = load_json(BROWSER_SMOKE)

    before = browser.get("beforeFirstReturn", {})
    second = browser.get("afterSecondReturn", {})
    after_defer = browser.get("afterDefer", {})
    after_resolve = browser.get("afterResolve", {})
    pending_obligation = second.get("selectedObligation", {})
    deferred_obligation = after_defer.get("selectedObligation", {})
    resolved_obligation = after_resolve.get("selectedObligation", {})
    console_errors = browser.get("consoleErrors", [])

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_351_remembered_obligation_gate_passing", report351.get("verdict") == "pass" and report351.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 351 verdict={report351.get('verdict')} weakest={report351.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "source_exposes_public_obligation_ledger", has_terms(app_text, ["obligationLedger", "browser-local-selectable-obligation-list-only", "selectedObligationId", "publicState"]), "app.js exposes public obligationLedger and selection state")
    add_criterion(criteria, "visible_obligation_selector_and_actions_wired", has_terms(index_text, ["obligationSelect", "Resolve obligation", "Defer obligation", "obligationListOut"]), "index.html exposes selector, resolve, defer, and visible list")
    add_criterion(criteria, "bounded_resolve_defer_source_actions", has_terms(app_text, ["function resolveSelectedObligation()", "function deferSelectedObligation()", "boundedAction: true", "obligation resolved", "obligation deferred"]), "app.js has bounded resolve/defer actions with resident history events")
    add_criterion(criteria, "browser_smoke_artifact_exists", bool(browser), str(BROWSER_SMOKE.relative_to(ROOT)) if BROWSER_SMOKE.exists() else "missing browser smoke artifact")
    add_criterion(criteria, "browser_smoke_used_maintained_shell", "ssrm_3d_browser_world_v61_vertical_slice_app_shell" in browser.get("shellUrl", ""), browser.get("shellUrl", "missing shellUrl"))
    add_criterion(criteria, "browser_smoke_created_pending_obligation_before_action", pending_obligation.get("status") == "open" and pending_obligation.get("stage") == "advanced" and "ari-awning-followup" in second.get("obligationListText", ""), f"pending status={pending_obligation.get('status')} stage={pending_obligation.get('stage')} list={second.get('obligationListText')}")
    add_criterion(criteria, "obligation_did_not_auto_resolve_on_return", "resolved" not in second.get("obligationListText", "") and "deferred" not in second.get("obligationListText", ""), second.get("obligationListText", "missing list"))
    add_criterion(criteria, "defer_action_changes_selected_obligation", deferred_obligation.get("status") == "deferred" and "deferred by avatar" in after_defer.get("obligationListText", ""), f"deferred status={deferred_obligation.get('status')} list={after_defer.get('obligationListText')}")
    add_criterion(criteria, "resolve_action_changes_selected_obligation", resolved_obligation.get("status") == "resolved" and "resolved by avatar help" in after_resolve.get("obligationListText", ""), f"resolved status={resolved_obligation.get('status')} list={after_resolve.get('obligationListText')}")
    add_criterion(criteria, "resident_memory_records_resolution", "resolved obligation" in after_resolve.get("memory", "") and after_resolve.get("trust", 0) > after_defer.get("trust", 1), f"memory={after_resolve.get('memory')} trust={after_defer.get('trust')}->{after_resolve.get('trust')}")
    add_criterion(criteria, "replay_and_history_record_bounded_actions", browser.get("deferReplayLogged") is True and browser.get("resolveReplayLogged") is True and "obligation resolved" in browser.get("historyEvidence", ""), browser.get("historyEvidence", "missing history"))
    add_criterion(criteria, "browser_console_clean", len(console_errors) == 0, f"console error count={len(console_errors)}")
    add_criterion(criteria, "experiment_index_includes_report_352", "experiments.ssrm_3d_browser_world_v112_primary_shell_selectable_obligation_resolution" in runner_text, "scripts/run_experiments.py includes Report 352 module")
    add_criterion(criteria, "claim_boundary_preserved", all(term in BOUNDARY for term in ["no LLM call", "subjective consciousness", "moral patienthood", "finished gameplay"]), BOUNDARY)

    category_scores = {
        "review_gate_score": criteria[0]["score"],
        "source_behavior_score": min(criteria[1]["score"], criteria[2]["score"], criteria[3]["score"]),
        "browser_interaction_score": min(criteria[4]["score"], criteria[5]["score"]),
        "selectable_obligation_score": min(criteria[6]["score"], criteria[7]["score"]),
        "bounded_action_score": min(criteria[8]["score"], criteria[9]["score"], criteria[10]["score"]),
        "replay_debug_score": criteria[11]["score"],
        "runtime_hygiene_score": criteria[12]["score"],
        "runner_index_score": criteria[13]["score"],
        "claim_hygiene_score": criteria[14]["score"],
    }
    weakest = min(category_scores.values())
    readiness = sum(category_scores.values()) / len(category_scores)
    metrics = {
        **category_scores,
        "weakest_channel_score": weakest,
        "readiness": readiness,
        "criterion_count": len(criteria),
        "before_replay_rows": int(before.get("replayRows", 0) or 0),
        "after_second_replay_rows": int(second.get("replayRows", 0) or 0),
        "after_defer_replay_rows": int(after_defer.get("replayRows", 0) or 0),
        "after_resolve_replay_rows": int(after_resolve.get("replayRows", 0) or 0),
        "before_trust": float(before.get("trust", 0.0) or 0.0),
        "after_defer_trust": float(after_defer.get("trust", 0.0) or 0.0),
        "after_resolve_trust": float(after_resolve.get("trust", 0.0) or 0.0),
        "before_progress": float(before.get("progress", 0.0) or 0.0),
        "after_defer_progress": float(after_defer.get("progress", 0.0) or 0.0),
        "after_resolve_progress": float(after_resolve.get("progress", 0.0) or 0.0),
        "console_error_count": len(console_errors),
    }
    verdict = "pass" if all(row["passed"] for row in criteria) else "fail"
    results = {"report": REPORT, "slug": SLUG, "verdict": verdict, "generated_at": datetime.now(timezone.utc).isoformat(), "boundary": BOUNDARY, "metrics": metrics, "criteria": criteria, "browser_smoke_artifact": str(BROWSER_SMOKE.relative_to(ROOT)), "next_gate": NEXT_GATE}
    state = {"report": REPORT, "shell_app": str(SHELL_APP.relative_to(ROOT)), "shell_index": str(SHELL_INDEX.relative_to(ROOT)), "browser_smoke": browser, "report351_gate": report351}

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
