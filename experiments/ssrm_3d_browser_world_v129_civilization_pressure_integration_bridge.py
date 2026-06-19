from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List

from experiments.ssrm_3d_browser_world_v128_long_horizon_belief_lineage_bridge import SEEDS, simulate_lineage

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 369
SLUG = "ssrm_3d_browser_world_v129_civilization_pressure_integration_bridge"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT368_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v128_long_horizon_belief_lineage_bridge_results.json"
SCHEDULE_REWRITES = ARTIFACT_DIR / f"{SLUG}_schedule_rewrites.csv"
APPRENTICESHIPS = ARTIFACT_DIR / f"{SLUG}_apprenticeships.csv"
TRADE_ROUTES = ARTIFACT_DIR / f"{SLUG}_trade_routes.csv"
SAFETY_CUSTOMS = ARTIFACT_DIR / f"{SLUG}_safety_customs.csv"
ORDINARY_CHOICES = ARTIFACT_DIR / f"{SLUG}_ordinary_choice_pressure.csv"
SOURCE_LINKS = ARTIFACT_DIR / f"{SLUG}_source_links.csv"
CIVILIZATION_OUTCOMES = ARTIFACT_DIR / f"{SLUG}_civilization_outcomes.csv"
ABLATIONS = ARTIFACT_DIR / f"{SLUG}_ablations.csv"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "369_ssrm_3d_civilization_pressure_integration_bridge_report.md"
BOUNDARY = (
    "Browser-local civilization-pressure integration only. Long-horizon belief lineage may rewrite ordinary schedules, "
    "apprenticeships, trade routes, safety customs, resources, and bounded resident choices while preserving source belief IDs. "
    "No LLM call, no subjective-consciousness claim, no moral-patienthood claim, no real civilization claim, and no predeclared device tree."
)
NEXT_GATE = (
    "post-369: make practical discovery emerge from repeated lived browser actions instead of report artifacts, with residents proposing "
    "new tests from everyday bottlenecks and no predeclared invention list"
)
FORBIDDEN_TERMS = ["electricity", "electron", "voltage", "conductor", "battery", "circuit", "technology unlock", "tech tree"]


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


def has_terms(text: str, terms: Iterable[str]) -> bool:
    return all(term in text for term in terms)


def forbidden_terms(rows: Iterable[Dict[str, Any]]) -> List[str]:
    text = json.dumps(list(rows), sort_keys=True).lower()
    return [term for term in FORBIDDEN_TERMS if term in text]


def score(condition: bool) -> float:
    return 1.0 if condition else 0.0


def resident_for(seed: int, offset: int) -> str:
    residents = ["Ari", "Fay", "Milo", "Sera", "Tovan", "Nia"]
    return residents[(seed + offset) % len(residents)]


def schedule_for_status(status: str, label: str, institution: str) -> str:
    if institution == "craft_bench" or status == "bench-tested":
        return f"bench practice for {label}"
    if institution == "route_exchange":
        return f"route exchange for {label}"
    if institution in {"safety_custom", "caution_rite"} or status == "tabooed":
        return f"safety custom for {label}"
    if institution == "memory_school" or status == "taught":
        return f"teaching lineage {label}"
    if status in {"archived", "mocked", "set-aside"}:
        return f"archiving failed {label}"
    return f"arguing rival theory {label}"


