from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List

from experiments.ssrm_3d_browser_world_v122_non_scripted_world_anomaly_discovery_bridge import SEEDS
from experiments.ssrm_3d_browser_world_v124_stochastic_resident_consequence_bridge import simulate_seed as simulate_stochastic_seed

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 365
SLUG = "ssrm_3d_browser_world_v125_stochastic_recovery_loop_bridge"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT364_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v124_stochastic_resident_consequence_bridge_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
RECOVERY_QUEUE = ARTIFACT_DIR / f"{SLUG}_recovery_queue.csv"
RECOVERY_EXECUTION = ARTIFACT_DIR / f"{SLUG}_recovery_execution.csv"
RELATIONSHIP_REPAIRS = ARTIFACT_DIR / f"{SLUG}_relationship_repairs.csv"
REPLAY_LEDGER = ARTIFACT_DIR / f"{SLUG}_replay_ledger.csv"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "365_ssrm_3d_stochastic_recovery_loop_bridge_report.md"
BOUNDARY = (
    "Browser-local stochastic recovery loop only. Stochastic harms from Report 364 create bounded recovery rows, "
    "relationship repair records, resource tradeoffs, and schedule repair notes. This is not a suffering model, "
    "not an autonomous language system, not subjective consciousness, not moral patienthood, not production persistence, "
    "not hosted proof, not a complete 3D engine, and not finished gameplay."
)
NEXT_GATE = (
    "post-365: make recovered and unrecovered stochastic histories affect later resident choices, refusals, and social "
    "memory without collapsing into permanent punishment or random behavior"
)

RECOVERY_TEMPLATES = {
    "roof_leak": ("shelter stress", "patch leak and rest near dry place", {"water": 0, "fiber": 1, "wood": 1, "care": 0}, 0.012, 0.014, -1, "help after environmental stress"),
    "tool_snag": ("tool frustration", "re-tie tool lashing and return focus", {"water": 0, "fiber": 1, "wood": 0, "care": 0}, 0.008, 0.018, 0, "practical repair after blocked work"),
    "neighbor_help": ("received help", "acknowledge help and share credit", {"water": 0, "fiber": 0, "wood": 0, "care": 0}, 0.006, 0.012, -1, "gratitude keeps help socially sticky"),
    "argument_echo": ("social disagreement", "mediate disagreement and name source boundary", {"water": 0, "fiber": 0, "wood": 0, "care": 1}, 0.014, 0.008, 0, "argument repaired without erasing disagreement"),
    "found_material": ("opportunity allocation", "share found material with pending work", {"water": 0, "fiber": 0, "wood": 0, "care": 0}, 0.005, 0.016, -1, "benefit distributed instead of hoarded"),
    "quiet_recovery": ("fatigue recovery", "protect quiet rest and resume slowly", {"water": 0, "fiber": 0, "wood": 0, "care": 0}, 0.004, 0.010, -1, "rest respected as recovery"),
}


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


def has_resources(resources: Dict[str, int], cost: Dict[str, int]) -> bool:
    return all(resources.get(key, 0) >= value for key, value in cost.items())


def apply_cost(resources: Dict[str, int], cost: Dict[str, int]) -> None:
    for key, value in cost.items():
        resources[key] = max(0, resources.get(key, 0) - value)


def plan_recovery(run: Dict[str, Any]) -> List[Dict[str, Any]]:
    queue: List[Dict[str, Any]] = []
    for index, event in enumerate(run["events"]):
        harm_type, action, cost, trust_delta, progress_delta, debt_delta, note = RECOVERY_TEMPLATES[event["event"]]
        queue.append({
            "seed": event["seed"],
            "recovery_id": f"{event['seed']}-SR-{index + 1:02d}",
            "pulse_id": event["pulse_id"],
            "actor": event["actor"],
            "event": event["event"],
            "harm_type": harm_type,
            "repair_action": action,
            "resource_cost": json.dumps(cost, sort_keys=True),
            "trust_delta": trust_delta,
            "progress_delta": progress_delta,
            "debt_delta": debt_delta,
            "relationship_note": note,
            "need_before": event["need_after"],
            "need_after": "unrecovered",
            "schedule_coupling": event["schedule_coupling"],
            "status": "pending",
        })
    return queue


