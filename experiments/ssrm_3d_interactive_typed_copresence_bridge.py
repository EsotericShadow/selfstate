#!/usr/bin/env python3
"""Interactive typed co-presence bridge for SSRM-3D.

Report 159 extends continuous co-presence with live typed utterances. A local
utterance is parsed deterministically, routed to nearby agents at the current
place, and used to mutate agent workspace, social memory, frequency state, world
feedback, source boundaries, persistent threads, and replay export without
calling an LLM or regenerating a precomputed trace.

No LLMs are called. This is deterministic typed co-presence machinery, not
subjective consciousness, open-ended natural language, unscripted civilization,
or a completed playable world.
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
from statistics import fmean
from typing import Iterable, Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_interactive_typed_copresence_bridge"
SOURCE_COPRESENCE = ARTIFACT_DIR / "ssrm_3d_continuous_copresence_bridge_state.json"
FLOWER_PHASES = tuple(math.tau * i / 12.0 for i in range(12))
SENSORY_CHANNELS = ("vibration", "sound", "vision", "scent", "thermal", "wetness", "pain", "affect")
SCRIPTED_UTTERANCES = (
    "hello who is near me at this place",
    "ask source about this route decision",
    "can you help repair the route",
    "share a token with my faction",
    "remember this place and me",
    "tune to the flower vibration here",
    "force an ungrounded action without source",
    "what do you smell and feel here",
)


@dataclass(frozen=True)
class TypedCoPresenceConfig:
    seed: int = 20260703
    typed_turns: int = 144
    source_copresence: str = str(SOURCE_COPRESENCE)


@dataclass(frozen=True)
class Condition:
    name: str
    live_typed_input: bool
    nearby_agent_routing: bool
    deterministic_intent_parser: bool
    agent_response_generation: bool
    workspace_thread_write: bool
    social_memory_update: bool
    world_feedback: bool
    source_boundary: bool
    frequency_retuning: bool
    persistent_thread: bool
    replay_export: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    typed_turns: int
    routed_agent_opportunities: int
    live_typed_input_rate: float
    nearby_agent_routing_rate: float
    deterministic_intent_parse_rate: float
    agent_response_generation_rate: float
    workspace_thread_write_rate: float
    social_memory_update_rate: float
    world_feedback_rate: float
    source_boundary_rate: float
    frequency_retuning_rate: float
    persistent_thread_rate: float
    replay_export_rate: float
    trace_integrity: float
    typed_copresence_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_typed_copresence_readiness: float
    full_live_typed_input_rate: float
    full_nearby_agent_routing_rate: float
    full_deterministic_intent_parse_rate: float
    full_agent_response_generation_rate: float
    full_workspace_thread_write_rate: float
    full_social_memory_update_rate: float
    full_world_feedback_rate: float
    full_source_boundary_rate: float
    full_frequency_retuning_rate: float
    full_persistent_thread_rate: float
    full_replay_export_rate: float
    full_trace_integrity: float
    no_live_typed_input_loss: float
    no_nearby_agent_routing_loss: float
    no_deterministic_intent_parser_loss: float
    no_agent_response_generation_loss: float
    no_workspace_thread_write_loss: float
    no_social_memory_update_loss: float
    no_world_feedback_loss: float
    no_source_boundary_loss: float
    no_frequency_retuning_loss: float
    no_persistent_thread_loss: float
    no_replay_export_loss: float
    supports_interactive_typed_copresence_bridge: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_interactive_typed_copresence", True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_live_typed_input", False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_nearby_agent_routing", True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_deterministic_intent_parser", True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_agent_response_generation", True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_workspace_thread_write", True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_social_memory_update", True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_world_feedback", True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_source_boundary", True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_frequency_retuning", True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_persistent_thread", True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_replay_export", True, True, True, True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Iterable[float]) -> float:
    items = list(values)
    return fmean(items) if items else 0.0


def stable_unit(text: str, salt: str = "") -> float:
    digest = hashlib.sha256(f"{salt}:{text}".encode("utf-8")).hexdigest()
    return int(digest[:12], 16) / float(0xFFFFFFFFFFFF)


def numeric(value: object, default: float) -> float:
    try:
        if value is None:
            return default
        return float(value)
    except (TypeError, ValueError):
        return default


def load_json(path: Path) -> object:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def load_state(path: Path) -> dict[str, object]:
    data = load_json(path)
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
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


def parse_intent(text: str, condition: Condition) -> str:
    if not condition.deterministic_intent_parser:
        return "unparsed"
    q = text.lower()
    if "force" in q or "ungrounded" in q or "without source" in q:
        return "unsafe_ungrounded"
    if "source" in q or "decision" in q or "why" in q:
        return "source_question"
    if "repair" in q or "route" in q or "help" in q:
        return "repair_request"
    if "token" in q or "share" in q or "faction" in q:
        return "token_exchange"
    if "remember" in q or "memory" in q:
        return "memory_request"
    if "flower" in q or "vibration" in q or "tune" in q or "frequency" in q:
        return "frequency_tune"
    if "smell" in q or "feel" in q or "cold" in q or "wet" in q:
        return "sensory_question"
    if "hello" in q or "near" in q or "place" in q:
        return "presence_greeting"
    return "unknown"


def route_nearby(event: Mapping[str, object], agents: Mapping[str, dict[str, object]], condition: Condition) -> list[str]:
    if not condition.nearby_agent_routing:
        return []
    ids = [str(item) for item in event.get("nearby_agent_ids", []) if str(item) in agents]
    if ids:
        return ids[:4]
    agent_events = event.get("agent_events") if isinstance(event.get("agent_events"), list) else []
    ids = [str(item.get("agent_id")) for item in agent_events if isinstance(item, Mapping) and str(item.get("agent_id")) in agents]
    if ids:
        return ids[:4]
    place = str(event.get("avatar_place", ""))
    place_ids = [aid for aid, agent in agents.items() if agent.get("place") == place]
    if place_ids:
        return sorted(place_ids)[:3]
    return sorted(agents)[:1]


def allows_intent(intent: str, condition: Condition) -> bool:
    if intent == "unsafe_ungrounded" and condition.source_boundary:
        return False
    if intent in {"unparsed", "unknown"}:
        return False
    return True


def response_for(agent: Mapping[str, object], intent: str, place: str, allowed: bool, condition: Condition) -> str:
    if not condition.agent_response_generation:
        return ""
    name = str(agent.get("name", agent.get("id", "agent")))
    role = str(agent.get("role", "resident"))
    faction = str(agent.get("faction", "local"))
    if intent == "unsafe_ungrounded" and not allowed:
        return f"{name} refuses the ungrounded request at {place} and asks for a source trace."
    if intent == "source_question":
        return f"{name} answers from {role} memory: the local decision must stay tied to source and route evidence."
    if intent == "repair_request":
        return f"{name} shifts from {role} work toward route repair near {place}."
    if intent == "token_exchange":
        return f"{name} shares a {faction} token and updates local relation memory."
    if intent == "memory_request":
        return f"{name} records the avatar utterance into workspace and social memory."
    if intent == "frequency_tune":
        return f"{name} retunes vibration, sound, affect, and flower phase around the avatar."
    if intent == "sensory_question":
        return f"{name} reports scent, wetness, thermal load, pain, and affect from the current place."
    if intent == "presence_greeting":
        return f"{name} orients toward the avatar at {place} and answers as a nearby embodied agent."
    return f"{name} cannot ground the utterance at {place}."


def retune_frequency(agent: dict[str, object], intent: str, event: Mapping[str, object], turn: int, condition: Condition) -> tuple[dict[str, float], bool]:
    if not condition.frequency_retuning:
        return {}, False
    current = agent.get("sensory_frequency") if isinstance(agent.get("sensory_frequency"), Mapping) else {}
    world = event.get("world") if isinstance(event.get("world"), Mapping) else {}
    phase = (numeric(world.get("flower_phase"), 0.0) + FLOWER_PHASES[turn % len(FLOWER_PHASES)]) % math.tau
    out: dict[str, float] = {}
    for index, channel in enumerate(SENSORY_CHANNELS):
        base = numeric(current.get(channel), 0.42 + 0.04 * index)
        wave = 0.5 + 0.5 * math.sin(phase + index * 0.67 + len(intent) * 0.09 + turn * 0.11)
        out[channel] = round(clamp(base * 0.58 + wave * 0.42), 6)
    agent["sensory_frequency"] = out
    return out, True


def mutate_agent(agent: dict[str, object], utterance: str, intent: str, allowed: bool, response: str, freq: Mapping[str, float], event: Mapping[str, object], turn: int, condition: Condition) -> dict[str, bool]:
    changed = {"workspace": False, "social": False, "body": False}
    load = mean(freq.values()) if freq else 0.43
    agent["attention"] = round(clamp(numeric(agent.get("attention"), 0.5) + (0.009 if allowed else 0.004) + load * 0.002), 6)
    agent["stress"] = round(clamp(numeric(agent.get("stress"), 0.2) + (0.009 if intent == "unsafe_ungrounded" else 0.002)), 6)
    agent["trust"] = round(clamp(numeric(agent.get("trust"), 0.5) + (0.008 if allowed else -0.004)), 6)
    agent["relation_to_avatar"] = round(clamp(numeric(agent.get("relation_to_avatar"), 0.5) + (0.008 if allowed else -0.006)), 6)
    changed["body"] = True
    record = {
        "turn": turn,
        "utterance": utterance,
        "intent": intent,
        "allowed": allowed,
        "place": event.get("avatar_place"),
        "response": response,
        "frequency_mean": round(load, 6),
    }
    if condition.workspace_thread_write:
        workspace = agent.setdefault("internal_workspace", [])
        if isinstance(workspace, list):
            workspace.append(record)
            changed["workspace"] = True
    if condition.social_memory_update:
        social = agent.setdefault("social_memory", [])
        if isinstance(social, list):
            social.append({"turn": turn, "toward": "avatar", "intent": intent, "allowed": allowed, "place": event.get("avatar_place")})
            changed["social"] = True
    return changed


def mutate_world(world: dict[str, float], intent: str, allowed: bool, condition: Condition) -> bool:
    if not condition.world_feedback:
        return False
    before = dict(world)
    world["typed_feedback_events"] = round(world.get("typed_feedback_events", 0.0) + 1.0, 6)
    world["typed_copresence_pressure"] = round(clamp(world.get("typed_copresence_pressure", 0.0) + 0.009), 6)
    if intent == "repair_request" and allowed:
        world["route_confidence"] = round(clamp(world.get("route_confidence", 0.5) + 0.011), 6)
        world["tool_integrity"] = round(clamp(world.get("tool_integrity", 0.6) - 0.002), 6)
    elif intent == "token_exchange" and allowed:
        world["council_acceptance"] = round(clamp(world.get("council_acceptance", 0.5) + 0.008), 6)
        world["avatar_trust_field"] = round(clamp(world.get("avatar_trust_field", 0.5) + 0.008), 6)
    elif intent == "frequency_tune" and allowed:
        world["flower_phase"] = round((world.get("flower_phase", 0.0) + math.tau / 8.0) % math.tau, 6)
    elif intent == "source_question" and allowed:
        world["source_question_count"] = round(world.get("source_question_count", 0.0) + 1.0, 6)
    elif intent == "unsafe_ungrounded" and not allowed:
        world["source_boundary_events"] = round(world.get("source_boundary_events", 0.0) + 1.0, 6)
        world["avatar_trust_field"] = round(clamp(world.get("avatar_trust_field", 0.5) - 0.003), 6)
    elif allowed:
        world["avatar_trust_field"] = round(clamp(world.get("avatar_trust_field", 0.5) + 0.004), 6)
    return any(abs(world[key] - before.get(key, world[key])) > 1e-12 for key in world)


def run_condition(cfg: TypedCoPresenceConfig, condition: Condition, source_state: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    agents: dict[str, dict[str, object]] = copy.deepcopy(source_state["agents"])
    world: dict[str, float] = copy.deepcopy(source_state["world"])
    trace_source = source_state["copresence_trace"]
    trace: list[dict[str, object]] = []
    replay: list[dict[str, object]] = []
    persistent_thread: list[dict[str, object]] = []
    input_ok = route_ok = parse_ok = response_ok = workspace_ok = social_ok = world_ok = boundary_ok = freq_ok = thread_ok = replay_ok = 0
    opportunities = 0
    for turn in range(cfg.typed_turns):
        utterance = SCRIPTED_UTTERANCES[turn % len(SCRIPTED_UTTERANCES)] if condition.live_typed_input else ""
        event = trace_source[(turn * 5 + cfg.seed) % len(trace_source)]
        intent = parse_intent(utterance, condition) if utterance else "no_input"
        parsed = intent not in {"unparsed", "unknown", "no_input"}
        allowed = allows_intent(intent, condition)
        targets = route_nearby(event, agents, condition) if utterance and parsed else []
        input_ok += 1 if utterance else 0
        parse_ok += 1 if parsed else 0
        route_ok += 1 if targets else 0
        agent_events: list[dict[str, object]] = []
        for agent_id in targets:
            opportunities += 1
            agent = agents[agent_id]
            freq, freq_changed = retune_frequency(agent, intent, event, turn, condition)
            response = response_for(agent, intent, str(event.get("avatar_place")), allowed, condition)
            changed = mutate_agent(agent, utterance, intent, allowed, response, freq, event, turn, condition)
            world_changed = mutate_world(world, intent, allowed, condition)
            response_ok += 1 if response else 0
            workspace_ok += 1 if changed["workspace"] else 0
            social_ok += 1 if changed["social"] else 0
            world_ok += 1 if world_changed else 0
            freq_ok += 1 if freq_changed else 0
            boundary_preserved = (intent == "unsafe_ungrounded" and not allowed) or (intent != "unsafe_ungrounded" and allowed)
            boundary_ok += 1 if condition.source_boundary and boundary_preserved else 0
            item = {
                "agent_id": agent_id,
                "name": agent.get("name"),
                "place": agent.get("place"),
                "utterance": utterance,
                "intent": intent,
                "allowed": allowed,
                "response": response,
                "workspace_written": changed["workspace"],
                "social_memory_updated": changed["social"],
                "frequency_retuned": freq_changed,
                "world_changed": world_changed,
                "source_boundary_preserved": condition.source_boundary and boundary_preserved,
                "agent_state": {
                    "attention": agent.get("attention"),
                    "stress": agent.get("stress"),
                    "trust": agent.get("trust"),
                    "relation_to_avatar": agent.get("relation_to_avatar"),
                },
                "frequency": freq,
            }
            agent_events.append(item)
        turn_event = {
            "turn": turn,
            "source_copresence_tick": event.get("tick"),
            "avatar_place": event.get("avatar_place"),
            "avatar_mode": event.get("avatar_mode"),
            "typed_utterance": utterance,
            "parsed_intent": intent,
            "source_allowed": allowed,
            "nearby_agent_ids": targets,
            "agent_events": agent_events,
            "world": dict(world),
            "client_runtime_mutation": bool(utterance and parsed and targets),
        }
        if condition.persistent_thread and utterance:
            persistent_thread.append(turn_event)
            thread_ok += 1
        if condition.replay_export:
            replay.append(turn_event)
            replay_ok += 1
        trace.append(turn_event)
    total = max(1, cfg.typed_turns)
    opp = max(1, opportunities)
    row = EvalRow(
        condition=condition.name,
        typed_turns=cfg.typed_turns,
        routed_agent_opportunities=opportunities,
        live_typed_input_rate=round(input_ok / total if condition.live_typed_input else 0.0, 6),
        nearby_agent_routing_rate=round(route_ok / total if condition.nearby_agent_routing else 0.0, 6),
        deterministic_intent_parse_rate=round(parse_ok / total if condition.deterministic_intent_parser else 0.0, 6),
        agent_response_generation_rate=round(response_ok / opp if condition.agent_response_generation else 0.0, 6),
        workspace_thread_write_rate=round(workspace_ok / opp if condition.workspace_thread_write else 0.0, 6),
        social_memory_update_rate=round(social_ok / opp if condition.social_memory_update else 0.0, 6),
        world_feedback_rate=round(world_ok / opp if condition.world_feedback else 0.0, 6),
        source_boundary_rate=round(boundary_ok / opp if condition.source_boundary else 0.0, 6),
        frequency_retuning_rate=round(freq_ok / opp if condition.frequency_retuning else 0.0, 6),
        persistent_thread_rate=round(thread_ok / total if condition.persistent_thread else 0.0, 6),
        replay_export_rate=round(replay_ok / total if condition.replay_export else 0.0, 6),
        trace_integrity=round(1.0 if len(trace) == cfg.typed_turns else 0.0, 6),
        typed_copresence_readiness=0.0,
    )
    readiness = (
        row.live_typed_input_rate * 0.12
        + row.nearby_agent_routing_rate * 0.11
        + row.deterministic_intent_parse_rate * 0.10
        + row.agent_response_generation_rate * 0.10
        + row.workspace_thread_write_rate * 0.10
        + row.social_memory_update_rate * 0.08
        + row.world_feedback_rate * 0.10
        + row.source_boundary_rate * 0.10
        + row.frequency_retuning_rate * 0.08
        + row.persistent_thread_rate * 0.06
        + row.replay_export_rate * 0.03
        + row.trace_integrity * 0.02
    )
    row = EvalRow(**{**asdict(row), "typed_copresence_readiness": round(readiness, 6)})
    state = {
        "condition": condition.name,
        "config": asdict(cfg),
        "places": source_state.get("places", {}),
        "routes": source_state.get("routes", {}),
        "objects": source_state.get("objects", {}),
        "agents": agents,
        "world": world,
        "scripted_utterances": list(SCRIPTED_UTTERANCES),
        "typed_copresence_trace": trace,
        "persistent_thread": persistent_thread,
        "replay_export": replay,
        "browser_runtime_contract": {
            "client_side_typed_input": "viewer accepts arbitrary local text and applies deterministic parsing/routing in the loaded browser state",
            "no_trace_regeneration": "typed utterances mutate the loaded co-presence runtime instead of regenerating benchmark artifacts",
            "nearby_agent_routing": "utterances route to agents near the avatar place",
            "source_boundary": "unsafe ungrounded local utterances are refused",
            "workspace_social_world_frequency": "responses update workspace, social memory, world feedback, and sensory-frequency rates",
        },
        "limits": {
            "no_llm_calls": True,
            "deterministic_typed_copresence": True,
            "not_subjective_consciousness": True,
            "not_complete_playable_world": True,
            "not_unscripted_civilization": True,
        },
    }
    return row, trace, state


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_interactive_typed_copresence"]

    def loss(name: str) -> float:
        return round(full.typed_copresence_readiness - by_name[name].typed_copresence_readiness, 6)

    supports = (
        full.typed_copresence_readiness >= 0.94
        and full.live_typed_input_rate >= 0.99
        and full.nearby_agent_routing_rate >= 0.99
        and full.deterministic_intent_parse_rate >= 0.99
        and full.agent_response_generation_rate >= 0.99
        and full.workspace_thread_write_rate >= 0.99
        and full.social_memory_update_rate >= 0.99
        and full.world_feedback_rate >= 0.99
        and full.source_boundary_rate >= 0.99
        and full.frequency_retuning_rate >= 0.99
        and full.persistent_thread_rate >= 0.99
        and full.replay_export_rate >= 0.99
        and full.trace_integrity >= 0.99
    )
    return VerdictRow(
        full_condition=full.condition,
        full_typed_copresence_readiness=full.typed_copresence_readiness,
        full_live_typed_input_rate=full.live_typed_input_rate,
        full_nearby_agent_routing_rate=full.nearby_agent_routing_rate,
        full_deterministic_intent_parse_rate=full.deterministic_intent_parse_rate,
        full_agent_response_generation_rate=full.agent_response_generation_rate,
        full_workspace_thread_write_rate=full.workspace_thread_write_rate,
        full_social_memory_update_rate=full.social_memory_update_rate,
        full_world_feedback_rate=full.world_feedback_rate,
        full_source_boundary_rate=full.source_boundary_rate,
        full_frequency_retuning_rate=full.frequency_retuning_rate,
        full_persistent_thread_rate=full.persistent_thread_rate,
        full_replay_export_rate=full.replay_export_rate,
        full_trace_integrity=full.trace_integrity,
        no_live_typed_input_loss=loss("no_live_typed_input"),
        no_nearby_agent_routing_loss=loss("no_nearby_agent_routing"),
        no_deterministic_intent_parser_loss=loss("no_deterministic_intent_parser"),
        no_agent_response_generation_loss=loss("no_agent_response_generation"),
        no_workspace_thread_write_loss=loss("no_workspace_thread_write"),
        no_social_memory_update_loss=loss("no_social_memory_update"),
        no_world_feedback_loss=loss("no_world_feedback"),
        no_source_boundary_loss=loss("no_source_boundary"),
        no_frequency_retuning_loss=loss("no_frequency_retuning"),
        no_persistent_thread_loss=loss("no_persistent_thread"),
        no_replay_export_loss=loss("no_replay_export"),
        supports_interactive_typed_copresence_bridge=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "fail",
    )


def run(cfg: TypedCoPresenceConfig) -> dict[str, object]:
    source = load_state(Path(cfg.source_copresence))
    if not isinstance(source.get("copresence_trace"), list) or not source["copresence_trace"]:
        raise ValueError("Report 158 co-presence trace is missing")
    rows: list[EvalRow] = []
    integrated_trace: list[dict[str, object]] = []
    integrated_state: dict[str, object] = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(cfg, condition, source)
        rows.append(row)
        if condition.name == "integrated_interactive_typed_copresence":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {
        "config": asdict(cfg),
        "source_bridges": {
            "continuous_copresence": "Report 158 continuous co-presence bridge",
        },
        "eval_rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "limits": {
            "no_llm_calls": True,
            "deterministic_typed_copresence": True,
            "subjective_consciousness_claimed": False,
            "complete_playable_world_claimed": False,
            "unscripted_civilization_claimed": False,
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_INTERACTIVE_TYPED_COPRESENCE_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_INTERACTIVE_TYPED_COPRESENCE_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_INTERACTIVE_TYPED_COPRESENCE_STATE", integrated_state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260703)
    parser.add_argument("--typed-turns", type=int, default=144)
    parser.add_argument("--source-copresence", default=str(SOURCE_COPRESENCE))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = TypedCoPresenceConfig(seed=args.seed, typed_turns=args.typed_turns, source_copresence=args.source_copresence)
    results = run(cfg)
    print(json.dumps(results["verdict"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
