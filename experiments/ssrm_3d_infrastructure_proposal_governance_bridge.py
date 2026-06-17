#!/usr/bin/env python3
"""Infrastructure proposal-governance bridge for SSRM-3D agents.

This deterministic bridge moves past Report 148's fixed infrastructure project
set. Agents generate project proposals from route/object/maintenance pressures,
resolve conflicts over priorities, allocate scarce budgets, service maintenance
debt, ground proposals in native tokens, rotate fairness across roles, and leave
persistent governance histories.
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
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_agent_made_infrastructure_bridge_state.json"
PREFIX = "ssrm_3d_infrastructure_proposal_governance_bridge"
FLOWER_PHASES = (0.0, math.tau / 6.0, math.tau / 3.0, math.tau / 2.0, math.tau * 2.0 / 3.0, math.tau * 5.0 / 6.0, math.tau)

ROLE_MATERIAL_AFFINITY = {
    "scout": ("stone", "charcoal", "fiber"),
    "builder": ("wood", "stone", "clay", "fiber"),
    "healer": ("ash", "fiber", "hide"),
    "farmer": ("clay", "ash", "wood"),
    "guard": ("wood", "resin", "charcoal"),
    "teacher": ("fiber", "hide", "charcoal"),
    "trader": ("wood", "stone", "clay"),
    "pattern_keeper": ("stone", "charcoal", "resin"),
}

PROPOSAL_FOCUS = {
    "maintenance_debt": "tool-or-route",
    "route_safety": "danger-or-weather-memory",
    "object_access": "shared-resource",
    "sanitation_repair": "care-or-kinship",
    "signal_visibility": "danger-or-weather-memory",
    "water_security": "shared-resource",
    "care_access": "care-or-kinship",
    "language_marker": "shared-resource",
}

GOVERNANCE_SEASONS = ("wet-cold", "repair-sun", "scarcity-wind", "teaching-moon")


@dataclass(frozen=True)
class GovernanceConfig:
    seed: int = 20260623
    councils: int = 18
    proposals_per_council: int = 8
    source_agents: str = str(SOURCE_AGENTS)
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    agent_created_proposals: bool
    conflict_priority_arbitration: bool
    scarce_budget: bool
    maintenance_debt: bool
    cultural_language_grounding: bool
    fairness_rotation: bool
    outcome_feedback: bool
    trace_replay: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    councils: int
    generated_proposals: int
    accepted_proposals: int
    completed_allocations: int
    proposal_generation_rate: float
    pressure_grounding_score: float
    priority_conflict_resolution_rate: float
    scarce_budget_allocation_rate: float
    maintenance_debt_service_rate: float
    cultural_token_grounding_rate: float
    fairness_rotation_score: float
    outcome_feedback_rate: float
    accepted_completion_rate: float
    rejected_overreach_rate: float
    governance_history_persistence: float
    trace_completeness: float
    proposal_governance_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_proposal_governance_readiness: float
    full_proposal_generation_rate: float
    full_pressure_grounding_score: float
    full_priority_conflict_resolution_rate: float
    full_scarce_budget_allocation_rate: float
    full_maintenance_debt_service_rate: float
    full_cultural_token_grounding_rate: float
    full_fairness_rotation_score: float
    full_outcome_feedback_rate: float
    full_accepted_completion_rate: float
    full_rejected_overreach_rate: float
    full_governance_history_persistence: float
    full_trace_completeness: float
    no_agent_created_proposals_loss: float
    no_conflict_priority_arbitration_loss: float
    no_scarce_budget_loss: float
    no_maintenance_debt_loss: float
    no_cultural_language_grounding_loss: float
    no_fairness_rotation_loss: float
    no_outcome_feedback_loss: float
    no_trace_replay_loss: float
    supports_infrastructure_proposal_governance_bridge: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_infrastructure_proposal_governance", True, True, True, True, True, True, True, True),
    Condition("no_agent_created_proposals", False, True, True, True, True, True, True, True),
    Condition("no_conflict_priority_arbitration", True, False, True, True, True, True, True, True),
    Condition("no_scarce_budget", True, True, False, True, True, True, True, True),
    Condition("no_maintenance_debt", True, True, True, False, True, True, True, True),
    Condition("no_cultural_language_grounding", True, True, True, True, False, True, True, True),
    Condition("no_fairness_rotation", True, True, True, True, True, False, True, True),
    Condition("no_outcome_feedback", True, True, True, True, True, True, False, True),
    Condition("no_trace_replay", True, True, True, True, True, True, True, False),
)


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
    if not isinstance(state, dict) or "projects" not in state or "routes" not in state or "objects" not in state:
        raise ValueError(f"Report 148 state artifact is invalid: {path}")
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


def sensory_wave(packet: dict[str, object], council: int, condition: Condition) -> float:
    if not condition.cultural_language_grounding:
        return 0.20
    rates = packet.get("sensory_rates_hz", {})
    audio = float(rates.get("audio", 3.0)) if isinstance(rates, dict) else 3.0
    affect = float(rates.get("affect", 8.0)) if isinstance(rates, dict) else 8.0
    phase = FLOWER_PHASES[council % len(FLOWER_PHASES)]
    return clamp(0.36 + (0.5 + 0.5 * math.sin(audio * 0.17 + affect * 0.07 + council * 0.21 + phase)) * 0.56)


def build_agents(source_agents: Sequence[dict[str, object]], source_state: dict[str, object]) -> dict[str, dict[str, object]]:
    prior = source_state.get("agents", {})
    if not isinstance(prior, dict):
        prior = {}
    agents = {}
    for packet in source_agents:
        agent_id = str(packet["agent_id"])
        live = copy.deepcopy(prior.get(agent_id, {}))
        if not live:
            live = {"agent_id": agent_id, "name": packet.get("name", agent_id), "role": packet.get("role", "agent"), "trust": 0.64}
        role = str(live.get("role", packet.get("role", "agent")))
        live["governance_memory"] = []
        live["proposal_count"] = 0
        live["accepted_count"] = 0
        live["budget_received"] = 0.0
        live["priority_debt"] = 0.0
        live["materials"] = copy.deepcopy(live.get("materials", {}))
        if not live["materials"]:
            for resource in ROLE_MATERIAL_AFFINITY.get(role, ("wood", "stone", "fiber")):
                live["materials"][resource] = 12
        agents[agent_id] = live
    return agents


def route_pressure(route: dict[str, object]) -> float:
    hazard = float(route.get("hazard", 0.2))
    cost = float(route.get("cost_multiplier", 1.0))
    maintenance = float(route.get("maintenance_load", 0.0))
    quality = float(route.get("quality", 0.6))
    return clamp(hazard * 0.38 + max(0.0, cost - 0.65) * 0.24 + maintenance * 0.24 + (1.0 - quality) * 0.14)


def object_pressure(obj: dict[str, object]) -> float:
    accessibility = float(obj.get("accessibility", 0.55))
    integrity = float(obj.get("integrity", 0.6))
    pathogen = float(obj.get("pathogen", 0.08))
    stock = float(obj.get("stock", 0.6))
    return clamp((1.0 - accessibility) * 0.34 + (1.0 - integrity) * 0.24 + pathogen * 0.24 + (1.0 - stock) * 0.18)


def project_pressure(project: dict[str, object]) -> float:
    integrity = float(project.get("integrity", 0.8))
    maintained = int(project.get("maintained", 0))
    load = 0.18 if maintained < 2 else 0.04
    return clamp((1.0 - integrity) * 0.78 + load)


def proposal_kind(agent: dict[str, object], route: dict[str, object], obj: dict[str, object], project: dict[str, object], condition: Condition) -> str:
    role = str(agent.get("role", "agent"))
    if condition.maintenance_debt and project_pressure(project) > 0.24:
        return "maintenance_debt"
    if route_pressure(route) > 0.26 and role in {"scout", "guard", "builder", "trader"}:
        return "route_safety"
    if object_pressure(obj) > 0.24 and role in {"farmer", "trader", "builder"}:
        return "object_access"
    if str(obj.get("kind", "")) == "sanitation" or role == "healer":
        return "sanitation_repair"
    if role in {"guard", "pattern_keeper"}:
        return "signal_visibility"
    if str(obj.get("kind", "")) in {"water", "storage"}:
        return "water_security"
    if role in {"teacher", "healer"}:
        return "care_access"
    return "language_marker"


def make_requirement(kind: str, severity: float, role: str) -> dict[str, int]:
    base = max(2, int(math.ceil(2 + severity * 6)))
    if kind == "maintenance_debt":
        keys = ("wood", "stone", "fiber")
    elif kind == "route_safety":
        keys = ("stone", "wood", "charcoal")
    elif kind == "object_access":
        keys = ("wood", "clay", "fiber")
    elif kind == "sanitation_repair":
        keys = ("ash", "stone", "wood")
    elif kind == "signal_visibility":
        keys = ("resin", "charcoal", "wood")
    elif kind == "water_security":
        keys = ("clay", "stone", "wood")
    elif kind == "care_access":
        keys = ("fiber", "hide", "wood")
    else:
        keys = ("stone", "charcoal", "clay")
    affinity = ROLE_MATERIAL_AFFINITY.get(role, ())
    return {key: base + (1 if key not in affinity else 0) for key in keys}


def generate_proposal(council: int, slot: int, agent: dict[str, object], packet: dict[str, object], routes: dict[str, dict[str, object]], objects: dict[str, dict[str, object]], projects: dict[str, dict[str, object]], condition: Condition) -> dict[str, object] | None:
    if not condition.agent_created_proposals:
        return None
    route_values = list(routes.values())
    object_values = [obj for obj in objects.values() if isinstance(obj, dict)]
    project_values = [project for project in projects.values() if isinstance(project, dict)]
    if not route_values or not object_values or not project_values:
        return None
    role = str(agent.get("role", "agent"))
    route = max(route_values, key=lambda item: route_pressure(item) + ((len(str(item.get("src", ""))) + slot) % 5) * 0.004)
    obj = max(object_values, key=lambda item: object_pressure(item) + ((len(str(item.get("id", ""))) + council) % 7) * 0.003)
    project = max(project_values, key=lambda item: project_pressure(item) + ((len(str(item.get("id", ""))) + slot) % 6) * 0.004)
    kind = proposal_kind(agent, route, obj, project, condition)
    route_p = route_pressure(route)
    obj_p = object_pressure(obj)
    debt_p = project_pressure(project) if condition.maintenance_debt else 0.0
    severity = clamp(max(route_p, obj_p, debt_p) + sensory_wave(packet, council + slot, condition) * 0.08)
    focus = PROPOSAL_FOCUS[kind]
    token = token_for_focus(packet, focus) if condition.cultural_language_grounding else "ungrounded"
    requirements = make_requirement(kind, severity, role)
    proposal = {
        "id": f"c{council:02d}_{slot:02d}_{role}_{kind}_{str(route.get('src', 'x'))}_{str(obj.get('id', 'object'))}",
        "council": council,
        "agent_id": agent.get("agent_id"),
        "agent_name": agent.get("name"),
        "role": role,
        "kind": kind,
        "route": [route.get("src"), route.get("dst")],
        "object": obj.get("id"),
        "project": project.get("id"),
        "severity": round(severity, 6),
        "route_pressure": round(route_p, 6),
        "object_pressure": round(obj_p, 6),
        "maintenance_pressure": round(debt_p, 6),
        "focus": focus,
        "native_token": token,
        "requirements": requirements,
        "requested_budget": sum(requirements.values()),
        "score": 0.0,
        "accepted": False,
        "allocated": 0,
        "completed": False,
        "rejected_reason": "pending",
    }
    agent["proposal_count"] = int(agent.get("proposal_count", 0)) + 1
    return proposal


def available_budget(agents: dict[str, dict[str, object]], council: int, condition: Condition) -> dict[str, int]:
    if not condition.scarce_budget:
        return {}
    budget = {"wood": 12 + council % 3, "stone": 12, "fiber": 10, "clay": 9, "resin": 7, "charcoal": 8, "ash": 7, "hide": 5}
    for agent in agents.values():
        materials = agent.get("materials", {})
        if not isinstance(materials, dict):
            continue
        for key in list(budget):
            budget[key] += min(2, int(materials.get(key, 0)) // 8)
    return budget


def score_proposal(proposal: dict[str, object], agents: dict[str, dict[str, object]], accepted_by_role: dict[str, int], condition: Condition) -> float:
    if not condition.conflict_priority_arbitration:
        return 0.40 + (proposal["council"] % 4) * 0.01
    role = str(proposal["role"])
    urgency = float(proposal["severity"])
    route_need = float(proposal["route_pressure"])
    object_need = float(proposal["object_pressure"])
    debt_need = float(proposal["maintenance_pressure"])
    fairness = 0.0
    if condition.fairness_rotation:
        fairness = max(0.0, 0.16 - accepted_by_role.get(role, 0) * 0.035)
    token_bonus = 0.07 if condition.cultural_language_grounding and proposal["native_token"] != "ungrounded" else 0.0
    social = mean(float(agent.get("trust", 0.6)) for agent in agents.values()) * 0.06
    score = urgency * 0.46 + route_need * 0.16 + object_need * 0.14 + debt_need * 0.14 + fairness + token_bonus + social
    return round(score, 6)


def allocate_budget(proposal: dict[str, object], budget: dict[str, int], condition: Condition) -> tuple[bool, int]:
    if not condition.scarce_budget:
        proposal["allocated"] = 0
        proposal["rejected_reason"] = "budget-channel-disabled"
        return False, 0
    requirements = proposal["requirements"]
    for key, amount in requirements.items():
        if int(budget.get(key, 0)) < int(amount):
            proposal["rejected_reason"] = "scarce-budget-rejected"
            return False, 0
    allocated = 0
    for key, amount in requirements.items():
        budget[key] -= int(amount)
        allocated += int(amount)
    proposal["allocated"] = allocated
    return True, allocated


def apply_completed_proposal(proposal: dict[str, object], routes: dict[str, dict[str, object]], objects: dict[str, dict[str, object]], projects: dict[str, dict[str, object]], condition: Condition) -> dict[str, float]:
    route_delta = 0.0
    object_delta = 0.0
    debt_delta = 0.0
    if not condition.outcome_feedback:
        return {"route_delta": 0.0, "object_delta": 0.0, "debt_delta": 0.0}
    for route in routes.values():
        if [route.get("src"), route.get("dst")] == proposal["route"] or [route.get("dst"), route.get("src")] == proposal["route"]:
            before = float(route.get("hazard", 0.2)) + float(route.get("cost_multiplier", 1.0))
            route["hazard"] = clamp(float(route.get("hazard", 0.2)) - 0.025 - float(proposal["severity"]) * 0.030)
            route["cost_multiplier"] = clamp(float(route.get("cost_multiplier", 1.0)) - 0.020 - float(proposal["severity"]) * 0.025, 0.40, 1.20)
            route.setdefault("governance_changes", []).append(proposal["id"])
            after = float(route.get("hazard", 0.2)) + float(route.get("cost_multiplier", 1.0))
            route_delta += max(0.0, before - after)
    obj = objects.get(str(proposal["object"]))
    if isinstance(obj, dict):
        before = float(obj.get("accessibility", 0.5)) + float(obj.get("integrity", 0.6)) - float(obj.get("pathogen", 0.1))
        obj["accessibility"] = clamp(float(obj.get("accessibility", 0.5)) + 0.030 + float(proposal["severity"]) * 0.035)
        obj["integrity"] = clamp(float(obj.get("integrity", 0.6)) + 0.020)
        obj["pathogen"] = clamp(float(obj.get("pathogen", 0.1)) - 0.010)
        obj.setdefault("governance_links", []).append(proposal["id"])
        after = float(obj.get("accessibility", 0.5)) + float(obj.get("integrity", 0.6)) - float(obj.get("pathogen", 0.1))
        object_delta += max(0.0, after - before)
    project = projects.get(str(proposal["project"]))
    if isinstance(project, dict) and condition.maintenance_debt:
        before = float(project.get("integrity", 0.7))
        project["integrity"] = clamp(float(project.get("integrity", 0.7)) + 0.050)
        project.setdefault("governance_maintenance", []).append(proposal["id"])
        debt_delta = max(0.0, float(project.get("integrity", 0.7)) - before)
    return {"route_delta": round(route_delta, 6), "object_delta": round(object_delta, 6), "debt_delta": round(debt_delta, 6)}


def run_condition(cfg: GovernanceConfig, condition: Condition, source_agents: Sequence[dict[str, object]], source_state: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    agents = build_agents(source_agents, source_state)
    routes = copy.deepcopy(source_state.get("routes", {})) if isinstance(source_state.get("routes", {}), dict) else {}
    objects = copy.deepcopy(source_state.get("objects", {})) if isinstance(source_state.get("objects", {}), dict) else {}
    projects = copy.deepcopy(source_state.get("projects", {})) if isinstance(source_state.get("projects", {}), dict) else {}
    governance_history: list[dict[str, object]] = []
    trace: list[dict[str, object]] = []
    generated = 0
    accepted = 0
    completed = 0
    budgeted = 0
    maintenance_served = 0
    token_grounded = 0
    overreach_rejected = 0
    pressure_scores: list[float] = []
    feedback_events = 0
    accepted_by_role: dict[str, int] = {}

    for council in range(1, cfg.councils + 1):
        season = GOVERNANCE_SEASONS[(council - 1) % len(GOVERNANCE_SEASONS)]
        proposals = []
        for slot in range(cfg.proposals_per_council):
            packet = source_agents[(council + slot - 1) % len(source_agents)]
            agent = agents[str(packet["agent_id"])]
            proposal = generate_proposal(council, slot, agent, packet, routes, objects, projects, condition)
            if proposal is None:
                continue
            proposal["score"] = score_proposal(proposal, agents, accepted_by_role, condition)
            proposals.append(proposal)
            generated += 1
            pressure_scores.append(max(float(proposal["route_pressure"]), float(proposal["object_pressure"]), float(proposal["maintenance_pressure"])))
            token_grounded += 1 if condition.cultural_language_grounding and proposal["native_token"] != "ungrounded" else 0
        if not condition.conflict_priority_arbitration:
            ranked = proposals[: max(1, cfg.proposals_per_council // 3)]
        else:
            ranked = sorted(proposals, key=lambda item: item["score"], reverse=True)
        budget = available_budget(agents, council, condition)
        accepted_this_council = []
        max_accept = 4 if condition.conflict_priority_arbitration else 2
        for proposal in ranked:
            if len(accepted_this_council) >= max_accept:
                proposal["rejected_reason"] = "priority-conflict-lost"
                continue
            ok, allocated = allocate_budget(proposal, budget, condition)
            if not ok:
                overreach_rejected += 1 if condition.scarce_budget else 0
                continue
            proposal["accepted"] = True
            proposal["rejected_reason"] = "accepted"
            accepted += 1
            budgeted += 1 if allocated > 0 else 0
            accepted_by_role[str(proposal["role"])] = accepted_by_role.get(str(proposal["role"]), 0) + 1
            agent = agents[str(proposal["agent_id"])]
            agent["accepted_count"] = int(agent.get("accepted_count", 0)) + 1
            agent["budget_received"] = float(agent.get("budget_received", 0.0)) + allocated
            feedback = apply_completed_proposal(proposal, routes, objects, projects, condition)
            proposal["feedback"] = feedback
            proposal["completed"] = condition.outcome_feedback
            completed += 1 if proposal["completed"] else 0
            feedback_events += 1 if condition.outcome_feedback and (feedback["route_delta"] > 0 or feedback["object_delta"] > 0 or feedback["debt_delta"] > 0) else 0
            maintenance_served += 1 if proposal["kind"] == "maintenance_debt" and feedback.get("debt_delta", 0) > 0 else 0
            memory = agent.setdefault("governance_memory", [])
            if isinstance(memory, list):
                memory.append({"council": council, "proposal": proposal["id"], "kind": proposal["kind"], "accepted": True, "season": season})
            accepted_this_council.append(proposal)
        council_row = {
            "council": council,
            "season": season,
            "generated": len(proposals),
            "accepted": len(accepted_this_council),
            "budget_remaining": budget,
            "accepted_proposals": accepted_this_council,
            "rejected_count": max(0, len(proposals) - len(accepted_this_council)),
        }
        governance_history.append(council_row)
        if condition.trace_replay:
            trace.append(council_row)

    proposal_generation_rate = generated / max(1, cfg.councils * cfg.proposals_per_council)
    pressure_grounding_score = mean(pressure_scores)
    priority_conflict_resolution_rate = accepted / max(1, generated) if condition.conflict_priority_arbitration else 0.0
    scarce_budget_allocation_rate = budgeted / max(1, accepted) if condition.scarce_budget else 0.0
    debt_denominator = max(1, sum(1 for proposal in [p for council in governance_history for p in council.get("accepted_proposals", [])] if proposal.get("kind") == "maintenance_debt"))
    maintenance_debt_service_rate = maintenance_served / debt_denominator if condition.maintenance_debt else 0.0
    cultural_token_grounding_rate = token_grounded / max(1, generated) if condition.cultural_language_grounding else 0.0
    if condition.fairness_rotation and accepted_by_role:
        values = list(accepted_by_role.values())
        fairness_rotation_score = clamp(1.0 - ((max(values) - min(values)) / max(1, sum(values))))
    else:
        fairness_rotation_score = 0.0
    outcome_feedback_rate = feedback_events / max(1, accepted) if condition.outcome_feedback else 0.0
    accepted_completion_rate = completed / max(1, accepted)
    rejected_overreach_rate = overreach_rejected / max(1, generated - accepted) if condition.scarce_budget else 0.0
    governance_history_persistence = 1.0 if governance_history and any(c["accepted"] for c in governance_history) else 0.0
    trace_completeness = 1.0 if condition.trace_replay and len(trace) == cfg.councils else 0.0
    readiness = (
        proposal_generation_rate * 0.11
        + pressure_grounding_score * 0.10
        + priority_conflict_resolution_rate * 0.11
        + scarce_budget_allocation_rate * 0.10
        + maintenance_debt_service_rate * 0.10
        + cultural_token_grounding_rate * 0.09
        + fairness_rotation_score * 0.09
        + outcome_feedback_rate * 0.10
        + accepted_completion_rate * 0.09
        + rejected_overreach_rate * 0.05
        + governance_history_persistence * 0.08
        + trace_completeness * 0.08
    )
    row = EvalRow(
        condition=condition.name,
        councils=cfg.councils,
        generated_proposals=generated,
        accepted_proposals=accepted,
        completed_allocations=completed,
        proposal_generation_rate=round(proposal_generation_rate, 6),
        pressure_grounding_score=round(pressure_grounding_score, 6),
        priority_conflict_resolution_rate=round(priority_conflict_resolution_rate, 6),
        scarce_budget_allocation_rate=round(scarce_budget_allocation_rate, 6),
        maintenance_debt_service_rate=round(maintenance_debt_service_rate, 6),
        cultural_token_grounding_rate=round(cultural_token_grounding_rate, 6),
        fairness_rotation_score=round(fairness_rotation_score, 6),
        outcome_feedback_rate=round(outcome_feedback_rate, 6),
        accepted_completion_rate=round(accepted_completion_rate, 6),
        rejected_overreach_rate=round(rejected_overreach_rate, 6),
        governance_history_persistence=round(governance_history_persistence, 6),
        trace_completeness=round(trace_completeness, 6),
        proposal_governance_readiness=round(readiness, 6),
    )
    state = {
        "condition": condition.name,
        "councils": cfg.councils,
        "agents": agents,
        "routes": routes,
        "objects": objects,
        "projects": projects,
        "governance_history": governance_history,
        "accepted_by_role": accepted_by_role,
    }
    return row, trace, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_infrastructure_proposal_governance"]

    def loss(condition: str) -> float:
        return round(full.proposal_governance_readiness - by_name[condition].proposal_governance_readiness, 6)

    supports = (
        full.proposal_governance_readiness >= 0.70
        and full.proposal_generation_rate >= 0.90
        and full.pressure_grounding_score >= 0.20
        and full.priority_conflict_resolution_rate >= 0.20
        and full.scarce_budget_allocation_rate >= 0.95
        and full.maintenance_debt_service_rate >= 0.80
        and full.cultural_token_grounding_rate >= 0.95
        and full.fairness_rotation_score >= 0.85
        and full.outcome_feedback_rate >= 0.95
        and full.accepted_completion_rate >= 0.95
        and full.governance_history_persistence >= 1.0
        and full.trace_completeness >= 1.0
        and loss("no_agent_created_proposals") >= 0.45
        and by_name["no_conflict_priority_arbitration"].priority_conflict_resolution_rate <= 0.0
        and by_name["no_scarce_budget"].scarce_budget_allocation_rate <= 0.0
        and by_name["no_maintenance_debt"].maintenance_debt_service_rate <= 0.0
        and by_name["no_cultural_language_grounding"].cultural_token_grounding_rate <= 0.0
        and by_name["no_fairness_rotation"].fairness_rotation_score <= 0.0
        and by_name["no_outcome_feedback"].outcome_feedback_rate <= 0.0
        and by_name["no_trace_replay"].trace_completeness <= 0.0
    )
    return VerdictRow(
        full_condition=full.condition,
        full_proposal_governance_readiness=full.proposal_governance_readiness,
        full_proposal_generation_rate=full.proposal_generation_rate,
        full_pressure_grounding_score=full.pressure_grounding_score,
        full_priority_conflict_resolution_rate=full.priority_conflict_resolution_rate,
        full_scarce_budget_allocation_rate=full.scarce_budget_allocation_rate,
        full_maintenance_debt_service_rate=full.maintenance_debt_service_rate,
        full_cultural_token_grounding_rate=full.cultural_token_grounding_rate,
        full_fairness_rotation_score=full.fairness_rotation_score,
        full_outcome_feedback_rate=full.outcome_feedback_rate,
        full_accepted_completion_rate=full.accepted_completion_rate,
        full_rejected_overreach_rate=full.rejected_overreach_rate,
        full_governance_history_persistence=full.governance_history_persistence,
        full_trace_completeness=full.trace_completeness,
        no_agent_created_proposals_loss=loss("no_agent_created_proposals"),
        no_conflict_priority_arbitration_loss=loss("no_conflict_priority_arbitration"),
        no_scarce_budget_loss=loss("no_scarce_budget"),
        no_maintenance_debt_loss=loss("no_maintenance_debt"),
        no_cultural_language_grounding_loss=loss("no_cultural_language_grounding"),
        no_fairness_rotation_loss=loss("no_fairness_rotation"),
        no_outcome_feedback_loss=loss("no_outcome_feedback"),
        no_trace_replay_loss=loss("no_trace_replay"),
        supports_infrastructure_proposal_governance_bridge=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "partial_or_failed",
    )


def run_benchmark(cfg: GovernanceConfig) -> dict[str, object]:
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
        "report": 149,
        "name": "SSRM-3D Infrastructure Proposal Governance Bridge",
        "config": asdict(cfg),
        "eval": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "trace": traces["integrated_infrastructure_proposal_governance"],
        "final_state": states["integrated_infrastructure_proposal_governance"],
        "source_agents": source_agents,
        "notes": {
            "claim": "deterministic bridge from fixed infrastructure projects to agent-created proposals, priority conflict, scarce budgets, maintenance debt, native-token grounding, fairness, and governance histories",
            "not_claimed": "subjective consciousness, LLM open dialogue, complete playable world, or unscripted civilization emergence",
            "governance_basis": "pressure-derived proposals, council arbitration, scarce budget allocation, maintenance debt service, token grounding, fairness rotation, outcome feedback, and replay traces",
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", payload)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", payload["trace"])
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", payload["final_state"])
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_INFRASTRUCTURE_PROPOSAL_GOVERNANCE_BRIDGE_RESULTS", payload)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_INFRASTRUCTURE_PROPOSAL_GOVERNANCE_BRIDGE_TRACE", payload["trace"])
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_INFRASTRUCTURE_PROPOSAL_GOVERNANCE_BRIDGE_STATE", payload["final_state"])
    return payload


def parse_args() -> GovernanceConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260623)
    parser.add_argument("--councils", type=int, default=18)
    parser.add_argument("--proposals-per-council", type=int, default=8)
    parser.add_argument("--source-agents", default=str(SOURCE_AGENTS))
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    if args.councils < 8:
        raise SystemExit("--councils must be at least 8")
    if args.proposals_per_council < 4:
        raise SystemExit("--proposals-per-council must be at least 4")
    return GovernanceConfig(seed=args.seed, councils=args.councils, proposals_per_council=args.proposals_per_council, source_agents=args.source_agents, source_state=args.source_state)


def main() -> None:
    payload = run_benchmark(parse_args())
    print(json.dumps(payload["verdict"], indent=2))


if __name__ == "__main__":
    main()
