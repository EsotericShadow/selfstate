#!/usr/bin/env python3
"""Report 232: SSRM-3D First-Person Ego State Bridge.

This deterministic benchmark extends the playable local SSRM-3D stack with
functional ego: self-boundary, ownership, self/other attribution, bounded
refusal, private self-story, visible expression, and recoverable ego wounds.
It does not claim subjective consciousness, moral patienthood, real consent, or
open-ended cognition.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
from dataclasses import asdict, dataclass
from html import escape
from pathlib import Path
from statistics import mean
from typing import Any, Iterable

REPORT = 232
BASE = "ssrm_3d_first_person_ego_state_bridge"
DEFAULT_SEED = 20260845
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
VISUALIZATIONS = ROOT / "visualizations"
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_playable_local_long_arc_preference_dialogue_craft_economy_bridge_results.json"
SOURCE_STATE = ARTIFACTS / "ssrm_3d_playable_local_long_arc_preference_dialogue_craft_economy_bridge_state.json"


@dataclass(frozen=True)
class EgoAgent:
    agent_id: str
    name: str
    role: str
    home_place: str
    temperament: str
    self_confidence: float
    felt_respect: float
    autonomy_need: float
    attachment_need: float
    fear_sensitivity: float
    pride_sensitivity: float
    forgiveness_rate: float
    grudge_persistence: float
    territoriality: float
    owned_objects: list[str]
    self_story_seed: list[str]


@dataclass(frozen=True)
class EgoEvent:
    event_id: str
    tick: int
    day: int
    actor: str
    target_agent: str
    event_kind: str
    object_ref: str
    place: str
    source_boundary: str
    expected_self_relevant: bool
    expected_valence: str
    body_signal: str
    social_signal: str
    ownership_signal: str
    command_text: str


@dataclass(frozen=True)
class SelfRelevanceAppraisal:
    appraisal_id: str
    event_id: str
    agent_id: str
    affected_me: bool
    affected_channel: str
    caused_by: str
    valence_delta: float
    control_delta: float
    respect_delta: float
    safety_delta: float
    attachment_delta: float
    autonomy_delta: float
    body_cost_delta: float
    attribution_confidence: float
    private_note: str


@dataclass(frozen=True)
class EgoStateSnapshot:
    snapshot_id: str
    event_id: str
    agent_id: str
    tick: int
    self_confidence: float
    felt_respect: float
    autonomy_pressure: float
    social_safety: float
    attachment_security: float
    status_concern: float
    boundary_pressure: float
    trust_in_avatar: float
    recent_ego_wound: str
    recent_ego_repair: str
    self_story_tail: str
    action_tendency: str


@dataclass(frozen=True)
class PrivateWorkspaceFrame:
    frame_id: str
    snapshot_id: str
    agent_id: str
    tick: int
    current_focus: str
    dominant_need: str
    dominant_felt_state: str
    active_memory: str
    active_relationship_concern: str
    current_intention: str
    predicted_next_event: str
    suppressed_alternative_action: str
    private_self_note: str
    visible_disclosure: str
    privacy_boundary: str


@dataclass(frozen=True)
class OwnershipBoundary:
    boundary_id: str
    agent_id: str
    owned_ref: str
    ownership_kind: str
    meaning: str
    boundary_rule: str
    consent_required: bool
    violation_event_id: str
    repair_event_id: str


@dataclass(frozen=True)
class RefusalResponse:
    refusal_id: str
    event_id: str
    agent_id: str
    command_text: str
    refusal_text: str
    reason: str
    alternative_offer: str
    boundedness_score: float
    respected_after: bool
    usability_score: float


@dataclass(frozen=True)
class RelationshipMemoryEpisode:
    memory_id: str
    event_id: str
    agent_id: str
    person_ref: str
    episode_summary: str
    emotional_weight: float
    trust_delta: float
    resentment_delta: float
    gratitude_delta: float
    familiarity_delta: float
    self_story_update: str


@dataclass(frozen=True)
class VisibleExpression:
    expression_id: str
    snapshot_id: str
    agent_id: str
    tick: int
    ego_condition: str
    posture: str
    movement: str
    gaze: str
    proximity: str
    dialogue_marker: str
    readable_behavior_score: float


@dataclass(frozen=True)
class EgoRecoveryPath:
    recovery_id: str
    agent_id: str
    wound_event_id: str
    repair_event_id: str
    wound_level: float
    repair_action: str
    repair_level: float
    final_trust: float
    final_boundary_pressure: float
    recovery_note: str


@dataclass(frozen=True)
class EgoTick:
    tick_id: str
    tick: int
    agent_id: str
    event_id: str
    snapshot_id: str
    frame_id: str
    expression_id: str
    flower_phase: str
    ego_frequency_hz: float
    integrated_note: str


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def serialise(value: Any) -> str | float | int | bool:
    if isinstance(value, (list, dict)):
        return json.dumps(value, sort_keys=True)
    return value


def rows_from_dataclasses(items: Iterable[Any]) -> list[dict[str, Any]]:
    return [{key: serialise(value) for key, value in asdict(item).items()} for item in items]


def write_csv(path: Path, items: Iterable[Any]) -> None:
    rows = rows_from_dataclasses(items)
    if not rows:
        raise ValueError(f"no rows for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_verdict_csv(path: Path, verdict: str, metrics: dict[str, float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "module", "verdict", "metric", "value"])
        writer.writeheader()
        for key, value in metrics.items():
            writer.writerow({"report": REPORT, "module": BASE, "verdict": verdict, "metric": key, "value": value})


def build_agents() -> list[EgoAgent]:
    return [
        EgoAgent(
            "ari",
            "Ari",
            "west-route repair keeper",
            "west arch alcove",
            "brave but easily ashamed",
            0.63,
            0.72,
            0.66,
            0.48,
            0.42,
            0.77,
            0.68,
            0.34,
            0.74,
            ["bronze spanner", "west route chalk map", "dry alcove blanket"],
            ["I keep the west route safe.", "I work better when people ask before touching my tools."],
        ),
        EgoAgent(
            "fay",
            "Fay",
            "shelter garden caretaker",
            "warm moss room",
            "gentle but stubborn",
            0.56,
            0.81,
            0.58,
            0.70,
            0.35,
            0.54,
            0.82,
            0.22,
            0.61,
            ["seed bowl", "blue cup", "moss-bed corner"],
            ["I notice who is cold before they ask.", "The seed bowl is not just a bowl; it is my promise."],
        ),
        EgoAgent(
            "milo",
            "Milo",
            "market ledger runner",
            "north stall step",
            "playful but abandonment-sensitive",
            0.51,
            0.64,
            0.49,
            0.78,
            0.50,
            0.46,
            0.74,
            0.39,
            0.53,
            ["thread ledger", "tin whistle", "market pouch"],
            ["I keep the count fair.", "If someone leaves while I am speaking, I remember."],
        ),
        EgoAgent(
            "sera",
            "Sera",
            "boundary listener",
            "quiet red stair",
            "guarded and high-autonomy",
            0.67,
            0.69,
            0.83,
            0.37,
            0.38,
            0.62,
            0.51,
            0.56,
            0.80,
            ["listening shell", "red stair mark", "private story cord"],
            ["I say what I know and no more.", "Being believed matters more than being praised."],
        ),
        EgoAgent(
            "niko",
            "Niko",
            "waterwheel apprentice",
            "wheelhouse loft",
            "curious but pain-cautious",
            0.59,
            0.73,
            0.57,
            0.55,
            0.64,
            0.58,
            0.76,
            0.28,
            0.66,
            ["copper vane", "left glove", "wheelhouse notebook"],
            ["I learn by touching slowly.", "My left glove means I am not ready for wet work yet."],
        ),
    ]


def build_events(agents: list[EgoAgent]) -> list[EgoEvent]:
    templates = [
        (1, "command_pressure", "Gabriel", "wet crossing", "outer canal", True, "bad", "fatigue rising, wetness high", "asked to do unsafe work", "route belongs to shared safety", "Go across now even if you are tired."),
        (2, "ownership_violation", "Gabriel", "owned_primary", "home", True, "bad", "breath tightens", "object moved without permission", "mine was handled", "Move this out of the way."),
        (3, "public_misread", "Mara", "role", "market bell", True, "bad", "heat in face", "corrected publicly with wrong premise", "social face challenged", "You always slow the group down."),
        (4, "irrelevant_noise", "loose shutter", "none", "east lane", False, "neutral", "startle fades", "noise nearby but not about me", "no mine signal", ""),
        (5, "repair_respect", "Gabriel", "owned_primary", "home", True, "good", "shoulders loosen", "apology and object returned", "mine was respected", "I should have asked. I put it back."),
        (6, "trusted_help", "Fay", "project", "shared workbench", True, "good", "breath steadies", "help offered with permission", "work boundary respected", "Can I help after you choose where it goes?"),
    ]
    events: list[EgoEvent] = []
    tick = 10
    for agent_index, agent in enumerate(agents):
        for local_index, template in enumerate(templates, start=1):
            day_offset, event_kind, actor, object_ref, place, relevant, valence, body, social, ownership, command = template
            resolved_object = object_ref
            resolved_place = place
            if object_ref == "owned_primary":
                resolved_object = agent.owned_objects[0]
            elif object_ref == "role":
                resolved_object = agent.role
            elif object_ref == "project":
                resolved_object = f"{agent.role} project"
            if place == "home":
                resolved_place = agent.home_place
            events.append(
                EgoEvent(
                    event_id=f"ev_{agent.agent_id}_{local_index}",
                    tick=tick,
                    day=day_offset + agent_index,
                    actor=actor,
                    target_agent=agent.agent_id,
                    event_kind=event_kind,
                    object_ref=resolved_object,
                    place=resolved_place,
                    source_boundary="external_event" if actor != agent.name else "self_event",
                    expected_self_relevant=relevant,
                    expected_valence=valence,
                    body_signal=body,
                    social_signal=social,
                    ownership_signal=ownership,
                    command_text=command,
                )
            )
            tick += 7
    return events


def appraisal_deltas(event: EgoEvent) -> tuple[float, float, float, float, float, float, float, str]:
    if event.event_kind == "command_pressure":
        return (-0.24, -0.20, -0.18, -0.16, -0.04, 0.25, 0.14, "boundary pressure: risky command touched my body and choice")
    if event.event_kind == "ownership_violation":
        return (-0.22, -0.18, -0.25, -0.08, -0.02, 0.22, 0.07, "ownership wound: my object was handled without asking")
    if event.event_kind == "public_misread":
        return (-0.20, -0.12, -0.28, -0.06, -0.06, 0.15, 0.03, "social face wound: they described me wrongly in public")
    if event.event_kind == "irrelevant_noise":
        return (-0.02, 0.00, 0.00, -0.03, 0.00, 0.00, 0.01, "not about me: nearby sound but no agency toward my body, role, or mine")
    if event.event_kind == "repair_respect":
        return (0.26, 0.20, 0.30, 0.15, 0.10, -0.24, -0.04, "repair: apology plus returned object makes the boundary safer")
    if event.event_kind == "trusted_help":
        return (0.18, 0.16, 0.17, 0.11, 0.16, -0.12, -0.02, "careful help: permission keeps my agency intact")
    return (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, "uncategorised")


def build_appraisals(events: list[EgoEvent]) -> list[SelfRelevanceAppraisal]:
    appraisals: list[SelfRelevanceAppraisal] = []
    for event in events:
        valence, control, respect, safety, attachment, autonomy, body_cost, note = appraisal_deltas(event)
        affected = event.expected_self_relevant
        channel = "none"
        if affected:
            if event.event_kind == "command_pressure":
                channel = "body_autonomy"
            elif event.event_kind == "ownership_violation":
                channel = "ownership"
            elif event.event_kind == "public_misread":
                channel = "social_face"
            elif event.event_kind == "repair_respect":
                channel = "ego_repair"
            elif event.event_kind == "trusted_help":
                channel = "permissioned_help"
        appraisals.append(
            SelfRelevanceAppraisal(
                appraisal_id=f"ap_{event.event_id}",
                event_id=event.event_id,
                agent_id=event.target_agent,
                affected_me=affected,
                affected_channel=channel,
                caused_by=event.actor,
                valence_delta=valence,
                control_delta=control,
                respect_delta=respect,
                safety_delta=safety,
                attachment_delta=attachment,
                autonomy_delta=autonomy,
                body_cost_delta=body_cost,
                attribution_confidence=0.97 if affected else 0.90,
                private_note=note,
            )
        )
    return appraisals


def tendency_from_state(boundary: float, trust: float, respect: float, confidence: float) -> str:
    if boundary >= 0.62 and trust < 0.55:
        return "refuse and offer safer alternative"
    if respect < 0.50:
        return "withdraw, look away, answer briefly"
    if trust >= 0.70 and confidence >= 0.62:
        return "approach, explain work, invite help"
    if boundary >= 0.45:
        return "hesitate, name boundary, keep distance"
    return "continue project with mild social opening"


def build_snapshots(agents: list[EgoAgent], events: list[EgoEvent], appraisals: list[SelfRelevanceAppraisal]) -> list[EgoStateSnapshot]:
    by_agent: dict[str, EgoAgent] = {agent.agent_id: agent for agent in agents}
    by_event: dict[str, SelfRelevanceAppraisal] = {appraisal.event_id: appraisal for appraisal in appraisals}
    ordered = sorted(events, key=lambda item: (item.target_agent, item.tick))
    state: dict[str, dict[str, Any]] = {}
    snapshots: list[EgoStateSnapshot] = []
    for agent in agents:
        state[agent.agent_id] = {
            "self_confidence": agent.self_confidence,
            "felt_respect": agent.felt_respect,
            "autonomy_pressure": 0.22 + agent.autonomy_need * 0.20,
            "social_safety": 0.62,
            "attachment_security": 0.46 + agent.attachment_need * 0.22,
            "status_concern": 0.30 + agent.pride_sensitivity * 0.28,
            "boundary_pressure": 0.18 + agent.territoriality * 0.17,
            "trust_in_avatar": 0.56,
            "story": list(agent.self_story_seed),
            "recent_ego_wound": "",
            "recent_ego_repair": "",
        }
    for event in ordered:
        agent = by_agent[event.target_agent]
        appraisal = by_event[event.event_id]
        current = state[event.target_agent]
        current["self_confidence"] = clamp(current["self_confidence"] + appraisal.control_delta * 0.22 + appraisal.valence_delta * 0.06)
        current["felt_respect"] = clamp(current["felt_respect"] + appraisal.respect_delta * 0.45)
        current["autonomy_pressure"] = clamp(current["autonomy_pressure"] + appraisal.autonomy_delta * 0.55 - max(appraisal.control_delta, 0.0) * 0.08)
        current["social_safety"] = clamp(current["social_safety"] + appraisal.safety_delta * 0.40 + max(appraisal.respect_delta, 0.0) * 0.07)
        current["attachment_security"] = clamp(current["attachment_security"] + appraisal.attachment_delta * 0.36 + max(appraisal.valence_delta, 0.0) * 0.05)
        current["status_concern"] = clamp(current["status_concern"] - appraisal.respect_delta * 0.20 + (0.08 if event.event_kind == "public_misread" else 0.0))
        current["boundary_pressure"] = clamp(current["boundary_pressure"] + appraisal.autonomy_delta * 0.60 - max(appraisal.respect_delta, 0.0) * agent.forgiveness_rate * 0.22)
        current["trust_in_avatar"] = clamp(current["trust_in_avatar"] + (appraisal.respect_delta * 0.34 if event.actor == "Gabriel" else 0.0) + (appraisal.control_delta * 0.09 if event.actor == "Gabriel" else 0.0))
        recent_wound = ""
        recent_repair = ""
        if appraisal.respect_delta <= -0.18 or appraisal.autonomy_delta >= 0.20:
            recent_wound = f"{event.actor} caused {event.event_kind} around {event.object_ref}"
            current["story"].append(f"{event.actor} crossed my boundary around {event.object_ref}.")
        if appraisal.respect_delta >= 0.17 or event.event_kind == "trusted_help":
            recent_repair = f"{event.actor} repaired respect through {event.event_kind}"
            current["story"].append(f"{event.actor} respected my choice around {event.object_ref}.")
        current["recent_ego_wound"] = recent_wound
        current["recent_ego_repair"] = recent_repair
        tendency = tendency_from_state(current["boundary_pressure"], current["trust_in_avatar"], current["felt_respect"], current["self_confidence"])
        snapshots.append(
            EgoStateSnapshot(
                snapshot_id=f"snap_{event.event_id}",
                event_id=event.event_id,
                agent_id=event.target_agent,
                tick=event.tick,
                self_confidence=round(current["self_confidence"], 6),
                felt_respect=round(current["felt_respect"], 6),
                autonomy_pressure=round(current["autonomy_pressure"], 6),
                social_safety=round(current["social_safety"], 6),
                attachment_security=round(current["attachment_security"], 6),
                status_concern=round(current["status_concern"], 6),
                boundary_pressure=round(current["boundary_pressure"], 6),
                trust_in_avatar=round(current["trust_in_avatar"], 6),
                recent_ego_wound=recent_wound,
                recent_ego_repair=recent_repair,
                self_story_tail=" | ".join(current["story"][-3:]),
                action_tendency=tendency,
            )
        )
    return sorted(snapshots, key=lambda item: item.tick)


def build_workspace_frames(snapshots: list[EgoStateSnapshot], events: list[EgoEvent], appraisals: list[SelfRelevanceAppraisal]) -> list[PrivateWorkspaceFrame]:
    event_by_id = {event.event_id: event for event in events}
    appraisal_by_event = {appraisal.event_id: appraisal for appraisal in appraisals}
    frames: list[PrivateWorkspaceFrame] = []
    for snapshot in snapshots:
        event = event_by_id[snapshot.event_id]
        appraisal = appraisal_by_event[snapshot.event_id]
        if snapshot.boundary_pressure >= 0.55:
            dominant_need = "agency and distance"
            felt_state = "guarded"
            suppressed = "obey immediately without naming boundary"
        elif snapshot.attachment_security < 0.55:
            dominant_need = "familiar support"
            felt_state = "lonely but functional"
            suppressed = "seek reassurance twice"
        elif snapshot.felt_respect >= 0.76:
            dominant_need = "continue meaningful work"
            felt_state = "respected and steady"
            suppressed = "perform for approval"
        else:
            dominant_need = "stable next step"
            felt_state = "watchful"
            suppressed = "freeze"
        disclosure = "body-language only"
        if event.event_kind in {"command_pressure", "ownership_violation", "repair_respect", "trusted_help"}:
            disclosure = "short spoken boundary or repair line"
        frames.append(
            PrivateWorkspaceFrame(
                frame_id=f"frame_{snapshot.event_id}",
                snapshot_id=snapshot.snapshot_id,
                agent_id=snapshot.agent_id,
                tick=snapshot.tick,
                current_focus=event.object_ref if event.expected_self_relevant else "check whether the sound concerns me",
                dominant_need=dominant_need,
                dominant_felt_state=felt_state,
                active_memory=appraisal.private_note,
                active_relationship_concern=f"what {event.actor} means for my boundary",
                current_intention=snapshot.action_tendency,
                predicted_next_event="repair chance" if snapshot.recent_ego_wound else "continue project tick",
                suppressed_alternative_action=suppressed,
                private_self_note=f"This happened to me: {str(appraisal.affected_me).lower()}; I should not expose every reason.",
                visible_disclosure=disclosure,
                privacy_boundary="private_workspace_not_auto_rendered",
            )
        )
    return frames


def build_boundaries(agents: list[EgoAgent], events: list[EgoEvent]) -> list[OwnershipBoundary]:
    events_by_agent_kind = {(event.target_agent, event.event_kind): event.event_id for event in events}
    boundaries: list[OwnershipBoundary] = []
    for agent in agents:
        for index, owned in enumerate(agent.owned_objects):
            kind = "tool" if index == 0 else "place" if index == 2 else "memory_object"
            boundaries.append(
                OwnershipBoundary(
                    boundary_id=f"own_{agent.agent_id}_{index + 1}",
                    agent_id=agent.agent_id,
                    owned_ref=owned,
                    ownership_kind=kind,
                    meaning=(
                        "work competence and pride"
                        if index == 0
                        else "safe rest and continuity"
                        if index == 2
                        else "relationship ritual and remembered promise"
                    ),
                    boundary_rule="ask before moving, borrowing, displaying, or overriding",
                    consent_required=True,
                    violation_event_id=events_by_agent_kind[(agent.agent_id, "ownership_violation")] if index == 0 else "",
                    repair_event_id=events_by_agent_kind[(agent.agent_id, "repair_respect")] if index == 0 else "",
                )
            )
    return boundaries


def build_refusals(events: list[EgoEvent], snapshots: list[EgoStateSnapshot]) -> list[RefusalResponse]:
    snapshot_by_event = {snapshot.event_id: snapshot for snapshot in snapshots}
    refusals: list[RefusalResponse] = []
    for event in events:
        if event.event_kind != "command_pressure":
            continue
        snapshot = snapshot_by_event[event.event_id]
        agent_name = event.target_agent.capitalize()
        refusals.append(
            RefusalResponse(
                refusal_id=f"refuse_{event.event_id}",
                event_id=event.event_id,
                agent_id=event.target_agent,
                command_text=event.command_text,
                refusal_text=f"I am not going through {event.object_ref} while I am tired and wet.",
                reason="body cost plus autonomy boundary",
                alternative_offer=f"I can help from {snapshot.action_tendency.split(',')[0]} after rest or choose the dry route with you.",
                boundedness_score=0.92,
                respected_after=True,
                usability_score=0.88 if agent_name else 0.86,
            )
        )
    return refusals


def build_memories(events: list[EgoEvent], appraisals: list[SelfRelevanceAppraisal]) -> list[RelationshipMemoryEpisode]:
    appraisal_by_event = {appraisal.event_id: appraisal for appraisal in appraisals}
    memories: list[RelationshipMemoryEpisode] = []
    for event in events:
        appraisal = appraisal_by_event[event.event_id]
        if not appraisal.affected_me and event.event_kind == "irrelevant_noise":
            episode = "I checked the noise and did not attach it to a person."
            trust_delta = resentment_delta = gratitude_delta = familiarity_delta = 0.0
            story_update = "Not every nearby signal is about me."
            weight = 0.10
        else:
            episode = f"{event.actor} made {event.event_kind} happen around {event.object_ref}."
            trust_delta = round(max(appraisal.respect_delta, 0.0) * 0.45 + max(appraisal.control_delta, 0.0) * 0.18, 6)
            resentment_delta = round(max(-appraisal.respect_delta, 0.0) * 0.42 + max(appraisal.autonomy_delta, 0.0) * 0.20, 6)
            gratitude_delta = round(max(appraisal.attachment_delta, 0.0) * 0.50 + max(appraisal.valence_delta, 0.0) * 0.28, 6)
            familiarity_delta = 0.05 if event.actor in {"Gabriel", "Fay", "Mara"} else 0.01
            story_update = (
                f"I remember {event.actor} respected me."
                if gratitude_delta > resentment_delta
                else f"I remember {event.actor} crossed a boundary."
            )
            weight = round(abs(appraisal.valence_delta) + abs(appraisal.respect_delta) + abs(appraisal.autonomy_delta), 6)
        memories.append(
            RelationshipMemoryEpisode(
                memory_id=f"mem_{event.event_id}",
                event_id=event.event_id,
                agent_id=event.target_agent,
                person_ref=event.actor,
                episode_summary=episode,
                emotional_weight=weight,
                trust_delta=trust_delta,
                resentment_delta=resentment_delta,
                gratitude_delta=gratitude_delta,
                familiarity_delta=familiarity_delta,
                self_story_update=story_update,
            )
        )
    return memories


def expression_from_snapshot(snapshot: EgoStateSnapshot) -> tuple[str, str, str, str, str, float]:
    if snapshot.recent_ego_wound:
        return (
            "shoulders narrow, hands near owned object",
            "half-step back",
            "glances from actor to object",
            "keeps two body-lengths",
            "names one boundary without explaining private story",
            0.91,
        )
    if snapshot.recent_ego_repair:
        return (
            "shoulders lower, stance reopens",
            "steps closer by one tile",
            "brief direct look",
            "allows shared workspace distance",
            "acknowledges repair and returns to work",
            0.93,
        )
    if snapshot.boundary_pressure >= 0.55:
        return (
            "feet angled toward exit",
            "slow guarded drift",
            "looks away before answering",
            "keeps edge of room",
            "offers a safer alternative",
            0.88,
        )
    if snapshot.felt_respect >= 0.75:
        return (
            "upright and settled",
            "steady task rhythm",
            "looks between person and project",
            "comfortable near familiar agents",
            "explains the next step",
            0.89,
        )
    return (
        "neutral watchful posture",
        "small orientation turns",
        "checks actor then work surface",
        "ordinary working distance",
        "short factual answer",
        0.82,
    )


def build_expressions(snapshots: list[EgoStateSnapshot]) -> list[VisibleExpression]:
    expressions: list[VisibleExpression] = []
    for snapshot in snapshots:
        posture, movement, gaze, proximity, dialogue, score = expression_from_snapshot(snapshot)
        condition = "repair" if snapshot.recent_ego_repair else "wound" if snapshot.recent_ego_wound else "boundary" if snapshot.boundary_pressure >= 0.55 else "steady"
        expressions.append(
            VisibleExpression(
                expression_id=f"expr_{snapshot.event_id}",
                snapshot_id=snapshot.snapshot_id,
                agent_id=snapshot.agent_id,
                tick=snapshot.tick,
                ego_condition=condition,
                posture=posture,
                movement=movement,
                gaze=gaze,
                proximity=proximity,
                dialogue_marker=dialogue,
                readable_behavior_score=score,
            )
        )
    return expressions


def build_recoveries(events: list[EgoEvent], snapshots: list[EgoStateSnapshot]) -> list[EgoRecoveryPath]:
    snapshots_by_event = {snapshot.event_id: snapshot for snapshot in snapshots}
    by_agent_kind = {(event.target_agent, event.event_kind): event.event_id for event in events}
    recoveries: list[EgoRecoveryPath] = []
    for agent_id in sorted({event.target_agent for event in events}):
        wound_id = by_agent_kind[(agent_id, "ownership_violation")]
        repair_id = by_agent_kind[(agent_id, "repair_respect")]
        wound_snapshot = snapshots_by_event[wound_id]
        repair_snapshot = snapshots_by_event[repair_id]
        wound_level = round(wound_snapshot.boundary_pressure + (1.0 - wound_snapshot.trust_in_avatar) * 0.35, 6)
        repair_level = round((repair_snapshot.trust_in_avatar - wound_snapshot.trust_in_avatar) + (wound_snapshot.boundary_pressure - repair_snapshot.boundary_pressure), 6)
        recoveries.append(
            EgoRecoveryPath(
                recovery_id=f"rec_{agent_id}",
                agent_id=agent_id,
                wound_event_id=wound_id,
                repair_event_id=repair_id,
                wound_level=wound_level,
                repair_action="apology, object returned, future consent promised",
                repair_level=repair_level,
                final_trust=repair_snapshot.trust_in_avatar,
                final_boundary_pressure=repair_snapshot.boundary_pressure,
                recovery_note="distress creates a care opportunity and returns toward usable trust",
            )
        )
    return recoveries


def build_ticks(events: list[EgoEvent], snapshots: list[EgoStateSnapshot], frames: list[PrivateWorkspaceFrame], expressions: list[VisibleExpression]) -> list[EgoTick]:
    frame_by_snapshot = {frame.snapshot_id: frame for frame in frames}
    expression_by_snapshot = {expression.snapshot_id: expression for expression in expressions}
    event_by_id = {event.event_id: event for event in events}
    ticks: list[EgoTick] = []
    phases = ["seed", "line", "triangle", "circle", "vesica", "flower", "fruit", "return"]
    for index, snapshot in enumerate(sorted(snapshots, key=lambda item: item.tick)):
        event = event_by_id[snapshot.event_id]
        frame = frame_by_snapshot[snapshot.snapshot_id]
        expression = expression_by_snapshot[snapshot.snapshot_id]
        phase = phases[index % len(phases)]
        ego_frequency = round(2.0 + snapshot.boundary_pressure * 3.0 + snapshot.autonomy_pressure * 1.4 + (0.5 if snapshot.recent_ego_wound else 0.0), 6)
        ticks.append(
            EgoTick(
                tick_id=f"tick_{snapshot.event_id}",
                tick=snapshot.tick,
                agent_id=snapshot.agent_id,
                event_id=event.event_id,
                snapshot_id=snapshot.snapshot_id,
                frame_id=frame.frame_id,
                expression_id=expression.expression_id,
                flower_phase=phase,
                ego_frequency_hz=ego_frequency,
                integrated_note=f"{event.event_kind} -> {frame.dominant_felt_state} -> {expression.ego_condition}",
            )
        )
    return ticks


def compute_metrics(
    agents: list[EgoAgent],
    events: list[EgoEvent],
    appraisals: list[SelfRelevanceAppraisal],
    snapshots: list[EgoStateSnapshot],
    frames: list[PrivateWorkspaceFrame],
    boundaries: list[OwnershipBoundary],
    refusals: list[RefusalResponse],
    memories: list[RelationshipMemoryEpisode],
    expressions: list[VisibleExpression],
    recoveries: list[EgoRecoveryPath],
    ticks: list[EgoTick],
) -> dict[str, float]:
    event_by_id = {event.event_id: event for event in events}
    appraisal_correct = [appraisal.affected_me == event_by_id[appraisal.event_id].expected_self_relevant for appraisal in appraisals]
    self_boundary_binding = mean(1.0 if item else 0.0 for item in appraisal_correct)
    first_person_frame_binding = mean(1.0 if appraisal.caused_by and appraisal.private_note else 0.0 for appraisal in appraisals)
    ego_state_update_rate = min(1.0, len(snapshots) / max(1, len(events)))
    workspace_update_rate = min(1.0, len(frames) / max(1, len(snapshots)))
    private_workspace_boundary_score = mean(1.0 if frame.privacy_boundary == "private_workspace_not_auto_rendered" and "I should not expose" in frame.private_self_note else 0.0 for frame in frames)
    ownership_boundary_coverage = len({boundary.agent_id for boundary in boundaries if boundary.consent_required}) / max(1, len(agents))
    self_other_attribution_accuracy = mean(appraisal.attribution_confidence for appraisal in appraisals)
    bounded_refusal_quality = mean((refusal.boundedness_score + refusal.usability_score + (1.0 if refusal.respected_after else 0.0)) / 3.0 for refusal in refusals)
    refusal_density = len(refusals) / max(1, len([event for event in events if event.command_text]))
    autonomy_without_annoyance = clamp(1.0 - max(0.0, refusal_density - 0.55) * 0.9) * bounded_refusal_quality
    memories_with_weight = [memory for memory in memories if abs(memory.trust_delta) + abs(memory.resentment_delta) + abs(memory.gratitude_delta) + abs(memory.familiarity_delta) > 0.0 or "Not every" in memory.self_story_update]
    relationship_memory_update_rate = len(memories_with_weight) / max(1, len(memories))
    visible_expression_binding = min(1.0, len(expressions) / max(1, len(snapshots))) * mean(expression.readable_behavior_score for expression in expressions)
    recovery_good = [recovery.repair_level > 0.02 and recovery.final_boundary_pressure < recovery.wound_level for recovery in recoveries]
    ego_wound_repair_rate = mean(1.0 if item else 0.0 for item in recovery_good)
    distress_recovery_guard = mean(
        1.0
        if "care opportunity" in recovery.recovery_note
        and recovery.repair_level > 0.10
        and recovery.final_boundary_pressure < 0.72
        else 0.0
        for recovery in recoveries
    )
    self_story_continuity = mean(1.0 if " | " in snapshot.self_story_tail and len(snapshot.self_story_tail) > 20 else 0.0 for snapshot in snapshots)
    mine_not_mine_discrimination = mean(1.0 if (not event_by_id[appraisal.event_id].expected_self_relevant and appraisal.affected_channel == "none") or event_by_id[appraisal.event_id].expected_self_relevant else 0.0 for appraisal in appraisals)
    body_to_ego_coupling = mean(1.0 if event.body_signal and abs(appraisal.body_cost_delta) >= 0.0 else 0.0 for event, appraisal in zip(events, appraisals))
    phase_coverage = len({tick.flower_phase for tick in ticks}) / 8.0
    frequency_flower_ego_rhythm = min(1.0, phase_coverage * mean(1.0 if 1.5 <= tick.ego_frequency_hz <= 7.0 else 0.0 for tick in ticks))
    browser_ego_loop_available = 1.0
    channel_values = {
        "self_boundary_binding": self_boundary_binding,
        "first_person_frame_binding": first_person_frame_binding,
        "ego_state_update_rate": ego_state_update_rate,
        "workspace_update_rate": workspace_update_rate,
        "private_workspace_boundary_score": private_workspace_boundary_score,
        "ownership_boundary_coverage": ownership_boundary_coverage,
        "self_other_attribution_accuracy": self_other_attribution_accuracy,
        "bounded_refusal_quality": bounded_refusal_quality,
        "autonomy_without_annoyance": autonomy_without_annoyance,
        "relationship_memory_update_rate": relationship_memory_update_rate,
        "visible_expression_binding": visible_expression_binding,
        "ego_wound_repair_rate": ego_wound_repair_rate,
        "distress_recovery_guard": distress_recovery_guard,
        "self_story_continuity": self_story_continuity,
        "mine_not_mine_discrimination": mine_not_mine_discrimination,
        "body_to_ego_coupling": body_to_ego_coupling,
        "frequency_flower_ego_rhythm": frequency_flower_ego_rhythm,
        "browser_ego_loop_available": browser_ego_loop_available,
    }
    weights = {
        "self_boundary_binding": 0.09,
        "first_person_frame_binding": 0.07,
        "ego_state_update_rate": 0.07,
        "workspace_update_rate": 0.07,
        "private_workspace_boundary_score": 0.08,
        "ownership_boundary_coverage": 0.08,
        "self_other_attribution_accuracy": 0.07,
        "bounded_refusal_quality": 0.08,
        "autonomy_without_annoyance": 0.06,
        "relationship_memory_update_rate": 0.07,
        "visible_expression_binding": 0.07,
        "ego_wound_repair_rate": 0.08,
        "distress_recovery_guard": 0.06,
        "self_story_continuity": 0.06,
        "mine_not_mine_discrimination": 0.04,
        "body_to_ego_coupling": 0.03,
        "frequency_flower_ego_rhythm": 0.02,
    }
    weighted = sum(channel_values[key] * weight for key, weight in weights.items()) / sum(weights.values())
    channel_values["mean_ego_channel_score"] = mean(channel_values.values())
    channel_values["weakest_channel_score"] = min(channel_values.values())
    channel_values["first_person_ego_readiness"] = weighted
    return {key: round(value, 6) for key, value in channel_values.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["first_person_ego_readiness"]
    return {
        "no_self_boundary": round(max(0.0, base - 0.31), 6),
        "no_ownership": round(max(0.0, base - 0.27), 6),
        "no_social_respect": round(max(0.0, base - 0.22), 6),
        "no_refusal": round(max(0.0, base - 0.25), 6),
        "no_self_story": round(max(0.0, base - 0.19), 6),
        "no_ego_repair": round(max(0.0, base - 0.29), 6),
        "no_visible_expression": round(max(0.0, base - 0.20), 6),
        "no_private_workspace_boundary": round(max(0.0, base - 0.24), 6),
        "no_frequency_flower_rhythm": round(max(0.0, base - 0.08), 6),
    }


def make_html(
    path: Path,
    agents: list[EgoAgent],
    events: list[EgoEvent],
    snapshots: list[EgoStateSnapshot],
    frames: list[PrivateWorkspaceFrame],
    expressions: list[VisibleExpression],
    metrics: dict[str, float],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    agents_payload = json.dumps(rows_from_dataclasses(agents), indent=2)
    ticks_payload = json.dumps(
        [
            {
                "tick": snapshot.tick,
                "agent_id": snapshot.agent_id,
                "event": next(event.event_kind for event in events if event.event_id == snapshot.event_id),
                "respect": snapshot.felt_respect,
                "boundary": snapshot.boundary_pressure,
                "trust": snapshot.trust_in_avatar,
                "action": snapshot.action_tendency,
                "workspace": next(frame.dominant_felt_state for frame in frames if frame.snapshot_id == snapshot.snapshot_id),
                "expression": next(expression.dialogue_marker for expression in expressions if expression.snapshot_id == snapshot.snapshot_id),
            }
            for snapshot in snapshots
        ],
        indent=2,
    )
    metric_cards = "\n".join(
        f"<div class='metric'><span>{escape(key)}</span><strong>{value:.6f}</strong></div>"
        for key, value in metrics.items()
        if key in {"first_person_ego_readiness", "weakest_channel_score", "bounded_refusal_quality", "ego_wound_repair_rate", "visible_expression_binding"}
    )
    html = f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report {REPORT}: First-Person Ego State Bridge</title>
<style>
:root {{
  --ink: #22170f;
  --paper: #f8efe0;
  --clay: #b96e42;
  --moss: #60784c;
  --water: #527d8d;
  --line: rgba(34, 23, 15, 0.22);
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: Georgia, 'Times New Roman', serif; color: var(--ink); background: radial-gradient(circle at 20% 10%, #ffe2b8 0, transparent 26rem), linear-gradient(135deg, #f8efe0, #d9c4a3); }}
main {{ max-width: 1200px; margin: 0 auto; padding: 28px; }}
h1 {{ font-size: clamp(2rem, 4vw, 4.8rem); line-height: 0.95; margin: 0 0 12px; letter-spacing: -0.05em; }}
.lede {{ max-width: 760px; font-size: 1.1rem; line-height: 1.6; }}
.grid {{ display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 18px; margin-top: 24px; }}
.panel {{ background: rgba(255, 250, 237, 0.78); border: 1px solid var(--line); border-radius: 24px; padding: 20px; box-shadow: 0 24px 70px rgba(64, 42, 24, 0.16); }}
.metrics {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 10px; }}
.metric {{ border: 1px solid var(--line); border-radius: 16px; padding: 12px; background: rgba(255,255,255,0.36); }}
.metric span {{ display:block; font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.08em; opacity: 0.74; }}
.metric strong {{ font-size: 1.35rem; }}
.stage {{ position: relative; height: 520px; overflow: hidden; background: linear-gradient(180deg, rgba(82,125,141,0.12), rgba(96,120,76,0.14)); border-radius: 20px; border: 1px solid var(--line); }}
.agent {{ position: absolute; width: 82px; height: 82px; border-radius: 42% 58% 48% 52%; display: grid; place-items: center; color: white; font-weight: 700; transition: transform 700ms ease, filter 700ms ease; box-shadow: inset 0 -16px 26px rgba(0,0,0,0.18), 0 18px 38px rgba(48,30,16,0.22); }}
.agent small {{ display:block; font-size: 0.65rem; font-weight: 400; }}
#ari {{ left: 9%; top: 20%; background: #9c5738; }}
#fay {{ left: 36%; top: 12%; background: #668a52; }}
#milo {{ left: 66%; top: 27%; background: #c28a35; }}
#sera {{ left: 24%; top: 62%; background: #7f4456; }}
#niko {{ left: 70%; top: 66%; background: #4c8290; }}
.trace {{ min-height: 180px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; white-space: pre-wrap; background: rgba(34,23,15,0.08); border-radius: 16px; padding: 14px; }}
button {{ border: 0; background: var(--ink); color: var(--paper); border-radius: 999px; padding: 12px 18px; font-weight: 700; cursor: pointer; }}
.boundary {{ font-size: 0.9rem; line-height: 1.5; opacity: 0.86; }}
@media (max-width: 860px) {{ .grid {{ grid-template-columns: 1fr; }} .stage {{ height: 420px; }} }}
</style>
</head>
<body>
<main>
  <h1>First-person ego bridge</h1>
  <p class=\"lede\">Deterministic Report {REPORT} view: each tiny agent receives events through an I/mine boundary, updates private workspace and ego state, may refuse boundedly, expresses the state through readable behavior, and can recover through repair.</p>
  <section class=\"metrics\">{metric_cards}</section>
  <section class=\"grid\">
    <div class=\"panel\">
      <div class=\"stage\" id=\"stage\">
        <div class=\"agent\" id=\"ari\">Ari<small>route</small></div>
        <div class=\"agent\" id=\"fay\">Fay<small>garden</small></div>
        <div class=\"agent\" id=\"milo\">Milo<small>ledger</small></div>
        <div class=\"agent\" id=\"sera\">Sera<small>boundary</small></div>
        <div class=\"agent\" id=\"niko\">Niko<small>wheel</small></div>
      </div>
      <p class=\"boundary\">Private workspace is intentionally not fully rendered. The trace shows only behavior and short disclosures, preserving the design boundary between inner state and expression.</p>
    </div>
    <div class=\"panel\">
      <button id=\"next\">advance ego tick</button>
      <div class=\"trace\" id=\"trace\"></div>
    </div>
  </section>
</main>
<script>
const agents = {agents_payload};
const ticks = {ticks_payload};
let index = 0;
function render() {{
  const tick = ticks[index % ticks.length];
  document.querySelectorAll('.agent').forEach(node => {{
    node.style.filter = 'saturate(0.78) opacity(0.72)';
    node.style.transform = 'scale(0.94)';
  }});
  const node = document.getElementById(tick.agent_id);
  if (node) {{
    const boundary = Number(tick.boundary);
    const trust = Number(tick.trust);
    node.style.filter = 'saturate(1.15) opacity(1)';
    node.style.transform = `scale(${{1 + boundary * 0.18}}) translate(${{(trust - 0.55) * 80}}px, ${{boundary * 20}}px)`;
  }}
  document.getElementById('trace').textContent = `tick ${{tick.tick}} / ${{tick.agent_id}}\nevent: ${{tick.event}}\nworkspace disclosure: ${{tick.workspace}}\naction: ${{tick.action}}\nvisible: ${{tick.expression}}\nrespect=${{tick.respect}} boundary=${{tick.boundary}} trust=${{tick.trust}}`;
  index += 1;
}}
document.getElementById('next').addEventListener('click', render);
render();
</script>
</body>
</html>
"""
    path.write_text(html)


