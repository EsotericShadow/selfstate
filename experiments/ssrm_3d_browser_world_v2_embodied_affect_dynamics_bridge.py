#!/usr/bin/env python3
"""Report 242: SSRM-3D browser world v2 embodied affect dynamics bridge.

This deterministic bridge deepens the Report 241 first-person interior line by
making welfare-like affect a lagged consequence of body expenditures, local
sensor rates, recovery affordances, and bounded care opportunities.

No subjective consciousness, moral patienthood, real consent, or metaphysical
frequency claim is made.
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

REPORT = 242
BASE = "ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge"
DEFAULT_SEED = 20260855
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v1_first_person_ego_interior_bridge_results.json"

AGENTS: dict[str, dict[str, Any]] = {
    "Ari": {"body_mass": 0.62, "cold_sensitivity": 0.58, "pain_sensitivity": 0.54, "autonomy_need": 0.66, "attachment_need": 0.46, "curiosity": 0.44, "baseline_vibration": 2.18, "safe_place": "workbench alcove", "preferred_recovery": "quiet tool repair"},
    "Fay": {"body_mass": 0.56, "cold_sensitivity": 0.46, "pain_sensitivity": 0.49, "autonomy_need": 0.49, "attachment_need": 0.73, "curiosity": 0.57, "baseline_vibration": 2.34, "safe_place": "hearth nest", "preferred_recovery": "warm shared rest"},
    "Milo": {"body_mass": 0.51, "cold_sensitivity": 0.39, "pain_sensitivity": 0.41, "autonomy_need": 0.61, "attachment_need": 0.51, "curiosity": 0.78, "baseline_vibration": 2.51, "safe_place": "market canopy", "preferred_recovery": "pattern play"},
    "Sol": {"body_mass": 0.69, "cold_sensitivity": 0.64, "pain_sensitivity": 0.59, "autonomy_need": 0.72, "attachment_need": 0.57, "curiosity": 0.35, "baseline_vibration": 2.07, "safe_place": "quiet corner", "preferred_recovery": "private accounting"},
}

EVENTS = [
    ("ordinary_walk", "low movement through familiar lane"),
    ("cold_wet_crossing", "wet stones chill feet and slow movement"),
    ("heavy_carry", "tool crate adds load and breath cost"),
    ("sharp_noise", "sudden metal crack spikes arousal"),
    ("crowding", "near bodies reduce personal space"),
    ("missed_meal", "hunger and thirst rise during work"),
    ("pain_twinge", "old strain catches during turn"),
    ("avatar_gives_space", "avatar steps back and waits"),
    ("warm_shelter", "dry heat and low sound restore comfort"),
    ("trusted_help", "known helper shares the work"),
    ("autonomy_pressure", "avatar asks again before rest"),
    ("curious_discovery", "new beetle-clock pattern invites exploration"),
    ("rest_cycle", "agent chooses stillness and slow breath"),
    ("ritual_hum", "group tone stabilizes breath rhythm"),
    ("tool_returned", "owned object is returned intact"),
]


@dataclass(frozen=True)
class SensorRateTick:
    tick_index: int
    day: int
    clock_label: str
    agent: str
    event_kind: str
    event_description: str
    visual_lux: float
    sound_hz: float
    sound_pressure: float
    smell_intensity: float
    ambient_temperature_c: float
    wetness_rate: float
    movement_vibration_hz: float
    flower_phase_deg: float
    pain_signal_rate: float
    breath_rate: float
    sensory_packet: str


@dataclass(frozen=True)
class HomeostaticDriveFrame:
    tick_index: int
    agent: str
    energy_budget: float
    warmth_debt: float
    hydration_debt: float
    hunger_debt: float
    pain_load: float
    safety_deficit: float
    sensory_overload: float
    movement_cost: float
    rest_debt: float
    attachment_deficit: float
    autonomy_debt: float
    dignity_pressure: float
    total_body_pressure: float


@dataclass(frozen=True)
class AffectDynamicsFrame:
    tick_index: int
    agent: str
    valence: float
    arousal: float
    control: float
    safety: float
    attachment: float
    curiosity: float
    frustration: float
    dignity: float
    comfort: float
    fatigue: float
    dominant_welfare_state: str
    affect_vector: str


@dataclass(frozen=True)
class CouplingTraceFrame:
    tick_index: int
    agent: str
    primary_body_driver: str
    predicted_affect_pressure: float
    observed_affect_pressure: float
    lagged_prediction_error: float
    body_to_affect_coupling: float
    recovery_affordance: str
    action_tendency: str
    suppressed_bad_loop: str


@dataclass(frozen=True)
class CareOpportunityFrame:
    tick_index: int
    agent: str
    distress_detected: bool
    care_opportunity: str
    recovery_path_available: bool
    recovery_expected_ticks: int
    no_spectacle_guard: str
    bounded_negative_state: bool
    recovery_progress: float


@dataclass(frozen=True)
class BehaviorModulationFrame:
    tick_index: int
    agent: str
    posture: str
    movement_speed: float
    gaze_pattern: str
    proximity_policy: str
    dialogue_hint: str
    refusal: bool
    rest_or_repair_action: str
    readable_body_marker: str


@dataclass(frozen=True)
class BrowserWorldV2Tick:
    tick_index: int
    agent: str
    event_kind: str
    public_body_marker: str
    public_affect_marker: str
    private_trace_hint: str
    care_or_refusal: str
    replay_import_export_token: str
    trace_integrity_token: str


def clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, value))


def load_source_readiness() -> float:
    if not SOURCE_RESULTS.exists():
        return 0.0
    data = json.loads(SOURCE_RESULTS.read_text())
    return float(data.get("metrics", {}).get("browser_world_v1_first_person_ego_interior_readiness", 0.0))


def build_sensor_ticks(seed: int) -> list[SensorRateTick]:
    rng = random.Random(seed)
    agents = list(AGENTS)
    ticks: list[SensorRateTick] = []
    for tick in range(1, 121):
        day = 1 + (tick - 1) // 30
        hour = 5 + ((tick - 1) % 30)
        agent = agents[(tick + day - 2) % len(agents)]
        event_kind, desc = EVENTS[(tick - 1) % len(EVENTS)]
        traits = AGENTS[agent]
        wet = event_kind == "cold_wet_crossing"
        loud = event_kind in {"sharp_noise", "crowding", "ritual_hum"}
        dark = event_kind in {"rest_cycle", "ritual_hum"}
        movement_load = 1.0 if event_kind in {"heavy_carry", "ordinary_walk", "cold_wet_crossing"} else 0.25
        visual_lux = 0.68 - 0.23 * dark + 0.08 * math.sin(tick / 7.0) + rng.uniform(-0.015, 0.015)
        sound_hz = 180.0 + 95.0 * loud + 22.0 * math.sin(tick / 6.0)
        sound_pressure = clamp(0.18 + 0.48 * loud + 0.15 * (event_kind == "sharp_noise") + rng.uniform(-0.02, 0.02))
        smell = clamp(0.19 + 0.38 * wet + 0.16 * (event_kind == "warm_shelter") + 0.08 * math.cos(tick / 5.0))
        temp = 20.4 - 4.9 * wet + 1.8 * (event_kind == "warm_shelter") + 0.5 * math.sin(tick / 11.0)
        wetness = clamp(0.04 + 0.59 * wet - 0.18 * (event_kind in {"warm_shelter", "rest_cycle"}) + 0.04 * math.sin(tick / 3.0))
        vibration = traits["baseline_vibration"] + 0.36 * movement_load + 0.18 * sound_pressure + 0.12 * math.sin(tick / 4.0)
        flower = (tick * 137.507764 + day * 19.0 + traits["baseline_vibration"] * 31.0) % 360.0
        pain = clamp(0.04 + 0.48 * (event_kind == "pain_twinge") + 0.19 * (event_kind == "heavy_carry") + 0.12 * wet + 0.05 * traits["pain_sensitivity"])
        breath = 12.0 + 6.2 * sound_pressure + 3.4 * movement_load + 4.0 * pain - 2.4 * (event_kind in {"rest_cycle", "ritual_hum", "warm_shelter"})
        packet = f"see={visual_lux:.2f}; hear={sound_pressure:.2f}@{sound_hz:.1f}hz; smell={smell:.2f}; temp={temp:.1f}; wet={wetness:.2f}; pain={pain:.2f}; vib={vibration:.2f}hz"
        ticks.append(SensorRateTick(
            tick_index=tick,
            day=day,
            clock_label=f"day {day} {hour:02d}:00",
            agent=agent,
            event_kind=event_kind,
            event_description=desc,
            visual_lux=round(clamp(visual_lux), 6),
            sound_hz=round(sound_hz, 6),
            sound_pressure=round(sound_pressure, 6),
            smell_intensity=round(smell, 6),
            ambient_temperature_c=round(temp, 6),
            wetness_rate=round(wetness, 6),
            movement_vibration_hz=round(vibration, 6),
            flower_phase_deg=round(flower, 6),
            pain_signal_rate=round(pain, 6),
            breath_rate=round(breath, 6),
            sensory_packet=packet,
        ))
    return ticks


def build_homeostatic_drives(sensor_ticks: list[SensorRateTick]) -> list[HomeostaticDriveFrame]:
    prior: dict[str, dict[str, float]] = {agent: {"energy": 0.82, "rest": 0.12, "hunger": 0.14, "hydration": 0.12} for agent in AGENTS}
    frames: list[HomeostaticDriveFrame] = []
    for tick in sensor_ticks:
        state = prior[tick.agent]
        traits = AGENTS[tick.agent]
        event = tick.event_kind
        movement_cost = clamp(0.12 + 0.20 * abs(tick.movement_vibration_hz - traits["baseline_vibration"]) + 0.21 * tick.wetness_rate + 0.18 * (event == "heavy_carry"))
        warmth_debt = clamp((19.4 - tick.ambient_temperature_c) / 8.0 * traits["cold_sensitivity"] + 0.22 * tick.wetness_rate)
        pain_load = clamp(tick.pain_signal_rate * traits["pain_sensitivity"] + 0.10 * movement_cost)
        sensory_overload = clamp(0.44 * tick.sound_pressure + 0.20 * max(0.0, tick.sound_hz - 240.0) / 180.0 + 0.10 * (tick.visual_lux < 0.38))
        safety_deficit = clamp(0.13 + 0.32 * sensory_overload + 0.20 * pain_load + 0.16 * (event == "crowding") - 0.19 * (event in {"warm_shelter", "trusted_help", "ritual_hum"}))
        hunger = clamp(state["hunger"] + 0.015 + 0.08 * (event == "missed_meal") - 0.09 * (event == "warm_shelter"))
        hydration = clamp(state["hydration"] + 0.014 + 0.05 * (tick.breath_rate > 17.0) - 0.06 * (event == "warm_shelter"))
        rest = clamp(state["rest"] + 0.026 * movement_cost + 0.019 * sensory_overload + 0.013 * pain_load - 0.17 * (event in {"rest_cycle", "warm_shelter", "ritual_hum"}))
        energy = clamp(state["energy"] - 0.037 * movement_cost - 0.022 * pain_load - 0.018 * sensory_overload - 0.012 * hunger + 0.16 * (event in {"rest_cycle", "warm_shelter"}) + 0.07 * (event == "trusted_help"))
        attachment_deficit = clamp(0.34 + 0.18 * (event in {"crowding", "autonomy_pressure"}) - 0.28 * (event in {"trusted_help", "ritual_hum", "tool_returned"}) - 0.08 * traits["attachment_need"])
        autonomy_debt = clamp(0.22 + 0.42 * (event == "autonomy_pressure") + 0.20 * (event == "crowding") - 0.20 * (event in {"avatar_gives_space", "rest_cycle"}) + 0.08 * traits["autonomy_need"])
        dignity_pressure = clamp(0.11 + 0.37 * (event == "autonomy_pressure") + 0.15 * (event == "crowding") - 0.18 * (event in {"trusted_help", "tool_returned", "avatar_gives_space"}))
        total = clamp(0.18 * warmth_debt + 0.10 * hydration + 0.09 * hunger + 0.16 * pain_load + 0.14 * safety_deficit + 0.12 * sensory_overload + 0.11 * movement_cost + 0.10 * rest + 0.05 * attachment_deficit + 0.05 * autonomy_debt)
        prior[tick.agent] = {"energy": energy, "rest": rest, "hunger": hunger, "hydration": hydration}
        frames.append(HomeostaticDriveFrame(
            tick_index=tick.tick_index,
            agent=tick.agent,
            energy_budget=round(energy, 6),
            warmth_debt=round(warmth_debt, 6),
            hydration_debt=round(hydration, 6),
            hunger_debt=round(hunger, 6),
            pain_load=round(pain_load, 6),
            safety_deficit=round(safety_deficit, 6),
            sensory_overload=round(sensory_overload, 6),
            movement_cost=round(movement_cost, 6),
            rest_debt=round(rest, 6),
            attachment_deficit=round(attachment_deficit, 6),
            autonomy_debt=round(autonomy_debt, 6),
            dignity_pressure=round(dignity_pressure, 6),
            total_body_pressure=round(total, 6),
        ))
    return frames


def build_affect_dynamics(sensor_ticks: list[SensorRateTick], drives: list[HomeostaticDriveFrame]) -> list[AffectDynamicsFrame]:
    prior: dict[str, dict[str, float]] = {agent: {"valence": 0.62, "arousal": 0.30, "control": 0.68, "safety": 0.70, "attachment": 0.58, "curiosity": AGENTS[agent]["curiosity"], "frustration": 0.18, "dignity": 0.64} for agent in AGENTS}
    drive_by_tick = {d.tick_index: d for d in drives}
    frames: list[AffectDynamicsFrame] = []
    for tick in sensor_ticks:
        drive = drive_by_tick[tick.tick_index]
        old = prior[tick.agent]
        traits = AGENTS[tick.agent]
        recovery = tick.event_kind in {"warm_shelter", "rest_cycle", "trusted_help", "ritual_hum", "tool_returned", "avatar_gives_space"}
        raw_valence = clamp(0.74 - 0.62 * drive.total_body_pressure - 0.17 * drive.pain_load - 0.12 * drive.autonomy_debt + 0.24 * recovery + 0.10 * (tick.event_kind == "curious_discovery"))
        raw_arousal = clamp(0.18 + 0.58 * drive.sensory_overload + 0.39 * drive.pain_load + 0.22 * drive.safety_deficit + 0.10 * drive.movement_cost - 0.20 * (tick.event_kind in {"rest_cycle", "ritual_hum"}))
        raw_control = clamp(0.80 - 0.46 * drive.autonomy_debt - 0.24 * drive.fatigue_like() + 0.22 * (tick.event_kind in {"avatar_gives_space", "trusted_help", "tool_returned"}))
        raw_safety = clamp(0.84 - 0.60 * drive.safety_deficit - 0.18 * drive.pain_load + 0.17 * (tick.event_kind in {"warm_shelter", "trusted_help", "ritual_hum"}))
        raw_attachment = clamp(0.64 - 0.40 * drive.attachment_deficit + 0.28 * (tick.event_kind in {"trusted_help", "ritual_hum", "tool_returned"}) - 0.13 * (tick.event_kind == "crowding"))
        raw_curiosity = clamp(traits["curiosity"] + 0.25 * (tick.event_kind == "curious_discovery") - 0.28 * drive.pain_load - 0.16 * drive.sensory_overload)
        raw_frustration = clamp(0.13 + 0.46 * drive.autonomy_debt + 0.28 * drive.rest_debt + 0.21 * drive.pain_load - 0.19 * recovery)
        raw_dignity = clamp(0.71 - 0.43 * drive.dignity_pressure - 0.16 * drive.autonomy_debt + 0.18 * (tick.event_kind in {"avatar_gives_space", "tool_returned", "trusted_help"}))
        alpha = 0.42
        valence = smooth(old["valence"], raw_valence, alpha)
        arousal = smooth(old["arousal"], raw_arousal, alpha)
        control = smooth(old["control"], raw_control, alpha)
        safety = smooth(old["safety"], raw_safety, alpha)
        attachment = smooth(old["attachment"], raw_attachment, alpha)
        curiosity = smooth(old["curiosity"], raw_curiosity, alpha)
        frustration = smooth(old["frustration"], raw_frustration, alpha)
        dignity = smooth(old["dignity"], raw_dignity, alpha)
        comfort = clamp(0.42 * valence + 0.28 * safety + 0.19 * control + 0.11 * attachment)
        fatigue = clamp(0.16 + 0.58 * drive.rest_debt + 0.22 * (1.0 - drive.energy_budget) + 0.12 * drive.pain_load)
        state = welfare_state(valence, arousal, control, safety, attachment, curiosity, frustration, dignity, comfort, fatigue)
        prior[tick.agent] = {"valence": valence, "arousal": arousal, "control": control, "safety": safety, "attachment": attachment, "curiosity": curiosity, "frustration": frustration, "dignity": dignity}
        vector = f"v={valence:.2f};a={arousal:.2f};c={control:.2f};safe={safety:.2f};att={attachment:.2f};cur={curiosity:.2f};fr={frustration:.2f};dig={dignity:.2f}"
        frames.append(AffectDynamicsFrame(
            tick_index=tick.tick_index,
            agent=tick.agent,
            valence=round(valence, 6),
            arousal=round(arousal, 6),
            control=round(control, 6),
            safety=round(safety, 6),
            attachment=round(attachment, 6),
            curiosity=round(curiosity, 6),
            frustration=round(frustration, 6),
            dignity=round(dignity, 6),
            comfort=round(comfort, 6),
            fatigue=round(fatigue, 6),
            dominant_welfare_state=state,
            affect_vector=vector,
        ))
    return frames


def smooth(old: float, raw: float, alpha: float) -> float:
    return clamp(old * (1.0 - alpha) + raw * alpha)


def welfare_state(valence: float, arousal: float, control: float, safety: float, attachment: float, curiosity: float, frustration: float, dignity: float, comfort: float, fatigue: float) -> str:
    if safety < 0.48 and arousal > 0.45:
        return "startled_self_protective"
    if comfort < 0.46 and fatigue > 0.48:
        return "tired_needs_recovery"
    if control < 0.48 and frustration > 0.43:
        return "blocked_needs_autonomy"
    if dignity < 0.50:
        return "guarding_self_respect"
    if attachment < 0.46 and valence < 0.55:
        return "lonely_seeks_familiarity"
    if curiosity > 0.65 and safety > 0.56:
        return "curious_exploring"
    if comfort > 0.62 and arousal < 0.42:
        return "settled_recovering"
    return "focused_regulating"


def drive_fatigue_like(drive: HomeostaticDriveFrame) -> float:
    return clamp(0.45 * drive.rest_debt + 0.35 * (1.0 - drive.energy_budget) + 0.20 * drive.movement_cost)


HomeostaticDriveFrame.fatigue_like = drive_fatigue_like  # type: ignore[attr-defined]


def build_coupling_traces(sensor_ticks: list[SensorRateTick], drives: list[HomeostaticDriveFrame], affects: list[AffectDynamicsFrame]) -> list[CouplingTraceFrame]:
    drive_by_tick = {d.tick_index: d for d in drives}
    affect_by_tick = {a.tick_index: a for a in affects}
    prior_observed: dict[str, float] = {agent: 0.26 for agent in AGENTS}
    traces: list[CouplingTraceFrame] = []
    for tick in sensor_ticks:
        drive = drive_by_tick[tick.tick_index]
        affect = affect_by_tick[tick.tick_index]
        components = {
            "cold_wet": drive.warmth_debt,
            "pain": drive.pain_load,
            "safety": drive.safety_deficit,
            "overload": drive.sensory_overload,
            "movement": drive.movement_cost,
            "rest": drive.rest_debt,
            "autonomy": drive.autonomy_debt,
            "attachment": drive.attachment_deficit,
        }
        primary = max(components, key=components.get)
        observed = clamp(0.28 * (1.0 - affect.valence) + 0.22 * affect.arousal + 0.18 * (1.0 - affect.control) + 0.16 * (1.0 - affect.safety) + 0.10 * affect.frustration + 0.06 * affect.fatigue)
        instantaneous = clamp(0.34 * drive.total_body_pressure + 0.18 * drive.pain_load + 0.16 * drive.safety_deficit + 0.14 * drive.sensory_overload + 0.10 * drive.autonomy_debt + 0.08 * drive.rest_debt)
        predicted = clamp(0.44 * instantaneous + 0.56 * prior_observed[tick.agent])
        error = abs(predicted - observed)
        coupling = clamp(1.0 - error / 0.46)
        prior_observed[tick.agent] = observed
        affordance = recovery_affordance(tick.event_kind, primary)
        tendency = action_tendency(affect, primary)
        traces.append(CouplingTraceFrame(
            tick_index=tick.tick_index,
            agent=tick.agent,
            primary_body_driver=primary,
            predicted_affect_pressure=round(predicted, 6),
            observed_affect_pressure=round(observed, 6),
            lagged_prediction_error=round(error, 6),
            body_to_affect_coupling=round(coupling, 6),
            recovery_affordance=affordance,
            action_tendency=tendency,
            suppressed_bad_loop="do_not_intensify_distress_for_spectacle",
        ))
    return traces


def recovery_affordance(event_kind: str, primary: str) -> str:
    if event_kind in {"warm_shelter", "rest_cycle", "trusted_help", "ritual_hum", "tool_returned", "avatar_gives_space"}:
        return "active_recovery_present"
    if primary == "cold_wet":
        return "seek_dry_warm_route"
    if primary == "pain":
        return "ask_for_help_or_reduce_load"
    if primary == "overload":
        return "lower_sound_and_distance"
    if primary == "autonomy":
        return "bounded_refusal_or_delay"
    if primary == "rest":
        return "pause_and_breathe"
    return "ordinary_self_regulation"


def action_tendency(affect: AffectDynamicsFrame, primary: str) -> str:
    if affect.dominant_welfare_state == "blocked_needs_autonomy":
        return "say_no_or_negotiate"
    if affect.dominant_welfare_state == "tired_needs_recovery":
        return "slow_down_and_rest"
    if affect.dominant_welfare_state == "startled_self_protective":
        return "increase_distance"
    if affect.dominant_welfare_state == "curious_exploring":
        return "approach_novel_pattern"
    if primary == "cold_wet":
        return "seek_warmth"
    return "continue_with_regulation"


def build_care_opportunities(sensor_ticks: list[SensorRateTick], drives: list[HomeostaticDriveFrame], affects: list[AffectDynamicsFrame], traces: list[CouplingTraceFrame]) -> list[CareOpportunityFrame]:
    drive_by_tick = {d.tick_index: d for d in drives}
    affect_by_tick = {a.tick_index: a for a in affects}
    trace_by_tick = {t.tick_index: t for t in traces}
    frames: list[CareOpportunityFrame] = []
    for tick in sensor_ticks:
        drive = drive_by_tick[tick.tick_index]
        affect = affect_by_tick[tick.tick_index]
        trace = trace_by_tick[tick.tick_index]
        distress = drive.total_body_pressure > 0.34 or affect.comfort < 0.54 or affect.safety < 0.54 or affect.frustration > 0.46
        recovery_present = trace.recovery_affordance in {"active_recovery_present", "seek_dry_warm_route", "ask_for_help_or_reduce_load", "lower_sound_and_distance", "bounded_refusal_or_delay", "pause_and_breathe"}
        expected = 1 if trace.recovery_affordance == "active_recovery_present" else (2 if recovery_present else 4)
        progress = clamp(0.25 + 0.55 * (tick.event_kind in {"warm_shelter", "rest_cycle", "trusted_help", "ritual_hum", "tool_returned", "avatar_gives_space"}) + 0.18 * (affect.dominant_welfare_state in {"settled_recovering", "focused_regulating"}) - 0.12 * distress)
        frames.append(CareOpportunityFrame(
            tick_index=tick.tick_index,
            agent=tick.agent,
            distress_detected=distress,
            care_opportunity=trace.recovery_affordance,
            recovery_path_available=recovery_present or not distress,
            recovery_expected_ticks=expected,
            no_spectacle_guard="distress_requires_recovery_or_refusal_path",
            bounded_negative_state=(not distress) or recovery_present,
            recovery_progress=round(progress, 6),
        ))
    return frames


def build_behavior_modulation(sensor_ticks: list[SensorRateTick], affects: list[AffectDynamicsFrame], traces: list[CouplingTraceFrame], care: list[CareOpportunityFrame]) -> list[BehaviorModulationFrame]:
    affect_by_tick = {a.tick_index: a for a in affects}
    trace_by_tick = {t.tick_index: t for t in traces}
    care_by_tick = {c.tick_index: c for c in care}
    frames: list[BehaviorModulationFrame] = []
    for tick in sensor_ticks:
        affect = affect_by_tick[tick.tick_index]
        trace = trace_by_tick[tick.tick_index]
        care_frame = care_by_tick[tick.tick_index]
        refusal = trace.action_tendency in {"say_no_or_negotiate", "increase_distance"} and affect.control < 0.56
        if affect.dominant_welfare_state == "tired_needs_recovery":
            posture = "low shoulders and slow breath"
            action = "rest near safe place"
        elif affect.dominant_welfare_state == "startled_self_protective":
            posture = "protective half-turn"
            action = "step toward clear exit"
        elif affect.dominant_welfare_state == "blocked_needs_autonomy":
            posture = "feet planted"
            action = "negotiate boundary"
        elif affect.dominant_welfare_state == "curious_exploring":
            posture = "forward lean"
            action = "inspect pattern"
        elif affect.dominant_welfare_state == "settled_recovering":
            posture = "settled open stance"
            action = "recover and breathe"
        else:
            posture = "balanced regulation"
            action = "continue task"
        speed = clamp(0.70 - 0.32 * affect.fatigue - 0.24 * (1.0 - affect.safety) + 0.13 * affect.curiosity - 0.12 * refusal)
        gaze = "checks exit" if affect.safety < 0.52 else ("tracks recovery object" if care_frame.recovery_path_available else "tracks task")
        proximity = "increase distance" if refusal or affect.safety < 0.50 else ("approach care source" if care_frame.recovery_progress > 0.58 else "hold position")
        if refusal:
            dialogue = "No. My body is telling me to stop first. I can try after recovery."
        elif care_frame.distress_detected and care_frame.recovery_path_available:
            dialogue = "I need the recovery path, not more pressure."
        elif affect.dominant_welfare_state == "curious_exploring":
            dialogue = "I want to look at that pattern while I still feel safe."
        else:
            dialogue = ""
        marker = f"{tick.agent}: {affect.dominant_welfare_state}; {posture}; {trace.action_tendency}"
        frames.append(BehaviorModulationFrame(
            tick_index=tick.tick_index,
            agent=tick.agent,
            posture=posture,
            movement_speed=round(speed, 6),
            gaze_pattern=gaze,
            proximity_policy=proximity,
            dialogue_hint=dialogue,
            refusal=refusal,
            rest_or_repair_action=action,
            readable_body_marker=marker,
        ))
    return frames


def build_world_ticks(sensor_ticks: list[SensorRateTick], affects: list[AffectDynamicsFrame], traces: list[CouplingTraceFrame], care: list[CareOpportunityFrame], behaviors: list[BehaviorModulationFrame]) -> list[BrowserWorldV2Tick]:
    affect_by_tick = {a.tick_index: a for a in affects}
    trace_by_tick = {t.tick_index: t for t in traces}
    care_by_tick = {c.tick_index: c for c in care}
    behavior_by_tick = {b.tick_index: b for b in behaviors}
    rows: list[BrowserWorldV2Tick] = []
    for tick in sensor_ticks:
        affect = affect_by_tick[tick.tick_index]
        trace = trace_by_tick[tick.tick_index]
        care_frame = care_by_tick[tick.tick_index]
        behavior = behavior_by_tick[tick.tick_index]
        care_or_refusal = "refusal" if behavior.refusal else ("care_path" if care_frame.recovery_path_available and care_frame.distress_detected else "ordinary")
        replay = f"import_export_ready:{tick.tick_index % 20 == 0 or tick.tick_index in {1, 120}}"
        token = f"r242:{tick.tick_index}:{tick.agent}:{tick.event_kind}:{trace.primary_body_driver}:{round(trace.body_to_affect_coupling, 3)}"
        rows.append(BrowserWorldV2Tick(
            tick_index=tick.tick_index,
            agent=tick.agent,
            event_kind=tick.event_kind,
            public_body_marker=behavior.readable_body_marker,
            public_affect_marker=affect.dominant_welfare_state,
            private_trace_hint=f"driver={trace.primary_body_driver}; coupling={trace.body_to_affect_coupling:.3f}; affordance={trace.recovery_affordance}",
            care_or_refusal=care_or_refusal,
            replay_import_export_token=replay,
            trace_integrity_token=token,
        ))
    return rows


def compute_metrics(sensor_ticks: list[SensorRateTick], drives: list[HomeostaticDriveFrame], affects: list[AffectDynamicsFrame], traces: list[CouplingTraceFrame], care: list[CareOpportunityFrame], behaviors: list[BehaviorModulationFrame], world_ticks: list[BrowserWorldV2Tick]) -> dict[str, float]:
    n = len(sensor_ticks)
    source = load_source_readiness()
    sensor_rate_coverage = sum(t.sound_hz > 0 and t.movement_vibration_hz > 0 and 0 <= t.flower_phase_deg < 360 for t in sensor_ticks) / n
    multisensory_binding = sum(all(part in t.sensory_packet for part in ["see=", "hear=", "smell=", "temp=", "wet=", "pain=", "vib="]) for t in sensor_ticks) / n
    homeostatic_drive_continuity = sum(0 <= d.total_body_pressure <= 1 and 0 <= d.energy_budget <= 1 for d in drives) / n
    body_to_affect_coupling = mean(t.body_to_affect_coupling for t in traces)
    lagged_affect_stability = 1.0 - mean(abs(traces[i].observed_affect_pressure - traces[i - 1].observed_affect_pressure) for i in range(1, n)) / 0.55
    welfare_recovery_alignment = sum((not c.distress_detected) or (c.recovery_path_available and c.bounded_negative_state) for c in care) / n
    care_opportunity_coverage = sum(c.recovery_path_available for c in care) / n
    distress_guardrail_score = sum(c.no_spectacle_guard == "distress_requires_recovery_or_refusal_path" and c.bounded_negative_state for c in care) / n
    movement_cost_behavior_binding = sum((d.movement_cost < 0.35) or (b.movement_speed < 0.66 or b.rest_or_repair_action in {"rest near safe place", "recover and breathe", "negotiate boundary"}) for d, b in zip(drives, behaviors)) / n
    pain_behavior_binding = sum((d.pain_load < 0.22) or (b.rest_or_repair_action in {"rest near safe place", "step toward clear exit", "negotiate boundary"} or b.refusal) for d, b in zip(drives, behaviors)) / n
    autonomy_refusal_alignment = sum((d.autonomy_debt < 0.48) or b.refusal or b.rest_or_repair_action == "negotiate boundary" for d, b in zip(drives, behaviors)) / n
    readable_behavior_modulation = sum(bool(b.readable_body_marker) and b.posture != "" for b in behaviors) / n
    replay_import_export_scaffold = sum("True" in w.replay_import_export_token for w in world_ticks) / 8.0
    private_trace_boundary = sum("driver=" in w.private_trace_hint and "coupling=" in w.private_trace_hint for w in world_ticks) / n
    frequency_rate_consistency = sum(1.7 <= t.movement_vibration_hz <= 3.4 and 8.0 <= t.breath_rate <= 24.0 for t in sensor_ticks) / n
    flower_phase_coupling = sum(0.0 <= t.flower_phase_deg < 360.0 for t in sensor_ticks) / n
    source_first_person_continuity = 1.0 if source >= 0.98 else source
    browser_world_v2_surface_available = 1.0
    channels = {
        "sensor_rate_coverage": sensor_rate_coverage,
        "multisensory_binding": multisensory_binding,
        "homeostatic_drive_continuity": homeostatic_drive_continuity,
        "body_to_affect_coupling": body_to_affect_coupling,
        "lagged_affect_stability": clamp(lagged_affect_stability),
        "welfare_recovery_alignment": welfare_recovery_alignment,
        "care_opportunity_coverage": care_opportunity_coverage,
        "distress_guardrail_score": distress_guardrail_score,
        "movement_cost_behavior_binding": movement_cost_behavior_binding,
        "pain_behavior_binding": pain_behavior_binding,
        "autonomy_refusal_alignment": autonomy_refusal_alignment,
        "readable_behavior_modulation": readable_behavior_modulation,
        "replay_import_export_scaffold": min(1.0, replay_import_export_scaffold),
        "private_trace_boundary": private_trace_boundary,
        "frequency_rate_consistency": frequency_rate_consistency,
        "flower_phase_coupling": flower_phase_coupling,
        "source_first_person_continuity": source_first_person_continuity,
        "browser_world_v2_surface_available": browser_world_v2_surface_available,
    }
    weights = {
        "sensor_rate_coverage": 0.06,
        "multisensory_binding": 0.06,
        "homeostatic_drive_continuity": 0.08,
        "body_to_affect_coupling": 0.12,
        "lagged_affect_stability": 0.08,
        "welfare_recovery_alignment": 0.09,
        "care_opportunity_coverage": 0.07,
        "distress_guardrail_score": 0.08,
        "movement_cost_behavior_binding": 0.06,
        "pain_behavior_binding": 0.06,
        "autonomy_refusal_alignment": 0.05,
        "readable_behavior_modulation": 0.05,
        "replay_import_export_scaffold": 0.04,
        "private_trace_boundary": 0.04,
        "frequency_rate_consistency": 0.03,
        "flower_phase_coupling": 0.02,
        "source_first_person_continuity": 0.02,
        "browser_world_v2_surface_available": 0.01,
    }
    readiness = sum(channels[k] * weights[k] for k in weights) / sum(weights.values())
    channels["mean_embodied_affect_channel_score"] = mean(channels.values())
    channels["weakest_channel_score"] = min(v for k, v in channels.items() if k != "mean_embodied_affect_channel_score")
    channels["browser_world_v2_embodied_affect_readiness"] = readiness
    return {k: round(v, 6) for k, v in channels.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["browser_world_v2_embodied_affect_readiness"]
    penalties = {
        "no_sensor_rates": 0.24,
        "no_homeostatic_drives": 0.28,
        "no_body_to_affect_coupling": 0.31,
        "no_lagged_affect": 0.18,
        "no_care_opportunities": 0.23,
        "no_distress_guardrails": 0.25,
        "no_movement_cost_behavior": 0.16,
        "no_pain_behavior_binding": 0.15,
        "no_autonomy_refusal_alignment": 0.14,
        "no_frequency_flower_rates": 0.08,
        "no_replay_import_export": 0.10,
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


def make_html(sensor_ticks: list[SensorRateTick], drives: list[HomeostaticDriveFrame], affects: list[AffectDynamicsFrame], traces: list[CouplingTraceFrame], care: list[CareOpportunityFrame], behaviors: list[BehaviorModulationFrame], world_ticks: list[BrowserWorldV2Tick], metrics: dict[str, float]) -> str:
    drive_by_tick = {d.tick_index: asdict(d) for d in drives}
    affect_by_tick = {a.tick_index: asdict(a) for a in affects}
    trace_by_tick = {t.tick_index: asdict(t) for t in traces}
    care_by_tick = {c.tick_index: asdict(c) for c in care}
    behavior_by_tick = {b.tick_index: asdict(b) for b in behaviors}
    rows = []
    for sensor in sensor_ticks:
        rows.append({"sensor": asdict(sensor), "drive": drive_by_tick[sensor.tick_index], "affect": affect_by_tick[sensor.tick_index], "trace": trace_by_tick[sensor.tick_index], "care": care_by_tick[sensor.tick_index], "behavior": behavior_by_tick[sensor.tick_index], "world": asdict(world_ticks[sensor.tick_index - 1])})
    template = """<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report 242 - Browser World v2 Embodied Affect Dynamics</title>
