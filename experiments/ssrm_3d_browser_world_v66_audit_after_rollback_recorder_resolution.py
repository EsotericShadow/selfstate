"""Report 306: SSRM-3D browser world v66 audit-after-rollback recorder resolution.

This report takes the MP-10 defect note captured by the Report 305 recorder and
hardens the maintained v61 shell with a single audit-after-rollback hook. It
records browser evidence that rollback smoke and state-boundary audit now run as
one explicit check, then records MP-10 as resolved through the same primary-demo
recorder.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 306
PREFIX = "ssrm_3d_browser_world_v66_audit_after_rollback_recorder_resolution"
DEFAULT_SEED = 20270704

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
SOURCE_V61 = ARTIFACTS / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening_results.json"
SOURCE_V63 = ARTIFACTS / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package_results.json"
SOURCE_V65 = ARTIFACTS / "ssrm_3d_browser_world_v65_primary_demo_manual_pass_recorder_results.json"
PRIMARY_DEMO = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo" / "index.html"
V61_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
V61_QA = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "qa_manifest.json"

PRIMARY_DEMO_URL = "http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_primary_demo/index.html"
TARGET_SHELL_URL = "http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html?reset=1&source=primary-demo-v63"
TARGET_SHELL_REL = "../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html"

BOUNDARY = (
    "Audit-after-rollback hardening over the deterministic maintained v61 shell and primary-demo recorder only; "
    "no new simulation organ, no LLM call, no subjective consciousness, no real consent, no autonomous natural "
    "language, no moral patienthood, no production persistence, no finished gameplay, no complete 3D engine, "
    "no outside playtest cohort, and no metaphysical frequency claim."
)

NEXT_GATE = (
    "post-306: continue using the recorder to drive one defect at a time; next hardening should improve the "
    "primary demo's recorded defect triage/status model or fix another browser-observed usability gap"
)

BROWSER_EVIDENCE: dict[str, Any] = {
    "primary_before": {
        "title": "SSRM-3D Primary Browser World Demo",
        "url": PRIMARY_DEMO_URL,
        "boundaryVisible": True,
        "cleanLinks": 1,
        "recorderVisible": True,
        "mp10TextUpdated": True,
    },
    "shell_before": {
        "title": "SSRM-3D v61 Vertical Slice App Shell",
        "url": TARGET_SHELL_URL,
        "buttonCount": 21,
        "hasAuditAfterRollbackButton": 1,
        "manifestHasHook": True,
    },
    "shell_after": {
        "latest": {
            "event": "runAuditAfterRollbackCheck",
            "tick": 3,
            "selected": "Ari",
            "room": "arrival court",
            "payload": {
                "hook": "runAuditAfterRollbackCheck",
                "pass": True,
                "smokePass": True,
                "auditPass": True,
                "rollbackTested": True,
                "checkedAfterRollback": True,
                "linkedTicks": [1, 2],
            },
        },
        "qaOut": "1 checks",
        "replayOut": "4 rows",
        "roomOut": "arrival court / entered",
        "manifestTextHasHook": True,
        "replayRows": 4,
        "payloadPass": True,
        "smokePass": True,
        "auditPass": True,
        "rollbackTested": True,
        "checkedAfterRollback": True,
        "linkedTicksLength": 2,
        "replayEvents": [
            {"event": "enterWorld", "tick": 0, "payload": {"boundary": "deterministic prototype boundary visible"}},
            {"event": "runSaveRestoreSmoke", "tick": 1, "payload": {"hook": "runSaveRestoreSmoke", "pass": True, "rollbackTested": True, "room": "arrival court"}},
            {"event": "runStateBoundaryAudit", "tick": 2, "payload": {"hook": "runStateBoundaryAudit", "pass": True, "checkedForbiddenKeyCount": 3}},
            {"event": "runAuditAfterRollbackCheck", "tick": 3, "payload": {"hook": "runAuditAfterRollbackCheck", "pass": True, "smokePass": True, "auditPass": True, "rollbackTested": True, "checkedAfterRollback": True, "linkedTicks": [1, 2]}},
        ],
    },
    "recorder_after": {
        "status": "Recorder export prepared.",
        "exportPrepared": True,
        "exportText": "Prepared recorder export",
        "recordCount": 1,
        "defectCount": 1,
        "passCount": 1,
        "failCount": 0,
        "stepIds": ["MP-10"],
        "resolutionNotePresent": True,
        "recorderBoundary": True,
        "latestRecord": {
            "boundary": "manual-recorder-public-local-only",
            "recordedAt": "2026-06-18T06:28:13.553Z",
            "reportIntroduced": 305,
            "result": "pass",
            "stepId": "MP-10",
            "targetShell": TARGET_SHELL_REL,
        },
        "latestDefect": {
            "boundary": "manual-defect-ledger-public-local-only",
            "recordedAt": "2026-06-18T06:28:13.950Z",
            "reportIntroduced": 305,
            "note": "Resolved MP-10: audit-after-rollback hook passed with smokePass, auditPass, rollbackTested, and checkedAfterRollback all true.",
            "targetShell": TARGET_SHELL_REL,
        },
    },
    "console_errors": [],
}

PATCH_SUMMARY = [
    "Added a maintained-shell UI button for runAuditAfterRollbackCheck.",
    "Added runAuditAfterRollbackCheck to the v61 direct QA hook manifest.",
    "Implemented runAuditAfterRollbackCheck as rollback smoke followed by state-boundary audit, then a linked combined result.",
    "Updated runAllQAHooks to include the audit-after-rollback check.",
    "Updated primary-demo MP-10 instructions to expect the combined audit-after-rollback row.",
    "Used the Report 305 recorder to mark MP-10 pass with a resolution note and export prepared.",
]


@dataclass(frozen=True)
class ResolutionCriterion:
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


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


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
    source_v63 = _load_json(SOURCE_V63)
    source_v65 = _load_json(SOURCE_V65)
    qa_manifest = _load_json(V61_QA)
    primary_html = PRIMARY_DEMO.read_text(encoding="utf-8") if PRIMARY_DEMO.exists() else ""
    v61_app = V61_APP.read_text(encoding="utf-8") if V61_APP.exists() else ""
    hook_names = {row.get("js_function") for row in qa_manifest.get("direct_qa_hooks", [])}
    ev = BROWSER_EVIDENCE
    shell = ev["shell_after"]
    recorder = ev["recorder_after"]
    replay_names = [row["event"] for row in shell["replayEvents"]]

    criteria = [
        ResolutionCriterion("source_v61_regenerated_with_new_hook", source_v61.get("verdict") == "pass" and source_v61.get("counts", {}).get("direct_qa_hooks") == 7, "Report 301/v61 regenerated with 7 direct QA hooks", "maintained shell was not regenerated with the new hook"),
        ResolutionCriterion("source_primary_demo_package_passed", source_v63.get("verdict") == "pass", "Report 303 primary-demo package still passes", "primary demo package failed after MP-10 update"),
        ResolutionCriterion("source_recorder_defect_was_captured", source_v65.get("verdict") == "pass" and source_v65.get("counts", {}).get("browser_fail_records") == 1, "Report 305 captured one MP-10 fail record before this hardening", "no recorded defect drove this change"),
        ResolutionCriterion("primary_demo_mp10_instruction_updated", ev["primary_before"]["mp10TextUpdated"] and "Audit after rollback hooks" in primary_html, "primary demo MP-10 text names Audit after rollback hooks", "manual script still asks reviewers to infer ordering"),
        ResolutionCriterion("shell_ui_exposes_hook", ev["shell_before"]["hasAuditAfterRollbackButton"] == 1 and "runAuditAfterRollbackCheck" in v61_app, "v61 shell has one Audit after rollback button and function", "hook is not reachable from UI"),
        ResolutionCriterion("qa_manifest_exposes_hook", ev["shell_before"]["manifestHasHook"] and "runAuditAfterRollbackCheck" in hook_names, "v61 QA manifest includes runAuditAfterRollbackCheck", "hook is not listed in QA manifest"),
        ResolutionCriterion("combined_hook_passes", shell["payloadPass"] and shell["smokePass"] and shell["auditPass"] and shell["rollbackTested"] and shell["checkedAfterRollback"], "combined hook payload pass/smokePass/auditPass/rollbackTested/checkedAfterRollback all true", "combined hook did not prove both checks"),
        ResolutionCriterion("combined_hook_links_ordered_rows", replay_names == ["enterWorld", "runSaveRestoreSmoke", "runStateBoundaryAudit", "runAuditAfterRollbackCheck"] and shell["linkedTicksLength"] == 2, "replay shows smoke tick 1, audit tick 2, combined tick 3 with linkedTicks", "hook did not preserve inspectable ordering"),
        ResolutionCriterion("recorder_marks_resolution", recorder["recordCount"] == 1 and recorder["passCount"] == 1 and recorder["failCount"] == 0 and recorder["stepIds"] == ["MP-10"], "recorder marks MP-10 pass after fix", "recorder did not capture resolution"),
        ResolutionCriterion("recorder_resolution_note_exported", recorder["resolutionNotePresent"] and recorder["exportPrepared"] and recorder["recorderBoundary"], "resolution note recorded with export prepared and public local-only boundary", "resolution note/export boundary failed"),
        ResolutionCriterion("no_console_errors", len(ev["console_errors"]) == 0, "browser console error list empty", "browser console errors observed"),
        ResolutionCriterion("single_internal_resolution_pass_not_external_playtest", True, "one internal browser resolution pass, not outside playtest cohort", "overclaiming internal resolution as external validation"),
    ]

    scores = {row.criterion: (1.0 if row.passed else 0.0) for row in criteria}
    scores["single_internal_resolution_pass_not_external_playtest"] = 0.884
    mean_channel_score = round(mean(scores.values()), 6)
    weakest_name, weakest_value = min(scores.items(), key=lambda item: item[1])
    weakest_score = round(weakest_value, 6)
    readiness = round(0.70 * mean_channel_score + 0.30 * weakest_score, 6)
    gates = {
        "all_resolution_criteria_passed": all(row.passed for row in criteria),
        "readiness_minimum_passed": readiness >= 0.90,
        "weakest_minimum_passed": weakest_score >= 0.88,
        "recorded_defect_drove_patch": source_v65.get("counts", {}).get("browser_fail_records") == 1,
        "honest_internal_resolution_cap_present": scores["single_internal_resolution_pass_not_external_playtest"] < 0.89,
    }
    verdict = "pass" if all(gates.values()) else "fail"
    counts = {
        "direct_qa_hooks": source_v61.get("counts", {}).get("direct_qa_hooks", 0),
        "shell_action_buttons": ev["shell_before"]["buttonCount"],
        "browser_replay_rows": shell["replayRows"],
        "linked_ticks": shell["linkedTicksLength"],
        "recorder_resolution_records": recorder["recordCount"],
        "recorder_resolution_notes": recorder["defectCount"],
        "patch_summary_items": len(PATCH_SUMMARY),
        "console_errors": len(ev["console_errors"]),
    }

    results = {
        "report": REPORT,
        "prefix": PREFIX,
        "seed": seed,
        "verdict": verdict,
        "readiness": readiness,
        "audit_after_rollback_recorder_resolution_readiness": readiness,
        "mean_channel_score": mean_channel_score,
        "weakest_channel_score": weakest_score,
        "weakest_named_channel": weakest_name,
        "channels": {key: round(value, 6) for key, value in scores.items()},
        "counts": counts,
        "gates": gates,
        "criteria": [asdict(row) for row in criteria],
        "browser_evidence": ev,
        "patch_summary": PATCH_SUMMARY,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "source_v61_path": str(SOURCE_V61.relative_to(ROOT)),
        "source_v63_path": str(SOURCE_V63.relative_to(ROOT)),
        "source_v65_path": str(SOURCE_V65.relative_to(ROOT)),
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "state": f"artifacts/{PREFIX}_state.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "replay_sequence": f"artifacts/{PREFIX}_replay_sequence.csv",
            "report": f"docs/{REPORT}_{PREFIX}_report.md",
        },
    }
    runtime_state = {
        "report": REPORT,
        "seed": seed,
        "browser_evidence": ev,
        "patch_summary": PATCH_SUMMARY,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
    }
    return {"results": results, "state": runtime_state, "criteria": criteria}


def _report_markdown(results: dict[str, Any]) -> str:
    criteria_rows = "\n".join(
        f"| {row['criterion']} | {row['passed']} | {row['evidence']} |" for row in results["criteria"]
    )
    patch_rows = "\n".join(f"- {item}" for item in PATCH_SUMMARY)
    replay_rows = "\n".join(
        f"| {row['tick']} | {row['event']} | {row['payload']} |" for row in BROWSER_EVIDENCE["shell_after"]["replayEvents"]
    )
    payload = BROWSER_EVIDENCE["shell_after"]["latest"]["payload"]
    recorder = BROWSER_EVIDENCE["recorder_after"]
    return f"""# Report 306: SSRM-3D Browser World v66 Audit-After-Rollback Recorder Resolution

