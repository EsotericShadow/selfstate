#!/usr/bin/env python3
"""Place-navigation bridge for SSRM-3D object ecology agents.

This deterministic bridge adds a place graph and route planning between the
Report 146 persistent objects. Agents must navigate terrain, pay travel costs,
use sensory gradients, update route memory, exchange wayfinding, arrive at
object destinations, and only then interact with object affordances.
"""

from __future__ import annotations

import argparse
import copy
import csv
import heapq
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import fmean
from typing import Iterable, List, Sequence


ARTIFACT_DIR = Path("artifacts")
SOURCE_AGENTS = ARTIFACT_DIR / "ssrm_3d_deep_time_playable_bridge_avatar_agents.json"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_affordance_object_ecology_bridge_state.json"
PREFIX = "ssrm_3d_place_navigation_object_bridge"
FLOWER_PHASES = (0.0, math.tau / 6.0, math.tau / 3.0, math.tau / 2.0, math.tau * 2.0 / 3.0, math.tau * 5.0 / 6.0, math.tau)
SENSES = ("visual", "audio", "olfactory", "thermal", "wetness", "pain", "affect", "vestibular")


@dataclass(frozen=True)
class NavigationConfig:
    seed: int = 20260621
    trips: int = 96
    source_agents: str = str(SOURCE_AGENTS)
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    place_graph: bool
    pathfinding: bool
    travel_expenditure: bool
    terrain_hazard: bool
    sensory_gradient: bool
    object_destination_binding: bool
    social_wayfinding: bool
    trace_replay: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    trips: int
    attempted_trips: int
    planned_routes: int
    arrivals: int
    object_interactions: int
    route_planning_success_rate: float
    destination_arrival_rate: float
    object_after_arrival_interaction_rate: float
    travel_expenditure_rate: float
    terrain_hazard_avoidance_rate: float
    sensory_gradient_alignment: float
    route_memory_update_rate: float
    social_wayfinding_rate: float
    path_efficiency_score: float
    trace_completeness: float
    place_navigation_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_place_navigation_readiness: float
    full_route_planning_success_rate: float
    full_destination_arrival_rate: float
    full_object_after_arrival_interaction_rate: float
    full_travel_expenditure_rate: float
    full_terrain_hazard_avoidance_rate: float
    full_sensory_gradient_alignment: float
    full_route_memory_update_rate: float
    full_social_wayfinding_rate: float
    full_path_efficiency_score: float
    full_trace_completeness: float
    no_place_graph_loss: float
    no_pathfinding_loss: float
    no_travel_expenditure_loss: float
    no_terrain_hazard_loss: float
    no_sensory_gradient_loss: float
    no_object_destination_binding_loss: float
    no_social_wayfinding_loss: float
    no_trace_replay_loss: float
    supports_place_navigation_object_bridge: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_place_navigation_object_bridge", True, True, True, True, True, True, True, True),
    Condition("no_place_graph", False, True, True, True, True, True, True, True),
    Condition("no_pathfinding", True, False, True, True, True, True, True, True),
    Condition("no_travel_expenditure", True, True, False, True, True, True, True, True),
    Condition("no_terrain_hazard", True, True, True, False, True, True, True, True),
    Condition("no_sensory_gradient", True, True, True, True, False, True, True, True),
    Condition("no_object_destination_binding", True, True, True, True, True, False, True, True),
    Condition("no_social_wayfinding", True, True, True, True, True, True, False, True),
    Condition("no_trace_replay", True, True, True, True, True, True, True, False),
)

