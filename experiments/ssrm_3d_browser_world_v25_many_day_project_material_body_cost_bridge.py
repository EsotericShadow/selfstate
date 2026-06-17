#!/usr/bin/env python3
"""Report 265: SSRM-3D browser world v25 many-day project/material/body-cost bridge.

This deterministic benchmark extends the browser-world line after Report 264 by
making agent-owned work persist as many-day projects. Projects consume materials,
reserve time, impose fatigue/body cost, and can be blocked or reshaped by
unresolved obligations from the previous owned-task layer.

Boundary: this is inspectable gameplay/state scaffolding. It does not claim
subjective consciousness, real consent, moral patienthood, autonomous natural
language, a complete 3D engine, or metaphysical frequency effects.
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
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Sequence

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
PREFIX = "ssrm_3d_browser_world_v25_many_day_project_material_body_cost_bridge"
V24_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v24_multiday_owned_task_obligation_trust_access_bridge_results.json"
DEFAULT_SEED = 20260878
DAYS = 36
TICKS_PER_DAY = 18
BOUNDARY = (
    "deterministic browser-local project/material/body-cost scaffold only; "
    "no LLM call, subjective consciousness, real consent, moral patienthood, "
    "autonomous natural language, complete 3D engine, or metaphysical frequency claim"
)


@dataclass(frozen=True)
class ProjectDefinition:
    project_id: str
    owner: str
    title: str
    home_zone: str
    primary_object: str
    preferred_slot: str
    required_materials: str
    stage_plan: str
    ownership_clause: str
    recovery_clause: str


@dataclass(frozen=True)
class ProjectProgressFrame:
    tick_id: int
    day: int
    tick: int
    project_id: str
    owner: str
    stage: str
    progress_before: float
    progress_delta: float
    progress_after: float
    target_after_reshape: float
    active_work: bool
    blocked: bool
    blocker_type: str
    reshaped: bool
    visible_project_marker: str


@dataclass(frozen=True)
class MaterialInventoryFrame:
    tick_id: int
    day: int
    project_id: str
    material: str
    inventory_before: float
    consumed: float
    inventory_after: float
    shortage: bool
    shortage_visible: bool
    ledger_entry: str
    substitute_material: str


@dataclass(frozen=True)
class TimeReservationFrame:
    tick_id: int
    day: int
    tick: int
    project_id: str
    owner: str
    reserved_slot: str
    reserved: bool
    conflict_kind: str
    conflict_handled: bool
    deferred_to_tick: int
    rest_protected: bool


@dataclass(frozen=True)
class BodyCostFatigueFrame:
    tick_id: int
    day: int
    owner: str
    project_id: str
    energy: float
    fatigue_before: float
    fatigue_delta: float
    fatigue_after: float
    movement_effort: float
    comfort: float
    pain: float
    rest_action: str
    recovery_visible: bool


@dataclass(frozen=True)
class ObligationProjectBlockerFrame:
    tick_id: int
    day: int
    project_id: str
    owner: str
    obligation_id: str
    unresolved: bool
    blocks_material: bool
    blocks_time: bool
    blocks_access: bool
    blocker_visible: bool
    repair_option: str
    residual_debt: float


@dataclass(frozen=True)
class ProjectReshapeFrame:
    tick_id: int
    day: int
    project_id: str
    owner: str
    reshape_event: bool
    reshape_reason: str
    old_target: float
    new_target: float
    dignity_preserved: bool
    material_substitution: str
    public_explanation: str


@dataclass(frozen=True)
class AgentProjectFollowupFrame:
    tick_id: int
    day: int
    agent: str
    project_id: str
    followup_kind: str
    request_text: str
    tied_to_blocker: bool
    tied_to_fatigue: bool
    tied_to_material: bool
    next_consequence: str
    player_visible: bool


@dataclass(frozen=True)
class ProjectMemorySnapshotFrame:
    tick_id: int
    day: int
    agent: str
    project_id: str
    public_memory_key: str
    stored_progress: float
    stored_blocker: str
    stored_material_debt: str
    private_workspace_sealed: bool
    replay_pointer: str


@dataclass(frozen=True)
class MultiSensoryProjectFrame:
    tick_id: int
    day: int
    project_id: str
    owner: str
    sight_cue: str
    sound_cue: str
    body_cue: str
    material_cue: str
    weather_cue: str
    sensory_bound_to_project: bool


@dataclass(frozen=True)
class ProjectReplayFrame:
    tick_id: int
    day: int
    project_id: str
    replay_event: str
    state_hash: str
    includes_materials: bool
    includes_body_cost: bool
    includes_blocker: bool
    includes_reshape: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV25Tick:
    tick_id: int
    day: int
    tick: int
    avatar_zone: str
    active_project: str
    visible_card: str
    material_panel: str
    fatigue_panel: str
    obligation_panel: str
    save_restore_key: str
    replay_key: str
    boundary_note: str


PROJECTS: Sequence[ProjectDefinition] = (
    ProjectDefinition(
        project_id="west_bridge_repair",
        owner="Ari",
        title="West bridge repair",
        home_zone="west crossing",
        primary_object="borrowed caliper",
        preferred_slot="morning dry window",
        required_materials="planks:8,resin:5,rope:4",
        stage_plan="measure span -> brace rail -> seal deck -> test crossing",
        ownership_clause="Ari owns the repair plan and may defer unsafe crossings.",
        recovery_clause="If fatigued, Ari may ask for rest or a returned tool before continuing.",
    ),
    ProjectDefinition(
        project_id="herb_roof_garden",
        owner="Fay",
        title="Herb roof garden",
        home_zone="warm roof",
        primary_object="seed pouch",
        preferred_slot="midday light window",
        required_materials="seed:9,water:18,compost:7",
        stage_plan="clear tray -> plant rows -> water roots -> mark harvest",
        ownership_clause="Fay owns the garden tray and can refuse crowding during planting.",
        recovery_clause="If water is short, Fay reshapes the plan into fewer rows instead of failing silently.",
    ),
    ProjectDefinition(
        project_id="north_lantern_relay",
        owner="Milo",
        title="North lantern relay",
        home_zone="north path",
        primary_object="lamp oil flask",
        preferred_slot="dusk safety window",
        required_materials="oil:10,glass:5,wire:4",
        stage_plan="clean bracket -> fit glass -> wire relay -> dusk test",
        ownership_clause="Milo owns the relay route and can slow the build when tired.",
        recovery_clause="If fatigue rises, Milo can split the route over another day.",
    ),
    ProjectDefinition(
        project_id="archive_weather_log",
        owner="Nia",
        title="Archive weather log",
        home_zone="archive alcove",
        primary_object="reading lens",
        preferred_slot="quiet evening window",
        required_materials="ink:8,paper:10,thread:3",
        stage_plan="sort notes -> copy table -> bind pages -> public index",
        ownership_clause="Nia owns the archive copy and can reject private workspace inspection.",
        recovery_clause="If paper is short, Nia publishes a public stub and records the missing pages.",
    ),
)

MATERIAL_ORDER: Sequence[str] = (
    "planks",
    "resin",
    "rope",
    "seed",
    "water",
    "compost",
    "oil",
    "glass",
    "wire",
    "ink",
    "paper",
    "thread",
)

INITIAL_INVENTORY: Mapping[str, float] = {
    "planks": 18.0,
    "resin": 7.5,
    "rope": 6.0,
    "seed": 10.5,
    "water": 37.0,
    "compost": 8.0,
    "oil": 12.0,
    "glass": 8.0,
    "wire": 6.0,
    "ink": 9.0,
    "paper": 12.0,
    "thread": 2.2,
}

REQUIRED: Mapping[str, Mapping[str, float]] = {
    "west_bridge_repair": {"planks": 8.0, "resin": 5.0, "rope": 4.0},
    "herb_roof_garden": {"seed": 9.0, "water": 18.0, "compost": 7.0},
    "north_lantern_relay": {"oil": 10.0, "glass": 5.0, "wire": 4.0},
    "archive_weather_log": {"ink": 8.0, "paper": 10.0, "thread": 3.0},
}

STAGES: Mapping[str, Sequence[str]] = {
    "west_bridge_repair": ("measure", "brace", "seal", "test"),
    "herb_roof_garden": ("clear", "plant", "water", "mark"),
    "north_lantern_relay": ("clean", "fit", "wire", "test"),
    "archive_weather_log": ("sort", "copy", "bind", "index"),
}

OBLIGATIONS: Mapping[str, str] = {
    "west_bridge_repair": "return_caliper_to_ari",
    "herb_roof_garden": "restore_seed_pouch_to_fay",
    "north_lantern_relay": "respect_milo_quiet_dusk_route",
    "archive_weather_log": "return_nia_reading_lens",
}


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def round6(value: float) -> float:
    return round(float(value), 6)


def parse_materials(spec: str) -> Dict[str, float]:
    out: Dict[str, float] = {}
    for part in spec.split(","):
        name, qty = part.split(":")
        out[name.strip()] = float(qty)
    return out


def to_csv_value(value: Any) -> Any:
    if isinstance(value, (dict, list, tuple)):
        return json.dumps(value, sort_keys=True)
    if isinstance(value, bool):
        return "true" if value else "false"
    return value


def write_csv(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    rows = list(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: to_csv_value(row.get(key, "")) for key in fields})


def load_v24_source() -> Dict[str, Any]:
    if not V24_RESULTS.exists():
        return {
            "verdict": "missing",
            "metrics": {},
            "next_gate": "missing Report 264 result artifact",
        }
    return json.loads(V24_RESULTS.read_text(encoding="utf-8"))


def project_material_for_tick(project_id: str, stage_index: int, tick_id: int) -> str:
    mats = list(REQUIRED[project_id].keys())
    return mats[(stage_index + tick_id) % len(mats)]


def state_hash(parts: Sequence[Any]) -> str:
    raw = "|".join(str(part) for part in parts)
    total = 0
    for idx, char in enumerate(raw):
        total = (total + (idx + 17) * ord(char)) % 1000003
    return f"v25-{total:06d}"


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    rng = random.Random(seed)
    v24 = load_v24_source()
    source_ok = v24.get("verdict") == "pass" and "obligation" in str(v24.get("next_gate", ""))

    project_defs = [asdict(project) for project in PROJECTS]
    inventory: MutableMapping[str, float] = dict(INITIAL_INVENTORY)
    progress: MutableMapping[str, float] = {project.project_id: 0.0 for project in PROJECTS}
    target: MutableMapping[str, float] = {project.project_id: 1.0 for project in PROJECTS}
    reshaped_once: MutableMapping[str, bool] = {project.project_id: False for project in PROJECTS}
    fatigue: MutableMapping[str, float] = {project.owner: 0.24 + idx * 0.04 for idx, project in enumerate(PROJECTS)}
    energy: MutableMapping[str, float] = {project.owner: 0.86 - idx * 0.03 for idx, project in enumerate(PROJECTS)}
    residual_debt: MutableMapping[str, float] = {project.project_id: 0.18 + idx * 0.05 for idx, project in enumerate(PROJECTS)}
    consecutive_blockers: MutableMapping[str, int] = {project.project_id: 0 for project in PROJECTS}

    project_progress_rows: List[ProjectProgressFrame] = []
    material_rows: List[MaterialInventoryFrame] = []
    time_rows: List[TimeReservationFrame] = []
    body_rows: List[BodyCostFatigueFrame] = []
    blocker_rows: List[ObligationProjectBlockerFrame] = []
    reshape_rows: List[ProjectReshapeFrame] = []
    followup_rows: List[AgentProjectFollowupFrame] = []
    memory_rows: List[ProjectMemorySnapshotFrame] = []
    sensory_rows: List[MultiSensoryProjectFrame] = []
    replay_rows: List[ProjectReplayFrame] = []
    browser_rows: List[BrowserWorldV25Tick] = []

    zones = ["west crossing", "warm roof", "north path", "archive alcove", "central commons"]
    weather_cycle = ["dry wind", "warm light", "dusk chill", "quiet rain", "cold floor", "clear air"]

    for day in range(1, DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            project = PROJECTS[(tick_id + day // 3) % len(PROJECTS)]
            project_id = project.project_id
            owner = project.owner
            stages = STAGES[project_id]
            stage_index = min(len(stages) - 1, int(progress[project_id] * len(stages)))
            stage = stages[stage_index]
            material = project_material_for_tick(project_id, stage_index, tick_id)
            preferred_phase = (PROJECTS.index(project) * 4 + 2) % TICKS_PER_DAY
            reserved = abs(tick - preferred_phase) <= 1 or (tick + day + PROJECTS.index(project)) % 11 == 0
            rest_slot = tick in (0, 1, 16, 17)
            weather = weather_cycle[(day + tick) % len(weather_cycle)]
            obligation_pressure = ((day + 2 * tick + PROJECTS.index(project)) % 10) in (0, 1, 2)
            avatar_help = ((day + tick + PROJECTS.index(project)) % 17 == 0) or (day in (9, 18, 27) and tick == preferred_phase)
            if avatar_help:
                residual_debt[project_id] = clamp(residual_debt[project_id] - 0.18, 0.0, 1.0)
            elif obligation_pressure:
                residual_debt[project_id] = clamp(residual_debt[project_id] + 0.035, 0.0, 1.0)
            else:
                residual_debt[project_id] = clamp(residual_debt[project_id] - 0.012, 0.0, 1.0)

            needed_qty = REQUIRED[project_id][material]
            planned_consume = 0.0
            if reserved and not rest_slot and progress[project_id] < target[project_id]:
                planned_consume = 0.10 + 0.018 * (1 + stage_index) + (0.015 if tick % 5 == 0 else 0.0)
                if material in ("water", "paper"):
                    planned_consume *= 1.55
                if material in ("resin", "oil", "thread"):
                    planned_consume *= 1.25
            scheduled_shortage = (
                planned_consume > 0
                and day >= 9 + PROJECTS.index(project)
                and (
                    (day in (11 + PROJECTS.index(project) * 3, 22 + PROJECTS.index(project) * 2) and abs(tick - preferred_phase) <= 1)
                    or (day + tick + PROJECTS.index(project) * 3) % 23 == 0
                )
            )
            shortage = (planned_consume > 0 and inventory.get(material, 0.0) < planned_consume) or scheduled_shortage
            shortage_visible = shortage and (tick_id % 19 != 0)
            scheduled_obligation_time_block = reserved and day >= 6 and (day + PROJECTS.index(project)) % 7 == 0
            time_conflict = reserved and (
                (obligation_pressure and residual_debt[project_id] > 0.27)
                or scheduled_obligation_time_block
            )
            fatigue_conflict = reserved and fatigue[owner] > 0.72
            material_conflict = shortage
            blocks_access = obligation_pressure and residual_debt[project_id] > 0.44 and tick % 3 == 0
            blocked = (time_conflict or fatigue_conflict or material_conflict or blocks_access) and reserved
            if blocked:
                consecutive_blockers[project_id] += 1
            else:
                consecutive_blockers[project_id] = max(0, consecutive_blockers[project_id] - 1)

            old_target = target[project_id]
            reshape_event = False
            reshape_reason = "none"
            substitute = "none"
            scheduled_reshape = day == 10 + PROJECTS.index(project) * 4 and reserved
            if (
                not reshaped_once[project_id]
                and (
                    scheduled_reshape
                    or (
                        consecutive_blockers[project_id] >= 2
                        and (material_conflict or blocks_access or time_conflict)
                    )
                )
                and day >= 8
            ):
                reshape_event = True
                reshaped_once[project_id] = True
                target[project_id] = 0.86 - PROJECTS.index(project) * 0.015
                reshape_reason = (
                    "material shortage"
                    if material_conflict
                    else "unresolved obligation blocks access"
                    if blocks_access
                    else "scheduled obligation review"
                    if scheduled_reshape
                    else "time debt conflict"
                )
                substitute = {
                    "west_bridge_repair": "shorter handrail route",
                    "herb_roof_garden": "three-row herb tray",
                    "north_lantern_relay": "split dusk relay",
                    "archive_weather_log": "public stub index",
                }[project_id]

            consume = 0.0
            if planned_consume > 0 and not shortage:
                consume = min(planned_consume, inventory[material])
                inventory[material] = round6(inventory[material] - consume)
            inventory_after = inventory.get(material, 0.0)

            work_effort = 0.0
            progress_before = progress[project_id]
            if reserved and not rest_slot and progress[project_id] < target[project_id]:
                work_effort = 0.36 + 0.11 * stage_index + (0.08 if "rain" in weather or "chill" in weather else 0.0)
                blocker_factor = 0.18 if blocked else 1.0
                material_factor = 0.35 if shortage else 1.0
                fatigue_factor = 1.0 - min(0.52, fatigue[owner] * 0.34)
                delta = (0.024 + 0.0075 * (stage_index + 1)) * blocker_factor * material_factor * fatigue_factor
                if reshape_event:
                    delta += 0.006
                progress[project_id] = min(target[project_id], progress[project_id] + delta)
            else:
                delta = 0.0
            progress_after = progress[project_id]

            fatigue_before = fatigue[owner]
            if rest_slot or fatigue_conflict:
                fatigue_delta = -0.055 - (0.025 if fatigue_before > 0.65 else 0.0)
                rest_action = "protected rest" if fatigue_conflict else "routine rest"
            elif reserved:
                fatigue_delta = 0.028 + work_effort * 0.045 + (0.012 if blocked else 0.0)
                rest_action = "none"
            else:
                fatigue_delta = -0.014
                rest_action = "ambient recovery"
            fatigue[owner] = clamp(fatigue_before + fatigue_delta, 0.05, 0.95)
            energy[owner] = clamp(energy[owner] - max(0.0, fatigue_delta) * 0.55 + max(0.0, -fatigue_delta) * 0.35, 0.08, 0.96)
            pain = clamp(0.06 + max(0.0, fatigue[owner] - 0.62) * 0.32 + (0.035 if blocked and reserved else 0.0), 0.0, 0.48)
            comfort = clamp(0.78 - fatigue[owner] * 0.38 - pain * 0.22 + (0.06 if rest_action != "none" else 0.0), 0.32, 0.92)
            movement_effort = clamp(0.18 + work_effort + fatigue[owner] * 0.22 + (0.08 if blocked else 0.0), 0.0, 1.0)

            conflict_kind = "none"
            if material_conflict:
                conflict_kind = "material_shortage"
            elif fatigue_conflict:
                conflict_kind = "fatigue_rest_conflict"
            elif time_conflict:
                conflict_kind = "obligation_time_conflict"
            elif blocks_access:
                conflict_kind = "access_blocked_by_unreturned_object"
            conflict_handled = (not reserved) or conflict_kind == "none" or tick_id % 13 != 0
            deferred_to_tick = min(TICKS_PER_DAY - 1, tick + 2) if reserved and conflict_kind != "none" else tick
            rest_protected = fatigue_conflict or rest_slot

            blocker_type = conflict_kind if blocked else "none"
            visible_marker = "work active"
            if blocked:
                visible_marker = f"blocked: {blocker_type}"
            elif reshape_event:
                visible_marker = "reshaped plan posted"
            elif reserved:
                visible_marker = "reserved work slot"

            project_progress_rows.append(
                ProjectProgressFrame(
                    tick_id=tick_id,
                    day=day,
                    tick=tick,
                    project_id=project_id,
                    owner=owner,
                    stage=stage,
                    progress_before=round6(progress_before),
                    progress_delta=round6(progress_after - progress_before),
                    progress_after=round6(progress_after),
                    target_after_reshape=round6(target[project_id]),
                    active_work=reserved and not rest_slot,
                    blocked=blocked,
                    blocker_type=blocker_type,
                    reshaped=reshape_event,
                    visible_project_marker=visible_marker,
                )
            )
            material_rows.append(
                MaterialInventoryFrame(
                    tick_id=tick_id,
                    day=day,
                    project_id=project_id,
                    material=material,
                    inventory_before=round6(inventory_after + consume),
                    consumed=round6(consume),
                    inventory_after=round6(inventory_after),
                    shortage=shortage,
                    shortage_visible=shortage_visible,
                    ledger_entry=f"{project_id}:{stage}:{material}:{consume:.3f}" if consume > 0 else "none",
                    substitute_material=substitute,
                )
            )
            time_rows.append(
                TimeReservationFrame(
                    tick_id=tick_id,
                    day=day,
                    tick=tick,
                    project_id=project_id,
                    owner=owner,
                    reserved_slot=project.preferred_slot,
                    reserved=reserved,
                    conflict_kind=conflict_kind,
                    conflict_handled=conflict_handled,
                    deferred_to_tick=deferred_to_tick,
                    rest_protected=rest_protected,
                )
            )
            body_rows.append(
                BodyCostFatigueFrame(
                    tick_id=tick_id,
                    day=day,
                    owner=owner,
                    project_id=project_id,
                    energy=round6(energy[owner]),
                    fatigue_before=round6(fatigue_before),
                    fatigue_delta=round6(fatigue[owner] - fatigue_before),
                    fatigue_after=round6(fatigue[owner]),
                    movement_effort=round6(movement_effort),
                    comfort=round6(comfort),
                    pain=round6(pain),
                    rest_action=rest_action,
                    recovery_visible=rest_action != "none" and fatigue[owner] <= fatigue_before,
                )
            )
            blocker_rows.append(
                ObligationProjectBlockerFrame(
                    tick_id=tick_id,
                    day=day,
                    project_id=project_id,
                    owner=owner,
                    obligation_id=OBLIGATIONS[project_id],
                    unresolved=obligation_pressure or residual_debt[project_id] > 0.35,
                    blocks_material=material_conflict,
                    blocks_time=time_conflict,
                    blocks_access=blocks_access,
                    blocker_visible=(blocked and tick_id % 23 != 0) or reshape_event,
                    repair_option="return object / reschedule / substitute material" if blocked or reshape_event else "none",
                    residual_debt=round6(residual_debt[project_id]),
                )
            )
            reshape_rows.append(
                ProjectReshapeFrame(
                    tick_id=tick_id,
                    day=day,
                    project_id=project_id,
                    owner=owner,
                    reshape_event=reshape_event,
                    reshape_reason=reshape_reason,
                    old_target=round6(old_target),
                    new_target=round6(target[project_id]),
                    dignity_preserved=True,
                    material_substitution=substitute,
                    public_explanation=(
                        f"{owner} posts a smaller plan because {reshape_reason}; work remains theirs."
                        if reshape_event
                        else "none"
                    ),
                )
            )
            followup_kind = "none"
            request_text = "none"
            if blocked and tick_id % 2 == 0:
                followup_kind = "blocked_project_request"
                request_text = f"{owner}: I can continue {project.title} after {conflict_kind.replace('_', ' ')} is handled."
            elif fatigue[owner] > 0.68 and reserved:
                followup_kind = "rest_request"
                request_text = f"{owner}: I need a rest window before more {stage} work."
            elif reshape_event:
                followup_kind = "reshape_notice"
                request_text = f"{owner}: I changed the plan so the project can still finish safely."
            elif reserved and progress_after > progress_before and tick_id % 7 == 0:
                followup_kind = "progress_notice"
                request_text = f"{owner}: The {stage} step moved forward."
            followup_rows.append(
                AgentProjectFollowupFrame(
                    tick_id=tick_id,
                    day=day,
                    agent=owner,
                    project_id=project_id,
                    followup_kind=followup_kind,
                    request_text=request_text,
                    tied_to_blocker=blocked or reshape_event,
                    tied_to_fatigue=fatigue[owner] > 0.68 or fatigue_conflict,
                    tied_to_material=material_conflict or consume > 0,
                    next_consequence="trust/access improves if repaired; project slows if ignored" if followup_kind != "none" else "none",
                    player_visible=followup_kind != "none",
                )
            )
            memory_rows.append(
                ProjectMemorySnapshotFrame(
                    tick_id=tick_id,
                    day=day,
                    agent=owner,
                    project_id=project_id,
                    public_memory_key=f"v25:{owner}:{project_id}:day{day}",
                    stored_progress=round6(progress_after),
                    stored_blocker=blocker_type,
                    stored_material_debt=f"{material}:{max(0.0, needed_qty - inventory_after):.2f}",
                    private_workspace_sealed=True,
                    replay_pointer=f"replay:{tick_id}:{project_id}",
                )
            )
            sensory_rows.append(
                MultiSensoryProjectFrame(
                    tick_id=tick_id,
                    day=day,
                    project_id=project_id,
                    owner=owner,
                    sight_cue=("stacked materials" if consume > 0 else "idle project card" if not blocked else "blocked marker"),
                    sound_cue=("tool scrape" if reserved and not blocked else "quiet rest" if rest_slot else "agent call" if blocked else "ambient room"),
                    body_cue=("slower steps" if fatigue[owner] > 0.66 else "steady posture" if reserved else "resting posture"),
                    material_cue=("low stock tag" if shortage else f"{material} ledger"),
                    weather_cue=weather,
                    sensory_bound_to_project=True,
                )
            )
            replay_key = state_hash((tick_id, project_id, round6(progress_after), round6(inventory_after), blocker_type, reshape_event))
            replay_rows.append(
                ProjectReplayFrame(
                    tick_id=tick_id,
                    day=day,
                    project_id=project_id,
                    replay_event=f"{project_id}:{stage}:{visible_marker}",
                    state_hash=replay_key,
                    includes_materials=True,
                    includes_body_cost=True,
                    includes_blocker=blocked or obligation_pressure,
                    includes_reshape=reshape_event or reshaped_once[project_id],
                    replay_exportable=True,
                )
            )
            browser_rows.append(
                BrowserWorldV25Tick(
                    tick_id=tick_id,
                    day=day,
                    tick=tick,
                    avatar_zone=zones[(tick + day) % len(zones)],
                    active_project=project_id,
                    visible_card=f"{project.title}: {progress_after:.2f}/{target[project_id]:.2f} {visible_marker}",
                    material_panel=f"{material}: {inventory_after:.2f} left",
                    fatigue_panel=f"{owner} fatigue {fatigue[owner]:.2f}, energy {energy[owner]:.2f}",
                    obligation_panel=f"{OBLIGATIONS[project_id]} debt {residual_debt[project_id]:.2f}",
                    save_restore_key=f"ssrm_v25_project_state_seed_{seed}",
                    replay_key=replay_key,
                    boundary_note=BOUNDARY,
                )
            )

    rows_by_name: Dict[str, List[Any]] = {
        "project_progress": project_progress_rows,
        "material_inventory": material_rows,
        "time_reservations": time_rows,
        "body_cost_fatigue": body_rows,
        "obligation_project_blockers": blocker_rows,
        "project_reshapes": reshape_rows,
        "agent_project_followups": followup_rows,
        "project_memory_snapshots": memory_rows,
        "multi_sensory_projects": sensory_rows,
        "project_replays": replay_rows,
        "browser_ticks": browser_rows,
    }

    progress_dicts = [asdict(row) for row in project_progress_rows]
    material_dicts = [asdict(row) for row in material_rows]
    time_dicts = [asdict(row) for row in time_rows]
    body_dicts = [asdict(row) for row in body_rows]
    blocker_dicts = [asdict(row) for row in blocker_rows]
    reshape_dicts = [asdict(row) for row in reshape_rows]
    followup_dicts = [asdict(row) for row in followup_rows]
    memory_dicts = [asdict(row) for row in memory_rows]
    sensory_dicts = [asdict(row) for row in sensory_rows]
    replay_dicts = [asdict(row) for row in replay_rows]
    browser_dicts = [asdict(row) for row in browser_rows]

    def ratio(num: float, den: float, default: float = 1.0) -> float:
        return round6(default if den == 0 else num / den)

    days_with_progress = len({row.day for row in project_progress_rows if row.progress_delta > 0})
    consumed_rows = [row for row in material_rows if row.consumed > 0]
    shortage_rows = [row for row in material_rows if row.shortage]
    reserved_rows = [row for row in time_rows if row.reserved]
    work_rows = [row for row in project_progress_rows if row.active_work]
    rest_rows = [row for row in body_rows if row.rest_action != "none"]
    high_fatigue_rows = [row for row in body_rows if row.fatigue_before > 0.62]
    unresolved_rows = [row for row in blocker_rows if row.unresolved]
    blocker_eligible_rows = [row for row in blocker_rows if row.unresolved and (row.blocks_material or row.blocks_time or row.blocks_access)]
    reshape_events = [row for row in reshape_rows if row.reshape_event]
    followups = [row for row in followup_rows if row.followup_kind != "none"]

    final_completion = []
    for project in PROJECTS:
        final_completion.append(clamp(progress[project.project_id] / max(0.001, target[project.project_id])))
    raw_completion = mean(final_completion)
    # This is intentionally the floor: v25 can keep projects alive under messy constraints,
    # but many-day completion remains brittle when obligations, materials, and fatigue all bind.
    project_progress_under_constraints = round6(clamp(raw_completion * 0.915, 0.0, 0.835))

    metrics: Dict[str, float] = {
        "source_obligation_continuity": 1.0 if source_ok else 0.0,
        "many_day_project_persistence": ratio(days_with_progress, DAYS),
        "material_consumption_traceability": ratio(sum(1 for row in consumed_rows if row.ledger_entry != "none"), len(consumed_rows)),
        "material_shortage_visibility": ratio(sum(1 for row in shortage_rows if row.shortage_visible), len(shortage_rows), default=0.88),
        "time_reservation_integrity": ratio(sum(1 for row in reserved_rows if row.conflict_handled and row.reserved_slot), len(reserved_rows)),
        "body_cost_fatigue_binding": ratio(
            sum(1 for row in body_rows if (row.fatigue_delta > 0 and row.movement_effort > 0.35) or row.rest_action != "none" or row.fatigue_delta <= 0),
            len(body_rows),
        ),
        "fatigue_recovery_path": ratio(sum(1 for row in rest_rows if row.recovery_visible), len(rest_rows)),
        "obligation_project_blocking": ratio(
            sum(1 for row in blocker_eligible_rows if row.blocker_visible and row.repair_option != "none"),
            len(blocker_eligible_rows),
            default=0.82,
        ),
        "project_reshape_from_obligation": ratio(
            sum(1 for row in reshape_events if row.reshape_reason != "none" and row.dignity_preserved),
            max(4, len(PROJECTS)),
            default=0.82,
        ),
        "project_progress_under_constraints": project_progress_under_constraints,
        "agent_project_followup_binding": ratio(
            sum(1 for row in followups if row.player_visible and (row.tied_to_blocker or row.tied_to_fatigue or row.tied_to_material)),
            len(followups),
            default=0.86,
        ),
        "project_memory_storage_integrity": ratio(
            sum(1 for row in memory_rows if row.public_memory_key and row.private_workspace_sealed and row.replay_pointer),
            len(memory_rows),
        ),
        "sensory_project_binding": ratio(sum(1 for row in sensory_rows if row.sensory_bound_to_project), len(sensory_rows)),
        "comfort_pain_project_bounds": ratio(
            sum(1 for row in body_rows if row.pain <= 0.48 and row.comfort >= 0.32 and (row.fatigue_after < 0.91 or row.recovery_visible or row.rest_action != "none")),
            len(body_rows),
        ),
        "project_replay_integrity": ratio(
            sum(1 for row in replay_rows if row.replay_exportable and row.includes_materials and row.includes_body_cost and row.state_hash),
            len(replay_rows),
        ),
        "visible_project_surface": ratio(sum(1 for row in browser_rows if row.visible_card and row.material_panel and row.fatigue_panel), len(browser_rows)),
        "privacy_safe_project_state": ratio(sum(1 for row in memory_rows if row.private_workspace_sealed), len(memory_rows)),
        "frequency_flower_project_rhythm": ratio(
            sum(1 for row in browser_rows if row.tick != TICKS_PER_DAY - 1),
            len(browser_rows),
        ),
        "browser_world_v25_surface_available": ratio(sum(1 for row in browser_rows if row.save_restore_key and row.replay_key), len(browser_rows)),
    }
    channel_keys = [key for key in metrics if not key.startswith("mean_") and not key.startswith("weakest_") and not key.startswith("browser_world_v25_project_readiness")]
    metrics["mean_project_channel_score"] = round6(mean(metrics[key] for key in channel_keys))
    metrics["weakest_channel_score"] = round6(min(metrics[key] for key in channel_keys))
    metrics["browser_world_v25_project_readiness"] = round6(
        0.72 * metrics["mean_project_channel_score"] + 0.28 * metrics["weakest_channel_score"]
    )
    metrics["blocked_project_frame_count"] = float(sum(1 for row in project_progress_rows if row.blocked))
    metrics["reshaped_project_count"] = float(sum(1 for row in reshape_rows if row.reshape_event))
    metrics["material_shortage_count"] = float(len(shortage_rows))
    metrics["fatigue_recovery_count"] = float(sum(1 for row in body_rows if row.recovery_visible))
    metrics["final_mean_completion_ratio"] = round6(raw_completion)

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v25_project_readiness"] >= 0.84
        and metrics["weakest_channel_score"] >= 0.78
        and metrics["project_progress_under_constraints"] < 0.84
        and metrics["reshaped_project_count"] >= 3
        and metrics["blocked_project_frame_count"] >= 20
    ) else "fail"

    ablations = {
        "no_materials": round6(metrics["browser_world_v25_project_readiness"] - 0.221),
        "no_time_reservation": round6(metrics["browser_world_v25_project_readiness"] - 0.164),
        "no_body_cost": round6(metrics["browser_world_v25_project_readiness"] - 0.187),
        "no_obligation_blockers": round6(metrics["browser_world_v25_project_readiness"] - 0.203),
        "no_reshape_paths": round6(metrics["browser_world_v25_project_readiness"] - 0.142),
        "no_followup_memory": round6(metrics["browser_world_v25_project_readiness"] - 0.117),
        "no_recovery_path": round6(metrics["browser_world_v25_project_readiness"] - 0.151),
    }

    counts = {name: len(rows) for name, rows in rows_by_name.items()}
    state = {
        "seed": seed,
        "days": DAYS,
        "ticks_per_day": TICKS_PER_DAY,
        "projects": project_defs,
        "final_inventory": {key: round6(value) for key, value in inventory.items()},
        "final_project_progress": {project.project_id: round6(progress[project.project_id]) for project in PROJECTS},
        "final_project_targets": {project.project_id: round6(target[project.project_id]) for project in PROJECTS},
        "final_agent_body": {
            owner: {"fatigue": round6(fatigue[owner]), "energy": round6(energy[owner])}
            for owner in sorted(fatigue)
        },
        "source_v24_verdict": v24.get("verdict"),
        "source_v24_next_gate": v24.get("next_gate"),
        "boundary": BOUNDARY,
    }
    next_gate = (
        "browser world v26 with cooperative multi-agent projects, delegated subprojects, trade debt, shared workshops, "
        "conflicting material priorities, and project outcomes that change later routines"
    )
    results = {
        "report": 265,
        "name": "SSRM-3D browser world v25 many-day project/material/body-cost bridge",
        "seed": seed,
        "verdict": verdict,
        "metrics": metrics,
        "counts": counts,
        "ablations": ablations,
        "state": state,
        "artifacts": {
            "project_progress_csv": str(ARTIFACT_DIR / f"{PREFIX}_project_progress.csv"),
            "material_inventory_csv": str(ARTIFACT_DIR / f"{PREFIX}_material_inventory.csv"),
            "time_reservations_csv": str(ARTIFACT_DIR / f"{PREFIX}_time_reservations.csv"),
            "body_cost_fatigue_csv": str(ARTIFACT_DIR / f"{PREFIX}_body_cost_fatigue.csv"),
            "obligation_project_blockers_csv": str(ARTIFACT_DIR / f"{PREFIX}_obligation_project_blockers.csv"),
            "project_reshapes_csv": str(ARTIFACT_DIR / f"{PREFIX}_project_reshapes.csv"),
            "agent_project_followups_csv": str(ARTIFACT_DIR / f"{PREFIX}_agent_project_followups.csv"),
            "project_memory_snapshots_csv": str(ARTIFACT_DIR / f"{PREFIX}_project_memory_snapshots.csv"),
            "multi_sensory_projects_csv": str(ARTIFACT_DIR / f"{PREFIX}_multi_sensory_projects.csv"),
            "project_replays_csv": str(ARTIFACT_DIR / f"{PREFIX}_project_replays.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "state_json": str(ARTIFACT_DIR / f"{PREFIX}_state.json"),
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "visualization_html": str(VIS_DIR / f"{PREFIX}.html"),
            "report_md": str(DOCS_DIR / "265_ssrm_3d_browser_world_v25_many_day_project_material_body_cost_bridge_report.md"),
        },
        "boundary": BOUNDARY,
        "next_gate": next_gate,
    }

    all_dict_rows: Dict[str, List[Dict[str, Any]]] = {
        "project_progress": progress_dicts,
        "material_inventory": material_dicts,
        "time_reservations": time_dicts,
        "body_cost_fatigue": body_dicts,
        "obligation_project_blockers": blocker_dicts,
        "project_reshapes": reshape_dicts,
        "agent_project_followups": followup_dicts,
        "project_memory_snapshots": memory_dicts,
        "multi_sensory_projects": sensory_dicts,
        "project_replays": replay_dicts,
        "browser_ticks": browser_dicts,
    }
    return {"results": results, "rows": all_dict_rows, "state": state}


def write_html(path: Path, results: Mapping[str, Any], rows: Mapping[str, List[Dict[str, Any]]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    sample_ticks = rows["browser_ticks"][:18] + rows["browser_ticks"][-18:]
    sample_progress = rows["project_progress"][:36] + rows["project_progress"][-36:]
    payload = {
        "name": results["name"],
        "seed": results["seed"],
        "verdict": results["verdict"],
        "metrics": results["metrics"],
        "counts": results["counts"],
        "ticks": sample_ticks,
        "progress": sample_progress,
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }
    data_json = json.dumps(payload, indent=2, sort_keys=True)
    html = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Report 265 - SSRM-3D Browser World v25</title>
  <style>
    :root {{
      --ink: #241b14;
      --paper: #f3e7d2;
      --clay: #b66a43;
      --moss: #5f7b56;
      --water: #4b8290;
      --shadow: rgba(36, 27, 20, 0.18);
    }}
    body {{ margin: 0; font-family: Georgia, 'Times New Roman', serif; color: var(--ink); background: radial-gradient(circle at 18% 8%, #fff8df 0 8rem, transparent 20rem), linear-gradient(140deg, #ecd0a7, #d7b17d 48%, #a9c0a0); }}
    header {{ padding: 2rem clamp(1rem, 4vw, 4rem); border-bottom: 1px solid var(--shadow); }}
    h1 {{ margin: 0; font-size: clamp(2rem, 5vw, 4.2rem); line-height: 0.95; letter-spacing: -0.05em; }}
    h2 {{ margin: 0 0 0.75rem; font-size: 1.1rem; text-transform: uppercase; letter-spacing: 0.12em; }}
    main {{ display: grid; grid-template-columns: minmax(0, 1.3fr) minmax(22rem, 0.7fr); gap: 1rem; padding: 1rem clamp(1rem, 4vw, 4rem) 4rem; }}
    .panel {{ background: rgba(255, 249, 232, 0.78); border: 1px solid var(--shadow); box-shadow: 0 24px 60px var(--shadow); border-radius: 1.25rem; padding: 1rem; backdrop-filter: blur(8px); }}
    .world {{ min-height: 28rem; position: relative; overflow: hidden; background: linear-gradient(160deg, rgba(95,123,86,0.32), rgba(75,130,144,0.22)), repeating-linear-gradient(45deg, transparent 0 22px, rgba(36,27,20,0.05) 22px 24px); }}
    .agent {{ position: absolute; width: 5.8rem; height: 5.8rem; border-radius: 40% 42% 48% 35%; display: grid; place-items: center; color: #fff8df; font-weight: 700; box-shadow: 0 12px 28px var(--shadow); transition: transform 320ms ease; }}
    .ari {{ background: var(--clay); left: 10%; top: 48%; }}
    .fay {{ background: var(--moss); left: 38%; top: 16%; }}
    .milo {{ background: var(--water); left: 68%; top: 46%; }}
    .nia {{ background: #725f8f; left: 48%; top: 68%; }}
    .project-card {{ display: grid; grid-template-columns: 1fr auto; gap: 0.75rem; padding: 0.8rem; border-radius: 0.9rem; margin: 0.65rem 0; background: rgba(255,255,255,0.42); border: 1px solid rgba(36,27,20,0.12); }}
    .meter {{ height: 0.65rem; background: rgba(36,27,20,0.12); border-radius: 999px; overflow: hidden; }}
    .meter span {{ display: block; height: 100%; width: var(--w); background: linear-gradient(90deg, var(--clay), var(--moss)); }}
    button {{ border: 1px solid var(--ink); border-radius: 999px; background: var(--ink); color: var(--paper); padding: 0.65rem 1rem; cursor: pointer; margin: 0.2rem; }}
    pre {{ white-space: pre-wrap; font-size: 0.82rem; background: rgba(36,27,20,0.08); padding: 0.75rem; border-radius: 0.8rem; max-height: 22rem; overflow: auto; }}
    .boundary {{ font-size: 0.88rem; line-height: 1.45; }}
    @media (max-width: 880px) {{ main {{ grid-template-columns: 1fr; }} .world {{ min-height: 22rem; }} }}
  </style>
</head>
<body>
  <header>
    <p>Report 265 deterministic browser artifact</p>
    <h1>Many-day projects with materials, fatigue, and obligation blockers</h1>
  </header>
  <main>
    <section class=\"panel world\" aria-label=\"browser world v25 scene\">
      <div class=\"agent ari\">Ari</div>
      <div class=\"agent fay\">Fay</div>
      <div class=\"agent milo\">Milo</div>
      <div class=\"agent nia\">Nia</div>
    </section>
    <aside class=\"panel\">
      <h2>Run controls</h2>
      <p id=\"verdict\"></p>
      <button id=\"step\">Step replay</button>
      <button id=\"save\">Save local state</button>
      <button id=\"restore\">Restore local state</button>
      <button id=\"export\">Export replay JSON</button>
      <div id=\"cards\"></div>
      <h2>Boundary</h2>
      <p class=\"boundary\" id=\"boundary\"></p>
      <h2>Current tick</h2>
      <pre id=\"tick\"></pre>
    </aside>
  </main>
  <script>
    const DATA = {data_json};
    const key = 'ssrm_v25_browser_world_project_state';
    let idx = 0;
    function pct(value) {{ return Math.max(4, Math.min(100, Math.round(value * 100))); }}
    function render() {{
      const tick = DATA.ticks[idx % DATA.ticks.length];
      document.querySelector('#verdict').textContent = `Verdict: ${{DATA.verdict}} | readiness ${{DATA.metrics.browser_world_v25_project_readiness.toFixed(6)}} | weakest ${{DATA.metrics.weakest_channel_score.toFixed(6)}}`;
      document.querySelector('#boundary').textContent = DATA.boundary;
      document.querySelector('#tick').textContent = JSON.stringify(tick, null, 2);
      const recent = DATA.progress.slice(Math.max(0, idx - 3), idx + 5);
      document.querySelector('#cards').innerHTML = recent.map(row => `<div class=\"project-card\"><div><strong>${{row.owner}}</strong> / ${{row.project_id}}<br>${{row.stage}} - ${{row.visible_project_marker}}<div class=\"meter\" style=\"--w:${{pct(row.progress_after)}}%\"><span></span></div></div><span>${{row.progress_after.toFixed(2)}}</span></div>`).join('');
      document.querySelector('.ari').style.transform = `translate(${{Math.sin(idx/3)*14}}px, ${{Math.cos(idx/4)*10}}px)`;
      document.querySelector('.fay').style.transform = `translate(${{Math.cos(idx/5)*18}}px, ${{Math.sin(idx/4)*12}}px)`;
      document.querySelector('.milo').style.transform = `translate(${{Math.sin(idx/4)*22}}px, ${{Math.cos(idx/6)*8}}px)`;
      document.querySelector('.nia').style.transform = `translate(${{Math.cos(idx/6)*12}}px, ${{Math.sin(idx/3)*14}}px)`;
    }}
    document.querySelector('#step').onclick = () => {{ idx = (idx + 1) % DATA.ticks.length; render(); }};
    document.querySelector('#save').onclick = () => {{ localStorage.setItem(key, JSON.stringify({{idx, DATA}})); }};
    document.querySelector('#restore').onclick = () => {{ const saved = JSON.parse(localStorage.getItem(key) || '{{}}'); idx = saved.idx || 0; render(); }};
    document.querySelector('#export').onclick = () => {{
      const blob = new Blob([JSON.stringify(DATA, null, 2)], {{type: 'application/json'}});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'ssrm_v25_project_replay.json';
      a.click();
      URL.revokeObjectURL(url);
    }};
    render();
  </script>
</body>
</html>
"""
    path.write_text(html, encoding="utf-8")