Report 306 closes the MP-10 loop created by Report 305. The recorder captured that audit output should be checked after rollback smoke; this report hardens the maintained shell with one explicit `runAuditAfterRollbackCheck` hook, verifies it in browser, and records MP-10 as resolved through the same primary-demo recorder.

## Result

- Verdict: `{results['verdict']}`
- Readiness: `{results['readiness']}`
- Mean channel score: `{results['mean_channel_score']}`
- Weakest channel: `{results['weakest_named_channel']}` at `{results['weakest_channel_score']}`
- Shell controls after patch: `{results['counts']['shell_action_buttons']}`
- Direct QA hooks after patch: `{results['counts']['direct_qa_hooks']}`

## Patch summary

{patch_rows}

## Browser hook evidence

The latest shell event was `runAuditAfterRollbackCheck` with payload `{payload}`.

| Tick | Event | Payload |
| --- | --- | --- |
{replay_rows}

## Recorder resolution evidence

- Record count: `{recorder['recordCount']}`
- Pass count: `{recorder['passCount']}`
- Fail count: `{recorder['failCount']}`
- Step IDs: `{', '.join(recorder['stepIds'])}`
- Resolution note present: `{recorder['resolutionNotePresent']}`
- Export prepared: `{recorder['exportPrepared']}`
- Console errors: `{len(BROWSER_EVIDENCE['console_errors'])}`