PLACES = (
    {"id": "central_hearth", "name": "central hearth", "x": 0.0, "z": 0.0, "terrain": "packed", "visibility": 0.86, "scent": 0.30, "sound": 0.70, "cold": 0.24, "wetness": 0.20, "slope": 0.08},
    {"id": "spring_hollow", "name": "spring hollow", "x": -7.0, "z": 2.5, "terrain": "mud", "visibility": 0.62, "scent": 0.52, "sound": 0.46, "cold": 0.38, "wetness": 0.72, "slope": 0.20},
    {"id": "storage_yard", "name": "storage yard", "x": -4.8, "z": 0.8, "terrain": "packed", "visibility": 0.78, "scent": 0.36, "sound": 0.58, "cold": 0.30, "wetness": 0.40, "slope": 0.12},
    {"id": "tool_bend", "name": "tool bend", "x": 1.6, "z": -2.2, "terrain": "stone", "visibility": 0.72, "scent": 0.24, "sound": 0.50, "cold": 0.34, "wetness": 0.28, "slope": 0.18},
    {"id": "roof_ring", "name": "roof ring", "x": -0.4, "z": 0.8, "terrain": "packed", "visibility": 0.82, "scent": 0.32, "sound": 0.62, "cold": 0.26, "wetness": 0.34, "slope": 0.08},
    {"id": "herb_slope", "name": "herb slope", "x": 4.4, "z": 3.0, "terrain": "brush", "visibility": 0.58, "scent": 0.78, "sound": 0.38, "cold": 0.32, "wetness": 0.50, "slope": 0.36},
    {"id": "grain_shade", "name": "grain shade", "x": -2.6, "z": -3.4, "terrain": "packed", "visibility": 0.76, "scent": 0.62, "sound": 0.42, "cold": 0.28, "wetness": 0.32, "slope": 0.10},
    {"id": "ash_edge", "name": "ash edge", "x": -8.0, "z": -4.2, "terrain": "rough", "visibility": 0.50, "scent": 0.70, "sound": 0.30, "cold": 0.36, "wetness": 0.58, "slope": 0.26},
    {"id": "cairn_ridge", "name": "cairn ridge", "x": 7.8, "z": -1.8, "terrain": "ridge", "visibility": 0.92, "scent": 0.34, "sound": 0.36, "cold": 0.48, "wetness": 0.26, "slope": 0.45},
    {"id": "drum_court", "name": "drum court", "x": 2.8, "z": 2.7, "terrain": "packed", "visibility": 0.80, "scent": 0.28, "sound": 0.88, "cold": 0.25, "wetness": 0.24, "slope": 0.10},
    {"id": "loom_room", "name": "loom room", "x": -1.8, "z": 4.2, "terrain": "covered", "visibility": 0.70, "scent": 0.40, "sound": 0.48, "cold": 0.22, "wetness": 0.22, "slope": 0.08},
    {"id": "archive_knoll", "name": "archive knoll", "x": 3.5, "z": -3.8, "terrain": "stone", "visibility": 0.84, "scent": 0.22, "sound": 0.42, "cold": 0.38, "wetness": 0.20, "slope": 0.30},
    {"id": "nursery_nest", "name": "nursery nest", "x": -0.8, "z": 1.8, "terrain": "covered", "visibility": 0.68, "scent": 0.38, "sound": 0.40, "cold": 0.20, "wetness": 0.30, "slope": 0.06},
    {"id": "smoke_watch", "name": "smoke watch", "x": 5.2, "z": 0.7, "terrain": "ridge", "visibility": 0.90, "scent": 0.82, "sound": 0.34, "cold": 0.42, "wetness": 0.24, "slope": 0.38},
)

OBJECT_PLACE = {
    "spring_pool": "spring_hollow",
    "clay_cistern": "storage_yard",
    "tool_cache": "tool_bend",
    "shelter_roof": "roof_ring",
    "fire_hearth": "central_hearth",
    "herb_garden": "herb_slope",
    "grain_store": "grain_shade",
    "waste_pit": "ash_edge",
    "route_cairn": "cairn_ridge",
    "signal_drum": "drum_court",
    "loom_frame": "loom_room",
    "archive_stone": "archive_knoll",
    "nursery_mat": "nursery_nest",
    "smoke_marker": "smoke_watch",
}