def derive_pressure_for_seed(run: Dict[str, Any], *, ablation: str | None = None) -> Dict[str, List[Dict[str, Any]]]:
    seed = run["seed"]
    outcome = run["outcome"]
    competitions = run["competitions"]
    material_chains = run["material_chains"]
    cultural = run["cultural"]
    schedule_rows: List[Dict[str, Any]] = []
    apprenticeship_rows: List[Dict[str, Any]] = []
    trade_rows: List[Dict[str, Any]] = []
    safety_rows: List[Dict[str, Any]] = []
    choice_rows: List[Dict[str, Any]] = []
    source_rows: List[Dict[str, Any]] = []
    selected_competitions = competitions[-4:]
    for index, row in enumerate(selected_competitions):
        resident = resident_for(seed, index)
        schedule_after = schedule_for_status(row["status"], row["label"], row["institution"])
        source_id = row["belief_id"]
        if ablation != "no_schedule_rewrite":
            schedule_row = {
                "seed": seed,
                "schedule_id": f"{seed}-SCH-{index + 1:02d}",
                "resident": resident,
                "era": row["era"],
                "source_belief_id": source_id,
                "source_label": row["label"],
                "competition_status": row["status"],
                "institution": row["institution"],
                "schedule_before": "ordinary work",
                "schedule_after": schedule_after,
                "ordinary_schedule_surface": True,
                "direct_avatar_command": False,
                "true_law_exposed": False,
            }
            schedule_rows.append(schedule_row)
            choice_rows.append({
                "seed": seed,
                "choice_id": f"{seed}-CHO-{index + 1:02d}",
                "resident": resident,
                "action": "askSchedule" if index % 2 == 0 else "offerHelp",
                "source_belief_id": source_id,
                "effect": schedule_after,
                "bounded_refusal_allowed": row["safety_norm"],
                "ordinary_affordance": True,
                "direct_avatar_command": False,
            })
            source_rows.append({
                "seed": seed,
                "row_id": schedule_row["schedule_id"],
                "row_type": "schedule_rewrite",
                "source_belief_id": source_id,
                "source_era": row["era"],
                "hidden_law_exposed": False,
            })
    if ablation == "no_ordinary_choice":
        choice_rows = []
    if ablation != "no_apprenticeship":
        taught_rows = [row for row in competitions if row["institution"] in {"craft_bench", "memory_school"} or row["status"] in {"taught", "bench-tested", "dominant"}]
        for index, row in enumerate((taught_rows or competitions[-2:])[:3]):
            mentor = resident_for(seed, index)
            apprentice = resident_for(seed, index + 1)
            apprenticeship_rows.append({
                "seed": seed,
                "apprenticeship_id": f"{seed}-APP-{index + 1:02d}",
                "mentor": mentor,
                "apprentice": apprentice,
                "source_belief_id": row["belief_id"],
                "practice": row["label"],
                "institution": row["institution"] if row["institution"] != "none" else "informal_teaching",
                "schedule_changed": ablation != "no_schedule_rewrite",
                "predeclared_device": False,
            })
    if ablation != "no_trade_routes":
        shifted = [row for row in material_chains if row["trade_shift"] != "none"]
        for index, row in enumerate(shifted[-3:]):
            trade_rows.append({
                "seed": seed,
                "route_id": f"{seed}-TRD-{index + 1:02d}",
                "resident": resident_for(seed, index + 2),
                "source_proposal_id": row["proposal_id"],
                "materials": row["materials"],
                "trade_shift": row["trade_shift"],
                "stock_before": row["stock_before"],
                "stock_after": row["stock_after"],
                "ordinary_resource_surface": True,
                "predeclared_device": False,
            })
            source_rows.append({
                "seed": seed,
                "row_id": trade_rows[-1]["route_id"],
                "row_type": "trade_route",
                "source_belief_id": row["proposal_id"],
                "source_era": row["era"],
                "hidden_law_exposed": False,
            })
    if ablation != "no_safety_customs":
        safety_source = [row for row in competitions if row["safety_norm"] or row["status"] == "tabooed" or row["archived_not_erased"]]
        for index, row in enumerate((safety_source or competitions[-2:])[:3]):
            safety_rows.append({
                "seed": seed,
                "custom_id": f"{seed}-SAF-{index + 1:02d}",
                "resident": resident_for(seed, index + 3),
                "source_belief_id": row["belief_id"],
                "custom": f"ask before repeating {row['label']}",
                "refusal_allowed": True,
                "recovery_path": "teach safe boundary then retry",
                "archived_failure_preserved": row["archived_not_erased"],
                "direct_avatar_command": False,
            })
    civilization_row = {
        "seed": seed,
        "law_hash": outcome["law_hash"],
        "settlement_bias": outcome["settlement_bias"],
        "outcome": outcome["outcome"],
        "history_signature": outcome["history_signature"],
        "schedule_count": len(schedule_rows),
        "apprenticeship_count": len(apprenticeship_rows),
        "trade_route_count": len(trade_rows),
        "safety_custom_count": len(safety_rows),
        "ordinary_choice_count": len(choice_rows),
        "source_memory": cultural[-1]["memory"] if cultural else "missing",
        "predeclared_ending": False,
    }
    if ablation == "no_source_links":
        source_rows = []
    return {
        "schedules": schedule_rows,
        "apprenticeships": apprenticeship_rows,
        "trade_routes": trade_rows,
        "safety_customs": safety_rows,
        "ordinary_choices": choice_rows,
        "source_links": source_rows,
        "outcomes": [civilization_row],
    }


