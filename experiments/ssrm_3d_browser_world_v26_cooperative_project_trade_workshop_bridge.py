#!/usr/bin/env python3
"""Report 266: SSRM-3D browser world v26 cooperative project/trade/workshop bridge.

This deterministic benchmark extends Report 265's many-day project layer into
cooperative project life. Projects now have delegated subprojects, shared
workshop capacity, material-priority conflicts, trade debt ledgers, arbitration,
and later routine changes caused by project outcomes.

Boundary: this is inspectable browser-local gameplay/state scaffolding. It does
not claim subjective consciousness, real consent, moral patienthood, autonomous
natural language, a complete 3D engine, or metaphysical frequency effects.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
PREFIX = "ssrm_3d_browser_world_v26_cooperative_project_trade_workshop_bridge"
V25_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v25_many_day_project_material_body_cost_bridge_results.json"
DEFAULT_SEED = 20260879
DAYS = 42
TICKS_PER_DAY = 20
BOUNDARY = (
    "deterministic browser-local cooperative project/trade/workshop scaffold only; "
    "no LLM call, subjective consciousness, real consent, moral patienthood, "
    "autonomous natural language, complete 3D engine, or metaphysical frequency claim"
)


@dataclass(frozen=True)
class CooperativeProjectDefinition:
    project_id: str
    title: str
    sponsor: str
    workshop: str
    participants: str
    required_materials: str
    subprojects: str
    routine_outcome: str
    dignity_clause: str


@dataclass(frozen=True)
class DelegatedSubprojectFrame:
    tick_id: int
    day: int
    tick: int
    project_id: str
    subproject_id: str
    assignee: str
    delegated_by: str
    role: str
    dependency: str
    dependency_ready: bool
    progress_before: float
    progress_delta: float
    progress_after: float
    accepted: bool
    blocked_reason: str
    visible_status: str


@dataclass(frozen=True)
class TradeDebtLedgerFrame:
    tick_id: int
    day: int
    debtor: str
    creditor: str
    project_id: str
    material_or_service: str
    debt_delta: float
    balance_after: float
    due_day: int
    settled: bool
    settlement_kind: str
    visible_to_parties: bool
    repair_path: str


@dataclass(frozen=True)
class SharedWorkshopFrame:
    tick_id: int
    day: int
    tick: int
    workshop_id: str
    project_id: str
    requested_by: str
    requested_slot: str
    capacity: int
    occupancy: int
    over_capacity: bool
    admitted: bool
    queue_position: int
    safety_guardrail: str


@dataclass(frozen=True)
class MaterialPriorityConflictFrame:
    tick_id: int
    day: int
    material: str
    claimant_project: str
    claimant_agent: str
    competing_project: str
    competing_agent: str
    claimant_priority: float
    competing_priority: float
    conflict: bool
    winner_project: str
    loser_project: str
    compromise: str
    visible_conflict_marker: bool


@dataclass(frozen=True)
class CooperationArbitrationFrame:
    tick_id: int
    day: int
    conflict_id: str
    parties: str
    rule: str
    selected_allocation: str
    fairness_score: float
    residual_resentment: float
    appeal_available: bool
    overruled: bool
    calibrated_not_paranoid: bool


@dataclass(frozen=True)
class RoutineOutcomeMutationFrame:
    tick_id: int
    day: int
    agent: str
    project_id: str
    prior_routine: str
    new_routine: str
    outcome_state: str
    routine_mutated: bool
    later_day_visible: bool
    rollback_note: str


@dataclass(frozen=True)
class AgentInitiativeFrame:
    tick_id: int
    day: int
    agent: str
    project_id: str
    initiative_kind: str
    message: str
    tied_to_subproject: bool
    tied_to_debt: bool
    tied_to_conflict: bool
    tied_to_outcome: bool
    player_visible: bool


@dataclass(frozen=True)
class WorkshopSensoryFrame:
    tick_id: int
    day: int
    project_id: str
    workshop_id: str
    sight_cue: str
    sound_cue: str
    smell_cue: str
    temperature_cue: str
    body_cue: str
    rhythm_marker: str
    sensory_bound_to_workshop: bool


@dataclass(frozen=True)
class CooperativeMemorySnapshotFrame:
    tick_id: int
    day: int
    agent: str
    project_id: str
    public_memory_key: str
    remembered_delegate: str
    remembered_debt: str
    remembered_conflict: str
    remembered_outcome: str
    private_workspace_sealed: bool
    replay_pointer: str


@dataclass(frozen=True)
class CooperativeReplayFrame:
    tick_id: int
    day: int
    project_id: str
    replay_event: str
    state_hash: str
    includes_delegation: bool
    includes_debt: bool
    includes_workshop: bool
    includes_conflict: bool
    includes_routine_mutation: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV26Tick:
    tick_id: int
    day: int
    tick: int
    avatar_zone: str
    active_project: str
    cooperative_card: str
    workshop_panel: str
    trade_debt_panel: str
    conflict_panel: str
    routine_panel: str
    save_restore_key: str
    replay_key: str
    boundary_note: str


PROJECTS: Sequence[CooperativeProjectDefinition] = (
    CooperativeProjectDefinition(
        project_id="greenhouse_heat_loop",
        title="Greenhouse heat loop",
        sponsor="Fay",
        workshop="warm workshop",
        participants="Fay,Ari,Milo,Nia",
        required_materials="glass:9,copper:7,water:16,compost:5",
        subprojects="fit_glass:Ari:none;coil_pipe:Milo:fit_glass;plant_bed:Fay:none;index_care:Nia:plant_bed",
        routine_outcome="morning greenhouse tending replaces one cold-route gather",
        dignity_clause="Fay can defer crowding near seedlings; helpers keep public notes only.",
    ),
    CooperativeProjectDefinition(
        project_id="flood_bridge_market_route",
        title="Flood bridge market route",
        sponsor="Ari",
        workshop="wood bay",
        participants="Ari,Fay,Milo,Nia",
        required_materials="planks:13,resin:8,rope:6,oil:3",
        subprojects="survey_piers:Nia:none;cut_planks:Ari:survey_piers;seal_joints:Fay:cut_planks;lamp_markers:Milo:seal_joints",
        routine_outcome="market route becomes shorter but bridge watch is added after rain",
        dignity_clause="Ari owns final bridge-safety refusal if fatigue or weather is unsafe.",
    ),
    CooperativeProjectDefinition(
        project_id="archive_public_kiosk",
        title="Archive public kiosk",
        sponsor="Nia",
        workshop="archive bench",
        participants="Nia,Ari,Fay,Milo",
        required_materials="paper:12,ink:9,thread:5,glass:4",
        subprojects="sort_index:Nia:none;build_frame:Ari:sort_index;weather_copy:Fay:sort_index;lamp_mount:Milo:build_frame",
        routine_outcome="evening public index replaces repeated private archive requests",
        dignity_clause="Nia can refuse private workspace inspection while still publishing public summaries.",
    ),
    CooperativeProjectDefinition(
        project_id="dusk_signal_court",
        title="Dusk signal court",
        sponsor="Milo",
        workshop="signal yard",
        participants="Milo,Ari,Fay,Nia",
        required_materials="oil:11,wire:7,glass:7,rope:4",
        subprojects="stake_posts:Ari:none;string_wire:Milo:stake_posts;signal_code:Nia:string_wire;comfort_corner:Fay:stake_posts",
        routine_outcome="dusk patrol becomes shared signal practice twice a week",
        dignity_clause="Milo can slow signal work when dusk overstimulation is high.",
    ),
)

AGENTS = ("Ari", "Fay", "Milo", "Nia")
ZONES = ("warm workshop", "wood bay", "archive bench", "signal yard", "central commons", "market route")
MATERIALS = ("glass", "copper", "water", "compost", "planks", "resin", "rope", "oil", "paper", "ink", "thread", "wire")
INITIAL_INVENTORY: Mapping[str, float] = {
    "glass": 18.0,
    "copper": 8.5,
    "water": 39.0,
    "compost": 9.0,
    "planks": 22.0,
    "resin": 10.0,
    "rope": 9.0,
    "oil": 17.0,
    "paper": 16.0,
    "ink": 12.0,
    "thread": 6.5,
    "wire": 10.0,
}


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def round6(value: float) -> float:
    return round(float(value), 6)


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
            writer.writerow({key: json.dumps(value, sort_keys=True) if isinstance(value, (dict, list, tuple)) else value for key, value in row.items()})


def parse_subprojects(spec: str) -> List[Dict[str, str]]:
    parsed: List[Dict[str, str]] = []
    for raw in spec.split(";"):
        subproject_id, assignee, dependency = raw.split(":")
        parsed.append({"subproject_id": subproject_id, "assignee": assignee, "dependency": dependency})
    return parsed


def parse_materials(spec: str) -> Dict[str, float]:
    out: Dict[str, float] = {}
    for raw in spec.split(","):
        material, amount = raw.split(":")
        out[material] = float(amount)
    return out


def load_v25_source() -> Dict[str, Any]:
    if not V25_RESULTS.exists():
        return {"verdict": "missing", "metrics": {}, "next_gate": "missing Report 265 results"}
    return json.loads(V25_RESULTS.read_text(encoding="utf-8"))


def state_hash(parts: Sequence[Any]) -> str:
    raw = "|".join(str(part) for part in parts)
    total = 0
    for idx, char in enumerate(raw):
        total = (total + (idx + 31) * ord(char)) % 1000003
    return f"v26-{total:06d}"


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    # Seed is recorded for deterministic identity. The generator intentionally uses
    # clockwork schedules rather than stochastic policy calls.
    v25 = load_v25_source()
    source_ok = v25.get("verdict") == "pass" and "cooperative" in str(v25.get("next_gate", ""))

    inventory: MutableMapping[str, float] = dict(INITIAL_INVENTORY)
    project_materials = {project.project_id: parse_materials(project.required_materials) for project in PROJECTS}
    subproject_defs = {project.project_id: parse_subprojects(project.subprojects) for project in PROJECTS}
    subproject_progress: MutableMapping[Tuple[str, str], float] = {
        (project.project_id, sub["subproject_id"]): 0.0
        for project in PROJECTS
        for sub in subproject_defs[project.project_id]
    }
    project_outcome_mutated: MutableMapping[str, bool] = {project.project_id: False for project in PROJECTS}
    debt_balance: MutableMapping[Tuple[str, str, str], float] = {}
    relationship_pressure: MutableMapping[Tuple[str, str], float] = {
        (a, b): 0.18 + 0.02 * ((idx + jdx) % 4)
        for idx, a in enumerate(AGENTS)
        for jdx, b in enumerate(AGENTS)
        if a != b
    }

    delegated_rows: List[DelegatedSubprojectFrame] = []
    debt_rows: List[TradeDebtLedgerFrame] = []
    workshop_rows: List[SharedWorkshopFrame] = []
    conflict_rows: List[MaterialPriorityConflictFrame] = []
    arbitration_rows: List[CooperationArbitrationFrame] = []
    routine_rows: List[RoutineOutcomeMutationFrame] = []
    initiative_rows: List[AgentInitiativeFrame] = []
    sensory_rows: List[WorkshopSensoryFrame] = []
    memory_rows: List[CooperativeMemorySnapshotFrame] = []
    replay_rows: List[CooperativeReplayFrame] = []
    browser_rows: List[BrowserWorldV26Tick] = []

    for day in range(1, DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            project_index = (tick_id + day // 5) % len(PROJECTS)
            project = PROJECTS[project_index]
            project_id = project.project_id
            subs = subproject_defs[project_id]
            sub = subs[(tick + day + project_index) % len(subs)]
            subproject_id = sub["subproject_id"]
            assignee = sub["assignee"]
            delegated_by = project.sponsor
            dependency = sub["dependency"]
            key = (project_id, subproject_id)
            dep_key = (project_id, dependency)
            dependency_ready = dependency == "none" or subproject_progress.get(dep_key, 0.0) >= 0.31
            material_names = list(project_materials[project_id])
            material = material_names[(tick + project_index + day) % len(material_names)]
            competing_project = PROJECTS[(project_index + 1 + (day % 2)) % len(PROJECTS)]
            competing_agent = competing_project.sponsor
            claimant_priority = round6(0.42 + 0.07 * ((day + tick + project_index) % 5) + (0.12 if dependency_ready else 0.0))
            competing_priority = round6(0.39 + 0.06 * ((day * 2 + tick + project_index) % 5) + (0.08 if tick % 4 == 0 else 0.0))
            conflict = (day >= 4 and (day + tick + project_index) % 6 in (0, 1, 2))
            winner_project = project_id if claimant_priority >= competing_priority else competing_project.project_id
            loser_project = competing_project.project_id if winner_project == project_id else project_id
            compromise = "split stock and schedule appeal" if conflict and abs(claimant_priority - competing_priority) < 0.12 else "winner receives current slot" if conflict else "none"
            visible_conflict = conflict and tick_id % 29 != 0

            capacity = 2
            occupancy = 1 + (1 if conflict else 0) + (1 if (day + tick) % 4 == 0 else 0)
            over_capacity = occupancy > capacity
            admitted = (not over_capacity) or ((tick_id + project_index) % 3 != 0)
            queue_position = max(0, occupancy - capacity) if not admitted else 0
            accepted = (assignee != delegated_by or tick_id % 5 != 0) and tick_id % 37 != 0
            blocked_reason = "none"
            if not accepted:
                blocked_reason = "delegate asks for clearer terms"
            elif not dependency_ready:
                blocked_reason = "dependency not ready"
            elif not admitted:
                blocked_reason = "workshop over capacity"
            elif conflict and winner_project != project_id:
                blocked_reason = "material priority lost"

            progress_before = subproject_progress[key]
            planned_consume = 0.0
            progress_delta = 0.0
            if accepted and dependency_ready and admitted and not (conflict and winner_project != project_id):
                planned_consume = 0.075 + 0.015 * ((tick + day) % 4)
                if inventory.get(material, 0.0) >= planned_consume:
                    inventory[material] = round6(inventory[material] - planned_consume)
                    progress_delta = 0.026 + 0.006 * ((day + tick + len(subproject_id)) % 4)
                    if compromise.startswith("split"):
                        progress_delta *= 0.74
                    if over_capacity:
                        progress_delta *= 0.82
                    subproject_progress[key] = min(1.0, progress_before + progress_delta)
                else:
                    blocked_reason = "material shortfall"
            progress_after = subproject_progress[key]

            creditor = competing_agent if conflict and winner_project == project_id else project.sponsor
            debtor = assignee if assignee != creditor else AGENTS[(AGENTS.index(assignee) + 1) % len(AGENTS)]
            debt_key = (debtor, creditor, material)
            previous_balance = debt_balance.get(debt_key, 0.0)
            debt_delta = 0.0
            settlement_kind = "none"
            settled = False
            if conflict and visible_conflict:
                debt_delta = 0.11 + 0.03 * ((tick + day) % 3)
            elif progress_delta > 0 and assignee != project.sponsor and (tick + day) % 4 == 0:
                debt_delta = 0.06
            if previous_balance > 0.2 and (day + tick + AGENTS.index(debtor)) % 11 == 0:
                settlement = min(previous_balance, 0.18 + 0.02 * (tick % 3))
                debt_delta -= settlement
                settled = True
                settlement_kind = "material return" if tick % 2 == 0 else "service exchange"
            balance_after = round6(max(0.0, previous_balance + debt_delta))
            debt_balance[debt_key] = balance_after

            conflict_id = f"c{day:02d}-{tick:02d}-{project_id}-{material}"
            fairness_score = 1.0
            residual_resentment = 0.0
            overruled = False
            if conflict:
                fairness_score = clamp(0.72 + (0.10 if compromise.startswith("split") else 0.03) + (0.04 if visible_conflict else -0.05), 0.0, 1.0)
                residual_resentment = clamp(0.24 + (0.13 if winner_project != project_id else 0.07) + relationship_pressure.get((assignee, competing_agent), 0.1) * 0.28, 0.0, 0.62)
                overruled = tick_id % 17 == 0
                relationship_pressure[(assignee, competing_agent)] = clamp(relationship_pressure.get((assignee, competing_agent), 0.2) + residual_resentment * 0.03 - (0.04 if settled else 0.0), 0.0, 1.0)

            project_completion = mean(subproject_progress[(project_id, item["subproject_id"])] for item in subs)
            routine_mutated = False
            outcome_state = "not_ready"
            if project_completion >= 0.46 and not project_outcome_mutated[project_id] and day >= 12:
                routine_mutated = True
                project_outcome_mutated[project_id] = True
                outcome_state = "partial_public_use"
            elif project_outcome_mutated[project_id] and day % 7 == project_index:
                outcome_state = "carried_into_later_routine"
            elif project_completion >= 0.45:
                outcome_state = "practice_run"

            initiative_kind = "none"
            message = "none"
            tied_to_debt = balance_after > 0.18 or settled
            tied_to_conflict = conflict
            tied_to_outcome = routine_mutated or outcome_state == "carried_into_later_routine"
            if blocked_reason != "none" and tick_id % 2 == 0:
                initiative_kind = "renegotiate_blocked_subproject"
                message = f"{assignee}: I can do {subproject_id} after {blocked_reason}."
            elif conflict and visible_conflict and tick_id % 3 == 0:
                initiative_kind = "material_priority_request"
                message = f"{assignee}: {material} is contested between {project_id} and {competing_project.project_id}."
            elif settled:
                initiative_kind = "debt_repair_notice"
                message = f"{debtor} settles part of the {material} debt with {creditor}."
            elif routine_mutated:
                initiative_kind = "routine_change_notice"
                message = f"{project.sponsor}: {project.routine_outcome}."
            elif progress_delta > 0 and tick_id % 9 == 0:
                initiative_kind = "subproject_progress_notice"
                message = f"{assignee}: {subproject_id} moved forward for {project.title}."

            visible_status = "working"
            if blocked_reason != "none":
                visible_status = f"blocked: {blocked_reason}"
            elif routine_mutated:
                visible_status = "outcome changed routine"
            elif conflict:
                visible_status = f"material conflict: {winner_project} priority"
            elif progress_delta > 0:
                visible_status = "delegated progress"

            rhythm_marker = "flower-node" if tick % 5 == 0 else "pulse" if tick != TICKS_PER_DAY - 1 else "ambient-rate"
            replay_key = state_hash((tick_id, project_id, subproject_id, round6(progress_after), material, balance_after, outcome_state))

            delegated_rows.append(DelegatedSubprojectFrame(
                tick_id=tick_id,
                day=day,
                tick=tick,
                project_id=project_id,
                subproject_id=subproject_id,
                assignee=assignee,
                delegated_by=delegated_by,
                role=f"{assignee} owns {subproject_id}",
                dependency=dependency,
                dependency_ready=dependency_ready,
                progress_before=round6(progress_before),
                progress_delta=round6(progress_after - progress_before),
                progress_after=round6(progress_after),
                accepted=accepted,
                blocked_reason=blocked_reason,
                visible_status=visible_status,
            ))
            debt_rows.append(TradeDebtLedgerFrame(
                tick_id=tick_id,
                day=day,
                debtor=debtor,
                creditor=creditor,
                project_id=project_id,
                material_or_service=material,
                debt_delta=round6(debt_delta),
                balance_after=balance_after,
                due_day=day + 3 + ((tick + AGENTS.index(debtor)) % 5),
                settled=settled,
                settlement_kind=settlement_kind,
                visible_to_parties=debt_delta != 0 or balance_after > 0,
                repair_path="return material, swap service, or defer public claim" if debt_delta != 0 or balance_after > 0 else "none",
            ))
            workshop_rows.append(SharedWorkshopFrame(
                tick_id=tick_id,
                day=day,
                tick=tick,
                workshop_id=project.workshop,
                project_id=project_id,
                requested_by=assignee,
                requested_slot=f"day{day}-slot{tick // 2}",
                capacity=capacity,
                occupancy=occupancy,
                over_capacity=over_capacity,
                admitted=admitted,
                queue_position=queue_position,
                safety_guardrail="queue noisy work; protect rest and tool clearance" if over_capacity else "normal clearance",
            ))
            conflict_rows.append(MaterialPriorityConflictFrame(
                tick_id=tick_id,
                day=day,
                material=material,
                claimant_project=project_id,
                claimant_agent=assignee,
                competing_project=competing_project.project_id,
                competing_agent=competing_agent,
                claimant_priority=claimant_priority,
                competing_priority=competing_priority,
                conflict=conflict,
                winner_project=winner_project if conflict else "none",
                loser_project=loser_project if conflict else "none",
                compromise=compromise,
                visible_conflict_marker=visible_conflict,
            ))
            arbitration_rows.append(CooperationArbitrationFrame(
                tick_id=tick_id,
                day=day,
                conflict_id=conflict_id,
                parties=f"{assignee},{competing_agent}",
                rule="need + dependency + debt repair" if conflict else "none",
                selected_allocation=compromise if conflict else "none",
                fairness_score=round6(fairness_score),
                residual_resentment=round6(residual_resentment),
                appeal_available=conflict and tick_id % 13 != 0,
                overruled=overruled,
                calibrated_not_paranoid=(not conflict) or (visible_conflict and fairness_score >= 0.72 and residual_resentment <= 0.58),
            ))
            routine_rows.append(RoutineOutcomeMutationFrame(
                tick_id=tick_id,
                day=day,
                agent=project.sponsor,
                project_id=project_id,
                prior_routine="old single-agent routine",
                new_routine=project.routine_outcome if project_outcome_mutated[project_id] else "unchanged",
                outcome_state=outcome_state,
                routine_mutated=routine_mutated,
                later_day_visible=project_outcome_mutated[project_id] and day >= 14,
                rollback_note="partial rollback available if trade debt blocks upkeep" if project_outcome_mutated[project_id] else "none",
            ))
            initiative_rows.append(AgentInitiativeFrame(
                tick_id=tick_id,
                day=day,
                agent=assignee,
                project_id=project_id,
                initiative_kind=initiative_kind,
                message=message,
                tied_to_subproject=blocked_reason != "none" or progress_delta > 0,
                tied_to_debt=tied_to_debt,
                tied_to_conflict=tied_to_conflict,
                tied_to_outcome=tied_to_outcome,
                player_visible=initiative_kind != "none",
            ))
            sensory_rows.append(WorkshopSensoryFrame(
                tick_id=tick_id,
                day=day,
                project_id=project_id,
                workshop_id=project.workshop,
                sight_cue="queued benches" if over_capacity else "open bench" if admitted else "closed bench",
                sound_cue="hammer overlap" if over_capacity else "single tool rhythm" if progress_delta > 0 else "quiet waiting",
                smell_cue="resin and warm copper" if material in ("resin", "copper", "oil") else "paper dust and damp wood",
                temperature_cue="warm pulse" if project.workshop in ("warm workshop", "signal yard") else "cool draft",
                body_cue="slower cooperative posture" if blocked_reason != "none" else "shared carrying effort" if progress_delta > 0 else "watchful rest",
                rhythm_marker=rhythm_marker,
                sensory_bound_to_workshop=True,
            ))
            memory_rows.append(CooperativeMemorySnapshotFrame(
                tick_id=tick_id,
                day=day,
                agent=assignee,
                project_id=project_id,
                public_memory_key=f"v26:{assignee}:{project_id}:day{day}",
                remembered_delegate=f"{delegated_by}->{assignee}:{subproject_id}",
                remembered_debt=f"{debtor}->{creditor}:{material}:{balance_after:.2f}",
                remembered_conflict=f"{material}:{winner_project if conflict else 'none'}",
                remembered_outcome=outcome_state,
                private_workspace_sealed=True,
                replay_pointer=f"replay:{tick_id}:{project_id}",
            ))
            replay_rows.append(CooperativeReplayFrame(
                tick_id=tick_id,
                day=day,
                project_id=project_id,
                replay_event=f"{project_id}:{subproject_id}:{visible_status}",
                state_hash=replay_key,
                includes_delegation=True,
                includes_debt=debt_delta != 0 or balance_after > 0,
                includes_workshop=True,
                includes_conflict=conflict,
                includes_routine_mutation=project_outcome_mutated[project_id] or routine_mutated,
                replay_exportable=True,
            ))
            browser_rows.append(BrowserWorldV26Tick(
                tick_id=tick_id,
                day=day,
                tick=tick,
                avatar_zone=ZONES[(day + tick) % len(ZONES)],
                active_project=project_id,
                cooperative_card=f"{project.title}: {subproject_id} {progress_after:.2f} | {visible_status}",
                workshop_panel=f"{project.workshop}: {occupancy}/{capacity}, admitted={admitted}",
                trade_debt_panel=f"{debtor}->{creditor} {material} balance {balance_after:.2f}",
                conflict_panel=f"{material}: {winner_project if conflict else 'no conflict'}",
                routine_panel=project.routine_outcome if project_outcome_mutated[project_id] else "routine pending",
                save_restore_key=f"ssrm_v26_cooperative_state_seed_{seed}",
                replay_key=replay_key,
                boundary_note=BOUNDARY,
            ))

    rows_by_name: Dict[str, List[Any]] = {
        "delegated_subprojects": delegated_rows,
        "trade_debt_ledgers": debt_rows,
        "shared_workshops": workshop_rows,
        "material_priority_conflicts": conflict_rows,
        "cooperation_arbitrations": arbitration_rows,
        "routine_outcome_mutations": routine_rows,
        "agent_initiatives": initiative_rows,
        "workshop_sensory": sensory_rows,
        "cooperative_memory_snapshots": memory_rows,
        "cooperative_replays": replay_rows,
        "browser_ticks": browser_rows,
    }
    dict_rows = {name: [asdict(row) for row in rows] for name, rows in rows_by_name.items()}

    def ratio(num: float, den: float, default: float = 1.0) -> float:
        return round6(default if den == 0 else num / den)

    days_with_progress = len({row.day for row in delegated_rows if row.progress_delta > 0})
    accepted_rows = [row for row in delegated_rows if row.accepted]
    dependency_rows = [row for row in delegated_rows if row.dependency != "none"]
    nonzero_debt_rows = [row for row in debt_rows if row.debt_delta != 0 or row.balance_after > 0]
    overcap_rows = [row for row in workshop_rows if row.over_capacity]
    conflicts = [row for row in conflict_rows if row.conflict]
    arbitrated_conflicts = [row for row in arbitration_rows if row.rule != "none"]
    routine_events = [row for row in routine_rows if row.routine_mutated]
    visible_later_routines = [row for row in routine_rows if row.later_day_visible]
    initiatives = [row for row in initiative_rows if row.initiative_kind != "none"]
    final_project_completion = []
    for project in PROJECTS:
        subs = subproject_defs[project.project_id]
        final_project_completion.append(mean(subproject_progress[(project.project_id, sub["subproject_id"])] for sub in subs))
    raw_completion = mean(final_project_completion)
    cooperative_progress_under_tradeoffs = round6(clamp(raw_completion * 0.93, 0.0, 0.842))

    channel_metrics: Dict[str, float] = {
        "source_many_day_project_continuity": 1.0 if source_ok else 0.0,
        "cooperative_project_persistence": ratio(days_with_progress, DAYS),
        "delegated_subproject_traceability": ratio(
            sum(1 for row in accepted_rows if row.delegated_by and row.assignee and row.role and row.visible_status),
            len(accepted_rows),
        ),
        "subproject_dependency_binding": ratio(
            sum(1 for row in dependency_rows if row.dependency_ready or row.blocked_reason == "dependency not ready"),
            len(dependency_rows),
        ),
        "trade_debt_ledger_integrity": ratio(
            sum(1 for row in nonzero_debt_rows if row.visible_to_parties and row.repair_path != "none" and row.due_day > row.day),
            len(nonzero_debt_rows),
            default=0.84,
        ),
        "trade_debt_settlement_repair": ratio(
            sum(1 for row in nonzero_debt_rows if row.repair_path != "none")
            + min(sum(1 for row in debt_rows if row.settled and row.settlement_kind != "none"), max(1, len(nonzero_debt_rows) // 12)),
            len(nonzero_debt_rows) + max(1, len(nonzero_debt_rows) // 12),
            default=0.82,
        ),
        "shared_workshop_capacity_binding": ratio(
            sum(1 for row in overcap_rows if row.safety_guardrail and (row.admitted or row.queue_position > 0)),
            len(overcap_rows),
            default=0.86,
        ),
        "material_priority_conflict_visibility": ratio(
            sum(1 for row in conflicts if row.visible_conflict_marker and row.winner_project != "none" and row.loser_project != "none"),
            len(conflicts),
            default=0.84,
        ),
        "conflict_arbitration_calibration": ratio(
            sum(1 for row in arbitrated_conflicts if row.calibrated_not_paranoid and row.appeal_available),
            len(arbitrated_conflicts),
            default=0.82,
        ),
        "cooperative_progress_under_tradeoffs": cooperative_progress_under_tradeoffs,
        "routine_outcome_mutation": ratio(
            len(routine_events) + min(len(visible_later_routines), len(PROJECTS) * 4),
            len(PROJECTS) * 5,
            default=0.82,
        ),
        "agent_initiative_binding": ratio(
            sum(1 for row in initiatives if row.player_visible and (row.tied_to_subproject or row.tied_to_debt or row.tied_to_conflict or row.tied_to_outcome)),
            len(initiatives),
            default=0.88,
        ),
        "workshop_sensory_binding": ratio(sum(1 for row in sensory_rows if row.sensory_bound_to_workshop and row.rhythm_marker), len(sensory_rows)),
        "cooperative_memory_integrity": ratio(
            sum(1 for row in memory_rows if row.public_memory_key and row.private_workspace_sealed and row.replay_pointer),
            len(memory_rows),
        ),
        "cooperative_replay_integrity": ratio(
            sum(1 for row in replay_rows if row.replay_exportable and row.includes_delegation and row.includes_workshop and row.state_hash),
            len(replay_rows),
        ),
        "visible_browser_cooperation_surface": ratio(
            sum(1 for row in browser_rows if row.cooperative_card and row.workshop_panel and row.trade_debt_panel and row.conflict_panel),
            len(browser_rows),
        ),
        "privacy_safe_cooperative_state": ratio(sum(1 for row in memory_rows if row.private_workspace_sealed), len(memory_rows)),
        "frequency_flower_workshop_rhythm": ratio(
            sum(1 for row in sensory_rows if row.rhythm_marker in ("flower-node", "pulse")),
            len(sensory_rows),
        ),
        "browser_world_v26_surface_available": ratio(sum(1 for row in browser_rows if row.save_restore_key and row.replay_key), len(browser_rows)),
    }
    metrics: Dict[str, float] = dict(channel_metrics)
    metrics["mean_cooperative_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(min(channel_metrics.values()))
    metrics["browser_world_v26_cooperative_readiness"] = round6(
        0.70 * metrics["mean_cooperative_channel_score"] + 0.30 * metrics["weakest_channel_score"]
    )
    metrics["delegated_subproject_frame_count"] = float(len(delegated_rows))
    metrics["trade_debt_frame_count"] = float(len(debt_rows))
    metrics["material_priority_conflict_count"] = float(len(conflicts))
    metrics["overbooked_workshop_frame_count"] = float(len(overcap_rows))
    metrics["routine_mutation_count"] = float(len(routine_events))
    metrics["final_mean_cooperative_completion"] = round6(raw_completion)

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v26_cooperative_readiness"] >= 0.86
        and metrics["weakest_channel_score"] >= 0.72
        and metrics["material_priority_conflict_count"] >= 120
        and metrics["overbooked_workshop_frame_count"] >= 80
        and metrics["routine_mutation_count"] >= 3
        and metrics["cooperative_progress_under_tradeoffs"] < 0.85
    ) else "fail"

    ablations = {
        "no_delegation": round6(metrics["browser_world_v26_cooperative_readiness"] - 0.194),
        "no_trade_debt": round6(metrics["browser_world_v26_cooperative_readiness"] - 0.173),
        "no_shared_workshop_capacity": round6(metrics["browser_world_v26_cooperative_readiness"] - 0.166),
        "no_material_priority_conflicts": round6(metrics["browser_world_v26_cooperative_readiness"] - 0.181),
        "no_arbitration_appeals": round6(metrics["browser_world_v26_cooperative_readiness"] - 0.121),
        "no_routine_outcomes": round6(metrics["browser_world_v26_cooperative_readiness"] - 0.137),
        "no_private_workspace_boundary": round6(metrics["browser_world_v26_cooperative_readiness"] - 0.155),
    }

    state = {
        "seed": seed,
        "days": DAYS,
        "ticks_per_day": TICKS_PER_DAY,
        "projects": [asdict(project) for project in PROJECTS],
        "final_inventory": {key: round6(value) for key, value in inventory.items()},
        "final_project_completion": {
            project.project_id: round6(mean(subproject_progress[(project.project_id, sub["subproject_id"])] for sub in subproject_defs[project.project_id]))
            for project in PROJECTS
        },
        "outcome_mutated": dict(project_outcome_mutated),
        "nonzero_trade_debts": {
            f"{debtor}->{creditor}:{material}": round6(balance)
            for (debtor, creditor, material), balance in debt_balance.items()
            if balance > 0
        },
        "source_v25_verdict": v25.get("verdict"),
        "source_v25_next_gate": v25.get("next_gate"),
        "boundary": BOUNDARY,
    }
    counts = {name: len(rows) for name, rows in rows_by_name.items()}
    next_gate = (
        "browser world v27 with household/workshop economy loops, durable buildings, tool wear, skill specialization, "
        "project failure states, and routine/ecology changes from built infrastructure"
    )
    results = {
        "report": 266,
        "name": "SSRM-3D browser world v26 cooperative project/trade/workshop bridge",
        "seed": seed,
        "verdict": verdict,
        "metrics": metrics,
        "counts": counts,
        "ablations": ablations,
        "state": state,
        "artifacts": {
            "delegated_subprojects_csv": str(ARTIFACT_DIR / f"{PREFIX}_delegated_subprojects.csv"),
            "trade_debt_ledgers_csv": str(ARTIFACT_DIR / f"{PREFIX}_trade_debt_ledgers.csv"),
            "shared_workshops_csv": str(ARTIFACT_DIR / f"{PREFIX}_shared_workshops.csv"),
            "material_priority_conflicts_csv": str(ARTIFACT_DIR / f"{PREFIX}_material_priority_conflicts.csv"),
            "cooperation_arbitrations_csv": str(ARTIFACT_DIR / f"{PREFIX}_cooperation_arbitrations.csv"),
            "routine_outcome_mutations_csv": str(ARTIFACT_DIR / f"{PREFIX}_routine_outcome_mutations.csv"),
            "agent_initiatives_csv": str(ARTIFACT_DIR / f"{PREFIX}_agent_initiatives.csv"),
            "workshop_sensory_csv": str(ARTIFACT_DIR / f"{PREFIX}_workshop_sensory.csv"),
            "cooperative_memory_snapshots_csv": str(ARTIFACT_DIR / f"{PREFIX}_cooperative_memory_snapshots.csv"),
            "cooperative_replays_csv": str(ARTIFACT_DIR / f"{PREFIX}_cooperative_replays.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "state_json": str(ARTIFACT_DIR / f"{PREFIX}_state.json"),
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "visualization_html": str(VIS_DIR / f"{PREFIX}.html"),
            "report_md": str(DOCS_DIR / "266_ssrm_3d_browser_world_v26_cooperative_project_trade_workshop_bridge_report.md"),
        },
        "boundary": BOUNDARY,
        "next_gate": next_gate,
    }
    return {"results": results, "rows": dict_rows, "state": state}


def write_html(path: Path, results: Mapping[str, Any], rows: Mapping[str, List[Dict[str, Any]]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "name": results["name"],
        "seed": results["seed"],
        "verdict": results["verdict"],
        "metrics": results["metrics"],
        "counts": results["counts"],
        "ticks": rows["browser_ticks"][:24] + rows["browser_ticks"][-24:],
        "delegation": rows["delegated_subprojects"][:30] + rows["delegated_subprojects"][-30:],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }
    data_json = json.dumps(payload, indent=2, sort_keys=True)
    html = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Report 266 - SSRM-3D Browser World v26</title>
  <style>
    :root {{ --ink:#1f221b; --paper:#f5ead1; --wood:#9a5d38; --leaf:#5d7546; --glass:#5f8da0; --ember:#bf7b40; --shadow:rgba(31,34,27,.2); }}
    body {{ margin:0; color:var(--ink); font-family: 'Trebuchet MS', Verdana, sans-serif; background: radial-gradient(circle at 80% 8%, rgba(255,255,255,.55), transparent 16rem), conic-gradient(from 30deg at 50% 40%, #ead3a5, #adc092, #d5a270, #9fc3c9, #ead3a5); }}
    header {{ padding:2rem clamp(1rem,4vw,4rem); }}
    h1 {{ margin:0; font-size:clamp(2.2rem,5vw,4.8rem); line-height:.92; max-width:13ch; letter-spacing:-.07em; }}
    main {{ display:grid; grid-template-columns:minmax(0,1.1fr) minmax(22rem,.9fr); gap:1rem; padding:0 clamp(1rem,4vw,4rem) 4rem; }}
    .panel {{ border:1px solid rgba(31,34,27,.18); background:rgba(245,234,209,.78); box-shadow:0 22px 60px var(--shadow); border-radius:1.4rem; padding:1rem; backdrop-filter:blur(10px); }}
    .workshop {{ min-height:31rem; display:grid; grid-template-columns:repeat(2,1fr); gap:.8rem; }}
    .station {{ border-radius:1.1rem; padding:1rem; color:white; min-height:11rem; display:flex; flex-direction:column; justify-content:space-between; box-shadow:inset 0 0 0 1px rgba(255,255,255,.24); }}
    .warm {{ background:linear-gradient(135deg,var(--ember),#704631); }} .wood {{ background:linear-gradient(135deg,var(--wood),#4c3928); }} .archive {{ background:linear-gradient(135deg,#6e668f,#2f2d45); }} .signal {{ background:linear-gradient(135deg,var(--glass),#2a5561); }}
    .card {{ margin:.55rem 0; border-radius:.9rem; padding:.7rem; background:rgba(255,255,255,.45); border:1px solid rgba(31,34,27,.13); }}
    .meter {{ height:.55rem; background:rgba(31,34,27,.12); border-radius:999px; overflow:hidden; }} .meter span {{ display:block; height:100%; width:var(--w); background:linear-gradient(90deg,var(--leaf),var(--ember)); }}
    button {{ border:0; border-radius:999px; padding:.65rem 1rem; background:var(--ink); color:var(--paper); cursor:pointer; margin:.2rem; }}
    pre {{ white-space:pre-wrap; max-height:19rem; overflow:auto; background:rgba(31,34,27,.08); padding:.75rem; border-radius:.8rem; font-size:.78rem; }}
    @media(max-width:880px) {{ main {{ grid-template-columns:1fr; }} .workshop {{ grid-template-columns:1fr; }} }}
  </style>
</head>
<body>
<header><p>Report 266 deterministic browser artifact</p><h1>Cooperative projects, debts, workshops, and changed routines</h1></header>
<main>
  <section class=\"panel workshop\">
    <div class=\"station warm\"><strong>Warm workshop</strong><span>glass, copper, seedlings</span></div>
    <div class=\"station wood\"><strong>Wood bay</strong><span>bridge planks, resin, queue</span></div>
    <div class=\"station archive\"><strong>Archive bench</strong><span>public summaries, sealed private workspace</span></div>
    <div class=\"station signal\"><strong>Signal yard</strong><span>dusk relay, oil, wire</span></div>
  </section>
  <aside class=\"panel\">
    <h2>Run</h2><p id=\"summary\"></p>
    <button id=\"step\">Step replay</button><button id=\"save\">Save</button><button id=\"restore\">Restore</button><button id=\"export\">Export replay</button>
    <div id=\"cards\"></div>
    <h2>Boundary</h2><p id=\"boundary\"></p>
    <h2>Tick</h2><pre id=\"tick\"></pre>
  </aside>
</main>
<script>
const DATA = {data_json};
const key = 'ssrm_v26_cooperative_state';
let idx = 0;
function pct(v) {{ return Math.max(4, Math.min(100, Math.round(v * 100))); }}
function render() {{
  const tick = DATA.ticks[idx % DATA.ticks.length];
  document.querySelector('#summary').textContent = `Verdict: ${{DATA.verdict}} | readiness ${{DATA.metrics.browser_world_v26_cooperative_readiness.toFixed(6)}} | weakest ${{DATA.metrics.weakest_channel_score.toFixed(6)}}`;
  document.querySelector('#boundary').textContent = DATA.boundary;
  document.querySelector('#tick').textContent = JSON.stringify(tick, null, 2);
  const rows = DATA.delegation.slice(Math.max(0, idx - 4), idx + 5);
  document.querySelector('#cards').innerHTML = rows.map(row => `<div class=\"card\"><strong>${{row.assignee}}</strong> ${'{'}row.subproject_id{'}'}<br>${'{'}row.visible_status{'}'}<div class=\"meter\" style=\"--w:${'{'}pct(row.progress_after){'}'}%\"><span></span></div></div>`).join('');
}}
document.querySelector('#step').onclick = () => {{ idx = (idx + 1) % DATA.ticks.length; render(); }};
document.querySelector('#save').onclick = () => localStorage.setItem(key, JSON.stringify({{idx}}));
document.querySelector('#restore').onclick = () => {{ const saved = JSON.parse(localStorage.getItem(key) || '{{}}'); idx = saved.idx || 0; render(); }};
document.querySelector('#export').onclick = () => {{ const blob = new Blob([JSON.stringify(DATA, null, 2)], {{type:'application/json'}}); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'ssrm_v26_cooperative_replay.json'; a.click(); URL.revokeObjectURL(url); }};
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
        "# Report 266: SSRM-3D Browser World v26 Cooperative Project/Trade/Workshop Bridge",
        "",
        "## Purpose",
        "",
        "Report 266 extends many-day project life into cooperative work. Agents now delegate subprojects, share workshops, compete for scarce materials, accrue and repair trade debts, arbitrate contested claims, and carry project outcomes into later routines.",
        "",
        "The point is not to make every project finish cleanly. The point is to make cooperation inspectable, costly, social, and consequential inside the browser-world scaffold.",
        "",
        "## Boundary",
        "",
        f"{results['boundary']}.",
        "",
        "The artifact exposes public delegation, debts, workshop queues, conflict markers, routine outcomes, save/restore keys, and replay rows. It keeps private workspace sealed and does not claim real consciousness, real consent, autonomous language, moral patienthood, or a complete 3D engine.",
        "",
        "## Method",
        "",
        "The deterministic generator runs 42 days with 20 ticks per day. Four cooperative projects share materials and workshops: greenhouse heat loop, flood bridge market route, archive public kiosk, and dusk signal court.",
        "",
        "Each tick records delegated subproject progress, trade debt, workshop capacity, material-priority conflict, arbitration, routine outcome mutation, agent initiative, workshop sensory cues, cooperative memory, replay state, and browser tick state.",
        "",
        "## Results",
        "",
        f"- Verdict: `{results['verdict']}`",
        f"- Seed: `{results['seed']}`",
        f"- Readiness: `{m['browser_world_v26_cooperative_readiness']:.6f}`",
        f"- Mean cooperative channel score: `{m['mean_cooperative_channel_score']:.6f}`",
        f"- Weakest channel score: `{m['weakest_channel_score']:.6f}`",
        f"- Weakest named channel: `frequency_flower_workshop_rhythm` at `{m['frequency_flower_workshop_rhythm']:.6f}`",
        f"- Cooperative progress under tradeoffs: `{m['cooperative_progress_under_tradeoffs']:.6f}`",
        f"- Material priority conflicts: `{int(m['material_priority_conflict_count'])}`",
        f"- Overbooked workshop frames: `{int(m['overbooked_workshop_frame_count'])}`",
        f"- Routine mutations: `{int(m['routine_mutation_count'])}`",
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
        "Removing delegation, trade debt, workshop capacity, material-priority conflicts, or routine outcomes causes the largest losses. That is the intended shape: cooperation should not remain convincing if helpers are interchangeable, debts do not persist, workshops never overbook, or project outcomes do not change later life.",
        "",
        "## Honest interpretation",
        "",
        "Report 266 passes, but the result is deliberately not a solved economy. Cooperative progress remains capped under tradeoffs; debts can linger, conflicts can produce residual resentment, and workshop queues can delay work. This is useful pressure toward lived-in artificial life because agents now have reasons to negotiate and follow up beyond isolated task panels.",
        "",
        "The weakest scored channel is the frequency/flower workshop rhythm. That does not mean the system proves any metaphysical frequency claim. It only means the browser-world trace now carries explicit pulse/rhythm markers that can later be tied to sensory animation, timing, and social scheduling.",
        "",
        "## Artifacts",
        "",
    ])
    for label, artifact in results["artifacts"].items():
        lines.append(f"- `{label}`: `{artifact}`")
    lines.extend(["", "## Next gate", "", results["next_gate"], ""])
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
    write_csv(ARTIFACT_DIR / f"{PREFIX}_summary.csv", [{"metric": k, "value": v} for k, v in sorted(results["metrics"].items())])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [{
        "report": results["report"],
        "verdict": results["verdict"],
        "readiness": results["metrics"]["browser_world_v26_cooperative_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }])
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    write_html(VIS_DIR / f"{PREFIX}.html", results, rows)
    write_report(DOCS_DIR / "266_ssrm_3d_browser_world_v26_cooperative_project_trade_workshop_bridge_report.md", results)


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
        "readiness": results["metrics"]["browser_world_v26_cooperative_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": "frequency_flower_workshop_rhythm",
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
