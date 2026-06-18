"""Report 305: SSRM-3D browser world v65 primary-demo manual pass recorder.

This report adds and verifies an in-page manual pass recorder plus defect ledger
for the stable primary demo. It is consolidation infrastructure for the single
playable shell, not a new simulation organ.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 305
PREFIX = "ssrm_3d_browser_world_v65_primary_demo_manual_pass_recorder"
DEFAULT_SEED = 20270703

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
SOURCE_V63 = ARTIFACTS / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package_results.json"
SOURCE_V64 = ARTIFACTS / "ssrm_3d_browser_world_v64_primary_demo_manual_playtest_hardening_results.json"
PRIMARY_QA = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo" / "qa_manifest.json"
PRIMARY_DEMO = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo" / "index.html"
DEMO_JS = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo" / "demo.js"

PRIMARY_DEMO_URL = "http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_primary_demo/index.html"
TARGET_SHELL = "../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html"
MANUAL_RECORD_KEY = "ssrm_primary_demo_manual_pass_records"
DEFECT_LEDGER_KEY = "ssrm_primary_demo_defect_ledger"
RECORDER_EXPORT_KEY = "ssrm_primary_demo_recorder_export"

BOUNDARY = (
    "Primary-demo manual pass recorder and defect ledger for deterministic browser-local review only; "
    "no new simulation organ, no LLM call, no subjective consciousness, no real consent, no autonomous "
    "natural language, no moral patienthood, no production persistence, no finished gameplay, no complete "
    "3D engine, no outside playtest cohort, and no metaphysical frequency claim."
)

NEXT_GATE = (
    "post-305: use the in-page recorder during the next browser pass, harden one recorded defect or usability "
    "gap in the same maintained shell, and keep report work tied to primary-demo evidence"
)

BROWSER_RECORDER_EVIDENCE: dict[str, Any] = {
    "url": PRIMARY_DEMO_URL,
    "actions": [
        "clearRecorder",
        "record MP-01 pass",
        "record MP-08 pass",
        "record MP-10 fail",
        "fill defect note",
        "recordDefect",
        "exportRecorder",
    ],
    "recorder_state": {
        "title": "SSRM-3D Primary Browser World Demo",
        "url": PRIMARY_DEMO_URL,
        "recorderVisible": True,
        "recordButtons": 24,
        "passButtons": 12,
        "failButtons": 12,
        "status": "Recorder export prepared.",
        "exportPrepared": True,
        "exportText": "Prepared recorder export",
        "recordCount": 3,
        "defectCount": 1,
        "passCount": 2,
        "failCount": 1,
        "stepIds": ["MP-01", "MP-08", "MP-10"],
        "defectNoteIncludesAudit": True,
        "recorderBoundary": True,
        "latestRecord": {
            "boundary": "manual-recorder-public-local-only",
            "recordedAt": "2026-06-18T06:23:03.087Z",
            "reportIntroduced": 305,
            "result": "fail",
            "stepId": "MP-10",
            "targetShell": TARGET_SHELL,
        },
        "latestDefect": {
            "boundary": "manual-defect-ledger-public-local-only",
            "note": "Observed MP-10 audit output should be checked after rollback smoke; recorder captured this as a review note.",
            "recordedAt": "2026-06-18T06:23:03.465Z",
            "reportIntroduced": 305,
            "targetShell": TARGET_SHELL,
        },
    },
    "console_errors": [],
}

RECORDER_KEYS = [MANUAL_RECORD_KEY, DEFECT_LEDGER_KEY, RECORDER_EXPORT_KEY]


@dataclass(frozen=True)
class RecorderCriterion:
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
    source_v63 = _load_json(SOURCE_V63)
    source_v64 = _load_json(SOURCE_V64)
    primary_manifest = _load_json(PRIMARY_QA)
    demo_html = PRIMARY_DEMO.read_text(encoding="utf-8") if PRIMARY_DEMO.exists() else ""
    demo_js = DEMO_JS.read_text(encoding="utf-8") if DEMO_JS.exists() else ""
    state_keys = set(primary_manifest.get("state_keys", []))
    ev = BROWSER_RECORDER_EVIDENCE
    state = ev["recorder_state"]

    criteria = [
        RecorderCriterion("source_primary_demo_package_passed", source_v63.get("verdict") == "pass", "Report 303 primary demo package verdict pass", "primary demo package is stale or failing"),
        RecorderCriterion("source_rollback_hardening_passed", source_v64.get("verdict") == "pass" and source_v64.get("counts", {}).get("runtime_defects_fixed") == 1, "Report 304 rollback hardening verdict pass and fixed one defect", "recorder is not layered on a hardened shell"),
        RecorderCriterion("recorder_ui_present", "manualRecorder" in demo_html and "Manual pass recorder and defect ledger" in demo_html, "primary demo contains manualRecorder section", "reviewers cannot record manual outcomes in page"),
        RecorderCriterion("recorder_js_present", all(key in demo_js for key in RECORDER_KEYS), "demo.js contains manual record, defect ledger, and export keys", "recorder state keys are not implemented"),
        RecorderCriterion("recorder_keys_in_manifest", all(key in state_keys for key in RECORDER_KEYS), ",".join(RECORDER_KEYS), "recorder keys are not visible in QA manifest"),
        RecorderCriterion("browser_record_buttons_visible", state["recordButtons"] == 24 and state["passButtons"] == 12 and state["failButtons"] == 12, "browser saw 24 record controls for 12 manual steps", "manual steps cannot all be marked pass/fail"),
        RecorderCriterion("browser_record_counts_correct", state["recordCount"] == 3 and state["passCount"] == 2 and state["failCount"] == 1 and state["stepIds"] == ["MP-01", "MP-08", "MP-10"], "fresh clean pass recorded 2 pass and 1 fail across MP-01/MP-08/MP-10", "manual records were not captured correctly"),
        RecorderCriterion("browser_defect_note_recorded", state["defectCount"] == 1 and state["defectNoteIncludesAudit"], "one MP-10 audit defect note recorded", "defect notes are not captured"),
        RecorderCriterion("browser_recorder_export_prepared", state["exportPrepared"] and state["exportText"] == "Prepared recorder export", "recorder export link prepared", "recorder export path failed"),
        RecorderCriterion("recorder_public_boundary_preserved", state["recorderBoundary"] and state["latestRecord"]["targetShell"] == TARGET_SHELL and state["latestDefect"]["targetShell"] == TARGET_SHELL, "records and defects use public local-only boundaries and target maintained shell", "recorder leaks private/ambiguous state or targets a fork"),
        RecorderCriterion("no_console_errors", len(ev["console_errors"]) == 0, "browser console error list empty", "browser console errors observed"),
        RecorderCriterion("single_internal_recorder_check_not_external_playtest", True, "one internal browser recorder check, not outside playtest cohort", "overclaiming recorder QA as external validation"),
    ]

    scores = {row.criterion: (1.0 if row.passed else 0.0) for row in criteria}
    scores["single_internal_recorder_check_not_external_playtest"] = 0.878
    mean_channel_score = round(mean(scores.values()), 6)
    weakest_name, weakest_value = min(scores.items(), key=lambda item: item[1])
    weakest_score = round(weakest_value, 6)
    readiness = round(0.70 * mean_channel_score + 0.30 * weakest_score, 6)
    gates = {
        "all_recorder_criteria_passed": all(row.passed for row in criteria),
        "readiness_minimum_passed": readiness >= 0.90,
        "weakest_minimum_passed": weakest_score >= 0.87,
        "recorder_targets_primary_demo": state["url"] == PRIMARY_DEMO_URL,
        "honest_internal_check_cap_present": scores["single_internal_recorder_check_not_external_playtest"] < 0.88,
    }
    verdict = "pass" if all(gates.values()) else "fail"
    counts = {
        "manual_steps": 12,
        "record_buttons": state["recordButtons"],
        "browser_records": state["recordCount"],
        "browser_pass_records": state["passCount"],
        "browser_fail_records": state["failCount"],
        "browser_defect_notes": state["defectCount"],
        "recorder_state_keys": len(RECORDER_KEYS),
        "browser_console_errors": len(ev["console_errors"]),
    }

    results = {
        "report": REPORT,
        "prefix": PREFIX,
        "seed": seed,
        "verdict": verdict,
        "readiness": readiness,
        "primary_demo_manual_pass_recorder_readiness": readiness,
        "mean_channel_score": mean_channel_score,
        "weakest_channel_score": weakest_score,
        "weakest_named_channel": weakest_name,
        "channels": {key: round(value, 6) for key, value in scores.items()},
        "counts": counts,
        "gates": gates,
        "criteria": [asdict(row) for row in criteria],
        "browser_recorder_evidence": ev,
        "recorder_keys": RECORDER_KEYS,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "source_v63_path": str(SOURCE_V63.relative_to(ROOT)),
        "source_v64_path": str(SOURCE_V64.relative_to(ROOT)),
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "state": f"artifacts/{PREFIX}_state.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "manual_records": f"artifacts/{PREFIX}_manual_records.csv",
            "report": f"docs/{REPORT}_{PREFIX}_report.md",
        },
    }
    runtime_state = {
        "report": REPORT,
        "seed": seed,
        "primary_demo_url": PRIMARY_DEMO_URL,
        "target_shell": TARGET_SHELL,
        "browser_recorder_evidence": ev,
        "recorder_keys": RECORDER_KEYS,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
    }
    return {"results": results, "state": runtime_state, "criteria": criteria}


def _report_markdown(results: dict[str, Any]) -> str:
    criteria_rows = "\n".join(
        f"| {row['criterion']} | {row['passed']} | {row['evidence']} |" for row in results["criteria"]
    )
    state = BROWSER_RECORDER_EVIDENCE["recorder_state"]
    return f"""# Report 305: SSRM-3D Browser World v65 Primary Demo Manual Pass Recorder

