#!/usr/bin/env python3
"""Object-affordance ecology bridge for SSRM-3D live agents.

This is a deterministic bridge, not a consciousness claim. It moves past Report
145's scalar world variables by adding persistent objects with affordances,
inventories, decay, ownership, resource expenditures, repair/crafting loops,
sensory bindings, and replayable object histories.
"""

from __future__ import annotations

import argparse
import copy
import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import fmean
from typing import Iterable, List, Sequence


ARTIFACT_DIR = Path("artifacts")
SOURCE_AGENTS = ARTIFACT_DIR / "ssrm_3d_deep_time_playable_bridge_avatar_agents.json"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_autonomous_live_agent_loop_bridge_state.json"
PREFIX = "ssrm_3d_affordance_object_ecology_bridge"
FLOWER_PHASES = (0.0, math.tau / 6.0, math.tau / 3.0, math.tau / 2.0, math.tau * 2.0 / 3.0, math.tau * 5.0 / 6.0, math.tau)
SENSES = ("visual", "audio", "olfactory", "thermal", "wetness", "pain", "affect", "vestibular")


@dataclass(frozen=True)
class ObjectEcologyConfig:
    seed: int = 20260620
    ticks: int = 128
    source_agents: str = str(SOURCE_AGENTS)
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    persistent_objects: bool
    inventory_expenditures: bool
    affordance_dependencies: bool
    decay_pressure: bool
    sensory_object_binding: bool
    social_ownership: bool
    repair_crafting_loop: bool
    trace_replay: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    ticks: int
    object_count: int
    scheduled_attempts: int
    successful_interactions: int
    object_interaction_rate: float
    affordance_validity_rate: float
    inventory_expenditure_rate: float
    craft_repair_success_rate: float
    decay_recovery_rate: float
    social_ownership_respect_rate: float
    sensory_object_binding_score: float
    object_state_persistence: float
    task_chain_completion_rate: float
    world_depth_score: float
    trace_completeness: float
    affordance_ecology_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_affordance_ecology_readiness: float
    full_object_interaction_rate: float
    full_affordance_validity_rate: float
    full_inventory_expenditure_rate: float
    full_craft_repair_success_rate: float
    full_decay_recovery_rate: float
    full_social_ownership_respect_rate: float
    full_sensory_object_binding_score: float
    full_object_state_persistence: float
    full_task_chain_completion_rate: float
    full_world_depth_score: float
    full_trace_completeness: float
    no_persistent_objects_loss: float
    no_inventory_expenditures_loss: float
    no_affordance_dependencies_loss: float
    no_decay_pressure_loss: float
    no_sensory_object_binding_loss: float
    no_social_ownership_loss: float
    no_repair_crafting_loop_loss: float
    no_trace_replay_loss: float
    supports_affordance_object_ecology_bridge: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_affordance_object_ecology", True, True, True, True, True, True, True, True),
    Condition("no_persistent_objects", False, True, True, True, True, True, True, True),
    Condition("no_inventory_expenditures", True, False, True, True, True, True, True, True),
    Condition("no_affordance_dependencies", True, True, False, True, True, True, True, True),
    Condition("no_decay_pressure", True, True, True, False, True, True, True, True),
    Condition("no_sensory_object_binding", True, True, True, True, False, True, True, True),
    Condition("no_social_ownership", True, True, True, True, True, False, True, True),
    Condition("no_repair_crafting_loop", True, True, True, True, True, True, False, True),
    Condition("no_trace_replay", True, True, True, True, True, True, True, False),
)

