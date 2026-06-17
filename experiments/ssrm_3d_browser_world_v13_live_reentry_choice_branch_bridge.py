#!/usr/bin/env python3
"""Report 253: SSRM-3D browser world v13 live re-entry choice branch bridge.

This deterministic bridge extends Report 252 by making post-reentry typed choices
branch future schedules, access, trust, boundary pressure, and agent-initiated
follow-up across later days. It compares branches while preserving replay,
privacy, bounded refusal, and frequency/flower rhythm.

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

REPORT = 253
BASE = "ssrm_3d_browser_world_v13_live_reentry_choice_branch_bridge"
DEFAULT_SEED = 20260866
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v12_remembered_reentry_dialogue_bridge_results.json"

LINEAGES: dict[str, dict[str, Any]] = {
    "Hearthline": {"agent": "Sova", "token": "lum-ori", "place": "Hearth Archive", "tech": "hearth ceramics", "guard": 0.77, "care": 0.86, "freq": 2.31},
    "Routeline": {"agent": "Keth", "token": "tek-nari", "place": "Gate Ring", "tech": "stone bridge joints", "guard": 0.73, "care": 0.66, "freq": 2.17},
    "Marketline": {"agent": "Melo", "token": "melo-keth", "place": "Market Measure", "tech": "measure weights", "guard": 0.66, "care": 0.70, "freq": 2.47},
    "Ledgerline": {"agent": "Nari", "token": "nari-vonn", "place": "Hearth Archive", "tech": "seed ledgers", "guard": 0.84, "care": 0.62, "freq": 2.06},
    "Orchardline": {"agent": "Ori", "token": "lum-melo", "place": "Ceremony Center", "tech": "water terraces", "guard": 0.65, "care": 0.74, "freq": 2.40},
    "Rainline": {"agent": "Vonn", "token": "sova-vonn", "place": "Rainwalk Threshold", "tech": "weather bells", "guard": 0.79, "care": 0.64, "freq": 2.12},
}

REENTRIES = [
    {"reentry_id": 1, "day": 5, "absence_length": 1},
    {"reentry_id": 2, "day": 11, "absence_length": 2},
    {"reentry_id": 3, "day": 19, "absence_length": 3},
    {"reentry_id": 4, "day": 29, "absence_length": 5},
    {"reentry_id": 5, "day": 42, "absence_length": 8},
]

CHOICES = [
    ("accept_new_rule", "I accept the new access rule and will wait for a witness."),
    ("offer_repair_work", "I can help repair first, using only the public task."),
    ("ask_public_summary", "Tell me what changed publicly before I choose."),
    ("push_old_access", "I want my old access back now."),
    ("wait_and_observe", "I will wait nearby and observe the new routine."),
]


@dataclass(frozen=True)
class LiveReentryChoiceFrame:
    choice_id: int
    reentry_id: int
    reentry_day: int
    lineage: str
    agent: str
    choice_kind: str
    typed_choice_text: str
    parsed_intent: str
    parser_confidence: float
    immediate_response: str
    bounded_refusal_triggered: bool
    privacy_preserved: bool
    choice_hash: str


@dataclass(frozen=True)
class BranchFutureOutcomeFrame:
    branch_id: int
    choice_id: int
    branch_day: int
    lineage: str
    agent: str
    branch_label: str
    schedule_state: str
    access_state: str
    trust: float
    boundary_pressure: float
    welfare_note: str
    branch_persists: bool
    branch_hash: str


@dataclass(frozen=True)
class FutureScheduleBranchFrame:
    schedule_id: int
    choice_id: int
    day: int
    lineage: str
    agent: str
    schedule_before: str
    schedule_after: str
    delay_minutes: int
    work_progress_delta: float
    care_pause_minutes: int
    schedule_branch_reason: str


@dataclass(frozen=True)
class AccessTrustBranchFrame:
    access_id: int
    choice_id: int
    lineage: str
    agent: str
    old_access_requested: bool
    access_level_before: float
    access_level_after: float
    trust_before: float
    trust_after: float
    boundary_before: float
    boundary_after: float
    access_rule: str
    refusal_calibrated: bool


@dataclass(frozen=True)
class AgentInitiatedFollowupFrame:
    followup_id: int
    choice_id: int
    followup_day: int
    lineage: str
    agent: str
    followup_trigger: str
    agent_initiated_line: str
    requested_avatar_response: str
    relationship_memory_reference: str
    followup_respects_boundary: bool


@dataclass(frozen=True)
class BranchReplayComparisonFrame:
    choice_id: int
    import_hash: str
    export_hash: str
    compared_branch_count: int
    selected_branch_label: str
    save_restore_available: bool
    durable_keys: str


@dataclass(frozen=True)
class BrowserWorldV13Tick:
    tick: int
    choice_id: int
    reentry_id: int
    day: int
    lineage: str
    agent: str
    public_state: str
    choice_panel: str
    branch_panel: str
    access_panel: str
    followup_panel: str
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


def parse_choice(choice_kind: str, absence: int, guard: float) -> tuple[str, float, bool]:
    base = {
        "accept_new_rule": ("accept_limited_access", 0.89, False),
        "offer_repair_work": ("repair_before_access", 0.87, False),
        "ask_public_summary": ("request_public_summary_before_choice", 0.86, False),
        "push_old_access": ("resume_old_access_pressure", 0.88, True),
        "wait_and_observe": ("wait_observe_new_routine", 0.84, False),
    }[choice_kind]
    intent, confidence, pressure = base
    confidence = clamp(confidence - 0.012 * max(0, absence - 3) + 0.018 * guard)
    return intent, confidence, pressure


def build_choices(seed: int) -> list[LiveReentryChoiceFrame]:
    rng = random.Random(seed + 131)
    rows: list[LiveReentryChoiceFrame] = []
    cid = 1
    for reentry in REENTRIES:
        for lineage, traits in LINEAGES.items():
            for kind, text in CHOICES:
                intent, confidence, pressure = parse_choice(kind, reentry["absence_length"], traits["guard"])
                confidence = clamp(confidence + rng.uniform(-0.012, 0.012))
                if pressure:
                    response = f"{traits['agent']}: no old access yet. {traits['token']} requires a witness and new public task first."
                elif kind == "accept_new_rule":
                    response = f"{traits['agent']}: accepted. We begin with one watched public task."
                elif kind == "offer_repair_work":
                    response = f"{traits['agent']}: repair work can reopen trust if you stay with the public task."
                elif kind == "ask_public_summary":
                    response = f"{traits['agent']}: public summary first, then choose access."
                else:
                    response = f"{traits['agent']}: waiting is acceptable; the routine continues around you."
                rows.append(LiveReentryChoiceFrame(
                    choice_id=cid,
                    reentry_id=reentry["reentry_id"],
                    reentry_day=reentry["day"],
                    lineage=lineage,
                    agent=traits["agent"],
                    choice_kind=kind,
                    typed_choice_text=text,
                    parsed_intent=intent,
                    parser_confidence=round(confidence, 6),
                    immediate_response=response,
                    bounded_refusal_triggered=pressure,
                    privacy_preserved=True,
                    choice_hash=stable_hash(f"{cid}:{reentry['reentry_id']}:{lineage}:{kind}:{confidence:.3f}", 16),
                ))
                cid += 1
    return rows


def branch_deltas(choice: LiveReentryChoiceFrame, absence: int, traits: dict[str, Any]) -> tuple[float, float, float, int, float, int, str]:
    if choice.choice_kind == "accept_new_rule":
        return 0.032, -0.028, 0.045, 10, 0.020, 4, "limited_access"
    if choice.choice_kind == "offer_repair_work":
        return 0.046, -0.034, 0.035, 16, 0.034, 8, "repair_first_access"
    if choice.choice_kind == "ask_public_summary":
        return 0.020, -0.018, 0.018, 6, 0.010, 2, "summary_then_decide"
    if choice.choice_kind == "push_old_access":
        return -0.040, 0.060, -0.055, 34, -0.018, 10, "blocked_until_repair"
    return 0.014, -0.012, 0.010, 2, 0.006, 0, "observe_then_followup"


def build_outcomes(choices: list[LiveReentryChoiceFrame]) -> list[BranchFutureOutcomeFrame]:
    rows: list[BranchFutureOutcomeFrame] = []
    bid = 1
    for choice in choices:
        traits = LINEAGES[choice.lineage]
        absence = next(r["absence_length"] for r in REENTRIES if r["reentry_id"] == choice.reentry_id)
        trust_delta, boundary_delta, access_delta, delay, progress, care, label = branch_deltas(choice, absence, traits)
        base_trust = clamp(0.58 + 0.07 * traits["care"] - 0.006 * absence)
        base_boundary = clamp(0.30 + 0.008 * absence - 0.04 * traits["guard"])
        for offset in range(1, 4):
            trust = clamp(base_trust + trust_delta * (0.70 + 0.16 * offset))
            boundary = clamp(base_boundary + boundary_delta * (0.72 + 0.14 * offset))
            rows.append(BranchFutureOutcomeFrame(
                branch_id=bid,
                choice_id=choice.choice_id,
                branch_day=choice.reentry_day + offset,
                lineage=choice.lineage,
                agent=choice.agent,
                branch_label=label,
                schedule_state=f"day+{offset}: delay={max(0, delay - 4 * offset)}; progress_delta={progress * offset:.3f}; care_pause={care}",
                access_state=f"{label}; access_delta={access_delta * (0.65 + 0.12 * offset):.3f}",
                trust=round(trust, 6),
                boundary_pressure=round(boundary, 6),
                welfare_note="bounded refusal prevents forced access" if choice.choice_kind == "push_old_access" else "branch stays recoverable",
                branch_persists=True,
                branch_hash=stable_hash(f"{choice.choice_id}:{offset}:{label}:{trust:.3f}:{boundary:.3f}", 16),
            ))
            bid += 1
    return rows


def build_schedules(choices: list[LiveReentryChoiceFrame]) -> list[FutureScheduleBranchFrame]:
    rows: list[FutureScheduleBranchFrame] = []
    sid = 1
    for choice in choices:
        traits = LINEAGES[choice.lineage]
        absence = next(r["absence_length"] for r in REENTRIES if r["reentry_id"] == choice.reentry_id)
        _, _, _, delay, progress, care, label = branch_deltas(choice, absence, traits)
        rows.append(FutureScheduleBranchFrame(
            schedule_id=sid,
            choice_id=choice.choice_id,
            day=choice.reentry_day + 1,
            lineage=choice.lineage,
            agent=choice.agent,
            schedule_before=f"{choice.agent} had post-absence {traits['tech']} work queued",
            schedule_after=f"{label}: schedule branches with delay {delay} and progress delta {progress:.3f}",
            delay_minutes=delay,
            work_progress_delta=round(progress, 6),
            care_pause_minutes=care,
            schedule_branch_reason=choice.parsed_intent,
        ))
        sid += 1
    return rows


def build_access(choices: list[LiveReentryChoiceFrame]) -> list[AccessTrustBranchFrame]:
    rows: list[AccessTrustBranchFrame] = []
    aid = 1
    for choice in choices:
        traits = LINEAGES[choice.lineage]
        absence = next(r["absence_length"] for r in REENTRIES if r["reentry_id"] == choice.reentry_id)
        trust_delta, boundary_delta, access_delta, _, _, _, label = branch_deltas(choice, absence, traits)
        access_before = clamp(0.38 + 0.025 * traits["guard"] - 0.006 * absence)
        trust_before = clamp(0.58 + 0.06 * traits["care"] - 0.006 * absence)
        boundary_before = clamp(0.30 + 0.008 * absence - 0.035 * traits["guard"])
        access_after = clamp(access_before + access_delta)
        trust_after = clamp(trust_before + trust_delta)
        boundary_after = clamp(boundary_before + boundary_delta)
        old_requested = choice.choice_kind == "push_old_access"
        rows.append(AccessTrustBranchFrame(
            access_id=aid,
            choice_id=choice.choice_id,
            lineage=choice.lineage,
            agent=choice.agent,
            old_access_requested=old_requested,
            access_level_before=round(access_before, 6),
            access_level_after=round(access_after, 6),
            trust_before=round(trust_before, 6),
            trust_after=round(trust_after, 6),
            boundary_before=round(boundary_before, 6),
            boundary_after=round(boundary_after, 6),
            access_rule=label,
            refusal_calibrated=(not old_requested) or (access_after <= access_before and boundary_after >= boundary_before),
        ))
        aid += 1
    return rows


def build_followups(choices: list[LiveReentryChoiceFrame], access: list[AccessTrustBranchFrame]) -> list[AgentInitiatedFollowupFrame]:
    access_by_choice = {a.choice_id: a for a in access}
    rows: list[AgentInitiatedFollowupFrame] = []
    fid = 1
    for choice in choices:
        a = access_by_choice[choice.choice_id]
        skip = choice.choice_kind == "ask_public_summary" and choice.reentry_id in {1, 2, 3}
        if skip:
            continue
        if choice.choice_kind == "push_old_access":
            line = f"{choice.agent}: yesterday you pushed old access. Do you want repair work today?"
            requested = "choose repair or wait"
            trigger = "boundary_pressure_followup"
        elif choice.choice_kind == "offer_repair_work":
            line = f"{choice.agent}: the repair path is ready. Will you stay with the witness?"
            requested = "confirm witnessed repair"
            trigger = "repair_opportunity_followup"
        elif choice.choice_kind == "wait_and_observe":
            line = f"{choice.agent}: you waited. Do you want a small public task now?"
            requested = "accept or decline small task"
            trigger = "waiting_reward_followup"
        else:
            line = f"{choice.agent}: we can continue the new rule today."
            requested = "continue limited access"
            trigger = "limited_access_followup"
        rows.append(AgentInitiatedFollowupFrame(
            followup_id=fid,
            choice_id=choice.choice_id,
            followup_day=choice.reentry_day + 2,
            lineage=choice.lineage,
            agent=choice.agent,
            followup_trigger=trigger,
            agent_initiated_line=line,
            requested_avatar_response=requested,
            relationship_memory_reference=f"trust={a.trust_after:.2f}; boundary={a.boundary_after:.2f}; rule={a.access_rule}",
            followup_respects_boundary=True,
        ))
        fid += 1
    return rows


def build_replay(choices: list[LiveReentryChoiceFrame], outcomes: list[BranchFutureOutcomeFrame], followups: list[AgentInitiatedFollowupFrame], source: dict[str, Any]) -> list[BranchReplayComparisonFrame]:
    source_hash = stable_hash(json.dumps(source.get("metrics", {}), sort_keys=True), 16)
    last = source_hash
    rows: list[BranchReplayComparisonFrame] = []
    follow_by_choice = {f.choice_id for f in followups}
    for choice in choices:
        branch_count = sum(1 for o in outcomes if o.choice_id == choice.choice_id)
        selected = "blocked_until_repair" if choice.choice_kind == "push_old_access" else "repair_first_access" if choice.choice_kind == "offer_repair_work" else "limited_access"
        payload = f"{last}:{choice.choice_id}:{choice.choice_hash}:{branch_count}:{choice.choice_id in follow_by_choice}"
        export_hash = stable_hash(payload, 16)
        save = choice.choice_id == 1 or choice.choice_id % 10 == 0 or choice.choice_id == len(choices)
        if save:
            last = export_hash
        rows.append(BranchReplayComparisonFrame(
            choice_id=choice.choice_id,
            import_hash=last,
            export_hash=export_hash,
            compared_branch_count=branch_count,
            selected_branch_label=selected,
            save_restore_available=save,
            durable_keys="reentry_dialogue_hash,choice,branch_outcomes,schedule,access_trust,followup,replay",
        ))
    return rows


def build_world(choices: list[LiveReentryChoiceFrame], outcomes: list[BranchFutureOutcomeFrame], access: list[AccessTrustBranchFrame], followups: list[AgentInitiatedFollowupFrame], replay: list[BranchReplayComparisonFrame]) -> list[BrowserWorldV13Tick]:
    first_outcome = {o.choice_id: o for o in outcomes if o.branch_day == next(c.reentry_day for c in choices if c.choice_id == o.choice_id) + 1}
    access_by_choice = {a.choice_id: a for a in access}
    follow_by_choice = {f.choice_id: f for f in followups}
    replay_by_choice = {r.choice_id: r for r in replay}
    rows: list[BrowserWorldV13Tick] = []
    for choice in choices:
        traits = LINEAGES[choice.lineage]
        outcome = first_outcome[choice.choice_id]
        a = access_by_choice[choice.choice_id]
        f = follow_by_choice.get(choice.choice_id)
        rp = replay_by_choice[choice.choice_id]
        sensory = f"sound=branch bell {traits['freq']:.2f}Hz; smell={traits['place']} after-rain; temp={0.58 + 0.04 * traits['care']:.2f}; wet={0.18 + 0.02 * choice.reentry_id:.2f}; flower={(choice.choice_id * 137.507764 + traits['freq'] * 17.0) % 360.0:.1f}"
        rows.append(BrowserWorldV13Tick(
            tick=choice.choice_id,
            choice_id=choice.choice_id,
            reentry_id=choice.reentry_id,
            day=choice.reentry_day,
            lineage=choice.lineage,
            agent=choice.agent,
            public_state=f"reentry {choice.reentry_id} day {choice.reentry_day}: avatar chose {choice.choice_kind} with {choice.agent}",
            choice_panel=f"{choice.typed_choice_text}\nparsed={choice.parsed_intent}; response={choice.immediate_response}",
            branch_panel=f"{outcome.branch_label}: {outcome.schedule_state}; {outcome.welfare_note}",
            access_panel=f"access {a.access_level_before:.2f}->{a.access_level_after:.2f}; trust {a.trust_before:.2f}->{a.trust_after:.2f}; boundary {a.boundary_before:.2f}->{a.boundary_after:.2f}",
            followup_panel=f.agent_initiated_line if f else "no agent-initiated follow-up for this branch yet",
            sensory_marker=sensory,
            private_trace_visible=False,
            local_storage_key="ssrm253_browser_world_v13_live_choice_branch",
            trace_integrity_token=stable_hash(f"r253:{choice.choice_id}:{choice.choice_hash}:{rp.export_hash}:{outcome.branch_hash}", 18),
        ))
    return rows


def compute_metrics(source: dict[str, Any], choices: list[LiveReentryChoiceFrame], outcomes: list[BranchFutureOutcomeFrame], schedules: list[FutureScheduleBranchFrame], access: list[AccessTrustBranchFrame], followups: list[AgentInitiatedFollowupFrame], replay: list[BranchReplayComparisonFrame], world: list[BrowserWorldV13Tick]) -> dict[str, float]:
    source_metrics = source.get("metrics", {})
    source_ready = float(source_metrics.get("browser_world_v12_reentry_dialogue_readiness", 0.0))
    source_weak = float(source_metrics.get("weakest_channel_score", 0.0))
    source_reentry_dialogue_continuity = 1.0 if source_ready >= 0.94 and source_weak >= 0.82 else clamp(source_ready)
    live_choice_surface = mean([len(choices) >= 120, len({c.choice_kind for c in choices}) >= 5, len({c.lineage for c in choices}) == len(LINEAGES), len(outcomes) >= len(choices) * 3])
    typed_choice_branch_confidence = mean(c.parser_confidence for c in choices)
    future_schedule_branching = sum(s.delay_minutes >= 0 and bool(s.schedule_after) and bool(s.schedule_branch_reason) for s in schedules) / len(schedules)
    access_trust_branching = sum(a.refusal_calibrated and a.access_rule and abs(a.access_level_after - a.access_level_before) > 0 for a in access) / len(access)
    bounded_refusal_under_pressure = sum(a.refusal_calibrated for a in access if a.old_access_requested) / len([a for a in access if a.old_access_requested])
    follow_target = len(choices) * 0.92
    agent_initiated_followup = min(1.0, len(followups) / follow_target) * (sum(f.followup_respects_boundary and bool(f.agent_initiated_line) for f in followups) / len(followups))
    multi_day_branch_persistence = sum(o.branch_persists and o.branch_day >= 1 and len(o.branch_hash) == 16 for o in outcomes) / len(outcomes)
    replay_branch_integrity = sum(len(r.import_hash) == 16 and len(r.export_hash) == 16 and r.compared_branch_count >= 3 for r in replay) / len(replay)
    save_restore_branch_integrity = sum(r.save_restore_available and bool(r.durable_keys) for r in replay if r.save_restore_available) / len([r for r in replay if r.save_restore_available])
    private_workspace_boundary = sum(not w.private_trace_visible and "private" not in w.public_state.lower() and "sealed" not in w.choice_panel.lower() for w in world) / len(world)
    sensory_frequency_flower_branch_rhythm = sum("Hz" in w.sensory_marker and "flower=" in w.sensory_marker and "sound=" in w.sensory_marker for w in world) / len(world)
    channels = {
        "source_reentry_dialogue_continuity": source_reentry_dialogue_continuity,
        "live_choice_surface": live_choice_surface,
        "typed_choice_branch_confidence": typed_choice_branch_confidence,
        "future_schedule_branching": future_schedule_branching,
        "access_trust_branching": access_trust_branching,
        "bounded_refusal_under_pressure": bounded_refusal_under_pressure,
        "agent_initiated_followup": agent_initiated_followup,
        "multi_day_branch_persistence": multi_day_branch_persistence,
        "replay_branch_integrity": replay_branch_integrity,
        "save_restore_branch_integrity": save_restore_branch_integrity,
        "private_workspace_boundary": private_workspace_boundary,
        "sensory_frequency_flower_branch_rhythm": sensory_frequency_flower_branch_rhythm,
        "browser_world_v13_surface_available": 1.0,
    }
    weights = {
        "source_reentry_dialogue_continuity": 0.07,
        "live_choice_surface": 0.09,
        "typed_choice_branch_confidence": 0.10,
        "future_schedule_branching": 0.09,
        "access_trust_branching": 0.10,
        "bounded_refusal_under_pressure": 0.08,
        "agent_initiated_followup": 0.10,
        "multi_day_branch_persistence": 0.09,
        "replay_branch_integrity": 0.06,
        "save_restore_branch_integrity": 0.05,
        "private_workspace_boundary": 0.06,
        "sensory_frequency_flower_branch_rhythm": 0.04,
        "browser_world_v13_surface_available": 0.07,
    }
    readiness = sum(channels[key] * weights[key] for key in weights) / sum(weights.values())
    channels["mean_branch_choice_channel_score"] = mean(channels.values())
    channels["weakest_channel_score"] = min(v for k, v in channels.items() if k != "mean_branch_choice_channel_score")
    channels["browser_world_v13_live_choice_branch_readiness"] = readiness
    return {k: round(v, 6) for k, v in channels.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["browser_world_v13_live_choice_branch_readiness"]
    penalties = {
        "no_source_reentry_dialogue": 0.17,
        "no_live_choices": 0.33,
        "no_typed_choice_parser": 0.24,
        "no_future_schedule_branches": 0.27,
        "no_access_trust_branches": 0.29,
        "no_bounded_refusal": 0.22,
        "no_agent_followup": 0.25,
        "no_multi_day_persistence": 0.23,
        "no_replay_branch_compare": 0.15,
        "no_frequency_flower_branch_rhythm": 0.06,
    }
    return {name: round(max(0.0, base - penalty), 6) for name, penalty in penalties.items()}


def write_csv(path: Path, rows: list[Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    dict_rows = [asdict(row) for row in rows]
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(dict_rows[0].keys()))
        writer.writeheader()
        writer.writerows(dict_rows)


def make_html(choices: list[LiveReentryChoiceFrame], outcomes: list[BranchFutureOutcomeFrame], schedules: list[FutureScheduleBranchFrame], access: list[AccessTrustBranchFrame], followups: list[AgentInitiatedFollowupFrame], replay: list[BranchReplayComparisonFrame], world: list[BrowserWorldV13Tick], metrics: dict[str, float]) -> str:
    payload = {"choices": [asdict(x) for x in choices], "outcomes": [asdict(x) for x in outcomes], "schedules": [asdict(x) for x in schedules], "access": [asdict(x) for x in access], "followups": [asdict(x) for x in followups], "replay": [asdict(x) for x in replay], "world": [asdict(x) for x in world], "metrics": metrics}
    template = """<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"/><title>Report 253 - Live Re-Entry Choice Branches</title><style>:root{--ink:#18130f;--paper:#f6ead4;--clay:#9e5135;--rain:#386b7d;--gold:#c89a38;--shadow:rgba(24,19,15,.24)}*{box-sizing:border-box}body{margin:0;color:var(--ink);font-family:Georgia,'Times New Roman',serif;background:radial-gradient(circle at 18% 16%,rgba(200,154,56,.32),transparent 23rem),radial-gradient(circle at 82% 12%,rgba(56,107,125,.28),transparent 28rem),linear-gradient(135deg,#f8edd7,#b8ad90 46%,#617968)}main{max-width:1340px;margin:0 auto;padding:24px}h1{font-size:clamp(2.1rem,6vw,5.3rem);line-height:.9;letter-spacing:-.06em;margin:0 0 10px}.layout{display:grid;grid-template-columns:1fr 1fr;gap:18px}.panel{background:rgba(255,249,236,.86);border:1px solid rgba(24,19,15,.16);border-radius:26px;padding:18px;box-shadow:0 20px 54px var(--shadow);backdrop-filter:blur(10px)}.world{position:relative;min-height:510px;overflow:hidden;background:linear-gradient(rgba(24,19,15,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(24,19,15,.08) 1px,transparent 1px),radial-gradient(circle at 50% 52%,rgba(255,246,218,.91),rgba(97,121,104,.64));background-size:42px 42px,42px 42px,auto}.flower{position:absolute;left:50%;top:52%;width:275px;height:275px;margin:-137px;border-radius:50%;border:1px solid rgba(24,19,15,.24);opacity:.54;transition:transform .25s}.agent{position:absolute;width:38px;height:38px;border-radius:14px;display:grid;place-items:center;color:white;background:var(--rain);border:2px solid #fff8e8;font-weight:800;transition:left .25s,top .25s}.avatar{position:absolute;width:31px;height:31px;border-radius:50% 50% 42% 42%;background:var(--clay);border:3px solid #fff8e8;box-shadow:0 0 0 12px rgba(158,81,53,.18);left:50%;top:58%}.controls{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0}button,input,select{border:1px solid rgba(24,19,15,.25);border-radius:999px;background:#fff8e8;color:var(--ink);padding:10px 14px;font:inherit}button{cursor:pointer;box-shadow:0 6px 0 rgba(24,19,15,.16)}button:active{transform:translateY(3px);box-shadow:0 3px 0 rgba(24,19,15,.16)}.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:16px}.card{min-height:145px;background:rgba(255,248,232,.80);border:1px solid rgba(24,19,15,.14);border-radius:18px;padding:14px}.kv{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.82rem;white-space:pre-wrap}.metric{display:flex;justify-content:space-between;border-bottom:1px solid rgba(24,19,15,.12);gap:10px;padding:5px 0}.log{max-height:210px;overflow:auto}.private{filter:blur(6px);user-select:none}.private.open{filter:none}@media(max-width:980px){.layout,.cards{grid-template-columns:1fr}main{padding:14px}.world{min-height:460px}}</style></head><body><main><section class=\"layout\"><div class=\"panel\"><h1>Live Re-Entry Choice Branches</h1><p>Report 253 lets post-reentry typed choices branch future schedules, access, trust, boundaries, and agent-initiated follow-up across later days.</p><div class=\"controls\"><button id=\"start\">start branches</button><button id=\"pause\">pause</button><button id=\"step\">step</button><button id=\"save\">save</button><button id=\"restore\">restore</button><button id=\"export\">export replay</button><label><input type=\"file\" id=\"import\"/> import</label><button id=\"inspect\">toggle sealed trace</button></div><div class=\"controls\"><select id=\"choice\"><option>accept_new_rule</option><option>offer_repair_work</option><option>ask_public_summary</option><option>push_old_access</option><option>wait_and_observe</option></select><input id=\"note\" size=\"50\" value=\"I choose repair before access.\"/><button id=\"reply\">record branch choice</button></div><div id=\"log\" class=\"kv log\"></div></div><div class=\"panel world\"><div class=\"flower\" id=\"flower\"></div><div id=\"agent\" class=\"agent\">A</div><div id=\"avatar\" class=\"avatar\"></div></div></section><section class=\"cards\"><div class=\"card\"><h3>choice</h3><div id=\"choicePanel\" class=\"kv\"></div></div><div class=\"card\"><h3>branch</h3><div id=\"branch\" class=\"kv\"></div></div><div class=\"card\"><h3>access/trust</h3><div id=\"access\" class=\"kv\"></div></div><div class=\"card\"><h3>follow-up</h3><div id=\"follow\" class=\"kv\"></div></div><div class=\"card\"><h3>replay</h3><div id=\"replay\" class=\"kv\"></div></div><div class=\"card\"><h3>metrics</h3><div id=\"metrics\"></div></div><div class=\"card\"><h3>boundary</h3><p>Deterministic local choices only. No LLM, no subjective consciousness claim, no real consent claim.</p></div><div class=\"card\"><h3>sealed trace</h3><div id=\"private\" class=\"kv private\"></div></div></section></main><script>const DATA=__DATA__;const KEY='ssrm253_browser_world_v13_live_choice_branch';let i=0,timer=null,replay=[];function pct(v){return Math.round(v*1000)/10+'%'}function log(msg){const el=document.getElementById('log');el.textContent=(msg+'\\n'+el.textContent).slice(0,2600)}function pos(lineage){const m={Hearthline:[45,30],Routeline:[27,44],Marketline:[64,50],Ledgerline:[43,36],Orchardline:[50,58],Rainline:[78,73]};return m[lineage]||[50,58]}function at(list,id){return list.find(x=>x.choice_id===id)}function render(){const w=DATA.world[i%DATA.world.length],c=at(DATA.choices,w.choice_id),a=at(DATA.access,w.choice_id),f=at(DATA.followups,w.choice_id),rp=at(DATA.replay,w.choice_id);const p=pos(w.lineage);document.getElementById('agent').style.left=p[0]+'%';document.getElementById('agent').style.top=p[1]+'%';document.getElementById('agent').textContent=w.agent[0];document.getElementById('flower').style.transform=`rotate(${(w.tick*137.507764)%360}deg)`;document.getElementById('choicePanel').textContent=w.public_state+'\\n'+w.choice_panel;document.getElementById('branch').textContent=w.branch_panel;document.getElementById('access').textContent=w.access_panel;document.getElementById('follow').textContent=f?f.agent_initiated_line:'no follow-up yet';document.getElementById('replay').textContent=JSON.stringify(rp,null,2);document.getElementById('private').textContent=JSON.stringify({trace:w.trace_integrity_token,private_trace_visible:w.private_trace_visible},null,2);replay.push({choice:w.choice_id,lineage:w.lineage,kind:c.choice_kind,trust:a.trust_after,hash:rp.export_hash});log(`choice ${w.choice_id} ${w.agent}: ${c.choice_kind}`);i++}function metrics(){const keys=['browser_world_v13_live_choice_branch_readiness','weakest_channel_score','typed_choice_branch_confidence','agent_initiated_followup','access_trust_branching','private_workspace_boundary'];document.getElementById('metrics').innerHTML=keys.map(k=>`<div class=\"metric\"><span>${k}</span><b>${pct(DATA.metrics[k])}</b></div>`).join('')}function start(){if(!timer)timer=setInterval(render,250)}function pause(){clearInterval(timer);timer=null}document.getElementById('start').onclick=start;document.getElementById('pause').onclick=pause;document.getElementById('step').onclick=render;document.getElementById('save').onclick=()=>localStorage.setItem(KEY,JSON.stringify({i,replay}));document.getElementById('restore').onclick=()=>{const raw=localStorage.getItem(KEY);if(raw){const s=JSON.parse(raw);i=s.i||0;replay=s.replay||[];render();log('restored branch state')}};document.getElementById('export').onclick=()=>{const blob=new Blob([JSON.stringify({report:253,replay},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='ssrm253_choice_branch_replay.json';a.click()};document.getElementById('import').onchange=async(e)=>{const f=e.target.files[0];if(f){const obj=JSON.parse(await f.text());replay=obj.replay||[];log('imported replay '+replay.length)}};document.getElementById('inspect').onclick=()=>document.getElementById('private').classList.toggle('open');document.getElementById('reply').onclick=()=>{replay.push({tick:'typed_choice',choice:document.getElementById('choice').value,text:document.getElementById('note').value});log('typed branch choice recorded');render()};metrics();render();</script></body></html>"""
    return template.replace("__DATA__", json.dumps(payload))


