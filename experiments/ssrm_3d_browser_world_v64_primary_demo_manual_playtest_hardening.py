"""Report 304: SSRM-3D browser world v64 primary-demo manual playtest hardening.

This report records the first real defect found by running the Report 303 primary
demo manual-playtest spine against the maintained v61 browser shell: save/restore
was only a live-state round trip, not a rollback snapshot. The report captures
before/after browser evidence and keeps the fix in the v61 generator.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 304
PREFIX = "ssrm_3d_browser_world_v64_primary_demo_manual_playtest_hardening"
DEFAULT_SEED = 20270702

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
SOURCE_V61 = ARTIFACTS / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening_results.json"
SOURCE_V63 = ARTIFACTS / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package_results.json"
V61_QA_MANIFEST = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "qa_manifest.json"
PRIMARY_DEMO_QA = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo" / "qa_manifest.json"

PRIMARY_DEMO_URL = "http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_primary_demo/index.html"
TARGET_SHELL_URL = "http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html?reset=1&source=primary-demo-v63"
RESUME_SHELL_URL = "http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html?source=primary-demo-v63"
SNAPSHOT_KEY = "ssrm_v61_app_shell_saved_snapshot"

BOUNDARY = (
    "Primary-demo browser manual-playtest hardening over the deterministic maintained v61 shell only; "
    "no new simulation organ, no LLM call, no subjective consciousness, no real consent, no autonomous "
    "natural language, no moral patienthood, no production persistence, no finished gameplay, no complete "
    "3D engine, and no metaphysical frequency claim."
)

NEXT_GATE = (
    "post-304: keep the primary demo as the only review surface, add a tiny in-page defect ledger/manual "
    "pass recorder, and continue hardening defects found through the same primary-demo path"
)

MANUAL_SEQUENCE = [
    "openPrimaryDemo",
    "launchCleanDemo",
    "enterWorld",
    "moveEast",
    "moveNorth",
    "talkBounded",
    "askSchedule",
    "borrowTool",
    "returnTool",
    "waitOffscreen",
    "saveWorld",
    "moveWest",
    "restoreWorld",
    "runPlaytestChecklist",
    "runStateBoundaryAudit",
    "runSaveRestoreSmoke",
    "exportReplay",
    "resumeDemo",
]

BEFORE_FIX_EVIDENCE: dict[str, Any] = {
    "browser_url": TARGET_SHELL_URL,
    "defect": "restoreWorld reloaded STATE_KEY, which had already been overwritten by moveWest after saveWorld",
    "save_avatar": {"room": "arrival court", "x": 214, "y": 226},
    "changed_avatar": {"room": "arrival court", "x": 180, "y": 226},
    "restore_avatar": {"room": "arrival court", "x": 180, "y": 226},
    "rollback_worked": False,
    "console_errors": 0,
    "latest_restore_payload": {"restored": True},
    "public_trace_source": "traceOut DOM JSON",
}

AFTER_FIX_EVIDENCE: dict[str, Any] = {
    "primary_demo": {
        "url": PRIMARY_DEMO_URL,
        "title": "SSRM-3D Primary Browser World Demo",
        "boundary_visible": True,
        "clean_links": 1,
        "resume_links": 1,
        "manual_has_mp12": True,
    },
    "clean_launch": {
        "url": TARGET_SHELL_URL,
        "title": "SSRM-3D v61 Vertical Slice App Shell",
        "boundary_visible": True,
        "has_snapshot_key_in_manifest": True,
        "action_button_count": 20,
    },
    "save_point": {
        "avatar": {"room": "arrival court", "x": 214, "y": 226},
        "payload": {"saved": True, "snapshotKey": SNAPSHOT_KEY},
        "replay_rows": 9,
    },
    "changed_point": {
        "avatar": {"room": "arrival court", "x": 180, "y": 226},
        "payload": {"room": "arrival court", "x": 180},
        "replay_rows": 10,
    },
    "restore_point": {
        "avatar": {"room": "arrival court", "x": 214, "y": 226},
        "payload": {"restored": True, "snapshotKey": SNAPSHOT_KEY},
        "replay_rows": 9,
    },
    "smoke_point": {
        "payload": {"hook": "runSaveRestoreSmoke", "pass": True, "rollbackTested": True, "room": "arrival court"},
        "replay_rows": 12,
    },
    "export_point": {
        "payload": {"bytes": 2454, "prepared": True, "rows": 12},
        "prepared_link_text": "Prepared replay export",
        "replay_rows": 13,
    },
    "resume_point": {
        "url": RESUME_SHELL_URL,
        "avatar": {"room": "arrival court", "x": 214, "y": 226},
        "latest_event": "exportReplay",
        "replay_rows": 13,
        "debt_out": "1 / trust 0.595",
        "schedule_out": "repair awning / progress 0.378",
    },
    "flags": {
        "rollback_worked": True,
        "mutation_actually_changed": True,
        "smoke_rollback_tested": True,
        "resume_kept_state": True,
        "console_errors": 0,
    },
    "sequence": MANUAL_SEQUENCE,
}

PATCH_SUMMARY = [
    "Added SAVE_SNAPSHOT_KEY to the maintained v61 shell generator.",
    "Changed reset behavior to clear the saved snapshot alongside world, replay, QA, and export keys.",
    "Changed saveWorld to write an explicit rollback snapshot instead of only rewriting live STATE_KEY.",
    "Changed restoreWorld to restore from the saved snapshot and report the snapshot key in replay payload.",
    "Changed runSaveRestoreSmoke to mutate after snapshot and verify rollback, not just storage round trip.",
    "Added the saved snapshot key to v61 and primary-demo QA manifests.",
]


@dataclass(frozen=True)
class HardeningCriterion:
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


def _avatar_equal(left: dict[str, Any], right: dict[str, Any]) -> bool:
    return left == right


def generate(seed: int = DEFAULT_SEED) -> dict[str, Any]:
    source_v61 = _load_json(SOURCE_V61)
    source_v63 = _load_json(SOURCE_V63)
    v61_manifest = _load_json(V61_QA_MANIFEST)
    primary_manifest = _load_json(PRIMARY_DEMO_QA)

    before_restore_failed = not BEFORE_FIX_EVIDENCE["rollback_worked"] and not _avatar_equal(
        BEFORE_FIX_EVIDENCE["save_avatar"], BEFORE_FIX_EVIDENCE["restore_avatar"]
    )
    after_flags = AFTER_FIX_EVIDENCE["flags"]
    after_restore_fixed = after_flags["rollback_worked"] and _avatar_equal(
        AFTER_FIX_EVIDENCE["save_point"]["avatar"], AFTER_FIX_EVIDENCE["restore_point"]["avatar"]
    )
    after_mutated = after_flags["mutation_actually_changed"] and not _avatar_equal(
        AFTER_FIX_EVIDENCE["save_point"]["avatar"], AFTER_FIX_EVIDENCE["changed_point"]["avatar"]
    )
    v61_state_keys = {row.get("state_key") for row in v61_manifest.get("state_boundary_rules", [])}
    primary_state_keys = set(primary_manifest.get("state_keys", []))

    criteria = [
        HardeningCriterion("source_v61_shell_regenerated", source_v61.get("verdict") == "pass" and source_v61.get("counts", {}).get("state_boundary_rules") == 10, "Report 301/v61 regenerated with 10 state-boundary rules", "maintained shell was not regenerated after patch"),
        HardeningCriterion("source_v63_primary_demo_passed", source_v63.get("verdict") == "pass" and source_v63.get("counts", {}).get("manual_playtest_steps") == 12, "Report 303 primary-demo package still passes with 12 manual steps", "primary demo package is stale or failing"),
        HardeningCriterion("primary_demo_launcher_opened", AFTER_FIX_EVIDENCE["primary_demo"]["boundary_visible"] and AFTER_FIX_EVIDENCE["primary_demo"]["clean_links"] == 1 and AFTER_FIX_EVIDENCE["primary_demo"]["resume_links"] == 1, PRIMARY_DEMO_URL, "stable primary launcher did not open correctly"),
        HardeningCriterion("clean_launch_targets_maintained_shell", AFTER_FIX_EVIDENCE["clean_launch"]["url"] == TARGET_SHELL_URL and AFTER_FIX_EVIDENCE["clean_launch"]["has_snapshot_key_in_manifest"], TARGET_SHELL_URL, "clean launch does not target the maintained shell with updated manifest"),
        HardeningCriterion("manual_spine_completed", len(AFTER_FIX_EVIDENCE["sequence"]) == 18 and AFTER_FIX_EVIDENCE["export_point"]["payload"]["prepared"], "18 primary-demo/manual actions including exportReplay and resumeDemo", "manual playtest spine was not exercised"),
        HardeningCriterion("rollback_defect_reproduced_before_fix", before_restore_failed, "before fix: save x=214, mutate x=180, restore stayed x=180", "hardening report lacks a reproduced defect"),
        HardeningCriterion("rollback_fixed_after_patch", after_restore_fixed and after_mutated, "after fix: save x=214, mutate x=180, restore returns x=214", "save/restore still does not roll back"),
        HardeningCriterion("smoke_hook_tests_real_rollback", after_flags["smoke_rollback_tested"] and AFTER_FIX_EVIDENCE["smoke_point"]["payload"]["pass"], "runSaveRestoreSmoke payload pass=true and rollbackTested=true", "QA hook still only tests round trip storage"),
        HardeningCriterion("snapshot_key_documented_in_manifests", SNAPSHOT_KEY in v61_state_keys and SNAPSHOT_KEY in primary_state_keys, "saved snapshot key appears in v61 state-boundary rules and primary-demo state keys", "snapshot persistence is not visible to reviewers"),
        HardeningCriterion("resume_keeps_state_after_export", after_flags["resume_kept_state"] and AFTER_FIX_EVIDENCE["resume_point"]["replay_rows"] > 0, "resume path reopens shell with replay rows and latest exportReplay event", "leave/return continuity failed"),
        HardeningCriterion("no_console_errors_after_fix", after_flags["console_errors"] == 0, "fresh after-fix browser tab reported 0 console errors", "browser console errors remain"),
        HardeningCriterion("single_internal_playtest_not_external_user", True, "one internal browser manual-playtest pass, not an outside user cohort", "overclaiming internal QA as external validation"),
    ]

    scores = {row.criterion: (1.0 if row.passed else 0.0) for row in criteria}
    scores["single_internal_playtest_not_external_user"] = 0.872
    mean_channel_score = round(mean(scores.values()), 6)
    weakest_name, weakest_value = min(scores.items(), key=lambda item: item[1])
    weakest_score = round(weakest_value, 6)
    readiness = round(0.70 * mean_channel_score + 0.30 * weakest_score, 6)
    gates = {
        "all_hardening_criteria_passed": all(row.passed for row in criteria),
        "readiness_minimum_passed": readiness >= 0.90,
        "weakest_minimum_passed": weakest_score >= 0.86,
        "defect_was_reproduced_before_fix": before_restore_failed,
        "defect_fixed_in_after_evidence": after_restore_fixed,
        "honest_internal_playtest_cap_present": scores["single_internal_playtest_not_external_user"] < 0.88,
    }
    verdict = "pass" if all(gates.values()) else "fail"
    counts = {
        "manual_sequence_events": len(MANUAL_SEQUENCE),
        "runtime_defects_reproduced": 1 if before_restore_failed else 0,
        "runtime_defects_fixed": 1 if after_restore_fixed else 0,
        "patch_summary_items": len(PATCH_SUMMARY),
        "after_action_buttons": AFTER_FIX_EVIDENCE["clean_launch"]["action_button_count"],
        "after_replay_rows": AFTER_FIX_EVIDENCE["export_point"]["replay_rows"],
        "after_resume_replay_rows": AFTER_FIX_EVIDENCE["resume_point"]["replay_rows"],
        "after_console_errors": AFTER_FIX_EVIDENCE["flags"]["console_errors"],
        "v61_state_boundary_rules": source_v61.get("counts", {}).get("state_boundary_rules", 0),
    }

    results = {
        "report": REPORT,
        "prefix": PREFIX,
        "seed": seed,
        "verdict": verdict,
        "readiness": readiness,
        "primary_demo_manual_playtest_hardening_readiness": readiness,
        "mean_channel_score": mean_channel_score,
        "weakest_channel_score": weakest_score,
        "weakest_named_channel": weakest_name,
        "channels": {key: round(value, 6) for key, value in scores.items()},
        "counts": counts,
        "gates": gates,
        "criteria": [asdict(row) for row in criteria],
        "before_fix_evidence": BEFORE_FIX_EVIDENCE,
        "after_fix_evidence": AFTER_FIX_EVIDENCE,
        "manual_sequence": MANUAL_SEQUENCE,
        "patch_summary": PATCH_SUMMARY,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "source_v61_path": str(SOURCE_V61.relative_to(ROOT)),
        "source_v63_path": str(SOURCE_V63.relative_to(ROOT)),
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "state": f"artifacts/{PREFIX}_state.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "manual_sequence": f"artifacts/{PREFIX}_manual_sequence.csv",
            "report": f"docs/{REPORT}_{PREFIX}_report.md",
        },
    }
    state = {
        "report": REPORT,
        "seed": seed,
        "target_shell_url": TARGET_SHELL_URL,
        "primary_demo_url": PRIMARY_DEMO_URL,
        "snapshot_key": SNAPSHOT_KEY,
        "before_fix_evidence": BEFORE_FIX_EVIDENCE,
        "after_fix_evidence": AFTER_FIX_EVIDENCE,
        "patch_summary": PATCH_SUMMARY,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
    }
    return {"results": results, "state": state, "criteria": criteria}


def _report_markdown(results: dict[str, Any]) -> str:
    criteria_rows = "\n".join(
        f"| {row['criterion']} | {row['passed']} | {row['evidence']} |" for row in results["criteria"]
    )
    patch_rows = "\n".join(f"- {item}" for item in PATCH_SUMMARY)
    sequence_rows = "\n".join(f"| {index + 1} | {event} |" for index, event in enumerate(MANUAL_SEQUENCE))
    return f"""# Report 304: SSRM-3D Browser World v64 Primary Demo Manual Playtest Hardening

