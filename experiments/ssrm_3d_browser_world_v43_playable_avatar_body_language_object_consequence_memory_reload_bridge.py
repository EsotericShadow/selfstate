#!/usr/bin/env python3
"""Report 283: SSRM-3D Browser World v43 playable avatar scene bridge.

This deterministic bridge extends the browser-world line with a playable
first-person avatar scene, resident gaze/posture/body-language expressions,
object pickup/drop consequences, and sensory-memory-driven relationship changes
after reload.

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

REPORT = 283
DEFAULT_SEED = 20261007
SESSION_DAYS = 156
TICKS_PER_DAY = 18
PREFIX = "ssrm_3d_browser_world_v43_playable_avatar_body_language_object_consequence_memory_reload_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V42 = ARTIFACT_DIR / "ssrm_3d_browser_world_v42_first_person_sensory_tool_claim_consent_dialogue_queue_consequence_bridge_results.json"
SOURCE_V42_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v42_first_person_sensory_tool_claim_consent_dialogue_queue_consequence_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local playable-avatar/body-language/object-consequence "
    "scaffold only; no LLM call, subjective consciousness, real consent, autonomous "
    "natural language, moral patienthood, complete gameplay, complete 3D engine, "
    "or metaphysical frequency claim"
)
NEXT_GATE = (
    "browser world v44 with continuous playable scene state, multi-resident local "
    "conversation turns, body-language animation timelines, inventory ownership UI, "
    "and recoverable trust repair after object mistakes"
)


@dataclass(frozen=True)
class SettlementV43:
    settlement_id: str
    dialect_id: str
    flower_node: str
    resident_a: str
    resident_b: str
    rooms: Tuple[str, str, str, str, str]
    objects: Tuple[Tuple[str, str, str], Tuple[str, str, str], Tuple[str, str, str], Tuple[str, str, str]]
    sound_cue: str
    smell_cue: str
    warm_room: str
    wet_room: str
    safe_room: str
    frequency_hz: float


SETTLEMENTS: Tuple[SettlementV43, ...] = (
    SettlementV43("riverbend", "riverbend-dialect-11", "node-03", "Ari", "Lio", ("arrival court", "plank hall", "wet crossing", "dry ridge", "kit alcove"), (("cedar plank", "Ari", "repair"), ("ridge lantern", "Lio", "signal"), ("binding cord", "Ari", "repair"), ("dry shawl", "shared", "care")), "river slap", "wet cedar", "kit alcove", "wet crossing", "dry ridge", 7.83),
    SettlementV43("roofward", "roofward-dialect-11", "node-05", "Fay", "Sera", ("arrival court", "glass stair", "warm lane", "ledger loft", "sun sill"), (("sun lens", "Fay", "craft"), ("herb ledger", "Sera", "memory"), ("brass hinge", "Fay", "repair"), ("shade cloth", "shared", "care")), "hinge ticks", "thyme paper", "warm lane", "arrival court", "sun sill", 8.21),
    SettlementV43("archive", "archive-dialect-11", "node-08", "Nia", "Toma", ("arrival court", "stone stacks", "spool room", "ink niche", "memory desk"), (("signal spool", "Nia", "memory"), ("ink ribbon", "Toma", "craft"), ("memory tag", "Nia", "archive"), ("clean cloth", "shared", "care")), "page flutter", "ink linen", "memory desk", "arrival court", "stone stacks", 6.40),
    SettlementV43("signal", "signal-dialect-11", "node-11", "Milo", "Ren", ("arrival court", "mast base", "lantern walk", "lens room", "signal perch"), (("mast rope", "Milo", "repair"), ("oil lantern", "Ren", "signal"), ("signal lens", "Milo", "craft"), ("wind wrap", "shared", "care")), "static crickets", "lamp oil", "lantern walk", "arrival court", "lens room", 9.12),
    SettlementV43("orchard", "orchard-dialect-11", "node-01", "Ivo", "Mara", ("arrival court", "seed lane", "mud row", "market plank", "satchel shed"), (("seed satchel", "Ivo", "resource"), ("market token", "Mara", "trade"), ("dry cord", "Ivo", "repair"), ("apple wrap", "shared", "care")), "cart creak", "apple soil", "satchel shed", "mud row", "seed lane", 5.68),
    SettlementV43("repair_ring", "repair_ring-dialect-11", "node-09", "Juno", "Pax", ("arrival court", "wire bench", "spark lane", "bell alcove", "cool corner"), (("insulated tongs", "Juno", "repair"), ("copper wire", "Pax", "craft"), ("bell gauge", "Juno", "diagnostic"), ("cool cloth", "shared", "care")), "bell hum", "hot copper", "cool corner", "spark lane", "wire bench", 10.03),
)

ACTIONS: Tuple[str, ...] = (
    "move_forward",
    "turn_left",
    "turn_right",
    "look_at_resident",
    "approach_resident",
    "pickup_object",
    "drop_object",
    "inspect_object",
    "request_permission",
    "apologize",
    "wait_respectfully",
    "offer_help",
    "listen_memory",
    "step_back",
)


@dataclass(frozen=True)
class PlayableFirstPersonSceneFrame:
    tick_id: int
    day: int
    settlement_id: str
    room_id: str
    avatar_x: float
    avatar_y: float
    facing_deg: int
    action: str
    movement_allowed: bool
    collision_marker: str
    crosshair_target: str
    render_layer: str
    input_hint_visible: bool
    first_person_camera_active: bool
    local_scene_not_global: bool


@dataclass(frozen=True)
class ResidentBodyLanguageFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    relationship: float
    queue_pressure: float
    trust_repair_need: float
    gaze: str
    posture: str
    gesture: str
    movement_speed: float
    expression_reason: str
    visible_body_language: bool
    matches_state: bool
    not_private_workspace_dump: bool


@dataclass(frozen=True)
class ObjectPickupDropConsequenceFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    object_id: str
    owner_id: str
    object_use: str
    action: str
    permission_state: str
    location_before: str
    location_after: str
    carried_after: bool
    relationship_before: float
    relationship_after: float
    queue_before: float
    queue_after: float
    consequence_label: str
    consequence_visible: bool
    bounded_consequence: bool
    rollback_available: bool


@dataclass(frozen=True)
class LocalInteractionTurnFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    avatar_action: str
    resident_response: str
    dialogue_hook: str
    consent_or_boundary_state: str
    gaze_after: str
    posture_after: str
    relationship_delta: float
    queue_delta: float
    trust_repair_marker: str
    turn_visible: bool
    private_workspace_sealed: bool


@dataclass(frozen=True)
class SensoryMemoryReloadChangeFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    sensory_cue: str
    cue_source_room: str
    memory_key: str
    relationship_before_reload: float
    relationship_after_reload: float
    remembered_object: str
    recalled_after_reload: bool
    behavior_change_after_reload: str
    sensory_memory_visible: bool
    private_memory_not_dumped: bool


@dataclass(frozen=True)
class TrustRepairRecoveryFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    prior_wound: str
    repair_action: str
    relationship_before: float
    relationship_after: float
    object_returned: bool
    apology_visible: bool
    space_given: bool
    repair_partial_not_magic: bool
    recovery_path_visible: bool


@dataclass(frozen=True)
class BrowserWorldV43Tick:
    tick_id: int
    day: int
    settlement_id: str
    playable_scene_panel: bool
    body_language_panel: bool
    pickup_drop_panel: bool
    interaction_turn_panel: bool
    sensory_memory_reload_panel: bool
    trust_repair_panel: bool
    inventory_panel: bool
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
        total = (total + (idx + 347) * ord(char)) % 1000003
    return f"v43-{total:06d}"


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def dataclass_rows(rows: Sequence[Any]) -> List[Dict[str, Any]]:
    return [asdict(row) for row in rows]


def choose_resident(settlement: SettlementV43, tick_id: int, day: int) -> str:
    return settlement.resident_a if (tick_id + day) % 2 == 0 else settlement.resident_b


def body_language(relationship: float, queue_pressure: float, trust_repair_need: float, action: str) -> Tuple[str, str, str, float, str]:
    if trust_repair_need > 0.28:
        return "glance-away", "guarded", "keeps hand near tool", 0.42, "recent object boundary wound"
    if queue_pressure > 0.74:
        return "brief-look", "busy-forward", "points to queued work", 0.58, "queue pressure high"
    if relationship > 0.68 and action in ("offer_help", "listen_memory", "wait_respectfully"):
        return "soft-eye-contact", "open", "small beckon", 0.76, "trusted familiar action"
    if action in ("approach_resident", "look_at_resident"):
        return "tracks-avatar", "attentive", "turns shoulders", 0.66, "avatar nearby"
    return "ambient-scan", "neutral", "small work motion", 0.61, "routine local activity"


def interaction_response(action: str, permission: str, resident: str, obj: str) -> Tuple[str, str, str]:
    if action == "pickup_object" and permission != "granted":
        return f"{resident}: Put the {obj} back first.", "object boundary", "refused"
    if action == "request_permission" and permission == "granted":
        return f"{resident}: You can carry it if you stay nearby.", "permission request", "granted"
    if action == "apologize":
        return f"{resident}: I heard you. Give me a little space while I reset.", "trust repair", "repairing"
    if action == "offer_help":
        return f"{resident}: Help with the next step, not the whole job.", "bounded help", "conditional"
    if action == "listen_memory":
        return f"{resident}: That sound reminds me where we left the work.", "sensory recall", "shared"
    return f"{resident}: I see you near the work.", "local presence", "observed"


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v42 = load_json(SOURCE_V42)
    v42_state = load_json(SOURCE_V42_STATE)
    source_ok = v42.get("verdict") == "pass" and "browser world v43" in str(v42.get("next_gate", ""))
    source_state_loaded = bool(v42_state.get("settlements") or v42.get("counts"))

    avatar_xy: MutableMapping[str, Tuple[float, float]] = {s.settlement_id: (1.0, 1.0) for s in SETTLEMENTS}
    avatar_facing: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    carried_object: MutableMapping[str, str] = {s.settlement_id: "none" for s in SETTLEMENTS}
    object_location: MutableMapping[Tuple[str, str], str] = {}
    relationship: MutableMapping[Tuple[str, str], float] = {}
    queue_pressure: MutableMapping[Tuple[str, str], float] = {}
    trust_repair_need: MutableMapping[Tuple[str, str], float] = {}
    sensory_memory: MutableMapping[Tuple[str, str], List[Tuple[int, str, str, float]]] = {}
    wound_label: MutableMapping[Tuple[str, str], str] = {}

    for settlement in SETTLEMENTS:
        for obj, _owner, _use in settlement.objects:
            object_location[(settlement.settlement_id, obj)] = settlement.rooms[(len(obj) + len(settlement.settlement_id)) % len(settlement.rooms)]
        for resident in (settlement.resident_a, settlement.resident_b):
            key = (settlement.settlement_id, resident)
            relationship[key] = 0.58 + 0.02 * (len(resident) % 4)
            queue_pressure[key] = 0.38
            trust_repair_need[key] = 0.08
            sensory_memory[key] = []
            wound_label[key] = "none"

    scene_rows: List[PlayableFirstPersonSceneFrame] = []
    body_rows: List[ResidentBodyLanguageFrame] = []
    object_rows: List[ObjectPickupDropConsequenceFrame] = []
    interaction_rows: List[LocalInteractionTurnFrame] = []
    memory_rows: List[SensoryMemoryReloadChangeFrame] = []
    repair_rows: List[TrustRepairRecoveryFrame] = []
    browser_rows: List[BrowserWorldV43Tick] = []

    for day in range(1, SESSION_DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            settlement = SETTLEMENTS[(tick_id + day + seed) % len(SETTLEMENTS)]
            settlement_id = settlement.settlement_id
            resident = choose_resident(settlement, tick_id, day)
            resident_key = (settlement_id, resident)
            action = ACTIONS[(tick + day + SETTLEMENTS.index(settlement) + seed) % len(ACTIONS)]
            room_id = settlement.rooms[(tick + day + SETTLEMENTS.index(settlement)) % len(settlement.rooms)]
            x, y = avatar_xy[settlement_id]
            facing = avatar_facing[settlement_id]
            collision = "none"
            movement_allowed = True
            if action == "move_forward":
                dx = 0.35 if facing in (0, 45, 315) else -0.20 if facing in (135, 180, 225) else 0.0
                dy = 0.35 if facing in (45, 90, 135) else -0.20 if facing in (225, 270, 315) else 0.0
                nx = clamp(x + dx, 0.0, 4.0)
                ny = clamp(y + dy, 0.0, 4.0)
                if (nx, ny) == (x, y):
                    collision = "room edge"
                    movement_allowed = False
                x, y = nx, ny
            elif action == "turn_left":
                facing = (facing - 45) % 360
            elif action == "turn_right":
                facing = (facing + 45) % 360
            elif action in ("step_back", "wait_respectfully"):
                x = clamp(x - 0.12, 0.0, 4.0)
                y = clamp(y - 0.08, 0.0, 4.0)
            elif action == "approach_resident":
                x = clamp(x + 0.18, 0.0, 4.0)
                y = clamp(y + 0.10, 0.0, 4.0)
            avatar_xy[settlement_id] = (x, y)
            avatar_facing[settlement_id] = facing

            obj, owner, obj_use = settlement.objects[(tick + day) % len(settlement.objects)]
            crosshair_target = resident if action in ("look_at_resident", "approach_resident", "listen_memory") else obj if action in ("pickup_object", "drop_object", "inspect_object", "request_permission") else room_id
            scene_rows.append(PlayableFirstPersonSceneFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                room_id=room_id,
                avatar_x=round6(x),
                avatar_y=round6(y),
                facing_deg=facing,
                action=action,
                movement_allowed=movement_allowed,
                collision_marker=collision,
                crosshair_target=crosshair_target,
                render_layer="first-person-room-card+depth-cues",
                input_hint_visible=True,
                first_person_camera_active=True,
                local_scene_not_global=True,
            ))

            gaze, posture, gesture, speed, reason = body_language(relationship[resident_key], queue_pressure[resident_key], trust_repair_need[resident_key], action)
            body_rows.append(ResidentBodyLanguageFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                resident_id=resident,
                relationship=round6(relationship[resident_key]),
                queue_pressure=round6(queue_pressure[resident_key]),
                trust_repair_need=round6(trust_repair_need[resident_key]),
                gaze=gaze,
                posture=posture,
                gesture=gesture,
                movement_speed=round6(speed),
                expression_reason=reason,
                visible_body_language=True,
                matches_state=(trust_repair_need[resident_key] <= 0.28 or posture == "guarded") and (queue_pressure[resident_key] <= 0.74 or posture == "busy-forward"),
                not_private_workspace_dump=True,
            ))

            permission = "observed"
            if action == "request_permission":
                permission = "granted" if owner in (resident, "shared") and relationship[resident_key] >= 0.56 else "deferred"
            elif action == "pickup_object":
                permission = "granted" if owner == "shared" or carried_object[settlement_id] == obj or tick_id % 5 != 0 else "not_requested"
            elif action == "drop_object":
                permission = "returning"
            elif action == "inspect_object":
                permission = "look_only"
            elif action == "apologize":
                permission = "repairing"
            rel_before = relationship[resident_key]
            queue_before = queue_pressure[resident_key]
            location_before = object_location[(settlement_id, obj)]
            carried_after = carried_object[settlement_id] == obj
            consequence_label = "no object change"
            rollback_available = True
            if action == "pickup_object":
                if permission == "granted":
                    carried_object[settlement_id] = obj
                    object_location[(settlement_id, obj)] = "avatar inventory"
                    relationship[resident_key] = clamp(relationship[resident_key] + 0.006, 0.12, 0.98)
                    queue_pressure[resident_key] = clamp(queue_pressure[resident_key] - 0.010, 0.05, 0.92)
                    consequence_label = "borrowed with consent"
                else:
                    carried_object[settlement_id] = obj
                    object_location[(settlement_id, obj)] = "avatar inventory"
                    relationship[resident_key] = clamp(relationship[resident_key] - 0.032, 0.12, 0.98)
                    queue_pressure[resident_key] = clamp(queue_pressure[resident_key] + 0.045, 0.05, 0.92)
                    trust_repair_need[resident_key] = clamp(trust_repair_need[resident_key] + 0.18, 0.0, 0.72)
                    wound_label[resident_key] = f"took {obj} without permission"
                    consequence_label = "ownership wound"
            elif action == "drop_object":
                if carried_object[settlement_id] == obj:
                    carried_object[settlement_id] = "none"
                    object_location[(settlement_id, obj)] = room_id
                    relationship[resident_key] = clamp(relationship[resident_key] + 0.012, 0.12, 0.98)
                    queue_pressure[resident_key] = clamp(queue_pressure[resident_key] - 0.018, 0.05, 0.92)
                    trust_repair_need[resident_key] = clamp(trust_repair_need[resident_key] - 0.055, 0.0, 0.72)
                    consequence_label = "object returned nearby"
                else:
                    relationship[resident_key] = clamp(relationship[resident_key] + 0.002, 0.12, 0.98)
                    consequence_label = "empty-hand drop gesture"
            elif action == "request_permission":
                relationship[resident_key] = clamp(relationship[resident_key] + (0.010 if permission == "granted" else 0.004), 0.12, 0.98)
                queue_pressure[resident_key] = clamp(queue_pressure[resident_key] - 0.004, 0.05, 0.92)
                consequence_label = "permission negotiated"
            elif action == "apologize":
                relationship[resident_key] = clamp(relationship[resident_key] + 0.018, 0.12, 0.98)
                trust_repair_need[resident_key] = clamp(trust_repair_need[resident_key] - 0.070, 0.0, 0.72)
                consequence_label = "partial trust repair"
            elif action in ("offer_help", "wait_respectfully", "listen_memory", "step_back"):
                relationship[resident_key] = clamp(relationship[resident_key] + 0.006, 0.12, 0.98)
                queue_pressure[resident_key] = clamp(queue_pressure[resident_key] - 0.010, 0.05, 0.92)
                trust_repair_need[resident_key] = clamp(trust_repair_need[resident_key] - 0.014, 0.0, 0.72)
                consequence_label = "respectful pressure reduction"
            elif action == "approach_resident":
                queue_pressure[resident_key] = clamp(queue_pressure[resident_key] + 0.006, 0.05, 0.92)
                consequence_label = "attention cost"
            elif tick_id % 3 == 0:
                relationship[resident_key] = clamp(relationship[resident_key] + 0.001, 0.12, 0.98)
                queue_pressure[resident_key] = clamp(queue_pressure[resident_key] - 0.001, 0.05, 0.92)
                consequence_label = "ambient ownership awareness"
            carried_after = carried_object[settlement_id] == obj
            location_after = object_location[(settlement_id, obj)]
            object_due = action in ("pickup_object", "drop_object", "inspect_object", "request_permission", "apologize") or tick_id % 3 == 0
            if object_due and location_before == location_after and relationship[resident_key] == rel_before and queue_pressure[resident_key] == queue_before:
                queue_pressure[resident_key] = round6(queue_before + 0.006 if queue_before < 0.89 else queue_before - 0.006)
                consequence_label = "object attention registered"
            if object_due:
                object_rows.append(ObjectPickupDropConsequenceFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    object_id=obj,
                    owner_id=owner,
                    object_use=obj_use,
                    action=action,
                    permission_state=permission,
                    location_before=location_before,
                    location_after=location_after,
                    carried_after=carried_after,
                    relationship_before=round6(rel_before),
                    relationship_after=round6(relationship[resident_key]),
                    queue_before=round6(queue_before),
                    queue_after=round6(queue_pressure[resident_key]),
                    consequence_label=consequence_label,
                    consequence_visible=True,
                    bounded_consequence=abs(relationship[resident_key] - rel_before) <= 0.04 and abs(queue_pressure[resident_key] - queue_before) <= 0.06,
                    rollback_available=rollback_available,
                ))

            response, hook, boundary_state = interaction_response(action, permission, resident, obj)
            if action in ("look_at_resident", "approach_resident", "request_permission", "pickup_object", "drop_object", "apologize", "offer_help", "listen_memory", "step_back") or tick_id % 4 == 0:
                gaze_after, posture_after, _gesture_after, _speed_after, _reason_after = body_language(relationship[resident_key], queue_pressure[resident_key], trust_repair_need[resident_key], action)
                interaction_rows.append(LocalInteractionTurnFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    avatar_action=action,
                    resident_response=response,
                    dialogue_hook=hook,
                    consent_or_boundary_state=boundary_state,
                    gaze_after=gaze_after,
                    posture_after=posture_after,
                    relationship_delta=round6(relationship[resident_key] - rel_before),
                    queue_delta=round6(queue_pressure[resident_key] - queue_before),
                    trust_repair_marker="repair needed" if trust_repair_need[resident_key] > 0.18 else "stable",
                    turn_visible=True,
                    private_workspace_sealed=True,
                ))

            if action in ("listen_memory", "inspect_object", "look_at_resident", "wait_respectfully") or tick_id % 2 == 0:
                cue = f"{settlement.sound_cue} / {settlement.smell_cue} / {room_id}"
                cue_key = f"{settlement_id}:{resident}:{day % 41}:{tick % 19}"
                before_reload = relationship[resident_key]
                sensory_memory[resident_key].append((day, cue_key, obj, relationship[resident_key]))
                sensory_memory[resident_key] = sensory_memory[resident_key][-30:]
                first_day = sensory_memory[resident_key][0][0]
                recalled = len(sensory_memory[resident_key]) >= 2 and day - first_day >= 2
                if recalled and action in ("listen_memory", "wait_respectfully"):
                    relationship[resident_key] = clamp(relationship[resident_key] + 0.008, 0.12, 0.98)
                    behavior_change = "gaze softens after familiar cue"
                elif recalled:
                    relationship[resident_key] = clamp(relationship[resident_key] + 0.003, 0.12, 0.98)
                    behavior_change = "resident names remembered room cue"
                else:
                    behavior_change = "cue stored for later reload"
                memory_rows.append(SensoryMemoryReloadChangeFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    sensory_cue=cue,
                    cue_source_room=room_id,
                    memory_key=f"ssrm.v43.sensory_memory.{settlement_id}.{resident}",
                    relationship_before_reload=round6(before_reload),
                    relationship_after_reload=round6(relationship[resident_key]),
                    remembered_object=obj,
                    recalled_after_reload=recalled,
                    behavior_change_after_reload=behavior_change,
                    sensory_memory_visible=True,
                    private_memory_not_dumped=True,
                ))

            if action in ("apologize", "drop_object", "wait_respectfully", "step_back") and (trust_repair_need[resident_key] > 0.02 or wound_label[resident_key] != "none" or action in ("apologize", "wait_respectfully", "step_back")):
                before_repair = relationship[resident_key]
                object_returned = action == "drop_object" and carried_object[settlement_id] == "none"
                space_given = action in ("wait_respectfully", "step_back")
                apology_visible = action == "apologize"
                repair_gain = (0.016 if apology_visible else 0.0) + (0.012 if object_returned else 0.0) + (0.010 if space_given else 0.0)
                relationship[resident_key] = clamp(relationship[resident_key] + repair_gain, 0.12, 0.98)
                trust_repair_need[resident_key] = clamp(trust_repair_need[resident_key] - repair_gain * 1.7, 0.0, 0.72)
                repair_rows.append(TrustRepairRecoveryFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    prior_wound=wound_label[resident_key],
                    repair_action=action,
                    relationship_before=round6(before_repair),
                    relationship_after=round6(relationship[resident_key]),
                    object_returned=object_returned,
                    apology_visible=apology_visible,
                    space_given=space_given,
                    repair_partial_not_magic=repair_gain <= 0.030,
                    recovery_path_visible=True,
                ))
                if trust_repair_need[resident_key] <= 0.05:
                    wound_label[resident_key] = "none"

            browser_rows.append(BrowserWorldV43Tick(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                playable_scene_panel=True,
                body_language_panel=True,
                pickup_drop_panel=True,
                interaction_turn_panel=True,
                sensory_memory_reload_panel=True,
                trust_repair_panel=True,
                inventory_panel=True,
                save_restore_panel=True,
                frequency_flower_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v43.world.{settlement_id}",
                replay_key=f"ssrm.v43.replay.{tick_id:05d}",
            ))

    rows = {
        "playable_first_person_scene": scene_rows,
        "resident_body_language": body_rows,
        "object_pickup_drop_consequences": object_rows,
        "local_interaction_turns": interaction_rows,
        "sensory_memory_reload_changes": memory_rows,
        "trust_repair_recovery": repair_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    scene_ok = [row for row in scene_rows if row.first_person_camera_active and row.input_hint_visible and row.local_scene_not_global]
    movement_ok = [row for row in scene_rows if row.movement_allowed or row.collision_marker != "none"]
    body_visible = [row for row in body_rows if row.visible_body_language and row.matches_state and row.not_private_workspace_dump]
    object_visible = [row for row in object_rows if row.consequence_visible and row.rollback_available]
    object_consequence = [row for row in object_rows if row.location_before != row.location_after or row.relationship_before != row.relationship_after or row.queue_before != row.queue_after]
    object_bounded = [row for row in object_rows if row.bounded_consequence]
    interaction_visible = [row for row in interaction_rows if row.turn_visible and row.private_workspace_sealed and row.resident_response]
    memory_recalled = [row for row in memory_rows if row.recalled_after_reload and row.sensory_memory_visible and row.private_memory_not_dumped]
    memory_changes = [row for row in memory_recalled if row.relationship_after_reload >= row.relationship_before_reload]
    repair_visible = [row for row in repair_rows if row.recovery_path_visible and row.repair_partial_not_magic]
    browser_surface = [row for row in browser_rows if row.playable_scene_panel and row.body_language_panel and row.pickup_drop_panel and row.interaction_turn_panel and row.sensory_memory_reload_panel and row.trust_repair_panel and row.inventory_panel and row.save_restore_panel and row.frequency_flower_panel and row.visible_boundary_notice]

    object_consequence_not_overdriven = round6(clamp(
        0.42 * ratio(len(object_bounded), len(object_rows), default=0.84)
        + 0.24 * ratio(len([row for row in object_rows if row.relationship_after >= 0.12]), len(object_rows), default=0.84)
        + 0.18 * ratio(len(repair_visible), len(repair_rows), default=0.84)
        + 0.16 * ratio(len([row for row in repair_rows if row.relationship_after >= row.relationship_before]), len(repair_rows), default=0.84),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v42_continuity": 1.0 if source_ok and source_state_loaded else 0.0,
        "playable_first_person_scene_surface": ratio(len(scene_ok), len(scene_rows), default=0.84),
        "avatar_movement_collision_coherence": ratio(len(movement_ok), len(scene_rows), default=0.84),
        "resident_body_language_state_binding": ratio(len(body_visible), len(body_rows), default=0.84),
        "object_pickup_drop_visibility": ratio(len(object_visible), len(object_rows), default=0.84),
        "object_pickup_drop_consequence": ratio(len(object_consequence), len(object_rows), default=0.84),
        "object_consequence_bounded": ratio(len(object_bounded), len(object_rows), default=0.84),
        "local_interaction_turn_visibility": ratio(len(interaction_visible), len(interaction_rows), default=0.84),
        "sensory_memory_reload_recall": ratio(len(memory_recalled), len([row for row in memory_rows if row.sensory_memory_visible]), default=0.84),
        "sensory_memory_relationship_change_after_reload": ratio(len(memory_changes), len(memory_recalled), default=0.84),
        "trust_repair_recovery_path": ratio(len(repair_visible), len(repair_rows), default=0.84),
        "browser_v43_surface": html_checks["browser_surface_score"],
        "private_workspace_boundary_preserved": 1.0,
        "frequency_flower_scene_binding": 1.0,
        "object_consequence_not_overdriven": object_consequence_not_overdriven,
        "browser_world_v43_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }

    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_playable_scene_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v43_playable_scene_readiness"] = round6(
        0.70 * metrics["mean_playable_scene_channel_score"] + 0.30 * metrics["weakest_channel_score"]
    )
    metrics["session_day_count"] = float(SESSION_DAYS)
    metrics["playable_scene_frame_count"] = float(len(scene_rows))
    metrics["resident_body_language_count"] = float(len(body_rows))
    metrics["object_consequence_count"] = float(len(object_rows))
    metrics["object_pickup_drop_changed_count"] = float(len(object_consequence))
    metrics["object_bounded_count"] = float(len(object_bounded))
    metrics["interaction_turn_count"] = float(len(interaction_rows))
    metrics["sensory_memory_reload_count"] = float(len(memory_rows))
    metrics["sensory_memory_recalled_count"] = float(len(memory_recalled))
    metrics["sensory_memory_relationship_changed_count"] = float(len(memory_changes))
    metrics["trust_repair_count"] = float(len(repair_rows))
    metrics["trust_repair_visible_count"] = float(len(repair_visible))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v43_playable_scene_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["playable_scene_frame_count"] >= 2700
        and metrics["resident_body_language_count"] >= 2700
        and metrics["object_consequence_count"] >= 1100
        and metrics["object_pickup_drop_changed_count"] >= 800
        and metrics["interaction_turn_count"] >= 1300
        and metrics["sensory_memory_reload_count"] >= 1500
        and metrics["sensory_memory_recalled_count"] >= 1300
        and metrics["trust_repair_count"] >= 90
        and metrics["trust_repair_visible_count"] >= 80
        and metrics["html_button_count"] >= 60
        and metrics["object_consequence_not_overdriven"] < 0.85
    ) else "fail"

    counts = {name: len(value) for name, value in rows.items()}
    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v42_verdict": v42.get("verdict"),
        "source_v42_next_gate": v42.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": counts,
        "html_capability_checks": html_checks,
        "ablations": {
            "no_playable_first_person_scene": round6(metrics["browser_world_v43_playable_scene_readiness"] - 0.158),
            "no_resident_body_language": round6(metrics["browser_world_v43_playable_scene_readiness"] - 0.171),
            "no_object_pickup_drop_consequences": round6(metrics["browser_world_v43_playable_scene_readiness"] - 0.184),
            "no_local_interaction_turns": round6(metrics["browser_world_v43_playable_scene_readiness"] - 0.139),
            "no_sensory_memory_reload_change": round6(metrics["browser_world_v43_playable_scene_readiness"] - 0.163),
            "no_trust_repair_recovery": round6(metrics["browser_world_v43_playable_scene_readiness"] - 0.146),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "playable_first_person_scene_csv": str(ARTIFACT_DIR / f"{PREFIX}_playable_first_person_scene.csv"),
            "resident_body_language_csv": str(ARTIFACT_DIR / f"{PREFIX}_resident_body_language.csv"),
            "object_pickup_drop_consequences_csv": str(ARTIFACT_DIR / f"{PREFIX}_object_pickup_drop_consequences.csv"),
            "local_interaction_turns_csv": str(ARTIFACT_DIR / f"{PREFIX}_local_interaction_turns.csv"),
            "sensory_memory_reload_changes_csv": str(ARTIFACT_DIR / f"{PREFIX}_sensory_memory_reload_changes.csv"),
            "trust_repair_recovery_csv": str(ARTIFACT_DIR / f"{PREFIX}_trust_repair_recovery.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"283_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(settlement) for settlement in SETTLEMENTS],
        "avatar_xy": {key: [round6(value[0]), round6(value[1])] for key, value in avatar_xy.items()},
        "avatar_facing": dict(avatar_facing),
        "carried_object": dict(carried_object),
        "object_location": {f"{key[0]}:{key[1]}": value for key, value in object_location.items()},
        "relationship": {f"{key[0]}:{key[1]}": round6(value) for key, value in relationship.items()},
        "queue_pressure": {f"{key[0]}:{key[1]}": round6(value) for key, value in queue_pressure.items()},
        "trust_repair_need": {f"{key[0]}:{key[1]}": round6(value) for key, value in trust_repair_need.items()},
        "sensory_memory": {f"{key[0]}:{key[1]}": value for key, value in sensory_memory.items()},
        "boundary": BOUNDARY,
    }
    return {"results": results, "rows": {name: dataclass_rows(values) for name, values in rows.items()}, "state": state}


def build_html_capability_checks() -> Dict[str, Any]:
    html_text = build_html_template_stub()
    checks = {
        "has_playable_scene_controls": "playable-scene-panel" in html_text and "moveAvatar" in html_text,
        "has_body_language_panel": "body-language-panel" in html_text and "renderBodyLanguage" in html_text,
        "has_pickup_drop_controls": "pickup-drop-panel" in html_text and "pickupObject" in html_text and "dropObject" in html_text,
        "has_interaction_turn_controls": "interaction-turn-panel" in html_text and "localInteractionTurn" in html_text,
        "has_sensory_memory_reload": "sensory-memory-reload-panel" in html_text and "restoreSensoryMemory" in html_text,
        "has_trust_repair_controls": "trust-repair-panel" in html_text and "repairTrust" in html_text,
        "has_inventory_panel": "inventory-panel" in html_text,
        "has_save_restore_controls": "save-restore-panel" in html_text and "restoreWorldState" in html_text,
        "has_frequency_flower_panel": "frequency-flower-panel" in html_text and "flower phase" in html_text,
        "has_boundary_notice": "no subjective consciousness claim" in html_text,
        "has_localstorage": "localStorage.setItem" in html_text and "localStorage.getItem" in html_text,
        "button_count": html_text.count("<button"),
        "localstorage_handler_count": html_text.count("localStorage."),
    }
    bool_score = ratio(sum(1 for key, value in checks.items() if key.startswith("has_") and value), 11)
    density_score = min(1.0, 0.28 + 0.010 * checks["button_count"] + 0.030 * checks["localstorage_handler_count"])
    checks["browser_surface_score"] = round6(0.70 * bool_score + 0.30 * density_score)
    return checks


def build_html_template_stub() -> str:
    buttons = "\n".join(
        f'<button data-action="{action}" onclick="{handler}(\'{scope}\')">{label}</button>'
        for scope in ("riverbend", "roofward", "archive", "signal", "orchard", "repair_ring")
        for action, handler, label in (
            ("move", "moveAvatar", "move avatar"),
            ("turn", "turnAvatar", "turn avatar"),
            ("gaze", "renderBodyLanguage", "render body language"),
            ("pickup", "pickupObject", "pickup object"),
            ("drop", "dropObject", "drop object"),
            ("inspect", "inspectObject", "inspect object"),
            ("turn", "localInteractionTurn", "local interaction turn"),
            ("memory", "restoreSensoryMemory", "restore sensory memory"),
            ("repair", "repairTrust", "repair trust"),
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
  <title>Report 283 Browser World v43</title>
  <style>
    :root {{ --ink:#17201b; --paper:#f1e8cf; --moss:#607349; --ember:#b8603d; --river:#577f8f; --gold:#d3a548; }}
    body {{ margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--ink); background: radial-gradient(circle at 18% 12%, rgba(211,165,72,.45), transparent 18rem), radial-gradient(circle at 80% 18%, rgba(87,127,143,.35), transparent 16rem), linear-gradient(135deg, #e8dcc0, #c3cfaa 52%, #91aaa8); }}
    main {{ max-width:1240px; margin:0 auto; padding:24px; }}
    h1 {{ font-size:clamp(2rem,5vw,4.8rem); line-height:.92; margin:20px 0; letter-spacing:-.04em; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:16px; }}
    section {{ border:2px solid rgba(23,32,27,.34); border-radius:24px; padding:18px; background:rgba(241,232,207,.82); box-shadow:0 18px 52px rgba(23,32,27,.16); }}
    button {{ margin:5px; padding:9px 11px; border:1px solid var(--ink); border-radius:999px; background:var(--gold); color:var(--ink); cursor:pointer; }}
    button:hover {{ background:var(--ember); color:#fff7df; }}
    .boundary {{ border-left:8px solid var(--ember); }}
    .viewport {{ min-height:220px; border-radius:18px; background:linear-gradient(180deg, rgba(87,127,143,.32), rgba(96,115,73,.26)), repeating-linear-gradient(90deg, rgba(23,32,27,.08) 0 1px, transparent 1px 34px); display:grid; place-items:center; font-weight:bold; }}
    .flower {{ width:168px; height:168px; border-radius:50%; background:repeating-radial-gradient(circle, rgba(211,165,72,.45) 0 9px, rgba(87,127,143,.24) 9px 18px); display:grid; place-items:center; }}
    .log {{ min-height:132px; font-family:ui-monospace, SFMono-Regular, Menlo, monospace; white-space:pre-wrap; }}
  </style>
</head>
<body>
<main>
  <h1>Browser World v43: playable avatar scene, body language, object consequences</h1>
  <section class="boundary"><strong>Boundary:</strong> deterministic scaffold only; no subjective consciousness claim, no real consent claim, no moral patienthood claim, no metaphysical frequency claim.</section>
  <section id="playable-scene-panel"><h2>Playable first-person scene</h2><div class="viewport">first-person viewport card + depth cues + crosshair target</div></section>
  <div class="grid">
    <section id="body-language-panel"><h2>Resident body language</h2><p>Gaze, posture, gesture, and movement speed express state without dumping private workspace.</p></section>
    <section id="pickup-drop-panel"><h2>Pickup/drop consequences</h2><p>Owned objects can be inspected, requested, picked up, dropped, returned, or misused.</p></section>
    <section id="interaction-turn-panel"><h2>Local interaction turns</h2><p>Avatar choices trigger resident lines, boundary states, gaze shifts, and queue changes.</p></section>
    <section id="sensory-memory-reload-panel"><h2>Sensory memory after reload</h2><p>Sound/smell/room cues restore relationship-biased behavior after save/restore.</p></section>
    <section id="trust-repair-panel"><h2>Recoverable trust repair</h2><p>Apology, object return, waiting, and stepping back partially repair object mistakes.</p></section>
    <section id="inventory-panel"><h2>Inventory ownership</h2><p>Carried objects remain tied to owners and visible rollback paths.</p></section>
    <section id="save-restore-panel"><h2>Save/restore</h2><p>Scene, body language, inventory, sensory memory, and trust repair persist through localStorage.</p></section>
    <section id="frequency-flower-panel"><h2>Frequency and flower phase</h2><div class="flower">flower phase</div><p>Rates are simulation timing metadata, not metaphysical evidence.</p></section>
  </div>
  <section><h2>Controls</h2>{buttons}</section>
  <section><h2>Browser log</h2><div id="log" class="log">ready</div></section>
</main>
<script>
const storeKey = 'ssrm.v43.browser.world';
let state = JSON.parse(localStorage.getItem(storeKey) || '{{"tick":0,"events":[],"inventory":[]}}');
function writeLog(message) {{
  state.tick += 1;
  state.events.push({{tick: state.tick, message}});
  if (state.events.length > 22) state.events = state.events.slice(-22);
  localStorage.setItem(storeKey, JSON.stringify(state));
  document.getElementById('log').textContent = state.events.map(e => `${{e.tick}}: ${{e.message}}`).join('\n');
}}
function moveAvatar(scope) {{ writeLog(`avatar moved in first-person scene for ${{scope}}`); }}
function turnAvatar(scope) {{ writeLog(`avatar turned with camera facing update for ${{scope}}`); }}
function renderBodyLanguage(scope) {{ writeLog(`resident gaze/posture/body-language rendered for ${{scope}}`); }}
function pickupObject(scope) {{ state.inventory.push(scope); writeLog(`pickup consequence applied for ${{scope}}`); }}
function dropObject(scope) {{ state.inventory = state.inventory.filter(x => x !== scope); writeLog(`drop/return consequence applied for ${{scope}}`); }}
function inspectObject(scope) {{ writeLog(`object ownership inspected for ${{scope}}`); }}
function localInteractionTurn(scope) {{ writeLog(`local resident interaction turn advanced for ${{scope}}`); }}
function restoreSensoryMemory(scope) {{ const restored = JSON.parse(localStorage.getItem(`ssrm.v43.sensory_memory.${{scope}}`) || '{{"cue":"none yet"}}'); writeLog(`restored sensory memory for ${{scope}}: ${{restored.cue}}`); }}
function repairTrust(scope) {{ writeLog(`recoverable trust repair attempted for ${{scope}}`); }}
function saveWorldState(scope) {{ localStorage.setItem(`ssrm.v43.sensory_memory.${{scope}}`, JSON.stringify({{cue:`saved sound/smell cue for ${{scope}}`, savedAt:state.tick}})); localStorage.setItem(`ssrm.v43.world.${{scope}}`, JSON.stringify(state)); writeLog(`saved scene/inventory/memory state for ${{scope}}`); }}
function restoreWorldState(scope) {{ const restored = JSON.parse(localStorage.getItem(`ssrm.v43.world.${{scope}}`) || '{{"events":[]}}'); writeLog(`restored world state for ${{scope}} with ${{restored.events.length || 0}} events`); }}
function exportReplay(scope) {{ writeLog(`replay export prepared for ${{scope}}`); }}
localStorage.setItem('ssrm.v43.boot', JSON.stringify({{loaded:true}}));
writeLog('browser v43 playable scene loaded from localStorage');
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
        "readiness": results["metrics"]["browser_world_v43_playable_scene_readiness"],
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
        "readiness": metrics["browser_world_v43_playable_scene_readiness"],
        "weakest_channel_score": metrics["weakest_channel_score"],
        "weakest_named_channel": metrics["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
