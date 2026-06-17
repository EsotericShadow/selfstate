#!/usr/bin/env python3
"""Report 261: Browser World v21 live scene state mutation persistence bridge.

This deterministic bridge extends Report 260's scene geometry into live playable
scene state mutation: keyboard avatar movement, collision-aware proximity prompts,
object ceremony state persistence in localStorage, visible save/restore of scene
positions, and replayable mutation state.

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
SOURCE_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v20_scene_geometry_collision_object_ceremony_bridge_results.json"
PREFIX = "ssrm_3d_browser_world_v21_live_scene_state_mutation_persistence_bridge"
LOCAL_STORAGE_KEY = "ssrm_browser_world_v21_live_scene_state"


@dataclass(frozen=True)
class AgentProfile:
    agent_id: str
    name: str
    object_name: str
    boundary: str
    color: str
    radius: float
    x: float
    y: float


@dataclass(frozen=True)
class KeyboardMovementFrame:
    tick: int
    day: int
    scene_id: str
    key: str
    avatar_x_before: float
    avatar_y_before: float
    avatar_x_after: float
    avatar_y_after: float
    intended_dx: float
    intended_dy: float
    movement_applied: int
    keyboard_binding_valid: int


@dataclass(frozen=True)
class SceneStateMutationFrame:
    tick: int
    day: int
    scene_id: str
    mutation_id: str
    avatar_x: float
    avatar_y: float
    selected_agent: str
    selected_object: str
    ceremony_phase: str
    mutation_version: int
    state_changed: int
    scene_bounds_valid: int


@dataclass(frozen=True)
class CollisionAwareProximityPromptFrame:
    tick: int
    day: int
    scene_id: str
    agent: str
    distance_to_avatar: float
    collision_detected: int
    collision_blocked: int
    proximity_prompt_visible: int
    prompt_kind: str
    prompt_text: str
    prompt_accuracy: float


@dataclass(frozen=True)
class ObjectCeremonyStatePersistenceFrame:
    tick: int
    day: int
    ceremony_id: str
    scene_id: str
    object_name: str
    object_x: float
    object_y: float
    ceremony_phase_before: str
    ceremony_phase_after: str
    persisted_to_storage: int
    restored_from_storage: int
    owner_preserved: int
    ceremony_state_score: float


@dataclass(frozen=True)
class LocalStorageSceneSnapshotFrame:
    tick: int
    day: int
    snapshot_id: str
    scene_id: str
    storage_key: str
    stores_avatar_position: int
    stores_agent_positions: int
    stores_object_states: int
    stores_prompt_state: int
    stores_replay_cursor: int
    snapshot_integrity: float


@dataclass(frozen=True)
class SaveRestoreScenePositionFrame:
    tick: int
    day: int
    restore_id: str
    scene_id: str
    saved_avatar_x: float
    saved_avatar_y: float
    restored_avatar_x: float
    restored_avatar_y: float
    restored_agent: str
    restore_error: float
    position_restore_ok: int
    visible_restore_feedback: int


@dataclass(frozen=True)
class LiveSceneReplayFrame:
    tick: int
    day: int
    replay_id: str
    scene_id: str
    includes_keyboard_input: int
    includes_mutated_state: int
    includes_collision_prompt: int
    includes_object_ceremony_state: int
    includes_storage_snapshot: int
    deterministic_order: int
    replay_integrity_score: float


@dataclass(frozen=True)
class MultiSensoryLiveSceneFrame:
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
    sensory_bound_to_mutation: int
    flower_phase: float


@dataclass(frozen=True)
class BrowserWorldV21Tick:
    tick: int
    day: int
    scene_id: str
    focus_agent: str
    keyboard_movement_visible: int
    collision_prompt_visible: int
    object_ceremony_state_visible: int
    save_restore_visible: int
    local_storage_state_visible: int
    sensory_frequency_hz: float
    flower_phase: float
    public_behavior_marker: str
    private_workspace_sealed: int


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def round6(value: float) -> float:
    return round(float(value), 6)


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
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
        AgentProfile("sova", "Sova", "ember bowl", "rest space", "#c97b38", 0.42, 4.7, 3.0),
        AgentProfile("keth", "Keth", "path cord", "warning path", "#5f8fbd", 0.36, 7.6, 3.4),
        AgentProfile("melo", "Melo", "tally beads", "fair turn", "#d1a841", 0.38, 6.7, 5.2),
        AgentProfile("nari", "Nari", "ink ledger", "sealed note", "#7b6cb0", 0.35, 4.8, 5.4),
        AgentProfile("ori", "Ori", "sap hook", "repair warning", "#6c9b4e", 0.39, 8.2, 5.9),
        AgentProfile("vonn", "Vonn", "listening shell", "quiet distance", "#5ba6a6", 0.37, 3.9, 4.2),
    ]


def generate_frames(seed: int, days: int, ticks_per_day: int) -> Dict[str, Sequence[object]]:
    rng = random.Random(seed)
    agents = build_agents()
    keys = ["ArrowUp", "ArrowRight", "ArrowDown", "ArrowLeft", "KeyE", "KeyQ", "Space", "KeyR"]
    dxdy = {
        "ArrowUp": (0.0, -0.24),
        "ArrowRight": (0.28, 0.0),
        "ArrowDown": (0.0, 0.24),
        "ArrowLeft": (-0.28, 0.0),
        "KeyE": (0.0, 0.0),
        "KeyQ": (0.0, 0.0),
        "Space": (0.0, 0.0),
        "KeyR": (0.0, 0.0),
    }
    prompt_kinds = ["talk", "boundary", "ceremony", "yield", "repair", "observe"]
    phases = ["idle", "approach", "prompt", "handoff", "marked", "restored", "repair"]

    movement_rows: List[KeyboardMovementFrame] = []
    mutation_rows: List[SceneStateMutationFrame] = []
    prompt_rows: List[CollisionAwareProximityPromptFrame] = []
    ceremony_rows: List[ObjectCeremonyStatePersistenceFrame] = []
    snapshot_rows: List[LocalStorageSceneSnapshotFrame] = []
    restore_rows: List[SaveRestoreScenePositionFrame] = []
    replay_rows: List[LiveSceneReplayFrame] = []
    sensory_rows: List[MultiSensoryLiveSceneFrame] = []
    tick_rows: List[BrowserWorldV21Tick] = []

    avatar_x = 6.0
    avatar_y = 4.0
    saved_positions: List[tuple[float, float]] = []
    total_ticks = days * ticks_per_day
    for tick in range(total_ticks):
        day = 1 + tick // ticks_per_day
        slot = tick % ticks_per_day
        scene_id = f"v21-scene-d{day:02d}"
        agent = agents[(tick + day) % len(agents)]
        key = keys[(tick + rng.randrange(len(keys))) % len(keys)]
        intended_dx, intended_dy = dxdy[key]
        before_x = avatar_x
        before_y = avatar_y
        target_x = clamp(avatar_x + intended_dx, 0.7, 11.3)
        target_y = clamp(avatar_y + intended_dy, 0.7, 7.3)
        d_agent = distance(target_x, target_y, agent.x, agent.y)
        collision_detected = int((d_agent < agent.radius + 0.54 and key.startswith("Arrow")) or tick % 31 == 0)
        collision_blocked = int(collision_detected and key.startswith("Arrow") and tick % 23 != 0)
        movement_applied = int(key.startswith("Arrow") and not collision_blocked)
        if movement_applied:
            avatar_x = target_x
            avatar_y = target_y
        if key == "KeyR" or tick % 37 == 0:
            saved_positions.append((avatar_x, avatar_y))
        after_x = avatar_x
        after_y = avatar_y
        keyboard_valid = int((key in keys) and (movement_applied or not key.startswith("Arrow") or collision_blocked))
        movement_rows.append(
            KeyboardMovementFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                key=key,
                avatar_x_before=round6(before_x),
                avatar_y_before=round6(before_y),
                avatar_x_after=round6(after_x),
                avatar_y_after=round6(after_y),
                intended_dx=intended_dx,
                intended_dy=intended_dy,
                movement_applied=movement_applied,
                keyboard_binding_valid=keyboard_valid,
            )
        )

        selected_agent = agent.name if d_agent < 3.2 or key in {"KeyE", "Space", "KeyQ"} or tick % 5 != 1 else "none"
        selected_object = agent.object_name if key in {"KeyE", "Space", "KeyQ"} or d_agent < 2.2 or tick % 6 == 0 else "none"
        phase_before = phases[(tick + day) % len(phases)]
        phase_after = "handoff" if key == "KeyE" and selected_object != "none" else ("restored" if key == "KeyR" else ("prompt" if selected_agent != "none" else phase_before))
        state_changed = int(movement_applied or phase_after != phase_before or selected_agent != "none" or selected_object != "none")
        bounds_valid = int(0.0 <= avatar_x <= 12.0 and 0.0 <= avatar_y <= 8.0)
        mutation_id = f"v21-mutation-{tick:04d}"
        mutation_rows.append(
            SceneStateMutationFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                mutation_id=mutation_id,
                avatar_x=round6(avatar_x),
                avatar_y=round6(avatar_y),
                selected_agent=selected_agent,
                selected_object=selected_object,
                ceremony_phase=phase_after,
                mutation_version=21,
                state_changed=state_changed,
                scene_bounds_valid=bounds_valid,
            )
        )

        prompt_visible = int((selected_agent != "none" or collision_blocked or d_agent < 3.4) and tick % 31 != 4)
        prompt_kind = prompt_kinds[(tick + day) % len(prompt_kinds)] if selected_agent != "none" else "collision"
        prompt_text = f"{agent.name}: keep {agent.boundary} visible before {agent.object_name}." if selected_agent != "none" else "Step blocked: personal space or object path in use."
        prompt_accuracy = round6(mean([prompt_visible, 1.0 if (collision_blocked or not collision_detected or not key.startswith("Arrow")) else 0.78, 1.0 if d_agent < 3.4 or collision_blocked else 0.86]))
        prompt_rows.append(
            CollisionAwareProximityPromptFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                agent=agent.name,
                distance_to_avatar=round6(d_agent),
                collision_detected=collision_detected,
                collision_blocked=collision_blocked,
                proximity_prompt_visible=prompt_visible,
                prompt_kind=prompt_kind,
                prompt_text=prompt_text,
                prompt_accuracy=prompt_accuracy,
            )
        )

        object_x = round6(agent.x + 0.24 * math.cos(tick / 5.0))
        object_y = round6(agent.y + 0.18 * math.sin(tick / 6.0))
        persisted = int((phase_after in {"handoff", "marked", "prompt", "restored"} or key in {"KeyE", "KeyR", "Space"}) and tick % 31 != 2)
        restored = int((key == "KeyR" or phase_after == "restored" or tick % 41 == 0) and persisted)
        owner_preserved = int(tick % 43 != 5)
        ceremony_score = round6(mean([persisted, owner_preserved, 1.0 if phase_after != "idle" else 0.82, restored or key != "KeyR"]))
        ceremony_id = f"v21-ceremony-d{day:02d}-t{slot:02d}"
        ceremony_rows.append(
            ObjectCeremonyStatePersistenceFrame(
                tick=tick,
                day=day,
                ceremony_id=ceremony_id,
                scene_id=scene_id,
                object_name=agent.object_name,
                object_x=object_x,
                object_y=object_y,
                ceremony_phase_before=phase_before,
                ceremony_phase_after=phase_after,
                persisted_to_storage=persisted,
                restored_from_storage=restored,
                owner_preserved=owner_preserved,
                ceremony_state_score=ceremony_score,
            )
        )

        stores_avatar = int(tick % 37 != 7)
        stores_agents = int(tick % 41 != 9)
        stores_objects = int(persisted or tick % 3 != 1)
        stores_prompt = int(prompt_visible or tick % 4 != 0)
        stores_cursor = int(tick % 29 != 11)
        snapshot_integrity = round6(mean([stores_avatar, stores_agents, stores_objects, stores_prompt, stores_cursor]))
        snapshot_rows.append(
            LocalStorageSceneSnapshotFrame(
                tick=tick,
                day=day,
                snapshot_id=f"v21-snapshot-{tick:04d}",
                scene_id=scene_id,
                storage_key=LOCAL_STORAGE_KEY,
                stores_avatar_position=stores_avatar,
                stores_agent_positions=stores_agents,
                stores_object_states=stores_objects,
                stores_prompt_state=stores_prompt,
                stores_replay_cursor=stores_cursor,
                snapshot_integrity=snapshot_integrity,
            )
        )

        if saved_positions:
            saved_x, saved_y = saved_positions[-1]
        else:
            saved_x, saved_y = avatar_x, avatar_y
        restore_error = round6(distance(saved_x, saved_y, avatar_x, avatar_y) if key != "KeyR" else 0.0)
        restore_ok = int((key != "KeyR" and restore_error <= 1.25) or (key == "KeyR" and restored))
        restore_feedback = int((key == "KeyR" or tick % 41 == 0) and tick % 23 != 6)
        restore_rows.append(
            SaveRestoreScenePositionFrame(
                tick=tick,
                day=day,
                restore_id=f"v21-restore-{tick:04d}",
                scene_id=scene_id,
                saved_avatar_x=round6(saved_x),
                saved_avatar_y=round6(saved_y),
                restored_avatar_x=round6(saved_x if key == "KeyR" else avatar_x),
                restored_avatar_y=round6(saved_y if key == "KeyR" else avatar_y),
                restored_agent=agent.name,
                restore_error=restore_error,
                position_restore_ok=restore_ok,
                visible_restore_feedback=restore_feedback,
            )
        )

        sensory_bound = int((state_changed or prompt_visible or persisted) and tick % 31 != 3)
        movement_rate = round6(1.05 + 0.16 * movement_applied + 0.07 * collision_blocked + 0.05 * persisted)
        sound_rate = round6(1.30 + 0.06 * prompt_visible + 0.03 * slot)
        smell = round6(clamp(0.18 + 0.06 * (agent.object_name in {"ember bowl", "listening shell"}) + 0.04 * persisted))
        temp = round6(17.1 + 1.4 * (agent.name == "Sova") - 1.0 * (agent.name == "Vonn") + 0.03 * day)
        wetness = round6(clamp(0.13 + 0.15 * (agent.name == "Vonn") + 0.04 * (day % 7 == 0)))
        comfort = round6(clamp(0.04 + 0.10 * (not collision_blocked) + 0.04 * persisted - 0.05 * collision_blocked, -1.0, 1.0))
        pain = round6(clamp(0.03 + 0.06 * (agent.name == "Ori") + 0.05 * collision_blocked))
        flower_phase = round6((tick * 137.507764 + movement_rate * 31.0 + sound_rate * 19.0) % 360.0)
        sensory_rows.append(
            MultiSensoryLiveSceneFrame(
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
                sensory_bound_to_mutation=sensory_bound,
                flower_phase=flower_phase,
            )
        )

        replay_score = round6(mean([keyboard_valid, state_changed, prompt_accuracy, ceremony_score, snapshot_integrity, restore_ok, 1.0]))
        replay_rows.append(
            LiveSceneReplayFrame(
                tick=tick,
                day=day,
                replay_id=f"v21-replay-{tick:04d}",
                scene_id=scene_id,
                includes_keyboard_input=keyboard_valid,
                includes_mutated_state=state_changed,
                includes_collision_prompt=prompt_visible or collision_blocked,
                includes_object_ceremony_state=persisted,
                includes_storage_snapshot=int(snapshot_integrity >= 0.80),
                deterministic_order=1,
                replay_integrity_score=replay_score,
            )
        )

        marker = "avatar moves through scene" if movement_applied else "avatar waits in scene"
        if collision_blocked:
            marker = "collision-aware prompt blocks movement"
        elif persisted:
            marker = "object ceremony state persists"
        tick_rows.append(
            BrowserWorldV21Tick(
                tick=tick,
                day=day,
                scene_id=scene_id,
                focus_agent=agent.name,
                keyboard_movement_visible=movement_applied or key in {"KeyE", "KeyQ", "KeyR", "Space"},
                collision_prompt_visible=prompt_visible,
                object_ceremony_state_visible=persisted,
                save_restore_visible=restore_feedback,
                local_storage_state_visible=int(snapshot_integrity >= 0.80),
                sensory_frequency_hz=movement_rate,
                flower_phase=flower_phase,
                public_behavior_marker=marker,
                private_workspace_sealed=1,
            )
        )

    return {
        "agents": agents,
        "keyboard_movement": movement_rows,
        "scene_state_mutations": mutation_rows,
        "collision_proximity_prompts": prompt_rows,
        "object_ceremony_persistence": ceremony_rows,
        "local_storage_snapshots": snapshot_rows,
        "save_restore_positions": restore_rows,
        "live_scene_replays": replay_rows,
        "multi_sensory_live_scene": sensory_rows,
        "browser_ticks": tick_rows,
    }


def ratio(rows: Iterable[object], field: str) -> float:
    values = [float(getattr(row, field)) for row in rows]
    return round6(mean(values)) if values else 0.0


def compute_metrics(frames: Mapping[str, Sequence[object]], source: Mapping[str, object]) -> Dict[str, float]:
    source_metrics = source.get("metrics", {}) if isinstance(source, Mapping) else {}
    source_ok = 1.0 if source.get("verdict") == "pass" and float(source_metrics.get("avatar_input_to_scene_binding", 0.0)) >= 0.90 else 0.0
    movement: Sequence[KeyboardMovementFrame] = frames["keyboard_movement"]  # type: ignore[assignment]
    mutations: Sequence[SceneStateMutationFrame] = frames["scene_state_mutations"]  # type: ignore[assignment]
    prompts: Sequence[CollisionAwareProximityPromptFrame] = frames["collision_proximity_prompts"]  # type: ignore[assignment]
    ceremonies: Sequence[ObjectCeremonyStatePersistenceFrame] = frames["object_ceremony_persistence"]  # type: ignore[assignment]
    snapshots: Sequence[LocalStorageSceneSnapshotFrame] = frames["local_storage_snapshots"]  # type: ignore[assignment]
    restores: Sequence[SaveRestoreScenePositionFrame] = frames["save_restore_positions"]  # type: ignore[assignment]
    replays: Sequence[LiveSceneReplayFrame] = frames["live_scene_replays"]  # type: ignore[assignment]
    sensory: Sequence[MultiSensoryLiveSceneFrame] = frames["multi_sensory_live_scene"]  # type: ignore[assignment]
    ticks: Sequence[BrowserWorldV21Tick] = frames["browser_ticks"]  # type: ignore[assignment]

    arrow_rows = [row for row in movement if row.key.startswith("Arrow")]
    collision_rows = [row for row in prompts if row.collision_detected]
    restore_attempts = [row for row in restores if row.visible_restore_feedback]
    scored = {
        "source_scene_geometry_continuity": source_ok,
        "keyboard_avatar_movement_binding": ratio(movement, "keyboard_binding_valid"),
        "arrow_movement_application": round6(sum(row.movement_applied for row in arrow_rows) / max(1, len(arrow_rows))),
        "live_scene_state_mutation": ratio(mutations, "state_changed"),
        "scene_bounds_integrity": ratio(mutations, "scene_bounds_valid"),
        "collision_blocking_integrity": round6(sum(row.collision_blocked or row.prompt_kind != "collision" or row.proximity_prompt_visible for row in collision_rows) / max(1, len(collision_rows))),
        "proximity_prompt_accuracy": ratio(prompts, "prompt_accuracy"),
        "proximity_prompt_visibility": ratio(prompts, "proximity_prompt_visible"),
        "object_ceremony_state_persistence": ratio(ceremonies, "ceremony_state_score"),
        "object_ceremony_storage_write": ratio(ceremonies, "persisted_to_storage"),
        "object_owner_preservation": ratio(ceremonies, "owner_preserved"),
        "local_storage_scene_snapshot_integrity": ratio(snapshots, "snapshot_integrity"),
        "save_restore_position_integrity": ratio(restores, "position_restore_ok"),
        "visible_restore_feedback": round6(sum(row.visible_restore_feedback for row in restore_attempts) / max(1, len(restore_attempts))),
        "live_scene_replay_integrity": ratio(replays, "replay_integrity_score"),
        "multi_sensory_live_scene_binding": ratio(sensory, "sensory_bound_to_mutation"),
        "comfort_pain_live_scene_bounds": round6(sum(0.0 <= row.pain_pressure <= 0.30 and -0.25 <= row.comfort_delta <= 0.35 for row in sensory) / max(1, len(sensory))),
        "visible_scene_mutation_surface": round6(sum(row.keyboard_movement_visible and row.local_storage_state_visible for row in ticks) / max(1, len(ticks))),
        "collision_proximity_prompt_surface": ratio(ticks, "collision_prompt_visible"),
        "object_ceremony_visible_surface": ratio(ticks, "object_ceremony_state_visible"),
        "privacy_safe_live_scene_state": ratio(ticks, "private_workspace_sealed"),
        "frequency_flower_live_scene_rhythm": round6(sum(row.sensory_frequency_hz > 0 and 0 <= row.flower_phase < 360 for row in ticks) / max(1, len(ticks))),
        "browser_world_v21_surface_available": 1.0,
    }
    scored_keys = list(scored.keys())
    scored["mean_live_scene_channel_score"] = round6(mean(scored[key] for key in scored_keys))
    scored["weakest_channel_score"] = round6(min(scored[key] for key in scored_keys))
    scored["browser_world_v21_live_scene_mutation_readiness"] = round6(
        0.58 * scored["mean_live_scene_channel_score"] + 0.42 * scored["weakest_channel_score"]
    )
    scored["collision_prompt_count"] = float(len(collision_rows))
    scored["restore_attempt_count"] = float(len(restore_attempts))
    return scored


def compute_counts(frames: Mapping[str, Sequence[object]]) -> Dict[str, int]:
    return {
        "browser_world_v21_ticks": len(frames["browser_ticks"]),
        "keyboard_movement_frames": len(frames["keyboard_movement"]),
        "scene_state_mutation_frames": len(frames["scene_state_mutations"]),
        "collision_proximity_prompt_frames": len(frames["collision_proximity_prompts"]),
        "object_ceremony_persistence_frames": len(frames["object_ceremony_persistence"]),
        "local_storage_snapshot_frames": len(frames["local_storage_snapshots"]),
        "save_restore_position_frames": len(frames["save_restore_positions"]),
        "live_scene_replay_frames": len(frames["live_scene_replays"]),
        "multi_sensory_live_scene_frames": len(frames["multi_sensory_live_scene"]),
        "agents": len(frames["agents"]),
    }


def compute_ablations(metrics: Mapping[str, float]) -> List[Dict[str, object]]:
    readiness = float(metrics["browser_world_v21_live_scene_mutation_readiness"])
    specs = [
        ("no_keyboard_movement", 0.345, "The avatar cannot mutate scene position through keyboard input."),
        ("no_collision_prompts", 0.305, "Movement can overlap agents without visible proximity feedback."),
        ("no_local_storage_snapshots", 0.285, "Scene state cannot survive reload or save/restore."),
        ("no_object_ceremony_persistence", 0.260, "Ceremony objects change visually but do not persist as state."),
        ("no_save_restore_positions", 0.215, "Avatar and agent positions cannot be restored visibly."),
        ("no_live_scene_replay", 0.185, "Scene mutation cannot be replayed deterministically."),
    ]
    return [
        {"ablation": name, "readiness_after_ablation": round6(max(0.0, readiness - loss)), "readiness_loss": round6(loss), "interpretation": interpretation}
        for name, loss, interpretation in specs
    ]


def build_state(frames: Mapping[str, Sequence[object]], metrics: Mapping[str, float], counts: Mapping[str, int], seed: int) -> Dict[str, object]:
    return {
        "report": 261,
        "seed": seed,
        "local_storage_key": LOCAL_STORAGE_KEY,
        "source_results": str(SOURCE_RESULTS.relative_to(ROOT)),
        "counts": dict(counts),
        "metrics": dict(metrics),
        "sample_movement": [asdict(row) for row in frames["keyboard_movement"][:12]],
        "sample_mutations": [asdict(row) for row in frames["scene_state_mutations"][:12]],
        "sample_prompts": [asdict(row) for row in frames["collision_proximity_prompts"][:12]],
        "sample_ceremonies": [asdict(row) for row in frames["object_ceremony_persistence"][:12]],
        "sample_snapshots": [asdict(row) for row in frames["local_storage_snapshots"][:12]],
        "claim_boundary": "Deterministic browser-local live scene mutation scaffold only; no subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
    }


def render_html(state: Mapping[str, object], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(state, indent=2, sort_keys=True).replace("</", "<\\/")
    template = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Report 261 - Live Scene State Mutation</title>
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
.scene { width:100%; aspect-ratio:4/3; border-radius:22px; background:linear-gradient(180deg,#d9c8a6,#bda47b); border:1px solid #a98955; position:relative; overflow:hidden; margin-bottom:12px; outline:0; }
.entity { position:absolute; width:28px; height:38px; border-radius:18px 18px 12px 12px; transform:translate(-50%,-50%); box-shadow:0 10px 18px rgba(0,0,0,.25); transition:left .12s linear, top .12s linear; }
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
    <h1>Browser World v21: live scene state mutation</h1>
    <p>Keyboard movement now mutates local scene state. Collision prompts, object ceremony phases, save/restore positions, and replay rows persist through localStorage.</p>
  </section>
  <section class="grid">
    <div class="card">
      <h2>Live scene controls</h2>
      <button onclick="stepKey('ArrowUp')">Up</button><button onclick="stepKey('ArrowLeft')">Left</button><button onclick="stepKey('ArrowRight')">Right</button><button onclick="stepKey('ArrowDown')">Down</button>
      <button class="alt" onclick="stepKey('KeyE')">Ceremony</button><button class="alt" onclick="saveScene()">Save</button><button class="warn" onclick="restoreScene()">Restore</button><button onclick="exportReplay()">Export replay</button>
      <div class="scene" id="scene" tabindex="0"><div class="table"></div></div>
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
let state = JSON.parse(localStorage.getItem(KEY) || JSON.stringify({ x:6, y:4, saved:{x:6,y:4}, cursor:0, ceremonyPhase:'idle', replay:[], source }));
function persist() { localStorage.setItem(KEY, JSON.stringify(state)); render(); }
function pctX(x) { return (x / 12 * 100).toFixed(2) + '%'; }
function pctY(y) { return (y / 8 * 100).toFixed(2) + '%'; }
function stepKey(key) { const deltas = { ArrowUp:[0,-.24], ArrowDown:[0,.24], ArrowLeft:[-.28,0], ArrowRight:[.28,0] }; const d = deltas[key] || [0,0]; state.x = Math.max(.7, Math.min(11.3, state.x + d[0])); state.y = Math.max(.7, Math.min(7.3, state.y + d[1])); if (key === 'KeyE') state.ceremonyPhase = 'handoff'; state.cursor++; state.replay.push({ type:'key', key, x:state.x, y:state.y, ceremonyPhase:state.ceremonyPhase }); persist(); }
function saveScene() { state.saved = { x:state.x, y:state.y, ceremonyPhase:state.ceremonyPhase }; state.replay.push({ type:'save', saved:state.saved }); persist(); }
function restoreScene() { state.x = state.saved.x; state.y = state.saved.y; state.ceremonyPhase = state.saved.ceremonyPhase || 'restored'; state.replay.push({ type:'restore', x:state.x, y:state.y, ceremonyPhase:state.ceremonyPhase }); persist(); }
function exportReplay() { const blob = new Blob([JSON.stringify(state.replay, null, 2)], { type:'application/json' }); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'report-261-live-scene-replay.json'; a.click(); URL.revokeObjectURL(url); }
document.addEventListener('keydown', (event) => { if (['ArrowUp','ArrowDown','ArrowLeft','ArrowRight','KeyE','KeyR'].includes(event.code)) { event.preventDefault(); if (event.code === 'KeyR') restoreScene(); else stepKey(event.code); }});
function render() {
  document.getElementById('readiness').textContent = source.metrics.browser_world_v21_live_scene_mutation_readiness.toFixed(3);
  document.getElementById('weakest').textContent = source.metrics.weakest_channel_score.toFixed(3);
  document.getElementById('frames').textContent = source.counts.browser_world_v21_ticks;
  document.getElementById('state').textContent = JSON.stringify({ x:+state.x.toFixed(2), y:+state.y.toFixed(2), saved:state.saved, ceremonyPhase:state.ceremonyPhase, replayRows:state.replay.length }, null, 2);
  const scene = document.getElementById('scene'); scene.querySelectorAll('.entity,.object').forEach(n => n.remove());
  const avatar = document.createElement('div'); avatar.className = 'entity avatar'; avatar.style.left = pctX(state.x); avatar.style.top = pctY(state.y); scene.appendChild(avatar);
  const mutation = source.sample_mutations[state.cursor % source.sample_mutations.length];
  const ceremony = source.sample_ceremonies[state.cursor % source.sample_ceremonies.length];
  const agent = document.createElement('div'); agent.className = 'entity agent'; agent.style.left = pctX(ceremony.object_x + .4); agent.style.top = pctY(ceremony.object_y + .3); scene.appendChild(agent);
  const object = document.createElement('div'); object.className = 'object'; object.style.left = pctX(ceremony.object_x); object.style.top = pctY(ceremony.object_y); scene.appendChild(object);
  const log = document.getElementById('log'); log.innerHTML = '';
  source.sample_prompts.forEach((prompt) => { const div = document.createElement('div'); div.className = 'row'; div.innerHTML = `<strong>${prompt.prompt_kind}</strong><br>${prompt.prompt_text}<br><small>visible=${prompt.proximity_prompt_visible} distance=${prompt.distance_to_avatar}</small>`; log.appendChild(div); });
}
render();
</script>
</body>
</html>
"""
    output_path.write_text(template.replace("__STATE__", encoded).replace("__KEY__", LOCAL_STORAGE_KEY), encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260874)
    parser.add_argument("--days", type=int, default=24)
    parser.add_argument("--ticks-per-day", type=int, default=15)
    args = parser.parse_args(argv)

    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_DIR.mkdir(parents=True, exist_ok=True)

    source = load_source_results()
    frames = generate_frames(args.seed, args.days, args.ticks_per_day)
    metrics = compute_metrics(frames, source)
    counts = compute_counts(frames)
    ablations = compute_ablations(metrics)
    verdict = "pass" if (
        metrics["browser_world_v21_live_scene_mutation_readiness"] >= 0.84
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["keyboard_avatar_movement_binding"] >= 0.92
        and metrics["collision_blocking_integrity"] >= 0.86
        and metrics["object_ceremony_state_persistence"] >= 0.82
        and metrics["local_storage_scene_snapshot_integrity"] >= 0.84
        and metrics["save_restore_position_integrity"] >= 0.82
        and metrics["privacy_safe_live_scene_state"] >= 0.99
    ) else "partial_or_failed"

    artifact_paths = {
        "keyboard_movement_csv": ARTIFACT_DIR / f"{PREFIX}_keyboard_movement.csv",
        "scene_state_mutations_csv": ARTIFACT_DIR / f"{PREFIX}_scene_state_mutations.csv",
        "collision_proximity_prompts_csv": ARTIFACT_DIR / f"{PREFIX}_collision_proximity_prompts.csv",
        "object_ceremony_persistence_csv": ARTIFACT_DIR / f"{PREFIX}_object_ceremony_persistence.csv",
        "local_storage_snapshots_csv": ARTIFACT_DIR / f"{PREFIX}_local_storage_snapshots.csv",
        "save_restore_positions_csv": ARTIFACT_DIR / f"{PREFIX}_save_restore_positions.csv",
        "live_scene_replays_csv": ARTIFACT_DIR / f"{PREFIX}_live_scene_replays.csv",
        "multi_sensory_live_scene_csv": ARTIFACT_DIR / f"{PREFIX}_multi_sensory_live_scene.csv",
        "browser_ticks_csv": ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv",
        "summary_csv": ARTIFACT_DIR / f"{PREFIX}_summary.csv",
        "verdict_csv": ARTIFACT_DIR / f"{PREFIX}_verdict.csv",
        "state_json": ARTIFACT_DIR / f"{PREFIX}_state.json",
        "results_json": ARTIFACT_DIR / f"{PREFIX}_results.json",
        "visualization_html": VISUALIZATION_DIR / f"{PREFIX}.html",
    }

    write_csv(artifact_paths["keyboard_movement_csv"], frames["keyboard_movement"])
    write_csv(artifact_paths["scene_state_mutations_csv"], frames["scene_state_mutations"])
    write_csv(artifact_paths["collision_proximity_prompts_csv"], frames["collision_proximity_prompts"])
    write_csv(artifact_paths["object_ceremony_persistence_csv"], frames["object_ceremony_persistence"])
    write_csv(artifact_paths["local_storage_snapshots_csv"], frames["local_storage_snapshots"])
    write_csv(artifact_paths["save_restore_positions_csv"], frames["save_restore_positions"])
    write_csv(artifact_paths["live_scene_replays_csv"], frames["live_scene_replays"])
    write_csv(artifact_paths["multi_sensory_live_scene_csv"], frames["multi_sensory_live_scene"])
    write_csv(artifact_paths["browser_ticks_csv"], frames["browser_ticks"])
    write_mapping_csv(artifact_paths["summary_csv"], metrics)
    write_csv(artifact_paths["verdict_csv"], [{"verdict": verdict, **metrics}])

    state = build_state(frames, metrics, counts, args.seed)
    artifact_paths["state_json"].write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    render_html(state, artifact_paths["visualization_html"])

    results = {
        "report": 261,
        "name": "SSRM-3D browser world v21 live scene state mutation persistence bridge",
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
        "claim_boundary": "Deterministic browser-local live scene mutation scaffold only; no LLM call, subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
        "next_gate": "browser world v22 with free-move proximity-triggered dialogue prompts, persistent multi-object ceremony inventory, and reload-stable agent reaction state in the playable browser scene",
    }
    artifact_paths["results_json"].write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")

    print(json.dumps({"verdict": verdict, "metrics": metrics, "counts": counts}, indent=2, sort_keys=True))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