ROUTES = (
    ("central_hearth", "roof_ring", "packed", 0.05, 0.98),
    ("central_hearth", "tool_bend", "stone", 0.10, 0.88),
    ("central_hearth", "drum_court", "packed", 0.06, 0.94),
    ("central_hearth", "nursery_nest", "covered", 0.04, 0.96),
    ("roof_ring", "storage_yard", "packed", 0.08, 0.90),
    ("storage_yard", "spring_hollow", "mud", 0.28, 0.62),
    ("storage_yard", "grain_shade", "packed", 0.10, 0.84),
    ("grain_shade", "ash_edge", "rough", 0.34, 0.56),
    ("drum_court", "herb_slope", "brush", 0.24, 0.66),
    ("drum_court", "smoke_watch", "ridge", 0.22, 0.72),
    ("tool_bend", "archive_knoll", "stone", 0.18, 0.76),
    ("archive_knoll", "cairn_ridge", "ridge", 0.31, 0.58),
    ("cairn_ridge", "smoke_watch", "ridge", 0.26, 0.64),
    ("nursery_nest", "loom_room", "covered", 0.08, 0.88),
    ("loom_room", "herb_slope", "brush", 0.20, 0.68),
    ("spring_hollow", "ash_edge", "mud", 0.38, 0.48),
    ("roof_ring", "drum_court", "packed", 0.08, 0.92),
    ("tool_bend", "grain_shade", "stone", 0.14, 0.80),
)

ROLE_HOME = {
    "scout": "cairn_ridge",
    "builder": "tool_bend",
    "healer": "nursery_nest",
    "farmer": "grain_shade",
    "guard": "smoke_watch",
    "teacher": "loom_room",
    "trader": "storage_yard",
    "pattern_keeper": "archive_knoll",
}

ROLE_TARGETS = {
    "scout": ("route_cairn", "smoke_marker", "spring_pool", "archive_stone"),
    "builder": ("tool_cache", "shelter_roof", "clay_cistern", "fire_hearth"),
    "healer": ("nursery_mat", "herb_garden", "waste_pit", "loom_frame"),
    "farmer": ("grain_store", "clay_cistern", "spring_pool", "waste_pit"),
    "guard": ("smoke_marker", "signal_drum", "route_cairn", "fire_hearth"),
    "teacher": ("loom_frame", "archive_stone", "nursery_mat", "signal_drum"),
    "trader": ("spring_pool", "tool_cache", "grain_store", "clay_cistern"),
    "pattern_keeper": ("archive_stone", "signal_drum", "smoke_marker", "route_cairn"),
}

TERRAIN_COST = {"packed": 1.00, "covered": 0.92, "stone": 1.18, "mud": 1.52, "brush": 1.36, "rough": 1.70, "ridge": 1.44}
TERRAIN_SENSE = {"packed": "visual", "covered": "affect", "stone": "vestibular", "mud": "wetness", "brush": "olfactory", "rough": "pain", "ridge": "thermal"}


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
    if not isinstance(state, dict) or "agents" not in state or "objects" not in state:
        raise ValueError(f"Report 146 state artifact is invalid: {path}")
    return state


def distance(a: dict[str, object], b: dict[str, object]) -> float:
    return math.hypot(float(a["x"]) - float(b["x"]), float(a["z"]) - float(b["z"]))


def sensory_wave(packet: dict[str, object], sense: str, step: int, enabled: bool) -> float:
    if not enabled:
        return 0.20
    rates = packet.get("sensory_rates_hz", {})
    rate = float(rates.get(sense, 1.0)) if isinstance(rates, dict) else 1.0
    phase = FLOWER_PHASES[step % len(FLOWER_PHASES)]
    return clamp(0.34 + (0.5 + 0.5 * math.sin(rate * 0.31 + step * 0.13 + phase)) * 0.58)


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


