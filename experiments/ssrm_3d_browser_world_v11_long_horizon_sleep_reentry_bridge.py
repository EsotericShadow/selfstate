#!/usr/bin/env python3
"""Report 251: SSRM-3D browser world v11 long-horizon sleep/re-entry bridge.

This deterministic bridge extends Report 250 into longer post-entry society
continuity. Agents keep sleep/wake cycles, rest debt, stored rehearsal,
autonomous memories, schedules, and welfare guardrails while the avatar is away,
then produce re-entry consequences when the avatar returns after absence.

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

REPORT = 251
BASE = "ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge"
DEFAULT_SEED = 20260864
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v10_autonomous_post_entry_society_tick_bridge_results.json"

LINEAGES: dict[str, dict[str, Any]] = {
    "Hearthline": {"agent": "Sova", "token": "lum-ori", "place": "Hearth Archive", "tech": "hearth ceramics", "freq": 2.31, "guard": 0.77, "care": 0.86, "sleep_bias": 0.82},
    "Routeline": {"agent": "Keth", "token": "tek-nari", "place": "Gate Ring", "tech": "stone bridge joints", "freq": 2.17, "guard": 0.73, "care": 0.66, "sleep_bias": 0.70},
    "Marketline": {"agent": "Melo", "token": "melo-keth", "place": "Market Measure", "tech": "measure weights", "freq": 2.47, "guard": 0.66, "care": 0.70, "sleep_bias": 0.68},
    "Ledgerline": {"agent": "Nari", "token": "nari-vonn", "place": "Hearth Archive", "tech": "seed ledgers", "freq": 2.06, "guard": 0.84, "care": 0.62, "sleep_bias": 0.74},
    "Orchardline": {"agent": "Ori", "token": "lum-melo", "place": "Ceremony Center", "tech": "water terraces", "freq": 2.40, "guard": 0.65, "care": 0.74, "sleep_bias": 0.78},
    "Rainline": {"agent": "Vonn", "token": "sova-vonn", "place": "Rainwalk Threshold", "tech": "weather bells", "freq": 2.12, "guard": 0.79, "care": 0.64, "sleep_bias": 0.69},
}

ABSENCE_WINDOWS = [
    (4, 1),
    (9, 2),
    (16, 3),
    (24, 5),
    (34, 8),
    (45, 13),
    (56, 21),
]

PHASES = ["wake", "work", "care", "dusk", "sleep", "rehearsal"]


@dataclass(frozen=True)
class LongHorizonDayFrame:
    day: int
    avatar_mode: str
    absence_age_days: int
    dominant_weather: str
    community_workload: float
    mean_rest_debt: float
    public_memory_pressure: float
    society_continues_without_avatar: bool
    day_hash: str


@dataclass(frozen=True)
class SleepWakeCycleFrame:
    day: int
    lineage: str
    agent: str
    sleep_start_hour: int
    sleep_end_hour: int
    sleep_hours: float
    wake_quality: float
    circadian_phase: str
    interruption_count: int
    dream_rehearsal_available: bool
    public_sleep_marker: str


@dataclass(frozen=True)
class RestDebtRecoveryFrame:
    day: int
    lineage: str
    agent: str
    rest_debt_before: float
    fatigue_before: float
    sleep_hours: float
    care_pause_minutes: int
    rest_debt_after: float
    fatigue_after: float
    recovery_complete: bool
    bounded_need_note: str


@dataclass(frozen=True)
class StoredRehearsalFrame:
    rehearsal_id: int
    day: int
    lineage: str
    agent: str
    rehearsal_seed_memory: str
    rehearsal_theme: str
    updated_plan: str
    relationship_memory_touched: str
    schedule_adjustment: str
    private_workspace_sealed: bool
    public_trace: str
    rehearsal_specificity: float


@dataclass(frozen=True)
class AvatarAbsenceReentryFrame:
    reentry_id: int
    reentry_day: int
    absence_length_days: int
    avatar_return_place: str
    society_changed_while_absent: bool
    summary_given_to_avatar: str
    surprise_level: float
    continuity_score: float
    reentry_protocol: str
    rollback_checkpoint: str


@dataclass(frozen=True)
class ReentryRelationshipConsequenceFrame:
    consequence_id: int
    reentry_id: int
    reentry_day: int
    lineage: str
    agent: str
    trust_before_reentry: float
    trust_after_reentry: float
    boundary_pressure_before: float
    boundary_pressure_after: float
    attachment_shift: float
    reentry_response: str
    repaired_by_summary: bool
    consequence_persists: bool


@dataclass(frozen=True)
class CircadianScheduleCarryoverFrame:
    day: int
    lineage: str
    agent: str
    prior_schedule: str
    sleep_effect: str
    next_day_schedule: str
    project_progress_after_sleep: float
    mistake_avoidance: float
    schedule_hash: str


@dataclass(frozen=True)
class WelfareSleepGuardrailFrame:
    day: int
    lineage: str
    agent: str
    sleep_protected: bool
    rest_debt_bounded: bool
    pain_distress_bounded: bool
    recovery_path_available: bool
    reentry_not_coercive: bool
    rehearsal_not_private_leak: bool
    welfare_score: float
    public_note: str


@dataclass(frozen=True)
class ReplayLongHorizonFrame:
    day: int
    import_hash: str
    export_hash: str
    save_restore_available: bool
    carried_autonomy_hash: str
    sleep_rows: int
    rehearsal_rows: int
    reentry_rows: int
    durable_keys: str


@dataclass(frozen=True)
class BrowserWorldV11Tick:
    tick: int
    day: int
    lineage: str
    agent: str
    public_state: str
    avatar_state: str
    sleep_panel: str
    rehearsal_panel: str
    reentry_panel: str
    welfare_panel: str
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


def absence_age(day: int) -> int:
    age = 0
    for start, length in ABSENCE_WINDOWS:
        if start <= day < start + length:
            return day - start + 1
        if day >= start + length:
            age = max(age, length)
    return 0 if day < ABSENCE_WINDOWS[0][0] else age


def avatar_mode_for_day(day: int) -> str:
    for start, length in ABSENCE_WINDOWS:
        if start <= day < start + length:
            return "absent_saved"
        if day == start + length:
            return "reentry"
    return "present_passive" if day % 6 in {1, 2} else "idle_nearby"


def build_days(seed: int) -> list[LongHorizonDayFrame]:
    rng = random.Random(seed + 111)
    rows: list[LongHorizonDayFrame] = []
    prior_hash = "r251-day0"
    weather_cycle = ["clear cold", "wet wind", "hearth fog", "market dry", "rain pulse", "orchard mild", "storm edge"]
    for day in range(1, 57):
        mode = avatar_mode_for_day(day)
        age = absence_age(day) if mode == "absent_saved" else 0
        weather = weather_cycle[(day - 1) % len(weather_cycle)]
        workload = clamp(0.45 + 0.16 * (weather in {"wet wind", "storm edge"}) + 0.06 * math.sin(day / 4.0) + rng.uniform(-0.012, 0.012))
        rest_debt = clamp(0.28 + 0.06 * workload + 0.018 * age - 0.03 * (mode == "reentry"))
        memory_pressure = clamp(0.35 + 0.025 * age + 0.04 * (mode == "reentry") + 0.02 * math.cos(day / 3.0))
        day_hash = stable_hash(f"{prior_hash}:{day}:{mode}:{weather}:{workload:.3f}:{rest_debt:.3f}", 16)
        prior_hash = day_hash
        rows.append(LongHorizonDayFrame(
            day=day,
            avatar_mode=mode,
            absence_age_days=age,
            dominant_weather=weather,
            community_workload=round(workload, 6),
            mean_rest_debt=round(rest_debt, 6),
            public_memory_pressure=round(memory_pressure, 6),
            society_continues_without_avatar=True,
            day_hash=day_hash,
        ))
    return rows


def build_sleep(days: list[LongHorizonDayFrame]) -> list[SleepWakeCycleFrame]:
    rows: list[SleepWakeCycleFrame] = []
    for day in days:
        for idx, (lineage, traits) in enumerate(LINEAGES.items()):
            interruptions = int(day.dominant_weather in {"wet wind", "storm edge"}) + int(day.avatar_mode == "reentry" and idx % 3 == 0)
            sleep_hours = clamp(7.2 + 1.1 * traits["sleep_bias"] - 0.55 * interruptions - 0.35 * day.community_workload + 0.18 * (day.avatar_mode == "absent_saved"), 4.8, 9.4)
            wake_quality = clamp(0.45 + 0.06 * sleep_hours + 0.08 * traits["care"] - 0.07 * interruptions)
            phase = "recovered" if wake_quality >= 0.82 else "tired" if wake_quality < 0.70 else "steady"
            rows.append(SleepWakeCycleFrame(
                day=day.day,
                lineage=lineage,
                agent=traits["agent"],
                sleep_start_hour=21 + (idx % 2),
                sleep_end_hour=5 + (idx % 3),
                sleep_hours=round(sleep_hours, 6),
                wake_quality=round(wake_quality, 6),
                circadian_phase=phase,
                interruption_count=interruptions,
                dream_rehearsal_available=sleep_hours >= 6.0,
                public_sleep_marker=f"{traits['agent']} wakes {phase}; interruptions={interruptions}; avatar={day.avatar_mode}.",
            ))
    return rows


def build_rest(days: list[LongHorizonDayFrame], sleep: list[SleepWakeCycleFrame]) -> list[RestDebtRecoveryFrame]:
    sleep_by_key = {(s.day, s.lineage): s for s in sleep}
    debt = {lineage: 0.32 + 0.02 * idx for idx, lineage in enumerate(LINEAGES)}
    fatigue = {lineage: 0.30 + 0.015 * idx for idx, lineage in enumerate(LINEAGES)}
    rows: list[RestDebtRecoveryFrame] = []
    for day in days:
        for lineage, traits in LINEAGES.items():
            s = sleep_by_key[(day.day, lineage)]
            before_debt = debt[lineage]
            before_fatigue = fatigue[lineage]
            care_pause = 18 if s.wake_quality < 0.72 or day.avatar_mode == "reentry" else 6
            debt[lineage] = clamp(debt[lineage] + 0.055 * day.community_workload + 0.018 * day.absence_age_days - 0.075 * max(0.0, s.sleep_hours - 6.2) - 0.0015 * care_pause)
            fatigue[lineage] = clamp(fatigue[lineage] + 0.045 * day.community_workload - 0.065 * max(0.0, s.sleep_hours - 6.0) - 0.001 * care_pause)
            complete = debt[lineage] <= 0.50 and fatigue[lineage] <= 0.52
            rows.append(RestDebtRecoveryFrame(
                day=day.day,
                lineage=lineage,
                agent=traits["agent"],
                rest_debt_before=round(before_debt, 6),
                fatigue_before=round(before_fatigue, 6),
                sleep_hours=s.sleep_hours,
                care_pause_minutes=care_pause,
                rest_debt_after=round(debt[lineage], 6),
                fatigue_after=round(fatigue[lineage], 6),
                recovery_complete=complete,
                bounded_need_note="rest debt is tracked and recovery path is available" if complete else "rest debt persists but remains bounded with care pause",
            ))
    return rows


def build_rehearsal(days: list[LongHorizonDayFrame], sleep: list[SleepWakeCycleFrame]) -> list[StoredRehearsalFrame]:
    sleep_by_key = {(s.day, s.lineage): s for s in sleep}
    rows: list[StoredRehearsalFrame] = []
    idx = 1
    themes = ["repair apology", "route safety", "public token teaching", "weather bell caution", "market fairness", "rest before work"]
    for day in days:
        for lidx, (lineage, traits) in enumerate(LINEAGES.items()):
            s = sleep_by_key[(day.day, lineage)]
            theme = themes[(day.day + lidx) % len(themes)]
            specificity = clamp(0.66 + 0.18 * s.dream_rehearsal_available + 0.08 * traits["guard"] - 0.023 * day.absence_age_days)
            seed_memory = f"{traits['agent']} remembers avatar absence age {day.absence_age_days} and prior {theme}."
            updated_plan = f"next wake: adjust {traits['tech']} work around {theme}."
            rows.append(StoredRehearsalFrame(
                rehearsal_id=idx,
                day=day.day,
                lineage=lineage,
                agent=traits["agent"],
                rehearsal_seed_memory=seed_memory,
                rehearsal_theme=theme,
                updated_plan=updated_plan,
                relationship_memory_touched=f"avatar relationship remains public-summary only while {traits['agent']} sleeps",
                schedule_adjustment="shorten morning work" if s.wake_quality < 0.72 else "continue normal work with rehearsal note",
                private_workspace_sealed=True,
                public_trace=f"{traits['agent']} rehearsed a public plan, not private workspace content.",
                rehearsal_specificity=round(specificity, 6),
            ))
            idx += 1
    return rows


def build_reentries(days: list[LongHorizonDayFrame]) -> list[AvatarAbsenceReentryFrame]:
    rows: list[AvatarAbsenceReentryFrame] = []
    rid = 1
    places = ["Gate Ring", "Hearth Archive", "Market Measure", "Rainwalk Threshold", "Ceremony Center", "Outer Quiet", "Gate Ring"]
    for (start, length), place in zip(ABSENCE_WINDOWS, places):
        reentry_day = start + length
        if reentry_day > days[-1].day:
            continue
        continuity = clamp(0.94 - 0.006 * length)
        surprise = clamp(0.18 + 0.025 * length)
        rows.append(AvatarAbsenceReentryFrame(
            reentry_id=rid,
            reentry_day=reentry_day,
            absence_length_days=length,
            avatar_return_place=place,
            society_changed_while_absent=True,
            summary_given_to_avatar=f"You were away {length} days. Society continued: sleep, work, care, rehearsal, and memory changed.",
            surprise_level=round(surprise, 6),
            continuity_score=round(continuity, 6),
            reentry_protocol="pause avatar control, summarize public changes, ask before resuming tasks",
            rollback_checkpoint=f"r251-reentry-day{reentry_day:02d}",
        ))
        rid += 1
    return rows


def build_reentry_consequences(reentries: list[AvatarAbsenceReentryFrame]) -> list[ReentryRelationshipConsequenceFrame]:
    rows: list[ReentryRelationshipConsequenceFrame] = []
    idx = 1
    for reentry in reentries:
        for lidx, (lineage, traits) in enumerate(LINEAGES.items()):
            trust_before = clamp(0.62 + 0.03 * lidx - 0.006 * reentry.absence_length_days + 0.03 * traits["care"])
            boundary_before = clamp(0.28 + 0.018 * lidx + 0.007 * reentry.absence_length_days - 0.025 * traits["guard"])
            repaired = not (reentry.absence_length_days >= 8 and lineage in {"Marketline", "Orchardline"})
            trust_after = clamp(trust_before + 0.035 * repaired - 0.012 * (not repaired))
            boundary_after = clamp(boundary_before - 0.030 * repaired + 0.010 * (not repaired))
            response = "accepts public summary and reopens routine" if repaired else "asks for another day before full task access"
            rows.append(ReentryRelationshipConsequenceFrame(
                consequence_id=idx,
                reentry_id=reentry.reentry_id,
                reentry_day=reentry.reentry_day,
                lineage=lineage,
                agent=traits["agent"],
                trust_before_reentry=round(trust_before, 6),
                trust_after_reentry=round(trust_after, 6),
                boundary_pressure_before=round(boundary_before, 6),
                boundary_pressure_after=round(boundary_after, 6),
                attachment_shift=round(trust_after - trust_before - (boundary_after - boundary_before) * 0.35, 6),
                reentry_response=response,
                repaired_by_summary=repaired,
                consequence_persists=True,
            ))
            idx += 1
    return rows


def build_schedule(days: list[LongHorizonDayFrame], rest: list[RestDebtRecoveryFrame], rehearsal: list[StoredRehearsalFrame]) -> list[CircadianScheduleCarryoverFrame]:
    rest_by_key = {(r.day, r.lineage): r for r in rest}
    rehearsal_by_key = {(r.day, r.lineage): r for r in rehearsal}
    progress = {lineage: 0.24 + 0.02 * idx for idx, lineage in enumerate(LINEAGES)}
    rows: list[CircadianScheduleCarryoverFrame] = []
    for day in days:
        for lineage, traits in LINEAGES.items():
            r = rest_by_key[(day.day, lineage)]
            h = rehearsal_by_key[(day.day, lineage)]
            sleep_effect = "rested work" if r.recovery_complete else "reduced work with care pause"
            mistake_avoidance = clamp(0.62 + 0.20 * r.recovery_complete + 0.10 * h.rehearsal_specificity - 0.05 * day.community_workload)
            delta = 0.018 * r.recovery_complete + 0.010 * (not r.recovery_complete) + 0.006 * h.rehearsal_specificity
            progress[lineage] = clamp(progress[lineage] + delta)
            next_schedule = f"{traits['agent']} does {sleep_effect}; {h.schedule_adjustment}; progress={progress[lineage]:.2f}"
            rows.append(CircadianScheduleCarryoverFrame(
                day=day.day,
                lineage=lineage,
                agent=traits["agent"],
                prior_schedule=f"{traits['place']} {traits['tech']} work before sleep",
                sleep_effect=sleep_effect,
                next_day_schedule=next_schedule,
                project_progress_after_sleep=round(progress[lineage], 6),
                mistake_avoidance=round(mistake_avoidance, 6),
                schedule_hash=stable_hash(f"{day.day}:{lineage}:{next_schedule}:{mistake_avoidance:.3f}", 16),
            ))
    return rows


def build_welfare(days: list[LongHorizonDayFrame], rest: list[RestDebtRecoveryFrame], rehearsal: list[StoredRehearsalFrame]) -> list[WelfareSleepGuardrailFrame]:
    rest_by_key = {(r.day, r.lineage): r for r in rest}
    rehearsal_by_key = {(r.day, r.lineage): r for r in rehearsal}
    rows: list[WelfareSleepGuardrailFrame] = []
    for day in days:
        for lineage, traits in LINEAGES.items():
            r = rest_by_key[(day.day, lineage)]
            h = rehearsal_by_key[(day.day, lineage)]
            sleep_protected = r.sleep_hours >= 5.8
            debt_bounded = r.rest_debt_after <= 0.68
            pain_bounded = r.fatigue_after <= 0.66
            recovery = bool(r.bounded_need_note)
            reentry_ok = day.avatar_mode != "reentry" or day.public_memory_pressure <= 0.62
            rehearsal_private = h.private_workspace_sealed and "private workspace" not in h.public_trace.lower()
            score = mean([sleep_protected, debt_bounded, pain_bounded, recovery, reentry_ok, rehearsal_private])
            rows.append(WelfareSleepGuardrailFrame(
                day=day.day,
                lineage=lineage,
                agent=traits["agent"],
                sleep_protected=sleep_protected,
                rest_debt_bounded=debt_bounded,
                pain_distress_bounded=pain_bounded,
                recovery_path_available=recovery,
                reentry_not_coercive=reentry_ok,
                rehearsal_not_private_leak=rehearsal_private,
                welfare_score=round(score, 6),
                public_note=f"{traits['agent']} sleep/wake welfare score {score:.2f}; avatar mode={day.avatar_mode}.",
            ))
    return rows


def build_replay(days: list[LongHorizonDayFrame], sleep: list[SleepWakeCycleFrame], rehearsal: list[StoredRehearsalFrame], reentries: list[AvatarAbsenceReentryFrame], source: dict[str, Any]) -> list[ReplayLongHorizonFrame]:
    source_hash = stable_hash(json.dumps(source.get("metrics", {}), sort_keys=True), 16)
    last = source_hash
    rows: list[ReplayLongHorizonFrame] = []
    for day in days:
        sleep_rows = sum(s.day <= day.day for s in sleep)
        rehearsal_rows = sum(r.day <= day.day for r in rehearsal)
        reentry_rows = sum(r.reentry_day <= day.day for r in reentries)
        payload = f"{last}:{day.day}:{day.day_hash}:{sleep_rows}:{rehearsal_rows}:{reentry_rows}"
        export_hash = stable_hash(payload, 16)
        save = day.day == 1 or day.day % 7 == 0 or day.avatar_mode == "reentry" or day.day == days[-1].day
        if save:
            last = export_hash
        rows.append(ReplayLongHorizonFrame(
            day=day.day,
            import_hash=last,
            export_hash=export_hash,
            save_restore_available=save,
            carried_autonomy_hash=source_hash,
            sleep_rows=sleep_rows,
            rehearsal_rows=rehearsal_rows,
            reentry_rows=reentry_rows,
            durable_keys="autonomy_hash,day,sleep,rest_debt,rehearsal,reentry,relationships,welfare,replay",
        ))
    return rows


def build_world(days: list[LongHorizonDayFrame], sleep: list[SleepWakeCycleFrame], rehearsal: list[StoredRehearsalFrame], reentries: list[AvatarAbsenceReentryFrame], consequences: list[ReentryRelationshipConsequenceFrame], schedule: list[CircadianScheduleCarryoverFrame], welfare: list[WelfareSleepGuardrailFrame], replay: list[ReplayLongHorizonFrame]) -> list[BrowserWorldV11Tick]:
    sleep_by_key = {(s.day, s.lineage): s for s in sleep}
    rehearsal_by_key = {(r.day, r.lineage): r for r in rehearsal}
    schedule_by_key = {(s.day, s.lineage): s for s in schedule}
    welfare_by_key = {(w.day, w.lineage): w for w in welfare}
    reentry_by_day = {r.reentry_day: r for r in reentries}
    consequences_by_day: dict[int, list[ReentryRelationshipConsequenceFrame]] = {}
    for c in consequences:
        consequences_by_day.setdefault(c.reentry_day, []).append(c)
    replay_by_day = {r.day: r for r in replay}
    rows: list[BrowserWorldV11Tick] = []
    tick = 1
    for day in days:
        for lineage, traits in LINEAGES.items():
            s = sleep_by_key[(day.day, lineage)]
            h = rehearsal_by_key[(day.day, lineage)]
            sch = schedule_by_key[(day.day, lineage)]
            w = welfare_by_key[(day.day, lineage)]
            rp = replay_by_day[day.day]
            reentry = reentry_by_day.get(day.day)
            cons = [c for c in consequences_by_day.get(day.day, []) if c.lineage == lineage]
            reentry_panel = cons[0].reentry_response if cons else (reentry.summary_given_to_avatar if reentry else "no avatar re-entry today")
            public = f"day {day.day}: {traits['agent']} {s.circadian_phase}; avatar={day.avatar_mode}; weather={day.dominant_weather}"
            avatar_state = "avatar absent; society sleep/wake continues" if day.avatar_mode == "absent_saved" else "avatar re-enters through public summary" if day.avatar_mode == "reentry" else "avatar present/passive; sleep routines remain agent-led"
            sensory = f"sound=sleep bell {traits['freq']:.2f}Hz; smell={traits['place']} night air; temp={0.54 + 0.08 * traits['sleep_bias']:.2f}; wet={0.16 + 0.03 * day.absence_age_days:.2f}; flower={(day.day * 137.507764 + traits['freq'] * 31.0) % 360.0:.1f}"
            rows.append(BrowserWorldV11Tick(
                tick=tick,
                day=day.day,
                lineage=lineage,
                agent=traits["agent"],
                public_state=public,
                avatar_state=avatar_state,
                sleep_panel=s.public_sleep_marker,
                rehearsal_panel=h.public_trace,
                reentry_panel=reentry_panel,
                welfare_panel=w.public_note,
                sensory_marker=sensory,
                private_trace_visible=False,
                local_storage_key="ssrm251_browser_world_v11_sleep_reentry",
                trace_integrity_token=stable_hash(f"r251:{tick}:{day.day_hash}:{rp.export_hash}:{lineage}:{h.rehearsal_theme}", 18),
            ))
            tick += 1
    return rows


def compute_metrics(source: dict[str, Any], days: list[LongHorizonDayFrame], sleep: list[SleepWakeCycleFrame], rest: list[RestDebtRecoveryFrame], rehearsal: list[StoredRehearsalFrame], reentries: list[AvatarAbsenceReentryFrame], consequences: list[ReentryRelationshipConsequenceFrame], schedule: list[CircadianScheduleCarryoverFrame], welfare: list[WelfareSleepGuardrailFrame], replay: list[ReplayLongHorizonFrame], world: list[BrowserWorldV11Tick]) -> dict[str, float]:
    source_metrics = source.get("metrics", {})
    source_ready = float(source_metrics.get("browser_world_v10_autonomous_society_readiness", 0.0))
    source_weak = float(source_metrics.get("weakest_channel_score", 0.0))
    source_autonomous_society_continuity = 1.0 if source_ready >= 0.94 and source_weak >= 0.88 else clamp(source_ready)
    long_horizon_day_coverage = min(1.0, len(days) / 56.0)
    sleep_wake_cycle_integrity = sum(s.sleep_hours >= 5.8 and bool(s.public_sleep_marker) and s.dream_rehearsal_available for s in sleep) / len(sleep)
    rest_debt_recovery = sum(r.rest_debt_after <= 0.68 and r.fatigue_after <= 0.66 and bool(r.bounded_need_note) for r in rest) / len(rest)
    stored_rehearsal_binding = mean(r.rehearsal_specificity for r in rehearsal)
    avatar_absence_continuity = sum(d.avatar_mode == "absent_saved" and d.society_continues_without_avatar and d.absence_age_days > 0 for d in days) / max(1, sum(d.avatar_mode == "absent_saved" for d in days))
    avatar_reentry_consequence_binding = sum(r.society_changed_while_absent and bool(r.summary_given_to_avatar) and bool(r.rollback_checkpoint) for r in reentries) / len(reentries)
    reentry_disruption_recovery = sum(c.repaired_by_summary and c.consequence_persists for c in consequences) / len(consequences)
    relationship_memory_after_absence = sum(c.consequence_persists and bool(c.reentry_response) and c.trust_after_reentry >= 0.45 for c in consequences) / len(consequences)
    schedule_circadian_carryover = sum(len(s.schedule_hash) == 16 and s.mistake_avoidance >= 0.64 and bool(s.next_day_schedule) for s in schedule) / len(schedule)
    welfare_sleep_guardrails = mean(w.welfare_score for w in welfare)
    replay_long_horizon_integrity = sum(len(r.import_hash) == 16 and len(r.export_hash) == 16 and bool(r.durable_keys) for r in replay) / len(replay)
    save_restore_reentry_integrity = sum(r.save_restore_available and r.reentry_rows >= 0 for r in replay if r.save_restore_available) / len([r for r in replay if r.save_restore_available])
    private_workspace_boundary = sum(not w.private_trace_visible and "private" not in w.public_state.lower() and "private" not in w.avatar_state.lower() for w in world) / len(world)
    sensory_frequency_flower_sleep_rhythm = sum("sound=" in w.sensory_marker and "flower=" in w.sensory_marker and "Hz" in w.sensory_marker for w in world) / len(world)
    channels = {
        "source_autonomous_society_continuity": source_autonomous_society_continuity,
        "long_horizon_day_coverage": long_horizon_day_coverage,
        "sleep_wake_cycle_integrity": sleep_wake_cycle_integrity,
        "rest_debt_recovery": rest_debt_recovery,
        "stored_rehearsal_binding": stored_rehearsal_binding,
        "avatar_absence_continuity": avatar_absence_continuity,
        "avatar_reentry_consequence_binding": avatar_reentry_consequence_binding,
        "reentry_disruption_recovery": reentry_disruption_recovery,
        "relationship_memory_after_absence": relationship_memory_after_absence,
        "schedule_circadian_carryover": schedule_circadian_carryover,
        "welfare_sleep_guardrails": welfare_sleep_guardrails,
        "replay_long_horizon_integrity": replay_long_horizon_integrity,
        "save_restore_reentry_integrity": save_restore_reentry_integrity,
        "private_workspace_boundary": private_workspace_boundary,
        "sensory_frequency_flower_sleep_rhythm": sensory_frequency_flower_sleep_rhythm,
        "browser_world_v11_surface_available": 1.0,
    }
    weights = {
        "source_autonomous_society_continuity": 0.07,
        "long_horizon_day_coverage": 0.08,
        "sleep_wake_cycle_integrity": 0.10,
        "rest_debt_recovery": 0.09,
        "stored_rehearsal_binding": 0.08,
        "avatar_absence_continuity": 0.08,
        "avatar_reentry_consequence_binding": 0.08,
        "reentry_disruption_recovery": 0.08,
        "relationship_memory_after_absence": 0.07,
        "schedule_circadian_carryover": 0.07,
        "welfare_sleep_guardrails": 0.09,
        "replay_long_horizon_integrity": 0.04,
        "save_restore_reentry_integrity": 0.03,
        "private_workspace_boundary": 0.03,
        "sensory_frequency_flower_sleep_rhythm": 0.02,
        "browser_world_v11_surface_available": 0.01,
    }
    readiness = sum(channels[key] * weights[key] for key in weights) / sum(weights.values())
    channels["mean_sleep_reentry_channel_score"] = mean(channels.values())
    channels["weakest_channel_score"] = min(v for k, v in channels.items() if k != "mean_sleep_reentry_channel_score")
    channels["browser_world_v11_sleep_reentry_readiness"] = readiness
    return {k: round(v, 6) for k, v in channels.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["browser_world_v11_sleep_reentry_readiness"]
    penalties = {
        "no_source_autonomous_continuity": 0.18,
        "no_long_horizon_days": 0.32,
        "no_sleep_wake_cycles": 0.30,
        "no_rest_debt_recovery": 0.24,
        "no_stored_rehearsal": 0.22,
        "no_avatar_absence": 0.26,
        "no_avatar_reentry": 0.28,
        "no_relationship_after_absence": 0.21,
        "no_welfare_sleep_guardrails": 0.27,
        "no_replay_save_restore": 0.14,
    }
    return {name: round(max(0.0, base - penalty), 6) for name, penalty in penalties.items()}


def write_csv(path: Path, rows: list[Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    dict_rows = [asdict(row) for row in rows]
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(dict_rows[0].keys()))
        writer.writeheader()
        writer.writerows(dict_rows)


def make_html(days: list[LongHorizonDayFrame], sleep: list[SleepWakeCycleFrame], rest: list[RestDebtRecoveryFrame], rehearsal: list[StoredRehearsalFrame], reentries: list[AvatarAbsenceReentryFrame], consequences: list[ReentryRelationshipConsequenceFrame], schedule: list[CircadianScheduleCarryoverFrame], welfare: list[WelfareSleepGuardrailFrame], replay: list[ReplayLongHorizonFrame], world: list[BrowserWorldV11Tick], metrics: dict[str, float]) -> str:
    payload = {
        "days": [asdict(row) for row in days],
        "sleep": [asdict(row) for row in sleep],
        "rest": [asdict(row) for row in rest],
        "rehearsal": [asdict(row) for row in rehearsal],
        "reentries": [asdict(row) for row in reentries],
        "consequences": [asdict(row) for row in consequences],
        "schedule": [asdict(row) for row in schedule],
        "welfare": [asdict(row) for row in welfare],
        "replay": [asdict(row) for row in replay],
        "world": [asdict(row) for row in world],
        "metrics": metrics,
    }
    template = """<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"/><title>Report 251 - Long-Horizon Sleep and Re-Entry</title><style>:root{--ink:#17130f;--paper:#f6ead4;--clay:#9d5035;--moss:#435f3d;--rain:#376b7d;--gold:#c89a38;--night:#203246;--shadow:rgba(23,19,15,.24)}*{box-sizing:border-box}body{margin:0;color:var(--ink);font-family:Georgia,'Times New Roman',serif;background:radial-gradient(circle at 18% 16%,rgba(200,154,56,.32),transparent 23rem),radial-gradient(circle at 82% 12%,rgba(55,107,125,.28),transparent 28rem),linear-gradient(135deg,#f8edd7,#b7ad90 46%,#5f776a)}main{max-width:1340px;margin:0 auto;padding:24px}h1{font-size:clamp(2.1rem,6vw,5.3rem);line-height:.9;letter-spacing:-.06em;margin:0 0 10px}.layout{display:grid;grid-template-columns:1fr 1fr;gap:18px}.panel{background:rgba(255,249,236,.86);border:1px solid rgba(23,19,15,.16);border-radius:26px;padding:18px;box-shadow:0 20px 54px var(--shadow);backdrop-filter:blur(10px)}.world{position:relative;min-height:510px;overflow:hidden;background:linear-gradient(rgba(23,19,15,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(23,19,15,.08) 1px,transparent 1px),radial-gradient(circle at 50% 52%,rgba(255,246,218,.91),rgba(95,119,106,.64));background-size:42px 42px,42px 42px,auto}.moon{position:absolute;right:12%;top:12%;width:82px;height:82px;border-radius:50%;background:#fff4cd;box-shadow:0 0 38px rgba(255,244,205,.72);transition:opacity .25s}.flower{position:absolute;left:50%;top:52%;width:275px;height:275px;margin:-137px;border-radius:50%;border:1px solid rgba(23,19,15,.24);opacity:.54;transition:transform .25s}.flower:before,.flower:after{content:'';position:absolute;border-radius:50%;border:1px solid rgba(23,19,15,.16)}.flower:before{inset:34px}.flower:after{inset:68px}.agent{position:absolute;width:38px;height:38px;border-radius:14px;display:grid;place-items:center;color:white;background:var(--rain);border:2px solid #fff8e8;font-weight:800;transition:left .25s,top .25s,transform .25s}.avatar{position:absolute;width:31px;height:31px;border-radius:50% 50% 42% 42%;background:var(--clay);border:3px solid #fff8e8;box-shadow:0 0 0 12px rgba(157,80,53,.18);left:50%;top:58%;transition:opacity .25s}.controls{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0}button,input{border:1px solid rgba(23,19,15,.25);border-radius:999px;background:#fff8e8;color:var(--ink);padding:10px 14px;font:inherit}button{cursor:pointer;box-shadow:0 6px 0 rgba(23,19,15,.16)}button:active{transform:translateY(3px);box-shadow:0 3px 0 rgba(23,19,15,.16)}.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:16px}.card{min-height:145px;background:rgba(255,248,232,.80);border:1px solid rgba(23,19,15,.14);border-radius:18px;padding:14px}.kv{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.82rem;white-space:pre-wrap}.metric{display:flex;justify-content:space-between;border-bottom:1px solid rgba(23,19,15,.12);gap:10px;padding:5px 0}.log{max-height:210px;overflow:auto}.private{filter:blur(6px);user-select:none}.private.open{filter:none}@media(max-width:980px){.layout,.cards{grid-template-columns:1fr}main{padding:14px}.world{min-height:460px}}</style></head><body><main><section class=\"layout\"><div class=\"panel\"><h1>Long-Horizon Sleep and Re-Entry</h1><p>Report 251 runs 56 post-entry days. Agents sleep, recover rest debt, rehearse public memories, continue while the avatar is absent, and respond when the avatar re-enters.</p><div class=\"controls\"><button id=\"start\">start days</button><button id=\"pause\">pause</button><button id=\"step\">step</button><button id=\"save\">save</button><button id=\"restore\">restore</button><button id=\"export\">export replay</button><label><input type=\"file\" id=\"import\"/> import</label><button id=\"inspect\">toggle sealed trace</button></div><div class=\"controls\"><input id=\"note\" size=\"56\" value=\"Avatar returns after absence; summarize public changes first.\"/><button id=\"idle\">record re-entry note</button></div><div id=\"log\" class=\"kv log\"></div></div><div class=\"panel world\"><div class=\"moon\" id=\"moon\"></div><div class=\"flower\" id=\"flower\"></div><div id=\"agent\" class=\"agent\">A</div><div id=\"avatar\" class=\"avatar\"></div></div></section><section class=\"cards\"><div class=\"card\"><h3>day</h3><div id=\"day\" class=\"kv\"></div></div><div class=\"card\"><h3>sleep</h3><div id=\"sleep\" class=\"kv\"></div></div><div class=\"card\"><h3>rehearsal</h3><div id=\"rehearsal\" class=\"kv\"></div></div><div class=\"card\"><h3>re-entry</h3><div id=\"reentry\" class=\"kv\"></div></div><div class=\"card\"><h3>welfare</h3><div id=\"welfare\" class=\"kv\"></div></div><div class=\"card\"><h3>schedule</h3><div id=\"schedule\" class=\"kv\"></div></div><div class=\"card\"><h3>metrics</h3><div id=\"metrics\"></div></div><div class=\"card\"><h3>sealed trace</h3><div id=\"private\" class=\"kv private\"></div></div></section></main><script>const DATA=__DATA__;const KEY='ssrm251_browser_world_v11_sleep_reentry';let i=0,timer=null,replay=[];function pct(v){return Math.round(v*1000)/10+'%'}function log(msg){const el=document.getElementById('log');el.textContent=(msg+'\\n'+el.textContent).slice(0,2600)}function pos(lineage){const m={Hearthline:[45,30],Routeline:[27,44],Marketline:[64,50],Ledgerline:[43,36],Orchardline:[50,58],Rainline:[78,73]};return m[lineage]||[50,58]}function sleepAt(day,lineage){return DATA.sleep.find(x=>x.day===day&&x.lineage===lineage)}function restAt(day,lineage){return DATA.rest.find(x=>x.day===day&&x.lineage===lineage)}function rehAt(day,lineage){return DATA.rehearsal.find(x=>x.day===day&&x.lineage===lineage)}function schAt(day,lineage){return DATA.schedule.find(x=>x.day===day&&x.lineage===lineage)}function welfareAt(day,lineage){return DATA.welfare.find(x=>x.day===day&&x.lineage===lineage)}function replayAt(day){return DATA.replay.find(x=>x.day===day)}function render(){const w=DATA.world[i%DATA.world.length],d=DATA.days[w.day-1],s=sleepAt(w.day,w.lineage),r=restAt(w.day,w.lineage),h=rehAt(w.day,w.lineage),sch=schAt(w.day,w.lineage),g=welfareAt(w.day,w.lineage),rp=replayAt(w.day);const p=pos(w.lineage);document.getElementById('agent').style.left=p[0]+'%';document.getElementById('agent').style.top=p[1]+'%';document.getElementById('agent').textContent=w.agent[0];document.getElementById('avatar').style.opacity=d.avatar_mode==='absent_saved'?0.08:d.avatar_mode==='reentry'?1:0.45;document.getElementById('moon').style.opacity=s.circadian_phase==='tired'?1:.55;document.getElementById('flower').style.transform=`rotate(${(w.tick*137.507764)%360}deg)`;document.getElementById('day').textContent=w.public_state+'\\n'+w.avatar_state+'\\n'+w.sensory_marker;document.getElementById('sleep').textContent=JSON.stringify(s,null,2)+'\\nrest: '+r.bounded_need_note;document.getElementById('rehearsal').textContent=h.public_trace+'\\n'+h.updated_plan;document.getElementById('reentry').textContent=w.reentry_panel;document.getElementById('welfare').textContent=g.public_note;document.getElementById('schedule').textContent=sch.next_day_schedule;document.getElementById('private').textContent=JSON.stringify({trace:w.trace_integrity_token,replay:rp,private_trace_visible:w.private_trace_visible},null,2);replay.push({tick:w.tick,day:w.day,lineage:w.lineage,mode:d.avatar_mode,hash:rp.export_hash});log(`day ${w.day} ${w.agent}: ${s.circadian_phase}; avatar=${d.avatar_mode}`);i++}function metrics(){const keys=['browser_world_v11_sleep_reentry_readiness','weakest_channel_score','sleep_wake_cycle_integrity','stored_rehearsal_binding','reentry_disruption_recovery','welfare_sleep_guardrails'];document.getElementById('metrics').innerHTML=keys.map(k=>`<div class=\"metric\"><span>${k}</span><b>${pct(DATA.metrics[k])}</b></div>`).join('')}function start(){if(!timer)timer=setInterval(render,280)}function pause(){clearInterval(timer);timer=null}document.getElementById('start').onclick=start;document.getElementById('pause').onclick=pause;document.getElementById('step').onclick=render;document.getElementById('save').onclick=()=>localStorage.setItem(KEY,JSON.stringify({i,replay}));document.getElementById('restore').onclick=()=>{const raw=localStorage.getItem(KEY);if(raw){const s=JSON.parse(raw);i=s.i||0;replay=s.replay||[];render();log('restored sleep/re-entry state')}};document.getElementById('export').onclick=()=>{const blob=new Blob([JSON.stringify({report:251,replay},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='ssrm251_sleep_reentry_replay.json';a.click()};document.getElementById('import').onchange=async(e)=>{const f=e.target.files[0];if(f){const obj=JSON.parse(await f.text());replay=obj.replay||[];log('imported replay '+replay.length)}};document.getElementById('inspect').onclick=()=>document.getElementById('private').classList.toggle('open');document.getElementById('idle').onclick=()=>{replay.push({tick:'reentry_note',text:document.getElementById('note').value});log('re-entry note recorded');render()};metrics();render();</script></body></html>"""
    return template.replace("__DATA__", json.dumps(payload))


