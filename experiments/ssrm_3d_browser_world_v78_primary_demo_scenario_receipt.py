"""Report 318: SSRM-3D browser world v78 primary demo scenario receipt.

This report turns the integrated continuity loop into a reviewer-facing receipt. The
receipt derives PASS/FAIL fields from public browser-local state for entry, schedule,
debt, offscreen life, trust repair, resident social memory, public history, replay/export,
and resume readiness.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 318
PREFIX = "ssrm_3d_browser_world_v78_primary_demo_scenario_receipt"
DEFAULT_SEED = 20270716

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V61_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening.py"
V61_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
V61_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local scenario-receipt consolidation only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, "
    "no complete 3D engine, and no finished gameplay claim. The receipt audits public state continuity, "
    "not private experience."
)

NEXT_GATE = (
    "post-318: make the receipt actionable for outside reviewers by adding a compact defect/observation "
    "capture path tied to each failed receipt field, still inside the single primary shell"
)


@dataclass(frozen=True)
class Criterion:
    channel: str
    passed: bool
    score: float
    evidence: str
    failure_if_false: str


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


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
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(normalized)


def _criterion(channel: str, passed: bool, evidence: str, failure_if_false: str, partial: float = 0.0) -> Criterion:
    return Criterion(channel, passed, 1.0 if passed else partial, evidence, failure_if_false)


def _evaluate(seed: int) -> dict[str, Any]:
    gen = _read(V61_GEN)
    app = _read(V61_APP)
    index = _read(V61_INDEX)
    browser = _load_json(BROWSER_EVIDENCE)
    receipt_fields = [
        "entry_and_movement",
        "schedule_visibility",
        "debt_consequence",
        "offscreen_life",
        "recoverable_trust_repair",
        "resident_social_memory",
        "public_history_sync",
        "replay_export_ready",
        "resume_ready_snapshot",
    ]

    criteria = [
        _criterion(
            "receipt_panel_present",
            "scenarioReceiptOut" in index and "Integrated scenario receipt" in index,
            "maintained shell exposes a compact integrated scenario receipt panel",
            "reviewers would still need to cross-check multiple raw panels manually",
        ),
        _criterion(
            "generated_source_of_truth",
            all(term in gen for term in ["calculateScenarioReceipt", "formatScenarioReceipt", "generateScenarioReceipt", "scenarioReceiptOut"]),
            "receipt logic is generated from the maintained v61 source",
            "regeneration would erase the receipt audit layer",
        ),
        _criterion(
            "public_state_receipt_fields",
            all(term in app for term in receipt_fields),
            "receipt fields cover entry, schedule, debt, offscreen, repair, social memory, history, replay, and resume readiness",
            "receipt would not cover the actual non-toy integration requirements",
        ),
        _criterion(
            "boundary_visible_in_receipt",
            "no subjective consciousness" in app and "no moral patienthood" in app,
            "receipt repeats the no-consciousness/no-moral-patienthood boundary",
            "all-pass receipt could be mistaken for a subjective-experience claim",
        ),
        _criterion(
            "browser_receipt_all_pass",
            browser.get("receipt_all_pass") is True,
            str(browser.get("receipt_all_pass_evidence", "missing receipt all-pass evidence")),
            "browser receipt did not reach ALL_PASS after the integrated loop",
        ),
        _criterion(
            "browser_receipt_fields_visible",
            browser.get("receipt_fields_visible_pass") is True,
            str(browser.get("receipt_fields_visible_evidence", "missing receipt field evidence")),
            "browser receipt did not visibly list every required PASS field",
        ),
        _criterion(
            "browser_generate_receipt_action",
            browser.get("generate_receipt_action_pass") is True,
            str(browser.get("generate_receipt_action_evidence", "missing generate receipt action evidence")),
            "manual receipt generation did not create replay/checkpoint evidence",
        ),
        _criterion(
            "browser_resume_receipt_persistence",
            browser.get("resume_receipt_persistence_pass") is True,
            str(browser.get("resume_receipt_persistence_evidence", "missing resume receipt evidence")),
            "receipt all-pass state did not survive leave/resume",
        ),
        _criterion(
            "browser_receipt_matches_integrated_loop",
            browser.get("receipt_matches_loop_pass") is True,
            str(browser.get("receipt_matches_loop_evidence", "missing receipt/loop match evidence")),
            "receipt did not agree with continuity-loop/social-memory panels",
        ),
        _criterion(
            "console_clean",
            browser.get("console_errors") == 0,
            f"browser console error count was {browser.get('console_errors')}",
            "browser workflow produced runtime console errors",
        ),
    ]

    scores = [row.score for row in criteria]
    readiness = mean(scores)
    weakest = min(scores)
    verdict = "pass" if readiness >= 0.94 and weakest >= 0.9 and all(row.passed for row in criteria) else "needs_browser_evidence"
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "receipt_panel_score": next(row.score for row in criteria if row.channel == "receipt_panel_present"),
        "browser_receipt_score": next(row.score for row in criteria if row.channel == "browser_receipt_all_pass"),
        "console_errors": browser.get("console_errors", -1),
        "criterion_count": len(criteria),
        "receipt_field_count": len(receipt_fields),
    }
    return {
        "report": REPORT,
        "prefix": PREFIX,
        "seed": seed,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "verdict": verdict,
        "metrics": metrics,
        "criteria": [asdict(row) for row in criteria],
        "receipt_fields": receipt_fields,
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "browser_evidence": browser,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "state": f"artifacts/{PREFIX}_state.json",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v78_primary_demo_scenario_receipt_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    receipt_fields = ", ".join(results["receipt_fields"])
    report = f"""# Report 318: SSRM-3D Browser World v78 Primary Demo Scenario Receipt

