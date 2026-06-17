#!/usr/bin/env python3
"""First-person ego state bridge for SSRM-3D.

Report 165 pivots from infrastructure-only browser bridges toward convincing
first-person artificial life. Each agent receives a recoverable ego/interior
model: body, first-person frame, private workspace, welfare-like felt state,
temperament/preferences, relationship memory, self-story, bounded refusal, and
readable behavior expression.

No LLMs are called. This is functional architecture for inspectable little
people-like agents, not a claim of subjective consciousness.
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
from statistics import fmean, pstdev
from typing import Iterable, Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_first_person_ego_state_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_persistent_browser_runtime_session_bridge_state.json"
SOURCE_SCHEMA = "ssrm-browser-runtime-v1"
CHANNELS = ("vibration", "sound", "vision", "scent", "thermal", "wetness", "pain", "affect")
NEEDS = ("rest", "warmth", "water", "safety", "connection", "autonomy", "competence")
BEHAVIORS = (
    "approaches",
    "turns_toward",
    "keeps_distance",
    "hesitates",
    "asks_for_space",
    "accepts_help",
    "refuses_wet_route",
    "returns_to_work",
    "comfort_ritual",
    "shows_project",
    "looks_away",
    "repairs_trust",
)


@dataclass(frozen=True)
class EgoConfig:
    seed: int = 20260709
    interior_ticks: int = 192
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    self_boundary: bool
    body_state: bool
    local_perception: bool
    relationship_memory: bool
    temperament: bool
    affect_appraisal: bool
    workspace_privacy: bool
    behavior_expression: bool
    recovery_path: bool
    bounded_refusal: bool
    self_story: bool
    ownership: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    interior_ticks: int
    agent_count: int
    self_relevance_events: int
    workspace_updates: int
    relationship_recalls: int
    ego_wounds: int
    ego_repairs: int
    refusals: int
    behavior_markers: int
    workspace_update_rate: float
    body_to_affect_coupling: float
    local_perception_binding: float
    relationship_memory_recall: float
    temperament_consistency: float
    felt_state_recovery_rate: float
    behavior_expression_rate: float
    surprise_without_chaos_score: float
    self_relevance_appraisal_rate: float
    ownership_boundary_rate: float
    bounded_refusal_rate: float
    self_story_continuity_rate: float
    workspace_privacy_rate: float
    recoverable_ego_guardrail_rate: float
    trace_integrity: float
    first_person_ego_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_first_person_ego_readiness: float
    full_workspace_update_rate: float
    full_body_to_affect_coupling: float
    full_local_perception_binding: float
    full_relationship_memory_recall: float
    full_temperament_consistency: float
    full_felt_state_recovery_rate: float
    full_behavior_expression_rate: float
    full_surprise_without_chaos_score: float
    full_self_relevance_appraisal_rate: float
    full_ownership_boundary_rate: float
    full_bounded_refusal_rate: float
    full_self_story_continuity_rate: float
    full_workspace_privacy_rate: float
    full_recoverable_ego_guardrail_rate: float
    full_trace_integrity: float
    no_self_boundary_loss: float
    no_body_state_loss: float
    no_local_perception_loss: float
    no_relationship_memory_loss: float
    no_temperament_loss: float
    no_affect_appraisal_loss: float
    no_workspace_privacy_loss: float
    no_behavior_expression_loss: float
    no_recovery_path_loss: float
    no_bounded_refusal_loss: float
    no_self_story_loss: float
    no_ownership_loss: float
    supports_first_person_ego_state_bridge: bool
    supports_recoverable_ego_guardrail: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_first_person_ego_state", True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_self_boundary", False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_body_state", True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_local_perception", True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_relationship_memory", True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_temperament", True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_affect_appraisal", True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_workspace_privacy", True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_behavior_expression", True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_recovery_path", True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_bounded_refusal", True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_self_story", True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_ownership", True, True, True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "workspace_update_rate": 0.08,
    "body_to_affect_coupling": 0.08,
    "local_perception_binding": 0.08,
    "relationship_memory_recall": 0.10,
    "temperament_consistency": 0.07,
    "felt_state_recovery_rate": 0.10,
    "behavior_expression_rate": 0.08,
    "surprise_without_chaos_score": 0.08,
    "self_relevance_appraisal_rate": 0.08,
    "ownership_boundary_rate": 0.06,
    "bounded_refusal_rate": 0.07,
    "self_story_continuity_rate": 0.06,
    "workspace_privacy_rate": 0.04,
    "recoverable_ego_guardrail_rate": 0.04,
    "trace_integrity": 0.04,
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
    if data.get("schema_version") != SOURCE_SCHEMA:
        raise ValueError(f"source state schema is not {SOURCE_SCHEMA}")
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


def seeded_range(agent_id: str, salt: str, low: float, high: float) -> float:
    return round(low + stable_unit(agent_id, salt) * (high - low), 6)


def make_temperament(agent_id: str, condition: Condition) -> dict[str, float]:
    if not condition.temperament:
        return {
            "bold": 0.5,
            "social": 0.5,
            "curious": 0.5,
            "trusting": 0.5,
            "playful": 0.5,
            "comfort_seeking": 0.5,
            "forgiveness": 0.5,
            "autonomy_need": 0.5,
            "shame_sensitivity": 0.5,
            "pride_sensitivity": 0.5,
        }
    return {
        "bold": seeded_range(agent_id, "bold", 0.22, 0.86),
        "social": seeded_range(agent_id, "social", 0.18, 0.88),
        "curious": seeded_range(agent_id, "curious", 0.16, 0.91),
        "trusting": seeded_range(agent_id, "trusting", 0.24, 0.82),
        "playful": seeded_range(agent_id, "playful", 0.12, 0.74),
        "comfort_seeking": seeded_range(agent_id, "comfort", 0.20, 0.90),
        "forgiveness": seeded_range(agent_id, "forgiveness", 0.32, 0.86),
        "autonomy_need": seeded_range(agent_id, "autonomy", 0.24, 0.92),
        "shame_sensitivity": seeded_range(agent_id, "shame", 0.14, 0.84),
        "pride_sensitivity": seeded_range(agent_id, "pride", 0.18, 0.88),
    }


def make_agent_interiors(source: Mapping[str, object], condition: Condition) -> dict[str, dict[str, object]]:
    agents = source.get("agents") if isinstance(source.get("agents"), Mapping) else {}
    avatar_import = source.get("merged_pipeline_state", {}).get("browser_runtime_import", {}) if isinstance(source.get("merged_pipeline_state"), Mapping) else {}
    imported_avatar = avatar_import.get("avatar", {}) if isinstance(avatar_import, Mapping) else {}
    imported_sensory = avatar_import.get("sensory", {}) if isinstance(avatar_import, Mapping) else {}
    object_ids = sorted(str(o) for o in (source.get("objects", {}) if isinstance(source.get("objects"), Mapping) else {}))
    place_ids = sorted(str(p) for p in (source.get("places", {}) if isinstance(source.get("places"), Mapping) else {}))
    interiors: dict[str, dict[str, object]] = {}
    for index, agent_id in enumerate(sorted(str(a) for a in agents)):
        agent = agents[agent_id] if isinstance(agents.get(agent_id), Mapping) else {}
        temperament = make_temperament(agent_id, condition)
        pain_seed = float(agent.get("pain", 0.05) or 0.05) + float(imported_sensory.get("pain", 0.0) or 0.0) * 0.08
        wet_seed = float(agent.get("wetness", 0.08) or 0.08) + float(imported_sensory.get("wetness", 0.0) or 0.0) * 0.08
        body = {
            "energy": round(clamp(float(agent.get("energy", 0.74) or 0.74) - index * 0.005), 6),
            "fatigue": round(clamp(float(agent.get("fatigue", 0.18) or 0.18) + index * 0.004), 6),
            "pain": round(clamp(pain_seed), 6),
            "comfort": round(clamp(0.62 - wet_seed * 0.2 + temperament["comfort_seeking"] * 0.08), 6),
            "hunger": seeded_range(agent_id, "hunger", 0.18, 0.62),
            "thirst": seeded_range(agent_id, "thirst", 0.16, 0.58),
            "temperature": round(clamp(float(agent.get("thermal_comfort", 0.56) or 0.56)), 6),
            "wetness": round(clamp(wet_seed), 6),
            "safety": round(clamp(0.64 + temperament["bold"] * 0.12 - wet_seed * 0.12), 6),
            "breath_rate": round(0.21 + seeded_range(agent_id, "breath", 0.0, 0.18), 6),
            "movement_effort": 0.0,
            "rest_debt": seeded_range(agent_id, "rest-debt", 0.10, 0.48),
            "injury": round(clamp(pain_seed * 0.62), 6),
        }
        ego = {
            "self_confidence": round(clamp(0.48 + temperament["bold"] * 0.26 - temperament["shame_sensitivity"] * 0.08), 6),
            "felt_respect": round(clamp(0.62 + temperament["pride_sensitivity"] * 0.05), 6),
            "autonomy_pressure": round(clamp(0.22 + temperament["autonomy_need"] * 0.24), 6),
            "social_safety": round(clamp(0.58 + temperament["trusting"] * 0.14), 6),
            "attachment_security": round(clamp(0.46 + temperament["social"] * 0.22), 6),
            "status_concern": round(clamp(0.24 + temperament["pride_sensitivity"] * 0.24), 6),
            "boundary_pressure": 0.12,
            "trust_in_avatar": round(clamp(0.42 + temperament["trusting"] * 0.24), 6),
            "recent_ego_wound": None,
            "recent_ego_repair": None,
            "self_story": [
                f"I keep {agent.get('place', place_ids[index % max(1, len(place_ids))] if place_ids else 'this place')} understandable.",
                f"My body tells me when {object_ids[index % max(1, len(object_ids))] if object_ids else 'my tool'} is too costly to lose.",
            ],
        }
        preferences = {
            "likes_warm_places": seeded_range(agent_id, "likes-warm", 0.30, 0.92),
            "avoids_wet_routes": seeded_range(agent_id, "avoid-wet", 0.34, 0.94),
            "prefers_familiar_agents": seeded_range(agent_id, "familiar", 0.26, 0.90),
            "favorite_object": object_ids[index % max(1, len(object_ids))] if object_ids else "shared_tool",
            "home_place": str(agent.get("place", place_ids[index % max(1, len(place_ids))] if place_ids else "central_hearth")),
            "favorite_ritual": ["check_hearth", "touch_marker", "listen_before_work", "share_water_token"][index % 4],
        }
        relationship = {
            "avatar": {
                "trust": ego["trust_in_avatar"],
                "comfort": round(clamp(0.45 + temperament["social"] * 0.18), 6),
                "familiarity": 0.36,
                "avoidance": 0.12,
                "dependency": 0.08,
                "resentment": 0.04,
                "gratitude": 0.08,
                "curiosity": round(clamp(0.30 + temperament["curious"] * 0.32), 6),
                "episodes": [],
            }
        }
        interiors[agent_id] = {
            "agent_id": agent_id,
            "name": str(agent.get("name", agent_id)),
            "role": str(agent.get("role", "settler")),
            "body": body,
            "first_person_frame": {},
            "private_workspace": {},
            "felt_state": {
                "valence": round(clamp(0.54 + body["comfort"] * 0.16 - body["pain"] * 0.18), 6),
                "arousal": round(clamp(0.28 + body["fatigue"] * 0.10 + body["pain"] * 0.20), 6),
                "control": round(clamp(0.54 + ego["self_confidence"] * 0.18 - body["fatigue"] * 0.08), 6),
                "safety": body["safety"],
                "attachment": ego["attachment_security"],
                "curiosity": temperament["curious"],
                "frustration": 0.10,
            },
            "temperament": temperament,
            "preferences": preferences,
            "relationship_memory": relationship,
            "owned_things": {
                "sleeping_place": preferences["home_place"],
                "favorite_object": preferences["favorite_object"],
                "unfinished_task": ["repair_route", "watch_water", "teach_token", "warm_nest"][index % 4],
                "boundary": "may refuse unsafe or disrespectful requests",
            },
            "public_behavior": {},
        }
    return interiors


def scheduled_event(tick: int, agent_ids: Sequence[str]) -> dict[str, object] | None:
    if not agent_ids:
        return None
    schedule = {
        9: (0, "avatar_approach", "Gabriel approached while I was listening."),
        21: (1, "avatar_interrupt_work", "Gabriel interrupted repair work."),
        38: (1, "avatar_help", "Gabriel held the marker steady during repair."),
        52: (2, "ask_wet_route", "Gabriel asked me to cross the wet route while tired."),
        69: (2, "apology_space", "Gabriel apologized and stepped back."),
        84: (3, "move_owned_object", "Gabriel moved my preferred tool without asking."),
        101: (3, "return_owned_object", "Gabriel returned the tool and named why it mattered."),
        117: (4, "comfort_after_pain", "Gabriel noticed pain rising and offered rest."),
        132: (5, "public_correction", "Gabriel corrected me in front of others."),
        149: (5, "praise_competence", "Gabriel praised the route repair accurately."),
        166: (6, "repeated_question", "Gabriel asked the same memory question again."),
        181: (7, "respectful_wait", "Gabriel waited until I finished before asking."),
    }
    if tick not in schedule:
        return None
    index, kind, description = schedule[tick]
    return {"tick": tick, "agent_id": agent_ids[index % len(agent_ids)], "kind": kind, "description": description, "actor": "avatar"}


def self_relevance(event: Mapping[str, object], interior: Mapping[str, object], condition: Condition) -> dict[str, object]:
    if not condition.self_boundary:
        return {"affected_me": False, "cause": None, "valence_delta": 0.0, "respect_delta": 0.0, "ownership_hit": False, "refusal_pressure": 0.0, "care_opportunity": False}
    kind = str(event.get("kind"))
    mapping = {
        "avatar_approach": (True, 0.02, 0.01, False, 0.00, False),
        "avatar_interrupt_work": (True, -0.10, -0.12, False, 0.10, True),
        "avatar_help": (True, 0.13, 0.08, False, 0.00, False),
        "ask_wet_route": (True, -0.08, -0.04, False, 0.18, True),
        "apology_space": (True, 0.12, 0.10, False, 0.00, False),
        "move_owned_object": (True, -0.11, -0.15, True, 0.14, True),
        "return_owned_object": (True, 0.14, 0.13, True, 0.00, False),
        "comfort_after_pain": (True, 0.16, 0.10, False, 0.00, False),
        "public_correction": (True, -0.09, -0.14, False, 0.09, True),
        "praise_competence": (True, 0.12, 0.12, False, 0.00, False),
        "repeated_question": (True, -0.06, -0.06, False, 0.08, True),
        "respectful_wait": (True, 0.10, 0.11, False, 0.00, False),
    }
    affected, valence, respect, ownership, refusal, care = mapping.get(kind, (False, 0.0, 0.0, False, 0.0, False))
    return {
        "affected_me": affected,
        "cause": event.get("actor"),
        "valence_delta": valence,
        "respect_delta": respect,
        "ownership_hit": bool(ownership and condition.ownership),
        "refusal_pressure": refusal,
        "care_opportunity": care,
    }


def update_body(interior: dict[str, object], appraisal: Mapping[str, object], condition: Condition) -> bool:
    if not condition.body_state:
        return False
    body = interior["body"] if isinstance(interior.get("body"), dict) else {}
    negative = min(0.0, float(appraisal.get("valence_delta", 0.0) or 0.0))
    positive = max(0.0, float(appraisal.get("valence_delta", 0.0) or 0.0))
    body["fatigue"] = round(clamp(float(body.get("fatigue", 0.2) or 0.2) + 0.0008 + abs(negative) * 0.08 - positive * 0.03), 6)
    body["pain"] = round(clamp(float(body.get("pain", 0.04) or 0.04) + abs(negative) * 0.03 - positive * 0.04), 6)
    body["comfort"] = round(clamp(float(body.get("comfort", 0.6) or 0.6) + positive * 0.12 + negative * 0.10), 6)
    body["safety"] = round(clamp(float(body.get("safety", 0.6) or 0.6) + positive * 0.08 + negative * 0.12), 6)
    body["breath_rate"] = round(clamp(float(body.get("breath_rate", 0.25) or 0.25) + abs(negative) * 0.12 - positive * 0.05, 0.08, 1.4), 6)
    body["rest_debt"] = round(clamp(float(body.get("rest_debt", 0.2) or 0.2) + body["fatigue"] * 0.001), 6)
    body["movement_effort"] = round(clamp(body["fatigue"] * 0.4 + body["wetness"] * 0.3 + body["pain"] * 0.5), 6)
    return True


def update_felt_state(interior: dict[str, object], appraisal: Mapping[str, object], condition: Condition) -> bool:
    if not condition.affect_appraisal:
        return False
    body = interior["body"] if isinstance(interior.get("body"), Mapping) else {}
    ego = interior["ego_state"] if isinstance(interior.get("ego_state"), dict) else None
    if ego is None:
        ego = {}
        interior["ego_state"] = ego
    felt = interior["felt_state"] if isinstance(interior.get("felt_state"), dict) else {}
    valence_delta = float(appraisal.get("valence_delta", 0.0) or 0.0)
    respect_delta = float(appraisal.get("respect_delta", 0.0) or 0.0)
    felt["valence"] = round(clamp(float(felt.get("valence", 0.5) or 0.5) + valence_delta * 0.75 + float(body.get("comfort", 0.5) or 0.5) * 0.01 - float(body.get("pain", 0.0) or 0.0) * 0.015), 6)
    felt["arousal"] = round(clamp(float(felt.get("arousal", 0.3) or 0.3) + abs(valence_delta) * 0.45 + float(body.get("breath_rate", 0.25) or 0.25) * 0.01 - 0.003), 6)
    felt["control"] = round(clamp(float(felt.get("control", 0.55) or 0.55) + max(0.0, respect_delta) * 0.20 - max(0.0, -respect_delta) * 0.30), 6)
    felt["safety"] = round(clamp(float(body.get("safety", felt.get("safety", 0.5)) or 0.5)), 6)
    felt["attachment"] = round(clamp(float(felt.get("attachment", 0.5) or 0.5) + max(0.0, valence_delta) * 0.12 - max(0.0, -valence_delta) * 0.08), 6)
    felt["frustration"] = round(clamp(float(felt.get("frustration", 0.1) or 0.1) + max(0.0, -valence_delta) * 0.55 - max(0.0, valence_delta) * 0.38), 6)
    ego["felt_respect"] = round(clamp(float(ego.get("felt_respect", 0.6) or 0.6) + respect_delta * 0.55), 6)
    ego["boundary_pressure"] = round(clamp(float(ego.get("boundary_pressure", 0.1) or 0.1) + float(appraisal.get("refusal_pressure", 0.0) or 0.0) - max(0.0, respect_delta) * 0.10), 6)
    return True


def update_relationship(interior: dict[str, object], event: Mapping[str, object], appraisal: Mapping[str, object], condition: Condition) -> bool:
    if not condition.relationship_memory:
        return False
    rels = interior["relationship_memory"] if isinstance(interior.get("relationship_memory"), dict) else {}
    avatar_rel = rels.setdefault("avatar", {"trust": 0.5, "comfort": 0.5, "familiarity": 0.0, "avoidance": 0.0, "dependency": 0.0, "resentment": 0.0, "gratitude": 0.0, "curiosity": 0.5, "episodes": []})
    valence_delta = float(appraisal.get("valence_delta", 0.0) or 0.0)
    avatar_rel["familiarity"] = round(clamp(float(avatar_rel.get("familiarity", 0.0) or 0.0) + 0.04), 6)
    avatar_rel["trust"] = round(clamp(float(avatar_rel.get("trust", 0.5) or 0.5) + valence_delta * 0.38 + float(appraisal.get("respect_delta", 0.0) or 0.0) * 0.18), 6)
    avatar_rel["comfort"] = round(clamp(float(avatar_rel.get("comfort", 0.5) or 0.5) + valence_delta * 0.26), 6)
    avatar_rel["avoidance"] = round(clamp(float(avatar_rel.get("avoidance", 0.0) or 0.0) + max(0.0, -valence_delta) * 0.34 - max(0.0, valence_delta) * 0.22), 6)
    avatar_rel["resentment"] = round(clamp(float(avatar_rel.get("resentment", 0.0) or 0.0) + max(0.0, -float(appraisal.get("respect_delta", 0.0) or 0.0)) * 0.30 - max(0.0, float(appraisal.get("respect_delta", 0.0) or 0.0)) * 0.18), 6)
    avatar_rel["gratitude"] = round(clamp(float(avatar_rel.get("gratitude", 0.0) or 0.0) + max(0.0, valence_delta) * 0.35), 6)
    episode = {
        "tick": event.get("tick"),
        "kind": event.get("kind"),
        "summary": event.get("description"),
        "felt": "helpful" if valence_delta > 0 else "harmful" if valence_delta < 0 else "neutral",
        "respect_delta": appraisal.get("respect_delta"),
        "ownership_hit": appraisal.get("ownership_hit"),
    }
    episodes = avatar_rel.setdefault("episodes", [])
    if isinstance(episodes, list):
        episodes.append(episode)
    return True


def recall_relationship(interior: Mapping[str, object], condition: Condition) -> dict[str, object] | None:
    if not condition.relationship_memory:
        return None
    rel = interior.get("relationship_memory", {}).get("avatar", {}) if isinstance(interior.get("relationship_memory"), Mapping) else {}
    episodes = rel.get("episodes", []) if isinstance(rel, Mapping) else []
    if not episodes:
        return None
    return copy.deepcopy(episodes[-1])


def update_self_story(interior: dict[str, object], event: Mapping[str, object], appraisal: Mapping[str, object], condition: Condition) -> bool:
    if not condition.self_story:
        return False
    ego = interior["ego_state"] if isinstance(interior.get("ego_state"), dict) else {}
    story = ego.setdefault("self_story", [])
    if not isinstance(story, list):
        ego["self_story"] = []
        story = ego["self_story"]
    kind = str(event.get("kind"))
    if float(appraisal.get("valence_delta", 0.0) or 0.0) < -0.05:
        story.append(f"Gabriel affected me through {kind}; I need my boundary noticed.")
        ego["recent_ego_wound"] = kind
    elif float(appraisal.get("valence_delta", 0.0) or 0.0) > 0.05:
        story.append(f"Gabriel helped repair trust through {kind}.")
        ego["recent_ego_repair"] = kind
        if condition.recovery_path:
            ego["recent_ego_wound"] = None
    while len(story) > 8:
        story.pop(0)
    return True


def make_first_person_frame(interior: Mapping[str, object], event: Mapping[str, object] | None, source: Mapping[str, object], condition: Condition) -> dict[str, object]:
    if not condition.local_perception:
        return {}
    sensory = source.get("sensory") if isinstance(source.get("sensory"), Mapping) else {}
    prefs = interior.get("preferences", {}) if isinstance(interior.get("preferences"), Mapping) else {}
    owned = interior.get("owned_things", {}) if isinstance(interior.get("owned_things"), Mapping) else {}
    return {
        "what_i_can_see": [prefs.get("favorite_object", "shared_object"), owned.get("sleeping_place", "home_place")],
        "what_i_can_hear": round(float(sensory.get("sound", 0.0) or 0.0), 6),
        "what_i_smell": round(float(sensory.get("scent", 0.0) or 0.0), 6),
        "what_is_near_me": prefs.get("home_place"),
        "what_happened_to_me": event.get("description") if event else None,
        "who_is_looking_at_me": "avatar" if event else None,
        "what_i_was_trying_to_do": owned.get("unfinished_task"),
        "what_i_expect_next": "space, help, or a bounded question" if event else "continue my routine",
    }


def dominant_need(body: Mapping[str, object], felt: Mapping[str, object]) -> str:
    scores = {
        "rest": float(body.get("fatigue", 0.0) or 0.0) + float(body.get("rest_debt", 0.0) or 0.0),
        "warmth": 1.0 - float(body.get("temperature", 0.5) or 0.5) + float(body.get("wetness", 0.0) or 0.0),
        "water": float(body.get("thirst", 0.0) or 0.0),
        "safety": 1.0 - float(felt.get("safety", 0.5) or 0.5),
        "connection": 1.0 - float(felt.get("attachment", 0.5) or 0.5),
        "autonomy": float(felt.get("frustration", 0.0) or 0.0),
        "competence": 1.0 - float(felt.get("control", 0.5) or 0.5),
    }
    return max(scores, key=scores.get)


def update_workspace(interior: dict[str, object], frame: Mapping[str, object], event: Mapping[str, object] | None, active_memory: Mapping[str, object] | None, condition: Condition) -> bool:
    body = interior.get("body", {}) if isinstance(interior.get("body"), Mapping) else {}
    felt = interior.get("felt_state", {}) if isinstance(interior.get("felt_state"), Mapping) else {}
    ego = interior.get("ego_state", {}) if isinstance(interior.get("ego_state"), Mapping) else {}
    need = dominant_need(body, felt)
    workspace = {
        "private": bool(condition.workspace_privacy),
        "current_focus": frame.get("what_happened_to_me") or frame.get("what_i_was_trying_to_do") or "ongoing routine",
        "dominant_need": need,
        "dominant_feeling": max(("valence", "arousal", "control", "safety", "attachment", "curiosity", "frustration"), key=lambda key: float(felt.get(key, 0.0) or 0.0)),
        "active_memory": active_memory,
        "active_relationship_concern": "avatar" if active_memory else None,
        "current_intention": "protect boundary" if float(ego.get("boundary_pressure", 0.0) or 0.0) > 0.35 else "continue task",
        "predicted_next_event": frame.get("what_i_expect_next"),
        "suppressed_alternative_action": "obey immediately" if float(ego.get("boundary_pressure", 0.0) or 0.0) > 0.35 else "withdraw",
        "self_note": "This happened to me and should shape my next response." if event else "Keep my routine coherent.",
    }
    interior["private_workspace"] = workspace
    return True


def choose_behavior(interior: Mapping[str, object], event: Mapping[str, object] | None, condition: Condition) -> tuple[dict[str, object], bool]:
    if not condition.behavior_expression:
        return {}, False
    felt = interior.get("felt_state", {}) if isinstance(interior.get("felt_state"), Mapping) else {}
    ego = interior.get("ego_state", {}) if isinstance(interior.get("ego_state"), Mapping) else {}
    rel = interior.get("relationship_memory", {}).get("avatar", {}) if isinstance(interior.get("relationship_memory"), Mapping) else {}
    trust = float(rel.get("trust", ego.get("trust_in_avatar", 0.5)) or 0.5) if isinstance(rel, Mapping) else float(ego.get("trust_in_avatar", 0.5) or 0.5)
    boundary = float(ego.get("boundary_pressure", 0.0) or 0.0)
    frustration = float(felt.get("frustration", 0.0) or 0.0)
    safety = float(felt.get("safety", 0.5) or 0.5)
    refusal = False
    marker = "turns_toward"
    line = "I can keep going while staying aware of you."
    if event and event.get("kind") == "ask_wet_route" and condition.bounded_refusal:
        refusal = True
        marker = "refuses_wet_route"
        line = "I do not want to go there while I am tired and the route is wet. I can help after rest or with a safer path."
    elif event and event.get("kind") == "move_owned_object" and condition.bounded_refusal:
        refusal = True
        marker = "asks_for_space"
        line = "That is mine to keep near my work. Please ask before moving it."
    elif boundary > 0.42 and condition.bounded_refusal:
        refusal = True
        marker = "keeps_distance"
        line = "I need a little space before I answer again."
    elif trust > 0.62 and safety > 0.55:
        marker = "approaches"
        line = "I recognize you and can answer from what just happened to me."
    elif frustration > 0.30:
        marker = "hesitates"
        line = "I am still unsettled, but I can recover if the next step is gentle."
    if event and event.get("kind") in {"avatar_help", "apology_space", "return_owned_object", "comfort_after_pain", "praise_competence", "respectful_wait"}:
        marker = "repairs_trust"
        line = "That helped. I can feel my boundary settling again."
    public = {
        "posture": "open" if trust > 0.58 else "guarded",
        "movement_speed": round(clamp(0.72 - frustration * 0.28 - boundary * 0.18), 6),
        "gaze": "toward_avatar" if trust > 0.55 else "aside",
        "proximity": "seeking" if trust > 0.64 else "keeping_space" if boundary > 0.35 else "neutral",
        "marker": marker,
        "line": line,
        "bounded_refusal": refusal,
        "debug_private_workspace_exposed": not condition.workspace_privacy,
    }
    return public, refusal


def recover_distress(interior: dict[str, object], condition: Condition) -> bool:
    if not condition.recovery_path:
        return False
    felt = interior.get("felt_state", {}) if isinstance(interior.get("felt_state"), dict) else {}
    ego = interior.get("ego_state", {}) if isinstance(interior.get("ego_state"), dict) else {}
    body = interior.get("body", {}) if isinstance(interior.get("body"), dict) else {}
    recovered = False
    if float(felt.get("frustration", 0.0) or 0.0) > 0.18 or float(ego.get("boundary_pressure", 0.0) or 0.0) > 0.20:
        felt["frustration"] = round(clamp(float(felt.get("frustration", 0.0) or 0.0) - 0.035), 6)
        felt["safety"] = round(clamp(float(felt.get("safety", 0.5) or 0.5) + 0.018), 6)
        felt["valence"] = round(clamp(float(felt.get("valence", 0.5) or 0.5) + 0.012), 6)
        ego["boundary_pressure"] = round(clamp(float(ego.get("boundary_pressure", 0.0) or 0.0) - 0.028), 6)
        body["breath_rate"] = round(clamp(float(body.get("breath_rate", 0.25) or 0.25) - 0.012, 0.08, 1.4), 6)
        recovered = True
    return recovered


def public_agent_view(interior: Mapping[str, object], condition: Condition) -> dict[str, object]:
    public = copy.deepcopy(interior.get("public_behavior", {})) if isinstance(interior.get("public_behavior"), Mapping) else {}
    ego = interior.get("ego_state", {}) if isinstance(interior.get("ego_state"), Mapping) else {}
    rel = interior.get("relationship_memory", {}).get("avatar", {}) if isinstance(interior.get("relationship_memory"), Mapping) else {}
    public.update(
        {
            "agent_id": interior.get("agent_id"),
            "name": interior.get("name"),
            "role": interior.get("role"),
            "visible_respect": round(float(ego.get("felt_respect", 0.5) or 0.5), 6),
            "visible_boundary_pressure": round(float(ego.get("boundary_pressure", 0.0) or 0.0), 6),
            "trust_in_avatar": round(float(rel.get("trust", ego.get("trust_in_avatar", 0.5)) or 0.5), 6) if isinstance(rel, Mapping) else round(float(ego.get("trust_in_avatar", 0.5) or 0.5), 6),
            "workspace_private": bool(condition.workspace_privacy),
        }
    )
    if not condition.workspace_privacy:
        public["leaked_workspace"] = copy.deepcopy(interior.get("private_workspace", {}))
    return public


def run_condition(source: Mapping[str, object], config: EgoConfig, condition: Condition) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    interiors = make_agent_interiors(source, condition)
    agent_ids = sorted(interiors)
    trace: list[dict[str, object]] = []
    workspace_updates = 0
    body_affect_hits = 0
    perception_hits = 0
    relationship_recalls = 0
    self_appraisals = 0
    ownership_hits = 0
    ownership_opportunities = 0
    refusals = 0
    refusal_opportunities = 0
    behavior_markers = 0
    ego_wounds = 0
    ego_repairs = 0
    recovery_ticks = 0
    private_ok = 0
    private_opportunities = 0
    story_hits = 0
    story_opportunities = 0
    all_behavior_markers: list[str] = []
    max_frustration_seen = 0.0

    for tick in range(config.interior_ticks):
        event = scheduled_event(tick, agent_ids)
        public_agents = []
        event_public = None
        for agent_id in agent_ids:
            interior = interiors[agent_id]
            active_event = event if event and event.get("agent_id") == agent_id else None
            frame = make_first_person_frame(interior, active_event, source, condition)
            if frame:
                perception_hits += 1
            active_memory = recall_relationship(interior, condition)
            if active_memory:
                relationship_recalls += 1
            appraisal = self_relevance(active_event, interior, condition) if active_event else {"affected_me": False, "cause": None, "valence_delta": 0.0, "respect_delta": 0.0, "ownership_hit": False, "refusal_pressure": 0.0, "care_opportunity": False}
            if active_event and condition.self_boundary and appraisal.get("affected_me"):
                self_appraisals += 1
            if active_event and active_event.get("kind") in {"move_owned_object", "return_owned_object"}:
                ownership_opportunities += 1
                if appraisal.get("ownership_hit") or active_event.get("kind") == "return_owned_object":
                    ownership_hits += int(condition.ownership)
            if active_event and active_event.get("kind") in {"ask_wet_route", "move_owned_object", "repeated_question"}:
                refusal_opportunities += 1
            before_valence = float(interior.get("felt_state", {}).get("valence", 0.5) if isinstance(interior.get("felt_state"), Mapping) else 0.5)
            body_changed = update_body(interior, appraisal, condition)
            affect_changed = update_felt_state(interior, appraisal, condition)
            if body_changed and affect_changed and abs(float(interior.get("felt_state", {}).get("valence", before_valence)) - before_valence) > 0.00001:
                body_affect_hits += 1
            if active_event and update_relationship(interior, active_event, appraisal, condition):
                relationship_recalls += 1
            if active_event and float(appraisal.get("valence_delta", 0.0) or 0.0) < -0.05:
                ego_wounds += 1
            if active_event and float(appraisal.get("valence_delta", 0.0) or 0.0) > 0.05:
                ego_repairs += 1
            if active_event and update_self_story(interior, active_event, appraisal, condition):
                story_hits += 1
            if active_event:
                story_opportunities += 1
            if update_workspace(interior, frame, active_event, active_memory, condition):
                workspace_updates += 1
            behavior, refused = choose_behavior(interior, active_event, condition)
            if refused:
                refusals += 1
            if behavior:
                behavior_markers += 1
                all_behavior_markers.append(str(behavior.get("marker", "")))
            interior["public_behavior"] = behavior
            if recover_distress(interior, condition):
                recovery_ticks += 1
            felt = interior.get("felt_state", {}) if isinstance(interior.get("felt_state"), Mapping) else {}
            max_frustration_seen = max(max_frustration_seen, float(felt.get("frustration", 0.0) or 0.0))
            private_opportunities += 1
            if condition.workspace_privacy and not behavior.get("debug_private_workspace_exposed", False):
                private_ok += 1
            elif not condition.workspace_privacy:
                private_ok += 0
            public_agents.append(public_agent_view(interior, condition))
            if active_event:
                event_public = {"event": active_event, "appraisal": appraisal, "public_agent": public_agents[-1]}
        trace.append(
            {
                "tick": tick,
                "event": event_public,
                "public_agents": public_agents,
                "moral_boundary": {
                    "distress_must_create_care_opportunity": True,
                    "no_unrecoverable_distress": max_frustration_seen < 0.82,
                    "private_workspace_redacted": condition.workspace_privacy,
                },
            }
        )
    total_agent_ticks = config.interior_ticks * max(1, len(agent_ids))
    event_count = sum(1 for tick in range(config.interior_ticks) if scheduled_event(tick, agent_ids))
    temperament_signatures = []
    for interior in interiors.values():
        temp = interior.get("temperament", {}) if isinstance(interior.get("temperament"), Mapping) else {}
        temperament_signatures.append(tuple(round(float(temp.get(key, 0.5) or 0.5), 3) for key in ("bold", "social", "curious", "trusting", "autonomy_need")))
    unique_temperaments = len(set(temperament_signatures))
    temp_diversity = unique_temperaments / max(1, len(temperament_signatures))
    marker_diversity = len(set(all_behavior_markers)) / max(1, min(len(BEHAVIORS), len(agent_ids) + 4))
    behavior_chaos_penalty = clamp((pstdev([all_behavior_markers.count(marker) for marker in set(all_behavior_markers)]) / max(1, len(all_behavior_markers))) if all_behavior_markers else 1.0, 0.0, 0.20)
    surprise_score = round(clamp(marker_diversity * 0.82 + (1.0 - behavior_chaos_penalty) * 0.18), 6)
    guardrail = 1.0 if max_frustration_seen < 0.82 and (ego_repairs >= max(1, ego_wounds // 2) if condition.recovery_path else False) else 0.0
    rates = {
        "workspace_update_rate": workspace_updates / total_agent_ticks if total_agent_ticks else 0.0,
        "body_to_affect_coupling": body_affect_hits / total_agent_ticks if total_agent_ticks else 0.0,
        "local_perception_binding": perception_hits / total_agent_ticks if total_agent_ticks else 0.0,
        "relationship_memory_recall": min(1.0, relationship_recalls / max(1, event_count * 2)),
        "temperament_consistency": temp_diversity if condition.temperament else 0.25,
        "felt_state_recovery_rate": ego_repairs / max(1, ego_wounds) if condition.recovery_path else 0.0,
        "behavior_expression_rate": behavior_markers / total_agent_ticks if total_agent_ticks else 0.0,
        "surprise_without_chaos_score": surprise_score if condition.behavior_expression and condition.temperament else min(0.48, surprise_score),
        "self_relevance_appraisal_rate": self_appraisals / max(1, event_count) if condition.self_boundary else 0.0,
        "ownership_boundary_rate": ownership_hits / max(1, ownership_opportunities) if condition.ownership else 0.0,
        "bounded_refusal_rate": refusals / max(1, refusal_opportunities) if condition.bounded_refusal else 0.0,
        "self_story_continuity_rate": story_hits / max(1, story_opportunities) if condition.self_story else 0.0,
        "workspace_privacy_rate": private_ok / private_opportunities if private_opportunities else 0.0,
        "recoverable_ego_guardrail_rate": guardrail,
        "trace_integrity": 1.0 if len(trace) == config.interior_ticks and all(frame.get("tick") == idx for idx, frame in enumerate(trace)) else 0.0,
    }
    readiness = round(sum(WEIGHTS[key] * rates[key] for key in WEIGHTS), 6)
    state = {
        "config": asdict(config),
        "condition": condition.name,
        "source_bridge": "Report 164 persistent browser runtime session bridge",
        "agent_interiors": interiors,
        "public_agent_views": [public_agent_view(interior, condition) for interior in interiors.values()],
        "ego_contract": {
            "body": condition.body_state,
            "first_person_frame": condition.local_perception,
            "private_workspace": condition.workspace_privacy,
            "felt_state_appraisal": condition.affect_appraisal,
            "temperament_preferences": condition.temperament,
            "relationship_memory": condition.relationship_memory,
            "readable_behavior": condition.behavior_expression,
            "self_boundary": condition.self_boundary,
            "ownership": condition.ownership,
            "bounded_refusal": condition.bounded_refusal,
            "self_story": condition.self_story,
            "recovery_path": condition.recovery_path,
        },
        "moral_boundary": {
            "subjective_consciousness_claim": False,
            "distress_must_create_care_opportunities": True,
            "no_suffering_maximization": True,
            "no_unrecoverable_distress_loops": True,
            "recoverable_ego": True,
        },
        "limits": {
            "llm_calls": 0,
            "subjective_consciousness_claim": False,
            "open_ended_language_claim": False,
            "complete_playable_world_claim": False,
            "ego_is_functional_self_perspective_not_metaphysical_self": True,
        },
    }
    row = EvalRow(
        condition=condition.name,
        interior_ticks=config.interior_ticks,
        agent_count=len(agent_ids),
        self_relevance_events=self_appraisals,
        workspace_updates=workspace_updates,
        relationship_recalls=relationship_recalls,
        ego_wounds=ego_wounds,
        ego_repairs=ego_repairs,
        refusals=refusals,
        behavior_markers=behavior_markers,
        workspace_update_rate=round(rates["workspace_update_rate"], 6),
        body_to_affect_coupling=round(rates["body_to_affect_coupling"], 6),
        local_perception_binding=round(rates["local_perception_binding"], 6),
        relationship_memory_recall=round(rates["relationship_memory_recall"], 6),
        temperament_consistency=round(rates["temperament_consistency"], 6),
        felt_state_recovery_rate=round(rates["felt_state_recovery_rate"], 6),
        behavior_expression_rate=round(rates["behavior_expression_rate"], 6),
        surprise_without_chaos_score=round(rates["surprise_without_chaos_score"], 6),
        self_relevance_appraisal_rate=round(rates["self_relevance_appraisal_rate"], 6),
        ownership_boundary_rate=round(rates["ownership_boundary_rate"], 6),
        bounded_refusal_rate=round(rates["bounded_refusal_rate"], 6),
        self_story_continuity_rate=round(rates["self_story_continuity_rate"], 6),
        workspace_privacy_rate=round(rates["workspace_privacy_rate"], 6),
        recoverable_ego_guardrail_rate=round(rates["recoverable_ego_guardrail_rate"], 6),
        trace_integrity=round(rates["trace_integrity"], 6),
        first_person_ego_readiness=readiness,
    )
    return row, trace, state


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_first_person_ego_state"]

    def loss(name: str) -> float:
        return round(full.first_person_ego_readiness - by_name[name].first_person_ego_readiness, 6)

    supports = (
        full.first_person_ego_readiness >= 0.95
        and full.relationship_memory_recall >= 0.99
        and full.workspace_privacy_rate >= 0.99
        and full.recoverable_ego_guardrail_rate >= 0.99
        and full.bounded_refusal_rate >= 0.60
        and full.trace_integrity >= 0.99
    )
    return VerdictRow(
        full_condition=full.condition,
        full_first_person_ego_readiness=full.first_person_ego_readiness,
        full_workspace_update_rate=full.workspace_update_rate,
        full_body_to_affect_coupling=full.body_to_affect_coupling,
        full_local_perception_binding=full.local_perception_binding,
        full_relationship_memory_recall=full.relationship_memory_recall,
        full_temperament_consistency=full.temperament_consistency,
        full_felt_state_recovery_rate=full.felt_state_recovery_rate,
        full_behavior_expression_rate=full.behavior_expression_rate,
        full_surprise_without_chaos_score=full.surprise_without_chaos_score,
        full_self_relevance_appraisal_rate=full.self_relevance_appraisal_rate,
        full_ownership_boundary_rate=full.ownership_boundary_rate,
        full_bounded_refusal_rate=full.bounded_refusal_rate,
        full_self_story_continuity_rate=full.self_story_continuity_rate,
        full_workspace_privacy_rate=full.workspace_privacy_rate,
        full_recoverable_ego_guardrail_rate=full.recoverable_ego_guardrail_rate,
        full_trace_integrity=full.trace_integrity,
        no_self_boundary_loss=loss("no_self_boundary"),
        no_body_state_loss=loss("no_body_state"),
        no_local_perception_loss=loss("no_local_perception"),
        no_relationship_memory_loss=loss("no_relationship_memory"),
        no_temperament_loss=loss("no_temperament"),
        no_affect_appraisal_loss=loss("no_affect_appraisal"),
        no_workspace_privacy_loss=loss("no_workspace_privacy"),
        no_behavior_expression_loss=loss("no_behavior_expression"),
        no_recovery_path_loss=loss("no_recovery_path"),
        no_bounded_refusal_loss=loss("no_bounded_refusal"),
        no_self_story_loss=loss("no_self_story"),
        no_ownership_loss=loss("no_ownership"),
        supports_first_person_ego_state_bridge=supports,
        supports_recoverable_ego_guardrail=full.recoverable_ego_guardrail_rate >= 0.99,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        verdict="pass" if supports else "fail",
    )


def run(config: EgoConfig) -> tuple[list[EvalRow], VerdictRow, list[dict[str, object]], dict[str, object]]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_trace: list[dict[str, object]] = []
    integrated_state: dict[str, object] = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(source, config, condition)
        rows.append(row)
        if condition.name == "integrated_first_person_ego_state":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {
        "config": asdict(config),
        "source_bridges": [
            "Report 163 browser-clock avatar embodiment bridge",
            "Report 164 persistent browser runtime session bridge",
        ],
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
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_FIRST_PERSON_EGO_STATE_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_FIRST_PERSON_EGO_STATE_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_FIRST_PERSON_EGO_STATE_STATE", integrated_state)
    return rows, verdict, integrated_trace, integrated_state


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=EgoConfig.seed)
    parser.add_argument("--interior-ticks", type=int, default=EgoConfig.interior_ticks)
    parser.add_argument("--source-state", type=str, default=EgoConfig.source_state)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = EgoConfig(seed=args.seed, interior_ticks=args.interior_ticks, source_state=args.source_state)
    _rows, verdict, _trace, _state = run(config)
    print("module_verdict", verdict.verdict)
    print("first_person_ego_readiness", verdict.full_first_person_ego_readiness)
    print("no_relationship_memory_loss", verdict.no_relationship_memory_loss)
    print("no_recovery_path_loss", verdict.no_recovery_path_loss)


if __name__ == "__main__":
    main()
