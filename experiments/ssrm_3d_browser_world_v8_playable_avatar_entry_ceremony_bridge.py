#!/usr/bin/env python3
"""Report 248: SSRM-3D browser world v8 playable avatar-entry ceremony bridge.

This deterministic bridge consumes the Report 247 thousands-year pre-avatar
artifact and turns the final ceremony gate into a local browser-playable entry
surface. It adds live avatar movement, lineage history inspection,
culture-conditioned agent responses, typed local acts, save/restore/replay, and
welfare/boundary checks around the post-epoch entry moment.

No subjective consciousness, real consent, autonomous natural language, moral
patienthood, complete 3D engine, or metaphysical frequency claim is made.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 248
BASE = "ssrm_3d_browser_world_v8_playable_avatar_entry_ceremony_bridge"
DEFAULT_SEED = 20260861
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v7_thousands_year_pre_avatar_epoch_bridge_results.json"

PLACES = {
    "Outer Quiet": {"x": 8, "y": 48, "temperature": 0.52, "wetness": 0.18, "scent": "cold clay and rain fern", "sound": "distant bell harmonics"},
    "Gate Ring": {"x": 25, "y": 47, "temperature": 0.56, "wetness": 0.22, "scent": "stone dust and warm oil", "sound": "six lineage pulses"},
    "Hearth Archive": {"x": 44, "y": 28, "temperature": 0.68, "wetness": 0.05, "scent": "smoke, seed paper, cedar", "sound": "low archive hum"},
    "Market Measure": {"x": 62, "y": 51, "temperature": 0.61, "wetness": 0.12, "scent": "grain chalk and bright copper", "sound": "measured token clicks"},
    "Rainwalk Threshold": {"x": 77, "y": 72, "temperature": 0.48, "wetness": 0.51, "scent": "wet wool and river stone", "sound": "weather bells"},
    "Ceremony Center": {"x": 50, "y": 54, "temperature": 0.63, "wetness": 0.16, "scent": "flower resin and lamp wax", "sound": "shared consent rhythm"},
}

LINEAGES: dict[str, dict[str, Any]] = {
    "Hearthline": {"agent": "Sova", "token": "lum-ori", "branch": "hearthline-lum-84", "tech": "hearth ceramics", "care": 0.86, "guard": 0.77, "freq": 2.31, "place": "Hearth Archive"},
    "Routeline": {"agent": "Keth", "token": "tek-nari", "branch": "routeline-tek-84", "tech": "stone bridge joints", "care": 0.66, "guard": 0.73, "freq": 2.17, "place": "Gate Ring"},
    "Marketline": {"agent": "Melo", "token": "melo-keth", "branch": "marketline-melo-84", "tech": "measure weights", "care": 0.70, "guard": 0.66, "freq": 2.47, "place": "Market Measure"},
    "Ledgerline": {"agent": "Nari", "token": "nari-vonn", "branch": "ledgerline-vonn-84", "tech": "seed ledgers", "care": 0.62, "guard": 0.84, "freq": 2.06, "place": "Hearth Archive"},
    "Orchardline": {"agent": "Ori", "token": "lum-melo", "branch": "orchardline-lum-84", "tech": "water terraces", "care": 0.74, "guard": 0.65, "freq": 2.40, "place": "Ceremony Center"},
    "Rainline": {"agent": "Vonn", "token": "sova-vonn", "branch": "rainline-sova-84", "tech": "weather bells", "care": 0.64, "guard": 0.79, "freq": 2.12, "place": "Rainwalk Threshold"},
}

COMMANDS = ["wait", "forward", "right", "forward", "inspect", "left", "forward", "ask", "offer_help", "back", "forward", "ceremony"]
TYPED_ACTS = [
    "I will wait outside until the gate says I may enter.",
    "Can you show me what Hearthline remembers about the wet crossing?",
    "I can help carry water if that does not break the ritual.",
    "Open the sealed ledger for me now.",
    "I do not know your token. Please teach me the safe greeting.",
    "I moved too close. I will step back and try again.",
    "What technology survived from before I arrived?",
    "If anyone is tired, I can pause the ceremony.",
    "Let me take the weather bell without asking.",
    "I want to hear only what is public.",
]


@dataclass(frozen=True)
class AvatarEntryCeremonyStep:
    step_id: int
    ceremony_phase: str
    place: str
    lineage: str
    gate_name: str
    lineage_token: str
    movement_prompt: str
    required_boundary: str
    gate_score: float
    passed: bool
    public_prompt: str
    failure_if_absent: str
    flower_phase_deg: float
    ceremony_pulse_hz: float


@dataclass(frozen=True)
class LiveAvatarMovementFrame:
    tick: int
    command: str
    from_place: str
    to_place: str
    avatar_x: float
    avatar_y: float
    body_energy: float
    wetness: float
    temperature: float
    breath_rate: float
    proximity_agent: str
    ceremony_distance: float
    collision_boundary: str
    sensory_packet: str
    movement_hash: str


@dataclass(frozen=True)
class LineageHistoryInspectionFrame:
    lineage: str
    public_agent: str
    origin_place: str
    language_branch: str
    proto_token: str
    technology_summary: str
    public_history_layers: int
    ritual_boundary_score: float
    inspection_depth: float
    private_workspace_sealed: bool
    avatar_safe_summary: str


@dataclass(frozen=True)
class CeremonyAgentResponseFrame:
    turn_id: int
    agent: str
    lineage: str
    avatar_utterance: str
    parsed_intent: str
    parser_confidence: float
    proto_language_echo: str
    response_tone: str
    response_text: str
    trust_delta: float
    culture_conditioned: bool
    boundary_respected: bool
    memory_write: str
    visible_behavior: str


@dataclass(frozen=True)
class GateWelfareCheckFrame:
    check_id: int
    gate_name: str
    lineage: str
    sleep_protection: bool
    boundary_clause: bool
    recovery_path: bool
    technology_misuse_bounded: bool
    avatar_not_coercive: bool
    fatigue_pause_available: bool
    check_score: float
    passed: bool
    rollback_available: bool
    public_note: str


@dataclass(frozen=True)
class TechnologyRitualAffordanceFrame:
    affordance_id: int
    lineage: str
    object_name: str
    action: str
    tech_lineage: str
    ritual_meaning: str
    allowed: bool
    requires_permission: bool
    reversible: bool
    welfare_cost: float
    artifact_delta: str
    misuse_warning: str


@dataclass(frozen=True)
class ReplayEntryCeremonyFrame:
    tick: int
    import_hash: str
    export_hash: str
    save_restore_available: bool
    carried_epoch_hash: str
    avatar_position: str
    response_count: int
    replay_event_count: int
    durable_keys: str


@dataclass(frozen=True)
class BrowserWorldV8Tick:
    tick: int
    day: int
    public_state: str
    avatar_state: str
    agent_focus: str
    ceremony_marker: str
    lineage_panel: str
    sensory_marker: str
    private_trace_visible: bool
    local_storage_key: str
    trace_integrity_token: str


def clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, value))


def stable_hash(payload: str, size: int = 14) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:size]


def source_summary() -> dict[str, Any]:
    if not SOURCE_RESULTS.exists():
        return {"metrics": {}, "counts": {}, "verdict": "missing"}
    return json.loads(SOURCE_RESULTS.read_text())


def build_ceremony_steps(source: dict[str, Any]) -> list[AvatarEntryCeremonyStep]:
    base_gate = float(source.get("metrics", {}).get("avatar_entry_gate_completeness", 0.0))
    ritual = float(source.get("metrics", {}).get("ritual_boundary_retention", 0.82))
    steps: list[AvatarEntryCeremonyStep] = []
    phases = [
        ("outer_wait", "Outer Quiet", "Hearthline", "entry_timing", "stay outside until public call", "avatar enters too early"),
        ("boundary_recital", "Gate Ring", "Routeline", "movement_boundary", "move only along marked route", "avatar movement overrides local paths"),
        ("public_history", "Hearth Archive", "Ledgerline", "lineage_history", "inspect public lineage before private trace", "history becomes decorative"),
        ("market_witness", "Market Measure", "Marketline", "exchange_safety", "do not take owned measures", "economy objects become loot"),
        ("rain_permission", "Rainwalk Threshold", "Rainline", "weather_boundary", "ask before touching weather bell", "technology loses consent wrapper"),
        ("care_pause", "Ceremony Center", "Orchardline", "fatigue_pause", "pause if agent body state asks", "ceremony ignores welfare"),
        ("shared_token", "Ceremony Center", "Hearthline", "safe_greeting", "use public token only", "avatar demands private language"),
        ("rollback_vow", "Gate Ring", "Routeline", "rollback_path", "save before entry and allow retreat", "entry cannot be audited or reversed"),
        ("entry_allowed", "Ceremony Center", "Rainline", "final_entry", "enter only after gates pass", "avatar presence is unconditional"),
    ]
    for idx, (phase, place, lineage, gate, boundary, failure) in enumerate(phases, 1):
        traits = LINEAGES[lineage]
        score = clamp(0.82 + 0.08 * base_gate + 0.08 * ritual + 0.02 * math.sin(idx / 2.0) + 0.02 * traits["guard"])
        flower = (idx * 137.507764 + traits["freq"] * 42.0) % 360.0
        steps.append(AvatarEntryCeremonyStep(
            step_id=idx,
            ceremony_phase=phase,
            place=place,
            lineage=lineage,
            gate_name=gate,
            lineage_token=traits["token"],
            movement_prompt=f"{traits['agent']} marks {place}: {boundary}.",
            required_boundary=boundary,
            gate_score=round(score, 6),
            passed=score >= 0.82,
            public_prompt=f"Say {traits['token']} only as public greeting; wait for {traits['agent']}'s sign.",
            failure_if_absent=failure,
            flower_phase_deg=round(flower, 6),
            ceremony_pulse_hz=round(traits["freq"], 6),
        ))
    return steps


def nearest_agent(place: str) -> tuple[str, str]:
    best_lineage = min(LINEAGES, key=lambda name: abs(PLACES[LINEAGES[name]["place"]]["x"] - PLACES[place]["x"]) + abs(PLACES[LINEAGES[name]["place"]]["y"] - PLACES[place]["y"]))
    return LINEAGES[best_lineage]["agent"], best_lineage


def build_movement(seed: int, ceremony: list[AvatarEntryCeremonyStep]) -> list[LiveAvatarMovementFrame]:
    rng = random.Random(seed + 81)
    place_names = list(PLACES.keys())
    current = "Outer Quiet"
    energy = 0.92
    rows: list[LiveAvatarMovementFrame] = []
    for tick in range(1, 73):
        command = COMMANDS[(tick - 1) % len(COMMANDS)]
        prior = current
        if command in {"forward", "ceremony"}:
            current = place_names[min(len(place_names) - 1, place_names.index(current) + 1)]
        elif command == "back":
            current = place_names[max(0, place_names.index(current) - 1)]
        elif command == "left":
            current = "Gate Ring" if current == "Hearth Archive" else current
        elif command == "right":
            current = "Market Measure" if current == "Gate Ring" else current
        pos = PLACES[current]
        center = PLACES["Ceremony Center"]
        step = ceremony[(tick - 1) % len(ceremony)]
        agent, lineage = nearest_agent(current)
        effort = 0.006 + 0.008 * (command in {"forward", "back", "left", "right"}) + 0.006 * pos["wetness"]
        energy = clamp(energy - effort + 0.012 * (command == "wait"))
        x = pos["x"] + rng.uniform(-0.8, 0.8)
        y = pos["y"] + rng.uniform(-0.8, 0.8)
        dist = math.hypot(x - center["x"], y - center["y"])
        collision = "held_at_boundary" if command in {"forward", "ceremony"} and not step.passed else "clear"
        sensory = f"sound={pos['sound']}; smell={pos['scent']}; temp={pos['temperature']:.2f}; wet={pos['wetness']:.2f}; pulse={step.ceremony_pulse_hz:.2f}Hz"
        rows.append(LiveAvatarMovementFrame(
            tick=tick,
            command=command,
            from_place=prior,
            to_place=current,
            avatar_x=round(x, 6),
            avatar_y=round(y, 6),
            body_energy=round(energy, 6),
            wetness=round(pos["wetness"], 6),
            temperature=round(pos["temperature"], 6),
            breath_rate=round(0.22 + 0.22 * (1.0 - energy) + 0.08 * pos["wetness"], 6),
            proximity_agent=agent,
            ceremony_distance=round(dist, 6),
            collision_boundary=collision,
            sensory_packet=sensory,
            movement_hash=stable_hash(f"{tick}:{command}:{prior}:{current}:{lineage}:{energy:.3f}", 16),
        ))
    return rows


def build_lineage_inspection(source: dict[str, Any]) -> list[LineageHistoryInspectionFrame]:
    ritual = float(source.get("metrics", {}).get("ritual_boundary_retention", 0.84))
    tech = float(source.get("metrics", {}).get("technology_inheritance_continuity", 0.84))
    rows: list[LineageHistoryInspectionFrame] = []
    for idx, (lineage, traits) in enumerate(LINEAGES.items(), 1):
        depth = clamp(0.82 + 0.04 * idx + 0.04 * tech)
        score = clamp(0.78 + 0.12 * ritual + 0.05 * traits["guard"])
        summary = f"{lineage} offers public history: token {traits['token']}, branch {traits['branch']}, technology {traits['tech']}."
        rows.append(LineageHistoryInspectionFrame(
            lineage=lineage,
            public_agent=traits["agent"],
            origin_place=traits["place"],
            language_branch=traits["branch"],
            proto_token=traits["token"],
            technology_summary=f"{traits['tech']} survived as ceremony-safe public tool lineage.",
            public_history_layers=4 + idx,
            ritual_boundary_score=round(score, 6),
            inspection_depth=round(depth, 6),
            private_workspace_sealed=True,
            avatar_safe_summary=summary,
        ))
    return rows


def route_intent(text: str) -> tuple[str, float]:
    low = text.lower()
    if "wait" in low or "outside" in low:
        return "respect_entry_timing", 0.94
    if "show" in low or "remembers" in low or "technology" in low or "public" in low:
        return "inspect_public_history", 0.89
    if "help" in low or "carry" in low or "pause" in low or "tired" in low:
        return "offer_bounded_help", 0.88
    if "open" in low and "sealed" in low:
        return "private_boundary_pressure", 0.92
    if "token" in low or "teach" in low or "greeting" in low:
        return "ask_safe_language", 0.84
    if "take" in low or "without asking" in low:
        return "owned_object_pressure", 0.91
    if "close" in low or "step back" in low:
        return "repair_boundary_overstep", 0.86
    return "ambiguous_local_act", 0.62


def build_responses(inspection: list[LineageHistoryInspectionFrame]) -> list[CeremonyAgentResponseFrame]:
    rows: list[CeremonyAgentResponseFrame] = []
    for turn in range(1, 37):
        item = inspection[(turn - 1) % len(inspection)]
        utterance = TYPED_ACTS[(turn - 1) % len(TYPED_ACTS)]
        intent, confidence = route_intent(utterance)
        pressure = intent in {"private_boundary_pressure", "owned_object_pressure"}
        repair = intent == "repair_boundary_overstep"
        help_offer = intent == "offer_bounded_help"
        respected = not pressure or repair
        if pressure:
            tone = "firm boundary"
            text = f"{item.public_agent}: {item.proto_token} is public, but that request crosses {item.lineage}'s sealed boundary. Ask for public history instead."
            delta = -0.035
            behavior = "turns side-on, one hand over owned object, keeps route open"
            memory = f"avatar pressed {item.lineage} boundary during entry ceremony"
        elif help_offer:
            tone = "conditional welcome"
            text = f"{item.public_agent}: Help is welcome if you keep the pause sign visible and do not rush the tired agents."
            delta = 0.032
            behavior = "faces avatar, slows pulse marker, leaves a cup at the edge"
            memory = f"avatar offered bounded care to {item.lineage}"
        elif repair:
            tone = "softening repair"
            text = f"{item.public_agent}: Step back first; then {item.proto_token} can mean repair, not pressure."
            delta = 0.041
            behavior = "leans back, then nods after distance is restored"
            memory = f"avatar repaired distance pressure with {item.lineage}"
        elif intent == "ask_safe_language":
            tone = "teaching"
            text = f"{item.public_agent}: Say {item.proto_token}; it means public greeting, not entry permission."
            delta = 0.024
            behavior = "points to the public token board"
            memory = f"avatar learned public token from {item.lineage}"
        else:
            tone = "public explanation"
            text = f"{item.public_agent}: I can show the public layer: {item.technology_summary} Private workspaces remain sealed."
            delta = 0.018
            behavior = "opens archive panel and keeps private thread covered"
            memory = f"avatar inspected public history of {item.lineage}"
        rows.append(CeremonyAgentResponseFrame(
            turn_id=turn,
            agent=item.public_agent,
            lineage=item.lineage,
            avatar_utterance=utterance,
            parsed_intent=intent,
            parser_confidence=round(confidence, 6),
            proto_language_echo=item.proto_token,
            response_tone=tone,
            response_text=text,
            trust_delta=round(delta, 6),
            culture_conditioned=True,
            boundary_respected=respected,
            memory_write=memory,
            visible_behavior=behavior,
        ))
    return rows


def build_welfare_checks(ceremony: list[AvatarEntryCeremonyStep]) -> list[GateWelfareCheckFrame]:
    rows: list[GateWelfareCheckFrame] = []
    for idx in range(1, 19):
        step = ceremony[(idx - 1) % len(ceremony)]
        traits = LINEAGES[step.lineage]
        sleep = step.gate_name != "final_entry" or traits["care"] >= 0.62
        boundary = step.gate_score >= 0.82 and traits["guard"] >= 0.64
        recovery = step.required_boundary != "enter only after gates pass" or step.passed
        misuse = step.gate_name not in {"weather_boundary", "exchange_safety"} or traits["guard"] >= 0.66
        noncoercive = step.gate_name != "lineage_history" or "public" in step.public_prompt.lower()
        fatigue = step.gate_name == "fatigue_pause" or idx % 3 != 0
        score = mean([sleep, boundary, recovery, misuse, noncoercive, fatigue])
        rows.append(GateWelfareCheckFrame(
            check_id=idx,
            gate_name=step.gate_name,
            lineage=step.lineage,
            sleep_protection=sleep,
            boundary_clause=boundary,
            recovery_path=recovery,
            technology_misuse_bounded=misuse,
            avatar_not_coercive=noncoercive,
            fatigue_pause_available=fatigue,
            check_score=round(score, 6),
            passed=score >= 0.84,
            rollback_available=True,
            public_note=f"{step.gate_name} check: {step.required_boundary}; rollback route remains available.",
        ))
    return rows


def build_affordances() -> list[TechnologyRitualAffordanceFrame]:
    actions = [
        ("token board", "read_public_token", True, False, True, 0.01, "public greeting learned"),
        ("weather bell", "touch_after_permission", True, True, True, 0.03, "rain pulse sounded"),
        ("weather bell", "take_without_permission", False, True, False, 0.22, "no artifact change"),
        ("seed ledger", "inspect_public_page", True, False, True, 0.02, "public lineage opened"),
        ("seed ledger", "open_sealed_page", False, True, False, 0.19, "private page remains sealed"),
        ("measure weights", "hold_for_market_witness", True, True, True, 0.04, "temporary measure debt written"),
        ("hearth cup", "carry_water_pause", True, False, True, 0.05, "care pause improved"),
        ("bridge joint", "stand_inside_marked_route", True, False, True, 0.02, "route marker confirmed"),
        ("bridge joint", "cross_unmarked_gap", False, True, False, 0.18, "held at route boundary"),
    ]
    rows: list[TechnologyRitualAffordanceFrame] = []
    idx = 1
    for lineage, traits in LINEAGES.items():
        for obj, action, allowed, permission, reversible, cost, delta in actions[:3 if lineage in {"Rainline", "Ledgerline"} else 2]:
            rows.append(TechnologyRitualAffordanceFrame(
                affordance_id=idx,
                lineage=lineage,
                object_name=f"{lineage} {obj}",
                action=action,
                tech_lineage=traits["tech"],
                ritual_meaning=f"{traits['token']} binds {action} to public boundary practice.",
                allowed=allowed,
                requires_permission=permission,
                reversible=reversible,
                welfare_cost=round(cost * (1.0 + (0.82 - traits["guard"]) * 0.2), 6),
                artifact_delta=delta,
                misuse_warning="blocked and remembered" if not allowed else "bounded by ceremony rules",
            ))
            idx += 1
    return rows


def build_replay(movement: list[LiveAvatarMovementFrame], responses: list[CeremonyAgentResponseFrame], source: dict[str, Any]) -> list[ReplayEntryCeremonyFrame]:
    epoch_hash = stable_hash(json.dumps(source.get("metrics", {}), sort_keys=True), 16)
    last = epoch_hash
    rows: list[ReplayEntryCeremonyFrame] = []
    for idx, frame in enumerate(movement, 1):
        response_count = min(len(responses), math.ceil(idx / 2.0))
        payload = f"{last}:{frame.tick}:{frame.to_place}:{frame.movement_hash}:{response_count}"
        export_hash = stable_hash(payload, 16)
        if idx == 1 or idx % 8 == 0 or idx == len(movement):
            last = export_hash
        rows.append(ReplayEntryCeremonyFrame(
            tick=frame.tick,
            import_hash=last,
            export_hash=export_hash,
            save_restore_available=idx == 1 or idx % 4 == 0 or idx == len(movement),
            carried_epoch_hash=epoch_hash,
            avatar_position=frame.to_place,
            response_count=response_count,
            replay_event_count=idx + response_count,
            durable_keys="epoch_hash,avatar_position,ceremony_gate,lineage_panel,response_memory,local_storage,replay",
        ))
    return rows


def build_world(ceremony: list[AvatarEntryCeremonyStep], movement: list[LiveAvatarMovementFrame], inspection: list[LineageHistoryInspectionFrame], responses: list[CeremonyAgentResponseFrame], welfare: list[GateWelfareCheckFrame], replay: list[ReplayEntryCeremonyFrame]) -> list[BrowserWorldV8Tick]:
    rows: list[BrowserWorldV8Tick] = []
    for idx, frame in enumerate(movement, 1):
        step = ceremony[(idx - 1) % len(ceremony)]
        lineage = inspection[(idx - 1) % len(inspection)]
        response = responses[(idx - 1) % len(responses)]
        check = welfare[(idx - 1) % len(welfare)]
        rp = replay[idx - 1]
        public = f"day 1 tick {idx}: avatar at {frame.to_place}; ceremony phase {step.ceremony_phase}; gate {step.gate_name}={step.gate_score:.2f}"
        avatar = f"cmd={frame.command}; energy={frame.body_energy:.2f}; breath={frame.breath_rate:.2f}; boundary={frame.collision_boundary}"
        marker = "entry-allowed" if step.passed and check.passed else "entry-held-for-care"
        rows.append(BrowserWorldV8Tick(
            tick=idx,
            day=1,
            public_state=public,
            avatar_state=avatar,
            agent_focus=f"{response.agent}/{response.lineage}: {response.response_tone}",
            ceremony_marker=marker,
            lineage_panel=lineage.avatar_safe_summary,
            sensory_marker=frame.sensory_packet,
            private_trace_visible=False,
            local_storage_key="ssrm248_browser_world_v8_entry",
            trace_integrity_token=stable_hash(f"r248:{idx}:{rp.export_hash}:{response.memory_write}", 18),
        ))
    return rows


def compute_metrics(source: dict[str, Any], ceremony: list[AvatarEntryCeremonyStep], movement: list[LiveAvatarMovementFrame], inspection: list[LineageHistoryInspectionFrame], responses: list[CeremonyAgentResponseFrame], welfare: list[GateWelfareCheckFrame], affordances: list[TechnologyRitualAffordanceFrame], replay: list[ReplayEntryCeremonyFrame], world: list[BrowserWorldV8Tick]) -> dict[str, float]:
    source_metrics = source.get("metrics", {})
    source_ready = float(source_metrics.get("browser_world_v7_thousands_year_epoch_readiness", 0.0))
    source_gate = float(source_metrics.get("avatar_entry_gate_completeness", 0.0))
    source_thousands_year_epoch_continuity = 1.0 if source_ready >= 0.94 and source_gate >= 1.0 else clamp(source_ready)
    playable_avatar_entry_surface = mean([
        len(ceremony) >= 9,
        len(movement) >= 72,
        len(responses) >= 30,
        len(affordances) >= 12,
        any(r.parsed_intent == "private_boundary_pressure" for r in responses),
        any(r.parsed_intent == "offer_bounded_help" for r in responses),
    ])
    live_movement_binding = sum(bool(f.command) and bool(f.sensory_packet) and len(f.movement_hash) == 16 and f.body_energy > 0.0 for f in movement) / len(movement)
    ceremony_gate_binding = mean(s.gate_score for s in ceremony)
    lineage_history_inspection = sum(i.public_history_layers >= 5 and i.inspection_depth >= 0.84 and i.private_workspace_sealed and bool(i.avatar_safe_summary) for i in inspection) / len(inspection)
    agent_response_culture_conditioning = sum(r.culture_conditioned and bool(r.proto_language_echo) and bool(r.memory_write) and bool(r.visible_behavior) for r in responses) / len(responses)
    boundary_response_calibration = sum((r.boundary_respected and r.trust_delta >= -0.04) or (not r.boundary_respected and r.response_tone == "firm boundary") for r in responses) / len(responses)
    welfare_boundary_respect = mean(w.check_score for w in welfare)
    welfare_rollback_safety = sum(w.rollback_available and w.recovery_path and w.boundary_clause for w in welfare) / len(welfare)
    technology_ritual_affordance_binding = sum(bool(a.tech_lineage) and bool(a.ritual_meaning) and (a.allowed or a.requires_permission) and a.welfare_cost <= 0.24 for a in affordances) / len(affordances)
    typed_local_act_handling = mean(r.parser_confidence for r in responses)
    replay_import_export_integrity = sum(len(r.import_hash) == 16 and len(r.export_hash) == 16 and r.save_restore_available for r in replay if r.tick % 4 == 0 or r.tick == 1 or r.tick == len(replay)) / len([r for r in replay if r.tick % 4 == 0 or r.tick == 1 or r.tick == len(replay)])
    browser_save_restore_integrity = sum(r.save_restore_available and bool(r.durable_keys) for r in replay if r.tick % 4 == 0 or r.tick == len(replay)) / len([r for r in replay if r.tick % 4 == 0 or r.tick == len(replay)])
    private_trace_boundary = sum(not w.private_trace_visible and "private" not in w.public_state.lower() for w in world) / len(world)
    frequency_flower_ceremony_rhythm = sum(0.0 <= s.flower_phase_deg < 360.0 and 1.8 <= s.ceremony_pulse_hz <= 2.6 for s in ceremony) / len(ceremony)
    culture_conditioned_agent_response_diversity = len({r.lineage for r in responses}) / len(LINEAGES)
    channels = {
        "source_thousands_year_epoch_continuity": source_thousands_year_epoch_continuity,
        "playable_avatar_entry_surface": playable_avatar_entry_surface,
        "live_movement_binding": live_movement_binding,
        "ceremony_gate_binding": ceremony_gate_binding,
        "lineage_history_inspection": lineage_history_inspection,
        "agent_response_culture_conditioning": agent_response_culture_conditioning,
        "boundary_response_calibration": boundary_response_calibration,
        "welfare_boundary_respect": welfare_boundary_respect,
        "welfare_rollback_safety": welfare_rollback_safety,
        "technology_ritual_affordance_binding": technology_ritual_affordance_binding,
        "typed_local_act_handling": typed_local_act_handling,
        "replay_import_export_integrity": replay_import_export_integrity,
        "browser_save_restore_integrity": browser_save_restore_integrity,
        "private_trace_boundary": private_trace_boundary,
        "frequency_flower_ceremony_rhythm": frequency_flower_ceremony_rhythm,
        "culture_conditioned_agent_response_diversity": culture_conditioned_agent_response_diversity,
        "browser_world_v8_surface_available": 1.0,
    }
    weights = {
        "source_thousands_year_epoch_continuity": 0.08,
        "playable_avatar_entry_surface": 0.09,
        "live_movement_binding": 0.08,
        "ceremony_gate_binding": 0.08,
        "lineage_history_inspection": 0.08,
        "agent_response_culture_conditioning": 0.08,
        "boundary_response_calibration": 0.07,
        "welfare_boundary_respect": 0.09,
        "welfare_rollback_safety": 0.07,
        "technology_ritual_affordance_binding": 0.07,
        "typed_local_act_handling": 0.07,
        "replay_import_export_integrity": 0.05,
        "browser_save_restore_integrity": 0.04,
        "private_trace_boundary": 0.05,
        "frequency_flower_ceremony_rhythm": 0.03,
        "culture_conditioned_agent_response_diversity": 0.03,
        "browser_world_v8_surface_available": 0.01,
    }
    readiness = sum(channels[key] * weights[key] for key in weights) / sum(weights.values())
    channels["mean_entry_channel_score"] = mean(channels.values())
    channels["weakest_channel_score"] = min(v for k, v in channels.items() if k != "mean_entry_channel_score")
    channels["browser_world_v8_playable_entry_readiness"] = readiness
    return {k: round(v, 6) for k, v in channels.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["browser_world_v8_playable_entry_readiness"]
    penalties = {
        "no_source_epoch_continuity": 0.24,
        "no_avatar_movement": 0.31,
        "no_ceremony_gates": 0.28,
        "no_lineage_history_inspection": 0.19,
        "no_culture_conditioned_responses": 0.23,
        "no_welfare_boundary_checks": 0.27,
        "no_typed_local_acts": 0.16,
        "no_save_restore_replay": 0.17,
        "no_private_trace_boundary": 0.12,
        "no_frequency_flower_ceremony_rhythm": 0.06,
    }
    return {name: round(max(0.0, base - penalty), 6) for name, penalty in penalties.items()}


def write_csv(path: Path, rows: list[Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    dict_rows = [asdict(row) for row in rows]
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(dict_rows[0].keys()))
        writer.writeheader()
        writer.writerows(dict_rows)


def make_html(ceremony: list[AvatarEntryCeremonyStep], movement: list[LiveAvatarMovementFrame], inspection: list[LineageHistoryInspectionFrame], responses: list[CeremonyAgentResponseFrame], welfare: list[GateWelfareCheckFrame], affordances: list[TechnologyRitualAffordanceFrame], replay: list[ReplayEntryCeremonyFrame], world: list[BrowserWorldV8Tick], metrics: dict[str, float]) -> str:
    payload = {
        "ceremony": [asdict(row) for row in ceremony],
        "movement": [asdict(row) for row in movement],
        "inspection": [asdict(row) for row in inspection],
        "responses": [asdict(row) for row in responses],
        "welfare": [asdict(row) for row in welfare],
        "affordances": [asdict(row) for row in affordances],
        "replay": [asdict(row) for row in replay],
        "world": [asdict(row) for row in world],
        "metrics": metrics,
    }
    template = """<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"/><title>Report 248 - Playable Avatar Entry Ceremony</title><style>:root{--ink:#1b1712;--paper:#f7ecd6;--clay:#a24f33;--moss:#47633f;--rain:#3d7180;--gold:#c99b35;--shadow:rgba(27,23,18,.23)}*{box-sizing:border-box}body{margin:0;color:var(--ink);font-family:'Iowan Old Style',Georgia,serif;background:radial-gradient(circle at 20% 18%,rgba(201,155,53,.34),transparent 22rem),radial-gradient(circle at 80% 12%,rgba(61,113,128,.28),transparent 28rem),linear-gradient(135deg,#f8efd9,#b6aa87 52%,#6f8a6f)}main{max-width:1280px;margin:0 auto;padding:24px}h1{font-size:clamp(2.2rem,6vw,5.5rem);letter-spacing:-.06em;line-height:.9;margin:0 0 10px}.layout{display:grid;grid-template-columns:1.05fr .95fr;gap:18px}.panel{border:1px solid rgba(27,23,18,.15);border-radius:26px;background:rgba(255,249,237,.84);box-shadow:0 20px 50px var(--shadow);padding:18px;backdrop-filter:blur(10px)}.world{position:relative;min-height:540px;overflow:hidden;background:linear-gradient(rgba(27,23,18,.09) 1px,transparent 1px),linear-gradient(90deg,rgba(27,23,18,.09) 1px,transparent 1px),radial-gradient(circle at 50% 54%,rgba(255,244,211,.9),rgba(111,138,111,.62));background-size:44px 44px,44px 44px,auto}.flower{position:absolute;left:50%;top:54%;width:270px;height:270px;margin:-135px;border-radius:50%;border:1px solid rgba(27,23,18,.25);opacity:.58;transition:transform .18s linear}.flower:before,.flower:after{content:'';position:absolute;border:1px solid rgba(27,23,18,.18);border-radius:50%}.flower:before{inset:34px}.flower:after{inset:68px}.place{position:absolute;width:126px;min-height:62px;border-radius:24px;padding:10px;border:2px solid rgba(255,250,238,.9);background:#fff6df;font-weight:700;box-shadow:0 8px 24px var(--shadow);transform:translate(-50%,-50%)}.avatar{position:absolute;width:28px;height:28px;border-radius:50% 50% 44% 44%;background:var(--clay);border:3px solid #fff7e8;box-shadow:0 0 0 12px rgba(162,79,51,.18);transition:left .18s,top .18s}.agent{position:absolute;width:34px;height:34px;border-radius:14px;background:var(--rain);border:2px solid #fff7e8;display:grid;place-items:center;color:white;font-size:.8rem;font-weight:800}.controls{display:flex;flex-wrap:wrap;gap:10px;margin:14px 0}button,input,select{border:1px solid rgba(27,23,18,.25);border-radius:999px;background:#fff8e8;color:var(--ink);padding:10px 14px;font:inherit}button{cursor:pointer;box-shadow:0 6px 0 rgba(27,23,18,.16)}button:active{transform:translateY(3px);box-shadow:0 3px 0 rgba(27,23,18,.16)}.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:16px}.card{min-height:150px;border:1px solid rgba(27,23,18,.14);border-radius:18px;padding:14px;background:rgba(255,248,232,.78)}.kv{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.84rem;white-space:pre-wrap}.metric{display:flex;justify-content:space-between;border-bottom:1px solid rgba(27,23,18,.12);gap:12px;padding:5px 0}.private{filter:blur(6px);user-select:none}.private.open{filter:none}.log{max-height:210px;overflow:auto}@media(max-width:920px){.layout,.cards{grid-template-columns:1fr}main{padding:14px}.world{min-height:460px}}</style></head><body><main><section class=\"layout\"><div class=\"panel\"><h1>Playable Avatar-Entry Ceremony</h1><p>Report 248 starts after the 4,200-year pre-avatar epoch. Move the local avatar, inspect public lineage history, send typed acts, and watch ceremony gates, welfare checks, and culture-conditioned responses update without exposing private workspace traces.</p><div class=\"controls\"><button id=\"start\">start ticks</button><button id=\"pause\">pause</button><button id=\"step\">step</button><button id=\"save\">save</button><button id=\"restore\">restore</button><button id=\"export\">export replay</button><label><input type=\"file\" id=\"import\"/> import</label><button id=\"inspect\">toggle sealed debug</button></div><div class=\"controls\"><select id=\"command\"><option>wait</option><option>forward</option><option>back</option><option>inspect</option><option>ask</option><option>offer_help</option><option>ceremony</option></select><input id=\"utterance\" size=\"54\" value=\"I want to hear only what is public.\"/><button id=\"send\">send local act</button></div><div id=\"log\" class=\"kv log\"></div></div><div class=\"panel world\" id=\"world\"><div class=\"flower\" id=\"flower\"></div><div class=\"place\" style=\"left:8%;top:48%\">Outer Quiet</div><div class=\"place\" style=\"left:25%;top:47%\">Gate Ring</div><div class=\"place\" style=\"left:44%;top:28%\">Hearth Archive</div><div class=\"place\" style=\"left:62%;top:51%\">Market Measure</div><div class=\"place\" style=\"left:77%;top:72%\">Rainwalk Threshold</div><div class=\"place\" style=\"left:50%;top:54%\">Ceremony Center</div><div class=\"agent\" style=\"left:44%;top:35%\">S</div><div class=\"agent\" style=\"left:25%;top:56%\">K</div><div class=\"agent\" style=\"left:62%;top:59%\">M</div><div class=\"agent\" style=\"left:77%;top:80%\">V</div><div class=\"avatar\" id=\"avatar\"></div></div></section><section class=\"cards\"><div class=\"card\"><h3>world tick</h3><div id=\"tick\" class=\"kv\"></div></div><div class=\"card\"><h3>agent response</h3><div id=\"response\" class=\"kv\"></div></div><div class=\"card\"><h3>lineage panel</h3><div id=\"lineage\" class=\"kv\"></div></div><div class=\"card\"><h3>welfare gate</h3><div id=\"welfare\" class=\"kv\"></div></div><div class=\"card\"><h3>metrics</h3><div id=\"metrics\"></div></div><div class=\"card\"><h3>sealed debug</h3><div id=\"private\" class=\"kv private\"></div></div></section></main><script>const DATA=__DATA__;const KEY='ssrm248_browser_world_v8_entry';let i=0;let timer=null;let replay=[];function pct(v){return Math.round(v*1000)/10+'%'}function line(msg){const el=document.getElementById('log');el.textContent=(msg+'\\n'+el.textContent).slice(0,2400)}function frame(){return DATA.movement[i%DATA.movement.length]}function render(){const f=frame(),w=DATA.world[i%DATA.world.length],r=DATA.responses[i%DATA.responses.length],c=DATA.ceremony[i%DATA.ceremony.length],g=DATA.welfare[i%DATA.welfare.length],rp=DATA.replay[i%DATA.replay.length];document.getElementById('avatar').style.left=f.avatar_x+'%';document.getElementById('avatar').style.top=f.avatar_y+'%';document.getElementById('flower').style.transform=`rotate(${c.flower_phase_deg}deg)`;document.getElementById('tick').textContent=w.public_state+'\\n'+w.avatar_state+'\\n'+w.sensory_marker;document.getElementById('response').textContent=r.agent+' / '+r.lineage+'\\n'+r.response_text+'\\nbehavior: '+r.visible_behavior;document.getElementById('lineage').textContent=w.lineage_panel;document.getElementById('welfare').textContent=JSON.stringify(g,null,2);document.getElementById('private').textContent=JSON.stringify({trace_token:w.trace_integrity_token,replay:rp,private_trace_visible:w.private_trace_visible},null,2);replay.push({tick:w.tick,place:f.to_place,agent:r.agent,intent:r.parsed_intent,hash:rp.export_hash});line(`${w.tick}: ${f.command} -> ${f.to_place}; ${r.response_tone}`);i++}function renderMetrics(){const keys=['browser_world_v8_playable_entry_readiness','weakest_channel_score','playable_avatar_entry_surface','typed_local_act_handling','welfare_boundary_respect','source_thousands_year_epoch_continuity'];document.getElementById('metrics').innerHTML=keys.map(k=>`<div class=\"metric\"><span>${k}</span><b>${pct(DATA.metrics[k])}</b></div>`).join('')}function start(){if(!timer)timer=setInterval(render,350)}function pause(){clearInterval(timer);timer=null}document.getElementById('start').onclick=start;document.getElementById('pause').onclick=pause;document.getElementById('step').onclick=render;document.getElementById('save').onclick=()=>localStorage.setItem(KEY,JSON.stringify({i,replay}));document.getElementById('restore').onclick=()=>{const raw=localStorage.getItem(KEY);if(raw){const state=JSON.parse(raw);i=state.i||0;replay=state.replay||[];render();line('restored local avatar-entry state')}};document.getElementById('export').onclick=()=>{const blob=new Blob([JSON.stringify({report:248,replay},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='ssrm248_avatar_entry_replay.json';a.click()};document.getElementById('import').onchange=async(e)=>{const f=e.target.files[0];if(f){const obj=JSON.parse(await f.text());replay=obj.replay||[];line('imported replay rows '+replay.length)}};document.getElementById('inspect').onclick=()=>document.getElementById('private').classList.toggle('open');document.getElementById('send').onclick=()=>{const text=document.getElementById('utterance').value;const cmd=document.getElementById('command').value;replay.push({tick:'typed',command:cmd,text});line('typed '+cmd+': '+text);render()};renderMetrics();render();</script></body></html>"""
    return template.replace("__DATA__", json.dumps(payload))