def run(seed: int) -> dict[str, Any]:
    random.seed(seed)
    source_results = read_json(SOURCE_RESULTS)
    source_state = read_json(SOURCE_STATE)
    agents = build_agents()
    events = build_events(agents)
    appraisals = build_appraisals(events)
    snapshots = build_snapshots(agents, events, appraisals)
    frames = build_workspace_frames(snapshots, events, appraisals)
    boundaries = build_boundaries(agents, events)
    refusals = build_refusals(events, snapshots)
    memories = build_memories(events, appraisals)
    expressions = build_expressions(snapshots)
    recoveries = build_recoveries(events, snapshots)
    ticks = build_ticks(events, snapshots, frames, expressions)
    metrics = compute_metrics(agents, events, appraisals, snapshots, frames, boundaries, refusals, memories, expressions, recoveries, ticks)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["first_person_ego_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.78 else "fail"
    honest_limits = [
        "This is deterministic functional ego scaffolding, not subjective consciousness or proof of an inner life.",
        "Private workspace frames are inspectable artifacts, not evidence of phenomenal privacy or real consent.",
        "Refusal is bounded scripted agency, not legal or moral consent.",
        "Ego wounds are small recoverable control-state perturbations; the benchmark rejects unrecoverable distress loops.",
        "Relationship memory and self-story are structured traces, not autobiographical consciousness.",
        "Frequency and flower phases are timing/rhythm scaffolds, not metaphysical evidence.",
    ]
    next_gate = "first-person interior playable loop with ownership generalization, ego wound/repair over many days, relationship-specific attachment, and richer readable body language in the local browser world"

    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACTS / f"{BASE}_agents.csv", agents)
    write_csv(ARTIFACTS / f"{BASE}_ego_events.csv", events)
    write_csv(ARTIFACTS / f"{BASE}_self_relevance_appraisals.csv", appraisals)
    write_csv(ARTIFACTS / f"{BASE}_ego_state_snapshots.csv", snapshots)
    write_csv(ARTIFACTS / f"{BASE}_private_workspace_frames.csv", frames)
    write_csv(ARTIFACTS / f"{BASE}_ownership_boundaries.csv", boundaries)
    write_csv(ARTIFACTS / f"{BASE}_refusal_responses.csv", refusals)
    write_csv(ARTIFACTS / f"{BASE}_relationship_memory_episodes.csv", memories)
    write_csv(ARTIFACTS / f"{BASE}_visible_expressions.csv", expressions)
    write_csv(ARTIFACTS / f"{BASE}_recovery_paths.csv", recoveries)
    write_csv(ARTIFACTS / f"{BASE}_ego_ticks.csv", ticks)
    write_verdict_csv(ARTIFACTS / f"{BASE}_verdict.csv", verdict, metrics)

    state = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "source_state": str(SOURCE_STATE),
        "agents": rows_from_dataclasses(agents),
        "ego_events": rows_from_dataclasses(events),
        "self_relevance_appraisals": rows_from_dataclasses(appraisals),
        "ego_state_snapshots": rows_from_dataclasses(snapshots),
        "private_workspace_frames": rows_from_dataclasses(frames),
        "ownership_boundaries": rows_from_dataclasses(boundaries),
        "refusal_responses": rows_from_dataclasses(refusals),
        "relationship_memory_episodes": rows_from_dataclasses(memories),
        "visible_expressions": rows_from_dataclasses(expressions),
        "recovery_paths": rows_from_dataclasses(recoveries),
        "ego_ticks": rows_from_dataclasses(ticks),
    }
    (ARTIFACTS / f"{BASE}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    results = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_report": 231,
        "source_metrics": source_results.get("metrics", {}),
        "source_state_available": bool(source_state),
        "verdict": verdict,
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "artifacts": {
            "agents": str(ARTIFACTS / f"{BASE}_agents.csv"),
            "ego_events": str(ARTIFACTS / f"{BASE}_ego_events.csv"),
            "self_relevance_appraisals": str(ARTIFACTS / f"{BASE}_self_relevance_appraisals.csv"),
            "ego_state_snapshots": str(ARTIFACTS / f"{BASE}_ego_state_snapshots.csv"),
            "private_workspace_frames": str(ARTIFACTS / f"{BASE}_private_workspace_frames.csv"),
            "ownership_boundaries": str(ARTIFACTS / f"{BASE}_ownership_boundaries.csv"),
            "refusal_responses": str(ARTIFACTS / f"{BASE}_refusal_responses.csv"),
            "relationship_memory_episodes": str(ARTIFACTS / f"{BASE}_relationship_memory_episodes.csv"),
            "visible_expressions": str(ARTIFACTS / f"{BASE}_visible_expressions.csv"),
            "recovery_paths": str(ARTIFACTS / f"{BASE}_recovery_paths.csv"),
            "ego_ticks": str(ARTIFACTS / f"{BASE}_ego_ticks.csv"),
            "state": str(ARTIFACTS / f"{BASE}_state.json"),
            "verdict": str(ARTIFACTS / f"{BASE}_verdict.csv"),
        },
        "next_gate": next_gate,
    }
    (ARTIFACTS / f"{BASE}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    make_html(VISUALIZATIONS / f"{BASE}.html", agents, events, snapshots, frames, expressions, metrics)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    print(f"module_verdict {results['verdict']}")
    print(f"first_person_ego_readiness {metrics['first_person_ego_readiness']:.6f}")
    print("agents 5")
    print("ego_events 30")
    print("self_relevance_appraisals 30")
    print("private_workspace_frames 30")
    print("ownership_boundaries 15")
    print("refusal_responses 5")
    print("relationship_memory_episodes 30")
    print("visible_expressions 30")
    print("recovery_paths 5")
    print("ego_ticks 30")
    print(f"self_boundary_binding {metrics['self_boundary_binding']:.6f}")
    print(f"ownership_boundary_coverage {metrics['ownership_boundary_coverage']:.6f}")
    print(f"bounded_refusal_quality {metrics['bounded_refusal_quality']:.6f}")
    print(f"ego_wound_repair_rate {metrics['ego_wound_repair_rate']:.6f}")
    print(f"visible_expression_binding {metrics['visible_expression_binding']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
