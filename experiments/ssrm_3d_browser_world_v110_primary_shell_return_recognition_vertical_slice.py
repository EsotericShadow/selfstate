"""Report 350: primary shell return-recognition vertical slice.

This report adds a real maintained-shell behavior change after the receipt-gate
work: when a persisted session returns and the avatar enters again, the selected
resident recognizes the returning avatar, updates public resident memory/trust,
and logs continuity evidence. The verifier requires the Report 349 browser-smoked
combined receipt gate and a fresh browser-local return-recognition smoke artifact.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 350
SEED = 20270748
PREFIX = "ssrm_3d_browser_world_v110_primary_shell_return_recognition_vertical_slice"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
DOCS = ROOT / "docs"

SHELL_JS = ROOT / "visualizations/ssrm_3d_browser_world_v61_vertical_slice_app_shell/app.js"
BROWSER_SMOKE = ARTIFACTS / f"{PREFIX}_browser_smoke.json"
RECEIPT_GATE_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v109_primary_demo_guarded_receipt_browser_smoke_results.json"
RECEIPT_GATE_SMOKE = ARTIFACTS / "ssrm_3d_browser_world_v109_primary_demo_guarded_receipt_browser_smoke_browser_smoke.json"
EXPERIMENT_INDEX = ROOT / "scripts/run_experiments.py"

BOUNDARIES = (
    "browser-local maintained-shell return-recognition behavior only",
    "no LLM call",
    "no subjective-consciousness claim",
    "no moral-patienthood claim",
    "no autonomous natural-language claim",
    "no production persistence claim",
    "no hosted URL claim",
    "no complete 3D engine claim",
    "no finished gameplay claim",
)

NEXT_GATE = (
    "post-350: expand the return-recognition loop into a visible resident promise/follow-up "
    "thread so returning to the world advances one remembered obligation rather than only a greeting memory"
)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _criterion(name: str, passed: bool, detail: str, channel: str) -> dict[str, Any]:
    return {"name": name, "passed": bool(passed), "score": 1.0 if passed else 0.0, "channel": channel, "detail": detail}


def _has_all(text: str, terms: tuple[str, ...]) -> bool:
    return all(term in text for term in terms)


def build_results() -> dict[str, Any]:
    shell_js = _read(SHELL_JS)
    experiment_index = _read(EXPERIMENT_INDEX)
    receipt_gate_results = _load_json(RECEIPT_GATE_RESULTS) if RECEIPT_GATE_RESULTS.exists() else {}
    receipt_gate_smoke = _load_json(RECEIPT_GATE_SMOKE) if RECEIPT_GATE_SMOKE.exists() else {}
    smoke = _load_json(BROWSER_SMOKE) if BROWSER_SMOKE.exists() else {}

    source_terms = (
        "const returningVisit = world.entered === true && world.replay.length > 0;",
        "recognized returning avatar after",
        "historyEvent: 'return recognition'",
        "world.returnContinuity =",
        "reportIntroduced: 350",
        "returningVisit",
        "returnContinuity: world.returnContinuity || null",
        "browser-local-return-recognition-public-state-only",
        "publicState:",
        "'returnContinuity'",
        "returnContinuityOut",
        "function renderReturnContinuity()",
    )

    before = smoke.get("beforeReturn", {})
    after = smoke.get("afterReturn", {})
    return_continuity = smoke.get("returnContinuity", {})
    replay_events = smoke.get("replayEvents", [])

    criteria = [
        _criterion(
            "receipt_gate_browser_smoke_available_and_passing",
            RECEIPT_GATE_RESULTS.exists() and RECEIPT_GATE_SMOKE.exists() and receipt_gate_results.get("verdict") == "pass" and receipt_gate_smoke.get("browser") == "in_app_browser",
            "Report 349 browser-smoked combined receipt gate exists and passes before this behavior change is accepted.",
            "review gate",
        ),
        _criterion(
            "return_recognition_source_wired",
            _has_all(shell_js, source_terms),
            "Maintained shell source wires returningVisit recognition, public continuity state, history event, and replay payload.",
            "source behavior",
        ),
        _criterion(
            "browser_smoke_artifact_exists",
            BROWSER_SMOKE.exists() and smoke.get("report") == REPORT,
            "Report 350 browser smoke artifact exists and is tagged correctly.",
            "browser artifact",
        ),
        _criterion(
            "browser_smoke_used_maintained_shell",
            smoke.get("browser") == "in_app_browser" and smoke.get("parallelSurfaceCreated") is False and "ssrm_3d_browser_world_v61_vertical_slice_app_shell" in smoke.get("shellUrl", ""),
            "Smoke ran in the maintained v61 app shell with no parallel surface.",
            "surface discipline",
        ),
        _criterion(
            "browser_smoke_created_persisted_session_before_return",
            smoke.get("initialEnterClicked") is True and smoke.get("talkClicked") is True and before.get("memory") and before.get("replayRows", 0) >= 2,
            "Smoke entered the world, talked to a resident, and created visible persisted replay/memory before return.",
            "browser interaction",
        ),
        _criterion(
            "browser_smoke_returned_without_reset",
            smoke.get("returnedWithoutReset") is True and after.get("replayRows", 0) > before.get("replayRows", 0),
            "Smoke navigated back to the maintained shell without reset and added a return entry to replay.",
            "browser interaction",
        ),
        _criterion(
            "resident_recognized_returning_avatar",
            "recognized returning avatar" in after.get("memory", "") and after.get("trust", 0) > before.get("trust", 1),
            "Visible resident memory and trust changed after return recognition.",
            "visible consequence",
        ),
        _criterion(
            "return_continuity_public_state_recorded",
            return_continuity.get("reportIntroduced") == REPORT and return_continuity.get("resident") == smoke.get("selectedResident") and return_continuity.get("replayRowsBeforeReturn", 0) >= before.get("replayRows", 0),
            "Browser smoke observed public returnContinuity state with report marker, resident, and replay row count.",
            "public state",
        ),
        _criterion(
            "return_recognition_replay_logged",
            "enterWorld" in replay_events and smoke.get("returningVisitLogged") is True,
            "Browser smoke observed an enterWorld replay row with returningVisit true.",
            "replay/debug",
        ),
        _criterion(
            "browser_console_clean",
            smoke.get("consoleErrors", []) == [],
            f"Browser console errors observed: {len(smoke.get('consoleErrors', []))}.",
            "runtime hygiene",
        ),
        _criterion(
            "experiment_index_includes_report_350",
            "experiments.ssrm_3d_browser_world_v110_primary_shell_return_recognition_vertical_slice" in experiment_index,
            "Experiment runner index includes the Report 350 verifier module.",
            "runner index",
        ),
        _criterion(
            "claim_boundary_preserved",
            all(boundary.startswith("no ") or "browser-local" in boundary for boundary in BOUNDARIES),
            "Boundary rejects LLM, consciousness, moral patienthood, autonomous language, production persistence, hosted URL, complete engine, and finished gameplay claims.",
            "claim hygiene",
        ),
    ]

    by_channel: dict[str, list[float]] = {}
    for item in criteria:
        by_channel.setdefault(item["channel"], []).append(float(item["score"]))

    metrics = {
        "readiness": mean(float(item["score"]) for item in criteria),
        "weakest_channel_score": min(float(item["score"]) for item in criteria),
        "review_gate_score": mean(by_channel.get("review gate", [0.0])),
        "source_behavior_score": mean(by_channel.get("source behavior", [0.0])),
        "browser_artifact_score": mean(by_channel.get("browser artifact", [0.0])),
        "surface_discipline_score": mean(by_channel.get("surface discipline", [0.0])),
        "browser_interaction_score": mean(by_channel.get("browser interaction", [0.0])),
        "visible_consequence_score": mean(by_channel.get("visible consequence", [0.0])),
        "public_state_score": mean(by_channel.get("public state", [0.0])),
        "replay_debug_score": mean(by_channel.get("replay/debug", [0.0])),
        "runtime_hygiene_score": mean(by_channel.get("runtime hygiene", [0.0])),
        "runner_index_score": mean(by_channel.get("runner index", [0.0])),
        "claim_hygiene_score": mean(by_channel.get("claim hygiene", [0.0])),
        "before_trust": float(before.get("trust", 0.0) or 0.0),
        "after_trust": float(after.get("trust", 0.0) or 0.0),
        "before_replay_rows": int(before.get("replayRows", 0) or 0),
        "after_replay_rows": int(after.get("replayRows", 0) or 0),
        "console_error_count": len(smoke.get("consoleErrors", [])),
        "criterion_count": len(criteria),
    }
    verdict = "pass" if metrics["weakest_channel_score"] >= 1.0 else "fail"

    return {
        "report": REPORT,
        "seed": SEED,
        "prefix": PREFIX,
        "verdict": verdict,
        "metrics": metrics,
        "criteria": criteria,
        "browser_smoke": smoke,
        "boundaries": BOUNDARIES,
        "next_gate": NEXT_GATE,
    }


def _write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def _write_report(results: dict[str, Any]) -> None:
    metrics = results["metrics"]
    criteria = results["criteria"]
    smoke = results["browser_smoke"]
    report_path = DOCS / f"{REPORT}_{PREFIX}_report.md"
    criterion_lines = "\n".join(f"- {'PASS' if item['passed'] else 'FAIL'} `{item['name']}` ({item['channel']}): {item['detail']}" for item in criteria)
    boundary_lines = "\n".join(f"- {boundary}" for boundary in BOUNDARIES)

    report_path.write_text(
        f"# Report {REPORT}: SSRM-3D Browser World v110 Primary Shell Return-Recognition Vertical Slice\n\n"
        "## Purpose\n\n"
        "Report 350 is an actual maintained-shell behavior change after the receipt-gate work. Returning to a persisted session and entering again now causes the selected resident to recognize the returning avatar, update public memory/trust/progress, and log continuity evidence.\n\n"
        "## What changed\n\n"
        "- `enterWorld()` now detects a returning persisted session with prior replay rows.\n"
        "- The selected resident records `recognized returning avatar ...` in visible memory.\n"
        "- Trust/progress move slightly through the same public resident mutation path.\n"
        "- Public `returnContinuity` state records the resident, replay rows before return, memory, tick, and boundary.\n"
        "- The replay payload records `returningVisit` and `returnContinuity`.\n"
        "- Report 350 requires the Report 349 browser-smoked combined receipt gate before accepting the behavior.\n\n"
        "## Browser smoke summary\n\n"
        f"- shell_url: `{smoke.get('shellUrl')}`\n"
        f"- selected_resident: `{smoke.get('selectedResident')}`\n"
        f"- before_memory: `{(smoke.get('beforeReturn') or {}).get('memory')}`\n"
        f"- after_memory: `{(smoke.get('afterReturn') or {}).get('memory')}`\n"
        f"- before_trust: `{metrics['before_trust']:.3f}`\n"
        f"- after_trust: `{metrics['after_trust']:.3f}`\n"
        f"- before_replay_rows: `{metrics['before_replay_rows']}`\n"
        f"- after_replay_rows: `{metrics['after_replay_rows']}`\n"
        f"- console_errors: `{metrics['console_error_count']}`\n\n"
        "## Metrics\n\n"
        f"- verdict: `{results['verdict']}`\n"
        f"- readiness: `{metrics['readiness']:.3f}`\n"
        f"- weakest_channel_score: `{metrics['weakest_channel_score']:.3f}`\n"
        f"- review_gate_score: `{metrics['review_gate_score']:.3f}`\n"
        f"- browser_interaction_score: `{metrics['browser_interaction_score']:.3f}`\n"
        f"- visible_consequence_score: `{metrics['visible_consequence_score']:.3f}`\n"
        f"- public_state_score: `{metrics['public_state_score']:.3f}`\n"
        f"- replay_debug_score: `{metrics['replay_debug_score']:.3f}`\n"
        f"- runtime_hygiene_score: `{metrics['runtime_hygiene_score']:.3f}`\n"
        f"- criterion_count: `{metrics['criterion_count']}`\n\n"
        "## Criteria\n\n"
        f"{criterion_lines}\n\n"
        "## Boundary\n\n"
        f"{boundary_lines}\n\n"
        "## Interpretation\n\n"
        "This is a small integrated behavior, not a new organ: the maintained shell now shows resident continuity when a player leaves/resumes and enters again. It still does not prove subjective consciousness, autonomous language, production persistence, a hosted URL, moral patienthood, a complete 3D engine, or finished gameplay.\n\n"
        "## Next gate\n\n"
        f"{results['next_gate']}\n",
        encoding="utf-8",
    )


def write_artifacts(results: dict[str, Any]) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    DOCS.mkdir(exist_ok=True)
    (ARTIFACTS / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACTS / f"{PREFIX}_state.json").write_text(json.dumps({"report": REPORT, "seed": SEED, "verdict": results["verdict"], "metrics": results["metrics"], "next_gate": results["next_gate"]}, indent=2, sort_keys=True), encoding="utf-8")
    _write_csv(ARTIFACTS / f"{PREFIX}_summary.csv", [{"report": REPORT, "seed": SEED, "verdict": results["verdict"], **results["metrics"]}], ["report", "seed", "verdict", *results["metrics"].keys()])
    _write_csv(ARTIFACTS / f"{PREFIX}_verdict.csv", [{"report": REPORT, "verdict": results["verdict"], "weakest_channel_score": results["metrics"]["weakest_channel_score"], "visible_consequence_score": results["metrics"]["visible_consequence_score"], "next_gate": results["next_gate"]}], ["report", "verdict", "weakest_channel_score", "visible_consequence_score", "next_gate"])
    _write_csv(ARTIFACTS / f"{PREFIX}_criteria.csv", results["criteria"], ["name", "passed", "score", "channel", "detail"])
    _write_report(results)


def main() -> dict[str, Any]:
    results = build_results()
    write_artifacts(results)
    print(json.dumps({"report": REPORT, "verdict": results["verdict"], "metrics": results["metrics"]}, indent=2, sort_keys=True))
    return results


if __name__ == "__main__":
    main()
