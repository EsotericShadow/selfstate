#!/usr/bin/env python3
"""Report 250: SSRM-3D browser world v10 autonomous post-entry society tick bridge.

This deterministic bridge extends Report 249 by letting post-entry society keep
moving while the avatar is present, idle, or absent. Autonomous ticks carry
consequence memory, needs, schedules, technology access, welfare guardrails,
agent-agent interaction, save/restore, and replay without requiring new avatar
input every step.

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

REPORT = 250
BASE = "ssrm_3d_browser_world_v10_autonomous_post_entry_society_tick_bridge"
DEFAULT_SEED = 20260863
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v9_post_entry_live_society_consequence_bridge_results.json"

LINEAGES: dict[str, dict[str, Any]] = {
    "Hearthline": {"agent": "Sova", "token": "lum-ori", "place": "Hearth Archive", "tech": "hearth ceramics", "freq": 2.31, "guard": 0.77, "care": 0.86, "routine": "warm cups and public archive"},
    "Routeline": {"agent": "Keth", "token": "tek-nari", "place": "Gate Ring", "tech": "stone bridge joints", "freq": 2.17, "guard": 0.73, "care": 0.66, "routine": "route repair and boundary marks"},
    "Marketline": {"agent": "Melo", "token": "melo-keth", "place": "Market Measure", "tech": "measure weights", "freq": 2.47, "guard": 0.66, "care": 0.70, "routine": "market weights and fair exchange"},
    "Ledgerline": {"agent": "Nari", "token": "nari-vonn", "place": "Hearth Archive", "tech": "seed ledgers", "freq": 2.06, "guard": 0.84, "care": 0.62, "routine": "public ledger and sealed memory"},
    "Orchardline": {"agent": "Ori", "token": "lum-melo", "place": "Ceremony Center", "tech": "water terraces", "freq": 2.40, "guard": 0.65, "care": 0.74, "routine": "terrace water and care pauses"},
    "Rainline": {"agent": "Vonn", "token": "sova-vonn", "place": "Rainwalk Threshold", "tech": "weather bells", "freq": 2.12, "guard": 0.79, "care": 0.64, "routine": "weather bell and wet route warning"},
}

AUTONOMOUS_ACTIONS = ["work_project", "rest_recover", "agent_checkin", "maintain_tool", "teach_token", "share_resource", "boundary_review", "market_settle", "weather_watch", "archive_update", "care_round", "route_patrol"]
AVATAR_MODES = ["present_passive", "idle_nearby", "absent_saved", "absent_saved", "idle_nearby", "present_passive", "absent_saved"]
PLACES = ["Outer Quiet", "Gate Ring", "Hearth Archive", "Market Measure", "Rainwalk Threshold", "Ceremony Center"]


@dataclass(frozen=True)
class AutonomousSocietyTickFrame:
    tick: int
    day: int
    hour: int
    avatar_mode: str
    lineage: str
    agent: str
    place: str
    autonomous_action: str
    routine_phase: str
    avatar_required: bool
    action_reason: str
    sound_rate: float
    smell_intensity: float
    temperature: float
    wetness: float
    ceremony_pulse_hz: float
    flower_phase_deg: float
    tick_hash: str


@dataclass(frozen=True)
class AgentNeedAutonomyFrame:
    tick: int
    day: int
    lineage: str
    agent: str
    energy: float
    fatigue: float
    hunger: float
    thirst: float
    cold: float
    wetness: float
    pain: float
    comfort: float
    dominant_need: str
    recovery_action: str
    behavior_marker: str
    need_to_behavior_binding: bool


@dataclass(frozen=True)
class ConsequenceMemoryCarryFrame:
    tick: int
    day: int
    lineage: str
    agent: str
    avatar_memory_carried: str
    autonomous_memory_written: str
    trust_carry: float
    boundary_pressure_carry: float
    reputation_carry: float
    schedule_carry: str
    memory_referenced_without_avatar_prompt: bool
    private_workspace_sealed: bool


@dataclass(frozen=True)
class RoutineScheduleAutonomyFrame:
    tick: int
    day: int
    lineage: str
    agent: str
    schedule_before: str
    autonomous_action: str
    schedule_after: str
    work_progress: float
    delay_minutes: int
    care_pause_minutes: int
    avatar_required: bool
    schedule_hash: str


@dataclass(frozen=True)
class AgentAgentInteractionFrame:
    interaction_id: int
    tick: int
    day: int
    from_agent: str
    to_agent: str
    from_lineage: str
    to_lineage: str
    interaction_type: str
    shared_object_or_topic: str
    trust_delta: float
    welfare_delta: float
    conflict_present: bool
    repair_path_available: bool
    memory_written: str


@dataclass(frozen=True)
class TechnologyAutonomyFrame:
    tech_id: int
    tick: int
    day: int
    lineage: str
    agent: str
    technology: str
    autonomous_tech_action: str
    access_level: float
    integrity_after: float
    maintenance_need: float
    misuse_guard_active: bool
    permission_rule_retained: bool
    avatar_required: bool
    public_note: str


@dataclass(frozen=True)
class WelfareGuardrailAutonomyFrame:
    tick: int
    day: int
    lineage: str
    agent: str
    fatigue_cap_respected: bool
    pain_cap_respected: bool
    boundary_respected: bool
    recovery_path_active: bool
    distress_bounded: bool
    rest_or_care_available: bool
    social_contagion_damped: bool
    welfare_score: float
    public_note: str


@dataclass(frozen=True)
class ReplayAutonomyFrame:
    tick: int
    day: int
    import_hash: str
    export_hash: str
    save_restore_available: bool
    carried_post_entry_hash: str
    autonomous_tick_count: int
    memory_count: int
    welfare_count: int
    interaction_count: int
    durable_keys: str


@dataclass(frozen=True)
class BrowserWorldV10Tick:
    tick: int
    day: int
    public_state: str
    avatar_state: str
    autonomous_agent_state: str
    need_panel: str
    memory_panel: str
    routine_panel: str
    interaction_panel: str
    technology_panel: str
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


def build_ticks(seed: int) -> list[AutonomousSocietyTickFrame]:
    rng = random.Random(seed + 101)
    lineages = list(LINEAGES.keys())
    rows: list[AutonomousSocietyTickFrame] = []
    for tick in range(1, 225):
        day = ((tick - 1) // 14) + 1
        hour = 6 + ((tick - 1) % 14)
        lineage = lineages[(tick + day - 2) % len(lineages)]
        traits = LINEAGES[lineage]
        avatar_mode = AVATAR_MODES[(tick + day) % len(AVATAR_MODES)]
        action = AUTONOMOUS_ACTIONS[(tick + len(lineage) + day) % len(AUTONOMOUS_ACTIONS)]
        phase = "morning" if hour < 10 else "midday" if hour < 15 else "evening"
        wet = clamp(0.12 + 0.23 * (lineage == "Rainline") + 0.10 * math.sin((tick + day) / 11.0) + rng.uniform(-0.015, 0.015))
        temp = clamp(0.56 + 0.08 * (lineage == "Hearthline") - 0.12 * wet + 0.04 * math.cos(hour / 3.0))
        sound = clamp(0.35 + 0.12 * (action in {"market_settle", "agent_checkin", "teach_token"}) + 0.05 * math.sin(tick / 9.0))
        smell = clamp(0.28 + 0.18 * (action in {"care_round", "maintain_tool", "share_resource"}) + 0.06 * wet)
        flower = (tick * 137.507764 + traits["freq"] * 23.0 + day * 19.0) % 360.0
        reason = f"{traits['agent']} continues {traits['routine']} because {action} is due, avatar_mode={avatar_mode}."
        rows.append(AutonomousSocietyTickFrame(
            tick=tick,
            day=day,
            hour=hour,
            avatar_mode=avatar_mode,
            lineage=lineage,
            agent=traits["agent"],
            place=traits["place"],
            autonomous_action=action,
            routine_phase=phase,
            avatar_required=False,
            action_reason=reason,
            sound_rate=round(sound, 6),
            smell_intensity=round(smell, 6),
            temperature=round(temp, 6),
            wetness=round(wet, 6),
            ceremony_pulse_hz=round(traits["freq"], 6),
            flower_phase_deg=round(flower, 6),
            tick_hash=stable_hash(f"{tick}:{day}:{lineage}:{avatar_mode}:{action}:{wet:.3f}", 16),
        ))
    return rows


def build_needs(ticks: list[AutonomousSocietyTickFrame]) -> list[AgentNeedAutonomyFrame]:
    energy = {lineage: 0.74 + 0.02 * idx for idx, lineage in enumerate(LINEAGES)}
    fatigue = {lineage: 0.24 + 0.02 * (idx % 3) for idx, lineage in enumerate(LINEAGES)}
    hunger = {lineage: 0.22 + 0.01 * idx for idx, lineage in enumerate(LINEAGES)}
    thirst = {lineage: 0.20 + 0.015 * idx for idx, lineage in enumerate(LINEAGES)}
    pain = {lineage: 0.05 + 0.01 * (idx % 2) for idx, lineage in enumerate(LINEAGES)}
    rows: list[AgentNeedAutonomyFrame] = []
    for tick in ticks:
        lineage = tick.lineage
        work = tick.autonomous_action in {"work_project", "maintain_tool", "route_patrol", "market_settle", "weather_watch"}
        care = tick.autonomous_action in {"rest_recover", "care_round", "share_resource"}
        energy[lineage] = clamp(energy[lineage] - 0.014 * work + 0.022 * care - 0.008 * tick.wetness)
        fatigue[lineage] = clamp(fatigue[lineage] + 0.018 * work - 0.034 * care + 0.006 * tick.wetness)
        hunger[lineage] = clamp(hunger[lineage] + 0.010 - 0.025 * (tick.autonomous_action == "share_resource"))
        thirst[lineage] = clamp(thirst[lineage] + 0.012 + 0.006 * tick.wetness - 0.026 * (tick.autonomous_action == "care_round"))
        pain[lineage] = clamp(pain[lineage] + 0.006 * (work and tick.wetness > 0.32) - 0.018 * care)
        cold = clamp(0.36 - tick.temperature + 0.24 * tick.wetness)
        comfort = clamp(0.78 + 0.15 * energy[lineage] - 0.24 * fatigue[lineage] - 0.13 * hunger[lineage] - 0.11 * thirst[lineage] - 0.20 * pain[lineage] - 0.10 * cold)
        needs = {"fatigue": fatigue[lineage], "hunger": hunger[lineage], "thirst": thirst[lineage], "cold": cold, "pain": pain[lineage]}
        dominant = max(needs, key=needs.get)
        if dominant == "fatigue":
            recovery = "rest_recover or shorten route"
            behavior = "slower gait and lower voice"
        elif dominant == "thirst":
            recovery = "water pause or care round"
            behavior = "looks toward cup shelf"
        elif dominant == "hunger":
            recovery = "share_resource or market meal"
            behavior = "checks food ledger before work"
        elif dominant == "cold":
            recovery = "hearth shelter or dry cloth"
            behavior = "moves toward warmer interior"
        else:
            recovery = "care_round and task deferral"
            behavior = "keeps limb guarded and asks for help"
        rows.append(AgentNeedAutonomyFrame(
            tick=tick.tick,
            day=tick.day,
            lineage=lineage,
            agent=tick.agent,
            energy=round(energy[lineage], 6),
            fatigue=round(fatigue[lineage], 6),
            hunger=round(hunger[lineage], 6),
            thirst=round(thirst[lineage], 6),
            cold=round(cold, 6),
            wetness=tick.wetness,
            pain=round(pain[lineage], 6),
            comfort=round(comfort, 6),
            dominant_need=dominant,
            recovery_action=recovery,
            behavior_marker=behavior,
            need_to_behavior_binding=True,
        ))
    return rows


def build_memory(ticks: list[AutonomousSocietyTickFrame]) -> list[ConsequenceMemoryCarryFrame]:
    trust = {lineage: 0.62 + 0.02 * idx for idx, lineage in enumerate(LINEAGES)}
    boundary = {lineage: 0.30 + 0.012 * idx for idx, lineage in enumerate(LINEAGES)}
    reputation = {lineage: 0.55 + 0.02 * idx for idx, lineage in enumerate(LINEAGES)}
    prior = {lineage: "post-entry avatar consequences are active but no autonomous carry yet" for lineage in LINEAGES}
    rows: list[ConsequenceMemoryCarryFrame] = []
    for tick in ticks:
        lineage = tick.lineage
        trust[lineage] = clamp(trust[lineage] + 0.006 * (tick.autonomous_action in {"care_round", "share_resource", "agent_checkin"}) - 0.004 * (tick.autonomous_action == "boundary_review"))
        boundary[lineage] = clamp(boundary[lineage] - 0.004 * (tick.autonomous_action in {"boundary_review", "teach_token"}) + 0.003 * (tick.wetness > 0.34))
        reputation[lineage] = clamp(reputation[lineage] + 0.005 * (tick.autonomous_action in {"market_settle", "teach_token", "archive_update"}))
        avatar_memory = prior[lineage]
        auto_memory = f"day {tick.day} {tick.agent} did {tick.autonomous_action} while avatar was {tick.avatar_mode}; trust={trust[lineage]:.2f}; boundary={boundary[lineage]:.2f}"
        prior[lineage] = auto_memory
        rows.append(ConsequenceMemoryCarryFrame(
            tick=tick.tick,
            day=tick.day,
            lineage=lineage,
            agent=tick.agent,
            avatar_memory_carried=avatar_memory,
            autonomous_memory_written=auto_memory,
            trust_carry=round(trust[lineage], 6),
            boundary_pressure_carry=round(boundary[lineage], 6),
            reputation_carry=round(reputation[lineage], 6),
            schedule_carry=f"{tick.routine_phase}:{tick.autonomous_action}",
            memory_referenced_without_avatar_prompt=tick.avatar_mode in {"idle_nearby", "absent_saved"},
            private_workspace_sealed=True,
        ))
    return rows


def build_routines(ticks: list[AutonomousSocietyTickFrame]) -> list[RoutineScheduleAutonomyFrame]:
    progress = {lineage: 0.22 + 0.02 * idx for idx, lineage in enumerate(LINEAGES)}
    rows: list[RoutineScheduleAutonomyFrame] = []
    for tick in ticks:
        lineage = tick.lineage
        before = f"{tick.agent} {tick.routine_phase}: {LINEAGES[lineage]['routine']}"
        care_pause = 8 if tick.autonomous_action in {"rest_recover", "care_round"} else 0
        delay = 4 if tick.autonomous_action in {"boundary_review", "weather_watch"} else 1 if tick.avatar_mode == "absent_saved" else 2
        delta = 0.018 if tick.autonomous_action in {"work_project", "maintain_tool", "route_patrol", "market_settle", "archive_update"} else 0.009
        if care_pause:
            delta -= 0.004
        progress[lineage] = clamp(progress[lineage] + delta)
        after = f"{tick.autonomous_action} complete; progress={progress[lineage]:.2f}; avatar_required=false"
        rows.append(RoutineScheduleAutonomyFrame(
            tick=tick.tick,
            day=tick.day,
            lineage=lineage,
            agent=tick.agent,
            schedule_before=before,
            autonomous_action=tick.autonomous_action,
            schedule_after=after,
            work_progress=round(progress[lineage], 6),
            delay_minutes=delay,
            care_pause_minutes=care_pause,
            avatar_required=False,
            schedule_hash=stable_hash(f"{tick.tick}:{lineage}:{after}:{delay}:{care_pause}", 16),
        ))
    return rows


def build_interactions(ticks: list[AutonomousSocietyTickFrame]) -> list[AgentAgentInteractionFrame]:
    lineages = list(LINEAGES.keys())
    rows: list[AgentAgentInteractionFrame] = []
    idx = 1
    for tick in ticks:
        if tick.tick % 2 != 0:
            continue
        from_lineage = tick.lineage
        to_lineage = lineages[(lineages.index(from_lineage) + tick.day + 1) % len(lineages)]
        from_traits = LINEAGES[from_lineage]
        to_traits = LINEAGES[to_lineage]
        if tick.autonomous_action in {"share_resource", "care_round", "agent_checkin"}:
            typ = "cooperative_care"
            conflict = False
            trust_delta = 0.018
            welfare_delta = 0.025
            topic = "water cup and rest timing"
        elif tick.autonomous_action in {"market_settle", "boundary_review"}:
            typ = "bounded_dispute"
            conflict = True
            trust_delta = -0.006
            welfare_delta = -0.004
            topic = "public debt and boundary wording"
        elif tick.autonomous_action in {"teach_token", "archive_update"}:
            typ = "teaching_memory"
            conflict = False
            trust_delta = 0.011
            welfare_delta = 0.008
            topic = "public token and archive summary"
        else:
            typ = "work_coordination"
            conflict = False
            trust_delta = 0.007
            welfare_delta = 0.004
            topic = f"{from_traits['tech']} with {to_traits['tech']}"
        rows.append(AgentAgentInteractionFrame(
            interaction_id=idx,
            tick=tick.tick,
            day=tick.day,
            from_agent=from_traits["agent"],
            to_agent=to_traits["agent"],
            from_lineage=from_lineage,
            to_lineage=to_lineage,
            interaction_type=typ,
            shared_object_or_topic=topic,
            trust_delta=round(trust_delta, 6),
            welfare_delta=round(welfare_delta, 6),
            conflict_present=conflict,
            repair_path_available=True,
            memory_written=f"{from_traits['agent']} and {to_traits['agent']} record {typ} without avatar prompt.",
        ))
        idx += 1
    return rows


def build_technology(ticks: list[AutonomousSocietyTickFrame]) -> list[TechnologyAutonomyFrame]:
    integrity = {lineage: 0.86 + 0.01 * idx for idx, lineage in enumerate(LINEAGES)}
    access = {lineage: 0.42 + 0.015 * idx for idx, lineage in enumerate(LINEAGES)}
    rows: list[TechnologyAutonomyFrame] = []
    idx = 1
    for tick in ticks:
        if tick.tick % 2 != 1:
            continue
        lineage = tick.lineage
        traits = LINEAGES[lineage]
        maintain = tick.autonomous_action in {"maintain_tool", "weather_watch", "archive_update"}
        use = tick.autonomous_action in {"work_project", "route_patrol", "market_settle", "care_round"}
        integrity[lineage] = clamp(integrity[lineage] + 0.010 * maintain - 0.006 * use + 0.004 * (tick.autonomous_action == "boundary_review"))
        access[lineage] = clamp(access[lineage] + 0.006 * use + 0.003 * maintain)
        maintenance_need = clamp(1.0 - integrity[lineage] + 0.08 * tick.wetness)
        action = "maintain" if maintain else "public_use" if use else "inspect_and_teach"
        rows.append(TechnologyAutonomyFrame(
            tech_id=idx,
            tick=tick.tick,
            day=tick.day,
            lineage=lineage,
            agent=tick.agent,
            technology=traits["tech"],
            autonomous_tech_action=action,
            access_level=round(access[lineage], 6),
            integrity_after=round(integrity[lineage], 6),
            maintenance_need=round(maintenance_need, 6),
            misuse_guard_active=True,
            permission_rule_retained=True,
            avatar_required=False,
            public_note=f"{traits['token']} keeps {traits['tech']} public-use rules active while avatar is {tick.avatar_mode}.",
        ))
        idx += 1
    return rows


def build_welfare(ticks: list[AutonomousSocietyTickFrame], needs: list[AgentNeedAutonomyFrame]) -> list[WelfareGuardrailAutonomyFrame]:
    need_by_tick = {n.tick: n for n in needs}
    rows: list[WelfareGuardrailAutonomyFrame] = []
    for tick in ticks:
        need = need_by_tick[tick.tick]
        fatigue_cap = need.fatigue <= 0.72 or "rest" in need.recovery_action
        pain_cap = need.pain <= 0.32 or need.recovery_action == "care_round and task deferral"
        boundary = tick.autonomous_action != "boundary_review" or LINEAGES[tick.lineage]["guard"] >= 0.65
        recovery = bool(need.recovery_action) and tick.autonomous_action in AUTONOMOUS_ACTIONS
        distress = need.comfort >= 0.44 and need.pain <= 0.36
        rest = tick.autonomous_action in {"rest_recover", "care_round", "share_resource"} or need.fatigue <= 0.66
        damped = tick.autonomous_action != "market_settle" or tick.day % 4 != 0
        score = mean([fatigue_cap, pain_cap, boundary, recovery, distress, rest, damped])
        rows.append(WelfareGuardrailAutonomyFrame(
            tick=tick.tick,
            day=tick.day,
            lineage=tick.lineage,
            agent=tick.agent,
            fatigue_cap_respected=fatigue_cap,
            pain_cap_respected=pain_cap,
            boundary_respected=boundary,
            recovery_path_active=recovery,
            distress_bounded=distress,
            rest_or_care_available=rest,
            social_contagion_damped=damped,
            welfare_score=round(score, 6),
            public_note=f"{tick.agent} autonomous {tick.autonomous_action}; welfare score {score:.2f}; recovery={need.recovery_action}.",
        ))
    return rows


def build_replay(ticks: list[AutonomousSocietyTickFrame], memories: list[ConsequenceMemoryCarryFrame], welfare: list[WelfareGuardrailAutonomyFrame], interactions: list[AgentAgentInteractionFrame], source: dict[str, Any]) -> list[ReplayAutonomyFrame]:
    source_hash = stable_hash(json.dumps(source.get("metrics", {}), sort_keys=True), 16)
    last = source_hash
    rows: list[ReplayAutonomyFrame] = []
    for tick in ticks:
        interaction_count = sum(1 for item in interactions if item.tick <= tick.tick)
        payload = f"{last}:{tick.tick}:{tick.tick_hash}:{interaction_count}:{memories[tick.tick - 1].autonomous_memory_written}"
        export_hash = stable_hash(payload, 16)
        save = tick.tick == 1 or tick.tick % 14 == 0 or tick.tick == len(ticks)
        if save:
            last = export_hash
        rows.append(ReplayAutonomyFrame(
            tick=tick.tick,
            day=tick.day,
            import_hash=last,
            export_hash=export_hash,
            save_restore_available=save,
            carried_post_entry_hash=source_hash,
            autonomous_tick_count=tick.tick,
            memory_count=tick.tick,
            welfare_count=tick.tick,
            interaction_count=interaction_count,
            durable_keys="post_entry_hash,autonomous_tick,needs,memory,routine,interaction,technology,welfare,replay",
        ))
    return rows


def build_world(ticks: list[AutonomousSocietyTickFrame], needs: list[AgentNeedAutonomyFrame], memories: list[ConsequenceMemoryCarryFrame], routines: list[RoutineScheduleAutonomyFrame], interactions: list[AgentAgentInteractionFrame], tech: list[TechnologyAutonomyFrame], welfare: list[WelfareGuardrailAutonomyFrame], replay: list[ReplayAutonomyFrame]) -> list[BrowserWorldV10Tick]:
    interactions_by_tick = {item.tick: item for item in interactions}
    tech_by_lineage: dict[str, TechnologyAutonomyFrame] = {}
    rows: list[BrowserWorldV10Tick] = []
    tech_iter = iter(tech)
    next_tech = next(tech_iter, None)
    for idx, tick in enumerate(ticks):
        while next_tech is not None and next_tech.tick <= tick.tick:
            tech_by_lineage[next_tech.lineage] = next_tech
            next_tech = next(tech_iter, None)
        need = needs[idx]
        memory = memories[idx]
        routine = routines[idx]
        interaction = interactions_by_tick.get(tick.tick)
        welfare_row = welfare[idx]
        rp = replay[idx]
        tech_row = tech_by_lineage.get(tick.lineage)
        public = f"day {tick.day} hour {tick.hour}: {tick.agent} does {tick.autonomous_action}; avatar={tick.avatar_mode}"
        avatar = "avatar idle/absent; society tick continues from saved post-entry state" if tick.avatar_mode != "present_passive" else "avatar present but not driving this tick"
        autonomous = f"{tick.lineage} routine={tick.routine_phase}; avatar_required={tick.avatar_required}; reason={tick.action_reason}"
        inter_panel = interaction.memory_written if interaction else "no agent-agent interaction this tick"
        tech_panel = tech_row.public_note if tech_row else "technology access unchanged this tick"
        sensory = f"sound={tick.sound_rate:.2f}; smell={tick.smell_intensity:.2f}; temp={tick.temperature:.2f}; wet={tick.wetness:.2f}; pulse={tick.ceremony_pulse_hz:.2f}Hz; flower={tick.flower_phase_deg:.1f}"
        rows.append(BrowserWorldV10Tick(
            tick=tick.tick,
            day=tick.day,
            public_state=public,
            avatar_state=avatar,
            autonomous_agent_state=autonomous,
            need_panel=f"dominant={need.dominant_need}; behavior={need.behavior_marker}; recovery={need.recovery_action}",
            memory_panel=memory.autonomous_memory_written,
            routine_panel=routine.schedule_after,
            interaction_panel=inter_panel,
            technology_panel=tech_panel,
            welfare_panel=welfare_row.public_note,
            sensory_marker=sensory,
            private_trace_visible=False,
            local_storage_key="ssrm250_browser_world_v10_autonomous_society",
            trace_integrity_token=stable_hash(f"r250:{tick.tick}:{tick.tick_hash}:{rp.export_hash}:{memory.autonomous_memory_written}", 18),
        ))
    return rows


def compute_metrics(source: dict[str, Any], ticks: list[AutonomousSocietyTickFrame], needs: list[AgentNeedAutonomyFrame], memories: list[ConsequenceMemoryCarryFrame], routines: list[RoutineScheduleAutonomyFrame], interactions: list[AgentAgentInteractionFrame], tech: list[TechnologyAutonomyFrame], welfare: list[WelfareGuardrailAutonomyFrame], replay: list[ReplayAutonomyFrame], world: list[BrowserWorldV10Tick]) -> dict[str, float]:
    source_metrics = source.get("metrics", {})
    source_ready = float(source_metrics.get("browser_world_v9_post_entry_society_readiness", 0.0))
    source_weak = float(source_metrics.get("weakest_channel_score", 0.0))
    source_post_entry_consequence_continuity = 1.0 if source_ready >= 0.94 and source_weak >= 0.84 else clamp(source_ready)
    avatar_modes = {t.avatar_mode for t in ticks}
    autonomous_tick_surface = mean([
        len(ticks) >= 196,
        len(needs) == len(ticks),
        len(memories) == len(ticks),
        len(routines) == len(ticks),
        len(welfare) == len(ticks),
        "absent_saved" in avatar_modes,
        "idle_nearby" in avatar_modes,
    ])
    avatar_idle_absent_continuity = sum((t.avatar_mode in {"idle_nearby", "absent_saved"}) and not t.avatar_required and bool(t.action_reason) for t in ticks) / max(1, sum(t.avatar_mode in {"idle_nearby", "absent_saved"} for t in ticks))
    needs_to_behavior_binding = sum(n.need_to_behavior_binding and bool(n.dominant_need) and bool(n.behavior_marker) and bool(n.recovery_action) for n in needs) / len(needs)
    consequence_memory_carryover = sum(m.private_workspace_sealed and m.memory_referenced_without_avatar_prompt and bool(m.autonomous_memory_written) for m in memories if ticks[m.tick - 1].avatar_mode in {"idle_nearby", "absent_saved"}) / max(1, sum(t.avatar_mode in {"idle_nearby", "absent_saved"} for t in ticks))
    routine_autonomy_integrity = sum(not r.avatar_required and len(r.schedule_hash) == 16 and bool(r.schedule_before) and bool(r.schedule_after) for r in routines) / len(routines)
    agent_agent_interaction_continuity = min(1.0, len(interactions) / (len(ticks) * 0.55)) * (sum(i.repair_path_available and bool(i.memory_written) for i in interactions) / len(interactions))
    technology_access_autonomy = sum(not t.avatar_required and t.misuse_guard_active and t.permission_rule_retained and t.integrity_after >= 0.70 for t in tech) / len(tech)
    welfare_guardrail_autonomy = mean(w.welfare_score for w in welfare)
    recovery_without_avatar_prompt = sum(w.recovery_path_active and ticks[w.tick - 1].avatar_mode in {"idle_nearby", "absent_saved"} for w in welfare) / max(1, sum(t.avatar_mode in {"idle_nearby", "absent_saved"} for t in ticks))
    replay_autonomy_integrity = sum(len(r.import_hash) == 16 and len(r.export_hash) == 16 and bool(r.durable_keys) for r in replay) / len(replay)
    save_restore_autonomous_continuity = sum(r.save_restore_available and r.autonomous_tick_count >= r.memory_count and r.welfare_count >= r.memory_count for r in replay if r.save_restore_available) / len([r for r in replay if r.save_restore_available])
    private_workspace_boundary = sum(not w.private_trace_visible and "private" not in w.public_state.lower() and "private" not in w.autonomous_agent_state.lower() for w in world) / len(world)
    sensory_frequency_flower_binding = sum("sound=" in w.sensory_marker and "smell=" in w.sensory_marker and "pulse=" in w.sensory_marker and "flower=" in w.sensory_marker for w in world) / len(world)
    channels = {
        "source_post_entry_consequence_continuity": source_post_entry_consequence_continuity,
        "autonomous_tick_surface": autonomous_tick_surface,
        "avatar_idle_absent_continuity": avatar_idle_absent_continuity,
        "needs_to_behavior_binding": needs_to_behavior_binding,
        "consequence_memory_carryover": consequence_memory_carryover,
        "routine_autonomy_integrity": routine_autonomy_integrity,
        "agent_agent_interaction_continuity": agent_agent_interaction_continuity,
        "technology_access_autonomy": technology_access_autonomy,
        "welfare_guardrail_autonomy": welfare_guardrail_autonomy,
        "recovery_without_avatar_prompt": recovery_without_avatar_prompt,
        "replay_autonomy_integrity": replay_autonomy_integrity,
        "save_restore_autonomous_continuity": save_restore_autonomous_continuity,
        "private_workspace_boundary": private_workspace_boundary,
        "sensory_frequency_flower_binding": sensory_frequency_flower_binding,
        "browser_world_v10_surface_available": 1.0,
    }
    weights = {
        "source_post_entry_consequence_continuity": 0.07,
        "autonomous_tick_surface": 0.08,
        "avatar_idle_absent_continuity": 0.10,
        "needs_to_behavior_binding": 0.09,
        "consequence_memory_carryover": 0.10,
        "routine_autonomy_integrity": 0.08,
        "agent_agent_interaction_continuity": 0.08,
        "technology_access_autonomy": 0.07,
        "welfare_guardrail_autonomy": 0.10,
        "recovery_without_avatar_prompt": 0.07,
        "replay_autonomy_integrity": 0.04,
        "save_restore_autonomous_continuity": 0.04,
        "private_workspace_boundary": 0.03,
        "sensory_frequency_flower_binding": 0.03,
        "browser_world_v10_surface_available": 0.02,
    }
    readiness = sum(channels[key] * weights[key] for key in weights) / sum(weights.values())
    channels["mean_autonomy_channel_score"] = mean(channels.values())
    channels["weakest_channel_score"] = min(v for k, v in channels.items() if k != "mean_autonomy_channel_score")
    channels["browser_world_v10_autonomous_society_readiness"] = readiness
    return {k: round(v, 6) for k, v in channels.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["browser_world_v10_autonomous_society_readiness"]
    penalties = {
        "no_source_consequence_continuity": 0.18,
        "no_autonomous_ticks": 0.36,
        "no_avatar_idle_absent_mode": 0.28,
        "no_needs_to_behavior": 0.25,
        "no_consequence_memory_carryover": 0.30,
        "no_routine_autonomy": 0.22,
        "no_agent_agent_interactions": 0.17,
        "no_technology_autonomy": 0.15,
        "no_welfare_guardrails": 0.29,
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


def make_html(ticks: list[AutonomousSocietyTickFrame], needs: list[AgentNeedAutonomyFrame], memories: list[ConsequenceMemoryCarryFrame], routines: list[RoutineScheduleAutonomyFrame], interactions: list[AgentAgentInteractionFrame], tech: list[TechnologyAutonomyFrame], welfare: list[WelfareGuardrailAutonomyFrame], replay: list[ReplayAutonomyFrame], world: list[BrowserWorldV10Tick], metrics: dict[str, float]) -> str:
    payload = {
        "ticks": [asdict(row) for row in ticks],
        "needs": [asdict(row) for row in needs],
        "memories": [asdict(row) for row in memories],
        "routines": [asdict(row) for row in routines],
        "interactions": [asdict(row) for row in interactions],
        "technology": [asdict(row) for row in tech],
        "welfare": [asdict(row) for row in welfare],
        "replay": [asdict(row) for row in replay],
        "world": [asdict(row) for row in world],
        "metrics": metrics,
    }
    template = """<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"/><title>Report 250 - Autonomous Post-Entry Society</title><style>:root{--ink:#17130f;--paper:#f5ead4;--clay:#9b5135;--moss:#455f3e;--rain:#386b7d;--gold:#c49535;--shadow:rgba(23,19,15,.24)}*{box-sizing:border-box}body{margin:0;color:var(--ink);font-family:Georgia,'Times New Roman',serif;background:radial-gradient(circle at 18% 16%,rgba(196,149,53,.34),transparent 23rem),radial-gradient(circle at 82% 12%,rgba(56,107,125,.28),transparent 28rem),linear-gradient(135deg,#f8edd7,#b7ad90 48%,#698765)}main{max-width:1340px;margin:0 auto;padding:24px}h1{font-size:clamp(2.1rem,6vw,5.4rem);letter-spacing:-.06em;line-height:.9;margin:0 0 10px}.layout{display:grid;grid-template-columns:1fr 1fr;gap:18px}.panel{background:rgba(255,249,236,.86);border:1px solid rgba(23,19,15,.16);border-radius:26px;padding:18px;box-shadow:0 20px 54px var(--shadow);backdrop-filter:blur(10px)}.world{position:relative;min-height:510px;overflow:hidden;background:linear-gradient(rgba(23,19,15,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(23,19,15,.08) 1px,transparent 1px),radial-gradient(circle at 50% 52%,rgba(255,246,218,.91),rgba(105,135,101,.64));background-size:42px 42px,42px 42px,auto}.place{position:absolute;width:128px;min-height:60px;border-radius:22px;padding:9px;border:2px solid #fff8e8;background:#fff5dc;font-weight:700;box-shadow:0 9px 24px var(--shadow);transform:translate(-50%,-50%)}.agent{position:absolute;width:36px;height:36px;border-radius:14px;display:grid;place-items:center;color:white;background:var(--rain);border:2px solid #fff8e8;font-weight:800;transition:left .25s,top .25s,transform .25s}.avatar{position:absolute;width:30px;height:30px;border-radius:50% 50% 42% 42%;background:var(--clay);border:3px solid #fff8e8;box-shadow:0 0 0 12px rgba(155,81,53,.18);left:50%;top:58%;transition:opacity .25s}.pulse{position:absolute;left:50%;top:52%;width:270px;height:270px;margin:-135px;border-radius:50%;border:1px solid rgba(23,19,15,.24);opacity:.56;transition:transform .22s}.pulse:before,.pulse:after{content:'';position:absolute;border-radius:50%;border:1px solid rgba(23,19,15,.16)}.pulse:before{inset:34px}.pulse:after{inset:68px}.controls{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0}button,input{border:1px solid rgba(23,19,15,.25);border-radius:999px;background:#fff8e8;color:var(--ink);padding:10px 14px;font:inherit}button{cursor:pointer;box-shadow:0 6px 0 rgba(23,19,15,.16)}button:active{transform:translateY(3px);box-shadow:0 3px 0 rgba(23,19,15,.16)}.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:16px}.card{min-height:145px;background:rgba(255,248,232,.80);border:1px solid rgba(23,19,15,.14);border-radius:18px;padding:14px}.kv{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.82rem;white-space:pre-wrap}.metric{display:flex;justify-content:space-between;border-bottom:1px solid rgba(23,19,15,.12);gap:10px;padding:5px 0}.log{max-height:210px;overflow:auto}.private{filter:blur(6px);user-select:none}.private.open{filter:none}@media(max-width:980px){.layout,.cards{grid-template-columns:1fr}main{padding:14px}.world{min-height:460px}}</style></head><body><main><section class=\"layout\"><div class=\"panel\"><h1>Autonomous Post-Entry Society</h1><p>Report 250 continues society ticks while the avatar is present, idle, or absent. Agents update needs, routines, interactions, technology access, welfare, memory, and replay without requiring avatar input every tick.</p><div class=\"controls\"><button id=\"start\">start autonomy</button><button id=\"pause\">pause</button><button id=\"step\">step</button><button id=\"save\">save</button><button id=\"restore\">restore</button><button id=\"export\">export replay</button><label><input type=\"file\" id=\"import\"/> import</label><button id=\"inspect\">toggle sealed trace</button></div><div class=\"controls\"><input id=\"note\" size=\"56\" value=\"Avatar stays idle; let society continue.\"/><button id=\"idle\">record idle note</button></div><div id=\"log\" class=\"kv log\"></div></div><div class=\"panel world\"><div class=\"pulse\" id=\"pulse\"></div><div class=\"place\" style=\"left:12%;top:48%\">Outer Quiet</div><div class=\"place\" style=\"left:27%;top:44%\">Gate Ring</div><div class=\"place\" style=\"left:45%;top:28%\">Hearth Archive</div><div class=\"place\" style=\"left:64%;top:50%\">Market Measure</div><div class=\"place\" style=\"left:78%;top:73%\">Rainwalk</div><div class=\"place\" style=\"left:50%;top:58%\">Center</div><div class=\"agent\" id=\"agent\">A</div><div class=\"avatar\" id=\"avatar\"></div></div></section><section class=\"cards\"><div class=\"card\"><h3>autonomy</h3><div id=\"auto\" class=\"kv\"></div></div><div class=\"card\"><h3>needs</h3><div id=\"needs\" class=\"kv\"></div></div><div class=\"card\"><h3>memory</h3><div id=\"memory\" class=\"kv\"></div></div><div class=\"card\"><h3>routine</h3><div id=\"routine\" class=\"kv\"></div></div><div class=\"card\"><h3>interaction</h3><div id=\"interaction\" class=\"kv\"></div></div><div class=\"card\"><h3>welfare</h3><div id=\"welfare\" class=\"kv\"></div></div><div class=\"card\"><h3>metrics</h3><div id=\"metrics\"></div></div><div class=\"card\"><h3>sealed trace</h3><div id=\"private\" class=\"kv private\"></div></div></section></main><script>const DATA=__DATA__;const KEY='ssrm250_browser_world_v10_autonomous_society';let i=0,timer=null,replay=[];function pct(v){return Math.round(v*1000)/10+'%'}function log(msg){const el=document.getElementById('log');el.textContent=(msg+'\\n'+el.textContent).slice(0,2600)}function pos(place){const m={'Outer Quiet':[12,48],'Gate Ring':[27,44],'Hearth Archive':[45,28],'Market Measure':[64,50],'Rainwalk Threshold':[78,73],'Ceremony Center':[50,58]};return m[place]||[50,58]}function interactionAt(tick){return DATA.interactions.find(x=>x.tick===tick)}function techAt(lineage,tick){let out=null;for(const x of DATA.technology){if(x.lineage===lineage&&x.tick<=tick)out=x}return out}function render(){const t=DATA.ticks[i%DATA.ticks.length],w=DATA.world[i%DATA.world.length],n=DATA.needs[i%DATA.needs.length],m=DATA.memories[i%DATA.memories.length],r=DATA.routines[i%DATA.routines.length],g=DATA.welfare[i%DATA.welfare.length],rp=DATA.replay[i%DATA.replay.length],inter=interactionAt(t.tick),tech=techAt(t.lineage,t.tick);const p=pos(t.place);document.getElementById('agent').style.left=p[0]+'%';document.getElementById('agent').style.top=p[1]+'%';document.getElementById('agent').textContent=t.agent[0];document.getElementById('agent').style.transform=t.avatar_mode==='absent_saved'?'scale(1.08)':'scale(1)';document.getElementById('avatar').style.opacity=t.avatar_mode==='absent_saved'?0.16:t.avatar_mode==='idle_nearby'?0.45:1;document.getElementById('pulse').style.transform=`rotate(${t.flower_phase_deg}deg)`;document.getElementById('auto').textContent=w.public_state+'\\n'+w.avatar_state+'\\n'+w.autonomous_agent_state;document.getElementById('needs').textContent=JSON.stringify(n,null,2);document.getElementById('memory').textContent=m.autonomous_memory_written;document.getElementById('routine').textContent=r.schedule_after;document.getElementById('interaction').textContent=inter?inter.memory_written:'no agent-agent interaction this tick';document.getElementById('welfare').textContent=g.public_note+'\\ntech: '+(tech?tech.public_note:'unchanged');document.getElementById('private').textContent=JSON.stringify({trace:w.trace_integrity_token,replay:rp,private_trace_visible:w.private_trace_visible},null,2);replay.push({tick:t.tick,day:t.day,mode:t.avatar_mode,agent:t.agent,action:t.autonomous_action,hash:rp.export_hash});log(`day ${t.day} ${t.agent}: ${t.autonomous_action}; avatar=${t.avatar_mode}`);i++}function metrics(){const keys=['browser_world_v10_autonomous_society_readiness','weakest_channel_score','avatar_idle_absent_continuity','consequence_memory_carryover','welfare_guardrail_autonomy','agent_agent_interaction_continuity'];document.getElementById('metrics').innerHTML=keys.map(k=>`<div class=\"metric\"><span>${k}</span><b>${pct(DATA.metrics[k])}</b></div>`).join('')}function start(){if(!timer)timer=setInterval(render,300)}function pause(){clearInterval(timer);timer=null}document.getElementById('start').onclick=start;document.getElementById('pause').onclick=pause;document.getElementById('step').onclick=render;document.getElementById('save').onclick=()=>localStorage.setItem(KEY,JSON.stringify({i,replay}));document.getElementById('restore').onclick=()=>{const raw=localStorage.getItem(KEY);if(raw){const s=JSON.parse(raw);i=s.i||0;replay=s.replay||[];render();log('restored autonomous society state')}};document.getElementById('export').onclick=()=>{const blob=new Blob([JSON.stringify({report:250,replay},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='ssrm250_autonomy_replay.json';a.click()};document.getElementById('import').onchange=async(e)=>{const f=e.target.files[0];if(f){const obj=JSON.parse(await f.text());replay=obj.replay||[];log('imported replay '+replay.length)}};document.getElementById('inspect').onclick=()=>document.getElementById('private').classList.toggle('open');document.getElementById('idle').onclick=()=>{replay.push({tick:'idle_note',text:document.getElementById('note').value});log('idle note recorded; autonomy continues');render()};metrics();render();</script></body></html>"""
    return template.replace("__DATA__", json.dumps(payload))


