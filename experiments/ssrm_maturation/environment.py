"""Environmental pressure dynamics for the multi-day maturation benchmark."""

from __future__ import annotations

import math
import random
from typing import Dict, Iterable

from .models import Agent, Condition, World


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def living(agents: Iterable[Agent]) -> list[Agent]:
    return [agent for agent in agents if agent.alive]


def set_tiers(world: World) -> None:
    world.architecture_tier = min(4, int(world.architecture / 0.24))
    world.tool_tier = min(4, int(world.tools / 0.22 + world.workshop / 0.34 + world.fire_control / 0.44))


def initialize_shock_schedule(world: World, rng: random.Random) -> None:
    world.next_shock = 12.75 + rng.random() * 4.0


def update_environment(world: World, agents: list[Agent], condition: Condition, dt: float, rng: random.Random) -> Dict[str, float]:
    alive = living(agents)
    day_phase = (world.time % 24.0) / 24.0
    daylight = max(0.0, math.sin(day_phase * math.pi))
    season = math.sin(world.time / 72.0 * math.pi * 2.0 + 0.4)
    storm_roll = rng.random() < (0.010 + world.wind * 0.010 + world.contamination * 0.006) * dt
    heat_wave = max(0.0, season) * 0.22
    cold_snap = max(0.0, -season) * 0.18
    world.weather = "storm" if storm_roll else ("hot" if heat_wave > 0.16 else ("cold" if cold_snap > 0.13 else "clear"))
    world.rainfall = clamp(0.14 + max(0.0, -season) * 0.18 + (0.34 if storm_roll else 0.0) - heat_wave * 0.20)
    world.wind = clamp(0.12 + abs(season) * 0.18 + (0.34 if storm_roll else 0.0))
    world.temperature = clamp(0.54 + heat_wave - cold_snap + daylight * 0.10 - world.rainfall * 0.08)
    world.visibility = clamp(0.30 + daylight * 0.54 - world.rainfall * 0.20 - world.wind * 0.10 + world.paths * 0.12)

    sensing = 1.0 if condition.environmental_sensing else 0.35
    teaching = world.culture if condition.teaching else 0.0
    risk = world.risk_memory if condition.risk_memory else 0.0
    infrastructure = 1.0 if condition.infrastructure_memory else 0.34
    tool_quality = world.tools * 0.45 + world.workshop * 0.30 + world.fire_control * 0.18

    movement = math.sin(world.time / 13.0 * math.pi * 2.0 + 1.1)
    world.resource_migration = clamp(0.10 + abs(movement) * 0.34 + world.predators * 0.08 - world.paths * 0.10 - world.map_knowledge * 0.08)
    world.resource_depletion = clamp(world.resource_depletion + len(alive) * 0.0009 * dt - world.garden * 0.006 * dt - world.culture * 0.003 * dt)
    water_reliability = clamp(0.46 + world.rainfall * 0.22 + world.waterworks * 0.24 - world.contamination * 0.18 - heat_wave * 0.10)
    food_reliability = clamp(0.48 + world.soil * 0.20 + world.garden * 0.18 - world.resource_migration * 0.12 - world.resource_depletion * 0.12)

    cleanliness = mean(1.0 - agent.stress for agent in alive)
    world.soil = clamp(world.soil + (world.rainfall - 0.16) * 0.010 * dt - world.resource_depletion * 0.010 * dt + world.garden * 0.006 * dt)
    world.contamination = clamp(world.contamination + (world.rainfall * 0.020 + world.disease * 0.015 + len(alive) * (1.0 - cleanliness) * 0.0016) * dt - (world.sanitation + world.waterworks) * 0.036 * dt)
    world.disease = clamp(world.disease + (world.contamination * 0.024 + max(0.0, 0.44 - world.shelter) * 0.016) * dt - (world.medicine + world.sanitation + teaching) * 0.030 * dt)
    world.route_hazard = clamp(0.10 + world.predators * 0.24 + world.wind * 0.14 + world.resource_migration * 0.10 - world.paths * 0.16 - world.terrain_knowledge * 0.10)
    world.predators = clamp(world.predators + (world.resource_migration * 0.010 + (0.005 if world.time >= 12.0 else 0.0)) * dt - (risk + world.paths + tool_quality) * 0.016 * dt)
    social_learning = 1.0 if condition.social_learning else 0.18
    world.conflict = clamp(world.conflict + max(0.0, 0.40 - min(world.food, world.water)) * 0.060 * dt - (world.social_trust + world.culture * social_learning) * 0.026 * dt)
    world.social_trust = clamp(
        world.social_trust
        + (world.culture * 0.012 + world.symbols * 0.006) * social_learning * dt
        - (world.conflict * 0.012 + max(0.0, 0.42 - min(world.food, world.water)) * 0.012) * dt
    )

    count = len(alive)
    world.food = clamp(world.food - count * 0.0025 * dt + world.garden * food_reliability * 0.084 * dt + world.granary * 0.026 * dt - world.contamination * 0.006 * dt)
    world.water = clamp(world.water - count * 0.0028 * dt + world.waterworks * water_reliability * 0.082 * dt + world.rainfall * 0.016 * dt - world.contamination * 0.007 * dt)
    world.materials = clamp(world.materials + (world.paths + world.map_knowledge + world.tool_tier * 0.05) * 0.010 * dt - max(0, count - 4) * 0.0012 * dt)
    world.tools = clamp(world.tools - count * (0.0017 - min(0.0012, world.workshop * 0.0009 + world.tool_tier * 0.0003)) * dt)
    world.shelter = clamp(world.shelter - (0.004 + world.wind * 0.008 + world.rainfall * 0.006 - world.architecture * 0.008) * dt)

    if condition.infrastructure_memory:
        world.architecture = clamp(world.architecture - world.wind * 0.004 * dt)
        world.paths = clamp(world.paths - world.rainfall * 0.005 * dt + world.terrain_knowledge * 0.003 * dt)
        world.granary = clamp(world.granary - world.contamination * 0.003 * dt)
    else:
        world.architecture = clamp(world.architecture - 0.020 * dt)
        world.paths = clamp(world.paths - 0.020 * dt)
        world.granary = clamp(world.granary - 0.018 * dt)
        world.waterworks = clamp(world.waterworks - 0.018 * dt)
        world.sanitation = clamp(world.sanitation - 0.016 * dt)

    if condition.risk_memory:
        world.risk_memory = clamp(world.risk_memory * (1.0 - 0.003 * dt) + world.major_shocks * 0.0008 * dt + world.route_hazard * 0.003 * dt)
    else:
        world.risk_memory = 0.0
    world.map_knowledge = clamp(world.map_knowledge * (1.0 - (0.006 + world.resource_migration * 0.004) * dt) + sensing * world.terrain_knowledge * 0.004 * dt)
    set_tiers(world)
    return {
        "water_reliability": water_reliability,
        "food_reliability": food_reliability,
        "sensing": sensing,
    }


