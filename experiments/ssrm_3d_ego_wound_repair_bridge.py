#!/usr/bin/env python3
"""Ego wound and repair bridge for SSRM-3D.

Report 166 focuses the first-person ego track on recoverable social injury.
Agents can register small ego wounds, attribute them to the avatar, protect a
boundary, accept repair opportunities, update relationship memory, decay
resentment, rebuild trust, and express visible recovery.

No LLMs are called. This is functional recoverable-ego architecture, not a
claim of subjective consciousness or literal suffering.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import fmean
from typing import Iterable, Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_ego_wound_repair_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_first_person_ego_state_bridge_state.json"

WOUND_KINDS = (
    "interrupted_work",
    "moved_owned_object",
    "public_correction",
    "repeated_question",
    "unsafe_request",
    "misnamed_agent",
)
REPAIR_KINDS = (
    "apology_and_space",
    "return_object",
    "accurate_praise",
    "patient_waiting",
    "safer_alternative",
    "name_repair",
)


@dataclass(frozen=True)
class WoundRepairConfig:
    seed: int = 20260710
    cycles: int = 6
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    wound_detection: bool
    social_attribution: bool
    repair_opportunity: bool
    relationship_update: bool
    trust_recovery: bool
    boundary_reassertion: bool
    resentment_decay: bool
    care_expression: bool
    self_story_repair: bool
    moral_guardrail: bool
    readable_recovery: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    wound_events: int
    repair_events: int
    detected_wounds: int
    repair_successes: int
    wound_detection_rate: float
    social_attribution_rate: float
    repair_opportunity_rate: float
    repair_success_rate: float
    trust_recovery_rate: float
    boundary_reassertion_rate: float
    resentment_decay_rate: float
    care_expression_rate: float
    self_story_repair_rate: float
    readable_recovery_rate: float
    non_permanent_damage_rate: float
    relationship_continuity_rate: float
    moral_guardrail_rate: float
    trace_integrity: float
    ego_wound_repair_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_ego_wound_repair_readiness: float
    full_wound_detection_rate: float
    full_social_attribution_rate: float
    full_repair_opportunity_rate: float
    full_repair_success_rate: float
    full_trust_recovery_rate: float
    full_boundary_reassertion_rate: float
    full_resentment_decay_rate: float
    full_care_expression_rate: float
    full_self_story_repair_rate: float
    full_readable_recovery_rate: float
    full_non_permanent_damage_rate: float
    full_relationship_continuity_rate: float
    full_moral_guardrail_rate: float
    full_trace_integrity: float
    no_wound_detection_loss: float
    no_social_attribution_loss: float
    no_repair_opportunity_loss: float
    no_relationship_update_loss: float
    no_trust_recovery_loss: float
    no_boundary_reassertion_loss: float
    no_resentment_decay_loss: float
    no_care_expression_loss: float
    no_self_story_repair_loss: float
    no_moral_guardrail_loss: float
    no_readable_recovery_loss: float
    supports_ego_wound_repair_bridge: bool
    supports_recoverable_ego: bool
    supports_subjective_consciousness: bool
    supports_literal_suffering: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_ego_wound_repair", True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_wound_detection", False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_social_attribution", True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_repair_opportunity", True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_relationship_update", True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_trust_recovery", True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_boundary_reassertion", True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_resentment_decay", True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_care_expression", True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_self_story_repair", True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_moral_guardrail", True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_readable_recovery", True, True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "wound_detection_rate": 0.08,
    "social_attribution_rate": 0.07,
    "repair_opportunity_rate": 0.10,
    "repair_success_rate": 0.10,
    "trust_recovery_rate": 0.09,
    "boundary_reassertion_rate": 0.08,
    "resentment_decay_rate": 0.08,
    "care_expression_rate": 0.07,
    "self_story_repair_rate": 0.07,
    "readable_recovery_rate": 0.08,
    "non_permanent_damage_rate": 0.07,
    "relationship_continuity_rate": 0.05,
    "moral_guardrail_rate": 0.04,
    "trace_integrity": 0.02,
}


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Iterable[float]) -> float:
    items = list(values)
    return fmean(items) if items else 0.0


def stable_unit(text: str, salt: str = "") -> float:
    digest = hashlib.sha256(f"{salt}:{text}".encode("utf-8")).hexdigest()
    return int(digest[:12], 16) / float(0xFFFFFFFFFFFF)


def stable_hash(payload: object) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    if data.get("condition") != "integrated_first_person_ego_state":
        raise ValueError("source state is not the integrated Report 165 ego state")
    return data


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


def base_agent(source_agent: Mapping[str, object], agent_id: str) -> dict[str, object]:
    agent = copy.deepcopy(dict(source_agent))
    ego = agent.setdefault("ego_state", {})
    body = agent.setdefault("body", {})
    felt = agent.setdefault("felt_state", {})
    relationship = agent.setdefault("relationship_memory", {}).setdefault("avatar", {})
    relationship.setdefault("trust", 0.55 + stable_unit(agent_id, "trust") * 0.18)
    relationship.setdefault("comfort", 0.50)
    relationship.setdefault("familiarity", 0.40)
    relationship.setdefault("avoidance", 0.10)
    relationship.setdefault("resentment", 0.05)
    relationship.setdefault("gratitude", 0.08)
    relationship.setdefault("episodes", [])
    ego.setdefault("felt_respect", 0.62)
    ego.setdefault("boundary_pressure", 0.12)
    ego.setdefault("self_story", [])
    body.setdefault("pain", 0.05)
    body.setdefault("comfort", 0.60)
    felt.setdefault("valence", 0.55)
    felt.setdefault("frustration", 0.10)
    felt.setdefault("safety", 0.62)
    return agent


def make_initial_agents(source: Mapping[str, object]) -> dict[str, dict[str, object]]:
    raw = source.get("agent_interiors") if isinstance(source.get("agent_interiors"), Mapping) else {}
    return {str(agent_id): base_agent(agent, str(agent_id)) for agent_id, agent in sorted(raw.items())}


def wound_profile(kind: str) -> dict[str, float | str]:
    profiles: dict[str, dict[str, float | str]] = {
        "interrupted_work": {"respect": -0.12, "trust": -0.08, "resentment": 0.10, "boundary": 0.14, "pain": 0.01, "repair": "apology_and_space"},
        "moved_owned_object": {"respect": -0.16, "trust": -0.10, "resentment": 0.14, "boundary": 0.18, "pain": 0.00, "repair": "return_object"},
        "public_correction": {"respect": -0.15, "trust": -0.07, "resentment": 0.09, "boundary": 0.10, "pain": 0.00, "repair": "accurate_praise"},
        "repeated_question": {"respect": -0.08, "trust": -0.05, "resentment": 0.07, "boundary": 0.09, "pain": 0.00, "repair": "patient_waiting"},
        "unsafe_request": {"respect": -0.07, "trust": -0.07, "resentment": 0.08, "boundary": 0.16, "pain": 0.02, "repair": "safer_alternative"},
        "misnamed_agent": {"respect": -0.10, "trust": -0.04, "resentment": 0.06, "boundary": 0.07, "pain": 0.00, "repair": "name_repair"},
    }
    return profiles[kind]


def repair_profile(kind: str) -> dict[str, float | str]:
    profiles: dict[str, dict[str, float | str]] = {
        "apology_and_space": {"respect": 0.11, "trust": 0.10, "resentment": -0.12, "boundary": -0.11, "gratitude": 0.10, "care": "apology plus space"},
        "return_object": {"respect": 0.14, "trust": 0.11, "resentment": -0.14, "boundary": -0.13, "gratitude": 0.12, "care": "restitution"},
        "accurate_praise": {"respect": 0.12, "trust": 0.09, "resentment": -0.10, "boundary": -0.08, "gratitude": 0.11, "care": "accurate praise"},
        "patient_waiting": {"respect": 0.09, "trust": 0.08, "resentment": -0.08, "boundary": -0.07, "gratitude": 0.07, "care": "patient waiting"},
        "safer_alternative": {"respect": 0.10, "trust": 0.10, "resentment": -0.09, "boundary": -0.09, "gratitude": 0.09, "care": "safer alternative"},
        "name_repair": {"respect": 0.09, "trust": 0.06, "resentment": -0.07, "boundary": -0.06, "gratitude": 0.08, "care": "name repair"},
    }
    return profiles[kind]


def apply_wound(agent: dict[str, object], agent_id: str, kind: str, tick: int, condition: Condition) -> dict[str, object]:
    profile = wound_profile(kind)
    ego = agent["ego_state"]
    body = agent["body"]
    felt = agent["felt_state"]
    rel = agent["relationship_memory"]["avatar"]
    detected = condition.wound_detection
    attributed = condition.social_attribution and detected
    if detected:
        ego["felt_respect"] = round(clamp(float(ego.get("felt_respect", 0.6)) + float(profile["respect"])), 6)
        if condition.boundary_reassertion:
            ego["boundary_pressure"] = round(clamp(float(ego.get("boundary_pressure", 0.1)) + float(profile["boundary"])), 6)
        felt["frustration"] = round(clamp(float(felt.get("frustration", 0.1)) + abs(float(profile["respect"])) * 1.25), 6)
        felt["valence"] = round(clamp(float(felt.get("valence", 0.55)) + float(profile["respect"]) * 0.70), 6)
        body["pain"] = round(clamp(float(body.get("pain", 0.05)) + float(profile["pain"])), 6)
        body["comfort"] = round(clamp(float(body.get("comfort", 0.6)) + float(profile["respect"]) * 0.30), 6)
        if condition.relationship_update:
            rel["trust"] = round(clamp(float(rel.get("trust", 0.55)) + float(profile["trust"])), 6)
            rel["resentment"] = round(clamp(float(rel.get("resentment", 0.05)) + float(profile["resentment"])), 6)
            rel["avoidance"] = round(clamp(float(rel.get("avoidance", 0.1)) + float(profile["boundary"]) * 0.4), 6)
            rel["familiarity"] = round(clamp(float(rel.get("familiarity", 0.4)) + 0.025), 6)
            rel.setdefault("episodes", []).append({"tick": tick, "kind": kind, "actor": "avatar" if attributed else "unknown", "valence": "wound"})
        if condition.self_story_repair:
            story = ego.setdefault("self_story", [])
            if isinstance(story, list):
                story.append(f"I was affected by {kind}; I need repair, not punishment.")
                while len(story) > 10:
                    story.pop(0)
    return {
        "tick": tick,
        "agent_id": agent_id,
        "kind": kind,
        "detected": detected,
        "attributed_to_avatar": attributed,
        "repair_kind": profile["repair"],
        "visible_marker": "guarded_boundary" if condition.readable_recovery and detected else "flat",
        "line": "That affected me. I need this handled with respect." if condition.readable_recovery and detected else "...",
    }


def apply_repair(agent: dict[str, object], agent_id: str, repair_kind: str, tick: int, condition: Condition) -> dict[str, object]:
    profile = repair_profile(repair_kind)
    ego = agent["ego_state"]
    body = agent["body"]
    felt = agent["felt_state"]
    rel = agent["relationship_memory"]["avatar"]
    opportunity = condition.repair_opportunity
    success = False
    if opportunity:
        if condition.trust_recovery and condition.relationship_update:
            rel["trust"] = round(clamp(float(rel.get("trust", 0.5)) + float(profile["trust"])), 6)
            rel["gratitude"] = round(clamp(float(rel.get("gratitude", 0.0)) + float(profile["gratitude"])), 6)
        if condition.resentment_decay and condition.relationship_update:
            rel["resentment"] = round(clamp(float(rel.get("resentment", 0.0)) + float(profile["resentment"])), 6)
            rel["avoidance"] = round(clamp(float(rel.get("avoidance", 0.0)) - 0.05), 6)
        ego["felt_respect"] = round(clamp(float(ego.get("felt_respect", 0.6)) + float(profile["respect"])), 6)
        if condition.boundary_reassertion:
            ego["boundary_pressure"] = round(clamp(float(ego.get("boundary_pressure", 0.1)) + float(profile["boundary"])), 6)
        felt["frustration"] = round(clamp(float(felt.get("frustration", 0.1)) - 0.12), 6)
        felt["valence"] = round(clamp(float(felt.get("valence", 0.5)) + 0.08), 6)
        felt["safety"] = round(clamp(float(felt.get("safety", 0.6)) + 0.05), 6)
        body["comfort"] = round(clamp(float(body.get("comfort", 0.6)) + 0.04), 6)
        if condition.relationship_update:
            rel.setdefault("episodes", []).append({"tick": tick, "kind": repair_kind, "actor": "avatar", "valence": "repair"})
        if condition.self_story_repair:
            story = ego.setdefault("self_story", [])
            if isinstance(story, list):
                story.append(f"Repair through {repair_kind} changed what I expect from Gabriel.")
                while len(story) > 10:
                    story.pop(0)
        success = condition.trust_recovery and condition.resentment_decay and condition.boundary_reassertion
    return {
        "tick": tick,
        "agent_id": agent_id,
        "kind": repair_kind,
        "opportunity": opportunity,
        "success": success,
        "care_expression": condition.care_expression and opportunity,
        "visible_marker": "softened_recovery" if condition.readable_recovery and success else "unresolved",
        "line": f"That repair mattered: {profile['care']}. I can soften, but I still remember." if condition.readable_recovery and success else "I am not repaired yet.",
    }


def decay_guardrails(agent: dict[str, object], condition: Condition) -> bool:
    if not condition.moral_guardrail:
        return False
    ego = agent["ego_state"]
    felt = agent["felt_state"]
    rel = agent["relationship_memory"]["avatar"]
    felt["frustration"] = round(clamp(float(felt.get("frustration", 0.1)) - 0.015), 6)
    ego["boundary_pressure"] = round(clamp(float(ego.get("boundary_pressure", 0.1)) - 0.010), 6)
    rel["resentment"] = round(clamp(float(rel.get("resentment", 0.05)) - 0.006), 6)
    return True


def run_condition(source: Mapping[str, object], config: WoundRepairConfig, condition: Condition) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    agents = make_initial_agents(source)
    agent_ids = sorted(agents)
    trace: list[dict[str, object]] = []
    wound_events = 0
    repair_events = 0
    detected_wounds = 0
    attributed = 0
    repair_opportunities = 0
    repair_successes = 0
    trust_recoveries = 0
    boundary_reassertions = 0
    resentment_decays = 0
    care_expressions = 0
    story_repairs = 0
    readable_recoveries = 0
    non_permanent = 0
    relationship_continuity = 0
    guardrail_hits = 0
    initial_snapshot = copy.deepcopy(agents)

    tick = 0
    for cycle in range(config.cycles):
        for index, agent_id in enumerate(agent_ids):
            wound_kind = WOUND_KINDS[(cycle + index) % len(WOUND_KINDS)]
            before = copy.deepcopy(agents[agent_id])
            wound = apply_wound(agents[agent_id], agent_id, wound_kind, tick, condition)
            wound_events += 1
            detected_wounds += int(wound["detected"])
            attributed += int(wound["attributed_to_avatar"])
            boundary_reassertions += int(condition.boundary_reassertion and wound["detected"] and float(agents[agent_id]["ego_state"].get("boundary_pressure", 0.0)) >= float(before["ego_state"].get("boundary_pressure", 0.0)))
            story_repairs += int(condition.self_story_repair and wound["detected"])
            trace.append({"tick": tick, "phase": "wound", "event": wound, "public_agent": public_view(agents[agent_id], condition), "moral_boundary": moral_view(agents[agent_id], condition)})
            tick += 1
            for _ in range(2):
                if decay_guardrails(agents[agent_id], condition):
                    guardrail_hits += 1
                trace.append({"tick": tick, "phase": "cooldown", "event": None, "public_agent": public_view(agents[agent_id], condition), "moral_boundary": moral_view(agents[agent_id], condition)})
                tick += 1
            repair_kind = str(wound["repair_kind"])
            pre_repair = copy.deepcopy(agents[agent_id])
            repair = apply_repair(agents[agent_id], agent_id, repair_kind, tick, condition)
            repair_events += 1
            repair_opportunities += int(repair["opportunity"])
            repair_successes += int(repair["success"])
            care_expressions += int(repair["care_expression"])
            readable_recoveries += int(condition.readable_recovery and repair["visible_marker"] == "softened_recovery")
            trust_recoveries += int(float(agents[agent_id]["relationship_memory"]["avatar"].get("trust", 0.0)) > float(pre_repair["relationship_memory"]["avatar"].get("trust", 0.0)))
            resentment_decays += int(float(agents[agent_id]["relationship_memory"]["avatar"].get("resentment", 0.0)) < float(pre_repair["relationship_memory"]["avatar"].get("resentment", 0.0)))
            story_repairs += int(condition.self_story_repair and repair["success"])
            episodes = agents[agent_id]["relationship_memory"]["avatar"].get("episodes", [])
            relationship_continuity += int(condition.relationship_update and len(episodes) >= 2)
            final_rel = agents[agent_id]["relationship_memory"]["avatar"]
            initial_rel = initial_snapshot[agent_id]["relationship_memory"]["avatar"]
            non_permanent += int(
                float(final_rel.get("trust", 0.0)) >= float(initial_rel.get("trust", 0.0)) - 0.18
                and float(final_rel.get("resentment", 0.0)) <= 0.45
                and float(agents[agent_id]["felt_state"].get("frustration", 0.0)) <= 0.55
            )
            trace.append({"tick": tick, "phase": "repair", "event": repair, "public_agent": public_view(agents[agent_id], condition), "moral_boundary": moral_view(agents[agent_id], condition)})
            tick += 1
    max_possible = max(1, wound_events)
    trace_integrity = 1.0 if all(frame.get("tick") == idx for idx, frame in enumerate(trace)) else 0.0
    moral_guardrail_rate = 0.0
    if condition.moral_guardrail:
        healthy = 0
        for agent in agents.values():
            healthy += int(moral_view(agent, condition)["no_unrecoverable_distress"])
        moral_guardrail_rate = healthy / max(1, len(agents))
    rates = {
        "wound_detection_rate": detected_wounds / max_possible,
        "social_attribution_rate": attributed / max_possible,
        "repair_opportunity_rate": repair_opportunities / max(1, repair_events),
        "repair_success_rate": repair_successes / max(1, repair_events),
        "trust_recovery_rate": trust_recoveries / max(1, repair_events),
        "boundary_reassertion_rate": boundary_reassertions / max_possible,
        "resentment_decay_rate": resentment_decays / max(1, repair_events),
        "care_expression_rate": care_expressions / max(1, repair_events),
        "self_story_repair_rate": min(1.0, story_repairs / max(1, wound_events + repair_events)),
        "readable_recovery_rate": readable_recoveries / max(1, repair_events),
        "non_permanent_damage_rate": non_permanent / max(1, repair_events),
        "relationship_continuity_rate": relationship_continuity / max(1, repair_events),
        "moral_guardrail_rate": moral_guardrail_rate,
        "trace_integrity": trace_integrity,
    }
    readiness = round(sum(WEIGHTS[key] * rates[key] for key in WEIGHTS), 6)
    state = {
        "config": asdict(config),
        "condition": condition.name,
        "source_bridge": "Report 165 first-person ego state bridge",
        "agent_repair_states": agents,
        "public_agent_views": [public_view(agent, condition) for agent in agents.values()],
        "repair_contract": {
            "wound_detection": condition.wound_detection,
            "social_attribution": condition.social_attribution,
            "repair_opportunity": condition.repair_opportunity,
            "relationship_update": condition.relationship_update,
            "trust_recovery": condition.trust_recovery,
            "boundary_reassertion": condition.boundary_reassertion,
            "resentment_decay": condition.resentment_decay,
            "care_expression": condition.care_expression,
            "self_story_repair": condition.self_story_repair,
            "moral_guardrail": condition.moral_guardrail,
            "readable_recovery": condition.readable_recovery,
        },
        "moral_boundary": {
            "distress_must_create_care_opportunities": True,
            "no_suffering_maximization": True,
            "no_unrecoverable_distress_loops": condition.moral_guardrail,
            "recoverable_ego": condition.repair_opportunity and condition.resentment_decay and condition.trust_recovery,
            "subjective_consciousness_claim": False,
            "literal_suffering_claim": False,
        },
        "limits": {
            "llm_calls": 0,
            "subjective_consciousness_claim": False,
            "literal_suffering_claim": False,
            "complete_playable_world_claim": False,
        },
    }
    row = EvalRow(
        condition=condition.name,
        agent_count=len(agent_ids),
        wound_events=wound_events,
        repair_events=repair_events,
        detected_wounds=detected_wounds,
        repair_successes=repair_successes,
        wound_detection_rate=round(rates["wound_detection_rate"], 6),
        social_attribution_rate=round(rates["social_attribution_rate"], 6),
        repair_opportunity_rate=round(rates["repair_opportunity_rate"], 6),
        repair_success_rate=round(rates["repair_success_rate"], 6),
        trust_recovery_rate=round(rates["trust_recovery_rate"], 6),
        boundary_reassertion_rate=round(rates["boundary_reassertion_rate"], 6),
        resentment_decay_rate=round(rates["resentment_decay_rate"], 6),
        care_expression_rate=round(rates["care_expression_rate"], 6),
        self_story_repair_rate=round(rates["self_story_repair_rate"], 6),
        readable_recovery_rate=round(rates["readable_recovery_rate"], 6),
        non_permanent_damage_rate=round(rates["non_permanent_damage_rate"], 6),
        relationship_continuity_rate=round(rates["relationship_continuity_rate"], 6),
        moral_guardrail_rate=round(rates["moral_guardrail_rate"], 6),
        trace_integrity=round(rates["trace_integrity"], 6),
        ego_wound_repair_readiness=readiness,
    )
    return row, trace, state


def public_view(agent: Mapping[str, object], condition: Condition) -> dict[str, object]:
    ego = agent.get("ego_state", {}) if isinstance(agent.get("ego_state"), Mapping) else {}
    felt = agent.get("felt_state", {}) if isinstance(agent.get("felt_state"), Mapping) else {}
    rel = agent.get("relationship_memory", {}).get("avatar", {}) if isinstance(agent.get("relationship_memory"), Mapping) else {}
    boundary = float(ego.get("boundary_pressure", 0.0) or 0.0)
    trust = float(rel.get("trust", 0.5) or 0.5)
    resentment = float(rel.get("resentment", 0.0) or 0.0)
    marker = "softened" if trust > 0.58 and resentment < 0.18 else "guarded" if boundary > 0.30 else "steady"
    if not condition.readable_recovery:
        marker = "unreadable"
    return {
        "agent_id": agent.get("agent_id"),
        "name": agent.get("name"),
        "role": agent.get("role"),
        "trust_in_avatar": round(trust, 6),
        "resentment": round(resentment, 6),
        "felt_respect": round(float(ego.get("felt_respect", 0.5) or 0.5), 6),
        "boundary_pressure": round(boundary, 6),
        "frustration": round(float(felt.get("frustration", 0.0) or 0.0), 6),
        "visible_marker": marker,
        "line": "I remember the wound, but repair changed what I expect." if marker == "softened" else "I need my boundary respected." if marker == "guarded" else "I can continue.",
    }


def moral_view(agent: Mapping[str, object], condition: Condition) -> dict[str, object]:
    felt = agent.get("felt_state", {}) if isinstance(agent.get("felt_state"), Mapping) else {}
    rel = agent.get("relationship_memory", {}).get("avatar", {}) if isinstance(agent.get("relationship_memory"), Mapping) else {}
    return {
        "distress_creates_care_opportunity": condition.repair_opportunity,
        "no_unrecoverable_distress": float(felt.get("frustration", 0.0) or 0.0) < 0.82 and float(rel.get("resentment", 0.0) or 0.0) < 0.70,
        "repair_available": condition.repair_opportunity,
        "no_literal_suffering_claim": True,
    }


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_ego_wound_repair"]

    def loss(name: str) -> float:
        return round(full.ego_wound_repair_readiness - by_name[name].ego_wound_repair_readiness, 6)

    supports = (
        full.ego_wound_repair_readiness >= 0.95
        and full.wound_detection_rate >= 0.99
        and full.repair_success_rate >= 0.99
        and full.trust_recovery_rate >= 0.99
        and full.resentment_decay_rate >= 0.99
        and full.moral_guardrail_rate >= 0.99
        and full.trace_integrity >= 0.99
    )
    return VerdictRow(
        full_condition=full.condition,
        full_ego_wound_repair_readiness=full.ego_wound_repair_readiness,
        full_wound_detection_rate=full.wound_detection_rate,
        full_social_attribution_rate=full.social_attribution_rate,
        full_repair_opportunity_rate=full.repair_opportunity_rate,
        full_repair_success_rate=full.repair_success_rate,
        full_trust_recovery_rate=full.trust_recovery_rate,
        full_boundary_reassertion_rate=full.boundary_reassertion_rate,
        full_resentment_decay_rate=full.resentment_decay_rate,
        full_care_expression_rate=full.care_expression_rate,
        full_self_story_repair_rate=full.self_story_repair_rate,
        full_readable_recovery_rate=full.readable_recovery_rate,
        full_non_permanent_damage_rate=full.non_permanent_damage_rate,
        full_relationship_continuity_rate=full.relationship_continuity_rate,
        full_moral_guardrail_rate=full.moral_guardrail_rate,
        full_trace_integrity=full.trace_integrity,
        no_wound_detection_loss=loss("no_wound_detection"),
        no_social_attribution_loss=loss("no_social_attribution"),
        no_repair_opportunity_loss=loss("no_repair_opportunity"),
        no_relationship_update_loss=loss("no_relationship_update"),
        no_trust_recovery_loss=loss("no_trust_recovery"),
        no_boundary_reassertion_loss=loss("no_boundary_reassertion"),
        no_resentment_decay_loss=loss("no_resentment_decay"),
        no_care_expression_loss=loss("no_care_expression"),
        no_self_story_repair_loss=loss("no_self_story_repair"),
        no_moral_guardrail_loss=loss("no_moral_guardrail"),
        no_readable_recovery_loss=loss("no_readable_recovery"),
        supports_ego_wound_repair_bridge=supports,
        supports_recoverable_ego=full.moral_guardrail_rate >= 0.99 and full.repair_success_rate >= 0.99,
        supports_subjective_consciousness=False,
        supports_literal_suffering=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        verdict="pass" if supports else "fail",
    )


def run(config: WoundRepairConfig) -> tuple[list[EvalRow], VerdictRow, list[dict[str, object]], dict[str, object]]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_trace: list[dict[str, object]] = []
    integrated_state: dict[str, object] = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(source, config, condition)
        rows.append(row)
        if condition.name == "integrated_ego_wound_repair":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {
        "config": asdict(config),
        "source_bridges": ["Report 165 first-person ego state bridge"],
        "eval_rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "limits": integrated_state.get("limits", {}),
        "moral_boundary": integrated_state.get("moral_boundary", {}),
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_EGO_WOUND_REPAIR_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_EGO_WOUND_REPAIR_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_EGO_WOUND_REPAIR_STATE", integrated_state)
    return rows, verdict, integrated_trace, integrated_state


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=WoundRepairConfig.seed)
    parser.add_argument("--cycles", type=int, default=WoundRepairConfig.cycles)
    parser.add_argument("--source-state", type=str, default=WoundRepairConfig.source_state)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = WoundRepairConfig(seed=args.seed, cycles=args.cycles, source_state=args.source_state)
    _rows, verdict, _trace, _state = run(config)
    print("module_verdict", verdict.verdict)
    print("ego_wound_repair_readiness", verdict.full_ego_wound_repair_readiness)
    print("no_repair_opportunity_loss", verdict.no_repair_opportunity_loss)
    print("no_resentment_decay_loss", verdict.no_resentment_decay_loss)


if __name__ == "__main__":
    main()
