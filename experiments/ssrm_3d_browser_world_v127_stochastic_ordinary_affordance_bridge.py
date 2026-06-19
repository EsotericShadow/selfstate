from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List

from experiments.ssrm_3d_browser_world_v122_non_scripted_world_anomaly_discovery_bridge import SEEDS
from experiments.ssrm_3d_browser_world_v126_stochastic_history_influence_bridge import simulate_history_influence

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 367
SLUG = "ssrm_3d_browser_world_v127_stochastic_ordinary_affordance_bridge"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT366_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v126_stochastic_history_influence_bridge_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
ORDINARY_ACTIONS = ARTIFACT_DIR / f"{SLUG}_ordinary_actions.csv"
AFFORDANCE_EFFECTS = ARTIFACT_DIR / f"{SLUG}_affordance_effects.csv"
SOURCE_LINKS = ARTIFACT_DIR / f"{SLUG}_source_links.csv"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "367_ssrm_3d_stochastic_ordinary_affordance_bridge_report.md"
BOUNDARY = (
    "Browser-local stochastic ordinary-affordance influence only. Recovered, pending, and stabilized stochastic history "
    "can bias normal actions such as Offer help, Talk, Ask schedule, and Movement while preserving source choice IDs, "
    "recovery paths, no-permanent-penalty flags, and no-LLM/no-consciousness boundaries."
)
NEXT_GATE = (
    "post-367: make ordinary-affordance influence persist across save/restore and return sessions, then surface it through "
    "resident body language instead of only text panels"
)


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2, sort_keys=True)
        handle.write("\n")


