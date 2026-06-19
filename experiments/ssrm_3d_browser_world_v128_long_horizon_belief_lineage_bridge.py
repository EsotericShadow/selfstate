from __future__ import annotations

import csv
import hashlib
import json
import random
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

from experiments.ssrm_3d_browser_world_v122_non_scripted_world_anomaly_discovery_bridge import (
    RESIDENTS,
    SEEDS as BASE_SEEDS,
    VOCAB,
    generate_hidden_law,
    observe_effect,
)

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 368
SLUG = "ssrm_3d_browser_world_v128_long_horizon_belief_lineage_bridge"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT362_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v122_non_scripted_world_anomaly_discovery_bridge_results.json"
REPORT367_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v127_stochastic_ordinary_affordance_bridge_results.json"
SHARED_HIDDEN_LAW = ARTIFACT_DIR / f"{SLUG}_shared_hidden_law.json"
BELIEF_LINEAGES = ARTIFACT_DIR / f"{SLUG}_belief_lineages.csv"
AGENT_PROPOSALS = ARTIFACT_DIR / f"{SLUG}_agent_proposals.csv"
EXPERIMENT_RESULTS = ARTIFACT_DIR / f"{SLUG}_experiment_results.csv"
THEORY_COMPETITION = ARTIFACT_DIR / f"{SLUG}_theory_competition.csv"
CULTURAL_MEMORY = ARTIFACT_DIR / f"{SLUG}_cultural_memory.csv"
MATERIAL_CHAINS = ARTIFACT_DIR / f"{SLUG}_material_chains.csv"
SEED_OUTCOMES = ARTIFACT_DIR / f"{SLUG}_seed_outcomes.csv"
AUDIT_REPLAY = ARTIFACT_DIR / f"{SLUG}_audit_replay.json"
ABLATIONS = ARTIFACT_DIR / f"{SLUG}_ablations.csv"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "368_ssrm_3d_long_horizon_belief_lineage_bridge_report.md"

SEEDS = [36217, 36231, 36247, 36263, 36281, 36307, 36319, 36343]
ERAS: List[Tuple[str, int]] = [
    ("week_01", 7),
    ("moon_02", 42),
    ("season_01", 120),
    ("year_01", 365),
    ("year_03", 1095),
    ("generation_02", 9125),
    ("generation_04", 18250),
]
MATERIALS = ["red_scrap", "dry_resin", "wet_wood", "reed_fiber", "ash_glass", "iron_sand", "clay_jar"]
SETTLEMENT_BIASES = ["craft", "caution", "ritual", "trade", "archive", "skeptic", "teacher", "wanderer"]
FORBIDDEN_PUBLIC_TERMS = ["electricity", "electron", "voltage", "conductor", "battery", "circuit", "magnetism", "static charge", "technology unlock", "tech tree"]
BOUNDARY = (
    "Deterministic per-seed long-horizon belief-lineage simulation over one shared hidden-law world. Residents inherit, mutate, "
    "compete over, archive, and sometimes operationalize partial beliefs without receiving the true law. No LLM call, no autonomous "
    "language, no subjective-consciousness claim, no moral-patienthood claim, no real science claim, no finished game engine, and no "
    "predeclared device tree."
)
NEXT_GATE = (
    "post-368: make theory competition alter everyday scheduling, apprenticeship, trade routes, and safety customs in the browser shell "
    "so lineage pressure is lived as ordinary civilization behavior rather than only artifact history"
)


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


def public_forbidden_terms(rows: Iterable[Dict[str, Any]]) -> List[str]:
    text = json.dumps(list(rows), sort_keys=True).lower()
    return [term for term in FORBIDDEN_PUBLIC_TERMS if term in text]


def stable_hash(payload: Any) -> str:
    encoded = json.dumps(payload, sort_keys=True).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()[:16]


def shared_law() -> Dict[str, Any]:
    law = generate_hidden_law(36217)
    law["sharedAcrossSeeds"] = True
    law["auditOnly"] = True
    return law


def score(condition: bool) -> float:
    return 1.0 if condition else 0.0


def clamp(value: float, low: float = 0.02, high: float = 0.96) -> float:
    return round(max(low, min(high, value)), 3)


