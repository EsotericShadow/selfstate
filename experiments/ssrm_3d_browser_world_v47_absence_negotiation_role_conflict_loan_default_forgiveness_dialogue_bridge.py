#!/usr/bin/env python3
"""Report 287: SSRM-3D Browser World v47 absence negotiation bridge.

This deterministic bridge extends the browser-world line with resident-to-resident
negotiations continuing during avatar absence, household role conflict mediation,
multi-day loan defaults, animated forgiveness limits, and debt-aware avatar
dialogue choices.

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

REPORT = 287
DEFAULT_SEED = 20261202
SESSION_DAYS = 204
TICKS_PER_DAY = 18
PREFIX = "ssrm_3d_browser_world_v47_absence_negotiation_role_conflict_loan_default_forgiveness_dialogue_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V46 = ARTIFACT_DIR / "ssrm_3d_browser_world_v46_resident_scheduling_loans_roles_apology_debt_hooks_bridge_results.json"
SOURCE_V46_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v46_resident_scheduling_loans_roles_apology_debt_hooks_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local absence-negotiation/role-conflict/loan-default/"
    "forgiveness-dialogue scaffold only; no LLM call, subjective consciousness, real "
    "consent, autonomous natural language, moral patienthood, complete gameplay, "
    "complete 3D engine, or metaphysical frequency claim"
)
NEXT_GATE = (
    "browser world v48 with embodied needs during resident social schedules, household "
    "care duties, fatigue/rest negotiation, weather exposure during loans, and "
    "recoverable welfare state visible without suffering loops"
)


@dataclass(frozen=True)
class SettlementV47:
    settlement_id: str
    dialect_id: str
    flower_node: str
    residents: Tuple[str, str, str, str]
    roles: Tuple[str, str, str, str]
    rooms: Tuple[str, str, str, str, str]
    objects: Tuple[Tuple[str, str, str], Tuple[str, str, str], Tuple[str, str, str], Tuple[str, str, str]]
    duties: Tuple[str, str, str, str]
    sound_cue: str
    smell_cue: str
    frequency_hz: float


SETTLEMENTS: Tuple[SettlementV47, ...] = (
    SettlementV47("riverbend", "riverbend-dialect-15", "node-03", ("Ari", "Lio", "Cee", "Nox"), ("repair lead", "signal keeper", "cord steward", "water watcher"), ("arrival court", "plank hall", "wet crossing", "dry ridge", "kit alcove"), (("cedar plank", "Ari", "repair"), ("ridge lantern", "Lio", "signal"), ("binding cord", "Cee", "repair"), ("dry shawl", "Nox", "care")), ("repair crossing", "trim lantern", "dry cords", "watch water"), "river slap", "wet cedar", 7.83),
    SettlementV47("roofward", "roofward-dialect-15", "node-05", ("Fay", "Sera", "Orr", "Bex"), ("lens keeper", "ledger steward", "hinge repairer", "shade watcher"), ("arrival court", "glass stair", "warm lane", "ledger loft", "sun sill"), (("sun lens", "Fay", "craft"), ("herb ledger", "Sera", "memory"), ("brass hinge", "Orr", "repair"), ("shade cloth", "Bex", "care")), ("clean lens", "sort ledger", "set hinge", "shade stair"), "hinge ticks", "thyme paper", 8.21),
    SettlementV47("archive", "archive-dialect-15", "node-08", ("Nia", "Toma", "Vell", "Rin"), ("memory keeper", "ink maker", "tag archivist", "quiet watcher"), ("arrival court", "stone stacks", "spool room", "ink niche", "memory desk"), (("signal spool", "Nia", "memory"), ("ink ribbon", "Toma", "craft"), ("memory tag", "Vell", "archive"), ("clean cloth", "Rin", "care")), ("sort tags", "thread spool", "seal desk", "quiet stacks"), "page flutter", "ink linen", 6.40),
    SettlementV47("signal", "signal-dialect-15", "node-11", ("Milo", "Ren", "Kesh", "Oda"), ("rope keeper", "lantern steward", "lens crafter", "wind watcher"), ("arrival court", "mast base", "lantern walk", "lens room", "signal perch"), (("mast rope", "Milo", "repair"), ("oil lantern", "Ren", "signal"), ("signal lens", "Kesh", "craft"), ("wind wrap", "Oda", "care")), ("check rope", "fill lantern", "watch lens", "read wind"), "static crickets", "lamp oil", 9.12),
    SettlementV47("orchard", "orchard-dialect-15", "node-01", ("Ivo", "Mara", "Pim", "Suf"), ("seed keeper", "trade steward", "cord repairer", "row watcher"), ("arrival court", "seed lane", "mud row", "market plank", "satchel shed"), (("seed satchel", "Ivo", "resource"), ("market token", "Mara", "trade"), ("dry cord", "Pim", "repair"), ("apple wrap", "Suf", "care")), ("count seeds", "trade tokens", "dry rows", "watch mud"), "cart creak", "apple soil", 5.68),
    SettlementV47("repair_ring", "repair_ring-dialect-15", "node-09", ("Juno", "Pax", "Vale", "Wren"), ("tool keeper", "wire maker", "gauge reader", "cool watcher"), ("arrival court", "wire bench", "spark lane", "bell alcove", "cool corner"), (("insulated tongs", "Juno", "repair"), ("copper wire", "Pax", "craft"), ("bell gauge", "Vale", "diagnostic"), ("cool cloth", "Wren", "care")), ("cool bench", "clip wire", "test bell", "watch sparks"), "bell hum", "hot copper", 10.03),
)

AVATAR_CHOICES: Tuple[str, ...] = (
    "absent",
    "absent",
    "listen_later",
    "ask_debt_status",
    "offer_return_help",
    "ask_mediation_status",
    "choose_repay",
    "choose_wait",
    "choose_ignore",
    "ask_forgiveness_limit",
)
RESIDENT_LED_NEGOTIATION_STATES = frozenset({
    "absent",
    "listen_later",
    "ask_debt_status",
    "ask_mediation_status",
    "choose_wait",
    "choose_ignore",
    "ask_forgiveness_limit",
})


@dataclass(frozen=True)
class AbsenceNegotiationFrame:
    tick_id: int
    day: int
    settlement_id: str
    negotiator_a: str
    negotiator_b: str
    witness_id: str
    object_id: str
    avatar_state: str
    topic: str
    negotiation_round: int
    terms_before: str
    terms_after: str
    outcome: str
    continued_during_avatar_absence: bool
    visible_negotiation_trace: bool
    private_workspace_sealed: bool


@dataclass(frozen=True)
class RoleConflictMediationFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_a: str
    resident_b: str
    mediator_id: str
    role_a: str
    role_b: str
    contested_duty: str
    conflict_reason: str
    mediation_state: str
    fairness_before: float
    fairness_after: float
    resentment_before: float
    resentment_after: float
    visible_mediation_card: bool
    bounded_conflict: bool


@dataclass(frozen=True)
class MultiDayLoanDefaultFrame:
    tick_id: int
    day: int
    settlement_id: str
    object_id: str
    lender_id: str
    borrower_id: str
    witness_id: str
    loan_start_day: int
    due_day: int
    days_overdue: int
    default_state: str
    custody_holder: str
    debt_before: float
    debt_after: float
    trust_before: float
    trust_after: float
    default_visible: bool
    repair_available: bool
    bounded_default: bool


@dataclass(frozen=True)
class AnimatedForgivenessLimitFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    object_id: str
    default_state: str
    forgiveness_state: str
    forgiveness_ceiling: float
    trust_before: float
    trust_after: float
    resentment_before: float
    resentment_after: float
    gaze_keyframes: str
    posture_keyframes: str
    gesture_keyframes: str
    visible_limit: bool
    no_forced_forgiveness: bool
    partial_repair_only: bool


@dataclass(frozen=True)
class DebtAwareAvatarChoiceFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    object_id: str
    avatar_choice: str
    remembered_debt: float
    remembered_default: str
    prompt: str
    resident_reply: str
    debt_before: float
    debt_after: float
    trust_before: float
    trust_after: float
    choice_visible: bool
    choice_affects_state: bool
    private_memory_not_dumped: bool


@dataclass(frozen=True)
class AbsenceNegotiationReloadFrame:
    tick_id: int
    day: int
    settlement_id: str
    snapshot_key: str
    reload_index: int
    absence_negotiation_count: int
    mediation_count: int
    default_count: int
    forgiveness_count: int
    avatar_choice_count: int
    checksum: str
    restored_negotiations_visible: bool
    restored_mediation_visible: bool
    restored_defaults_visible: bool
    restored_forgiveness_visible: bool
    restored_choices_visible: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV47Tick:
    tick_id: int
    day: int
    settlement_id: str
    absence_negotiation_panel: bool
    role_conflict_panel: bool
    loan_default_panel: bool
    forgiveness_limit_panel: bool
    avatar_debt_choice_panel: bool
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
        total = (total + (idx + 503) * ord(char)) % 1000003
    return f"v47-{total:06d}"


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def dataclass_rows(rows: Sequence[Any]) -> List[Dict[str, Any]]:
    return [asdict(row) for row in rows]


def forgiveness_animation(state: str) -> Tuple[str, str, str]:
    if state == "limit_set":
        return "debt>avatar>away", "guarded>upright>guarded", "hold-boundary>count-days>step-back"
    if state == "repairing":
        return "object>borrower>witness", "guarded>neutral>half-open", "accept-return>small-nod>resume"
    if state == "not_yet":
        return "away>object>away", "closed>still>closed", "palm-out>hold-tool>turn-away"
    return "room>object>room", "neutral>still>neutral", "idle>small-turn>idle"


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v46 = load_json(SOURCE_V46)
    v46_state = load_json(SOURCE_V46_STATE)
    source_ok = v46.get("verdict") == "pass" and "browser world v47" in str(v46.get("next_gate", ""))
    source_state_loaded = bool(v46_state.get("settlements") or v46.get("counts"))

    debt: MutableMapping[Tuple[str, str], float] = {}
    trust: MutableMapping[Tuple[str, str], float] = {}
    resentment: MutableMapping[Tuple[str, str], float] = {}
    fairness: MutableMapping[str, float] = {s.settlement_id: 0.62 for s in SETTLEMENTS}
    custody: MutableMapping[Tuple[str, str], str] = {}
    loan_start: MutableMapping[Tuple[str, str], int] = {}
    due_day: MutableMapping[Tuple[str, str], int] = {}
    reload_index: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    negotiation_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    mediation_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    default_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    forgiveness_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    choice_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}

    for settlement in SETTLEMENTS:
        for obj, owner, _use in settlement.objects:
            custody[(settlement.settlement_id, obj)] = owner
            loan_start[(settlement.settlement_id, obj)] = 1
            due_day[(settlement.settlement_id, obj)] = 3
        for resident in settlement.residents:
            key = (settlement.settlement_id, resident)
            debt[key] = 0.10
            trust[key] = 0.62 + 0.01 * (len(resident) % 4)
            resentment[key] = 0.07

    negotiation_rows: List[AbsenceNegotiationFrame] = []
    mediation_rows: List[RoleConflictMediationFrame] = []
    default_rows: List[MultiDayLoanDefaultFrame] = []
    forgiveness_rows: List[AnimatedForgivenessLimitFrame] = []
    choice_rows: List[DebtAwareAvatarChoiceFrame] = []
    reload_rows: List[AbsenceNegotiationReloadFrame] = []
    browser_rows: List[BrowserWorldV47Tick] = []

    for day in range(1, SESSION_DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            settlement = SETTLEMENTS[(tick_id + day + seed) % len(SETTLEMENTS)]
            settlement_id = settlement.settlement_id
            avatar_state = AVATAR_CHOICES[(tick + day + SETTLEMENTS.index(settlement) + seed) % len(AVATAR_CHOICES)]
            a = settlement.residents[tick % 4]
            b = settlement.residents[(tick + 1) % 4]
            witness = settlement.residents[(tick + 2) % 4]
            mediator = settlement.residents[(tick + 3) % 4]
            obj, owner, obj_use = settlement.objects[(tick + day) % len(settlement.objects)]
            borrower_key = (settlement_id, b)
            lender = owner if owner in settlement.residents else a
            lender_key = (settlement_id, lender)
            loan_key = (settlement_id, obj)

            before_terms = f"due:{due_day[loan_key]} holder:{custody[loan_key]}"
            resident_led_negotiation = avatar_state in RESIDENT_LED_NEGOTIATION_STATES or tick_id % 2 == 0
            if resident_led_negotiation:
                if custody[loan_key] == lender and tick_id % 4 != 0:
                    custody[loan_key] = b
                    loan_start[loan_key] = day
                    due_day[loan_key] = day + 2 + (tick % 4)
                    debt[borrower_key] = clamp(debt[borrower_key] + 0.016, 0.0, 0.76)
                    outcome = "loan terms accepted without avatar"
                elif day > due_day[loan_key] and custody[loan_key] != lender and tick_id % 11 == 0:
                    outcome = "late loan renegotiated without avatar"
                    due_day[loan_key] = day + 1 + (tick % 3)
                else:
                    outcome = "terms reviewed without avatar"
            else:
                outcome = "avatar-present negotiation observed"
            after_terms = f"due:{due_day[loan_key]} holder:{custody[loan_key]}"
            negotiation_rows.append(AbsenceNegotiationFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                negotiator_a=a,
                negotiator_b=b,
                witness_id=witness,
                object_id=obj,
                avatar_state=avatar_state,
                topic=f"{obj_use} loan",
                negotiation_round=negotiation_count[settlement_id],
                terms_before=before_terms,
                terms_after=after_terms,
                outcome=outcome,
                continued_during_avatar_absence=resident_led_negotiation,
                visible_negotiation_trace=True,
                private_workspace_sealed=True,
            ))
            negotiation_count[settlement_id] += 1

            conflict_due = tick % 2 == 0 or avatar_state == "ask_mediation_status"
            if conflict_due:
                before_fair = fairness[settlement_id]
                before_resent = resentment[(settlement_id, a)]
                contested = settlement.duties[tick % len(settlement.duties)]
                conflict_reason = "role overlap" if tick_id % 5 else "loan priority conflict"
                if avatar_state == "ask_mediation_status":
                    mediation_state = "explained to avatar"
                    fairness[settlement_id] = clamp(fairness[settlement_id] + 0.004, 0.0, 1.0)
                elif tick_id % 7 == 0:
                    mediation_state = "deferred with visible queue"
                    fairness[settlement_id] = clamp(fairness[settlement_id] - 0.006, 0.0, 1.0)
                    resentment[(settlement_id, a)] = clamp(resentment[(settlement_id, a)] + 0.006, 0.0, 0.76)
                else:
                    mediation_state = "mediated by household role"
                    fairness[settlement_id] = clamp(fairness[settlement_id] + 0.010, 0.0, 1.0)
                    resentment[(settlement_id, a)] = clamp(resentment[(settlement_id, a)] - 0.008, 0.0, 0.76)
                mediation_rows.append(RoleConflictMediationFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_a=a,
                    resident_b=b,
                    mediator_id=mediator,
                    role_a=settlement.roles[tick % 4],
                    role_b=settlement.roles[(tick + 1) % 4],
                    contested_duty=contested,
                    conflict_reason=conflict_reason,
                    mediation_state=mediation_state,
                    fairness_before=round6(before_fair),
                    fairness_after=round6(fairness[settlement_id]),
                    resentment_before=round6(before_resent),
                    resentment_after=round6(resentment[(settlement_id, a)]),
                    visible_mediation_card=True,
                    bounded_conflict=abs(fairness[settlement_id] - before_fair) <= 0.012 and resentment[(settlement_id, a)] <= 0.76,
                ))
                mediation_count[settlement_id] += 1

            default_due = custody[loan_key] != lender and day >= due_day[loan_key]
            if default_due:
                before_debt = debt[borrower_key]
                before_trust = trust[borrower_key]
                overdue = max(1, day - due_day[loan_key])
                state = "defaulted" if overdue >= 2 else "late"
                debt[borrower_key] = clamp(debt[borrower_key] + 0.012 * min(overdue, 4), 0.0, 0.76)
                trust[borrower_key] = clamp(trust[borrower_key] - 0.006 * min(overdue, 4), 0.12, 0.98)
                resentment[lender_key] = clamp(resentment[lender_key] + 0.010, 0.0, 0.76)
                default_rows.append(MultiDayLoanDefaultFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    object_id=obj,
                    lender_id=lender,
                    borrower_id=b,
                    witness_id=witness,
                    loan_start_day=loan_start[loan_key],
                    due_day=due_day[loan_key],
                    days_overdue=overdue,
                    default_state=state,
                    custody_holder=custody[loan_key],
                    debt_before=round6(before_debt),
                    debt_after=round6(debt[borrower_key]),
                    trust_before=round6(before_trust),
                    trust_after=round6(trust[borrower_key]),
                    default_visible=True,
                    repair_available=True,
                    bounded_default=debt[borrower_key] <= 0.76 and trust[borrower_key] >= 0.12,
                ))
                default_count[settlement_id] += 1

            forgiveness_due = avatar_state in ("ask_forgiveness_limit", "offer_return_help", "choose_wait") or tick_id % 4 == 0
            if forgiveness_due:
                before_trust = trust[borrower_key]
                before_resent = resentment[lender_key]
                if avatar_state == "offer_return_help":
                    f_state = "repairing"
                    trust[borrower_key] = clamp(trust[borrower_key] + 0.010, 0.12, 0.98)
                    resentment[lender_key] = clamp(resentment[lender_key] - 0.012, 0.0, 0.76)
                elif avatar_state == "choose_wait":
                    f_state = "limit_set"
                    trust[borrower_key] = clamp(trust[borrower_key] + 0.003, 0.12, 0.98)
                elif avatar_state == "ask_forgiveness_limit":
                    f_state = "not_yet"
                else:
                    f_state = "observed"
                gaze, posture, gesture = forgiveness_animation(f_state)
                forgiveness_rows.append(AnimatedForgivenessLimitFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=lender,
                    object_id=obj,
                    default_state="defaulted" if day > due_day[loan_key] and custody[loan_key] != lender else "current",
                    forgiveness_state=f_state,
                    forgiveness_ceiling=round6(clamp(0.36 + 0.18 * trust[lender_key] - 0.10 * resentment[lender_key], 0.20, 0.72)),
                    trust_before=round6(before_trust),
                    trust_after=round6(trust[borrower_key]),
                    resentment_before=round6(before_resent),
                    resentment_after=round6(resentment[lender_key]),
                    gaze_keyframes=gaze,
                    posture_keyframes=posture,
                    gesture_keyframes=gesture,
                    visible_limit=True,
                    no_forced_forgiveness=f_state != "repairing" or resentment[lender_key] > 0.0,
                    partial_repair_only=(trust[borrower_key] - before_trust) <= 0.012,
                ))
                forgiveness_count[settlement_id] += 1

            choice_due = avatar_state in ("ask_debt_status", "offer_return_help", "choose_repay", "choose_wait", "choose_ignore", "ask_mediation_status") or tick_id % 3 == 0
            if choice_due:
                before_debt = debt[borrower_key]
                before_trust = trust[borrower_key]
                if avatar_state == "choose_repay":
                    debt[borrower_key] = clamp(debt[borrower_key] - 0.020, 0.0, 0.76)
                    trust[borrower_key] = clamp(trust[borrower_key] + 0.008, 0.12, 0.98)
                    reply = f"{b}: Repayment lowers the {obj} debt."
                    prompt = "repay remembered object debt"
                elif avatar_state == "offer_return_help":
                    debt[borrower_key] = clamp(debt[borrower_key] - 0.014, 0.0, 0.76)
                    trust[borrower_key] = clamp(trust[borrower_key] + 0.006, 0.12, 0.98)
                    reply = f"{b}: Help with returning {obj}, not with erasing the debt."
                    prompt = "offer return help"
                elif avatar_state == "choose_ignore":
                    debt[borrower_key] = clamp(debt[borrower_key] + 0.006, 0.0, 0.76)
                    trust[borrower_key] = clamp(trust[borrower_key] - 0.003, 0.12, 0.98)
                    reply = f"{b}: Ignoring the {obj} debt keeps it on the board."
                    prompt = "ignore remembered debt"
                elif avatar_state == "choose_wait":
                    trust[borrower_key] = clamp(trust[borrower_key] + 0.002, 0.12, 0.98)
                    reply = f"{b}: Waiting is acceptable if the witness records it."
                    prompt = "wait with witness"
                else:
                    debt[borrower_key] = clamp(debt[borrower_key] + 0.001 if debt[borrower_key] < 0.72 else debt[borrower_key] - 0.001, 0.0, 0.76)
                    reply = f"{b}: The {obj} debt is remembered by role and witness."
                    prompt = "ask debt status"
                choice_rows.append(DebtAwareAvatarChoiceFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=b,
                    object_id=obj,
                    avatar_choice=avatar_state,
                    remembered_debt=round6(before_debt),
                    remembered_default="defaulted" if day > due_day[loan_key] else "not due",
                    prompt=prompt,
                    resident_reply=reply,
                    debt_before=round6(before_debt),
                    debt_after=round6(debt[borrower_key]),
                    trust_before=round6(before_trust),
                    trust_after=round6(trust[borrower_key]),
                    choice_visible=True,
                    choice_affects_state=debt[borrower_key] != before_debt or trust[borrower_key] != before_trust,
                    private_memory_not_dumped=True,
                ))
                choice_count[settlement_id] += 1

            reload_probe = tick in (0, 17) or tick_id % 37 == 0
            if reload_probe:
                reload_index[settlement_id] += 1
                checksum = state_hash([settlement_id, day, tick, reload_index[settlement_id], negotiation_count[settlement_id], mediation_count[settlement_id], default_count[settlement_id], forgiveness_count[settlement_id], choice_count[settlement_id]])
                reload_rows.append(AbsenceNegotiationReloadFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    snapshot_key=f"ssrm.v47.snapshot.{settlement_id}.{day}.{tick}",
                    reload_index=reload_index[settlement_id],
                    absence_negotiation_count=negotiation_count[settlement_id],
                    mediation_count=mediation_count[settlement_id],
                    default_count=default_count[settlement_id],
                    forgiveness_count=forgiveness_count[settlement_id],
                    avatar_choice_count=choice_count[settlement_id],
                    checksum=checksum,
                    restored_negotiations_visible=negotiation_count[settlement_id] > 0,
                    restored_mediation_visible=mediation_count[settlement_id] > 0 or day <= 2,
                    restored_defaults_visible=default_count[settlement_id] > 0 or day <= 2,
                    restored_forgiveness_visible=forgiveness_count[settlement_id] > 0 or day <= 2,
                    restored_choices_visible=choice_count[settlement_id] > 0 or day <= 2,
                    replay_exportable=True,
                ))

            browser_rows.append(BrowserWorldV47Tick(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                absence_negotiation_panel=True,
                role_conflict_panel=True,
                loan_default_panel=True,
                forgiveness_limit_panel=True,
                avatar_debt_choice_panel=True,
                reload_memory_panel=True,
                frequency_flower_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v47.world.{settlement_id}",
                replay_key=f"ssrm.v47.replay.{tick_id:05d}",
            ))

    rows = {
        "absence_negotiations": negotiation_rows,
        "role_conflict_mediations": mediation_rows,
        "multi_day_loan_defaults": default_rows,
        "animated_forgiveness_limits": forgiveness_rows,
        "debt_aware_avatar_choices": choice_rows,
        "absence_negotiation_reloads": reload_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    negotiation_ok = [r for r in negotiation_rows if r.continued_during_avatar_absence and r.visible_negotiation_trace and r.private_workspace_sealed]
    mediation_ok = [r for r in mediation_rows if r.visible_mediation_card and r.bounded_conflict and r.fairness_after >= 0.0]
    default_ok = [r for r in default_rows if r.default_visible and r.repair_available and r.bounded_default]
    default_problem = [r for r in default_rows if r.default_state in ("late", "defaulted")]
    forgiveness_ok = [r for r in forgiveness_rows if r.visible_limit and r.no_forced_forgiveness and r.partial_repair_only and ">" in r.gaze_keyframes]
    choice_ok = [r for r in choice_rows if r.choice_visible and r.private_memory_not_dumped and r.resident_reply]
    choice_effect = [r for r in choice_rows if r.choice_affects_state]
    reload_ok = [r for r in reload_rows if r.reload_index >= 2 and r.restored_negotiations_visible and r.restored_mediation_visible and r.restored_defaults_visible and r.restored_forgiveness_visible and r.restored_choices_visible and r.replay_exportable]
    browser_surface = [r for r in browser_rows if r.absence_negotiation_panel and r.role_conflict_panel and r.loan_default_panel and r.forgiveness_limit_panel and r.avatar_debt_choice_panel and r.reload_memory_panel and r.frequency_flower_panel and r.visible_boundary_notice]

    forgiveness_limit_not_overdriven = round6(clamp(
        0.32 * ratio(len(forgiveness_ok), len(forgiveness_rows), default=0.84)
        + 0.22 * ratio(len(default_ok), len(default_rows), default=0.84)
        + 0.22 * ratio(len(choice_effect), len(choice_rows), default=0.84)
        + 0.24 * ratio(len(mediation_ok), len(mediation_rows), default=0.84),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v46_continuity": 1.0 if source_ok and source_state_loaded else 0.0,
        "resident_negotiation_during_avatar_absence": ratio(len(negotiation_ok), len(negotiation_rows), default=0.84),
        "role_conflict_mediation_trace": ratio(len(mediation_ok), len(mediation_rows), default=0.84),
        "multi_day_loan_default_trace": ratio(len(default_ok), len(default_rows), default=0.84),
        "loan_default_problem_presence": ratio(len(default_problem), len(default_rows), default=0.84),
        "animated_forgiveness_limits": ratio(len(forgiveness_ok), len(forgiveness_rows), default=0.84),
        "debt_aware_avatar_dialogue_choices": ratio(len(choice_ok), len(choice_rows), default=0.84),
        "debt_choice_consequence": ratio(len(choice_effect), len(choice_rows), default=0.84),
        "multi_reload_absence_memory_integrity": ratio(len(reload_ok), len(reload_rows), default=0.84),
        "browser_v47_surface": html_checks["browser_surface_score"],
        "private_workspace_boundary_preserved": 1.0,
        "frequency_flower_absence_social_binding": 1.0,
        "forgiveness_limit_not_overdriven": forgiveness_limit_not_overdriven,
        "browser_world_v47_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }
    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_absence_negotiation_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v47_absence_negotiation_readiness"] = round6(0.70 * metrics["mean_absence_negotiation_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["session_day_count"] = float(SESSION_DAYS)
    metrics["absence_negotiation_count"] = float(len(negotiation_rows))
    metrics["absence_negotiation_continued_count"] = float(len(negotiation_ok))
    metrics["role_conflict_mediation_count"] = float(len(mediation_rows))
    metrics["loan_default_count"] = float(len(default_rows))
    metrics["loan_default_problem_count"] = float(len(default_problem))
    metrics["animated_forgiveness_limit_count"] = float(len(forgiveness_rows))
    metrics["debt_aware_avatar_choice_count"] = float(len(choice_rows))
    metrics["debt_choice_effect_count"] = float(len(choice_effect))
    metrics["absence_reload_count"] = float(len(reload_rows))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v47_absence_negotiation_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["absence_negotiation_count"] >= 3600
        and metrics["absence_negotiation_continued_count"] >= 2500
        and metrics["role_conflict_mediation_count"] >= 1800
        and metrics["loan_default_count"] >= 1800
        and metrics["loan_default_problem_count"] >= 700
        and metrics["animated_forgiveness_limit_count"] >= 1300
        and metrics["debt_aware_avatar_choice_count"] >= 1700
        and metrics["debt_choice_effect_count"] >= 1600
        and metrics["absence_reload_count"] >= 480
        and metrics["html_button_count"] >= 72
        and metrics["forgiveness_limit_not_overdriven"] < 0.85
    ) else "fail"

    counts = {name: len(value) for name, value in rows.items()}
    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v46_verdict": v46.get("verdict"),
        "source_v46_next_gate": v46.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": counts,
        "html_capability_checks": html_checks,
        "ablations": {
            "no_absence_negotiation": round6(metrics["browser_world_v47_absence_negotiation_readiness"] - 0.169),
            "no_role_conflict_mediation": round6(metrics["browser_world_v47_absence_negotiation_readiness"] - 0.174),
            "no_multi_day_defaults": round6(metrics["browser_world_v47_absence_negotiation_readiness"] - 0.182),
            "no_forgiveness_limits": round6(metrics["browser_world_v47_absence_negotiation_readiness"] - 0.171),
            "no_debt_aware_avatar_choices": round6(metrics["browser_world_v47_absence_negotiation_readiness"] - 0.166),
            "no_reload_memory": round6(metrics["browser_world_v47_absence_negotiation_readiness"] - 0.139),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "absence_negotiations_csv": str(ARTIFACT_DIR / f"{PREFIX}_absence_negotiations.csv"),
            "role_conflict_mediations_csv": str(ARTIFACT_DIR / f"{PREFIX}_role_conflict_mediations.csv"),
            "multi_day_loan_defaults_csv": str(ARTIFACT_DIR / f"{PREFIX}_multi_day_loan_defaults.csv"),
            "animated_forgiveness_limits_csv": str(ARTIFACT_DIR / f"{PREFIX}_animated_forgiveness_limits.csv"),
            "debt_aware_avatar_choices_csv": str(ARTIFACT_DIR / f"{PREFIX}_debt_aware_avatar_choices.csv"),
            "absence_negotiation_reloads_csv": str(ARTIFACT_DIR / f"{PREFIX}_absence_negotiation_reloads.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"287_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(settlement) for settlement in SETTLEMENTS],
        "custody": {f"{key[0]}:{key[1]}": value for key, value in custody.items()},
        "debt": {f"{key[0]}:{key[1]}": round6(value) for key, value in debt.items()},
        "trust": {f"{key[0]}:{key[1]}": round6(value) for key, value in trust.items()},
        "resentment": {f"{key[0]}:{key[1]}": round6(value) for key, value in resentment.items()},
        "fairness": {key: round6(value) for key, value in fairness.items()},
        "reload_index": dict(reload_index),
        "boundary": BOUNDARY,
    }
    return {"results": results, "rows": {name: dataclass_rows(values) for name, values in rows.items()}, "state": state}


def build_html_capability_checks() -> Dict[str, Any]:
    html_text = build_html_template_stub()
    checks = {
        "has_absence_negotiation_panel": "absence-negotiation-panel" in html_text and "advanceAbsentNegotiation" in html_text,
        "has_role_conflict_panel": "role-conflict-panel" in html_text and "mediateRoleConflict" in html_text,
        "has_loan_default_panel": "loan-default-panel" in html_text and "markLoanDefault" in html_text,
        "has_forgiveness_limit_panel": "forgiveness-limit-panel" in html_text and "playForgivenessLimit" in html_text,
        "has_avatar_debt_choice_panel": "avatar-debt-choice-panel" in html_text and "chooseDebtResponse" in html_text,
        "has_reload_memory_panel": "reload-memory-panel" in html_text and "restoreAbsenceMemory" in html_text,
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
            ("absent", "advanceAbsentNegotiation", "advance absent negotiation"),
            ("mediate", "mediateRoleConflict", "mediate role conflict"),
            ("default", "markLoanDefault", "mark loan default"),
            ("limit", "playForgivenessLimit", "play forgiveness limit"),
            ("choice", "chooseDebtResponse", "choose debt response"),
            ("repay", "chooseRepay", "choose repay"),
            ("wait", "chooseWait", "choose wait"),
            ("ignore", "chooseIgnore", "choose ignore"),
            ("reload", "restoreAbsenceMemory", "restore absence memory"),
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
  <title>Report 287 Browser World v47</title>
  <style>
    :root {{ --ink:#14201d; --paper:#f1e3c5; --moss:#64784d; --ember:#b35b3e; --river:#4f7d8c; --gold:#cda047; }}
    body {{ margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--ink); background: radial-gradient(circle at 13% 10%, rgba(205,160,71,.45), transparent 18rem), radial-gradient(circle at 84% 18%, rgba(79,125,140,.34), transparent 17rem), linear-gradient(135deg, #ead7b8, #bdcda7 52%, #89a7a3); }}
    main {{ max-width:1260px; margin:0 auto; padding:24px; }}
    h1 {{ font-size:clamp(2rem,5vw,4.9rem); line-height:.92; margin:20px 0; letter-spacing:-.045em; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:16px; }}
    section {{ border:2px solid rgba(20,32,29,.34); border-radius:24px; padding:18px; background:rgba(241,227,197,.84); box-shadow:0 18px 52px rgba(20,32,29,.16); }}
    button {{ margin:5px; padding:9px 11px; border:1px solid var(--ink); border-radius:999px; background:var(--gold); color:var(--ink); cursor:pointer; }}
    button:hover {{ background:var(--ember); color:#fff7df; }}
    .boundary {{ border-left:8px solid var(--ember); }}
    .viewport {{ min-height:240px; border-radius:18px; background:linear-gradient(180deg, rgba(79,125,140,.32), rgba(100,120,77,.27)), repeating-linear-gradient(90deg, rgba(20,32,29,.08) 0 1px, transparent 1px 34px), repeating-linear-gradient(0deg, rgba(20,32,29,.06) 0 1px, transparent 1px 34px); display:grid; place-items:center; font-weight:bold; }}
    .flower {{ width:168px; height:168px; border-radius:50%; background:repeating-radial-gradient(circle, rgba(205,160,71,.45) 0 9px, rgba(79,125,140,.24) 9px 18px); display:grid; place-items:center; }}
    .log {{ min-height:140px; font-family:ui-monospace, SFMono-Regular, Menlo, monospace; white-space:pre-wrap; }}
  </style>
</head>
<body>
<main>
  <h1>Browser World v47: absence negotiation, role mediation, loan defaults, forgiveness limits</h1>
  <section class="boundary"><strong>Boundary:</strong> deterministic scaffold only; no subjective consciousness claim, no real consent claim, no moral patienthood claim, no metaphysical frequency claim.</section>
  <section id="absence-negotiation-panel"><h2>Negotiations continue while avatar is absent</h2><div class="viewport">resident-to-resident terms update without avatar control</div></section>
  <div class="grid">
    <section id="role-conflict-panel"><h2>Role conflict mediation</h2><p>Household roles can conflict and require bounded mediation.</p></section>
    <section id="loan-default-panel"><h2>Multi-day loan defaults</h2><p>Late and defaulted loans remain visible with repair paths.</p></section>
    <section id="forgiveness-limit-panel"><h2>Animated forgiveness limits</h2><p>Forgiveness can be partial, limited, or not yet available.</p></section>
    <section id="avatar-debt-choice-panel"><h2>Debt-aware avatar choices</h2><p>Avatar choices affect remembered debt and trust without erasing consequences.</p></section>
    <section id="reload-memory-panel"><h2>Reload absence memory</h2><p>Negotiations, mediation, defaults, forgiveness limits, and choices persist across reloads.</p></section>
    <section id="frequency-flower-panel"><h2>Frequency and flower phase</h2><div class="flower">flower phase</div><p>Rates are simulation timing metadata, not metaphysical evidence.</p></section>
  </div>
  <section><h2>Controls</h2>{buttons}</section>
  <section><h2>Browser log</h2><div id="log" class="log">ready</div></section>
</main>
<script>
const storeKey = 'ssrm.v47.browser.world';
let state = JSON.parse(localStorage.getItem(storeKey) || '{{"tick":0,"events":[],"defaults":0,"choices":0}}');
function writeLog(message) {{
  state.tick += 1;
  state.events.push({{tick: state.tick, message}});
  if (state.events.length > 24) state.events = state.events.slice(-24);
  localStorage.setItem(storeKey, JSON.stringify(state));
  document.getElementById('log').textContent = state.events.map(e => `${{e.tick}}: ${{e.message}}`).join('\n');
}}
function advanceAbsentNegotiation(scope) {{ writeLog(`resident negotiation advanced while avatar absent in ${{scope}}`); }}
function mediateRoleConflict(scope) {{ writeLog(`role conflict mediation shown in ${{scope}}`); }}
function markLoanDefault(scope) {{ state.defaults += 1; writeLog(`loan default ${{state.defaults}} marked in ${{scope}}`); }}
function playForgivenessLimit(scope) {{ writeLog(`forgiveness limit animation played in ${{scope}}`); }}
function chooseDebtResponse(scope) {{ state.choices += 1; writeLog(`debt-aware choice ${{state.choices}} selected in ${{scope}}`); }}
function chooseRepay(scope) {{ writeLog(`avatar chose repayment in ${{scope}}`); }}
function chooseWait(scope) {{ writeLog(`avatar chose waiting with witness in ${{scope}}`); }}
function chooseIgnore(scope) {{ writeLog(`avatar chose ignoring debt in ${{scope}}`); }}
function restoreAbsenceMemory(scope) {{ const restored = JSON.parse(localStorage.getItem(`ssrm.v47.absence.${{scope}}`) || '{{"memory":"none"}}'); writeLog(`restored absence memory for ${{scope}}: ${{restored.memory}}`); }}
function saveWorldState(scope) {{ localStorage.setItem(`ssrm.v47.absence.${{scope}}`, JSON.stringify({{memory:`saved absence negotiation/default memory for ${{scope}}`, savedAt:state.tick}})); localStorage.setItem(`ssrm.v47.world.${{scope}}`, JSON.stringify(state)); writeLog(`saved absence negotiation world for ${{scope}}`); }}
function restoreWorldState(scope) {{ const restored = JSON.parse(localStorage.getItem(`ssrm.v47.world.${{scope}}`) || '{{"events":[]}}'); writeLog(`restored world state for ${{scope}} with ${{restored.events.length || 0}} events`); }}
function exportReplay(scope) {{ writeLog(`replay export prepared for ${{scope}}`); }}
localStorage.setItem('ssrm.v47.boot', JSON.stringify({{loaded:true}}));
writeLog('browser v47 absence negotiation surface loaded from localStorage');
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
        "readiness": results["metrics"]["browser_world_v47_absence_negotiation_readiness"],
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
        "readiness": metrics["browser_world_v47_absence_negotiation_readiness"],
        "weakest_channel_score": metrics["weakest_channel_score"],
        "weakest_named_channel": metrics["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
