#!/usr/bin/env python3
"""Hidden-regime adaptation benchmark for SSRM-3D.

This benchmark adds a scientific pressure layer to the long-horizon verifier:
the world changes its causal rules after the 12h development gate, but agents
do not receive the regime label. They only receive noisy consequences such as
illness, bad yields, tool failures, weather exposure, and social fracture.

The result is still a designed simulation benchmark. It is not a claim of
subjective consciousness or open-ended civilization.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import statistics
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Sequence


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"

CHECKPOINTS = (1.0, 6.0, 12.0, 12.5, 14.5, 16.0)
REGIME_NAMES = (
    "contaminated_water",
    "cold_wet_season",
    "crop_blight",
    "tool_fatigue",
    "trust_fracture",
)
REGIME_CHANNEL = {
    "contaminated_water": "water",
    "cold_wet_season": "weather",
    "crop_blight": "food",
    "tool_fatigue": "tool",
    "trust_fracture": "social",
}
TARGETED_ACTIONS = {
    "contaminated_water": {"filter_water", "quarantine", "inspect"},
    "cold_wet_season": {"reinforce_shelter", "construct", "inspect"},
    "crop_blight": {"diversify_food", "inspect", "teach"},
    "tool_fatigue": {"redesign_tools", "inspect", "teach"},
    "trust_fracture": {"mediate", "teach", "inspect"},
}


@dataclass(frozen=True)
class Config:
    seeds: Sequence[int]
    hours: float = 16.0
    step_hours: float = 0.05
    population: int = 10
    trace_seed: int = 20260713


@dataclass(frozen=True)
class Condition:
    name: str
    description: str
    regime_inference: bool = True
    teaching: bool = True
    reputation_influence: bool = True
    sanitation_memory: bool = True
    weather_sensors: bool = True
    tool_adaptation: bool = True
    infrastructure_memory: bool = True
    adaptive_arbitration: bool = True


CONDITIONS = (
    Condition("integrated_hidden_regime", "full hidden-regime inference and adaptation channels"),
    Condition(
        "reactive_survival_only",
        "immediate survival without persistent regime, social, or development channels",
        regime_inference=False,
        teaching=False,
        reputation_influence=False,
        sanitation_memory=False,
        weather_sensors=False,
        tool_adaptation=False,
        infrastructure_memory=False,
        adaptive_arbitration=False,
    ),
    Condition("no_regime_inference", "symptoms are visible but not integrated into a regime belief", regime_inference=False),
    Condition("no_teaching_transmission", "teaching and cultural transfer removed", teaching=False),
    Condition("no_reputation_influence", "influence, trust, and convention pressure cannot stabilize socially", reputation_influence=False),
    Condition("no_sanitation_memory", "water and illness responses cannot persist as sanitation practice", sanitation_memory=False),
    Condition("no_weather_sensors", "weather exposure is not available as a reliable sensor", weather_sensors=False),
    Condition("no_tool_adaptation", "tools can be used but not redesigned after failures", tool_adaptation=False),
)


@dataclass
class Agent:
    health: float
    energy: float
    hunger: float
    thirst: float
    stress: float
    cleanliness: float
    reserve: float
    wisdom: float
    adaptation: float
    reliability: float
    reputation: float
    influence: float
    skill_build: float
    skill_tool: float
    skill_forage: float
    skill_care: float
    skill_teach: float
    child: bool = False
    alive: bool = True


@dataclass
class World:
    time: float
    regime_name: str
    first_regime_hour: float
    food: float
    water: float
    materials: float
    medicine: float
    shelter: float
    architecture: float
    tool_quality: float
    tool_design: float
    path_network: float
    waterworks: float
    sanitation: float
    garden: float
    food_storage: float
    clinic: float
    trust: float
    conflict: float
    social_inequality: float
    reputation_accuracy: float
    symbol_convergence: float
    teaching: float
    risk_memory: float
    culture_memory: float
    knowledge_transfer: float
    contamination: float
    sickness: float
    weather_exposure: float
    storminess: float
    resource_shift: float
    route_hazard: float
    hidden_pressure: float
    adaptation_evidence: float
    pressure_integral: float
    births: int
    deaths: int
    action_counts: Dict[str, int] = field(default_factory=dict)
    targeted_action_count: int = 0
    post_regime_action_count: int = 0
    regime_anomalies: Dict[str, float] = field(default_factory=lambda: {
        "water": 0.0,
        "weather": 0.0,
        "food": 0.0,
        "tool": 0.0,
        "social": 0.0,
    })
    beliefs: Dict[str, float] = field(default_factory=lambda: {
        "water": 0.10,
        "weather": 0.10,
        "food": 0.10,
        "tool": 0.10,
        "social": 0.10,
    })


@dataclass(frozen=True)
class EpisodeRow:
    seed: int
    regime: str
    condition: str
    final_alive: int
    total_agents: int
    alive_at_12h: int
    no_major_regime_before_12h: bool
    hidden_regime_after_12h: bool
    first_regime_hour: float
    deaths: int
    births: int
    final_food: float
    final_water: float
    final_trust: float
    final_symbol_convergence: float
    architecture_delta: float
    tool_design_delta: float
    sanitation_delta: float
    teaching_delta: float
    knowledge_transfer: float
    adaptation_evidence: float
    inference_score: float
    response_score: float
    targeted_response_rate: float
    survival_score: float
    development_score: float
    culture_score: float
    long_horizon_score: float


@dataclass(frozen=True)
class SummaryRow:
    condition: str
    mean_long_horizon_score: float
    mean_survival_score: float
    mean_development_score: float
    mean_culture_score: float
    mean_inference_score: float
    mean_response_score: float
    mean_targeted_response_rate: float
    mean_final_alive: float
    mean_alive_at_12h: float
    mean_architecture_delta: float
    mean_tool_design_delta: float
    mean_sanitation_delta: float
    mean_knowledge_transfer: float
    mean_symbol_convergence: float
    no_major_regime_before_12h_rate: float
    hidden_regime_after_12h_rate: float


@dataclass(frozen=True)
class RegimeSummaryRow:
    regime: str
    condition: str
    mean_long_horizon_score: float
    mean_inference_score: float
    mean_response_score: float
    mean_targeted_response_rate: float


@dataclass(frozen=True)
class VerdictRow:
    integrated_score: float
    reactive_score: float
    no_regime_inference_score: float
    no_teaching_score: float
    no_reputation_influence_score: float
    no_sanitation_memory_score: float
    no_weather_sensors_score: float
    no_tool_adaptation_score: float
    reactive_loss: float
    inference_loss: float
    teaching_loss: float
    reputation_loss: float
    sanitation_loss: float
    weather_loss: float
    tool_loss: float
    shock_gate_pass_rate: float
    hidden_regime_rate: float
    mean_inference_score: float
    mean_response_score: float
    mean_targeted_response_rate: float
    supports_hidden_regime_adaptation: bool
    supports_ablation_specificity: bool
    verdict: str


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def living(agents: Sequence[Agent]) -> List[Agent]:
    return [agent for agent in agents if agent.alive]


def make_agents(rng: random.Random, population: int) -> List[Agent]:
    agents: List[Agent] = []
    for _ in range(population):
        stamina = 0.36 + rng.random() * 0.42
        dexterity = 0.34 + rng.random() * 0.44
        sociability = 0.32 + rng.random() * 0.48
        care = 0.30 + rng.random() * 0.50
        agents.append(
            Agent(
                health=0.88 + rng.random() * 0.08,
                energy=0.74 + rng.random() * 0.14,
                hunger=0.20 + rng.random() * 0.12,
                thirst=0.20 + rng.random() * 0.12,
                stress=0.12 + rng.random() * 0.12,
                cleanliness=0.62 + rng.random() * 0.20,
                reserve=0.82 + rng.random() * 0.14,
                wisdom=0.10 + rng.random() * 0.10,
                adaptation=0.10 + rng.random() * 0.08,
                reliability=0.42 + stamina * 0.24 + rng.random() * 0.10,
                reputation=0.42 + sociability * 0.20 + rng.random() * 0.10,
                influence=0.30,
                skill_build=0.10 + stamina * 0.10 + rng.random() * 0.08,
                skill_tool=0.10 + dexterity * 0.12 + rng.random() * 0.08,
                skill_forage=0.12 + dexterity * 0.11 + rng.random() * 0.08,
                skill_care=0.10 + care * 0.13 + rng.random() * 0.08,
                skill_teach=0.09 + sociability * 0.12 + rng.random() * 0.08,
            )
        )
    update_agent_influence(agents, reputation_enabled=True)
    return agents


def regime_for_seed(seed: int) -> str:
    return REGIME_NAMES[seed % len(REGIME_NAMES)]


def make_world(seed: int, rng: random.Random) -> World:
    return World(
        time=0.0,
        regime_name=regime_for_seed(seed),
        first_regime_hour=12.35 + rng.random() * 0.55,
        food=0.82,
        water=0.82,
        materials=0.60,
        medicine=0.42,
        shelter=0.52,
        architecture=0.18,
        tool_quality=0.48,
        tool_design=0.16,
        path_network=0.14,
        waterworks=0.18,
        sanitation=0.16,
        garden=0.30,
        food_storage=0.18,
        clinic=0.12,
        trust=0.58,
        conflict=0.10,
        social_inequality=0.14,
        reputation_accuracy=0.38,
        symbol_convergence=0.20,
        teaching=0.09,
        risk_memory=0.10,
        culture_memory=0.08,
        knowledge_transfer=0.0,
        contamination=0.12,
        sickness=0.10,
        weather_exposure=0.14,
        storminess=0.12,
        resource_shift=0.12,
        route_hazard=0.16,
        hidden_pressure=0.12,
        adaptation_evidence=0.0,
        pressure_integral=0.0,
        births=0,
        deaths=0,
    )


def update_agent_influence(agents: Sequence[Agent], reputation_enabled: bool) -> None:
    for agent in agents:
        if not agent.alive:
            continue
        if reputation_enabled:
            agent.influence = clamp(
                agent.reputation * 0.26
                + agent.reliability * 0.20
                + agent.cleanliness * 0.12
                + agent.wisdom * 0.12
                + agent.adaptation * 0.12
                + max(agent.skill_build, agent.skill_tool, agent.skill_forage, agent.skill_care, agent.skill_teach) * 0.18
            )
        else:
            agent.influence = clamp(0.34 + agent.reliability * 0.06 + agent.skill_teach * 0.05)


def regime_active(world: World) -> bool:
    return world.time >= world.first_regime_hour


def symptom_channels(world: World, condition: Condition, rng: random.Random) -> Dict[str, float]:
    weather_signal = world.weather_exposure + world.storminess * 0.36 + world.regime_anomalies["weather"] * 0.86
    if not condition.weather_sensors:
        weather_signal = weather_signal * 0.25 + rng.random() * 0.04
    signals = {
        "water": clamp(world.contamination * 0.72 + world.sickness * 0.28 + max(0.0, 0.56 - world.water) * 0.16 + world.regime_anomalies["water"] * 0.86 + rng.random() * 0.025),
        "weather": clamp(weather_signal + max(0.0, 0.54 - world.shelter) * 0.12 + rng.random() * 0.025),
        "food": clamp(world.resource_shift * 0.48 + max(0.0, 0.56 - world.food) * 0.34 + max(0.0, 0.48 - world.garden) * 0.12 + world.regime_anomalies["food"] * 0.86 + rng.random() * 0.025),
        "tool": clamp(max(0.0, 0.62 - world.tool_quality) * 0.52 + max(0.0, 0.46 - world.tool_design) * 0.20 + max(0.0, 0.48 - world.materials) * 0.12 + world.regime_anomalies["tool"] * 0.86 + rng.random() * 0.025),
        "social": clamp(world.conflict * 0.40 + max(0.0, 0.64 - world.trust) * 0.34 + world.social_inequality * 0.26 + world.regime_anomalies["social"] * 0.86 + rng.random() * 0.025),
    }
    return signals


def update_beliefs(world: World, condition: Condition, signals: Dict[str, float], dt: float) -> None:
    if not condition.regime_inference:
        for key in world.beliefs:
            decay = 0.030 * dt
            world.beliefs[key] = clamp(world.beliefs[key] * (1.0 - decay) + 0.08 * decay)
        return
    teaching_gain = world.teaching if condition.teaching else 0.0
    culture_gain = world.culture_memory if condition.teaching else 0.0
    risk_gain = world.risk_memory
    learning_rate = clamp(0.130 + teaching_gain * 0.048 + culture_gain * 0.028 + risk_gain * 0.024, high=0.34)
    for key, signal in signals.items():
        prior = world.beliefs[key]
        contrast = signal - mean(value for name, value in signals.items() if name != key)
        evidence = clamp(signal * 0.78 + max(0.0, contrast) * 0.34)
        world.beliefs[key] = clamp(prior * (1.0 - learning_rate * dt) + evidence * learning_rate * dt)
    if condition.teaching:
        dominant = max(world.beliefs, key=world.beliefs.get)
        world.risk_memory = clamp(world.risk_memory + world.beliefs[dominant] * 0.006 * dt)


def apply_baseline_environment(world: World, agents: Sequence[Agent], condition: Condition, dt: float, rng: random.Random) -> None:
    alive = living(agents)
    population = len(alive)
    day = max(0.0, math.sin((world.time % 2.4) / 2.4 * math.pi))
    seasonal = math.sin(world.time / 18.0 * math.pi * 2.0)
    storm = 1.0 if rng.random() < (0.020 + world.storminess * 0.018) * dt else 0.0
    world.storminess = clamp(0.10 + abs(seasonal) * 0.16 + storm * 0.22)
    weather_sensor_factor = 1.0 if condition.weather_sensors else 0.35
    world.weather_exposure = clamp(0.10 + world.storminess * 0.24 - world.shelter * 0.12 - world.architecture * 0.08 + (1.0 - weather_sensor_factor) * 0.08)
    world.resource_shift = clamp(0.10 + abs(math.sin(world.time / 5.9 + 0.4)) * 0.24 + world.route_hazard * 0.08 - world.path_network * 0.08)
    cleanliness = mean(agent.cleanliness for agent in alive)
    sanitation_factor = world.sanitation if condition.sanitation_memory else world.sanitation * 0.32
    infrastructure_factor = 1.0 if condition.infrastructure_memory else 0.38
    for key in world.regime_anomalies:
        world.regime_anomalies[key] = clamp(world.regime_anomalies[key] * (1.0 - 0.080 * dt))
    world.contamination = clamp(world.contamination + (population * (1.0 - cleanliness) * 0.0018 + storm * 0.018 + world.sickness * 0.010) * dt - sanitation_factor * 0.045 * dt)
    world.sickness = clamp(world.sickness + (world.contamination * 0.026 + world.weather_exposure * 0.010) * dt - (world.clinic + sanitation_factor + world.medicine) * 0.026 * dt)
    world.route_hazard = clamp(0.12 + world.storminess * 0.12 + world.resource_shift * 0.10 + world.conflict * 0.06 - world.path_network * 0.18 - world.risk_memory * 0.10)
    world.conflict = clamp(world.conflict + max(0.0, 0.42 - min(world.food, world.water)) * 0.070 * dt + world.social_inequality * 0.016 * dt - world.trust * 0.026 * dt)
    if condition.reputation_influence:
        world.reputation_accuracy = clamp(world.reputation_accuracy + world.trust * 0.018 * dt + world.teaching * 0.016 * dt - world.conflict * 0.012 * dt)
        world.symbol_convergence = clamp(world.symbol_convergence + world.reputation_accuracy * 0.018 * dt + mean(agent.influence for agent in alive) * 0.012 * dt - world.conflict * 0.020 * dt)
        world.social_inequality = clamp(world.social_inequality + max(0.0, 0.42 - world.trust) * 0.018 * dt - world.reputation_accuracy * 0.016 * dt)
    else:
        world.reputation_accuracy = clamp(world.reputation_accuracy - 0.014 * dt + rng.random() * 0.002)
        world.symbol_convergence = clamp(world.symbol_convergence - 0.018 * dt + world.teaching * 0.004 * dt)
        world.social_inequality = clamp(world.social_inequality + max(0.0, 0.58 - world.trust) * 0.020 * dt)
    world.food = clamp(world.food - population * 0.0048 * dt + (world.garden + world.food_storage * 0.20) * (0.13 - world.resource_shift * 0.035) * dt - world.contamination * 0.006 * dt)
    world.water = clamp(world.water - population * 0.0051 * dt + world.waterworks * (0.11 + day * 0.015) * dt - world.contamination * 0.008 * dt)
    world.materials = clamp(world.materials + (world.path_network + world.tool_quality) * 0.016 * dt - population * 0.0018 * dt)
    world.shelter = clamp(world.shelter - (0.006 + storm * 0.014 - world.architecture * 0.008) * dt)
    world.tool_quality = clamp(world.tool_quality - (0.006 + population * 0.0010 - world.tool_design * 0.004) * dt)
    if not condition.infrastructure_memory:
        world.architecture = clamp(world.architecture - 0.010 * dt)
        world.path_network = clamp(world.path_network - 0.012 * dt)
        world.waterworks = clamp(world.waterworks - 0.010 * dt)
        world.food_storage = clamp(world.food_storage - 0.010 * dt)


def apply_hidden_regime(world: World, condition: Condition, dt: float) -> None:
    if not regime_active(world):
        return
    if world.regime_name == "contaminated_water":
        world.regime_anomalies["water"] = clamp(world.regime_anomalies["water"] + 0.130 * dt)
        world.contamination = clamp(world.contamination + 0.060 * dt)
        world.sickness = clamp(world.sickness + 0.034 * dt)
        world.water = clamp(world.water - 0.015 * dt)
        world.hidden_pressure = clamp(world.hidden_pressure + 0.040 * dt)
    elif world.regime_name == "cold_wet_season":
        sensor_gap = 1.0 if condition.weather_sensors else 1.85
        world.regime_anomalies["weather"] = clamp(world.regime_anomalies["weather"] + 0.130 * dt)
        world.weather_exposure = clamp(world.weather_exposure + 0.060 * sensor_gap * dt)
        world.storminess = clamp(world.storminess + 0.036 * sensor_gap * dt)
        world.shelter = clamp(world.shelter - 0.030 * sensor_gap * dt)
        world.route_hazard = clamp(world.route_hazard + 0.020 * sensor_gap * dt)
        world.hidden_pressure = clamp(world.hidden_pressure + 0.036 * sensor_gap * dt)
    elif world.regime_name == "crop_blight":
        world.regime_anomalies["food"] = clamp(world.regime_anomalies["food"] + 0.130 * dt)
        world.resource_shift = clamp(world.resource_shift + 0.052 * dt)
        world.food = clamp(world.food - 0.025 * dt)
        world.garden = clamp(world.garden - 0.014 * dt)
        world.contamination = clamp(world.contamination + 0.012 * dt)
        world.hidden_pressure = clamp(world.hidden_pressure + 0.038 * dt)
    elif world.regime_name == "tool_fatigue":
        world.regime_anomalies["tool"] = clamp(world.regime_anomalies["tool"] + 0.130 * dt)
        world.tool_quality = clamp(world.tool_quality - 0.050 * dt)
        world.materials = clamp(world.materials - 0.010 * dt)
        world.route_hazard = clamp(world.route_hazard + 0.012 * dt)
        world.hidden_pressure = clamp(world.hidden_pressure + 0.034 * dt)
    elif world.regime_name == "trust_fracture":
        world.regime_anomalies["social"] = clamp(world.regime_anomalies["social"] + 0.130 * dt)
        world.trust = clamp(world.trust - 0.040 * dt)
        world.conflict = clamp(world.conflict + 0.044 * dt)
        world.social_inequality = clamp(world.social_inequality + 0.028 * dt)
        world.symbol_convergence = clamp(world.symbol_convergence - 0.020 * dt)
        world.hidden_pressure = clamp(world.hidden_pressure + 0.038 * dt)
    if not condition.adaptive_arbitration:
        world.hidden_pressure = clamp(world.hidden_pressure + 0.018 * dt)


def dominant_belief(world: World) -> str:
    return max(world.beliefs, key=world.beliefs.get)


def choose_action(agent: Agent, world: World, condition: Condition, rng: random.Random) -> str:
    urgent = max(
        agent.hunger,
        agent.thirst,
        max(0.0, 0.42 - world.food) * 1.35,
        max(0.0, 0.42 - world.water) * 1.45,
        max(0.0, 0.40 - agent.health) * 1.20,
        max(0.0, 0.26 - agent.energy) * 1.25,
    )
    if condition.name == "reactive_survival_only":
        if agent.energy < 0.26 or agent.health < 0.46:
            return "rest"
        return "harvest_water" if world.water < world.food or agent.thirst > agent.hunger else "harvest_food"

    if not condition.adaptive_arbitration:
        roll = rng.random()
        if agent.energy < 0.22 or agent.health < 0.42:
            return "rest"
        if roll < 0.28:
            return "inspect"
        if roll < 0.46:
            return "teach"
        if roll < 0.62:
            return "construct"
        if roll < 0.78:
            return "mediate"
        return "harvest_water" if rng.random() < 0.5 else "harvest_food"

    if urgent > 0.70:
        if agent.energy < 0.22 or agent.health < 0.42:
            return "rest"
        return "harvest_water" if world.water < world.food or agent.thirst > agent.hunger else "harvest_food"

    belief = dominant_belief(world)
    confidence = world.beliefs[belief]
    if confidence > 0.30 or world.hidden_pressure > 0.32:
        if belief == "water":
            return "filter_water" if condition.sanitation_memory else "harvest_water"
        if belief == "weather":
            return "reinforce_shelter" if condition.weather_sensors else "construct"
        if belief == "food":
            return "diversify_food"
        if belief == "tool":
            return "redesign_tools" if condition.tool_adaptation else "construct"
        if belief == "social":
            return "mediate" if condition.reputation_influence else "teach"

    if world.sickness + world.contamination > 0.56 and condition.sanitation_memory:
        return "filter_water"
    if world.tool_quality < 0.44 and condition.tool_adaptation:
        return "redesign_tools"
    if world.shelter < 0.56 or world.architecture < 0.56 or world.waterworks < 0.44:
        return "construct"
    if condition.teaching and (world.teaching < 0.62 or world.culture_memory < 0.50) and rng.random() < 0.55:
        return "teach"
    if world.conflict > 0.34 or world.trust < 0.52:
        return "mediate"
    if world.food < 0.58 or world.water < 0.58:
        return "harvest_water" if world.water < world.food else "harvest_food"
    if agent.energy < 0.38 or agent.stress > 0.60:
        return "rest"
    return rng.choice(("inspect", "construct", "redesign_tools", "diversify_food", "teach", "mediate", "rest"))


def action_success(agent: Agent, world: World, condition: Condition, action: str, rng: random.Random) -> float:
    tool_factor = world.tool_quality * 0.18 + world.tool_design * 0.16
    teaching_factor = world.teaching * 0.08 if condition.teaching else 0.0
    social_factor = agent.influence * 0.08 if condition.reputation_influence else 0.02
    base = agent.energy * 0.20 + agent.health * 0.18 + tool_factor + teaching_factor + social_factor + rng.random() * 0.12
    if action in {"construct", "reinforce_shelter"}:
        base += agent.skill_build * 0.28 + world.materials * 0.10
    elif action == "redesign_tools":
        base += agent.skill_tool * 0.34 + world.materials * 0.10
    elif action in {"harvest_food", "harvest_water", "diversify_food"}:
        base += agent.skill_forage * 0.30 + world.path_network * 0.10 - world.route_hazard * 0.08
    elif action in {"filter_water", "quarantine"}:
        base += agent.skill_care * 0.28 + world.clinic * 0.10 + world.medicine * 0.12
    elif action in {"teach", "mediate"}:
        base += agent.skill_teach * 0.28 + agent.reputation * 0.12 + agent.wisdom * 0.10
    elif action == "inspect":
        base += agent.wisdom * 0.12 + world.risk_memory * 0.10
    return clamp(base)


def count_action(world: World, action: str) -> None:
    world.action_counts[action] = world.action_counts.get(action, 0) + 1
    if regime_active(world):
        world.post_regime_action_count += 1
        if action in TARGETED_ACTIONS[world.regime_name]:
            world.targeted_action_count += 1


def apply_action(agent: Agent, world: World, condition: Condition, action: str, dt: float, rng: random.Random) -> None:
    count_action(world, action)
    success = action_success(agent, world, condition, action, rng)
    reward = 0.0
    persistence = 1.0 if condition.infrastructure_memory else 0.30
    sanitation_persistence = 1.0 if condition.sanitation_memory else 0.26

    if action == "harvest_food":
        gain = (0.018 + success * 0.050 + world.garden * 0.010 + world.food_storage * 0.012) * dt
        world.food = clamp(world.food + gain)
        agent.hunger = clamp(agent.hunger - success * 0.15 * dt)
        agent.skill_forage = clamp(agent.skill_forage + success * 0.010 * dt)
        reward = gain * 5.0
    elif action == "harvest_water":
        gain = (0.020 + success * 0.055 + world.waterworks * 0.018) * dt
        world.water = clamp(world.water + gain)
        agent.thirst = clamp(agent.thirst - success * 0.16 * dt)
        agent.skill_forage = clamp(agent.skill_forage + success * 0.010 * dt)
        reward = gain * 5.0
    elif action == "construct":
        world.materials = clamp(world.materials - success * 0.016 * dt)
        world.shelter = clamp(world.shelter + success * 0.038 * persistence * dt)
        world.architecture = clamp(world.architecture + success * 0.030 * persistence * dt)
        world.path_network = clamp(world.path_network + success * 0.026 * persistence * dt)
        world.waterworks = clamp(world.waterworks + success * 0.022 * persistence * dt)
        world.food_storage = clamp(world.food_storage + success * 0.022 * persistence * dt)
        agent.skill_build = clamp(agent.skill_build + success * 0.012 * dt)
        reward = success * 0.16
    elif action == "reinforce_shelter":
        world.materials = clamp(world.materials - success * 0.018 * dt)
        world.shelter = clamp(world.shelter + success * 0.060 * persistence * dt)
        world.architecture = clamp(world.architecture + success * 0.044 * persistence * dt)
        world.weather_exposure = clamp(world.weather_exposure - success * 0.050 * dt)
        world.path_network = clamp(world.path_network + success * 0.018 * persistence * dt)
        agent.skill_build = clamp(agent.skill_build + success * 0.014 * dt)
        reward = success * 0.19
    elif action == "redesign_tools":
        world.materials = clamp(world.materials - success * 0.014 * dt)
        if condition.tool_adaptation:
            world.tool_design = clamp(world.tool_design + success * 0.050 * dt)
            world.tool_quality = clamp(world.tool_quality + success * 0.060 * dt)
        else:
            world.tool_quality = clamp(world.tool_quality + success * 0.012 * dt)
        agent.skill_tool = clamp(agent.skill_tool + success * 0.014 * dt)
        reward = success * 0.18
    elif action == "filter_water":
        world.materials = clamp(world.materials - success * 0.010 * dt)
        world.sanitation = clamp(world.sanitation + success * 0.060 * sanitation_persistence * dt)
        world.waterworks = clamp(world.waterworks + success * 0.034 * sanitation_persistence * dt)
        world.contamination = clamp(world.contamination - success * 0.076 * dt)
        world.sickness = clamp(world.sickness - success * 0.030 * dt)
        agent.cleanliness = clamp(agent.cleanliness + success * 0.030 * dt)
        agent.skill_care = clamp(agent.skill_care + success * 0.012 * dt)
        reward = success * 0.20
    elif action == "quarantine":
        world.clinic = clamp(world.clinic + success * 0.036 * dt)
        world.sickness = clamp(world.sickness - success * 0.070 * dt)
        world.conflict = clamp(world.conflict - success * 0.020 * dt)
        agent.skill_care = clamp(agent.skill_care + success * 0.012 * dt)
        reward = success * 0.17
    elif action == "diversify_food":
        world.materials = clamp(world.materials - success * 0.010 * dt)
        world.garden = clamp(world.garden + success * 0.048 * persistence * dt)
        world.food_storage = clamp(world.food_storage + success * 0.040 * persistence * dt)
        world.resource_shift = clamp(world.resource_shift - success * 0.032 * dt)
        world.food = clamp(world.food + success * 0.020 * dt)
        agent.skill_forage = clamp(agent.skill_forage + success * 0.012 * dt)
        reward = success * 0.19
    elif action == "teach":
        if condition.teaching:
            influence = mean(peer.influence for peer in living(current_agents))
            world.teaching = clamp(world.teaching + success * (0.040 + influence * 0.018) * dt)
            world.culture_memory = clamp(world.culture_memory + success * 0.050 * dt)
            world.risk_memory = clamp(world.risk_memory + success * 0.030 * dt)
            world.knowledge_transfer = clamp(world.knowledge_transfer + success * 0.044 * dt)
            world.symbol_convergence = clamp(world.symbol_convergence + success * (0.024 if condition.reputation_influence else 0.006) * dt)
            spread_skill(agent, success, dt)
        agent.skill_teach = clamp(agent.skill_teach + success * 0.012 * dt)
        reward = success * 0.15
    elif action == "mediate":
        if condition.reputation_influence:
            world.trust = clamp(world.trust + success * 0.052 * dt)
            world.reputation_accuracy = clamp(world.reputation_accuracy + success * 0.046 * dt)
            world.symbol_convergence = clamp(world.symbol_convergence + success * 0.040 * dt)
            world.conflict = clamp(world.conflict - success * 0.060 * dt)
            world.social_inequality = clamp(world.social_inequality - success * 0.032 * dt)
        else:
            world.trust = clamp(world.trust + success * 0.010 * dt)
            world.conflict = clamp(world.conflict - success * 0.010 * dt)
        agent.skill_teach = clamp(agent.skill_teach + success * 0.008 * dt)
        reward = success * 0.16
    elif action == "inspect":
        world.risk_memory = clamp(world.risk_memory + success * 0.042 * dt)
        world.route_hazard = clamp(world.route_hazard - success * 0.026 * dt)
        world.resource_shift = clamp(world.resource_shift - success * 0.014 * dt)
        reward = success * 0.12
    else:
        rest_quality = clamp(world.shelter * 0.34 + world.architecture * 0.18 + world.trust * 0.08 + 0.28)
        agent.energy = clamp(agent.energy + rest_quality * 0.20 * dt)
        agent.health = clamp(agent.health + rest_quality * 0.025 * dt)
        agent.stress = clamp(agent.stress - rest_quality * 0.10 * dt)
        reward = rest_quality * 0.07

    if action != "rest":
        agent.energy = clamp(agent.energy - (0.016 + world.weather_exposure * 0.006 + world.tool_quality * -0.003) * dt)
    agent.stress = clamp(agent.stress + world.hidden_pressure * 0.010 * dt + world.conflict * 0.012 * dt - world.trust * 0.006 * dt)
    agent.reliability = clamp(agent.reliability + max(0.0, reward) * 0.010 * dt - max(0.0, -reward) * 0.020 * dt)
    if action in TARGETED_ACTIONS[world.regime_name] and regime_active(world):
        quality = clamp(success * (0.60 + world.hidden_pressure * 0.35))
        world.adaptation_evidence = clamp(world.adaptation_evidence + quality * 0.024 * dt)
        agent.adaptation = clamp(agent.adaptation + quality * 0.014 * dt)
        agent.wisdom = clamp(agent.wisdom + quality * 0.007 * dt)
    else:
        agent.wisdom = clamp(agent.wisdom + max(0.0, reward) * 0.003 * dt)


current_agents: List[Agent] = []


def spread_skill(source: Agent, success: float, dt: float) -> None:
    peers = [agent for agent in current_agents if agent is not source and agent.alive]
    peers.sort(key=lambda agent: agent.influence, reverse=True)
    for peer in peers[:3]:
        peer.skill_build = clamp(peer.skill_build + source.skill_build * 0.004 * success * dt)
        peer.skill_tool = clamp(peer.skill_tool + source.skill_tool * 0.004 * success * dt)
        peer.skill_forage = clamp(peer.skill_forage + source.skill_forage * 0.004 * success * dt)
        peer.skill_care = clamp(peer.skill_care + source.skill_care * 0.004 * success * dt)
        peer.wisdom = clamp(peer.wisdom + source.wisdom * 0.003 * success * dt)


def update_agents(world: World, agents: List[Agent], condition: Condition, dt: float, rng: random.Random) -> None:
    update_agent_influence(agents, condition.reputation_influence)
    for agent in living(agents):
        if agent.child:
            agent.hunger = clamp(agent.hunger + 0.018 * dt - world.food * 0.016 * dt)
            agent.thirst = clamp(agent.thirst + 0.020 * dt - world.water * 0.018 * dt)
            agent.health = clamp(agent.health - max(0.0, agent.hunger - 0.78) * 0.08 * dt - max(0.0, agent.thirst - 0.78) * 0.10 * dt)
            continue
        action = choose_action(agent, world, condition, rng)
        apply_action(agent, world, condition, action, dt, rng)

    for agent in living(agents):
        food_support = world.food * 0.015 + world.food_storage * 0.008
        water_support = world.water * 0.017 + world.waterworks * 0.009
        agent.hunger = clamp(agent.hunger + (0.019 + world.weather_exposure * 0.006 + agent.stress * 0.004) * dt - food_support * dt)
        agent.thirst = clamp(agent.thirst + (0.022 + world.weather_exposure * 0.008 + agent.stress * 0.004) * dt - water_support * dt)
        agent.cleanliness = clamp(agent.cleanliness + world.sanitation * 0.018 * dt - world.contamination * 0.020 * dt - agent.stress * 0.004 * dt)
        illness = world.sickness * 0.036 + world.contamination * 0.020 + world.weather_exposure * 0.010
        scarcity = max(0.0, agent.hunger - 0.88) * 0.48 + max(0.0, agent.thirst - 0.88) * 0.62
        agent.health = clamp(agent.health - (illness + scarcity) * dt + world.clinic * 0.010 * dt)
        reserve_cost = 0.0012 * (1.0 + agent.stress * 0.44 + world.hidden_pressure * 0.30 + scarcity - agent.wisdom * 0.12)
        agent.reserve = clamp(agent.reserve - reserve_cost * dt)
        if agent.health <= 0.04 or agent.reserve <= 0.02:
            agent.alive = False
            world.deaths += 1


def maybe_reproduce(world: World, agents: List[Agent], condition: Condition, rng: random.Random, dt: float) -> None:
    if world.time < 7.5 or len(agents) >= 16:
        return
    if world.food < 0.50 or world.water < 0.50 or world.shelter < 0.50 or world.trust < 0.42:
        return
    if rng.random() > 0.032 * dt:
        return
    adults = [agent for agent in living(agents) if not agent.child and agent.health > 0.72 and agent.energy > 0.42 and agent.reserve > 0.46]
    if len(adults) < 2:
        return
    parent_a, parent_b = rng.sample(adults, 2)
    inheritance = 0.0
    if condition.teaching:
        inheritance = clamp(world.culture_memory * 0.16 + world.teaching * 0.12 + (parent_a.wisdom + parent_b.wisdom) * 0.04)
    child = Agent(
        health=0.74,
        energy=0.62,
        hunger=0.34,
        thirst=0.34,
        stress=0.16,
        cleanliness=0.60,
        reserve=0.68,
        wisdom=inheritance * 0.35,
        adaptation=inheritance * 0.30,
        reliability=0.34 + inheritance * 0.16,
        reputation=0.32 + inheritance * 0.12,
        influence=0.20,
        skill_build=0.06 + inheritance,
        skill_tool=0.06 + inheritance,
        skill_forage=0.08 + inheritance,
        skill_care=0.06 + inheritance,
        skill_teach=0.05 + inheritance,
        child=True,
    )
    parent_a.energy = clamp(parent_a.energy - 0.10)
    parent_b.energy = clamp(parent_b.energy - 0.08)
    parent_a.reserve = clamp(parent_a.reserve - 0.014)
    parent_b.reserve = clamp(parent_b.reserve - 0.012)
    world.births += 1
    world.knowledge_transfer = clamp(world.knowledge_transfer + inheritance * 0.50)
    agents.append(child)


def pressure_score(world: World, agents: Sequence[Agent]) -> float:
    alive = living(agents)
    survival = max(0.0, 0.52 - world.food) * 0.26 + max(0.0, 0.52 - world.water) * 0.28 + world.sickness * 0.16 + world.contamination * 0.14
    ecology = world.weather_exposure * 0.16 + world.resource_shift * 0.16 + world.route_hazard * 0.12
    social = world.conflict * 0.14 + max(0.0, 0.56 - world.trust) * 0.12 + world.social_inequality * 0.10
    body = max(0.0, 0.62 - mean(agent.reserve for agent in alive)) * 0.14
    return clamp(survival + ecology + social + body + world.hidden_pressure * 0.20)


def regime_response_score(world: World) -> float:
    if world.regime_name == "contaminated_water":
        return clamp(world.sanitation * 0.32 + world.waterworks * 0.28 + (1.0 - world.contamination) * 0.24 + (1.0 - world.sickness) * 0.16)
    if world.regime_name == "cold_wet_season":
        return clamp(world.shelter * 0.30 + world.architecture * 0.30 + world.path_network * 0.18 + (1.0 - world.weather_exposure) * 0.22)
    if world.regime_name == "crop_blight":
        return clamp(world.garden * 0.30 + world.food_storage * 0.28 + world.food * 0.22 + (1.0 - world.resource_shift) * 0.20)
    if world.regime_name == "tool_fatigue":
        return clamp(world.tool_design * 0.44 + world.tool_quality * 0.40 + world.materials * 0.16)
    return clamp(world.trust * 0.30 + world.reputation_accuracy * 0.24 + world.symbol_convergence * 0.22 + (1.0 - world.conflict) * 0.24)


def inference_score(world: World) -> float:
    channel = REGIME_CHANNEL[world.regime_name]
    target = world.beliefs[channel]
    distractors = [value for key, value in world.beliefs.items() if key != channel]
    margin = target - mean(distractors)
    return clamp(target * 0.72 + max(0.0, margin) * 0.58)


def checkpoint_snapshot(world: World, agents: Sequence[Agent], label: str) -> Dict[str, object]:
    alive = living(agents)
    return {
        "label": label,
        "hours": world.time,
        "regime": world.regime_name,
        "regime_active": regime_active(world),
        "alive": len(alive),
        "total_agents": len(agents),
        "food": world.food,
        "water": world.water,
        "shelter": world.shelter,
        "architecture": world.architecture,
        "tool_quality": world.tool_quality,
        "tool_design": world.tool_design,
        "sanitation": world.sanitation,
        "trust": world.trust,
        "conflict": world.conflict,
        "teaching": world.teaching,
        "knowledge_transfer": world.knowledge_transfer,
        "symbol_convergence": world.symbol_convergence,
        "hidden_pressure": world.hidden_pressure,
        "adaptation_evidence": world.adaptation_evidence,
        "beliefs": dict(world.beliefs),
        "dominant_belief": dominant_belief(world),
        "inference_score": inference_score(world),
        "response_score": regime_response_score(world),
        "targeted_response_rate": world.targeted_action_count / max(1, world.post_regime_action_count),
        "mean_wisdom": mean(agent.wisdom for agent in alive),
        "mean_influence": mean(agent.influence for agent in alive),
    }


def run_episode(seed: int, condition: Condition, cfg: Config, *, trace: bool = False) -> tuple[EpisodeRow, List[Dict[str, object]]]:
    rng = random.Random(seed * 131 + sum(ord(ch) for ch in condition.name))
    agents = make_agents(rng, cfg.population)
    world = make_world(seed, rng)
    global current_agents
    current_agents = agents
    baseline = {
        "architecture": world.architecture,
        "tool_design": world.tool_design,
        "sanitation": world.sanitation,
        "teaching": world.teaching,
    }
    checkpoints: List[Dict[str, object]] = []
    checkpoint_targets = list(CHECKPOINTS)
    alive_at_12h: int | None = None
    no_major_before_12 = True

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        world.time += dt
        apply_baseline_environment(world, agents, condition, dt, rng)
        apply_hidden_regime(world, condition, dt)
        signals = symptom_channels(world, condition, rng)
        update_beliefs(world, condition, signals, dt)
        pressure = pressure_score(world, agents)
        world.pressure_integral = clamp(world.pressure_integral + pressure * dt / max(cfg.hours, 1.0))
        update_agents(world, agents, condition, dt, rng)
        maybe_reproduce(world, agents, condition, rng, dt)

        if world.time < 12.0 and regime_active(world):
            no_major_before_12 = False
        if alive_at_12h is None and world.time >= 12.0:
            alive_at_12h = len(living(agents))
        while checkpoint_targets and world.time >= checkpoint_targets[0] - 1e-9:
            checkpoints.append(checkpoint_snapshot(world, agents, f"{checkpoint_targets.pop(0):.1f}h"))

    final_alive = len(living(agents))
    total_agents = len(agents)
    survival_score = final_alive / max(1, total_agents)
    architecture_delta = world.architecture - baseline["architecture"]
    tool_delta = world.tool_design - baseline["tool_design"]
    sanitation_delta = world.sanitation - baseline["sanitation"]
    teaching_delta = world.teaching - baseline["teaching"]
    development_score = clamp(
        max(0.0, architecture_delta) * 0.34
        + max(0.0, tool_delta) * 0.30
        + max(0.0, sanitation_delta) * 0.24
        + max(0.0, world.path_network - 0.14) * 0.14
        + max(0.0, world.food_storage - 0.18) * 0.12
    )
    culture_score = clamp(world.knowledge_transfer * 0.46 + max(0.0, teaching_delta) * 0.32 + world.symbol_convergence * 0.18 + world.reputation_accuracy * 0.14)
    response = regime_response_score(world)
    inference = inference_score(world)
    targeted_rate = world.targeted_action_count / max(1, world.post_regime_action_count)
    long_horizon_score = clamp(
        survival_score * 0.24
        + development_score * 0.18
        + culture_score * 0.16
        + response * 0.24
        + inference * 0.10
        + targeted_rate * 0.08
    )
    row = EpisodeRow(
        seed=seed,
        regime=world.regime_name,
        condition=condition.name,
        final_alive=final_alive,
        total_agents=total_agents,
        alive_at_12h=alive_at_12h if alive_at_12h is not None else final_alive,
        no_major_regime_before_12h=no_major_before_12,
        hidden_regime_after_12h=world.first_regime_hour >= 12.0 and regime_active(world),
        first_regime_hour=world.first_regime_hour,
        deaths=world.deaths,
        births=world.births,
        final_food=world.food,
        final_water=world.water,
        final_trust=world.trust,
        final_symbol_convergence=world.symbol_convergence,
        architecture_delta=architecture_delta,
        tool_design_delta=tool_delta,
        sanitation_delta=sanitation_delta,
        teaching_delta=teaching_delta,
        knowledge_transfer=world.knowledge_transfer,
        adaptation_evidence=world.adaptation_evidence,
        inference_score=inference,
        response_score=response,
        targeted_response_rate=targeted_rate,
        survival_score=survival_score,
        development_score=development_score,
        culture_score=culture_score,
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
                mean_culture_score=mean(row.culture_score for row in items),
                mean_inference_score=mean(row.inference_score for row in items),
                mean_response_score=mean(row.response_score for row in items),
                mean_targeted_response_rate=mean(row.targeted_response_rate for row in items),
                mean_final_alive=mean(row.final_alive for row in items),
                mean_alive_at_12h=mean(row.alive_at_12h for row in items),
                mean_architecture_delta=mean(row.architecture_delta for row in items),
                mean_tool_design_delta=mean(row.tool_design_delta for row in items),
                mean_sanitation_delta=mean(row.sanitation_delta for row in items),
                mean_knowledge_transfer=mean(row.knowledge_transfer for row in items),
                mean_symbol_convergence=mean(row.final_symbol_convergence for row in items),
                no_major_regime_before_12h_rate=mean(1.0 if row.no_major_regime_before_12h else 0.0 for row in items),
                hidden_regime_after_12h_rate=mean(1.0 if row.hidden_regime_after_12h else 0.0 for row in items),
            )
        )
    return summary


def summarize_by_regime(rows: Sequence[EpisodeRow]) -> List[RegimeSummaryRow]:
    buckets: Dict[tuple[str, str], List[EpisodeRow]] = {}
    for row in rows:
        buckets.setdefault((row.regime, row.condition), []).append(row)
    out: List[RegimeSummaryRow] = []
    for (regime, condition), items in sorted(buckets.items()):
        out.append(
            RegimeSummaryRow(
                regime=regime,
                condition=condition,
                mean_long_horizon_score=mean(row.long_horizon_score for row in items),
                mean_inference_score=mean(row.inference_score for row in items),
                mean_response_score=mean(row.response_score for row in items),
                mean_targeted_response_rate=mean(row.targeted_response_rate for row in items),
            )
        )
    return out


def regime_metric(regime_summary: Sequence[RegimeSummaryRow], regime: str, condition: str, metric: str) -> float:
    for row in regime_summary:
        if row.regime == regime and row.condition == condition:
            return float(getattr(row, metric))
    return 0.0


def verdict_from_summary(summary: Sequence[SummaryRow], regime_summary: Sequence[RegimeSummaryRow]) -> VerdictRow:
    by_name = {row.condition: row for row in summary}
    full = by_name["integrated_hidden_regime"]
    reactive = by_name["reactive_survival_only"]
    no_inference = by_name["no_regime_inference"]
    no_teaching = by_name["no_teaching_transmission"]
    no_reputation = by_name["no_reputation_influence"]
    no_sanitation = by_name["no_sanitation_memory"]
    no_weather = by_name["no_weather_sensors"]
    no_tool = by_name["no_tool_adaptation"]
    full_water = regime_metric(regime_summary, "contaminated_water", "integrated_hidden_regime", "mean_response_score")
    no_sanitation_water = regime_metric(regime_summary, "contaminated_water", "no_sanitation_memory", "mean_response_score")
    full_weather = regime_metric(regime_summary, "cold_wet_season", "integrated_hidden_regime", "mean_response_score")
    no_weather_cold = regime_metric(regime_summary, "cold_wet_season", "no_weather_sensors", "mean_response_score")
    full_tool = regime_metric(regime_summary, "tool_fatigue", "integrated_hidden_regime", "mean_response_score")
    no_tool_fatigue = regime_metric(regime_summary, "tool_fatigue", "no_tool_adaptation", "mean_response_score")
    full_trust = regime_metric(regime_summary, "trust_fracture", "integrated_hidden_regime", "mean_response_score")
    no_reputation_trust = regime_metric(regime_summary, "trust_fracture", "no_reputation_influence", "mean_response_score")
    losses = {
        "reactive": full.mean_long_horizon_score - reactive.mean_long_horizon_score,
        "inference": full.mean_inference_score - no_inference.mean_inference_score,
        "teaching": full.mean_culture_score - no_teaching.mean_culture_score,
        "reputation": full_trust - no_reputation_trust,
        "sanitation": full_water - no_sanitation_water,
        "weather": full_weather - no_weather_cold,
        "tool": full_tool - no_tool_fatigue,
    }
    supports_hidden = (
        full.no_major_regime_before_12h_rate == 1.0
        and full.hidden_regime_after_12h_rate == 1.0
        and full.mean_alive_at_12h >= 8.0
        and full.mean_final_alive >= 7.0
        and full.mean_response_score >= 0.62
        and full.mean_inference_score >= 0.20
        and full.mean_targeted_response_rate >= 0.30
        and full.mean_development_score >= 0.34
        and full.mean_culture_score >= 0.40
    )
    supports_ablation = (
        losses["reactive"] >= 0.10
        and losses["inference"] >= 0.05
        and losses["teaching"] >= 0.08
        and losses["reputation"] >= 0.04
        and losses["sanitation"] >= 0.018
        and losses["weather"] >= 0.012
        and losses["tool"] >= 0.040
    )
    return VerdictRow(
        integrated_score=full.mean_long_horizon_score,
        reactive_score=reactive.mean_long_horizon_score,
        no_regime_inference_score=no_inference.mean_long_horizon_score,
        no_teaching_score=no_teaching.mean_long_horizon_score,
        no_reputation_influence_score=no_reputation.mean_long_horizon_score,
        no_sanitation_memory_score=no_sanitation.mean_long_horizon_score,
        no_weather_sensors_score=no_weather.mean_long_horizon_score,
        no_tool_adaptation_score=no_tool.mean_long_horizon_score,
        reactive_loss=losses["reactive"],
        inference_loss=losses["inference"],
        teaching_loss=losses["teaching"],
        reputation_loss=losses["reputation"],
        sanitation_loss=losses["sanitation"],
        weather_loss=losses["weather"],
        tool_loss=losses["tool"],
        shock_gate_pass_rate=full.no_major_regime_before_12h_rate,
        hidden_regime_rate=full.hidden_regime_after_12h_rate,
        mean_inference_score=full.mean_inference_score,
        mean_response_score=full.mean_response_score,
        mean_targeted_response_rate=full.mean_targeted_response_rate,
        supports_hidden_regime_adaptation=supports_hidden,
        supports_ablation_specificity=supports_ablation,
        verdict="pass" if supports_hidden and supports_ablation else "partial_or_failed",
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


def write_artifacts(
    rows: Sequence[EpisodeRow],
    summary: Sequence[SummaryRow],
    regime_summary: Sequence[RegimeSummaryRow],
    verdict: VerdictRow,
    trace: List[Dict[str, object]],
    cfg: Config,
) -> Dict[str, object]:
    payload = {
        "config": {
            "seeds": list(cfg.seeds),
            "hours": cfg.hours,
            "step_hours": cfg.step_hours,
            "population": cfg.population,
            "trace_seed": cfg.trace_seed,
        },
        "regimes": list(REGIME_NAMES),
        "summary": [asdict(row) for row in summary],
        "regime_summary": [asdict(row) for row in regime_summary],
        "verdict": asdict(verdict),
        "trace": trace,
        "notes": {
            "claim": "hidden-regime adaptation pressure verifier",
            "not_claimed": "subjective consciousness, open-ended civilization, or closed-loop deep RL",
            "label_discipline": "agents receive noisy symptoms, not hidden regime labels",
        },
    }
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_hidden_regime_adaptation_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_hidden_regime_adaptation_summary.csv", summary)
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_hidden_regime_adaptation_regime_summary.csv", regime_summary)
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_hidden_regime_adaptation_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / "ssrm_3d_hidden_regime_adaptation_results.json", payload)
    write_json(ARTIFACT_DIR / "ssrm_3d_hidden_regime_adaptation_trace.json", trace)
    write_js(ARTIFACT_DIR / "ssrm_3d_hidden_regime_adaptation_results.js", "SSRM_3D_HIDDEN_REGIME_ADAPTATION_RESULTS", payload)
    write_js(ARTIFACT_DIR / "ssrm_3d_hidden_regime_adaptation_trace.js", "SSRM_3D_HIDDEN_REGIME_ADAPTATION_TRACE", trace)
    return payload


def run_benchmark(cfg: Config) -> Dict[str, object]:
    rows: List[EpisodeRow] = []
    trace: List[Dict[str, object]] = []
    for seed in cfg.seeds:
        for condition in CONDITIONS:
            row, maybe_trace = run_episode(seed, condition, cfg, trace=(seed == cfg.trace_seed and condition.name == "integrated_hidden_regime"))
            rows.append(row)
            if maybe_trace:
                trace = maybe_trace
    summary = summarize(rows)
    regime_summary = summarize_by_regime(rows)
    verdict = verdict_from_summary(summary, regime_summary)
    return write_artifacts(rows, summary, regime_summary, verdict, trace, cfg)


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", default="20260713,20260714,20260715,20260716,20260717")
    parser.add_argument("--hours", type=float, default=16.0)
    parser.add_argument("--step-hours", type=float, default=0.05)
    parser.add_argument("--population", type=int, default=10)
    parser.add_argument("--trace-seed", type=int, default=20260713)
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
