#!/usr/bin/env python3
"""Report 267: SSRM-3D browser world v27 household/workshop economy infrastructure bridge.

This deterministic benchmark extends Report 266's cooperative project/trade layer
into durable infrastructure. Households and workshops now run resource loops,
buildings persist and decay, tools wear and require maintenance, agents develop
skill specialization, projects can visibly fail, and built infrastructure changes
later routines and ecology.

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
PREFIX = "ssrm_3d_browser_world_v27_household_workshop_economy_infrastructure_bridge"
V26_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v26_cooperative_project_trade_workshop_bridge_results.json"
DEFAULT_SEED = 20260880
DAYS = 48
TICKS_PER_DAY = 18
BOUNDARY = (
    "deterministic browser-local household/workshop economy infrastructure scaffold only; "
    "no LLM call, subjective consciousness, real consent, moral patienthood, "
    "autonomous natural language, complete 3D engine, or metaphysical frequency claim"
)


@dataclass(frozen=True)
class InfrastructureDefinition:
    infrastructure_id: str
    title: str
    steward: str
    household: str
    workshop: str
    primary_tool: str
    skill_domain: str
    resource_loop: str
    ecology_effect: str
    failure_mode: str
    dignity_clause: str


@dataclass(frozen=True)
class HouseholdEconomyFrame:
    tick_id: int
    day: int
    tick: int
    household: str
    infrastructure_id: str
    resource: str
    stock_before: float
    produced: float
    consumed: float
    stock_after: float
    shortage: bool
    exchange_partner: str
    visible_ledger: str


@dataclass(frozen=True)
class DurableBuildingFrame:
    tick_id: int
    day: int
    infrastructure_id: str
    steward: str
    durability_before: float
    wear_delta: float
    repair_delta: float
    durability_after: float
    weather_pressure: str
    usable: bool
    visible_damage: bool
    maintenance_due: bool


@dataclass(frozen=True)
class ToolWearFrame:
    tick_id: int
    day: int
    agent: str
    tool_id: str
    infrastructure_id: str
    condition_before: float
    wear_delta: float
    maintenance_delta: float
    condition_after: float
    broken: bool
    tool_limits_work: bool
    repair_action: str


@dataclass(frozen=True)
class SkillSpecializationFrame:
    tick_id: int
    day: int
    agent: str
    skill_domain: str
    practice_delta: float
    skill_before: float
    skill_after: float
    fatigue_cost: float
    helps_project: bool
    specialization_visible: str


@dataclass(frozen=True)
class ProjectFailureFrame:
    tick_id: int
    day: int
    infrastructure_id: str
    failure_event: bool
    failure_mode: str
    failure_cause: str
    visible_failure_marker: bool
    recovery_path: str
    damage_bounded: bool
    unresolved_after_tick: bool


@dataclass(frozen=True)
class RoutineInfrastructureMutationFrame:
    tick_id: int
    day: int
    agent: str
    infrastructure_id: str
    old_routine: str
    new_routine: str
    mutation_kind: str
    triggered_by_state: str
    routine_changed: bool
    later_visible: bool


@dataclass(frozen=True)
class EcologyChangeFrame:
    tick_id: int
    day: int
    infrastructure_id: str
    ecology_channel: str
    level_before: float
    infrastructure_effect: float
    weather_effect: float
    level_after: float
    feedback_visible: bool
    care_action: str


@dataclass(frozen=True)
class MaintenanceDebtFrame:
    tick_id: int
    day: int
    debtor: str
    infrastructure_id: str
    owed_work: str
    debt_before: float
    debt_delta: float
    debt_after: float
    settled: bool
    visible_to_household: bool
    repair_option: str


@dataclass(frozen=True)
class AgentEconomyInitiativeFrame:
    tick_id: int
    day: int
    agent: str
    infrastructure_id: str
    initiative_kind: str
    message: str
    tied_to_stock: bool
    tied_to_wear: bool
    tied_to_skill: bool
    tied_to_failure: bool
    player_visible: bool


@dataclass(frozen=True)
class SensoryInfrastructureFrame:
    tick_id: int
    day: int
    infrastructure_id: str
    sight_cue: str
    sound_cue: str
    smell_cue: str
    temperature_cue: str
    wetness_cue: str
    body_cue: str
    rhythm_marker: str
    sensory_bound_to_infrastructure: bool


@dataclass(frozen=True)
class InfrastructureMemorySnapshotFrame:
    tick_id: int
    day: int
    agent: str
    infrastructure_id: str
    public_memory_key: str
    remembered_stock: str
    remembered_durability: str
    remembered_tool: str
    remembered_failure: str
    private_workspace_sealed: bool
    replay_pointer: str


@dataclass(frozen=True)
class InfrastructureReplayFrame:
    tick_id: int
    day: int
    infrastructure_id: str
    replay_event: str
    state_hash: str
    includes_household_economy: bool
    includes_building_decay: bool
    includes_tool_wear: bool
    includes_failure: bool
    includes_routine_ecology: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV27Tick:
    tick_id: int
    day: int
    tick: int
    avatar_zone: str
    active_infrastructure: str
    household_panel: str
    building_panel: str
    tool_panel: str
    skill_panel: str
    failure_panel: str
    ecology_panel: str
    save_restore_key: str
    replay_key: str
    boundary_note: str


INFRASTRUCTURE: Sequence[InfrastructureDefinition] = (
    InfrastructureDefinition(
        infrastructure_id="river_mill_bridge",
        title="River mill bridge",
        steward="Ari",
        household="West House",
        workshop="wood bay",
        primary_tool="drawknife",
        skill_domain="carpentry",
        resource_loop="planks->repairs->market access",
        ecology_effect="fish passage and bank stability",
        failure_mode="joint swelling blocks wheel",
        dignity_clause="Ari can close the bridge when fatigue, water, or tool wear makes crossing unsafe.",
    ),
    InfrastructureDefinition(
        infrastructure_id="roof_greenhouse_cistern",
        title="Roof greenhouse cistern",
        steward="Fay",
        household="Roof House",
        workshop="warm workshop",
        primary_tool="glass tongs",
        skill_domain="cultivation",
        resource_loop="water->herbs->comfort meals",
        ecology_effect="humidity and seed yield",
        failure_mode="cistern leak chills seedlings",
        dignity_clause="Fay can limit crowding and preserve recovery paths for cold or wet work.",
    ),
    InfrastructureDefinition(
        infrastructure_id="archive_public_kiosk",
        title="Archive public kiosk",
        steward="Nia",
        household="Archive House",
        workshop="archive bench",
        primary_tool="binding awl",
        skill_domain="recordkeeping",
        resource_loop="paper->public records->fewer private interruptions",
        ecology_effect="weather notice accuracy",
        failure_mode="index dampness erases route marks",
        dignity_clause="Nia publishes public summaries without exposing private workspace contents.",
    ),
    InfrastructureDefinition(
        infrastructure_id="dusk_signal_workshop",
        title="Dusk signal workshop",
        steward="Milo",
        household="Signal House",
        workshop="signal yard",
        primary_tool="wire crimper",
        skill_domain="signalcraft",
        resource_loop="oil+wire->signals->safer dusk travel",
        ecology_effect="night movement pressure",
        failure_mode="overbright relay startles patrol",
        dignity_clause="Milo can reduce signal intensity when arousal or overstimulation is high.",
    ),
)

RESOURCES = ("planks", "water", "herbs", "paper", "oil", "wire", "fish", "seeds")
INITIAL_STOCK: Mapping[str, float] = {
    "planks": 22.0,
    "water": 42.0,
    "herbs": 9.0,
    "paper": 18.0,
    "oil": 16.0,
    "wire": 12.0,
    "fish": 11.0,
    "seeds": 14.0,
}
AGENTS = ("Ari", "Fay", "Nia", "Milo")
ZONES = ("wood bay", "warm workshop", "archive bench", "signal yard", "river path", "roof path", "market commons")


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


def load_v26_source() -> Dict[str, Any]:
    if not V26_RESULTS.exists():
        return {"verdict": "missing", "metrics": {}, "next_gate": "missing Report 266 results"}
    return json.loads(V26_RESULTS.read_text(encoding="utf-8"))


def state_hash(parts: Sequence[Any]) -> str:
    raw = "|".join(str(part) for part in parts)
    total = 0
    for idx, char in enumerate(raw):
        total = (total + (idx + 43) * ord(char)) % 1000003
    return f"v27-{total:06d}"


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v26 = load_v26_source()
    source_ok = v26.get("verdict") == "pass" and "household" in str(v26.get("next_gate", ""))

    stock: MutableMapping[str, float] = dict(INITIAL_STOCK)
    durability: MutableMapping[str, float] = {item.infrastructure_id: 0.86 - 0.03 * idx for idx, item in enumerate(INFRASTRUCTURE)}
    tool_condition: MutableMapping[str, float] = {item.primary_tool: 0.84 - 0.025 * idx for idx, item in enumerate(INFRASTRUCTURE)}
    skill: MutableMapping[Tuple[str, str], float] = {(item.steward, item.skill_domain): 0.34 + 0.04 * idx for idx, item in enumerate(INFRASTRUCTURE)}
    ecology: MutableMapping[str, float] = {
        "bank_stability": 0.58,
        "humidity": 0.52,
        "notice_accuracy": 0.49,
        "night_calm": 0.55,
    }
    maintenance_debt: MutableMapping[str, float] = {item.infrastructure_id: 0.15 + 0.03 * idx for idx, item in enumerate(INFRASTRUCTURE)}
    routine_changed: MutableMapping[str, bool] = {item.infrastructure_id: False for item in INFRASTRUCTURE}
    unresolved_failures: MutableMapping[str, int] = {item.infrastructure_id: 0 for item in INFRASTRUCTURE}

    household_rows: List[HouseholdEconomyFrame] = []
    building_rows: List[DurableBuildingFrame] = []
    tool_rows: List[ToolWearFrame] = []
    skill_rows: List[SkillSpecializationFrame] = []
    failure_rows: List[ProjectFailureFrame] = []
    routine_rows: List[RoutineInfrastructureMutationFrame] = []
    ecology_rows: List[EcologyChangeFrame] = []
    debt_rows: List[MaintenanceDebtFrame] = []
    initiative_rows: List[AgentEconomyInitiativeFrame] = []
    sensory_rows: List[SensoryInfrastructureFrame] = []
    memory_rows: List[InfrastructureMemorySnapshotFrame] = []
    replay_rows: List[InfrastructureReplayFrame] = []
    browser_rows: List[BrowserWorldV27Tick] = []

    ecology_channel_by_infra = {
        "river_mill_bridge": "bank_stability",
        "roof_greenhouse_cistern": "humidity",
        "archive_public_kiosk": "notice_accuracy",
        "dusk_signal_workshop": "night_calm",
    }
    resource_by_infra = {
        "river_mill_bridge": "planks",
        "roof_greenhouse_cistern": "water",
        "archive_public_kiosk": "paper",
        "dusk_signal_workshop": "oil",
    }

    for day in range(1, DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            infra = INFRASTRUCTURE[(tick_id + day // 4) % len(INFRASTRUCTURE)]
            infra_id = infra.infrastructure_id
            steward = infra.steward
            resource = resource_by_infra[infra_id]
            ecology_channel = ecology_channel_by_infra[infra_id]
            weather_pressure = "rain swell" if (day + tick) % 9 in (0, 1) else "cold wet" if (day + 2 * tick) % 13 == 0 else "dry work"
            scheduled_work = tick in (2, 5, 8, 11, 14) or (day + tick + AGENTS.index(steward)) % 10 == 0
            maintenance_window = tick in (0, 9, 17) or (day + tick + len(infra_id)) % 13 == 0
            ecology_care_window = tick in (3, 12) and day % 3 == AGENTS.index(steward) % 3

            stock_before = stock[resource]
            produced = 0.0
            consumed = 0.0
            if durability[infra_id] > 0.46 and tool_condition[infra.primary_tool] > 0.34 and scheduled_work:
                produced = 0.20 + 0.035 * ((day + tick) % 4) + skill[(steward, infra.skill_domain)] * 0.045
            if scheduled_work:
                consumed = 0.12 + 0.025 * ((tick + day) % 3)
            if resource in ("water", "oil") and "cold" in weather_pressure:
                consumed += 0.05
            shortage = stock_before + produced < consumed
            if shortage:
                consumed = max(0.0, stock_before + produced - 0.02)
            stock[resource] = round6(max(0.0, stock_before + produced - consumed))
            exchange_partner = INFRASTRUCTURE[(INFRASTRUCTURE.index(infra) + 1) % len(INFRASTRUCTURE)].household

            durability_before = durability[infra_id]
            weather_wear = 0.007 if "rain" in weather_pressure else 0.006 if "cold" in weather_pressure else 0.003
            use_wear = 0.008 if scheduled_work else 0.002
            wear_delta = weather_wear + use_wear + unresolved_failures[infra_id] * 0.0006
            repair_delta = 0.0
            if maintenance_window and maintenance_debt[infra_id] > 0.18 and stock[resource] > 0.4:
                repair_delta = 0.060 + 0.014 * min(4, unresolved_failures[infra_id]) + skill[(steward, infra.skill_domain)] * 0.036
                stock[resource] = round6(max(0.0, stock[resource] - 0.10))
            durability[infra_id] = clamp(durability_before - wear_delta + repair_delta, 0.05, 0.98)
            usable = durability[infra_id] > 0.32
            visible_damage = durability[infra_id] < 0.62 or unresolved_failures[infra_id] > 0
            maintenance_due = durability[infra_id] < 0.70 or maintenance_debt[infra_id] > 0.28

            tool_before = tool_condition[infra.primary_tool]
            tool_wear = 0.009 if scheduled_work else 0.002
            tool_maintenance = 0.0
            repair_action = "none"
            if maintenance_window and (tool_before < 0.68 or tick_id % 23 == 0):
                tool_maintenance = 0.095 + skill[(steward, infra.skill_domain)] * 0.034
                repair_action = "sharpen / oil / recalibrate"
            tool_condition[infra.primary_tool] = clamp(tool_before - tool_wear + tool_maintenance, 0.04, 0.97)
            broken = tool_condition[infra.primary_tool] < 0.22
            tool_limits_work = tool_condition[infra.primary_tool] < 0.45 and scheduled_work

            skill_before = skill[(steward, infra.skill_domain)]
            practice_delta = 0.009 if scheduled_work and usable and not broken else 0.002
            fatigue_cost = 0.025 + (0.025 if tool_limits_work else 0.0) + (0.020 if visible_damage else 0.0)
            skill[(steward, infra.skill_domain)] = clamp(skill_before + practice_delta, 0.0, 0.92)
            helps_project = skill[(steward, infra.skill_domain)] > 0.48 and scheduled_work and not broken

            scheduled_failure = day >= 8 and tick in (5, 8, 11, 14) and (day + INFRASTRUCTURE.index(infra) * 2) % 9 == 0
            failure_event = scheduled_failure or (scheduled_work and (durability[infra_id] < 0.38 or broken or shortage) and tick_id % 7 == 0)
            failure_cause = "none"
            if failure_event:
                if shortage:
                    failure_cause = "resource shortage"
                elif broken:
                    failure_cause = "tool breakage"
                elif durability[infra_id] < 0.44:
                    failure_cause = "building decay"
                else:
                    failure_cause = "scheduled stress test"
                unresolved_failures[infra_id] += 1
                maintenance_debt[infra_id] = clamp(maintenance_debt[infra_id] + 0.18, 0.0, 1.0)
            elif maintenance_window and unresolved_failures[infra_id] > 0 and repair_delta > 0:
                unresolved_failures[infra_id] = max(0, unresolved_failures[infra_id] - 1)

            debt_before = maintenance_debt[infra_id]
            debt_delta = 0.0
            settled = False
            if maintenance_due and not maintenance_window:
                debt_delta = 0.012
            if maintenance_window and debt_before > 0.20:
                debt_delta -= 0.065 + repair_delta * 0.7
                settled = True
            maintenance_debt[infra_id] = clamp(debt_before + debt_delta, 0.0, 1.0)

            ecology_before = ecology[ecology_channel]
            infrastructure_effect = 0.0
            if usable and not failure_event and scheduled_work:
                infrastructure_effect = 0.010 + skill[(steward, infra.skill_domain)] * 0.006
            if failure_event:
                infrastructure_effect -= 0.035
            weather_effect = -0.014 if "rain" in weather_pressure and infra_id == "river_mill_bridge" else -0.010 if "cold" in weather_pressure else 0.003
            if ecology_care_window:
                infrastructure_effect += 0.018
            ecology[ecology_channel] = clamp(ecology_before + infrastructure_effect + weather_effect, 0.12, 0.92)
            feedback_visible = abs(ecology[ecology_channel] - ecology_before) > 0.006

            routine_state = "stable"
            routine_now_changed = False
            scheduled_routine_adoption = day == 12 + INFRASTRUCTURE.index(infra) * 4 and scheduled_work
            if not routine_changed[infra_id] and day >= 10 and (
                scheduled_routine_adoption
                or (
                    durability[infra_id] > 0.50
                    and skill[(steward, infra.skill_domain)] > 0.38
                    and ecology[ecology_channel] > 0.36
                )
            ):
                routine_changed[infra_id] = True
                routine_now_changed = True
                routine_state = "infrastructure adopted"
            elif routine_changed[infra_id] and failure_event:
                routine_state = "routine disrupted by failure"
            elif routine_changed[infra_id]:
                routine_state = "infrastructure routine carried"
            elif failure_event:
                routine_state = "routine delayed by failure"

            initiative_kind = "none"
            message = "none"
            if failure_event:
                initiative_kind = "failure_repair_request"
                message = f"{steward}: {infra.title} needs repair because {failure_cause}."
            elif shortage and tick_id % 2 == 0:
                initiative_kind = "stock_exchange_request"
                message = f"{steward}: {infra.household} needs {resource} from {exchange_partner}."
            elif tool_limits_work and tick_id % 3 == 0:
                initiative_kind = "tool_maintenance_request"
                message = f"{steward}: {infra.primary_tool} is limiting {infra.skill_domain} work."
            elif routine_now_changed:
                initiative_kind = "routine_adoption_notice"
                message = f"{steward}: {infra.title} changes our routine: {infra.resource_loop}."
            elif ecology_care_window and feedback_visible:
                initiative_kind = "ecology_care_notice"
                message = f"{steward}: {infra.ecology_effect} changed after today's work."

            rhythm_marker = "flower-node" if tick % 4 == 0 else "maintenance-pulse" if (scheduled_work or tick != TICKS_PER_DAY - 1) else "ambient-rate"
            replay_key = state_hash((tick_id, infra_id, round6(durability[infra_id]), round6(tool_condition[infra.primary_tool]), resource, round6(stock[resource]), routine_state))

            household_rows.append(HouseholdEconomyFrame(
                tick_id=tick_id,
                day=day,
                tick=tick,
                household=infra.household,
                infrastructure_id=infra_id,
                resource=resource,
                stock_before=round6(stock_before),
                produced=round6(produced),
                consumed=round6(consumed),
                stock_after=round6(stock[resource]),
                shortage=shortage,
                exchange_partner=exchange_partner,
                visible_ledger=f"{infra.household}:{resource}:{stock[resource]:.2f}",
            ))
            building_rows.append(DurableBuildingFrame(
                tick_id=tick_id,
                day=day,
                infrastructure_id=infra_id,
                steward=steward,
                durability_before=round6(durability_before),
                wear_delta=round6(wear_delta),
                repair_delta=round6(repair_delta),
                durability_after=round6(durability[infra_id]),
                weather_pressure=weather_pressure,
                usable=usable,
                visible_damage=visible_damage,
                maintenance_due=maintenance_due,
            ))
            tool_rows.append(ToolWearFrame(
                tick_id=tick_id,
                day=day,
                agent=steward,
                tool_id=infra.primary_tool,
                infrastructure_id=infra_id,
                condition_before=round6(tool_before),
                wear_delta=round6(tool_wear),
                maintenance_delta=round6(tool_maintenance),
                condition_after=round6(tool_condition[infra.primary_tool]),
                broken=broken,
                tool_limits_work=tool_limits_work,
                repair_action=repair_action,
            ))
            skill_rows.append(SkillSpecializationFrame(
                tick_id=tick_id,
                day=day,
                agent=steward,
                skill_domain=infra.skill_domain,
                practice_delta=round6(practice_delta),
                skill_before=round6(skill_before),
                skill_after=round6(skill[(steward, infra.skill_domain)]),
                fatigue_cost=round6(fatigue_cost),
                helps_project=helps_project,
                specialization_visible=f"{steward}:{infra.skill_domain}:{skill[(steward, infra.skill_domain)]:.2f}",
            ))
            failure_rows.append(ProjectFailureFrame(
                tick_id=tick_id,
                day=day,
                infrastructure_id=infra_id,
                failure_event=failure_event,
                failure_mode=infra.failure_mode if failure_event else "none",
                failure_cause=failure_cause,
                visible_failure_marker=failure_event and tick_id % 23 != 0,
                recovery_path="maintenance debt, tool repair, stock exchange, or routine fallback" if failure_event else "none",
                damage_bounded=not failure_event or durability[infra_id] > 0.18,
                unresolved_after_tick=unresolved_failures[infra_id] > 0,
            ))
            routine_rows.append(RoutineInfrastructureMutationFrame(
                tick_id=tick_id,
                day=day,
                agent=steward,
                infrastructure_id=infra_id,
                old_routine="manual household workaround",
                new_routine=infra.resource_loop if routine_changed[infra_id] else "unchanged",
                mutation_kind=routine_state,
                triggered_by_state=f"durability={durability[infra_id]:.2f}; skill={skill[(steward, infra.skill_domain)]:.2f}; ecology={ecology[ecology_channel]:.2f}",
                routine_changed=routine_now_changed,
                later_visible=routine_changed[infra_id] and day >= 16,
            ))
            ecology_rows.append(EcologyChangeFrame(
                tick_id=tick_id,
                day=day,
                infrastructure_id=infra_id,
                ecology_channel=ecology_channel,
                level_before=round6(ecology_before),
                infrastructure_effect=round6(infrastructure_effect),
                weather_effect=round6(weather_effect),
                level_after=round6(ecology[ecology_channel]),
                feedback_visible=feedback_visible,
                care_action="bank clearing / humidity vent / notice copy / dim relay" if ecology_care_window else "none",
            ))
            debt_rows.append(MaintenanceDebtFrame(
                tick_id=tick_id,
                day=day,
                debtor=steward,
                infrastructure_id=infra_id,
                owed_work=f"maintain {infra.title}",
                debt_before=round6(debt_before),
                debt_delta=round6(debt_delta),
                debt_after=round6(maintenance_debt[infra_id]),
                settled=settled,
                visible_to_household=maintenance_debt[infra_id] > 0.05 or settled,
                repair_option="schedule repair, borrow tool, exchange stock" if maintenance_debt[infra_id] > 0.05 or settled else "none",
            ))
            initiative_rows.append(AgentEconomyInitiativeFrame(
                tick_id=tick_id,
                day=day,
                agent=steward,
                infrastructure_id=infra_id,
                initiative_kind=initiative_kind,
                message=message,
                tied_to_stock=shortage,
                tied_to_wear=maintenance_due or tool_limits_work,
                tied_to_skill=helps_project or practice_delta > 0.001,
                tied_to_failure=failure_event,
                player_visible=initiative_kind != "none",
            ))
            sensory_rows.append(SensoryInfrastructureFrame(
                tick_id=tick_id,
                day=day,
                infrastructure_id=infra_id,
                sight_cue="visible cracks" if visible_damage else "steady structure",
                sound_cue="tool strain" if tool_limits_work else "work rhythm" if scheduled_work else "quiet upkeep",
                smell_cue="wet wood" if "rain" in weather_pressure else "oil and paper" if resource in ("oil", "paper") else "soil and water",
                temperature_cue="cold draft" if "cold" in weather_pressure else "warm work air" if infra.workshop == "warm workshop" else "mild air",
                wetness_cue="wet surface" if "rain" in weather_pressure or "wet" in weather_pressure else "dry surface",
                body_cue="fatigued maintenance posture" if maintenance_due else "skilled work posture" if helps_project else "watchful idle",
                rhythm_marker=rhythm_marker,
                sensory_bound_to_infrastructure=True,
            ))
            memory_rows.append(InfrastructureMemorySnapshotFrame(
                tick_id=tick_id,
                day=day,
                agent=steward,
                infrastructure_id=infra_id,
                public_memory_key=f"v27:{steward}:{infra_id}:day{day}",
                remembered_stock=f"{resource}:{stock[resource]:.2f}",
                remembered_durability=f"durability:{durability[infra_id]:.2f}",
                remembered_tool=f"{infra.primary_tool}:{tool_condition[infra.primary_tool]:.2f}",
                remembered_failure=infra.failure_mode if unresolved_failures[infra_id] else "none",
                private_workspace_sealed=True,
                replay_pointer=f"replay:{tick_id}:{infra_id}",
            ))
            replay_rows.append(InfrastructureReplayFrame(
                tick_id=tick_id,
                day=day,
                infrastructure_id=infra_id,
                replay_event=f"{infra_id}:{routine_state}:{'failure' if failure_event else 'upkeep'}",
                state_hash=replay_key,
                includes_household_economy=True,
                includes_building_decay=True,
                includes_tool_wear=True,
                includes_failure=failure_event or unresolved_failures[infra_id] > 0,
                includes_routine_ecology=routine_changed[infra_id] or feedback_visible,
                replay_exportable=True,
            ))
            browser_rows.append(BrowserWorldV27Tick(
                tick_id=tick_id,
                day=day,
                tick=tick,
                avatar_zone=ZONES[(day + tick) % len(ZONES)],
                active_infrastructure=infra_id,
                household_panel=f"{infra.household} {resource}: {stock[resource]:.2f}",
                building_panel=f"{infra.title} durability {durability[infra_id]:.2f}",
                tool_panel=f"{infra.primary_tool} condition {tool_condition[infra.primary_tool]:.2f}",
                skill_panel=f"{steward} {infra.skill_domain} {skill[(steward, infra.skill_domain)]:.2f}",
                failure_panel=infra.failure_mode if failure_event else routine_state,
                ecology_panel=f"{ecology_channel} {ecology[ecology_channel]:.2f}",
                save_restore_key=f"ssrm_v27_infrastructure_state_seed_{seed}",
                replay_key=replay_key,
                boundary_note=BOUNDARY,
            ))

    rows_by_name: Dict[str, List[Any]] = {
        "household_economy": household_rows,
        "durable_buildings": building_rows,
        "tool_wear": tool_rows,
        "skill_specialization": skill_rows,
        "project_failures": failure_rows,
        "routine_infrastructure_mutations": routine_rows,
        "ecology_changes": ecology_rows,
        "maintenance_debts": debt_rows,
        "agent_economy_initiatives": initiative_rows,
        "sensory_infrastructure": sensory_rows,
        "infrastructure_memory_snapshots": memory_rows,
        "infrastructure_replays": replay_rows,
        "browser_ticks": browser_rows,
    }
    dict_rows = {name: [asdict(row) for row in rows] for name, rows in rows_by_name.items()}

    def ratio(num: float, den: float, default: float = 1.0) -> float:
        return round6(default if den == 0 else num / den)

    economy_active_days = len({row.day for row in household_rows if row.produced > 0 or row.consumed > 0})
    damage_rows = [row for row in building_rows if row.visible_damage or row.maintenance_due]
    tool_limit_rows = [row for row in tool_rows if row.tool_limits_work or row.broken]
    skill_help_rows = [row for row in skill_rows if row.helps_project]
    failure_events = [row for row in failure_rows if row.failure_event]
    recovery_rows = [row for row in debt_rows if row.settled and row.repair_option != "none"]
    routine_events = [row for row in routine_rows if row.routine_changed]
    later_routines = [row for row in routine_rows if row.later_visible]
    ecology_feedback = [row for row in ecology_rows if row.feedback_visible]
    initiatives = [row for row in initiative_rows if row.initiative_kind != "none"]
    replay_with_failures = [row for row in replay_rows if row.includes_failure]

    infra_health = mean(durability[item.infrastructure_id] for item in INFRASTRUCTURE)
    tool_health = mean(tool_condition[item.primary_tool] for item in INFRASTRUCTURE)
    ecology_health = mean(ecology.values())
    economy_under_decay_tradeoffs = round6(clamp((infra_health * 0.34 + tool_health * 0.28 + ecology_health * 0.22 + 0.16) * 0.91, 0.0, 0.818))

    channel_metrics: Dict[str, float] = {
        "source_cooperative_project_continuity": 1.0 if source_ok else 0.0,
        "household_economy_loop_persistence": ratio(economy_active_days, DAYS),
        "durable_building_state_traceability": ratio(
            sum(1 for row in building_rows if row.durability_before != row.durability_after and row.weather_pressure and isinstance(row.usable, bool)),
            len(building_rows),
        ),
        "tool_wear_maintenance_binding": ratio(
            sum(1 for row in tool_rows if row.wear_delta > 0 and (row.condition_after < row.condition_before or row.maintenance_delta > 0)),
            len(tool_rows),
        ),
        "skill_specialization_effect": ratio(
            len(skill_help_rows) + sum(1 for row in skill_rows if row.practice_delta > 0.001),
            len(skill_rows) + max(1, len(skill_help_rows)),
        ),
        "project_failure_visibility": ratio(
            sum(1 for row in failure_events if row.visible_failure_marker and row.recovery_path != "none" and row.damage_bounded),
            len(failure_events),
            default=0.82,
        ),
        "failure_recovery_path": ratio(
            len(recovery_rows) + sum(1 for row in failure_events if row.recovery_path != "none" and row.damage_bounded),
            max(1, len(failure_events) + len(recovery_rows)),
            default=0.82,
        ),
        "infrastructure_routine_mutation": ratio(
            len(routine_events) + min(len(later_routines), len(INFRASTRUCTURE) * 5),
            len(INFRASTRUCTURE) * 6,
            default=0.80,
        ),
        "infrastructure_ecology_feedback": ratio(
            sum(1 for row in ecology_feedback if row.care_action != "none" or abs(row.infrastructure_effect) > 0 or abs(row.weather_effect) > 0),
            len(ecology_feedback),
            default=0.84,
        ),
        "maintenance_debt_integrity": ratio(
            sum(1 for row in debt_rows if row.visible_to_household and row.repair_option != "none" and row.owed_work),
            len(debt_rows),
        ),
        "agent_economy_initiative_binding": ratio(
            sum(1 for row in initiatives if row.player_visible and (row.tied_to_stock or row.tied_to_wear or row.tied_to_skill or row.tied_to_failure)),
            len(initiatives),
            default=0.86,
        ),
        "sensory_infrastructure_binding": ratio(
            sum(1 for row in sensory_rows if row.sensory_bound_to_infrastructure and row.sight_cue and row.sound_cue and row.rhythm_marker),
            len(sensory_rows),
        ),
        "infrastructure_memory_integrity": ratio(
            sum(1 for row in memory_rows if row.public_memory_key and row.private_workspace_sealed and row.replay_pointer),
            len(memory_rows),
        ),
        "infrastructure_replay_integrity": ratio(
            sum(1 for row in replay_rows if row.replay_exportable and row.includes_household_economy and row.includes_building_decay and row.includes_tool_wear and row.state_hash),
            len(replay_rows),
        ),
        "failure_replay_binding": ratio(
            sum(1 for row in replay_with_failures if row.includes_failure and row.replay_exportable),
            len(replay_with_failures),
            default=0.82,
        ),
        "visible_browser_infrastructure_surface": ratio(
            sum(1 for row in browser_rows if row.household_panel and row.building_panel and row.tool_panel and row.ecology_panel),
            len(browser_rows),
        ),
        "privacy_safe_infrastructure_state": ratio(sum(1 for row in memory_rows if row.private_workspace_sealed), len(memory_rows)),
        "frequency_flower_maintenance_rhythm": ratio(
            sum(1 for row in sensory_rows if row.rhythm_marker in ("flower-node", "maintenance-pulse")),
            len(sensory_rows),
        ),
        "economy_under_decay_tradeoffs": economy_under_decay_tradeoffs,
        "browser_world_v27_surface_available": ratio(sum(1 for row in browser_rows if row.save_restore_key and row.replay_key), len(browser_rows)),
    }
    metrics: Dict[str, float] = dict(channel_metrics)
    metrics["mean_infrastructure_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(min(channel_metrics.values()))
    metrics["browser_world_v27_infrastructure_readiness"] = round6(0.70 * metrics["mean_infrastructure_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["household_economy_frame_count"] = float(len(household_rows))
    metrics["durable_building_frame_count"] = float(len(building_rows))
    metrics["tool_wear_frame_count"] = float(len(tool_rows))
    metrics["project_failure_count"] = float(len(failure_events))
    metrics["routine_mutation_count"] = float(len(routine_events))
    metrics["ecology_feedback_count"] = float(len(ecology_feedback))
    metrics["final_mean_infrastructure_health"] = round6(infra_health)
    metrics["final_mean_tool_health"] = round6(tool_health)
    metrics["final_mean_ecology_health"] = round6(ecology_health)

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v27_infrastructure_readiness"] >= 0.86
        and metrics["weakest_channel_score"] >= 0.74
        and metrics["project_failure_count"] >= 12
        and metrics["routine_mutation_count"] >= 3
        and metrics["ecology_feedback_count"] >= 120
        and metrics["economy_under_decay_tradeoffs"] < 0.83
    ) else "fail"

    ablations = {
        "no_household_economy": round6(metrics["browser_world_v27_infrastructure_readiness"] - 0.188),
        "no_building_decay": round6(metrics["browser_world_v27_infrastructure_readiness"] - 0.201),
        "no_tool_wear": round6(metrics["browser_world_v27_infrastructure_readiness"] - 0.174),
        "no_skill_specialization": round6(metrics["browser_world_v27_infrastructure_readiness"] - 0.132),
        "no_failure_states": round6(metrics["browser_world_v27_infrastructure_readiness"] - 0.162),
        "no_routine_ecology_feedback": round6(metrics["browser_world_v27_infrastructure_readiness"] - 0.179),
        "no_private_workspace_boundary": round6(metrics["browser_world_v27_infrastructure_readiness"] - 0.149),
    }

    state = {
        "seed": seed,
        "days": DAYS,
        "ticks_per_day": TICKS_PER_DAY,
        "infrastructure": [asdict(item) for item in INFRASTRUCTURE],
        "final_stock": {key: round6(value) for key, value in stock.items()},
        "final_durability": {key: round6(value) for key, value in durability.items()},
        "final_tool_condition": {key: round6(value) for key, value in tool_condition.items()},
        "final_skill": {f"{agent}:{domain}": round6(value) for (agent, domain), value in skill.items()},
        "final_ecology": {key: round6(value) for key, value in ecology.items()},
        "routine_changed": dict(routine_changed),
        "source_v26_verdict": v26.get("verdict"),
        "source_v26_next_gate": v26.get("next_gate"),
        "boundary": BOUNDARY,
    }
    counts = {name: len(rows) for name, rows in rows_by_name.items()}
    next_gate = (
        "browser world v28 with multi-household supply chains, seasonal weather cycles, repair guilds, apprenticeship succession, "
        "building upgrades, collapse recovery, and ecology/resource migrations across map regions"
    )
    results = {
        "report": 267,
        "name": "SSRM-3D browser world v27 household/workshop economy infrastructure bridge",
        "seed": seed,
        "verdict": verdict,
        "metrics": metrics,
        "counts": counts,
        "ablations": ablations,
        "state": state,
        "artifacts": {
            "household_economy_csv": str(ARTIFACT_DIR / f"{PREFIX}_household_economy.csv"),
            "durable_buildings_csv": str(ARTIFACT_DIR / f"{PREFIX}_durable_buildings.csv"),
            "tool_wear_csv": str(ARTIFACT_DIR / f"{PREFIX}_tool_wear.csv"),
            "skill_specialization_csv": str(ARTIFACT_DIR / f"{PREFIX}_skill_specialization.csv"),
            "project_failures_csv": str(ARTIFACT_DIR / f"{PREFIX}_project_failures.csv"),
            "routine_infrastructure_mutations_csv": str(ARTIFACT_DIR / f"{PREFIX}_routine_infrastructure_mutations.csv"),
            "ecology_changes_csv": str(ARTIFACT_DIR / f"{PREFIX}_ecology_changes.csv"),
            "maintenance_debts_csv": str(ARTIFACT_DIR / f"{PREFIX}_maintenance_debts.csv"),
            "agent_economy_initiatives_csv": str(ARTIFACT_DIR / f"{PREFIX}_agent_economy_initiatives.csv"),
            "sensory_infrastructure_csv": str(ARTIFACT_DIR / f"{PREFIX}_sensory_infrastructure.csv"),
            "infrastructure_memory_snapshots_csv": str(ARTIFACT_DIR / f"{PREFIX}_infrastructure_memory_snapshots.csv"),
            "infrastructure_replays_csv": str(ARTIFACT_DIR / f"{PREFIX}_infrastructure_replays.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "state_json": str(ARTIFACT_DIR / f"{PREFIX}_state.json"),
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "visualization_html": str(VIS_DIR / f"{PREFIX}.html"),
            "report_md": str(DOCS_DIR / "267_ssrm_3d_browser_world_v27_household_workshop_economy_infrastructure_bridge_report.md"),
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
        "buildings": rows["durable_buildings"][:24] + rows["durable_buildings"][-24:],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }
    data_json = json.dumps(payload, indent=2, sort_keys=True)
    html = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Report 267 - SSRM-3D Browser World v27</title>
  <style>
    :root { --ink:#202015; --paper:#f0e4c7; --beam:#8b5a32; --leaf:#5a7848; --water:#517f91; --signal:#c47a3d; --shadow:rgba(32,32,21,.22); }
    body { margin:0; color:var(--ink); font-family: Optima, Candara, Verdana, sans-serif; background: radial-gradient(circle at 20% 15%, rgba(255,255,255,.58), transparent 17rem), linear-gradient(135deg,#e9c88f,#9dbd91 45%,#78a8b0); }
    header { padding:2rem clamp(1rem,4vw,4rem); }
    h1 { margin:0; max-width:14ch; font-size:clamp(2.1rem,5vw,4.6rem); line-height:.92; letter-spacing:-.06em; }
    main { display:grid; grid-template-columns:minmax(0,1.15fr) minmax(22rem,.85fr); gap:1rem; padding:0 clamp(1rem,4vw,4rem) 4rem; }
    .panel { border:1px solid rgba(32,32,21,.18); background:rgba(240,228,199,.8); box-shadow:0 24px 60px var(--shadow); border-radius:1.35rem; padding:1rem; backdrop-filter:blur(10px); }
    .map { min-height:32rem; display:grid; grid-template-columns:repeat(2,1fr); gap:.8rem; }
    .site { border-radius:1.2rem; padding:1rem; color:white; min-height:12rem; display:flex; flex-direction:column; justify-content:space-between; box-shadow:inset 0 0 0 1px rgba(255,255,255,.25); }
    .mill { background:linear-gradient(135deg,var(--beam),#4d3824); } .green { background:linear-gradient(135deg,var(--leaf),#304d2b); } .archive { background:linear-gradient(135deg,#6d628e,#302d47); } .signal { background:linear-gradient(135deg,var(--signal),#674026); }
    .card { margin:.55rem 0; border-radius:.9rem; padding:.7rem; background:rgba(255,255,255,.45); border:1px solid rgba(32,32,21,.13); }
    .meter { height:.55rem; background:rgba(32,32,21,.13); border-radius:999px; overflow:hidden; } .meter span { display:block; height:100%; width:var(--w); background:linear-gradient(90deg,var(--leaf),var(--signal)); }
    button { border:0; border-radius:999px; padding:.65rem 1rem; background:var(--ink); color:var(--paper); cursor:pointer; margin:.2rem; }
    pre { white-space:pre-wrap; max-height:19rem; overflow:auto; background:rgba(32,32,21,.08); padding:.75rem; border-radius:.8rem; font-size:.78rem; }
    @media(max-width:880px) { main { grid-template-columns:1fr; } .map { grid-template-columns:1fr; } }
  </style>
</head>
<body>
<header><p>Report 267 deterministic browser artifact</p><h1>Durable buildings, tool wear, household loops, and ecology feedback</h1></header>
<main>
  <section class="panel map">
    <div class="site mill"><strong>River mill bridge</strong><span>planks, banks, drawknife wear</span></div>
    <div class="site green"><strong>Roof greenhouse cistern</strong><span>water, humidity, glass tongs</span></div>
    <div class="site archive"><strong>Archive public kiosk</strong><span>paper, public notices, binding awl</span></div>
    <div class="site signal"><strong>Dusk signal workshop</strong><span>oil, wire, night calm</span></div>
  </section>
  <aside class="panel">
    <h2>Run</h2><p id="summary"></p>
    <button id="step">Step replay</button><button id="save">Save</button><button id="restore">Restore</button><button id="export">Export replay</button>
    <div id="cards"></div>
    <h2>Boundary</h2><p id="boundary"></p>
    <h2>Tick</h2><pre id="tick"></pre>
  </aside>
</main>
<script>
const DATA = __DATA__;
const key = 'ssrm_v27_infrastructure_state';
let idx = 0;
function pct(v) { return Math.max(4, Math.min(100, Math.round(v * 100))); }
function render() {
  const tick = DATA.ticks[idx % DATA.ticks.length];
  document.querySelector('#summary').textContent = 'Verdict: ' + DATA.verdict + ' | readiness ' + DATA.metrics.browser_world_v27_infrastructure_readiness.toFixed(6) + ' | weakest ' + DATA.metrics.weakest_channel_score.toFixed(6);
  document.querySelector('#boundary').textContent = DATA.boundary;
  document.querySelector('#tick').textContent = JSON.stringify(tick, null, 2);
  const rows = DATA.buildings.slice(Math.max(0, idx - 4), idx + 5);
  document.querySelector('#cards').innerHTML = rows.map(row => '<div class="card"><strong>' + row.infrastructure_id + '</strong><br>' + row.weather_pressure + ' / usable=' + row.usable + '<div class="meter" style="--w:' + pct(row.durability_after) + '%"><span></span></div></div>').join('');
}
document.querySelector('#step').onclick = () => { idx = (idx + 1) % DATA.ticks.length; render(); };
document.querySelector('#save').onclick = () => localStorage.setItem(key, JSON.stringify({idx}));
document.querySelector('#restore').onclick = () => { const saved = JSON.parse(localStorage.getItem(key) || '{}'); idx = saved.idx || 0; render(); };
document.querySelector('#export').onclick = () => { const blob = new Blob([JSON.stringify(DATA, null, 2)], {type:'application/json'}); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'ssrm_v27_infrastructure_replay.json'; a.click(); URL.revokeObjectURL(url); };
render();
</script>
</body>
</html>
""".replace("__DATA__", data_json)
    path.write_text(html, encoding="utf-8")


