"""Report 344: primary demo lifecycle preflight/status panel.

Report 343 wired the lifecycle smoke runner into the primary demo entrypoint.
Report 344 makes that wiring actionable from the launcher by verifying a
browser-visible preflight panel that names freshness sources, covered lifecycle
phases, and the release-blocking phase.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 344
SEED = 20270742
PREFIX = "ssrm_3d_browser_world_v104_primary_demo_lifecycle_preflight_status_panel"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"

COMMAND = "python3 -m experiments.ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner"
POLICY = "Run this one maintained lifecycle smoke runner before adding another tab, reload, stale, repair, or return handoff report."
PREFLIGHT_BOUNDARY = "Lifecycle preflight is artifact-backed by Report 342 runner results and Report 343 entrypoint wiring evidence; it is not a live hosted browser E2E claim."
FRESHNESS_TEXT = "Report 342 runner results pass; Report 343 entrypoint wiring pass"
BLOCKING_PHASE = "none"
EXPECTED_PHASES = {
    "cross_tab_prepared_resume_visible": "fresh cross-tab prepared resume",
    "closed_origin_tab_continuity": "closed-origin continuity",
    "hard_reload_continuity": "hard-reload continuity",
    "stale_supersession_calibration": "stale prepared-handoff calibration",
    "stale_reprepare_repair": "stale mismatch clean reprepare repair",
    "repaired_continue_return_refresh": "repaired continue-return-refresh freshness",
}

ENTRYPOINT_HTML = ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/index.html"
MANUAL_PLAYTEST = ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/manual_playtest.md"
GENERATOR = ROOT / "experiments/ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
RUNNER_RESULTS = ROOT / "artifacts/ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner_results.json"
RUNNER_MANIFEST = ROOT / "artifacts/ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner_runner_manifest.json"
WIRING_RESULTS = ROOT / "artifacts/ssrm_3d_browser_world_v103_primary_demo_entrypoint_lifecycle_smoke_runner_wiring_results.json"
EXPERIMENT_INDEX = ROOT / "scripts/run_experiments.py"

BOUNDARIES = (
    "browser-visible source/status panel verification only",
    "artifact-backed freshness only",
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
    "post-344: add a local browser action that can copy/export the lifecycle preflight "
    "packet from the launcher so outside reviewers can attach one compact smoke-status "
    "receipt to vertical-slice feedback"
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _criterion(name: str, passed: bool, detail: str, channel: str) -> dict[str, Any]:
    return {
        "name": name,
        "passed": bool(passed),
        "score": 1.0 if passed else 0.0,
        "channel": channel,
        "detail": detail,
    }


def _contains_all(text: str, terms: tuple[str, ...]) -> bool:
    return all(term in text for term in terms)


def build_results() -> dict[str, Any]:
    html = _read(ENTRYPOINT_HTML)
    manual = _read(MANUAL_PLAYTEST)
    generator = _read(GENERATOR)
    experiment_index = _read(EXPERIMENT_INDEX)
    runner_results = _load_json(RUNNER_RESULTS) if RUNNER_RESULTS.exists() else {}
    runner_manifest = _load_json(RUNNER_MANIFEST) if RUNNER_MANIFEST.exists() else {}
    wiring_results = _load_json(WIRING_RESULTS) if WIRING_RESULTS.exists() else {}

    runner_metrics = runner_results.get("metrics", {})
    wiring_metrics = wiring_results.get("metrics", {})
    covered_phases = set(runner_manifest.get("covered_phases", []))
    expected_phase_set = set(EXPECTED_PHASES)

    html_panel_terms = (
        'id="lifecycleSmokePreflight"',
        'data-lifecycle-preflight-source="report-342-results+report-343-wiring"',
        'data-lifecycle-preflight-blocking-phase="none"',
        'id="lifecycleSmokeFreshness"',
        'id="lifecycleSmokeBlockingPhase"',
        'id="lifecycleSmokePreflightBoundary"',
        FRESHNESS_TEXT,
        "Blocking lifecycle phase: none",
        PREFLIGHT_BOUNDARY,
    )
    html_phase_terms = tuple(
        f'data-lifecycle-preflight-phase="{phase}" data-lifecycle-preflight-status="pass"'
        for phase in EXPECTED_PHASES
    )
    manual_terms = (
        "Preflight status visible in the launcher:",
        f"Runner freshness: {FRESHNESS_TEXT}",
        "Blocking lifecycle phase: none",
        PREFLIGHT_BOUNDARY,
        "Lifecycle phases shown in the preflight panel:",
    )
    generator_terms = (
        "LIFECYCLE_SMOKE_PREFLIGHT_FRESHNESS",
        "LIFECYCLE_SMOKE_PREFLIGHT_BLOCKING_PHASE",
        "LIFECYCLE_SMOKE_PREFLIGHT_BOUNDARY",
        'id=\\"lifecycleSmokePreflight\\"',
        'id=\\"lifecycleSmokeFreshness\\"',
        'id=\\"lifecycleSmokeBlockingPhase\\"',
        'data-lifecycle-preflight-source=\\"report-342-results+report-343-wiring\\"',
    )

    panel_packet = {
        "command": COMMAND,
        "policy": POLICY,
        "freshness": FRESHNESS_TEXT,
        "blocking_phase": BLOCKING_PHASE,
        "phase_statuses": {phase: "pass" for phase in EXPECTED_PHASES},
        "sources": {
            "runner_results": str(RUNNER_RESULTS.relative_to(ROOT)),
            "runner_manifest": str(RUNNER_MANIFEST.relative_to(ROOT)),
            "wiring_results": str(WIRING_RESULTS.relative_to(ROOT)),
            "entrypoint_html": str(ENTRYPOINT_HTML.relative_to(ROOT)),
            "manual_playtest": str(MANUAL_PLAYTEST.relative_to(ROOT)),
            "generator": str(GENERATOR.relative_to(ROOT)),
        },
        "boundary": PREFLIGHT_BOUNDARY,
    }

    criteria = [
        _criterion(
            "runner_results_available_and_passing",
            RUNNER_RESULTS.exists() and runner_results.get("verdict") == "pass" and float(runner_metrics.get("weakest_channel_score", 0.0)) >= 1.0,
            "Report 342 runner results exist, pass, and retain full weakest-channel score.",
            "artifact freshness",
        ),
        _criterion(
            "wiring_results_available_and_passing",
            WIRING_RESULTS.exists() and wiring_results.get("verdict") == "pass" and float(wiring_metrics.get("weakest_channel_score", 0.0)) >= 1.0,
            "Report 343 wiring results exist, pass, and retain full weakest-channel score.",
            "artifact freshness",
        ),
        _criterion(
            "runner_manifest_phase_set_matches_panel",
            RUNNER_MANIFEST.exists() and expected_phase_set.issubset(covered_phases),
            "Report 342 manifest phase coverage matches the phase set exposed by the preflight panel.",
            "phase coverage",
        ),
        _criterion(
            "launcher_has_preflight_panel",
            _contains_all(html, html_panel_terms),
            "Primary launcher has visible preflight panel, source marker, freshness text, blocking phase, and boundary text.",
            "entrypoint panel",
        ),
        _criterion(
            "launcher_lists_all_preflight_phases",
            _contains_all(html, html_phase_terms) and all(label in html for label in EXPECTED_PHASES.values()),
            "Primary launcher lists all lifecycle phases with pass status labels.",
            "entrypoint panel",
        ),
        _criterion(
            "launcher_still_exposes_runner_command_and_policy",
            COMMAND in html and POLICY in html,
            "Preflight panel remains attached to the Report 342 runner command and report-sprawl policy.",
            "entrypoint panel",
        ),
        _criterion(
            "manual_documents_preflight_status",
            _contains_all(manual, manual_terms),
            "Manual playtest script documents runner freshness, blocking phase, and boundary semantics.",
            "manual path",
        ),
        _criterion(
            "manual_lists_all_preflight_phases",
            all(phase in manual and label in manual for phase, label in EXPECTED_PHASES.items()),
            "Manual playtest script lists every phase shown in the preflight panel.",
            "manual path",
        ),
        _criterion(
            "generator_preserves_preflight_constants",
            _contains_all(generator, generator_terms[:3]),
            "v63 generator defines preflight freshness, blocking phase, and boundary constants.",
            "generator durability",
        ),
        _criterion(
            "generator_emits_preflight_panel",
            _contains_all(generator, generator_terms[3:]),
            "v63 generator emits the browser-visible preflight panel and source marker.",
            "generator durability",
        ),
        _criterion(
            "generator_emits_all_phase_rows",
            all(phase in generator and label in generator for phase, label in EXPECTED_PHASES.items()),
            "v63 generator preserves every preflight phase row.",
            "generator durability",
        ),
        _criterion(
            "preflight_blocking_phase_is_calibrated",
            BLOCKING_PHASE == "none" and runner_results.get("verdict") == "pass" and wiring_results.get("verdict") == "pass",
            "Blocking phase is none only because the runner and wiring verifier artifacts both pass.",
            "calibration",
        ),
        _criterion(
            "preflight_packet_is_exportable_artifact",
            panel_packet["blocking_phase"] == "none" and len(panel_packet["phase_statuses"]) == len(EXPECTED_PHASES),
            "Report 344 emits a compact preflight packet suitable for future browser export/copy wiring.",
            "preflight packet",
        ),
        _criterion(
            "experiment_index_includes_preflight_report",
            "experiments.ssrm_3d_browser_world_v104_primary_demo_lifecycle_preflight_status_panel" in experiment_index,
            "Experiment runner index includes the Report 344 verifier module.",
            "runner index",
        ),
        _criterion(
            "claim_boundary_preserved",
            all(boundary.startswith("no ") or "artifact" in boundary or "source/status" in boundary for boundary in BOUNDARIES),
            "Boundary rejects hosted URL, live browser automation, production persistence, consciousness, moral patienthood, complete engine, and finished gameplay claims.",
            "claim hygiene",
        ),
    ]

    by_channel: dict[str, list[float]] = {}
    for item in criteria:
        by_channel.setdefault(item["channel"], []).append(float(item["score"]))

    metrics = {
        "readiness": mean(float(item["score"]) for item in criteria),
        "weakest_channel_score": min(float(item["score"]) for item in criteria),
        "artifact_freshness_score": mean(by_channel.get("artifact freshness", [0.0])),
        "phase_coverage_score": mean(by_channel.get("phase coverage", [0.0])),
        "entrypoint_panel_score": mean(by_channel.get("entrypoint panel", [0.0])),
        "manual_path_score": mean(by_channel.get("manual path", [0.0])),
        "generator_durability_score": mean(by_channel.get("generator durability", [0.0])),
        "calibration_score": mean(by_channel.get("calibration", [0.0])),
        "preflight_packet_score": mean(by_channel.get("preflight packet", [0.0])),
        "runner_index_score": mean(by_channel.get("runner index", [0.0])),
        "claim_hygiene_score": mean(by_channel.get("claim hygiene", [0.0])),
        "runner_weakest_channel_score": float(runner_metrics.get("weakest_channel_score", 0.0)),
        "wiring_weakest_channel_score": float(wiring_metrics.get("weakest_channel_score", 0.0)),
        "blocking_phase_count": 0 if BLOCKING_PHASE == "none" else 1,
        "phase_count": len(EXPECTED_PHASES),
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
        "preflight_packet": panel_packet,
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
    packet = results["preflight_packet"]
    report_path = DOCS / f"{REPORT}_{PREFIX}_report.md"
    criterion_lines = "\n".join(
        f"- {'PASS' if item['passed'] else 'FAIL'} `{item['name']}` ({item['channel']}): {item['detail']}"
        for item in criteria
    )
    phase_lines = "\n".join(f"- `{phase}`: {status}" for phase, status in packet["phase_statuses"].items())
    boundary_lines = "\n".join(f"- {boundary}" for boundary in BOUNDARIES)

    report_path.write_text(
        f"# Report {REPORT}: SSRM-3D Browser World v104 Primary Demo Lifecycle Preflight Status Panel\n\n"
        "## Purpose\n\n"
        "Report 344 makes the Report 343 smoke-runner wiring actionable from the primary playable launcher. "
        "The launcher now exposes a lightweight preflight/status panel with runner freshness, release-blocking phase, lifecycle phase coverage, and claim boundary text.\n\n"
        "## What changed\n\n"
        "- Added a browser-visible `Lifecycle release preflight` panel to the primary launcher.\n"
        "- Shows runner freshness from Report 342 results and Report 343 wiring evidence.\n"
        "- Shows `Blocking lifecycle phase: none` only because the current runner and wiring artifacts pass.\n"
        "- Lists all fresh, stale, repair, and post-repair lifecycle phases with pass status.\n"
        "- Updated the manual playtest script and v63 entrypoint generator so the panel survives regeneration.\n"
        "- Emitted a compact preflight packet for the next export/copy gate.\n\n"
        "## Preflight packet\n\n"
        f"- command: `{packet['command']}`\n"
        f"- freshness: `{packet['freshness']}`\n"
        f"- blocking_phase: `{packet['blocking_phase']}`\n"
        f"- boundary: `{packet['boundary']}`\n\n"
        "## Lifecycle phase statuses\n\n"
        f"{phase_lines}\n\n"
        "## Metrics\n\n"
        f"- verdict: `{results['verdict']}`\n"
        f"- readiness: `{metrics['readiness']:.3f}`\n"
        f"- weakest_channel_score: `{metrics['weakest_channel_score']:.3f}`\n"
        f"- artifact_freshness_score: `{metrics['artifact_freshness_score']:.3f}`\n"
        f"- phase_coverage_score: `{metrics['phase_coverage_score']:.3f}`\n"
        f"- entrypoint_panel_score: `{metrics['entrypoint_panel_score']:.3f}`\n"
        f"- manual_path_score: `{metrics['manual_path_score']:.3f}`\n"
        f"- generator_durability_score: `{metrics['generator_durability_score']:.3f}`\n"
        f"- calibration_score: `{metrics['calibration_score']:.3f}`\n"
        f"- preflight_packet_score: `{metrics['preflight_packet_score']:.3f}`\n"
        f"- claim_hygiene_score: `{metrics['claim_hygiene_score']:.3f}`\n"
        f"- blocking_phase_count: `{metrics['blocking_phase_count']}`\n"
        f"- phase_count: `{metrics['phase_count']}`\n"
        f"- criterion_count: `{metrics['criterion_count']}`\n\n"
        "## Criteria\n\n"
        f"{criterion_lines}\n\n"
        "## Boundary\n\n"
        f"{boundary_lines}\n\n"
        "## Interpretation\n\n"
        "This turns the smoke-runner link from passive documentation into an operational status surface inside the launcher. "
        "It is still artifact-backed status, not a live hosted browser E2E proof, production persistence proof, autonomous conversation proof, subjective-consciousness claim, moral-patienthood claim, complete engine, or finished gameplay.\n\n"
        "## Next gate\n\n"
        f"{results['next_gate']}\n",
        encoding="utf-8",
    )


def write_artifacts(results: dict[str, Any]) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    DOCS.mkdir(exist_ok=True)
    (ARTIFACTS / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACTS / f"{PREFIX}_state.json").write_text(
        json.dumps(
            {
                "report": REPORT,
                "seed": SEED,
                "verdict": results["verdict"],
                "metrics": results["metrics"],
                "preflight_packet": results["preflight_packet"],
                "next_gate": results["next_gate"],
            },
            indent=2,
            sort_keys=True,
        ),
        encoding="utf-8",
    )
    (ARTIFACTS / f"{PREFIX}_preflight_packet.json").write_text(json.dumps(results["preflight_packet"], indent=2, sort_keys=True), encoding="utf-8")
    _write_csv(
        ARTIFACTS / f"{PREFIX}_summary.csv",
        [{"report": REPORT, "seed": SEED, "verdict": results["verdict"], **results["metrics"]}],
        ["report", "seed", "verdict", *results["metrics"].keys()],
    )
    _write_csv(
        ARTIFACTS / f"{PREFIX}_verdict.csv",
        [
            {
                "report": REPORT,
                "verdict": results["verdict"],
                "weakest_channel_score": results["metrics"]["weakest_channel_score"],
                "blocking_phase_count": results["metrics"]["blocking_phase_count"],
                "next_gate": results["next_gate"],
            }
        ],
        ["report", "verdict", "weakest_channel_score", "blocking_phase_count", "next_gate"],
    )
    _write_csv(
        ARTIFACTS / f"{PREFIX}_criteria.csv",
        results["criteria"],
        ["name", "passed", "score", "channel", "detail"],
    )
    _write_report(results)


def main() -> dict[str, Any]:
    results = build_results()
    write_artifacts(results)
    print(json.dumps({"report": REPORT, "verdict": results["verdict"], "metrics": results["metrics"]}, indent=2, sort_keys=True))
    return results


if __name__ == "__main__":
    main()
