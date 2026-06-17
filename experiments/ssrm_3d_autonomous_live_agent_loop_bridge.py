#!/usr/bin/env python3
"""Autonomous live-agent loop bridge for SSRM-3D avatar-entry packets.

This remains a deterministic bridge. It does not call LLMs and does not claim
subjective consciousness. It moves past Report 144's scripted benchmark rows by
running mature agents in an autonomous multi-rate loop: agents perceive world
pressure, update internal workspace state, select actions, affect each other,
respond to sparse avatar interrupts, change the world, and leave replay traces.
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
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_embodied_avatar_input_bridge_state.json"
PREFIX = "ssrm_3d_autonomous_live_agent_loop_bridge"
FLOWER_PHASES = (0.0, math.tau / 6.0, math.tau / 3.0, math.tau / 2.0, math.tau * 2.0 / 3.0, math.tau * 5.0 / 6.0, math.tau)

SENSES = ("visual", "audio", "olfactory", "thermal", "wetness", "pain", "affect", "vestibular")
ACTIONS = (
    "forage_water",
    "repair_tool",
    "warm_shelter",
    "route_scout",
    "watch_weather",
    "comfort_neighbor",
    "teach_token",
    "clean_camp",
    "rest_body",
)

ROLE_BIAS = {
    "scout": ("route_scout", "watch_weather"),
    "builder": ("repair_tool", "warm_shelter"),
    "healer": ("comfort_neighbor", "clean_camp"),
    "farmer": ("forage_water", "clean_camp"),
    "guard": ("watch_weather", "route_scout"),
    "teacher": ("teach_token", "comfort_neighbor"),
    "trader": ("forage_water", "route_scout"),
    "pattern_keeper": ("teach_token", "watch_weather"),
}

ACTION_FOCUS = {
    "forage_water": "shared-resource",
    "repair_tool": "tool-or-route",
    "warm_shelter": "care-or-kinship",
    "route_scout": "tool-or-route",
    "watch_weather": "danger-or-weather-memory",
    "comfort_neighbor": "care-or-kinship",
    "teach_token": "shared-resource",
    "clean_camp": "care-or-kinship",
    "rest_body": "care-or-kinship",
}

ACTION_SENSE = {
    "forage_water": "wetness",
    "repair_tool": "thermal",
    "warm_shelter": "thermal",
    "route_scout": "vestibular",
    "watch_weather": "olfactory",
    "comfort_neighbor": "affect",
    "teach_token": "audio",
    "clean_camp": "pain",
    "rest_body": "pain",
}

PLAYER_INTERRUPTS = {
    18: "avatar asks who needs water before the cold rain",
    42: "avatar asks whether the old route is safe",
    66: "avatar promises to return the borrowed tool",
    90: "avatar asks what warning token belongs near the shelter",
}


@dataclass(frozen=True)
class LiveLoopConfig:
    seed: int = 20260619
    ticks: int = 96
    source_agents: str = str(SOURCE_AGENTS)
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    autonomous_scheduler: bool
    internal_workspace: bool
    sensory_bus: bool
    social_exchange: bool
    world_consequences: bool
    player_interrupts: bool
    persistent_trace: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    ticks: int
    autonomous_actions: int
    player_interrupts: int
    autonomous_action_rate: float
    perception_update_rate: float
    workspace_tick_rate: float
    social_exchange_rate: float
    world_state_update_rate: float
    player_interrupt_response_rate: float
    multi_rate_synchrony: float
    world_homeostasis_score: float
    trace_completeness: float
    autonomous_live_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_autonomous_live_readiness: float
    full_autonomous_action_rate: float
    full_perception_update_rate: float
    full_workspace_tick_rate: float
    full_social_exchange_rate: float
    full_world_state_update_rate: float
    full_player_interrupt_response_rate: float
    full_multi_rate_synchrony: float
    full_world_homeostasis_score: float
    full_trace_completeness: float
    no_autonomous_scheduler_loss: float
    no_internal_workspace_loss: float
    no_sensory_bus_loss: float
    no_social_exchange_loss: float
    no_world_consequences_loss: float
    no_player_interrupts_loss: float
    no_persistent_trace_loss: float
    supports_autonomous_live_agent_loop_bridge: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_autonomous_live_loop", True, True, True, True, True, True, True),
    Condition("no_autonomous_scheduler", False, True, True, True, True, True, True),
    Condition("no_internal_workspace", True, False, True, True, True, True, True),
    Condition("no_sensory_bus", True, True, False, True, True, True, True),
    Condition("no_social_exchange", True, True, True, False, True, True, True),
    Condition("no_world_consequences", True, True, True, True, False, True, True),
    Condition("no_player_interrupts", True, True, True, True, True, False, True),
    Condition("no_persistent_trace", True, True, True, True, True, True, False),
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
    if not isinstance(state, dict) or "agents" not in state or "world" not in state:
        raise ValueError(f"Report 144 state artifact is invalid: {path}")
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


def packet_position(packet: dict[str, object], index: int) -> dict[str, float]:
    pos = packet.get("position", {})
    if isinstance(pos, dict) and "x" in pos and "z" in pos:
        return {"x": float(pos["x"]), "z": float(pos["z"])}
    angle = index / 8.0 * math.tau
    return {"x": math.cos(angle) * 8.0, "z": math.sin(angle) * 8.0}


def build_initial_state(source_agents: Sequence[dict[str, object]], source_state: dict[str, object]) -> tuple[dict[str, dict[str, object]], dict[str, float]]:
    prior_agents = source_state.get("agents", {})
    if not isinstance(prior_agents, dict):
        prior_agents = {}
    agents: dict[str, dict[str, object]] = {}
    for index, packet in enumerate(source_agents):
        agent_id = str(packet["agent_id"])
        prior = copy.deepcopy(prior_agents.get(agent_id, {}))
        workspace = packet.get("internal_workspace", {})
        affect = workspace.get("affect", {}) if isinstance(workspace, dict) else {}
        if not prior:
            prior = {
                "agent_id": agent_id,
                "name": packet.get("name", agent_id),
                "role": packet.get("role", "agent"),
                "trust": 0.46 + float(affect.get("attachment", 0.4)) * 0.22,
                "attention": workspace.get("attention", "shared-field") if isinstance(workspace, dict) else "shared-field",
                "motive": workspace.get("motive", "wait") if isinstance(workspace, dict) else "wait",
                "body_state": float(workspace.get("body_state", 0.55)) if isinstance(workspace, dict) else 0.55,
                "fear": float(affect.get("fear", 0.35)),
                "attachment": float(affect.get("attachment", 0.45)),
                "curiosity": float(affect.get("curiosity", 0.35)),
            }
        prior["position"] = packet_position(packet, index)
        prior["fatigue"] = 0.18 + (index % 4) * 0.035
        prior["pain"] = 0.08 + (index % 3) * 0.025
        prior["wetness"] = 0.14 + (index % 5) * 0.018
        prior["thermal_comfort"] = 0.62 - (index % 4) * 0.020
        prior["workspace_ticks"] = 0
        prior["autonomous_actions"] = 0
        prior["social_exchanges"] = 0
        prior["player_responses"] = 0
        prior["live_memory"] = []
        agents[agent_id] = prior
    old_world = source_state.get("world", {})
    if not isinstance(old_world, dict):
        old_world = {}
    defaults = {
        "shared_water": 0.58,
        "tool_integrity": 0.60,
        "shelter_warmth": 0.56,
        "route_confidence": 0.58,
        "council_acceptance": 0.55,
        "danger_memory": 0.58,
        "food_cache": 0.52,
        "waste_control": 0.50,
        "fire_heat": 0.54,
        "language_coherence": 0.60,
        "trace_integrity": 0.20,
    }
    caps = {
        "shared_water": 0.66,
        "tool_integrity": 0.68,
        "shelter_warmth": 0.64,
        "route_confidence": 0.66,
        "council_acceptance": 0.64,
        "danger_memory": 0.66,
        "food_cache": 0.62,
        "waste_control": 0.62,
        "fire_heat": 0.62,
        "language_coherence": 0.68,
        "trace_integrity": 0.20,
    }
    world = {key: clamp(min(float(old_world.get(key, fallback)), caps[key])) for key, fallback in defaults.items()}
    world["weather_cold"] = 0.32
    world["rain_wetness"] = 0.28
    world["threat_scent"] = 0.22
    world["flower_phase"] = 0.0
    return agents, world


def sensory_wave(packet: dict[str, object], sense: str, tick: int, index: int, enabled: bool) -> float:
    if not enabled:
        return 0.20
    rates = packet.get("sensory_rates_hz", {})
    rate = float(rates.get(sense, 1.0)) if isinstance(rates, dict) else 1.0
    phase = FLOWER_PHASES[(tick + index) % len(FLOWER_PHASES)]
    return clamp(0.34 + (0.5 + 0.5 * math.sin(rate * 0.23 + tick * 0.19 + phase)) * 0.58)


def scheduler_due(packet: dict[str, object], tick: int, index: int, condition: Condition) -> bool:
    if not condition.autonomous_scheduler:
        return False
    rates = packet.get("sensory_rates_hz", {})
    audio = float(rates.get("audio", 4.0)) if isinstance(rates, dict) else 4.0
    interval = 1 + ((index + int(audio)) % 3)
    return (tick + index) % interval == 0


def degrade_world(world: dict[str, float], tick: int) -> None:
    phase = 0.5 + 0.5 * math.sin(tick * 0.11)
    world["flower_phase"] = round(phase, 6)
    world["weather_cold"] = clamp(0.28 + phase * 0.18)
    world["rain_wetness"] = clamp(0.22 + (1.0 - phase) * 0.20)
    world["threat_scent"] = clamp(world.get("threat_scent", 0.22) + 0.002 * math.sin(tick * 0.31))
    for key, amount in (
        ("shared_water", 0.0018),
        ("food_cache", 0.0015),
        ("tool_integrity", 0.0016),
        ("shelter_warmth", 0.0019 + world["weather_cold"] * 0.0012),
        ("fire_heat", 0.0020),
        ("route_confidence", 0.0013),
        ("council_acceptance", 0.0009),
        ("danger_memory", 0.0011),
        ("waste_control", 0.0014),
        ("language_coherence", 0.0008),
    ):
        world[key] = clamp(world.get(key, 0.5) - amount)


def perceive(world: dict[str, float], live: dict[str, object], packet: dict[str, object], tick: int, index: int, condition: Condition) -> dict[str, float]:
    sensory = {sense: sensory_wave(packet, sense, tick, index, condition.sensory_bus) for sense in SENSES}
    pressure = {
        "water": clamp(1.0 - world["shared_water"] + sensory["wetness"] * 0.08),
        "food": clamp(1.0 - world["food_cache"] + float(live.get("fatigue", 0.2)) * 0.10),
        "tool": clamp(1.0 - world["tool_integrity"] + float(live.get("pain", 0.1)) * 0.08),
        "shelter": clamp(1.0 - world["shelter_warmth"] + world["weather_cold"] * 0.25 + sensory["thermal"] * 0.05),
        "route": clamp(1.0 - world["route_confidence"] + sensory["vestibular"] * 0.05),
        "danger": clamp(1.0 - world["danger_memory"] + world["threat_scent"] * 0.35 + sensory["olfactory"] * 0.07),
        "social": clamp(1.0 - world["council_acceptance"] + sensory["affect"] * 0.05),
        "language": clamp(1.0 - world["language_coherence"] + sensory["audio"] * 0.04),
        "sanitation": clamp(1.0 - world["waste_control"] + sensory["pain"] * 0.04),
        "body": clamp(float(live.get("fatigue", 0.2)) + float(live.get("pain", 0.1)) + world["rain_wetness"] * 0.12),
    }
    return {**pressure, **{f"sense_{key}": value for key, value in sensory.items()}}


def choose_action(live: dict[str, object], perception: dict[str, float], tick: int, condition: Condition) -> str:
    role = str(live.get("role", "agent"))
    if not condition.internal_workspace:
        fallback = ROLE_BIAS.get(role, ("forage_water", "rest_body"))
        return fallback[tick % len(fallback)]
    scores = {
        "forage_water": perception["water"] * 0.75 + perception["food"] * 0.35,
        "repair_tool": perception["tool"] * 0.85 + perception["shelter"] * 0.25,
        "warm_shelter": perception["shelter"] * 0.85 + perception["body"] * 0.20,
        "route_scout": perception["route"] * 0.78 + perception["danger"] * 0.18,
        "watch_weather": perception["danger"] * 0.72 + perception["shelter"] * 0.26,
        "comfort_neighbor": perception["social"] * 0.62 + perception["body"] * 0.22,
        "teach_token": perception["language"] * 0.80 + perception["social"] * 0.18,
        "clean_camp": perception["sanitation"] * 0.82 + perception["body"] * 0.14,
        "rest_body": perception["body"] * 0.76 + float(live.get("fatigue", 0.2)) * 0.25,
    }
    for action in ROLE_BIAS.get(role, ()):
        scores[action] += 0.16
    if tick % 17 == 0:
        scores["teach_token"] += 0.08
    if tick % 19 == 0:
        scores["watch_weather"] += 0.07
    return max(scores.items(), key=lambda item: (item[1], item[0]))[0]


def apply_agent_update(live: dict[str, object], action: str, perception: dict[str, float], condition: Condition) -> None:
    if condition.internal_workspace:
        live["attention"] = ACTION_FOCUS[action]
        live["motive"] = action
        live["workspace_ticks"] = int(live.get("workspace_ticks", 0)) + 1
    fatigue = float(live.get("fatigue", 0.2))
    pain = float(live.get("pain", 0.1))
    if action == "rest_body":
        live["fatigue"] = clamp(fatigue - 0.060)
        live["pain"] = clamp(pain - 0.020)
        live["body_state"] = clamp(float(live.get("body_state", 0.6)) + 0.018)
    else:
        live["fatigue"] = clamp(fatigue + 0.012 + perception.get("body", 0.2) * 0.004)
        live["pain"] = clamp(pain + (0.004 if action in {"repair_tool", "route_scout"} else -0.003))
        live["body_state"] = clamp(float(live.get("body_state", 0.6)) + 0.004 - live["fatigue"] * 0.004)
    live["fear"] = clamp(float(live.get("fear", 0.25)) + perception.get("danger", 0.3) * 0.006 - (0.018 if action in {"watch_weather", "comfort_neighbor"} else 0.005))
    live["curiosity"] = clamp(float(live.get("curiosity", 0.5)) + (0.009 if action in {"teach_token", "route_scout", "watch_weather"} else 0.002))
    live["autonomous_actions"] = int(live.get("autonomous_actions", 0)) + 1


def apply_world_action(world: dict[str, float], action: str, strength: float, enabled: bool) -> float:
    if not enabled:
        return 0.0
    before = dict(world)
    if action == "forage_water":
        world["shared_water"] = clamp(world["shared_water"] + strength * 0.030)
        world["food_cache"] = clamp(world["food_cache"] + strength * 0.020)
    elif action == "repair_tool":
        world["tool_integrity"] = clamp(world["tool_integrity"] + strength * 0.035)
        world["shelter_warmth"] = clamp(world["shelter_warmth"] + strength * 0.012)
    elif action == "warm_shelter":
        world["shelter_warmth"] = clamp(world["shelter_warmth"] + strength * 0.030)
        world["fire_heat"] = clamp(world["fire_heat"] + strength * 0.026)
    elif action == "route_scout":
        world["route_confidence"] = clamp(world["route_confidence"] + strength * 0.034)
        world["danger_memory"] = clamp(world["danger_memory"] + strength * 0.010)
    elif action == "watch_weather":
        world["danger_memory"] = clamp(world["danger_memory"] + strength * 0.036)
        world["threat_scent"] = clamp(world["threat_scent"] - strength * 0.010)
    elif action == "comfort_neighbor":
        world["council_acceptance"] = clamp(world["council_acceptance"] + strength * 0.030)
    elif action == "teach_token":
        world["language_coherence"] = clamp(world["language_coherence"] + strength * 0.034)
        world["council_acceptance"] = clamp(world["council_acceptance"] + strength * 0.010)
    elif action == "clean_camp":
        world["waste_control"] = clamp(world["waste_control"] + strength * 0.035)
        world["council_acceptance"] = clamp(world["council_acceptance"] + strength * 0.006)
    elif action == "rest_body":
        world["council_acceptance"] = clamp(world["council_acceptance"] + strength * 0.004)
    world["trace_integrity"] = clamp(world.get("trace_integrity", 0.0) + 0.006)
    return mean(abs(world[key] - before.get(key, 0.0)) for key in before)


def social_exchange(live: dict[str, object], partner: dict[str, object], action: str, token: str, condition: Condition) -> bool:
    if not condition.social_exchange or action not in {"comfort_neighbor", "teach_token", "forage_water", "repair_tool", "watch_weather"}:
        return False
    live["trust"] = clamp(float(live.get("trust", 0.5)) + 0.010)
    partner["trust"] = clamp(float(partner.get("trust", 0.5)) + 0.012)
    partner["attention"] = ACTION_FOCUS[action]
    partner["motive"] = f"heard-{action}"
    partner["social_exchanges"] = int(partner.get("social_exchanges", 0)) + 1
    live["social_exchanges"] = int(live.get("social_exchanges", 0)) + 1
    memory = partner.setdefault("live_memory", [])
    if isinstance(memory, list):
        memory.append({"kind": "social", "token": token, "from": live.get("name", "agent"), "action": action})
    return True


def handle_player_interrupt(tick: int, agents: dict[str, dict[str, object]], source_agents: Sequence[dict[str, object]], world: dict[str, float], condition: Condition) -> tuple[bool, dict[str, object] | None]:
    if not condition.player_interrupts or tick not in PLAYER_INTERRUPTS:
        return False, None
    index = (tick // 6) % len(source_agents)
    packet = source_agents[index]
    live = agents[str(packet["agent_id"])]
    text = PLAYER_INTERRUPTS[tick]
    if "water" in text:
        action = "forage_water"
    elif "route" in text:
        action = "route_scout"
    elif "tool" in text:
        action = "repair_tool"
    else:
        action = "teach_token"
    focus = ACTION_FOCUS[action]
    token = token_for_focus(packet, focus)
    live["attention"] = focus
    live["motive"] = f"avatar-response-{action}"
    live["trust"] = clamp(float(live.get("trust", 0.5)) + 0.020)
    live["player_responses"] = int(live.get("player_responses", 0)) + 1
    live["workspace_ticks"] = int(live.get("workspace_ticks", 0)) + (1 if condition.internal_workspace else 0)
    memory = live.setdefault("live_memory", [])
    if isinstance(memory, list):
        memory.append({"kind": "player_interrupt", "text": text, "token": token, "action": action, "tick": tick})
    if condition.world_consequences:
        apply_world_action(world, action, 0.55, True)
    return True, {
        "tick": tick,
        "event": "player_interrupt",
        "player_text": text,
        "agent_id": live["agent_id"],
        "agent_name": live.get("name", live["agent_id"]),
        "action": action,
        "focus": focus,
        "native_token": token,
        "response": f"{live.get('name', live['agent_id'])} answers with {token} and starts {action}.",
    }


def run_condition(cfg: LiveLoopConfig, condition: Condition, source_agents: Sequence[dict[str, object]], source_state: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    agents, world = build_initial_state(source_agents, source_state)
    trace: list[dict[str, object]] = []
    autonomous_actions = 0
    perception_updates = 0
    workspace_updates = 0
    social_events = 0
    world_updates = 0
    interrupt_count = 0
    interrupt_responses = 0
    senses_seen: set[str] = set()
    actions_seen: set[str] = set()
    possible = cfg.ticks * len(source_agents)

    for tick in range(1, cfg.ticks + 1):
        degrade_world(world, tick)
        responded, interrupt_row = handle_player_interrupt(tick, agents, source_agents, world, condition)
        if tick in PLAYER_INTERRUPTS and condition.player_interrupts:
            interrupt_count += 1
        if responded:
            interrupt_responses += 1
            if condition.persistent_trace and interrupt_row is not None:
                trace.append(interrupt_row)
        for index, packet in enumerate(source_agents):
            if not scheduler_due(packet, tick, index, condition):
                continue
            agent_id = str(packet["agent_id"])
            live = agents[agent_id]
            perception = perceive(world, live, packet, tick, index, condition)
            perception_updates += 1 if condition.sensory_bus else 0
            action = choose_action(live, perception, tick, condition)
            sense = ACTION_SENSE[action]
            senses_seen.add(sense if condition.sensory_bus else "flat")
            actions_seen.add(action)
            strength = sensory_wave(packet, sense, tick, index, condition.sensory_bus)
            before_workspace = int(live.get("workspace_ticks", 0))
            apply_agent_update(live, action, perception, condition)
            workspace_updates += max(0, int(live.get("workspace_ticks", 0)) - before_workspace)
            world_delta = apply_world_action(world, action, strength, condition.world_consequences)
            if world_delta > 0.00005:
                world_updates += 1
            partner_index = (index + 1 + tick % (len(source_agents) - 1)) % len(source_agents)
            partner = agents[str(source_agents[partner_index]["agent_id"])]
            focus = ACTION_FOCUS[action]
            token = token_for_focus(packet, focus)
            social = social_exchange(live, partner, action, token, condition)
            social_events += 1 if social else 0
            autonomous_actions += 1
            memory = live.setdefault("live_memory", [])
            if isinstance(memory, list):
                memory.append({"kind": "autonomous_tick", "tick": tick, "action": action, "focus": focus, "token": token})
            if condition.persistent_trace:
                trace.append({
                    "tick": tick,
                    "event": "autonomous_action",
                    "agent_id": agent_id,
                    "agent_name": live.get("name", agent_id),
                    "role": live.get("role", "agent"),
                    "action": action,
                    "focus": focus,
                    "native_token": token,
                    "sense": sense,
                    "sensory_strength": round(strength, 6),
                    "attention": live.get("attention", "none"),
                    "motive": live.get("motive", "none"),
                    "world_delta": round(world_delta, 6),
                    "social_exchange": social,
                    "world_snapshot": {key: round(world[key], 6) for key in ("shared_water", "tool_integrity", "shelter_warmth", "route_confidence", "council_acceptance", "danger_memory", "language_coherence")},
                })

    autonomous_action_rate = autonomous_actions / possible
    perception_update_rate = perception_updates / max(1, autonomous_actions)
    workspace_tick_rate = workspace_updates / max(1, autonomous_actions + interrupt_responses)
    social_exchange_rate = social_events / max(1, autonomous_actions)
    world_state_update_rate = world_updates / max(1, autonomous_actions)
    player_interrupt_response_rate = interrupt_responses / max(1, interrupt_count if condition.player_interrupts else len(PLAYER_INTERRUPTS))
    multi_rate_synchrony = clamp((len(senses_seen) / len(SENSES)) * 0.50 + (len(actions_seen) / len(ACTIONS)) * 0.50)
    homeostasis_keys = ("shared_water", "tool_integrity", "shelter_warmth", "route_confidence", "council_acceptance", "danger_memory", "food_cache", "waste_control", "fire_heat", "language_coherence")
    world_homeostasis_score = mean(world[key] for key in homeostasis_keys)
    trace_completeness = 1.0 if condition.persistent_trace and len(trace) >= autonomous_actions + interrupt_responses else 0.0
    readiness = (
        autonomous_action_rate * 0.14
        + perception_update_rate * 0.12
        + workspace_tick_rate * 0.14
        + social_exchange_rate * 0.10
        + world_state_update_rate * 0.13
        + player_interrupt_response_rate * 0.12
        + multi_rate_synchrony * 0.10
        + world_homeostasis_score * 0.08
        + trace_completeness * 0.07
    )
    row = EvalRow(
        condition=condition.name,
        ticks=cfg.ticks,
        autonomous_actions=autonomous_actions,
        player_interrupts=interrupt_count,
        autonomous_action_rate=round(autonomous_action_rate, 6),
        perception_update_rate=round(perception_update_rate, 6),
        workspace_tick_rate=round(workspace_tick_rate, 6),
        social_exchange_rate=round(social_exchange_rate, 6),
        world_state_update_rate=round(world_state_update_rate, 6),
        player_interrupt_response_rate=round(player_interrupt_response_rate, 6),
        multi_rate_synchrony=round(multi_rate_synchrony, 6),
        world_homeostasis_score=round(world_homeostasis_score, 6),
        trace_completeness=round(trace_completeness, 6),
        autonomous_live_readiness=round(readiness, 6),
    )
    state = {
        "condition": condition.name,
        "ticks": cfg.ticks,
        "world": {key: round(value, 6) for key, value in world.items()},
        "agents": agents,
    }
    return row, trace, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_autonomous_live_loop"]

    def loss(condition: str) -> float:
        return round(full.autonomous_live_readiness - by_name[condition].autonomous_live_readiness, 6)

    supports = (
        full.autonomous_live_readiness >= 0.70
        and full.autonomous_action_rate >= 0.35
        and full.perception_update_rate >= 0.95
        and full.workspace_tick_rate >= 0.80
        and full.world_state_update_rate >= 0.70
        and full.player_interrupt_response_rate >= 0.95
        and full.multi_rate_synchrony >= 0.75
        and full.trace_completeness >= 1.0
        and loss("no_autonomous_scheduler") >= 0.20
        and loss("no_internal_workspace") >= 0.08
        and loss("no_world_consequences") >= 0.08
        and loss("no_player_interrupts") >= 0.08
        and loss("no_persistent_trace") >= 0.05
    )
    return VerdictRow(
        full_condition=full.condition,
        full_autonomous_live_readiness=full.autonomous_live_readiness,
        full_autonomous_action_rate=full.autonomous_action_rate,
        full_perception_update_rate=full.perception_update_rate,
        full_workspace_tick_rate=full.workspace_tick_rate,
        full_social_exchange_rate=full.social_exchange_rate,
        full_world_state_update_rate=full.world_state_update_rate,
        full_player_interrupt_response_rate=full.player_interrupt_response_rate,
        full_multi_rate_synchrony=full.multi_rate_synchrony,
        full_world_homeostasis_score=full.world_homeostasis_score,
        full_trace_completeness=full.trace_completeness,
        no_autonomous_scheduler_loss=loss("no_autonomous_scheduler"),
        no_internal_workspace_loss=loss("no_internal_workspace"),
        no_sensory_bus_loss=loss("no_sensory_bus"),
        no_social_exchange_loss=loss("no_social_exchange"),
        no_world_consequences_loss=loss("no_world_consequences"),
        no_player_interrupts_loss=loss("no_player_interrupts"),
        no_persistent_trace_loss=loss("no_persistent_trace"),
        supports_autonomous_live_agent_loop_bridge=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "partial_or_failed",
    )


def run_benchmark(cfg: LiveLoopConfig) -> dict[str, object]:
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
        "report": 145,
        "name": "SSRM-3D Autonomous Live Agent Loop Bridge",
        "config": asdict(cfg),
        "eval": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "trace": traces["integrated_autonomous_live_loop"],
        "final_state": states["integrated_autonomous_live_loop"],
        "source_agents": source_agents,
        "notes": {
            "claim": "deterministic bridge from typed avatar input to autonomous multi-agent live ticking",
            "not_claimed": "subjective consciousness, LLM open dialogue, complete playable world, or unscripted civilization emergence",
            "loop_basis": "multi-rate scheduler, sensory pressure, internal workspace ticks, autonomous actions, social exchanges, sparse player interrupts, world consequences, and replay traces",
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", payload)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", payload["trace"])
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", payload["final_state"])
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_AUTONOMOUS_LIVE_AGENT_LOOP_BRIDGE_RESULTS", payload)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_AUTONOMOUS_LIVE_AGENT_LOOP_BRIDGE_TRACE", payload["trace"])
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_AUTONOMOUS_LIVE_AGENT_LOOP_BRIDGE_STATE", payload["final_state"])
    return payload


def parse_args() -> LiveLoopConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260619)
    parser.add_argument("--ticks", type=int, default=96)
    parser.add_argument("--source-agents", default=str(SOURCE_AGENTS))
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    if args.ticks < 48:
        raise SystemExit("--ticks must be at least 48")
    return LiveLoopConfig(seed=args.seed, ticks=args.ticks, source_agents=args.source_agents, source_state=args.source_state)


def main() -> None:
    payload = run_benchmark(parse_args())
    print(json.dumps(payload["verdict"], indent=2))


if __name__ == "__main__":
    main()
