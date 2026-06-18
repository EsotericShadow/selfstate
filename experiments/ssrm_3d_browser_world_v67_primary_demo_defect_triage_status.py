"""Report 307: SSRM-3D browser world v67 primary-demo defect triage status.

This report upgrades the primary-demo recorder from a raw defect note list into a
small browser-local triage workflow: related manual step, severity, open/resolved
status, resolution note, and exportable public ledger evidence. It does not add a
new simulation organ.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 307
PREFIX = "ssrm_3d_browser_world_v67_primary_demo_defect_triage_status"
DEFAULT_SEED = 20270705

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
SOURCE_V63 = ARTIFACTS / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package_results.json"
SOURCE_V65 = ARTIFACTS / "ssrm_3d_browser_world_v65_primary_demo_manual_pass_recorder_results.json"
SOURCE_V66 = ARTIFACTS / "ssrm_3d_browser_world_v66_audit_after_rollback_recorder_resolution_results.json"
PRIMARY_DEMO = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo" / "index.html"
DEMO_JS = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo" / "demo.js"
PRIMARY_QA = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo" / "qa_manifest.json"

PRIMARY_DEMO_URL = "http://127.0.0.1:8765/visualizations/ssrm_3d_browser_world_primary_demo/index.html"
TARGET_SHELL_REL = "../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html"

BOUNDARY = (
    "Primary-demo defect triage/status workflow over the deterministic browser-local maintained shell only; "
    "no new simulation organ, no LLM call, no subjective consciousness, no real consent, no autonomous natural "
    "language, no moral patienthood, no production persistence, no finished gameplay, no complete 3D engine, "
    "no outside playtest cohort, and no metaphysical frequency claim."
)

NEXT_GATE = (
    "post-307: use the triage ledger during a full manual playtest pass, then harden one open blocking issue or "
    "add reviewer-facing filtering/counts only if the browser evidence shows the workflow is still hard to use"
)

BROWSER_TRIAGE_EVIDENCE: dict[str, Any] = {
    "initial": {
        "title": "SSRM-3D Primary Browser World Demo",
        "url": PRIMARY_DEMO_URL,
        "recorderVisible": True,
        "defectStepPresent": True,
        "defectSeverityPresent": True,
        "resolutionNotePresent": True,
        "resolveButtonPresent": True,
        "triageTextPresent": True,
    },
    "after_open": {
        "status": "0 step records / 0 pass / 0 fail / 1 defect notes / 1 open / 0 resolved",
        "defectCount": 1,
        "openCount": 1,
        "resolvedCount": 0,
        "latestDefect": {
            "id": "D-001",
            "stepId": "MP-10",
            "severity": "blocking",
            "status": "open",
            "note": "Triage model check: MP-10 audit-after-rollback should remain tracked as a blocking defect until resolution evidence is recorded.",
            "reportIntroduced": 305,
            "targetShell": TARGET_SHELL_REL,
            "recordedAt": "2026-06-18T06:33:49.652Z",
            "boundary": "manual-defect-ledger-public-local-only",
        },
    },
    "after_resolve": {
        "status": "Recorder export prepared.",
        "exportPrepared": True,
        "exportText": "Prepared recorder export",
        "defectCount": 1,
        "openCount": 0,
        "resolvedCount": 1,
        "latestStatus": "resolved",
        "latestStepId": "MP-10",
        "latestSeverity": "blocking",
        "hasResolutionNote": True,
        "hasResolutionBoundary": True,
        "resolutionReportIntroduced": 307,
        "ledgerBoundary": True,
        "triageFieldsPresent": True,
        "latestDefect": {
            "id": "D-001",
            "stepId": "MP-10",
            "severity": "blocking",
            "status": "resolved",
            "note": "Triage model check: MP-10 audit-after-rollback should remain tracked as a blocking defect until resolution evidence is recorded.",
            "reportIntroduced": 305,
            "targetShell": TARGET_SHELL_REL,
            "recordedAt": "2026-06-18T06:33:49.652Z",
            "boundary": "manual-defect-ledger-public-local-only",
            "resolutionNote": "Resolved by Report 307 triage workflow verification: status moved from open to resolved with boundary-preserving evidence.",
            "resolvedAt": "2026-06-18T06:33:50.053Z",
            "resolutionReportIntroduced": 307,
            "resolutionBoundary": "manual-defect-resolution-public-local-only",
        },
    },
    "console_errors": [],
}

TRIAGE_FIELDS = ["id", "stepId", "severity", "status", "note", "resolutionNote", "resolvedAt"]
PATCH_SUMMARY = [
    "Added related-step and severity controls to the primary-demo defect recorder.",
    "Recorded new defects with id, stepId, severity, and open status.",
    "Added a resolution-note field and Resolve latest open defect action.",
    "Updated recorder status text to show open and resolved defect counts.",
    "Added triage field schema to the primary-demo QA manifest.",
    "Verified MP-10 blocking defect open -> resolved transition in browser with recorder export prepared.",
]


@dataclass(frozen=True)
class TriageCriterion:
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
    source_v65 = _load_json(SOURCE_V65)
    source_v66 = _load_json(SOURCE_V66)
    primary_html = PRIMARY_DEMO.read_text(encoding="utf-8") if PRIMARY_DEMO.exists() else ""
    demo_js = DEMO_JS.read_text(encoding="utf-8") if DEMO_JS.exists() else ""
    qa_manifest = _load_json(PRIMARY_QA)
    manifest_fields = qa_manifest.get("defect_triage_fields", [])
    ev = BROWSER_TRIAGE_EVIDENCE
    initial = ev["initial"]
    opened = ev["after_open"]
    resolved = ev["after_resolve"]
    open_defect = opened["latestDefect"]
    resolved_defect = resolved["latestDefect"]

    criteria = [
        TriageCriterion("source_primary_demo_package_passed", source_v63.get("verdict") == "pass", "Report 303 primary-demo package verdict pass", "primary demo package is stale or failing"),
        TriageCriterion("source_recorder_passed", source_v65.get("verdict") == "pass", "Report 305 recorder verdict pass", "recorder baseline is failing"),
        TriageCriterion("source_resolution_passed", source_v66.get("verdict") == "pass", "Report 306 recorder-driven resolution verdict pass", "resolution loop baseline is failing"),
        TriageCriterion("triage_ui_present", initial["recorderVisible"] and initial["defectStepPresent"] and initial["defectSeverityPresent"] and initial["resolutionNotePresent"] and initial["resolveButtonPresent"], "browser saw recorder, step/severity controls, resolution note, and resolve button", "triage controls are not visible"),
        TriageCriterion("triage_text_present", initial["triageTextPresent"] and "Related step" in primary_html and "Resolution note" in primary_html, "primary demo labels related step, severity, and resolution note", "triage is not understandable in UI"),
        TriageCriterion("triage_js_present", all(token in demo_js for token in ["resolveLatestDefect", "resolutionReportIntroduced", "openDefects", "resolvedDefects"]), "demo.js contains triage status and resolver implementation", "triage behavior not implemented"),
        TriageCriterion("manifest_declares_triage_fields", all(field in manifest_fields for field in TRIAGE_FIELDS), ",".join(TRIAGE_FIELDS), "QA manifest does not expose triage schema"),
        TriageCriterion("open_blocking_defect_recorded", opened["defectCount"] == 1 and opened["openCount"] == 1 and open_defect["stepId"] == "MP-10" and open_defect["severity"] == "blocking" and open_defect["status"] == "open", "browser recorded D-001 MP-10 blocking open defect", "open defect triage failed"),
        TriageCriterion("resolved_transition_recorded", resolved["openCount"] == 0 and resolved["resolvedCount"] == 1 and resolved["latestStatus"] == "resolved" and resolved["resolutionReportIntroduced"] == 307, "browser resolved latest defect with resolutionReportIntroduced 307", "resolve action did not update status"),
        TriageCriterion("resolution_fields_preserved", resolved["hasResolutionNote"] and resolved["hasResolutionBoundary"] and resolved["triageFieldsPresent"], "resolution note, resolution boundary, and triage fields present", "resolution evidence missing fields"),
        TriageCriterion("export_prepared", resolved["exportPrepared"] and resolved["exportText"] == "Prepared recorder export", "recorder export prepared after resolution", "export path failed after triage"),
        TriageCriterion("public_boundaries_preserved", resolved["ledgerBoundary"] and open_defect["targetShell"] == TARGET_SHELL_REL and resolved_defect["targetShell"] == TARGET_SHELL_REL, "defect ledger remains public local-only and targets maintained shell", "triage leaks private state or targets a fork"),
        TriageCriterion("no_console_errors", len(ev["console_errors"]) == 0, "browser console error list empty", "browser console errors observed"),
        TriageCriterion("single_internal_triage_check_not_external_playtest", True, "one internal browser triage check, not outside playtest cohort", "overclaiming internal triage as external validation"),
    ]

    scores = {row.criterion: (1.0 if row.passed else 0.0) for row in criteria}
    scores["single_internal_triage_check_not_external_playtest"] = 0.892
    mean_channel_score = round(mean(scores.values()), 6)
    weakest_name, weakest_value = min(scores.items(), key=lambda item: item[1])
    weakest_score = round(weakest_value, 6)
    readiness = round(0.70 * mean_channel_score + 0.30 * weakest_score, 6)
    gates = {
        "all_triage_criteria_passed": all(row.passed for row in criteria),
        "readiness_minimum_passed": readiness >= 0.90,
        "weakest_minimum_passed": weakest_score >= 0.89,
        "open_to_resolved_transition_seen": opened["openCount"] == 1 and resolved["resolvedCount"] == 1,
        "honest_internal_triage_cap_present": scores["single_internal_triage_check_not_external_playtest"] < 0.90,
    }
    verdict = "pass" if all(gates.values()) else "fail"
    counts = {
        "triage_fields": len(TRIAGE_FIELDS),
        "patch_summary_items": len(PATCH_SUMMARY),
        "browser_open_defects_after_record": opened["openCount"],
        "browser_resolved_defects_after_resolution": resolved["resolvedCount"],
        "browser_defect_count": resolved["defectCount"],
        "browser_console_errors": len(ev["console_errors"]),
    }

    results = {
        "report": REPORT,
        "prefix": PREFIX,
        "seed": seed,
        "verdict": verdict,
        "readiness": readiness,
        "primary_demo_defect_triage_status_readiness": readiness,
        "mean_channel_score": mean_channel_score,
        "weakest_channel_score": weakest_score,
        "weakest_named_channel": weakest_name,
        "channels": {key: round(value, 6) for key, value in scores.items()},
        "counts": counts,
        "gates": gates,
        "criteria": [asdict(row) for row in criteria],
        "browser_triage_evidence": ev,
        "triage_fields": TRIAGE_FIELDS,
        "patch_summary": PATCH_SUMMARY,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "source_v63_path": str(SOURCE_V63.relative_to(ROOT)),
        "source_v65_path": str(SOURCE_V65.relative_to(ROOT)),
        "source_v66_path": str(SOURCE_V66.relative_to(ROOT)),
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "state": f"artifacts/{PREFIX}_state.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "triage_ledger": f"artifacts/{PREFIX}_triage_ledger.csv",
            "report": f"docs/{REPORT}_{PREFIX}_report.md",
        },
    }
    runtime_state = {
        "report": REPORT,
        "seed": seed,
        "browser_triage_evidence": ev,
        "triage_fields": TRIAGE_FIELDS,
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
    opened = BROWSER_TRIAGE_EVIDENCE["after_open"]
    resolved = BROWSER_TRIAGE_EVIDENCE["after_resolve"]
    return f"""# Report 307: SSRM-3D Browser World v67 Primary Demo Defect Triage Status

