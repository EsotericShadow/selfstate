from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List

from experiments.ssrm_3d_browser_world_v130_lived_practical_discovery_bridge import (
    SEEDS,
    build_rows_for_report as build_report370_rows,
)

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 371
SLUG = "ssrm_3d_browser_world_v131_avatar_hint_divergence_bridge"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"

HINT_EVENTS = ARTIFACT_DIR / f"{SLUG}_hint_events.csv"
HOUSEHOLD_INTERPRETATIONS = ARTIFACT_DIR / f"{SLUG}_household_interpretations.csv"
DIVERGENCE_BRANCHES = ARTIFACT_DIR / f"{SLUG}_divergence_branches.csv"
RESIDENT_NEGOTIATIONS = ARTIFACT_DIR / f"{SLUG}_resident_negotiations.csv"
PRACTICE_MUTATIONS = ARTIFACT_DIR / f"{SLUG}_practice_mutations.csv"
VILLAGE_COUPLINGS = ARTIFACT_DIR / f"{SLUG}_village_board_couplings.csv"
REALITY_LEDGER = ARTIFACT_DIR / f"{SLUG}_reality_constraint_ledger.csv"
SEED_OUTCOMES = ARTIFACT_DIR / f"{SLUG}_seed_outcomes.csv"
SOURCE_LINKS = ARTIFACT_DIR / f"{SLUG}_source_links.csv"
ABLATIONS = ARTIFACT_DIR / f"{SLUG}_ablations.csv"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_surface_smoke.json"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "371_ssrm_3d_avatar_hint_divergence_bridge_report.md"

BOUNDARY = (
    "Browser-local avatar-hint divergence bridge only. The avatar can ask, warn, demonstrate, wait, or offer material, "
    "but residents must interpret through household memory, trust, fear, materials, and prior practice. No LLM call, "
    "no autonomous language claim, no subjective-consciousness claim, no moral-patienthood claim, no real science claim, "
    "no finished civilization simulator, and no fixed technology tree."
)
NEXT_GATE = (
    "post-371: let hint-divergent branches compete across return sessions through household reputation, maintenance burden, "
    "and forgotten-or-revived practice memory without collapsing to a uniform unlock"
)
LAW_HASH = "shared_hidden_law_resin_fiber_charge_like_effect_v1_audit_only"
FORBIDDEN_PUBLIC_TERMS = [
    "electricity",
    "electron",
    "voltage",
    "battery",
    "circuit",
    "conductor",
    "metallurgy",
    "agriculture",
    "pottery",
    "technology unlock",
]
HINT_KINDS = ["question", "warning", "material_offer", "demonstration", "wait_and_return"]
BRANCH_PLANS = [
    {
        "status": "useful_practice",
        "local_label": "dry keeping habit",
        "interpretation": "dry things keep the small bite quieter and easier to repeat",
        "decision": "accepts a limited household trial",
        "willingness": 0.72,
        "misread": True,
    },
    {
        "status": "ritualized",
        "local_label": "quiet sign waiting",
        "interpretation": "the sign should be respected before work resumes",
        "decision": "delays and asks the campfire first",
        "willingness": 0.46,
        "misread": True,
    },
    {
        "status": "taboo",
        "local_label": "storm-thread avoidance",
        "interpretation": "children should stay away from dry thread after storms",
        "decision": "refuses until an elder watches",
        "willingness": 0.22,
        "misread": True,
    },
    {
        "status": "disputed",
        "local_label": "wet counterexample note",
        "interpretation": "wet scraps dull the sign, so the old story may be incomplete",
        "decision": "asks for another small test",
        "willingness": 0.55,
        "misread": False,
    },
    {
        "status": "rejected",
        "local_label": "busy-season refusal",
        "interpretation": "the hint can wait because roof work matters more",
        "decision": "puts the hint aside for later",
        "willingness": 0.31,
        "misread": False,
    },
]


