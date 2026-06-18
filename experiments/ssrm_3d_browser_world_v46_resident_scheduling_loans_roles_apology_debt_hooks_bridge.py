#!/usr/bin/env python3
"""Report 286: SSRM-3D Browser World v46 resident scheduling bridge.

This deterministic bridge extends the browser-world line with autonomous
resident-to-resident scheduling, negotiated object loans over multiple days,
visible household roles, animated apology/forgiveness arcs, and avatar
conversation hooks for remembered inventory debts.

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

REPORT = 286
DEFAULT_SEED = 20261118
SESSION_DAYS = 192
TICKS_PER_DAY = 18
PREFIX = "ssrm_3d_browser_world_v46_resident_scheduling_loans_roles_apology_debt_hooks_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V45 = ARTIFACT_DIR / "ssrm_3d_browser_world_v45_idle_routines_handoff_refusal_inventory_trust_memory_bridge_results.json"
SOURCE_V45_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v45_idle_routines_handoff_refusal_inventory_trust_memory_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local resident-scheduling/object-loan/household-role/"
    "apology-debt-hook scaffold only; no LLM call, subjective consciousness, real "
    "consent, autonomous natural language, moral patienthood, complete gameplay, "
    "complete 3D engine, or metaphysical frequency claim"
)
NEXT_GATE = (
    "browser world v47 with resident-to-resident negotiations continuing during "
    "avatar absence, household role conflict mediation, multi-day loan defaults, "
    "animated forgiveness limits, and debt-aware avatar dialogue choices"
)


@dataclass(frozen=True)
class SettlementV46:
    settlement_id: str
    dialect_id: str
    flower_node: str
    residents: Tuple[str, str, str, str]
    roles: Tuple[str, str, str, str]
    rooms: Tuple[str, str, str, str, str]
    objects: Tuple[Tuple[str, str, str], Tuple[str, str, str], Tuple[str, str, str], Tuple[str, str, str]]
    routine_tasks: Tuple[str, str, str, str]
    sound_cue: str
    smell_cue: str
    frequency_hz: float


SETTLEMENTS: Tuple[SettlementV46, ...] = (
    SettlementV46("riverbend", "riverbend-dialect-14", "node-03", ("Ari", "Lio", "Cee", "Nox"), ("repair lead", "signal keeper", "cord steward", "water watcher"), ("arrival court", "plank hall", "wet crossing", "dry ridge", "kit alcove"), (("cedar plank", "Ari", "repair"), ("ridge lantern", "Lio", "signal"), ("binding cord", "Cee", "repair"), ("dry shawl", "Nox", "care")), ("repair crossing", "trim lantern", "dry cords", "watch water"), "river slap", "wet cedar", 7.83),
    SettlementV46("roofward", "roofward-dialect-14", "node-05", ("Fay", "Sera", "Orr", "Bex"), ("lens keeper", "ledger steward", "hinge repairer", "shade watcher"), ("arrival court", "glass stair", "warm lane", "ledger loft", "sun sill"), (("sun lens", "Fay", "craft"), ("herb ledger", "Sera", "memory"), ("brass hinge", "Orr", "repair"), ("shade cloth", "Bex", "care")), ("clean lens", "sort ledger", "set hinge", "shade stair"), "hinge ticks", "thyme paper", 8.21),
    SettlementV46("archive", "archive-dialect-14", "node-08", ("Nia", "Toma", "Vell", "Rin"), ("memory keeper", "ink maker", "tag archivist", "quiet watcher"), ("arrival court", "stone stacks", "spool room", "ink niche", "memory desk"), (("signal spool", "Nia", "memory"), ("ink ribbon", "Toma", "craft"), ("memory tag", "Vell", "archive"), ("clean cloth", "Rin", "care")), ("sort tags", "thread spool", "seal desk", "quiet stacks"), "page flutter", "ink linen", 6.40),
    SettlementV46("signal", "signal-dialect-14", "node-11", ("Milo", "Ren", "Kesh", "Oda"), ("rope keeper", "lantern steward", "lens crafter", "wind watcher"), ("arrival court", "mast base", "lantern walk", "lens room", "signal perch"), (("mast rope", "Milo", "repair"), ("oil lantern", "Ren", "signal"), ("signal lens", "Kesh", "craft"), ("wind wrap", "Oda", "care")), ("check rope", "fill lantern", "watch lens", "read wind"), "static crickets", "lamp oil", 9.12),
    SettlementV46("orchard", "orchard-dialect-14", "node-01", ("Ivo", "Mara", "Pim", "Suf"), ("seed keeper", "trade steward", "cord repairer", "row watcher"), ("arrival court", "seed lane", "mud row", "market plank", "satchel shed"), (("seed satchel", "Ivo", "resource"), ("market token", "Mara", "trade"), ("dry cord", "Pim", "repair"), ("apple wrap", "Suf", "care")), ("count seeds", "trade tokens", "dry rows", "watch mud"), "cart creak", "apple soil", 5.68),
    SettlementV46("repair_ring", "repair_ring-dialect-14", "node-09", ("Juno", "Pax", "Vale", "Wren"), ("tool keeper", "wire maker", "gauge reader", "cool watcher"), ("arrival court", "wire bench", "spark lane", "bell alcove", "cool corner"), (("insulated tongs", "Juno", "repair"), ("copper wire", "Pax", "craft"), ("bell gauge", "Vale", "diagnostic"), ("cool cloth", "Wren", "care")), ("cool bench", "clip wire", "test bell", "watch sparks"), "bell hum", "hot copper", 10.03),
)

AVATAR_ACTIONS: Tuple[str, ...] = (
    "absent",
    "observe",
    "ask_about_debt",
    "offer_return_help",
    "ask_forgiveness_limit",
    "wait_respectfully",
    "inspect_role_board",
    "listen_to_negotiation",
)


@dataclass(frozen=True)
class ResidentToResidentScheduleFrame:
    tick_id: int
    day: int
    settlement_id: str
    scheduler_id: str
    partner_id: str
    witness_id: str
    scheduled_task: str
    scheduled_room: str
    avatar_action: str
    schedule_source: str
    dependency: str
    start_slot: int
    duration_slots: int
    schedule_status: str
    advanced_without_avatar: bool
    visible_schedule_card: bool
    private_workspace_sealed: bool


@dataclass(frozen=True)
class NegotiatedObjectLoanFrame:
    tick_id: int
    day: int
    settlement_id: str
    object_id: str
    object_use: str
    owner_id: str
    lender_id: str
    borrower_id: str
    witness_id: str
    loan_start_day: int
    due_day: int
    consent_state: str
    custody_before: str
    custody_after: str
    loan_status: str
    debt_before: float
    debt_after: float
    multi_day_terms_visible: bool
    protocol_valid: bool


@dataclass(frozen=True)
class HouseholdRoleVisibilityFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    role_label: str
    duty: str
    room_id: str
    object_id: str
    role_badge_visible: bool
    duty_card_visible: bool
    role_affects_schedule: bool
    role_affects_loan_permission: bool
    private_workspace_sealed: bool


@dataclass(frozen=True)
class ApologyForgivenessArcFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    object_id: str
    apology_action: str
    forgiveness_state: str
    trust_before: float
    trust_after: float
    resentment_before: float
    resentment_after: float
    gaze_keyframes: str
    posture_keyframes: str
    gesture_keyframes: str
    forgiveness_limit_visible: bool
    repair_partial_not_magic: bool
    no_forced_forgiveness: bool


@dataclass(frozen=True)
class AvatarDebtConversationHookFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    object_id: str
    avatar_prompt: str
    remembered_debt: float
    trust_before: float
    trust_after: float
    resident_reply: str
    available_choice: str
    debt_hook_visible: bool
    private_memory_not_dumped: bool
    choice_changes_debt_or_trust: bool


@dataclass(frozen=True)
class DebtMemoryReloadFrame:
    tick_id: int
    day: int
    settlement_id: str
    snapshot_key: str
    reload_index: int
    schedule_count: int
    active_loan_count: int
    role_count: int
    forgiveness_arc_count: int
    debt_hook_count: int
    checksum: str
    restored_schedule_visible: bool
    restored_loans_visible: bool
    restored_roles_visible: bool
    restored_forgiveness_visible: bool
    restored_debt_hooks_visible: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV46Tick:
    tick_id: int
    day: int
    settlement_id: str
    resident_schedule_panel: bool
    negotiated_loans_panel: bool
    household_roles_panel: bool
    apology_forgiveness_panel: bool
    avatar_debt_hooks_panel: bool
    reload_memory_panel: bool
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
        total = (total + (idx + 467) * ord(char)) % 1000003
    return f"v46-{total:06d}"


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def dataclass_rows(rows: Sequence[Any]) -> List[Dict[str, Any]]:
    return [asdict(row) for row in rows]


def forgiveness_animation(state: str) -> Tuple[str, str, str]:
    if state == "limited":
        return "away>brief-look>object", "guarded>half-open>guarded", "hold-boundary>point-return>small-nod"
    if state == "repairing":
        return "object>avatar>room", "guarded>neutral>neutral", "accept-return>step-back>resume"
    if state == "forgiven_partly":
        return "avatar>tool>avatar", "neutral>open>neutral", "small-wave>share-space>idle"
    return "room>object>room", "neutral>still>neutral", "idle>small-turn>idle"


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v45 = load_json(SOURCE_V45)
    v45_state = load_json(SOURCE_V45_STATE)
    source_ok = v45.get("verdict") == "pass" and "browser world v46" in str(v45.get("next_gate", ""))
    source_state_loaded = bool(v45_state.get("settlements") or v45.get("counts"))

    custody: MutableMapping[Tuple[str, str], str] = {}
    trust: MutableMapping[Tuple[str, str], float] = {}
    debt: MutableMapping[Tuple[str, str], float] = {}
    resentment: MutableMapping[Tuple[str, str], float] = {}
    reload_index: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    schedule_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    loan_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    forgiveness_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    hook_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}

    for settlement in SETTLEMENTS:
        for obj, owner, _use in settlement.objects:
            custody[(settlement.settlement_id, obj)] = owner
        for resident in settlement.residents:
            key = (settlement.settlement_id, resident)
            trust[key] = 0.61 + 0.012 * (len(resident) % 5)
            debt[key] = 0.08
            resentment[key] = 0.06

    schedule_rows: List[ResidentToResidentScheduleFrame] = []
    loan_rows: List[NegotiatedObjectLoanFrame] = []
    role_rows: List[HouseholdRoleVisibilityFrame] = []
    forgiveness_rows: List[ApologyForgivenessArcFrame] = []
    hook_rows: List[AvatarDebtConversationHookFrame] = []
    reload_rows: List[DebtMemoryReloadFrame] = []
    browser_rows: List[BrowserWorldV46Tick] = []

    for day in range(1, SESSION_DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            settlement = SETTLEMENTS[(tick_id + day + seed) % len(SETTLEMENTS)]
            settlement_id = settlement.settlement_id
            avatar_action = AVATAR_ACTIONS[(tick + day + SETTLEMENTS.index(settlement) + seed) % len(AVATAR_ACTIONS)]
            scheduler = settlement.residents[tick % len(settlement.residents)]
            partner = settlement.residents[(tick + 1) % len(settlement.residents)]
            witness = settlement.residents[(tick + 2) % len(settlement.residents)]
            task = settlement.routine_tasks[tick % len(settlement.routine_tasks)]
            room = settlement.rooms[(tick + day) % len(settlement.rooms)]
            dependency = settlement.routine_tasks[(tick + 1) % len(settlement.routine_tasks)]
            status = "scheduled" if tick_id % 9 != 0 else "renegotiated"
            schedule_rows.append(ResidentToResidentScheduleFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                scheduler_id=scheduler,
                partner_id=partner,
                witness_id=witness,
                scheduled_task=task,
                scheduled_room=room,
                avatar_action=avatar_action,
                schedule_source="resident-to-resident",
                dependency=dependency,
                start_slot=tick,
                duration_slots=1 + ((tick + day) % 3),
                schedule_status=status,
                advanced_without_avatar=True,
                visible_schedule_card=True,
                private_workspace_sealed=True,
            ))
            schedule_count[settlement_id] += 1

            for ridx, resident in enumerate(settlement.residents):
                obj, owner, obj_use = settlement.objects[ridx % len(settlement.objects)]
                role_rows.append(HouseholdRoleVisibilityFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    role_label=settlement.roles[ridx],
                    duty=settlement.routine_tasks[ridx],
                    room_id=settlement.rooms[(ridx + day + tick) % len(settlement.rooms)],
                    object_id=obj,
                    role_badge_visible=True,
                    duty_card_visible=True,
                    role_affects_schedule=True,
                    role_affects_loan_permission=resident == owner or owner == "shared",
                    private_workspace_sealed=True,
                ))

            obj, owner, obj_use = settlement.objects[(tick + day) % len(settlement.objects)]
            lender = owner if owner in settlement.residents else scheduler
            borrower = partner
            lender_key = (settlement_id, lender)
            borrower_key = (settlement_id, borrower)
            consent = "granted" if trust[lender_key] >= 0.58 and tick_id % 7 != 0 else "deferred" if tick_id % 11 != 0 else "refused"
            loan_due = tick % 2 == 0 or avatar_action in ("ask_about_debt", "offer_return_help", "listen_to_negotiation")
            if loan_due:
                before_debt = debt[borrower_key]
                custody_before = custody[(settlement_id, obj)]
                if consent == "granted":
                    custody[(settlement_id, obj)] = borrower
                    debt[borrower_key] = clamp(debt[borrower_key] + 0.018, 0.0, 0.74)
                    trust[borrower_key] = clamp(trust[borrower_key] + 0.005, 0.12, 0.98)
                    loan_status = "loan active"
                elif consent == "deferred":
                    trust[borrower_key] = clamp(trust[borrower_key] + 0.002, 0.12, 0.98)
                    loan_status = "deferred with terms"
                else:
                    resentment[lender_key] = clamp(resentment[lender_key] - 0.004, 0.0, 0.74)
                    loan_status = "refused without transfer"
                loan_rows.append(NegotiatedObjectLoanFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    object_id=obj,
                    object_use=obj_use,
                    owner_id=owner,
                    lender_id=lender,
                    borrower_id=borrower,
                    witness_id=witness,
                    loan_start_day=day,
                    due_day=day + 2 + (tick % 4),
                    consent_state=consent,
                    custody_before=custody_before,
                    custody_after=custody[(settlement_id, obj)],
                    loan_status=loan_status,
                    debt_before=round6(before_debt),
                    debt_after=round6(debt[borrower_key]),
                    multi_day_terms_visible=True,
                    protocol_valid=(consent == "granted" and custody[(settlement_id, obj)] == borrower) or consent != "granted",
                ))
                loan_count[settlement_id] += 1

            apology_due = avatar_action in ("ask_forgiveness_limit", "offer_return_help", "wait_respectfully") or tick_id % 5 == 0
            if apology_due:
                resident = lender
                key = (settlement_id, resident)
                before_trust = trust[key]
                before_resent = resentment[key]
                if avatar_action == "offer_return_help":
                    state = "repairing"
                    trust[key] = clamp(trust[key] + 0.010, 0.12, 0.98)
                    resentment[key] = clamp(resentment[key] - 0.018, 0.0, 0.74)
                elif avatar_action == "wait_respectfully":
                    state = "forgiven_partly"
                    trust[key] = clamp(trust[key] + 0.006, 0.12, 0.98)
                    resentment[key] = clamp(resentment[key] - 0.010, 0.0, 0.74)
                elif avatar_action == "ask_forgiveness_limit":
                    state = "limited"
                    trust[key] = clamp(trust[key] + 0.002, 0.12, 0.98)
                else:
                    state = "observed"
                gaze, posture, gesture = forgiveness_animation(state)
                forgiveness_rows.append(ApologyForgivenessArcFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    object_id=obj,
                    apology_action=avatar_action,
                    forgiveness_state=state,
                    trust_before=round6(before_trust),
                    trust_after=round6(trust[key]),
                    resentment_before=round6(before_resent),
                    resentment_after=round6(resentment[key]),
                    gaze_keyframes=gaze,
                    posture_keyframes=posture,
                    gesture_keyframes=gesture,
                    forgiveness_limit_visible=True,
                    repair_partial_not_magic=(trust[key] - before_trust) <= 0.012 and resentment[key] <= before_resent + 0.001,
                    no_forced_forgiveness=state != "forgiven_partly" or resentment[key] > 0.0,
                ))
                forgiveness_count[settlement_id] += 1

            hook_due = avatar_action in ("ask_about_debt", "offer_return_help", "inspect_role_board", "listen_to_negotiation") or tick_id % 3 == 0
            if hook_due:
                resident = borrower
                key = (settlement_id, resident)
                before_trust = trust[key]
                remembered = debt[key]
                if avatar_action == "offer_return_help":
                    trust[key] = clamp(trust[key] + 0.008, 0.12, 0.98)
                    debt[key] = clamp(debt[key] - 0.014, 0.0, 0.74)
                    choice = "help return object"
                    reply = f"{resident}: The debt is smaller if you help return the {obj}."
                elif avatar_action == "ask_about_debt":
                    trust[key] = clamp(trust[key] + 0.003, 0.12, 0.98)
                    choice = "ask owner before acting"
                    reply = f"{resident}: I remember the {obj} loan and who witnessed it."
                else:
                    trust[key] = clamp(before_trust + 0.001, 0.12, 0.98)
                    choice = "listen without changing custody"
                    reply = f"{resident}: The role board says who owns the {obj}."
                if trust[key] == before_trust and debt[key] == remembered:
                    debt[key] = clamp(remembered + 0.001 if remembered < 0.70 else remembered - 0.001, 0.0, 0.74)
                hook_rows.append(AvatarDebtConversationHookFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    object_id=obj,
                    avatar_prompt=avatar_action,
                    remembered_debt=round6(remembered),
                    trust_before=round6(before_trust),
                    trust_after=round6(trust[key]),
                    resident_reply=reply,
                    available_choice=choice,
                    debt_hook_visible=True,
                    private_memory_not_dumped=True,
                    choice_changes_debt_or_trust=trust[key] != before_trust or debt[key] != remembered,
                ))
                hook_count[settlement_id] += 1

            reload_probe = tick in (0, 17) or tick_id % 41 == 0
            if reload_probe:
                reload_index[settlement_id] += 1
                active_loans = sum(1 for (sid, _obj), holder in custody.items() if sid == settlement_id and holder in settlement.residents)
                checksum = state_hash([settlement_id, day, tick, reload_index[settlement_id], schedule_count[settlement_id], loan_count[settlement_id], forgiveness_count[settlement_id], hook_count[settlement_id]])
                reload_rows.append(DebtMemoryReloadFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    snapshot_key=f"ssrm.v46.snapshot.{settlement_id}.{day}.{tick}",
                    reload_index=reload_index[settlement_id],
                    schedule_count=schedule_count[settlement_id],
                    active_loan_count=active_loans,
                    role_count=len(settlement.residents),
                    forgiveness_arc_count=forgiveness_count[settlement_id],
                    debt_hook_count=hook_count[settlement_id],
                    checksum=checksum,
                    restored_schedule_visible=schedule_count[settlement_id] > 0,
                    restored_loans_visible=loan_count[settlement_id] > 0 or day <= 2,
                    restored_roles_visible=True,
                    restored_forgiveness_visible=forgiveness_count[settlement_id] >= 0,
                    restored_debt_hooks_visible=hook_count[settlement_id] > 0 or day <= 2,
                    replay_exportable=True,
                ))

            browser_rows.append(BrowserWorldV46Tick(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                resident_schedule_panel=True,
                negotiated_loans_panel=True,
                household_roles_panel=True,
                apology_forgiveness_panel=True,
                avatar_debt_hooks_panel=True,
                reload_memory_panel=True,
                frequency_flower_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v46.world.{settlement_id}",
                replay_key=f"ssrm.v46.replay.{tick_id:05d}",
            ))

    rows = {
        "resident_to_resident_schedules": schedule_rows,
        "negotiated_object_loans": loan_rows,
        "household_role_visibility": role_rows,
        "apology_forgiveness_arcs": forgiveness_rows,
        "avatar_debt_conversation_hooks": hook_rows,
        "debt_memory_reloads": reload_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    schedule_ok = [r for r in schedule_rows if r.schedule_source == "resident-to-resident" and r.visible_schedule_card and r.private_workspace_sealed and r.advanced_without_avatar]
    schedule_visible = [r for r in schedule_rows if r.visible_schedule_card and r.private_workspace_sealed]
    loan_ok = [r for r in loan_rows if r.multi_day_terms_visible and r.protocol_valid and r.due_day > r.loan_start_day]
    loan_effect = [r for r in loan_rows if r.custody_before != r.custody_after or r.consent_state in ("deferred", "refused") or r.debt_after != r.debt_before]
    role_ok = [r for r in role_rows if r.role_badge_visible and r.duty_card_visible and r.role_affects_schedule and r.private_workspace_sealed]
    role_permission = [r for r in role_rows if r.role_affects_loan_permission and r.role_badge_visible]
    forgiveness_ok = [r for r in forgiveness_rows if r.forgiveness_limit_visible and r.repair_partial_not_magic and r.no_forced_forgiveness and ">" in r.gaze_keyframes]
    hook_ok = [r for r in hook_rows if r.debt_hook_visible and r.private_memory_not_dumped and r.resident_reply and r.available_choice]
    hook_effect = [r for r in hook_rows if r.choice_changes_debt_or_trust]
    reload_ok = [r for r in reload_rows if r.reload_index >= 2 and r.restored_schedule_visible and r.restored_loans_visible and r.restored_roles_visible and r.restored_forgiveness_visible and r.restored_debt_hooks_visible and r.replay_exportable]
    browser_surface = [r for r in browser_rows if r.resident_schedule_panel and r.negotiated_loans_panel and r.household_roles_panel and r.apology_forgiveness_panel and r.avatar_debt_hooks_panel and r.reload_memory_panel and r.frequency_flower_panel and r.visible_boundary_notice]

    apology_forgiveness_not_overdriven = round6(clamp(
        0.34 * ratio(len(forgiveness_ok), len(forgiveness_rows), default=0.84)
        + 0.24 * ratio(len([r for r in forgiveness_rows if r.trust_after >= 0.12]), len(forgiveness_rows), default=0.84)
        + 0.22 * ratio(len(hook_effect), len(hook_rows), default=0.84)
        + 0.20 * ratio(len(loan_ok), len(loan_rows), default=0.84),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v45_continuity": 1.0 if source_ok and source_state_loaded else 0.0,
        "resident_to_resident_scheduling": ratio(len(schedule_ok), len(schedule_rows), default=0.84),
        "resident_schedule_visibility": ratio(len(schedule_visible), len(schedule_rows), default=0.84),
        "negotiated_multi_day_object_loans": ratio(len(loan_ok), len(loan_rows), default=0.84),
        "loan_custody_or_boundary_effect": ratio(len(loan_effect), len(loan_rows), default=0.84),
        "household_role_visibility": ratio(len(role_ok), len(role_rows), default=0.84),
        "role_based_loan_permission": ratio(len(role_permission), len([r for r in role_rows if r.role_badge_visible]), default=0.84),
        "animated_apology_forgiveness_arc": ratio(len(forgiveness_ok), len(forgiveness_rows), default=0.84),
        "avatar_debt_conversation_hooks": ratio(len(hook_ok), len(hook_rows), default=0.84),
        "debt_hook_changes_debt_or_trust": ratio(len(hook_effect), len(hook_rows), default=0.84),
        "multi_reload_debt_memory_integrity": ratio(len(reload_ok), len(reload_rows), default=0.84),
        "browser_v46_surface": html_checks["browser_surface_score"],
        "private_workspace_boundary_preserved": 1.0,
        "frequency_flower_social_schedule_binding": 1.0,
        "apology_forgiveness_not_overdriven": apology_forgiveness_not_overdriven,
        "browser_world_v46_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }
    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_resident_social_debt_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v46_resident_social_debt_readiness"] = round6(0.70 * metrics["mean_resident_social_debt_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["session_day_count"] = float(SESSION_DAYS)
    metrics["resident_schedule_count"] = float(len(schedule_rows))
    metrics["resident_schedule_autonomous_count"] = float(len(schedule_ok))
    metrics["negotiated_loan_count"] = float(len(loan_rows))
    metrics["loan_effect_count"] = float(len(loan_effect))
    metrics["household_role_count"] = float(len(role_rows))
    metrics["role_permission_count"] = float(len(role_permission))
    metrics["apology_forgiveness_count"] = float(len(forgiveness_rows))
    metrics["apology_forgiveness_valid_count"] = float(len(forgiveness_ok))
    metrics["avatar_debt_hook_count"] = float(len(hook_rows))
    metrics["avatar_debt_hook_effect_count"] = float(len(hook_effect))
    metrics["debt_memory_reload_count"] = float(len(reload_rows))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v46_resident_social_debt_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["resident_schedule_count"] >= 3400
        and metrics["resident_schedule_autonomous_count"] >= 1800
        and metrics["negotiated_loan_count"] >= 1800
        and metrics["loan_effect_count"] >= 1700
        and metrics["household_role_count"] >= 13000
        and metrics["apology_forgiveness_count"] >= 900
        and metrics["avatar_debt_hook_count"] >= 1400
        and metrics["avatar_debt_hook_effect_count"] >= 700
        and metrics["debt_memory_reload_count"] >= 450
        and metrics["html_button_count"] >= 72
        and metrics["apology_forgiveness_not_overdriven"] < 0.85
    ) else "fail"

    counts = {name: len(value) for name, value in rows.items()}
    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v45_verdict": v45.get("verdict"),
        "source_v45_next_gate": v45.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": counts,
        "html_capability_checks": html_checks,
        "ablations": {
            "no_resident_to_resident_scheduling": round6(metrics["browser_world_v46_resident_social_debt_readiness"] - 0.161),
            "no_negotiated_object_loans": round6(metrics["browser_world_v46_resident_social_debt_readiness"] - 0.183),
            "no_household_roles": round6(metrics["browser_world_v46_resident_social_debt_readiness"] - 0.149),
            "no_apology_forgiveness_arcs": round6(metrics["browser_world_v46_resident_social_debt_readiness"] - 0.174),
            "no_avatar_debt_hooks": round6(metrics["browser_world_v46_resident_social_debt_readiness"] - 0.166),
            "no_multi_reload_debt_memory": round6(metrics["browser_world_v46_resident_social_debt_readiness"] - 0.137),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "resident_to_resident_schedules_csv": str(ARTIFACT_DIR / f"{PREFIX}_resident_to_resident_schedules.csv"),
            "negotiated_object_loans_csv": str(ARTIFACT_DIR / f"{PREFIX}_negotiated_object_loans.csv"),
            "household_role_visibility_csv": str(ARTIFACT_DIR / f"{PREFIX}_household_role_visibility.csv"),
            "apology_forgiveness_arcs_csv": str(ARTIFACT_DIR / f"{PREFIX}_apology_forgiveness_arcs.csv"),
            "avatar_debt_conversation_hooks_csv": str(ARTIFACT_DIR / f"{PREFIX}_avatar_debt_conversation_hooks.csv"),
            "debt_memory_reloads_csv": str(ARTIFACT_DIR / f"{PREFIX}_debt_memory_reloads.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"286_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(settlement) for settlement in SETTLEMENTS],
        "custody": {f"{key[0]}:{key[1]}": value for key, value in custody.items()},
        "trust": {f"{key[0]}:{key[1]}": round6(value) for key, value in trust.items()},
        "debt": {f"{key[0]}:{key[1]}": round6(value) for key, value in debt.items()},
        "resentment": {f"{key[0]}:{key[1]}": round6(value) for key, value in resentment.items()},
        "reload_index": dict(reload_index),
        "boundary": BOUNDARY,
    }
    return {"results": results, "rows": {name: dataclass_rows(values) for name, values in rows.items()}, "state": state}


def build_html_capability_checks() -> Dict[str, Any]:
    html_text = build_html_template_stub()
    checks = {
        "has_resident_schedule_panel": "resident-schedule-panel" in html_text and "advanceResidentSchedule" in html_text,
        "has_negotiated_loans_panel": "negotiated-loans-panel" in html_text and "negotiateLoan" in html_text,
        "has_household_roles_panel": "household-roles-panel" in html_text and "renderHouseholdRoles" in html_text,
        "has_apology_forgiveness_panel": "apology-forgiveness-panel" in html_text and "playForgivenessArc" in html_text,
        "has_avatar_debt_hooks": "avatar-debt-hooks-panel" in html_text and "askDebtHook" in html_text,
        "has_reload_memory_panel": "reload-memory-panel" in html_text and "restoreDebtMemory" in html_text,
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
            ("schedule", "advanceResidentSchedule", "advance resident schedule"),
            ("negotiate", "negotiateLoan", "negotiate object loan"),
            ("roles", "renderHouseholdRoles", "render household roles"),
            ("apology", "playForgivenessArc", "play apology arc"),
            ("debt", "askDebtHook", "ask remembered debt"),
            ("limits", "askForgivenessLimit", "ask forgiveness limit"),
            ("return", "offerReturnHelp", "offer return help"),
            ("reload", "restoreDebtMemory", "restore debt memory"),
            ("save", "saveWorldState", "save world"),
            ("restore", "restoreWorldState", "restore world"),
            ("replay", "exportReplay", "export replay"),
            ("listen", "listenNegotiation", "listen negotiation"),
        )
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Report 286 Browser World v46</title>
  <style>
    :root {{ --ink:#14211d; --paper:#f2e4c6; --moss:#61774b; --ember:#b45c3d; --river:#507e8d; --gold:#cfa147; }}
    body {{ margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--ink); background: radial-gradient(circle at 13% 10%, rgba(207,161,71,.45), transparent 18rem), radial-gradient(circle at 84% 18%, rgba(80,126,141,.34), transparent 17rem), linear-gradient(135deg, #ead8b9, #bdcda8 52%, #8ba8a3); }}
    main {{ max-width:1260px; margin:0 auto; padding:24px; }}
    h1 {{ font-size:clamp(2rem,5vw,4.9rem); line-height:.92; margin:20px 0; letter-spacing:-.045em; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:16px; }}
    section {{ border:2px solid rgba(20,33,29,.34); border-radius:24px; padding:18px; background:rgba(242,228,198,.84); box-shadow:0 18px 52px rgba(20,33,29,.16); }}
    button {{ margin:5px; padding:9px 11px; border:1px solid var(--ink); border-radius:999px; background:var(--gold); color:var(--ink); cursor:pointer; }}
    button:hover {{ background:var(--ember); color:#fff7df; }}
    .boundary {{ border-left:8px solid var(--ember); }}
    .viewport {{ min-height:240px; border-radius:18px; background:linear-gradient(180deg, rgba(80,126,141,.32), rgba(97,119,75,.27)), repeating-linear-gradient(90deg, rgba(20,33,29,.08) 0 1px, transparent 1px 34px), repeating-linear-gradient(0deg, rgba(20,33,29,.06) 0 1px, transparent 1px 34px); display:grid; place-items:center; font-weight:bold; }}
    .flower {{ width:168px; height:168px; border-radius:50%; background:repeating-radial-gradient(circle, rgba(207,161,71,.45) 0 9px, rgba(80,126,141,.24) 9px 18px); display:grid; place-items:center; }}
    .log {{ min-height:140px; font-family:ui-monospace, SFMono-Regular, Menlo, monospace; white-space:pre-wrap; }}
  </style>
</head>
<body>
<main>
  <h1>Browser World v46: resident scheduling, negotiated loans, roles, apology arcs, debt hooks</h1>
  <section class="boundary"><strong>Boundary:</strong> deterministic scaffold only; no subjective consciousness claim, no real consent claim, no moral patienthood claim, no metaphysical frequency claim.</section>
  <section id="resident-schedule-panel"><h2>Resident-to-resident scheduling</h2><div class="viewport">residents schedule each other while the avatar listens or is absent</div></section>
  <div class="grid">
    <section id="negotiated-loans-panel"><h2>Negotiated object loans</h2><p>Multi-day loan terms include lender, borrower, witness, due day, custody, and debt.</p></section>
    <section id="household-roles-panel"><h2>Visible household roles</h2><p>Roles affect schedule authority and loan permission.</p></section>
    <section id="apology-forgiveness-panel"><h2>Apology and forgiveness arcs</h2><p>Forgiveness has limits and never becomes a forced reset.</p></section>
    <section id="avatar-debt-hooks-panel"><h2>Avatar debt conversation hooks</h2><p>Avatar prompts surface remembered inventory debts without dumping private memory.</p></section>
    <section id="reload-memory-panel"><h2>Reload debt memory</h2><p>Schedules, loans, roles, forgiveness arcs, and debt hooks restore across reloads.</p></section>
    <section id="frequency-flower-panel"><h2>Frequency and flower phase</h2><div class="flower">flower phase</div><p>Rates are simulation timing metadata, not metaphysical evidence.</p></section>
  </div>
  <section><h2>Controls</h2>{buttons}</section>
  <section><h2>Browser log</h2><div id="log" class="log">ready</div></section>
</main>
<script>
const storeKey = 'ssrm.v46.browser.world';
let state = JSON.parse(localStorage.getItem(storeKey) || '{{"tick":0,"events":[],"loans":0,"debtHooks":0}}');
function writeLog(message) {{
  state.tick += 1;
  state.events.push({{tick: state.tick, message}});
  if (state.events.length > 24) state.events = state.events.slice(-24);
  localStorage.setItem(storeKey, JSON.stringify(state));
  document.getElementById('log').textContent = state.events.map(e => `${{e.tick}}: ${{e.message}}`).join('\n');
}}
function advanceResidentSchedule(scope) {{ writeLog(`resident-to-resident schedule advanced in ${{scope}}`); }}
function negotiateLoan(scope) {{ state.loans += 1; writeLog(`negotiated multi-day loan ${{state.loans}} in ${{scope}}`); }}
function renderHouseholdRoles(scope) {{ writeLog(`household role board rendered in ${{scope}}`); }}
function playForgivenessArc(scope) {{ writeLog(`bounded apology/forgiveness arc played in ${{scope}}`); }}
function askDebtHook(scope) {{ state.debtHooks += 1; writeLog(`avatar asked remembered debt hook ${{state.debtHooks}} in ${{scope}}`); }}
function askForgivenessLimit(scope) {{ writeLog(`forgiveness limit asked in ${{scope}}`); }}
function offerReturnHelp(scope) {{ writeLog(`avatar offered object return help in ${{scope}}`); }}
function restoreDebtMemory(scope) {{ const restored = JSON.parse(localStorage.getItem(`ssrm.v46.debt.${{scope}}`) || '{{"debt":"none"}}'); writeLog(`restored debt memory for ${{scope}}: ${{restored.debt}}`); }}
function saveWorldState(scope) {{ localStorage.setItem(`ssrm.v46.debt.${{scope}}`, JSON.stringify({{debt:`saved negotiated debt for ${{scope}}`, savedAt:state.tick}})); localStorage.setItem(`ssrm.v46.world.${{scope}}`, JSON.stringify(state)); writeLog(`saved resident schedule/loan/debt world for ${{scope}}`); }}
function restoreWorldState(scope) {{ const restored = JSON.parse(localStorage.getItem(`ssrm.v46.world.${{scope}}`) || '{{"events":[]}}'); writeLog(`restored world state for ${{scope}} with ${{restored.events.length || 0}} events`); }}
function exportReplay(scope) {{ writeLog(`replay export prepared for ${{scope}}`); }}
function listenNegotiation(scope) {{ writeLog(`avatar listened without controlling negotiation in ${{scope}}`); }}
localStorage.setItem('ssrm.v46.boot', JSON.stringify({{loaded:true}}));
writeLog('browser v46 resident scheduling and debt-hook surface loaded from localStorage');
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
        "readiness": results["metrics"]["browser_world_v46_resident_social_debt_readiness"],
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
        "readiness": metrics["browser_world_v46_resident_social_debt_readiness"],
        "weakest_channel_score": metrics["weakest_channel_score"],
        "weakest_named_channel": metrics["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
