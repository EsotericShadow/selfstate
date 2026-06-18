"""Report 309: SSRM-3D browser world v69 primary demo full manual pass.

This report uses the filtered manual ledger from Report 308 during a full primary-demo
playtest pass. The pass found and repaired a maintained-shell evidence defect: QA hooks
were executing, but the visible QA panel only reported "N checks" instead of all-pass
and rollback detail evidence required by the manual script.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 309
PREFIX = "ssrm_3d_browser_world_v69_primary_demo_full_manual_pass"
DEFAULT_SEED = 20270707

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V61_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening.py"
V61_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
PRIMARY_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo" / "index.html"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local full manual pass and maintained-shell QA evidence repair only; "
    "no LLM calls, no subjective consciousness, no autonomous natural language, no moral "
    "patienthood, no production persistence, no complete 3D engine, and no finished gameplay claim."
)

NEXT_GATE = (
    "post-309: keep using the primary demo as the one playable surface; next hardening should add "
    "a reviewer-readable session transcript/checkpoint view only if the next full pass shows the "
    "current replay/debug layer is still too opaque"
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
    primary = _read(PRIMARY_INDEX)
    browser = _load_json(BROWSER_EVIDENCE)
    post_steps = browser.get("post_fix_steps", []) if isinstance(browser.get("post_fix_steps"), list) else []
    pass_count = sum(1 for row in post_steps if row.get("passed") is True)
    required_count = 12
    pre_defects = browser.get("pre_fix_defects", []) if isinstance(browser.get("pre_fix_defects"), list) else []
    resolved_defects = browser.get("resolved_defects", []) if isinstance(browser.get("resolved_defects"), list) else []

    criteria = [
        _criterion(
            "single_primary_surface_retained",
            "ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html" in primary,
            "primary demo still launches the maintained v61 app shell",
            "the full pass would apply to a forked or parallel surface",
        ),
        _criterion(
            "qa_visible_summary_source",
            "function formatQAResults()" in gen and "formatQAResults()" in app,
            "v61 generator and generated app both render detailed QA summaries",
            "the fix would be hand-edited or missing from regenerated shell assets",
        ),
        _criterion(
            "qa_all_pass_wording",
            "all pass" in app and "checks /" in app,
            "QA panel can visibly show all-pass status, not only raw check count",
            "MP-09 would remain unprovable from visible UI text",
        ),
        _criterion(
            "qa_detail_wording",
            "Object.entries(row)" in app and "rollbackTested" in app,
            "QA panel can expose per-hook fields such as rollbackTested/smokePass/auditPass",
            "MP-10 would remain unprovable from visible UI text",
        ),
        _criterion(
            "pre_fix_defect_captured",
            len(pre_defects) >= 2 and {row.get("step_id") for row in pre_defects} >= {"MP-09", "MP-10"},
            "browser pass captured the pre-fix QA visibility defects before repair",
            "the report would claim a repair without recording the defect that motivated it",
        ),
        _criterion(
            "full_manual_pass_complete",
            pass_count == required_count and browser.get("workflow_pass") is True,
            f"post-fix browser pass reported {pass_count}/{required_count} manual steps passing",
            "the primary demo still would not prove the whole loop through MP-12",
        ),
        _criterion(
            "ledger_used_for_resolution",
            len(resolved_defects) >= 2 and browser.get("ledger_filter_pass") is True,
            "filtered ledger records MP-09 and MP-10 as resolved and verifies open/resolved filters",
            "Report 308's ledger would not actually be used for the full-pass defect loop",
        ),
        _criterion(
            "qa_output_proves_checklist",
            "10 checks" in browser.get("post_fix_qa_text", "") and "all pass" in browser.get("post_fix_qa_text", ""),
            "post-fix visible checklist text contains 10 checks and all pass",
            "the checklist output would still not satisfy MP-09",
        ),
        _criterion(
            "qa_output_proves_rollback_audit",
            all(term in browser.get("post_fix_rollback_text", "") for term in ["rollbackTested=true", "smokePass=true", "auditPass=true"]),
            "post-fix visible rollback-audit text exposes rollbackTested, smokePass, and auditPass",
            "the rollback audit output would still not satisfy MP-10",
        ),
        _criterion(
            "console_clean",
            browser.get("console_errors") == 0,
            f"browser console error count was {browser.get('console_errors')}",
            "browser pass produced runtime console errors",
        ),
    ]

    scores = [criterion.score for criterion in criteria]
    readiness = mean(scores)
    weakest = min(scores)
    verdict = "pass" if readiness >= 0.94 and weakest >= 0.9 and all(row.passed for row in criteria) else "fail"
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "full_manual_pass_rate": pass_count / required_count,
        "pre_fix_defect_count": len(pre_defects),
        "resolved_defect_count": len(resolved_defects),
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
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "browser_evidence": browser,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v69_primary_demo_full_manual_pass_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    step_rows = "\n".join(
        f"| {row.get('step_id')} | {row.get('passed')} | {row.get('evidence_summary', '')} |"
        for row in browser.get("post_fix_steps", [])
    ) or "| missing | False | browser evidence missing |"
    defect_rows = "\n".join(
        f"| {row.get('step_id')} | {row.get('severity')} | {row.get('status')} | {row.get('note')} |"
        for row in browser.get("resolved_defects", [])
    ) or "| none | none | none | no resolved defects recorded |"
    report = f"""# Report 309: SSRM-3D Browser World v69 Primary Demo Full Manual Pass