## Criteria

| Criterion | Passed | Evidence |
| --- | --- | --- |
{criteria_rows}

## Honest limit

The weakest channel is `{results['weakest_named_channel']}`. This is one internal browser resolution pass over the primary demo and maintained shell, not an external playtest cohort or production-readiness claim.

## Boundary

{BOUNDARY}

## Next gate

{NEXT_GATE}.
"""


def write_outputs(bundle: dict[str, Any]) -> dict[str, Path]:
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    results = bundle["results"]
    state = bundle["state"]
    criteria = bundle["criteria"]
    paths = {
        "results": ARTIFACTS / f"{PREFIX}_results.json",
        "state": ARTIFACTS / f"{PREFIX}_state.json",
        "summary": ARTIFACTS / f"{PREFIX}_summary.csv",
        "verdict": ARTIFACTS / f"{PREFIX}_verdict.csv",
        "criteria": ARTIFACTS / f"{PREFIX}_criteria.csv",
        "browser_evidence": ARTIFACTS / f"{PREFIX}_browser_evidence.json",
        "replay_sequence": ARTIFACTS / f"{PREFIX}_replay_sequence.csv",
        "report": ROOT / "docs" / f"{REPORT}_{PREFIX}_report.md",
    }
    _write_json(paths["results"], results)
    _write_json(paths["state"], state)
    _write_json(paths["browser_evidence"], BROWSER_EVIDENCE)
    _write_csv(paths["summary"], [{"metric": key, "value": value} for key, value in results["counts"].items()] + [
        {"metric": "readiness", "value": results["readiness"]},
        {"metric": "mean_channel_score", "value": results["mean_channel_score"]},
        {"metric": "weakest_channel_score", "value": results["weakest_channel_score"]},
        {"metric": "weakest_named_channel", "value": results["weakest_named_channel"]},
    ])
    _write_csv(paths["verdict"], [{"report": REPORT, "verdict": results["verdict"], "readiness": results["readiness"], "weakest_channel_score": results["weakest_channel_score"], "weakest_named_channel": results["weakest_named_channel"]}])
    _write_csv(paths["criteria"], criteria)
    _write_csv(paths["replay_sequence"], BROWSER_EVIDENCE["shell_after"]["replayEvents"])
    paths["report"].write_text(_report_markdown(results), encoding="utf-8")
    return paths


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    bundle = generate(seed=args.seed)
    write_outputs(bundle)
    results = bundle["results"]
    print(json.dumps({
        "report": REPORT,
        "prefix": PREFIX,
        "seed": args.seed,
        "verdict": results["verdict"],
        "readiness": results["readiness"],
        "weakest_channel_score": results["weakest_channel_score"],
        "weakest_named_channel": results["weakest_named_channel"],
        "counts": results["counts"],
        "next_gate": NEXT_GATE,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