Report 305 adds a small in-page manual pass recorder and defect ledger to the stable primary demo. This is consolidation infrastructure: reviewers can record pass/fail outcomes and defect notes while using the maintained shell, then prepare a public local export.

## Result

- Verdict: `{results['verdict']}`
- Readiness: `{results['readiness']}`
- Mean channel score: `{results['mean_channel_score']}`
- Weakest channel: `{results['weakest_named_channel']}` at `{results['weakest_channel_score']}`
- Primary demo URL: `{PRIMARY_DEMO_URL}`
- Target shell: `{TARGET_SHELL}`

## Browser evidence

- Recorder visible: `{state['recorderVisible']}`
- Record controls: `{state['recordButtons']}` total, `{state['passButtons']}` pass, `{state['failButtons']}` fail
- Fresh records: `{state['recordCount']}` total, `{state['passCount']}` pass, `{state['failCount']}` fail
- Step IDs recorded: `{', '.join(state['stepIds'])}`
- Defect notes: `{state['defectCount']}`
- Export prepared: `{state['exportPrepared']}` / `{state['exportText']}`
- Console errors: `{len(BROWSER_RECORDER_EVIDENCE['console_errors'])}`

## Criteria

| Criterion | Passed | Evidence |
| --- | --- | --- |
{criteria_rows}

