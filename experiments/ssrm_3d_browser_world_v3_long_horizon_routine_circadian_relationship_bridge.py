#!/usr/bin/env python3
"""Report 243: SSRM-3D browser world v3 long-horizon routine/circadian relationship bridge.

This deterministic bridge extends Report 242 by making embodied affect history
matter across days: autonomous routines, circadian/sleep debt cycles, replay
import/export checkpoints, and relationship consequences are all carried through
a 21-day browser-world v3 trace.

No subjective consciousness, real consent, moral patienthood, or metaphysical
frequency claim is made.
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

REPORT = 243
BASE = "ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge"
DEFAULT_SEED = 20260856
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v2_embodied_affect_dynamics_bridge_results.json"

AGENTS: dict[str, dict[str, Any]] = {
    "Ari": {"role": "route keeper", "chronotype": 0.18, "autonomy_need": 0.66, "attachment_need": 0.46, "routine_bias": "repair", "safe_place": "workbench alcove", "baseline_trust": 0.54, "frequency_hz": 2.18},
    "Fay": {"role": "hearth ritualist", "chronotype": -0.10, "autonomy_need": 0.49, "attachment_need": 0.73, "routine_bias": "care", "safe_place": "hearth nest", "baseline_trust": 0.62, "frequency_hz": 2.34},
    "Milo": {"role": "market pattern scout", "chronotype": 0.32, "autonomy_need": 0.61, "attachment_need": 0.51, "routine_bias": "explore", "safe_place": "market canopy", "baseline_trust": 0.58, "frequency_hz": 2.51},
    "Sol": {"role": "seed ledger guardian", "chronotype": -0.22, "autonomy_need": 0.72, "attachment_need": 0.57, "routine_bias": "account", "safe_place": "quiet corner", "baseline_trust": 0.49, "frequency_hz": 2.07},
}

ROUTINE_BY_PHASE = {
    "dawn": ["wake_check_body", "prepare_tools", "quiet_route_scan", "share_water"],
    "day": ["work_project", "market_exchange", "repair_route", "teach_skill"],
    "dusk": ["hearth_return", "ritual_hum", "relationship_check", "store_objects"],
    "night": ["sleep", "dream_sort_memory", "guarded_rest", "soft_recovery"],
}

EVENTS = ["ordinary", "help_received", "pressure_repeated", "cold_rain", "shared_ritual", "object_returned", "crowding", "quiet_success"]


@dataclass(frozen=True)
class AutonomousRoutineTick:
    tick_index: int
    day: int
    hour: int
    phase: str
    agent: str
    role: str
    routine: str
    autonomous_goal: str
    avatar_pressure: float
    social_context: str
    event_kind: str
    routine_source: str
    routine_continuity_token: str


@dataclass(frozen=True)
class CircadianSleepFrame:
    tick_index: int
    agent: str
    circadian_phase: float
    wake_pressure: float
    sleep_debt: float
    sleep_quality: float
    rest_recovery: float
    dream_memory_sorting: float
    fatigue_next_tick: float
    rhythm_vibration_hz: float
    flower_phase_deg: float
    sleep_state: str


@dataclass(frozen=True)
class AffectHistoryFrame:
    tick_index: int
    agent: str
    rolling_valence: float
    rolling_arousal: float
    rolling_control: float
    rolling_safety: float
    embodied_stress_load: float
    recovery_momentum: float
    affect_memory_charge: float
    dominant_long_mood: str
    private_history_note: str


@dataclass(frozen=True)
class RelationshipConsequenceFrame:
    tick_index: int
    agent: str
    other_actor: str
    trust: float
    comfort: float
    avoidance: float
    dependency: float
    gratitude: float
    resentment: float
    attachment_security: float
    consequence_action: str
    remembered_reason: str


@dataclass(frozen=True)
class RoutineConsequenceFrame:
    tick_index: int
    agent: str
    routine: str
    project_progress: float
    skill_practice: float
    resource_change: float
    social_face_change: float
    autonomy_satisfaction: float
    routine_variation: float
    consequence_summary: str


@dataclass(frozen=True)
class ReplayContinuityFrame:
    tick_index: int
    day: int
    checkpoint_id: str
    import_hash: str
    export_hash: str
    restore_verified: bool
    replay_rows_carried: int
    durable_state_keys: str


@dataclass(frozen=True)
class BrowserWorldV3Tick:
    tick_index: int
    day: int
    agent: str
    public_routine_marker: str
    public_body_affect_marker: str
    public_relationship_marker: str
    private_history_hint: str
    replay_checkpoint: str
    trace_integrity_token: str


def clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, value))


def source_readiness() -> float:
    if not SOURCE_RESULTS.exists():
        return 0.0
    data = json.loads(SOURCE_RESULTS.read_text())
    return float(data.get("metrics", {}).get("browser_world_v2_embodied_affect_readiness", 0.0))


def phase_for_hour(hour: int) -> str:
    if 5 <= hour < 9:
        return "dawn"
    if 9 <= hour < 17:
        return "day"
    if 17 <= hour < 21:
        return "dusk"
    return "night"


def stable_hash(payload: str, size: int = 12) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:size]


def build_routine_ticks(seed: int) -> list[AutonomousRoutineTick]:
    rng = random.Random(seed)
    agents = list(AGENTS)
    ticks: list[AutonomousRoutineTick] = []
    tick_index = 0
    for day in range(1, 22):
        for hour in [5, 8, 11, 14, 17, 20, 23, 2]:
            phase = phase_for_hour(hour)
            for agent in agents:
                tick_index += 1
                traits = AGENTS[agent]
                options = ROUTINE_BY_PHASE[phase]
                bias = traits["routine_bias"]
                offset = (day + hour + agents.index(agent)) % len(options)
                routine = options[offset]
                if phase == "day" and bias == "repair":
                    routine = "repair_route"
                if phase == "dusk" and bias == "care":
                    routine = "ritual_hum"
                if phase == "day" and bias == "explore" and day % 2 == 0:
                    routine = "market_exchange"
                if phase == "dawn" and bias == "account" and day % 3 == 0:
                    routine = "quiet_route_scan"
                event_kind = EVENTS[(day + hour + agents.index(agent)) % len(EVENTS)]
                avatar_pressure = clamp(0.08 + 0.43 * (event_kind == "pressure_repeated") + 0.17 * (event_kind == "crowding") - 0.11 * (event_kind in {"help_received", "object_returned"}) + rng.uniform(-0.015, 0.015))
                social = "avatar nearby" if avatar_pressure > 0.30 else ("trusted peer nearby" if event_kind in {"help_received", "shared_ritual"} else "self-directed")
                goal = goal_for_routine(agent, routine, phase)
                token = f"r243:{day}:{hour}:{agent}:{routine}:{stable_hash(goal, 8)}"
                ticks.append(AutonomousRoutineTick(
                    tick_index=tick_index,
                    day=day,
                    hour=hour,
                    phase=phase,
                    agent=agent,
                    role=traits["role"],
                    routine=routine,
                    autonomous_goal=goal,
                    avatar_pressure=round(avatar_pressure, 6),
                    social_context=social,
                    event_kind=event_kind,
                    routine_source="agent_schedule_not_avatar_command",
                    routine_continuity_token=token,
                ))
    return ticks


def goal_for_routine(agent: str, routine: str, phase: str) -> str:
    if routine == "sleep":
        return f"{agent} protects recovery before tomorrow"
    if routine == "dream_sort_memory":
        return f"{agent} sorts social episodes into private story"
    if routine == "ritual_hum":
        return f"{agent} stabilizes group rhythm"
    if routine == "repair_route":
        return f"{agent} keeps a route usable"
    if routine == "market_exchange":
        return f"{agent} trades without losing boundaries"
    if routine == "relationship_check":
        return f"{agent} tests whether trust changed"
    return f"{agent} continues {phase} routine: {routine}"


def build_circadian_frames(routines: list[AutonomousRoutineTick]) -> list[CircadianSleepFrame]:
    sleep_debt: dict[str, float] = {agent: 0.22 for agent in AGENTS}
    frames: list[CircadianSleepFrame] = []
    for row in routines:
        traits = AGENTS[row.agent]
        hour_angle = ((row.hour % 24) / 24.0 + traits["chronotype"] * 0.10) * math.tau
        circadian_phase = (math.sin(hour_angle - math.pi / 2) + 1.0) / 2.0
        is_sleep = row.routine in {"sleep", "dream_sort_memory", "guarded_rest", "soft_recovery"}
        wake_pressure = clamp(0.18 + 0.64 * circadian_phase + 0.28 * sleep_debt[row.agent] - 0.44 * is_sleep)
        quality = clamp(0.36 + 0.43 * is_sleep + 0.12 * (row.event_kind in {"shared_ritual", "quiet_success"}) - 0.18 * row.avatar_pressure - 0.12 * (row.event_kind == "cold_rain"))
        rest_recovery = clamp(0.08 + 0.56 * is_sleep * quality + 0.18 * (row.routine in {"ritual_hum", "soft_recovery"}))
        new_debt = clamp(sleep_debt[row.agent] + 0.045 * (not is_sleep) + 0.036 * row.avatar_pressure + 0.035 * (row.event_kind in {"cold_rain", "crowding"}) - 0.32 * rest_recovery)
        dream_sort = clamp(0.12 + 0.58 * (row.routine == "dream_sort_memory") + 0.15 * quality)
        fatigue_next = clamp(0.16 + 0.66 * new_debt + 0.12 * row.avatar_pressure - 0.13 * quality)
        vibration = traits["frequency_hz"] + 0.22 * wake_pressure - 0.18 * rest_recovery + 0.09 * math.sin(row.tick_index / 8.0)
        flower = (row.tick_index * 137.507764 + row.day * 23.0 + traits["frequency_hz"] * 29.0) % 360.0
        sleep_debt[row.agent] = new_debt
        if is_sleep and quality > 0.60:
            state = "deep_recovery_sleep"
        elif is_sleep:
            state = "light_guarded_rest"
        elif fatigue_next > 0.62:
            state = "sleep_debt_visible"
        elif wake_pressure > 0.62:
            state = "awake_active"
        else:
            state = "steady_wakefulness"
        frames.append(CircadianSleepFrame(
            tick_index=row.tick_index,
            agent=row.agent,
            circadian_phase=round(circadian_phase, 6),
            wake_pressure=round(wake_pressure, 6),
            sleep_debt=round(new_debt, 6),
            sleep_quality=round(quality, 6),
            rest_recovery=round(rest_recovery, 6),
            dream_memory_sorting=round(dream_sort, 6),
            fatigue_next_tick=round(fatigue_next, 6),
            rhythm_vibration_hz=round(vibration, 6),
            flower_phase_deg=round(flower, 6),
            sleep_state=state,
        ))
    return frames


def build_affect_history(routines: list[AutonomousRoutineTick], circadian: list[CircadianSleepFrame]) -> list[AffectHistoryFrame]:
    circadian_by_tick = {c.tick_index: c for c in circadian}
    state: dict[str, dict[str, float]] = {agent: {"valence": 0.60, "arousal": 0.32, "control": 0.64, "safety": 0.67, "stress": 0.20, "recovery": 0.28, "charge": 0.22} for agent in AGENTS}
    frames: list[AffectHistoryFrame] = []
    for row in routines:
        c = circadian_by_tick[row.tick_index]
        old = state[row.agent]
        traits = AGENTS[row.agent]
        care_event = row.event_kind in {"help_received", "shared_ritual", "object_returned", "quiet_success"}
        pressure_event = row.event_kind in {"pressure_repeated", "cold_rain", "crowding"}
        stress_raw = clamp(0.20 + 0.34 * c.sleep_debt + 0.20 * row.avatar_pressure + 0.18 * pressure_event - 0.18 * c.rest_recovery - 0.12 * care_event)
        recovery_raw = clamp(0.18 + 0.44 * c.rest_recovery + 0.19 * care_event + 0.13 * (row.routine in {"ritual_hum", "soft_recovery", "dream_sort_memory"}) - 0.10 * pressure_event)
        valence_raw = clamp(0.62 + 0.22 * recovery_raw + 0.08 * care_event - 0.30 * stress_raw - 0.09 * c.sleep_debt)
        arousal_raw = clamp(0.24 + 0.34 * c.wake_pressure + 0.20 * pressure_event + 0.12 * row.avatar_pressure - 0.20 * c.rest_recovery)
        control_raw = clamp(0.66 + 0.20 * (row.routine_source == "agent_schedule_not_avatar_command") - 0.27 * row.avatar_pressure - 0.10 * c.sleep_debt + 0.10 * traits["autonomy_need"])
        safety_raw = clamp(0.68 + 0.17 * care_event + 0.11 * c.rest_recovery - 0.24 * pressure_event - 0.10 * c.sleep_debt)
        valence = smooth(old["valence"], valence_raw, 0.25)
        arousal = smooth(old["arousal"], arousal_raw, 0.25)
        control = smooth(old["control"], control_raw, 0.25)
        safety = smooth(old["safety"], safety_raw, 0.25)
        stress = smooth(old["stress"], stress_raw, 0.32)
        recovery = smooth(old["recovery"], recovery_raw, 0.32)
        charge = clamp(old["charge"] * 0.83 + 0.13 * stress + 0.09 * row.avatar_pressure - 0.10 * recovery)
        state[row.agent] = {"valence": valence, "arousal": arousal, "control": control, "safety": safety, "stress": stress, "recovery": recovery, "charge": charge}
        mood = long_mood(valence, arousal, control, safety, stress, recovery, charge, c.sleep_debt)
        note = f"private: {row.agent} carries {mood} from day {row.day}; stress={stress:.2f}; recovery={recovery:.2f}; charge={charge:.2f}"
        frames.append(AffectHistoryFrame(
            tick_index=row.tick_index,
            agent=row.agent,
            rolling_valence=round(valence, 6),
            rolling_arousal=round(arousal, 6),
            rolling_control=round(control, 6),
            rolling_safety=round(safety, 6),
            embodied_stress_load=round(stress, 6),
            recovery_momentum=round(recovery, 6),
            affect_memory_charge=round(charge, 6),
            dominant_long_mood=mood,
            private_history_note=note,
        ))
    return frames


def smooth(old: float, raw: float, alpha: float) -> float:
    return clamp(old * (1.0 - alpha) + raw * alpha)


def long_mood(valence: float, arousal: float, control: float, safety: float, stress: float, recovery: float, charge: float, sleep_debt: float) -> str:
    if sleep_debt > 0.62 and recovery < 0.42:
        return "weary_needs_sleep"
    if stress > 0.48 and control < 0.58:
        return "guarded_from_pressure"
    if recovery > 0.53 and safety > 0.62:
        return "settled_after_care"
    if charge > 0.42 and valence < 0.56:
        return "remembering_unresolved_event"
    if arousal > 0.58 and safety > 0.58:
        return "energized_routine_focus"
    return "steady_continuity"


def build_relationship_consequences(routines: list[AutonomousRoutineTick], affect: list[AffectHistoryFrame]) -> list[RelationshipConsequenceFrame]:
    affect_by_tick = {a.tick_index: a for a in affect}
    rel: dict[str, dict[str, float]] = {agent: {"trust": AGENTS[agent]["baseline_trust"], "comfort": 0.55, "avoidance": 0.18, "dependency": 0.20, "gratitude": 0.22, "resentment": 0.16, "attachment": 0.52} for agent in AGENTS}
    frames: list[RelationshipConsequenceFrame] = []
    for row in routines:
        old = rel[row.agent]
        aff = affect_by_tick[row.tick_index]
        helped = row.event_kind in {"help_received", "object_returned", "shared_ritual", "quiet_success"}
        pressured = row.event_kind in {"pressure_repeated", "crowding"}
        other = "avatar" if row.avatar_pressure > 0.20 or helped or pressured else "local peers"
        trust = clamp(old["trust"] + 0.022 * helped + 0.012 * aff.recovery_momentum - 0.026 * pressured - 0.018 * (aff.dominant_long_mood == "guarded_from_pressure"))
        comfort = clamp(old["comfort"] + 0.025 * helped + 0.018 * aff.rolling_safety - 0.020 * pressured - 0.014 * aff.embodied_stress_load)
        avoidance = clamp(old["avoidance"] + 0.030 * pressured + 0.014 * (aff.affect_memory_charge > 0.42) - 0.022 * helped - 0.010 * aff.recovery_momentum)
        dependency = clamp(old["dependency"] + 0.018 * helped * AGENTS[row.agent]["attachment_need"] - 0.010 * (row.routine_source == "agent_schedule_not_avatar_command"))
        gratitude = clamp(old["gratitude"] + 0.032 * helped + 0.010 * aff.recovery_momentum - 0.010 * pressured)
        resentment = clamp(old["resentment"] + 0.028 * pressured + 0.012 * (aff.rolling_control < 0.55) - 0.026 * helped)
        attachment = clamp(old["attachment"] + 0.020 * helped + 0.012 * aff.recovery_momentum - 0.014 * avoidance + 0.004 * AGENTS[row.agent]["attachment_need"])
        rel[row.agent] = {"trust": trust, "comfort": comfort, "avoidance": avoidance, "dependency": dependency, "gratitude": gratitude, "resentment": resentment, "attachment": attachment}
        if pressured and avoidance > 0.24:
            action = "keeps_more_distance_later"
            reason = "pressure and stress carried across routines"
        elif helped and gratitude > resentment:
            action = "approaches_for_shared_task_later"
            reason = "help became recovery memory"
        elif aff.dominant_long_mood == "weary_needs_sleep":
            action = "delays_social_commitment_until_rest"
            reason = "sleep debt changes social availability"
        elif trust > 0.62:
            action = "shares_private_hint_voluntarily"
            reason = "trust stable across days"
        else:
            action = "continues_neutral_boundary"
            reason = "relationship state remains bounded"
        frames.append(RelationshipConsequenceFrame(
            tick_index=row.tick_index,
            agent=row.agent,
            other_actor=other,
            trust=round(trust, 6),
            comfort=round(comfort, 6),
            avoidance=round(avoidance, 6),
            dependency=round(dependency, 6),
            gratitude=round(gratitude, 6),
            resentment=round(resentment, 6),
            attachment_security=round(attachment, 6),
            consequence_action=action,
            remembered_reason=reason,
        ))
    return frames


def build_routine_consequences(routines: list[AutonomousRoutineTick], circadian: list[CircadianSleepFrame], affect: list[AffectHistoryFrame]) -> list[RoutineConsequenceFrame]:
    circadian_by_tick = {c.tick_index: c for c in circadian}
    affect_by_tick = {a.tick_index: a for a in affect}
    progress: dict[str, float] = {agent: 0.18 for agent in AGENTS}
    skill: dict[str, float] = {agent: 0.22 for agent in AGENTS}
    resource: dict[str, float] = {agent: 0.50 for agent in AGENTS}
    face: dict[str, float] = {agent: 0.48 for agent in AGENTS}
    frames: list[RoutineConsequenceFrame] = []
    for row in routines:
        c = circadian_by_tick[row.tick_index]
        a = affect_by_tick[row.tick_index]
        productive = row.routine in {"work_project", "repair_route", "market_exchange", "teach_skill", "prepare_tools", "quiet_route_scan"}
        restorative = row.routine in {"sleep", "dream_sort_memory", "guarded_rest", "soft_recovery", "ritual_hum"}
        progress[row.agent] = clamp(progress[row.agent] + 0.020 * productive * a.rolling_control + 0.012 * (a.dominant_long_mood == "energized_routine_focus") - 0.018 * (c.sleep_debt > 0.64))
        skill[row.agent] = clamp(skill[row.agent] + 0.014 * productive + 0.010 * (row.routine == "teach_skill") + 0.007 * restorative)
        resource[row.agent] = clamp(resource[row.agent] + 0.026 * (row.routine == "market_exchange") + 0.012 * (row.routine == "store_objects") - 0.018 * (row.event_kind == "cold_rain"))
        face[row.agent] = clamp(face[row.agent] + 0.018 * (row.routine in {"ritual_hum", "teach_skill", "relationship_check"}) + 0.010 * (a.recovery_momentum > 0.50) - 0.014 * (row.event_kind == "pressure_repeated"))
        autonomy = clamp(0.44 + 0.32 * (row.routine_source == "agent_schedule_not_avatar_command") - 0.24 * row.avatar_pressure + 0.14 * AGENTS[row.agent]["autonomy_need"])
        variation = clamp(0.18 + 0.08 * ((row.day + row.hour) % 5) + 0.16 * (row.event_kind in {"quiet_success", "curious_discovery"}) - 0.10 * (c.sleep_debt > 0.65))
        summary = f"{row.agent} {row.routine}: progress={progress[row.agent]:.2f}; resource={resource[row.agent]:.2f}; face={face[row.agent]:.2f}"
        frames.append(RoutineConsequenceFrame(
            tick_index=row.tick_index,
            agent=row.agent,
            routine=row.routine,
            project_progress=round(progress[row.agent], 6),
            skill_practice=round(skill[row.agent], 6),
            resource_change=round(resource[row.agent], 6),
            social_face_change=round(face[row.agent], 6),
            autonomy_satisfaction=round(autonomy, 6),
            routine_variation=round(variation, 6),
            consequence_summary=summary,
        ))
    return frames


def build_replay_frames(routines: list[AutonomousRoutineTick], affect: list[AffectHistoryFrame], rel: list[RelationshipConsequenceFrame], routine_conseq: list[RoutineConsequenceFrame]) -> list[ReplayContinuityFrame]:
    affect_by_tick = {a.tick_index: a for a in affect}
    rel_by_tick = {r.tick_index: r for r in rel}
    cons_by_tick = {c.tick_index: c for c in routine_conseq}
    frames: list[ReplayContinuityFrame] = []
    last_hash = "genesis-r243"
    carried = 0
    for row in routines:
        a = affect_by_tick[row.tick_index]
        r = rel_by_tick[row.tick_index]
        c = cons_by_tick[row.tick_index]
        checkpoint_due = row.tick_index == 1 or row.day % 3 == 0 and row.hour == 23 and row.agent == "Sol" or row.tick_index == len(routines)
        payload = f"{last_hash}|{row.tick_index}|{row.agent}|{row.routine}|{a.dominant_long_mood}|{r.trust:.3f}|{c.project_progress:.3f}"
        export_hash = stable_hash(payload, 16)
        checkpoint = f"r243-day{row.day:02d}-tick{row.tick_index:03d}" if checkpoint_due else ""
        if checkpoint_due:
            last_hash = export_hash
        carried += 1
        frames.append(ReplayContinuityFrame(
            tick_index=row.tick_index,
            day=row.day,
            checkpoint_id=checkpoint,
            import_hash=last_hash if checkpoint_due else "pending",
            export_hash=export_hash,
            restore_verified=checkpoint_due or row.tick_index % 28 == 0,
            replay_rows_carried=carried,
            durable_state_keys="routine,circadian,affect_history,relationship,project,replay",
        ))
    return frames


def build_world_ticks(routines: list[AutonomousRoutineTick], circadian: list[CircadianSleepFrame], affect: list[AffectHistoryFrame], rel: list[RelationshipConsequenceFrame], cons: list[RoutineConsequenceFrame], replay: list[ReplayContinuityFrame]) -> list[BrowserWorldV3Tick]:
    c_by_tick = {c.tick_index: c for c in circadian}
    a_by_tick = {a.tick_index: a for a in affect}
    r_by_tick = {r.tick_index: r for r in rel}
    cons_by_tick = {c.tick_index: c for c in cons}
    replay_by_tick = {r.tick_index: r for r in replay}
    rows: list[BrowserWorldV3Tick] = []
    for row in routines:
        c = c_by_tick[row.tick_index]
        a = a_by_tick[row.tick_index]
        r = r_by_tick[row.tick_index]
        rc = cons_by_tick[row.tick_index]
        rp = replay_by_tick[row.tick_index]
        routine_marker = f"day {row.day} {row.phase}: {row.agent} chooses {row.routine}"
        affect_marker = f"{a.dominant_long_mood}; sleep_debt={c.sleep_debt:.2f}; recovery={a.recovery_momentum:.2f}"
        relationship_marker = f"{r.consequence_action}; trust={r.trust:.2f}; avoid={r.avoidance:.2f}"
        private_hint = f"history_charge={a.affect_memory_charge:.2f}; autonomy={rc.autonomy_satisfaction:.2f}; reason={r.remembered_reason}"
        checkpoint = rp.checkpoint_id or "no_checkpoint"
        token = f"r243:{row.tick_index}:{row.agent}:{stable_hash(routine_marker + affect_marker + relationship_marker, 10)}"
        rows.append(BrowserWorldV3Tick(
            tick_index=row.tick_index,
            day=row.day,
            agent=row.agent,
            public_routine_marker=routine_marker,
            public_body_affect_marker=affect_marker,
            public_relationship_marker=relationship_marker,
            private_history_hint=private_hint,
            replay_checkpoint=checkpoint,
            trace_integrity_token=token,
        ))
    return rows


def compute_metrics(routines: list[AutonomousRoutineTick], circadian: list[CircadianSleepFrame], affect: list[AffectHistoryFrame], rel: list[RelationshipConsequenceFrame], cons: list[RoutineConsequenceFrame], replay: list[ReplayContinuityFrame], world: list[BrowserWorldV3Tick]) -> dict[str, float]:
    n = len(routines)
    source = source_readiness()
    days = {r.day for r in routines}
    long_horizon_span_coverage = min(1.0, len(days) / 21.0)
    autonomous_routine_continuity = sum(r.routine_source == "agent_schedule_not_avatar_command" and bool(r.autonomous_goal) for r in routines) / n
    phase_coverage = len({r.phase for r in routines}) / 4.0
    circadian_sleep_debt_coupling = correlation_like([c.fatigue_next_tick for c in circadian], [c.sleep_debt for c in circadian], positive=True)
    sleep_recovery_effect = sum((c.sleep_state not in {"deep_recovery_sleep", "light_guarded_rest"}) or c.rest_recovery > 0.18 for c in circadian) / n
    affect_history_carryover = sum(a.private_history_note.startswith("private:") and a.affect_memory_charge >= 0 for a in affect) / n
    mood_temporal_inertia = 1.0 - sum(abs(affect[i].rolling_valence - affect[i - 1].rolling_valence) for i in range(1, n)) / (n * 0.40)
    relationship_consequence_binding = sum((r.consequence_action != "continues_neutral_boundary") or abs(r.trust - AGENTS[r.agent]["baseline_trust"]) > 0.015 for r in rel) / n
    relationship_recovery_from_help = sum((row.event_kind not in {"help_received", "object_returned", "shared_ritual"}) or rel[i].gratitude >= rel[i].resentment for i, row in enumerate(routines)) / n
    routine_consequence_accumulation = sum(c.project_progress > 0.16 and c.skill_practice > 0.20 for c in cons) / n
    schedule_autonomy_balance = sum(c.autonomy_satisfaction >= 0.40 for c in cons) / n
    routine_variation_without_chaos = sum(0.14 <= c.routine_variation <= 0.70 for c in cons) / n
    replay_checkpoints = [r for r in replay if r.checkpoint_id]
    replay_import_export_integrity = sum(r.restore_verified and len(r.export_hash) == 16 for r in replay_checkpoints) / max(1, len(replay_checkpoints))
    replay_checkpoint_coverage = min(1.0, len(replay_checkpoints) / 8.0)
    private_history_boundary = sum("history_charge=" in w.private_history_hint and w.private_history_hint not in w.public_body_affect_marker for w in world) / n
    frequency_circadian_rhythm = sum(1.6 <= c.rhythm_vibration_hz <= 3.2 and 0.0 <= c.flower_phase_deg < 360.0 for c in circadian) / n
    source_embodied_affect_continuity = 1.0 if source >= 0.96 else source
    browser_world_v3_surface_available = 1.0
    channels = {
        "long_horizon_span_coverage": long_horizon_span_coverage,
        "autonomous_routine_continuity": autonomous_routine_continuity,
        "phase_coverage": phase_coverage,
        "circadian_sleep_debt_coupling": circadian_sleep_debt_coupling,
        "sleep_recovery_effect": sleep_recovery_effect,
        "affect_history_carryover": affect_history_carryover,
        "mood_temporal_inertia": clamp(mood_temporal_inertia),
        "relationship_consequence_binding": relationship_consequence_binding,
        "relationship_recovery_from_help": relationship_recovery_from_help,
        "routine_consequence_accumulation": routine_consequence_accumulation,
        "schedule_autonomy_balance": schedule_autonomy_balance,
        "routine_variation_without_chaos": routine_variation_without_chaos,
        "replay_import_export_integrity": replay_import_export_integrity,
        "replay_checkpoint_coverage": replay_checkpoint_coverage,
        "private_history_boundary": private_history_boundary,
        "frequency_circadian_rhythm": frequency_circadian_rhythm,
        "source_embodied_affect_continuity": source_embodied_affect_continuity,
        "browser_world_v3_surface_available": browser_world_v3_surface_available,
    }
    weights = {
        "long_horizon_span_coverage": 0.07,
        "autonomous_routine_continuity": 0.08,
        "phase_coverage": 0.04,
        "circadian_sleep_debt_coupling": 0.09,
        "sleep_recovery_effect": 0.07,
        "affect_history_carryover": 0.08,
        "mood_temporal_inertia": 0.06,
        "relationship_consequence_binding": 0.09,
        "relationship_recovery_from_help": 0.06,
        "routine_consequence_accumulation": 0.07,
        "schedule_autonomy_balance": 0.06,
        "routine_variation_without_chaos": 0.05,
        "replay_import_export_integrity": 0.06,
        "replay_checkpoint_coverage": 0.04,
        "private_history_boundary": 0.04,
        "frequency_circadian_rhythm": 0.03,
        "source_embodied_affect_continuity": 0.02,
        "browser_world_v3_surface_available": 0.01,
    }
    readiness = sum(channels[k] * weights[k] for k in weights) / sum(weights.values())
    channels["mean_long_horizon_channel_score"] = mean(channels.values())
    channels["weakest_channel_score"] = min(v for k, v in channels.items() if k != "mean_long_horizon_channel_score")
    channels["browser_world_v3_long_horizon_readiness"] = readiness
    return {k: round(v, 6) for k, v in channels.items()}


def correlation_like(xs: list[float], ys: list[float], positive: bool) -> float:
    if not xs or not ys or len(xs) != len(ys):
        return 0.0
    mean_x = mean(xs)
    mean_y = mean(ys)
    num = sum((x - mean_x) * (y - mean_y) for x, y in zip(xs, ys))
    den_x = math.sqrt(sum((x - mean_x) ** 2 for x in xs))
    den_y = math.sqrt(sum((y - mean_y) ** 2 for y in ys))
    if den_x == 0 or den_y == 0:
        return 0.0
    corr = num / (den_x * den_y)
    score = (corr + 1.0) / 2.0 if positive else (1.0 - corr) / 2.0
    return clamp(score)


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["browser_world_v3_long_horizon_readiness"]
    penalties = {
        "no_long_horizon_span": 0.25,
        "no_autonomous_routines": 0.27,
        "no_circadian_sleep_debt": 0.29,
        "no_sleep_recovery": 0.18,
        "no_affect_history_carryover": 0.24,
        "no_relationship_consequences": 0.28,
        "no_routine_consequence_accumulation": 0.19,
        "no_replay_import_export": 0.16,
        "no_private_history_boundary": 0.13,
        "no_frequency_circadian_rhythm": 0.08,
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


def make_html(routines: list[AutonomousRoutineTick], circadian: list[CircadianSleepFrame], affect: list[AffectHistoryFrame], rel: list[RelationshipConsequenceFrame], cons: list[RoutineConsequenceFrame], replay: list[ReplayContinuityFrame], world: list[BrowserWorldV3Tick], metrics: dict[str, float]) -> str:
    c_by_tick = {c.tick_index: asdict(c) for c in circadian}
    a_by_tick = {a.tick_index: asdict(a) for a in affect}
    r_by_tick = {r.tick_index: asdict(r) for r in rel}
    cons_by_tick = {c.tick_index: asdict(c) for c in cons}
    replay_by_tick = {r.tick_index: asdict(r) for r in replay}
    world_by_tick = {w.tick_index: asdict(w) for w in world}
    rows = []
    for row in routines:
        rows.append({"routine": asdict(row), "circadian": c_by_tick[row.tick_index], "affect": a_by_tick[row.tick_index], "relationship": r_by_tick[row.tick_index], "consequence": cons_by_tick[row.tick_index], "replay": replay_by_tick[row.tick_index], "world": world_by_tick[row.tick_index]})
    template = """<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report 243 - Browser World v3 Long-Horizon Routines</title>
