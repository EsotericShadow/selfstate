"""Environment-readiness maturation verifier for SSRM-3D.

This report-grade verifier moves the live open-emergence sandbox readiness
variables into a headless, multi-seed benchmark. It remains a designed
simulation, not deep RL or open-ended civilization, but it makes the 12h
development window stricter: agents must build slow preparation state before
post-gate shocks test the world.
"""

from __future__ import annotations

import argparse
import json
import math
import random
from dataclasses import asdict, dataclass, field
from pathlib import Path
from statistics import mean
from typing import Dict, Iterable, List, Sequence, Tuple

from ssrm_maturation.artifacts import rows_to_csv, write_js, write_json


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
TRACE_CHECKPOINTS = (0.0, 3.0, 6.0, 9.0, 12.0, 18.0, 24.0, 36.0, 48.0, 60.0, 72.0)


@dataclass(frozen=True)
class Config:
    seeds: Sequence[int]
    hours: float = 72.0
    step_hours: float = 0.10
    population: int = 14
    trace_seed: int = 20261201


@dataclass(frozen=True)
class Condition:
    name: str
    description: str
    planning: bool = True
    seed_bank: bool = True
    blueprints: bool = True
    forecast: bool = True
    apprenticeship: bool = True
    pest_control: bool = True
    strain_repair: bool = True
    reproduction: bool = True


CONDITIONS = (
    Condition("integrated_readiness", "full readiness world with slow preparation and post-gate shocks"),
    Condition(
        "reactive_immediate_needs",
        "reactive food/water/rest/treat controller without persistent preparation channels",
        planning=False,
        seed_bank=False,
        blueprints=False,
        forecast=False,
        apprenticeship=False,
        pest_control=False,
        strain_repair=False,
        reproduction=False,
    ),
    Condition("no_seed_bank", "seed storage and crop recovery memory removed", seed_bank=False),
    Condition("no_blueprints", "building and tool blueprint memory removed", blueprints=False),
    Condition("no_forecast_memory", "weather/route forecast memory removed", forecast=False),
    Condition("no_apprenticeship", "skill transmission and apprenticeship removed", apprenticeship=False),
    Condition("no_pest_control", "active pest pressure control removed", pest_control=False),
    Condition("no_structural_repair", "structural strain repair removed", strain_repair=False),
)


@dataclass
class Agent:
    ident: str
    generation: int
    age_hours: float
    max_life_hours: float
    resilience: float
    dexterity: float
    sociability: float
    curiosity: float
    health: float
    energy: float
    hunger: float
    thirst: float
    stress: float
    illness: float
    injury: float
    wisdom: float
    build_skill: float
    tool_skill: float
    harvest_skill: float
    scout_skill: float
    care_skill: float
    teach_skill: float
    alive: bool = True
    child: bool = False
    action: str = "idle"


@dataclass
class World:
    time: float = 0.0
    food: float = 0.82
    water: float = 0.82
    materials: float = 0.58
    medicine: float = 0.36
    shelter: float = 0.48
    architecture: float = 0.14
    tools: float = 0.34
    workshop: float = 0.14
    waterworks: float = 0.14
    granary: float = 0.14
    paths: float = 0.12
    garden: float = 0.24
    sanitation: float = 0.13
    fire_control: float = 0.12
    culture: float = 0.07
    symbols: float = 0.06
    social_trust: float = 0.50
    conflict: float = 0.10
    risk_memory: float = 0.08
    map_knowledge: float = 0.12
    terrain_knowledge: float = 0.10
    fuel_reserve: float = 0.30
    seed_bank: float = 0.16
    building_blueprints: float = 0.10
    tool_blueprints: float = 0.08
    forecast_memory: float = 0.10
    apprenticeship: float = 0.08
    pest_pressure: float = 0.08
    structural_strain: float = 0.14
    soil: float = 0.64
    contamination: float = 0.14
    disease: float = 0.10
    temperature: float = 0.55
    rainfall: float = 0.18
    wind: float = 0.16
    visibility: float = 0.78
    route_hazard: float = 0.16
    resource_migration: float = 0.12
    resource_depletion: float = 0.08
    weather: str = "clear"
    adaptive_pressure: float = 0.12
    pressure_integral: float = 0.0
    adaptation_evidence: float = 0.0
    major_shocks: int = 0
    next_shock: float = 12.75
    first_shock_hour: float = 0.0
    births: int = 0
    deaths: int = 0
    knowledge_transfer: float = 0.0


@dataclass(frozen=True)
class EpisodeRow:
    seed: int
    condition: str
    final_alive: int
    total_agents: int
    alive_at_12h: int
    no_major_shock_before_12h: bool
    post_gate_shock: bool
    major_shocks: int
    first_shock_hour: float
    births: int
    deaths: int
    readiness_at_12h: float
    final_readiness: float
    readiness_delta: float
    final_pest_pressure: float
    final_structural_strain: float
    final_fuel_reserve: float
    final_seed_bank: float
    final_building_blueprints: float
    final_tool_blueprints: float
    final_forecast_memory: float
    final_apprenticeship: float
    architecture_delta: float
    tool_system_delta: float
    knowledge_transfer: float
    adaptation_evidence: float
    pressure_integral: float
    survival_score: float
    readiness_score: float
    development_score: float
    knowledge_score: float
    resilience_score: float
    maturation_score: float


@dataclass(frozen=True)
class SummaryRow:
    condition: str
    mean_maturation_score: float
    mean_survival_score: float
    mean_readiness_score: float
    mean_development_score: float
    mean_knowledge_score: float
    mean_resilience_score: float
    mean_final_alive: float
    mean_alive_at_12h: float
    mean_births: float
    mean_deaths: float
    mean_readiness_at_12h: float
    mean_final_readiness: float
    mean_readiness_delta: float
    mean_final_fuel_reserve: float
    mean_final_seed_bank: float
    mean_final_building_blueprints: float
    mean_final_tool_blueprints: float
    mean_final_forecast_memory: float
    mean_final_apprenticeship: float
    mean_final_pest_pressure: float
    mean_final_structural_strain: float
    mean_architecture_delta: float
    mean_tool_system_delta: float
    mean_knowledge_transfer: float
    mean_adaptation_evidence: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float


@dataclass(frozen=True)
class VerdictRow:
    integrated_score: float
    reactive_score: float
    no_seed_score: float
    no_blueprint_score: float
    no_forecast_score: float
    no_apprenticeship_score: float
    no_pest_control_score: float
    no_structural_repair_score: float
    reactive_loss: float
    seed_bank_loss: float
    blueprint_loss: float
    forecast_loss: float
    apprenticeship_loss: float
    pest_control_loss: float
    structural_repair_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    readiness_at_12h: float
    final_readiness: float
    final_pest_pressure: float
    final_structural_strain: float
    supports_12h_development_window: bool
    supports_environment_readiness: bool
    supports_ablation_specificity: bool
    verdict: str


TraceFrame = Dict[str, object]


@dataclass
class Trace:
    seed: int
    condition: str
    frames: List[TraceFrame] = field(default_factory=list)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def safe_mean(values: Iterable[float]) -> float:
    values = list(values)
    return mean(values) if values else 0.0


def living(agents: Iterable[Agent]) -> List[Agent]:
    return [agent for agent in agents if agent.alive]


def tool_system(world: World) -> float:
    return world.tools + world.workshop * 0.38 + world.fire_control * 0.24 + world.tool_blueprints * 0.18


