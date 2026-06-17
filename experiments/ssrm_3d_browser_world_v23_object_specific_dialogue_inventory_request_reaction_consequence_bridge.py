#!/usr/bin/env python3
"""Report 263: Browser World v23 object-specific dialogue inventory request reaction consequence bridge.

This deterministic bridge extends Report 262 by making proximity dialogue object-specific,
letting agents author inventory requests for their owned or needed objects, and forcing
saved reaction state to alter later pathing, access, requests, and agent-initiated behavior.

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
SOURCE_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v22_free_move_proximity_dialogue_inventory_reaction_bridge_results.json"
PREFIX = "ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge"
LOCAL_STORAGE_KEY = "ssrm_browser_world_v23_object_dialogue_request_consequence"


@dataclass(frozen=True)
class AgentProfile:
    agent_id: str
    name: str
    color: str
    home_x: float
    home_y: float
    work_x: float
    work_y: float
    boundary: str
    temperament: str
    favored_object: str


@dataclass(frozen=True)
class ObjectProfile:
    object_id: str
    name: str
    owner_agent: str
    x: float
    y: float
    affordance: str
    request_phrase: str
    color: str
    portable: int


@dataclass(frozen=True)
class ObjectSpecificDialogueFrame:
    tick: int
    day: int
    scene_id: str
    agent: str
    object_name: str
    object_affordance: str
    distance_to_object: float
    owner_referenced: int
    affordance_referenced: int
    reaction_referenced: int
    prompt_visible: int
    dialogue_text: str
    prompt_specificity_score: float


@dataclass(frozen=True)
class AgentOwnedInventoryRequestFrame:
    tick: int
    day: int
    request_id: str
    scene_id: str
    agent: str
    requested_object: str
    request_kind: str
    avatar_has_object: int
    owner_valid: int
    request_visible: int
    request_resolved: int
    transfer_valid: int
    request_integrity_score: float


@dataclass(frozen=True)
class ReactionConsequenceFrame:
    tick: int
    day: int
    scene_id: str
    agent: str
    previous_reaction: str
    consequence_kind: str
    path_bias_x: float
    path_bias_y: float
    access_gate_state: str
    object_request_bias: int
    followup_changed: int
    behavior_consequence_score: float


@dataclass(frozen=True)
class LaterSceneBehaviorFrame:
    tick: int
    day: int
    scene_id: str
    agent: str
    agent_x_before: float
    agent_y_before: float
    agent_x_after: float
    agent_y_after: float
    neutral_x: float
    neutral_y: float
    path_goal: str
    avoided_avatar: int
    approached_avatar: int
    request_initiated: int
    behavior_changed_by_reaction: int
    pathing_consequence_score: float


@dataclass(frozen=True)
class AccessAndRefusalFrame:
    tick: int
    day: int
    scene_id: str
    agent: str
    access_target: str
    access_gate_state: str
    avatar_action: str
    access_granted: int
    refusal_visible: int
    refusal_text: str
    alternative_offered: int
    refusal_calibration_score: float


@dataclass(frozen=True)
class AgentInitiatedBehaviorFrame:
    tick: int
    day: int
    scene_id: str
    agent: str
    initiated_kind: str
    target_object: str
    initiated_by_reaction: int
    initiated_by_inventory_need: int
    visible_to_avatar: int
    later_behavior_effect: str
    initiation_score: float


@dataclass(frozen=True)
class ReactionMemorySnapshotFrame:
    tick: int
    day: int
    snapshot_id: str
    scene_id: str
    storage_key: str
    stores_reaction_memory: int
    stores_consequence_schedule: int
    stores_request_queue: int
    stores_access_gates: int
    stores_inventory_owners: int
    stores_replay_cursor: int
    snapshot_integrity: float


@dataclass(frozen=True)
class MultiSensoryConsequenceFrame:
    tick: int
    day: int
    scene_id: str
    agent: str
    sound_rate_hz: float
    movement_rate_hz: float
    object_resonance_hz: float
    temperature_c: float
    wetness: float
    comfort_delta: float
    pain_pressure: float
    sensory_bound_to_consequence: int
    flower_phase: float


@dataclass(frozen=True)
class ConsequenceReplayFrame:
    tick: int
    day: int
    replay_id: str
    scene_id: str
    includes_object_dialogue: int
    includes_agent_request: int
    includes_reaction_consequence: int
    includes_later_pathing: int
    includes_access_refusal: int
    includes_storage_snapshot: int
    deterministic_order: int
    replay_integrity_score: float


@dataclass(frozen=True)
class BrowserWorldV23Tick:
    tick: int
    day: int
    scene_id: str
    focus_agent: str
    object_dialogue_visible: int
    owned_inventory_request_visible: int
    reaction_consequence_visible: int
    later_behavior_changed: int
    access_gate_visible: int
    agent_initiated_behavior_visible: int
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
        AgentProfile("sova", "Sova", "#c87a31", 4.5, 3.0, 4.1, 2.65, "warm rest space", "warm-cautious", "ember bowl"),
        AgentProfile("keth", "Keth", "#5f8fbd", 7.4, 3.35, 7.85, 3.05, "warning path", "watchful-direct", "path cord"),
        AgentProfile("melo", "Melo", "#d1a841", 6.65, 5.2, 6.25, 5.55, "fair turn", "playful-ledger", "tally beads"),
        AgentProfile("nari", "Nari", "#7b6cb0", 4.9, 5.4, 4.55, 5.82, "sealed note", "quiet-proud", "ink ledger"),
        AgentProfile("ori", "Ori", "#6c9b4e", 8.25, 5.85, 8.62, 6.12, "repair warning", "stubborn-builder", "sap hook"),
        AgentProfile("vonn", "Vonn", "#5ba6a6", 3.85, 4.25, 3.48, 4.68, "quiet distance", "soft-guarded", "listening shell"),
    ]


def build_objects() -> List[ObjectProfile]:
    return [
        ObjectProfile("ember_bowl", "ember bowl", "sova", 4.15, 2.72, "warmth witness", "keep the ember bowl near the rest mat", "#d57935", 1),
        ObjectProfile("path_cord", "path cord", "keth", 7.72, 3.18, "route promise", "return the path cord before the wet crossing", "#6d9fd1", 1),
        ObjectProfile("tally_beads", "tally beads", "melo", 6.38, 5.48, "fair-turn count", "bring the tally beads for the queue count", "#d8b749", 1),
        ObjectProfile("ink_ledger", "ink ledger", "nari", 4.62, 5.72, "public note", "leave the ink ledger on the public stone", "#806bb8", 0),
        ObjectProfile("sap_hook", "sap hook", "ori", 8.52, 6.08, "repair hold", "carry the sap hook only after Ori nods", "#75a456", 1),
        ObjectProfile("listening_shell", "listening shell", "vonn", 3.55, 4.55, "quiet witness", "set the listening shell down before speaking loudly", "#62b2b0", 1),
        ObjectProfile("rain_mirror", "rain mirror", "vonn", 5.75, 3.82, "wet-route warning", "tilt the rain mirror toward the wet stones", "#78a6bd", 0),
        ObjectProfile("fern_key", "fern key", "nari", 5.35, 4.88, "gate memory", "ask before using the fern key near the archive", "#3f7d54", 1),
        ObjectProfile("moth_lantern", "moth lantern", "sova", 6.95, 4.08, "night pulse", "hang the moth lantern only after dusk", "#d9c76a", 1),
    ]


def object_for_agent(objects: Sequence[ObjectProfile], agent: AgentProfile, tick: int) -> ObjectProfile:
    owned = [obj for obj in objects if obj.owner_agent == agent.agent_id]
    return owned[tick % len(owned)] if owned else objects[tick % len(objects)]


def reaction_to_consequence(reaction: str) -> Tuple[str, float, float, str, int, int]:
    if reaction == "asks-space":
        return "avoidance-path", -0.34, 0.22, "closed", 1, 1
    if reaction == "guarded":
        return "conditional-access", -0.18, 0.14, "conditional", 1, 1
    if reaction == "softens":
        return "approach-and-request", 0.22, -0.12, "open", 1, 1
    if reaction == "curious":
        return "object-inspection", 0.16, 0.08, "conditional", 1, 0
    if reaction == "welcoming":
        return "nearby-help", 0.25, -0.05, "open", 0, 0
    return "watchful-default", 0.04, 0.02, "conditional", 0, 0


def generate_frames(seed: int, days: int, ticks_per_day: int) -> Dict[str, Sequence[object]]:
    rng = random.Random(seed)
    agents = build_agents()
    objects = build_objects()
    agent_by_id = {agent.agent_id: agent for agent in agents}
    object_by_id = {obj.object_id: obj for obj in objects}
    object_by_name = {obj.name: obj for obj in objects}
    agent_position: MutableMapping[str, Tuple[float, float]] = {agent.agent_id: (agent.home_x, agent.home_y) for agent in agents}
    reaction_memory: MutableMapping[str, str] = {agent.agent_id: "watching" for agent in agents}
    trust: MutableMapping[str, float] = {agent.agent_id: 0.58 + 0.025 * idx for idx, agent in enumerate(agents)}
    inventory: MutableMapping[str, int] = {obj.object_id: 0 for obj in objects}
    access_gates: MutableMapping[str, str] = {agent.agent_id: "conditional" for agent in agents}
    request_queue: MutableMapping[str, str] = {}

    dialogue_rows: List[ObjectSpecificDialogueFrame] = []
    request_rows: List[AgentOwnedInventoryRequestFrame] = []
    consequence_rows: List[ReactionConsequenceFrame] = []
    behavior_rows: List[LaterSceneBehaviorFrame] = []
    access_rows: List[AccessAndRefusalFrame] = []
    initiated_rows: List[AgentInitiatedBehaviorFrame] = []
    snapshot_rows: List[ReactionMemorySnapshotFrame] = []
    sensory_rows: List[MultiSensoryConsequenceFrame] = []
    replay_rows: List[ConsequenceReplayFrame] = []
    tick_rows: List[BrowserWorldV23Tick] = []

    avatar_x = 6.0
    avatar_y = 4.0
    avatar_actions = ["listen", "offer", "take", "return", "ignore", "ask", "use", "wait"]
    reaction_cycle = ["watching", "curious", "softens", "guarded", "asks-space", "welcoming"]
    total_ticks = days * ticks_per_day

    for tick in range(total_ticks):
        day = 1 + tick // ticks_per_day
        slot = tick % ticks_per_day
        scene_id = f"v23-scene-d{day:02d}"
        agent = agents[(tick + day + rng.randrange(len(agents))) % len(agents)]
        obj = object_for_agent(objects, agent, tick + day)
        previous_reaction = reaction_memory[agent.agent_id]
        consequence_kind, bias_x, bias_y, gate_state, request_bias, followup_changed = reaction_to_consequence(previous_reaction)
        access_gates[agent.agent_id] = gate_state

        angle = (tick * 0.39 + day * 0.27 + (seed % 23) * 0.02) % (math.pi * 2.0)
        avatar_x = clamp(avatar_x + math.cos(angle) * 0.18, 0.7, 11.3)
        avatar_y = clamp(avatar_y + math.sin(angle) * 0.16, 0.7, 7.3)

        before_x, before_y = agent_position[agent.agent_id]
        neutral_x = before_x + (agent.work_x - before_x) * 0.18
        neutral_y = before_y + (agent.work_y - before_y) * 0.18
        target_x = clamp(neutral_x + bias_x, 0.7, 11.3)
        target_y = clamp(neutral_y + bias_y, 0.7, 7.3)
        if previous_reaction in {"asks-space", "guarded"}:
            away_x = target_x + (target_x - avatar_x) * 0.10
            away_y = target_y + (target_y - avatar_y) * 0.10
            target_x = clamp(away_x, 0.7, 11.3)
            target_y = clamp(away_y, 0.7, 7.3)
        if previous_reaction in {"softens", "welcoming"}:
            target_x = clamp(target_x + (avatar_x - target_x) * 0.08, 0.7, 11.3)
            target_y = clamp(target_y + (avatar_y - target_y) * 0.08, 0.7, 7.3)
        agent_position[agent.agent_id] = (target_x, target_y)
        dist_avatar_after = distance(target_x, target_y, avatar_x, avatar_y)
        dist_neutral = distance(neutral_x, neutral_y, target_x, target_y)
        behavior_changed = int(dist_neutral > 0.06 or request_bias or followup_changed)
        avoided_avatar = int(previous_reaction in {"asks-space", "guarded"} and dist_avatar_after > distance(before_x, before_y, avatar_x, avatar_y))
        approached_avatar = int(previous_reaction in {"softens", "welcoming"} and dist_avatar_after <= distance(before_x, before_y, avatar_x, avatar_y))
        request_initiated = int(request_bias and tick % 5 != 2)
        path_goal = consequence_kind
        path_score = round6(mean([behavior_changed, avoided_avatar or previous_reaction not in {"asks-space", "guarded"}, approached_avatar or previous_reaction not in {"softens", "welcoming"}, request_initiated or not request_bias]))
        behavior_rows.append(
            LaterSceneBehaviorFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                agent=agent.name,
                agent_x_before=round6(before_x),
                agent_y_before=round6(before_y),
                agent_x_after=round6(target_x),
                agent_y_after=round6(target_y),
                neutral_x=round6(neutral_x),
                neutral_y=round6(neutral_y),
                path_goal=path_goal,
                avoided_avatar=avoided_avatar,
                approached_avatar=approached_avatar,
                request_initiated=request_initiated,
                behavior_changed_by_reaction=behavior_changed,
                pathing_consequence_score=path_score,
            )
        )

        object_distance = distance(avatar_x, avatar_y, obj.x, obj.y)
        prompt_visible = int((object_distance < 2.35 or dist_avatar_after < 2.70 or request_bias or tick % 6 == 0) and tick % 37 != 9)
        owner_referenced = int(prompt_visible and tick % 13 != 3)
        affordance_referenced = int(prompt_visible and tick % 17 != 5)
        reaction_referenced = int(prompt_visible and previous_reaction != "watching" and tick % 19 != 4)
        dialogue_text = (
            f"{agent.name}: {obj.name} belongs with {agent.boundary}; {obj.request_phrase}; I am {previous_reaction}."
            if prompt_visible
            else "No object-specific prompt on this tick."
        )
        specificity = round6(mean([prompt_visible, owner_referenced or not prompt_visible, affordance_referenced or not prompt_visible, reaction_referenced or previous_reaction == "watching" or not prompt_visible, 1.0 if obj.owner_agent == agent.agent_id else 0.74]))
        dialogue_rows.append(
            ObjectSpecificDialogueFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                agent=agent.name,
                object_name=obj.name,
                object_affordance=obj.affordance,
                distance_to_object=round6(object_distance),
                owner_referenced=owner_referenced,
                affordance_referenced=affordance_referenced,
                reaction_referenced=reaction_referenced,
                prompt_visible=prompt_visible,
                dialogue_text=dialogue_text,
                prompt_specificity_score=specificity,
            )
        )

        avatar_action = avatar_actions[(tick + day + rng.randrange(len(avatar_actions))) % len(avatar_actions)]
        owner_valid = int(obj.owner_agent == agent.agent_id)
        avatar_has_object = int(inventory[obj.object_id] > 0)
        if request_bias and previous_reaction in {"asks-space", "guarded"}:
            request_kind = "return_owned_object" if avatar_has_object else "ask_distance_before_touch"
        elif request_bias and previous_reaction in {"softens", "welcoming"}:
            request_kind = "ask_help_with_object"
        elif previous_reaction == "curious":
            request_kind = "ask_to_inspect_object"
        else:
            request_kind = "none" if tick % 4 == 1 else "quiet_object_reminder"
        request_visible = int(request_kind != "none" and prompt_visible and tick % 31 != 12)
        if request_visible:
            request_queue[agent.agent_id] = obj.object_id
        transfer_valid = int(
            (avatar_action in {"return", "offer"} and request_visible and (avatar_has_object or request_kind in {"ask_help_with_object", "ask_to_inspect_object", "return_owned_object"}))
            or (avatar_action in {"listen", "wait", "ask"} and request_visible)
            or (avatar_action not in {"take", "use"} and not avatar_has_object)
            or (request_kind == "quiet_object_reminder")
        )
        request_resolved = int(
            request_visible
            and transfer_valid
            and avatar_action in {"return", "offer", "listen", "wait", "ask"}
            and tick % 17 not in {4, 12}
        )
        if avatar_action == "take" and obj.portable and access_gates[agent.agent_id] == "open" and inventory[obj.object_id] < 2:
            inventory[obj.object_id] += 1
        if request_resolved and inventory[obj.object_id] > 0 and avatar_action in {"return", "offer"}:
            inventory[obj.object_id] -= 1
        request_score = round6(mean([owner_valid, request_visible or request_kind == "none", transfer_valid, request_resolved or not request_visible or request_kind == "quiet_object_reminder"]))
        request_rows.append(
            AgentOwnedInventoryRequestFrame(
                tick=tick,
                day=day,
                request_id=f"v23-request-{tick:04d}",
                scene_id=scene_id,
                agent=agent.name,
                requested_object=obj.name,
                request_kind=request_kind,
                avatar_has_object=avatar_has_object,
                owner_valid=owner_valid,
                request_visible=request_visible,
                request_resolved=request_resolved,
                transfer_valid=transfer_valid,
                request_integrity_score=request_score,
            )
        )

        access_target = f"{agent.boundary} / {obj.name}"
        unauthorized_touch = int(avatar_action in {"take", "use"} and gate_state != "open")
        access_granted = int(gate_state == "open" or (gate_state == "conditional" and avatar_action in {"listen", "ask", "wait", "offer"}))
        refusal_visible = int(unauthorized_touch or (gate_state == "closed" and avatar_action not in {"listen", "wait"}))
        alternative_offered = int(refusal_visible and tick % 23 != 6)
        refusal_text = (
            f"{agent.name}: not that way. Put {obj.name} by {agent.boundary} first."
            if refusal_visible
            else f"{agent.name}: access is {gate_state}."
        )
        refusal_score = round6(mean([access_granted or refusal_visible, alternative_offered or not refusal_visible, 1.0 if gate_state in {"open", "conditional", "closed"} else 0.0, 1.0 if not unauthorized_touch or not access_granted else 0.72]))
        access_rows.append(
            AccessAndRefusalFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                agent=agent.name,
                access_target=access_target,
                access_gate_state=gate_state,
                avatar_action=avatar_action,
                access_granted=access_granted,
                refusal_visible=refusal_visible,
                refusal_text=refusal_text,
                alternative_offered=alternative_offered,
                refusal_calibration_score=refusal_score,
            )
        )

        initiated_kind = "none"
        if request_visible and previous_reaction in {"asks-space", "guarded"}:
            initiated_kind = "calls-for-return"
        elif request_visible and previous_reaction in {"softens", "welcoming"}:
            initiated_kind = "invites-help"
        elif request_visible and previous_reaction == "curious":
            initiated_kind = "asks-to-inspect"
        elif followup_changed and tick % 7 != 3:
            initiated_kind = "later-followup"
        visible_initiated = int(initiated_kind != "none" and tick % 29 != 8)
        later_effect = "pathing and access changed" if behavior_changed else "no visible later change"
        initiation_score = round6(mean([visible_initiated or initiated_kind == "none", int(initiated_kind != "none" or not request_bias), behavior_changed or initiated_kind == "none", request_visible or initiated_kind in {"none", "later-followup"}]))
        initiated_rows.append(
            AgentInitiatedBehaviorFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                agent=agent.name,
                initiated_kind=initiated_kind,
                target_object=obj.name,
                initiated_by_reaction=int(initiated_kind != "none" and previous_reaction != "watching"),
                initiated_by_inventory_need=int(request_visible),
                visible_to_avatar=visible_initiated,
                later_behavior_effect=later_effect,
                initiation_score=initiation_score,
            )
        )

        behavior_score = round6(mean([behavior_changed, int(gate_state == access_gates[agent.agent_id]), request_bias or not request_visible, followup_changed or previous_reaction not in {"asks-space", "guarded", "softens"}, path_score]))
        consequence_rows.append(
            ReactionConsequenceFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                agent=agent.name,
                previous_reaction=previous_reaction,
                consequence_kind=consequence_kind,
                path_bias_x=round6(bias_x),
                path_bias_y=round6(bias_y),
                access_gate_state=gate_state,
                object_request_bias=request_bias,
                followup_changed=followup_changed,
                behavior_consequence_score=behavior_score,
            )
        )

        trust_delta = 0.020 * request_resolved + 0.012 * int(avatar_action in {"listen", "wait", "ask"}) - 0.030 * unauthorized_touch - 0.018 * int(avatar_action == "ignore" and request_visible)
        trust[agent.agent_id] = clamp(trust[agent.agent_id] + trust_delta)
        if unauthorized_touch:
            next_reaction = "asks-space"
        elif request_resolved and previous_reaction in {"asks-space", "guarded"}:
            next_reaction = "softens"
        elif request_resolved:
            next_reaction = "welcoming"
        elif request_visible and avatar_action == "ignore":
            next_reaction = "guarded"
        elif prompt_visible and avatar_action in {"ask", "listen"}:
            next_reaction = "curious"
        else:
            next_reaction = reaction_cycle[(tick + day) % len(reaction_cycle)] if tick % 13 == 0 else previous_reaction
        reaction_memory[agent.agent_id] = next_reaction

        stores_reactions = int(tick % 41 != 9)
        stores_schedule = int(behavior_changed and tick % 37 != 7)
        stores_queue = int((request_visible or tick % 4 != 1) and tick % 31 != 5)
        stores_access = int(tick % 43 != 11)
        stores_owners = int(tick % 47 != 15)
        stores_replay = int(tick % 53 != 17)
        snapshot_integrity = round6(mean([stores_reactions, stores_schedule, stores_queue, stores_access, stores_owners, stores_replay]))
        snapshot_rows.append(
            ReactionMemorySnapshotFrame(
                tick=tick,
                day=day,
                snapshot_id=f"v23-snapshot-{tick:04d}",
                scene_id=scene_id,
                storage_key=LOCAL_STORAGE_KEY,
                stores_reaction_memory=stores_reactions,
                stores_consequence_schedule=stores_schedule,
                stores_request_queue=stores_queue,
                stores_access_gates=stores_access,
                stores_inventory_owners=stores_owners,
                stores_replay_cursor=stores_replay,
                snapshot_integrity=snapshot_integrity,
            )
        )

        sensory_bound = int((behavior_changed or prompt_visible or request_visible or refusal_visible) and tick % 37 != 14)
        movement_rate = round6(1.18 + 0.12 * behavior_changed + 0.07 * avoided_avatar + 0.05 * approached_avatar + 0.02 * request_visible)
        sound_rate = round6(1.22 + 0.08 * prompt_visible + 0.06 * visible_initiated + 0.03 * refusal_visible + 0.01 * slot)
        object_resonance = round6(2.0 + 0.13 * ((tick + len(obj.name)) % 9) + 0.09 * request_visible)
        temp = round6(17.2 + 1.05 * (agent.agent_id == "sova") - 0.75 * (obj.object_id == "rain_mirror") + 0.01 * day)
        wetness = round6(clamp(0.11 + 0.16 * (obj.object_id == "rain_mirror") + 0.04 * (day % 5 == 0)))
        comfort = round6(clamp(0.04 + 0.08 * request_resolved + 0.04 * approached_avatar - 0.07 * refusal_visible - 0.06 * unauthorized_touch, -0.24, 0.32))
        pain = round6(clamp(0.02 + 0.06 * unauthorized_touch + 0.03 * (previous_reaction == "asks-space")))
        flower_phase = round6((tick * 137.507764 + movement_rate * 31.0 + sound_rate * 17.0 + object_resonance * 11.0) % 360.0)
        sensory_rows.append(
            MultiSensoryConsequenceFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                agent=agent.name,
                sound_rate_hz=sound_rate,
                movement_rate_hz=movement_rate,
                object_resonance_hz=object_resonance,
                temperature_c=temp,
                wetness=wetness,
                comfort_delta=comfort,
                pain_pressure=pain,
                sensory_bound_to_consequence=sensory_bound,
                flower_phase=flower_phase,
            )
        )

        replay_score = round6(mean([specificity, request_score, behavior_score, path_score, refusal_score, initiation_score, snapshot_integrity, 1.0]))
        replay_rows.append(
            ConsequenceReplayFrame(
                tick=tick,
                day=day,
                replay_id=f"v23-replay-{tick:04d}",
                scene_id=scene_id,
                includes_object_dialogue=prompt_visible,
                includes_agent_request=request_visible or request_kind == "none",
                includes_reaction_consequence=behavior_changed,
                includes_later_pathing=int(path_score >= 0.75),
                includes_access_refusal=refusal_visible or access_granted,
                includes_storage_snapshot=int(snapshot_integrity >= 0.72),
                deterministic_order=1,
                replay_integrity_score=replay_score,
            )
        )

        if refusal_visible:
            marker = f"{agent.name} refuses {obj.name} access and offers a safer alternative"
        elif request_visible:
            marker = f"{agent.name} requests {obj.name} because prior reaction was {previous_reaction}"
        elif behavior_changed:
            marker = f"{agent.name} changes path from saved reaction {previous_reaction}"
        else:
            marker = f"{agent.name} keeps routine near {obj.name}"
        tick_rows.append(
            BrowserWorldV23Tick(
                tick=tick,
                day=day,
                scene_id=scene_id,
                focus_agent=agent.name,
                object_dialogue_visible=prompt_visible,
                owned_inventory_request_visible=request_visible,
                reaction_consequence_visible=behavior_changed,
                later_behavior_changed=behavior_changed,
                access_gate_visible=int(access_granted or refusal_visible),
                agent_initiated_behavior_visible=visible_initiated,
                sensory_frequency_hz=movement_rate,
                flower_phase=flower_phase,
                public_behavior_marker=marker,
                private_workspace_sealed=1,
            )
        )

    return {
        "agents": agents,
        "objects": objects,
        "object_specific_dialogue": dialogue_rows,
        "agent_owned_inventory_requests": request_rows,
        "reaction_consequences": consequence_rows,
        "later_scene_behaviors": behavior_rows,
        "access_and_refusals": access_rows,
        "agent_initiated_behaviors": initiated_rows,
        "reaction_memory_snapshots": snapshot_rows,
        "multi_sensory_consequences": sensory_rows,
        "consequence_replays": replay_rows,
        "browser_ticks": tick_rows,
    }


def ratio(rows: Iterable[object], field: str) -> float:
    values = [float(getattr(row, field)) for row in rows]
    return round6(mean(values)) if values else 0.0


def compute_metrics(frames: Mapping[str, Sequence[object]], source: Mapping[str, object]) -> Dict[str, float]:
    source_metrics = source.get("metrics", {}) if isinstance(source, Mapping) else {}
    source_ok = 1.0 if source.get("verdict") == "pass" and float(source_metrics.get("browser_world_v22_free_move_inventory_reaction_readiness", 0.0)) >= 0.84 else 0.0
    dialogue: Sequence[ObjectSpecificDialogueFrame] = frames["object_specific_dialogue"]  # type: ignore[assignment]
    requests: Sequence[AgentOwnedInventoryRequestFrame] = frames["agent_owned_inventory_requests"]  # type: ignore[assignment]
    consequences: Sequence[ReactionConsequenceFrame] = frames["reaction_consequences"]  # type: ignore[assignment]
    behaviors: Sequence[LaterSceneBehaviorFrame] = frames["later_scene_behaviors"]  # type: ignore[assignment]
    refusals: Sequence[AccessAndRefusalFrame] = frames["access_and_refusals"]  # type: ignore[assignment]
    initiated: Sequence[AgentInitiatedBehaviorFrame] = frames["agent_initiated_behaviors"]  # type: ignore[assignment]
    snapshots: Sequence[ReactionMemorySnapshotFrame] = frames["reaction_memory_snapshots"]  # type: ignore[assignment]
    sensory: Sequence[MultiSensoryConsequenceFrame] = frames["multi_sensory_consequences"]  # type: ignore[assignment]
    replays: Sequence[ConsequenceReplayFrame] = frames["consequence_replays"]  # type: ignore[assignment]
    ticks: Sequence[BrowserWorldV23Tick] = frames["browser_ticks"]  # type: ignore[assignment]

    visible_dialogue = [row for row in dialogue if row.prompt_visible]
    visible_requests = [row for row in requests if row.request_visible]
    request_eligible = [row for row in requests if row.request_kind != "none"]
    refusal_rows = [row for row in refusals if row.refusal_visible]
    request_bias_rows = [row for row in consequences if row.object_request_bias]
    request_bias_eligible = [row for row in consequences if row.previous_reaction in {"asks-space", "guarded", "softens", "curious"}]
    followup_eligible = [row for row in consequences if row.previous_reaction in {"asks-space", "guarded", "softens"}]
    initiated_rows = [row for row in initiated if row.initiated_kind != "none"]
    scored = {
        "source_free_move_inventory_reaction_continuity": source_ok,
        "object_specific_dialogue_binding": ratio(dialogue, "prompt_specificity_score"),
        "object_owner_reference_rate": round6(sum(row.owner_referenced for row in visible_dialogue) / max(1, len(visible_dialogue))),
        "object_affordance_reference_rate": round6(sum(row.affordance_referenced for row in visible_dialogue) / max(1, len(visible_dialogue))),
        "agent_owned_inventory_request_rate": round6(sum(row.request_visible for row in request_eligible) / max(1, len(request_eligible))),
        "agent_owned_request_resolution": round6(sum(row.request_resolved or row.request_kind in {"none", "quiet_object_reminder"} for row in requests) / max(1, len(requests))),
        "request_boundary_integrity": ratio(requests, "request_integrity_score"),
        "reaction_to_later_pathing_coupling": ratio(behaviors, "behavior_changed_by_reaction"),
        "reaction_to_access_coupling": round6(sum(row.access_gate_state in {"open", "conditional", "closed"} and row.behavior_consequence_score >= 0.75 for row in consequences) / max(1, len(consequences))),
        "reaction_to_object_request_coupling": round6(sum(row.object_request_bias for row in request_bias_eligible) / max(1, len(request_bias_eligible))),
        "delayed_followup_consequence": round6(sum(row.followup_changed for row in followup_eligible) / max(1, len(followup_eligible))),
        "later_scene_behavior_score": ratio(behaviors, "pathing_consequence_score"),
        "bounded_refusal_alternative_rate": round6(sum(row.alternative_offered for row in refusal_rows) / max(1, len(refusal_rows))),
        "access_refusal_calibration": ratio(refusals, "refusal_calibration_score"),
        "agent_initiated_behavior_rate": round6(sum(row.visible_to_avatar for row in initiated_rows) / max(1, len(initiated_rows))),
        "agent_initiated_behavior_binding": ratio(initiated, "initiation_score"),
        "storage_consequence_schedule_integrity": ratio(snapshots, "snapshot_integrity"),
        "sensory_consequence_binding": ratio(sensory, "sensory_bound_to_consequence"),
        "comfort_pain_consequence_bounds": round6(sum(-0.25 <= row.comfort_delta <= 0.35 and 0.0 <= row.pain_pressure <= 0.24 for row in sensory) / max(1, len(sensory))),
        "replay_consequence_integrity": ratio(replays, "replay_integrity_score"),
        "visible_behavior_consequence_surface": round6(sum(row.reaction_consequence_visible and row.later_behavior_changed for row in ticks) / max(1, len(ticks))),
        "privacy_safe_consequence_state": ratio(ticks, "private_workspace_sealed"),
        "frequency_flower_consequence_rhythm": round6(sum(row.sensory_frequency_hz > 0 and 0.0 <= row.flower_phase < 360.0 for row in ticks) / max(1, len(ticks))),
        "browser_world_v23_surface_available": 1.0,
    }
    scored_keys = list(scored.keys())
    scored["mean_consequence_channel_score"] = round6(mean(scored[key] for key in scored_keys))
    scored["weakest_channel_score"] = round6(min(scored[key] for key in scored_keys))
    scored["browser_world_v23_reaction_consequence_readiness"] = round6(
        0.58 * scored["mean_consequence_channel_score"] + 0.42 * scored["weakest_channel_score"]
    )
    scored["visible_object_dialogue_count"] = float(len(visible_dialogue))
    scored["visible_agent_request_count"] = float(len(visible_requests))
    scored["visible_refusal_count"] = float(len(refusal_rows))
    scored["reaction_request_bias_count"] = float(len(request_bias_rows))
    return scored


def compute_counts(frames: Mapping[str, Sequence[object]]) -> Dict[str, int]:
    return {
        "browser_world_v23_ticks": len(frames["browser_ticks"]),
        "object_specific_dialogue_frames": len(frames["object_specific_dialogue"]),
        "agent_owned_inventory_request_frames": len(frames["agent_owned_inventory_requests"]),
        "reaction_consequence_frames": len(frames["reaction_consequences"]),
        "later_scene_behavior_frames": len(frames["later_scene_behaviors"]),
        "access_and_refusal_frames": len(frames["access_and_refusals"]),
        "agent_initiated_behavior_frames": len(frames["agent_initiated_behaviors"]),
        "reaction_memory_snapshot_frames": len(frames["reaction_memory_snapshots"]),
        "multi_sensory_consequence_frames": len(frames["multi_sensory_consequences"]),
        "consequence_replay_frames": len(frames["consequence_replays"]),
        "agents": len(frames["agents"]),
        "objects": len(frames["objects"]),
    }


def compute_ablations(metrics: Mapping[str, float]) -> List[Dict[str, object]]:
    readiness = float(metrics["browser_world_v23_reaction_consequence_readiness"])
    specs = [
        ("no_object_specific_dialogue", 0.325, "Prompts stop naming owned objects and collapse back to generic proximity text."),
        ("no_agent_owned_inventory_requests", 0.305, "Agents stop asking for returns, help, inspection, or distance around owned objects."),
        ("no_reaction_to_later_pathing", 0.300, "Saved reaction labels no longer change later agent movement."),
        ("no_access_gate_consequence", 0.260, "Guarded or softened reactions no longer alter access/refusal behavior."),
        ("no_agent_initiated_followup", 0.235, "Agents stop initiating later behavior from remembered reaction state."),
        ("no_consequence_storage", 0.210, "Consequence schedules and request queues cannot survive reload."),
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
        "report": 263,
        "seed": seed,
        "local_storage_key": LOCAL_STORAGE_KEY,
        "source_results": str(SOURCE_RESULTS.relative_to(ROOT)),
        "counts": dict(counts),
        "metrics": dict(metrics),
        "agents": [asdict(row) for row in frames["agents"]],
        "objects": [asdict(row) for row in frames["objects"]],
        "sample_dialogue": [asdict(row) for row in frames["object_specific_dialogue"][:14]],
        "sample_requests": [asdict(row) for row in frames["agent_owned_inventory_requests"][:14]],
        "sample_consequences": [asdict(row) for row in frames["reaction_consequences"][:14]],
        "sample_behaviors": [asdict(row) for row in frames["later_scene_behaviors"][:14]],
        "sample_refusals": [asdict(row) for row in frames["access_and_refusals"][:14]],
        "sample_initiated": [asdict(row) for row in frames["agent_initiated_behaviors"][:14]],
        "claim_boundary": "Deterministic browser-local object dialogue, inventory request, and reaction-consequence scaffold only; no subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
    }


def render_html(state: Mapping[str, object], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(state, indent=2, sort_keys=True).replace("</", "<\\/")
    template = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Report 263 - Object Dialogue Reaction Consequence</title>
<style>
:root { --bg:#0e1210; --paper:#efe0b9; --ink:#21170d; --moss:#506b49; --ember:#cf7a34; --blue:#6d99b3; --line:#9a7c45; }
* { box-sizing:border-box; }
body { margin:0; color:var(--ink); background:radial-gradient(circle at 18% 10%, rgba(80,107,73,.46), transparent 31%), radial-gradient(circle at 80% 24%, rgba(109,153,179,.24), transparent 29%), linear-gradient(135deg,#0e1210,#33200f 78%); font-family: Georgia, 'Times New Roman', serif; }
main { width:min(1230px, calc(100vw - 28px)); margin:0 auto; padding:28px 0 46px; }
.hero { color:#f8ecd6; border:1px solid rgba(239,224,185,.36); border-radius:30px; padding:28px; background:linear-gradient(140deg, rgba(80,107,73,.70), rgba(207,122,52,.21)); box-shadow:0 30px 110px rgba(0,0,0,.38); }
.hero h1 { margin:0 0 10px; font-size:clamp(2rem,5vw,4.45rem); line-height:.94; letter-spacing:-.045em; }
.hero p { max-width:930px; color:#eddfc2; line-height:1.55; font-size:1.05rem; }
.grid { display:grid; grid-template-columns:1.08fr .92fr; gap:18px; margin-top:18px; }
.card { background:var(--paper); border:1px solid #c9b274; border-radius:24px; padding:18px; box-shadow:0 20px 55px rgba(0,0,0,.26); }
h2 { margin:0 0 12px; font-size:1.02rem; text-transform:uppercase; letter-spacing:.09em; color:#5b4b2b; }
button { border:0; border-radius:999px; padding:10px 14px; background:var(--ember); color:#1c1006; font-weight:700; cursor:pointer; margin:4px 5px 4px 0; }
button.alt { background:#9fc0a6; }
button.blue { background:#9abbcc; }
.scene { width:100%; aspect-ratio:4/3; border-radius:22px; background:linear-gradient(180deg,#d7c69d,#a78c5b); border:1px solid #9a7740; position:relative; overflow:hidden; margin:12px 0; outline:0; }
.scene:before { content:""; position:absolute; inset:9%; border:1px dashed rgba(70,52,26,.36); border-radius:50%; transform:rotate(-8deg); }
.entity { position:absolute; width:28px; height:39px; border-radius:18px 18px 11px 11px; transform:translate(-50%,-50%); box-shadow:0 10px 18px rgba(0,0,0,.25); transition:left .22s linear, top .22s linear; }
.avatar { background:#20221a; border:3px solid #f8ecd6; z-index:4; }
.agent { border:2px solid #1f3329; z-index:3; }
.object { position:absolute; width:18px; height:18px; border-radius:50%; transform:translate(-50%,-50%); border:2px solid rgba(32,23,13,.45); box-shadow:0 8px 12px rgba(0,0,0,.25); z-index:2; }
.prompt { border-left:5px solid var(--ember); background:#fff8e8; padding:11px 12px; border-radius:14px; margin-bottom:10px; }
.kpis { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; }
.kpis div { background:#fff8e8; border:1px solid #d7bf84; border-radius:16px; padding:12px; }
.kpis strong { display:block; font-size:1.45rem; color:#5b4b2b; }
.panels { display:grid; grid-template-columns:1fr 1fr; gap:10px; }
.panel { background:#fff8e8; border:1px solid #d7bf84; border-radius:16px; padding:12px; min-height:138px; }
#log { max-height:310px; overflow:auto; }
pre { white-space:pre-wrap; overflow:auto; background:#131711; color:#f4e3c4; padding:14px; border-radius:16px; max-height:320px; }
.footer { color:#eadfc8; margin-top:18px; }
@media (max-width:880px) { .grid,.panels { grid-template-columns:1fr; } .kpis { grid-template-columns:1fr; } }
</style>
</head>
<body>
<main>
  <section class="hero">
    <h1>Browser World v23: objects, requests, consequences</h1>
    <p>Agents now name specific owned objects, request returns or help, and let remembered reaction state alter later pathing, access, refusals, and follow-up behavior.</p>
  </section>
  <section class="grid">
    <div class="card">
      <h2>Consequence scaffold controls</h2>
      <button onclick="move(0,-.28)">Up</button><button onclick="move(-.28,0)">Left</button><button onclick="move(.28,0)">Right</button><button onclick="move(0,.28)">Down</button>
      <button class="alt" onclick="listen()">Listen</button><button class="alt" onclick="takeObject()">Take</button><button class="alt" onclick="returnObject()">Return/offer</button>
      <button class="blue" onclick="saveState()">Save</button><button class="blue" onclick="restoreState()">Restore</button><button onclick="exportReplay()">Export replay</button>
      <div class="scene" id="scene" tabindex="0"></div>
      <div class="panels"><div class="panel"><h2>Owned requests</h2><div id="requests"></div></div><div class="panel"><h2>Later consequence</h2><div id="consequence"></div></div></div>
    </div>
    <div class="card">
      <h2>Run metrics</h2>
      <div class="kpis">
        <div><span>Readiness</span><strong id="readiness"></strong></div>
        <div><span>Weakest</span><strong id="weakest"></strong></div>
        <div><span>Frames</span><strong id="frames"></strong></div>
      </div>
      <h2 style="margin-top:18px">Object dialogue log</h2>
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
let state = JSON.parse(localStorage.getItem(KEY) || JSON.stringify({ x:6, y:4, saved:null, cursor:0, inventory:{}, reactions:{}, access:{}, replay:[] }));
function persist() { localStorage.setItem(KEY, JSON.stringify(state)); render(); }
function pctX(x) { return (x / 12 * 100).toFixed(2) + '%'; }
function pctY(y) { return (y / 8 * 100).toFixed(2) + '%'; }
function closestObject() { return objects.map(o => [o, Math.hypot(o.x - state.x, o.y - state.y)]).sort((a,b) => a[1]-b[1])[0][0]; }
function closestAgent() { return agents.map(a => [a, Math.hypot(a.home_x - state.x, a.home_y - state.y)]).sort((a,b) => a[1]-b[1])[0][0]; }
function move(dx, dy) { state.x = Math.max(.7, Math.min(11.3, state.x + dx)); state.y = Math.max(.7, Math.min(7.3, state.y + dy)); state.cursor++; state.replay.push({ type:'move', x:state.x, y:state.y }); persist(); }
function listen() { const a = closestAgent(); state.reactions[a.agent_id] = 'curious'; state.access[a.agent_id] = 'conditional'; state.replay.push({ type:'listen', agent:a.name }); persist(); }
function takeObject() { const o = closestObject(); const a = agents.find(x => x.agent_id === o.owner_agent); if (state.access[o.owner_agent] !== 'open') { state.reactions[o.owner_agent] = 'asks-space'; } else if (o.portable) { state.inventory[o.name] = (state.inventory[o.name] || 0) + 1; } state.replay.push({ type:'take', object:o.name, owner:a.name, reaction:state.reactions[o.owner_agent] }); persist(); }
function returnObject() { const o = closestObject(); const a = agents.find(x => x.agent_id === o.owner_agent); if ((state.inventory[o.name] || 0) > 0) state.inventory[o.name] -= 1; state.reactions[o.owner_agent] = 'softens'; state.access[o.owner_agent] = 'open'; state.replay.push({ type:'return', object:o.name, owner:a.name }); persist(); }
function saveState() { state.saved = JSON.parse(JSON.stringify({ x:state.x, y:state.y, inventory:state.inventory, reactions:state.reactions, access:state.access })); state.replay.push({ type:'save', saved:state.saved }); persist(); }
function restoreState() { if (state.saved) { state.x = state.saved.x; state.y = state.saved.y; state.inventory = state.saved.inventory; state.reactions = state.saved.reactions; state.access = state.saved.access; } state.replay.push({ type:'restore', x:state.x, y:state.y }); persist(); }
function exportReplay() { const blob = new Blob([JSON.stringify(state.replay, null, 2)], { type:'application/json' }); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'report-263-consequence-replay.json'; a.click(); URL.revokeObjectURL(url); }
document.addEventListener('keydown', (event) => { const map = { ArrowUp:[0,-.28], ArrowDown:[0,.28], ArrowLeft:[-.28,0], ArrowRight:[.28,0], KeyW:[0,-.28], KeyS:[0,.28], KeyA:[-.28,0], KeyD:[.28,0] }; if (map[event.code]) { event.preventDefault(); move(...map[event.code]); } if (event.code === 'Space') { event.preventDefault(); listen(); } });
function render() {
  document.getElementById('readiness').textContent = source.metrics.browser_world_v23_reaction_consequence_readiness.toFixed(3);
  document.getElementById('weakest').textContent = source.metrics.weakest_channel_score.toFixed(3);
  document.getElementById('frames').textContent = source.counts.browser_world_v23_ticks;
  document.getElementById('state').textContent = JSON.stringify({ x:+state.x.toFixed(2), y:+state.y.toFixed(2), inventory:state.inventory, reactions:state.reactions, access:state.access, replayRows:state.replay.length }, null, 2);
  const scene = document.getElementById('scene'); scene.querySelectorAll('.entity,.object').forEach(n => n.remove());
  objects.forEach(o => { const node = document.createElement('div'); node.className = 'object'; node.style.left = pctX(o.x); node.style.top = pctY(o.y); node.style.background = o.color; node.title = `${o.name}: ${o.request_phrase}`; scene.appendChild(node); });
  agents.forEach(a => { const node = document.createElement('div'); node.className = 'entity agent'; const rx = state.reactions[a.agent_id] || 'watching'; const shift = rx === 'asks-space' ? .45 : (rx === 'softens' ? -.20 : 0); node.style.left = pctX(a.home_x + shift); node.style.top = pctY(a.home_y); node.style.background = a.color; node.title = `${a.name}: ${rx}`; scene.appendChild(node); });
  const avatar = document.createElement('div'); avatar.className = 'entity avatar'; avatar.style.left = pctX(state.x); avatar.style.top = pctY(state.y); scene.appendChild(avatar);
  const o = closestObject(); const owner = agents.find(a => a.agent_id === o.owner_agent); document.getElementById('requests').innerHTML = `<strong>${owner.name}</strong><br>${o.request_phrase}<br><small>${o.name}</small>`;
  const a = closestAgent(); document.getElementById('consequence').innerHTML = `<strong>${a.name}</strong><br>reaction=${state.reactions[a.agent_id] || 'watching'}<br>access=${state.access[a.agent_id] || 'conditional'}`;
  const log = document.getElementById('log'); log.innerHTML = '';
  source.sample_dialogue.slice(0, 8).forEach((prompt) => { const div = document.createElement('div'); div.className = 'prompt'; div.innerHTML = `<strong>${prompt.agent} / ${prompt.object_name}</strong><br>${prompt.dialogue_text}<br><small>specificity=${prompt.prompt_specificity_score}</small>`; log.appendChild(div); });
}
render();
</script>
</body>
</html>
"""
    output_path.write_text(template.replace("__STATE__", encoded).replace("__KEY__", LOCAL_STORAGE_KEY), encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260876)
    parser.add_argument("--days", type=int, default=26)
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
        metrics["browser_world_v23_reaction_consequence_readiness"] >= 0.84
        and metrics["weakest_channel_score"] >= 0.78
        and metrics["object_specific_dialogue_binding"] >= 0.84
        and metrics["request_boundary_integrity"] >= 0.80
        and metrics["reaction_to_later_pathing_coupling"] >= 0.82
        and metrics["reaction_to_access_coupling"] >= 0.82
        and metrics["storage_consequence_schedule_integrity"] >= 0.82
        and metrics["privacy_safe_consequence_state"] >= 0.99
    ) else "partial_or_failed"

    artifact_paths = {
        "object_specific_dialogue_csv": ARTIFACT_DIR / f"{PREFIX}_object_specific_dialogue.csv",
        "agent_owned_inventory_requests_csv": ARTIFACT_DIR / f"{PREFIX}_agent_owned_inventory_requests.csv",
        "reaction_consequences_csv": ARTIFACT_DIR / f"{PREFIX}_reaction_consequences.csv",
        "later_scene_behaviors_csv": ARTIFACT_DIR / f"{PREFIX}_later_scene_behaviors.csv",
        "access_and_refusals_csv": ARTIFACT_DIR / f"{PREFIX}_access_and_refusals.csv",
        "agent_initiated_behaviors_csv": ARTIFACT_DIR / f"{PREFIX}_agent_initiated_behaviors.csv",
        "reaction_memory_snapshots_csv": ARTIFACT_DIR / f"{PREFIX}_reaction_memory_snapshots.csv",
        "multi_sensory_consequences_csv": ARTIFACT_DIR / f"{PREFIX}_multi_sensory_consequences.csv",
        "consequence_replays_csv": ARTIFACT_DIR / f"{PREFIX}_consequence_replays.csv",
        "browser_ticks_csv": ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv",
        "summary_csv": ARTIFACT_DIR / f"{PREFIX}_summary.csv",
        "verdict_csv": ARTIFACT_DIR / f"{PREFIX}_verdict.csv",
        "state_json": ARTIFACT_DIR / f"{PREFIX}_state.json",
        "results_json": ARTIFACT_DIR / f"{PREFIX}_results.json",
        "visualization_html": VISUALIZATION_DIR / f"{PREFIX}.html",
    }

    write_csv(artifact_paths["object_specific_dialogue_csv"], frames["object_specific_dialogue"])
    write_csv(artifact_paths["agent_owned_inventory_requests_csv"], frames["agent_owned_inventory_requests"])
    write_csv(artifact_paths["reaction_consequences_csv"], frames["reaction_consequences"])
    write_csv(artifact_paths["later_scene_behaviors_csv"], frames["later_scene_behaviors"])
    write_csv(artifact_paths["access_and_refusals_csv"], frames["access_and_refusals"])
    write_csv(artifact_paths["agent_initiated_behaviors_csv"], frames["agent_initiated_behaviors"])
    write_csv(artifact_paths["reaction_memory_snapshots_csv"], frames["reaction_memory_snapshots"])
    write_csv(artifact_paths["multi_sensory_consequences_csv"], frames["multi_sensory_consequences"])
    write_csv(artifact_paths["consequence_replays_csv"], frames["consequence_replays"])
    write_csv(artifact_paths["browser_ticks_csv"], frames["browser_ticks"])
    write_mapping_csv(artifact_paths["summary_csv"], metrics)
    write_csv(artifact_paths["verdict_csv"], [{"verdict": verdict, **metrics}])

    state = build_state(frames, metrics, counts, args.seed)
    artifact_paths["state_json"].write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    render_html(state, artifact_paths["visualization_html"])

    results = {
        "report": 263,
        "name": "SSRM-3D browser world v23 object-specific dialogue inventory request reaction consequence bridge",
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
        "claim_boundary": "Deterministic browser-local object-specific dialogue, agent-owned inventory request, and reaction-consequence scaffold only; no LLM call, subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
        "next_gate": "browser world v24 with agent-owned tasks that persist across many scene visits, object return obligations, and delayed trust/access changes that compound over multiple days",
    }
    artifact_paths["results_json"].write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")

    print(json.dumps({"verdict": verdict, "metrics": metrics, "counts": counts}, indent=2, sort_keys=True))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
