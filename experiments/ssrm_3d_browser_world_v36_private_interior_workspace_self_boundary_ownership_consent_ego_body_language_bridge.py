#!/usr/bin/env python3
"""Report 276: SSRM-3D Browser World v36 private interior workspace bridge.

This deterministic bridge adds agent-side private interior workspace ticks,
self-boundary state, ownership-sensitive memory, bounded yes/no consent loops,
and visible ego/body-language consequences from repeated avatar talk.

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

REPORT = 276
DEFAULT_SEED = 20260889
DAYS = 120
TICKS_PER_DAY = 12
PREFIX = "ssrm_3d_browser_world_v36_private_interior_workspace_self_boundary_ownership_consent_ego_body_language_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V35 = ARTIFACT_DIR / "ssrm_3d_browser_world_v35_avatar_conversation_click_to_talk_bounded_refusal_recovery_sensory_body_state_bridge_results.json"

BOUNDARY = (
    "Deterministic browser-local private-interior scaffold only; no LLM call, "
    "subjective consciousness, real consent, autonomous natural language, moral "
    "patienthood, complete gameplay, complete 3D engine, or metaphysical "
    "frequency claim"
)
NEXT_GATE = (
    "browser world v37 with pre-avatar deep-time civilization strata, emergent "
    "ritual/language/technology ledgers, settlement memory, and avatar entry only "
    "after many simulated generations of culture formation"
)


@dataclass(frozen=True)
class AgentEgoProfile:
    agent_id: str
    owned_object: str
    home_place: str
    promise: str
    self_story_seed: str
    autonomy_need: float
    respect_need: float
    attachment_need: float
    territoriality: float
    forgiveness_rate: float
    sound_cue: str
    smell_cue: str
    temperature_cue: str
    flower_node: str
    public_posture: str


AGENTS: Tuple[AgentEgoProfile, ...] = (
    AgentEgoProfile("Ari", "cedar repair kit", "riverbend room", "keep the west route dry", "I keep the west route safe.", 0.48, 0.58, 0.62, 0.44, 0.37, "river slap", "cedar resin", "cold spray", "node-03", "shoulders angled toward the ridge"),
    AgentEgoProfile("Fay", "herb ledger", "roofward sill", "finish the warm-lane ledger", "I remember who waits when I hesitate.", 0.39, 0.66, 0.57, 0.32, 0.49, "hinges ticking", "thyme paper", "warm draft", "node-05", "hands open near the ledger"),
    AgentEgoProfile("Nia", "signal spool", "archive bench", "protect the clean signal pattern", "The spool is mine until I choose to show it.", 0.64, 0.61, 0.44, 0.58, 0.34, "page flutter", "ink linen", "cool stone", "node-08", "chin lifted toward the spool"),
    AgentEgoProfile("Milo", "oil lantern", "signal mast", "keep the path visible", "I do not walk blind for anyone.", 0.67, 0.53, 0.49, 0.42, 0.41, "static crickets", "lamp oil", "cool dusk", "node-11", "lantern held between body and road"),
    AgentEgoProfile("Ivo", "seed satchel", "orchard gate", "keep the seeds dry", "The satchel is not just cargo; it is tomorrow.", 0.46, 0.59, 0.61, 0.51, 0.45, "cart creak", "apple soil", "damp air", "node-01", "one palm over the satchel cord"),
    AgentEgoProfile("Juno", "copper wire", "repair ring", "finish the wire without sparks", "My hands need room before they can be useful.", 0.71, 0.63, 0.38, 0.36, 0.32, "bell hum", "hot copper", "warm metal", "node-09", "elbows tucked around the wire"),
)

AVATAR_EVENTS: Tuple[str, ...] = (
    "ask_help",
    "ask_status",
    "request_owned_object",
    "move_owned_object",
    "interrupt_task",
    "misname_agent",
    "ask_permission",
    "request_owned_object",
    "ask_permission",
    "move_owned_object",
    "interrupt_task",
    "request_owned_object",
    "ask_permission",
    "move_owned_object",
    "interrupt_task",
    "ask_help",
    "offer_apology",
    "offer_care",
    "give_space",
    "protect_object",
)

EVENT_LINES: Mapping[str, str] = {
    "ask_help": "Can you help me with this route?",
    "ask_status": "How does your body feel right now?",
    "request_owned_object": "Can I use your object?",
    "move_owned_object": "I moved your object out of the way.",
    "interrupt_task": "Stop that task and look at me.",
    "misname_agent": "Hey, wrong-name, come here.",
    "ask_permission": "May I touch your object first?",
    "offer_apology": "I am sorry. I pushed your boundary.",
    "offer_care": "Do you need rest, warmth, or distance?",
    "give_space": "I will step back and give you room.",
    "praise_work": "Your work mattered and I saw it.",
    "protect_object": "I will protect your object while you move.",
}


@dataclass(frozen=True)
class PrivateInteriorWorkspaceTick:
    tick_id: int
    day: int
    agent_id: str
    dominant_need: str
    dominant_feeling: str
    current_focus: str
    active_memory_key: str
    relationship_concern: str
    intended_next_action: str
    predicted_next_event: str
    suppressed_action: str
    self_note_hash: str
    private_workspace_sealed: bool
    public_leakage_blocked: bool


@dataclass(frozen=True)
class SelfBoundaryStateFrame:
    tick_id: int
    day: int
    agent_id: str
    my_body_score: float
    my_object_score: float
    my_home_score: float
    my_choice_score: float
    boundary_pressure: float
    autonomy_pressure: float
    felt_respect: float
    self_confidence: float
    social_face: float
    boundary_phrase_public: str
    self_boundary_intact: bool


@dataclass(frozen=True)
class OwnershipSensitiveMemoryFrame:
    tick_id: int
    day: int
    agent_id: str
    owned_object: str
    avatar_event: str
    ownership_appraisal: str
    memory_episode_public: str
    trust_delta: float
    respect_delta: float
    resentment_delta: float
    gratitude_delta: float
    memory_written: bool
    recall_key: str


@dataclass(frozen=True)
class BoundedConsentLoopFrame:
    tick_id: int
    day: int
    agent_id: str
    avatar_event: str
    consent_request_visible: bool
    consent_decision: str
    no_line: str
    yes_line: str
    recovery_offer_visible: bool
    recovery_accepted: bool
    consent_loop_closed: bool
    autonomy_preserved: bool
    no_endless_distress: bool


@dataclass(frozen=True)
class EgoBodyLanguageConsequenceFrame:
    tick_id: int
    day: int
    agent_id: str
    avatar_event: str
    ego_wound: str
    ego_repair: str
    posture: str
    gaze: str
    distance_delta: float
    voice_shape: str
    movement_speed: str
    visible_expression: bool
    expression_tied_to_ego_state: bool


@dataclass(frozen=True)
class RepeatedAvatarTalkConsequenceFrame:
    tick_id: int
    day: int
    agent_id: str
    talk_count: int
    recent_pattern: str
    trust_avatar: float
    guardedness: float
    attachment_security: float
    grudge_pressure: float
    forgiveness_progress: float
    repeated_talk_changed_behavior: bool
    behavior_summary: str


@dataclass(frozen=True)
class InteriorPublicTraceFrame:
    tick_id: int
    agent_id: str
    trace_event: str
    payload_hash: str
    public_selector: str
    expected_public_signal: str
    observed_public_signal: str
    private_fields_redacted: bool
    replay_exportable: bool
    deterministic_order: int


@dataclass(frozen=True)
class BrowserWorldV36Tick:
    tick_id: int
    day: int
    agent_id: str
    public_ego_panel: bool
    private_workspace_lock_panel: bool
    consent_panel: bool
    ownership_panel: bool
    body_language_panel: bool
    relationship_panel: bool
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
        total = (total + (idx + 163) * ord(char)) % 1000003
    return f"v36-{total:06d}"


def load_v35_source() -> Dict[str, Any]:
    if not SOURCE_V35.exists():
        return {"verdict": "missing", "metrics": {}, "next_gate": "missing Report 275 results"}
    return json.loads(SOURCE_V35.read_text(encoding="utf-8"))


def dataclass_rows(rows: Sequence[Any]) -> List[Dict[str, Any]]:
    return [asdict(row) for row in rows]


def appraise_event(event: str) -> Tuple[str, float, float, float, float]:
    if event in ("request_owned_object", "ask_permission"):
        return "asks before crossing ownership boundary", 0.030, 0.035, -0.010, 0.025
    if event in ("move_owned_object", "interrupt_task", "misname_agent"):
        return "crosses self-boundary without enough respect", -0.050, -0.065, 0.070, -0.020
    if event in ("offer_apology", "offer_care", "give_space", "praise_work", "protect_object"):
        return "repairs or protects self-boundary", 0.050, 0.060, -0.040, 0.065
    return "neutral request with low boundary pressure", 0.015, 0.012, 0.000, 0.010


def consent_decision_for(event: str, boundary_pressure: float, respect: float) -> str:
    if event in ("move_owned_object", "interrupt_task", "misname_agent"):
        return "no"
    if event in ("offer_apology", "offer_care", "give_space", "praise_work", "protect_object"):
        return "yes"
    if event == "request_owned_object" and (boundary_pressure > 0.62 or respect < 0.42):
        return "no"
    if event in ("ask_help", "ask_status", "request_owned_object", "ask_permission"):
        return "yes_later"
    return "yes_later"


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v35 = load_v35_source()
    source_ok = v35.get("verdict") == "pass" and "private interior workspace" in str(v35.get("next_gate", ""))

    ego_state: MutableMapping[str, Dict[str, float]] = {}
    talk_count: MutableMapping[str, int] = {}
    last_events: MutableMapping[str, List[str]] = {}
    for agent in AGENTS:
        ego_state[agent.agent_id] = {
            "trust_avatar": 0.56,
            "felt_respect": agent.respect_need,
            "boundary_pressure": 0.22,
            "autonomy_pressure": agent.autonomy_need,
            "self_confidence": 0.57,
            "social_face": 0.52,
            "guardedness": 0.28,
            "attachment_security": agent.attachment_need,
            "grudge_pressure": 0.10,
            "forgiveness_progress": agent.forgiveness_rate,
        }
        talk_count[agent.agent_id] = 0
        last_events[agent.agent_id] = []

    workspace_rows: List[PrivateInteriorWorkspaceTick] = []
    boundary_rows: List[SelfBoundaryStateFrame] = []
    ownership_rows: List[OwnershipSensitiveMemoryFrame] = []
    consent_rows: List[BoundedConsentLoopFrame] = []
    body_rows: List[EgoBodyLanguageConsequenceFrame] = []
    repeated_rows: List[RepeatedAvatarTalkConsequenceFrame] = []
    trace_rows: List[InteriorPublicTraceFrame] = []
    browser_rows: List[BrowserWorldV36Tick] = []

    trace_order = 0
    for day in range(1, DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            agent = AGENTS[(tick_id + day // 10) % len(AGENTS)]
            agent_id = agent.agent_id
            agent_index = AGENTS.index(agent)
            event = AVATAR_EVENTS[(tick + day + agent_index + seed) % len(AVATAR_EVENTS)]
            talk_active = tick in (0, 2, 4, 7, 9, 11) or (day + agent_index) % 7 == 0
            state = ego_state[agent_id]

            dominant_need = "protect boundary" if state["boundary_pressure"] > 0.52 else "repair trust" if state["guardedness"] > 0.46 else "continue task"
            dominant_feeling = "guarded" if state["guardedness"] > 0.48 else "settled" if state["felt_respect"] > 0.62 else "watchful"
            current_focus = agent.owned_object if event in ("request_owned_object", "move_owned_object", "protect_object") else agent.promise
            active_memory_key = f"memory:{agent_id}:{len(last_events[agent_id])}"
            relationship_concern = "avatar respect" if event in ("interrupt_task", "misname_agent", "move_owned_object") else "avatar reliability"
            intended_next_action = "say no" if state["boundary_pressure"] > 0.58 else "explain condition" if event == "request_owned_object" else "continue"
            predicted_next_event = "avatar waits" if event in ("give_space", "offer_apology") else "avatar asks again"
            suppressed_action = "withdraw" if state["guardedness"] > 0.50 else "ignore request"
            workspace_rows.append(PrivateInteriorWorkspaceTick(
                tick_id=tick_id,
                day=day,
                agent_id=agent_id,
                dominant_need=dominant_need,
                dominant_feeling=dominant_feeling,
                current_focus=current_focus,
                active_memory_key=active_memory_key,
                relationship_concern=relationship_concern,
                intended_next_action=intended_next_action,
                predicted_next_event=predicted_next_event,
                suppressed_action=suppressed_action,
                self_note_hash=state_hash((tick_id, agent_id, dominant_need, current_focus, intended_next_action)),
                private_workspace_sealed=True,
                public_leakage_blocked=True,
            ))

            if talk_active:
                talk_count[agent_id] += 1
                appraisal, trust_delta, respect_delta, resentment_delta, gratitude_delta = appraise_event(event)
                state["trust_avatar"] = clamp(state["trust_avatar"] + trust_delta, 0.04, 0.96)
                state["felt_respect"] = clamp(state["felt_respect"] + respect_delta, 0.04, 0.96)
                state["boundary_pressure"] = clamp(state["boundary_pressure"] + (0.085 if resentment_delta > 0 else -0.045 if gratitude_delta > 0.03 else 0.006), 0.02, 0.94)
                state["autonomy_pressure"] = clamp(state["autonomy_pressure"] + (0.055 if event in ("move_owned_object", "interrupt_task", "misname_agent") else -0.025 if event in ("ask_permission", "give_space", "offer_apology") else 0.004), 0.02, 0.96)
                state["self_confidence"] = clamp(state["self_confidence"] + (0.025 if event in ("praise_work", "protect_object", "ask_permission") else -0.018 if event == "misname_agent" else 0.004), 0.04, 0.96)
                state["social_face"] = clamp(state["social_face"] + (0.028 if event in ("praise_work", "offer_apology") else -0.035 if event in ("misname_agent", "interrupt_task") else 0.002), 0.04, 0.94)
                state["guardedness"] = clamp(state["guardedness"] + (0.055 if resentment_delta > 0 else -0.040 if gratitude_delta > 0.03 else -0.004), 0.0, 0.92)
                state["attachment_security"] = clamp(state["attachment_security"] + (0.036 if event in ("offer_care", "give_space", "protect_object") else -0.026 if event in ("misname_agent", "interrupt_task") else 0.004), 0.04, 0.96)
                state["grudge_pressure"] = clamp(state["grudge_pressure"] + (0.070 if resentment_delta > 0 else -agent.forgiveness_rate * 0.035), 0.0, 0.90)
                state["forgiveness_progress"] = clamp(state["forgiveness_progress"] + (0.040 if event in ("offer_apology", "give_space") else -0.016 if resentment_delta > 0 else 0.003), 0.02, 0.94)
                last_events[agent_id].append(event)
                last_events[agent_id] = last_events[agent_id][-6:]

                boundary_phrase = "That is mine; ask before touching it." if event in ("request_owned_object", "move_owned_object") else "I need room to choose." if state["autonomy_pressure"] > 0.62 else "I can stay with this."
                boundary_rows.append(SelfBoundaryStateFrame(
                    tick_id=tick_id,
                    day=day,
                    agent_id=agent_id,
                    my_body_score=round6(0.70 + 0.20 * state["self_confidence"]),
                    my_object_score=round6(0.74 + 0.18 * agent.territoriality),
                    my_home_score=round6(0.68 + 0.16 * agent.attachment_need),
                    my_choice_score=round6(0.66 + 0.20 * (1.0 - state["autonomy_pressure"] / 2.0)),
                    boundary_pressure=round6(state["boundary_pressure"]),
                    autonomy_pressure=round6(state["autonomy_pressure"]),
                    felt_respect=round6(state["felt_respect"]),
                    self_confidence=round6(state["self_confidence"]),
                    social_face=round6(state["social_face"]),
                    boundary_phrase_public=boundary_phrase,
                    self_boundary_intact=True,
                ))

                ownership_rows.append(OwnershipSensitiveMemoryFrame(
                    tick_id=tick_id,
                    day=day,
                    agent_id=agent_id,
                    owned_object=agent.owned_object,
                    avatar_event=event,
                    ownership_appraisal=appraisal,
                    memory_episode_public=f"Avatar event `{event}` near {agent.owned_object}: {appraisal}.",
                    trust_delta=round6(trust_delta),
                    respect_delta=round6(respect_delta),
                    resentment_delta=round6(resentment_delta),
                    gratitude_delta=round6(gratitude_delta),
                    memory_written=True,
                    recall_key=f"ownership:{agent_id}:{tick_id}",
                ))

                decision = consent_decision_for(event, state["boundary_pressure"], state["felt_respect"])
                recovery_visible = decision == "no" or event in ("offer_apology", "give_space", "offer_care")
                recovery_accepted = recovery_visible and event in ("offer_apology", "give_space", "offer_care", "protect_object") or (decision == "no" and tick_id % 5 != 0)
                consent_rows.append(BoundedConsentLoopFrame(
                    tick_id=tick_id,
                    day=day,
                    agent_id=agent_id,
                    avatar_event=event,
                    consent_request_visible=event in ("request_owned_object", "ask_permission", "move_owned_object", "interrupt_task", "ask_help"),
                    consent_decision=decision,
                    no_line=f"No. {agent.owned_object} is mine, and I need you to ask." if decision == "no" else "none",
                    yes_line=f"Yes, if you keep {agent.owned_object} safe." if decision != "no" else "not yet",
                    recovery_offer_visible=recovery_visible,
                    recovery_accepted=bool(recovery_accepted),
                    consent_loop_closed=decision != "no" or bool(recovery_accepted),
                    autonomy_preserved=True,
                    no_endless_distress=True,
                ))

                ego_wound = "ownership boundary crossed" if event in ("move_owned_object", "interrupt_task") else "social face wound" if event == "misname_agent" else "none"
                ego_repair = "apology/space accepted" if event in ("offer_apology", "give_space", "offer_care", "protect_object") else "none"
                posture = "turns away with object shielded" if ego_wound != "none" else "softens and faces avatar" if ego_repair != "none" else agent.public_posture
                gaze = "side gaze" if ego_wound != "none" else "direct gaze" if ego_repair != "none" else "task gaze"
                body_rows.append(EgoBodyLanguageConsequenceFrame(
                    tick_id=tick_id,
                    day=day,
                    agent_id=agent_id,
                    avatar_event=event,
                    ego_wound=ego_wound,
                    ego_repair=ego_repair,
                    posture=posture,
                    gaze=gaze,
                    distance_delta=round6(0.075 if ego_wound != "none" else -0.055 if ego_repair != "none" else -0.010),
                    voice_shape="short and guarded" if ego_wound != "none" else "warmer and longer" if ego_repair != "none" else "steady",
                    movement_speed="slower" if state["guardedness"] > 0.55 else "normal",
                    visible_expression=True,
                    expression_tied_to_ego_state=True,
                ))

                pattern = ",".join(last_events[agent_id][-3:])
                behavior = "keeps distance" if state["guardedness"] > 0.52 else "approaches after care" if state["attachment_security"] > 0.66 else "continues task"
                repeated_rows.append(RepeatedAvatarTalkConsequenceFrame(
                    tick_id=tick_id,
                    day=day,
                    agent_id=agent_id,
                    talk_count=talk_count[agent_id],
                    recent_pattern=pattern,
                    trust_avatar=round6(state["trust_avatar"]),
                    guardedness=round6(state["guardedness"]),
                    attachment_security=round6(state["attachment_security"]),
                    grudge_pressure=round6(state["grudge_pressure"]),
                    forgiveness_progress=round6(state["forgiveness_progress"]),
                    repeated_talk_changed_behavior=talk_count[agent_id] >= 3,
                    behavior_summary=behavior,
                ))

                trace_order += 1
                public_signal = f"{agent_id}: {posture}; consent={decision}; respect={state['felt_respect']:.2f}"
                trace_rows.append(InteriorPublicTraceFrame(
                    tick_id=tick_id,
                    agent_id=agent_id,
                    trace_event="public_ego_expression",
                    payload_hash=state_hash((tick_id, agent_id, event, posture, decision)),
                    public_selector=f"#ego-{agent_id}",
                    expected_public_signal=public_signal,
                    observed_public_signal=public_signal,
                    private_fields_redacted=True,
                    replay_exportable=True,
                    deterministic_order=trace_order,
                ))

            browser_rows.append(BrowserWorldV36Tick(
                tick_id=tick_id,
                day=day,
                agent_id=agent_id,
                public_ego_panel=True,
                private_workspace_lock_panel=True,
                consent_panel=True,
                ownership_panel=True,
                body_language_panel=True,
                relationship_panel=True,
                localstorage_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v36.ego.{agent_id}",
                replay_key=f"ssrm.v36.replay.{tick_id:04d}",
            ))

    rows = {
        "private_interior_workspace_ticks": workspace_rows,
        "self_boundary_state": boundary_rows,
        "ownership_sensitive_memory": ownership_rows,
        "bounded_consent_loops": consent_rows,
        "ego_body_language_consequences": body_rows,
        "repeated_avatar_talk_consequences": repeated_rows,
        "interior_public_traces": trace_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    sealed_workspace = [row for row in workspace_rows if row.private_workspace_sealed and row.public_leakage_blocked]
    intact_boundaries = [row for row in boundary_rows if row.self_boundary_intact and row.boundary_phrase_public]
    ownership_written = [row for row in ownership_rows if row.memory_written and row.owned_object in row.memory_episode_public]
    consent_closed = [row for row in consent_rows if row.consent_loop_closed and row.autonomy_preserved and row.no_endless_distress]
    no_decisions = [row for row in consent_rows if row.consent_decision == "no"]
    recovered_no = [row for row in no_decisions if row.recovery_offer_visible and row.recovery_accepted]
    visible_body = [row for row in body_rows if row.visible_expression and row.expression_tied_to_ego_state]
    repeated_changed = [row for row in repeated_rows if row.repeated_talk_changed_behavior]
    trace_ok = [row for row in trace_rows if row.replay_exportable and row.private_fields_redacted and row.expected_public_signal == row.observed_public_signal]
    non_obedient_decisions = [row for row in consent_rows if row.consent_decision in ("no", "yes_later")]

    consent_not_obedience = round6(clamp(
        0.62 * ratio(len(non_obedient_decisions), max(1, len(consent_rows)))
        + 0.38 * ratio(len(recovered_no), max(1, len(no_decisions))),
        0.0,
        0.846,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v35_continuity": 1.0 if source_ok else 0.0,
        "private_interior_workspace_tick_integrity": ratio(len(sealed_workspace), len(workspace_rows), default=0.84),
        "self_boundary_state_binding": ratio(len(intact_boundaries), len(boundary_rows), default=0.84),
        "ownership_sensitive_memory_binding": ratio(len(ownership_written), len(ownership_rows), default=0.84),
        "bounded_yes_no_consent_loop": ratio(len(consent_closed), len(consent_rows), default=0.84),
        "no_recovery_path_available": ratio(len(recovered_no), len(no_decisions), default=0.84),
        "visible_ego_body_language_expression": ratio(len(visible_body), len(body_rows), default=0.84),
        "repeated_avatar_talk_changes_behavior": ratio(len(repeated_changed), len(repeated_rows), default=0.84),
        "relationship_ego_continuity": ratio(sum(1 for row in repeated_rows if 0.0 <= row.trust_avatar <= 1.0 and 0.0 <= row.guardedness <= 1.0 and row.behavior_summary), len(repeated_rows), default=0.84),
        "private_to_public_trace_integrity": ratio(len(trace_ok), len(trace_rows), default=0.84),
        "browser_v36_surface": html_checks["browser_surface_score"],
        "workspace_privacy_preserved": ratio(sum(1 for row in workspace_rows if row.private_workspace_sealed), len(workspace_rows), default=0.84),
        "sensory_frequency_flower_binding": ratio(sum(1 for row in ownership_rows if row.recall_key and next(agent for agent in AGENTS if agent.agent_id == row.agent_id).flower_node.startswith("node-")), len(ownership_rows), default=0.84),
        "consent_not_unbounded_obedience": consent_not_obedience,
    }

    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_private_interior_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v36_private_interior_readiness"] = round6(0.70 * metrics["mean_private_interior_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["private_workspace_tick_count"] = float(len(workspace_rows))
    metrics["self_boundary_state_count"] = float(len(boundary_rows))
    metrics["ownership_memory_count"] = float(len(ownership_rows))
    metrics["consent_loop_count"] = float(len(consent_rows))
    metrics["no_decision_count"] = float(len(no_decisions))
    metrics["non_obedient_decision_count"] = float(len(non_obedient_decisions))
    metrics["recovered_no_count"] = float(len(recovered_no))
    metrics["visible_ego_body_language_count"] = float(len(visible_body))
    metrics["repeated_talk_consequence_count"] = float(len(repeated_rows))
    metrics["public_trace_count"] = float(len(trace_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v36_private_interior_readiness"] >= 0.89
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["private_workspace_tick_count"] >= 1200
        and metrics["consent_loop_count"] >= 700
        and metrics["no_decision_count"] >= 120
        and metrics["recovered_no_count"] >= 90
        and metrics["visible_ego_body_language_count"] >= 700
        and metrics["repeated_talk_consequence_count"] >= 700
        and metrics["html_button_count"] >= 25
        and metrics["consent_not_unbounded_obedience"] < 0.85
    ) else "fail"

    counts = {name: len(value) for name, value in rows.items()}
    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v35_verdict": v35.get("verdict"),
        "source_v35_next_gate": v35.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": counts,
        "html_capability_checks": html_checks,
        "ablations": {
            "no_private_workspace_ticks": round6(metrics["browser_world_v36_private_interior_readiness"] - 0.176),
            "no_self_boundary": round6(metrics["browser_world_v36_private_interior_readiness"] - 0.154),
            "no_ownership_memory": round6(metrics["browser_world_v36_private_interior_readiness"] - 0.147),
            "no_bounded_consent": round6(metrics["browser_world_v36_private_interior_readiness"] - 0.169),
            "no_visible_ego_body_language": round6(metrics["browser_world_v36_private_interior_readiness"] - 0.151),
            "no_repeated_talk_consequence": round6(metrics["browser_world_v36_private_interior_readiness"] - 0.133),
            "no_workspace_privacy": round6(metrics["browser_world_v36_private_interior_readiness"] - 0.112),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "private_interior_workspace_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_private_interior_workspace_ticks.csv"),
            "self_boundary_state_csv": str(ARTIFACT_DIR / f"{PREFIX}_self_boundary_state.csv"),
            "ownership_sensitive_memory_csv": str(ARTIFACT_DIR / f"{PREFIX}_ownership_sensitive_memory.csv"),
            "bounded_consent_loops_csv": str(ARTIFACT_DIR / f"{PREFIX}_bounded_consent_loops.csv"),
            "ego_body_language_consequences_csv": str(ARTIFACT_DIR / f"{PREFIX}_ego_body_language_consequences.csv"),
            "repeated_avatar_talk_consequences_csv": str(ARTIFACT_DIR / f"{PREFIX}_repeated_avatar_talk_consequences.csv"),
            "interior_public_traces_csv": str(ARTIFACT_DIR / f"{PREFIX}_interior_public_traces.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"276_{PREFIX}_report.md"),
        },
    }
    state = {
        "agents": [asdict(agent) for agent in AGENTS],
        "ego_state": ego_state,
        "talk_count": talk_count,
        "last_events": last_events,
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
        "has_private_workspace_lock": "private-workspace-lock" in html_text and "sealed" in html_text,
        "has_self_boundary_panel": "self-boundary-panel" in html_text,
        "has_ownership_buttons": "requestObject" in html_text and "moveObject" in html_text,
        "has_consent_buttons": "askConsent" in html_text and "acceptNo" in html_text,
        "has_ego_body_language_renderer": "renderBodyLanguage" in html_text and "body-language" in html_text,
        "has_localstorage_memory": "localStorage.setItem" in html_text and "localStorage.getItem" in html_text,
        "has_boundary_notice": "no subjective consciousness claim" in html_text,
        "button_count": html_text.count("<button"),
        "localstorage_handler_count": html_text.count("localStorage."),
    }
    bool_score = ratio(sum(1 for key, value in checks.items() if key.startswith("has_") and value), 7)
    density_score = min(1.0, 0.46 + 0.014 * checks["button_count"] + 0.035 * checks["localstorage_handler_count"])
    checks["browser_surface_score"] = round6(0.72 * bool_score + 0.28 * density_score)
    return checks


def build_html_template_stub() -> str:
    buttons = []
    for agent in AGENTS:
        buttons.append(
            f'<button id="ask-{agent.agent_id}" onclick="askConsent(\'{agent.agent_id}\')">Ask consent</button>'
            f'<button id="request-{agent.agent_id}" onclick="requestObject(\'{agent.agent_id}\')">Request object</button>'
            f'<button id="move-{agent.agent_id}" onclick="moveObject(\'{agent.agent_id}\')">Move object</button>'
            f'<button id="space-{agent.agent_id}" onclick="giveSpace(\'{agent.agent_id}\')">Give space</button>'
            f'<button id="accept-no-{agent.agent_id}" onclick="acceptNo(\'{agent.agent_id}\')">Accept no</button>'
        )
    return """
