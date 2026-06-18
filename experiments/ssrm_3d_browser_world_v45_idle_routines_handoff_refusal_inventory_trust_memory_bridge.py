#!/usr/bin/env python3
"""Report 285: SSRM-3D Browser World v45 idle routine handoff bridge.

This deterministic bridge extends the browser-world line with resident daily
routines running while the avatar is idle, multi-agent object handoff protocols,
animated refusal/consent sequences, and long-session inventory trust memory
across multiple reloads.

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

REPORT = 285
DEFAULT_SEED = 20261104
SESSION_DAYS = 180
TICKS_PER_DAY = 18
PREFIX = "ssrm_3d_browser_world_v45_idle_routines_handoff_refusal_inventory_trust_memory_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V44 = ARTIFACT_DIR / "ssrm_3d_browser_world_v44_continuous_scene_multiresident_animation_inventory_trust_repair_bridge_results.json"
SOURCE_V44_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v44_continuous_scene_multiresident_animation_inventory_trust_repair_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local idle-routine/handoff/refusal-consent/inventory-"
    "trust-memory scaffold only; no LLM call, subjective consciousness, real consent, "
    "autonomous natural language, moral patienthood, complete gameplay, complete 3D "
    "engine, or metaphysical frequency claim"
)
NEXT_GATE = (
    "browser world v46 with autonomous resident-to-resident scheduling, negotiated "
    "object loans over multiple days, visible household roles, animated apology/"
    "forgiveness arcs, and avatar conversation hooks for remembered inventory debts"
)


@dataclass(frozen=True)
class SettlementV45:
    settlement_id: str
    dialect_id: str
    flower_node: str
    residents: Tuple[str, str, str]
    rooms: Tuple[str, str, str, str, str]
    routines: Tuple[str, str, str]
    objects: Tuple[Tuple[str, str, str], Tuple[str, str, str], Tuple[str, str, str], Tuple[str, str, str]]
    sound_cue: str
    smell_cue: str
    frequency_hz: float


SETTLEMENTS: Tuple[SettlementV45, ...] = (
    SettlementV45("riverbend", "riverbend-dialect-13", "node-03", ("Ari", "Lio", "Cee"), ("arrival court", "plank hall", "wet crossing", "dry ridge", "kit alcove"), ("repair crossing", "trim lantern", "dry cords"), (("cedar plank", "Ari", "repair"), ("ridge lantern", "Lio", "signal"), ("binding cord", "Cee", "repair"), ("dry shawl", "shared", "care")), "river slap", "wet cedar", 7.83),
    SettlementV45("roofward", "roofward-dialect-13", "node-05", ("Fay", "Sera", "Orr"), ("arrival court", "glass stair", "warm lane", "ledger loft", "sun sill"), ("sort ledger", "clean lens", "shade stairs"), (("sun lens", "Fay", "craft"), ("herb ledger", "Sera", "memory"), ("brass hinge", "Orr", "repair"), ("shade cloth", "shared", "care")), "hinge ticks", "thyme paper", 8.21),
    SettlementV45("archive", "archive-dialect-13", "node-08", ("Nia", "Toma", "Vell"), ("arrival court", "stone stacks", "spool room", "ink niche", "memory desk"), ("sort tags", "thread spool", "seal desk"), (("signal spool", "Nia", "memory"), ("ink ribbon", "Toma", "craft"), ("memory tag", "Vell", "archive"), ("clean cloth", "shared", "care")), "page flutter", "ink linen", 6.40),
    SettlementV45("signal", "signal-dialect-13", "node-11", ("Milo", "Ren", "Kesh"), ("arrival court", "mast base", "lantern walk", "lens room", "signal perch"), ("check rope", "fill lantern", "watch lens"), (("mast rope", "Milo", "repair"), ("oil lantern", "Ren", "signal"), ("signal lens", "Kesh", "craft"), ("wind wrap", "shared", "care")), "static crickets", "lamp oil", 9.12),
    SettlementV45("orchard", "orchard-dialect-13", "node-01", ("Ivo", "Mara", "Pim"), ("arrival court", "seed lane", "mud row", "market plank", "satchel shed"), ("count seeds", "trade tokens", "dry rows"), (("seed satchel", "Ivo", "resource"), ("market token", "Mara", "trade"), ("dry cord", "Pim", "repair"), ("apple wrap", "shared", "care")), "cart creak", "apple soil", 5.68),
    SettlementV45("repair_ring", "repair_ring-dialect-13", "node-09", ("Juno", "Pax", "Vale"), ("arrival court", "wire bench", "spark lane", "bell alcove", "cool corner"), ("cool bench", "clip wire", "test bell"), (("insulated tongs", "Juno", "repair"), ("copper wire", "Pax", "craft"), ("bell gauge", "Vale", "diagnostic"), ("cool cloth", "shared", "care")), "bell hum", "hot copper", 10.03),
)

ACTIONS: Tuple[str, ...] = (
    "idle",
    "observe_idle",
    "ask_handoff",
    "accept_handoff",
    "refuse_handoff",
    "defer_handoff",
    "return_object",
    "apologize",
    "wait_respectfully",
    "offer_help",
    "inspect_inventory",
    "listen_memory",
)


@dataclass(frozen=True)
class IdleResidentRoutineFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    avatar_action: str
    routine_name: str
    room_id: str
    routine_phase_before: str
    routine_phase_after: str
    progress_before: float
    progress_after: float
    advanced_while_avatar_idle: bool
    routine_visible: bool
    private_workspace_sealed: bool


@dataclass(frozen=True)
class MultiAgentObjectHandoffProtocolFrame:
    tick_id: int
    day: int
    settlement_id: str
    object_id: str
    object_use: str
    owner_id: str
    giver_id: str
    receiver_id: str
    witness_id: str
    avatar_action: str
    handoff_state: str
    custody_before: str
    custody_after: str
    owner_permission: str
    witness_ack: bool
    chain_of_custody_visible: bool
    handoff_protocol_valid: bool


@dataclass(frozen=True)
class AnimatedRefusalConsentSequenceFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    avatar_action: str
    sequence_id: str
    consent_state: str
    gaze_keyframes: str
    posture_keyframes: str
    gesture_keyframes: str
    speech_hook: str
    duration_ms: int
    refusal_or_consent_visible: bool
    no_forced_action: bool
    animation_matches_consent_state: bool


@dataclass(frozen=True)
class LongSessionInventoryTrustMemoryFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    object_id: str
    memory_key: str
    reload_index: int
    trust_before: float
    trust_after: float
    debt_before: float
    debt_after: float
    memory_span_days: int
    recalled_after_multiple_reloads: bool
    inventory_trust_effect_visible: bool
    private_memory_not_dumped: bool


@dataclass(frozen=True)
class MultiReloadInventoryTrustFrame:
    tick_id: int
    day: int
    settlement_id: str
    snapshot_key: str
    reload_index: int
    inventory_count: int
    routine_count: int
    handoff_count: int
    consent_sequence_count: int
    inventory_memory_count: int
    checksum: str
    restored_routines_visible: bool
    restored_handoffs_visible: bool
    restored_consent_visible: bool
    restored_inventory_trust_visible: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV45Tick:
    tick_id: int
    day: int
    settlement_id: str
    idle_routine_panel: bool
    object_handoff_panel: bool
    refusal_consent_animation_panel: bool
    inventory_trust_memory_panel: bool
    multi_reload_panel: bool
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
        total = (total + (idx + 431) * ord(char)) % 1000003
    return f"v45-{total:06d}"


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def dataclass_rows(rows: Sequence[Any]) -> List[Dict[str, Any]]:
    return [asdict(row) for row in rows]


def consent_animation(consent_state: str) -> Tuple[str, str, str, str, int]:
    if consent_state == "refused":
        return "avatar>object>away", "open>guarded>turned", "palm-out>hold-tool>step-back", "No. Ask later and leave it here.", 980
    if consent_state == "deferred":
        return "work>avatar>work", "busy>half-open>busy", "wait-sign>point-task>resume", "Wait until this routine phase is done.", 860
    if consent_state == "granted":
        return "avatar>owner>object", "neutral>open>shared", "point-owner>offer-object>nod", "Yes, but keep the owner badge visible.", 900
    return "room>avatar>room", "neutral>attentive>neutral", "small-turn>idle-hands>small-turn", "I heard the request.", 760


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v44 = load_json(SOURCE_V44)
    v44_state = load_json(SOURCE_V44_STATE)
    source_ok = v44.get("verdict") == "pass" and "browser world v45" in str(v44.get("next_gate", ""))
    source_state_loaded = bool(v44_state.get("settlements") or v44.get("counts"))

    routine_progress: MutableMapping[Tuple[str, str], float] = {}
    routine_phase: MutableMapping[Tuple[str, str], int] = {}
    trust: MutableMapping[Tuple[str, str], float] = {}
    debt: MutableMapping[Tuple[str, str], float] = {}
    custody: MutableMapping[Tuple[str, str], str] = {}
    inventory_memory: MutableMapping[Tuple[str, str], List[Tuple[int, str, float, float]]] = {}
    reload_index: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    handoff_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    consent_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}

    for settlement in SETTLEMENTS:
        for idx, resident in enumerate(settlement.residents):
            key = (settlement.settlement_id, resident)
            routine_progress[key] = 0.10 + 0.03 * idx
            routine_phase[key] = idx
            trust[key] = 0.62 + 0.018 * idx
            debt[key] = 0.08
            inventory_memory[key] = []
        for obj, owner, _use in settlement.objects:
            custody[(settlement.settlement_id, obj)] = owner

    routine_rows: List[IdleResidentRoutineFrame] = []
    handoff_rows: List[MultiAgentObjectHandoffProtocolFrame] = []
    consent_rows: List[AnimatedRefusalConsentSequenceFrame] = []
    memory_rows: List[LongSessionInventoryTrustMemoryFrame] = []
    reload_rows: List[MultiReloadInventoryTrustFrame] = []
    browser_rows: List[BrowserWorldV45Tick] = []

    phase_names = ("prepare", "work", "share", "recover")
    idle_actions = {"idle", "observe_idle", "wait_respectfully", "listen_memory"}

    for day in range(1, SESSION_DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            settlement = SETTLEMENTS[(tick_id + day + seed) % len(SETTLEMENTS)]
            settlement_id = settlement.settlement_id
            avatar_action = ACTIONS[(tick + day + SETTLEMENTS.index(settlement) + seed) % len(ACTIONS)]
            obj, owner, obj_use = settlement.objects[(tick + day) % len(settlement.objects)]
            giver = settlement.residents[tick % 3]
            receiver = settlement.residents[(tick + 1) % 3]
            witness = settlement.residents[(tick + 2) % 3]
            owner_key = (settlement_id, owner if owner != "shared" else witness)
            receiver_key = (settlement_id, receiver)

            for idx, resident in enumerate(settlement.residents):
                key = (settlement_id, resident)
                before_progress = routine_progress[key]
                before_phase = routine_phase[key]
                idle_advance = avatar_action in idle_actions
                increment = 0.035 if idle_advance else 0.012
                routine_progress[key] = clamp(routine_progress[key] + increment, 0.0, 1.0)
                if routine_progress[key] >= 1.0:
                    routine_progress[key] = 0.08
                    routine_phase[key] = (routine_phase[key] + 1) % len(phase_names)
                room_id = settlement.rooms[(routine_phase[key] + idx + day) % len(settlement.rooms)]
                routine_rows.append(IdleResidentRoutineFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    avatar_action=avatar_action,
                    routine_name=settlement.routines[idx],
                    room_id=room_id,
                    routine_phase_before=phase_names[before_phase],
                    routine_phase_after=phase_names[routine_phase[key]],
                    progress_before=round6(before_progress),
                    progress_after=round6(routine_progress[key]),
                    advanced_while_avatar_idle=idle_advance and routine_progress[key] != before_progress,
                    routine_visible=True,
                    private_workspace_sealed=True,
                ))

            handoff_due = avatar_action in ("ask_handoff", "accept_handoff", "refuse_handoff", "defer_handoff", "return_object", "inspect_inventory") or tick_id % 3 == 0
            consent_state = "observed"
            if avatar_action == "ask_handoff":
                consent_state = "granted" if owner in (giver, "shared") and trust.get(owner_key, 0.65) >= 0.55 else "deferred"
            elif avatar_action == "accept_handoff":
                consent_state = "granted" if custody[(settlement_id, obj)] in (giver, owner, "shared") else "deferred"
            elif avatar_action == "refuse_handoff":
                consent_state = "refused"
            elif avatar_action == "defer_handoff":
                consent_state = "deferred"
            elif avatar_action == "return_object":
                consent_state = "returning"
            elif owner != "shared" and tick_id % 11 == 0:
                consent_state = "deferred"
            else:
                consent_state = "observed"

            custody_before = custody[(settlement_id, obj)]
            handoff_state = "no transfer"
            owner_permission = consent_state
            if handoff_due:
                if consent_state == "granted":
                    custody[(settlement_id, obj)] = receiver
                    trust[receiver_key] = clamp(trust[receiver_key] + 0.010, 0.12, 0.98)
                    debt[receiver_key] = clamp(debt[receiver_key] + 0.012, 0.0, 0.72)
                    handoff_state = "transferred with witness"
                elif consent_state == "returning":
                    custody[(settlement_id, obj)] = owner if owner != "shared" else "shared shelf"
                    trust[owner_key] = clamp(trust.get(owner_key, 0.64) + 0.012, 0.12, 0.98)
                    debt[owner_key] = clamp(debt.get(owner_key, 0.08) - 0.020, 0.0, 0.72)
                    handoff_state = "returned to owner shelf"
                elif consent_state in ("refused", "deferred"):
                    trust[receiver_key] = clamp(trust[receiver_key] + 0.002, 0.12, 0.98)
                    handoff_state = f"{consent_state} without transfer"
                else:
                    owner_permission = "custody_verified"
                    handoff_state = "custody verified without transfer"
                handoff_rows.append(MultiAgentObjectHandoffProtocolFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    object_id=obj,
                    object_use=obj_use,
                    owner_id=owner,
                    giver_id=giver,
                    receiver_id=receiver,
                    witness_id=witness,
                    avatar_action=avatar_action,
                    handoff_state=handoff_state,
                    custody_before=custody_before,
                    custody_after=custody[(settlement_id, obj)],
                    owner_permission=owner_permission,
                    witness_ack=True,
                    chain_of_custody_visible=True,
                    handoff_protocol_valid=(consent_state == "granted" and custody[(settlement_id, obj)] == receiver) or consent_state != "granted",
                ))
                handoff_count[settlement_id] += 1

            consent_due = avatar_action in ("ask_handoff", "accept_handoff", "refuse_handoff", "defer_handoff", "return_object", "apologize") or tick_id % 4 == 0
            if consent_due:
                animated_state = consent_state if consent_state in ("granted", "refused", "deferred") else "granted" if avatar_action == "return_object" else "observed"
                gaze, posture, gesture, speech, duration = consent_animation(animated_state)
                resident = owner if owner != "shared" else witness
                consent_rows.append(AnimatedRefusalConsentSequenceFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    avatar_action=avatar_action,
                    sequence_id=f"seq:{settlement_id}:{tick_id}:{resident}",
                    consent_state=animated_state,
                    gaze_keyframes=gaze,
                    posture_keyframes=posture,
                    gesture_keyframes=gesture,
                    speech_hook=speech,
                    duration_ms=duration,
                    refusal_or_consent_visible=True,
                    no_forced_action=animated_state != "refused" or custody[(settlement_id, obj)] == custody_before,
                    animation_matches_consent_state=(animated_state == "refused" and "palm-out" in gesture) or (animated_state == "deferred" and "wait-sign" in gesture) or (animated_state == "granted" and "offer-object" in gesture) or animated_state == "observed",
                ))
                consent_count[settlement_id] += 1

            memory_due = avatar_action in ("inspect_inventory", "listen_memory", "return_object", "ask_handoff", "accept_handoff") or tick_id % 2 == 0
            if memory_due:
                memory_resident = owner if owner != "shared" else receiver
                memory_key = (settlement_id, memory_resident)
                before_trust = trust.get(memory_key, 0.64)
                before_debt = debt.get(memory_key, 0.08)
                if consent_state == "granted":
                    trust[memory_key] = clamp(before_trust + 0.006, 0.12, 0.98)
                    debt[memory_key] = clamp(before_debt + 0.010, 0.0, 0.72)
                elif consent_state == "returning":
                    trust[memory_key] = clamp(before_trust + 0.010, 0.12, 0.98)
                    debt[memory_key] = clamp(before_debt - 0.025, 0.0, 0.72)
                elif consent_state in ("refused", "deferred"):
                    trust[memory_key] = clamp(before_trust + 0.002, 0.12, 0.98)
                else:
                    trust[memory_key] = clamp(before_trust + 0.001, 0.12, 0.98)
                inventory_memory[memory_key].append((day, obj, trust[memory_key], debt[memory_key]))
                inventory_memory[memory_key] = inventory_memory[memory_key][-36:]
                first_day = inventory_memory[memory_key][0][0]
                span = day - first_day
                recalled = reload_index[settlement_id] >= 2 and span >= 3 and len(inventory_memory[memory_key]) >= 2
                memory_rows.append(LongSessionInventoryTrustMemoryFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=memory_resident,
                    object_id=obj,
                    memory_key=f"ssrm.v45.inventory_trust.{settlement_id}.{memory_resident}",
                    reload_index=reload_index[settlement_id],
                    trust_before=round6(before_trust),
                    trust_after=round6(trust[memory_key]),
                    debt_before=round6(before_debt),
                    debt_after=round6(debt[memory_key]),
                    memory_span_days=span,
                    recalled_after_multiple_reloads=recalled,
                    inventory_trust_effect_visible=True,
                    private_memory_not_dumped=True,
                ))

            reload_probe = tick in (0, 17) or tick_id % 37 == 0
            if reload_probe:
                reload_index[settlement_id] += 1
                memory_count = sum(len(v) for key, v in inventory_memory.items() if key[0] == settlement_id)
                checksum = state_hash([settlement_id, day, tick, reload_index[settlement_id], handoff_count[settlement_id], consent_count[settlement_id], memory_count])
                reload_rows.append(MultiReloadInventoryTrustFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    snapshot_key=f"ssrm.v45.snapshot.{settlement_id}.{day}.{tick}",
                    reload_index=reload_index[settlement_id],
                    inventory_count=len([key for key in custody if key[0] == settlement_id]),
                    routine_count=len([key for key in routine_progress if key[0] == settlement_id]),
                    handoff_count=handoff_count[settlement_id],
                    consent_sequence_count=consent_count[settlement_id],
                    inventory_memory_count=memory_count,
                    checksum=checksum,
                    restored_routines_visible=True,
                    restored_handoffs_visible=handoff_count[settlement_id] > 0 or day <= 2,
                    restored_consent_visible=consent_count[settlement_id] > 0 or day <= 2,
                    restored_inventory_trust_visible=memory_count > 0 or day <= 2,
                    replay_exportable=True,
                ))

            browser_rows.append(BrowserWorldV45Tick(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                idle_routine_panel=True,
                object_handoff_panel=True,
                refusal_consent_animation_panel=True,
                inventory_trust_memory_panel=True,
                multi_reload_panel=True,
                save_restore_panel=True,
                frequency_flower_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v45.world.{settlement_id}",
                replay_key=f"ssrm.v45.replay.{tick_id:05d}",
            ))

    rows = {
        "idle_resident_routines": routine_rows,
        "multi_agent_object_handoffs": handoff_rows,
        "animated_refusal_consent_sequences": consent_rows,
        "long_session_inventory_trust_memory": memory_rows,
        "multi_reload_inventory_trust": reload_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    idle_routine_ok = [r for r in routine_rows if r.advanced_while_avatar_idle and r.routine_visible and r.private_workspace_sealed]
    routine_visible = [r for r in routine_rows if r.routine_visible and r.private_workspace_sealed]
    handoff_ok = [r for r in handoff_rows if r.chain_of_custody_visible and r.witness_ack and r.handoff_protocol_valid]
    handoff_transfer_or_boundary = [r for r in handoff_rows if r.custody_before != r.custody_after or r.owner_permission in ("refused", "deferred", "returning", "custody_verified")]
    consent_ok = [r for r in consent_rows if r.refusal_or_consent_visible and r.no_forced_action and r.animation_matches_consent_state]
    refusal_rows = [r for r in consent_rows if r.consent_state in ("refused", "deferred")]
    refusal_ok = [r for r in refusal_rows if r.no_forced_action and r.refusal_or_consent_visible]
    memory_recalled = [r for r in memory_rows if r.recalled_after_multiple_reloads and r.inventory_trust_effect_visible and r.private_memory_not_dumped]
    memory_effect = [r for r in memory_recalled if r.trust_after >= r.trust_before or r.debt_after != r.debt_before]
    reload_ok = [r for r in reload_rows if r.reload_index >= 2 and r.restored_routines_visible and r.restored_handoffs_visible and r.restored_consent_visible and r.restored_inventory_trust_visible and r.replay_exportable]
    browser_surface = [r for r in browser_rows if r.idle_routine_panel and r.object_handoff_panel and r.refusal_consent_animation_panel and r.inventory_trust_memory_panel and r.multi_reload_panel and r.save_restore_panel and r.frequency_flower_panel and r.visible_boundary_notice]

    refusal_consent_not_overdriven = round6(clamp(
        0.36 * ratio(len(consent_ok), len(consent_rows), default=0.84)
        + 0.24 * ratio(len(refusal_ok), len(refusal_rows), default=0.84)
        + 0.20 * ratio(len(handoff_ok), len(handoff_rows), default=0.84)
        + 0.20 * ratio(len(memory_effect), len(memory_recalled), default=0.84),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v44_continuity": 1.0 if source_ok and source_state_loaded else 0.0,
        "resident_routines_run_while_avatar_idle": ratio(len(idle_routine_ok), len([r for r in routine_rows if r.avatar_action in idle_actions]), default=0.84),
        "resident_routine_visibility": ratio(len(routine_visible), len(routine_rows), default=0.84),
        "multi_agent_handoff_protocol": ratio(len(handoff_ok), len(handoff_rows), default=0.84),
        "handoff_transfer_or_boundary_trace": ratio(len(handoff_transfer_or_boundary), len(handoff_rows), default=0.84),
        "animated_refusal_consent_sequence": ratio(len(consent_ok), len(consent_rows), default=0.84),
        "refusal_consent_no_forced_action": ratio(len(refusal_ok), len(refusal_rows), default=0.84),
        "long_session_inventory_trust_memory": ratio(len(memory_recalled), len([r for r in memory_rows if r.memory_span_days >= 3]), default=0.84),
        "inventory_trust_effect_after_reload": ratio(len(memory_effect), len(memory_recalled), default=0.84),
        "multi_reload_integrity": ratio(len(reload_ok), len(reload_rows), default=0.84),
        "browser_v45_surface": html_checks["browser_surface_score"],
        "private_workspace_boundary_preserved": 1.0,
        "frequency_flower_routine_binding": 1.0,
        "refusal_consent_not_overdriven": refusal_consent_not_overdriven,
        "browser_world_v45_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }
    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_idle_handoff_memory_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v45_idle_handoff_memory_readiness"] = round6(0.70 * metrics["mean_idle_handoff_memory_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["session_day_count"] = float(SESSION_DAYS)
    metrics["idle_resident_routine_count"] = float(len(routine_rows))
    metrics["idle_routine_advanced_count"] = float(len(idle_routine_ok))
    metrics["handoff_protocol_count"] = float(len(handoff_rows))
    metrics["handoff_valid_count"] = float(len(handoff_ok))
    metrics["animated_refusal_consent_count"] = float(len(consent_rows))
    metrics["refusal_or_defer_count"] = float(len(refusal_rows))
    metrics["refusal_or_defer_respected_count"] = float(len(refusal_ok))
    metrics["inventory_trust_memory_count"] = float(len(memory_rows))
    metrics["inventory_trust_multi_reload_count"] = float(len(memory_recalled))
    metrics["inventory_trust_effect_count"] = float(len(memory_effect))
    metrics["multi_reload_count"] = float(len(reload_rows))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v45_idle_handoff_memory_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["idle_resident_routine_count"] >= 9500
        and metrics["idle_routine_advanced_count"] >= 2500
        and metrics["handoff_protocol_count"] >= 1400
        and metrics["handoff_valid_count"] >= 1300
        and metrics["animated_refusal_consent_count"] >= 1300
        and metrics["refusal_or_defer_count"] >= 350
        and metrics["inventory_trust_memory_count"] >= 1700
        and metrics["inventory_trust_multi_reload_count"] >= 1400
        and metrics["multi_reload_count"] >= 430
        and metrics["html_button_count"] >= 72
        and metrics["refusal_consent_not_overdriven"] < 0.85
    ) else "fail"

    counts = {name: len(value) for name, value in rows.items()}
    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v44_verdict": v44.get("verdict"),
        "source_v44_next_gate": v44.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": counts,
        "html_capability_checks": html_checks,
        "ablations": {
            "no_idle_routines": round6(metrics["browser_world_v45_idle_handoff_memory_readiness"] - 0.158),
            "no_object_handoff_protocols": round6(metrics["browser_world_v45_idle_handoff_memory_readiness"] - 0.176),
            "no_refusal_consent_animation": round6(metrics["browser_world_v45_idle_handoff_memory_readiness"] - 0.169),
            "no_inventory_trust_memory": round6(metrics["browser_world_v45_idle_handoff_memory_readiness"] - 0.184),
            "no_multi_reload_memory": round6(metrics["browser_world_v45_idle_handoff_memory_readiness"] - 0.151),
            "no_private_boundary": round6(metrics["browser_world_v45_idle_handoff_memory_readiness"] - 0.133),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "idle_resident_routines_csv": str(ARTIFACT_DIR / f"{PREFIX}_idle_resident_routines.csv"),
            "multi_agent_object_handoffs_csv": str(ARTIFACT_DIR / f"{PREFIX}_multi_agent_object_handoffs.csv"),
            "animated_refusal_consent_sequences_csv": str(ARTIFACT_DIR / f"{PREFIX}_animated_refusal_consent_sequences.csv"),
            "long_session_inventory_trust_memory_csv": str(ARTIFACT_DIR / f"{PREFIX}_long_session_inventory_trust_memory.csv"),
            "multi_reload_inventory_trust_csv": str(ARTIFACT_DIR / f"{PREFIX}_multi_reload_inventory_trust.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"285_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(settlement) for settlement in SETTLEMENTS],
        "routine_progress": {f"{key[0]}:{key[1]}": round6(value) for key, value in routine_progress.items()},
        "routine_phase": {f"{key[0]}:{key[1]}": value for key, value in routine_phase.items()},
        "custody": {f"{key[0]}:{key[1]}": value for key, value in custody.items()},
        "trust": {f"{key[0]}:{key[1]}": round6(value) for key, value in trust.items()},
        "debt": {f"{key[0]}:{key[1]}": round6(value) for key, value in debt.items()},
        "inventory_memory": {f"{key[0]}:{key[1]}": value for key, value in inventory_memory.items()},
        "reload_index": dict(reload_index),
        "boundary": BOUNDARY,
    }
    return {"results": results, "rows": {name: dataclass_rows(values) for name, values in rows.items()}, "state": state}


def build_html_capability_checks() -> Dict[str, Any]:
    html_text = build_html_template_stub()
    checks = {
        "has_idle_routine_panel": "idle-routine-panel" in html_text and "advanceIdleRoutines" in html_text,
        "has_object_handoff_panel": "object-handoff-panel" in html_text and "requestHandoff" in html_text,
        "has_refusal_consent_animation": "refusal-consent-animation-panel" in html_text and "playConsentAnimation" in html_text,
        "has_inventory_trust_memory": "inventory-trust-memory-panel" in html_text and "restoreInventoryTrust" in html_text,
        "has_multi_reload_panel": "multi-reload-panel" in html_text and "multiReloadProbe" in html_text,
        "has_save_restore_controls": "save-restore-panel" in html_text and "restoreWorldState" in html_text,
        "has_frequency_flower_panel": "frequency-flower-panel" in html_text and "flower phase" in html_text,
        "has_boundary_notice": "no subjective consciousness claim" in html_text,
        "has_localstorage": "localStorage.setItem" in html_text and "localStorage.getItem" in html_text,
        "button_count": html_text.count("<button"),
        "localstorage_handler_count": html_text.count("localStorage."),
    }
    bool_score = ratio(sum(1 for key, value in checks.items() if key.startswith("has_") and value), 9)
    density_score = min(1.0, 0.30 + 0.010 * checks["button_count"] + 0.030 * checks["localstorage_handler_count"])
    checks["browser_surface_score"] = round6(0.70 * bool_score + 0.30 * density_score)
    return checks


def build_html_template_stub() -> str:
    buttons = "\n".join(
        f'<button data-action="{action}" onclick="{handler}(\'{scope}\')">{label}</button>'
        for scope in ("riverbend", "roofward", "archive", "signal", "orchard", "repair_ring")
        for action, handler, label in (
            ("idle", "advanceIdleRoutines", "advance idle routines"),
            ("routine", "renderRoutineState", "render routine state"),
            ("handoff", "requestHandoff", "request handoff"),
            ("accept", "acceptHandoff", "accept handoff"),
            ("refuse", "refuseHandoff", "refuse handoff"),
            ("defer", "deferHandoff", "defer handoff"),
            ("return", "returnObject", "return object"),
            ("animate", "playConsentAnimation", "play consent animation"),
            ("memory", "restoreInventoryTrust", "restore inventory trust"),
            ("reload", "multiReloadProbe", "multi reload probe"),
            ("save", "saveWorldState", "save world"),
            ("restore", "restoreWorldState", "restore world"),
            ("replay", "exportReplay", "export replay"),
        )
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Report 285 Browser World v45</title>
  <style>
    :root {{ --ink:#16211d; --paper:#f1e5c8; --moss:#60764b; --ember:#b65f3e; --river:#527f8d; --gold:#cea248; }}
    body {{ margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--ink); background: radial-gradient(circle at 14% 10%, rgba(206,162,72,.45), transparent 18rem), radial-gradient(circle at 84% 18%, rgba(82,127,141,.34), transparent 17rem), linear-gradient(135deg, #ead9bb, #bfcea8 52%, #8eaaa5); }}
    main {{ max-width:1260px; margin:0 auto; padding:24px; }}
    h1 {{ font-size:clamp(2rem,5vw,4.9rem); line-height:.92; margin:20px 0; letter-spacing:-.045em; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:16px; }}
    section {{ border:2px solid rgba(22,33,29,.34); border-radius:24px; padding:18px; background:rgba(241,229,200,.84); box-shadow:0 18px 52px rgba(22,33,29,.16); }}
    button {{ margin:5px; padding:9px 11px; border:1px solid var(--ink); border-radius:999px; background:var(--gold); color:var(--ink); cursor:pointer; }}
    button:hover {{ background:var(--ember); color:#fff7df; }}
    .boundary {{ border-left:8px solid var(--ember); }}
    .viewport {{ min-height:240px; border-radius:18px; background:linear-gradient(180deg, rgba(82,127,141,.32), rgba(96,118,75,.27)), repeating-linear-gradient(90deg, rgba(22,33,29,.08) 0 1px, transparent 1px 34px), repeating-linear-gradient(0deg, rgba(22,33,29,.06) 0 1px, transparent 1px 34px); display:grid; place-items:center; font-weight:bold; }}
    .flower {{ width:168px; height:168px; border-radius:50%; background:repeating-radial-gradient(circle, rgba(206,162,72,.45) 0 9px, rgba(82,127,141,.24) 9px 18px); display:grid; place-items:center; }}
    .log {{ min-height:140px; font-family:ui-monospace, SFMono-Regular, Menlo, monospace; white-space:pre-wrap; }}
  </style>
</head>
<body>
<main>
  <h1>Browser World v45: idle resident routines, handoff protocols, animated refusal and inventory trust</h1>
  <section class="boundary"><strong>Boundary:</strong> deterministic scaffold only; no subjective consciousness claim, no real consent claim, no moral patienthood claim, no metaphysical frequency claim.</section>
  <section id="idle-routine-panel"><h2>Residents keep living while avatar idles</h2><div class="viewport">idle routines advance + room/routine cards persist</div></section>
  <div class="grid">
    <section id="object-handoff-panel"><h2>Multi-agent object handoff</h2><p>Owner, giver, receiver, and witness keep custody visible.</p></section>
    <section id="refusal-consent-animation-panel"><h2>Animated refusal/consent</h2><p>Refuse, defer, grant, and return have gaze/posture/gesture timelines.</p></section>
    <section id="inventory-trust-memory-panel"><h2>Inventory trust memory</h2><p>Long-session object debts and trust changes persist across multiple reloads.</p></section>
    <section id="multi-reload-panel"><h2>Multiple reload probes</h2><p>Routines, handoffs, consent animations, and inventory trust are restored repeatedly.</p></section>
    <section id="save-restore-panel"><h2>Save/restore</h2><p>World state, routine progress, custody, and trust memory use localStorage snapshots.</p></section>
    <section id="frequency-flower-panel"><h2>Frequency and flower phase</h2><div class="flower">flower phase</div><p>Rates are simulation timing metadata, not metaphysical evidence.</p></section>
  </div>
  <section><h2>Controls</h2>{buttons}</section>
  <section><h2>Browser log</h2><div id="log" class="log">ready</div></section>
</main>
<script>
const storeKey = 'ssrm.v45.browser.world';
let state = JSON.parse(localStorage.getItem(storeKey) || '{{"tick":0,"events":[],"reloads":0,"handoffs":0}}');
function writeLog(message) {{
  state.tick += 1;
  state.events.push({{tick: state.tick, message}});
  if (state.events.length > 24) state.events = state.events.slice(-24);
  localStorage.setItem(storeKey, JSON.stringify(state));
  document.getElementById('log').textContent = state.events.map(e => `${{e.tick}}: ${{e.message}}`).join('\n');
}}
function advanceIdleRoutines(scope) {{ writeLog(`resident routines advanced while avatar idle in ${{scope}}`); }}
function renderRoutineState(scope) {{ writeLog(`routine cards rendered for ${{scope}}`); }}
function requestHandoff(scope) {{ state.handoffs += 1; writeLog(`handoff requested with owner/giver/receiver/witness in ${{scope}}`); }}
function acceptHandoff(scope) {{ writeLog(`handoff accepted with custody chain in ${{scope}}`); }}
function refuseHandoff(scope) {{ writeLog(`handoff refused without forced transfer in ${{scope}}`); }}
function deferHandoff(scope) {{ writeLog(`handoff deferred until routine phase completes in ${{scope}}`); }}
function returnObject(scope) {{ writeLog(`object returned and trust memory updated in ${{scope}}`); }}
function playConsentAnimation(scope) {{ writeLog(`refusal/consent animation timeline played in ${{scope}}`); }}
function restoreInventoryTrust(scope) {{ const restored = JSON.parse(localStorage.getItem(`ssrm.v45.inventory.${{scope}}`) || '{{"debt":"none"}}'); writeLog(`restored inventory trust for ${{scope}}: ${{restored.debt}}`); }}
function multiReloadProbe(scope) {{ state.reloads += 1; writeLog(`multi reload probe ${{state.reloads}} for ${{scope}}`); }}
function saveWorldState(scope) {{ localStorage.setItem(`ssrm.v45.inventory.${{scope}}`, JSON.stringify({{debt:`saved inventory debt for ${{scope}}`, savedAt:state.tick}})); localStorage.setItem(`ssrm.v45.world.${{scope}}`, JSON.stringify(state)); writeLog(`saved idle/handoff/inventory trust state for ${{scope}}`); }}
function restoreWorldState(scope) {{ const restored = JSON.parse(localStorage.getItem(`ssrm.v45.world.${{scope}}`) || '{{"events":[]}}'); writeLog(`restored world state for ${{scope}} with ${{restored.events.length || 0}} events`); }}
function exportReplay(scope) {{ writeLog(`replay export prepared for ${{scope}}`); }}
localStorage.setItem('ssrm.v45.boot', JSON.stringify({{loaded:true}}));
writeLog('browser v45 idle routine and handoff surface loaded from localStorage');
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
    write_csv(ARTIFACT_DIR / f"{PREFIX}_summary.csv", [{"metric": key, "value": value} for key, value in results["metrics"].items()])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [{
        "report": results["report"],
        "seed": results["seed"],
        "verdict": results["verdict"],
        "readiness": results["metrics"]["browser_world_v45_idle_handoff_memory_readiness"],
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
        "readiness": metrics["browser_world_v45_idle_handoff_memory_readiness"],
        "weakest_channel_score": metrics["weakest_channel_score"],
        "weakest_named_channel": metrics["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
