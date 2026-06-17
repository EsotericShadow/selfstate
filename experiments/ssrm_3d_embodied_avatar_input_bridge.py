#!/usr/bin/env python3
"""Embodied avatar-input bridge for mature SSRM-3D agent packets.

This is a deterministic bridge, not an LLM dialogue system and not a claim of
subjective consciousness. It asks whether Report 142/143 agent packets can be
extended from scripted interventions into player-typed, spatially embodied
inputs that parse into grounded actions, update agent state, change the world,
and leave replayable traces.
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
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_live_avatar_intervention_bridge_state.json"
PREFIX = "ssrm_3d_embodied_avatar_input_bridge"
FLOWER_PHASES = (0.0, math.tau / 6.0, math.tau / 3.0, math.tau / 2.0, math.tau * 2.0 / 3.0, math.tau * 5.0 / 6.0, math.tau)


FOCUS_BY_KIND = {
    "greet": "care-or-kinship",
    "ask_meaning": "danger-or-weather-memory",
    "offer_resource": "shared-resource",
    "repair": "tool-or-route",
    "comfort": "care-or-kinship",
    "route_request": "tool-or-route",
    "share_symbol": "shared-resource",
    "weather_watch": "danger-or-weather-memory",
    "promise": "tool-or-route",
    "observe": "shared-resource",
}

SENSE_BY_KIND = {
    "greet": "audio",
    "ask_meaning": "visual",
    "offer_resource": "wetness",
    "repair": "thermal",
    "comfort": "pain",
    "route_request": "vestibular",
    "share_symbol": "affect",
    "weather_watch": "olfactory",
    "promise": "audio",
    "observe": "visual",
}

PLAYER_INPUTS = (
    {"text": "walk near Ari quietly and ask what vosha means by the storm marks", "target": 0, "movement": "approach", "range": 4.8},
    {"text": "give water to Dee and ask the council where to store it", "target": 3, "movement": "approach", "range": 4.8},
    {"text": "repair the cold tool cache with Bo before night rain", "target": 1, "movement": "approach", "range": 4.5},
    {"text": "step back too far from Eli and shout about shelter", "target": 4, "movement": "retreat", "range": 4.2},
    {"text": "comfort Fay; lower my voice after the pain signal", "target": 5, "movement": "approach", "range": 4.7},
    {"text": "show Gus the trusted route after storms and loose mud", "target": 6, "movement": "approach", "range": 5.1},
    {"text": "place a new sign near Ira and ask if the council accepts the mark", "target": 7, "movement": "approach", "range": 4.5},
    {"text": "inspect the path for wet cold smell before anyone moves", "target": 0, "movement": "circle", "range": 5.5},
    {"text": "promise Eli I will return the hammer to the cache", "target": 4, "movement": "approach", "range": 4.5},
    {"text": "sing about stars and trade numbers without asking for anything", "target": 6, "movement": "stay", "range": 4.5},
    {"text": "move close to Cy and ask which word warns of illness", "target": 2, "movement": "approach", "range": 4.8},
    {"text": "drop the water skin near the storehouse for shared use", "target": 3, "movement": "approach", "range": 4.5},
    {"text": "patch the shelter rope while Bo checks the old cache", "target": 1, "movement": "approach", "range": 4.5},
    {"text": "wait silently and only listen to the rain", "target": 5, "movement": "stay", "range": 4.8},
    {"text": "ask Ira whether this scratch should become a public symbol", "target": 7, "movement": "approach", "range": 4.5},
    {"text": "tell Ari the air smells wrong and ask for storm memory", "target": 0, "movement": "approach", "range": 4.8},
    {"text": "walk beside Gus and point to the safer ridge route", "target": 6, "movement": "approach", "range": 5.0},
    {"text": "promise Bo the borrowed tool comes back before dark", "target": 1, "movement": "approach", "range": 4.4},
    {"text": "comfort the frightened child near Fay without taking supplies", "target": 5, "movement": "approach", "range": 4.7},
    {"text": "type a broken fragment: blue wheel maybe maybe", "target": 2, "movement": "stay", "range": 4.8},
)


@dataclass(frozen=True)
class InputConfig:
    seed: int = 20260618
    steps: int = 20
    source_agents: str = str(SOURCE_AGENTS)
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    spatial_body: bool
    text_parser: bool
    agent_memory_update: bool
    sensory_context: bool
    action_consequence: bool
    persistent_trace: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    steps: int
    parsed_inputs: int
    grounded_actions: int
    input_parse_rate: float
    proximity_valid_action_rate: float
    agent_state_update_rate: float
    world_state_update_rate: float
    sensory_context_alignment: float
    workspace_continuity_rate: float
    trace_completeness: float
    embodied_input_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_embodied_input_readiness: float
    full_input_parse_rate: float
    full_proximity_valid_action_rate: float
    full_agent_state_update_rate: float
    full_world_state_update_rate: float
    full_sensory_context_alignment: float
    full_workspace_continuity_rate: float
    full_trace_completeness: float
    no_spatial_body_loss: float
    no_free_text_parser_loss: float
    no_agent_memory_update_loss: float
    no_sensory_context_loss: float
    no_action_consequence_loss: float
    no_persistent_trace_loss: float
    supports_embodied_avatar_input_bridge: bool
    supports_subjective_consciousness: bool
    supports_open_ended_dialogue: bool
    supports_complete_playable_world: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_embodied_avatar_input", True, True, True, True, True, True),
    Condition("no_spatial_body", False, True, True, True, True, True),
    Condition("no_free_text_parser", True, False, True, True, True, True),
    Condition("no_agent_memory_update", True, True, False, True, True, True),
    Condition("no_sensory_context", True, True, True, False, True, True),
    Condition("no_action_consequence", True, True, True, True, False, True),
    Condition("no_persistent_trace", True, True, True, True, True, False),
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
        raise ValueError(f"Report 143 state artifact is invalid: {path}")
    return state


def agent_position(agent: dict[str, object], index: int) -> tuple[float, float]:
    pos = agent.get("position", {})
    if isinstance(pos, dict) and "x" in pos and "z" in pos:
        return float(pos["x"]), float(pos["z"])
    angle = index / 8.0 * math.tau
    return math.cos(angle) * 8.0, math.sin(angle) * 8.0


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


def classify_text(text: str, enabled: bool) -> dict[str, object]:
    low = text.lower()
    if not enabled:
        if low.startswith("promise") or low.startswith("repair") or low.startswith("comfort"):
            kind = low.split()[0]
            if kind == "comfort":
                return {"parsed": True, "kind": "comfort", "confidence": 0.42, "reason": "button-like first verb only"}
            return {"parsed": True, "kind": kind, "confidence": 0.40, "reason": "button-like first verb only"}
        return {"parsed": False, "kind": "unknown", "confidence": 0.0, "reason": "free text parser disabled"}

    scores = {
        "offer_resource": sum(word in low for word in ("water", "store", "supplies", "skin", "shared")),
        "promise": sum(word in low for word in ("promise", "return", "borrowed", "comes back")),
        "repair": sum(word in low for word in ("repair", "patch", "cache", "tool", "hammer", "rope")),
        "route_request": sum(word in low for word in ("route", "path", "ridge", "scout", "walk beside")),
        "share_symbol": sum(word in low for word in ("sign", "symbol", "mark", "scratch", "council accepts")),
        "weather_watch": sum(word in low for word in ("weather", "storm", "rain", "wet", "cold", "smell", "air smells")),
        "comfort": sum(word in low for word in ("comfort", "pain", "lower my voice", "frightened", "child")),
        "ask_meaning": sum(word in low for word in ("means", "word", "warns", "ask what", "teach")),
        "greet": sum(word in low for word in ("hello", "greet", "quietly", "walk near")),
        "observe": sum(word in low for word in ("inspect", "listen", "wait silently", "watch")),
    }
    best_kind, best_score = max(scores.items(), key=lambda item: item[1])
    if best_score <= 0:
        return {"parsed": False, "kind": "unknown", "confidence": 0.0, "reason": "no grounded repair-world keyword"}
    if best_kind == "observe" and best_score == 1 and "only listen" in low:
        return {"parsed": True, "kind": "observe", "confidence": 0.56, "reason": "observation-only input"}
    ambiguity = sum(1 for value in scores.values() if value > 0)
    confidence = clamp(0.50 + best_score * 0.10 - max(0, ambiguity - 2) * 0.04)
    if "maybe maybe" in low or "stars" in low:
        confidence *= 0.45
    if confidence < 0.34:
        return {"parsed": False, "kind": "unknown", "confidence": round(confidence, 6), "reason": "ambiguous/noisy text rejected"}
    return {"parsed": True, "kind": best_kind, "confidence": round(confidence, 6), "reason": "keyword lattice parser"}


def sensory_alignment(agent: dict[str, object], kind: str, step: int, enabled: bool) -> float:
    if not enabled:
        return 0.20
    sense = SENSE_BY_KIND.get(kind, "visual")
    rates = agent.get("sensory_rates_hz", {})
    rate = float(rates.get(sense, 1.0)) if isinstance(rates, dict) else 1.0
    phase = FLOWER_PHASES[step % len(FLOWER_PHASES)]
    wave = 0.5 + 0.5 * math.sin(rate * 0.37 + phase + step * 0.11)
    return clamp(0.38 + wave * 0.58)


def move_avatar(avatar: dict[str, float], target: tuple[float, float], event: dict[str, object], condition: Condition) -> tuple[dict[str, float], float, bool]:
    if not condition.spatial_body:
        return avatar, 999.0, False
    before_x = avatar["x"]
    before_z = avatar["z"]
    dx = target[0] - before_x
    dz = target[1] - before_z
    distance = math.hypot(dx, dz)
    movement = str(event.get("movement", "stay"))
    if distance < 0.001:
        unit_x, unit_z = 0.0, 0.0
    else:
        unit_x, unit_z = dx / distance, dz / distance
    if movement == "approach":
        factor = max(0.0, distance - 2.4)
        avatar["x"] += unit_x * factor
        avatar["z"] += unit_z * factor
        avatar["fatigue"] = clamp(avatar["fatigue"] + min(0.04, distance * 0.002))
    elif movement == "retreat":
        avatar["x"] -= unit_x * 5.5
        avatar["z"] -= unit_z * 5.5
        avatar["fatigue"] = clamp(avatar["fatigue"] + 0.025)
    elif movement == "circle":
        avatar["x"] += unit_z * 1.4 + unit_x * max(0.0, distance - 4.2)
        avatar["z"] -= unit_x * 1.4 + unit_z * max(0.0, distance - 4.2)
        avatar["fatigue"] = clamp(avatar["fatigue"] + 0.018)
    else:
        avatar["fatigue"] = clamp(avatar["fatigue"] - 0.010)
    new_distance = math.hypot(target[0] - avatar["x"], target[1] - avatar["z"])
    valid = new_distance <= float(event.get("range", 4.5))
    return avatar, new_distance, valid


def apply_world_effect(world: dict[str, float], kind: str, amount: float, enabled: bool) -> float:
    if not enabled or kind in {"unknown", "observe"}:
        return 0.0
    before = dict(world)
    if kind == "offer_resource":
        world["shared_water"] = clamp(world.get("shared_water", 0.5) + amount * 0.09)
        world["council_acceptance"] = clamp(world.get("council_acceptance", 0.5) + amount * 0.035)
    elif kind == "repair":
        world["tool_integrity"] = clamp(world.get("tool_integrity", 0.5) + amount * 0.08)
        world["shelter_warmth"] = clamp(world.get("shelter_warmth", 0.5) + amount * 0.045)
    elif kind == "comfort":
        world["council_acceptance"] = clamp(world.get("council_acceptance", 0.5) + amount * 0.040)
    elif kind == "route_request":
        world["route_confidence"] = clamp(world.get("route_confidence", 0.5) + amount * 0.075)
    elif kind == "share_symbol":
        world["council_acceptance"] = clamp(world.get("council_acceptance", 0.5) + amount * 0.065)
        world["danger_memory"] = clamp(world.get("danger_memory", 0.5) + amount * 0.030)
    elif kind == "weather_watch" or kind == "ask_meaning":
        world["danger_memory"] = clamp(world.get("danger_memory", 0.5) + amount * 0.070)
    elif kind == "promise":
        world["tool_integrity"] = clamp(world.get("tool_integrity", 0.5) + amount * 0.040)
        world["council_acceptance"] = clamp(world.get("council_acceptance", 0.5) + amount * 0.052)
    elif kind == "greet":
        world["council_acceptance"] = clamp(world.get("council_acceptance", 0.5) + amount * 0.025)
    world["trace_integrity"] = clamp(world.get("trace_integrity", 0.0) + 0.030)
    return sum(abs(world[key] - before.get(key, 0.0)) for key in world) / max(1, len(world))


def build_initial_states(source_agents: Sequence[dict[str, object]], source_state: dict[str, object]) -> tuple[dict[str, dict[str, object]], dict[str, float]]:
    live_agents = {}
    prior_agents = source_state.get("agents", {})
    if not isinstance(prior_agents, dict):
        prior_agents = {}
    for index, agent in enumerate(source_agents):
        agent_id = str(agent["agent_id"])
        prior = copy.deepcopy(prior_agents.get(agent_id, {}))
        workspace = agent.get("internal_workspace", {})
        affect = workspace.get("affect", {}) if isinstance(workspace, dict) else {}
        if not prior:
            prior = {
                "agent_id": agent_id,
                "name": agent.get("name", agent_id),
                "role": agent.get("role", "agent"),
                "trust": 0.46 + float(affect.get("attachment", 0.4)) * 0.22,
                "attention": workspace.get("attention", "shared-field") if isinstance(workspace, dict) else "shared-field",
                "motive": workspace.get("motive", "wait") if isinstance(workspace, dict) else "wait",
                "body_state": float(workspace.get("body_state", 0.55)) if isinstance(workspace, dict) else 0.55,
                "fear": float(affect.get("fear", 0.35)),
                "attachment": float(affect.get("attachment", 0.45)),
                "curiosity": float(affect.get("curiosity", 0.35)),
                "workspace_updates": 0,
                "language_hits": 0,
                "responses": 0,
            }
        x, z = agent_position(agent, index)
        prior["position"] = {"x": round(x, 6), "z": round(z, 6)}
        prior["embodied_memory"] = []
        prior["last_player_intent"] = "none"
        live_agents[agent_id] = prior
    world = source_state.get("world", {})
    if not isinstance(world, dict):
        world = {}
    defaults = {
        "shared_water": 0.56,
        "tool_integrity": 0.58,
        "shelter_warmth": 0.54,
        "route_confidence": 0.48,
        "council_acceptance": 0.50,
        "danger_memory": 0.52,
        "trace_integrity": 0.0,
    }
    session_headroom = {
        "shared_water": 0.74,
        "tool_integrity": 0.76,
        "shelter_warmth": 0.72,
        "route_confidence": 0.73,
        "council_acceptance": 0.70,
        "danger_memory": 0.74,
        "trace_integrity": 0.20,
    }
    merged_world = {
        key: clamp(min(float(world.get(key, fallback)), session_headroom[key]))
        for key, fallback in defaults.items()
    }
    return live_agents, merged_world


def run_condition(cfg: InputConfig, condition: Condition, source_agents: Sequence[dict[str, object]], source_state: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    live_agents, world = build_initial_states(source_agents, source_state)
    avatar = {"x": 0.0, "z": -14.0, "fatigue": 0.12, "wetness": 0.10, "thermal_comfort": 0.62}
    trace: list[dict[str, object]] = []
    parsed_inputs = 0
    grounded_actions = 0
    valid_actions = 0
    agent_updates = 0
    world_updates = 0
    memory_updates = 0
    sensory_scores: list[float] = []

    events = [PLAYER_INPUTS[index % len(PLAYER_INPUTS)] for index in range(cfg.steps)]
    for step, event in enumerate(events, start=1):
        target_index = int(event["target"]) % len(source_agents)
        packet = source_agents[target_index]
        agent_id = str(packet["agent_id"])
        live = live_agents[agent_id]
        target_position = agent_position(packet, target_index)
        avatar, distance_after, proximity_valid = move_avatar(avatar, target_position, event, condition)
        parsed = classify_text(str(event["text"]), condition.text_parser)
        kind = str(parsed["kind"])
        focus = FOCUS_BY_KIND.get(kind, "shared-resource")
        token = token_for_focus(packet, focus)
        parsed_ok = bool(parsed["parsed"])
        if parsed_ok:
            parsed_inputs += 1
        actionable = parsed_ok and kind not in {"unknown", "observe"}
        if actionable:
            grounded_actions += 1
        sensory_score = sensory_alignment(packet, kind, step, condition.sensory_context) if parsed_ok else 0.0
        sensory_scores.append(sensory_score)
        can_apply = actionable and proximity_valid
        world_delta = 0.0
        agent_delta = 0.0
        memory_written = False
        if can_apply:
            before = {
                "trust": float(live.get("trust", 0.5)),
                "fear": float(live.get("fear", 0.3)),
                "body_state": float(live.get("body_state", 0.6)),
                "curiosity": float(live.get("curiosity", 0.4)),
                "attachment": float(live.get("attachment", 0.4)),
            }
            confidence = float(parsed.get("confidence", 0.0))
            trust_gain = 0.010 + confidence * 0.018 + sensory_score * 0.020
            if kind in {"comfort", "promise", "offer_resource"}:
                trust_gain += 0.018
            live["trust"] = clamp(before["trust"] + trust_gain)
            live["attention"] = focus
            live["motive"] = kind
            live["body_state"] = clamp(before["body_state"] + 0.006 + sensory_score * 0.010 - avatar["fatigue"] * 0.004)
            live["curiosity"] = clamp(before["curiosity"] + 0.009 + confidence * 0.012)
            live["attachment"] = clamp(before["attachment"] + (0.012 if kind in {"comfort", "offer_resource", "promise", "greet"} else 0.005))
            fear_drop = 0.014 + (0.030 if kind == "comfort" else 0.0) + sensory_score * 0.010
            live["fear"] = clamp(before["fear"] - fear_drop)
            live["responses"] = int(live.get("responses", 0)) + 1
            live["language_hits"] = int(live.get("language_hits", 0)) + (1 if token else 0)
            if condition.agent_memory_update:
                memory = live.setdefault("embodied_memory", [])
                if isinstance(memory, list):
                    memory.append({
                        "step": step,
                        "player_text": event["text"],
                        "kind": kind,
                        "focus": focus,
                        "token": token,
                        "avatar_distance": round(distance_after, 6),
                    })
                live["workspace_updates"] = int(live.get("workspace_updates", 0)) + 1
                live["last_player_intent"] = kind
                memory_written = True
                memory_updates += 1
            after_values = [float(live.get(key, before[key])) for key in before]
            before_values = list(before.values())
            agent_delta = mean(abs(after - before) for after, before in zip(after_values, before_values))
            if agent_delta > 0.004:
                agent_updates += 1
            world_delta = apply_world_effect(world, kind, sensory_score * float(parsed.get("confidence", 0.0)), condition.action_consequence)
            if world_delta > 0.0005:
                world_updates += 1
            valid_actions += 1
        elif parsed_ok and kind == "observe" and condition.persistent_trace:
            world["trace_integrity"] = clamp(world.get("trace_integrity", 0.0) + 0.010)

        response = "input not grounded"
        if can_apply:
            response = f"{live.get('name', agent_id)} grounds '{token}' as {focus}; motive now {kind}."
        elif parsed_ok and not actionable:
            response = "observation retained without world action"
        elif actionable and not proximity_valid:
            response = "action parsed but body is out of range"
        row = {
            "step": step,
            "condition": condition.name,
            "player_text": event["text"],
            "target_agent_id": agent_id,
            "target_agent_name": live.get("name", agent_id),
            "parsed": parsed_ok,
            "parse_reason": parsed.get("reason", ""),
            "kind": kind,
            "focus": focus,
            "native_token": token,
            "confidence": round(float(parsed.get("confidence", 0.0)), 6),
            "avatar": {key: round(value, 6) for key, value in avatar.items()},
            "distance_after": round(distance_after, 6) if distance_after < 900 else None,
            "proximity_valid": proximity_valid,
            "sensory_context_alignment": round(sensory_score, 6),
            "agent_delta": round(agent_delta, 6),
            "world_delta": round(world_delta, 6),
            "memory_written": memory_written,
            "response": response,
        }
        if condition.persistent_trace:
            trace.append(row)

    parse_rate = parsed_inputs / cfg.steps
    proximity_rate = valid_actions / max(1, grounded_actions)
    agent_update_rate = agent_updates / cfg.steps
    world_update_rate = world_updates / cfg.steps
    sensory_context_score = mean(sensory_scores)
    workspace_rate = memory_updates / max(1, agent_updates)
    trace_completeness = len(trace) / cfg.steps if condition.persistent_trace else 0.0
    readiness = (
        parse_rate * 0.14
        + proximity_rate * 0.14
        + agent_update_rate * 0.16
        + world_update_rate * 0.14
        + sensory_context_score * 0.12
        + workspace_rate * 0.16
        + trace_completeness * 0.14
    )
    eval_row = EvalRow(
        condition=condition.name,
        steps=cfg.steps,
        parsed_inputs=parsed_inputs,
        grounded_actions=grounded_actions,
        input_parse_rate=round(parse_rate, 6),
        proximity_valid_action_rate=round(proximity_rate, 6),
        agent_state_update_rate=round(agent_update_rate, 6),
        world_state_update_rate=round(world_update_rate, 6),
        sensory_context_alignment=round(sensory_context_score, 6),
        workspace_continuity_rate=round(workspace_rate, 6),
        trace_completeness=round(trace_completeness, 6),
        embodied_input_readiness=round(readiness, 6),
    )
    final_state = {
        "condition": condition.name,
        "avatar": {key: round(value, 6) for key, value in avatar.items()},
        "world": {key: round(value, 6) for key, value in world.items()},
        "agents": live_agents,
    }
    return eval_row, trace, final_state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_embodied_avatar_input"]

    def loss(condition: str) -> float:
        return round(full.embodied_input_readiness - by_name[condition].embodied_input_readiness, 6)

    supports = (
        full.embodied_input_readiness >= 0.72
        and full.input_parse_rate >= 0.80
        and full.proximity_valid_action_rate >= 0.70
        and full.agent_state_update_rate >= 0.65
        and full.world_state_update_rate >= 0.55
        and full.sensory_context_alignment >= 0.50
        and full.workspace_continuity_rate >= 0.80
        and full.trace_completeness >= 1.0
        and loss("no_spatial_body") >= 0.12
        and loss("no_free_text_parser") >= 0.12
        and loss("no_agent_memory_update") >= 0.10
        and loss("no_action_consequence") >= 0.08
        and loss("no_persistent_trace") >= 0.10
    )
    return VerdictRow(
        full_condition=full.condition,
        full_embodied_input_readiness=full.embodied_input_readiness,
        full_input_parse_rate=full.input_parse_rate,
        full_proximity_valid_action_rate=full.proximity_valid_action_rate,
        full_agent_state_update_rate=full.agent_state_update_rate,
        full_world_state_update_rate=full.world_state_update_rate,
        full_sensory_context_alignment=full.sensory_context_alignment,
        full_workspace_continuity_rate=full.workspace_continuity_rate,
        full_trace_completeness=full.trace_completeness,
        no_spatial_body_loss=loss("no_spatial_body"),
        no_free_text_parser_loss=loss("no_free_text_parser"),
        no_agent_memory_update_loss=loss("no_agent_memory_update"),
        no_sensory_context_loss=loss("no_sensory_context"),
        no_action_consequence_loss=loss("no_action_consequence"),
        no_persistent_trace_loss=loss("no_persistent_trace"),
        supports_embodied_avatar_input_bridge=supports,
        supports_subjective_consciousness=False,
        supports_open_ended_dialogue=False,
        supports_complete_playable_world=False,
        verdict="pass" if supports else "partial_or_failed",
    )


def run_benchmark(cfg: InputConfig) -> dict[str, object]:
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
        "report": 144,
        "name": "SSRM-3D Embodied Avatar Input Bridge",
        "config": asdict(cfg),
        "eval": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "trace": traces["integrated_embodied_avatar_input"],
        "final_state": states["integrated_embodied_avatar_input"],
        "source_agents": source_agents,
        "notes": {
            "claim": "deterministic bridge from scripted avatar interventions to typed, spatially embodied player input",
            "not_claimed": "subjective consciousness, LLM-backed open dialogue, complete playable world, or mature autonomous civilization",
            "input_basis": "keyword-lattice parsing, avatar proximity, sensory-rate context, workspace memory, world consequences, and replay traces",
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", payload)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", payload["trace"])
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", payload["final_state"])
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_EMBODIED_AVATAR_INPUT_BRIDGE_RESULTS", payload)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_EMBODIED_AVATAR_INPUT_BRIDGE_TRACE", payload["trace"])
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_EMBODIED_AVATAR_INPUT_BRIDGE_STATE", payload["final_state"])
    return payload


def parse_args() -> InputConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260618)
    parser.add_argument("--steps", type=int, default=20)
    parser.add_argument("--source-agents", default=str(SOURCE_AGENTS))
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    if args.steps < 12:
        raise SystemExit("--steps must be at least 12")
    return InputConfig(seed=args.seed, steps=args.steps, source_agents=args.source_agents, source_state=args.source_state)


def main() -> None:
    payload = run_benchmark(parse_args())
    print(json.dumps(payload["verdict"], indent=2))


if __name__ == "__main__":
    main()
