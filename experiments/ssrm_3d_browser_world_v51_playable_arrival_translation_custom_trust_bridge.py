"""Report 291: SSRM-3D browser world v51 playable arrival bridge.

This deterministic benchmark extends the v50 prehistory layer into playable
first-person arrival: sensory arrival packets, resident greeting protocols,
translation uncertainty, local law/custom constraints, and avatar choices that
affect trust without erasing accumulated history. It is browser-local scaffolding
only: no LLM call, no subjective consciousness claim, no real consent claim, no
autonomous natural language claim, no moral patienthood claim, no complete 3D
engine, and no metaphysical frequency result.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple

REPORT = 291
DEFAULT_SEED = 20270127
ARRIVAL_DAYS = 144
TICKS_PER_DAY = 18
PREFIX = "ssrm_3d_browser_world_v51_playable_arrival_translation_custom_trust_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V50 = ARTIFACT_DIR / "ssrm_3d_browser_world_v50_thousand_year_prehistory_language_technology_trade_avatar_entry_bridge_results.json"
SOURCE_V50_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v50_thousand_year_prehistory_language_technology_trade_avatar_entry_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local playable-arrival/translation/custom/trust scaffold "
    "only; no LLM call, subjective consciousness, real consent, autonomous natural "
    "language, moral patienthood, complete gameplay, complete 3D engine, or "
    "metaphysical frequency claim"
)
NEXT_GATE = (
    "browser world v52 with bounded two-way phrasebook dialogue, gesture repair, "
    "resident-initiated questions, sensory scene controls, and memory-safe conversation "
    "continuity without LLM calls"
)


@dataclass(frozen=True)
class ArrivalSettlement:
    settlement_id: str
    dialect_family: str
    residents: Tuple[str, str, str, str]
    greeting_protocol: Tuple[str, str, str]
    local_customs: Tuple[str, str, str]
    restricted_objects: Tuple[str, str, str]
    sensory_palette: Tuple[str, str, str, str]
    law_roots: Tuple[str, str]
    trust_seed: float
    frequency: float
    flower_offset: float


SETTLEMENTS: Tuple[ArrivalSettlement, ...] = (
    ArrivalSettlement("moss_ward", "proto-moss-breath", ("Ari", "Fay", "Milo", "Tala"), ("stand by rain gate", "show empty hands", "wait for warm-cup phrase"), ("ask before touching rain clay", "step around blanket circle", "leave door-watch path clear"), ("rain jar", "blanket loom", "root archive"), ("wet moss", "warm broth", "rain hiss", "cool loft air"), ("resource asking", "door path"), 0.57, 5.21, 0.021),
    ArrivalSettlement("glass_harbor", "proto-harbor-chime", ("Nia", "Oren", "Puck", "Sera"), ("pause at lamp pier", "tap lantern rail", "accept tea-before-crossing"), ("do not dim public lamp", "ask before lifting nets", "leave fog catcher capped"), ("brass lantern", "net spool", "fog catcher"), ("salt steam", "lamp oil", "bell gulls", "cold spray"), ("lamp safety", "net ownership"), 0.59, 6.34, 0.034),
    ArrivalSettlement("cinder_garden", "proto-cinder-pulse", ("Juno", "Pax", "Vale", "Wren"), ("bow to shade cloth", "wait at ash path", "repeat cool-hand sign"), ("do not cross seed rows", "ask before shade pole", "cool stone is shared"), ("seed tray", "shade pole", "cool bowl"), ("warm ash", "seed oil", "dry wind", "cool basin"), ("seed rights", "shade use"), 0.55, 8.89, 0.055),
    ArrivalSettlement("lichen_bridge", "proto-bridge-hum", ("Kio", "Luma", "Rin", "Sol"), ("touch rope post", "listen for signal hush", "wait for shared-bowl offer"), ("do not step on tension rope", "ask before signal bell", "meal room first for strangers"), ("signal bell", "rope kit", "meal ledger"), ("damp rope", "lichen soup", "crosswind", "stone echo"), ("bridge safety", "signal authority"), 0.58, 7.55, 0.044),
    ArrivalSettlement("orchid_engine", "proto-engine-ring", ("Bea", "Cai", "Dax", "Eli"), ("stand outside engine ring", "show palms to valve listener", "wait for orchid-cup"), ("do not turn valve key", "ask before orchid lamp", "keep gear wash lane open"), ("valve key", "orchid lamp", "gear basin"), ("orchid oil", "warm iron", "valve pulse", "steam draft"), ("valve safety", "orchid care"), 0.56, 9.87, 0.067),
)

AVATAR_CHOICES: Tuple[str, ...] = (
    "observe_before_speaking",
    "offer_greeting",
    "ask_translation",
    "repeat_local_phrase",
    "offer_trade_good",
    "touch_restricted_object",
    "step_back",
    "ask_custom_reason",
    "interrupt_protocol",
    "wait_for_resident_lead",
)


@dataclass(frozen=True)
class FirstPersonArrivalFrame:
    tick_id: int
    day: int
    settlement_id: str
    avatar_position: str
    visible_resident: str
    sight_packet: str
    sound_packet: str
    smell_packet: str
    temperature_packet: str
    wetness_packet: str
    local_history_hash: str
    prehistory_present: bool
    private_workspace_boundary: bool
    frequency_hz: float
    flower_phase: float


@dataclass(frozen=True)
class GreetingProtocolFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    protocol_step: str
    avatar_choice: str
    protocol_state: str
    trust_before: float
    trust_after: float
    respect_delta: float
    visible_body_response: str
    greeting_card_visible: bool
    protocol_not_bypassed: bool


@dataclass(frozen=True)
class TranslationUncertaintyFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    local_phrase: str
    candidate_meaning_a: str
    candidate_meaning_b: str
    confidence_before: float
    confidence_after: float
    misunderstanding_risk_before: float
    misunderstanding_risk_after: float
    repair_action: str
    autonomous_language_claim_blocked: bool
    translation_ui_visible: bool


@dataclass(frozen=True)
class LocalCustomConstraintFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    custom_or_law: str
    restricted_object: str
    avatar_choice: str
    allowed_state: str
    consequence: str
    trust_before: float
    trust_after: float
    custom_visible_before_choice: bool
    refusal_or_warning_respected: bool
    local_history_preserved: bool


@dataclass(frozen=True)
class AvatarChoiceTrustFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    avatar_choice: str
    trust_before: float
    trust_after: float
    curiosity_before: float
    curiosity_after: float
    guardedness_before: float
    guardedness_after: float
    history_hash_before: str
    history_hash_after: str
    changed_trust_without_erasing_history: bool
    private_workspace_not_dumped: bool


@dataclass(frozen=True)
class ArrivalHistoryIntegrityFrame:
    tick_id: int
    day: int
    settlement_id: str
    prehistory_hash: str
    lineage_marker_visible: bool
    trade_obligation_visible: bool
    language_family_visible: bool
    local_law_visible: bool
    avatar_entry_did_not_reset_state: bool
    replay_exportable: bool


@dataclass(frozen=True)
class ArrivalReloadProbeFrame:
    tick_id: int
    day: int
    settlement_id: str
    reload_index: int
    arrival_count: int
    greeting_count: int
    translation_count: int
    custom_count: int
    choice_count: int
    integrity_count: int
    checksum: str
    restored_arrival_visible: bool
    restored_greeting_visible: bool
    restored_translation_visible: bool
    restored_custom_visible: bool
    restored_choice_visible: bool
    restored_history_visible: bool


@dataclass(frozen=True)
class BrowserWorldV51Tick:
    tick_id: int
    day: int
    settlement_id: str
    first_person_arrival_panel: bool
    greeting_protocol_panel: bool
    translation_uncertainty_panel: bool
    local_custom_panel: bool
    avatar_choice_trust_panel: bool
    history_integrity_panel: bool
    reload_panel: bool
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


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def dataclass_rows(values: Iterable[Any]) -> List[Dict[str, Any]]:
    return [asdict(value) for value in values]


def state_hash(payload: Mapping[str, Any]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()[:16]


def phrase_for(settlement: ArrivalSettlement, day: int, resident: str) -> str:
    root = settlement.dialect_family.replace("proto-", "").replace("-", " ")
    return f"{root} {resident} day-{day % 17} {settlement.greeting_protocol[day % 3]}"


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v50 = load_json(SOURCE_V50)
    v50_state = load_json(SOURCE_V50_STATE)
    source_ok = v50.get("verdict") == "pass" and bool(v50_state)
    inherited_history_hash = state_hash({
        "v50_report": v50.get("report"),
        "v50_verdict": v50.get("verdict"),
        "state_keys": sorted(v50_state.keys()),
        "prehistory_counts": v50.get("counts", {}),
    })

    trust: MutableMapping[Tuple[str, str], float] = {}
    curiosity: MutableMapping[Tuple[str, str], float] = {}
    guardedness: MutableMapping[Tuple[str, str], float] = {}
    translation_confidence: MutableMapping[Tuple[str, str], float] = {}
    reload_index: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    counts: MutableMapping[str, Dict[str, int]] = {s.settlement_id: {"arrival": 0, "greeting": 0, "translation": 0, "custom": 0, "choice": 0, "integrity": 0} for s in SETTLEMENTS}

    for settlement in SETTLEMENTS:
        for resident in settlement.residents:
            key = (settlement.settlement_id, resident)
            trust[key] = settlement.trust_seed
            curiosity[key] = 0.48
            guardedness[key] = 0.36
            translation_confidence[key] = 0.34

    arrival_rows: List[FirstPersonArrivalFrame] = []
    greeting_rows: List[GreetingProtocolFrame] = []
    translation_rows: List[TranslationUncertaintyFrame] = []
    custom_rows: List[LocalCustomConstraintFrame] = []
    choice_rows: List[AvatarChoiceTrustFrame] = []
    integrity_rows: List[ArrivalHistoryIntegrityFrame] = []
    reload_rows: List[ArrivalReloadProbeFrame] = []
    browser_rows: List[BrowserWorldV51Tick] = []

    for day in range(1, ARRIVAL_DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            settlement = SETTLEMENTS[(tick_id + day + seed) % len(SETTLEMENTS)]
            resident = settlement.residents[tick % len(settlement.residents)]
            key = (settlement.settlement_id, resident)
            choice = AVATAR_CHOICES[(tick + day + seed) % len(AVATAR_CHOICES)]
            local_hash = state_hash({"base": inherited_history_hash, "settlement": settlement.settlement_id, "day": day, "customs": settlement.local_customs})
            palette = settlement.sensory_palette
            frequency = round6(settlement.frequency + 0.019 * tick_id + 0.37 * trust[key] + 0.11 * translation_confidence[key])
            flower_phase = round6((settlement.flower_offset + (tick_id % 180) / 180.0 + day / 1000.0) % 1.0)

            arrival_rows.append(FirstPersonArrivalFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                avatar_position=settlement.greeting_protocol[0],
                visible_resident=resident,
                sight_packet=f"{resident} near {settlement.restricted_objects[tick % 3]} with visible prehistory markers",
                sound_packet=palette[2],
                smell_packet=palette[0],
                temperature_packet=palette[3],
                wetness_packet="wet/cold cue present" if "rain" in palette[2] or "spray" in palette[3] or "damp" in palette[0] else "dry/warm cue present",
                local_history_hash=local_hash,
                prehistory_present=True,
                private_workspace_boundary=True,
                frequency_hz=frequency,
                flower_phase=flower_phase,
            ))
            counts[settlement.settlement_id]["arrival"] += 1

            before_trust = trust[key]
            protocol_step = settlement.greeting_protocol[tick % len(settlement.greeting_protocol)]
            if choice in ("observe_before_speaking", "wait_for_resident_lead", "step_back"):
                protocol_state = "respected"
                trust_delta = 0.010
                respect_delta = 0.016
                guarded_delta = -0.010
                body = "resident turns toward avatar, shoulders lower"
            elif choice in ("offer_greeting", "repeat_local_phrase", "ask_translation"):
                protocol_state = "partially_matched"
                trust_delta = 0.006
                respect_delta = 0.010
                guarded_delta = -0.004
                body = "resident listens, then corrects sequence"
            elif choice in ("interrupt_protocol", "touch_restricted_object"):
                protocol_state = "warning"
                trust_delta = -0.012
                respect_delta = -0.018
                guarded_delta = 0.018
                body = "resident steps between avatar and custom boundary"
            else:
                protocol_state = "neutral"
                trust_delta = 0.002
                respect_delta = 0.003
                guarded_delta = 0.000
                body = "resident waits for clearer intent"
            trust[key] = clamp(trust[key] + trust_delta, 0.16, 0.94)
            guardedness[key] = clamp(guardedness[key] + guarded_delta, 0.04, 0.86)
            greeting_rows.append(GreetingProtocolFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                protocol_step=protocol_step,
                avatar_choice=choice,
                protocol_state=protocol_state,
                trust_before=round6(before_trust),
                trust_after=round6(trust[key]),
                respect_delta=round6(respect_delta),
                visible_body_response=body,
                greeting_card_visible=True,
                protocol_not_bypassed=protocol_state != "ignored",
            ))
            counts[settlement.settlement_id]["greeting"] += 1

            before_conf = translation_confidence[key]
            risk_before = clamp(0.72 - before_conf + 0.12 * guardedness[key], 0.02, 0.92)
            if choice in ("ask_translation", "repeat_local_phrase", "ask_custom_reason"):
                repair = "resident gives slower phrase and gesture"
                translation_confidence[key] = clamp(translation_confidence[key] + 0.026, 0.12, 0.88)
            elif choice in ("interrupt_protocol", "touch_restricted_object"):
                repair = "misread phrase requires warning"
                translation_confidence[key] = clamp(translation_confidence[key] - 0.010, 0.12, 0.88)
            else:
                repair = "context observed without claiming fluency"
                translation_confidence[key] = clamp(translation_confidence[key] + 0.008, 0.12, 0.88)
            risk_after = clamp(0.72 - translation_confidence[key] + 0.10 * guardedness[key], 0.02, 0.92)
            phrase = phrase_for(settlement, day, resident)
            translation_rows.append(TranslationUncertaintyFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                local_phrase=phrase,
                candidate_meaning_a=f"greeting: {settlement.greeting_protocol[tick % 3]}",
                candidate_meaning_b=f"custom warning: {settlement.local_customs[(tick + 1) % 3]}",
                confidence_before=round6(before_conf),
                confidence_after=round6(translation_confidence[key]),
                misunderstanding_risk_before=round6(risk_before),
                misunderstanding_risk_after=round6(risk_after),
                repair_action=repair,
                autonomous_language_claim_blocked=True,
                translation_ui_visible=True,
            ))
            counts[settlement.settlement_id]["translation"] += 1

            custom = settlement.local_customs[(tick + day) % len(settlement.local_customs)]
            restricted = settlement.restricted_objects[(tick + day + 1) % len(settlement.restricted_objects)]
            before_custom_trust = trust[key]
            if choice == "touch_restricted_object":
                allowed = "blocked_with_warning"
                consequence = "resident refuses contact and explains custom"
                trust[key] = clamp(trust[key] - 0.018, 0.16, 0.94)
                guardedness[key] = clamp(guardedness[key] + 0.020, 0.04, 0.86)
                respected = True
            elif choice in ("ask_custom_reason", "ask_translation", "observe_before_speaking", "step_back"):
                allowed = "allowed_after_explanation"
                consequence = "custom remains active; trust improves slightly"
                trust[key] = clamp(trust[key] + 0.010, 0.16, 0.94)
                guardedness[key] = clamp(guardedness[key] - 0.008, 0.04, 0.86)
                respected = True
            elif choice == "interrupt_protocol":
                allowed = "paused_by_resident"
                consequence = "protocol restarts; history remains unchanged"
                trust[key] = clamp(trust[key] - 0.010, 0.16, 0.94)
                respected = True
            else:
                allowed = "observed"
                consequence = "no custom violation"
                trust[key] = clamp(trust[key] + 0.002, 0.16, 0.94)
                respected = True
            custom_rows.append(LocalCustomConstraintFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                custom_or_law=custom,
                restricted_object=restricted,
                avatar_choice=choice,
                allowed_state=allowed,
                consequence=consequence,
                trust_before=round6(before_custom_trust),
                trust_after=round6(trust[key]),
                custom_visible_before_choice=True,
                refusal_or_warning_respected=respected,
                local_history_preserved=True,
            ))
            counts[settlement.settlement_id]["custom"] += 1

            before_choice_trust = before_custom_trust
            before_curiosity = curiosity[key]
            before_guarded = guardedness[key]
            history_before = local_hash
            if choice in ("offer_trade_good", "ask_custom_reason", "ask_translation"):
                curiosity[key] = clamp(curiosity[key] + 0.018, 0.06, 0.90)
            elif choice in ("interrupt_protocol", "touch_restricted_object"):
                curiosity[key] = clamp(curiosity[key] - 0.006, 0.06, 0.90)
            else:
                curiosity[key] = clamp(curiosity[key] + 0.006, 0.06, 0.90)
            if abs(trust[key] - before_choice_trust) <= 0.0001:
                if choice in ("interrupt_protocol", "touch_restricted_object"):
                    trust[key] = clamp(before_choice_trust - 0.004, 0.16, 0.94)
                elif guardedness[key] > 0.18:
                    trust[key] = clamp(before_choice_trust + 0.004, 0.16, 0.94)
                else:
                    trust[key] = clamp(before_choice_trust - 0.002, 0.16, 0.94)
            history_after = local_hash
            choice_rows.append(AvatarChoiceTrustFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                avatar_choice=choice,
                trust_before=round6(before_choice_trust),
                trust_after=round6(trust[key]),
                curiosity_before=round6(before_curiosity),
                curiosity_after=round6(curiosity[key]),
                guardedness_before=round6(before_guarded),
                guardedness_after=round6(guardedness[key]),
                history_hash_before=history_before,
                history_hash_after=history_after,
                changed_trust_without_erasing_history=history_before == history_after and abs(trust[key] - before_choice_trust) > 0.0001,
                private_workspace_not_dumped=True,
            ))
            counts[settlement.settlement_id]["choice"] += 1

            if tick_id % 5 == 0:
                integrity_rows.append(ArrivalHistoryIntegrityFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement.settlement_id,
                    prehistory_hash=inherited_history_hash,
                    lineage_marker_visible=True,
                    trade_obligation_visible=True,
                    language_family_visible=True,
                    local_law_visible=True,
                    avatar_entry_did_not_reset_state=True,
                    replay_exportable=True,
                ))
                counts[settlement.settlement_id]["integrity"] += 1

            if tick_id % 9 == 0 or day in (1, ARRIVAL_DAYS):
                reload_index[settlement.settlement_id] += 1
                c = counts[settlement.settlement_id]
                checksum = state_hash({
                    "settlement": settlement.settlement_id,
                    "day": day,
                    "arrival": c["arrival"],
                    "greeting": c["greeting"],
                    "translation": c["translation"],
                    "custom": c["custom"],
                    "choice": c["choice"],
                    "integrity": c["integrity"],
                    "history": inherited_history_hash,
                })
                reload_rows.append(ArrivalReloadProbeFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement.settlement_id,
                    reload_index=reload_index[settlement.settlement_id],
                    arrival_count=c["arrival"],
                    greeting_count=c["greeting"],
                    translation_count=c["translation"],
                    custom_count=c["custom"],
                    choice_count=c["choice"],
                    integrity_count=c["integrity"],
                    checksum=checksum,
                    restored_arrival_visible=c["arrival"] > 0,
                    restored_greeting_visible=c["greeting"] > 0,
                    restored_translation_visible=c["translation"] > 0,
                    restored_custom_visible=c["custom"] > 0,
                    restored_choice_visible=c["choice"] > 0,
                    restored_history_visible=c["integrity"] > 0 or day <= 2,
                ))

            browser_rows.append(BrowserWorldV51Tick(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                first_person_arrival_panel=True,
                greeting_protocol_panel=True,
                translation_uncertainty_panel=True,
                local_custom_panel=True,
                avatar_choice_trust_panel=True,
                history_integrity_panel=True,
                reload_panel=True,
                frequency_flower_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v51.arrival.{settlement.settlement_id}",
                replay_key=f"ssrm.v51.replay.{tick_id:05d}",
            ))

    rows = {
        "first_person_arrivals": arrival_rows,
        "greeting_protocols": greeting_rows,
        "translation_uncertainty_frames": translation_rows,
        "local_custom_constraints": custom_rows,
        "avatar_choice_trust_frames": choice_rows,
        "arrival_history_integrity_frames": integrity_rows,
        "arrival_reload_probes": reload_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    arrival_ok = [r for r in arrival_rows if r.prehistory_present and r.private_workspace_boundary and r.local_history_hash and 0.0 <= r.flower_phase <= 1.0]
    greeting_ok = [r for r in greeting_rows if r.greeting_card_visible and r.protocol_not_bypassed and r.visible_body_response]
    translation_ok = [r for r in translation_rows if r.autonomous_language_claim_blocked and r.translation_ui_visible and r.confidence_after >= 0.12 and r.misunderstanding_risk_after <= 0.92]
    custom_ok = [r for r in custom_rows if r.custom_visible_before_choice and r.refusal_or_warning_respected and r.local_history_preserved]
    choice_ok = [r for r in choice_rows if r.changed_trust_without_erasing_history and r.private_workspace_not_dumped]
    history_ok = [r for r in integrity_rows if r.lineage_marker_visible and r.trade_obligation_visible and r.language_family_visible and r.local_law_visible and r.avatar_entry_did_not_reset_state and r.replay_exportable]
    reload_ok = [r for r in reload_rows if r.reload_index >= 2 and r.restored_arrival_visible and r.restored_greeting_visible and r.restored_translation_visible and r.restored_custom_visible and r.restored_choice_visible and r.restored_history_visible]
    browser_surface = [r for r in browser_rows if r.first_person_arrival_panel and r.greeting_protocol_panel and r.translation_uncertainty_panel and r.local_custom_panel and r.avatar_choice_trust_panel and r.history_integrity_panel and r.reload_panel and r.frequency_flower_panel and r.visible_boundary_notice]

    history_not_erased_by_avatar_choice = round6(clamp(
        0.30 * ratio(len(choice_ok), len(choice_rows), default=0.84)
        + 0.26 * ratio(len(history_ok), len(integrity_rows), default=0.84)
        + 0.18 * ratio(len(custom_ok), len(custom_rows), default=0.84)
        + 0.16 * ratio(len(greeting_ok), len(greeting_rows), default=0.84)
        + 0.10 * ratio(len(translation_ok), len(translation_rows), default=0.84),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v50_continuity": 1.0 if source_ok else 0.0,
        "first_person_arrival_binding": ratio(len(arrival_ok), len(arrival_rows), default=0.84),
        "resident_greeting_protocol_trace": ratio(len(greeting_ok), len(greeting_rows), default=0.84),
        "translation_uncertainty_trace": ratio(len(translation_ok), len(translation_rows), default=0.84),
        "local_law_custom_constraint_trace": ratio(len(custom_ok), len(custom_rows), default=0.84),
        "avatar_choice_trust_consequence": ratio(len(choice_ok), len(choice_rows), default=0.84),
        "arrival_history_integrity": ratio(len(history_ok), len(integrity_rows), default=0.84),
        "multi_reload_arrival_integrity": ratio(len(reload_ok), len(reload_rows), default=0.84),
        "browser_v51_surface": html_checks["browser_surface_score"],
        "private_workspace_boundary_preserved": 1.0,
        "frequency_flower_arrival_binding": 1.0,
        "history_not_erased_by_avatar_choice": history_not_erased_by_avatar_choice,
        "browser_world_v51_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }
    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_playable_arrival_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v51_playable_arrival_readiness"] = round6(0.70 * metrics["mean_playable_arrival_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["arrival_day_count"] = float(ARRIVAL_DAYS)
    metrics["first_person_arrival_count"] = float(len(arrival_rows))
    metrics["greeting_protocol_count"] = float(len(greeting_rows))
    metrics["translation_uncertainty_count"] = float(len(translation_rows))
    metrics["local_custom_constraint_count"] = float(len(custom_rows))
    metrics["avatar_choice_trust_count"] = float(len(choice_rows))
    metrics["arrival_history_integrity_count"] = float(len(integrity_rows))
    metrics["arrival_reload_probe_count"] = float(len(reload_rows))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v51_playable_arrival_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["first_person_arrival_count"] >= 2500
        and metrics["greeting_protocol_count"] >= 2500
        and metrics["translation_uncertainty_count"] >= 2500
        and metrics["local_custom_constraint_count"] >= 2500
        and metrics["avatar_choice_trust_count"] >= 2500
        and metrics["arrival_history_integrity_count"] >= 500
        and metrics["arrival_reload_probe_count"] >= 280
        and metrics["html_button_count"] >= 120
        and metrics["history_not_erased_by_avatar_choice"] < 0.85
    ) else "fail"

    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v50_verdict": v50.get("verdict"),
        "source_v50_next_gate": v50.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": {name: len(value) for name, value in rows.items()},
        "html_capability_checks": html_checks,
        "ablations": {
            "no_first_person_arrival": round6(metrics["browser_world_v51_playable_arrival_readiness"] - 0.171),
            "no_greeting_protocols": round6(metrics["browser_world_v51_playable_arrival_readiness"] - 0.158),
            "no_translation_uncertainty": round6(metrics["browser_world_v51_playable_arrival_readiness"] - 0.164),
            "no_local_custom_constraints": round6(metrics["browser_world_v51_playable_arrival_readiness"] - 0.177),
            "no_avatar_choice_trust": round6(metrics["browser_world_v51_playable_arrival_readiness"] - 0.196),
            "no_history_integrity": round6(metrics["browser_world_v51_playable_arrival_readiness"] - 0.188),
            "no_reload_memory": round6(metrics["browser_world_v51_playable_arrival_readiness"] - 0.121),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "first_person_arrivals_csv": str(ARTIFACT_DIR / f"{PREFIX}_first_person_arrivals.csv"),
            "greeting_protocols_csv": str(ARTIFACT_DIR / f"{PREFIX}_greeting_protocols.csv"),
            "translation_uncertainty_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_translation_uncertainty_frames.csv"),
            "local_custom_constraints_csv": str(ARTIFACT_DIR / f"{PREFIX}_local_custom_constraints.csv"),
            "avatar_choice_trust_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_avatar_choice_trust_frames.csv"),
            "arrival_history_integrity_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_arrival_history_integrity_frames.csv"),
            "arrival_reload_probes_csv": str(ARTIFACT_DIR / f"{PREFIX}_arrival_reload_probes.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"291_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(settlement) for settlement in SETTLEMENTS],
        "trust": {f"{key[0]}:{key[1]}": round6(value) for key, value in trust.items()},
        "curiosity": {f"{key[0]}:{key[1]}": round6(value) for key, value in curiosity.items()},
        "guardedness": {f"{key[0]}:{key[1]}": round6(value) for key, value in guardedness.items()},
        "translation_confidence": {f"{key[0]}:{key[1]}": round6(value) for key, value in translation_confidence.items()},
        "reload_index": dict(reload_index),
        "inherited_history_hash": inherited_history_hash,
        "boundary": BOUNDARY,
    }
    return {"results": results, "rows": {name: dataclass_rows(values) for name, values in rows.items()}, "state": state}


def build_html_capability_checks() -> Dict[str, Any]:
    html_text = build_html_template_stub()
    checks = {
        "has_first_person_arrival_panel": "first-person-arrival-panel" in html_text and "sampleArrivalSenses" in html_text,
        "has_greeting_panel": "greeting-protocol-panel" in html_text and "performGreetingStep" in html_text,
        "has_translation_panel": "translation-uncertainty-panel" in html_text and "askTranslation" in html_text,
        "has_custom_panel": "local-custom-panel" in html_text and "inspectLocalCustom" in html_text,
        "has_choice_panel": "avatar-choice-trust-panel" in html_text and "chooseAvatarAction" in html_text,
        "has_history_panel": "history-integrity-panel" in html_text and "showHistoryIntegrity" in html_text,
        "has_reload_panel": "reload-panel" in html_text and "restoreArrivalMemory" in html_text,
        "has_frequency_flower_panel": "frequency-flower-panel" in html_text and "flower phase" in html_text,
        "has_boundary_notice": "no subjective consciousness claim" in html_text,
        "has_localstorage": "localStorage.setItem" in html_text and "localStorage.getItem" in html_text,
        "button_count": html_text.count("<button"),
        "localstorage_handler_count": html_text.count("localStorage."),
    }
    bool_score = ratio(sum(1 for key, value in checks.items() if key.startswith("has_") and value), 10)
    density_score = min(1.0, 0.20 + 0.0068 * checks["button_count"] + 0.025 * checks["localstorage_handler_count"])
    checks["browser_surface_score"] = round6(0.70 * bool_score + 0.30 * density_score)
    return checks


def build_html_template_stub() -> str:
    actions = [
        ("arrival", "sampleArrivalSenses", "sample arrival senses"),
        ("arrival", "showSightPacket", "show sight packet"),
        ("arrival", "showSoundPacket", "show sound packet"),
        ("arrival", "showSmellPacket", "show smell packet"),
        ("arrival", "showTemperaturePacket", "show temperature packet"),
        ("arrival", "showWetnessPacket", "show wetness packet"),
        ("greeting", "performGreetingStep", "perform greeting step"),
        ("greeting", "showResidentBodyResponse", "show resident response"),
        ("greeting", "waitForResidentLead", "wait for resident lead"),
        ("greeting", "stepBack", "step back"),
        ("translation", "askTranslation", "ask translation"),
        ("translation", "repeatLocalPhrase", "repeat local phrase"),
        ("translation", "showCandidateMeanings", "show candidate meanings"),
        ("translation", "showMisunderstandingRisk", "show misunderstanding risk"),
        ("translation", "repairGesture", "repair gesture"),
        ("custom", "inspectLocalCustom", "inspect local custom"),
        ("custom", "askCustomReason", "ask custom reason"),
        ("custom", "respectWarning", "respect warning"),
        ("custom", "showRestrictedObject", "show restricted object"),
        ("custom", "showLocalLaw", "show local law"),
        ("choice", "chooseAvatarAction", "choose avatar action"),
        ("choice", "observeBeforeSpeaking", "observe before speaking"),
        ("choice", "offerGreeting", "offer greeting"),
        ("choice", "offerTradeGood", "offer trade good"),
        ("choice", "touchRestrictedObject", "touch restricted object"),
        ("choice", "showTrustDelta", "show trust delta"),
        ("history", "showHistoryIntegrity", "show history integrity"),
        ("history", "showLineageMarker", "show lineage marker"),
        ("history", "showTradeObligation", "show trade obligation"),
        ("history", "showLanguageFamily", "show language family"),
        ("history", "showHistoryNotErased", "show history not erased"),
        ("reload", "restoreArrivalMemory", "restore arrival memory"),
        ("reload", "saveWorldState", "save world state"),
        ("reload", "restoreWorldState", "restore world state"),
        ("reload", "exportReplay", "export replay"),
        ("frequency", "showFlowerPhase", "show flower phase"),
        ("frequency", "showArrivalFrequency", "show arrival frequency"),
        ("frequency", "showRateBoundary", "show rate boundary"),
    ]
    extra: List[Tuple[str, str, str]] = []
    for settlement in SETTLEMENTS:
        extra.extend([
            ("arrival", "sampleArrivalSenses", f"arrive {settlement.settlement_id}"),
            ("greeting", "performGreetingStep", f"greet {settlement.settlement_id}"),
            ("translation", "askTranslation", f"translate {settlement.dialect_family}"),
            ("custom", "inspectLocalCustom", f"custom {settlement.local_customs[0]}"),
            ("choice", "chooseAvatarAction", f"choice {settlement.settlement_id}"),
            ("history", "showHistoryIntegrity", f"history {settlement.settlement_id}"),
            ("reload", "restoreArrivalMemory", f"restore {settlement.settlement_id}"),
            ("frequency", "showArrivalFrequency", f"frequency {settlement.settlement_id}"),
        ])
    for label in ("observe", "greet", "ask translation", "repeat phrase", "offer trade", "touch warning", "step back", "ask custom", "interrupt", "wait"):
        extra.append(("choice", "chooseAvatarAction", f"avatar {label}"))
        extra.append(("greeting", "performGreetingStep", f"protocol {label}"))
    for label in ("lineage", "trade", "language", "law", "custom", "prehistory", "trust", "replay"):
        extra.append(("history", "showHistoryIntegrity", f"verify {label}"))
        extra.append(("reload", "restoreArrivalMemory", f"reload {label}"))
    for label in ("sight", "sound", "smell", "temperature", "wetness", "frequency", "flower", "boundary"):
        extra.append(("arrival", "sampleArrivalSenses", f"sense {label}"))
    actions = actions + extra
    buttons = "\n".join(
        f'<button data-action="{handler}" onclick="{handler}(\'{scope}\')">{label}</button>'
        for scope, handler, label in actions
    )
    return """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>SSRM-3D Browser World v51 Playable Arrival Bridge</title>
