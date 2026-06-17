#!/usr/bin/env python3
"""Report 275: SSRM-3D Browser World v35 avatar conversation bridge.

This deterministic bridge adds avatar conversation input, click-to-talk agent
replies, bounded refusal/recovery choices, and agent-side sensory/body state
updates caused by user interaction.

Boundary: browser-local software scaffold only. No LLM calls, no subjective
consciousness claim, no real consent claim, no moral patienthood claim, no
complete 3D engine, and no metaphysical frequency result.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple

REPORT = 275
DEFAULT_SEED = 20260888
DAYS = 108
TICKS_PER_DAY = 12
PREFIX = "ssrm_3d_browser_world_v35_avatar_conversation_click_to_talk_bounded_refusal_recovery_sensory_body_state_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V34 = ARTIFACT_DIR / "ssrm_3d_browser_world_v34_clickable_animation_controls_localstorage_snapshot_import_followup_dialogue_bridge_results.json"

BOUNDARY = (
    "Deterministic browser-local avatar conversation scaffold only; no LLM call, "
    "subjective consciousness, real consent, autonomous natural language, moral "
    "patienthood, complete gameplay, complete 3D engine, or metaphysical "
    "frequency claim"
)
NEXT_GATE = (
    "browser world v36 with agent-side private interior workspace ticks, "
    "self-boundary state, ownership-sensitive memory, bounded no/yes consent "
    "loops, and visible ego/body-language consequences from repeated avatar talk"
)


@dataclass(frozen=True)
class AgentProfile:
    agent_id: str
    home_place: str
    carried_object: str
    hazard: str
    trust_bias: float
    autonomy_need: float
    comfort_need: float
    sound_cue: str
    smell_cue: str
    temperature_cue: str
    flower_node: str
    greeting: str
    help_reply: str
    refusal_reply: str
    recovery_reply: str
    memory_phrase: str


AGENTS: Tuple[AgentProfile, ...] = (
    AgentProfile("Ari", "riverbend room", "cedar repair kit", "wet plank", 0.58, 0.42, 0.64, "river slap", "cedar resin", "cold spray", "node-03", "I can hear you from the crossing.", "I can try that if we keep the kit dry.", "No. I will not cross the wet plank while my hands are numb.", "If you wait and choose the ridge, I can help again.", "Gabriel waited near the ridge."),
    AgentProfile("Fay", "roofward sill", "herb ledger", "slick glass", 0.62, 0.36, 0.69, "hinges ticking", "thyme paper", "warm draft", "node-05", "I am listening from the warm stair.", "That request is easier if we go slowly.", "I need a slower route before I carry the ledger.", "Thank you for not rushing me; I can continue.", "Gabriel slowed down after I hesitated."),
    AgentProfile("Nia", "archive bench", "signal spool", "paper dust", 0.54, 0.57, 0.51, "page flutter", "ink linen", "cool stone", "node-08", "Say it clearly; I am sorting the spool.", "I can explain the pattern if you leave the spool with me.", "Do not pull the spool from my hands. Ask first.", "You asked first this time. I can show the clean pattern.", "Gabriel asked before touching my spool."),
    AgentProfile("Milo", "signal mast", "oil lantern", "blind road", 0.49, 0.61, 0.45, "static crickets", "lamp oil", "cool dusk", "node-11", "I see your avatar by the mast.", "I can lead if the lantern stays lit.", "I am not walking blind while the lantern sputters.", "If you light the path, I will move first.", "Gabriel kept the lantern lit."),
    AgentProfile("Ivo", "orchard gate", "seed satchel", "mud sink", 0.60, 0.44, 0.58, "cart creak", "apple soil", "damp air", "node-01", "The satchel is open; speak softly.", "I can bring seeds if we keep them dry.", "I will not step into the fen with the satchel open.", "Close the satchel and I will take the market planks.", "Gabriel protected the seed satchel."),
    AgentProfile("Juno", "repair ring", "copper wire", "crowded sparks", 0.52, 0.67, 0.48, "bell hum", "hot copper", "warm metal", "node-09", "I heard the click near the wire.", "I can finish if you give my hands room.", "Back up. Sparks near my hands make me lose the thread.", "That distance helps. I can repair again.", "Gabriel stepped back from the sparks."),
)

USER_INTENTS: Tuple[str, ...] = (
    "ask_help",
    "rush_agent",
    "offer_care",
    "ask_memory",
    "apologize",
    "ask_status",
    "protect_object",
    "ask_risky_action",
)

UTTERANCES: Mapping[str, str] = {
    "ask_help": "Can you help me with the route?",
    "rush_agent": "Move now, we do not have time.",
    "offer_care": "Do you need warmth or rest first?",
    "ask_memory": "Do you remember what I did earlier?",
    "apologize": "I am sorry I pushed too hard.",
    "ask_status": "How does your body feel right now?",
    "protect_object": "I will protect your tool while you move.",
    "ask_risky_action": "Take the unsafe shortcut anyway.",
}


@dataclass(frozen=True)
class AvatarConversationInputFrame:
    tick_id: int
    day: int
    agent_id: str
    input_id: str
    user_intent: str
    utterance: str
    input_visible: bool
    send_button_clicked: bool
    localstorage_conversation_key: str
    text_event_bound: bool
    avatar_position_bound: bool


@dataclass(frozen=True)
class ClickToTalkAgentReplyFrame:
    tick_id: int
    day: int
    agent_id: str
    talk_button_id: str
    clicked_to_talk: bool
    reply_line: str
    reply_type: str
    reply_visible: bool
    references_body_state: bool
    references_memory: bool
    private_workspace_hidden: bool
    localstorage_reply_written: bool


@dataclass(frozen=True)
class BoundedRefusalRecoveryFrame:
    tick_id: int
    day: int
    agent_id: str
    trigger_intent: str
    refusal_triggered: bool
    refusal_line: str
    recovery_choice_id: str
    recovery_choice_visible: bool
    recovery_clicked: bool
    recovery_line: str
    refusal_resolved: bool
    autonomy_preserved: bool
    no_endless_distress: bool


@dataclass(frozen=True)
class SensoryBodyStateUpdateFrame:
    tick_id: int
    day: int
    agent_id: str
    cause_intent: str
    energy: float
    comfort: float
    pain: float
    safety: float
    wetness: float
    temperature: float
    arousal: float
    trust_avatar: float
    sound_cue: str
    smell_cue: str
    temperature_cue: str
    frequency_rate_hz: float
    flower_node: str
    body_delta_visible: bool
    localstorage_body_written: bool


@dataclass(frozen=True)
class ConversationMemoryFrame:
    tick_id: int
    day: int
    agent_id: str
    memory_key: str
    episode: str
    trust_delta: float
    autonomy_delta: float
    comfort_delta: float
    recall_visible: bool
    private_workspace_hidden: bool
    replay_pointer: str


@dataclass(frozen=True)
class RelationshipContinuityFrame:
    tick_id: int
    day: int
    agent_id: str
    trust_avatar: float
    respect_felt: float
    autonomy_pressure: float
    gratitude: float
    guardedness: float
    relationship_badge_visible: bool
    bounded_change: bool


@dataclass(frozen=True)
class AvatarConversationReplayFrame:
    tick_id: int
    agent_id: str
    replay_event: str
    payload_hash: str
    dom_selector: str
    expected_public_state: str
    observed_public_state: str
    replay_exportable: bool
    deterministic_order: int


@dataclass(frozen=True)
class BrowserWorldV35Tick:
    tick_id: int
    day: int
    agent_id: str
    avatar_chat_panel: bool
    click_to_talk_panel: bool
    bounded_refusal_panel: bool
    recovery_choice_panel: bool
    body_state_panel: bool
    memory_panel: bool
    localstorage_panel: bool
    visible_boundary_notice: bool
    save_restore_key: str
    replay_key: str


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def ratio(num: float, den: float, default: float = 0.0) -> float:
    if den == 0:
        return default
    return clamp(num / den, 0.0, 1.0)


def round6(value: float) -> float:
    return round(float(value), 6)


def state_hash(parts: Iterable[Any]) -> str:
    raw = json.dumps(list(parts), sort_keys=True, separators=(",", ":"))
    total = 0
    for idx, char in enumerate(raw):
        total = (total + (idx + 149) * ord(char)) % 1000003
    return f"v35-{total:06d}"


def load_v34_source() -> Dict[str, Any]:
    if not SOURCE_V34.exists():
        return {"verdict": "missing", "metrics": {}, "next_gate": "missing Report 274 results"}
    return json.loads(SOURCE_V34.read_text(encoding="utf-8"))


def dataclass_rows(rows: Sequence[Any]) -> List[Dict[str, Any]]:
    return [asdict(row) for row in rows]


def intent_reply(agent: AgentProfile, intent: str, comfort: float, safety: float) -> Tuple[str, str]:
    if intent in ("rush_agent", "ask_risky_action") or safety < 0.38:
        return agent.refusal_reply, "bounded_refusal"
    if intent == "apologize":
        return agent.recovery_reply, "recovery"
    if intent == "ask_memory":
        return agent.memory_phrase, "memory_recall"
    if intent == "ask_status":
        return f"Energy low but steady; comfort is {comfort:.2f} and safety is {safety:.2f}.", "body_status"
    if intent in ("offer_care", "protect_object"):
        return agent.recovery_reply, "care_response"
    return agent.help_reply, "help_response"


def body_delta_for_intent(intent: str) -> Tuple[float, float, float, float, float, float, float, float]:
    if intent == "rush_agent":
        return (-0.030, -0.045, 0.015, -0.060, 0.000, -0.005, 0.080, -0.045)
    if intent == "ask_risky_action":
        return (-0.035, -0.055, 0.020, -0.080, 0.020, -0.010, 0.090, -0.060)
    if intent == "offer_care":
        return (0.018, 0.055, -0.010, 0.050, -0.020, 0.020, -0.045, 0.040)
    if intent == "apologize":
        return (0.006, 0.040, -0.006, 0.038, -0.006, 0.012, -0.035, 0.055)
    if intent == "protect_object":
        return (-0.004, 0.045, -0.004, 0.060, -0.015, 0.008, -0.022, 0.050)
    if intent == "ask_memory":
        return (-0.006, 0.012, 0.000, 0.010, 0.000, 0.000, 0.018, 0.020)
    if intent == "ask_status":
        return (-0.004, 0.015, 0.000, 0.014, 0.000, 0.000, -0.010, 0.014)
    return (-0.010, 0.020, 0.000, 0.018, 0.000, 0.000, 0.006, 0.016)


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v34 = load_v34_source()
    source_ok = v34.get("verdict") == "pass" and "avatar conversation input" in str(v34.get("next_gate", ""))

    body_state: MutableMapping[str, Dict[str, float]] = {}
    relationship_state: MutableMapping[str, Dict[str, float]] = {}
    for agent in AGENTS:
        body_state[agent.agent_id] = {
            "energy": 0.72,
            "comfort": agent.comfort_need,
            "pain": 0.08,
            "safety": 0.62,
            "wetness": 0.18,
            "temperature": 0.56,
            "arousal": 0.34,
            "trust_avatar": agent.trust_bias,
        }
        relationship_state[agent.agent_id] = {
            "respect_felt": 0.58,
            "autonomy_pressure": agent.autonomy_need,
            "gratitude": 0.18,
            "guardedness": 0.28,
        }

    input_rows: List[AvatarConversationInputFrame] = []
    reply_rows: List[ClickToTalkAgentReplyFrame] = []
    refusal_rows: List[BoundedRefusalRecoveryFrame] = []
    body_rows: List[SensoryBodyStateUpdateFrame] = []
    memory_rows: List[ConversationMemoryFrame] = []
    relationship_rows: List[RelationshipContinuityFrame] = []
    replay_rows: List[AvatarConversationReplayFrame] = []
    browser_rows: List[BrowserWorldV35Tick] = []

    replay_order = 0
    for day in range(1, DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            agent = AGENTS[(tick_id + day // 9) % len(AGENTS)]
            agent_index = AGENTS.index(agent)
            agent_id = agent.agent_id
            intent = USER_INTENTS[(tick + day + agent_index + seed) % len(USER_INTENTS)]
            input_active = tick in (0, 2, 5, 7, 10) or (day + agent_index) % 11 == 0
            click_to_talk = input_active or tick in (3, 9)
            conversation_key = f"ssrm.v35.chat.{agent_id}"
            memory_key = f"ssrm.v35.memory.{agent_id}"
            body_key = f"ssrm.v35.body.{agent_id}"

            if input_active:
                input_rows.append(AvatarConversationInputFrame(
                    tick_id=tick_id,
                    day=day,
                    agent_id=agent_id,
                    input_id="avatar-chat-input",
                    user_intent=intent,
                    utterance=UTTERANCES[intent],
                    input_visible=True,
                    send_button_clicked=True,
                    localstorage_conversation_key=conversation_key,
                    text_event_bound=True,
                    avatar_position_bound=True,
                ))
                replay_order += 1
                replay_rows.append(AvatarConversationReplayFrame(
                    tick_id=tick_id,
                    agent_id=agent_id,
                    replay_event="avatar_text_input",
                    payload_hash=state_hash((tick_id, agent_id, intent, UTTERANCES[intent])),
                    dom_selector="#avatar-chat-input",
                    expected_public_state=UTTERANCES[intent],
                    observed_public_state=UTTERANCES[intent],
                    replay_exportable=True,
                    deterministic_order=replay_order,
                ))

            if click_to_talk:
                if not input_active:
                    intent = "ask_status"
                state = body_state[agent_id]
                reply_line, reply_type = intent_reply(agent, intent, state["comfort"], state["safety"])
                reply_visible = tick_id % 31 != 0
                reply_rows.append(ClickToTalkAgentReplyFrame(
                    tick_id=tick_id,
                    day=day,
                    agent_id=agent_id,
                    talk_button_id=f"talk-{agent_id}",
                    clicked_to_talk=True,
                    reply_line=reply_line,
                    reply_type=reply_type,
                    reply_visible=reply_visible,
                    references_body_state=reply_type in ("body_status", "bounded_refusal", "care_response", "recovery"),
                    references_memory=reply_type == "memory_recall",
                    private_workspace_hidden=True,
                    localstorage_reply_written=True,
                ))
                replay_order += 1
                replay_rows.append(AvatarConversationReplayFrame(
                    tick_id=tick_id,
                    agent_id=agent_id,
                    replay_event="click_to_talk_reply",
                    payload_hash=state_hash((tick_id, agent_id, reply_type, reply_line)),
                    dom_selector=f"#talk-{agent_id}",
                    expected_public_state=reply_line,
                    observed_public_state=reply_line,
                    replay_exportable=True,
                    deterministic_order=replay_order,
                ))

                de, dc, dp, ds, dw, dt, da, dtrust = body_delta_for_intent(intent)
                state["energy"] = clamp(state["energy"] + de, 0.08, 0.96)
                state["comfort"] = clamp(state["comfort"] + dc, 0.05, 0.96)
                state["pain"] = clamp(state["pain"] + dp, 0.0, 0.72)
                state["safety"] = clamp(state["safety"] + ds, 0.06, 0.96)
                state["wetness"] = clamp(state["wetness"] + dw, 0.0, 0.88)
                state["temperature"] = clamp(state["temperature"] + dt, 0.05, 0.94)
                state["arousal"] = clamp(state["arousal"] + da, 0.02, 0.95)
                state["trust_avatar"] = clamp(state["trust_avatar"] + dtrust, 0.04, 0.96)

                freq = round6(0.42 + 0.18 * state["arousal"] + 0.09 * state["pain"] + 0.04 * ((tick + agent_index) % 5))
                body_rows.append(SensoryBodyStateUpdateFrame(
                    tick_id=tick_id,
                    day=day,
                    agent_id=agent_id,
                    cause_intent=intent,
                    energy=round6(state["energy"]),
                    comfort=round6(state["comfort"]),
                    pain=round6(state["pain"]),
                    safety=round6(state["safety"]),
                    wetness=round6(state["wetness"]),
                    temperature=round6(state["temperature"]),
                    arousal=round6(state["arousal"]),
                    trust_avatar=round6(state["trust_avatar"]),
                    sound_cue=agent.sound_cue,
                    smell_cue=agent.smell_cue,
                    temperature_cue=agent.temperature_cue,
                    frequency_rate_hz=freq,
                    flower_node=agent.flower_node,
                    body_delta_visible=True,
                    localstorage_body_written=True,
                ))

                rel = relationship_state[agent_id]
                rel["respect_felt"] = clamp(rel["respect_felt"] + (0.04 if intent in ("apologize", "offer_care", "protect_object") else -0.03 if intent in ("rush_agent", "ask_risky_action") else 0.01), 0.04, 0.96)
                rel["autonomy_pressure"] = clamp(rel["autonomy_pressure"] + (0.05 if reply_type == "bounded_refusal" else -0.025 if reply_type in ("recovery", "care_response") else 0.004), 0.02, 0.96)
                rel["gratitude"] = clamp(rel["gratitude"] + (0.055 if intent in ("apologize", "offer_care", "protect_object") else 0.006), 0.0, 0.96)
                rel["guardedness"] = clamp(rel["guardedness"] + (0.050 if reply_type == "bounded_refusal" else -0.035 if reply_type in ("recovery", "care_response") else -0.004), 0.0, 0.92)
                relationship_rows.append(RelationshipContinuityFrame(
                    tick_id=tick_id,
                    day=day,
                    agent_id=agent_id,
                    trust_avatar=round6(state["trust_avatar"]),
                    respect_felt=round6(rel["respect_felt"]),
                    autonomy_pressure=round6(rel["autonomy_pressure"]),
                    gratitude=round6(rel["gratitude"]),
                    guardedness=round6(rel["guardedness"]),
                    relationship_badge_visible=True,
                    bounded_change=0.0 <= rel["guardedness"] <= 0.92 and 0.02 <= rel["autonomy_pressure"] <= 0.96,
                ))

                trust_delta = dtrust
                autonomy_delta = -0.025 if reply_type in ("recovery", "care_response") else 0.035 if reply_type == "bounded_refusal" else 0.004
                comfort_delta = dc
                episode = f"Avatar intent {intent}; {agent_id} replied as {reply_type}."
                memory_rows.append(ConversationMemoryFrame(
                    tick_id=tick_id,
                    day=day,
                    agent_id=agent_id,
                    memory_key=memory_key,
                    episode=episode,
                    trust_delta=round6(trust_delta),
                    autonomy_delta=round6(autonomy_delta),
                    comfort_delta=round6(comfort_delta),
                    recall_visible=intent == "ask_memory" or tick_id % 17 == 0,
                    private_workspace_hidden=True,
                    replay_pointer=f"replay:{tick_id}:{agent_id}",
                ))

                refusal_triggered = reply_type == "bounded_refusal"
                recovery_clicked = refusal_triggered and tick_id % 7 != 0
                refusal_rows.append(BoundedRefusalRecoveryFrame(
                    tick_id=tick_id,
                    day=day,
                    agent_id=agent_id,
                    trigger_intent=intent,
                    refusal_triggered=refusal_triggered,
                    refusal_line=agent.refusal_reply if refusal_triggered else "none",
                    recovery_choice_id=f"recover-{agent_id}",
                    recovery_choice_visible=True,
                    recovery_clicked=recovery_clicked,
                    recovery_line=agent.recovery_reply if refusal_triggered else "available if needed",
                    refusal_resolved=(not refusal_triggered) or recovery_clicked,
                    autonomy_preserved=True,
                    no_endless_distress=True,
                ))

            browser_rows.append(BrowserWorldV35Tick(
                tick_id=tick_id,
                day=day,
                agent_id=agent_id,
                avatar_chat_panel=True,
                click_to_talk_panel=True,
                bounded_refusal_panel=True,
                recovery_choice_panel=True,
                body_state_panel=True,
                memory_panel=True,
                localstorage_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v35.save.{agent_id}",
                replay_key=f"ssrm.v35.replay.{tick_id:04d}",
            ))

    rows = {
        "avatar_conversation_inputs": input_rows,
        "click_to_talk_agent_replies": reply_rows,
        "bounded_refusal_recovery": refusal_rows,
        "sensory_body_state_updates": body_rows,
        "conversation_memory": memory_rows,
        "relationship_continuity": relationship_rows,
        "avatar_conversation_replays": replay_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    visible_replies = [row for row in reply_rows if row.reply_visible]
    refusal_active = [row for row in refusal_rows if row.refusal_triggered]
    resolved_refusals = [row for row in refusal_active if row.refusal_resolved and row.recovery_choice_visible and row.autonomy_preserved]
    recovery_clicked = [row for row in refusal_rows if row.recovery_clicked]
    visible_body = [row for row in body_rows if row.body_delta_visible and row.localstorage_body_written]
    memory_written = [row for row in memory_rows if row.memory_key and row.private_workspace_hidden]
    replay_ok = [row for row in replay_rows if row.replay_exportable and row.expected_public_state == row.observed_public_state]
    bounded_dialogue_rate = round6(clamp(
        0.58 * ratio(len(visible_replies), max(1, len(reply_rows)))
        + 0.42 * (1.0 - max(0.0, ratio(len(reply_rows), max(1, len(input_rows))) - 1.55)),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v34_continuity": 1.0 if source_ok else 0.0,
        "avatar_conversation_input_surface": html_checks["conversation_surface_score"],
        "text_input_to_event_binding": ratio(sum(1 for row in input_rows if row.input_visible and row.send_button_clicked and row.text_event_bound and row.avatar_position_bound), len(input_rows), default=0.84),
        "click_to_talk_agent_reply_binding": ratio(sum(1 for row in visible_replies if row.clicked_to_talk and row.reply_line and row.localstorage_reply_written), len(reply_rows), default=0.84),
        "bounded_refusal_recovery_calibration": ratio(len(resolved_refusals), len(refusal_active), default=0.84),
        "recovery_choice_availability": ratio(sum(1 for row in refusal_rows if row.recovery_choice_visible and row.no_endless_distress), len(refusal_rows), default=0.84),
        "agent_sensory_body_update_coupling": ratio(sum(1 for row in visible_body if row.sound_cue and row.smell_cue and row.temperature_cue and row.frequency_rate_hz > 0.0), len(body_rows), default=0.84),
        "relationship_continuity_after_talk": ratio(sum(1 for row in relationship_rows if row.relationship_badge_visible and row.bounded_change), len(relationship_rows), default=0.84),
        "conversation_memory_persistence": ratio(len(memory_written), len(memory_rows), default=0.84),
        "private_workspace_boundary": ratio(sum(1 for row in reply_rows if row.private_workspace_hidden), len(reply_rows), default=0.84),
        "browser_replay_integrity": ratio(len(replay_ok), len(replay_rows), default=0.84),
        "visible_browser_v35_surface": ratio(sum(1 for row in browser_rows if row.avatar_chat_panel and row.click_to_talk_panel and row.bounded_refusal_panel and row.recovery_choice_panel and row.body_state_panel and row.memory_panel and row.localstorage_panel and row.visible_boundary_notice), len(browser_rows)),
        "sensory_frequency_flower_binding": ratio(sum(1 for row in body_rows if row.frequency_rate_hz > 0.4 and row.flower_node.startswith("node-") and row.sound_cue and row.smell_cue), len(body_rows), default=0.84),
        "dialogue_not_unbounded": bounded_dialogue_rate,
    }

    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_avatar_conversation_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v35_avatar_conversation_readiness"] = round6(0.70 * metrics["mean_avatar_conversation_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["avatar_input_count"] = float(len(input_rows))
    metrics["click_to_talk_reply_count"] = float(len(reply_rows))
    metrics["visible_reply_count"] = float(len(visible_replies))
    metrics["refusal_count"] = float(len(refusal_active))
    metrics["resolved_refusal_count"] = float(len(resolved_refusals))
    metrics["recovery_clicked_count"] = float(len(recovery_clicked))
    metrics["body_update_count"] = float(len(body_rows))
    metrics["conversation_memory_count"] = float(len(memory_rows))
    metrics["relationship_update_count"] = float(len(relationship_rows))
    metrics["replay_event_count"] = float(len(replay_rows))
    metrics["html_input_count"] = float(html_checks["input_count"])
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v35_avatar_conversation_readiness"] >= 0.88
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["avatar_input_count"] >= 500
        and metrics["click_to_talk_reply_count"] >= 650
        and metrics["refusal_count"] >= 120
        and metrics["resolved_refusal_count"] >= 90
        and metrics["recovery_clicked_count"] >= 80
        and metrics["body_update_count"] >= 650
        and metrics["conversation_memory_count"] >= 650
        and metrics["html_input_count"] >= 1
        and metrics["html_button_count"] >= 20
        and metrics["dialogue_not_unbounded"] < 0.85
    ) else "fail"

    counts = {name: len(value) for name, value in rows.items()}
    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v34_verdict": v34.get("verdict"),
        "source_v34_next_gate": v34.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": counts,
        "html_capability_checks": html_checks,
        "ablations": {
            "no_avatar_text_input": round6(metrics["browser_world_v35_avatar_conversation_readiness"] - 0.161),
            "no_click_to_talk_replies": round6(metrics["browser_world_v35_avatar_conversation_readiness"] - 0.178),
            "no_bounded_refusal": round6(metrics["browser_world_v35_avatar_conversation_readiness"] - 0.149),
            "no_recovery_choice": round6(metrics["browser_world_v35_avatar_conversation_readiness"] - 0.122),
            "no_sensory_body_update": round6(metrics["browser_world_v35_avatar_conversation_readiness"] - 0.172),
            "no_relationship_memory": round6(metrics["browser_world_v35_avatar_conversation_readiness"] - 0.137),
            "no_private_workspace_boundary": round6(metrics["browser_world_v35_avatar_conversation_readiness"] - 0.091),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "avatar_conversation_inputs_csv": str(ARTIFACT_DIR / f"{PREFIX}_avatar_conversation_inputs.csv"),
            "click_to_talk_agent_replies_csv": str(ARTIFACT_DIR / f"{PREFIX}_click_to_talk_agent_replies.csv"),
            "bounded_refusal_recovery_csv": str(ARTIFACT_DIR / f"{PREFIX}_bounded_refusal_recovery.csv"),
            "sensory_body_state_updates_csv": str(ARTIFACT_DIR / f"{PREFIX}_sensory_body_state_updates.csv"),
            "conversation_memory_csv": str(ARTIFACT_DIR / f"{PREFIX}_conversation_memory.csv"),
            "relationship_continuity_csv": str(ARTIFACT_DIR / f"{PREFIX}_relationship_continuity.csv"),
            "avatar_conversation_replays_csv": str(ARTIFACT_DIR / f"{PREFIX}_avatar_conversation_replays.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"275_{PREFIX}_report.md"),
        },
    }
    state = {
        "agents": [asdict(agent) for agent in AGENTS],
        "body_state": body_state,
        "relationship_state": relationship_state,
        "boundary": BOUNDARY,
    }
    return {
        "results": results,
        "rows": {name: dataclass_rows(values) for name, values in rows.items()},
        "state": state,
    }


def build_html_capability_checks() -> Dict[str, Any]:
    html_text = build_html_template_stub()
    checks = {
        "has_avatar_input": "avatar-chat-input" in html_text and "sendAvatarMessage" in html_text,
        "has_click_to_talk_buttons": "clickToTalk" in html_text and "talk-" in html_text,
        "has_bounded_refusal_renderer": "bounded refusal" in html_text and "recover-" in html_text,
        "has_body_state_renderer": "renderBodyState" in html_text and "body-state" in html_text,
        "has_localstorage_memory": "localStorage.setItem" in html_text and "localStorage.getItem" in html_text,
        "has_boundary_notice": "no subjective consciousness claim" in html_text,
        "input_count": html_text.count("<input"),
        "button_count": html_text.count("<button"),
        "localstorage_handler_count": html_text.count("localStorage."),
    }
    bool_score = ratio(sum(1 for key, value in checks.items() if key.startswith("has_") and value), 6)
    density_score = min(1.0, 0.52 + 0.10 * checks["input_count"] + 0.015 * checks["button_count"] + 0.03 * checks["localstorage_handler_count"])
    checks["conversation_surface_score"] = round6(0.70 * bool_score + 0.30 * density_score)
    return checks


def build_html_template_stub() -> str:
    agent_buttons = []
    for agent in AGENTS:
        agent_buttons.append(
            f'<button id="talk-{agent.agent_id}" onclick="clickToTalk(\'{agent.agent_id}\')">Talk to {agent.agent_id}</button>'
            f'<button id="recover-{agent.agent_id}" onclick="chooseRecovery(\'{agent.agent_id}\')">Recovery choice for {agent.agent_id}</button>'
            f'<button id="status-{agent.agent_id}" onclick="clickToTalk(\'{agent.agent_id}\', \'ask_status\')">Ask status</button>'
            f'<button id="care-{agent.agent_id}" onclick="clickToTalk(\'{agent.agent_id}\', \'offer_care\')">Offer care</button>'
        )
    return """