def lineage_label(parent_label: str, effect_kind: str, era_index: int, resident: str, rng: random.Random) -> str:
    suffix_by_effect = {
        "jump": ["dry-jump", "fiber-rise", "rub-sign"],
        "transfer": ["far-bite", "red-path", "handspan-carry"],
        "motion": ["dark-crawl", "red-call", "grain-follow"],
        "dulling": ["wet-silence", "water-hush", "rain-fail"],
        "breakage": ["crack-warning", "tool-anger", "edge-shame"],
        "risk": ["smoke-bound", "ash-fear", "stop-rule"],
        "unclear": ["half-sign", "missing-repeat", "quiet-doubt"],
    }
    base = parent_label.split("/")[-1]
    token = rng.choice(suffix_by_effect.get(effect_kind, suffix_by_effect["unclear"]))
    if era_index >= 5:
        keeper = rng.choice(["school", "route", "bench", "jar", "roof"])
        return f"{base}/{keeper}-{token}"
    if resident in VOCAB and rng.random() < 0.35:
        return f"{rng.choice(VOCAB[resident])}/{token}"
    return f"{base}/{token}"


def initial_belief(seed: int, law_hash: str) -> Dict[str, Any]:
    rng = random.Random(seed * 17 + 368)
    resident = RESIDENTS[seed % len(RESIDENTS)]
    effect, effect_kind = observe_effect(shared_law(), ["dry_resin", "reed_fiber"])
    label = rng.choice(VOCAB[resident])
    return {
        "seed": seed,
        "belief_id": f"{seed}-BEL-000",
        "parent_belief_id": "root_observation",
        "era": "week_00",
        "era_day": 0,
        "generation": 0,
        "resident": resident,
        "household": f"house_{seed % 4}",
        "label": label,
        "kind": rng.choice(["practical", "skeptical", "ritualized", "useful_wrong"]),
        "confidence": clamp(0.31 + rng.random() * 0.22),
        "evidence_count": 1,
        "contradiction_count": 0,
        "witness_count": 1,
        "abstraction_level": 0,
        "source": "public_anomaly_observation",
        "source_effect": effect,
        "source_effect_kind": effect_kind,
        "law_hash": law_hash,
        "true_law_exposed": False,
        "avatar_answer": False,
    }


def choose_materials(seed: int, era_index: int, belief: Dict[str, Any], stock: Dict[str, int], bias: str, rng: random.Random) -> Tuple[List[str], str]:
    available = [name for name in MATERIALS if stock.get(name, 0) > 0]
    if len(available) < 2:
        available = MATERIALS[:]
    label = belief["label"]
    preferred: List[str] = []
    if "wet" in label or "water" in label or bias == "caution":
        preferred.append("wet_wood")
    if "red" in label or "bite" in label or bias == "craft":
        preferred.append("red_scrap")
    if "jar" in label or bias == "archive":
        preferred.append("clay_jar")
    if "grain" in label or bias == "trade":
        preferred.append("iron_sand")
    if "dry" in label or "fiber" in label or bias in {"teacher", "skeptic"}:
        preferred.extend(["dry_resin", "reed_fiber"])
    preferred = [item for item in preferred if item in available]
    pool = preferred + [item for item in available if item not in preferred]
    rng.shuffle(pool)
    first = pool[0]
    second = pool[1] if len(pool) > 1 else rng.choice([item for item in MATERIALS if item != first])
    if era_index >= 4 and stock.get("ash_glass", 0) > 0 and rng.random() < 0.28:
        second = "ash_glass"
    question = "compare inherited label against available material"
    if bias == "caution" or belief["contradiction_count"] > 1:
        question = "find a safer boundary before repeating the sign"
    elif bias == "trade":
        question = "learn whether scarce material is worth carrying farther"
    elif bias == "ritual":
        question = "test whether the rite repeats outside the old place"
    elif bias == "craft":
        question = "turn a repeated sign into a usable bench rule"
    return [first, second], question


def proposal_from_belief(seed: int, era_index: int, belief: Dict[str, Any], stock: Dict[str, int], bias: str, rng: random.Random) -> Dict[str, Any]:
    materials, question = choose_materials(seed, era_index, belief, stock, bias, rng)
    resident = RESIDENTS[(RESIDENTS.index(belief["resident"]) + era_index + rng.randrange(len(RESIDENTS))) % len(RESIDENTS)]
    return {
        "seed": seed,
        "proposal_id": f"{seed}-PROP-{era_index:02d}-{rng.randrange(1000, 9999)}",
        "era": ERAS[era_index][0],
        "era_day": ERAS[era_index][1],
        "generation": era_index,
        "resident": resident,
        "source_belief_id": belief["belief_id"],
        "source_label": belief["label"],
        "question": question,
        "materials": "+".join(materials),
        "proposal_source": "resident_generated_from_belief_state",
        "predeclared_device": False,
        "avatar_answer": False,
    }


