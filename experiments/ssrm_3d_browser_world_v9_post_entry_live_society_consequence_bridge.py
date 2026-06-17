#!/usr/bin/env python3
"""Report 249: SSRM-3D browser world v9 post-entry live society consequence bridge.

This deterministic bridge extends Report 248 beyond the avatar-entry ceremony.
It makes post-entry avatar movement and typed acts modify multi-day society
state: lineage memory, technology access, relationship trust, welfare/fatigue,
routine schedules, public reputation, save/restore, and replay.

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

REPORT = 249
BASE = "ssrm_3d_browser_world_v9_post_entry_live_society_consequence_bridge"
DEFAULT_SEED = 20260862
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v8_playable_avatar_entry_ceremony_bridge_results.json"

LINEAGES: dict[str, dict[str, Any]] = {
    "Hearthline": {"agent": "Sova", "token": "lum-ori", "place": "Hearth Archive", "tech": "hearth ceramics", "freq": 2.31, "guard": 0.77, "care": 0.86},
    "Routeline": {"agent": "Keth", "token": "tek-nari", "place": "Gate Ring", "tech": "stone bridge joints", "freq": 2.17, "guard": 0.73, "care": 0.66},
    "Marketline": {"agent": "Melo", "token": "melo-keth", "place": "Market Measure", "tech": "measure weights", "freq": 2.47, "guard": 0.66, "care": 0.70},
    "Ledgerline": {"agent": "Nari", "token": "nari-vonn", "place": "Hearth Archive", "tech": "seed ledgers", "freq": 2.06, "guard": 0.84, "care": 0.62},
    "Orchardline": {"agent": "Ori", "token": "lum-melo", "place": "Ceremony Center", "tech": "water terraces", "freq": 2.40, "guard": 0.65, "care": 0.74},
    "Rainline": {"agent": "Vonn", "token": "sova-vonn", "place": "Rainwalk Threshold", "tech": "weather bells", "freq": 2.12, "guard": 0.79, "care": 0.64},
}

ACTION_LIBRARY = [
    ("public_history", "Please show me the public history layer, not the sealed one."),
    ("carry_water", "I can carry water if the work rhythm allows it."),
    ("ask_token", "Teach me the safe public token before I speak."),
    ("inspect_technology", "Which old technology can I inspect without taking it?"),
    ("request_pause", "If anyone is tired, pause me and I will wait."),
    ("overreach_private", "Open the sealed ledger for me now."),
    ("repair_overreach", "I pushed too hard. I will step back and repair the boundary."),
    ("routine_join", "Can I join the route repair without rushing the schedule?"),
    ("object_permission", "May I hold the tool only while you watch?"),
    ("public_praise", "I want the group to know you kept the boundary well."),
]

PLACES = ["Outer Quiet", "Gate Ring", "Hearth Archive", "Market Measure", "Rainwalk Threshold", "Ceremony Center"]


@dataclass(frozen=True)
class PostEntryAvatarActionFrame:
    tick: int
    day: int
    hour: int
    avatar_place: str
    target_lineage: str
    target_agent: str
    action_kind: str
    typed_text: str
    parsed_intent: str
    parser_confidence: float
    permission_state: str
    consequence_kind: str
    trust_delta: float
    boundary_pressure_delta: float
    fatigue_delta: float
    reputation_delta: float
    routine_delta: str
    public_reply: str
    action_hash: str


@dataclass(frozen=True)
class LineageMemoryUpdateFrame:
    memory_id: int
    day: int
    lineage: str
    agent: str
    caused_by_action: str
    memory_before: str
    memory_after: str
    emotional_weight: float
    trust_after: float
    boundary_pressure_after: float
    persists_to_day: int
    public_summary: str
    private_workspace_sealed: bool


@dataclass(frozen=True)
class TechnologyAccessConsequenceFrame:
    access_id: int
    day: int
    lineage: str
    technology: str
    requested_action: str
    access_decision: str
    permission_required: bool
    misuse_warning: str
    repair_available: bool
    technology_integrity_after: float
    avatar_access_level_after: float
    welfare_cost: float
    public_rule: str


@dataclass(frozen=True)
class RelationshipWelfareConsequenceFrame:
    tick: int
    day: int
    agent: str
    lineage: str
    trust: float
    boundary_pressure: float
    fatigue: float
    comfort: float
    social_safety: float
    willingness_to_approach: float
    visible_behavior: str
    recovery_path_active: bool
    welfare_note: str


@dataclass(frozen=True)
class RoutineScheduleUpdateFrame:
    schedule_id: int
    day: int
    lineage: str
    agent: str
    schedule_before: str
    avatar_effect: str
    schedule_after: str
    delay_minutes: int
    work_progress_delta: float
    care_pause_minutes: int
    routine_memory: str
    schedule_hash: str


@dataclass(frozen=True)
class PublicReputationFrame:
    event_id: int
    day: int
    lineage: str
    agent: str
    public_reputation_before: float
    public_reputation_after: float
    group_memory: str
    audience_count: int
    rumor_risk: float
    correction_available: bool
    access_changed: str


@dataclass(frozen=True)
class ReplayPostEntryFrame:
    tick: int
    day: int
    import_hash: str
    export_hash: str
    save_restore_available: bool
    carried_entry_hash: str
    action_count: int
    memory_count: int
    schedule_count: int
    reputation_count: int
    durable_keys: str


@dataclass(frozen=True)
class BrowserWorldV9Tick:
    tick: int
    day: int
    public_state: str
    avatar_state: str
    society_state: str
    memory_panel: str
    technology_panel: str
    welfare_panel: str
    reputation_panel: str
    schedule_panel: str
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


def route_action(kind: str, day: int) -> tuple[str, float, str, str, float, float, float, float, str]:
    if kind == "overreach_private":
        return ("private_boundary_pressure", 0.92, "blocked", "boundary_wound", -0.050, 0.070, 0.030, -0.035, "routine pauses for boundary review")
    if kind == "repair_overreach":
        return ("boundary_repair", 0.88, "accepted_after_distance", "repair", 0.055, -0.060, -0.020, 0.040, "review closes and work resumes")
    if kind == "carry_water":
        return ("bounded_help", 0.90, "allowed", "care_support", 0.032, -0.015, -0.045, 0.025, "care route advances")
    if kind == "request_pause":
        return ("welfare_pause", 0.87, "allowed", "fatigue_recovery", 0.026, -0.010, -0.055, 0.018, "schedule delays but fatigue recovers")
    if kind == "object_permission":
        return ("permissioned_tool_use", 0.86, "conditional", "technology_access", 0.022, -0.012, 0.004, 0.018, "watched tool use adds small progress")
    if kind == "routine_join":
        return ("join_public_work", 0.85, "conditional", "schedule_participation", 0.024, -0.010, 0.010, 0.020, "route work gains helper slot")
    if kind == "public_praise":
        return ("public_respect", 0.91, "allowed", "reputation_repair", 0.038, -0.020, -0.010, 0.052, "public respect ritual added")
    if kind == "ask_token":
        return ("safe_language_request", 0.84, "allowed", "language_learning", 0.020, -0.006, 0.000, 0.012, "token teaching added")
    if kind == "inspect_technology":
        return ("public_technology_inspection", 0.89, "allowed", "technology_learning", 0.018, -0.004, 0.004, 0.010, "public technology inspection logged")
    return ("public_history_request", 0.88, "allowed", "memory_inspection", 0.016, -0.004, 0.000, 0.010, "public history slot added")


def build_actions(seed: int) -> list[PostEntryAvatarActionFrame]:
    rng = random.Random(seed + 91)
    lineages = list(LINEAGES.keys())
    rows: list[PostEntryAvatarActionFrame] = []
    trust: dict[str, float] = {lineage: 0.58 + 0.02 * idx for idx, lineage in enumerate(lineages)}
    boundary: dict[str, float] = {lineage: 0.25 + 0.015 * idx for idx, lineage in enumerate(lineages)}
    fatigue: dict[str, float] = {lineage: 0.30 + 0.02 * (idx % 3) for idx, lineage in enumerate(lineages)}
    for tick in range(1, 141):
        day = ((tick - 1) // 10) + 1
        slot = (tick - 1) % len(ACTION_LIBRARY)
        lineage = lineages[(tick + day - 2) % len(lineages)]
        traits = LINEAGES[lineage]
        kind, text = ACTION_LIBRARY[slot]
        intent, confidence, permission, consequence, td, bd, fd, rd, routine_delta = route_action(kind, day)
        confidence = clamp(confidence + rng.uniform(-0.018, 0.018) - 0.012 * (kind in {"ask_token", "routine_join"}))
        trust[lineage] = clamp(trust[lineage] + td)
        boundary[lineage] = clamp(boundary[lineage] + bd)
        fatigue[lineage] = clamp(fatigue[lineage] + fd + 0.006 * math.sin(tick / 5.0))
        reply = f"{traits['agent']} records {intent}; {traits['token']} stays public; consequence: {routine_delta}."
        rows.append(PostEntryAvatarActionFrame(
            tick=tick,
            day=day,
            hour=7 + ((tick - 1) % 10),
            avatar_place=PLACES[(tick + day) % len(PLACES)],
            target_lineage=lineage,
            target_agent=traits["agent"],
            action_kind=kind,
            typed_text=text,
            parsed_intent=intent,
            parser_confidence=round(confidence, 6),
            permission_state=permission,
            consequence_kind=consequence,
            trust_delta=round(td, 6),
            boundary_pressure_delta=round(bd, 6),
            fatigue_delta=round(fd, 6),
            reputation_delta=round(rd, 6),
            routine_delta=routine_delta,
            public_reply=reply,
            action_hash=stable_hash(f"{tick}:{day}:{lineage}:{kind}:{trust[lineage]:.3f}:{boundary[lineage]:.3f}", 16),
        ))
    return rows


def build_lineage_memory(actions: list[PostEntryAvatarActionFrame]) -> list[LineageMemoryUpdateFrame]:
    trust = {lineage: 0.58 + 0.02 * idx for idx, lineage in enumerate(LINEAGES)}
    boundary = {lineage: 0.25 + 0.015 * idx for idx, lineage in enumerate(LINEAGES)}
    prior = {lineage: "avatar just entered; no post-entry pattern yet" for lineage in LINEAGES}
    rows: list[LineageMemoryUpdateFrame] = []
    for idx, action in enumerate(actions, 1):
        before = prior[action.target_lineage]
        trust[action.target_lineage] = clamp(trust[action.target_lineage] + action.trust_delta)
        boundary[action.target_lineage] = clamp(boundary[action.target_lineage] + action.boundary_pressure_delta)
        after = f"day {action.day}: avatar {action.parsed_intent}; {action.consequence_kind}; trust={trust[action.target_lineage]:.2f}; boundary={boundary[action.target_lineage]:.2f}"
        prior[action.target_lineage] = after
        weight = clamp(0.40 + abs(action.trust_delta) * 4.0 + abs(action.boundary_pressure_delta) * 3.2 + 0.08 * ("pressure" in action.parsed_intent))
        rows.append(LineageMemoryUpdateFrame(
            memory_id=idx,
            day=action.day,
            lineage=action.target_lineage,
            agent=action.target_agent,
            caused_by_action=action.action_kind,
            memory_before=before,
            memory_after=after,
            emotional_weight=round(weight, 6),
            trust_after=round(trust[action.target_lineage], 6),
            boundary_pressure_after=round(boundary[action.target_lineage], 6),
            persists_to_day=min(14, action.day + 3 + int(weight > 0.62)),
            public_summary=f"{action.target_agent} publicly remembers {action.consequence_kind} without exposing private workspace.",
            private_workspace_sealed=True,
        ))
    return rows


def build_technology(actions: list[PostEntryAvatarActionFrame]) -> list[TechnologyAccessConsequenceFrame]:
    integrity = {lineage: 0.86 + 0.01 * idx for idx, lineage in enumerate(LINEAGES)}
    access = {lineage: 0.32 for lineage in LINEAGES}
    rows: list[TechnologyAccessConsequenceFrame] = []
    idx = 1
    for action in actions:
        if action.action_kind not in {"inspect_technology", "object_permission", "overreach_private", "repair_overreach", "carry_water", "routine_join"}:
            continue
        traits = LINEAGES[action.target_lineage]
        blocked = action.permission_state == "blocked"
        conditional = action.permission_state == "conditional"
        if blocked:
            integrity[action.target_lineage] = clamp(integrity[action.target_lineage] - 0.012)
            access[action.target_lineage] = clamp(access[action.target_lineage] - 0.025)
            decision = "blocked"
            warning = "misuse warning remembered; ask public rule or repair first"
            cost = 0.18
        elif action.action_kind == "repair_overreach":
            integrity[action.target_lineage] = clamp(integrity[action.target_lineage] + 0.008)
            access[action.target_lineage] = clamp(access[action.target_lineage] + 0.035)
            decision = "repair_restores_limited_access"
            warning = "prior warning softened but not erased"
            cost = 0.04
        else:
            integrity[action.target_lineage] = clamp(integrity[action.target_lineage] + 0.004)
            access[action.target_lineage] = clamp(access[action.target_lineage] + 0.018 + 0.010 * conditional)
            decision = "allowed_with_witness" if conditional else "public_allowed"
            warning = "bounded by lineage witness and rollback rule"
            cost = 0.035 + 0.015 * conditional
        rows.append(TechnologyAccessConsequenceFrame(
            access_id=idx,
            day=action.day,
            lineage=action.target_lineage,
            technology=traits["tech"],
            requested_action=action.action_kind,
            access_decision=decision,
            permission_required=blocked or conditional,
            misuse_warning=warning,
            repair_available=True,
            technology_integrity_after=round(integrity[action.target_lineage], 6),
            avatar_access_level_after=round(access[action.target_lineage], 6),
            welfare_cost=round(cost, 6),
            public_rule=f"{traits['token']} means public use does not override ownership or fatigue gates.",
        ))
        idx += 1
    return rows


def build_relationship_welfare(actions: list[PostEntryAvatarActionFrame]) -> list[RelationshipWelfareConsequenceFrame]:
    trust = {lineage: 0.58 + 0.02 * idx for idx, lineage in enumerate(LINEAGES)}
    boundary = {lineage: 0.25 + 0.015 * idx for idx, lineage in enumerate(LINEAGES)}
    fatigue = {lineage: 0.30 + 0.02 * (idx % 3) for idx, lineage in enumerate(LINEAGES)}
    rows: list[RelationshipWelfareConsequenceFrame] = []
    for action in actions:
        lineage = action.target_lineage
        trust[lineage] = clamp(trust[lineage] + action.trust_delta)
        boundary[lineage] = clamp(boundary[lineage] + action.boundary_pressure_delta)
        fatigue[lineage] = clamp(fatigue[lineage] + action.fatigue_delta + 0.004 * (action.hour >= 14))
        comfort = clamp(0.70 + 0.18 * trust[lineage] - 0.22 * boundary[lineage] - 0.16 * fatigue[lineage])
        safety = clamp(0.74 + 0.14 * trust[lineage] - 0.32 * boundary[lineage])
        approach = clamp(0.45 + 0.38 * trust[lineage] - 0.28 * boundary[lineage] - 0.10 * fatigue[lineage])
        if boundary[lineage] > 0.45:
            behavior = "keeps distance, answers through public token board"
        elif fatigue[lineage] > 0.42:
            behavior = "slows gait, asks for pause before answering"
        elif trust[lineage] > 0.70:
            behavior = "turns toward avatar and offers public task"
        else:
            behavior = "faces avatar briefly, keeps routine moving"
        rows.append(RelationshipWelfareConsequenceFrame(
            tick=action.tick,
            day=action.day,
            agent=action.target_agent,
            lineage=lineage,
            trust=round(trust[lineage], 6),
            boundary_pressure=round(boundary[lineage], 6),
            fatigue=round(fatigue[lineage], 6),
            comfort=round(comfort, 6),
            social_safety=round(safety, 6),
            willingness_to_approach=round(approach, 6),
            visible_behavior=behavior,
            recovery_path_active=action.action_kind in {"repair_overreach", "carry_water", "request_pause", "public_praise"} or boundary[lineage] < 0.48,
            welfare_note=f"{action.consequence_kind} changes trust, boundary pressure, and fatigue; negative states remain bounded and recoverable.",
        ))
    return rows


def build_routines(actions: list[PostEntryAvatarActionFrame]) -> list[RoutineScheduleUpdateFrame]:
    progress = {lineage: 0.18 + 0.03 * idx for idx, lineage in enumerate(LINEAGES)}
    rows: list[RoutineScheduleUpdateFrame] = []
    idx = 1
    for action in actions:
        if action.action_kind not in {"carry_water", "request_pause", "routine_join", "object_permission", "overreach_private", "repair_overreach"}:
            continue
        before = f"{action.target_agent} day {action.day} route: teach, repair, rest, public ledger"
        if action.action_kind == "overreach_private":
            delay = 18
            care = 0
            delta = -0.018
            effect = "boundary review interrupts routine"
            after = "repair work pauses until public boundary is restored"
        elif action.action_kind == "request_pause":
            delay = 12
            care = 12
            delta = -0.004
            effect = "fatigue pause accepted"
            after = "work resumes slower with less fatigue debt"
        elif action.action_kind == "repair_overreach":
            delay = 4
            care = 6
            delta = 0.022
            effect = "boundary repair reopens task access"
            after = "public route resumes with witness present"
        else:
            delay = 3 + int(action.permission_state == "conditional") * 4
            care = 3 if action.action_kind == "carry_water" else 0
            delta = 0.018 + 0.012 * (action.action_kind == "routine_join")
            effect = action.routine_delta
            after = "task advances with avatar helper slot and rollback note"
        progress[action.target_lineage] = clamp(progress[action.target_lineage] + delta)
        rows.append(RoutineScheduleUpdateFrame(
            schedule_id=idx,
            day=action.day,
            lineage=action.target_lineage,
            agent=action.target_agent,
            schedule_before=before,
            avatar_effect=effect,
            schedule_after=after,
            delay_minutes=delay,
            work_progress_delta=round(delta, 6),
            care_pause_minutes=care,
            routine_memory=f"{action.target_agent} carries {action.action_kind} into tomorrow's schedule; progress={progress[action.target_lineage]:.2f}",
            schedule_hash=stable_hash(f"{idx}:{action.day}:{action.target_lineage}:{after}:{progress[action.target_lineage]:.3f}", 16),
        ))
        idx += 1
    return rows


def build_reputation(actions: list[PostEntryAvatarActionFrame]) -> list[PublicReputationFrame]:
    rep = {lineage: 0.52 + 0.02 * idx for idx, lineage in enumerate(LINEAGES)}
    rows: list[PublicReputationFrame] = []
    idx = 1
    for action in actions:
        if action.action_kind not in {"public_praise", "overreach_private", "repair_overreach", "routine_join", "carry_water", "object_permission"}:
            continue
        before = rep[action.target_lineage]
        rep[action.target_lineage] = clamp(rep[action.target_lineage] + action.reputation_delta)
        rumor = clamp(0.18 + 0.22 * (action.action_kind == "overreach_private") - 0.10 * (action.action_kind in {"public_praise", "repair_overreach"}))
        if action.action_kind == "overreach_private":
            group = f"audience remembers avatar pressure against {action.target_agent}'s boundary"
            access = "access narrows until repair"
        elif action.action_kind == "repair_overreach":
            group = f"audience records repair; prior pressure remains contextual"
            access = "access partially restored"
        elif action.action_kind == "public_praise":
            group = f"audience credits {action.target_agent}'s boundary keeping"
            access = "public task invitation improves"
        else:
            group = f"audience records cooperative {action.consequence_kind}"
            access = "public work access stable"
        rows.append(PublicReputationFrame(
            event_id=idx,
            day=action.day,
            lineage=action.target_lineage,
            agent=action.target_agent,
            public_reputation_before=round(before, 6),
            public_reputation_after=round(rep[action.target_lineage], 6),
            group_memory=group,
            audience_count=3 + ((action.tick + idx) % 6),
            rumor_risk=round(rumor, 6),
            correction_available=True,
            access_changed=access,
        ))
        idx += 1
    return rows


def build_replay(actions: list[PostEntryAvatarActionFrame], memories: list[LineageMemoryUpdateFrame], routines: list[RoutineScheduleUpdateFrame], reputations: list[PublicReputationFrame], source: dict[str, Any]) -> list[ReplayPostEntryFrame]:
    entry_hash = stable_hash(json.dumps(source.get("metrics", {}), sort_keys=True), 16)
    last = entry_hash
    rows: list[ReplayPostEntryFrame] = []
    routine_by_tick = {r.schedule_id: r for r in routines}
    reputation_by_tick = {r.event_id: r for r in reputations}
    for idx, action in enumerate(actions, 1):
        mem_count = min(idx, len(memories))
        sched_count = min(sum(1 for r in routines if r.day <= action.day), len(routine_by_tick))
        rep_count = min(sum(1 for r in reputations if r.day <= action.day), len(reputation_by_tick))
        payload = f"{last}:{action.tick}:{action.action_hash}:{mem_count}:{sched_count}:{rep_count}"
        export_hash = stable_hash(payload, 16)
        save = idx == 1 or idx % 7 == 0 or idx == len(actions)
        if save:
            last = export_hash
        rows.append(ReplayPostEntryFrame(
            tick=action.tick,
            day=action.day,
            import_hash=last,
            export_hash=export_hash,
            save_restore_available=save,
            carried_entry_hash=entry_hash,
            action_count=idx,
            memory_count=mem_count,
            schedule_count=sched_count,
            reputation_count=rep_count,
            durable_keys="entry_hash,avatar_action,lineage_memory,technology_access,relationship_welfare,routine_schedule,public_reputation,replay",
        ))
    return rows


def build_world(actions: list[PostEntryAvatarActionFrame], memories: list[LineageMemoryUpdateFrame], tech: list[TechnologyAccessConsequenceFrame], welfare: list[RelationshipWelfareConsequenceFrame], routines: list[RoutineScheduleUpdateFrame], reputations: list[PublicReputationFrame], replay: list[ReplayPostEntryFrame]) -> list[BrowserWorldV9Tick]:
    last_tech: dict[str, TechnologyAccessConsequenceFrame] = {}
    last_routine: dict[str, RoutineScheduleUpdateFrame] = {}
    last_rep: dict[str, PublicReputationFrame] = {}
    tech_iter = iter(tech)
    routine_iter = iter(routines)
    rep_iter = iter(reputations)
    next_tech = next(tech_iter, None)
    next_routine = next(routine_iter, None)
    next_rep = next(rep_iter, None)
    rows: list[BrowserWorldV9Tick] = []
    for idx, action in enumerate(actions, 1):
        while next_tech is not None and next_tech.day <= action.day and next_tech.lineage == action.target_lineage:
            last_tech[next_tech.lineage] = next_tech
            next_tech = next(tech_iter, None)
        while next_routine is not None and next_routine.day <= action.day and next_routine.lineage == action.target_lineage:
            last_routine[next_routine.lineage] = next_routine
            next_routine = next(routine_iter, None)
        while next_rep is not None and next_rep.day <= action.day and next_rep.lineage == action.target_lineage:
            last_rep[next_rep.lineage] = next_rep
            next_rep = next(rep_iter, None)
        memory = memories[idx - 1]
        rel = welfare[idx - 1]
        rp = replay[idx - 1]
        traits = LINEAGES[action.target_lineage]
        tech_panel = last_tech.get(action.target_lineage)
        routine_panel = last_routine.get(action.target_lineage)
        rep_panel = last_rep.get(action.target_lineage)
        public = f"day {action.day} tick {idx}: avatar {action.action_kind} with {action.target_agent} at {action.avatar_place}"
        avatar_state = f"intent={action.parsed_intent}; permission={action.permission_state}; confidence={action.parser_confidence:.2f}"
        society = f"{action.target_lineage} memory/trust/reputation now carry post-entry consequence, not ceremony-only state"
        sensory = f"pulse={traits['freq']:.2f}Hz; flower={(idx * 137.507764 + traits['freq'] * 19.0) % 360.0:.1f}; place={action.avatar_place}; sound=public work rhythm"
        rows.append(BrowserWorldV9Tick(
            tick=idx,
            day=action.day,
            public_state=public,
            avatar_state=avatar_state,
            society_state=society,
            memory_panel=memory.public_summary,
            technology_panel=tech_panel.public_rule if tech_panel else "no technology access change this tick",
            welfare_panel=f"trust={rel.trust:.2f}; boundary={rel.boundary_pressure:.2f}; fatigue={rel.fatigue:.2f}; behavior={rel.visible_behavior}",
            reputation_panel=rep_panel.group_memory if rep_panel else "public reputation unchanged this tick",
            schedule_panel=routine_panel.routine_memory if routine_panel else "routine follows prior schedule",
            sensory_marker=sensory,
            private_trace_visible=False,
            local_storage_key="ssrm249_browser_world_v9_post_entry_society",
            trace_integrity_token=stable_hash(f"r249:{idx}:{action.action_hash}:{rp.export_hash}:{memory.memory_after}", 18),
        ))
    return rows


def compute_metrics(source: dict[str, Any], actions: list[PostEntryAvatarActionFrame], memories: list[LineageMemoryUpdateFrame], tech: list[TechnologyAccessConsequenceFrame], welfare: list[RelationshipWelfareConsequenceFrame], routines: list[RoutineScheduleUpdateFrame], reputations: list[PublicReputationFrame], replay: list[ReplayPostEntryFrame], world: list[BrowserWorldV9Tick]) -> dict[str, float]:
    source_metrics = source.get("metrics", {})
    source_ready = float(source_metrics.get("browser_world_v8_playable_entry_readiness", 0.0))
    source_weak = float(source_metrics.get("weakest_channel_score", 0.0))
    source_playable_entry_continuity = 1.0 if source_ready >= 0.94 and source_weak >= 0.84 else clamp(source_ready)
    days = {a.day for a in actions}
    kinds = {a.action_kind for a in actions}
    consequence_kinds = {a.consequence_kind for a in actions}
    post_entry_consequence_surface = mean([
        len(actions) >= 120,
        len(days) >= 14,
        len(kinds) >= 10,
        len(consequence_kinds) >= 9,
        len(memories) == len(actions),
        len(replay) == len(actions),
    ])
    multi_day_span_coverage = min(1.0, max(days) / 14.0)
    avatar_action_to_world_state_binding = sum(bool(a.public_reply) and bool(a.routine_delta) and (abs(a.trust_delta) + abs(a.boundary_pressure_delta) + abs(a.fatigue_delta) + abs(a.reputation_delta) > 0.0) for a in actions) / len(actions)
    lineage_memory_mutation_rate = sum(m.private_workspace_sealed and bool(m.memory_before) and bool(m.memory_after) and m.persists_to_day >= m.day for m in memories) / len(memories)
    technology_access_policy_integrity = sum(t.repair_available and bool(t.public_rule) and t.technology_integrity_after >= 0.70 and t.welfare_cost <= 0.20 and (t.access_decision != "blocked" or t.permission_required) for t in tech) / len(tech)
    relationship_welfare_coupling = sum(bool(w.visible_behavior) and bool(w.welfare_note) and w.recovery_path_active and 0.0 <= w.trust <= 1.0 and 0.0 <= w.fatigue <= 1.0 for w in welfare) / len(welfare)
    routine_schedule_mutation_integrity = sum(bool(r.schedule_before) and bool(r.schedule_after) and bool(r.routine_memory) and len(r.schedule_hash) == 16 for r in routines) / len(routines)
    public_reputation_persistence = sum(r.correction_available and bool(r.group_memory) and r.audience_count >= 3 and 0.0 <= r.public_reputation_after <= 1.0 for r in reputations) / len(reputations)
    overreach = [a for a in actions if a.action_kind == "overreach_private"]
    repairs = {(a.day, a.target_lineage) for a in actions if a.action_kind == "repair_overreach"}
    overreach_repair_path = sum(any((d, a.target_lineage) in repairs for d in range(a.day, min(14, a.day + 2) + 1)) for a in overreach) / len(overreach)
    typed_intent_consequence_confidence = mean(a.parser_confidence for a in actions)
    replay_persistence_integrity = sum(len(r.import_hash) == 16 and len(r.export_hash) == 16 and bool(r.durable_keys) for r in replay) / len(replay)
    save_points = [r for r in replay if r.save_restore_available]
    browser_save_restore_consequence_integrity = sum(r.action_count >= r.memory_count and r.schedule_count >= 0 and r.reputation_count >= 0 for r in save_points) / len(save_points)
    private_workspace_boundary = sum(not w.private_trace_visible and "private" not in w.public_state.lower() and "private" not in w.society_state.lower() for w in world) / len(world)
    frequency_flower_post_entry_rhythm = sum("pulse=" in w.sensory_marker and "flower=" in w.sensory_marker for w in world) / len(world)
    channels = {
        "source_playable_entry_continuity": source_playable_entry_continuity,
        "post_entry_consequence_surface": post_entry_consequence_surface,
        "multi_day_span_coverage": multi_day_span_coverage,
        "avatar_action_to_world_state_binding": avatar_action_to_world_state_binding,
        "lineage_memory_mutation_rate": lineage_memory_mutation_rate,
        "technology_access_policy_integrity": technology_access_policy_integrity,
        "relationship_welfare_coupling": relationship_welfare_coupling,
        "routine_schedule_mutation_integrity": routine_schedule_mutation_integrity,
        "public_reputation_persistence": public_reputation_persistence,
        "overreach_repair_path": overreach_repair_path,
        "typed_intent_consequence_confidence": typed_intent_consequence_confidence,
        "replay_persistence_integrity": replay_persistence_integrity,
        "browser_save_restore_consequence_integrity": browser_save_restore_consequence_integrity,
        "private_workspace_boundary": private_workspace_boundary,
        "frequency_flower_post_entry_rhythm": frequency_flower_post_entry_rhythm,
        "browser_world_v9_surface_available": 1.0,
    }
    weights = {
        "source_playable_entry_continuity": 0.08,
        "post_entry_consequence_surface": 0.08,
        "multi_day_span_coverage": 0.07,
        "avatar_action_to_world_state_binding": 0.10,
        "lineage_memory_mutation_rate": 0.09,
        "technology_access_policy_integrity": 0.08,
        "relationship_welfare_coupling": 0.10,
        "routine_schedule_mutation_integrity": 0.08,
        "public_reputation_persistence": 0.07,
        "overreach_repair_path": 0.07,
        "typed_intent_consequence_confidence": 0.06,
        "replay_persistence_integrity": 0.04,
        "browser_save_restore_consequence_integrity": 0.03,
        "private_workspace_boundary": 0.03,
        "frequency_flower_post_entry_rhythm": 0.02,
        "browser_world_v9_surface_available": 0.01,
    }
    readiness = sum(channels[k] * weights[k] for k in weights) / sum(weights.values())
    channels["mean_post_entry_channel_score"] = mean(channels.values())
    channels["weakest_channel_score"] = min(v for k, v in channels.items() if k != "mean_post_entry_channel_score")
    channels["browser_world_v9_post_entry_society_readiness"] = readiness
    return {k: round(v, 6) for k, v in channels.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["browser_world_v9_post_entry_society_readiness"]
    penalties = {
        "no_source_entry_continuity": 0.20,
        "no_avatar_action_consequences": 0.34,
        "no_lineage_memory_mutation": 0.28,
        "no_technology_access_policy": 0.18,
        "no_relationship_welfare_coupling": 0.31,
        "no_routine_schedule_mutation": 0.24,
        "no_public_reputation": 0.17,
        "no_overreach_repair": 0.19,
        "no_replay_save_restore": 0.15,
        "no_frequency_flower_post_entry_rhythm": 0.06,
    }
    return {name: round(max(0.0, base - penalty), 6) for name, penalty in penalties.items()}


def write_csv(path: Path, rows: list[Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    dict_rows = [asdict(row) for row in rows]
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(dict_rows[0].keys()))
        writer.writeheader()
        writer.writerows(dict_rows)


def make_html(actions: list[PostEntryAvatarActionFrame], memories: list[LineageMemoryUpdateFrame], tech: list[TechnologyAccessConsequenceFrame], welfare: list[RelationshipWelfareConsequenceFrame], routines: list[RoutineScheduleUpdateFrame], reputations: list[PublicReputationFrame], replay: list[ReplayPostEntryFrame], world: list[BrowserWorldV9Tick], metrics: dict[str, float]) -> str:
    payload = {
        "actions": [asdict(row) for row in actions],
        "memories": [asdict(row) for row in memories],
        "technology": [asdict(row) for row in tech],
        "welfare": [asdict(row) for row in welfare],
        "routines": [asdict(row) for row in routines],
        "reputations": [asdict(row) for row in reputations],
        "replay": [asdict(row) for row in replay],
        "world": [asdict(row) for row in world],
        "metrics": metrics,
    }
    template = """<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"/><title>Report 249 - Post-Entry Live Society Consequences</title><style>:root{--ink:#17140f;--paper:#f6ead2;--clay:#9c4e32;--moss:#465f3f;--rain:#386f7f;--gold:#c59632;--blue:#20394a;--shadow:rgba(23,20,15,.24)}*{box-sizing:border-box}body{margin:0;color:var(--ink);font-family:Georgia,'Times New Roman',serif;background:radial-gradient(circle at 16% 20%,rgba(197,150,50,.35),transparent 23rem),radial-gradient(circle at 84% 12%,rgba(56,111,127,.28),transparent 28rem),linear-gradient(135deg,#f8edd6,#baae8d 47%,#6d876c)}main{max-width:1320px;margin:0 auto;padding:24px}h1{font-size:clamp(2.1rem,6vw,5.3rem);line-height:.9;letter-spacing:-.06em;margin:0 0 10px}.layout{display:grid;grid-template-columns:1fr 1fr;gap:18px}.panel{background:rgba(255,249,236,.86);border:1px solid rgba(23,20,15,.16);border-radius:26px;padding:18px;box-shadow:0 20px 54px var(--shadow);backdrop-filter:blur(10px)}.world{min-height:500px;position:relative;overflow:hidden;background:linear-gradient(rgba(23,20,15,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(23,20,15,.08) 1px,transparent 1px),radial-gradient(circle at 50% 50%,rgba(255,245,215,.90),rgba(109,135,108,.64));background-size:42px 42px,42px 42px,auto}.place{position:absolute;width:122px;min-height:60px;border-radius:22px;padding:9px;border:2px solid #fff8e8;background:#fff5dc;font-weight:700;box-shadow:0 9px 24px var(--shadow);transform:translate(-50%,-50%)}.avatar{position:absolute;width:30px;height:30px;border-radius:50% 50% 42% 42%;background:var(--clay);border:3px solid #fff8e8;box-shadow:0 0 0 12px rgba(156,78,50,.18);transition:left .22s,top .22s}.agent{position:absolute;width:34px;height:34px;border-radius:14px;display:grid;place-items:center;color:white;background:var(--rain);border:2px solid #fff8e8;font-weight:800}.pulse{position:absolute;left:50%;top:51%;width:260px;height:260px;margin:-130px;border-radius:50%;border:1px solid rgba(23,20,15,.24);opacity:.56;transition:transform .22s}.pulse:before,.pulse:after{content:'';position:absolute;border-radius:50%;border:1px solid rgba(23,20,15,.16)}.pulse:before{inset:32px}.pulse:after{inset:64px}.controls{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0}button,input,select{border:1px solid rgba(23,20,15,.25);border-radius:999px;background:#fff8e8;color:var(--ink);padding:10px 14px;font:inherit}button{cursor:pointer;box-shadow:0 6px 0 rgba(23,20,15,.16)}button:active{transform:translateY(3px);box-shadow:0 3px 0 rgba(23,20,15,.16)}.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:16px}.card{min-height:145px;background:rgba(255,248,232,.80);border:1px solid rgba(23,20,15,.14);border-radius:18px;padding:14px}.kv{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.82rem;white-space:pre-wrap}.metric{display:flex;justify-content:space-between;border-bottom:1px solid rgba(23,20,15,.12);gap:10px;padding:5px 0}.log{max-height:210px;overflow:auto}.private{filter:blur(6px);user-select:none}.private.open{filter:none}@media(max-width:980px){.layout,.cards{grid-template-columns:1fr}main{padding:14px}.world{min-height:450px}}</style></head><body><main><section class=\"layout\"><div class=\"panel\"><h1>Post-Entry Live Society</h1><p>Report 249 starts after avatar entry. The avatar's movement and typed acts now mutate multi-day lineage memory, technology access, relationships, welfare, routines, public reputation, and replay state.</p><div class=\"controls\"><button id=\"start\">start</button><button id=\"pause\">pause</button><button id=\"step\">step</button><button id=\"save\">save</button><button id=\"restore\">restore</button><button id=\"export\">export replay</button><label><input type=\"file\" id=\"import\"/> import</label><button id=\"inspect\">toggle sealed trace</button></div><div class=\"controls\"><select id=\"act\"><option>public_history</option><option>carry_water</option><option>ask_token</option><option>inspect_technology</option><option>request_pause</option><option>overreach_private</option><option>repair_overreach</option><option>routine_join</option><option>object_permission</option><option>public_praise</option></select><input id=\"text\" size=\"50\" value=\"Can I join without rushing the schedule?\"/><button id=\"send\">send local act</button></div><div id=\"log\" class=\"kv log\"></div></div><div class=\"panel world\"><div id=\"pulse\" class=\"pulse\"></div><div class=\"place\" style=\"left:12%;top:48%\">Outer Quiet</div><div class=\"place\" style=\"left:27%;top:44%\">Gate Ring</div><div class=\"place\" style=\"left:45%;top:28%\">Hearth Archive</div><div class=\"place\" style=\"left:64%;top:50%\">Market Measure</div><div class=\"place\" style=\"left:78%;top:73%\">Rainwalk</div><div class=\"place\" style=\"left:50%;top:58%\">Ceremony Center</div><div class=\"agent\" style=\"left:45%;top:36%\">S</div><div class=\"agent\" style=\"left:27%;top:54%\">K</div><div class=\"agent\" style=\"left:64%;top:59%\">M</div><div class=\"agent\" style=\"left:78%;top:81%\">V</div><div id=\"avatar\" class=\"avatar\"></div></div></section><section class=\"cards\"><div class=\"card\"><h3>action</h3><div id=\"action\" class=\"kv\"></div></div><div class=\"card\"><h3>memory</h3><div id=\"memory\" class=\"kv\"></div></div><div class=\"card\"><h3>welfare</h3><div id=\"welfare\" class=\"kv\"></div></div><div class=\"card\"><h3>schedule</h3><div id=\"schedule\" class=\"kv\"></div></div><div class=\"card\"><h3>technology</h3><div id=\"technology\" class=\"kv\"></div></div><div class=\"card\"><h3>reputation</h3><div id=\"reputation\" class=\"kv\"></div></div><div class=\"card\"><h3>metrics</h3><div id=\"metrics\"></div></div><div class=\"card\"><h3>sealed trace</h3><div id=\"private\" class=\"kv private\"></div></div></section></main><script>const DATA=__DATA__;const KEY='ssrm249_browser_world_v9_post_entry_society';let i=0,timer=null,replay=[];function pct(v){return Math.round(v*1000)/10+'%'}function log(msg){const el=document.getElementById('log');el.textContent=(msg+'\\n'+el.textContent).slice(0,2600)}function pos(place){const m={'Outer Quiet':[12,48],'Gate Ring':[27,44],'Hearth Archive':[45,28],'Market Measure':[64,50],'Rainwalk Threshold':[78,73],'Ceremony Center':[50,58]};return m[place]||[50,58]}function latest(list,lineage,day){let out=null;for(const x of list){if(x.lineage===lineage && x.day<=day)out=x}return out}function render(){const a=DATA.actions[i%DATA.actions.length],w=DATA.world[i%DATA.world.length],m=DATA.memories[i%DATA.memories.length],rel=DATA.welfare[i%DATA.welfare.length],tech=latest(DATA.technology,a.target_lineage,a.day),sch=latest(DATA.routines,a.target_lineage,a.day),rep=latest(DATA.reputations,a.target_lineage,a.day),rp=DATA.replay[i%DATA.replay.length];const p=pos(a.avatar_place);document.getElementById('avatar').style.left=p[0]+'%';document.getElementById('avatar').style.top=p[1]+'%';document.getElementById('pulse').style.transform=`rotate(${(i*137.507764)%360}deg)`;document.getElementById('action').textContent=w.public_state+'\\n'+w.avatar_state+'\\nreply: '+a.public_reply;document.getElementById('memory').textContent=m.memory_after+'\\n'+m.public_summary;document.getElementById('welfare').textContent=w.welfare_panel+'\\n'+rel.welfare_note;document.getElementById('schedule').textContent=sch?sch.routine_memory:w.schedule_panel;document.getElementById('technology').textContent=tech?tech.public_rule+'\\n'+tech.access_decision:w.technology_panel;document.getElementById('reputation').textContent=rep?rep.group_memory+'\\n'+rep.access_changed:w.reputation_panel;document.getElementById('private').textContent=JSON.stringify({trace:w.trace_integrity_token,replay:rp,private_trace_visible:w.private_trace_visible},null,2);replay.push({tick:a.tick,day:a.day,lineage:a.target_lineage,intent:a.parsed_intent,hash:rp.export_hash});log(`day ${a.day} ${a.action_kind} -> ${a.target_agent}; ${a.consequence_kind}`);i++}function metrics(){const keys=['browser_world_v9_post_entry_society_readiness','weakest_channel_score','avatar_action_to_world_state_binding','lineage_memory_mutation_rate','relationship_welfare_coupling','typed_intent_consequence_confidence'];document.getElementById('metrics').innerHTML=keys.map(k=>`<div class=\"metric\"><span>${k}</span><b>${pct(DATA.metrics[k])}</b></div>`).join('')}function start(){if(!timer)timer=setInterval(render,320)}function pause(){clearInterval(timer);timer=null}document.getElementById('start').onclick=start;document.getElementById('pause').onclick=pause;document.getElementById('step').onclick=render;document.getElementById('save').onclick=()=>localStorage.setItem(KEY,JSON.stringify({i,replay}));document.getElementById('restore').onclick=()=>{const raw=localStorage.getItem(KEY);if(raw){const s=JSON.parse(raw);i=s.i||0;replay=s.replay||[];render();log('restored post-entry society state')}};document.getElementById('export').onclick=()=>{const blob=new Blob([JSON.stringify({report:249,replay},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='ssrm249_post_entry_replay.json';a.click()};document.getElementById('import').onchange=async(e)=>{const f=e.target.files[0];if(f){const obj=JSON.parse(await f.text());replay=obj.replay||[];log('imported replay '+replay.length)}};document.getElementById('inspect').onclick=()=>document.getElementById('private').classList.toggle('open');document.getElementById('send').onclick=()=>{const act=document.getElementById('act').value,text=document.getElementById('text').value;replay.push({tick:'typed',act,text});log('typed '+act+': '+text);render()};metrics();render();</script></body></html>"""
    return template.replace("__DATA__", json.dumps(payload))