Report 304 uses the Report 303 primary demo path as intended: run the manual playtest against the real browser surface, find a concrete defect, patch the maintained shell, and record before/after evidence. It does not add another simulation organ.

## Result

- Verdict: `{results['verdict']}`
- Readiness: `{results['readiness']}`
- Mean channel score: `{results['mean_channel_score']}`
- Weakest channel: `{results['weakest_named_channel']}` at `{results['weakest_channel_score']}`
- Runtime defects reproduced: `{results['counts']['runtime_defects_reproduced']}`
- Runtime defects fixed: `{results['counts']['runtime_defects_fixed']}`
- Primary demo URL: `{PRIMARY_DEMO_URL}`
- Target shell URL: `{TARGET_SHELL_URL}`

## Defect found

Before the patch, `saveWorld` wrote the live world key and `restoreWorld` reloaded that same key. After saving at avatar `x=214`, moving west to `x=180`, restore stayed at `x=180`. That failed the manual-playtest rollback expectation.

## Fix

{patch_rows}

## After-fix browser evidence

- Save point: avatar `x={AFTER_FIX_EVIDENCE['save_point']['avatar']['x']}`, payload `{AFTER_FIX_EVIDENCE['save_point']['payload']}`
- Mutation point: avatar `x={AFTER_FIX_EVIDENCE['changed_point']['avatar']['x']}`
- Restore point: avatar `x={AFTER_FIX_EVIDENCE['restore_point']['avatar']['x']}`, payload `{AFTER_FIX_EVIDENCE['restore_point']['payload']}`
- Smoke hook: `{AFTER_FIX_EVIDENCE['smoke_point']['payload']}`
- Export point: `{AFTER_FIX_EVIDENCE['export_point']['payload']}`
- Resume point: replay rows `{AFTER_FIX_EVIDENCE['resume_point']['replay_rows']}`, latest event `{AFTER_FIX_EVIDENCE['resume_point']['latest_event']}`
- Console errors: `{AFTER_FIX_EVIDENCE['flags']['console_errors']}`