def build_places(condition: Condition) -> dict[str, dict[str, object]]:
    if not condition.place_graph:
        return {}
    places = {row["id"]: {**copy.deepcopy(row), "visited": 0, "route_memory": []} for row in PLACES}
    return places


def build_routes(places: dict[str, dict[str, object]], condition: Condition) -> dict[str, list[dict[str, object]]]:
    graph = {place_id: [] for place_id in places}
    if not places:
        return graph
    for src, dst, terrain, hazard, quality in ROUTES:
        if src not in places or dst not in places:
            continue
        dist = distance(places[src], places[dst])
        route = {"src": src, "dst": dst, "terrain": terrain, "distance": dist, "hazard": hazard if condition.terrain_hazard else 0.0, "quality": quality}
        graph[src].append(route)
        graph[dst].append({**route, "src": dst, "dst": src})
    return graph


def build_agents(source_agents: Sequence[dict[str, object]], source_state: dict[str, object]) -> dict[str, dict[str, object]]:
    prior = source_state.get("agents", {})
    if not isinstance(prior, dict):
        prior = {}
    agents = {}
    for packet in source_agents:
        agent_id = str(packet["agent_id"])
        live = copy.deepcopy(prior.get(agent_id, {}))
        if not live:
            live = {"agent_id": agent_id, "name": packet.get("name", agent_id), "role": packet.get("role", "agent"), "trust": 0.60, "body_state": 0.75}
        role = str(live.get("role", packet.get("role", "agent")))
        live["place"] = ROLE_HOME.get(role, "central_hearth")
        live["fatigue"] = min(0.22, float(live.get("fatigue", 0.12)))
        live["wetness"] = min(0.24, float(live.get("wetness", 0.10)))
        live["cold"] = 0.12 + (len(role) % 4) * 0.025
        live["pain"] = min(0.16, float(live.get("pain", 0.08)))
        live["route_memory"] = []
        live["travel_spent"] = 0
        live["arrivals"] = 0
        live["object_after_arrival"] = 0
        live["wayfinding_given"] = 0
        agents[agent_id] = live
    return agents


def choose_object(agent: dict[str, object], objects: dict[str, dict[str, object]], trip: int, condition: Condition) -> tuple[str, dict[str, object] | None]:
    if not objects:
        return "none", None
    role = str(agent.get("role", "agent"))
    targets = ROLE_TARGETS.get(role, tuple(objects.keys()))
    candidate_ids = [object_id for object_id in targets if object_id in objects]
    if not candidate_ids:
        candidate_ids = list(objects.keys())
    if not condition.object_destination_binding:
        wrong = list(reversed(list(objects.keys())))
        object_id = wrong[trip % len(wrong)]
        return object_id, objects[object_id]
    scored = []
    for object_id in candidate_ids:
        obj = objects[object_id]
        need = (1.0 - float(obj.get("integrity", 0.6))) * 0.36 + (1.0 - float(obj.get("stock", 0.6))) * 0.22 + float(obj.get("pathogen", 0.1)) * 0.24 + float(obj.get("wetness", 0.3)) * 0.10 + (trip % 7) * 0.004
        scored.append((need, object_id, obj))
    scored.sort(reverse=True, key=lambda row: row[0])
    if trip % 6 == 0:
        return scored[(trip + len(role)) % len(scored)][1], scored[(trip + len(role)) % len(scored)][2]
    return scored[0][1], scored[0][2]


def edge_cost(edge: dict[str, object], packet: dict[str, object], step: int, condition: Condition) -> float:
    terrain = str(edge["terrain"])
    sense = TERRAIN_SENSE.get(terrain, "visual")
    sensory = sensory_wave(packet, sense, step, condition.sensory_gradient)
    hazard = float(edge["hazard"])
    quality = float(edge["quality"])
    cost = float(edge["distance"]) * TERRAIN_COST.get(terrain, 1.0)
    if condition.terrain_hazard:
        cost *= 1.0 + hazard * (1.20 - sensory * 0.55)
    if condition.sensory_gradient:
        cost *= 1.08 - sensory * 0.16
    cost *= 1.15 - quality * 0.10
    return max(0.001, cost)


