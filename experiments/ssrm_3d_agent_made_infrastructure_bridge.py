#!/usr/bin/env python3
"""Agent-made infrastructure bridge for SSRM-3D place/object worlds.

This deterministic bridge moves past Report 147's fixed place graph. Agents now
build and maintain route/object infrastructure: roads, bridges, drainage,
watch posts, caches, signs, shelter walks, and water channels. Projects consume
materials, require social labor, mutate route costs/hazards, affect object
access, decay without maintenance, and leave persistent histories.
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
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_place_navigation_object_bridge_state.json"
PREFIX = "ssrm_3d_agent_made_infrastructure_bridge"
FLOWER_PHASES = (0.0, math.tau / 6.0, math.tau / 3.0, math.tau / 2.0, math.tau * 2.0 / 3.0, math.tau * 5.0 / 6.0, math.tau)
SENSES = ("visual", "audio", "olfactory", "thermal", "wetness", "pain", "affect", "vestibular")


@dataclass(frozen=True)
class InfrastructureConfig:
    seed: int = 20260622
    cycles: int = 84
    source_agents: str = str(SOURCE_AGENTS)
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    infrastructure_projects: bool
    material_expenditure: bool
    social_labor: bool
    route_mutation: bool
    maintenance_decay: bool
    sensory_site_selection: bool
    object_route_coupling: bool
    trace_replay: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    cycles: int
    project_count: int
    completed_projects: int
    project_completion_rate: float
    material_expenditure_rate: float
    social_labor_coordination_rate: float
    route_mutation_rate: float
    route_cost_reduction_score: float
    hazard_reduction_score: float
    maintenance_sustainability: float
    sensory_site_alignment: float
    object_route_coupling_rate: float
    accessibility_gain: float
    infrastructure_history_persistence: float
    trace_completeness: float
    infrastructure_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_infrastructure_readiness: float
    full_project_completion_rate: float
    full_material_expenditure_rate: float
    full_social_labor_coordination_rate: float
    full_route_mutation_rate: float
    full_route_cost_reduction_score: float
    full_hazard_reduction_score: float
    full_maintenance_sustainability: float
    full_sensory_site_alignment: float
    full_object_route_coupling_rate: float
    full_accessibility_gain: float
    full_infrastructure_history_persistence: float
    full_trace_completeness: float
    no_infrastructure_projects_loss: float
    no_material_expenditure_loss: float
    no_social_labor_loss: float
    no_route_mutation_loss: float
    no_maintenance_decay_loss: float
    no_sensory_site_selection_loss: float
    no_object_route_coupling_loss: float
    no_trace_replay_loss: float
    supports_agent_made_infrastructure_bridge: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_agent_made_infrastructure", True, True, True, True, True, True, True, True),
    Condition("no_infrastructure_projects", False, True, True, True, True, True, True, True),
    Condition("no_material_expenditure", True, False, True, True, True, True, True, True),
    Condition("no_social_labor", True, True, False, True, True, True, True, True),
    Condition("no_route_mutation", True, True, True, False, True, True, True, True),
    Condition("no_maintenance_decay", True, True, True, True, False, True, True, True),
    Condition("no_sensory_site_selection", True, True, True, True, True, False, True, True),
    Condition("no_object_route_coupling", True, True, True, True, True, True, False, True),
    Condition("no_trace_replay", True, True, True, True, True, True, True, False),
)

PROJECTS = (
    {
        "id": "mud_causeway",
        "name": "mud causeway",
        "route": ("storage_yard", "spring_hollow"),
        "object": "spring_pool",
        "kind": "road",
        "sense": "wetness",
        "roles": ("builder", "scout", "trader", "farmer"),
        "materials": {"wood": 5, "stone": 4, "fiber": 2},
        "labor": 8.0,
        "cost_delta": -0.23,
        "hazard_delta": -0.18,
        "access_delta": 0.15,
    },
    {
        "id": "ash_drain",
        "name": "ash drainage trench",
        "route": ("grain_shade", "ash_edge"),
        "object": "waste_pit",
        "kind": "drainage",
        "sense": "pain",
        "roles": ("healer", "farmer", "builder"),
        "materials": {"ash": 6, "stone": 3, "wood": 2},
        "labor": 7.0,
        "cost_delta": -0.18,
        "hazard_delta": -0.22,
        "access_delta": 0.13,
    },
    {
        "id": "ridge_steps",
        "name": "ridge stone steps",
        "route": ("archive_knoll", "cairn_ridge"),
        "object": "route_cairn",
        "kind": "stairs",
        "sense": "vestibular",
        "roles": ("scout", "guard", "builder", "pattern_keeper"),
        "materials": {"stone": 7, "fiber": 2},
        "labor": 8.5,
        "cost_delta": -0.20,
        "hazard_delta": -0.20,
        "access_delta": 0.12,
    },
    {
        "id": "smoke_watchtower",
        "name": "smoke watchtower",
        "route": ("drum_court", "smoke_watch"),
        "object": "smoke_marker",
        "kind": "watch",
        "sense": "olfactory",
        "roles": ("guard", "scout", "pattern_keeper", "builder"),
        "materials": {"wood": 7, "resin": 4, "fiber": 3},
        "labor": 9.0,
        "cost_delta": -0.12,
        "hazard_delta": -0.23,
        "access_delta": 0.14,
    },
    {
        "id": "covered_walk",
        "name": "covered nursery walk",
        "route": ("nursery_nest", "loom_room"),
        "object": "nursery_mat",
        "kind": "covered_walk",
        "sense": "affect",
        "roles": ("teacher", "healer", "builder"),
        "materials": {"fiber": 6, "wood": 4, "hide": 2},
        "labor": 7.5,
        "cost_delta": -0.16,
        "hazard_delta": -0.12,
        "access_delta": 0.16,
    },
    {
        "id": "herb_switchback",
        "name": "herb slope switchback",
        "route": ("loom_room", "herb_slope"),
        "object": "herb_garden",
        "kind": "switchback",
        "sense": "olfactory",
        "roles": ("healer", "teacher", "scout", "builder"),
        "materials": {"stone": 4, "wood": 3, "fiber": 3},
        "labor": 8.0,
        "cost_delta": -0.21,
        "hazard_delta": -0.17,
        "access_delta": 0.15,
    },
    {
        "id": "tool_sledge_path",
        "name": "tool sledge path",
        "route": ("central_hearth", "tool_bend"),
        "object": "tool_cache",
        "kind": "haul_path",
        "sense": "visual",
        "roles": ("builder", "trader", "guard"),
        "materials": {"wood": 5, "stone": 5, "clay": 2},
        "labor": 7.0,
        "cost_delta": -0.18,
        "hazard_delta": -0.11,
        "access_delta": 0.13,
    },
    {
        "id": "archive_waystones",
        "name": "archive waystones",
        "route": ("tool_bend", "archive_knoll"),
        "object": "archive_stone",
        "kind": "signage",
        "sense": "visual",
        "roles": ("pattern_keeper", "teacher", "scout"),
        "materials": {"stone": 5, "charcoal": 3, "clay": 2},
        "labor": 6.0,
        "cost_delta": -0.10,
        "hazard_delta": -0.10,
        "access_delta": 0.18,
    },
    {
        "id": "water_channel",
        "name": "cistern water channel",
        "route": ("storage_yard", "spring_hollow"),
        "object": "clay_cistern",
        "kind": "channel",
        "sense": "wetness",
        "roles": ("farmer", "builder", "trader"),
        "materials": {"clay": 7, "stone": 4, "wood": 2},
        "labor": 8.5,
        "cost_delta": -0.12,
        "hazard_delta": -0.08,
        "access_delta": 0.20,
    },
    {
        "id": "drum_resonance_posts",
        "name": "drum resonance posts",
        "route": ("central_hearth", "drum_court"),
        "object": "signal_drum",
        "kind": "signal",
        "sense": "audio",
        "roles": ("pattern_keeper", "guard", "teacher"),
        "materials": {"wood": 4, "fiber": 4, "resin": 2},
        "labor": 6.5,
        "cost_delta": -0.08,
        "hazard_delta": -0.13,
        "access_delta": 0.17,
    },
)

ROLE_MATERIALS = {
    "scout": {"wood": 18, "stone": 16, "fiber": 14, "resin": 8, "charcoal": 8, "clay": 8},
    "builder": {"wood": 60, "stone": 54, "fiber": 36, "clay": 32, "resin": 8, "hide": 6, "ash": 8},
    "healer": {"wood": 16, "stone": 14, "fiber": 28, "hide": 12, "ash": 24, "resin": 8},
    "farmer": {"wood": 24, "stone": 20, "fiber": 18, "clay": 34, "ash": 18, "hide": 4},
    "guard": {"wood": 32, "stone": 24, "fiber": 18, "resin": 28, "charcoal": 18, "clay": 8},
    "teacher": {"wood": 18, "stone": 16, "fiber": 36, "hide": 18, "charcoal": 14, "resin": 8, "clay": 8},
    "trader": {"wood": 34, "stone": 28, "fiber": 24, "clay": 24, "resin": 10, "hide": 8},
    "pattern_keeper": {"wood": 20, "stone": 28, "fiber": 24, "resin": 22, "charcoal": 24, "clay": 16},
}


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
    if not isinstance(state, dict) or "places" not in state or "objects" not in state or "agents" not in state:
        raise ValueError(f"Report 147 state artifact is invalid: {path}")
    return state


def sensory_wave(packet: dict[str, object], sense: str, cycle: int, enabled: bool) -> float:
    if not enabled:
        return 0.18
    rates = packet.get("sensory_rates_hz", {})
    rate = float(rates.get(sense, 1.0)) if isinstance(rates, dict) else 1.0
    phase = FLOWER_PHASES[cycle % len(FLOWER_PHASES)]
    return clamp(0.34 + (0.5 + 0.5 * math.sin(rate * 0.27 + cycle * 0.15 + phase)) * 0.58)


def route_key(route: Sequence[str]) -> str:
    return "->".join(route)


def build_routes(source_state: dict[str, object]) -> dict[str, dict[str, object]]:
    places = source_state.get("places", {})
    route_rows = source_state.get("routes", [])
    routes: dict[str, dict[str, object]] = {}
    for row in route_rows:
        if not isinstance(row, list) and not isinstance(row, tuple):
            continue
        if len(row) < 5:
            continue
        src, dst, terrain, hazard, quality = row[:5]
        if src not in places or dst not in places:
            continue
        distance = math.hypot(float(places[src]["x"]) - float(places[dst]["x"]), float(places[src]["z"]) - float(places[dst]["z"]))
        data = {
            "src": src,
            "dst": dst,
            "terrain": terrain,
            "base_distance": round(distance, 6),
            "cost_multiplier": 1.0,
            "hazard": float(hazard),
            "quality": float(quality),
            "built_projects": [],
            "closures": [],
            "maintenance_load": 0.0,
        }
        routes[route_key((str(src), str(dst)))] = copy.deepcopy(data)
        reverse = copy.deepcopy(data)
        reverse["src"] = dst
        reverse["dst"] = src
        routes[route_key((str(dst), str(src)))] = reverse
    return routes


def build_projects(condition: Condition) -> dict[str, dict[str, object]]:
    if not condition.infrastructure_projects:
        return {}
    projects = {}
    for project in PROJECTS:
        data = copy.deepcopy(project)
        data["progress"] = 0.0
        data["integrity"] = 0.0
        data["completed"] = False
        data["maintained"] = 0
        data["spent_events"] = 0
        data["labor_events"] = 0
        data["history"] = []
        projects[data["id"]] = data
    return projects


def build_agents(source_agents: Sequence[dict[str, object]], source_state: dict[str, object]) -> dict[str, dict[str, object]]:
    prior = source_state.get("agents", {})
    if not isinstance(prior, dict):
        prior = {}
    agents = {}
    for packet in source_agents:
        agent_id = str(packet["agent_id"])
        live = copy.deepcopy(prior.get(agent_id, {}))
        if not live:
            live = {"agent_id": agent_id, "name": packet.get("name", agent_id), "role": packet.get("role", "agent"), "trust": 0.64, "body_state": 0.75}
        role = str(live.get("role", packet.get("role", "agent")))
        live["materials"] = copy.deepcopy(ROLE_MATERIALS.get(role, {"wood": 12, "stone": 12, "fiber": 12}))
        live["infrastructure_memory"] = []
        live["labor_given"] = 0
        live["materials_spent"] = 0
        live["maintenance_given"] = 0
        agents[agent_id] = live
    return agents


def choose_project(agent: dict[str, object], projects: dict[str, dict[str, object]], cycle: int, condition: Condition) -> dict[str, object] | None:
    if not projects:
        return None
    role = str(agent.get("role", "agent"))
    candidates = [project for project in projects.values() if role in project["roles"]]
    if not candidates:
        candidates = list(projects.values())
    scored = []
    for project in candidates:
        unfinished = 1.0 - float(project["progress"])
        decay_need = 1.0 - float(project["integrity"])
        role_bonus = 0.12 if role == project["roles"][0] else 0.05
        score = unfinished * 0.62 + decay_need * 0.20 + role_bonus + ((cycle + len(project["id"])) % 5) * 0.006
        if condition.sensory_site_selection:
            score += sensory_wave({}, str(project["sense"]), cycle, True) * 0.06
        scored.append((score, project))
    scored.sort(reverse=True, key=lambda row: row[0])
    if cycle % 9 == 0 and len(scored) > 1:
        return scored[(cycle + len(role)) % len(scored)][1]
    return scored[0][1]


def spend_materials(agent: dict[str, object], project: dict[str, object], condition: Condition) -> float:
    if not condition.material_expenditure:
        return 0.0
    materials = agent.setdefault("materials", {})
    if not isinstance(materials, dict):
        return 0.0
    spent = 0
    required = project["materials"]
    for resource, amount in required.items():
        available = int(materials.get(resource, 0))
        if available <= 0:
            continue
        unit = max(1, math.ceil(int(amount) / 4))
        use = min(available, unit)
        materials[resource] = available - use
        spent += use
    agent["materials_spent"] = int(agent.get("materials_spent", 0)) + spent
    project["spent_events"] = int(project.get("spent_events", 0)) + (1 if spent else 0)
    return spent / max(1.0, sum(int(value) for value in required.values()))


def labor_multiplier(agent: dict[str, object], agents: dict[str, dict[str, object]], project: dict[str, object], condition: Condition) -> tuple[float, bool]:
    if not condition.social_labor:
        return 0.55, False
    role = str(agent.get("role", "agent"))
    helpers = [other for other in agents.values() if other is not agent and str(other.get("role", "agent")) in project["roles"]]
    coordination = bool(helpers)
    trust = float(agent.get("trust", 0.6))
    multiplier = 0.82 + min(0.22, len(helpers) * 0.035) + trust * 0.10
    agent["labor_given"] = int(agent.get("labor_given", 0)) + 1
    project["labor_events"] = int(project.get("labor_events", 0)) + 1
    if coordination:
        helper = helpers[(len(project["id"]) + int(project["labor_events"])) % len(helpers)]
        helper["labor_given"] = int(helper.get("labor_given", 0)) + 1
        helper["trust"] = clamp(float(helper.get("trust", 0.6)) + 0.004)
    return multiplier, coordination


def mutate_route(project: dict[str, object], routes: dict[str, dict[str, object]], condition: Condition) -> bool:
    if not condition.route_mutation:
        return False
    src, dst = project["route"]
    changed = False
    for key in (route_key((src, dst)), route_key((dst, src))):
        route = routes.get(key)
        if not route:
            continue
        route["cost_multiplier"] = clamp(float(route.get("cost_multiplier", 1.0)) + float(project["cost_delta"]), 0.45, 1.25)
        route["hazard"] = clamp(float(route.get("hazard", 0.2)) + float(project["hazard_delta"]), 0.0, 1.0)
        route["quality"] = clamp(float(route.get("quality", 0.6)) + 0.12)
        if project["id"] not in route["built_projects"]:
            route["built_projects"].append(project["id"])
        changed = True
    return changed


def couple_object(project: dict[str, object], objects: dict[str, dict[str, object]], condition: Condition) -> bool:
    if not condition.object_route_coupling:
        return False
    obj = objects.get(project["object"])
    if not isinstance(obj, dict):
        return False
    obj["accessibility"] = clamp(float(obj.get("accessibility", 0.50)) + float(project["access_delta"]))
    obj["integrity"] = clamp(float(obj.get("integrity", 0.6)) + 0.012)
    obj.setdefault("infrastructure_links", []).append(project["id"])
    return True


def decay_infrastructure(projects: dict[str, dict[str, object]], routes: dict[str, dict[str, object]], condition: Condition) -> int:
    if not condition.maintenance_decay:
        return 0
    decayed = 0
    for project in projects.values():
        if not project.get("completed"):
            continue
        wear = 0.010 + (len(project["id"]) % 4) * 0.002
        project["integrity"] = clamp(float(project["integrity"]) - wear)
        if float(project["integrity"]) < 0.72:
            decayed += 1
            src, dst = project["route"]
            for key in (route_key((src, dst)), route_key((dst, src))):
                route = routes.get(key)
                if route:
                    route["maintenance_load"] = clamp(float(route.get("maintenance_load", 0.0)) + 0.03)
    return decayed


def maintain_project(agent: dict[str, object], project: dict[str, object], condition: Condition) -> bool:
    if not condition.maintenance_decay or not project.get("completed") or float(project.get("integrity", 0.0)) >= 0.78:
        return False
    project["integrity"] = clamp(float(project["integrity"]) + 0.045)
    project["maintained"] = int(project.get("maintained", 0)) + 1
    agent["maintenance_given"] = int(agent.get("maintenance_given", 0)) + 1
    return True


def run_condition(cfg: InfrastructureConfig, condition: Condition, source_agents: Sequence[dict[str, object]], source_state: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    projects = build_projects(condition)
    agents = build_agents(source_agents, source_state)
    objects = copy.deepcopy(source_state.get("objects", {})) if isinstance(source_state.get("objects", {}), dict) else {}
    places = copy.deepcopy(source_state.get("places", {})) if isinstance(source_state.get("places", {}), dict) else {}
    routes = build_routes(source_state)
    trace: list[dict[str, object]] = []
    completed = 0
    material_events = 0
    labor_events = 0
    route_mutations = 0
    object_couplings = 0
    sensory_scores: list[float] = []
    maintenance_events = 0
    decay_events = 0
    baseline_costs = {key: float(route["cost_multiplier"]) for key, route in routes.items()}
    baseline_hazards = {key: float(route["hazard"]) for key, route in routes.items()}

    for cycle in range(1, cfg.cycles + 1):
        decay_events += decay_infrastructure(projects, routes, condition)
        packet = source_agents[(cycle - 1) % len(source_agents)]
        agent = agents[str(packet["agent_id"])]
        project = choose_project(agent, projects, cycle, condition)
        if project is None:
            if condition.trace_replay:
                trace.append({"cycle": cycle, "success": False, "reason": "no-infrastructure-projects", "agent": agent.get("name")})
            continue
        maintained = maintain_project(agent, project, condition)
        maintenance_events += 1 if maintained else 0
        sensory = sensory_wave(packet, str(project["sense"]), cycle, condition.sensory_site_selection)
        sensory_scores.append(sensory)
        material_fraction = spend_materials(agent, project, condition)
        material_events += 1 if material_fraction > 0 else 0
        labor, coordinated = labor_multiplier(agent, agents, project, condition)
        labor_events += 1 if coordinated else 0
        progress_gain = 0.055 * labor + material_fraction * 0.22 + sensory * 0.020
        if not condition.material_expenditure:
            progress_gain *= 0.48
        if not condition.social_labor:
            progress_gain *= 0.62
        project["progress"] = clamp(float(project["progress"]) + progress_gain)
        project["integrity"] = clamp(float(project["integrity"]) + progress_gain * 0.60)
        just_completed = False
        route_changed = False
        object_changed = False
        if not project.get("completed") and float(project["progress"]) >= 1.0:
            project["completed"] = True
            project["integrity"] = max(float(project["integrity"]), 0.82)
            just_completed = True
            completed += 1
            route_changed = mutate_route(project, routes, condition)
            object_changed = couple_object(project, objects, condition)
            route_mutations += 1 if route_changed else 0
            object_couplings += 1 if object_changed else 0
        project.setdefault("history", []).append({
            "cycle": cycle,
            "agent": agent.get("name"),
            "role": agent.get("role"),
            "material_fraction": round(material_fraction, 6),
            "coordinated": coordinated,
            "sensory_alignment": round(sensory, 6),
            "progress": round(float(project["progress"]), 6),
            "maintained": maintained,
            "completed": just_completed,
        })
        memory = agent.setdefault("infrastructure_memory", [])
        if isinstance(memory, list):
            memory.append({"cycle": cycle, "project": project["id"], "progress": round(float(project["progress"]), 6), "completed": just_completed})
        if condition.trace_replay:
            trace.append({
                "cycle": cycle,
                "agent_id": agent.get("agent_id"),
                "agent_name": agent.get("name"),
                "role": agent.get("role"),
                "project_id": project["id"],
                "project_name": project["name"],
                "route": list(project["route"]),
                "object": project["object"],
                "kind": project["kind"],
                "material_fraction": round(material_fraction, 6),
                "social_labor": coordinated,
                "sensory_alignment": round(sensory, 6),
                "progress": round(float(project["progress"]), 6),
                "integrity": round(float(project["integrity"]), 6),
                "maintained": maintained,
                "completed_now": just_completed,
                "route_mutated": route_changed,
                "object_coupled": object_changed,
            })

    project_count = len(projects)
    completed_projects = sum(1 for project in projects.values() if project.get("completed"))
    project_completion_rate = completed_projects / max(1, project_count)
    material_expenditure_rate = material_events / max(1, cfg.cycles) if condition.material_expenditure else 0.0
    social_labor_coordination_rate = labor_events / max(1, cfg.cycles) if condition.social_labor else 0.0
    route_mutation_rate = route_mutations / max(1, completed_projects) if condition.route_mutation else 0.0
    route_cost_reduction_score = mean(clamp(baseline_costs[key] - float(route["cost_multiplier"])) for key, route in routes.items()) if condition.route_mutation else 0.0
    hazard_reduction_score = mean(clamp(baseline_hazards[key] - float(route["hazard"])) for key, route in routes.items()) if condition.route_mutation else 0.0
    if condition.maintenance_decay:
        completed_integrity = [float(project["integrity"]) for project in projects.values() if project.get("completed")]
        maintenance_sustainability = mean(completed_integrity) if completed_integrity else 0.0
    else:
        maintenance_sustainability = 0.0
    sensory_site_alignment = mean(sensory_scores) if condition.sensory_site_selection else 0.0
    object_route_coupling_rate = object_couplings / max(1, completed_projects) if condition.object_route_coupling else 0.0
    accessibility_values = [float(obj.get("accessibility", 0.50)) for obj in objects.values() if isinstance(obj, dict)]
    accessibility_gain = clamp(mean(accessibility_values) - 0.50) if condition.object_route_coupling and accessibility_values else 0.0
    infrastructure_history_persistence = mean(1.0 if project.get("history") else 0.0 for project in projects.values()) if projects else 0.0
    trace_completeness = 1.0 if condition.trace_replay and len(trace) == cfg.cycles else 0.0
    readiness = (
        project_completion_rate * 0.13
        + material_expenditure_rate * 0.10
        + social_labor_coordination_rate * 0.10
        + route_mutation_rate * 0.13
        + route_cost_reduction_score * 0.10
        + hazard_reduction_score * 0.10
        + maintenance_sustainability * 0.09
        + sensory_site_alignment * 0.08
        + object_route_coupling_rate * 0.08
        + accessibility_gain * 0.04
        + infrastructure_history_persistence * 0.07
        + trace_completeness * 0.08
    )
    row = EvalRow(
        condition=condition.name,
        cycles=cfg.cycles,
        project_count=project_count,
        completed_projects=completed_projects,
        project_completion_rate=round(project_completion_rate, 6),
        material_expenditure_rate=round(material_expenditure_rate, 6),
        social_labor_coordination_rate=round(social_labor_coordination_rate, 6),
        route_mutation_rate=round(route_mutation_rate, 6),
        route_cost_reduction_score=round(route_cost_reduction_score, 6),
        hazard_reduction_score=round(hazard_reduction_score, 6),
        maintenance_sustainability=round(maintenance_sustainability, 6),
        sensory_site_alignment=round(sensory_site_alignment, 6),
        object_route_coupling_rate=round(object_route_coupling_rate, 6),
        accessibility_gain=round(accessibility_gain, 6),
        infrastructure_history_persistence=round(infrastructure_history_persistence, 6),
        trace_completeness=round(trace_completeness, 6),
        infrastructure_readiness=round(readiness, 6),
    )
    state = {
        "condition": condition.name,
        "cycles": cfg.cycles,
        "places": places,
        "routes": routes,
        "objects": objects,
        "agents": agents,
        "projects": projects,
    }
    return row, trace, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_agent_made_infrastructure"]

    def loss(condition: str) -> float:
        return round(full.infrastructure_readiness - by_name[condition].infrastructure_readiness, 6)

    supports = (
        full.infrastructure_readiness >= 0.70
        and full.project_completion_rate >= 0.85
        and full.material_expenditure_rate >= 0.55
        and full.social_labor_coordination_rate >= 0.70
        and full.route_mutation_rate >= 0.85
        and full.route_cost_reduction_score >= 0.05
        and full.hazard_reduction_score >= 0.05
        and full.maintenance_sustainability >= 0.65
        and full.sensory_site_alignment >= 0.55
        and full.object_route_coupling_rate >= 0.85
        and full.infrastructure_history_persistence >= 1.0
        and full.trace_completeness >= 1.0
        and loss("no_infrastructure_projects") >= 0.45
        and by_name["no_material_expenditure"].material_expenditure_rate <= 0.0
        and by_name["no_social_labor"].social_labor_coordination_rate <= 0.0
        and by_name["no_route_mutation"].route_mutation_rate <= 0.0
        and by_name["no_maintenance_decay"].maintenance_sustainability <= 0.0
        and by_name["no_sensory_site_selection"].sensory_site_alignment <= 0.0
        and by_name["no_object_route_coupling"].object_route_coupling_rate <= 0.0
        and by_name["no_trace_replay"].trace_completeness <= 0.0
    )
    return VerdictRow(
        full_condition=full.condition,
        full_infrastructure_readiness=full.infrastructure_readiness,
        full_project_completion_rate=full.project_completion_rate,
        full_material_expenditure_rate=full.material_expenditure_rate,
        full_social_labor_coordination_rate=full.social_labor_coordination_rate,
        full_route_mutation_rate=full.route_mutation_rate,
        full_route_cost_reduction_score=full.route_cost_reduction_score,
        full_hazard_reduction_score=full.hazard_reduction_score,
        full_maintenance_sustainability=full.maintenance_sustainability,
        full_sensory_site_alignment=full.sensory_site_alignment,
        full_object_route_coupling_rate=full.object_route_coupling_rate,
        full_accessibility_gain=full.accessibility_gain,
        full_infrastructure_history_persistence=full.infrastructure_history_persistence,
        full_trace_completeness=full.trace_completeness,
        no_infrastructure_projects_loss=loss("no_infrastructure_projects"),
        no_material_expenditure_loss=loss("no_material_expenditure"),
        no_social_labor_loss=loss("no_social_labor"),
        no_route_mutation_loss=loss("no_route_mutation"),
        no_maintenance_decay_loss=loss("no_maintenance_decay"),
        no_sensory_site_selection_loss=loss("no_sensory_site_selection"),
        no_object_route_coupling_loss=loss("no_object_route_coupling"),
        no_trace_replay_loss=loss("no_trace_replay"),
        supports_agent_made_infrastructure_bridge=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "partial_or_failed",
    )


def run_benchmark(cfg: InfrastructureConfig) -> dict[str, object]:
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
        "report": 148,
        "name": "SSRM-3D Agent-Made Infrastructure Bridge",
        "config": asdict(cfg),
        "eval": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "trace": traces["integrated_agent_made_infrastructure"],
        "final_state": states["integrated_agent_made_infrastructure"],
        "source_agents": source_agents,
        "notes": {
            "claim": "deterministic bridge from fixed place navigation to agent-made infrastructure that mutates route and object access histories",
            "not_claimed": "subjective consciousness, LLM open dialogue, complete playable world, or unscripted civilization emergence",
            "infrastructure_basis": "projects, material expenditure, social labor, route cost/hazard mutation, maintenance decay, sensory site selection, object-route coupling, and replay traces",
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", payload)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", payload["trace"])
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", payload["final_state"])
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_AGENT_MADE_INFRASTRUCTURE_BRIDGE_RESULTS", payload)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_AGENT_MADE_INFRASTRUCTURE_BRIDGE_TRACE", payload["trace"])
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_AGENT_MADE_INFRASTRUCTURE_BRIDGE_STATE", payload["final_state"])
    return payload


def parse_args() -> InfrastructureConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260622)
    parser.add_argument("--cycles", type=int, default=84)
    parser.add_argument("--source-agents", default=str(SOURCE_AGENTS))
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    if args.cycles < 48:
        raise SystemExit("--cycles must be at least 48")
    return InfrastructureConfig(seed=args.seed, cycles=args.cycles, source_agents=args.source_agents, source_state=args.source_state)


def main() -> None:
    payload = run_benchmark(parse_args())
    print(json.dumps(payload["verdict"], indent=2))


if __name__ == "__main__":
    main()
