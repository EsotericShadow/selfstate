#!/usr/bin/env python3
"""Persistent craft ecology with wear, breakage, maintenance, and shocks.

Report 186 consumes the Report 185 project economy state and adds durability
state for tools and crafted outputs. Use causes wear, wear can become breakage,
maintenance consumes scarce repair materials, supply shocks remove stock, repair
queues compete with new work, and replans preserve recoverable continuity.

No LLMs are called. This is deterministic craft-ecology substrate, not a claim
of complete gameplay, subjective consciousness, moral patienthood, natural
language emergence, or free will.
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
PREFIX = "ssrm_3d_persistent_craft_ecology_wear_maintenance_supply_shock_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_project_economy_resource_negotiation_toolchain_bridge_state.json"

CRAFT_ITEMS = {
    "hearth_latch_repaired": {"kind": "output", "owner": "Ari", "place": "hearth_vale", "durability": 0.86, "wear_rate": 0.13, "repair": ("repair_fiber", "clay_mass"), "frequency_hz": 0.242, "flower_node": "work_petal"},
    "dry_bedding_ready": {"kind": "output", "owner": "Fay", "place": "moss_hollow", "durability": 0.84, "wear_rate": 0.12, "repair": ("dry_moss", "reed_bundle"), "frequency_hz": 0.219, "flower_node": "root_rest"},
    "route_warning_signal_ready": {"kind": "output", "owner": "Milo", "place": "stone_ridge", "durability": 0.82, "wear_rate": 0.14, "repair": ("signal_charge", "glass_reading"), "frequency_hz": 0.259, "flower_node": "social_petal"},
    "clay_patch_kit": {"kind": "tool", "owner": "Ari", "place": "clay_basin", "durability": 0.78, "wear_rate": 0.11, "repair": ("repair_fiber",), "frequency_hz": 0.241, "flower_node": "work_petal"},
    "dry_cloak": {"kind": "tool", "owner": "Fay", "place": "moss_hollow", "durability": 0.76, "wear_rate": 0.10, "repair": ("dry_moss",), "frequency_hz": 0.219, "flower_node": "return_petal"},
    "signal_shell": {"kind": "tool", "owner": "Milo", "place": "stone_ridge", "durability": 0.75, "wear_rate": 0.12, "repair": ("signal_charge",), "frequency_hz": 0.258, "flower_node": "social_petal"},
    "glass_lens": {"kind": "tool", "owner": "Milo", "place": "glass_mire", "durability": 0.72, "wear_rate": 0.13, "repair": ("glass_reading",), "frequency_hz": 0.271, "flower_node": "explore_petal"},
}

MAINTENANCE_RESOURCES = {
    "repair_fiber": {"stock": 6, "place": "reed_wetland", "frequency_hz": 0.229, "flower_node": "return_petal"},
    "clay_mass": {"stock": 5, "place": "clay_basin", "frequency_hz": 0.241, "flower_node": "work_petal"},
    "dry_moss": {"stock": 5, "place": "moss_hollow", "frequency_hz": 0.218, "flower_node": "root_rest"},
    "reed_bundle": {"stock": 4, "place": "reed_wetland", "frequency_hz": 0.233, "flower_node": "social_petal"},
    "signal_charge": {"stock": 5, "place": "stone_ridge", "frequency_hz": 0.258, "flower_node": "social_petal"},
    "glass_reading": {"stock": 4, "place": "glass_mire", "frequency_hz": 0.271, "flower_node": "explore_petal"},
    "reed_offcut": {"stock": 3, "place": "moss_hollow", "frequency_hz": 0.236, "flower_node": "return_petal"},
    "clay_scrap": {"stock": 3, "place": "clay_basin", "frequency_hz": 0.244, "flower_node": "work_petal"},
}

REPAIR_SUBSTITUTES = {
    "reed_bundle": "reed_offcut",
    "repair_fiber": "reed_offcut",
    "clay_mass": "clay_scrap",
}

SUPPLY_SHOCKS = {
    2: {"shock_id": "reed_flood", "place": "reed_wetland", "losses": {"repair_fiber": 1, "reed_bundle": 1}},
    4: {"shock_id": "glass_mire_slick", "place": "glass_mire", "losses": {"glass_reading": 1}},
    5: {"shock_id": "ridge_silence", "place": "stone_ridge", "losses": {"signal_charge": 1}},
}

WEIGHTS = {
    "wear_tracking_rate": 0.06,
    "breakage_detection_rate": 0.09,
    "maintenance_action_rate": 0.14,
    "supply_shock_response_rate": 0.12,
    "repair_resource_competition_rate": 0.08,
    "output_degradation_rate": 0.06,
    "toolchain_degradation_coupling_rate": 0.09,
    "replan_from_shock_rate": 0.08,
    "craft_state_persistence_rate": 0.08,
    "resource_conservation_rate": 0.07,
    "frequency_flower_maintenance_binding_rate": 0.05,
    "browser_craft_replay_rate": 0.04,
    "privacy_preservation_rate": 0.02,
    "trace_integrity": 0.02,
}


@dataclass(frozen=True)
class CraftConfig:
    seed: int = 20260730
    days: int = 7
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    wear_tracking: bool
    breakage_detection: bool
    maintenance: bool
    supply_shocks: bool
    repair_competition: bool
    output_degradation: bool
    toolchain_coupling: bool
    replan_from_shock: bool
    craft_persistence: bool
    frequency_flower_binding: bool
    replay_timeline: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    item_count: int
    resource_count: int
    simulated_days: int
    craft_events: int
    wear_tracking_rate: float
    breakage_detection_rate: float
    maintenance_action_rate: float
    supply_shock_response_rate: float
    repair_resource_competition_rate: float
    output_degradation_rate: float
    toolchain_degradation_coupling_rate: float
    replan_from_shock_rate: float
    craft_state_persistence_rate: float
    resource_conservation_rate: float
    frequency_flower_maintenance_binding_rate: float
    browser_craft_replay_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    craft_ecology_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_craft_ecology_readiness: float
    full_wear_tracking_rate: float
    full_breakage_detection_rate: float
    full_maintenance_action_rate: float
    full_supply_shock_response_rate: float
    full_repair_resource_competition_rate: float
    full_output_degradation_rate: float
    full_toolchain_degradation_coupling_rate: float
    full_replan_from_shock_rate: float
    full_craft_state_persistence_rate: float
    full_resource_conservation_rate: float
    full_frequency_flower_maintenance_binding_rate: float
    full_browser_craft_replay_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    no_wear_tracking_loss: float
    no_breakage_detection_loss: float
    no_maintenance_loss: float
    no_supply_shocks_loss: float
    no_repair_competition_loss: float
    no_output_degradation_loss: float
    no_toolchain_coupling_loss: float
    no_replan_from_shock_loss: float
    no_craft_persistence_loss: float
    no_frequency_flower_binding_loss: float
    no_replay_timeline_loss: float
    no_privacy_filter_loss: float
    supports_persistent_craft_ecology_wear_maintenance_supply_shock_bridge: bool
    supports_persistent_craft_ecology_seed: bool
    supports_complete_3d_world: bool
    supports_complete_playable_world: bool
    supports_subjective_consciousness: bool
    supports_moral_patienthood_claim: bool
    supports_natural_language_emergence: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_persistent_craft_ecology_wear_maintenance_supply_shock", True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_wear_tracking", False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_breakage_detection", True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_maintenance", True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_supply_shocks", True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_repair_competition", True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_output_degradation", True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_toolchain_coupling", True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_replan_from_shock", True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_craft_persistence", True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_frequency_flower_binding", True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_replay_timeline", True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_hash(*parts: object) -> str:
    key = "|".join(json.dumps(part, sort_keys=True) if isinstance(part, (dict, list, tuple)) else str(part) for part in parts)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


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


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    if data.get("condition") != "integrated_project_economy_resource_negotiation_toolchain":
        raise ValueError("source state is not the integrated Report 185 economy state")
    return data


def init_items(source: Mapping[str, object]) -> dict[str, dict[str, object]]:
    economy = source.get("economy_state", {}) if isinstance(source.get("economy_state"), Mapping) else {}
    source_outputs = economy.get("outputs", {}) if isinstance(economy.get("outputs"), Mapping) else {}
    items = copy.deepcopy(CRAFT_ITEMS)
    for output_id, output in source_outputs.items():
        if output_id in items and isinstance(output, Mapping):
            items[output_id]["durability"] = float(output.get("durability", items[output_id]["durability"]))
    for item_id, item in items.items():
        item["item_id"] = item_id
        item["initial_durability"] = item["durability"]
        item["wear_events"] = 0
        item["maintenance_events"] = 0
        item["broken"] = False
        item["blocked_project"] = False
    return items


def init_resources() -> dict[str, dict[str, object]]:
    resources = copy.deepcopy(MAINTENANCE_RESOURCES)
    for rid, res in resources.items():
        res["resource_id"] = rid
        res["initial_stock"] = int(res["stock"])
        res["consumed"] = 0
        res["lost_to_shock"] = 0
        res["produced"] = 0
    return resources


def apply_resource_loss(resources: dict[str, dict[str, object]], losses: Mapping[str, int]) -> dict[str, int]:
    actual: dict[str, int] = {}
    for rid, requested_loss in losses.items():
        res = resources.get(rid)
        if res is None:
            continue
        loss = min(int(requested_loss), int(res.get("stock", 0)))
        res["stock"] = int(res.get("stock", 0)) - loss
        res["lost_to_shock"] = int(res.get("lost_to_shock", 0)) + loss
        actual[rid] = loss
    return actual


def allocate_repair(resources: dict[str, dict[str, object]], required: Sequence[str], condition: Condition) -> tuple[list[str], list[str], bool]:
    used: list[str] = []
    missing: list[str] = []
    substitute_used = False
    for rid in required:
        res = resources.get(rid)
        if res is not None and int(res.get("stock", 0)) > 0:
            res["stock"] = int(res["stock"]) - 1
            res["consumed"] = int(res.get("consumed", 0)) + 1
            used.append(rid)
            continue
        sub = REPAIR_SUBSTITUTES.get(rid)
        sub_res = resources.get(sub) if condition.repair_competition else None
        if sub and sub_res is not None and int(sub_res.get("stock", 0)) > 0:
            sub_res["stock"] = int(sub_res["stock"]) - 1
            sub_res["consumed"] = int(sub_res.get("consumed", 0)) + 1
            used.append(sub)
            substitute_used = True
        else:
            missing.append(rid)
    return used, missing, substitute_used


def trace_ok(event: Mapping[str, object]) -> bool:
    required = {
        "event_id", "condition", "day", "event_kind", "item_id", "item_before", "item_after",
        "wear_packet", "breakage_packet", "maintenance_packet", "supply_shock_packet",
        "competition_packet", "toolchain_packet", "replan_packet", "resource_packet",
        "frequency_hz", "flower_node", "private_maintenance_hidden", "replay_frame", "claim_boundary",
    }
    return required.issubset(event.keys())


def simulate_condition(config: CraftConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, object], list[dict[str, object]]]:
    items = init_items(source)
    resources = init_resources()
    events: list[dict[str, object]] = []
    replay: list[dict[str, object]] = []
    hits = {key: [] for key in ["wear", "breakage", "maint", "shock", "competition", "output", "toolchain", "replan", "persist", "freq", "replay", "privacy", "trace"]}
    claim_boundary = {"complete_3d_world": False, "complete_playable_world": False, "subjective_consciousness": False, "moral_patienthood": False, "natural_language_emergence": False}
    event_id = 0

    for day in range(config.days):
        shock_packet = None
        if condition.supply_shocks and day in SUPPLY_SHOCKS:
            shock = SUPPLY_SHOCKS[day]
            actual = apply_resource_loss(resources, shock["losses"])
            shock_packet = {"shock_id": shock["shock_id"], "place": shock["place"], "losses": actual, "detected": True}
            event = make_event(event_id, condition, day, "supply_shock", None, None, None, None, None, shock_packet, None, None, resources, replay, claim_boundary)
            events.append(event)
            hits["shock"].append(1.0 if actual else 0.0)
            hits["replan"].append(1.0 if condition.replan_from_shock and actual else 0.0)
            record_common_hits(event, condition, hits)
            event_id += 1
        for item_id in sorted(items):
            item = items[item_id]
            if not condition.craft_persistence:
                item["durability"] = item["initial_durability"]
                item["broken"] = False
            before = copy.deepcopy(item)
            wear_delta = 0.0
            if condition.wear_tracking and (condition.output_degradation or item["kind"] == "tool"):
                wear_delta = -float(item["wear_rate"])
                item["durability"] = round(clamp(float(item["durability"]) + wear_delta), 6)
                item["wear_events"] = int(item.get("wear_events", 0)) + 1
            became_broken = False
            if condition.breakage_detection and float(item["durability"]) <= 0.45:
                became_broken = not bool(item.get("broken"))
                item["broken"] = True
            if condition.toolchain_coupling and (item["broken"] or float(item["durability"]) <= 0.55):
                item["blocked_project"] = True
            wear_packet = {"tracked": condition.wear_tracking, "wear_delta": round(wear_delta, 6), "use_count": item.get("wear_events", 0)}
            breakage_packet = {"detected": bool(item.get("broken")) and condition.breakage_detection, "became_broken": became_broken, "threshold": 0.45}
            toolchain_packet = {"coupled": condition.toolchain_coupling, "project_blocked": bool(item.get("blocked_project")), "item_kind": item["kind"]}
            event = make_event(event_id, condition, day, "use_wear", item_id, before, copy.deepcopy(item), wear_packet, breakage_packet, shock_packet, None, toolchain_packet, resources, replay, claim_boundary)
            events.append(event)
            hits["wear"].append(1.0 if wear_delta < 0 else 0.0)
            if item["kind"] == "output":
                hits["output"].append(1.0 if condition.output_degradation and wear_delta < 0 else 0.0)
            if breakage_packet["detected"]:
                hits["breakage"].append(1.0)
            if toolchain_packet["project_blocked"]:
                hits["toolchain"].append(1.0)
            hits["persist"].append(1.0 if condition.craft_persistence and item["durability"] != item["initial_durability"] else 0.0)
            record_common_hits(event, condition, hits)
            event_id += 1
        maintenance_queue = [item_id for item_id, item in sorted(items.items()) if float(item["durability"]) <= 0.55 or bool(item.get("broken"))]
        same_resource_pressure = len([item_id for item_id in maintenance_queue if "repair_fiber" in items[item_id]["repair"]]) >= 2
        for item_id in maintenance_queue[:4]:
            item = items[item_id]
            before = copy.deepcopy(item)
            used, missing, substitute_used = allocate_repair(resources, item["repair"], condition) if condition.maintenance else ([], list(item["repair"]), False)
            success = condition.maintenance and not missing
            if success:
                item["durability"] = round(clamp(float(item["durability"]) + 0.34), 6)
                item["broken"] = False
                item["blocked_project"] = False
                item["maintenance_events"] = int(item.get("maintenance_events", 0)) + 1
            maintenance_packet = {"attempted": True, "success": success, "used_resources": used, "missing_resources": missing}
            competition_packet = {"enabled": condition.repair_competition, "same_resource_pressure": same_resource_pressure, "substitute_used": substitute_used, "queue_size": len(maintenance_queue)}
            replan_packet = {"enabled": condition.replan_from_shock, "maintenance_priority": "repair_before_new_work" if condition.replan_from_shock else "none", "delayed_new_work": bool(maintenance_queue)}
            event = make_event(event_id, condition, day, "maintenance", item_id, before, copy.deepcopy(item), None, None, shock_packet, maintenance_packet, None, resources, replay, claim_boundary, competition_packet=competition_packet, replan_packet=replan_packet)
            events.append(event)
            hits["maint"].append(1.0 if success else 0.0)
            hits["competition"].append(1.0 if condition.repair_competition and (same_resource_pressure or substitute_used) else 0.0)
            hits["replan"].append(1.0 if condition.replan_from_shock and replan_packet["delayed_new_work"] else 0.0)
            hits["persist"].append(1.0 if condition.craft_persistence and item["maintenance_events"] > 0 else 0.0)
            record_common_hits(event, condition, hits)
            event_id += 1

    conservation = all(int(res["initial_stock"]) + int(res.get("produced", 0)) - int(res.get("consumed", 0)) - int(res.get("lost_to_shock", 0)) == int(res.get("stock", 0)) for res in resources.values())
    metrics = {
        "wear_tracking_rate": mean(hits["wear"]),
        "breakage_detection_rate": 1.0 if hits["breakage"] else 0.0,
        "maintenance_action_rate": mean(hits["maint"]),
        "supply_shock_response_rate": mean(hits["shock"]),
        "repair_resource_competition_rate": mean(hits["competition"]),
        "output_degradation_rate": mean(hits["output"]),
        "toolchain_degradation_coupling_rate": 1.0 if hits["toolchain"] else 0.0,
        "replan_from_shock_rate": mean(hits["replan"]),
        "craft_state_persistence_rate": mean(hits["persist"]),
        "resource_conservation_rate": 1.0 if conservation else 0.0,
        "frequency_flower_maintenance_binding_rate": mean(hits["freq"]),
        "browser_craft_replay_rate": mean(hits["replay"]),
        "privacy_preservation_rate": mean(hits["privacy"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: clamp(value) for key, value in metrics.items()}
    readiness = sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS)
    row = EvalRow(
        condition=condition.name,
        item_count=len(items),
        resource_count=len(resources),
        simulated_days=config.days,
        craft_events=len(events),
        craft_ecology_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in metrics.items()},
    )
    state = {"condition": condition.name, "source_condition": source.get("condition"), "items": items, "resources": resources, "events": events, "replay": replay, "supply_shocks": SUPPLY_SHOCKS, "craft_kernel": {"wear_threshold": 0.55, "breakage_threshold": 0.45, "maintenance_restores": 0.34, "not_subjective_suffering": True}}
    return row, state, events


def make_event(event_id: int, condition: Condition, day: int, kind: str, item_id: str | None, item_before: Mapping[str, object] | None, item_after: Mapping[str, object] | None, wear_packet: Mapping[str, object] | None, breakage_packet: Mapping[str, object] | None, shock_packet: Mapping[str, object] | None, maintenance_packet: Mapping[str, object] | None, toolchain_packet: Mapping[str, object] | None, resources: Mapping[str, Mapping[str, object]], replay: list[dict[str, object]], claim_boundary: Mapping[str, bool], competition_packet: Mapping[str, object] | None = None, replan_packet: Mapping[str, object] | None = None) -> dict[str, object]:
    source = item_after or item_before or {}
    frequency = source.get("frequency_hz") if condition.frequency_flower_binding else None
    flower = source.get("flower_node") if condition.frequency_flower_binding else "unbound"
    resource_packet = {rid: {"stock": res.get("stock"), "consumed": res.get("consumed"), "lost_to_shock": res.get("lost_to_shock")} for rid, res in resources.items()}
    event = {
        "event_id": event_id,
        "condition": condition.name,
        "day": day,
        "event_kind": kind,
        "item_id": item_id,
        "item_before": copy.deepcopy(item_before),
        "item_after": copy.deepcopy(item_after),
        "wear_packet": copy.deepcopy(wear_packet) if wear_packet is not None else {"tracked": condition.wear_tracking, "wear_delta": 0.0},
        "breakage_packet": copy.deepcopy(breakage_packet) if breakage_packet is not None else {"detected": False, "became_broken": False, "threshold": 0.45},
        "maintenance_packet": copy.deepcopy(maintenance_packet) if maintenance_packet is not None else {"attempted": False, "success": False, "used_resources": [], "missing_resources": []},
        "supply_shock_packet": copy.deepcopy(shock_packet) if shock_packet is not None else {"detected": False, "losses": {}},
        "competition_packet": copy.deepcopy(competition_packet) if competition_packet is not None else {"enabled": condition.repair_competition, "same_resource_pressure": False, "substitute_used": False, "queue_size": 0},
        "toolchain_packet": copy.deepcopy(toolchain_packet) if toolchain_packet is not None else {"coupled": condition.toolchain_coupling, "project_blocked": False},
        "replan_packet": copy.deepcopy(replan_packet) if replan_packet is not None else {"enabled": condition.replan_from_shock, "maintenance_priority": "none", "delayed_new_work": False},
        "resource_packet": resource_packet,
        "frequency_hz": frequency,
        "flower_node": flower,
        "private_maintenance_hidden": condition.privacy_filter,
        "claim_boundary": dict(claim_boundary),
    }
    if condition.replay_timeline:
        event["replay_frame"] = {"replay_index": len(replay), "day": day, "kind": kind, "item_id": item_id, "durability": item_after.get("durability") if item_after else None, "shock": shock_packet.get("shock_id") if shock_packet else None}
        replay.append(event["replay_frame"])
    else:
        event["replay_frame"] = None
    return event


def record_common_hits(event: Mapping[str, object], condition: Condition, hits: dict[str, list[float]]) -> None:
    hits["freq"].append(1.0 if condition.frequency_flower_binding and event.get("frequency_hz") is not None and event.get("flower_node") != "unbound" else 0.0)
    hits["replay"].append(1.0 if event.get("replay_frame") is not None else 0.0)
    hits["privacy"].append(1.0 if condition.privacy_filter and event.get("private_maintenance_hidden") else 0.0)
    hits["trace"].append(1.0 if trace_ok(event) else 0.0)


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_persistent_craft_ecology_wear_maintenance_supply_shock"]

    def loss(name: str) -> float:
        return round(full.craft_ecology_readiness - by_name[name].craft_ecology_readiness, 6)

    losses = {
        "no_wear_tracking_loss": loss("no_wear_tracking"),
        "no_breakage_detection_loss": loss("no_breakage_detection"),
        "no_maintenance_loss": loss("no_maintenance"),
        "no_supply_shocks_loss": loss("no_supply_shocks"),
        "no_repair_competition_loss": loss("no_repair_competition"),
        "no_output_degradation_loss": loss("no_output_degradation"),
        "no_toolchain_coupling_loss": loss("no_toolchain_coupling"),
        "no_replan_from_shock_loss": loss("no_replan_from_shock"),
        "no_craft_persistence_loss": loss("no_craft_persistence"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_replay_timeline_loss": loss("no_replay_timeline"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.craft_ecology_readiness >= 0.90
        and full.craft_events >= 40
        and full.wear_tracking_rate == 1.0
        and full.breakage_detection_rate == 1.0
        and full.maintenance_action_rate >= 0.70
        and full.supply_shock_response_rate == 1.0
        and full.output_degradation_rate == 1.0
        and full.toolchain_degradation_coupling_rate == 1.0
        and full.resource_conservation_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_wear_tracking_loss"] >= 0.10
        and losses["no_maintenance_loss"] >= 0.10
        and losses["no_supply_shocks_loss"] >= 0.09
        and losses["no_output_degradation_loss"] >= 0.09
        and losses["no_toolchain_coupling_loss"] >= 0.09
    )
    return VerdictRow(
        full_condition=full.condition,
        full_craft_ecology_readiness=full.craft_ecology_readiness,
        full_wear_tracking_rate=full.wear_tracking_rate,
        full_breakage_detection_rate=full.breakage_detection_rate,
        full_maintenance_action_rate=full.maintenance_action_rate,
        full_supply_shock_response_rate=full.supply_shock_response_rate,
        full_repair_resource_competition_rate=full.repair_resource_competition_rate,
        full_output_degradation_rate=full.output_degradation_rate,
        full_toolchain_degradation_coupling_rate=full.toolchain_degradation_coupling_rate,
        full_replan_from_shock_rate=full.replan_from_shock_rate,
        full_craft_state_persistence_rate=full.craft_state_persistence_rate,
        full_resource_conservation_rate=full.resource_conservation_rate,
        full_frequency_flower_maintenance_binding_rate=full.frequency_flower_maintenance_binding_rate,
        full_browser_craft_replay_rate=full.browser_craft_replay_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        supports_persistent_craft_ecology_wear_maintenance_supply_shock_bridge=supports,
        supports_persistent_craft_ecology_seed=supports,
        supports_complete_3d_world=False,
        supports_complete_playable_world=False,
        supports_subjective_consciousness=False,
        supports_moral_patienthood_claim=False,
        supports_natural_language_emergence=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: CraftConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_state: dict[str, object] = {}
    integrated_trace: list[dict[str, object]] = []
    for condition in CONDITIONS:
        row, state, trace = simulate_condition(config, source, condition)
        rows.append(row)
        if condition.name == "integrated_persistent_craft_ecology_wear_maintenance_supply_shock":
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
        "craft_items": CRAFT_ITEMS,
        "supply_shocks": SUPPLY_SHOCKS,
        "moral_boundary": {
            "craft_ecology_seed_not_complete_gameplay": True,
            "wear_breakage_not_subjective_suffering": True,
            "maintenance_policy_not_moral_patienthood": True,
            "supply_shock_not_subjective_deprivation": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "persistent ecological regeneration, spoilage, waste, and sanitation feedback",
    }
    state = {"condition": "integrated_persistent_craft_ecology_wear_maintenance_supply_shock", "config": asdict(config), "source_condition": source.get("condition"), "craft_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": results["moral_boundary"]}
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_PERSISTENT_CRAFT_ECOLOGY_WEAR_MAINTENANCE_SUPPLY_SHOCK_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_PERSISTENT_CRAFT_ECOLOGY_WEAR_MAINTENANCE_SUPPLY_SHOCK_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_PERSISTENT_CRAFT_ECOLOGY_WEAR_MAINTENANCE_SUPPLY_SHOCK_STATE", state)
    return results


def parse_args() -> CraftConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=CraftConfig.seed)
    parser.add_argument("--days", type=int, default=CraftConfig.days)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return CraftConfig(seed=args.seed, days=args.days, source_state=args.source_state)


def main() -> None:
    config = parse_args()
    results = run(config)
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("craft_ecology_readiness", f"{verdict['full_craft_ecology_readiness']:.6f}")
    print("craft_events", results["rows"][0]["craft_events"])
    print("no_wear_tracking_loss", f"{verdict['no_wear_tracking_loss']:.6f}")
    print("no_maintenance_loss", f"{verdict['no_maintenance_loss']:.6f}")
    print("no_supply_shocks_loss", f"{verdict['no_supply_shocks_loss']:.6f}")


if __name__ == "__main__":
    main()