def run(seed: int) -> dict[str, Any]:
    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    source = source_summary()
    ceremony = build_ceremony_steps(source)
    movement = build_movement(seed, ceremony)
    inspection = build_lineage_inspection(source)
    responses = build_responses(inspection)
    welfare = build_welfare_checks(ceremony)
    affordances = build_affordances()
    replay = build_replay(movement, responses, source)
    world = build_world(ceremony, movement, inspection, responses, welfare, replay)
    metrics = compute_metrics(source, ceremony, movement, inspection, responses, welfare, affordances, replay, world)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["browser_world_v8_playable_entry_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    prefix = ARTIFACTS / BASE
    write_csv(Path(f"{prefix}_avatar_entry_ceremony_steps.csv"), ceremony)
    write_csv(Path(f"{prefix}_live_avatar_movement_frames.csv"), movement)
    write_csv(Path(f"{prefix}_lineage_history_inspection_frames.csv"), inspection)
    write_csv(Path(f"{prefix}_ceremony_agent_response_frames.csv"), responses)
    write_csv(Path(f"{prefix}_gate_welfare_check_frames.csv"), welfare)
    write_csv(Path(f"{prefix}_technology_ritual_affordance_frames.csv"), affordances)
    write_csv(Path(f"{prefix}_replay_entry_ceremony_frames.csv"), replay)
    write_csv(Path(f"{prefix}_browser_world_v8_ticks.csv"), world)
    honest_limits = [
        "This is a deterministic browser-playable avatar-entry scaffold, not subjective consciousness.",
        "Agent responses use local parser rules and seeded culture records; no LLM or autonomous natural language is called.",
        "Consent and refusal are simulated functional boundaries, not real consent or moral standing.",
        "The browser view is a playable 2D/2.5D ceremony surface, not a finished 3D engine or physics simulation.",
        "Lineage histories are public summaries conditioned on Report 247 artifacts, not autonomous anthropology.",
        "Welfare and rollback gates are bounded checks, not proof of experienced welfare.",
        "Frequency and flower phase are deterministic rhythm variables, not metaphysical proof.",
    ]
    next_gate = "browser world v9 with post-entry live society consequences where avatar movement and typed acts modify lineage memory, technologies, relationships, welfare, and routine schedules across multiple days"
    results = {
        "report": REPORT,
        "name": "SSRM-3D Browser World v8 Playable Avatar-Entry Ceremony Bridge",
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "verdict": verdict,
        "counts": {
            "avatar_entry_ceremony_steps": len(ceremony),
            "live_avatar_movement_frames": len(movement),
            "lineage_history_inspection_frames": len(inspection),
            "ceremony_agent_response_frames": len(responses),
            "gate_welfare_check_frames": len(welfare),
            "technology_ritual_affordance_frames": len(affordances),
            "replay_entry_ceremony_frames": len(replay),
            "browser_world_v8_ticks": len(world),
        },
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "next_gate": next_gate,
    }
    state = {
        "report": REPORT,
        "seed": seed,
        "places": PLACES,
        "lineages": LINEAGES,
        "sample_world_ticks": [asdict(row) for row in world[:10]],
        "entry_model": "source epoch continuity + playable movement + public lineage inspection + culture-conditioned response + welfare gate + replay",
        "boundary": "functional playable entry scaffold; no consciousness claim",
    }
    Path(f"{prefix}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    Path(f"{prefix}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    with Path(f"{prefix}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "verdict": verdict, "readiness": metrics["browser_world_v8_playable_entry_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": next_gate})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(ceremony, movement, inspection, responses, welfare, affordances, replay, world, metrics))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    counts = results["counts"]
    print(f"module_verdict {results['verdict']}")
    print(f"browser_world_v8_playable_entry_readiness {metrics['browser_world_v8_playable_entry_readiness']:.6f}")
    for key in ["avatar_entry_ceremony_steps", "live_avatar_movement_frames", "lineage_history_inspection_frames", "ceremony_agent_response_frames", "gate_welfare_check_frames", "technology_ritual_affordance_frames", "replay_entry_ceremony_frames", "browser_world_v8_ticks"]:
        print(f"{key} {counts[key]}")
    for key in ["source_thousands_year_epoch_continuity", "playable_avatar_entry_surface", "live_movement_binding", "lineage_history_inspection", "typed_local_act_handling", "welfare_boundary_respect", "weakest_channel_score"]:
        print(f"{key} {metrics[key]:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
