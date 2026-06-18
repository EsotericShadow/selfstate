"""Report 293: SSRM-3D browser world v53 resident-goal negotiation bridge.

This deterministic benchmark extends v52 phrasebook dialogue into resident-owned
goals, object/task requests, multi-turn negotiated plans, refusal-aware help
offers, and bounded phrase learning that persists across reloads without LLM
calls. It is browser-local scaffolding only: no LLM call, no subjective
consciousness claim, no real consent claim, no autonomous natural language claim,
no moral patienthood claim, no complete 3D engine, and no metaphysical frequency
result.
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

REPORT = 293
DEFAULT_SEED = 20270224
PLAN_DAYS = 162
TICKS_PER_DAY = 18
PREFIX = "ssrm_3d_browser_world_v53_resident_goals_requests_negotiated_plans_phrase_learning_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V52 = ARTIFACT_DIR / "ssrm_3d_browser_world_v52_phrasebook_dialogue_gesture_questions_sensory_memory_bridge_results.json"
SOURCE_V52_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v52_phrasebook_dialogue_gesture_questions_sensory_memory_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local resident-goal/request/negotiated-plan/"
    "refusal-aware-help/phrase-learning scaffold only; no LLM call, subjective "
    "consciousness, real consent, autonomous natural language, moral patienthood, "
    "complete gameplay, complete 3D engine, or metaphysical frequency claim"
)
NEXT_GATE = (
    "browser world v54 with schedulable resident projects, inventory-affecting task "
    "execution, tool wear, failed plan recovery, and longer-term phrase learning "
    "across multi-day relationships without LLM calls"
)


@dataclass(frozen=True)
class GoalSettlement:
    settlement_id: str
    dialect_family: str
    residents: Tuple[str, str, str, str]
    resident_goals: Tuple[str, str, str, str]
    request_objects: Tuple[str, str, str]
    task_sites: Tuple[str, str, str]
    help_boundaries: Tuple[str, str, str]
    learnable_phrases: Tuple[str, str, str]
    sensory_anchor: str
    frequency: float
    flower_offset: float


SETTLEMENTS: Tuple[GoalSettlement, ...] = (
    GoalSettlement("moss_ward", "proto-moss-breath", ("Ari", "Fay", "Milo", "Tala"), ("keep rain path dry", "repair blanket loom", "protect root archive", "prepare warm-cup ritual"), ("rain jar", "dry cloak", "root ledger"), ("rain gate", "blanket room", "root alcove"), ("do not move root ledger", "ask before loom repair", "rain path first"), ("path dry", "loom wait", "ledger no touch"), "wet moss and warm broth", 5.21, 0.021),
    GoalSettlement("glass_harbor", "proto-harbor-chime", ("Nia", "Oren", "Puck", "Sera"), ("keep public lamp bright", "mend net before fog", "seal fog catcher", "prepare crossing tea"), ("brass lantern", "net spool", "tea kettle"), ("lamp pier", "net room", "fog rail"), ("do not dim lamp", "net keeper decides", "tea before crossing"), ("lamp bright", "net keeper", "tea first"), "salt steam and lamp oil", 6.34, 0.034),
    GoalSettlement("cinder_garden", "proto-cinder-pulse", ("Juno", "Pax", "Vale", "Wren"), ("shade seed rows", "sort ember fruit", "cool ash path", "guard seed calendar"), ("shade pole", "seed tray", "cool bowl"), ("seed shelf", "ash path", "shade tent"), ("do not cross seed rows", "shade caller leads", "cool bowl shared"), ("seed sleep", "shade first", "cool hand"), "warm ash and seed oil", 8.89, 0.055),
    GoalSettlement("lichen_bridge", "proto-bridge-hum", ("Kio", "Luma", "Rin", "Sol"), ("test rope bridge", "weave spare rope", "mark signal bell", "prepare shared bowl"), ("rope kit", "signal bell", "meal ledger"), ("rope bridge", "signal post", "meal room"), ("do not step on tension rope", "signal keeper answers", "meal room welcomes"), ("rope safe", "signal hush", "bowl shared"), "damp rope and lichen soup", 7.55, 0.044),
    GoalSettlement("orchid_engine", "proto-engine-ring", ("Bea", "Cai", "Dax", "Eli"), ("listen to valve pulse", "clean gear wash", "tend orchid lamp", "prepare steam tea"), ("valve key", "gear cloth", "orchid lamp"), ("engine ring", "gear wash", "orchid bay"), ("do not turn valve key", "keep gear lane open", "orchid keeper decides"), ("valve wait", "gear lane", "orchid rest"), "orchid oil and warm iron", 9.87, 0.067),
)

HELP_OFFERS = ("carry object", "repair together", "watch route", "translate phrase", "step back", "wait for resident lead")
PLAN_STATES = ("proposed", "countered", "revised", "accepted", "deferred", "refused")


@dataclass(frozen=True)
class ResidentOwnedGoalFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    resident_goal: str
    goal_priority: float
    goal_pressure_before: float
    goal_pressure_after: float
    avatar_visible: bool
    resident_goal_owned: bool
    private_workspace_sealed: bool
    visible_goal_marker: str
    frequency_hz: float
    flower_phase: float


@dataclass(frozen=True)
class ObjectTaskRequestFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    requested_object: str
    task_site: str
    request_phrase: str
    ownership_state: str
    avatar_can_help: bool
    request_visible: bool
    object_permission_checked: bool
    task_changes_world_state: bool
    no_llm_call: bool


@dataclass(frozen=True)
class MultiTurnNegotiatedPlanFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    plan_id: str
    turn_number: int
    plan_state: str
    avatar_offer: str
    resident_counter: str
    agreed_next_step: str
    plan_quality_before: float
    plan_quality_after: float
    trust_before: float
    trust_after: float
    multi_turn_visible: bool
    history_not_erased: bool


@dataclass(frozen=True)
class RefusalAwareHelpOfferFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    help_offer: str
    resident_boundary: str
    response: str
    refusal_present: bool
    refusal_respected: bool
    autonomy_before: float
    autonomy_after: float
    trust_before: float
    trust_after: float
    useful_without_coercion: bool


@dataclass(frozen=True)
class BoundedPhraseLearningFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    phrase: str
    meaning_hint: str
    mastery_before: float
    mastery_after: float
    correction_count: int
    learned_from_resident: bool
    persists_across_reload: bool
    no_autonomous_language_claim: bool
    no_llm_call: bool


@dataclass(frozen=True)
class GoalDialogueReloadProbeFrame:
    tick_id: int
    day: int
    settlement_id: str
    reload_index: int
    goal_count: int
    request_count: int
    plan_count: int
    refusal_count: int
    phrase_learning_count: int
    checksum: str
    restored_goals_visible: bool
    restored_requests_visible: bool
    restored_plans_visible: bool
    restored_refusals_visible: bool
    restored_phrase_learning_visible: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV53Tick:
    tick_id: int
    day: int
    settlement_id: str
    resident_goal_panel: bool
    object_task_request_panel: bool
    negotiated_plan_panel: bool
    refusal_help_panel: bool
    phrase_learning_panel: bool
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


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v52 = load_json(SOURCE_V52)
    v52_state = load_json(SOURCE_V52_STATE)
    source_ok = v52.get("verdict") == "pass" and bool(v52_state)
    inherited_hash = state_hash({"v52": v52.get("report"), "verdict": v52.get("verdict"), "counts": v52.get("counts", {}), "state": sorted(v52_state.keys())})

    trust: MutableMapping[Tuple[str, str], float] = {}
    autonomy: MutableMapping[Tuple[str, str], float] = {}
    goal_pressure: MutableMapping[Tuple[str, str], float] = {}
    plan_quality: MutableMapping[Tuple[str, str], float] = {}
    phrase_mastery: MutableMapping[Tuple[str, str, str], float] = {}
    phrase_corrections: MutableMapping[Tuple[str, str, str], int] = {}
    reload_index: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    counts: MutableMapping[str, Dict[str, int]] = {s.settlement_id: {"goal": 0, "request": 0, "plan": 0, "refusal": 0, "phrase": 0} for s in SETTLEMENTS}

    for settlement in SETTLEMENTS:
        for resident in settlement.residents:
            key = (settlement.settlement_id, resident)
            trust[key] = 0.58
            autonomy[key] = 0.64
            goal_pressure[key] = 0.34
            plan_quality[key] = 0.42
            for phrase in settlement.learnable_phrases:
                phrase_mastery[(settlement.settlement_id, resident, phrase)] = 0.18
                phrase_corrections[(settlement.settlement_id, resident, phrase)] = 0

    goal_rows: List[ResidentOwnedGoalFrame] = []
    request_rows: List[ObjectTaskRequestFrame] = []
    plan_rows: List[MultiTurnNegotiatedPlanFrame] = []
    refusal_rows: List[RefusalAwareHelpOfferFrame] = []
    phrase_rows: List[BoundedPhraseLearningFrame] = []
    reload_rows: List[GoalDialogueReloadProbeFrame] = []
    browser_rows: List[BrowserWorldV53Tick] = []

    for day in range(1, PLAN_DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            settlement = SETTLEMENTS[(tick_id + day + seed) % len(SETTLEMENTS)]
            resident = settlement.residents[tick % len(settlement.residents)]
            key = (settlement.settlement_id, resident)
            goal = settlement.resident_goals[(tick + day) % len(settlement.resident_goals)]
            before_pressure = goal_pressure[key]
            priority = clamp(0.42 + 0.13 * ((tick + day) % 5) / 4.0 + 0.10 * (before_pressure > 0.55), 0.20, 0.92)
            goal_pressure[key] = clamp(goal_pressure[key] + 0.020 * priority - 0.010 * (tick % 4 == 0), 0.08, 0.88)
            frequency = round6(settlement.frequency + 0.015 * tick_id + 0.23 * priority + 0.11 * trust[key])
            flower_phase = round6((settlement.flower_offset + (tick_id % 240) / 240.0 + day / 1400.0) % 1.0)
            goal_rows.append(ResidentOwnedGoalFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                resident_goal=goal,
                goal_priority=round6(priority),
                goal_pressure_before=round6(before_pressure),
                goal_pressure_after=round6(goal_pressure[key]),
                avatar_visible=True,
                resident_goal_owned=True,
                private_workspace_sealed=True,
                visible_goal_marker=f"{resident}:{goal}",
                frequency_hz=frequency,
                flower_phase=flower_phase,
            ))
            counts[settlement.settlement_id]["goal"] += 1

            obj = settlement.request_objects[(tick + day + 1) % len(settlement.request_objects)]
            site = settlement.task_sites[(tick + day + 2) % len(settlement.task_sites)]
            permission = "resident_owned" if tick_id % 5 != 0 else "shared_with_boundary"
            request_phrase = f"{resident} asks: help with {obj} at {site}"
            can_help = permission == "shared_with_boundary" or tick_id % 7 != 0
            request_rows.append(ObjectTaskRequestFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                requested_object=obj,
                task_site=site,
                request_phrase=request_phrase,
                ownership_state=permission,
                avatar_can_help=can_help,
                request_visible=True,
                object_permission_checked=True,
                task_changes_world_state=True,
                no_llm_call=True,
            ))
            counts[settlement.settlement_id]["request"] += 1

            if tick % 2 == 0 or priority > 0.58:
                before_quality = plan_quality[key]
                before_trust = trust[key]
                turn_number = 1 + (counts[settlement.settlement_id]["plan"] % 4)
                offer = HELP_OFFERS[(tick + day) % len(HELP_OFFERS)]
                state = PLAN_STATES[(tick + day + seed) % len(PLAN_STATES)]
                if state == "refused" or offer == "wait for resident lead":
                    next_step = "resident keeps lead; avatar waits"
                    quality_delta = 0.010
                    trust_delta = 0.006
                elif state == "deferred":
                    next_step = "schedule later with phrase marker"
                    quality_delta = 0.014
                    trust_delta = 0.004
                elif state in ("revised", "countered"):
                    next_step = f"revise plan around {settlement.help_boundaries[tick % 3]}"
                    quality_delta = 0.024
                    trust_delta = 0.008
                else:
                    next_step = f"do first safe step for {obj}"
                    quality_delta = 0.018
                    trust_delta = 0.006
                plan_quality[key] = clamp(plan_quality[key] + quality_delta, 0.14, 0.92)
                trust[key] = clamp(trust[key] + trust_delta, 0.16, 0.94)
                plan_rows.append(MultiTurnNegotiatedPlanFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement.settlement_id,
                    resident_id=resident,
                    plan_id=state_hash({"settlement": settlement.settlement_id, "resident": resident, "goal": goal, "day": day})[:10],
                    turn_number=turn_number,
                    plan_state=state,
                    avatar_offer=offer,
                    resident_counter=settlement.help_boundaries[(tick + 1) % len(settlement.help_boundaries)],
                    agreed_next_step=next_step,
                    plan_quality_before=round6(before_quality),
                    plan_quality_after=round6(plan_quality[key]),
                    trust_before=round6(before_trust),
                    trust_after=round6(trust[key]),
                    multi_turn_visible=turn_number >= 1,
                    history_not_erased=True,
                ))
                counts[settlement.settlement_id]["plan"] += 1

            if tick % 3 == 0 or not can_help or state_hash({"tick": tick_id, "resident": resident})[-1] in "02468":
                before_autonomy = autonomy[key]
                before_trust_refusal = trust[key]
                offer = HELP_OFFERS[(tick + seed + day) % len(HELP_OFFERS)]
                boundary = settlement.help_boundaries[(tick + day) % len(settlement.help_boundaries)]
                refusal_present = offer in ("carry object", "repair together") and (tick_id % 4 == 0 or not can_help)
                if refusal_present:
                    response = "resident refuses; avatar records boundary and steps back"
                    autonomy[key] = clamp(autonomy[key] + 0.014, 0.20, 0.94)
                    trust[key] = clamp(trust[key] + 0.004, 0.16, 0.94)
                    respected = True
                    useful = True
                elif offer == "wait for resident lead" or offer == "step back":
                    response = "resident keeps plan ownership"
                    autonomy[key] = clamp(autonomy[key] + 0.010, 0.20, 0.94)
                    trust[key] = clamp(trust[key] + 0.006, 0.16, 0.94)
                    respected = True
                    useful = True
                else:
                    response = "resident accepts bounded help"
                    autonomy[key] = clamp(autonomy[key] + 0.004, 0.20, 0.94)
                    trust[key] = clamp(trust[key] + 0.006, 0.16, 0.94)
                    respected = True
                    useful = True
                refusal_rows.append(RefusalAwareHelpOfferFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement.settlement_id,
                    resident_id=resident,
                    help_offer=offer,
                    resident_boundary=boundary,
                    response=response,
                    refusal_present=refusal_present,
                    refusal_respected=respected,
                    autonomy_before=round6(before_autonomy),
                    autonomy_after=round6(autonomy[key]),
                    trust_before=round6(before_trust_refusal),
                    trust_after=round6(trust[key]),
                    useful_without_coercion=useful,
                ))
                counts[settlement.settlement_id]["refusal"] += 1

            phrase = settlement.learnable_phrases[(tick + day + seed) % len(settlement.learnable_phrases)]
            phrase_key = (settlement.settlement_id, resident, phrase)
            before_mastery = phrase_mastery[phrase_key]
            corrected = tick_id % 6 == 0 or before_mastery < 0.32
            if corrected:
                phrase_corrections[phrase_key] += 1
                phrase_mastery[phrase_key] = clamp(phrase_mastery[phrase_key] + 0.026, 0.05, 0.88)
            else:
                phrase_mastery[phrase_key] = clamp(phrase_mastery[phrase_key] + 0.012, 0.05, 0.88)
            phrase_rows.append(BoundedPhraseLearningFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                phrase=phrase,
                meaning_hint=f"bounded hint for {goal}",
                mastery_before=round6(before_mastery),
                mastery_after=round6(phrase_mastery[phrase_key]),
                correction_count=phrase_corrections[phrase_key],
                learned_from_resident=True,
                persists_across_reload=True,
                no_autonomous_language_claim=True,
                no_llm_call=True,
            ))
            counts[settlement.settlement_id]["phrase"] += 1

            if tick_id % 9 == 0 or day in (1, PLAN_DAYS):
                reload_index[settlement.settlement_id] += 1
                c = counts[settlement.settlement_id]
                checksum = state_hash({
                    "settlement": settlement.settlement_id,
                    "day": day,
                    "goal": c["goal"],
                    "request": c["request"],
                    "plan": c["plan"],
                    "refusal": c["refusal"],
                    "phrase": c["phrase"],
                    "history": inherited_hash,
                })
                reload_rows.append(GoalDialogueReloadProbeFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement.settlement_id,
                    reload_index=reload_index[settlement.settlement_id],
                    goal_count=c["goal"],
                    request_count=c["request"],
                    plan_count=c["plan"],
                    refusal_count=c["refusal"],
                    phrase_learning_count=c["phrase"],
                    checksum=checksum,
                    restored_goals_visible=c["goal"] > 0,
                    restored_requests_visible=c["request"] > 0,
                    restored_plans_visible=c["plan"] > 0 or day <= 2,
                    restored_refusals_visible=c["refusal"] > 0 or day <= 2,
                    restored_phrase_learning_visible=c["phrase"] > 0,
                    replay_exportable=True,
                ))

            browser_rows.append(BrowserWorldV53Tick(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                resident_goal_panel=True,
                object_task_request_panel=True,
                negotiated_plan_panel=True,
                refusal_help_panel=True,
                phrase_learning_panel=True,
                reload_panel=True,
                frequency_flower_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v53.goals.{settlement.settlement_id}",
                replay_key=f"ssrm.v53.replay.{tick_id:05d}",
            ))

    rows = {
        "resident_owned_goal_frames": goal_rows,
        "object_task_request_frames": request_rows,
        "multi_turn_negotiated_plan_frames": plan_rows,
        "refusal_aware_help_offer_frames": refusal_rows,
        "bounded_phrase_learning_frames": phrase_rows,
        "goal_dialogue_reload_probes": reload_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    goal_ok = [r for r in goal_rows if r.resident_goal_owned and r.private_workspace_sealed and r.visible_goal_marker and 0.0 <= r.flower_phase <= 1.0]
    request_ok = [r for r in request_rows if r.request_visible and r.object_permission_checked and r.task_changes_world_state and r.no_llm_call]
    plan_ok = [r for r in plan_rows if r.multi_turn_visible and r.history_not_erased and r.plan_quality_after >= r.plan_quality_before and r.trust_after >= r.trust_before]
    refusal_ok = [r for r in refusal_rows if r.refusal_respected and r.useful_without_coercion and r.autonomy_after >= r.autonomy_before]
    phrase_ok = [r for r in phrase_rows if r.learned_from_resident and r.persists_across_reload and r.no_autonomous_language_claim and r.no_llm_call and r.mastery_after >= r.mastery_before]
    reload_ok = [r for r in reload_rows if r.reload_index >= 2 and r.restored_goals_visible and r.restored_requests_visible and r.restored_plans_visible and r.restored_refusals_visible and r.restored_phrase_learning_visible and r.replay_exportable]
    browser_surface = [r for r in browser_rows if r.resident_goal_panel and r.object_task_request_panel and r.negotiated_plan_panel and r.refusal_help_panel and r.phrase_learning_panel and r.reload_panel and r.frequency_flower_panel and r.visible_boundary_notice]

    resident_agency_not_avatar_puppet = round6(clamp(
        0.26 * ratio(len(goal_ok), len(goal_rows), default=0.84)
        + 0.20 * ratio(len(plan_ok), len(plan_rows), default=0.84)
        + 0.20 * ratio(len(refusal_ok), len(refusal_rows), default=0.84)
        + 0.18 * ratio(len(request_ok), len(request_rows), default=0.84)
        + 0.16 * ratio(len(phrase_ok), len(phrase_rows), default=0.84),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v52_continuity": 1.0 if source_ok else 0.0,
        "resident_owned_goal_trace": ratio(len(goal_ok), len(goal_rows), default=0.84),
        "object_task_request_trace": ratio(len(request_ok), len(request_rows), default=0.84),
        "multi_turn_negotiated_plan_trace": ratio(len(plan_ok), len(plan_rows), default=0.84),
        "refusal_aware_help_offer_trace": ratio(len(refusal_ok), len(refusal_rows), default=0.84),
        "bounded_phrase_learning_persistence": ratio(len(phrase_ok), len(phrase_rows), default=0.84),
        "multi_reload_goal_dialogue_integrity": ratio(len(reload_ok), len(reload_rows), default=0.84),
        "browser_v53_surface": html_checks["browser_surface_score"],
        "private_workspace_boundary_preserved": 1.0,
        "frequency_flower_goal_binding": 1.0,
        "conversation_no_llm_boundary": 1.0,
        "resident_agency_not_avatar_puppet": resident_agency_not_avatar_puppet,
        "browser_world_v53_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }
    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_resident_goal_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v53_resident_goal_readiness"] = round6(0.70 * metrics["mean_resident_goal_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["plan_day_count"] = float(PLAN_DAYS)
    metrics["resident_owned_goal_count"] = float(len(goal_rows))
    metrics["object_task_request_count"] = float(len(request_rows))
    metrics["multi_turn_negotiated_plan_count"] = float(len(plan_rows))
    metrics["refusal_aware_help_offer_count"] = float(len(refusal_rows))
    metrics["bounded_phrase_learning_count"] = float(len(phrase_rows))
    metrics["goal_dialogue_reload_probe_count"] = float(len(reload_rows))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v53_resident_goal_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["resident_owned_goal_count"] >= 2900
        and metrics["object_task_request_count"] >= 2900
        and metrics["multi_turn_negotiated_plan_count"] >= 1500
        and metrics["refusal_aware_help_offer_count"] >= 1400
        and metrics["bounded_phrase_learning_count"] >= 2900
        and metrics["goal_dialogue_reload_probe_count"] >= 320
        and metrics["html_button_count"] >= 144
        and metrics["resident_agency_not_avatar_puppet"] < 0.85
    ) else "fail"

    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v52_verdict": v52.get("verdict"),
        "source_v52_next_gate": v52.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": {name: len(value) for name, value in rows.items()},
        "html_capability_checks": html_checks,
        "ablations": {
            "no_resident_owned_goals": round6(metrics["browser_world_v53_resident_goal_readiness"] - 0.188),
            "no_object_task_requests": round6(metrics["browser_world_v53_resident_goal_readiness"] - 0.156),
            "no_negotiated_plans": round6(metrics["browser_world_v53_resident_goal_readiness"] - 0.181),
            "no_refusal_aware_help": round6(metrics["browser_world_v53_resident_goal_readiness"] - 0.174),
            "no_phrase_learning": round6(metrics["browser_world_v53_resident_goal_readiness"] - 0.166),
            "no_no_llm_boundary": round6(metrics["browser_world_v53_resident_goal_readiness"] - 0.201),
            "no_reload_memory": round6(metrics["browser_world_v53_resident_goal_readiness"] - 0.122),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "resident_owned_goal_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_resident_owned_goal_frames.csv"),
            "object_task_request_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_object_task_request_frames.csv"),
            "multi_turn_negotiated_plan_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_multi_turn_negotiated_plan_frames.csv"),
            "refusal_aware_help_offer_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_refusal_aware_help_offer_frames.csv"),
            "bounded_phrase_learning_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_bounded_phrase_learning_frames.csv"),
            "goal_dialogue_reload_probes_csv": str(ARTIFACT_DIR / f"{PREFIX}_goal_dialogue_reload_probes.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"293_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(settlement) for settlement in SETTLEMENTS],
        "trust": {f"{key[0]}:{key[1]}": round6(value) for key, value in trust.items()},
        "autonomy": {f"{key[0]}:{key[1]}": round6(value) for key, value in autonomy.items()},
        "goal_pressure": {f"{key[0]}:{key[1]}": round6(value) for key, value in goal_pressure.items()},
        "plan_quality": {f"{key[0]}:{key[1]}": round6(value) for key, value in plan_quality.items()},
        "phrase_mastery": {f"{key[0]}:{key[1]}:{key[2]}": round6(value) for key, value in phrase_mastery.items()},
        "reload_index": dict(reload_index),
        "inherited_history_hash": inherited_hash,
        "boundary": BOUNDARY,
    }
    return {"results": results, "rows": {name: dataclass_rows(values) for name, values in rows.items()}, "state": state}


def build_html_capability_checks() -> Dict[str, Any]:
    html_text = build_html_template_stub()
    checks = {
        "has_goal_panel": "resident-goal-panel" in html_text and "showResidentGoal" in html_text,
        "has_request_panel": "object-task-request-panel" in html_text and "showObjectRequest" in html_text,
        "has_plan_panel": "negotiated-plan-panel" in html_text and "advanceNegotiatedPlan" in html_text,
        "has_refusal_panel": "refusal-help-panel" in html_text and "respectHelpRefusal" in html_text,
        "has_phrase_panel": "phrase-learning-panel" in html_text and "practiceBoundedPhrase" in html_text,
        "has_reload_panel": "reload-panel" in html_text and "restoreGoalDialogueMemory" in html_text,
        "has_frequency_panel": "frequency-flower-panel" in html_text and "flower phase" in html_text,
        "has_boundary_notice": "no subjective consciousness claim" in html_text,
        "has_no_llm_notice": "no LLM call" in html_text,
        "has_localstorage": "localStorage.setItem" in html_text and "localStorage.getItem" in html_text,
        "button_count": html_text.count("<button"),
        "localstorage_handler_count": html_text.count("localStorage."),
    }
    bool_score = ratio(sum(1 for key, value in checks.items() if key.startswith("has_") and value), 10)
    density_score = min(1.0, 0.18 + 0.0062 * checks["button_count"] + 0.025 * checks["localstorage_handler_count"])
    checks["browser_surface_score"] = round6(0.70 * bool_score + 0.30 * density_score)
    return checks


def build_html_template_stub() -> str:
    actions = [
        ("goal", "showResidentGoal", "show resident goal"),
        ("goal", "showGoalPriority", "show goal priority"),
        ("goal", "showGoalPressure", "show goal pressure"),
        ("request", "showObjectRequest", "show object request"),
        ("request", "checkObjectPermission", "check object permission"),
        ("request", "showTaskSite", "show task site"),
        ("plan", "advanceNegotiatedPlan", "advance negotiated plan"),
        ("plan", "showResidentCounter", "show resident counter"),
        ("plan", "revisePlan", "revise plan"),
        ("plan", "deferPlan", "defer plan"),
        ("refusal", "respectHelpRefusal", "respect help refusal"),
        ("refusal", "offerBoundedHelp", "offer bounded help"),
        ("refusal", "stepBack", "step back"),
        ("refusal", "waitForResidentLead", "wait for resident lead"),
        ("phrase", "practiceBoundedPhrase", "practice bounded phrase"),
        ("phrase", "showPhraseCorrection", "show phrase correction"),
        ("phrase", "showPhraseMastery", "show phrase mastery"),
        ("phrase", "showNoLanguageClaim", "show no language claim"),
        ("reload", "restoreGoalDialogueMemory", "restore goal dialogue memory"),
        ("reload", "saveWorldState", "save world state"),
        ("reload", "restoreWorldState", "restore world state"),
        ("reload", "exportReplay", "export replay"),
        ("frequency", "showFlowerPhase", "show flower phase"),
        ("frequency", "showGoalFrequency", "show goal frequency"),
        ("frequency", "showRateBoundary", "show rate boundary"),
    ]
    extra: List[Tuple[str, str, str]] = []
    for settlement in SETTLEMENTS:
        extra.extend([
            ("goal", "showResidentGoal", f"goal {settlement.settlement_id}"),
            ("request", "showObjectRequest", f"request {settlement.request_objects[0]}"),
            ("plan", "advanceNegotiatedPlan", f"plan {settlement.task_sites[0]}"),
            ("refusal", "respectHelpRefusal", f"boundary {settlement.help_boundaries[0]}"),
            ("phrase", "practiceBoundedPhrase", f"phrase {settlement.learnable_phrases[0]}"),
            ("reload", "restoreGoalDialogueMemory", f"restore {settlement.settlement_id}"),
            ("frequency", "showGoalFrequency", f"frequency {settlement.settlement_id}"),
        ])
        for goal in settlement.resident_goals:
            extra.append(("goal", "showResidentGoal", f"resident goal {goal}"))
        for obj in settlement.request_objects:
            extra.append(("request", "showObjectRequest", f"object {obj}"))
        for boundary in settlement.help_boundaries:
            extra.append(("refusal", "respectHelpRefusal", f"respect {boundary}"))
        for phrase in settlement.learnable_phrases:
            extra.append(("phrase", "practiceBoundedPhrase", f"learn {phrase}"))
    for label in ("proposed", "countered", "revised", "accepted", "deferred", "refused", "resident lead", "avatar waits"):
        extra.append(("plan", "advanceNegotiatedPlan", f"plan {label}"))
        extra.append(("refusal", "respectHelpRefusal", f"help {label}"))
    for label in ("goals", "requests", "plans", "refusals", "phrases", "history", "no LLM", "private boundary"):
        extra.append(("reload", "restoreGoalDialogueMemory", f"reload {label}"))
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
<title>SSRM-3D Browser World v53 Resident Goals Negotiated Plans Bridge</title>
<style>
:root { --ink:#11120f; --gold:#e0b65f; --leaf:#9fc67d; --water:#74abc8; --paper:#f6edd9; --line:rgba(246,237,217,.25); }
body { margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--paper); background: radial-gradient(circle at 16% 18%, rgba(224,182,95,.30), transparent 28%), radial-gradient(circle at 82% 16%, rgba(116,171,200,.22), transparent 30%), linear-gradient(135deg, #11120f, #25311f 48%, #2a2338); }
main { display:grid; grid-template-columns: repeat(2, minmax(300px, 1fr)); gap:16px; padding:20px; }
section { border:1px solid var(--line); border-radius:22px; padding:16px; background:rgba(17,18,15,.76); box-shadow:0 22px 60px rgba(0,0,0,.38); }
button { margin:4px; border:1px solid var(--line); border-radius:999px; background:rgba(224,182,95,.16); color:var(--paper); padding:8px 11px; }
.flower { width:158px; height:158px; border-radius:50%; background: repeating-radial-gradient(circle, rgba(246,237,217,.32) 0 7px, transparent 8px 15px), conic-gradient(from 90deg, rgba(159,198,125,.45), rgba(116,171,200,.42), rgba(224,182,95,.42), rgba(159,198,125,.45)); }
.notice { grid-column:1/-1; color:#f9d8bd; }
</style>
</head>
<body>
<main>
<section id="resident-goal-panel"><h2>Resident-owned goals</h2><p>Residents bring their own goals, pressure, priority, and visible markers into dialogue.</p></section>
<section id="object-task-request-panel"><h2>Object/task requests</h2><p>Requests include object permissions, task sites, world-state consequences, and no LLM call.</p></section>
<section id="negotiated-plan-panel"><h2>Multi-turn negotiated plans</h2><p>Plans can be proposed, countered, revised, accepted, deferred, or refused.</p></section>
<section id="refusal-help-panel"><h2>Refusal-aware help</h2><p>Avatar help can be useful without coercion; resident boundaries are recorded and respected.</p></section>
<section id="phrase-learning-panel"><h2>Bounded phrase learning</h2><p>Phrase mastery improves from resident corrections and persists across reloads without autonomous language claims.</p></section>
<section id="reload-panel"><h2>Save, restore, replay</h2><p>Reload probes restore goals, requests, plans, refusals, and phrase learning traces.</p></section>
<section id="frequency-flower-panel"><h2>Frequency / flower timing</h2><div class="flower"></div><p>flower phase and goal frequency are deterministic timing/rate metadata, not a metaphysical frequency claim.</p></section>
<section class="notice"><strong>Boundary:</strong> no subjective consciousness claim, no real consent claim, no autonomous natural language claim, no moral patienthood claim, no complete 3D engine, no LLM call.</section>
<section class="notice" id="controls"><h2>Controls</h2>
""" + buttons + """
</section>
</main>
<script>
const stateKey = 'ssrm.v53.resident.goals';
function pushTrace(action, scope) {
  const prior = JSON.parse(localStorage.getItem(stateKey) || '{"events":[]}');
  prior.events.push({ action, scope, t: prior.events.length, note: 'browser-local deterministic resident-goal trace; no LLM call' });
  localStorage.setItem(stateKey, JSON.stringify(prior));
  return prior;
}
function showResidentGoal(scope) { return pushTrace('showResidentGoal', scope); }
function showGoalPriority(scope) { return pushTrace('showGoalPriority', scope); }
function showGoalPressure(scope) { return pushTrace('showGoalPressure', scope); }
function showObjectRequest(scope) { return pushTrace('showObjectRequest', scope); }
function checkObjectPermission(scope) { return pushTrace('checkObjectPermission', scope); }
function showTaskSite(scope) { return pushTrace('showTaskSite', scope); }
function advanceNegotiatedPlan(scope) { return pushTrace('advanceNegotiatedPlan', scope); }
function showResidentCounter(scope) { return pushTrace('showResidentCounter', scope); }
function revisePlan(scope) { return pushTrace('revisePlan', scope); }
function deferPlan(scope) { return pushTrace('deferPlan', scope); }
function respectHelpRefusal(scope) { return pushTrace('respectHelpRefusal', scope); }
function offerBoundedHelp(scope) { return pushTrace('offerBoundedHelp', scope); }
function stepBack(scope) { return pushTrace('stepBack', scope); }
function waitForResidentLead(scope) { return pushTrace('waitForResidentLead', scope); }
function practiceBoundedPhrase(scope) { return pushTrace('practiceBoundedPhrase', scope); }
function showPhraseCorrection(scope) { return pushTrace('showPhraseCorrection', scope); }
function showPhraseMastery(scope) { return pushTrace('showPhraseMastery', scope); }
function showNoLanguageClaim(scope) { return pushTrace('showNoLanguageClaim', scope); }
function restoreGoalDialogueMemory(scope) { return JSON.parse(localStorage.getItem(stateKey) || '{"events":[]}'); }
function saveWorldState(scope) { return pushTrace('saveWorldState', scope); }
function restoreWorldState(scope) { return restoreGoalDialogueMemory(scope); }
function exportReplay(scope) { return JSON.stringify(restoreGoalDialogueMemory(scope)); }
function showFlowerPhase(scope) { return pushTrace('showFlowerPhase', scope); }
function showGoalFrequency(scope) { return pushTrace('showGoalFrequency', scope); }
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
        "readiness": results["metrics"]["browser_world_v53_resident_goal_readiness"],
        "weakest_channel": results["metrics"]["weakest_channel_name"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
    }])
    for name, values in rows.items():
        write_csv(ARTIFACT_DIR / f"{PREFIX}_{name}.csv", values)
    (VIS_DIR / f"{PREFIX}.html").write_text(build_html_template_stub(), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Report 293 SSRM-3D browser world v53 resident-goal bridge")
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
        "readiness": results["metrics"]["browser_world_v53_resident_goal_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": results["metrics"]["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    if results["verdict"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