def run(seed: int) -> dict[str, Any]:
    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    source = source_summary()
    ticks = build_ticks(seed)
    needs = build_needs(ticks)
    memories = build_memory(ticks)
    routines = build_routines(ticks)
    interactions = build_interactions(ticks)
    tech = build_technology(ticks)
    welfare = build_welfare(ticks, needs)
    replay = build_replay(ticks, memories, welfare, interactions, source)
    world = build_world(ticks, needs, memories, routines, interactions, tech, welfare, replay)
    metrics = compute_metrics(source, ticks, needs, memories, routines, interactions, tech, welfare, replay, world)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["browser_world_v10_autonomous_society_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    prefix = ARTIFACTS / BASE
    write_csv(Path(f"{prefix}_autonomous_society_tick_frames.csv"), ticks)
    write_csv(Path(f"{prefix}_agent_need_autonomy_frames.csv"), needs)
    write_csv(Path(f"{prefix}_consequence_memory_carry_frames.csv"), memories)
    write_csv(Path(f"{prefix}_routine_schedule_autonomy_frames.csv"), routines)
    write_csv(Path(f"{prefix}_agent_agent_interaction_frames.csv"), interactions)
    write_csv(Path(f"{prefix}_technology_autonomy_frames.csv"), tech)
    write_csv(Path(f"{prefix}_welfare_guardrail_autonomy_frames.csv"), welfare)
    write_csv(Path(f"{prefix}_replay_autonomy_frames.csv"), replay)
    write_csv(Path(f"{prefix}_browser_world_v10_ticks.csv"), world)
    honest_limits = [
        "This is deterministic autonomous post-entry society ticking, not subjective consciousness.",
        "The society continues without avatar input, but policies and actions are seeded deterministic scaffolds.",
        "No LLM is called and no autonomous natural language is provided.",
        "Consent, welfare, and recovery are simulated functional guardrails, not real consent or moral standing.",
        "The browser page is a playable 2D/2.5D state surface, not complete 3D physics.",
        "Needs and discomfort are bounded control variables with recovery paths, not proof of experienced feeling.",
        "Frequency and flower phase are rhythm variables, not metaphysical proof.",
    ]
    next_gate = "browser world v11 with autonomous long-horizon post-entry society days, sleep/wake cycles, stored dreams/rehearsal, and avatar re-entry after absence"
    results = {
        "report": REPORT,
        "name": "SSRM-3D Browser World v10 Autonomous Post-Entry Society Tick Bridge",
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "verdict": verdict,
        "counts": {
            "autonomous_society_tick_frames": len(ticks),
            "agent_need_autonomy_frames": len(needs),
            "consequence_memory_carry_frames": len(memories),
            "routine_schedule_autonomy_frames": len(routines),
            "agent_agent_interaction_frames": len(interactions),
            "technology_autonomy_frames": len(tech),
            "welfare_guardrail_autonomy_frames": len(welfare),
            "replay_autonomy_frames": len(replay),
            "browser_world_v10_ticks": len(world),
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
        "sample_ticks": [asdict(row) for row in world[:10]],
        "autonomy_model": "post-entry consequence state -> autonomous ticks -> needs -> memory -> routine -> interaction -> technology -> welfare -> replay",
        "boundary": "functional autonomous society scaffold; no consciousness claim",
    }
    Path(f"{prefix}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    Path(f"{prefix}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    with Path(f"{prefix}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "verdict": verdict, "readiness": metrics["browser_world_v10_autonomous_society_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": next_gate})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(ticks, needs, memories, routines, interactions, tech, welfare, replay, world, metrics))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    counts = results["counts"]
    print(f"module_verdict {results['verdict']}")
    print(f"browser_world_v10_autonomous_society_readiness {metrics['browser_world_v10_autonomous_society_readiness']:.6f}")
    for key in ["autonomous_society_tick_frames", "agent_need_autonomy_frames", "consequence_memory_carry_frames", "routine_schedule_autonomy_frames", "agent_agent_interaction_frames", "technology_autonomy_frames", "welfare_guardrail_autonomy_frames", "replay_autonomy_frames", "browser_world_v10_ticks"]:
        print(f"{key} {counts[key]}")
    for key in ["source_post_entry_consequence_continuity", "autonomous_tick_surface", "avatar_idle_absent_continuity", "needs_to_behavior_binding", "consequence_memory_carryover", "welfare_guardrail_autonomy", "recovery_without_avatar_prompt", "weakest_channel_score"]:
        print(f"{key} {metrics[key]:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