## Purpose

Report 318 makes the one-button integrated primary-demo loop easier to review by adding an all-public scenario receipt. Instead of forcing reviewers to read raw JSON or compare every panel manually, the maintained shell now shows PASS/FAIL fields for the integrated loop.

This is interface and audit consolidation, not a new simulation branch.

## Boundary

{results['boundary']}

## What changed

- Added an `Integrated scenario receipt` panel to the maintained v61 shell.
- Added `Generate receipt`, which records a public receipt checkpoint/replay row.
- Derived receipt fields from public replay, history, relationship, checkpoint, and export state.
- Verified that receipt all-pass survives primary-demo resume.

## Receipt fields

`{receipt_fields}`

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| receipt_panel_score | {metrics['receipt_panel_score']:.6f} |
| browser_receipt_score | {metrics['browser_receipt_score']:.6f} |
| receipt_field_count | {metrics['receipt_field_count']} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- receipt_all_pass: `{browser.get('receipt_all_pass')}`
- receipt_fields_visible_pass: `{browser.get('receipt_fields_visible_pass')}`
- generate_receipt_action_pass: `{browser.get('generate_receipt_action_pass')}`
- resume_receipt_persistence_pass: `{browser.get('resume_receipt_persistence_pass')}`
- receipt_matches_loop_pass: `{browser.get('receipt_matches_loop_pass')}`
- console_errors: `{browser.get('console_errors')}`
- receipt all-pass evidence: `{browser.get('receipt_all_pass_evidence')}`
- field evidence: `{browser.get('receipt_fields_visible_evidence')}`
- generation evidence: `{browser.get('generate_receipt_action_evidence')}`
- resume evidence: `{browser.get('resume_receipt_persistence_evidence')}`
- loop match evidence: `{browser.get('receipt_matches_loop_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

The receipt is an audit affordance over deterministic public browser-local state. It does not claim subjective experience, moral status, autonomous language, production persistence, complete gameplay, or a complete 3D engine.

## Next gate

{results['next_gate']}
"""
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v78_primary_demo_scenario_receipt_report.md").write_text(report, encoding="utf-8")


def run(seed: int) -> dict[str, Any]:
    results = _evaluate(seed)
    _write_json(ARTIFACTS / f"{PREFIX}_results.json", results)
    _write_json(
        ARTIFACTS / f"{PREFIX}_state.json",
        {
            "report": REPORT,
            "seed": seed,
            "boundary": BOUNDARY,
            "maintained_shell": "visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html",
            "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
            "receipt_fields": results["receipt_fields"],
        },
    )
    _write_csv(ARTIFACTS / f"{PREFIX}_criteria.csv", results["criteria"])
    _write_csv(ARTIFACTS / f"{PREFIX}_summary.csv", [{"metric": key, "value": value} for key, value in results["metrics"].items()])
    _write_csv(
        ARTIFACTS / f"{PREFIX}_verdict.csv",
        [
            {
                "report": REPORT,
                "verdict": results["verdict"],
                "readiness": results["metrics"]["readiness"],
                "weakest_channel_score": results["metrics"]["weakest_channel_score"],
                "browser_receipt_score": results["metrics"]["browser_receipt_score"],
                "next_gate": NEXT_GATE,
            }
        ],
    )
    _write_report(results)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    print(
        json.dumps(
            {
                "report": results["report"],
                "verdict": results["verdict"],
                "readiness": round(results["metrics"]["readiness"], 6),
                "weakest_channel_score": round(results["metrics"]["weakest_channel_score"], 6),
                "browser_receipt_score": round(results["metrics"]["browser_receipt_score"], 6),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