def environment_readiness(world: World) -> float:
    return clamp(
        (
            world.fuel_reserve
            + world.seed_bank
            + world.building_blueprints
            + world.tool_blueprints
            + world.forecast_memory
            + world.apprenticeship
        )
        / 6.0
    )


def make_agents(rng: random.Random, population: int) -> List[Agent]:
    agents: List[Agent] = []
    for index in range(population):
        resilience = 0.34 + rng.random() * 0.50
        dexterity = 0.34 + rng.random() * 0.48
        sociability = 0.30 + rng.random() * 0.52
        curiosity = 0.30 + rng.random() * 0.52
        agents.append(
            Agent(
                ident=f"A{index + 1:02d}",
                generation=0,
                age_hours=18.0 + rng.random() * 26.0,
                max_life_hours=108.0 + resilience * 58.0 + rng.random() * 20.0,
                resilience=resilience,
                dexterity=dexterity,
                sociability=sociability,
                curiosity=curiosity,
                health=0.86 + rng.random() * 0.10,
                energy=0.70 + rng.random() * 0.16,
                hunger=0.20 + rng.random() * 0.12,
                thirst=0.20 + rng.random() * 0.12,
                stress=0.12 + rng.random() * 0.12,
                illness=0.04 + rng.random() * 0.06,
                injury=0.02 + rng.random() * 0.05,
                wisdom=0.06 + rng.random() * 0.12,
                build_skill=0.08 + resilience * 0.12 + rng.random() * 0.08,
                tool_skill=0.08 + dexterity * 0.13 + rng.random() * 0.08,
                harvest_skill=0.10 + dexterity * 0.10 + rng.random() * 0.08,
                scout_skill=0.08 + curiosity * 0.13 + rng.random() * 0.08,
                care_skill=0.08 + sociability * 0.11 + rng.random() * 0.08,
                teach_skill=0.07 + sociability * 0.13 + rng.random() * 0.08,
            )
        )
    return agents


def make_world(rng: random.Random) -> World:
    world = World()
    world.food = clamp(world.food + rng.uniform(-0.03, 0.03))
    world.water = clamp(world.water + rng.uniform(-0.03, 0.03))
    world.materials = clamp(world.materials + rng.uniform(-0.04, 0.04))
    world.shelter = clamp(world.shelter + rng.uniform(-0.03, 0.03))
    world.next_shock = 12.75 + rng.random() * 4.0
    return world


def pressure_components(world: World, agents: List[Agent]) -> Dict[str, float]:
    alive = living(agents)
    body_reserve = safe_mean(
        agent.health * 0.42 + agent.energy * 0.24 + (1.0 - agent.hunger) * 0.17 + (1.0 - agent.thirst) * 0.17
        for agent in alive
    )
    survival = clamp(
        max(0.0, 0.48 - world.food) * 0.32
        + max(0.0, 0.48 - world.water) * 0.34
        + world.disease * 0.18
        + world.pest_pressure * 0.16
        + max(0.0, 0.42 - world.fuel_reserve) * 0.14
        + max(0.0, 0.58 - body_reserve) * 0.28
    )
    ecology = clamp(
        world.resource_migration * 0.22
        + world.resource_depletion * 0.16
        + world.route_hazard * 0.20
        + abs(world.temperature - 0.55) * 0.20
        + max(0.0, 0.56 - world.visibility) * 0.14
        + world.pest_pressure * 0.16
        + max(0.0, 0.42 - world.forecast_memory) * 0.16
    )
    infrastructure = clamp(
        max(0.0, 0.60 - world.shelter) * 0.18
        + max(0.0, 0.56 - world.architecture) * 0.18
        + max(0.0, 0.52 - world.tools) * 0.14
        + max(0.0, 0.48 - world.granary) * 0.10
        + world.structural_strain * 0.22
        + max(0.0, 0.42 - world.building_blueprints) * 0.12
        + max(0.0, 0.38 - world.tool_blueprints) * 0.10
    )
    dependents = sum(1 for agent in alive if agent.child)
    social = clamp(
        world.conflict * 0.28
        + max(0.0, 0.54 - world.social_trust) * 0.18
        + max(0.0, 0.46 - world.culture) * 0.16
        + dependents / max(1, len(alive)) * 0.16
        + max(0.0, 0.40 - world.apprenticeship) * 0.12
    )
    uncertainty = clamp(
        world.resource_migration * 0.16
        + max(0.0, 0.58 - world.map_knowledge) * 0.20
        + max(0.0, 0.52 - world.risk_memory) * 0.17
        + max(0.0, 0.50 - world.symbols) * 0.10
        + max(0.0, 0.46 - world.forecast_memory) * 0.18
        + max(0.0, 0.40 - world.apprenticeship) * 0.10
    )
    total = clamp(survival * 0.23 + ecology * 0.20 + infrastructure * 0.23 + social * 0.16 + uncertainty * 0.18)
    return {
        "survival": survival,
        "ecology": ecology,
        "infrastructure": infrastructure,
        "social": social,
        "uncertainty": uncertainty,
        "total": total,
    }


def condition_scalar(condition: Condition, name: str) -> float:
    return 1.0 if getattr(condition, name) else 0.0