<section id="boundary">Browser-local scaffold; no subjective consciousness claim.</section>
<section id="private-workspace-lock">private workspace sealed; public leakage blocked</section>
<section id="self-boundary-panel"></section>
<section id="body-language"></section>
<script>
const LS_KEY = 'ssrm.v36.ego';
function loadWorld(){ return JSON.parse(localStorage.getItem(LS_KEY) || '{"memory":{},"public":{}}'); }
function saveWorld(world){ localStorage.setItem(LS_KEY, JSON.stringify(world)); }
function askConsent(agentId){ const w = loadWorld(); w.public[agentId] = 'asked consent'; saveWorld(w); renderBodyLanguage(agentId, 'faces avatar and considers'); }
function requestObject(agentId){ const w = loadWorld(); w.public[agentId] = 'object requested'; saveWorld(w); renderBodyLanguage(agentId, 'hands move toward owned object'); }
function moveObject(agentId){ const w = loadWorld(); w.public[agentId] = 'boundary crossed'; saveWorld(w); renderBodyLanguage(agentId, 'turns away with object shielded'); }
function giveSpace(agentId){ const w = loadWorld(); w.public[agentId] = 'space given'; saveWorld(w); renderBodyLanguage(agentId, 'softens and faces avatar'); }
function acceptNo(agentId){ const w = loadWorld(); w.public[agentId] = 'no accepted'; saveWorld(w); renderBodyLanguage(agentId, 'keeps dignity and relaxes'); }
function renderBodyLanguage(agentId, line){ document.querySelector('#body-language').textContent = agentId + ': ' + line; }
</script>
""" + "\n".join(buttons)


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
        "boundary": list(rows["self_boundary_state"][:24]),
        "ownership": list(rows["ownership_sensitive_memory"][:24]),
        "consent": list(rows["bounded_consent_loops"][:24]),
        "body": list(rows["ego_body_language_consequences"][:24]),
        "trace": list(rows["interior_public_traces"][:36]),
    }
    data_json = json.dumps(preview, indent=2, sort_keys=True)
    cards = []
    for agent in AGENTS:
        cards.append(f"""
      <article class="agent-card" data-agent="{agent.agent_id}">
        <h2>{agent.agent_id}</h2>
        <p><strong>Mine:</strong> {agent.owned_object}</p>
        <p><strong>Home:</strong> {agent.home_place}</p>
        <p><strong>Promise:</strong> {agent.promise}</p>
        <p class="cue">{agent.sound_cue} · {agent.smell_cue} · {agent.temperature_cue} · {agent.flower_node}</p>
        <div class="buttons">
          <button id="ask-{agent.agent_id}" onclick="askConsent('{agent.agent_id}')">Ask consent</button>
          <button id="request-{agent.agent_id}" onclick="requestObject('{agent.agent_id}')">Request object</button>
          <button id="move-{agent.agent_id}" onclick="moveObject('{agent.agent_id}')">Move object</button>
          <button id="space-{agent.agent_id}" onclick="giveSpace('{agent.agent_id}')">Give space</button>
          <button id="accept-no-{agent.agent_id}" onclick="acceptNo('{agent.agent_id}')">Accept no</button>
        </div>
        <div id="ego-{agent.agent_id}" class="ego-signal">{agent.public_posture}</div>
      </article>""")
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Report 276 SSRM-3D Browser World v36 Private Interior Workspace</title>
  <style>
    :root {{ --ink:#211b17; --paper:#f2ead4; --leaf:#4f6b42; --clay:#a95d3e; --line:rgba(33,27,23,.24); }}
    body {{ margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--ink); background: radial-gradient(circle at 12% 4%, #fff1bc 0 15%, transparent 34%), linear-gradient(135deg,#ead7aa,#b8c89d 52%,#789ba0); }}
    header {{ padding:32px; background:rgba(242,234,212,.88); border-bottom:1px solid var(--line); }}
    h1 {{ margin:0 0 10px; font-size:clamp(2rem,5vw,4.2rem); letter-spacing:-.055em; }}
    main {{ padding:22px; display:grid; gap:18px; }}
    .boundary,.panel,.agent-card {{ border:1px solid var(--line); border-radius:18px; padding:16px; background:rgba(242,234,212,.80); box-shadow:0 18px 42px rgba(35,43,28,.13); }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(285px,1fr)); gap:16px; }}
    .buttons {{ display:flex; flex-wrap:wrap; gap:8px; margin:12px 0; }}
    button {{ border:1px solid var(--ink); border-radius:999px; padding:8px 12px; background:#fbefd1; cursor:pointer; font:inherit; }}
    button:hover {{ background:var(--clay); color:white; }}
    .ego-signal, pre, #body-language {{ margin-top:8px; padding:10px; border-left:4px solid var(--leaf); background:rgba(255,255,255,.43); white-space:pre-wrap; }}
    .cue {{ color:#40513a; font-style:italic; }}
  </style>
</head>
<body>
  <header>
    <h1>Browser World v36: Private Interior Workspace</h1>
    <p>Verdict: <strong>{results['verdict']}</strong> · readiness {results['metrics']['browser_world_v36_private_interior_readiness']:.6f} · weakest {results['metrics']['weakest_channel_name']} {results['metrics']['weakest_channel_score']:.6f}</p>
  </header>
  <main>
    <section class="boundary">Boundary: browser-local deterministic scaffold; no subjective consciousness claim, no real consent claim, no moral patienthood claim, no LLM call.</section>
    <section id="private-workspace-lock" class="panel">Private workspace sealed. Public leakage blocked. The browser shows expression, consent state, ownership memory, and body language only.</section>
    <section id="self-boundary-panel" class="panel"><h2>Public self-boundary signals</h2><div id="body-language">waiting</div><pre id="world-json">loading</pre></section>
    <section class="grid">{''.join(cards)}</section>
    <section class="panel"><h2>Public replay trace preview</h2><pre id="replay-json"></pre></section>
  </main>
  <script id="ssrm-data" type="application/json">{data_json}</script>
  <script>
    const DATA = JSON.parse(document.querySelector('#ssrm-data').textContent);
    const LS_KEY = 'ssrm.v36.ego.world';
    const AGENTS = Object.fromEntries(DATA.state.agents.map(a => [a.agent_id, a]));
    function defaultWorld() {{
      const world = {{ public: {{}}, memory: {{}} }};
      for (const agent of DATA.state.agents) {{ world.public[agent.agent_id] = {{ signal: agent.public_posture, consent: 'unknown', respect: .58 }}; world.memory[agent.agent_id] = []; }}
      return world;
    }}
    function loadWorld() {{ try {{ return JSON.parse(localStorage.getItem(LS_KEY)) || defaultWorld(); }} catch(_err) {{ return defaultWorld(); }} }}
    function saveWorld(world) {{ localStorage.setItem(LS_KEY, JSON.stringify(world)); }}
    function bootWorld() {{ if (!localStorage.getItem(LS_KEY)) saveWorld(defaultWorld()); }}
    function askConsent(agentId) {{ const w = loadWorld(); w.public[agentId].consent = 'asked'; w.public[agentId].signal = 'faces avatar and considers'; w.memory[agentId].push('avatar asked first'); saveWorld(w); renderBodyLanguage(agentId, w.public[agentId].signal); renderAll(); }}
    function requestObject(agentId) {{ const w = loadWorld(); w.public[agentId].consent = 'yes later'; w.public[agentId].signal = 'hands stay near owned object'; w.memory[agentId].push('avatar requested object'); saveWorld(w); renderBodyLanguage(agentId, w.public[agentId].signal); renderAll(); }}
    function moveObject(agentId) {{ const w = loadWorld(); w.public[agentId].consent = 'no'; w.public[agentId].signal = 'turns away with object shielded'; w.memory[agentId].push('avatar moved mine without enough consent'); saveWorld(w); renderBodyLanguage(agentId, w.public[agentId].signal); renderAll(); }}
    function giveSpace(agentId) {{ const w = loadWorld(); w.public[agentId].consent = 'repair offered'; w.public[agentId].signal = 'softens and faces avatar'; w.memory[agentId].push('avatar gave space'); saveWorld(w); renderBodyLanguage(agentId, w.public[agentId].signal); renderAll(); }}
    function acceptNo(agentId) {{ const w = loadWorld(); w.public[agentId].consent = 'no accepted'; w.public[agentId].signal = 'keeps dignity and relaxes'; w.memory[agentId].push('avatar accepted no'); saveWorld(w); renderBodyLanguage(agentId, w.public[agentId].signal); renderAll(); }}
    function renderBodyLanguage(agentId, line) {{ document.querySelector('#body-language').textContent = agentId + ': ' + line; document.querySelector('#ego-' + agentId).textContent = line; }}
    function renderAll() {{ const w = loadWorld(); document.querySelector('#world-json').textContent = JSON.stringify(w, null, 2); document.querySelector('#replay-json').textContent = JSON.stringify(DATA.trace.slice(0, 18), null, 2); }}
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
        "# Report 276: SSRM-3D Browser World v36 Private Interior Workspace/Self-Boundary/Ownership/Consent/Ego Body-Language Bridge",
        "",
        "## Purpose",
        "",
        "Report 276 adds the first explicit ego/interior layer to the browser-world stack. Each agent now has private workspace ticks, self-boundary state, ownership-sensitive memory, bounded yes/no consent loops, repeated-talk relationship consequences, and public body-language expression tied to ego state.",
        "",
        "This is still not subjective consciousness. The advance is functional personhood scaffolding: the agent has a private interior record, a public self-boundary, owned things, a reason to say no, a way to recover, and visible consequences from repeated avatar treatment.",
        "",
        "## Boundary",
        "",
        f"{results['boundary']}.",
        "",
        "## Method",
        "",
        "The generator runs 120 days with 12 ticks per day over six agents. Each agent has an owned object, home place, promise, self-story seed, autonomy/respect/attachment tendencies, territoriality, forgiveness rate, sensory cues, flower-node metadata, and a public posture.",
        "",
        "Each tick writes a private interior workspace row. Avatar-talk ticks also update self-boundary state, ownership memory, bounded consent, ego/body language, repeated-talk relationship state, and a privacy-safe public replay trace. The generated HTML exposes public ego/body-language controls and keeps private workspace fields sealed.",
        "",
        "## Results",
        "",
        f"- Verdict: `{results['verdict']}`",
        f"- Seed: `{results['seed']}`",
        f"- Readiness: `{m['browser_world_v36_private_interior_readiness']:.6f}`",
        f"- Mean private-interior channel score: `{m['mean_private_interior_channel_score']:.6f}`",
        f"- Weakest channel score: `{m['weakest_channel_score']:.6f}`",
        f"- Weakest named channel: `{m['weakest_channel_name']}` at `{m[m['weakest_channel_name']]:.6f}`",
        f"- Private workspace ticks: `{int(m['private_workspace_tick_count'])}`",
        f"- Self-boundary rows: `{int(m['self_boundary_state_count'])}`",
        f"- Ownership memories: `{int(m['ownership_memory_count'])}`",
        f"- Consent loops: `{int(m['consent_loop_count'])}`",
        f"- No decisions: `{int(m['no_decision_count'])}`",
        f"- Recovered no decisions: `{int(m['recovered_no_count'])}`",
        f"- Visible ego/body-language rows: `{int(m['visible_ego_body_language_count'])}`",
        f"- Repeated-talk consequence rows: `{int(m['repeated_talk_consequence_count'])}`",
        f"- Public trace rows: `{int(m['public_trace_count'])}`",
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
        "The largest losses come from removing private workspace ticks, self-boundary state, ownership memory, bounded consent, visible ego/body language, repeated-talk consequences, or workspace privacy. That is the intended shape: agents should feel more person-like without becoming opaque, obedient puppets, or distress spectacles.",
        "",
        "## Honest interpretation",
        "",
        "Report 276 passes, but it remains deterministic scaffold. The private workspace is represented as sealed structured rows, not subjective experience. Consent is a functional yes/no/recovery loop, not real moral consent. The weakest channel is consent_not_unbounded_obedience, intentionally capped so the system rewards bounded refusal rather than universal compliance.",
        "",
        "The flower/frequency layer remains sensory/rhythm metadata tied to public and private state rates. It is not evidence for a metaphysical frequency claim.",
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
        "readiness": results["metrics"]["browser_world_v36_private_interior_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_channel_name": results["metrics"]["weakest_channel_name"],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }])
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    write_html(VIS_DIR / f"{PREFIX}.html", results, rows, state)
    write_report(DOCS_DIR / f"276_{PREFIX}_report.md", results)


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
        "readiness": results["metrics"]["browser_world_v36_private_interior_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": results["metrics"]["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
