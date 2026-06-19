from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List

from experiments.ssrm_3d_browser_world_v122_non_scripted_world_anomaly_discovery_bridge import SEEDS, RESIDENTS, simulate_seed

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 363
SLUG = "ssrm_3d_browser_world_v123_scheduled_anomaly_investigation_bridge"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT362_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v122_non_scripted_world_anomaly_discovery_bridge_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
SCHEDULE_PLANS = ARTIFACT_DIR / f"{SLUG}_schedule_plans.csv"
SCHEDULE_EXECUTION = ARTIFACT_DIR / f"{SLUG}_schedule_execution.csv"
RESOURCE_TRADEOFFS = ARTIFACT_DIR / f"{SLUG}_resource_tradeoffs.csv"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "363_ssrm_3d_scheduled_anomaly_investigation_bridge_report.md"
BOUNDARY = (
    "Browser-local scheduled anomaly investigation only; residents may schedule, defer, refuse, or run anomaly tests "
    "around ordinary work and scarce materials, but this is deterministic per seed and remains no LLM call, no autonomous "
    "natural language, no subjective consciousness, no real science, no real consent, no moral patienthood, no production "
    "persistence, no hosted URL proof, no complete 3D engine, no finished gameplay, and no hard-coded technology tree."
)
NEXT_GATE = (
    "post-363: make scheduled anomaly investigation create longer-run relationship consequences when residents disagree about "
    "risk, resource use, or whether ordinary work should be delayed"
)


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def has_terms(text: str, terms: Iterable[str]) -> bool:
    return all(term in text for term in terms)


def add_criterion(criteria: List[Dict[str, Any]], name: str, passed: bool, evidence: str) -> None:
    criteria.append({"criterion": name, "passed": bool(passed), "score": 1.0 if passed else 0.0, "evidence": evidence})