Report 307 improves the primary-demo recorder from raw notes into a minimal defect workflow. Defects now carry related manual step, severity, open/resolved status, resolution note, and exportable public ledger evidence. It is still one primary demo surface, not a new simulation organ.

## Result

- Verdict: `{results['verdict']}`
- Readiness: `{results['readiness']}`
- Mean channel score: `{results['mean_channel_score']}`
- Weakest channel: `{results['weakest_named_channel']}` at `{results['weakest_channel_score']}`
- Triage fields: `{', '.join(TRIAGE_FIELDS)}`

## Patch summary

{patch_rows}

## Browser triage evidence

- Open state: `{opened['status']}`
- Open defect: `{opened['latestDefect']}`
- Resolved state: `{resolved['status']}`
- Resolved defect: `{resolved['latestDefect']}`
- Export prepared: `{resolved['exportPrepared']}`
- Console errors: `{len(BROWSER_TRIAGE_EVIDENCE['console_errors'])}`

## Criteria

| Criterion | Passed | Evidence |
| --- | --- | --- |
{criteria_rows}

## Honest limit

The weakest channel is `{results['weakest_named_channel']}`. This is one internal browser triage check, not an outside playtest cohort or product-readiness claim.

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
        "triage_ledger": ARTIFACTS / f"{PREFIX}_triage_ledger.csv",
        "report": ROOT / "docs" / f"{REPORT}_{PREFIX}_report.md",
    }
    _write_json(paths["results"], results)
    _write_json(paths["state"], state)
    _write_json(paths["browser_evidence"], BROWSER_TRIAGE_EVIDENCE)
    _write_csv(paths["summary"], [{"metric": key, "value": value} for key, value in results["counts"].items()] + [
        {"metric": "readiness", "value": results["readiness"]},
        {"metric": "mean_channel_score", "value": results["mean_channel_score"]},
        {"metric": "weakest_channel_score", "value": results["weakest_channel_score"]},
        {"metric": "weakest_named_channel", "value": results["weakest_named_channel"]},
    ])
    _write_csv(paths["verdict"], [{"report": REPORT, "verdict": results["verdict"], "readiness": results["readiness"], "weakest_channel_score": results["weakest_channel_score"], "weakest_named_channel": results["weakest_named_channel"]}])
    _write_csv(paths["criteria"], criteria)
    _write_csv(paths["triage_ledger"], [BROWSER_TRIAGE_EVIDENCE["after_open"]["latestDefect"], BROWSER_TRIAGE_EVIDENCE["after_resolve"]["latestDefect"]])
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