def update_environment(world: World, agents: List[Agent], condition: Condition, dt: float, rng: random.Random) -> None:
    alive = living(agents)
    day_phase = (world.time % 24.0) / 24.0
    daylight = max(0.0, math.sin(day_phase * math.pi))
    season = math.sin(world.time / 72.0 * math.pi * 2.0 + 0.4)
    storm = rng.random() < (0.009 + world.wind * 0.009 + world.contamination * 0.004) * dt
    heat = max(0.0, season) * 0.22
    cold = max(0.0, -season) * 0.18
    world.weather = "storm" if storm else ("hot" if heat > 0.16 else ("cold" if cold > 0.13 else "clear"))
    world.rainfall = clamp(0.14 + max(0.0, -season) * 0.18 + (0.34 if storm else 0.0) - heat * 0.20)
    world.wind = clamp(0.12 + abs(season) * 0.18 + (0.34 if storm else 0.0))
    world.temperature = clamp(0.54 + heat - cold + daylight * 0.10 - world.rainfall * 0.08)
    world.visibility = clamp(0.30 + daylight * 0.54 - world.rainfall * 0.20 - world.wind * 0.10 + world.paths * 0.12 + world.forecast_memory * 0.04)

    forecast = condition_scalar(condition, "forecast")
    seed_bank = condition_scalar(condition, "seed_bank")
    blueprints = condition_scalar(condition, "blueprints")
    apprenticeship = condition_scalar(condition, "apprenticeship")
    pest_control = condition_scalar(condition, "pest_control")
    strain_repair = condition_scalar(condition, "strain_repair")

    clean = safe_mean(max(0.0, 1.0 - agent.stress) for agent in alive)
    cold_stress = max(0.0, 0.46 - world.temperature)
    heat_stress = max(0.0, world.temperature - 0.70)
    movement = math.sin(world.time / 13.0 * math.pi * 2.0 + 1.1)

    world.pest_pressure = clamp(
        world.pest_pressure
        + (
            world.garden * 0.010
            + world.granary * 0.010
            + world.rainfall * 0.017
            + heat_stress * 0.040
            + world.contamination * 0.016
            + world.disease * 0.008
        )
        * dt
        - (world.seed_bank * seed_bank + world.sanitation + world.culture + clean) * 0.022 * pest_control * dt
    )
    world.structural_strain = clamp(
        world.structural_strain
        + (world.wind * 0.014 + world.rainfall * 0.010 + len(alive) * 0.0012 + world.shelter * 0.003) * dt
        - (world.architecture + world.building_blueprints * blueprints + world.materials) * 0.019 * strain_repair * dt
    )
    world.fuel_reserve = clamp(
        world.fuel_reserve
        - (cold_stress * 0.030 + (0.014 if storm else 0.0) + len(alive) * 0.0012) * dt
        + (world.paths + world.map_knowledge + world.workshop) * 0.006 * dt
    )
    world.seed_bank = clamp(
        world.seed_bank
        + (world.garden + world.culture + world.apprenticeship * apprenticeship) * 0.006 * seed_bank * dt
        - (world.pest_pressure + abs(movement) * 0.08 + world.contamination) * 0.008 * dt
    )
    world.forecast_memory = clamp(
        world.forecast_memory
        + (world.map_knowledge + world.risk_memory + world.symbols) * 0.006 * forecast * dt
        - (world.resource_migration + world.disease + (0.10 if storm else 0.0)) * 0.006 * dt
    )
    world.building_blueprints = clamp(
        world.building_blueprints
        + (world.architecture + world.culture + world.apprenticeship) * 0.005 * blueprints * dt
        - world.resource_migration * 0.004 * dt
    )
    world.tool_blueprints = clamp(
        world.tool_blueprints
        + (world.workshop + world.tools + world.apprenticeship) * 0.005 * blueprints * dt
        - world.resource_migration * 0.004 * dt
    )
    world.apprenticeship = clamp(
        world.apprenticeship
        + (world.culture + world.social_trust + world.knowledge_transfer) * 0.004 * apprenticeship * dt
        - (world.conflict + world.disease) * 0.005 * dt
    )

    world.resource_migration = clamp(
        0.10
        + abs(movement) * 0.34
        + world.pest_pressure * 0.06
        + world.resource_depletion * 0.08
        - world.paths * 0.09
        - world.map_knowledge * 0.07
        - world.forecast_memory * 0.06 * forecast
    )
    water_reliability = clamp(0.46 + world.rainfall * 0.22 + world.waterworks * 0.24 + world.forecast_memory * 0.04 * forecast - world.contamination * 0.18 - heat * 0.10)
    food_reliability = clamp(0.48 + world.soil * 0.18 + world.garden * 0.16 + world.seed_bank * 0.12 * seed_bank - world.pest_pressure * 0.16 - world.resource_migration * 0.12 - world.resource_depletion * 0.10)
    material_reliability = clamp(0.50 + world.paths * 0.11 + world.map_knowledge * 0.12 + world.tool_blueprints * 0.06 * blueprints - world.route_hazard * 0.12)

    world.soil = clamp(world.soil + (world.rainfall - 0.16) * 0.010 * dt + world.garden * 0.006 * dt + world.seed_bank * 0.006 * seed_bank * dt - world.resource_depletion * 0.010 * dt - world.pest_pressure * 0.010 * dt)
    world.contamination = clamp(world.contamination + (world.rainfall * 0.018 + world.disease * 0.014 + world.pest_pressure * 0.012 + len(alive) * (1.0 - clean) * 0.0014) * dt - (world.sanitation + world.waterworks) * 0.036 * dt)
    world.disease = clamp(world.disease + (world.contamination * 0.024 + world.pest_pressure * 0.012 + max(0.0, 0.44 - world.shelter) * 0.016) * dt - (world.medicine + world.sanitation + world.culture) * 0.030 * dt)
    world.route_hazard = clamp(0.10 + world.wind * 0.14 + world.resource_migration * 0.12 + world.structural_strain * 0.05 - world.paths * 0.16 - world.terrain_knowledge * 0.10 - world.forecast_memory * 0.06 * forecast)

    count = len(alive)
    world.resource_depletion = clamp(world.resource_depletion + count * 0.0008 * dt - world.garden * 0.006 * dt - world.seed_bank * 0.003 * seed_bank * dt)
    world.food = clamp(world.food - count * 0.0025 * dt + world.garden * food_reliability * 0.084 * dt + world.granary * 0.026 * dt + world.seed_bank * 0.014 * seed_bank * dt - world.pest_pressure * 0.010 * dt)
    world.water = clamp(world.water - count * 0.0028 * dt + world.waterworks * water_reliability * 0.082 * dt + world.rainfall * 0.016 * dt - world.contamination * 0.007 * dt)
    world.materials = clamp(world.materials + (world.paths + world.map_knowledge + material_reliability) * 0.009 * dt - max(0, count - 4) * 0.0012 * dt)
    world.tools = clamp(world.tools - count * max(0.0008, 0.0017 - world.workshop * 0.0009 - world.tool_blueprints * 0.0005 * blueprints) * dt)
    world.shelter = clamp(world.shelter - max(0.002, 0.004 + world.wind * 0.008 + world.rainfall * 0.006 + world.structural_strain * 0.007 - world.architecture * 0.008 - world.building_blueprints * 0.004 * blueprints) * dt)
    world.architecture = clamp(world.architecture - max(0.0008, world.wind * 0.003 + world.structural_strain * 0.005 - world.building_blueprints * 0.003 * blueprints) * dt)
    world.granary = clamp(world.granary - (world.contamination * 0.003 + world.pest_pressure * 0.004) * dt)
    world.risk_memory = clamp(world.risk_memory * (1.0 - 0.003 * dt) + world.major_shocks * 0.0008 * dt + world.route_hazard * 0.003 * dt)
    world.map_knowledge = clamp(world.map_knowledge * (1.0 - (0.006 + world.resource_migration * 0.004) * dt) + world.terrain_knowledge * 0.004 * dt + world.forecast_memory * 0.0015 * dt)

    if not condition.seed_bank:
        world.seed_bank = 0.0
    if not condition.blueprints:
        world.building_blueprints = 0.0
        world.tool_blueprints = 0.0
    if not condition.forecast:
        world.forecast_memory = 0.0
    if not condition.apprenticeship:
        world.apprenticeship = 0.0


def maybe_major_shock(world: World, condition: Condition, rng: random.Random) -> str | None:
    if world.time < 12.0 or world.time < world.next_shock:
        return None
    shock = rng.choice(("drought", "blight", "epidemic", "structural_failure", "resource_shift", "wind_damage"))
    world.major_shocks += 1
    if world.first_shock_hour <= 0.0:
        world.first_shock_hour = world.time
    seed_mitigation = world.seed_bank * 0.18 if condition.seed_bank else 0.0
    forecast_mitigation = world.forecast_memory * 0.18 if condition.forecast else 0.0
    blueprint_mitigation = world.building_blueprints * 0.16 if condition.blueprints else 0.0
    if shock == "drought":
        world.water = clamp(world.water - max(0.08, 0.20 - forecast_mitigation * 0.35))
        world.soil = clamp(world.soil - max(0.05, 0.15 - seed_mitigation * 0.28))
        world.temperature = clamp(world.temperature + 0.12)
        world.fuel_reserve = clamp(world.fuel_reserve - 0.05)
    elif shock == "blight":
        world.food = clamp(world.food - max(0.07, 0.20 - seed_mitigation * 0.42))
        world.garden = clamp(world.garden - max(0.03, 0.12 - seed_mitigation * 0.25))
        world.pest_pressure = clamp(world.pest_pressure + 0.16)
    elif shock == "epidemic":
        world.disease = clamp(world.disease + 0.20)
        world.contamination = clamp(world.contamination + 0.10)
        world.social_trust = clamp(world.social_trust - 0.05)
    elif shock == "structural_failure":
        world.shelter = clamp(world.shelter - max(0.05, 0.14 - blueprint_mitigation * 0.45))
        world.architecture = clamp(world.architecture - max(0.03, 0.09 - blueprint_mitigation * 0.30))
        world.structural_strain = clamp(world.structural_strain + 0.18)
    elif shock == "resource_shift":
        world.resource_migration = clamp(world.resource_migration + max(0.12, 0.24 - forecast_mitigation * 0.40))
        world.map_knowledge = clamp(world.map_knowledge - max(0.05, 0.12 - forecast_mitigation * 0.26))
    else:
        world.wind = clamp(world.wind + 0.24)
        world.structural_strain = clamp(world.structural_strain + max(0.10, 0.20 - blueprint_mitigation * 0.35))
        world.paths = clamp(world.paths - max(0.04, 0.10 - forecast_mitigation * 0.20))
    world.risk_memory = clamp(world.risk_memory + 0.18)
    world.adaptive_pressure = clamp(world.adaptive_pressure + 0.16)
    world.next_shock = world.time + 8.0 + rng.random() * 9.0
    return shock


