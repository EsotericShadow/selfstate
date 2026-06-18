"""Report 322: SSRM-3D browser world v82 primary demo actionable landing failures.

This report makes the reviewer landing useful before the receipt passes: failing
receipt fields now show concrete recovery actions and can be captured as blocking
observation rows without leaving reviewer-focus mode.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 322
PREFIX = "ssrm_3d_browser_world_v82_primary_demo_actionable_landing_failures"
DEFAULT_SEED = 20270720

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V61_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening.py"
V61_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
V61_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
V61_CSS = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "styles.css"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local landing-failure actionability only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, "
    "no complete 3D engine, and no finished gameplay claim. The failure map is reviewer guidance over "
    "public receipt state, not autonomous debugging or hidden cognition."
)

NEXT_GATE = (
    "post-322: make the reviewer-first shell more handoff-ready by packaging the launcher, landing, "
    "manual script, receipt, observation triage, and boundary into one outside-review checklist"
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
    css = _read(V61_CSS)
    browser = _load_json(BROWSER_EVIDENCE)
    source_terms = [
        "reviewerFailureActionBook",
        "reviewerFailureActions",
        "auditLandingFailures",
        "Actionable failure map",
        "Deep diagnostics",
    ]
    criteria = [
        _criterion(
            "failure_action_map_generated",
            all(term in gen for term in source_terms) and all(term in app for term in source_terms),
            "reviewer landing failure map is generated from the maintained source and present in app.js",
            "regeneration would erase actionable failure guidance",
        ),
        _criterion(
            "audit_failures_action_present",
            "data-action=\"auditLandingFailures\"" in index and "function auditLandingFailures" in app,
            "landing panel includes an Audit failures action wired to app logic",
            "reviewers could read failures but not capture them as review state",
        ),
        _criterion(
            "blocking_observation_route",
            all(term in app for term in ["severity: 'blocking'", "receiptStatus: 'FAIL'", "setItem(OBSERVATION_FILTER_KEY, 'blocking')"]),
            "failure audit records current failing receipt fields as blocking observations and opens the blocking triage filter",
            "failed receipt fields would not become triageable reviewer work items",
        ),
        _criterion(
            "deep_panels_preserved",
            index.count("deep-panel") >= 8 and "toggleDeepPanels" in app and "body.reviewer-focus .deep-panel" in css,
            "optional diagnostics remain hidden by default but revealable on demand",
            "actionability would either bury reviewers in debug panels or remove diagnostic access",
        ),
        _criterion(
            "browser_ready_failure_map",
            browser.get("ready_failure_map_pass") is True,
            str(browser.get("ready_failure_map_evidence", "missing ready failure map evidence")),
            "browser did not show field-level recovery actions on a clean failing landing",
        ),
        _criterion(
            "browser_audit_blocks_failures",
            browser.get("audit_blocks_failures_pass") is True,
            str(browser.get("audit_blocks_failures_evidence", "missing failure audit evidence")),
            "browser did not convert failing fields into blocking observation rows",
        ),
        _criterion(
            "browser_pass_clears_failure_map",
            browser.get("pass_clears_failure_map_pass") is True,
            str(browser.get("pass_clears_failure_map_evidence", "missing pass-clears evidence")),
            "browser did not replace failure guidance with all-pass guidance after reviewer pass",
        ),
        _criterion(
            "browser_deep_toggle_after_audit",
            browser.get("deep_toggle_after_audit_pass") is True,
            str(browser.get("deep_toggle_after_audit_evidence", "missing deep toggle evidence")),
            "optional diagnostic panels were not revealable after auditing failures",
        ),
        _criterion(
            "browser_resume_actionability",
            browser.get("resume_actionability_pass") is True,
            str(browser.get("resume_actionability_evidence", "missing resume actionability evidence")),
            "landing actionability did not persist through launcher resume",
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
        "failure_action_map_score": next(row.score for row in criteria if row.channel == "failure_action_map_generated"),
        "browser_audit_score": next(row.score for row in criteria if row.channel == "browser_audit_blocks_failures"),
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
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v82_primary_demo_actionable_landing_failures_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 322: SSRM-3D Browser World v82 Primary Demo Actionable Landing Failures

## Purpose

Report 322 makes the reviewer landing useful when the integrated receipt is not passing yet. Instead of only showing `READY_FOR_RUN`, the landing now maps each failing public receipt field to a concrete recovery action and can convert the current failure set into blocking observation rows.

This is consolidation of the review workflow in the maintained playable shell, not a new simulation branch.

## Boundary

{results['boundary']}

## What changed

- Added a field-level `Actionable failure map` to the reviewer landing output.
- Added recovery guidance for entry, schedule, debt, offscreen life, trust repair, resident social memory, public history, replay export, and resume snapshot fields.
- Added `Audit failures`, which records the current failing receipt fields as blocking receipt observations and switches observation triage to the blocking filter.
- Preserved reviewer-focus mode and optional deep-panel reveal, so actionability does not force reviewers into the debug surface.
- Verified clean failure guidance, blocking observation creation, all-pass guidance after reviewer pass, deep-panel reveal after audit, resume actionability, and console cleanliness in browser.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| failure_action_map_score | {metrics['failure_action_map_score']:.6f} |
| browser_audit_score | {metrics['browser_audit_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- ready_failure_map_pass: `{browser.get('ready_failure_map_pass')}`
- audit_blocks_failures_pass: `{browser.get('audit_blocks_failures_pass')}`
- pass_clears_failure_map_pass: `{browser.get('pass_clears_failure_map_pass')}`
- deep_toggle_after_audit_pass: `{browser.get('deep_toggle_after_audit_pass')}`
- resume_actionability_pass: `{browser.get('resume_actionability_pass')}`
- console_errors: `{browser.get('console_errors')}`
- ready evidence: `{browser.get('ready_failure_map_evidence')}`
- audit evidence: `{browser.get('audit_blocks_failures_evidence')}`
- pass evidence: `{browser.get('pass_clears_failure_map_evidence')}`
- deep toggle evidence: `{browser.get('deep_toggle_after_audit_evidence')}`
- resume evidence: `{browser.get('resume_actionability_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

The result keeps the claim narrow: it improves reviewer workflow over deterministic public browser state. It does not claim subjective consciousness, autonomous debugging, moral status, production readiness, complete gameplay, or a complete 3D engine.

## Next gate

{results['next_gate']}
"""
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v82_primary_demo_actionable_landing_failures_report.md").write_text(report, encoding="utf-8")


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
            "actionable_landing_path": [
                "open reviewer landing in default reviewer-focus mode",
                "read Actionable failure map when receipt is incomplete",
                "click Audit failures to create blocking observation rows",
                "use Observation triage blocking filter without opening deep diagnostics",
                "toggle deep panels only if trace detail is needed",
                "run reviewer pass and confirm all-pass guidance replaces failure guidance",
            ],
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
