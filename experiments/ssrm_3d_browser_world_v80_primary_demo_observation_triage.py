"""Report 320: SSRM-3D browser world v80 primary demo observation triage.

This report makes the receipt-observation ledger reviewer-ready by adding in-shell triage
filters and counts for all, open, watch, resolved, and blocking receipt observations.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 320
PREFIX = "ssrm_3d_browser_world_v80_primary_demo_observation_triage"
DEFAULT_SEED = 20270718

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V61_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening.py"
V61_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
V61_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local observation-triage consolidation only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, "
    "no complete 3D engine, and no finished gameplay claim. Triage filters organize public review notes; "
    "they do not create autonomous debugging."
)

NEXT_GATE = (
    "post-320: condense the primary shell into an outside-reviewer landing path that exposes only the "
    "integrated loop, receipt, observation triage, transcript, and boundary before optional deep panels"
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
        "observationTriageOut",
        "OBSERVATION_FILTER_KEY",
        "setObservationFilterOpen",
        "setObservationFilterWatch",
        "setObservationFilterResolved",
        "setObservationFilterBlocking",
        "formatObservationTriage",
    ]

    criteria = [
        _criterion(
            "triage_panel_present",
            "observationTriageOut" in index and "Observation triage" in index,
            "maintained shell exposes an observation triage panel",
            "reviewers would still need to scan receipt observations manually",
        ),
        _criterion(
            "generated_source_of_truth",
            all(term in gen for term in required_terms),
            "triage filters and formatter are generated from the maintained v61 source",
            "regeneration would erase observation triage",
        ),
        _criterion(
            "filter_controls_present",
            all(term in index for term in ["setObservationFilterAll", "setObservationFilterOpen", "setObservationFilterWatch", "setObservationFilterResolved", "setObservationFilterBlocking"]),
            "all/open/watch/resolved/blocking filter controls are visible in the shell",
            "triage would not separate the reviewer states required by the next gate",
        ),
        _criterion(
            "public_count_summary",
            all(term in app for term in ["Counts: total", "Visible rows", "blocking", "resolved", "watch"]),
            "triage output summarizes counts and visible rows from public observation state",
            "reviewers would not see count-level status without raw storage",
        ),
        _criterion(
            "browser_filter_counts_visible",
            browser.get("filter_counts_visible_pass") is True,
            str(browser.get("filter_counts_visible_evidence", "missing filter count evidence")),
            "browser flow did not show observation counts for all/open/watch/resolved/blocking",
        ),
        _criterion(
            "browser_open_watch_blocking_filters",
            browser.get("open_watch_blocking_pass") is True,
            str(browser.get("open_watch_blocking_evidence", "missing open/watch/blocking evidence")),
            "browser flow did not separate open, watch, and blocking observations",
        ),
        _criterion(
            "browser_resolved_filter",
            browser.get("resolved_filter_pass") is True,
            str(browser.get("resolved_filter_evidence", "missing resolved filter evidence")),
            "browser flow did not show resolved observation filtering",
        ),
        _criterion(
            "browser_transcript_checkpoint_visible",
            browser.get("transcript_checkpoint_pass") is True,
            str(browser.get("transcript_checkpoint_evidence", "missing transcript/checkpoint evidence")),
            "filter changes were not visible in replay transcript and checkpoints",
        ),
        _criterion(
            "browser_resume_persistence",
            browser.get("resume_persistence_pass") is True,
            str(browser.get("resume_persistence_evidence", "missing resume evidence")),
            "observation triage filter/count state did not persist through leave/resume",
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
        "triage_panel_score": next(row.score for row in criteria if row.channel == "triage_panel_present"),
        "browser_filter_score": next(row.score for row in criteria if row.channel == "browser_filter_counts_visible"),
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
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v80_primary_demo_observation_triage_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 320: SSRM-3D Browser World v80 Primary Demo Observation Triage

## Purpose

Report 320 makes the receipt-observation ledger usable for outside review by adding in-shell triage filters and counts for all, open, watch, resolved, and blocking observations.

This is reviewer workflow consolidation, not a new simulation branch.

## Boundary

{results['boundary']}

## What changed

- Added an `Observation triage` panel to the maintained v61 shell.
- Added `All`, `Open`, `Watch`, `Resolved`, and `Blocking` filter buttons.
- Added visible counts for total, open, watch, minor, blocking, and resolved observations.
- Persisted the active filter in browser-local public state.
- Verified filter counts, open/watch/blocking separation, resolved filtering, transcript/checkpoint visibility, resume persistence, and console cleanliness in browser.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| triage_panel_score | {metrics['triage_panel_score']:.6f} |
| browser_filter_score | {metrics['browser_filter_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- filter_counts_visible_pass: `{browser.get('filter_counts_visible_pass')}`
- open_watch_blocking_pass: `{browser.get('open_watch_blocking_pass')}`
- resolved_filter_pass: `{browser.get('resolved_filter_pass')}`
- transcript_checkpoint_pass: `{browser.get('transcript_checkpoint_pass')}`
- resume_persistence_pass: `{browser.get('resume_persistence_pass')}`
- console_errors: `{browser.get('console_errors')}`
- filter count evidence: `{browser.get('filter_counts_visible_evidence')}`
- open/watch/blocking evidence: `{browser.get('open_watch_blocking_evidence')}`
- resolved evidence: `{browser.get('resolved_filter_evidence')}`
- transcript/checkpoint evidence: `{browser.get('transcript_checkpoint_evidence')}`
- resume evidence: `{browser.get('resume_persistence_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

Observation triage remains a public audit affordance over deterministic browser-local state. It does not claim subjective experience, moral status, autonomous debugging, production persistence, complete gameplay, or a complete 3D engine.

## Next gate

{results['next_gate']}
"""
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v80_primary_demo_observation_triage_report.md").write_text(report, encoding="utf-8")


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
                "browser_filter_score": results["metrics"]["browser_filter_score"],
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
                "browser_filter_score": round(results["metrics"]["browser_filter_score"], 6),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