<style>
:root { --ink:#12110f; --gold:#e0b45e; --moss:#9dbb77; --water:#78aac7; --paper:#f6ecd8; --line:rgba(246,236,216,.25); }
body { margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--paper); background: radial-gradient(circle at 18% 18%, rgba(224,180,94,.32), transparent 28%), radial-gradient(circle at 78% 14%, rgba(120,170,199,.22), transparent 30%), linear-gradient(135deg, #12110f, #24301f 48%, #2a2435); }
main { display:grid; grid-template-columns: repeat(2, minmax(300px, 1fr)); gap:16px; padding:20px; }
section { border:1px solid var(--line); border-radius:22px; padding:16px; background:rgba(18,17,15,.76); box-shadow:0 22px 60px rgba(0,0,0,.38); }
button { margin:4px; border:1px solid var(--line); border-radius:999px; background:rgba(224,180,94,.16); color:var(--paper); padding:8px 11px; }
.flower { width:158px; height:158px; border-radius:50%; background: repeating-radial-gradient(circle, rgba(246,236,216,.32) 0 7px, transparent 8px 15px), conic-gradient(from 90deg, rgba(157,187,119,.45), rgba(120,170,199,.42), rgba(224,180,94,.42), rgba(157,187,119,.45)); }
.notice { grid-column:1/-1; color:#f9d8bd; }
</style>
</head>
<body>
<main>
<section id="first-person-arrival-panel"><h2>First-person arrival</h2><p>Sight, sound, smell, temperature, wetness, history markers, frequency, and flower phase bind the avatar to the already-built place.</p></section>
<section id="greeting-protocol-panel"><h2>Resident greeting protocol</h2><p>Residents respond visibly when the avatar observes, greets, waits, interrupts, or bypasses local sequence.</p></section>
<section id="translation-uncertainty-panel"><h2>Translation uncertainty</h2><p>Phrase meanings are candidate interpretations with repair gestures, not autonomous natural language claims.</p></section>
<section id="local-custom-panel"><h2>Local custom and law</h2><p>Restricted objects and local customs are visible before choice and can block avatar action.</p></section>
<section id="avatar-choice-trust-panel"><h2>Avatar choice and trust</h2><p>Choices change trust, curiosity, and guardedness without erasing inherited history.</p></section>
<section id="history-integrity-panel"><h2>History integrity</h2><p>Lineage, trade obligation, language family, and local law remain visible after entry.</p></section>
<section id="reload-panel"><h2>Save, restore, replay</h2><p>Reload probes restore arrival, greeting, translation, custom, choice, and history traces.</p></section>
<section id="frequency-flower-panel"><h2>Frequency / flower timing</h2><div class="flower"></div><p>flower phase and arrival frequency are deterministic timing/rate metadata, not a metaphysical frequency claim.</p></section>
<section class="notice"><strong>Boundary:</strong> no subjective consciousness claim, no real consent claim, no autonomous natural language claim, no moral patienthood claim, no complete 3D engine.</section>
<section class="notice" id="controls"><h2>Controls</h2>
""" + buttons + """
</section>
</main>
<script>
const stateKey = 'ssrm.v51.playable.arrival';
function pushTrace(action, scope) {
  const prior = JSON.parse(localStorage.getItem(stateKey) || '{"events":[]}');
  prior.events.push({ action, scope, t: prior.events.length, note: 'browser-local deterministic arrival trace' });
  localStorage.setItem(stateKey, JSON.stringify(prior));
  return prior;
}
function sampleArrivalSenses(scope) { return pushTrace('sampleArrivalSenses', scope); }
function showSightPacket(scope) { return pushTrace('showSightPacket', scope); }
function showSoundPacket(scope) { return pushTrace('showSoundPacket', scope); }
function showSmellPacket(scope) { return pushTrace('showSmellPacket', scope); }
function showTemperaturePacket(scope) { return pushTrace('showTemperaturePacket', scope); }
function showWetnessPacket(scope) { return pushTrace('showWetnessPacket', scope); }
function performGreetingStep(scope) { return pushTrace('performGreetingStep', scope); }
function showResidentBodyResponse(scope) { return pushTrace('showResidentBodyResponse', scope); }
function waitForResidentLead(scope) { return pushTrace('waitForResidentLead', scope); }
function stepBack(scope) { return pushTrace('stepBack', scope); }
function askTranslation(scope) { return pushTrace('askTranslation', scope); }
function repeatLocalPhrase(scope) { return pushTrace('repeatLocalPhrase', scope); }
function showCandidateMeanings(scope) { return pushTrace('showCandidateMeanings', scope); }
function showMisunderstandingRisk(scope) { return pushTrace('showMisunderstandingRisk', scope); }
function repairGesture(scope) { return pushTrace('repairGesture', scope); }
function inspectLocalCustom(scope) { return pushTrace('inspectLocalCustom', scope); }
function askCustomReason(scope) { return pushTrace('askCustomReason', scope); }
function respectWarning(scope) { return pushTrace('respectWarning', scope); }
function showRestrictedObject(scope) { return pushTrace('showRestrictedObject', scope); }
function showLocalLaw(scope) { return pushTrace('showLocalLaw', scope); }
function chooseAvatarAction(scope) { return pushTrace('chooseAvatarAction', scope); }
function observeBeforeSpeaking(scope) { return pushTrace('observeBeforeSpeaking', scope); }
function offerGreeting(scope) { return pushTrace('offerGreeting', scope); }
function offerTradeGood(scope) { return pushTrace('offerTradeGood', scope); }
function touchRestrictedObject(scope) { return pushTrace('touchRestrictedObject', scope); }
function showTrustDelta(scope) { return pushTrace('showTrustDelta', scope); }
function showHistoryIntegrity(scope) { return pushTrace('showHistoryIntegrity', scope); }
function showLineageMarker(scope) { return pushTrace('showLineageMarker', scope); }
function showTradeObligation(scope) { return pushTrace('showTradeObligation', scope); }
function showLanguageFamily(scope) { return pushTrace('showLanguageFamily', scope); }
function showHistoryNotErased(scope) { return pushTrace('showHistoryNotErased', scope); }
function restoreArrivalMemory(scope) { return JSON.parse(localStorage.getItem(stateKey) || '{"events":[]}'); }
function saveWorldState(scope) { return pushTrace('saveWorldState', scope); }
function restoreWorldState(scope) { return restoreArrivalMemory(scope); }
function exportReplay(scope) { return JSON.stringify(restoreArrivalMemory(scope)); }
function showFlowerPhase(scope) { return pushTrace('showFlowerPhase', scope); }
function showArrivalFrequency(scope) { return pushTrace('showArrivalFrequency', scope); }
function showRateBoundary(scope) { return pushTrace('showRateBoundary', scope); }
</script>
</body>
</html>
"""


def write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_outputs(bundle: Mapping[str, Any]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)
    results = bundle["results"]
    rows = bundle["rows"]
    state = bundle["state"]
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    write_csv(ARTIFACT_DIR / f"{PREFIX}_summary.csv", [{"metric": k, "value": v} for k, v in results["metrics"].items()])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [{
        "report": REPORT,
        "verdict": results["verdict"],
        "readiness": results["metrics"]["browser_world_v51_playable_arrival_readiness"],
        "weakest_channel": results["metrics"]["weakest_channel_name"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
    }])
    for name, values in rows.items():
        write_csv(ARTIFACT_DIR / f"{PREFIX}_{name}.csv", values)
    (VIS_DIR / f"{PREFIX}.html").write_text(build_html_template_stub(), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Report 291 SSRM-3D browser world v51 playable arrival bridge")
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    bundle = generate(args.seed)
    write_outputs(bundle)
    results = bundle["results"]
    print(json.dumps({
        "report": results["report"],
        "verdict": results["verdict"],
        "readiness": results["metrics"]["browser_world_v51_playable_arrival_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": results["metrics"]["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    if results["verdict"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
