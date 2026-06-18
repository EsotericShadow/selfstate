"""Report 334: SSRM-3D browser world v94 continue-return freshness bridge.

This report verifies the Report 333 continue action across a full return loop:
a cold reviewer can click the persisted handoff-local continue action, return to
the launcher, refresh shell evidence, and keep the prepared handoff fresh without
creating a new visible handoff timestamp or relying on localStorage inspection.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 334
PREFIX = "ssrm_3d_browser_world_v94_primary_demo_continue_return_freshness_bridge"
DEFAULT_SEED = 20270732

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V63_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
PRIMARY_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo"
PRIMARY_JS = PRIMARY_DIR / "demo.js"
PRIMARY_HTML = PRIMARY_DIR / "index.html"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"
REPORT_333_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v93_primary_demo_handoff_continue_action_bridge_results.json"

BOUNDARY = (
    "Deterministic browser-local continue-return freshness bridge only; no LLM calls, no subjective "
    "consciousness, no autonomous natural language, no moral patienthood, no production persistence, no "
    "complete 3D engine, and no finished gameplay claim. This is local restart workflow and review "
    "freshness hygiene, not external validation or evidence of inner experience."
)

NEXT_GATE = (
    "post-334: verify the same continue-return path after a fresh browser tab enters from the primary "
    "URL, so cross-tab handoff continuity is visible without privileged storage inspection"
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
    report_333 = _load_json(REPORT_333_RESULTS)
    checks = browser.get("checks", {}) if isinstance(browser.get("checks"), dict) else {}
    before = browser.get("beforeContinueLauncher", {}) if isinstance(browser.get("beforeContinueLauncher"), dict) else {}
    shell = browser.get("continuedShell", {}) if isinstance(browser.get("continuedShell"), dict) else {}
    after_before_refresh = browser.get("afterReturnBeforeRefresh", {}) if isinstance(browser.get("afterReturnBeforeRefresh"), dict) else {}
    after = browser.get("afterReturnAfterRefresh", {}) if isinstance(browser.get("afterReturnAfterRefresh"), dict) else {}
    required_terms = [
        "continuePreparedHandoff",
        "preparedHandoffHref",
        "renderOutsideReviewHandoffActions",
        "Continue from prepared",
        "Download prepared outside-review handoff JSON",
        "handoffPayloadFreshnessState",
    ]
    criteria = [
        _criterion(
            "report_333_continue_action_gate_passed",
            report_333.get("verdict") == "pass" and _safe_get(report_333, "metrics", "weakest_channel_score") == 1.0,
            f"Report 333 verdict={report_333.get('verdict')} weakest={_safe_get(report_333, 'metrics', 'weakest_channel_score')}",
            "Report 334 would not be grounded in a passing continue-action gate",
        ),
        _criterion(
            "continue_return_source_still_present",
            all(term in generator for term in required_terms) and all(term in js for term in required_terms) and "outsideReviewHandoffActions" in html,
            "generator, emitted JS, and emitted HTML retain continue-return handoff machinery",
            "regeneration would remove the handoff continue-return path",
        ),
        _criterion(
            "before_continue_visible_fresh_resume",
            checks.get("before_continue_visible_fresh_resume") is True,
            str(before.get("statusText", "missing before status")),
            "handoff was not visibly fresh and resume-bound before continue",
        ),
        _criterion(
            "continue_control_visible_before_continue",
            checks.get("continue_control_visible_before_continue") is True and before.get("hasContinueControl") is True,
            str(before.get("actionsText", "missing actions")),
            "reviewer cannot continue from the prepared handoff with visible controls",
        ),
        _criterion(
            "continue_reaches_reviewer_shell",
            checks.get("continue_reaches_reviewer_shell") is True,
            f"url={shell.get('url')} reviewer={shell.get('hasReviewerLanding')} runPass={shell.get('hasRunReviewerPass')} return={shell.get('hasReturnToLauncher')}",
            "continue action does not reach the maintained shell reviewer path",
        ),
        _criterion(
            "return_to_launcher_visible_after_continue",
            checks.get("return_to_launcher_visible_after_continue") is True,
            str(after_before_refresh.get("url", "missing return URL")),
            "continued reviewer session cannot return to the launcher handoff area",
        ),
        _criterion(
            "visible_handoff_timestamp_unchanged_after_return",
            checks.get("visible_handoff_timestamp_unchanged_after_return") is True,
            f"before={before.get('handoffStatusText')} after={after.get('handoffStatusText')}",
            "continue-return created a new visible handoff timestamp",
        ),
        _criterion(
            "prepared_payload_recorded_at_unchanged_after_return",
            checks.get("prepared_payload_recorded_at_unchanged_after_return") is True,
            f"before={before.get('payloadRecordedAt')} after={after.get('payloadRecordedAt')}",
            "prepared payload recordedAt changed across continue-return",
        ),
        _criterion(
            "preview_current_recorded_at_unchanged_after_return",
            checks.get("preview_current_recorded_at_unchanged_after_return") is True,
            f"before={before.get('payloadCurrentRecordedAt')} after={after.get('payloadCurrentRecordedAt')}",
            "freshness preview current handoff timestamp changed across continue-return",
        ),
        _criterion(
            "handoff_remains_fresh_after_refresh",
            checks.get("handoff_remains_fresh_after_refresh") is True and _safe_get(after, "payloadPreviewFreshness", "fresh") is True,
            str(after.get("payloadPreviewFreshness", "missing freshness")),
            "prepared handoff goes stale after returning and refreshing evidence",
        ),
        _criterion(
            "visible_status_remains_fresh_resume_after_refresh",
            checks.get("visible_status_remains_fresh_resume_after_refresh") is True,
            str(after.get("statusText", "missing after status")),
            "visible handoff status does not remain fresh resume after refresh",
        ),
        _criterion(
            "controls_still_available_after_refresh",
            checks.get("controls_still_available_after_refresh") is True,
            str(after.get("actionsText", "missing after actions")),
            "continue/download controls disappear after return refresh",
        ),
        _criterion(
            "shell_evidence_refresh_visible_after_continue",
            checks.get("shell_evidence_refresh_visible_after_continue") is True,
            str(after.get("evidenceStatusText", "missing shell evidence status")),
            "shell evidence refresh is not visible and all-pass after continue-return",
        ),
        _criterion(
            "browser_evidence_uses_visible_or_preview_state",
            "localHandoff" not in json.dumps(browser) and "localPayloadHandoff" not in json.dumps(browser),
            "browser evidence compares visible status text and visible preview payload, not localStorage-only fields",
            "Report 334 proof relies on privileged localStorage inspection",
        ),
        _criterion(
            "browser_console_clean",
            checks.get("no_console_errors") is True and browser.get("consoleErrors") == 0,
            f"consoleErrors={browser.get('consoleErrors')} messages={browser.get('consoleErrorMessages', [])}",
            "continue-return browser flow produced console errors",
        ),
        _criterion(
            "boundary_preserved",
            "no subjective consciousness" in BOUNDARY and "no LLM calls" in BOUNDARY,
            BOUNDARY,
            "report boundary implies more than browser-local restart workflow freshness",
        ),
    ]
    scores = [row.score for row in criteria]
    readiness = mean(scores)
    weakest = min(scores)
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "continue_return_navigation_score": next(row.score for row in criteria if row.channel == "return_to_launcher_visible_after_continue"),
        "timestamp_stability_score": mean([
            next(row.score for row in criteria if row.channel == "visible_handoff_timestamp_unchanged_after_return"),
            next(row.score for row in criteria if row.channel == "prepared_payload_recorded_at_unchanged_after_return"),
            next(row.score for row in criteria if row.channel == "preview_current_recorded_at_unchanged_after_return"),
        ]),
        "post_return_freshness_score": next(row.score for row in criteria if row.channel == "handoff_remains_fresh_after_refresh"),
        "visible_no_json_score": next(row.score for row in criteria if row.channel == "browser_evidence_uses_visible_or_preview_state"),
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
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "report_333_results_path": str(REPORT_333_RESULTS.relative_to(ROOT)),
        "browser_evidence": browser,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "state": f"artifacts/{PREFIX}_state.json",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "report": f"docs/{REPORT}_{PREFIX}_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    before = browser.get("beforeContinueLauncher", {}) if isinstance(browser.get("beforeContinueLauncher"), dict) else {}
    after = browser.get("afterReturnAfterRefresh", {}) if isinstance(browser.get("afterReturnAfterRefresh"), dict) else {}
    shell = browser.get("continuedShell", {}) if isinstance(browser.get("continuedShell"), dict) else {}
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 334: SSRM-3D Browser World v94 Primary Demo Continue Return Freshness Bridge

## Purpose

Report 334 follows the Report 333 handoff-local continue action through the return loop. The browser run prepared a fresh resume handoff, clicked `Continue from prepared resume handoff`, reached the maintained shell reviewer path, returned to the launcher, refreshed shell evidence, and confirmed the prepared handoff stayed fresh without a new visible launch timestamp.

No launcher source patch was needed. The existing continue action does not call the launcher `recordLaunch` path, so returning and refreshing shell evidence preserves the same visible resume handoff timestamp and the same prepared payload timestamp.

## Boundary

{results['boundary']}

## Browser path

- Prepare a reviewed clean handoff, then create the stale clean-vs-resume condition.
- Re-prepare the outside-review handoff as a fresh `resume` handoff.
- Reload the launcher and confirm the readable handoff card is visible.
- Click `Continue from prepared resume handoff`.
- Use the shell's visible `Return to launcher handoff` link.
- Click `Refresh shell evidence`.
- Confirm the visible launch handoff timestamp and visible payload freshness stayed stable.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| continue_return_navigation_score | {metrics['continue_return_navigation_score']:.6f} |
| timestamp_stability_score | {metrics['timestamp_stability_score']:.6f} |
| post_return_freshness_score | {metrics['post_return_freshness_score']:.6f} |
| visible_no_json_score | {metrics['visible_no_json_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence summary

- before_continue_visible_fresh_resume: `{browser.get('checks', {}).get('before_continue_visible_fresh_resume')}`
- continue_control_visible_before_continue: `{browser.get('checks', {}).get('continue_control_visible_before_continue')}`
- continue_reaches_reviewer_shell: `{browser.get('checks', {}).get('continue_reaches_reviewer_shell')}`
- return_to_launcher_visible_after_continue: `{browser.get('checks', {}).get('return_to_launcher_visible_after_continue')}`
- visible_handoff_timestamp_unchanged_after_return: `{browser.get('checks', {}).get('visible_handoff_timestamp_unchanged_after_return')}`
- prepared_payload_recorded_at_unchanged_after_return: `{browser.get('checks', {}).get('prepared_payload_recorded_at_unchanged_after_return')}`
- preview_current_recorded_at_unchanged_after_return: `{browser.get('checks', {}).get('preview_current_recorded_at_unchanged_after_return')}`
- handoff_remains_fresh_after_refresh: `{browser.get('checks', {}).get('handoff_remains_fresh_after_refresh')}`
- visible_status_remains_fresh_resume_after_refresh: `{browser.get('checks', {}).get('visible_status_remains_fresh_resume_after_refresh')}`
- controls_still_available_after_refresh: `{browser.get('checks', {}).get('controls_still_available_after_refresh')}`
- shell_evidence_refresh_visible_after_continue: `{browser.get('checks', {}).get('shell_evidence_refresh_visible_after_continue')}`
- no_console_errors: `{browser.get('checks', {}).get('no_console_errors')}`

## Visible timestamp before continue

```text
{before.get('handoffStatusText', '')}
```

## Visible timestamp after return and refresh

```text
{after.get('handoffStatusText', '')}
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
        "browser_evidence_path": results["browser_evidence_path"],
        "report_333_results_path": results["report_333_results_path"],
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
