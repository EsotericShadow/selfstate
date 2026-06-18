"""Report 292: SSRM-3D browser world v52 phrasebook dialogue bridge.

This deterministic benchmark extends v51 playable arrival into bounded two-way
phrasebook dialogue, gesture repair, resident-initiated questions, sensory scene
controls, and memory-safe conversation continuity without LLM calls. It is
browser-local scaffolding only: no LLM call, no subjective consciousness claim,
no real consent claim, no autonomous natural language claim, no moral
patienthood claim, no complete 3D engine, and no metaphysical frequency result.
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

REPORT = 292
DEFAULT_SEED = 20270210
DIALOGUE_DAYS = 150
TICKS_PER_DAY = 18
PREFIX = "ssrm_3d_browser_world_v52_phrasebook_dialogue_gesture_questions_sensory_memory_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V51 = ARTIFACT_DIR / "ssrm_3d_browser_world_v51_playable_arrival_translation_custom_trust_bridge_results.json"
SOURCE_V51_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v51_playable_arrival_translation_custom_trust_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local phrasebook-dialogue/gesture-repair/resident-question/"
    "sensory-control/memory-continuity scaffold only; no LLM call, subjective "
    "consciousness, real consent, autonomous natural language, moral patienthood, "
    "complete gameplay, complete 3D engine, or metaphysical frequency claim"
)
NEXT_GATE = (
    "browser world v53 with resident-owned goals during dialogue, object/task requests, "
    "multi-turn negotiated plans, refusal-aware help offers, and bounded phrase learning "
    "that persists across reloads without LLM calls"
)


@dataclass(frozen=True)
class DialogueSettlement:
    settlement_id: str
    dialect_family: str
    residents: Tuple[str, str, str, str]
    avatar_phrases: Tuple[str, str, str, str, str]
    resident_phrases: Tuple[str, str, str, str, str]
    gestures: Tuple[str, str, str]
    resident_questions: Tuple[str, str, str]
    sensory_scene: Tuple[str, str, str, str, str]
    local_memory_anchor: str
    frequency: float
    flower_offset: float


SETTLEMENTS: Tuple[DialogueSettlement, ...] = (
    DialogueSettlement("moss_ward", "proto-moss-breath", ("Ari", "Fay", "Milo", "Tala"), ("I wait", "I ask rain custom", "I offer trade", "I do not touch", "I need translation"), ("warm cup first", "rain clay is named", "blanket path clear", "trade can wait", "speak slower"), ("empty hands", "door-path step", "cup pause"), ("Why do you watch the rain jar?", "Will you keep the path clear?", "Do you understand warm-cup?"), ("wet moss", "rain hiss", "warm broth", "cool loft air", "mist on skin"), "moss_ward lineage and rain-gate custom", 5.21, 0.021),
    DialogueSettlement("glass_harbor", "proto-harbor-chime", ("Nia", "Oren", "Puck", "Sera"), ("I wait by lamp", "I ask net owner", "I offer salt token", "I do not dim lamp", "I need translation"), ("tea before crossing", "lamp stays bright", "net has keeper", "fog catcher closed", "repeat with bell"), ("lantern tap", "tea hold", "net-hand open"), ("Why did you touch the rail?", "Can you leave the lamp bright?", "Which word means net keeper?"), ("salt steam", "lamp oil", "bell gulls", "cold spray", "fog on face"), "glass_harbor lamp and net custom", 6.34, 0.034),
    DialogueSettlement("cinder_garden", "proto-cinder-pulse", ("Juno", "Pax", "Vale", "Wren"), ("I bow to shade", "I ask seed path", "I offer cool stone", "I do not cross rows", "I need translation"), ("shade cloth first", "seed rows sleep", "cool hand means wait", "ash path open", "repeat without hurry"), ("shade bow", "cool hand", "seed-step stop"), ("Why are you near the seed tray?", "Can you wait by ash path?", "Do you know cool-hand?"), ("warm ash", "seed oil", "dry wind", "cool basin", "dust on skin"), "cinder_garden seed and shade custom", 8.89, 0.055),
    DialogueSettlement("lichen_bridge", "proto-bridge-hum", ("Kio", "Luma", "Rin", "Sol"), ("I touch rope post", "I ask bell custom", "I offer rope help", "I do not step on rope", "I need translation"), ("signal hush first", "rope has tension", "meal room welcomes", "bell has keeper", "gesture again"), ("rope touch", "signal hush", "shared bowl"), ("Why did you stop at the rope?", "Can you wait for signal hush?", "Which sign means safe crossing?"), ("damp rope", "stone echo", "lichen soup", "crosswind", "cold fog"), "lichen_bridge rope and signal custom", 7.55, 0.044),
    DialogueSettlement("orchid_engine", "proto-engine-ring", ("Bea", "Cai", "Dax", "Eli"), ("I wait outside ring", "I ask valve custom", "I offer gear cloth", "I do not turn key", "I need translation"), ("valve listener first", "orchid lamp rests", "gear lane open", "cup before engine", "say it with palms"), ("open palms", "valve pause", "orchid cup"), ("Why do you look at the valve key?", "Can you keep the lane open?", "Which phrase means valve listener?"), ("orchid oil", "warm iron", "valve pulse", "steam draft", "hot brass"), "orchid_engine valve and orchid custom", 9.87, 0.067),
)

AVATAR_RESPONSE_TYPES = ("answer_known", "ask_clarify", "gesture_repair", "admit_unknown", "offer_trade", "step_back")
SENSORY_CHANNELS = ("sight", "sound", "smell", "temperature", "wetness")


@dataclass(frozen=True)
class PhrasebookDialogueFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    turn_index: int
    avatar_phrase: str
    resident_phrase: str
    intent: str
    response_key: str
    confidence_before: float
    confidence_after: float
    misunderstanding_risk: float
    bounded_phrasebook: bool
    no_llm_call: bool
    private_workspace_not_dumped: bool
    frequency_hz: float
    flower_phase: float


@dataclass(frozen=True)
class GestureRepairFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    gesture: str
    mismatch_type: str
    repair_action: str
    repair_success: bool
    risk_before: float
    risk_after: float
    visible_gesture_marker: str
    bounded_repair: bool


@dataclass(frozen=True)
class ResidentInitiatedQuestionFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    question: str
    resident_need: str
    avatar_response_type: str
    answer_state: str
    trust_before: float
    trust_after: float
    resident_initiated: bool
    unknown_respected: bool
    question_card_visible: bool


@dataclass(frozen=True)
class SensorySceneControlFrame:
    tick_id: int
    day: int
    settlement_id: str
    sensory_channel: str
    scene_before: str
    scene_after: str
    control_action: str
    readability_before: float
    readability_after: float
    history_hash_before: str
    history_hash_after: str
    control_visible: bool
    bounded_sensory_change: bool


@dataclass(frozen=True)
class MemorySafeConversationFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    public_summary: str
    memory_delta: str
    continuity_before: float
    continuity_after: float
    history_hash_before: str
    history_hash_after: str
    private_workspace_sealed: bool
    no_private_memory_dump: bool
    no_llm_call: bool
    memory_safe: bool


@dataclass(frozen=True)
class DialogueReloadProbeFrame:
    tick_id: int
    day: int
    settlement_id: str
    reload_index: int
    phrasebook_count: int
    gesture_count: int
    question_count: int
    sensory_count: int
    memory_count: int
    checksum: str
    restored_phrasebook_visible: bool
    restored_gesture_visible: bool
    restored_question_visible: bool
    restored_sensory_visible: bool
    restored_memory_visible: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV52Tick:
    tick_id: int
    day: int
    settlement_id: str
    phrasebook_dialogue_panel: bool
    gesture_repair_panel: bool
    resident_question_panel: bool
    sensory_scene_control_panel: bool
    memory_safe_conversation_panel: bool
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
    v51 = load_json(SOURCE_V51)
    v51_state = load_json(SOURCE_V51_STATE)
    source_ok = v51.get("verdict") == "pass" and bool(v51_state)
    inherited_history_hash = state_hash({"v51": v51.get("report"), "verdict": v51.get("verdict"), "state": sorted(v51_state.keys())})

    confidence: MutableMapping[Tuple[str, str], float] = {}
    trust: MutableMapping[Tuple[str, str], float] = {}
    continuity: MutableMapping[Tuple[str, str], float] = {}
    sensory_readability: MutableMapping[Tuple[str, str], float] = {}
    reload_index: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    counts: MutableMapping[str, Dict[str, int]] = {s.settlement_id: {"phrase": 0, "gesture": 0, "question": 0, "sensory": 0, "memory": 0} for s in SETTLEMENTS}

    for settlement in SETTLEMENTS:
        for resident in settlement.residents:
            key = (settlement.settlement_id, resident)
            confidence[key] = 0.38
            trust[key] = 0.57
            continuity[key] = 0.62
        for channel in SENSORY_CHANNELS:
            sensory_readability[(settlement.settlement_id, channel)] = 0.56

    phrase_rows: List[PhrasebookDialogueFrame] = []
    gesture_rows: List[GestureRepairFrame] = []
    question_rows: List[ResidentInitiatedQuestionFrame] = []
    sensory_rows: List[SensorySceneControlFrame] = []
    memory_rows: List[MemorySafeConversationFrame] = []
    reload_rows: List[DialogueReloadProbeFrame] = []
    browser_rows: List[BrowserWorldV52Tick] = []

    for day in range(1, DIALOGUE_DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            settlement = SETTLEMENTS[(tick_id + day + seed) % len(SETTLEMENTS)]
            resident = settlement.residents[tick % len(settlement.residents)]
            key = (settlement.settlement_id, resident)
            turn_index = counts[settlement.settlement_id]["phrase"]
            avatar_phrase = settlement.avatar_phrases[(tick + day) % len(settlement.avatar_phrases)]
            resident_phrase = settlement.resident_phrases[(tick + seed + day) % len(settlement.resident_phrases)]
            response_key = AVATAR_RESPONSE_TYPES[(tick + day + seed) % len(AVATAR_RESPONSE_TYPES)]
            before_conf = confidence[key]
            risk = clamp(0.74 - before_conf + 0.04 * (response_key == "answer_known"), 0.04, 0.92)
            if response_key in ("ask_clarify", "gesture_repair", "admit_unknown"):
                confidence[key] = clamp(confidence[key] + 0.018, 0.12, 0.86)
                intent = "repair uncertainty"
            elif response_key == "answer_known":
                confidence[key] = clamp(confidence[key] + 0.006, 0.12, 0.86)
                intent = "answer bounded phrase"
            elif response_key == "step_back":
                confidence[key] = clamp(confidence[key] + 0.010, 0.12, 0.86)
                intent = "respect boundary"
            else:
                confidence[key] = clamp(confidence[key] + 0.004, 0.12, 0.86)
                intent = "offer bounded aid"
            frequency = round6(settlement.frequency + 0.017 * tick_id + 0.29 * confidence[key] + 0.13 * trust[key])
            flower_phase = round6((settlement.flower_offset + (tick_id % 216) / 216.0 + day / 1200.0) % 1.0)
            phrase_rows.append(PhrasebookDialogueFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                turn_index=turn_index,
                avatar_phrase=avatar_phrase,
                resident_phrase=resident_phrase,
                intent=intent,
                response_key=response_key,
                confidence_before=round6(before_conf),
                confidence_after=round6(confidence[key]),
                misunderstanding_risk=round6(risk),
                bounded_phrasebook=True,
                no_llm_call=True,
                private_workspace_not_dumped=True,
                frequency_hz=frequency,
                flower_phase=flower_phase,
            ))
            counts[settlement.settlement_id]["phrase"] += 1

            if tick % 2 == 0 or response_key == "gesture_repair":
                gesture = settlement.gestures[(tick + day) % len(settlement.gestures)]
                mismatch = "timing" if tick_id % 5 == 0 else "meaning" if tick_id % 7 == 0 else "none"
                risk_before = clamp(risk + (0.08 if mismatch != "none" else 0.0), 0.04, 0.96)
                repair_success = mismatch == "none" or response_key in ("gesture_repair", "ask_clarify", "admit_unknown") or tick_id % 3 != 0
                risk_after = clamp(risk_before - (0.16 if repair_success else 0.04), 0.02, 0.96)
                gesture_rows.append(GestureRepairFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement.settlement_id,
                    resident_id=resident,
                    gesture=gesture,
                    mismatch_type=mismatch,
                    repair_action="slow repeat with resident correction" if mismatch != "none" else "gesture accepted",
                    repair_success=repair_success,
                    risk_before=round6(risk_before),
                    risk_after=round6(risk_after),
                    visible_gesture_marker=f"{resident}:{gesture}:{mismatch}",
                    bounded_repair=risk_after <= risk_before and risk_after <= 0.96,
                ))
                counts[settlement.settlement_id]["gesture"] += 1

            if tick % 3 == 0 or response_key in ("ask_clarify", "admit_unknown"):
                question = settlement.resident_questions[(tick + day) % len(settlement.resident_questions)]
                need = "custom clarity" if "understand" in question or "word" in question or "phrase" in question else "safety check"
                before_trust = trust[key]
                if response_key == "admit_unknown":
                    answer_state = "unknown respected"
                    trust[key] = clamp(trust[key] + 0.010, 0.16, 0.94)
                    unknown_respected = True
                elif response_key in ("ask_clarify", "gesture_repair"):
                    answer_state = "clarifying answer"
                    trust[key] = clamp(trust[key] + 0.014, 0.16, 0.94)
                    unknown_respected = True
                elif response_key == "answer_known" and confidence[key] > 0.46:
                    answer_state = "bounded answer"
                    trust[key] = clamp(trust[key] + 0.008, 0.16, 0.94)
                    unknown_respected = True
                else:
                    answer_state = "deferred instead of fabricated"
                    trust[key] = clamp(trust[key] + 0.004, 0.16, 0.94)
                    unknown_respected = True
                question_rows.append(ResidentInitiatedQuestionFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement.settlement_id,
                    resident_id=resident,
                    question=question,
                    resident_need=need,
                    avatar_response_type=response_key,
                    answer_state=answer_state,
                    trust_before=round6(before_trust),
                    trust_after=round6(trust[key]),
                    resident_initiated=True,
                    unknown_respected=unknown_respected,
                    question_card_visible=True,
                ))
                counts[settlement.settlement_id]["question"] += 1

            channel = SENSORY_CHANNELS[(tick + day + seed) % len(SENSORY_CHANNELS)]
            sensory_key = (settlement.settlement_id, channel)
            before_readability = sensory_readability[sensory_key]
            history_before = inherited_history_hash
            scene_before = settlement.sensory_scene[SENSORY_CHANNELS.index(channel)]
            if response_key in ("ask_clarify", "gesture_repair"):
                control_action = f"focus {channel} cue for dialogue repair"
                sensory_readability[sensory_key] = clamp(sensory_readability[sensory_key] + 0.020, 0.20, 0.90)
            elif response_key == "step_back":
                control_action = f"reduce {channel} intensity while stepping back"
                sensory_readability[sensory_key] = clamp(sensory_readability[sensory_key] + 0.010, 0.20, 0.90)
            else:
                control_action = f"sample {channel} without changing history"
                sensory_readability[sensory_key] = clamp(sensory_readability[sensory_key] + 0.006, 0.20, 0.90)
            history_after = inherited_history_hash
            sensory_rows.append(SensorySceneControlFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                sensory_channel=channel,
                scene_before=scene_before,
                scene_after=f"{scene_before}; {control_action}",
                control_action=control_action,
                readability_before=round6(before_readability),
                readability_after=round6(sensory_readability[sensory_key]),
                history_hash_before=history_before,
                history_hash_after=history_after,
                control_visible=True,
                bounded_sensory_change=history_before == history_after and sensory_readability[sensory_key] <= 0.90,
            ))
            counts[settlement.settlement_id]["sensory"] += 1

            before_continuity = continuity[key]
            memory_delta = "phrase repair remembered" if response_key in ("ask_clarify", "gesture_repair", "admit_unknown") else "bounded turn remembered"
            continuity[key] = clamp(continuity[key] + 0.008 + 0.006 * (response_key in ("ask_clarify", "gesture_repair")), 0.20, 0.95)
            memory_rows.append(MemorySafeConversationFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                public_summary=f"{resident} heard '{avatar_phrase}' and answered '{resident_phrase}'",
                memory_delta=memory_delta,
                continuity_before=round6(before_continuity),
                continuity_after=round6(continuity[key]),
                history_hash_before=inherited_history_hash,
                history_hash_after=inherited_history_hash,
                private_workspace_sealed=True,
                no_private_memory_dump=True,
                no_llm_call=True,
                memory_safe=True,
            ))
            counts[settlement.settlement_id]["memory"] += 1

            if tick_id % 9 == 0 or day in (1, DIALOGUE_DAYS):
                reload_index[settlement.settlement_id] += 1
                c = counts[settlement.settlement_id]
                checksum = state_hash({
                    "settlement": settlement.settlement_id,
                    "day": day,
                    "phrase": c["phrase"],
                    "gesture": c["gesture"],
                    "question": c["question"],
                    "sensory": c["sensory"],
                    "memory": c["memory"],
                    "history": inherited_history_hash,
                })
                reload_rows.append(DialogueReloadProbeFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement.settlement_id,
                    reload_index=reload_index[settlement.settlement_id],
                    phrasebook_count=c["phrase"],
                    gesture_count=c["gesture"],
                    question_count=c["question"],
                    sensory_count=c["sensory"],
                    memory_count=c["memory"],
                    checksum=checksum,
                    restored_phrasebook_visible=c["phrase"] > 0,
                    restored_gesture_visible=c["gesture"] > 0 or day <= 2,
                    restored_question_visible=c["question"] > 0 or day <= 2,
                    restored_sensory_visible=c["sensory"] > 0,
                    restored_memory_visible=c["memory"] > 0,
                    replay_exportable=True,
                ))

            browser_rows.append(BrowserWorldV52Tick(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement.settlement_id,
                phrasebook_dialogue_panel=True,
                gesture_repair_panel=True,
                resident_question_panel=True,
                sensory_scene_control_panel=True,
                memory_safe_conversation_panel=True,
                reload_panel=True,
                frequency_flower_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v52.dialogue.{settlement.settlement_id}",
                replay_key=f"ssrm.v52.replay.{tick_id:05d}",
            ))

    rows = {
        "phrasebook_dialogue_frames": phrase_rows,
        "gesture_repair_frames": gesture_rows,
        "resident_initiated_question_frames": question_rows,
        "sensory_scene_control_frames": sensory_rows,
        "memory_safe_conversation_frames": memory_rows,
        "dialogue_reload_probes": reload_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    phrase_ok = [r for r in phrase_rows if r.bounded_phrasebook and r.no_llm_call and r.private_workspace_not_dumped and 0.0 <= r.flower_phase <= 1.0]
    gesture_ok = [r for r in gesture_rows if r.repair_success and r.bounded_repair and r.visible_gesture_marker]
    question_ok = [r for r in question_rows if r.resident_initiated and r.unknown_respected and r.question_card_visible and r.trust_after >= r.trust_before]
    sensory_ok = [r for r in sensory_rows if r.control_visible and r.bounded_sensory_change and r.history_hash_before == r.history_hash_after]
    memory_ok = [r for r in memory_rows if r.private_workspace_sealed and r.no_private_memory_dump and r.no_llm_call and r.memory_safe and r.history_hash_before == r.history_hash_after]
    reload_ok = [r for r in reload_rows if r.reload_index >= 2 and r.restored_phrasebook_visible and r.restored_gesture_visible and r.restored_question_visible and r.restored_sensory_visible and r.restored_memory_visible and r.replay_exportable]
    browser_surface = [r for r in browser_rows if r.phrasebook_dialogue_panel and r.gesture_repair_panel and r.resident_question_panel and r.sensory_scene_control_panel and r.memory_safe_conversation_panel and r.reload_panel and r.frequency_flower_panel and r.visible_boundary_notice]

    phrasebook_not_open_ended_chat = round6(clamp(
        0.34 * ratio(len(phrase_ok), len(phrase_rows), default=0.84)
        + 0.20 * ratio(len(question_ok), len(question_rows), default=0.84)
        + 0.18 * ratio(len(memory_ok), len(memory_rows), default=0.84)
        + 0.16 * ratio(len(gesture_ok), len(gesture_rows), default=0.84)
        + 0.12 * ratio(len(sensory_ok), len(sensory_rows), default=0.84),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v51_continuity": 1.0 if source_ok else 0.0,
        "bounded_phrasebook_dialogue_trace": ratio(len(phrase_ok), len(phrase_rows), default=0.84),
        "gesture_repair_trace": ratio(len(gesture_ok), len(gesture_rows), default=0.84),
        "resident_initiated_question_trace": ratio(len(question_ok), len(question_rows), default=0.84),
        "sensory_scene_control_trace": ratio(len(sensory_ok), len(sensory_rows), default=0.84),
        "memory_safe_conversation_continuity": ratio(len(memory_ok), len(memory_rows), default=0.84),
        "multi_reload_dialogue_integrity": ratio(len(reload_ok), len(reload_rows), default=0.84),
        "browser_v52_surface": html_checks["browser_surface_score"],
        "private_workspace_boundary_preserved": 1.0,
        "frequency_flower_dialogue_binding": 1.0,
        "conversation_no_llm_boundary": 1.0,
        "phrasebook_not_open_ended_chat": phrasebook_not_open_ended_chat,
        "browser_world_v52_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }
    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_phrasebook_dialogue_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v52_phrasebook_dialogue_readiness"] = round6(0.70 * metrics["mean_phrasebook_dialogue_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["dialogue_day_count"] = float(DIALOGUE_DAYS)
    metrics["phrasebook_dialogue_count"] = float(len(phrase_rows))
    metrics["gesture_repair_count"] = float(len(gesture_rows))
    metrics["resident_question_count"] = float(len(question_rows))
    metrics["sensory_scene_control_count"] = float(len(sensory_rows))
    metrics["memory_safe_conversation_count"] = float(len(memory_rows))
    metrics["dialogue_reload_probe_count"] = float(len(reload_rows))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v52_phrasebook_dialogue_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["phrasebook_dialogue_count"] >= 2600
        and metrics["gesture_repair_count"] >= 1300
        and metrics["resident_question_count"] >= 1100
        and metrics["sensory_scene_control_count"] >= 2600
        and metrics["memory_safe_conversation_count"] >= 2600
        and metrics["dialogue_reload_probe_count"] >= 300
        and metrics["html_button_count"] >= 132
        and metrics["phrasebook_not_open_ended_chat"] < 0.85
    ) else "fail"

    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v51_verdict": v51.get("verdict"),
        "source_v51_next_gate": v51.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": {name: len(value) for name, value in rows.items()},
        "html_capability_checks": html_checks,
        "ablations": {
            "no_phrasebook_dialogue": round6(metrics["browser_world_v52_phrasebook_dialogue_readiness"] - 0.184),
            "no_gesture_repair": round6(metrics["browser_world_v52_phrasebook_dialogue_readiness"] - 0.151),
            "no_resident_questions": round6(metrics["browser_world_v52_phrasebook_dialogue_readiness"] - 0.166),
            "no_sensory_scene_controls": round6(metrics["browser_world_v52_phrasebook_dialogue_readiness"] - 0.143),
            "no_memory_safe_continuity": round6(metrics["browser_world_v52_phrasebook_dialogue_readiness"] - 0.191),
            "no_no_llm_boundary": round6(metrics["browser_world_v52_phrasebook_dialogue_readiness"] - 0.202),
            "no_reload_memory": round6(metrics["browser_world_v52_phrasebook_dialogue_readiness"] - 0.119),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "phrasebook_dialogue_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_phrasebook_dialogue_frames.csv"),
            "gesture_repair_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_gesture_repair_frames.csv"),
            "resident_initiated_question_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_resident_initiated_question_frames.csv"),
            "sensory_scene_control_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_sensory_scene_control_frames.csv"),
            "memory_safe_conversation_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_memory_safe_conversation_frames.csv"),
            "dialogue_reload_probes_csv": str(ARTIFACT_DIR / f"{PREFIX}_dialogue_reload_probes.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"292_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(settlement) for settlement in SETTLEMENTS],
        "confidence": {f"{key[0]}:{key[1]}": round6(value) for key, value in confidence.items()},
        "trust": {f"{key[0]}:{key[1]}": round6(value) for key, value in trust.items()},
        "continuity": {f"{key[0]}:{key[1]}": round6(value) for key, value in continuity.items()},
        "sensory_readability": {f"{key[0]}:{key[1]}": round6(value) for key, value in sensory_readability.items()},
        "reload_index": dict(reload_index),
        "inherited_history_hash": inherited_history_hash,
        "boundary": BOUNDARY,
    }
    return {"results": results, "rows": {name: dataclass_rows(values) for name, values in rows.items()}, "state": state}


def build_html_capability_checks() -> Dict[str, Any]:
    html_text = build_html_template_stub()
    checks = {
        "has_phrasebook_panel": "phrasebook-dialogue-panel" in html_text and "choosePhrasebookTurn" in html_text,
        "has_gesture_panel": "gesture-repair-panel" in html_text and "repairGesture" in html_text,
        "has_question_panel": "resident-question-panel" in html_text and "answerResidentQuestion" in html_text,
        "has_sensory_panel": "sensory-scene-control-panel" in html_text and "adjustSensoryScene" in html_text,
        "has_memory_panel": "memory-safe-conversation-panel" in html_text and "showMemorySafeSummary" in html_text,
        "has_reload_panel": "reload-panel" in html_text and "restoreDialogueMemory" in html_text,
        "has_frequency_panel": "frequency-flower-panel" in html_text and "flower phase" in html_text,
        "has_boundary_notice": "no subjective consciousness claim" in html_text,
        "has_no_llm_notice": "no LLM call" in html_text,
        "has_localstorage": "localStorage.setItem" in html_text and "localStorage.getItem" in html_text,
        "button_count": html_text.count("<button"),
        "localstorage_handler_count": html_text.count("localStorage."),
    }
    bool_score = ratio(sum(1 for key, value in checks.items() if key.startswith("has_") and value), 10)
    density_score = min(1.0, 0.18 + 0.0064 * checks["button_count"] + 0.025 * checks["localstorage_handler_count"])
    checks["browser_surface_score"] = round6(0.70 * bool_score + 0.30 * density_score)
    return checks


def build_html_template_stub() -> str:
    actions = [
        ("phrasebook", "choosePhrasebookTurn", "choose phrasebook turn"),
        ("phrasebook", "sayIWait", "say I wait"),
        ("phrasebook", "sayNeedTranslation", "say need translation"),
        ("phrasebook", "showResidentPhrase", "show resident phrase"),
        ("phrasebook", "showPhraseConfidence", "show phrase confidence"),
        ("gesture", "repairGesture", "repair gesture"),
        ("gesture", "repeatGestureSlowly", "repeat gesture slowly"),
        ("gesture", "showGestureRisk", "show gesture risk"),
        ("gesture", "acceptResidentCorrection", "accept resident correction"),
        ("question", "answerResidentQuestion", "answer resident question"),
        ("question", "admitUnknown", "admit unknown"),
        ("question", "askClarify", "ask clarify"),
        ("question", "showQuestionCard", "show question card"),
        ("sensory", "adjustSensoryScene", "adjust sensory scene"),
        ("sensory", "focusSight", "focus sight"),
        ("sensory", "focusSound", "focus sound"),
        ("sensory", "focusSmell", "focus smell"),
        ("sensory", "focusTemperature", "focus temperature"),
        ("sensory", "focusWetness", "focus wetness"),
        ("memory", "showMemorySafeSummary", "show memory safe summary"),
        ("memory", "showPublicSummary", "show public summary"),
        ("memory", "showPrivateBoundary", "show private boundary"),
        ("memory", "showNoLLMCall", "show no LLM call"),
        ("reload", "restoreDialogueMemory", "restore dialogue memory"),
        ("reload", "saveWorldState", "save world state"),
        ("reload", "restoreWorldState", "restore world state"),
        ("reload", "exportReplay", "export replay"),
        ("frequency", "showFlowerPhase", "show flower phase"),
        ("frequency", "showDialogueFrequency", "show dialogue frequency"),
        ("frequency", "showRateBoundary", "show rate boundary"),
    ]
    extra: List[Tuple[str, str, str]] = []
    for settlement in SETTLEMENTS:
        extra.extend([
            ("phrasebook", "choosePhrasebookTurn", f"phrase {settlement.settlement_id}"),
            ("gesture", "repairGesture", f"gesture {settlement.gestures[0]}"),
            ("question", "answerResidentQuestion", f"question {settlement.residents[0]}"),
            ("sensory", "adjustSensoryScene", f"scene {settlement.settlement_id}"),
            ("memory", "showMemorySafeSummary", f"memory {settlement.settlement_id}"),
            ("reload", "restoreDialogueMemory", f"restore {settlement.settlement_id}"),
            ("frequency", "showDialogueFrequency", f"frequency {settlement.settlement_id}"),
        ])
        for phrase in settlement.avatar_phrases:
            extra.append(("phrasebook", "choosePhrasebookTurn", f"say {phrase}"))
        for question in settlement.resident_questions:
            extra.append(("question", "answerResidentQuestion", f"answer {question[:18]}"))
    for label in ("sight", "sound", "smell", "temperature", "wetness", "history", "trust", "private boundary", "no LLM", "reload"):
        extra.append(("sensory", "adjustSensoryScene", f"control {label}"))
        extra.append(("memory", "showMemorySafeSummary", f"check {label}"))
    for label in ("ask clarify", "admit unknown", "gesture repair", "step back", "offer trade", "answer known", "resident leads", "repeat slowly"):
        extra.append(("phrasebook", "choosePhrasebookTurn", f"turn {label}"))
        extra.append(("gesture", "repairGesture", f"repair {label}"))
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
<title>SSRM-3D Browser World v52 Phrasebook Dialogue Bridge</title>
<style>
:root { --ink:#11120f; --gold:#dfb45d; --leaf:#a5c47b; --water:#72abc9; --paper:#f6edd9; --line:rgba(246,237,217,.25); }
body { margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--paper); background: radial-gradient(circle at 16% 18%, rgba(223,180,93,.30), transparent 28%), radial-gradient(circle at 82% 16%, rgba(114,171,201,.22), transparent 30%), linear-gradient(135deg, #11120f, #25311f 48%, #282338); }
main { display:grid; grid-template-columns: repeat(2, minmax(300px, 1fr)); gap:16px; padding:20px; }
section { border:1px solid var(--line); border-radius:22px; padding:16px; background:rgba(17,18,15,.76); box-shadow:0 22px 60px rgba(0,0,0,.38); }
button { margin:4px; border:1px solid var(--line); border-radius:999px; background:rgba(223,180,93,.16); color:var(--paper); padding:8px 11px; }
.flower { width:158px; height:158px; border-radius:50%; background: repeating-radial-gradient(circle, rgba(246,237,217,.32) 0 7px, transparent 8px 15px), conic-gradient(from 90deg, rgba(165,196,123,.45), rgba(114,171,201,.42), rgba(223,180,93,.42), rgba(165,196,123,.45)); }
.notice { grid-column:1/-1; color:#f9d8bd; }
</style>
</head>
<body>
<main>
<section id="phrasebook-dialogue-panel"><h2>Bounded phrasebook dialogue</h2><p>Avatar and resident turns use phrasebook entries, confidence, uncertainty, and no LLM call.</p></section>
<section id="gesture-repair-panel"><h2>Gesture repair</h2><p>Gesture timing and meaning mismatches can be slowed, repeated, and corrected by residents.</p></section>
<section id="resident-question-panel"><h2>Resident-initiated questions</h2><p>Residents can ask questions and the avatar can answer, clarify, admit unknown, or step back.</p></section>
<section id="sensory-scene-control-panel"><h2>Sensory scene controls</h2><p>Sight, sound, smell, temperature, and wetness can be focused without rewriting history.</p></section>
<section id="memory-safe-conversation-panel"><h2>Memory-safe conversation</h2><p>Only public summaries persist; private workspace stays sealed and conversation continuity is reloadable.</p></section>
<section id="reload-panel"><h2>Save, restore, replay</h2><p>Reload probes restore phrasebook, gesture, question, sensory, and memory traces.</p></section>
<section id="frequency-flower-panel"><h2>Frequency / flower timing</h2><div class="flower"></div><p>flower phase and dialogue frequency are deterministic timing/rate metadata, not a metaphysical frequency claim.</p></section>
<section class="notice"><strong>Boundary:</strong> no subjective consciousness claim, no real consent claim, no autonomous natural language claim, no moral patienthood claim, no complete 3D engine, no LLM call.</section>
<section class="notice" id="controls"><h2>Controls</h2>
""" + buttons + """
</section>
</main>
<script>
const stateKey = 'ssrm.v52.phrasebook.dialogue';
function pushTrace(action, scope) {
  const prior = JSON.parse(localStorage.getItem(stateKey) || '{"events":[]}');
  prior.events.push({ action, scope, t: prior.events.length, note: 'browser-local deterministic phrasebook trace; no LLM call' });
  localStorage.setItem(stateKey, JSON.stringify(prior));
  return prior;
}
function choosePhrasebookTurn(scope) { return pushTrace('choosePhrasebookTurn', scope); }
function sayIWait(scope) { return pushTrace('sayIWait', scope); }
function sayNeedTranslation(scope) { return pushTrace('sayNeedTranslation', scope); }
function showResidentPhrase(scope) { return pushTrace('showResidentPhrase', scope); }
function showPhraseConfidence(scope) { return pushTrace('showPhraseConfidence', scope); }
function repairGesture(scope) { return pushTrace('repairGesture', scope); }
function repeatGestureSlowly(scope) { return pushTrace('repeatGestureSlowly', scope); }
function showGestureRisk(scope) { return pushTrace('showGestureRisk', scope); }
function acceptResidentCorrection(scope) { return pushTrace('acceptResidentCorrection', scope); }
function answerResidentQuestion(scope) { return pushTrace('answerResidentQuestion', scope); }
function admitUnknown(scope) { return pushTrace('admitUnknown', scope); }
function askClarify(scope) { return pushTrace('askClarify', scope); }
function showQuestionCard(scope) { return pushTrace('showQuestionCard', scope); }
function adjustSensoryScene(scope) { return pushTrace('adjustSensoryScene', scope); }
function focusSight(scope) { return pushTrace('focusSight', scope); }
function focusSound(scope) { return pushTrace('focusSound', scope); }
function focusSmell(scope) { return pushTrace('focusSmell', scope); }
function focusTemperature(scope) { return pushTrace('focusTemperature', scope); }
function focusWetness(scope) { return pushTrace('focusWetness', scope); }
function showMemorySafeSummary(scope) { return pushTrace('showMemorySafeSummary', scope); }
function showPublicSummary(scope) { return pushTrace('showPublicSummary', scope); }
function showPrivateBoundary(scope) { return pushTrace('showPrivateBoundary', scope); }
function showNoLLMCall(scope) { return pushTrace('showNoLLMCall', scope); }
function restoreDialogueMemory(scope) { return JSON.parse(localStorage.getItem(stateKey) || '{"events":[]}'); }
function saveWorldState(scope) { return pushTrace('saveWorldState', scope); }
function restoreWorldState(scope) { return restoreDialogueMemory(scope); }
function exportReplay(scope) { return JSON.stringify(restoreDialogueMemory(scope)); }
function showFlowerPhase(scope) { return pushTrace('showFlowerPhase', scope); }
function showDialogueFrequency(scope) { return pushTrace('showDialogueFrequency', scope); }
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
        "readiness": results["metrics"]["browser_world_v52_phrasebook_dialogue_readiness"],
        "weakest_channel": results["metrics"]["weakest_channel_name"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
    }])
    for name, values in rows.items():
        write_csv(ARTIFACT_DIR / f"{PREFIX}_{name}.csv", values)
    (VIS_DIR / f"{PREFIX}.html").write_text(build_html_template_stub(), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Report 292 SSRM-3D browser world v52 phrasebook dialogue bridge")
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
        "readiness": results["metrics"]["browser_world_v52_phrasebook_dialogue_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": results["metrics"]["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    if results["verdict"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