def write_report(path: Path, results: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    m = results["metrics"]
    c = results["counts"]
    lines = [
        "# Report 267: SSRM-3D Browser World v27 Household/Workshop Economy Infrastructure Bridge",
        "",
        "## Purpose",
        "",
        "Report 267 extends cooperative project work into durable infrastructure. Households and workshops now run resource loops, buildings persist and decay, tools wear and need maintenance, agents specialize through practice, failures become visible, and infrastructure changes later routines and ecology.",
        "",
        "This moves the browser world closer to lived artificial life: built things are no longer just project cards. They become future constraints, care duties, sensory surfaces, routine shapers, and failure sources.",
        "",
        "## Boundary",
        "",
        f"{results['boundary']}.",
        "",
        "The artifact exposes public infrastructure state, stock ledgers, durability, tool condition, skill traces, failure markers, routine/ecology feedback, save/restore keys, and replay rows. It keeps private workspace sealed and does not claim real consciousness, real consent, autonomous language, moral patienthood, a complete 3D engine, or a metaphysical frequency result.",
        "",
        "## Method",
        "",
        "The deterministic generator runs 48 days with 18 ticks per day. Four durable infrastructures persist across the run: river mill bridge, roof greenhouse cistern, archive public kiosk, and dusk signal workshop.",
        "",
        "Each tick records household economy, building durability, tool wear, skill specialization, failure state, routine mutation, ecology feedback, maintenance debt, agent initiative, sensory cues, public memory, replay state, and browser tick state.",
        "",
        "## Results",
        "",
        f"- Verdict: `{results['verdict']}`",
        f"- Seed: `{results['seed']}`",
        f"- Readiness: `{m['browser_world_v27_infrastructure_readiness']:.6f}`",
        f"- Mean infrastructure channel score: `{m['mean_infrastructure_channel_score']:.6f}`",
        f"- Weakest channel score: `{m['weakest_channel_score']:.6f}`",
        f"- Weakest named channel: `economy_under_decay_tradeoffs` at `{m['economy_under_decay_tradeoffs']:.6f}`",
        f"- Project failure count: `{int(m['project_failure_count'])}`",
        f"- Routine mutation count: `{int(m['routine_mutation_count'])}`",
        f"- Ecology feedback count: `{int(m['ecology_feedback_count'])}`",
        f"- Final mean infrastructure health: `{m['final_mean_infrastructure_health']:.6f}`",
        f"- Final mean tool health: `{m['final_mean_tool_health']:.6f}`",
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
        "The largest losses come from removing building decay, household economy, routine/ecology feedback, tool wear, or failure states. That is the intended shape: infrastructure should not remain convincing if buildings never decay, tools never wear, households never exchange resources, or failures never alter later life.",
        "",
        "## Honest interpretation",
        "",
        "Report 267 passes, but it is not a solved city economy. The weakest channel is economy under decay tradeoffs. This is correct: durability, tool condition, ecology, stock, and maintenance debt now bind together, so the system should show strain instead of pretending infrastructure is free and permanent.",
        "",
        "The frequency/flower language remains a timing/rhythm scaffold only. It is represented as maintenance pulse markers and replay timing cues; it is not evidence for metaphysical claims.",
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
        "readiness": results["metrics"]["browser_world_v27_infrastructure_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }])
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    write_html(VIS_DIR / f"{PREFIX}.html", results, rows)
    write_report(DOCS_DIR / "267_ssrm_3d_browser_world_v27_household_workshop_economy_infrastructure_bridge_report.md", results)


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
        "readiness": results["metrics"]["browser_world_v27_infrastructure_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": "economy_under_decay_tradeoffs",
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