def action_success(agent: Agent, world: World, base_skill: float, condition: Condition, rng: random.Random) -> float:
    tool_bonus = world.tools * 0.16 + world.workshop * 0.10 + world.tool_blueprints * (0.10 if condition.blueprints else 0.0)
    culture_bonus = world.culture * 0.07 + world.apprenticeship * (0.08 if condition.apprenticeship else 0.0)
    forecast_bonus = world.forecast_memory * (0.05 if condition.forecast else 0.0)
    return clamp(
        agent.energy * 0.22
        + agent.health * 0.18
        + base_skill * 0.34
        + tool_bonus
        + culture_bonus
        + forecast_bonus
        + rng.random() * 0.12
        - agent.stress * 0.08
        - agent.injury * 0.07
    )


def choose_action(agent: Agent, world: World, condition: Condition, rng: random.Random) -> str:
    if condition.name == "reactive_immediate_needs":
        if agent.energy < 0.23 or agent.health < 0.46:
            return "rest"
        if agent.illness > 0.42 or world.disease > 0.50:
            return "treat"
        return "collect_water" if world.water < world.food or agent.thirst > agent.hunger else "harvest_food"
    if agent.child:
        if agent.energy < 0.34 or agent.health < 0.64:
            return "rest"
        return "learn" if condition.apprenticeship and world.apprenticeship > 0.20 else "stay_near_shelter"

    urgent = max(
        agent.thirst,
        agent.hunger,
        max(0.0, 0.42 - world.water) * 1.45,
        max(0.0, 0.42 - world.food) * 1.35,
        max(0.0, 0.42 - agent.health) * 1.45,
    )
    if urgent > 0.64:
        if agent.energy < 0.18 or agent.health < 0.38:
            return "rest"
        return "collect_water" if world.water < world.food or agent.thirst > agent.hunger else "harvest_food"
    if world.disease + world.contamination > 0.58 or agent.illness > 0.40:
        return "sanitize" if world.sanitation < 0.54 else "treat"
    if condition.pest_control and world.pest_pressure > 0.32:
        return "control_pests"
    if condition.strain_repair and world.structural_strain > 0.36:
        return "repair_strain"
    if condition.forecast and (world.forecast_memory < 0.48 or world.resource_migration > 0.36 or world.route_hazard > 0.38):
        return "scout"
    if condition.seed_bank and (world.seed_bank < 0.46 or (world.pest_pressure > 0.24 and world.food < 0.68)):
        return "harvest_food" if rng.random() < 0.55 else "construct"
    if condition.blueprints and (world.building_blueprints < 0.44 or world.tool_blueprints < 0.42):
        return "improve_tools" if world.tool_blueprints < world.building_blueprints else "construct"
    if condition.planning and (world.shelter < 0.70 or world.architecture < 0.66 or world.waterworks < 0.54 or world.granary < 0.54 or world.paths < 0.54):
        return "construct"
    if condition.planning and world.fuel_reserve < 0.44:
        return "gather_fuel"
    if world.tools < 0.70 or world.workshop < 0.56 or world.fire_control < 0.44:
        return "improve_tools"
    if condition.apprenticeship and (world.apprenticeship < 0.52 or world.culture < 0.66 or world.knowledge_transfer < 0.46) and rng.random() < 0.62:
        return "teach"
    if world.conflict > 0.30 or world.social_trust < 0.56 or world.symbols < 0.40:
        return "social_repair"
    if agent.energy < 0.34 or agent.stress > 0.64:
        return "rest"
    return rng.choice(("construct", "improve_tools", "teach", "scout", "control_pests", "repair_strain", "harvest_food", "collect_water", "gather_fuel"))


