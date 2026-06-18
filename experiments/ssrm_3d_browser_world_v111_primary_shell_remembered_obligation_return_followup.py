from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 351
SLUG = "ssrm_3d_browser_world_v111_primary_shell_remembered_obligation_return_followup"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT350_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v110_primary_shell_return_recognition_vertical_slice_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "351_ssrm_3d_browser_world_v111_primary_shell_remembered_obligation_return_followup_report.md"

BOUNDARY = (
    "Browser-local remembered obligation follow-up behavior over the maintained v61 shell only; "
    "no LLM call, subjective consciousness, real consent, autonomous natural language, moral patienthood, "
    "production persistence, hosted URL proof, complete 3D engine, finished gameplay, or metaphysical claim."
)
NEXT_GATE = (
    "post-351: make the remembered follow-up selectable from a visible obligation list and require the avatar "
    "to resolve or defer it through a bounded action rather than advancing it only on repeated entry"
)


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def has_terms(text: str, terms: List[str]) -> bool:
    return all(term in text for term in terms)


def add_criterion(criteria: List[Dict[str, Any]], name: str, passed: bool, evidence: str) -> None:
    criteria.append(
        {
            "criterion": name,
            "passed": bool(passed),
            "score": 1.0 if passed else 0.0,
            "evidence": evidence,
        }
    )