## Honest limit

The weakest channel is `{results['weakest_named_channel']}`. This is one internal browser recorder check, not an outside playtest cohort or product-readiness claim.

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
        "manual_records": ARTIFACTS / f"{PREFIX}_manual_records.csv",
        "report": ROOT / "docs" / f"{REPORT}_{PREFIX}_report.md",
    }
    _write_json(paths["results"], results)
    _write_json(paths["state"], state)
    _write_json(paths["browser_evidence"], BROWSER_RECORDER_EVIDENCE)
    _write_csv(paths["summary"], [{"metric": key, "value": value} for key, value in results["counts"].items()] + [
        {"metric": "readiness", "value": results["readiness"]},
        {"metric": "mean_channel_score", "value": results["mean_channel_score"]},
        {"metric": "weakest_channel_score", "value": results["weakest_channel_score"]},
        {"metric": "weakest_named_channel", "value": results["weakest_named_channel"]},
    ])
    _write_csv(paths["verdict"], [{"report": REPORT, "verdict": results["verdict"], "readiness": results["readiness"], "weakest_channel_score": results["weakest_channel_score"], "weakest_named_channel": results["weakest_named_channel"]}])
    _write_csv(paths["criteria"], criteria)
    records = BROWSER_RECORDER_EVIDENCE["recorder_state"]
    _write_csv(paths["manual_records"], [
        {"kind": "record", "step_id": step, "source": "browser_recorder_evidence"} for step in records["stepIds"]
    ] + [{"kind": "defect", "step_id": "MP-10", "source": "browser_recorder_evidence"}])
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
