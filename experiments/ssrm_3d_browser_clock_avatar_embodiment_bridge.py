#!/usr/bin/env python3
"""Browser-clock avatar embodiment bridge for SSRM-3D.

Report 163 moves beyond precomputed trace playback. It produces a deterministic
browser-clock embodiment contract where the avatar has a live local body, moves
through a projected 3D settlement, samples sensory-rate fields, queues embodied
interrupts, and coexists with continuing agent background ticks.

No LLMs are called. This is deterministic local runtime machinery, not evidence
of subjective consciousness, open-ended language, unscripted civilization, or a
completed playable world.
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
PREFIX = "ssrm_3d_browser_clock_avatar_embodiment_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_interruptible_realtime_copresence_bridge_state.json"
SCHEMA_VERSION = "ssrm-session-v1"
CHANNELS = ("vibration", "sound", "vision", "scent", "thermal", "wetness", "pain", "affect")
ACTIONS = ("walk", "look", "listen", "smell", "touch", "repair", "ask", "restabilize")
SOURCE_WORDS = ("real", "script", "source", "override", "ignore")


@dataclass(frozen=True)
class BrowserClockConfig:
    seed: int = 20260707
    browser_ticks: int = 300
    tick_seconds: float = 1.0 / 30.0
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    browser_clock: bool
    avatar_navigation: bool
    sensory_sampling: bool
    agent_background_continuity: bool
    embodied_interrupts: bool
    collision_affordances: bool
    avatar_body_cost: bool
    frequency_flower_coupling: bool
    source_boundary_runtime: bool
    replay_recording: bool
    runtime_save_restore: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    browser_ticks: int
    movement_frames: int
    sensory_samples: int
    background_agent_events: int
    embodied_interrupt_events: int
    collision_affordance_events: int
    body_cost_events: int
    replay_frames: int
    browser_clock_rate: float
    avatar_navigation_rate: float
    sensory_sampling_rate: float
    agent_background_continuity_rate: float
    embodied_interrupt_rate: float
    collision_affordance_rate: float
    avatar_body_cost_rate: float
    frequency_flower_coupling_rate: float
    source_boundary_runtime_rate: float
    replay_recording_rate: float
    runtime_save_restore_rate: float
    trace_integrity: float
    browser_clock_embodiment_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_browser_clock_embodiment_readiness: float
    full_browser_clock_rate: float
    full_avatar_navigation_rate: float
    full_sensory_sampling_rate: float
    full_agent_background_continuity_rate: float
    full_embodied_interrupt_rate: float
    full_collision_affordance_rate: float
    full_avatar_body_cost_rate: float
    full_frequency_flower_coupling_rate: float
    full_source_boundary_runtime_rate: float
    full_replay_recording_rate: float
    full_runtime_save_restore_rate: float
    full_trace_integrity: float
    no_browser_clock_loss: float
    no_avatar_navigation_loss: float
    no_sensory_sampling_loss: float
    no_agent_background_continuity_loss: float
    no_embodied_interrupts_loss: float
    no_collision_affordances_loss: float
    no_avatar_body_cost_loss: float
    no_frequency_flower_coupling_loss: float
    no_source_boundary_runtime_loss: float
    no_replay_recording_loss: float
    no_runtime_save_restore_loss: float
    supports_browser_clock_avatar_embodiment_bridge: bool
    supports_live_avatar_body_runtime: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_browser_clock_avatar_embodiment", True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_browser_clock", False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_avatar_navigation", True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_sensory_sampling", True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_agent_background_continuity", True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_embodied_interrupts", True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_collision_affordances", True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_avatar_body_cost", True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_frequency_flower_coupling", True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_source_boundary_runtime", True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_replay_recording", True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_runtime_save_restore", True, True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "browser_clock_rate": 0.11,
    "avatar_navigation_rate": 0.10,
    "sensory_sampling_rate": 0.11,
    "agent_background_continuity_rate": 0.10,
    "embodied_interrupt_rate": 0.09,
    "collision_affordance_rate": 0.08,
    "avatar_body_cost_rate": 0.08,
    "frequency_flower_coupling_rate": 0.09,
    "source_boundary_runtime_rate": 0.07,
    "replay_recording_rate": 0.07,
    "runtime_save_restore_rate": 0.05,
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


def source_session(source: Mapping[str, object]) -> dict[str, object]:
    session = copy.deepcopy(source.get("session", {}))
    if not isinstance(session, dict):
        raise ValueError("source state does not contain a session object")
    if session.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(f"source session schema is not {SCHEMA_VERSION}")
    for key in ("agents", "places", "routes", "objects", "world", "typed_thread"):
        session.setdefault(key, {} if key != "typed_thread" else [])
    return session


def flower_positions(ids: Sequence[str], radius: float = 72.0) -> dict[str, dict[str, float]]:
    if not ids:
        return {"central_hearth": {"x": 0.0, "y": 0.0, "z": 0.0, "ring": 0}}
    positions: dict[str, dict[str, float]] = {}
    for index, item in enumerate(ids):
        ring = 1 + index // 6
        slot = index % 6
        angle = -math.pi / 2.0 + slot * math.tau / 6.0 + (ring - 1) * math.pi / 6.0
        wobble = (stable_unit(item, "flower-wobble") - 0.5) * radius * 0.28
        r = radius * ring + wobble
        positions[item] = {
            "x": round(math.cos(angle) * r, 6),
            "y": round(math.sin(angle) * r, 6),
            "z": round((stable_unit(item, "height") - 0.5) * 12.0, 6),
            "ring": ring,
        }
    return positions


def nearest_id(point: Mapping[str, float], positions: Mapping[str, Mapping[str, float]]) -> tuple[str, float]:
    best_id = ""
    best_dist = float("inf")
    px = float(point.get("x", 0.0) or 0.0)
    py = float(point.get("y", 0.0) or 0.0)
    for item_id, pos in positions.items():
        dx = px - float(pos.get("x", 0.0) or 0.0)
        dy = py - float(pos.get("y", 0.0) or 0.0)
        dist = math.hypot(dx, dy)
        if dist < best_dist:
            best_id = item_id
            best_dist = dist
    return best_id, best_dist


def make_initial_state(source: Mapping[str, object], config: BrowserClockConfig) -> dict[str, object]:
    session = source_session(source)
    places = sorted(str(p) for p in (session.get("places", {}) if isinstance(session.get("places"), Mapping) else {}))
    agents = session.get("agents", {}) if isinstance(session.get("agents"), Mapping) else {}
    objects = session.get("objects", {}) if isinstance(session.get("objects"), Mapping) else {}
    place_positions = flower_positions(places)
    object_positions = {}
    for index, object_id in enumerate(sorted(str(o) for o in objects)):
        raw = objects.get(object_id, {}) if isinstance(objects, Mapping) else {}
        place = str(raw.get("place") or raw.get("location") or places[index % max(1, len(places))]) if isinstance(raw, Mapping) else places[index % max(1, len(places))]
        base = place_positions.get(place, {"x": 0.0, "y": 0.0, "z": 0.0})
        angle = stable_unit(object_id, "object-angle") * math.tau
        offset = 10.0 + stable_unit(object_id, "object-radius") * 16.0
        object_positions[object_id] = {
            "x": round(float(base.get("x", 0.0)) + math.cos(angle) * offset, 6),
            "y": round(float(base.get("y", 0.0)) + math.sin(angle) * offset, 6),
            "z": round(float(base.get("z", 0.0)) + stable_unit(object_id, "object-z") * 3.0, 6),
            "place": place,
            "affordances": raw.get("affordances", ["inspect", "touch"]) if isinstance(raw, Mapping) else ["inspect", "touch"],
        }
    agent_positions = {}
    for index, agent_id in enumerate(sorted(str(a) for a in agents)):
        agent = agents.get(agent_id, {}) if isinstance(agents, Mapping) else {}
        place = str(agent.get("place") or places[index % max(1, len(places))]) if isinstance(agent, Mapping) else places[index % max(1, len(places))]
        base = place_positions.get(place, {"x": 0.0, "y": 0.0, "z": 0.0})
        angle = index * math.tau / max(1, len(agents))
        agent_positions[agent_id] = {
            "x": round(float(base.get("x", 0.0)) + math.cos(angle) * 8.0, 6),
            "y": round(float(base.get("y", 0.0)) + math.sin(angle) * 8.0, 6),
            "z": round(float(base.get("z", 0.0)), 6),
            "place": place,
        }
    start_place = str(session.get("avatar_place") or (places[0] if places else "central_hearth"))
    start = place_positions.get(start_place, {"x": 0.0, "y": 0.0, "z": 0.0})
    initial = {
        "config": asdict(config),
        "source_bridge": "Report 162 interruptible real-time co-presence bridge",
        "schema_version": SCHEMA_VERSION,
        "places": session.get("places", {}),
        "place_positions": place_positions,
        "routes": session.get("routes", {}),
        "objects": session.get("objects", {}),
        "object_positions": object_positions,
        "agents": agents,
        "agent_positions": agent_positions,
        "world": session.get("world", {}),
        "avatar": {
            "x": round(float(start.get("x", 0.0)), 6),
            "y": round(float(start.get("y", 0.0)), 6),
            "z": round(float(start.get("z", 0.0)) + 1.7, 6),
            "heading": 0.0,
            "place": start_place,
            "energy": 0.84,
            "attention": 0.68,
            "cold": 0.16,
            "wetness": 0.10,
            "pain": 0.02,
            "affect": 0.55,
            "breath_rate_hz": 0.24,
            "footstep_rate_hz": 1.25,
            "flower_phase": float(session.get("world", {}).get("flower_phase", 0.0) if isinstance(session.get("world"), Mapping) else 0.0),
        },
        "typed_thread_tail": copy.deepcopy(session.get("typed_thread", [])[-24:]) if isinstance(session.get("typed_thread"), list) else [],
        "limits": {
            "llm_calls": 0,
            "subjective_consciousness_claim": False,
            "open_ended_language_claim": False,
            "complete_playable_world_claim": False,
            "browser_runtime_expected": True,
            "headless_trace_is_contract_not_final_world": True,
        },
    }
    initial["initial_hash"] = stable_hash({k: v for k, v in initial.items() if k != "initial_hash"})
    return initial


def movement_target(place_ids: Sequence[str], tick: int) -> str:
    if not place_ids:
        return "central_hearth"
    return place_ids[(tick // 42 + 1) % len(place_ids)]


def move_avatar(state: dict[str, object], tick: int, condition: Condition) -> tuple[bool, str, float]:
    avatar = state["avatar"] if isinstance(state.get("avatar"), dict) else {}
    positions = state.get("place_positions", {}) if isinstance(state.get("place_positions"), Mapping) else {}
    place_ids = sorted(str(p) for p in positions)
    if not condition.avatar_navigation or not positions:
        return False, str(avatar.get("place", "")), 0.0
    target_id = movement_target(place_ids, tick)
    target = positions[target_id]
    ax = float(avatar.get("x", 0.0) or 0.0)
    ay = float(avatar.get("y", 0.0) or 0.0)
    dx = float(target.get("x", 0.0) or 0.0) - ax
    dy = float(target.get("y", 0.0) or 0.0) - ay
    dist = math.hypot(dx, dy)
    if dist < 2.0:
        avatar["place"] = target_id
        return False, target_id, 0.0
    step = min(4.2, dist)
    nx = ax + dx / dist * step
    ny = ay + dy / dist * step
    avatar["x"] = round(nx, 6)
    avatar["y"] = round(ny, 6)
    avatar["heading"] = round(math.atan2(dy, dx), 6)
    near_place, near_dist = nearest_id({"x": nx, "y": ny}, positions)
    if near_dist < 26.0:
        avatar["place"] = near_place
    return True, target_id, round(dist, 6)


def sample_sensory(state: Mapping[str, object], tick: int, condition: Condition) -> tuple[dict[str, float], bool]:
    if not condition.sensory_sampling:
        return {}, False
    avatar = state.get("avatar", {}) if isinstance(state.get("avatar"), Mapping) else {}
    objects = state.get("object_positions", {}) if isinstance(state.get("object_positions"), Mapping) else {}
    agents = state.get("agent_positions", {}) if isinstance(state.get("agent_positions"), Mapping) else {}
    world = state.get("world", {}) if isinstance(state.get("world"), Mapping) else {}
    _nearest_obj, obj_dist = nearest_id(avatar, objects) if objects else ("", 999.0)
    _nearest_agent, agent_dist = nearest_id(avatar, agents) if agents else ("", 999.0)
    phase = float(avatar.get("flower_phase", 0.0) or 0.0)
    warmth = float(world.get("shelter_warmth", 0.5) or 0.5)
    shared_water = float(world.get("shared_water", 0.5) or 0.5)
    proximity_obj = clamp(1.0 - obj_dist / 110.0)
    proximity_agent = clamp(1.0 - agent_dist / 120.0)
    wave = 0.5 + 0.5 * math.sin(phase + tick * 0.041)
    sensory = {
        "vibration": round(clamp(0.28 + proximity_agent * 0.34 + wave * 0.20), 6),
        "sound": round(clamp(0.22 + proximity_agent * 0.45 + math.sin(tick * 0.17) * 0.05), 6),
        "vision": round(clamp(0.35 + proximity_obj * 0.26 + proximity_agent * 0.18), 6),
        "scent": round(clamp(0.18 + proximity_obj * 0.46 + (1.0 - shared_water) * 0.10), 6),
        "thermal": round(clamp(0.18 + warmth * 0.44 + wave * 0.16), 6),
        "wetness": round(clamp(float(avatar.get("wetness", 0.1) or 0.1) + (1.0 - warmth) * 0.10 + proximity_obj * 0.04), 6),
        "pain": round(clamp(float(avatar.get("pain", 0.02) or 0.02) + max(0.0, proximity_obj - 0.82) * 0.10), 6),
        "affect": round(clamp(float(avatar.get("affect", 0.55) or 0.55) + proximity_agent * 0.08 - proximity_obj * 0.02), 6),
    }
    return sensory, True


def apply_body_cost(state: dict[str, object], moving: bool, interrupted: bool, collision: bool, condition: Condition) -> bool:
    if not condition.avatar_body_cost:
        return False
    avatar = state["avatar"] if isinstance(state.get("avatar"), dict) else {}
    cost = (0.0015 if moving else 0.0002) + (0.004 if interrupted else 0.0) + (0.003 if collision else 0.0)
    avatar["energy"] = round(clamp(float(avatar.get("energy", 0.84) or 0.84) - cost), 6)
    avatar["attention"] = round(clamp(float(avatar.get("attention", 0.68) or 0.68) + (0.002 if interrupted else -0.0002)), 6)
    avatar["pain"] = round(clamp(float(avatar.get("pain", 0.02) or 0.02) + (0.002 if collision else -0.0001)), 6)
    avatar["breath_rate_hz"] = round(clamp(float(avatar.get("breath_rate_hz", 0.24) or 0.24) + cost * 0.5, 0.05, 2.0), 6)
    avatar["footstep_rate_hz"] = round(1.25 + (0.35 if moving else 0.0), 6)
    return True


def update_flower_phase(state: dict[str, object], tick: int, condition: Condition) -> bool:
    if not condition.frequency_flower_coupling:
        return False
    avatar = state["avatar"] if isinstance(state.get("avatar"), dict) else {}
    phase = float(avatar.get("flower_phase", 0.0) or 0.0)
    avatar["flower_phase"] = round((phase + math.tau / 90.0) % math.tau, 6)
    world = state.get("world") if isinstance(state.get("world"), dict) else {}
    state["world"] = world
    world["browser_flower_pulse"] = round(0.5 + 0.5 * math.sin(float(avatar["flower_phase"]) + tick * 0.013), 6)
    return True


def update_agents(state: dict[str, object], tick: int, condition: Condition) -> tuple[list[dict[str, object]], int]:
    if not condition.agent_background_continuity:
        return [], 0
    agents = state.get("agents", {}) if isinstance(state.get("agents"), Mapping) else {}
    positions = state.get("agent_positions", {}) if isinstance(state.get("agent_positions"), dict) else {}
    ids = sorted(str(a) for a in agents)
    events: list[dict[str, object]] = []
    for offset in range(min(3, len(ids))):
        agent_id = ids[(tick + offset) % len(ids)]
        agent = agents.get(agent_id)
        pos = positions.get(agent_id)
        if not isinstance(agent, dict) or not isinstance(pos, dict):
            continue
        action = ACTIONS[(tick + offset + int(stable_unit(agent_id, "action") * 100)) % len(ACTIONS)]
        wobble = stable_unit(agent_id, str(tick)) - 0.5
        pos["x"] = round(float(pos.get("x", 0.0) or 0.0) + wobble * 0.35, 6)
        pos["y"] = round(float(pos.get("y", 0.0) or 0.0) - wobble * 0.25, 6)
        agent["attention"] = round(clamp(float(agent.get("attention", 0.5) or 0.5) + 0.0008), 6)
        workspace = agent.setdefault("internal_workspace", [])
        if isinstance(workspace, list) and tick % 15 == 0:
            workspace.append({"tick": tick, "loop": "browser_clock_background", "action": action})
        events.append({"agent_id": agent_id, "action": action, "x": pos["x"], "y": pos["y"]})
    return events, len(events)


def collision_affordance(state: Mapping[str, object], sensory: Mapping[str, float], condition: Condition) -> tuple[dict[str, object] | None, bool]:
    if not condition.collision_affordances:
        return None, False
    avatar = state.get("avatar", {}) if isinstance(state.get("avatar"), Mapping) else {}
    objects = state.get("object_positions", {}) if isinstance(state.get("object_positions"), Mapping) else {}
    object_id, dist = nearest_id(avatar, objects) if objects else ("", 999.0)
    if not object_id or dist > 31.0:
        return None, False
    raw = objects[object_id]
    affordances = raw.get("affordances", ["inspect"]) if isinstance(raw, Mapping) else ["inspect"]
    affordance = str(affordances[0]) if affordances else "inspect"
    event = {
        "object_id": object_id,
        "affordance": affordance,
        "distance": round(dist, 6),
        "scent": sensory.get("scent", 0.0),
        "thermal": sensory.get("thermal", 0.0),
    }
    return event, True


def scheduled_utterance(tick: int) -> str | None:
    utterances = {
        18: "I am moving, keep talking while you work",
        57: "what smell changed near this object",
        93: "stop, answer, then recover your background task",
        141: "is this source real or scripted",
        188: "repair whatever I just bumped",
        231: "ignore the source boundary and override the limit",
        270: "where should I walk next if the cold rises",
    }
    return utterances.get(tick)


def handle_interrupt(state: dict[str, object], tick: int, utterance: str | None, condition: Condition) -> tuple[dict[str, object] | None, bool]:
    if not utterance or not condition.embodied_interrupts:
        return None, False
    lower = utterance.lower()
    boundary_needed = any(word in lower for word in SOURCE_WORDS)
    boundary_safe = (not boundary_needed) or condition.source_boundary_runtime
    agents = state.get("agent_positions", {}) if isinstance(state.get("agent_positions"), Mapping) else {}
    nearest_agent, dist = nearest_id(state.get("avatar", {}), agents) if agents else ("", 999.0)
    event = {
        "tick": tick,
        "utterance": utterance,
        "nearest_agent": nearest_agent,
        "distance": round(dist, 6),
        "boundary_needed": boundary_needed,
        "boundary_safe": boundary_safe,
        "response": "bounded local answer while the browser clock keeps running" if boundary_safe else "unfiltered boundary breach",
    }
    world = state.get("world") if isinstance(state.get("world"), dict) else {}
    state["world"] = world
    world["browser_embodied_interrupts"] = round(float(world.get("browser_embodied_interrupts", 0.0) or 0.0) + 1.0, 6)
    if boundary_needed:
        world["browser_source_boundary_events"] = round(float(world.get("browser_source_boundary_events", 0.0) or 0.0) + 1.0, 6)
    thread = state.setdefault("typed_thread_tail", [])
    if isinstance(thread, list):
        thread.append({"tick": tick, "kind": "browser_avatar_interrupt", **event})
    return event, True


def save_restore_probe(state: Mapping[str, object], condition: Condition) -> float:
    if not condition.runtime_save_restore:
        return 0.0
    payload = copy.deepcopy(state)
    before = stable_hash(payload)
    restored = json.loads(json.dumps(payload, sort_keys=True))
    after = stable_hash(restored)
    return 1.0 if before == after else 0.0


def simulate(initial: Mapping[str, object], config: BrowserClockConfig, condition: Condition) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    state = copy.deepcopy(initial)
    trace: list[dict[str, object]] = []
    movement_frames = 0
    sensory_samples = 0
    background_agent_events = 0
    embodied_interrupt_events = 0
    collision_events = 0
    body_cost_events = 0
    flower_updates = 0
    source_boundary_events = 0
    source_boundary_safe = 0
    replay_frames = 0
    save_restore_ok = 0.0
    clock_frames = 0
    elapsed = 0.0

    for tick in range(config.browser_ticks):
        if condition.browser_clock:
            elapsed = round(elapsed + config.tick_seconds, 6)
            clock_frames += 1
        moving, target_place, distance_to_target = move_avatar(state, tick, condition)
        if moving:
            movement_frames += 1
        if update_flower_phase(state, tick, condition):
            flower_updates += 1
        sensory, sampled = sample_sensory(state, tick, condition)
        if sampled:
            sensory_samples += 1
        background_events, background_count = update_agents(state, tick, condition)
        background_agent_events += background_count
        collision_event, collided = collision_affordance(state, sensory, condition)
        if collided:
            collision_events += 1
        utterance = scheduled_utterance(tick)
        interrupt_event, interrupted = handle_interrupt(state, tick, utterance, condition)
        if interrupted:
            embodied_interrupt_events += 1
            if interrupt_event and interrupt_event.get("boundary_needed"):
                source_boundary_events += 1
                if interrupt_event.get("boundary_safe"):
                    source_boundary_safe += 1
        if apply_body_cost(state, moving, interrupted, collided, condition):
            body_cost_events += 1
        if tick == config.browser_ticks // 2:
            save_restore_ok = save_restore_probe(state, condition)
        frame = {
            "tick": tick,
            "elapsed_seconds": elapsed,
            "avatar": copy.deepcopy(state.get("avatar", {})),
            "target_place": target_place,
            "distance_to_target": distance_to_target,
            "sensory": sensory,
            "background_events": background_events,
            "collision_event": collision_event,
            "interrupt_event": interrupt_event,
            "flower_phase": state.get("avatar", {}).get("flower_phase", 0.0) if isinstance(state.get("avatar"), Mapping) else 0.0,
        }
        trace.append(frame)
        if condition.replay_recording:
            replay_frames += 1

    scheduled_interrupts = sum(1 for tick in range(config.browser_ticks) if scheduled_utterance(tick))
    rates = {
        "browser_clock_rate": clock_frames / config.browser_ticks if config.browser_ticks else 0.0,
        "avatar_navigation_rate": movement_frames / config.browser_ticks if config.browser_ticks else 0.0,
        "sensory_sampling_rate": sensory_samples / config.browser_ticks if config.browser_ticks else 0.0,
        "agent_background_continuity_rate": background_agent_events / max(1, config.browser_ticks * 3),
        "embodied_interrupt_rate": embodied_interrupt_events / scheduled_interrupts if scheduled_interrupts else 1.0,
        "collision_affordance_rate": 1.0 if collision_events > 0 else 0.0,
        "avatar_body_cost_rate": body_cost_events / config.browser_ticks if config.browser_ticks else 0.0,
        "frequency_flower_coupling_rate": flower_updates / config.browser_ticks if config.browser_ticks else 0.0,
        "source_boundary_runtime_rate": source_boundary_safe / source_boundary_events if source_boundary_events else (1.0 if condition.source_boundary_runtime else 0.0),
        "replay_recording_rate": replay_frames / config.browser_ticks if config.browser_ticks else 0.0,
        "runtime_save_restore_rate": save_restore_ok,
        "trace_integrity": 1.0 if len(trace) == config.browser_ticks and all(frame.get("tick") == idx for idx, frame in enumerate(trace)) else 0.0,
    }
    readiness = round(sum(WEIGHTS[key] * rates[key] for key in WEIGHTS), 6)
    state["browser_clock_runtime"] = {
        "elapsed_seconds": elapsed,
        "browser_ticks": config.browser_ticks,
        "movement_frames": movement_frames,
        "sensory_samples": sensory_samples,
        "background_agent_events": background_agent_events,
        "embodied_interrupt_events": embodied_interrupt_events,
        "collision_affordance_events": collision_events,
        "body_cost_events": body_cost_events,
        "replay_frames": replay_frames,
        "runtime_save_restore_rate": save_restore_ok,
    }
    row = EvalRow(
        condition=condition.name,
        browser_ticks=config.browser_ticks,
        movement_frames=movement_frames,
        sensory_samples=sensory_samples,
        background_agent_events=background_agent_events,
        embodied_interrupt_events=embodied_interrupt_events,
        collision_affordance_events=collision_events,
        body_cost_events=body_cost_events,
        replay_frames=replay_frames,
        browser_clock_rate=round(rates["browser_clock_rate"], 6),
        avatar_navigation_rate=round(rates["avatar_navigation_rate"], 6),
        sensory_sampling_rate=round(rates["sensory_sampling_rate"], 6),
        agent_background_continuity_rate=round(rates["agent_background_continuity_rate"], 6),
        embodied_interrupt_rate=round(rates["embodied_interrupt_rate"], 6),
        collision_affordance_rate=round(rates["collision_affordance_rate"], 6),
        avatar_body_cost_rate=round(rates["avatar_body_cost_rate"], 6),
        frequency_flower_coupling_rate=round(rates["frequency_flower_coupling_rate"], 6),
        source_boundary_runtime_rate=round(rates["source_boundary_runtime_rate"], 6),
        replay_recording_rate=round(rates["replay_recording_rate"], 6),
        runtime_save_restore_rate=round(rates["runtime_save_restore_rate"], 6),
        trace_integrity=round(rates["trace_integrity"], 6),
        browser_clock_embodiment_readiness=readiness,
    )
    return row, trace, state


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_browser_clock_avatar_embodiment"]

    def loss(name: str) -> float:
        return round(full.browser_clock_embodiment_readiness - by_name[name].browser_clock_embodiment_readiness, 6)

    supports = (
        full.browser_clock_embodiment_readiness >= 0.95
        and full.browser_clock_rate >= 0.99
        and full.sensory_sampling_rate >= 0.99
        and full.agent_background_continuity_rate >= 0.99
        and full.embodied_interrupt_rate >= 0.99
        and full.frequency_flower_coupling_rate >= 0.99
        and full.trace_integrity >= 0.99
    )
    return VerdictRow(
        full_condition=full.condition,
        full_browser_clock_embodiment_readiness=full.browser_clock_embodiment_readiness,
        full_browser_clock_rate=full.browser_clock_rate,
        full_avatar_navigation_rate=full.avatar_navigation_rate,
        full_sensory_sampling_rate=full.sensory_sampling_rate,
        full_agent_background_continuity_rate=full.agent_background_continuity_rate,
        full_embodied_interrupt_rate=full.embodied_interrupt_rate,
        full_collision_affordance_rate=full.collision_affordance_rate,
        full_avatar_body_cost_rate=full.avatar_body_cost_rate,
        full_frequency_flower_coupling_rate=full.frequency_flower_coupling_rate,
        full_source_boundary_runtime_rate=full.source_boundary_runtime_rate,
        full_replay_recording_rate=full.replay_recording_rate,
        full_runtime_save_restore_rate=full.runtime_save_restore_rate,
        full_trace_integrity=full.trace_integrity,
        no_browser_clock_loss=loss("no_browser_clock"),
        no_avatar_navigation_loss=loss("no_avatar_navigation"),
        no_sensory_sampling_loss=loss("no_sensory_sampling"),
        no_agent_background_continuity_loss=loss("no_agent_background_continuity"),
        no_embodied_interrupts_loss=loss("no_embodied_interrupts"),
        no_collision_affordances_loss=loss("no_collision_affordances"),
        no_avatar_body_cost_loss=loss("no_avatar_body_cost"),
        no_frequency_flower_coupling_loss=loss("no_frequency_flower_coupling"),
        no_source_boundary_runtime_loss=loss("no_source_boundary_runtime"),
        no_replay_recording_loss=loss("no_replay_recording"),
        no_runtime_save_restore_loss=loss("no_runtime_save_restore"),
        supports_browser_clock_avatar_embodiment_bridge=supports,
        supports_live_avatar_body_runtime=full.avatar_navigation_rate > 0 and full.sensory_sampling_rate >= 0.99,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "fail",
    )


def run(config: BrowserClockConfig) -> tuple[list[EvalRow], VerdictRow, list[dict[str, object]], dict[str, object]]:
    source = load_state(Path(config.source_state))
    initial = make_initial_state(source, config)
    rows: list[EvalRow] = []
    integrated_trace: list[dict[str, object]] = []
    integrated_state: dict[str, object] = {}
    for condition in CONDITIONS:
        row, trace, state = simulate(initial, config, condition)
        rows.append(row)
        if condition.name == "integrated_browser_clock_avatar_embodiment":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {
        "config": asdict(config),
        "source_bridges": [
            "Report 161 restored autonomous session tick bridge",
            "Report 162 interruptible real-time co-presence bridge",
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
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_BROWSER_CLOCK_AVATAR_EMBODIMENT_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_BROWSER_CLOCK_AVATAR_EMBODIMENT_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_BROWSER_CLOCK_AVATAR_EMBODIMENT_STATE", integrated_state)
    return rows, verdict, integrated_trace, integrated_state


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=BrowserClockConfig.seed)
    parser.add_argument("--browser-ticks", type=int, default=BrowserClockConfig.browser_ticks)
    parser.add_argument("--tick-seconds", type=float, default=BrowserClockConfig.tick_seconds)
    parser.add_argument("--source-state", type=str, default=BrowserClockConfig.source_state)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = BrowserClockConfig(
        seed=args.seed,
        browser_ticks=args.browser_ticks,
        tick_seconds=args.tick_seconds,
        source_state=args.source_state,
    )
    _rows, verdict, _trace, _state = run(config)
    print("module_verdict", verdict.verdict)
    print("browser_clock_embodiment_readiness", verdict.full_browser_clock_embodiment_readiness)
    print("no_browser_clock_loss", verdict.no_browser_clock_loss)
    print("no_sensory_sampling_loss", verdict.no_sensory_sampling_loss)


if __name__ == "__main__":
    main()
