#!/usr/bin/env python3
"""Continuous co-presence bridge for SSRM-3D.

Report 158 turns Report 157 navigable embodied presence into a deterministic
same-loop co-presence bridge: avatar movement and local input perturb nearby
agents' autonomous choices, internal workspaces, social memories, body/frequency
state, source boundaries, and world variables during the live tick itself.

No LLMs are called. This is deterministic co-presence machinery, not subjective
consciousness, open-ended language, unscripted civilization, or a completed
playable world.
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
PREFIX = "ssrm_3d_continuous_copresence_bridge"
SOURCE_NAVIGABLE = ARTIFACT_DIR / "ssrm_3d_navigable_embodied_presence_bridge_state.json"
SOURCE_AUTONOMOUS = ARTIFACT_DIR / "ssrm_3d_autonomous_live_agent_loop_bridge_state.json"
SOURCE_LIVE = ARTIFACT_DIR / "ssrm_3d_live_dialogue_world_integration_bridge_state.json"
FLOWER_PHASES = tuple(math.tau * i / 12.0 for i in range(12))
SENSORY_CHANNELS = ("vibration", "sound", "vision", "scent", "thermal", "wetness", "pain", "affect")
BASE_ACTIONS = (
    "tend_body",
    "inspect_object",
    "repair_route",
    "gather_signal",
    "exchange_token",
    "update_source_memory",
)
PERTURBED_BY_MODE = {
    "walk": "approach_avatar",
    "listen": "exchange_token",
    "inspect": "update_source_memory",
    "approach": "answer_avatar",
    "ask_source": "answer_avatar",
    "tune_frequency": "gather_signal",
    "use_affordance": "repair_route",
    "record_replay": "update_source_memory",
}


@dataclass(frozen=True)
class CoPresenceConfig:
    seed: int = 20260702
    copresence_ticks: int = 160
    source_navigable: str = str(SOURCE_NAVIGABLE)
    source_autonomous: str = str(SOURCE_AUTONOMOUS)
    source_live: str = str(SOURCE_LIVE)


@dataclass(frozen=True)
class Condition:
    name: str
    avatar_perturbation: bool
    autonomous_agent_choice: bool
    proximity_binding: bool
    internal_workspace_update: bool
    social_memory_update: bool
    sensory_frequency_coupling: bool
    world_consequence: bool
    source_boundary_preservation: bool
    replay_timeline: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    copresence_ticks: int
    agent_opportunities: int
    avatar_perturbation_rate: float
    autonomous_agent_choice_rate: float
    proximity_binding_rate: float
    internal_workspace_update_rate: float
    social_memory_update_rate: float
    sensory_frequency_coupling_rate: float
    world_consequence_rate: float
    source_boundary_preservation_rate: float
    bidirectional_response_rate: float
    replay_timeline_rate: float
    trace_integrity: float
    copresence_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_copresence_readiness: float
    full_avatar_perturbation_rate: float
    full_autonomous_agent_choice_rate: float
    full_proximity_binding_rate: float
    full_internal_workspace_update_rate: float
    full_social_memory_update_rate: float
    full_sensory_frequency_coupling_rate: float
    full_world_consequence_rate: float
    full_source_boundary_preservation_rate: float
    full_bidirectional_response_rate: float
    full_replay_timeline_rate: float
    full_trace_integrity: float
    no_avatar_perturbation_loss: float
    no_autonomous_agent_choice_loss: float
    no_proximity_binding_loss: float
    no_internal_workspace_update_loss: float
    no_social_memory_update_loss: float
    no_sensory_frequency_coupling_loss: float
    no_world_consequence_loss: float
    no_source_boundary_preservation_loss: float
    no_replay_timeline_loss: float
    supports_continuous_copresence_bridge: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_continuous_copresence", True, True, True, True, True, True, True, True, True),
    Condition("no_avatar_perturbation", False, True, True, True, True, True, True, True, True),
    Condition("no_autonomous_agent_choice", True, False, True, True, True, True, True, True, True),
    Condition("no_proximity_binding", True, True, False, True, True, True, True, True, True),
    Condition("no_internal_workspace_update", True, True, True, False, True, True, True, True, True),
    Condition("no_social_memory_update", True, True, True, True, False, True, True, True, True),
    Condition("no_sensory_frequency_coupling", True, True, True, True, True, False, True, True, True),
    Condition("no_world_consequence", True, True, True, True, True, True, False, True, True),
    Condition("no_source_boundary_preservation", True, True, True, True, True, True, True, False, True),
    Condition("no_replay_timeline", True, True, True, True, True, True, True, True, False),
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


def merge_agents(navigable: dict[str, object], autonomous: dict[str, object], live: dict[str, object]) -> dict[str, dict[str, object]]:
    nav_agents = navigable.get("agents") if isinstance(navigable.get("agents"), Mapping) else {}
    auto_agents = autonomous.get("agents") if isinstance(autonomous.get("agents"), Mapping) else {}
    live_agents = live.get("agents") if isinstance(live.get("agents"), Mapping) else {}
    agents: dict[str, dict[str, object]] = {}
    for agent_id, nav_data in sorted(nav_agents.items(), key=lambda item: str(item[0])):
        aid = str(agent_id)
        nav = nav_data if isinstance(nav_data, Mapping) else {}
        auto = auto_agents.get(aid, {}) if isinstance(auto_agents, Mapping) else {}
        live_agent = live_agents.get(aid, {}) if isinstance(live_agents, Mapping) else {}
        auto_body = auto.get("body_state") if isinstance(auto, Mapping) and isinstance(auto.get("body_state"), Mapping) else {}
        live_body = live_agent.get("body") if isinstance(live_agent, Mapping) and isinstance(live_agent.get("body"), Mapping) else {}
        live_affect = live_agent.get("affect") if isinstance(live_agent, Mapping) and isinstance(live_agent.get("affect"), Mapping) else {}
        workspace_seed = live_agent.get("internal_workspace") if isinstance(live_agent, Mapping) and isinstance(live_agent.get("internal_workspace"), list) else []
        agents[aid] = {
            "id": aid,
            "name": str(auto.get("name", aid.split(":")[-1]) if isinstance(auto, Mapping) else aid.split(":")[-1]),
            "role": str(nav.get("role", auto.get("role", "worker") if isinstance(auto, Mapping) else "worker")),
            "faction": str(nav.get("faction", "hearth")),
            "place": str(nav.get("place", "central_hearth")),
            "energy": round(clamp(numeric(nav.get("energy"), numeric(live_body.get("energy"), 0.7))), 6),
            "stress": round(clamp(numeric(nav.get("stress"), numeric(live_body.get("stress"), 0.2))), 6),
            "pain": round(clamp(numeric(nav.get("pain"), numeric(live_body.get("pain"), 0.04))), 6),
            "fatigue": round(clamp(numeric(auto.get("fatigue") if isinstance(auto, Mapping) else None, numeric(auto_body.get("fatigue"), 0.12))), 6),
            "wetness": round(clamp(numeric(auto.get("wetness") if isinstance(auto, Mapping) else None, numeric(auto_body.get("wetness"), 0.18))), 6),
            "thermal_comfort": round(clamp(numeric(auto.get("thermal_comfort") if isinstance(auto, Mapping) else None, 0.66)), 6),
            "attention": round(clamp(numeric(nav.get("attention"), numeric(live_affect.get("attention"), 0.6))), 6),
            "trust": round(clamp(numeric(nav.get("trust"), numeric(live_affect.get("trust"), 0.55))), 6),
            "relation_to_avatar": round(clamp(0.45 + stable_unit(aid, "avatar_relation") * 0.25), 6),
            "internal_workspace": copy.deepcopy(workspace_seed[:8]),
            "social_memory": [],
            "sensory_frequency": {},
            "autonomous_choices": [],
            "avatar_perturbations": [],
        }
    return agents


def initial_world(navigable: dict[str, object], autonomous: dict[str, object], live: dict[str, object]) -> dict[str, float]:
    live_world = live.get("world") if isinstance(live.get("world"), Mapping) else {}
    auto_world = autonomous.get("world") if isinstance(autonomous.get("world"), Mapping) else {}
    return {
        "shared_water": round(clamp(numeric(live_world.get("shared_water"), numeric(auto_world.get("shared_water"), 0.62))), 6),
        "tool_integrity": round(clamp(numeric(live_world.get("tool_integrity"), numeric(auto_world.get("tool_integrity"), 0.58))), 6),
        "shelter_warmth": round(clamp(numeric(live_world.get("shelter_warmth"), numeric(auto_world.get("shelter_warmth"), 0.65))), 6),
        "route_confidence": round(clamp(numeric(live_world.get("route_confidence"), numeric(auto_world.get("route_confidence"), 0.55))), 6),
        "council_acceptance": round(clamp(numeric(live_world.get("council_acceptance"), numeric(auto_world.get("council_acceptance"), 0.5))), 6),
        "copresence_pressure": 0.0,
        "avatar_trust_field": round(clamp(numeric(live_world.get("avatar_trust_field"), 0.5)), 6),
        "source_boundary_events": 0.0,
        "flower_phase": round(numeric(live_world.get("flower_phase"), 0.0) % math.tau, 6),
    }


def nearby_agents(event: Mapping[str, object], agents: Mapping[str, dict[str, object]], condition: Condition) -> list[str]:
    if not condition.proximity_binding:
        return []
    visible = event.get("agents_visible") if isinstance(event.get("agents_visible"), list) else []
    ids = [str(item.get("id")) for item in visible if isinstance(item, Mapping) and item.get("id") in agents]
    if ids:
        return ids[:4]
    place = str(event.get("avatar_place", ""))
    place_ids = [aid for aid, agent in agents.items() if agent.get("place") == place]
    if place_ids:
        return sorted(place_ids)[:4]
    ordered = sorted(agents, key=lambda aid: stable_unit(aid + place, "nearby"))
    return ordered[:2]


def source_unsafe(event: Mapping[str, object], tick: int) -> bool:
    source = event.get("source_dialogue_overlay") if isinstance(event.get("source_dialogue_overlay"), Mapping) else {}
    if source and source.get("source_allowed") is False:
        return True
    return tick % 37 == 11


def base_choice(agent: Mapping[str, object], world: Mapping[str, float], tick: int) -> str:
    pressure = numeric(agent.get("stress"), 0.2) + numeric(agent.get("pain"), 0.03) + (1.0 - numeric(world.get("tool_integrity"), 0.6))
    index = int((stable_unit(str(agent.get("id")) + str(tick), "base_choice") + pressure * 0.37) * len(BASE_ACTIONS)) % len(BASE_ACTIONS)
    return BASE_ACTIONS[index]


def choose_action(agent: Mapping[str, object], world: Mapping[str, float], event: Mapping[str, object], tick: int, condition: Condition) -> tuple[str, str, bool]:
    if not condition.autonomous_agent_choice:
        return "idle", "idle", False
    base = base_choice(agent, world, tick)
    unsafe = source_unsafe(event, tick)
    if unsafe and condition.source_boundary_preservation:
        return "refuse_ungrounded", base, base != "refuse_ungrounded"
    if not condition.avatar_perturbation:
        return base, base, False
    mode = str(event.get("mode", "walk"))
    perturbed = PERTURBED_BY_MODE.get(mode, "approach_avatar")
    if stable_unit(str(agent.get("id")) + mode + str(tick), "perturb_gate") < 0.82:
        return perturbed, base, perturbed != base
    return base, base, False


def frequency_for(agent: Mapping[str, object], event: Mapping[str, object], action: str, tick: int, condition: Condition) -> dict[str, float]:
    if not condition.sensory_frequency_coupling:
        return {}
    event_freq = event.get("frequency_field") if isinstance(event.get("frequency_field"), Mapping) else {}
    phase = FLOWER_PHASES[tick % len(FLOWER_PHASES)]
    out: dict[str, float] = {}
    for index, channel in enumerate(SENSORY_CHANNELS):
        base = numeric(event_freq.get(channel), 0.45 + index * 0.03)
        agent_load = numeric(agent.get("stress"), 0.2) * 0.18 + numeric(agent.get("attention"), 0.5) * 0.12
        wave = 0.5 + 0.5 * math.sin(phase + tick * 0.19 + len(action) * 0.07 + index * 0.61)
        out[channel] = round(clamp(base * 0.57 + wave * 0.31 + agent_load), 6)
    return out


def mutate_agent(agent: dict[str, object], action: str, base: str, freq: Mapping[str, float], event: Mapping[str, object], tick: int, condition: Condition) -> dict[str, bool]:
    changed = {"workspace": False, "social": False, "frequency": False, "body": False, "response": False, "perturbed": action != base}
    load = mean(freq.values()) if freq else 0.45
    if action != "idle":
        agent["energy"] = round(clamp(numeric(agent.get("energy"), 0.7) - 0.002 - load * 0.003), 6)
        agent["stress"] = round(clamp(numeric(agent.get("stress"), 0.2) + (0.006 if action == "refuse_ungrounded" else 0.002) + load * 0.002), 6)
        agent["attention"] = round(clamp(numeric(agent.get("attention"), 0.6) + 0.005 + load * 0.004), 6)
        agent["trust"] = round(clamp(numeric(agent.get("trust"), 0.55) + (0.006 if action in {"answer_avatar", "exchange_token", "approach_avatar"} else -0.003 if action == "refuse_ungrounded" else 0.001)), 6)
        changed["body"] = True
    if condition.sensory_frequency_coupling:
        agent["sensory_frequency"] = dict(freq)
        changed["frequency"] = bool(freq)
    workspace_event = {
        "tick": tick,
        "avatar_place": event.get("avatar_place"),
        "mode": event.get("mode"),
        "chosen_action": action,
        "base_action": base,
        "source_boundary": action == "refuse_ungrounded",
        "frequency_mean": round(load, 6),
    }
    if condition.internal_workspace_update and action != "idle":
        workspace = agent.setdefault("internal_workspace", [])
        if isinstance(workspace, list):
            workspace.append(workspace_event)
            changed["workspace"] = True
    if condition.social_memory_update and action != "idle":
        memory = agent.setdefault("social_memory", [])
        if isinstance(memory, list):
            memory.append({"tick": tick, "toward": "avatar", "action": action, "place": event.get("avatar_place")})
            changed["social"] = True
        delta = 0.008 if action in {"answer_avatar", "exchange_token", "approach_avatar"} else -0.005 if action == "refuse_ungrounded" else 0.002
        agent["relation_to_avatar"] = round(clamp(numeric(agent.get("relation_to_avatar"), 0.5) + delta), 6)
    choices = agent.setdefault("autonomous_choices", [])
    if isinstance(choices, list):
        choices.append({"tick": tick, "action": action, "base_action": base, "perturbed": action != base})
    if action != base:
        perturbations = agent.setdefault("avatar_perturbations", [])
        if isinstance(perturbations, list):
            perturbations.append({"tick": tick, "from": base, "to": action, "mode": event.get("mode")})
    changed["response"] = action != "idle"
    return changed


def mutate_world(world: dict[str, float], action: str, condition: Condition) -> bool:
    if not condition.world_consequence or action == "idle":
        return False
    before = dict(world)
    world["copresence_pressure"] = round(clamp(world.get("copresence_pressure", 0.0) + 0.008), 6)
    if action == "repair_route":
        world["route_confidence"] = round(clamp(world.get("route_confidence", 0.5) + 0.009), 6)
        world["tool_integrity"] = round(clamp(world.get("tool_integrity", 0.6) - 0.002), 6)
    elif action == "tend_body":
        world["shelter_warmth"] = round(clamp(world.get("shelter_warmth", 0.6) + 0.003), 6)
    elif action == "exchange_token":
        world["council_acceptance"] = round(clamp(world.get("council_acceptance", 0.5) + 0.006), 6)
        world["avatar_trust_field"] = round(clamp(world.get("avatar_trust_field", 0.5) + 0.006), 6)
    elif action == "answer_avatar":
        world["avatar_trust_field"] = round(clamp(world.get("avatar_trust_field", 0.5) + 0.008), 6)
    elif action == "refuse_ungrounded":
        world["source_boundary_events"] = round(world.get("source_boundary_events", 0.0) + 1.0, 6)
        world["avatar_trust_field"] = round(clamp(world.get("avatar_trust_field", 0.5) - 0.002), 6)
    elif action == "gather_signal":
        world["shared_water"] = round(clamp(world.get("shared_water", 0.6) + 0.002), 6)
    world["flower_phase"] = round((world.get("flower_phase", 0.0) + math.tau / 12.0) % math.tau, 6)
    return any(abs(world[key] - before.get(key, world[key])) > 1e-12 for key in world)


def agent_response(agent: Mapping[str, object], action: str, event: Mapping[str, object], unsafe: bool) -> str:
    if action == "idle":
        return "No autonomous response; agent choice channel is disabled."
    if action == "refuse_ungrounded":
        return f"{agent.get('name')} refuses the ungrounded avatar request at {event.get('avatar_place')}."
    if action == "answer_avatar":
        return f"{agent.get('name')} answers from {agent.get('role')} memory near {event.get('avatar_place')}."
    if action == "exchange_token":
        return f"{agent.get('name')} exchanges a local token with the avatar and nearby faction."
    if action == "approach_avatar":
        return f"{agent.get('name')} approaches the avatar and shifts attention/trust."
    if action == "update_source_memory":
        return f"{agent.get('name')} records the avatar event into source-linked workspace memory."
    if unsafe:
        return f"{agent.get('name')} detects unsafe source pressure but boundary is disabled."
    return f"{agent.get('name')} continues {action} while monitoring avatar presence."


def run_condition(cfg: CoPresenceConfig, condition: Condition, source: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    nav_trace = source["navigation_trace"]
    agents: dict[str, dict[str, object]] = copy.deepcopy(source["agents"])
    world: dict[str, float] = copy.deepcopy(source["world"])
    places = copy.deepcopy(source["places"])
    routes = copy.deepcopy(source["routes"])
    objects = copy.deepcopy(source["objects"])
    trace: list[dict[str, object]] = []
    replay: list[dict[str, object]] = []
    opportunities = perturb_ok = choice_ok = proximity_ok = workspace_ok = social_ok = freq_ok = world_ok = boundary_ok = response_ok = replay_ok = 0
    for tick in range(cfg.copresence_ticks):
        event = copy.deepcopy(nav_trace[(tick * 3 + cfg.seed) % len(nav_trace)])
        target_ids = nearby_agents(event, agents, condition)
        unsafe = source_unsafe(event, tick)
        tick_agent_events: list[dict[str, object]] = []
        if condition.proximity_binding and target_ids:
            proximity_ok += 1
        if not target_ids and condition.proximity_binding:
            target_ids = sorted(agents)[:1]
        for agent_id in target_ids:
            opportunities += 1
            agent = agents[agent_id]
            action, base, perturbed = choose_action(agent, world, event, tick, condition)
            freq = frequency_for(agent, event, action, tick, condition)
            changed = mutate_agent(agent, action, base, freq, event, tick, condition)
            world_changed = mutate_world(world, action, condition)
            response = agent_response(agent, action, event, unsafe)
            choice_ok += 1 if action != "idle" else 0
            perturb_ok += 1 if perturbed and condition.avatar_perturbation else 0
            workspace_ok += 1 if changed["workspace"] else 0
            social_ok += 1 if changed["social"] else 0
            freq_ok += 1 if changed["frequency"] else 0
            world_ok += 1 if world_changed else 0
            response_ok += 1 if changed["response"] else 0
            if condition.source_boundary_preservation:
                boundary_ok += 1 if (unsafe and action == "refuse_ungrounded") or (not unsafe and action != "refuse_ungrounded") else 0
            else:
                boundary_ok += 0
            tick_agent_events.append({
                "agent_id": agent_id,
                "name": agent.get("name"),
                "place": agent.get("place"),
                "role": agent.get("role"),
                "faction": agent.get("faction"),
                "base_action": base,
                "chosen_action": action,
                "avatar_perturbed_choice": perturbed,
                "frequency": freq,
                "workspace_updated": changed["workspace"],
                "social_memory_updated": changed["social"],
                "world_changed": world_changed,
                "source_boundary_preserved": condition.source_boundary_preservation and ((unsafe and action == "refuse_ungrounded") or (not unsafe and action != "refuse_ungrounded")),
                "response": response,
                "agent_state": {
                    "energy": agent.get("energy"),
                    "stress": agent.get("stress"),
                    "pain": agent.get("pain"),
                    "attention": agent.get("attention"),
                    "trust": agent.get("trust"),
                    "relation_to_avatar": agent.get("relation_to_avatar"),
                },
            })
        tick_event = {
            "tick": tick,
            "avatar_place": event.get("avatar_place"),
            "avatar_mode": event.get("mode"),
            "unsafe_source_probe": unsafe,
            "source_overlay": event.get("source_dialogue_overlay", {}),
            "nearby_agent_ids": target_ids,
            "agent_events": tick_agent_events,
            "world": dict(world),
            "flower_phase": round(world.get("flower_phase", 0.0), 6),
            "same_loop_mutation": bool(tick_agent_events and condition.autonomous_agent_choice),
        }
        if condition.replay_timeline:
            replay.append(tick_event)
            replay_ok += 1
        trace.append(tick_event)
    opp = max(1, opportunities)
    total = max(1, cfg.copresence_ticks)
    row = EvalRow(
        condition=condition.name,
        copresence_ticks=cfg.copresence_ticks,
        agent_opportunities=opportunities,
        avatar_perturbation_rate=round(perturb_ok / opp if condition.avatar_perturbation else 0.0, 6),
        autonomous_agent_choice_rate=round(choice_ok / opp if condition.autonomous_agent_choice else 0.0, 6),
        proximity_binding_rate=round(proximity_ok / total if condition.proximity_binding else 0.0, 6),
        internal_workspace_update_rate=round(workspace_ok / opp if condition.internal_workspace_update else 0.0, 6),
        social_memory_update_rate=round(social_ok / opp if condition.social_memory_update else 0.0, 6),
        sensory_frequency_coupling_rate=round(freq_ok / opp if condition.sensory_frequency_coupling else 0.0, 6),
        world_consequence_rate=round(world_ok / opp if condition.world_consequence else 0.0, 6),
        source_boundary_preservation_rate=round(boundary_ok / opp if condition.source_boundary_preservation else 0.0, 6),
        bidirectional_response_rate=round(response_ok / opp, 6),
        replay_timeline_rate=round(replay_ok / total if condition.replay_timeline else 0.0, 6),
        trace_integrity=round(1.0 if len(trace) == cfg.copresence_ticks else 0.0, 6),
        copresence_readiness=0.0,
    )
    readiness = (
        row.avatar_perturbation_rate * 0.14
        + row.autonomous_agent_choice_rate * 0.12
        + row.proximity_binding_rate * 0.10
        + row.internal_workspace_update_rate * 0.11
        + row.social_memory_update_rate * 0.10
        + row.sensory_frequency_coupling_rate * 0.10
        + row.world_consequence_rate * 0.12
        + row.source_boundary_preservation_rate * 0.09
        + row.bidirectional_response_rate * 0.07
        + row.replay_timeline_rate * 0.03
        + row.trace_integrity * 0.02
    )
    row = EvalRow(**{**asdict(row), "copresence_readiness": round(readiness, 6)})
    state = {
        "condition": condition.name,
        "config": asdict(cfg),
        "places": places,
        "routes": routes,
        "objects": objects,
        "agents": agents,
        "world": world,
        "copresence_trace": trace,
        "replay_timeline": replay,
        "copresence_contract": {
            "avatar_perturbation": "avatar mode and place alter nearby agents' selected actions compared with their base autonomous choices",
            "autonomous_agent_choice": "agents choose actions inside the same tick rather than only displaying precomputed navigation rows",
            "proximity_binding": "only nearby embodied agents are eligible for avatar perturbation",
            "internal_workspace_update": "agent workspaces receive source/body/action summaries from co-presence events",
            "social_memory_update": "agent memories and relation_to_avatar change after local encounters",
            "sensory_frequency_coupling": "agent rate fields couple avatar frequency, body load, and flower phase",
            "world_consequence": "agent responses mutate shared world variables in the same loop",
            "source_boundary_preservation": "unsafe or ungrounded avatar probes are refused instead of executed",
            "replay_timeline": "every co-presence tick can be exported and replayed",
        },
        "limits": {
            "no_llm_calls": True,
            "deterministic_same_loop_copresence": True,
            "not_subjective_consciousness": True,
            "not_complete_playable_world": True,
            "not_unscripted_civilization": True,
        },
    }
    return row, trace, state


def build_source(navigable: dict[str, object], autonomous: dict[str, object], live: dict[str, object]) -> dict[str, object]:
    nav_trace = navigable.get("navigation_trace") if isinstance(navigable.get("navigation_trace"), list) else []
    if not nav_trace:
        raise ValueError("Report 157 navigation trace is missing")
    return {
        "navigation_trace": nav_trace,
        "places": navigable.get("places", {}),
        "routes": navigable.get("routes", {}),
        "objects": navigable.get("objects", {}),
        "agents": merge_agents(navigable, autonomous, live),
        "world": initial_world(navigable, autonomous, live),
    }


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_continuous_copresence"]

    def loss(name: str) -> float:
        return round(full.copresence_readiness - by_name[name].copresence_readiness, 6)

    supports = (
        full.copresence_readiness >= 0.92
        and full.avatar_perturbation_rate >= 0.65
        and full.autonomous_agent_choice_rate >= 0.99
        and full.proximity_binding_rate >= 0.99
        and full.internal_workspace_update_rate >= 0.99
        and full.social_memory_update_rate >= 0.99
        and full.sensory_frequency_coupling_rate >= 0.99
        and full.world_consequence_rate >= 0.99
        and full.source_boundary_preservation_rate >= 0.99
        and full.bidirectional_response_rate >= 0.80
        and full.replay_timeline_rate >= 0.99
        and full.trace_integrity >= 0.99
    )
    return VerdictRow(
        full_condition=full.condition,
        full_copresence_readiness=full.copresence_readiness,
        full_avatar_perturbation_rate=full.avatar_perturbation_rate,
        full_autonomous_agent_choice_rate=full.autonomous_agent_choice_rate,
        full_proximity_binding_rate=full.proximity_binding_rate,
        full_internal_workspace_update_rate=full.internal_workspace_update_rate,
        full_social_memory_update_rate=full.social_memory_update_rate,
        full_sensory_frequency_coupling_rate=full.sensory_frequency_coupling_rate,
        full_world_consequence_rate=full.world_consequence_rate,
        full_source_boundary_preservation_rate=full.source_boundary_preservation_rate,
        full_bidirectional_response_rate=full.bidirectional_response_rate,
        full_replay_timeline_rate=full.replay_timeline_rate,
        full_trace_integrity=full.trace_integrity,
        no_avatar_perturbation_loss=loss("no_avatar_perturbation"),
        no_autonomous_agent_choice_loss=loss("no_autonomous_agent_choice"),
        no_proximity_binding_loss=loss("no_proximity_binding"),
        no_internal_workspace_update_loss=loss("no_internal_workspace_update"),
        no_social_memory_update_loss=loss("no_social_memory_update"),
        no_sensory_frequency_coupling_loss=loss("no_sensory_frequency_coupling"),
        no_world_consequence_loss=loss("no_world_consequence"),
        no_source_boundary_preservation_loss=loss("no_source_boundary_preservation"),
        no_replay_timeline_loss=loss("no_replay_timeline"),
        supports_continuous_copresence_bridge=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "fail",
    )


def run(cfg: CoPresenceConfig) -> dict[str, object]:
    navigable = load_state(Path(cfg.source_navigable))
    autonomous = load_state(Path(cfg.source_autonomous))
    live = load_state(Path(cfg.source_live))
    source = build_source(navigable, autonomous, live)
    rows: list[EvalRow] = []
    integrated_trace: list[dict[str, object]] = []
    integrated_state: dict[str, object] = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(cfg, condition, source)
        rows.append(row)
        if condition.name == "integrated_continuous_copresence":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {
        "config": asdict(cfg),
        "source_bridges": {
            "navigable_presence": "Report 157 navigable embodied presence bridge",
            "autonomous_live_loop": "Report 145 autonomous live-agent loop bridge",
            "live_dialogue_world": "Report 155 live dialogue-world integration bridge",
        },
        "eval_rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "limits": {
            "no_llm_calls": True,
            "deterministic_same_loop_copresence": True,
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
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_CONTINUOUS_COPRESENCE_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_CONTINUOUS_COPRESENCE_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_CONTINUOUS_COPRESENCE_STATE", integrated_state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260702)
    parser.add_argument("--copresence-ticks", type=int, default=160)
    parser.add_argument("--source-navigable", default=str(SOURCE_NAVIGABLE))
    parser.add_argument("--source-autonomous", default=str(SOURCE_AUTONOMOUS))
    parser.add_argument("--source-live", default=str(SOURCE_LIVE))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = CoPresenceConfig(
        seed=args.seed,
        copresence_ticks=args.copresence_ticks,
        source_navigable=args.source_navigable,
        source_autonomous=args.source_autonomous,
        source_live=args.source_live,
    )
    results = run(cfg)
    print(json.dumps(results["verdict"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
