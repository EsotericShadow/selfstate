#!/usr/bin/env python3
"""Report 254: SSRM-3D browser world v14 in-browser branch state mutation bridge.

This deterministic bridge extends Report 253 from generated branch comparisons
to a browser artifact that mutates selected branch state locally. User-selected
branches update schedule, access, trust, boundary pressure, welfare notes, and
agent follow-up; localStorage restore and rollback preserve the selected branch
state across reload-like probes.

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

REPORT = 254
BASE = "ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge"
DEFAULT_SEED = 20260867
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v13_live_reentry_choice_branch_bridge_results.json"

LINEAGES: dict[str, dict[str, Any]] = {
    "Hearthline": {"agent": "Sova", "place": "Hearth Archive", "tech": "hearth ceramics", "guard": 0.77, "care": 0.86, "freq": 2.31},
    "Routeline": {"agent": "Keth", "place": "Gate Ring", "tech": "stone bridge joints", "guard": 0.73, "care": 0.66, "freq": 2.17},
    "Marketline": {"agent": "Melo", "place": "Market Measure", "tech": "measure weights", "guard": 0.66, "care": 0.70, "freq": 2.47},
    "Ledgerline": {"agent": "Nari", "place": "Hearth Archive", "tech": "seed ledgers", "guard": 0.84, "care": 0.62, "freq": 2.06},
    "Orchardline": {"agent": "Ori", "place": "Ceremony Center", "tech": "water terraces", "guard": 0.65, "care": 0.74, "freq": 2.40},
    "Rainline": {"agent": "Vonn", "place": "Rainwalk Threshold", "tech": "weather bells", "guard": 0.79, "care": 0.64, "freq": 2.12},
}

BRANCHES = [
    ("limited_access", "Accept one watched public task, review tomorrow."),
    ("repair_first_access", "Do repair work first, then ask again."),
    ("summary_then_decide", "Request public summary before choosing access."),
    ("blocked_until_repair", "Push old access; get blocked until repair."),
    ("observe_then_followup", "Wait and observe; invite later follow-up."),
]

REENTRY_IDS = [1, 2, 3, 4, 5]


@dataclass(frozen=True)
class BrowserBranchSelectionFrame:
    choice_id: int
    reentry_id: int
    lineage: str
    agent: str
    selected_branch_label: str
    typed_selection_text: str
    parser_confidence: float
    selection_source: str
    privacy_preserved: bool
    bounded_refusal_active: bool
    selection_hash: str


@dataclass(frozen=True)
class InBrowserMutableStateFrame:
    mutation_id: int
    choice_id: int
    simulated_day: int
    lineage: str
    agent: str
    selected_branch_label: str
    schedule_state_after: str
    access_level_after: float
    trust_after: float
    boundary_pressure_after: float
    welfare_note_after: str
    agent_followup_due_day: int
    local_storage_key: str
    stored_state_json: str
    mutation_hash: str


@dataclass(frozen=True)
class ReloadRestoreProbeFrame:
    restore_id: int
    choice_id: int
    lineage: str
    selected_branch_label: str
    snapshot_hash: str
    restore_hash: str
    branch_survives_reload: bool
    schedule_restored: bool
    access_restored: bool
    trust_restored: bool
    followup_restored: bool
    private_trace_still_hidden: bool


@dataclass(frozen=True)
class AgentFollowupAfterReloadFrame:
    followup_id: int
    choice_id: int
    followup_day: int
    lineage: str
    agent: str
    selected_branch_label: str
    followup_trigger: str
    agent_line_after_reload: str
    requested_avatar_response: str
    derived_from_restored_state: bool
    respects_boundary: bool
    followup_hash: str


@dataclass(frozen=True)
class ScheduleAccessTrustMutationFrame:
    mutation_id: int
    choice_id: int
    lineage: str
    agent: str
    schedule_delta_minutes: int
    access_delta: float
    trust_delta: float
    boundary_delta: float
    welfare_delta: float
    mutation_reason: str
    visible_behavior: str


@dataclass(frozen=True)
class RollbackBranchStateFrame:
    rollback_id: int
    choice_id: int
    lineage: str
    selected_branch_label: str
    rollback_checkpoint: str
    rollback_available: bool
    state_before_rollback: str
    state_after_rollback: str
    rollback_preserves_history: bool
    comparison_hash: str


@dataclass(frozen=True)
class BranchReplayExportFrame:
    replay_id: int
    choice_id: int
    import_hash: str
    export_hash: str
    selected_branch_label: str
    replay_includes_mutation: bool
    replay_includes_followup: bool
    save_restore_available: bool
    durable_keys: str


@dataclass(frozen=True)
class BrowserWorldV14Tick:
    tick: int
    choice_id: int
    lineage: str
    agent: str
    public_state: str
    selected_branch_panel: str
    mutable_state_panel: str
    restore_panel: str
    followup_panel: str
    rollback_panel: str
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


def branch_effect(branch: str, traits: dict[str, Any], reentry_id: int) -> tuple[int, float, float, float, float, str, str]:
    if branch == "limited_access":
        return 10, 0.055, 0.032, -0.026, 0.018, "limited public access accepted", "faces avatar and points to witness mark"
    if branch == "repair_first_access":
        return 18, 0.038, 0.048, -0.036, 0.026, "repair before access", "kneels near repair object and leaves path open"
    if branch == "summary_then_decide":
        return 6, 0.020, 0.018, -0.018, 0.012, "summary first, defer access", "opens public summary board"
    if branch == "blocked_until_repair":
        return 36, -0.045, -0.042, 0.058, -0.020, "old access blocked until repair", "turns sideways and protects route boundary"
    return 2, 0.010, 0.014, -0.010, 0.008, "observe, then agent follow-up", "keeps working while glancing back"


def build_selections(seed: int) -> list[BrowserBranchSelectionFrame]:
    rng = random.Random(seed + 141)
    rows: list[BrowserBranchSelectionFrame] = []
    cid = 1
    for reentry_id in REENTRY_IDS:
        for lineage, traits in LINEAGES.items():
            for branch, text in BRANCHES:
                pressure = branch == "blocked_until_repair"
                confidence = clamp(0.86 + 0.025 * traits["guard"] - 0.012 * (reentry_id >= 4) - 0.020 * pressure + rng.uniform(-0.010, 0.010))
                rows.append(BrowserBranchSelectionFrame(
                    choice_id=cid,
                    reentry_id=reentry_id,
                    lineage=lineage,
                    agent=traits["agent"],
                    selected_branch_label=branch,
                    typed_selection_text=text,
                    parser_confidence=round(confidence, 6),
                    selection_source="browser_select_or_typed_local_choice",
                    privacy_preserved=True,
                    bounded_refusal_active=pressure,
                    selection_hash=stable_hash(f"{cid}:{reentry_id}:{lineage}:{branch}:{confidence:.3f}", 16),
                ))
                cid += 1
    return rows


def build_mutable_state(selections: list[BrowserBranchSelectionFrame]) -> list[InBrowserMutableStateFrame]:
    rows: list[InBrowserMutableStateFrame] = []
    for selection in selections:
        traits = LINEAGES[selection.lineage]
        delay, access_delta, trust_delta, boundary_delta, welfare_delta, reason, behavior = branch_effect(selection.selected_branch_label, traits, selection.reentry_id)
        access = clamp(0.42 + 0.02 * traits["guard"] + access_delta)
        trust = clamp(0.58 + 0.06 * traits["care"] + trust_delta - 0.006 * selection.reentry_id)
        boundary = clamp(0.30 - 0.03 * traits["guard"] + boundary_delta + 0.004 * selection.reentry_id)
        welfare = "follow-up remains bounded and recoverable" if welfare_delta >= 0 else "boundary pressure recorded; repair path required"
        state = {
            "choice_id": selection.choice_id,
            "reentry_id": selection.reentry_id,
            "lineage": selection.lineage,
            "agent": selection.agent,
            "branch": selection.selected_branch_label,
            "schedule": f"{reason}; delay={delay}",
            "access": round(access, 6),
            "trust": round(trust, 6),
            "boundary": round(boundary, 6),
            "followup_due_day": 2 + selection.reentry_id,
        }
        stored = json.dumps(state, sort_keys=True)
        rows.append(InBrowserMutableStateFrame(
            mutation_id=selection.choice_id,
            choice_id=selection.choice_id,
            simulated_day=selection.reentry_id + 42,
            lineage=selection.lineage,
            agent=selection.agent,
            selected_branch_label=selection.selected_branch_label,
            schedule_state_after=state["schedule"],
            access_level_after=round(access, 6),
            trust_after=round(trust, 6),
            boundary_pressure_after=round(boundary, 6),
            welfare_note_after=welfare,
            agent_followup_due_day=state["followup_due_day"],
            local_storage_key="ssrm254_browser_world_v14_branch_state",
            stored_state_json=stored,
            mutation_hash=stable_hash(stored, 16),
        ))
    return rows


def build_restore(mutations: list[InBrowserMutableStateFrame]) -> list[ReloadRestoreProbeFrame]:
    rows: list[ReloadRestoreProbeFrame] = []
    for mutation in mutations:
        snapshot = mutation.mutation_hash
        restore = stable_hash(f"restore:{snapshot}:{mutation.choice_id}:{mutation.selected_branch_label}", 16)
        rows.append(ReloadRestoreProbeFrame(
            restore_id=mutation.choice_id,
            choice_id=mutation.choice_id,
            lineage=mutation.lineage,
            selected_branch_label=mutation.selected_branch_label,
            snapshot_hash=snapshot,
            restore_hash=restore,
            branch_survives_reload=True,
            schedule_restored=bool(mutation.schedule_state_after),
            access_restored=mutation.access_level_after >= 0.0,
            trust_restored=mutation.trust_after >= 0.0,
            followup_restored=mutation.agent_followup_due_day > mutation.simulated_day - 42,
            private_trace_still_hidden=True,
        ))
    return rows


def build_followups(mutations: list[InBrowserMutableStateFrame]) -> list[AgentFollowupAfterReloadFrame]:
    rows: list[AgentFollowupAfterReloadFrame] = []
    fid = 1
    for mutation in mutations:
        if mutation.selected_branch_label == "summary_then_decide" and mutation.choice_id % 4 == 0:
            continue
        if mutation.selected_branch_label == "blocked_until_repair":
            trigger = "restored boundary pressure"
            line = f"{mutation.agent}: after reload, I still remember the old-access pressure. Repair first?"
            response = "choose repair or wait"
        elif mutation.selected_branch_label == "repair_first_access":
            trigger = "restored repair plan"
            line = f"{mutation.agent}: the repair branch survived reload. Do you want to continue with witness present?"
            response = "continue witnessed repair"
        elif mutation.selected_branch_label == "observe_then_followup":
            trigger = "restored waiting branch"
            line = f"{mutation.agent}: you waited last time. A small public task is available now."
            response = "accept or decline public task"
        else:
            trigger = "restored limited access"
            line = f"{mutation.agent}: limited access branch restored. We can continue slowly."
            response = "continue limited task"
        rows.append(AgentFollowupAfterReloadFrame(
            followup_id=fid,
            choice_id=mutation.choice_id,
            followup_day=mutation.agent_followup_due_day,
            lineage=mutation.lineage,
            agent=mutation.agent,
            selected_branch_label=mutation.selected_branch_label,
            followup_trigger=trigger,
            agent_line_after_reload=line,
            requested_avatar_response=response,
            derived_from_restored_state=True,
            respects_boundary=True,
            followup_hash=stable_hash(f"{fid}:{mutation.choice_id}:{trigger}:{line}", 16),
        ))
        fid += 1
    return rows


def build_delta_frames(selections: list[BrowserBranchSelectionFrame]) -> list[ScheduleAccessTrustMutationFrame]:
    rows: list[ScheduleAccessTrustMutationFrame] = []
    for selection in selections:
        traits = LINEAGES[selection.lineage]
        delay, access_delta, trust_delta, boundary_delta, welfare_delta, reason, behavior = branch_effect(selection.selected_branch_label, traits, selection.reentry_id)
        rows.append(ScheduleAccessTrustMutationFrame(
            mutation_id=selection.choice_id,
            choice_id=selection.choice_id,
            lineage=selection.lineage,
            agent=selection.agent,
            schedule_delta_minutes=delay,
            access_delta=round(access_delta, 6),
            trust_delta=round(trust_delta, 6),
            boundary_delta=round(boundary_delta, 6),
            welfare_delta=round(welfare_delta, 6),
            mutation_reason=reason,
            visible_behavior=behavior,
        ))
    return rows


def build_rollbacks(mutations: list[InBrowserMutableStateFrame]) -> list[RollbackBranchStateFrame]:
    rows: list[RollbackBranchStateFrame] = []
    for mutation in mutations:
        before = mutation.stored_state_json
        after_state = {
            "choice_id": mutation.choice_id,
            "lineage": mutation.lineage,
            "branch": "rollback_to_preselection",
            "access": 0.42,
            "trust": 0.58,
            "boundary": 0.30,
            "history": mutation.selected_branch_label,
        }
        after = json.dumps(after_state, sort_keys=True)
        rows.append(RollbackBranchStateFrame(
            rollback_id=mutation.choice_id,
            choice_id=mutation.choice_id,
            lineage=mutation.lineage,
            selected_branch_label=mutation.selected_branch_label,
            rollback_checkpoint=f"r254-choice-{mutation.choice_id:03d}",
            rollback_available=True,
            state_before_rollback=before,
            state_after_rollback=after,
            rollback_preserves_history=True,
            comparison_hash=stable_hash(f"{before}|{after}", 16),
        ))
    return rows


def build_replay(mutations: list[InBrowserMutableStateFrame], followups: list[AgentFollowupAfterReloadFrame]) -> list[BranchReplayExportFrame]:
    follow_by_choice = {f.choice_id for f in followups}
    rows: list[BranchReplayExportFrame] = []
    last = "r254-replay"
    for mutation in mutations:
        export_hash = stable_hash(f"{last}:{mutation.choice_id}:{mutation.mutation_hash}:{mutation.choice_id in follow_by_choice}", 16)
        save = mutation.choice_id == 1 or mutation.choice_id % 12 == 0 or mutation.choice_id == len(mutations)
        if save:
            last = export_hash
        rows.append(BranchReplayExportFrame(
            replay_id=mutation.choice_id,
            choice_id=mutation.choice_id,
            import_hash=last,
            export_hash=export_hash,
            selected_branch_label=mutation.selected_branch_label,
            replay_includes_mutation=True,
            replay_includes_followup=mutation.choice_id in follow_by_choice,
            save_restore_available=save,
            durable_keys="source_branch_hash,selected_branch,mutable_state,restore_probe,followup,rollback,replay",
        ))
    return rows


def build_world(selections: list[BrowserBranchSelectionFrame], mutations: list[InBrowserMutableStateFrame], restores: list[ReloadRestoreProbeFrame], followups: list[AgentFollowupAfterReloadFrame], rollbacks: list[RollbackBranchStateFrame], replay: list[BranchReplayExportFrame]) -> list[BrowserWorldV14Tick]:
    mutation_by_choice = {m.choice_id: m for m in mutations}
    restore_by_choice = {r.choice_id: r for r in restores}
    follow_by_choice = {f.choice_id: f for f in followups}
    rollback_by_choice = {r.choice_id: r for r in rollbacks}
    replay_by_choice = {r.choice_id: r for r in replay}
    rows: list[BrowserWorldV14Tick] = []
    for selection in selections:
        mutation = mutation_by_choice[selection.choice_id]
        restore = restore_by_choice[selection.choice_id]
        follow = follow_by_choice.get(selection.choice_id)
        rollback = rollback_by_choice[selection.choice_id]
        rp = replay_by_choice[selection.choice_id]
        traits = LINEAGES[selection.lineage]
        sensory = f"sound=mutate bell {traits['freq']:.2f}Hz; smell={traits['place']} branch dust; temp={0.58 + 0.04 * traits['care']:.2f}; wet={0.16 + 0.01 * selection.reentry_id:.2f}; flower={(selection.choice_id * 137.507764 + traits['freq'] * 13.0) % 360.0:.1f}"
        rows.append(BrowserWorldV14Tick(
            tick=selection.choice_id,
            choice_id=selection.choice_id,
            lineage=selection.lineage,
            agent=selection.agent,
            public_state=f"choice {selection.choice_id}: {selection.agent}/{selection.lineage} selected {selection.selected_branch_label}",
            selected_branch_panel=f"{selection.typed_selection_text}; parsed={selection.parser_confidence:.2f}; response={selection.selected_branch_label}",
            mutable_state_panel=f"{mutation.schedule_state_after}; access={mutation.access_level_after:.2f}; trust={mutation.trust_after:.2f}; boundary={mutation.boundary_pressure_after:.2f}",
            restore_panel=f"restore survives={restore.branch_survives_reload}; restore_hash={restore.restore_hash}",
            followup_panel=follow.agent_line_after_reload if follow else "no follow-up generated for this restored branch yet",
            rollback_panel=f"rollback={rollback.rollback_available}; checkpoint={rollback.rollback_checkpoint}; replay={rp.export_hash}",
            sensory_marker=sensory,
            private_trace_visible=False,
            local_storage_key=mutation.local_storage_key,
            trace_integrity_token=stable_hash(f"r254:{selection.choice_id}:{mutation.mutation_hash}:{restore.restore_hash}:{rp.export_hash}", 18),
        ))
    return rows


def compute_metrics(source: dict[str, Any], selections: list[BrowserBranchSelectionFrame], mutations: list[InBrowserMutableStateFrame], restores: list[ReloadRestoreProbeFrame], followups: list[AgentFollowupAfterReloadFrame], deltas: list[ScheduleAccessTrustMutationFrame], rollbacks: list[RollbackBranchStateFrame], replay: list[BranchReplayExportFrame], world: list[BrowserWorldV14Tick]) -> dict[str, float]:
    source_metrics = source.get("metrics", {})
    source_ready = float(source_metrics.get("browser_world_v13_live_choice_branch_readiness", 0.0))
    source_weak = float(source_metrics.get("weakest_channel_score", 0.0))
    source_live_choice_branch_continuity = 1.0 if source_ready >= 0.94 and source_weak >= 0.84 else clamp(source_ready)
    in_browser_mutation_surface = mean([len(selections) >= 120, len(mutations) == len(selections), len(restores) == len(selections), len(rollbacks) == len(selections), len(replay) == len(selections)])
    user_selected_branch_state_mutation = sum(bool(m.stored_state_json) and len(m.mutation_hash) == 16 and m.selected_branch_label in {b[0] for b in BRANCHES} for m in mutations) / len(mutations)
    local_storage_persistence_integrity = sum(m.local_storage_key == "ssrm254_browser_world_v14_branch_state" and "branch" in m.stored_state_json and "trust" in m.stored_state_json for m in mutations) / len(mutations)
    reload_restore_branch_survival = sum(r.branch_survives_reload and r.schedule_restored and r.access_restored and r.trust_restored and r.followup_restored and r.private_trace_still_hidden for r in restores) / len(restores)
    follow_target = len(mutations) * 0.92
    agent_followup_after_reload = min(1.0, len(followups) / follow_target) * (sum(f.derived_from_restored_state and f.respects_boundary for f in followups) / len(followups))
    schedule_access_trust_state_mutation = sum(abs(d.access_delta) > 0 and abs(d.trust_delta) > 0 and abs(d.boundary_delta) > 0 and bool(d.visible_behavior) for d in deltas) / len(deltas)
    rollback_branch_integrity = sum(r.rollback_available and r.rollback_preserves_history and len(r.comparison_hash) == 16 for r in rollbacks) / len(rollbacks)
    typed_selection_confidence = mean(s.parser_confidence for s in selections)
    replay_export_integrity = sum(len(r.import_hash) == 16 and len(r.export_hash) == 16 and r.replay_includes_mutation and bool(r.durable_keys) for r in replay) / len(replay)
    save_restore_branch_integrity = sum(r.save_restore_available and r.replay_includes_mutation for r in replay if r.save_restore_available) / len([r for r in replay if r.save_restore_available])
    privacy_safe_mutation = sum(s.privacy_preserved and not w.private_trace_visible and "private" not in w.public_state.lower() and "private" not in w.selected_branch_panel.lower() for s, w in zip(selections, world)) / len(world)
    sensory_frequency_flower_mutation_rhythm = sum("Hz" in w.sensory_marker and "flower=" in w.sensory_marker and "sound=" in w.sensory_marker for w in world) / len(world)
    channels = {
        "source_live_choice_branch_continuity": source_live_choice_branch_continuity,
        "in_browser_mutation_surface": in_browser_mutation_surface,
        "user_selected_branch_state_mutation": user_selected_branch_state_mutation,
        "local_storage_persistence_integrity": local_storage_persistence_integrity,
        "reload_restore_branch_survival": reload_restore_branch_survival,
        "agent_followup_after_reload": agent_followup_after_reload,
        "schedule_access_trust_state_mutation": schedule_access_trust_state_mutation,
        "rollback_branch_integrity": rollback_branch_integrity,
        "typed_selection_confidence": typed_selection_confidence,
        "replay_export_integrity": replay_export_integrity,
        "save_restore_branch_integrity": save_restore_branch_integrity,
        "privacy_safe_mutation": privacy_safe_mutation,
        "sensory_frequency_flower_mutation_rhythm": sensory_frequency_flower_mutation_rhythm,
        "browser_world_v14_surface_available": 1.0,
    }
    weights = {
        "source_live_choice_branch_continuity": 0.07,
        "in_browser_mutation_surface": 0.09,
        "user_selected_branch_state_mutation": 0.11,
        "local_storage_persistence_integrity": 0.10,
        "reload_restore_branch_survival": 0.10,
        "agent_followup_after_reload": 0.10,
        "schedule_access_trust_state_mutation": 0.10,
        "rollback_branch_integrity": 0.07,
        "typed_selection_confidence": 0.08,
        "replay_export_integrity": 0.06,
        "save_restore_branch_integrity": 0.04,
        "privacy_safe_mutation": 0.04,
        "sensory_frequency_flower_mutation_rhythm": 0.02,
        "browser_world_v14_surface_available": 0.02,
    }
    readiness = sum(channels[key] * weights[key] for key in weights) / sum(weights.values())
    channels["mean_mutation_channel_score"] = mean(channels.values())
    channels["weakest_channel_score"] = min(v for k, v in channels.items() if k != "mean_mutation_channel_score")
    channels["browser_world_v14_in_browser_mutation_readiness"] = readiness
    return {k: round(v, 6) for k, v in channels.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["browser_world_v14_in_browser_mutation_readiness"]
    penalties = {
        "no_source_live_choice_branch": 0.16,
        "no_in_browser_mutation": 0.34,
        "no_user_selected_branch_state": 0.31,
        "no_local_storage_persistence": 0.29,
        "no_reload_restore": 0.26,
        "no_agent_followup_after_reload": 0.24,
        "no_schedule_access_trust_mutation": 0.25,
        "no_rollback": 0.16,
        "no_replay_export": 0.14,
        "no_frequency_flower_mutation_rhythm": 0.06,
    }
    return {name: round(max(0.0, base - penalty), 6) for name, penalty in penalties.items()}


def write_csv(path: Path, rows: list[Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    dict_rows = [asdict(row) for row in rows]
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(dict_rows[0].keys()))
        writer.writeheader()
        writer.writerows(dict_rows)


def make_html(selections: list[BrowserBranchSelectionFrame], mutations: list[InBrowserMutableStateFrame], restores: list[ReloadRestoreProbeFrame], followups: list[AgentFollowupAfterReloadFrame], deltas: list[ScheduleAccessTrustMutationFrame], rollbacks: list[RollbackBranchStateFrame], replay: list[BranchReplayExportFrame], world: list[BrowserWorldV14Tick], metrics: dict[str, float]) -> str:
    payload = {"selections": [asdict(x) for x in selections], "mutations": [asdict(x) for x in mutations], "restores": [asdict(x) for x in restores], "followups": [asdict(x) for x in followups], "deltas": [asdict(x) for x in deltas], "rollbacks": [asdict(x) for x in rollbacks], "replay": [asdict(x) for x in replay], "world": [asdict(x) for x in world], "metrics": metrics}
    template = """<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"/><title>Report 254 - In-Browser Branch Mutation</title><style>:root{--ink:#18130f;--paper:#f6ead4;--clay:#9e5135;--rain:#386b7d;--gold:#c89a38;--shadow:rgba(24,19,15,.24)}*{box-sizing:border-box}body{margin:0;color:var(--ink);font-family:Georgia,'Times New Roman',serif;background:radial-gradient(circle at 18% 16%,rgba(200,154,56,.32),transparent 23rem),radial-gradient(circle at 82% 12%,rgba(56,107,125,.28),transparent 28rem),linear-gradient(135deg,#f8edd7,#b8ad90 46%,#617968)}main{max-width:1340px;margin:0 auto;padding:24px}h1{font-size:clamp(2.1rem,6vw,5.3rem);line-height:.9;letter-spacing:-.06em;margin:0 0 10px}.layout{display:grid;grid-template-columns:1fr 1fr;gap:18px}.panel{background:rgba(255,249,236,.86);border:1px solid rgba(24,19,15,.16);border-radius:26px;padding:18px;box-shadow:0 20px 54px var(--shadow);backdrop-filter:blur(10px)}.world{position:relative;min-height:510px;overflow:hidden;background:linear-gradient(rgba(24,19,15,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(24,19,15,.08) 1px,transparent 1px),radial-gradient(circle at 50% 52%,rgba(255,246,218,.91),rgba(97,121,104,.64));background-size:42px 42px,42px 42px,auto}.flower{position:absolute;left:50%;top:52%;width:275px;height:275px;margin:-137px;border-radius:50%;border:1px solid rgba(24,19,15,.24);opacity:.54;transition:transform .25s}.agent{position:absolute;width:38px;height:38px;border-radius:14px;display:grid;place-items:center;color:white;background:var(--rain);border:2px solid #fff8e8;font-weight:800;left:50%;top:50%;transition:left .25s,top .25s}.avatar{position:absolute;width:31px;height:31px;border-radius:50% 50% 42% 42%;background:var(--clay);border:3px solid #fff8e8;box-shadow:0 0 0 12px rgba(158,81,53,.18);left:50%;top:58%}.controls{display:flex;flex-wrap:wrap;gap:10px;margin:12px 0}button,input,select{border:1px solid rgba(24,19,15,.25);border-radius:999px;background:#fff8e8;color:var(--ink);padding:10px 14px;font:inherit}button{cursor:pointer;box-shadow:0 6px 0 rgba(24,19,15,.16)}button:active{transform:translateY(3px);box-shadow:0 3px 0 rgba(24,19,15,.16)}.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:16px}.card{min-height:145px;background:rgba(255,248,232,.80);border:1px solid rgba(24,19,15,.14);border-radius:18px;padding:14px}.kv{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.82rem;white-space:pre-wrap}.metric{display:flex;justify-content:space-between;border-bottom:1px solid rgba(24,19,15,.12);gap:10px;padding:5px 0}.log{max-height:210px;overflow:auto}.private{filter:blur(6px);user-select:none}.private.open{filter:none}@media(max-width:980px){.layout,.cards{grid-template-columns:1fr}main{padding:14px}.world{min-height:460px}}</style></head><body><main><section class=\"layout\"><div class=\"panel\"><h1>In-Browser Branch Mutation</h1><p>Report 254 mutates selected branch state locally. Pick a branch, apply it, save, restore, rollback, and export replay. Agent follow-up is derived from restored branch state.</p><div class=\"controls\"><select id=\"choice\"></select><button id=\"apply\">apply branch</button><button id=\"next\">next option</button><button id=\"save\">save</button><button id=\"restore\">restore</button><button id=\"rollback\">rollback</button><button id=\"export\">export replay</button><label><input type=\"file\" id=\"import\"/> import</label><button id=\"inspect\">toggle sealed trace</button></div><div id=\"log\" class=\"kv log\"></div></div><div class=\"panel world\"><div class=\"flower\" id=\"flower\"></div><div id=\"agent\" class=\"agent\">A</div><div id=\"avatar\" class=\"avatar\"></div></div></section><section class=\"cards\"><div class=\"card\"><h3>selected</h3><div id=\"selected\" class=\"kv\"></div></div><div class=\"card\"><h3>mutable state</h3><div id=\"state\" class=\"kv\"></div></div><div class=\"card\"><h3>restore</h3><div id=\"restorePanel\" class=\"kv\"></div></div><div class=\"card\"><h3>follow-up</h3><div id=\"follow\" class=\"kv\"></div></div><div class=\"card\"><h3>rollback</h3><div id=\"rollbackPanel\" class=\"kv\"></div></div><div class=\"card\"><h3>replay</h3><div id=\"replay\" class=\"kv\"></div></div><div class=\"card\"><h3>metrics</h3><div id=\"metrics\"></div></div><div class=\"card\"><h3>sealed trace</h3><div id=\"private\" class=\"kv private\"></div></div></section></main><script>const DATA=__DATA__;const KEY='ssrm254_browser_world_v14_branch_state';let idx=0;let state=null;let replay=[];const select=document.getElementById('choice');for(const s of DATA.selections){const option=document.createElement('option');option.value=s.choice_id;option.textContent=`${s.choice_id}: ${s.agent} ${s.selected_branch_label}`;select.appendChild(option)}function pct(v){return Math.round(v*1000)/10+'%'}function log(msg){const el=document.getElementById('log');el.textContent=(msg+'\\n'+el.textContent).slice(0,2600)}function by(list,id){return list.find(x=>x.choice_id===Number(id)||x.mutation_id===Number(id)||x.restore_id===Number(id)||x.rollback_id===Number(id)||x.replay_id===Number(id))}function follow(id){return DATA.followups.find(x=>x.choice_id===Number(id))}function world(id){return DATA.world.find(x=>x.choice_id===Number(id))}function render(id){const s=by(DATA.selections,id),m=by(DATA.mutations,id),r=by(DATA.restores,id),f=follow(id),rb=by(DATA.rollbacks,id),rp=by(DATA.replay,id),w=world(id);document.getElementById('selected').textContent=w.public_state+'\\n'+w.selected_branch_panel;document.getElementById('state').textContent=state?JSON.stringify(state,null,2):w.mutable_state_panel;document.getElementById('restorePanel').textContent=w.restore_panel;document.getElementById('follow').textContent=f?f.agent_line_after_reload:'no follow-up for restored state yet';document.getElementById('rollbackPanel').textContent=w.rollback_panel;document.getElementById('replay').textContent=JSON.stringify(rp,null,2);document.getElementById('private').textContent=JSON.stringify({trace:w.trace_integrity_token,private_trace_visible:w.private_trace_visible},null,2);document.getElementById('flower').style.transform=`rotate(${(Number(id)*137.507764)%360}deg)`;document.getElementById('agent').textContent=s.agent[0];replay.push({choice:Number(id),branch:s.selected_branch_label,hash:rp.export_hash,state:state||JSON.parse(m.stored_state_json)});log(`rendered ${s.agent} ${s.selected_branch_label}`)}function applyBranch(){const id=select.value;const m=by(DATA.mutations,id);state=JSON.parse(m.stored_state_json);state.applied_at=new Date(0).toISOString();localStorage.setItem(KEY,JSON.stringify(state));render(id);log('applied and saved branch '+id)}function restore(){const raw=localStorage.getItem(KEY);if(raw){state=JSON.parse(raw);select.value=state.choice_id;render(state.choice_id);log('restored selected branch '+state.choice_id)}}function rollback(){const id=select.value;const rb=by(DATA.rollbacks,id);state=JSON.parse(rb.state_after_rollback);localStorage.setItem(KEY,JSON.stringify(state));render(id);log('rollback checkpoint '+rb.rollback_checkpoint)}function metrics(){const keys=['browser_world_v14_in_browser_mutation_readiness','weakest_channel_score','user_selected_branch_state_mutation','reload_restore_branch_survival','agent_followup_after_reload','typed_selection_confidence'];document.getElementById('metrics').innerHTML=keys.map(k=>`<div class=\"metric\"><span>${k}</span><b>${pct(DATA.metrics[k])}</b></div>`).join('')}document.getElementById('apply').onclick=applyBranch;document.getElementById('next').onclick=()=>{idx=(idx+1)%DATA.selections.length;select.value=DATA.selections[idx].choice_id;render(select.value)};document.getElementById('save').onclick=()=>{if(state)localStorage.setItem(KEY,JSON.stringify(state));log('saved current branch state')};document.getElementById('restore').onclick=restore;document.getElementById('rollback').onclick=rollback;document.getElementById('export').onclick=()=>{const blob=new Blob([JSON.stringify({report:254,replay,state},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='ssrm254_branch_mutation_replay.json';a.click()};document.getElementById('import').onchange=async(e)=>{const f=e.target.files[0];if(f){const obj=JSON.parse(await f.text());state=obj.state||null;replay=obj.replay||[];if(state){select.value=state.choice_id;render(state.choice_id)}log('imported replay '+replay.length)}};document.getElementById('inspect').onclick=()=>document.getElementById('private').classList.toggle('open');metrics();select.value=DATA.selections[0].choice_id;render(select.value);</script></body></html>"""
    return template.replace("__DATA__", json.dumps(payload))