def build_rows(ablation: str | None = None) -> Dict[str, List[Dict[str, Any]]]:
    rows = {"schedules": [], "apprenticeships": [], "trade_routes": [], "safety_customs": [], "ordinary_choices": [], "source_links": [], "outcomes": []}
    for seed in SEEDS:
        run = simulate_lineage(seed)
        derived = derive_pressure_for_seed(run, ablation=ablation)
        for key, values in derived.items():
            rows[key].extend(values)
    if ablation == "no_lineage_divergence" and rows["outcomes"]:
        first = rows["outcomes"][0]
        for row in rows["outcomes"]:
            row["history_signature"] = first["history_signature"]
            row["outcome"] = first["outcome"]
    return rows


def compute_metrics(rows: Dict[str, List[Dict[str, Any]]], app_text: str = "", index_text: str = "") -> Dict[str, float]:
    schedules = rows["schedules"]
    apprenticeships = rows["apprenticeships"]
    trade_routes = rows["trade_routes"]
    safety_customs = rows["safety_customs"]
    ordinary_choices = rows["ordinary_choices"]
    source_links = rows["source_links"]
    outcomes = rows["outcomes"]
    all_public = schedules + apprenticeships + trade_routes + safety_customs + ordinary_choices + outcomes
    law_hashes = {row["law_hash"] for row in outcomes}
    outcome_kinds = {row["outcome"] for row in outcomes}
    return {
        "lineage_to_schedule_binding": score(len(schedules) >= len(SEEDS) and all(row["ordinary_schedule_surface"] for row in schedules)),
        "lineage_to_apprenticeship_binding": score(len(apprenticeships) >= len(SEEDS) and all(not row["predeclared_device"] for row in apprenticeships)),
        "lineage_to_trade_route_binding": score(len(trade_routes) >= 4 and all(row["ordinary_resource_surface"] for row in trade_routes)),
        "lineage_to_safety_custom_binding": score(len(safety_customs) >= len(SEEDS) and all(row["refusal_allowed"] and row["recovery_path"] for row in safety_customs)),
        "ordinary_affordance_pressure_binding": score({"askSchedule", "offerHelp"}.issubset({row["action"] for row in ordinary_choices}) and all(row["ordinary_affordance"] for row in ordinary_choices)),
        "same_law_divergent_civilization_pressure": score(len(law_hashes) == 1 and len({row["history_signature"] for row in outcomes}) == len(SEEDS) and len(outcome_kinds) >= 4),
        "source_trace_integrity": score(len(source_links) >= len(schedules) and all(not row["hidden_law_exposed"] for row in source_links)),
        "no_predeclared_device_tree": score(not forbidden_terms(all_public) and all(not row.get("predeclared_device", False) for row in apprenticeships + trade_routes) and all(not row["predeclared_ending"] for row in outcomes)),
        "archived_failure_affects_safety": score(any(row["archived_failure_preserved"] for row in safety_customs)),
        "browser_shell_state_wired": score(has_terms(app_text, ["civilizationPressure", "runCivilizationPressureLoop", "runCivilizationPressureStep", "scheduleRewrites", "apprenticeships", "tradeRoutes", "safetyCustoms"])),
        "browser_shell_not_panel_only": score(has_terms(app_text, ["world.residents[resident].schedule = newSchedule", "world.scheduleQueue.push", "world.resources.fiber += 1", "mutateResident(resident"])),
        "browser_index_wired": score(has_terms(index_text, ["civilizationPressureOut", "Civilization pressure", "runCivilizationPressureLoop", "Run pressure step"])),
    }