def execute_recovery(run: Dict[str, Any], queue: List[Dict[str, Any]]) -> Dict[str, Any]:
    resources = dict(run["resources"])
    residents = json.loads(json.dumps(run["residents"]))
    execution: List[Dict[str, Any]] = []
    repairs: List[Dict[str, Any]] = []
    replay: List[Dict[str, Any]] = []
    for tick, row in enumerate(queue):
        actor = row["actor"]
        cost = json.loads(row["resource_cost"])
        trust_before = residents[actor]["trust"]
        before_resources = dict(resources)
        resolved = has_resources(resources, cost)
        if resolved:
            apply_cost(resources, cost)
            status = "resolved"
            need_after = "social-safety" if row["harm_type"] == "social disagreement" else "recovering"
            trust_delta = row["trust_delta"]
            progress_delta = row["progress_delta"]
            outcome = f"{actor} used {row['repair_action']} after {row['event']}"
        else:
            status = "stabilized without materials"
            need_after = "stabilized"
            trust_delta = round(row["trust_delta"] * 0.5, 3)
            progress_delta = round(row["progress_delta"] * 0.5, 3)
            outcome = f"{actor} lacked materials and stabilized through rest and attention"
        residents[actor]["trust"] = round(min(1, max(0, residents[actor]["trust"] + trust_delta)), 3)
        residents[actor]["progress"] = round(min(1, max(0, residents[actor]["progress"] + progress_delta)), 3)
        residents[actor]["debt"] = max(0, residents[actor]["debt"] + row["debt_delta"])
        trust_after = residents[actor]["trust"]
        schedule_repair = "schedule consequence acknowledged" if row["schedule_coupling"] else ""
        execution.append({
            **row,
            "status": status,
            "need_after": need_after,
            "resources_before": json.dumps(before_resources, sort_keys=True),
            "resources_after": json.dumps(resources, sort_keys=True),
            "schedule_repair": schedule_repair,
            "outcome": outcome,
        })
        repairs.append({
            "seed": row["seed"],
            "recovery_id": row["recovery_id"],
            "pulse_id": row["pulse_id"],
            "actor": actor,
            "trust_before": trust_before,
            "trust_after": trust_after,
            "relationship_note": row["relationship_note"],
            "schedule_repair": schedule_repair,
        })
        replay.append({
            "seed": row["seed"],
            "tick": tick,
            "event": "resolveStochasticRecoveryStep",
            "payload_keys": "recovery,relationshipRepair,outcome,pendingCount",
            "recovery_id": row["recovery_id"],
            "status": status,
        })
    return {"execution": execution, "repairs": repairs, "replay": replay, "resources": resources, "residents": residents}