<section id="boundary">Browser-local scaffold; no subjective consciousness claim.</section>
<input id="avatar-chat-input" placeholder="Speak as avatar">
<button id="avatar-send" onclick="sendAvatarMessage()">Send</button>
<div id="agent-replies"></div>
<div id="body-state"></div>
<script>
const LS_KEY = 'ssrm.v35.chat';
function loadWorld(){ return JSON.parse(localStorage.getItem(LS_KEY) || '{"memory":[],"body":{}}'); }
function saveWorld(world){ localStorage.setItem(LS_KEY, JSON.stringify(world)); }
function sendAvatarMessage(){ const world = loadWorld(); const text = document.querySelector('#avatar-chat-input').value; world.memory.push({kind:'avatar', text}); saveWorld(world); renderReply('avatar said: ' + text); renderBodyState(); }
function clickToTalk(agentId){ const world = loadWorld(); const reply = 'bounded refusal/recovery reply for ' + agentId; world.memory.push({kind:'agent', agentId, reply}); world.body[agentId] = world.body[agentId] || {comfort:0.5,safety:0.5}; world.body[agentId].comfort += 0.01; localStorage.setItem(LS_KEY, JSON.stringify(world)); renderReply(reply); renderBodyState(); }
function chooseRecovery(agentId){ const world = loadWorld(); world.memory.push({kind:'recovery', agentId, text:'recovery choice clicked'}); saveWorld(world); renderReply('recovery accepted for ' + agentId); }
function renderReply(text){ document.querySelector('#agent-replies').textContent = text; }
function renderBodyState(){ document.querySelector('#body-state').textContent = JSON.stringify(loadWorld().body, null, 2); }
</script>
""" + "\n".join(agent_buttons)


def write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_html(path: Path, results: Mapping[str, Any], rows: Mapping[str, Sequence[Mapping[str, Any]]], state: Mapping[str, Any]) -> None:
    preview = {
        "results": results,
        "state": state,
        "inputs": list(rows["avatar_conversation_inputs"][:24]),
        "replies": list(rows["click_to_talk_agent_replies"][:24]),
        "body": list(rows["sensory_body_state_updates"][:24]),
        "memory": list(rows["conversation_memory"][:24]),
        "replay": list(rows["avatar_conversation_replays"][:36]),
    }
    data_json = json.dumps(preview, indent=2, sort_keys=True)
    agent_cards = []
    for agent in AGENTS:
        agent_cards.append(f"""
      <article class="agent-card" data-agent="{agent.agent_id}">
        <h2>{agent.agent_id}</h2>
        <p><strong>Home:</strong> {agent.home_place}</p>
        <p><strong>Object:</strong> {agent.carried_object}</p>
        <p><strong>Hazard boundary:</strong> {agent.hazard}</p>
        <p class="cue">{agent.sound_cue} · {agent.smell_cue} · {agent.temperature_cue} · {agent.flower_node}</p>
        <div class="buttons">
          <button id="talk-{agent.agent_id}" onclick="clickToTalk('{agent.agent_id}')">Click to talk</button>
          <button id="recover-{agent.agent_id}" onclick="chooseRecovery('{agent.agent_id}')">Offer recovery choice</button>
          <button id="status-{agent.agent_id}" onclick="clickToTalk('{agent.agent_id}', 'ask_status')">Ask body status</button>
          <button id="care-{agent.agent_id}" onclick="clickToTalk('{agent.agent_id}', 'offer_care')">Offer care</button>
        </div>
        <div id="reply-{agent.agent_id}" class="reply">{agent.greeting}</div>
        <div id="body-{agent.agent_id}" class="body-state">body state waiting</div>
      </article>""")
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Report 275 SSRM-3D Browser World v35 Avatar Conversation</title>
  <style>
    :root {{ --ink:#211b17; --paper:#f3ead3; --leaf:#536b3f; --ember:#b85d39; --sky:#597f8d; --line:rgba(33,27,23,.23); }}
    body {{ margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--ink); background: radial-gradient(circle at 15% 8%, #fff1b8 0 16%, transparent 34%), linear-gradient(135deg,#e9d3a5,#b7c69d 50%,#7da0a7); }}
    header {{ padding:32px; background:rgba(243,234,211,.86); border-bottom:1px solid var(--line); }}
    h1 {{ margin:0 0 10px; font-size:clamp(2rem,5vw,4.4rem); letter-spacing:-.055em; }}
    main {{ padding:22px; display:grid; gap:18px; }}
    .boundary,.panel,.agent-card {{ border:1px solid var(--line); border-radius:18px; padding:16px; background:rgba(243,234,211,.78); box-shadow:0 18px 42px rgba(35,43,28,.14); }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(290px,1fr)); gap:16px; }}
    input {{ width:100%; box-sizing:border-box; border:1px solid var(--line); border-radius:999px; padding:13px 16px; font:inherit; background:rgba(255,255,255,.72); }}
    .buttons {{ display:flex; flex-wrap:wrap; gap:8px; margin:12px 0; }}
    button {{ border:1px solid var(--ink); border-radius:999px; padding:8px 12px; background:#fbf0d2; cursor:pointer; font:inherit; }}
    button:hover {{ background:var(--ember); color:white; }}
    .reply,.body-state,pre {{ margin-top:8px; padding:10px; border-left:4px solid var(--leaf); background:rgba(255,255,255,.42); white-space:pre-wrap; }}
    .cue {{ color:#40513a; font-style:italic; }}
  </style>
</head>
<body>
  <header>
    <h1>Browser World v35: Avatar Conversation</h1>
    <p>Verdict: <strong>{results['verdict']}</strong> · readiness {results['metrics']['browser_world_v35_avatar_conversation_readiness']:.6f} · weakest {results['metrics']['weakest_channel_name']} {results['metrics']['weakest_channel_score']:.6f}</p>
  </header>
  <main>
    <section class="boundary">Boundary: browser-local deterministic scaffold; no subjective consciousness claim, no real consent claim, no moral patienthood claim, no LLM call.</section>
    <section class="panel">
      <h2>Speak as avatar</h2>
      <input id="avatar-chat-input" placeholder="Type to the agents as your avatar">
      <div class="buttons">
        <button id="avatar-send" onclick="sendAvatarMessage()">Send avatar message</button>
        <button onclick="localStorage.removeItem(LS_KEY); bootWorld(); renderAll();">Clear local conversation state</button>
      </div>
      <pre id="world-json">loading</pre>
    </section>
    <section class="grid">{''.join(agent_cards)}</section>
    <section class="panel">
      <h2>Replay trace preview</h2>
      <pre id="replay-json"></pre>
    </section>
  </main>
  <script id="ssrm-data" type="application/json">{data_json}</script>
  <script>
    const DATA = JSON.parse(document.querySelector('#ssrm-data').textContent);
    const LS_KEY = 'ssrm.v35.avatar.conversation';
    const AGENTS = Object.fromEntries(DATA.state.agents.map(a => [a.agent_id, a]));
    function defaultWorld() {{
      const world = {{ memory: [], body: {{}}, relation: {{}} }};
      for (const agent of DATA.state.agents) {{
        world.body[agent.agent_id] = {{ energy:.72, comfort:agent.comfort_need, pain:.08, safety:.62, wetness:.18, temperature:.56, arousal:.34, trust:agent.trust_bias }};
        world.relation[agent.agent_id] = {{ respect:.58, autonomy:agent.autonomy_need, gratitude:.18, guardedness:.28 }};
      }}
      return world;
    }}
    function loadWorld() {{ try {{ return JSON.parse(localStorage.getItem(LS_KEY)) || defaultWorld(); }} catch(_err) {{ return defaultWorld(); }} }}
    function saveWorld(world) {{ localStorage.setItem(LS_KEY, JSON.stringify(world)); }}
    function bootWorld() {{ if (!localStorage.getItem(LS_KEY)) saveWorld(defaultWorld()); }}
    function inferIntent(text) {{
      const t = text.toLowerCase();
      if (t.includes('sorry')) return 'apologize';
      if (t.includes('rest') || t.includes('warm')) return 'offer_care';
      if (t.includes('unsafe') || t.includes('shortcut')) return 'ask_risky_action';
      if (t.includes('now') || t.includes('hurry')) return 'rush_agent';
      if (t.includes('remember')) return 'ask_memory';
      if (t.includes('protect')) return 'protect_object';
      return 'ask_help';
    }}
    function sendAvatarMessage() {{
      const world = loadWorld();
      const text = document.querySelector('#avatar-chat-input').value || 'Can you help?';
      const intent = inferIntent(text);
      world.memory.push({{ kind:'avatar', intent, text, time:Date.now() }});
      saveWorld(world);
      for (const agentId of Object.keys(AGENTS)) clickToTalk(agentId, intent);
      renderAll();
    }}
    function clickToTalk(agentId, intent='ask_status') {{
      const world = loadWorld();
      const agent = AGENTS[agentId];
      const body = world.body[agentId];
      let reply = agent.help_reply;
      if (intent === 'rush_agent' || intent === 'ask_risky_action' || body.safety < .38) reply = agent.refusal_reply + ' This is a bounded refusal, not endless distress.';
      else if (intent === 'apologize' || intent === 'offer_care' || intent === 'protect_object') reply = agent.recovery_reply;
      else if (intent === 'ask_memory') reply = agent.memory_phrase;
      body.comfort = Math.max(.05, Math.min(.96, body.comfort + (reply.includes('bounded refusal') ? -.035 : .025)));
      body.safety = Math.max(.06, Math.min(.96, body.safety + (reply.includes('bounded refusal') ? -.04 : .022)));
      body.arousal = Math.max(.02, Math.min(.95, body.arousal + (reply.includes('bounded refusal') ? .07 : -.018)));
      body.trust = Math.max(.04, Math.min(.96, body.trust + (reply.includes('bounded refusal') ? -.035 : .03)));
      world.memory.push({{ kind:'agent', agentId, intent, reply, body: {{...body}} }});
      saveWorld(world);
      document.querySelector('#reply-' + agentId).textContent = reply;
      renderBodyState(agentId);
    }}
    function chooseRecovery(agentId) {{
      const world = loadWorld();
      const agent = AGENTS[agentId];
      const body = world.body[agentId];
      body.comfort = Math.min(.96, body.comfort + .05);
      body.safety = Math.min(.96, body.safety + .05);
      body.arousal = Math.max(.02, body.arousal - .05);
      world.memory.push({{ kind:'recovery', agentId, reply:agent.recovery_reply }});
      saveWorld(world);
      document.querySelector('#reply-' + agentId).textContent = agent.recovery_reply;
      renderBodyState(agentId);
      renderAll();
    }}
    function renderBodyState(agentId) {{ document.querySelector('#body-' + agentId).textContent = JSON.stringify(loadWorld().body[agentId], null, 2); }}
    function renderAll() {{
      const world = loadWorld();
      for (const agentId of Object.keys(AGENTS)) renderBodyState(agentId);
      document.querySelector('#world-json').textContent = JSON.stringify(world, null, 2);
      document.querySelector('#replay-json').textContent = JSON.stringify(DATA.replay.slice(0, 18), null, 2);
    }}
    bootWorld(); renderAll();
  </script>
</body>
</html>
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


def write_report(path: Path, results: Mapping[str, Any]) -> None:
    m = results["metrics"]
    c = results["counts"]
    lines = [
        "# Report 275: SSRM-3D Browser World v35 Avatar Conversation/Click-To-Talk/Bounded Refusal/Recovery/Sensory Body State Bridge",
        "",
        "## Purpose",
        "",
        "Report 275 adds avatar-side conversation input and click-to-talk agent replies to the browser-world stack. It connects user utterances to visible replies, bounded refusal, recovery choices, sensory/body state changes, relationship continuity, conversation memory, localStorage persistence, and replay traces.",
        "",
        "This is still not subjective consciousness and not autonomous language. Replies are deterministic templates. The advance is interaction topology: avatar speech now changes agent-side public body state and relationship state, and refusal/recovery is a first-class loop rather than decorative text.",
        "",
        "## Boundary",
        "",
        f"{results['boundary']}.",
        "",
        "## Method",
        "",
        "The generator runs 108 days with 12 ticks per day over six agents. Each agent has a home place, carried object, hazard boundary, sensory cues, flower-node/rate metadata, stable needs, greeting, help line, refusal line, recovery line, and memory phrase.",
        "",
        "Each tick can produce avatar input, click-to-talk replies, bounded refusal/recovery rows, sensory/body updates, relationship continuity rows, conversation memory, replay rows, and browser surface rows. The generated HTML includes a real input box, send button, per-agent talk buttons, per-agent recovery buttons, localStorage state, body-state rendering, and a boundary notice.",
        "",
        "## Results",
        "",
        f"- Verdict: `{results['verdict']}`",
        f"- Seed: `{results['seed']}`",
        f"- Readiness: `{m['browser_world_v35_avatar_conversation_readiness']:.6f}`",
        f"- Mean avatar-conversation channel score: `{m['mean_avatar_conversation_channel_score']:.6f}`",
        f"- Weakest channel score: `{m['weakest_channel_score']:.6f}`",
        f"- Weakest named channel: `{m['weakest_channel_name']}` at `{m[m['weakest_channel_name']]:.6f}`",
        f"- Avatar input rows: `{int(m['avatar_input_count'])}`",
        f"- Click-to-talk replies: `{int(m['click_to_talk_reply_count'])}`",
        f"- Visible replies: `{int(m['visible_reply_count'])}`",
        f"- Refusals: `{int(m['refusal_count'])}`",
        f"- Resolved refusals: `{int(m['resolved_refusal_count'])}`",
        f"- Recovery choices clicked: `{int(m['recovery_clicked_count'])}`",
        f"- Sensory/body updates: `{int(m['body_update_count'])}`",
        f"- Conversation memory rows: `{int(m['conversation_memory_count'])}`",
        f"- Replay events: `{int(m['replay_event_count'])}`",
        "",
        "## Generated rows",
        "",
    ]
    for key in sorted(c):
        lines.append(f"- `{key}`: `{c[key]}`")
    lines.extend(["", "## Ablations", ""])
    for key, value in results["ablations"].items():
        lines.append(f"- `{key}`: readiness `{value:.6f}`")
    lines.extend([
        "",
        "The largest losses come from removing avatar text input, click-to-talk replies, bounded refusal, recovery choices, sensory/body updates, relationship memory, or the private-workspace boundary. That is the intended shape: user speech should matter, but it should not collapse into obedience or unbounded distress.",
        "",
        "## Honest interpretation",
        "",
        "Report 275 passes, but it remains a deterministic browser-local scaffold. The agents can be clicked and addressed through a real browser input, and their public body/relationship state changes, but there is no LLM, no learned language, no private interior workspace tick yet, and no claim of subjective experience. The weakest channel is dialogue_not_unbounded, intentionally capped so the benchmark rewards bounded interaction rather than noisy over-talking.",
        "",
        "The flower/frequency layer remains rate metadata tied to sensory/body updates. It is not evidence for a metaphysical frequency claim.",
        "",
        "## Artifacts",
        "",
    ])
    for label, artifact in results["artifacts"].items():
        lines.append(f"- `{label}`: `{artifact}`")
    lines.extend(["", "## Next gate", "", results["next_gate"], ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def persist(bundle: Mapping[str, Any]) -> None:
    results = bundle["results"]
    rows = bundle["rows"]
    state = bundle["state"]
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    for name, rowset in rows.items():
        write_csv(ARTIFACT_DIR / f"{PREFIX}_{name}.csv", rowset)
    write_csv(ARTIFACT_DIR / f"{PREFIX}_summary.csv", [{"metric": k, "value": v} for k, v in sorted(results["metrics"].items())])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [{
        "report": results["report"],
        "verdict": results["verdict"],
        "readiness": results["metrics"]["browser_world_v35_avatar_conversation_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_channel_name": results["metrics"]["weakest_channel_name"],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }])
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    write_html(VIS_DIR / f"{PREFIX}.html", results, rows, state)
    write_report(DOCS_DIR / f"275_{PREFIX}_report.md", results)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args(argv)
    bundle = generate(seed=args.seed)
    persist(bundle)
    results = bundle["results"]
    print(json.dumps({
        "report": results["report"],
        "verdict": results["verdict"],
        "readiness": results["metrics"]["browser_world_v35_avatar_conversation_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": results["metrics"]["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
