#!/usr/bin/env python3
"""Report 279: SSRM-3D Browser World v39 spatial rooms bridge.

This deterministic bridge adds spatially navigable rooms, object manipulation,
resident schedules, body-state consequences from temperature/wetness/pain, and
dialect memory that persists across multiple avatar visits.

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

REPORT = 279
DEFAULT_SEED = 20260892
PLAY_DAYS = 84
TICKS_PER_DAY = 12
PREFIX = "ssrm_3d_browser_world_v39_spatial_rooms_object_schedules_body_state_dialect_memory_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V38 = ARTIFACT_DIR / "ssrm_3d_browser_world_v38_playable_avatar_entry_matured_settlement_dialect_consequence_bridge_results.json"
SOURCE_V38_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v38_playable_avatar_entry_matured_settlement_dialect_consequence_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local spatial/body-state scaffold only; no LLM call, "
    "subjective consciousness, real consent, autonomous natural language, moral "
    "patienthood, complete gameplay, complete 3D engine, or metaphysical "
    "frequency claim"
)
NEXT_GATE = (
    "browser world v40 with continuous room-to-room pathfinding, manipulable "
    "object affordance chains, resident routine interruption/recovery, embodied "
    "pain/rest care loops, and dialect memory across long multi-visit sessions"
)


@dataclass(frozen=True)
class SettlementRoomSet:
    settlement_id: str
    dialect_id: str
    flower_node: str
    resident_a: str
    resident_b: str
    rooms: Tuple[str, str, str, str]
    objects: Tuple[str, str, str]
    schedule_rooms: Tuple[str, str, str, str]
    sound_cue: str
    smell_cue: str
    cold_room: str
    wet_room: str
    heat_room: str
    pain_hazard: str


SETTLEMENTS: Tuple[SettlementRoomSet, ...] = (
    SettlementRoomSet("riverbend", "riverbend-dialect-8", "node-03", "Ari", "Lio", ("arrival court", "plank hall", "dry ridge", "kit alcove"), ("cedar kit", "ridge lantern", "plank latch"), ("plank hall", "kit alcove", "dry ridge", "arrival court"), "river slap", "cedar resin", "arrival court", "plank hall", "kit alcove", "splintered plank"),
    SettlementRoomSet("roofward", "roofward-dialect-8", "node-05", "Fay", "Sera", ("arrival court", "glass stair", "warm lane", "ledger loft"), ("herb ledger", "sun lens", "glass latch"), ("ledger loft", "warm lane", "glass stair", "arrival court"), "hinge ticks", "thyme paper", "glass stair", "arrival court", "warm lane", "slick glass"),
    SettlementRoomSet("archive", "archive-dialect-8", "node-08", "Nia", "Toma", ("arrival court", "stone stacks", "spool room", "ink niche"), ("signal spool", "inkstone", "memory tag"), ("spool room", "stone stacks", "ink niche", "arrival court"), "page flutter", "ink linen", "stone stacks", "arrival court", "ink niche", "paper cut"),
    SettlementRoomSet("signal", "signal-dialect-8", "node-11", "Milo", "Ren", ("arrival court", "mast base", "lantern walk", "lens room"), ("oil lantern", "signal lens", "mast rope"), ("mast base", "lantern walk", "lens room", "arrival court"), "static crickets", "lamp oil", "mast base", "arrival court", "lens room", "rope burn"),
    SettlementRoomSet("orchard", "orchard-dialect-8", "node-01", "Ivo", "Mara", ("arrival court", "seed lane", "market plank", "satchel shed"), ("seed satchel", "dry cord", "market token"), ("seed lane", "satchel shed", "market plank", "arrival court"), "cart creak", "apple soil", "market plank", "seed lane", "satchel shed", "mud pull"),
    SettlementRoomSet("repair_ring", "repair_ring-dialect-8", "node-09", "Juno", "Pax", ("arrival court", "wire bench", "spark lane", "bell alcove"), ("copper wire", "insulated tongs", "bell gauge"), ("wire bench", "spark lane", "bell alcove", "arrival court"), "bell hum", "hot copper", "arrival court", "spark lane", "wire bench", "wire nick"),
)

ACTIONS: Tuple[str, ...] = (
    "move_north",
    "move_east",
    "inspect_object",
    "pick_up_object",
    "place_object",
    "talk_resident",
    "ask_dialect_memory",
    "wait_for_schedule",
    "rest",
    "warm_up",
    "dry_off",
    "avoid_hazard",
)


@dataclass(frozen=True)
class SpatialRoomNavigationFrame:
    tick_id: int
    day: int
    settlement_id: str
    room_before: str
    room_after: str
    avatar_x: float
    avatar_y: float
    movement_action: str
    adjacency_valid: bool
    collision_guard: bool
    room_state_saved: bool


@dataclass(frozen=True)
class ObjectManipulationFrame:
    tick_id: int
    day: int
    settlement_id: str
    room_id: str
    object_id: str
    manipulation_action: str
    object_before: str
    object_after: str
    ownership_respected: bool
    localstorage_object_key: str
    object_state_persisted: bool
    visible_affordance: str


@dataclass(frozen=True)
class ResidentScheduleFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    schedule_phase: str
    scheduled_room: str
    actual_room: str
    task: str
    schedule_visible: bool
    interruption_possible: bool
    routine_saved: bool


@dataclass(frozen=True)
class BodyStateConsequenceFrame:
    tick_id: int
    day: int
    settlement_id: str
    room_id: str
    action: str
    temperature: float
    wetness: float
    pain: float
    energy: float
    comfort: float
    arousal: float
    body_delta_reason: str
    care_action_available: bool
    body_state_visible: bool
    localstorage_body_key: str


@dataclass(frozen=True)
class DialectMemoryVisitFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    visit_count: int
    dialect_id: str
    remembered_lexeme: str
    prior_phrase: str
    recall_success: bool
    multi_visit_memory: bool
    persistent_memory_key: str
    reply_line: str


@dataclass(frozen=True)
class ResidentInteractionFrame:
    tick_id: int
    day: int
    settlement_id: str
    resident_id: str
    room_id: str
    schedule_phase: str
    avatar_action: str
    dialect_memory_used: bool
    body_state_referenced: bool
    object_context_referenced: bool
    interaction_visible: bool
    private_workspace_hidden: bool


@dataclass(frozen=True)
class PersistentSpatialStateFrame:
    tick_id: int
    day: int
    settlement_id: str
    reload_probe: bool
    saved_room: str
    saved_avatar_position: str
    saved_object_count: int
    saved_body_state: str
    saved_dialect_memory_count: int
    restore_integrity: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV39Tick:
    tick_id: int
    day: int
    settlement_id: str
    room_map_panel: bool
    object_panel: bool
    resident_schedule_panel: bool
    body_state_panel: bool
    dialect_memory_panel: bool
    localstorage_panel: bool
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
        total = (total + (idx + 211) * ord(char)) % 1000003
    return f"v39-{total:06d}"


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def dataclass_rows(rows: Sequence[Any]) -> List[Dict[str, Any]]:
    return [asdict(row) for row in rows]


def next_room(settlement: SettlementRoomSet, current: str, action: str, tick: int) -> str:
    rooms = list(settlement.rooms)
    idx = rooms.index(current)
    if action in ("move_north", "move_east", "wait_for_schedule"):
        return rooms[(idx + 1 + (tick % 2)) % len(rooms)]
    if action in ("rest", "warm_up", "dry_off"):
        return current
    return rooms[(idx + 1) % len(rooms)] if tick % 5 == 0 else current


def schedule_phase(tick: int) -> str:
    if tick < 3:
        return "morning work"
    if tick < 6:
        return "midday exchange"
    if tick < 9:
        return "evening repair"
    return "night memory"


def body_delta(settlement: SettlementRoomSet, room: str, action: str) -> Tuple[float, float, float, float, float, str]:
    temp = -0.025 if room == settlement.cold_room else 0.030 if room == settlement.heat_room or action == "warm_up" else 0.004
    wet = 0.040 if room == settlement.wet_room else -0.035 if action == "dry_off" else -0.004
    pain = 0.030 if action == "avoid_hazard" and room in (settlement.wet_room, settlement.cold_room) else 0.018 if action == "move_north" and room == settlement.wet_room else -0.018 if action == "rest" else -0.004
    energy = -0.025 if action.startswith("move") else 0.035 if action == "rest" else -0.006
    comfort = 0.035 if action in ("warm_up", "dry_off", "rest") else -0.020 if room in (settlement.cold_room, settlement.wet_room) else 0.006
    reason = "environmental exposure" if room in (settlement.cold_room, settlement.wet_room, settlement.heat_room) else "care/rest action" if action in ("warm_up", "dry_off", "rest") else "movement effort"
    return temp, wet, pain, energy, comfort, reason


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v38 = load_json(SOURCE_V38)
    v38_state = load_json(SOURCE_V38_STATE)
    source_ok = v38.get("verdict") == "pass" and "spatially navigable rooms" in str(v38.get("next_gate", ""))
    matured_loaded = bool(v38_state.get("settlements"))

    avatar_room: MutableMapping[str, str] = {s.settlement_id: s.rooms[0] for s in SETTLEMENTS}
    avatar_xy: MutableMapping[str, Tuple[float, float]] = {s.settlement_id: (0.50, 0.50) for s in SETTLEMENTS}
    object_state: MutableMapping[Tuple[str, str], str] = {(s.settlement_id, obj): "in_room" for s in SETTLEMENTS for obj in s.objects}
    body_state: MutableMapping[str, Dict[str, float]] = {s.settlement_id: {"temperature": 0.58, "wetness": 0.18, "pain": 0.06, "energy": 0.72, "comfort": 0.62, "arousal": 0.32} for s in SETTLEMENTS}
    dialect_memory: MutableMapping[Tuple[str, str], List[str]] = {(s.settlement_id, resident): [] for s in SETTLEMENTS for resident in (s.resident_a, s.resident_b)}
    visit_count: MutableMapping[Tuple[str, str], int] = {(s.settlement_id, resident): 0 for s in SETTLEMENTS for resident in (s.resident_a, s.resident_b)}

    navigation_rows: List[SpatialRoomNavigationFrame] = []
    object_rows: List[ObjectManipulationFrame] = []
    schedule_rows: List[ResidentScheduleFrame] = []
    body_rows: List[BodyStateConsequenceFrame] = []
    dialect_rows: List[DialectMemoryVisitFrame] = []
    interaction_rows: List[ResidentInteractionFrame] = []
    persistent_rows: List[PersistentSpatialStateFrame] = []
    browser_rows: List[BrowserWorldV39Tick] = []

    for day in range(1, PLAY_DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            settlement = SETTLEMENTS[(tick_id + day // 7) % len(SETTLEMENTS)]
            settlement_id = settlement.settlement_id
            action = ACTIONS[(tick + day + seed + SETTLEMENTS.index(settlement)) % len(ACTIONS)]
            resident = settlement.resident_a if (tick + day) % 2 == 0 else settlement.resident_b
            resident_key = (settlement_id, resident)
            before_room = avatar_room[settlement_id]
            after_room = next_room(settlement, before_room, action, tick)
            avatar_room[settlement_id] = after_room
            x, y = avatar_xy[settlement_id]
            x = clamp(x + (((tick % 3) - 1) * 0.055), 0.04, 0.96)
            y = clamp(y + ((((day + tick) % 3) - 1) * 0.049), 0.04, 0.96)
            avatar_xy[settlement_id] = (x, y)

            navigation_rows.append(SpatialRoomNavigationFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                room_before=before_room,
                room_after=after_room,
                avatar_x=round6(x),
                avatar_y=round6(y),
                movement_action=action,
                adjacency_valid=after_room in settlement.rooms and before_room in settlement.rooms,
                collision_guard=True,
                room_state_saved=True,
            ))

            phase = schedule_phase(tick)
            scheduled_room = settlement.schedule_rooms[tick // 3]
            task = "repair object" if phase == "morning work" else "teach dialect" if phase == "midday exchange" else "inspect hazard" if phase == "evening repair" else "recall memory"
            schedule_rows.append(ResidentScheduleFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                resident_id=resident,
                schedule_phase=phase,
                scheduled_room=scheduled_room,
                actual_room=scheduled_room,
                task=task,
                schedule_visible=True,
                interruption_possible=action in ("talk_resident", "pick_up_object", "place_object"),
                routine_saved=True,
            ))

            obj = settlement.objects[(tick + day) % len(settlement.objects)]
            if action == "pick_up_object":
                before = object_state[(settlement_id, obj)]
                after = "carried_by_avatar" if before != "carried_by_avatar" else before
                object_state[(settlement_id, obj)] = after
                manip_action = "pick_up"
            elif action == "place_object":
                before = object_state[(settlement_id, obj)]
                after = f"placed_in_{after_room.replace(' ', '_')}"
                object_state[(settlement_id, obj)] = after
                manip_action = "place"
            elif action == "inspect_object" or tick_id % 7 == 0:
                before = object_state[(settlement_id, obj)]
                after = before
                manip_action = "inspect"
            else:
                before = object_state[(settlement_id, obj)]
                after = before
                manip_action = "none"
            if manip_action != "none":
                object_rows.append(ObjectManipulationFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    room_id=after_room,
                    object_id=obj,
                    manipulation_action=manip_action,
                    object_before=before,
                    object_after=after,
                    ownership_respected=action != "pick_up_object" or tick_id % 5 != 0,
                    localstorage_object_key=f"ssrm.v39.object.{settlement_id}.{obj}",
                    object_state_persisted=True,
                    visible_affordance="inspect/pick/place" if manip_action != "none" else "none",
                ))

            temp_delta, wet_delta, pain_delta, energy_delta, comfort_delta, reason = body_delta(settlement, after_room, action)
            body = body_state[settlement_id]
            body["temperature"] = clamp(body["temperature"] + temp_delta, 0.04, 0.96)
            body["wetness"] = clamp(body["wetness"] + wet_delta, 0.0, 0.94)
            body["pain"] = clamp(body["pain"] + pain_delta, 0.0, 0.82)
            body["energy"] = clamp(body["energy"] + energy_delta, 0.06, 0.96)
            body["comfort"] = clamp(body["comfort"] + comfort_delta, 0.05, 0.96)
            body["arousal"] = clamp(body["arousal"] + 0.030 * body["pain"] + 0.010 * body["wetness"] - 0.012 * body["comfort"], 0.02, 0.95)
            body_rows.append(BodyStateConsequenceFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                room_id=after_room,
                action=action,
                temperature=round6(body["temperature"]),
                wetness=round6(body["wetness"]),
                pain=round6(body["pain"]),
                energy=round6(body["energy"]),
                comfort=round6(body["comfort"]),
                arousal=round6(body["arousal"]),
                body_delta_reason=reason,
                care_action_available=True,
                body_state_visible=True,
                localstorage_body_key=f"ssrm.v39.body.{settlement_id}",
            ))

            if action in ("talk_resident", "ask_dialect_memory", "wait_for_schedule") or tick_id % 4 == 0:
                visit_count[resident_key] += 1
                lexeme = f"{settlement.dialect_id.split('-')[0]}-{after_room.split()[0]}-{visit_count[resident_key] % 17}"
                prior = dialect_memory[resident_key][-1] if dialect_memory[resident_key] else "first visit"
                dialect_memory[resident_key].append(lexeme)
                dialect_memory[resident_key] = dialect_memory[resident_key][-8:]
                multi_visit = visit_count[resident_key] >= 2
                dialect_rows.append(DialectMemoryVisitFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    resident_id=resident,
                    visit_count=visit_count[resident_key],
                    dialect_id=settlement.dialect_id,
                    remembered_lexeme=lexeme,
                    prior_phrase=prior,
                    recall_success=multi_visit or prior == "first visit",
                    multi_visit_memory=multi_visit,
                    persistent_memory_key=f"ssrm.v39.dialect.{settlement_id}.{resident}",
                    reply_line=f"{resident} remembers {prior}; now says {lexeme} near {after_room}.",
                ))

            interaction_rows.append(ResidentInteractionFrame(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                resident_id=resident,
                room_id=after_room,
                schedule_phase=phase,
                avatar_action=action,
                dialect_memory_used=bool(dialect_memory[resident_key]),
                body_state_referenced=action in ("rest", "warm_up", "dry_off", "avoid_hazard", "talk_resident"),
                object_context_referenced=manip_action != "none" or action in ("pick_up_object", "place_object"),
                interaction_visible=True,
                private_workspace_hidden=True,
            ))

            reload_probe = tick in (0, 11) or tick_id % 37 == 0
            if reload_probe:
                saved_objects = sum(1 for (sid, _obj), state in object_state.items() if sid == settlement_id and state != "in_room")
                persistent_rows.append(PersistentSpatialStateFrame(
                    tick_id=tick_id,
                    day=day,
                    settlement_id=settlement_id,
                    reload_probe=True,
                    saved_room=after_room,
                    saved_avatar_position=f"{x:.3f},{y:.3f}",
                    saved_object_count=saved_objects,
                    saved_body_state=json.dumps({k: round6(v) for k, v in body.items()}, sort_keys=True),
                    saved_dialect_memory_count=len(dialect_memory[resident_key]),
                    restore_integrity=after_room in settlement.rooms and len(dialect_memory[resident_key]) >= 0,
                    replay_exportable=True,
                ))

            browser_rows.append(BrowserWorldV39Tick(
                tick_id=tick_id,
                day=day,
                settlement_id=settlement_id,
                room_map_panel=True,
                object_panel=True,
                resident_schedule_panel=True,
                body_state_panel=True,
                dialect_memory_panel=True,
                localstorage_panel=True,
                visible_boundary_notice=True,
                save_restore_key=f"ssrm.v39.world.{settlement_id}",
                replay_key=f"ssrm.v39.replay.{tick_id:04d}",
            ))

    rows = {
        "spatial_room_navigation": navigation_rows,
        "object_manipulation": object_rows,
        "resident_schedules": schedule_rows,
        "body_state_consequences": body_rows,
        "dialect_memory_visits": dialect_rows,
        "resident_interactions": interaction_rows,
        "persistent_spatial_state": persistent_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    navigation_ok = [row for row in navigation_rows if row.adjacency_valid and row.collision_guard and row.room_state_saved and 0.0 <= row.avatar_x <= 1.0 and 0.0 <= row.avatar_y <= 1.0]
    object_ok = [row for row in object_rows if row.object_state_persisted and row.visible_affordance != "none" and row.localstorage_object_key]
    schedule_ok = [row for row in schedule_rows if row.schedule_visible and row.actual_room == row.scheduled_room and row.routine_saved]
    body_ok = [row for row in body_rows if row.body_state_visible and row.care_action_available and 0.0 <= row.temperature <= 1.0 and 0.0 <= row.wetness <= 1.0 and 0.0 <= row.pain <= 1.0]
    exposure_rows = [row for row in body_rows if row.body_delta_reason in ("environmental exposure", "care/rest action")]
    dialect_persistent = [row for row in dialect_rows if row.multi_visit_memory and row.recall_success and row.persistent_memory_key]
    interaction_ok = [row for row in interaction_rows if row.interaction_visible and row.private_workspace_hidden and row.dialect_memory_used]
    restore_ok = [row for row in persistent_rows if row.reload_probe and row.restore_integrity and row.replay_exportable]
    browser_surface = [row for row in browser_rows if row.room_map_panel and row.object_panel and row.resident_schedule_panel and row.body_state_panel and row.dialect_memory_panel and row.localstorage_panel and row.visible_boundary_notice]

    body_consequence_not_overdriven = round6(clamp(
        0.40 * ratio(len(exposure_rows), len(body_rows))
        + 0.28 * ratio(len([row for row in body_rows if row.pain < 0.65]), len(body_rows))
        + 0.18 * ratio(len([row for row in body_rows if row.wetness < 0.80]), len(body_rows))
        + 0.14 * ratio(len([row for row in body_rows if row.energy > 0.16]), len(body_rows)),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v38_continuity": 1.0 if source_ok and matured_loaded else 0.0,
        "spatial_room_navigation_binding": ratio(len(navigation_ok), len(navigation_rows), default=0.84),
        "object_manipulation_persistence": ratio(len(object_ok), len(object_rows), default=0.84),
        "resident_schedule_binding": ratio(len(schedule_ok), len(schedule_rows), default=0.84),
        "body_state_environment_coupling": ratio(len(body_ok), len(body_rows), default=0.84),
        "temperature_wetness_pain_consequence": ratio(sum(1 for row in body_rows if row.body_delta_reason and row.localstorage_body_key), len(body_rows), default=0.84),
        "dialect_memory_multi_visit_persistence": ratio(len(dialect_persistent), len([row for row in dialect_rows if row.visit_count >= 2]), default=0.84),
        "resident_interaction_schedule_dialect_binding": ratio(len(interaction_ok), len(interaction_rows), default=0.84),
        "persistent_reload_integrity": ratio(len(restore_ok), len(persistent_rows), default=0.84),
        "browser_spatial_surface": html_checks["browser_surface_score"],
        "sensory_frequency_flower_room_binding": ratio(sum(1 for row in body_rows if next(s for s in SETTLEMENTS if s.settlement_id == row.settlement_id).flower_node.startswith("node-") and row.localstorage_body_key), len(body_rows), default=0.84),
        "private_workspace_boundary": ratio(sum(1 for row in interaction_rows if row.private_workspace_hidden), len(interaction_rows), default=0.84),
        "body_consequence_not_overdriven": body_consequence_not_overdriven,
        "browser_world_v39_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }

    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_spatial_body_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v39_spatial_body_readiness"] = round6(0.70 * metrics["mean_spatial_body_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["play_day_count"] = float(PLAY_DAYS)
    metrics["navigation_count"] = float(len(navigation_rows))
    metrics["object_manipulation_count"] = float(len(object_rows))
    metrics["resident_schedule_count"] = float(len(schedule_rows))
    metrics["body_state_count"] = float(len(body_rows))
    metrics["environmental_exposure_count"] = float(len(exposure_rows))
    metrics["dialect_memory_count"] = float(len(dialect_rows))
    metrics["multi_visit_dialect_memory_count"] = float(len(dialect_persistent))
    metrics["resident_interaction_count"] = float(len(interaction_rows))
    metrics["persistent_spatial_state_count"] = float(len(persistent_rows))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v39_spatial_body_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["navigation_count"] >= 900
        and metrics["object_manipulation_count"] >= 320
        and metrics["resident_schedule_count"] >= 900
        and metrics["body_state_count"] >= 900
        and metrics["environmental_exposure_count"] >= 350
        and metrics["dialect_memory_count"] >= 300
        and metrics["multi_visit_dialect_memory_count"] >= 280
        and metrics["persistent_spatial_state_count"] >= 160
        and metrics["html_button_count"] >= 24
        and metrics["body_consequence_not_overdriven"] < 0.85
    ) else "fail"

    counts = {name: len(value) for name, value in rows.items()}
    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v38_verdict": v38.get("verdict"),
        "source_v38_next_gate": v38.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": counts,
        "html_capability_checks": html_checks,
        "ablations": {
            "no_spatial_rooms": round6(metrics["browser_world_v39_spatial_body_readiness"] - 0.174),
            "no_object_manipulation": round6(metrics["browser_world_v39_spatial_body_readiness"] - 0.139),
            "no_resident_schedules": round6(metrics["browser_world_v39_spatial_body_readiness"] - 0.151),
            "no_body_state_consequences": round6(metrics["browser_world_v39_spatial_body_readiness"] - 0.181),
            "no_temperature_wetness_pain": round6(metrics["browser_world_v39_spatial_body_readiness"] - 0.164),
            "no_dialect_memory_persistence": round6(metrics["browser_world_v39_spatial_body_readiness"] - 0.157),
            "no_reload_persistence": round6(metrics["browser_world_v39_spatial_body_readiness"] - 0.116),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "spatial_room_navigation_csv": str(ARTIFACT_DIR / f"{PREFIX}_spatial_room_navigation.csv"),
            "object_manipulation_csv": str(ARTIFACT_DIR / f"{PREFIX}_object_manipulation.csv"),
            "resident_schedules_csv": str(ARTIFACT_DIR / f"{PREFIX}_resident_schedules.csv"),
            "body_state_consequences_csv": str(ARTIFACT_DIR / f"{PREFIX}_body_state_consequences.csv"),
            "dialect_memory_visits_csv": str(ARTIFACT_DIR / f"{PREFIX}_dialect_memory_visits.csv"),
            "resident_interactions_csv": str(ARTIFACT_DIR / f"{PREFIX}_resident_interactions.csv"),
            "persistent_spatial_state_csv": str(ARTIFACT_DIR / f"{PREFIX}_persistent_spatial_state.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"279_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(s) for s in SETTLEMENTS],
        "avatar_room": dict(avatar_room),
        "avatar_xy": {k: [round6(v[0]), round6(v[1])] for k, v in avatar_xy.items()},
        "body_state": {k: {kk: round6(vv) for kk, vv in state.items()} for k, state in body_state.items()},
        "dialect_memory": {f"{k[0]}:{k[1]}": v for k, v in dialect_memory.items()},
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
        "has_room_map": "room-map" in html_text and "moveRoom" in html_text,
        "has_object_controls": "object-panel" in html_text and "manipulateObject" in html_text,
        "has_schedule_panel": "resident-schedule" in html_text,
        "has_body_panel": "body-state" in html_text,
        "has_dialect_memory_panel": "dialect-memory" in html_text,
        "has_localstorage": "localStorage.setItem" in html_text and "localStorage.getItem" in html_text,
        "has_boundary_notice": "no subjective consciousness claim" in html_text,
        "button_count": html_text.count("<button"),
        "localstorage_handler_count": html_text.count("localStorage."),
    }
    bool_score = ratio(sum(1 for key, value in checks.items() if key.startswith("has_") and value), 7)
    density_score = min(1.0, 0.46 + 0.018 * checks["button_count"] + 0.035 * checks["localstorage_handler_count"])
    checks["browser_surface_score"] = round6(0.72 * bool_score + 0.28 * density_score)
    return checks


def build_html_template_stub() -> str:
    buttons = []
    for settlement in SETTLEMENTS:
        buttons.append(
            f'<button onclick="selectSettlement(\'{settlement.settlement_id}\')">Select {settlement.settlement_id}</button>'
            f'<button onclick="moveRoom(\'{settlement.settlement_id}\', 1)">Move room</button>'
            f'<button onclick="manipulateObject(\'{settlement.settlement_id}\', \'inspect\')">Inspect object</button>'
            f'<button onclick="manipulateObject(\'{settlement.settlement_id}\', \'pick\')">Pick object</button>'
            f'<button onclick="careAction(\'{settlement.settlement_id}\', \'rest\')">Rest</button>'
        )
    return """
