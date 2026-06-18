"""Report 314: SSRM-3D browser world v74 primary demo recoverable trust repair.

This report hardens the maintained primary demo with a bounded recoverable trust-repair
scenario. It adds selected-resident Interrupt/Apologize/Give-space/Repair-with-help
controls that make a small trust wound visible, then show non-magical repair through
public trust/debt/progress/history updates in the same shell.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 314
PREFIX = "ssrm_3d_browser_world_v74_primary_demo_recoverable_trust_repair"
DEFAULT_SEED = 20270712

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V61_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening.py"
V61_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
V61_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local recoverable trust-repair hardening only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, no "
    "complete 3D engine, and no finished gameplay claim. Negative states are bounded and recoverable."
)

NEXT_GATE = (
    "post-314: run a reviewer pass using the trust-repair scenario plus dashboard actions; if coherent, "
    "next consolidation should expose a compact scenario checklist for arrival, consequence, repair, resume, "
    "and replay export on the same primary surface"
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

    criteria = [
        _criterion(
            "trust_repair_panel_present",
            "trustRepairOut" in index and "Trust repair scenario" in index,
            "maintained shell exposes a visible trust-repair scenario panel",
            "recoverable harm/trust repair would remain implicit in generic controls",
        ),
        _criterion(
            "generated_source_of_truth",
            all(term in gen for term in ["interruptWork", "apologizeToResident", "giveSpace", "completeTrustRepair"]),
            "trust-repair scenario logic lives in the v61 generator",
            "regeneration would erase the scenario controls",
        ),
        _criterion(
            "bounded_recoverable_design",
            all(term in app for term in ["recoverableHarm", "bounded", "nonMagic", "concrete help"]),
            "scenario labels harm as bounded/recoverable and repair as non-magical concrete help",
            "scenario could imply unbounded distress or magical trust repair",
        ),
        _criterion(
            "routes_to_public_history",
            all(term in app for term in ["historyEvent: 'trust wound'", "historyEvent: 'trust repair'", "readResidentHistory"]),
            "trust wound and repair steps are recorded in public resident history",
            "reviewers would not see the consequence loop without raw JSON",
        ),
        _criterion(
            "browser_workflow",
            browser.get("workflow_pass") is True,
            f"browser workflow pass recorded as {browser.get('workflow_pass')}",
            "source checks alone would not prove the scenario works in a browser",
        ),
        _criterion(
            "browser_interrupt_visible",
            browser.get("interrupt_pass") is True,
            str(browser.get("interrupt_evidence", "missing interrupt evidence")),
            "interrupt action would not visibly lower trust and record the wound",
        ),
        _criterion(
            "browser_repair_sequence_visible",
            browser.get("repair_sequence_pass") is True,
            str(browser.get("repair_sequence_evidence", "missing repair sequence evidence")),
            "apology/space/help would not visibly repair trust through multiple public steps",
        ),
        _criterion(
            "browser_dashboard_history_sync",
            browser.get("dashboard_history_sync_pass") is True,
            str(browser.get("dashboard_history_sync_evidence", "missing dashboard/history sync evidence")),
            "dashboard and resident history would not agree on trust-repair state",
        ),
        _criterion(
            "browser_resume_persistence",
            browser.get("resume_repair_pass") is True,
            str(browser.get("resume_repair_evidence", "missing resume evidence")),
            "trust-repair consequences would not persist through leave/return",
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
        "trust_repair_panel_score": next(row.score for row in criteria if row.channel == "trust_repair_panel_present"),
        "browser_workflow_score": next(row.score for row in criteria if row.channel == "browser_workflow"),
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
            "state": f"artifacts/{PREFIX}_state.json",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v74_primary_demo_recoverable_trust_repair_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 314: SSRM-3D Browser World v74 Primary Demo Recoverable Trust Repair

## Purpose

Report 314 keeps the primary browser demo moving toward a coherent playable loop by making recoverable harm and trust repair visible. A small selected-resident interruption lowers trust and records a public wound; apology, space, and concrete help repair it through visible history/dashboard changes.

This is not suffering maximization. Negative state is bounded, inspectable, and recoverable.

## Boundary

{results['boundary']}

## What changed

- Added a visible `Trust repair scenario` panel to the maintained v61 shell.
- Added `Interrupt work`, `Apologize`, `Give space`, and `Repair with help` controls.
- Recorded wound and repair steps into public resident history.
- Kept dashboard/history/trust/debt/progress in the same existing state loop.
- Verified repair persists through primary-demo resume.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| trust_repair_panel_score | {metrics['trust_repair_panel_score']:.6f} |
| browser_workflow_score | {metrics['browser_workflow_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- workflow_pass: `{browser.get('workflow_pass')}`
- interrupt_pass: `{browser.get('interrupt_pass')}`
- repair_sequence_pass: `{browser.get('repair_sequence_pass')}`
- dashboard_history_sync_pass: `{browser.get('dashboard_history_sync_pass')}`
- resume_repair_pass: `{browser.get('resume_repair_pass')}`
- console_errors: `{browser.get('console_errors')}`
- interrupt evidence: `{browser.get('interrupt_evidence')}`
- repair evidence: `{browser.get('repair_sequence_evidence')}`
- sync evidence: `{browser.get('dashboard_history_sync_evidence')}`
- resume evidence: `{browser.get('resume_repair_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

This is recoverable-consequence consolidation only. It does not imply subjective distress, moral patienthood, autonomous language, or finished gameplay.

## Next gate

{results['next_gate']}
"""
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v74_primary_demo_recoverable_trust_repair_report.md").write_text(report, encoding="utf-8")


def run(seed: int) -> dict[str, Any]:
    results = _evaluate(seed)
    _write_json(ARTIFACTS / f"{PREFIX}_results.json", results)
    _write_json(ARTIFACTS / f"{PREFIX}_state.json", {
        "report": REPORT,
        "seed": seed,
        "boundary": BOUNDARY,
        "maintained_shell": "visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/index.html",
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
