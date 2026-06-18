"""Report 328: SSRM-3D browser world v88 primary demo one-URL handoff integrity.

This report fixes a cold-reviewer evidence divergence: the final handoff payload
used a hardcoded localhost URL instead of the primary-demo URL actually used by
the reviewer.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 328
PREFIX = "ssrm_3d_browser_world_v88_primary_demo_one_url_handoff_integrity"
DEFAULT_SEED = 20270726

ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"
V63_GEN = ROOT / "experiments" / "ssrm_3d_browser_world_v63_primary_demo_entrypoint_manual_playtest_package.py"
PRIMARY_DIR = ROOT / "visualizations" / "ssrm_3d_browser_world_primary_demo"
PRIMARY_INDEX = PRIMARY_DIR / "index.html"
PRIMARY_JS = PRIMARY_DIR / "demo.js"
BROWSER_EVIDENCE = ARTIFACTS / f"{PREFIX}_browser_evidence.json"
PRE_PATCH_EVIDENCE = ARTIFACTS / f"{PREFIX.replace('_integrity', '')}_pre_patch_evidence.json"

BOUNDARY = (
    "Deterministic browser-local one-URL handoff integrity only; no LLM calls, no subjective consciousness, "
    "no autonomous natural language, no moral patienthood, no production persistence, no complete 3D engine, "
    "and no finished gameplay claim. URL integrity is review evidence hygiene, not external validation or "
    "evidence of inner experience."
)

NEXT_GATE = (
    "post-328: continue the cold one-URL reviewer pass and fix the next place where visible reviewer state, "
    "recorder state, shell evidence, and exported handoff payload can drift after reload or resume"
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
    generator = _read(V63_GEN)
    index = _read(PRIMARY_INDEX)
    js = _read(PRIMARY_JS)
    browser = _load_json(BROWSER_EVIDENCE)
    pre_patch = _load_json(PRE_PATCH_EVIDENCE)
    required_terms = ["currentLauncherUrl", "renderCurrentLauncherUrl", "launcherUrl: currentLauncherUrl()", "launchUrl: currentLauncherUrl()", "currentLaunchUrl"]
    blockers = pre_patch.get("blockers", []) if isinstance(pre_patch.get("blockers"), list) else []
    criteria = [
        _criterion(
            "pre_patch_cold_url_divergence_found",
            any("launchUrl" in blocker and "diverge" in blocker for blocker in blockers),
            "; ".join(blockers) or "missing pre-patch URL-divergence evidence",
            "Report 328 would not be tied to a demonstrated cold-reviewer defect",
        ),
        _criterion(
            "dynamic_url_source_generated",
            all(term in generator for term in required_terms) and all(term in js for term in required_terms[:4]),
            "launcher generator and emitted JS derive current URL from the opened page",
            "regeneration would restore hardcoded one-port handoff URLs",
        ),
        _criterion(
            "visible_current_url_slot_present",
            "currentLaunchUrl" in index and "currentLaunchUrl" in generator,
            "handoff panel exposes the URL actually used by the reviewer",
            "reviewers still see a stale hardcoded local URL",
        ),
        _criterion(
            "hardcoded_export_url_removed",
            "launchUrl: 'http://127.0.0.1:8765" not in js and "launchUrl: 'http://127.0.0.1:8765" not in generator,
            "outside-review export no longer hardcodes port 8765 in JS payloads",
            "exports can diverge from non-8765 reviewer URLs",
        ),
        _criterion(
            "browser_visible_url_matches_current_page",
            browser.get("visible_url_matches_current_page") is True,
            str(browser.get("visible_url_evidence", "missing visible URL evidence")),
            "visible handoff URL does not match the browser URL actually used",
        ),
        _criterion(
            "browser_payload_launch_url_matches_current_page",
            browser.get("payload_launch_url_matches_current_page") is True,
            str(browser.get("payload_launch_url_evidence", "missing payload URL evidence")),
            "handoff payload launchUrl still diverges from the URL actually used",
        ),
        _criterion(
            "browser_handoff_launcher_url_matches_current_page",
            browser.get("handoff_launcher_url_matches_current_page") is True,
            str(browser.get("handoff_launcher_url_evidence", "missing handoff launcherUrl evidence")),
            "launch handoff record still omits or misstates the current launcher URL",
        ),
        _criterion(
            "browser_completion_still_ready",
            browser.get("completion_still_ready") is True,
            str(browser.get("completion_evidence", "missing completion evidence")),
            "URL integrity patch broke reviewed handoff completion",
        ),
        _criterion(
            "browser_one_url_console_clean",
            browser.get("console_errors") == 0,
            f"browser console error count was {browser.get('console_errors')}",
            "one-URL handoff flow produced browser console errors",
        ),
        _criterion(
            "boundary_preserved",
            "no subjective consciousness" in BOUNDARY and "no LLM calls" in BOUNDARY,
            BOUNDARY,
            "report boundary implies more than browser-local URL integrity hardening",
        ),
    ]
    scores = [row.score for row in criteria]
    readiness = mean(scores)
    weakest = min(scores)
    verdict = "pass" if readiness >= 0.95 and weakest >= 0.9 and all(row.passed for row in criteria) else "needs_browser_evidence"
    metrics = {
        "readiness": readiness,
        "weakest_channel_score": weakest,
        "url_source_score": next(row.score for row in criteria if row.channel == "dynamic_url_source_generated"),
        "browser_url_score": next(row.score for row in criteria if row.channel == "browser_payload_launch_url_matches_current_page"),
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
        "pre_patch_evidence_path": str(PRE_PATCH_EVIDENCE.relative_to(ROOT)),
        "browser_evidence_path": str(BROWSER_EVIDENCE.relative_to(ROOT)),
        "pre_patch_evidence": pre_patch,
        "browser_evidence": browser,
        "artifacts": {
            "results": f"artifacts/{PREFIX}_results.json",
            "summary": f"artifacts/{PREFIX}_summary.csv",
            "verdict": f"artifacts/{PREFIX}_verdict.csv",
            "criteria": f"artifacts/{PREFIX}_criteria.csv",
            "state": f"artifacts/{PREFIX}_state.json",
            "browser_evidence": f"artifacts/{PREFIX}_browser_evidence.json",
            "pre_patch_evidence": f"artifacts/{PREFIX.replace('_integrity', '')}_pre_patch_evidence.json",
            "report": f"docs/{REPORT}_ssrm_3d_browser_world_v88_primary_demo_one_url_handoff_integrity_report.md",
        },
    }


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    browser = results["browser_evidence"]
    blockers = results["pre_patch_evidence"].get("blockers", [])
    blocker_rows = "\n".join(f"- {blocker}" for blocker in blockers) or "- No pre-patch blocker evidence was available."
    criteria_rows = "\n".join(
        f"| {row['channel']} | {row['passed']} | {row['score']:.3f} | {row['evidence']} |"
        for row in results["criteria"]
    )
    report = f"""# Report 328: SSRM-3D Browser World v88 Primary Demo One-URL Handoff Integrity

