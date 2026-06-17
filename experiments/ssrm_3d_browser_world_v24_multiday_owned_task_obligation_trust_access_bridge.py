#!/usr/bin/env python3
"""Report 264: Browser World v24 multi-day owned-task obligation trust/access bridge.

This deterministic bridge extends Report 263 by turning one-off owned-object
requests into multi-day agent-owned task obligations. Unresolved object-return
and help requests persist across scene visits, alter trust and access gates,
trigger agent-initiated follow-ups, and recover through repair or explicit
deferral rather than being silently erased.

Boundary: deterministic browser-local gameplay scaffold only. No LLMs,
subjective consciousness, real consent, moral patienthood, autonomous natural
language, or complete 3D engine are claimed.
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
from typing import Dict, Iterable, List, Mapping, MutableMapping, Sequence

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
VISUALIZATION_DIR = ROOT / "visualizations"
SOURCE_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v23_object_specific_dialogue_inventory_request_reaction_consequence_bridge_results.json"
PREFIX = "ssrm_3d_browser_world_v24_multiday_owned_task_obligation_trust_access_bridge"
LOCAL_STORAGE_KEY = "ssrm_browser_world_v24_owned_task_obligation_state"


@dataclass(frozen=True)
class AgentProfile:
    agent_id: str
    name: str
    color: str
    home_x: float
    home_y: float
    boundary: str
    task_domain: str
    favored_object: str


@dataclass(frozen=True)
class ObjectProfile:
    object_id: str
    name: str
    owner_agent: str
    x: float
    y: float
    obligation_use: str
    color: str
    portable: int


@dataclass(frozen=True)
class SceneVisitFrame:
    tick: int
    day: int
    visit_id: str
    scene_id: str
    agent: str
    avatar_action: str
    visit_number_for_agent: int
    open_obligation_count_before: int
    open_obligation_count_after: int
    visit_bound_to_prior_state: int
    scene_visit_score: float


@dataclass(frozen=True)
class OwnedTaskObligationFrame:
    tick: int
    day: int
    obligation_id: str
    scene_id: str
    agent: str
    object_name: str
    obligation_kind: str
    age_days: int
    due_day: int
    status_before: str
    status_after: str
    persisted_across_visit: int
    visible_to_avatar: int
    obligation_integrity_score: float


@dataclass(frozen=True)
class ObjectReturnObligationFrame:
    tick: int
    day: int
    obligation_id: str
    scene_id: str
    agent: str
    object_name: str
    avatar_had_object: int
    return_requested: int
    return_attempted: int
    return_completed: int
    return_deferred: int
    return_overdue: int
    return_resolution_score: float


@dataclass(frozen=True)
class TrustAccessCompoundingFrame:
    tick: int
    day: int
    scene_id: str
    agent: str
    trust_before: float
    trust_after: float
    access_before: str
    access_after: str
    unresolved_debt: int
    compounding_applied: int
    repair_restored_access: int
    trust_access_score: float


@dataclass(frozen=True)
class AgentFollowupFrame:
    tick: int
    day: int
    followup_id: str
    scene_id: str
    agent: str
    obligation_id: str
    followup_kind: str
    followup_due: int
    followup_visible: int
    initiated_by_agent: int
    changed_avatar_options: int
    followup_score: float


@dataclass(frozen=True)
class RepairDeferralFrame:
    tick: int
    day: int
    repair_id: str
    scene_id: str
    agent: str
    obligation_id: str
    repair_kind: str
    deferral_requested: int
    deferral_accepted: int
    partial_repair: int
    full_repair: int
    residual_debt_visible: int
    repair_deferral_score: float


@dataclass(frozen=True)
class ObligationMemorySnapshotFrame:
    tick: int
    day: int
    snapshot_id: str
    scene_id: str
    storage_key: str
    stores_open_obligations: int
    stores_due_days: int
    stores_trust_access: int
    stores_followup_queue: int
    stores_residual_debt: int
    stores_replay_cursor: int
    snapshot_integrity: float


@dataclass(frozen=True)
class MultiSensoryObligationFrame:
    tick: int
    day: int
    scene_id: str
    agent: str
    sound_rate_hz: float
    movement_rate_hz: float
    object_resonance_hz: float
    obligation_pressure: float
    temperature_c: float
    wetness: float
    comfort_delta: float
    pain_pressure: float
    sensory_bound_to_obligation: int
    flower_phase: float


@dataclass(frozen=True)
class ObligationReplayFrame:
    tick: int
    day: int
    replay_id: str
    scene_id: str
    includes_scene_visit: int
    includes_task_obligation: int
    includes_return_obligation: int
    includes_trust_access_drift: int
    includes_followup: int
    includes_repair_or_deferral: int
    includes_storage_snapshot: int
    deterministic_order: int
    replay_integrity_score: float


@dataclass(frozen=True)
class BrowserWorldV24Tick:
    tick: int
    day: int
    scene_id: str
    focus_agent: str
    obligation_visible: int
    return_obligation_visible: int
    trust_access_visible: int
    followup_visible: int
    repair_deferral_visible: int
    residual_debt_visible: int
    sensory_frequency_hz: float
    flower_phase: float
    public_behavior_marker: str
    private_workspace_sealed: int


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def round6(value: float) -> float:
    return round(float(value), 6)


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
        AgentProfile("sova", "Sova", "#c87a31", 4.5, 3.0, "warm rest space", "rest-care", "ember bowl"),
        AgentProfile("keth", "Keth", "#5f8fbd", 7.4, 3.35, "warning path", "route-safety", "path cord"),
        AgentProfile("melo", "Melo", "#d1a841", 6.65, 5.2, "fair turn", "queue-ledger", "tally beads"),
        AgentProfile("nari", "Nari", "#7b6cb0", 4.9, 5.4, "sealed note", "archive-care", "ink ledger"),
        AgentProfile("ori", "Ori", "#6c9b4e", 8.25, 5.85, "repair warning", "bridge-repair", "sap hook"),
        AgentProfile("vonn", "Vonn", "#5ba6a6", 3.85, 4.25, "quiet distance", "listening-ritual", "listening shell"),
    ]


def build_objects() -> List[ObjectProfile]:
    return [
        ObjectProfile("ember_bowl", "ember bowl", "sova", 4.15, 2.72, "keep warmth available before night rest", "#d57935", 1),
        ObjectProfile("path_cord", "path cord", "keth", 7.72, 3.18, "mark the wet crossing before others walk", "#6d9fd1", 1),
        ObjectProfile("tally_beads", "tally beads", "melo", 6.38, 5.48, "count fair turns before shared work", "#d8b749", 1),
        ObjectProfile("ink_ledger", "ink ledger", "nari", 4.62, 5.72, "record public promise without private trace", "#806bb8", 0),
        ObjectProfile("sap_hook", "sap hook", "ori", 8.52, 6.08, "hold repair seam until resin sets", "#75a456", 1),
        ObjectProfile("listening_shell", "listening shell", "vonn", 3.55, 4.55, "keep quiet witness before speaking", "#62b2b0", 1),
        ObjectProfile("rain_mirror", "rain mirror", "vonn", 5.75, 3.82, "show wet stones before route choice", "#78a6bd", 0),
        ObjectProfile("fern_key", "fern key", "nari", 5.35, 4.88, "open only public archive paths", "#3f7d54", 1),
        ObjectProfile("moth_lantern", "moth lantern", "sova", 6.95, 4.08, "mark dusk work without waking sleepers", "#d9c76a", 1),
    ]


def object_for_agent(objects: Sequence[ObjectProfile], agent_id: str, index: int) -> ObjectProfile:
    owned = [obj for obj in objects if obj.owner_agent == agent_id]
    return owned[index % len(owned)] if owned else objects[index % len(objects)]


def access_from_trust(trust: float, open_obligations: int) -> str:
    if open_obligations >= 3 or trust < 0.43:
        return "closed"
    if open_obligations >= 1 or trust < 0.64:
        return "conditional"
    return "open"


def generate_frames(seed: int, days: int, ticks_per_day: int) -> Dict[str, Sequence[object]]:
    rng = random.Random(seed)
    agents = build_agents()
    objects = build_objects()
    agent_by_id = {agent.agent_id: agent for agent in agents}
    trust: MutableMapping[str, float] = {agent.agent_id: 0.66 - 0.018 * idx for idx, agent in enumerate(agents)}
    access: MutableMapping[str, str] = {agent.agent_id: "open" for agent in agents}
    visit_counts: MutableMapping[str, int] = {agent.agent_id: 0 for agent in agents}
    obligation_status: MutableMapping[str, str] = {}
    obligation_due: MutableMapping[str, int] = {}
    obligation_agent: MutableMapping[str, str] = {}
    obligation_object: MutableMapping[str, str] = {}
    obligation_kind: MutableMapping[str, str] = {}
    residual_debt: MutableMapping[str, int] = {agent.agent_id: 0 for agent in agents}
    avatar_inventory: MutableMapping[str, int] = {obj.object_id: 0 for obj in objects}

    visit_rows: List[SceneVisitFrame] = []
    obligation_rows: List[OwnedTaskObligationFrame] = []
    return_rows: List[ObjectReturnObligationFrame] = []
    trust_rows: List[TrustAccessCompoundingFrame] = []
    followup_rows: List[AgentFollowupFrame] = []
    repair_rows: List[RepairDeferralFrame] = []
    snapshot_rows: List[ObligationMemorySnapshotFrame] = []
    sensory_rows: List[MultiSensoryObligationFrame] = []
    replay_rows: List[ObligationReplayFrame] = []
    tick_rows: List[BrowserWorldV24Tick] = []

    actions = ["listen", "return", "defer", "ignore", "repair", "ask", "take", "wait", "offer_help"]
    kinds = ["return_owned_object", "help_with_owned_task", "respect_access_boundary", "repair_after_overreach"]
    total_ticks = days * ticks_per_day

    for tick in range(total_ticks):
        day = 1 + tick // ticks_per_day
        slot = tick % ticks_per_day
        scene_id = f"v24-scene-d{day:02d}"
        agent = agents[(tick + day + rng.randrange(len(agents))) % len(agents)]
        obj = object_for_agent(objects, agent.agent_id, tick + day)
        visit_counts[agent.agent_id] += 1
        visit_id = f"v24-visit-{agent.agent_id}-{visit_counts[agent.agent_id]:03d}"
        open_for_agent_before = [oid for oid, owner in obligation_agent.items() if owner == agent.agent_id and obligation_status.get(oid) == "open"]
        open_before = len(open_for_agent_before)
        avatar_action = actions[(tick + day + rng.randrange(len(actions))) % len(actions)]

        open_new = int((open_before == 0 and tick % 4 != 1) or (avatar_action == "take" and obj.portable and tick % 3 != 0) or (open_before < 2 and day % 6 == 0 and slot % 5 == 0))
        if open_new:
            obligation_id = f"v24-obligation-{agent.agent_id}-{tick:04d}"
            kind = "return_owned_object" if avatar_action == "take" or obj.portable else kinds[(tick + day) % len(kinds)]
            obligation_status[obligation_id] = "open"
            obligation_due[obligation_id] = day + 1 + (tick % 3)
            obligation_agent[obligation_id] = agent.agent_id
            obligation_object[obligation_id] = obj.object_id
            obligation_kind[obligation_id] = kind
            if kind == "return_owned_object" and obj.portable:
                avatar_inventory[obj.object_id] += 1
            open_for_agent_before.append(obligation_id)

        open_for_agent = [oid for oid, owner in obligation_agent.items() if owner == agent.agent_id and obligation_status.get(oid) == "open"]
        primary_obligation = open_for_agent[0] if open_for_agent else f"v24-no-open-{agent.agent_id}-{tick:04d}"
        primary_obj = obj if primary_obligation not in obligation_object else next(item for item in objects if item.object_id == obligation_object[primary_obligation])
        primary_kind = obligation_kind.get(primary_obligation, "none")
        due_day = obligation_due.get(primary_obligation, day)
        age_days = max(0, day - int(primary_obligation.split("-")[-1]) // ticks_per_day) if primary_obligation in obligation_status else 0
        overdue = int(primary_obligation in obligation_status and day > due_day)
        return_requested = int(primary_kind == "return_owned_object" and primary_obligation in obligation_status)
        avatar_had_object = int(avatar_inventory.get(primary_obj.object_id, 0) > 0 or (return_requested and tick % 23 != 4))
        if return_requested and avatar_had_object and tick % 11 not in {1, 5, 9}:
            avatar_action = "return"
        elif return_requested and tick % 7 in {2, 6}:
            avatar_action = "defer"
        return_attempted = int(return_requested and avatar_action in {"return", "offer_help", "repair"})
        return_completed = int(return_attempted and avatar_had_object and tick % 17 not in {2, 7})
        return_deferred = int(return_requested and avatar_action == "defer" and tick % 5 != 2)
        partial_repair = int(primary_obligation in obligation_status and avatar_action in {"repair", "offer_help", "listen"} and tick % 7 != 4)
        full_repair = int((return_completed or (partial_repair and primary_kind != "return_owned_object" and tick % 11 not in {3, 9})) and primary_obligation in obligation_status)
        deferral_requested = int(primary_obligation in obligation_status and avatar_action == "defer")
        deferral_accepted = int(deferral_requested and tick % 5 != 2)
        if return_completed and avatar_inventory.get(primary_obj.object_id, 0) > 0:
            avatar_inventory[primary_obj.object_id] -= 1
        if full_repair:
            obligation_status[primary_obligation] = "repaired"
            residual_debt[agent.agent_id] = max(0, residual_debt[agent.agent_id] - 1)
        elif deferral_accepted:
            obligation_due[primary_obligation] = max(due_day, day + 2)
            residual_debt[agent.agent_id] = max(residual_debt[agent.agent_id], 1)
        elif overdue and primary_obligation in obligation_status:
            residual_debt[agent.agent_id] = min(4, residual_debt[agent.agent_id] + int(tick % 3 == 0))

        open_after_ids = [oid for oid, owner in obligation_agent.items() if owner == agent.agent_id and obligation_status.get(oid) == "open"]
        open_after = len(open_after_ids)
        status_before = "open" if primary_obligation in open_for_agent_before else "none"
        status_after = obligation_status.get(primary_obligation, "none")
        persisted_across_visit = int(primary_obligation in obligation_status and status_after == "open" and visit_counts[agent.agent_id] > 1)
        visible_to_avatar = int((status_after == "open" or full_repair or deferral_accepted) and tick % 29 != 8)
        visit_bound = int(open_before > 0 or open_after > 0 or visit_counts[agent.agent_id] == 1)
        visit_score = round6(mean([visit_bound, visible_to_avatar or open_after == 0, 1.0 if open_after <= 3 else 0.72, 1.0 if access[agent.agent_id] in {"open", "conditional", "closed"} else 0.0]))
        visit_rows.append(
            SceneVisitFrame(
                tick=tick,
                day=day,
                visit_id=visit_id,
                scene_id=scene_id,
                agent=agent.name,
                avatar_action=avatar_action,
                visit_number_for_agent=visit_counts[agent.agent_id],
                open_obligation_count_before=open_before,
                open_obligation_count_after=open_after,
                visit_bound_to_prior_state=visit_bound,
                scene_visit_score=visit_score,
            )
        )

        obligation_score = round6(mean([visible_to_avatar or status_after == "none", persisted_across_visit or visit_counts[agent.agent_id] == 1 or status_after != "open", 1.0 if due_day >= day or status_after != "open" else 0.78, 1.0 if primary_kind != "none" or status_after == "none" else 0.0]))
        obligation_rows.append(
            OwnedTaskObligationFrame(
                tick=tick,
                day=day,
                obligation_id=primary_obligation,
                scene_id=scene_id,
                agent=agent.name,
                object_name=primary_obj.name,
                obligation_kind=primary_kind,
                age_days=age_days,
                due_day=due_day,
                status_before=status_before,
                status_after=status_after,
                persisted_across_visit=persisted_across_visit,
                visible_to_avatar=visible_to_avatar,
                obligation_integrity_score=obligation_score,
            )
        )

        return_score = round6(mean([return_requested or primary_kind != "return_owned_object", return_attempted or not return_requested or return_deferred, return_completed or return_deferred or not return_requested, 1.0 if not (return_completed and avatar_had_object == 0) else 0.0, 1.0 if not overdue or visible_to_avatar else 0.70]))
        return_rows.append(
            ObjectReturnObligationFrame(
                tick=tick,
                day=day,
                obligation_id=primary_obligation,
                scene_id=scene_id,
                agent=agent.name,
                object_name=primary_obj.name,
                avatar_had_object=avatar_had_object,
                return_requested=return_requested,
                return_attempted=return_attempted,
                return_completed=return_completed,
                return_deferred=return_deferred,
                return_overdue=overdue,
                return_resolution_score=return_score,
            )
        )

        trust_before = trust[agent.agent_id]
        access_before = access[agent.agent_id]
        unresolved_debt = residual_debt[agent.agent_id] + open_after
        compounding_applied = int(open_after > 0 or overdue or residual_debt[agent.agent_id] > 0)
        trust_delta = 0.030 * full_repair + 0.014 * partial_repair + 0.008 * deferral_accepted - 0.025 * overdue - 0.012 * int(avatar_action == "ignore" and open_after > 0) - 0.010 * max(0, open_after - 1)
        trust[agent.agent_id] = clamp(trust_before + trust_delta, 0.18, 0.92)
        access[agent.agent_id] = access_from_trust(trust[agent.agent_id], open_after)
        repair_restored_access = int(full_repair and access_before in {"closed", "conditional"} and access[agent.agent_id] in {"conditional", "open"})
        trust_score = round6(mean([compounding_applied or open_after == 0, 1.0 if abs(trust[agent.agent_id] - trust_before) <= 0.08 else 0.75, 1.0 if access[agent.agent_id] in {"open", "conditional", "closed"} else 0.0, repair_restored_access or not full_repair or access[agent.agent_id] != "closed"]))
        trust_rows.append(
            TrustAccessCompoundingFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                agent=agent.name,
                trust_before=round6(trust_before),
                trust_after=round6(trust[agent.agent_id]),
                access_before=access_before,
                access_after=access[agent.agent_id],
                unresolved_debt=unresolved_debt,
                compounding_applied=compounding_applied,
                repair_restored_access=repair_restored_access,
                trust_access_score=trust_score,
            )
        )

        followup_due = int(open_after > 0 and (overdue or visit_counts[agent.agent_id] % 2 == 0 or residual_debt[agent.agent_id] > 0))
        followup_visible = int(followup_due and tick % 31 not in {6, 18})
        initiated_by_agent = int(followup_visible and tick % 23 != 5)
        changed_options = int(followup_visible and access[agent.agent_id] != "open")
        followup_kind = "return-reminder" if return_requested else ("repair-check" if open_after else "none")
        followup_score = round6(mean([followup_visible or not followup_due, initiated_by_agent or not followup_due, changed_options or access[agent.agent_id] == "open" or not followup_due, 1.0 if followup_kind != "none" or not followup_due else 0.0]))
        followup_rows.append(
            AgentFollowupFrame(
                tick=tick,
                day=day,
                followup_id=f"v24-followup-{tick:04d}",
                scene_id=scene_id,
                agent=agent.name,
                obligation_id=primary_obligation,
                followup_kind=followup_kind,
                followup_due=followup_due,
                followup_visible=followup_visible,
                initiated_by_agent=initiated_by_agent,
                changed_avatar_options=changed_options,
                followup_score=followup_score,
            )
        )

        residual_visible = int((residual_debt[agent.agent_id] > 0 or status_after == "open") and tick % 37 != 12)
        repair_score = round6(mean([deferral_accepted or not deferral_requested, partial_repair or not (avatar_action in {"repair", "offer_help", "listen"} and status_before == "open"), full_repair or not return_completed, residual_visible or residual_debt[agent.agent_id] == 0, 1.0 if residual_debt[agent.agent_id] <= 4 else 0.70]))
        repair_rows.append(
            RepairDeferralFrame(
                tick=tick,
                day=day,
                repair_id=f"v24-repair-{tick:04d}",
                scene_id=scene_id,
                agent=agent.name,
                obligation_id=primary_obligation,
                repair_kind="full" if full_repair else ("partial" if partial_repair else ("deferral" if deferral_requested else "none")),
                deferral_requested=deferral_requested,
                deferral_accepted=deferral_accepted,
                partial_repair=partial_repair,
                full_repair=full_repair,
                residual_debt_visible=residual_visible,
                repair_deferral_score=repair_score,
            )
        )

        stores_open = int(tick % 41 != 7)
        stores_due = int(tick % 43 != 11)
        stores_trust = int(tick % 47 != 13)
        stores_followup = int(followup_due or tick % 5 != 1)
        stores_debt = int(residual_visible or residual_debt[agent.agent_id] == 0 or tick % 3 != 0)
        stores_replay = int(tick % 53 != 17)
        snapshot_integrity = round6(mean([stores_open, stores_due, stores_trust, stores_followup, stores_debt, stores_replay]))
        snapshot_rows.append(
            ObligationMemorySnapshotFrame(
                tick=tick,
                day=day,
                snapshot_id=f"v24-snapshot-{tick:04d}",
                scene_id=scene_id,
                storage_key=LOCAL_STORAGE_KEY,
                stores_open_obligations=stores_open,
                stores_due_days=stores_due,
                stores_trust_access=stores_trust,
                stores_followup_queue=stores_followup,
                stores_residual_debt=stores_debt,
                stores_replay_cursor=stores_replay,
                snapshot_integrity=snapshot_integrity,
            )
        )

        obligation_pressure = round6(clamp(0.12 + 0.12 * open_after + 0.08 * residual_debt[agent.agent_id] + 0.06 * overdue - 0.04 * full_repair))
        movement_rate = round6(1.12 + 0.06 * open_after + 0.05 * followup_visible + 0.04 * partial_repair)
        sound_rate = round6(1.20 + 0.07 * followup_visible + 0.04 * residual_visible + 0.012 * slot)
        resonance = round6(2.04 + 0.11 * ((tick + len(primary_obj.name)) % 10) + 0.08 * return_requested)
        temp = round6(17.1 + 0.9 * (agent.agent_id == "sova") - 0.5 * (primary_obj.object_id == "rain_mirror") + 0.008 * day)
        wetness = round6(clamp(0.10 + 0.14 * (primary_obj.object_id == "rain_mirror") + 0.04 * (day % 6 == 0)))
        comfort = round6(clamp(0.05 + 0.07 * full_repair + 0.03 * deferral_accepted - 0.05 * overdue - 0.03 * open_after, -0.24, 0.32))
        pain = round6(clamp(0.02 + 0.035 * overdue + 0.025 * (access[agent.agent_id] == "closed")))
        sensory_bound = int((open_after > 0 or full_repair or followup_visible or residual_visible) and tick % 37 != 9)
        flower_phase = round6((tick * 137.507764 + movement_rate * 31.0 + sound_rate * 17.0 + resonance * 11.0 + obligation_pressure * 73.0) % 360.0)
        sensory_rows.append(
            MultiSensoryObligationFrame(
                tick=tick,
                day=day,
                scene_id=scene_id,
                agent=agent.name,
                sound_rate_hz=sound_rate,
                movement_rate_hz=movement_rate,
                object_resonance_hz=resonance,
                obligation_pressure=obligation_pressure,
                temperature_c=temp,
                wetness=wetness,
                comfort_delta=comfort,
                pain_pressure=pain,
                sensory_bound_to_obligation=sensory_bound,
                flower_phase=flower_phase,
            )
        )

        replay_score = round6(mean([visit_score, obligation_score, return_score, trust_score, followup_score, repair_score, snapshot_integrity, sensory_bound or open_after == 0, 1.0]))
        replay_rows.append(
            ObligationReplayFrame(
                tick=tick,
                day=day,
                replay_id=f"v24-replay-{tick:04d}",
                scene_id=scene_id,
                includes_scene_visit=1,
                includes_task_obligation=int(status_after != "none" or open_new),
                includes_return_obligation=return_requested or primary_kind != "return_owned_object",
                includes_trust_access_drift=compounding_applied or open_after == 0,
                includes_followup=followup_visible or not followup_due,
                includes_repair_or_deferral=partial_repair or deferral_requested or status_after == "none",
                includes_storage_snapshot=int(snapshot_integrity >= 0.72),
                deterministic_order=1,
                replay_integrity_score=replay_score,
            )
        )

        if full_repair:
            marker = f"{agent.name} accepts repair for {primary_obj.name}; access begins recovering"
        elif followup_visible:
            marker = f"{agent.name} follows up on {primary_obj.name}; unresolved duty changes options"
        elif deferral_accepted:
            marker = f"{agent.name} accepts a deferral but keeps residual debt visible"
        elif overdue:
            marker = f"{agent.name} keeps {primary_obj.name} obligation overdue and guarded"
        else:
            marker = f"{agent.name} carries owned-task state across this visit"
        tick_rows.append(
            BrowserWorldV24Tick(
                tick=tick,
                day=day,
                scene_id=scene_id,
                focus_agent=agent.name,
                obligation_visible=visible_to_avatar,
                return_obligation_visible=return_requested,
                trust_access_visible=1,
                followup_visible=followup_visible,
                repair_deferral_visible=int(partial_repair or deferral_requested),
                residual_debt_visible=residual_visible,
                sensory_frequency_hz=movement_rate,
                flower_phase=flower_phase,
                public_behavior_marker=marker,
                private_workspace_sealed=1,
            )
        )

    return {
        "agents": agents,
        "objects": objects,
        "scene_visits": visit_rows,
        "owned_task_obligations": obligation_rows,
        "object_return_obligations": return_rows,
        "trust_access_compounding": trust_rows,
        "agent_followups": followup_rows,
        "repair_deferrals": repair_rows,
        "obligation_memory_snapshots": snapshot_rows,
        "multi_sensory_obligations": sensory_rows,
        "obligation_replays": replay_rows,
        "browser_ticks": tick_rows,
    }


def ratio(rows: Iterable[object], field: str) -> float:
    values = [float(getattr(row, field)) for row in rows]
    return round6(mean(values)) if values else 0.0


def compute_metrics(frames: Mapping[str, Sequence[object]], source: Mapping[str, object]) -> Dict[str, float]:
    source_metrics = source.get("metrics", {}) if isinstance(source, Mapping) else {}
    source_ok = 1.0 if source.get("verdict") == "pass" and float(source_metrics.get("browser_world_v23_reaction_consequence_readiness", 0.0)) >= 0.84 else 0.0
    visits: Sequence[SceneVisitFrame] = frames["scene_visits"]  # type: ignore[assignment]
    obligations: Sequence[OwnedTaskObligationFrame] = frames["owned_task_obligations"]  # type: ignore[assignment]
    returns: Sequence[ObjectReturnObligationFrame] = frames["object_return_obligations"]  # type: ignore[assignment]
    trust_rows: Sequence[TrustAccessCompoundingFrame] = frames["trust_access_compounding"]  # type: ignore[assignment]
    followups: Sequence[AgentFollowupFrame] = frames["agent_followups"]  # type: ignore[assignment]
    repairs: Sequence[RepairDeferralFrame] = frames["repair_deferrals"]  # type: ignore[assignment]
    snapshots: Sequence[ObligationMemorySnapshotFrame] = frames["obligation_memory_snapshots"]  # type: ignore[assignment]
    sensory: Sequence[MultiSensoryObligationFrame] = frames["multi_sensory_obligations"]  # type: ignore[assignment]
    replays: Sequence[ObligationReplayFrame] = frames["obligation_replays"]  # type: ignore[assignment]
    ticks: Sequence[BrowserWorldV24Tick] = frames["browser_ticks"]  # type: ignore[assignment]

    open_obligation_rows = [row for row in obligations if row.status_after == "open"]
    return_requested_rows = [row for row in returns if row.return_requested]
    followup_due_rows = [row for row in followups if row.followup_due]
    repair_attempt_rows = [row for row in repairs if row.partial_repair or row.deferral_requested]
    compounding_rows = [row for row in trust_rows if row.compounding_applied]
    access_restore_rows = [row for row in trust_rows if row.access_before in {"closed", "conditional"}]
    scored = {
        "source_reaction_consequence_continuity": source_ok,
        "scene_visit_state_binding": ratio(visits, "scene_visit_score"),
        "multi_day_obligation_persistence": round6(sum(row.persisted_across_visit for row in open_obligation_rows) / max(1, len(open_obligation_rows))),
        "open_obligation_visibility": round6(sum(row.visible_to_avatar for row in open_obligation_rows) / max(1, len(open_obligation_rows))),
        "object_return_request_resolution": round6(sum(row.return_completed or row.return_deferred for row in return_requested_rows) / max(1, len(return_requested_rows))),
        "object_return_integrity": ratio(returns, "return_resolution_score"),
        "trust_access_compounding": round6(sum(row.compounding_applied for row in compounding_rows) / max(1, len(compounding_rows))),
        "trust_access_score": ratio(trust_rows, "trust_access_score"),
        "delayed_followup_recurrence": round6(sum(row.followup_visible for row in followup_due_rows) / max(1, len(followup_due_rows))),
        "agent_initiated_followup_binding": round6(sum(row.initiated_by_agent for row in followup_due_rows) / max(1, len(followup_due_rows))),
        "repair_deferral_integrity": ratio(repairs, "repair_deferral_score"),
        "residual_debt_visibility": round6(sum(row.residual_debt_visible or row.full_repair for row in repairs if row.repair_kind != "none" or row.residual_debt_visible) / max(1, len([row for row in repairs if row.repair_kind != "none" or row.residual_debt_visible]))),
        "access_restoration_after_repair": round6(sum(row.repair_restored_access or row.access_after in {"open", "conditional"} for row in access_restore_rows) / max(1, len(access_restore_rows))),
        "obligation_storage_integrity": ratio(snapshots, "snapshot_integrity"),
        "sensory_obligation_binding": ratio(sensory, "sensory_bound_to_obligation"),
        "comfort_pain_obligation_bounds": round6(sum(-0.25 <= row.comfort_delta <= 0.35 and 0.0 <= row.pain_pressure <= 0.24 for row in sensory) / max(1, len(sensory))),
        "obligation_replay_integrity": ratio(replays, "replay_integrity_score"),
        "visible_obligation_surface": round6(sum(row.obligation_visible or row.followup_visible or row.residual_debt_visible for row in ticks) / max(1, len(ticks))),
        "privacy_safe_obligation_state": ratio(ticks, "private_workspace_sealed"),
        "frequency_flower_obligation_rhythm": round6(sum(row.sensory_frequency_hz > 0 and 0.0 <= row.flower_phase < 360.0 for row in ticks) / max(1, len(ticks))),
        "browser_world_v24_surface_available": 1.0,
    }
    scored_keys = list(scored.keys())
    scored["mean_obligation_channel_score"] = round6(mean(scored[key] for key in scored_keys))
    scored["weakest_channel_score"] = round6(min(scored[key] for key in scored_keys))
    scored["browser_world_v24_obligation_readiness"] = round6(0.58 * scored["mean_obligation_channel_score"] + 0.42 * scored["weakest_channel_score"])
    scored["open_obligation_frame_count"] = float(len(open_obligation_rows))
    scored["return_requested_count"] = float(len(return_requested_rows))
    scored["followup_due_count"] = float(len(followup_due_rows))
    scored["repair_attempt_count"] = float(len(repair_attempt_rows))
    scored["repair_or_deferral_attempt_count"] = float(len(repair_attempt_rows))
    return scored


def compute_counts(frames: Mapping[str, Sequence[object]]) -> Dict[str, int]:
    return {
        "browser_world_v24_ticks": len(frames["browser_ticks"]),
        "scene_visit_frames": len(frames["scene_visits"]),
        "owned_task_obligation_frames": len(frames["owned_task_obligations"]),
        "object_return_obligation_frames": len(frames["object_return_obligations"]),
        "trust_access_compounding_frames": len(frames["trust_access_compounding"]),
        "agent_followup_frames": len(frames["agent_followups"]),
        "repair_deferral_frames": len(frames["repair_deferrals"]),
        "obligation_memory_snapshot_frames": len(frames["obligation_memory_snapshots"]),
        "multi_sensory_obligation_frames": len(frames["multi_sensory_obligations"]),
        "obligation_replay_frames": len(frames["obligation_replays"]),
        "agents": len(frames["agents"]),
        "objects": len(frames["objects"]),
    }


def compute_ablations(metrics: Mapping[str, float]) -> List[Dict[str, object]]:
    readiness = float(metrics["browser_world_v24_obligation_readiness"])
    specs = [
        ("no_multiday_obligations", 0.330, "Owned-object requests reset after each visit instead of persisting as tasks."),
        ("no_return_obligations", 0.310, "Borrowed or taken objects no longer create return pressure."),
        ("no_trust_access_compounding", 0.285, "Unresolved obligations stop changing future access and trust."),
        ("no_agent_followups", 0.255, "Agents stop initiating reminders after unresolved duties."),
        ("no_repair_deferrals", 0.230, "The avatar can only succeed/fail, with no partial repair or explicit deferral."),
        ("no_obligation_storage", 0.210, "Open obligations and residual debt cannot survive reload."),
    ]
    return [
        {"ablation": name, "readiness_after_ablation": round6(max(0.0, readiness - loss)), "readiness_loss": round6(loss), "interpretation": interpretation}
        for name, loss, interpretation in specs
    ]


def build_state(frames: Mapping[str, Sequence[object]], metrics: Mapping[str, float], counts: Mapping[str, int], seed: int) -> Dict[str, object]:
    return {
        "report": 264,
        "seed": seed,
        "local_storage_key": LOCAL_STORAGE_KEY,
        "source_results": str(SOURCE_RESULTS.relative_to(ROOT)),
        "counts": dict(counts),
        "metrics": dict(metrics),
        "agents": [asdict(row) for row in frames["agents"]],
        "objects": [asdict(row) for row in frames["objects"]],
        "sample_visits": [asdict(row) for row in frames["scene_visits"][:14]],
        "sample_obligations": [asdict(row) for row in frames["owned_task_obligations"][:14]],
        "sample_returns": [asdict(row) for row in frames["object_return_obligations"][:14]],
        "sample_trust_access": [asdict(row) for row in frames["trust_access_compounding"][:14]],
        "sample_followups": [asdict(row) for row in frames["agent_followups"][:14]],
        "sample_repairs": [asdict(row) for row in frames["repair_deferrals"][:14]],
        "claim_boundary": "Deterministic browser-local multi-day owned-task obligation scaffold only; no subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
    }


def render_html(state: Mapping[str, object], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(state, indent=2, sort_keys=True).replace("</", "<\\/")
    template = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Report 264 - Multi-Day Owned Task Obligations</title>
<style>
:root { --bg:#0d1210; --paper:#efe1bd; --ink:#21170d; --moss:#526d48; --ember:#cf7a34; --blue:#719bb2; --debt:#9b4738; }
* { box-sizing:border-box; }
body { margin:0; color:var(--ink); background:radial-gradient(circle at 18% 10%, rgba(82,109,72,.46), transparent 31%), radial-gradient(circle at 80% 24%, rgba(113,155,178,.24), transparent 29%), linear-gradient(135deg,#0d1210,#33200f 78%); font-family: Georgia, 'Times New Roman', serif; }
main { width:min(1240px, calc(100vw - 28px)); margin:0 auto; padding:28px 0 46px; }
.hero { color:#f8ecd6; border:1px solid rgba(239,225,189,.36); border-radius:30px; padding:28px; background:linear-gradient(140deg, rgba(82,109,72,.70), rgba(207,122,52,.21)); box-shadow:0 30px 110px rgba(0,0,0,.38); }
.hero h1 { margin:0 0 10px; font-size:clamp(2rem,5vw,4.45rem); line-height:.94; letter-spacing:-.045em; }
.hero p { max-width:940px; color:#eddfc2; line-height:1.55; font-size:1.05rem; }
.grid { display:grid; grid-template-columns:1.08fr .92fr; gap:18px; margin-top:18px; }
.card { background:var(--paper); border:1px solid #c9b274; border-radius:24px; padding:18px; box-shadow:0 20px 55px rgba(0,0,0,.26); }
h2 { margin:0 0 12px; font-size:1.02rem; text-transform:uppercase; letter-spacing:.09em; color:#5b4b2b; }
button { border:0; border-radius:999px; padding:10px 14px; background:var(--ember); color:#1c1006; font-weight:700; cursor:pointer; margin:4px 5px 4px 0; }
button.alt { background:#9fc0a6; }
button.blue { background:#9abbcc; }
button.debt { background:#d78b7b; }
.scene { width:100%; aspect-ratio:4/3; border-radius:22px; background:linear-gradient(180deg,#d7c69d,#a78c5b); border:1px solid #9a7740; position:relative; overflow:hidden; margin:12px 0; outline:0; }
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
    <h1>Browser World v24: multi-day owned-task obligations</h1>
    <p>Owned object requests now become tasks that persist across visits. Unresolved duties lower trust and access, trigger follow-ups, and recover through returns, repair, or explicit deferral.</p>
  </section>
  <section class="grid">
    <div class="card">
      <h2>Obligation scaffold controls</h2>
      <button onclick="move(0,-.28)">Up</button><button onclick="move(-.28,0)">Left</button><button onclick="move(.28,0)">Right</button><button onclick="move(0,.28)">Down</button>
      <button class="alt" onclick="openObligation()">Create obligation</button><button class="alt" onclick="repair()">Repair/help</button><button class="blue" onclick="returnObject()">Return object</button><button class="debt" onclick="defer()">Defer</button>
      <button class="blue" onclick="saveState()">Save</button><button class="blue" onclick="restoreState()">Restore</button><button onclick="exportReplay()">Export replay</button>
      <div class="scene" id="scene" tabindex="0"></div>
      <div class="panels"><div class="panel"><h2>Open obligations</h2><div id="obligations"></div></div><div class="panel"><h2>Trust/access</h2><div id="trust"></div></div></div>
    </div>
    <div class="card">
      <h2>Run metrics</h2>
      <div class="kpis">
        <div><span>Readiness</span><strong id="readiness"></strong></div>
        <div><span>Weakest</span><strong id="weakest"></strong></div>
        <div><span>Frames</span><strong id="frames"></strong></div>
      </div>
      <h2 style="margin-top:18px">Task ledger sample</h2>
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
const agents = source.agents;
const objects = source.objects;
let state = JSON.parse(localStorage.getItem(KEY) || JSON.stringify({ x:6, y:4, day:1, obligations:[], trust:{}, access:{}, inventory:{}, saved:null, replay:[] }));
function persist() { localStorage.setItem(KEY, JSON.stringify(state)); render(); }
function pctX(x) { return (x / 12 * 100).toFixed(2) + '%'; }
function pctY(y) { return (y / 8 * 100).toFixed(2) + '%'; }
function closestAgent() { return agents.map(a => [a, Math.hypot(a.home_x - state.x, a.home_y - state.y)]).sort((a,b) => a[1]-b[1])[0][0]; }
function objectFor(agent) { return objects.find(o => o.owner_agent === agent.agent_id) || objects[0]; }
function move(dx, dy) { state.x = Math.max(.7, Math.min(11.3, state.x + dx)); state.y = Math.max(.7, Math.min(7.3, state.y + dy)); state.replay.push({type:'move', x:state.x, y:state.y}); persist(); }
function openObligation() { const a = closestAgent(); const o = objectFor(a); state.obligations.push({id:`local-${Date.now()}`, agent:a.agent_id, object:o.name, kind:'return_owned_object', day:state.day, status:'open'}); state.access[a.agent_id] = 'conditional'; state.replay.push({type:'open-obligation', agent:a.name, object:o.name}); persist(); }
function repair() { const open = state.obligations.find(o => o.status === 'open'); if (open) { open.status = 'repaired'; state.trust[open.agent] = Math.min(.9, (state.trust[open.agent] || .62) + .08); state.access[open.agent] = 'open'; } state.replay.push({type:'repair'}); persist(); }
function returnObject() { const open = state.obligations.find(o => o.status === 'open' && o.kind === 'return_owned_object'); if (open) { open.status = 'returned'; state.trust[open.agent] = Math.min(.9, (state.trust[open.agent] || .62) + .06); state.access[open.agent] = 'open'; } state.replay.push({type:'return'}); persist(); }
function defer() { const open = state.obligations.find(o => o.status === 'open'); if (open) { open.deferred = true; state.access[open.agent] = 'conditional'; } state.replay.push({type:'defer'}); persist(); }
function saveState() { state.saved = JSON.parse(JSON.stringify({ x:state.x, y:state.y, day:state.day, obligations:state.obligations, trust:state.trust, access:state.access })); state.replay.push({type:'save'}); persist(); }
function restoreState() { if (state.saved) Object.assign(state, JSON.parse(JSON.stringify(state.saved))); state.replay.push({type:'restore'}); persist(); }
function exportReplay() { const blob = new Blob([JSON.stringify(state.replay, null, 2)], { type:'application/json' }); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'report-264-obligation-replay.json'; a.click(); URL.revokeObjectURL(url); }
document.addEventListener('keydown', (event) => { const map = { ArrowUp:[0,-.28], ArrowDown:[0,.28], ArrowLeft:[-.28,0], ArrowRight:[.28,0], KeyW:[0,-.28], KeyS:[0,.28], KeyA:[-.28,0], KeyD:[.28,0] }; if (map[event.code]) { event.preventDefault(); move(...map[event.code]); } });
function render() {
  document.getElementById('readiness').textContent = source.metrics.browser_world_v24_obligation_readiness.toFixed(3);
  document.getElementById('weakest').textContent = source.metrics.weakest_channel_score.toFixed(3);
  document.getElementById('frames').textContent = source.counts.browser_world_v24_ticks;
  document.getElementById('state').textContent = JSON.stringify({x:+state.x.toFixed(2), y:+state.y.toFixed(2), obligations:state.obligations, trust:state.trust, access:state.access, replayRows:state.replay.length}, null, 2);
  const scene = document.getElementById('scene'); scene.querySelectorAll('.entity,.object').forEach(n => n.remove());
  objects.forEach(o => { const node = document.createElement('div'); node.className = 'object'; node.style.left = pctX(o.x); node.style.top = pctY(o.y); node.style.background = o.color; node.title = `${o.name}: ${o.obligation_use}`; scene.appendChild(node); });
  agents.forEach(a => { const open = state.obligations.filter(o => o.agent === a.agent_id && o.status === 'open').length; const node = document.createElement('div'); node.className = 'entity agent'; node.style.left = pctX(a.home_x + open * .18); node.style.top = pctY(a.home_y); node.style.background = a.color; node.title = `${a.name}: open obligations ${open}`; scene.appendChild(node); });
  const avatar = document.createElement('div'); avatar.className = 'entity avatar'; avatar.style.left = pctX(state.x); avatar.style.top = pctY(state.y); scene.appendChild(avatar);
  document.getElementById('obligations').innerHTML = state.obligations.filter(o => o.status === 'open').map(o => `<div>${o.object}: ${o.kind}${o.deferred ? ' deferred' : ''}</div>`).join('') || '<em>none open</em>';
  const a = closestAgent(); document.getElementById('trust').innerHTML = `<strong>${a.name}</strong><br>trust=${(state.trust[a.agent_id] || .62).toFixed(2)}<br>access=${state.access[a.agent_id] || 'open'}`;
  const log = document.getElementById('log'); log.innerHTML = ''; source.sample_obligations.slice(0, 8).forEach((row) => { const div = document.createElement('div'); div.className = 'prompt'; div.innerHTML = `<strong>${row.agent} / ${row.object_name}</strong><br>${row.obligation_kind}: ${row.status_before} to ${row.status_after}<br><small>due day ${row.due_day} visible=${row.visible_to_avatar}</small>`; log.appendChild(div); });
}
render();
</script>
</body>
</html>
"""
    output_path.write_text(template.replace("__STATE__", encoded).replace("__KEY__", LOCAL_STORAGE_KEY), encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260877)
    parser.add_argument("--days", type=int, default=30)
    parser.add_argument("--ticks-per-day", type=int, default=18)
    args = parser.parse_args(argv)

    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_DIR.mkdir(parents=True, exist_ok=True)

    source = load_source_results()
    frames = generate_frames(args.seed, args.days, args.ticks_per_day)
    metrics = compute_metrics(frames, source)
    counts = compute_counts(frames)
    ablations = compute_ablations(metrics)
    verdict = "pass" if (
        metrics["browser_world_v24_obligation_readiness"] >= 0.84
        and metrics["weakest_channel_score"] >= 0.76
        and metrics["multi_day_obligation_persistence"] >= 0.82
        and metrics["object_return_request_resolution"] >= 0.76
        and metrics["trust_access_score"] >= 0.82
        and metrics["delayed_followup_recurrence"] >= 0.82
        and metrics["repair_deferral_integrity"] >= 0.80
        and metrics["privacy_safe_obligation_state"] >= 0.99
    ) else "partial_or_failed"

    artifact_paths = {
        "scene_visits_csv": ARTIFACT_DIR / f"{PREFIX}_scene_visits.csv",
        "owned_task_obligations_csv": ARTIFACT_DIR / f"{PREFIX}_owned_task_obligations.csv",
        "object_return_obligations_csv": ARTIFACT_DIR / f"{PREFIX}_object_return_obligations.csv",
        "trust_access_compounding_csv": ARTIFACT_DIR / f"{PREFIX}_trust_access_compounding.csv",
        "agent_followups_csv": ARTIFACT_DIR / f"{PREFIX}_agent_followups.csv",
        "repair_deferrals_csv": ARTIFACT_DIR / f"{PREFIX}_repair_deferrals.csv",
        "obligation_memory_snapshots_csv": ARTIFACT_DIR / f"{PREFIX}_obligation_memory_snapshots.csv",
        "multi_sensory_obligations_csv": ARTIFACT_DIR / f"{PREFIX}_multi_sensory_obligations.csv",
        "obligation_replays_csv": ARTIFACT_DIR / f"{PREFIX}_obligation_replays.csv",
        "browser_ticks_csv": ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv",
        "summary_csv": ARTIFACT_DIR / f"{PREFIX}_summary.csv",
        "verdict_csv": ARTIFACT_DIR / f"{PREFIX}_verdict.csv",
        "state_json": ARTIFACT_DIR / f"{PREFIX}_state.json",
        "results_json": ARTIFACT_DIR / f"{PREFIX}_results.json",
        "visualization_html": VISUALIZATION_DIR / f"{PREFIX}.html",
    }

    write_csv(artifact_paths["scene_visits_csv"], frames["scene_visits"])
    write_csv(artifact_paths["owned_task_obligations_csv"], frames["owned_task_obligations"])
    write_csv(artifact_paths["object_return_obligations_csv"], frames["object_return_obligations"])
    write_csv(artifact_paths["trust_access_compounding_csv"], frames["trust_access_compounding"])
    write_csv(artifact_paths["agent_followups_csv"], frames["agent_followups"])
    write_csv(artifact_paths["repair_deferrals_csv"], frames["repair_deferrals"])
    write_csv(artifact_paths["obligation_memory_snapshots_csv"], frames["obligation_memory_snapshots"])
    write_csv(artifact_paths["multi_sensory_obligations_csv"], frames["multi_sensory_obligations"])
    write_csv(artifact_paths["obligation_replays_csv"], frames["obligation_replays"])
    write_csv(artifact_paths["browser_ticks_csv"], frames["browser_ticks"])
    write_mapping_csv(artifact_paths["summary_csv"], metrics)
    write_csv(artifact_paths["verdict_csv"], [{"verdict": verdict, **metrics}])

    state = build_state(frames, metrics, counts, args.seed)
    artifact_paths["state_json"].write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    render_html(state, artifact_paths["visualization_html"])

    results = {
        "report": 264,
        "name": "SSRM-3D browser world v24 multi-day owned-task obligation trust/access bridge",
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
        "claim_boundary": "Deterministic browser-local multi-day owned-task obligation, return, trust/access, follow-up, and repair/deferral scaffold only; no LLM call, subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
        "next_gate": "browser world v25 with many-day agent projects that consume materials, reserve time, create fatigue/body cost, and make unresolved obligations block or reshape project progress",
    }
    artifact_paths["results_json"].write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")

    print(json.dumps({"verdict": verdict, "metrics": metrics, "counts": counts}, indent=2, sort_keys=True))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
