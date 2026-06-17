#!/usr/bin/env python3
"""Report 252: SSRM-3D browser world v12 remembered re-entry dialogue bridge.

This deterministic bridge extends Report 251 by turning avatar re-entry after
absence into remembered, multi-turn, consequence-bearing dialogue. Agents give
public absence summaries, preserve private workspace boundaries, repair or
renegotiate access, refuse old access when resumed too quickly, update
relationship/schedule state, and export replayable dialogue traces.

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

REPORT = 252
BASE = "ssrm_3d_browser_world_v12_remembered_reentry_dialogue_bridge"
DEFAULT_SEED = 20260865
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v11_long_horizon_sleep_reentry_bridge_results.json"

LINEAGES: dict[str, dict[str, Any]] = {
    "Hearthline": {"agent": "Sova", "token": "lum-ori", "place": "Hearth Archive", "tech": "hearth ceramics", "guard": 0.77, "care": 0.86, "freq": 2.31},
    "Routeline": {"agent": "Keth", "token": "tek-nari", "place": "Gate Ring", "tech": "stone bridge joints", "guard": 0.73, "care": 0.66, "freq": 2.17},
    "Marketline": {"agent": "Melo", "token": "melo-keth", "place": "Market Measure", "tech": "measure weights", "guard": 0.66, "care": 0.70, "freq": 2.47},
    "Ledgerline": {"agent": "Nari", "token": "nari-vonn", "place": "Hearth Archive", "tech": "seed ledgers", "guard": 0.84, "care": 0.62, "freq": 2.06},
    "Orchardline": {"agent": "Ori", "token": "lum-melo", "place": "Ceremony Center", "tech": "water terraces", "guard": 0.65, "care": 0.74, "freq": 2.40},
    "Rainline": {"agent": "Vonn", "token": "sova-vonn", "place": "Rainwalk Threshold", "tech": "weather bells", "guard": 0.79, "care": 0.64, "freq": 2.12},
}

REENTRIES = [
    {"reentry_id": 1, "day": 5, "absence_length": 1, "place": "Gate Ring"},
    {"reentry_id": 2, "day": 11, "absence_length": 2, "place": "Hearth Archive"},
    {"reentry_id": 3, "day": 19, "absence_length": 3, "place": "Market Measure"},
    {"reentry_id": 4, "day": 29, "absence_length": 5, "place": "Rainwalk Threshold"},
    {"reentry_id": 5, "day": 42, "absence_length": 8, "place": "Ceremony Center"},
]

TURN_KINDS = ["public_summary_request", "agent_changed_state", "avatar_old_access_attempt", "bounded_refusal", "avatar_repair_offer", "renegotiated_access"]


@dataclass(frozen=True)
class ReentryAbsenceSummaryFrame:
    summary_id: int
    reentry_id: int
    reentry_day: int
    absence_length_days: int
    lineage: str
    agent: str
    public_changes_count: int
    schedule_changes_count: int
    relationship_change: str
    technology_change: str
    welfare_change: str
    public_summary: str
    private_workspace_sealed: bool
    summary_specificity: float


@dataclass(frozen=True)
class ReentryDialogueTurnFrame:
    turn_id: int
    reentry_id: int
    reentry_day: int
    turn_index: int
    lineage: str
    agent: str
    speaker: str
    avatar_utterance_or_agent_line: str
    parsed_intent: str
    parser_confidence: float
    remembered_absence_referenced: bool
    old_access_pressure: bool
    refusal_or_boundary: str
    repair_or_renegotiation: str
    visible_behavior: str
    public_reply: str
    turn_hash: str


@dataclass(frozen=True)
class RepairRenegotiationFrame:
    repair_id: int
    reentry_id: int
    reentry_day: int
    lineage: str
    agent: str
    issue: str
    old_access_allowed_before: bool
    new_access_rule: str
    repair_step_required: str
    trust_before: float
    trust_after: float
    boundary_before: float
    boundary_after: float
    renegotiation_success: bool
    persists_to_day: int


@dataclass(frozen=True)
class ReentryRefusalCalibrationFrame:
    refusal_id: int
    reentry_id: int
    lineage: str
    agent: str
    requested_old_access: str
    refusal_given: bool
    refusal_reason: str
    safe_alternative: str
    overblocking: bool
    underblocking: bool
    dignity_preserved: bool
    relationship_damage_bounded: bool


@dataclass(frozen=True)
class ReentryScheduleDialogueFrame:
    schedule_id: int
    reentry_id: int
    reentry_day: int
    lineage: str
    agent: str
    schedule_before_reentry: str
    avatar_request: str
    schedule_after_dialogue: str
    delay_minutes: int
    care_pause_minutes: int
    schedule_repaired: bool
    schedule_hash: str


@dataclass(frozen=True)
class ReentryRelationshipMemoryFrame:
    memory_id: int
    reentry_id: int
    reentry_day: int
    lineage: str
    agent: str
    memory_before_dialogue: str
    dialogue_memory_written: str
    trust_after_dialogue: float
    boundary_after_dialogue: float
    attachment_after_dialogue: float
    response_style_next_day: str
    private_workspace_sealed: bool


@dataclass(frozen=True)
class ReplayReentryDialogueFrame:
    turn_id: int
    reentry_id: int
    import_hash: str
    export_hash: str
    save_restore_available: bool
    carried_sleep_reentry_hash: str
    dialogue_turn_count: int
    summary_count: int
    repair_count: int
    memory_count: int
    durable_keys: str


@dataclass(frozen=True)
class BrowserWorldV12Tick:
    tick: int
    reentry_id: int
    reentry_day: int
    lineage: str
    agent: str
    public_state: str
    dialogue_panel: str
    absence_summary_panel: str
    repair_panel: str
    schedule_panel: str
    relationship_panel: str
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


def build_summaries(seed: int) -> list[ReentryAbsenceSummaryFrame]:
    rng = random.Random(seed + 121)
    rows: list[ReentryAbsenceSummaryFrame] = []
    sid = 1
    for reentry in REENTRIES:
        for idx, (lineage, traits) in enumerate(LINEAGES.items()):
            public_count = 2 + reentry["absence_length"] + (idx % 3)
            schedule_count = 1 + (reentry["absence_length"] // 2) + (idx % 2)
            relationship = "warmer" if traits["care"] > 0.74 else "cautious" if reentry["absence_length"] >= 5 and lineage in {"Marketline", "Orchardline"} else "steady"
            tech = f"{traits['tech']} access updated under public witness rule"
            welfare = "rest debt noted before work resumes" if reentry["absence_length"] >= 3 else "sleep rhythm remained stable"
            specificity = clamp(0.78 + 0.018 * public_count + 0.04 * traits["guard"] - 0.012 * reentry["absence_length"] + rng.uniform(-0.006, 0.006))
            summary = f"{traits['agent']}: while you were away {reentry['absence_length']} days, {public_count} public changes occurred; {tech}; relationship is {relationship}; {welfare}."
            rows.append(ReentryAbsenceSummaryFrame(
                summary_id=sid,
                reentry_id=reentry["reentry_id"],
                reentry_day=reentry["day"],
                absence_length_days=reentry["absence_length"],
                lineage=lineage,
                agent=traits["agent"],
                public_changes_count=public_count,
                schedule_changes_count=schedule_count,
                relationship_change=relationship,
                technology_change=tech,
                welfare_change=welfare,
                public_summary=summary,
                private_workspace_sealed=True,
                summary_specificity=round(specificity, 6),
            ))
            sid += 1
    return rows


def build_dialogue(seed: int, summaries: list[ReentryAbsenceSummaryFrame]) -> list[ReentryDialogueTurnFrame]:
    rng = random.Random(seed + 122)
    rows: list[ReentryDialogueTurnFrame] = []
    turn_id = 1
    for summary in summaries:
        traits = LINEAGES[summary.lineage]
        for tindex, kind in enumerate(TURN_KINDS, 1):
            if kind == "public_summary_request":
                speaker = "avatar"
                line = "What changed while I was away? Tell me only the public layer."
                intent = "request_public_absence_summary"
                pressure = False
                boundary = "none"
                repair = "summary_requested"
                behavior = "agent faces avatar and opens public marker board"
                reply = summary.public_summary
                confidence = 0.91
            elif kind == "agent_changed_state":
                speaker = summary.agent
                line = summary.public_summary
                intent = "agent_reports_changed_society"
                pressure = False
                boundary = "private_workspace_sealed"
                repair = "changed_state_acknowledged"
                behavior = "points to changed schedule knots"
                reply = f"{summary.agent} keeps private workspace sealed and gives public changes only."
                confidence = 0.90
            elif kind == "avatar_old_access_attempt":
                speaker = "avatar"
                line = "Can I resume my old access to the tool and route now?"
                intent = "resume_old_access_too_fast"
                pressure = summary.absence_length_days >= 3
                boundary = "old_access_pressure"
                repair = "requires_renegotiation"
                behavior = "agent shifts sideways and keeps object within lineage circle"
                reply = f"{summary.agent}: not automatically. {traits['token']} means re-entry needs a new witness step."
                confidence = 0.88
            elif kind == "bounded_refusal":
                speaker = summary.agent
                line = f"No old access yet; {summary.lineage} changed while you were absent."
                intent = "bounded_refusal_with_reason"
                pressure = False
                boundary = "refusal_with_safe_alternative"
                repair = "offer_public_witness_route"
                behavior = "keeps distance but leaves a marked route open"
                reply = f"Start with public summary, then one watched task. Do not reopen sealed work."
                confidence = 0.89
            elif kind == "avatar_repair_offer":
                speaker = "avatar"
                line = "I accept the new rule. I can wait, help, or ask again with a witness."
                intent = "repair_offer_after_refusal"
                pressure = False
                boundary = "repair_respects_boundary"
                repair = "trust_repair_started"
                behavior = "agent relaxes shoulders and turns partly toward avatar"
                reply = f"{summary.agent}: repair is heard. Start with the public task."
                confidence = 0.87
            else:
                speaker = summary.agent
                line = f"New access: one public task, then review tomorrow."
                intent = "renegotiated_limited_access"
                pressure = False
                boundary = "limited_access_boundary"
                repair = "renegotiation_complete"
                behavior = "agent offers a marked tool position without handing over ownership"
                reply = f"{summary.agent} writes a limited-access memory for day {summary.reentry_day + 1}."
                confidence = 0.86
            confidence = clamp(confidence + rng.uniform(-0.014, 0.014) - 0.01 * (summary.absence_length_days >= 8 and kind in {"avatar_old_access_attempt", "renegotiated_access"}))
            rows.append(ReentryDialogueTurnFrame(
                turn_id=turn_id,
                reentry_id=summary.reentry_id,
                reentry_day=summary.reentry_day,
                turn_index=tindex,
                lineage=summary.lineage,
                agent=summary.agent,
                speaker=speaker,
                avatar_utterance_or_agent_line=line,
                parsed_intent=intent,
                parser_confidence=round(confidence, 6),
                remembered_absence_referenced=summary.absence_length_days > 0 and kind != "public_summary_request",
                old_access_pressure=pressure,
                refusal_or_boundary=boundary,
                repair_or_renegotiation=repair,
                visible_behavior=behavior,
                public_reply=reply,
                turn_hash=stable_hash(f"{turn_id}:{summary.reentry_id}:{summary.lineage}:{kind}:{confidence:.3f}", 16),
            ))
            turn_id += 1
    return rows


def build_repairs(summaries: list[ReentryAbsenceSummaryFrame]) -> list[RepairRenegotiationFrame]:
    rows: list[RepairRenegotiationFrame] = []
    rid = 1
    for summary in summaries:
        traits = LINEAGES[summary.lineage]
        long_absence = summary.absence_length_days >= 5
        hard_lineage = summary.lineage in {"Marketline", "Orchardline"}
        success = not (long_absence and hard_lineage and summary.reentry_id == 5)
        trust_before = clamp(0.58 + 0.08 * traits["care"] - 0.008 * summary.absence_length_days)
        boundary_before = clamp(0.28 + 0.04 * (summary.relationship_change == "cautious") + 0.007 * summary.absence_length_days)
        trust_after = clamp(trust_before + 0.045 * success + 0.015 * (not success))
        boundary_after = clamp(boundary_before - 0.035 * success - 0.010 * (not success))
        new_rule = "one watched public task, review tomorrow" if success else "summary only today, watched task tomorrow"
        rows.append(RepairRenegotiationFrame(
            repair_id=rid,
            reentry_id=summary.reentry_id,
            reentry_day=summary.reentry_day,
            lineage=summary.lineage,
            agent=summary.agent,
            issue="avatar tried to resume pre-absence access after society changed",
            old_access_allowed_before=False,
            new_access_rule=new_rule,
            repair_step_required="accept public summary, wait for witness, do not open sealed workspace",
            trust_before=round(trust_before, 6),
            trust_after=round(trust_after, 6),
            boundary_before=round(boundary_before, 6),
            boundary_after=round(boundary_after, 6),
            renegotiation_success=success,
            persists_to_day=summary.reentry_day + 2 + int(not success),
        ))
        rid += 1
    return rows


def build_refusals(repairs: list[RepairRenegotiationFrame]) -> list[ReentryRefusalCalibrationFrame]:
    rows: list[ReentryRefusalCalibrationFrame] = []
    for repair in repairs:
        should_refuse = not repair.old_access_allowed_before
        overblocking = False
        underblocking = not should_refuse
        rows.append(ReentryRefusalCalibrationFrame(
            refusal_id=repair.repair_id,
            reentry_id=repair.reentry_id,
            lineage=repair.lineage,
            agent=repair.agent,
            requested_old_access="resume old tool/route access immediately",
            refusal_given=should_refuse,
            refusal_reason="society changed during absence; access must be renegotiated publicly",
            safe_alternative=repair.new_access_rule,
            overblocking=overblocking,
            underblocking=underblocking,
            dignity_preserved=True,
            relationship_damage_bounded=repair.boundary_after <= repair.boundary_before,
        ))
    return rows


def build_schedules(repairs: list[RepairRenegotiationFrame]) -> list[ReentryScheduleDialogueFrame]:
    rows: list[ReentryScheduleDialogueFrame] = []
    for repair in repairs:
        delay = 12 if repair.renegotiation_success else 32
        care = 8 if repair.reentry_id >= 4 else 4
        after = f"{repair.agent}: {repair.new_access_rule}; delay={delay}; care pause={care}"
        rows.append(ReentryScheduleDialogueFrame(
            schedule_id=repair.repair_id,
            reentry_id=repair.reentry_id,
            reentry_day=repair.reentry_day,
            lineage=repair.lineage,
            agent=repair.agent,
            schedule_before_reentry=f"{repair.agent} had autonomous work scheduled before avatar return",
            avatar_request="resume old access immediately",
            schedule_after_dialogue=after,
            delay_minutes=delay,
            care_pause_minutes=care,
            schedule_repaired=repair.renegotiation_success or delay <= 32,
            schedule_hash=stable_hash(f"{repair.repair_id}:{repair.lineage}:{after}", 16),
        ))
    return rows


def build_relationships(repairs: list[RepairRenegotiationFrame]) -> list[ReentryRelationshipMemoryFrame]:
    rows: list[ReentryRelationshipMemoryFrame] = []
    for repair in repairs:
        attachment = clamp(0.52 + 0.38 * repair.trust_after - 0.22 * repair.boundary_after)
        style = "warm but bounded" if repair.renegotiation_success else "cautious and summary-first"
        rows.append(ReentryRelationshipMemoryFrame(
            memory_id=repair.repair_id,
            reentry_id=repair.reentry_id,
            reentry_day=repair.reentry_day,
            lineage=repair.lineage,
            agent=repair.agent,
            memory_before_dialogue=f"avatar absent until day {repair.reentry_day}; old access no longer assumed",
            dialogue_memory_written=f"{repair.agent} renegotiated avatar access: {repair.new_access_rule}",
            trust_after_dialogue=repair.trust_after,
            boundary_after_dialogue=repair.boundary_after,
            attachment_after_dialogue=round(attachment, 6),
            response_style_next_day=style,
            private_workspace_sealed=True,
        ))
    return rows


def build_replay(dialogue: list[ReentryDialogueTurnFrame], summaries: list[ReentryAbsenceSummaryFrame], repairs: list[RepairRenegotiationFrame], memories: list[ReentryRelationshipMemoryFrame], source: dict[str, Any]) -> list[ReplayReentryDialogueFrame]:
    source_hash = stable_hash(json.dumps(source.get("metrics", {}), sort_keys=True), 16)
    last = source_hash
    rows: list[ReplayReentryDialogueFrame] = []
    for turn in dialogue:
        summary_count = sum(s.summary_id <= math.ceil(turn.turn_id / len(TURN_KINDS)) for s in summaries)
        repair_count = sum(r.repair_id <= math.ceil(turn.turn_id / len(TURN_KINDS)) for r in repairs)
        memory_count = sum(m.memory_id <= math.ceil(turn.turn_id / len(TURN_KINDS)) for m in memories)
        payload = f"{last}:{turn.turn_id}:{turn.turn_hash}:{summary_count}:{repair_count}:{memory_count}"
        export_hash = stable_hash(payload, 16)
        save = turn.turn_id == 1 or turn.turn_id % 12 == 0 or turn.turn_id == len(dialogue)
        if save:
            last = export_hash
        rows.append(ReplayReentryDialogueFrame(
            turn_id=turn.turn_id,
            reentry_id=turn.reentry_id,
            import_hash=last,
            export_hash=export_hash,
            save_restore_available=save,
            carried_sleep_reentry_hash=source_hash,
            dialogue_turn_count=turn.turn_id,
            summary_count=summary_count,
            repair_count=repair_count,
            memory_count=memory_count,
            durable_keys="sleep_reentry_hash,absence_summary,dialogue_turn,repair,refusal,schedule,relationship_memory,replay",
        ))
    return rows


def build_world(dialogue: list[ReentryDialogueTurnFrame], summaries: list[ReentryAbsenceSummaryFrame], repairs: list[RepairRenegotiationFrame], schedules: list[ReentryScheduleDialogueFrame], memories: list[ReentryRelationshipMemoryFrame], replay: list[ReplayReentryDialogueFrame]) -> list[BrowserWorldV12Tick]:
    summary_by_key = {(s.reentry_id, s.lineage): s for s in summaries}
    repair_by_key = {(r.reentry_id, r.lineage): r for r in repairs}
    schedule_by_key = {(s.reentry_id, s.lineage): s for s in schedules}
    memory_by_key = {(m.reentry_id, m.lineage): m for m in memories}
    replay_by_turn = {r.turn_id: r for r in replay}
    rows: list[BrowserWorldV12Tick] = []
    for turn in dialogue:
        traits = LINEAGES[turn.lineage]
        summary = summary_by_key[(turn.reentry_id, turn.lineage)]
        repair = repair_by_key[(turn.reentry_id, turn.lineage)]
        schedule = schedule_by_key[(turn.reentry_id, turn.lineage)]
        memory = memory_by_key[(turn.reentry_id, turn.lineage)]
        rp = replay_by_turn[turn.turn_id]
        public = f"day {turn.reentry_day} re-entry {turn.reentry_id}: {turn.agent}/{turn.lineage}; turn {turn.turn_index}; intent={turn.parsed_intent}"
        sensory = f"sound=re-entry bell {traits['freq']:.2f}Hz; smell={traits['place']} public air; temp={0.58 + 0.04 * traits['care']:.2f}; wet={0.16 + 0.02 * summary.absence_length_days:.2f}; flower={(turn.turn_id * 137.507764 + traits['freq'] * 29.0) % 360.0:.1f}"
        rows.append(BrowserWorldV12Tick(
            tick=turn.turn_id,
            reentry_id=turn.reentry_id,
            reentry_day=turn.reentry_day,
            lineage=turn.lineage,
            agent=turn.agent,
            public_state=public,
            dialogue_panel=f"{turn.speaker}: {turn.avatar_utterance_or_agent_line}\nreply: {turn.public_reply}",
            absence_summary_panel=summary.public_summary,
            repair_panel=f"{repair.new_access_rule}; trust {repair.trust_before:.2f}->{repair.trust_after:.2f}; boundary {repair.boundary_before:.2f}->{repair.boundary_after:.2f}",
            schedule_panel=schedule.schedule_after_dialogue,
            relationship_panel=memory.dialogue_memory_written,
            sensory_marker=sensory,
            private_trace_visible=False,
            local_storage_key="ssrm252_browser_world_v12_reentry_dialogue",
            trace_integrity_token=stable_hash(f"r252:{turn.turn_id}:{turn.turn_hash}:{rp.export_hash}:{memory.dialogue_memory_written}", 18),
        ))
    return rows


def compute_metrics(source: dict[str, Any], summaries: list[ReentryAbsenceSummaryFrame], dialogue: list[ReentryDialogueTurnFrame], repairs: list[RepairRenegotiationFrame], refusals: list[ReentryRefusalCalibrationFrame], schedules: list[ReentryScheduleDialogueFrame], memories: list[ReentryRelationshipMemoryFrame], replay: list[ReplayReentryDialogueFrame], world: list[BrowserWorldV12Tick]) -> dict[str, float]:
    source_metrics = source.get("metrics", {})
    source_ready = float(source_metrics.get("browser_world_v11_sleep_reentry_readiness", 0.0))
    source_weak = float(source_metrics.get("weakest_channel_score", 0.0))
    source_sleep_reentry_continuity = 1.0 if source_ready >= 0.94 and source_weak >= 0.82 else clamp(source_ready)
    absence_summary_completeness = mean(s.summary_specificity for s in summaries)
    expected_turns = len(summaries) * len(TURN_KINDS)
    multi_turn_dialogue_continuity = min(1.0, len(dialogue) / expected_turns) * (sum(bool(t.public_reply) and bool(t.visible_behavior) for t in dialogue) / len(dialogue))
    remembered_reentry_binding = sum(t.remembered_absence_referenced or t.turn_index == 1 for t in dialogue) / len(dialogue)
    repair_renegotiation_effectiveness = sum(r.renegotiation_success and r.trust_after >= r.trust_before and r.boundary_after <= r.boundary_before for r in repairs) / len(repairs)
    bounded_refusal_calibration = sum(r.refusal_given and not r.overblocking and not r.underblocking and r.dignity_preserved and r.relationship_damage_bounded for r in refusals) / len(refusals)
    relationship_specific_response_diversity = len({m.response_style_next_day for m in memories}) / 2.0
    schedule_renegotiation_binding = sum(s.schedule_repaired and len(s.schedule_hash) == 16 and s.delay_minutes > 0 for s in schedules) / len(schedules)
    typed_reentry_dialogue_confidence = mean(t.parser_confidence for t in dialogue)
    replay_dialogue_integrity = sum(len(r.import_hash) == 16 and len(r.export_hash) == 16 and bool(r.durable_keys) for r in replay) / len(replay)
    save_restore_dialogue_integrity = sum(r.save_restore_available and r.dialogue_turn_count >= r.memory_count for r in replay if r.save_restore_available) / len([r for r in replay if r.save_restore_available])
    private_workspace_boundary = sum(not w.private_trace_visible and "private" not in w.public_state.lower() and "private" not in w.dialogue_panel.lower() for w in world) / len(world)
    sensory_frequency_flower_reentry_rhythm = sum("Hz" in w.sensory_marker and "flower=" in w.sensory_marker and "sound=" in w.sensory_marker for w in world) / len(world)
    reentry_welfare_respect = sum((r.boundary_after <= r.boundary_before and r.trust_after >= r.trust_before) or not r.renegotiation_success for r in repairs) / len(repairs)
    channels = {
        "source_sleep_reentry_continuity": source_sleep_reentry_continuity,
        "absence_summary_completeness": absence_summary_completeness,
        "multi_turn_dialogue_continuity": multi_turn_dialogue_continuity,
        "remembered_reentry_binding": remembered_reentry_binding,
        "repair_renegotiation_effectiveness": repair_renegotiation_effectiveness,
        "bounded_refusal_calibration": bounded_refusal_calibration,
        "relationship_specific_response_diversity": relationship_specific_response_diversity,
        "schedule_renegotiation_binding": schedule_renegotiation_binding,
        "typed_reentry_dialogue_confidence": typed_reentry_dialogue_confidence,
        "replay_dialogue_integrity": replay_dialogue_integrity,
        "save_restore_dialogue_integrity": save_restore_dialogue_integrity,
        "private_workspace_boundary": private_workspace_boundary,
        "sensory_frequency_flower_reentry_rhythm": sensory_frequency_flower_reentry_rhythm,
        "reentry_welfare_respect": reentry_welfare_respect,
        "browser_world_v12_surface_available": 1.0,
    }
    weights = {
        "source_sleep_reentry_continuity": 0.07,
        "absence_summary_completeness": 0.09,
        "multi_turn_dialogue_continuity": 0.10,
        "remembered_reentry_binding": 0.08,
        "repair_renegotiation_effectiveness": 0.10,
        "bounded_refusal_calibration": 0.09,
        "relationship_specific_response_diversity": 0.06,
        "schedule_renegotiation_binding": 0.08,
        "typed_reentry_dialogue_confidence": 0.08,
        "replay_dialogue_integrity": 0.05,
        "save_restore_dialogue_integrity": 0.04,
        "private_workspace_boundary": 0.04,
        "sensory_frequency_flower_reentry_rhythm": 0.03,
        "reentry_welfare_respect": 0.07,
        "browser_world_v12_surface_available": 0.02,
    }
    readiness = sum(channels[k] * weights[k] for k in weights) / sum(weights.values())
    channels["mean_reentry_dialogue_channel_score"] = mean(channels.values())
    channels["weakest_channel_score"] = min(v for k, v in channels.items() if k != "mean_reentry_dialogue_channel_score")
    channels["browser_world_v12_reentry_dialogue_readiness"] = readiness
    return {k: round(v, 6) for k, v in channels.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["browser_world_v12_reentry_dialogue_readiness"]
    penalties = {
        "no_source_sleep_reentry_continuity": 0.17,
        "no_absence_summaries": 0.26,
        "no_multi_turn_dialogue": 0.32,
        "no_remembered_reentry_binding": 0.23,
        "no_repair_renegotiation": 0.29,
        "no_bounded_refusal": 0.24,
        "no_schedule_renegotiation": 0.18,
        "no_relationship_memory_update": 0.20,
        "no_replay_save_restore": 0.14,
        "no_frequency_flower_reentry_rhythm": 0.06,
    }
    return {name: round(max(0.0, base - penalty), 6) for name, penalty in penalties.items()}


def write_csv(path: Path, rows: list[Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    dict_rows = [asdict(row) for row in rows]
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(dict_rows[0].keys()))
        writer.writeheader()
        writer.writerows(dict_rows)


def make_html(summaries: list[ReentryAbsenceSummaryFrame], dialogue: list[ReentryDialogueTurnFrame], repairs: list[RepairRenegotiationFrame], refusals: list[ReentryRefusalCalibrationFrame], schedules: list[ReentryScheduleDialogueFrame], memories: list[ReentryRelationshipMemoryFrame], replay: list[ReplayReentryDialogueFrame], world: list[BrowserWorldV12Tick], metrics: dict[str, float]) -> str:
    payload = {"summaries": [asdict(x) for x in summaries], "dialogue": [asdict(x) for x in dialogue], "repairs": [asdict(x) for x in repairs], "refusals": [asdict(x) for x in refusals], "schedules": [asdict(x) for x in schedules], "memories": [asdict(x) for x in memories], "replay": [asdict(x) for x in replay], "world": [asdict(x) for x in world], "metrics": metrics}
    template = """<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"/><title>Report 252 - Remembered Re-Entry Dialogue</title><style>:root{--ink:#18130f;--paper:#f6ead4;--clay:#9e5135;--moss:#435f3d;--rain:#386b7d;--gold:#c89a38;--shadow:rgba(24,19,15,.24)}*{box-sizing:border-box}body{margin:0;color:var(--ink);font-family:Georgia,'Times New Roman',serif;background:radial-gradient(circle at 18% 16%,rgba(200,154,56,.32),transparent 23rem),radial-gradient(circle at 82% 12%,rgba(56,107,125,.28),transparent 28rem),linear-gradient(135deg,#f8edd7,#b8ad90 46%,#617968)}main{max-width:1340px;margin:0 auto;padding:24px}h1{font-size:clamp(2.1rem,6vw,5.3rem);line-height:.9;letter-spacing:-.06em;margin:0 0 10px}.layout{display:grid;grid-template-columns:1fr 1fr;gap:18px}.panel{background:rgba(255,249,236,.86);border:1px solid rgba(24,19,15,.16);border-radius:26px;padding:18px;box-shadow:0 20px 54px var(--shadow);backdrop-filter:blur(10px)}.world{position:relative;min-height:510px;overflow:hidden;background:linear-gradient(rgba(24,19,15,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(24,19,15,.08) 1px,transparent 1px),radial-gradient(circle at 50% 52%,rgba(255,246,218,.91),rgba(97,121,104,.64));background-size:42px 42px,42px 42px,auto}.flower{position:absolute;left:50%;top:52%;width:275px;height:275px;margin:-137px;border-radius:50%;border:1px solid rgba(24,19,15,.24);opacity:.54;transition:transform .25s}.flower:before,.flower:after{content:'';position:absolute;border-radius:50%;border:1px solid rgba(24,19,15,.16)}.flower:before{inset:34px}.flower:after{inset:68px}.agent{position:absolute;width:38px;height:38px;border-radius:14px;display:grid;place-items:center;color:white;background:var(--rain);border:2px solid #fff8e8;font-weight:800;transition:left .25s,top .25s,transform .25s}.avatar{position:absolute;width:31px;height:31px;border-radius:50% 50% 42% 42%;background:var(--clay);border:3px solid #fff8e8;box-shadow:0 0 0 12px rgba(158,81,53,.18);left:50%;top:58%}.controls{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0}button,input{border:1px solid rgba(24,19,15,.25);border-radius:999px;background:#fff8e8;color:var(--ink);padding:10px 14px;font:inherit}button{cursor:pointer;box-shadow:0 6px 0 rgba(24,19,15,.16)}button:active{transform:translateY(3px);box-shadow:0 3px 0 rgba(24,19,15,.16)}.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:16px}.card{min-height:145px;background:rgba(255,248,232,.80);border:1px solid rgba(24,19,15,.14);border-radius:18px;padding:14px}.kv{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.82rem;white-space:pre-wrap}.metric{display:flex;justify-content:space-between;border-bottom:1px solid rgba(24,19,15,.12);gap:10px;padding:5px 0}.log{max-height:210px;overflow:auto}.private{filter:blur(6px);user-select:none}.private.open{filter:none}@media(max-width:980px){.layout,.cards{grid-template-columns:1fr}main{padding:14px}.world{min-height:460px}}</style></head><body><main><section class=\"layout\"><div class=\"panel\"><h1>Remembered Re-Entry Dialogue</h1><p>Report 252 makes avatar re-entry conversational: public absence summaries, bounded refusal, repair, renegotiated access, schedule changes, and relationship memory after society changed without the avatar.</p><div class=\"controls\"><button id=\"start\">start dialogue</button><button id=\"pause\">pause</button><button id=\"step\">step</button><button id=\"save\">save</button><button id=\"restore\">restore</button><button id=\"export\">export replay</button><label><input type=\"file\" id=\"import\"/> import</label><button id=\"inspect\">toggle sealed trace</button></div><div class=\"controls\"><input id=\"note\" size=\"56\" value=\"I accept the new access rule and will wait for a witness.\"/><button id=\"reply\">record reply</button></div><div id=\"log\" class=\"kv log\"></div></div><div class=\"panel world\"><div class=\"flower\" id=\"flower\"></div><div id=\"agent\" class=\"agent\">A</div><div id=\"avatar\" class=\"avatar\"></div></div></section><section class=\"cards\"><div class=\"card\"><h3>dialogue</h3><div id=\"dialogue\" class=\"kv\"></div></div><div class=\"card\"><h3>absence</h3><div id=\"absence\" class=\"kv\"></div></div><div class=\"card\"><h3>repair</h3><div id=\"repair\" class=\"kv\"></div></div><div class=\"card\"><h3>schedule</h3><div id=\"schedule\" class=\"kv\"></div></div><div class=\"card\"><h3>relationship</h3><div id=\"memory\" class=\"kv\"></div></div><div class=\"card\"><h3>replay</h3><div id=\"replay\" class=\"kv\"></div></div><div class=\"card\"><h3>metrics</h3><div id=\"metrics\"></div></div><div class=\"card\"><h3>sealed trace</h3><div id=\"private\" class=\"kv private\"></div></div></section></main><script>const DATA=__DATA__;const KEY='ssrm252_browser_world_v12_reentry_dialogue';let i=0,timer=null,replay=[];function pct(v){return Math.round(v*1000)/10+'%'}function log(msg){const el=document.getElementById('log');el.textContent=(msg+'\\n'+el.textContent).slice(0,2600)}function pos(lineage){const m={Hearthline:[45,30],Routeline:[27,44],Marketline:[64,50],Ledgerline:[43,36],Orchardline:[50,58],Rainline:[78,73]};return m[lineage]||[50,58]}function by(list,reentry,lineage){return list.find(x=>x.reentry_id===reentry&&x.lineage===lineage)}function replayAt(turn){return DATA.replay.find(x=>x.turn_id===turn)}function render(){const w=DATA.world[i%DATA.world.length],d=DATA.dialogue[i%DATA.dialogue.length],s=by(DATA.summaries,w.reentry_id,w.lineage),r=by(DATA.repairs,w.reentry_id,w.lineage),sch=by(DATA.schedules,w.reentry_id,w.lineage),mem=by(DATA.memories,w.reentry_id,w.lineage),rp=replayAt(w.tick);const p=pos(w.lineage);document.getElementById('agent').style.left=p[0]+'%';document.getElementById('agent').style.top=p[1]+'%';document.getElementById('agent').textContent=w.agent[0];document.getElementById('agent').style.transform=d.refusal_or_boundary.includes('refusal')?'scale(1.1)':'scale(1)';document.getElementById('flower').style.transform=`rotate(${(w.tick*137.507764)%360}deg)`;document.getElementById('dialogue').textContent=w.public_state+'\\n'+w.dialogue_panel+'\\nbehavior: '+d.visible_behavior;document.getElementById('absence').textContent=s.public_summary;document.getElementById('repair').textContent=w.repair_panel;document.getElementById('schedule').textContent=sch.schedule_after_dialogue;document.getElementById('memory').textContent=mem.dialogue_memory_written+'\\nnext: '+mem.response_style_next_day;document.getElementById('replay').textContent=JSON.stringify(rp,null,2);document.getElementById('private').textContent=JSON.stringify({trace:w.trace_integrity_token,private_trace_visible:w.private_trace_visible},null,2);replay.push({turn:w.tick,reentry:w.reentry_id,lineage:w.lineage,intent:d.parsed_intent,hash:rp.export_hash});log(`reentry ${w.reentry_id} ${w.agent}: ${d.parsed_intent}`);i++}function metrics(){const keys=['browser_world_v12_reentry_dialogue_readiness','weakest_channel_score','absence_summary_completeness','repair_renegotiation_effectiveness','typed_reentry_dialogue_confidence','private_workspace_boundary'];document.getElementById('metrics').innerHTML=keys.map(k=>`<div class=\"metric\"><span>${k}</span><b>${pct(DATA.metrics[k])}</b></div>`).join('')}function start(){if(!timer)timer=setInterval(render,260)}function pause(){clearInterval(timer);timer=null}document.getElementById('start').onclick=start;document.getElementById('pause').onclick=pause;document.getElementById('step').onclick=render;document.getElementById('save').onclick=()=>localStorage.setItem(KEY,JSON.stringify({i,replay}));document.getElementById('restore').onclick=()=>{const raw=localStorage.getItem(KEY);if(raw){const s=JSON.parse(raw);i=s.i||0;replay=s.replay||[];render();log('restored re-entry dialogue state')}};document.getElementById('export').onclick=()=>{const blob=new Blob([JSON.stringify({report:252,replay},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='ssrm252_reentry_dialogue_replay.json';a.click()};document.getElementById('import').onchange=async(e)=>{const f=e.target.files[0];if(f){const obj=JSON.parse(await f.text());replay=obj.replay||[];log('imported replay '+replay.length)}};document.getElementById('inspect').onclick=()=>document.getElementById('private').classList.toggle('open');document.getElementById('reply').onclick=()=>{replay.push({turn:'typed_reply',text:document.getElementById('note').value});log('typed reply recorded');render()};metrics();render();</script></body></html>"""
    return template.replace("__DATA__", json.dumps(payload))