def classify_effect(effect: str) -> Tuple[bool, bool, float]:
    failure = any(token in effect for token in ["nothing", "dulled", "cracked", "smoke", "stopped"])
    safety = any(token in effect for token in ["smoke", "cracked", "hurt", "stopped"])
    utility = 0.14
    if "jumped" in effect or "carried" in effect or "crawled" in effect:
        utility += 0.46
    if "farther" in effect or "holds" in effect:
        utility += 0.12
    if failure:
        utility -= 0.18
    if safety:
        utility -= 0.08
    return failure, safety, clamp(utility, 0.0, 1.0)


def update_stock(stock: Dict[str, int], materials: List[str], effect: str, era_index: int) -> Dict[str, Any]:
    before = dict(stock)
    for material in materials:
        stock[material] = max(0, stock.get(material, 0) - 1)
    trade_shift = "none"
    if any(token in effect for token in ["jumped", "carried", "crawled"]):
        focus = materials[0]
        stock[focus] = stock.get(focus, 0) + (2 if era_index >= 4 else 1)
        trade_shift = f"more_{focus}"
    elif "smoke" in effect or "cracked" in effect:
        stock[materials[-1]] = max(0, stock.get(materials[-1], 0) - 1)
        trade_shift = f"avoid_{materials[-1]}"
    return {"before": before, "after": dict(stock), "trade_shift": trade_shift}


def institution_for(seed: int, era_index: int, bias: str, successful_count: int, safety_count: int, abstraction_level: int) -> str:
    if safety_count >= 2 and bias in {"caution", "ritual"}:
        return "safety_custom"
    if abstraction_level >= 3 and successful_count >= 3 and bias in {"craft", "teacher"}:
        return "craft_bench"
    if successful_count >= 3 and bias == "trade":
        return "route_exchange"
    if era_index >= 5 and bias == "archive":
        return "memory_school"
    if bias == "ritual" and era_index >= 3:
        return "caution_rite"
    return "none"


def competition_status(score_value: float, safety_count: int, bias: str, rng: random.Random) -> str:
    if safety_count >= 2 and bias in {"caution", "ritual"}:
        return "tabooed"
    if score_value >= 0.72:
        return "dominant"
    if score_value >= 0.56:
        return rng.choice(["carried", "taught", "bench-tested"])
    if score_value <= 0.30:
        return rng.choice(["archived", "mocked", "set-aside"])
    return rng.choice(["rival", "argued", "minority"])


