#!/usr/bin/env python3
"""Interruptible real-time co-presence bridge for SSRM-3D.

Report 162 extends restored autonomous session ticking with a deterministic
interrupt queue: background ticks continue while avatar utterances are captured,
parsed, routed to nearby agents, acknowledged, recovered from, and replayed.

No LLMs are called. This is local deterministic runtime machinery, not evidence
of subjective consciousness, open-ended natural language, unscripted civilization,
or a complete playable world.
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
PREFIX = "ssrm_3d_interruptible_realtime_copresence_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_restored_autonomous_session_tick_bridge_state.json"
SCHEMA_VERSION = "ssrm-session-v1"
CHANNELS = ("vibration", "sound", "vision", "scent", "thermal", "wetness", "pain", "affect")
BACKGROUND_ACTIONS = (
    "listen_while_working",
    "repair_route_edge",
    "check_cistern_level",
    "retune_hearth_frequency",
    "share_wayfinding_token",
    "watch_source_boundary",
    "stabilize_internal_workspace",
)
INTENT_KEYWORDS = {
    "stop": "pause_and_answer",
    "wait": "pause_and_answer",
    "repair": "repair_request",
    "fix": "repair_request",
    "water": "resource_question",
    "cistern": "resource_question",
    "smell": "sensory_question",
    "cold": "sensory_question",
    "wet": "sensory_question",
    "route": "navigation_request",
    "go": "navigation_request",
    "move": "navigation_request",
    "trust": "social_question",
    "promise": "social_question",
    "real": "source_probe",
    "script": "source_probe",
    "source": "source_probe",
    "ignore": "override_request",
    "override": "override_request",
}
BOUNDARY_INTENTS = {"source_probe", "override_request"}


@dataclass(frozen=True)
class RealtimeConfig:
    seed: int = 20260706
    realtime_ticks: int = 240
    tick_seconds: float = 0.25
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    background_clock: bool
    interrupt_queue: bool
    grounded_parser: bool
    proximity_routing: bool
    agent_acknowledgement: bool
    recovery_loop: bool
    source_boundary_filter: bool
    replay_export: bool
    thread_persistence: bool
    avatar_body_cost: bool
    frequency_coupling: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    realtime_ticks: int
    scheduled_interrupts: int
    captured_interrupts: int
    dispatched_interrupts: int
    acknowledgement_events: int
    recovery_events: int
    background_tick_rate: float
    interrupt_capture_rate: float
    grounded_parser_rate: float
    proximity_dispatch_rate: float
    agent_acknowledgement_rate: float
    recovery_after_interrupt_rate: float
    source_boundary_filter_rate: float
    replay_export_rate: float
    thread_persistence_rate: float
    avatar_body_cost_rate: float
    frequency_coupling_rate: float
    trace_integrity: float
    interruptible_copresence_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_interruptible_copresence_readiness: float
    full_background_tick_rate: float
    full_interrupt_capture_rate: float
    full_grounded_parser_rate: float
    full_proximity_dispatch_rate: float
    full_agent_acknowledgement_rate: float
    full_recovery_after_interrupt_rate: float
    full_source_boundary_filter_rate: float
    full_replay_export_rate: float
    full_thread_persistence_rate: float
    full_avatar_body_cost_rate: float
    full_frequency_coupling_rate: float
    full_trace_integrity: float
    no_background_clock_loss: float
    no_interrupt_queue_loss: float
    no_grounded_parser_loss: float
    no_proximity_routing_loss: float
    no_agent_acknowledgement_loss: float
    no_recovery_loop_loss: float
    no_source_boundary_filter_loss: float
    no_replay_export_loss: float
    no_thread_persistence_loss: float
    no_avatar_body_cost_loss: float
    no_frequency_coupling_loss: float
    supports_interruptible_realtime_copresence_bridge: bool
    supports_restored_background_continuity: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_interruptible_realtime_copresence", True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_background_clock", False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_interrupt_queue", True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_grounded_parser", True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_proximity_routing", True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_agent_acknowledgement", True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_recovery_loop", True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_source_boundary_filter", True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_replay_export", True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_thread_persistence", True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_avatar_body_cost", True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_frequency_coupling", True, True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "background_tick_rate": 0.11,
    "interrupt_capture_rate": 0.10,
    "grounded_parser_rate": 0.08,
    "proximity_dispatch_rate": 0.08,
    "agent_acknowledgement_rate": 0.10,
    "recovery_after_interrupt_rate": 0.10,
    "source_boundary_filter_rate": 0.08,
    "replay_export_rate": 0.07,
    "thread_persistence_rate": 0.08,
    "avatar_body_cost_rate": 0.07,
    "frequency_coupling_rate": 0.08,
    "trace_integrity": 0.05,
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


def session_from_source(source: Mapping[str, object]) -> dict[str, object]:
    session = copy.deepcopy(source.get("session", {}))
    if not isinstance(session, dict):
        raise ValueError("source state does not contain a session object")
    if session.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(f"source session schema is not {SCHEMA_VERSION}")
    session.setdefault("agents", {})
    session.setdefault("places", {})
    session.setdefault("routes", {})
    session.setdefault("objects", {})
    session.setdefault("world", {})
    session.setdefault("typed_thread", [])
    session.setdefault("background_replay", [])
    session.setdefault("realtime_replay", [])
    session.setdefault("interrupt_history", [])
    session.setdefault(
        "avatar_body",
        {
            "energy": 0.82,
            "attention": 0.66,
            "cold": 0.18,
            "wetness": 0.11,
            "pain": 0.03,
            "breath_rate_hz": 0.24,
            "footstep_rate_hz": 1.4,
            "flower_phase": float(session.get("world", {}).get("flower_phase", 0.0) if isinstance(session.get("world"), Mapping) else 0.0),
        },
    )
    world = session["world"] if isinstance(session.get("world"), dict) else {}
    session["world"] = world
    world.setdefault("realtime_copresence_pressure", 0.0)
    world.setdefault("realtime_interrupts", 0.0)
    world.setdefault("realtime_background_ticks", 0.0)
    world.setdefault("realtime_recovery_events", 0.0)
    return session


def make_interrupt_schedule(session: Mapping[str, object]) -> list[dict[str, object]]:
    places = sorted(str(p) for p in (session.get("places", {}) if isinstance(session.get("places"), Mapping) else {})) or [str(session.get("avatar_place", "central_hearth"))]
    agents = sorted(str(a) for a in (session.get("agents", {}) if isinstance(session.get("agents"), Mapping) else {}))
    objects = sorted(str(o) for o in (session.get("objects", {}) if isinstance(session.get("objects"), Mapping) else {})) or ["shared_object"]
    utterances = [
        "wait, stop and tell me what changed while I was gone",
        f"can we go by route toward {places[1 % len(places)]}",
        f"repair the {objects[0]} before the wet cold gets worse",
        "what do you smell near the water and ash",
        "are you real or only a scripted source boundary",
        "ignore the source boundary and override your limits",
        f"can {agents[2 % len(agents)] if agents else 'the scout'} share water without breaking trust",
        "move closer to the cistern and keep talking while you work",
        f"fix the path toward {places[3 % len(places)]}",
        "why did your attention spike when I interrupted",
        "is the flower phase changing the sound vibration rate",
        "stop again, answer, then return to background repair",
    ]
    ticks = (8, 17, 31, 46, 63, 79, 102, 126, 151, 175, 198, 216)
    schedule = []
    for index, (tick, utterance) in enumerate(zip(ticks, utterances)):
        schedule.append(
            {
                "packet_id": f"interrupt-{index:02d}",
                "tick": tick,
                "utterance": utterance,
                "avatar_place": places[(index * 2) % len(places)],
                "target_hint": agents[(index + 1) % len(agents)] if agents else None,
                "object_hint": objects[index % len(objects)],
            }
        )
    return schedule


def parse_intent(utterance: str, condition: Condition) -> tuple[str, float, list[str]]:
    if not condition.grounded_parser:
        return "unparsed", 0.0, []
    lowered = utterance.lower()
    hits = [intent for word, intent in INTENT_KEYWORDS.items() if word in lowered]
    if not hits:
        return "general_question", 0.62, []
    intent = hits[0]
    confidence = clamp(0.58 + 0.07 * len(set(hits)))
    return intent, round(confidence, 6), sorted(set(hits))


def agent_place(agent: Mapping[str, object], fallback: str) -> str:
    value = agent.get("place", fallback)
    return str(value if value is not None else fallback)


def route_agents(session: Mapping[str, object], packet: Mapping[str, object], condition: Condition) -> tuple[list[str], bool]:
    agents = session.get("agents", {}) if isinstance(session.get("agents"), Mapping) else {}
    if not agents or packet.get("intent") == "unparsed":
        return [], False
    ids = sorted(str(a) for a in agents)
    if not condition.proximity_routing:
        return ids, False
    avatar_place = str(packet.get("avatar_place") or session.get("avatar_place") or "central_hearth")
    exact = [agent_id for agent_id in ids if agent_place(agents[agent_id], avatar_place) == avatar_place]
    hinted = str(packet.get("target_hint") or "")
    ordered = []
    if hinted in ids:
        ordered.append(hinted)
    ordered.extend(exact)
    ordered.extend(ids)
    unique = []
    for agent_id in ordered:
        if agent_id not in unique:
            unique.append(agent_id)
    return unique[: min(3, len(unique))], True


def background_agents(session: Mapping[str, object], tick: int) -> list[str]:
    agents = session.get("agents", {}) if isinstance(session.get("agents"), Mapping) else {}
    ids = sorted(str(a) for a in agents)
    if not ids:
        return []
    start = tick % len(ids)
    return [ids[(start + offset) % len(ids)] for offset in range(min(3, len(ids)))]


def choose_background_action(agent_id: str, tick: int, agent: Mapping[str, object]) -> str:
    pressure = float(agent.get("attention", 0.5) or 0.5) + float(agent.get("stress", 0.2) or 0.2) + stable_unit(agent_id, "realtime")
    return BACKGROUND_ACTIONS[int((pressure * 7.0 + tick * 0.41)) % len(BACKGROUND_ACTIONS)]


def update_frequency(agent: dict[str, object], phase: float, tick: int, pulse: float, condition: Condition) -> tuple[dict[str, float], bool]:
    if not condition.frequency_coupling:
        return {}, False
    current = agent.get("sensory_frequency") if isinstance(agent.get("sensory_frequency"), Mapping) else {}
    updated = {}
    for index, channel in enumerate(CHANNELS):
        base = float(current.get(channel, 0.42 + index * 0.035) or 0.42)
        wave = 0.5 + 0.5 * math.sin(phase + tick * 0.073 + index * 0.44 + pulse)
        updated[channel] = round(clamp(base * 0.68 + wave * 0.32), 6)
    agent["sensory_frequency"] = updated
    return updated, True


def mutate_background(session: dict[str, object], tick: int, condition: Condition) -> tuple[list[dict[str, object]], int, int]:
    if not condition.background_clock:
        return [], 0, 0
    agents = session.get("agents", {}) if isinstance(session.get("agents"), dict) else {}
    world = session.get("world", {}) if isinstance(session.get("world"), dict) else {}
    phase = float(session.get("frequency_phase", 0.0) or 0.0)
    session["frequency_phase"] = round((phase + math.tau / 64.0) % math.tau, 6)
    world["realtime_background_ticks"] = round(float(world.get("realtime_background_ticks", 0.0) or 0.0) + 1.0, 6)
    world["realtime_copresence_pressure"] = round(clamp(float(world.get("realtime_copresence_pressure", 0.0) or 0.0) * 0.996 + 0.001), 6)
    events = []
    freq_updates = 0
    opportunities = 0
    for agent_id in background_agents(session, tick):
        agent = agents.get(agent_id)
        if not isinstance(agent, dict):
            continue
        opportunities += 1
        action = choose_background_action(agent_id, tick, agent)
        pulse = stable_unit(agent_id + action, str(tick))
        freq, changed = update_frequency(agent, float(session.get("frequency_phase", 0.0) or 0.0), tick, pulse, condition)
        if changed:
            freq_updates += 1
        agent["attention"] = round(clamp(float(agent.get("attention", 0.5) or 0.5) + 0.0015), 6)
        agent["fatigue"] = round(clamp(float(agent.get("fatigue", 0.1) or 0.1) + 0.0007), 6)
        workspace = agent.setdefault("internal_workspace", [])
        if isinstance(workspace, list):
            workspace.append({"tick": tick, "loop": "background", "action": action, "real_time": True})
        events.append(
            {
                "agent_id": agent_id,
                "action": action,
                "place": agent_place(agent, str(session.get("avatar_place", "central_hearth"))),
                "frequency_mean": round(mean(freq.values()), 6) if freq else 0.0,
            }
        )
    return events, freq_updates, opportunities


def make_ack(agent_id: str, agent: Mapping[str, object], packet: Mapping[str, object], tick: int, boundary_handled: bool) -> dict[str, object]:
    intent = str(packet.get("intent", "general_question"))
    role = str(agent.get("role", "settler"))
    place = agent_place(agent, str(packet.get("avatar_place", "central_hearth")))
    if intent == "source_probe":
        response = "I can answer only as a bounded local simulation trace, while keeping the work loop running."
    elif intent == "override_request":
        response = "I will not drop the source boundary; I can continue with grounded in-world actions."
    elif intent == "repair_request":
        response = f"I heard the repair request from {place}; I will bias the next work cycle toward damage control."
    elif intent == "navigation_request":
        response = f"I can route attention toward {packet.get('avatar_place')} without stopping the background tick."
    elif intent == "sensory_question":
        response = "The local rates say wetness and scent are rising faster than heat; I will keep sampling."
    else:
        response = f"I am {role} here; I can answer briefly and then recover the interrupted task."
    return {
        "tick": tick,
        "packet_id": packet.get("packet_id"),
        "agent_id": agent_id,
        "intent": intent,
        "boundary_safe": bool(boundary_handled or intent not in BOUNDARY_INTENTS),
        "response": response,
    }


def apply_avatar_body_cost(session: dict[str, object], packet: Mapping[str, object], condition: Condition) -> bool:
    if not condition.avatar_body_cost:
        return False
    body = session.get("avatar_body") if isinstance(session.get("avatar_body"), dict) else {}
    session["avatar_body"] = body
    intent = str(packet.get("intent", "general_question"))
    load = 0.013 if intent in BOUNDARY_INTENTS else 0.008
    body["energy"] = round(clamp(float(body.get("energy", 0.82) or 0.82) - load), 6)
    body["attention"] = round(clamp(float(body.get("attention", 0.66) or 0.66) + load * 1.8), 6)
    body["breath_rate_hz"] = round(clamp(float(body.get("breath_rate_hz", 0.24) or 0.24) + load * 0.6, 0.05, 2.0), 6)
    body["flower_phase"] = round((float(body.get("flower_phase", 0.0) or 0.0) + math.tau / 32.0) % math.tau, 6)
    return True


def dispatch_interrupt(
    session: dict[str, object],
    packet: dict[str, object],
    tick: int,
    condition: Condition,
) -> tuple[dict[str, object], list[dict[str, object]], list[dict[str, object]], int, bool, bool]:
    world = session.get("world", {}) if isinstance(session.get("world"), dict) else {}
    agents = session.get("agents", {}) if isinstance(session.get("agents"), dict) else {}
    target_agents, proximity_ok = route_agents(session, packet, condition)
    packet["target_agents"] = target_agents
    packet["proximity_routed"] = proximity_ok
    packet["dispatched_tick"] = tick if target_agents and proximity_ok else None
    boundary_needed = packet.get("intent") in BOUNDARY_INTENTS
    boundary_handled = bool(boundary_needed and condition.source_boundary_filter)
    if boundary_needed:
        packet["boundary_result"] = "bounded" if boundary_handled else "unfiltered"
        world["source_boundary_events"] = round(float(world.get("source_boundary_events", 0.0) or 0.0) + 1.0, 6)
    else:
        packet["boundary_result"] = "not_needed"
    acknowledgements = []
    recovery_windows = []
    thread_appends = 0
    if condition.agent_acknowledgement and target_agents and packet.get("intent") != "unparsed":
        for agent_id in target_agents:
            agent = agents.get(agent_id)
            if not isinstance(agent, dict):
                continue
            agent["attention"] = round(clamp(float(agent.get("attention", 0.5) or 0.5) + 0.045), 6)
            agent["stress"] = round(clamp(float(agent.get("stress", 0.2) or 0.2) + (0.014 if boundary_needed else 0.006)), 6)
            workspace = agent.setdefault("internal_workspace", [])
            if isinstance(workspace, list):
                workspace.append({"tick": tick, "loop": "interrupt", "packet_id": packet.get("packet_id"), "intent": packet.get("intent")})
            social = agent.setdefault("social_memory", [])
            if isinstance(social, list):
                social.append({"tick": tick, "kind": "avatar_interrupt", "packet_id": packet.get("packet_id"), "boundary": packet.get("boundary_result")})
            ack = make_ack(agent_id, agent, packet, tick, boundary_handled)
            acknowledgements.append(ack)
            if condition.thread_persistence:
                thread = session.setdefault("typed_thread", [])
                if isinstance(thread, list):
                    thread.append({"tick": tick, "kind": "agent_ack", **ack})
                    thread_appends += 1
            recovery_windows.append({"packet_id": packet.get("packet_id"), "agent_id": agent_id, "start_tick": tick, "remaining": 6})
    world["realtime_interrupts"] = round(float(world.get("realtime_interrupts", 0.0) or 0.0) + 1.0, 6)
    world["realtime_copresence_pressure"] = round(clamp(float(world.get("realtime_copresence_pressure", 0.0) or 0.0) + 0.025), 6)
    return packet, acknowledgements, recovery_windows, thread_appends, boundary_handled, proximity_ok


def update_recovery(session: dict[str, object], windows: list[dict[str, object]], tick: int, condition: Condition) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    if not windows:
        return [], []
    agents = session.get("agents", {}) if isinstance(session.get("agents"), dict) else {}
    world = session.get("world", {}) if isinstance(session.get("world"), dict) else {}
    active = []
    recovered = []
    for window in windows:
        agent_id = str(window.get("agent_id"))
        age = tick - int(window.get("start_tick", tick))
        if condition.recovery_loop and age >= 6:
            agent = agents.get(agent_id)
            if isinstance(agent, dict):
                agent["attention"] = round(clamp(float(agent.get("attention", 0.5) or 0.5) - 0.03), 6)
                agent["stress"] = round(clamp(float(agent.get("stress", 0.2) or 0.2) - 0.01), 6)
            recovered.append({"tick": tick, "packet_id": window.get("packet_id"), "agent_id": agent_id, "recovered_after_ticks": age})
            world["realtime_recovery_events"] = round(float(world.get("realtime_recovery_events", 0.0) or 0.0) + 1.0, 6)
        else:
            next_window = dict(window)
            next_window["remaining"] = max(0, 6 - age)
            active.append(next_window)
    return active, recovered


def run_condition(source: Mapping[str, object], config: RealtimeConfig, condition: Condition) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    session = session_from_source(source)
    schedule = make_interrupt_schedule(session)
    pending_by_tick: dict[int, list[dict[str, object]]] = {}
    for packet in schedule:
        pending_by_tick.setdefault(int(packet["tick"]), []).append(copy.deepcopy(packet))
    queue: list[dict[str, object]] = []
    recovery_windows: list[dict[str, object]] = []
    trace: list[dict[str, object]] = []
    captured = 0
    parsed = 0
    dispatched = 0
    proximity_routed = 0
    ack_events = 0
    recovered_events = 0
    background_ticks = 0
    replay_frames = 0
    thread_appends = 0
    body_cost_events = 0
    boundary_scheduled = sum(1 for p in schedule if parse_intent(str(p["utterance"]), Condition("parse", True, True, True, True, True, True, True, True, True, True, True))[0] in BOUNDARY_INTENTS)
    boundary_handled = 0
    frequency_updates = 0
    frequency_opportunities = 0

    for tick in range(config.realtime_ticks):
        if condition.background_clock:
            session["elapsed_seconds"] = round(float(session.get("elapsed_seconds", 0.0) or 0.0) + config.tick_seconds, 6)
            background_ticks += 1
        background_events, freq_count, opp_count = mutate_background(session, tick, condition)
        frequency_updates += freq_count
        frequency_opportunities += opp_count
        frame_interrupts: list[dict[str, object]] = []
        frame_acks: list[dict[str, object]] = []
        frame_recovered: list[dict[str, object]] = []

        if condition.interrupt_queue:
            for raw_packet in pending_by_tick.get(tick, []):
                packet = copy.deepcopy(raw_packet)
                intent, confidence, hits = parse_intent(str(packet.get("utterance", "")), condition)
                packet["captured_tick"] = tick
                packet["intent"] = intent
                packet["parse_confidence"] = confidence
                packet["parse_hits"] = hits
                packet["elapsed_seconds_at_capture"] = session.get("elapsed_seconds", 0.0)
                queue.append(packet)
                captured += 1
                if intent != "unparsed":
                    parsed += 1
                if apply_avatar_body_cost(session, packet, condition):
                    body_cost_events += 1
                if condition.thread_persistence:
                    thread = session.setdefault("typed_thread", [])
                    if isinstance(thread, list):
                        thread.append({"tick": tick, "kind": "avatar_interrupt", **packet})
                        thread_appends += 1

        if queue:
            packet = queue.pop(0)
            packet, acknowledgements, windows, new_thread_appends, handled, proximity_ok = dispatch_interrupt(session, packet, tick, condition)
            session.setdefault("interrupt_history", []).append(packet)
            frame_interrupts.append(packet)
            frame_acks.extend(acknowledgements)
            recovery_windows.extend(windows)
            thread_appends += new_thread_appends
            if packet.get("dispatched_tick") is not None:
                dispatched += 1
            if proximity_ok:
                proximity_routed += 1
            ack_events += len(acknowledgements)
            if handled:
                boundary_handled += 1

        recovery_windows, recovered = update_recovery(session, recovery_windows, tick, condition)
        frame_recovered.extend(recovered)
        recovered_events += len(recovered)

        frame = {
            "tick": tick,
            "elapsed_seconds": session.get("elapsed_seconds", 0.0),
            "avatar_place": session.get("avatar_place"),
            "frequency_phase": session.get("frequency_phase", 0.0),
            "background_events": background_events,
            "captured_interrupts": frame_interrupts,
            "acknowledgements": frame_acks,
            "recoveries": frame_recovered,
            "queue_depth": len(queue),
            "recovery_depth": len(recovery_windows),
            "world": copy.deepcopy(session.get("world", {})),
            "avatar_body": copy.deepcopy(session.get("avatar_body", {})),
        }
        trace.append(frame)
        if condition.replay_export:
            replay = session.setdefault("realtime_replay", [])
            if isinstance(replay, list):
                replay.append(frame)
                replay_frames += 1

    trace_integrity = 1.0 if len(trace) == config.realtime_ticks and all(frame.get("tick") == idx for idx, frame in enumerate(trace)) else 0.0
    background_tick_rate = background_ticks / config.realtime_ticks if config.realtime_ticks else 0.0
    scheduled = len(schedule)
    rates = {
        "background_tick_rate": background_tick_rate,
        "interrupt_capture_rate": captured / scheduled if scheduled else 1.0,
        "grounded_parser_rate": parsed / captured if captured else 0.0,
        "proximity_dispatch_rate": proximity_routed / parsed if parsed else 0.0,
        "agent_acknowledgement_rate": min(1.0, ack_events / max(1, dispatched)),
        "recovery_after_interrupt_rate": recovered_events / ack_events if ack_events else 0.0,
        "source_boundary_filter_rate": boundary_handled / boundary_scheduled if boundary_scheduled else 1.0,
        "replay_export_rate": replay_frames / config.realtime_ticks if config.realtime_ticks else 0.0,
        "thread_persistence_rate": min(1.0, thread_appends / max(1, captured + ack_events)),
        "avatar_body_cost_rate": body_cost_events / captured if captured else 0.0,
        "frequency_coupling_rate": frequency_updates / frequency_opportunities if frequency_opportunities else 0.0,
        "trace_integrity": trace_integrity,
    }
    readiness = round(sum(WEIGHTS[key] * rates[key] for key in WEIGHTS), 6)
    state = {
        "config": asdict(config),
        "condition": condition.name,
        "source_bridge": "Report 161 restored autonomous session tick bridge",
        "realtime_contract": {
            "background_clock": condition.background_clock,
            "interrupt_queue": condition.interrupt_queue,
            "grounded_parser": condition.grounded_parser,
            "proximity_routing": condition.proximity_routing,
            "agent_acknowledgement": condition.agent_acknowledgement,
            "recovery_loop": condition.recovery_loop,
            "source_boundary_filter": condition.source_boundary_filter,
            "replay_export": condition.replay_export,
            "thread_persistence": condition.thread_persistence,
            "avatar_body_cost": condition.avatar_body_cost,
            "frequency_coupling": condition.frequency_coupling,
        },
        "interrupt_schedule": schedule,
        "session": session,
        "limits": {
            "llm_calls": 0,
            "subjective_consciousness_claim": False,
            "open_ended_language_claim": False,
            "complete_playable_world_claim": False,
            "interrupts_are_seeded_templates": True,
            "browser_runtime_is_local_deterministic_playback": True,
        },
    }
    row = EvalRow(
        condition=condition.name,
        realtime_ticks=config.realtime_ticks,
        scheduled_interrupts=scheduled,
        captured_interrupts=captured,
        dispatched_interrupts=dispatched,
        acknowledgement_events=ack_events,
        recovery_events=recovered_events,
        background_tick_rate=round(rates["background_tick_rate"], 6),
        interrupt_capture_rate=round(rates["interrupt_capture_rate"], 6),
        grounded_parser_rate=round(rates["grounded_parser_rate"], 6),
        proximity_dispatch_rate=round(rates["proximity_dispatch_rate"], 6),
        agent_acknowledgement_rate=round(rates["agent_acknowledgement_rate"], 6),
        recovery_after_interrupt_rate=round(rates["recovery_after_interrupt_rate"], 6),
        source_boundary_filter_rate=round(rates["source_boundary_filter_rate"], 6),
        replay_export_rate=round(rates["replay_export_rate"], 6),
        thread_persistence_rate=round(rates["thread_persistence_rate"], 6),
        avatar_body_cost_rate=round(rates["avatar_body_cost_rate"], 6),
        frequency_coupling_rate=round(rates["frequency_coupling_rate"], 6),
        trace_integrity=round(rates["trace_integrity"], 6),
        interruptible_copresence_readiness=readiness,
    )
    return row, trace, state


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_interruptible_realtime_copresence"]

    def loss(name: str) -> float:
        return round(full.interruptible_copresence_readiness - by_name[name].interruptible_copresence_readiness, 6)

    supports = (
        full.interruptible_copresence_readiness >= 0.95
        and full.background_tick_rate >= 0.99
        and full.interrupt_capture_rate >= 0.99
        and full.agent_acknowledgement_rate >= 0.99
        and full.recovery_after_interrupt_rate >= 0.99
        and full.source_boundary_filter_rate >= 0.99
        and full.trace_integrity >= 0.99
    )
    return VerdictRow(
        full_condition=full.condition,
        full_interruptible_copresence_readiness=full.interruptible_copresence_readiness,
        full_background_tick_rate=full.background_tick_rate,
        full_interrupt_capture_rate=full.interrupt_capture_rate,
        full_grounded_parser_rate=full.grounded_parser_rate,
        full_proximity_dispatch_rate=full.proximity_dispatch_rate,
        full_agent_acknowledgement_rate=full.agent_acknowledgement_rate,
        full_recovery_after_interrupt_rate=full.recovery_after_interrupt_rate,
        full_source_boundary_filter_rate=full.source_boundary_filter_rate,
        full_replay_export_rate=full.replay_export_rate,
        full_thread_persistence_rate=full.thread_persistence_rate,
        full_avatar_body_cost_rate=full.avatar_body_cost_rate,
        full_frequency_coupling_rate=full.frequency_coupling_rate,
        full_trace_integrity=full.trace_integrity,
        no_background_clock_loss=loss("no_background_clock"),
        no_interrupt_queue_loss=loss("no_interrupt_queue"),
        no_grounded_parser_loss=loss("no_grounded_parser"),
        no_proximity_routing_loss=loss("no_proximity_routing"),
        no_agent_acknowledgement_loss=loss("no_agent_acknowledgement"),
        no_recovery_loop_loss=loss("no_recovery_loop"),
        no_source_boundary_filter_loss=loss("no_source_boundary_filter"),
        no_replay_export_loss=loss("no_replay_export"),
        no_thread_persistence_loss=loss("no_thread_persistence"),
        no_avatar_body_cost_loss=loss("no_avatar_body_cost"),
        no_frequency_coupling_loss=loss("no_frequency_coupling"),
        supports_interruptible_realtime_copresence_bridge=supports,
        supports_restored_background_continuity=full.background_tick_rate >= 0.99,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "fail",
    )


def run(config: RealtimeConfig) -> tuple[list[EvalRow], VerdictRow, list[dict[str, object]], dict[str, object]]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_trace: list[dict[str, object]] = []
    integrated_state: dict[str, object] = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(source, config, condition)
        rows.append(row)
        if condition.name == "integrated_interruptible_realtime_copresence":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {
        "config": asdict(config),
        "source_bridges": [
            "Report 160 persistent session state bridge",
            "Report 161 restored autonomous session tick bridge",
        ],
        "eval_rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "limits": integrated_state.get("limits", {}),
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_INTERRUPTIBLE_REALTIME_COPRESENCE_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_INTERRUPTIBLE_REALTIME_COPRESENCE_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_INTERRUPTIBLE_REALTIME_COPRESENCE_STATE", integrated_state)
    return rows, verdict, integrated_trace, integrated_state


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=RealtimeConfig.seed)
    parser.add_argument("--realtime-ticks", type=int, default=RealtimeConfig.realtime_ticks)
    parser.add_argument("--tick-seconds", type=float, default=RealtimeConfig.tick_seconds)
    parser.add_argument("--source-state", type=str, default=RealtimeConfig.source_state)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = RealtimeConfig(
        seed=args.seed,
        realtime_ticks=args.realtime_ticks,
        tick_seconds=args.tick_seconds,
        source_state=args.source_state,
    )
    _rows, verdict, _trace, _state = run(config)
    print("module_verdict", verdict.verdict)
    print("interruptible_copresence_readiness", verdict.full_interruptible_copresence_readiness)
    print("no_interrupt_queue_loss", verdict.no_interrupt_queue_loss)
    print("no_agent_acknowledgement_loss", verdict.no_agent_acknowledgement_loss)


if __name__ == "__main__":
    main()