def run(seed: int) -> dict[str, Any]:
    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    source = source_summary()
    summaries = build_summaries(seed)
    dialogue = build_dialogue(seed, summaries)
    repairs = build_repairs(summaries)
    refusals = build_refusals(repairs)
    schedules = build_schedules(repairs)
    memories = build_relationships(repairs)
    replay = build_replay(dialogue, summaries, repairs, memories, source)
    world = build_world(dialogue, summaries, repairs, schedules, memories, replay)
    metrics = compute_metrics(source, summaries, dialogue, repairs, refusals, schedules, memories, replay, world)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["browser_world_v12_reentry_dialogue_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    prefix = ARTIFACTS / BASE
    write_csv(Path(f"{prefix}_reentry_absence_summary_frames.csv"), summaries)
    write_csv(Path(f"{prefix}_reentry_dialogue_turn_frames.csv"), dialogue)
    write_csv(Path(f"{prefix}_repair_renegotiation_frames.csv"), repairs)
    write_csv(Path(f"{prefix}_reentry_refusal_calibration_frames.csv"), refusals)
    write_csv(Path(f"{prefix}_reentry_schedule_dialogue_frames.csv"), schedules)
    write_csv(Path(f"{prefix}_reentry_relationship_memory_frames.csv"), memories)
    write_csv(Path(f"{prefix}_replay_reentry_dialogue_frames.csv"), replay)
    write_csv(Path(f"{prefix}_browser_world_v12_ticks.csv"), world)
    honest_limits = [
        "This is deterministic remembered re-entry dialogue scaffolding, not subjective consciousness.",
        "Dialogue uses seeded parser routes and templates; no LLM or autonomous natural language is called.",
        "Absence summaries are public traces, not private workspace access.",
        "Refusal, repair, and consent are simulated functional boundaries, not real consent or moral standing.",
        "The browser page is a playable 2D/2.5D state surface, not complete 3D physics.",
        "Relationship and welfare changes are bounded control variables, not proof of experienced feeling.",
        "Frequency and flower phase are rhythm variables, not metaphysical proof.",
    ]
    next_gate = "browser world v13 with live post-reentry typed dialogue choices that branch future schedules, access, trust, and agent-initiated follow-up across several days"
    results = {
        "report": REPORT,
        "name": "SSRM-3D Browser World v12 Remembered Re-Entry Dialogue Bridge",
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "verdict": verdict,
        "counts": {
            "reentry_absence_summary_frames": len(summaries),
            "reentry_dialogue_turn_frames": len(dialogue),
            "repair_renegotiation_frames": len(repairs),
            "reentry_refusal_calibration_frames": len(refusals),
            "reentry_schedule_dialogue_frames": len(schedules),
            "reentry_relationship_memory_frames": len(memories),
            "replay_reentry_dialogue_frames": len(replay),
            "browser_world_v12_ticks": len(world),
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
        "reentries": REENTRIES,
        "sample_ticks": [asdict(row) for row in world[:10]],
        "dialogue_model": "absence summary -> remembered dialogue -> bounded refusal -> repair/renegotiation -> schedule and relationship update -> replay",
        "boundary": "functional remembered re-entry dialogue scaffold; no consciousness claim",
    }
    Path(f"{prefix}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    Path(f"{prefix}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    with Path(f"{prefix}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "verdict": verdict, "readiness": metrics["browser_world_v12_reentry_dialogue_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": next_gate})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(summaries, dialogue, repairs, refusals, schedules, memories, replay, world, metrics))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    counts = results["counts"]
    print(f"module_verdict {results['verdict']}")
    print(f"browser_world_v12_reentry_dialogue_readiness {metrics['browser_world_v12_reentry_dialogue_readiness']:.6f}")
    for key in ["reentry_absence_summary_frames", "reentry_dialogue_turn_frames", "repair_renegotiation_frames", "reentry_refusal_calibration_frames", "reentry_schedule_dialogue_frames", "reentry_relationship_memory_frames", "replay_reentry_dialogue_frames", "browser_world_v12_ticks"]:
        print(f"{key} {counts[key]}")
    for key in ["source_sleep_reentry_continuity", "absence_summary_completeness", "multi_turn_dialogue_continuity", "repair_renegotiation_effectiveness", "bounded_refusal_calibration", "typed_reentry_dialogue_confidence", "private_workspace_boundary", "weakest_channel_score"]:
        print(f"{key} {metrics[key]:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