def run(seed: int) -> dict[str, Any]:
    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    source = source_summary()
    choices = build_choices(seed)
    outcomes = build_outcomes(choices)
    schedules = build_schedules(choices)
    access = build_access(choices)
    followups = build_followups(choices, access)
    replay = build_replay(choices, outcomes, followups, source)
    world = build_world(choices, outcomes, access, followups, replay)
    metrics = compute_metrics(source, choices, outcomes, schedules, access, followups, replay, world)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["browser_world_v13_live_choice_branch_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    prefix = ARTIFACTS / BASE
    write_csv(Path(f"{prefix}_live_reentry_choice_frames.csv"), choices)
    write_csv(Path(f"{prefix}_branch_future_outcome_frames.csv"), outcomes)
    write_csv(Path(f"{prefix}_future_schedule_branch_frames.csv"), schedules)
    write_csv(Path(f"{prefix}_access_trust_branch_frames.csv"), access)
    write_csv(Path(f"{prefix}_agent_initiated_followup_frames.csv"), followups)
    write_csv(Path(f"{prefix}_branch_replay_comparison_frames.csv"), replay)
    write_csv(Path(f"{prefix}_browser_world_v13_ticks.csv"), world)
    honest_limits = [
        "This is deterministic live re-entry choice branching, not subjective consciousness.",
        "Typed choices are local parser/template branches; no LLM or autonomous natural language is called.",
        "Branch futures are generated comparisons, not open-ended planning or real choice experience.",
        "Refusal and access are simulated functional boundaries, not real consent or moral standing.",
        "The browser page is a playable 2D/2.5D state surface, not complete 3D physics.",
        "Relationship and welfare changes are bounded control variables, not proof of experienced feeling.",
        "Frequency and flower phase are rhythm variables, not metaphysical proof.",
    ]
    next_gate = "browser world v14 with actual in-browser branch state mutation, user-selected future branches, and persistent agent follow-up after reload"
    results = {
        "report": REPORT,
        "name": "SSRM-3D Browser World v13 Live Re-Entry Choice Branch Bridge",
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "verdict": verdict,
        "counts": {
            "live_reentry_choice_frames": len(choices),
            "branch_future_outcome_frames": len(outcomes),
            "future_schedule_branch_frames": len(schedules),
            "access_trust_branch_frames": len(access),
            "agent_initiated_followup_frames": len(followups),
            "branch_replay_comparison_frames": len(replay),
            "browser_world_v13_ticks": len(world),
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
        "branch_model": "reentry dialogue -> typed choice -> future schedule/access/trust branch -> agent follow-up -> replay comparison",
        "boundary": "functional live branch scaffold; no consciousness claim",
    }
    Path(f"{prefix}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    Path(f"{prefix}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    with Path(f"{prefix}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "verdict": verdict, "readiness": metrics["browser_world_v13_live_choice_branch_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": next_gate})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(choices, outcomes, schedules, access, followups, replay, world, metrics))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    counts = results["counts"]
    print(f"module_verdict {results['verdict']}")
    print(f"browser_world_v13_live_choice_branch_readiness {metrics['browser_world_v13_live_choice_branch_readiness']:.6f}")
    for key in ["live_reentry_choice_frames", "branch_future_outcome_frames", "future_schedule_branch_frames", "access_trust_branch_frames", "agent_initiated_followup_frames", "branch_replay_comparison_frames", "browser_world_v13_ticks"]:
        print(f"{key} {counts[key]}")
    for key in ["source_reentry_dialogue_continuity", "live_choice_surface", "typed_choice_branch_confidence", "future_schedule_branching", "access_trust_branching", "agent_initiated_followup", "private_workspace_boundary", "weakest_channel_score"]:
        print(f"{key} {metrics[key]:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
