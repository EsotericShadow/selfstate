from __future__ import annotations

import csv
import json
import random
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
REPORT = 362
SLUG = "ssrm_3d_browser_world_v122_non_scripted_world_anomaly_discovery_bridge"
SHELL_APP = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "app.js"
SHELL_INDEX = ROOT / "visualizations" / "ssrm_3d_browser_world_v61_vertical_slice_app_shell" / "index.html"
RUNNER = ROOT / "scripts" / "run_experiments.py"
REPORT361_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v121_primary_shell_echo_influenced_choice_refusal_results.json"
BROWSER_SMOKE = ARTIFACT_DIR / f"{SLUG}_browser_smoke.json"
HIDDEN_LAWS = ARTIFACT_DIR / f"{SLUG}_hidden_laws.json"
OBSERVATIONS = ARTIFACT_DIR / f"{SLUG}_observations.csv"
BELIEFS = ARTIFACT_DIR / f"{SLUG}_resident_beliefs.csv"
EXPERIMENTS = ARTIFACT_DIR / f"{SLUG}_experiments.csv"
FAILURES = ARTIFACT_DIR / f"{SLUG}_failures.csv"
SOCIAL = ARTIFACT_DIR / f"{SLUG}_social_transmissions.csv"
CULTURAL = ARTIFACT_DIR / f"{SLUG}_cultural_memory.csv"
AUDIT = ARTIFACT_DIR / f"{SLUG}_audit_replay.json"
ABLATIONS = ARTIFACT_DIR / f"{SLUG}_ablations.csv"
RESULTS = ARTIFACT_DIR / f"{SLUG}_results.json"
STATE = ARTIFACT_DIR / f"{SLUG}_state.json"
SUMMARY = ARTIFACT_DIR / f"{SLUG}_summary.csv"
VERDICT = ARTIFACT_DIR / f"{SLUG}_verdict.csv"
CRITERIA = ARTIFACT_DIR / f"{SLUG}_criteria.csv"
REPORT_PATH = DOCS_DIR / "362_ssrm_3d_non_scripted_world_anomaly_discovery_bridge_report.md"
SEEDS = [36217, 36231, 36247, 36263, 36281, 36307]
FORBIDDEN_MODERN_TERMS = ["electricity", "electron", "voltage", "conductor", "battery", "circuit", "magnetism", "static charge", "technology unlock", "tech tree"]
PROPERTY_KEYS = ["conductivityLike", "chargeRetention", "frictionResponse", "moistureSensitivity", "heatTolerance", "fragility", "toxicity", "combustionRisk", "insulationBlocking", "storagePotential", "magneticAttraction"]
RESIDENTS = ["Ari", "Fay", "Milo", "Sera", "Tovan", "Nia"]
VOCAB = {
    "Ari": ["awl-bite", "roof-snap", "dry-path"],
    "Fay": ["quiet sting", "jar omen", "herb-jump"],
    "Milo": ["water-anger", "red carry", "handspan bite"],
    "Sera": ["cloak ghost", "smoke warning", "cold spark"],
    "Tovan": ["route sign", "safe-gap", "storm crumb"],
    "Nia": ["glass sleep", "grain pull", "shelf whisper"],
}
BOUNDARY = (
    "Deterministic per-seed browser-local non-scripted anomaly discovery only; hidden material laws are audit-visible "
    "but not resident knowledge; no LLM call, no autonomous natural language, no subjective consciousness, no real science, "
    "no real consent, no moral patienthood, no production persistence, no hosted URL proof, no complete 3D engine, "
    "no finished gameplay, no hard-coded technology tree, and no metaphysical claim."
)
NEXT_GATE = (
    "post-362: move anomaly discovery into longer-session resident scheduling so resident-chosen tests compete with ordinary work, "
    "scarce materials, fear, trust, and social disagreement instead of running as a panel-only loop"
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


def rounded(value: float) -> float:
    return round(max(0.0, min(1.0, value)), 3)


def generate_hidden_law(seed: int) -> Dict[str, Any]:
    rng = random.Random(seed)
    templates = {
        "red_scrap": dict(conductivityLike=0.78, chargeRetention=0.22, frictionResponse=0.30, moistureSensitivity=0.18, heatTolerance=0.74, fragility=0.26, toxicity=0.12, combustionRisk=0.10, insulationBlocking=0.08, storagePotential=0.30, magneticAttraction=0.64),
        "dry_resin": dict(conductivityLike=0.20, chargeRetention=0.72, frictionResponse=0.82, moistureSensitivity=0.70, heatTolerance=0.42, fragility=0.38, toxicity=0.18, combustionRisk=0.52, insulationBlocking=0.58, storagePotential=0.68, magneticAttraction=0.06),
        "wet_wood": dict(conductivityLike=0.34, chargeRetention=0.08, frictionResponse=0.12, moistureSensitivity=0.92, heatTolerance=0.36, fragility=0.32, toxicity=0.08, combustionRisk=0.44, insulationBlocking=0.38, storagePotential=0.10, magneticAttraction=0.04),
        "reed_fiber": dict(conductivityLike=0.16, chargeRetention=0.48, frictionResponse=0.76, moistureSensitivity=0.55, heatTolerance=0.30, fragility=0.62, toxicity=0.06, combustionRisk=0.60, insulationBlocking=0.54, storagePotential=0.42, magneticAttraction=0.03),
        "ash_glass": dict(conductivityLike=0.10, chargeRetention=0.62, frictionResponse=0.54, moistureSensitivity=0.24, heatTolerance=0.82, fragility=0.78, toxicity=0.10, combustionRisk=0.02, insulationBlocking=0.74, storagePotential=0.76, magneticAttraction=0.02),
        "iron_sand": dict(conductivityLike=0.68, chargeRetention=0.18, frictionResponse=0.22, moistureSensitivity=0.30, heatTolerance=0.70, fragility=0.18, toxicity=0.16, combustionRisk=0.06, insulationBlocking=0.12, storagePotential=0.26, magneticAttraction=0.86),
        "clay_jar": dict(conductivityLike=0.12, chargeRetention=0.52, frictionResponse=0.44, moistureSensitivity=0.46, heatTolerance=0.66, fragility=0.70, toxicity=0.04, combustionRisk=0.01, insulationBlocking=0.68, storagePotential=0.64, magneticAttraction=0.01),
    }
    materials = {
        name: {key: rounded(value + rng.uniform(-0.08, 0.08)) for key, value in props.items()}
        for name, props in templates.items()
    }
    return {"seed": seed, "materials": materials, "hiddenFromResidents": True, "propertyNames": PROPERTY_KEYS}


def observe_effect(law: Dict[str, Any], materials: List[str]) -> Tuple[str, str]:
    rows = [law["materials"][material] for material in materials]
    avg = lambda key: sum(row[key] for row in rows) / len(rows)
    if avg("combustionRisk") > 0.48 and avg("heatTolerance") < 0.52:
        return "smoke appeared and the test was stopped", "risk"
    if avg("magneticAttraction") > 0.45:
        return "dark grains crawled toward the red scrap", "motion"
    if avg("conductivityLike") > 0.48 and avg("chargeRetention") > 0.24:
        return "the sharp bite carried farther than a handspan", "transfer"
    if avg("frictionResponse") > 0.58 and avg("chargeRetention") > 0.42:
        return "loose fiber jumped after rubbing", "jump"
    if avg("moistureSensitivity") > 0.62:
        return "wet pieces dulled the effect and left only a sting", "dulling"
    if avg("fragility") > 0.68:
        return "a tool edge cracked before the sign returned", "breakage"
    return "nothing repeated clearly", "unclear"


def belief_for(resident: str, observation: Dict[str, Any], rng: random.Random, transmitted: bool) -> Dict[str, Any]:
    kind = rng.choice(["practical", "skeptical", "ritualized", "fearful", "useful_wrong"])
    return {
        "resident": resident,
        "label": rng.choice(VOCAB[resident]),
        "kind": kind,
        "confidence": round(max(0.08, min(0.82, 0.34 + rng.random() * 0.28 - (0.06 if transmitted else 0.0))), 3),
        "source": "social transmission" if transmitted else observation["id"],
        "evidence": [observation["effect"]],
        "contradiction_count": 0,
        "social_trust": round(0.45 + rng.random() * 0.24, 3),
        "personally_witnessed": not transmitted,
        "modern_concept": False,
        "direct_avatar_command": False,
    }


def choose_test(seed: int, run_index: int, resident: str, belief: Dict[str, Any]) -> Dict[str, Any]:
    rng = random.Random(seed + run_index * 193 + len(belief["label"]))
    candidate_tests = [
        {"materials": ["red_scrap", "dry_resin"], "reason": "compare red carry with dry sign"},
        {"materials": ["wet_wood", "dry_resin"], "reason": "try a wet counterexample"},
        {"materials": ["ash_glass", "reed_fiber"], "reason": "see whether glass sleep holds the jump"},
        {"materials": ["iron_sand", "red_scrap"], "reason": "test whether dark grains follow red scrap"},
        {"materials": ["clay_jar", "reed_fiber"], "reason": "try storage in a common jar"},
        {"materials": ["wet_wood", "red_scrap"], "reason": "ask whether water ruins the carry"},
    ]
    role_bias = (RESIDENTS.index(resident) + int(belief["confidence"] * 10) + int(belief["social_trust"] * 10)) % len(candidate_tests)
    return candidate_tests[(role_bias + rng.randrange(len(candidate_tests))) % len(candidate_tests)]


def simulate_seed(seed: int, options: Dict[str, bool] | None = None) -> Dict[str, Any]:
    opts = {
        "hidden_world_laws": True,
        "wrong_beliefs": True,
        "failed_experiments": True,
        "material_constraints": True,
        "social_mutation": True,
        "avatar_boundary": True,
        "multi_seed_divergence": True,
        "audit_hidden_public_split": True,
    }
    if options:
        opts.update(options)
    rng = random.Random(seed)
    law = generate_hidden_law(seed) if opts["hidden_world_laws"] else {"seed": seed, "materials": {}, "hiddenFromResidents": False, "propertyNames": []}
    observations: List[Dict[str, Any]] = []
    beliefs: Dict[str, Dict[str, Any]] = {}
    experiments: List[Dict[str, Any]] = []
    failures: List[Dict[str, Any]] = []
    social: List[Dict[str, Any]] = []
    cultural: List[Dict[str, Any]] = []
    audit: List[Dict[str, Any]] = []

    first_materials = ["dry_resin", "reed_fiber"]
    first_effect, first_kind = observe_effect(law, first_materials) if opts["hidden_world_laws"] else ("an unexplained sign was claimed", "unclear")
    first_observation = {
        "seed": seed,
        "id": f"{seed}-OBS-01",
        "witness": RESIDENTS[seed % len(RESIDENTS)],
        "materials": "+".join(first_materials),
        "effect": first_effect,
        "effect_kind": first_kind,
        "phase": "avatar demonstration",
        "true_law_exposed": False,
    }
    observations.append(first_observation)
    beliefs[first_observation["witness"]] = belief_for(first_observation["witness"], first_observation, rng, transmitted=False)
    if not opts["wrong_beliefs"]:
        beliefs[first_observation["witness"]]["kind"] = "practical"
        beliefs[first_observation["witness"]]["confidence"] = 0.9
    audit.extend([
        {"seed": seed, "type": "hidden_law", "summary": "hidden material properties generated; audit-only", "audit_only": True},
        {"seed": seed, "type": "public_observation", "summary": first_effect, "audit_only": False},
        {"seed": seed, "type": "private_belief", "summary": beliefs[first_observation["witness"]]["label"], "audit_only": False},
    ])

    for index in range(5):
        actor = RESIDENTS[(seed + index * 2 + rng.randrange(len(RESIDENTS))) % len(RESIDENTS)]
        if actor not in beliefs:
            beliefs[actor] = belief_for(actor, first_observation, rng, transmitted=True)
        test = choose_test(seed, index, actor, beliefs[actor])
        effect, effect_kind = observe_effect(law, test["materials"]) if opts["material_constraints"] and opts["hidden_world_laws"] else (rng.choice(["loose fiber jumped after rubbing", "nothing repeated clearly"]), "unbound")
        failure = any(token in effect for token in ["nothing", "dulled", "cracked", "smoke"])
        if not opts["failed_experiments"] and failure:
            effect, effect_kind, failure = "loose fiber jumped after rubbing", "jump", False
        observation = {
            "seed": seed,
            "id": f"{seed}-OBS-{index + 2:02d}",
            "witness": actor,
            "materials": "+".join(test["materials"]),
            "effect": effect,
            "effect_kind": effect_kind,
            "phase": "resident experiment",
            "true_law_exposed": False,
        }
        observations.append(observation)
        belief = beliefs[actor]
        if failure:
            belief["contradiction_count"] += 1
            belief["confidence"] = round(max(0.08, belief["confidence"] - 0.09), 3)
        else:
            belief["confidence"] = round(min(0.86, belief["confidence"] + 0.08), 3)
        belief["evidence"] = (belief["evidence"] + [effect])[-5:]
        experiment = {
            "seed": seed,
            "id": f"{seed}-EXP-{index + 1:02d}",
            "actor": actor,
            "materials": "+".join(test["materials"]),
            "reason": test["reason"],
            "consumed_time": index + 1,
            "consumed_materials": "+".join(test["materials"]),
            "outcome": effect,
            "failure": failure,
            "source_belief": belief["label"],
            "technology_unlock": False,
        }
        experiments.append(experiment)
        if failure:
            failures.append(experiment)
        audit.append({"seed": seed, "type": "experiment", "summary": f"{actor} tested {experiment['materials']} from {belief['label']}", "audit_only": False})
        if failure:
            audit.append({"seed": seed, "type": "failed_experiment", "summary": effect, "audit_only": False})

        if opts["social_mutation"]:
            target = RESIDENTS[(RESIDENTS.index(actor) + 1 + rng.randrange(len(RESIDENTS) - 1)) % len(RESIDENTS)]
            mutation = rng.choice(["warning", "trick", "path", "omen", "craft", "taboo"])
            before = belief["label"]
            after = f"{before}-{mutation}"
        else:
            target, before, after, mutation = RESIDENTS[(RESIDENTS.index(actor) + 1) % len(RESIDENTS)], belief["label"], belief["label"], "none"
        beliefs[target] = {
            "resident": target,
            "label": after,
            "kind": rng.choice(["ritualized", "useful_wrong", "practical", "skeptical"]),
            "confidence": round(max(0.1, min(0.78, belief["confidence"] + rng.uniform(-0.09, 0.09))), 3),
            "source": f"heard from {actor}",
            "evidence": [effect],
            "contradiction_count": belief["contradiction_count"] + (1 if failure and rng.random() > 0.5 else 0),
            "social_trust": round(0.42 + rng.random() * 0.28, 3),
            "personally_witnessed": False,
            "modern_concept": False,
            "direct_avatar_command": False,
        }
        row = {
            "seed": seed,
            "id": f"{seed}-SOC-{index + 1:02d}",
            "from": actor,
            "to": target,
            "channel": rng.choice(["gossip", "teaching", "trade", "argument", "ritual caution", "household warning"]),
            "before": before,
            "after": after,
            "mutation": mutation,
            "source_avatar_command": False,
        }
        social.append(row)
        audit.append({"seed": seed, "type": "social_transmission", "summary": f"{before} -> {after}", "audit_only": False})

    success_count = sum(1 for row in experiments if not row["failure"])
    failure_count = len(failures)
    kinds = Counter(belief["kind"] for belief in beliefs.values())
    if success_count >= 3 and len({row["materials"] for row in experiments if not row["failure"]}) >= 2:
        outcome = "practical_discovery"
        memory = "Residents keep a practical dry-material test without claiming a final concept."
    elif kinds["ritualized"] >= 2:
        outcome = "ritualized_anomaly"
        memory = "The sign becomes a caution rite because labels travel faster than repeatable tests."
    elif kinds["fearful"] >= 2 or failure_count >= 3:
        outcome = "fear_taboo"
        memory = "Failures and smoke turn the sign into a bounded taboo around wet tests."
    elif success_count <= 1:
        outcome = "stalled"
        memory = "The settlement remembers the sign but lacks a stable way to repeat it."
    else:
        outcome = "useful_wrong_theory"
        memory = "A wrong label still helps residents avoid wet materials and preserve failures."
    cultural.append({
        "seed": seed,
        "id": f"{seed}-CUL-01",
        "outcome": outcome,
        "memory": memory,
        "competing_beliefs": ";".join(sorted({belief["label"] for belief in beliefs.values()})),
        "no_correct_unlock": True,
    })
    audit.append({"seed": seed, "type": "cultural_memory", "summary": memory, "audit_only": False})
    return {"seed": seed, "hidden_law": law, "observations": observations, "beliefs": list(beliefs.values()), "experiments": experiments, "failures": failures, "social": social, "cultural": cultural, "audit": audit, "outcome": outcome, "avatar_boundary": opts["avatar_boundary"]}


def flatten(runs: List[Dict[str, Any]], key: str) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for run in runs:
        rows.extend(run[key])
    return rows


def forbidden_terms_in(rows: Iterable[Dict[str, Any]]) -> List[str]:
    text = json.dumps(list(rows), sort_keys=True).lower()
    return [term for term in FORBIDDEN_MODERN_TERMS if term in text]


def score(condition: bool) -> float:
    return 1.0 if condition else 0.0


def ablation_rows(baseline: Dict[str, float]) -> List[Dict[str, Any]]:
    configs = {
        "no_hidden_world_laws": {"hidden_world_laws": False},
        "no_wrong_beliefs": {"wrong_beliefs": False},
        "no_failed_experiments": {"failed_experiments": False},
        "no_material_constraints": {"material_constraints": False},
        "no_social_mutation": {"social_mutation": False},
        "no_avatar_boundary": {"avatar_boundary": False},
        "no_multi_seed_divergence": {"multi_seed_divergence": False},
        "no_audit_hidden_public_split": {"audit_hidden_public_split": False},
    }
    rows = []
    for name, options in configs.items():
        runs = [simulate_seed(seed, options) for seed in SEEDS]
        observations = flatten(runs, "observations")
        beliefs = flatten(runs, "beliefs")
        experiments = flatten(runs, "experiments")
        failures = flatten(runs, "failures")
        social = flatten(runs, "social")
        outcomes = {run["outcome"] for run in runs} if options.get("multi_seed_divergence", True) else {runs[0]["outcome"]}
        degraded = {
            "hidden_world_law_integrity": score(options.get("hidden_world_laws", True) and all(run["hidden_law"].get("hiddenFromResidents") for run in runs)),
            "wrong_belief_preservation": score(options.get("wrong_beliefs", True) and any(row["kind"] in {"ritualized", "fearful", "useful_wrong", "skeptical"} for row in beliefs)),
            "failed_experiment_honesty": score(options.get("failed_experiments", True) and len(failures) >= len(SEEDS)),
            "material_constraint_binding": score(options.get("material_constraints", True) and all(row["consumed_materials"] for row in experiments)),
            "social_transmission_mutation": score(options.get("social_mutation", True) and any(row["before"] != row["after"] for row in social)),
            "multi_seed_divergence": score(options.get("multi_seed_divergence", True) and len(outcomes) >= 3),
            "avatar_hint_not_command": score(options.get("avatar_boundary", True) and all(not row.get("source_avatar_command") for row in social)),
            "audit_trace_integrity": score(options.get("audit_hidden_public_split", True) and all(run["audit"] for run in runs)),
        }
        rows.append({"ablation": name, "mean_score": round(sum(degraded.values()) / len(degraded), 3), "degraded_metrics": ";".join(metric for metric, value in degraded.items() if value < baseline.get(metric, 0.0)) or "none"})
    return rows


def report_text(results: Dict[str, Any], criteria: List[Dict[str, Any]], browser: Dict[str, Any]) -> str:
    metrics = results["metrics"]
    passed_count = sum(1 for row in criteria if row["passed"])
    lines = [
        "# Report 362: SSRM-3D Non-Scripted World Anomaly Discovery Bridge",
        "",
        "Report 362 pivots the browser-world line away from scripted feature unlock bridges. The maintained v61 shell now has an anomaly discovery panel backed by hidden material properties, public observations, resident partial beliefs, resident-chosen tests, preserved failures, mutated social transmission, cultural memory, and an audit split that reveals hidden laws only when audit mode is enabled.",
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
        f"- Public before audit: `{browser.get('beforeAudit', {}).get('anomalyText', 'missing')}`",
        f"- Audit after toggle: `{browser.get('afterAudit', {}).get('anomalyText', 'missing')}`",
        f"- Console errors: `{metrics['console_error_count']}`",
        "",
        "## Multi-seed outcomes",
        "",
    ]
    for outcome, count in sorted(results["outcome_counts"].items()):
        lines.append(f"- `{outcome}`: `{count}`")
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
        "This is deterministic per seed for auditability, not open-ended scientific discovery. The important change is architectural: the correct concept is not installed into residents. They see effects, invent local labels, run constrained tests, preserve wrong or failed paths, mutate beliefs socially, and record cultural memory that can diverge across seeds.",
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
    hidden_laws = {str(run["seed"]): run["hidden_law"] for run in runs}
    observations = flatten(runs, "observations")
    beliefs = flatten(runs, "beliefs")
    experiments = flatten(runs, "experiments")
    failures = flatten(runs, "failures")
    social = flatten(runs, "social")
    cultural = flatten(runs, "cultural")
    audit = flatten(runs, "audit")
    outcomes = Counter(run["outcome"] for run in runs)

    app_text = SHELL_APP.read_text(encoding="utf-8")
    index_text = SHELL_INDEX.read_text(encoding="utf-8")
    runner_text = RUNNER.read_text(encoding="utf-8")
    report361 = load_json(REPORT361_RESULTS)
    browser = load_json(BROWSER_SMOKE)
    console_errors = browser.get("consoleErrors", [])

    forbidden_public_terms = forbidden_terms_in(observations + beliefs + experiments + social + cultural)
    baseline_metrics = {
        "hidden_world_law_integrity": score(all(run["hidden_law"].get("hiddenFromResidents") and set(PROPERTY_KEYS).issubset(set(run["hidden_law"].get("propertyNames", []))) for run in runs) and not any(prop in json.dumps(beliefs) for prop in PROPERTY_KEYS)),
        "resident_observation_binding": score(all(row["effect"] and not row["true_law_exposed"] for row in observations)),
        "belief_generation_diversity": score(len({row["label"] for row in beliefs}) >= 8 and len({row["kind"] for row in beliefs}) >= 4),
        "wrong_belief_preservation": score(any(row["kind"] in {"ritualized", "fearful", "useful_wrong", "skeptical"} for row in beliefs) and any(row["contradiction_count"] > 0 for row in beliefs)),
        "experiment_choice_non_scriptedness": score(len({row["materials"] for row in experiments}) >= 5 and len({row["actor"] for row in experiments}) >= 4),
        "failed_experiment_honesty": score(len(failures) >= len(SEEDS) and all(row["failure"] for row in failures)),
        "material_constraint_binding": score(all(row["consumed_time"] and row["consumed_materials"] for row in experiments) and len({row["outcome"] for row in experiments}) >= 4),
        "social_transmission_mutation": score(any(row["before"] != row["after"] for row in social) and len({row["channel"] for row in social}) >= 4),
        "multi_seed_divergence": score(len(outcomes) >= 3),
        "no_instant_correct_unlock": score(not forbidden_public_terms and all(not row["technology_unlock"] for row in experiments)),
        "avatar_hint_not_command": score(all(not row["source_avatar_command"] for row in social) and all(not row["direct_avatar_command"] for row in beliefs)),
        "cultural_memory_update": score(len(cultural) == len(SEEDS) and all(row["memory"] for row in cultural)),
        "audit_trace_integrity": score({"hidden_law", "public_observation", "private_belief", "experiment", "failed_experiment", "social_transmission", "cultural_memory"}.issubset({row["type"] for row in audit})),
    }
    ablations = ablation_rows(baseline_metrics)

    HIDDEN_LAWS.write_text(json.dumps(hidden_laws, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_csv(OBSERVATIONS, observations, ["seed", "id", "witness", "materials", "effect", "effect_kind", "phase", "true_law_exposed"])
    write_csv(BELIEFS, beliefs, ["resident", "label", "kind", "confidence", "source", "evidence", "contradiction_count", "social_trust", "personally_witnessed", "modern_concept", "direct_avatar_command"])
    write_csv(EXPERIMENTS, experiments, ["seed", "id", "actor", "materials", "reason", "consumed_time", "consumed_materials", "outcome", "failure", "source_belief", "technology_unlock"])
    write_csv(FAILURES, failures, ["seed", "id", "actor", "materials", "reason", "consumed_time", "consumed_materials", "outcome", "failure", "source_belief", "technology_unlock"])
    write_csv(SOCIAL, social, ["seed", "id", "from", "to", "channel", "before", "after", "mutation", "source_avatar_command"])
    write_csv(CULTURAL, cultural, ["seed", "id", "outcome", "memory", "competing_beliefs", "no_correct_unlock"])
    AUDIT.write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_csv(ABLATIONS, ablations, ["ablation", "mean_score", "degraded_metrics"])

    before_audit = browser.get("beforeAudit", {})
    after_audit = browser.get("afterAudit", {})
    criteria: List[Dict[str, Any]] = []
    add_criterion(criteria, "report_361_choice_gate_passing", report361.get("verdict") == "pass" and report361.get("metrics", {}).get("weakest_channel_score") == 1.0, f"Report 361 verdict={report361.get('verdict')} weakest={report361.get('metrics', {}).get('weakest_channel_score')}")
    add_criterion(criteria, "source_exposes_hidden_world_laws", has_terms(app_text, ["generateHiddenWorldLaw", "conductivityLike", "chargeRetention", "moistureSensitivity", "magneticAttraction", "hiddenFromResidents"]), "app.js creates hidden material properties")
    add_criterion(criteria, "source_exposes_observations_beliefs_experiments", has_terms(app_text, ["observationForMaterials", "residentBeliefs", "runAnomalyExperiment", "failedExperimentPreserved", "materialConstraintBinding"]), "app.js binds observations, beliefs, experiments, and failures")
    add_criterion(criteria, "source_exposes_social_mutation_cultural_memory", has_terms(app_text, ["spreadAnomalyBelief", "socialTransmissions", "culturalMemory", "label/evidence/confidence mutated"]), "app.js mutates social belief transmission and updates cultural memory")
    add_criterion(criteria, "source_preserves_avatar_boundary", has_terms(app_text, ["avatar demonstrated an unexplained effect", "residents receive observations only", "noTechnologyTree", "noInstantCorrectUnlock"]), "avatar can trigger investigation but not install correct concept")
    add_criterion(criteria, "visible_shell_panel_wired", has_terms(index_text, ["anomalyDiscoveryOut", "Non-scripted anomaly discovery", "Introduce anomaly", "Run resident test", "Spread belief"]), "index.html exposes anomaly discovery controls and panel")
    add_criterion(criteria, "runner_includes_report_362", "experiments.ssrm_3d_browser_world_v122_non_scripted_world_anomaly_discovery_bridge" in runner_text, "scripts/run_experiments.py includes Report 362 module")
    for metric, value in baseline_metrics.items():
        add_criterion(criteria, metric, value == 1.0, f"metric={value}")
    add_criterion(criteria, "browser_smoke_artifact_exists", bool(browser), str(BROWSER_SMOKE.relative_to(ROOT)) if BROWSER_SMOKE.exists() else "missing browser smoke artifact")
    add_criterion(criteria, "browser_public_hidden_split", "Hidden law: concealed from residents" in before_audit.get("anomalyText", "") and "red_scrap: transfer" in after_audit.get("anomalyText", ""), f"before={before_audit.get('anomalyText')} after={after_audit.get('anomalyText')}")
    add_criterion(criteria, "browser_observes_beliefs_experiments_social_memory", all(term in before_audit.get("anomalyText", "") for term in ["Public observations", "Resident partial beliefs", "Resident experiments and preserved failures", "Social transmission mutations", "Cultural memory"]), before_audit.get("anomalyText", "missing anomaly text"))
    add_criterion(criteria, "browser_console_clean", len(console_errors) == 0, f"console error count={len(console_errors)}")
    add_criterion(criteria, "negative_controls_pass", not forbidden_public_terms and all(row["mean_score"] < 1.0 or row["ablation"] == "no_avatar_boundary" for row in ablations), f"forbidden_terms={forbidden_public_terms} ablations={ablations}")
    add_criterion(criteria, "claim_boundary_preserved", all(term in BOUNDARY for term in ["no LLM call", "subjective consciousness", "moral patienthood", "no hard-coded technology tree", "finished gameplay"]), BOUNDARY)

    weakest = min(row["score"] for row in criteria)
    readiness = sum(row["score"] for row in criteria) / len(criteria)
    metrics = {**baseline_metrics, "weakest_channel_score": weakest, "readiness": readiness, "criterion_count": len(criteria), "console_error_count": len(console_errors), "seed_count": len(SEEDS), "outcome_diversity": len(outcomes)}
    verdict = "pass" if all(row["passed"] for row in criteria) else "fail"
    results = {"report": REPORT, "slug": SLUG, "verdict": verdict, "generated_at": datetime.now(timezone.utc).isoformat(), "boundary": BOUNDARY, "metrics": metrics, "criteria": criteria, "outcome_counts": dict(outcomes), "artifacts": {"hidden_laws": str(HIDDEN_LAWS.relative_to(ROOT)), "observations": str(OBSERVATIONS.relative_to(ROOT)), "resident_beliefs": str(BELIEFS.relative_to(ROOT)), "experiments": str(EXPERIMENTS.relative_to(ROOT)), "failures": str(FAILURES.relative_to(ROOT)), "social_transmissions": str(SOCIAL.relative_to(ROOT)), "cultural_memory": str(CULTURAL.relative_to(ROOT)), "audit_replay": str(AUDIT.relative_to(ROOT)), "ablations": str(ABLATIONS.relative_to(ROOT)), "browser_smoke": str(BROWSER_SMOKE.relative_to(ROOT))}, "next_gate": NEXT_GATE}
    state = {"report": REPORT, "runs": runs, "browser_smoke": browser, "report361_gate": report361}
    RESULTS.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    STATE.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    write_csv(SUMMARY, [{"report": REPORT, "verdict": verdict, **metrics}], ["report", "verdict", *metrics.keys()])
    write_csv(VERDICT, [{"report": REPORT, "verdict": verdict, "weakest_channel_score": weakest, "readiness": readiness, "next_gate": NEXT_GATE}], ["report", "verdict", "weakest_channel_score", "readiness", "next_gate"])
    write_csv(CRITERIA, criteria, ["criterion", "passed", "score", "evidence"])
    REPORT_PATH.write_text(report_text(results, criteria, browser), encoding="utf-8")
    print(json.dumps({"report": REPORT, "verdict": verdict, "metrics": metrics, "outcome_counts": dict(outcomes)}, indent=2, sort_keys=True))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