## Purpose

Report 309 uses the Report 308 filtered ledger during a full primary-demo manual pass. The first pass found a real evidence defect in the maintained shell: QA hooks executed, but the visible QA panel only said `10 checks` or `1 checks`, so the manual script could not see `all pass`, `rollbackTested`, `smokePass`, or `auditPass` evidence.

The repair is deliberately narrow: keep the same maintained v61 shell and render detailed QA summaries in the visible QA panel. No new simulation organ was added.

## Boundary

{results['boundary']}

## What changed

- Added `formatQAResults()` to the v61 app-shell generator.
- Regenerated the maintained v61 shell so `qaOut` shows `N checks / all pass` plus per-hook fields.
- Re-ran the primary-demo manual flow through MP-12 in the browser.
- Recorded MP-09 and MP-10 as resolved defects in the browser-local filtered ledger.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| full_manual_pass_rate | {metrics['full_manual_pass_rate']:.6f} |
| pre_fix_defect_count | {metrics['pre_fix_defect_count']} |
| resolved_defect_count | {metrics['resolved_defect_count']} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Manual pass evidence

| Step | Passed | Evidence summary |
|---|---:|---|
{step_rows}

## Resolved defects

| Step | Severity | Status | Note |
|---|---|---|---|
{defect_rows}

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

Report 309 is a consolidation repair, not a capability claim. The meaningful result is that the primary demo can now visibly prove the full manual pass, including the previously opaque QA hooks.

## Next gate

{results['next_gate']}
"""
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v69_primary_demo_full_manual_pass_report.md").write_text(report, encoding="utf-8")


def run(seed: int) -> dict[str, Any]:
    results = _evaluate(seed)
    _write_json(ARTIFACTS / f"{PREFIX}_results.json", results)
    _write_json(ARTIFACTS / f"{PREFIX}_state.json", {
        "report": REPORT,
        "seed": seed,
        "boundary": BOUNDARY,
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "maintained_shell": "visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html",
    })
    _write_csv(ARTIFACTS / f"{PREFIX}_criteria.csv", results["criteria"])
    _write_csv(ARTIFACTS / f"{PREFIX}_summary.csv", [{"metric": key, "value": value} for key, value in results["metrics"].items()])
    _write_csv(ARTIFACTS / f"{PREFIX}_verdict.csv", [{
        "report": REPORT,
        "verdict": results["verdict"],
        "readiness": results["metrics"]["readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "full_manual_pass_rate": results["metrics"]["full_manual_pass_rate"],
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
        "full_manual_pass_rate": results["metrics"]["full_manual_pass_rate"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