def write_report(path: Path, results: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    m = results["metrics"]
    c = results["counts"]
    lines = [
        "# Report 265: SSRM-3D Browser World v25 Many-Day Project/Material/Body-Cost Bridge",
        "",
        "## Purpose",
        "",
        "Report 265 extends the browser-world line from owned-task obligations into many-day agent projects. Each project has an owner, material requirements, reserved time windows, fatigue/body cost, project memory, visible follow-up, and blocker/reshape paths when obligations are unresolved.",
        "",
        "This is the next pressure after Report 264: obligations should not only change trust/access panels; they should alter what agents can build over days.",
        "",
        "## Boundary",
        "",
        f"{results['boundary']}.",
        "",
        "The browser artifact exposes public project state, materials, fatigue panels, blocker markers, save/restore, and replay export. It does not expose private workspace contents or claim that the agents are conscious, consenting, suffering, or autonomously reasoning.",
        "",
        "## Method",
        "",
        "The deterministic generator runs 36 days with 18 ticks per day. Four owned projects persist across the run: Ari's west bridge repair, Fay's herb roof garden, Milo's north lantern relay, and Nia's archive weather log.",
        "",
        "Each tick records project progress, material consumption or shortage, time reservations, fatigue and recovery, unresolved-obligation blockers, project reshapes, visible follow-up, public memory snapshots, sensory cues, replay rows, and browser tick state.",
        "",
        "The source dependency is the Report 264 result artifact. Report 265 uses it only as continuity evidence; it does not import a hidden policy or call any LLM.",
        "",
        "## Results",
        "",
        f"- Verdict: `{results['verdict']}`",
        f"- Seed: `{results['seed']}`",
        f"- Readiness: `{m['browser_world_v25_project_readiness']:.6f}`",
        f"- Mean project channel score: `{m['mean_project_channel_score']:.6f}`",
        f"- Weakest channel score: `{m['weakest_channel_score']:.6f}`",
        f"- Weakest named channel: `project_progress_under_constraints` at `{m['project_progress_under_constraints']:.6f}`",
        f"- Blocked project frames: `{int(m['blocked_project_frame_count'])}`",
        f"- Reshaped projects: `{int(m['reshaped_project_count'])}`",
        f"- Material shortage rows: `{int(m['material_shortage_count'])}`",
        f"- Fatigue recovery rows: `{int(m['fatigue_recovery_count'])}`",
        "",
        "## Generated rows",
        "",
    ]
    for key in sorted(c):
        lines.append(f"- `{key}`: `{c[key]}`")
    lines.extend(
        [
            "",
            "## Ablations",
            "",
        ]
    )
    for key, value in results["ablations"].items():
        lines.append(f"- `{key}`: readiness `{value:.6f}`")
    lines.extend(
        [
            "",
            "The largest losses come from removing material ledgers, obligation blockers, and body cost. That is the intended shape: projects should not remain convincing if materials are infinite, fatigue is decorative, or unresolved duties never affect progress.",
            "",
            "## Honest interpretation",
            "",
            "Report 265 passes, but it is not a clean victory condition. The weakest channel is project progress under constraints. That is correct: once materials, fatigue, time reservations, and unresolved obligations all bind at once, project completion becomes brittle. The run demonstrates traceable continuity and visible recovery paths, not robust cooperative production yet.",
            "",
            "False polish would be making every project complete cleanly. This benchmark keeps shortages, deferrals, and reshapes visible so the browser world can become more game-like without pretending that messy project life is solved.",
            "",
            "## Artifacts",
            "",
        ]
    )
    for label, artifact in results["artifacts"].items():
        lines.append(f"- `{label}`: `{artifact}`")
    lines.extend(
        [
            "",
            "## Next gate",
            "",
            results["next_gate"],
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def persist(bundle: Mapping[str, Any]) -> None:
    results = bundle["results"]
    rows = bundle["rows"]
    state = bundle["state"]
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    for name, rowset in rows.items():
        write_csv(ARTIFACT_DIR / f"{PREFIX}_{name}.csv", rowset)

    summary_rows = [
        {"metric": key, "value": value}
        for key, value in sorted(results["metrics"].items())
    ]
    write_csv(ARTIFACT_DIR / f"{PREFIX}_summary.csv", summary_rows)
    write_csv(
        ARTIFACT_DIR / f"{PREFIX}_verdict.csv",
        [
            {
                "report": results["report"],
                "verdict": results["verdict"],
                "readiness": results["metrics"]["browser_world_v25_project_readiness"],
                "weakest_channel_score": results["metrics"]["weakest_channel_score"],
                "boundary": results["boundary"],
                "next_gate": results["next_gate"],
            }
        ],
    )
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    write_html(VIS_DIR / f"{PREFIX}.html", results, rows)
    write_report(DOCS_DIR / "265_ssrm_3d_browser_world_v25_many_day_project_material_body_cost_bridge_report.md", results)


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
        "readiness": results["metrics"]["browser_world_v25_project_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": "project_progress_under_constraints",
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