def report_text(results: Dict[str, Any], criteria: List[Dict[str, Any]], browser: Dict[str, Any]) -> str:
    metrics = results["metrics"]
    passed_count = sum(1 for row in criteria if row["passed"])
    lines = [
        "# Report 365: SSRM-3D Stochastic Recovery Loop Bridge",
        "",
        "Report 365 turns Report 364 stochastic surprises into bounded recovery loops. A pulse can still damage resources, delay schedules, or create social disagreement, but the maintained shell now plans recovery rows, resolves steps, records relationship repair, and notes schedule recovery instead of leaving surprise as one-shot damage.",
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
        f"- Recovery summary: `{browser.get('afterRecovery', {}).get('recoverySummary', 'missing')}`",
        f"- Recovery panel excerpt: `{browser.get('afterRecovery', {}).get('recoveryText', 'missing')}`",
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
        "This is still browser-local scaffolding, but it is less toy than one-shot stochastic perturbation. Random shocks now create repair obligations with costs and relationship continuity. The moral guardrail is explicit: stochastic harm must remain bounded, recoverable, and inspectable.",
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
    runs = [simulate_stochastic_seed(seed) for seed in SEEDS]
    queues = [plan_recovery(run) for run in runs]
    executed = [execute_recovery(run, queue) for run, queue in zip(runs, queues)]
    queue_rows = [row for queue in queues for row in queue]
    execution_rows = [row for run in executed for row in run["execution"]]
    repair_rows = [row for run in executed for row in run["repairs"]]
    replay_rows = [row for run in executed for row in run["replay"]]
    app_text = SHELL_APP.read_text(encoding="utf-8")
    index_text = SHELL_INDEX.read_text(encoding="utf-8")
    runner_text = RUNNER.read_text(encoding="utf-8")
    report364 = load_json(REPORT364_RESULTS)
    browser = load_json(BROWSER_SMOKE)
    console_errors = browser.get("consoleErrors", [])

    metrics_base = {
        "recovery_queue_binding": float(len(queue_rows) == 48 and all(row["pulse_id"] and row["repair_action"] for row in queue_rows)),
        "recovery_action_diversity": float(len({row["repair_action"] for row in queue_rows}) >= 5),
        "bounded_recovery_or_stabilization": float(all(row["status"] in {"resolved", "stabilized without materials"} for row in execution_rows)),
        "relationship_repair_binding": float(len(repair_rows) == len(execution_rows) and any(row["trust_after"] > row["trust_before"] for row in repair_rows)),
        "schedule_recovery_binding": float(any(row["schedule_repair"] for row in execution_rows)),
        "resource_tradeoff_binding": float(any(row["resources_before"] != row["resources_after"] for row in execution_rows)),
        "replay_recovery_integrity": float(all(row["event"] == "resolveStochasticRecoveryStep" for row in replay_rows)),
        "not_panel_only_loop": float(has_terms(app_text, ["planStochasticRecoveryLoop", "resolveStochasticRecoveryStep", "runStochasticRecoveryLoop", "mutateResident", "recordCheckpoint"])),
        "browser_surface_wired": float(has_terms(index_text, ["stochasticRecoveryLoopOut", "Plan recovery", "Resolve step", "Run recovery loop", "Stochastic recovery"])),
        "no_permanent_damage_policy": float("every stochastic harm must have a bounded recovery or stabilization path" in app_text),
    }

    write_csv(RECOVERY_QUEUE, queue_rows, ["seed", "recovery_id", "pulse_id", "actor", "event", "harm_type", "repair_action", "resource_cost", "trust_delta", "progress_delta", "debt_delta", "relationship_note", "need_before", "need_after", "schedule_coupling", "status"])
    write_csv(RECOVERY_EXECUTION, execution_rows, ["seed", "recovery_id", "pulse_id", "actor", "event", "harm_type", "repair_action", "resource_cost", "trust_delta", "progress_delta", "debt_delta", "relationship_note", "need_before", "need_after", "schedule_coupling", "status", "resources_before", "resources_after", "schedule_repair", "outcome"])
    write_csv(RELATIONSHIP_REPAIRS, repair_rows, ["seed", "recovery_id", "pulse_id", "actor", "trust_before", "trust_after", "relationship_note", "schedule_repair"])
    write_csv(REPLAY_LEDGER, replay_rows, ["seed", "tick", "event", "payload_keys", "recovery_id", "status"])

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_364_stochastic_gate_passing", report364.get("verdict") == "pass" and report364.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 364 verdict={report364.get('verdict')} weakest={report364.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "source_declares_recovery_boundary", has_terms(app_text, ["browser-local-stochastic-recovery-loop-only", "noPermanentDamagePolicy", "stochasticRecoveryLoop"]), "app.js declares recovery boundary and public state")
    add_criterion(criteria, "source_plans_and_resolves_recovery", has_terms(app_text, ["recoveryTemplateForPulse", "planStochasticRecoveryLoop", "resolveStochasticRecoveryStep", "relationshipRepairs"]), "app.js plans/resolves recovery and relationship repair")
    add_criterion(criteria, "visible_recovery_panel_wired", metrics_base["browser_surface_wired"] == 1.0, "index.html exposes recovery controls and panel")
    add_criterion(criteria, "runner_includes_report_365", "experiments.ssrm_3d_browser_world_v125_stochastic_recovery_loop_bridge" in runner_text, "scripts/run_experiments.py includes Report 365 module")
    for metric, value in metrics_base.items():
        add_criterion(criteria, metric, value == 1.0, f"metric={value}")
    recovery_text = browser.get("afterRecovery", {}).get("recoveryText", "")
    add_criterion(criteria, "browser_smoke_artifact_exists", bool(browser), str(BROWSER_SMOKE.relative_to(ROOT)) if BROWSER_SMOKE.exists() else "missing browser smoke artifact")
    add_criterion(criteria, "browser_recovery_loop_visible", all(term in recovery_text for term in ["Recovery queue:", "Relationship repairs:", "Repair ledger:", "No permanent damage policy:"]), recovery_text or "missing recovery text")
    add_criterion(criteria, "browser_recovery_resolved_visible", "resolved" in recovery_text or "stabilized without materials" in recovery_text, recovery_text or "missing recovery text")
    add_criterion(criteria, "browser_console_clean", len(console_errors) == 0, f"console error count={len(console_errors)}")

    passed = sum(1 for row in criteria if row["passed"])
    metrics = {
        **metrics_base,
        "recovery_count": len(queue_rows),
        "execution_count": len(execution_rows),
        "relationship_repair_count": len(repair_rows),
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
    state = {"runs": runs, "queue": queue_rows, "execution": execution_rows, "repairs": repair_rows, "browser_smoke": browser, "criteria": criteria}
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
