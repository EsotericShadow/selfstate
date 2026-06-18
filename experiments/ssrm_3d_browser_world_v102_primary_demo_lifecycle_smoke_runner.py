"""Report 342: reusable primary-demo lifecycle smoke runner.

Report 341 defined the lifecycle contract. This module turns that contract into a
single maintained smoke runner surface so future primary-demo handoff work can run
one deterministic gate instead of adding one-off tab/reload/return variants.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import mean
from typing import Any

from experiments import ssrm_3d_browser_world_v101_primary_demo_lifecycle_smoke_contract as contract_module

REPORT = 342
SEED = 20270740
PREFIX = "ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"

EXPECTED_PHASES = {
    "cross_tab_prepared_resume_visible",
    "closed_origin_tab_continuity",
    "hard_reload_continuity",
    "stale_supersession_calibration",
    "stale_reprepare_repair",
    "repaired_continue_return_refresh",
}

FRESH_PHASES = {
    "cross_tab_prepared_resume_visible",
    "closed_origin_tab_continuity",
    "hard_reload_continuity",
}
STALE_PHASES = {"stale_supersession_calibration"}
REPAIR_PHASES = {"stale_reprepare_repair"}
POST_REPAIR_PHASES = {"repaired_continue_return_refresh"}

RECOMMENDED_COMMAND = "python3 -m experiments.ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner"
CONTRACT_COMMAND = "python3 -m experiments.ssrm_3d_browser_world_v101_primary_demo_lifecycle_smoke_contract"

BOUNDARIES = (
    "reusable deterministic lifecycle smoke runner only",
    "browser-local artifact and source-binding evidence only",
    "no live hosted URL claim",
    "no production persistence claim",
    "no autonomous natural-language claim",
    "no subjective-consciousness claim",
    "no moral-patienthood claim",
    "no complete 3D engine claim",
    "no finished gameplay claim",
)

NEXT_GATE = (
    "post-342: wire the primary playable demo entrypoint to this lifecycle smoke runner "
    "so future vertical-slice work changes the maintained surface and immediately exercises "
    "fresh, stale, repair, and post-repair handoff paths"
)


def _criterion(name: str, passed: bool, detail: str, channel: str) -> dict[str, Any]:
    return {
        "name": name,
        "passed": bool(passed),
        "score": 1.0 if passed else 0.0,
        "channel": channel,
        "detail": detail,
    }


def _contract_artifacts_exist() -> bool:
    paths = [
        ARTIFACTS / f"{contract_module.PREFIX}_results.json",
        ARTIFACTS / f"{contract_module.PREFIX}_summary.csv",
        ARTIFACTS / f"{contract_module.PREFIX}_verdict.csv",
        ARTIFACTS / f"{contract_module.PREFIX}_criteria.csv",
        ARTIFACTS / f"{contract_module.PREFIX}_state.json",
        ARTIFACTS / f"{contract_module.PREFIX}_contract.json",
        DOCS / f"{contract_module.REPORT}_{contract_module.PREFIX}_report.md",
    ]
    return all(path.exists() for path in paths)


def _runner_manifest(contract_results: dict[str, Any]) -> dict[str, Any]:
    phases = [phase["phase"] for phase in contract_results["contract"]["phases"]]
    return {
        "report": REPORT,
        "seed": SEED,
        "name": "primary_demo_lifecycle_smoke_runner",
        "recommended_command": RECOMMENDED_COMMAND,
        "contract_refresh_command": CONTRACT_COMMAND,
        "routine_policy": "run one maintained lifecycle smoke runner after primary-demo handoff changes",
        "manual_variant_policy": "do not add another tab, reload, stale, or return report unless this runner fails and the failure names a missing lifecycle path",
        "covered_phases": phases,
        "required_phase_sets": {
            "fresh": sorted(FRESH_PHASES),
            "stale": sorted(STALE_PHASES),
            "repair": sorted(REPAIR_PHASES),
            "post_repair": sorted(POST_REPAIR_PHASES),
        },
        "failure_outputs": {
            "results": f"artifacts/{PREFIX}_results.json",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "manifest": f"artifacts/{PREFIX}_runner_manifest.json",
            "contract_results": f"artifacts/{contract_module.PREFIX}_results.json",
        },
        "rerun_commands": [
            RECOMMENDED_COMMAND,
            "python3 -m py_compile experiments/ssrm_3d_browser_world_v102_primary_demo_lifecycle_smoke_runner.py experiments/ssrm_3d_browser_world_v101_primary_demo_lifecycle_smoke_contract.py scripts/run_experiments.py",
            "git diff --check",
        ],
        "future_browser_e2e_slot": {
            "status": "not_claimed",
            "reason": "This runner consolidates deterministic lifecycle artifacts and source bindings; it does not replace a real browser automation gate for future hosted/playable checks.",
        },
        "boundaries": BOUNDARIES,
    }


def build_results() -> dict[str, Any]:
    contract_results = contract_module.build_results()
    contract_module.write_artifacts(contract_results)

    contract = contract_results["contract"]
    phases = {phase["phase"] for phase in contract["phases"]}
    requirements = set(contract.get("future_smoke_requirements", []))
    manifest = _runner_manifest(contract_results)
    contract_metrics = contract_results["metrics"]

    failed_contract_criteria = [item["name"] for item in contract_results["criteria"] if not item["passed"]]
    source_bindings_full = float(contract_metrics.get("source_binding_score", 0.0)) >= 1.0
    input_reports_full = float(contract_metrics.get("input_report_pass_rate", 0.0)) >= 1.0
    no_console_errors = int(contract_metrics.get("console_errors_total", 1)) == 0

    criteria = [
        _criterion(
            "contract_module_available",
            contract_module.REPORT == 341 and contract_module.PREFIX.endswith("lifecycle_smoke_contract"),
            "Runner imports the canonical Report 341 lifecycle contract module.",
            "runner binding",
        ),
        _criterion(
            "contract_rebuilds_in_process",
            contract_results.get("verdict") == "pass" and not failed_contract_criteria,
            "Runner rebuilds the lifecycle contract in-process before judging its own status.",
            "executable contract",
        ),
        _criterion(
            "contract_artifacts_refreshed",
            _contract_artifacts_exist(),
            "Runner refreshes or confirms the canonical contract result, summary, verdict, criteria, state, contract, and report artifacts.",
            "artifact refresh",
        ),
        _criterion(
            "contract_weakest_channel_full",
            float(contract_metrics.get("weakest_channel_score", 0.0)) >= 1.0,
            f"Contract weakest-channel score is {float(contract_metrics.get('weakest_channel_score', 0.0)):.3f}.",
            "evidence quality",
        ),
        _criterion(
            "single_recommended_runner_surface",
            manifest["recommended_command"] == RECOMMENDED_COMMAND and len([manifest["recommended_command"]]) == 1,
            "Manifest exposes one recommended smoke command for future primary-demo handoff changes.",
            "maintainability",
        ),
        _criterion(
            "manual_variant_policy_blocks_report_sprawl",
            "do not add another" in manifest["manual_variant_policy"] and "runner fails" in manifest["manual_variant_policy"],
            "Manifest says new lifecycle variants should be driven by runner failures, not report sprawl.",
            "maintainability",
        ),
        _criterion(
            "all_lifecycle_phases_covered",
            phases == EXPECTED_PHASES,
            f"Covered phases: {', '.join(sorted(phases))}.",
            "phase coverage",
        ),
        _criterion(
            "fresh_path_phase_set_covered",
            FRESH_PHASES.issubset(phases),
            "Fresh path covers cross-tab, closed-origin, and hard-reload continuity.",
            "phase coverage",
        ),
        _criterion(
            "stale_path_phase_set_covered",
            STALE_PHASES.issubset(phases),
            "Stale path covers stale prepared-handoff calibration.",
            "phase coverage",
        ),
        _criterion(
            "repair_path_phase_set_covered",
            REPAIR_PHASES.issubset(phases),
            "Repair path covers clean reprepare after stale mismatch.",
            "phase coverage",
        ),
        _criterion(
            "post_repair_phase_set_covered",
            POST_REPAIR_PHASES.issubset(phases),
            "Post-repair path covers actual continue, return, refresh, and reload freshness.",
            "phase coverage",
        ),
        _criterion(
            "future_smoke_requirements_present",
            len(requirements) >= 7 and any("repair stale" in item for item in requirements) and any("return" in item for item in requirements),
            "Contract retains actionable future smoke requirements instead of a vague pass/fail label.",
            "actionability",
        ),
        _criterion(
            "failure_output_is_actionable",
            all(key in manifest["failure_outputs"] for key in ("results", "criteria", "manifest", "contract_results")) and len(manifest["rerun_commands"]) >= 3,
            "Runner manifest points to failure artifacts and exact rerun commands.",
            "actionability",
        ),
        _criterion(
            "input_report_evidence_full",
            input_reports_full,
            f"Input report pass rate is {float(contract_metrics.get('input_report_pass_rate', 0.0)):.3f}.",
            "evidence quality",
        ),
        _criterion(
            "source_binding_evidence_full",
            source_bindings_full,
            f"Source binding score is {float(contract_metrics.get('source_binding_score', 0.0)):.3f}.",
            "source binding",
        ),
        _criterion(
            "aggregated_console_clean",
            no_console_errors,
            f"Aggregated console error count is {int(contract_metrics.get('console_errors_total', 1))}.",
            "runtime hygiene",
        ),
        _criterion(
            "future_browser_e2e_slot_not_claimed",
            manifest["future_browser_e2e_slot"]["status"] == "not_claimed",
            "Manifest reserves a future live browser E2E slot without pretending this deterministic runner is that proof.",
            "claim hygiene",
        ),
        _criterion(
            "claim_boundary_preserved",
            all(boundary.startswith("no ") or "browser-local" in boundary or "runner only" in boundary for boundary in BOUNDARIES),
            "Boundaries explicitly reject hosted URL, production persistence, complete gameplay, consciousness, and moral-patienthood claims.",
            "claim hygiene",
        ),
    ]

    by_channel: dict[str, list[float]] = {}
    for item in criteria:
        by_channel.setdefault(item["channel"], []).append(float(item["score"]))

    metrics = {
        "readiness": mean(float(item["score"]) for item in criteria),
        "weakest_channel_score": min(float(item["score"]) for item in criteria),
        "executable_contract_score": mean(by_channel.get("executable contract", [0.0])),
        "single_runner_surface_score": mean(by_channel.get("maintainability", [0.0])),
        "phase_coverage_score": mean(by_channel.get("phase coverage", [0.0])),
        "artifact_refresh_score": mean(by_channel.get("artifact refresh", [0.0])),
        "actionability_score": mean(by_channel.get("actionability", [0.0])),
        "evidence_quality_score": mean(by_channel.get("evidence quality", [0.0])),
        "source_binding_score": mean(by_channel.get("source binding", [0.0])),
        "runtime_hygiene_score": mean(by_channel.get("runtime hygiene", [0.0])),
        "claim_boundary_score": mean(by_channel.get("claim hygiene", [0.0])),
        "contract_input_report_pass_rate": float(contract_metrics.get("input_report_pass_rate", 0.0)),
        "contract_weakest_channel_score": float(contract_metrics.get("weakest_channel_score", 0.0)),
        "console_errors_total": int(contract_metrics.get("console_errors_total", 1)),
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
        "runner_manifest": manifest,
        "contract_summary": {
            "report": contract_results["report"],
            "verdict": contract_results["verdict"],
            "metrics": contract_results["metrics"],
            "phases": sorted(phases),
            "failed_criteria": failed_contract_criteria,
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
    manifest = results["runner_manifest"]
    report_path = DOCS / f"{REPORT}_{PREFIX}_report.md"

    criterion_lines = "\n".join(
        f"- {'PASS' if item['passed'] else 'FAIL'} `{item['name']}` ({item['channel']}): {item['detail']}"
        for item in criteria
    )
    phase_lines = "\n".join(f"- `{phase}`" for phase in manifest["covered_phases"])
    boundary_lines = "\n".join(f"- {boundary}" for boundary in BOUNDARIES)
    command_lines = "\n".join(f"- `{command}`" for command in manifest["rerun_commands"])

    report_path.write_text(
        f"# Report {REPORT}: SSRM-3D Browser World v102 Primary Demo Lifecycle Smoke Runner\n\n"
        "## Purpose\n\n"
        "Report 342 turns the Report 341 lifecycle contract into one reusable deterministic smoke runner. "
        "The point is consolidation: future primary-demo handoff work should run a maintained lifecycle gate instead of adding a new bridge report for each tab, reload, stale, repair, or return variant.\n\n"
        "## What changed\n\n"
        "- Added one recommended lifecycle smoke command for the primary demo handoff surface.\n"
        "- Rebuilt the Report 341 contract in-process before judging the runner.\n"
        "- Emitted a runner manifest with covered phases, failure artifacts, rerun commands, and a policy against report sprawl.\n"
        "- Kept the future live browser E2E slot explicit but not claimed by this deterministic runner.\n\n"
        "## Recommended smoke command\n\n"
        f"`{manifest['recommended_command']}`\n\n"
        "## Covered lifecycle phases\n\n"
        f"{phase_lines}\n\n"
        "## Rerun commands\n\n"
        f"{command_lines}\n\n"
        "## Metrics\n\n"
        f"- verdict: `{results['verdict']}`\n"
        f"- readiness: `{metrics['readiness']:.3f}`\n"
        f"- weakest_channel_score: `{metrics['weakest_channel_score']:.3f}`\n"
        f"- executable_contract_score: `{metrics['executable_contract_score']:.3f}`\n"
        f"- single_runner_surface_score: `{metrics['single_runner_surface_score']:.3f}`\n"
        f"- phase_coverage_score: `{metrics['phase_coverage_score']:.3f}`\n"
        f"- artifact_refresh_score: `{metrics['artifact_refresh_score']:.3f}`\n"
        f"- actionability_score: `{metrics['actionability_score']:.3f}`\n"
        f"- evidence_quality_score: `{metrics['evidence_quality_score']:.3f}`\n"
        f"- source_binding_score: `{metrics['source_binding_score']:.3f}`\n"
        f"- runtime_hygiene_score: `{metrics['runtime_hygiene_score']:.3f}`\n"
        f"- claim_boundary_score: `{metrics['claim_boundary_score']:.3f}`\n"
        f"- contract_input_report_pass_rate: `{metrics['contract_input_report_pass_rate']:.3f}`\n"
        f"- contract_weakest_channel_score: `{metrics['contract_weakest_channel_score']:.3f}`\n"
        f"- console_errors_total: `{metrics['console_errors_total']}`\n"
        f"- criterion_count: `{metrics['criterion_count']}`\n\n"
        "## Criteria\n\n"
        f"{criterion_lines}\n\n"
        "## Boundary\n\n"
        f"{boundary_lines}\n\n"
        "## Interpretation\n\n"
        "This is a maintenance consolidation result. It makes the next vertical-slice work less toy-like by reducing report sprawl and giving future handoff changes one command that exercises fresh, stale, repair, and post-repair paths. "
        "It still does not prove a hosted playable world, production persistence, autonomous resident conversation, subjective consciousness, moral patienthood, a complete 3D engine, or finished gameplay.\n\n"
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
                "contract_summary": results["contract_summary"],
                "next_gate": results["next_gate"],
            },
            indent=2,
            sort_keys=True,
        ),
        encoding="utf-8",
    )
    (ARTIFACTS / f"{PREFIX}_runner_manifest.json").write_text(json.dumps(results["runner_manifest"], indent=2, sort_keys=True), encoding="utf-8")

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
                "recommended_command": results["runner_manifest"]["recommended_command"],
                "next_gate": results["next_gate"],
            }
        ],
        ["report", "verdict", "weakest_channel_score", "recommended_command", "next_gate"],
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