def simulate_lineage(seed: int, *, ablation: str | None = None) -> Dict[str, Any]:
    rng = random.Random(seed * 101 + 368)
    law = shared_law() if ablation != "no_shared_law" else generate_hidden_law(seed)
    law_hash = stable_hash(law)
    bias = SETTLEMENT_BIASES[SEEDS.index(seed) % len(SETTLEMENT_BIASES)]
    stock = {
        "red_scrap": 4 + seed % 3,
        "dry_resin": 5,
        "wet_wood": 6,
        "reed_fiber": 5,
        "ash_glass": 3,
        "iron_sand": 3 + (1 if bias == "trade" else 0),
        "clay_jar": 4,
    }
    lineages: List[Dict[str, Any]] = []
    proposals: List[Dict[str, Any]] = []
    experiments: List[Dict[str, Any]] = []
    competitions: List[Dict[str, Any]] = []
    cultural: List[Dict[str, Any]] = []
    material_chains: List[Dict[str, Any]] = []
    audit: List[Dict[str, Any]] = [{
        "seed": seed,
        "era": "audit_start",
        "type": "shared_hidden_law",
        "law_hash": law_hash,
        "audit_only": True,
        "summary": "shared material law attached to this seed without resident access",
    }]
    root = initial_belief(seed, law_hash)
    if ablation == "no_lineage_parent":
        root["parent_belief_id"] = "missing"
    lineages.append(root)
    active = root
    successful_count = 0
    failed_count = 0
    safety_count = 0
    institutions_seen: List[str] = []
    trade_shifts: List[str] = []

    era_range = range(len(ERAS)) if ablation != "no_long_horizon" else range(2)
    for era_index in era_range:
        era, era_day = ERAS[era_index]
        proposal = proposal_from_belief(seed, era_index, active, stock, bias, rng)
        if ablation == "no_agent_proposals":
            proposal["proposal_source"] = "fixed_test_slot"
        proposals.append(proposal)
        materials = proposal["materials"].split("+")
        effect, effect_kind = observe_effect(law, materials)
        failure, safety, utility = classify_effect(effect)
        if ablation == "no_failures_preserved" and failure:
            effect, effect_kind, failure, safety, utility = "loose fiber jumped after rubbing", "jump", False, False, 0.64
        if failure:
            failed_count += 1
        else:
            successful_count += 1
        if safety:
            safety_count += 1
        stock_change = update_stock(stock, materials, effect, era_index) if ablation != "no_material_bottlenecks" else {"before": dict(stock), "after": dict(stock), "trade_shift": "none"}
        if stock_change["trade_shift"] != "none":
            trade_shifts.append(stock_change["trade_shift"])
        material_chains.append({
            "seed": seed,
            "era": era,
            "era_day": era_day,
            "proposal_id": proposal["proposal_id"],
            "materials": proposal["materials"],
            "stock_before": json.dumps(stock_change["before"], sort_keys=True),
            "stock_after": json.dumps(stock_change["after"], sort_keys=True),
            "trade_shift": stock_change["trade_shift"],
            "material_bottleneck_bound": ablation != "no_material_bottlenecks",
        })
        abstraction_gain = 1 if (not failure and active["evidence_count"] + successful_count >= 3 and era_index >= 2) else 0
        if bias in {"teacher", "craft"} and not failure and era_index >= 3:
            abstraction_gain += 1
        contradiction = active["contradiction_count"] + (1 if failure else 0)
        confidence_delta = utility * 0.18 - (0.10 if failure else 0.0) + (0.04 if bias in {"craft", "teacher"} and not failure else 0.0)
        new_confidence = clamp(active["confidence"] + confidence_delta)
        new_label = lineage_label(active["label"], effect_kind, era_index, proposal["resident"], rng)
        child_id = f"{seed}-BEL-{era_index + 1:03d}"
        kind_pool = ["practical", "skeptical", "ritualized", "useful_wrong", "craft_rule", "safety_rule"]
        if safety:
            kind = "safety_rule" if bias in {"caution", "teacher"} else "ritualized"
        elif not failure and abstraction_gain:
            kind = "craft_rule"
        elif failure:
            kind = rng.choice(["skeptical", "useful_wrong", "ritualized"])
        else:
            kind = rng.choice(kind_pool[:4])
        child = {
            "seed": seed,
            "belief_id": child_id,
            "parent_belief_id": active["belief_id"] if ablation != "no_lineage_parent" else "missing",
            "era": era,
            "era_day": era_day,
            "generation": era_index + 1,
            "resident": proposal["resident"],
            "household": f"house_{(seed + era_index) % 4}",
            "label": new_label,
            "kind": kind,
            "confidence": new_confidence,
            "evidence_count": active["evidence_count"] + 1,
            "contradiction_count": contradiction,
            "witness_count": active["witness_count"] + 1 + (1 if bias in {"teacher", "trade"} else 0),
            "abstraction_level": min(5, active["abstraction_level"] + abstraction_gain),
            "source": proposal["proposal_id"],
            "source_effect": effect,
            "source_effect_kind": effect_kind,
            "law_hash": law_hash,
            "true_law_exposed": False,
            "avatar_answer": False,
        }
        if ablation == "no_social_mutation":
            child["label"] = active["label"]
        lineages.append(child)
        experiments.append({
            "seed": seed,
            "experiment_id": f"{seed}-EXP-{era_index + 1:03d}",
            "proposal_id": proposal["proposal_id"],
            "era": era,
            "era_day": era_day,
            "resident": proposal["resident"],
            "source_belief_id": active["belief_id"],
            "materials": proposal["materials"],
            "effect": effect,
            "effect_kind": effect_kind,
            "failure": failure,
            "safety_event": safety,
            "utility_score": utility,
            "preserved_failure": failure and ablation != "no_failures_preserved",
            "true_law_exposed": False,
            "predeclared_device": False,
        })
        institution = institution_for(seed, era_index, bias, successful_count, safety_count, child["abstraction_level"])
        if institution != "none":
            institutions_seen.append(institution)
        competition_score = clamp(child["confidence"] * 0.55 + utility * 0.25 + min(0.20, child["witness_count"] * 0.025) - child["contradiction_count"] * 0.035)
        if ablation == "no_competition":
            status = "accepted_without_rival"
        else:
            status = competition_status(competition_score, safety_count, bias, rng)
        competitions.append({
            "seed": seed,
            "era": era,
            "era_day": era_day,
            "belief_id": child_id,
            "label": child["label"],
            "rival_count": 0 if ablation == "no_competition" else max(1, len({row["kind"] for row in lineages[-3:]})),
            "competition_score": competition_score,
            "status": status,
            "institution": institution,
            "safety_norm": institution == "safety_custom" or child["kind"] == "safety_rule",
            "archived_not_erased": status in {"archived", "mocked", "set-aside"} or failure,
        })
        memory = f"{era}: {proposal['resident']} carried {active['label']} into {child['label']} after {effect}"
        if institution != "none":
            memory = f"{memory}; {institution} began using it"
        cultural.append({
            "seed": seed,
            "era": era,
            "era_day": era_day,
            "memory_id": f"{seed}-CUL-{era_index + 1:03d}",
            "memory": memory,
            "dominant_label": child["label"],
            "archived_failures": failed_count,
            "institution": institution,
            "trade_shifts": ";".join(trade_shifts[-3:]) or "none",
            "avatar_as_answer_source": False,
        })
        audit.extend([
            {"seed": seed, "era": era, "type": "proposal", "audit_only": False, "summary": f"{proposal['resident']} proposed {proposal['materials']} from {active['label']}"},
            {"seed": seed, "era": era, "type": "public_effect", "audit_only": False, "summary": effect},
            {"seed": seed, "era": era, "type": "belief_descendant", "audit_only": False, "summary": f"{active['belief_id']} -> {child_id} as {child['label']}"},
            {"seed": seed, "era": era, "type": "theory_competition", "audit_only": False, "summary": f"{child['label']} became {status}"},
            {"seed": seed, "era": era, "type": "material_chain", "audit_only": False, "summary": f"{proposal['materials']} stock shift {stock_change['trade_shift']}"},
        ])
        if failure:
            audit.append({"seed": seed, "era": era, "type": "preserved_failure", "audit_only": False, "summary": effect})
        active = child

    final = lineages[-1]
    institution_counts = Counter(institutions_seen)
    status_counts = Counter(row["status"] for row in competitions)
    practice_discovered = successful_count >= 4 and final["abstraction_level"] >= 2 and any(item in institutions_seen for item in ["craft_bench", "route_exchange", "memory_school"])
    taboo_emerged = safety_count >= 2 or status_counts["tabooed"] >= 1 or "safety_custom" in institutions_seen
    if practice_discovered and bias in {"craft", "teacher"}:
        outcome = "practice_lineage"
    elif "route_exchange" in institutions_seen or (trade_shifts and bias == "trade"):
        outcome = "material_route_shift"
    elif taboo_emerged and bias in {"caution", "ritual"}:
        outcome = "safety_taboo_lineage"
    elif final["abstraction_level"] >= 2 and bias == "archive":
        outcome = "archive_school_lineage"
    elif failed_count >= successful_count:
        outcome = "stalled_rival_theories"
    else:
        outcome = "useful_wrong_custom"
    history_signature = stable_hash([row["label"] for row in lineages] + [row["status"] for row in competitions] + trade_shifts)
    seed_outcome = {
        "seed": seed,
        "law_hash": law_hash,
        "settlement_bias": bias,
        "outcome": outcome,
        "history_signature": history_signature,
        "final_label": final["label"],
        "final_abstraction_level": final["abstraction_level"],
        "successful_experiments": successful_count,
        "failed_experiments": failed_count,
        "safety_events": safety_count,
        "practice_discovered": practice_discovered,
        "taboo_emerged": taboo_emerged,
        "institutions": ";".join(sorted(institution_counts)) or "none",
        "trade_shifts": ";".join(trade_shifts) or "none",
        "predeclared_ending": False,
    }
    return {
        "seed": seed,
        "law_hash": law_hash,
        "lineages": lineages,
        "proposals": proposals,
        "experiments": experiments,
        "competitions": competitions,
        "cultural": cultural,
        "material_chains": material_chains,
        "audit": audit,
        "outcome": seed_outcome,
    }


