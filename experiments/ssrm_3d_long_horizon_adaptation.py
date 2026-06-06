#!/usr/bin/env python3
"""Headless SSRM-3D long-horizon adaptation verifier.

This is a fast, multi-seed companion to the live open-emergence browser
sandbox. It tests the specific milestone the browser audit was designed for:

- no autonomous major shock before the 12h development gate;
- post-gate shock pressure appears after the gate;
- agents survive long enough to develop;
- infrastructure, tool design, risk memory, teaching, and adaptation evidence
  improve across the run;
- targeted ablations create specific losses.

It is still a designed pressure benchmark. It does not claim subjective
experience, open-ended civilization, or closed-loop deep reinforcement learning.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"

CHECKPOINTS = (1.0, 6.0, 12.0, 12.5, 14.5)


@dataclass(frozen=True)
class Config:
    seeds: Sequence[int]
    hours: float = 14.5
    step_hours: float = 0.05
    population: int = 10
    trace_seed: int = 20260708


@dataclass(frozen=True)
class Condition:
    name: str
    description: str
    teaching: bool = True
    risk_memory: bool = True
    infrastructure_memory: bool = True
    tool_improvement: bool = True
    adaptive_arbitration: bool = True


CONDITIONS = (
    Condition("integrated_long_horizon", "full long-horizon state and adaptation channels"),
    Condition("reactive_survival_only", "immediate survival without persistent development channels", teaching=False, risk_memory=False, infrastructure_memory=False, tool_improvement=False, adaptive_arbitration=False),
    Condition("no_teaching_transmission", "teaching and intergenerational knowledge transfer removed", teaching=False),
    Condition("no_risk_memory", "risk memory removed", risk_memory=False),
    Condition("no_infrastructure_memory", "persistent infrastructure memory removed", infrastructure_memory=False),
    Condition("no_tool_improvement", "tool-design improvement removed", tool_improvement=False),
    Condition("no_adaptive_arbitration", "survival cannot override attention/social/fear loops", adaptive_arbitration=False),
)


@dataclass
class Agent:
    health: float
    energy: float
    hunger: float
    thirst: float
    fear: float
    stress: float
    reserve: float
    wisdom: float
    adaptation: float
    attachment: float
    skill_build: float
    skill_tool: float
    skill_harvest: float
    skill_teach: float
    child: bool = False
    alive: bool = True


@dataclass
class World:
    time: float
    food: float
    water: float
    materials: float
    medicine: float
    tools: float
    shelter: float
    architecture: float
    tool_design: float
    food_storage: float
    path_network: float
    waterworks: float
    garden: float
    teaching: float
    risk_memory: float
    map_knowledge: float
    contamination: float
    sickness: float
    threat: float
    conflict: float
    soil: float
    temperature: float
    visibility: float
    route_hazard: float
    ecology_volatility: float
    resource_migration: float
    disease_strain: float
    social_inequality: float
    adaptive_pressure: float
    adaptation_evidence: float
    pressure_integral: float
    major_shocks: int
    next_shock: float
    first_shock_hour: float | None
    births: int
    knowledge_transfer: float


@dataclass(frozen=True)
class EpisodeRow:
    seed: int
    condition: str
    final_alive: int
    total_agents: int
    alive_at_12h: int
    no_major_shock_before_12h: bool
    no_major_shock_at_12h: bool
    post_gate_shock: bool
    major_shocks: int
    first_shock_hour: float
    food_final: float
    water_final: float
    architecture_delta: float
    tool_design_delta: float
    teaching_delta: float
    risk_memory_delta: float
    adaptation_evidence: float
    pressure_integral: float
    births: int
    knowledge_transfer: float
    survival_score: float
    development_score: float
    knowledge_score: float
    post_shock_score: float
    long_horizon_score: float


@dataclass(frozen=True)
class SummaryRow:
    condition: str
    mean_long_horizon_score: float
    mean_survival_score: float
    mean_development_score: float
    mean_knowledge_score: float
    mean_post_shock_score: float
    mean_final_alive: float
    mean_alive_at_12h: float
    mean_adaptation_evidence: float
    mean_architecture_delta: float
    mean_tool_design_delta: float
    mean_knowledge_transfer: float
    no_major_shock_before_12h_rate: float
    post_gate_shock_rate: float


@dataclass(frozen=True)
class VerdictRow:
    integrated_score: float
    reactive_score: float
    no_teaching_score: float
    no_risk_memory_score: float
    no_infrastructure_memory_score: float
    no_tool_improvement_score: float
    no_adaptive_arbitration_score: float
    reactive_loss: float
    teaching_loss: float
    risk_memory_loss: float
    infrastructure_memory_loss: float
    tool_improvement_loss: float
    adaptive_arbitration_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    supports_long_horizon_development: bool
    supports_ablation_specificity: bool
    verdict: str


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def make_agents(rng: random.Random, population: int) -> List[Agent]:
    agents: List[Agent] = []
    for _ in range(population):
        resilience = 0.38 + rng.random() * 0.46
        dexterity = 0.34 + rng.random() * 0.44
        sociability = 0.32 + rng.random() * 0.50
        agents.append(
            Agent(
                health=0.88 + rng.random() * 0.08,
                energy=0.74 + rng.random() * 0.16,
                hunger=0.20 + rng.random() * 0.12,
                thirst=0.20 + rng.random() * 0.12,
                fear=0.10 + rng.random() * 0.12,
                stress=0.10 + rng.random() * 0.12,
                reserve=0.82 + rng.random() * 0.16,
                wisdom=0.10 + rng.random() * 0.10,
                adaptation=0.10 + rng.random() * 0.08,
                attachment=0.38 + rng.random() * 0.22,
                skill_build=0.08 + resilience * 0.10 + rng.random() * 0.08,
                skill_tool=0.08 + dexterity * 0.11 + rng.random() * 0.08,
                skill_harvest=0.10 + dexterity * 0.10 + rng.random() * 0.08,
                skill_teach=0.08 + sociability * 0.12 + rng.random() * 0.08,
            )
        )
    return agents


def make_world(rng: random.Random) -> World:
    return World(
        time=0.0,
        food=0.82,
        water=0.82,
        materials=0.58,
        medicine=0.38,
        tools=0.38,
        shelter=0.48,
        architecture=0.16,
        tool_design=0.14,
        food_storage=0.18,
        path_network=0.12,
        waterworks=0.16,
        garden=0.28,
        teaching=0.08,
        risk_memory=0.08,
        map_knowledge=0.12,
        contamination=0.14,
        sickness=0.10,
        threat=0.12,
        conflict=0.08,
        soil=0.64,
        temperature=0.58,
        visibility=0.82,
        route_hazard=0.18,
        ecology_volatility=0.12,
        resource_migration=0.14,
        disease_strain=0.10,
        social_inequality=0.12,
        adaptive_pressure=0.16,
        adaptation_evidence=0.0,
        pressure_integral=0.0,
        major_shocks=0,
        next_shock=12.75 + rng.random() * 1.50,
        first_shock_hour=None,
        births=0,
        knowledge_transfer=0.0,
    )


def living(agents: Sequence[Agent]) -> List[Agent]:
    return [agent for agent in agents if agent.alive]


def pressure_breakdown(world: World, agents: Sequence[Agent]) -> Dict[str, float]:
    alive = living(agents)
    alive_count = max(1, len(alive))
    survival = clamp(
        max(0.0, 0.54 - world.food) * 0.55
        + max(0.0, 0.54 - world.water) * 0.60
        + world.sickness * 0.22
        + world.contamination * 0.22
        + max(0.0, 0.62 - mean(agent.reserve for agent in alive)) * 0.28
    )
    ecology = clamp(
        world.ecology_volatility * 0.36
        + world.resource_migration * 0.28
        + abs(world.temperature - 0.58) * 0.42
        + max(0.0, 0.55 - world.visibility) * 0.20
        + world.route_hazard * 0.24
    )
    infrastructure = clamp(
        max(0.0, 0.62 - world.shelter) * 0.32
        + max(0.0, 0.54 - world.architecture) * 0.24
        + max(0.0, 0.54 - world.tool_design) * 0.18
        + max(0.0, 0.50 - world.path_network) * 0.16
        + max(0.0, 0.48 - world.waterworks) * 0.12
    )
    social = clamp(
        world.social_inequality * 0.34
        + world.conflict * 0.30
        + max(0.0, 0.56 - mean(agent.attachment for agent in alive)) * 0.12
        + sum(1 for agent in alive if agent.child) / alive_count * 0.18
    )
    uncertainty = clamp(
        world.resource_migration * 0.24
        + max(0.0, 0.58 - world.map_knowledge) * 0.26
        + max(0.0, 0.50 - world.risk_memory) * 0.18
        + world.ecology_volatility * 0.16
    )
    total = clamp(survival * 0.24 + ecology * 0.20 + infrastructure * 0.18 + social * 0.18 + uncertainty * 0.20)
    return {
        "survival": survival,
        "ecology": ecology,
        "infrastructure": infrastructure,
        "social": social,
        "uncertainty": uncertainty,
        "total": total,
    }


def update_environment(world: World, agents: Sequence[Agent], condition: Condition, dt: float, rng: random.Random) -> None:
    day_phase = (world.time % 2.4) / 2.4
    daylight = max(0.0, math.sin(day_phase * math.pi))
    seasonal = math.sin((world.time / 18.0) * math.pi * 2.0)
    storm = 1.0 if rng.random() < (0.018 + world.contamination * 0.010) * dt else 0.0
    migration = math.sin((world.time / 7.2) * math.pi * 2.0 + 0.7)
    water_cycle = math.sin((world.time / 5.6) * math.pi * 2.0 + 1.3)
    alive = living(agents)
    cleanliness = mean(max(0.0, 1.0 - agent.stress) for agent in alive)

    world.ecology_volatility = clamp(0.08 + abs(seasonal) * 0.18 + storm * 0.18 + world.major_shocks * 0.018)
    world.resource_migration = clamp(0.12 + abs(migration) * 0.30 + world.threat * 0.06 + world.ecology_volatility * 0.10 - world.path_network * 0.06)
    world.temperature = clamp(0.54 + seasonal * 0.20 + daylight * 0.13 - storm * 0.11)
    world.visibility = clamp(0.44 + daylight * 0.42 - storm * 0.24 + world.path_network * 0.08)
    water_reliability = clamp(0.54 + water_cycle * 0.15 - world.contamination * 0.18 + world.waterworks * 0.16)
    food_reliability = clamp(0.54 + seasonal * 0.16 + world.soil * 0.22 + world.garden * 0.12 - world.contamination * 0.12 - world.resource_migration * 0.08)

    teaching_factor = world.teaching if condition.teaching else 0.0
    risk_factor = world.risk_memory if condition.risk_memory else 0.0
    infra_factor = 1.0 if condition.infrastructure_memory else 0.38

    world.disease_strain = clamp(world.disease_strain + (world.contamination * 0.030 + storm * 0.018) * dt - (world.medicine + teaching_factor + world.waterworks) * 0.026 * dt)
    world.soil = clamp(world.soil + (food_reliability - 0.55) * 0.014 * dt + world.garden * 0.010 * dt - len(alive) * 0.0012 * dt)
    world.contamination = clamp(world.contamination + (storm * 0.028 + len(alive) * (1.0 - cleanliness) * 0.0020 + world.sickness * 0.015 + world.disease_strain * 0.016) * dt - world.waterworks * 0.050 * dt)
    world.route_hazard = clamp(0.10 + world.threat * 0.30 + storm * 0.22 + world.contamination * 0.08 - world.path_network * 0.18 - world.map_knowledge * 0.10)
    world.sickness = clamp(world.sickness + (storm * 0.030 + 0.007) * dt + world.contamination * 0.025 * dt + world.disease_strain * 0.020 * dt - (world.waterworks + teaching_factor) * 0.030 * dt)
    world.threat = clamp(world.threat + (world.route_hazard * 0.018 + (0.006 if world.time >= 12.0 else 0.0)) * dt - (world.map_knowledge + risk_factor + world.path_network) * 0.022 * dt)
    world.conflict = clamp(world.conflict + max(0.0, 0.38 - min(world.food, world.water)) * 0.10 * dt + world.social_inequality * 0.020 * dt - teaching_factor * 0.040 * dt)

    population_cost = len(alive)
    world.food = clamp(world.food - population_cost * 0.0046 * dt + world.garden * world.soil * food_reliability * 0.145 * dt + world.food_storage * 0.026 * dt - world.contamination * 0.010 * dt - world.resource_migration * 0.002 * dt)
    world.water = clamp(world.water - population_cost * 0.0050 * dt + world.waterworks * water_reliability * 0.118 * dt + max(0.0, seasonal) * 0.010 * dt - world.contamination * 0.012 * dt)
    world.materials = clamp(world.materials + (world.path_network + world.tool_design) * 0.015 * dt - max(0.0, population_cost - 2) * 0.0025 * dt)
    world.tools = clamp(world.tools - max(0.0, population_cost - 2) * (0.0048 - world.tool_design * 0.0024) * dt)
    world.shelter = clamp(world.shelter - (0.006 + storm * 0.018 - world.architecture * 0.008) * dt)
    if not condition.infrastructure_memory:
        world.architecture = clamp(world.architecture - 0.012 * dt)
        world.path_network = clamp(world.path_network - 0.016 * dt)
        world.waterworks = clamp(world.waterworks - 0.012 * dt)
        world.food_storage = clamp(world.food_storage - 0.014 * dt)
    else:
        world.path_network = clamp(world.path_network - storm * 0.014 * dt + world.map_knowledge * 0.004 * dt)
        world.architecture = clamp(world.architecture - storm * 0.008 * dt)
        world.food_storage = clamp(world.food_storage - world.contamination * 0.006 * dt)
    if condition.risk_memory:
        world.risk_memory = clamp(world.risk_memory * (1.0 - 0.006 * dt) + world.major_shocks * 0.001 * dt)
    else:
        world.risk_memory = 0.0


def maybe_trigger_major_shock(world: World, rng: random.Random) -> None:
    if world.time < 12.0 or world.time < world.next_shock:
        return
    shock = rng.choice(("drought", "blight", "epidemic", "structural_failure", "frontier_threat"))
    world.major_shocks += 1
    if world.first_shock_hour is None:
        world.first_shock_hour = world.time
    if shock == "drought":
        world.water = clamp(world.water - 0.18)
        world.soil = clamp(world.soil - 0.12)
        world.temperature = clamp(world.temperature + 0.12)
    elif shock == "blight":
        world.food = clamp(world.food - 0.18)
        world.garden = clamp(world.garden - 0.10)
        world.contamination = clamp(world.contamination + 0.08)
    elif shock == "epidemic":
        world.sickness = clamp(world.sickness + 0.20)
        world.conflict = clamp(world.conflict + 0.04)
    elif shock == "structural_failure":
        world.shelter = clamp(world.shelter - 0.12)
        world.architecture = clamp(world.architecture - 0.08)
    else:
        world.threat = clamp(world.threat + 0.18)
        world.route_hazard = clamp(world.route_hazard + 0.14)
        world.conflict = clamp(world.conflict + 0.06)
    world.risk_memory = clamp(world.risk_memory + 0.18)
    world.next_shock = world.time + 2.5 + rng.random() * 3.5


def choose_action(agent: Agent, world: World, condition: Condition, rng: random.Random) -> str:
    urgent_survival = max(
        agent.thirst,
        agent.hunger,
        max(0.0, 0.42 - world.water) * 1.45,
        max(0.0, 0.42 - world.food) * 1.35,
        max(0.0, 0.32 - agent.energy),
        max(0.0, 0.46 - agent.health),
    )
    if condition.name == "reactive_survival_only":
        if agent.energy < 0.26 or agent.health < 0.50:
            return "rest"
        return "harvest_water" if world.water < world.food or agent.thirst > agent.hunger else "harvest_food"

    if not condition.adaptive_arbitration:
        if agent.energy < 0.22 or agent.health < 0.44:
            return "rest"
        roll = rng.random()
        if agent.fear + world.threat > 0.56 and roll < 0.64:
            return "signal"
        if world.route_hazard > 0.32 and roll < 0.70:
            return "inspect"
        if (world.food < 0.28 or world.water < 0.28 or agent.hunger > 0.74 or agent.thirst > 0.74) and roll < 0.48:
            return "harvest_water" if world.water < world.food or agent.thirst > agent.hunger else "harvest_food"
        if roll < 0.34:
            return "signal"
        if roll < 0.56:
            return "inspect"
        if roll < 0.72:
            return "construct"
        if roll < 0.86:
            return "modify"
        return "rest"

    if condition.adaptive_arbitration and urgent_survival > 0.62:
        if agent.energy < 0.20 or agent.health < 0.42:
            return "rest"
        return "harvest_water" if world.water < world.food or agent.thirst > agent.hunger else "harvest_food"

    if not condition.adaptive_arbitration and agent.fear + world.threat > 0.72 and rng.random() < 0.70:
        return "signal"

    if world.sickness + world.contamination + max(0.0, 0.74 - agent.health) > 0.74:
        return "treat"
    if world.route_hazard > 0.38 or world.map_knowledge < 0.42:
        return "inspect"
    if world.tool_design < 0.52 and world.materials > 0.10:
        return "modify"
    if world.architecture < 0.60 or world.shelter < 0.58 or world.waterworks < 0.48:
        return "construct"
    if condition.teaching and (world.teaching < 0.58 or world.risk_memory < 0.46) and rng.random() < 0.54:
        return "share_pattern"
    if agent.energy < 0.38 or agent.stress > 0.60:
        return "rest"
    if rng.random() < 0.18:
        return "inspect"
    if world.food < 0.58 or world.water < 0.58:
        return "harvest_water" if world.water < world.food else "harvest_food"
    return rng.choice(("construct", "modify", "share_pattern", "inspect", "rest"))


def apply_action(agent: Agent, world: World, condition: Condition, action: str, dt: float, rng: random.Random) -> None:
    tool_factor = 0.58 + world.tools * 0.28 + world.tool_design * 0.24
    teaching_factor = world.teaching if condition.teaching else 0.0
    risk_factor = world.risk_memory if condition.risk_memory else 0.0
    success = clamp(
        agent.energy * 0.23
        + agent.health * 0.18
        + tool_factor * 0.16
        + teaching_factor * 0.08
        + risk_factor * 0.05
        + rng.random() * 0.14
    )
    reward = 0.0
    if action == "harvest_food":
        success = clamp(success + agent.skill_harvest * 0.30 + world.path_network * 0.12 - world.route_hazard * 0.10)
        gain = (0.018 + success * 0.050 + world.garden * 0.014 + world.food_storage * 0.014) * dt
        world.food = clamp(world.food + gain)
        agent.hunger = clamp(agent.hunger - success * 0.16 * dt)
        agent.skill_harvest = clamp(agent.skill_harvest + success * 0.010 * dt)
        reward = gain * 5.5
    elif action == "harvest_water":
        success = clamp(success + agent.skill_harvest * 0.28 + world.path_network * 0.10 - world.route_hazard * 0.08)
        gain = (0.020 + success * 0.055 + world.waterworks * 0.020) * dt
        world.water = clamp(world.water + gain)
        agent.thirst = clamp(agent.thirst - success * 0.17 * dt)
        agent.skill_harvest = clamp(agent.skill_harvest + success * 0.010 * dt)
        reward = gain * 5.5
    elif action == "construct":
        success = clamp(success + agent.skill_build * 0.30 + world.materials * 0.12)
        persistence = 1.0 if condition.infrastructure_memory else 0.28
        world.materials = clamp(world.materials - 0.015 * success * dt)
        world.shelter = clamp(world.shelter + 0.042 * success * persistence * dt)
        world.architecture = clamp(world.architecture + 0.030 * success * persistence * dt)
        world.food_storage = clamp(world.food_storage + 0.022 * success * persistence * dt)
        world.path_network = clamp(world.path_network + 0.026 * success * persistence * dt)
        world.waterworks = clamp(world.waterworks + 0.024 * success * persistence * dt)
        world.garden = clamp(world.garden + 0.018 * success * persistence * dt)
        agent.skill_build = clamp(agent.skill_build + success * 0.012 * dt)
        reward = success * 0.18
    elif action == "modify":
        success = clamp(success + agent.skill_tool * 0.36 + world.materials * 0.10)
        world.materials = clamp(world.materials - 0.014 * success * dt)
        if condition.tool_improvement:
            world.tool_design = clamp(world.tool_design + 0.040 * success * dt)
            world.tools = clamp(world.tools + 0.036 * success * dt)
        else:
            world.tools = clamp(world.tools + 0.012 * success * dt)
        agent.skill_tool = clamp(agent.skill_tool + success * 0.012 * dt)
        reward = success * 0.16
    elif action == "treat":
        success = clamp(success + agent.attachment * 0.16 + world.medicine * 0.16 - world.disease_strain * 0.12)
        world.sickness = clamp(world.sickness - success * 0.070 * dt)
        world.contamination = clamp(world.contamination - success * 0.050 * dt)
        world.disease_strain = clamp(world.disease_strain - success * 0.050 * dt)
        agent.health = clamp(agent.health + success * 0.045 * dt)
        reward = success * 0.14
    elif action == "share_pattern":
        success = clamp(success + agent.skill_teach * 0.34 + agent.wisdom * 0.14)
        if condition.teaching:
            world.teaching = clamp(world.teaching + success * 0.045 * dt)
            world.risk_memory = clamp(world.risk_memory + success * 0.030 * dt)
            world.knowledge_transfer = clamp(world.knowledge_transfer + success * 0.040 * dt)
            for other in living_agents_sample(world_agents_current, agent, rng, limit=3):
                other.skill_build = clamp(other.skill_build + agent.skill_build * 0.006 * dt)
                other.skill_tool = clamp(other.skill_tool + agent.skill_tool * 0.006 * dt)
                other.skill_harvest = clamp(other.skill_harvest + agent.skill_harvest * 0.006 * dt)
                other.wisdom = clamp(other.wisdom + success * 0.004 * dt)
        agent.skill_teach = clamp(agent.skill_teach + success * 0.012 * dt)
        reward = success * 0.13
    elif action == "inspect":
        success = clamp(success + world.visibility * 0.18 + agent.wisdom * 0.10 - world.route_hazard * 0.08)
        world.map_knowledge = clamp(world.map_knowledge + success * 0.055 * dt)
        if condition.risk_memory:
            world.risk_memory = clamp(world.risk_memory + max(0.0, world.route_hazard - 0.25) * 0.040 * dt + success * 0.012 * dt)
        world.resource_migration = clamp(world.resource_migration - success * 0.012 * dt)
        reward = success * 0.12
    elif action == "rest":
        success = clamp(world.shelter * 0.34 + world.architecture * 0.16 + agent.reserve * 0.18 + 0.28)
        agent.energy = clamp(agent.energy + success * 0.20 * dt)
        agent.health = clamp(agent.health + success * 0.025 * dt)
        agent.stress = clamp(agent.stress - success * 0.10 * dt)
        reward = success * 0.08
    else:
        world.conflict = clamp(world.conflict - success * 0.010 * dt)
        agent.fear = clamp(agent.fear - success * 0.020 * dt)
        reward = success * 0.04

    adaptive_actions = {"harvest_food", "harvest_water", "construct", "modify", "treat", "share_pattern", "inspect"}
    if action in adaptive_actions:
        quality = clamp(success * (0.55 + max(0.0, reward) * 0.40) * (0.72 + world.adaptive_pressure * 0.42))
        world.adaptation_evidence = clamp(world.adaptation_evidence + quality * 0.015 * dt)
        agent.adaptation = clamp(agent.adaptation + quality * 0.010 * dt)
        agent.wisdom = clamp(agent.wisdom + max(0.0, reward) * 0.010 * dt + success * 0.0025 * dt)

    agent.energy = clamp(agent.energy - (0.018 if action != "rest" else 0.004) * dt)
    agent.stress = clamp(agent.stress + world.conflict * 0.010 * dt + world.adaptive_pressure * 0.008 * dt - world.teaching * 0.010 * dt)


world_agents_current: List[Agent] = []


def living_agents_sample(agents: Sequence[Agent], source: Agent, rng: random.Random, limit: int) -> List[Agent]:
    peers = [agent for agent in agents if agent is not source and agent.alive]
    rng.shuffle(peers)
    return peers[:limit]


def update_agents(world: World, agents: List[Agent], condition: Condition, dt: float, rng: random.Random) -> None:
    alive = living(agents)
    for agent in alive:
        if agent.child:
            agent.hunger = clamp(agent.hunger + 0.020 * dt - world.food * 0.020 * dt)
            agent.thirst = clamp(agent.thirst + 0.022 * dt - world.water * 0.022 * dt)
            agent.health = clamp(agent.health - max(0.0, agent.hunger - 0.78) * 0.10 * dt - max(0.0, agent.thirst - 0.78) * 0.12 * dt)
            continue
        action = choose_action(agent, world, condition, rng)
        apply_action(agent, world, condition, action, dt, rng)

    for agent in alive:
        temperature_cost = abs(world.temperature - 0.58) * 0.010
        agent.hunger = clamp(agent.hunger + (0.020 + temperature_cost + agent.stress * 0.004) * dt - (world.food * 0.016 + world.food_storage * 0.008) * dt)
        agent.thirst = clamp(agent.thirst + (0.024 + max(0.0, world.temperature - 0.62) * 0.026 + agent.stress * 0.004) * dt - (world.water * 0.020 + world.waterworks * 0.008) * dt)
        agent.health = clamp(agent.health - max(0.0, agent.hunger - 0.91) * 0.55 * dt - max(0.0, agent.thirst - 0.91) * 0.70 * dt - (world.sickness + world.contamination * 0.28 + world.disease_strain * 0.12) * 0.040 * dt)
        agent.fear = clamp(agent.fear * (1.0 - (0.030 + world.risk_memory * 0.018) * dt) + (world.threat + world.route_hazard * 0.28 + world.adaptive_pressure * 0.08) * 0.052 * dt - world.shelter * 0.085 * dt)
        quality_penalty = max(0.0, 0.40 - world.shelter) + max(0.0, world.sickness - 0.38) + max(0.0, world.contamination - 0.40) * 0.50 + max(0.0, world.route_hazard - 0.45) * 0.35
        scarcity = max(0.0, agent.hunger - 0.74) * 1.35 + max(0.0, agent.thirst - 0.74) * 1.50
        agent.reserve = clamp(agent.reserve - 0.00125 * dt * (1.0 + agent.stress * 0.45 + quality_penalty + scarcity - agent.wisdom * 0.14))
        if agent.health <= 0.04 or agent.reserve <= 0.02:
            agent.alive = False


def maybe_reproduce(world: World, agents: List[Agent], condition: Condition, rng: random.Random, dt: float) -> None:
    if world.time < 6.0 or len(agents) >= 15:
        return
    if world.food < 0.46 or world.water < 0.46 or world.shelter < 0.48 or rng.random() > 0.045 * dt:
        return
    adults = [agent for agent in agents if agent.alive and not agent.child and agent.health > 0.72 and agent.energy > 0.45]
    if len(adults) < 2:
        return
    parent_a, parent_b = rng.sample(adults, 2)
    inheritance = 0.0
    if condition.teaching:
        inheritance = clamp(world.teaching * 0.18 + (parent_a.wisdom + parent_b.wisdom) * 0.04)
    child = Agent(
        health=0.74,
        energy=0.62,
        hunger=0.36,
        thirst=0.36,
        fear=0.18,
        stress=0.18,
        reserve=0.70,
        wisdom=inheritance * 0.35,
        adaptation=inheritance * 0.30,
        attachment=0.82,
        skill_build=0.06 + inheritance,
        skill_tool=0.06 + inheritance,
        skill_harvest=0.08 + inheritance,
        skill_teach=0.05 + inheritance,
        child=True,
    )
    parent_a.energy = clamp(parent_a.energy - 0.10)
    parent_b.energy = clamp(parent_b.energy - 0.08)
    parent_a.reserve = clamp(parent_a.reserve - 0.018)
    parent_b.reserve = clamp(parent_b.reserve - 0.012)
    world.births += 1
    world.knowledge_transfer = clamp(world.knowledge_transfer + inheritance * 0.60)
    agents.append(child)


def checkpoint_snapshot(world: World, agents: Sequence[Agent], label: str) -> Dict[str, object]:
    alive = living(agents)
    return {
        "label": label,
        "hours": world.time,
        "alive": len(alive),
        "total_agents": len(agents),
        "major_shocks": world.major_shocks,
        "major_shock_unlocked": world.time >= 12.0,
        "food": world.food,
        "water": world.water,
        "architecture": world.architecture,
        "tool_design": world.tool_design,
        "teaching": world.teaching,
        "risk_memory": world.risk_memory,
        "adaptation_evidence": world.adaptation_evidence,
        "adaptive_pressure": world.adaptive_pressure,
        "knowledge_transfer": world.knowledge_transfer,
        "mean_wisdom": mean(agent.wisdom for agent in alive),
        "mean_adaptation": mean(agent.adaptation for agent in alive),
        "mean_health": mean(agent.health for agent in alive),
        "mean_reserve": mean(agent.reserve for agent in alive),
    }


def run_episode(seed: int, condition: Condition, cfg: Config, *, trace: bool = False) -> tuple[EpisodeRow, List[Dict[str, object]]]:
    rng = random.Random(seed * 97 + sum(ord(ch) for ch in condition.name))
    agents = make_agents(rng, cfg.population)
    world = make_world(rng)
    global world_agents_current
    world_agents_current = agents
    baseline = {
        "architecture": world.architecture,
        "tool_design": world.tool_design,
        "teaching": world.teaching,
        "risk_memory": world.risk_memory,
    }
    checkpoints: List[Dict[str, object]] = []
    checkpoint_targets = list(CHECKPOINTS)
    alive_at_12h = cfg.population
    no_pre_gate_shock = True
    no_shock_at_12 = True

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        world.time += dt
        update_environment(world, agents, condition, dt, rng)
        pressure = pressure_breakdown(world, agents)
        alpha = min(0.08, max(0.004, dt / 0.20))
        world.adaptive_pressure = clamp(world.adaptive_pressure * (1.0 - alpha) + pressure["total"] * alpha)
        world.pressure_integral = clamp(world.pressure_integral + pressure["total"] * dt / 18.0)
        maybe_trigger_major_shock(world, rng)
        update_agents(world, agents, condition, dt, rng)
        maybe_reproduce(world, agents, condition, rng, dt)

        if world.time < 12.0 and world.major_shocks > 0:
            no_pre_gate_shock = False
        if world.time >= 12.0 and alive_at_12h == cfg.population:
            alive_at_12h = len(living(agents))
            no_shock_at_12 = world.major_shocks == 0
        while checkpoint_targets and world.time >= checkpoint_targets[0] - 1e-9:
            label = f"{checkpoint_targets.pop(0):.1f}h"
            checkpoints.append(checkpoint_snapshot(world, agents, label))

    final_alive = len(living(agents))
    total_agents = len(agents)
    architecture_delta = world.architecture - baseline["architecture"]
    tool_delta = world.tool_design - baseline["tool_design"]
    teaching_delta = world.teaching - baseline["teaching"]
    risk_delta = world.risk_memory - baseline["risk_memory"]
    survival_score = final_alive / max(1, total_agents)
    development_score = clamp(max(0.0, architecture_delta) * 0.55 + max(0.0, tool_delta) * 0.45 + max(0.0, world.waterworks - 0.16) * 0.25 + max(0.0, world.path_network - 0.12) * 0.20 + max(0.0, world.food_storage - 0.18) * 0.15)
    knowledge_score = clamp(world.knowledge_transfer * 1.30 + max(0.0, teaching_delta) * 1.10 + mean(agent.wisdom for agent in living(agents)) * 0.18)
    post_shock_score = clamp((1.0 if world.major_shocks else 0.0) * 0.30 + survival_score * 0.38 + world.adaptation_evidence * 0.36 + world.risk_memory * 0.16)
    long_horizon_score = clamp(survival_score * 0.30 + development_score * 0.24 + knowledge_score * 0.18 + post_shock_score * 0.18 + world.adaptation_evidence * 0.10)
    row = EpisodeRow(
        seed=seed,
        condition=condition.name,
        final_alive=final_alive,
        total_agents=total_agents,
        alive_at_12h=alive_at_12h,
        no_major_shock_before_12h=no_pre_gate_shock,
        no_major_shock_at_12h=no_shock_at_12,
        post_gate_shock=world.major_shocks > 0,
        major_shocks=world.major_shocks,
        first_shock_hour=world.first_shock_hour or 0.0,
        food_final=world.food,
        water_final=world.water,
        architecture_delta=architecture_delta,
        tool_design_delta=tool_delta,
        teaching_delta=teaching_delta,
        risk_memory_delta=risk_delta,
        adaptation_evidence=world.adaptation_evidence,
        pressure_integral=world.pressure_integral,
        births=world.births,
        knowledge_transfer=world.knowledge_transfer,
        survival_score=survival_score,
        development_score=development_score,
        knowledge_score=knowledge_score,
        post_shock_score=post_shock_score,
        long_horizon_score=long_horizon_score,
    )
    return row, checkpoints if trace else []


def summarize(rows: Sequence[EpisodeRow]) -> List[SummaryRow]:
    by_condition: Dict[str, List[EpisodeRow]] = {}
    for row in rows:
        by_condition.setdefault(row.condition, []).append(row)
    summary: List[SummaryRow] = []
    for condition, items in sorted(by_condition.items()):
        summary.append(
            SummaryRow(
                condition=condition,
                mean_long_horizon_score=mean(row.long_horizon_score for row in items),
                mean_survival_score=mean(row.survival_score for row in items),
                mean_development_score=mean(row.development_score for row in items),
                mean_knowledge_score=mean(row.knowledge_score for row in items),
                mean_post_shock_score=mean(row.post_shock_score for row in items),
                mean_final_alive=mean(row.final_alive for row in items),
                mean_alive_at_12h=mean(row.alive_at_12h for row in items),
                mean_adaptation_evidence=mean(row.adaptation_evidence for row in items),
                mean_architecture_delta=mean(row.architecture_delta for row in items),
                mean_tool_design_delta=mean(row.tool_design_delta for row in items),
                mean_knowledge_transfer=mean(row.knowledge_transfer for row in items),
                no_major_shock_before_12h_rate=mean(1.0 if row.no_major_shock_before_12h else 0.0 for row in items),
                post_gate_shock_rate=mean(1.0 if row.post_gate_shock else 0.0 for row in items),
            )
        )
    return summary


def verdict_from_summary(summary: Sequence[SummaryRow]) -> VerdictRow:
    by_name = {row.condition: row for row in summary}
    full = by_name["integrated_long_horizon"]
    reactive = by_name["reactive_survival_only"]
    no_teaching = by_name["no_teaching_transmission"]
    no_risk = by_name["no_risk_memory"]
    no_infra = by_name["no_infrastructure_memory"]
    no_tool = by_name["no_tool_improvement"]
    no_arbitration = by_name["no_adaptive_arbitration"]
    losses = {
        "reactive": full.mean_long_horizon_score - reactive.mean_long_horizon_score,
        "teaching": full.mean_knowledge_score - no_teaching.mean_knowledge_score,
        "risk": full.mean_post_shock_score - no_risk.mean_post_shock_score,
        "infrastructure": full.mean_development_score - no_infra.mean_development_score,
        "tool": full.mean_development_score - no_tool.mean_development_score,
        "arbitration": full.mean_long_horizon_score - no_arbitration.mean_long_horizon_score,
    }
    supports_development = (
        full.no_major_shock_before_12h_rate == 1.0
        and full.post_gate_shock_rate == 1.0
        and full.mean_alive_at_12h >= 8.0
        and full.mean_final_alive >= 7.0
        and full.mean_architecture_delta >= 0.18
        and full.mean_tool_design_delta >= 0.30
        and full.mean_adaptation_evidence >= 0.20
    )
    supports_ablation = (
        losses["reactive"] >= 0.12
        and losses["teaching"] >= 0.08
        and losses["risk"] >= 0.025
        and full.mean_architecture_delta - no_infra.mean_architecture_delta >= 0.20
        and full.mean_tool_design_delta - no_tool.mean_tool_design_delta >= 0.25
        and losses["arbitration"] >= 0.015
    )
    return VerdictRow(
        integrated_score=full.mean_long_horizon_score,
        reactive_score=reactive.mean_long_horizon_score,
        no_teaching_score=no_teaching.mean_long_horizon_score,
        no_risk_memory_score=no_risk.mean_long_horizon_score,
        no_infrastructure_memory_score=no_infra.mean_long_horizon_score,
        no_tool_improvement_score=no_tool.mean_long_horizon_score,
        no_adaptive_arbitration_score=no_arbitration.mean_long_horizon_score,
        reactive_loss=losses["reactive"],
        teaching_loss=losses["teaching"],
        risk_memory_loss=losses["risk"],
        infrastructure_memory_loss=losses["infrastructure"],
        tool_improvement_loss=losses["tool"],
        adaptive_arbitration_loss=losses["arbitration"],
        shock_gate_pass_rate=full.no_major_shock_before_12h_rate,
        post_gate_shock_rate=full.post_gate_shock_rate,
        survival_at_12h=full.mean_alive_at_12h,
        supports_long_horizon_development=supports_development,
        supports_ablation_specificity=supports_ablation,
        verdict="pass" if supports_development and supports_ablation else "partial_or_failed",
    )


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = [asdict(row) for row in rows]
    if not data:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(data[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def write_js(path: Path, variable: str, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"window.{variable} = {json.dumps(payload, indent=2)};\n", encoding="utf-8")


def write_artifacts(rows: Sequence[EpisodeRow], summary: Sequence[SummaryRow], verdict: VerdictRow, trace: List[Dict[str, object]], cfg: Config) -> Dict[str, object]:
    payload = {
        "config": {
            "seeds": list(cfg.seeds),
            "hours": cfg.hours,
            "step_hours": cfg.step_hours,
            "population": cfg.population,
            "trace_seed": cfg.trace_seed,
        },
        "summary": [asdict(row) for row in summary],
        "verdict": asdict(verdict),
        "trace": trace,
        "notes": {
            "claim": "headless long-horizon adaptation verifier",
            "not_claimed": "subjective consciousness, open-ended civilization, or closed-loop deep RL",
        },
    }
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_long_horizon_adaptation_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_long_horizon_adaptation_summary.csv", summary)
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_long_horizon_adaptation_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / "ssrm_3d_long_horizon_adaptation_results.json", payload)
    write_json(ARTIFACT_DIR / "ssrm_3d_long_horizon_adaptation_trace.json", trace)
    write_js(ARTIFACT_DIR / "ssrm_3d_long_horizon_adaptation_results.js", "SSRM_3D_LONG_HORIZON_ADAPTATION_RESULTS", payload)
    write_js(ARTIFACT_DIR / "ssrm_3d_long_horizon_adaptation_trace.js", "SSRM_3D_LONG_HORIZON_ADAPTATION_TRACE", trace)
    return payload


def run_benchmark(cfg: Config) -> Dict[str, object]:
    rows: List[EpisodeRow] = []
    trace: List[Dict[str, object]] = []
    for seed in cfg.seeds:
        for condition in CONDITIONS:
            row, maybe_trace = run_episode(seed, condition, cfg, trace=(seed == cfg.trace_seed and condition.name == "integrated_long_horizon"))
            rows.append(row)
            if maybe_trace:
                trace = maybe_trace
    summary = summarize(rows)
    verdict = verdict_from_summary(summary)
    payload = write_artifacts(rows, summary, verdict, trace, cfg)
    return payload


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", default="20260708,20260709,20260710,20260711,20260712")
    parser.add_argument("--hours", type=float, default=14.5)
    parser.add_argument("--step-hours", type=float, default=0.05)
    parser.add_argument("--population", type=int, default=10)
    parser.add_argument("--trace-seed", type=int, default=20260708)
    args = parser.parse_args()
    seeds = tuple(int(part.strip()) for part in args.seeds.split(",") if part.strip())
    return Config(
        seeds=seeds,
        hours=args.hours,
        step_hours=args.step_hours,
        population=args.population,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({"verdict": payload["verdict"], "summary": payload["summary"]}, indent=2))
    return 0 if payload["verdict"]["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