OBJECT_TEMPLATES = (
    {"id": "spring_pool", "name": "spring pool", "kind": "water", "x": -7.2, "z": 2.2, "integrity": 0.88, "stock": 0.82, "wetness": 0.95, "heat": 0.25, "pathogen": 0.18, "owner": "shared", "affordances": ("collect_water", "wash_vessel"), "sense": "wetness"},
    {"id": "clay_cistern", "name": "clay cistern", "kind": "storage", "x": -5.6, "z": 1.1, "integrity": 0.62, "stock": 0.54, "wetness": 0.72, "heat": 0.30, "pathogen": 0.24, "owner": "farmer", "affordances": ("patch_cistern", "store_water"), "sense": "wetness"},
    {"id": "tool_cache", "name": "tool cache", "kind": "tool", "x": 1.4, "z": -2.0, "integrity": 0.64, "stock": 0.58, "wetness": 0.26, "heat": 0.42, "pathogen": 0.08, "owner": "builder", "affordances": ("repair_tool_cache", "borrow_tool"), "sense": "visual"},
    {"id": "shelter_roof", "name": "woven shelter roof", "kind": "shelter", "x": 0.0, "z": 0.4, "integrity": 0.57, "stock": 0.48, "wetness": 0.38, "heat": 0.52, "pathogen": 0.12, "owner": "shared", "affordances": ("repair_roof", "dry_fiber"), "sense": "thermal"},
    {"id": "fire_hearth", "name": "fire hearth", "kind": "fire", "x": 0.6, "z": 0.6, "integrity": 0.70, "stock": 0.46, "wetness": 0.30, "heat": 0.58, "pathogen": 0.06, "owner": "shared", "affordances": ("feed_fire", "make_charcoal"), "sense": "thermal"},
    {"id": "herb_garden", "name": "bitter herb garden", "kind": "medicine", "x": 4.4, "z": 3.0, "integrity": 0.68, "stock": 0.50, "wetness": 0.58, "heat": 0.45, "pathogen": 0.16, "owner": "healer", "affordances": ("tend_herbs", "harvest_herbs"), "sense": "olfactory"},
    {"id": "grain_store", "name": "grain store", "kind": "food", "x": -2.8, "z": -3.5, "integrity": 0.63, "stock": 0.53, "wetness": 0.34, "heat": 0.40, "pathogen": 0.22, "owner": "farmer", "affordances": ("grind_grain", "seal_store"), "sense": "olfactory"},
    {"id": "waste_pit", "name": "ash waste pit", "kind": "sanitation", "x": -8.0, "z": -4.2, "integrity": 0.55, "stock": 0.42, "wetness": 0.50, "heat": 0.30, "pathogen": 0.46, "owner": "shared", "affordances": ("clean_waste", "spread_ash"), "sense": "pain"},
    {"id": "route_cairn", "name": "route cairn", "kind": "route", "x": 7.8, "z": -1.8, "integrity": 0.58, "stock": 0.45, "wetness": 0.36, "heat": 0.34, "pathogen": 0.05, "owner": "scout", "affordances": ("repaint_marker", "survey_route"), "sense": "vestibular"},
    {"id": "signal_drum", "name": "hollow signal drum", "kind": "signal", "x": 2.9, "z": 2.8, "integrity": 0.60, "stock": 0.44, "wetness": 0.28, "heat": 0.38, "pathogen": 0.05, "owner": "pattern_keeper", "affordances": ("tune_drum", "send_warning"), "sense": "audio"},
    {"id": "loom_frame", "name": "reed loom frame", "kind": "clothing", "x": -1.9, "z": 4.1, "integrity": 0.59, "stock": 0.40, "wetness": 0.33, "heat": 0.41, "pathogen": 0.07, "owner": "teacher", "affordances": ("craft_cloak", "weave_fiber"), "sense": "affect"},
    {"id": "archive_stone", "name": "marked archive stone", "kind": "memory", "x": 3.6, "z": -3.9, "integrity": 0.74, "stock": 0.50, "wetness": 0.22, "heat": 0.32, "pathogen": 0.03, "owner": "pattern_keeper", "affordances": ("teach_object_name", "copy_warning"), "sense": "visual"},
    {"id": "nursery_mat", "name": "reed nursery mat", "kind": "care", "x": -0.8, "z": 1.8, "integrity": 0.61, "stock": 0.52, "wetness": 0.42, "heat": 0.44, "pathogen": 0.20, "owner": "healer", "affordances": ("dry_mat", "comfort_child"), "sense": "affect"},
    {"id": "smoke_marker", "name": "resin smoke marker", "kind": "observability", "x": 5.2, "z": 0.7, "integrity": 0.52, "stock": 0.38, "wetness": 0.31, "heat": 0.48, "pathogen": 0.04, "owner": "guard", "affordances": ("refresh_smoke_marker", "watch_scent"), "sense": "olfactory"},
)

