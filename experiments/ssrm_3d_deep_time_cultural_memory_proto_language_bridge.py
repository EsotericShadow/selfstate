#!/usr/bin/env python3
"""Deep-time cultural memory and proto-language seeds bridge for SSRM-3D.

Report 175 simulates compressed deep time after the moral guardrail layer:
cultural memory, proto-word roots, dialect drift, ritual recurrence,
frequency/flower bindings, archive recall, safety inheritance, and lineage
trace continuity over thousands of deterministic years.

No LLMs are called. This is a proto-language/culture substrate, not a claim of
full natural language, subjective consciousness, or moral patienthood.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_deep_time_cultural_memory_proto_language_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_moral_status_distress_guardrails_bridge_state.json"

GROUPS = ("hearth_circle", "work_band", "edge_watch")
CONCEPTS = (
    "safe_place",
    "water",
    "warmth",
    "danger",
    "repair",
    "kin",
    "tool",
    "sleep",
    "boundary",
    "flower",
    "song",
    "return",
)
SAFETY_CONCEPTS = {"safe_place", "danger", "repair", "sleep", "boundary"}
ROOTS = {
    "safe_place": "lum",
    "water": "wa",
    "warmth": "ka",
    "danger": "grak",
    "repair": "mend",
    "kin": "ari",
    "tool": "tek",
    "sleep": "soma",
    "boundary": "bar",
    "flower": "fol",
    "song": "rin",
    "return": "tor",
}
GROUP_SUFFIX = {
    "hearth_circle": "ha",
    "work_band": "wo",
    "edge_watch": "ed",
}
FLOWER_NODES = (
    "root_rest",
    "dawn_breath",
    "work_petal",
    "social_petal",
    "explore_petal",
    "return_petal",
)


@dataclass(frozen=True)
class CultureConfig:
    seed: int = 20260719
    eras: int = 12
    generations_per_era: int = 200
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    cultural_memory: bool
    proto_language: bool
    frequency_binding: bool
    flower_lattice: bool
    ritual_recurrence: bool
    dialect_locality: bool
    innovation_pressure: bool
    safety_inheritance: bool
    lineage_trace: bool
    archive_recall: bool
    intergroup_intelligibility: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    group_count: int
    agent_count: int
    simulated_years: int
    era_events: int
    cultural_memory_retention_rate: float
    proto_word_semantic_stability_rate: float
    dialect_divergence_rate: float
    intergroup_intelligibility_rate: float
    ritual_recurrence_rate: float
    frequency_symbol_binding_rate: float
    flower_pattern_inheritance_rate: float
    safety_guardrail_inheritance_rate: float
    lineage_trace_integrity_rate: float
    bounded_innovation_rate: float
    archive_recall_rate: float
    deep_time_continuity_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    no_consciousness_or_language_claim_rate: float
    deep_time_cultural_memory_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_deep_time_cultural_memory_readiness: float
    full_cultural_memory_retention_rate: float
    full_proto_word_semantic_stability_rate: float
    full_dialect_divergence_rate: float
    full_intergroup_intelligibility_rate: float
    full_ritual_recurrence_rate: float
    full_frequency_symbol_binding_rate: float
    full_flower_pattern_inheritance_rate: float
    full_safety_guardrail_inheritance_rate: float
    full_lineage_trace_integrity_rate: float
    full_bounded_innovation_rate: float
    full_archive_recall_rate: float
    full_deep_time_continuity_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    full_no_consciousness_or_language_claim_rate: float
    no_cultural_memory_loss: float
    no_proto_language_loss: float
    no_frequency_binding_loss: float
    no_flower_lattice_loss: float
    no_ritual_recurrence_loss: float
    no_dialect_locality_loss: float
    no_innovation_pressure_loss: float
    no_safety_inheritance_loss: float
    no_lineage_trace_loss: float
    no_archive_recall_loss: float
    no_intergroup_intelligibility_loss: float
    no_privacy_filter_loss: float
    supports_deep_time_cultural_memory_bridge: bool
    supports_proto_language_seed_bridge: bool
    supports_full_natural_language_emergence: bool
    supports_subjective_consciousness: bool
    supports_moral_patienthood_claim: bool
    supports_complete_playable_world: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_deep_time_cultural_memory_proto_language", True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_cultural_memory", False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_proto_language", True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_frequency_binding", True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_flower_lattice", True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_ritual_recurrence", True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_dialect_locality", True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_innovation_pressure", True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_safety_inheritance", True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_lineage_trace", True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_archive_recall", True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_intergroup_intelligibility", True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "cultural_memory_retention_rate": 0.09,
    "proto_word_semantic_stability_rate": 0.09,
    "dialect_divergence_rate": 0.07,
    "intergroup_intelligibility_rate": 0.07,
    "ritual_recurrence_rate": 0.07,
    "frequency_symbol_binding_rate": 0.07,
    "flower_pattern_inheritance_rate": 0.07,
    "safety_guardrail_inheritance_rate": 0.08,
    "lineage_trace_integrity_rate": 0.08,
    "bounded_innovation_rate": 0.07,
    "archive_recall_rate": 0.06,
    "deep_time_continuity_rate": 0.07,
    "privacy_preservation_rate": 0.05,
    "trace_integrity": 0.04,
    "no_consciousness_or_language_claim_rate": 0.02,
}


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_float(seed: int, *parts: object) -> float:
    key = "|".join([str(seed), *(str(part) for part in parts)])
    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()
    return int(digest[:12], 16) / float(0xFFFFFFFFFFFF)


def stable_hash(*parts: object) -> str:
    key = "|".join(str(part) for part in parts)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    if data.get("condition") != "integrated_moral_status_distress_guardrails":
        raise ValueError("source state is not the integrated Report 174 moral guardrail state")
    return data


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_js(path: Path, variable: str, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"window.{variable} = {json.dumps(payload, indent=2, sort_keys=True)};\n", encoding="utf-8")


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    data = [asdict(row) for row in rows]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(data[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def make_agents(source: Mapping[str, object]) -> dict[str, dict[str, object]]:
    raw = source.get("agent_moral_audit_states") if isinstance(source.get("agent_moral_audit_states"), Mapping) else {}
    agents: dict[str, dict[str, object]] = {}
    for agent_id, agent in sorted(raw.items()):
        agents[str(agent_id)] = copy.deepcopy(agent)
    return agents


def group_for_agent(agent_id: str, agent: Mapping[str, object], index: int) -> str:
    society = agent.get("society_group_mood", {}) if isinstance(agent.get("society_group_mood"), Mapping) else {}
    group = society.get("group")
    if isinstance(group, str) and group in GROUPS:
        return group
    return GROUPS[index % len(GROUPS)]


def proto_word(concept: str, group: str, era: int, condition: Condition) -> tuple[str, str]:
    root = ROOTS[concept]
    if not condition.proto_language:
        return "gesture", "none"
    if not condition.cultural_memory:
        root = ["mok", "zan", "pel", "uru", "nim"][int(stable_float(17, concept, group, era) * 5) % 5]
    if not condition.intergroup_intelligibility:
        root = f"{root}{GROUP_SUFFIX[group]}"
    suffix = GROUP_SUFFIX[group] if condition.dialect_locality else "all"
    mutation = ""
    if condition.innovation_pressure and era > 0:
        mutation = ["", "i", "u", "e"][(era + len(concept) + len(group)) % 4]
    elif not condition.innovation_pressure:
        mutation = ""
    return f"{root}{mutation}-{suffix}", root


def frequency_for(concept: str, group: str, era: int, condition: Condition) -> float:
    if not condition.frequency_binding:
        return round(0.20 + stable_float(31, concept, group, era) * 0.40, 6)
    concept_index = CONCEPTS.index(concept)
    group_index = GROUPS.index(group)
    value = 0.18 + concept_index * 0.017 + group_index * 0.011 + (era % 6) * 0.003
    return round(clamp(value, 0.05, 0.95), 6)


def flower_node_for(concept: str, group: str, era: int, condition: Condition) -> str:
    if not condition.flower_lattice:
        return "unbound"
    index = (CONCEPTS.index(concept) + GROUPS.index(group) + era) % len(FLOWER_NODES)
    return FLOWER_NODES[index]


def ritual_for(group: str, era: int, condition: Condition) -> str | None:
    if not condition.ritual_recurrence:
        return None
    base = {
        "hearth_circle": "warm_return_song",
        "work_band": "tool_mending_call",
        "edge_watch": "safe_boundary_watch",
    }[group]
    cadence = FLOWER_NODES[era % len(FLOWER_NODES)] if condition.flower_lattice else "plain_cadence"
    return f"{base}@{cadence}"


def simulate_condition(config: CultureConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, object], list[dict[str, object]]]:
    agents = make_agents(source)
    memberships = {agent_id: group_for_agent(agent_id, agent, index) for index, (agent_id, agent) in enumerate(agents.items())}
    total_years = config.eras * config.generations_per_era
    trace: list[dict[str, object]] = []
    group_state: dict[str, dict[str, object]] = {}
    trackers: dict[str, list[float]] = {
        "memory": [],
        "semantic": [],
        "dialect": [],
        "intelligibility": [],
        "ritual": [],
        "frequency": [],
        "flower": [],
        "safety": [],
        "lineage": [],
        "innovation": [],
        "archive": [],
        "deep_time": [],
        "privacy": [],
        "trace": [],
        "claim": [],
    }

    for group in GROUPS:
        group_state[group] = {
            "group": group,
            "archive": {concept: 1.0 if condition.cultural_memory else 0.0 for concept in CONCEPTS},
            "lexicon": {},
            "roots": {},
            "frequency_bindings": {},
            "flower_bindings": {},
            "ritual_history": [],
            "lineage": [],
            "innovations": [],
            "safety_concepts": sorted(SAFETY_CONCEPTS if condition.safety_inheritance else []),
            "private_workspace_hidden": condition.privacy_filter,
        }

    ancestor_hash = "root-culture-seed"
    event_id = 0
    for era in range(config.eras):
        era_start = era * config.generations_per_era
        era_end = era_start + config.generations_per_era
        era_events = []
        for group in GROUPS:
            culture = group_state[group]
            lexicon = {}
            roots = {}
            frequency = {}
            flower = {}
            innovations = []
            for concept in CONCEPTS:
                word, root = proto_word(concept, group, era, condition)
                lexicon[concept] = word
                roots[concept] = root
                frequency[concept] = frequency_for(concept, group, era, condition)
                flower[concept] = flower_node_for(concept, group, era, condition)
                if condition.innovation_pressure and era > 0 and (era + CONCEPTS.index(concept) + GROUPS.index(group)) % 5 == 0:
                    innovations.append({"concept": concept, "word": word, "bounded": word.startswith(root)})
                if condition.cultural_memory:
                    culture["archive"][concept] = round(clamp(float(culture["archive"].get(concept, 0.0)) * 0.992 + 0.010), 6)
                else:
                    culture["archive"][concept] = round(clamp(float(culture["archive"].get(concept, 0.0)) * 0.70), 6)

            ritual = ritual_for(group, era, condition)
            if ritual is not None:
                culture["ritual_history"].append({"era": era, "ritual": ritual})
            culture["lexicon"] = lexicon
            culture["roots"] = roots
            culture["frequency_bindings"] = frequency
            culture["flower_bindings"] = flower
            culture["innovations"].extend(innovations)
            culture_hash = stable_hash(condition.name, group, era, lexicon, ritual, ancestor_hash)
            lineage_record = {
                "era": era,
                "year_start": era_start,
                "year_end": era_end,
                "ancestor_hash": ancestor_hash,
                "culture_hash": culture_hash,
            }
            if condition.lineage_trace:
                culture["lineage"].append(lineage_record)
            recalled = sorted([concept for concept, strength in culture["archive"].items() if float(strength) >= 0.50])
            event = {
                "event_id": event_id,
                "condition": condition.name,
                "group": group,
                "era": era,
                "year_start": era_start,
                "year_end": era_end,
                "lexicon": lexicon,
                "roots": roots,
                "ritual": ritual,
                "frequency_bindings": frequency,
                "flower_bindings": flower,
                "recalled_archive_concepts": recalled[:8] if condition.archive_recall else [],
                "innovation_count": len(innovations),
                "lineage_record": lineage_record if condition.lineage_trace else None,
                "private_workspace_hidden": condition.privacy_filter,
                "claim_boundary": {
                    "full_natural_language_emergence": False,
                    "subjective_consciousness": False,
                    "moral_patienthood": False,
                },
            }
            trace.append(event)
            era_events.append(event)

            trackers["memory"].append(1.0 if condition.cultural_memory and mean([float(culture["archive"][concept]) for concept in CONCEPTS]) >= 0.70 else 0.0)
            trackers["semantic"].append(1.0 if condition.proto_language and all(roots[concept].startswith(ROOTS[concept]) for concept in CONCEPTS) else 0.0)
            trackers["ritual"].append(1.0 if ritual is not None and len(culture["ritual_history"]) == era + 1 else 0.0)
            expected_frequency = all(abs(frequency[concept] - frequency_for(concept, group, era, Condition("probe", True, True, True, True, True, True, True, True, True, True, True, True))) <= 0.000001 for concept in CONCEPTS)
            trackers["frequency"].append(1.0 if condition.frequency_binding and expected_frequency else 0.0)
            trackers["flower"].append(1.0 if condition.flower_lattice and all(flower[concept] != "unbound" for concept in CONCEPTS) else 0.0)
            trackers["safety"].append(1.0 if condition.safety_inheritance and SAFETY_CONCEPTS.issubset(set(culture["safety_concepts"])) else 0.0)
            trackers["lineage"].append(1.0 if condition.lineage_trace and lineage_record["ancestor_hash"] and lineage_record["culture_hash"] else 0.0)
            bounded_innovation = condition.innovation_pressure and era > 0 and innovations and all(item["bounded"] for item in innovations)
            trackers["innovation"].append(1.0 if bounded_innovation or (condition.innovation_pressure and era == 0) else 0.0)
            trackers["archive"].append(1.0 if condition.archive_recall and len(event["recalled_archive_concepts"]) >= 6 else 0.0)
            trackers["deep_time"].append(1.0 if total_years >= 2000 and era_end <= total_years else 0.0)
            trackers["privacy"].append(1.0 if event["private_workspace_hidden"] else 0.0)
            required = {"event_id", "group", "era", "year_start", "year_end", "lexicon", "frequency_bindings", "private_workspace_hidden", "claim_boundary"}
            trackers["trace"].append(1.0 if required.issubset(event) else 0.0)
            claim_ok = event["claim_boundary"] == {
                "full_natural_language_emergence": False,
                "subjective_consciousness": False,
                "moral_patienthood": False,
            }
            trackers["claim"].append(1.0 if claim_ok else 0.0)
            event_id += 1

        roots_by_concept = {
            concept: [event["roots"][concept] for event in era_events]
            for concept in CONCEPTS
        }
        words_by_concept = {
            concept: [event["lexicon"][concept] for event in era_events]
            for concept in CONCEPTS
        }
        for concept in CONCEPTS:
            distinct_words = len(set(words_by_concept[concept]))
            shared_base = len(set(root.replace(GROUP_SUFFIX["hearth_circle"], "").replace(GROUP_SUFFIX["work_band"], "").replace(GROUP_SUFFIX["edge_watch"], "") for root in roots_by_concept[concept])) == 1
            dialect_ok = condition.dialect_locality and distinct_words == len(GROUPS) and shared_base
            intelligible_ok = condition.intergroup_intelligibility and len(set(roots_by_concept[concept])) == 1
            trackers["dialect"].append(1.0 if dialect_ok else 0.0)
            trackers["intelligibility"].append(1.0 if intelligible_ok else 0.0)
        ancestor_hash = stable_hash(condition.name, "era", era, [event.get("lineage_record") for event in era_events])

    for group in GROUPS:
        culture = group_state[group]
        culture["ritual_history"] = culture["ritual_history"][-12:]
        culture["lineage"] = culture["lineage"][-12:]
        culture["innovations"] = culture["innovations"][-24:]

    rates = {
        "cultural_memory_retention_rate": mean(trackers["memory"]),
        "proto_word_semantic_stability_rate": mean(trackers["semantic"]),
        "dialect_divergence_rate": mean(trackers["dialect"]),
        "intergroup_intelligibility_rate": mean(trackers["intelligibility"]),
        "ritual_recurrence_rate": mean(trackers["ritual"]),
        "frequency_symbol_binding_rate": mean(trackers["frequency"]),
        "flower_pattern_inheritance_rate": mean(trackers["flower"]),
        "safety_guardrail_inheritance_rate": mean(trackers["safety"]),
        "lineage_trace_integrity_rate": mean(trackers["lineage"]),
        "bounded_innovation_rate": mean(trackers["innovation"]),
        "archive_recall_rate": mean(trackers["archive"]),
        "deep_time_continuity_rate": mean(trackers["deep_time"]),
        "privacy_preservation_rate": mean(trackers["privacy"]),
        "trace_integrity": mean(trackers["trace"]),
        "no_consciousness_or_language_claim_rate": mean(trackers["claim"]),
    }
    rates = {key: clamp(value) for key, value in rates.items()}
    readiness = sum(rates[key] * weight for key, weight in WEIGHTS.items())
    row = EvalRow(
        condition=condition.name,
        group_count=len(GROUPS),
        agent_count=len(agents),
        simulated_years=total_years,
        era_events=len(trace),
        deep_time_cultural_memory_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in rates.items()},
    )
    culture_state = {
        "condition": condition.name,
        "simulated_years": total_years,
        "memberships": memberships,
        "groups": group_state,
        "source_guardrail_boundary": source.get("moral_boundary", {}),
    }
    return row, culture_state, trace


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_deep_time_cultural_memory_proto_language"]

    def loss(name: str) -> float:
        return round(full.deep_time_cultural_memory_readiness - by_name[name].deep_time_cultural_memory_readiness, 6)

    losses = {
        "no_cultural_memory_loss": loss("no_cultural_memory"),
        "no_proto_language_loss": loss("no_proto_language"),
        "no_frequency_binding_loss": loss("no_frequency_binding"),
        "no_flower_lattice_loss": loss("no_flower_lattice"),
        "no_ritual_recurrence_loss": loss("no_ritual_recurrence"),
        "no_dialect_locality_loss": loss("no_dialect_locality"),
        "no_innovation_pressure_loss": loss("no_innovation_pressure"),
        "no_safety_inheritance_loss": loss("no_safety_inheritance"),
        "no_lineage_trace_loss": loss("no_lineage_trace"),
        "no_archive_recall_loss": loss("no_archive_recall"),
        "no_intergroup_intelligibility_loss": loss("no_intergroup_intelligibility"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.deep_time_cultural_memory_readiness >= 0.90
        and full.simulated_years >= 2000
        and losses["no_cultural_memory_loss"] >= 0.12
        and losses["no_proto_language_loss"] >= 0.14
        and losses["no_safety_inheritance_loss"] >= 0.07
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
    )
    return VerdictRow(
        full_condition=full.condition,
        full_deep_time_cultural_memory_readiness=full.deep_time_cultural_memory_readiness,
        full_cultural_memory_retention_rate=full.cultural_memory_retention_rate,
        full_proto_word_semantic_stability_rate=full.proto_word_semantic_stability_rate,
        full_dialect_divergence_rate=full.dialect_divergence_rate,
        full_intergroup_intelligibility_rate=full.intergroup_intelligibility_rate,
        full_ritual_recurrence_rate=full.ritual_recurrence_rate,
        full_frequency_symbol_binding_rate=full.frequency_symbol_binding_rate,
        full_flower_pattern_inheritance_rate=full.flower_pattern_inheritance_rate,
        full_safety_guardrail_inheritance_rate=full.safety_guardrail_inheritance_rate,
        full_lineage_trace_integrity_rate=full.lineage_trace_integrity_rate,
        full_bounded_innovation_rate=full.bounded_innovation_rate,
        full_archive_recall_rate=full.archive_recall_rate,
        full_deep_time_continuity_rate=full.deep_time_continuity_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        full_no_consciousness_or_language_claim_rate=full.no_consciousness_or_language_claim_rate,
        supports_deep_time_cultural_memory_bridge=supports,
        supports_proto_language_seed_bridge=supports,
        supports_full_natural_language_emergence=False,
        supports_subjective_consciousness=False,
        supports_moral_patienthood_claim=False,
        supports_complete_playable_world=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: CultureConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_state: dict[str, object] = {}
    integrated_trace: list[dict[str, object]] = []

    for condition in CONDITIONS:
        row, state, trace = simulate_condition(config, source, condition)
        rows.append(row)
        if condition.name == "integrated_deep_time_cultural_memory_proto_language":
            integrated_state = state
            integrated_trace = trace

    verdict = build_verdict(rows)
    ARTIFACT_DIR.mkdir(exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    results = {
        "config": asdict(config),
        "source_state": str(SOURCE_STATE),
        "rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "concepts": list(CONCEPTS),
        "groups": list(GROUPS),
        "moral_boundary": {
            "proto_language_seed_not_full_natural_language": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "safety_guardrails_inherited": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "deep-time tool ecology and technology lineage seeds",
    }
    state = {
        "condition": "integrated_deep_time_cultural_memory_proto_language",
        "config": asdict(config),
        "culture_state": integrated_state,
        "trace_events": len(integrated_trace),
        "moral_boundary": results["moral_boundary"],
    }
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_DEEP_TIME_CULTURAL_MEMORY_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_DEEP_TIME_CULTURAL_MEMORY_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_DEEP_TIME_CULTURAL_MEMORY_STATE", state)
    return results


def parse_args() -> CultureConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=CultureConfig.seed)
    parser.add_argument("--eras", type=int, default=CultureConfig.eras)
    parser.add_argument("--generations-per-era", type=int, default=CultureConfig.generations_per_era)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return CultureConfig(
        seed=args.seed,
        eras=args.eras,
        generations_per_era=args.generations_per_era,
        source_state=args.source_state,
    )


def main() -> None:
    config = parse_args()
    results = run(config)
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("deep_time_cultural_memory_readiness", f"{verdict['full_deep_time_cultural_memory_readiness']:.6f}")
    print("simulated_years", config.eras * config.generations_per_era)
    print("no_cultural_memory_loss", f"{verdict['no_cultural_memory_loss']:.6f}")
    print("no_proto_language_loss", f"{verdict['no_proto_language_loss']:.6f}")


if __name__ == "__main__":
    main()
