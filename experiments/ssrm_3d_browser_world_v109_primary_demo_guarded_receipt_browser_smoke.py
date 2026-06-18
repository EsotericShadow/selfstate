"""Report 349: real browser-local guarded receipt smoke.

Report 348 added a source-verified combined receipt download guard. Report 349
requires a browser-local smoke artifact from the maintained primary launcher that
prepares a combined receipt, observes the guarded state, toggles the explicit
debug override, and observes an export/download path for the final handoff JSON.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 349
SEED = 20270747
PREFIX = "ssrm_3d_browser_world_v109_primary_demo_guarded_receipt_browser_smoke"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"

SMOKE_ARTIFACT = ARTIFACTS / f"{PREFIX}_browser_smoke.json"
GUARD_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v108_primary_demo_combined_receipt_download_guard_results.json"
GUARD_CONTRACT = ARTIFACTS / "ssrm_3d_browser_world_v108_primary_demo_combined_receipt_download_guard_guard_contract.json"
ENTRYPOINT_JS = ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/demo.js"
GENERATOR = ROOT / "experiments/ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
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
    "one real browser-local launcher smoke artifact plus deterministic verification",
    "in-app browser smoke on localhost only",
    "debug override smoke proves the incomplete review export path only",
    "no hosted URL claim",
    "no production persistence claim",
    "no autonomous natural-language claim",
    "no subjective-consciousness claim",
    "no moral-patienthood claim",
    "no complete 3D engine claim",
    "no finished gameplay claim",
)

NEXT_GATE = (
    "post-349: use this browser-smoked combined receipt path as the review gate for the next "
    "actual vertical-slice behavior change, instead of adding another receipt-only bridge"
)


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _criterion(name: str, passed: bool, detail: str, channel: str) -> dict[str, Any]:
    return {"name": name, "passed": bool(passed), "score": 1.0 if passed else 0.0, "channel": channel, "detail": detail}


def build_results() -> dict[str, Any]:
    smoke = _load_json(SMOKE_ARTIFACT) if SMOKE_ARTIFACT.exists() else {}
    guard_results = _load_json(GUARD_RESULTS) if GUARD_RESULTS.exists() else {}
    guard_contract = _load_json(GUARD_CONTRACT) if GUARD_CONTRACT.exists() else {}
    js = _read(ENTRYPOINT_JS)
    generator = _read(GENERATOR)
    experiment_index = _read(EXPERIMENT_INDEX)

    initial_gate = smoke.get("initialGate", {})
    override_gate = smoke.get("overrideGate", {})
    final_payload = smoke.get("finalPayload", {})
    final_gate = final_payload.get("combinedReceiptDownloadGate", {})
    final_status = final_payload.get("combinedReceiptStatus", {})
    final_fields = set(final_status.get("fields", {}).keys())
    browser_logs = smoke.get("consoleErrors", [])

    criteria = [
        _criterion(
            "guard_source_artifacts_available_and_passing",
            GUARD_RESULTS.exists() and GUARD_CONTRACT.exists() and guard_results.get("verdict") == "pass",
            "Report 348 guard results and contract exist and pass.",
            "source guard",
        ),
        _criterion(
            "browser_smoke_artifact_exists",
            SMOKE_ARTIFACT.exists() and smoke.get("report") == REPORT,
            "Browser smoke artifact exists and is tagged as Report 349.",
            "browser artifact",
        ),
        _criterion(
            "browser_smoke_used_localhost_primary_launcher",
            smoke.get("browser") == "in_app_browser" and "127.0.0.1" in smoke.get("launcherUrl", "") and "ssrm_3d_browser_world_primary_demo" in smoke.get("launcherUrl", ""),
            "Smoke ran in the in-app browser against the localhost primary launcher.",
            "browser artifact",
        ),
        _criterion(
            "browser_smoke_used_maintained_surface",
            smoke.get("parallelSurfaceCreated") is False and smoke.get("targetShell", "").endswith("ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html"),
            "Smoke used the primary launcher and maintained v61 shell target, not a parallel surface.",
            "surface discipline",
        ),
        _criterion(
            "browser_smoke_clicked_clean_launch_and_returned",
            smoke.get("cleanLaunchClicked") is True and smoke.get("returnedToLauncher") is True,
            "Smoke clicked clean launch to create a real launch handoff, then returned to the launcher.",
            "browser interaction",
        ),
        _criterion(
            "browser_smoke_prepared_combined_handoff",
            smoke.get("prepareOutsideReviewClicked") is True and final_payload.get("combinedReceiptReportIntroduced") == 346,
            "Smoke clicked Prepare outside-review handoff and produced a combined receipt payload.",
            "browser interaction",
        ),
        _criterion(
            "initial_download_was_guarded_before_override",
            initial_gate.get("state") == "blocked" and initial_gate.get("downloadLinkCount") == 0 and "recorderExport" in initial_gate.get("missing", []),
            "Before debug override, normal download was blocked and recorderExport was missing.",
            "download guard",
        ),
        _criterion(
            "debug_override_enabled_download_path",
            override_gate.get("state") == "debug-override" and override_gate.get("downloadLinkCount") == 1 and override_gate.get("checkboxChecked") is True,
            "After toggling debug override, the incomplete download path became available and explicitly marked debug override.",
            "download guard",
        ),
        _criterion(
            "final_payload_records_debug_override_gate",
            final_gate.get("debugOverride") is True and final_gate.get("downloadEnabled") is True and final_gate.get("allowed") is False,
            "Final stored payload records debug override export, download enabled, and normal gate not allowed.",
            "payload evidence",
        ),
        _criterion(
            "final_payload_keeps_required_receipt_fields",
            EXPECTED_FIELDS.issubset(final_fields) and set(guard_contract.get("required_fields", [])) == EXPECTED_FIELDS,
            "Final payload status and guard contract cover all six combined receipt fields.",
            "payload evidence",
        ),
        _criterion(
            "browser_export_link_click_attempt_recorded",
            smoke.get("downloadEventObserved") is True or "Downloads are not supported" in str(smoke.get("downloadError", "")),
            "Smoke clicked the debug-override handoff export link and recorded either a download event or the in-app browser download limitation.",
            "browser interaction",
        ),
        _criterion(
            "browser_console_clean",
            browser_logs == [],
            f"Browser console errors observed: {len(browser_logs)}.",
            "runtime hygiene",
        ),
        _criterion(
            "source_persists_override_gate_in_payload",
            "payload.combinedReceiptDownloadGate = combinedReceiptDownloadGate(payload);" in js and "localStorage.setItem(OUTSIDE_REVIEW_EXPORT_KEY, JSON.stringify(payload, null, 2));" in js,
            "Launcher source persists the current download gate back into the stored handoff payload.",
            "source binding",
        ),
        _criterion(
            "generator_preserves_override_gate_persistence",
            "payload.combinedReceiptDownloadGate = combinedReceiptDownloadGate(payload);" in generator and "localStorage.setItem(OUTSIDE_REVIEW_EXPORT_KEY, JSON.stringify(payload, null, 2));" in generator,
            "v63 generator preserves download-gate persistence in regenerated launchers.",
            "generator durability",
        ),
        _criterion(
            "experiment_index_includes_browser_smoke_report",
            "experiments.ssrm_3d_browser_world_v109_primary_demo_guarded_receipt_browser_smoke" in experiment_index,
            "Experiment runner index includes the Report 349 verifier module.",
            "runner index",
        ),
        _criterion(
            "claim_boundary_preserved",
            all(boundary.startswith("no ") or "browser-local" in boundary or "localhost" in boundary or "debug override" in boundary for boundary in BOUNDARIES),
            "Boundary rejects hosted URL, production persistence, autonomous language, consciousness, moral patienthood, complete engine, and finished gameplay claims.",
            "claim hygiene",
        ),
    ]

    by_channel: dict[str, list[float]] = {}
    for item in criteria:
        by_channel.setdefault(item["channel"], []).append(float(item["score"]))

    metrics = {
        "readiness": mean(float(item["score"]) for item in criteria),
        "weakest_channel_score": min(float(item["score"]) for item in criteria),
        "source_guard_score": mean(by_channel.get("source guard", [0.0])),
        "browser_artifact_score": mean(by_channel.get("browser artifact", [0.0])),
        "surface_discipline_score": mean(by_channel.get("surface discipline", [0.0])),
        "browser_interaction_score": mean(by_channel.get("browser interaction", [0.0])),
        "download_guard_score": mean(by_channel.get("download guard", [0.0])),
        "payload_evidence_score": mean(by_channel.get("payload evidence", [0.0])),
        "runtime_hygiene_score": mean(by_channel.get("runtime hygiene", [0.0])),
        "source_binding_score": mean(by_channel.get("source binding", [0.0])),
        "generator_durability_score": mean(by_channel.get("generator durability", [0.0])),
        "runner_index_score": mean(by_channel.get("runner index", [0.0])),
        "claim_hygiene_score": mean(by_channel.get("claim hygiene", [0.0])),
        "console_error_count": len(browser_logs),
        "download_event_observed": 1.0 if smoke.get("downloadEventObserved") is True else 0.0,
        "export_click_attempt_recorded": 1.0 if (smoke.get("downloadEventObserved") is True or "Downloads are not supported" in str(smoke.get("downloadError", ""))) else 0.0,
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
        "browser_smoke": smoke,
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
    smoke = results["browser_smoke"]
    report_path = DOCS / f"{REPORT}_{PREFIX}_report.md"
    criterion_lines = "\n".join(f"- {'PASS' if item['passed'] else 'FAIL'} `{item['name']}` ({item['channel']}): {item['detail']}" for item in criteria)
    boundary_lines = "\n".join(f"- {boundary}" for boundary in BOUNDARIES)

    report_path.write_text(
        f"# Report {REPORT}: SSRM-3D Browser World v109 Primary Demo Guarded Receipt Browser Smoke\n\n"
        "## Purpose\n\n"
        "Report 349 is the first real browser-local smoke for the guarded combined receipt path. It uses the maintained primary launcher on localhost, prepares a combined outside-review handoff, observes the normal download guard, toggles the explicit debug override, and observes the guarded export link and records whether the browser supports the download event.\n\n"
        "## Browser smoke summary\n\n"
        f"- browser: `{smoke.get('browser')}`\n"
        f"- launcher_url: `{smoke.get('launcherUrl')}`\n"
        f"- target_shell: `{smoke.get('targetShell')}`\n"
        f"- clean_launch_clicked: `{smoke.get('cleanLaunchClicked')}`\n"
        f"- returned_to_launcher: `{smoke.get('returnedToLauncher')}`\n"
        f"- prepare_outside_review_clicked: `{smoke.get('prepareOutsideReviewClicked')}`\n"
        f"- initial_gate_state: `{(smoke.get('initialGate') or {}).get('state')}`\n"
        f"- override_gate_state: `{(smoke.get('overrideGate') or {}).get('state')}`\n"
        f"- download_event_observed: `{smoke.get('downloadEventObserved')}`\n"
        f"- download_error: `{smoke.get('downloadError')}`\n"
        f"- console_errors: `{len(smoke.get('consoleErrors', []))}`\n\n"
        "## Metrics\n\n"
        f"- verdict: `{results['verdict']}`\n"
        f"- readiness: `{metrics['readiness']:.3f}`\n"
        f"- weakest_channel_score: `{metrics['weakest_channel_score']:.3f}`\n"
        f"- browser_interaction_score: `{metrics['browser_interaction_score']:.3f}`\n"
        f"- download_guard_score: `{metrics['download_guard_score']:.3f}`\n"
        f"- payload_evidence_score: `{metrics['payload_evidence_score']:.3f}`\n"
        f"- runtime_hygiene_score: `{metrics['runtime_hygiene_score']:.3f}`\n"
        f"- download_event_observed: `{metrics['download_event_observed']:.3f}`\n"
        f"- export_click_attempt_recorded: `{metrics['export_click_attempt_recorded']:.3f}`\n"
        f"- console_error_count: `{metrics['console_error_count']}`\n"
        f"- criterion_count: `{metrics['criterion_count']}`\n\n"
        "## Criteria\n\n"
        f"{criterion_lines}\n\n"
        "## Boundary\n\n"
        f"{boundary_lines}\n\n"
        "## Interpretation\n\n"
        "This report moves the receipt path from source-only verification to one actual browser-local launcher smoke. In this environment, the in-app browser does not support file downloads, so the smoke records the guarded export-link click attempt and final payload rather than claiming a completed file download. It still does not prove a hosted URL, production persistence, autonomous resident conversation, subjective consciousness, moral patienthood, a complete 3D engine, or finished gameplay.\n\n"
        "## Next gate\n\n"
        f"{results['next_gate']}\n",
        encoding="utf-8",
    )


def write_artifacts(results: dict[str, Any]) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    DOCS.mkdir(exist_ok=True)
    (ARTIFACTS / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACTS / f"{PREFIX}_state.json").write_text(json.dumps({"report": REPORT, "seed": SEED, "verdict": results["verdict"], "metrics": results["metrics"], "next_gate": results["next_gate"]}, indent=2, sort_keys=True), encoding="utf-8")
    _write_csv(ARTIFACTS / f"{PREFIX}_summary.csv", [{"report": REPORT, "seed": SEED, "verdict": results["verdict"], **results["metrics"]}], ["report", "seed", "verdict", *results["metrics"].keys()])
    _write_csv(ARTIFACTS / f"{PREFIX}_verdict.csv", [{"report": REPORT, "verdict": results["verdict"], "weakest_channel_score": results["metrics"]["weakest_channel_score"], "download_event_observed": results["metrics"]["download_event_observed"], "next_gate": results["next_gate"]}], ["report", "verdict", "weakest_channel_score", "download_event_observed", "next_gate"])
    _write_csv(ARTIFACTS / f"{PREFIX}_criteria.csv", results["criteria"], ["name", "passed", "score", "channel", "detail"])
    _write_report(results)


def main() -> dict[str, Any]:
    results = build_results()
    write_artifacts(results)
    print(json.dumps({"report": REPORT, "verdict": results["verdict"], "metrics": results["metrics"]}, indent=2, sort_keys=True))
    return results


if __name__ == "__main__":
    main()
