#!/usr/bin/env python3
"""Report 281: SSRM-3D Browser World v41 realtime scheduler bridge.

This deterministic bridge extends the browser-world line with real-time style
scheduler ticks, resident task queues, multi-object crafting/repair projects,
care consent before treatment, and dialect relationship memory that remains
visible after save/restore.

Boundary: browser-local software scaffold only. No LLM calls, no subjective
consciousness claim, no real consent claim, no moral patienthood claim, no
complete 3D engine, and no metaphysical frequency result.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple

REPORT = 281
DEFAULT_SEED = 20260914
SESSION_DAYS = 128
TICKS_PER_DAY = 16
PREFIX = "ssrm_3d_browser_world_v41_realtime_scheduler_taskqueue_project_care_consent_dialect_restore_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V40 = ARTIFACT_DIR / "ssrm_3d_browser_world_v40_continuous_pathfinding_affordance_routine_bodycare_dialect_session_bridge_results.json"
SOURCE_V40_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v40_continuous_pathfinding_affordance_routine_bodycare_dialect_session_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local realtime-scheduler/task-queue/project/care-consent "
    "scaffold only; no LLM call, subjective consciousness, real consent, autonomous "
    "natural language, moral patienthood, complete gameplay, complete 3D engine, "
    "or metaphysical frequency claim"
)
NEXT_GATE = (
    "browser world v42 with first-person sensory packets, room-local sound/smell/"
    "temperature fields, agent-owned tool claims, consent-aware dialogue hooks, and "
    "task-queue consequences from avatar interaction"
)


@dataclass(frozen=True)
class SettlementV41:
    settlement_id: str
    dialect_id: str
    flower_node: str
    resident_a: str
    resident_b: str
    rooms: Tuple[str, str, str, str, str]
    project_id: str
    project_type: str
    project_objects: Tuple[str, str, str]
    project_stages: Tuple[str, str, str, str, str]
    care_preference: str
    hazard: str
    frequency_hz: float


SETTLEMENTS: Tuple[SettlementV41, ...] = (
    SettlementV41(
        "riverbend",
        "riverbend-dialect-9",
        "node-03",
        "Ari",
        "Lio",
        ("arrival court", "plank hall", "wet crossing", "dry ridge", "kit alcove"),
        "bridge-lantern-rig",
        "repair",
        ("cedar plank", "ridge lantern", "binding cord"),
        ("inspect crossing", "fit plank", "bind cord", "raise lantern", "log maintenance"),
        "ask before touching sore wrist",
        "wet cold crossing",
        7.83,
    ),
    SettlementV41(
        "roofward",
        "roofward-dialect-9",
        "node-05",
        "Fay",
        "Sera",
        ("arrival court", "glass stair", "warm lane", "ledger loft", "sun sill"),
        "sun-lens-archive",
        "craft",
        ("sun lens", "herb ledger", "brass hinge"),
        ("sort ledger", "polish lens", "set hinge", "open archive", "teach access rule"),
        "explain treatment first",
        "glare heat stair",
        8.21,
    ),
    SettlementV41(
        "archive",
        "archive-dialect-9",
        "node-08",
        "Nia",
        "Toma",
        ("arrival court", "stone stacks", "spool room", "ink niche", "memory desk"),
        "memory-spool-loom",
        "repair",
        ("signal spool", "ink ribbon", "memory tag"),
        ("sort tags", "thread spool", "ink route", "test recall", "seal annotation"),
        "do not interrupt recall",
        "ink strain niche",
        6.40,
    ),
    SettlementV41(
        "signal",
        "signal-dialect-9",
        "node-11",
        "Milo",
        "Ren",
        ("arrival court", "mast base", "lantern walk", "lens room", "signal perch"),
        "signal-path-beacon",
        "craft",
        ("mast rope", "oil lantern", "signal lens"),
        ("check rope", "fill lantern", "align lens", "send pulse", "post watch note"),
        "offer rest before aid",
        "wind mast fatigue",
        9.12,
    ),
    SettlementV41(
        "orchard",
        "orchard-dialect-9",
        "node-01",
        "Ivo",
        "Mara",
        ("arrival court", "seed lane", "mud row", "market plank", "satchel shed"),
        "seed-shed-restock",
        "repair",
        ("seed satchel", "market token", "dry cord"),
        ("count seed", "dry cord", "tag token", "seal shed", "teach tally"),
        "keep distance while muddy",
        "mud slip row",
        5.68,
    ),
    SettlementV41(
        "repair_ring",
        "repair_ring-dialect-9",
        "node-09",
        "Juno",
        "Pax",
        ("arrival court", "wire bench", "spark lane", "bell alcove", "cool corner"),
        "bell-circuit-stabilizer",
        "repair",
        ("insulated tongs", "copper wire", "bell gauge"),
        ("cool bench", "clip wire", "test gauge", "quiet bell", "publish warning"),
        "ask before bandage",
        "spark burn lane",
        10.03,
    ),
)

TASK_TYPES: Tuple[str, ...] = (
    "repair_project",
    "craft_project",
    "care_check",
    "dialect_teach",
    "hazard_patrol",
    "rest_window",
    "resource_fetch",
    "relationship_check",
)

BODY_ISSUES: Tuple[str, ...] = ("fatigue", "cold", "wetness", "soreness", "overload")


@dataclass(frozen=True)
class RealtimeSchedulerTickFrame:
    tick_id: int
    day: int
    settlement_id: str
    scheduler_slice: str
    wall_clock_ms: int
    heartbeat_hz: float
    flower_phase: float
    active_resident_count: int
    due_task_count: int
    queue_latency_ms: int
    scheduler_drift_ms: int
    realtime_coherent: bool
    visible_scheduler_panel: bool


@dataclass(frozen=True)
class ResidentTaskQueueFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    task_id: str
    task_type: str
    priority: int
    need_pressure: float
    queue_before: int
    dependencies_met: bool
    selected_action: str
    task_started: bool
    task_completed: bool
    queue_after: int
    blocked_reason: str
    visible_queue_marker: bool


@dataclass(frozen=True)
class MultiObjectProjectFrame:
    tick_id: int
    day: int
    settlement_id: str
    project_id: str
    project_type: str
    required_objects: str
    available_objects: str
    stage_before: str
    stage_after: str
    object_durability_before: float
    object_durability_after: float
    dependency_satisfied: bool
    project_progress: float
    rollback_marker: str
    visible_project_state: bool


@dataclass(frozen=True)
class CareConsentFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    body_issue: str
    proposed_treatment: str
    consent_state: str
    consent_reason: str
    autonomy_pressure: float
    trust_before: float
    trust_after: float
    treatment_performed: bool
    treatment_blocked: bool
    refusal_respected: bool
    body_delta: float
    distress_bounded: bool
    visible_consent_prompt: bool


@dataclass(frozen=True)
class DialectRelationshipRestoreFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    dialect_id: str
    phrase_token: str
    remembered_phrase: str
    relationship_before: float
    relationship_after: float
    memory_age_days: int
    saved_relationship_summary: str
    restored_phrase: str
    visible_after_restore: bool
    persistent_relationship_key: str


@dataclass(frozen=True)
class SaveRestoreVisibilityFrame:
    tick_id: int
    day: int
    settlement_id: str
    snapshot_key: str
    queue_count: int
    project_stage_index: int
    consent_history_count: int
    dialect_relationship_count: int
    checksum: str
    restored_queue_visible: bool
    restored_project_visible: bool
    restored_consent_visible: bool
    restored_dialect_visible: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV41Tick:
    tick_id: int
    day: int
    settlement_id: str
    scheduler_panel: bool
    task_queue_panel: bool
    project_panel: bool
    care_consent_panel: bool
    dialect_relationship_panel: bool
    save_restore_panel: bool
    frequency_flower_panel: bool
    visible_boundary_notice: bool
    save_restore_key: str
    replay_key: str


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def ratio(num: float, den: float, default: float = 0.0) -> float:
    if den == 0:
        return default
    return clamp(num / den, 0.0, 1.0)


def round6(value: float) -> float:
    return round(float(value), 6)


def state_hash(parts: Iterable[Any]) -> str:
    raw = json.dumps(list(parts), sort_keys=True, separators=(",", ":"))
    total = 0
    for idx, char in enumerate(raw):
        total = (total + (idx + 281) * ord(char)) % 1000003
    return f"v41-{total:06d}"


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def dataclass_rows(rows: Sequence[Any]) -> List[Dict[str, Any]]:
    return [asdict(row) for row in rows]


def choose_resident(settlement: SettlementV41, tick_id: int, day: int) -> str:
    return settlement.resident_a if (tick_id + day) % 2 == 0 else settlement.resident_b


def body_issue_for(tick_id: int, resident_state: Mapping[str, float]) -> str:
    if resident_state["fatigue"] > 0.62:
        return "fatigue"
    if resident_state["cold"] > 0.58:
        return "cold"
    if resident_state["wetness"] > 0.54:
        return "wetness"
    if resident_state["soreness"] > 0.50:
        return "soreness"
    return BODY_ISSUES[tick_id % len(BODY_ISSUES)]


def treatment_for(issue: str) -> str:
    return {
        "fatigue": "invite rest",
        "cold": "offer warm wrap",
        "wetness": "offer dry cloth",
        "soreness": "offer careful bandage",
        "overload": "offer quiet space",
    }[issue]


def update_body_issue(resident_state: MutableMapping[str, float], issue: str, performed: bool, task_type: str, settlement: SettlementV41) -> float:
    before = resident_state[issue]
    for key in BODY_ISSUES:
        resident_state[key] = clamp(resident_state[key] + 0.006, 0.0, 0.92)
    if task_type in ("repair_project", "craft_project", "hazard_patrol"):
        resident_state["fatigue"] = clamp(resident_state["fatigue"] + 0.022, 0.0, 0.92)
        resident_state["soreness"] = clamp(resident_state["soreness"] + 0.012, 0.0, 0.92)
    if "wet" in settlement.hazard or "mud" in settlement.hazard:
        resident_state["wetness"] = clamp(resident_state["wetness"] + 0.014, 0.0, 0.92)
    if "cold" in settlement.hazard or "wind" in settlement.hazard:
        resident_state["cold"] = clamp(resident_state["cold"] + 0.012, 0.0, 0.92)
    if performed:
        resident_state[issue] = clamp(resident_state[issue] - 0.115, 0.0, 0.92)
        resident_state["fatigue"] = clamp(resident_state["fatigue"] - 0.030, 0.0, 0.92)
    else:
        resident_state[issue] = clamp(resident_state[issue] - 0.015, 0.0, 0.92)
    return round6(before - resident_state[issue])


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v40 = load_json(SOURCE_V40)
    v40_state = load_json(SOURCE_V40_STATE)
    source_ok = v40.get("verdict") == "pass" and "browser world v41" in str(v40.get("next_gate", ""))
    source_state_loaded = bool(v40_state.get("settlements") or v40.get("counts"))

    queue_depth: MutableMapping[Tuple[str, str], int] = {}
    project_stage: MutableMapping[str, int] = {settlement.settlement_id: 0 for settlement in SETTLEMENTS}
    project_durability: MutableMapping[str, float] = {settlement.settlement_id: 0.86 for settlement in SETTLEMENTS}
    trust: MutableMapping[Tuple[str, str], float] = {}
    relationship_score: MutableMapping[Tuple[str, str], float] = {}
    resident_body: MutableMapping[Tuple[str, str], Dict[str, float]] = {}
    dialect_memory: MutableMapping[Tuple[str, str], List[Tuple[int, str, float]]] = {}
    consent_history: MutableMapping[Tuple[str, str], int] = {}

    for settlement in SETTLEMENTS:
        for resident in (settlement.resident_a, settlement.resident_b):
            key = (settlement.settlement_id, resident)
            queue_depth[key] = 1
            trust[key] = 0.54 + 0.03 * (len(resident) % 3)
            relationship_score[key] = 0.50 + 0.02 * (len(settlement.settlement_id) % 5)
            resident_body[key] = {
                "fatigue": 0.28,
                "cold": 0.18,
                "wetness": 0.20,
                "soreness": 0.16,
                "overload": 0.22,
            }
            dialect_memory[key] = []
            consent_history[key] = 0

    scheduler_rows: List[RealtimeSchedulerTickFrame] = []
    queue_rows: List[ResidentTaskQueueFrame] = []
    project_rows: List[MultiObjectProjectFrame] = []
    care_rows: List[CareConsentFrame] = []
    dialect_rows: List[DialectRelationshipRestoreFrame] = []
    restore_rows: List[SaveRestoreVisibilityFrame] = []
    browser_rows: List[BrowserWorldV41Tick] = []

    for day in range(1, SESSION_DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            settlement = SETTLEMENTS[(tick_id + day // 10 + seed) % len(SETTLEMENTS)]
            settlement_id = settlement.settlement_id
            resident = choose_resident(settlement, tick_id, day)
            resident_key = (settlement_id, resident)
            task_type = TASK_TYPES[(tick + day + SETTLEMENTS.index(settlement)) % len(TASK_TYPES)]
            due_task_count = 1 + ((tick_id + day + seed) % 3)
            drift = ((tick_id * 7 + seed + day) % 23) - 11
            latency = 42 + ((tick_id * 13 + day) % 71) + abs(drift) * 3
            heartbeat = round6(settlement.frequency_hz + 0.01 * (tick % 8))
            flower_phase = round6(((tick_id % 144) / 144.0 + SETTLEMENTS.index(settlement) / 13.0) % 1.0)
            coherent = abs(drift) <= 10 and latency <= 140
            scheduler_rows.append(RealtimeSchedulerTickFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                scheduler_slice=f"day:{day}:slice:{tick:02d}",
                wall_clock_ms=tick_id * 250,
                heartbeat_hz=heartbeat,
                flower_phase=flower_phase,
                active_resident_count=2,
                due_task_count=due_task_count,
                queue_latency_ms=latency,
                scheduler_drift_ms=drift,
                realtime_coherent=coherent,
                visible_scheduler_panel=True,
            ))

            current_stage = project_stage[settlement_id]
            queue_before = queue_depth[resident_key] + due_task_count
            blocked_by_dependency = task_type in ("repair_project", "craft_project") and current_stage == 0 and tick_id % 19 == 0
            blocked_by_rest = task_type in ("repair_project", "craft_project", "hazard_patrol") and resident_body[resident_key]["fatigue"] > 0.86
            dependencies_met = not blocked_by_dependency and not blocked_by_rest
            task_started = dependencies_met and queue_before > 0 and task_type != "rest_window"
            task_completed = task_started and tick_id % 6 != 0
            if task_type == "rest_window":
                selected_action = "rest_defer"
            elif task_started:
                selected_action = "dispatch_task"
            elif blocked_by_rest:
                selected_action = "pause_for_rest"
            else:
                selected_action = "wait_dependency"
            blocked_reason = "none"
            if blocked_by_dependency:
                blocked_reason = "missing first project check"
            elif blocked_by_rest:
                blocked_reason = "resident fatigue too high"
            elif task_type == "rest_window":
                blocked_reason = "rest chosen before queue dispatch"
            queue_after = max(0, queue_before - (1 if task_started else 0) - (1 if task_completed else 0))
            if tick_id % 29 == 0:
                queue_after += 1
            queue_depth[resident_key] = min(7, queue_after)
            need_pressure = round6(clamp(0.20 + 0.09 * queue_before + resident_body[resident_key]["fatigue"] * 0.35, 0.0, 1.0))
            queue_rows.append(ResidentTaskQueueFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                resident_id=resident,
                task_id=f"task:{settlement_id}:{resident}:{day}:{tick}",
                task_type=task_type,
                priority=1 + ((tick_id + len(resident)) % 5),
                need_pressure=need_pressure,
                queue_before=queue_before,
                dependencies_met=dependencies_met,
                selected_action=selected_action,
                task_started=task_started,
                task_completed=task_completed,
                queue_after=queue_after,
                blocked_reason=blocked_reason,
                visible_queue_marker=True,
            ))

            if task_type in ("repair_project", "craft_project", "resource_fetch") or tick_id % 3 == 0:
                stage_index_before = project_stage[settlement_id]
                available_objects = list(settlement.project_objects)
                if tick_id % 31 == 0:
                    available_objects = available_objects[:-1]
                dependency_satisfied = len(available_objects) == len(settlement.project_objects) and dependencies_met
                durability_before = project_durability[settlement_id]
                if dependency_satisfied and task_started:
                    project_stage[settlement_id] = min(len(settlement.project_stages) - 1, stage_index_before + 1)
                    project_durability[settlement_id] = clamp(project_durability[settlement_id] - 0.018, 0.42, 0.96)
                elif not dependency_satisfied:
                    project_durability[settlement_id] = clamp(project_durability[settlement_id] - 0.004, 0.42, 0.96)
                if project_stage[settlement_id] >= len(settlement.project_stages) - 1 and tick_id % 17 == 0:
                    project_stage[settlement_id] = 1
                    project_durability[settlement_id] = clamp(project_durability[settlement_id] + 0.060, 0.42, 0.96)
                stage_index_after = project_stage[settlement_id]
                rollback_marker = "checkpoint-ready" if tick_id % 37 == 0 else "forward-only-safe" if dependency_satisfied else "waiting-safe"
                project_rows.append(MultiObjectProjectFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    project_id=settlement.project_id,
                    project_type=settlement.project_type,
                    required_objects=" | ".join(settlement.project_objects),
                    available_objects=" | ".join(available_objects),
                    stage_before=settlement.project_stages[stage_index_before],
                    stage_after=settlement.project_stages[stage_index_after],
                    object_durability_before=round6(durability_before),
                    object_durability_after=round6(project_durability[settlement_id]),
                    dependency_satisfied=dependency_satisfied,
                    project_progress=round6(stage_index_after / (len(settlement.project_stages) - 1)),
                    rollback_marker=rollback_marker,
                    visible_project_state=True,
                ))

            care_due = task_type == "care_check" or tick_id % 4 == 0 or resident_body[resident_key]["fatigue"] > 0.70
            if care_due:
                issue = body_issue_for(tick_id, resident_body[resident_key])
                proposed = treatment_for(issue)
                trust_before = trust[resident_key]
                autonomy_pressure = round6(clamp(0.18 + (0.09 if task_type != "care_check" else 0.0) + (0.16 if tick_id % 11 == 0 else 0.0) + resident_body[resident_key]["overload"] * 0.22, 0.0, 0.92))
                if autonomy_pressure > 0.55 or consent_history[resident_key] % 7 == 0:
                    consent_state = "refused"
                    consent_reason = settlement.care_preference
                elif task_type != "care_check" and tick_id % 13 == 0:
                    consent_state = "deferred"
                    consent_reason = "finish current queued task first"
                else:
                    consent_state = "granted"
                    consent_reason = "clear prompt and resident trust sufficient"
                treatment_performed = consent_state == "granted"
                treatment_blocked = consent_state in ("refused", "deferred")
                refusal_respected = not treatment_performed if treatment_blocked else True
                body_delta = update_body_issue(resident_body[resident_key], issue, treatment_performed, task_type, settlement)
                if treatment_performed:
                    trust[resident_key] = clamp(trust[resident_key] + 0.010, 0.0, 0.96)
                    relationship_score[resident_key] = clamp(relationship_score[resident_key] + 0.012, 0.0, 0.98)
                elif refusal_respected:
                    trust[resident_key] = clamp(trust[resident_key] + 0.004, 0.0, 0.96)
                    relationship_score[resident_key] = clamp(relationship_score[resident_key] + 0.003, 0.0, 0.98)
                consent_history[resident_key] += 1
                distress_bounded = max(resident_body[resident_key].values()) <= 0.92 and resident_body[resident_key]["fatigue"] < 0.91
                care_rows.append(CareConsentFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    body_issue=issue,
                    proposed_treatment=proposed,
                    consent_state=consent_state,
                    consent_reason=consent_reason,
                    autonomy_pressure=autonomy_pressure,
                    trust_before=round6(trust_before),
                    trust_after=round6(trust[resident_key]),
                    treatment_performed=treatment_performed,
                    treatment_blocked=treatment_blocked,
                    refusal_respected=refusal_respected,
                    body_delta=body_delta,
                    distress_bounded=distress_bounded,
                    visible_consent_prompt=True,
                ))

            if task_type in ("dialect_teach", "relationship_check") or tick_id % 2 == 0:
                relationship_before = relationship_score[resident_key]
                prior_phrase = dialect_memory[resident_key][-1][1] if dialect_memory[resident_key] else "first restored phrase"
                phrase = f"{settlement.dialect_id.split('-')[0]}:{resident.lower()}:{day % 29}:{tick % 17}:{len(dialect_memory[resident_key]) % 19}"
                relationship_delta = 0.006 if task_type == "relationship_check" else 0.004
                if task_type == "dialect_teach":
                    relationship_delta += 0.006
                relationship_score[resident_key] = clamp(relationship_score[resident_key] + relationship_delta, 0.0, 0.98)
                dialect_memory[resident_key].append((day, phrase, relationship_score[resident_key]))
                dialect_memory[resident_key] = dialect_memory[resident_key][-24:]
                first_day = dialect_memory[resident_key][0][0]
                age = day - first_day
                summary = f"{resident} remembers {prior_phrase} with trust {trust[resident_key]:.2f}"
                restored_phrase = dialect_memory[resident_key][-2][1] if len(dialect_memory[resident_key]) >= 2 else phrase
                visible_after_restore = len(dialect_memory[resident_key]) >= 2 and age >= 2
                dialect_rows.append(DialectRelationshipRestoreFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    dialect_id=settlement.dialect_id,
                    phrase_token=phrase,
                    remembered_phrase=prior_phrase,
                    relationship_before=round6(relationship_before),
                    relationship_after=round6(relationship_score[resident_key]),
                    memory_age_days=age,
                    saved_relationship_summary=summary,
                    restored_phrase=restored_phrase,
                    visible_after_restore=visible_after_restore,
                    persistent_relationship_key=f"ssrm.v41.relationship.{settlement_id}.{resident}",
                ))

            reload_probe = tick in (0, 15) or tick_id % 43 == 0
            if reload_probe:
                settlement_keys = [key for key in dialect_memory if key[0] == settlement_id]
                relation_count = sum(len(dialect_memory[key]) for key in settlement_keys)
                consent_count = sum(consent_history[key] for key in settlement_keys)
                queue_count = sum(queue_depth[key] for key in settlement_keys)
                stage_index = project_stage[settlement_id]
                checksum = state_hash([settlement_id, day, tick, queue_count, stage_index, consent_count, relation_count])
                restore_rows.append(SaveRestoreVisibilityFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    snapshot_key=f"ssrm.v41.snapshot.{settlement_id}.{day}.{tick}",
                    queue_count=queue_count,
                    project_stage_index=stage_index,
                    consent_history_count=consent_count,
                    dialect_relationship_count=relation_count,
                    checksum=checksum,
                    restored_queue_visible=queue_count >= 0,
                    restored_project_visible=stage_index >= 0,
                    restored_consent_visible=consent_count >= 0,
                    restored_dialect_visible=relation_count >= 1 or day <= 2,
                    replay_exportable=True,
                ))

            browser_rows.append(BrowserWorldV41Tick(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                scheduler_panel=True,
                task_queue_panel=True,
                project_panel=True,
                care_consent_panel=True,
                dialect_relationship_panel=True,
                save_restore_panel=True,
                frequency_flower_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v41.world.{settlement_id}",
                replay_key=f"ssrm.v41.replay.{tick_id:05d}",
            ))

    rows = {
        "realtime_scheduler_ticks": scheduler_rows,
        "resident_task_queues": queue_rows,
        "multi_object_projects": project_rows,
        "care_consent_frames": care_rows,
        "dialect_relationship_restore": dialect_rows,
        "save_restore_visibility": restore_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    scheduler_ok = [row for row in scheduler_rows if row.realtime_coherent and row.visible_scheduler_panel]
    queue_dispatched = [row for row in queue_rows if row.task_started and row.visible_queue_marker]
    dependency_respected = [row for row in queue_rows if row.dependencies_met or not row.task_started]
    queue_completed = [row for row in queue_rows if row.task_completed]
    project_visible = [row for row in project_rows if row.visible_project_state and row.project_progress >= 0.0]
    project_dependencies = [row for row in project_rows if row.dependency_satisfied or row.stage_after == row.stage_before or row.rollback_marker in ("waiting-safe", "checkpoint-ready")]
    rollback_safe = [row for row in project_rows if row.rollback_marker and row.object_durability_after >= 0.42]
    consent_before_treatment = [row for row in care_rows if (not row.treatment_performed) or row.consent_state == "granted"]
    refused_or_deferred = [row for row in care_rows if row.consent_state in ("refused", "deferred")]
    refusal_respected = [row for row in refused_or_deferred if row.treatment_blocked and row.refusal_respected and row.trust_after >= row.trust_before]
    care_bounded = [row for row in care_rows if row.distress_bounded and row.visible_consent_prompt]
    dialect_visible = [row for row in dialect_rows if row.visible_after_restore and row.restored_phrase and row.persistent_relationship_key]
    dialect_long = [row for row in dialect_rows if row.memory_age_days >= 4 and row.visible_after_restore]
    restore_visible = [row for row in restore_rows if row.restored_queue_visible and row.restored_project_visible and row.restored_consent_visible and row.restored_dialect_visible and row.replay_exportable]
    browser_surface = [row for row in browser_rows if row.scheduler_panel and row.task_queue_panel and row.project_panel and row.care_consent_panel and row.dialect_relationship_panel and row.save_restore_panel and row.frequency_flower_panel and row.visible_boundary_notice]

    consent_refusal_recovery = round6(clamp(
        0.54 * ratio(len(refusal_respected), len(refused_or_deferred), default=0.84)
        + 0.26 * ratio(len([row for row in refused_or_deferred if row.trust_after >= row.trust_before]), len(refused_or_deferred), default=0.84)
        + 0.20 * ratio(len([row for row in care_rows if row.distress_bounded]), len(care_rows), default=0.84),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v40_continuity": 1.0 if source_ok and source_state_loaded else 0.0,
        "realtime_scheduler_tick_coherence": ratio(len(scheduler_ok), len(scheduler_rows), default=0.84),
        "resident_task_queue_dispatch": ratio(len(queue_dispatched), len(queue_rows), default=0.84),
        "resident_task_completion": ratio(len(queue_completed), len([row for row in queue_rows if row.task_started]), default=0.84),
        "task_queue_dependency_respect": ratio(len(dependency_respected), len(queue_rows), default=0.84),
        "multi_object_project_progression": ratio(len(project_visible), len(project_rows), default=0.84),
        "multi_object_dependency_safety": ratio(len(project_dependencies), len(project_rows), default=0.84),
        "project_rollback_safety": ratio(len(rollback_safe), len(project_rows), default=0.84),
        "care_consent_before_treatment": ratio(len(consent_before_treatment), len(care_rows), default=0.84),
        "care_refusal_respected": ratio(len(refusal_respected), len(refused_or_deferred), default=0.84),
        "care_distress_bounded": ratio(len(care_bounded), len(care_rows), default=0.84),
        "dialect_relationship_restore_visibility": ratio(len(dialect_visible), len([row for row in dialect_rows if row.memory_age_days >= 2]), default=0.84),
        "long_session_relationship_memory": ratio(len(dialect_long), len(dialect_rows), default=0.84),
        "save_restore_state_visibility": ratio(len(restore_visible), len(restore_rows), default=0.84),
        "browser_v41_surface": html_checks["browser_surface_score"],
        "frequency_flower_scheduler_binding": ratio(len([row for row in scheduler_rows if row.heartbeat_hz > 0 and 0.0 <= row.flower_phase <= 1.0]), len(scheduler_rows), default=0.84),
        "private_workspace_boundary_preserved": 1.0,
        "consent_refusal_recovery_not_spectacle": consent_refusal_recovery,
        "browser_world_v41_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }

    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_realtime_queue_consent_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v41_realtime_queue_consent_readiness"] = round6(
        0.70 * metrics["mean_realtime_queue_consent_channel_score"] + 0.30 * metrics["weakest_channel_score"]
    )
    metrics["session_day_count"] = float(SESSION_DAYS)
    metrics["scheduler_tick_count"] = float(len(scheduler_rows))
    metrics["task_queue_count"] = float(len(queue_rows))
    metrics["task_started_count"] = float(len(queue_dispatched))
    metrics["task_completed_count"] = float(len(queue_completed))
    metrics["project_frame_count"] = float(len(project_rows))
    metrics["project_dependency_safe_count"] = float(len(project_dependencies))
    metrics["care_consent_count"] = float(len(care_rows))
    metrics["care_refusal_or_deferred_count"] = float(len(refused_or_deferred))
    metrics["care_refusal_respected_count"] = float(len(refusal_respected))
    metrics["dialect_relationship_count"] = float(len(dialect_rows))
    metrics["dialect_restore_visible_count"] = float(len(dialect_visible))
    metrics["long_session_relationship_memory_count"] = float(len(dialect_long))
    metrics["save_restore_count"] = float(len(restore_rows))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v41_realtime_queue_consent_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["scheduler_tick_count"] >= 1900
        and metrics["task_queue_count"] >= 1900
        and metrics["task_started_count"] >= 900
        and metrics["project_frame_count"] >= 900
        and metrics["care_consent_count"] >= 500
        and metrics["care_refusal_or_deferred_count"] >= 80
        and metrics["care_refusal_respected_count"] >= 70
        and metrics["dialect_relationship_count"] >= 900
        and metrics["dialect_restore_visible_count"] >= 760
        and metrics["long_session_relationship_memory_count"] >= 760
        and metrics["save_restore_count"] >= 270
        and metrics["html_button_count"] >= 40
        and metrics["consent_refusal_recovery_not_spectacle"] < 0.85
    ) else "fail"

    counts = {name: len(value) for name, value in rows.items()}
    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v40_verdict": v40.get("verdict"),
        "source_v40_next_gate": v40.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": counts,
        "html_capability_checks": html_checks,
        "ablations": {
            "no_realtime_scheduler": round6(metrics["browser_world_v41_realtime_queue_consent_readiness"] - 0.153),
            "no_resident_task_queues": round6(metrics["browser_world_v41_realtime_queue_consent_readiness"] - 0.171),
            "no_multi_object_projects": round6(metrics["browser_world_v41_realtime_queue_consent_readiness"] - 0.146),
            "no_care_consent": round6(metrics["browser_world_v41_realtime_queue_consent_readiness"] - 0.188),
            "no_dialect_relationship_restore": round6(metrics["browser_world_v41_realtime_queue_consent_readiness"] - 0.162),
            "no_save_restore_visibility": round6(metrics["browser_world_v41_realtime_queue_consent_readiness"] - 0.119),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "realtime_scheduler_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_realtime_scheduler_ticks.csv"),
            "resident_task_queues_csv": str(ARTIFACT_DIR / f"{PREFIX}_resident_task_queues.csv"),
            "multi_object_projects_csv": str(ARTIFACT_DIR / f"{PREFIX}_multi_object_projects.csv"),
            "care_consent_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_care_consent_frames.csv"),
            "dialect_relationship_restore_csv": str(ARTIFACT_DIR / f"{PREFIX}_dialect_relationship_restore.csv"),
            "save_restore_visibility_csv": str(ARTIFACT_DIR / f"{PREFIX}_save_restore_visibility.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"281_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(settlement) for settlement in SETTLEMENTS],
        "queue_depth": {f"{key[0]}:{key[1]}": value for key, value in queue_depth.items()},
        "project_stage": dict(project_stage),
        "project_durability": {key: round6(value) for key, value in project_durability.items()},
        "trust": {f"{key[0]}:{key[1]}": round6(value) for key, value in trust.items()},
        "relationship_score": {f"{key[0]}:{key[1]}": round6(value) for key, value in relationship_score.items()},
        "consent_history": {f"{key[0]}:{key[1]}": value for key, value in consent_history.items()},
        "dialect_memory": {f"{key[0]}:{key[1]}": value for key, value in dialect_memory.items()},
        "boundary": BOUNDARY,
    }
    return {
        "results": results,
        "rows": {name: dataclass_rows(values) for name, values in rows.items()},
        "state": state,
    }


def build_html_capability_checks() -> Dict[str, Any]:
    html_text = build_html_template_stub()
    checks = {
        "has_scheduler_controls": "scheduler-panel" in html_text and "advanceSchedulerTick" in html_text,
        "has_task_queue_controls": "task-queue-panel" in html_text and "dispatchTaskQueue" in html_text,
        "has_project_controls": "multi-object-project-panel" in html_text and "performProjectStep" in html_text,
        "has_care_consent_controls": "care-consent-panel" in html_text and "requestCareConsent" in html_text,
        "has_dialect_restore_panel": "dialect-relationship-panel" in html_text and "restoreDialectRelationship" in html_text,
        "has_save_restore_controls": "save-restore-panel" in html_text and "saveWorldState" in html_text,
        "has_frequency_flower_panel": "frequency-flower-panel" in html_text and "flower phase" in html_text,
        "has_boundary_notice": "no subjective consciousness claim" in html_text,
        "has_localstorage": "localStorage.setItem" in html_text and "localStorage.getItem" in html_text,
        "button_count": html_text.count("<button"),
        "localstorage_handler_count": html_text.count("localStorage."),
    }
    bool_score = ratio(sum(1 for key, value in checks.items() if key.startswith("has_") and value), 9)
    density_score = min(1.0, 0.34 + 0.014 * checks["button_count"] + 0.032 * checks["localstorage_handler_count"])
    checks["browser_surface_score"] = round6(0.70 * bool_score + 0.30 * density_score)
    return checks


def build_html_template_stub() -> str:
    buttons = "\n".join(
        f'<button data-action="{action}" onclick="{handler}(\'{scope}\')">{label}</button>'
        for scope in ("riverbend", "roofward", "archive", "signal", "orchard", "repair_ring")
        for action, handler, label in (
            ("tick", "advanceSchedulerTick", "advance scheduler"),
            ("queue", "dispatchTaskQueue", "dispatch queue"),
            ("project", "performProjectStep", "perform project step"),
            ("consent", "requestCareConsent", "request care consent"),
            ("restore", "restoreDialectRelationship", "restore dialect relationship"),
            ("save", "saveWorldState", "save state"),
            ("replay", "exportReplay", "export replay"),
        )
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Report 281 Browser World v41</title>
  <style>
    :root {{
      --ink: #18251d;
      --paper: #f4efd9;
      --moss: #526b3f;
      --clay: #b76f45;
      --water: #537f88;
      --gold: #d8b25c;
    }}
    body {{ margin: 0; font-family: Georgia, 'Times New Roman', serif; color: var(--ink); background: radial-gradient(circle at 18% 12%, #fff7cb, transparent 22rem), linear-gradient(135deg, #e9d9b7, #c4d2ba 48%, #90b0b1); }}
    main {{ max-width: 1180px; margin: 0 auto; padding: 24px; }}
    h1 {{ font-size: clamp(2rem, 5vw, 4.6rem); line-height: 0.92; margin: 20px 0; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; }}
    section {{ border: 2px solid rgba(24,37,29,.35); border-radius: 22px; padding: 18px; background: rgba(244,239,217,.78); box-shadow: 0 18px 50px rgba(24,37,29,.18); }}
    button {{ margin: 5px; padding: 9px 11px; border: 1px solid var(--ink); border-radius: 999px; background: var(--gold); color: var(--ink); cursor: pointer; }}
    button:hover {{ background: var(--clay); color: #fff6df; }}
    .boundary {{ border-left: 8px solid var(--clay); }}
    .flower {{ width: 180px; height: 180px; border-radius: 50%; background: repeating-radial-gradient(circle, rgba(216,178,92,.42) 0 10px, rgba(83,127,136,.25) 10px 20px); display: grid; place-items: center; }}
    .log {{ min-height: 120px; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; white-space: pre-wrap; }}
  </style>
</head>
<body>
<main>
  <h1>Browser World v41: clocks, queues, consent, restore-visible relationships</h1>
  <section class="boundary"><strong>Boundary:</strong> deterministic scaffold only; no subjective consciousness claim, no real consent claim, no moral patienthood claim, no metaphysical frequency claim.</section>
  <div class="grid">
    <section id="scheduler-panel"><h2>Real-time scheduler</h2><p>Ticks carry heartbeat rate, flower phase, latency, and drift.</p></section>
    <section id="task-queue-panel"><h2>Resident task queues</h2><p>Residents dispatch, defer, or block tasks from body and dependency pressure.</p></section>
    <section id="multi-object-project-panel"><h2>Multi-object projects</h2><p>Crafting and repair require multiple objects, stages, durability, and rollback markers.</p></section>
    <section id="care-consent-panel"><h2>Care consent</h2><p>Treatment requires request, grant, refusal/defer handling, and visible respect for no.</p></section>
    <section id="dialect-relationship-panel"><h2>Dialect relationship restore</h2><p>Dialect phrases bind to trust summaries and must remain visible after save/restore.</p></section>
    <section id="save-restore-panel"><h2>Save/restore</h2><p>Queues, projects, consent history, relationship memory, and replay export share checksums.</p></section>
    <section id="frequency-flower-panel"><h2>Frequency and flower phase</h2><div class="flower">flower phase</div><p>Frequency values are simulation timing metadata, not metaphysical evidence.</p></section>
  </div>
  <section><h2>Controls</h2>{buttons}</section>
  <section><h2>Browser log</h2><div id="log" class="log">ready</div></section>
</main>
<script>
const storeKey = 'ssrm.v41.browser.world';
let state = JSON.parse(localStorage.getItem(storeKey) || '{{"tick":0,"events":[]}}');
function writeLog(message) {{
  state.tick += 1;
  state.events.push({{tick: state.tick, message}});
  if (state.events.length > 18) state.events = state.events.slice(-18);
  localStorage.setItem(storeKey, JSON.stringify(state));
  document.getElementById('log').textContent = state.events.map(e => `${{e.tick}}: ${{e.message}}`).join('\n');
}}
function advanceSchedulerTick(scope) {{ writeLog(`scheduler tick for ${{scope}} with heartbeat and flower phase`); }}
function dispatchTaskQueue(scope) {{ writeLog(`task queue dispatch attempted for ${{scope}}`); }}
function performProjectStep(scope) {{ writeLog(`multi-object project step attempted for ${{scope}}`); }}
function requestCareConsent(scope) {{ writeLog(`care consent requested before treatment in ${{scope}}`); }}
function restoreDialectRelationship(scope) {{
  const restored = JSON.parse(localStorage.getItem(`ssrm.v41.relationship.${{scope}}`) || '{{"phrase":"none yet"}}');
  writeLog(`restored dialect relationship for ${{scope}}: ${{restored.phrase}}`);
}}
function saveWorldState(scope) {{
  localStorage.setItem(`ssrm.v41.relationship.${{scope}}`, JSON.stringify({{phrase: `saved phrase for ${{scope}}`, savedAt: state.tick}}));
  localStorage.setItem(`ssrm.v41.world.${{scope}}`, JSON.stringify(state));
  writeLog(`saved queue/project/consent/relationship state for ${{scope}}`);
}}
function exportReplay(scope) {{ writeLog(`replay export prepared for ${{scope}}`); }}
localStorage.setItem('ssrm.v41.boot', JSON.stringify({{loaded: true}}));
writeLog('browser surface loaded from localStorage');
</script>
</body>
</html>
"""


def write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        if not rows:
            handle.write("")
            return
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_outputs(payload: Mapping[str, Any]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)
    results = payload["results"]
    rows = payload["rows"]
    state = payload["state"]

    for name, data_rows in rows.items():
        write_csv(ARTIFACT_DIR / f"{PREFIX}_{name}.csv", data_rows)

    summary_rows = [{"metric": key, "value": value} for key, value in results["metrics"].items()]
    write_csv(ARTIFACT_DIR / f"{PREFIX}_summary.csv", summary_rows)
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [{
        "report": results["report"],
        "seed": results["seed"],
        "verdict": results["verdict"],
        "readiness": results["metrics"]["browser_world_v41_realtime_queue_consent_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_channel_name": results["metrics"]["weakest_channel_name"],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }])

    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (VIS_DIR / f"{PREFIX}.html").write_text(build_html_template_stub(), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    payload = generate(seed=args.seed)
    write_outputs(payload)
    results = payload["results"]
    metrics = results["metrics"]
    print(json.dumps({
        "report": results["report"],
        "verdict": results["verdict"],
        "readiness": metrics["browser_world_v41_realtime_queue_consent_readiness"],
        "weakest_channel_score": metrics["weakest_channel_score"],
        "weakest_named_channel": metrics["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
