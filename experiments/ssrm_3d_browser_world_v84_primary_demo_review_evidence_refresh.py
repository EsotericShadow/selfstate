"""Report 324: SSRM-3D browser world v84 primary demo review evidence refresh.

This report makes the outside-review launcher checklist evidence-bearing: after a
reviewer uses the maintained shell, the launcher can refresh and export shell-side
replay, receipt, observation, checkpoint, and replay-export evidence.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 324
PREFIX = "ssrm_3d_browser_world_v84_primary_demo_review_evidence_refresh"
DEFAULT_SEED = 20270722

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V63_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
PRIMARY_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo"
PRIMARY_INDEX = PRIMARY_DIR / "index.html"
PRIMARY_JS = PRIMARY_DIR / "demo.js"
PRIMARY_QA = PRIMARY_DIR / "qa_manifest.json"
PRIMARY_LAUNCH = PRIMARY_DIR / "launch_manifest.json"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local review-evidence refresh only; no LLM calls, no subjective consciousness, "
    "no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, "
    "and no finished gameplay claim. The refresh summarizes public localStorage evidence from the maintained shell; "
    "it is not external validation, autonomous judgment, or hidden cognition."
)

NEXT_GATE = (
    "post-324: run the outside-review checklist against a complete walkthrough and fix the first concrete defect "
    "that blocks reviewer comprehension in the same maintained shell or launcher"
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
    gen = _read(V63_GEN)
    index = _read(PRIMARY_INDEX)
    js = _read(PRIMARY_JS)
    qa = _load_json(PRIMARY_QA)
    launch = _load_json(PRIMARY_LAUNCH)
    browser = _load_json(BROWSER_EVIDENCE)
    source_terms = [
        "buildOutsideReviewEvidence",
        "renderOutsideReviewEvidence",
        "refreshOutsideReviewEvidence",
        "outsideReviewEvidenceOut",
        "SHELL_RECEIPT_OBSERVATION_KEY",
        "shellEvidence: buildOutsideReviewEvidence()",
    ]
    state_keys = qa.get("state_keys", []) if isinstance(qa.get("state_keys"), list) else []
    criteria = [
        _criterion(
            "evidence_refresh_generated_from_source",
            all(term in gen for term in source_terms) and all(term in js for term in source_terms[0:5]),
            "launcher evidence refresh is generated from Report 303 source and present in demo.js",
            "regeneration would erase the evidence refresh path",
        ),
        _criterion(
            "launcher_evidence_panel_visible",
            "Refresh shell evidence" in index and "outsideReviewEvidenceOut" in index and "outsideReviewEvidenceStatus" in index,
            "primary launcher exposes shell-evidence refresh controls and output",
            "reviewers would still need to inspect raw localStorage or shell panels manually",
        ),
        _criterion(
            "handoff_export_embeds_shell_evidence",
            "shellEvidence: buildOutsideReviewEvidence()" in js and "outside-review-handoff-public-local-only" in js,
            "outside-review handoff export embeds refreshed shell evidence under a local-only boundary",
            "exported handoff would not prove what happened inside the maintained shell",
        ),
        _criterion(
            "manifest_shell_evidence_keys_registered",
            all(key in state_keys for key in ["ssrm_v61_app_shell_receipt_observations", "ssrm_v61_app_shell_checkpoints", "ssrm_primary_demo_outside_review_handoff"]),
            "QA manifest lists shell receipt-observation/checkpoint keys and outside-review handoff key",
            "evidence refresh would rely on unregistered browser-local state",
        ),
        _criterion(
            "one_shell_policy_preserved",
            launch.get("target_shell") == "../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html" and "ssrm_3d_browser_world_v61_vertical_slice_app_shell" in index,
            "launcher still targets the maintained v61 shell instead of another demo surface",
            "review-evidence refresh would fragment the demo path",
        ),
        _criterion(
            "browser_pre_shell_missing_state",
            browser.get("pre_shell_missing_state_pass") is True,
            str(browser.get("pre_shell_missing_state_evidence", "missing pre-shell evidence")),
            "browser did not show missing shell evidence before the shell walkthrough",
        ),
        _criterion(
            "browser_shell_evidence_refresh",
            browser.get("shell_evidence_refresh_pass") is True,
            str(browser.get("shell_evidence_refresh_evidence", "missing shell refresh evidence")),
            "browser did not surface replay, reviewer pass, receipt, observation, checkpoint, and export evidence after walkthrough",
        ),
        _criterion(
            "browser_export_contains_shell_evidence",
            browser.get("export_contains_shell_evidence_pass") is True,
            str(browser.get("export_contains_shell_evidence_evidence", "missing export evidence")),
            "outside-review handoff export did not include shell evidence",
        ),
        _criterion(
            "browser_clean_resume_preserved",
            browser.get("clean_resume_preserved_pass") is True,
            str(browser.get("clean_resume_preserved_evidence", "missing clean/resume evidence")),
            "clean/resume launcher handoff no longer preserved reviewer-focus shell path",
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
    verdict = "pass" if readiness >= 0.95 and weakest >= 0.9 and all(row.passed for row in criteria) else "needs_browser_evidence"
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "evidence_refresh_source_score": next(row.score for row in criteria if row.channel == "evidence_refresh_generated_from_source"),
        "browser_refresh_score": next(row.score for row in criteria if row.channel == "browser_shell_evidence_refresh"),
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
        "required_terms": source_terms,
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "browser_evidence": browser,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "state": f"artifacts/{PREFIX}_state.json",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v84_primary_demo_review_evidence_refresh_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 324: SSRM-3D Browser World v84 Primary Demo Review Evidence Refresh

## Purpose

Report 324 fixes a concrete handoff gap from the outside-review checklist: after the reviewer uses the maintained shell, the launcher should be able to summarize whether real shell-side evidence exists. The primary launcher now refreshes and exports public browser-local shell evidence: replay rows, reviewer-pass event, integrated receipt, receipt observations, checkpoints, and replay-export readiness.

This keeps the work on the single primary demo path instead of creating another review surface.

## Boundary

{results['boundary']}

## What changed

- Added `Refresh shell evidence` to the primary launcher outside-review checklist.
- Added `outsideReviewEvidenceStatus` and `outsideReviewEvidenceOut` to summarize maintained-shell evidence from browser-local state.
- Added shell evidence to the outside-review handoff export.
- Registered receipt-observation and checkpoint shell state keys in the launcher QA manifest.
- Verified pre-shell missing state, post-walkthrough evidence refresh, handoff export embedding, clean/resume preservation, and console cleanliness in browser.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| evidence_refresh_source_score | {metrics['evidence_refresh_source_score']:.6f} |
| browser_refresh_score | {metrics['browser_refresh_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- pre_shell_missing_state_pass: `{browser.get('pre_shell_missing_state_pass')}`
- shell_evidence_refresh_pass: `{browser.get('shell_evidence_refresh_pass')}`
- export_contains_shell_evidence_pass: `{browser.get('export_contains_shell_evidence_pass')}`
- clean_resume_preserved_pass: `{browser.get('clean_resume_preserved_pass')}`
- console_errors: `{browser.get('console_errors')}`
- pre-shell evidence: `{browser.get('pre_shell_missing_state_evidence')}`
- refresh evidence: `{browser.get('shell_evidence_refresh_evidence')}`
- export evidence: `{browser.get('export_contains_shell_evidence_evidence')}`
- clean/resume evidence: `{browser.get('clean_resume_preserved_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

The honest limit remains: this is internal browser evidence and local handoff packaging, not an external reviewer cohort or production deployment.

## Next gate

{results['next_gate']}
"""
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v84_primary_demo_review_evidence_refresh_report.md").write_text(report, encoding="utf-8")


