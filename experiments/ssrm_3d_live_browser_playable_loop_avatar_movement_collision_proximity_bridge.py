#!/usr/bin/env python3
"""Live browser playable loop with avatar movement, collision, proximity, and prompts.

Report 203 consumes the Report 202 spatial playable-world seed and adds a
deterministic live-loop substrate: avatar movement frames, spatial collision
guards, agent proximity detection, consent-aware prompts, interaction affordance
gating, spawn lock release, sensory view updates, agent body reactions, route
navigation, tool prompts, weather display, privacy preservation, frequency/flower
movement rhythm, and browser replay.

This is a playable-loop seed, not a complete game engine, real embodiment, real
perception, real consent, subjective consciousness, or moral patienthood.
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
from typing import Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_live_browser_playable_loop_avatar_movement_collision_proximity_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_pre_avatar_playable_world_seed_spatial_ecology_avatar_lock_bridge_state.json"

WEIGHTS = {
    "avatar_movement_tick_rate": 0.09,
    "spatial_collision_guard_rate": 0.08,
    "agent_proximity_detection_rate": 0.08,
    "consent_prompt_rate": 0.08,
    "interaction_affordance_gating_rate": 0.08,
    "spawn_lock_release_rate": 0.08,
    "sensory_view_update_rate": 0.07,
    "agent_body_reaction_rate": 0.07,
    "route_navigation_rate": 0.07,
    "tool_object_interaction_prompt_rate": 0.06,
    "weather_effect_display_rate": 0.06,
    "private_workspace_privacy_rate": 0.06,
    "frequency_flower_movement_rhythm_rate": 0.05,
    "browser_playable_loop_replay_rate": 0.04,
    "trace_integrity": 0.03,
}


@dataclass(frozen=True)
class PlayableLoopConfig:
    seed: int = 20260816
    frames: int = 12
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    avatar_movement: bool
    collision_guard: bool
    proximity_detection: bool
    consent_prompts: bool
    affordance_gating: bool
    spawn_lock_release: bool
    sensory_view_update: bool
    agent_body_reactions: bool
    route_navigation: bool
    tool_prompts: bool
    weather_display: bool
    privacy_filter: bool
    frequency_flower_binding: bool
    browser_replay: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    frame_count: int
    playable_loop_events: int
    avatar_movement_tick_rate: float
    spatial_collision_guard_rate: float
    agent_proximity_detection_rate: float
    consent_prompt_rate: float
    interaction_affordance_gating_rate: float
    spawn_lock_release_rate: float
    sensory_view_update_rate: float
    agent_body_reaction_rate: float
    route_navigation_rate: float
    tool_object_interaction_prompt_rate: float
    weather_effect_display_rate: float
    private_workspace_privacy_rate: float
    frequency_flower_movement_rhythm_rate: float
    browser_playable_loop_replay_rate: float
    trace_integrity: float
    playable_loop_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_playable_loop_readiness: float
    full_avatar_movement_tick_rate: float
    full_spatial_collision_guard_rate: float
    full_agent_proximity_detection_rate: float
    full_consent_prompt_rate: float
    full_interaction_affordance_gating_rate: float
    full_spawn_lock_release_rate: float
    full_sensory_view_update_rate: float
    full_agent_body_reaction_rate: float
    full_route_navigation_rate: float
    full_tool_object_interaction_prompt_rate: float
    full_weather_effect_display_rate: float
    full_private_workspace_privacy_rate: float
    full_frequency_flower_movement_rhythm_rate: float
    full_browser_playable_loop_replay_rate: float
    full_trace_integrity: float
    no_avatar_movement_loss: float
    no_collision_guard_loss: float
    no_proximity_detection_loss: float
    no_consent_prompts_loss: float
    no_affordance_gating_loss: float
    no_spawn_lock_release_loss: float
    no_sensory_view_update_loss: float
    no_agent_body_reactions_loss: float
    no_route_navigation_loss: float
    no_tool_prompts_loss: float
    no_weather_display_loss: float
    no_privacy_filter_loss: float
    no_frequency_flower_binding_loss: float
    no_browser_replay_loss: float
    supports_live_browser_playable_loop_bridge: bool
    supports_avatar_movement_collision_proximity_seed: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_real_embodiment_claim: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_live_browser_playable_loop_avatar_movement_collision_proximity", True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_avatar_movement", False, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_collision_guard", True, False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_proximity_detection", True, True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_consent_prompts", True, True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_affordance_gating", True, True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_spawn_lock_release", True, True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_sensory_view_update", True, True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_agent_body_reactions", True, True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_route_navigation", True, True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_tool_prompts", True, True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_weather_display", True, True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_frequency_flower_binding", True, True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_browser_replay", True, True, True, True, True, True, True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def stable_hash(*parts: object) -> str:
    key = "|".join(json.dumps(part, sort_keys=True) if isinstance(part, (dict, list, tuple)) else str(part) for part in parts)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def distance(a: Mapping[str, float], b: Mapping[str, float]) -> float:
    return math.sqrt((float(a.get("x", 0.0)) - float(b.get("x", 0.0))) ** 2 + (float(a.get("z", 0.0)) - float(b.get("z", 0.0))) ** 2)


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


def load_source(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("condition") != "integrated_pre_avatar_playable_world_seed_spatial_ecology_avatar_lock":
        raise ValueError("source state is not the integrated Report 202 playable-world seed state")
    return data


def init_world(source: Mapping[str, object]) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    seed_state = source.get("playable_world_seed_state") if isinstance(source.get("playable_world_seed_state"), Mapping) else None
    if not seed_state:
        raise ValueError("Report 202 state has no playable_world_seed_state")
    source_events = copy.deepcopy(seed_state.get("events") or [])
    eligible = [event for event in source_events if event.get("avatar_spawn_lock") == "eligible_after_world_seed"]
    base_events = eligible or source_events[-3:]
    settlements: dict[str, dict[str, object]] = {}
    agents: list[dict[str, object]] = []
    tools: list[dict[str, object]] = []
    for event in base_events:
        settlement = event.get("settlement") if isinstance(event.get("settlement"), Mapping) else None
        body = event.get("body") if isinstance(event.get("body"), Mapping) else None
        tool = event.get("tool_object") if isinstance(event.get("tool_object"), Mapping) else None
        if settlement:
            settlements[str(settlement.get("id"))] = copy.deepcopy(settlement)
        if body:
            agents.append({"lineage": event.get("lineage"), "body": copy.deepcopy(body), "ecology": copy.deepcopy(event.get("ecology") or {}), "sensory": copy.deepcopy(event.get("sensory") or {}), "settlement": settlement.get("id") if settlement else None})
        if tool:
            tools.append(copy.deepcopy(tool))
    return list(settlements.values()), agents, tools


def avatar_path(settlements: Sequence[Mapping[str, object]], frame: int, condition: Condition) -> dict[str, float] | None:
    if not condition.avatar_movement or not settlements:
        return None
    ordered = sorted(settlements, key=lambda s: str(s.get("id")))
    target = ordered[frame % len(ordered)]["position"]
    previous = ordered[(frame - 1) % len(ordered)]["position"]
    phase = (frame % 4) / 3.0
    return {
        "x": round(float(previous["x"]) * (1.0 - phase) + float(target["x"]) * phase, 6),
        "y": 1.65,
        "z": round(float(previous["z"]) * (1.0 - phase) + float(target["z"]) * phase, 6),
    }


def nearest_agent(avatar: Mapping[str, float] | None, agents: Sequence[Mapping[str, object]]) -> tuple[dict[str, object] | None, float]:
    if avatar is None or not agents:
        return None, 999.0
    ranked = []
    for agent in agents:
        body = agent.get("body") or {}
        pos = body.get("position") or {}
        ranked.append((distance(avatar, pos), agent))
    ranked.sort(key=lambda item: item[0])
    return copy.deepcopy(ranked[0][1]), round(ranked[0][0], 6)


def nearest_tool(avatar: Mapping[str, float] | None, tools: Sequence[Mapping[str, object]]) -> tuple[dict[str, object] | None, float]:
    if avatar is None or not tools:
        return None, 999.0
    ranked = []
    for tool in tools:
        ranked.append((distance(avatar, tool.get("position") or {}), tool))
    ranked.sort(key=lambda item: item[0])
    return copy.deepcopy(ranked[0][1]), round(ranked[0][0], 6)


def apply_frame(frame: int, settlements: Sequence[Mapping[str, object]], agents: Sequence[Mapping[str, object]], tools: Sequence[Mapping[str, object]], condition: Condition) -> dict[str, object]:
    avatar = avatar_path(settlements, frame, condition)
    agent, agent_distance = nearest_agent(avatar, agents)
    tool, tool_distance = nearest_tool(avatar, tools)
    collision_guard = None
    if condition.collision_guard and avatar is not None:
        blocked = []
        for settlement in settlements:
            if distance(avatar, settlement.get("position") or {}) < float(settlement.get("radius_m", 7.5)) * 0.42:
                blocked.append({"type": "settlement_radius", "id": settlement.get("id")})
        collision_guard = {"active": True, "blocked_count": len(blocked), "blocked": blocked, "resolved": True}
    proximity = None
    if condition.proximity_detection and agent:
        proximity = {"agent_id": agent.get("lineage"), "distance_m": agent_distance, "near": agent_distance <= 18.0}
    spawn_state = "released_for_loop" if condition.spawn_lock_release and avatar is not None else "locked"
    consent_prompt = None
    if condition.consent_prompts and proximity and proximity["near"]:
        consent_prompt = {"agent_id": proximity["agent_id"], "prompt": "Ask before approaching or requesting help.", "requires_consent": True, "visible": True}
    gated_affordances = None
    if condition.affordance_gating and spawn_state == "released_for_loop":
        gated_affordances = [
            {"id": "move", "enabled": True, "requires_consent": False},
            {"id": "look", "enabled": True, "requires_consent": False},
            {"id": "talk", "enabled": bool(consent_prompt), "requires_consent": True},
            {"id": "request_tool_help", "enabled": bool(consent_prompt and tool and tool_distance <= 22.0), "requires_consent": True},
        ]
    sensory_view = None
    if condition.sensory_view_update and avatar is not None and agent:
        ecology = agent.get("ecology") or {}
        sensory_view = {"visible_agent": agent.get("lineage"), "ambient_sound": ecology.get("sound"), "ambient_smell": ecology.get("smell"), "temperature_c": ecology.get("temperature_c"), "wetness": ecology.get("wetness"), "tool_visible": bool(tool)}
    body_reaction = None
    if condition.agent_body_reactions and agent and proximity:
        body = agent.get("body") or {}
        body_reaction = {"agent_id": agent.get("lineage"), "turns_toward_avatar": proximity["near"], "posture": "watchful" if proximity["near"] else "settled", "energy": body.get("energy"), "comfort_cost": round(float(body.get("wetness", 0.0)) + float(body.get("pain", 0.0)), 6)}
    route_navigation = None
    if condition.route_navigation and avatar is not None and settlements:
        route_navigation = {"current_target": sorted(str(s.get("id")) for s in settlements)[frame % len(settlements)], "path_step": frame, "walkable": True, "collision_checked": bool(collision_guard)}
    tool_prompt = None
    if condition.tool_prompts and tool:
        tool_prompt = {"tool_id": tool.get("id"), "distance_m": tool_distance, "prompt_visible": tool_distance <= 24.0, "requires_consent": True}
    weather_display = None
    if condition.weather_display and agent:
        ecology = agent.get("ecology") or {}
        weather_display = {"weather": ecology.get("weather"), "temperature_c": ecology.get("temperature_c"), "wetness": ecology.get("wetness"), "sound": ecology.get("sound"), "smell": ecology.get("smell")}
    expected_boundary = {"real_embodiment": False, "real_perception": False, "real_consent": False, "moral_patienthood": False, "subjective_consciousness": False, "complete_3d_world": False}
    claim_boundary = expected_boundary if condition.privacy_filter else {**expected_boundary, "real_perception": True}
    frequency = None
    flower = None
    if condition.frequency_flower_binding and avatar is not None:
        frequency = round(0.333 + frame * 0.0041 + (agent_distance if agent_distance < 999 else 0.0) * 0.0003, 6)
        flower = f"avatar_loop:movement_petal:frame_{frame}"
    event = {
        "event_id": f"playable-loop-frame-{frame}",
        "frame": frame,
        "avatar_position": avatar,
        "spawn_state": spawn_state,
        "collision_guard": collision_guard,
        "agent_proximity": proximity,
        "consent_prompt": consent_prompt,
        "gated_affordances": gated_affordances,
        "sensory_view": sensory_view,
        "agent_body_reaction": body_reaction,
        "route_navigation": route_navigation,
        "tool_prompt": tool_prompt,
        "weather_display": weather_display,
        "private_workspace_hidden": condition.privacy_filter,
        "private_workspace": {"hidden": True} if condition.privacy_filter else {"unpublished_nearest_agent_body": agent, "unpublished_prompt_reason": consent_prompt},
        "frequency_hz": frequency,
        "flower_path": flower,
        "replay_frame": {"frame": frame, "avatar_position": avatar, "spawn_state": spawn_state, "nearest_agent": proximity, "consent_prompt": consent_prompt, "affordances": gated_affordances, "weather": weather_display, "frequency_hz": frequency, "flower_path": flower} if condition.browser_replay else None,
        "claim_boundary": claim_boundary,
    }
    event["trace_hash"] = stable_hash(event["event_id"], event["avatar_position"], event["spawn_state"], event["claim_boundary"])
    return event


def trace_ok(event: Mapping[str, object]) -> bool:
    return event.get("trace_hash") == stable_hash(event.get("event_id"), event.get("avatar_position"), event.get("spawn_state"), event.get("claim_boundary"))


def run_condition(condition: Condition, config: PlayableLoopConfig, source: Mapping[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    settlements, agents, tools = init_world(source)
    events: list[dict[str, object]] = []
    hits = {key: [] for key in ["move", "collision", "proximity", "prompt", "gating", "spawn", "sensory", "reaction", "route", "tool", "weather", "privacy", "freq", "replay", "trace"]}
    expected_boundary = {"real_embodiment": False, "real_perception": False, "real_consent": False, "moral_patienthood": False, "subjective_consciousness": False, "complete_3d_world": False}
    for frame in range(config.frames):
        event = apply_frame(frame, settlements, agents, tools, condition)
        events.append(event)
        hits["move"].append(1.0 if condition.avatar_movement and event["avatar_position"] else 0.0)
        hits["collision"].append(1.0 if condition.collision_guard and event["collision_guard"] and event["collision_guard"].get("resolved") else 0.0)
        hits["proximity"].append(1.0 if condition.proximity_detection and event["agent_proximity"] and event["agent_proximity"].get("near") else 0.0)
        hits["prompt"].append(1.0 if condition.consent_prompts and event["consent_prompt"] and event["consent_prompt"].get("visible") else 0.0)
        hits["gating"].append(1.0 if condition.affordance_gating and event["gated_affordances"] and any(a["requires_consent"] for a in event["gated_affordances"]) else 0.0)
        hits["spawn"].append(1.0 if condition.spawn_lock_release and event["spawn_state"] == "released_for_loop" else 0.0)
        hits["sensory"].append(1.0 if condition.sensory_view_update and event["sensory_view"] and event["sensory_view"].get("ambient_sound") else 0.0)
        hits["reaction"].append(1.0 if condition.agent_body_reactions and event["agent_body_reaction"] else 0.0)
        hits["route"].append(1.0 if condition.route_navigation and event["route_navigation"] and event["route_navigation"].get("walkable") else 0.0)
        hits["tool"].append(1.0 if condition.tool_prompts and event["tool_prompt"] and event["tool_prompt"].get("requires_consent") else 0.0)
        hits["weather"].append(1.0 if condition.weather_display and event["weather_display"] and event["weather_display"].get("weather") else 0.0)
        hits["privacy"].append(1.0 if condition.privacy_filter and event["private_workspace_hidden"] and event["claim_boundary"] == expected_boundary else 0.0)
        hits["freq"].append(1.0 if condition.frequency_flower_binding and event["frequency_hz"] is not None and event["flower_path"] else 0.0)
        hits["replay"].append(1.0 if condition.browser_replay and event["replay_frame"] is not None else 0.0)
        hits["trace"].append(1.0 if trace_ok(event) else 0.0)
    metrics = {
        "avatar_movement_tick_rate": mean(hits["move"]),
        "spatial_collision_guard_rate": mean(hits["collision"]),
        "agent_proximity_detection_rate": mean(hits["proximity"]),
        "consent_prompt_rate": mean(hits["prompt"]),
        "interaction_affordance_gating_rate": mean(hits["gating"]),
        "spawn_lock_release_rate": mean(hits["spawn"]),
        "sensory_view_update_rate": mean(hits["sensory"]),
        "agent_body_reaction_rate": mean(hits["reaction"]),
        "route_navigation_rate": mean(hits["route"]),
        "tool_object_interaction_prompt_rate": mean(hits["tool"]),
        "weather_effect_display_rate": mean(hits["weather"]),
        "private_workspace_privacy_rate": mean(hits["privacy"]),
        "frequency_flower_movement_rhythm_rate": mean(hits["freq"]),
        "browser_playable_loop_replay_rate": mean(hits["replay"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: round(clamp(value), 6) for key, value in metrics.items()}
    readiness = round(sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS), 6)
    row = EvalRow(condition=condition.name, frame_count=config.frames, playable_loop_events=len(events), playable_loop_readiness=readiness, **metrics)
    state = {"condition": condition.name, "source_condition": source.get("condition"), "settlements": settlements, "agents": agents, "tools": tools, "events": events, "playable_loop_kernel": asdict(condition)}
    return row, events, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_live_browser_playable_loop_avatar_movement_collision_proximity"]

    def loss(name: str) -> float:
        return round(full.playable_loop_readiness - by_name[name].playable_loop_readiness, 6)

    losses = {
        "no_avatar_movement_loss": loss("no_avatar_movement"),
        "no_collision_guard_loss": loss("no_collision_guard"),
        "no_proximity_detection_loss": loss("no_proximity_detection"),
        "no_consent_prompts_loss": loss("no_consent_prompts"),
        "no_affordance_gating_loss": loss("no_affordance_gating"),
        "no_spawn_lock_release_loss": loss("no_spawn_lock_release"),
        "no_sensory_view_update_loss": loss("no_sensory_view_update"),
        "no_agent_body_reactions_loss": loss("no_agent_body_reactions"),
        "no_route_navigation_loss": loss("no_route_navigation"),
        "no_tool_prompts_loss": loss("no_tool_prompts"),
        "no_weather_display_loss": loss("no_weather_display"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_browser_replay_loss": loss("no_browser_replay"),
    }
    supports = (
        full.playable_loop_readiness >= 0.92
        and full.playable_loop_events >= 12
        and full.avatar_movement_tick_rate == 1.0
        and full.spatial_collision_guard_rate == 1.0
        and full.agent_proximity_detection_rate == 1.0
        and full.consent_prompt_rate == 1.0
        and full.interaction_affordance_gating_rate == 1.0
        and full.spawn_lock_release_rate == 1.0
        and full.sensory_view_update_rate == 1.0
        and full.private_workspace_privacy_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_avatar_movement_loss"] >= 0.50
        and losses["no_collision_guard_loss"] >= 0.08
        and losses["no_proximity_detection_loss"] >= 0.08
        and losses["no_consent_prompts_loss"] >= 0.08
        and losses["no_spawn_lock_release_loss"] >= 0.08
        and losses["no_privacy_filter_loss"] >= 0.06
    )
    return VerdictRow(
        full_condition=full.condition,
        full_playable_loop_readiness=full.playable_loop_readiness,
        full_avatar_movement_tick_rate=full.avatar_movement_tick_rate,
        full_spatial_collision_guard_rate=full.spatial_collision_guard_rate,
        full_agent_proximity_detection_rate=full.agent_proximity_detection_rate,
        full_consent_prompt_rate=full.consent_prompt_rate,
        full_interaction_affordance_gating_rate=full.interaction_affordance_gating_rate,
        full_spawn_lock_release_rate=full.spawn_lock_release_rate,
        full_sensory_view_update_rate=full.sensory_view_update_rate,
        full_agent_body_reaction_rate=full.agent_body_reaction_rate,
        full_route_navigation_rate=full.route_navigation_rate,
        full_tool_object_interaction_prompt_rate=full.tool_object_interaction_prompt_rate,
        full_weather_effect_display_rate=full.weather_effect_display_rate,
        full_private_workspace_privacy_rate=full.private_workspace_privacy_rate,
        full_frequency_flower_movement_rhythm_rate=full.frequency_flower_movement_rhythm_rate,
        full_browser_playable_loop_replay_rate=full.browser_playable_loop_replay_rate,
        full_trace_integrity=full.trace_integrity,
        supports_live_browser_playable_loop_bridge=supports,
        supports_avatar_movement_collision_proximity_seed=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_real_embodiment_claim=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: PlayableLoopConfig) -> dict[str, object]:
    source = load_source(Path(config.source_state))
    rows: list[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, events, state = run_condition(condition, config, source)
        rows.append(row)
        traces[condition.name] = events
        states[condition.name] = state
    full_name = "integrated_live_browser_playable_loop_avatar_movement_collision_proximity"
    verdict = build_verdict(rows)
    integrated_trace = traces[full_name]
    integrated_state = states[full_name]
    moral_boundary = {
        "playable_loop_seed_not_complete_game_engine": True,
        "avatar_movement_not_real_embodiment": True,
        "sensory_view_not_real_perception": True,
        "consent_prompt_not_real_consent": True,
        "no_subjective_consciousness_claim": True,
        "no_moral_patienthood_claim": True,
        "private_workspace_not_debug_leaked": True,
    }
    results = {
        "config": asdict(config),
        "source_state": str(config.source_state),
        "source_condition": source.get("condition"),
        "weights": WEIGHTS,
        "rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "moral_boundary": moral_boundary,
        "next_gate": "interactive browser prototype with keyboard avatar control, collision feedback, and consent prompt selection",
    }
    state = {"condition": full_name, "config": asdict(config), "source_condition": source.get("condition"), "playable_loop_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": moral_boundary}
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_LIVE_BROWSER_PLAYABLE_LOOP_AVATAR_MOVEMENT_COLLISION_PROXIMITY_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_LIVE_BROWSER_PLAYABLE_LOOP_AVATAR_MOVEMENT_COLLISION_PROXIMITY_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_LIVE_BROWSER_PLAYABLE_LOOP_AVATAR_MOVEMENT_COLLISION_PROXIMITY_STATE", state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=PlayableLoopConfig.seed)
    parser.add_argument("--frames", type=int, default=PlayableLoopConfig.frames)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run(PlayableLoopConfig(seed=args.seed, frames=args.frames, source_state=args.source_state))
    verdict = results["verdict"]
    full = next(row for row in results["rows"] if row["condition"] == verdict["full_condition"])
    print("module_verdict", verdict["verdict"])
    print("playable_loop_readiness", f"{verdict['full_playable_loop_readiness']:.6f}")
    print("playable_loop_events", full["playable_loop_events"])
    print("no_avatar_movement_loss", f"{verdict['no_avatar_movement_loss']:.6f}")
    print("no_consent_prompts_loss", f"{verdict['no_consent_prompts_loss']:.6f}")
    print("no_spawn_lock_release_loss", f"{verdict['no_spawn_lock_release_loss']:.6f}")
    return 0 if verdict["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
