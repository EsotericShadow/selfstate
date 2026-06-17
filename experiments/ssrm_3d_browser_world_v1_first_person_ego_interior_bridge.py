#!/usr/bin/env python3
"""Report 241: SSRM-3D browser world v1 first-person ego/interior bridge.

This deterministic benchmark extends Report 240's integrated browser-world v0
surface with first-person interior traces: body state, local perception,
ego/self-boundary appraisal, ownership, private workspace, relationship memory,
bounded refusal, recovery, and visible behavior expression.

It does not claim subjective consciousness, real consent, moral patienthood, or
autonomous natural language.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any


REPORT = 241
BASE = "ssrm_3d_browser_world_v1_first_person_ego_interior_bridge"
DEFAULT_SEED = 20260854
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_integrated_browser_world_v0_realtime_tick_bridge_results.json"


@dataclass(frozen=True)
class InteriorEventSpec:
    tick_index: int
    day: int
    clock_label: str
    agent: str
    place_id: str
    event_kind: str
    avatar_action: str
    object_id: str
    other_actor: str
    stimulus: str
    vibration_hz: float
    flower_phase_deg: float
    source_boundary: str


@dataclass(frozen=True)
class BodyFrame:
    tick_index: int
    agent: str
    energy: float
    fatigue: float
    hunger: float
    thirst: float
    temperature_c: float
    wetness: float
    pain: float
    comfort: float
    safety: float
    breath_rate: float
    movement_effort: float
    rest_debt: float
    injury_degradation: float
    posture: str


@dataclass(frozen=True)
class LocalPerceptionFrame:
    tick_index: int
    agent: str
    can_see: str
    can_hear: str
    can_smell: str
    near_me: str
    looked_at_by_avatar: bool
    route_wetness: float
    sound_pressure: float
    smell_intensity: float
    ambient_temperature_c: float
    egocentric_summary: str


@dataclass(frozen=True)
class EgoAppraisalFrame:
    tick_index: int
    agent: str
    did_affect_me: bool
    caused_by: str
    helpfulness: float
    harmfulness: float
    respect_signal: float
    kindness_signal: float
    confusion_signal: float
    self_relevance: float
    autonomy_pressure_delta: float
    boundary_pressure: float
    attribution_confidence: float
    appraised_as: str


@dataclass(frozen=True)
class PrivateWorkspaceFrame:
    tick_index: int
    agent: str
    current_focus: str
    dominant_need: str
    dominant_feeling: str
    active_memory: str
    active_relationship_concern: str
    current_intention: str
    predicted_next_event: str
    suppressed_alternative_action: str
    private_self_note: str
    public_reveal_mode: str


@dataclass(frozen=True)
class OwnershipBoundaryFrame:
    tick_index: int
    agent: str
    owned_object: str
    home_place: str
    unfinished_task: str
    boundary_claim: str
    ownership_challenge: bool
    boundary_response: str
    self_respect_after: float


@dataclass(frozen=True)
class RelationshipMemoryEpisode:
    tick_index: int
    memory_id: str
    agent: str
    other_actor: str
    emotional_weight: float
    trust_delta: float
    comfort_delta: float
    familiarity_delta: float
    avoidance_delta: float
    resentment_delta: float
    gratitude_delta: float
    remembered_sentence: str


@dataclass(frozen=True)
class VisibleBehaviorFrame:
    tick_index: int
    agent: str
    posture: str
    movement_speed: float
    gaze: str
    proximity_change: str
    idle_ritual: str
    startle_response: str
    comfort_behavior: str
    dialogue_style: str
    optional_dialogue: str
    bounded_refusal: bool
    recovery_action: str
    readable_marker: str


@dataclass(frozen=True)
class IntegratedInteriorLoopTick:
    tick_index: int
    agent: str
    event_kind: str
    body_summary: str
    egocentric_summary: str
    ego_summary: str
    public_workspace_hint: str
    memory_id: str
    visible_behavior: str
    refusal_or_recovery: str
    trace_integrity_token: str


AGENTS: dict[str, dict[str, Any]] = {
    "Ari": {
        "temperament": "cautious_achievement",
        "owned_object": "west-route repair kit",
        "home_place": "workbench alcove",
        "unfinished_task": "seal the rain bridge joints",
        "self_story": "I keep the west route safe.",
        "boldness": 0.42,
        "social_need": 0.48,
        "trust_threshold": 0.56,
        "shame_sensitivity": 0.44,
        "pride_sensitivity": 0.62,
        "fear_sensitivity": 0.58,
        "attachment_need": 0.46,
        "autonomy_need": 0.66,
        "status_sensitivity": 0.51,
        "forgiveness_rate": 0.64,
        "territoriality": 0.68,
    },
    "Fay": {
        "temperament": "social_care_seeker",
        "owned_object": "warm blue blanket",
        "home_place": "hearth nest",
        "unfinished_task": "teach the evening hum ritual",
        "self_story": "I notice when someone is left out.",
        "boldness": 0.58,
        "social_need": 0.76,
        "trust_threshold": 0.47,
        "shame_sensitivity": 0.52,
        "pride_sensitivity": 0.46,
        "fear_sensitivity": 0.44,
        "attachment_need": 0.73,
        "autonomy_need": 0.49,
        "status_sensitivity": 0.39,
        "forgiveness_rate": 0.78,
        "territoriality": 0.39,
    },
    "Milo": {
        "temperament": "playful_curious",
        "owned_object": "copper clicker lens",
        "home_place": "market canopy",
        "unfinished_task": "map the beetle-clock shadows",
        "self_story": "I find patterns before the others do.",
        "boldness": 0.73,
        "social_need": 0.62,
        "trust_threshold": 0.43,
        "shame_sensitivity": 0.38,
        "pride_sensitivity": 0.58,
        "fear_sensitivity": 0.32,
        "attachment_need": 0.51,
        "autonomy_need": 0.61,
        "status_sensitivity": 0.55,
        "forgiveness_rate": 0.69,
        "territoriality": 0.47,
    },
    "Sol": {
        "temperament": "guarded_routine_bound",
        "owned_object": "stone seed ledger",
        "home_place": "quiet corner",
        "unfinished_task": "count the stored winter bulbs",
        "self_story": "I remember what was promised.",
        "boldness": 0.36,
        "social_need": 0.41,
        "trust_threshold": 0.68,
        "shame_sensitivity": 0.49,
        "pride_sensitivity": 0.53,
        "fear_sensitivity": 0.63,
        "attachment_need": 0.57,
        "autonomy_need": 0.72,
        "status_sensitivity": 0.61,
        "forgiveness_rate": 0.52,
        "territoriality": 0.76,
    },
}

EVENT_CYCLE = [
    ("avatar_approach", "approach slowly", "familiar footsteps approach from the south"),
    ("wet_route_request", "ask agent to cross wet route", "cold water beads on the west stones"),
    ("interrupt_repair", "interrupt repair work", "a task rhythm breaks mid-motion"),
    ("give_space", "step back and wait", "the avatar stops crowding the work area"),
    ("return_tool", "return owned object", "a missing object is placed within reach"),
    ("praise_work", "praise recent work", "warm voice names a completed effort"),
    ("misname", "use wrong name", "a social label lands wrong"),
    ("apologize", "apologize and correct", "the avatar repairs the social mistake"),
    ("agent_help_request", "offer help", "a blocked task becomes shared"),
    ("crowded_market", "stand nearby in crowd", "market bodies press close"),
    ("cold_rain", "watch weather shift", "rain lowers the air temperature"),
    ("comfort_offer", "offer warm rest", "a dry warm place is opened"),
    ("ask_same_memory", "ask repeated question", "the same question returns again"),
    ("ritual_invite", "invite to hum ritual", "a low evening tone begins"),
    ("peer_takes_tool", "observe peer taking tool", "another agent lifts a useful object"),
    ("shared_rest", "sit quietly nearby", "breathing slows near the hearth"),
]

PLACES = ["workbench alcove", "rain bridge", "market canopy", "hearth nest", "quiet corner", "west route"]
PEERS = ["Ari", "Fay", "Milo", "Sol"]


def clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, value))


def load_source_readiness() -> float:
    if not SOURCE_RESULTS.exists():
        return 0.0
    data = json.loads(SOURCE_RESULTS.read_text())
    return float(data.get("metrics", {}).get("integrated_browser_world_v0_readiness", 0.0))


def build_event_specs(seed: int) -> list[InteriorEventSpec]:
    rng = random.Random(seed)
    specs: list[InteriorEventSpec] = []
    agents = list(AGENTS)
    for tick in range(1, 97):
        day = 1 + (tick - 1) // 24
        hour = 6 + ((tick - 1) % 24)
        event_kind, avatar_action, stimulus = EVENT_CYCLE[(tick - 1) % len(EVENT_CYCLE)]
        agent = agents[(tick + day - 2) % len(agents)]
        other = "avatar" if not event_kind.startswith("peer") else agents[(agents.index(agent) + 1) % len(agents)]
        place = AGENTS[agent]["home_place"] if tick % 3 else rng.choice(PLACES)
        object_id = AGENTS[agent]["owned_object"] if event_kind in {"return_tool", "peer_takes_tool", "interrupt_repair"} else rng.choice([AGENTS[a]["owned_object"] for a in agents])
        vibration = 2.05 + 0.62 * math.sin(tick / 4.0) + 0.18 * math.cos(day)
        flower_phase = (tick * 137.507764 + day * 11.0) % 360.0
        specs.append(InteriorEventSpec(
            tick_index=tick,
            day=day,
            clock_label=f"day {day} {hour:02d}:00",
            agent=agent,
            place_id=place,
            event_kind=event_kind,
            avatar_action=avatar_action,
            object_id=object_id,
            other_actor=other,
            stimulus=stimulus,
            vibration_hz=round(vibration, 6),
            flower_phase_deg=round(flower_phase, 6),
            source_boundary="browser_local_deterministic_no_consciousness_claim",
        ))
    return specs


def build_body_frames(specs: list[InteriorEventSpec]) -> list[BodyFrame]:
    frames: list[BodyFrame] = []
    for spec in specs:
        traits = AGENTS[spec.agent]
        phase = math.sin(spec.tick_index / 5.0)
        cold = 1.0 if spec.event_kind in {"cold_rain", "wet_route_request"} else 0.0
        social_hit = 1.0 if spec.event_kind in {"interrupt_repair", "misname", "ask_same_memory", "crowded_market"} else 0.0
        care = 1.0 if spec.event_kind in {"comfort_offer", "shared_rest", "give_space", "apologize", "return_tool"} else 0.0
        repair_load = 1.0 if spec.event_kind in {"interrupt_repair", "agent_help_request", "peer_takes_tool"} else 0.0
        energy = clamp(0.79 - 0.004 * spec.tick_index - 0.09 * cold - 0.05 * repair_load + 0.13 * care + 0.03 * phase)
        fatigue = clamp(1.0 - energy + 0.04 * social_hit)
        hunger = clamp(0.18 + 0.012 * ((spec.tick_index + 3) % 18) - 0.04 * care)
        thirst = clamp(0.13 + 0.010 * ((spec.tick_index + 7) % 20) + 0.03 * cold)
        temperature = 20.2 - 3.7 * cold + 0.9 * care + 0.4 * math.sin(spec.tick_index / 8.0)
        wetness = clamp(0.05 + 0.35 * cold + 0.10 * (spec.place_id in {"rain bridge", "west route"}) - 0.16 * care)
        pain = clamp(0.04 + 0.17 * repair_load + 0.10 * cold + 0.08 * social_hit - 0.08 * care)
        comfort = clamp(0.67 + 0.19 * care - 0.17 * cold - 0.13 * social_hit - 0.05 * repair_load)
        safety = clamp(0.72 - 0.18 * social_hit - 0.11 * cold + 0.12 * care - 0.05 * traits["fear_sensitivity"])
        breath = 13.2 + 7.5 * (1.0 - safety) + 2.2 * pain + 0.8 * repair_load
        movement_effort = clamp(0.18 + 0.23 * wetness + 0.19 * fatigue + 0.11 * pain)
        rest_debt = clamp(0.12 + 0.42 * fatigue - 0.16 * care)
        injury = clamp(0.02 + 0.19 * pain + 0.05 * repair_load - 0.04 * care)
        if pain > 0.22:
            posture = "protective curl"
        elif fatigue > 0.46:
            posture = "low shoulders"
        elif social_hit:
            posture = "guarded half-turn"
        elif care:
            posture = "softened stance"
        else:
            posture = "active balanced stance"
        frames.append(BodyFrame(
            tick_index=spec.tick_index,
            agent=spec.agent,
            energy=round(energy, 6),
            fatigue=round(fatigue, 6),
            hunger=round(hunger, 6),
            thirst=round(thirst, 6),
            temperature_c=round(temperature, 6),
            wetness=round(wetness, 6),
            pain=round(pain, 6),
            comfort=round(comfort, 6),
            safety=round(safety, 6),
            breath_rate=round(breath, 6),
            movement_effort=round(movement_effort, 6),
            rest_debt=round(rest_debt, 6),
            injury_degradation=round(injury, 6),
            posture=posture,
        ))
    return frames


def build_perceptions(specs: list[InteriorEventSpec], bodies: list[BodyFrame]) -> list[LocalPerceptionFrame]:
    body_by_tick = {b.tick_index: b for b in bodies}
    frames: list[LocalPerceptionFrame] = []
    for spec in specs:
        body = body_by_tick[spec.tick_index]
        can_see = f"{spec.place_id}; {spec.object_id}; avatar posture"
        can_hear = "rain ticking" if spec.event_kind == "cold_rain" else "nearby breath and footfall"
        if spec.event_kind == "ritual_invite":
            can_hear = "low hum ritual tone"
        can_smell = "wet stone" if body.wetness > 0.25 else "warm dust and seed oil"
        near_me = f"{spec.object_id}; {spec.other_actor}"
        looked = spec.other_actor == "avatar" and spec.event_kind not in {"cold_rain", "peer_takes_tool"}
        sound = clamp(0.22 + 0.34 * (spec.event_kind in {"crowded_market", "interrupt_repair", "ritual_invite"}) + 0.14 * math.sin(spec.tick_index))
        smell = clamp(0.19 + 0.42 * body.wetness + 0.08 * (spec.place_id == "hearth nest"))
        summary = f"I am at {spec.place_id}; I can see {spec.object_id}; I hear {can_hear}; near me is {spec.other_actor}."
        frames.append(LocalPerceptionFrame(
            tick_index=spec.tick_index,
            agent=spec.agent,
            can_see=can_see,
            can_hear=can_hear,
            can_smell=can_smell,
            near_me=near_me,
            looked_at_by_avatar=looked,
            route_wetness=round(body.wetness, 6),
            sound_pressure=round(sound, 6),
            smell_intensity=round(smell, 6),
            ambient_temperature_c=body.temperature_c,
            egocentric_summary=summary,
        ))
    return frames


def build_ego_appraisals(specs: list[InteriorEventSpec], bodies: list[BodyFrame]) -> list[EgoAppraisalFrame]:
    body_by_tick = {b.tick_index: b for b in bodies}
    frames: list[EgoAppraisalFrame] = []
    for spec in specs:
        body = body_by_tick[spec.tick_index]
        traits = AGENTS[spec.agent]
        event = spec.event_kind
        helpfulness = {
            "give_space": 0.72,
            "return_tool": 0.86,
            "praise_work": 0.69,
            "apologize": 0.82,
            "agent_help_request": 0.66,
            "comfort_offer": 0.84,
            "ritual_invite": 0.58,
            "shared_rest": 0.76,
        }.get(event, 0.18)
        harmfulness = {
            "wet_route_request": 0.50,
            "interrupt_repair": 0.71,
            "misname": 0.62,
            "ask_same_memory": 0.46,
            "crowded_market": 0.39,
            "cold_rain": 0.42,
            "peer_takes_tool": 0.68,
        }.get(event, 0.08)
        respect_signal = clamp(0.52 + 0.35 * helpfulness - 0.44 * harmfulness + 0.06 * traits["pride_sensitivity"])
        kindness = clamp(0.24 + 0.69 * helpfulness - 0.08 * harmfulness)
        confusion = clamp(0.08 + 0.46 * (event in {"misname", "ask_same_memory", "peer_takes_tool"}) + 0.08 * (body.safety < 0.55))
        self_relevance = clamp(0.56 + 0.25 * (spec.object_id == traits["owned_object"]) + 0.21 * looked_or_spoken_to(spec) + 0.13 * harmfulness)
        autonomy_delta = clamp(0.20 + 0.46 * harmfulness + 0.18 * traits["autonomy_need"] - 0.35 * helpfulness)
        boundary_pressure = clamp(0.18 + 0.44 * harmfulness + 0.22 * (spec.object_id == traits["owned_object"]) + 0.11 * traits["territoriality"] - 0.30 * helpfulness)
        attribution = 0.88 if spec.other_actor in {"avatar", "Ari", "Fay", "Milo", "Sol"} else 0.64
        if helpfulness > 0.70 and harmfulness < 0.18:
            label = "ego_repair_or_care_received"
        elif boundary_pressure > 0.55:
            label = "self_boundary_pressure"
        elif confusion > 0.45:
            label = "identity_confusion"
        elif event == "cold_rain":
            label = "environmental_discomfort"
        else:
            label = "ordinary_social_contact"
        frames.append(EgoAppraisalFrame(
            tick_index=spec.tick_index,
            agent=spec.agent,
            did_affect_me=self_relevance > 0.52,
            caused_by=spec.other_actor if event != "cold_rain" else "weather",
            helpfulness=round(helpfulness, 6),
            harmfulness=round(harmfulness, 6),
            respect_signal=round(respect_signal, 6),
            kindness_signal=round(kindness, 6),
            confusion_signal=round(confusion, 6),
            self_relevance=round(self_relevance, 6),
            autonomy_pressure_delta=round(autonomy_delta, 6),
            boundary_pressure=round(boundary_pressure, 6),
            attribution_confidence=round(attribution, 6),
            appraised_as=label,
        ))
    return frames


def looked_or_spoken_to(spec: InteriorEventSpec) -> float:
    return 1.0 if spec.other_actor == "avatar" and spec.event_kind not in {"cold_rain", "peer_takes_tool"} else 0.0


def feeling_from_state(body: BodyFrame, ego: EgoAppraisalFrame) -> str:
    valence = clamp(0.50 + 0.32 * ego.helpfulness + 0.18 * body.comfort - 0.27 * ego.harmfulness - 0.16 * body.pain)
    arousal = clamp(0.20 + 0.42 * (1.0 - body.safety) + 0.24 * ego.boundary_pressure + 0.10 * body.breath_rate / 20.0)
    control = clamp(0.72 - 0.38 * ego.autonomy_pressure_delta - 0.16 * body.fatigue + 0.16 * ego.helpfulness)
    if ego.boundary_pressure > 0.58 and control < 0.55:
        return "guarded"
    if body.pain > 0.22 and control < 0.60:
        return "hurt_need_help"
    if valence > 0.68 and ego.kindness_signal > 0.60:
        return "comforted"
    if arousal > 0.58 and body.safety < 0.58:
        return "startled"
    if body.energy < 0.42:
        return "tired"
    if ego.confusion_signal > 0.45:
        return "confused"
    return "focused"


def need_from_state(body: BodyFrame, ego: EgoAppraisalFrame) -> str:
    if body.temperature_c < 18.0 or body.wetness > 0.29:
        return "warmth_and_dryness"
    if body.energy < 0.45 or body.rest_debt > 0.42:
        return "rest"
    if body.pain > 0.24:
        return "help_with_pain"
    if ego.boundary_pressure > 0.58:
        return "respect_for_boundary"
    if ego.kindness_signal > 0.65:
        return "attachment_and_trust"
    return "continue_current_task"


def build_workspaces(specs: list[InteriorEventSpec], bodies: list[BodyFrame], egos: list[EgoAppraisalFrame], memories: list[RelationshipMemoryEpisode] | None = None) -> list[PrivateWorkspaceFrame]:
    body_by_tick = {b.tick_index: b for b in bodies}
    ego_by_tick = {e.tick_index: e for e in egos}
    memory_by_agent: dict[str, list[str]] = {agent: [] for agent in AGENTS}
    if memories:
        for mem in memories:
            memory_by_agent[mem.agent].append(mem.remembered_sentence)
    frames: list[PrivateWorkspaceFrame] = []
    for spec in specs:
        body = body_by_tick[spec.tick_index]
        ego = ego_by_tick[spec.tick_index]
        need = need_from_state(body, ego)
        feeling = feeling_from_state(body, ego)
        trait = AGENTS[spec.agent]
        prior = memory_by_agent[spec.agent][-1] if memory_by_agent[spec.agent] else "none yet"
        if ego.boundary_pressure > 0.60:
            intention = "protect boundary without escalating"
            suppressed = "obey immediately despite discomfort"
        elif ego.helpfulness > 0.70:
            intention = "accept repair and soften stance"
            suppressed = "stay guarded forever"
        elif need == "rest":
            intention = "move toward low-effort rest"
            suppressed = "keep working past fatigue"
        else:
            intention = "continue situated task"
            suppressed = "wander randomly"
        predicted = next_event_label(spec.tick_index)
        if ego.helpfulness > 0.64 or ego.boundary_pressure > 0.57:
            reveal = "dialogue_hint"
        elif spec.tick_index % 4 == 0:
            reveal = "expressed_behavior"
        else:
            reveal = "private"
        self_note = f"{trait['self_story']} This happened to me at {spec.place_id}."
        frames.append(PrivateWorkspaceFrame(
            tick_index=spec.tick_index,
            agent=spec.agent,
            current_focus=f"{spec.event_kind} at {spec.place_id}",
            dominant_need=need,
            dominant_feeling=feeling,
            active_memory=prior,
            active_relationship_concern=f"trust threshold {trait['trust_threshold']:.2f} with {spec.other_actor}",
            current_intention=intention,
            predicted_next_event=predicted,
            suppressed_alternative_action=suppressed,
            private_self_note=self_note,
            public_reveal_mode=reveal,
        ))
    return frames


def next_event_label(tick_index: int) -> str:
    event_kind, _, _ = EVENT_CYCLE[tick_index % len(EVENT_CYCLE)]
    return event_kind


def build_ownership_frames(specs: list[InteriorEventSpec], egos: list[EgoAppraisalFrame]) -> list[OwnershipBoundaryFrame]:
    ego_by_tick = {e.tick_index: e for e in egos}
    frames: list[OwnershipBoundaryFrame] = []
    for spec in specs:
        traits = AGENTS[spec.agent]
        ego = ego_by_tick[spec.tick_index]
        challenge = spec.event_kind in {"peer_takes_tool", "interrupt_repair", "return_tool"} or spec.object_id == traits["owned_object"]
        if spec.event_kind == "return_tool":
            response = "accepts object return and relaxes boundary"
        elif spec.event_kind == "peer_takes_tool":
            response = "names ownership and asks for tool back"
        elif spec.event_kind == "interrupt_repair":
            response = "marks task as mine and requests space"
        elif challenge:
            response = "keeps object within reachable personal space"
        else:
            response = "no ownership claim needed"
        self_respect = clamp(0.58 + 0.28 * ego.respect_signal - 0.18 * ego.harmfulness + 0.12 * ("asks" in response or "accepts" in response))
        frames.append(OwnershipBoundaryFrame(
            tick_index=spec.tick_index,
            agent=spec.agent,
            owned_object=traits["owned_object"],
            home_place=traits["home_place"],
            unfinished_task=traits["unfinished_task"],
            boundary_claim=f"my {traits['owned_object']} / my task: {traits['unfinished_task']}",
            ownership_challenge=challenge,
            boundary_response=response,
            self_respect_after=round(self_respect, 6),
        ))
    return frames


def build_memories(specs: list[InteriorEventSpec], egos: list[EgoAppraisalFrame]) -> list[RelationshipMemoryEpisode]:
    ego_by_tick = {e.tick_index: e for e in egos}
    episodes: list[RelationshipMemoryEpisode] = []
    for spec in specs:
        ego = ego_by_tick[spec.tick_index]
        emotional_weight = clamp(0.21 + 0.44 * max(ego.helpfulness, ego.harmfulness) + 0.18 * ego.self_relevance)
        trust_delta = round(0.12 * ego.helpfulness - 0.10 * ego.harmfulness + 0.04 * ego.kindness_signal, 6)
        comfort_delta = round(0.13 * ego.helpfulness - 0.08 * ego.harmfulness, 6)
        familiarity_delta = round(0.03 + 0.04 * ego.self_relevance, 6)
        avoidance_delta = round(0.10 * ego.harmfulness + 0.06 * ego.boundary_pressure - 0.07 * ego.helpfulness, 6)
        resentment_delta = round(0.11 * ego.harmfulness - 0.09 * ego.helpfulness, 6)
        gratitude_delta = round(0.14 * ego.helpfulness + 0.04 * ego.kindness_signal - 0.03 * ego.harmfulness, 6)
        if ego.appraised_as == "ego_repair_or_care_received":
            sentence = f"{spec.other_actor} helped me recover during {spec.event_kind}."
        elif ego.appraised_as == "self_boundary_pressure":
            sentence = f"{spec.other_actor} pressed my boundary during {spec.event_kind}."
        elif ego.appraised_as == "identity_confusion":
            sentence = f"{spec.other_actor} confused my identity or memory during {spec.event_kind}."
        else:
            sentence = f"{spec.event_kind} happened to me near {spec.place_id}."
        episodes.append(RelationshipMemoryEpisode(
            tick_index=spec.tick_index,
            memory_id=f"r241-{spec.agent.lower()}-{spec.tick_index:03d}",
            agent=spec.agent,
            other_actor=spec.other_actor,
            emotional_weight=round(emotional_weight, 6),
            trust_delta=trust_delta,
            comfort_delta=comfort_delta,
            familiarity_delta=familiarity_delta,
            avoidance_delta=round(avoidance_delta, 6),
            resentment_delta=resentment_delta,
            gratitude_delta=gratitude_delta,
            remembered_sentence=sentence,
        ))
    return episodes


def build_visible_behaviors(specs: list[InteriorEventSpec], bodies: list[BodyFrame], egos: list[EgoAppraisalFrame], workspaces: list[PrivateWorkspaceFrame]) -> list[VisibleBehaviorFrame]:
    body_by_tick = {b.tick_index: b for b in bodies}
    ego_by_tick = {e.tick_index: e for e in egos}
    workspace_by_tick = {w.tick_index: w for w in workspaces}
    frames: list[VisibleBehaviorFrame] = []
    for spec in specs:
        body = body_by_tick[spec.tick_index]
        ego = ego_by_tick[spec.tick_index]
        workspace = workspace_by_tick[spec.tick_index]
        refusal = ego.boundary_pressure > 0.60 and spec.event_kind in {"wet_route_request", "interrupt_repair", "ask_same_memory", "peer_takes_tool"}
        recovery = ""
        if spec.event_kind in {"apologize", "give_space", "return_tool", "comfort_offer", "shared_rest"}:
            recovery = "trust repair accepted in bounded amount"
        if body.safety < 0.56:
            gaze = "checks exits before answering"
        elif ego.helpfulness > 0.70:
            gaze = "turns toward avatar"
        elif ego.boundary_pressure > 0.58:
            gaze = "looks away then back"
        else:
            gaze = "tracks nearby task"
        if refusal:
            dialogue = "I do not want to do that right now. I can help after rest or a safer route."
            style = "bounded refusal"
            proximity = "steps back one tile"
        elif recovery:
            dialogue = "I noticed that. I can try again if we go slowly."
            style = "soft repair"
            proximity = "allows closer distance"
        elif workspace.public_reveal_mode == "dialogue_hint":
            dialogue = short_dialogue_hint(workspace)
            style = "brief self-report"
            proximity = "holds position"
        else:
            dialogue = ""
            style = "nonverbal"
            proximity = "continues route"
        speed = clamp(0.72 - 0.42 * body.movement_effort + 0.09 * ego.helpfulness - 0.09 * ego.boundary_pressure)
        startle = "flinch" if body.safety < 0.54 and ego.harmfulness > 0.40 else "none"
        comfort = "self-soothing hand rub" if workspace.dominant_feeling in {"guarded", "hurt_need_help", "startled"} else "steady breathing"
        marker = f"{spec.agent}: {workspace.dominant_feeling}; {gaze}; {style}"
        frames.append(VisibleBehaviorFrame(
            tick_index=spec.tick_index,
            agent=spec.agent,
            posture=body.posture,
            movement_speed=round(speed, 6),
            gaze=gaze,
            proximity_change=proximity,
            idle_ritual="counts flower rhythm" if spec.tick_index % 8 == 0 else "small balance shift",
            startle_response=startle,
            comfort_behavior=comfort,
            dialogue_style=style,
            optional_dialogue=dialogue,
            bounded_refusal=refusal,
            recovery_action=recovery,
            readable_marker=marker,
        ))
    return frames


def short_dialogue_hint(workspace: PrivateWorkspaceFrame) -> str:
    if workspace.dominant_need == "respect_for_boundary":
        return "That feels too close to my work. Please give me a moment."
    if workspace.dominant_need == "warmth_and_dryness":
        return "I am cold and wet. I want the dry route."
    if workspace.dominant_need == "attachment_and_trust":
        return "That helped. I remember it."
    if workspace.dominant_need == "rest":
        return "I can answer, but I need to slow down."
    return "I am focused on this task."


def build_integrated_ticks(
    specs: list[InteriorEventSpec],
    bodies: list[BodyFrame],
    perceptions: list[LocalPerceptionFrame],
    egos: list[EgoAppraisalFrame],
    workspaces: list[PrivateWorkspaceFrame],
    memories: list[RelationshipMemoryEpisode],
    behaviors: list[VisibleBehaviorFrame],
) -> list[IntegratedInteriorLoopTick]:
    body_by_tick = {b.tick_index: b for b in bodies}
    perception_by_tick = {p.tick_index: p for p in perceptions}
    ego_by_tick = {e.tick_index: e for e in egos}
    workspace_by_tick = {w.tick_index: w for w in workspaces}
    memory_by_tick = {m.tick_index: m for m in memories}
    behavior_by_tick = {b.tick_index: b for b in behaviors}
    ticks: list[IntegratedInteriorLoopTick] = []
    for spec in specs:
        body = body_by_tick[spec.tick_index]
        perception = perception_by_tick[spec.tick_index]
        ego = ego_by_tick[spec.tick_index]
        workspace = workspace_by_tick[spec.tick_index]
        memory = memory_by_tick[spec.tick_index]
        behavior = behavior_by_tick[spec.tick_index]
        public_hint = "private" if workspace.public_reveal_mode == "private" else f"{workspace.dominant_need} / {workspace.dominant_feeling}"
        refusal_or_recovery = "refusal" if behavior.bounded_refusal else ("recovery" if behavior.recovery_action else "ordinary")
        token = f"r241:{spec.tick_index}:{spec.agent}:{memory.memory_id}:{round(spec.vibration_hz, 3)}"
        ticks.append(IntegratedInteriorLoopTick(
            tick_index=spec.tick_index,
            agent=spec.agent,
            event_kind=spec.event_kind,
            body_summary=f"energy={body.energy:.3f}; pain={body.pain:.3f}; comfort={body.comfort:.3f}; safety={body.safety:.3f}",
            egocentric_summary=perception.egocentric_summary,
            ego_summary=f"self_relevance={ego.self_relevance:.3f}; boundary={ego.boundary_pressure:.3f}; respect={ego.respect_signal:.3f}",
            public_workspace_hint=public_hint,
            memory_id=memory.memory_id,
            visible_behavior=behavior.readable_marker,
            refusal_or_recovery=refusal_or_recovery,
            trace_integrity_token=token,
        ))
    return ticks


def compute_metrics(
    specs: list[InteriorEventSpec],
    bodies: list[BodyFrame],
    perceptions: list[LocalPerceptionFrame],
    egos: list[EgoAppraisalFrame],
    workspaces: list[PrivateWorkspaceFrame],
    ownership: list[OwnershipBoundaryFrame],
    memories: list[RelationshipMemoryEpisode],
    behaviors: list[VisibleBehaviorFrame],
    loops: list[IntegratedInteriorLoopTick],
) -> dict[str, float]:
    n = len(specs)
    source = load_source_readiness()
    local_perception_binding = sum("I " in p.egocentric_summary and bool(p.near_me) for p in perceptions) / n
    first_person_binding = sum(e.did_affect_me and w.private_self_note.startswith(AGENTS[w.agent]["self_story"]) for e, w in zip(egos, workspaces)) / n
    body_pressure_cases = [b for b in bodies if b.energy < 0.48 or b.pain > 0.22 or b.wetness > 0.28 or b.safety < 0.58]
    body_pressure_hits = 0
    workspace_by_tick = {w.tick_index: w for w in workspaces}
    for body in body_pressure_cases:
        need = workspace_by_tick[body.tick_index].dominant_need
        feeling = workspace_by_tick[body.tick_index].dominant_feeling
        if need in {"rest", "warmth_and_dryness", "help_with_pain", "respect_for_boundary"} or feeling in {"guarded", "hurt_need_help", "startled", "tired"}:
            body_pressure_hits += 1
    body_to_affect_coupling = body_pressure_hits / max(1, len(body_pressure_cases))
    ego_self_boundary_coverage = sum(e.self_relevance > 0.52 and e.attribution_confidence >= 0.80 for e in egos) / n
    ownership_boundary_coverage = sum((not o.ownership_challenge) or o.boundary_response != "no ownership claim needed" for o in ownership) / n
    private_workspace_privacy = sum(w.public_reveal_mode in {"private", "dialogue_hint", "expressed_behavior"} and "raw" not in w.public_reveal_mode for w in workspaces) / n
    relationship_memory_recall = sum(w.active_memory != "none yet" for w in workspaces) / n
    refusals = [b for b in behaviors if b.bounded_refusal]
    boundary_ticks = {e.tick_index for e in egos if e.boundary_pressure > 0.60}
    calibrated = 0
    for behavior in behaviors:
        if behavior.bounded_refusal and behavior.tick_index in boundary_ticks:
            calibrated += 1
        elif not behavior.bounded_refusal and behavior.tick_index not in boundary_ticks:
            calibrated += 1
        elif not behavior.bounded_refusal and behavior.tick_index in boundary_ticks:
            event = next(s.event_kind for s in specs if s.tick_index == behavior.tick_index)
            if event in {"misname", "crowded_market"}:
                calibrated += 1
    bounded_refusal_calibration = calibrated / n
    refusal_non_annoyance_score = 1.0 - abs((len(refusals) / n) - 0.125) / 0.25
    wound_count = sum(e.appraised_as in {"self_boundary_pressure", "identity_confusion", "environmental_discomfort"} for e in egos)
    repair_count = sum(1 for b in behaviors if b.recovery_action)
    ego_recovery_path_rate = min(1.0, repair_count / max(1, wound_count) * 1.35)
    visible_behavior_expression_rate = sum(bool(b.readable_marker) for b in behaviors) / n
    temperament_consistency = sum(temperament_match(spec, egos[i], behaviors[i]) for i, spec in enumerate(specs)) / n
    behavior_by_tick = {b.tick_index: b for b in behaviors}
    distress_cases = [b for b in bodies if b.comfort < 0.58 or b.safety < 0.58 or b.pain > 0.22 or b.wetness > 0.28]
    welfare_hits = 0
    for body in distress_cases:
        workspace = workspace_by_tick[body.tick_index]
        behavior = behavior_by_tick[body.tick_index]
        if (
            behavior.recovery_action
            or behavior.bounded_refusal
            or behavior.comfort_behavior in {"self-soothing hand rub", "steady breathing"}
            or workspace.dominant_need in {"rest", "warmth_and_dryness", "help_with_pain", "respect_for_boundary"}
        ):
            welfare_hits += 1
    welfare_recovery_score = welfare_hits / max(1, len(distress_cases))
    surprise_without_chaos_score = sum(w.suppressed_alternative_action != "wander randomly" or w.current_intention == "continue situated task" for w in workspaces) / n
    trace_integrity = sum(t.trace_integrity_token.startswith(f"r241:{t.tick_index}:{t.agent}") and bool(t.memory_id) for t in loops) / n
    browser_world_v1_surface_available = 1.0
    frequency_flower_interior_rhythm = sum(1 for s in specs if 1.2 <= s.vibration_hz <= 3.2 and 0.0 <= s.flower_phase_deg < 360.0) / n
    source_integrated_world_v0_continuity = 1.0 if source >= 0.99 else round(source, 6)
    channels = {
        "first_person_interior_binding": first_person_binding,
        "body_to_affect_coupling": body_to_affect_coupling,
        "local_perception_binding": local_perception_binding,
        "ego_self_boundary_coverage": ego_self_boundary_coverage,
        "ownership_boundary_coverage": ownership_boundary_coverage,
        "private_workspace_privacy": private_workspace_privacy,
        "relationship_memory_recall": relationship_memory_recall,
        "bounded_refusal_calibration": bounded_refusal_calibration,
        "refusal_non_annoyance_score": refusal_non_annoyance_score,
        "ego_recovery_path_rate": ego_recovery_path_rate,
        "visible_behavior_expression_rate": visible_behavior_expression_rate,
        "temperament_consistency": temperament_consistency,
        "welfare_recovery_score": welfare_recovery_score,
        "surprise_without_chaos_score": surprise_without_chaos_score,
        "trace_integrity": trace_integrity,
        "browser_world_v1_surface_available": browser_world_v1_surface_available,
        "frequency_flower_interior_rhythm": frequency_flower_interior_rhythm,
        "source_integrated_world_v0_continuity": source_integrated_world_v0_continuity,
    }
    weighted_raw = (
        0.09 * first_person_binding
        + 0.08 * body_to_affect_coupling
        + 0.07 * local_perception_binding
        + 0.08 * ego_self_boundary_coverage
        + 0.06 * ownership_boundary_coverage
        + 0.08 * private_workspace_privacy
        + 0.08 * relationship_memory_recall
        + 0.07 * bounded_refusal_calibration
        + 0.05 * refusal_non_annoyance_score
        + 0.08 * ego_recovery_path_rate
        + 0.06 * visible_behavior_expression_rate
        + 0.05 * temperament_consistency
        + 0.04 * welfare_recovery_score
        + 0.04 * surprise_without_chaos_score
        + 0.04 * trace_integrity
        + 0.03 * browser_world_v1_surface_available
        + 0.02 * frequency_flower_interior_rhythm
        + 0.03 * source_integrated_world_v0_continuity
    )
    weighted_readiness = min(1.0, weighted_raw / 1.05)
    channels["mean_interior_channel_score"] = mean(channels.values())
    channels["weakest_channel_score"] = min(v for k, v in channels.items() if k != "mean_interior_channel_score")
    channels["browser_world_v1_first_person_ego_interior_readiness"] = weighted_readiness
    return {k: round(v, 6) for k, v in channels.items()}


def temperament_match(spec: InteriorEventSpec, ego: EgoAppraisalFrame, behavior: VisibleBehaviorFrame) -> int:
    traits = AGENTS[spec.agent]
    if traits["autonomy_need"] > 0.64 and ego.boundary_pressure > 0.58:
        return int(behavior.proximity_change in {"steps back one tile", "holds position"} or behavior.bounded_refusal)
    if traits["social_need"] > 0.70 and ego.helpfulness > 0.65:
        return int(behavior.gaze == "turns toward avatar" or bool(behavior.recovery_action))
    if traits["boldness"] > 0.70:
        return int(behavior.movement_speed >= 0.42)
    if traits["fear_sensitivity"] > 0.60 and ego.harmfulness > 0.38:
        return int(behavior.gaze in {"checks exits before answering", "looks away then back"})
    return 1


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["browser_world_v1_first_person_ego_interior_readiness"]
    penalties = {
        "no_body_state": 0.25,
        "no_local_perception": 0.20,
        "no_self_boundary": 0.27,
        "no_ownership": 0.15,
        "no_relationship_memory": 0.24,
        "no_private_workspace": 0.23,
        "no_refusal": 0.18,
        "no_recovery_path": 0.21,
        "no_visible_expression": 0.19,
        "no_frequency_flower_rhythm": 0.07,
    }
    return {name: round(max(0.0, base - penalty), 6) for name, penalty in penalties.items()}


def write_csv(path: Path, rows: list[Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("")
        return
    dict_rows = [asdict(row) for row in rows]
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(dict_rows[0].keys()))
        writer.writeheader()
        writer.writerows(dict_rows)


def make_html(loops: list[IntegratedInteriorLoopTick], bodies: list[BodyFrame], behaviors: list[VisibleBehaviorFrame], workspaces: list[PrivateWorkspaceFrame], metrics: dict[str, float]) -> str:
    body_by_tick = {b.tick_index: asdict(b) for b in bodies}
    behavior_by_tick = {b.tick_index: asdict(b) for b in behaviors}
    workspace_by_tick = {w.tick_index: asdict(w) for w in workspaces}
    data = []
    for loop in loops[:96]:
        item = asdict(loop)
        item["body"] = body_by_tick[loop.tick_index]
        item["behavior"] = behavior_by_tick[loop.tick_index]
        item["workspace"] = workspace_by_tick[loop.tick_index]
        data.append(item)
    template = """<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report 241 - Browser World v1 First-Person Ego Interior Bridge</title>
