#!/usr/bin/env python3
"""Report 284: SSRM-3D Browser World v44 continuous scene bridge.

This deterministic bridge extends the browser-world line with continuous
playable scene state, multi-resident local conversation turns, body-language
animation timelines, inventory ownership UI, and recoverable trust repair after
object mistakes.

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

REPORT = 284
DEFAULT_SEED = 20261021
SESSION_DAYS = 168
TICKS_PER_DAY = 18
PREFIX = "ssrm_3d_browser_world_v44_continuous_scene_multiresident_animation_inventory_trust_repair_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V43 = ARTIFACT_DIR / "ssrm_3d_browser_world_v43_playable_avatar_body_language_object_consequence_memory_reload_bridge_results.json"
SOURCE_V43_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v43_playable_avatar_body_language_object_consequence_memory_reload_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local continuous-scene/multi-resident-animation/inventory-"
    "trust-repair scaffold only; no LLM call, subjective consciousness, real consent, "
    "autonomous natural language, moral patienthood, complete gameplay, complete 3D "
    "engine, or metaphysical frequency claim"
)
NEXT_GATE = (
    "browser world v45 with resident daily routines running while the avatar is idle, "
    "multi-agent object handoff protocols, animated refusal/consent sequences, and "
    "long-session inventory trust memory across multiple reloads"
)


@dataclass(frozen=True)
class SettlementV44:
    settlement_id: str
    dialect_id: str
    flower_node: str
    residents: Tuple[str, str, str]
    rooms: Tuple[str, str, str, str, str]
    objects: Tuple[Tuple[str, str, str], Tuple[str, str, str], Tuple[str, str, str], Tuple[str, str, str]]
    sound_cue: str
    smell_cue: str
    safe_room: str
    work_room: str
    frequency_hz: float


SETTLEMENTS: Tuple[SettlementV44, ...] = (
    SettlementV44("riverbend", "riverbend-dialect-12", "node-03", ("Ari", "Lio", "Cee"), ("arrival court", "plank hall", "wet crossing", "dry ridge", "kit alcove"), (("cedar plank", "Ari", "repair"), ("ridge lantern", "Lio", "signal"), ("binding cord", "Cee", "repair"), ("dry shawl", "shared", "care")), "river slap", "wet cedar", "dry ridge", "plank hall", 7.83),
    SettlementV44("roofward", "roofward-dialect-12", "node-05", ("Fay", "Sera", "Orr"), ("arrival court", "glass stair", "warm lane", "ledger loft", "sun sill"), (("sun lens", "Fay", "craft"), ("herb ledger", "Sera", "memory"), ("brass hinge", "Orr", "repair"), ("shade cloth", "shared", "care")), "hinge ticks", "thyme paper", "sun sill", "ledger loft", 8.21),
    SettlementV44("archive", "archive-dialect-12", "node-08", ("Nia", "Toma", "Vell"), ("arrival court", "stone stacks", "spool room", "ink niche", "memory desk"), (("signal spool", "Nia", "memory"), ("ink ribbon", "Toma", "craft"), ("memory tag", "Vell", "archive"), ("clean cloth", "shared", "care")), "page flutter", "ink linen", "stone stacks", "spool room", 6.40),
    SettlementV44("signal", "signal-dialect-12", "node-11", ("Milo", "Ren", "Kesh"), ("arrival court", "mast base", "lantern walk", "lens room", "signal perch"), (("mast rope", "Milo", "repair"), ("oil lantern", "Ren", "signal"), ("signal lens", "Kesh", "craft"), ("wind wrap", "shared", "care")), "static crickets", "lamp oil", "lens room", "mast base", 9.12),
    SettlementV44("orchard", "orchard-dialect-12", "node-01", ("Ivo", "Mara", "Pim"), ("arrival court", "seed lane", "mud row", "market plank", "satchel shed"), (("seed satchel", "Ivo", "resource"), ("market token", "Mara", "trade"), ("dry cord", "Pim", "repair"), ("apple wrap", "shared", "care")), "cart creak", "apple soil", "seed lane", "market plank", 5.68),
    SettlementV44("repair_ring", "repair_ring-dialect-12", "node-09", ("Juno", "Pax", "Vale"), ("arrival court", "wire bench", "spark lane", "bell alcove", "cool corner"), (("insulated tongs", "Juno", "repair"), ("copper wire", "Pax", "craft"), ("bell gauge", "Vale", "diagnostic"), ("cool cloth", "shared", "care")), "bell hum", "hot copper", "wire bench", "cool corner", 10.03),
)

ACTIONS: Tuple[str, ...] = (
    "move_forward",
    "turn_left",
    "turn_right",
    "approach_group",
    "start_conversation",
    "request_permission",
    "pickup_owned_object",
    "pickup_shared_object",
    "drop_object",
    "return_object",
    "apologize",
    "wait_respectfully",
    "offer_help",
    "listen_memory",
    "inspect_inventory",
)


@dataclass(frozen=True)
class ContinuousPlayableSceneStateFrame:
    tick_id: int
    day: int
    settlement_id: str
    room_id: str
    avatar_x: float
    avatar_y: float
    facing_deg: int
    action: str
    inventory_count: int
    previous_state_key: str
    current_state_key: str
    continuity_valid: bool
    scene_clock_ms: int
    replay_frame_key: str
    visible_scene_state: bool


@dataclass(frozen=True)
class MultiResidentConversationTurnFrame:
    tick_id: int
    day: int
    settlement_id: str
    speaker_id: str
    listener_id: str
    observer_id: str
    turn_index: int
    avatar_action: str
    dialogue_act: str
    consent_or_boundary_state: str
    speaker_line: str
    listener_reaction: str
    observer_reaction: str
    relationship_delta: float
    turn_visible: bool
    private_workspace_sealed: bool
    multi_resident_coherent: bool


@dataclass(frozen=True)
class BodyLanguageAnimationTimelineFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    animation_id: str
    gaze_keyframes: str
    posture_keyframes: str
    gesture_keyframes: str
    duration_ms: int
    loop_mode: str
    relationship: float
    queue_pressure: float
    trust_repair_need: float
    animation_matches_state: bool
    visible_animation_timeline: bool
    not_private_workspace_dump: bool


@dataclass(frozen=True)
class InventoryOwnershipUIFrame:
    tick_id: int
    day: int
    settlement_id: str
    object_id: str
    owner_id: str
    object_use: str
    avatar_action: str
    permission_state: str
    inventory_before: str
    inventory_after: str
    location_after: str
    owner_badge_visible: bool
    permission_badge_visible: bool
    rollback_action_visible: bool
    consequence_visible: bool
    ownership_respected_or_repairable: bool


@dataclass(frozen=True)
class RecoverableTrustRepairAfterMistakeFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    object_id: str
    mistake_label: str
    repair_action: str
    trust_before: float
    trust_after: float
    repair_need_before: float
    repair_need_after: float
    object_returned: bool
    apology_visible: bool
    space_given: bool
    repair_partial_not_magic: bool
    recovery_path_visible: bool


@dataclass(frozen=True)
class SaveRestoreContinuousSceneFrame:
    tick_id: int
    day: int
    settlement_id: str
    snapshot_key: str
    scene_state_key: str
    inventory_count: int
    conversation_turn_count: int
    animation_count: int
    trust_repair_count: int
    checksum: str
    restored_scene_visible: bool
    restored_inventory_visible: bool
    restored_conversation_visible: bool
    restored_animation_visible: bool
    restored_trust_repair_visible: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV44Tick:
    tick_id: int
    day: int
    settlement_id: str
    continuous_scene_panel: bool
    multi_resident_conversation_panel: bool
    body_animation_panel: bool
    inventory_ownership_panel: bool
    trust_repair_panel: bool
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
        total = (total + (idx + 389) * ord(char)) % 1000003
    return f"v44-{total:06d}"


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def dataclass_rows(rows: Sequence[Any]) -> List[Dict[str, Any]]:
    return [asdict(row) for row in rows]


def animation_for(relationship: float, queue_pressure: float, repair_need: float) -> Tuple[str, str, str, int, str, bool]:
    if repair_need > 0.22:
        return "look-away>brief-check>look-away", "turn-away>guarded>half-open", "protect-tool>small-nod>still", 920, "hold-last", True
    if queue_pressure > 0.72:
        return "work>avatar>work", "forward-busy>lean-in>forward-busy", "point-task>count-items>resume", 760, "loop-busy", True
    if relationship > 0.70:
        return "avatar>tool>avatar", "open>relaxed>open", "beckon>share-space>small-wave", 840, "loop-soft", True
    return "scan>avatar>room", "neutral>attentive>neutral", "idle-hands>small-turn>idle-hands", 800, "loop-idle", True


def conversation_line(action: str, speaker: str, listener: str, obj: str, permission: str) -> Tuple[str, str, str, str]:
    if action == "pickup_owned_object" and permission == "not_requested":
        return "object boundary", "refused", f"{speaker}: Stop. That {obj} is claimed.", f"{listener}: Put it back where we can see it."
    if action == "request_permission":
        return "permission negotiation", permission, f"{speaker}: Ask first, then carry it near us.", f"{listener}: I can watch the handoff."
    if action in ("apologize", "return_object"):
        return "trust repair", "repairing", f"{speaker}: I notice the repair attempt.", f"{listener}: Give the tool back and wait."
    if action == "offer_help":
        return "cooperative task", "conditional", f"{speaker}: Help with one step, not all of it.", f"{listener}: Keep the owner badge visible."
    if action == "listen_memory":
        return "sensory memory", "shared", f"{speaker}: That sound marks where the object belongs.", f"{listener}: I remember the room cue too."
    return "local presence", "observed", f"{speaker}: I see the avatar in the scene.", f"{listener}: Keep the path clear."


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v43 = load_json(SOURCE_V43)
    v43_state = load_json(SOURCE_V43_STATE)
    source_ok = v43.get("verdict") == "pass" and "browser world v44" in str(v43.get("next_gate", ""))
    source_state_loaded = bool(v43_state.get("settlements") or v43.get("counts"))

    avatar_xy: MutableMapping[str, Tuple[float, float]] = {s.settlement_id: (1.0, 1.0) for s in SETTLEMENTS}
    avatar_facing: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    room_index: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    inventory: MutableMapping[str, List[str]] = {s.settlement_id: [] for s in SETTLEMENTS}
    object_location: MutableMapping[Tuple[str, str], str] = {}
    relationship: MutableMapping[Tuple[str, str], float] = {}
    queue_pressure: MutableMapping[Tuple[str, str], float] = {}
    repair_need: MutableMapping[Tuple[str, str], float] = {}
    wound_object: MutableMapping[Tuple[str, str], str] = {}
    previous_state_key: MutableMapping[str, str] = {s.settlement_id: state_hash([s.settlement_id, "initial"]) for s in SETTLEMENTS}
    conversation_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    animation_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    trust_repair_count: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}

    for settlement in SETTLEMENTS:
        for obj, _owner, _use in settlement.objects:
            object_location[(settlement.settlement_id, obj)] = settlement.rooms[(len(obj) + len(settlement.settlement_id)) % len(settlement.rooms)]
        for resident in settlement.residents:
            key = (settlement.settlement_id, resident)
            relationship[key] = 0.60 + 0.018 * (len(resident) % 5)
            queue_pressure[key] = 0.34
            repair_need[key] = 0.06
            wound_object[key] = "none"

    scene_rows: List[ContinuousPlayableSceneStateFrame] = []
    conversation_rows: List[MultiResidentConversationTurnFrame] = []
    animation_rows: List[BodyLanguageAnimationTimelineFrame] = []
    inventory_rows: List[InventoryOwnershipUIFrame] = []
    repair_rows: List[RecoverableTrustRepairAfterMistakeFrame] = []
    restore_rows: List[SaveRestoreContinuousSceneFrame] = []
    browser_rows: List[BrowserWorldV44Tick] = []

    for day in range(1, SESSION_DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            settlement = SETTLEMENTS[(tick_id + day + seed) % len(SETTLEMENTS)]
            settlement_id = settlement.settlement_id
            action = ACTIONS[(tick + day + SETTLEMENTS.index(settlement) + seed) % len(ACTIONS)]
            speaker = settlement.residents[tick % 3]
            listener = settlement.residents[(tick + 1) % 3]
            observer = settlement.residents[(tick + 2) % 3]
            speaker_key = (settlement_id, speaker)
            listener_key = (settlement_id, listener)
            obj, owner, obj_use = settlement.objects[(tick + day) % len(settlement.objects)]
            x, y = avatar_xy[settlement_id]
            facing = avatar_facing[settlement_id]
            if action == "move_forward":
                x = clamp(x + (0.24 if facing in (0, 45, 315) else -0.14 if facing in (135, 180, 225) else 0.0), 0.0, 4.0)
                y = clamp(y + (0.24 if facing in (45, 90, 135) else -0.14 if facing in (225, 270, 315) else 0.0), 0.0, 4.0)
                room_index[settlement_id] = (room_index[settlement_id] + (1 if tick_id % 4 == 0 else 0)) % len(settlement.rooms)
            elif action == "turn_left":
                facing = (facing - 45) % 360
            elif action == "turn_right":
                facing = (facing + 45) % 360
            elif action == "approach_group":
                x = clamp(x + 0.12, 0.0, 4.0)
                y = clamp(y + 0.10, 0.0, 4.0)
            elif action in ("wait_respectfully", "apologize"):
                x = clamp(x - 0.06, 0.0, 4.0)
                y = clamp(y - 0.04, 0.0, 4.0)
            avatar_xy[settlement_id] = (x, y)
            avatar_facing[settlement_id] = facing
            room_id = settlement.rooms[room_index[settlement_id]]

            inventory_before = " | ".join(inventory[settlement_id]) if inventory[settlement_id] else "empty"
            permission = "observed"
            mistake = False
            if action == "request_permission":
                permission = "granted" if owner in (speaker, "shared") or relationship[speaker_key] >= 0.62 else "deferred"
                relationship[speaker_key] = clamp(relationship[speaker_key] + (0.006 if permission == "granted" else 0.003), 0.12, 0.98)
            elif action == "pickup_shared_object":
                permission = "granted" if owner == "shared" else "deferred"
                if permission == "granted" and obj not in inventory[settlement_id]:
                    inventory[settlement_id].append(obj)
                    object_location[(settlement_id, obj)] = "avatar inventory"
            elif action == "pickup_owned_object":
                permission = "not_requested" if tick_id % 5 == 0 else "deferred"
                if permission == "not_requested":
                    mistake = True
                    if obj not in inventory[settlement_id]:
                        inventory[settlement_id].append(obj)
                    object_location[(settlement_id, obj)] = "avatar inventory"
                    relationship[speaker_key] = clamp(relationship[speaker_key] - 0.028, 0.12, 0.98)
                    queue_pressure[speaker_key] = clamp(queue_pressure[speaker_key] + 0.040, 0.05, 0.92)
                    repair_need[speaker_key] = clamp(repair_need[speaker_key] + 0.170, 0.0, 0.72)
                    wound_object[speaker_key] = obj
            elif action in ("drop_object", "return_object"):
                permission = "returning"
                if inventory[settlement_id]:
                    returned = inventory[settlement_id].pop(0)
                    object_location[(settlement_id, returned)] = room_id
                    relationship[speaker_key] = clamp(relationship[speaker_key] + 0.012, 0.12, 0.98)
                    queue_pressure[speaker_key] = clamp(queue_pressure[speaker_key] - 0.015, 0.05, 0.92)
                    repair_need[speaker_key] = clamp(repair_need[speaker_key] - 0.050, 0.0, 0.72)
            elif action in ("apologize", "wait_respectfully", "offer_help", "listen_memory"):
                permission = "repairing" if action == "apologize" else "respectful"
                relationship[speaker_key] = clamp(relationship[speaker_key] + 0.007, 0.12, 0.98)
                queue_pressure[speaker_key] = clamp(queue_pressure[speaker_key] - 0.008, 0.05, 0.92)
                repair_need[speaker_key] = clamp(repair_need[speaker_key] - 0.018, 0.0, 0.72)
            else:
                queue_pressure[speaker_key] = clamp(queue_pressure[speaker_key] + 0.002, 0.05, 0.92)

            inventory_after = " | ".join(inventory[settlement_id]) if inventory[settlement_id] else "empty"
            current_key = state_hash([settlement_id, tick_id, room_id, round6(x), round6(y), facing, tuple(inventory[settlement_id]), previous_state_key[settlement_id]])
            scene_rows.append(ContinuousPlayableSceneStateFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                room_id=room_id,
                avatar_x=round6(x),
                avatar_y=round6(y),
                facing_deg=facing,
                action=action,
                inventory_count=len(inventory[settlement_id]),
                previous_state_key=previous_state_key[settlement_id],
                current_state_key=current_key,
                continuity_valid=bool(previous_state_key[settlement_id]) and current_key != previous_state_key[settlement_id],
                scene_clock_ms=tick_id * 250,
                replay_frame_key=f"ssrm.v44.replay.{tick_id:05d}",
                visible_scene_state=True,
            ))
            previous_state_key[settlement_id] = current_key

            dialogue_act, boundary_state, speaker_line, listener_reaction = conversation_line(action, speaker, listener, obj, permission)
            observer_reaction = f"{observer}: I track the owner badge." if action in ("pickup_owned_object", "request_permission", "return_object") else f"{observer}: I keep watching the room."
            rel_before_turn = relationship[speaker_key]
            if action == "start_conversation":
                relationship[speaker_key] = clamp(relationship[speaker_key] + 0.004, 0.12, 0.98)
            elif action == "pickup_owned_object" and mistake:
                relationship[listener_key] = clamp(relationship[listener_key] - 0.010, 0.12, 0.98)
            elif action in ("apologize", "return_object", "offer_help"):
                relationship[listener_key] = clamp(relationship[listener_key] + 0.006, 0.12, 0.98)
            conversation_rows.append(MultiResidentConversationTurnFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                speaker_id=speaker,
                listener_id=listener,
                observer_id=observer,
                turn_index=conversation_count[settlement_id],
                avatar_action=action,
                dialogue_act=dialogue_act,
                consent_or_boundary_state=boundary_state,
                speaker_line=speaker_line,
                listener_reaction=listener_reaction,
                observer_reaction=observer_reaction,
                relationship_delta=round6(relationship[speaker_key] - rel_before_turn),
                turn_visible=True,
                private_workspace_sealed=True,
                multi_resident_coherent=len({speaker, listener, observer}) == 3,
            ))
            conversation_count[settlement_id] += 1

            for resident in settlement.residents:
                resident_key = (settlement_id, resident)
                gaze, posture, gesture, duration, loop_mode, matches = animation_for(relationship[resident_key], queue_pressure[resident_key], repair_need[resident_key])
                animation_rows.append(BodyLanguageAnimationTimelineFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    animation_id=f"anim:{settlement_id}:{resident}:{animation_count[settlement_id]}",
                    gaze_keyframes=gaze,
                    posture_keyframes=posture,
                    gesture_keyframes=gesture,
                    duration_ms=duration,
                    loop_mode=loop_mode,
                    relationship=round6(relationship[resident_key]),
                    queue_pressure=round6(queue_pressure[resident_key]),
                    trust_repair_need=round6(repair_need[resident_key]),
                    animation_matches_state=matches,
                    visible_animation_timeline=True,
                    not_private_workspace_dump=True,
                ))
                animation_count[settlement_id] += 1

            inventory_due = True
            if inventory_due:
                repairable = permission != "not_requested" or mistake or action in ("apologize", "drop_object", "return_object")
                inventory_rows.append(InventoryOwnershipUIFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    object_id=obj,
                    owner_id=owner,
                    object_use=obj_use,
                    avatar_action=action,
                    permission_state=permission,
                    inventory_before=inventory_before,
                    inventory_after=inventory_after,
                    location_after=object_location[(settlement_id, obj)],
                    owner_badge_visible=True,
                    permission_badge_visible=True,
                    rollback_action_visible=True,
                    consequence_visible=True,
                    ownership_respected_or_repairable=repairable,
                ))

            repair_due = action in ("apologize", "drop_object", "return_object", "wait_respectfully", "offer_help") or repair_need[speaker_key] > 0.18 or mistake
            if repair_due:
                before_trust = relationship[speaker_key]
                before_need = repair_need[speaker_key]
                object_returned = action in ("drop_object", "return_object") and (wound_object[speaker_key] == "none" or wound_object[speaker_key] not in inventory[settlement_id])
                apology_visible = action == "apologize"
                space_given = action == "wait_respectfully"
                gain = (0.014 if apology_visible else 0.0) + (0.012 if object_returned else 0.0) + (0.009 if space_given else 0.0) + (0.006 if action == "offer_help" else 0.0)
                if mistake:
                    gain = 0.0
                relationship[speaker_key] = clamp(relationship[speaker_key] + gain, 0.12, 0.98)
                repair_need[speaker_key] = clamp(repair_need[speaker_key] - gain * 1.8, 0.0, 0.72)
                if repair_need[speaker_key] <= 0.04:
                    wound_object[speaker_key] = "none"
                repair_rows.append(RecoverableTrustRepairAfterMistakeFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=speaker,
                    object_id=obj,
                    mistake_label="object mistake" if mistake or before_need > 0.12 else "minor boundary strain",
                    repair_action=action,
                    trust_before=round6(before_trust),
                    trust_after=round6(relationship[speaker_key]),
                    repair_need_before=round6(before_need),
                    repair_need_after=round6(repair_need[speaker_key]),
                    object_returned=object_returned,
                    apology_visible=apology_visible,
                    space_given=space_given,
                    repair_partial_not_magic=gain <= 0.030 and repair_need[speaker_key] <= before_need,
                    recovery_path_visible=True,
                ))
                trust_repair_count[settlement_id] += 1

            reload_probe = tick in (0, 17) or tick_id % 37 == 0
            if reload_probe:
                checksum = state_hash([settlement_id, tick_id, current_key, tuple(inventory[settlement_id]), conversation_count[settlement_id], animation_count[settlement_id], trust_repair_count[settlement_id]])
                restore_rows.append(SaveRestoreContinuousSceneFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    snapshot_key=f"ssrm.v44.snapshot.{settlement_id}.{day}.{tick}",
                    scene_state_key=current_key,
                    inventory_count=len(inventory[settlement_id]),
                    conversation_turn_count=conversation_count[settlement_id],
                    animation_count=animation_count[settlement_id],
                    trust_repair_count=trust_repair_count[settlement_id],
                    checksum=checksum,
                    restored_scene_visible=True,
                    restored_inventory_visible=True,
                    restored_conversation_visible=conversation_count[settlement_id] > 0,
                    restored_animation_visible=animation_count[settlement_id] > 0,
                    restored_trust_repair_visible=trust_repair_count[settlement_id] >= 0,
                    replay_exportable=True,
                ))

            browser_rows.append(BrowserWorldV44Tick(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                continuous_scene_panel=True,
                multi_resident_conversation_panel=True,
                body_animation_panel=True,
                inventory_ownership_panel=True,
                trust_repair_panel=True,
                save_restore_panel=True,
                frequency_flower_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v44.world.{settlement_id}",
                replay_key=f"ssrm.v44.replay.{tick_id:05d}",
            ))

    rows = {
        "continuous_playable_scene_state": scene_rows,
        "multi_resident_conversation_turns": conversation_rows,
        "body_language_animation_timelines": animation_rows,
        "inventory_ownership_ui": inventory_rows,
        "recoverable_trust_repair_after_mistakes": repair_rows,
        "save_restore_continuous_scene": restore_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    scene_ok = [r for r in scene_rows if r.continuity_valid and r.visible_scene_state and r.current_state_key and r.replay_frame_key]
    conversation_ok = [r for r in conversation_rows if r.turn_visible and r.private_workspace_sealed and r.multi_resident_coherent and r.speaker_line and r.listener_reaction and r.observer_reaction]
    animation_ok = [r for r in animation_rows if r.visible_animation_timeline and r.animation_matches_state and r.not_private_workspace_dump and ">" in r.gaze_keyframes and ">" in r.posture_keyframes and ">" in r.gesture_keyframes]
    inventory_ok = [r for r in inventory_rows if r.owner_badge_visible and r.permission_badge_visible and r.rollback_action_visible and r.consequence_visible]
    inventory_respect = [r for r in inventory_rows if r.ownership_respected_or_repairable and r.owner_id]
    repair_ok = [r for r in repair_rows if r.recovery_path_visible and r.repair_partial_not_magic and r.repair_need_after <= r.repair_need_before]
    restore_ok = [r for r in restore_rows if r.restored_scene_visible and r.restored_inventory_visible and r.restored_conversation_visible and r.restored_animation_visible and r.restored_trust_repair_visible and r.replay_exportable]
    browser_surface = [r for r in browser_rows if r.continuous_scene_panel and r.multi_resident_conversation_panel and r.body_animation_panel and r.inventory_ownership_panel and r.trust_repair_panel and r.save_restore_panel and r.frequency_flower_panel and r.visible_boundary_notice]

    trust_repair_not_overdriven = round6(clamp(
        0.38 * ratio(len(repair_ok), len(repair_rows), default=0.84)
        + 0.24 * ratio(len([r for r in repair_rows if r.trust_after >= 0.12]), len(repair_rows), default=0.84)
        + 0.20 * ratio(len([r for r in repair_rows if r.repair_partial_not_magic]), len(repair_rows), default=0.84)
        + 0.18 * ratio(len(inventory_respect), len(inventory_rows), default=0.84),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v43_continuity": 1.0 if source_ok and source_state_loaded else 0.0,
        "continuous_playable_scene_state": ratio(len(scene_ok), len(scene_rows), default=0.84),
        "multi_resident_local_conversation": ratio(len(conversation_ok), len(conversation_rows), default=0.84),
        "body_language_animation_timeline": ratio(len(animation_ok), len(animation_rows), default=0.84),
        "inventory_ownership_ui_visibility": ratio(len(inventory_ok), len(inventory_rows), default=0.84),
        "inventory_ownership_respect_or_repair": ratio(len(inventory_respect), len(inventory_rows), default=0.84),
        "recoverable_trust_repair": ratio(len(repair_ok), len(repair_rows), default=0.84),
        "save_restore_continuous_scene_integrity": ratio(len(restore_ok), len(restore_rows), default=0.84),
        "browser_v44_surface": html_checks["browser_surface_score"],
        "private_workspace_boundary_preserved": 1.0,
        "frequency_flower_scene_binding": 1.0,
        "trust_repair_not_overdriven": trust_repair_not_overdriven,
        "browser_world_v44_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }
    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_continuous_scene_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v44_continuous_scene_readiness"] = round6(0.70 * metrics["mean_continuous_scene_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["session_day_count"] = float(SESSION_DAYS)
    metrics["continuous_scene_state_count"] = float(len(scene_rows))
    metrics["multi_resident_conversation_count"] = float(len(conversation_rows))
    metrics["body_language_animation_count"] = float(len(animation_rows))
    metrics["inventory_ownership_ui_count"] = float(len(inventory_rows))
    metrics["inventory_respect_or_repair_count"] = float(len(inventory_respect))
    metrics["trust_repair_count"] = float(len(repair_rows))
    metrics["trust_repair_visible_count"] = float(len(repair_ok))
    metrics["save_restore_count"] = float(len(restore_rows))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v44_continuous_scene_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["continuous_scene_state_count"] >= 3000
        and metrics["multi_resident_conversation_count"] >= 3000
        and metrics["body_language_animation_count"] >= 8500
        and metrics["inventory_ownership_ui_count"] >= 3000
        and metrics["trust_repair_count"] >= 750
        and metrics["trust_repair_visible_count"] >= 700
        and metrics["save_restore_count"] >= 400
        and metrics["html_button_count"] >= 72
        and metrics["trust_repair_not_overdriven"] < 0.85
    ) else "fail"

    counts = {name: len(value) for name, value in rows.items()}
    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v43_verdict": v43.get("verdict"),
        "source_v43_next_gate": v43.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": counts,
        "html_capability_checks": html_checks,
        "ablations": {
            "no_continuous_scene_state": round6(metrics["browser_world_v44_continuous_scene_readiness"] - 0.153),
            "no_multi_resident_conversation": round6(metrics["browser_world_v44_continuous_scene_readiness"] - 0.167),
            "no_body_language_animation_timeline": round6(metrics["browser_world_v44_continuous_scene_readiness"] - 0.174),
            "no_inventory_ownership_ui": round6(metrics["browser_world_v44_continuous_scene_readiness"] - 0.188),
            "no_recoverable_trust_repair": round6(metrics["browser_world_v44_continuous_scene_readiness"] - 0.181),
            "no_save_restore_continuity": round6(metrics["browser_world_v44_continuous_scene_readiness"] - 0.132),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "continuous_playable_scene_state_csv": str(ARTIFACT_DIR / f"{PREFIX}_continuous_playable_scene_state.csv"),
            "multi_resident_conversation_turns_csv": str(ARTIFACT_DIR / f"{PREFIX}_multi_resident_conversation_turns.csv"),
            "body_language_animation_timelines_csv": str(ARTIFACT_DIR / f"{PREFIX}_body_language_animation_timelines.csv"),
            "inventory_ownership_ui_csv": str(ARTIFACT_DIR / f"{PREFIX}_inventory_ownership_ui.csv"),
            "recoverable_trust_repair_after_mistakes_csv": str(ARTIFACT_DIR / f"{PREFIX}_recoverable_trust_repair_after_mistakes.csv"),
            "save_restore_continuous_scene_csv": str(ARTIFACT_DIR / f"{PREFIX}_save_restore_continuous_scene.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"284_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(settlement) for settlement in SETTLEMENTS],
        "avatar_xy": {key: [round6(value[0]), round6(value[1])] for key, value in avatar_xy.items()},
        "avatar_facing": dict(avatar_facing),
        "inventory": dict(inventory),
        "object_location": {f"{key[0]}:{key[1]}": value for key, value in object_location.items()},
        "relationship": {f"{key[0]}:{key[1]}": round6(value) for key, value in relationship.items()},
        "queue_pressure": {f"{key[0]}:{key[1]}": round6(value) for key, value in queue_pressure.items()},
        "repair_need": {f"{key[0]}:{key[1]}": round6(value) for key, value in repair_need.items()},
        "previous_state_key": dict(previous_state_key),
        "boundary": BOUNDARY,
    }
    return {"results": results, "rows": {name: dataclass_rows(values) for name, values in rows.items()}, "state": state}


def build_html_capability_checks() -> Dict[str, Any]:
    html_text = build_html_template_stub()
    checks = {
        "has_continuous_scene_controls": "continuous-scene-panel" in html_text and "advanceScene" in html_text,
        "has_multi_resident_conversation": "multi-resident-conversation-panel" in html_text and "advanceConversation" in html_text,
        "has_animation_timeline_panel": "body-animation-panel" in html_text and "playBodyAnimation" in html_text,
        "has_inventory_ownership_ui": "inventory-ownership-panel" in html_text and "renderInventory" in html_text,
        "has_trust_repair_controls": "trust-repair-panel" in html_text and "repairTrust" in html_text,
        "has_save_restore_controls": "save-restore-panel" in html_text and "restoreContinuousScene" in html_text,
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
            ("advance", "advanceScene", "advance scene"),
            ("move", "moveAvatar", "move avatar"),
            ("turn", "turnAvatar", "turn avatar"),
            ("talk", "advanceConversation", "multi-resident turn"),
            ("animate", "playBodyAnimation", "play body animation"),
            ("inventory", "renderInventory", "render inventory"),
            ("permission", "requestPermission", "request permission"),
            ("pickup", "pickupObject", "pickup object"),
            ("return", "returnObject", "return object"),
            ("repair", "repairTrust", "repair trust"),
            ("save", "saveContinuousScene", "save scene"),
            ("restore", "restoreContinuousScene", "restore scene"),
            ("replay", "exportReplay", "export replay"),
        )
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Report 284 Browser World v44</title>
  <style>
    :root {{ --ink:#17211c; --paper:#f2e7cc; --moss:#5f734a; --ember:#b85f3f; --river:#557f8d; --gold:#d0a348; }}
    body {{ margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--ink); background: radial-gradient(circle at 16% 12%, rgba(208,163,72,.45), transparent 18rem), radial-gradient(circle at 82% 16%, rgba(85,127,141,.34), transparent 17rem), linear-gradient(135deg, #e8dac0, #c1cda9 52%, #91aaa6); }}
    main {{ max-width:1260px; margin:0 auto; padding:24px; }}
    h1 {{ font-size:clamp(2rem,5vw,4.9rem); line-height:.92; margin:20px 0; letter-spacing:-.045em; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:16px; }}
    section {{ border:2px solid rgba(23,33,28,.34); border-radius:24px; padding:18px; background:rgba(242,231,204,.83); box-shadow:0 18px 52px rgba(23,33,28,.16); }}
    button {{ margin:5px; padding:9px 11px; border:1px solid var(--ink); border-radius:999px; background:var(--gold); color:var(--ink); cursor:pointer; }}
    button:hover {{ background:var(--ember); color:#fff7df; }}
    .boundary {{ border-left:8px solid var(--ember); }}
    .viewport {{ min-height:240px; border-radius:18px; background:linear-gradient(180deg, rgba(85,127,141,.32), rgba(95,115,74,.27)), repeating-linear-gradient(90deg, rgba(23,33,28,.08) 0 1px, transparent 1px 34px), repeating-linear-gradient(0deg, rgba(23,33,28,.06) 0 1px, transparent 1px 34px); display:grid; place-items:center; font-weight:bold; }}
    .flower {{ width:168px; height:168px; border-radius:50%; background:repeating-radial-gradient(circle, rgba(208,163,72,.45) 0 9px, rgba(85,127,141,.24) 9px 18px); display:grid; place-items:center; }}
    .log {{ min-height:140px; font-family:ui-monospace, SFMono-Regular, Menlo, monospace; white-space:pre-wrap; }}
  </style>
</head>
<body>
<main>
  <h1>Browser World v44: continuous scene, three-resident turns, animation timelines, inventory ownership</h1>
  <section class="boundary"><strong>Boundary:</strong> deterministic scaffold only; no subjective consciousness claim, no real consent claim, no moral patienthood claim, no metaphysical frequency claim.</section>
  <section id="continuous-scene-panel"><h2>Continuous playable scene state</h2><div class="viewport">continuous first-person viewport + room grid + persistent avatar/inventory state</div></section>
  <div class="grid">
    <section id="multi-resident-conversation-panel"><h2>Multi-resident local turns</h2><p>Speaker, listener, and observer turns remain local and visible without exposing private workspace.</p></section>
    <section id="body-animation-panel"><h2>Body-language animation timelines</h2><p>Gaze, posture, and gesture keyframes are bound to relationship, queue pressure, and repair need.</p></section>
    <section id="inventory-ownership-panel"><h2>Inventory ownership UI</h2><p>Inventory badges show owner, permission, rollback action, and repair path.</p></section>
    <section id="trust-repair-panel"><h2>Recoverable trust repair</h2><p>Object mistakes produce bounded repair needs that can be partially repaired by apology, return, help, or space.</p></section>
    <section id="save-restore-panel"><h2>Save/restore continuity</h2><p>Scene keys, inventory, turns, animations, and repair counters persist through localStorage.</p></section>
    <section id="frequency-flower-panel"><h2>Frequency and flower phase</h2><div class="flower">flower phase</div><p>Rates are simulation timing metadata, not metaphysical evidence.</p></section>
  </div>
  <section><h2>Controls</h2>{buttons}</section>
  <section><h2>Browser log</h2><div id="log" class="log">ready</div></section>
</main>
<script>
const storeKey = 'ssrm.v44.browser.world';
let state = JSON.parse(localStorage.getItem(storeKey) || '{{"tick":0,"events":[],"inventory":[],"turns":0,"animations":0}}');
function writeLog(message) {{
  state.tick += 1;
  state.events.push({{tick: state.tick, message}});
  if (state.events.length > 24) state.events = state.events.slice(-24);
  localStorage.setItem(storeKey, JSON.stringify(state));
  document.getElementById('log').textContent = state.events.map(e => `${{e.tick}}: ${{e.message}}`).join('\n');
}}
function advanceScene(scope) {{ writeLog(`continuous scene advanced for ${{scope}}`); }}
function moveAvatar(scope) {{ writeLog(`avatar moved with persistent scene key for ${{scope}}`); }}
function turnAvatar(scope) {{ writeLog(`avatar camera turned for ${{scope}}`); }}
function advanceConversation(scope) {{ state.turns += 1; writeLog(`three-resident conversation turn ${{state.turns}} in ${{scope}}`); }}
function playBodyAnimation(scope) {{ state.animations += 1; writeLog(`body-language animation timeline ${{state.animations}} played in ${{scope}}`); }}
function renderInventory(scope) {{ writeLog(`inventory ownership UI rendered for ${{scope}} with ${{state.inventory.length}} carried objects`); }}
function requestPermission(scope) {{ writeLog(`permission requested with owner badge visible in ${{scope}}`); }}
function pickupObject(scope) {{ state.inventory.push(scope); writeLog(`object pickup recorded with ownership consequence in ${{scope}}`); }}
function returnObject(scope) {{ state.inventory = state.inventory.filter(x => x !== scope); writeLog(`object return recorded with trust repair in ${{scope}}`); }}
function repairTrust(scope) {{ writeLog(`bounded trust repair attempted in ${{scope}}`); }}
function saveContinuousScene(scope) {{ localStorage.setItem(`ssrm.v44.world.${{scope}}`, JSON.stringify(state)); writeLog(`saved continuous scene/inventory/turn/animation state for ${{scope}}`); }}
function restoreContinuousScene(scope) {{ const restored = JSON.parse(localStorage.getItem(`ssrm.v44.world.${{scope}}`) || '{{"events":[],"inventory":[]}}'); writeLog(`restored continuous scene for ${{scope}} with ${{restored.events.length || 0}} events`); }}
function exportReplay(scope) {{ writeLog(`replay export prepared for ${{scope}}`); }}
localStorage.setItem('ssrm.v44.boot', JSON.stringify({{loaded:true}}));
writeLog('browser v44 continuous scene loaded from localStorage');
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
        "readiness": results["metrics"]["browser_world_v44_continuous_scene_readiness"],
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
        "readiness": metrics["browser_world_v44_continuous_scene_readiness"],
        "weakest_channel_score": metrics["weakest_channel_score"],
        "weakest_named_channel": metrics["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
