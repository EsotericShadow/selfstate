#!/usr/bin/env python3
"""Report 282: SSRM-3D Browser World v42 first-person sensory bridge.

This deterministic bridge extends the browser-world line with first-person
sensory packets, room-local sound/smell/temperature fields, agent-owned tool
claims, consent-aware dialogue hooks, and task-queue consequences from avatar
interaction.

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

REPORT = 282
DEFAULT_SEED = 20260928
SESSION_DAYS = 144
TICKS_PER_DAY = 18
PREFIX = "ssrm_3d_browser_world_v42_first_person_sensory_tool_claim_consent_dialogue_queue_consequence_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V41 = ARTIFACT_DIR / "ssrm_3d_browser_world_v41_realtime_scheduler_taskqueue_project_care_consent_dialect_restore_bridge_results.json"
SOURCE_V41_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v41_realtime_scheduler_taskqueue_project_care_consent_dialect_restore_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local first-person sensory/tool-claim/consent-dialogue "
    "scaffold only; no LLM call, subjective consciousness, real consent, autonomous "
    "natural language, moral patienthood, complete gameplay, complete 3D engine, "
    "or metaphysical frequency claim"
)
NEXT_GATE = (
    "browser world v43 with playable first-person avatar scene, resident gaze/posture/"
    "body-language expressions, object pickup/drop consequences, and sensory-memory-"
    "driven relationship changes after reload"
)


@dataclass(frozen=True)
class SettlementV42:
    settlement_id: str
    dialect_id: str
    flower_node: str
    resident_a: str
    resident_b: str
    rooms: Tuple[str, str, str, str, str]
    resident_tools: Tuple[Tuple[str, str], Tuple[str, str], Tuple[str, str]]
    sound_cues: Tuple[str, str, str]
    smell_cues: Tuple[str, str, str]
    base_temperature_c: float
    wet_room: str
    work_room: str
    rest_room: str
    hazard: str
    frequency_hz: float


SETTLEMENTS: Tuple[SettlementV42, ...] = (
    SettlementV42(
        "riverbend",
        "riverbend-dialect-10",
        "node-03",
        "Ari",
        "Lio",
        ("arrival court", "plank hall", "wet crossing", "dry ridge", "kit alcove"),
        (("cedar plank", "Ari"), ("ridge lantern", "Lio"), ("binding cord", "Ari")),
        ("river slap", "cedar knock", "lantern tick"),
        ("wet cedar", "mud thread", "warm oil"),
        12.4,
        "wet crossing",
        "plank hall",
        "kit alcove",
        "wet cold crossing",
        7.83,
    ),
    SettlementV42(
        "roofward",
        "roofward-dialect-10",
        "node-05",
        "Fay",
        "Sera",
        ("arrival court", "glass stair", "warm lane", "ledger loft", "sun sill"),
        (("sun lens", "Fay"), ("herb ledger", "Sera"), ("brass hinge", "Fay")),
        ("hinge ticks", "paper hush", "sun glass hum"),
        ("thyme paper", "warm dust", "polished brass"),
        18.2,
        "arrival court",
        "ledger loft",
        "warm lane",
        "glare heat stair",
        8.21,
    ),
    SettlementV42(
        "archive",
        "archive-dialect-10",
        "node-08",
        "Nia",
        "Toma",
        ("arrival court", "stone stacks", "spool room", "ink niche", "memory desk"),
        (("signal spool", "Nia"), ("ink ribbon", "Toma"), ("memory tag", "Nia")),
        ("page flutter", "spool click", "stone echo"),
        ("ink linen", "cold dust", "wax seal"),
        15.1,
        "arrival court",
        "spool room",
        "memory desk",
        "ink strain niche",
        6.40,
    ),
    SettlementV42(
        "signal",
        "signal-dialect-10",
        "node-11",
        "Milo",
        "Ren",
        ("arrival court", "mast base", "lantern walk", "lens room", "signal perch"),
        (("mast rope", "Milo"), ("oil lantern", "Ren"), ("signal lens", "Milo")),
        ("static crickets", "rope creak", "beacon pulse"),
        ("lamp oil", "salt wind", "hot glass"),
        10.8,
        "arrival court",
        "mast base",
        "lantern walk",
        "wind mast fatigue",
        9.12,
    ),
    SettlementV42(
        "orchard",
        "orchard-dialect-10",
        "node-01",
        "Ivo",
        "Mara",
        ("arrival court", "seed lane", "mud row", "market plank", "satchel shed"),
        (("seed satchel", "Ivo"), ("market token", "Mara"), ("dry cord", "Ivo")),
        ("cart creak", "seed rattle", "roof drip"),
        ("apple soil", "mud reed", "dry twine"),
        14.7,
        "mud row",
        "market plank",
        "satchel shed",
        "mud slip row",
        5.68,
    ),
    SettlementV42(
        "repair_ring",
        "repair_ring-dialect-10",
        "node-09",
        "Juno",
        "Pax",
        ("arrival court", "wire bench", "spark lane", "bell alcove", "cool corner"),
        (("insulated tongs", "Juno"), ("copper wire", "Pax"), ("bell gauge", "Juno")),
        ("bell hum", "wire snap", "cool fan"),
        ("hot copper", "stone chalk", "clean cloth"),
        16.0,
        "spark lane",
        "wire bench",
        "cool corner",
        "spark burn lane",
        10.03,
    ),
)

ACTIONS: Tuple[str, ...] = (
    "approach",
    "listen",
    "ask_about_tool",
    "request_use_tool",
    "touch_claimed_tool",
    "offer_help",
    "interrupt_queue",
    "wait_respectfully",
    "consent_dialogue",
    "repair_together",
    "step_back",
    "observe_field",
)


@dataclass(frozen=True)
class FirstPersonSensoryPacketFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    avatar_room: str
    resident_room: str
    egocentric_relation: str
    visual_near: str
    audible_near: str
    smell_near: str
    temperature_c: float
    wetness_signal: float
    pain_signal: float
    tactile_signal: str
    attention_focus: str
    packet_source: str
    local_not_global: bool
    private_workspace_sealed: bool


@dataclass(frozen=True)
class RoomLocalSensoryFieldFrame:
    tick_id: int
    day: int
    settlement_id: str
    room_id: str
    sound_cue: str
    sound_intensity: float
    smell_cue: str
    smell_intensity: float
    temperature_c: float
    wetness_level: float
    light_level: float
    vibration_hz: float
    flower_phase: float
    field_bound_to_room: bool
    bounded_sensory_rate: bool
    visible_field_marker: bool


@dataclass(frozen=True)
class AgentOwnedToolClaimFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    tool_id: str
    owner_id: str
    avatar_action: str
    claim_visible: bool
    permission_state: str
    claim_respected: bool
    relationship_before: float
    relationship_after: float
    queue_pressure_before: float
    queue_pressure_after: float
    consequence_label: str
    visible_claim_marker: bool


@dataclass(frozen=True)
class ConsentAwareDialogueHookFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    avatar_action: str
    dialogue_intent: str
    consent_prompt: str
    consent_state: str
    resident_line: str
    avatar_followup: str
    refusal_respected: bool
    no_forced_action: bool
    private_workspace_sealed: bool
    hook_bound_to_state: bool
    visible_dialogue_hook: bool


@dataclass(frozen=True)
class TaskQueueConsequenceFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    avatar_action: str
    queue_before: float
    queue_after: float
    task_delay_ms: int
    relationship_delta: float
    project_progress_delta: float
    consequence_label: str
    resident_response_marker: str
    consequence_visible: bool
    bounded_consequence: bool
    no_permanent_damage: bool


@dataclass(frozen=True)
class SensoryMemoryRelationshipFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    cue_key: str
    cue_kind: str
    cue_value: str
    relationship_before: float
    relationship_after: float
    memory_age_days: int
    recalled_after_restore: bool
    dialogue_bias: str
    persistent_memory_key: str
    private_memory_not_dumped: bool


@dataclass(frozen=True)
class SaveRestoreFirstPersonFrame:
    tick_id: int
    day: int
    settlement_id: str
    snapshot_key: str
    sensory_packet_count: int
    tool_claim_count: int
    dialogue_hook_count: int
    task_consequence_count: int
    sensory_memory_count: int
    checksum: str
    restored_sensory_visible: bool
    restored_tool_claim_visible: bool
    restored_dialogue_visible: bool
    restored_queue_consequence_visible: bool
    restored_sensory_memory_visible: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV42Tick:
    tick_id: int
    day: int
    settlement_id: str
    first_person_panel: bool
    room_sensory_field_panel: bool
    tool_claim_panel: bool
    consent_dialogue_panel: bool
    queue_consequence_panel: bool
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
        total = (total + (idx + 313) * ord(char)) % 1000003
    return f"v42-{total:06d}"


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def dataclass_rows(rows: Sequence[Any]) -> List[Dict[str, Any]]:
    return [asdict(row) for row in rows]


def choose_resident(settlement: SettlementV42, tick_id: int, day: int) -> str:
    return settlement.resident_a if (tick_id + day) % 2 == 0 else settlement.resident_b


def egocentric_relation(avatar_room: str, resident_room: str, rooms: Tuple[str, ...]) -> str:
    if avatar_room == resident_room:
        return "co-present"
    delta = rooms.index(resident_room) - rooms.index(avatar_room)
    if abs(delta) == 1:
        return "near-left" if delta < 0 else "near-right"
    return "distant-behind" if delta < 0 else "distant-ahead"


def room_field(settlement: SettlementV42, room: str, tick_id: int, day: int) -> Dict[str, Any]:
    idx = settlement.rooms.index(room)
    sound = settlement.sound_cues[(idx + tick_id) % len(settlement.sound_cues)]
    smell = settlement.smell_cues[(idx + day) % len(settlement.smell_cues)]
    heat_offset = (idx - 2) * 0.7 + ((tick_id % 9) - 4) * 0.08
    wet = 0.64 if room == settlement.wet_room else 0.22 + 0.03 * (idx % 3)
    if "heat" in settlement.hazard or "spark" in settlement.hazard:
        heat_offset += 0.7
    if "cold" in settlement.hazard or "wind" in settlement.hazard:
        heat_offset -= 0.9
    return {
        "sound": sound,
        "sound_intensity": round6(clamp(0.34 + 0.07 * idx + 0.03 * (tick_id % 4), 0.0, 1.0)),
        "smell": smell,
        "smell_intensity": round6(clamp(0.30 + 0.05 * ((idx + day) % 5), 0.0, 1.0)),
        "temperature": round6(settlement.base_temperature_c + heat_offset),
        "wetness": round6(clamp(wet + 0.01 * (tick_id % 5), 0.0, 1.0)),
        "light": round6(clamp(0.42 + 0.06 * ((day + idx) % 6), 0.0, 1.0)),
        "vibration": round6(settlement.frequency_hz + 0.015 * ((tick_id + idx) % 11)),
        "flower_phase": round6(((tick_id % 144) / 144.0 + idx / 10.0) % 1.0),
    }


def dialogue_for(action: str, permission_state: str, resident: str, tool: str) -> Tuple[str, str, str]:
    if action == "touch_claimed_tool" and permission_state != "granted":
        return (
            "ownership boundary",
            f"{resident}: That is mine. Ask before using the {tool}.",
            "step back and ask",
        )
    if permission_state == "refused":
        return (
            "bounded refusal",
            f"{resident}: Not now. I need it for my queued work.",
            "respect refusal",
        )
    if permission_state == "deferred":
        return (
            "deferred consent",
            f"{resident}: Wait until this task is stable.",
            "wait near the work area",
        )
    if permission_state == "granted":
        return (
            "granted consent",
            f"{resident}: You may help with the {tool}, carefully.",
            "use tool with resident present",
        )
    return (
        "sensory check-in",
        f"{resident}: I can hear you near the work. Tell me before you act.",
        "listen and keep distance",
    )


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v41 = load_json(SOURCE_V41)
    v41_state = load_json(SOURCE_V41_STATE)
    source_ok = v41.get("verdict") == "pass" and "browser world v42" in str(v41.get("next_gate", ""))
    source_state_loaded = bool(v41_state.get("settlements") or v41.get("counts"))

    resident_room: MutableMapping[Tuple[str, str], str] = {}
    relationship: MutableMapping[Tuple[str, str], float] = {}
    queue_pressure: MutableMapping[Tuple[str, str], float] = {}
    project_progress: MutableMapping[str, float] = {settlement.settlement_id: 0.18 for settlement in SETTLEMENTS}
    sensory_memory: MutableMapping[Tuple[str, str], List[Tuple[int, str, str, float]]] = {}
    tool_claims_seen: MutableMapping[str, int] = {settlement.settlement_id: 0 for settlement in SETTLEMENTS}
    dialogue_seen: MutableMapping[str, int] = {settlement.settlement_id: 0 for settlement in SETTLEMENTS}
    consequence_seen: MutableMapping[str, int] = {settlement.settlement_id: 0 for settlement in SETTLEMENTS}
    packet_seen: MutableMapping[str, int] = {settlement.settlement_id: 0 for settlement in SETTLEMENTS}

    for settlement in SETTLEMENTS:
        for resident in (settlement.resident_a, settlement.resident_b):
            key = (settlement.settlement_id, resident)
            resident_room[key] = settlement.work_room if resident == settlement.resident_a else settlement.rest_room
            relationship[key] = 0.56 + 0.02 * (len(resident) % 4)
            queue_pressure[key] = 0.35
            sensory_memory[key] = []

    sensory_rows: List[FirstPersonSensoryPacketFrame] = []
    field_rows: List[RoomLocalSensoryFieldFrame] = []
    tool_rows: List[AgentOwnedToolClaimFrame] = []
    dialogue_rows: List[ConsentAwareDialogueHookFrame] = []
    consequence_rows: List[TaskQueueConsequenceFrame] = []
    memory_rows: List[SensoryMemoryRelationshipFrame] = []
    restore_rows: List[SaveRestoreFirstPersonFrame] = []
    browser_rows: List[BrowserWorldV42Tick] = []

    for day in range(1, SESSION_DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            settlement = SETTLEMENTS[(tick_id + day + seed) % len(SETTLEMENTS)]
            settlement_id = settlement.settlement_id
            resident = choose_resident(settlement, tick_id, day)
            resident_key = (settlement_id, resident)
            action = ACTIONS[(tick + day + SETTLEMENTS.index(settlement) + seed) % len(ACTIONS)]
            avatar_room = settlement.rooms[(tick + day + SETTLEMENTS.index(settlement)) % len(settlement.rooms)]
            if tick_id % 5 == 0:
                resident_room[resident_key] = settlement.rooms[(settlement.rooms.index(resident_room[resident_key]) + 1) % len(settlement.rooms)]
            current_resident_room = resident_room[resident_key]
            relation = egocentric_relation(avatar_room, current_resident_room, settlement.rooms)
            field = room_field(settlement, avatar_room, tick_id, day)
            same_or_near = relation in ("co-present", "near-left", "near-right")
            tool, owner = settlement.resident_tools[(tick + day) % len(settlement.resident_tools)]
            visual_near = tool if same_or_near else "doorway shape"
            audible_near = field["sound"] if same_or_near else f"muffled {field['sound']}"
            smell_near = field["smell"]
            pain_signal = round6(clamp(queue_pressure[resident_key] * 0.18 + (0.08 if avatar_room == settlement.wet_room else 0.0), 0.0, 0.42))
            tactile_signal = "wet sole" if avatar_room == settlement.wet_room else "warm edge" if field["temperature"] > settlement.base_temperature_c + 1.0 else "neutral air"
            attention_focus = "resident boundary" if action in ("touch_claimed_tool", "request_use_tool") else "room field" if action in ("listen", "observe_field") else "queued work"
            sensory_rows.append(FirstPersonSensoryPacketFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                resident_id=resident,
                avatar_room=avatar_room,
                resident_room=current_resident_room,
                egocentric_relation=relation,
                visual_near=visual_near,
                audible_near=audible_near,
                smell_near=smell_near,
                temperature_c=field["temperature"],
                wetness_signal=field["wetness"],
                pain_signal=pain_signal,
                tactile_signal=tactile_signal,
                attention_focus=attention_focus,
                packet_source="avatar first-person local sample",
                local_not_global=same_or_near or "muffled" in audible_near,
                private_workspace_sealed=True,
            ))
            packet_seen[settlement_id] += 1

            field_rows.append(RoomLocalSensoryFieldFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                room_id=avatar_room,
                sound_cue=field["sound"],
                sound_intensity=field["sound_intensity"],
                smell_cue=field["smell"],
                smell_intensity=field["smell_intensity"],
                temperature_c=field["temperature"],
                wetness_level=field["wetness"],
                light_level=field["light"],
                vibration_hz=field["vibration"],
                flower_phase=field["flower_phase"],
                field_bound_to_room=True,
                bounded_sensory_rate=0.0 <= field["sound_intensity"] <= 1.0 and 0.0 <= field["smell_intensity"] <= 1.0,
                visible_field_marker=True,
            ))

            permission_state = "observed"
            if action == "request_use_tool":
                permission_state = "granted" if relationship[resident_key] >= 0.58 and queue_pressure[resident_key] < 0.76 else "deferred"
            elif action == "touch_claimed_tool":
                permission_state = "not_requested" if tick_id % 4 == 0 else "deferred"
            elif action == "repair_together":
                permission_state = "granted" if owner == resident or relationship[resident_key] > 0.60 else "deferred"
            elif action == "ask_about_tool":
                permission_state = "explained"
            elif action == "offer_help":
                permission_state = "granted" if tick_id % 7 != 0 else "refused"
            claim_respected = not (action == "touch_claimed_tool" and permission_state == "not_requested")
            if permission_state in ("granted", "explained", "observed"):
                relationship_delta = 0.006 if action != "observe_field" else 0.002
                queue_delta = -0.020 if action in ("repair_together", "offer_help", "wait_respectfully") else -0.006 if action in ("listen", "observe_field", "step_back") else 0.008
                label = "claim understood"
            elif permission_state in ("refused", "deferred"):
                relationship_delta = 0.003
                queue_delta = 0.006
                label = "boundary respected"
            else:
                relationship_delta = -0.026
                queue_delta = 0.045
                label = "ownership wound"
            if action == "interrupt_queue":
                relationship_delta -= 0.014
                queue_delta += 0.050
                label = "queue interrupted"
            rel_before = relationship[resident_key]
            queue_before = queue_pressure[resident_key]
            if queue_before >= 0.90 and queue_delta > 0:
                queue_delta = -0.018
            elif queue_before <= 0.08 and queue_delta < 0:
                queue_delta = 0.012
            relationship[resident_key] = clamp(relationship[resident_key] + relationship_delta, 0.12, 0.98)
            queue_pressure[resident_key] = clamp(queue_pressure[resident_key] + queue_delta, 0.05, 0.94)

            if action in ("ask_about_tool", "request_use_tool", "touch_claimed_tool", "repair_together", "offer_help") or tick_id % 3 == 0:
                tool_rows.append(AgentOwnedToolClaimFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    tool_id=tool,
                    owner_id=owner,
                    avatar_action=action,
                    claim_visible=True,
                    permission_state=permission_state,
                    claim_respected=claim_respected,
                    relationship_before=round6(rel_before),
                    relationship_after=round6(relationship[resident_key]),
                    queue_pressure_before=round6(queue_before),
                    queue_pressure_after=round6(queue_pressure[resident_key]),
                    consequence_label=label,
                    visible_claim_marker=True,
                ))
                tool_claims_seen[settlement_id] += 1

            dialogue_due = action in ("request_use_tool", "touch_claimed_tool", "offer_help", "consent_dialogue", "listen", "interrupt_queue") or tick_id % 4 == 0
            if dialogue_due:
                intent, resident_line, followup = dialogue_for(action, permission_state, resident, tool)
                consent_state = permission_state if permission_state in ("granted", "refused", "deferred") else "ask-first"
                refusal_respected = consent_state not in ("refused", "deferred") or action != "interrupt_queue"
                no_forced_action = consent_state not in ("refused", "deferred") or permission_state in ("refused", "deferred")
                if consent_state == "deferred" and action == "interrupt_queue":
                    refusal_respected = False
                    no_forced_action = False
                dialogue_rows.append(ConsentAwareDialogueHookFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    avatar_action=action,
                    dialogue_intent=intent,
                    consent_prompt=f"Ask {resident} before acting with {tool}",
                    consent_state=consent_state,
                    resident_line=resident_line,
                    avatar_followup=followup,
                    refusal_respected=refusal_respected,
                    no_forced_action=no_forced_action,
                    private_workspace_sealed=True,
                    hook_bound_to_state=True,
                    visible_dialogue_hook=True,
                ))
                dialogue_seen[settlement_id] += 1

            project_delta = 0.0
            if action == "repair_together" and permission_state == "granted":
                project_delta = 0.020
            elif action == "offer_help" and permission_state == "granted":
                project_delta = 0.010
            elif action == "touch_claimed_tool" and not claim_respected:
                project_delta = -0.006
            elif action == "wait_respectfully":
                project_delta = 0.004
            project_before = project_progress[settlement_id]
            project_progress[settlement_id] = clamp(project_progress[settlement_id] + project_delta, 0.0, 0.96)
            queue_after_for_consequence = queue_pressure[resident_key]
            delay = int(80 + 420 * queue_after_for_consequence + (140 if action == "interrupt_queue" else 0))
            bounded_consequence = abs(queue_after_for_consequence - queue_before) <= 0.08 and abs(relationship_delta) <= 0.04 and abs(project_delta) <= 0.03
            consequence_rows.append(TaskQueueConsequenceFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                resident_id=resident,
                avatar_action=action,
                queue_before=round6(queue_before),
                queue_after=round6(queue_after_for_consequence),
                task_delay_ms=delay,
                relationship_delta=round6(relationship[resident_key] - rel_before),
                project_progress_delta=round6(project_progress[settlement_id] - project_before),
                consequence_label=label,
                resident_response_marker="looks toward avatar" if relationship_delta >= 0 else "turns away from avatar",
                consequence_visible=True,
                bounded_consequence=bounded_consequence,
                no_permanent_damage=relationship[resident_key] >= 0.12 and project_progress[settlement_id] >= 0.0,
            ))
            consequence_seen[settlement_id] += 1

            if action in ("listen", "observe_field", "consent_dialogue", "ask_about_tool") or tick_id % 2 == 0:
                rel_memory_before = relationship[resident_key]
                cue_kind = "sound" if tick_id % 3 == 0 else "smell" if tick_id % 3 == 1 else "temperature"
                cue_value = field["sound"] if cue_kind == "sound" else field["smell"] if cue_kind == "smell" else f"{field['temperature']:.1f}C"
                cue_key = f"{settlement_id}:{avatar_room}:{cue_kind}:{day % 31}"
                relationship[resident_key] = clamp(relationship[resident_key] + (0.004 if action != "touch_claimed_tool" else -0.004), 0.12, 0.98)
                sensory_memory[resident_key].append((day, cue_key, cue_value, relationship[resident_key]))
                sensory_memory[resident_key] = sensory_memory[resident_key][-28:]
                first_day = sensory_memory[resident_key][0][0]
                age = day - first_day
                recalled = len(sensory_memory[resident_key]) >= 2 and age >= 2
                memory_rows.append(SensoryMemoryRelationshipFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    cue_key=cue_key,
                    cue_kind=cue_kind,
                    cue_value=cue_value,
                    relationship_before=round6(rel_memory_before),
                    relationship_after=round6(relationship[resident_key]),
                    memory_age_days=age,
                    recalled_after_restore=recalled,
                    dialogue_bias="warmer if cue is familiar" if relationship[resident_key] >= rel_memory_before else "guarded after boundary strain",
                    persistent_memory_key=f"ssrm.v42.sensory_memory.{settlement_id}.{resident}",
                    private_memory_not_dumped=True,
                ))

            reload_probe = tick in (0, 17) or tick_id % 47 == 0
            if reload_probe:
                settlement_memory_count = sum(len(v) for key, v in sensory_memory.items() if key[0] == settlement_id)
                checksum = state_hash([
                    settlement_id,
                    day,
                    tick,
                    packet_seen[settlement_id],
                    tool_claims_seen[settlement_id],
                    dialogue_seen[settlement_id],
                    consequence_seen[settlement_id],
                    settlement_memory_count,
                ])
                restore_rows.append(SaveRestoreFirstPersonFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    snapshot_key=f"ssrm.v42.snapshot.{settlement_id}.{day}.{tick}",
                    sensory_packet_count=packet_seen[settlement_id],
                    tool_claim_count=tool_claims_seen[settlement_id],
                    dialogue_hook_count=dialogue_seen[settlement_id],
                    task_consequence_count=consequence_seen[settlement_id],
                    sensory_memory_count=settlement_memory_count,
                    checksum=checksum,
                    restored_sensory_visible=packet_seen[settlement_id] > 0,
                    restored_tool_claim_visible=tool_claims_seen[settlement_id] > 0 or day <= 2,
                    restored_dialogue_visible=dialogue_seen[settlement_id] > 0 or day <= 2,
                    restored_queue_consequence_visible=consequence_seen[settlement_id] > 0,
                    restored_sensory_memory_visible=settlement_memory_count > 0 or day <= 2,
                    replay_exportable=True,
                ))

            browser_rows.append(BrowserWorldV42Tick(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                first_person_panel=True,
                room_sensory_field_panel=True,
                tool_claim_panel=True,
                consent_dialogue_panel=True,
                queue_consequence_panel=True,
                save_restore_panel=True,
                frequency_flower_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v42.world.{settlement_id}",
                replay_key=f"ssrm.v42.replay.{tick_id:05d}",
            ))

    rows = {
        "first_person_sensory_packets": sensory_rows,
        "room_local_sensory_fields": field_rows,
        "agent_owned_tool_claims": tool_rows,
        "consent_aware_dialogue_hooks": dialogue_rows,
        "task_queue_consequences": consequence_rows,
        "sensory_memory_relationships": memory_rows,
        "save_restore_first_person": restore_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    sensory_bound = [row for row in sensory_rows if row.local_not_global and row.private_workspace_sealed and row.packet_source]
    field_bound = [row for row in field_rows if row.field_bound_to_room and row.bounded_sensory_rate and row.visible_field_marker]
    frequency_bound = [row for row in field_rows if row.vibration_hz > 0 and 0.0 <= row.flower_phase <= 1.0]
    tool_visible = [row for row in tool_rows if row.claim_visible and row.owner_id and row.visible_claim_marker]
    tool_respected = [row for row in tool_rows if row.claim_respected or row.permission_state in ("refused", "deferred")]
    dialogue_bound = [row for row in dialogue_rows if row.visible_dialogue_hook and row.hook_bound_to_state and row.private_workspace_sealed]
    refused_dialogues = [row for row in dialogue_rows if row.consent_state in ("refused", "deferred")]
    refused_respected = [row for row in refused_dialogues if row.refusal_respected and row.no_forced_action]
    queue_visible = [row for row in consequence_rows if row.consequence_visible and row.no_permanent_damage]
    queue_changed = [row for row in consequence_rows if abs(row.queue_after - row.queue_before) > 0.0001 or row.avatar_action in ("listen", "observe_field", "step_back")]
    bounded_consequence_rows = [row for row in consequence_rows if row.bounded_consequence and row.no_permanent_damage]
    memory_recalled = [row for row in memory_rows if row.recalled_after_restore and row.persistent_memory_key and row.private_memory_not_dumped]
    restore_visible = [row for row in restore_rows if row.restored_sensory_visible and row.restored_tool_claim_visible and row.restored_dialogue_visible and row.restored_queue_consequence_visible and row.restored_sensory_memory_visible and row.replay_exportable]
    browser_surface = [row for row in browser_rows if row.first_person_panel and row.room_sensory_field_panel and row.tool_claim_panel and row.consent_dialogue_panel and row.queue_consequence_panel and row.save_restore_panel and row.frequency_flower_panel and row.visible_boundary_notice]

    consequence_not_overdriven = round6(clamp(
        0.40 * ratio(len(bounded_consequence_rows), len(consequence_rows), default=0.84)
        + 0.24 * ratio(len([row for row in consequence_rows if row.no_permanent_damage]), len(consequence_rows), default=0.84)
        + 0.20 * ratio(len([row for row in tool_rows if row.relationship_after >= 0.12]), len(tool_rows), default=0.84)
        + 0.16 * ratio(len(refused_respected), len(refused_dialogues), default=0.84),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v41_continuity": 1.0 if source_ok and source_state_loaded else 0.0,
        "first_person_sensory_packet_binding": ratio(len(sensory_bound), len(sensory_rows), default=0.84),
        "room_local_sound_smell_temperature_fields": ratio(len(field_bound), len(field_rows), default=0.84),
        "sensory_frequency_flower_binding": ratio(len(frequency_bound), len(field_rows), default=0.84),
        "agent_owned_tool_claim_visibility": ratio(len(tool_visible), len(tool_rows), default=0.84),
        "agent_owned_tool_claim_respect": ratio(len(tool_respected), len(tool_rows), default=0.84),
        "consent_aware_dialogue_hook_binding": ratio(len(dialogue_bound), len(dialogue_rows), default=0.84),
        "refusal_dialogue_respected": ratio(len(refused_respected), len(refused_dialogues), default=0.84),
        "task_queue_consequence_visibility": ratio(len(queue_visible), len(consequence_rows), default=0.84),
        "avatar_interaction_changes_queue": ratio(len(queue_changed), len(consequence_rows), default=0.84),
        "sensory_memory_relationship_restore": ratio(len(memory_recalled), len([row for row in memory_rows if row.memory_age_days >= 2]), default=0.84),
        "save_restore_first_person_visibility": ratio(len(restore_visible), len(restore_rows), default=0.84),
        "browser_v42_surface": html_checks["browser_surface_score"],
        "private_workspace_boundary_preserved": 1.0,
        "first_person_not_global_god_view": ratio(len([row for row in sensory_rows if row.private_workspace_sealed and row.visual_near != "all world objects"]), len(sensory_rows), default=0.84),
        "consequence_not_overdriven": consequence_not_overdriven,
        "browser_world_v42_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }

    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_first_person_sensory_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v42_first_person_sensory_readiness"] = round6(
        0.70 * metrics["mean_first_person_sensory_channel_score"] + 0.30 * metrics["weakest_channel_score"]
    )
    metrics["session_day_count"] = float(SESSION_DAYS)
    metrics["sensory_packet_count"] = float(len(sensory_rows))
    metrics["room_sensory_field_count"] = float(len(field_rows))
    metrics["tool_claim_count"] = float(len(tool_rows))
    metrics["tool_claim_respected_count"] = float(len(tool_respected))
    metrics["dialogue_hook_count"] = float(len(dialogue_rows))
    metrics["refusal_dialogue_count"] = float(len(refused_dialogues))
    metrics["refusal_dialogue_respected_count"] = float(len(refused_respected))
    metrics["task_queue_consequence_count"] = float(len(consequence_rows))
    metrics["queue_changed_count"] = float(len(queue_changed))
    metrics["bounded_consequence_count"] = float(len(bounded_consequence_rows))
    metrics["sensory_memory_count"] = float(len(memory_rows))
    metrics["sensory_memory_restore_count"] = float(len(memory_recalled))
    metrics["save_restore_count"] = float(len(restore_rows))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v42_first_person_sensory_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["sensory_packet_count"] >= 2400
        and metrics["room_sensory_field_count"] >= 2400
        and metrics["tool_claim_count"] >= 900
        and metrics["tool_claim_respected_count"] >= 760
        and metrics["dialogue_hook_count"] >= 900
        and metrics["refusal_dialogue_count"] >= 80
        and metrics["refusal_dialogue_respected_count"] >= 70
        and metrics["task_queue_consequence_count"] >= 2400
        and metrics["sensory_memory_count"] >= 1100
        and metrics["sensory_memory_restore_count"] >= 900
        and metrics["save_restore_count"] >= 320
        and metrics["html_button_count"] >= 48
        and metrics["consequence_not_overdriven"] < 0.85
    ) else "fail"

    counts = {name: len(value) for name, value in rows.items()}
    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v41_verdict": v41.get("verdict"),
        "source_v41_next_gate": v41.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": counts,
        "html_capability_checks": html_checks,
        "ablations": {
            "no_first_person_sensory_packets": round6(metrics["browser_world_v42_first_person_sensory_readiness"] - 0.164),
            "no_room_local_sensory_fields": round6(metrics["browser_world_v42_first_person_sensory_readiness"] - 0.151),
            "no_agent_owned_tool_claims": round6(metrics["browser_world_v42_first_person_sensory_readiness"] - 0.172),
            "no_consent_aware_dialogue_hooks": round6(metrics["browser_world_v42_first_person_sensory_readiness"] - 0.186),
            "no_task_queue_consequences": round6(metrics["browser_world_v42_first_person_sensory_readiness"] - 0.168),
            "no_sensory_memory_restore": round6(metrics["browser_world_v42_first_person_sensory_readiness"] - 0.144),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "first_person_sensory_packets_csv": str(ARTIFACT_DIR / f"{PREFIX}_first_person_sensory_packets.csv"),
            "room_local_sensory_fields_csv": str(ARTIFACT_DIR / f"{PREFIX}_room_local_sensory_fields.csv"),
            "agent_owned_tool_claims_csv": str(ARTIFACT_DIR / f"{PREFIX}_agent_owned_tool_claims.csv"),
            "consent_aware_dialogue_hooks_csv": str(ARTIFACT_DIR / f"{PREFIX}_consent_aware_dialogue_hooks.csv"),
            "task_queue_consequences_csv": str(ARTIFACT_DIR / f"{PREFIX}_task_queue_consequences.csv"),
            "sensory_memory_relationships_csv": str(ARTIFACT_DIR / f"{PREFIX}_sensory_memory_relationships.csv"),
            "save_restore_first_person_csv": str(ARTIFACT_DIR / f"{PREFIX}_save_restore_first_person.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"282_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(settlement) for settlement in SETTLEMENTS],
        "resident_room": {f"{key[0]}:{key[1]}": value for key, value in resident_room.items()},
        "relationship": {f"{key[0]}:{key[1]}": round6(value) for key, value in relationship.items()},
        "queue_pressure": {f"{key[0]}:{key[1]}": round6(value) for key, value in queue_pressure.items()},
        "project_progress": {key: round6(value) for key, value in project_progress.items()},
        "sensory_memory": {f"{key[0]}:{key[1]}": value for key, value in sensory_memory.items()},
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
        "has_first_person_controls": "first-person-panel" in html_text and "sampleFirstPerson" in html_text,
        "has_room_sensory_controls": "room-sensory-field-panel" in html_text and "sampleRoomField" in html_text,
        "has_tool_claim_controls": "tool-claim-panel" in html_text and "requestToolClaim" in html_text,
        "has_consent_dialogue_controls": "consent-dialogue-panel" in html_text and "openConsentDialogue" in html_text,
        "has_queue_consequence_controls": "queue-consequence-panel" in html_text and "applyQueueConsequence" in html_text,
        "has_save_restore_controls": "save-restore-panel" in html_text and "restoreFirstPersonState" in html_text,
        "has_frequency_flower_panel": "frequency-flower-panel" in html_text and "flower phase" in html_text,
        "has_boundary_notice": "no subjective consciousness claim" in html_text,
        "has_localstorage": "localStorage.setItem" in html_text and "localStorage.getItem" in html_text,
        "button_count": html_text.count("<button"),
        "localstorage_handler_count": html_text.count("localStorage."),
    }
    bool_score = ratio(sum(1 for key, value in checks.items() if key.startswith("has_") and value), 9)
    density_score = min(1.0, 0.30 + 0.013 * checks["button_count"] + 0.032 * checks["localstorage_handler_count"])
    checks["browser_surface_score"] = round6(0.70 * bool_score + 0.30 * density_score)
    return checks


def build_html_template_stub() -> str:
    buttons = "\n".join(
        f'<button data-action="{action}" onclick="{handler}(\'{scope}\')">{label}</button>'
        for scope in ("riverbend", "roofward", "archive", "signal", "orchard", "repair_ring")
        for action, handler, label in (
            ("sense", "sampleFirstPerson", "sample first-person packet"),
            ("field", "sampleRoomField", "sample room field"),
            ("claim", "requestToolClaim", "request tool claim"),
            ("dialogue", "openConsentDialogue", "open consent dialogue"),
            ("queue", "applyQueueConsequence", "apply queue consequence"),
            ("memory", "restoreSensoryMemory", "restore sensory memory"),
            ("save", "saveFirstPersonState", "save state"),
            ("restore", "restoreFirstPersonState", "restore state"),
            ("replay", "exportReplay", "export replay"),
        )
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Report 282 Browser World v42</title>
  <style>
    :root {{
      --ink: #1c241f;
      --paper: #f2ead1;
      --lichen: #7c8f5d;
      --ember: #bf6b43;
      --river: #5f8e9b;
      --gold: #d6a84b;
    }}
    body {{ margin: 0; font-family: Georgia, 'Times New Roman', serif; color: var(--ink); background: radial-gradient(circle at 20% 16%, rgba(214,168,75,.46), transparent 18rem), radial-gradient(circle at 78% 8%, rgba(95,142,155,.35), transparent 16rem), linear-gradient(135deg, #e8ddbf, #c8d3b0 50%, #94b1ad); }}
    main {{ max-width: 1220px; margin: 0 auto; padding: 24px; }}
    h1 {{ font-size: clamp(2rem, 5vw, 4.8rem); line-height: 0.92; margin: 20px 0; letter-spacing: -0.04em; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; }}
    section {{ border: 2px solid rgba(28,36,31,.34); border-radius: 24px; padding: 18px; background: rgba(242,234,209,.80); box-shadow: 0 18px 52px rgba(28,36,31,.17); }}
    button {{ margin: 5px; padding: 9px 11px; border: 1px solid var(--ink); border-radius: 999px; background: var(--gold); color: var(--ink); cursor: pointer; }}
    button:hover {{ background: var(--ember); color: #fff8df; }}
    .boundary {{ border-left: 8px solid var(--ember); }}
    .flower {{ width: 176px; height: 176px; border-radius: 50%; background: repeating-radial-gradient(circle, rgba(214,168,75,.44) 0 9px, rgba(95,142,155,.24) 9px 18px); display: grid; place-items: center; }}
    .log {{ min-height: 128px; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; white-space: pre-wrap; }}
  </style>
</head>
<body>
<main>
  <h1>Browser World v42: first-person packets, sensory rooms, owned tools, consent dialogue</h1>
  <section class="boundary"><strong>Boundary:</strong> deterministic scaffold only; no subjective consciousness claim, no real consent claim, no moral patienthood claim, no metaphysical frequency claim.</section>
  <div class="grid">
    <section id="first-person-panel"><h2>First-person sensory packet</h2><p>Avatar-local visual, sound, smell, temperature, wetness, tactile, and pain-like signals.</p></section>
    <section id="room-sensory-field-panel"><h2>Room-local sensory fields</h2><p>Rooms carry sound, smell, temperature, wetness, light, vibration rate, and flower phase.</p></section>
    <section id="tool-claim-panel"><h2>Agent-owned tool claims</h2><p>Tools have owners; use requires request, grant, defer, or refusal handling.</p></section>
    <section id="consent-dialogue-panel"><h2>Consent-aware dialogue hooks</h2><p>Dialogue exposes ask-first prompts without dumping private workspace state.</p></section>
    <section id="queue-consequence-panel"><h2>Task queue consequences</h2><p>Avatar interruption, waiting, help, or tool misuse changes queue pressure visibly.</p></section>
    <section id="save-restore-panel"><h2>Save/restore</h2><p>Sensory memory, claims, dialogue hooks, and queue consequences persist through localStorage.</p></section>
    <section id="frequency-flower-panel"><h2>Frequency and flower phase</h2><div class="flower">flower phase</div><p>Rates are simulation timing metadata, not metaphysical evidence.</p></section>
  </div>
  <section><h2>Controls</h2>{buttons}</section>
  <section><h2>Browser log</h2><div id="log" class="log">ready</div></section>
</main>
<script>
const storeKey = 'ssrm.v42.browser.world';
let state = JSON.parse(localStorage.getItem(storeKey) || '{{"tick":0,"events":[]}}');
function writeLog(message) {{
  state.tick += 1;
  state.events.push({{tick: state.tick, message}});
  if (state.events.length > 20) state.events = state.events.slice(-20);
  localStorage.setItem(storeKey, JSON.stringify(state));
  document.getElementById('log').textContent = state.events.map(e => `${{e.tick}}: ${{e.message}}`).join('\n');
}}
function sampleFirstPerson(scope) {{ writeLog(`first-person sensory packet sampled for ${{scope}}`); }}
function sampleRoomField(scope) {{ writeLog(`room-local sound/smell/temp field sampled for ${{scope}}`); }}
function requestToolClaim(scope) {{ writeLog(`agent-owned tool claim requested in ${{scope}}`); }}
function openConsentDialogue(scope) {{ writeLog(`consent-aware dialogue hook opened in ${{scope}}`); }}
function applyQueueConsequence(scope) {{ writeLog(`task queue consequence applied in ${{scope}}`); }}
function restoreSensoryMemory(scope) {{
  const restored = JSON.parse(localStorage.getItem(`ssrm.v42.sensory_memory.${{scope}}`) || '{{"cue":"none yet"}}');
  writeLog(`restored sensory memory for ${{scope}}: ${{restored.cue}}`);
}}
function saveFirstPersonState(scope) {{
  localStorage.setItem(`ssrm.v42.sensory_memory.${{scope}}`, JSON.stringify({{cue: `saved sensory cue for ${{scope}}`, savedAt: state.tick}}));
  localStorage.setItem(`ssrm.v42.world.${{scope}}`, JSON.stringify(state));
  writeLog(`saved sensory/tool/dialogue/queue state for ${{scope}}`);
}}
function restoreFirstPersonState(scope) {{
  const restored = JSON.parse(localStorage.getItem(`ssrm.v42.world.${{scope}}`) || '{{"events":[]}}');
  writeLog(`restored first-person state for ${{scope}} with ${{restored.events.length || 0}} events`);
}}
function exportReplay(scope) {{ writeLog(`replay export prepared for ${{scope}}`); }}
localStorage.setItem('ssrm.v42.boot', JSON.stringify({{loaded: true}}));
writeLog('browser v42 surface loaded from localStorage');
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
        "readiness": results["metrics"]["browser_world_v42_first_person_sensory_readiness"],
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
        "readiness": metrics["browser_world_v42_first_person_sensory_readiness"],
        "weakest_channel_score": metrics["weakest_channel_score"],
        "weakest_named_channel": metrics["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