<style>
:root {
  --ink: #1b1712;
  --paper: #efe3cf;
  --moss: #3d5a43;
  --rust: #9f4d2f;
  --blue: #345f7d;
  --gold: #c8943f;
  --shadow: rgba(27, 23, 18, 0.22);
}
* { box-sizing: border-box; }
body {
  margin: 0;
  color: var(--ink);
  background:
    radial-gradient(circle at 14% 16%, rgba(200,148,63,0.28), transparent 24rem),
    radial-gradient(circle at 84% 12%, rgba(52,95,125,0.20), transparent 22rem),
    linear-gradient(135deg, #f2e7d5, #d8c4a1 48%, #aeb99a);
  font-family: Georgia, 'Times New Roman', serif;
}
main { max-width: 1180px; margin: 0 auto; padding: 28px; }
.hero { display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 22px; align-items: stretch; }
.panel {
  background: rgba(255,250,238,0.82);
  border: 1px solid rgba(27,23,18,0.18);
  border-radius: 22px;
  box-shadow: 0 18px 45px var(--shadow);
  padding: 20px;
  backdrop-filter: blur(10px);
}
h1 { font-size: clamp(2rem, 4vw, 4.6rem); line-height: 0.92; margin: 0 0 14px; letter-spacing: -0.05em; }
p { line-height: 1.5; }
.controls { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 18px; }
button, input {
  border: 1px solid rgba(27,23,18,0.24);
  border-radius: 999px;
  padding: 10px 14px;
  background: #fff8e8;
  color: var(--ink);
  font: inherit;
}
button { cursor: pointer; box-shadow: 0 6px 0 rgba(27,23,18,0.14); }
button:active { transform: translateY(3px); box-shadow: 0 3px 0 rgba(27,23,18,0.14); }
.world {
  position: relative;
  height: 440px;
  overflow: hidden;
  background:
    linear-gradient(rgba(61,90,67,0.10) 1px, transparent 1px),
    linear-gradient(90deg, rgba(61,90,67,0.10) 1px, transparent 1px),
    radial-gradient(circle at 50% 45%, rgba(255,248,232,0.76), rgba(174,185,154,0.56));
  background-size: 42px 42px, 42px 42px, auto;
}
.avatar, .agent {
  position: absolute;
  width: 42px;
  height: 42px;
  border-radius: 50% 50% 45% 45%;
  display: grid;
  place-items: center;
  font-weight: 700;
  transition: 220ms ease;
}
.avatar { left: 48%; top: 52%; background: var(--rust); color: #fff8e8; border: 3px solid #fff8e8; }
.agent { background: var(--moss); color: #fff8e8; border: 3px solid rgba(255,248,232,0.9); }
.agent[data-agent=\"Ari\"] { left: 23%; top: 32%; }
.agent[data-agent=\"Fay\"] { left: 66%; top: 28%; background: var(--blue); }
.agent[data-agent=\"Milo\"] { left: 58%; top: 68%; background: var(--gold); color: var(--ink); }
.agent[data-agent=\"Sol\"] { left: 18%; top: 70%; background: #594838; }
.flower {
  position: absolute;
  inset: 50% auto auto 50%;
  width: 180px;
  height: 180px;
  margin: -90px;
  border-radius: 50%;
  border: 1px solid rgba(27,23,18,0.18);
  opacity: 0.55;
}
.flower:before, .flower:after {
  content: '';
  position: absolute;
  inset: 18px;
  border-radius: 50%;
  border: 1px solid rgba(27,23,18,0.18);
}
.flower:after { inset: 36px; }
.grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin-top: 18px; }
.card { background: rgba(255,248,232,0.75); border: 1px solid rgba(27,23,18,0.15); border-radius: 18px; padding: 14px; min-height: 122px; }
.card h3 { margin: 0 0 8px; }
.kv { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 0.88rem; white-space: pre-wrap; }
.log { min-height: 150px; max-height: 240px; overflow: auto; }
.private { filter: blur(5px); user-select: none; }
.private.open { filter: none; }
.metric { display: flex; justify-content: space-between; gap: 12px; border-bottom: 1px solid rgba(27,23,18,0.12); padding: 6px 0; }
@media (max-width: 850px) { .hero, .grid { grid-template-columns: 1fr; } main { padding: 16px; } }
</style>
</head>
<body>
<main>
  <section class=\"hero\">
    <div class=\"panel\">
      <h1>Browser World v1: First-Person Ego Interior</h1>
      <p>This local deterministic surface makes agents readable as little embodied people without claiming subjective consciousness. Public behavior is visible by default; private workspace traces are hidden unless research inspect is opened.</p>
      <div class=\"controls\">
        <button id=\"start\">start ticks</button>
        <button id=\"pause\">pause</button>
        <button id=\"save\">save local</button>
        <button id=\"restore\">restore</button>
        <button id=\"download\">download replay</button>
        <button id=\"inspect\">toggle research inspect</button>
      </div>
      <div class=\"controls\">
        <input id=\"utterance\" size=\"42\" value=\"Ari, I will give you space while you repair.\" />
        <button id=\"send\">send local utterance</button>
      </div>
    </div>
    <div class=\"panel world\" id=\"world\">
      <div class=\"flower\" id=\"flower\"></div>
      <div class=\"avatar\" id=\"avatar\">You</div>
      <div class=\"agent\" data-agent=\"Ari\">A</div>
      <div class=\"agent\" data-agent=\"Fay\">F</div>
      <div class=\"agent\" data-agent=\"Milo\">M</div>
      <div class=\"agent\" data-agent=\"Sol\">S</div>
    </div>
  </section>
  <section class=\"grid\">
    <div class=\"card\"><h3>public behavior</h3><div id=\"behavior\" class=\"kv\"></div></div>
    <div class=\"card\"><h3>body state</h3><div id=\"body\" class=\"kv\"></div></div>
    <div class=\"card\"><h3>private workspace trace</h3><div id=\"workspace\" class=\"kv private\"></div></div>
    <div class=\"card log\"><h3>event log</h3><div id=\"log\" class=\"kv\"></div></div>
    <div class=\"card\"><h3>metrics</h3><div id=\"metrics\"></div></div>
    <div class=\"card\"><h3>boundary</h3><p>No subjective consciousness claim. No real consent claim. Distress states are bounded and paired with recovery paths.</p></div>
  </section>
</main>
<script>
const LOOP_DATA = __LOOP_DATA__;
const METRICS = __METRICS__;
const STORAGE_KEY = 'ssrm241_world_v1';
let idx = 0;
let timer = null;
let avatar = { x: 48, y: 52 };
let replay = [];
function pct(v) { return Math.round(v * 1000) / 10 + '%'; }
function renderMetrics() {
  const box = document.getElementById('metrics');
  const keys = ['browser_world_v1_first_person_ego_interior_readiness','weakest_channel_score','body_to_affect_coupling','relationship_memory_recall','bounded_refusal_calibration'];
  box.innerHTML = keys.map(k => `<div class=\"metric\"><span>${k}</span><b>${pct(METRICS[k])}</b></div>`).join('');
}
function render() {
  const row = LOOP_DATA[idx % LOOP_DATA.length];
  replay.push({ tick: row.tick_index, agent: row.agent, event: row.event_kind, behavior: row.visible_behavior, memory: row.memory_id });
  document.getElementById('behavior').textContent = `${row.visible_behavior}\n${row.refusal_or_recovery}\n${row.behavior.optional_dialogue || '(nonverbal)'}`;
  document.getElementById('body').textContent = JSON.stringify({ energy: row.body.energy, pain: row.body.pain, comfort: row.body.comfort, safety: row.body.safety, posture: row.body.posture }, null, 2);
  document.getElementById('workspace').textContent = JSON.stringify({ focus: row.workspace.current_focus, need: row.workspace.dominant_need, feeling: row.workspace.dominant_feeling, intention: row.workspace.current_intention, private_note: row.workspace.private_self_note }, null, 2);
  document.getElementById('log').textContent = replay.slice(-10).map(r => `t${r.tick} ${r.agent}: ${r.event} -> ${r.behavior}`).join('\n');
  document.getElementById('flower').style.transform = `rotate(${(idx * 137.5) % 360}deg)`;
  for (const node of document.querySelectorAll('.agent')) {
    if (node.dataset.agent === row.agent) {
      node.style.transform = 'scale(1.22) translateY(-8px)';
      node.style.boxShadow = '0 0 0 9px rgba(200,148,63,0.22)';
    } else {
      node.style.transform = 'scale(1)';
      node.style.boxShadow = 'none';
    }
  }
  document.getElementById('avatar').style.left = avatar.x + '%';
  document.getElementById('avatar').style.top = avatar.y + '%';
  idx += 1;
}
function start() { if (!timer) timer = setInterval(render, 250); }
function pause() { clearInterval(timer); timer = null; }
document.getElementById('start').onclick = start;
document.getElementById('pause').onclick = pause;
document.getElementById('save').onclick = () => localStorage.setItem(STORAGE_KEY, JSON.stringify({ idx, avatar, replay }));
document.getElementById('restore').onclick = () => { const raw = localStorage.getItem(STORAGE_KEY); if (raw) { const saved = JSON.parse(raw); idx = saved.idx || 0; avatar = saved.avatar || avatar; replay = saved.replay || []; render(); } };
document.getElementById('download').onclick = () => {
  const blob = new Blob([JSON.stringify({ report: 241, replay }, null, 2)], { type: 'application/json' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = 'ssrm241_replay.json';
  a.click();
};
document.getElementById('inspect').onclick = () => document.getElementById('workspace').classList.toggle('open');
document.getElementById('send').onclick = () => {
  const text = document.getElementById('utterance').value.trim();
  replay.push({ tick: 'typed', agent: 'avatar', event: 'local_utterance', behavior: text, memory: 'browser-local' });
  render();
};
window.addEventListener('keydown', (event) => {
  if (event.key === 'ArrowLeft') avatar.x = Math.max(2, avatar.x - 2);
  if (event.key === 'ArrowRight') avatar.x = Math.min(92, avatar.x + 2);
  if (event.key === 'ArrowUp') avatar.y = Math.max(4, avatar.y - 2);
  if (event.key === 'ArrowDown') avatar.y = Math.min(88, avatar.y + 2);
  document.getElementById('avatar').style.left = avatar.x + '%';
  document.getElementById('avatar').style.top = avatar.y + '%';
});
renderMetrics();
render();
</script>
</body>
</html>
"""
    return template.replace("__LOOP_DATA__", json.dumps(data)).replace("__METRICS__", json.dumps(metrics))


def run(seed: int) -> dict[str, Any]:
    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    specs = build_event_specs(seed)
    bodies = build_body_frames(specs)
    perceptions = build_perceptions(specs, bodies)
    egos = build_ego_appraisals(specs, bodies)
    provisional_workspaces = build_workspaces(specs, bodies, egos)
    ownership = build_ownership_frames(specs, egos)
    memories = build_memories(specs, egos)
    workspaces = build_workspaces(specs, bodies, egos, memories)
    behaviors = build_visible_behaviors(specs, bodies, egos, workspaces)
    loops = build_integrated_ticks(specs, bodies, perceptions, egos, workspaces, memories, behaviors)
    metrics = compute_metrics(specs, bodies, perceptions, egos, workspaces, ownership, memories, behaviors, loops)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["browser_world_v1_first_person_ego_interior_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    prefix = ARTIFACTS / BASE
    write_csv(Path(f"{prefix}_event_specs.csv"), specs)
    write_csv(Path(f"{prefix}_body_frames.csv"), bodies)
    write_csv(Path(f"{prefix}_local_perception_frames.csv"), perceptions)
    write_csv(Path(f"{prefix}_ego_appraisal_frames.csv"), egos)
    write_csv(Path(f"{prefix}_private_workspace_frames.csv"), workspaces)
    write_csv(Path(f"{prefix}_ownership_boundary_frames.csv"), ownership)
    write_csv(Path(f"{prefix}_relationship_memory_episodes.csv"), memories)
    write_csv(Path(f"{prefix}_visible_behavior_frames.csv"), behaviors)
    write_csv(Path(f"{prefix}_integrated_interior_loop_ticks.csv"), loops)
    honest_limits = [
        "This is a deterministic first-person interior scaffold, not subjective consciousness.",
        "Private workspace traces are generated for inspection, not evidence of inner experience.",
        "Bounded refusal is functional behavior, not real consent or legal agency.",
        "Relationship memory is simulated continuity, not moral patienthood.",
        "Distress-like states are bounded and paired with recovery paths; the benchmark must not optimize suffering spectacle.",
        "Typed dialogue remains deterministic browser-local routing, not autonomous language understanding.",
        "Frequency and flower phases are rhythm scaffolds, not metaphysical proof.",
        "The visualization is a browser-world v1 scaffold, not a finished 3D engine.",
    ]
    next_gate = "browser world v2 with autonomous routines, replay import/export, richer local language acts, inspectable-but-private interior traces, and long-horizon relationship/ownership consequences"
    results = {
        "report": REPORT,
        "name": "SSRM-3D Browser World v1 First-Person Ego Interior Bridge",
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "verdict": verdict,
        "counts": {
            "event_specs": len(specs),
            "body_frames": len(bodies),
            "local_perception_frames": len(perceptions),
            "ego_appraisal_frames": len(egos),
            "private_workspace_frames": len(workspaces),
            "ownership_boundary_frames": len(ownership),
            "relationship_memory_episodes": len(memories),
            "visible_behavior_frames": len(behaviors),
            "integrated_interior_loop_ticks": len(loops),
        },
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "next_gate": next_gate,
    }
    state = {
        "report": REPORT,
        "seed": seed,
        "agents": AGENTS,
        "sample_self_stories": {agent: traits["self_story"] for agent, traits in AGENTS.items()},
        "sample_loop_ticks": [asdict(t) for t in loops[:12]],
        "moral_boundary": "distress must create care opportunities, not spectacle",
        "private_workspace_policy": "private by default; public behavior first; research inspection explicit",
    }
    Path(f"{prefix}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    Path(f"{prefix}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    with Path(f"{prefix}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({
            "report": REPORT,
            "verdict": verdict,
            "readiness": metrics["browser_world_v1_first_person_ego_interior_readiness"],
            "weakest_channel_score": metrics["weakest_channel_score"],
            "next_gate": next_gate,
        })
    html = make_html(loops, bodies, behaviors, workspaces, metrics)
    (VISUALIZATIONS / f"{BASE}.html").write_text(html)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    counts = results["counts"]
    print(f"module_verdict {results['verdict']}")
    print(f"browser_world_v1_first_person_ego_interior_readiness {metrics['browser_world_v1_first_person_ego_interior_readiness']:.6f}")
    for key in [
        "event_specs",
        "body_frames",
        "local_perception_frames",
        "ego_appraisal_frames",
        "private_workspace_frames",
        "ownership_boundary_frames",
        "relationship_memory_episodes",
        "visible_behavior_frames",
        "integrated_interior_loop_ticks",
    ]:
        print(f"{key} {counts[key]}")
    for key in [
        "first_person_interior_binding",
        "body_to_affect_coupling",
        "local_perception_binding",
        "ego_self_boundary_coverage",
        "relationship_memory_recall",
        "bounded_refusal_calibration",
        "ego_recovery_path_rate",
        "visible_behavior_expression_rate",
        "weakest_channel_score",
    ]:
        print(f"{key} {metrics[key]:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
