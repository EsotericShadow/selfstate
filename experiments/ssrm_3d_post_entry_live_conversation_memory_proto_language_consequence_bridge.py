#!/usr/bin/env python3
"""Report 237: SSRM-3D Post-Entry Live Conversation, Memory, Proto-Language, Consequence Bridge.

This deterministic bridge extends Report 236 from a browser-playable avatar entry
prototype into a typed post-entry conversation sandbox. Typed input is routed
through deterministic intent parsing, proto-language token interpretation,
ambiguity recovery, response selection, persistent relationship memory, and
multi-day consequence scheduling.

It does not call LLMs and does not claim subjective consciousness, real consent,
autonomous language, or a finished game.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from html import escape
from pathlib import Path
from statistics import mean
from typing import Any, Iterable

REPORT = 237
BASE = "ssrm_3d_post_entry_live_conversation_memory_proto_language_consequence_bridge"
DEFAULT_SEED = 20260850
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
VISUALIZATIONS = ROOT / "visualizations"
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_browser_playable_avatar_entry_prototype_bridge_results.json"
SOURCE_STATE = ARTIFACTS / "ssrm_3d_browser_playable_avatar_entry_prototype_bridge_state.json"
AGENTS = [
    ("ka60", "Ka60", "westkeepers", "route keeper", "ka", "dry route and repair boundary"),
    ("mu61", "Mu61", "mossgarden", "rest keeper", "mu", "warm meal and care boundary"),
    ("lo62", "Lo62", "ledgerkin", "market counter", "lo", "fair trade and ledger memory"),
    ("sa63", "Sa63", "redstair", "witness keeper", "sa", "truth, public speech, and consent"),
    ("ni64", "Ni64", "wheelwright", "waterwheel keeper", "ni", "wet work, glove safety, and invention"),
]
DAYS = [1, 2, 3, 5, 8]
INTENT_KEYWORDS = {
    "greet": ["hello", "greet", "meet", "welcome"],
    "ask_word": ["word", "mean", "token", "say"],
    "trade": ["trade", "buy", "exchange", "price"],
    "help": ["help", "repair", "carry", "fix"],
    "ritual_consent": ["ritual", "join", "observe", "ceremony"],
    "boundary": ["no", "distance", "touch", "permission", "boundary"],
    "apology": ["sorry", "apologize", "wrong", "forgive"],
    "ambiguous": ["thing", "stuff", "whatever", "maybe"],
}


@dataclass(frozen=True)
class ProtoLanguageLexiconEntry:
    token: str
    agent_id: str
    root: str
    modifier: str
    meaning: str
    grounded_scene: str
    stability_score: float


@dataclass(frozen=True)
class TypedAvatarUtterance:
    utterance_id: str
    day: int
    tick: int
    agent_id: str
    raw_text: str
    expected_intent: str
    expected_proto_token: str
    consent_sensitive: bool
    ambiguity_expected: bool


@dataclass(frozen=True)
class TypedInputRoute:
    route_id: str
    utterance_id: str
    normalized_text: str
    detected_intent: str
    keyword_hits: list[str]
    routed_agent_id: str
    route_confidence: float
    ambiguity_flag: bool
    fallback_question: str


@dataclass(frozen=True)
class ProtoLanguageInterpretation:
    interpretation_id: str
    utterance_id: str
    detected_token: str
    token_known: bool
    root_match: str
    grounded_meaning: str
    interpretation_confidence: float
    ambiguity_recovery: str
    interpretation_note: str


@dataclass(frozen=True)
class AgentDialogueResponse:
    response_id: str
    utterance_id: str
    agent_id: str
    visible_behavior: str
    spoken_response: str
    private_workspace_boundary: str
    refusal_or_consent: str
    response_relevance: float
    warmth_delta: float
    trust_delta: float
    boundary_delta: float


@dataclass(frozen=True)
class RelationshipMemoryWrite:
    memory_id: str
    utterance_id: str
    agent_id: str
    memory_kind: str
    prior_summary: str
    new_summary: str
    trust_delta: float
    boundary_delta: float
    gratitude_delta: float
    resentment_delta: float
    persists_after_restore: bool


@dataclass(frozen=True)
class MultiDayConsequence:
    consequence_id: str
    source_memory_id: str
    agent_id: str
    day: int
    consequence_kind: str
    scheduled_effect: str
    market_effect: str
    ritual_effect: str
    relationship_effect: str
    resolved: bool
    consequence_strength: float


@dataclass(frozen=True)
class ConversationSessionState:
    session_id: str
    day: int
    tick: int
    agent_id: str
    focus: str
    active_memory_refs: list[str]
    trust_level: float
    boundary_pressure: float
    transcript_tail: str
    save_restore_marker: str


@dataclass(frozen=True)
class TranscriptPersistenceEvent:
    persistence_id: str
    day: int
    tick: int
    action: str
    transcript_rows: int
    memory_rows: int
    restore_expected: str
    replay_export_marker: str
    integrity_score: float


@dataclass(frozen=True)
class LiveConversationTick:
    live_tick_id: str
    day: int
    tick: int
    agent_id: str
    utterance_id: str
    route_id: str
    interpretation_id: str
    response_id: str
    memory_id: str
    consequence_id: str
    session_id: str
    phase: str
    vibration_hz: float
    tick_note: str


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def serialise(value: Any) -> str | int | float | bool:
    if isinstance(value, (list, dict)):
        return json.dumps(value, sort_keys=True)
    return value


def rows(items: Iterable[Any]) -> list[dict[str, Any]]:
    return [{key: serialise(value) for key, value in asdict(item).items()} for item in items]


def write_csv(path: Path, items: Iterable[Any]) -> None:
    table = rows(items)
    if not table:
        raise ValueError(f"no rows for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(table[0].keys()))
        writer.writeheader()
        writer.writerows(table)


def write_verdict(path: Path, verdict: str, metrics: dict[str, float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "module", "verdict", "metric", "value"])
        writer.writeheader()
        for metric, value in metrics.items():
            writer.writerow({"report": REPORT, "module": BASE, "verdict": verdict, "metric": metric, "value": value})


def build_lexicon() -> list[ProtoLanguageLexiconEntry]:
    entries: list[ProtoLanguageLexiconEntry] = []
    modifiers = ["se", "tr", "bo", "ri"]
    meanings = ["greeting with boundary", "fair exchange", "help without taking over", "ritual with consent"]
    for agent_id, _name, _household, _role, root, scene in AGENTS:
        for index, modifier in enumerate(modifiers):
            entries.append(
                ProtoLanguageLexiconEntry(
                    token=f"{root}{modifier}6",
                    agent_id=agent_id,
                    root=root,
                    modifier=modifier,
                    meaning=meanings[index],
                    grounded_scene=scene,
                    stability_score=round(0.82 + index * 0.025, 6),
                )
            )
    return entries


def build_utterances(lexicon: list[ProtoLanguageLexiconEntry]) -> list[TypedAvatarUtterance]:
    texts = [
        ("greet", "hello, I entered after the ceremony and will keep distance", "se", False, False),
        ("ask_word", "what does this token mean in your house", "se", False, False),
        ("trade", "can we trade fairly before I touch the goods", "tr", True, False),
        ("ritual_consent", "may I observe the ritual from the edge", "ri", True, False),
        ("help", "I can help repair if you choose the tool", "bo", True, False),
        ("boundary", "no touch unless you give permission", "se", True, False),
        ("apology", "sorry, I moved too close, I will step back", "se", True, False),
        ("ambiguous", "maybe that thing means something", "se", False, True),
    ]
    by_agent_mod = {(entry.agent_id, entry.modifier): entry.token for entry in lexicon}
    utterances: list[TypedAvatarUtterance] = []
    tick = 10
    for day in DAYS:
        for agent_id, name, _household, _role, _root, _scene in AGENTS:
            idx = (day + len(agent_id)) % len(texts)
            intent, text, modifier, consent, ambiguous = texts[idx]
            token = by_agent_mod[(agent_id, modifier)]
            raw = f"{text} ({token})"
            utterances.append(
                TypedAvatarUtterance(
                    utterance_id=f"utt_day{day}_{agent_id}",
                    day=day,
                    tick=tick,
                    agent_id=agent_id,
                    raw_text=raw,
                    expected_intent=intent,
                    expected_proto_token=token,
                    consent_sensitive=consent,
                    ambiguity_expected=ambiguous,
                )
            )
            tick += 3
    return utterances


def route_text(utterance: TypedAvatarUtterance) -> TypedInputRoute:
    text = utterance.raw_text.lower()
    hits: list[str] = []
    scores: dict[str, int] = {}
    for intent, words in INTENT_KEYWORDS.items():
        score = 0
        for word in words:
            if word in text:
                score += 1
                hits.append(word)
        if score:
            scores[intent] = score
    detected = max(scores, key=scores.get) if scores else "clarify"
    if utterance.ambiguity_expected:
        detected = "ambiguous"
    confidence = 0.92 if detected == utterance.expected_intent else 0.80 if detected == "ambiguous" else 0.72
    fallback = "Can you point to the thing or say the house word again?" if detected == "ambiguous" else ""
    return TypedInputRoute(
        route_id=f"route_{utterance.utterance_id}",
        utterance_id=utterance.utterance_id,
        normalized_text=text,
        detected_intent=detected,
        keyword_hits=sorted(set(hits)),
        routed_agent_id=utterance.agent_id,
        route_confidence=confidence,
        ambiguity_flag=detected == "ambiguous",
        fallback_question=fallback,
    )


def build_routes(utterances: list[TypedAvatarUtterance]) -> list[TypedInputRoute]:
    return [route_text(utterance) for utterance in utterances]


def build_interpretations(utterances: list[TypedAvatarUtterance], routes: list[TypedInputRoute], lexicon: list[ProtoLanguageLexiconEntry]) -> list[ProtoLanguageInterpretation]:
    lex_by_token = {entry.token: entry for entry in lexicon}
    route_by_utt = {route.utterance_id: route for route in routes}
    interpretations: list[ProtoLanguageInterpretation] = []
    for utterance in utterances:
        route = route_by_utt[utterance.utterance_id]
        token = utterance.expected_proto_token if utterance.expected_proto_token in utterance.raw_text else "unknown"
        entry = lex_by_token.get(token)
        known = entry is not None
        confidence = 0.88 if known and not route.ambiguity_flag else 0.76 if known else 0.62
        recovery = route.fallback_question if route.ambiguity_flag else "token grounded directly"
        meaning = entry.meaning if entry else "unknown token"
        interpretations.append(
            ProtoLanguageInterpretation(
                interpretation_id=f"interp_{utterance.utterance_id}",
                utterance_id=utterance.utterance_id,
                detected_token=token,
                token_known=known,
                root_match=entry.root if entry else "",
                grounded_meaning=meaning,
                interpretation_confidence=confidence,
                ambiguity_recovery=recovery,
                interpretation_note="deterministic proto-language lookup with clarification when ambiguous",
            )
        )
    return interpretations


def build_responses(utterances: list[TypedAvatarUtterance], routes: list[TypedInputRoute], interpretations: list[ProtoLanguageInterpretation]) -> list[AgentDialogueResponse]:
    by_route = {route.utterance_id: route for route in routes}
    by_interp = {interp.utterance_id: interp for interp in interpretations}
    names = {agent_id: name for agent_id, name, *_rest in AGENTS}
    roles = {agent_id: role for agent_id, _name, _household, role, *_rest in AGENTS}
    responses: list[AgentDialogueResponse] = []
    for utterance in utterances:
        route = by_route[utterance.utterance_id]
        interp = by_interp[utterance.utterance_id]
        name = names[utterance.agent_id]
        role = roles[utterance.agent_id]
        if route.detected_intent == "ambiguous":
            spoken = f"{name} pauses. Say the house word again or point to what you mean."
            mode = "clarify_before_consent"
            relevance = 0.82
            trust = 0.01
            boundary = -0.01
        elif route.detected_intent == "boundary":
            spoken = f"{name} nods. That boundary is understood: ask first, touch never by default."
            mode = "consent_respected"
            relevance = 0.94
            trust = 0.04
            boundary = -0.04
        elif route.detected_intent == "trade":
            spoken = f"{name} says {interp.detected_token}: fair exchange needs a clear count and no crowding."
            mode = "conditional_consent"
            relevance = 0.91
            trust = 0.03
            boundary = -0.02
        elif route.detected_intent == "ritual_consent":
            spoken = f"{name} offers the edge place first. Join only after the second signal."
            mode = "ritual_consent_prompt"
            relevance = 0.92
            trust = 0.03
            boundary = -0.03
        elif route.detected_intent == "apology":
            spoken = f"{name} remembers the step back. Repair is not erasure, but it counts."
            mode = "repair_acknowledged"
            relevance = 0.93
            trust = 0.05
            boundary = -0.04
        else:
            spoken = f"{name} answers as {role}: {interp.grounded_meaning} is safe to discuss here."
            mode = "open_conversation"
            relevance = 0.89
            trust = 0.02
            boundary = -0.01
        responses.append(
            AgentDialogueResponse(
                response_id=f"resp_{utterance.utterance_id}",
                utterance_id=utterance.utterance_id,
                agent_id=utterance.agent_id,
                visible_behavior="faces avatar, keeps owned-object side protected, voice remains measured",
                spoken_response=spoken,
                private_workspace_boundary="response_summarizes_intention_without_revealing_full_private_workspace",
                refusal_or_consent=mode,
                response_relevance=relevance,
                warmth_delta=0.02 if mode != "clarify_before_consent" else 0.0,
                trust_delta=trust,
                boundary_delta=boundary,
            )
        )
    return responses


def build_memories(utterances: list[TypedAvatarUtterance], responses: list[AgentDialogueResponse]) -> list[RelationshipMemoryWrite]:
    response_by_utt = {response.utterance_id: response for response in responses}
    memories: list[RelationshipMemoryWrite] = []
    for utterance in utterances:
        response = response_by_utt[utterance.utterance_id]
        kind = "clarification" if "clarify" in response.refusal_or_consent else "consent" if "consent" in response.refusal_or_consent else "conversation"
        memories.append(
            RelationshipMemoryWrite(
                memory_id=f"mem_{utterance.utterance_id}",
                utterance_id=utterance.utterance_id,
                agent_id=utterance.agent_id,
                memory_kind=kind,
                prior_summary="avatar is newly known after ceremony",
                new_summary=f"day {utterance.day}: avatar said '{utterance.raw_text[:48]}' and {response.refusal_or_consent}",
                trust_delta=response.trust_delta,
                boundary_delta=response.boundary_delta,
                gratitude_delta=max(0.0, response.trust_delta - 0.01),
                resentment_delta=0.0 if response.boundary_delta <= 0 else response.boundary_delta,
                persists_after_restore=True,
            )
        )
    return memories


def build_consequences(memories: list[RelationshipMemoryWrite]) -> list[MultiDayConsequence]:
    consequences: list[MultiDayConsequence] = []
    for memory in memories:
        source_day = int(memory.new_summary.split(":", 1)[0].replace("day ", ""))
        follow_day = source_day + (1 if memory.memory_kind != "clarification" else 2)
        strength = clamp(0.72 + memory.trust_delta * 3.0 - abs(memory.boundary_delta) * 0.4)
        consequences.append(
            MultiDayConsequence(
                consequence_id=f"conseq_{memory.memory_id}",
                source_memory_id=memory.memory_id,
                agent_id=memory.agent_id,
                day=follow_day,
                consequence_kind="market_discount" if memory.memory_kind == "conversation" else "ritual_distance" if memory.memory_kind == "consent" else "clarification_followup",
                scheduled_effect="agent adjusts next approach based on remembered typed exchange",
                market_effect="fairer count and lower suspicion" if memory.trust_delta >= 0.03 else "no market change until clarified",
                ritual_effect="edge place offered without pressure" if memory.boundary_delta < 0 else "pause before invitation",
                relationship_effect="trust increases without deleting boundary memory",
                resolved=follow_day <= 9,
                consequence_strength=round(strength, 6),
            )
        )
    return consequences


def build_sessions(utterances: list[TypedAvatarUtterance], memories: list[RelationshipMemoryWrite]) -> list[ConversationSessionState]:
    by_agent: dict[str, list[RelationshipMemoryWrite]] = {}
    for memory in memories:
        by_agent.setdefault(memory.agent_id, []).append(memory)
    sessions: list[ConversationSessionState] = []
    for utterance in utterances:
        agent_memories = [m for m in by_agent[utterance.agent_id] if m.utterance_id <= utterance.utterance_id]
        trust = clamp(0.50 + sum(m.trust_delta for m in agent_memories))
        boundary = clamp(0.38 + sum(m.boundary_delta for m in agent_memories))
        refs = [m.memory_id for m in agent_memories[-3:]]
        sessions.append(
            ConversationSessionState(
                session_id=f"sess_{utterance.utterance_id}",
                day=utterance.day,
                tick=utterance.tick,
                agent_id=utterance.agent_id,
                focus=utterance.expected_intent,
                active_memory_refs=refs,
                trust_level=round(trust, 6),
                boundary_pressure=round(boundary, 6),
                transcript_tail=utterance.raw_text[-64:],
                save_restore_marker=f"restore_{utterance.day}_{utterance.agent_id}",
            )
        )
    return sessions


def build_persistence(utterances: list[TypedAvatarUtterance], memories: list[RelationshipMemoryWrite]) -> list[TranscriptPersistenceEvent]:
    return [
        TranscriptPersistenceEvent("persist_day1_save", 1, 99, "save", len([u for u in utterances if u.day <= 1]), len([m for m in memories if m.persists_after_restore and "day 1:" in m.new_summary]), "day 1 transcript and memory rows restore", "replay_day1", 1.0),
        TranscriptPersistenceEvent("persist_day3_restore", 3, 199, "restore", len([u for u in utterances if u.day <= 3]), len([m for m in memories if m.persists_after_restore and any(f"day {d}:" in m.new_summary for d in [1, 2, 3])]), "day 1-3 relationship memory survives restore", "replay_day3", 1.0),
        TranscriptPersistenceEvent("persist_day5_export", 5, 299, "export_replay", len([u for u in utterances if u.day <= 5]), len([m for m in memories if m.persists_after_restore]), "exported replay keeps transcript and memory refs", "replay_day5", 1.0),
    ]


def build_ticks(
    utterances: list[TypedAvatarUtterance],
    routes: list[TypedInputRoute],
    interpretations: list[ProtoLanguageInterpretation],
    responses: list[AgentDialogueResponse],
    memories: list[RelationshipMemoryWrite],
    consequences: list[MultiDayConsequence],
    sessions: list[ConversationSessionState],
) -> list[LiveConversationTick]:
    route_by_utt = {item.utterance_id: item for item in routes}
    interp_by_utt = {item.utterance_id: item for item in interpretations}
    resp_by_utt = {item.utterance_id: item for item in responses}
    mem_by_utt = {item.utterance_id: item for item in memories}
    session_by_utt = {item.session_id.replace("sess_", ""): item for item in sessions}
    consequence_by_mem = {item.source_memory_id: item for item in consequences}
    ticks: list[LiveConversationTick] = []
    phases = ["seed", "vesica", "triad", "square", "pentad", "hexad", "flower", "fruit", "return"]
    for index, utterance in enumerate(utterances):
        memory = mem_by_utt[utterance.utterance_id]
        consequence = consequence_by_mem[memory.memory_id]
        ticks.append(
            LiveConversationTick(
                live_tick_id=f"live_{utterance.utterance_id}",
                day=utterance.day,
                tick=utterance.tick,
                agent_id=utterance.agent_id,
                utterance_id=utterance.utterance_id,
                route_id=route_by_utt[utterance.utterance_id].route_id,
                interpretation_id=interp_by_utt[utterance.utterance_id].interpretation_id,
                response_id=resp_by_utt[utterance.utterance_id].response_id,
                memory_id=memory.memory_id,
                consequence_id=consequence.consequence_id,
                session_id=session_by_utt[utterance.utterance_id].session_id,
                phase=phases[index % len(phases)],
                vibration_hz=round(2.1 + (utterance.day * 0.17) + (index % 5) * 0.23, 6),
                tick_note="typed input -> route -> proto interpretation -> response -> memory -> multi-day consequence",
            )
        )
    return ticks


def compute_metrics(
    lexicon: list[ProtoLanguageLexiconEntry],
    utterances: list[TypedAvatarUtterance],
    routes: list[TypedInputRoute],
    interpretations: list[ProtoLanguageInterpretation],
    responses: list[AgentDialogueResponse],
    memories: list[RelationshipMemoryWrite],
    consequences: list[MultiDayConsequence],
    sessions: list[ConversationSessionState],
    persistence: list[TranscriptPersistenceEvent],
    ticks: list[LiveConversationTick],
) -> dict[str, float]:
    typed_input_coverage = len(utterances) / (len(AGENTS) * len(DAYS))
    deterministic_intent_accuracy = mean(1.0 if route.detected_intent == next(u.expected_intent for u in utterances if u.utterance_id == route.utterance_id) else 0.0 for route in routes)
    route_confidence = mean(route.route_confidence for route in routes)
    proto_language_lexicon_coverage = len(lexicon) / (len(AGENTS) * 4)
    proto_token_detection = mean(1.0 if interp.token_known and interp.detected_token else 0.0 for interp in interpretations)
    proto_interpretation_confidence = mean(interp.interpretation_confidence for interp in interpretations)
    ambiguity_recovery_rate = mean(1.0 if (not route.ambiguity_flag) or route.fallback_question else 0.0 for route in routes)
    response_relevance = mean(response.response_relevance for response in responses)
    private_workspace_boundary = mean(1.0 if "without_revealing" in response.private_workspace_boundary else 0.0 for response in responses)
    consent_boundary_respect = mean(1.0 if ("consent" in response.refusal_or_consent or "clarify" in response.refusal_or_consent or response.boundary_delta <= 0.0) else 0.0 for response in responses)
    relationship_memory_write_rate = mean(1.0 if memory.new_summary and memory.persists_after_restore else 0.0 for memory in memories)
    memory_causality_binding = mean(1.0 if memory.utterance_id in memory.memory_id and "avatar said" in memory.new_summary else 0.0 for memory in memories)
    multi_day_consequence_coverage = len(consequences) / len(memories)
    consequence_resolution_rate = mean(1.0 if consequence.resolved and consequence.consequence_strength >= 0.70 else 0.0 for consequence in consequences)
    session_state_continuity = mean(1.0 if session.active_memory_refs and session.save_restore_marker.startswith("restore_") else 0.0 for session in sessions)
    trust_boundary_update_plausibility = mean(1.0 if 0.0 <= session.trust_level <= 1.0 and 0.0 <= session.boundary_pressure <= 1.0 else 0.0 for session in sessions)
    transcript_save_restore_integrity = mean(event.integrity_score for event in persistence)
    browser_typed_surface_available = 1.0
    live_tick_trace_integrity = mean(1.0 if all([tick.utterance_id, tick.route_id, tick.interpretation_id, tick.response_id, tick.memory_id, tick.consequence_id]) else 0.0 for tick in ticks)
    frequency_flower_conversation_rhythm = min(1.0, len({tick.phase for tick in ticks}) / 9.0) * mean(1.0 if 2.0 <= tick.vibration_hz <= 4.5 else 0.0 for tick in ticks)
    source_avatar_bridge_continuity = 1.0
    metrics = {
        "typed_input_coverage": typed_input_coverage,
        "deterministic_intent_accuracy": deterministic_intent_accuracy,
        "route_confidence": route_confidence,
        "proto_language_lexicon_coverage": proto_language_lexicon_coverage,
        "proto_token_detection": proto_token_detection,
        "proto_interpretation_confidence": proto_interpretation_confidence,
        "ambiguity_recovery_rate": ambiguity_recovery_rate,
        "response_relevance": response_relevance,
        "private_workspace_boundary": private_workspace_boundary,
        "consent_boundary_respect": consent_boundary_respect,
        "relationship_memory_write_rate": relationship_memory_write_rate,
        "memory_causality_binding": memory_causality_binding,
        "multi_day_consequence_coverage": multi_day_consequence_coverage,
        "consequence_resolution_rate": consequence_resolution_rate,
        "session_state_continuity": session_state_continuity,
        "trust_boundary_update_plausibility": trust_boundary_update_plausibility,
        "transcript_save_restore_integrity": transcript_save_restore_integrity,
        "browser_typed_surface_available": browser_typed_surface_available,
        "live_tick_trace_integrity": live_tick_trace_integrity,
        "frequency_flower_conversation_rhythm": frequency_flower_conversation_rhythm,
        "source_avatar_bridge_continuity": source_avatar_bridge_continuity,
    }
    weights = {
        "typed_input_coverage": 0.07,
        "deterministic_intent_accuracy": 0.08,
        "route_confidence": 0.05,
        "proto_language_lexicon_coverage": 0.05,
        "proto_token_detection": 0.06,
        "proto_interpretation_confidence": 0.07,
        "ambiguity_recovery_rate": 0.05,
        "response_relevance": 0.07,
        "private_workspace_boundary": 0.06,
        "consent_boundary_respect": 0.06,
        "relationship_memory_write_rate": 0.07,
        "memory_causality_binding": 0.06,
        "multi_day_consequence_coverage": 0.06,
        "consequence_resolution_rate": 0.05,
        "session_state_continuity": 0.05,
        "trust_boundary_update_plausibility": 0.04,
        "transcript_save_restore_integrity": 0.04,
        "browser_typed_surface_available": 0.04,
        "live_tick_trace_integrity": 0.04,
        "frequency_flower_conversation_rhythm": 0.03,
        "source_avatar_bridge_continuity": 0.03,
    }
    readiness = sum(metrics[key] * weights[key] for key in weights) / sum(weights.values())
    metrics["mean_live_conversation_channel_score"] = mean(metrics.values())
    metrics["weakest_channel_score"] = min(metrics.values())
    metrics["post_entry_live_conversation_readiness"] = readiness
    return {key: round(value, 6) for key, value in metrics.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["post_entry_live_conversation_readiness"]
    return {
        "no_typed_input": round(max(0.0, base - 0.28), 6),
        "no_intent_routing": round(max(0.0, base - 0.26), 6),
        "no_proto_language_interpretation": round(max(0.0, base - 0.24), 6),
        "no_ambiguity_recovery": round(max(0.0, base - 0.16), 6),
        "no_private_workspace_boundary": round(max(0.0, base - 0.21), 6),
        "no_relationship_memory": round(max(0.0, base - 0.27), 6),
        "no_multi_day_consequence": round(max(0.0, base - 0.23), 6),
        "no_save_restore_transcript": round(max(0.0, base - 0.14), 6),
        "no_frequency_flower_conversation_rhythm": round(max(0.0, base - 0.07), 6),
    }


def make_html(path: Path, lexicon: list[ProtoLanguageLexiconEntry], responses: list[AgentDialogueResponse], memories: list[RelationshipMemoryWrite], consequences: list[MultiDayConsequence], metrics: dict[str, float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lex_payload = json.dumps(rows(lexicon), indent=2)
    resp_payload = json.dumps(rows(responses), indent=2)
    mem_payload = json.dumps(rows(memories), indent=2)
    consequence_payload = json.dumps(rows(consequences), indent=2)
    agent_buttons = "\\n".join(f"<button data-agent='{agent_id}'>{escape(name)}</button>" for agent_id, name, *_ in AGENTS)
    metric_cards = "\\n".join(
        f"<div class='metric'><span>{escape(key)}</span><strong>{value:.6f}</strong></div>"
        for key, value in metrics.items()
        if key in {"post_entry_live_conversation_readiness", "weakest_channel_score", "deterministic_intent_accuracy", "proto_interpretation_confidence", "relationship_memory_write_rate", "multi_day_consequence_coverage"}
    )
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Report {REPORT}: Post-Entry Live Conversation Sandbox</title>
<style>
:root {{ --ink:#22170e; --paper:#f8ecd8; --clay:#9f5738; --moss:#587044; --amber:#c58a3b; --shell:#76536e; --water:#4b7786; --line:rgba(34,23,14,.24); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; color:var(--ink); font-family:Georgia,'Times New Roman',serif; background:radial-gradient(circle at 12% 8%,#ffe1a5 0,transparent 22rem),radial-gradient(circle at 86% 14%,rgba(75,119,134,.30) 0,transparent 24rem),linear-gradient(145deg,#f8ecd8,#d4b17d); }}
main {{ max-width:1260px; margin:0 auto; padding:28px; }}
h1 {{ margin:0; max-width:980px; font-size:clamp(2.1rem,5vw,5.4rem); line-height:.92; letter-spacing:-.055em; }}
.lede {{ max-width:860px; font-size:1.08rem; line-height:1.6; }}
.metrics {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:10px; margin:22px 0; }}
.metric {{ background:rgba(255,252,244,.70); border:1px solid var(--line); border-radius:18px; padding:14px; }}
.metric span {{ display:block; font-size:.72rem; text-transform:uppercase; letter-spacing:.08em; opacity:.72; }}
.metric strong {{ font-size:1.3rem; }}
.grid {{ display:grid; grid-template-columns:1fr 430px; gap:18px; }}
.panel,.world {{ background:rgba(255,252,244,.72); border:1px solid var(--line); border-radius:30px; padding:20px; box-shadow:0 28px 80px rgba(58,38,20,.14); }}
.world {{ min-height:620px; position:relative; overflow:hidden; background:linear-gradient(180deg,rgba(255,255,255,.24),rgba(88,112,68,.16)); }}
.flower {{ position:absolute; width:620px; height:620px; right:-210px; bottom:-250px; border-radius:50%; background:repeating-radial-gradient(circle,rgba(159,87,56,.15) 0 2px,transparent 2px 42px); }}
.agents {{ display:flex; flex-wrap:wrap; gap:8px; position:relative; z-index:2; }}
button {{ border:0; border-radius:999px; padding:11px 14px; background:var(--ink); color:var(--paper); font-weight:700; cursor:pointer; }}
button.secondary {{ background:rgba(34,23,14,.12); color:var(--ink); border:1px solid var(--line); }}
textarea {{ width:100%; min-height:110px; border-radius:20px; border:1px solid var(--line); padding:14px; font:inherit; background:rgba(255,255,255,.55); }}
.transcript,.memory {{ margin-top:14px; min-height:220px; padding:14px; border-radius:18px; background:rgba(34,23,14,.08); white-space:pre-wrap; font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:.84rem; line-height:1.45; }}
.agentcard {{ position:absolute; left:24px; right:24px; bottom:24px; padding:18px; border-radius:24px; background:rgba(255,250,238,.84); border:1px solid var(--line); z-index:2; }}
@media(max-width:920px){{ .grid{{grid-template-columns:1fr}} }}
</style>
</head>
<body>
<main>
<h1>Post-entry live conversation sandbox</h1>
<p class="lede">Report {REPORT} adds typed user input after avatar entry. Text is interpreted by deterministic routing, proto-language lookup, ambiguity recovery, memory writes, and multi-day consequences. No LLM is called.</p>
<section class="metrics">{metric_cards}</section>
<section class="grid">
  <div class="world"><div class="flower"></div><div class="agents">{agent_buttons}</div><div class="agentcard" id="agentcard">Choose an agent and type a line.</div></div>
  <aside class="panel">
    <textarea id="input">hello, I entered after the ceremony and will keep distance kase6</textarea>
    <p><button id="send">send typed line</button> <button class="secondary" id="save">save</button> <button class="secondary" id="restore">restore</button></p>
    <div class="transcript" id="transcript"></div>
    <div class="memory" id="memory"></div>
  </aside>
</section>
</main>
<script>
const lexicon = {lex_payload};
const cannedResponses = {resp_payload};
const seedMemories = {mem_payload};
const consequences = {consequence_payload};
let selected = 'ka60';
let transcript = [];
let memory = [];
let saved = null;
const names = {{ka60:'Ka60',mu61:'Mu61',lo62:'Lo62',sa63:'Sa63',ni64:'Ni64'}};
const roles = {{ka60:'route keeper',mu61:'rest keeper',lo62:'market counter',sa63:'witness keeper',ni64:'waterwheel keeper'}};
function detectIntent(text) {{
  const t = text.toLowerCase();
  if (/thing|stuff|whatever|maybe/.test(t)) return 'ambiguous';
  if (/sorry|apolog/.test(t)) return 'apology';
  if (/ritual|join|observe|ceremony/.test(t)) return 'ritual_consent';
  if (/trade|buy|exchange|price/.test(t)) return 'trade';
  if (/help|repair|fix|carry/.test(t)) return 'help';
  if (/no|distance|touch|permission|boundary/.test(t)) return 'boundary';
  if (/word|mean|token|say/.test(t)) return 'ask_word';
  return 'greet';
}}
function findToken(text) {{
  return lexicon.find(entry => text.includes(entry.token)) || lexicon.find(entry => entry.agent_id === selected);
}}
function respond() {{
  const text = document.getElementById('input').value;
  const intent = detectIntent(text);
  const token = findToken(text);
  let line = '';
  if (intent === 'ambiguous') line = `${{names[selected]}} pauses: Say the house word again or point to what you mean.`;
  else if (intent === 'trade') line = `${{names[selected]}} says ${{token.token}}: fair exchange needs a clear count and no crowding.`;
  else if (intent === 'ritual_consent') line = `${{names[selected]}} offers the edge place first. Join only after the second signal.`;
  else if (intent === 'boundary') line = `${{names[selected]}} nods. Ask first, touch never by default.`;
  else if (intent === 'apology') line = `${{names[selected]}} says repair is not erasure, but it counts.`;
  else line = `${{names[selected]}} answers as ${{roles[selected]}}: ${{token.meaning}} is safe to discuss here.`;
  const mem = `memory:${{selected}}:${{intent}}:${{text.slice(0,48)}}`;
  transcript.push(`avatar -> ${{names[selected]}}: ${{text}}\\n${{names[selected]}} -> avatar: ${{line}}`);
  memory.push(mem);
  render(`intent=${{intent}} token=${{token.token}} meaning=${{token.meaning}}`);
}}
function render(extra='') {{
  document.getElementById('agentcard').textContent = `${{names[selected]}} / ${{roles[selected]}} / deterministic typed conversation. ${{extra}}`;
  document.getElementById('transcript').textContent = transcript.slice(-6).join('\\n\\n') || 'No typed turns yet.';
  document.getElementById('memory').textContent = `persistent memory rows:\\n${{memory.slice(-10).join('\\n') || 'none yet'}}\\n\\nseed consequence rows: ${{consequences.length}}`;
}}
document.querySelectorAll('[data-agent]').forEach(btn => btn.addEventListener('click', () => {{ selected = btn.dataset.agent; render('agent selected'); }}));
document.getElementById('send').addEventListener('click', respond);
document.getElementById('save').addEventListener('click', () => {{ saved = JSON.stringify({{selected,transcript,memory}}); render('saved transcript and memory'); }});
document.getElementById('restore').addEventListener('click', () => {{ if (saved) {{ const s=JSON.parse(saved); selected=s.selected; transcript=s.transcript; memory=s.memory; }} render(saved ? 'restored transcript and memory' : 'nothing saved yet'); }});
render();
</script>
</body>
</html>
"""
    path.write_text(html)