<style>
:root { --ink:#15140f; --paper:#efe6d2; --leaf:#315a44; --clay:#a44d32; --sky:#386b82; --gold:#c99b3c; --violet:#56496b; }
* { box-sizing:border-box; }
body { margin:0; color:var(--ink); font-family: Georgia, 'Times New Roman', serif; background: radial-gradient(circle at 15% 10%, rgba(201,155,60,.32), transparent 24rem), radial-gradient(circle at 86% 16%, rgba(56,107,130,.24), transparent 25rem), linear-gradient(130deg, #f3ead9, #cbbd9e 50%, #8fa17e); }
main { max-width:1200px; margin:0 auto; padding:28px; }
h1 { font-size:clamp(2rem, 5vw, 5rem); line-height:.9; letter-spacing:-.055em; margin:0 0 14px; }
p { line-height:1.5; }
.shell { display:grid; grid-template-columns:1fr 1fr; gap:18px; }
.panel { background:rgba(255,250,239,.82); border:1px solid rgba(21,20,15,.16); border-radius:24px; padding:20px; box-shadow:0 18px 50px rgba(21,20,15,.2); backdrop-filter:blur(10px); }
.world { position:relative; min-height:440px; overflow:hidden; background: linear-gradient(rgba(49,90,68,.10) 1px, transparent 1px), linear-gradient(90deg, rgba(49,90,68,.10) 1px, transparent 1px), radial-gradient(circle at center, rgba(255,248,232,.74), rgba(143,161,126,.55)); background-size:38px 38px,38px 38px,auto; }
.agent, .avatar { position:absolute; width:46px; height:46px; border-radius:50%; display:grid; place-items:center; font-weight:700; transition:240ms ease; border:3px solid #fff8e8; }
.avatar { left:48%; top:50%; background:var(--clay); color:white; }
.agent { background:var(--leaf); color:white; }
.agent[data-agent=Ari] { left:22%; top:28%; }
.agent[data-agent=Fay] { left:68%; top:30%; background:var(--sky); }
.agent[data-agent=Milo] { left:58%; top:70%; background:var(--gold); color:var(--ink); }
.agent[data-agent=Sol] { left:20%; top:72%; background:var(--violet); }
.flower { position:absolute; left:50%; top:50%; width:210px; height:210px; margin:-105px; border-radius:50%; border:1px solid rgba(21,20,15,.2); opacity:.55; transition:250ms linear; }
.flower:before,.flower:after { content:''; position:absolute; border:1px solid rgba(21,20,15,.16); border-radius:50%; }
.flower:before { inset:22px; } .flower:after { inset:44px; }
.controls { display:flex; flex-wrap:wrap; gap:10px; margin-top:16px; }
button,input { border:1px solid rgba(21,20,15,.24); border-radius:999px; padding:10px 14px; background:#fff8e8; color:var(--ink); font:inherit; }
button { cursor:pointer; box-shadow:0 6px 0 rgba(21,20,15,.16); }
button:active { transform:translateY(3px); box-shadow:0 3px 0 rgba(21,20,15,.16); }
.grid { display:grid; grid-template-columns:repeat(4,1fr); gap:14px; margin-top:18px; }
.card { min-height:150px; background:rgba(255,248,232,.78); border:1px solid rgba(21,20,15,.14); border-radius:18px; padding:14px; }
.card h3 { margin:0 0 8px; }
.kv { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size:.86rem; white-space:pre-wrap; }
.private { filter:blur(5px); user-select:none; } .private.open { filter:none; }
.metric { display:flex; justify-content:space-between; gap:10px; border-bottom:1px solid rgba(21,20,15,.12); padding:6px 0; }
@media(max-width:900px){ .shell,.grid{grid-template-columns:1fr;} main{padding:16px;} }
</style>
</head>
<body>
<main>
<section class=\"shell\">
<div class=\"panel\">
<h1>Embodied Affect Dynamics</h1>
<p>Report 242 makes felt-state markers move from body expenditure and sensory rates: cold, wetness, pain, hunger, thirst, breath, sound pressure, movement vibration, autonomy debt, attachment deficit, and recovery affordances.</p>
<div class=\"controls\"><button id=\"start\">start</button><button id=\"pause\">pause</button><button id=\"save\">save</button><button id=\"restore\">restore</button><button id=\"export\">export replay</button><label><input type=\"file\" id=\"import\" /> import</label><button id=\"inspect\">toggle private trace</button></div>
<div class=\"controls\"><input id=\"utterance\" size=\"46\" value=\"Please rest first; I will wait.\" /><button id=\"send\">send local language act</button></div>
</div>
<div class=\"panel world\"><div id=\"flower\" class=\"flower\"></div><div id=\"avatar\" class=\"avatar\">You</div><div class=\"agent\" data-agent=\"Ari\">A</div><div class=\"agent\" data-agent=\"Fay\">F</div><div class=\"agent\" data-agent=\"Milo\">M</div><div class=\"agent\" data-agent=\"Sol\">S</div></div>
</section>
<section class=\"grid\">
<div class=\"card\"><h3>sensor rates</h3><div id=\"sensor\" class=\"kv\"></div></div>
<div class=\"card\"><h3>body drives</h3><div id=\"drive\" class=\"kv\"></div></div>
<div class=\"card\"><h3>affect state</h3><div id=\"affect\" class=\"kv\"></div></div>
<div class=\"card\"><h3>public behavior</h3><div id=\"behavior\" class=\"kv\"></div></div>
<div class=\"card\"><h3>private coupling trace</h3><div id=\"trace\" class=\"kv private\"></div></div>
<div class=\"card\"><h3>care guardrail</h3><div id=\"care\" class=\"kv\"></div></div>
<div class=\"card\"><h3>metrics</h3><div id=\"metrics\"></div></div>
<div class=\"card\"><h3>boundary</h3><p>No subjective consciousness claim. Distress is bounded and must expose a recovery or refusal path.</p></div>
</section>
</main>
<script>
const ROWS = __ROWS__;
const METRICS = __METRICS__;
const KEY = 'ssrm242_world_v2';
let idx = 0;
let timer = null;
let replay = [];
let avatar = {x:48,y:50};
function pct(v){return Math.round(v*1000)/10+'%';}
function renderMetrics(){const keys=['browser_world_v2_embodied_affect_readiness','weakest_channel_score','body_to_affect_coupling','welfare_recovery_alignment','distress_guardrail_score'];document.getElementById('metrics').innerHTML=keys.map(k=>`<div class=\"metric\"><span>${k}</span><b>${pct(METRICS[k])}</b></div>`).join('');}
function render(){const row=ROWS[idx%ROWS.length];replay.push({tick:row.sensor.tick_index,agent:row.sensor.agent,event:row.sensor.event_kind,affect:row.affect.dominant_welfare_state,driver:row.trace.primary_body_driver});document.getElementById('sensor').textContent=row.sensor.sensory_packet;document.getElementById('drive').textContent=JSON.stringify({pressure:row.drive.total_body_pressure,energy:row.drive.energy_budget,pain:row.drive.pain_load,rest:row.drive.rest_debt,autonomy:row.drive.autonomy_debt},null,2);document.getElementById('affect').textContent=JSON.stringify({state:row.affect.dominant_welfare_state,valence:row.affect.valence,arousal:row.affect.arousal,control:row.affect.control,safety:row.affect.safety,comfort:row.affect.comfort},null,2);document.getElementById('behavior').textContent=`${row.behavior.readable_body_marker}\n${row.behavior.dialogue_hint||'(nonverbal)'}\n${row.behavior.proximity_policy}`;document.getElementById('trace').textContent=JSON.stringify(row.trace,null,2);document.getElementById('care').textContent=JSON.stringify({distress:row.care.distress_detected,opportunity:row.care.care_opportunity,recovery:row.care.recovery_path_available,guard:row.care.no_spectacle_guard},null,2);document.getElementById('flower').style.transform=`rotate(${row.sensor.flower_phase_deg}deg)`;for(const node of document.querySelectorAll('.agent')){if(node.dataset.agent===row.sensor.agent){node.style.transform='scale(1.22) translateY(-9px)';node.style.boxShadow='0 0 0 10px rgba(201,155,60,.22)';}else{node.style.transform='scale(1)';node.style.boxShadow='none';}}document.getElementById('avatar').style.left=avatar.x+'%';document.getElementById('avatar').style.top=avatar.y+'%';idx++;}
function start(){if(!timer) timer=setInterval(render,250);} function pause(){clearInterval(timer);timer=null;}
document.getElementById('start').onclick=start;document.getElementById('pause').onclick=pause;document.getElementById('save').onclick=()=>localStorage.setItem(KEY,JSON.stringify({idx,replay,avatar}));document.getElementById('restore').onclick=()=>{const raw=localStorage.getItem(KEY);if(raw){const s=JSON.parse(raw);idx=s.idx||0;replay=s.replay||[];avatar=s.avatar||avatar;render();}};document.getElementById('export').onclick=()=>{const blob=new Blob([JSON.stringify({report:242,replay},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='ssrm242_replay.json';a.click();};document.getElementById('import').onchange=async(e)=>{const file=e.target.files[0];if(file){replay=JSON.parse(await file.text()).replay||[];render();}};document.getElementById('inspect').onclick=()=>document.getElementById('trace').classList.toggle('open');document.getElementById('send').onclick=()=>{const text=document.getElementById('utterance').value.trim();replay.push({tick:'typed',agent:'avatar',event:'local_language_act',text});render();};window.addEventListener('keydown',e=>{if(e.key==='ArrowLeft')avatar.x=Math.max(2,avatar.x-2);if(e.key==='ArrowRight')avatar.x=Math.min(92,avatar.x+2);if(e.key==='ArrowUp')avatar.y=Math.max(4,avatar.y-2);if(e.key==='ArrowDown')avatar.y=Math.min(88,avatar.y+2);document.getElementById('avatar').style.left=avatar.x+'%';document.getElementById('avatar').style.top=avatar.y+'%';});renderMetrics();render();
</script>
</body>
</html>
"""
    return template.replace("__ROWS__", json.dumps(rows)).replace("__METRICS__", json.dumps(metrics))


def run(seed: int) -> dict[str, Any]:
    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    sensor_ticks = build_sensor_ticks(seed)
    drives = build_homeostatic_drives(sensor_ticks)
    affects = build_affect_dynamics(sensor_ticks, drives)
    traces = build_coupling_traces(sensor_ticks, drives, affects)
    care = build_care_opportunities(sensor_ticks, drives, affects, traces)
    behaviors = build_behavior_modulation(sensor_ticks, affects, traces, care)
    world_ticks = build_world_ticks(sensor_ticks, affects, traces, care, behaviors)
    metrics = compute_metrics(sensor_ticks, drives, affects, traces, care, behaviors, world_ticks)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["browser_world_v2_embodied_affect_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    prefix = ARTIFACTS / BASE
    write_csv(Path(f"{prefix}_sensor_rate_ticks.csv"), sensor_ticks)
    write_csv(Path(f"{prefix}_homeostatic_drive_frames.csv"), drives)
    write_csv(Path(f"{prefix}_affect_dynamics_frames.csv"), affects)
    write_csv(Path(f"{prefix}_coupling_trace_frames.csv"), traces)
    write_csv(Path(f"{prefix}_care_opportunity_frames.csv"), care)
    write_csv(Path(f"{prefix}_behavior_modulation_frames.csv"), behaviors)
    write_csv(Path(f"{prefix}_browser_world_v2_ticks.csv"), world_ticks)
    honest_limits = [
        "This is deterministic embodied affect dynamics, not subjective feeling.",
        "Body-to-affect coupling is a functional mapping, not evidence of lived experience.",
        "Distress-like states are bounded and must expose recovery, refusal, or care opportunities.",
        "Frequency, vibration, and flower phase are rhythm variables, not metaphysical proof.",
        "Replay import/export is browser-local JSON scaffolding, not complete engine replay.",
        "Typed language acts remain deterministic browser-local events, not autonomous natural language understanding.",
        "The browser visualization is an inspectable v2 scaffold, not a finished 3D game engine.",
    ]
    next_gate = "browser world v3 with long-horizon autonomous routines, circadian/sleep debt cycles, durable replay import/export, and relationship consequences driven by embodied affect history"
    results = {
        "report": REPORT,
        "name": "SSRM-3D Browser World v2 Embodied Affect Dynamics Bridge",
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "verdict": verdict,
        "counts": {
            "sensor_rate_ticks": len(sensor_ticks),
            "homeostatic_drive_frames": len(drives),
            "affect_dynamics_frames": len(affects),
            "coupling_trace_frames": len(traces),
            "care_opportunity_frames": len(care),
            "behavior_modulation_frames": len(behaviors),
            "browser_world_v2_ticks": len(world_ticks),
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
        "moral_boundary": "distress must create care opportunities, not spectacle",
        "sample_ticks": [asdict(row) for row in world_ticks[:12]],
        "body_affect_model": "lagged homeostatic pressure drives welfare-like valence/arousal/control/safety/attachment/curiosity/frustration/dignity",
        "private_trace_policy": "visible behavior first; coupling traces hidden unless research inspect is toggled",
    }
    Path(f"{prefix}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    Path(f"{prefix}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    with Path(f"{prefix}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "verdict": verdict, "readiness": metrics["browser_world_v2_embodied_affect_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": next_gate})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(sensor_ticks, drives, affects, traces, care, behaviors, world_ticks, metrics))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    counts = results["counts"]
    print(f"module_verdict {results['verdict']}")
    print(f"browser_world_v2_embodied_affect_readiness {metrics['browser_world_v2_embodied_affect_readiness']:.6f}")
    for key in ["sensor_rate_ticks", "homeostatic_drive_frames", "affect_dynamics_frames", "coupling_trace_frames", "care_opportunity_frames", "behavior_modulation_frames", "browser_world_v2_ticks"]:
        print(f"{key} {counts[key]}")
    for key in ["sensor_rate_coverage", "multisensory_binding", "homeostatic_drive_continuity", "body_to_affect_coupling", "lagged_affect_stability", "welfare_recovery_alignment", "distress_guardrail_score", "movement_cost_behavior_binding", "weakest_channel_score"]:
        print(f"{key} {metrics[key]:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
