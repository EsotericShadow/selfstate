"""Report 308: SSRM-3D browser world v68 primary demo reviewer triage filter.

This report hardens the single primary browser-world demo by adding reviewer-facing
filters for the browser-local manual defect ledger. It is not a new simulation organ;
it makes real manual playtest evidence easier to inspect without forking the world.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 308
PREFIX = "ssrm_3d_browser_world_v68_primary_demo_reviewer_triage_filter"
DEFAULT_SEED = 20270706

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
DEMO_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo"
INDEX = DEMO_DIR / "index.html"
DEMO_JS = DEMO_DIR / "demo.js"
TRIAGE_JS = DEMO_DIR / "triage_filters.js"
QA_MANIFEST = DEMO_DIR / "qa_manifest.json"
README = DEMO_DIR / "README.md"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local reviewer workflow only: no LLM calls, no subjective consciousness, "
    "no autonomous natural language, no moral patienthood, no production persistence, no finished "
    "gameplay claim, and no claim that a filtered defect ledger proves agent interiority."
)

NEXT_GATE = (
    "post-308: use the filtered ledger during a full manual playtest pass, then fix one blocking "
    "defect in the maintained shell only if the ledger shows a reproducible issue"
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
    return Criterion(
        channel=channel,
        passed=passed,
        score=1.0 if passed else partial,
        evidence=evidence,
        failure_if_false=failure_if_false,
    )


def _evaluate(seed: int) -> dict[str, Any]:
    index = _read(INDEX)
    demo_js = _read(DEMO_JS)
    triage_js = _read(TRIAGE_JS)
    qa_manifest = _load_json(QA_MANIFEST)
    readme = _read(README)
    browser = _load_json(BROWSER_EVIDENCE)

    criteria = [
        _criterion(
            "single_primary_surface",
            "../ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html" in index,
            "primary launcher still targets the maintained v61 shell rather than a forked world",
            "reviewers would inspect a parallel surface instead of the consolidated demo",
        ),
        _criterion(
            "visible_boundary",
            all(term in index for term in ["no subjective consciousness", "no LLM call", "no finished gameplay"]),
            "launcher boundary remains visible before play",
            "reviewer workflow could overclaim the demo's status",
        ),
        _criterion(
            "recorder_schema_retained",
            all(term in demo_js for term in [
                "ssrm_primary_demo_manual_pass_records",
                "ssrm_primary_demo_defect_ledger",
                "resolutionNote",
                "resolvedAt",
            ]),
            "manual recorder and Report 307 resolution fields remain in the primary demo script",
            "filtering would replace or weaken the existing recorder ledger",
        ),
        _criterion(
            "triage_script_bound",
            "triage_filters.js" in index and TRIAGE_JS.exists(),
            "primary demo loads a separate reviewer filter script after the recorder script",
            "filter controls would exist only as inert markup or generated drift",
        ),
        _criterion(
            "status_filter_paths",
            all(term in index + triage_js for term in [
                'data-triage-status="all"',
                'data-triage-status="open"',
                'data-triage-status="resolved"',
            ]),
            "all/open/resolved filter paths are present in generated markup and script",
            "reviewers could not separate unresolved defects from closed evidence",
        ),
        _criterion(
            "severity_filter_paths",
            all(term in index + triage_js for term in ["defectSeverityFilter", "blocking", "minor", "watch"]),
            "severity filtering supports watch, minor, and blocking categories",
            "blocking issues would be buried in a flat ledger",
        ),
        _criterion(
            "persistent_filter_state",
            "ssrm_primary_demo_defect_filter_state" in triage_js and "writeFilter" in triage_js,
            "reviewer filter preference persists in browser-local storage",
            "reloads would erase reviewer triage context during a manual pass",
        ),
        _criterion(
            "shared_defect_ledger",
            "ssrm_primary_demo_defect_ledger" in triage_js and "readLedger" in triage_js,
            "filters read the same ledger key used by the manual recorder",
            "the dashboard would inspect a different source than the recorder writes",
        ),
        _criterion(
            "record_resolve_refresh",
            all(term in triage_js for term in ["recordDefect", "resolveLatestDefect", "setTimeout(render, 0)"]),
            "dashboard refreshes after recording and resolving defects",
            "reviewers would need reloads to trust the filtered counts",
        ),
        _criterion(
            "escaped_ledger_rendering",
            all(term in triage_js for term in ["escapeText", "&lt;", "resolutionNote"]),
            "defect notes and resolution text are escaped before rendering",
            "a local defect note could inject markup into the reviewer page",
        ),
        _criterion(
            "count_dashboard",
            all(term in triage_js for term in ["blocking open", "resolved", "filtered.length"]),
            "summary shows filtered count, open count, resolved count, and blocking-open count",
            "the ledger would remain a hard-to-review freeform record",
        ),
        _criterion(
            "empty_state",
            "No defects match the current reviewer filter" in triage_js,
            "filter dashboard has a clear empty state",
            "reviewers could confuse no matching defects with a broken dashboard",
        ),
        _criterion(
            "qa_manifest_survives",
            "defect_triage_fields" in qa_manifest and "resolutionNote" in json.dumps(qa_manifest),
            "generated QA manifest still advertises triage fields from Report 307",
            "runner metadata would lose the existing defect-resolution contract",
        ),
        _criterion(
            "generated_readme_boundary",
            "primary demo" in readme.lower() and "browser-local" in readme.lower(),
            "generated demo README keeps the local primary-demo boundary visible",
            "reviewers would lack local context when opening the demo package directly",
        ),
    ]

    browser_workflow = browser.get("workflow_pass") is True
    if browser.get("missing"):
        browser_score = 0.0
        browser_evidence = "browser evidence artifact missing until the direct browser pass writes it"
    else:
        browser_score = 1.0 if browser_workflow else 0.0
        browser_evidence = f"browser workflow_pass={browser.get('workflow_pass')} console_errors={browser.get('console_errors')}"
    criteria.append(
        Criterion(
            channel="direct_browser_workflow",
            passed=browser_workflow,
            score=browser_score,
            evidence=browser_evidence,
            failure_if_false="source checks alone would not prove the reviewer filter works in a browser",
        )
    )

    scores = [criterion.score for criterion in criteria]
    passed_required = all(criterion.passed for criterion in criteria if criterion.channel != "direct_browser_workflow")
    readiness = mean(scores)
    weakest = min(scores)
    verdict = "pass" if readiness >= 0.92 and weakest >= 0.8 and passed_required and browser_workflow else "needs_browser_evidence"

    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "source_static_pass_rate": mean([c.score for c in criteria if c.channel != "direct_browser_workflow"]),
        "review_filter_coverage": mean([
            c.score for c in criteria if c.channel in {
                "status_filter_paths",
                "severity_filter_paths",
                "persistent_filter_state",
                "shared_defect_ledger",
                "record_resolve_refresh",
                "count_dashboard",
                "empty_state",
            }
        ]),
        "single_surface_score": next(c.score for c in criteria if c.channel == "single_primary_surface"),
        "browser_workflow_score": browser_score,
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
        "criteria": [asdict(c) for c in criteria],
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "browser_evidence": browser,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "state": f"artifacts/{PREFIX}_state.json",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v68_primary_demo_reviewer_triage_filter_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    browser = results["browser_evidence"]
    if browser.get("missing"):
        browser_line = "Direct browser evidence is not present yet; run the browser pass and rerun this module."
    else:
        browser_line = (
            f"Direct browser workflow pass: `{browser.get('workflow_pass')}`; "
            f"console errors: `{browser.get('console_errors')}`; "
            f"status filter evidence: `{browser.get('status_filter_evidence')}`; "
            f"severity filter evidence: `{browser.get('severity_filter_evidence')}`."
        )
    report = f"""# Report 308: SSRM-3D Browser World v68 Primary Demo Reviewer Triage Filter

