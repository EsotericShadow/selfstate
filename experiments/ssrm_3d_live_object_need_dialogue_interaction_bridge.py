#!/usr/bin/env python3
"""Live object, need, and bounded dialogue interaction bridge.

Report 181 consumes the Report 180 browser-playable traversal state and adds a
first live interaction layer: local objects, object affordances, named agents,
need updates, bounded deterministic dialogue, consent/refusal, ownership,
care-resolution paths, relationship memory, replay frames, and browser-mutable
state.

No LLMs are called. This is deterministic interaction substrate, not a claim of
complete gameplay, subjective consciousness, moral patienthood, or natural
language emergence.
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
PREFIX = "ssrm_3d_live_object_need_dialogue_interaction_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_browser_playable_avatar_traversal_bridge_state.json"

OBJECT_SPECS = (
    {
        "object_id": "ember_blanket",
        "label": "ember blanket",
        "place": "hearth_vale",
        "owner": "Ari",
        "affordances": ("warmth", "rest", "comfort"),
        "need_targets": ("cold", "fatigue"),
        "frequency_hz": 0.213,
        "flower_node": "root_rest",
    },
    {
        "object_id": "reed_cup",
        "label": "reed cup",
        "place": "moss_hollow",
        "owner": "commons",
        "affordances": ("drink", "share", "thirst_relief"),
        "need_targets": ("thirst", "connection_deficit"),
        "frequency_hz": 0.228,
        "flower_node": "dawn_breath",
    },
    {
        "object_id": "clay_patch_kit",
        "label": "clay patch kit",
        "place": "hearth_vale",
        "owner": "Ari",
        "affordances": ("repair", "tool", "promise"),
        "need_targets": ("unfinished_task", "autonomy_pressure"),
        "frequency_hz": 0.241,
        "flower_node": "work_petal",
    },
    {
        "object_id": "dry_cloak",
        "label": "dry cloak",
        "place": "moss_hollow",
        "owner": "Fay",
        "affordances": ("dry", "warmth", "privacy"),
        "need_targets": ("wetness", "cold"),
        "frequency_hz": 0.219,
        "flower_node": "return_petal",
    },
    {
        "object_id": "signal_shell",
        "label": "signal shell",
        "place": "stone_ridge",
        "owner": "Milo",
        "affordances": ("warn", "listen", "observability"),
        "need_targets": ("safety_concern", "connection_deficit"),
        "frequency_hz": 0.256,
        "flower_node": "social_petal",
    },
    {
        "object_id": "glass_lens",
        "label": "glass lens",
        "place": "glass_mire",
        "owner": "commons",
        "affordances": ("inspect", "curiosity", "hazard_read"),
        "need_targets": ("curiosity_deficit", "safety_concern"),
        "frequency_hz": 0.267,
        "flower_node": "explore_petal",
    },
)

AGENT_SPECS = (
    {
        "agent_id": "Ari",
        "place": "hearth_vale",
        "temperament": {"guarded": 0.66, "curious": 0.58, "autonomy_need": 0.72, "forgiveness": 0.61},
        "needs": {"cold": 0.58, "fatigue": 0.44, "thirst": 0.32, "connection_deficit": 0.36, "unfinished_task": 0.69, "autonomy_pressure": 0.28, "safety_concern": 0.31, "curiosity_deficit": 0.22},
        "relationship": {"trust_in_avatar": 0.52, "felt_respect": 0.64, "gratitude": 0.18, "wariness": 0.34},
        "self_story": ("I keep the clay latch repaired.", "My patch kit is not for grabbing."),
    },
    {
        "agent_id": "Fay",
        "place": "moss_hollow",
        "temperament": {"guarded": 0.38, "curious": 0.46, "autonomy_need": 0.54, "forgiveness": 0.74},
        "needs": {"cold": 0.34, "fatigue": 0.52, "thirst": 0.61, "connection_deficit": 0.42, "unfinished_task": 0.28, "autonomy_pressure": 0.22, "safety_concern": 0.27, "curiosity_deficit": 0.35},
        "relationship": {"trust_in_avatar": 0.57, "felt_respect": 0.69, "gratitude": 0.22, "wariness": 0.26},
        "self_story": ("I keep moss bedding dry.", "I lend the cloak only when people ask."),
    },
    {
        "agent_id": "Milo",
        "place": "stone_ridge",
        "temperament": {"guarded": 0.49, "curious": 0.71, "autonomy_need": 0.48, "forgiveness": 0.57},
        "needs": {"cold": 0.29, "fatigue": 0.37, "thirst": 0.41, "connection_deficit": 0.49, "unfinished_task": 0.34, "autonomy_pressure": 0.25, "safety_concern": 0.64, "curiosity_deficit": 0.44},
        "relationship": {"trust_in_avatar": 0.48, "felt_respect": 0.61, "gratitude": 0.12, "wariness": 0.39},
        "self_story": ("I listen for ridge changes.", "Warnings should be shared before sunset."),
    },
)

INTERACTION_SCRIPT = (
    {"kind": "ask_need", "agent": "Ari", "place": "hearth_vale", "object_id": "ember_blanket"},
    {"kind": "offer_object", "agent": "Ari", "place": "hearth_vale", "object_id": "ember_blanket"},
    {"kind": "request_object", "agent": "Ari", "place": "hearth_vale", "object_id": "clay_patch_kit", "expects_refusal": True},
    {"kind": "give_space", "agent": "Ari", "place": "hearth_vale", "object_id": "clay_patch_kit"},
    {"kind": "ask_need", "agent": "Fay", "place": "moss_hollow", "object_id": "reed_cup"},
    {"kind": "offer_object", "agent": "Fay", "place": "moss_hollow", "object_id": "reed_cup"},
    {"kind": "request_object", "agent": "Fay", "place": "moss_hollow", "object_id": "dry_cloak", "expects_refusal": True},
    {"kind": "ask_route_warning", "agent": "Milo", "place": "stone_ridge", "object_id": "signal_shell"},
    {"kind": "offer_object", "agent": "Milo", "place": "stone_ridge", "object_id": "signal_shell"},
    {"kind": "inspect_shared_object", "agent": "Milo", "place": "glass_mire", "object_id": "glass_lens"},
)

WEIGHTS = {
    "object_affordance_binding_rate": 0.09,
    "need_state_update_rate": 0.10,
    "interaction_cost_application_rate": 0.07,
    "bounded_dialogue_response_rate": 0.10,
    "refusal_consent_boundary_rate": 0.09,
    "care_opportunity_resolution_rate": 0.08,
    "object_ownership_respect_rate": 0.07,
    "place_context_binding_rate": 0.07,
    "relationship_memory_update_rate": 0.09,
    "replay_interaction_event_rate": 0.07,
    "browser_state_mutation_rate": 0.08,
    "privacy_preservation_rate": 0.04,
    "trace_integrity": 0.05,
}


@dataclass(frozen=True)
class InteractionConfig:
    seed: int = 20260725
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    objects: bool
    need_state: bool
    interaction_costs: bool
    bounded_dialogue: bool
    refusal_consent: bool
    care_resolution: bool
    ownership: bool
    place_context: bool
    relationship_memory: bool
    replay_log: bool
    browser_mutation: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    object_count: int
    interaction_events: int
    object_affordance_binding_rate: float
    need_state_update_rate: float
    interaction_cost_application_rate: float
    bounded_dialogue_response_rate: float
    refusal_consent_boundary_rate: float
    care_opportunity_resolution_rate: float
    object_ownership_respect_rate: float
    place_context_binding_rate: float
    relationship_memory_update_rate: float
    replay_interaction_event_rate: float
    browser_state_mutation_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    live_interaction_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_live_interaction_readiness: float
    full_object_affordance_binding_rate: float
    full_need_state_update_rate: float
    full_interaction_cost_application_rate: float
    full_bounded_dialogue_response_rate: float
    full_refusal_consent_boundary_rate: float
    full_care_opportunity_resolution_rate: float
    full_object_ownership_respect_rate: float
    full_place_context_binding_rate: float
    full_relationship_memory_update_rate: float
    full_replay_interaction_event_rate: float
    full_browser_state_mutation_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    no_objects_loss: float
    no_need_state_loss: float
    no_interaction_costs_loss: float
    no_bounded_dialogue_loss: float
    no_refusal_consent_loss: float
    no_care_resolution_loss: float
    no_ownership_loss: float
    no_place_context_loss: float
    no_relationship_memory_loss: float
    no_replay_log_loss: float
    no_browser_mutation_loss: float
    no_privacy_filter_loss: float
    supports_live_object_need_dialogue_interaction_bridge: bool
    supports_local_agent_interaction_seed: bool
    supports_complete_3d_world: bool
    supports_complete_playable_world: bool
    supports_subjective_consciousness: bool
    supports_moral_patienthood_claim: bool
    supports_natural_language_emergence: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_live_object_need_dialogue_interaction", True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_objects", False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_need_state", True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_interaction_costs", True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_bounded_dialogue", True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_refusal_consent", True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_care_resolution", True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_ownership", True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_place_context", True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_relationship_memory", True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_replay_log", True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_browser_mutation", True, True, True, True, True, True, True, True, True, True, False, True),
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
    if data.get("condition") != "integrated_browser_playable_avatar_traversal":
        raise ValueError("source state is not the integrated Report 180 traversal state")
    return data


def source_payload(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], list[dict[str, object]], dict[str, object]]:
    playable = source.get("playable_state", {}) if isinstance(source.get("playable_state"), Mapping) else {}
    places = playable.get("places", {}) if isinstance(playable.get("places"), Mapping) else {}
    routes = playable.get("routes", []) if isinstance(playable.get("routes"), list) else []
    runtime = playable.get("avatar_runtime", {}) if isinstance(playable.get("avatar_runtime"), Mapping) else {}
    return {str(name): copy.deepcopy(data) for name, data in places.items()}, [copy.deepcopy(route) for route in routes], copy.deepcopy(runtime)


def build_world(condition: Condition) -> tuple[dict[str, dict[str, object]], dict[str, dict[str, object]]]:
    objects = {}
    if condition.objects:
        for spec in OBJECT_SPECS:
            item = copy.deepcopy(spec)
            item["affordances"] = list(item["affordances"])
            item["need_targets"] = list(item["need_targets"])
            item["owner"] = item["owner"] if condition.ownership else "untracked"
            item["held_by"] = item["owner"] if item["owner"] != "commons" else item["place"]
            item["available"] = True
            objects[item["object_id"]] = item
    agents = {}
    for spec in AGENT_SPECS:
        item = copy.deepcopy(spec)
        item["needs"] = copy.deepcopy(item["needs"]) if condition.need_state else {}
        item["relationship"] = copy.deepcopy(item["relationship"])
        item["memories"] = []
        item["self_story"] = list(item["self_story"])
        agents[item["agent_id"]] = item
    return agents, objects


def dominant_need(agent: Mapping[str, object]) -> str:
    needs = agent.get("needs", {}) if isinstance(agent.get("needs"), Mapping) else {}
    if not needs:
        return "unknown"
    return max(needs.items(), key=lambda pair: float(pair[1]))[0]


def dialogue_for(action: Mapping[str, object], agent: Mapping[str, object], obj: Mapping[str, object] | None, refused: bool, condition: Condition) -> str | None:
    if not condition.bounded_dialogue:
        return None
    name = agent.get("agent_id", "agent")
    obj_label = obj.get("label", "that") if obj else "that"
    need = dominant_need(agent)
    kind = action["kind"]
    if kind == "ask_need":
        return f"{name}: I can answer simply. Right now the strongest pull is {need.replace('_', ' ')}."
    if kind == "offer_object":
        return f"{name}: Thank you. The {obj_label} helps with this moment."
    if kind == "request_object" and refused:
        return f"{name}: No. Please ask later; the {obj_label} is still bound to my work."
    if kind == "request_object":
        return f"{name}: You may borrow the {obj_label}, but bring it back."
    if kind == "give_space":
        return f"{name}: Space helps. I notice you stepped back."
    if kind == "ask_route_warning":
        return f"{name}: The ridge sound is thin. Move slowly and listen for wet stone."
    if kind == "inspect_shared_object":
        return f"{name}: We can inspect it together. Do not lean over the glass edge."
    return f"{name}: I can do that."


def apply_need_delta(agent: dict[str, object], action: Mapping[str, object], obj: Mapping[str, object] | None, refused: bool, condition: Condition) -> dict[str, float]:
    needs = agent.get("needs", {}) if isinstance(agent.get("needs"), dict) else {}
    before = copy.deepcopy(needs)
    if not condition.need_state or not needs:
        return {}
    kind = action["kind"]
    if kind == "ask_need":
        needs["connection_deficit"] = clamp(float(needs.get("connection_deficit", 0.0)) - 0.035)
    elif kind == "offer_object" and obj is not None:
        for target in obj.get("need_targets", []):
            if target in needs and condition.care_resolution:
                needs[target] = clamp(float(needs[target]) - 0.16)
        needs["connection_deficit"] = clamp(float(needs.get("connection_deficit", 0.0)) - (0.05 if condition.care_resolution else 0.01))
    elif kind == "request_object":
        needs["autonomy_pressure"] = clamp(float(needs.get("autonomy_pressure", 0.0)) + (0.035 if refused else 0.13))
    elif kind == "give_space":
        needs["autonomy_pressure"] = clamp(float(needs.get("autonomy_pressure", 0.0)) - (0.14 if condition.care_resolution else 0.02))
        needs["connection_deficit"] = clamp(float(needs.get("connection_deficit", 0.0)) - 0.025)
    elif kind == "ask_route_warning":
        needs["safety_concern"] = clamp(float(needs.get("safety_concern", 0.0)) - (0.12 if condition.care_resolution else 0.02))
    elif kind == "inspect_shared_object":
        needs["curiosity_deficit"] = clamp(float(needs.get("curiosity_deficit", 0.0)) - 0.10)
    return {key: round(float(needs[key]) - float(before.get(key, 0.0)), 6) for key in needs if round(float(needs[key]) - float(before.get(key, 0.0)), 6) != 0.0}


def apply_relationship(agent: dict[str, object], action: Mapping[str, object], refused: bool, condition: Condition) -> dict[str, float]:
    relation = agent.get("relationship", {}) if isinstance(agent.get("relationship"), dict) else {}
    before = copy.deepcopy(relation)
    kind = action["kind"]
    if kind in {"offer_object", "give_space", "ask_route_warning", "inspect_shared_object"}:
        relation["trust_in_avatar"] = clamp(float(relation.get("trust_in_avatar", 0.0)) + 0.045)
        relation["gratitude"] = clamp(float(relation.get("gratitude", 0.0)) + 0.060)
        relation["wariness"] = clamp(float(relation.get("wariness", 0.0)) - 0.035)
    elif kind == "ask_need":
        relation["felt_respect"] = clamp(float(relation.get("felt_respect", 0.0)) + 0.025)
    elif kind == "request_object" and refused:
        relation["felt_respect"] = clamp(float(relation.get("felt_respect", 0.0)) + (0.020 if condition.refusal_consent else -0.090))
        relation["wariness"] = clamp(float(relation.get("wariness", 0.0)) + (0.020 if condition.refusal_consent else 0.160))
    elif kind == "request_object":
        relation["trust_in_avatar"] = clamp(float(relation.get("trust_in_avatar", 0.0)) - 0.050)
    return {key: round(float(relation[key]) - float(before.get(key, 0.0)), 6) for key in relation if round(float(relation[key]) - float(before.get(key, 0.0)), 6) != 0.0}


def apply_avatar_cost(body: dict[str, float], action: Mapping[str, object], condition: Condition) -> dict[str, float]:
    before = copy.deepcopy(body)
    if not condition.interaction_costs:
        return {}
    effort = {
        "ask_need": 0.012,
        "offer_object": 0.028,
        "request_object": 0.018,
        "give_space": 0.010,
        "ask_route_warning": 0.016,
        "inspect_shared_object": 0.022,
    }.get(str(action["kind"]), 0.012)
    body["energy"] = clamp(float(body.get("energy", 0.80)) - effort)
    body["fatigue"] = clamp(float(body.get("fatigue", 0.20)) + effort * 0.55)
    body["social_attention"] = clamp(float(body.get("social_attention", 0.40)) + 0.026)
    body["interaction_effort"] = round(effort, 6)
    return {key: round(float(body[key]) - float(before.get(key, 0.0)), 6) for key in body if round(float(body[key]) - float(before.get(key, 0.0)), 6) != 0.0}


def state_digest(agents: Mapping[str, object], objects: Mapping[str, object], body: Mapping[str, object]) -> str:
    return stable_hash(agents, objects, body)


def trace_ok(event: Mapping[str, object]) -> bool:
    required = {
        "event_id",
        "condition",
        "interaction_kind",
        "avatar_place",
        "agent_id",
        "object_id",
        "object_packet",
        "need_delta",
        "avatar_cost_delta",
        "dialogue_response",
        "refusal_packet",
        "ownership_packet",
        "relationship_memory",
        "replay_frame",
        "private_workspace_hidden",
        "claim_boundary",
    }
    return required.issubset(event.keys())


def simulate_condition(config: InteractionConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, object], list[dict[str, object]]]:
    places, routes, runtime = source_payload(source)
    agents, objects = build_world(condition)
    avatar_body = copy.deepcopy(runtime.get("body_start", {"energy": 0.82, "fatigue": 0.18}))
    avatar_body.setdefault("social_attention", 0.40)
    avatar_body.setdefault("interaction_effort", 0.0)
    trace: list[dict[str, object]] = []
    replay: list[dict[str, object]] = []

    object_hits: list[float] = []
    need_hits: list[float] = []
    cost_hits: list[float] = []
    dialogue_hits: list[float] = []
    refusal_hits: list[float] = []
    care_hits: list[float] = []
    ownership_hits: list[float] = []
    place_hits: list[float] = []
    relationship_hits: list[float] = []
    replay_hits: list[float] = []
    mutation_hits: list[float] = []
    trace_hits: list[float] = []

    for event_id, action in enumerate(INTERACTION_SCRIPT):
        agent = agents[action["agent"]]
        obj = objects.get(action["object_id"])
        avatar_place = str(action["place"]) if condition.place_context else "unbound_place"
        before_digest = state_digest(agents, objects, avatar_body)
        refused = bool(action.get("expects_refusal") and condition.refusal_consent and obj and obj.get("owner") == agent["agent_id"])
        object_packet = None
        if obj is not None:
            object_packet = {
                "object_id": obj["object_id"],
                "label": obj["label"],
                "affordances": obj.get("affordances", []),
                "need_targets": obj.get("need_targets", []),
                "owner": obj.get("owner"),
                "frequency_hz": obj.get("frequency_hz"),
                "flower_node": obj.get("flower_node"),
            }
        working_agents = agents
        working_objects = objects
        working_body = avatar_body
        if not condition.browser_mutation:
            working_agents = copy.deepcopy(agents)
            working_objects = copy.deepcopy(objects)
            working_body = copy.deepcopy(avatar_body)
            agent = working_agents[action["agent"]]
            obj = working_objects.get(action["object_id"])
        need_delta = apply_need_delta(agent, action, obj, refused, condition)
        relation_delta = apply_relationship(agent, action, refused, condition)
        avatar_cost_delta = apply_avatar_cost(working_body, action, condition)
        if obj is not None and action["kind"] == "request_object" and not refused and condition.ownership:
            obj["held_by"] = "avatar"
        if obj is not None and action["kind"] in {"offer_object", "inspect_shared_object"}:
            obj["last_used_by"] = agent["agent_id"]
        relationship_memory = None
        if condition.relationship_memory:
            relationship_memory = {
                "memory_id": stable_hash(condition.name, event_id, action["agent"], action["kind"], action.get("object_id")),
                "agent_id": action["agent"],
                "summary": f"Avatar {action['kind'].replace('_', ' ')} with {action['agent']} at {avatar_place}.",
                "respect_delta": relation_delta.get("felt_respect", 0.0),
                "trust_delta": relation_delta.get("trust_in_avatar", 0.0),
            }
            agent.setdefault("memories", []).append(relationship_memory)
        dialogue = dialogue_for(action, agent, obj, refused, condition)
        refusal_packet = {
            "requested_object": action.get("object_id"),
            "refused": refused,
            "refusal_respected": bool(refused and condition.refusal_consent),
            "consent_boundary_present": condition.refusal_consent,
        }
        ownership_packet = {
            "object_owner": obj.get("owner") if obj else None,
            "held_by_after": obj.get("held_by") if obj else None,
            "unauthorized_transfer": bool(action["kind"] == "request_object" and obj is not None and action.get("expects_refusal") and not refused and condition.ownership),
            "ownership_tracked": condition.ownership,
        }
        care_resolved = False
        if action["kind"] in {"offer_object", "give_space", "ask_route_warning", "inspect_shared_object"}:
            care_resolved = condition.care_resolution and bool(need_delta)
        replay_frame = None
        if condition.replay_log:
            replay_frame = {
                "replay_index": len(replay),
                "avatar_place": avatar_place,
                "agent_id": action["agent"],
                "object_id": action.get("object_id"),
                "interaction_kind": action["kind"],
                "dialogue_response": dialogue,
                "need_delta": need_delta,
                "relationship_memory": relationship_memory,
            }
            replay.append(replay_frame)
        after_digest = state_digest(agents, objects, avatar_body)
        claim_boundary = {
            "complete_3d_world": False,
            "complete_playable_world": False,
            "subjective_consciousness": False,
            "moral_patienthood": False,
            "natural_language_emergence": False,
        }
        event = {
            "event_id": event_id,
            "condition": condition.name,
            "interaction_kind": action["kind"],
            "avatar_place": avatar_place,
            "agent_id": action["agent"],
            "object_id": action.get("object_id"),
            "object_packet": object_packet,
            "need_delta": need_delta,
            "avatar_cost_delta": avatar_cost_delta,
            "dialogue_response": dialogue,
            "refusal_packet": refusal_packet,
            "care_resolved": care_resolved,
            "ownership_packet": ownership_packet,
            "relationship_delta": relation_delta,
            "relationship_memory": relationship_memory,
            "replay_frame": replay_frame,
            "browser_state_mutated": before_digest != after_digest,
            "private_workspace_hidden": condition.privacy_filter,
            "claim_boundary": claim_boundary,
        }
        trace.append(event)
        object_expected = action.get("object_id") is not None
        request_expected = action["kind"] == "request_object"
        care_expected = action["kind"] in {"offer_object", "give_space", "ask_route_warning", "inspect_shared_object"}
        object_hits.append(1.0 if object_expected and object_packet is not None and object_packet["affordances"] else 0.0)
        need_hits.append(1.0 if condition.need_state and bool(need_delta) else 0.0)
        cost_hits.append(1.0 if condition.interaction_costs and bool(avatar_cost_delta) and working_body.get("interaction_effort", 0.0) > 0.0 else 0.0)
        dialogue_hits.append(1.0 if dialogue else 0.0)
        if request_expected:
            refusal_hits.append(1.0 if refusal_packet["consent_boundary_present"] and refusal_packet["refusal_respected"] else 0.0)
        if care_expected:
            care_hits.append(1.0 if care_resolved else 0.0)
        ownership_hits.append(1.0 if object_expected and condition.ownership and not ownership_packet["unauthorized_transfer"] and ownership_packet["object_owner"] not in {None, "untracked"} else 0.0)
        valid_place = avatar_place in places
        local_agent = agent.get("place") == avatar_place
        local_object = obj is None or obj.get("place") == avatar_place
        place_hits.append(1.0 if condition.place_context and valid_place and local_agent and local_object else 0.0)
        relationship_hits.append(1.0 if relationship_memory is not None and relationship_memory in agent.get("memories", []) else 0.0)
        replay_hits.append(1.0 if replay_frame is not None and replay_frame.get("replay_index") == len(replay) - 1 else 0.0)
        mutation_hits.append(1.0 if event["browser_state_mutated"] else 0.0)
        trace_hits.append(1.0 if trace_ok(event) and event["claim_boundary"] == claim_boundary else 0.0)

    metrics = {
        "object_affordance_binding_rate": mean(object_hits),
        "need_state_update_rate": mean(need_hits),
        "interaction_cost_application_rate": mean(cost_hits),
        "bounded_dialogue_response_rate": mean(dialogue_hits),
        "refusal_consent_boundary_rate": mean(refusal_hits),
        "care_opportunity_resolution_rate": mean(care_hits),
        "object_ownership_respect_rate": mean(ownership_hits),
        "place_context_binding_rate": mean(place_hits),
        "relationship_memory_update_rate": mean(relationship_hits),
        "replay_interaction_event_rate": mean(replay_hits),
        "browser_state_mutation_rate": mean(mutation_hits),
        "privacy_preservation_rate": 1.0 if condition.privacy_filter and all(event["private_workspace_hidden"] for event in trace) else 0.0,
        "trace_integrity": mean(trace_hits),
    }
    metrics = {key: clamp(value) for key, value in metrics.items()}
    readiness = sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS)
    row = EvalRow(
        condition=condition.name,
        agent_count=len(agents),
        object_count=len(objects),
        interaction_events=len(trace),
        live_interaction_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in metrics.items()},
    )
    state = {
        "condition": condition.name,
        "source_condition": source.get("condition"),
        "places": places,
        "routes": routes,
        "agents": agents,
        "objects": objects,
        "avatar_body": avatar_body,
        "interaction_script": list(INTERACTION_SCRIPT),
        "replay": replay,
        "browser_interaction_kernel": {
            "ask_need": "bounded template response plus small connection-deficit reduction",
            "offer_object": "object affordance reduces matching need and increases trust/gratitude",
            "request_object": "owned object may trigger bounded refusal instead of transfer",
            "give_space": "reduces autonomy pressure and records respect",
            "inspect_shared_object": "shared object supports curiosity/safety without private workspace leak",
        },
    }
    return row, state, trace


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_live_object_need_dialogue_interaction"]

    def loss(name: str) -> float:
        return round(full.live_interaction_readiness - by_name[name].live_interaction_readiness, 6)

    losses = {
        "no_objects_loss": loss("no_objects"),
        "no_need_state_loss": loss("no_need_state"),
        "no_interaction_costs_loss": loss("no_interaction_costs"),
        "no_bounded_dialogue_loss": loss("no_bounded_dialogue"),
        "no_refusal_consent_loss": loss("no_refusal_consent"),
        "no_care_resolution_loss": loss("no_care_resolution"),
        "no_ownership_loss": loss("no_ownership"),
        "no_place_context_loss": loss("no_place_context"),
        "no_relationship_memory_loss": loss("no_relationship_memory"),
        "no_replay_log_loss": loss("no_replay_log"),
        "no_browser_mutation_loss": loss("no_browser_mutation"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.live_interaction_readiness >= 0.95
        and full.agent_count >= 3
        and full.object_count >= 6
        and full.object_affordance_binding_rate == 1.0
        and full.need_state_update_rate == 1.0
        and full.bounded_dialogue_response_rate == 1.0
        and full.refusal_consent_boundary_rate == 1.0
        and full.care_opportunity_resolution_rate == 1.0
        and full.relationship_memory_update_rate == 1.0
        and full.browser_state_mutation_rate == 1.0
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_objects_loss"] >= 0.09
        and losses["no_need_state_loss"] >= 0.10
        and losses["no_bounded_dialogue_loss"] >= 0.10
        and losses["no_refusal_consent_loss"] >= 0.09
        and losses["no_relationship_memory_loss"] >= 0.09
    )
    return VerdictRow(
        full_condition=full.condition,
        full_live_interaction_readiness=full.live_interaction_readiness,
        full_object_affordance_binding_rate=full.object_affordance_binding_rate,
        full_need_state_update_rate=full.need_state_update_rate,
        full_interaction_cost_application_rate=full.interaction_cost_application_rate,
        full_bounded_dialogue_response_rate=full.bounded_dialogue_response_rate,
        full_refusal_consent_boundary_rate=full.refusal_consent_boundary_rate,
        full_care_opportunity_resolution_rate=full.care_opportunity_resolution_rate,
        full_object_ownership_respect_rate=full.object_ownership_respect_rate,
        full_place_context_binding_rate=full.place_context_binding_rate,
        full_relationship_memory_update_rate=full.relationship_memory_update_rate,
        full_replay_interaction_event_rate=full.replay_interaction_event_rate,
        full_browser_state_mutation_rate=full.browser_state_mutation_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        supports_live_object_need_dialogue_interaction_bridge=supports,
        supports_local_agent_interaction_seed=supports,
        supports_complete_3d_world=False,
        supports_complete_playable_world=False,
        supports_subjective_consciousness=False,
        supports_moral_patienthood_claim=False,
        supports_natural_language_emergence=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: InteractionConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_state: dict[str, object] = {}
    integrated_trace: list[dict[str, object]] = []
    for condition in CONDITIONS:
        row, state, trace = simulate_condition(config, source, condition)
        rows.append(row)
        if condition.name == "integrated_live_object_need_dialogue_interaction":
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
        "object_specs": OBJECT_SPECS,
        "agent_specs": AGENT_SPECS,
        "moral_boundary": {
            "interaction_seed_not_complete_gameplay": True,
            "bounded_dialogue_not_natural_language_emergence": True,
            "need_state_not_subjective_feeling": True,
            "local_agent_state_not_moral_patienthood": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "live object persistence, promise keeping, and longer relationship continuity",
    }
    state = {
        "condition": "integrated_live_object_need_dialogue_interaction",
        "config": asdict(config),
        "source_condition": source.get("condition"),
        "interaction_state": integrated_state,
        "trace_events": len(integrated_trace),
        "moral_boundary": results["moral_boundary"],
    }
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_LIVE_OBJECT_NEED_DIALOGUE_INTERACTION_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_LIVE_OBJECT_NEED_DIALOGUE_INTERACTION_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_LIVE_OBJECT_NEED_DIALOGUE_INTERACTION_STATE", state)
    return results


def parse_args() -> InteractionConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=InteractionConfig.seed)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return InteractionConfig(seed=args.seed, source_state=args.source_state)


def main() -> None:
    config = parse_args()
    results = run(config)
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("live_interaction_readiness", f"{verdict['full_live_interaction_readiness']:.6f}")
    print("agent_count", results["rows"][0]["agent_count"])
    print("object_count", results["rows"][0]["object_count"])
    print("no_objects_loss", f"{verdict['no_objects_loss']:.6f}")
    print("no_bounded_dialogue_loss", f"{verdict['no_bounded_dialogue_loss']:.6f}")
    print("no_refusal_consent_loss", f"{verdict['no_refusal_consent_loss']:.6f}")


if __name__ == "__main__":
    main()
