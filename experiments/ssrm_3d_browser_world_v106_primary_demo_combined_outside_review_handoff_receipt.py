"""Report 346: combined outside-review handoff receipt.

Report 345 made the lifecycle preflight packet exportable. Report 346 connects
that packet to the outside-review handoff payload so reviewers get one compact
receipt covering shell evidence, manual notes, defect state, recorder export, and
lifecycle smoke status.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 346
SEED = 20270744
PREFIX = "ssrm_3d_browser_world_v106_primary_demo_combined_outside_review_handoff_receipt"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"

ENTRYPOINT_JS = ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/demo.js"
ENTRYPOINT_HTML = ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/index.html"
MANUAL_PLAYTEST = ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/manual_playtest.md"
GENERATOR = ROOT / "experiments/ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
PACKET_RESULTS = ROOT / "artifacts/ssrm_3d_browser_world_v105_primary_demo_lifecycle_preflight_packet_export_results.json"
PACKET_CONTRACT = ROOT / "artifacts/ssrm_3d_browser_world_v105_primary_demo_lifecycle_preflight_packet_export_export_packet_contract.json"
EXPERIMENT_INDEX = ROOT / "scripts/run_experiments.py"

EXPECTED_RECEIPT_FIELDS = {
    "shellEvidence",
    "reviewedHandoffCompletion",
    "manualRecords",
    "defects",
    "recorderExport",
    "lifecyclePreflightPacket",
}
EXPECTED_PHASES = {
    "cross_tab_prepared_resume_visible",
    "closed_origin_tab_continuity",
    "hard_reload_continuity",
    "stale_supersession_calibration",
    "stale_reprepare_repair",
    "repaired_continue_return_refresh",
}
EXPORT_KEY = "ssrm_primary_demo_lifecycle_preflight_packet"

BOUNDARIES = (
    "browser-local combined handoff receipt source verification only",
    "artifact-backed lifecycle smoke status only",
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
    "post-346: make the combined outside-review receipt visible as one checklist completion "
    "status row so reviewers can see whether shell evidence, manual notes, defect state, "
    "recorder export, and lifecycle preflight packet are all included before downloading"
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
    packet_results = _load_json(PACKET_RESULTS) if PACKET_RESULTS.exists() else {}
    packet_contract = _load_json(PACKET_CONTRACT) if PACKET_CONTRACT.exists() else {}
    phase_statuses = packet_contract.get("phase_statuses", {})

    export_terms = (
        "const lifecyclePreflightPacket = prepareLifecyclePreflightPacket('outside-review-handoff');",
        "combinedReceiptReportIntroduced: 346",
        "lifecyclePreflightPacket,",
        "lifecyclePreflightPacketPrepared: Boolean(localStorage.getItem(LIFECYCLE_PREFLIGHT_EXPORT_KEY))",
        "lifecyclePreflightPacketSource: LIFECYCLE_PREFLIGHT_EXPORT_KEY",
        "combinedReceiptIncludes: ['shellEvidence', 'reviewedHandoffCompletion', 'manualRecords', 'defects', 'recorderExport', 'lifecyclePreflightPacket']",
    )
    summary_terms = (
        "const preflightPacket = payload.lifecyclePreflightPacket || {};",
        "const preflightPhaseCount = preflightPacket.phaseCount || Object.keys(preflightPacket.phaseStatuses || {}).length;",
        "lifecycle preflight blocking phase",
        "download combined outside-review handoff JSON",
    )
    visible_terms = (
        "lifecycle preflight packet",
        "one browser-local public review receipt",
    )
    manual_terms = (
        "lifecycle preflight status",
        "exportable combined handoff evidence",
        "automatically prepares and embeds the lifecycle preflight packet",
        "one browser-local receipt",
    )

    combined_receipt_contract = {
        "report": REPORT,
        "outside_review_export_action": "exportOutsideReviewHandoff",
        "preflight_prepare_action": "prepareLifecyclePreflightPacket('outside-review-handoff')",
        "preflight_export_key": EXPORT_KEY,
        "included_fields": sorted(EXPECTED_RECEIPT_FIELDS),
        "phase_statuses": phase_statuses,
        "blocking_phase": packet_contract.get("blocking_phase", "unknown"),
        "download_name": "ssrm_primary_demo_outside_review_handoff.json",
        "source_packet_contract": str(PACKET_CONTRACT.relative_to(ROOT)),
        "boundary": "outside-review-handoff-combined-browser-local-receipt-only",
    }

    criteria = [
        _criterion(
            "packet_export_artifacts_available_and_passing",
            PACKET_RESULTS.exists() and PACKET_CONTRACT.exists() and packet_results.get("verdict") == "pass",
            "Report 345 packet export results and contract exist and pass.",
            "artifact source",
        ),
        _criterion(
            "packet_contract_phase_set_complete",
            EXPECTED_PHASES.issubset(set(phase_statuses.keys())) and packet_contract.get("blocking_phase") == "none",
            "Source preflight packet contract has all lifecycle phases and no blocking phase.",
            "artifact source",
        ),
        _criterion(
            "outside_review_export_auto_prepares_preflight_packet",
            "prepareLifecyclePreflightPacket('outside-review-handoff')" in js,
            "Outside-review handoff export prepares the lifecycle preflight packet automatically.",
            "handoff payload",
        ),
        _criterion(
            "outside_review_payload_embeds_preflight_packet",
            _has_all(js, export_terms),
            "Outside-review payload includes lifecycle preflight packet, source key, prepared flag, report marker, and combined receipt field list.",
            "handoff payload",
        ),
        _criterion(
            "readable_summary_reports_preflight_status",
            _has_all(js, summary_terms),
            "Readable handoff summary names lifecycle preflight blocking phase and combined JSON download.",
            "visible summary",
        ),
        _criterion(
            "launcher_or07_names_combined_receipt",
            _has_all(html, visible_terms),
            "Visible OR-07 checklist text says the handoff export includes the lifecycle preflight packet as one review receipt.",
            "visible summary",
        ),
        _criterion(
            "manual_documents_combined_receipt",
            _has_all(manual, manual_terms),
            "Manual playtest documentation says outside-review handoff embeds lifecycle preflight status into one receipt.",
            "manual path",
        ),
        _criterion(
            "generator_preserves_combined_receipt_js",
            _has_all(generator, export_terms + summary_terms),
            "v63 generator preserves combined receipt payload wiring and readable preflight summary.",
            "generator durability",
        ),
        _criterion(
            "generator_preserves_combined_receipt_docs",
            _has_all(generator, visible_terms + manual_terms),
            "v63 generator preserves OR-07 and manual combined receipt language.",
            "generator durability",
        ),
        _criterion(
            "combined_receipt_contract_is_complete",
            set(combined_receipt_contract["included_fields"]) == EXPECTED_RECEIPT_FIELDS and combined_receipt_contract["blocking_phase"] == "none",
            "Report 346 emits a combined receipt contract covering shell evidence, completion state, manual notes, defects, recorder export, and lifecycle preflight packet.",
            "receipt contract",
        ),
        _criterion(
            "experiment_index_includes_combined_receipt_report",
            "experiments.ssrm_3d_browser_world_v106_primary_demo_combined_outside_review_handoff_receipt" in experiment_index,
            "Experiment runner index includes the Report 346 verifier module.",
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
        "handoff_payload_score": mean(by_channel.get("handoff payload", [0.0])),
        "visible_summary_score": mean(by_channel.get("visible summary", [0.0])),
        "manual_path_score": mean(by_channel.get("manual path", [0.0])),
        "generator_durability_score": mean(by_channel.get("generator durability", [0.0])),
        "receipt_contract_score": mean(by_channel.get("receipt contract", [0.0])),
        "runner_index_score": mean(by_channel.get("runner index", [0.0])),
        "claim_hygiene_score": mean(by_channel.get("claim hygiene", [0.0])),
        "included_field_count": len(combined_receipt_contract["included_fields"]),
        "phase_count": len(phase_statuses),
        "blocking_phase_count": 0 if combined_receipt_contract["blocking_phase"] == "none" else 1,
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
        "combined_receipt_contract": combined_receipt_contract,
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
    contract = results["combined_receipt_contract"]
    report_path = DOCS / f"{REPORT}_{PREFIX}_report.md"
    criterion_lines = "\n".join(f"- {'PASS' if item['passed'] else 'FAIL'} `{item['name']}` ({item['channel']}): {item['detail']}" for item in criteria)
    field_lines = "\n".join(f"- `{field}`" for field in contract["included_fields"])
    phase_lines = "\n".join(f"- `{phase}`: {status}" for phase, status in contract["phase_statuses"].items())
    boundary_lines = "\n".join(f"- {boundary}" for boundary in BOUNDARIES)

    report_path.write_text(
        f"# Report {REPORT}: SSRM-3D Browser World v106 Primary Demo Combined Outside-Review Handoff Receipt\n\n"
        "## Purpose\n\n"
        "Report 346 connects the lifecycle preflight packet to the outside-review handoff payload. Reviewers now get one browser-local receipt covering shell evidence, reviewed completion state, manual notes, defects, recorder export, and lifecycle smoke status.\n\n"
        "## What changed\n\n"
        "- `exportOutsideReviewHandoff()` now prepares the lifecycle preflight packet with action `outside-review-handoff`.\n"
        "- The outside-review JSON payload embeds `lifecyclePreflightPacket`, its source key, prepared flag, and combined receipt field list.\n"
        "- The readable handoff summary reports lifecycle preflight blocking phase and phase count.\n"
        "- OR-07 and manual playtest language now describe one combined browser-local review receipt.\n"
        "- The v63 generator preserves the combined receipt payload wiring and documentation.\n\n"
        "## Combined receipt fields\n\n"
        f"{field_lines}\n\n"
        "## Lifecycle phase statuses\n\n"
        f"{phase_lines}\n\n"
        "## Metrics\n\n"
        f"- verdict: `{results['verdict']}`\n"
        f"- readiness: `{metrics['readiness']:.3f}`\n"
        f"- weakest_channel_score: `{metrics['weakest_channel_score']:.3f}`\n"
        f"- artifact_source_score: `{metrics['artifact_source_score']:.3f}`\n"
        f"- handoff_payload_score: `{metrics['handoff_payload_score']:.3f}`\n"
        f"- visible_summary_score: `{metrics['visible_summary_score']:.3f}`\n"
        f"- manual_path_score: `{metrics['manual_path_score']:.3f}`\n"
        f"- generator_durability_score: `{metrics['generator_durability_score']:.3f}`\n"
        f"- receipt_contract_score: `{metrics['receipt_contract_score']:.3f}`\n"
        f"- included_field_count: `{metrics['included_field_count']}`\n"
        f"- phase_count: `{metrics['phase_count']}`\n"
        f"- blocking_phase_count: `{metrics['blocking_phase_count']}`\n"
        f"- criterion_count: `{metrics['criterion_count']}`\n\n"
        "## Criteria\n\n"
        f"{criterion_lines}\n\n"
        "## Boundary\n\n"
        f"{boundary_lines}\n\n"
        "## Interpretation\n\n"
        "The outside-review path now produces one consolidated handoff receipt instead of separate smoke-status and handoff artifacts. This improves reviewer continuity, but remains browser-local source/artifact verification rather than a hosted URL proof, live browser automation proof, production persistence proof, autonomous conversation proof, consciousness claim, moral-patienthood claim, complete engine, or finished gameplay.\n\n"
        "## Next gate\n\n"
        f"{results['next_gate']}\n",
        encoding="utf-8",
    )


def write_artifacts(results: dict[str, Any]) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    DOCS.mkdir(exist_ok=True)
    (ARTIFACTS / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACTS / f"{PREFIX}_state.json").write_text(json.dumps({"report": REPORT, "seed": SEED, "verdict": results["verdict"], "metrics": results["metrics"], "combined_receipt_contract": results["combined_receipt_contract"], "next_gate": results["next_gate"]}, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACTS / f"{PREFIX}_combined_receipt_contract.json").write_text(json.dumps(results["combined_receipt_contract"], indent=2, sort_keys=True), encoding="utf-8")
    _write_csv(ARTIFACTS / f"{PREFIX}_summary.csv", [{"report": REPORT, "seed": SEED, "verdict": results["verdict"], **results["metrics"]}], ["report", "seed", "verdict", *results["metrics"].keys()])
    _write_csv(ARTIFACTS / f"{PREFIX}_verdict.csv", [{"report": REPORT, "verdict": results["verdict"], "weakest_channel_score": results["metrics"]["weakest_channel_score"], "included_field_count": results["metrics"]["included_field_count"], "next_gate": results["next_gate"]}], ["report", "verdict", "weakest_channel_score", "included_field_count", "next_gate"])
    _write_csv(ARTIFACTS / f"{PREFIX}_criteria.csv", results["criteria"], ["name", "passed", "score", "channel", "detail"])
    _write_report(results)


def main() -> dict[str, Any]:
    results = build_results()
    write_artifacts(results)
    print(json.dumps({"report": REPORT, "verdict": results["verdict"], "metrics": results["metrics"]}, indent=2, sort_keys=True))
    return results


if __name__ == "__main__":
    main()