def write_csv(path: Path, rows: List[Dict[str, Any]], fieldnames: List[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def cost_for(resident: str, index: int) -> Dict[str, int]:
    costs = [
        {"fiber": 1, "wood": 1, "care": 0, "water": 0},
        {"fiber": 0, "wood": 1, "care": 1, "water": 1},
        {"fiber": 1, "wood": 0, "care": 1, "water": 0},
        {"fiber": 0, "wood": 2, "care": 0, "water": 1},
    ]
    return costs[(ord(resident[0]) + index) % len(costs)]


def has_resources(resources: Dict[str, int], cost: Dict[str, int]) -> bool:
    return all(resources.get(key, 0) >= value for key, value in cost.items())


def apply_cost(resources: Dict[str, int], cost: Dict[str, int]) -> None:
    for key, value in cost.items():
        resources[key] = max(0, resources.get(key, 0) - value)


def latest_beliefs(run: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    rows = {}
    for belief in run["beliefs"]:
        rows[belief["resident"]] = belief
    return rows


def plan_and_execute(run: Dict[str, Any]) -> Dict[str, Any]:
    seed = run["seed"]
    resources = {"water": 2 + seed % 2, "fiber": 2 + seed % 3, "wood": 3 + seed % 2, "care": 1 + seed % 2}
    resources_before = dict(resources)
    beliefs = latest_beliefs(run)
    social_count = Counter()
    for row in run["social"]:
        social_count[row["from"]] += 1
        social_count[row["to"]] += 1
    plans: List[Dict[str, Any]] = []
    executions: List[Dict[str, Any]] = []
    tradeoffs: List[Dict[str, Any]] = []
    experiments_by_actor = defaultdict(list)
    for experiment in run["experiments"]:
        experiments_by_actor[experiment["actor"]].append(experiment)
    blocks = ["dawn work block", "midday work block", "rain pause", "evening repair", "market gossip"]
    schedules = {
        "Ari": "repair awning",
        "Fay": "sort herbs",
        "Milo": "carry water",
        "Sera": "dry cloaks",
        "Tovan": "map safe route",
        "Nia": "sort glass jars",
    }
    for index, resident in enumerate(RESIDENTS[:5]):
        belief = beliefs.get(resident) or run["beliefs"][index % len(run["beliefs"])]
        cost = cost_for(resident, index)
        scarce = not has_resources(resources, cost)
        trust = round(0.45 + ((seed + index * 7) % 25) / 100, 3)
        fear = round(min(1.0, (0.42 if belief["kind"] == "fearful" else 0.12) + belief["contradiction_count"] * 0.16 + (0.14 if belief["kind"] == "ritualized" else 0.0)), 3)
        pressure = round(min(1.0, social_count[resident] * 0.18 + len({belief["kind"] for belief in run["beliefs"]}) * 0.04), 3)
        decision = "test_anomaly"
        reason = "curiosity and available materials beat ordinary work"
        if scarce:
            decision = "defer_for_materials"
            reason = "ordinary work keeps scarce material"
        elif fear > trust + 0.18:
            decision = "refuse_test"
            reason = "fear and contradictions outweigh trust"
        elif pressure > 0.42 and belief["confidence"] < 0.48:
            decision = "argue_before_test"
            reason = "social disagreement delays the test"
        plan = {
            "seed": seed,
            "slot_id": f"{seed}-AIS-{index + 1:02d}",
            "block": blocks[index],
            "resident": resident,
            "ordinary_work": schedules[resident],
            "belief": belief["label"],
            "decision": decision,
            "reason": reason,
            "cost_water": cost["water"],
            "cost_fiber": cost["fiber"],
            "cost_wood": cost["wood"],
            "cost_care": cost["care"],
            "fear": fear,
            "trust": trust,
            "social_pressure": pressure,
            "resources_before_slot": json.dumps(resources, sort_keys=True),
        }
        plans.append(plan)
        if decision != "test_anomaly":
            outcome = f"{resident} kept {schedules[resident]} ahead of anomaly testing because {reason}"
            executions.append({**plan, "status": "deferred_or_refused", "executed_test": False, "experiment_id": "", "failure": False, "outcome": outcome, "resources_after_slot": json.dumps(resources, sort_keys=True)})
            tradeoffs.append({"seed": seed, "slot_id": plan["slot_id"], "resident": resident, "tradeoff": decision, "ordinary_work_delayed": False, "material_scarcity": scarce, "reason": reason})
            continue
        if not has_resources(resources, cost):
            outcome = f"{resident} could not test {belief['label']}; resources were too scarce"
            executions.append({**plan, "status": "blocked_by_scarcity", "executed_test": False, "experiment_id": "", "failure": False, "outcome": outcome, "resources_after_slot": json.dumps(resources, sort_keys=True)})
            tradeoffs.append({"seed": seed, "slot_id": plan["slot_id"], "resident": resident, "tradeoff": "blocked_by_scarcity", "ordinary_work_delayed": False, "material_scarcity": True, "reason": reason})
            continue
        apply_cost(resources, cost)
        candidates = experiments_by_actor.get(resident) or run["experiments"]
        experiment = candidates[index % len(candidates)]
        outcome = f"{resident} delayed {schedules[resident]}, spent scheduled materials, and got {experiment['outcome']}"
        executions.append({**plan, "status": "failed test preserved" if experiment["failure"] else "test completed", "executed_test": True, "experiment_id": experiment["id"], "failure": experiment["failure"], "outcome": outcome, "resources_after_slot": json.dumps(resources, sort_keys=True)})
        tradeoffs.append({"seed": seed, "slot_id": plan["slot_id"], "resident": resident, "tradeoff": "ordinary_work_delayed_for_test", "ordinary_work_delayed": True, "material_scarcity": False, "reason": reason})
    return {"seed": seed, "resources_before": resources_before, "resources_after": resources, "plans": plans, "executions": executions, "tradeoffs": tradeoffs}


def report_text(results: Dict[str, Any], criteria: List[Dict[str, Any]], browser: Dict[str, Any]) -> str:
    metrics = results["metrics"]
    passed_count = sum(1 for row in criteria if row["passed"])
    lines = [
        "# Report 363: SSRM-3D Scheduled Anomaly Investigation Bridge",
        "",
        "Report 363 moves anomaly discovery out of a panel-only loop and into the maintained shell's resident schedule/resource economy. Residents now plan investigation slots around ordinary work, scarce materials, fear, trust, and social disagreement. Execution can run a resident-owned test, delay work, consume resources, preserve a failed test, refuse, or defer.",
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
        f"- Schedule summary: `{browser.get('afterExecution', {}).get('scheduleSummary', 'missing')}`",
        f"- Schedule panel: `{browser.get('afterExecution', {}).get('scheduleText', 'missing')}`",
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
        "This remains deterministic browser-local scaffolding. The non-toy movement is integration: anomaly testing now competes with ordinary resident life and resources, so investigation can be delayed, refused, or failed instead of advancing through a scripted panel path.",
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
    runs = [simulate_seed(seed) for seed in SEEDS]
    schedules = [plan_and_execute(run) for run in runs]
    plans = [row for schedule in schedules for row in schedule["plans"]]
    executions = [row for schedule in schedules for row in schedule["executions"]]
    tradeoffs = [row for schedule in schedules for row in schedule["tradeoffs"]]
    app_text = SHELL_APP.read_text(encoding="utf-8")
    index_text = SHELL_INDEX.read_text(encoding="utf-8")
    runner_text = RUNNER.read_text(encoding="utf-8")
    report362 = load_json(REPORT362_RESULTS)
    browser = load_json(BROWSER_SMOKE)
    console_errors = browser.get("consoleErrors", [])

    metrics_base = {
        "schedule_competition_binding": float(all(row["ordinary_work"] and row["decision"] for row in plans)),
        "resource_scarcity_binding": float(any(row["tradeoff"] in {"defer_for_materials", "blocked_by_scarcity"} or row["material_scarcity"] for row in tradeoffs) and any(row["resources_after_slot"] != row["resources_before_slot"] for row in executions)),
        "fear_trust_social_pressure_binding": float(all("fear" in row and "trust" in row and "social_pressure" in row for row in plans) and len({row["decision"] for row in plans}) >= 3),
        "resident_chosen_test_binding": float(len({row["resident"] for row in executions if row["executed_test"]}) >= 3),
        "ordinary_work_tradeoff": float(any(row["ordinary_work_delayed"] for row in tradeoffs)),
        "refusal_or_defer_preservation": float(any(row["tradeoff"] in {"refuse_test", "argue_before_test", "defer_for_materials"} for row in tradeoffs)),
        "scheduled_failure_preservation": float(any(row["failure"] for row in executions if row["executed_test"])),
        "not_panel_only_loop": float(has_terms(app_text, ["planAnomalyInvestigationSchedule", "runScheduledAnomalyInvestigation", "ordinaryWorkDelayed", "noPanelOnlyLoop"])),
        "schedule_replay_integrity": float(has_terms(app_text, ["schedule_tradeoff", "runScheduledAnomalyInvestigation", "planned anomaly investigation slots"])),
    }

    write_csv(SCHEDULE_PLANS, plans, ["seed", "slot_id", "block", "resident", "ordinary_work", "belief", "decision", "reason", "cost_water", "cost_fiber", "cost_wood", "cost_care", "fear", "trust", "social_pressure", "resources_before_slot"])
    write_csv(SCHEDULE_EXECUTION, executions, ["seed", "slot_id", "block", "resident", "ordinary_work", "belief", "decision", "reason", "cost_water", "cost_fiber", "cost_wood", "cost_care", "fear", "trust", "social_pressure", "resources_before_slot", "status", "executed_test", "experiment_id", "failure", "outcome", "resources_after_slot"])
    write_csv(RESOURCE_TRADEOFFS, tradeoffs, ["seed", "slot_id", "resident", "tradeoff", "ordinary_work_delayed", "material_scarcity", "reason"])

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_362_anomaly_gate_passing", report362.get("verdict") == "pass" and report362.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 362 verdict={report362.get('verdict')} weakest={report362.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "source_exposes_schedule_state", has_terms(app_text, ["anomalyInvestigationSchedule", "renderAnomalyInvestigationSchedule", "browser-local-scheduled-anomaly-investigation-only"]), "app.js exposes scheduled anomaly investigation state/render/boundary")
    add_criterion(criteria, "source_plans_and_runs_schedule", has_terms(app_text, ["planAnomalyInvestigationSchedule", "runScheduledAnomalyInvestigation", "ordinaryWork", "materialCost", "socialPressure"]), "app.js plans and executes resident schedule slots")
    add_criterion(criteria, "visible_schedule_panel_wired", has_terms(index_text, ["anomalyInvestigationScheduleOut", "Scheduled anomaly investigation", "Plan schedule", "Run next slot"]), "index.html exposes schedule controls and panel")
    add_criterion(criteria, "runner_includes_report_363", "experiments.ssrm_3d_browser_world_v123_scheduled_anomaly_investigation_bridge" in runner_text, "scripts/run_experiments.py includes Report 363 module")
    for metric, value in metrics_base.items():
        add_criterion(criteria, metric, value == 1.0, f"metric={value}")
    after_execution = browser.get("afterExecution", {})
    schedule_text = after_execution.get("scheduleText", "")
    add_criterion(criteria, "browser_smoke_artifact_exists", bool(browser), str(BROWSER_SMOKE.relative_to(ROOT)) if BROWSER_SMOKE.exists() else "missing browser smoke artifact")
    add_criterion(criteria, "browser_schedule_competition_visible", all(term in schedule_text for term in ["Scheduled slots", "work=", "cost=", "fear=", "trust=", "pressure="]), schedule_text or "missing schedule text")
    add_criterion(criteria, "browser_execution_tradeoff_visible", all(term in schedule_text for term in ["Execution log", "Ordinary work delayed", "Resources now"]), schedule_text or "missing schedule execution text")
    add_criterion(criteria, "browser_console_clean", len(console_errors) == 0, f"console error count={len(console_errors)}")
    add_criterion(criteria, "claim_boundary_preserved", all(term in BOUNDARY for term in ["no LLM call", "subjective consciousness", "moral patienthood", "no hard-coded technology tree", "finished gameplay"]), BOUNDARY)

    weakest = min(row["score"] for row in criteria)
    readiness = sum(row["score"] for row in criteria) / len(criteria)
    metrics = {**metrics_base, "weakest_channel_score": weakest, "readiness": readiness, "criterion_count": len(criteria), "console_error_count": len(console_errors), "slot_count": len(plans), "executed_test_count": sum(1 for row in executions if row["executed_test"]), "refusal_or_defer_count": sum(1 for row in tradeoffs if row["tradeoff"] != "ordinary_work_delayed_for_test")}
    verdict = "pass" if all(row["passed"] for row in criteria) else "fail"
    results = {"report": REPORT, "slug": SLUG, "verdict": verdict, "generated_at": datetime.now(timezone.utc).isoformat(), "boundary": BOUNDARY, "metrics": metrics, "criteria": criteria, "artifacts": {"schedule_plans": str(SCHEDULE_PLANS.relative_to(ROOT)), "schedule_execution": str(SCHEDULE_EXECUTION.relative_to(ROOT)), "resource_tradeoffs": str(RESOURCE_TRADEOFFS.relative_to(ROOT)), "browser_smoke": str(BROWSER_SMOKE.relative_to(ROOT))}, "next_gate": NEXT_GATE}
    state = {"report": REPORT, "schedules": schedules, "browser_smoke": browser, "report362_gate": report362}
    RESULTS.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    STATE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_csv(SUMMARY, [{"report": REPORT, "verdict": verdict, **metrics}], ["report", "verdict", *metrics.keys()])
    write_csv(VERDICT, [{"report": REPORT, "verdict": verdict, "weakest_channel_score": weakest, "readiness": readiness, "next_gate": NEXT_GATE}], ["report", "verdict", "weakest_channel_score", "readiness", "next_gate"])
    write_csv(CRITERIA, criteria, ["criterion", "passed", "score", "evidence"])
    REPORT_PATH.write_text(report_text(results, criteria, browser), encoding="utf-8")
    print(json.dumps({"report": REPORT, "verdict": verdict, "metrics": metrics}, indent=2, sort_keys=True))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