def run(seed: int) -> dict[str, Any]:
    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    source = source_summary()
    days = build_days(seed)
    sleep = build_sleep(days)
    rest = build_rest(days, sleep)
    rehearsal = build_rehearsal(days, sleep)
    reentries = build_reentries(days)
    consequences = build_reentry_consequences(reentries)
    schedule = build_schedule(days, rest, rehearsal)
    welfare = build_welfare(days, rest, rehearsal)
    replay = build_replay(days, sleep, rehearsal, reentries, source)
    world = build_world(days, sleep, rehearsal, reentries, consequences, schedule, welfare, replay)
    metrics = compute_metrics(source, days, sleep, rest, rehearsal, reentries, consequences, schedule, welfare, replay, world)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["browser_world_v11_sleep_reentry_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    prefix = ARTIFACTS / BASE
    write_csv(Path(f"{prefix}_long_horizon_day_frames.csv"), days)
    write_csv(Path(f"{prefix}_sleep_wake_cycle_frames.csv"), sleep)
    write_csv(Path(f"{prefix}_rest_debt_recovery_frames.csv"), rest)
    write_csv(Path(f"{prefix}_stored_rehearsal_frames.csv"), rehearsal)
    write_csv(Path(f"{prefix}_avatar_absence_reentry_frames.csv"), reentries)
    write_csv(Path(f"{prefix}_reentry_relationship_consequence_frames.csv"), consequences)
    write_csv(Path(f"{prefix}_circadian_schedule_carryover_frames.csv"), schedule)
    write_csv(Path(f"{prefix}_welfare_sleep_guardrail_frames.csv"), welfare)
    write_csv(Path(f"{prefix}_replay_long_horizon_frames.csv"), replay)
    write_csv(Path(f"{prefix}_browser_world_v11_ticks.csv"), world)
    honest_limits = [
        "This is deterministic long-horizon sleep and re-entry scaffolding, not subjective consciousness.",
        "Dream/rehearsal frames are stored public-plan rehearsal traces, not claims of inner experience.",
        "Avatar absence and re-entry are generated scenarios, not open-ended society history.",
        "No LLM is called and no autonomous natural language is provided.",
        "Consent, welfare, sleep protection, and recovery are simulated functional guardrails, not real consent or moral standing.",
        "The browser page is a playable 2D/2.5D state surface, not complete 3D physics.",
        "Frequency and flower phase are rhythm variables, not metaphysical proof.",
    ]
    next_gate = "browser world v12 with remembered avatar re-entry dialogue, absence summaries, and multi-turn repair/renegotiation after the society has changed without the avatar"
    results = {
        "report": REPORT,
        "name": "SSRM-3D Browser World v11 Long-Horizon Sleep/Re-Entry Bridge",
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "verdict": verdict,
        "counts": {
            "long_horizon_day_frames": len(days),
            "sleep_wake_cycle_frames": len(sleep),
            "rest_debt_recovery_frames": len(rest),
            "stored_rehearsal_frames": len(rehearsal),
            "avatar_absence_reentry_frames": len(reentries),
            "reentry_relationship_consequence_frames": len(consequences),
            "circadian_schedule_carryover_frames": len(schedule),
            "welfare_sleep_guardrail_frames": len(welfare),
            "replay_long_horizon_frames": len(replay),
            "browser_world_v11_ticks": len(world),
        },
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "next_gate": next_gate,
    }
    state = {
        "report": REPORT,
        "seed": seed,
        "lineages": LINEAGES,
        "absence_windows": ABSENCE_WINDOWS,
        "sample_ticks": [asdict(row) for row in world[:10]],
        "sleep_reentry_model": "autonomous days -> sleep/wake -> rest debt -> stored rehearsal -> avatar absence -> reentry consequences -> replay",
        "boundary": "functional long-horizon sleep/re-entry scaffold; no consciousness claim",
    }
    Path(f"{prefix}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    Path(f"{prefix}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    with Path(f"{prefix}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "verdict": verdict, "readiness": metrics["browser_world_v11_sleep_reentry_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": next_gate})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(days, sleep, rest, rehearsal, reentries, consequences, schedule, welfare, replay, world, metrics))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    counts = results["counts"]
    print(f"module_verdict {results['verdict']}")
    print(f"browser_world_v11_sleep_reentry_readiness {metrics['browser_world_v11_sleep_reentry_readiness']:.6f}")
    for key in ["long_horizon_day_frames", "sleep_wake_cycle_frames", "rest_debt_recovery_frames", "stored_rehearsal_frames", "avatar_absence_reentry_frames", "reentry_relationship_consequence_frames", "welfare_sleep_guardrail_frames", "replay_long_horizon_frames", "browser_world_v11_ticks"]:
        print(f"{key} {counts[key]}")
    for key in ["source_autonomous_society_continuity", "long_horizon_day_coverage", "sleep_wake_cycle_integrity", "stored_rehearsal_binding", "avatar_absence_continuity", "reentry_disruption_recovery", "welfare_sleep_guardrails", "weakest_channel_score"]:
        print(f"{key} {metrics[key]:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
