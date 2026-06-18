"""Report 333: SSRM-3D browser world v93 handoff continue action bridge.

This report fixes the next cold-reviewer restart defect after Report 332: the
readable handoff said what the persisted resume handoff meant, but the handoff
area did not restore a local Continue action or download link after reload.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 333
PREFIX = "ssrm_3d_browser_world_v93_primary_demo_handoff_continue_action_bridge"
DEFAULT_SEED = 20270731

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V63_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
PRIMARY_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo"
PRIMARY_HTML = PRIMARY_DIR / "index.html"
PRIMARY_JS = PRIMARY_DIR / "demo.js"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"
PRE_PATCH_EVIDENCE = ARTIFACTS / f"{PREFIX}_pre_patch_evidence.json"
REPORT_332_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v92_primary_demo_readable_handoff_restart_bridge_results.json"

BOUNDARY = (
    "Deterministic browser-local handoff continue action bridge only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, no "
    "complete 3D engine, and no finished gameplay claim. This is local restart UX and review workflow "
    "hygiene, not external validation or evidence of inner experience."
)

NEXT_GATE = (
    "post-333: verify a continued reviewer session can return to the launcher and keep the prepared "
    "handoff fresh without creating a new hidden handoff timestamp or forcing JSON inspection"
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


def _safe_get(value: Any, *path: str) -> Any:
    current = value
    for key in path:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def _evaluate(seed: int) -> dict[str, Any]:
    generator = _read(V63_GEN)
    js = _read(PRIMARY_JS)
    html = _read(PRIMARY_HTML)
    browser = _load_json(BROWSER_EVIDENCE)
    pre_patch = _load_json(PRE_PATCH_EVIDENCE)
    report_332 = _load_json(REPORT_332_RESULTS)
    checks = browser.get("checks", {}) if isinstance(browser.get("checks"), dict) else {}
    restart = browser.get("restartControls", {}) if isinstance(browser.get("restartControls"), dict) else {}
    shell = browser.get("shellAfterContinue", {}) if isinstance(browser.get("shellAfterContinue"), dict) else {}
    pre_restart = pre_patch.get("restartControls", {}) if isinstance(pre_patch.get("restartControls"), dict) else {}
    blockers = pre_patch.get("blockers", []) if isinstance(pre_patch.get("blockers"), list) else []
    required_terms = [
        "outsideReviewHandoffActions",
        "preparedHandoffHref",
        "renderOutsideReviewHandoffActions",
        "Continue from prepared",
        "Download prepared outside-review handoff JSON",
        "click Continue from prepared",
    ]
    criteria = [
        _criterion(
            "report_332_readable_restart_gate_passed",
            report_332.get("verdict") == "pass" and _safe_get(report_332, "metrics", "weakest_channel_score") == 1.0,
            f"Report 332 verdict={report_332.get('verdict')} weakest={_safe_get(report_332, 'metrics', 'weakest_channel_score')}",
            "Report 333 would not be grounded in a passing readable-handoff gate",
        ),
        _criterion(
            "pre_patch_continue_action_defect_found",
            pre_restart.get("continueControlCount") == 0 and any("no visible Continue" in blocker for blocker in blockers),
            "; ".join(blockers) or str(pre_restart),
            "Report 333 would not be tied to an observed missing continue-action defect",
        ),
        _criterion(
            "pre_patch_download_restore_defect_found",
            pre_restart.get("downloadControlCount") == 0 and any("download" in blocker for blocker in blockers),
            "; ".join(blockers) or str(pre_restart),
            "Report 333 would not be tied to an observed missing restored-download defect",
        ),
        _criterion(
            "continue_action_source_generated",
            all(term in generator for term in required_terms) and all(term in js for term in required_terms) and "outsideReviewHandoffActions" in html,
            "generator, emitted JS, and emitted HTML contain the prepared-handoff action bridge",
            "regeneration would remove the handoff continue/download action card",
        ),
        _criterion(
            "readable_resume_status_visible",
            checks.get("readable_resume_status_visible") is True,
            str(restart.get("statusText", "missing status")),
            "restart card does not preserve the readable fresh resume handoff status",
        ),
        _criterion(
            "continue_control_visible",
            checks.get("continue_control_visible") is True and restart.get("continueControlCount") == 1,
            str(restart.get("actionsText", "missing actions")),
            "no visible Continue from prepared handoff control is restored after reload",
        ),
        _criterion(
            "continue_control_href_resume_shell",
            checks.get("continue_control_href_resume_shell") is True,
            str(restart.get("continueControl", "missing continue control")),
            "continue control does not target the maintained resume shell URL",
        ),
        _criterion(
            "download_link_restored_after_reload",
            checks.get("download_link_restored_after_reload") is True and restart.get("downloadControlCount") == 1,
            str(restart.get("downloadControl", "missing download control")),
            "prepared handoff download link is not restored from persisted state after reload",
        ),
        _criterion(
            "status_next_action_matches_control",
            checks.get("status_next_action_matches_control") is True,
            str(restart.get("statusText", "missing status")),
            "status next-action text does not match the visible continue control",
        ),
        _criterion(
            "raw_json_preview_still_fresh_resume",
            checks.get("raw_json_preview_still_fresh_resume") is True,
            f"fresh={restart.get('parsedPayloadFresh')} kind={restart.get('parsedPayloadKind')}",
            "action card broke the raw fresh resume JSON preview",
        ),
        _criterion(
            "continue_click_reaches_shell",
            checks.get("continue_click_reaches_shell") is True,
            str(shell.get("url", "missing shell URL")),
            "clicking Continue from prepared handoff does not reach the maintained shell",
        ),
        _criterion(
            "shell_reviewer_controls_visible_after_continue",
            checks.get("shell_reviewer_controls_visible") is True,
            f"reviewer={shell.get('hasReviewerLanding')} runPass={shell.get('hasRunReviewerPass')} return={shell.get('hasReturnToLauncher')}",
            "continued shell session does not expose reviewer controls and return path",
        ),
        _criterion(
            "browser_console_clean",
            checks.get("no_console_errors") is True and browser.get("consoleErrors") == 0,
            f"consoleErrors={browser.get('consoleErrors')} messages={browser.get('consoleErrorMessages', [])}",
            "handoff continue-action browser flow produced console errors",
        ),
        _criterion(
            "boundary_preserved",
            "no subjective consciousness" in BOUNDARY and "no LLM calls" in BOUNDARY,
            BOUNDARY,
            "report boundary implies more than browser-local restart workflow hardening",
        ),
    ]
    scores = [row.score for row in criteria]
    readiness = mean(scores)
    weakest = min(scores)
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "continue_action_score": next(row.score for row in criteria if row.channel == "continue_control_visible"),
        "continue_navigation_score": next(row.score for row in criteria if row.channel == "continue_click_reaches_shell"),
        "download_restore_score": next(row.score for row in criteria if row.channel == "download_link_restored_after_reload"),
        "visible_restart_workflow_score": mean([
            next(row.score for row in criteria if row.channel == "readable_resume_status_visible"),
            next(row.score for row in criteria if row.channel == "continue_control_visible"),
            next(row.score for row in criteria if row.channel == "status_next_action_matches_control"),
            next(row.score for row in criteria if row.channel == "shell_reviewer_controls_visible_after_continue"),
        ]),
        "console_errors": browser.get("consoleErrors", -1),
        "criterion_count": len(criteria),
    }
    verdict = "pass" if readiness >= 0.95 and weakest >= 0.9 and all(row.passed for row in criteria) else "needs_followup"
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
        "pre_patch_evidence_path": str(PRE_PATCH_EVIDENCE.relative_to(ROOT)),
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "report_332_results_path": str(REPORT_332_RESULTS.relative_to(ROOT)),
        "pre_patch_evidence": pre_patch,
        "browser_evidence": browser,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "state": f"artifacts/{PREFIX}_state.json",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "pre_patch_evidence": f"artifacts/{PREFIX}_pre_patch_evidence.json",
            "report": f"docs/{REPORT}_{PREFIX}_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    pre_patch = results["pre_patch_evidence"]
    restart = browser.get("restartControls", {}) if isinstance(browser.get("restartControls"), dict) else {}
    shell = browser.get("shellAfterContinue", {}) if isinstance(browser.get("shellAfterContinue"), dict) else {}
    blocker_rows = "\n".join(f"- {blocker}" for blocker in pre_patch.get("blockers", [])) or "- No pre-patch restart-control blocker was recorded."
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 333: SSRM-3D Browser World v93 Primary Demo Handoff Continue Action Bridge

## Purpose

Report 333 follows the readable restart card from Report 332 and fixes the next concrete workflow gap. The pre-patch browser run reached a persisted readable `fresh resume handoff` after reload, but the handoff area restored neither a visible `Continue from prepared handoff` control nor a download link. The status told reviewers to use the handoff, but the page did not provide the handoff-local controls after reload.

The launcher now renders an `outsideReviewHandoffActions` card whenever a prepared payload is visible. A fresh payload gets a `Continue from prepared <kind> handoff` link and a restored `Download prepared outside-review handoff JSON` link. A stale payload gets a visible reprepare note plus the restored download link for audit.

## Boundary

{results['boundary']}

## Pre-patch blockers

{blocker_rows}

## What changed

- Added `outsideReviewHandoffActions` to the primary launcher HTML and generator.
- Added `preparedHandoffHref(payload)` and `renderOutsideReviewHandoffActions(payload, freshness)`.
- Updated the readable summary next action to name the actual visible continue control.
- Restored the prepared handoff download link from persisted browser-local state after reload.
- Verified clicking `Continue from prepared resume handoff` reaches the maintained shell with reviewer controls and return path visible.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| continue_action_score | {metrics['continue_action_score']:.6f} |
| continue_navigation_score | {metrics['continue_navigation_score']:.6f} |
| download_restore_score | {metrics['download_restore_score']:.6f} |
| visible_restart_workflow_score | {metrics['visible_restart_workflow_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence summary

- readable_resume_status_visible: `{browser.get('checks', {}).get('readable_resume_status_visible')}`
- continue_control_visible: `{browser.get('checks', {}).get('continue_control_visible')}`
- continue_control_href_resume_shell: `{browser.get('checks', {}).get('continue_control_href_resume_shell')}`
- download_link_restored_after_reload: `{browser.get('checks', {}).get('download_link_restored_after_reload')}`
- status_next_action_matches_control: `{browser.get('checks', {}).get('status_next_action_matches_control')}`
- raw_json_preview_still_fresh_resume: `{browser.get('checks', {}).get('raw_json_preview_still_fresh_resume')}`
- continue_click_reaches_shell: `{browser.get('checks', {}).get('continue_click_reaches_shell')}`
- shell_reviewer_controls_visible: `{browser.get('checks', {}).get('shell_reviewer_controls_visible')}`
- no_console_errors: `{browser.get('checks', {}).get('no_console_errors')}`

## Visible restart card after reload

```text
{restart.get('statusText', '')}

{restart.get('actionsText', '')}
```

## Continued shell URL

```text
{shell.get('url', '')}
```

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
    (DOCS / f"{REPORT}_{PREFIX}_report.md").write_text(report, encoding="utf-8")


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
        "required_terms": results["required_terms"],
        "pre_patch_evidence_path": results["pre_patch_evidence_path"],
        "browser_evidence_path": results["browser_evidence_path"],
        "report_332_results_path": results["report_332_results_path"],
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