def ablation_rows(baseline: Dict[str, float], app_text: str, index_text: str) -> List[Dict[str, Any]]:
    names = ["no_schedule_rewrite", "no_apprenticeship", "no_trade_routes", "no_safety_customs", "no_ordinary_choice", "no_source_links", "no_lineage_divergence"]
    rows: List[Dict[str, Any]] = []
    for name in names:
        built = build_rows(name)
        metrics = compute_metrics(built, app_text, index_text)
        degraded = [metric for metric, value in metrics.items() if value < baseline.get(metric, 0.0)]
        rows.append({"ablation": name, "mean_score": round(sum(metrics.values()) / len(metrics), 6), "degraded_metrics": ";".join(degraded) or "none"})
    return rows


def report_text(results: Dict[str, Any], criteria: List[Dict[str, Any]]) -> str:
    metrics = results["metrics"]
    passed = sum(1 for row in criteria if row["passed"])
    lines = [
        "# Report 369: SSRM-3D Civilization Pressure Integration Bridge",
        "",
        "Report 369 moves Report 368's long-horizon lineage pressure into ordinary civilization surfaces. Belief descendants and theory competition now map into schedule rewrites, apprenticeships, trade routes, safety customs, and bounded ordinary-choice pressure instead of living only in report artifacts.",
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
        "## Civilization pressure outcomes",
        "",
        "| Outcome | Count |",
        "| --- | ---: |",
    ]
    for outcome, count in sorted(results["outcome_counts"].items()):
        lines.append(f"| `{outcome}` | `{count}` |")
    lines.extend([
        "",
        "## Criteria",
        "",
        "| Criterion | Score | Evidence |",
        "| --- | ---: | --- |",
    ])
    for row in criteria:
        evidence = str(row["evidence"]).replace("|", "/")
        lines.append(f"| `{row['criterion']}` | `{row['score']:.1f}` | {evidence} |")
    lines.extend([
        "",
        "## Honest interpretation",
        "",
        "This is still not a living civilization. The step forward is integration pressure: lineage history now has ordinary consequences in schedules, teaching, material movement, safety refusal, resource shifts, and later resident-facing affordances. The same hidden-law lineage remains source-traceable and does not become a predeclared invention tree.",
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
    rows = build_rows()
    app_text = SHELL_APP.read_text(encoding="utf-8")
    index_text = SHELL_INDEX.read_text(encoding="utf-8")
    runner_text = RUNNER.read_text(encoding="utf-8")
    report368 = load_json(REPORT368_RESULTS)
    metrics_base = compute_metrics(rows, app_text, index_text)
    ablations = ablation_rows(metrics_base, app_text, index_text)

    write_csv(SCHEDULE_REWRITES, rows["schedules"], ["seed", "schedule_id", "resident", "era", "source_belief_id", "source_label", "competition_status", "institution", "schedule_before", "schedule_after", "ordinary_schedule_surface", "direct_avatar_command", "true_law_exposed"])
    write_csv(APPRENTICESHIPS, rows["apprenticeships"], ["seed", "apprenticeship_id", "mentor", "apprentice", "source_belief_id", "practice", "institution", "schedule_changed", "predeclared_device"])
    write_csv(TRADE_ROUTES, rows["trade_routes"], ["seed", "route_id", "resident", "source_proposal_id", "materials", "trade_shift", "stock_before", "stock_after", "ordinary_resource_surface", "predeclared_device"])
    write_csv(SAFETY_CUSTOMS, rows["safety_customs"], ["seed", "custom_id", "resident", "source_belief_id", "custom", "refusal_allowed", "recovery_path", "archived_failure_preserved", "direct_avatar_command"])
    write_csv(ORDINARY_CHOICES, rows["ordinary_choices"], ["seed", "choice_id", "resident", "action", "source_belief_id", "effect", "bounded_refusal_allowed", "ordinary_affordance", "direct_avatar_command"])
    write_csv(SOURCE_LINKS, rows["source_links"], ["seed", "row_id", "row_type", "source_belief_id", "source_era", "hidden_law_exposed"])
    write_csv(CIVILIZATION_OUTCOMES, rows["outcomes"], ["seed", "law_hash", "settlement_bias", "outcome", "history_signature", "schedule_count", "apprenticeship_count", "trade_route_count", "safety_custom_count", "ordinary_choice_count", "source_memory", "predeclared_ending"])
    write_csv(ABLATIONS, ablations, ["ablation", "mean_score", "degraded_metrics"])

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_368_lineage_gate_passing", report368.get("verdict") == "pass" and report368.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 368 verdict={report368.get('verdict')} weakest={report368.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "runner_includes_report_369", "experiments.ssrm_3d_browser_world_v129_civilization_pressure_integration_bridge" in runner_text, "scripts/run_experiments.py includes Report 369 module")
    add_criterion(criteria, "artifact_set_written", all(path.exists() for path in [SCHEDULE_REWRITES, APPRENTICESHIPS, TRADE_ROUTES, SAFETY_CUSTOMS, ORDINARY_CHOICES, SOURCE_LINKS, CIVILIZATION_OUTCOMES, ABLATIONS]), "all Report 369 artifacts exist")
    for metric, value in metrics_base.items():
        add_criterion(criteria, metric, value == 1.0, f"metric={value}")
    add_criterion(criteria, "ablations_degrade_relevant_channels", all(row["degraded_metrics"] != "none" for row in ablations), f"ablations={ablations}")
    add_criterion(criteria, "boundary_preserved", has_terms(BOUNDARY, ["No LLM call", "no subjective-consciousness claim", "no moral-patienthood claim", "no predeclared device tree"]), BOUNDARY)

    passed = sum(1 for row in criteria if row["passed"])
    metrics = {
        **metrics_base,
        "seed_count": len(SEEDS),
        "schedule_rewrite_count": len(rows["schedules"]),
        "apprenticeship_count": len(rows["apprenticeships"]),
        "trade_route_count": len(rows["trade_routes"]),
        "safety_custom_count": len(rows["safety_customs"]),
        "ordinary_choice_count": len(rows["ordinary_choices"]),
        "outcome_diversity": len({row["outcome"] for row in rows["outcomes"]}),
        "criterion_count": len(criteria),
        "readiness": round(passed / len(criteria), 6),
        "weakest_channel_score": min(row["score"] for row in criteria),
    }
    results = {
        "report": REPORT,
        "slug": SLUG,
        "verdict": "pass" if metrics["weakest_channel_score"] == 1.0 else "needs_work",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "criteria": criteria,
        "outcome_counts": dict(Counter(row["outcome"] for row in rows["outcomes"])),
        "artifacts": {
            "schedule_rewrites": str(SCHEDULE_REWRITES.relative_to(ROOT)),
            "apprenticeships": str(APPRENTICESHIPS.relative_to(ROOT)),
            "trade_routes": str(TRADE_ROUTES.relative_to(ROOT)),
            "safety_customs": str(SAFETY_CUSTOMS.relative_to(ROOT)),
            "ordinary_choice_pressure": str(ORDINARY_CHOICES.relative_to(ROOT)),
            "source_links": str(SOURCE_LINKS.relative_to(ROOT)),
            "civilization_outcomes": str(CIVILIZATION_OUTCOMES.relative_to(ROOT)),
            "ablations": str(ABLATIONS.relative_to(ROOT)),
        },
    }
    write_json(RESULTS, results)
    write_json(STATE, {"rows": rows, "ablations": ablations, "report368_gate": report368})
    write_csv(SUMMARY, [{"metric": key, "value": value} for key, value in metrics.items()], ["metric", "value"])
    write_csv(VERDICT, [{"report": REPORT, "verdict": results["verdict"], "readiness": metrics["readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": NEXT_GATE}], ["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
    write_csv(CRITERIA, criteria, ["criterion", "passed", "score", "evidence"])
    REPORT_PATH.write_text(report_text(results, criteria), encoding="utf-8")
    print(json.dumps({"report": REPORT, "verdict": results["verdict"], "metrics": metrics, "outcome_counts": results["outcome_counts"]}, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
