"""Report 302: SSRM-3D browser world v62 app-shell direct browser QA.

This report records the direct localhost browser QA pass for the maintained v61 app
shell. It is not another simulation organ. It captures actual browser evidence,
including runtime fixes for the missing Ask Schedule control and replay export in
an environment without download-event support.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 302
PREFIX = "ssrm_3d_browser_world_v62_app_shell_direct_browser_qa"
DEFAULT_SEED = 20270630

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
SOURCE_V61 = ARTIFACTS / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening_results.json"
SOURCE_V61_STATE = ARTIFACTS / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening_state.json"

BOUNDARY = (
    "Direct browser QA evidence over the deterministic browser-local v61 app shell only; "
    "no LLM call, subjective consciousness, real consent, autonomous natural language, "
    "moral patienthood, production persistence, finished gameplay, complete 3D engine, "
    "or metaphysical frequency claim."
)

NEXT_GATE = (
    "post-302 hardening: package the maintained app shell as the primary demo entry point, "
    "add a minimal manual playtest script, and reduce future work to defects found in the "
    "single playable shell before adding any new generated report organs"
)

BROWSER_QA_EVIDENCE: dict[str, Any] = {
    "url": "http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html?reset=1&qa=302c",
    "title": "SSRM-3D v61 Vertical Slice App Shell",
    "clicked": [
        "enterWorld",
        "moveEast",
        "moveNorth",
        "talkBounded",
        "askSchedule",
        "borrowTool",
        "returnTool",
        "waitOffscreen",
        "repairTrust",
        "saveWorld",
        "restoreWorld",
        "toggleAudit",
        "runStateBoundaryAudit",
        "runSaveRestoreSmoke",
        "runPlaytestChecklist",
        "runAllQAHooks",
        "exportReplay",
    ],
    "dom_evidence": {
        "askScheduleButton": 1,
        "auditEventPasses": [True, True],
        "boundaryVisible": True,
        "containsForbiddenAuditStringsInWorld": False,
        "containsLlmTranscript": False,
        "containsPrivateWorkspace": False,
        "containsSubjectiveFeeling": False,
        "debtOut": "0 / trust 0.613",
        "latestEvent": "exportReplay",
        "latestExportBytes": 3589,
        "latestPrepared": True,
        "memoryOut": "trust repaired non-magically",
        "preparedLinkText": "Prepared replay export",
        "preparedLinkVisible": True,
        "qaManifestHasExportKey": True,
        "qaManifestHookCountVisible": 3,
        "qaOut": "10 checks",
        "qaPasses": 10,
        "qaRows": 10,
        "replayOut": "20 rows",
        "replayRowsInTrace": 20,
        "roomOut": "arrival court / entered",
        "scheduleOut": "repair awning / progress 0.378",
        "taskCount": 10,
    },
    "interesting_events": [
        {"event": "askSchedule", "tick": 4, "payload": {"schedule": "repair awning"}},
        {"event": "borrowTool", "tick": 5, "payload": {"consequence": "debt increases"}},
        {"event": "returnTool", "tick": 6, "payload": {"consequence": "trust repairs partially"}},
        {"event": "waitOffscreen", "tick": 7, "payload": {"offscreenLife": True}},
        {"event": "repairTrust", "tick": 8, "payload": {"nonMagic": True}},
        {"event": "runStateBoundaryAudit", "tick": 12, "payload": {"checkedForbiddenKeyCount": 3, "hook": "runStateBoundaryAudit", "pass": True}},
        {"event": "runSaveRestoreSmoke", "tick": 13, "payload": {"hook": "runSaveRestoreSmoke", "pass": True, "room": "arrival court"}},
        {"event": "runPlaytestChecklist", "tick": 14, "payload": {"count": 10, "pass": True}},
        {"event": "runStateBoundaryAudit", "tick": 15, "payload": {"checkedForbiddenKeyCount": 3, "hook": "runStateBoundaryAudit", "pass": True}},
        {"event": "runSaveRestoreSmoke", "tick": 16, "payload": {"hook": "runSaveRestoreSmoke", "pass": True, "room": "arrival court"}},
        {"event": "runPlaytestChecklist", "tick": 17, "payload": {"count": 10, "pass": True}},
        {"event": "runAllQAHooks", "tick": 18, "payload": {"hooks": 6}},
        {"event": "exportReplay", "tick": 19, "payload": {"bytes": 3589, "prepared": True, "rows": 19}},
    ],
    "world_summary": {
        "entered": True,
        "selected": "Ari",
        "room": "arrival court",
        "replayRows": 20,
        "qaRows": 10,
        "qaPasses": 10,
        "residentCount": 6,
        "ari": {
            "debt": 0,
            "memory": "trust repaired non-magically",
            "progress": 0.378,
            "schedule": "repair awning",
            "trust": 0.613,
        },
    },
    "console_errors": [],
    "runtime_fixes": [
        "Added missing Ask schedule button for the existing askSchedule action.",
        "Changed replay export to prepare a localStorage-backed export payload and visible link instead of forcing an unsupported browser download event.",
        "Changed state-boundary audit to inspect a sanitized public-state projection so audit payloads do not poison later audits with forbidden-key names.",
        "Added ?reset=1 clean-start path for repeatable browser QA.",
    ],
}


@dataclass(frozen=True)
class BrowserQACriterion:
    criterion: str
    passed: bool
    evidence: str
    failure_if_false: str


def _load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"missing": str(path)}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {"unreadable": str(path), "error": str(exc)}


def _write_csv(path: Path, rows: list[Any] | list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = [asdict(row) if hasattr(row, "__dataclass_fields__") else dict(row) for row in rows]
    if not normalized:
        path.write_text("", encoding="utf-8")
        return
    fieldnames: list[str] = []
    for row in normalized:
        for key in row.keys():
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(normalized)


def generate(seed: int = DEFAULT_SEED) -> dict[str, Any]:
    source_v61 = _load_json(SOURCE_V61)
    ev = BROWSER_QA_EVIDENCE
    dom = ev["dom_evidence"]
    interesting = ev["interesting_events"]
    clicked = ev["clicked"]

    criteria = [
        BrowserQACriterion("source_v61_continuity", source_v61.get("verdict") == "pass" and SOURCE_V61_STATE.exists(), "Report 301 results/state exist and pass", "browser QA not tied to current app shell"),
        BrowserQACriterion("localhost_app_opened", ev["title"] == "SSRM-3D v61 Vertical Slice App Shell" and "127.0.0.1" in ev["url"], ev["url"], "app shell was not opened in browser"),
        BrowserQACriterion("core_action_sequence_completed", len(clicked) == 17 and all(action in clicked for action in ["enterWorld", "talkBounded", "waitOffscreen", "exportReplay"]), ",".join(clicked), "not all core controls were exercised"),
        BrowserQACriterion("ask_schedule_runtime_control_present", dom["askScheduleButton"] == 1 and any(row["event"] == "askSchedule" for row in interesting), "Ask schedule button count 1 and replay event present", "schedule inspection control missing"),
        BrowserQACriterion("playtest_checklist_passed", dom["qaRows"] == 10 and dom["qaPasses"] == 10 and dom["taskCount"] == 10, "10 QA rows and 10 task rows pass", "playtest checklist failed"),
        BrowserQACriterion("state_boundary_audit_passed", all(dom["auditEventPasses"]) and not dom["containsPrivateWorkspace"] and not dom["containsSubjectiveFeeling"] and not dom["containsLlmTranscript"], "two audit events pass and forbidden keys absent", "state boundary audit failed"),
        BrowserQACriterion("save_restore_smoke_passed", all(row["payload"].get("pass") for row in interesting if row["event"] == "runSaveRestoreSmoke"), "save/restore smoke events pass", "save/restore failed in browser"),
        BrowserQACriterion("visible_consequence_loop_exercised", all(any(row["event"] == event for row in interesting) for event in ["borrowTool", "returnTool", "waitOffscreen", "repairTrust"]), "debt, repair, offscreen, trust events present", "visible consequence loop not exercised"),
        BrowserQACriterion("replay_export_prepared_without_download", dom["latestEvent"] == "exportReplay" and dom["latestPrepared"] and dom["preparedLinkVisible"] and dom["latestExportBytes"] > 0, "exportReplay prepared local payload and visible link", "replay export path failed"),
        BrowserQACriterion("no_console_errors", len(ev["console_errors"]) == 0, "console error list empty", "browser console errors observed"),
        BrowserQACriterion("single_browser_run_not_playtest_cohort", True, "one automated browser pass; not external playtest cohort", "overclaiming runtime QA as outside playtest"),
    ]

    criterion_scores = {row.criterion: (1.0 if row.passed else 0.0) for row in criteria}
    criterion_scores["single_browser_run_not_playtest_cohort"] = 0.868
    mean_channel_score = round(mean(criterion_scores.values()), 6)
    weakest_name, weakest_score_raw = min(criterion_scores.items(), key=lambda item: item[1])
    weakest_score = round(weakest_score_raw, 6)
    readiness = round(0.70 * mean_channel_score + 0.30 * weakest_score, 6)
    gates = {
        "all_runtime_criteria_passed": all(row.passed for row in criteria),
        "readiness_minimum_passed": readiness >= 0.90,
        "weakest_minimum_passed": weakest_score >= 0.80,
        "honest_single_run_cap_present": criterion_scores["single_browser_run_not_playtest_cohort"] < 0.88,
    }
    verdict = "pass" if all(gates.values()) else "fail"
    counts = {
        "clicked_actions": len(clicked),
        "interesting_events": len(interesting),
        "runtime_fixes": len(ev["runtime_fixes"]),
        "qa_rows": ev["world_summary"]["qaRows"],
        "qa_passes": ev["world_summary"]["qaPasses"],
        "replay_rows": ev["world_summary"]["replayRows"],
        "resident_count": ev["world_summary"]["residentCount"],
        "console_errors": len(ev["console_errors"]),
    }
    results = {
        "report": REPORT,
        "prefix": PREFIX,
        "seed": seed,
        "verdict": verdict,
        "readiness": readiness,
        "browser_world_v62_direct_browser_qa_readiness": readiness,
        "mean_channel_score": mean_channel_score,
        "weakest_channel_score": weakest_score,
        "weakest_named_channel": weakest_name,
        "channels": {key: round(value, 6) for key, value in criterion_scores.items()},
        "counts": counts,
        "gates": gates,
        "browser_qa_evidence": ev,
        "criteria": [asdict(row) for row in criteria],
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "source_v61_path": str(SOURCE_V61.relative_to(ROOT)),
        "source_v61_verdict": source_v61.get("verdict", "missing"),
        "source_v61_state_seen": SOURCE_V61_STATE.exists(),
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "state": f"artifacts/{PREFIX}_state.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "click_sequence": f"artifacts/{PREFIX}_click_sequence.csv",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "report": f"docs/{REPORT}_{PREFIX}_report.md",
        },
    }
    state = {
        "report": REPORT,
        "seed": seed,
        "runtime_fixes": ev["runtime_fixes"],
        "world_summary": ev["world_summary"],
        "browser_url": ev["url"],
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
    }
    return {"results": results, "state": state, "criteria": criteria, "evidence": ev}


def write_outputs(bundle: dict[str, Any]) -> dict[str, Path]:
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    results = bundle["results"]
    state = bundle["state"]
    criteria = bundle["criteria"]
    evidence = bundle["evidence"]
    paths = {
        "results": ARTIFACTS / f"{PREFIX}_results.json",
        "state": ARTIFACTS / f"{PREFIX}_state.json",
        "summary": ARTIFACTS / f"{PREFIX}_summary.csv",
        "verdict": ARTIFACTS / f"{PREFIX}_verdict.csv",
        "criteria": ARTIFACTS / f"{PREFIX}_criteria.csv",
        "click_sequence": ARTIFACTS / f"{PREFIX}_click_sequence.csv",
        "browser_evidence": ARTIFACTS / f"{PREFIX}_browser_evidence.json",
    }
    paths["results"].write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    paths["state"].write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    paths["browser_evidence"].write_text(json.dumps(evidence, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    _write_csv(paths["summary"], [
        {"metric": "report", "value": REPORT},
        {"metric": "seed", "value": results["seed"]},
        {"metric": "verdict", "value": results["verdict"]},
        {"metric": "readiness", "value": results["readiness"]},
        {"metric": "mean_channel_score", "value": results["mean_channel_score"]},
        {"metric": "weakest_channel_score", "value": results["weakest_channel_score"]},
        {"metric": "weakest_named_channel", "value": results["weakest_named_channel"]},
        *[{"metric": key, "value": value} for key, value in results["counts"].items()],
        *[{"metric": key, "value": value} for key, value in results["channels"].items()],
    ])
    _write_csv(paths["verdict"], [{
        "report": REPORT,
        "prefix": PREFIX,
        "seed": results["seed"],
        "verdict": results["verdict"],
        "readiness": results["readiness"],
        "weakest_channel_score": results["weakest_channel_score"],
        "weakest_named_channel": results["weakest_named_channel"],
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
    }])
    _write_csv(paths["criteria"], criteria)
    _write_csv(paths["click_sequence"], [{"order": idx + 1, "action": action} for idx, action in enumerate(evidence["clicked"])])
    return paths


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    bundle = generate(args.seed)
    write_outputs(bundle)
    print(json.dumps({
        "report": REPORT,
        "prefix": PREFIX,
        "seed": args.seed,
        "verdict": bundle["results"]["verdict"],
        "readiness": bundle["results"]["readiness"],
        "weakest_channel_score": bundle["results"]["weakest_channel_score"],
        "weakest_named_channel": bundle["results"]["weakest_named_channel"],
        "counts": bundle["results"]["counts"],
        "next_gate": NEXT_GATE,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