def apply_action(agent: Agent, world: World, agents: List[Agent], condition: Condition, action: str, dt: float, rng: random.Random) -> None:
    agent.action = action
    evidence = 0.0
    if action == "harvest_food":
        success = action_success(agent, world, agent.harvest_skill, condition, rng)
        gain = (0.017 + success * 0.045 + world.garden * 0.014 + world.granary * 0.012 + world.seed_bank * 0.010 - world.resource_migration * 0.006) * dt
        world.food = clamp(world.food + gain)
        if condition.seed_bank:
            world.seed_bank = clamp(world.seed_bank + success * 0.010 * dt + max(0.0, gain - 0.025) * 0.10)
        world.pest_pressure = clamp(world.pest_pressure - success * 0.003 * dt)
        agent.hunger = clamp(agent.hunger - success * 0.12 * dt)
        agent.harvest_skill = clamp(agent.harvest_skill + success * 0.007 * dt)
        evidence = success * 0.05
    elif action == "collect_water":
        success = action_success(agent, world, agent.harvest_skill, condition, rng)
        gain = (0.017 + success * 0.048 + world.waterworks * 0.018 + world.forecast_memory * 0.006 - world.contamination * 0.006) * dt
        world.water = clamp(world.water + gain)
        agent.thirst = clamp(agent.thirst - success * 0.13 * dt)
        agent.harvest_skill = clamp(agent.harvest_skill + success * 0.006 * dt)
        evidence = success * 0.04
    elif action == "gather_fuel":
        success = action_success(agent, world, agent.harvest_skill * 0.5 + agent.scout_skill * 0.5, condition, rng)
        world.fuel_reserve = clamp(world.fuel_reserve + (0.014 + success * 0.040 + world.paths * 0.010 + world.forecast_memory * 0.006) * dt)
        world.materials = clamp(world.materials + success * 0.012 * dt)
        agent.harvest_skill = clamp(agent.harvest_skill + success * 0.004 * dt)
        agent.scout_skill = clamp(agent.scout_skill + success * 0.003 * dt)
        evidence = success * 0.05
    elif action == "construct":
        success = action_success(agent, world, agent.build_skill, condition, rng)
        persistence = 1.0 if condition.planning else 0.08
        world.materials = clamp(world.materials - success * 0.010 * dt)
        world.shelter = clamp(world.shelter + success * 0.024 * persistence * dt)
        world.architecture = clamp(world.architecture + success * 0.024 * persistence * dt)
        world.waterworks = clamp(world.waterworks + success * 0.020 * persistence * dt)
        world.granary = clamp(world.granary + success * 0.020 * persistence * dt)
        world.paths = clamp(world.paths + success * 0.019 * persistence * dt)
        world.garden = clamp(world.garden + success * 0.013 * persistence * dt)
        world.fuel_reserve = clamp(world.fuel_reserve + success * 0.006 * dt)
        if condition.blueprints:
            world.building_blueprints = clamp(world.building_blueprints + success * 0.014 * dt)
        if condition.strain_repair:
            world.structural_strain = clamp(world.structural_strain - success * 0.010 * dt)
        agent.build_skill = clamp(agent.build_skill + success * 0.009 * dt)
        evidence = success * 0.13
    elif action == "improve_tools":
        success = action_success(agent, world, agent.tool_skill, condition, rng)
        world.materials = clamp(world.materials - success * 0.010 * dt)
        world.tools = clamp(world.tools + success * 0.030 * dt)
        world.workshop = clamp(world.workshop + success * 0.024 * dt)
        world.fire_control = clamp(world.fire_control + success * 0.018 * dt)
        if condition.blueprints:
            world.tool_blueprints = clamp(world.tool_blueprints + success * 0.014 * dt)
        agent.tool_skill = clamp(agent.tool_skill + success * 0.010 * dt)
        evidence = success * 0.12
    elif action == "control_pests":
        success = action_success(agent, world, agent.care_skill * 0.55 + agent.harvest_skill * 0.45, condition, rng)
        if condition.pest_control:
            world.pest_pressure = clamp(world.pest_pressure - success * 0.042 * dt)
            world.contamination = clamp(world.contamination - success * 0.012 * dt)
            world.seed_bank = clamp(world.seed_bank + success * 0.006 * dt if condition.seed_bank else world.seed_bank)
            world.garden = clamp(world.garden + success * 0.004 * dt)
        agent.care_skill = clamp(agent.care_skill + success * 0.006 * dt)
        evidence = success * 0.09
    elif action == "repair_strain":
        success = action_success(agent, world, agent.build_skill * 0.60 + agent.tool_skill * 0.40, condition, rng)
        if condition.strain_repair:
            world.structural_strain = clamp(world.structural_strain - success * 0.042 * dt)
            world.shelter = clamp(world.shelter + success * 0.016 * dt)
            world.architecture = clamp(world.architecture + success * 0.010 * dt)
            if condition.blueprints:
                world.building_blueprints = clamp(world.building_blueprints + success * 0.006 * dt)
        agent.build_skill = clamp(agent.build_skill + success * 0.006 * dt)
        evidence = success * 0.10
    elif action == "sanitize":
        success = action_success(agent, world, agent.care_skill, condition, rng)
        world.sanitation = clamp(world.sanitation + success * 0.034 * dt)
        world.contamination = clamp(world.contamination - success * 0.038 * dt)
        world.disease = clamp(world.disease - success * 0.024 * dt)
        world.pest_pressure = clamp(world.pest_pressure - success * 0.006 * dt)
        agent.care_skill = clamp(agent.care_skill + success * 0.008 * dt)
        evidence = success * 0.08
    elif action == "treat":
        success = action_success(agent, world, agent.care_skill, condition, rng)
        world.medicine = clamp(world.medicine - success * 0.004 * dt)
        world.disease = clamp(world.disease - success * 0.030 * dt)
        agent.health = clamp(agent.health + success * 0.038 * dt)
        agent.illness = clamp(agent.illness - success * 0.056 * dt)
        agent.care_skill = clamp(agent.care_skill + success * 0.007 * dt)
        evidence = success * 0.08
    elif action == "scout":
        success = action_success(agent, world, agent.scout_skill, condition, rng)
        if rng.random() < world.route_hazard * 0.015 * dt:
            agent.injury = clamp(agent.injury + 0.10)
            agent.stress = clamp(agent.stress + 0.12)
        world.map_knowledge = clamp(world.map_knowledge + success * 0.038 * dt)
        world.terrain_knowledge = clamp(world.terrain_knowledge + success * 0.034 * dt)
        world.risk_memory = clamp(world.risk_memory + success * 0.014 * dt + world.route_hazard * 0.010 * dt)
        if condition.forecast:
            world.forecast_memory = clamp(world.forecast_memory + success * 0.026 * dt)
        agent.scout_skill = clamp(agent.scout_skill + success * 0.009 * dt)
        evidence = success * 0.11
    elif action == "teach":
        success = action_success(agent, world, agent.teach_skill, condition, rng)
        world.culture = clamp(world.culture + success * 0.032 * dt)
        world.symbols = clamp(world.symbols + success * 0.024 * dt)
        if condition.apprenticeship:
            world.apprenticeship = clamp(world.apprenticeship + success * 0.030 * dt)
            world.knowledge_transfer = clamp(world.knowledge_transfer + success * 0.032 * dt)
        world.risk_memory = clamp(world.risk_memory + success * 0.014 * dt)
        for other in living(agents):
            if other is agent:
                continue
            shared = success * (0.0035 if other.child else 0.0018) * dt * (0.50 + world.apprenticeship)
            other.build_skill = clamp(other.build_skill + agent.build_skill * shared)
            other.tool_skill = clamp(other.tool_skill + agent.tool_skill * shared)
            other.harvest_skill = clamp(other.harvest_skill + agent.harvest_skill * shared)
            other.wisdom = clamp(other.wisdom + success * 0.0022 * dt)
        agent.teach_skill = clamp(agent.teach_skill + success * 0.009 * dt)
        evidence = success * 0.11
    elif action == "social_repair":
        success = action_success(agent, world, agent.teach_skill * 0.45 + agent.care_skill * 0.35 + agent.sociability * 0.20, condition, rng)
        world.social_trust = clamp(world.social_trust + success * 0.032 * dt)
        world.conflict = clamp(world.conflict - success * 0.034 * dt)
        world.culture = clamp(world.culture + success * 0.014 * dt)
        world.symbols = clamp(world.symbols + success * 0.010 * dt)
        evidence = success * 0.07
    elif action == "learn":
        success = clamp(world.culture * 0.28 + world.symbols * 0.18 + world.apprenticeship * 0.32 + agent.sociability * 0.12 + rng.random() * 0.12)
        agent.wisdom = clamp(agent.wisdom + success * 0.012 * dt)
        agent.build_skill = clamp(agent.build_skill + world.building_blueprints * 0.007 * dt)
        agent.tool_skill = clamp(agent.tool_skill + world.tool_blueprints * 0.007 * dt)
        agent.harvest_skill = clamp(agent.harvest_skill + world.map_knowledge * 0.005 * dt)
        world.knowledge_transfer = clamp(world.knowledge_transfer + success * 0.010 * dt)
        evidence = success * 0.05
    elif action in {"rest", "stay_near_shelter"}:
        safety = clamp(world.shelter * 0.34 + world.architecture * 0.16 + world.fire_control * 0.12 + world.fuel_reserve * 0.12 + 0.22)
        agent.energy = clamp(agent.energy + safety * 0.15 * dt)
        agent.health = clamp(agent.health + safety * 0.018 * dt)
        agent.stress = clamp(agent.stress - safety * 0.060 * dt)
    world.adaptation_evidence = clamp(world.adaptation_evidence + evidence * (0.50 + world.adaptive_pressure * 0.50) * dt)
    agent.wisdom = clamp(agent.wisdom + evidence * 0.016 * dt)
    agent.energy = clamp(agent.energy - (0.012 if action not in {"rest", "stay_near_shelter"} else 0.003) * dt)
    agent.stress = clamp(agent.stress + world.adaptive_pressure * 0.006 * dt + world.conflict * 0.010 * dt - world.culture * 0.005 * dt)


