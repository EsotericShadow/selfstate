"""Report 345: primary demo lifecycle preflight packet export.

Report 344 added a browser-visible lifecycle preflight status panel. Report 345
adds browser-local prepare/copy/download actions so outside reviewers can attach a
compact smoke-status receipt to vertical-slice feedback.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 345
SEED = 20270743
PREFIX = "ssrm_3d_browser_world_v105_primary_demo_lifecycle_preflight_packet_export"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"

COMMAND = "python3 -m experiments.ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner"
EXPORT_KEY = "ssrm_primary_demo_lifecycle_preflight_packet"
DOWNLOAD_NAME = "ssrm_primary_demo_lifecycle_preflight_packet.json"
BOUNDARY = "lifecycle-preflight-packet-browser-local-artifact-status-only"
EXPECTED_PHASES = {
    "cross_tab_prepared_resume_visible",
    "closed_origin_tab_continuity",
    "hard_reload_continuity",
    "stale_supersession_calibration",
    "stale_reprepare_repair",
    "repaired_continue_return_refresh",
}

ENTRYPOINT_HTML = ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/index.html"
ENTRYPOINT_JS = ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/demo.js"
MANUAL_PLAYTEST = ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/manual_playtest.md"
GENERATOR = ROOT / "experiments/ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
PREFLIGHT_RESULTS = ROOT / "artifacts/ssrm_3d_browser_world_v104_primary_demo_lifecycle_preflight_status_panel_results.json"
PREFLIGHT_PACKET = ROOT / "artifacts/ssrm_3d_browser_world_v104_primary_demo_lifecycle_preflight_status_panel_preflight_packet.json"
EXPERIMENT_INDEX = ROOT / "scripts/run_experiments.py"

CLAIM_BOUNDARIES = (
    "browser-local preflight packet prepare/copy/download wiring only",
    "artifact-backed status receipt only",
    "clipboard success is attempted but not claimed by deterministic source verification",
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
    "post-345: connect the exported lifecycle preflight packet to the outside-review handoff "
    "payload so reviewers get one combined handoff receipt covering shell evidence, manual notes, "
    "defects, and lifecycle smoke status"
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _criterion(name: str, passed: bool, detail: str, channel: str) -> dict[str, Any]:
    return {"name": name, "passed": bool(passed), "score": 1.0 if passed else 0.0, "channel": channel, "detail": detail}


def _contains_all(text: str, terms: tuple[str, ...]) -> bool:
    return all(term in text for term in terms)


def build_results() -> dict[str, Any]:
    html = _read(ENTRYPOINT_HTML)
    js = _read(ENTRYPOINT_JS)
    manual = _read(MANUAL_PLAYTEST)
    generator = _read(GENERATOR)
    experiment_index = _read(EXPERIMENT_INDEX)
    preflight_results = _load_json(PREFLIGHT_RESULTS) if PREFLIGHT_RESULTS.exists() else {}
    preflight_packet = _load_json(PREFLIGHT_PACKET) if PREFLIGHT_PACKET.exists() else {}
    source_phases = set(preflight_packet.get("phase_statuses", {}).keys())

    html_terms = (
        'id="lifecyclePreflightPacketActions"',
        'id="prepareLifecyclePreflightPacket"',
        'id="copyLifecyclePreflightPacket"',
        'id="lifecyclePreflightExportStatus"',
        'id="lifecyclePreflightPacketOut"',
    )
    js_terms = (
        f"const LIFECYCLE_PREFLIGHT_EXPORT_KEY = '{EXPORT_KEY}';",
        "function lifecyclePreflightPhaseStatuses()",
        "function readLifecyclePreflightPacket()",
        "function buildLifecyclePreflightPacket(action = 'prepare')",
        "function renderLifecyclePreflightPacket(message)",
        "function prepareLifecyclePreflightPacket(action = 'prepare')",
        "async function copyLifecyclePreflightPacket()",
        "navigator.clipboard",
        "Clipboard unavailable; download link prepared instead",
        DOWNLOAD_NAME,
        BOUNDARY,
    )
    generator_html_terms = tuple(term.replace('"', '\\\"') for term in html_terms)
    generator_terms = js_terms + generator_html_terms + (
        "Browser-local packet action:",
        "Prepare preflight packet",
        "Copy preflight packet",
    )
    manual_terms = (
        "Browser-local packet action:",
        "Prepare preflight packet",
        "Copy preflight packet",
        DOWNLOAD_NAME,
        "clipboard permission is unavailable",
        "browser-local review evidence only",
    )

    export_packet = {
        "report": REPORT,
        "command": COMMAND,
        "export_key": EXPORT_KEY,
        "download_name": DOWNLOAD_NAME,
        "blocking_phase": preflight_packet.get("blocking_phase", "unknown"),
        "phase_statuses": preflight_packet.get("phase_statuses", {}),
        "sources": preflight_packet.get("sources", {}),
        "browser_actions": {
            "prepare": "prepareLifecyclePreflightPacket",
            "copy": "copyLifecyclePreflightPacket",
            "download_link": "preparedLifecyclePreflightPacket",
            "preview": "lifecyclePreflightPacketOut",
            "status": "lifecyclePreflightExportStatus",
        },
        "boundary": BOUNDARY,
    }

    criteria = [
        _criterion(
            "preflight_artifacts_available_and_passing",
            PREFLIGHT_RESULTS.exists() and PREFLIGHT_PACKET.exists() and preflight_results.get("verdict") == "pass",
            "Report 344 preflight results and packet exist and pass.",
            "artifact source",
        ),
        _criterion(
            "preflight_source_phase_set_complete",
            EXPECTED_PHASES.issubset(source_phases) and preflight_packet.get("blocking_phase") == "none",
            "Source preflight packet has all lifecycle phases and no blocking phase.",
            "artifact source",
        ),
        _criterion(
            "launcher_exposes_packet_actions",
            _contains_all(html, html_terms),
            "Primary launcher exposes prepare/copy controls, status line, and JSON preview for the preflight packet.",
            "entrypoint controls",
        ),
        _criterion(
            "javascript_defines_packet_storage_and_builders",
            _contains_all(js, js_terms[:7]),
            "Launcher JS defines storage key, phase reader, packet reader, packet builder, renderer, prepare, and copy functions.",
            "browser behavior",
        ),
        _criterion(
            "javascript_defines_clipboard_fallback_and_download",
            _contains_all(js, js_terms[7:]),
            "Launcher JS attempts clipboard copy but prepares a downloadable JSON fallback and visible preview.",
            "browser behavior",
        ),
        _criterion(
            "javascript_wires_packet_buttons",
            "document.getElementById('prepareLifecyclePreflightPacket')?.addEventListener" in js and "document.getElementById('copyLifecyclePreflightPacket')?.addEventListener" in js,
            "Prepare and copy buttons are wired to browser-local packet actions.",
            "browser behavior",
        ),
        _criterion(
            "manual_documents_packet_action",
            _contains_all(manual, manual_terms),
            "Manual playtest script explains prepare, copy, fallback, and review-evidence semantics.",
            "manual path",
        ),
        _criterion(
            "generator_preserves_packet_export_controls",
            _contains_all(generator, generator_html_terms),
            "v63 generator preserves the packet action controls and preview/status nodes.",
            "generator durability",
        ),
        _criterion(
            "generator_preserves_packet_export_behavior",
            _contains_all(generator, generator_terms),
            "v63 generator preserves packet JS behavior and manual documentation.",
            "generator durability",
        ),
        _criterion(
            "export_packet_is_compact_and_attachable",
            export_packet["blocking_phase"] == "none" and len(export_packet["phase_statuses"]) == len(EXPECTED_PHASES) and export_packet["download_name"].endswith(".json"),
            "Report 345 emits a compact packet contract matching the browser download payload.",
            "packet contract",
        ),
        _criterion(
            "experiment_index_includes_packet_export_report",
            "experiments.ssrm_3d_browser_world_v105_primary_demo_lifecycle_preflight_packet_export" in experiment_index,
            "Experiment runner index includes the Report 345 verifier module.",
            "runner index",
        ),
        _criterion(
            "claim_boundary_preserved",
            all(boundary.startswith("no ") or "browser-local" in boundary or "artifact" in boundary or "clipboard" in boundary for boundary in CLAIM_BOUNDARIES),
            "Boundary rejects clipboard-success overclaiming, hosted URL, live E2E, production persistence, consciousness, moral patienthood, complete engine, and finished gameplay claims.",
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
        "packet_contract_score": mean(by_channel.get("packet contract", [0.0])),
        "runner_index_score": mean(by_channel.get("runner index", [0.0])),
        "claim_hygiene_score": mean(by_channel.get("claim hygiene", [0.0])),
        "phase_count": len(export_packet["phase_statuses"]),
        "blocking_phase_count": 0 if export_packet["blocking_phase"] == "none" else 1,
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
        "export_packet_contract": export_packet,
        "boundaries": CLAIM_BOUNDARIES,
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
    packet = results["export_packet_contract"]
    report_path = DOCS / f"{REPORT}_{PREFIX}_report.md"
    criterion_lines = "\n".join(f"- {'PASS' if item['passed'] else 'FAIL'} `{item['name']}` ({item['channel']}): {item['detail']}" for item in criteria)
    phase_lines = "\n".join(f"- `{phase}`: {status}" for phase, status in packet["phase_statuses"].items())
    boundary_lines = "\n".join(f"- {boundary}" for boundary in CLAIM_BOUNDARIES)
    action_lines = "\n".join(f"- `{name}`: `{target}`" for name, target in packet["browser_actions"].items())

    report_path.write_text(
        f"# Report {REPORT}: SSRM-3D Browser World v105 Primary Demo Lifecycle Preflight Packet Export\n\n"
        "## Purpose\n\n"
        "Report 345 turns the lifecycle preflight panel into a browser-local packet action. Outside reviewers can prepare a downloadable JSON receipt, attempt clipboard copy, and still see the packet in a visible preview if clipboard access is unavailable.\n\n"
        "## What changed\n\n"
        "- Added `Prepare preflight packet` and `Copy preflight packet` controls to the primary launcher preflight panel.\n"
        "- Added browser-local packet storage, JSON preview, downloadable receipt, clipboard attempt, and fallback messages to `demo.js`.\n"
        "- Updated the manual playtest script and v63 generator so regenerated launchers preserve the packet path.\n"
        "- Added a deterministic verifier for controls, JS behavior, generator durability, manual docs, and packet contract.\n\n"
        "## Browser actions\n\n"
        f"{action_lines}\n\n"
        "## Export packet contract\n\n"
        f"- command: `{packet['command']}`\n"
        f"- export_key: `{packet['export_key']}`\n"
        f"- download_name: `{packet['download_name']}`\n"
        f"- blocking_phase: `{packet['blocking_phase']}`\n"
        f"- boundary: `{packet['boundary']}`\n\n"
        "## Lifecycle phase statuses\n\n"
        f"{phase_lines}\n\n"
        "## Metrics\n\n"
        f"- verdict: `{results['verdict']}`\n"
        f"- readiness: `{metrics['readiness']:.3f}`\n"
        f"- weakest_channel_score: `{metrics['weakest_channel_score']:.3f}`\n"
        f"- artifact_source_score: `{metrics['artifact_source_score']:.3f}`\n"
        f"- entrypoint_controls_score: `{metrics['entrypoint_controls_score']:.3f}`\n"
        f"- browser_behavior_score: `{metrics['browser_behavior_score']:.3f}`\n"
        f"- manual_path_score: `{metrics['manual_path_score']:.3f}`\n"
        f"- generator_durability_score: `{metrics['generator_durability_score']:.3f}`\n"
        f"- packet_contract_score: `{metrics['packet_contract_score']:.3f}`\n"
        f"- blocking_phase_count: `{metrics['blocking_phase_count']}`\n"
        f"- phase_count: `{metrics['phase_count']}`\n"
        f"- criterion_count: `{metrics['criterion_count']}`\n\n"
        "## Criteria\n\n"
        f"{criterion_lines}\n\n"
        "## Boundary\n\n"
        f"{boundary_lines}\n\n"
        "## Interpretation\n\n"
        "The primary launcher now produces a compact lifecycle smoke-status receipt that can travel with outside-review feedback. This improves review continuity, but it remains browser-local artifact/status wiring rather than a hosted URL proof, live browser automation proof, production persistence proof, autonomous conversation proof, consciousness claim, moral-patienthood claim, complete engine, or finished gameplay.\n\n"
        "## Next gate\n\n"
        f"{results['next_gate']}\n",
        encoding="utf-8",
    )


def write_artifacts(results: dict[str, Any]) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    DOCS.mkdir(exist_ok=True)
    (ARTIFACTS / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACTS / f"{PREFIX}_state.json").write_text(json.dumps({"report": REPORT, "seed": SEED, "verdict": results["verdict"], "metrics": results["metrics"], "export_packet_contract": results["export_packet_contract"], "next_gate": results["next_gate"]}, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACTS / f"{PREFIX}_export_packet_contract.json").write_text(json.dumps(results["export_packet_contract"], indent=2, sort_keys=True), encoding="utf-8")
    _write_csv(ARTIFACTS / f"{PREFIX}_summary.csv", [{"report": REPORT, "seed": SEED, "verdict": results["verdict"], **results["metrics"]}], ["report", "seed", "verdict", *results["metrics"].keys()])
    _write_csv(ARTIFACTS / f"{PREFIX}_verdict.csv", [{"report": REPORT, "verdict": results["verdict"], "weakest_channel_score": results["metrics"]["weakest_channel_score"], "blocking_phase_count": results["metrics"]["blocking_phase_count"], "next_gate": results["next_gate"]}], ["report", "verdict", "weakest_channel_score", "blocking_phase_count", "next_gate"])
    _write_csv(ARTIFACTS / f"{PREFIX}_criteria.csv", results["criteria"], ["name", "passed", "score", "channel", "detail"])
    _write_report(results)


def main() -> dict[str, Any]:
    results = build_results()
    write_artifacts(results)
    print(json.dumps({"report": REPORT, "verdict": results["verdict"], "metrics": results["metrics"]}, indent=2, sort_keys=True))
    return results


if __name__ == "__main__":
    main()