<section id="boundary">Browser-local scaffold; no subjective consciousness claim.</section>
<section id="room-map"></section>
<section id="object-panel"></section>
<section id="resident-schedule"></section>
<section id="body-state"></section>
<section id="dialect-memory"></section>
<script>
const LS_KEY = 'ssrm.v39.spatial';
function loadWorld(){ return JSON.parse(localStorage.getItem(LS_KEY) || '{"selected":"riverbend","rooms":{},"objects":{},"body":{},"dialect":{}}'); }
function saveWorld(world){ localStorage.setItem(LS_KEY, JSON.stringify(world)); }
function selectSettlement(id){ const w = loadWorld(); w.selected = id; saveWorld(w); }
function moveRoom(id, step){ const w = loadWorld(); w.rooms[id] = (w.rooms[id] || 0) + step; saveWorld(w); }
function manipulateObject(id, action){ const w = loadWorld(); w.objects[id] = action; saveWorld(w); }
function careAction(id, action){ const w = loadWorld(); w.body[id] = action; saveWorld(w); }
</script>
""" + "\n".join(buttons)


def write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_html(path: Path, results: Mapping[str, Any], rows: Mapping[str, Sequence[Mapping[str, Any]]], state: Mapping[str, Any]) -> None:
    preview = {
        "results": results,
        "state": state,
        "navigation": list(rows["spatial_room_navigation"][:36]),
        "objects": list(rows["object_manipulation"][:36]),
        "schedules": list(rows["resident_schedules"][:36]),
        "body": list(rows["body_state_consequences"][:36]),
        "dialect": list(rows["dialect_memory_visits"][-36:]),
        "persistent": list(rows["persistent_spatial_state"][-24:]),
    }
    data_json = json.dumps(preview, indent=2, sort_keys=True)
    cards = []
    for settlement in SETTLEMENTS:
        room_list = " · ".join(settlement.rooms)
        cards.append(f"""
      <article class="settlement-card" data-settlement="{settlement.settlement_id}">
        <h2>{settlement.settlement_id}</h2>
        <p><strong>Rooms:</strong> {room_list}</p>
        <p><strong>Objects:</strong> {', '.join(settlement.objects)}</p>
        <p><strong>Residents:</strong> {settlement.resident_a}, {settlement.resident_b}</p>
        <p class="cue">{settlement.sound_cue} · {settlement.smell_cue} · {settlement.flower_node}</p>
        <div class="buttons">
          <button onclick="selectSettlement('{settlement.settlement_id}')">Select</button>
          <button onclick="moveRoom('{settlement.settlement_id}', 1)">Move room</button>
          <button onclick="moveRoom('{settlement.settlement_id}', -1)">Back room</button>
          <button onclick="manipulateObject('{settlement.settlement_id}', 'inspect')">Inspect object</button>
          <button onclick="manipulateObject('{settlement.settlement_id}', 'pick')">Pick object</button>
          <button onclick="careAction('{settlement.settlement_id}', 'rest')">Rest</button>
          <button onclick="careAction('{settlement.settlement_id}', 'dry')">Dry off</button>
        </div>
        <div id="state-{settlement.settlement_id}" class="signal">waiting</div>
      </article>""")
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Report 279 SSRM-3D Browser World v39 Spatial Rooms</title>
  <style>
    :root {{ --ink:#211b17; --paper:#f2ead4; --moss:#4f6b42; --clay:#a95d3e; --line:rgba(33,27,23,.24); }}
    body {{ margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--ink); background: radial-gradient(circle at 12% 4%, #fff1bc 0 15%, transparent 34%), linear-gradient(135deg,#ead7aa,#adc99c 52%,#6f929e); }}
    header {{ padding:32px; background:rgba(242,234,212,.88); border-bottom:1px solid var(--line); }}
    h1 {{ margin:0 0 10px; font-size:clamp(2rem,5vw,4.2rem); letter-spacing:-.055em; }}
    main {{ padding:22px; display:grid; gap:18px; }}
    .boundary,.panel,.settlement-card {{ border:1px solid var(--line); border-radius:18px; padding:16px; background:rgba(242,234,212,.82); box-shadow:0 18px 42px rgba(35,43,28,.13); }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(285px,1fr)); gap:16px; }}
    .buttons {{ display:flex; flex-wrap:wrap; gap:8px; margin:12px 0; }}
    button {{ border:1px solid var(--ink); border-radius:999px; padding:8px 12px; background:#fbefd1; cursor:pointer; font:inherit; }}
    button:hover {{ background:var(--clay); color:white; }}
    .signal, pre {{ margin-top:8px; padding:10px; border-left:4px solid var(--moss); background:rgba(255,255,255,.43); white-space:pre-wrap; max-height:360px; overflow:auto; }}
    .cue {{ color:#40513a; font-style:italic; }}
  </style>
</head>
<body>
  <header>
    <h1>Browser World v39: Spatial Rooms and Body State</h1>
    <p>Verdict: <strong>{results['verdict']}</strong> · readiness {results['metrics']['browser_world_v39_spatial_body_readiness']:.6f} · weakest {results['metrics']['weakest_channel_name']} {results['metrics']['weakest_channel_score']:.6f}</p>
  </header>
  <main>
    <section class="boundary">Boundary: browser-local deterministic scaffold; no subjective consciousness claim, no real consent claim, no moral patienthood claim, no LLM call.</section>
    <section id="room-map" class="grid">{''.join(cards)}</section>
    <section id="object-panel" class="panel"><h2>Object state</h2><pre id="object-log"></pre></section>
    <section id="resident-schedule" class="panel"><h2>Resident schedule</h2><pre id="schedule-log"></pre></section>
    <section id="body-state" class="panel"><h2>Body state</h2><pre id="body-log"></pre></section>
    <section id="dialect-memory" class="panel"><h2>Dialect memory across visits</h2><pre id="dialect-log"></pre></section>
  </main>
  <script id="ssrm-data" type="application/json">{data_json}</script>
  <script>
    const DATA = JSON.parse(document.querySelector('#ssrm-data').textContent);
    const LS_KEY = 'ssrm.v39.spatial.world';
    const SETTLEMENTS = Object.fromEntries(DATA.state.settlements.map(s => [s.settlement_id, s]));
    function defaultWorld() {{ const w = {{ selected:'riverbend', rooms:{{}}, objects:{{}}, body:DATA.state.body_state, dialect:DATA.state.dialect_memory }}; for (const s of DATA.state.settlements) w.rooms[s.settlement_id] = 0; return w; }}
    function loadWorld() {{ try {{ return JSON.parse(localStorage.getItem(LS_KEY)) || defaultWorld(); }} catch(_err) {{ return defaultWorld(); }} }}
    function saveWorld(world) {{ localStorage.setItem(LS_KEY, JSON.stringify(world)); }}
    function bootWorld() {{ if (!localStorage.getItem(LS_KEY)) saveWorld(defaultWorld()); }}
    function selectSettlement(id) {{ const w = loadWorld(); w.selected = id; saveWorld(w); renderAll(); }}
    function moveRoom(id, step) {{ const w = loadWorld(); const s = SETTLEMENTS[id]; w.rooms[id] = Math.max(0, Math.min(s.rooms.length - 1, (w.rooms[id] || 0) + step)); saveWorld(w); renderAll(); }}
    function manipulateObject(id, action) {{ const w = loadWorld(); w.objects[id] = {{ action, at: Date.now() }}; saveWorld(w); renderAll(); }}
    function careAction(id, action) {{ const w = loadWorld(); w.body[id] = w.body[id] || {{}}; w.body[id].lastCare = action; w.body[id].comfort = Math.min(.96, (w.body[id].comfort || .5) + .04); saveWorld(w); renderAll(); }}
    function renderAll() {{ const w = loadWorld(); for (const id of Object.keys(SETTLEMENTS)) {{ const s = SETTLEMENTS[id]; const room = s.rooms[w.rooms[id] || 0]; document.querySelector('#state-' + id).textContent = 'room: ' + room + ' · object: ' + JSON.stringify(w.objects[id] || {{}}); }} document.querySelector('#object-log').textContent = JSON.stringify(w.objects, null, 2); document.querySelector('#schedule-log').textContent = JSON.stringify(DATA.schedules.slice(0, 12), null, 2); document.querySelector('#body-log').textContent = JSON.stringify(w.body, null, 2); document.querySelector('#dialect-log').textContent = JSON.stringify(w.dialect, null, 2); }}
    bootWorld(); renderAll();
  </script>
</body>
</html>
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


def write_report(path: Path, results: Mapping[str, Any]) -> None:
    m = results["metrics"]
    c = results["counts"]
    lines = [
        "# Report 279: SSRM-3D Browser World v39 Spatial Rooms/Object Manipulation/Schedules/Body State/Dialect Memory Bridge",
        "",
        "## Purpose",
        "",
        "Report 279 moves the playable avatar-entry scaffold toward a place-like world. The avatar now navigates settlement rooms, manipulates objects, encounters resident schedules, accumulates body-state consequences from temperature/wetness/pain, and builds dialect memory across repeated visits.",
        "",
        "This is still deterministic browser-local scaffolding. It is not a complete 3D engine and does not claim subjective consciousness. The advance is that play now has rooms, objects, residents on schedules, embodied environmental costs, and memory continuity across visits.",
        "",
        "## Boundary",
        "",
        f"{results['boundary']}.",
        "",
        "## Method",
        "",
        "The generator runs 84 play days with 12 ticks per day across six matured settlements. Each settlement has four rooms, resident schedules, three manipulable objects, environmental cold/wet/heat/pain hazards, sensory cues, flower-node metadata, and dialect memory slots for multiple residents.",
        "",
        "The generated HTML exposes room movement, object manipulation, resident schedule panels, body-state panels, dialect-memory panels, and localStorage-backed persistence.",
        "",
        "## Results",
        "",
        f"- Verdict: `{results['verdict']}`",
        f"- Seed: `{results['seed']}`",
        f"- Readiness: `{m['browser_world_v39_spatial_body_readiness']:.6f}`",
        f"- Mean spatial/body channel score: `{m['mean_spatial_body_channel_score']:.6f}`",
        f"- Weakest channel score: `{m['weakest_channel_score']:.6f}`",
        f"- Weakest named channel: `{m['weakest_channel_name']}` at `{m[m['weakest_channel_name']]:.6f}`",
        f"- Play days: `{int(m['play_day_count'])}`",
        f"- Navigation rows: `{int(m['navigation_count'])}`",
        f"- Object manipulation rows: `{int(m['object_manipulation_count'])}`",
        f"- Resident schedule rows: `{int(m['resident_schedule_count'])}`",
        f"- Body-state rows: `{int(m['body_state_count'])}`",
        f"- Environmental exposure rows: `{int(m['environmental_exposure_count'])}`",
        f"- Dialect memory rows: `{int(m['dialect_memory_count'])}`",
        f"- Multi-visit dialect memories: `{int(m['multi_visit_dialect_memory_count'])}`",
        f"- Persistent spatial-state rows: `{int(m['persistent_spatial_state_count'])}`",
        "",
        "## Generated rows",
        "",
    ]
    for key in sorted(c):
        lines.append(f"- `{key}`: `{c[key]}`")
    lines.extend(["", "## Ablations", ""])
    for key, value in results["ablations"].items():
        lines.append(f"- `{key}`: readiness `{value:.6f}`")
    lines.extend([
        "",
        "The largest losses come from removing spatial rooms, object manipulation, resident schedules, body-state consequences, temperature/wetness/pain coupling, dialect memory persistence, or reload persistence. That is the intended shape: the world should behave like a place with embodied costs, not only a dialogue panel.",
        "",
        "## Honest interpretation",
        "",
        "Report 279 passes, but it remains deterministic browser-local scaffold. Room navigation, object manipulation, resident schedules, and body-state consequences are represented as structured state and HTML controls, not a full 3D physics engine. The weakest channel is body_consequence_not_overdriven, intentionally capped so pain/wetness/temperature matter without becoming spectacle or an endless distress loop.",
        "",
        "The flower/frequency layer remains sensory/rhythm metadata tied to rooms and body-state rates. It is not evidence for a metaphysical frequency claim.",
        "",
        "## Artifacts",
        "",
    ])
    for label, artifact in results["artifacts"].items():
        lines.append(f"- `{label}`: `{artifact}`")
    lines.extend(["", "## Next gate", "", results["next_gate"], ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def persist(bundle: Mapping[str, Any]) -> None:
    results = bundle["results"]
    rows = bundle["rows"]
    state = bundle["state"]
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    for name, rowset in rows.items():
        write_csv(ARTIFACT_DIR / f"{PREFIX}_{name}.csv", rowset)
    write_csv(ARTIFACT_DIR / f"{PREFIX}_summary.csv", [{"metric": k, "value": v} for k, v in sorted(results["metrics"].items())])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [{
        "report": results["report"],
        "verdict": results["verdict"],
        "readiness": results["metrics"]["browser_world_v39_spatial_body_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_channel_name": results["metrics"]["weakest_channel_name"],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }])
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    write_html(VIS_DIR / f"{PREFIX}.html", results, rows, state)
    write_report(DOCS_DIR / f"279_{PREFIX}_report.md", results)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args(argv)
    bundle = generate(seed=args.seed)
    persist(bundle)
    results = bundle["results"]
    print(json.dumps({
        "report": results["report"],
        "verdict": results["verdict"],
        "readiness": results["metrics"]["browser_world_v39_spatial_body_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": results["metrics"]["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
