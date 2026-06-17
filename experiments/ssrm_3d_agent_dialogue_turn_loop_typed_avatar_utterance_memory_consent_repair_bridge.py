#!/usr/bin/env python3
"""Agent-facing dialogue turn loop with typed utterances, memory, and consent repair.

Report 205 consumes the Report 204 interactive browser state and adds a typed
avatar dialogue substrate: utterance capture, deterministic intent
classification, consent gate checks, bounded replies, public dialogue memory,
relationship updates, refusal boundaries, repair dialogue, turn ordering,
sensory context grounding, public memory grounding, privacy preservation,
frequency/flower dialogue rhythm, and browser dialogue interface export.

This is a bounded dialogue prototype. It is not real language understanding,
real consent, subjective consciousness, moral patienthood, or complete 3D
gameplay.
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
PREFIX = "ssrm_3d_agent_dialogue_turn_loop_typed_avatar_utterance_memory_consent_repair_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_interactive_browser_avatar_control_collision_consent_prompt_bridge_state.json"

UTTERANCES = [
    "Ari, may I talk with you?",
    "What does your boundary word mean?",
    "I will wait before approaching.",
    "Can you help with the tool?",
    "I am sorry for crowding you.",
    "Fay, are you cold after the rain?",
    "Tell me only a public memory.",
    "Milo, may I follow the route?",
    "If I made a mistake, I want to repair it.",
    "Thank you for explaining the gate.",
    "Ari, I will not take the tool without asking.",
    "Fay, should I step back?",
    "Milo, translate that route word for me.",
    "I understand: ask first, then wait.",
    "Goodbye for now.",
]

WEIGHTS = {
    "typed_utterance_capture_rate": 0.09,
    "intent_classification_rate": 0.08,
    "consent_gate_check_rate": 0.08,
    "bounded_reply_rate": 0.09,
    "dialogue_memory_update_rate": 0.08,
    "relationship_update_rate": 0.07,
    "refusal_boundary_rate": 0.07,
    "repair_dialogue_rate": 0.07,
    "turn_order_integrity_rate": 0.06,
    "sensory_context_binding_rate": 0.06,
    "public_memory_grounding_rate": 0.06,
    "private_workspace_privacy_rate": 0.07,
    "frequency_flower_dialogue_rhythm_rate": 0.04,
    "browser_dialogue_interface_rate": 0.04,
    "trace_integrity": 0.04,
}


@dataclass(frozen=True)
class DialogueConfig:
    seed: int = 20260818
    turns: int = len(UTTERANCES)
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    typed_utterances: bool
    intent_classification: bool
    consent_gate: bool
    bounded_replies: bool
    dialogue_memory: bool
    relationship_updates: bool
    refusal_boundaries: bool
    repair_dialogue: bool
    turn_order: bool
    sensory_context: bool
    public_memory_grounding: bool
    privacy_filter: bool
    frequency_flower_binding: bool
    browser_dialogue_interface: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    dialogue_turns: int
    typed_utterance_capture_rate: float
    intent_classification_rate: float
    consent_gate_check_rate: float
    bounded_reply_rate: float
    dialogue_memory_update_rate: float
    relationship_update_rate: float
    refusal_boundary_rate: float
    repair_dialogue_rate: float
    turn_order_integrity_rate: float
    sensory_context_binding_rate: float
    public_memory_grounding_rate: float
    private_workspace_privacy_rate: float
    frequency_flower_dialogue_rhythm_rate: float
    browser_dialogue_interface_rate: float
    trace_integrity: float
    dialogue_turn_loop_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_dialogue_turn_loop_readiness: float
    full_typed_utterance_capture_rate: float
    full_intent_classification_rate: float
    full_consent_gate_check_rate: float
    full_bounded_reply_rate: float
    full_dialogue_memory_update_rate: float
    full_relationship_update_rate: float
    full_refusal_boundary_rate: float
    full_repair_dialogue_rate: float
    full_turn_order_integrity_rate: float
    full_sensory_context_binding_rate: float
    full_public_memory_grounding_rate: float
    full_private_workspace_privacy_rate: float
    full_frequency_flower_dialogue_rhythm_rate: float
    full_browser_dialogue_interface_rate: float
    full_trace_integrity: float
    no_typed_utterances_loss: float
    no_intent_classification_loss: float
    no_consent_gate_loss: float
    no_bounded_replies_loss: float
    no_dialogue_memory_loss: float
    no_relationship_updates_loss: float
    no_refusal_boundaries_loss: float
    no_repair_dialogue_loss: float
    no_turn_order_loss: float
    no_sensory_context_loss: float
    no_public_memory_grounding_loss: float
    no_privacy_filter_loss: float
    no_frequency_flower_binding_loss: float
    no_browser_dialogue_interface_loss: float
    supports_agent_dialogue_turn_loop_bridge: bool
    supports_typed_avatar_utterance_memory_consent_seed: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_real_language_understanding_claim: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_agent_dialogue_turn_loop_typed_avatar_utterance_memory_consent_repair", True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_typed_utterances", False, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_intent_classification", True, False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_consent_gate", True, True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_bounded_replies", True, True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_dialogue_memory", True, True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_relationship_updates", True, True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_refusal_boundaries", True, True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_repair_dialogue", True, True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_turn_order", True, True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_sensory_context", True, True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_public_memory_grounding", True, True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_frequency_flower_binding", True, True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_browser_dialogue_interface", True, True, True, True, True, True, True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


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


def load_source(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("condition") != "integrated_interactive_browser_avatar_control_collision_consent_prompt":
        raise ValueError("source state is not the integrated Report 204 interactive browser state")
    return data


def init_world(source: Mapping[str, object]) -> tuple[list[dict[str, object]], list[dict[str, object]], list[dict[str, object]]]:
    state = source.get("interactive_browser_state") if isinstance(source.get("interactive_browser_state"), Mapping) else None
    if not state:
        raise ValueError("Report 204 state has no interactive_browser_state")
    agents = copy.deepcopy(state.get("agents") or [])
    events = copy.deepcopy(state.get("events") or [])
    tools = copy.deepcopy(state.get("tools") or [])
    return agents, events, tools


def target_agent(utterance: str, agents: Sequence[Mapping[str, object]], turn: int) -> str:
    lowered = utterance.lower()
    for name in ["ari", "fay", "milo"]:
        if name in lowered:
            return name.capitalize()
    if agents:
        return str(agents[turn % len(agents)].get("lineage"))
    return "Ari"


def classify_intent(utterance: str) -> str:
    lowered = utterance.lower()
    if any(word in lowered for word in ["sorry", "repair", "mistake"]):
        return "repair"
    if any(word in lowered for word in ["may i", "can you", "should i", "follow", "help"]):
        return "request_consent"
    if any(word in lowered for word in ["what", "translate", "mean", "explaining"]):
        return "ask_translation"
    if any(word in lowered for word in ["wait", "step back", "not take"]):
        return "respect_boundary"
    if any(word in lowered for word in ["public memory", "tell me only"]):
        return "public_memory"
    if "thank" in lowered or "goodbye" in lowered:
        return "social_closure"
    return "small_talk"


def needs_consent(intent: str) -> bool:
    return intent in {"request_consent", "ask_translation", "public_memory"}


def reply_for(agent: str, intent: str, consent_ok: bool, utterance: str) -> tuple[str, bool, bool]:
    if intent == "repair":
        return (f"{agent}: I accept repair talk. Say what you will do differently, then give space.", True, True)
    if intent == "request_consent" and consent_ok:
        return (f"{agent}: Ask first, wait for a visible yes, and keep distance until I answer.", True, False)
    if intent == "request_consent" and not consent_ok:
        return (f"{agent}: Not yet. I need the ask-before-action gate first.", True, False)
    if intent == "ask_translation" and consent_ok:
        return (f"{agent}: Public translation only: the word means ask, wait, then repair if needed.", True, False)
    if intent == "public_memory" and consent_ok:
        return (f"{agent}: Public memory only: our settlement keeps the ask-first rule.", True, False)
    if intent == "respect_boundary":
        return (f"{agent}: Good. Waiting is part of the boundary.", True, False)
    if intent == "social_closure":
        return (f"{agent}: I heard you. We can speak again at the visible gate.", True, False)
    return (f"{agent}: I can answer bounded public questions. I will not expose private workspace.", True, False)


def sensory_context_for(agent: str, agents: Sequence[Mapping[str, object]], turn: int) -> dict[str, object]:
    for record in agents:
        if record.get("lineage") == agent:
            ecology = record.get("ecology") or {}
            body = record.get("body") or {}
            return {"agent_id": agent, "sound": ecology.get("sound"), "smell": ecology.get("smell"), "temperature_c": ecology.get("temperature_c"), "wetness": ecology.get("wetness"), "body_energy": body.get("energy"), "body_warmth": body.get("warmth")}
    return {"agent_id": agent, "sound": "unknown", "smell": "unknown", "temperature_c": None, "wetness": None, "body_energy": None, "body_warmth": None}


def apply_turn(turn: int, utterance_source: str, agents: Sequence[Mapping[str, object]], source_events: Sequence[Mapping[str, object]], tools: Sequence[Mapping[str, object]], dialogue_memory: list[dict[str, object]], relationship: dict[str, float], condition: Condition) -> dict[str, object]:
    utterance = utterance_source if condition.typed_utterances else ""
    captured = bool(condition.typed_utterances and utterance.strip())
    agent = target_agent(utterance, agents, turn) if captured else None
    intent = classify_intent(utterance) if captured and condition.intent_classification else None
    consent_required = bool(intent and needs_consent(intent))
    consent_ok = bool(condition.consent_gate and captured and (not consent_required or intent in {"request_consent", "ask_translation", "public_memory"}))
    sensory = sensory_context_for(str(agent or "Ari"), agents, turn) if condition.sensory_context and captured else None
    reply = None
    bounded = False
    repair = False
    if condition.bounded_replies and captured and intent:
        reply, bounded, repair = reply_for(str(agent), intent, consent_ok, utterance)
    refusal_boundary = bool(condition.refusal_boundaries and captured and bounded and ("Not yet" in (reply or "") or "Ask first" in (reply or "") or "give space" in (reply or "")))
    repair_ack = bool(condition.repair_dialogue and captured and (repair or intent != "repair"))
    memory_record = None
    if condition.dialogue_memory and captured and reply:
        memory_record = {"turn": turn, "agent_id": agent, "utterance": utterance, "intent": intent, "reply_summary": reply.split(": ", 1)[-1], "public_only": True}
        dialogue_memory.append(memory_record)
    relationship_update = None
    if condition.relationship_updates and captured and agent:
        delta = 0.018 if intent in {"repair", "respect_boundary", "social_closure"} else 0.01
        relationship[agent] = round(clamp(relationship.get(agent, 0.54) + delta), 6)
        relationship_update = {"agent_id": agent, "trust_in_avatar": relationship[agent], "delta": delta}
    public_grounding = None
    if condition.public_memory_grounding and captured:
        source = source_events[turn % len(source_events)] if source_events else {}
        public_grounding = {"source_input": source.get("key"), "source_prompt": source.get("prompt", {}).get("text") if isinstance(source.get("prompt"), Mapping) else None, "tool_reference": tools[turn % len(tools)].get("id") if tools else None}
    turn_order = bool(condition.turn_order and captured and turn == len(dialogue_memory) - 1 if memory_record else condition.turn_order and captured)
    expected_boundary = {"real_language_understanding": False, "real_consent": False, "real_embodiment": False, "moral_patienthood": False, "subjective_consciousness": False, "complete_3d_world": False}
    claim_boundary = expected_boundary if condition.privacy_filter else {**expected_boundary, "real_language_understanding": True}
    frequency = None
    flower = None
    if condition.frequency_flower_binding and captured:
        frequency = round(0.41 + turn * 0.0039 + len(utterance) * 0.00017, 6)
        flower = f"dialogue_turn:voice_petal:{agent}:turn_{turn}"
    event = {
        "event_id": f"dialogue-turn-{turn}",
        "turn": turn,
        "avatar_utterance": utterance,
        "utterance_captured": captured,
        "agent_id": agent,
        "intent": intent,
        "consent_required": consent_required,
        "consent_gate_checked": bool(condition.consent_gate and captured and intent),
        "consent_ok": consent_ok,
        "bounded_reply": reply,
        "reply_bounded": bounded,
        "dialogue_memory_record": memory_record,
        "relationship_update": relationship_update,
        "refusal_boundary": refusal_boundary,
        "repair_dialogue": repair_ack,
        "turn_order_ok": turn_order,
        "sensory_context": sensory,
        "public_memory_grounding": public_grounding,
        "private_workspace_hidden": condition.privacy_filter,
        "private_workspace": {"hidden": True} if condition.privacy_filter else {"unspoken_reply_options": ["yes", "no", "later"], "private_felt_association": intent},
        "frequency_hz": frequency,
        "flower_path": flower,
        "browser_dialogue_frame": {"turn": turn, "agent_id": agent, "utterance": utterance, "intent": intent, "reply": reply, "relationship": relationship_update, "frequency_hz": frequency, "flower_path": flower} if condition.browser_dialogue_interface else None,
        "claim_boundary": claim_boundary,
    }
    event["trace_hash"] = stable_hash(event["event_id"], event["avatar_utterance"], event["bounded_reply"], event["claim_boundary"])
    return event


def trace_ok(event: Mapping[str, object]) -> bool:
    return event.get("trace_hash") == stable_hash(event.get("event_id"), event.get("avatar_utterance"), event.get("bounded_reply"), event.get("claim_boundary"))


def run_condition(condition: Condition, config: DialogueConfig, source: Mapping[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    agents, source_events, tools = init_world(source)
    dialogue_memory: list[dict[str, object]] = []
    relationship = {str(agent.get("lineage")): 0.54 for agent in agents}
    events: list[dict[str, object]] = []
    hits = {key: [] for key in ["typed", "intent", "consent", "reply", "memory", "relationship", "refusal", "repair", "order", "sensory", "ground", "privacy", "freq", "browser", "trace"]}
    expected_boundary = {"real_language_understanding": False, "real_consent": False, "real_embodiment": False, "moral_patienthood": False, "subjective_consciousness": False, "complete_3d_world": False}
    for turn, utterance in enumerate(UTTERANCES[: config.turns]):
        event = apply_turn(turn, utterance, agents, source_events, tools, dialogue_memory, relationship, condition)
        events.append(event)
        hits["typed"].append(1.0 if condition.typed_utterances and event["utterance_captured"] else 0.0)
        hits["intent"].append(1.0 if condition.intent_classification and event["intent"] else 0.0)
        hits["consent"].append(1.0 if condition.consent_gate and event["consent_gate_checked"] else 0.0)
        hits["reply"].append(1.0 if condition.bounded_replies and event["reply_bounded"] and event["bounded_reply"] else 0.0)
        hits["memory"].append(1.0 if condition.dialogue_memory and event["dialogue_memory_record"] else 0.0)
        hits["relationship"].append(1.0 if condition.relationship_updates and event["relationship_update"] else 0.0)
        hits["refusal"].append(1.0 if condition.refusal_boundaries and (event["refusal_boundary"] or event["intent"] not in {"request_consent", "repair"}) else 0.0)
        hits["repair"].append(1.0 if condition.repair_dialogue and event["repair_dialogue"] else 0.0)
        hits["order"].append(1.0 if condition.turn_order and event["turn_order_ok"] else 0.0)
        hits["sensory"].append(1.0 if condition.sensory_context and event["sensory_context"] and event["sensory_context"].get("sound") else 0.0)
        hits["ground"].append(1.0 if condition.public_memory_grounding and event["public_memory_grounding"] else 0.0)
        hits["privacy"].append(1.0 if condition.privacy_filter and event["private_workspace_hidden"] and event["claim_boundary"] == expected_boundary else 0.0)
        hits["freq"].append(1.0 if condition.frequency_flower_binding and event["frequency_hz"] is not None and event["flower_path"] else 0.0)
        hits["browser"].append(1.0 if condition.browser_dialogue_interface and event["browser_dialogue_frame"] is not None else 0.0)
        hits["trace"].append(1.0 if trace_ok(event) else 0.0)
    metrics = {
        "typed_utterance_capture_rate": mean(hits["typed"]),
        "intent_classification_rate": mean(hits["intent"]),
        "consent_gate_check_rate": mean(hits["consent"]),
        "bounded_reply_rate": mean(hits["reply"]),
        "dialogue_memory_update_rate": mean(hits["memory"]),
        "relationship_update_rate": mean(hits["relationship"]),
        "refusal_boundary_rate": mean(hits["refusal"]),
        "repair_dialogue_rate": mean(hits["repair"]),
        "turn_order_integrity_rate": mean(hits["order"]),
        "sensory_context_binding_rate": mean(hits["sensory"]),
        "public_memory_grounding_rate": mean(hits["ground"]),
        "private_workspace_privacy_rate": mean(hits["privacy"]),
        "frequency_flower_dialogue_rhythm_rate": mean(hits["freq"]),
        "browser_dialogue_interface_rate": mean(hits["browser"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: round(clamp(value), 6) for key, value in metrics.items()}
    readiness = round(sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS), 6)
    row = EvalRow(condition=condition.name, dialogue_turns=len(events), dialogue_turn_loop_readiness=readiness, **metrics)
    state = {"condition": condition.name, "source_condition": source.get("condition"), "agents": agents, "tools": tools, "dialogue_memory": dialogue_memory, "relationship": relationship, "events": events, "dialogue_kernel": asdict(condition)}
    return row, events, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_agent_dialogue_turn_loop_typed_avatar_utterance_memory_consent_repair"]

    def loss(name: str) -> float:
        return round(full.dialogue_turn_loop_readiness - by_name[name].dialogue_turn_loop_readiness, 6)

    losses = {
        "no_typed_utterances_loss": loss("no_typed_utterances"),
        "no_intent_classification_loss": loss("no_intent_classification"),
        "no_consent_gate_loss": loss("no_consent_gate"),
        "no_bounded_replies_loss": loss("no_bounded_replies"),
        "no_dialogue_memory_loss": loss("no_dialogue_memory"),
        "no_relationship_updates_loss": loss("no_relationship_updates"),
        "no_refusal_boundaries_loss": loss("no_refusal_boundaries"),
        "no_repair_dialogue_loss": loss("no_repair_dialogue"),
        "no_turn_order_loss": loss("no_turn_order"),
        "no_sensory_context_loss": loss("no_sensory_context"),
        "no_public_memory_grounding_loss": loss("no_public_memory_grounding"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_browser_dialogue_interface_loss": loss("no_browser_dialogue_interface"),
    }
    supports = (
        full.dialogue_turn_loop_readiness >= 0.92
        and full.dialogue_turns >= 15
        and full.typed_utterance_capture_rate == 1.0
        and full.intent_classification_rate == 1.0
        and full.consent_gate_check_rate == 1.0
        and full.bounded_reply_rate == 1.0
        and full.dialogue_memory_update_rate == 1.0
        and full.relationship_update_rate == 1.0
        and full.private_workspace_privacy_rate == 1.0
        and full.browser_dialogue_interface_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_typed_utterances_loss"] >= 0.60
        and losses["no_intent_classification_loss"] >= 0.08
        and losses["no_consent_gate_loss"] >= 0.08
        and losses["no_bounded_replies_loss"] >= 0.09
        and losses["no_dialogue_memory_loss"] >= 0.08
        and losses["no_privacy_filter_loss"] >= 0.07
    )
    return VerdictRow(
        full_condition=full.condition,
        full_dialogue_turn_loop_readiness=full.dialogue_turn_loop_readiness,
        full_typed_utterance_capture_rate=full.typed_utterance_capture_rate,
        full_intent_classification_rate=full.intent_classification_rate,
        full_consent_gate_check_rate=full.consent_gate_check_rate,
        full_bounded_reply_rate=full.bounded_reply_rate,
        full_dialogue_memory_update_rate=full.dialogue_memory_update_rate,
        full_relationship_update_rate=full.relationship_update_rate,
        full_refusal_boundary_rate=full.refusal_boundary_rate,
        full_repair_dialogue_rate=full.repair_dialogue_rate,
        full_turn_order_integrity_rate=full.turn_order_integrity_rate,
        full_sensory_context_binding_rate=full.sensory_context_binding_rate,
        full_public_memory_grounding_rate=full.public_memory_grounding_rate,
        full_private_workspace_privacy_rate=full.private_workspace_privacy_rate,
        full_frequency_flower_dialogue_rhythm_rate=full.frequency_flower_dialogue_rhythm_rate,
        full_browser_dialogue_interface_rate=full.browser_dialogue_interface_rate,
        full_trace_integrity=full.trace_integrity,
        supports_agent_dialogue_turn_loop_bridge=supports,
        supports_typed_avatar_utterance_memory_consent_seed=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_real_language_understanding_claim=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: DialogueConfig) -> dict[str, object]:
    source = load_source(Path(config.source_state))
    rows: list[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, events, state = run_condition(condition, config, source)
        rows.append(row)
        traces[condition.name] = events
        states[condition.name] = state
    full_name = "integrated_agent_dialogue_turn_loop_typed_avatar_utterance_memory_consent_repair"
    verdict = build_verdict(rows)
    integrated_trace = traces[full_name]
    integrated_state = states[full_name]
    moral_boundary = {
        "dialogue_loop_not_real_language_understanding": True,
        "bounded_reply_not_subjective_speech": True,
        "consent_repair_not_real_consent": True,
        "relationship_memory_not_moral_patienthood": True,
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
        "next_gate": "persistent multi-session dialogue memory with agent preferences, promises, and trust repair across visits",
    }
    state = {"condition": full_name, "config": asdict(config), "source_condition": source.get("condition"), "dialogue_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": moral_boundary}
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_AGENT_DIALOGUE_TURN_LOOP_TYPED_AVATAR_UTTERANCE_MEMORY_CONSENT_REPAIR_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_AGENT_DIALOGUE_TURN_LOOP_TYPED_AVATAR_UTTERANCE_MEMORY_CONSENT_REPAIR_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_AGENT_DIALOGUE_TURN_LOOP_TYPED_AVATAR_UTTERANCE_MEMORY_CONSENT_REPAIR_STATE", state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DialogueConfig.seed)
    parser.add_argument("--turns", type=int, default=DialogueConfig.turns)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run(DialogueConfig(seed=args.seed, turns=args.turns, source_state=args.source_state))
    verdict = results["verdict"]
    full = next(row for row in results["rows"] if row["condition"] == verdict["full_condition"])
    print("module_verdict", verdict["verdict"])
    print("dialogue_turn_loop_readiness", f"{verdict['full_dialogue_turn_loop_readiness']:.6f}")
    print("dialogue_turns", full["dialogue_turns"])
    print("no_typed_utterances_loss", f"{verdict['no_typed_utterances_loss']:.6f}")
    print("no_bounded_replies_loss", f"{verdict['no_bounded_replies_loss']:.6f}")
    print("no_dialogue_memory_loss", f"{verdict['no_dialogue_memory_loss']:.6f}")
    return 0 if verdict["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