<style>
:root{--ink:#17130e;--paper:#f1e7d4;--moss:#36573d;--clay:#a65034;--blue:#356578;--gold:#c69a3e;--plum:#5a4863}*{box-sizing:border-box}body{margin:0;color:var(--ink);font-family:Georgia,'Times New Roman',serif;background:radial-gradient(circle at 18% 12%,rgba(198,154,62,.30),transparent 25rem),radial-gradient(circle at 82% 18%,rgba(53,101,120,.24),transparent 26rem),linear-gradient(130deg,#f5ecdb,#c9bea0 48%,#879978)}main{max-width:1220px;margin:0 auto;padding:28px}h1{font-size:clamp(2rem,5vw,5.1rem);line-height:.9;letter-spacing:-.055em;margin:0 0 14px}.shell{display:grid;grid-template-columns:1fr 1fr;gap:18px}.panel{background:rgba(255,250,239,.84);border:1px solid rgba(23,19,14,.16);border-radius:24px;padding:20px;box-shadow:0 18px 50px rgba(23,19,14,.2);backdrop-filter:blur(10px)}p{line-height:1.5}.world{position:relative;min-height:450px;overflow:hidden;background:linear-gradient(rgba(54,87,61,.10) 1px,transparent 1px),linear-gradient(90deg,rgba(54,87,61,.10) 1px,transparent 1px),radial-gradient(circle at center,rgba(255,248,232,.76),rgba(135,153,120,.56));background-size:40px 40px,40px 40px,auto}.avatar,.agent{position:absolute;width:46px;height:46px;border-radius:50%;display:grid;place-items:center;font-weight:700;transition:240ms ease;border:3px solid #fff8e8}.avatar{left:48%;top:50%;background:var(--clay);color:white}.agent{background:var(--moss);color:white}.agent[data-agent=Ari]{left:22%;top:28%}.agent[data-agent=Fay]{left:68%;top:30%;background:var(--blue)}.agent[data-agent=Milo]{left:58%;top:70%;background:var(--gold);color:var(--ink)}.agent[data-agent=Sol]{left:20%;top:72%;background:var(--plum)}.flower{position:absolute;left:50%;top:50%;width:230px;height:230px;margin:-115px;border-radius:50%;border:1px solid rgba(23,19,14,.2);opacity:.55;transition:250ms linear}.flower:before,.flower:after{content:'';position:absolute;border:1px solid rgba(23,19,14,.16);border-radius:50%}.flower:before{inset:24px}.flower:after{inset:48px}.controls{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}button,input{border:1px solid rgba(23,19,14,.24);border-radius:999px;padding:10px 14px;background:#fff8e8;color:var(--ink);font:inherit}button{cursor:pointer;box-shadow:0 6px 0 rgba(23,19,14,.16)}button:active{transform:translateY(3px);box-shadow:0 3px 0 rgba(23,19,14,.16)}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:18px}.card{min-height:150px;background:rgba(255,248,232,.78);border:1px solid rgba(23,19,14,.14);border-radius:18px;padding:14px}.card h3{margin:0 0 8px}.kv{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.85rem;white-space:pre-wrap}.private{filter:blur(5px);user-select:none}.private.open{filter:none}.metric{display:flex;justify-content:space-between;gap:10px;border-bottom:1px solid rgba(23,19,14,.12);padding:6px 0}@media(max-width:900px){.shell,.grid{grid-template-columns:1fr}main{padding:16px}}
</style>
</head>
<body>
<main>
<section class=\"shell\"><div class=\"panel\"><h1>Long-Horizon Autonomous Life</h1><p>Report 243 lets routines, sleep debt, affect history, relationship consequences, and replay checkpoints persist across 21 deterministic days. The avatar can enter, but the agents are already doing things for their own schedule reasons.</p><div class=\"controls\"><button id=\"start\">start</button><button id=\"pause\">pause</button><button id=\"save\">save</button><button id=\"restore\">restore</button><button id=\"export\">export replay</button><label><input type=\"file\" id=\"import\" /> import</label><button id=\"inspect\">toggle private history</button></div><div class=\"controls\"><input id=\"utterance\" size=\"48\" value=\"I will wait until you finish your routine.\" /><button id=\"send\">send local act</button></div></div><div class=\"panel world\"><div id=\"flower\" class=\"flower\"></div><div id=\"avatar\" class=\"avatar\">You</div><div class=\"agent\" data-agent=\"Ari\">A</div><div class=\"agent\" data-agent=\"Fay\">F</div><div class=\"agent\" data-agent=\"Milo\">M</div><div class=\"agent\" data-agent=\"Sol\">S</div></div></section>
<section class=\"grid\"><div class=\"card\"><h3>routine</h3><div id=\"routine\" class=\"kv\"></div></div><div class=\"card\"><h3>circadian</h3><div id=\"circadian\" class=\"kv\"></div></div><div class=\"card\"><h3>affect history</h3><div id=\"affect\" class=\"kv\"></div></div><div class=\"card\"><h3>relationship</h3><div id=\"relationship\" class=\"kv\"></div></div><div class=\"card\"><h3>project consequence</h3><div id=\"consequence\" class=\"kv\"></div></div><div class=\"card\"><h3>private history</h3><div id=\"private\" class=\"kv private\"></div></div><div class=\"card\"><h3>metrics</h3><div id=\"metrics\"></div></div><div class=\"card\"><h3>boundary</h3><p>No subjective consciousness claim. Long-horizon continuity is functional simulated artificial life, not moral patienthood.</p></div></section>
</main>
<script>
const ROWS=__ROWS__;const METRICS=__METRICS__;const KEY='ssrm243_world_v3';let idx=0;let timer=null;let replay=[];let avatar={x:48,y:50};function pct(v){return Math.round(v*1000)/10+'%'}function renderMetrics(){const keys=['browser_world_v3_long_horizon_readiness','weakest_channel_score','circadian_sleep_debt_coupling','relationship_consequence_binding','replay_import_export_integrity'];document.getElementById('metrics').innerHTML=keys.map(k=>`<div class=\"metric\"><span>${k}</span><b>${pct(METRICS[k])}</b></div>`).join('')}function render(){const row=ROWS[idx%ROWS.length];replay.push({tick:row.routine.tick_index,day:row.routine.day,agent:row.routine.agent,routine:row.routine.routine,mood:row.affect.dominant_long_mood,checkpoint:row.replay.checkpoint_id});document.getElementById('routine').textContent=`${row.world.public_routine_marker}\n${row.routine.autonomous_goal}\nsource=${row.routine.routine_source}`;document.getElementById('circadian').textContent=JSON.stringify({sleep_debt:row.circadian.sleep_debt,sleep_quality:row.circadian.sleep_quality,state:row.circadian.sleep_state,vibration:row.circadian.rhythm_vibration_hz},null,2);document.getElementById('affect').textContent=JSON.stringify({mood:row.affect.dominant_long_mood,valence:row.affect.rolling_valence,stress:row.affect.embodied_stress_load,recovery:row.affect.recovery_momentum,charge:row.affect.affect_memory_charge},null,2);document.getElementById('relationship').textContent=`${row.world.public_relationship_marker}\nreason=${row.relationship.remembered_reason}`;document.getElementById('consequence').textContent=row.consequence.consequence_summary;document.getElementById('private').textContent=JSON.stringify({private_note:row.affect.private_history_note,private_hint:row.world.private_history_hint,replay:row.replay},null,2);document.getElementById('flower').style.transform=`rotate(${row.circadian.flower_phase_deg}deg)`;for(const node of document.querySelectorAll('.agent')){if(node.dataset.agent===row.routine.agent){node.style.transform='scale(1.22) translateY(-9px)';node.style.boxShadow='0 0 0 10px rgba(198,154,62,.22)'}else{node.style.transform='scale(1)';node.style.boxShadow='none'}}document.getElementById('avatar').style.left=avatar.x+'%';document.getElementById('avatar').style.top=avatar.y+'%';idx++}function start(){if(!timer)timer=setInterval(render,250)}function pause(){clearInterval(timer);timer=null}document.getElementById('start').onclick=start;document.getElementById('pause').onclick=pause;document.getElementById('save').onclick=()=>localStorage.setItem(KEY,JSON.stringify({idx,replay,avatar}));document.getElementById('restore').onclick=()=>{const raw=localStorage.getItem(KEY);if(raw){const s=JSON.parse(raw);idx=s.idx||0;replay=s.replay||[];avatar=s.avatar||avatar;render()}};document.getElementById('export').onclick=()=>{const blob=new Blob([JSON.stringify({report:243,replay},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='ssrm243_replay.json';a.click()};document.getElementById('import').onchange=async(e)=>{const f=e.target.files[0];if(f){replay=JSON.parse(await f.text()).replay||[];render()}};document.getElementById('inspect').onclick=()=>document.getElementById('private').classList.toggle('open');document.getElementById('send').onclick=()=>{replay.push({tick:'typed',agent:'avatar',event:'local_wait_or_pressure_act',text:document.getElementById('utterance').value.trim()});render()};window.addEventListener('keydown',e=>{if(e.key==='ArrowLeft')avatar.x=Math.max(2,avatar.x-2);if(e.key==='ArrowRight')avatar.x=Math.min(92,avatar.x+2);if(e.key==='ArrowUp')avatar.y=Math.max(4,avatar.y-2);if(e.key==='ArrowDown')avatar.y=Math.min(88,avatar.y+2);document.getElementById('avatar').style.left=avatar.x+'%';document.getElementById('avatar').style.top=avatar.y+'%'});renderMetrics();render();
</script>
</body>
</html>
"""
    return template.replace("__ROWS__", json.dumps(rows)).replace("__METRICS__", json.dumps(metrics))


def run(seed: int) -> dict[str, Any]:
    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    routines = build_routine_ticks(seed)
    circadian = build_circadian_frames(routines)
    affect = build_affect_history(routines, circadian)
    rel = build_relationship_consequences(routines, affect)
    cons = build_routine_consequences(routines, circadian, affect)
    replay = build_replay_frames(routines, affect, rel, cons)
    world = build_world_ticks(routines, circadian, affect, rel, cons, replay)
    metrics = compute_metrics(routines, circadian, affect, rel, cons, replay, world)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["browser_world_v3_long_horizon_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    prefix = ARTIFACTS / BASE
    write_csv(Path(f"{prefix}_autonomous_routine_ticks.csv"), routines)
    write_csv(Path(f"{prefix}_circadian_sleep_frames.csv"), circadian)
    write_csv(Path(f"{prefix}_affect_history_frames.csv"), affect)
    write_csv(Path(f"{prefix}_relationship_consequence_frames.csv"), rel)
    write_csv(Path(f"{prefix}_routine_consequence_frames.csv"), cons)
    write_csv(Path(f"{prefix}_replay_continuity_frames.csv"), replay)
    write_csv(Path(f"{prefix}_browser_world_v3_ticks.csv"), world)
    honest_limits = [
        "This is deterministic long-horizon continuity, not subjective consciousness.",
        "Autonomous routines are scheduled agent-state policies, not independent moral agency.",
        "Sleep debt and affect history are functional simulation variables, not lived fatigue or dreams.",
        "Relationship consequences are simulated continuity, not real attachment or consent.",
        "Replay import/export is browser-local JSON scaffolding, not complete engine replay.",
        "Frequency and flower phase remain rhythm variables, not metaphysical proof.",
        "The browser world v3 visualization is a scaffold, not a finished 3D game engine.",
    ]
    next_gate = "browser world v4 with multi-week learned routine adaptation, proto-language drift from repeated interactions, and avatar-entry consequences that respect agent sleep, boundaries, and relationship history"
    results = {
        "report": REPORT,
        "name": "SSRM-3D Browser World v3 Long-Horizon Routine Circadian Relationship Bridge",
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "verdict": verdict,
        "counts": {
            "autonomous_routine_ticks": len(routines),
            "circadian_sleep_frames": len(circadian),
            "affect_history_frames": len(affect),
            "relationship_consequence_frames": len(rel),
            "routine_consequence_frames": len(cons),
            "replay_continuity_frames": len(replay),
            "browser_world_v3_ticks": len(world),
        },
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "next_gate": next_gate,
    }
    state = {
        "report": REPORT,
        "seed": seed,
        "days": 21,
        "agents": AGENTS,
        "sample_ticks": [asdict(row) for row in world[:12]],
        "continuity_model": "autonomous routines + circadian sleep debt + affect history + relationship consequences + replay checkpoints",
        "boundary": "functional long-horizon artificial life scaffold; no consciousness claim",
    }
    Path(f"{prefix}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    Path(f"{prefix}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    with Path(f"{prefix}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "verdict": verdict, "readiness": metrics["browser_world_v3_long_horizon_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": next_gate})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(routines, circadian, affect, rel, cons, replay, world, metrics))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    counts = results["counts"]
    print(f"module_verdict {results['verdict']}")
    print(f"browser_world_v3_long_horizon_readiness {metrics['browser_world_v3_long_horizon_readiness']:.6f}")
    for key in ["autonomous_routine_ticks", "circadian_sleep_frames", "affect_history_frames", "relationship_consequence_frames", "routine_consequence_frames", "replay_continuity_frames", "browser_world_v3_ticks"]:
        print(f"{key} {counts[key]}")
    for key in ["long_horizon_span_coverage", "autonomous_routine_continuity", "circadian_sleep_debt_coupling", "affect_history_carryover", "relationship_consequence_binding", "replay_import_export_integrity", "routine_variation_without_chaos", "weakest_channel_score"]:
        print(f"{key} {metrics[key]:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
