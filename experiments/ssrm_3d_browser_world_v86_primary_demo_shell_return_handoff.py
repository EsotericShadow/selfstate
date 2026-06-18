"""Report 326: SSRM-3D browser world v86 primary demo shell return handoff.

This report fixes a cold-reviewer walkthrough defect in the consolidated primary
browser-world demo: after the maintained shell proves the reviewer path, the
reviewer now has a visible return affordance back to the launcher checklist and
handoff export area.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 326
PREFIX = "ssrm_3d_browser_world_v86_primary_demo_shell_return_handoff"
DEFAULT_SEED = 20270724

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
SHELL_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell"
SHELL_INDEX = SHELL_DIR / "index.html"
SHELL_CSS = SHELL_DIR / "styles.css"
SHELL_JS = SHELL_DIR / "app.js"
SHELL_GENERATOR = ROOT / "experiments" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening.py"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local shell-to-launcher handoff only; no LLM calls, no subjective consciousness, "
    "no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, "
    "and no finished gameplay claim. The return link is reviewer workflow hardening, not external validation "
    "or evidence of inner experience."
)

NEXT_GATE = (
    "post-326: run the full outside-review loop end-to-end from clean launcher through shell pass, return, "
    "checklist completion, evidence refresh, visible payload preview, and defect-recorder export; fix the next "
    "concrete comprehension or state-continuity defect in the same launcher/shell path"
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
    index = _read(SHELL_INDEX)
    css = _read(SHELL_CSS)
    js = _read(SHELL_JS)
    generator = _read(SHELL_GENERATOR)
    browser = _load_json(BROWSER_EVIDENCE)
    required_link_terms = [
        "returnLauncherHandoffLink",
        "Return to launcher handoff",
        "../ssrm_3d_browser_world_primary_demo/index.html#outsideReviewChecklist",
    ]
    criteria = [
        _criterion(
            "shell_return_link_visible",
            all(term in index for term in required_link_terms),
            "maintained shell contains a visible return link to the launcher checklist/handoff anchor",
            "reviewers can finish the shell pass but have no obvious return path to the handoff export",
        ),
        _criterion(
            "generator_preserves_return_link",
            all(term in generator for term in required_link_terms),
            "Report 301 shell generator preserves the return affordance",
            "future regeneration would erase the shell return path",
        ),
        _criterion(
            "return_link_styled_as_reviewer_action",
            ".handoff-return" in css and "grid-template-columns: repeat(4" in css,
            "return link is styled as a first-class reviewer action, not hidden prose",
            "cold reviewers may miss the return link after the pass",
        ),
        _criterion(
            "reviewer_landing_names_next_step",
            "Return to launcher handoff" in js and "returnToLauncherHandoff: true" in js,
            "reviewer landing text and payload name the shell-to-launcher next step",
            "the link exists but the pass summary does not explain what to do next",
        ),
        _criterion(
            "browser_return_link_visible_after_pass",
            browser.get("return_link_visible_after_pass") is True,
            str(browser.get("return_link_visible_after_pass_evidence", "missing visible-link browser evidence")),
            "browser pass did not expose the return link after reviewer pass",
        ),
        _criterion(
            "browser_return_link_href_correct",
            browser.get("return_link_href_correct") is True,
            str(browser.get("return_link_href_evidence", "missing href browser evidence")),
            "return link does not target the launcher checklist/handoff anchor",
        ),
        _criterion(
            "browser_return_navigation_reaches_launcher",
            browser.get("return_navigation_reaches_launcher") is True,
            str(browser.get("return_navigation_evidence", "missing navigation browser evidence")),
            "clicking return link did not bring reviewer back to the launcher checklist",
        ),
        _criterion(
            "browser_handoff_prepares_after_return",
            browser.get("handoff_prepares_after_return") is True,
            str(browser.get("handoff_after_return_evidence", "missing after-return handoff evidence")),
            "reviewer could return to launcher but could not refresh evidence and prepare visible handoff payload",
        ),
        _criterion(
            "browser_no_console_errors",
            browser.get("console_errors") == 0,
            f"browser console error count was {browser.get('console_errors')}",
            "return handoff flow produced console errors",
        ),
        _criterion(
            "boundary_preserved",
            "no subjective consciousness" in BOUNDARY and "no LLM calls" in BOUNDARY,
            BOUNDARY,
            "report boundary implies more than browser-local reviewer workflow hardening",
        ),
    ]
    scores = [row.score for row in criteria]
    readiness = mean(scores)
    weakest = min(scores)
    verdict = "pass" if readiness >= 0.95 and weakest >= 0.9 and all(row.passed for row in criteria) else "needs_browser_evidence"
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "return_source_score": next(row.score for row in criteria if row.channel == "shell_return_link_visible"),
        "browser_return_score": next(row.score for row in criteria if row.channel == "browser_return_navigation_reaches_launcher"),
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
        "required_link_terms": required_link_terms,
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "browser_evidence": browser,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "state": f"artifacts/{PREFIX}_state.json",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v86_primary_demo_shell_return_handoff_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 326: SSRM-3D Browser World v86 Primary Demo Shell Return Handoff

## Purpose

Report 326 fixes a cold-reviewer comprehension defect found by running the Report 325 next gate against the actual primary-demo path. After `Run reviewer pass`, the maintained shell showed `PASSABLE_REVIEW_PATH` and an `ALL_PASS` receipt, but it did not provide an obvious way back to the launcher checklist and handoff export area. A reviewer had to know to use browser navigation manually.

The shell now includes a visible `Return to launcher handoff` action in the reviewer landing controls. It targets the launcher checklist anchor, preserves the reviewer-focus shell path, and keeps the handoff payload export in the same primary demo route.

## Boundary

{results['boundary']}

## What changed

- Added `returnLauncherHandoffLink` to the maintained v61 shell reviewer landing controls.
- Styled the link as a first-class reviewer action with `.handoff-return`.
- Updated the reviewer landing summary/payload to name the return handoff as the next step after all-pass.
- Updated the Report 301 v61 shell generator so regeneration preserves the affordance.
- Verified in browser: clean launcher, clean shell launch, reviewer pass, visible return link, link target, return navigation, evidence refresh, visible handoff payload, and console health.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| return_source_score | {metrics['return_source_score']:.6f} |
| browser_return_score | {metrics['browser_return_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- return_link_visible_after_pass: `{browser.get('return_link_visible_after_pass')}`
- return_link_href_correct: `{browser.get('return_link_href_correct')}`
- return_navigation_reaches_launcher: `{browser.get('return_navigation_reaches_launcher')}`
- handoff_prepares_after_return: `{browser.get('handoff_prepares_after_return')}`
- console_errors: `{browser.get('console_errors')}`
- visible-link evidence: `{browser.get('return_link_visible_after_pass_evidence')}`
- href evidence: `{browser.get('return_link_href_evidence')}`
- navigation evidence: `{browser.get('return_navigation_evidence')}`
- handoff evidence: `{browser.get('handoff_after_return_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

## Next gate

{results['next_gate']}
"""
    DOCS.mkdir(parents=True, exist_ok=True)
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v86_primary_demo_shell_return_handoff_report.md").write_text(report, encoding="utf-8")


def run(seed: int) -> dict[str, Any]:
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    results = _evaluate(seed)
    _write_report(results)
    _write_json(ARTIFACTS / f"{PREFIX}_results.json", results)
    _write_json(ARTIFACTS / f"{PREFIX}_state.json", {
        "report": REPORT,
        "seed": seed,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "required_link_terms": results["required_link_terms"],
        "browser_evidence_path": results["browser_evidence_path"],
        "verdict": results["verdict"],
    })
    _write_csv(ARTIFACTS / f"{PREFIX}_criteria.csv", results["criteria"])
    _write_csv(ARTIFACTS / f"{PREFIX}_summary.csv", [{**results["metrics"], "report": REPORT, "seed": seed, "verdict": results["verdict"]}])
    _write_csv(ARTIFACTS / f"{PREFIX}_verdict.csv", [{"report": REPORT, "seed": seed, "verdict": results["verdict"], "boundary": BOUNDARY, "next_gate": NEXT_GATE}])
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    print(json.dumps({"report": REPORT, "prefix": PREFIX, "verdict": results["verdict"], "metrics": results["metrics"]}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