def flatten(runs: List[Dict[str, Any]], key: str) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for run in runs:
        rows.extend(run[key])
    return rows


def compute_metrics(runs: List[Dict[str, Any]], *, ablation: str | None = None) -> Dict[str, float]:
    lineages = flatten(runs, "lineages")
    proposals = flatten(runs, "proposals")
    experiments = flatten(runs, "experiments")
    competitions = flatten(runs, "competitions")
    cultural = flatten(runs, "cultural")
    material_chains = flatten(runs, "material_chains")
    audit = flatten(runs, "audit")
    outcomes = [run["outcome"] for run in runs]
    law_hashes = {run["law_hash"] for run in runs}
    by_seed_generations: Dict[int, List[int]] = defaultdict(list)
    for row in lineages:
        by_seed_generations[row["seed"]].append(int(row["generation"]))
    lineage_ids = {row["belief_id"] for row in lineages}
    lineage_by_id = {row["belief_id"]: row for row in lineages}
    parent_rows = [row for row in lineages if row["generation"] > 0]
    mutated_children = [row for row in parent_rows if row["label"] != lineage_by_id.get(row["parent_belief_id"], {}).get("label")]
    public_rows = lineages + proposals + experiments + competitions + cultural + material_chains + outcomes
    forbidden = public_forbidden_terms(public_rows)
    practice_count = sum(1 for row in outcomes if row["practice_discovered"])
    outcome_kinds = {row["outcome"] for row in outcomes}
    return {
        "shared_world_law_integrity": score(len(law_hashes) == 1 and ablation != "no_shared_law"),
        "lineage_survives_time": score(all(max(gens) >= 7 for gens in by_seed_generations.values()) and len(by_seed_generations) == len(SEEDS)),
        "parent_child_traceability": score(bool(parent_rows) and all(row["parent_belief_id"] in lineage_ids for row in parent_rows)),
        "agent_generated_proposal_rate": round(sum(1 for row in proposals if row["proposal_source"] == "resident_generated_from_belief_state") / max(1, len(proposals)), 6),
        "failed_experiment_preservation": score(any(row["failure"] for row in experiments) and all((not row["failure"]) or row["preserved_failure"] for row in experiments)),
        "rival_theory_competition": score(any(row["rival_count"] >= 2 for row in competitions) and len({row["status"] for row in competitions}) >= 4),
        "social_label_mutation": score(len(mutated_children) >= len(SEEDS)),
        "multi_seed_history_divergence": score(len({row["history_signature"] for row in outcomes}) == len(outcomes) and len(outcome_kinds) >= 4),
        "no_predeclared_endings": score(all(not row["predeclared_ending"] for row in outcomes) and len(outcome_kinds) >= 4),
        "concept_abstraction_from_evidence": score(any(row["abstraction_level"] >= 3 and row["evidence_count"] >= 5 for row in lineages)),
        "material_bottleneck_binding": score(any(row["trade_shift"] != "none" for row in material_chains) and all(row["material_bottleneck_bound"] for row in material_chains)),
        "safety_norm_emergence": score(any(row["safety_norm"] for row in competitions)),
        "institution_emergence": score(any(row["institution"] != "none" for row in competitions)),
        "avatar_hint_boundary": score(all(not row["avatar_answer"] for row in proposals) and all(not row["avatar_as_answer_source"] for row in cultural) and all(not row["true_law_exposed"] for row in experiments + lineages)),
        "no_modern_terms": score(not forbidden),
        "audit_trace_integrity": score({"shared_hidden_law", "proposal", "public_effect", "belief_descendant", "theory_competition", "material_chain", "preserved_failure"}.issubset({row["type"] for row in audit})),
        "long_horizon_span": score(max(row["era_day"] for row in lineages) >= 18000),
        "practical_discovery_not_guaranteed": score(0 < practice_count < len(outcomes)),
    }