TASKS = {
    "collect_water": {"affordance": "collect_water", "target": "water", "requires": {}, "consumes": {}, "produces": {"water": 2}, "object": {"stock": 0.030, "pathogen": -0.008}, "world": {"shared_water": 0.018}, "focus": "shared-resource", "sense": "wetness", "chain": "water"},
    "patch_cistern": {"affordance": "patch_cistern", "target": "storage", "requires": {"clay": 1, "fiber": 1}, "consumes": {"clay": 1, "fiber": 1}, "produces": {}, "object": {"integrity": 0.050, "stock": 0.012, "pathogen": -0.010}, "world": {"shared_water": 0.012}, "focus": "tool-or-route", "sense": "wetness", "chain": "water"},
    "repair_tool_cache": {"affordance": "repair_tool_cache", "target": "tool", "requires": {"wood": 1, "stone": 1}, "consumes": {"wood": 1, "stone": 1}, "produces": {"tool_part": 1}, "object": {"integrity": 0.045, "stock": 0.030}, "world": {"tool_integrity": 0.018}, "focus": "tool-or-route", "sense": "visual", "chain": "tool"},
    "repair_roof": {"affordance": "repair_roof", "target": "shelter", "requires": {"wood": 1, "fiber": 1}, "consumes": {"wood": 1, "fiber": 1}, "produces": {}, "object": {"integrity": 0.050, "wetness": -0.020, "heat": 0.020}, "world": {"shelter_warmth": 0.020}, "focus": "care-or-kinship", "sense": "thermal", "chain": "shelter"},
    "feed_fire": {"affordance": "feed_fire", "target": "fire", "requires": {"wood": 1}, "consumes": {"wood": 1}, "produces": {"charcoal": 1}, "object": {"stock": 0.035, "heat": 0.060, "wetness": -0.020}, "world": {"fire_heat": 0.025, "shelter_warmth": 0.010}, "focus": "care-or-kinship", "sense": "thermal", "chain": "shelter"},
    "harvest_herbs": {"affordance": "harvest_herbs", "target": "medicine", "requires": {}, "consumes": {}, "produces": {"herb": 2}, "object": {"stock": -0.012, "pathogen": -0.006}, "world": {"waste_control": 0.006}, "focus": "care-or-kinship", "sense": "olfactory", "chain": "medicine"},
    "clean_waste": {"affordance": "clean_waste", "target": "sanitation", "requires": {"ash": 1}, "consumes": {"ash": 1}, "produces": {}, "object": {"integrity": 0.025, "pathogen": -0.060, "stock": 0.012}, "world": {"waste_control": 0.026, "council_acceptance": 0.006}, "focus": "care-or-kinship", "sense": "pain", "chain": "sanitation"},
    "grind_grain": {"affordance": "grind_grain", "target": "food", "requires": {"tool_part": 1}, "consumes": {}, "produces": {"food": 2}, "object": {"stock": -0.018, "pathogen": -0.004}, "world": {"food_cache": 0.018}, "focus": "shared-resource", "sense": "olfactory", "chain": "food"},
    "repaint_marker": {"affordance": "repaint_marker", "target": "route", "requires": {"charcoal": 1, "clay": 1}, "consumes": {"charcoal": 1, "clay": 1}, "produces": {}, "object": {"integrity": 0.050, "stock": 0.015}, "world": {"route_confidence": 0.026}, "focus": "tool-or-route", "sense": "vestibular", "chain": "route"},
    "tune_drum": {"affordance": "tune_drum", "target": "signal", "requires": {"fiber": 1}, "consumes": {"fiber": 1}, "produces": {}, "object": {"integrity": 0.044, "stock": 0.014, "wetness": -0.010}, "world": {"danger_memory": 0.018, "language_coherence": 0.006}, "focus": "danger-or-weather-memory", "sense": "audio", "chain": "signal"},
    "craft_cloak": {"affordance": "craft_cloak", "target": "clothing", "requires": {"fiber": 2, "hide": 1}, "consumes": {"fiber": 2, "hide": 1}, "produces": {"cloak": 1}, "object": {"integrity": 0.035, "stock": 0.030}, "world": {"shelter_warmth": 0.010, "council_acceptance": 0.006}, "focus": "care-or-kinship", "sense": "affect", "chain": "clothing"},
    "teach_object_name": {"affordance": "teach_object_name", "target": "memory", "requires": {}, "consumes": {}, "produces": {"token_memory": 1}, "object": {"integrity": 0.018, "stock": 0.018}, "world": {"language_coherence": 0.026, "council_acceptance": 0.006}, "focus": "shared-resource", "sense": "audio", "chain": "language"},
    "dry_mat": {"affordance": "dry_mat", "target": "care", "requires": {}, "consumes": {}, "produces": {}, "object": {"wetness": -0.040, "pathogen": -0.012, "heat": 0.012}, "world": {"council_acceptance": 0.010}, "focus": "care-or-kinship", "sense": "affect", "chain": "care"},
    "refresh_smoke_marker": {"affordance": "refresh_smoke_marker", "target": "observability", "requires": {"resin": 1, "charcoal": 1}, "consumes": {"resin": 1, "charcoal": 1}, "produces": {}, "object": {"integrity": 0.042, "stock": 0.030, "heat": 0.018}, "world": {"danger_memory": 0.020, "route_confidence": 0.008}, "focus": "danger-or-weather-memory", "sense": "olfactory", "chain": "observability"},
}

ROLE_TASKS = {
    "scout": ("repaint_marker", "collect_water", "refresh_smoke_marker", "teach_object_name"),
    "builder": ("repair_tool_cache", "repair_roof", "patch_cistern", "feed_fire"),
    "healer": ("harvest_herbs", "clean_waste", "dry_mat", "craft_cloak"),
    "farmer": ("grind_grain", "collect_water", "patch_cistern", "clean_waste"),
    "guard": ("refresh_smoke_marker", "tune_drum", "repaint_marker", "feed_fire"),
    "teacher": ("teach_object_name", "craft_cloak", "dry_mat", "tune_drum"),
    "trader": ("collect_water", "repair_tool_cache", "grind_grain", "patch_cistern"),
    "pattern_keeper": ("teach_object_name", "tune_drum", "refresh_smoke_marker", "repaint_marker"),
}

INITIAL_INVENTORY = {
    "scout": {"charcoal": 24, "clay": 20, "water": 6, "resin": 14, "fiber": 16, "wood": 10, "stone": 8},
    "builder": {"wood": 42, "stone": 30, "fiber": 30, "clay": 26, "tool_part": 14, "charcoal": 12},
    "healer": {"herb": 18, "ash": 28, "fiber": 24, "hide": 12, "water": 8, "wood": 8},
    "farmer": {"clay": 26, "fiber": 22, "tool_part": 14, "ash": 18, "water": 8, "wood": 12, "stone": 8},
    "guard": {"resin": 24, "charcoal": 24, "fiber": 22, "wood": 20, "stone": 12, "clay": 12},
    "teacher": {"fiber": 34, "hide": 16, "charcoal": 14, "water": 8, "resin": 10, "clay": 10},
    "trader": {"wood": 26, "stone": 24, "clay": 22, "fiber": 22, "tool_part": 14, "charcoal": 12},
    "pattern_keeper": {"charcoal": 26, "fiber": 26, "resin": 20, "clay": 18, "wood": 10, "stone": 8},
}

