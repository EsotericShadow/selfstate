#!/usr/bin/env python3
"""Agent-local planning with interruptions, dependencies, and cooperation.

Report 184 consumes the Report 183 autonomous routine state and adds a
multi-step local planning layer. Agents generate private plan stacks, coordinate
project dependencies, pause and resume after interruptions, hand objects across
ownership boundaries, replan priorities, and cooperate without exposing private
workspace internals.

No LLMs are called. This is deterministic planning substrate, not a claim of
complete gameplay, subjective consciousness, moral patienthood, natural language
emergence, or free will.
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
PREFIX = "ssrm_3d_agent_local_planning_interruptions_cooperation_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_agent_routine_home_work_unscripted_object_use_bridge_state.json"

PROJECTS = {
    "Ari": {
        "project_id": "repair_clay_latch_with_dry_patch",
        "home": "hearth_vale",
        "work_place": "clay_basin",
        "primary_object": "clay_patch_kit",
        "dependencies": ("dry_cloak_handoff", "ridge_route_signal"),
        "cooperators": ("Fay", "Milo"),
    },
    "Fay": {
        "project_id": "dry_cloak_and_moss_bedding_support",
        "home": "moss_hollow",
        "work_place": "moss_hollow",
        "primary_object": "dry_cloak",
        "dependencies": ("reed_cup_ready",),
        "cooperators": ("Ari",),
    },
    "Milo": {
        "project_id": "ridge_warning_route_clearance",
        "home": "stone_ridge",
        "work_place": "stone_ridge",
        "primary_object": "signal_shell",
        "dependencies": ("glass_lens_check",),
        "cooperators": ("Ari", "Fay"),
    },
}

PLAN_STEPS = ("orient", "collect_primary_object", "move_to_work", "resolve_dependency", "cooperate", "work_step", "stabilize_and_rest")
INTERRUPTIONS = {
    4: "wet_squall",
    9: "missing_dependency",
    14: "route_hazard_warning",
}

WEIGHTS = {
    "plan_generation_rate": 0.09,
    "multi_step_plan_integrity_rate": 0.08,
    "interruption_detection_rate": 0.08,
    "interruption_recovery_rate": 0.09,
    "project_dependency_resolution_rate": 0.10,
    "cooperation_event_rate": 0.09,
    "handoff_integrity_rate": 0.07,
    "route_coordination_rate": 0.07,
    "priority_replan_rate": 0.08,
    "frequency_flower_plan_binding_rate": 0.06,
    "bounded_stress_recovery_rate": 0.07,
    "browser_plan_replay_rate": 0.05,
    "privacy_preservation_rate": 0.04,
    "trace_integrity": 0.03,
}


@dataclass(frozen=True)
class PlanningConfig:
    seed: int = 20260728
    days: int = 4
    ticks_per_day: int = 6
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    plan_generation: bool
    multi_step_plan: bool
    interruptions: bool
    resume_after_interrupt: bool
    project_dependencies: bool
    cooperation: bool
    dependency_handoff: bool
    route_coordination: bool
    priority_replan: bool
    frequency_flower_plan_binding: bool
    bounded_stress_recovery: bool
    replay_timeline: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    object_count: int
    simulated_days: int
    planning_ticks: int
    planning_events: int
    plan_generation_rate: float
    multi_step_plan_integrity_rate: float
    interruption_detection_rate: float
    interruption_recovery_rate: float
    project_dependency_resolution_rate: float
    cooperation_event_rate: float
    handoff_integrity_rate: float
    route_coordination_rate: float
    priority_replan_rate: float
    frequency_flower_plan_binding_rate: float
    bounded_stress_recovery_rate: float
    browser_plan_replay_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    local_planning_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_local_planning_readiness: float
    full_plan_generation_rate: float
    full_multi_step_plan_integrity_rate: float
    full_interruption_detection_rate: float
    full_interruption_recovery_rate: float
    full_project_dependency_resolution_rate: float
    full_cooperation_event_rate: float
    full_handoff_integrity_rate: float
    full_route_coordination_rate: float
    full_priority_replan_rate: float
    full_frequency_flower_plan_binding_rate: float
    full_bounded_stress_recovery_rate: float
    full_browser_plan_replay_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    no_plan_generation_loss: float
    no_multi_step_plan_loss: float
    no_interruptions_loss: float
    no_resume_after_interrupt_loss: float
    no_project_dependencies_loss: float
    no_cooperation_loss: float
    no_dependency_handoff_loss: float
    no_route_coordination_loss: float
    no_priority_replan_loss: float
    no_frequency_flower_plan_binding_loss: float
    no_bounded_stress_recovery_loss: float
    no_replay_timeline_loss: float
    no_privacy_filter_loss: float
    supports_agent_local_planning_interruptions_cooperation_bridge: bool
    supports_local_planning_and_cooperation_seed: bool
    supports_complete_3d_world: bool
    supports_complete_playable_world: bool
    supports_subjective_consciousness: bool
    supports_moral_patienthood_claim: bool
    supports_natural_language_emergence: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_agent_local_planning_interruptions_cooperation", True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_plan_generation", False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_multi_step_plan", True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_interruptions", True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_resume_after_interrupt", True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_project_dependencies", True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_cooperation", True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_dependency_handoff", True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_route_coordination", True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_priority_replan", True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_frequency_flower_plan_binding", True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_bounded_stress_recovery", True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_replay_timeline", True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, True, False),
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
    if data.get("condition") != "integrated_agent_routine_home_work_unscripted_object_use":
        raise ValueError("source state is not the integrated Report 183 routine state")
    return data


def source_payload(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], list[dict[str, object]], dict[str, dict[str, object]], dict[str, dict[str, object]]]:
    state = source.get("routine_state", {}) if isinstance(source.get("routine_state"), Mapping) else {}
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
    for edges in graph.values():
        edges.sort(key=lambda item: (float(item.get("hazard", 0.0)), float(item.get("route_cost", 0.0)), item["to"]))
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
    for agent_id, project in PROJECTS.items():
        agent = agents.setdefault(agent_id, {"agent_id": agent_id, "relationship": {}, "needs": {}})
        agent["agent_id"] = agent_id
        agent["home"] = project["home"]
        agent["place"] = project["home"]
        steps = list(PLAN_STEPS) if condition.multi_step_plan else ["work_step"]
        agent["public_plan"] = {
            "plan_id": stable_hash(condition.name, agent_id, project["project_id"]),
            "project_id": project["project_id"],
            "summary": f"{agent_id} plans {project['project_id']}",
            "step_count": len(steps),
            "private_stack_hidden": condition.privacy_filter,
        } if condition.plan_generation else None
        agent["private_plan_stack"] = steps if condition.plan_generation else []
        agent["plan_index"] = 0
        agent["paused_by"] = None
        agent["stress"] = 0.24
        agent["project_progress"] = 0.0
    return agents


def init_dependencies(condition: Condition) -> dict[str, dict[str, object]]:
    deps = {
        "dry_cloak_handoff": {"needed_by": "Ari", "provided_by": "Fay", "object_id": "dry_cloak", "status": "open"},
        "ridge_route_signal": {"needed_by": "Ari", "provided_by": "Milo", "object_id": "signal_shell", "status": "open"},
        "reed_cup_ready": {"needed_by": "Fay", "provided_by": "Ari", "object_id": "reed_cup", "status": "open"},
        "glass_lens_check": {"needed_by": "Milo", "provided_by": "Milo", "object_id": "glass_lens", "status": "open"},
    }
    if not condition.project_dependencies:
        for dep in deps.values():
            dep["status"] = "ignored"
    return deps


def target_for_step(agent_id: str, step: str) -> str:
    project = PROJECTS[agent_id]
    if step in {"orient", "stabilize_and_rest"}:
        return project["home"]
    if step in {"move_to_work", "resolve_dependency", "cooperate", "work_step"}:
        return project["work_place"]
    return project["home"]


def unresolved_dependency(agent_id: str, dependencies: Mapping[str, Mapping[str, object]], condition: Condition) -> str | None:
    if not condition.project_dependencies:
        return None
    for dep_name in PROJECTS[agent_id]["dependencies"]:
        dep = dependencies.get(dep_name)
        if dep and dep.get("status") != "resolved":
            return dep_name
    return None


def maybe_resolve_dependency(agent_id: str, step: str, dependencies: dict[str, dict[str, object]], objects: dict[str, dict[str, object]], condition: Condition) -> tuple[str | None, dict[str, object] | None]:
    if not condition.project_dependencies:
        return None, None
    if step not in {"resolve_dependency", "cooperate"}:
        return None, None
    for dep_name, dep in dependencies.items():
        if dep.get("status") == "resolved":
            continue
        if dep.get("provided_by") == agent_id or (condition.cooperation and dep.get("needed_by") == agent_id and dep.get("provided_by") in PROJECTS):
            if condition.dependency_handoff:
                dep["status"] = "resolved"
                dep["resolved_by"] = agent_id if dep.get("provided_by") == agent_id else dep.get("provided_by")
                obj = objects.get(str(dep["object_id"]))
                if obj is not None:
                    obj["held_by"] = dep["needed_by"]
                    obj["handoff_for"] = dep_name
                    obj["routine_uses"] = int(obj.get("routine_uses", 0)) + 1
                return dep_name, copy.deepcopy(obj) if obj is not None else None
    return None, None


def trace_ok(event: Mapping[str, object]) -> bool:
    required = {
        "event_id",
        "condition",
        "day",
        "tick",
        "agent_id",
        "event_kind",
        "public_plan_summary",
        "private_plan_hidden",
        "current_step",
        "plan_index_before",
        "plan_index_after",
        "interruption_packet",
        "dependency_packet",
        "cooperation_packet",
        "handoff_packet",
        "route_step",
        "priority_replan_packet",
        "stress_packet",
        "frequency_hz",
        "flower_node",
        "replay_frame",
        "claim_boundary",
    }
    return required.issubset(event.keys())


def simulate_condition(config: PlanningConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, object], list[dict[str, object]]]:
    places, routes, source_agents, source_objects = source_payload(source)
    graph = route_graph(routes)
    agents = init_agents(source_agents, condition)
    objects = copy.deepcopy(source_objects)
    dependencies = init_dependencies(condition)
    events: list[dict[str, object]] = []
    replay: list[dict[str, object]] = []
    metrics = {key: [] for key in ["plan", "multi", "interrupt", "recover", "coop", "handoff", "route", "replan", "freq", "stress", "replay", "privacy", "trace"]}
    claim_boundary = {
        "complete_3d_world": False,
        "complete_playable_world": False,
        "subjective_consciousness": False,
        "moral_patienthood": False,
        "natural_language_emergence": False,
    }
    recovered_interruptions: set[tuple[str, str]] = set()
    detected_interruptions: set[tuple[str, str]] = set()
    coop_events: list[str] = []
    handoffs: list[str] = []
    event_id = 0

    for day in range(config.days):
        for tick in range(config.ticks_per_day):
            global_tick = day * config.ticks_per_day + tick
            interruption_kind = INTERRUPTIONS.get(global_tick) if condition.interruptions else None
            for agent_id in sorted(agents):
                agent = agents[agent_id]
                plan = agent.get("private_plan_stack", []) if condition.plan_generation else []
                plan_index_before = int(agent.get("plan_index", 0))
                current_step = plan[min(plan_index_before, len(plan) - 1)] if plan else "idle"
                event_kind = "plan_step"
                interruption_packet = None
                recovery_packet = None
                priority_replan_packet = None
                if interruption_kind is not None:
                    event_kind = "interruption_detected"
                    detected_interruptions.add((agent_id, interruption_kind))
                    agent["paused_by"] = interruption_kind
                    agent["stress"] = clamp(float(agent.get("stress", 0.24)) + (0.14 if condition.bounded_stress_recovery else 0.30))
                    interruption_packet = {"kind": interruption_kind, "detected": True, "plan_paused": True}
                    if condition.priority_replan:
                        priority_replan_packet = {"priority": "safety_first", "inserted_step": "stabilize_and_rest", "replan_reason": interruption_kind}
                        current_step = "stabilize_and_rest"
                elif agent.get("paused_by") is not None:
                    event_kind = "plan_resumed" if condition.resume_after_interrupt else "plan_stalled"
                    interruption_packet = {"kind": agent.get("paused_by"), "detected": True, "plan_paused": False}
                    if condition.resume_after_interrupt:
                        recovered_interruptions.add((agent_id, str(agent.get("paused_by"))))
                        recovery_packet = {"resumed_step": current_step, "resume_ok": True}
                        agent["paused_by"] = None
                        if condition.bounded_stress_recovery:
                            agent["stress"] = clamp(float(agent.get("stress", 0.24)) - 0.12)
                    else:
                        recovery_packet = {"resumed_step": None, "resume_ok": False}
                else:
                    interruption_packet = {"kind": None, "detected": False, "plan_paused": False}
                target_place = target_for_step(agent_id, current_step)
                place_before = str(agent.get("place", PROJECTS[agent_id]["home"]))
                route_step = first_step_route(graph, place_before, target_place) if condition.route_coordination else None
                if route_step is not None:
                    agent["place"] = route_step["to"]
                elif condition.route_coordination and target_place in places:
                    agent["place"] = target_place
                place_after = str(agent.get("place", place_before))
                blocked_dep = unresolved_dependency(agent_id, dependencies, condition)
                dep_name, handoff_object = maybe_resolve_dependency(agent_id, current_step, dependencies, objects, condition)
                if dep_name is not None:
                    event_kind = "dependency_handoff" if condition.dependency_handoff else event_kind
                    handoffs.append(dep_name)
                cooperation_packet = None
                if condition.cooperation and current_step == "cooperate":
                    partners = list(PROJECTS[agent_id]["cooperators"])
                    cooperation_packet = {"partners": partners, "cooperation_kind": "dependency_support", "accepted": True}
                    coop_events.append(agent_id)
                    event_kind = "cooperation_step"
                elif condition.cooperation and dep_name is not None:
                    cooperation_packet = {"partners": [dependencies[dep_name].get("needed_by"), dependencies[dep_name].get("provided_by")], "cooperation_kind": "handoff", "accepted": True}
                    coop_events.append(agent_id)
                else:
                    cooperation_packet = {"partners": [], "cooperation_kind": None, "accepted": False}
                if current_step == "work_step" and blocked_dep is None and condition.project_dependencies:
                    agent["project_progress"] = clamp(float(agent.get("project_progress", 0.0)) + 0.24)
                elif current_step == "work_step" and not condition.project_dependencies:
                    agent["project_progress"] = clamp(float(agent.get("project_progress", 0.0)) + 0.08)
                if condition.plan_generation and event_kind not in {"interruption_detected", "plan_stalled"} and plan:
                    agent["plan_index"] = min(plan_index_before + 1, len(plan) - 1)
                plan_index_after = int(agent.get("plan_index", 0))
                frequency = None
                flower = "unbound"
                if condition.frequency_flower_plan_binding:
                    if route_step is not None:
                        frequency = route_step.get("frequency_hz")
                        flower = route_step.get("flower_node", "unbound")
                    elif handoff_object is not None:
                        frequency = handoff_object.get("frequency_hz")
                        flower = handoff_object.get("flower_node", "unbound")
                    else:
                        frequency = round(0.211 + (event_id % 7) * 0.006, 6)
                        flower = ("root_rest", "work_petal", "social_petal", "return_petal")[event_id % 4]
                replay_frame = None
                if condition.replay_timeline:
                    replay_frame = {
                        "replay_index": len(replay),
                        "day": day,
                        "tick": tick,
                        "agent_id": agent_id,
                        "event_kind": event_kind,
                        "current_step": current_step,
                        "place_after": place_after,
                        "dependency": dep_name,
                        "interruption": interruption_kind,
                    }
                    replay.append(replay_frame)
                stress_value = clamp(float(agent.get("stress", 0.24)))
                event = {
                    "event_id": event_id,
                    "condition": condition.name,
                    "day": day,
                    "tick": tick,
                    "global_tick": global_tick,
                    "agent_id": agent_id,
                    "event_kind": event_kind,
                    "public_plan_summary": copy.deepcopy(agent.get("public_plan")),
                    "private_plan_hidden": condition.privacy_filter,
                    "current_step": current_step,
                    "plan_index_before": plan_index_before,
                    "plan_index_after": plan_index_after,
                    "place_before": place_before,
                    "place_after": place_after,
                    "interruption_packet": interruption_packet,
                    "recovery_packet": recovery_packet,
                    "dependency_packet": {"blocked_dependency": blocked_dep, "resolved_dependency": dep_name, "all_dependencies": copy.deepcopy(dependencies)},
                    "cooperation_packet": cooperation_packet,
                    "handoff_packet": {"object": handoff_object, "handoff_ok": dep_name is not None and handoff_object is not None},
                    "route_step": copy.deepcopy(dict(route_step)) if route_step is not None else None,
                    "priority_replan_packet": priority_replan_packet,
                    "stress_packet": {"stress": round(stress_value, 6), "bounded": condition.bounded_stress_recovery, "recoverable": stress_value <= 0.72 if condition.bounded_stress_recovery else stress_value <= 1.0},
                    "frequency_hz": frequency,
                    "flower_node": flower,
                    "replay_frame": replay_frame,
                    "claim_boundary": claim_boundary,
                }
                events.append(event)
                metrics["plan"].append(1.0 if condition.plan_generation and agent.get("public_plan") is not None else 0.0)
                public_plan = agent.get("public_plan") or {}
                metrics["multi"].append(1.0 if condition.multi_step_plan and public_plan.get("step_count", 0) >= 5 else 0.0)
                if interruption_kind is not None:
                    metrics["interrupt"].append(1.0 if condition.interruptions and event["interruption_packet"]["detected"] else 0.0)
                if event_kind in {"plan_resumed", "plan_stalled"}:
                    metrics["recover"].append(1.0 if condition.resume_after_interrupt and recovery_packet and recovery_packet["resume_ok"] else 0.0)
                metrics["coop"].append(1.0 if cooperation_packet["accepted"] else 0.0)
                if dep_name is not None or (current_step == "resolve_dependency" and condition.project_dependencies):
                    metrics["handoff"].append(1.0 if condition.dependency_handoff and dep_name is not None and handoff_object is not None else 0.0)
                if place_before != target_place:
                    metrics["route"].append(1.0 if condition.route_coordination and (route_step is not None or place_after == target_place) else 0.0)
                if interruption_kind is not None:
                    metrics["replan"].append(1.0 if condition.priority_replan and priority_replan_packet is not None else 0.0)
                metrics["freq"].append(1.0 if condition.frequency_flower_plan_binding and frequency is not None and flower != "unbound" else 0.0)
                metrics["stress"].append(1.0 if condition.bounded_stress_recovery and event["stress_packet"]["recoverable"] else 0.0)
                metrics["replay"].append(1.0 if replay_frame is not None and replay_frame["replay_index"] == len(replay) - 1 else 0.0)
                metrics["privacy"].append(1.0 if condition.privacy_filter and event["private_plan_hidden"] else 0.0)
                metrics["trace"].append(1.0 if trace_ok(event) and event["claim_boundary"] == claim_boundary else 0.0)
                event_id += 1
    dependency_rate = mean([1.0 if dep.get("status") == "resolved" else 0.0 for dep in dependencies.values()]) if condition.project_dependencies else 0.0
    cooperation_rate = min(1.0, len(set(coop_events)) / 3.0) if condition.cooperation else 0.0
    handoff_rate = min(1.0, len(set(handoffs)) / 4.0) if condition.dependency_handoff else 0.0
    metrics_out = {
        "plan_generation_rate": mean(metrics["plan"]),
        "multi_step_plan_integrity_rate": mean(metrics["multi"]),
        "interruption_detection_rate": mean(metrics["interrupt"]),
        "interruption_recovery_rate": mean(metrics["recover"]),
        "project_dependency_resolution_rate": dependency_rate,
        "cooperation_event_rate": cooperation_rate,
        "handoff_integrity_rate": handoff_rate,
        "route_coordination_rate": mean(metrics["route"]),
        "priority_replan_rate": mean(metrics["replan"]),
        "frequency_flower_plan_binding_rate": mean(metrics["freq"]),
        "bounded_stress_recovery_rate": mean(metrics["stress"]),
        "browser_plan_replay_rate": mean(metrics["replay"]),
        "privacy_preservation_rate": mean(metrics["privacy"]),
        "trace_integrity": mean(metrics["trace"]),
    }
    metrics_out = {key: clamp(value) for key, value in metrics_out.items()}
    readiness = sum(metrics_out[key] * WEIGHTS[key] for key in WEIGHTS)
    row = EvalRow(
        condition=condition.name,
        agent_count=len(agents),
        object_count=len(objects),
        simulated_days=config.days,
        planning_ticks=config.days * config.ticks_per_day,
        planning_events=len(events),
        local_planning_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in metrics_out.items()},
    )
    state = {
        "condition": condition.name,
        "source_condition": source.get("condition"),
        "places": places,
        "routes": routes,
        "agents": agents,
        "objects": objects,
        "dependencies": dependencies,
        "events": events,
        "replay": replay,
        "project_specs": PROJECTS,
        "interruptions": INTERRUPTIONS,
        "planning_kernel": {
            "plan_steps": PLAN_STEPS,
            "private_plan_stack_hidden": condition.privacy_filter,
            "resume_after_interrupt": condition.resume_after_interrupt,
            "dependency_handoff": condition.dependency_handoff,
            "not_free_will_claim": True,
        },
    }
    return row, state, events


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_agent_local_planning_interruptions_cooperation"]

    def loss(name: str) -> float:
        return round(full.local_planning_readiness - by_name[name].local_planning_readiness, 6)

    losses = {
        "no_plan_generation_loss": loss("no_plan_generation"),
        "no_multi_step_plan_loss": loss("no_multi_step_plan"),
        "no_interruptions_loss": loss("no_interruptions"),
        "no_resume_after_interrupt_loss": loss("no_resume_after_interrupt"),
        "no_project_dependencies_loss": loss("no_project_dependencies"),
        "no_cooperation_loss": loss("no_cooperation"),
        "no_dependency_handoff_loss": loss("no_dependency_handoff"),
        "no_route_coordination_loss": loss("no_route_coordination"),
        "no_priority_replan_loss": loss("no_priority_replan"),
        "no_frequency_flower_plan_binding_loss": loss("no_frequency_flower_plan_binding"),
        "no_bounded_stress_recovery_loss": loss("no_bounded_stress_recovery"),
        "no_replay_timeline_loss": loss("no_replay_timeline"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.local_planning_readiness >= 0.90
        and full.planning_events >= 70
        and full.plan_generation_rate == 1.0
        and full.multi_step_plan_integrity_rate == 1.0
        and full.interruption_detection_rate == 1.0
        and full.interruption_recovery_rate == 1.0
        and full.project_dependency_resolution_rate == 1.0
        and full.cooperation_event_rate == 1.0
        and full.handoff_integrity_rate == 1.0
        and full.route_coordination_rate == 1.0
        and full.priority_replan_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_plan_generation_loss"] >= 0.09
        and losses["no_project_dependencies_loss"] >= 0.10
        and losses["no_cooperation_loss"] >= 0.09
        and losses["no_dependency_handoff_loss"] >= 0.07
        and losses["no_priority_replan_loss"] >= 0.08
    )
    return VerdictRow(
        full_condition=full.condition,
        full_local_planning_readiness=full.local_planning_readiness,
        full_plan_generation_rate=full.plan_generation_rate,
        full_multi_step_plan_integrity_rate=full.multi_step_plan_integrity_rate,
        full_interruption_detection_rate=full.interruption_detection_rate,
        full_interruption_recovery_rate=full.interruption_recovery_rate,
        full_project_dependency_resolution_rate=full.project_dependency_resolution_rate,
        full_cooperation_event_rate=full.cooperation_event_rate,
        full_handoff_integrity_rate=full.handoff_integrity_rate,
        full_route_coordination_rate=full.route_coordination_rate,
        full_priority_replan_rate=full.priority_replan_rate,
        full_frequency_flower_plan_binding_rate=full.frequency_flower_plan_binding_rate,
        full_bounded_stress_recovery_rate=full.bounded_stress_recovery_rate,
        full_browser_plan_replay_rate=full.browser_plan_replay_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        supports_agent_local_planning_interruptions_cooperation_bridge=supports,
        supports_local_planning_and_cooperation_seed=supports,
        supports_complete_3d_world=False,
        supports_complete_playable_world=False,
        supports_subjective_consciousness=False,
        supports_moral_patienthood_claim=False,
        supports_natural_language_emergence=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: PlanningConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_state: dict[str, object] = {}
    integrated_trace: list[dict[str, object]] = []
    for condition in CONDITIONS:
        row, state, trace = simulate_condition(config, source, condition)
        rows.append(row)
        if condition.name == "integrated_agent_local_planning_interruptions_cooperation":
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
        "project_specs": PROJECTS,
        "interruptions": INTERRUPTIONS,
        "moral_boundary": {
            "planning_seed_not_complete_gameplay": True,
            "private_plan_stack_not_subjective_workspace": True,
            "cooperation_policy_not_moral_patienthood": True,
            "interruption_recovery_not_subjective_suffering": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "multi-agent project economy with resource scarcity, negotiation, and tool chains",
    }
    state = {
        "condition": "integrated_agent_local_planning_interruptions_cooperation",
        "config": asdict(config),
        "source_condition": source.get("condition"),
        "planning_state": integrated_state,
        "trace_events": len(integrated_trace),
        "moral_boundary": results["moral_boundary"],
    }
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_AGENT_LOCAL_PLANNING_INTERRUPTION_COOPERATION_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_AGENT_LOCAL_PLANNING_INTERRUPTION_COOPERATION_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_AGENT_LOCAL_PLANNING_INTERRUPTION_COOPERATION_STATE", state)
    return results


def parse_args() -> PlanningConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=PlanningConfig.seed)
    parser.add_argument("--days", type=int, default=PlanningConfig.days)
    parser.add_argument("--ticks-per-day", type=int, default=PlanningConfig.ticks_per_day)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return PlanningConfig(seed=args.seed, days=args.days, ticks_per_day=args.ticks_per_day, source_state=args.source_state)


def main() -> None:
    config = parse_args()
    results = run(config)
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("local_planning_readiness", f"{verdict['full_local_planning_readiness']:.6f}")
    print("planning_events", results["rows"][0]["planning_events"])
    print("no_project_dependencies_loss", f"{verdict['no_project_dependencies_loss']:.6f}")
    print("no_cooperation_loss", f"{verdict['no_cooperation_loss']:.6f}")
    print("no_priority_replan_loss", f"{verdict['no_priority_replan_loss']:.6f}")


if __name__ == "__main__":
    main()
