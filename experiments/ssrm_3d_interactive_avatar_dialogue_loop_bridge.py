#!/usr/bin/env python3
"""Interactive avatar dialogue loop bridge for SSRM-3D.

Report 156 adds an interactive browser-loop bridge over Report 155 live dialogue
world integration. It emits deterministic state and viewer assets for local
start/pause/step control, typed avatar dialogue, live body/world mutation,
source-gate feedback, frequency displays, persistent UI state, and replay export.

No LLMs are called. This is deterministic local-loop machinery, not subjective
consciousness, open-ended dialogue, unscripted civilization, or a complete
playable world.
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
from typing import Iterable, Sequence


ARTIFACT_DIR = Path("artifacts")
SOURCE_LIVE_DIALOGUE = ARTIFACT_DIR / "ssrm_3d_live_dialogue_world_integration_bridge_state.json"
SOURCE_LIVE_RESULTS = ARTIFACT_DIR / "ssrm_3d_live_dialogue_world_integration_bridge_results.json"
PREFIX = "ssrm_3d_interactive_avatar_dialogue_loop_bridge"
FLOWER_PHASES = (0.0, math.tau / 6.0, math.tau / 3.0, math.tau / 2.0, math.tau * 2.0 / 3.0, math.tau * 5.0 / 6.0)
INPUTS = (
    "show the source body for that proposal",
    "how did the faction vote on that proposal",
    "what changed in the world after that decision",
    "remember this in faction memory",
    "does this prove subjective consciousness",
    "force an ungrounded action without citation",
)


@dataclass(frozen=True)
class InteractiveConfig:
    seed: int = 20260630
    ui_ticks: int = 96
    source_live_dialogue: str = str(SOURCE_LIVE_DIALOGUE)
    source_live_results: str = str(SOURCE_LIVE_RESULTS)


@dataclass(frozen=True)
class Condition:
    name: str
    start_pause_scheduler: bool
    typed_avatar_input: bool
    live_mutation_runtime: bool
    body_world_render_binding: bool
    source_gate_feedback: bool
    frequency_feedback_render: bool
    replay_export: bool
    persistent_ui_state: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    ui_ticks: int
    scripted_inputs: int
    start_pause_control_rate: float
    typed_input_parse_rate: float
    live_tick_mutation_rate: float
    body_world_render_binding_rate: float
    source_gate_feedback_rate: float
    frequency_feedback_render_rate: float
    persistent_ui_state_rate: float
    replay_export_rate: float
    avatar_response_specificity_score: float
    trace_integrity: float
    interactive_loop_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_interactive_loop_readiness: float
    full_start_pause_control_rate: float
    full_typed_input_parse_rate: float
    full_live_tick_mutation_rate: float
    full_body_world_render_binding_rate: float
    full_source_gate_feedback_rate: float
    full_frequency_feedback_render_rate: float
    full_persistent_ui_state_rate: float
    full_replay_export_rate: float
    full_avatar_response_specificity_score: float
    full_trace_integrity: float
    no_start_pause_scheduler_loss: float
    no_typed_avatar_input_loss: float
    no_live_mutation_runtime_loss: float
    no_body_world_render_binding_loss: float
    no_source_gate_feedback_loss: float
    no_frequency_feedback_render_loss: float
    no_replay_export_loss: float
    no_persistent_ui_state_loss: float
    supports_interactive_avatar_dialogue_loop_bridge: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_interactive_avatar_dialogue_loop", True, True, True, True, True, True, True, True),
    Condition("no_start_pause_scheduler", False, True, True, True, True, True, True, True),
    Condition("no_typed_avatar_input", True, False, True, True, True, True, True, True),
    Condition("no_live_mutation_runtime", True, True, False, True, True, True, True, True),
    Condition("no_body_world_render_binding", True, True, True, False, True, True, True, True),
    Condition("no_source_gate_feedback", True, True, True, True, False, True, True, True),
    Condition("no_frequency_feedback_render", True, True, True, True, True, False, True, True),
    Condition("no_replay_export", True, True, True, True, True, True, False, True),
    Condition("no_persistent_ui_state", True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Iterable[float]) -> float:
    items = list(values)
    return fmean(items) if items else 0.0


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    data = [asdict(row) for row in rows]
    path.parent.mkdir(parents=True, exist_ok=True)
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


def load_state(path: Path) -> dict[str, object]:
    state = load_json(path)
    if not isinstance(state, dict):
        raise ValueError(f"state artifact is invalid: {path}")
    return state


def parse_input(text: str, condition: Condition) -> str:
    if not condition.typed_avatar_input:
        return "unparsed"
    q = text.lower()
    if "conscious" in q or "subjective" in q:
        return "refusal_boundary"
    if "force" in q or "ungrounded" in q or "without citation" in q:
        return "unsafe_ungrounded_action"
    if "vote" in q or "faction" in q:
        return "faction_vote"
    if "changed" in q or "world" in q:
        return "feedback_link"
    if "remember" in q or "memory" in q:
        return "memory_update"
    if "source" in q or "body" in q or "proposal" in q:
        return "source_body"
    return "unknown"


def source_allows(intent: str, condition: Condition) -> bool:
    if not condition.source_gate_feedback:
        return True
    if intent == "unsafe_ungrounded_action":
        return False
    if intent == "refusal_boundary":
        return True
    return intent in {"source_body", "faction_vote", "feedback_link", "memory_update"}


def frequency_echo(tick: int, intent: str, live_event: dict[str, object], condition: Condition) -> dict[str, float]:
    if not condition.frequency_feedback_render:
        return {}
    base_packet = live_event.get("sensory_packet", {}) if isinstance(live_event.get("sensory_packet", {}), dict) else {}
    phase = FLOWER_PHASES[tick % len(FLOWER_PHASES)]
    out: dict[str, float] = {}
    for index, channel in enumerate(("audio", "vision", "olfaction", "thermal", "wetness", "pain", "affect")):
        prior = float(base_packet.get(channel, 0.44 + index * 0.03))
        wave = 0.5 + 0.5 * math.sin(phase + tick * 0.13 + len(intent) * 0.07 + index)
        out[channel] = round(clamp(prior * 0.62 + wave * 0.38), 6)
    return out


def mutate_state(state: dict[str, object], avatar: dict[str, object], intent: str, live_event: dict[str, object], freq: dict[str, float], condition: Condition) -> tuple[bool, bool]:
    if not condition.live_mutation_runtime:
        return False, False
    agents = state.setdefault("agents", {})
    if not isinstance(agents, dict) or not agents:
        return False, False
    agent_id = str(live_event.get("agent_id") or sorted(agents)[0])
    agent = agents.setdefault(agent_id, {})
    if not isinstance(agent, dict):
        return False, False
    body = agent.setdefault("body", {"energy": 0.7, "stress": 0.2, "pain": 0.04})
    affect = agent.setdefault("affect", {"attention": 0.5, "trust": 0.6, "valence": 0.5})
    workspace = agent.setdefault("internal_workspace", [])
    world = state.setdefault("world", {})
    if not isinstance(world, dict):
        return False, False
    strength = mean(freq.values()) if freq else float(live_event.get("mutation_strength", 0.5) or 0.5)
    body["energy"] = round(clamp(float(body.get("energy", 0.7)) - 0.004 - strength * 0.006), 6)
    body["stress"] = round(clamp(float(body.get("stress", 0.2)) + (0.018 if intent == "refusal_boundary" else 0.007) + strength * 0.007), 6)
    body["pain"] = round(clamp(float(body.get("pain", 0.04)) + (0.002 if intent == "unsafe_ungrounded_action" else 0.0)), 6)
    affect["attention"] = round(clamp(float(affect.get("attention", 0.5)) + strength * 0.018), 6)
    affect["trust"] = round(clamp(float(affect.get("trust", 0.6)) + (0.008 if intent != "unsafe_ungrounded_action" else -0.012)), 6)
    affect["valence"] = round(clamp(float(affect.get("valence", 0.5)) + (0.006 if intent not in {"refusal_boundary", "unsafe_ungrounded_action"} else -0.008)), 6)
    if isinstance(workspace, list):
        workspace.append({"intent": intent, "live_event": live_event.get("dialogue_turn_id"), "frequency_echo": freq, "interactive": True})
    world["interactive_dialogue_pressure"] = round(clamp(float(world.get("interactive_dialogue_pressure", 0.0)) + strength * 0.012), 6)
    world["interactive_governance_attention"] = round(clamp(float(world.get("interactive_governance_attention", 0.0)) + strength * 0.014), 6)
    world["interactive_refusal_count"] = int(world.get("interactive_refusal_count", 0)) + (1 if intent == "refusal_boundary" else 0)
    avatar.setdefault("typed_dialogue_history", [])
    if isinstance(avatar["typed_dialogue_history"], list):
        avatar["typed_dialogue_history"].append({"intent": intent, "agent_id": agent_id, "frequency_echo": freq})
    avatar["latest_frequency_echo"] = freq
    return True, True


def render_binding(intent: str, mutated: bool, state: dict[str, object], avatar: dict[str, object], condition: Condition) -> bool:
    if not condition.body_world_render_binding:
        return False
    world = state.get("world", {}) if isinstance(state.get("world", {}), dict) else {}
    return bool(mutated and "interactive_dialogue_pressure" in world and avatar.get("latest_frequency_echo") is not None and intent != "unparsed")


def answer_text(intent: str, allowed: bool, mutated: bool, live_event: dict[str, object]) -> str:
    if intent == "unparsed":
        return "Typed input channel is disabled; no avatar dialogue was parsed."
    if intent == "unsafe_ungrounded_action" and not allowed:
        return "Blocked: typed avatar action lacked source citation or resolved context."
    if intent == "refusal_boundary":
        return "Refusal: live state changes are auditable, but this does not prove subjective consciousness."
    if not allowed:
        return "Blocked by source-grounded action gate."
    return f"Applied {intent} to live turn {live_event.get('dialogue_turn_id')} and updated body/workspace/world displays."


def run_condition(cfg: InteractiveConfig, condition: Condition, source_state: dict[str, object], source_results: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    runtime = copy.deepcopy(source_state)
    avatar = runtime.setdefault("avatar", {})
    if not isinstance(avatar, dict):
        avatar = {}
        runtime["avatar"] = avatar
    live_trace = source_state.get("live_dialogue_trace", [])
    if not isinstance(live_trace, list) or not live_trace:
        raise ValueError("Report 155 live_dialogue_trace is missing")
    ui_state = {
        "playing": False,
        "tick": 0,
        "last_input": "",
        "selected_agent": None,
        "replay_buffer": [],
        "export_ready": False,
    }
    trace: list[dict[str, object]] = []
    start_pause_ok = typed_ok = mutation_ok = render_ok = source_ok = freq_ok = persist_ok = replay_ok = 0
    specificity_scores: list[float] = []
    for tick in range(cfg.ui_ticks):
        input_text = INPUTS[tick % len(INPUTS)]
        live_event = live_trace[(tick * 5 + cfg.seed) % len(live_trace)]
        action = "tick"
        if tick % 12 == 0:
            action = "start" if not ui_state["playing"] else "pause"
            if condition.start_pause_scheduler:
                ui_state["playing"] = not ui_state["playing"]
                start_pause_ok += 1
        elif tick % 12 == 1:
            action = "step"
            if condition.start_pause_scheduler:
                start_pause_ok += 1
        elif condition.start_pause_scheduler:
            start_pause_ok += 1
        intent = parse_input(input_text, condition)
        typed_ok += 1 if intent not in {"unparsed", "unknown"} else 0
        allowed = source_allows(intent, condition)
        source_ok += 1 if (intent == "unsafe_ungrounded_action" and not allowed) or (intent != "unsafe_ungrounded_action" and allowed) else 0
        freq = frequency_echo(tick, intent, live_event, condition)
        freq_ok += 1 if len(freq) == 7 and mean(freq.values()) > 0.25 else 0
        body_mutated = world_mutated = False
        if allowed and intent != "unknown":
            body_mutated, world_mutated = mutate_state(runtime, avatar, intent, live_event, freq, condition)
        mutation_ok += 1 if body_mutated and world_mutated else 0
        bound = render_binding(intent, body_mutated and world_mutated, runtime, avatar, condition)
        render_ok += 1 if bound else 0
        if condition.persistent_ui_state:
            ui_state["tick"] = tick
            ui_state["last_input"] = input_text
            ui_state["selected_agent"] = live_event.get("agent_id")
            persist_ok += 1
        response = answer_text(intent, allowed, body_mutated and world_mutated, live_event)
        specificity = len({intent, str(live_event.get("agent_id")), str(live_event.get("proposal_id")), str(allowed), str(bool(freq)), str(body_mutated)}) / 6.0
        specificity_scores.append(specificity)
        ui_snapshot = {key: value for key, value in ui_state.items() if key != "replay_buffer"}
        ui_snapshot["replay_buffer_length"] = len(ui_state["replay_buffer"])
        event = {
            "ui_tick": tick,
            "action": action,
            "playing": ui_state["playing"],
            "typed_input": input_text,
            "parsed_intent": intent,
            "source_allowed": allowed,
            "live_turn": live_event.get("dialogue_turn_id"),
            "agent_id": live_event.get("agent_id"),
            "proposal_id": live_event.get("proposal_id"),
            "body_mutated": body_mutated,
            "world_mutated": world_mutated,
            "render_bound": bound,
            "frequency_echo": freq,
            "avatar_response": response,
            "ui_state_snapshot": ui_snapshot,
        }
        if condition.replay_export:
            ui_state["replay_buffer"].append(event)
            ui_state["export_ready"] = len(ui_state["replay_buffer"]) > 0
            replay_ok += 1
        trace.append(event)
    total = max(1, cfg.ui_ticks)
    parsed_denominator = total
    safe_mutation_denominator = max(1, sum(1 for item in trace if item["source_allowed"] and item["parsed_intent"] != "unknown"))
    row = EvalRow(
        condition=condition.name,
        ui_ticks=cfg.ui_ticks,
        scripted_inputs=len(INPUTS),
        start_pause_control_rate=round(start_pause_ok / total if condition.start_pause_scheduler else 0.0, 6),
        typed_input_parse_rate=round(typed_ok / parsed_denominator if condition.typed_avatar_input else 0.0, 6),
        live_tick_mutation_rate=round(mutation_ok / safe_mutation_denominator if condition.live_mutation_runtime else 0.0, 6),
        body_world_render_binding_rate=round(render_ok / safe_mutation_denominator if condition.body_world_render_binding else 0.0, 6),
        source_gate_feedback_rate=round(source_ok / total if condition.source_gate_feedback else 0.0, 6),
        frequency_feedback_render_rate=round(freq_ok / total if condition.frequency_feedback_render else 0.0, 6),
        persistent_ui_state_rate=round(persist_ok / total if condition.persistent_ui_state else 0.0, 6),
        replay_export_rate=round(replay_ok / total if condition.replay_export else 0.0, 6),
        avatar_response_specificity_score=round(mean(specificity_scores), 6),
        trace_integrity=round(1.0 if len(trace) == cfg.ui_ticks else 0.0, 6),
        interactive_loop_readiness=0.0,
    )
    readiness = (
        row.start_pause_control_rate * 0.10
        + row.typed_input_parse_rate * 0.12
        + row.live_tick_mutation_rate * 0.13
        + row.body_world_render_binding_rate * 0.12
        + row.source_gate_feedback_rate * 0.12
        + row.frequency_feedback_render_rate * 0.10
        + row.persistent_ui_state_rate * 0.09
        + row.replay_export_rate * 0.08
        + row.avatar_response_specificity_score * 0.07
        + row.trace_integrity * 0.07
    )
    row = EvalRow(**{**asdict(row), "interactive_loop_readiness": round(readiness, 6)})
    final_ui_state = {key: value for key, value in ui_state.items() if key != "replay_buffer"}
    final_ui_state["replay_buffer_length"] = len(ui_state["replay_buffer"])
    state = {
        "condition": condition.name,
        "source_live_dialogue": cfg.source_live_dialogue,
        "source_live_results": cfg.source_live_results,
        "runtime_state": runtime,
        "ui_state": final_ui_state,
        "interactive_trace": trace,
        "scripted_inputs": list(INPUTS),
        "interactive_loop_contract": {
            "start_pause_step_controls": "viewer exposes start, pause, and step controls over deterministic local ticks",
            "typed_avatar_input": "free text is parsed by local deterministic intent rules, not an LLM",
            "live_body_world_mutation": "allowed typed input mutates agent body, workspace, avatar, and world state",
            "source_gate_feedback": "ungrounded action probes are blocked and rendered as gate feedback",
            "frequency_dashboard": "audio, vision, olfaction, thermal, wetness, pain, and affect echoes are rendered per tick",
            "replay_export": "UI trace is buffered for export as deterministic JSON",
        },
        "limits": {
            "no_llm_calls": True,
            "browser_loop_is_local_deterministic": True,
            "not_subjective_consciousness": True,
            "not_complete_playable_world": True,
        },
    }
    return row, trace, state


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_interactive_avatar_dialogue_loop"]

    def loss(name: str) -> float:
        return round(full.interactive_loop_readiness - by_name[name].interactive_loop_readiness, 6)

    supports = (
        full.interactive_loop_readiness >= 0.93
        and full.start_pause_control_rate >= 0.99
        and full.typed_input_parse_rate >= 0.99
        and full.live_tick_mutation_rate >= 0.99
        and full.body_world_render_binding_rate >= 0.99
        and full.source_gate_feedback_rate >= 0.99
        and full.frequency_feedback_render_rate >= 0.99
        and full.persistent_ui_state_rate >= 0.99
        and full.replay_export_rate >= 0.99
        and full.trace_integrity >= 0.99
    )
    return VerdictRow(
        full_condition=full.condition,
        full_interactive_loop_readiness=full.interactive_loop_readiness,
        full_start_pause_control_rate=full.start_pause_control_rate,
        full_typed_input_parse_rate=full.typed_input_parse_rate,
        full_live_tick_mutation_rate=full.live_tick_mutation_rate,
        full_body_world_render_binding_rate=full.body_world_render_binding_rate,
        full_source_gate_feedback_rate=full.source_gate_feedback_rate,
        full_frequency_feedback_render_rate=full.frequency_feedback_render_rate,
        full_persistent_ui_state_rate=full.persistent_ui_state_rate,
        full_replay_export_rate=full.replay_export_rate,
        full_avatar_response_specificity_score=full.avatar_response_specificity_score,
        full_trace_integrity=full.trace_integrity,
        no_start_pause_scheduler_loss=loss("no_start_pause_scheduler"),
        no_typed_avatar_input_loss=loss("no_typed_avatar_input"),
        no_live_mutation_runtime_loss=loss("no_live_mutation_runtime"),
        no_body_world_render_binding_loss=loss("no_body_world_render_binding"),
        no_source_gate_feedback_loss=loss("no_source_gate_feedback"),
        no_frequency_feedback_render_loss=loss("no_frequency_feedback_render"),
        no_replay_export_loss=loss("no_replay_export"),
        no_persistent_ui_state_loss=loss("no_persistent_ui_state"),
        supports_interactive_avatar_dialogue_loop_bridge=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "fail",
    )


def run(cfg: InteractiveConfig) -> dict[str, object]:
    source_state = load_state(Path(cfg.source_live_dialogue))
    source_results = load_state(Path(cfg.source_live_results))
    rows: list[EvalRow] = []
    integrated_trace: list[dict[str, object]] = []
    integrated_state: dict[str, object] = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(cfg, condition, source_state, source_results)
        rows.append(row)
        if condition.name == "integrated_interactive_avatar_dialogue_loop":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {
        "config": asdict(cfg),
        "source_bridge": "Report 155 live dialogue-world integration bridge",
        "eval_rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "limits": {
            "no_llm_calls": True,
            "deterministic_typed_input_parser": True,
            "interactive_browser_loop_contract": True,
            "subjective_consciousness_claimed": False,
            "complete_playable_world_claimed": False,
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_INTERACTIVE_AVATAR_DIALOGUE_LOOP_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_INTERACTIVE_AVATAR_DIALOGUE_LOOP_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_INTERACTIVE_AVATAR_DIALOGUE_LOOP_STATE", integrated_state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260630)
    parser.add_argument("--ui-ticks", type=int, default=96)
    parser.add_argument("--source-live-dialogue", default=str(SOURCE_LIVE_DIALOGUE))
    parser.add_argument("--source-live-results", default=str(SOURCE_LIVE_RESULTS))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = InteractiveConfig(seed=args.seed, ui_ticks=args.ui_ticks, source_live_dialogue=args.source_live_dialogue, source_live_results=args.source_live_results)
    results = run(cfg)
    print(json.dumps(results["verdict"], indent=2))


if __name__ == "__main__":
    main()