def update_agents(world: World, agents: List[Agent], condition: Condition, dt: float, rng: random.Random) -> None:
    for agent in living(agents):
        agent.age_hours += dt
        action = choose_action(agent, world, condition, rng)
        apply_action(agent, world, agents, condition, action, dt, rng)

    for agent in living(agents):
        age_pressure = max(0.0, agent.age_hours - agent.max_life_hours * 0.74) / max(1.0, agent.max_life_hours * 0.26)
        exposure_buffer = clamp(world.shelter * 0.34 + world.architecture * 0.16 + world.fuel_reserve * 0.18)
        thermal = max(0.0, abs(world.temperature - 0.55) - exposure_buffer * 0.20) * 0.018
        shelter_protection = world.shelter * 0.014 + world.architecture * 0.006 + world.fuel_reserve * 0.004
        agent.hunger = clamp(agent.hunger + (0.011 + thermal + agent.stress * 0.003) * dt - (world.food + world.granary * 0.30 + world.seed_bank * 0.12) * 0.010 * dt)
        agent.thirst = clamp(agent.thirst + (0.013 + max(0.0, world.temperature - 0.62) * 0.018 + agent.stress * 0.003) * dt - (world.water + world.waterworks * 0.26) * 0.012 * dt)
        agent.illness = clamp(agent.illness + (world.disease * 0.022 + world.contamination * 0.015 + world.pest_pressure * 0.010 - world.sanitation * 0.014) * dt)
        agent.injury = clamp(agent.injury - (world.medicine + world.shelter) * 0.008 * dt)
        quality_penalty = world.pest_pressure * 0.020 + world.structural_strain * 0.018 + max(0.0, 0.34 - world.fuel_reserve) * 0.018
        health_loss = max(0.0, agent.hunger - 0.88) * 0.22 + max(0.0, agent.thirst - 0.88) * 0.28 + agent.illness * 0.030 + agent.injury * 0.018 + age_pressure * 0.014 + quality_penalty
        agent.health = clamp(agent.health - max(0.0, health_loss - shelter_protection) * dt)
        agent.energy = clamp(agent.energy - (0.004 + age_pressure * 0.010 - world.shelter * 0.003) * dt)
        if agent.health <= 0.03 or agent.thirst >= 0.995 or agent.age_hours > agent.max_life_hours:
            agent.alive = False
            world.deaths += 1


def maybe_reproduce(world: World, agents: List[Agent], condition: Condition, rng: random.Random, dt: float) -> None:
    if not condition.reproduction or world.time < 18.0 or len(agents) >= 30:
        return
    if world.food < 0.56 or world.water < 0.56 or world.shelter < 0.58 or world.social_trust < 0.46 or environment_readiness(world) < 0.28:
        return
    if rng.random() > 0.175 * dt * (0.60 + world.culture + world.apprenticeship * 0.40):
        return
    adults = [agent for agent in living(agents) if not agent.child and agent.health > 0.72 and agent.energy > 0.40 and agent.age_hours < agent.max_life_hours * 0.74]
    if len(adults) < 2:
        return
    parent_a, parent_b = rng.sample(adults, 2)
    lineage = 0.0
    if condition.apprenticeship:
        lineage = clamp(world.apprenticeship * 0.18 + world.knowledge_transfer * 0.14 + safe_mean((parent_a.wisdom, parent_b.wisdom)) * 0.10)
    child = Agent(
        ident=f"G{max(agent.generation for agent in agents) + 1}-{world.births + 1:02d}",
        generation=max(parent_a.generation, parent_b.generation) + 1,
        age_hours=0.0,
        max_life_hours=108.0 + safe_mean((parent_a.resilience, parent_b.resilience)) * 58.0 + rng.random() * 20.0,
        resilience=clamp(safe_mean((parent_a.resilience, parent_b.resilience)) + rng.uniform(-0.04, 0.04)),
        dexterity=clamp(safe_mean((parent_a.dexterity, parent_b.dexterity)) + rng.uniform(-0.04, 0.04)),
        sociability=clamp(safe_mean((parent_a.sociability, parent_b.sociability)) + rng.uniform(-0.04, 0.04)),
        curiosity=clamp(safe_mean((parent_a.curiosity, parent_b.curiosity)) + rng.uniform(-0.04, 0.04)),
        health=0.70,
        energy=0.56,
        hunger=0.34,
        thirst=0.34,
        stress=0.20,
        illness=0.03,
        injury=0.0,
        wisdom=lineage * 0.36,
        build_skill=0.05 + lineage,
        tool_skill=0.05 + lineage,
        harvest_skill=0.07 + lineage,
        scout_skill=0.05 + lineage,
        care_skill=0.05 + lineage,
        teach_skill=0.05 + lineage,
        child=True,
    )
    parent_a.energy = clamp(parent_a.energy - 0.08)
    parent_b.energy = clamp(parent_b.energy - 0.06)
    parent_a.stress = clamp(parent_a.stress + 0.04)
    parent_b.stress = clamp(parent_b.stress + 0.03)
    world.births += 1
    world.knowledge_transfer = clamp(world.knowledge_transfer + lineage * 0.42)
    agents.append(child)


def mature_children(agents: List[Agent]) -> None:
    for agent in agents:
        if agent.child and agent.alive and agent.age_hours >= 16.0:
            agent.child = False
            agent.energy = clamp(agent.energy + 0.12)


def snapshot(world: World, agents: List[Agent], label: str, events: List[str]) -> TraceFrame:
    alive = living(agents)
    return {
        "label": label,
        "hours": round(world.time, 3),
        "alive": len(alive),
        "total_agents": len(agents),
        "children": sum(1 for agent in alive if agent.child),
        "births": world.births,
        "deaths": world.deaths,
        "major_shocks": world.major_shocks,
        "next_shock": round(world.next_shock, 3),
        "weather": world.weather,
        "food": world.food,
        "water": world.water,
        "materials": world.materials,
        "shelter": world.shelter,
        "architecture": world.architecture,
        "tools": world.tools,
        "tool_system": tool_system(world),
        "fuel_reserve": world.fuel_reserve,
        "seed_bank": world.seed_bank,
        "building_blueprints": world.building_blueprints,
        "tool_blueprints": world.tool_blueprints,
        "forecast_memory": world.forecast_memory,
        "apprenticeship": world.apprenticeship,
        "environment_readiness": environment_readiness(world),
        "pest_pressure": world.pest_pressure,
        "structural_strain": world.structural_strain,
        "culture": world.culture,
        "symbols": world.symbols,
        "knowledge_transfer": world.knowledge_transfer,
        "risk_memory": world.risk_memory,
        "map_knowledge": world.map_knowledge,
        "contamination": world.contamination,
        "disease": world.disease,
        "route_hazard": world.route_hazard,
        "resource_migration": world.resource_migration,
        "adaptive_pressure": world.adaptive_pressure,
        "pressure_integral": world.pressure_integral,
        "adaptation_evidence": world.adaptation_evidence,
        "mean_wisdom": safe_mean(agent.wisdom for agent in alive),
        "mean_health": safe_mean(agent.health for agent in alive),
        "mean_energy": safe_mean(agent.energy for agent in alive),
        "actions": {action: sum(1 for agent in alive if agent.action == action) for action in sorted({agent.action for agent in alive})},
        "events": events[-6:],
    }