def maybe_major_shock(world: World, rng: random.Random) -> str | None:
    if world.time < 12.0 or world.time < world.next_shock:
        return None
    shock = rng.choice(("drought", "epidemic", "predator_wave", "crop_failure", "building_failure", "resource_shift"))
    world.major_shocks += 1
    if world.first_shock_hour is None:
        world.first_shock_hour = world.time
    if shock == "drought":
        world.water = clamp(world.water - 0.16)
        world.temperature = clamp(world.temperature + 0.12)
        world.soil = clamp(world.soil - 0.10)
    elif shock == "epidemic":
        world.disease = clamp(world.disease + 0.22)
        world.contamination = clamp(world.contamination + 0.10)
    elif shock == "predator_wave":
        world.predators = clamp(world.predators + 0.24)
        world.route_hazard = clamp(world.route_hazard + 0.14)
    elif shock == "crop_failure":
        world.food = clamp(world.food - 0.18)
        world.garden = clamp(world.garden - 0.08)
        world.resource_depletion = clamp(world.resource_depletion + 0.08)
    elif shock == "building_failure":
        world.shelter = clamp(world.shelter - 0.12)
        world.architecture = clamp(world.architecture - 0.08)
    else:
        world.resource_migration = clamp(world.resource_migration + 0.24)
        world.map_knowledge = clamp(world.map_knowledge - 0.10)
    world.risk_memory = clamp(world.risk_memory + 0.18)
    world.adaptive_pressure = clamp(world.adaptive_pressure + 0.16)
    world.next_shock = world.time + 8.0 + rng.random() * 9.0
    return shock


def pressure_components(world: World, agents: list[Agent]) -> Dict[str, float]:
    alive = living(agents)
    reserves = mean(agent.health * 0.45 + agent.energy * 0.25 + (1.0 - agent.hunger) * 0.15 + (1.0 - agent.thirst) * 0.15 for agent in alive)
    survival = clamp(max(0.0, 0.46 - world.food) * 0.40 + max(0.0, 0.46 - world.water) * 0.45 + world.disease * 0.22 + max(0.0, 0.58 - reserves) * 0.32)
    ecology = clamp(world.resource_migration * 0.24 + world.resource_depletion * 0.20 + world.route_hazard * 0.22 + abs(world.temperature - 0.55) * 0.22 + max(0.0, 0.56 - world.visibility) * 0.18)
    infrastructure = clamp(max(0.0, 0.60 - world.shelter) * 0.22 + max(0.0, 0.56 - world.architecture) * 0.24 + max(0.0, 0.52 - world.tools) * 0.18 + max(0.0, 0.50 - world.waterworks) * 0.16 + max(0.0, 0.48 - world.granary) * 0.12)
    social = clamp(world.conflict * 0.30 + max(0.0, 0.54 - world.social_trust) * 0.20 + max(0.0, 0.46 - world.culture) * 0.16 + sum(1 for agent in alive if agent.child) / max(1, len(alive)) * 0.14)
    uncertainty = clamp(world.resource_migration * 0.18 + max(0.0, 0.58 - world.map_knowledge) * 0.24 + max(0.0, 0.52 - world.risk_memory) * 0.20 + max(0.0, 0.50 - world.symbols) * 0.12)
    total = clamp(survival * 0.24 + ecology * 0.20 + infrastructure * 0.22 + social * 0.16 + uncertainty * 0.18)
    return {
        "survival": survival,
        "ecology": ecology,
        "infrastructure": infrastructure,
        "social": social,
        "uncertainty": uncertainty,
        "total": total,
    }