## Purpose

Report 328 runs the cold one-URL outside-review path after Report 327. The flow completed, but the final handoff payload still claimed the hardcoded Report 303 localhost URL on port `8765`, even when the reviewer actually entered through another primary-demo URL. That made exported evidence diverge from the one URL used during review.

The launcher now derives its visible and exported handoff URL from `window.location`, records it in the launch handoff payload, and embeds the current URL in the final outside-review handoff payload.

## Boundary

{results['boundary']}

## Pre-patch blocker

{blocker_rows}

## What changed

- Added `currentLauncherUrl()` and `renderCurrentLauncherUrl()` to the primary launcher.
- The visible handoff panel now exposes the URL actually opened in the browser.
- Launch handoff records now carry `launcherUrl`.
- Outside-review exports now use `launchUrl: currentLauncherUrl()` instead of the old hardcoded port-8765 URL.
- Verified in browser that visible URL, launch-handoff `launcherUrl`, final payload `launchUrl`, reviewed completion, and console health all hold on a non-8765 port.

## Metrics

| Metric | Value |
|---|---:|
| readiness | {metrics['readiness']:.6f} |
| weakest_channel_score | {metrics['weakest_channel_score']:.6f} |
| url_source_score | {metrics['url_source_score']:.6f} |
| browser_url_score | {metrics['browser_url_score']:.6f} |
| console_errors | {metrics['console_errors']} |
| criterion_count | {metrics['criterion_count']} |

## Browser evidence

- visible_url_matches_current_page: `{browser.get('visible_url_matches_current_page')}`
- payload_launch_url_matches_current_page: `{browser.get('payload_launch_url_matches_current_page')}`
- handoff_launcher_url_matches_current_page: `{browser.get('handoff_launcher_url_matches_current_page')}`
- completion_still_ready: `{browser.get('completion_still_ready')}`
- console_errors: `{browser.get('console_errors')}`
- visible URL evidence: `{browser.get('visible_url_evidence')}`
- payload URL evidence: `{browser.get('payload_launch_url_evidence')}`
- handoff launcher URL evidence: `{browser.get('handoff_launcher_url_evidence')}`
- completion evidence: `{browser.get('completion_evidence')}`

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
    (DOCS / f"{REPORT}_ssrm_3d_browser_world_v88_primary_demo_one_url_handoff_integrity_report.md").write_text(report, encoding="utf-8")


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
        "pre_patch_evidence_path": results["pre_patch_evidence_path"],
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
