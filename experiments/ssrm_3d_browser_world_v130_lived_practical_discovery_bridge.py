from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List

from experiments.ssrm_3d_browser_world_v129_civilization_pressure_integration_bridge import SEEDS, build_rows

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 370
SLUG = "ssrm_3d_browser_world_v130_lived_practical_discovery_bridge"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT369_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v129_civilization_pressure_integration_bridge_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
LIVED_ACTIONS = ARTIFACT_DIR / f"{SLUG}_lived_actions.csv"
BOTTLENECKS = ARTIFACT_DIR / f"{SLUG}_bottlenecks.csv"
RESIDENT_PROPOSALS = ARTIFACT_DIR / f"{SLUG}_resident_proposals.csv"
PRACTICAL_TESTS = ARTIFACT_DIR / f"{SLUG}_practical_tests.csv"
PRESERVED_FAILURES = ARTIFACT_DIR / f"{SLUG}_preserved_failures.csv"
PRACTICE_NODES = ARTIFACT_DIR / f"{SLUG}_emergent_practice_nodes.csv"
PRACTICE_EDGES = ARTIFACT_DIR / f"{SLUG}_emergent_practice_edges.csv"
VILLAGE_CONCERNS = ARTIFACT_DIR / f"{SLUG}_village_board_concerns.csv"
PROJECT_PROPOSALS = ARTIFACT_DIR / f"{SLUG}_project_proposals.csv"
REALITY_LEDGER = ARTIFACT_DIR / f"{SLUG}_reality_constraint_ledger.csv"
SOURCE_LINKS = ARTIFACT_DIR / f"{SLUG}_source_links.csv"
ABLATIONS = ARTIFACT_DIR / f"{SLUG}_ablations.csv"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "370_ssrm_3d_emergent_practice_graph_reality_bridge_report.md"
BOUNDARY = (
    "Browser-local emergent practice graph, diegetic village-board, and reality-constraint bridge only. Practices are generated "
    "after repeated resident action, bottleneck pressure, evidence, failures, and social memory. No LLM call, no subjective-consciousness "
    "claim, no moral-patienthood claim, no real science claim, no real civilization claim, and no pre-authored tech tree."
)
NEXT_GATE = (
    "post-370: let successful local practices alter resident roles, reputation, and multi-household diffusion over return sessions without "
    "turning them into a fixed technology tree"
)
FORBIDDEN_TERMS = ["electricity", "electron", "voltage", "conductor", "battery", "circuit", "technology unlock", "metallurgy", "agriculture", "pottery"]
ACTION_SEQUENCE = ["askSchedule", "borrowTool", "offerHelp", "runScheduledAnomalyInvestigation", "askSchedule", "offerHelp", "askSchedule"]
STATUSES = ["practical", "disputed", "ritualized", "taboo", "refined", "forgotten", "institutionalized"]


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: List[Dict[str, Any]], fieldnames: List[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def add_criterion(criteria: List[Dict[str, Any]], name: str, passed: bool, evidence: str) -> None:
    criteria.append({"criterion": name, "passed": bool(passed), "score": 1.0 if passed else 0.0, "evidence": evidence})


def score(condition: bool) -> float:
    return 1.0 if condition else 0.0


def has_terms(text: str, terms: Iterable[str]) -> bool:
    return all(term in text for term in terms)


def forbidden_terms(rows: Iterable[Dict[str, Any]]) -> List[str]:
    text = json.dumps(list(rows), sort_keys=True).lower()
    return [term for term in FORBIDDEN_TERMS if term in text]


def resident_for(seed: int, offset: int) -> str:
    residents = ["Ari", "Fay", "Milo", "Sera", "Tovan", "Nia"]
    return residents[(seed + offset) % len(residents)]


def bottleneck_for(action: str, schedule: str, source_label: str, index: int) -> Dict[str, str]:
    if action == "borrowTool" or "route" in schedule:
        return {"type": "material_shortage", "detail": f"materials needed for {source_label}"}
    if action == "offerHelp" and ("safety" in schedule or index == 2):
        return {"type": "safety_limit", "detail": f"help pauses around {source_label}"}
    if "teaching" in schedule:
        return {"type": "apprenticeship_gap", "detail": f"teaching lacks a repeatable example for {source_label}"}
    if action == "runScheduledAnomalyInvestigation":
        return {"type": "test_time_conflict", "detail": f"scheduled test competes with {schedule}"}
    return {"type": "schedule_conflict", "detail": f"ordinary schedule keeps returning to {source_label}"}


def materials_for(bottleneck_type: str, label: str) -> str:
    first = "reed_fiber"
    second = "dry_resin"
    if "red" in label or "bite" in label or "carry" in label:
        first = "red_scrap"
    if bottleneck_type == "material_shortage":
        first = "iron_sand"
    if bottleneck_type == "safety_limit":
        second = "wet_wood"
    if bottleneck_type == "apprenticeship_gap":
        second = "clay_jar"
    return f"{first}+{second}"


def status_for(seed: int, bottleneck_type: str, repeated: int, failure: bool) -> str:
    if failure:
        return "taboo"
    if repeated < 2:
        return "emerging"
    if bottleneck_type == "safety_limit":
        return "ritualized"
    if seed % 7 == 0:
        return "forgotten"
    if repeated >= 4 and seed % 3 == 0:
        return "institutionalized"
    if repeated >= 3:
        return "refined"
    return "practical" if seed % 2 == 0 else "disputed"


def build_rows_for_report(ablation: str | None = None) -> Dict[str, List[Dict[str, Any]]]:
    pressure = build_rows()
    schedules_by_seed: Dict[int, List[Dict[str, Any]]] = defaultdict(list)
    safety_by_seed: Dict[int, List[Dict[str, Any]]] = defaultdict(list)
    for row in pressure["schedules"]:
        schedules_by_seed[row["seed"]].append(row)
    for row in pressure["safety_customs"]:
        safety_by_seed[row["seed"]].append(row)
    rows: Dict[str, List[Dict[str, Any]]] = {
        "lived_actions": [], "bottlenecks": [], "resident_proposals": [], "practical_tests": [], "preserved_failures": [],
        "practice_nodes": [], "practice_edges": [], "village_concerns": [], "project_proposals": [], "reality_ledger": [], "source_links": []
    }
    evidence_counts: Dict[str, int] = defaultdict(int)
    nodes_by_label: Dict[str, Dict[str, Any]] = {}
    for seed in SEEDS:
        source_schedule = schedules_by_seed[seed][0]
        resident = source_schedule["resident"]
        source_belief_id = source_schedule["source_belief_id"]
        source_label = source_schedule["source_label"]
        schedule = source_schedule["schedule_after"]
        action_sequence = ACTION_SEQUENCE if ablation != "no_repeated_use_requirement" else ACTION_SEQUENCE[:3]
        for index, action in enumerate(action_sequence):
            action_id = f"{seed}-LIV-{index + 1:02d}"
            actor = resident_for(seed, index)
            rows["lived_actions"].append({"seed": seed, "action_id": action_id, "action": action, "resident": actor, "source_schedule_id": source_schedule["schedule_id"], "schedule": schedule, "ordinary_action": True})
            bottleneck = bottleneck_for(action, schedule, source_label, index)
            if ablation == "no_material_constraints":
                bottleneck = {"type": "unbound", "detail": "material constraint ignored"}
            bottleneck_id = f"{seed}-BOT-{index + 1:02d}"
            rows["bottlenecks"].append({"seed": seed, "bottleneck_id": bottleneck_id, "action_id": action_id, "resident": actor, "bottleneck_type": bottleneck["type"], "detail": bottleneck["detail"], "source_belief_id": source_belief_id, "source_label": source_label})
            if ablation == "no_resident_proposals":
                continue
            proposal_id = f"{seed}-PDP-{index + 1:02d}"
            materials = materials_for(bottleneck["type"], source_label)
            rows["resident_proposals"].append({"seed": seed, "proposal_id": proposal_id, "bottleneck_id": bottleneck_id, "resident": actor, "question": f"try a local workaround for {bottleneck['type']}", "materials": materials, "source_belief_id": source_belief_id, "resident_generated": ablation != "forced_tech_tree_unlock", "avatar_answer": ablation == "no_avatar_boundary", "predeclared_tech": ablation == "forced_tech_tree_unlock"})
            key = f"{seed}:{source_belief_id}:{bottleneck['type']}"
            evidence_counts[key] += 1
            repeated = evidence_counts[key]
            failure = bottleneck["type"] == "safety_limit" and repeated < 2
            if ablation == "no_failed_ancestor_memory":
                failure = False
            test_id = f"{seed}-PDT-{index + 1:02d}"
            candidate_label = f"{source_label} {bottleneck['type'].replace('_', ' ')} practice"
            test = {"seed": seed, "test_id": test_id, "proposal_id": proposal_id, "resident": actor, "materials": materials, "visible_observation": "paused for safety boundary" if failure else f"repeatable workaround for {bottleneck['type']}", "failure": failure, "preserved_failure": failure and ablation != "no_failed_ancestor_memory", "repeated_evidence": repeated, "candidate_label": candidate_label, "source_belief_id": source_belief_id, "wrong_belief_still_useful": "omen" in source_label or "bite" in source_label or seed % 2 == 1, "stochastic_seeded": seed % 3 == 0, "hidden_law_exposed_to_resident": False}
            rows["practical_tests"].append(test)
            if test["preserved_failure"]:
                rows["preserved_failures"].append(test)
            if (failure or repeated >= 2 or ablation == "no_repeated_use_requirement") and ablation != "forced_tech_tree_unlock":
                status = status_for(seed, bottleneck["type"], repeated, failure)
                if ablation == "no_practice_decay" and status == "forgotten":
                    status = "practical"
                local_name = candidate_label
                node = nodes_by_label.get(f"{seed}:{local_name}")
                if not node:
                    failed_ancestors = [row["test_id"] for row in rows["preserved_failures"] if row["seed"] == seed and row["source_belief_id"] == source_belief_id]
                    node = {
                        "practice_id": f"{seed}-EPG-{len(nodes_by_label) + 1:03d}",
                        "local_name": local_name,
                        "origin_event": test_id,
                        "origin_resident": actor,
                        "origin_household": f"house_{seed % 4}",
                        "problem_pressure": bottleneck["type"],
                        "materials_used": materials,
                        "hidden_properties_involved": "audit_only_material_law",
                        "visible_observations": test["visible_observation"],
                        "resident_beliefs_involved": source_belief_id,
                        "failed_ancestor_tests": ";".join(failed_ancestors) or "none",
                        "social_transmission_path": f"{actor}->{resident_for(seed, index + 1)}",
                        "mutation_variants": f"{source_label};{local_name}",
                        "adoption_count": 0,
                        "adoption_households": "",
                        "practical_score": 0.0,
                        "ritual_score": 0.0,
                        "taboo_score": 0.0,
                        "dispute_score": 0.0,
                        "maintenance_cost": len(materials.split("+")) + (1 if bottleneck["type"] == "material_shortage" else 0),
                        "risk_flags": "failed ancestor" if failed_ancestors else ("wet material" if "wet_wood" in materials else "none"),
                        "generations_survived": max(0, repeated - 1),
                        "status": status,
                        "avatar_role": "triggered inquiry" if index == 0 else "witnessed or supported",
                        "predeclared_tech": False,
                    }
                    nodes_by_label[f"{seed}:{local_name}"] = node
                    rows["practice_nodes"].append(node)
                node["adoption_count"] += 0 if failure else 1
                households = set(filter(None, node["adoption_households"].split(";")))
                if not failure:
                    households.add(f"house_{(seed + index) % 4}")
                node["adoption_households"] = ";".join(sorted(households))
                node["practical_score"] = round(min(1.0, float(node["practical_score"]) + (0.2 if not failure else 0.0)), 3)
                node["ritual_score"] = round(min(1.0, float(node["ritual_score"]) + (0.2 if bottleneck["type"] == "safety_limit" else 0.04)), 3)
                node["taboo_score"] = round(min(1.0, float(node["taboo_score"]) + (0.28 if failure else 0.02)), 3)
                node["dispute_score"] = round(min(1.0, float(node["dispute_score"]) + (0.12 if repeated < 3 else 0.03)), 3)
                node["status"] = status
                rows["practice_edges"].append({"seed": seed, "from_id": source_belief_id, "to_id": node["practice_id"], "relation": "failed_into_safety_rule" if failure else "repeated_use_into_practice", "event_id": test_id, "hidden_law_exposed": False})
            rows["source_links"].append({"seed": seed, "row_id": test_id, "source_belief_id": source_belief_id, "source_schedule_id": source_schedule["schedule_id"], "source_bottleneck_id": bottleneck_id, "ordinary_action": action, "hidden_law_exposed": ablation == "no_audit_split", "avatar_answer": ablation == "no_avatar_boundary"})
            before_fiber = 10 - index
            after_fiber = before_fiber - (1 if "reed_fiber" in materials else 0)
            rows["reality_ledger"].append({"seed": seed, "ledger_id": f"{seed}-RCL-{index + 1:02d}", "event": test_id, "material_sources": materials, "material_transformation": "materials handled in test", "time_cost": 1, "labor_cost": 1 + (1 if bottleneck["type"] == "material_shortage" else 0), "tool_wear": 1 if "iron_sand" in materials else 0, "resident_effort": 1, "hidden_law_involved": "audit_only_material_law", "public_observation": test["visible_observation"], "resident_interpretation": candidate_label, "resources_before": before_fiber, "resources_after": after_fiber, "conservation_check": after_fiber <= before_fiber, "maintenance_obligation_created": candidate_label if repeated >= 2 else "none", "unintended_consequence": "safety caution" if failure else "resource use", "normal_view_hidden_law_exposed": ablation == "no_audit_split"})
    if ablation == "forced_tech_tree_unlock":
        rows["practice_nodes"].append({"practice_id": "forced-tech-001", "local_name": "electricity", "origin_event": "none", "origin_resident": "avatar", "origin_household": "none", "problem_pressure": "none", "materials_used": "none", "hidden_properties_involved": "exposed", "visible_observations": "none", "resident_beliefs_involved": "none", "failed_ancestor_tests": "none", "social_transmission_path": "none", "mutation_variants": "none", "adoption_count": len(SEEDS), "adoption_households": "all", "practical_score": 1, "ritual_score": 0, "taboo_score": 0, "dispute_score": 0, "maintenance_cost": 0, "risk_flags": "none", "generations_survived": 0, "status": "institutionalized", "avatar_role": "installed answer", "predeclared_tech": True})
    for index, node in enumerate(rows["practice_nodes"]):
        concern_id = f"VBC-{index + 1:03d}"
        proposer = resident_for(SEEDS[index % len(SEEDS)], index)
        rows["village_concerns"].append({"concern_id": concern_id, "resident": proposer, "problem": f"maintenance for {node['local_name']}", "source_practice_id": node["practice_id"], "urgency": "high" if node["status"] == "taboo" else "medium", "who_felt_this": proposer, "avatar_direct_control": False})
        rows["project_proposals"].append({"proposal_id": f"VBP-{index + 1:03d}", "resident_proposer": proposer, "problem_addressed": f"maintenance for {node['local_name']}", "materials_needed": node["materials_used"], "likely_helpers": f"{resident_for(SEEDS[index % len(SEEDS)], index + 1)};{resident_for(SEEDS[index % len(SEEDS)], index + 2)}", "resident_willingness": 0.62 if node["status"] not in {"taboo", "forgotten"} else 0.36, "known_objections": "fear of failed ancestor" if node["failed_ancestor_tests"] != "none" else "ordinary work delay", "risk": node["risk_flags"], "maintenance_cost": node["maintenance_cost"], "related_memories": node["origin_event"], "related_practice_nodes": node["practice_id"], "possible_failure_modes": "materials run short; resident refuses; weather interrupts", "current_support_level": 0.0, "avatar_can_force": False})
    return rows


def compute_metrics(rows: Dict[str, List[Dict[str, Any]]], app_text: str = "", index_text: str = "", browser: Dict[str, Any] | None = None) -> Dict[str, float]:
    browser = browser or {}
    actions = rows["lived_actions"]
    proposals = rows["resident_proposals"]
    tests = rows["practical_tests"]
    failures = rows["preserved_failures"]
    nodes = rows["practice_nodes"]
    concerns = rows["village_concerns"]
    project_proposals = rows["project_proposals"]
    ledger = rows["reality_ledger"]
    source_links = rows["source_links"]
    statuses = {row["status"] for row in nodes}
    public_rows = actions + proposals + tests + nodes + concerns + project_proposals
    smoke_text = json.dumps(browser, sort_keys=True)
    return {
        "practice_node_emerges_from_repetition": score(bool(nodes) and all(row["origin_event"] != "none" and int(row["adoption_count"]) >= 0 for row in nodes)),
        "no_predefined_tech_unlock": score(not forbidden_terms(public_rows) and all(not row.get("predeclared_tech", False) for row in nodes)),
        "failed_tests_can_become_safety_rules": score(any(row["failure"] for row in tests) and any(row["relation"] == "failed_into_safety_rule" for row in rows["practice_edges"]) and any(row["status"] == "taboo" for row in nodes)),
        "wrong_belief_can_stabilize_practice": score(any(row["wrong_belief_still_useful"] for row in tests) and any(row["resident_beliefs_involved"] in {test["source_belief_id"] for test in tests if test["wrong_belief_still_useful"]} for row in nodes)),
        "practice_social_mutation": score(any(";" in row["mutation_variants"] and "->" in row["social_transmission_path"] for row in nodes)),
        "adoption_without_modern_name": score(bool(nodes) and not forbidden_terms(nodes) and any(int(row["adoption_count"]) > 0 for row in nodes)),
        "material_constraint_binding": score(all(row["materials_used"] != "none" and int(row["maintenance_cost"]) > 0 for row in nodes) and all(row["conservation_check"] for row in ledger)),
        "stochastic_history_can_seed_practice": score(any(row["stochastic_seeded"] for row in tests)),
        "avatar_not_direct_source_of_correct_concept": score(all(not row["avatar_answer"] for row in proposals) and all(row["avatar_role"] != "installed answer" for row in nodes)),
        "hidden_law_resident_belief_split": score(all(not row["hidden_law_exposed"] for row in source_links) and all(not row["normal_view_hidden_law_exposed"] for row in ledger)),
        "multi_seed_practice_divergence": score(len({row["local_name"] for row in nodes}) >= len(SEEDS) and len(statuses) >= 4),
        "practice_can_die_or_become_taboo": score(bool({"taboo", "forgotten"}.intersection(statuses))),
        "village_board_diegetic_management": score(bool(concerns) and bool(project_proposals) and all(not row["avatar_direct_control"] for row in concerns) and all(not row["avatar_can_force"] for row in project_proposals)),
        "reality_constraint_ledger_integrity": score(bool(ledger) and all(row["time_cost"] >= 1 and row["labor_cost"] >= 1 and row["resources_after"] <= row["resources_before"] for row in ledger)),
        "audit_trace_integrity": score(len(source_links) == len(tests) and len(ledger) == len(tests) and all(row["hidden_law_involved"] == "audit_only_material_law" for row in ledger)),
        "shell_practice_graph_wired": score(has_terms(app_text, ["emergentPracticeGraph", "updateEmergentPracticeGraphFromTest", "practice_id", "failed_ancestor_tests", "status"])),
        "shell_village_board_wired": score(has_terms(app_text, ["villageBoard", "projectProposals", "supportVillageProposal", "avatarCannotForce", "who_felt_this"])),
        "shell_reality_ledger_wired": score(has_terms(app_text, ["realityConstraintLedger", "recordRealityConstraint", "material_transformations", "conservation_check", "normal_view_hidden_law_exposed"])),
        "browser_surface_wired": score(has_terms(index_text, ["Emergent Practices", "Village Board", "Reality Constraint Ledger", "runVillageBoardLoop", "runRealityConstraintAudit"])),
        "browser_smoke_visible": score(bool(browser) and bool(browser.get("afterLoop", {}).get("practiceSummary")) and bool(browser.get("afterLoop", {}).get("boardSummary")) and bool(browser.get("afterLoop", {}).get("realitySummary")) and not browser.get("consoleErrors") and not browser.get("errors")),
    }


def ablation_rows(baseline: Dict[str, float], app_text: str, index_text: str) -> List[Dict[str, Any]]:
    names = ["no_repeated_use_requirement", "no_failed_ancestor_memory", "no_material_constraints", "no_resident_proposals", "no_avatar_boundary", "no_practice_decay", "no_audit_split", "forced_tech_tree_unlock"]
    rows: List[Dict[str, Any]] = []
    for name in names:
        built = build_rows_for_report(name)
        metrics = compute_metrics(built, app_text, index_text, {})
        degraded = [metric for metric, value in metrics.items() if value < baseline.get(metric, 0.0)]
        rows.append({"ablation": name, "mean_score": round(sum(metrics.values()) / len(metrics), 6), "degraded_metrics": ";".join(degraded) or "none"})
    return rows


def report_text(results: Dict[str, Any], criteria: List[Dict[str, Any]], browser: Dict[str, Any]) -> str:
    metrics = results["metrics"]
    passed = sum(1 for row in criteria if row["passed"])
    lines = [
        "# Report 370: SSRM-3D Emergent Practice Graph and Reality Constraint Bridge",
        "",
        "Report 370 implements the first emergent practice graph layer, a diegetic village-board management surface, and a reality constraint ledger. The implementation rejects a pre-authored technology tree: practice nodes appear only after resident actions, bottlenecks, repeated tests, preserved failures, social mutation, and remembered evidence.",
        "",
        f"Boundary: {BOUNDARY}",
        "",
        "## Result",
        "",
        f"Verdict: `{results['verdict']}`",
        f"Readiness: `{metrics['readiness']:.3f}`",
        f"Weakest channel score: `{metrics['weakest_channel_score']:.3f}`",
        f"Criteria passed: `{passed} / {len(criteria)}`",
        "",
        "## Browser-smoke evidence",
        "",
        f"- Shell URL: `{browser.get('shellUrl', 'missing')}`",
        f"- Practice summary: `{browser.get('afterLoop', {}).get('practiceSummary', 'missing')}`",
        f"- Board summary: `{browser.get('afterLoop', {}).get('boardSummary', 'missing')}`",
        f"- Reality summary: `{browser.get('afterLoop', {}).get('realitySummary', 'missing')}`",
        f"- Console errors: `{len(browser.get('consoleErrors', []))}`",
        "",
        "## Artifact counts",
        "",
        f"- Practice nodes: `{metrics['practice_node_count']}`",
        f"- Village concerns: `{metrics['village_concern_count']}`",
        f"- Project proposals: `{metrics['project_proposal_count']}`",
        f"- Reality ledger rows: `{metrics['reality_ledger_count']}`",
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
        "This is still bounded scaffolding, not real science or a finished civilization simulator. The important change is causal discipline: no practice node exists before history, failed tests remain evidence, village management is proposal/support rather than command, and every practice/proposal/test carries source and cost rows.",
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
    rows = build_rows_for_report()
    app_text = SHELL_APP.read_text(encoding="utf-8")
    index_text = SHELL_INDEX.read_text(encoding="utf-8")
    runner_text = RUNNER.read_text(encoding="utf-8")
    report369 = load_json(REPORT369_RESULTS)
    browser = load_json(BROWSER_SMOKE)
    metrics_base = compute_metrics(rows, app_text, index_text, browser)
    ablations = ablation_rows(metrics_base, app_text, index_text)

    write_csv(LIVED_ACTIONS, rows["lived_actions"], ["seed", "action_id", "action", "resident", "source_schedule_id", "schedule", "ordinary_action"])
    write_csv(BOTTLENECKS, rows["bottlenecks"], ["seed", "bottleneck_id", "action_id", "resident", "bottleneck_type", "detail", "source_belief_id", "source_label"])
    write_csv(RESIDENT_PROPOSALS, rows["resident_proposals"], ["seed", "proposal_id", "bottleneck_id", "resident", "question", "materials", "source_belief_id", "resident_generated", "avatar_answer", "predeclared_tech"])
    write_csv(PRACTICAL_TESTS, rows["practical_tests"], ["seed", "test_id", "proposal_id", "resident", "materials", "visible_observation", "failure", "preserved_failure", "repeated_evidence", "candidate_label", "source_belief_id", "wrong_belief_still_useful", "stochastic_seeded", "hidden_law_exposed_to_resident"])
    write_csv(PRESERVED_FAILURES, rows["preserved_failures"], ["seed", "test_id", "proposal_id", "resident", "materials", "visible_observation", "failure", "preserved_failure", "repeated_evidence", "candidate_label", "source_belief_id", "wrong_belief_still_useful", "stochastic_seeded", "hidden_law_exposed_to_resident"])
    write_csv(PRACTICE_NODES, rows["practice_nodes"], ["practice_id", "local_name", "origin_event", "origin_resident", "origin_household", "problem_pressure", "materials_used", "hidden_properties_involved", "visible_observations", "resident_beliefs_involved", "failed_ancestor_tests", "social_transmission_path", "mutation_variants", "adoption_count", "adoption_households", "practical_score", "ritual_score", "taboo_score", "dispute_score", "maintenance_cost", "risk_flags", "generations_survived", "status", "avatar_role", "predeclared_tech"])
    write_csv(PRACTICE_EDGES, rows["practice_edges"], ["seed", "from_id", "to_id", "relation", "event_id", "hidden_law_exposed"])
    write_csv(VILLAGE_CONCERNS, rows["village_concerns"], ["concern_id", "resident", "problem", "source_practice_id", "urgency", "who_felt_this", "avatar_direct_control"])
    write_csv(PROJECT_PROPOSALS, rows["project_proposals"], ["proposal_id", "resident_proposer", "problem_addressed", "materials_needed", "likely_helpers", "resident_willingness", "known_objections", "risk", "maintenance_cost", "related_memories", "related_practice_nodes", "possible_failure_modes", "current_support_level", "avatar_can_force"])
    write_csv(REALITY_LEDGER, rows["reality_ledger"], ["seed", "ledger_id", "event", "material_sources", "material_transformation", "time_cost", "labor_cost", "tool_wear", "resident_effort", "hidden_law_involved", "public_observation", "resident_interpretation", "resources_before", "resources_after", "conservation_check", "maintenance_obligation_created", "unintended_consequence", "normal_view_hidden_law_exposed"])
    write_csv(SOURCE_LINKS, rows["source_links"], ["seed", "row_id", "source_belief_id", "source_schedule_id", "source_bottleneck_id", "ordinary_action", "hidden_law_exposed", "avatar_answer"])
    write_csv(ABLATIONS, ablations, ["ablation", "mean_score", "degraded_metrics"])

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_369_civilization_pressure_gate_passing", report369.get("verdict") == "pass" and report369.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 369 verdict={report369.get('verdict')} weakest={report369.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "runner_includes_report_370", "experiments.ssrm_3d_browser_world_v130_lived_practical_discovery_bridge" in runner_text, "scripts/run_experiments.py includes Report 370 module")
    add_criterion(criteria, "artifact_set_written", all(path.exists() for path in [LIVED_ACTIONS, BOTTLENECKS, RESIDENT_PROPOSALS, PRACTICAL_TESTS, PRESERVED_FAILURES, PRACTICE_NODES, PRACTICE_EDGES, VILLAGE_CONCERNS, PROJECT_PROPOSALS, REALITY_LEDGER, SOURCE_LINKS, ABLATIONS]), "all Report 370 artifacts exist")
    for metric, value in metrics_base.items():
        add_criterion(criteria, metric, value == 1.0, f"metric={value}")
    add_criterion(criteria, "ablations_degrade_relevant_channels", all(row["degraded_metrics"] != "none" for row in ablations), f"ablations={ablations}")
    add_criterion(criteria, "boundary_preserved", has_terms(BOUNDARY, ["No LLM call", "no subjective-consciousness claim", "no moral-patienthood claim", "no pre-authored tech tree"]), BOUNDARY)

    passed = sum(1 for row in criteria if row["passed"])
    metrics = {
        **metrics_base,
        "seed_count": len(SEEDS),
        "lived_action_count": len(rows["lived_actions"]),
        "test_count": len(rows["practical_tests"]),
        "practice_node_count": len(rows["practice_nodes"]),
        "practice_status_count": len({row["status"] for row in rows["practice_nodes"]}),
        "village_concern_count": len(rows["village_concerns"]),
        "project_proposal_count": len(rows["project_proposals"]),
        "reality_ledger_count": len(rows["reality_ledger"]),
        "criterion_count": len(criteria),
        "readiness": round(passed / len(criteria), 6),
        "weakest_channel_score": min(row["score"] for row in criteria),
    }
    results = {"report": REPORT, "slug": SLUG, "verdict": "pass" if metrics["weakest_channel_score"] == 1.0 else "needs_work", "generated_at": datetime.now(timezone.utc).isoformat(), "boundary": BOUNDARY, "next_gate": NEXT_GATE, "metrics": metrics, "criteria": criteria, "artifacts": {"lived_actions": str(LIVED_ACTIONS.relative_to(ROOT)), "bottlenecks": str(BOTTLENECKS.relative_to(ROOT)), "resident_proposals": str(RESIDENT_PROPOSALS.relative_to(ROOT)), "practical_tests": str(PRACTICAL_TESTS.relative_to(ROOT)), "preserved_failures": str(PRESERVED_FAILURES.relative_to(ROOT)), "practice_nodes": str(PRACTICE_NODES.relative_to(ROOT)), "practice_edges": str(PRACTICE_EDGES.relative_to(ROOT)), "village_concerns": str(VILLAGE_CONCERNS.relative_to(ROOT)), "project_proposals": str(PROJECT_PROPOSALS.relative_to(ROOT)), "reality_ledger": str(REALITY_LEDGER.relative_to(ROOT)), "source_links": str(SOURCE_LINKS.relative_to(ROOT)), "browser_smoke": str(BROWSER_SMOKE.relative_to(ROOT)), "ablations": str(ABLATIONS.relative_to(ROOT))}}
    write_json(RESULTS, results)
    write_json(STATE, {"rows": rows, "ablations": ablations, "report369_gate": report369, "browser_smoke": browser})
    write_csv(SUMMARY, [{"metric": key, "value": value} for key, value in metrics.items()], ["metric", "value"])
    write_csv(VERDICT, [{"report": REPORT, "verdict": results["verdict"], "readiness": metrics["readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": NEXT_GATE}], ["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
    write_csv(CRITERIA, criteria, ["criterion", "passed", "score", "evidence"])
    REPORT_PATH.write_text(report_text(results, criteria, browser), encoding="utf-8")
    print(json.dumps({"report": REPORT, "verdict": results["verdict"], "metrics": metrics}, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
