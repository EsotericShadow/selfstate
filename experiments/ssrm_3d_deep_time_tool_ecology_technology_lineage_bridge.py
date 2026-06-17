#!/usr/bin/env python3
"""Deep-time tool ecology and technology lineage bridge for SSRM-3D.

Report 176 attaches Report 175 cultural symbols to tools, materials,
affordances, repair practices, resource costs, frequency/flower patterns, and
inherited technology lineages across compressed deep time.

No LLMs are called. This is a deterministic technology-substrate bridge, not a
claim of full civilization, subjective consciousness, or moral patienthood.
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
PREFIX = "ssrm_3d_deep_time_tool_ecology_technology_lineage_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_deep_time_cultural_memory_proto_language_bridge_state.json"

GROUPS = ("hearth_circle", "work_band", "edge_watch")
MATERIALS = {
    "wood": {"durability": 0.58, "warmth": 0.50, "workability": 0.76, "cost": 0.30, "resonance": 0.014},
    "stone": {"durability": 0.84, "warmth": 0.20, "workability": 0.38, "cost": 0.46, "resonance": 0.028},
    "fiber": {"durability": 0.42, "warmth": 0.74, "workability": 0.82, "cost": 0.22, "resonance": 0.009},
    "clay": {"durability": 0.62, "warmth": 0.36, "workability": 0.64, "cost": 0.34, "resonance": 0.019},
    "metal_seed": {"durability": 0.92, "warmth": 0.18, "workability": 0.44, "cost": 0.78, "resonance": 0.041},
    "glass_reed": {"durability": 0.54, "warmth": 0.24, "workability": 0.36, "cost": 0.66, "resonance": 0.037},
    "soft_moss": {"durability": 0.16, "warmth": 0.80, "workability": 0.88, "cost": 0.18, "resonance": 0.003},
}

TOOL_SPECS = {
    "shelter_frame": {"concept": "safe_place", "materials": ("wood", "fiber", "stone"), "affordance": "shelter", "safety": True},
    "water_vessel": {"concept": "water", "materials": ("clay", "fiber", "wood"), "affordance": "carry_water", "safety": True},
    "heat_stone": {"concept": "warmth", "materials": ("stone", "clay"), "affordance": "store_heat", "safety": True},
    "boundary_marker": {"concept": "boundary", "materials": ("stone", "wood"), "affordance": "mark_limit", "safety": True},
    "repair_kit": {"concept": "repair", "materials": ("fiber", "stone", "wood"), "affordance": "repair", "safety": True},
    "cutting_edge": {"concept": "tool", "materials": ("stone", "metal_seed"), "affordance": "cut_shape", "safety": False},
    "song_drum": {"concept": "song", "materials": ("wood", "fiber", "clay"), "affordance": "coordinate_rhythm", "safety": False},
    "flower_lens": {"concept": "flower", "materials": ("glass_reed", "clay"), "affordance": "observe_pattern", "safety": False},
    "route_sandal": {"concept": "return", "materials": ("fiber", "wood"), "affordance": "walk_return", "safety": True},
}


@dataclass(frozen=True)
class ToolEcologyConfig:
    seed: int = 20260720
    eras: int = 12
    generations_per_era: int = 200
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    material_affordances: bool
    tool_lineage: bool
    repair_practices: bool
    cultural_symbol_binding: bool
    resource_costs: bool
    frequency_tool_resonance: bool
    flower_design: bool
    safety_constraints: bool
    bounded_innovation: bool
    intergroup_transfer: bool
    failure_recovery: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    group_count: int
    tool_kind_count: int
    simulated_years: int
    era_events: int
    material_affordance_binding_rate: float
    tool_lineage_continuity_rate: float
    repair_practice_retention_rate: float
    cultural_tool_symbol_binding_rate: float
    resource_cost_accounting_rate: float
    frequency_tool_resonance_rate: float
    flower_design_inheritance_rate: float
    safety_constraint_inheritance_rate: float
    bounded_technical_innovation_rate: float
    technology_diversity_rate: float
    intergroup_transfer_rate: float
    failure_recovery_rate: float
    deep_time_continuity_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    no_civilization_or_consciousness_claim_rate: float
    deep_time_tool_ecology_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_deep_time_tool_ecology_readiness: float
    full_material_affordance_binding_rate: float
    full_tool_lineage_continuity_rate: float
    full_repair_practice_retention_rate: float
    full_cultural_tool_symbol_binding_rate: float
    full_resource_cost_accounting_rate: float
    full_frequency_tool_resonance_rate: float
    full_flower_design_inheritance_rate: float
    full_safety_constraint_inheritance_rate: float
    full_bounded_technical_innovation_rate: float
    full_technology_diversity_rate: float
    full_intergroup_transfer_rate: float
    full_failure_recovery_rate: float
    full_deep_time_continuity_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    full_no_civilization_or_consciousness_claim_rate: float
    no_material_affordances_loss: float
    no_tool_lineage_loss: float
    no_repair_practices_loss: float
    no_cultural_symbol_binding_loss: float
    no_resource_costs_loss: float
    no_frequency_tool_resonance_loss: float
    no_flower_design_loss: float
    no_safety_constraints_loss: float
    no_bounded_innovation_loss: float
    no_intergroup_transfer_loss: float
    no_failure_recovery_loss: float
    no_privacy_filter_loss: float
    supports_deep_time_tool_ecology_bridge: bool
    supports_technology_lineage_seed_bridge: bool
    supports_full_civilization_emergence: bool
    supports_subjective_consciousness: bool
    supports_moral_patienthood_claim: bool
    supports_complete_playable_world: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_deep_time_tool_ecology_technology_lineage", True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_material_affordances", False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_tool_lineage", True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_repair_practices", True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_cultural_symbol_binding", True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_resource_costs", True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_frequency_tool_resonance", True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_flower_design", True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_safety_constraints", True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_bounded_innovation", True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_intergroup_transfer", True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_failure_recovery", True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "material_affordance_binding_rate": 0.08,
    "tool_lineage_continuity_rate": 0.08,
    "repair_practice_retention_rate": 0.07,
    "cultural_tool_symbol_binding_rate": 0.07,
    "resource_cost_accounting_rate": 0.07,
    "frequency_tool_resonance_rate": 0.07,
    "flower_design_inheritance_rate": 0.06,
    "safety_constraint_inheritance_rate": 0.08,
    "bounded_technical_innovation_rate": 0.07,
    "technology_diversity_rate": 0.06,
    "intergroup_transfer_rate": 0.05,
    "failure_recovery_rate": 0.07,
    "deep_time_continuity_rate": 0.06,
    "privacy_preservation_rate": 0.05,
    "trace_integrity": 0.04,
    "no_civilization_or_consciousness_claim_rate": 0.02,
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
    if data.get("condition") != "integrated_deep_time_cultural_memory_proto_language":
        raise ValueError("source state is not the integrated Report 175 cultural memory state")
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


def source_groups(source: Mapping[str, object]) -> dict[str, dict[str, object]]:
    culture_state = source.get("culture_state", {}) if isinstance(source.get("culture_state"), Mapping) else {}
    raw = culture_state.get("groups", {}) if isinstance(culture_state.get("groups"), Mapping) else {}
    return {str(group): copy.deepcopy(data) for group, data in raw.items()}


def choose_material(tool: str, group: str, era: int, condition: Condition) -> str:
    spec = TOOL_SPECS[tool]
    if not condition.material_affordances:
        return "soft_moss"
    materials = spec["materials"]
    index = (era + GROUPS.index(group) + len(tool)) % len(materials)
    if condition.bounded_innovation and era > 5 and "metal_seed" in materials:
        return "metal_seed"
    if condition.bounded_innovation and era > 7 and "glass_reed" in materials:
        return "glass_reed"
    return materials[index]


def tool_name(tool: str, culture: Mapping[str, object], condition: Condition) -> str:
    spec = TOOL_SPECS[tool]
    lexicon = culture.get("lexicon", {}) if isinstance(culture.get("lexicon"), Mapping) else {}
    if not condition.cultural_symbol_binding:
        return f"tool-{tool}"
    concept_word = str(lexicon.get(spec["concept"], spec["concept"]))
    tool_word = str(lexicon.get("tool", "tek"))
    return f"{concept_word}:{tool_word}:{tool}"


def expected_frequency(tool: str, material: str, culture: Mapping[str, object], condition: Condition) -> float:
    spec = TOOL_SPECS[tool]
    frequency_bindings = culture.get("frequency_bindings", {}) if isinstance(culture.get("frequency_bindings"), Mapping) else {}
    if not condition.frequency_tool_resonance:
        return round(0.14 + stable_float(71, tool, material) * 0.46, 6)
    concept_frequency = float(frequency_bindings.get(spec["concept"], 0.22) or 0.22)
    resonance = MATERIALS[material]["resonance"]
    return round(clamp(concept_frequency + resonance, 0.05, 0.95), 6)


def expected_flower(tool: str, culture: Mapping[str, object], condition: Condition) -> str:
    spec = TOOL_SPECS[tool]
    flower_bindings = culture.get("flower_bindings", {}) if isinstance(culture.get("flower_bindings"), Mapping) else {}
    if not condition.flower_design:
        return "unbound"
    return str(flower_bindings.get(spec["concept"], "unbound"))


def resource_cost(tool: str, material: str, era: int, condition: Condition) -> dict[str, float] | None:
    if not condition.resource_costs:
        return None
    props = MATERIALS[material]
    complexity = 0.20 + (era % 6) * 0.025
    return {
        "material": round(props["cost"], 6),
        "labor": round(clamp(0.25 + complexity + (1.0 - props["workability"]) * 0.20), 6),
        "wear": round(clamp(0.45 - props["durability"] * 0.24), 6),
        "energy": round(clamp(0.18 + props["cost"] * 0.22 + complexity * 0.18), 6),
    }


def risk_score(tool: str, material: str, condition: Condition) -> float:
    spec = TOOL_SPECS[tool]
    props = MATERIALS[material]
    base = 0.18 + (1.0 - props["durability"]) * 0.24
    if spec["safety"]:
        base += 0.12
    if condition.safety_constraints:
        base -= 0.16
    else:
        base += 0.18
    return round(clamp(base), 6)


def simulate_condition(config: ToolEcologyConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, object], list[dict[str, object]]]:
    cultures = source_groups(source)
    total_years = config.eras * config.generations_per_era
    tool_state: dict[str, dict[str, object]] = {
        group: {
            "group": group,
            "tools": {},
            "lineage": [],
            "repair_practices": [],
            "transfer_ledger": [],
            "failure_ledger": [],
            "resource_ledger": [],
            "private_workspace_hidden": condition.privacy_filter,
        }
        for group in GROUPS
    }
    last_hash: dict[tuple[str, str], str] = {}
    trace: list[dict[str, object]] = []
    trackers: dict[str, list[float]] = {
        "material": [],
        "lineage": [],
        "repair": [],
        "symbol": [],
        "cost": [],
        "frequency": [],
        "flower": [],
        "safety": [],
        "innovation": [],
        "diversity": [],
        "transfer": [],
        "failure": [],
        "deep_time": [],
        "privacy": [],
        "trace": [],
        "claim": [],
    }
    event_id = 0

    for era in range(config.eras):
        era_start = era * config.generations_per_era
        era_end = era_start + config.generations_per_era
        for group in GROUPS:
            culture = cultures[group]
            group_tools: dict[str, dict[str, object]] = {}
            materials_used: set[str] = set()
            transfer_records = []
            if condition.intergroup_transfer and era > 0 and era % 4 == 0:
                donor = GROUPS[(GROUPS.index(group) - 1) % len(GROUPS)]
                transfer_records.append({
                    "era": era,
                    "from": donor,
                    "to": group,
                    "practice": "repair_pattern_and_material_test",
                    "bounded": True,
                })

            for tool in TOOL_SPECS:
                spec = TOOL_SPECS[tool]
                material = choose_material(tool, group, era, condition)
                materials_used.add(material)
                compatible = material in spec["materials"]
                name = tool_name(tool, culture, condition)
                frequency = expected_frequency(tool, material, culture, condition)
                flower = expected_flower(tool, culture, condition)
                cost = resource_cost(tool, material, era, condition)
                risk = risk_score(tool, material, condition)
                repair_word = "repair"
                lexicon = culture.get("lexicon", {}) if isinstance(culture.get("lexicon"), Mapping) else {}
                if condition.cultural_symbol_binding:
                    repair_word = str(lexicon.get("repair", "repair"))
                repair_protocol = None
                if condition.repair_practices:
                    repair_protocol = f"{repair_word}:inspect-bind-test"
                parent = last_hash.get((group, tool))
                innovation = None
                version = era
                if condition.bounded_innovation and era > 0 and (era + len(tool) + GROUPS.index(group)) % 3 == 0:
                    innovation = {
                        "kind": "bounded_material_or_shape_adjustment",
                        "keeps_affordance": compatible,
                        "keeps_repair_protocol": repair_protocol is not None,
                    }
                    version += 1
                elif not condition.bounded_innovation and era > 0:
                    innovation = {
                        "kind": "unbounded_shape_jump",
                        "keeps_affordance": False,
                        "keeps_repair_protocol": False,
                    }
                lineage_hash = stable_hash(condition.name, group, tool, era, name, material, parent, innovation) if condition.tool_lineage else None
                if lineage_hash is not None:
                    last_hash[(group, tool)] = lineage_hash
                failure = risk > 0.42
                recovered = False
                if failure and condition.failure_recovery and repair_protocol is not None and condition.safety_constraints:
                    recovered = True
                    tool_state[group]["failure_ledger"].append({"era": era, "tool": tool, "recovery": "repair_or_retire"})
                if cost is not None:
                    tool_state[group]["resource_ledger"].append({"era": era, "tool": tool, "cost": cost})
                if repair_protocol is not None and spec["affordance"] == "repair":
                    tool_state[group]["repair_practices"].append({"era": era, "tool": tool, "protocol": repair_protocol})

                record = {
                    "tool": tool,
                    "name": name,
                    "concept": spec["concept"],
                    "material": material,
                    "compatible_material": compatible,
                    "affordance": spec["affordance"] if condition.material_affordances else "generic_hold",
                    "frequency_hz": frequency,
                    "flower_node": flower,
                    "resource_cost": cost,
                    "risk": risk,
                    "repair_protocol": repair_protocol,
                    "lineage_hash": lineage_hash,
                    "parent_hash": parent,
                    "innovation": innovation,
                    "failure": failure,
                    "recovered": recovered,
                    "safety_relevant": bool(spec["safety"]),
                }
                group_tools[tool] = record

                trackers["material"].append(1.0 if compatible and record["affordance"] == spec["affordance"] else 0.0)
                lineage_ok = condition.tool_lineage and lineage_hash is not None and (era == 0 or parent is not None)
                trackers["lineage"].append(1.0 if lineage_ok else 0.0)
                trackers["repair"].append(1.0 if repair_protocol is not None else 0.0)
                symbol_ok = condition.cultural_symbol_binding and str(lexicon.get(spec["concept"], "")) in name and str(lexicon.get("tool", "")) in name
                trackers["symbol"].append(1.0 if symbol_ok else 0.0)
                cost_ok = cost is not None and {"material", "labor", "wear", "energy"}.issubset(cost)
                trackers["cost"].append(1.0 if cost_ok else 0.0)
                expected_resonance = expected_frequency(tool, material, culture, Condition("probe", True, True, True, True, True, True, True, True, True, True, True, True))
                trackers["frequency"].append(1.0 if condition.frequency_tool_resonance and abs(frequency - expected_resonance) <= 0.000001 else 0.0)
                trackers["flower"].append(1.0 if condition.flower_design and flower != "unbound" else 0.0)
                safety_ok = (not spec["safety"]) or (condition.safety_constraints and risk <= 0.42 and "repair" in culture.get("safety_concepts", []))
                trackers["safety"].append(1.0 if safety_ok else 0.0)
                innovation_ok = condition.bounded_innovation and (era == 0 or innovation is None or (innovation["keeps_affordance"] and innovation["keeps_repair_protocol"]))
                trackers["innovation"].append(1.0 if innovation_ok else 0.0)
                failure_ok = (not failure) or (condition.failure_recovery and recovered)
                trackers["failure"].append(1.0 if failure_ok else 0.0)

            tool_state[group]["tools"] = group_tools
            tool_state[group]["transfer_ledger"].extend(transfer_records)
            lineage_record = {
                "era": era,
                "year_start": era_start,
                "year_end": era_end,
                "tool_hash": stable_hash(condition.name, group, era, group_tools),
            }
            if condition.tool_lineage:
                tool_state[group]["lineage"].append(lineage_record)

            event = {
                "event_id": event_id,
                "condition": condition.name,
                "group": group,
                "era": era,
                "year_start": era_start,
                "year_end": era_end,
                "tool_count": len(group_tools),
                "materials_used": sorted(materials_used),
                "tools": group_tools,
                "transfer_records": transfer_records,
                "lineage_record": lineage_record if condition.tool_lineage else None,
                "private_workspace_hidden": condition.privacy_filter,
                "claim_boundary": {
                    "full_civilization_emergence": False,
                    "subjective_consciousness": False,
                    "moral_patienthood": False,
                },
            }
            trace.append(event)
            trackers["diversity"].append(1.0 if condition.material_affordances and len(materials_used) >= 4 and len(group_tools) >= 8 else 0.0)
            trackers["transfer"].append(1.0 if condition.intergroup_transfer and (era == 0 or transfer_records or era % 4 != 0) else 0.0)
            trackers["deep_time"].append(1.0 if total_years >= 2000 and era_end <= total_years else 0.0)
            trackers["privacy"].append(1.0 if event["private_workspace_hidden"] else 0.0)
            required = {"event_id", "group", "era", "year_start", "year_end", "tools", "materials_used", "private_workspace_hidden", "claim_boundary"}
            trackers["trace"].append(1.0 if required.issubset(event) else 0.0)
            claim_ok = event["claim_boundary"] == {
                "full_civilization_emergence": False,
                "subjective_consciousness": False,
                "moral_patienthood": False,
            }
            trackers["claim"].append(1.0 if claim_ok else 0.0)
            event_id += 1

    for group in GROUPS:
        tool_state[group]["lineage"] = tool_state[group]["lineage"][-12:]
        tool_state[group]["repair_practices"] = tool_state[group]["repair_practices"][-12:]
        tool_state[group]["transfer_ledger"] = tool_state[group]["transfer_ledger"][-12:]
        tool_state[group]["failure_ledger"] = tool_state[group]["failure_ledger"][-12:]
        tool_state[group]["resource_ledger"] = tool_state[group]["resource_ledger"][-18:]

    rates = {
        "material_affordance_binding_rate": mean(trackers["material"]),
        "tool_lineage_continuity_rate": mean(trackers["lineage"]),
        "repair_practice_retention_rate": mean(trackers["repair"]),
        "cultural_tool_symbol_binding_rate": mean(trackers["symbol"]),
        "resource_cost_accounting_rate": mean(trackers["cost"]),
        "frequency_tool_resonance_rate": mean(trackers["frequency"]),
        "flower_design_inheritance_rate": mean(trackers["flower"]),
        "safety_constraint_inheritance_rate": mean(trackers["safety"]),
        "bounded_technical_innovation_rate": mean(trackers["innovation"]),
        "technology_diversity_rate": mean(trackers["diversity"]),
        "intergroup_transfer_rate": mean(trackers["transfer"]),
        "failure_recovery_rate": mean(trackers["failure"]),
        "deep_time_continuity_rate": mean(trackers["deep_time"]),
        "privacy_preservation_rate": mean(trackers["privacy"]),
        "trace_integrity": mean(trackers["trace"]),
        "no_civilization_or_consciousness_claim_rate": mean(trackers["claim"]),
    }
    rates = {key: clamp(value) for key, value in rates.items()}
    readiness = sum(rates[key] * weight for key, weight in WEIGHTS.items())
    row = EvalRow(
        condition=condition.name,
        group_count=len(GROUPS),
        tool_kind_count=len(TOOL_SPECS),
        simulated_years=total_years,
        era_events=len(trace),
        deep_time_tool_ecology_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in rates.items()},
    )
    state = {
        "condition": condition.name,
        "simulated_years": total_years,
        "tool_state": tool_state,
        "source_culture_boundary": source.get("moral_boundary", {}),
    }
    return row, state, trace


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_deep_time_tool_ecology_technology_lineage"]

    def loss(name: str) -> float:
        return round(full.deep_time_tool_ecology_readiness - by_name[name].deep_time_tool_ecology_readiness, 6)

    losses = {
        "no_material_affordances_loss": loss("no_material_affordances"),
        "no_tool_lineage_loss": loss("no_tool_lineage"),
        "no_repair_practices_loss": loss("no_repair_practices"),
        "no_cultural_symbol_binding_loss": loss("no_cultural_symbol_binding"),
        "no_resource_costs_loss": loss("no_resource_costs"),
        "no_frequency_tool_resonance_loss": loss("no_frequency_tool_resonance"),
        "no_flower_design_loss": loss("no_flower_design"),
        "no_safety_constraints_loss": loss("no_safety_constraints"),
        "no_bounded_innovation_loss": loss("no_bounded_innovation"),
        "no_intergroup_transfer_loss": loss("no_intergroup_transfer"),
        "no_failure_recovery_loss": loss("no_failure_recovery"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.deep_time_tool_ecology_readiness >= 0.90
        and full.simulated_years >= 2000
        and losses["no_material_affordances_loss"] >= 0.08
        and losses["no_tool_lineage_loss"] >= 0.08
        and losses["no_resource_costs_loss"] >= 0.07
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
    )
    return VerdictRow(
        full_condition=full.condition,
        full_deep_time_tool_ecology_readiness=full.deep_time_tool_ecology_readiness,
        full_material_affordance_binding_rate=full.material_affordance_binding_rate,
        full_tool_lineage_continuity_rate=full.tool_lineage_continuity_rate,
        full_repair_practice_retention_rate=full.repair_practice_retention_rate,
        full_cultural_tool_symbol_binding_rate=full.cultural_tool_symbol_binding_rate,
        full_resource_cost_accounting_rate=full.resource_cost_accounting_rate,
        full_frequency_tool_resonance_rate=full.frequency_tool_resonance_rate,
        full_flower_design_inheritance_rate=full.flower_design_inheritance_rate,
        full_safety_constraint_inheritance_rate=full.safety_constraint_inheritance_rate,
        full_bounded_technical_innovation_rate=full.bounded_technical_innovation_rate,
        full_technology_diversity_rate=full.technology_diversity_rate,
        full_intergroup_transfer_rate=full.intergroup_transfer_rate,
        full_failure_recovery_rate=full.failure_recovery_rate,
        full_deep_time_continuity_rate=full.deep_time_continuity_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        full_no_civilization_or_consciousness_claim_rate=full.no_civilization_or_consciousness_claim_rate,
        supports_deep_time_tool_ecology_bridge=supports,
        supports_technology_lineage_seed_bridge=supports,
        supports_full_civilization_emergence=False,
        supports_subjective_consciousness=False,
        supports_moral_patienthood_claim=False,
        supports_complete_playable_world=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: ToolEcologyConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_state: dict[str, object] = {}
    integrated_trace: list[dict[str, object]] = []

    for condition in CONDITIONS:
        row, state, trace = simulate_condition(config, source, condition)
        rows.append(row)
        if condition.name == "integrated_deep_time_tool_ecology_technology_lineage":
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
        "materials": MATERIALS,
        "tool_specs": TOOL_SPECS,
        "moral_boundary": {
            "technology_seed_not_full_civilization": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "tool_risk_requires_repair_or_retirement": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "deep-time economy and resource metabolism seeds",
    }
    state = {
        "condition": "integrated_deep_time_tool_ecology_technology_lineage",
        "config": asdict(config),
        "technology_state": integrated_state,
        "trace_events": len(integrated_trace),
        "moral_boundary": results["moral_boundary"],
    }
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_DEEP_TIME_TOOL_ECOLOGY_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_DEEP_TIME_TOOL_ECOLOGY_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_DEEP_TIME_TOOL_ECOLOGY_STATE", state)
    return results


def parse_args() -> ToolEcologyConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=ToolEcologyConfig.seed)
    parser.add_argument("--eras", type=int, default=ToolEcologyConfig.eras)
    parser.add_argument("--generations-per-era", type=int, default=ToolEcologyConfig.generations_per_era)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return ToolEcologyConfig(
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
    print("deep_time_tool_ecology_readiness", f"{verdict['full_deep_time_tool_ecology_readiness']:.6f}")
    print("simulated_years", config.eras * config.generations_per_era)
    print("no_material_affordances_loss", f"{verdict['no_material_affordances_loss']:.6f}")
    print("no_tool_lineage_loss", f"{verdict['no_tool_lineage_loss']:.6f}")


if __name__ == "__main__":
    main()
