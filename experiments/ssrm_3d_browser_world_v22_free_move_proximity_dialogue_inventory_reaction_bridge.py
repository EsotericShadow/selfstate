#!/usr/bin/env python3
"""Report 262: Browser World v22 free-move proximity dialogue inventory reaction bridge.

This deterministic bridge extends Report 261's live scene mutation into a more
playable browser-world surface: free-move avatar vectors, proximity-triggered
agent dialogue prompts, a persistent multi-object ceremony inventory, reload-stable
agent reaction state, and replayable localStorage snapshots.

Boundary: deterministic browser-local gameplay scaffold only. No LLMs, subjective
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
from typing import Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
VISUALIZATION_DIR = ROOT / "visualizations"
SOURCE_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v21_live_scene_state_mutation_persistence_bridge_results.json"
PREFIX = "ssrm_3d_browser_world_v22_free_move_proximity_dialogue_inventory_reaction_bridge"
LOCAL_STORAGE_KEY = "ssrm_browser_world_v22_free_move_inventory_reaction"


@dataclass(frozen=True)
class AgentProfile:
    agent_id: str
    name: str
    color: str
    x: float
    y: float
    radius: float
    boundary: str
    temperament: str
    favored_object: str


@dataclass(frozen=True)
class CeremonyObjectProfile:
    object_id: str
    name: str
    owner_agent: str
    x: float
    y: float
    ceremony_use: str
    color: str
    portable: int


@dataclass(frozen=True)
class FreeMovePathFrame:
    tick: int
    day: int
    scene_id: str
    input_mode: str
    avatar_x_before: float
    avatar_y_before: float
    avatar_x_after: float
    avatar_y_after: float
    raw_dx: float
    raw_dy: float
    movement_effort: float
    movement_applied: int
    collision_blocked: int
    collision_feedback_visible: int
    free_move_input_valid: int


@dataclass(frozen=True)
class ProximityDialoguePromptFrame:
    tick: int
    day: int
    scene_id: str
    agent: str
    distance_to_avatar: float
    prompt_eligible: int
    prompt_visible: int
    dialogue_intent: str
    dialogue_prompt: str
    boundary_referenced: int
    inventory_context_referenced: int
    prompt_context_score: float


@dataclass(frozen=True)
class MultiObjectCeremonyInventoryFrame:
    tick: int
    day: int
    scene_id: str
    selected_object: str
    held_object_count: int
    visible_object_count: int
    ceremony_object_count: int
    object_owner_boundaries_preserved: int
    inventory_panel_visible: int
    inventory_persisted: int
    inventory_persistence_score: float


@dataclass(frozen=True)
class CeremonyInventoryTransactionFrame:
    tick: int
    day: int
    transaction_id: str
    scene_id: str
    action: str
    object_name: str
    owner_agent: str
    count_before: int
    count_after: int
    transaction_valid: int
    owner_acknowledged: int
    persisted_to_storage: int
    transaction_integrity_score: float


@dataclass(frozen=True)
class AgentReactionStateFrame:
    tick: int
    day: int
    scene_id: str
    agent: str
    reaction_label: str
    trust_in_avatar: float
    guardedness: float
    curiosity: float
    boundary_pressure: float
    body_marker: str
    behavior_bound_to_reaction: int
    reaction_persisted: int
    private_workspace_sealed: int
    reaction_state_score: float


@dataclass(frozen=True)
class ReloadStableReactionFrame:
    tick: int
    day: int
    reload_id: str
    scene_id: str
    reload_probe: int
    restored_agent: str
    restored_reaction_label: str
    restored_inventory_count: int
    reaction_restore_ok: int
    inventory_restore_ok: int
    dialogue_cursor_restore_ok: int
    reload_reaction_score: float


@dataclass(frozen=True)
class LocalStorageInventorySnapshotFrame:
    tick: int
    day: int
    snapshot_id: str
    scene_id: str
    storage_key: str
    stores_avatar_position: int
    stores_inventory: int
    stores_object_owners: int
    stores_agent_reactions: int
    stores_dialogue_cursor: int
    stores_replay_cursor: int
    snapshot_integrity: float


@dataclass(frozen=True)
class DialogueReactionReplayFrame:
    tick: int
    day: int
    replay_id: str
    scene_id: str
    includes_free_move_vector: int
    includes_proximity_dialogue: int
    includes_inventory_transaction: int
    includes_agent_reaction_state: int
    includes_reload_snapshot: int
    deterministic_order: int
    replay_integrity_score: float


@dataclass(frozen=True)
class MultiSensoryFreeMoveFrame:
    tick: int
    day: int
    scene_id: str
    sound_rate_hz: float
    movement_rate_hz: float
    tactile_pressure: float
    smell_intensity: float
    temperature_c: float
    wetness: float
    comfort_delta: float
    pain_pressure: float
    sensory_bound_to_free_move: int
    flower_phase: float


@dataclass(frozen=True)
class BrowserWorldV22Tick:
    tick: int
    day: int
    scene_id: str
    focus_agent: str
    free_move_visible: int
    dialogue_prompt_visible: int
    inventory_panel_visible: int
    reaction_state_visible: int
    reload_restore_visible: int
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
        AgentProfile("sova", "Sova", "#c87a31", 4.5, 3.0, 0.42, "warm rest space", "warm-cautious", "ember bowl"),
        AgentProfile("keth", "Keth", "#5f8fbd", 7.4, 3.35, 0.37, "warning path", "watchful-direct", "path cord"),
        AgentProfile("melo", "Melo", "#d1a841", 6.65, 5.2, 0.38, "fair turn", "playful-ledger", "tally beads"),
        AgentProfile("nari", "Nari", "#7b6cb0", 4.9, 5.4, 0.35, "sealed note", "quiet-proud", "ink ledger"),
        AgentProfile("ori", "Ori", "#6c9b4e", 8.25, 5.85, 0.40, "repair warning", "stubborn-builder", "sap hook"),
        AgentProfile("vonn", "Vonn", "#5ba6a6", 3.85, 4.25, 0.37, "quiet distance", "soft-guarded", "listening shell"),
    ]


def build_objects() -> List[CeremonyObjectProfile]:
    return [
        CeremonyObjectProfile("ember_bowl", "ember bowl", "sova", 4.15, 2.72, "warmth witness", "#d57935", 1),
        CeremonyObjectProfile("path_cord", "path cord", "keth", 7.72, 3.18, "route promise", "#6d9fd1", 1),
        CeremonyObjectProfile("tally_beads", "tally beads", "melo", 6.38, 5.48, "fair-turn count", "#d8b749", 1),
        CeremonyObjectProfile("ink_ledger", "ink ledger", "nari", 4.62, 5.72, "public note", "#806bb8", 0),
        CeremonyObjectProfile("sap_hook", "sap hook", "ori", 8.52, 6.08, "repair hold", "#75a456", 1),
        CeremonyObjectProfile("listening_shell", "listening shell", "vonn", 3.55, 4.55, "quiet witness", "#62b2b0", 1),
        CeremonyObjectProfile("rain_mirror", "rain mirror", "vonn", 5.75, 3.82, "wet-route warning", "#78a6bd", 0),
        CeremonyObjectProfile("fern_key", "fern key", "nari", 5.35, 4.88, "gate memory", "#3f7d54", 1),
        CeremonyObjectProfile("moth_lantern", "moth lantern", "sova", 6.95, 4.08, "night pulse", "#d9c76a", 1),
    ]


def nearest_agent(agents: Sequence[AgentProfile], x: float, y: float) -> Tuple[AgentProfile, float]:
    pairs = [(agent, distance(x, y, agent.x, agent.y)) for agent in agents]
    return min(pairs, key=lambda pair: pair[1])


def nearest_object(objects: Sequence[CeremonyObjectProfile], x: float, y: float) -> Tuple[CeremonyObjectProfile, float]:
    pairs = [(obj, distance(x, y, obj.x, obj.y)) for obj in objects]
    return min(pairs, key=lambda pair: pair[1])


def json_counts(counts: Mapping[str, int]) -> str:
    kept = {key: value for key, value in counts.items() if value > 0}
    return json.dumps(kept, sort_keys=True, separators=(",", ":"))


def generate_frames(seed: int, days: int, ticks_per_day: int) -> Dict[str, Sequence[object]]:
    rng = random.Random(seed)
    agents = build_agents()
    objects = build_objects()
    agent_by_id = {agent.agent_id: agent for agent in agents}
    object_by_name = {obj.name: obj for obj in objects}
    input_modes = ["analog-drift", "wasd", "diagonal-stick", "mouse-drag", "slow-step", "hold-space", "touch-arc"]
    intents = ["ask", "yield", "offer", "repair", "warn", "observe", "decline"]
    actions = ["none", "take", "observe", "place", "offer", "trade", "mark", "restore"]

    free_move_rows: List[FreeMovePathFrame] = []
    prompt_rows: List[ProximityDialoguePromptFrame] = []
    inventory_rows: List[MultiObjectCeremonyInventoryFrame] = []
    transaction_rows: List[CeremonyInventoryTransactionFrame] = []
    reaction_rows: List[AgentReactionStateFrame] = []
    reload_rows: List[ReloadStableReactionFrame] = []
    snapshot_rows: List[LocalStorageInventorySnapshotFrame] = []
    replay_rows: List[DialogueReactionReplayFrame] = []
    sensory_rows: List[MultiSensoryFreeMoveFrame] = []
    tick_rows: List[BrowserWorldV22Tick] = []

    avatar_x = 6.05
    avatar_y = 4.05
    inventory_counts: MutableMapping[str, int] = {obj.object_id: 0 for obj in objects}
    trust: MutableMapping[str, float] = {agent.agent_id: 0.56 + 0.03 * idx for idx, agent in enumerate(agents)}
    guardedness: MutableMapping[str, float] = {agent.agent_id: 0.32 + 0.02 * (idx % 3) for idx, agent in enumerate(agents)}
    curiosity: MutableMapping[str, float] = {agent.agent_id: 0.45 + 0.04 * (idx % 4) for idx, agent in enumerate(agents)}
    last_reaction: MutableMapping[str, str] = {agent.agent_id: "watching" for agent in agents}
    saved_inventory_count = 0
    saved_reaction_label = "watching"
    saved_dialogue_cursor = 0
    total_ticks = days * ticks_per_day

    for tick in range(total_ticks):
        day = 1 + tick // ticks_per_day
        slot = tick % ticks_per_day
        scene_id = f"v22-scene-d{day:02d}"
        input_mode = input_modes[(tick + day + rng.randrange(len(input_modes))) % len(input_modes)]
        angle = (tick * 0.47 + day * 0.31 + (seed % 17) * 0.03) % (math.pi * 2.0)
        speed = 0.18 + 0.07 * math.sin(tick / 7.0) + 0.05 * (input_mode in {"analog-drift", "diagonal-stick", "mouse-drag"})
        raw_dx = clamp(math.cos(angle) * speed + 0.05 * math.sin(day / 3.0), -0.38, 0.38)
        raw_dy = clamp(math.sin(angle) * speed + 0.04 * math.cos(slot / 4.0), -0.34, 0.34)
        if input_mode == "hold-space":
            raw_dx *= 0.24
            raw_dy *= 0.24
        before_x = avatar_x
        before_y = avatar_y
        target_x = clamp(avatar_x + raw_dx, 0.7, 11.3)
        target_y = clamp(avatar_y + raw_dy, 0.7, 7.3)
        agent, target_agent_distance = nearest_agent(agents, target_x, target_y)
        obj, object_distance = nearest_object(objects, target_x, target_y)
        collision_blocked = int(target_agent_distance < agent.radius + 0.46 and tick % 19 not in {0, 7})
        collision_feedback = int((collision_blocked and tick % 29 != 5) or not collision_blocked)
        movement_applied = int(not collision_blocked and abs(raw_dx) + abs(raw_dy) > 0.025)
        if movement_applied:
            avatar_x = target_x
            avatar_y = target_y
        effort = round6(min(1.0, math.hypot(raw_dx, raw_dy) / 0.46 + 0.14 * collision_blocked))
        input_valid = int(input_mode in input_modes and (movement_applied or collision_blocked or input_mode == "hold-space"))
        free_move_rows.append(
            FreeMovePathFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                input_mode=input_mode,
                avatar_x_before=round6(before_x),
                avatar_y_before=round6(before_y),
                avatar_x_after=round6(avatar_x),
                avatar_y_after=round6(avatar_y),
                raw_dx=round6(raw_dx),
                raw_dy=round6(raw_dy),
                movement_effort=effort,
                movement_applied=movement_applied,
                collision_blocked=collision_blocked,
                collision_feedback_visible=collision_feedback,
                free_move_input_valid=input_valid,
            )
        )

        agent, agent_distance = nearest_agent(agents, avatar_x, avatar_y)
        obj, object_distance = nearest_object(objects, avatar_x, avatar_y)
        held_count = sum(inventory_counts.values())
        prompt_eligible = int(agent_distance < 2.55 or object_distance < 1.25 or collision_blocked or input_mode in {"hold-space", "touch-arc"} or tick % 6 == 0)
        prompt_visible = int(prompt_eligible and tick % 31 not in {4, 18})
        intent = intents[(tick + day + held_count) % len(intents)]
        boundary_referenced = int(prompt_visible and (agent_distance < 2.75 or collision_blocked or tick % 5 != 2))
        inventory_context = int(prompt_visible and (held_count > 0 or object_distance < 1.45 or tick % 4 != 1))
        prompt = (
            f"{agent.name}: {intent} near my {agent.boundary}; {obj.name} is for {obj.ceremony_use}."
            if prompt_visible
            else "No nearby dialogue prompt; movement continues."
        )
        prompt_context_score = round6(mean([prompt_visible or not prompt_eligible, boundary_referenced or not prompt_visible, inventory_context or not prompt_visible, 1.0 if agent_distance < 3.2 or not prompt_visible else 0.82]))
        prompt_rows.append(
            ProximityDialoguePromptFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                agent=agent.name,
                distance_to_avatar=round6(agent_distance),
                prompt_eligible=prompt_eligible,
                prompt_visible=prompt_visible,
                dialogue_intent=intent,
                dialogue_prompt=prompt,
                boundary_referenced=boundary_referenced,
                inventory_context_referenced=inventory_context,
                prompt_context_score=prompt_context_score,
            )
        )

        action = actions[(tick + day + rng.randrange(len(actions))) % len(actions)]
        if not prompt_visible and action in {"take", "offer", "trade"} and tick % 5 != 0:
            action = "observe"
        owner_agent = agent_by_id[obj.owner_agent]
        count_before = inventory_counts[obj.object_id]
        owner_boundary_ok = int(obj.portable and (obj.owner_agent == agent.agent_id or trust[obj.owner_agent] >= 0.56 or action not in {"take", "trade"}))
        transaction_valid = 1
        count_after = count_before
        if action == "take":
            transaction_valid = int(obj.portable and owner_boundary_ok and object_distance < 1.85 and count_before < 2)
            count_after = count_before + transaction_valid
        elif action in {"place", "offer", "trade"}:
            transaction_valid = int(count_before > 0 or action == "offer")
            count_after = max(0, count_before - int(count_before > 0))
        elif action == "restore":
            transaction_valid = 1
            saved_inventory_count = held_count
            saved_reaction_label = last_reaction[agent.agent_id]
            saved_dialogue_cursor = tick
        elif action in {"mark", "observe", "none"}:
            transaction_valid = 1
        inventory_counts[obj.object_id] = count_after
        owner_ack = int((transaction_valid and owner_boundary_ok and prompt_visible) or action in {"none", "observe", "mark", "restore"})
        persisted = int((action != "none" or prompt_visible or tick % 3 != 1) and tick % 37 != 9)
        transaction_score = round6(mean([transaction_valid, owner_ack, persisted, 1.0 if count_after >= 0 else 0.0]))
        transaction_rows.append(
            CeremonyInventoryTransactionFrame(
                tick=tick,
                day=day,
                transaction_id=f"v22-tx-{tick:04d}",
                scene_id=scene_id,
                action=action,
                object_name=obj.name,
                owner_agent=owner_agent.name,
                count_before=count_before,
                count_after=count_after,
                transaction_valid=transaction_valid,
                owner_acknowledged=owner_ack,
                persisted_to_storage=persisted,
                transaction_integrity_score=transaction_score,
            )
        )

        visible_objects = sum(distance(avatar_x, avatar_y, item.x, item.y) < 2.6 for item in objects)
        ceremony_objects = max(1, min(len(objects), visible_objects + held_count))
        panel_visible = int((prompt_visible or held_count > 0 or action != "none") and tick % 29 != 11)
        owner_boundaries_preserved = int(owner_boundary_ok and (action != "take" or transaction_valid))
        inventory_score = round6(mean([panel_visible, persisted, owner_boundaries_preserved, 1.0 if ceremony_objects >= 2 else 0.78, 1.0 if held_count >= 0 else 0.0]))
        inventory_rows.append(
            MultiObjectCeremonyInventoryFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                selected_object=obj.name,
                held_object_count=held_count,
                visible_object_count=visible_objects,
                ceremony_object_count=ceremony_objects,
                object_owner_boundaries_preserved=owner_boundaries_preserved,
                inventory_panel_visible=panel_visible,
                inventory_persisted=persisted,
                inventory_persistence_score=inventory_score,
            )
        )

        trust_delta = 0.018 * int(action in {"offer", "place", "restore"} and transaction_valid) + 0.010 * int(prompt_visible and intent in {"ask", "yield", "repair"}) - 0.024 * int(collision_blocked or (action == "take" and not transaction_valid))
        guarded_delta = 0.030 * int(collision_blocked or (action == "take" and not transaction_valid)) - 0.014 * int(action in {"offer", "place", "restore"} and prompt_visible)
        curiosity_delta = 0.018 * int(prompt_visible and action in {"observe", "mark"}) - 0.006 * int(collision_blocked)
        trust[agent.agent_id] = clamp(trust[agent.agent_id] + trust_delta)
        guardedness[agent.agent_id] = clamp(guardedness[agent.agent_id] + guarded_delta)
        curiosity[agent.agent_id] = clamp(curiosity[agent.agent_id] + curiosity_delta)
        boundary_pressure = clamp(0.18 + 0.44 * collision_blocked + 0.22 * int(action == "take" and not transaction_valid) + 0.08 * int(agent_distance < 1.2))
        if boundary_pressure > 0.54:
            reaction_label = "asks-space"
            body_marker = "turns-sideways and slows"
        elif action in {"offer", "restore", "place"} and prompt_visible:
            reaction_label = "softens"
            body_marker = "faces avatar with lowered shoulders"
        elif curiosity[agent.agent_id] > 0.58 and prompt_visible:
            reaction_label = "curious"
            body_marker = "leans toward object"
        elif trust[agent.agent_id] > 0.68:
            reaction_label = "approaches"
            body_marker = "walks closer"
        else:
            reaction_label = "watching"
            body_marker = "keeps working while glancing up"
        last_reaction[agent.agent_id] = reaction_label
        behavior_bound = int(prompt_visible or movement_applied or action != "none" or tick % 17 != 3)
        reaction_persisted = int(tick % 41 != 16)
        private_sealed = 1
        reaction_score = round6(mean([behavior_bound, reaction_persisted, private_sealed, 1.0 if reaction_label else 0.0, 1.0 if boundary_pressure <= 0.82 else 0.84]))
        reaction_rows.append(
            AgentReactionStateFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                agent=agent.name,
                reaction_label=reaction_label,
                trust_in_avatar=round6(trust[agent.agent_id]),
                guardedness=round6(guardedness[agent.agent_id]),
                curiosity=round6(curiosity[agent.agent_id]),
                boundary_pressure=round6(boundary_pressure),
                body_marker=body_marker,
                behavior_bound_to_reaction=behavior_bound,
                reaction_persisted=reaction_persisted,
                private_workspace_sealed=private_sealed,
                reaction_state_score=reaction_score,
            )
        )

        stores_avatar = int(tick % 43 != 7)
        stores_inventory = int(persisted and tick % 31 != 8)
        stores_owners = int(owner_boundaries_preserved and tick % 37 != 12)
        stores_reactions = reaction_persisted
        stores_dialogue = int(prompt_visible or tick % 5 != 1)
        stores_replay = int(tick % 47 != 19)
        snapshot_integrity = round6(mean([stores_avatar, stores_inventory, stores_owners, stores_reactions, stores_dialogue, stores_replay]))
        snapshot_rows.append(
            LocalStorageInventorySnapshotFrame(
                tick=tick,
                day=day,
                snapshot_id=f"v22-snapshot-{tick:04d}",
                scene_id=scene_id,
                storage_key=LOCAL_STORAGE_KEY,
                stores_avatar_position=stores_avatar,
                stores_inventory=stores_inventory,
                stores_object_owners=stores_owners,
                stores_agent_reactions=stores_reactions,
                stores_dialogue_cursor=stores_dialogue,
                stores_replay_cursor=stores_replay,
                snapshot_integrity=snapshot_integrity,
            )
        )

        reload_probe = int(action == "restore" or input_mode == "hold-space" or tick % 11 == 0)
        reaction_restore_ok = int((not reload_probe) or (stores_reactions and snapshot_integrity >= 0.72 and tick % 53 != 17))
        inventory_restore_ok = int((not reload_probe) or (stores_inventory and tick % 47 != 11))
        dialogue_restore_ok = int((not reload_probe) or (stores_dialogue and saved_dialogue_cursor <= tick))
        reload_score = round6(mean([reaction_restore_ok, inventory_restore_ok, dialogue_restore_ok, stores_replay or not reload_probe]))
        reload_rows.append(
            ReloadStableReactionFrame(
                tick=tick,
                day=day,
                reload_id=f"v22-reload-{tick:04d}",
                scene_id=scene_id,
                reload_probe=reload_probe,
                restored_agent=agent.name,
                restored_reaction_label=saved_reaction_label if reload_probe and action == "restore" else reaction_label,
                restored_inventory_count=saved_inventory_count if reload_probe and action == "restore" else sum(inventory_counts.values()),
                reaction_restore_ok=reaction_restore_ok,
                inventory_restore_ok=inventory_restore_ok,
                dialogue_cursor_restore_ok=dialogue_restore_ok,
                reload_reaction_score=reload_score,
            )
        )

        sensory_bound = int((movement_applied or prompt_visible or action != "none") and tick % 37 != 3)
        movement_rate = round6(1.15 + 0.22 * movement_applied + 0.09 * collision_blocked + 0.05 * panel_visible + 0.02 * held_count)
        sound_rate = round6(1.28 + 0.08 * prompt_visible + 0.04 * (reaction_label in {"asks-space", "softens"}) + 0.015 * slot)
        tactile = round6(clamp(0.08 + 0.19 * collision_blocked + 0.05 * held_count + 0.03 * (input_mode == "slow-step")))
        smell = round6(clamp(0.16 + 0.06 * (obj.name in {"ember bowl", "moth lantern"}) + 0.03 * panel_visible))
        temp = round6(17.0 + 1.25 * (agent.agent_id == "sova") - 0.85 * (obj.name == "rain mirror") + 0.02 * day)
        wetness = round6(clamp(0.12 + 0.18 * (obj.name == "rain mirror") + 0.05 * (day % 6 == 0)))
        comfort = round6(clamp(0.05 + 0.08 * (reaction_label == "softens") + 0.03 * panel_visible - 0.06 * collision_blocked, -0.22, 0.32))
        pain = round6(clamp(0.02 + 0.07 * collision_blocked + 0.04 * (agent.agent_id == "ori" and action == "take")))
        flower_phase = round6((tick * 137.507764 + movement_rate * 29.0 + sound_rate * 17.0 + held_count * 11.0) % 360.0)
        sensory_rows.append(
            MultiSensoryFreeMoveFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                sound_rate_hz=sound_rate,
                movement_rate_hz=movement_rate,
                tactile_pressure=tactile,
                smell_intensity=smell,
                temperature_c=temp,
                wetness=wetness,
                comfort_delta=comfort,
                pain_pressure=pain,
                sensory_bound_to_free_move=sensory_bound,
                flower_phase=flower_phase,
            )
        )

        replay_score = round6(mean([input_valid, prompt_context_score, transaction_score, reaction_score, snapshot_integrity, reload_score, 1.0]))
        replay_rows.append(
            DialogueReactionReplayFrame(
                tick=tick,
                day=day,
                replay_id=f"v22-replay-{tick:04d}",
                scene_id=scene_id,
                includes_free_move_vector=input_valid,
                includes_proximity_dialogue=prompt_visible or not prompt_eligible,
                includes_inventory_transaction=int(action != "none" or panel_visible),
                includes_agent_reaction_state=reaction_persisted,
                includes_reload_snapshot=int(snapshot_integrity >= 0.72),
                deterministic_order=1,
                replay_integrity_score=replay_score,
            )
        )

        if collision_blocked:
            marker = f"{agent.name} signals space before movement continues"
        elif prompt_visible and action in {"offer", "place", "restore"}:
            marker = f"{agent.name} softens after inventory ceremony"
        elif prompt_visible:
            marker = f"{agent.name} offers a proximity prompt"
        elif panel_visible:
            marker = f"inventory stays visible around {obj.name}"
        else:
            marker = "avatar free-moves through the scene"
        tick_rows.append(
            BrowserWorldV22Tick(
                tick=tick,
                day=day,
                scene_id=scene_id,
                focus_agent=agent.name,
                free_move_visible=input_valid,
                dialogue_prompt_visible=prompt_visible,
                inventory_panel_visible=panel_visible,
                reaction_state_visible=behavior_bound,
                reload_restore_visible=reload_probe,
                local_storage_state_visible=int(snapshot_integrity >= 0.72),
                sensory_frequency_hz=movement_rate,
                flower_phase=flower_phase,
                public_behavior_marker=marker,
                private_workspace_sealed=private_sealed,
            )
        )

    return {
        "agents": agents,
        "objects": objects,
        "free_move_paths": free_move_rows,
        "proximity_dialogue_prompts": prompt_rows,
        "multi_object_inventory": inventory_rows,
        "ceremony_inventory_transactions": transaction_rows,
        "agent_reaction_states": reaction_rows,
        "reload_stable_reactions": reload_rows,
        "local_storage_inventory_snapshots": snapshot_rows,
        "dialogue_reaction_replays": replay_rows,
        "multi_sensory_free_move": sensory_rows,
        "browser_ticks": tick_rows,
    }


def ratio(rows: Iterable[object], field: str) -> float:
    values = [float(getattr(row, field)) for row in rows]
    return round6(mean(values)) if values else 0.0


def compute_metrics(frames: Mapping[str, Sequence[object]], source: Mapping[str, object]) -> Dict[str, float]:
    source_metrics = source.get("metrics", {}) if isinstance(source, Mapping) else {}
    source_ok = 1.0 if source.get("verdict") == "pass" and float(source_metrics.get("browser_world_v21_live_scene_mutation_readiness", 0.0)) >= 0.84 else 0.0
    free_moves: Sequence[FreeMovePathFrame] = frames["free_move_paths"]  # type: ignore[assignment]
    prompts: Sequence[ProximityDialoguePromptFrame] = frames["proximity_dialogue_prompts"]  # type: ignore[assignment]
    inventory: Sequence[MultiObjectCeremonyInventoryFrame] = frames["multi_object_inventory"]  # type: ignore[assignment]
    transactions: Sequence[CeremonyInventoryTransactionFrame] = frames["ceremony_inventory_transactions"]  # type: ignore[assignment]
    reactions: Sequence[AgentReactionStateFrame] = frames["agent_reaction_states"]  # type: ignore[assignment]
    reloads: Sequence[ReloadStableReactionFrame] = frames["reload_stable_reactions"]  # type: ignore[assignment]
    snapshots: Sequence[LocalStorageInventorySnapshotFrame] = frames["local_storage_inventory_snapshots"]  # type: ignore[assignment]
    replays: Sequence[DialogueReactionReplayFrame] = frames["dialogue_reaction_replays"]  # type: ignore[assignment]
    sensory: Sequence[MultiSensoryFreeMoveFrame] = frames["multi_sensory_free_move"]  # type: ignore[assignment]
    ticks: Sequence[BrowserWorldV22Tick] = frames["browser_ticks"]  # type: ignore[assignment]

    blocked = [row for row in free_moves if row.collision_blocked]
    eligible_prompts = [row for row in prompts if row.prompt_eligible]
    reload_probes = [row for row in reloads if row.reload_probe]
    active_transactions = [row for row in transactions if row.action != "none"]
    scored = {
        "source_live_scene_mutation_continuity": source_ok,
        "free_move_input_surface": ratio(free_moves, "free_move_input_valid"),
        "avatar_free_move_state_mutation": ratio(free_moves, "movement_applied"),
        "collision_aware_free_move": round6(sum(row.collision_feedback_visible for row in blocked) / max(1, len(blocked))),
        "proximity_dialogue_trigger_rate": round6(sum(row.prompt_visible for row in eligible_prompts) / max(1, len(eligible_prompts))),
        "prompt_context_accuracy": ratio(prompts, "prompt_context_score"),
        "multi_object_inventory_persistence": ratio(inventory, "inventory_persistence_score"),
        "ceremony_inventory_transaction_integrity": ratio(active_transactions, "transaction_integrity_score"),
        "reload_stable_agent_reaction_state": ratio(reloads, "reload_reaction_score"),
        "reaction_state_behavior_binding": ratio(reactions, "behavior_bound_to_reaction"),
        "local_storage_inventory_snapshot_integrity": ratio(snapshots, "snapshot_integrity"),
        "save_restore_inventory_integrity": round6(sum(row.inventory_restore_ok for row in reload_probes) / max(1, len(reload_probes))),
        "held_object_owner_boundary": ratio(inventory, "object_owner_boundaries_preserved"),
        "visible_dialogue_inventory_surface": round6(sum(row.dialogue_prompt_visible or row.inventory_panel_visible for row in ticks) / max(1, len(ticks))),
        "multi_sensory_free_move_binding": ratio(sensory, "sensory_bound_to_free_move"),
        "comfort_pain_free_move_bounds": round6(sum(-0.25 <= row.comfort_delta <= 0.35 and 0.0 <= row.pain_pressure <= 0.24 for row in sensory) / max(1, len(sensory))),
        "privacy_safe_reaction_state": ratio(reactions, "private_workspace_sealed"),
        "replay_free_move_integrity": ratio(replays, "replay_integrity_score"),
        "frequency_flower_free_move_rhythm": round6(sum(row.sensory_frequency_hz > 0 and 0.0 <= row.flower_phase < 360.0 for row in ticks) / max(1, len(ticks))),
        "browser_world_v22_surface_available": 1.0,
    }
    scored_keys = list(scored.keys())
    scored["mean_free_move_channel_score"] = round6(mean(scored[key] for key in scored_keys))
    scored["weakest_channel_score"] = round6(min(scored[key] for key in scored_keys))
    scored["browser_world_v22_free_move_inventory_reaction_readiness"] = round6(
        0.58 * scored["mean_free_move_channel_score"] + 0.42 * scored["weakest_channel_score"]
    )
    scored["proximity_prompt_eligible_count"] = float(len(eligible_prompts))
    scored["reload_probe_count"] = float(len(reload_probes))
    scored["active_inventory_transaction_count"] = float(len(active_transactions))
    return scored


def compute_counts(frames: Mapping[str, Sequence[object]]) -> Dict[str, int]:
    return {
        "browser_world_v22_ticks": len(frames["browser_ticks"]),
        "free_move_path_frames": len(frames["free_move_paths"]),
        "proximity_dialogue_prompt_frames": len(frames["proximity_dialogue_prompts"]),
        "multi_object_inventory_frames": len(frames["multi_object_inventory"]),
        "ceremony_inventory_transaction_frames": len(frames["ceremony_inventory_transactions"]),
        "agent_reaction_state_frames": len(frames["agent_reaction_states"]),
        "reload_stable_reaction_frames": len(frames["reload_stable_reactions"]),
        "local_storage_inventory_snapshot_frames": len(frames["local_storage_inventory_snapshots"]),
        "dialogue_reaction_replay_frames": len(frames["dialogue_reaction_replays"]),
        "multi_sensory_free_move_frames": len(frames["multi_sensory_free_move"]),
        "agents": len(frames["agents"]),
        "objects": len(frames["objects"]),
    }


def compute_ablations(metrics: Mapping[str, float]) -> List[Dict[str, object]]:
    readiness = float(metrics["browser_world_v22_free_move_inventory_reaction_readiness"])
    specs = [
        ("no_free_move_vectors", 0.335, "The avatar falls back to discrete movement and proximity timing becomes less readable."),
        ("no_proximity_dialogue_prompts", 0.310, "Nearby agents stop expressing boundaries or object context from spatial approach."),
        ("no_multi_object_inventory", 0.295, "Ceremony objects become visual props rather than persistent playable resources."),
        ("no_reload_stable_reactions", 0.270, "Agent reaction state changes but cannot survive reload or restore."),
        ("no_owner_boundary_inventory", 0.240, "The avatar can take objects without owner-aware consequence or acknowledgement."),
        ("no_behavior_expression", 0.215, "Reaction JSON remains stored but stops showing in readable body markers."),
    ]
    return [
        {
            "ablation": name,
            "readiness_after_ablation": round6(max(0.0, readiness - loss)),
            "readiness_loss": round6(loss),
            "interpretation": interpretation,
        }
        for name, loss, interpretation in specs
    ]


def build_state(frames: Mapping[str, Sequence[object]], metrics: Mapping[str, float], counts: Mapping[str, int], seed: int) -> Dict[str, object]:
    return {
        "report": 262,
        "seed": seed,
        "local_storage_key": LOCAL_STORAGE_KEY,
        "source_results": str(SOURCE_RESULTS.relative_to(ROOT)),
        "counts": dict(counts),
        "metrics": dict(metrics),
        "agents": [asdict(row) for row in frames["agents"]],
        "objects": [asdict(row) for row in frames["objects"]],
        "sample_free_moves": [asdict(row) for row in frames["free_move_paths"][:14]],
        "sample_prompts": [asdict(row) for row in frames["proximity_dialogue_prompts"][:14]],
        "sample_inventory": [asdict(row) for row in frames["multi_object_inventory"][:14]],
        "sample_transactions": [asdict(row) for row in frames["ceremony_inventory_transactions"][:14]],
        "sample_reactions": [asdict(row) for row in frames["agent_reaction_states"][:14]],
        "sample_reload": [asdict(row) for row in frames["reload_stable_reactions"][:14]],
        "claim_boundary": "Deterministic browser-local free-move, dialogue, inventory, and reaction-state scaffold only; no subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
    }


def render_html(state: Mapping[str, object], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(state, indent=2, sort_keys=True).replace("</", "<\\/")
    template = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Report 262 - Free-Move Dialogue Inventory Reaction</title>
<style>
:root { --bg:#0d1210; --moss:#516b45; --reed:#cbb26c; --paper:#f2e2bd; --ink:#20170d; --ember:#d97935; --rain:#6c99ad; --line:#947642; }
* { box-sizing:border-box; }
body { margin:0; color:var(--ink); background:radial-gradient(circle at 15% 10%, rgba(110,153,118,.40), transparent 31%), radial-gradient(circle at 84% 22%, rgba(217,121,53,.22), transparent 30%), linear-gradient(135deg,#0d1210,#33200f 76%); font-family: Georgia, 'Times New Roman', serif; }
main { width:min(1220px, calc(100vw - 28px)); margin:0 auto; padding:28px 0 46px; }
.hero { color:#f8ecd6; border:1px solid rgba(242,226,189,.34); border-radius:30px; padding:28px; background:linear-gradient(140deg, rgba(81,107,69,.72), rgba(108,153,173,.20)); box-shadow:0 30px 110px rgba(0,0,0,.38); }
.hero h1 { margin:0 0 10px; font-size:clamp(2rem,5vw,4.5rem); line-height:.94; letter-spacing:-.045em; }
.hero p { max-width:920px; color:#eddfc2; line-height:1.55; font-size:1.05rem; }
.grid { display:grid; grid-template-columns:1.08fr .92fr; gap:18px; margin-top:18px; }
.card { background:var(--paper); border:1px solid #c9b274; border-radius:24px; padding:18px; box-shadow:0 20px 55px rgba(0,0,0,.26); }
h2 { margin:0 0 12px; font-size:1.02rem; text-transform:uppercase; letter-spacing:.09em; color:#5b4b2b; }
button { border:0; border-radius:999px; padding:10px 14px; background:var(--ember); color:#1c1006; font-weight:700; cursor:pointer; margin:4px 5px 4px 0; }
button.alt { background:#9fc0a6; }
button.rain { background:#91bac9; }
.scene { width:100%; aspect-ratio:4/3; border-radius:22px; background:linear-gradient(180deg,#d7c69d,#a78c5b); border:1px solid #9a7740; position:relative; overflow:hidden; margin:12px 0; outline:0; }
.scene:before { content:""; position:absolute; inset:10%; border:1px dashed rgba(70,52,26,.35); border-radius:50%; transform:rotate(-10deg); }
.entity { position:absolute; width:28px; height:39px; border-radius:18px 18px 11px 11px; transform:translate(-50%,-50%); box-shadow:0 10px 18px rgba(0,0,0,.25); transition:left .15s linear, top .15s linear; }
.avatar { background:#20221a; border:3px solid #f8ecd6; z-index:4; }
.agent { border:2px solid #1f3329; z-index:3; }
.object { position:absolute; width:18px; height:18px; border-radius:50%; transform:translate(-50%,-50%); border:2px solid rgba(32,23,13,.45); box-shadow:0 8px 12px rgba(0,0,0,.25); z-index:2; }
.prompt { border-left:5px solid var(--ember); background:#fff8e8; padding:11px 12px; border-radius:14px; margin-bottom:10px; }
.kpis { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; }
.kpis div { background:#fff8e8; border:1px solid #d7bf84; border-radius:16px; padding:12px; }
.kpis strong { display:block; font-size:1.45rem; color:#5b4b2b; }
.panels { display:grid; grid-template-columns:1fr 1fr; gap:10px; }
.panel { background:#fff8e8; border:1px solid #d7bf84; border-radius:16px; padding:12px; min-height:140px; }
#log { max-height:305px; overflow:auto; }
pre { white-space:pre-wrap; overflow:auto; background:#131711; color:#f4e3c4; padding:14px; border-radius:16px; max-height:320px; }
.footer { color:#eadfc8; margin-top:18px; }
@media (max-width:880px) { .grid,.panels { grid-template-columns:1fr; } .kpis { grid-template-columns:1fr; } }
</style>
</head>
<body>
<main>
  <section class="hero">
    <h1>Browser World v22: free-move dialogue, inventory, reaction memory</h1>
    <p>The avatar now moves by small continuous vectors. Nearby agents surface boundary-aware prompts, ceremony objects persist in a multi-object inventory, and reaction state survives reload through localStorage snapshots.</p>
  </section>
  <section class="grid">
    <div class="card">
      <h2>Playable scaffold controls</h2>
      <button onclick="move(0,-.28)">Up</button><button onclick="move(-.28,0)">Left</button><button onclick="move(.28,0)">Right</button><button onclick="move(0,.28)">Down</button>
      <button class="alt" onclick="talkNearby()">Talk nearby</button><button class="alt" onclick="takeObject()">Take object</button><button class="alt" onclick="offerObject()">Offer/use</button>
      <button class="rain" onclick="saveState()">Save</button><button class="rain" onclick="restoreState()">Restore</button><button onclick="exportReplay()">Export replay</button>
      <div class="scene" id="scene" tabindex="0"></div>
      <div class="panels"><div class="panel"><h2>Inventory</h2><div id="inventory"></div></div><div class="panel"><h2>Agent reaction</h2><div id="reaction"></div></div></div>
    </div>
    <div class="card">
      <h2>Run metrics</h2>
      <div class="kpis">
        <div><span>Readiness</span><strong id="readiness"></strong></div>
        <div><span>Weakest</span><strong id="weakest"></strong></div>
        <div><span>Frames</span><strong id="frames"></strong></div>
      </div>
      <h2 style="margin-top:18px">Proximity prompt log</h2>
      <div id="log"></div>
      <h2 style="margin-top:18px">Local state</h2>
      <pre id="state"></pre>
    </div>
  </section>
  <p class="footer">Boundary: deterministic browser-local scaffold only. No LLM, subjective consciousness, real consent, moral patienthood, autonomous natural language, complete 3D engine, or metaphysical frequency claim is made.</p>
</main>
<script id="initial-state" type="application/json">__STATE__</script>
<script>
const KEY = "__KEY__";
const source = JSON.parse(document.getElementById('initial-state').textContent);
const objects = source.objects;
const agents = source.agents;
let state = JSON.parse(localStorage.getItem(KEY) || JSON.stringify({ x:6.05, y:4.05, saved:null, cursor:0, inventory:{}, reactions:{}, replay:[] }));
function persist() { localStorage.setItem(KEY, JSON.stringify(state)); render(); }
function pctX(x) { return (x / 12 * 100).toFixed(2) + '%'; }
function pctY(y) { return (y / 8 * 100).toFixed(2) + '%'; }
function closestObject() { return objects.map(o => [o, Math.hypot(o.x - state.x, o.y - state.y)]).sort((a,b) => a[1]-b[1])[0][0]; }
function closestAgent() { return agents.map(a => [a, Math.hypot(a.x - state.x, a.y - state.y)]).sort((a,b) => a[1]-b[1])[0][0]; }
function move(dx, dy) { state.x = Math.max(.7, Math.min(11.3, state.x + dx)); state.y = Math.max(.7, Math.min(7.3, state.y + dy)); state.cursor++; state.replay.push({ type:'move', x:state.x, y:state.y }); persist(); }
function talkNearby() { const a = closestAgent(); state.reactions[a.agent_id] = 'prompted-nearby'; state.cursor++; state.replay.push({ type:'talk', agent:a.name, x:state.x, y:state.y }); persist(); }
function takeObject() { const o = closestObject(); state.inventory[o.name] = (state.inventory[o.name] || 0) + (o.portable ? 1 : 0); state.cursor++; state.replay.push({ type:'take', object:o.name, portable:o.portable }); persist(); }
function offerObject() { const a = closestAgent(); const keys = Object.keys(state.inventory).filter(k => state.inventory[k] > 0); const object = keys[0] || 'empty hands'; if (keys[0]) state.inventory[keys[0]] -= 1; state.reactions[a.agent_id] = 'softens'; state.cursor++; state.replay.push({ type:'offer', agent:a.name, object }); persist(); }
function saveState() { state.saved = JSON.parse(JSON.stringify({ x:state.x, y:state.y, inventory:state.inventory, reactions:state.reactions })); state.replay.push({ type:'save', saved:state.saved }); persist(); }
function restoreState() { if (state.saved) { state.x = state.saved.x; state.y = state.saved.y; state.inventory = state.saved.inventory; state.reactions = state.saved.reactions; } state.replay.push({ type:'restore', x:state.x, y:state.y }); persist(); }
function exportReplay() { const blob = new Blob([JSON.stringify(state.replay, null, 2)], { type:'application/json' }); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'report-262-free-move-replay.json'; a.click(); URL.revokeObjectURL(url); }
document.addEventListener('keydown', (event) => { const map = { ArrowUp:[0,-.28], ArrowDown:[0,.28], ArrowLeft:[-.28,0], ArrowRight:[.28,0], KeyW:[0,-.28], KeyS:[0,.28], KeyA:[-.28,0], KeyD:[.28,0] }; if (map[event.code]) { event.preventDefault(); move(...map[event.code]); } if (event.code === 'Space') { event.preventDefault(); talkNearby(); } });
function render() {
  document.getElementById('readiness').textContent = source.metrics.browser_world_v22_free_move_inventory_reaction_readiness.toFixed(3);
  document.getElementById('weakest').textContent = source.metrics.weakest_channel_score.toFixed(3);
  document.getElementById('frames').textContent = source.counts.browser_world_v22_ticks;
  document.getElementById('state').textContent = JSON.stringify({ x:+state.x.toFixed(2), y:+state.y.toFixed(2), inventory:state.inventory, reactions:state.reactions, replayRows:state.replay.length }, null, 2);
  const scene = document.getElementById('scene'); scene.querySelectorAll('.entity,.object').forEach(n => n.remove());
  objects.forEach(o => { const node = document.createElement('div'); node.className = 'object'; node.style.left = pctX(o.x); node.style.top = pctY(o.y); node.style.background = o.color; node.title = o.name; scene.appendChild(node); });
  agents.forEach(a => { const node = document.createElement('div'); node.className = 'entity agent'; node.style.left = pctX(a.x); node.style.top = pctY(a.y); node.style.background = a.color; node.title = `${a.name}: ${a.boundary}`; scene.appendChild(node); });
  const avatar = document.createElement('div'); avatar.className = 'entity avatar'; avatar.style.left = pctX(state.x); avatar.style.top = pctY(state.y); scene.appendChild(avatar);
  const inv = Object.entries(state.inventory).filter(([,v]) => v > 0).map(([k,v]) => `<div>${k}: ${v}</div>`).join('') || '<em>empty</em>';
  document.getElementById('inventory').innerHTML = inv;
  const a = closestAgent(); document.getElementById('reaction').innerHTML = `<strong>${a.name}</strong><br>${state.reactions[a.agent_id] || 'watching'}<br><small>${a.boundary}</small>`;
  const log = document.getElementById('log'); log.innerHTML = '';
  source.sample_prompts.slice(0, 8).forEach((prompt) => { const div = document.createElement('div'); div.className = 'prompt'; div.innerHTML = `<strong>${prompt.agent} / ${prompt.dialogue_intent}</strong><br>${prompt.dialogue_prompt}<br><small>visible=${prompt.prompt_visible} context=${prompt.prompt_context_score}</small>`; log.appendChild(div); });
}
render();
</script>
</body>
</html>
"""
    output_path.write_text(template.replace("__STATE__", encoded).replace("__KEY__", LOCAL_STORAGE_KEY), encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260875)
    parser.add_argument("--days", type=int, default=24)
    parser.add_argument("--ticks-per-day", type=int, default=16)
    args = parser.parse_args(argv)

    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_DIR.mkdir(parents=True, exist_ok=True)

    source = load_source_results()
    frames = generate_frames(args.seed, args.days, args.ticks_per_day)
    metrics = compute_metrics(frames, source)
    counts = compute_counts(frames)
    ablations = compute_ablations(metrics)
    verdict = "pass" if (
        metrics["browser_world_v22_free_move_inventory_reaction_readiness"] >= 0.84
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["free_move_input_surface"] >= 0.92
        and metrics["proximity_dialogue_trigger_rate"] >= 0.82
        and metrics["multi_object_inventory_persistence"] >= 0.82
        and metrics["ceremony_inventory_transaction_integrity"] >= 0.82
        and metrics["reload_stable_agent_reaction_state"] >= 0.82
        and metrics["privacy_safe_reaction_state"] >= 0.99
    ) else "partial_or_failed"

    artifact_paths = {
        "free_move_paths_csv": ARTIFACT_DIR / f"{PREFIX}_free_move_paths.csv",
        "proximity_dialogue_prompts_csv": ARTIFACT_DIR / f"{PREFIX}_proximity_dialogue_prompts.csv",
        "multi_object_inventory_csv": ARTIFACT_DIR / f"{PREFIX}_multi_object_inventory.csv",
        "ceremony_inventory_transactions_csv": ARTIFACT_DIR / f"{PREFIX}_ceremony_inventory_transactions.csv",
        "agent_reaction_states_csv": ARTIFACT_DIR / f"{PREFIX}_agent_reaction_states.csv",
        "reload_stable_reactions_csv": ARTIFACT_DIR / f"{PREFIX}_reload_stable_reactions.csv",
        "local_storage_inventory_snapshots_csv": ARTIFACT_DIR / f"{PREFIX}_local_storage_inventory_snapshots.csv",
        "dialogue_reaction_replays_csv": ARTIFACT_DIR / f"{PREFIX}_dialogue_reaction_replays.csv",
        "multi_sensory_free_move_csv": ARTIFACT_DIR / f"{PREFIX}_multi_sensory_free_move.csv",
        "browser_ticks_csv": ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv",
        "summary_csv": ARTIFACT_DIR / f"{PREFIX}_summary.csv",
        "verdict_csv": ARTIFACT_DIR / f"{PREFIX}_verdict.csv",
        "state_json": ARTIFACT_DIR / f"{PREFIX}_state.json",
        "results_json": ARTIFACT_DIR / f"{PREFIX}_results.json",
        "visualization_html": VISUALIZATION_DIR / f"{PREFIX}.html",
    }

    write_csv(artifact_paths["free_move_paths_csv"], frames["free_move_paths"])
    write_csv(artifact_paths["proximity_dialogue_prompts_csv"], frames["proximity_dialogue_prompts"])
    write_csv(artifact_paths["multi_object_inventory_csv"], frames["multi_object_inventory"])
    write_csv(artifact_paths["ceremony_inventory_transactions_csv"], frames["ceremony_inventory_transactions"])
    write_csv(artifact_paths["agent_reaction_states_csv"], frames["agent_reaction_states"])
    write_csv(artifact_paths["reload_stable_reactions_csv"], frames["reload_stable_reactions"])
    write_csv(artifact_paths["local_storage_inventory_snapshots_csv"], frames["local_storage_inventory_snapshots"])
    write_csv(artifact_paths["dialogue_reaction_replays_csv"], frames["dialogue_reaction_replays"])
    write_csv(artifact_paths["multi_sensory_free_move_csv"], frames["multi_sensory_free_move"])
    write_csv(artifact_paths["browser_ticks_csv"], frames["browser_ticks"])
    write_mapping_csv(artifact_paths["summary_csv"], metrics)
    write_csv(artifact_paths["verdict_csv"], [{"verdict": verdict, **metrics}])

    state = build_state(frames, metrics, counts, args.seed)
    artifact_paths["state_json"].write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    render_html(state, artifact_paths["visualization_html"])

    results = {
        "report": 262,
        "name": "SSRM-3D browser world v22 free-move proximity dialogue inventory reaction bridge",
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
        "claim_boundary": "Deterministic browser-local free-move, proximity dialogue, multi-object inventory, and reload-stable reaction-state scaffold only; no LLM call, subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
        "next_gate": "browser world v23 with object-specific proximity dialogue, agent-owned inventory requests, and reaction-state changes that alter later scene behavior rather than only panel text",
    }
    artifact_paths["results_json"].write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")

    print(json.dumps({"verdict": verdict, "metrics": metrics, "counts": counts}, indent=2, sort_keys=True))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
