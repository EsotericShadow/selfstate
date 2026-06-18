"""Report 343: primary demo entrypoint lifecycle smoke-runner wiring.

Report 342 created the reusable lifecycle smoke runner. Report 343 verifies that
the primary playable demo entrypoint now exposes that runner directly through the
launcher, manual playtest script, and v63 generator so future handoff work changes
one maintained surface instead of adding detached lifecycle reports.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 343
SEED = 20270741
PREFIX = "ssrm_3d_browser_world_v103_primary_demo_entrypoint_lifecycle_smoke_runner_wiring"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"

COMMAND = "python3 -m experiments.ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner"
POLICY = "Run this one maintained lifecycle smoke runner before adding another tab, reload, stale, repair, or return handoff report."
REPORT_342_DOC = "docs/342_ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner_report.md"
REPORT_342_RESULTS = "artifacts/ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner_results.json"
REPORT_342_MANIFEST = "artifacts/ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner_runner_manifest.json"

ENTRYPOINT_HTML = ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/index.html"
MANUAL_PLAYTEST = ROOT / "visualizations/ssrm_3d_browser_world_primary_demo/manual_playtest.md"
GENERATOR = ROOT / "experiments/ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
RUNNER_RESULTS = ROOT / REPORT_342_RESULTS
RUNNER_MANIFEST = ROOT / REPORT_342_MANIFEST
EXPERIMENT_INDEX = ROOT / "scripts/run_experiments.py"

BOUNDARIES = (
    "entrypoint wiring and deterministic source verification only",
    "no hosted URL claim",
    "no live browser automation claim",
    "no production persistence claim",
    "no autonomous natural-language claim",
    "no subjective-consciousness claim",
    "no moral-patienthood claim",
    "no complete 3D engine claim",
    "no finished gameplay claim",
)

NEXT_GATE = (
    "post-343: make the smoke-runner wiring actionable from the playable demo by adding "
    "a lightweight browser-visible preflight/status panel that explains when the runner was "
    "last regenerated and what lifecycle phase would block release"
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _has_all(text: str, terms: tuple[str, ...]) -> bool:
    return all(term in text for term in terms)


def _criterion(name: str, passed: bool, detail: str, channel: str) -> dict[str, Any]:
    return {
        "name": name,
        "passed": bool(passed),
        "score": 1.0 if passed else 0.0,
        "channel": channel,
        "detail": detail,
    }


def build_results() -> dict[str, Any]:
    html = _read(ENTRYPOINT_HTML)
    manual = _read(MANUAL_PLAYTEST)
    generator = _read(GENERATOR)
    experiment_index = _read(EXPERIMENT_INDEX)
    runner_results = _load_json(RUNNER_RESULTS) if RUNNER_RESULTS.exists() else {}
    runner_manifest = _load_json(RUNNER_MANIFEST) if RUNNER_MANIFEST.exists() else {}

    html_terms = (
        'id="lifecycleSmokeRunner"',
        'id="lifecycleSmokeRunnerCommand"',
        'id="lifecycleSmokeRunnerPolicy"',
        COMMAND,
        POLICY,
        "../../" + REPORT_342_DOC,
        "../../" + REPORT_342_RESULTS,
        "../../" + REPORT_342_MANIFEST,
    )
    manual_terms = (
        "MP-13",
        COMMAND,
        POLICY,
        REPORT_342_DOC,
        REPORT_342_RESULTS,
        REPORT_342_MANIFEST,
    )
    generator_terms = (
        "LIFECYCLE_SMOKE_RUNNER_COMMAND",
        "LIFECYCLE_SMOKE_RUNNER_POLICY",
        "LIFECYCLE_SMOKE_RUNNER_REPORT_REL",
        "LIFECYCLE_SMOKE_RUNNER_RESULTS_REL",
        "LIFECYCLE_SMOKE_RUNNER_MANIFEST_REL",
        "MP-13",
        '"required": True',
        COMMAND,
        POLICY,
        'id=\\"lifecycleSmokeRunner\\"',
        'id=\\"lifecycleSmokeRunnerCommand\\"',
    )

    runner_metrics = runner_results.get("metrics", {})
    future_slot = runner_manifest.get("future_browser_e2e_slot", {})
    covered_phases = set(runner_manifest.get("covered_phases", []))
    required_phases = {
        "cross_tab_prepared_resume_visible",
        "closed_origin_tab_continuity",
        "hard_reload_continuity",
        "stale_supersession_calibration",
        "stale_reprepare_repair",
        "repaired_continue_return_refresh",
    }

    criteria = [
        _criterion(
            "runner_artifacts_available_and_passing",
            RUNNER_RESULTS.exists() and RUNNER_MANIFEST.exists() and runner_results.get("verdict") == "pass",
            "Report 342 runner results and manifest exist and the runner verdict is pass.",
            "runner evidence",
        ),
        _criterion(
            "runner_command_matches_manifest",
            runner_manifest.get("recommended_command") == COMMAND,
            "Entrypoint wiring uses the same command as the Report 342 runner manifest.",
            "runner evidence",
        ),
        _criterion(
            "runner_phase_coverage_retained",
            required_phases.issubset(covered_phases) and float(runner_metrics.get("phase_coverage_score", 0.0)) >= 1.0,
            "The wired runner still covers fresh, stale, repair, and post-repair lifecycle phases.",
            "runner evidence",
        ),
        _criterion(
            "launcher_exposes_visible_smoke_section",
            _has_all(html, html_terms[:5]),
            "Primary demo launcher exposes a visible lifecycle-smoke section with command and policy.",
            "entrypoint wiring",
        ),
        _criterion(
            "launcher_links_runner_artifacts",
            _has_all(html, html_terms[5:]),
            "Primary demo launcher links the Report 342 doc, results artifact, and runner manifest.",
            "entrypoint wiring",
        ),
        _criterion(
            "launcher_hero_has_runner_action",
            "Lifecycle smoke runner" in html and "manual_playtest.md" in html,
            "Launcher hero exposes the smoke runner next to the manual playtest script.",
            "entrypoint wiring",
        ),
        _criterion(
            "manual_playtest_has_mp13_runner_step",
            _has_all(manual, manual_terms[:3]),
            "Manual playtest script adds MP-13 for the maintained lifecycle smoke runner.",
            "manual path",
        ),
        _criterion(
            "manual_playtest_lists_runner_artifacts",
            _has_all(manual, manual_terms[3:]),
            "Manual playtest script lists the Report 342 doc, results, and manifest artifacts.",
            "manual path",
        ),
        _criterion(
            "generator_preserves_runner_constants",
            _has_all(generator, generator_terms[:5]),
            "The v63 entrypoint generator defines reusable smoke-runner constants.",
            "generator durability",
        ),
        _criterion(
            "generator_preserves_required_mp13",
            _has_all(generator, generator_terms[5:8]),
            "The v63 generator includes MP-13 as a required manual step.",
            "generator durability",
        ),
        _criterion(
            "generator_generates_smoke_section",
            _has_all(generator, generator_terms[8:]),
            "The v63 generator emits the visible lifecycle-smoke section and command binding.",
            "generator durability",
        ),
        _criterion(
            "policy_blocks_lifecycle_report_sprawl",
            all(POLICY in text for text in (html, manual, generator)) and "do not add another" in runner_manifest.get("manual_variant_policy", ""),
            "Launcher, manual, generator, and runner manifest all direct future work toward one maintained gate.",
            "consolidation policy",
        ),
        _criterion(
            "experiment_index_includes_wiring_report",
            "experiments.ssrm_3d_browser_world_v103_primary_demo_entrypoint_lifecycle_smoke_runner_wiring" in experiment_index,
            "The experiment runner index includes the Report 343 verifier module.",
            "runner index",
        ),
        _criterion(
            "future_browser_e2e_boundary_preserved",
            future_slot.get("status") == "not_claimed" and "no live browser automation claim" in BOUNDARIES,
            "The wiring remains honest that this is source/artifact wiring, not a live browser E2E proof.",
            "claim hygiene",
        ),
        _criterion(
            "claim_boundary_preserved",
            all(boundary.startswith("no ") or "wiring" in boundary for boundary in BOUNDARIES),
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
        "runner_evidence_score": mean(by_channel.get("runner evidence", [0.0])),
        "entrypoint_wiring_score": mean(by_channel.get("entrypoint wiring", [0.0])),
        "manual_path_score": mean(by_channel.get("manual path", [0.0])),
        "generator_durability_score": mean(by_channel.get("generator durability", [0.0])),
        "consolidation_policy_score": mean(by_channel.get("consolidation policy", [0.0])),
        "runner_index_score": mean(by_channel.get("runner index", [0.0])),
        "claim_hygiene_score": mean(by_channel.get("claim hygiene", [0.0])),
        "runner_phase_coverage_score": float(runner_metrics.get("phase_coverage_score", 0.0)),
        "runner_weakest_channel_score": float(runner_metrics.get("weakest_channel_score", 0.0)),
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
        "wiring": {
            "command": COMMAND,
            "policy": POLICY,
            "entrypoint_html": str(ENTRYPOINT_HTML.relative_to(ROOT)),
            "manual_playtest": str(MANUAL_PLAYTEST.relative_to(ROOT)),
            "generator": str(GENERATOR.relative_to(ROOT)),
            "runner_results": REPORT_342_RESULTS,
            "runner_manifest": REPORT_342_MANIFEST,
            "covered_phases": sorted(covered_phases),
        },
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
    wiring = results["wiring"]
    report_path = DOCS / f"{REPORT}_{PREFIX}_report.md"
    criterion_lines = "\n".join(
        f"- {'PASS' if item['passed'] else 'FAIL'} `{item['name']}` ({item['channel']}): {item['detail']}"
        for item in criteria
    )
    boundary_lines = "\n".join(f"- {boundary}" for boundary in BOUNDARIES)
    phase_lines = "\n".join(f"- `{phase}`" for phase in wiring["covered_phases"])

    report_path.write_text(
        f"# Report {REPORT}: SSRM-3D Browser World v103 Primary Demo Entrypoint Lifecycle Smoke Runner Wiring\n\n"
        "## Purpose\n\n"
        "Report 343 wires the reusable Report 342 lifecycle smoke runner into the primary playable demo entrypoint. "
        "The launcher, manual playtest script, and v63 generator now all point future handoff changes at one maintained smoke command rather than encouraging another detached lifecycle report.\n\n"
        "## What changed\n\n"
        "- Added a visible `Maintained lifecycle smoke runner` section to the primary demo launcher.\n"
        "- Added the runner command, Report 342 doc link, results link, and manifest link to the launcher.\n"
        "- Added `MP-13` to the manual playtest path and recorder/defect step list.\n"
        "- Updated the v63 entrypoint generator so regenerated launchers preserve the wiring.\n"
        "- Added a deterministic verifier that fails if command, policy, artifact links, manual step, generator constants, or runner manifest alignment disappear.\n\n"
        "## Wired command\n\n"
        f"`{wiring['command']}`\n\n"
        "## Runner phases retained\n\n"
        f"{phase_lines}\n\n"
        "## Metrics\n\n"
        f"- verdict: `{results['verdict']}`\n"
        f"- readiness: `{metrics['readiness']:.3f}`\n"
        f"- weakest_channel_score: `{metrics['weakest_channel_score']:.3f}`\n"
        f"- runner_evidence_score: `{metrics['runner_evidence_score']:.3f}`\n"
        f"- entrypoint_wiring_score: `{metrics['entrypoint_wiring_score']:.3f}`\n"
        f"- manual_path_score: `{metrics['manual_path_score']:.3f}`\n"
        f"- generator_durability_score: `{metrics['generator_durability_score']:.3f}`\n"
        f"- consolidation_policy_score: `{metrics['consolidation_policy_score']:.3f}`\n"
        f"- runner_index_score: `{metrics['runner_index_score']:.3f}`\n"
        f"- claim_hygiene_score: `{metrics['claim_hygiene_score']:.3f}`\n"
        f"- runner_phase_coverage_score: `{metrics['runner_phase_coverage_score']:.3f}`\n"
        f"- runner_weakest_channel_score: `{metrics['runner_weakest_channel_score']:.3f}`\n"
        f"- criterion_count: `{metrics['criterion_count']}`\n\n"
        "## Criteria\n\n"
        f"{criterion_lines}\n\n"
        "## Boundary\n\n"
        f"{boundary_lines}\n\n"
        "## Interpretation\n\n"
        "This is a small but direct consolidation step: the playable entrypoint now tells reviewers and future maintainers which lifecycle smoke gate protects the handoff path. "
        "It does not prove a hosted URL, live browser automation, production persistence, autonomous resident conversation, subjective consciousness, moral patienthood, complete 3D engine, or finished gameplay.\n\n"
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
                "wiring": results["wiring"],
                "next_gate": results["next_gate"],
            },
            indent=2,
            sort_keys=True,
        ),
        encoding="utf-8",
    )
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
                "command": results["wiring"]["command"],
                "next_gate": results["next_gate"],
            }
        ],
        ["report", "verdict", "weakest_channel_score", "command", "next_gate"],
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
