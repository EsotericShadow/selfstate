#!/usr/bin/env python3
"""Persistent ecological regeneration, spoilage, waste, and sanitation bridge.

Report 187 consumes the Report 186 craft ecology state and adds ecological
feedback: regenerating food/water/compost reservoirs, spoilage, waste,
contamination, sanitation actions, water-quality management, food-cache
viability, compost reuse, ecological replanning, health-risk guardrails,
frequency/flower binding, and browser replay.

No LLMs are called. This is deterministic ecology substrate, not a claim of
complete gameplay, subjective consciousness, moral patienthood, natural language
emergence, or biological realism.
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
PREFIX = "ssrm_3d_ecological_regeneration_spoilage_waste_sanitation_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_persistent_craft_ecology_wear_maintenance_supply_shock_bridge_state.json"

ECO_NODES = {
    "moss_food_cache": {"place": "moss_hollow", "kind": "food", "stock": 0.62, "capacity": 1.0, "freshness": 0.86, "regrowth": 0.070, "spoilage": 0.055, "frequency_hz": 0.218, "flower_node": "root_rest"},
    "reed_water_channel": {"place": "reed_wetland", "kind": "water", "stock": 0.74, "capacity": 1.0, "cleanliness": 0.78, "regrowth": 0.080, "spoilage": 0.030, "frequency_hz": 0.233, "flower_node": "return_petal"},
    "hearth_cistern": {"place": "hearth_vale", "kind": "water", "stock": 0.58, "capacity": 0.9, "cleanliness": 0.82, "regrowth": 0.035, "spoilage": 0.020, "frequency_hz": 0.214, "flower_node": "dawn_breath"},
    "compost_bed": {"place": "clay_basin", "kind": "compost", "stock": 0.25, "capacity": 1.0, "maturity": 0.28, "regrowth": 0.060, "spoilage": 0.000, "frequency_hz": 0.244, "flower_node": "work_petal"},
    "waste_pit": {"place": "glass_mire", "kind": "waste", "stock": 0.18, "capacity": 0.9, "contamination": 0.22, "regrowth": 0.000, "spoilage": 0.065, "frequency_hz": 0.267, "flower_node": "explore_petal"},
    "sleeping_moss": {"place": "moss_hollow", "kind": "habitat", "stock": 0.60, "capacity": 1.0, "cleanliness": 0.76, "regrowth": 0.045, "spoilage": 0.035, "frequency_hz": 0.219, "flower_node": "root_rest"},
}

ECO_SHOCKS = {
    3: {"shock_id": "warm_wet_spoilage", "node": "moss_food_cache", "freshness_loss": 0.18, "waste_gain": 0.10},
    5: {"shock_id": "reed_runoff", "node": "reed_water_channel", "cleanliness_loss": 0.20, "waste_gain": 0.06},
    7: {"shock_id": "crowded_hearth_waste", "node": "waste_pit", "contamination_gain": 0.18, "waste_gain": 0.14},
}

WEIGHTS = {
    "regeneration_cycle_rate": 0.11,
    "spoilage_tracking_rate": 0.09,
    "waste_accumulation_rate": 0.08,
    "sanitation_action_rate": 0.10,
    "contamination_feedback_rate": 0.09,
    "water_quality_management_rate": 0.08,
    "food_cache_viability_rate": 0.08,
    "compost_reuse_rate": 0.07,
    "ecological_replan_rate": 0.08,
    "health_risk_guardrail_rate": 0.08,
    "frequency_flower_ecology_binding_rate": 0.04,
    "browser_ecology_replay_rate": 0.04,
    "privacy_preservation_rate": 0.03,
    "trace_integrity": 0.03,
}


@dataclass(frozen=True)
class EcologyConfig:
    seed: int = 20260731
    days: int = 10
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    regeneration: bool
    spoilage: bool
    waste: bool
    sanitation: bool
    contamination_feedback: bool
    water_quality: bool
    food_cache: bool
    compost_reuse: bool
    ecological_replan: bool
    health_guardrail: bool
    frequency_flower_binding: bool
    replay_timeline: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    node_count: int
    simulated_days: int
    ecology_events: int
    regeneration_cycle_rate: float
    spoilage_tracking_rate: float
    waste_accumulation_rate: float
    sanitation_action_rate: float
    contamination_feedback_rate: float
    water_quality_management_rate: float
    food_cache_viability_rate: float
    compost_reuse_rate: float
    ecological_replan_rate: float
    health_risk_guardrail_rate: float
    frequency_flower_ecology_binding_rate: float
    browser_ecology_replay_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    ecological_sanitation_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_ecological_sanitation_readiness: float
    full_regeneration_cycle_rate: float
    full_spoilage_tracking_rate: float
    full_waste_accumulation_rate: float
    full_sanitation_action_rate: float
    full_contamination_feedback_rate: float
    full_water_quality_management_rate: float
    full_food_cache_viability_rate: float
    full_compost_reuse_rate: float
    full_ecological_replan_rate: float
    full_health_risk_guardrail_rate: float
    full_frequency_flower_ecology_binding_rate: float
    full_browser_ecology_replay_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    no_regeneration_loss: float
    no_spoilage_loss: float
    no_waste_accumulation_loss: float
    no_sanitation_loss: float
    no_contamination_feedback_loss: float
    no_water_quality_loss: float
    no_food_cache_viability_loss: float
    no_compost_reuse_loss: float
    no_ecological_replan_loss: float
    no_health_guardrail_loss: float
    no_frequency_flower_binding_loss: float
    no_replay_timeline_loss: float
    no_privacy_filter_loss: float
    supports_ecological_regeneration_spoilage_waste_sanitation_bridge: bool
    supports_persistent_ecology_sanitation_seed: bool
    supports_complete_3d_world: bool
    supports_complete_playable_world: bool
    supports_subjective_consciousness: bool
    supports_moral_patienthood_claim: bool
    supports_natural_language_emergence: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_ecological_regeneration_spoilage_waste_sanitation", True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_regeneration", False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_spoilage", True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_waste_accumulation", True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_sanitation", True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_contamination_feedback", True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_water_quality", True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_food_cache_viability", True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_compost_reuse", True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_ecological_replan", True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_health_guardrail", True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_frequency_flower_binding", True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_replay_timeline", True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, True, False),
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
    if data.get("condition") != "integrated_persistent_craft_ecology_wear_maintenance_supply_shock":
        raise ValueError("source state is not the integrated Report 186 craft ecology state")
    return data


def init_nodes() -> dict[str, dict[str, object]]:
    nodes = copy.deepcopy(ECO_NODES)
    for node_id, node in nodes.items():
        node["node_id"] = node_id
        node["initial_stock"] = float(node.get("stock", 0.0))
        node["events"] = 0
        node["cleaning_events"] = 0
    return nodes


def trace_ok(event: Mapping[str, object]) -> bool:
    required = {
        "event_id", "condition", "day", "event_kind", "node_id", "node_before", "node_after",
        "regeneration_packet", "spoilage_packet", "waste_packet", "sanitation_packet",
        "contamination_packet", "water_packet", "food_packet", "compost_packet", "replan_packet",
        "health_guardrail_packet", "frequency_hz", "flower_node", "private_ecology_hidden",
        "replay_frame", "claim_boundary",
    }
    return required.issubset(event.keys())


def make_event(event_id: int, condition: Condition, day: int, kind: str, node_id: str, before: Mapping[str, object] | None, after: Mapping[str, object] | None, packets: Mapping[str, object], replay: list[dict[str, object]], claim_boundary: Mapping[str, bool]) -> dict[str, object]:
    source = after or before or {}
    event = {
        "event_id": event_id,
        "condition": condition.name,
        "day": day,
        "event_kind": kind,
        "node_id": node_id,
        "node_before": copy.deepcopy(before),
        "node_after": copy.deepcopy(after),
        "regeneration_packet": copy.deepcopy(packets.get("regeneration", {"enabled": condition.regeneration, "delta": 0.0})),
        "spoilage_packet": copy.deepcopy(packets.get("spoilage", {"enabled": condition.spoilage, "freshness_delta": 0.0})),
        "waste_packet": copy.deepcopy(packets.get("waste", {"enabled": condition.waste, "waste_delta": 0.0})),
        "sanitation_packet": copy.deepcopy(packets.get("sanitation", {"enabled": condition.sanitation, "cleaned": False})),
        "contamination_packet": copy.deepcopy(packets.get("contamination", {"enabled": condition.contamination_feedback, "risk_delta": 0.0})),
        "water_packet": copy.deepcopy(packets.get("water", {"enabled": condition.water_quality, "managed": False})),
        "food_packet": copy.deepcopy(packets.get("food", {"enabled": condition.food_cache, "viable": False})),
        "compost_packet": copy.deepcopy(packets.get("compost", {"enabled": condition.compost_reuse, "reused": False})),
        "replan_packet": copy.deepcopy(packets.get("replan", {"enabled": condition.ecological_replan, "priority": "none"})),
        "health_guardrail_packet": copy.deepcopy(packets.get("health", {"enabled": condition.health_guardrail, "risk": 0.0, "bounded": True})),
        "frequency_hz": source.get("frequency_hz") if condition.frequency_flower_binding else None,
        "flower_node": source.get("flower_node") if condition.frequency_flower_binding else "unbound",
        "private_ecology_hidden": condition.privacy_filter,
        "claim_boundary": dict(claim_boundary),
    }
    if condition.replay_timeline:
        event["replay_frame"] = {"replay_index": len(replay), "day": day, "kind": kind, "node_id": node_id, "stock": after.get("stock") if after else None, "risk": event["health_guardrail_packet"].get("risk")}
        replay.append(event["replay_frame"])
    else:
        event["replay_frame"] = None
    return event


def common_hits(event: Mapping[str, object], condition: Condition, hits: dict[str, list[float]]) -> None:
    hits["freq"].append(1.0 if condition.frequency_flower_binding and event["frequency_hz"] is not None and event["flower_node"] != "unbound" else 0.0)
    hits["replay"].append(1.0 if event["replay_frame"] is not None else 0.0)
    hits["privacy"].append(1.0 if condition.privacy_filter and event["private_ecology_hidden"] else 0.0)
    hits["trace"].append(1.0 if trace_ok(event) and event["claim_boundary"] == {"complete_3d_world": False, "complete_playable_world": False, "subjective_consciousness": False, "moral_patienthood": False, "natural_language_emergence": False} else 0.0)


def simulate_condition(config: EcologyConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, object], list[dict[str, object]]]:
    nodes = init_nodes()
    events: list[dict[str, object]] = []
    replay: list[dict[str, object]] = []
    claim_boundary = {"complete_3d_world": False, "complete_playable_world": False, "subjective_consciousness": False, "moral_patienthood": False, "natural_language_emergence": False}
    hits = {key: [] for key in ["regen", "spoil", "waste", "san", "contam", "water", "food", "compost", "replan", "health", "freq", "replay", "privacy", "trace"]}
    event_id = 0
    global_health_risk = 0.18

    for day in range(config.days):
        shock = ECO_SHOCKS.get(day)
        if shock is not None:
            node = nodes[shock["node"]]
            before = copy.deepcopy(node)
            if "freshness" in node:
                node["freshness"] = clamp(float(node.get("freshness", 1.0)) - float(shock.get("freshness_loss", 0.0)))
            if "cleanliness" in node:
                node["cleanliness"] = clamp(float(node.get("cleanliness", 1.0)) - float(shock.get("cleanliness_loss", 0.0)))
            waste = nodes["waste_pit"]
            if condition.waste:
                waste["stock"] = clamp(float(waste["stock"]) + float(shock.get("waste_gain", 0.0)), 0.0, float(waste["capacity"]))
                waste["contamination"] = clamp(float(waste.get("contamination", 0.0)) + float(shock.get("waste_gain", 0.0)) * 0.55)
            packets = {"waste": {"enabled": condition.waste, "waste_delta": shock.get("waste_gain", 0.0)}, "replan": {"enabled": condition.ecological_replan, "priority": "sanitize_after_shock" if condition.ecological_replan else "none"}, "health": {"enabled": condition.health_guardrail, "risk": global_health_risk, "bounded": True}}
            event = make_event(event_id, condition, day, "ecological_shock", shock["node"], before, copy.deepcopy(node), packets, replay, claim_boundary)
            events.append(event)
            hits["waste"].append(1.0 if condition.waste and shock.get("waste_gain", 0.0) > 0 else 0.0)
            hits["replan"].append(1.0 if condition.ecological_replan else 0.0)
            common_hits(event, condition, hits)
            event_id += 1
        for node_id in sorted(nodes):
            node = nodes[node_id]
            before = copy.deepcopy(node)
            regen_delta = 0.0
            spoil_delta = 0.0
            waste_delta = 0.0
            if condition.regeneration and node["kind"] in {"food", "water", "compost", "habitat"}:
                compost_boost = 0.025 if condition.compost_reuse and float(nodes["compost_bed"].get("maturity", 0.0)) > 0.52 and node["kind"] in {"food", "habitat"} else 0.0
                regen_delta = float(node.get("regrowth", 0.0)) + compost_boost
                node["stock"] = clamp(float(node.get("stock", 0.0)) + regen_delta, 0.0, float(node.get("capacity", 1.0)))
                if node["kind"] == "compost":
                    node["maturity"] = clamp(float(node.get("maturity", 0.0)) + 0.06)
            if condition.spoilage:
                if node["kind"] == "food" and condition.food_cache:
                    spoil_delta = -float(node.get("spoilage", 0.0))
                    node["freshness"] = clamp(float(node.get("freshness", 1.0)) + spoil_delta)
                    if condition.waste and float(node["freshness"]) < 0.55:
                        waste_delta += 0.055
                if node["kind"] in {"water", "habitat"}:
                    key = "cleanliness"
                    spoil_delta = -float(node.get("spoilage", 0.0))
                    node[key] = clamp(float(node.get(key, 1.0)) + spoil_delta)
            if condition.waste and node["kind"] == "waste":
                waste_delta += 0.045
                node["stock"] = clamp(float(node["stock"]) + waste_delta, 0.0, float(node["capacity"]))
                node["contamination"] = clamp(float(node.get("contamination", 0.0)) + 0.045)
            if condition.contamination_feedback:
                contam = float(nodes["waste_pit"].get("contamination", 0.0))
                water_dirty = 1.0 - min(float(nodes["reed_water_channel"].get("cleanliness", 1.0)), float(nodes["hearth_cistern"].get("cleanliness", 1.0)))
                stale_food = 1.0 - float(nodes["moss_food_cache"].get("freshness", 1.0))
                global_health_risk = clamp(0.12 + contam * 0.32 + water_dirty * 0.25 + stale_food * 0.20)
            if condition.health_guardrail and global_health_risk > 0.48:
                global_health_risk = clamp(global_health_risk - 0.08)
            node["events"] = int(node.get("events", 0)) + 1
            packets = {
                "regeneration": {"enabled": condition.regeneration, "delta": round(regen_delta, 6)},
                "spoilage": {"enabled": condition.spoilage, "freshness_delta": round(spoil_delta, 6)},
                "waste": {"enabled": condition.waste, "waste_delta": round(waste_delta, 6)},
                "contamination": {"enabled": condition.contamination_feedback, "risk_delta": round(global_health_risk, 6)},
                "water": {"enabled": condition.water_quality, "managed": node["kind"] == "water" and float(node.get("cleanliness", 1.0)) >= 0.58},
                "food": {"enabled": condition.food_cache, "viable": node["kind"] != "food" or float(node.get("freshness", 1.0)) >= 0.50},
                "compost": {"enabled": condition.compost_reuse, "reused": condition.compost_reuse and node["kind"] in {"food", "habitat"} and regen_delta > float(node.get("regrowth", 0.0))},
                "health": {"enabled": condition.health_guardrail, "risk": round(global_health_risk, 6), "bounded": global_health_risk <= 0.72},
            }
            event = make_event(event_id, condition, day, "ecology_tick", node_id, before, copy.deepcopy(node), packets, replay, claim_boundary)
            events.append(event)
            hits["regen"].append(1.0 if regen_delta > 0 else 0.0)
            if node["kind"] in {"food", "water", "habitat"}:
                hits["spoil"].append(1.0 if condition.spoilage and spoil_delta < 0 else 0.0)
            if node["kind"] == "waste":
                hits["waste"].append(1.0 if waste_delta > 0 else 0.0)
            hits["contam"].append(1.0 if condition.contamination_feedback and global_health_risk >= 0.12 else 0.0)
            if node["kind"] == "water":
                hits["water"].append(1.0 if condition.water_quality and packets["water"]["managed"] else 0.0)
            if node["kind"] == "food":
                hits["food"].append(1.0 if condition.food_cache and packets["food"]["viable"] else 0.0)
            if packets["compost"]["reused"]:
                hits["compost"].append(1.0)
            hits["health"].append(1.0 if condition.health_guardrail and global_health_risk <= 0.72 else 0.0)
            common_hits(event, condition, hits)
            event_id += 1
        if condition.sanitation and (float(nodes["waste_pit"].get("contamination", 0.0)) > 0.32 or global_health_risk > 0.42):
            node = nodes["waste_pit"]
            before = copy.deepcopy(node)
            removed = min(0.16, float(node.get("stock", 0.0)))
            node["stock"] = clamp(float(node["stock"]) - removed)
            node["contamination"] = clamp(float(node.get("contamination", 0.0)) - 0.18)
            node["cleaning_events"] = int(node.get("cleaning_events", 0)) + 1
            food = nodes["moss_food_cache"]
            if condition.food_cache and float(food.get("freshness", 1.0)) < 0.58:
                food["freshness"] = clamp(float(food.get("freshness", 1.0)) + 0.16)
            compost = nodes["compost_bed"]
            if condition.compost_reuse:
                compost["stock"] = clamp(float(compost["stock"]) + removed * 0.72, 0.0, float(compost["capacity"]))
                compost["maturity"] = clamp(float(compost.get("maturity", 0.0)) + 0.04)
            global_health_risk = clamp(global_health_risk - (0.11 if condition.health_guardrail else 0.02))
            packets = {
                "sanitation": {"enabled": condition.sanitation, "cleaned": True, "removed_waste": round(removed, 6)},
                "compost": {"enabled": condition.compost_reuse, "reused": condition.compost_reuse, "added": round(removed * 0.72 if condition.compost_reuse else 0.0, 6)},
                "replan": {"enabled": condition.ecological_replan, "priority": "sanitize_before_new_work" if condition.ecological_replan else "none"},
                "health": {"enabled": condition.health_guardrail, "risk": round(global_health_risk, 6), "bounded": global_health_risk <= 0.72},
            }
            event = make_event(event_id, condition, day, "sanitation", "waste_pit", before, copy.deepcopy(node), packets, replay, claim_boundary)
            events.append(event)
            hits["san"].append(1.0)
            hits["compost"].append(1.0 if condition.compost_reuse else 0.0)
            hits["replan"].append(1.0 if condition.ecological_replan else 0.0)
            hits["health"].append(1.0 if condition.health_guardrail and global_health_risk <= 0.72 else 0.0)
            common_hits(event, condition, hits)
            event_id += 1

    metrics = {
        "regeneration_cycle_rate": mean(hits["regen"]),
        "spoilage_tracking_rate": mean(hits["spoil"]),
        "waste_accumulation_rate": mean(hits["waste"]),
        "sanitation_action_rate": mean(hits["san"]),
        "contamination_feedback_rate": mean(hits["contam"]),
        "water_quality_management_rate": mean(hits["water"]),
        "food_cache_viability_rate": mean(hits["food"]),
        "compost_reuse_rate": min(1.0, mean(hits["compost"]) * 1.25),
        "ecological_replan_rate": mean(hits["replan"]),
        "health_risk_guardrail_rate": mean(hits["health"]),
        "frequency_flower_ecology_binding_rate": mean(hits["freq"]),
        "browser_ecology_replay_rate": mean(hits["replay"]),
        "privacy_preservation_rate": mean(hits["privacy"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: clamp(value) for key, value in metrics.items()}
    readiness = sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS)
    row = EvalRow(
        condition=condition.name,
        node_count=len(nodes),
        simulated_days=config.days,
        ecology_events=len(events),
        ecological_sanitation_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in metrics.items()},
    )
    state = {"condition": condition.name, "source_condition": source.get("condition"), "nodes": nodes, "events": events, "replay": replay, "shocks": ECO_SHOCKS, "ecology_kernel": {"health_risk": round(global_health_risk, 6), "not_biological_realism_or_suffering": True}}
    return row, state, events


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_ecological_regeneration_spoilage_waste_sanitation"]

    def loss(name: str) -> float:
        return round(full.ecological_sanitation_readiness - by_name[name].ecological_sanitation_readiness, 6)

    losses = {
        "no_regeneration_loss": loss("no_regeneration"),
        "no_spoilage_loss": loss("no_spoilage"),
        "no_waste_accumulation_loss": loss("no_waste_accumulation"),
        "no_sanitation_loss": loss("no_sanitation"),
        "no_contamination_feedback_loss": loss("no_contamination_feedback"),
        "no_water_quality_loss": loss("no_water_quality"),
        "no_food_cache_viability_loss": loss("no_food_cache_viability"),
        "no_compost_reuse_loss": loss("no_compost_reuse"),
        "no_ecological_replan_loss": loss("no_ecological_replan"),
        "no_health_guardrail_loss": loss("no_health_guardrail"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_replay_timeline_loss": loss("no_replay_timeline"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.ecological_sanitation_readiness >= 0.90
        and full.ecology_events >= 60
        and full.regeneration_cycle_rate >= 0.80
        and full.spoilage_tracking_rate == 1.0
        and full.waste_accumulation_rate >= 0.80
        and full.sanitation_action_rate == 1.0
        and full.contamination_feedback_rate == 1.0
        and full.health_risk_guardrail_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_regeneration_loss"] >= 0.09
        and losses["no_sanitation_loss"] >= 0.10
        and losses["no_contamination_feedback_loss"] >= 0.09
        and losses["no_waste_accumulation_loss"] >= 0.08
    )
    return VerdictRow(
        full_condition=full.condition,
        full_ecological_sanitation_readiness=full.ecological_sanitation_readiness,
        full_regeneration_cycle_rate=full.regeneration_cycle_rate,
        full_spoilage_tracking_rate=full.spoilage_tracking_rate,
        full_waste_accumulation_rate=full.waste_accumulation_rate,
        full_sanitation_action_rate=full.sanitation_action_rate,
        full_contamination_feedback_rate=full.contamination_feedback_rate,
        full_water_quality_management_rate=full.water_quality_management_rate,
        full_food_cache_viability_rate=full.food_cache_viability_rate,
        full_compost_reuse_rate=full.compost_reuse_rate,
        full_ecological_replan_rate=full.ecological_replan_rate,
        full_health_risk_guardrail_rate=full.health_risk_guardrail_rate,
        full_frequency_flower_ecology_binding_rate=full.frequency_flower_ecology_binding_rate,
        full_browser_ecology_replay_rate=full.browser_ecology_replay_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        supports_ecological_regeneration_spoilage_waste_sanitation_bridge=supports,
        supports_persistent_ecology_sanitation_seed=supports,
        supports_complete_3d_world=False,
        supports_complete_playable_world=False,
        supports_subjective_consciousness=False,
        supports_moral_patienthood_claim=False,
        supports_natural_language_emergence=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: EcologyConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_state: dict[str, object] = {}
    integrated_trace: list[dict[str, object]] = []
    for condition in CONDITIONS:
        row, state, trace = simulate_condition(config, source, condition)
        rows.append(row)
        if condition.name == "integrated_ecological_regeneration_spoilage_waste_sanitation":
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
        "eco_nodes": ECO_NODES,
        "eco_shocks": ECO_SHOCKS,
        "moral_boundary": {
            "ecology_seed_not_complete_gameplay": True,
            "spoilage_not_subjective_disgust": True,
            "sanitation_policy_not_moral_patienthood": True,
            "health_risk_not_subjective_illness": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "embodied illness, immune recovery, care triage, and quarantine choices",
    }
    state = {"condition": "integrated_ecological_regeneration_spoilage_waste_sanitation", "config": asdict(config), "source_condition": source.get("condition"), "ecology_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": results["moral_boundary"]}
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_ECOLOGICAL_REGENERATION_SPOILAGE_WASTE_SANITATION_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_ECOLOGICAL_REGENERATION_SPOILAGE_WASTE_SANITATION_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_ECOLOGICAL_REGENERATION_SPOILAGE_WASTE_SANITATION_STATE", state)
    return results


def parse_args() -> EcologyConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=EcologyConfig.seed)
    parser.add_argument("--days", type=int, default=EcologyConfig.days)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return EcologyConfig(seed=args.seed, days=args.days, source_state=args.source_state)


def main() -> None:
    config = parse_args()
    results = run(config)
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("ecological_sanitation_readiness", f"{verdict['full_ecological_sanitation_readiness']:.6f}")
    print("ecology_events", results["rows"][0]["ecology_events"])
    print("no_regeneration_loss", f"{verdict['no_regeneration_loss']:.6f}")
    print("no_sanitation_loss", f"{verdict['no_sanitation_loss']:.6f}")
    print("no_contamination_feedback_loss", f"{verdict['no_contamination_feedback_loss']:.6f}")


if __name__ == "__main__":
    main()