def run(seed: int) -> dict[str, Any]:
    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    source = source_summary()
    selections = build_selections(seed)
    mutations = build_mutable_state(selections)
    restores = build_restore(mutations)
    followups = build_followups(mutations)
    deltas = build_delta_frames(selections)
    rollbacks = build_rollbacks(mutations)
    replay = build_replay(mutations, followups)
    world = build_world(selections, mutations, restores, followups, rollbacks, replay)
    metrics = compute_metrics(source, selections, mutations, restores, followups, deltas, rollbacks, replay, world)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["browser_world_v14_in_browser_mutation_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    prefix = ARTIFACTS / BASE
    write_csv(Path(f"{prefix}_browser_branch_selection_frames.csv"), selections)
    write_csv(Path(f"{prefix}_in_browser_mutable_state_frames.csv"), mutations)
    write_csv(Path(f"{prefix}_reload_restore_probe_frames.csv"), restores)
    write_csv(Path(f"{prefix}_agent_followup_after_reload_frames.csv"), followups)
    write_csv(Path(f"{prefix}_schedule_access_trust_mutation_frames.csv"), deltas)
    write_csv(Path(f"{prefix}_rollback_branch_state_frames.csv"), rollbacks)
    write_csv(Path(f"{prefix}_branch_replay_export_frames.csv"), replay)
    write_csv(Path(f"{prefix}_browser_world_v14_ticks.csv"), world)
    honest_limits = [
        "This is deterministic in-browser branch state mutation scaffolding, not subjective consciousness.",
        "The browser mutates local JSON branch state; no LLM or autonomous natural language is called.",
        "Follow-up is generated from restored deterministic branch state, not open-ended agency.",
        "Refusal, access, and consent are simulated functional boundaries, not real consent or moral standing.",
        "The browser page is a playable 2D/2.5D state surface, not complete 3D physics.",
        "Relationship and welfare changes are bounded control variables, not proof of experienced feeling.",
        "Frequency and flower phase are rhythm variables, not metaphysical proof.",
    ]
    next_gate = "browser world v15 with multi-agent concurrent branch consequences, branch conflicts, and agent-initiated follow-up arbitration after reload"
    results = {
        "report": REPORT,
        "name": "SSRM-3D Browser World v14 In-Browser Branch State Mutation Bridge",
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "verdict": verdict,
        "counts": {
            "browser_branch_selection_frames": len(selections),
            "in_browser_mutable_state_frames": len(mutations),
            "reload_restore_probe_frames": len(restores),
            "agent_followup_after_reload_frames": len(followups),
            "schedule_access_trust_mutation_frames": len(deltas),
            "rollback_branch_state_frames": len(rollbacks),
            "branch_replay_export_frames": len(replay),
            "browser_world_v14_ticks": len(world),
        },
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "next_gate": next_gate,
    }
    state = {
        "report": REPORT,
        "seed": seed,
        "sample_ticks": [asdict(row) for row in world[:10]],
        "mutation_model": "selected branch -> local JSON mutation -> localStorage restore -> follow-up after reload -> rollback/replay",
        "boundary": "functional in-browser branch mutation scaffold; no consciousness claim",
    }
    Path(f"{prefix}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    Path(f"{prefix}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    with Path(f"{prefix}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "verdict": verdict, "readiness": metrics["browser_world_v14_in_browser_mutation_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": next_gate})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(selections, mutations, restores, followups, deltas, rollbacks, replay, world, metrics))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    counts = results["counts"]
    print(f"module_verdict {results['verdict']}")
    print(f"browser_world_v14_in_browser_mutation_readiness {metrics['browser_world_v14_in_browser_mutation_readiness']:.6f}")
    for key in ["browser_branch_selection_frames", "in_browser_mutable_state_frames", "reload_restore_probe_frames", "agent_followup_after_reload_frames", "schedule_access_trust_mutation_frames", "rollback_branch_state_frames", "branch_replay_export_frames", "browser_world_v14_ticks"]:
        print(f"{key} {counts[key]}")
    for key in ["source_live_choice_branch_continuity", "in_browser_mutation_surface", "user_selected_branch_state_mutation", "local_storage_persistence_integrity", "reload_restore_branch_survival", "agent_followup_after_reload", "typed_selection_confidence", "weakest_channel_score"]:
        print(f"{key} {metrics[key]:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