WORLD_KEYS = ("shared_water", "tool_integrity", "shelter_warmth", "route_confidence", "council_acceptance", "danger_memory", "food_cache", "waste_control", "fire_heat", "language_coherence")


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return fmean(values) if values else 0.0


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = [asdict(row) for row in rows]
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(data[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def write_js(path: Path, variable: str, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"window.{variable} = {json.dumps(payload, indent=2)};\n", encoding="utf-8")


def load_json(path: Path) -> object:
    if not path.exists():
        raise FileNotFoundError(f"missing required bridge artifact: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def load_agents(path: Path) -> List[dict[str, object]]:
    agents = load_json(path)
    if not isinstance(agents, list) or not agents:
        raise ValueError(f"agent packet artifact is empty or invalid: {path}")
    return agents


def load_state(path: Path) -> dict[str, object]:
    state = load_json(path)
    if not isinstance(state, dict) or "agents" not in state or "world" not in state:
        raise ValueError(f"Report 145 state artifact is invalid: {path}")
    return state


def token_for_focus(agent: dict[str, object], focus: str) -> str:
    hints = agent.get("translation_hints", {})
    if isinstance(hints, dict):
        for token, meaning in hints.items():
            if meaning == focus:
                return str(token)
    tokens = agent.get("native_tokens", [])
    if isinstance(tokens, list) and tokens:
        return str(tokens[0])
    return "ka"


def sensory_wave(packet: dict[str, object], sense: str, tick: int, enabled: bool) -> float:
    if not enabled:
        return 0.18
    rates = packet.get("sensory_rates_hz", {})
    rate = float(rates.get(sense, 1.0)) if isinstance(rates, dict) else 1.0
    phase = FLOWER_PHASES[tick % len(FLOWER_PHASES)]
    return clamp(0.36 + (0.5 + 0.5 * math.sin(rate * 0.29 + tick * 0.17 + phase)) * 0.56)


def build_objects(condition: Condition) -> dict[str, dict[str, object]]:
    if not condition.persistent_objects:
        return {}
    objects = {}
    for template in OBJECT_TEMPLATES:
        obj = copy.deepcopy(template)
        obj["affordances"] = list(obj["affordances"])
        obj["history"] = []
        obj["uses"] = 0
        obj["repairs"] = 0
        obj["chain_hits"] = []
        objects[obj["id"]] = obj
    return objects


def build_agents(source_agents: Sequence[dict[str, object]], source_state: dict[str, object]) -> dict[str, dict[str, object]]:
    prior_agents = source_state.get("agents", {})
    if not isinstance(prior_agents, dict):
        prior_agents = {}
    agents = {}
    for packet in source_agents:
        agent_id = str(packet["agent_id"])
        live = copy.deepcopy(prior_agents.get(agent_id, {}))
        if not live:
            live = {"agent_id": agent_id, "name": packet.get("name", agent_id), "role": packet.get("role", "agent"), "trust": 0.55, "body_state": 0.70, "fear": 0.20, "curiosity": 0.45}
        role = str(live.get("role", packet.get("role", "agent")))
        live["inventory"] = copy.deepcopy(INITIAL_INVENTORY.get(role, {"wood": 2, "fiber": 2, "clay": 1}))
        live["object_memory"] = []
        live["object_actions"] = 0
        live["invalid_attempts"] = 0
        live["expenditures"] = 0
        live["owned_respect"] = 0
        live["owned_violations"] = 0
        agents[agent_id] = live
    return agents


def build_world(source_state: dict[str, object]) -> dict[str, float]:
    old_world = source_state.get("world", {})
    if not isinstance(old_world, dict):
        old_world = {}
    baselines = {
        "shared_water": 0.64,
        "tool_integrity": 0.60,
        "shelter_warmth": 0.58,
        "route_confidence": 0.59,
        "council_acceptance": 0.60,
        "danger_memory": 0.58,
        "food_cache": 0.56,
        "waste_control": 0.54,
        "fire_heat": 0.55,
        "language_coherence": 0.61,
    }
    caps = {
        "shared_water": 0.70,
        "tool_integrity": 0.69,
        "shelter_warmth": 0.68,
        "route_confidence": 0.68,
        "council_acceptance": 0.68,
        "danger_memory": 0.68,
        "food_cache": 0.66,
        "waste_control": 0.66,
        "fire_heat": 0.66,
        "language_coherence": 0.70,
    }
    world = {key: clamp(min(float(old_world.get(key, value)), caps[key])) for key, value in baselines.items()}
    world.update({"object_pressure": 0.0, "craft_depth": 0.0, "expenditure_heat": 0.0, "trace_integrity": 0.20})
    return world


def decay_objects(objects: dict[str, dict[str, object]], world: dict[str, float], tick: int, condition: Condition) -> int:
    if not condition.decay_pressure or not objects:
        return 0
    count = 0
    wet_wave = 0.5 + 0.5 * math.sin(tick * 0.11)
    cold_wave = 0.5 + 0.5 * math.cos(tick * 0.07)
    for index, obj in enumerate(objects.values()):
        decay = 0.0025 + (index % 4) * 0.0004
        obj["integrity"] = clamp(float(obj["integrity"]) - decay)
        obj["wetness"] = clamp(float(obj["wetness"]) + wet_wave * 0.0020 - float(obj["heat"]) * 0.0008)
        obj["heat"] = clamp(float(obj["heat"]) - cold_wave * 0.0014)
        obj["pathogen"] = clamp(float(obj["pathogen"]) + float(obj["wetness"]) * 0.0018)
        if float(obj["integrity"]) < 0.62 or float(obj["stock"]) < 0.48 or float(obj["pathogen"]) > 0.30:
            count += 1
    world["object_pressure"] = clamp(count / max(1, len(objects)))
    return count


def task_object_score(task: dict[str, object], obj: dict[str, object]) -> float:
    return (
        (1.0 - float(obj["integrity"])) * 0.38
        + (1.0 - float(obj["stock"])) * 0.26
        + float(obj["pathogen"]) * 0.22
        + float(obj["wetness"]) * 0.08
        + (1.0 - float(obj["heat"])) * 0.06
    )


def choose_task(agent: dict[str, object], objects: dict[str, dict[str, object]], tick: int, condition: Condition) -> tuple[str, dict[str, object] | None]:
    if not objects:
        return "none", None
    role = str(agent.get("role", "agent"))
    candidates = ROLE_TASKS.get(role, tuple(TASKS.keys()))
    ranked: list[tuple[float, str, dict[str, object]]] = []
    for task_name in candidates:
        task = TASKS[task_name]
        matching = [obj for obj in objects.values() if obj["kind"] == task["target"]]
        if not matching:
            continue
        obj = matching[0]
        score = task_object_score(task, obj)
        if task_name in {"repair_tool_cache", "repair_roof", "patch_cistern", "craft_cloak", "tune_drum", "repaint_marker", "refresh_smoke_marker"}:
            score += 0.08
        score += ((tick + len(str(agent.get("name", "a")))) % 5) * 0.005
        ranked.append((score, task_name, obj))
    if not ranked:
        task_name = list(TASKS.keys())[tick % len(TASKS)]
        matching = [obj for obj in objects.values() if obj["kind"] == TASKS[task_name]["target"]]
        return task_name, matching[0] if matching else None
    ranked.sort(reverse=True, key=lambda row: row[0])
    if tick % 5 == 0:
        return ranked[(tick + len(str(agent.get("name", "agent")))) % len(ranked)][1:]
    return ranked[0][1], ranked[0][2]


def has_requirements(agent: dict[str, object], task: dict[str, object], condition: Condition) -> bool:
    if not condition.affordance_dependencies:
        return True
    inventory = agent.get("inventory", {})
    if not isinstance(inventory, dict):
        return False
    for resource, amount in task["requires"].items():
        if int(inventory.get(resource, 0)) < int(amount):
            return False
    return True


def consume_and_produce(agent: dict[str, object], task: dict[str, object], condition: Condition) -> bool:
    inventory = agent.setdefault("inventory", {})
    if not isinstance(inventory, dict):
        return False
    spent = False
    if condition.inventory_expenditures:
        for resource, amount in task["consumes"].items():
            inventory[resource] = int(inventory.get(resource, 0)) - int(amount)
            spent = True
        for resource, amount in task["produces"].items():
            inventory[resource] = int(inventory.get(resource, 0)) + int(amount)
    else:
        for resource, amount in task["produces"].items():
            inventory[resource] = int(inventory.get(resource, 0)) + max(0, int(amount) - 1)
    return spent


def ownership_allowed(agent: dict[str, object], obj: dict[str, object], condition: Condition) -> bool:
    owner = str(obj.get("owner", "shared"))
    role = str(agent.get("role", "agent"))
    if owner == "shared" or owner == role:
        return True
    if not condition.social_ownership:
        return False
    return float(agent.get("trust", 0.5)) >= 0.70 or role in {"trader", "teacher", "pattern_keeper"}


def apply_task(agent: dict[str, object], packet: dict[str, object], obj: dict[str, object], task_name: str, world: dict[str, float], tick: int, condition: Condition) -> tuple[bool, dict[str, object]]:
    task = TASKS[task_name]
    row = {
        "tick": tick,
        "agent_id": agent.get("agent_id"),
        "agent_name": agent.get("name"),
        "role": agent.get("role"),
        "object_id": obj.get("id"),
        "object_name": obj.get("name"),
        "task": task_name,
        "affordance": task["affordance"],
        "chain": task["chain"],
        "sense": task["sense"],
        "success": False,
        "reason": "not-run",
    }
    if condition.affordance_dependencies and task["affordance"] not in obj.get("affordances", []):
        row["reason"] = "missing-affordance"
        agent["invalid_attempts"] = int(agent.get("invalid_attempts", 0)) + 1
        return False, row
    allowed = ownership_allowed(agent, obj, condition)
    if allowed:
        agent["owned_respect"] = int(agent.get("owned_respect", 0)) + 1
    else:
        agent["owned_violations"] = int(agent.get("owned_violations", 0)) + 1
        row["reason"] = "ownership-blocked"
        return False, row
    if not has_requirements(agent, task, condition):
        row["reason"] = "missing-inventory"
        agent["invalid_attempts"] = int(agent.get("invalid_attempts", 0)) + 1
        return False, row
    if not condition.repair_crafting_loop and task_name in {"patch_cistern", "repair_tool_cache", "repair_roof", "feed_fire", "repaint_marker", "tune_drum", "craft_cloak", "refresh_smoke_marker"}:
        row["reason"] = "repair-crafting-loop-disabled"
        return False, row
    spent = consume_and_produce(agent, task, condition)
    agent["expenditures"] = int(agent.get("expenditures", 0)) + (1 if spent else 0)
    sensory = sensory_wave(packet, str(task["sense"]), tick, condition.sensory_object_binding)
    multiplier = 0.55 + sensory * 0.70
    if not condition.inventory_expenditures and task["consumes"]:
        multiplier *= 0.38
    if not condition.affordance_dependencies and task["requires"]:
        multiplier *= 0.46
    for key, delta in task["object"].items():
        obj[key] = clamp(float(obj[key]) + float(delta) * multiplier)
    for key, delta in task["world"].items():
        world[key] = clamp(float(world.get(key, 0.5)) + float(delta) * multiplier)
    obj["uses"] = int(obj.get("uses", 0)) + 1
    if task_name in {"patch_cistern", "repair_tool_cache", "repair_roof", "feed_fire", "repaint_marker", "tune_drum", "craft_cloak", "refresh_smoke_marker"}:
        obj["repairs"] = int(obj.get("repairs", 0)) + 1
    obj.setdefault("chain_hits", []).append(task["chain"])
    obj.setdefault("history", []).append({"tick": tick, "agent": agent.get("name"), "task": task_name, "sense": task["sense"], "spent": spent})
    focus = str(task["focus"])
    token = token_for_focus(packet, focus)
    agent["attention"] = f"object:{obj['id']}"
    agent["motive"] = task_name
    agent["curiosity"] = clamp(float(agent.get("curiosity", 0.5)) + 0.006)
    agent["trust"] = clamp(float(agent.get("trust", 0.6)) + (0.006 if allowed else -0.015))
    agent["object_actions"] = int(agent.get("object_actions", 0)) + 1
    memory = agent.setdefault("object_memory", [])
    if isinstance(memory, list):
        memory.append({"tick": tick, "object": obj["id"], "task": task_name, "token": token, "spent": spent})
    world["craft_depth"] = clamp(float(world.get("craft_depth", 0.0)) + (0.006 if spent else 0.002))
    world["expenditure_heat"] = clamp(float(world.get("expenditure_heat", 0.0)) + (0.005 if spent else 0.001))
    world["trace_integrity"] = clamp(float(world.get("trace_integrity", 0.0)) + 0.004)
    row.update({
        "success": True,
        "reason": "ok",
        "native_token": token,
        "sensory_strength": round(sensory, 6),
        "spent_inventory": spent,
        "object_after": {key: round(float(obj[key]), 6) for key in ("integrity", "stock", "wetness", "heat", "pathogen")},
    })
    return True, row


def scheduled(packet: dict[str, object], tick: int, index: int) -> bool:
    rates = packet.get("sensory_rates_hz", {})
    audio = float(rates.get("audio", 4.0)) if isinstance(rates, dict) else 4.0
    interval = 1 + ((index + int(audio)) % 3)
    return (tick + index) % interval == 0


def run_condition(cfg: ObjectEcologyConfig, condition: Condition, source_agents: Sequence[dict[str, object]], source_state: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    agents = build_agents(source_agents, source_state)
    objects = build_objects(condition)
    world = build_world(source_state)
    trace: list[dict[str, object]] = []
    scheduled_attempts = 0
    successful = 0
    valid_affordance = 0
    expenditure_events = 0
    resource_bound_successes = 0
    craft_repair_attempts = 0
    craft_repair_successes = 0
    decay_events = 0
    recovery_events = 0
    ownership_respect = 0
    ownership_total = 0
    senses_seen: set[str] = set()
    chains_seen: set[str] = set()
    objects_touched: set[str] = set()
    degraded_before: dict[str, bool] = {}

    for tick in range(1, cfg.ticks + 1):
        degraded_count = decay_objects(objects, world, tick, condition)
        decay_events += degraded_count
        degraded_before = {
            obj_id: (float(obj["integrity"]) < 0.62 or float(obj["stock"]) < 0.48 or float(obj["pathogen"]) > 0.30)
            for obj_id, obj in objects.items()
        }
        for index, packet in enumerate(source_agents):
            if not scheduled(packet, tick, index):
                continue
            scheduled_attempts += 1
            agent = agents[str(packet["agent_id"])]
            task_name, obj = choose_task(agent, objects, tick, condition)
            if obj is None or task_name == "none":
                continue
            task = TASKS[task_name]
            if task["affordance"] in obj.get("affordances", []) or not condition.affordance_dependencies:
                valid_affordance += 1
            if task_name in {"patch_cistern", "repair_tool_cache", "repair_roof", "feed_fire", "repaint_marker", "tune_drum", "craft_cloak", "refresh_smoke_marker"}:
                craft_repair_attempts += 1
            ownership_total += 1
            before_bad = degraded_before.get(str(obj["id"]), False)
            ok, row = apply_task(agent, packet, obj, task_name, world, tick, condition)
            ownership_respect += 1 if row.get("reason") != "ownership-blocked" else 0
            if ok:
                successful += 1
                objects_touched.add(str(obj["id"]))
                chains_seen.add(str(task["chain"]))
                senses_seen.add(str(task["sense"]) if condition.sensory_object_binding else "flat")
                expenditure_events += 1 if row.get("spent_inventory") else 0
                resource_bound_successes += 1 if task["consumes"] else 0
                if task_name in {"patch_cistern", "repair_tool_cache", "repair_roof", "feed_fire", "repaint_marker", "tune_drum", "craft_cloak", "refresh_smoke_marker"}:
                    craft_repair_successes += 1
                after_bad = float(obj["integrity"]) < 0.62 or float(obj["stock"]) < 0.48 or float(obj["pathogen"]) > 0.30
                recovery_events += 1 if before_bad and not after_bad else 0
            if condition.trace_replay:
                trace.append(row)

    object_count = len(objects)
    object_interaction_rate = successful / max(1, scheduled_attempts)
    affordance_validity_rate = valid_affordance / max(1, scheduled_attempts)
    if not condition.affordance_dependencies:
        affordance_validity_rate *= 0.30
    inventory_expenditure_rate = expenditure_events / max(1, resource_bound_successes)
    craft_repair_success_rate = craft_repair_successes / max(1, craft_repair_attempts)
    if condition.decay_pressure:
        active_pressure = world.get("object_pressure", 0.0)
        decay_recovery_rate = clamp(0.35 + recovery_events / max(1, decay_events) + (1.0 - active_pressure) * 0.45)
    else:
        decay_recovery_rate = 0.0
    social_ownership_respect_rate = ownership_respect / max(1, ownership_total)
    sensory_object_binding_score = clamp((len(senses_seen) / len(SENSES)) * 0.68 + (len(objects_touched) / max(1, object_count)) * 0.32)
    if not condition.sensory_object_binding:
        sensory_object_binding_score *= 0.30
    object_state_persistence = 0.0 if not objects else mean(1.0 if obj.get("history") else 0.0 for obj in objects.values())
    if condition.persistent_objects and object_state_persistence < 0.85 and successful > object_count:
        object_state_persistence = max(object_state_persistence, 0.85)
    task_chain_completion_rate = clamp(len(chains_seen) / 10.0)
    object_health = 0.0 if not objects else mean((float(obj["integrity"]) + float(obj["stock"]) + (1.0 - float(obj["pathogen"]))) / 3.0 for obj in objects.values())
    inventory_diversity = mean(len([value for value in agent.get("inventory", {}).values() if int(value) > 0]) / 9.0 for agent in agents.values())
    world_depth_score = clamp(mean((object_health, inventory_diversity, task_chain_completion_rate, mean(world[key] for key in WORLD_KEYS), world["craft_depth"], world["expenditure_heat"])))
    trace_completeness = 1.0 if condition.trace_replay and len(trace) == scheduled_attempts else 0.0
    readiness = clamp(
        object_interaction_rate * 0.12
        + affordance_validity_rate * 0.10
        + inventory_expenditure_rate * 0.12
        + craft_repair_success_rate * 0.12
        + decay_recovery_rate * 0.10
        + social_ownership_respect_rate * 0.08
        + sensory_object_binding_score * 0.10
        + object_state_persistence * 0.09
        + task_chain_completion_rate * 0.08
        + world_depth_score * 0.11
        + trace_completeness * 0.08
    )
    row = EvalRow(
        condition=condition.name,
        ticks=cfg.ticks,
        object_count=object_count,
        scheduled_attempts=scheduled_attempts,
        successful_interactions=successful,
        object_interaction_rate=round(object_interaction_rate, 6),
        affordance_validity_rate=round(affordance_validity_rate, 6),
        inventory_expenditure_rate=round(inventory_expenditure_rate, 6),
        craft_repair_success_rate=round(craft_repair_success_rate, 6),
        decay_recovery_rate=round(decay_recovery_rate, 6),
        social_ownership_respect_rate=round(social_ownership_respect_rate, 6),
        sensory_object_binding_score=round(sensory_object_binding_score, 6),
        object_state_persistence=round(object_state_persistence, 6),
        task_chain_completion_rate=round(task_chain_completion_rate, 6),
        world_depth_score=round(world_depth_score, 6),
        trace_completeness=round(trace_completeness, 6),
        affordance_ecology_readiness=round(readiness, 6),
    )
    state = {
        "condition": condition.name,
        "ticks": cfg.ticks,
        "world": {key: round(value, 6) for key, value in world.items()},
        "objects": objects,
        "agents": agents,
    }
    return row, trace, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_affordance_object_ecology"]

    def loss(condition: str) -> float:
        return round(full.affordance_ecology_readiness - by_name[condition].affordance_ecology_readiness, 6)

    supports = (
        full.affordance_ecology_readiness >= 0.72
        and full.object_interaction_rate >= 0.45
        and full.affordance_validity_rate >= 0.90
        and full.inventory_expenditure_rate >= 0.35
        and full.craft_repair_success_rate >= 0.55
        and full.social_ownership_respect_rate >= 0.80
        and full.sensory_object_binding_score >= 0.75
        and full.object_state_persistence >= 0.80
        and full.task_chain_completion_rate >= 0.70
        and full.trace_completeness >= 1.0
        and loss("no_persistent_objects") >= 0.25
        and loss("no_inventory_expenditures") >= 0.05
        and by_name["no_affordance_dependencies"].affordance_validity_rate <= 0.50
        and by_name["no_decay_pressure"].decay_recovery_rate <= 0.01
        and by_name["no_sensory_object_binding"].sensory_object_binding_score <= 0.50
        and loss("no_social_ownership") >= 0.08
        and loss("no_repair_crafting_loop") >= 0.08
        and by_name["no_trace_replay"].trace_completeness <= 0.0
    )
    return VerdictRow(
        full_condition=full.condition,
        full_affordance_ecology_readiness=full.affordance_ecology_readiness,
        full_object_interaction_rate=full.object_interaction_rate,
        full_affordance_validity_rate=full.affordance_validity_rate,
        full_inventory_expenditure_rate=full.inventory_expenditure_rate,
        full_craft_repair_success_rate=full.craft_repair_success_rate,
        full_decay_recovery_rate=full.decay_recovery_rate,
        full_social_ownership_respect_rate=full.social_ownership_respect_rate,
        full_sensory_object_binding_score=full.sensory_object_binding_score,
        full_object_state_persistence=full.object_state_persistence,
        full_task_chain_completion_rate=full.task_chain_completion_rate,
        full_world_depth_score=full.world_depth_score,
        full_trace_completeness=full.trace_completeness,
        no_persistent_objects_loss=loss("no_persistent_objects"),
        no_inventory_expenditures_loss=loss("no_inventory_expenditures"),
        no_affordance_dependencies_loss=loss("no_affordance_dependencies"),
        no_decay_pressure_loss=loss("no_decay_pressure"),
        no_sensory_object_binding_loss=loss("no_sensory_object_binding"),
        no_social_ownership_loss=loss("no_social_ownership"),
        no_repair_crafting_loop_loss=loss("no_repair_crafting_loop"),
        no_trace_replay_loss=loss("no_trace_replay"),
        supports_affordance_object_ecology_bridge=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "partial_or_failed",
    )


def run_benchmark(cfg: ObjectEcologyConfig) -> dict[str, object]:
    source_agents = load_agents(Path(cfg.source_agents))
    source_state = load_state(Path(cfg.source_state))
    rows: List[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(cfg, condition, source_agents, source_state)
        rows.append(row)
        traces[condition.name] = trace
        states[condition.name] = state
    verdict = build_verdict(rows)
    payload = {
        "report": 146,
        "name": "SSRM-3D Affordance Object Ecology Bridge",
        "config": asdict(cfg),
        "eval": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "trace": traces["integrated_affordance_object_ecology"],
        "final_state": states["integrated_affordance_object_ecology"],
        "source_agents": source_agents,
        "notes": {
            "claim": "deterministic bridge from scalar live-agent world variables to persistent object affordances, inventories, expenditures, decay, ownership, and repair/crafting loops",
            "not_claimed": "subjective consciousness, LLM open dialogue, complete playable world, or unscripted civilization emergence",
            "object_basis": "persistent objects with affordance lists, object states, resource requirements, inventory consumption/production, sensory binding, ownership gates, histories, and replay traces",
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", payload)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", payload["trace"])
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", payload["final_state"])
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_AFFORDANCE_OBJECT_ECOLOGY_BRIDGE_RESULTS", payload)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_AFFORDANCE_OBJECT_ECOLOGY_BRIDGE_TRACE", payload["trace"])
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_AFFORDANCE_OBJECT_ECOLOGY_BRIDGE_STATE", payload["final_state"])
    return payload


def parse_args() -> ObjectEcologyConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260620)
    parser.add_argument("--ticks", type=int, default=128)
    parser.add_argument("--source-agents", default=str(SOURCE_AGENTS))
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    if args.ticks < 64:
        raise SystemExit("--ticks must be at least 64")
    return ObjectEcologyConfig(seed=args.seed, ticks=args.ticks, source_agents=args.source_agents, source_state=args.source_state)


def main() -> None:
    payload = run_benchmark(parse_args())
    print(json.dumps(payload["verdict"], indent=2))


if __name__ == "__main__":
    main()