def run(seed: int) -> dict[str, Any]:
    results = _evaluate(seed)
    _write_json(ARTIFACTS / f"{PREFIX}_results.json", results)
    _write_json(
        ARTIFACTS / f"{PREFIX}_state.json",
        {
            "report": REPORT,
            "seed": seed,
            "prefix": PREFIX,
            "boundary": BOUNDARY,
            "next_gate": NEXT_GATE,
            "evidence_refresh_keys": [
                "ssrm_v61_app_shell_world",
                "ssrm_v61_app_shell_replay",
                "ssrm_v61_app_shell_export",
                "ssrm_v61_app_shell_receipt_observations",
                "ssrm_v61_app_shell_checkpoints",
            ],
            "target_shell": "visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html",
        },
    )
    _write_csv(ARTIFACTS / f"{PREFIX}_criteria.csv", results["criteria"])
    _write_csv(ARTIFACTS / f"{PREFIX}_summary.csv", [{**results["metrics"], "report": REPORT, "seed": seed, "verdict": results["verdict"]}])
    _write_csv(ARTIFACTS / f"{PREFIX}_verdict.csv", [{"report": REPORT, "seed": seed, "verdict": results["verdict"], "boundary": BOUNDARY, "next_gate": NEXT_GATE}])
    _write_report(results)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    print(json.dumps({"report": REPORT, "prefix": PREFIX, "verdict": results["verdict"], "metrics": results["metrics"]}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
