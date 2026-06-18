"""Report 316: SSRM-3D browser world v76 primary demo resident social memory.

This report keeps consolidating the maintained primary demo by making resident-to-resident
memory visible on the same playable shell. It adds a public relationship ledger, a social
memory pulse, and a selected relationship settlement action so reviewers can see agents
remember each other, not only remember the avatar.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 316
PREFIX = "ssrm_3d_browser_world_v76_primary_demo_resident_social_memory"
DEFAULT_SEED = 20270714

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V61_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening.py"
V61_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
V61_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local resident social-memory consolidation only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, "
    "no complete 3D engine, and no finished gameplay claim. Relationship memory is public state, not proof "
    "of private experience."
)

NEXT_GATE = (
    "post-316: fold the social-memory ledger into the main continuity loop so avatar actions, resident "
    "schedules, resident-to-resident obligations, replay, and resume all tell one inspectable story"
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
            "social_memory_panel_present",
            "relationshipMemoryOut" in index and "Resident social memory" in index,
            "maintained shell exposes a resident social-memory panel",
            "resident-to-resident memory would remain invisible in the primary demo",
        ),
        _criterion(
            "generated_source_of_truth",
            all(term in gen for term in ["RELATION_KEY", "runSocialMemoryPulse", "settleSelectedRelationship", "formatRelationshipMemory"]),
            "relationship memory is generated from the maintained v61 source",
            "regeneration would erase resident social-memory continuity",
        ),
        _criterion(
            "same_surface_relationship_state",
            all(term in app for term in ["readRelationships", "mutateRelationship", "residentToResident", "recordResidentHistory"]),
            "social memory uses the same shell, replay, checkpoints, and public resident history",
            "relationship memory would be another detached bridge instead of a playable system layer",
        ),
        _criterion(
            "public_relationship_signals",
            all(term in app for term in ["Selected tie", "Persistent key", "Public resident-to-resident network"]),
            "relationship panel exposes selected tie, persistence key, and network rows",
            "reviewers would need raw storage to see resident-to-resident continuity",
        ),
        _criterion(
            "browser_social_pulse_visible",
            browser.get("social_pulse_pass") is True,
            str(browser.get("social_pulse_evidence", "missing social pulse evidence")),
            "browser run did not visibly update resident-to-resident memories",
        ),
        _criterion(
            "browser_settlement_visible",
            browser.get("settlement_pass") is True,
            str(browser.get("settlement_evidence", "missing settlement evidence")),
            "selected relationship settlement did not visibly change trust/debt/memory",
        ),
        _criterion(
            "browser_history_sync",
            browser.get("history_sync_pass") is True,
            str(browser.get("history_sync_evidence", "missing history sync evidence")),
            "resident history did not record social-memory events for the affected residents",
        ),
        _criterion(
            "browser_replay_transcript_visible",
            browser.get("replay_transcript_pass") is True,
            str(browser.get("replay_transcript_evidence", "missing replay transcript evidence")),
            "replay transcript did not include social-memory actions",
        ),
        _criterion(
            "browser_resume_persistence",
            browser.get("resume_persistence_pass") is True,
            str(browser.get("resume_persistence_evidence", "missing resume evidence")),
            "resident social-memory state did not persist through leave/resume",
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
        "social_memory_panel_score": next(row.score for row in criteria if row.channel == "social_memory_panel_present"),
        "browser_social_pulse_score": next(row.score for row in criteria if row.channel == "browser_social_pulse_visible"),
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
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v76_primary_demo_resident_social_memory_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 316: SSRM-3D Browser World v76 Primary Demo Resident Social Memory

## Purpose

Report 316 makes the primary demo closer to a single living-world prototype by adding public resident-to-resident memory to the same maintained browser shell. Reviewers can now see residents remember obligations and help from each other, not only avatar-driven trust changes.

This is consolidation, not a new world branch.

## Boundary

{results['boundary']}

## What changed

- Added a visible `Resident social memory` panel to the maintained v61 shell.
- Added `Run social pulse` to update a six-pair resident relationship network.
- Added `Settle selected debt` to change the selected resident's public tie to another resident.
- Routed social-memory changes into public resident history, replay transcript, checkpoints, and local persistence.
- Verified the relationship network persists through primary-demo resume.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| social_memory_panel_score | {metrics['social_memory_panel_score']:.6f} |
| browser_social_pulse_score | {metrics['browser_social_pulse_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- social_pulse_pass: `{browser.get('social_pulse_pass')}`
- settlement_pass: `{browser.get('settlement_pass')}`
- history_sync_pass: `{browser.get('history_sync_pass')}`
- replay_transcript_pass: `{browser.get('replay_transcript_pass')}`
- resume_persistence_pass: `{browser.get('resume_persistence_pass')}`
- console_errors: `{browser.get('console_errors')}`
- social pulse evidence: `{browser.get('social_pulse_evidence')}`
- settlement evidence: `{browser.get('settlement_evidence')}`
- history sync evidence: `{browser.get('history_sync_evidence')}`
- replay transcript evidence: `{browser.get('replay_transcript_evidence')}`
- resume evidence: `{browser.get('resume_persistence_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

The result is public resident relationship continuity only. It does not claim subjective memory, moral status, autonomous language, production persistence, complete gameplay, or a complete 3D engine.

## Next gate

{results['next_gate']}
"""
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v76_primary_demo_resident_social_memory_report.md").write_text(report, encoding="utf-8")


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
                "browser_social_pulse_score": results["metrics"]["browser_social_pulse_score"],
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
                "browser_social_pulse_score": round(results["metrics"]["browser_social_pulse_score"], 6),
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