def score_episode(
    world: World,
    agents: List[Agent],
    baseline: Dict[str, float],
    at_12: Dict[str, float],
    seed: int,
    condition: Condition,
    alive_at_12h: int,
    no_pre_gate_shock: bool,
) -> EpisodeRow:
    alive = living(agents)
    final_alive = len(alive)
    total_agents = len(agents)
    readiness = environment_readiness(world)
    readiness_at_12 = at_12.get("readiness", 0.0)
    architecture_delta = world.architecture - baseline["architecture"]
    tool_delta = tool_system(world) - baseline["tool_system"]
    survival_score = clamp(final_alive / max(1, total_agents) * 0.70 + min(1.0, final_alive / max(1.0, baseline["population"])) * 0.30)
    readiness_score = clamp(readiness * 0.78 + readiness_at_12 * 0.20 + max(0.0, readiness - readiness_at_12) * 0.10)
    development_score = clamp(
        max(0.0, architecture_delta) * 0.36
        + max(0.0, tool_delta) * 0.34
        + max(0.0, world.shelter - baseline["shelter"]) * 0.12
        + max(0.0, world.granary - baseline["granary"]) * 0.08
        + max(0.0, world.paths - baseline["paths"]) * 0.08
        + readiness * 0.18
    )
    knowledge_score = clamp(world.knowledge_transfer * 0.48 + world.apprenticeship * 0.30 + world.culture * 0.20 + world.symbols * 0.14 + safe_mean(agent.wisdom for agent in alive) * 0.12)
    resilience_score = clamp(
        (1.0 if world.major_shocks > 0 else 0.0) * 0.14
        + survival_score * 0.24
        + readiness * 0.24
        + world.adaptation_evidence * 0.18
        + max(0.0, 0.72 - world.pest_pressure) * 0.09
        + max(0.0, 0.72 - world.structural_strain) * 0.09
        + max(0.0, 0.62 - world.disease) * 0.06
    )
    maturation_score = clamp(
        survival_score * 0.22
        + readiness_score * 0.24
        + development_score * 0.20
        + knowledge_score * 0.16
        + resilience_score * 0.18
        + world.births * 0.018
    )
    return EpisodeRow(
        seed=seed,
        condition=condition.name,
        final_alive=final_alive,
        total_agents=total_agents,
        alive_at_12h=alive_at_12h,
        no_major_shock_before_12h=no_pre_gate_shock,
        post_gate_shock=world.major_shocks > 0,
        major_shocks=world.major_shocks,
        first_shock_hour=world.first_shock_hour,
        births=world.births,
        deaths=world.deaths,
        readiness_at_12h=readiness_at_12,
        final_readiness=readiness,
        readiness_delta=readiness - baseline["readiness"],
        final_pest_pressure=world.pest_pressure,
        final_structural_strain=world.structural_strain,
        final_fuel_reserve=world.fuel_reserve,
        final_seed_bank=world.seed_bank,
        final_building_blueprints=world.building_blueprints,
        final_tool_blueprints=world.tool_blueprints,
        final_forecast_memory=world.forecast_memory,
        final_apprenticeship=world.apprenticeship,
        architecture_delta=architecture_delta,
        tool_system_delta=tool_delta,
        knowledge_transfer=world.knowledge_transfer,
        adaptation_evidence=world.adaptation_evidence,
        pressure_integral=world.pressure_integral,
        survival_score=survival_score,
        readiness_score=readiness_score,
        development_score=development_score,
        knowledge_score=knowledge_score,
        resilience_score=resilience_score,
        maturation_score=maturation_score,
    )


def run_episode(seed: int, condition: Condition, cfg: Config, *, trace: bool = False) -> Tuple[EpisodeRow, Trace]:
    rng = random.Random(seed * 101 + sum(ord(char) for char in condition.name))
    agents = make_agents(rng, cfg.population)
    world = make_world(rng)
    baseline = {
        "architecture": world.architecture,
        "tool_system": tool_system(world),
        "shelter": world.shelter,
        "granary": world.granary,
        "paths": world.paths,
        "readiness": environment_readiness(world),
        "population": float(cfg.population),
    }
    events: List[str] = []
    trace_out = Trace(seed=seed, condition=condition.name)
    checkpoints = list(TRACE_CHECKPOINTS)
    no_pre_gate_shock = True
    alive_at_12h = cfg.population
    at_12: Dict[str, float] = {}
    if trace:
        trace_out.frames.append(snapshot(world, agents, "0h", events))
        if checkpoints and checkpoints[0] == 0.0:
            checkpoints.pop(0)

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        world.time += dt
        update_environment(world, agents, condition, dt, rng)
        shock = maybe_major_shock(world, condition, rng)
        if shock:
            events.append(f"{world.time:.1f}h: {shock.replace('_', ' ')} shock")
        pressure = pressure_components(world, agents)
        alpha = min(0.10, max(0.004, dt / 1.5))
        world.adaptive_pressure = clamp(world.adaptive_pressure * (1.0 - alpha) + pressure["total"] * alpha)
        world.pressure_integral = clamp(world.pressure_integral + pressure["total"] * dt / max(1.0, cfg.hours))
        update_agents(world, agents, condition, dt, rng)
        mature_children(agents)
        before_births = world.births
        maybe_reproduce(world, agents, condition, rng, dt)
        if world.births > before_births:
            events.append(f"{world.time:.1f}h: new generation born")

        if world.time < 12.0 and world.major_shocks > 0:
            no_pre_gate_shock = False
        if world.time >= 12.0 and not at_12:
            alive_at_12h = len(living(agents))
            at_12 = {
                "readiness": environment_readiness(world),
            }
        while trace and checkpoints and world.time >= checkpoints[0] - 1e-9:
            hour = checkpoints.pop(0)
            trace_out.frames.append(snapshot(world, agents, f"{hour:g}h", events))

    if trace and (not trace_out.frames or trace_out.frames[-1]["hours"] < cfg.hours):
        trace_out.frames.append(snapshot(world, agents, f"{cfg.hours:g}h", events))
    return score_episode(world, agents, baseline, at_12, seed, condition, alive_at_12h, no_pre_gate_shock), trace_out


def summarize(rows: Sequence[EpisodeRow]) -> List[SummaryRow]:
    output: List[SummaryRow] = []
    for condition in [condition.name for condition in CONDITIONS]:
        items = [row for row in rows if row.condition == condition]
        output.append(
            SummaryRow(
                condition=condition,
                mean_maturation_score=safe_mean(row.maturation_score for row in items),
                mean_survival_score=safe_mean(row.survival_score for row in items),
                mean_readiness_score=safe_mean(row.readiness_score for row in items),
                mean_development_score=safe_mean(row.development_score for row in items),
                mean_knowledge_score=safe_mean(row.knowledge_score for row in items),
                mean_resilience_score=safe_mean(row.resilience_score for row in items),
                mean_final_alive=safe_mean(row.final_alive for row in items),
                mean_alive_at_12h=safe_mean(row.alive_at_12h for row in items),
                mean_births=safe_mean(row.births for row in items),
                mean_deaths=safe_mean(row.deaths for row in items),
                mean_readiness_at_12h=safe_mean(row.readiness_at_12h for row in items),
                mean_final_readiness=safe_mean(row.final_readiness for row in items),
                mean_readiness_delta=safe_mean(row.readiness_delta for row in items),
                mean_final_fuel_reserve=safe_mean(row.final_fuel_reserve for row in items),
                mean_final_seed_bank=safe_mean(row.final_seed_bank for row in items),
                mean_final_building_blueprints=safe_mean(row.final_building_blueprints for row in items),
                mean_final_tool_blueprints=safe_mean(row.final_tool_blueprints for row in items),
                mean_final_forecast_memory=safe_mean(row.final_forecast_memory for row in items),
                mean_final_apprenticeship=safe_mean(row.final_apprenticeship for row in items),
                mean_final_pest_pressure=safe_mean(row.final_pest_pressure for row in items),
                mean_final_structural_strain=safe_mean(row.final_structural_strain for row in items),
                mean_architecture_delta=safe_mean(row.architecture_delta for row in items),
                mean_tool_system_delta=safe_mean(row.tool_system_delta for row in items),
                mean_knowledge_transfer=safe_mean(row.knowledge_transfer for row in items),
                mean_adaptation_evidence=safe_mean(row.adaptation_evidence for row in items),
                shock_gate_pass_rate=safe_mean(1.0 if row.no_major_shock_before_12h else 0.0 for row in items),
                post_gate_shock_rate=safe_mean(1.0 if row.post_gate_shock else 0.0 for row in items),
            )
        )
    return output