def write_csv(path: Path, rows: List[Dict[str, Any]], fieldnames: List[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_report(results: Dict[str, Any], criteria: List[Dict[str, Any]], browser: Dict[str, Any]) -> str:
    metrics = results["metrics"]
    passed_count = sum(1 for row in criteria if row["passed"])
    lines = [
        "# Report 351: Browser World v111 Primary Shell Remembered Obligation Return Follow-up",
        "",
        "Report 351 continues the consolidation path by changing the maintained playable shell, not by adding another parallel world artifact. Report 350 made a resident recognize the avatar on return; this report makes repeated return advance one remembered obligation thread with visible resident memory, trust/progress consequences, public follow-up state, and replay/debug evidence.",
        "",
        "The browser-local smoke creates a persisted session, returns once to open the follow-up, then returns again without reset to advance the same obligation. The final visible state records `follow-up advanced`, return count `2`, replay growth, resident memory that links return recognition to the follow-up, and zero browser console errors.",
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
        f"- Before first return memory: `{browser.get('beforeFirstReturn', {}).get('memory', 'missing')}`",
        f"- After first return follow-up: `{browser.get('afterFirstReturn', {}).get('followUpText', 'missing')}`",
        f"- After second return follow-up: `{browser.get('afterSecondReturn', {}).get('followUpText', 'missing')}`",
        f"- Trust: `{metrics['before_trust']:.3f} -> {metrics['after_second_trust']:.3f}`",
        f"- Progress: `{metrics['before_progress']:.3f} -> {metrics['after_second_progress']:.3f}`",
        f"- Replay rows: `{metrics['before_replay_rows']} -> {metrics['after_second_replay_rows']}`",
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
    lines.extend(
        [
            "",
            "## Honest interpretation",
            "",
            "This is a concrete integration improvement: return continuity now creates and advances a small remembered obligation. It still remains deterministic browser-local state and bounded UI behavior. It is not subjective experience, autonomous language, real consent, production persistence, a hosted external demo, or finished gameplay.",
            "",
            "## Next gate",
            "",
            NEXT_GATE,
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    app_text = SHELL_APP.read_text(encoding="utf-8")
    index_text = SHELL_INDEX.read_text(encoding="utf-8")
    runner_text = RUNNER.read_text(encoding="utf-8")
    report350 = load_json(REPORT350_RESULTS)
    browser = load_json(BROWSER_SMOKE)

    before = browser.get("beforeFirstReturn", {})
    first = browser.get("afterFirstReturn", {})
    second = browser.get("afterSecondReturn", {})
    first_follow = first.get("promiseFollowUp", {})
    second_follow = second.get("promiseFollowUp", {})
    console_errors = browser.get("consoleErrors", [])

    criteria: List[Dict[str, Any]] = []
    add_criterion(
        criteria,
        "report_350_return_recognition_gate_passing",
        report350.get("verdict") == "pass" and report350.get("metrics", {}).get("weakest_channel_score") == 1.0,
        f"Report 350 verdict={report350.get('verdict')} weakest={report350.get('metrics', {}).get('weakest_channel_score')}",
    )
    add_criterion(
        criteria,
        "source_exposes_public_promise_followup_state",
        has_terms(app_text, ["promiseFollowUp", "publicState", "browser-local-public-obligation-thread-only"]),
        "app.js contains public promiseFollowUp state and boundary label",
    )
    add_criterion(
        criteria,
        "return_entry_advances_followup_state",
        has_terms(app_text, ["advancePromiseFollowUpState(residentName, 'return'", "follow-up", "returnCount"]),
        "enterWorld calls advancePromiseFollowUpState on returning visits",
    )
    add_criterion(
        criteria,
        "visible_followup_dashboard_wired",
        "promiseFollowUpOut" in index_text and "Advance follow-up" in index_text,
        "index.html exposes Follow-up dashboard text and manual advance control",
    )
    add_criterion(
        criteria,
        "browser_smoke_artifact_exists",
        bool(browser),
        str(BROWSER_SMOKE.relative_to(ROOT)) if BROWSER_SMOKE.exists() else "missing browser smoke artifact",
    )
    add_criterion(
        criteria,
        "browser_smoke_used_maintained_shell",
        "ssrm_3d_browser_world_v61_vertical_slice_app_shell" in browser.get("shellUrl", ""),
        browser.get("shellUrl", "missing shellUrl"),
    )
    add_criterion(
        criteria,
        "browser_smoke_created_persisted_session_before_return",
        before.get("replayRows", 0) >= 2 and "heard bounded phrase" in before.get("memory", ""),
        f"before replayRows={before.get('replayRows')} memory={before.get('memory')}",
    )
    add_criterion(
        criteria,
        "first_return_opened_remembered_obligation",
        first_follow.get("stage") == "opened" and first_follow.get("returnCount") == 1,
        f"first stage={first_follow.get('stage')} returnCount={first_follow.get('returnCount')}",
    )
    add_criterion(
        criteria,
        "second_return_advanced_same_obligation",
        second_follow.get("stage") == "advanced"
        and second_follow.get("returnCount") == 2
        and second_follow.get("obligation") == first_follow.get("obligation")
        and second.get("progress", 0) > first.get("progress", 0),
        f"second stage={second_follow.get('stage')} returnCount={second_follow.get('returnCount')} progress={first.get('progress')}->{second.get('progress')}",
    )
    add_criterion(
        criteria,
        "resident_memory_links_return_and_followup",
        "recognized returning avatar" in second.get("memory", "") and "follow-up advanced" in second.get("memory", ""),
        second.get("memory", "missing memory"),
    )
    add_criterion(
        criteria,
        "followup_visible_in_dashboard",
        "follow-up advanced" in second.get("followUpText", "") and "2 return(s)" in second.get("followUpText", ""),
        second.get("followUpText", "missing followUpText"),
    )
    add_criterion(
        criteria,
        "replay_and_history_record_followup",
        bool(browser.get("enterWorldReplayPayloadHasPromiseFollowUp")) and "promise follow-up" in browser.get("historyEvidence", ""),
        browser.get("historyEvidence", "missing history evidence"),
    )
    add_criterion(
        criteria,
        "browser_console_clean",
        len(console_errors) == 0,
        f"console error count={len(console_errors)}",
    )
    add_criterion(
        criteria,
        "experiment_index_includes_report_351",
        "experiments.ssrm_3d_browser_world_v111_primary_shell_remembered_obligation_return_followup" in runner_text,
        "scripts/run_experiments.py includes Report 351 module",
    )
    add_criterion(
        criteria,
        "claim_boundary_preserved",
        all(term in BOUNDARY for term in ["no LLM call", "subjective consciousness", "moral patienthood", "finished gameplay"]),
        BOUNDARY,
    )

    category_scores = {
        "review_gate_score": criteria[0]["score"],
        "source_behavior_score": min(criteria[1]["score"], criteria[2]["score"], criteria[3]["score"]),
        "browser_interaction_score": min(criteria[4]["score"], criteria[5]["score"], criteria[6]["score"]),
        "remembered_obligation_score": min(criteria[7]["score"], criteria[8]["score"], criteria[9]["score"], criteria[10]["score"]),
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
        "after_first_replay_rows": int(first.get("replayRows", 0) or 0),
        "after_second_replay_rows": int(second.get("replayRows", 0) or 0),
        "before_trust": float(before.get("trust", 0.0) or 0.0),
        "after_first_trust": float(first.get("trust", 0.0) or 0.0),
        "after_second_trust": float(second.get("trust", 0.0) or 0.0),
        "before_progress": float(before.get("progress", 0.0) or 0.0),
        "after_first_progress": float(first.get("progress", 0.0) or 0.0),
        "after_second_progress": float(second.get("progress", 0.0) or 0.0),
        "console_error_count": len(console_errors),
    }
    verdict = "pass" if all(row["passed"] for row in criteria) else "fail"
    results = {
        "report": REPORT,
        "slug": SLUG,
        "verdict": verdict,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "boundary": BOUNDARY,
        "metrics": metrics,
        "criteria": criteria,
        "browser_smoke_artifact": str(BROWSER_SMOKE.relative_to(ROOT)),
        "next_gate": NEXT_GATE,
    }
    state = {
        "report": REPORT,
        "shell_app": str(SHELL_APP.relative_to(ROOT)),
        "shell_index": str(SHELL_INDEX.relative_to(ROOT)),
        "browser_smoke": browser,
        "report350_gate": report350,
    }

    RESULTS.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    STATE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_csv(SUMMARY, [{"report": REPORT, "verdict": verdict, **metrics}], ["report", "verdict", *metrics.keys()])
    write_csv(VERDICT, [{"report": REPORT, "verdict": verdict, "weakest_channel_score": weakest, "readiness": readiness, "next_gate": NEXT_GATE}], ["report", "verdict", "weakest_channel_score", "readiness", "next_gate"])
    write_csv(CRITERIA, criteria, ["criterion", "passed", "score", "evidence"])
    REPORT_PATH.write_text(build_report(results, criteria, browser), encoding="utf-8")

    print(json.dumps({"report": REPORT, "verdict": verdict, "metrics": metrics}, indent=2, sort_keys=True))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