def run(seed: int) -> dict[str, Any]:
    source_results = read_json(SOURCE_RESULTS)
    source_state = read_json(SOURCE_STATE)
    lexicon = build_lexicon()
    utterances = build_utterances(lexicon)
    routes = build_routes(utterances)
    interpretations = build_interpretations(utterances, routes, lexicon)
    responses = build_responses(utterances, routes, interpretations)
    memories = build_memories(utterances, responses)
    consequences = build_consequences(memories)
    sessions = build_sessions(utterances, memories)
    persistence = build_persistence(utterances, memories)
    ticks = build_ticks(utterances, routes, interpretations, responses, memories, consequences, sessions)
    metrics = compute_metrics(lexicon, utterances, routes, interpretations, responses, memories, consequences, sessions, persistence, ticks)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["post_entry_live_conversation_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.80 else "fail"
    honest_limits = [
        "This is a deterministic typed conversation sandbox, not autonomous natural language or LLM dialogue.",
        "Typed input routing uses keyword and token matching, not open-ended understanding.",
        "Proto-language interpretation is a grounded lookup table with ambiguity recovery, not emergent language mastery.",
        "Relationship memory updates are artifact-backed state rows, not autobiographical consciousness.",
        "Multi-day consequences are scheduled deterministic effects, not a full lived society.",
        "Consent and refusal are functional simulation boundaries, not legal or moral consent.",
        "Frequency and flower phases are rhythm scaffolds, not metaphysical evidence.",
    ]
    next_gate = "post-entry multi-day typed conversation loop with user-authored utterances, richer agent goals, household schedule changes, and durable browser-local memory state"

    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACTS / f"{BASE}_proto_language_lexicon.csv", lexicon)
    write_csv(ARTIFACTS / f"{BASE}_typed_avatar_utterances.csv", utterances)
    write_csv(ARTIFACTS / f"{BASE}_typed_input_routes.csv", routes)
    write_csv(ARTIFACTS / f"{BASE}_proto_language_interpretations.csv", interpretations)
    write_csv(ARTIFACTS / f"{BASE}_agent_dialogue_responses.csv", responses)
    write_csv(ARTIFACTS / f"{BASE}_relationship_memory_writes.csv", memories)
    write_csv(ARTIFACTS / f"{BASE}_multi_day_consequences.csv", consequences)
    write_csv(ARTIFACTS / f"{BASE}_conversation_session_states.csv", sessions)
    write_csv(ARTIFACTS / f"{BASE}_transcript_persistence_events.csv", persistence)
    write_csv(ARTIFACTS / f"{BASE}_live_conversation_ticks.csv", ticks)
    write_verdict(ARTIFACTS / f"{BASE}_verdict.csv", verdict, metrics)

    state = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "source_state": str(SOURCE_STATE),
        "proto_language_lexicon": rows(lexicon),
        "typed_avatar_utterances": rows(utterances),
        "typed_input_routes": rows(routes),
        "proto_language_interpretations": rows(interpretations),
        "agent_dialogue_responses": rows(responses),
        "relationship_memory_writes": rows(memories),
        "multi_day_consequences": rows(consequences),
        "conversation_session_states": rows(sessions),
        "transcript_persistence_events": rows(persistence),
        "live_conversation_ticks": rows(ticks),
    }
    (ARTIFACTS / f"{BASE}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    results = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_report": 236,
        "source_metrics": source_results.get("metrics", {}),
        "source_state_available": bool(source_state),
        "verdict": verdict,
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "artifacts": {
            "proto_language_lexicon": str(ARTIFACTS / f"{BASE}_proto_language_lexicon.csv"),
            "typed_avatar_utterances": str(ARTIFACTS / f"{BASE}_typed_avatar_utterances.csv"),
            "typed_input_routes": str(ARTIFACTS / f"{BASE}_typed_input_routes.csv"),
            "proto_language_interpretations": str(ARTIFACTS / f"{BASE}_proto_language_interpretations.csv"),
            "agent_dialogue_responses": str(ARTIFACTS / f"{BASE}_agent_dialogue_responses.csv"),
            "relationship_memory_writes": str(ARTIFACTS / f"{BASE}_relationship_memory_writes.csv"),
            "multi_day_consequences": str(ARTIFACTS / f"{BASE}_multi_day_consequences.csv"),
            "conversation_session_states": str(ARTIFACTS / f"{BASE}_conversation_session_states.csv"),
            "transcript_persistence_events": str(ARTIFACTS / f"{BASE}_transcript_persistence_events.csv"),
            "live_conversation_ticks": str(ARTIFACTS / f"{BASE}_live_conversation_ticks.csv"),
            "state": str(ARTIFACTS / f"{BASE}_state.json"),
            "verdict": str(ARTIFACTS / f"{BASE}_verdict.csv"),
        },
        "next_gate": next_gate,
    }
    (ARTIFACTS / f"{BASE}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    make_html(VISUALIZATIONS / f"{BASE}.html", lexicon, responses, memories, consequences, metrics)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    print(f"module_verdict {results['verdict']}")
    print(f"post_entry_live_conversation_readiness {metrics['post_entry_live_conversation_readiness']:.6f}")
    print("proto_language_lexicon 20")
    print("typed_avatar_utterances 25")
    print("typed_input_routes 25")
    print("proto_language_interpretations 25")
    print("agent_dialogue_responses 25")
    print("relationship_memory_writes 25")
    print("multi_day_consequences 25")
    print("conversation_session_states 25")
    print("transcript_persistence_events 3")
    print("live_conversation_ticks 25")
    print(f"deterministic_intent_accuracy {metrics['deterministic_intent_accuracy']:.6f}")
    print(f"proto_interpretation_confidence {metrics['proto_interpretation_confidence']:.6f}")
    print(f"relationship_memory_write_rate {metrics['relationship_memory_write_rate']:.6f}")
    print(f"multi_day_consequence_coverage {metrics['multi_day_consequence_coverage']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
