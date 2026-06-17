#!/usr/bin/env python3
"""Multi-agent project economy with scarcity, negotiation, and tool chains.

Report 185 consumes the Report 184 planning state and adds a deterministic local
economy layer: scarce resources, tool-chain recipes, negotiation packets,
exchange ledgers, fair allocation, repair/reuse substitutions, route-cost
accounting, trust-price modulation, durable project outputs, and browser replay.

No LLMs are called. This is deterministic economy substrate, not a claim of
complete gameplay, subjective consciousness, moral patienthood, natural language
emergence, or free will.
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
PREFIX = "ssrm_3d_project_economy_resource_negotiation_toolchain_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_agent_local_planning_interruptions_cooperation_bridge_state.json"

RESOURCE_SPECS = {
    "clay_mass": {"stock": 1, "scarcity": "hard", "place": "clay_basin", "base_price": 0.38, "frequency_hz": 0.241, "flower_node": "work_petal"},
    "repair_fiber": {"stock": 1, "scarcity": "hard", "place": "reed_wetland", "base_price": 0.34, "frequency_hz": 0.229, "flower_node": "return_petal"},
    "reed_bundle": {"stock": 1, "scarcity": "critical", "place": "reed_wetland", "base_price": 0.42, "frequency_hz": 0.233, "flower_node": "social_petal"},
    "dry_moss": {"stock": 2, "scarcity": "limited", "place": "moss_hollow", "base_price": 0.31, "frequency_hz": 0.218, "flower_node": "root_rest"},
    "ember_heat": {"stock": 2, "scarcity": "limited", "place": "hearth_vale", "base_price": 0.36, "frequency_hz": 0.214, "flower_node": "dawn_breath"},
    "glass_shard": {"stock": 1, "scarcity": "critical", "place": "glass_mire", "base_price": 0.46, "frequency_hz": 0.267, "flower_node": "explore_petal"},
    "signal_charge": {"stock": 1, "scarcity": "hard", "place": "stone_ridge", "base_price": 0.40, "frequency_hz": 0.258, "flower_node": "social_petal"},
}

REUSE_SUBSTITUTES = {
    "reed_bundle": "reed_offcut",
    "glass_shard": "glass_reading",
}

PROJECTS = {
    "Ari": {
        "project_id": "durable_clay_latch",
        "output_id": "hearth_latch_repaired",
        "home": "hearth_vale",
        "stages": (
            {"stage": "prepare_patch", "resources": ("clay_mass", "repair_fiber"), "tool": "clay_patch_kit", "place": "clay_basin"},
            {"stage": "dry_patch", "resources": ("ember_heat", "dry_moss"), "tool": "dry_cloak", "place": "hearth_vale"},
            {"stage": "align_latch", "resources": ("glass_shard",), "tool": "glass_lens", "place": "clay_basin"},
        ),
    },
    "Fay": {
        "project_id": "insulated_moss_bedding",
        "output_id": "dry_bedding_ready",
        "home": "moss_hollow",
        "stages": (
            {"stage": "weave_bedding", "resources": ("reed_bundle", "dry_moss"), "tool": "dry_cloak", "place": "moss_hollow", "creates_reuse": "reed_offcut"},
            {"stage": "warm_bedding", "resources": ("ember_heat",), "tool": "ember_blanket", "place": "moss_hollow"},
            {"stage": "share_water_care", "resources": (), "tool": "reed_cup", "place": "moss_hollow"},
        ),
    },
    "Milo": {
        "project_id": "ridge_signal_array",
        "output_id": "route_warning_signal_ready",
        "home": "stone_ridge",
        "stages": (
            {"stage": "inspect_ridge", "resources": ("glass_shard",), "tool": "glass_lens", "place": "glass_mire", "creates_reuse": "glass_reading"},
            {"stage": "charge_signal", "resources": ("signal_charge",), "tool": "signal_shell", "place": "stone_ridge"},
            {"stage": "mount_signal", "resources": ("reed_bundle",), "tool": "signal_shell", "place": "stone_ridge"},
        ),
    },
}

SCHEDULE = (
    ("Fay", 0),
    ("Ari", 0),
    ("Milo", 0),
    ("Fay", 1),
    ("Milo", 1),
    ("Ari", 1),
    ("Milo", 2),
    ("Ari", 2),
    ("Fay", 2),
)

WEIGHTS = {
    "resource_scarcity_binding_rate": 0.10,
    "tool_chain_completion_rate": 0.10,
    "negotiation_resolution_rate": 0.10,
    "exchange_ledger_integrity_rate": 0.09,
    "fair_allocation_rate": 0.08,
    "repair_reuse_rate": 0.07,
    "route_cost_accounting_rate": 0.07,
    "trust_price_modulation_rate": 0.07,
    "project_output_rate": 0.10,
    "resource_conservation_rate": 0.08,
    "frequency_flower_economy_binding_rate": 0.06,
    "browser_economy_replay_rate": 0.04,
    "privacy_preservation_rate": 0.02,
    "trace_integrity": 0.02,
}


@dataclass(frozen=True)
class EconomyConfig:
    seed: int = 20260729
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    resource_scarcity: bool
    tool_chains: bool
    negotiation: bool
    exchange_ledger: bool
    fair_allocation: bool
    repair_reuse: bool
    route_cost_accounting: bool
    trust_price_modulation: bool
    project_outputs: bool
    frequency_flower_binding: bool
    replay_timeline: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    object_count: int
    resource_count: int
    project_count: int
    economy_events: int
    resource_scarcity_binding_rate: float
    tool_chain_completion_rate: float
    negotiation_resolution_rate: float
    exchange_ledger_integrity_rate: float
    fair_allocation_rate: float
    repair_reuse_rate: float
    route_cost_accounting_rate: float
    trust_price_modulation_rate: float
    project_output_rate: float
    resource_conservation_rate: float
    frequency_flower_economy_binding_rate: float
    browser_economy_replay_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    project_economy_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_project_economy_readiness: float
    full_resource_scarcity_binding_rate: float
    full_tool_chain_completion_rate: float
    full_negotiation_resolution_rate: float
    full_exchange_ledger_integrity_rate: float
    full_fair_allocation_rate: float
    full_repair_reuse_rate: float
    full_route_cost_accounting_rate: float
    full_trust_price_modulation_rate: float
    full_project_output_rate: float
    full_resource_conservation_rate: float
    full_frequency_flower_economy_binding_rate: float
    full_browser_economy_replay_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    no_resource_scarcity_loss: float
    no_tool_chains_loss: float
    no_negotiation_loss: float
    no_exchange_ledger_loss: float
    no_fair_allocation_loss: float
    no_repair_reuse_loss: float
    no_route_cost_accounting_loss: float
    no_trust_price_modulation_loss: float
    no_project_outputs_loss: float
    no_frequency_flower_economy_binding_loss: float
    no_replay_timeline_loss: float
    no_privacy_filter_loss: float
    supports_project_economy_resource_negotiation_toolchain_bridge: bool
    supports_multi_agent_project_economy_seed: bool
    supports_complete_3d_world: bool
    supports_complete_playable_world: bool
    supports_subjective_consciousness: bool
    supports_moral_patienthood_claim: bool
    supports_natural_language_emergence: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_project_economy_resource_negotiation_toolchain", True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_resource_scarcity", False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_tool_chains", True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_negotiation", True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_exchange_ledger", True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_fair_allocation", True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_repair_reuse", True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_route_cost_accounting", True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_trust_price_modulation", True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_project_outputs", True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_frequency_flower_economy_binding", True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_replay_timeline", True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_hash(*parts: object) -> str:
    key = "|".join(json.dumps(part, sort_keys=True) if isinstance(part, (dict, list, tuple)) else str(part) for part in parts)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


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


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    if data.get("condition") != "integrated_agent_local_planning_interruptions_cooperation":
        raise ValueError("source state is not the integrated Report 184 planning state")
    return data


def source_payload(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], list[dict[str, object]], dict[str, dict[str, object]], dict[str, dict[str, object]]]:
    state = source.get("planning_state", {}) if isinstance(source.get("planning_state"), Mapping) else {}
    places = state.get("places", {}) if isinstance(state.get("places"), Mapping) else {}
    routes = state.get("routes", []) if isinstance(state.get("routes"), list) else []
    agents = state.get("agents", {}) if isinstance(state.get("agents"), Mapping) else {}
    objects = state.get("objects", {}) if isinstance(state.get("objects"), Mapping) else {}
    return (
        {str(name): copy.deepcopy(data) for name, data in places.items()},
        [copy.deepcopy(route) for route in routes],
        {str(name): copy.deepcopy(data) for name, data in agents.items()},
        {str(name): copy.deepcopy(data) for name, data in objects.items()},
    )


def init_resources(condition: Condition) -> dict[str, dict[str, object]]:
    resources = copy.deepcopy(RESOURCE_SPECS)
    for name, item in resources.items():
        item["resource_id"] = name
        item["initial_stock"] = item["stock"] if condition.resource_scarcity else 99
        item["stock"] = item["initial_stock"]
        item["consumed"] = 0
        item["produced_by_reuse"] = 0
        item["scarce"] = condition.resource_scarcity and item["scarcity"] in {"critical", "hard", "limited"}
    return resources


def route_cost(routes: Sequence[Mapping[str, object]], start: str, end: str, condition: Condition) -> float | None:
    if not condition.route_cost_accounting:
        return None
    if start == end:
        return 0.0
    candidates = [route for route in routes if {route.get("from"), route.get("to")} == {start, end}]
    if candidates:
        return round(float(candidates[0].get("route_cost", 0.25)), 6)
    return round(0.18 + abs(len(start) - len(end)) * 0.011, 6)


def agent_trust(agent: Mapping[str, object]) -> float:
    relation = agent.get("relationship", {}) if isinstance(agent.get("relationship"), Mapping) else {}
    return clamp(float(relation.get("trust_in_avatar", 0.55)) - float(relation.get("wariness", 0.25)) * 0.25)


def allocate_resource(resource_id: str, resources: dict[str, dict[str, object]], condition: Condition) -> tuple[bool, str, dict[str, object] | None]:
    resource = resources.get(resource_id)
    if resource and int(resource.get("stock", 0)) > 0:
        resource["stock"] = int(resource["stock"]) - 1
        resource["consumed"] = int(resource.get("consumed", 0)) + 1
        return True, resource_id, copy.deepcopy(resource)
    substitute = REUSE_SUBSTITUTES.get(resource_id)
    if condition.repair_reuse and substitute and substitute in resources and int(resources[substitute].get("stock", 0)) > 0:
        resources[substitute]["stock"] = int(resources[substitute]["stock"]) - 1
        resources[substitute]["consumed"] = int(resources[substitute].get("consumed", 0)) + 1
        return True, substitute, copy.deepcopy(resources[substitute])
    return False, resource_id, copy.deepcopy(resource) if resource else None


def produce_reuse(resource_id: str, resources: dict[str, dict[str, object]], condition: Condition) -> dict[str, object] | None:
    if not condition.repair_reuse:
        return None
    base = {
        "reed_offcut": {"stock": 0, "scarcity": "reuse", "place": "moss_hollow", "base_price": 0.18, "frequency_hz": 0.236, "flower_node": "return_petal"},
        "glass_reading": {"stock": 0, "scarcity": "reuse", "place": "glass_mire", "base_price": 0.20, "frequency_hz": 0.271, "flower_node": "explore_petal"},
    }.get(resource_id)
    if base is None:
        return None
    item = resources.setdefault(resource_id, {"resource_id": resource_id, **base, "initial_stock": 0, "consumed": 0, "produced_by_reuse": 0, "scarce": True})
    item["stock"] = int(item.get("stock", 0)) + 1
    item["produced_by_reuse"] = int(item.get("produced_by_reuse", 0)) + 1
    return copy.deepcopy(item)


def trace_ok(event: Mapping[str, object]) -> bool:
    required = {
        "event_id",
        "condition",
        "agent_id",
        "project_id",
        "stage",
        "required_resources",
        "allocated_resources",
        "scarcity_packet",
        "negotiation_packet",
        "exchange_ledger_entry",
        "fairness_packet",
        "reuse_packet",
        "route_cost_packet",
        "trust_price_packet",
        "project_output_packet",
        "economy_frequency_hz",
        "flower_node",
        "private_negotiation_hidden",
        "replay_frame",
        "claim_boundary",
    }
    return required.issubset(event.keys())


def simulate_condition(config: EconomyConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, object], list[dict[str, object]]]:
    places, routes, agents, objects = source_payload(source)
    resources = init_resources(condition)
    projects = {agent: {"project_id": spec["project_id"], "stage_index": 0, "completed_stages": [], "output_id": spec["output_id"], "complete": False} for agent, spec in PROJECTS.items()}
    allocations = {agent: 0 for agent in PROJECTS}
    ledger: list[dict[str, object]] = []
    events: list[dict[str, object]] = []
    replay: list[dict[str, object]] = []
    outputs: dict[str, dict[str, object]] = {}
    claim_boundary = {
        "complete_3d_world": False,
        "complete_playable_world": False,
        "subjective_consciousness": False,
        "moral_patienthood": False,
        "natural_language_emergence": False,
    }
    hits = {key: [] for key in ["scarcity", "negotiation", "ledger", "fair", "route", "trust", "freq", "replay", "privacy", "trace"]}
    reuse_consumed: list[str] = []
    reuse_produced: list[str] = []

    for event_id, (agent_id, stage_index) in enumerate(SCHEDULE):
        spec = PROJECTS[agent_id]
        project = projects[agent_id]
        stage = spec["stages"][stage_index]
        agent = agents.get(agent_id, {"agent_id": agent_id, "relationship": {}})
        required = list(stage["resources"] if condition.tool_chains else ())
        scarce = [rid for rid in required if resources.get(rid, {}).get("scarce")]
        scarcity_packet = {"enabled": condition.resource_scarcity, "scarce_resources": scarce, "scarcity_count": len(scarce)}
        needs_negotiation = bool(scarce) or any(int(resources.get(rid, {}).get("stock", 0)) <= 0 for rid in required)
        negotiation_packet = None
        accepted = True
        if needs_negotiation:
            accepted = condition.negotiation
            negotiation_packet = {
                "participants": sorted({agent_id, *[name for name in PROJECTS if name != agent_id][:2]}),
                "proposal": f"allocate {','.join(required) or 'tool time'} to {agent_id}:{stage['stage']}",
                "accepted": accepted,
                "reason": "scarce_resource_allocation" if condition.negotiation else "negotiation_disabled",
            }
        else:
            negotiation_packet = {"participants": [agent_id], "proposal": "non_scarce_stage", "accepted": True, "reason": "available_stock"}
        allocated: list[dict[str, object]] = []
        blocked: list[str] = []
        if accepted:
            for rid in required:
                ok, used_id, resource_after = allocate_resource(rid, resources, condition)
                if ok:
                    allocations[agent_id] += 1
                    allocated.append({"requested": rid, "used": used_id, "resource_after": resource_after})
                    if used_id != rid:
                        reuse_consumed.append(used_id)
                else:
                    blocked.append(rid)
        stage_complete = accepted and not blocked and condition.tool_chains
        if stage_complete:
            project["completed_stages"].append(stage["stage"])
            project["stage_index"] = max(project["stage_index"], stage_index + 1)
            if stage.get("creates_reuse"):
                produced = produce_reuse(str(stage["creates_reuse"]), resources, condition)
                if produced is not None:
                    reuse_produced.append(str(stage["creates_reuse"]))
            if stage_index == len(spec["stages"]) - 1 and condition.project_outputs:
                project["complete"] = True
                outputs[spec["output_id"]] = {
                    "output_id": spec["output_id"],
                    "agent_id": agent_id,
                    "project_id": spec["project_id"],
                    "created_event": event_id,
                    "durability": round(0.76 + len(project["completed_stages"]) * 0.04, 6),
                }
        start_place = str(agent.get("place", spec["home"]))
        target_place = str(stage["place"])
        cost = route_cost(routes, start_place, target_place, condition)
        base_price = sum(float(resources.get(rid, {}).get("base_price", 0.2)) for rid in required)
        route_component = cost or 0.0
        trust_modifier = round(1.0 - agent_trust(agent) * 0.18, 6) if condition.trust_price_modulation else 1.0
        price = round((base_price + route_component) * trust_modifier, 6)
        fair_ok = condition.fair_allocation and (max(allocations.values()) - min(allocations.values()) <= 3)
        fairness_packet = {"enabled": condition.fair_allocation, "allocations": copy.deepcopy(allocations), "fair": fair_ok}
        ledger_entry = None
        if condition.exchange_ledger:
            ledger_entry = {
                "ledger_id": stable_hash(condition.name, event_id, agent_id, stage["stage"], allocated),
                "event_id": event_id,
                "agent_id": agent_id,
                "stage": stage["stage"],
                "allocated": [{"requested": item["requested"], "used": item["used"]} for item in allocated],
                "blocked": blocked,
                "price": price,
                "route_cost": cost,
                "trust_modifier": trust_modifier,
            }
            ledger.append(ledger_entry)
        reuse_packet = {"produced": list(reuse_produced), "consumed": list(reuse_consumed), "enabled": condition.repair_reuse}
        route_cost_packet = {"enabled": condition.route_cost_accounting, "from": start_place, "to": target_place, "cost": cost}
        trust_price_packet = {"enabled": condition.trust_price_modulation, "trust_modifier": trust_modifier, "price": price}
        freq_values = [float(resources.get(item["used"], {}).get("frequency_hz", 0.0)) for item in allocated if resources.get(item["used"], {}).get("frequency_hz") is not None]
        frequency = round(sum(freq_values) / len(freq_values), 6) if freq_values and condition.frequency_flower_binding else None
        flower = next((resources.get(item["used"], {}).get("flower_node") for item in allocated if resources.get(item["used"], {}).get("flower_node")), "unbound") if condition.frequency_flower_binding else "unbound"
        replay_frame = None
        if condition.replay_timeline:
            replay_frame = {
                "replay_index": len(replay),
                "event_id": event_id,
                "agent_id": agent_id,
                "stage": stage["stage"],
                "allocated": [{"requested": item["requested"], "used": item["used"]} for item in allocated],
                "blocked": blocked,
                "outputs": copy.deepcopy(outputs),
            }
            replay.append(replay_frame)
        event = {
            "event_id": event_id,
            "condition": condition.name,
            "agent_id": agent_id,
            "project_id": spec["project_id"],
            "stage": stage["stage"],
            "tool": stage["tool"] if condition.tool_chains else None,
            "required_resources": required,
            "allocated_resources": allocated,
            "blocked_resources": blocked,
            "stage_complete": stage_complete,
            "scarcity_packet": scarcity_packet,
            "negotiation_packet": negotiation_packet,
            "exchange_ledger_entry": ledger_entry,
            "fairness_packet": fairness_packet,
            "reuse_packet": reuse_packet,
            "route_cost_packet": route_cost_packet,
            "trust_price_packet": trust_price_packet,
            "project_output_packet": copy.deepcopy(outputs.get(spec["output_id"])),
            "economy_frequency_hz": frequency,
            "flower_node": flower,
            "private_negotiation_hidden": condition.privacy_filter,
            "replay_frame": replay_frame,
            "claim_boundary": claim_boundary,
        }
        events.append(event)
        if required:
            hits["scarcity"].append(1.0 if condition.resource_scarcity and scarcity_packet["scarcity_count"] > 0 else 0.0)
        if needs_negotiation:
            hits["negotiation"].append(1.0 if negotiation_packet and negotiation_packet["accepted"] else 0.0)
        hits["ledger"].append(1.0 if ledger_entry is not None and ledger_entry["event_id"] == event_id else 0.0)
        hits["fair"].append(1.0 if fair_ok else 0.0)
        hits["route"].append(1.0 if condition.route_cost_accounting and cost is not None else 0.0)
        hits["trust"].append(1.0 if condition.trust_price_modulation and trust_modifier != 1.0 else 0.0)
        if allocated:
            hits["freq"].append(1.0 if condition.frequency_flower_binding and frequency is not None and flower != "unbound" else 0.0)
        hits["replay"].append(1.0 if replay_frame is not None and replay_frame["replay_index"] == len(replay) - 1 else 0.0)
        hits["privacy"].append(1.0 if condition.privacy_filter and event["private_negotiation_hidden"] else 0.0)
        hits["trace"].append(1.0 if trace_ok(event) and event["claim_boundary"] == claim_boundary else 0.0)

    total_stages = sum(len(spec["stages"]) for spec in PROJECTS.values())
    completed_stages = sum(len(project["completed_stages"]) for project in projects.values())
    conservation_ok = all(int(res.get("stock", 0)) >= 0 for res in resources.values())
    conservation_ok = conservation_ok and all(int(res.get("initial_stock", 0)) + int(res.get("produced_by_reuse", 0)) - int(res.get("consumed", 0)) == int(res.get("stock", 0)) for res in resources.values())
    metrics = {
        "resource_scarcity_binding_rate": mean(hits["scarcity"]),
        "tool_chain_completion_rate": completed_stages / total_stages if condition.tool_chains else 0.0,
        "negotiation_resolution_rate": mean(hits["negotiation"]),
        "exchange_ledger_integrity_rate": mean(hits["ledger"]),
        "fair_allocation_rate": mean(hits["fair"]),
        "repair_reuse_rate": min(1.0, len(set(reuse_consumed)) / 2.0) if condition.repair_reuse else 0.0,
        "route_cost_accounting_rate": mean(hits["route"]),
        "trust_price_modulation_rate": mean(hits["trust"]),
        "project_output_rate": len(outputs) / len(PROJECTS) if condition.project_outputs else 0.0,
        "resource_conservation_rate": 1.0 if conservation_ok else 0.0,
        "frequency_flower_economy_binding_rate": mean(hits["freq"]),
        "browser_economy_replay_rate": mean(hits["replay"]),
        "privacy_preservation_rate": mean(hits["privacy"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: clamp(value) for key, value in metrics.items()}
    readiness = sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS)
    row = EvalRow(
        condition=condition.name,
        agent_count=len(agents),
        object_count=len(objects),
        resource_count=len(resources),
        project_count=len(projects),
        economy_events=len(events),
        project_economy_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in metrics.items()},
    )
    state = {
        "condition": condition.name,
        "source_condition": source.get("condition"),
        "places": places,
        "routes": routes,
        "agents": agents,
        "objects": objects,
        "resources": resources,
        "projects": projects,
        "outputs": outputs,
        "exchange_ledger": ledger,
        "events": events,
        "replay": replay,
        "economy_kernel": {
            "scarce_resources": RESOURCE_SPECS,
            "projects": PROJECTS,
            "reuse_substitutes": REUSE_SUBSTITUTES,
            "not_moral_patienthood_or_free_will": True,
        },
    }
    return row, state, events


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_project_economy_resource_negotiation_toolchain"]

    def loss(name: str) -> float:
        return round(full.project_economy_readiness - by_name[name].project_economy_readiness, 6)

    losses = {
        "no_resource_scarcity_loss": loss("no_resource_scarcity"),
        "no_tool_chains_loss": loss("no_tool_chains"),
        "no_negotiation_loss": loss("no_negotiation"),
        "no_exchange_ledger_loss": loss("no_exchange_ledger"),
        "no_fair_allocation_loss": loss("no_fair_allocation"),
        "no_repair_reuse_loss": loss("no_repair_reuse"),
        "no_route_cost_accounting_loss": loss("no_route_cost_accounting"),
        "no_trust_price_modulation_loss": loss("no_trust_price_modulation"),
        "no_project_outputs_loss": loss("no_project_outputs"),
        "no_frequency_flower_economy_binding_loss": loss("no_frequency_flower_economy_binding"),
        "no_replay_timeline_loss": loss("no_replay_timeline"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.project_economy_readiness >= 0.90
        and full.economy_events == len(SCHEDULE)
        and full.resource_scarcity_binding_rate == 1.0
        and full.tool_chain_completion_rate == 1.0
        and full.negotiation_resolution_rate == 1.0
        and full.exchange_ledger_integrity_rate == 1.0
        and full.repair_reuse_rate == 1.0
        and full.project_output_rate == 1.0
        and full.resource_conservation_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_resource_scarcity_loss"] >= 0.10
        and losses["no_tool_chains_loss"] >= 0.10
        and losses["no_negotiation_loss"] >= 0.10
        and losses["no_exchange_ledger_loss"] >= 0.09
        and losses["no_project_outputs_loss"] >= 0.10
    )
    return VerdictRow(
        full_condition=full.condition,
        full_project_economy_readiness=full.project_economy_readiness,
        full_resource_scarcity_binding_rate=full.resource_scarcity_binding_rate,
        full_tool_chain_completion_rate=full.tool_chain_completion_rate,
        full_negotiation_resolution_rate=full.negotiation_resolution_rate,
        full_exchange_ledger_integrity_rate=full.exchange_ledger_integrity_rate,
        full_fair_allocation_rate=full.fair_allocation_rate,
        full_repair_reuse_rate=full.repair_reuse_rate,
        full_route_cost_accounting_rate=full.route_cost_accounting_rate,
        full_trust_price_modulation_rate=full.trust_price_modulation_rate,
        full_project_output_rate=full.project_output_rate,
        full_resource_conservation_rate=full.resource_conservation_rate,
        full_frequency_flower_economy_binding_rate=full.frequency_flower_economy_binding_rate,
        full_browser_economy_replay_rate=full.browser_economy_replay_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        supports_project_economy_resource_negotiation_toolchain_bridge=supports,
        supports_multi_agent_project_economy_seed=supports,
        supports_complete_3d_world=False,
        supports_complete_playable_world=False,
        supports_subjective_consciousness=False,
        supports_moral_patienthood_claim=False,
        supports_natural_language_emergence=False,
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
        if condition.name == "integrated_project_economy_resource_negotiation_toolchain":
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
        "weights": WEIGHTS,
        "resource_specs": RESOURCE_SPECS,
        "project_specs": PROJECTS,
        "moral_boundary": {
            "economy_seed_not_complete_gameplay": True,
            "scarcity_not_subjective_deprivation": True,
            "negotiation_policy_not_moral_patienthood": True,
            "resource_prices_not_real_economy_claim": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "persistent craft ecology with wear, breakage, maintenance, and supply shocks",
    }
    state = {
        "condition": "integrated_project_economy_resource_negotiation_toolchain",
        "config": asdict(config),
        "source_condition": source.get("condition"),
        "economy_state": integrated_state,
        "trace_events": len(integrated_trace),
        "moral_boundary": results["moral_boundary"],
    }
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_PROJECT_ECONOMY_RESOURCE_NEGOTIATION_TOOLCHAIN_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_PROJECT_ECONOMY_RESOURCE_NEGOTIATION_TOOLCHAIN_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_PROJECT_ECONOMY_RESOURCE_NEGOTIATION_TOOLCHAIN_STATE", state)
    return results


def parse_args() -> EconomyConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=EconomyConfig.seed)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return EconomyConfig(seed=args.seed, source_state=args.source_state)


def main() -> None:
    config = parse_args()
    results = run(config)
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("project_economy_readiness", f"{verdict['full_project_economy_readiness']:.6f}")
    print("economy_events", results["rows"][0]["economy_events"])
    print("no_resource_scarcity_loss", f"{verdict['no_resource_scarcity_loss']:.6f}")
    print("no_negotiation_loss", f"{verdict['no_negotiation_loss']:.6f}")
    print("no_project_outputs_loss", f"{verdict['no_project_outputs_loss']:.6f}")


if __name__ == "__main__":
    main()
