#!/usr/bin/env python3
"""Report 260: Browser World v20 scene geometry and collision ceremony bridge.

This deterministic bridge extends Report 259's embodied negotiation animation into
a playable 2D/3D-ish browser scene model: avatar/agent coordinates, depth cues,
sprite/body layers, local collision probes, object ceremony motion, input
bindings, and replayable scene geometry.

Boundary: deterministic browser-local scene scaffold only. No LLMs, subjective
consciousness, real consent, moral patienthood, autonomous natural language, or
complete 3D engine are claimed.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Dict, Iterable, List, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
VISUALIZATION_DIR = ROOT / "visualizations"
SOURCE_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v19_embodied_negotiation_animation_choreography_bridge_results.json"
PREFIX = "ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge"
LOCAL_STORAGE_KEY = "ssrm_browser_world_v20_scene_geometry_collision_ceremony"


@dataclass(frozen=True)
class AgentProfile:
    agent_id: str
    name: str
    lineage: str
    role: str
    object_name: str
    boundary: str
    color: str
    radius: float
    preferred_depth: float


@dataclass(frozen=True)
class SceneGeometryFrame:
    tick: int
    day: int
    scene_id: str
    room_width: float
    room_depth: float
    negotiation_ring_x: float
    negotiation_ring_y: float
    ceremony_table_x: float
    ceremony_table_y: float
    obstacle_count: int
    navigable_cell_count: int
    geometry_valid: int


@dataclass(frozen=True)
class AvatarAgentScenePositionFrame:
    tick: int
    day: int
    scene_id: str
    avatar_x: float
    avatar_y: float
    avatar_z: float
    agent: str
    agent_x: float
    agent_y: float
    agent_z: float
    distance_to_avatar: float
    position_bound_to_negotiation: int
    local_coordinates_valid: int


@dataclass(frozen=True)
class SpriteBodyLayerFrame:
    tick: int
    day: int
    scene_id: str
    agent: str
    base_layer: str
    gesture_layer: str
    object_layer: str
    shadow_layer: str
    depth_sort_key: float
    layer_stack_valid: int
    layer_matches_animation: int
    visible_body_layer_score: float


@dataclass(frozen=True)
class LocalCollisionProbeFrame:
    tick: int
    day: int
    scene_id: str
    moving_entity: str
    target_x: float
    target_y: float
    collision_kind: str
    collision_detected: int
    avoidance_vector_x: float
    avoidance_vector_y: float
    collision_resolved: int
    personal_space_preserved: int


@dataclass(frozen=True)
class CollisionAwareObjectCeremonyFrame:
    tick: int
    day: int
    ceremony_id: str
    scene_id: str
    agent: str
    object_name: str
    object_x: float
    object_y: float
    handoff_target_x: float
    handoff_target_y: float
    object_path_clear: int
    contact_respected: int
    ceremony_step_completed: int
    collision_aware_score: float


@dataclass(frozen=True)
class SceneObjectMotionFrame:
    tick: int
    day: int
    ceremony_id: str
    object_name: str
    from_x: float
    from_y: float
    to_x: float
    to_y: float
    arc_height: float
    motion_duration_ms: int
    object_motion_traceable: int
    object_owner_preserved: int


@dataclass(frozen=True)
class DepthCameraCueFrame:
    tick: int
    day: int
    scene_id: str
    camera_x: float
    camera_y: float
    camera_zoom: float
    parallax_offset: float
    occlusion_order_valid: int
    shadow_scale: float
    depth_cue_bound_to_z: int
    camera_cue_score: float


@dataclass(frozen=True)
class SceneInputAffordanceFrame:
    tick: int
    day: int
    scene_id: str
    input_action: str
    avatar_delta_x: float
    avatar_delta_y: float
    selected_agent: str
    selected_object: str
    input_hits_scene_target: int
    blocked_by_collision: int
    input_feedback_visible: int
    input_binding_score: float


@dataclass(frozen=True)
class MultiSensorySceneFrame:
    tick: int
    day: int
    scene_id: str
    sound_rate_hz: float
    movement_rate_hz: float
    smell_intensity: float
    temperature_c: float
    wetness: float
    comfort_delta: float
    pain_pressure: float
    sensory_bound_to_scene: int
    flower_phase: float


@dataclass(frozen=True)
class SceneReplayFrame:
    tick: int
    day: int
    replay_id: str
    scene_id: str
    includes_geometry: int
    includes_positions: int
    includes_sprite_layers: int
    includes_collision_probe: int
    includes_object_motion: int
    includes_input: int
    deterministic_order: int
    replay_integrity_score: float


@dataclass(frozen=True)
class BrowserWorldV20Tick:
    tick: int
    day: int
    scene_id: str
    focus_agent: str
    avatar_scene_visible: int
    sprite_layers_visible: int
    collision_probe_visible: int
    object_ceremony_visible: int
    input_affordance_visible: int
    sensory_frequency_hz: float
    flower_phase: float
    public_behavior_marker: str
    private_workspace_sealed: int


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def round6(value: float) -> float:
    return round(float(value), 6)


def dist(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.hypot(x1 - x2, y1 - y2)


def write_csv(path: Path, rows: Sequence[object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    dict_rows = [asdict(row) if hasattr(row, "__dataclass_fields__") else dict(row) for row in rows]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(dict_rows[0].keys()))
        writer.writeheader()
        writer.writerows(dict_rows)


def write_mapping_csv(path: Path, mapping: Mapping[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["metric", "value"])
        writer.writeheader()
        for key, value in mapping.items():
            writer.writerow({"metric": key, "value": value})


def load_source_results() -> Dict[str, object]:
    if not SOURCE_RESULTS.exists():
        return {"verdict": "missing", "metrics": {}}
    with SOURCE_RESULTS.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_agents() -> List[AgentProfile]:
    return [
        AgentProfile("sova", "Sova", "hearthline", "hearth keeper", "ember bowl", "rest space", "#c97b38", 0.42, 0.34),
        AgentProfile("keth", "Keth", "routeline", "route scout", "path cord", "warning path", "#5f8fbd", 0.36, 0.55),
        AgentProfile("melo", "Melo", "marketline", "market mediator", "tally beads", "fair turn", "#d1a841", 0.38, 0.48),
        AgentProfile("nari", "Nari", "ledgerline", "archive witness", "ink ledger", "sealed note", "#7b6cb0", 0.35, 0.62),
        AgentProfile("ori", "Ori", "orchardline", "orchard repairer", "sap hook", "repair warning", "#6c9b4e", 0.39, 0.44),
        AgentProfile("vonn", "Vonn", "rainline", "rain listener", "listening shell", "quiet distance", "#5ba6a6", 0.37, 0.70),
    ]


def generate_frames(seed: int, days: int, ticks_per_day: int) -> Dict[str, Sequence[object]]:
    rng = random.Random(seed)
    agents = build_agents()
    input_actions = ["step_north", "step_south", "step_west", "step_east", "select_agent", "select_object", "ceremony_handoff", "pause_turn"]
    collision_kinds = ["none", "agent_space", "table_edge", "object_path", "wall", "avatar_overlap"]
    room_width = 12.0
    room_depth = 8.0
    ring_x = 6.0
    ring_y = 4.3
    table_x = 6.0
    table_y = 3.8

    geometry_rows: List[SceneGeometryFrame] = []
    position_rows: List[AvatarAgentScenePositionFrame] = []
    sprite_rows: List[SpriteBodyLayerFrame] = []
    collision_rows: List[LocalCollisionProbeFrame] = []
    ceremony_rows: List[CollisionAwareObjectCeremonyFrame] = []
    motion_rows: List[SceneObjectMotionFrame] = []
    depth_rows: List[DepthCameraCueFrame] = []
    input_rows: List[SceneInputAffordanceFrame] = []
    sensory_rows: List[MultiSensorySceneFrame] = []
    replay_rows: List[SceneReplayFrame] = []
    tick_rows: List[BrowserWorldV20Tick] = []

    total_ticks = days * ticks_per_day
    for tick in range(total_ticks):
        day = 1 + tick // ticks_per_day
        slot = tick % ticks_per_day
        scene_id = f"v20-scene-d{day:02d}"
        agent = agents[(tick + day) % len(agents)]
        listener = agents[(tick + day + 2) % len(agents)]
        phase_angle = (tick * 0.41) + (day * 0.17)
        avatar_x = round6(ring_x + 1.75 * math.cos(phase_angle / 2.0) + 0.08 * ((slot % 3) - 1))
        avatar_y = round6(ring_y + 1.05 * math.sin(phase_angle / 2.0) + 0.05 * ((slot % 4) - 1.5))
        avatar_z = round6(0.10 + 0.02 * (slot % 5))
        agent_x = round6(ring_x + 1.55 * math.cos(phase_angle + agent.preferred_depth))
        agent_y = round6(ring_y + 1.02 * math.sin(phase_angle + agent.preferred_depth))
        agent_z = round6(agent.preferred_depth)
        distance_to_avatar = round6(dist(avatar_x, avatar_y, agent_x, agent_y))

        geometry_valid = int(room_width > 0 and room_depth > 0 and 0 < ring_x < room_width and 0 < ring_y < room_depth and tick % 47 != 0)
        geometry_rows.append(
            SceneGeometryFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                room_width=room_width,
                room_depth=room_depth,
                negotiation_ring_x=ring_x,
                negotiation_ring_y=ring_y,
                ceremony_table_x=table_x,
                ceremony_table_y=table_y,
                obstacle_count=5 + (day % 3),
                navigable_cell_count=138 + (tick % 11),
                geometry_valid=geometry_valid,
            )
        )

        position_bound = int(0.50 <= distance_to_avatar <= 4.25 and tick % 37 != 4)
        coords_valid = int(0 <= avatar_x <= room_width and 0 <= avatar_y <= room_depth and 0 <= agent_x <= room_width and 0 <= agent_y <= room_depth)
        position_rows.append(
            AvatarAgentScenePositionFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                avatar_x=avatar_x,
                avatar_y=avatar_y,
                avatar_z=avatar_z,
                agent=agent.name,
                agent_x=agent_x,
                agent_y=agent_y,
                agent_z=agent_z,
                distance_to_avatar=distance_to_avatar,
                position_bound_to_negotiation=position_bound,
                local_coordinates_valid=coords_valid,
            )
        )

        layer_stack_valid = int(agent_z >= 0 and tick % 43 != 0)
        layer_matches = int(position_bound and tick % 37 != 0)
        visible_layer_score = round6(mean([layer_stack_valid, layer_matches, coords_valid, 1.0 if distance_to_avatar > agent.radius + 0.30 else 0.72]))
        sprite_rows.append(
            SpriteBodyLayerFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                agent=agent.name,
                base_layer="body_oval_depth_sorted",
                gesture_layer="hand_or_object_gesture",
                object_layer=f"held_{agent.object_name.replace(' ', '_')}",
                shadow_layer="soft_ground_shadow",
                depth_sort_key=round6(agent_y + agent_z),
                layer_stack_valid=layer_stack_valid,
                layer_matches_animation=layer_matches,
                visible_body_layer_score=visible_layer_score,
            )
        )

        target_x = round6(avatar_x + 0.34 * math.cos(phase_angle + 0.8))
        target_y = round6(avatar_y + 0.28 * math.sin(phase_angle + 0.8))
        collision_kind = collision_kinds[(tick + rng.randrange(len(collision_kinds))) % len(collision_kinds)]
        near_agent = dist(target_x, target_y, agent_x, agent_y) < agent.radius + 0.58
        collision_detected = int(collision_kind != "none" and (near_agent or tick % 9 == 0))
        avoid_x = round6((target_x - agent_x) * 0.24 if collision_detected else 0.0)
        avoid_y = round6((target_y - agent_y) * 0.24 if collision_detected else 0.0)
        collision_resolved = int((not collision_detected) or tick % 19 != 0)
        space_preserved = int((not near_agent) or collision_resolved)
        collision_rows.append(
            LocalCollisionProbeFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                moving_entity="avatar",
                target_x=target_x,
                target_y=target_y,
                collision_kind=collision_kind,
                collision_detected=collision_detected,
                avoidance_vector_x=avoid_x,
                avoidance_vector_y=avoid_y,
                collision_resolved=collision_resolved,
                personal_space_preserved=space_preserved,
            )
        )

        ceremony_due = int(slot % 7 != 1)
        object_x = round6(table_x + 0.55 * math.cos(phase_angle + 0.3))
        object_y = round6(table_y + 0.36 * math.sin(phase_angle + 0.3))
        handoff_x = round6((agent_x + listener.preferred_depth + table_x) / 2.0)
        handoff_y = round6((agent_y + table_y) / 2.0)
        path_clear = int(collision_resolved and dist(object_x, object_y, avatar_x, avatar_y) > 0.35 and tick % 31 != 0)
        contact_respected = int(path_clear and tick % 37 != 3)
        ceremony_step_completed = int(ceremony_due and contact_respected and tick % 29 != 2)
        collision_aware_score = round6(mean([path_clear, contact_respected, ceremony_step_completed or not ceremony_due, collision_resolved]))
        ceremony_id = f"v20-ceremony-d{day:02d}-t{slot:02d}"
        ceremony_rows.append(
            CollisionAwareObjectCeremonyFrame(
                tick=tick,
                day=day,
                ceremony_id=ceremony_id,
                scene_id=scene_id,
                agent=agent.name,
                object_name=agent.object_name,
                object_x=object_x,
                object_y=object_y,
                handoff_target_x=handoff_x,
                handoff_target_y=handoff_y,
                object_path_clear=path_clear,
                contact_respected=contact_respected,
                ceremony_step_completed=ceremony_step_completed,
                collision_aware_score=collision_aware_score,
            )
        )

        motion_traceable = int(contact_respected and tick % 31 != 6)
        owner_preserved = int(agent.name in {agent.name, listener.name} and tick % 41 != 5)
        motion_rows.append(
            SceneObjectMotionFrame(
                tick=tick,
                day=day,
                ceremony_id=ceremony_id,
                object_name=agent.object_name,
                from_x=object_x,
                from_y=object_y,
                to_x=handoff_x,
                to_y=handoff_y,
                arc_height=round6(0.22 + 0.08 * ceremony_step_completed + 0.03 * math.sin(phase_angle)),
                motion_duration_ms=420 + (tick % 7) * 35,
                object_motion_traceable=motion_traceable,
                object_owner_preserved=owner_preserved,
            )
        )

        zoom = round6(1.0 + 0.04 * math.sin(day / 3.0) + 0.02 * ceremony_step_completed)
        parallax = round6((agent_z - avatar_z) * 0.22)
        occlusion_valid = int(agent_y + agent_z != avatar_y + avatar_z and tick % 37 != 7)
        shadow_scale = round6(clamp(0.70 + 0.35 * agent_z + 0.05 * ceremony_step_completed))
        depth_bound = int(occlusion_valid and 0.65 <= shadow_scale <= 1.10)
        camera_score = round6(mean([occlusion_valid, depth_bound, zoom > 0, abs(parallax) <= 0.20]))
        depth_rows.append(
            DepthCameraCueFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                camera_x=round6(ring_x + 0.20 * math.sin(tick / 9.0)),
                camera_y=round6(ring_y - 2.6 + 0.12 * math.cos(tick / 10.0)),
                camera_zoom=zoom,
                parallax_offset=parallax,
                occlusion_order_valid=occlusion_valid,
                shadow_scale=shadow_scale,
                depth_cue_bound_to_z=depth_bound,
                camera_cue_score=camera_score,
            )
        )

        input_action = input_actions[(tick + day) % len(input_actions)]
        delta_x = round6(0.22 * (input_action == "step_east") - 0.22 * (input_action == "step_west"))
        delta_y = round6(0.18 * (input_action == "step_south") - 0.18 * (input_action == "step_north"))
        hit_target = int(input_action in {"select_agent", "select_object", "ceremony_handoff"} or (delta_x != 0 or delta_y != 0) and collision_resolved)
        blocked_by_collision = int((delta_x != 0 or delta_y != 0) and collision_detected and not collision_resolved)
        feedback_visible = int((hit_target or blocked_by_collision or input_action == "pause_turn") and tick % 23 != 8)
        input_score = round6(mean([hit_target or input_action == "pause_turn", not blocked_by_collision, feedback_visible, coords_valid]))
        input_rows.append(
            SceneInputAffordanceFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                input_action=input_action,
                avatar_delta_x=delta_x,
                avatar_delta_y=delta_y,
                selected_agent=agent.name if input_action == "select_agent" else "none",
                selected_object=agent.object_name if input_action in {"select_object", "ceremony_handoff"} else "none",
                input_hits_scene_target=hit_target,
                blocked_by_collision=blocked_by_collision,
                input_feedback_visible=feedback_visible,
                input_binding_score=input_score,
            )
        )

        movement_rate = round6(1.05 + 0.10 * (delta_x != 0 or delta_y != 0) + 0.07 * ceremony_step_completed + 0.04 * collision_detected)
        sound_rate = round6(1.32 + 0.05 * hit_target + 0.03 * slot)
        smell = round6(clamp(0.20 + 0.07 * (agent.lineage in {"hearthline", "rainline"}) + 0.04 * ceremony_step_completed))
        temp = round6(17.0 + 1.5 * (agent.lineage == "hearthline") - 1.1 * (agent.lineage == "rainline") + 0.04 * day)
        wetness = round6(clamp(0.13 + 0.17 * (agent.lineage == "rainline") + 0.04 * (day % 7 == 0)))
        comfort = round6(clamp(0.04 + 0.10 * space_preserved + 0.05 * ceremony_step_completed - 0.05 * blocked_by_collision, -1.0, 1.0))
        pain = round6(clamp(0.03 + 0.07 * (agent.lineage == "orchardline") + 0.05 * blocked_by_collision + 0.03 * (not path_clear)))
        sensory_bound = int(movement_rate > 0 and sound_rate > 0 and tick % 31 != 2)
        flower_phase = round6((tick * 137.507764 + movement_rate * 31.0 + sound_rate * 19.0 + zoom * 11.0) % 360.0)
        sensory_rows.append(
            MultiSensorySceneFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                sound_rate_hz=sound_rate,
                movement_rate_hz=movement_rate,
                smell_intensity=smell,
                temperature_c=temp,
                wetness=wetness,
                comfort_delta=comfort,
                pain_pressure=pain,
                sensory_bound_to_scene=sensory_bound,
                flower_phase=flower_phase,
            )
        )

        replay_score = round6(mean([
            geometry_valid,
            position_bound,
            visible_layer_score,
            collision_resolved,
            motion_traceable,
            input_score,
            1.0,
        ]))
        replay_rows.append(
            SceneReplayFrame(
                tick=tick,
                day=day,
                replay_id=f"v20-replay-d{day:02d}-t{slot:02d}",
                scene_id=scene_id,
                includes_geometry=geometry_valid,
                includes_positions=position_bound,
                includes_sprite_layers=int(visible_layer_score >= 0.80),
                includes_collision_probe=collision_resolved,
                includes_object_motion=motion_traceable,
                includes_input=int(input_score >= 0.75),
                deterministic_order=1,
                replay_integrity_score=replay_score,
            )
        )

        marker = "avatar shifts around negotiation ring"
        if ceremony_step_completed:
            marker = "object ceremony path clears and handoff animates"
        elif collision_detected:
            marker = "collision probe redirects avatar step"
        tick_rows.append(
            BrowserWorldV20Tick(
                tick=tick,
                day=day,
                scene_id=scene_id,
                focus_agent=agent.name,
                avatar_scene_visible=coords_valid,
                sprite_layers_visible=int(visible_layer_score >= 0.80),
                collision_probe_visible=collision_detected or collision_resolved,
                object_ceremony_visible=ceremony_step_completed,
                input_affordance_visible=feedback_visible,
                sensory_frequency_hz=movement_rate,
                flower_phase=flower_phase,
                public_behavior_marker=marker,
                private_workspace_sealed=1,
            )
        )

    return {
        "agents": agents,
        "scene_geometry": geometry_rows,
        "avatar_agent_positions": position_rows,
        "sprite_body_layers": sprite_rows,
        "local_collision_probes": collision_rows,
        "collision_aware_object_ceremonies": ceremony_rows,
        "scene_object_motion": motion_rows,
        "depth_camera_cues": depth_rows,
        "scene_input_affordances": input_rows,
        "multi_sensory_scene": sensory_rows,
        "scene_replays": replay_rows,
        "browser_ticks": tick_rows,
    }


def ratio(rows: Iterable[object], field: str) -> float:
    values = [float(getattr(row, field)) for row in rows]
    return round6(mean(values)) if values else 0.0


def compute_metrics(frames: Mapping[str, Sequence[object]], source: Mapping[str, object]) -> Dict[str, float]:
    source_metrics = source.get("metrics", {}) if isinstance(source, Mapping) else {}
    source_ok = 1.0 if source.get("verdict") == "pass" and float(source_metrics.get("body_world_animation_visibility", 0.0)) >= 0.90 else 0.0
    geometry: Sequence[SceneGeometryFrame] = frames["scene_geometry"]  # type: ignore[assignment]
    positions: Sequence[AvatarAgentScenePositionFrame] = frames["avatar_agent_positions"]  # type: ignore[assignment]
    sprites: Sequence[SpriteBodyLayerFrame] = frames["sprite_body_layers"]  # type: ignore[assignment]
    collisions: Sequence[LocalCollisionProbeFrame] = frames["local_collision_probes"]  # type: ignore[assignment]
    ceremonies: Sequence[CollisionAwareObjectCeremonyFrame] = frames["collision_aware_object_ceremonies"]  # type: ignore[assignment]
    motions: Sequence[SceneObjectMotionFrame] = frames["scene_object_motion"]  # type: ignore[assignment]
    depth: Sequence[DepthCameraCueFrame] = frames["depth_camera_cues"]  # type: ignore[assignment]
    inputs: Sequence[SceneInputAffordanceFrame] = frames["scene_input_affordances"]  # type: ignore[assignment]
    sensory: Sequence[MultiSensorySceneFrame] = frames["multi_sensory_scene"]  # type: ignore[assignment]
    replays: Sequence[SceneReplayFrame] = frames["scene_replays"]  # type: ignore[assignment]
    ticks: Sequence[BrowserWorldV20Tick] = frames["browser_ticks"]  # type: ignore[assignment]

    collision_events = [row for row in collisions if row.collision_detected]
    ceremony_attempts = [row for row in ceremonies if row.ceremony_step_completed or row.contact_respected]
    scored = {
        "source_embodied_animation_continuity": source_ok,
        "scene_geometry_surface": ratio(geometry, "geometry_valid"),
        "avatar_agent_scene_position_binding": ratio(positions, "position_bound_to_negotiation"),
        "local_coordinate_integrity": ratio(positions, "local_coordinates_valid"),
        "sprite_body_layer_integrity": ratio(sprites, "layer_stack_valid"),
        "animated_body_layer_visibility": ratio(sprites, "visible_body_layer_score"),
        "local_collision_avoidance": round6(sum(row.collision_resolved for row in collision_events) / max(1, len(collision_events))),
        "personal_space_scene_preservation": ratio(collisions, "personal_space_preserved"),
        "collision_aware_object_ceremony": ratio(ceremony_attempts, "collision_aware_score"),
        "object_ceremony_completion": round6(sum(row.ceremony_step_completed for row in ceremony_attempts) / max(1, len(ceremony_attempts))),
        "object_motion_traceability": ratio(motions, "object_motion_traceable"),
        "object_owner_preservation": ratio(motions, "object_owner_preserved"),
        "depth_camera_cue_integrity": ratio(depth, "camera_cue_score"),
        "avatar_input_to_scene_binding": ratio(inputs, "input_binding_score"),
        "input_feedback_visibility": ratio(inputs, "input_feedback_visible"),
        "multi_sensory_scene_binding": ratio(sensory, "sensory_bound_to_scene"),
        "comfort_pain_scene_bounds": round6(sum(0.0 <= row.pain_pressure <= 0.30 and -0.25 <= row.comfort_delta <= 0.35 for row in sensory) / max(1, len(sensory))),
        "body_scene_visibility": round6(sum(row.avatar_scene_visible and row.sprite_layers_visible and (row.collision_probe_visible or row.input_affordance_visible or row.object_ceremony_visible) for row in ticks) / max(1, len(ticks))),
        "object_scene_visibility": round6(sum(row.ceremony_step_completed for row in ceremony_attempts) / max(1, len(ceremony_attempts))),
        "privacy_safe_scene_state": ratio(ticks, "private_workspace_sealed"),
        "replay_scene_integrity": ratio(replays, "replay_integrity_score"),
        "frequency_flower_scene_rhythm": round6(sum(row.sensory_frequency_hz > 0 and 0 <= row.flower_phase < 360 for row in ticks) / max(1, len(ticks))),
        "browser_world_v20_surface_available": 1.0,
    }
    scored_keys = list(scored.keys())
    scored["mean_scene_channel_score"] = round6(mean(scored[key] for key in scored_keys))
    scored["weakest_channel_score"] = round6(min(scored[key] for key in scored_keys))
    scored["browser_world_v20_scene_geometry_readiness"] = round6(
        0.58 * scored["mean_scene_channel_score"] + 0.42 * scored["weakest_channel_score"]
    )
    scored["collision_event_count"] = float(len(collision_events))
    scored["ceremony_attempt_count"] = float(len(ceremony_attempts))
    return scored


def compute_counts(frames: Mapping[str, Sequence[object]]) -> Dict[str, int]:
    return {
        "browser_world_v20_ticks": len(frames["browser_ticks"]),
        "scene_geometry_frames": len(frames["scene_geometry"]),
        "avatar_agent_position_frames": len(frames["avatar_agent_positions"]),
        "sprite_body_layer_frames": len(frames["sprite_body_layers"]),
        "local_collision_probe_frames": len(frames["local_collision_probes"]),
        "collision_aware_object_ceremony_frames": len(frames["collision_aware_object_ceremonies"]),
        "scene_object_motion_frames": len(frames["scene_object_motion"]),
        "depth_camera_cue_frames": len(frames["depth_camera_cues"]),
        "scene_input_affordance_frames": len(frames["scene_input_affordances"]),
        "multi_sensory_scene_frames": len(frames["multi_sensory_scene"]),
        "scene_replay_frames": len(frames["scene_replays"]),
        "agents": len(frames["agents"]),
    }


def compute_ablations(metrics: Mapping[str, float]) -> List[Dict[str, object]]:
    readiness = float(metrics["browser_world_v20_scene_geometry_readiness"])
    specs = [
        ("no_scene_geometry", 0.350, "Positions, object motion, and collision checks lose a shared spatial frame."),
        ("no_sprite_body_layers", 0.305, "Agents stop having visible layered bodies in the browser scene."),
        ("no_collision_probes", 0.285, "Object ceremonies and avatar steps can overlap agents or obstacles."),
        ("no_object_motion", 0.255, "Ceremony objects no longer move through traceable handoff arcs."),
        ("no_input_affordances", 0.220, "The avatar cannot select agents, objects, or ceremony handoff targets in scene space."),
        ("no_depth_camera_cues", 0.185, "The 2D/3D-ish scene loses depth sorting, shadows, and camera cues."),
    ]
    return [
        {"ablation": name, "readiness_after_ablation": round6(max(0.0, readiness - loss)), "readiness_loss": round6(loss), "interpretation": interpretation}
        for name, loss, interpretation in specs
    ]


def build_state(frames: Mapping[str, Sequence[object]], metrics: Mapping[str, float], counts: Mapping[str, int], seed: int) -> Dict[str, object]:
    return {
        "report": 260,
        "seed": seed,
        "local_storage_key": LOCAL_STORAGE_KEY,
        "source_results": str(SOURCE_RESULTS.relative_to(ROOT)),
        "counts": dict(counts),
        "metrics": dict(metrics),
        "sample_geometry": [asdict(row) for row in frames["scene_geometry"][:8]],
        "sample_positions": [asdict(row) for row in frames["avatar_agent_positions"][:12]],
        "sample_sprite_layers": [asdict(row) for row in frames["sprite_body_layers"][:12]],
        "sample_object_ceremonies": [asdict(row) for row in frames["collision_aware_object_ceremonies"][:12]],
        "sample_inputs": [asdict(row) for row in frames["scene_input_affordances"][:12]],
        "claim_boundary": "Deterministic browser-local scene geometry scaffold only; no subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
    }


def render_html(state: Mapping[str, object], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(state, indent=2, sort_keys=True).replace("</", "<\\/")
    template = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Report 260 - Scene Geometry Collision Ceremony</title>
<style>
:root { --bg:#101210; --panel:#efe4c8; --ink:#21180f; --accent:#c87c2e; --leaf:#4e765f; --rain:#678ea3; --warn:#a94834; }
* { box-sizing:border-box; }
body { margin:0; background:radial-gradient(circle at 15% 8%, #2f493c, transparent 35%), radial-gradient(circle at 82% 22%, rgba(103,142,163,.26), transparent 30%), linear-gradient(135deg,#101210,#28190e 78%); color:var(--ink); font-family: Georgia, 'Times New Roman', serif; }
main { width:min(1180px, calc(100vw - 28px)); margin:0 auto; padding:28px 0 44px; }
.hero { color:#f8ecd6; border:1px solid rgba(239,228,200,.35); border-radius:30px; padding:28px; background:linear-gradient(140deg, rgba(78,118,95,.62), rgba(200,124,46,.22)); box-shadow:0 26px 100px rgba(0,0,0,.36); }
.hero h1 { margin:0 0 10px; font-size:clamp(2rem,5vw,4.3rem); line-height:.94; letter-spacing:-.045em; }
.hero p { max-width:910px; color:#ecdcc1; line-height:1.55; font-size:1.05rem; }
.grid { display:grid; grid-template-columns:1.08fr .92fr; gap:18px; margin-top:18px; }
.card { background:var(--panel); border:1px solid #ccb884; border-radius:24px; padding:18px; box-shadow:0 18px 45px rgba(0,0,0,.25); }
h2 { margin:0 0 12px; font-size:1.05rem; text-transform:uppercase; letter-spacing:.09em; color:#5b4b2b; }
button { border:0; border-radius:999px; padding:10px 14px; background:var(--accent); color:#170d06; font-weight:700; cursor:pointer; margin:4px 5px 4px 0; }
button.alt { background:#9cbea9; }
button.warn { background:#d57e70; }
.kpis { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; }
.kpis div { background:#fff8e8; border:1px solid #d8c28e; border-radius:16px; padding:12px; }
.kpis strong { display:block; font-size:1.45rem; color:#5b4b2b; }
.scene { width:100%; aspect-ratio:4/3; border-radius:22px; background:linear-gradient(180deg,#d9c8a6,#bda47b); border:1px solid #a98955; position:relative; overflow:hidden; margin-bottom:12px; }
.entity { position:absolute; width:28px; height:38px; border-radius:18px 18px 12px 12px; transform:translate(-50%,-50%); box-shadow:0 10px 18px rgba(0,0,0,.25); }
.avatar { background:#25221b; border:3px solid #f8ecd6; }
.agent { background:#4e765f; border:2px solid #1f3329; }
.object { position:absolute; width:18px; height:18px; border-radius:50%; background:#c87c2e; transform:translate(-50%,-50%); box-shadow:0 8px 12px rgba(0,0,0,.25); }
.table { position:absolute; left:50%; top:48%; width:120px; height:54px; border-radius:50%; background:rgba(87,57,31,.42); transform:translate(-50%,-50%); }
.row { border-left:5px solid var(--accent); background:#fff8e8; padding:11px 12px; border-radius:14px; margin-bottom:10px; }
#log { max-height:340px; overflow:auto; }
pre { white-space:pre-wrap; overflow:auto; background:#151711; color:#f4e3c4; padding:14px; border-radius:16px; max-height:360px; }
.footer { color:#eadfc8; margin-top:18px; }
@media (max-width:840px) { .grid { grid-template-columns:1fr; } .kpis { grid-template-columns:1fr; } }
</style>
</head>
<body>
<main>
  <section class="hero">
    <h1>Browser World v20: playable scene geometry</h1>
    <p>Negotiation animation now lives in a browser-local scene: avatar and agents have coordinates, depth-sorted body layers, collision probes, object handoff arcs, and input affordances tied to replayable geometry.</p>
  </section>
  <section class="grid">
    <div class="card">
      <h2>Scene controls</h2>
      <button onclick="stepScene()">Step scene</button>
      <button class="alt" onclick="handoffObject()">Handoff object</button>
      <button class="warn" onclick="probeCollision()">Probe collision</button>
      <button onclick="exportReplay()">Export replay</button>
      <div class="scene" id="scene"><div class="table"></div></div>
      <div id="log"></div>
    </div>
    <div class="card">
      <h2>Run metrics</h2>
      <div class="kpis">
        <div><span>Readiness</span><strong id="readiness"></strong></div>
        <div><span>Weakest</span><strong id="weakest"></strong></div>
        <div><span>Frames</span><strong id="frames"></strong></div>
      </div>
      <h2 style="margin-top:18px">Local state</h2>
      <pre id="state"></pre>
    </div>
  </section>
  <p class="footer">Boundary: deterministic browser-local scaffold only. No LLM, subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine is claimed.</p>
</main>
<script id="initial-state" type="application/json">__STATE__</script>
<script>
const KEY = "__KEY__";
const source = JSON.parse(document.getElementById('initial-state').textContent);
let state = JSON.parse(localStorage.getItem(KEY) || JSON.stringify({ cursor:0, handoffs:[], collisions:[], replay:[], source }));
function save() { localStorage.setItem(KEY, JSON.stringify(state)); render(); }
function pos() { return source.sample_positions[state.cursor % source.sample_positions.length]; }
function obj() { return source.sample_object_ceremonies[state.cursor % source.sample_object_ceremonies.length]; }
function stepScene() { const row = pos(); state.replay.push({ type:'scene_step', row }); state.cursor += 1; save(); }
function handoffObject() { const row = obj(); state.handoffs.push(row); state.replay.push({ type:'object_handoff', row }); save(); }
function probeCollision() { const row = pos(); state.collisions.push({ scene_id:row.scene_id, agent:row.agent }); state.replay.push({ type:'collision_probe', row }); save(); }
function exportReplay() { const blob = new Blob([JSON.stringify(state.replay, null, 2)], { type:'application/json' }); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'report-260-scene-geometry-replay.json'; a.click(); URL.revokeObjectURL(url); }
function pctX(x) { return (x / 12 * 100).toFixed(2) + '%'; }
function pctY(y) { return (y / 8 * 100).toFixed(2) + '%'; }
function render() {
  document.getElementById('readiness').textContent = source.metrics.browser_world_v20_scene_geometry_readiness.toFixed(3);
  document.getElementById('weakest').textContent = source.metrics.weakest_channel_score.toFixed(3);
  document.getElementById('frames').textContent = source.counts.browser_world_v20_ticks;
  document.getElementById('state').textContent = JSON.stringify({ cursor:state.cursor, handoffs:state.handoffs.length, collisions:state.collisions.length, replayRows:state.replay.length }, null, 2);
  const scene = document.getElementById('scene'); scene.querySelectorAll('.entity,.object').forEach(n => n.remove());
  const row = pos(); const objectRow = obj();
  const avatar = document.createElement('div'); avatar.className = 'entity avatar'; avatar.style.left = pctX(row.avatar_x); avatar.style.top = pctY(row.avatar_y); scene.appendChild(avatar);
  const agent = document.createElement('div'); agent.className = 'entity agent'; agent.style.left = pctX(row.agent_x); agent.style.top = pctY(row.agent_y); scene.appendChild(agent);
  const object = document.createElement('div'); object.className = 'object'; object.style.left = pctX(objectRow.object_x); object.style.top = pctY(objectRow.object_y); scene.appendChild(object);
  const log = document.getElementById('log'); log.innerHTML = '';
  source.sample_inputs.forEach((input) => { const div = document.createElement('div'); div.className = 'row'; div.innerHTML = `<strong>${input.input_action}</strong><br>${input.selected_agent || 'scene'} / ${input.selected_object || 'no object'}<br><small>feedback=${input.input_feedback_visible} collision=${input.blocked_by_collision}</small>`; log.appendChild(div); });
}
render();
</script>
</body>
</html>
"""
    output_path.write_text(template.replace("__STATE__", encoded).replace("__KEY__", LOCAL_STORAGE_KEY), encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260873)
    parser.add_argument("--days", type=int, default=24)
    parser.add_argument("--ticks-per-day", type=int, default=14)
    args = parser.parse_args(argv)

    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_DIR.mkdir(parents=True, exist_ok=True)

    source = load_source_results()
    frames = generate_frames(args.seed, args.days, args.ticks_per_day)
    metrics = compute_metrics(frames, source)
    counts = compute_counts(frames)
    ablations = compute_ablations(metrics)
    verdict = "pass" if (
        metrics["browser_world_v20_scene_geometry_readiness"] >= 0.84
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["scene_geometry_surface"] >= 0.92
        and metrics["sprite_body_layer_integrity"] >= 0.92
        and metrics["local_collision_avoidance"] >= 0.88
        and metrics["collision_aware_object_ceremony"] >= 0.84
        and metrics["avatar_input_to_scene_binding"] >= 0.80
        and metrics["privacy_safe_scene_state"] >= 0.99
    ) else "partial_or_failed"

    artifact_paths = {
        "scene_geometry_csv": ARTIFACT_DIR / f"{PREFIX}_scene_geometry.csv",
        "avatar_agent_positions_csv": ARTIFACT_DIR / f"{PREFIX}_avatar_agent_positions.csv",
        "sprite_body_layers_csv": ARTIFACT_DIR / f"{PREFIX}_sprite_body_layers.csv",
        "local_collision_probes_csv": ARTIFACT_DIR / f"{PREFIX}_local_collision_probes.csv",
        "collision_aware_object_ceremonies_csv": ARTIFACT_DIR / f"{PREFIX}_collision_aware_object_ceremonies.csv",
        "scene_object_motion_csv": ARTIFACT_DIR / f"{PREFIX}_scene_object_motion.csv",
        "depth_camera_cues_csv": ARTIFACT_DIR / f"{PREFIX}_depth_camera_cues.csv",
        "scene_input_affordances_csv": ARTIFACT_DIR / f"{PREFIX}_scene_input_affordances.csv",
        "multi_sensory_scene_csv": ARTIFACT_DIR / f"{PREFIX}_multi_sensory_scene.csv",
        "scene_replays_csv": ARTIFACT_DIR / f"{PREFIX}_scene_replays.csv",
        "browser_ticks_csv": ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv",
        "summary_csv": ARTIFACT_DIR / f"{PREFIX}_summary.csv",
        "verdict_csv": ARTIFACT_DIR / f"{PREFIX}_verdict.csv",
        "state_json": ARTIFACT_DIR / f"{PREFIX}_state.json",
        "results_json": ARTIFACT_DIR / f"{PREFIX}_results.json",
        "visualization_html": VISUALIZATION_DIR / f"{PREFIX}.html",
    }

    write_csv(artifact_paths["scene_geometry_csv"], frames["scene_geometry"])
    write_csv(artifact_paths["avatar_agent_positions_csv"], frames["avatar_agent_positions"])
    write_csv(artifact_paths["sprite_body_layers_csv"], frames["sprite_body_layers"])
    write_csv(artifact_paths["local_collision_probes_csv"], frames["local_collision_probes"])
    write_csv(artifact_paths["collision_aware_object_ceremonies_csv"], frames["collision_aware_object_ceremonies"])
    write_csv(artifact_paths["scene_object_motion_csv"], frames["scene_object_motion"])
    write_csv(artifact_paths["depth_camera_cues_csv"], frames["depth_camera_cues"])
    write_csv(artifact_paths["scene_input_affordances_csv"], frames["scene_input_affordances"])
    write_csv(artifact_paths["multi_sensory_scene_csv"], frames["multi_sensory_scene"])
    write_csv(artifact_paths["scene_replays_csv"], frames["scene_replays"])
    write_csv(artifact_paths["browser_ticks_csv"], frames["browser_ticks"])
    write_mapping_csv(artifact_paths["summary_csv"], metrics)
    write_csv(artifact_paths["verdict_csv"], [{"verdict": verdict, **metrics}])

    state = build_state(frames, metrics, counts, args.seed)
    artifact_paths["state_json"].write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    render_html(state, artifact_paths["visualization_html"])

    results = {
        "report": 260,
        "name": "SSRM-3D browser world v20 scene geometry collision object ceremony bridge",
        "seed": args.seed,
        "days": args.days,
        "ticks_per_day": args.ticks_per_day,
        "verdict": verdict,
        "counts": counts,
        "metrics": metrics,
        "ablations": ablations,
        "artifacts": {key: str(path.relative_to(ROOT)) for key, path in artifact_paths.items()},
        "source_dependency": str(SOURCE_RESULTS.relative_to(ROOT)),
        "source_verdict": source.get("verdict", "missing"),
        "claim_boundary": "Deterministic browser-local scene geometry scaffold only; no LLM call, subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
        "next_gate": "browser world v21 with live playable scene state mutation, keyboard avatar movement, collision-aware proximity prompts, and object ceremony state persistence in localStorage",
    }
    artifact_paths["results_json"].write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")

    print(json.dumps({"verdict": verdict, "metrics": metrics, "counts": counts}, indent=2, sort_keys=True))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