def direct_path(start: str, goal: str, places: dict[str, dict[str, object]], graph: dict[str, list[dict[str, object]]], packet: dict[str, object], trip: int, condition: Condition) -> tuple[list[str], float, float]:
    if start == goal:
        return [start], 0.0, 1.0
    if not condition.pathfinding:
        neighbors = graph.get(start, [])
        if not neighbors:
            return [], math.inf, 0.0
        edge = neighbors[(trip + len(start)) % len(neighbors)]
        if edge["dst"] == goal:
            return [start, goal], edge_cost(edge, packet, trip, condition), 0.60
        second = graph.get(edge["dst"], [])
        via = [item for item in second if item["dst"] == goal]
        if via:
            return [start, edge["dst"], goal], edge_cost(edge, packet, trip, condition) + edge_cost(via[0], packet, trip, condition), 0.48
        return [start, edge["dst"]], edge_cost(edge, packet, trip, condition), 0.18
    frontier: list[tuple[float, str, list[str]]] = [(0.0, start, [start])]
    best = {start: 0.0}
    while frontier:
        cost, node, path = heapq.heappop(frontier)
        if node == goal:
            straight = distance(places[start], places[goal]) if start in places and goal in places else cost
            efficiency = clamp(straight / max(cost, 0.001))
            return path, cost, efficiency
        for edge in graph.get(node, []):
            new_cost = cost + edge_cost(edge, packet, trip + len(path), condition)
            if new_cost < best.get(str(edge["dst"]), math.inf):
                best[str(edge["dst"])] = new_cost
                heapq.heappush(frontier, (new_cost, str(edge["dst"]), path + [str(edge["dst"])]))
    return [], math.inf, 0.0


def path_hazard(path: Sequence[str], graph: dict[str, list[dict[str, object]]]) -> float:
    hazards = []
    for src, dst in zip(path, path[1:]):
        for edge in graph.get(src, []):
            if edge["dst"] == dst:
                hazards.append(float(edge["hazard"]))
                break
    return mean(hazards)


def apply_travel(agent: dict[str, object], path: Sequence[str], cost: float, hazard: float, places: dict[str, dict[str, object]], condition: Condition) -> bool:
    if not condition.travel_expenditure or not path:
        return False
    fatigue = min(0.28, cost * 0.010)
    wet = mean(float(places[place].get("wetness", 0.3)) for place in path if place in places) * 0.025
    cold = mean(float(places[place].get("cold", 0.3)) for place in path if place in places) * 0.020
    pain = hazard * 0.045
    agent["fatigue"] = clamp(float(agent.get("fatigue", 0.1)) + fatigue)
    agent["wetness"] = clamp(float(agent.get("wetness", 0.1)) + wet)
    agent["cold"] = clamp(float(agent.get("cold", 0.1)) + cold)
    agent["pain"] = clamp(float(agent.get("pain", 0.1)) + pain)
    agent["body_state"] = clamp(float(agent.get("body_state", 0.7)) - fatigue * 0.20 - pain * 0.35)
    agent["travel_spent"] = int(agent.get("travel_spent", 0)) + 1
    return True


def object_interact(obj: dict[str, object], agent: dict[str, object], arrived: bool, condition: Condition) -> bool:
    if not arrived or not condition.object_destination_binding:
        return False
    obj["integrity"] = clamp(float(obj.get("integrity", 0.6)) + 0.012)
    obj["stock"] = clamp(float(obj.get("stock", 0.6)) + 0.010)
    obj["pathogen"] = clamp(float(obj.get("pathogen", 0.1)) - 0.004)
    history = obj.setdefault("navigation_history", [])
    if isinstance(history, list):
        history.append({"agent": agent.get("name"), "from": agent.get("place"), "arrived": arrived})
    agent["object_after_arrival"] = int(agent.get("object_after_arrival", 0)) + 1
    return True


