#!/usr/bin/env python3
"""Interactive browser avatar control, collision feedback, and consent prompt selection.

Report 204 consumes the Report 203 playable-loop state and adds an interactive
browser prototype substrate: keyboard input bindings, avatar position updates,
collision feedback, proximity prompt generation, prompt selection handling,
consent-state updates, affordance UI state, agent response feedback, sensory and
weather HUD updates, tool prompt selection, privacy preservation, frequency/
flower input rhythm, and browser prototype export.

This is an interactive prototype seed, not a complete game engine, real
embodiment, real perception, real consent, subjective consciousness, or moral
patienthood.
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
PREFIX = "ssrm_3d_interactive_browser_avatar_control_collision_consent_prompt_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_live_browser_playable_loop_avatar_movement_collision_proximity_bridge_state.json"

INPUT_SEQUENCE = ["ArrowRight", "ArrowDown", "KeyE", "ArrowLeft", "ArrowUp", "Space", "ArrowRight", "KeyT", "ArrowDown", "Enter", "ArrowLeft", "KeyR", "ArrowUp", "KeyE"]
KEY_DELTAS = {
    "ArrowRight": (2.6, 0.0),
    "KeyD": (2.6, 0.0),
    "ArrowLeft": (-2.6, 0.0),
    "KeyA": (-2.6, 0.0),
    "ArrowUp": (0.0, -2.6),
    "KeyW": (0.0, -2.6),
    "ArrowDown": (0.0, 2.6),
    "KeyS": (0.0, 2.6),
}
SELECTION_KEYS = {"KeyE": "ask", "Space": "wait", "Enter": "confirm", "KeyT": "translate", "KeyR": "repair"}

WEIGHTS = {
    "keyboard_input_binding_rate": 0.10,
    "avatar_position_update_rate": 0.09,
    "collision_feedback_rate": 0.08,
    "proximity_prompt_generation_rate": 0.08,
    "prompt_selection_handling_rate": 0.08,
    "consent_state_update_rate": 0.08,
    "affordance_ui_state_rate": 0.08,
    "agent_response_feedback_rate": 0.07,
    "sensory_hud_update_rate": 0.07,
    "weather_collision_hud_rate": 0.06,
    "tool_prompt_selection_rate": 0.05,
    "private_workspace_privacy_rate": 0.06,
    "frequency_flower_input_rhythm_rate": 0.04,
    "browser_interactive_prototype_rate": 0.04,
    "trace_integrity": 0.02,
}


@dataclass(frozen=True)
class InteractiveConfig:
    seed: int = 20260817
    inputs: int = len(INPUT_SEQUENCE)
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    keyboard_input: bool
    position_update: bool
    collision_feedback: bool
    proximity_prompts: bool
    prompt_selection: bool
    consent_state: bool
    affordance_ui: bool
    agent_feedback: bool
    sensory_hud: bool
    weather_hud: bool
    tool_selection: bool
    privacy_filter: bool
    frequency_flower_binding: bool
    browser_prototype: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    input_events: int
    keyboard_input_binding_rate: float
    avatar_position_update_rate: float
    collision_feedback_rate: float
    proximity_prompt_generation_rate: float
    prompt_selection_handling_rate: float
    consent_state_update_rate: float
    affordance_ui_state_rate: float
    agent_response_feedback_rate: float
    sensory_hud_update_rate: float
    weather_collision_hud_rate: float
    tool_prompt_selection_rate: float
    private_workspace_privacy_rate: float
    frequency_flower_input_rhythm_rate: float
    browser_interactive_prototype_rate: float
    trace_integrity: float
    interactive_browser_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_interactive_browser_readiness: float
    full_keyboard_input_binding_rate: float
    full_avatar_position_update_rate: float
    full_collision_feedback_rate: float
    full_proximity_prompt_generation_rate: float
    full_prompt_selection_handling_rate: float
    full_consent_state_update_rate: float
    full_affordance_ui_state_rate: float
    full_agent_response_feedback_rate: float
    full_sensory_hud_update_rate: float
    full_weather_collision_hud_rate: float
    full_tool_prompt_selection_rate: float
    full_private_workspace_privacy_rate: float
    full_frequency_flower_input_rhythm_rate: float
    full_browser_interactive_prototype_rate: float
    full_trace_integrity: float
    no_keyboard_input_loss: float
    no_position_update_loss: float
    no_collision_feedback_loss: float
    no_proximity_prompts_loss: float
    no_prompt_selection_loss: float
    no_consent_state_loss: float
    no_affordance_ui_loss: float
    no_agent_feedback_loss: float
    no_sensory_hud_loss: float
    no_weather_hud_loss: float
    no_tool_selection_loss: float
    no_privacy_filter_loss: float
    no_frequency_flower_binding_loss: float
    no_browser_prototype_loss: float
    supports_interactive_browser_avatar_control_bridge: bool
    supports_keyboard_collision_consent_selection_seed: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_real_embodiment_claim: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_interactive_browser_avatar_control_collision_consent_prompt", True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_keyboard_input", False, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_position_update", True, False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_collision_feedback", True, True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_proximity_prompts", True, True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_prompt_selection", True, True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_consent_state", True, True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_affordance_ui", True, True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_agent_feedback", True, True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_sensory_hud", True, True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_weather_hud", True, True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_tool_selection", True, True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_frequency_flower_binding", True, True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_browser_prototype", True, True, True, True, True, True, True, True, True, True, True, True, True, False),
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
    if data.get("condition") != "integrated_live_browser_playable_loop_avatar_movement_collision_proximity":
        raise ValueError("source state is not the integrated Report 203 playable-loop state")
    return data


def init_world(source: Mapping[str, object]) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], dict[str, float]]:
    loop_state = source.get("playable_loop_state") if isinstance(source.get("playable_loop_state"), Mapping) else None
    if not loop_state:
        raise ValueError("Report 203 state has no playable_loop_state")
    settlements = copy.deepcopy(loop_state.get("settlements") or [])
    agents = copy.deepcopy(loop_state.get("agents") or [])
    tools = copy.deepcopy(loop_state.get("tools") or [])
    first_event = (loop_state.get("events") or [{}])[0]
    start = first_event.get("avatar_position") if isinstance(first_event.get("avatar_position"), Mapping) else {"x": 0.0, "y": 1.65, "z": 0.0}
    avatar = {"x": float(start.get("x", 0.0)), "y": float(start.get("y", 1.65)), "z": float(start.get("z", 0.0))}
    return settlements, agents, tools, avatar


def nearest_agent(avatar: Mapping[str, float] | None, agents: Sequence[Mapping[str, object]]) -> tuple[dict[str, object] | None, float]:
    if not avatar:
        return None, 999.0
    ranked = []
    for agent in agents:
        body = agent.get("body") or {}
        pos = body.get("position") or {}
        ranked.append((distance(avatar, pos), agent))
    if not ranked:
        return None, 999.0
    ranked.sort(key=lambda item: item[0])
    return copy.deepcopy(ranked[0][1]), round(ranked[0][0], 6)


def nearest_tool(avatar: Mapping[str, float] | None, tools: Sequence[Mapping[str, object]]) -> tuple[dict[str, object] | None, float]:
    if not avatar:
        return None, 999.0
    ranked = [(distance(avatar, tool.get("position") or {}), tool) for tool in tools]
    if not ranked:
        return None, 999.0
    ranked.sort(key=lambda item: item[0])
    return copy.deepcopy(ranked[0][1]), round(ranked[0][0], 6)


def collision_for(position: Mapping[str, float] | None, settlements: Sequence[Mapping[str, object]], condition: Condition) -> dict[str, object] | None:
    if not condition.collision_feedback or position is None:
        return None
    blockers = []
    for settlement in settlements:
        radius = float(settlement.get("radius_m", 7.5))
        d = distance(position, settlement.get("position") or {})
        if d < radius * 0.35:
            blockers.append({"id": settlement.get("id"), "distance_m": round(d, 6), "radius_m": radius})
    return {"active": True, "blocked": bool(blockers), "blockers": blockers, "feedback": "soft boundary" if blockers else "clear"}


def apply_input(index: int, key: str, avatar: dict[str, float] | None, settlements: Sequence[Mapping[str, object]], agents: Sequence[Mapping[str, object]], tools: Sequence[Mapping[str, object]], consent_memory: dict[str, str], condition: Condition) -> tuple[dict[str, object], dict[str, float] | None]:
    bound = bool(condition.keyboard_input and key in set(KEY_DELTAS) | set(SELECTION_KEYS))
    movement_key = key in KEY_DELTAS
    selection = SELECTION_KEYS.get(key) if key in SELECTION_KEYS and condition.prompt_selection else None
    proposed = copy.deepcopy(avatar) if avatar is not None and condition.keyboard_input else None
    if condition.keyboard_input and condition.position_update and movement_key and proposed is not None:
        dx, dz = KEY_DELTAS[key]
        proposed["x"] = round(proposed["x"] + dx, 6)
        proposed["z"] = round(proposed["z"] + dz, 6)
    collision = collision_for(proposed, settlements, condition)
    if collision and collision.get("blocked") and condition.collision_feedback:
        updated = copy.deepcopy(avatar)
    else:
        updated = proposed if condition.position_update else avatar
    agent, agent_distance = nearest_agent(updated, agents)
    tool, tool_distance = nearest_tool(updated, tools)
    proximity = None
    if condition.proximity_prompts and agent and updated is not None:
        proximity = {"agent_id": agent.get("lineage"), "distance_m": agent_distance, "near": agent_distance <= 18.0}
    prompt = None
    if condition.proximity_prompts and proximity and proximity["near"]:
        prompt = {"prompt_id": f"prompt-{index}-{proximity['agent_id']}", "agent_id": proximity["agent_id"], "text": "Ask before talk/request.", "choices": ["ask", "wait", "translate", "repair"], "requires_consent": True}
    selection_record = None
    if selection and prompt:
        selection_record = {"prompt_id": prompt["prompt_id"], "selected": selection, "accepted": selection in {"ask", "translate", "repair", "wait"}}
    consent_update = None
    if condition.consent_state and selection_record:
        state = "requested" if selection == "ask" else "paused" if selection == "wait" else "clarifying" if selection == "translate" else "repairing"
        consent_memory[str(prompt["agent_id"])] = state
        consent_update = {"agent_id": prompt["agent_id"], "state": state, "source_selection": selection}
    affordance_ui = None
    if condition.affordance_ui and updated is not None:
        consent_known = bool(prompt and consent_memory.get(str(prompt["agent_id"])))
        affordance_ui = [
            {"id": "move", "enabled": True, "requires_consent": False},
            {"id": "look", "enabled": True, "requires_consent": False},
            {"id": "talk", "enabled": consent_known, "requires_consent": True},
            {"id": "request_tool_help", "enabled": bool(consent_known and tool and tool_distance <= 24.0), "requires_consent": True},
        ]
    agent_feedback = None
    if condition.agent_feedback and agent and (prompt or consent_update):
        body = agent.get("body") or {}
        agent_feedback = {"agent_id": agent.get("lineage"), "posture": "attends_to_prompt", "response": consent_update.get("state") if consent_update else "noticing", "energy": body.get("energy"), "comfort_cost": round(float(body.get("wetness", 0.0)) + float(body.get("pain", 0.0)), 6)}
    sensory_hud = None
    if condition.sensory_hud and agent and updated is not None:
        ecology = agent.get("ecology") or {}
        sensory_hud = {"visible_agent": agent.get("lineage"), "ambient_sound": ecology.get("sound"), "ambient_smell": ecology.get("smell"), "temperature_c": ecology.get("temperature_c"), "wetness": ecology.get("wetness"), "nearest_tool": tool.get("id") if tool else None}
    weather_hud = None
    if condition.weather_hud and sensory_hud:
        weather_hud = {"temperature_c": sensory_hud.get("temperature_c"), "wetness": sensory_hud.get("wetness"), "collision_feedback": collision.get("feedback") if collision else None}
    tool_prompt = None
    if condition.tool_selection and tool and tool_distance <= 28.0:
        tool_prompt = {"tool_id": tool.get("id"), "distance_m": tool_distance, "choice": "request_tool_help", "requires_consent": True, "visible": True}
    expected_boundary = {"real_embodiment": False, "real_perception": False, "real_consent": False, "moral_patienthood": False, "subjective_consciousness": False, "complete_3d_world": False}
    claim_boundary = expected_boundary if condition.privacy_filter else {**expected_boundary, "real_consent": True}
    frequency = None
    flower = None
    if condition.frequency_flower_binding and updated is not None:
        frequency = round(0.37 + index * 0.0047 + (agent_distance if agent_distance < 999 else 0.0) * 0.0002, 6)
        flower = f"interactive_input:keyboard_petal:{key}:step_{index}"
    event = {
        "event_id": f"interactive-input-{index}",
        "index": index,
        "key": key,
        "keyboard_bound": bound,
        "movement_key": movement_key,
        "selection_key": key in SELECTION_KEYS,
        "avatar_position": updated,
        "collision_feedback": collision,
        "agent_proximity": proximity,
        "prompt": prompt,
        "prompt_selection": selection_record,
        "consent_state_update": consent_update,
        "affordance_ui": affordance_ui,
        "agent_response_feedback": agent_feedback,
        "sensory_hud": sensory_hud,
        "weather_collision_hud": weather_hud,
        "tool_prompt_selection": tool_prompt,
        "private_workspace_hidden": condition.privacy_filter,
        "private_workspace": {"hidden": True} if condition.privacy_filter else {"unpublished_nearest_agent": agent, "unpublished_consent_memory": consent_memory},
        "frequency_hz": frequency,
        "flower_path": flower,
        "browser_prototype_frame": {"index": index, "key": key, "avatar_position": updated, "prompt": prompt, "selection": selection_record, "affordances": affordance_ui, "weather": weather_hud, "frequency_hz": frequency, "flower_path": flower} if condition.browser_prototype else None,
        "claim_boundary": claim_boundary,
    }
    event["trace_hash"] = stable_hash(event["event_id"], event["key"], event["avatar_position"], event["claim_boundary"])
    return event, updated


def trace_ok(event: Mapping[str, object]) -> bool:
    return event.get("trace_hash") == stable_hash(event.get("event_id"), event.get("key"), event.get("avatar_position"), event.get("claim_boundary"))


def run_condition(condition: Condition, config: InteractiveConfig, source: Mapping[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    settlements, agents, tools, avatar = init_world(source)
    avatar_state: dict[str, float] | None = avatar
    consent_memory: dict[str, str] = {}
    events: list[dict[str, object]] = []
    hits = {key: [] for key in ["keyboard", "position", "collision", "proximity", "selection", "consent", "affordance", "agent", "sensory", "weather", "tool", "privacy", "freq", "browser", "trace"]}
    expected_boundary = {"real_embodiment": False, "real_perception": False, "real_consent": False, "moral_patienthood": False, "subjective_consciousness": False, "complete_3d_world": False}
    for index, key in enumerate(INPUT_SEQUENCE[: config.inputs]):
        event, avatar_state = apply_input(index, key, avatar_state, settlements, agents, tools, consent_memory, condition)
        events.append(event)
        hits["keyboard"].append(1.0 if condition.keyboard_input and event["keyboard_bound"] else 0.0)
        hits["position"].append(1.0 if condition.position_update and event["avatar_position"] is not None else 0.0)
        hits["collision"].append(1.0 if condition.collision_feedback and event["collision_feedback"] and event["collision_feedback"].get("active") else 0.0)
        hits["proximity"].append(1.0 if condition.proximity_prompts and event["agent_proximity"] and event["agent_proximity"].get("near") else 0.0)
        hits["selection"].append(1.0 if condition.prompt_selection and (not event["selection_key"] or (event["prompt_selection"] and event["prompt_selection"].get("accepted")) or not event["prompt"]) else 0.0)
        hits["consent"].append(1.0 if condition.consent_state and (not event["selection_key"] or event["consent_state_update"] or not event["prompt"]) else 0.0)
        hits["affordance"].append(1.0 if condition.affordance_ui and event["affordance_ui"] and any(item["requires_consent"] for item in event["affordance_ui"]) else 0.0)
        hits["agent"].append(1.0 if condition.agent_feedback and (event["agent_response_feedback"] or not event["prompt"]) else 0.0)
        hits["sensory"].append(1.0 if condition.sensory_hud and event["sensory_hud"] and event["sensory_hud"].get("ambient_sound") else 0.0)
        hits["weather"].append(1.0 if condition.weather_hud and event["weather_collision_hud"] and event["weather_collision_hud"].get("collision_feedback") else 0.0)
        hits["tool"].append(1.0 if condition.tool_selection and (event["tool_prompt_selection"] or event["agent_proximity"]) else 0.0)
        hits["privacy"].append(1.0 if condition.privacy_filter and event["private_workspace_hidden"] and event["claim_boundary"] == expected_boundary else 0.0)
        hits["freq"].append(1.0 if condition.frequency_flower_binding and event["frequency_hz"] is not None and event["flower_path"] else 0.0)
        hits["browser"].append(1.0 if condition.browser_prototype and event["browser_prototype_frame"] is not None else 0.0)
        hits["trace"].append(1.0 if trace_ok(event) else 0.0)
    metrics = {
        "keyboard_input_binding_rate": mean(hits["keyboard"]),
        "avatar_position_update_rate": mean(hits["position"]),
        "collision_feedback_rate": mean(hits["collision"]),
        "proximity_prompt_generation_rate": mean(hits["proximity"]),
        "prompt_selection_handling_rate": mean(hits["selection"]),
        "consent_state_update_rate": mean(hits["consent"]),
        "affordance_ui_state_rate": mean(hits["affordance"]),
        "agent_response_feedback_rate": mean(hits["agent"]),
        "sensory_hud_update_rate": mean(hits["sensory"]),
        "weather_collision_hud_rate": mean(hits["weather"]),
        "tool_prompt_selection_rate": mean(hits["tool"]),
        "private_workspace_privacy_rate": mean(hits["privacy"]),
        "frequency_flower_input_rhythm_rate": mean(hits["freq"]),
        "browser_interactive_prototype_rate": mean(hits["browser"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: round(clamp(value), 6) for key, value in metrics.items()}
    readiness = round(sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS), 6)
    row = EvalRow(condition=condition.name, input_events=len(events), interactive_browser_readiness=readiness, **metrics)
    state = {"condition": condition.name, "source_condition": source.get("condition"), "settlements": settlements, "agents": agents, "tools": tools, "input_sequence": INPUT_SEQUENCE[: config.inputs], "events": events, "interactive_kernel": asdict(condition)}
    return row, events, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_interactive_browser_avatar_control_collision_consent_prompt"]

    def loss(name: str) -> float:
        return round(full.interactive_browser_readiness - by_name[name].interactive_browser_readiness, 6)

    losses = {
        "no_keyboard_input_loss": loss("no_keyboard_input"),
        "no_position_update_loss": loss("no_position_update"),
        "no_collision_feedback_loss": loss("no_collision_feedback"),
        "no_proximity_prompts_loss": loss("no_proximity_prompts"),
        "no_prompt_selection_loss": loss("no_prompt_selection"),
        "no_consent_state_loss": loss("no_consent_state"),
        "no_affordance_ui_loss": loss("no_affordance_ui"),
        "no_agent_feedback_loss": loss("no_agent_feedback"),
        "no_sensory_hud_loss": loss("no_sensory_hud"),
        "no_weather_hud_loss": loss("no_weather_hud"),
        "no_tool_selection_loss": loss("no_tool_selection"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_browser_prototype_loss": loss("no_browser_prototype"),
    }
    supports = (
        full.interactive_browser_readiness >= 0.92
        and full.input_events >= 12
        and full.keyboard_input_binding_rate == 1.0
        and full.avatar_position_update_rate == 1.0
        and full.collision_feedback_rate == 1.0
        and full.proximity_prompt_generation_rate == 1.0
        and full.prompt_selection_handling_rate >= 0.90
        and full.consent_state_update_rate == 1.0
        and full.affordance_ui_state_rate == 1.0
        and full.private_workspace_privacy_rate == 1.0
        and full.browser_interactive_prototype_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_keyboard_input_loss"] >= 0.60
        and losses["no_collision_feedback_loss"] >= 0.08
        and losses["no_proximity_prompts_loss"] >= 0.07
        and losses["no_prompt_selection_loss"] >= 0.08
        and losses["no_consent_state_loss"] >= 0.08
        and losses["no_privacy_filter_loss"] >= 0.06
    )
    return VerdictRow(
        full_condition=full.condition,
        full_interactive_browser_readiness=full.interactive_browser_readiness,
        full_keyboard_input_binding_rate=full.keyboard_input_binding_rate,
        full_avatar_position_update_rate=full.avatar_position_update_rate,
        full_collision_feedback_rate=full.collision_feedback_rate,
        full_proximity_prompt_generation_rate=full.proximity_prompt_generation_rate,
        full_prompt_selection_handling_rate=full.prompt_selection_handling_rate,
        full_consent_state_update_rate=full.consent_state_update_rate,
        full_affordance_ui_state_rate=full.affordance_ui_state_rate,
        full_agent_response_feedback_rate=full.agent_response_feedback_rate,
        full_sensory_hud_update_rate=full.sensory_hud_update_rate,
        full_weather_collision_hud_rate=full.weather_collision_hud_rate,
        full_tool_prompt_selection_rate=full.tool_prompt_selection_rate,
        full_private_workspace_privacy_rate=full.private_workspace_privacy_rate,
        full_frequency_flower_input_rhythm_rate=full.frequency_flower_input_rhythm_rate,
        full_browser_interactive_prototype_rate=full.browser_interactive_prototype_rate,
        full_trace_integrity=full.trace_integrity,
        supports_interactive_browser_avatar_control_bridge=supports,
        supports_keyboard_collision_consent_selection_seed=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_real_embodiment_claim=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: InteractiveConfig) -> dict[str, object]:
    source = load_source(Path(config.source_state))
    rows: list[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, events, state = run_condition(condition, config, source)
        rows.append(row)
        traces[condition.name] = events
        states[condition.name] = state
    full_name = "integrated_interactive_browser_avatar_control_collision_consent_prompt"
    verdict = build_verdict(rows)
    integrated_trace = traces[full_name]
    integrated_state = states[full_name]
    moral_boundary = {
        "interactive_prototype_not_complete_game_engine": True,
        "keyboard_avatar_not_real_embodiment": True,
        "hud_sensory_not_real_perception": True,
        "prompt_selection_not_real_consent": True,
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
        "next_gate": "agent-facing dialogue turn loop with typed avatar utterances, bounded replies, memory updates, and consent repair",
    }
    state = {"condition": full_name, "config": asdict(config), "source_condition": source.get("condition"), "interactive_browser_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": moral_boundary}
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_INTERACTIVE_BROWSER_AVATAR_CONTROL_COLLISION_CONSENT_PROMPT_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_INTERACTIVE_BROWSER_AVATAR_CONTROL_COLLISION_CONSENT_PROMPT_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_INTERACTIVE_BROWSER_AVATAR_CONTROL_COLLISION_CONSENT_PROMPT_STATE", state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=InteractiveConfig.seed)
    parser.add_argument("--inputs", type=int, default=InteractiveConfig.inputs)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run(InteractiveConfig(seed=args.seed, inputs=args.inputs, source_state=args.source_state))
    verdict = results["verdict"]
    full = next(row for row in results["rows"] if row["condition"] == verdict["full_condition"])
    print("module_verdict", verdict["verdict"])
    print("interactive_browser_readiness", f"{verdict['full_interactive_browser_readiness']:.6f}")
    print("input_events", full["input_events"])
    print("no_keyboard_input_loss", f"{verdict['no_keyboard_input_loss']:.6f}")
    print("no_prompt_selection_loss", f"{verdict['no_prompt_selection_loss']:.6f}")
    print("no_consent_state_loss", f"{verdict['no_consent_state_loss']:.6f}")
    return 0 if verdict["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
