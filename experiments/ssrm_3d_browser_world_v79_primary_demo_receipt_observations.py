"""Report 319: SSRM-3D browser world v79 primary demo receipt observations.

This report makes the integrated scenario receipt actionable for outside review. Reviewers
can attach public observations to receipt fields, resolve the latest observation, and see
the observation ledger persist through the primary-demo resume path.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 319
PREFIX = "ssrm_3d_browser_world_v79_primary_demo_receipt_observations"
DEFAULT_SEED = 20270717

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V61_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening.py"
V61_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
V61_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local receipt-observation consolidation only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, "
    "no complete 3D engine, and no finished gameplay claim. Observations are public review notes over "
    "public state, not private experience."
)

NEXT_GATE = (
    "post-319: use the receipt observation ledger to drive a reviewer-ready defect summary that separates "
    "open, watch, resolved, and blocking observations without leaving the primary shell"
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
    required_terms = [
        "RECEIPT_OBSERVATION_KEY",
        "logReceiptObservation",
        "resolveLatestObservation",
        "formatReceiptObservations",
        "receiptFieldSelect",
        "receiptSeveritySelect",
    ]

    criteria = [
        _criterion(
            "observation_panel_present",
            "receiptObservationOut" in index and "Receipt observations" in index,
            "maintained shell exposes a receipt-observation panel",
            "reviewers would still need external notes for receipt-field comments",
        ),
        _criterion(
            "generated_source_of_truth",
            all(term in gen for term in required_terms),
            "receipt-observation actions and persistence are generated from the maintained v61 source",
            "regeneration would erase the observation ledger",
        ),
        _criterion(
            "receipt_field_binding",
            "receiptFieldIds" in app and "Receipt field" in index and "Observation severity" in index,
            "observation UI binds notes to explicit receipt fields and severity",
            "observations would not be field-tied or severity-visible",
        ),
        _criterion(
            "public_review_ledger",
            all(term in app for term in ["Receipt observation ledger", "Persistent key", "publicReceipt", "receiptStatus"]),
            "ledger output exposes public persistence and receipt PASS/FAIL status",
            "review notes would be opaque or detached from receipt status",
        ),
        _criterion(
            "browser_observation_logged",
            browser.get("observation_logged_pass") is True,
            str(browser.get("observation_logged_evidence", "missing logged-observation evidence")),
            "browser flow did not visibly log a receipt observation",
        ),
        _criterion(
            "browser_observation_resolved",
            browser.get("observation_resolved_pass") is True,
            str(browser.get("observation_resolved_evidence", "missing resolved-observation evidence")),
            "browser flow did not visibly resolve the latest receipt observation",
        ),
        _criterion(
            "browser_transcript_checkpoint_visible",
            browser.get("transcript_checkpoint_pass") is True,
            str(browser.get("transcript_checkpoint_evidence", "missing transcript/checkpoint evidence")),
            "observation actions were not visible in replay transcript and checkpoints",
        ),
        _criterion(
            "browser_receipt_linkage",
            browser.get("receipt_linkage_pass") is True,
            str(browser.get("receipt_linkage_evidence", "missing receipt linkage evidence")),
            "observation ledger did not remain linked to the all-pass integrated receipt",
        ),
        _criterion(
            "browser_resume_persistence",
            browser.get("resume_persistence_pass") is True,
            str(browser.get("resume_persistence_evidence", "missing resume evidence")),
            "receipt observations did not persist through leave/resume",
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
        "observation_panel_score": next(row.score for row in criteria if row.channel == "observation_panel_present"),
        "browser_observation_score": next(row.score for row in criteria if row.channel == "browser_observation_logged"),
        "console_errors": browser.get("console_errors", -1),
        "criterion_count": len(criteria),
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
        "required_terms": required_terms,
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "browser_evidence": browser,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "state": f"artifacts/{PREFIX}_state.json",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v79_primary_demo_receipt_observations_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 319: SSRM-3D Browser World v79 Primary Demo Receipt Observations

## Purpose

Report 319 makes the integrated scenario receipt actionable for outside reviewers. The maintained shell now lets a reviewer attach a public observation to a specific receipt field, resolve the latest observation, and verify the ledger through replay/checkpoint/resume evidence.

This is review-loop consolidation, not a new simulation branch.

## Boundary

{results['boundary']}

## What changed

- Added a `Receipt observations` panel to the maintained v61 shell.
- Added receipt-field and severity selectors.
- Added `Log observation` and `Resolve latest` actions.
- Stored observations in a browser-local public ledger keyed to receipt field, severity, receipt PASS/FAIL status, selected resident, and replay rows.
- Verified observation logging, resolution, transcript/checkpoint visibility, receipt linkage, and resume persistence in browser.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| observation_panel_score | {metrics['observation_panel_score']:.6f} |
| browser_observation_score | {metrics['browser_observation_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- observation_logged_pass: `{browser.get('observation_logged_pass')}`
- observation_resolved_pass: `{browser.get('observation_resolved_pass')}`
- transcript_checkpoint_pass: `{browser.get('transcript_checkpoint_pass')}`
- receipt_linkage_pass: `{browser.get('receipt_linkage_pass')}`
- resume_persistence_pass: `{browser.get('resume_persistence_pass')}`
- console_errors: `{browser.get('console_errors')}`
- logged evidence: `{browser.get('observation_logged_evidence')}`
- resolved evidence: `{browser.get('observation_resolved_evidence')}`
- transcript/checkpoint evidence: `{browser.get('transcript_checkpoint_evidence')}`
- receipt linkage evidence: `{browser.get('receipt_linkage_evidence')}`
- resume evidence: `{browser.get('resume_persistence_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

The observation ledger is a public audit affordance over deterministic browser-local state. It does not claim subjective experience, moral status, autonomous language, production persistence, complete gameplay, or a complete 3D engine.

## Next gate

{results['next_gate']}
"""
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v79_primary_demo_receipt_observations_report.md").write_text(report, encoding="utf-8")


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
            "required_terms": results["required_terms"],
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
                "browser_observation_score": results["metrics"]["browser_observation_score"],
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
                "browser_observation_score": round(results["metrics"]["browser_observation_score"], 6),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