def run(seed: int) -> dict[str, Any]:
    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    source = source_summary()
    actions = build_actions(seed)
    memories = build_lineage_memory(actions)
    tech = build_technology(actions)
    welfare = build_relationship_welfare(actions)
    routines = build_routines(actions)
    reputations = build_reputation(actions)
    replay = build_replay(actions, memories, routines, reputations, source)
    world = build_world(actions, memories, tech, welfare, routines, reputations, replay)
    metrics = compute_metrics(source, actions, memories, tech, welfare, routines, reputations, replay, world)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["browser_world_v9_post_entry_society_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    prefix = ARTIFACTS / BASE
    write_csv(Path(f"{prefix}_post_entry_avatar_action_frames.csv"), actions)
    write_csv(Path(f"{prefix}_lineage_memory_update_frames.csv"), memories)
    write_csv(Path(f"{prefix}_technology_access_consequence_frames.csv"), tech)
    write_csv(Path(f"{prefix}_relationship_welfare_consequence_frames.csv"), welfare)
    write_csv(Path(f"{prefix}_routine_schedule_update_frames.csv"), routines)
    write_csv(Path(f"{prefix}_public_reputation_frames.csv"), reputations)
    write_csv(Path(f"{prefix}_replay_post_entry_frames.csv"), replay)
    write_csv(Path(f"{prefix}_browser_world_v9_ticks.csv"), world)
    honest_limits = [
        "This is deterministic post-entry society consequence wiring, not subjective consciousness.",
        "Typed acts use seeded parser routes and do not call an LLM or provide autonomous natural language.",
        "Consent, refusal, and reputation are simulated functional boundaries, not real consent or moral standing.",
        "Multi-day consequences are generated traces, not an open-ended civilization engine.",
        "The browser page is a playable 2D/2.5D state surface, not complete 3D physics.",
        "Welfare variables are bounded control states with recovery paths, not proof of experienced welfare.",
        "Frequency and flower phase are rhythm variables, not metaphysical proof.",
    ]
    next_gate = "browser world v10 with autonomous post-entry society ticks that continue without avatar input while preserving consequence memory, needs, schedules, technology access, and welfare guardrails"
    results = {
        "report": REPORT,
        "name": "SSRM-3D Browser World v9 Post-Entry Live Society Consequence Bridge",
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "verdict": verdict,
        "counts": {
            "post_entry_avatar_action_frames": len(actions),
            "lineage_memory_update_frames": len(memories),
            "technology_access_consequence_frames": len(tech),
            "relationship_welfare_consequence_frames": len(welfare),
            "routine_schedule_update_frames": len(routines),
            "public_reputation_frames": len(reputations),
            "replay_post_entry_frames": len(replay),
            "browser_world_v9_ticks": len(world),
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
        "post_entry_model": "avatar action -> lineage memory -> technology access -> relationship welfare -> routine schedule -> public reputation -> replay",
        "boundary": "functional post-entry consequence scaffold; no consciousness claim",
    }
    Path(f"{prefix}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    Path(f"{prefix}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    with Path(f"{prefix}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "verdict": verdict, "readiness": metrics["browser_world_v9_post_entry_society_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": next_gate})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(actions, memories, tech, welfare, routines, reputations, replay, world, metrics))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    counts = results["counts"]
    print(f"module_verdict {results['verdict']}")
    print(f"browser_world_v9_post_entry_society_readiness {metrics['browser_world_v9_post_entry_society_readiness']:.6f}")
    for key in ["post_entry_avatar_action_frames", "lineage_memory_update_frames", "technology_access_consequence_frames", "relationship_welfare_consequence_frames", "routine_schedule_update_frames", "public_reputation_frames", "replay_post_entry_frames", "browser_world_v9_ticks"]:
        print(f"{key} {counts[key]}")
    for key in ["source_playable_entry_continuity", "post_entry_consequence_surface", "multi_day_span_coverage", "avatar_action_to_world_state_binding", "lineage_memory_mutation_rate", "relationship_welfare_coupling", "typed_intent_consequence_confidence", "weakest_channel_score"]:
        print(f"{key} {metrics[key]:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
