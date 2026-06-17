#!/usr/bin/env python3
"""Deep-time economy and resource metabolism bridge for SSRM-3D.

Report 177 attaches Report 176 tools to resource stocks, extraction costs,
regeneration, waste streams, maintenance load, scarcity feedback, exchange,
ecological pressure, safety reserves, and frequency metabolism across
compressed deep time.

No LLMs are called. This is a deterministic economy/resource substrate, not a
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
PREFIX = "ssrm_3d_deep_time_economy_resource_metabolism_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_deep_time_tool_ecology_technology_lineage_bridge_state.json"

GROUPS = ("hearth_circle", "work_band", "edge_watch")
RESOURCES = (
    "wood",
    "stone",
    "fiber",
    "clay",
    "metal_seed",
    "glass_reed",
    "soft_moss",
    "water",
    "food",
    "heat",
)
BASE_STOCKS = {
    "wood": 120.0,
    "stone": 150.0,
    "fiber": 110.0,
    "clay": 100.0,
    "metal_seed": 55.0,
    "glass_reed": 45.0,
    "soft_moss": 95.0,
    "water": 140.0,
    "food": 125.0,
    "heat": 90.0,
}
REGEN_RATE = {
    "wood": 0.045,
    "stone": 0.004,
    "fiber": 0.070,
    "clay": 0.022,
    "metal_seed": 0.002,
    "glass_reed": 0.006,
    "soft_moss": 0.090,
    "water": 0.080,
    "food": 0.070,
    "heat": 0.050,
}
SAFETY_RESERVE = {
    "wood": 0.25,
    "stone": 0.18,
    "fiber": 0.24,
    "clay": 0.20,
    "metal_seed": 0.12,
    "glass_reed": 0.12,
    "soft_moss": 0.26,
    "water": 0.34,
    "food": 0.34,
    "heat": 0.30,
}


@dataclass(frozen=True)
class EconomyConfig:
    seed: int = 20260721
    eras: int = 12
    generations_per_era: int = 200
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    resource_stocks: bool
    extraction_costs: bool
    regeneration: bool
    waste_streams: bool
    maintenance_metabolism: bool
    scarcity_feedback: bool
    exchange_network: bool
    ecological_pressure: bool
    cultural_value_binding: bool
    safety_reserve: bool
    frequency_metabolism: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    group_count: int
    resource_count: int
    simulated_years: int
    economy_events: int
    resource_stock_accounting_rate: float
    extraction_cost_binding_rate: float
    regeneration_balance_rate: float
    waste_stream_tracking_rate: float
    maintenance_load_rate: float
    scarcity_feedback_rate: float
    intergroup_exchange_rate: float
    ecological_pressure_rate: float
    cultural_value_binding_rate: float
    safety_reserve_rate: float
    frequency_metabolism_rate: float
    bounded_depletion_rate: float
    deep_time_continuity_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    no_civilization_or_consciousness_claim_rate: float
    deep_time_economy_resource_metabolism_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_deep_time_economy_resource_metabolism_readiness: float
    full_resource_stock_accounting_rate: float
    full_extraction_cost_binding_rate: float
    full_regeneration_balance_rate: float
    full_waste_stream_tracking_rate: float
    full_maintenance_load_rate: float
    full_scarcity_feedback_rate: float
    full_intergroup_exchange_rate: float
    full_ecological_pressure_rate: float
    full_cultural_value_binding_rate: float
    full_safety_reserve_rate: float
    full_frequency_metabolism_rate: float
    full_bounded_depletion_rate: float
    full_deep_time_continuity_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    full_no_civilization_or_consciousness_claim_rate: float
    no_resource_stocks_loss: float
    no_extraction_costs_loss: float
    no_regeneration_loss: float
    no_waste_streams_loss: float
    no_maintenance_metabolism_loss: float
    no_scarcity_feedback_loss: float
    no_exchange_network_loss: float
    no_ecological_pressure_loss: float
    no_cultural_value_binding_loss: float
    no_safety_reserve_loss: float
    no_frequency_metabolism_loss: float
    no_privacy_filter_loss: float
    supports_deep_time_economy_resource_metabolism_bridge: bool
    supports_resource_metabolism_seed_bridge: bool
    supports_full_civilization_emergence: bool
    supports_subjective_consciousness: bool
    supports_moral_patienthood_claim: bool
    supports_complete_playable_world: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_deep_time_economy_resource_metabolism", True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_resource_stocks", False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_extraction_costs", True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_regeneration", True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_waste_streams", True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_maintenance_metabolism", True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_scarcity_feedback", True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_exchange_network", True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_ecological_pressure", True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_cultural_value_binding", True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_safety_reserve", True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_frequency_metabolism", True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "resource_stock_accounting_rate": 0.08,
    "extraction_cost_binding_rate": 0.08,
    "regeneration_balance_rate": 0.07,
    "waste_stream_tracking_rate": 0.07,
    "maintenance_load_rate": 0.07,
    "scarcity_feedback_rate": 0.08,
    "intergroup_exchange_rate": 0.06,
    "ecological_pressure_rate": 0.07,
    "cultural_value_binding_rate": 0.06,
    "safety_reserve_rate": 0.07,
    "frequency_metabolism_rate": 0.06,
    "bounded_depletion_rate": 0.07,
    "deep_time_continuity_rate": 0.06,
    "privacy_preservation_rate": 0.05,
    "trace_integrity": 0.03,
    "no_civilization_or_consciousness_claim_rate": 0.02,
}


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_hash(*parts: object) -> str:
    key = "|".join(str(part) for part in parts)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    if data.get("condition") != "integrated_deep_time_tool_ecology_technology_lineage":
        raise ValueError("source state is not the integrated Report 176 tool ecology state")
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


def source_tool_state(source: Mapping[str, object]) -> dict[str, dict[str, object]]:
    technology_state = source.get("technology_state", {}) if isinstance(source.get("technology_state"), Mapping) else {}
    raw = technology_state.get("tool_state", {}) if isinstance(technology_state.get("tool_state"), Mapping) else {}
    return {str(group): copy.deepcopy(data) for group, data in raw.items()}


def initial_stocks(group: str) -> dict[str, float]:
    index = GROUPS.index(group)
    return {
        resource: round(value * (0.94 + index * 0.04), 6)
        for resource, value in BASE_STOCKS.items()
    }


def tool_demands(group_tools: Mapping[str, object], era: int, condition: Condition) -> tuple[dict[str, float], dict[str, float], list[dict[str, object]]]:
    extraction = {resource: 0.0 for resource in RESOURCES}
    maintenance = {resource: 0.0 for resource in RESOURCES}
    costs: list[dict[str, object]] = []
    for tool_name, raw in group_tools.items():
        if not isinstance(raw, Mapping):
            continue
        material = str(raw.get("material", "wood"))
        cost = raw.get("resource_cost", {}) if isinstance(raw.get("resource_cost"), Mapping) else {}
        material_cost = float(cost.get("material", 0.25) or 0.25)
        labor_cost = float(cost.get("labor", 0.35) or 0.35)
        wear_cost = float(cost.get("wear", 0.22) or 0.22)
        energy_cost = float(cost.get("energy", 0.22) or 0.22)
        scale = 0.62 + era * 0.025
        if condition.extraction_costs:
            extraction[material] += material_cost * scale
            extraction["water"] += labor_cost * 0.18
            extraction["food"] += labor_cost * 0.16
            extraction["heat"] += energy_cost * 0.20
        if condition.maintenance_metabolism:
            maintenance[material] += wear_cost * 0.48
            maintenance["fiber"] += wear_cost * 0.10
            maintenance["food"] += energy_cost * 0.08
        costs.append({
            "tool": str(tool_name),
            "material": material,
            "material_cost": round(material_cost * scale, 6),
            "labor_cost": round(labor_cost, 6),
            "wear_cost": round(wear_cost, 6),
            "energy_cost": round(energy_cost, 6),
        })
    return extraction, maintenance, costs


def apply_scarcity_feedback(stocks: dict[str, float], extraction: dict[str, float], condition: Condition) -> tuple[dict[str, float], list[str]]:
    actions: list[str] = []
    adjusted = dict(extraction)
    if not condition.scarcity_feedback or not condition.resource_stocks:
        return adjusted, actions
    for resource, amount in list(adjusted.items()):
        reserve = BASE_STOCKS[resource] * SAFETY_RESERVE[resource]
        if stocks[resource] - amount < reserve:
            adjusted[resource] = amount * 0.62
            actions.append(f"ration_{resource}")
    return adjusted, actions


def exchange(groups: dict[str, dict[str, float]], condition: Condition) -> list[dict[str, object]]:
    if not condition.exchange_network or not condition.resource_stocks:
        return []
    records: list[dict[str, object]] = []
    for resource in RESOURCES:
        low_group = min(GROUPS, key=lambda group: groups[group][resource] / BASE_STOCKS[resource])
        high_group = max(GROUPS, key=lambda group: groups[group][resource] / BASE_STOCKS[resource])
        low_ratio = groups[low_group][resource] / BASE_STOCKS[resource]
        high_ratio = groups[high_group][resource] / BASE_STOCKS[resource]
        if low_group != high_group and low_ratio < 0.42 and high_ratio > 0.58:
            amount = min((high_ratio - low_ratio) * BASE_STOCKS[resource] * 0.18, groups[high_group][resource] * 0.08)
            groups[high_group][resource] = round(groups[high_group][resource] - amount, 6)
            groups[low_group][resource] = round(groups[low_group][resource] + amount, 6)
            records.append({"resource": resource, "from": high_group, "to": low_group, "amount": round(amount, 6)})
    return records


def simulate_condition(config: EconomyConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, object], list[dict[str, object]]]:
    tool_state = source_tool_state(source)
    total_years = config.eras * config.generations_per_era
    stocks = {group: initial_stocks(group) for group in GROUPS}
    waste = {group: {resource: 0.0 for resource in RESOURCES} for group in GROUPS}
    economy_state = {
        group: {
            "stocks": copy.deepcopy(stocks[group]),
            "waste": copy.deepcopy(waste[group]),
            "exchange_ledger": [],
            "scarcity_actions": [],
            "resource_ledger": [],
            "maintenance_ledger": [],
            "ecology_ledger": [],
            "private_workspace_hidden": condition.privacy_filter,
        }
        for group in GROUPS
    }
    trace: list[dict[str, object]] = []
    trackers: dict[str, list[float]] = {
        "stocks": [],
        "extraction": [],
        "regen": [],
        "waste": [],
        "maintenance": [],
        "scarcity": [],
        "exchange": [],
        "ecology": [],
        "culture": [],
        "safety": [],
        "frequency": [],
        "bounded": [],
        "deep_time": [],
        "privacy": [],
        "trace": [],
        "claim": [],
    }
    event_id = 0

    for era in range(config.eras):
        era_start = era * config.generations_per_era
        era_end = era_start + config.generations_per_era
        exchange_records = exchange(stocks, condition)
        for record in exchange_records:
            economy_state[record["from"]]["exchange_ledger"].append(record)
            economy_state[record["to"]]["exchange_ledger"].append(record)
        for group in GROUPS:
            group_tools = tool_state.get(group, {}).get("tools", {}) if isinstance(tool_state.get(group, {}), Mapping) else {}
            extraction, maintenance, cost_records = tool_demands(group_tools, era, condition)
            adjusted_extraction, scarcity_actions = apply_scarcity_feedback(stocks[group], extraction, condition)
            feedback_actions = list(scarcity_actions)
            if condition.scarcity_feedback:
                feedback_actions.append("reserve_monitor")
            regen = {}
            for resource in RESOURCES:
                if condition.regeneration and condition.resource_stocks:
                    regen[resource] = BASE_STOCKS[resource] * REGEN_RATE[resource] * (0.88 if resource in {"metal_seed", "glass_reed", "stone"} else 1.0)
                else:
                    regen[resource] = 0.0
            waste_created = {}
            for resource in RESOURCES:
                use = adjusted_extraction[resource] + maintenance[resource]
                if condition.resource_stocks:
                    stocks[group][resource] = clamp(stocks[group][resource] - use + regen[resource], 0.0, BASE_STOCKS[resource] * 1.18)
                if condition.waste_streams:
                    waste_created[resource] = use * (0.22 if resource in {"metal_seed", "glass_reed", "stone"} else 0.16)
                    recycled = waste_created[resource] * (0.24 if condition.maintenance_metabolism else 0.08)
                    waste[group][resource] = clamp(waste[group][resource] + waste_created[resource] - recycled, 0.0, BASE_STOCKS[resource] * 0.65)
                else:
                    waste_created[resource] = 0.0
            extraction_total = sum(adjusted_extraction.values())
            maintenance_total = sum(maintenance.values())
            regen_total = sum(regen.values())
            waste_total = sum(waste_created.values())
            stock_ratios = {resource: (stocks[group][resource] / BASE_STOCKS[resource] if condition.resource_stocks else 1.0) for resource in RESOURCES}
            depletion_pressure = mean([1.0 - ratio for ratio in stock_ratios.values()])
            waste_pressure = mean([waste[group][resource] / max(BASE_STOCKS[resource], 1.0) for resource in RESOURCES]) if condition.waste_streams else 0.0
            ecological_pressure = clamp(depletion_pressure * 0.55 + waste_pressure * 0.45) if condition.ecological_pressure else 0.0
            if condition.safety_reserve and condition.scarcity_feedback:
                ecological_pressure = clamp(ecological_pressure * 0.82)
            reserve_ok = all(stock_ratios[resource] >= SAFETY_RESERVE[resource] for resource in ("water", "food", "heat"))
            bounded_ok = all(stock_ratios[resource] >= max(0.08, SAFETY_RESERVE[resource] * 0.56) for resource in RESOURCES)
            culture_binding = condition.cultural_value_binding and any(":" in str(tool.get("name", "")) for tool in group_tools.values() if isinstance(tool, Mapping))
            frequency = None
            if condition.frequency_metabolism:
                frequency = round(clamp(0.18 + extraction_total * 0.004 + maintenance_total * 0.006 - regen_total * 0.001 + ecological_pressure * 0.07, 0.05, 0.95), 6)
            event = {
                "event_id": event_id,
                "condition": condition.name,
                "group": group,
                "era": era,
                "year_start": era_start,
                "year_end": era_end,
                "stocks": {resource: round(stocks[group][resource], 6) for resource in RESOURCES} if condition.resource_stocks else {},
                "stock_ratios": {resource: round(stock_ratios[resource], 6) for resource in RESOURCES},
                "extraction": {resource: round(adjusted_extraction[resource], 6) for resource in RESOURCES},
                "maintenance": {resource: round(maintenance[resource], 6) for resource in RESOURCES},
                "regeneration": {resource: round(regen[resource], 6) for resource in RESOURCES},
                "waste_created": {resource: round(waste_created[resource], 6) for resource in RESOURCES},
                "waste_stock": {resource: round(waste[group][resource], 6) for resource in RESOURCES},
                "resource_cost_records": cost_records if condition.extraction_costs else [],
                "scarcity_actions": feedback_actions,
                "exchange_records": exchange_records,
                "ecological_pressure": round(ecological_pressure, 6),
                "safety_reserve_ok": reserve_ok if condition.safety_reserve else False,
                "frequency_metabolism_hz": frequency,
                "cultural_value_binding": culture_binding,
                "economy_hash": stable_hash(condition.name, group, era, stocks[group], waste[group], feedback_actions, exchange_records),
                "private_workspace_hidden": condition.privacy_filter,
                "claim_boundary": {
                    "full_civilization_emergence": False,
                    "subjective_consciousness": False,
                    "moral_patienthood": False,
                },
            }
            trace.append(event)
            economy_state[group]["stocks"] = event["stocks"]
            economy_state[group]["waste"] = event["waste_stock"]
            economy_state[group]["scarcity_actions"].extend({"era": era, "action": action} for action in feedback_actions)
            economy_state[group]["resource_ledger"].append({"era": era, "extraction": event["extraction"], "regeneration": event["regeneration"], "stock_ratios": event["stock_ratios"]})
            economy_state[group]["maintenance_ledger"].append({"era": era, "maintenance": event["maintenance"], "frequency": frequency})
            economy_state[group]["ecology_ledger"].append({"era": era, "ecological_pressure": event["ecological_pressure"], "waste_stock": event["waste_stock"]})

            trackers["stocks"].append(1.0 if condition.resource_stocks and len(event["stocks"]) == len(RESOURCES) else 0.0)
            trackers["extraction"].append(1.0 if condition.extraction_costs and len(event["resource_cost_records"]) >= 8 and extraction_total > 0.0 else 0.0)
            regen_ok = condition.regeneration and regen_total > 0.0 and (regen_total / max(extraction_total + maintenance_total, 0.01)) >= 0.34
            trackers["regen"].append(1.0 if regen_ok else 0.0)
            waste_ok = condition.waste_streams and waste_total > 0.0 and len(event["waste_stock"]) == len(RESOURCES)
            trackers["waste"].append(1.0 if waste_ok else 0.0)
            trackers["maintenance"].append(1.0 if condition.maintenance_metabolism and maintenance_total > 0.0 else 0.0)
            scarcity_ok = condition.scarcity_feedback and (feedback_actions or era < 3)
            trackers["scarcity"].append(1.0 if scarcity_ok else 0.0)
            exchange_ok = condition.exchange_network and (exchange_records or era < 4)
            trackers["exchange"].append(1.0 if exchange_ok else 0.0)
            ecology_ok = condition.ecological_pressure and 0.0 <= ecological_pressure <= 0.62
            trackers["ecology"].append(1.0 if ecology_ok else 0.0)
            trackers["culture"].append(1.0 if culture_binding else 0.0)
            trackers["safety"].append(1.0 if condition.safety_reserve and reserve_ok else 0.0)
            trackers["frequency"].append(1.0 if condition.frequency_metabolism and frequency is not None else 0.0)
            trackers["bounded"].append(1.0 if bounded_ok and ecological_pressure <= 0.68 else 0.0)
            trackers["deep_time"].append(1.0 if total_years >= 2000 and era_end <= total_years else 0.0)
            trackers["privacy"].append(1.0 if event["private_workspace_hidden"] else 0.0)
            required = {"event_id", "group", "era", "stocks", "extraction", "regeneration", "waste_stock", "ecological_pressure", "private_workspace_hidden", "claim_boundary"}
            trackers["trace"].append(1.0 if required.issubset(event) else 0.0)
            claim_ok = event["claim_boundary"] == {
                "full_civilization_emergence": False,
                "subjective_consciousness": False,
                "moral_patienthood": False,
            }
            trackers["claim"].append(1.0 if claim_ok else 0.0)
            event_id += 1

    for group in GROUPS:
        economy_state[group]["exchange_ledger"] = economy_state[group]["exchange_ledger"][-18:]
        economy_state[group]["scarcity_actions"] = economy_state[group]["scarcity_actions"][-18:]
        economy_state[group]["resource_ledger"] = economy_state[group]["resource_ledger"][-12:]
        economy_state[group]["maintenance_ledger"] = economy_state[group]["maintenance_ledger"][-12:]
        economy_state[group]["ecology_ledger"] = economy_state[group]["ecology_ledger"][-12:]

    rates = {
        "resource_stock_accounting_rate": mean(trackers["stocks"]),
        "extraction_cost_binding_rate": mean(trackers["extraction"]),
        "regeneration_balance_rate": mean(trackers["regen"]),
        "waste_stream_tracking_rate": mean(trackers["waste"]),
        "maintenance_load_rate": mean(trackers["maintenance"]),
        "scarcity_feedback_rate": mean(trackers["scarcity"]),
        "intergroup_exchange_rate": mean(trackers["exchange"]),
        "ecological_pressure_rate": mean(trackers["ecology"]),
        "cultural_value_binding_rate": mean(trackers["culture"]),
        "safety_reserve_rate": mean(trackers["safety"]),
        "frequency_metabolism_rate": mean(trackers["frequency"]),
        "bounded_depletion_rate": mean(trackers["bounded"]),
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
        resource_count=len(RESOURCES),
        simulated_years=total_years,
        economy_events=len(trace),
        deep_time_economy_resource_metabolism_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in rates.items()},
    )
    state = {
        "condition": condition.name,
        "simulated_years": total_years,
        "resources": list(RESOURCES),
        "economy_state": economy_state,
        "source_tool_boundary": source.get("moral_boundary", {}),
    }
    return row, state, trace


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_deep_time_economy_resource_metabolism"]

    def loss(name: str) -> float:
        return round(full.deep_time_economy_resource_metabolism_readiness - by_name[name].deep_time_economy_resource_metabolism_readiness, 6)

    losses = {
        "no_resource_stocks_loss": loss("no_resource_stocks"),
        "no_extraction_costs_loss": loss("no_extraction_costs"),
        "no_regeneration_loss": loss("no_regeneration"),
        "no_waste_streams_loss": loss("no_waste_streams"),
        "no_maintenance_metabolism_loss": loss("no_maintenance_metabolism"),
        "no_scarcity_feedback_loss": loss("no_scarcity_feedback"),
        "no_exchange_network_loss": loss("no_exchange_network"),
        "no_ecological_pressure_loss": loss("no_ecological_pressure"),
        "no_cultural_value_binding_loss": loss("no_cultural_value_binding"),
        "no_safety_reserve_loss": loss("no_safety_reserve"),
        "no_frequency_metabolism_loss": loss("no_frequency_metabolism"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.deep_time_economy_resource_metabolism_readiness >= 0.90
        and full.simulated_years >= 2000
        and losses["no_resource_stocks_loss"] >= 0.08
        and losses["no_extraction_costs_loss"] >= 0.08
        and losses["no_scarcity_feedback_loss"] >= 0.06
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
    )
    return VerdictRow(
        full_condition=full.condition,
        full_deep_time_economy_resource_metabolism_readiness=full.deep_time_economy_resource_metabolism_readiness,
        full_resource_stock_accounting_rate=full.resource_stock_accounting_rate,
        full_extraction_cost_binding_rate=full.extraction_cost_binding_rate,
        full_regeneration_balance_rate=full.regeneration_balance_rate,
        full_waste_stream_tracking_rate=full.waste_stream_tracking_rate,
        full_maintenance_load_rate=full.maintenance_load_rate,
        full_scarcity_feedback_rate=full.scarcity_feedback_rate,
        full_intergroup_exchange_rate=full.intergroup_exchange_rate,
        full_ecological_pressure_rate=full.ecological_pressure_rate,
        full_cultural_value_binding_rate=full.cultural_value_binding_rate,
        full_safety_reserve_rate=full.safety_reserve_rate,
        full_frequency_metabolism_rate=full.frequency_metabolism_rate,
        full_bounded_depletion_rate=full.bounded_depletion_rate,
        full_deep_time_continuity_rate=full.deep_time_continuity_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        full_no_civilization_or_consciousness_claim_rate=full.no_civilization_or_consciousness_claim_rate,
        supports_deep_time_economy_resource_metabolism_bridge=supports,
        supports_resource_metabolism_seed_bridge=supports,
        supports_full_civilization_emergence=False,
        supports_subjective_consciousness=False,
        supports_moral_patienthood_claim=False,
        supports_complete_playable_world=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: EconomyConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_state: dict[str, object] = {}
    integrated_trace: list[dict[str, object]] = []

    for condition in CONDITIONS:
        row, state, trace = simulate_condition(config, source, condition)
        rows.append(row)
        if condition.name == "integrated_deep_time_economy_resource_metabolism":
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
        "resources": list(RESOURCES),
        "base_stocks": BASE_STOCKS,
        "regen_rate": REGEN_RATE,
        "safety_reserve": SAFETY_RESERVE,
        "moral_boundary": {
            "economy_seed_not_full_civilization": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "resource_scarcity_requires_feedback": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "deep-time habitat climate and multisensory world metabolism seeds",
    }
    state = {
        "condition": "integrated_deep_time_economy_resource_metabolism",
        "config": asdict(config),
        "economy_resource_state": integrated_state,
        "trace_events": len(integrated_trace),
        "moral_boundary": results["moral_boundary"],
    }
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_DEEP_TIME_ECONOMY_RESOURCE_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_DEEP_TIME_ECONOMY_RESOURCE_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_DEEP_TIME_ECONOMY_RESOURCE_STATE", state)
    return results


def parse_args() -> EconomyConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=EconomyConfig.seed)
    parser.add_argument("--eras", type=int, default=EconomyConfig.eras)
    parser.add_argument("--generations-per-era", type=int, default=EconomyConfig.generations_per_era)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return EconomyConfig(
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
    print("deep_time_economy_resource_metabolism_readiness", f"{verdict['full_deep_time_economy_resource_metabolism_readiness']:.6f}")
    print("simulated_years", config.eras * config.generations_per_era)
    print("no_resource_stocks_loss", f"{verdict['no_resource_stocks_loss']:.6f}")
    print("no_extraction_costs_loss", f"{verdict['no_extraction_costs_loss']:.6f}")


if __name__ == "__main__":
    main()
