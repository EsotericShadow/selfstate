"""Report 310: SSRM-3D browser world v70 primary demo session transcript.

This report hardens the maintained primary demo by adding a reviewer-readable session
transcript and checkpoint log derived from the existing public replay/save/restore state.
It does not add a new simulation organ; it makes the already-playable loop easier to
inspect without parsing raw world JSON.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 310
PREFIX = "ssrm_3d_browser_world_v70_primary_demo_session_transcript"
DEFAULT_SEED = 20270708

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V61_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell_hardening.py"
V61_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
V61_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"

BOUNDARY = (
    "Deterministic browser-local session-transcript and checkpoint hardening only; no LLM calls, "
    "no subjective consciousness, no autonomous natural language, no moral patienthood, no production "
    "persistence, no complete 3D engine, and no finished gameplay claim."
)

NEXT_GATE = (
    "post-310: use the readable transcript/checkpoint view during another primary-demo pass; if reviewers "
    "still need raw JSON to understand resident continuity, add a compact resident-facing history lane rather "
    "than another isolated report organ"
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
            "transcript_panel_present",
            "sessionTranscriptOut" in index and "Session transcript" in index,
            "maintained shell exposes a visible session transcript panel",
            "reviewers would still need raw trace JSON for action order",
        ),
        _criterion(
            "checkpoint_panel_present",
            "checkpointOut" in index and "Checkpoints" in index,
            "maintained shell exposes a visible checkpoint panel",
            "save/restore checkpoints would remain hidden in raw storage",
        ),
        _criterion(
            "generated_source_of_truth",
            all(term in gen for term in ["formatSessionTranscript", "formatCheckpointLog", "describeReplayRow"]),
            "transcript/checkpoint logic lives in the v61 generator, not a hand-edited generated file",
            "regeneration would erase the UI hardening",
        ),
        _criterion(
            "public_replay_derived",
            all(term in app for term in ["world.replay.slice", "describeReplayRow", "payloadKeys"]),
            "session transcript is derived from public replay rows rather than private state",
            "debug view could become a parallel or private state surface",
        ),
        _criterion(
            "checkpoint_storage_bounded",
            all(term in app for term in ["CHECKPOINT_KEY", "slice(-18)", "slice(-12)"]),
            "checkpoint log uses a bounded browser-local public storage key",
            "checkpoint evidence could grow unbounded or lack persistence across resume",
        ),
        _criterion(
            "private_boundary_preserved",
            "privateWorkspace" in app and "subjectiveFeeling" in app and "llmTranscript" in app,
            "existing state-boundary audit still forbids private/LLM leakage markers",
            "readability hardening might weaken the no-overclaim audit boundary",
        ),
        _criterion(
            "browser_transcript_workflow",
            browser.get("workflow_pass") is True,
            f"browser workflow pass recorded as {browser.get('workflow_pass')}",
            "source checks alone would not prove the readable panels update in the browser",
        ),
        _criterion(
            "browser_transcript_content",
            browser.get("transcript_pass") is True,
            str(browser.get("transcript_evidence", "missing transcript evidence")),
            "transcript panel would not show movement/dialogue/save/export in readable form",
        ),
        _criterion(
            "browser_checkpoint_content",
            browser.get("checkpoint_pass") is True,
            str(browser.get("checkpoint_evidence", "missing checkpoint evidence")),
            "checkpoint panel would not show save/restore/export moments",
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
        "transcript_panel_score": next(row.score for row in criteria if row.channel == "transcript_panel_present"),
        "checkpoint_panel_score": next(row.score for row in criteria if row.channel == "checkpoint_panel_present"),
        "browser_workflow_score": next(row.score for row in criteria if row.channel == "browser_transcript_workflow"),
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
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v70_primary_demo_session_transcript_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 310: SSRM-3D Browser World v70 Primary Demo Session Transcript

## Purpose

Report 310 continues consolidation of the single playable browser world. Report 309 proved the full manual path, but the remaining debug surface still leaned on raw JSON. This report adds a reviewer-readable session transcript and checkpoint log to the maintained v61 shell, derived from the existing public replay and save/restore/export events.

No new simulation organ was added. The change makes the existing loop easier to inspect.

## Boundary

{results['boundary']}

## What changed

- Added a `Session transcript` panel to the maintained v61 shell.
- Added a `Checkpoints` panel for save, restore, save/restore smoke, rollback audit, and replay export moments.
- Added bounded browser-local `ssrm_v61_app_shell_checkpoints` storage.
- Kept transcript text derived from public replay rows and existing action payloads.
- Preserved the existing no-private-workspace/no-subjective-feeling/no-LLM-transcript audit boundary.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| transcript_panel_score | {metrics['transcript_panel_score']:.6f} |
| checkpoint_panel_score | {metrics['checkpoint_panel_score']:.6f} |
| browser_workflow_score | {metrics['browser_workflow_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- workflow_pass: `{browser.get('workflow_pass')}`
- transcript_pass: `{browser.get('transcript_pass')}`
- checkpoint_pass: `{browser.get('checkpoint_pass')}`
- console_errors: `{browser.get('console_errors')}`
- transcript evidence: `{browser.get('transcript_evidence')}`
- checkpoint evidence: `{browser.get('checkpoint_evidence')}`

## Criteria

| Channel | Passed | Score | Evidence |
|---|---:|---:|---|
{criteria_rows}

## Verdict

`{results['verdict']}`

This result should be read as interface/debug consolidation only. It makes the playable loop easier to review; it does not strengthen any claim about subjective consciousness or finished gameplay.

## Next gate

{results['next_gate']}
"""
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v70_primary_demo_session_transcript_report.md").write_text(report, encoding="utf-8")


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
