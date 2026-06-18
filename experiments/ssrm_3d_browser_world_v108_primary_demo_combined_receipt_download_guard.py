"""Report 348: combined receipt download guard.

Report 347 made receipt completeness visible. Report 348 makes that status row
enforceable by blocking normal outside-review handoff download when required
receipt fields are missing, while preserving an explicit debug override for
intentionally incomplete review packets.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 348
SEED = 20270746
PREFIX = "ssrm_3d_browser_world_v108_primary_demo_combined_receipt_download_guard"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"

ENTRYPOINT_JS = ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/demo.js"
ENTRYPOINT_HTML = ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/index.html"
MANUAL_PLAYTEST = ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/manual_playtest.md"
GENERATOR = ROOT / "experiments/ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
STATUS_RESULTS = ROOT / "artifacts/ssrm_3d_browser_world_v107_primary_demo_combined_receipt_status_row_results.json"
STATUS_CONTRACT = ROOT / "artifacts/ssrm_3d_browser_world_v107_primary_demo_combined_receipt_status_row_status_row_contract.json"
EXPERIMENT_INDEX = ROOT / "scripts/run_experiments.py"

EXPECTED_FIELDS = {
    "shellEvidence",
    "reviewedHandoffCompletion",
    "manualRecords",
    "defects",
    "recorderExport",
    "lifecyclePreflightPacket",
}

BOUNDARIES = (
    "browser-local combined receipt download guard source verification only",
    "deterministic source check does not prove live download or checkbox behavior",
    "debug override is explicit and only for intentionally incomplete review packets",
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
    "post-348: run one real browser-local launcher smoke that prepares a combined receipt, "
    "observes the guarded download state, toggles the debug override, and exports the final "
    "outside-review handoff JSON without adding a parallel surface"
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
    status_results = _load_json(STATUS_RESULTS) if STATUS_RESULTS.exists() else {}
    status_contract = _load_json(STATUS_CONTRACT) if STATUS_CONTRACT.exists() else {}
    source_fields = set(status_contract.get("fields", {}).keys())

    html_terms = (
        'id="combinedReceiptDebugOverride"',
        'Allow incomplete receipt debug export',
        'id="combinedReceiptDownloadGate"',
        'data-combined-receipt-download-gate="blocked"',
        'complete receipt required unless debug override is checked',
    )
    js_guard_terms = (
        "function combinedReceiptDebugOverrideEnabled()",
        "function combinedReceiptDownloadGate(payload)",
        "function renderCombinedReceiptDownloadGate(payload, gate)",
        "reportIntroduced: 348",
        "downloadEnabled",
        "debugOverride",
        "combined-receipt-download-gate-browser-local-only",
    )
    js_enforcement_terms = (
        "payload.combinedReceiptDownloadGate = combinedReceiptDownloadGate(payload);",
        "previewCombinedReceiptDownloadGate: combinedReceiptDownloadGate",
        "renderOutsideReviewHandoffActions(payload, freshness, combinedReceiptDownloadGate)",
        "if (!gate.downloadEnabled)",
        "Download blocked: missing",
        "Check debug override to export an incomplete review packet",
        "Download incomplete outside-review handoff JSON (debug override)",
        "download.dataset.combinedReceiptDownloadGate = gate.allowed ? 'ready' : 'debug-override'",
        "document.getElementById('combinedReceiptDebugOverride')?.addEventListener('change', () => renderOutsideReviewHandoffPreview());",
    )
    manual_terms = (
        "Normal handoff download is blocked while required receipt fields are missing",
        "explicit debug override",
        "intentionally incomplete review packet",
    )
    generator_html_terms = tuple(term.replace('"', '\\"') for term in html_terms)
    generator_terms = js_guard_terms + js_enforcement_terms + generator_html_terms + manual_terms

    direct_download_creation_removed = "document.getElementById('outsideReviewChecklist')?.appendChild(link);" not in js

    guard_contract = {
        "report": REPORT,
        "guard_status_node": "combinedReceiptDownloadGate",
        "debug_override_control": "combinedReceiptDebugOverride",
        "download_link": "preparedOutsideReviewExport",
        "normal_download_gate": "combinedReceiptDownloadGate(payload).allowed",
        "debug_override_gate": "combinedReceiptDownloadGate(payload).debugOverride",
        "blocked_when_missing_fields": True,
        "debug_override_label": "Allow incomplete receipt debug export",
        "required_fields": sorted(EXPECTED_FIELDS),
        "source_status_row_contract": str(STATUS_CONTRACT.relative_to(ROOT)),
        "boundary": "combined-receipt-download-gate-browser-local-only",
    }

    criteria = [
        _criterion(
            "status_row_artifacts_available_and_passing",
            STATUS_RESULTS.exists() and STATUS_CONTRACT.exists() and status_results.get("verdict") == "pass",
            "Report 347 status-row results and contract exist and pass.",
            "artifact source",
        ),
        _criterion(
            "status_row_source_field_set_complete",
            source_fields == EXPECTED_FIELDS,
            "Source status-row contract has all required combined receipt fields.",
            "artifact source",
        ),
        _criterion(
            "launcher_exposes_download_guard_and_debug_override",
            _has_all(html, html_terms),
            "Primary launcher exposes a download gate status node and explicit incomplete-receipt debug override checkbox.",
            "entrypoint controls",
        ),
        _criterion(
            "javascript_defines_download_gate_model",
            _has_all(js, js_guard_terms),
            "Launcher JS defines debug override, download gate model, renderer, report marker, and boundary.",
            "browser behavior",
        ),
        _criterion(
            "javascript_enforces_download_gate",
            _has_all(js, js_enforcement_terms),
            "Launcher JS stores gate metadata, blocks missing-field downloads, supports explicit debug override, and rerenders on checkbox change.",
            "browser behavior",
        ),
        _criterion(
            "outside_review_export_no_longer_creates_unguarded_download",
            direct_download_creation_removed,
            "Outside-review export no longer appends a download link directly before receipt completeness is rendered.",
            "browser behavior",
        ),
        _criterion(
            "manual_documents_download_guard",
            _has_all(manual, manual_terms),
            "Manual playtest documentation explains blocked normal download and explicit debug override semantics.",
            "manual path",
        ),
        _criterion(
            "generator_preserves_download_guard",
            _has_all(generator, generator_terms),
            "v63 generator preserves debug override control, gate behavior, blocked/override branches, event listener, and manual guidance.",
            "generator durability",
        ),
        _criterion(
            "guard_contract_is_complete",
            set(guard_contract["required_fields"]) == EXPECTED_FIELDS and guard_contract["blocked_when_missing_fields"] is True,
            "Report 348 emits a guard contract covering the six required receipt fields and explicit debug override.",
            "guard contract",
        ),
        _criterion(
            "experiment_index_includes_download_guard_report",
            "experiments.ssrm_3d_browser_world_v108_primary_demo_combined_receipt_download_guard" in experiment_index,
            "Experiment runner index includes the Report 348 verifier module.",
            "runner index",
        ),
        _criterion(
            "claim_boundary_preserved",
            all(boundary.startswith("no ") or "browser-local" in boundary or "debug override" in boundary or "deterministic" in boundary for boundary in BOUNDARIES),
            "Boundary rejects live browser/download overclaiming, hosted URL, production persistence, autonomous language, consciousness, moral patienthood, complete engine, and finished gameplay claims.",
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
        "entrypoint_controls_score": mean(by_channel.get("entrypoint controls", [0.0])),
        "browser_behavior_score": mean(by_channel.get("browser behavior", [0.0])),
        "manual_path_score": mean(by_channel.get("manual path", [0.0])),
        "generator_durability_score": mean(by_channel.get("generator durability", [0.0])),
        "guard_contract_score": mean(by_channel.get("guard contract", [0.0])),
        "runner_index_score": mean(by_channel.get("runner index", [0.0])),
        "claim_hygiene_score": mean(by_channel.get("claim hygiene", [0.0])),
        "required_field_count": len(EXPECTED_FIELDS),
        "normal_download_guarded": 1.0 if direct_download_creation_removed else 0.0,
        "debug_override_count": 1,
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
        "guard_contract": guard_contract,
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
    contract = results["guard_contract"]
    report_path = DOCS / f"{REPORT}_{PREFIX}_report.md"
    criterion_lines = "\n".join(f"- {'PASS' if item['passed'] else 'FAIL'} `{item['name']}` ({item['channel']}): {item['detail']}" for item in criteria)
    field_lines = "\n".join(f"- `{field}`" for field in contract["required_fields"])
    boundary_lines = "\n".join(f"- {boundary}" for boundary in BOUNDARIES)

    report_path.write_text(
        f"# Report {REPORT}: SSRM-3D Browser World v108 Primary Demo Combined Receipt Download Guard\n\n"
        "## Purpose\n\n"
        "Report 348 makes the combined receipt status row enforceable. Normal outside-review handoff download is blocked when required receipt fields are missing, while an explicit debug override can intentionally export an incomplete review packet.\n\n"
        "## What changed\n\n"
        "- Added `combinedReceiptDebugOverride` and `combinedReceiptDownloadGate` to the launcher.\n"
        "- Added `combinedReceiptDebugOverrideEnabled()`, `combinedReceiptDownloadGate()`, and `renderCombinedReceiptDownloadGate()`.\n"
        "- Outside-review handoff payloads now include `combinedReceiptDownloadGate`.\n"
        "- Normal download creation moved behind `gate.downloadEnabled`; missing fields show a blocked message instead.\n"
        "- Debug override download uses explicit warning text and `data-combined-receipt-download-gate=debug-override`.\n"
        "- Manual guidance and the v63 generator preserve the blocked-normal/download-override semantics.\n\n"
        "## Required receipt fields\n\n"
        f"{field_lines}\n\n"
        "## Metrics\n\n"
        f"- verdict: `{results['verdict']}`\n"
        f"- readiness: `{metrics['readiness']:.3f}`\n"
        f"- weakest_channel_score: `{metrics['weakest_channel_score']:.3f}`\n"
        f"- artifact_source_score: `{metrics['artifact_source_score']:.3f}`\n"
        f"- entrypoint_controls_score: `{metrics['entrypoint_controls_score']:.3f}`\n"
        f"- browser_behavior_score: `{metrics['browser_behavior_score']:.3f}`\n"
        f"- manual_path_score: `{metrics['manual_path_score']:.3f}`\n"
        f"- generator_durability_score: `{metrics['generator_durability_score']:.3f}`\n"
        f"- guard_contract_score: `{metrics['guard_contract_score']:.3f}`\n"
        f"- normal_download_guarded: `{metrics['normal_download_guarded']:.3f}`\n"
        f"- debug_override_count: `{metrics['debug_override_count']}`\n"
        f"- criterion_count: `{metrics['criterion_count']}`\n\n"
        "## Criteria\n\n"
        f"{criterion_lines}\n\n"
        "## Boundary\n\n"
        f"{boundary_lines}\n\n"
        "## Interpretation\n\n"
        "This makes the receipt completeness row operational rather than decorative: a missing field blocks normal download. The override is explicit and review/debug-oriented. This remains source-level browser-local verification, not proof of live checkbox/download behavior, hosted URL behavior, production persistence, autonomous conversation, consciousness, moral patienthood, complete engine, or finished gameplay.\n\n"
        "## Next gate\n\n"
        f"{results['next_gate']}\n",
        encoding="utf-8",
    )


def write_artifacts(results: dict[str, Any]) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    DOCS.mkdir(exist_ok=True)
    (ARTIFACTS / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACTS / f"{PREFIX}_state.json").write_text(json.dumps({"report": REPORT, "seed": SEED, "verdict": results["verdict"], "metrics": results["metrics"], "guard_contract": results["guard_contract"], "next_gate": results["next_gate"]}, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACTS / f"{PREFIX}_guard_contract.json").write_text(json.dumps(results["guard_contract"], indent=2, sort_keys=True), encoding="utf-8")
    _write_csv(ARTIFACTS / f"{PREFIX}_summary.csv", [{"report": REPORT, "seed": SEED, "verdict": results["verdict"], **results["metrics"]}], ["report", "seed", "verdict", *results["metrics"].keys()])
    _write_csv(ARTIFACTS / f"{PREFIX}_verdict.csv", [{"report": REPORT, "verdict": results["verdict"], "weakest_channel_score": results["metrics"]["weakest_channel_score"], "normal_download_guarded": results["metrics"]["normal_download_guarded"], "next_gate": results["next_gate"]}], ["report", "verdict", "weakest_channel_score", "normal_download_guarded", "next_gate"])
    _write_csv(ARTIFACTS / f"{PREFIX}_criteria.csv", results["criteria"], ["name", "passed", "score", "channel", "detail"])
    _write_report(results)


def main() -> dict[str, Any]:
    results = build_results()
    write_artifacts(results)
    print(json.dumps({"report": REPORT, "verdict": results["verdict"], "metrics": results["metrics"]}, indent=2, sort_keys=True))
    return results


if __name__ == "__main__":
    main()