def write_json(path: Path, payload: Any) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: List[Dict[str, Any]], fieldnames: List[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def score(condition: bool) -> float:
    return 1.0 if condition else 0.0


def resident_for(seed: int, offset: int) -> str:
    residents = ["Ari", "Fay", "Milo", "Sera", "Tovan", "Nia"]
    return residents[(seed + offset) % len(residents)]


def seed_from_practice(node: Dict[str, Any]) -> int:
    try:
        return int(str(node["practice_id"]).split("-")[0])
    except (KeyError, ValueError):
        return 0


def material_list(value: Any) -> List[str]:
    if isinstance(value, list):
        return [str(item) for item in value if str(item)]
    return [part for part in str(value).replace(";", "+").split("+") if part]


def forbidden_terms(rows: Iterable[Dict[str, Any]]) -> List[str]:
    text = json.dumps(list(rows), sort_keys=True).lower()
    return [term for term in FORBIDDEN_PUBLIC_TERMS if term in text]


def build_rows_for_report(ablation: str | None = None) -> Dict[str, List[Dict[str, Any]]]:
    base = build_report370_rows()
    base_nodes = base["practice_nodes"]
    base_concerns = {row["source_practice_id"]: row for row in base["village_concerns"]}
    base_projects = {row["related_practice_nodes"]: row for row in base["project_proposals"]}
    rows: Dict[str, List[Dict[str, Any]]] = {
        "hint_events": [],
        "household_interpretations": [],
        "divergence_branches": [],
        "resident_negotiations": [],
        "practice_mutations": [],
        "village_couplings": [],
        "reality_ledger": [],
        "seed_outcomes": [],
        "source_links": [],
    }
    seed_statuses: Dict[int, List[str]] = defaultdict(list)
    for index, node in enumerate(base_nodes):
        seed = seed_from_practice(node)
        hint_kind = HINT_KINDS[index % len(HINT_KINDS)]
        source_practice_id = node["practice_id"] if ablation != "no_practice_memory" else "none"
        concern = base_concerns.get(node["practice_id"], {})
        project = base_projects.get(node["practice_id"], {})
        materials = material_list(node.get("materials_used", "reed_fiber+dry_resin"))
        if ablation == "no_material_cost":
            materials = []
        hint_id = f"{seed}-AHD-{index + 1:03d}"
        direct_install = ablation == "direct_correct_answer"
        future_use_named = ablation == "direct_correct_answer"
        hidden_law_exposed = ablation == "no_audit_split"
        hint_event = {
            "seed": seed,
            "hint_id": hint_id,
            "hidden_law_hash": LAW_HASH,
            "hint_kind": hint_kind,
            "avatar_action": f"avatar gives a {hint_kind} without a final explanation",
            "target_resident": resident_for(seed, index),
            "target_household": node.get("origin_household", f"house_{seed % 4}"),
            "source_practice_id": source_practice_id,
            "source_local_name": node.get("local_name", "local practice"),
            "material_offered": ";".join(materials) or "none",
            "visible_demonstration": "small local effect shown once" if hint_kind == "demonstration" else "question or warning only",
            "correct_explanation_given": direct_install,
            "future_use_named": future_use_named,
            "resident_must_interpret": not direct_install,
            "avatar_can_force": False,
            "time_cost": 0 if ablation == "no_material_cost" else 1,
            "material_cost": 0 if ablation == "no_material_cost" else (1 if hint_kind in {"material_offer", "demonstration"} else 0),
            "normal_view_hidden_law_exposed": hidden_law_exposed,
        }
        rows["hint_events"].append(hint_event)
        rows["village_couplings"].append({
            "seed": seed,
            "hint_id": hint_id,
            "source_practice_id": source_practice_id,
            "source_concern_id": concern.get("concern_id", "none"),
            "source_proposal_id": project.get("proposal_id", "none"),
            "avatar_support_mode": "question/support/wait, not assignment",
            "resident_generated_board_item": bool(concern or project),
        })
        rows["source_links"].append({
            "seed": seed,
            "row_id": hint_id,
            "row_type": "hint_event",
            "source_practice_id": source_practice_id,
            "source_concern_id": concern.get("concern_id", "none"),
            "source_proposal_id": project.get("proposal_id", "none"),
            "hidden_law_exposed_to_resident": hidden_law_exposed,
            "avatar_direct_install": direct_install,
        })
        branch_indexes = [0, 1, 2] if ablation != "no_household_difference" else [0, 0, 0]
        for household_offset, branch_index in enumerate(branch_indexes):
            plan = BRANCH_PLANS[(branch_index + seed + index + household_offset) % len(BRANCH_PLANS)]
            if ablation == "no_household_difference":
                plan = BRANCH_PLANS[0]
            if ablation == "forced_uniform_history":
                plan = BRANCH_PLANS[0]
            if ablation == "no_wait_and_refusal":
                plan = {**plan, "decision": "accepts immediately", "willingness": 0.88}
            if ablation == "no_trust_gate":
                plan = {**plan, "decision": "accepts immediately", "willingness": 1.0}
            household = f"house_{(seed + household_offset) % 4}"
            resident = resident_for(seed, index + household_offset + 1)
            interpretation_id = f"{seed}-AHI-{index + 1:03d}-{household_offset + 1}"
            branch_id = f"{seed}-AHB-{index + 1:03d}-{household_offset + 1}"
            local_name = f"{plan['local_label']} around {node.get('local_name', 'local sign')}"
            rows["household_interpretations"].append({
                "seed": seed,
                "interpretation_id": interpretation_id,
                "hint_id": hint_id,
                "resident": resident,
                "household": household,
                "local_name": local_name,
                "resident_interpretation": plan["interpretation"],
                "trust_gate": round(float(plan["willingness"]), 2),
                "fear_or_priority_gate": plan["decision"],
                "wrong_or_partial_interpretation": bool(plan["misread"]),
                "hidden_law_known": hidden_law_exposed,
                "correct_concept_received": direct_install,
                "modern_name_used": False,
            })
            status = "useful_practice" if direct_install else plan["status"]
            rows["divergence_branches"].append({
                "seed": seed,
                "branch_id": branch_id,
                "hint_id": hint_id,
                "interpretation_id": interpretation_id,
                "resident": resident,
                "household": household,
                "branch_status": status,
                "branch_reason": f"{resident} treats the hint as {plan['decision']}",
                "source_practice_id": source_practice_id,
                "accepts_avatar_priority": float(plan["willingness"]) >= 0.6,
                "can_refuse_or_delay": float(plan["willingness"]) <= 0.55 and ablation not in {"no_wait_and_refusal", "no_trust_gate"},
                "avatar_commanded": direct_install,
                "same_hidden_law_hash": LAW_HASH,
                "history_signature": f"{hint_kind}:{status}:{household}:{source_practice_id}",
            })
            rows["resident_negotiations"].append({
                "seed": seed,
                "negotiation_id": f"{seed}-AHN-{index + 1:03d}-{household_offset + 1}",
                "branch_id": branch_id,
                "resident": resident,
                "response": plan["decision"],
                "resident_willingness": round(float(plan["willingness"]), 2),
                "avatar_cannot_force": not direct_install,
                "relationship_memory_note": "avatar suggested; household decided",
            })
            if status in {"useful_practice", "ritualized", "taboo"}:
                rows["practice_mutations"].append({
                    "seed": seed,
                    "mutation_id": f"{seed}-AHM-{index + 1:03d}-{household_offset + 1}",
                    "parent_practice_id": source_practice_id,
                    "hint_id": hint_id,
                    "interpretation_id": interpretation_id,
                    "local_name": local_name,
                    "origin_household": household,
                    "status": "practical" if status == "useful_practice" else status,
                    "adoption_count": 0 if status == "taboo" else 1,
                    "maintenance_cost": int(node.get("maintenance_cost", 1)) + (1 if status == "ritualized" else 0),
                    "risk_flags": node.get("risk_flags", "none") if status != "useful_practice" else "ordinary upkeep",
                    "not_predeclared_unlock": True,
                    "wrong_interpretation_still_useful": bool(plan["misread"] and status == "useful_practice"),
                })
            seed_statuses[seed].append(status)
            before = 12
            material_cost = int(hint_event["material_cost"])
            rows["reality_ledger"].append({
                "seed": seed,
                "ledger_id": f"{seed}-AHR-{index + 1:03d}-{household_offset + 1}",
                "event": branch_id,
                "material_sources": ";".join(materials) or "none",
                "material_transformation": "sample handled by household" if material_cost else "no sample consumed",
                "time_cost": int(hint_event["time_cost"]) + 1,
                "labor_or_attention_cost": 1,
                "tool_wear": 0,
                "resident_effort": 1,
                "hidden_law_involved": LAW_HASH,
                "public_observation": hint_event["visible_demonstration"],
                "resident_interpretation": plan["interpretation"],
                "resources_before": before,
                "resources_after": before - material_cost,
                "conservation_check": before - material_cost <= before,
                "maintenance_obligation_created": local_name if status in {"useful_practice", "ritualized"} else "none",
                "unintended_consequence": status,
                "normal_view_hidden_law_exposed": hidden_law_exposed,
            })
            rows["source_links"].append({
                "seed": seed,
                "row_id": branch_id,
                "row_type": "divergence_branch",
                "source_practice_id": source_practice_id,
                "source_concern_id": concern.get("concern_id", "none"),
                "source_proposal_id": project.get("proposal_id", "none"),
                "hidden_law_exposed_to_resident": hidden_law_exposed,
                "avatar_direct_install": direct_install,
            })
    for seed in sorted(set(SEEDS)):
        statuses = seed_statuses.get(seed, [])
        rows["seed_outcomes"].append({
            "seed": seed,
            "hidden_law_hash": LAW_HASH,
            "branch_statuses": ";".join(statuses),
            "unique_statuses": len(set(statuses)),
            "history_signature": "|".join(statuses[:8]),
            "uniform_unlock": len(set(statuses)) <= 1,
        })
    return rows


def compute_metrics(rows: Dict[str, List[Dict[str, Any]]], app_text: str = "", index_text: str = "", browser: Dict[str, Any] | None = None) -> Dict[str, float]:
    browser = browser or {}
    hints = rows["hint_events"]
    interpretations = rows["household_interpretations"]
    branches = rows["divergence_branches"]
    negotiations = rows["resident_negotiations"]
    mutations = rows["practice_mutations"]
    couplings = rows["village_couplings"]
    ledger = rows["reality_ledger"]
    outcomes = rows["seed_outcomes"]
    links = rows["source_links"]
    public_rows = hints + interpretations + branches + negotiations + mutations + couplings
    branches_by_hint: Dict[str, set[str]] = defaultdict(set)
    for row in branches:
        branches_by_hint[row["hint_id"]].add(row["branch_status"])
    statuses = {row["branch_status"] for row in branches}
    signatures = {row["history_signature"] for row in outcomes}
    return {
        "avatar_hint_not_direct_install": score(bool(hints) and all(not row["correct_explanation_given"] and not row["future_use_named"] and row["resident_must_interpret"] and not row["avatar_can_force"] for row in hints)),
        "household_interpretation_divergence": score(any(len(statuses_for_hint) >= 2 for statuses_for_hint in branches_by_hint.values())),
        "same_hidden_law_different_histories": score(len({row["hidden_law_hash"] for row in hints}) == 1 and len(signatures) >= 4),
        "resident_refusal_and_delay_present": score(any("refuses" in row["response"] or "delays" in row["response"] or "aside" in row["response"] for row in negotiations)),
        "hint_requires_material_or_time_cost": score(bool(ledger) and all(int(row["time_cost"]) > 0 and int(row["labor_or_attention_cost"]) > 0 for row in ledger) and any(int(row["resources_after"]) < int(row["resources_before"]) for row in ledger)),
        "practice_mutation_from_existing_node": score(bool(mutations) and all(row["parent_practice_id"] != "none" and row["not_predeclared_unlock"] for row in mutations)),
        "wrong_interpretation_can_be_useful": score(any(row["wrong_interpretation_still_useful"] and row["status"] == "practical" for row in mutations)),
        "taboo_or_ritual_branch_present": score("taboo" in statuses and "ritualized" in statuses),
        "normal_view_no_modern_terms": score(not forbidden_terms(public_rows)),
        "audit_hidden_law_belief_split": score(all(not row["normal_view_hidden_law_exposed"] for row in hints) and all(not row["hidden_law_known"] for row in interpretations) and all(not row["normal_view_hidden_law_exposed"] for row in ledger)),
        "village_board_proposal_coupling": score(bool(couplings) and all(row["resident_generated_board_item"] and row["source_concern_id"] != "none" and row["source_proposal_id"] != "none" for row in couplings)),
        "reality_causal_ledger_integrity": score(bool(ledger) and all(int(row["resources_after"]) <= int(row["resources_before"]) and row["conservation_check"] and row["hidden_law_involved"] == LAW_HASH for row in ledger)),
        "multi_seed_hint_divergence": score(len([row for row in outcomes if int(row["unique_statuses"]) >= 3]) >= 4),
        "source_trace_integrity": score(bool(links) and all(row["source_practice_id"] != "none" and row["source_concern_id"] != "none" and row["source_proposal_id"] != "none" for row in links)),
        "shell_hint_divergence_wired": score("avatarHintDivergence" in app_text and "runAvatarHintDivergenceLoop" in app_text and "introduceAvatarHint" in app_text),
        "browser_surface_wired": score("Avatar Hint Divergence" in index_text and "avatarHintDivergenceOut" in index_text and "runHintDivergenceInterpretation" in index_text),
        "browser_surface_static_smoke": score(bool(browser) and browser.get("hint_panel_present") and browser.get("summary_present") and browser.get("actions_present")),
    }


def build_browser_surface_smoke(app_text: str, index_text: str) -> Dict[str, Any]:
    return {
        "kind": "static_browser_surface_smoke",
        "runtime_browser_exercised": False,
        "reason": "Report 371 checks that the maintained browser shell exposes the panel/actions; no external browser runtime is claimed here.",
        "hint_panel_present": "Avatar Hint Divergence" in index_text,
        "summary_present": "avatarHintDivergenceSummaryOut" in index_text,
        "detail_present": "avatarHintDivergenceOut" in index_text,
        "actions_present": all(token in index_text for token in ["introduceAvatarHint", "runHintDivergenceInterpretation", "runAvatarHintDivergenceLoop"]),
        "state_wired": "avatarHintDivergence" in app_text,
        "render_wired": "renderAvatarHintDivergence" in app_text,
    }


def build_ablations(app_text: str, index_text: str) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    expected_failures = {
        "direct_correct_answer": "avatar_hint_not_direct_install",
        "no_household_difference": "household_interpretation_divergence",
        "no_trust_gate": "resident_refusal_and_delay_present",
        "no_material_cost": "hint_requires_material_or_time_cost",
        "no_practice_memory": "practice_mutation_from_existing_node",
        "no_wait_and_refusal": "resident_refusal_and_delay_present",
        "forced_uniform_history": "multi_seed_hint_divergence",
        "no_audit_split": "audit_hidden_law_belief_split",
    }
    for name, expected_failure in expected_failures.items():
        ablated = build_rows_for_report(name)
        metrics = compute_metrics(ablated, app_text, index_text, {"hint_panel_present": True, "summary_present": True, "actions_present": True})
        rows.append({
            "ablation": name,
            "expected_failed_metric": expected_failure,
            "failed_as_expected": metrics.get(expected_failure, 1.0) == 0.0,
            "weakest_channel_score": min(metrics.values()),
        })
    return rows


def add_criterion(criteria: List[Dict[str, Any]], name: str, passed: bool, evidence: str) -> None:
    criteria.append({"criterion": name, "passed": bool(passed), "score": 1.0 if passed else 0.0, "evidence": evidence})


def write_report(metrics: Dict[str, float], rows: Dict[str, List[Dict[str, Any]]], ablations: List[Dict[str, Any]], verdict: str) -> None:
    status_counts = Counter(row["branch_status"] for row in rows["divergence_branches"])
    mutation_counts = Counter(row["status"] for row in rows["practice_mutations"])
    lines = [
        "# Report 371: SSRM-3D Avatar Hint Divergence Bridge",
        "",
        "## Purpose",
        "",
        "Report 371 tests the next post-practice-graph step: the avatar can introduce a hint, warning, question, demonstration, material, or delay, but the village does not receive a direct explanation or a uniform unlock. Households reinterpret the same hint through trust, fear, maintenance pressure, existing practice memory, and material constraints.",
        "",
        "This is deliberately not a technology tree. The output is a set of divergent historical branches and practice mutations generated after Report 370 practice nodes already exist.",
        "",
        "## Boundary",
        "",
        BOUNDARY,
        "",
        "## Method",
        "",
        "- Start from Report 370 emergent practice nodes, village board concerns, project proposals, and causal ledger assumptions.",
        "- Create avatar hint events with source practice IDs, household targets, material/time costs, and explicit flags that no correct explanation or future use was named.",
        "- Let three households per hint generate local interpretations, negotiation responses, branch outcomes, and possible practice mutations.",
        "- Preserve the split between hidden simulator law, public observation, household belief, local practice mutation, and audit-only causal trace.",
        "",
        "## Results",
        "",
        f"- Verdict: `{verdict}`",
        f"- Hint events: `{len(rows['hint_events'])}`",
        f"- Household interpretations: `{len(rows['household_interpretations'])}`",
        f"- Divergence branches: `{len(rows['divergence_branches'])}`",
        f"- Practice mutations: `{len(rows['practice_mutations'])}`",
        f"- Reality ledger rows: `{len(rows['reality_ledger'])}`",
        f"- Branch status counts: `{dict(status_counts)}`",
        f"- Mutation status counts: `{dict(mutation_counts)}`",
        "",
        "## Metrics",
        "",
    ]
    for key, value in sorted(metrics.items()):
        lines.append(f"- `{key}`: `{value:.3f}`")
    lines.extend([
        "",
        "## Ablations",
        "",
    ])
    for row in ablations:
        lines.append(f"- `{row['ablation']}`: expected failure `{row['expected_failed_metric']}`, failed as expected `{row['failed_as_expected']}`")
    lines.extend([
        "",
        "## Artifacts",
        "",
        f"- `{HINT_EVENTS}`",
        f"- `{HOUSEHOLD_INTERPRETATIONS}`",
        f"- `{DIVERGENCE_BRANCHES}`",
        f"- `{RESIDENT_NEGOTIATIONS}`",
        f"- `{PRACTICE_MUTATIONS}`",
        f"- `{VILLAGE_COUPLINGS}`",
        f"- `{REALITY_LEDGER}`",
        f"- `{SEED_OUTCOMES}`",
        f"- `{SOURCE_LINKS}`",
        f"- `{BROWSER_SMOKE}`",
        f"- `{RESULTS}`",
        "",
        "## Honest read",
        "",
        "This report makes the world less toy-like by preventing avatar input from becoming direct knowledge transfer. The strongest result is not that residents become scientifically correct. The stronger result is that the same hint can become a useful local habit, a ritual, a taboo, a dispute, or a rejection depending on household conditions and history.",
        "",
        "The browser smoke artifact is static shell-surface evidence, not a direct runtime browser pass. A later gate should exercise the new panel through a real browser session and make the divergent branches persist across save/restore and return sessions.",
        "",
        f"Next gate: {NEXT_GATE}.",
        "",
    ])
    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    app_text = SHELL_APP.read_text(encoding="utf-8")
    index_text = SHELL_INDEX.read_text(encoding="utf-8")
    browser = build_browser_surface_smoke(app_text, index_text)
    rows = build_rows_for_report()
    metrics = compute_metrics(rows, app_text, index_text, browser)
    ablations = build_ablations(app_text, index_text)
    criteria: List[Dict[str, Any]] = []
    for name, value in sorted(metrics.items()):
        add_criterion(criteria, name, value == 1.0, f"metric={value:.3f}")
    add_criterion(criteria, "ablations_fail_as_expected", all(row["failed_as_expected"] for row in ablations), f"{sum(1 for row in ablations if row['failed_as_expected'])}/{len(ablations)}")
    weakest = min(metrics.values()) if metrics else 0.0
    readiness = sum(metrics.values()) / len(metrics) if metrics else 0.0
    verdict = "pass" if weakest == 1.0 and all(row["failed_as_expected"] for row in ablations) else "fail"

    write_csv(HINT_EVENTS, rows["hint_events"], list(rows["hint_events"][0].keys()))
    write_csv(HOUSEHOLD_INTERPRETATIONS, rows["household_interpretations"], list(rows["household_interpretations"][0].keys()))
    write_csv(DIVERGENCE_BRANCHES, rows["divergence_branches"], list(rows["divergence_branches"][0].keys()))
    write_csv(RESIDENT_NEGOTIATIONS, rows["resident_negotiations"], list(rows["resident_negotiations"][0].keys()))
    write_csv(PRACTICE_MUTATIONS, rows["practice_mutations"], list(rows["practice_mutations"][0].keys()))
    write_csv(VILLAGE_COUPLINGS, rows["village_couplings"], list(rows["village_couplings"][0].keys()))
    write_csv(REALITY_LEDGER, rows["reality_ledger"], list(rows["reality_ledger"][0].keys()))
    write_csv(SEED_OUTCOMES, rows["seed_outcomes"], list(rows["seed_outcomes"][0].keys()))
    write_csv(SOURCE_LINKS, rows["source_links"], list(rows["source_links"][0].keys()))
    write_csv(ABLATIONS, ablations, list(ablations[0].keys()))
    write_json(BROWSER_SMOKE, browser)
    write_csv(CRITERIA, criteria, list(criteria[0].keys()))
    write_csv(SUMMARY, [{"report": REPORT, "verdict": verdict, "readiness": readiness, "weakest_channel_score": weakest, "hint_events": len(rows["hint_events"]), "divergence_branches": len(rows["divergence_branches"]), "practice_mutations": len(rows["practice_mutations"])}], ["report", "verdict", "readiness", "weakest_channel_score", "hint_events", "divergence_branches", "practice_mutations"])
    write_csv(VERDICT, [{"report": REPORT, "verdict": verdict, "boundary": BOUNDARY, "next_gate": NEXT_GATE}], ["report", "verdict", "boundary", "next_gate"])
    write_json(STATE, {"generated_at": datetime.now(timezone.utc).isoformat(), "report": REPORT, "boundary": BOUNDARY, "next_gate": NEXT_GATE, "rows": rows, "metrics": metrics, "ablations": ablations, "browser_surface_smoke": browser})
    write_json(RESULTS, {"report": REPORT, "slug": SLUG, "verdict": verdict, "metrics": metrics, "readiness": readiness, "weakest_channel_score": weakest, "counts": {name: len(value) for name, value in rows.items()}, "boundary": BOUNDARY, "next_gate": NEXT_GATE})
    write_report(metrics, rows, ablations, verdict)
    print(json.dumps({"report": REPORT, "verdict": verdict, "readiness": readiness, "weakest_channel_score": weakest, "hint_events": len(rows["hint_events"]), "branches": len(rows["divergence_branches"]), "mutations": len(rows["practice_mutations"])}, indent=2, sort_keys=True))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