## Purpose

Report 308 keeps consolidation pressure on the single playable browser-world surface. It adds a reviewer-facing filter dashboard for the browser-local manual defect ledger created in Reports 305-307, so a real playtest can separate open, resolved, watch, minor, and blocking issues without forking the demo or hiding defects in prose.

This is not a new simulation organ. It is a usability and evidence-inspection hardening pass for the primary demo path.

## Boundary

{results['boundary']}

## What changed

- The primary demo launcher now loads `triage_filters.js` after `demo.js`.
- The manual recorder UI now exposes all/open/resolved status filters.
- The defect ledger view now exposes severity filtering for watch/minor/blocking defects.
- The dashboard reads the same `ssrm_primary_demo_defect_ledger` key as the recorder and persists reviewer filter state in `ssrm_primary_demo_defect_filter_state`.
- Defect notes and resolution notes are escaped before display.
- Counts show filtered, total, open, resolved, and blocking-open defects.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| source_static_pass_rate | {metrics['source_static_pass_rate']:.6f} |
| review_filter_coverage | {metrics['review_filter_coverage']:.6f} |
| browser_workflow_score | {metrics['browser_workflow_score']:.6f} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

{browser_line}

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

The report should only be treated as passed when the direct browser workflow evidence is present. Static source checks are useful, but this specific report is about a visible reviewer workflow.

## Next gate

{results['next_gate']}
"""
    path = DOCS / f"{REPORT}_ssrm_3d_browser_world_v68_primary_demo_reviewer_triage_filter_report.md"
    path.write_text(report, encoding="utf-8")


def run(seed: int) -> dict[str, Any]:
    results = _evaluate(seed)
    _write_json(ARTIFACTS / f"{PREFIX}_results.json", results)
    _write_json(ARTIFACTS / f"{PREFIX}_state.json", {
        "report": REPORT,
        "seed": seed,
        "boundary": BOUNDARY,
        "demo_dir": str(DEMO_DIR.relative_to(ROOT)),
        "filter_script": str(TRIAGE_JS.relative_to(ROOT)),
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
    })
    _write_csv(ARTIFACTS / f"{PREFIX}_criteria.csv", results["criteria"])
    _write_csv(ARTIFACTS / f"{PREFIX}_summary.csv", [{"metric": key, "value": value} for key, value in results["metrics"].items()])
    _write_csv(ARTIFACTS / f"{PREFIX}_verdict.csv", [{
        "report": REPORT,
        "verdict": results["verdict"],
        "readiness": results["metrics"]["readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "browser_workflow_score": results["metrics"]["browser_workflow_score"],
        "next_gate": NEXT_GATE,
    }])
    _write_report(results)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    print(json.dumps({
        "report": REPORT,
        "verdict": results["verdict"],
        "readiness": results["metrics"]["readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "browser_workflow_score": results["metrics"]["browser_workflow_score"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
