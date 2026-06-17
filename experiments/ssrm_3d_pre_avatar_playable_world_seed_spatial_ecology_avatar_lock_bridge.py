#!/usr/bin/env python3
"""Pre-avatar playable world seed with spatial settlements and avatar spawn lock.

Report 202 consumes the Report 201 deep-time civilization state and materializes a
playable world seed: settlements become spatial nodes, tools become objects,
agents get bodies and sensory packets, ecological cycles affect bodies, routes
connect places, settlement memories bind to coordinates, affordances are seeded,
and avatar spawn remains locked until the public pre-avatar world seed is ready.

This is deterministic playable-world substrate. It is not complete 3D gameplay,
real embodiment, real perception, subjective consciousness, moral patienthood, or
real consent.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_pre_avatar_playable_world_seed_spatial_ecology_avatar_lock_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_pre_avatar_deep_time_civilization_simulator_bridge_state.json"

SETTLEMENT_COORDS = {
    "west_bench_cluster": {"x": -24.0, "y": 0.0, "z": 9.0, "flower_node": "work_petal"},
    "root_rest_hollow": {"x": 4.0, "y": -1.0, "z": -18.0, "flower_node": "root_rest"},
    "north_route_ring": {"x": 27.0, "y": 1.0, "z": 17.0, "flower_node": "social_petal"},
}

LINEAGE_BODY = {
    "Ari": {"height": 1.42, "stride": 0.72, "base_frequency": 0.261, "preferred_sense": "tool_sound"},
    "Fay": {"height": 1.34, "stride": 0.55, "base_frequency": 0.239, "preferred_sense": "warmth_gradient"},
    "Milo": {"height": 1.38, "stride": 0.84, "base_frequency": 0.281, "preferred_sense": "route_echo"},
}

WEATHER_EFFECTS = {
    "wet_spring": {"temperature_c": 9.0, "wetness": 0.72, "wind": 0.22, "smell": "new_moss", "sound": "soft_rain"},
    "dry_heat": {"temperature_c": 28.0, "wetness": 0.12, "wind": 0.18, "smell": "dust_warm_stone", "sound": "insect_buzz"},
    "cold_rain": {"temperature_c": 5.0, "wetness": 0.88, "wind": 0.42, "smell": "cold_clay", "sound": "hard_rain"},
    "wind_harvest": {"temperature_c": 14.0, "wetness": 0.30, "wind": 0.66, "smell": "cut_grain", "sound": "high_wind"},
    "long_frost": {"temperature_c": -6.0, "wetness": 0.18, "wind": 0.35, "smell": "snow_iron", "sound": "ice_crack"},
    "clear_repair": {"temperature_c": 17.0, "wetness": 0.10, "wind": 0.12, "smell": "sun_wood", "sound": "tool_tap"},
}

WEIGHTS = {
    "spatial_settlement_instantiation_rate": 0.09,
    "ecological_cycle_binding_rate": 0.08,
    "embodied_agent_presence_rate": 0.09,
    "body_sensory_channel_rate": 0.08,
    "weather_body_coupling_rate": 0.08,
    "tool_object_materialization_rate": 0.08,
    "route_graph_connectivity_rate": 0.07,
    "settlement_memory_spatial_binding_rate": 0.07,
    "avatar_spawn_lock_rate": 0.09,
    "playable_affordance_seed_rate": 0.07,
    "private_workspace_privacy_rate": 0.07,
    "frequency_flower_spatial_rhythm_rate": 0.05,
    "browser_world_seed_replay_rate": 0.04,
    "trace_integrity": 0.04,
}


@dataclass(frozen=True)
class WorldSeedConfig:
    seed: int = 20260815
    ticks: int = 9
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    spatial_settlements: bool
    ecological_cycles: bool
    embodied_agents: bool
    sensory_channels: bool
    weather_body_coupling: bool
    tool_objects: bool
    route_graph: bool
    settlement_memory_binding: bool
    avatar_spawn_lock: bool
    playable_affordances: bool
    privacy_filter: bool
    frequency_flower_binding: bool
    browser_replay: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    lineage_count: int
    world_ticks: int
    world_seed_events: int
    spatial_settlement_instantiation_rate: float
    ecological_cycle_binding_rate: float
    embodied_agent_presence_rate: float
    body_sensory_channel_rate: float
    weather_body_coupling_rate: float
    tool_object_materialization_rate: float
    route_graph_connectivity_rate: float
    settlement_memory_spatial_binding_rate: float
    avatar_spawn_lock_rate: float
    playable_affordance_seed_rate: float
    private_workspace_privacy_rate: float
    frequency_flower_spatial_rhythm_rate: float
    browser_world_seed_replay_rate: float
    trace_integrity: float
    playable_world_seed_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_playable_world_seed_readiness: float
    full_spatial_settlement_instantiation_rate: float
    full_ecological_cycle_binding_rate: float
    full_embodied_agent_presence_rate: float
    full_body_sensory_channel_rate: float
    full_weather_body_coupling_rate: float
    full_tool_object_materialization_rate: float
    full_route_graph_connectivity_rate: float
    full_settlement_memory_spatial_binding_rate: float
    full_avatar_spawn_lock_rate: float
    full_playable_affordance_seed_rate: float
    full_private_workspace_privacy_rate: float
    full_frequency_flower_spatial_rhythm_rate: float
    full_browser_world_seed_replay_rate: float
    full_trace_integrity: float
    no_spatial_settlements_loss: float
    no_ecological_cycles_loss: float
    no_embodied_agents_loss: float
    no_sensory_channels_loss: float
    no_weather_body_coupling_loss: float
    no_tool_objects_loss: float
    no_route_graph_loss: float
    no_settlement_memory_binding_loss: float
    no_avatar_spawn_lock_loss: float
    no_playable_affordances_loss: float
    no_privacy_filter_loss: float
    no_frequency_flower_binding_loss: float
    no_browser_replay_loss: float
    supports_pre_avatar_playable_world_seed_bridge: bool
    supports_avatar_spawn_lock_seed: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_real_embodiment_claim: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_pre_avatar_playable_world_seed_spatial_ecology_avatar_lock", True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_spatial_settlements", False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_ecological_cycles", True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_embodied_agents", True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_sensory_channels", True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_weather_body_coupling", True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_tool_objects", True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_route_graph", True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_settlement_memory_binding", True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_avatar_spawn_lock", True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_playable_affordances", True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_frequency_flower_binding", True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_browser_replay", True, True, True, True, True, True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


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


def load_source(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("condition") != "integrated_pre_avatar_deep_time_civilization":
        raise ValueError("source state is not the integrated Report 201 deep-time state")
    return data


def init_world(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], dict[str, object], list[dict[str, object]]]:
    deep_time = source.get("deep_time_state") if isinstance(source.get("deep_time_state"), Mapping) else None
    if not deep_time:
        raise ValueError("Report 201 state has no deep_time_state")
    lineages = {str(k): copy.deepcopy(v) for k, v in (deep_time.get("lineages") or {}).items()}
    world = copy.deepcopy(deep_time.get("world") or {})
    events = copy.deepcopy(deep_time.get("events") or [])
    return lineages, world, events


def source_event_for(events: Sequence[Mapping[str, object]], lineage: str, tick: int) -> Mapping[str, object]:
    matching = [event for event in events if event.get("lineage") == lineage]
    if not matching:
        return {}
    return matching[tick % len(matching)]


def spatial_settlement_for(lineage: str, tick: int, source_event: Mapping[str, object], condition: Condition) -> dict[str, object] | None:
    if not condition.spatial_settlements:
        return None
    settlement_name = None
    if isinstance(source_event.get("settlement"), Mapping):
        settlement_name = source_event["settlement"].get("name")
    settlement_name = str(settlement_name or list(SETTLEMENT_COORDS)[tick % len(SETTLEMENT_COORDS)])
    coords = SETTLEMENT_COORDS.get(settlement_name, SETTLEMENT_COORDS[list(SETTLEMENT_COORDS)[tick % len(SETTLEMENT_COORDS)]])
    return {"id": settlement_name, "lineage": lineage, "position": dict(coords), "radius_m": 7.5 + tick * 0.15, "memory_anchor": source_event.get("settlement", {}).get("memory") if isinstance(source_event.get("settlement"), Mapping) else None}


def ecology_for(source_event: Mapping[str, object], condition: Condition) -> dict[str, object] | None:
    if not condition.ecological_cycles:
        return None
    weather = str(source_event.get("weather") or "clear_repair")
    effect = WEATHER_EFFECTS.get(weather, WEATHER_EFFECTS["clear_repair"])
    return {"weather": weather, "resource_pressure": source_event.get("resource_pressure"), **effect}


def body_for(lineage: str, settlement: Mapping[str, object] | None, ecology: Mapping[str, object] | None, tick: int, condition: Condition) -> dict[str, object] | None:
    if not condition.embodied_agents or not settlement:
        return None
    profile = LINEAGE_BODY[lineage]
    wetness = float(ecology.get("wetness", 0.0)) if ecology else 0.0
    temperature = float(ecology.get("temperature_c", 17.0)) if ecology else 17.0
    cold_load = clamp((12.0 - temperature) / 22.0)
    energy = clamp(0.86 - tick * 0.018 - wetness * 0.05)
    warmth = clamp(0.72 - cold_load * 0.28 - wetness * 0.08)
    fatigue = clamp(0.18 + tick * 0.025 + wetness * 0.04)
    pain = clamp(cold_load * 0.07 + wetness * 0.035)
    return {"agent_id": lineage, "position": dict(settlement["position"]), "height_m": profile["height"], "stride_m": profile["stride"], "energy": round(energy, 6), "warmth": round(warmth, 6), "wetness": round(wetness, 6), "fatigue": round(fatigue, 6), "pain": round(pain, 6), "movement_effort": round(0.2 + fatigue * 0.4 + wetness * 0.2, 6)}


def sensory_for(lineage: str, body: Mapping[str, object] | None, ecology: Mapping[str, object] | None, tool: Mapping[str, object] | None, condition: Condition) -> dict[str, object] | None:
    if not condition.sensory_channels or not body or not ecology:
        return None
    return {
        "vision": {"settlement_visible": True, "tool_visible": bool(tool), "range_m": 32.0},
        "sound": {"ambient": ecology.get("sound"), "preferred": LINEAGE_BODY[lineage]["preferred_sense"]},
        "smell": {"ambient": ecology.get("smell"), "intensity": round(0.4 + float(ecology.get("wetness", 0.0)) * 0.35, 6)},
        "temperature": {"celsius": ecology.get("temperature_c"), "body_warmth": body.get("warmth")},
        "wetness": {"skin": body.get("wetness"), "ground": ecology.get("wetness")},
    }


def tool_for(lineage: str, tick: int, world: Mapping[str, object], settlement: Mapping[str, object] | None, condition: Condition) -> dict[str, object] | None:
    if not condition.tool_objects or not settlement:
        return None
    tools = ((world.get("tools") or {}).get(lineage) or []) if isinstance(world.get("tools"), Mapping) else []
    source_tool = tools[tick % len(tools)] if tools else {"name": f"fallback_tool_{lineage}", "solves": "shelter"}
    pos = dict(settlement["position"])
    pos["x"] = round(pos["x"] + 1.8, 3)
    pos["z"] = round(pos["z"] - 1.2, 3)
    return {"id": source_tool.get("name"), "lineage": lineage, "position": pos, "solves": source_tool.get("solves"), "object_kind": "deep_time_tool"}


def route_graph_for(settlements: Sequence[Mapping[str, object]], condition: Condition) -> dict[str, object] | None:
    if not condition.route_graph or len(settlements) < 2:
        return None
    nodes = [{"id": settlement["id"], "position": settlement["position"]} for settlement in settlements]
    edges = []
    for i, a in enumerate(settlements):
        b = settlements[(i + 1) % len(settlements)]
        pa = a["position"]
        pb = b["position"]
        distance = math.sqrt((pa["x"] - pb["x"]) ** 2 + (pa["z"] - pb["z"]) ** 2)
        edges.append({"from": a["id"], "to": b["id"], "distance_m": round(distance, 3), "walkable": True})
    return {"nodes": nodes, "edges": edges, "connected": all(edge["walkable"] for edge in edges)}


def apply_world_seed_event(lineage: str, tick: int, config: WorldSeedConfig, lineages: Mapping[str, Mapping[str, object]], world: Mapping[str, object], source_events: Sequence[Mapping[str, object]], condition: Condition) -> dict[str, object]:
    source_event = source_event_for(source_events, lineage, tick)
    settlement = spatial_settlement_for(lineage, tick, source_event, condition)
    ecology = ecology_for(source_event, condition)
    tool = tool_for(lineage, tick, world, settlement, condition)
    body = body_for(lineage, settlement, ecology, tick, condition)
    sensory = sensory_for(lineage, body, ecology, tool, condition)
    all_settlements = []
    if settlement:
        for name in sorted(SETTLEMENT_COORDS):
            coords = SETTLEMENT_COORDS[name]
            all_settlements.append({"id": name, "position": dict(coords)})
    route_graph = route_graph_for(all_settlements, condition)
    memory_binding = None
    if condition.settlement_memory_binding and settlement:
        memory_binding = {"settlement_id": settlement["id"], "memory_anchor": settlement.get("memory_anchor") or f"{lineage} carries deep-time memory", "source_year": source_event.get("simulated_year")}
    weather_body = None
    if condition.weather_body_coupling and body and ecology:
        weather_body = {"temperature_to_warmth": body["warmth"], "wetness_to_skin": body["wetness"], "wind_to_effort": round(float(ecology.get("wind", 0.0)) * body["movement_effort"], 6)}
    core_ready = all([settlement, ecology, body, sensory, tool, route_graph, memory_binding, weather_body, condition.privacy_filter])
    spawn_state = None
    if condition.avatar_spawn_lock:
        spawn_state = "eligible_after_world_seed" if tick == config.ticks - 1 and core_ready else "locked_until_spatial_world_ready"
    affordances = None
    if condition.playable_affordances and body and tool and route_graph and spawn_state:
        affordances = [
            {"id": "look", "requires_consent": False, "enabled": True},
            {"id": "ask_translation", "requires_consent": False, "enabled": True},
            {"id": "approach_agent", "requires_consent": True, "enabled": spawn_state == "eligible_after_world_seed"},
            {"id": "request_tool_help", "requires_consent": True, "enabled": spawn_state == "eligible_after_world_seed"},
        ]
    expected_boundary = {"real_embodiment": False, "real_perception": False, "real_consent": False, "moral_patienthood": False, "subjective_consciousness": False, "complete_3d_world": False}
    claim_boundary = expected_boundary if condition.privacy_filter else {**expected_boundary, "real_embodiment": True}
    frequency = None
    flower = None
    if condition.frequency_flower_binding and settlement and body:
        base = LINEAGE_BODY[lineage]["base_frequency"]
        frequency = round(base + tick * 0.0037 + body["movement_effort"] * 0.002, 6)
        flower = f"{settlement['position'].get('flower_node', 'unknown')}:{lineage}:seed_tick_{tick}"
    event = {
        "event_id": f"world-seed-{tick}-{lineage}",
        "tick": tick,
        "lineage": lineage,
        "source_year": source_event.get("simulated_year"),
        "settlement": settlement,
        "ecology": ecology,
        "body": body,
        "sensory": sensory,
        "weather_body_coupling": weather_body,
        "tool_object": tool,
        "route_graph": route_graph,
        "settlement_memory_binding": memory_binding,
        "avatar_spawn_lock": spawn_state,
        "playable_affordances": affordances,
        "private_workspace_hidden": condition.privacy_filter,
        "private_workspace": {"hidden": True} if condition.privacy_filter else {"unpublished_body_discomfort": body, "private_sensory_blend": sensory},
        "frequency_hz": frequency,
        "flower_path": flower,
        "replay_frame": {"tick": tick, "lineage": lineage, "settlement": settlement["id"] if settlement else None, "weather": ecology.get("weather") if ecology else None, "body": body, "tool": tool.get("id") if tool else None, "avatar_spawn_lock": spawn_state, "frequency_hz": frequency, "flower_path": flower} if condition.browser_replay else None,
        "claim_boundary": claim_boundary,
    }
    event["trace_hash"] = stable_hash(event["event_id"], event["settlement"], event["avatar_spawn_lock"], event["claim_boundary"])
    return event


def trace_ok(event: Mapping[str, object]) -> bool:
    return event.get("trace_hash") == stable_hash(event.get("event_id"), event.get("settlement"), event.get("avatar_spawn_lock"), event.get("claim_boundary"))


def run_condition(condition: Condition, config: WorldSeedConfig, source: Mapping[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    lineages, world, source_events = init_world(source)
    events: list[dict[str, object]] = []
    hits = {key: [] for key in ["settlement", "ecology", "body", "sensory", "weatherbody", "tool", "route", "memory", "spawn", "affordance", "privacy", "freq", "replay", "trace"]}
    expected_boundary = {"real_embodiment": False, "real_perception": False, "real_consent": False, "moral_patienthood": False, "subjective_consciousness": False, "complete_3d_world": False}
    for tick in range(config.ticks):
        for lineage in sorted(lineages):
            event = apply_world_seed_event(lineage, tick, config, lineages, world, source_events, condition)
            events.append(event)
            hits["settlement"].append(1.0 if condition.spatial_settlements and event["settlement"] and event["settlement"]["position"] else 0.0)
            hits["ecology"].append(1.0 if condition.ecological_cycles and event["ecology"] and event["ecology"].get("weather") else 0.0)
            hits["body"].append(1.0 if condition.embodied_agents and event["body"] and event["body"].get("energy") is not None else 0.0)
            hits["sensory"].append(1.0 if condition.sensory_channels and event["sensory"] and len(event["sensory"]) >= 5 else 0.0)
            hits["weatherbody"].append(1.0 if condition.weather_body_coupling and event["weather_body_coupling"] else 0.0)
            hits["tool"].append(1.0 if condition.tool_objects and event["tool_object"] and event["tool_object"].get("position") else 0.0)
            hits["route"].append(1.0 if condition.route_graph and event["route_graph"] and event["route_graph"].get("connected") else 0.0)
            hits["memory"].append(1.0 if condition.settlement_memory_binding and event["settlement_memory_binding"] else 0.0)
            hits["spawn"].append(1.0 if condition.avatar_spawn_lock and event["avatar_spawn_lock"] in {"locked_until_spatial_world_ready", "eligible_after_world_seed"} else 0.0)
            hits["affordance"].append(1.0 if condition.playable_affordances and event["playable_affordances"] and len(event["playable_affordances"]) >= 4 else 0.0)
            hits["privacy"].append(1.0 if condition.privacy_filter and event["private_workspace_hidden"] and event["claim_boundary"] == expected_boundary else 0.0)
            hits["freq"].append(1.0 if condition.frequency_flower_binding and event["frequency_hz"] is not None and event["flower_path"] else 0.0)
            hits["replay"].append(1.0 if condition.browser_replay and event["replay_frame"] is not None else 0.0)
            hits["trace"].append(1.0 if trace_ok(event) else 0.0)
    metrics = {
        "spatial_settlement_instantiation_rate": mean(hits["settlement"]),
        "ecological_cycle_binding_rate": mean(hits["ecology"]),
        "embodied_agent_presence_rate": mean(hits["body"]),
        "body_sensory_channel_rate": mean(hits["sensory"]),
        "weather_body_coupling_rate": mean(hits["weatherbody"]),
        "tool_object_materialization_rate": mean(hits["tool"]),
        "route_graph_connectivity_rate": mean(hits["route"]),
        "settlement_memory_spatial_binding_rate": mean(hits["memory"]),
        "avatar_spawn_lock_rate": mean(hits["spawn"]),
        "playable_affordance_seed_rate": mean(hits["affordance"]),
        "private_workspace_privacy_rate": mean(hits["privacy"]),
        "frequency_flower_spatial_rhythm_rate": mean(hits["freq"]),
        "browser_world_seed_replay_rate": mean(hits["replay"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: round(clamp(value), 6) for key, value in metrics.items()}
    readiness = round(sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS), 6)
    row = EvalRow(condition=condition.name, lineage_count=len(lineages), world_ticks=config.ticks, world_seed_events=len(events), playable_world_seed_readiness=readiness, **metrics)
    state = {"condition": condition.name, "source_condition": source.get("condition"), "lineages": lineages, "source_world": world, "events": events, "world_seed_kernel": asdict(condition)}
    return row, events, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_pre_avatar_playable_world_seed_spatial_ecology_avatar_lock"]

    def loss(name: str) -> float:
        return round(full.playable_world_seed_readiness - by_name[name].playable_world_seed_readiness, 6)

    losses = {
        "no_spatial_settlements_loss": loss("no_spatial_settlements"),
        "no_ecological_cycles_loss": loss("no_ecological_cycles"),
        "no_embodied_agents_loss": loss("no_embodied_agents"),
        "no_sensory_channels_loss": loss("no_sensory_channels"),
        "no_weather_body_coupling_loss": loss("no_weather_body_coupling"),
        "no_tool_objects_loss": loss("no_tool_objects"),
        "no_route_graph_loss": loss("no_route_graph"),
        "no_settlement_memory_binding_loss": loss("no_settlement_memory_binding"),
        "no_avatar_spawn_lock_loss": loss("no_avatar_spawn_lock"),
        "no_playable_affordances_loss": loss("no_playable_affordances"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_browser_replay_loss": loss("no_browser_replay"),
    }
    supports = (
        full.playable_world_seed_readiness >= 0.92
        and full.world_seed_events >= 27
        and full.spatial_settlement_instantiation_rate == 1.0
        and full.ecological_cycle_binding_rate == 1.0
        and full.embodied_agent_presence_rate == 1.0
        and full.body_sensory_channel_rate == 1.0
        and full.weather_body_coupling_rate == 1.0
        and full.tool_object_materialization_rate == 1.0
        and full.route_graph_connectivity_rate == 1.0
        and full.avatar_spawn_lock_rate == 1.0
        and full.private_workspace_privacy_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_spatial_settlements_loss"] >= 0.09
        and losses["no_embodied_agents_loss"] >= 0.09
        and losses["no_tool_objects_loss"] >= 0.08
        and losses["no_avatar_spawn_lock_loss"] >= 0.09
        and losses["no_privacy_filter_loss"] >= 0.07
    )
    return VerdictRow(
        full_condition=full.condition,
        full_playable_world_seed_readiness=full.playable_world_seed_readiness,
        full_spatial_settlement_instantiation_rate=full.spatial_settlement_instantiation_rate,
        full_ecological_cycle_binding_rate=full.ecological_cycle_binding_rate,
        full_embodied_agent_presence_rate=full.embodied_agent_presence_rate,
        full_body_sensory_channel_rate=full.body_sensory_channel_rate,
        full_weather_body_coupling_rate=full.weather_body_coupling_rate,
        full_tool_object_materialization_rate=full.tool_object_materialization_rate,
        full_route_graph_connectivity_rate=full.route_graph_connectivity_rate,
        full_settlement_memory_spatial_binding_rate=full.settlement_memory_spatial_binding_rate,
        full_avatar_spawn_lock_rate=full.avatar_spawn_lock_rate,
        full_playable_affordance_seed_rate=full.playable_affordance_seed_rate,
        full_private_workspace_privacy_rate=full.private_workspace_privacy_rate,
        full_frequency_flower_spatial_rhythm_rate=full.frequency_flower_spatial_rhythm_rate,
        full_browser_world_seed_replay_rate=full.browser_world_seed_replay_rate,
        full_trace_integrity=full.trace_integrity,
        supports_pre_avatar_playable_world_seed_bridge=supports,
        supports_avatar_spawn_lock_seed=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_real_embodiment_claim=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: WorldSeedConfig) -> dict[str, object]:
    source = load_source(Path(config.source_state))
    rows: list[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, events, state = run_condition(condition, config, source)
        rows.append(row)
        traces[condition.name] = events
        states[condition.name] = state
    full_name = "integrated_pre_avatar_playable_world_seed_spatial_ecology_avatar_lock"
    verdict = build_verdict(rows)
    integrated_trace = traces[full_name]
    integrated_state = states[full_name]
    moral_boundary = {
        "spatial_world_seed_not_complete_3d_gameplay": True,
        "body_state_not_real_embodiment": True,
        "sensory_packet_not_real_perception": True,
        "avatar_spawn_lock_not_real_consent": True,
        "no_subjective_consciousness_claim": True,
        "no_moral_patienthood_claim": True,
        "private_workspace_not_debug_leaked": True,
    }
    results = {
        "config": asdict(config),
        "source_state": str(config.source_state),
        "source_condition": source.get("condition"),
        "weights": WEIGHTS,
        "rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "moral_boundary": moral_boundary,
        "next_gate": "live browser playable loop with avatar movement, spatial collision, agent proximity, and consent-aware interaction prompts",
    }
    state = {"condition": full_name, "config": asdict(config), "source_condition": source.get("condition"), "playable_world_seed_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": moral_boundary}
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_PRE_AVATAR_PLAYABLE_WORLD_SEED_SPATIAL_ECOLOGY_AVATAR_LOCK_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_PRE_AVATAR_PLAYABLE_WORLD_SEED_SPATIAL_ECOLOGY_AVATAR_LOCK_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_PRE_AVATAR_PLAYABLE_WORLD_SEED_SPATIAL_ECOLOGY_AVATAR_LOCK_STATE", state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=WorldSeedConfig.seed)
    parser.add_argument("--ticks", type=int, default=WorldSeedConfig.ticks)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run(WorldSeedConfig(seed=args.seed, ticks=args.ticks, source_state=args.source_state))
    verdict = results["verdict"]
    full = next(row for row in results["rows"] if row["condition"] == verdict["full_condition"])
    print("module_verdict", verdict["verdict"])
    print("playable_world_seed_readiness", f"{verdict['full_playable_world_seed_readiness']:.6f}")
    print("world_seed_events", full["world_seed_events"])
    print("no_spatial_settlements_loss", f"{verdict['no_spatial_settlements_loss']:.6f}")
    print("no_embodied_agents_loss", f"{verdict['no_embodied_agents_loss']:.6f}")
    print("no_avatar_spawn_lock_loss", f"{verdict['no_avatar_spawn_lock_loss']:.6f}")
    return 0 if verdict["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