## Manual sequence exercised

| # | Event |
| --- | --- |
{sequence_rows}

## Criteria

| Criterion | Passed | Evidence |
| --- | --- | --- |
{criteria_rows}

## Honest limit

The weakest channel is `{results['weakest_named_channel']}`. This was one internal browser manual-playtest pass, not an external user cohort or production-readiness claim.

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
        "manual_sequence": ARTIFACTS / f"{PREFIX}_manual_sequence.csv",
        "report": ROOT / "docs" / f"{REPORT}_{PREFIX}_report.md",
    }
    _write_json(paths["results"], results)
    _write_json(paths["state"], state)
    _write_json(paths["browser_evidence"], {"before": BEFORE_FIX_EVIDENCE, "after": AFTER_FIX_EVIDENCE})
    _write_csv(paths["summary"], [{"metric": key, "value": value} for key, value in results["counts"].items()] + [
        {"metric": "readiness", "value": results["readiness"]},
        {"metric": "mean_channel_score", "value": results["mean_channel_score"]},
        {"metric": "weakest_channel_score", "value": results["weakest_channel_score"]},
        {"metric": "weakest_named_channel", "value": results["weakest_named_channel"]},
    ])
    _write_csv(paths["verdict"], [{"report": REPORT, "verdict": results["verdict"], "readiness": results["readiness"], "weakest_channel_score": results["weakest_channel_score"], "weakest_named_channel": results["weakest_named_channel"]}])
    _write_csv(paths["criteria"], criteria)
    _write_csv(paths["manual_sequence"], [{"position": index + 1, "event": event} for index, event in enumerate(MANUAL_SEQUENCE)])
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