def verdict_from_summary(summary: Sequence[SummaryRow]) -> VerdictRow:
    by_name = {row.condition: row for row in summary}
    full = by_name["integrated_readiness"]
    reactive = by_name["reactive_immediate_needs"]
    no_seed = by_name["no_seed_bank"]
    no_blueprint = by_name["no_blueprints"]
    no_forecast = by_name["no_forecast_memory"]
    no_apprentice = by_name["no_apprenticeship"]
    no_pest = by_name["no_pest_control"]
    no_strain = by_name["no_structural_repair"]

    reactive_loss = full.mean_maturation_score - reactive.mean_maturation_score
    seed_loss = full.mean_final_seed_bank - no_seed.mean_final_seed_bank
    blueprint_loss = (
        (full.mean_final_building_blueprints + full.mean_final_tool_blueprints)
        - (no_blueprint.mean_final_building_blueprints + no_blueprint.mean_final_tool_blueprints)
    ) / 2.0
    forecast_loss = full.mean_final_forecast_memory - no_forecast.mean_final_forecast_memory
    apprenticeship_loss = full.mean_final_apprenticeship - no_apprentice.mean_final_apprenticeship
    pest_loss = no_pest.mean_final_pest_pressure - full.mean_final_pest_pressure
    strain_loss = no_strain.mean_final_structural_strain - full.mean_final_structural_strain

    supports_window = (
        full.shock_gate_pass_rate == 1.0
        and full.post_gate_shock_rate == 1.0
        and full.mean_alive_at_12h >= 12.0
        and full.mean_readiness_at_12h >= 0.30
    )
    supports_readiness = (
        full.mean_maturation_score >= 0.70
        and full.mean_final_alive >= 10.0
        and full.mean_final_readiness >= 0.44
        and full.mean_final_pest_pressure <= 0.62
        and full.mean_final_structural_strain <= 0.62
        and full.mean_knowledge_transfer >= 0.38
        and full.mean_architecture_delta > 0.10
        and full.mean_tool_system_delta > 0.10
    )
    supports_ablation = (
        reactive_loss >= 0.12
        and seed_loss >= 0.40
        and blueprint_loss >= 0.40
        and forecast_loss >= 0.40
        and apprenticeship_loss >= 0.40
        and pest_loss >= 0.040
        and strain_loss >= 0.040
    )
    return VerdictRow(
        integrated_score=full.mean_maturation_score,
        reactive_score=reactive.mean_maturation_score,
        no_seed_score=no_seed.mean_maturation_score,
        no_blueprint_score=no_blueprint.mean_maturation_score,
        no_forecast_score=no_forecast.mean_maturation_score,
        no_apprenticeship_score=no_apprentice.mean_maturation_score,
        no_pest_control_score=no_pest.mean_maturation_score,
        no_structural_repair_score=no_strain.mean_maturation_score,
        reactive_loss=reactive_loss,
        seed_bank_loss=seed_loss,
        blueprint_loss=blueprint_loss,
        forecast_loss=forecast_loss,
        apprenticeship_loss=apprenticeship_loss,
        pest_control_loss=pest_loss,
        structural_repair_loss=strain_loss,
        shock_gate_pass_rate=full.shock_gate_pass_rate,
        post_gate_shock_rate=full.post_gate_shock_rate,
        survival_at_12h=full.mean_alive_at_12h,
        readiness_at_12h=full.mean_readiness_at_12h,
        final_readiness=full.mean_final_readiness,
        final_pest_pressure=full.mean_final_pest_pressure,
        final_structural_strain=full.mean_final_structural_strain,
        supports_12h_development_window=supports_window,
        supports_environment_readiness=supports_readiness,
        supports_ablation_specificity=supports_ablation,
        verdict="pass" if supports_window and supports_readiness and supports_ablation else "partial_or_failed",
    )


def write_artifacts(rows: Sequence[EpisodeRow], summary: Sequence[SummaryRow], verdict: VerdictRow, trace: Trace, cfg: Config) -> Dict[str, object]:
    payload = {
        "config": asdict(cfg),
        "summary": [asdict(row) for row in summary],
        "verdict": asdict(verdict),
        "trace": asdict(trace),
        "notes": {
            "claim": "designed environment-readiness maturation verifier",
            "not_claimed": "subjective consciousness, open-ended civilization, deep RL, or learned emergence of the readiness variables",
        },
    }
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_environment_readiness_maturation_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_environment_readiness_maturation_summary.csv", summary)
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_environment_readiness_maturation_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / "ssrm_3d_environment_readiness_maturation_results.json", payload)
    write_json(ARTIFACT_DIR / "ssrm_3d_environment_readiness_maturation_trace.json", asdict(trace))
    write_js(ARTIFACT_DIR / "ssrm_3d_environment_readiness_maturation_results.js", "SSRM_3D_ENVIRONMENT_READINESS_MATURATION_RESULTS", payload)
    write_js(ARTIFACT_DIR / "ssrm_3d_environment_readiness_maturation_trace.js", "SSRM_3D_ENVIRONMENT_READINESS_MATURATION_TRACE", asdict(trace))
    return payload


def run_benchmark(cfg: Config) -> Dict[str, object]:
    rows: List[EpisodeRow] = []
    trace = Trace(seed=cfg.trace_seed, condition="integrated_readiness")
    for seed in cfg.seeds:
        for condition in CONDITIONS:
            row, maybe_trace = run_episode(seed, condition, cfg, trace=(seed == cfg.trace_seed and condition.name == "integrated_readiness"))
            rows.append(row)
            if maybe_trace.frames:
                trace = maybe_trace
    summary = summarize(rows)
    verdict = verdict_from_summary(summary)
    return write_artifacts(rows, summary, verdict, trace, cfg)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seeds", default="20261201,20261202,20261203,20261204,20261205")
    parser.add_argument("--hours", type=float, default=72.0)
    parser.add_argument("--step-hours", type=float, default=0.10)
    parser.add_argument("--population", type=int, default=14)
    parser.add_argument("--trace-seed", type=int, default=20261201)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    seeds = [int(item.strip()) for item in args.seeds.split(",") if item.strip()]
    cfg = Config(seeds=seeds, hours=args.hours, step_hours=args.step_hours, population=args.population, trace_seed=args.trace_seed)
    payload = run_benchmark(cfg)
    print(json.dumps(payload["verdict"], indent=2))
    return 0 if payload["verdict"]["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