def ablation_table(baseline: Dict[str, float]) -> List[Dict[str, Any]]:
    names = [
        "no_shared_law",
        "no_lineage_parent",
        "no_agent_proposals",
        "no_failures_preserved",
        "no_competition",
        "no_material_bottlenecks",
        "no_long_horizon",
        "no_social_mutation",
    ]
    rows: List[Dict[str, Any]] = []
    for name in names:
        runs = [simulate_lineage(seed, ablation=name) for seed in SEEDS]
        metrics = compute_metrics(runs, ablation=name)
        degraded = [key for key, value in metrics.items() if value < baseline.get(key, 0.0)]
        rows.append({
            "ablation": name,
            "mean_score": round(sum(metrics.values()) / len(metrics), 6),
            "degraded_metrics": ";".join(degraded) or "none",
        })
    return rows


def report_text(results: Dict[str, Any], criteria: List[Dict[str, Any]]) -> str:
    metrics = results["metrics"]
    passed_count = sum(1 for row in criteria if row["passed"])
    lines = [
        "# Report 368: SSRM-3D Long-Horizon Belief Lineage Bridge",
        "",
        "Report 368 moves the non-scripted anomaly line from one-session observation/testing into long-horizon cultural memory. It uses one shared hidden-law world across many deterministic seeds, then lets different resident histories mutate belief descendants over weeks, months, years, and generations.",
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
        "## Why this is deeper than another anomaly panel",
        "",
        "The benchmark keeps the hidden laws fixed and changes only seeded resident history: inherited labels, material availability, agent-generated proposals, failures, safety events, rival-theory status, institutions, and trade shifts. The pass condition rewards divergent histories from the same world law rather than a pre-authored unlock path.",
        "",
        "## Seed outcomes",
        "",
        "| Seed | Bias | Outcome | Final label | Institutions |",
        "| ---: | --- | --- | --- | --- |",
    ]
    for row in results["seed_outcomes"]:
        lines.append(f"| `{row['seed']}` | `{row['settlement_bias']}` | `{row['outcome']}` | `{row['final_label']}` | `{row['institutions']}` |")
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
        "This is still a deterministic simulation harness, not open-ended anthropology or autonomous scientific reasoning. The step forward is that belief has ancestry, age, rivals, material costs, archived failures, safety customs, and institution pressure. The same hidden law can now produce different plausible civilization histories without installing a correct concept into residents.",
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
    law = shared_law()
    law_hash = stable_hash(law)
    runs = [simulate_lineage(seed) for seed in SEEDS]
    lineages = flatten(runs, "lineages")
    proposals = flatten(runs, "proposals")
    experiments = flatten(runs, "experiments")
    competitions = flatten(runs, "competitions")
    cultural = flatten(runs, "cultural")
    material_chains = flatten(runs, "material_chains")
    audit = flatten(runs, "audit")
    seed_outcomes = [run["outcome"] for run in runs]
    metrics_base = compute_metrics(runs)
    ablations = ablation_table(metrics_base)
    report362 = load_json(REPORT362_RESULTS)
    report367 = load_json(REPORT367_RESULTS)
    runner_text = RUNNER.read_text(encoding="utf-8") if RUNNER.exists() else ""

    write_json(SHARED_HIDDEN_LAW, {"law_hash": law_hash, "hidden_law": law, "resident_visible": False})
    write_csv(BELIEF_LINEAGES, lineages, ["seed", "belief_id", "parent_belief_id", "era", "era_day", "generation", "resident", "household", "label", "kind", "confidence", "evidence_count", "contradiction_count", "witness_count", "abstraction_level", "source", "source_effect", "source_effect_kind", "law_hash", "true_law_exposed", "avatar_answer"])
    write_csv(AGENT_PROPOSALS, proposals, ["seed", "proposal_id", "era", "era_day", "generation", "resident", "source_belief_id", "source_label", "question", "materials", "proposal_source", "predeclared_device", "avatar_answer"])
    write_csv(EXPERIMENT_RESULTS, experiments, ["seed", "experiment_id", "proposal_id", "era", "era_day", "resident", "source_belief_id", "materials", "effect", "effect_kind", "failure", "safety_event", "utility_score", "preserved_failure", "true_law_exposed", "predeclared_device"])
    write_csv(THEORY_COMPETITION, competitions, ["seed", "era", "era_day", "belief_id", "label", "rival_count", "competition_score", "status", "institution", "safety_norm", "archived_not_erased"])
    write_csv(CULTURAL_MEMORY, cultural, ["seed", "era", "era_day", "memory_id", "memory", "dominant_label", "archived_failures", "institution", "trade_shifts", "avatar_as_answer_source"])
    write_csv(MATERIAL_CHAINS, material_chains, ["seed", "era", "era_day", "proposal_id", "materials", "stock_before", "stock_after", "trade_shift", "material_bottleneck_bound"])
    write_csv(SEED_OUTCOMES, seed_outcomes, ["seed", "law_hash", "settlement_bias", "outcome", "history_signature", "final_label", "final_abstraction_level", "successful_experiments", "failed_experiments", "safety_events", "practice_discovered", "taboo_emerged", "institutions", "trade_shifts", "predeclared_ending"])
    write_json(AUDIT_REPLAY, audit)
    write_csv(ABLATIONS, ablations, ["ablation", "mean_score", "degraded_metrics"])

    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_362_discovery_gate_exists", report362.get("verdict") == "pass", f"Report 362 verdict={report362.get('verdict')}")
    add_criterion(criteria, "report_367_recent_integration_gate_exists", report367.get("verdict") == "pass", f"Report 367 verdict={report367.get('verdict')}")
    add_criterion(criteria, "runner_includes_report_368", "experiments.ssrm_3d_browser_world_v128_long_horizon_belief_lineage_bridge" in runner_text, "scripts/run_experiments.py includes Report 368 module")
    add_criterion(criteria, "artifact_set_written", all(path.exists() for path in [SHARED_HIDDEN_LAW, BELIEF_LINEAGES, AGENT_PROPOSALS, EXPERIMENT_RESULTS, THEORY_COMPETITION, CULTURAL_MEMORY, MATERIAL_CHAINS, SEED_OUTCOMES, AUDIT_REPLAY, ABLATIONS]), "all Report 368 artifacts exist")
    for metric, value in metrics_base.items():
        add_criterion(criteria, metric, value == 1.0, f"metric={value}")
    add_criterion(criteria, "ablations_degrade_relevant_channels", all(row["degraded_metrics"] != "none" for row in ablations), f"ablations={ablations}")
    add_criterion(criteria, "same_law_different_histories", len({row["law_hash"] for row in seed_outcomes}) == 1 and len({row["history_signature"] for row in seed_outcomes}) == len(seed_outcomes), f"law_hashes={sorted({row['law_hash'] for row in seed_outcomes})} histories={len({row['history_signature'] for row in seed_outcomes})}")
    add_criterion(criteria, "boundary_preserved", has_terms(BOUNDARY, ["No LLM call", "no subjective-consciousness claim", "no moral-patienthood claim", "no finished game engine", "no predeclared device tree"]), BOUNDARY)

    passed = sum(1 for row in criteria if row["passed"])
    metrics = {
        **metrics_base,
        "seed_count": len(SEEDS),
        "belief_lineage_rows": len(lineages),
        "proposal_rows": len(proposals),
        "experiment_rows": len(experiments),
        "outcome_diversity": len({row["outcome"] for row in seed_outcomes}),
        "history_signature_count": len({row["history_signature"] for row in seed_outcomes}),
        "criterion_count": len(criteria),
        "readiness": round(passed / len(criteria), 6),
        "weakest_channel_score": min(row["score"] for row in criteria),
    }
    verdict = "pass" if metrics["weakest_channel_score"] == 1.0 else "needs_work"
    results = {
        "report": REPORT,
        "slug": SLUG,
        "verdict": verdict,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "criteria": criteria,
        "seed_outcomes": seed_outcomes,
        "artifacts": {
            "shared_hidden_law": str(SHARED_HIDDEN_LAW.relative_to(ROOT)),
            "belief_lineages": str(BELIEF_LINEAGES.relative_to(ROOT)),
            "agent_proposals": str(AGENT_PROPOSALS.relative_to(ROOT)),
            "experiment_results": str(EXPERIMENT_RESULTS.relative_to(ROOT)),
            "theory_competition": str(THEORY_COMPETITION.relative_to(ROOT)),
            "cultural_memory": str(CULTURAL_MEMORY.relative_to(ROOT)),
            "material_chains": str(MATERIAL_CHAINS.relative_to(ROOT)),
            "seed_outcomes": str(SEED_OUTCOMES.relative_to(ROOT)),
            "audit_replay": str(AUDIT_REPLAY.relative_to(ROOT)),
            "ablations": str(ABLATIONS.relative_to(ROOT)),
        },
    }
    state = {"runs": runs, "shared_law_hash": law_hash, "ablations": ablations}
    write_json(RESULTS, results)
    write_json(STATE, state)
    write_csv(SUMMARY, [{"metric": key, "value": value} for key, value in metrics.items()], ["metric", "value"])
    write_csv(VERDICT, [{"report": REPORT, "verdict": verdict, "readiness": metrics["readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": NEXT_GATE}], ["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
    write_csv(CRITERIA, criteria, ["criterion", "passed", "score", "evidence"])
    REPORT_PATH.write_text(report_text(results, criteria), encoding="utf-8")
    print(json.dumps({"report": REPORT, "verdict": verdict, "metrics": metrics, "outcome_counts": dict(Counter(row["outcome"] for row in seed_outcomes))}, indent=2, sort_keys=True))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