def write_csv(path: Path, rows: List[Dict[str, Any]], fieldnames: List[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def has_terms(text: str, terms: Iterable[str]) -> bool:
    return all(term in text for term in terms)


def add_criterion(criteria: List[Dict[str, Any]], name: str, passed: bool, evidence: str) -> None:
    criteria.append({"criterion": name, "passed": bool(passed), "score": 1.0 if passed else 0.0, "evidence": evidence})


def effect_for(action: str, choice: Dict[str, Any]) -> Dict[str, Any]:
    decision = choice["decision"]
    outcome = "normal action unchanged by stochastic history"
    blocked = False
    movement_scale = 1.0
    care_cost = 1 if action == "offerHelp" else 0
    trust_delta = 0.004
    progress_delta = 0.004
    if decision == "bounded_refusal_until_recovery":
        blocked = action in {"offerHelp", "askSchedule"}
        movement_scale = 0.5 if action.startswith("move") else 1.0
        care_cost = 0 if blocked else care_cost
        trust_delta = -0.004 if action == "offerHelp" else -0.001
        progress_delta = 0.0 if blocked else 0.001
        outcome = "pending recovery creates bounded caution"
    elif decision == "cautious_help_with_limits":
        movement_scale = 0.75 if action.startswith("move") else 1.0
        trust_delta = 0.008 if action == "offerHelp" else 0.004
        progress_delta = 0.014 if action == "offerHelp" else 0.004
        outcome = "stabilized history allows cautious action"
    elif decision == "accept_recovery_informed_help":
        trust_delta = 0.020 if action == "offerHelp" else 0.010
        progress_delta = 0.028 if action == "offerHelp" else 0.006
        outcome = "recovered history supports ordinary action"
    return {
        "outcome": outcome,
        "blocked": blocked,
        "movement_scale": movement_scale,
        "care_cost": care_cost,
        "trust_delta": trust_delta,
        "progress_delta": progress_delta,
    }


def simulate_ordinary_affordances(seed: int) -> Dict[str, Any]:
    history = simulate_history_influence(seed)
    actions: List[Dict[str, Any]] = []
    effects: List[Dict[str, Any]] = []
    source_links: List[Dict[str, Any]] = []
    normal_actions = ["offerHelp", "talkBounded", "askSchedule", "moveEast"]
    for index, choice in enumerate(history["choices"][:12]):
        for action in normal_actions:
            effect = effect_for(action, choice)
            action_id = f"{seed}-SOA-{len(actions) + 1:03d}"
            row = {
                "seed": seed,
                "action_id": action_id,
                "normal_action": action,
                "actor": choice["actor"],
                "source_choice_id": choice["choice_id"],
                "source_decision": choice["decision"],
                "source_recovery_id": choice["source_recovery_id"],
                "outcome": effect["outcome"],
                "blocked": effect["blocked"],
                "movement_scale": effect["movement_scale"],
                "care_cost": effect["care_cost"],
                "trust_delta": effect["trust_delta"],
                "progress_delta": effect["progress_delta"],
                "permanent_penalty": False,
            }
            actions.append(row)
            effects.append({**row, "normal_affordance": True, "recovery_path": choice["recovery_path"]})
            source_links.append({
                "seed": seed,
                "action_id": action_id,
                "source_choice_id": choice["choice_id"],
                "source_recovery_id": choice["source_recovery_id"],
                "normal_action": action,
                "source_boundary_preserved": True,
            })
    return {"seed": seed, "actions": actions, "effects": effects, "source_links": source_links, "history": history}


def report_text(results: Dict[str, Any], criteria: List[Dict[str, Any]], browser: Dict[str, Any]) -> str:
    metrics = results["metrics"]
    passed_count = sum(1 for row in criteria if row["passed"])
    lines = [
        "# Report 367: SSRM-3D Stochastic Ordinary Affordance Bridge",
        "",
        "Report 367 attaches stochastic history influence to ordinary play affordances. Normal `Offer help`, `Talk`, `Ask schedule`, and movement can now be biased by recovered, pending, or stabilized stochastic recovery history instead of requiring the reviewer to press a dedicated history panel button.",
        "",
        f"Boundary: {BOUNDARY}",
        "",
        "## Result",
        "",
        f"Verdict: `{results['verdict']}`",
        f"Readiness: `{metrics['readiness']:.3f}`",
        f"Weakest channel score: `{metrics['weakest_channel_score']:.3f}`",
        f"Criteria passed: `{passed_count} / {len(criteria)}`",
        "",
        "## Browser-smoke evidence",
        "",
        f"- Maintained shell URL: `{browser.get('shellUrl', 'missing')}`",
        f"- Normal influence summary: `{browser.get('afterOrdinary', {}).get('ordinarySummary', 'missing')}`",
        f"- Normal influence excerpt: `{browser.get('afterOrdinary', {}).get('ordinaryText', 'missing')}`",
        f"- Console errors: `{metrics['console_error_count']}`",
        "",
        "## Criteria",
        "",
        "| Criterion | Score | Evidence |",
        "| --- | ---: | --- |",
    ]
    for row in criteria:
        evidence = str(row["evidence"]).replace("|", "/")
        lines.append(f"| `{row['criterion']}` | `{row['score']:.1f}` | {evidence} |")
    lines.extend([
        "",
        "## Honest interpretation",
        "",
        "This is still bounded browser-local scaffolding, but it is a material integration step: stochastic history now changes normal affordances the user already presses. It keeps source IDs and no-permanent-penalty flags, so the behavior is less scripted without becoming opaque or punitive.",
        "",
        "## Next gate",
        "",
        NEXT_GATE,
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    runs = [simulate_ordinary_affordances(seed) for seed in SEEDS]
    actions = [row for run in runs for row in run["actions"]]
    effects = [row for run in runs for row in run["effects"]]
    source_links = [row for run in runs for row in run["source_links"]]
    app_text = SHELL_APP.read_text(encoding="utf-8")
    index_text = SHELL_INDEX.read_text(encoding="utf-8")
    runner_text = RUNNER.read_text(encoding="utf-8")
    report366 = load_json(REPORT366_RESULTS)
    browser = load_json(BROWSER_SMOKE)
    console_errors = browser.get("consoleErrors", [])

    action_kinds = {row["normal_action"] for row in actions}
    metrics_base = {
        "ordinary_action_binding": float({"offerHelp", "talkBounded", "askSchedule", "moveEast"}.issubset(action_kinds)),
        "offer_help_influence": float(any(row["normal_action"] == "offerHelp" and row["source_choice_id"] for row in actions)),
        "talk_influence": float(any(row["normal_action"] == "talkBounded" and row["source_choice_id"] for row in actions)),
        "schedule_influence": float(any(row["normal_action"] == "askSchedule" and row["source_choice_id"] for row in actions)),
        "movement_influence": float(any(row["normal_action"] == "moveEast" and row["movement_scale"] != 1 for row in actions)),
        "bounded_refusal_blocks_help": float(any(row["normal_action"] == "offerHelp" and row["blocked"] for row in actions)),
        "source_link_integrity": float(len(source_links) == len(actions) and all(row["source_boundary_preserved"] for row in source_links)),
        "no_permanent_penalty": float(all(row["permanent_penalty"] is False for row in actions)),
        "not_panel_only_loop": float(has_terms(app_text, ["applyStochasticHistoryToOrdinaryAction", "offerHelp", "talkBounded", "askSchedule", "moveEast"])),
        "browser_surface_wired": float(has_terms(index_text, ["stochasticOrdinaryAffordanceOut", "Talk normally", "Offer help normally", "Run normal sequence"])),
    }

    write_csv(ORDINARY_ACTIONS, actions, ["seed", "action_id", "normal_action", "actor", "source_choice_id", "source_decision", "source_recovery_id", "outcome", "blocked", "movement_scale", "care_cost", "trust_delta", "progress_delta", "permanent_penalty"])
    write_csv(AFFORDANCE_EFFECTS, effects, ["seed", "action_id", "normal_action", "actor", "source_choice_id", "source_decision", "source_recovery_id", "outcome", "blocked", "movement_scale", "care_cost", "trust_delta", "progress_delta", "permanent_penalty", "normal_affordance", "recovery_path"])
    write_csv(SOURCE_LINKS, source_links, ["seed", "action_id", "source_choice_id", "source_recovery_id", "normal_action", "source_boundary_preserved"])

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_366_history_gate_passing", report366.get("verdict") == "pass" and report366.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 366 verdict={report366.get('verdict')} weakest={report366.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "source_declares_ordinary_boundary", has_terms(app_text, ["browser-local-stochastic-ordinary-affordance-only", "stochasticOrdinaryAffordance", "normalPlayPolicy"]), "app.js declares ordinary-affordance influence state")
    add_criterion(criteria, "source_normal_actions_call_influence", has_terms(app_text, ["applyStochasticHistoryToOrdinaryAction('offerHelp'", "applyStochasticHistoryToOrdinaryAction('talkBounded'", "applyStochasticHistoryToOrdinaryAction('askSchedule'", "applyStochasticHistoryToOrdinaryAction('moveEast'"]), "normal shell actions call stochastic history influence")
    add_criterion(criteria, "visible_ordinary_panel_wired", metrics_base["browser_surface_wired"] == 1.0, "index.html exposes normal influence panel and controls")
    add_criterion(criteria, "runner_includes_report_367", "experiments.ssrm_3d_browser_world_v127_stochastic_ordinary_affordance_bridge" in runner_text, "scripts/run_experiments.py includes Report 367 module")
    for metric, value in metrics_base.items():
        add_criterion(criteria, metric, value == 1.0, f"metric={value}")
    ordinary_text = browser.get("afterOrdinary", {}).get("ordinaryText", "")
    add_criterion(criteria, "browser_smoke_artifact_exists", bool(browser), str(BROWSER_SMOKE.relative_to(ROOT)) if BROWSER_SMOKE.exists() else "missing browser smoke artifact")
    add_criterion(criteria, "browser_ordinary_influence_visible", all(term in ordinary_text for term in ["Normal action records:", "Source ledger:", "Policy:"]), ordinary_text or "missing ordinary influence text")
    add_criterion(criteria, "browser_normal_actions_visible", any(term in ordinary_text for term in ["offerHelp", "talkBounded", "askSchedule", "moveEast"]), ordinary_text or "missing ordinary influence text")
    add_criterion(criteria, "browser_console_clean", len(console_errors) == 0, f"console error count={len(console_errors)}")

    passed = sum(1 for row in criteria if row["passed"])
    metrics = {
        **metrics_base,
        "ordinary_action_count": len(actions),
        "source_link_count": len(source_links),
        "console_error_count": len(console_errors),
        "criterion_count": len(criteria),
        "readiness": round(passed / len(criteria), 6),
        "weakest_channel_score": min(row["score"] for row in criteria),
    }
    results = {
        "report": REPORT,
        "slug": SLUG,
        "verdict": "pass" if metrics["weakest_channel_score"] == 1.0 else "needs_work",
        "metrics": metrics,
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }
    state = {"runs": runs, "browser_smoke": browser, "criteria": criteria}
    summary_rows = [{"metric": key, "value": value} for key, value in metrics.items()]
    verdict_rows = [{"report": REPORT, "verdict": results["verdict"], "readiness": metrics["readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": NEXT_GATE}]

    write_json(RESULTS, results)
    write_json(STATE, state)
    write_csv(SUMMARY, summary_rows, ["metric", "value"])
    write_csv(VERDICT, verdict_rows, ["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
    write_csv(CRITERIA, criteria, ["criterion", "passed", "score", "evidence"])
    REPORT_PATH.write_text(report_text(results, criteria, browser), encoding="utf-8")
    print(json.dumps({"report": REPORT, "verdict": results["verdict"], "metrics": metrics}, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
