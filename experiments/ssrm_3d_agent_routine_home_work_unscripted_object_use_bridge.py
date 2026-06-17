#!/usr/bin/env python3
"""Agent routines, persistent homes, work projects, and unscripted object use.

Report 183 consumes the Report 182 continuity state and adds deterministic
autonomous routine ticks. Agents have homes, projects, need pressure, local
object affordances, route movement, rest recovery, social-continuity bias,
frequency/flower coupling, and replayable browser-ready autonomy events.

No LLMs are called. This is deterministic autonomy substrate, not a claim of
complete gameplay, subjective consciousness, moral patienthood, or natural
language emergence.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
from collections import deque
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_agent_routine_home_work_unscripted_object_use_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_object_persistence_promise_relationship_continuity_bridge_state.json"

PHASES = ("dawn_home", "morning_work", "midday_care", "afternoon_work", "dusk_social", "night_rest")

AGENT_PROFILES = {
    "Ari": {
        "home": "hearth_vale",
        "work_place": "clay_basin",
        "project_id": "repair_clay_latch",
        "project_need": "unfinished_task",
        "work_object": "clay_patch_kit",
        "rest_object": "ember_blanket",
        "social_object": "reed_cup",
    },
    "Fay": {
        "home": "moss_hollow",
        "work_place": "moss_hollow",
        "project_id": "dry_moss_bedding",
        "project_need": "fatigue",
        "work_object": "dry_cloak",
        "rest_object": "dry_cloak",
        "social_object": "reed_cup",
    },
    "Milo": {
        "home": "stone_ridge",
        "work_place": "stone_ridge",
        "project_id": "ridge_warning_watch",
        "project_need": "safety_concern",
        "work_object": "signal_shell",
        "rest_object": "ember_blanket",
        "social_object": "signal_shell",
    },
}

OBJECT_ACTIONS = {
    "clay_patch_kit": ("work", "repair", "project"),
    "dry_cloak": ("rest", "work", "dry"),
    "ember_blanket": ("rest", "comfort", "home"),
    "reed_cup": ("care", "drink", "social"),
    "signal_shell": ("work", "watch", "social"),
    "glass_lens": ("explore", "safety", "work"),
}

WEIGHTS = {
    "home_place_binding_rate": 0.08,
    "routine_clock_progression_rate": 0.08,
    "work_project_progress_rate": 0.10,
    "need_driven_action_selection_rate": 0.10,
    "unscripted_object_use_rate": 0.09,
    "persistent_object_state_rate": 0.08,
    "place_traversal_rate": 0.08,
    "frequency_flower_coupling_rate": 0.07,
    "social_continuity_modulation_rate": 0.07,
    "rest_recovery_rate": 0.08,
    "browser_autonomy_tick_rate": 0.06,
    "replay_timeline_integrity_rate": 0.05,
    "privacy_preservation_rate": 0.03,
    "trace_integrity": 0.03,
}


@dataclass(frozen=True)
class RoutineConfig:
    seed: int = 20260727
    days: int = 5
    ticks_per_day: int = 6
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    home_binding: bool
    routine_clock: bool
    work_projects: bool
    need_driven_selection: bool
    unscripted_object_use: bool
    object_persistence: bool
    place_traversal: bool
    frequency_flower_coupling: bool
    social_continuity: bool
    rest_recovery: bool
    replay_timeline: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    object_count: int
    simulated_days: int
    routine_ticks: int
    autonomy_events: int
    home_place_binding_rate: float
    routine_clock_progression_rate: float
    work_project_progress_rate: float
    need_driven_action_selection_rate: float
    unscripted_object_use_rate: float
    persistent_object_state_rate: float
    place_traversal_rate: float
    frequency_flower_coupling_rate: float
    social_continuity_modulation_rate: float
    rest_recovery_rate: float
    browser_autonomy_tick_rate: float
    replay_timeline_integrity_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    routine_autonomy_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_routine_autonomy_readiness: float
    full_home_place_binding_rate: float
    full_routine_clock_progression_rate: float
    full_work_project_progress_rate: float
    full_need_driven_action_selection_rate: float
    full_unscripted_object_use_rate: float
    full_persistent_object_state_rate: float
    full_place_traversal_rate: float
    full_frequency_flower_coupling_rate: float
    full_social_continuity_modulation_rate: float
    full_rest_recovery_rate: float
    full_browser_autonomy_tick_rate: float
    full_replay_timeline_integrity_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    no_home_binding_loss: float
    no_routine_clock_loss: float
    no_work_projects_loss: float
    no_need_driven_selection_loss: float
    no_unscripted_object_use_loss: float
    no_object_persistence_loss: float
    no_place_traversal_loss: float
    no_frequency_flower_coupling_loss: float
    no_social_continuity_loss: float
    no_rest_recovery_loss: float
    no_replay_timeline_loss: float
    no_privacy_filter_loss: float
    supports_agent_routine_home_work_unscripted_object_use_bridge: bool
    supports_local_autonomous_agent_routine_seed: bool
    supports_complete_3d_world: bool
    supports_complete_playable_world: bool
    supports_subjective_consciousness: bool
    supports_moral_patienthood_claim: bool
    supports_natural_language_emergence: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_agent_routine_home_work_unscripted_object_use", True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_home_binding", False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_routine_clock", True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_work_projects", True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_need_driven_selection", True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_unscripted_object_use", True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_object_persistence", True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_place_traversal", True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_frequency_flower_coupling", True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_social_continuity", True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_rest_recovery", True, True, True, True, True, True, True, True, True, False, True, True),
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
    if data.get("condition") != "integrated_object_persistence_promise_relationship_continuity":
        raise ValueError("source state is not the integrated Report 182 continuity state")
    return data


def source_payload(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], list[dict[str, object]], dict[str, dict[str, object]], dict[str, dict[str, object]]]:
    state = source.get("continuity_state", {}) if isinstance(source.get("continuity_state"), Mapping) else {}
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


def route_graph(routes: Sequence[Mapping[str, object]]) -> dict[str, list[dict[str, object]]]:
    graph: dict[str, list[dict[str, object]]] = {}
    for route in routes:
        if not bool(route.get("avatar_traversable", True)):
            continue
        a = str(route["from"])
        b = str(route["to"])
        graph.setdefault(a, []).append({**copy.deepcopy(dict(route)), "from": a, "to": b})
        graph.setdefault(b, []).append({**copy.deepcopy(dict(route)), "from": b, "to": a})
    for value in graph.values():
        value.sort(key=lambda item: (float(item.get("hazard", 0.0)), float(item.get("route_cost", 0.0)), item["to"]))
    return graph


def first_step_route(graph: Mapping[str, Sequence[Mapping[str, object]]], start: str, goal: str) -> Mapping[str, object] | None:
    if start == goal:
        return None
    queue: deque[tuple[str, list[Mapping[str, object]]]] = deque([(start, [])])
    seen = set()
    while queue:
        node, path = queue.popleft()
        if node in seen:
            continue
        seen.add(node)
        for route in graph.get(node, []):
            target = str(route["to"])
            next_path = [*path, route]
            if target == goal:
                return next_path[0]
            queue.append((target, next_path))
    return None


def init_agents(source_agents: Mapping[str, Mapping[str, object]], condition: Condition) -> dict[str, dict[str, object]]:
    agents = copy.deepcopy(source_agents)
    for agent_id, agent in agents.items():
        profile = AGENT_PROFILES[agent_id]
        agent["home"] = profile["home"] if condition.home_binding else None
        agent["place"] = profile["home"] if condition.home_binding else agent.get("place", profile["home"])
        needs = agent.setdefault("needs", {})
        needs.setdefault("fatigue", 0.38)
        needs.setdefault("thirst", 0.34)
        needs.setdefault("connection_deficit", 0.32)
        needs.setdefault("unfinished_task", 0.42)
        needs.setdefault("safety_concern", 0.30)
        needs["rest_debt"] = 0.34
        needs["routine_boredom"] = 0.22
        agent["project"] = {
            "project_id": profile["project_id"],
            "work_place": profile["work_place"],
            "required_object": profile["work_object"],
            "progress": 0.0,
            "complete": False,
        } if condition.work_projects else None
    return agents


def init_objects(source_objects: Mapping[str, Mapping[str, object]]) -> dict[str, dict[str, object]]:
    objects = copy.deepcopy(source_objects)
    for object_id, obj in objects.items():
        obj.setdefault("object_id", object_id)
        obj.setdefault("label", object_id.replace("_", " "))
        obj.setdefault("held_by", obj.get("owner") if obj.get("owner") in AGENT_PROFILES else obj.get("place"))
        obj["routine_uses"] = 0
    return objects


def candidate_actions(agent_id: str, agent: Mapping[str, object], phase: str, condition: Condition) -> list[dict[str, object]]:
    profile = AGENT_PROFILES[agent_id]
    needs = agent.get("needs", {}) if isinstance(agent.get("needs"), Mapping) else {}
    project = agent.get("project") if isinstance(agent.get("project"), Mapping) else None
    trust = float(agent.get("relationship", {}).get("trust_in_avatar", 0.5)) if isinstance(agent.get("relationship"), Mapping) else 0.5
    wariness = float(agent.get("relationship", {}).get("wariness", 0.3)) if isinstance(agent.get("relationship"), Mapping) else 0.3
    relation_bias = (trust - wariness) * 0.08 if condition.social_continuity else 0.0
    phase_bonus = {
        "dawn_home": {"home_tend": 0.28, "rest": 0.14},
        "morning_work": {"work_project": 0.32},
        "midday_care": {"care_drink": 0.30},
        "afternoon_work": {"work_project": 0.28, "explore_safety": 0.10},
        "dusk_social": {"social_check": 0.30},
        "night_rest": {"rest": 0.36},
        "unclocked": {},
    }.get(phase, {}) if condition.routine_clock else {}
    candidates = [
        {
            "action": "home_tend",
            "target_place": profile["home"],
            "object_id": profile["rest_object"],
            "need_key": "routine_boredom",
            "score": 0.20 + phase_bonus.get("home_tend", 0.0) + float(needs.get("routine_boredom", 0.0)) * 0.25,
        },
        {
            "action": "rest",
            "target_place": profile["home"],
            "object_id": profile["rest_object"],
            "need_key": "rest_debt",
            "score": 0.18 + phase_bonus.get("rest", 0.0) + float(needs.get("fatigue", 0.0)) * 0.20 + float(needs.get("rest_debt", 0.0)) * 0.42,
        },
        {
            "action": "care_drink",
            "target_place": "moss_hollow",
            "object_id": "reed_cup",
            "need_key": "thirst",
            "score": 0.16 + phase_bonus.get("care_drink", 0.0) + float(needs.get("thirst", 0.0)) * 0.45,
        },
        {
            "action": "social_check",
            "target_place": "hearth_vale",
            "object_id": profile["social_object"],
            "need_key": "connection_deficit",
            "score": 0.14 + phase_bonus.get("social_check", 0.0) + float(needs.get("connection_deficit", 0.0)) * 0.38 + relation_bias,
        },
        {
            "action": "explore_safety",
            "target_place": "stone_ridge" if agent_id != "Milo" else "glass_mire",
            "object_id": "glass_lens" if agent_id != "Milo" else "signal_shell",
            "need_key": "safety_concern",
            "score": 0.12 + phase_bonus.get("explore_safety", 0.0) + float(needs.get("safety_concern", 0.0)) * 0.38,
        },
    ]
    if condition.work_projects and project is not None and not bool(project.get("complete")):
        candidates.append({
            "action": "work_project",
            "target_place": profile["work_place"],
            "object_id": profile["work_object"],
            "need_key": profile["project_need"],
            "score": 0.22 + phase_bonus.get("work_project", 0.0) + (1.0 - float(project.get("progress", 0.0))) * 0.30 + float(needs.get(profile["project_need"], 0.0)) * 0.18,
        })
    return candidates


def choose_action(candidates: Sequence[Mapping[str, object]], condition: Condition, tick_index: int) -> Mapping[str, object]:
    if condition.need_driven_selection:
        return sorted(candidates, key=lambda item: (-float(item["score"]), str(item["action"]), str(item["target_place"]))) [0]
    return candidates[tick_index % len(candidates)]


def apply_action(agent_id: str, agent: dict[str, object], objects: dict[str, dict[str, object]], chosen: Mapping[str, object], condition: Condition) -> tuple[dict[str, float], dict[str, object] | None, dict[str, float]]:
    needs = agent.get("needs", {}) if isinstance(agent.get("needs"), dict) else {}
    before_needs = copy.deepcopy(needs)
    object_id = str(chosen.get("object_id")) if condition.unscripted_object_use else ""
    obj = objects.get(object_id) if object_id else None
    if obj is not None and condition.object_persistence:
        obj["held_by"] = agent_id
        obj["last_used_by"] = agent_id
        obj["routine_uses"] = int(obj.get("routine_uses", 0)) + 1
    action = str(chosen["action"])
    if action == "rest" and condition.rest_recovery:
        needs["fatigue"] = clamp(float(needs.get("fatigue", 0.0)) - 0.16)
        needs["rest_debt"] = clamp(float(needs.get("rest_debt", 0.0)) - 0.20)
    elif action == "work_project":
        project = agent.get("project") if isinstance(agent.get("project"), dict) else None
        if condition.work_projects and project is not None:
            before = float(project.get("progress", 0.0))
            project["progress"] = clamp(before + 0.16)
            project["complete"] = project["progress"] >= 0.96
            needs["unfinished_task"] = clamp(float(needs.get("unfinished_task", 0.0)) - 0.055)
            needs["fatigue"] = clamp(float(needs.get("fatigue", 0.0)) + 0.030)
    elif action == "care_drink":
        needs["thirst"] = clamp(float(needs.get("thirst", 0.0)) - 0.18)
        needs["connection_deficit"] = clamp(float(needs.get("connection_deficit", 0.0)) - 0.025)
    elif action == "social_check":
        needs["connection_deficit"] = clamp(float(needs.get("connection_deficit", 0.0)) - 0.12)
        relation = agent.get("relationship", {}) if isinstance(agent.get("relationship"), dict) else {}
        if condition.social_continuity:
            relation["trust_in_avatar"] = clamp(float(relation.get("trust_in_avatar", 0.5)) + 0.006)
            relation["wariness"] = clamp(float(relation.get("wariness", 0.3)) - 0.006)
    elif action == "explore_safety":
        needs["safety_concern"] = clamp(float(needs.get("safety_concern", 0.0)) - 0.10)
        needs["routine_boredom"] = clamp(float(needs.get("routine_boredom", 0.0)) - 0.045)
    elif action == "home_tend":
        needs["routine_boredom"] = clamp(float(needs.get("routine_boredom", 0.0)) - 0.07)
        needs["rest_debt"] = clamp(float(needs.get("rest_debt", 0.0)) + 0.018)
    if action != "rest":
        needs["fatigue"] = clamp(float(needs.get("fatigue", 0.0)) + 0.012)
        needs["rest_debt"] = clamp(float(needs.get("rest_debt", 0.0)) + 0.010)
    needs["thirst"] = clamp(float(needs.get("thirst", 0.0)) + 0.012)
    need_delta = {key: round(float(needs[key]) - float(before_needs.get(key, 0.0)), 6) for key in needs if round(float(needs[key]) - float(before_needs.get(key, 0.0)), 6) != 0.0}
    project = agent.get("project") if isinstance(agent.get("project"), dict) else None
    project_packet = copy.deepcopy(project) if project is not None else None
    return need_delta, copy.deepcopy(obj) if obj is not None else None, project_packet


def trace_ok(event: Mapping[str, object]) -> bool:
    required = {
        "event_id",
        "condition",
        "day",
        "tick",
        "phase",
        "agent_id",
        "home_place",
        "place_before",
        "place_after",
        "candidate_scores",
        "chosen_action",
        "need_delta",
        "object_used",
        "project_packet",
        "route_step",
        "frequency_hz",
        "flower_node",
        "autonomy_tick",
        "replay_frame",
        "private_workspace_hidden",
        "claim_boundary",
    }
    return required.issubset(event.keys())


def simulate_condition(config: RoutineConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, object], list[dict[str, object]]]:
    places, routes, source_agents, source_objects = source_payload(source)
    graph = route_graph(routes)
    agents = init_agents(source_agents, condition)
    objects = init_objects(source_objects)
    source_object_home = {oid: copy.deepcopy(obj) for oid, obj in objects.items()}
    events: list[dict[str, object]] = []
    replay: list[dict[str, object]] = []
    event_id = 0
    claim_boundary = {
        "complete_3d_world": False,
        "complete_playable_world": False,
        "subjective_consciousness": False,
        "moral_patienthood": False,
        "natural_language_emergence": False,
    }
    trackers = {key: [] for key in ["home", "need", "object", "persist", "traverse", "freq", "social", "rest", "tick", "replay", "privacy", "trace"]}
    needed_traversals: list[float] = []
    work_progress_hits: list[float] = []
    used_phases: set[str] = set()
    object_use_history: list[dict[str, object]] = []

    for day in range(config.days):
        for tick in range(config.ticks_per_day):
            phase = PHASES[tick % len(PHASES)] if condition.routine_clock else "unclocked"
            used_phases.add(phase)
            for agent_id in sorted(agents):
                agent = agents[agent_id]
                if not condition.object_persistence:
                    objects = copy.deepcopy(source_object_home)
                place_before = str(agent.get("place", AGENT_PROFILES[agent_id]["home"]))
                candidates = candidate_actions(agent_id, agent, phase, condition)
                chosen = choose_action(candidates, condition, event_id + config.seed)
                target_place = str(chosen["target_place"])
                route_step = first_step_route(graph, place_before, target_place) if condition.place_traversal else None
                moved = False
                if place_before != target_place:
                    needed_traversals.append(1.0)
                    if route_step is not None:
                        agent["place"] = str(route_step["to"])
                        moved = True
                    elif condition.place_traversal and target_place in places:
                        agent["place"] = target_place
                        moved = True
                    else:
                        needed_traversals[-1] = 0.0
                place_after = str(agent.get("place", place_before))
                need_before = copy.deepcopy(agent.get("needs", {}))
                object_before = copy.deepcopy(objects.get(str(chosen.get("object_id")), {})) if chosen.get("object_id") in objects else None
                need_delta, object_used, project_packet = apply_action(agent_id, agent, objects, chosen, condition)
                if object_used is not None:
                    object_use_history.append({"event_id": event_id, "agent_id": agent_id, "object_id": object_used["object_id"], "held_by": object_used.get("held_by")})
                route_frequency = route_step.get("frequency_hz") if route_step and condition.frequency_flower_coupling else None
                object_frequency = object_used.get("frequency_hz") if object_used and condition.frequency_flower_coupling else None
                frequency = route_frequency if route_frequency is not None else object_frequency
                flower = route_step.get("flower_node") if route_step and condition.frequency_flower_coupling else object_used.get("flower_node") if object_used and condition.frequency_flower_coupling else "unbound"
                best_score = max(float(item["score"]) for item in candidates) if candidates else 0.0
                chosen_best = abs(float(chosen["score"]) - best_score) < 1e-9
                replay_frame = None
                if condition.replay_timeline:
                    replay_frame = {
                        "replay_index": len(replay),
                        "day": day,
                        "tick": tick,
                        "phase": phase,
                        "agent_id": agent_id,
                        "place_after": place_after,
                        "action": chosen["action"],
                        "object_id": object_used.get("object_id") if object_used else None,
                        "project": project_packet,
                    }
                    replay.append(replay_frame)
                event = {
                    "event_id": event_id,
                    "condition": condition.name,
                    "day": day,
                    "tick": tick,
                    "phase": phase,
                    "agent_id": agent_id,
                    "home_place": agent.get("home"),
                    "place_before": place_before,
                    "place_after": place_after,
                    "candidate_scores": [{"action": item["action"], "target_place": item["target_place"], "object_id": item["object_id"], "need_key": item["need_key"], "score": round(float(item["score"]), 6)} for item in candidates],
                    "chosen_action": {"action": chosen["action"], "target_place": target_place, "need_key": chosen["need_key"], "score": round(float(chosen["score"]), 6), "selection_policy": "need_scored" if condition.need_driven_selection else "phase_index"},
                    "need_before": need_before,
                    "need_delta": need_delta,
                    "object_before": object_before,
                    "object_used": object_used,
                    "project_packet": project_packet,
                    "route_step": copy.deepcopy(dict(route_step)) if route_step is not None else None,
                    "moved": moved,
                    "frequency_hz": frequency,
                    "flower_node": flower,
                    "social_continuity_bias_applied": condition.social_continuity,
                    "autonomy_tick": {"manual_script_event": False, "policy": "routine_need_object_route_score", "tick_hash": stable_hash(day, tick, agent_id, chosen, place_after)},
                    "replay_frame": replay_frame,
                    "private_workspace_hidden": condition.privacy_filter,
                    "claim_boundary": claim_boundary,
                }
                events.append(event)
                trackers["home"].append(1.0 if condition.home_binding and agent.get("home") in places and (chosen["action"] != "rest" or place_after == agent.get("home")) else 0.0)
                trackers["need"].append(1.0 if condition.need_driven_selection and chosen_best and chosen.get("need_key") in agent.get("needs", {}) else 0.0)
                trackers["object"].append(1.0 if condition.unscripted_object_use and object_used is not None and object_used.get("object_id") == chosen.get("object_id") and event["autonomy_tick"]["manual_script_event"] is False else 0.0)
                trackers["persist"].append(1.0 if condition.object_persistence and (object_used is None or object_used.get("held_by") == agent_id) else 0.0)
                if place_before != target_place:
                    trackers["traverse"].append(1.0 if moved else 0.0)
                trackers["freq"].append(1.0 if condition.frequency_flower_coupling and frequency is not None and flower not in {None, "unbound"} else 0.0)
                trackers["social"].append(1.0 if condition.social_continuity and event["social_continuity_bias_applied"] else 0.0)
                if chosen["action"] == "rest":
                    trackers["rest"].append(1.0 if condition.rest_recovery and any(value < 0.0 for key, value in need_delta.items() if key in {"fatigue", "rest_debt"}) else 0.0)
                trackers["tick"].append(1.0 if event["autonomy_tick"]["manual_script_event"] is False else 0.0)
                trackers["replay"].append(1.0 if replay_frame is not None and replay_frame.get("replay_index") == len(replay) - 1 else 0.0)
                trackers["privacy"].append(1.0 if condition.privacy_filter and event["private_workspace_hidden"] else 0.0)
                trackers["trace"].append(1.0 if trace_ok(event) and event["claim_boundary"] == claim_boundary else 0.0)
                event_id += 1

    projects = [agent.get("project") for agent in agents.values() if isinstance(agent.get("project"), Mapping)]
    if condition.work_projects and projects:
        work_progress_hits = [1.0 if float(project.get("progress", 0.0)) >= 0.80 else 0.0 for project in projects]
    routine_rate = 1.0 if condition.routine_clock and set(PHASES).issubset(used_phases) else 0.0
    traverse_rate = mean(trackers["traverse"]) if trackers["traverse"] else (1.0 if condition.place_traversal else 0.0)
    persistence_rate = mean(trackers["persist"]) if object_use_history else 0.0
    metrics = {
        "home_place_binding_rate": mean(trackers["home"]),
        "routine_clock_progression_rate": routine_rate,
        "work_project_progress_rate": mean(work_progress_hits),
        "need_driven_action_selection_rate": mean(trackers["need"]),
        "unscripted_object_use_rate": mean(trackers["object"]),
        "persistent_object_state_rate": persistence_rate,
        "place_traversal_rate": traverse_rate,
        "frequency_flower_coupling_rate": mean(trackers["freq"]),
        "social_continuity_modulation_rate": mean(trackers["social"]),
        "rest_recovery_rate": mean(trackers["rest"]),
        "browser_autonomy_tick_rate": mean(trackers["tick"]),
        "replay_timeline_integrity_rate": mean(trackers["replay"]),
        "privacy_preservation_rate": mean(trackers["privacy"]),
        "trace_integrity": mean(trackers["trace"]),
    }
    metrics = {key: clamp(value) for key, value in metrics.items()}
    readiness = sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS)
    row = EvalRow(
        condition=condition.name,
        agent_count=len(agents),
        object_count=len(objects),
        simulated_days=config.days,
        routine_ticks=config.days * config.ticks_per_day,
        autonomy_events=len(events),
        routine_autonomy_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in metrics.items()},
    )
    state = {
        "condition": condition.name,
        "source_condition": source.get("condition"),
        "places": places,
        "routes": routes,
        "agents": agents,
        "objects": objects,
        "events": events,
        "replay": replay,
        "phases": PHASES,
        "agent_profiles": AGENT_PROFILES,
        "autonomy_kernel": {
            "candidate_policy": "home/rest/care/social/explore/work actions scored from phase, need pressure, project progress, object affordance, route access, and relationship carryover",
            "not_scripted_interaction_ledger": True,
            "manual_script_event": False,
        },
    }
    return row, state, events


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_agent_routine_home_work_unscripted_object_use"]

    def loss(name: str) -> float:
        return round(full.routine_autonomy_readiness - by_name[name].routine_autonomy_readiness, 6)

    losses = {
        "no_home_binding_loss": loss("no_home_binding"),
        "no_routine_clock_loss": loss("no_routine_clock"),
        "no_work_projects_loss": loss("no_work_projects"),
        "no_need_driven_selection_loss": loss("no_need_driven_selection"),
        "no_unscripted_object_use_loss": loss("no_unscripted_object_use"),
        "no_object_persistence_loss": loss("no_object_persistence"),
        "no_place_traversal_loss": loss("no_place_traversal"),
        "no_frequency_flower_coupling_loss": loss("no_frequency_flower_coupling"),
        "no_social_continuity_loss": loss("no_social_continuity"),
        "no_rest_recovery_loss": loss("no_rest_recovery"),
        "no_replay_timeline_loss": loss("no_replay_timeline"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.routine_autonomy_readiness >= 0.90
        and full.agent_count >= 3
        and full.autonomy_events >= 80
        and full.home_place_binding_rate >= 0.95
        and full.routine_clock_progression_rate == 1.0
        and full.work_project_progress_rate == 1.0
        and full.need_driven_action_selection_rate == 1.0
        and full.unscripted_object_use_rate >= 0.95
        and full.place_traversal_rate == 1.0
        and full.rest_recovery_rate == 1.0
        and full.browser_autonomy_tick_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_home_binding_loss"] >= 0.08
        and losses["no_routine_clock_loss"] >= 0.08
        and losses["no_work_projects_loss"] >= 0.10
        and losses["no_need_driven_selection_loss"] >= 0.10
        and losses["no_unscripted_object_use_loss"] >= 0.09
        and losses["no_rest_recovery_loss"] >= 0.08
    )
    return VerdictRow(
        full_condition=full.condition,
        full_routine_autonomy_readiness=full.routine_autonomy_readiness,
        full_home_place_binding_rate=full.home_place_binding_rate,
        full_routine_clock_progression_rate=full.routine_clock_progression_rate,
        full_work_project_progress_rate=full.work_project_progress_rate,
        full_need_driven_action_selection_rate=full.need_driven_action_selection_rate,
        full_unscripted_object_use_rate=full.unscripted_object_use_rate,
        full_persistent_object_state_rate=full.persistent_object_state_rate,
        full_place_traversal_rate=full.place_traversal_rate,
        full_frequency_flower_coupling_rate=full.frequency_flower_coupling_rate,
        full_social_continuity_modulation_rate=full.social_continuity_modulation_rate,
        full_rest_recovery_rate=full.rest_recovery_rate,
        full_browser_autonomy_tick_rate=full.browser_autonomy_tick_rate,
        full_replay_timeline_integrity_rate=full.replay_timeline_integrity_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        supports_agent_routine_home_work_unscripted_object_use_bridge=supports,
        supports_local_autonomous_agent_routine_seed=supports,
        supports_complete_3d_world=False,
        supports_complete_playable_world=False,
        supports_subjective_consciousness=False,
        supports_moral_patienthood_claim=False,
        supports_natural_language_emergence=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: RoutineConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_state: dict[str, object] = {}
    integrated_trace: list[dict[str, object]] = []
    for condition in CONDITIONS:
        row, state, trace = simulate_condition(config, source, condition)
        rows.append(row)
        if condition.name == "integrated_agent_routine_home_work_unscripted_object_use":
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
        "phases": PHASES,
        "agent_profiles": AGENT_PROFILES,
        "moral_boundary": {
            "routine_autonomy_seed_not_complete_gameplay": True,
            "unscripted_policy_not_free_will_claim": True,
            "need_driven_choice_not_subjective_feeling": True,
            "agent_routines_not_moral_patienthood": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "agent-local planning with interruptions, project dependencies, and emergent cooperation",
    }
    state = {
        "condition": "integrated_agent_routine_home_work_unscripted_object_use",
        "config": asdict(config),
        "source_condition": source.get("condition"),
        "routine_state": integrated_state,
        "trace_events": len(integrated_trace),
        "moral_boundary": results["moral_boundary"],
    }
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_AGENT_ROUTINE_HOME_WORK_UNSCRIPTED_OBJECT_USE_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_AGENT_ROUTINE_HOME_WORK_UNSCRIPTED_OBJECT_USE_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_AGENT_ROUTINE_HOME_WORK_UNSCRIPTED_OBJECT_USE_STATE", state)
    return results


def parse_args() -> RoutineConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=RoutineConfig.seed)
    parser.add_argument("--days", type=int, default=RoutineConfig.days)
    parser.add_argument("--ticks-per-day", type=int, default=RoutineConfig.ticks_per_day)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return RoutineConfig(seed=args.seed, days=args.days, ticks_per_day=args.ticks_per_day, source_state=args.source_state)


def main() -> None:
    config = parse_args()
    results = run(config)
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("routine_autonomy_readiness", f"{verdict['full_routine_autonomy_readiness']:.6f}")
    print("simulated_days", config.days)
    print("autonomy_events", results["rows"][0]["autonomy_events"])
    print("no_work_projects_loss", f"{verdict['no_work_projects_loss']:.6f}")
    print("no_need_driven_selection_loss", f"{verdict['no_need_driven_selection_loss']:.6f}")
    print("no_unscripted_object_use_loss", f"{verdict['no_unscripted_object_use_loss']:.6f}")


if __name__ == "__main__":
    main()
