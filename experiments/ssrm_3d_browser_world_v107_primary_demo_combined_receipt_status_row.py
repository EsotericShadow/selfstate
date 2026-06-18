"""Report 347: combined outside-review receipt status row.

Report 346 embedded lifecycle smoke status into the outside-review handoff payload.
Report 347 makes that combined receipt visible before download as a field-by-field
status row for shell evidence, reviewed completion, manual notes, defect state,
recorder export, and lifecycle preflight packet.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 347
SEED = 20270745
PREFIX = "ssrm_3d_browser_world_v107_primary_demo_combined_receipt_status_row"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"

ENTRYPOINT_JS = ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/demo.js"
ENTRYPOINT_HTML = ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/index.html"
MANUAL_PLAYTEST = ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/manual_playtest.md"
GENERATOR = ROOT / "experiments/ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
COMBINED_RESULTS = ROOT / "artifacts/ssrm_3d_browser_world_v106_primary_demo_combined_outside_review_handoff_receipt_results.json"
COMBINED_CONTRACT = ROOT / "artifacts/ssrm_3d_browser_world_v106_primary_demo_combined_outside_review_handoff_receipt_combined_receipt_contract.json"
EXPERIMENT_INDEX = ROOT / "scripts/run_experiments.py"

EXPECTED_FIELDS = {
    "shellEvidence": "Shell evidence",
    "reviewedHandoffCompletion": "Reviewed completion",
    "manualRecords": "Manual notes",
    "defects": "Defect state",
    "recorderExport": "Recorder export",
    "lifecyclePreflightPacket": "Lifecycle preflight packet",
}

BOUNDARIES = (
    "browser-local combined receipt status row source verification only",
    "artifact-backed receipt field status only",
    "no live hosted URL claim",
    "no live browser automation claim",
    "no production persistence claim",
    "no autonomous natural-language claim",
    "no subjective-consciousness claim",
    "no moral-patienthood claim",
    "no complete 3D engine claim",
    "no finished gameplay claim",
)

NEXT_GATE = (
    "post-347: make the combined receipt status row enforceable by disabling or warning on "
    "handoff download when required receipt fields are missing, while preserving a deliberate "
    "debug override for incomplete review packets"
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _criterion(name: str, passed: bool, detail: str, channel: str) -> dict[str, Any]:
    return {"name": name, "passed": bool(passed), "score": 1.0 if passed else 0.0, "channel": channel, "detail": detail}


def _has_all(text: str, terms: tuple[str, ...]) -> bool:
    return all(term in text for term in terms)


def build_results() -> dict[str, Any]:
    js = _read(ENTRYPOINT_JS)
    html = _read(ENTRYPOINT_HTML)
    manual = _read(MANUAL_PLAYTEST)
    generator = _read(GENERATOR)
    experiment_index = _read(EXPERIMENT_INDEX)
    combined_results = _load_json(COMBINED_RESULTS) if COMBINED_RESULTS.exists() else {}
    combined_contract = _load_json(COMBINED_CONTRACT) if COMBINED_CONTRACT.exists() else {}

    html_terms = (
        'id="combinedReceiptStatusRow"',
        'id="combinedReceiptStatus"',
        'id="combinedReceiptFieldList"',
        'data-combined-receipt-ready="false"',
        'aria-label="Combined outside-review receipt included fields"',
    )
    html_field_terms = tuple(
        f'data-combined-receipt-field="{field}" data-combined-receipt-status="pending"' for field in EXPECTED_FIELDS
    ) + tuple(EXPECTED_FIELDS.values())
    js_terms = (
        "function combinedReceiptFieldStatus(payload)",
        "function renderCombinedReceiptStatus(payload, message)",
        "reportIntroduced: 347",
        "payload.combinedReceiptStatus = combinedReceiptFieldStatus(payload);",
        "previewCombinedReceiptStatus: combinedReceiptStatus",
        "combined receipt ready",
        "combined receipt blocked",
        "data-combined-receipt-field",
        "item.dataset.combinedReceiptStatus",
        "included",
        "missing",
        "combined-outside-review-receipt-status-browser-local-only",
    )
    generator_html_terms = tuple(term.replace('"', '\\"') for term in html_terms + html_field_terms)
    manual_terms = (
        "visible combined receipt status row",
        "shell evidence, reviewed completion, manual notes, defect state, recorder export, and lifecycle preflight packet before download",
    )

    status_row_contract = {
        "report": REPORT,
        "status_row": "combinedReceiptStatusRow",
        "status_text": "combinedReceiptStatus",
        "field_list": "combinedReceiptFieldList",
        "fields": EXPECTED_FIELDS,
        "payload_status_field": "combinedReceiptStatus",
        "preview_status_field": "previewCombinedReceiptStatus",
        "source_combined_receipt_contract": str(COMBINED_CONTRACT.relative_to(ROOT)),
        "blocking_phase": combined_contract.get("blocking_phase", "unknown"),
        "included_field_count": len(combined_contract.get("included_fields", [])),
        "boundary": "combined-outside-review-receipt-status-browser-local-only",
    }

    criteria = [
        _criterion(
            "combined_receipt_artifacts_available_and_passing",
            COMBINED_RESULTS.exists() and COMBINED_CONTRACT.exists() and combined_results.get("verdict") == "pass",
            "Report 346 combined receipt results and contract exist and pass.",
            "artifact source",
        ),
        _criterion(
            "combined_receipt_contract_field_set_complete",
            set(combined_contract.get("included_fields", [])) == set(EXPECTED_FIELDS) and combined_contract.get("blocking_phase") == "none",
            "Source combined receipt contract has all six required fields and no lifecycle blocking phase.",
            "artifact source",
        ),
        _criterion(
            "launcher_has_combined_receipt_status_row",
            _has_all(html, html_terms),
            "Primary launcher exposes a combined receipt status row before handoff action/download controls.",
            "entrypoint row",
        ),
        _criterion(
            "launcher_lists_all_combined_receipt_fields",
            _has_all(html, html_field_terms),
            "Primary launcher lists shell evidence, reviewed completion, manual notes, defect state, recorder export, and lifecycle preflight packet.",
            "entrypoint row",
        ),
        _criterion(
            "javascript_computes_combined_receipt_status",
            _has_all(js, js_terms[:5]),
            "Launcher JS computes combined receipt field status and stores it in payload and preview evidence.",
            "browser behavior",
        ),
        _criterion(
            "javascript_renders_included_missing_states",
            _has_all(js, js_terms[5:]),
            "Launcher JS renders ready/blocked and included/missing statuses for each combined receipt field.",
            "browser behavior",
        ),
        _criterion(
            "readable_summary_mentions_receipt_status",
            _has_all(js, ("const receiptTextStatus =", "combined receipt ready", "combined receipt blocked", "includedCount", "totalCount")),
            "Readable handoff summary includes combined receipt readiness and field count.",
            "visible summary",
        ),
        _criterion(
            "manual_documents_status_row",
            _has_all(manual, manual_terms),
            "Manual playtest documentation requires the visible combined receipt status row before download.",
            "manual path",
        ),
        _criterion(
            "generator_preserves_status_row_html",
            _has_all(generator, generator_html_terms),
            "v63 generator preserves combined receipt status row HTML and field rows.",
            "generator durability",
        ),
        _criterion(
            "generator_preserves_status_row_behavior",
            _has_all(generator, js_terms + manual_terms),
            "v63 generator preserves combined receipt status computation, rendering, payload storage, and manual guidance.",
            "generator durability",
        ),
        _criterion(
            "status_row_contract_is_complete",
            set(status_row_contract["fields"]) == set(EXPECTED_FIELDS) and status_row_contract["included_field_count"] == len(EXPECTED_FIELDS),
            "Report 347 emits a status-row contract for all six combined receipt fields.",
            "status contract",
        ),
        _criterion(
            "experiment_index_includes_status_row_report",
            "experiments.ssrm_3d_browser_world_v107_primary_demo_combined_receipt_status_row" in experiment_index,
            "Experiment runner index includes the Report 347 verifier module.",
            "runner index",
        ),
        _criterion(
            "claim_boundary_preserved",
            all(boundary.startswith("no ") or "browser-local" in boundary or "artifact" in boundary for boundary in BOUNDARIES),
            "Boundary rejects hosted URL, live E2E, production persistence, autonomous language, consciousness, moral patienthood, complete engine, and finished gameplay claims.",
            "claim hygiene",
        ),
    ]

    by_channel: dict[str, list[float]] = {}
    for item in criteria:
        by_channel.setdefault(item["channel"], []).append(float(item["score"]))

    metrics = {
        "readiness": mean(float(item["score"]) for item in criteria),
        "weakest_channel_score": min(float(item["score"]) for item in criteria),
        "artifact_source_score": mean(by_channel.get("artifact source", [0.0])),
        "entrypoint_row_score": mean(by_channel.get("entrypoint row", [0.0])),
        "browser_behavior_score": mean(by_channel.get("browser behavior", [0.0])),
        "visible_summary_score": mean(by_channel.get("visible summary", [0.0])),
        "manual_path_score": mean(by_channel.get("manual path", [0.0])),
        "generator_durability_score": mean(by_channel.get("generator durability", [0.0])),
        "status_contract_score": mean(by_channel.get("status contract", [0.0])),
        "runner_index_score": mean(by_channel.get("runner index", [0.0])),
        "claim_hygiene_score": mean(by_channel.get("claim hygiene", [0.0])),
        "field_count": len(EXPECTED_FIELDS),
        "source_included_field_count": len(combined_contract.get("included_fields", [])),
        "blocking_phase_count": 0 if combined_contract.get("blocking_phase") == "none" else 1,
        "criterion_count": len(criteria),
    }
    verdict = "pass" if metrics["weakest_channel_score"] >= 1.0 else "fail"

    return {
        "report": REPORT,
        "seed": SEED,
        "prefix": PREFIX,
        "verdict": verdict,
        "metrics": metrics,
        "criteria": criteria,
        "status_row_contract": status_row_contract,
        "boundaries": BOUNDARIES,
        "next_gate": NEXT_GATE,
    }


def _write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    criteria = results["criteria"]
    contract = results["status_row_contract"]
    report_path = DOCS / f"{REPORT}_{PREFIX}_report.md"
    criterion_lines = "\n".join(f"- {'PASS' if item['passed'] else 'FAIL'} `{item['name']}` ({item['channel']}): {item['detail']}" for item in criteria)
    field_lines = "\n".join(f"- `{field}`: {label}" for field, label in contract["fields"].items())
    boundary_lines = "\n".join(f"- {boundary}" for boundary in BOUNDARIES)

    report_path.write_text(
        f"# Report {REPORT}: SSRM-3D Browser World v107 Primary Demo Combined Receipt Status Row\n\n"
        "## Purpose\n\n"
        "Report 347 makes the combined outside-review handoff receipt visible before download. The launcher now shows one status row with every required receipt field marked pending, included, or missing.\n\n"
        "## What changed\n\n"
        "- Added `combinedReceiptStatusRow`, `combinedReceiptStatus`, and `combinedReceiptFieldList` before the handoff action/download controls.\n"
        "- Added six field rows: shell evidence, reviewed completion, manual notes, defect state, recorder export, and lifecycle preflight packet.\n"
        "- Added `combinedReceiptFieldStatus()` and `renderCombinedReceiptStatus()` to compute and render included/missing status.\n"
        "- Stored `combinedReceiptStatus` in the outside-review handoff payload and preview JSON.\n"
        "- Updated manual guidance and the v63 generator so regenerated launchers preserve the row and behavior.\n\n"
        "## Status row fields\n\n"
        f"{field_lines}\n\n"
        "## Metrics\n\n"
        f"- verdict: `{results['verdict']}`\n"
        f"- readiness: `{metrics['readiness']:.3f}`\n"
        f"- weakest_channel_score: `{metrics['weakest_channel_score']:.3f}`\n"
        f"- artifact_source_score: `{metrics['artifact_source_score']:.3f}`\n"
        f"- entrypoint_row_score: `{metrics['entrypoint_row_score']:.3f}`\n"
        f"- browser_behavior_score: `{metrics['browser_behavior_score']:.3f}`\n"
        f"- visible_summary_score: `{metrics['visible_summary_score']:.3f}`\n"
        f"- manual_path_score: `{metrics['manual_path_score']:.3f}`\n"
        f"- generator_durability_score: `{metrics['generator_durability_score']:.3f}`\n"
        f"- status_contract_score: `{metrics['status_contract_score']:.3f}`\n"
        f"- field_count: `{metrics['field_count']}`\n"
        f"- blocking_phase_count: `{metrics['blocking_phase_count']}`\n"
        f"- criterion_count: `{metrics['criterion_count']}`\n\n"
        "## Criteria\n\n"
        f"{criterion_lines}\n\n"
        "## Boundary\n\n"
        f"{boundary_lines}\n\n"
        "## Interpretation\n\n"
        "The outside-review path now surfaces receipt completeness before reviewers download the JSON handoff. This improves review usability, but remains browser-local source/artifact verification rather than a hosted URL proof, live browser automation proof, production persistence proof, autonomous conversation proof, consciousness claim, moral-patienthood claim, complete engine, or finished gameplay.\n\n"
        "## Next gate\n\n"
        f"{results['next_gate']}\n",
        encoding="utf-8",
    )


def write_artifacts(results: dict[str, Any]) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    DOCS.mkdir(exist_ok=True)
    (ARTIFACTS / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACTS / f"{PREFIX}_state.json").write_text(json.dumps({"report": REPORT, "seed": SEED, "verdict": results["verdict"], "metrics": results["metrics"], "status_row_contract": results["status_row_contract"], "next_gate": results["next_gate"]}, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACTS / f"{PREFIX}_status_row_contract.json").write_text(json.dumps(results["status_row_contract"], indent=2, sort_keys=True), encoding="utf-8")
    _write_csv(ARTIFACTS / f"{PREFIX}_summary.csv", [{"report": REPORT, "seed": SEED, "verdict": results["verdict"], **results["metrics"]}], ["report", "seed", "verdict", *results["metrics"].keys()])
    _write_csv(ARTIFACTS / f"{PREFIX}_verdict.csv", [{"report": REPORT, "verdict": results["verdict"], "weakest_channel_score": results["metrics"]["weakest_channel_score"], "field_count": results["metrics"]["field_count"], "next_gate": results["next_gate"]}], ["report", "verdict", "weakest_channel_score", "field_count", "next_gate"])
    _write_csv(ARTIFACTS / f"{PREFIX}_criteria.csv", results["criteria"], ["name", "passed", "score", "channel", "detail"])
    _write_report(results)


def main() -> dict[str, Any]:
    results = build_results()
    write_artifacts(results)
    print(json.dumps({"report": REPORT, "verdict": results["verdict"], "metrics": results["metrics"]}, indent=2, sort_keys=True))
    return results


if __name__ == "__main__":
    main()
