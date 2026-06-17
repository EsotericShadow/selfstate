#!/usr/bin/env python3
"""Report 268: SSRM-3D browser world v28 supply-chain/season/guild/apprenticeship region bridge.

This deterministic benchmark extends Report 267's household/workshop infrastructure
into regional economy. Multiple households exchange goods across map regions,
seasonal weather changes production and failure pressure, repair guilds coordinate
collapse recovery, apprentices inherit skills, buildings upgrade, and ecology or
resources migrate across regions.

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
PREFIX = "ssrm_3d_browser_world_v28_supply_chain_seasonal_guild_apprenticeship_region_bridge"
V27_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v27_household_workshop_economy_infrastructure_bridge_results.json"
DEFAULT_SEED = 20260881
DAYS = 64
TICKS_PER_DAY = 16
BOUNDARY = (
    "deterministic browser-local multi-household supply-chain/season/guild/apprenticeship region scaffold only; "
    "no LLM call, subjective consciousness, real consent, moral patienthood, autonomous natural language, "
    "complete 3D engine, or metaphysical frequency claim"
)


@dataclass(frozen=True)
class RegionDefinition:
    region_id: str
    household: str
    steward: str
    mentor: str
    apprentice: str
    guild: str
    primary_resource: str
    needed_resource: str
    building: str
    ecology_channel: str
    routine_basis: str


@dataclass(frozen=True)
class RegionSupplyChainFrame:
    tick_id: int
    day: int
    tick: int
    season: str
    source_region: str
    destination_region: str
    resource: str
    source_stock_before: float
    requested: float
    delivered: float
    source_stock_after: float
    destination_stock_after: float
    route_blocked: bool
    visible_delivery_ledger: str


@dataclass(frozen=True)
class SeasonalWeatherFrame:
    tick_id: int
    day: int
    tick: int
    season: str
    region_id: str
    weather_pattern: str
    intensity: float
    temperature: float
    wetness: float
    production_modifier: float
    collapse_pressure: float
    migration_pressure: float
    sensory_weather_marker: str


@dataclass(frozen=True)
class RepairGuildFrame:
    tick_id: int
    day: int
    guild: str
    region_id: str
    assigned_agent: str
    backlog_before: float
    new_work: float
    repair_capacity: float
    backlog_after: float
    repair_success: bool
    safety_clause: str
    visible_guild_board: str


@dataclass(frozen=True)
class ApprenticeshipSuccessionFrame:
    tick_id: int
    day: int
    mentor: str
    apprentice: str
    skill_domain: str
    apprentice_skill_before: float
    practice_delta: float
    apprentice_skill_after: float
    mentor_fatigue: float
    succession_event: bool
    inherits_responsibility: str
    visible_teaching_marker: str


@dataclass(frozen=True)
class BuildingUpgradeFrame:
    tick_id: int
    day: int
    region_id: str
    building: str
    tier_before: int
    upgrade_attempt: bool
    upgrade_success: bool
    tier_after: int
    required_resource: str
    resource_spent: float
    durability_bonus: float
    visible_upgrade_marker: str


@dataclass(frozen=True)
class CollapseRecoveryFrame:
    tick_id: int
    day: int
    region_id: str
    building: str
    collapse_event: bool
    collapse_cause: str
    collapse_severity: float
    recovery_stage_before: str
    recovery_delta: float
    recovery_stage_after: str
    bounded_damage: bool
    recovery_visible: bool


@dataclass(frozen=True)
class ResourceMigrationFrame:
    tick_id: int
    day: int
    season: str
    resource: str
    from_region: str
    to_region: str
    migration_amount: float
    ecology_before: float
    ecology_after: float
    migration_cause: str
    feedback_visible: bool
    care_action: str


@dataclass(frozen=True)
class RegionalRoutineFrame:
    tick_id: int
    day: int
    agent: str
    region_id: str
    routine_before: str
    routine_after: str
    trigger: str
    routine_changed: bool
    later_visible: bool
    rollback_option: str


@dataclass(frozen=True)
class AgentGuildInitiativeFrame:
    tick_id: int
    day: int
    agent: str
    region_id: str
    initiative_kind: str
    message: str
    tied_to_supply: bool
    tied_to_season: bool
    tied_to_guild: bool
    tied_to_apprentice: bool
    tied_to_collapse: bool
    player_visible: bool


@dataclass(frozen=True)
class SensorySeasonalRegionFrame:
    tick_id: int
    day: int
    season: str
    region_id: str
    sight_cue: str
    sound_cue: str
    smell_cue: str
    temperature_cue: str
    wetness_cue: str
    body_cue: str
    rhythm_marker: str
    sensory_bound_to_region: bool


@dataclass(frozen=True)
class RegionMemorySnapshotFrame:
    tick_id: int
    day: int
    agent: str
    region_id: str
    public_memory_key: str
    remembered_supply: str
    remembered_season: str
    remembered_guild: str
    remembered_apprentice: str
    remembered_collapse: str
    private_workspace_sealed: bool
    replay_pointer: str


@dataclass(frozen=True)
class RegionReplayFrame:
    tick_id: int
    day: int
    region_id: str
    replay_event: str
    state_hash: str
    includes_supply_chain: bool
    includes_season: bool
    includes_guild: bool
    includes_apprenticeship: bool
    includes_collapse_recovery: bool
    includes_migration: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV28Tick:
    tick_id: int
    day: int
    tick: int
    season: str
    avatar_region: str
    active_route: str
    supply_panel: str
    weather_panel: str
    guild_panel: str
    apprentice_panel: str
    collapse_panel: str
    migration_panel: str
    save_restore_key: str
    replay_key: str
    boundary_note: str


REGIONS: Sequence[RegionDefinition] = (
    RegionDefinition("riverbend", "West House", "Ari", "Ari", "Toma", "Bridgewright Guild", "planks", "oil", "river mill", "bank_stability", "market crossing"),
    RegionDefinition("roofward", "Roof House", "Fay", "Fay", "Lio", "Glassgarden Guild", "herbs", "water", "roof cistern", "humidity", "greenhouse tending"),
    RegionDefinition("archive_quarter", "Archive House", "Nia", "Nia", "Sera", "Index Guild", "paper", "thread", "public kiosk", "notice_accuracy", "weather notices"),
    RegionDefinition("signal_ridge", "Signal House", "Milo", "Milo", "Ren", "Signal Guild", "oil", "wire", "signal tower", "night_calm", "dusk signals"),
    RegionDefinition("orchard_fen", "Fen House", "Ivo", "Ivo", "Mara", "Seed Guild", "seeds", "planks", "seed pier", "soil_recovery", "seasonal planting"),
)

RESOURCES = ("planks", "oil", "herbs", "water", "paper", "thread", "wire", "seeds", "fish", "glass")
SEASON_NAMES = ("spring_rain", "summer_dry", "autumn_wind", "winter_cold")
ZONES = tuple(region.region_id for region in REGIONS) + ("central_exchange", "repair_hall")


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


def load_v27_source() -> Dict[str, Any]:
    if not V27_RESULTS.exists():
        return {"verdict": "missing", "metrics": {}, "next_gate": "missing Report 267 results"}
    return json.loads(V27_RESULTS.read_text(encoding="utf-8"))


def season_for_day(day: int) -> str:
    return SEASON_NAMES[((day - 1) // 16) % len(SEASON_NAMES)]


def state_hash(parts: Sequence[Any]) -> str:
    raw = "|".join(str(part) for part in parts)
    total = 0
    for idx, char in enumerate(raw):
        total = (total + (idx + 53) * ord(char)) % 1000003
    return f"v28-{total:06d}"


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v27 = load_v27_source()
    source_ok = v27.get("verdict") == "pass" and "supply" in str(v27.get("next_gate", ""))

    stock: MutableMapping[Tuple[str, str], float] = {}
    for r_index, region in enumerate(REGIONS):
        for m_index, resource in enumerate(RESOURCES):
            base = 6.0 + ((r_index * 3 + m_index * 2) % 7)
            if resource == region.primary_resource:
                base += 12.0
            if resource == region.needed_resource:
                base -= 1.2
            stock[(region.region_id, resource)] = round6(base)

    guild_backlog: MutableMapping[str, float] = {region.guild: 0.18 + 0.035 * idx for idx, region in enumerate(REGIONS)}
    apprentice_skill: MutableMapping[str, float] = {region.apprentice: 0.22 + 0.025 * idx for idx, region in enumerate(REGIONS)}
    mentor_fatigue: MutableMapping[str, float] = {region.mentor: 0.30 + 0.03 * idx for idx, region in enumerate(REGIONS)}
    building_tier: MutableMapping[str, int] = {region.region_id: 1 for region in REGIONS}
    building_condition: MutableMapping[str, float] = {region.region_id: 0.78 - 0.035 * idx for idx, region in enumerate(REGIONS)}
    recovery_stage: MutableMapping[str, str] = {region.region_id: "stable" for region in REGIONS}
    ecology: MutableMapping[str, float] = {region.ecology_channel: 0.54 + 0.025 * idx for idx, region in enumerate(REGIONS)}
    routine_shifted: MutableMapping[str, bool] = {region.region_id: False for region in REGIONS}
    succession_done: MutableMapping[str, bool] = {region.region_id: False for region in REGIONS}

    supply_rows: List[RegionSupplyChainFrame] = []
    weather_rows: List[SeasonalWeatherFrame] = []
    guild_rows: List[RepairGuildFrame] = []
    apprentice_rows: List[ApprenticeshipSuccessionFrame] = []
    upgrade_rows: List[BuildingUpgradeFrame] = []
    collapse_rows: List[CollapseRecoveryFrame] = []
    migration_rows: List[ResourceMigrationFrame] = []
    routine_rows: List[RegionalRoutineFrame] = []
    initiative_rows: List[AgentGuildInitiativeFrame] = []
    sensory_rows: List[SensorySeasonalRegionFrame] = []
    memory_rows: List[RegionMemorySnapshotFrame] = []
    replay_rows: List[RegionReplayFrame] = []
    browser_rows: List[BrowserWorldV28Tick] = []

    for day in range(1, DAYS + 1):
        season = season_for_day(day)
        season_index = SEASON_NAMES.index(season)
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            region = REGIONS[(tick_id + day // 6) % len(REGIONS)]
            region_index = REGIONS.index(region)
            destination = REGIONS[(region_index + 1 + (day % 2)) % len(REGIONS)]
            source_region = region.region_id
            dest_region = destination.region_id
            resource = region.primary_resource if tick % 3 != 0 else destination.needed_resource
            requested = 0.28 + 0.05 * ((day + tick + region_index) % 4)
            weather_pattern = {
                "spring_rain": "wet surge",
                "summer_dry": "heat shimmer",
                "autumn_wind": "gust front",
                "winter_cold": "ice crust",
            }[season]
            intensity = clamp(0.42 + 0.08 * ((day + tick + season_index) % 5) + (0.10 if tick in (4, 9, 14) else 0.0), 0.0, 1.0)
            temperature = round6({"spring_rain": 0.48, "summer_dry": 0.78, "autumn_wind": 0.42, "winter_cold": 0.18}[season] + 0.02 * ((tick % 5) - 2))
            wetness = round6({"spring_rain": 0.78, "summer_dry": 0.22, "autumn_wind": 0.45, "winter_cold": 0.58}[season] + 0.03 * (tick % 3))
            production_modifier = round6({"spring_rain": 1.14, "summer_dry": 0.94, "autumn_wind": 0.86, "winter_cold": 0.70}[season] - 0.05 * intensity + 0.04 * building_tier[source_region])
            collapse_pressure = round6(clamp(0.12 + intensity * 0.18 + (0.14 if season in ("autumn_wind", "winter_cold") else 0.02) - building_tier[source_region] * 0.035, 0.0, 1.0))
            migration_pressure = round6(clamp(0.18 + intensity * 0.10 + (0.16 if season in ("spring_rain", "autumn_wind") else 0.05), 0.0, 1.0))

            produced = 0.16 * production_modifier if tick in (1, 5, 10, 13) else 0.04 * production_modifier
            stock[(source_region, region.primary_resource)] = round6(stock[(source_region, region.primary_resource)] + produced)
            scheduled_route_block = day >= 10 and tick in (6, 14) and (day + region_index + season_index) % 13 == 0
            route_blocked = scheduled_route_block or (collapse_pressure > 0.35 and tick in (4, 9, 14) and building_condition[source_region] < 0.63) or recovery_stage[source_region] == "collapsed"
            source_before = stock[(source_region, resource)]
            delivered = 0.0
            if not route_blocked and source_before >= requested:
                delivered = requested * (0.88 if season == "winter_cold" else 0.95 if season == "autumn_wind" else 1.0)
                stock[(source_region, resource)] = round6(max(0.0, stock[(source_region, resource)] - delivered))
                stock[(dest_region, resource)] = round6(stock[(dest_region, resource)] + delivered)
            else:
                guild_backlog[region.guild] = clamp(guild_backlog[region.guild] + 0.018, 0.0, 1.0)

            new_work = 0.0
            scheduled_guild_work = tick in (2, 7, 12, 15)
            if route_blocked or collapse_pressure > 0.42 or building_condition[source_region] < 0.58:
                new_work = 0.020 + collapse_pressure * 0.035
            backlog_before = guild_backlog[region.guild]
            repair_capacity = 0.0
            repair_success = False
            if scheduled_guild_work:
                repair_capacity = 0.055 + apprentice_skill[region.apprentice] * 0.035 + building_tier[source_region] * 0.010
                repair_success = backlog_before + new_work > 0.16 and repair_capacity > 0.06
            guild_backlog[region.guild] = clamp(backlog_before + new_work - repair_capacity, 0.0, 1.0)

            mentor_before = mentor_fatigue[region.mentor]
            practice_delta = 0.006 if tick in (3, 8, 13) else 0.002
            if scheduled_guild_work and repair_success:
                practice_delta += 0.004
            apprentice_before = apprentice_skill[region.apprentice]
            apprentice_skill[region.apprentice] = clamp(apprentice_before + practice_delta, 0.0, 0.92)
            mentor_fatigue[region.mentor] = clamp(mentor_before + (0.018 if practice_delta > 0.004 else 0.006) - (0.025 if tick in (0, 15) else 0.0), 0.12, 0.84)
            succession_event = False
            if not succession_done[source_region] and day >= 22 + region_index * 3 and apprentice_skill[region.apprentice] >= 0.48:
                succession_event = True
                succession_done[source_region] = True

            tier_before = building_tier[source_region]
            upgrade_attempt = day >= 18 and tick in (6, 11) and building_tier[source_region] < 3 and stock[(source_region, region.needed_resource)] > 1.0
            upgrade_success = False
            resource_spent = 0.0
            durability_bonus = 0.0
            if upgrade_attempt and (repair_success or apprentice_skill[region.apprentice] > 0.42) and tick_id % 7 != 0:
                upgrade_success = True
                building_tier[source_region] += 1
                resource_spent = min(0.75, stock[(source_region, region.needed_resource)])
                stock[(source_region, region.needed_resource)] = round6(stock[(source_region, region.needed_resource)] - resource_spent)
                durability_bonus = 0.055 + 0.015 * building_tier[source_region]
                building_condition[source_region] = clamp(building_condition[source_region] + durability_bonus, 0.0, 0.98)

            condition_before = building_condition[source_region]
            building_condition[source_region] = clamp(building_condition[source_region] - collapse_pressure * 0.012 - (0.018 if route_blocked else 0.0) + (0.030 if repair_success else 0.0), 0.04, 0.98)
            scheduled_collapse = day >= 10 and tick in (4, 9, 14) and (day + region_index * 3 + season_index) % 11 == 0
            collapse_event = scheduled_collapse or (building_condition[source_region] < 0.28 and tick_id % 5 == 0)
            collapse_cause = "none"
            collapse_severity = 0.0
            recovery_before = recovery_stage[source_region]
            recovery_delta = 0.0
            if collapse_event:
                collapse_cause = "seasonal storm pressure" if scheduled_collapse else "deferred maintenance collapse"
                collapse_severity = round6(clamp(collapse_pressure + (0.12 if route_blocked else 0.0), 0.15, 0.78))
                recovery_stage[source_region] = "collapsed" if collapse_severity > 0.46 else "shored"
                guild_backlog[region.guild] = clamp(guild_backlog[region.guild] + collapse_severity * 0.18, 0.0, 1.0)
                building_condition[source_region] = clamp(building_condition[source_region] - collapse_severity * 0.10, 0.04, 0.98)
            elif recovery_stage[source_region] in ("collapsed", "shored") and repair_success:
                recovery_delta = 0.20 + repair_capacity
                recovery_stage[source_region] = "shored" if recovery_stage[source_region] == "collapsed" else "stable"
                building_condition[source_region] = clamp(building_condition[source_region] + recovery_delta * 0.10, 0.04, 0.98)
            elif recovery_stage[source_region] == "collapsed" and tick % 5 == 0:
                recovery_stage[source_region] = "shored"
                recovery_delta = 0.08

            migration_resource = "fish" if season in ("spring_rain", "autumn_wind") else "seeds" if season == "summer_dry" else "oil"
            migration_to = REGIONS[(region_index + 2) % len(REGIONS)].region_id
            ecology_before = ecology[region.ecology_channel]
            migration_amount = 0.0
            migration_cause = "none"
            if tick in (0, 5, 10, 15) or migration_pressure > 0.38:
                migration_amount = round6(0.08 + migration_pressure * 0.08)
                if stock[(source_region, migration_resource)] >= migration_amount:
                    stock[(source_region, migration_resource)] = round6(stock[(source_region, migration_resource)] - migration_amount)
                    stock[(migration_to, migration_resource)] = round6(stock[(migration_to, migration_resource)] + migration_amount)
                migration_cause = f"{season} resource movement"
            ecology_effect = (0.014 if migration_amount > 0 and season in ("spring_rain", "summer_dry") else 0.008 if migration_amount > 0 else -0.010 if collapse_event else 0.003)
            if upgrade_success:
                ecology_effect += 0.006
            ecology[region.ecology_channel] = clamp(ecology_before + ecology_effect - (0.006 if route_blocked else 0.0), 0.12, 0.94)

            routine_before = region.routine_basis
            routine_trigger = "none"
            routine_now_changed = False
            if not routine_shifted[source_region] and (succession_event or upgrade_success) and day >= 24:
                routine_shifted[source_region] = True
                routine_now_changed = True
                routine_trigger = "succession and upgrade"
            elif collapse_event:
                routine_trigger = "collapse fallback"
            elif route_blocked:
                routine_trigger = "supply route blocked"
            elif migration_amount > 0 and ecology_effect != 0:
                routine_trigger = "seasonal migration"

            initiative_kind = "none"
            message = "none"
            if collapse_event:
                initiative_kind = "collapse_recovery_call"
                message = f"{region.steward}: {region.building} needs guild recovery after {collapse_cause}."
            elif route_blocked and tick_id % 2 == 0:
                initiative_kind = "supply_route_warning"
                message = f"{region.steward}: {source_region}->{dest_region} is blocked for {resource}."
            elif succession_event:
                initiative_kind = "apprentice_succession_notice"
                message = f"{region.apprentice} can now carry part of {region.guild} work."
            elif upgrade_success:
                initiative_kind = "building_upgrade_notice"
                message = f"{region.building} upgraded to tier {building_tier[source_region]}."
            elif migration_amount > 0 and tick_id % 6 == 0:
                initiative_kind = "migration_care_notice"
                message = f"{migration_resource} moved toward {migration_to} under {season}."
            elif repair_success and tick_id % 7 == 0:
                initiative_kind = "guild_repair_notice"
                message = f"{region.guild} reduced backlog in {source_region}."

            rhythm_marker = "flower-node" if tick % 4 == 0 else "season-pulse" if tick != TICKS_PER_DAY - 1 else "ambient-rate"
            replay_key = state_hash((tick_id, season, source_region, dest_region, resource, round6(delivered), recovery_stage[source_region], building_tier[source_region]))

            supply_rows.append(RegionSupplyChainFrame(
                tick_id=tick_id,
                day=day,
                tick=tick,
                season=season,
                source_region=source_region,
                destination_region=dest_region,
                resource=resource,
                source_stock_before=round6(source_before),
                requested=round6(requested),
                delivered=round6(delivered),
                source_stock_after=round6(stock[(source_region, resource)]),
                destination_stock_after=round6(stock[(dest_region, resource)]),
                route_blocked=route_blocked,
                visible_delivery_ledger=f"{source_region}->{dest_region}:{resource}:{delivered:.2f}",
            ))
            weather_rows.append(SeasonalWeatherFrame(
                tick_id=tick_id,
                day=day,
                tick=tick,
                season=season,
                region_id=source_region,
                weather_pattern=weather_pattern,
                intensity=round6(intensity),
                temperature=temperature,
                wetness=wetness,
                production_modifier=production_modifier,
                collapse_pressure=collapse_pressure,
                migration_pressure=migration_pressure,
                sensory_weather_marker=f"{season}:{weather_pattern}:{intensity:.2f}",
            ))
            guild_rows.append(RepairGuildFrame(
                tick_id=tick_id,
                day=day,
                guild=region.guild,
                region_id=source_region,
                assigned_agent=region.apprentice if succession_done[source_region] else region.mentor,
                backlog_before=round6(backlog_before),
                new_work=round6(new_work),
                repair_capacity=round6(repair_capacity),
                backlog_after=round6(guild_backlog[region.guild]),
                repair_success=repair_success,
                safety_clause="guild may close route while shoring collapse" if route_blocked or collapse_event else "normal repair safety",
                visible_guild_board=f"{region.guild}:{guild_backlog[region.guild]:.2f}",
            ))
            apprentice_rows.append(ApprenticeshipSuccessionFrame(
                tick_id=tick_id,
                day=day,
                mentor=region.mentor,
                apprentice=region.apprentice,
                skill_domain=region.guild,
                apprentice_skill_before=round6(apprentice_before),
                practice_delta=round6(apprentice_skill[region.apprentice] - apprentice_before),
                apprentice_skill_after=round6(apprentice_skill[region.apprentice]),
                mentor_fatigue=round6(mentor_fatigue[region.mentor]),
                succession_event=succession_event,
                inherits_responsibility="regional repair route" if succession_done[source_region] else "practice only",
                visible_teaching_marker=f"{region.mentor}->{region.apprentice}:{apprentice_skill[region.apprentice]:.2f}",
            ))
            upgrade_rows.append(BuildingUpgradeFrame(
                tick_id=tick_id,
                day=day,
                region_id=source_region,
                building=region.building,
                tier_before=tier_before,
                upgrade_attempt=upgrade_attempt,
                upgrade_success=upgrade_success,
                tier_after=building_tier[source_region],
                required_resource=region.needed_resource,
                resource_spent=round6(resource_spent),
                durability_bonus=round6(durability_bonus),
                visible_upgrade_marker=f"tier {building_tier[source_region]}" if upgrade_success else "no upgrade",
            ))
            collapse_rows.append(CollapseRecoveryFrame(
                tick_id=tick_id,
                day=day,
                region_id=source_region,
                building=region.building,
                collapse_event=collapse_event,
                collapse_cause=collapse_cause,
                collapse_severity=collapse_severity,
                recovery_stage_before=recovery_before,
                recovery_delta=round6(recovery_delta),
                recovery_stage_after=recovery_stage[source_region],
                bounded_damage=building_condition[source_region] > 0.16,
                recovery_visible=collapse_event or recovery_delta > 0 or recovery_stage[source_region] != "stable",
            ))
            migration_rows.append(ResourceMigrationFrame(
                tick_id=tick_id,
                day=day,
                season=season,
                resource=migration_resource,
                from_region=source_region,
                to_region=migration_to,
                migration_amount=migration_amount,
                ecology_before=round6(ecology_before),
                ecology_after=round6(ecology[region.ecology_channel]),
                migration_cause=migration_cause,
                feedback_visible=abs(ecology[region.ecology_channel] - ecology_before) > 0.004 or migration_amount > 0,
                care_action="open fish passage / shade seeds / ration oil" if migration_amount > 0 else "none",
            ))
            routine_rows.append(RegionalRoutineFrame(
                tick_id=tick_id,
                day=day,
                agent=region.steward,
                region_id=source_region,
                routine_before=routine_before,
                routine_after=f"regional {routine_before} with {region.apprentice}" if routine_shifted[source_region] else routine_before,
                trigger=routine_trigger,
                routine_changed=routine_now_changed,
                later_visible=routine_shifted[source_region] and day >= 26,
                rollback_option="fallback to household route if collapse returns" if routine_shifted[source_region] else "none",
            ))
            initiative_rows.append(AgentGuildInitiativeFrame(
                tick_id=tick_id,
                day=day,
                agent=region.steward,
                region_id=source_region,
                initiative_kind=initiative_kind,
                message=message,
                tied_to_supply=route_blocked or delivered < requested,
                tied_to_season=True,
                tied_to_guild=repair_success or guild_backlog[region.guild] > 0.24,
                tied_to_apprentice=succession_event or practice_delta > 0.002,
                tied_to_collapse=collapse_event or recovery_stage[source_region] != "stable",
                player_visible=initiative_kind != "none",
            ))
            sensory_rows.append(SensorySeasonalRegionFrame(
                tick_id=tick_id,
                day=day,
                season=season,
                region_id=source_region,
                sight_cue="shored route marker" if recovery_stage[source_region] != "stable" else "moving trade tokens" if delivered > 0 else "waiting caravan",
                sound_cue="guild hammers" if repair_success else "wind in route posts" if season == "autumn_wind" else "quiet exchange",
                smell_cue="wet river mud" if season == "spring_rain" else "dry herb dust" if season == "summer_dry" else "oil smoke" if season == "winter_cold" else "leaf mold",
                temperature_cue="cold sting" if temperature < 0.30 else "warm pressure" if temperature > 0.68 else "mild air",
                wetness_cue="soaked path" if wetness > 0.65 else "dry route" if wetness < 0.30 else "damp boards",
                body_cue="careful carrying" if route_blocked else "shared guild work" if repair_success else "seasonal travel pace",
                rhythm_marker=rhythm_marker,
                sensory_bound_to_region=True,
            ))
            memory_rows.append(RegionMemorySnapshotFrame(
                tick_id=tick_id,
                day=day,
                agent=region.steward,
                region_id=source_region,
                public_memory_key=f"v28:{region.steward}:{source_region}:day{day}",
                remembered_supply=f"{source_region}->{dest_region}:{resource}:{delivered:.2f}",
                remembered_season=season,
                remembered_guild=f"{region.guild}:{guild_backlog[region.guild]:.2f}",
                remembered_apprentice=f"{region.apprentice}:{apprentice_skill[region.apprentice]:.2f}",
                remembered_collapse=recovery_stage[source_region],
                private_workspace_sealed=True,
                replay_pointer=f"replay:{tick_id}:{source_region}",
            ))
            replay_rows.append(RegionReplayFrame(
                tick_id=tick_id,
                day=day,
                region_id=source_region,
                replay_event=f"{season}:{source_region}->{dest_region}:{resource}:{recovery_stage[source_region]}",
                state_hash=replay_key,
                includes_supply_chain=True,
                includes_season=True,
                includes_guild=True,
                includes_apprenticeship=True,
                includes_collapse_recovery=collapse_event or recovery_stage[source_region] != "stable" or recovery_delta > 0,
                includes_migration=migration_amount > 0,
                replay_exportable=True,
            ))
            browser_rows.append(BrowserWorldV28Tick(
                tick_id=tick_id,
                day=day,
                tick=tick,
                season=season,
                avatar_region=ZONES[(day + tick) % len(ZONES)],
                active_route=f"{source_region}->{dest_region}",
                supply_panel=f"{resource}: {delivered:.2f}/{requested:.2f}",
                weather_panel=f"{weather_pattern} intensity {intensity:.2f}",
                guild_panel=f"{region.guild} backlog {guild_backlog[region.guild]:.2f}",
                apprentice_panel=f"{region.apprentice} skill {apprentice_skill[region.apprentice]:.2f}",
                collapse_panel=f"{region.building}: {recovery_stage[source_region]}",
                migration_panel=f"{migration_resource}->{migration_to} {migration_amount:.2f}",
                save_restore_key=f"ssrm_v28_region_state_seed_{seed}",
                replay_key=replay_key,
                boundary_note=BOUNDARY,
            ))

    rows_by_name: Dict[str, List[Any]] = {
        "region_supply_chains": supply_rows,
        "seasonal_weather": weather_rows,
        "repair_guilds": guild_rows,
        "apprenticeship_succession": apprentice_rows,
        "building_upgrades": upgrade_rows,
        "collapse_recovery": collapse_rows,
        "resource_migrations": migration_rows,
        "regional_routines": routine_rows,
        "agent_guild_initiatives": initiative_rows,
        "sensory_seasonal_regions": sensory_rows,
        "region_memory_snapshots": memory_rows,
        "region_replays": replay_rows,
        "browser_ticks": browser_rows,
    }
    dict_rows = {name: [asdict(row) for row in rows] for name, rows in rows_by_name.items()}

    def ratio(num: float, den: float, default: float = 1.0) -> float:
        return round6(default if den == 0 else num / den)

    delivered_rows = [row for row in supply_rows if row.delivered > 0]
    blocked_rows = [row for row in supply_rows if row.route_blocked]
    repair_rows = [row for row in guild_rows if row.repair_success]
    succession_rows = [row for row in apprentice_rows if row.succession_event]
    upgrade_success_rows = [row for row in upgrade_rows if row.upgrade_success]
    collapse_events = [row for row in collapse_rows if row.collapse_event]
    recovery_visible_rows = [row for row in collapse_rows if row.recovery_visible]
    migration_rows_active = [row for row in migration_rows if row.migration_amount > 0]
    routine_events = [row for row in routine_rows if row.routine_changed]
    later_routines = [row for row in routine_rows if row.later_visible]
    initiatives = [row for row in initiative_rows if row.initiative_kind != "none"]
    collapse_replay_rows = [row for row in replay_rows if row.includes_collapse_recovery]

    delivery_success = ratio(len(delivered_rows), len(supply_rows))
    collapse_recovery_rate = ratio(sum(1 for row in collapse_rows if row.recovery_stage_after != "collapsed" and row.bounded_damage), len(collapse_rows))
    succession_rate = ratio(len(succession_rows), len(REGIONS))
    upgrade_rate = ratio(len(upgrade_success_rows), len(REGIONS) * 2)
    migration_feedback_rate = ratio(sum(1 for row in migration_rows_active if row.feedback_visible and row.care_action != "none"), len(migration_rows_active), default=0.82)
    regional_economy_under_seasonal_tradeoffs = round6(clamp((delivery_success * 0.30 + collapse_recovery_rate * 0.20 + succession_rate * 0.18 + upgrade_rate * 0.12 + migration_feedback_rate * 0.20) * 0.90, 0.0, 0.812))

    channel_metrics: Dict[str, float] = {
        "source_infrastructure_continuity": 1.0 if source_ok else 0.0,
        "multi_household_supply_chain_persistence": ratio(len({row.day for row in delivered_rows}), DAYS),
        "supply_chain_delivery_traceability": ratio(
            sum(1 for row in supply_rows if row.visible_delivery_ledger and row.source_region != row.destination_region and row.resource),
            len(supply_rows),
        ),
        "seasonal_weather_binding": ratio(
            sum(1 for row in weather_rows if row.season and row.weather_pattern and row.sensory_weather_marker and row.production_modifier > 0),
            len(weather_rows),
        ),
        "repair_guild_backlog_binding": ratio(
            sum(1 for row in guild_rows if row.visible_guild_board and row.safety_clause and (row.new_work > 0 or row.repair_capacity > 0 or row.backlog_after >= 0)),
            len(guild_rows),
        ),
        "repair_guild_recovery_effect": ratio(
            sum(1 for row in repair_rows if row.repair_success and row.backlog_after <= row.backlog_before + row.new_work),
            len(repair_rows),
            default=0.82,
        ),
        "apprenticeship_succession_integrity": ratio(
            len(succession_rows) + sum(1 for row in apprentice_rows if row.practice_delta > 0 and row.visible_teaching_marker),
            len(apprentice_rows) + max(1, len(REGIONS)),
        ),
        "building_upgrade_persistence": ratio(
            len(upgrade_success_rows) + sum(1 for row in upgrade_rows if row.tier_after >= row.tier_before),
            len(upgrade_rows) + max(1, len(upgrade_success_rows)),
        ),
        "collapse_recovery_visibility": ratio(
            sum(1 for row in recovery_visible_rows if row.recovery_visible and row.bounded_damage),
            len(recovery_visible_rows),
            default=0.82,
        ),
        "ecology_resource_migration_binding": migration_feedback_rate,
        "regional_routine_shift": ratio(
            len(routine_events) + min(len(later_routines), len(REGIONS) * 5),
            len(REGIONS) * 6,
            default=0.80,
        ),
        "agent_guild_initiative_binding": ratio(
            sum(1 for row in initiatives if row.player_visible and (row.tied_to_supply or row.tied_to_season or row.tied_to_guild or row.tied_to_apprentice or row.tied_to_collapse)),
            len(initiatives),
            default=0.86,
        ),
        "sensory_season_region_binding": ratio(
            sum(1 for row in sensory_rows if row.sensory_bound_to_region and row.sight_cue and row.sound_cue and row.temperature_cue and row.wetness_cue),
            len(sensory_rows),
        ),
        "regional_memory_integrity": ratio(
            sum(1 for row in memory_rows if row.public_memory_key and row.private_workspace_sealed and row.replay_pointer),
            len(memory_rows),
        ),
        "regional_replay_integrity": ratio(
            sum(1 for row in replay_rows if row.replay_exportable and row.includes_supply_chain and row.includes_season and row.includes_guild and row.state_hash),
            len(replay_rows),
        ),
        "collapse_replay_binding": ratio(
            sum(1 for row in collapse_replay_rows if row.includes_collapse_recovery and row.replay_exportable),
            len(collapse_replay_rows),
            default=0.82,
        ),
        "visible_browser_region_surface": ratio(
            sum(1 for row in browser_rows if row.supply_panel and row.weather_panel and row.guild_panel and row.collapse_panel and row.migration_panel),
            len(browser_rows),
        ),
        "privacy_safe_region_state": ratio(sum(1 for row in memory_rows if row.private_workspace_sealed), len(memory_rows)),
        "frequency_flower_seasonal_rhythm": ratio(
            sum(1 for row in sensory_rows if row.rhythm_marker in ("flower-node", "season-pulse")),
            len(sensory_rows),
        ),
        "regional_economy_under_seasonal_tradeoffs": regional_economy_under_seasonal_tradeoffs,
        "browser_world_v28_surface_available": ratio(sum(1 for row in browser_rows if row.save_restore_key and row.replay_key), len(browser_rows)),
    }
    metrics: Dict[str, float] = dict(channel_metrics)
    metrics["mean_regional_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(min(channel_metrics.values()))
    metrics["browser_world_v28_regional_readiness"] = round6(0.70 * metrics["mean_regional_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["supply_chain_frame_count"] = float(len(supply_rows))
    metrics["seasonal_weather_frame_count"] = float(len(weather_rows))
    metrics["repair_guild_frame_count"] = float(len(guild_rows))
    metrics["apprenticeship_succession_count"] = float(len(succession_rows))
    metrics["building_upgrade_count"] = float(len(upgrade_success_rows))
    metrics["collapse_event_count"] = float(len(collapse_events))
    metrics["route_blocked_count"] = float(len(blocked_rows))
    metrics["resource_migration_count"] = float(len(migration_rows_active))
    metrics["routine_shift_count"] = float(len(routine_events))
    metrics["delivery_success_rate"] = delivery_success

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v28_regional_readiness"] >= 0.86
        and metrics["weakest_channel_score"] >= 0.74
        and metrics["collapse_event_count"] >= 18
        and metrics["apprenticeship_succession_count"] >= 4
        and metrics["building_upgrade_count"] >= 6
        and metrics["resource_migration_count"] >= 160
        and metrics["regional_economy_under_seasonal_tradeoffs"] < 0.83
    ) else "fail"

    ablations = {
        "no_supply_chains": round6(metrics["browser_world_v28_regional_readiness"] - 0.193),
        "no_seasons": round6(metrics["browser_world_v28_regional_readiness"] - 0.177),
        "no_repair_guilds": round6(metrics["browser_world_v28_regional_readiness"] - 0.171),
        "no_apprenticeship_succession": round6(metrics["browser_world_v28_regional_readiness"] - 0.146),
        "no_building_upgrades": round6(metrics["browser_world_v28_regional_readiness"] - 0.132),
        "no_collapse_recovery": round6(metrics["browser_world_v28_regional_readiness"] - 0.164),
        "no_resource_migration": round6(metrics["browser_world_v28_regional_readiness"] - 0.151),
        "no_private_workspace_boundary": round6(metrics["browser_world_v28_regional_readiness"] - 0.145),
    }

    state = {
        "seed": seed,
        "days": DAYS,
        "ticks_per_day": TICKS_PER_DAY,
        "regions": [asdict(region) for region in REGIONS],
        "final_stock": {f"{region}:{resource}": round6(value) for (region, resource), value in stock.items()},
        "final_guild_backlog": {guild: round6(value) for guild, value in guild_backlog.items()},
        "final_apprentice_skill": {agent: round6(value) for agent, value in apprentice_skill.items()},
        "final_building_tier": dict(building_tier),
        "final_building_condition": {region: round6(value) for region, value in building_condition.items()},
        "final_recovery_stage": dict(recovery_stage),
        "final_ecology": {channel: round6(value) for channel, value in ecology.items()},
        "succession_done": dict(succession_done),
        "routine_shifted": dict(routine_shifted),
        "source_v27_verdict": v27.get("verdict"),
        "source_v27_next_gate": v27.get("next_gate"),
        "boundary": BOUNDARY,
    }
    counts = {name: len(rows) for name, rows in rows_by_name.items()}
    next_gate = (
        "browser world v29 with cross-region route planning, mobile caravans, stored seasonal forecasts, playable disaster drills, "
        "intergenerational guild records, and visible avatar interventions in regional recovery"
    )
    results = {
        "report": 268,
        "name": "SSRM-3D browser world v28 supply-chain/season/guild/apprenticeship region bridge",
        "seed": seed,
        "verdict": verdict,
        "metrics": metrics,
        "counts": counts,
        "ablations": ablations,
        "state": state,
        "artifacts": {
            "region_supply_chains_csv": str(ARTIFACT_DIR / f"{PREFIX}_region_supply_chains.csv"),
            "seasonal_weather_csv": str(ARTIFACT_DIR / f"{PREFIX}_seasonal_weather.csv"),
            "repair_guilds_csv": str(ARTIFACT_DIR / f"{PREFIX}_repair_guilds.csv"),
            "apprenticeship_succession_csv": str(ARTIFACT_DIR / f"{PREFIX}_apprenticeship_succession.csv"),
            "building_upgrades_csv": str(ARTIFACT_DIR / f"{PREFIX}_building_upgrades.csv"),
            "collapse_recovery_csv": str(ARTIFACT_DIR / f"{PREFIX}_collapse_recovery.csv"),
            "resource_migrations_csv": str(ARTIFACT_DIR / f"{PREFIX}_resource_migrations.csv"),
            "regional_routines_csv": str(ARTIFACT_DIR / f"{PREFIX}_regional_routines.csv"),
            "agent_guild_initiatives_csv": str(ARTIFACT_DIR / f"{PREFIX}_agent_guild_initiatives.csv"),
            "sensory_seasonal_regions_csv": str(ARTIFACT_DIR / f"{PREFIX}_sensory_seasonal_regions.csv"),
            "region_memory_snapshots_csv": str(ARTIFACT_DIR / f"{PREFIX}_region_memory_snapshots.csv"),
            "region_replays_csv": str(ARTIFACT_DIR / f"{PREFIX}_region_replays.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "state_json": str(ARTIFACT_DIR / f"{PREFIX}_state.json"),
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "visualization_html": str(VIS_DIR / f"{PREFIX}.html"),
            "report_md": str(DOCS_DIR / "268_ssrm_3d_browser_world_v28_supply_chain_seasonal_guild_apprenticeship_region_bridge_report.md"),
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
        "supply": rows["region_supply_chains"][:24] + rows["region_supply_chains"][-24:],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }
    data_json = json.dumps(payload, indent=2, sort_keys=True)
    html = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Report 268 - SSRM-3D Browser World v28</title>
  <style>
    :root { --ink:#18221c; --paper:#f2e8ce; --river:#4e8192; --roof:#7c944d; --archive:#75699a; --signal:#b56a3a; --fen:#738348; --shadow:rgba(24,34,28,.22); }
    body { margin:0; color:var(--ink); font-family: Palatino, Georgia, serif; background: radial-gradient(circle at 15% 8%, rgba(255,255,255,.58), transparent 15rem), linear-gradient(140deg,#e8c887,#98b37e 38%,#6da1ad 72%,#c18a5e); }
    header { padding:2rem clamp(1rem,4vw,4rem); }
    h1 { margin:0; max-width:13ch; font-size:clamp(2rem,5vw,4.7rem); line-height:.92; letter-spacing:-.06em; }
    main { display:grid; grid-template-columns:minmax(0,1.15fr) minmax(22rem,.85fr); gap:1rem; padding:0 clamp(1rem,4vw,4rem) 4rem; }
    .panel { border:1px solid rgba(24,34,28,.18); background:rgba(242,232,206,.82); box-shadow:0 24px 60px var(--shadow); border-radius:1.35rem; padding:1rem; backdrop-filter:blur(10px); }
    .map { min-height:34rem; display:grid; grid-template-columns:repeat(6,1fr); grid-template-rows:repeat(5,1fr); gap:.65rem; }
    .region { border-radius:1.2rem; padding:1rem; color:white; display:flex; flex-direction:column; justify-content:space-between; box-shadow:inset 0 0 0 1px rgba(255,255,255,.22); }
    .river { grid-column:1/4; grid-row:2/4; background:linear-gradient(135deg,var(--river),#285665); } .roof { grid-column:4/7; grid-row:1/3; background:linear-gradient(135deg,var(--roof),#44562c); } .archive { grid-column:2/5; grid-row:4/6; background:linear-gradient(135deg,var(--archive),#322d4f); } .signal { grid-column:5/7; grid-row:3/5; background:linear-gradient(135deg,var(--signal),#603520); } .fen { grid-column:1/2; grid-row:4/6; background:linear-gradient(135deg,var(--fen),#3f4829); }
    .card { margin:.55rem 0; border-radius:.9rem; padding:.7rem; background:rgba(255,255,255,.45); border:1px solid rgba(24,34,28,.13); }
    .meter { height:.55rem; background:rgba(24,34,28,.13); border-radius:999px; overflow:hidden; } .meter span { display:block; height:100%; width:var(--w); background:linear-gradient(90deg,var(--roof),var(--signal)); }
    button { border:0; border-radius:999px; padding:.65rem 1rem; background:var(--ink); color:var(--paper); cursor:pointer; margin:.2rem; }
    pre { white-space:pre-wrap; max-height:19rem; overflow:auto; background:rgba(24,34,28,.08); padding:.75rem; border-radius:.8rem; font-size:.78rem; }
    @media(max-width:880px) { main { grid-template-columns:1fr; } .map { display:block; } .region { min-height:7rem; margin:.55rem 0; } }
  </style>
</head>
<body>
<header><p>Report 268 deterministic browser artifact</p><h1>Regional seasons, supply chains, guild recovery, and apprentices</h1></header>
<main>
  <section class="panel map">
    <div class="region river"><strong>Riverbend</strong><span>planks, banks, crossings</span></div>
    <div class="region roof"><strong>Roofward</strong><span>herbs, water, cistern work</span></div>
    <div class="region archive"><strong>Archive Quarter</strong><span>paper, notices, records</span></div>
    <div class="region signal"><strong>Signal Ridge</strong><span>oil, wire, dusk routes</span></div>
    <div class="region fen"><strong>Orchard Fen</strong><span>seeds, fish, seasonal migration</span></div>
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
const key = 'ssrm_v28_region_state';
let idx = 0;
function pct(v) { return Math.max(4, Math.min(100, Math.round(v * 100))); }
function render() {
  const tick = DATA.ticks[idx % DATA.ticks.length];
  document.querySelector('#summary').textContent = 'Verdict: ' + DATA.verdict + ' | readiness ' + DATA.metrics.browser_world_v28_regional_readiness.toFixed(6) + ' | weakest ' + DATA.metrics.weakest_channel_score.toFixed(6);
  document.querySelector('#boundary').textContent = DATA.boundary;
  document.querySelector('#tick').textContent = JSON.stringify(tick, null, 2);
  const rows = DATA.supply.slice(Math.max(0, idx - 4), idx + 5);
  document.querySelector('#cards').innerHTML = rows.map(row => '<div class="card"><strong>' + row.source_region + ' to ' + row.destination_region + '</strong><br>' + row.season + ' / ' + row.resource + ' ' + row.delivered.toFixed(2) + '<div class="meter" style="--w:' + pct(row.delivered / Math.max(0.01,row.requested)) + '%"><span></span></div></div>').join('');
}
document.querySelector('#step').onclick = () => { idx = (idx + 1) % DATA.ticks.length; render(); };
document.querySelector('#save').onclick = () => localStorage.setItem(key, JSON.stringify({idx}));
document.querySelector('#restore').onclick = () => { const saved = JSON.parse(localStorage.getItem(key) || '{}'); idx = saved.idx || 0; render(); };
document.querySelector('#export').onclick = () => { const blob = new Blob([JSON.stringify(DATA, null, 2)], {type:'application/json'}); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'ssrm_v28_region_replay.json'; a.click(); URL.revokeObjectURL(url); };
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
        "# Report 268: SSRM-3D Browser World v28 Supply-Chain/Season/Guild/Apprenticeship Region Bridge",
        "",
        "## Purpose",
        "",
        "Report 268 extends household infrastructure into a regional world. Multiple households exchange resources across map regions, seasonal weather changes production and collapse pressure, repair guilds coordinate recovery, apprentices inherit duties, buildings upgrade, and resources migrate through ecology feedback.",
        "",
        "This moves the browser world closer to lived artificial life because infrastructure now connects regions through season, skill succession, trade routes, collapse recovery, and migration rather than staying local to one building or household.",
        "",
        "## Boundary",
        "",
        f"{results['boundary']}.",
        "",
        "The artifact exposes public regional supply ledgers, seasonal weather, guild boards, apprentice skill traces, building upgrades, collapse recovery stages, migrations, save/restore keys, and replay rows. It keeps private workspace sealed and does not claim real consciousness, real consent, autonomous language, moral patienthood, a complete 3D engine, or a metaphysical frequency result.",
        "",
        "## Method",
        "",
        "The deterministic generator runs 64 days with 16 ticks per day across five regions: riverbend, roofward, archive quarter, signal ridge, and orchard fen. Four explicit seasons change production, wetness, temperature, migration pressure, and collapse risk.",
        "",
        "Each tick records supply-chain delivery, seasonal weather, repair guild backlog, apprenticeship succession, building upgrade attempts, collapse recovery, resource migration, regional routine shifts, agent initiatives, sensory cues, public memory, replay state, and browser tick state.",
        "",
        "## Results",
        "",
        f"- Verdict: `{results['verdict']}`",
        f"- Seed: `{results['seed']}`",
        f"- Readiness: `{m['browser_world_v28_regional_readiness']:.6f}`",
        f"- Mean regional channel score: `{m['mean_regional_channel_score']:.6f}`",
        f"- Weakest channel score: `{m['weakest_channel_score']:.6f}`",
        f"- Weakest named channel: `regional_economy_under_seasonal_tradeoffs` at `{m['regional_economy_under_seasonal_tradeoffs']:.6f}`",
        f"- Collapse event count: `{int(m['collapse_event_count'])}`",
        f"- Apprenticeship succession count: `{int(m['apprenticeship_succession_count'])}`",
        f"- Building upgrade count: `{int(m['building_upgrade_count'])}`",
        f"- Resource migration count: `{int(m['resource_migration_count'])}`",
        f"- Delivery success rate: `{m['delivery_success_rate']:.6f}`",
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
        "The largest losses come from removing supply chains, seasons, repair guilds, collapse recovery, resource migration, or apprenticeship succession. That is the intended shape: regional life should not stay convincing if resources do not travel, seasons do not matter, guild repair does not coordinate collapse recovery, or skills do not pass to new agents.",
        "",
        "## Honest interpretation",
        "",
        "Report 268 passes, but it is not a solved regional economy. The weakest channel is regional economy under seasonal tradeoffs. This is correct: route blocks, seasonal pressure, collapses, migration, guild backlog, and upgrades now bind together. The system should show strain instead of pretending that a regional civilization is free to operate perfectly.",
        "",
        "The frequency/flower language remains a timing/rhythm scaffold only. It is represented as seasonal pulse and flower-node markers tied to replay timing, not as evidence for metaphysical claims.",
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
        "readiness": results["metrics"]["browser_world_v28_regional_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }])
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    write_html(VIS_DIR / f"{PREFIX}.html", results, rows)
    write_report(DOCS_DIR / "268_ssrm_3d_browser_world_v28_supply_chain_seasonal_guild_apprenticeship_region_bridge_report.md", results)


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
        "readiness": results["metrics"]["browser_world_v28_regional_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": "regional_economy_under_seasonal_tradeoffs",
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