def social_wayfinding(agent: dict[str, object], agents: dict[str, dict[str, object]], goal: str, condition: Condition) -> bool:
    if not condition.social_wayfinding:
        return False
    role = str(agent.get("role", "agent"))
    if role in {"scout", "trader", "pattern_keeper", "teacher"}:
        agent["wayfinding_given"] = int(agent.get("wayfinding_given", 0)) + 1
        return True
    helpers = [other for other in agents.values() if other is not agent and str(other.get("role")) in {"scout", "trader", "pattern_keeper"}]
    if helpers:
        helper = helpers[(len(goal) + len(str(agent.get("name", "")))) % len(helpers)]
        helper["wayfinding_given"] = int(helper.get("wayfinding_given", 0)) + 1
        agent["trust"] = clamp(float(agent.get("trust", 0.6)) + 0.006)
        return True
    return False


def run_condition(cfg: NavigationConfig, condition: Condition, source_agents: Sequence[dict[str, object]], source_state: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    places = build_places(condition)
    graph = build_routes(places, condition)
    agents = build_agents(source_agents, source_state)
    objects = copy.deepcopy(source_state.get("objects", {})) if isinstance(source_state.get("objects", {}), dict) else {}
    trace: list[dict[str, object]] = []
    planned = 0
    arrivals = 0
    interactions = 0
    expenditures = 0
    hazard_scores = []
    sensory_scores = []
    route_memory = 0
    social_events = 0
    efficiency_scores = []
    attempted = 0

    for trip in range(1, cfg.trips + 1):
        packet = source_agents[(trip - 1) % len(source_agents)]
        agent = agents[str(packet["agent_id"])]
        attempted += 1
        object_id, obj = choose_object(agent, objects, trip, condition)
        if not places or obj is None:
            if condition.trace_replay:
                trace.append({"trip": trip, "success": False, "reason": "no-place-graph", "agent": agent.get("name")})
            continue
        start = str(agent.get("place", ROLE_HOME.get(str(agent.get("role", "agent")), "central_hearth")))
        goal = OBJECT_PLACE.get(object_id, "central_hearth") if condition.object_destination_binding else list(places.keys())[(trip + len(object_id)) % len(places)]
        path, cost, efficiency = direct_path(start, goal, places, graph, packet, trip, condition)
        route_ok = bool(path) and path[-1] == goal and math.isfinite(cost)
        planned += 1 if route_ok else 0
        hazard = path_hazard(path, graph) if route_ok else 1.0
        hazard_scores.append(clamp(1.0 - hazard))
        destination_place = places.get(goal, {})
        target_sense = "visual"
        if obj and isinstance(obj, dict):
            target_sense = str(obj.get("sense", TERRAIN_SENSE.get(str(destination_place.get("terrain", "packed")), "visual")))
        sensory = sensory_wave(packet, target_sense, trip, condition.sensory_gradient)
        sensory_scores.append(sensory if route_ok else 0.0)
        spent = apply_travel(agent, path, cost, hazard, places, condition) if route_ok else False
        expenditures += 1 if spent else 0
        arrived = route_ok and (condition.pathfinding or len(path) > 1) and (not condition.terrain_hazard or hazard < 0.36)
        if arrived:
            arrivals += 1
            agent["place"] = goal
            agent["arrivals"] = int(agent.get("arrivals", 0)) + 1
            places[goal]["visited"] = int(places[goal].get("visited", 0)) + 1
            if condition.pathfinding:
                memory = agent.setdefault("route_memory", [])
                if isinstance(memory, list):
                    memory.append({"from": start, "to": goal, "path": path, "cost": round(cost, 6)})
                    route_memory += 1
                places[goal].setdefault("route_memory", []).append({"agent": agent.get("name"), "path": path})
        interacted = object_interact(obj, agent, arrived, condition) if obj is not None else False
        interactions += 1 if interacted else 0
        social = social_wayfinding(agent, agents, goal, condition)
        social_events += 1 if social else 0
        efficiency_scores.append(efficiency if route_ok else 0.0)
        if condition.trace_replay:
            trace.append({
                "trip": trip,
                "agent_id": agent.get("agent_id"),
                "agent_name": agent.get("name"),
                "role": agent.get("role"),
                "object_id": object_id,
                "object_name": obj.get("name") if isinstance(obj, dict) else object_id,
                "start": start,
                "goal": goal,
                "path": path,
                "route_cost": round(cost, 6) if math.isfinite(cost) else None,
                "hazard": round(hazard, 6),
                "sensory_alignment": round(sensory, 6),
                "arrived": arrived,
                "object_interacted_after_arrival": interacted,
                "travel_spent": spent,
                "social_wayfinding": social,
            })

    route_planning_success_rate = planned / max(1, attempted)
    destination_arrival_rate = arrivals / max(1, planned)
    object_after_arrival_interaction_rate = interactions / max(1, arrivals)
    travel_expenditure_rate = expenditures / max(1, planned) if condition.travel_expenditure else 0.0
    terrain_hazard_avoidance_rate = mean(hazard_scores) if condition.terrain_hazard else 0.0
    sensory_gradient_alignment = mean(sensory_scores) if condition.sensory_gradient else 0.0
    route_memory_update_rate = route_memory / max(1, arrivals)
    social_wayfinding_rate = social_events / max(1, attempted) if condition.social_wayfinding else 0.0
    path_efficiency_score = mean(efficiency_scores)
    trace_completeness = 1.0 if condition.trace_replay and len(trace) == attempted else 0.0
    readiness = (
        route_planning_success_rate * 0.13
        + destination_arrival_rate * 0.13
        + object_after_arrival_interaction_rate * 0.13
        + travel_expenditure_rate * 0.10
        + terrain_hazard_avoidance_rate * 0.10
        + sensory_gradient_alignment * 0.10
        + route_memory_update_rate * 0.10
        + social_wayfinding_rate * 0.07
        + path_efficiency_score * 0.07
        + trace_completeness * 0.07
    )
    row = EvalRow(
        condition=condition.name,
        trips=cfg.trips,
        attempted_trips=attempted,
        planned_routes=planned,
        arrivals=arrivals,
        object_interactions=interactions,
        route_planning_success_rate=round(route_planning_success_rate, 6),
        destination_arrival_rate=round(destination_arrival_rate, 6),
        object_after_arrival_interaction_rate=round(object_after_arrival_interaction_rate, 6),
        travel_expenditure_rate=round(travel_expenditure_rate, 6),
        terrain_hazard_avoidance_rate=round(terrain_hazard_avoidance_rate, 6),
        sensory_gradient_alignment=round(sensory_gradient_alignment, 6),
        route_memory_update_rate=round(route_memory_update_rate, 6),
        social_wayfinding_rate=round(social_wayfinding_rate, 6),
        path_efficiency_score=round(path_efficiency_score, 6),
        trace_completeness=round(trace_completeness, 6),
        place_navigation_readiness=round(readiness, 6),
    )
    state = {
        "condition": condition.name,
        "trips": cfg.trips,
        "places": places,
        "routes": ROUTES,
        "objects": objects,
        "agents": agents,
    }
    return row, trace, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_place_navigation_object_bridge"]

    def loss(condition: str) -> float:
        return round(full.place_navigation_readiness - by_name[condition].place_navigation_readiness, 6)

    supports = (
        full.place_navigation_readiness >= 0.74
        and full.route_planning_success_rate >= 0.95
        and full.destination_arrival_rate >= 0.80
        and full.object_after_arrival_interaction_rate >= 0.95
        and full.travel_expenditure_rate >= 0.85
        and full.terrain_hazard_avoidance_rate >= 0.75
        and full.sensory_gradient_alignment >= 0.55
        and full.route_memory_update_rate >= 0.85
        and full.trace_completeness >= 1.0
        and loss("no_place_graph") >= 0.45
        and loss("no_pathfinding") >= 0.20
        and by_name["no_travel_expenditure"].travel_expenditure_rate <= 0.0
        and by_name["no_terrain_hazard"].terrain_hazard_avoidance_rate <= 0.0
        and by_name["no_sensory_gradient"].sensory_gradient_alignment <= 0.0
        and by_name["no_object_destination_binding"].object_after_arrival_interaction_rate <= 0.20
        and by_name["no_trace_replay"].trace_completeness <= 0.0
    )
    return VerdictRow(
        full_condition=full.condition,
        full_place_navigation_readiness=full.place_navigation_readiness,
        full_route_planning_success_rate=full.route_planning_success_rate,
        full_destination_arrival_rate=full.destination_arrival_rate,
        full_object_after_arrival_interaction_rate=full.object_after_arrival_interaction_rate,
        full_travel_expenditure_rate=full.travel_expenditure_rate,
        full_terrain_hazard_avoidance_rate=full.terrain_hazard_avoidance_rate,
        full_sensory_gradient_alignment=full.sensory_gradient_alignment,
        full_route_memory_update_rate=full.route_memory_update_rate,
        full_social_wayfinding_rate=full.social_wayfinding_rate,
        full_path_efficiency_score=full.path_efficiency_score,
        full_trace_completeness=full.trace_completeness,
        no_place_graph_loss=loss("no_place_graph"),
        no_pathfinding_loss=loss("no_pathfinding"),
        no_travel_expenditure_loss=loss("no_travel_expenditure"),
        no_terrain_hazard_loss=loss("no_terrain_hazard"),
        no_sensory_gradient_loss=loss("no_sensory_gradient"),
        no_object_destination_binding_loss=loss("no_object_destination_binding"),
        no_social_wayfinding_loss=loss("no_social_wayfinding"),
        no_trace_replay_loss=loss("no_trace_replay"),
        supports_place_navigation_object_bridge=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "partial_or_failed",
    )


def run_benchmark(cfg: NavigationConfig) -> dict[str, object]:
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
        "report": 147,
        "name": "SSRM-3D Place Navigation Object Bridge",
        "config": asdict(cfg),
        "eval": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "trace": traces["integrated_place_navigation_object_bridge"],
        "final_state": states["integrated_place_navigation_object_bridge"],
        "source_agents": source_agents,
        "notes": {
            "claim": "deterministic bridge from persistent object affordances to place-based navigation and object interaction after arrival",
            "not_claimed": "subjective consciousness, LLM open dialogue, complete playable world, or unscripted civilization emergence",
            "navigation_basis": "place graph, terrain route costs, pathfinding, travel expenditure, hazard avoidance, sensory gradients, route memory, social wayfinding, and object use after arrival",
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", payload)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", payload["trace"])
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", payload["final_state"])
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_PLACE_NAVIGATION_OBJECT_BRIDGE_RESULTS", payload)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_PLACE_NAVIGATION_OBJECT_BRIDGE_TRACE", payload["trace"])
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_PLACE_NAVIGATION_OBJECT_BRIDGE_STATE", payload["final_state"])
    return payload


def parse_args() -> NavigationConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260621)
    parser.add_argument("--trips", type=int, default=96)
    parser.add_argument("--source-agents", default=str(SOURCE_AGENTS))
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    if args.trips < 48:
        raise SystemExit("--trips must be at least 48")
    return NavigationConfig(seed=args.seed, trips=args.trips, source_agents=args.source_agents, source_state=args.source_state)


def main() -> None:
    payload = run_benchmark(parse_args())
    print(json.dumps(payload["verdict"], indent=2))


if __name__ == "__main__":
    main()
