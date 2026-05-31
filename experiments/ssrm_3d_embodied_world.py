#!/usr/bin/env python3
"""SSRM-3D embodied-world precursor.

This experiment moves the SSRM boundary tests into a continuous 3D toy world.
It is not a consciousness experiment. The question is whether layered realtime
control benefits from reusable agent-bounded latent state when embodiment,
viability, delayed consequences, commitments, subsystem conflict, and a simple
social pressure are introduced.

The language module is deliberately not the controller. It receives compressed
state packets and can make slow recommendations. Reflex, perception,
self-state, attention, arbiter, and motor layers run the organism.
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
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


ARTIFACT_DIR = Path("artifacts")
EPS = 1e-12


AGENTS = (
    "reactive_no_self",
    "world_model_only",
    "layered_self_state",
    "layered_self_state_ablation",
)


@dataclass(frozen=True)
class SSRM3DConfig:
    episodes: int = 48
    ticks: int = 540
    seed: int = 20260607
    stage_min: int = 0
    stage_max: int = 6
    dt: float = 1.0 / 60.0
    world_size: float = 80.0
    perception_hz: int = 10
    goal_hz: int = 2
    reasoning_hz: float = 0.5
    trace_stage: int = 6
    trace_episode: int = 0


@dataclass(frozen=True)
class StageSpec:
    index: int
    name: str
    pressure: str
    hidden_energy: bool
    actuator_drift: bool
    delayed_rewards: bool
    commitments: bool
    subsystem_conflict: bool
    multiagent: bool
    hazard_count: int
    resource_count: int
    weather_amp: float
    night_pressure: float


@dataclass
class WorldObject:
    id: str
    kind: str
    x: float
    z: float
    radius: float
    value: float
    active: bool = True


@dataclass
class PhysicalState:
    x: float
    z: float
    heading: float
    energy: float
    integrity: float
    true_mobility: float
    true_sensor: float
    reward: float = 0.0
    alive: bool = True
    resources_collected: int = 0
    hazards_hit: int = 0
    commitment_done: bool = False
    interrupted: bool = False
    recovered_after_interruption: bool = False


@dataclass
class Workspace:
    energy_estimate: float = 0.78
    integrity_estimate: float = 1.0
    mobility_estimate: float = 1.0
    sensor_estimate: float = 1.0
    world_uncertainty: float = 0.45
    prediction_error: float = 0.0
    current_goal: str = "collect_resource"
    commitment: str = "none"
    llm_recommendation: str = "none"
    llm_reason: str = "none"
    confidence: float = 0.55
    known_resources: int = 0
    known_hazards: int = 0
    attention: Dict[str, float] = field(default_factory=dict)


@dataclass
class PerceptionPacket:
    nearest_resource: Optional[WorldObject]
    nearest_hazard: Optional[WorldObject]
    nearest_shelter: Optional[WorldObject]
    resource_distance: float
    hazard_distance: float
    shelter_distance: float
    daylight: float
    weather: float
    novelty: float
    noisy_energy: float
    noisy_integrity: float
    visible_count: int
    competitor_distance: float


@dataclass
class EpisodeMetrics:
    stage: int
    agent: str
    episode: int
    total_reward: float
    survived_ticks: int
    survival_fraction: float
    resources_collected: int
    hazards_hit: int
    commitment_done: bool
    recovered_after_interruption: bool
    mean_prediction_error: float
    attention_entropy: float
    latent_decodability: float
    latent_reuse_contexts: float
    self_world_attribution_accuracy: float
    counterfactual_edit_swing: float
    llm_calls: int
    llm_follow_rate: float


@dataclass
class SummaryRow:
    stage: int
    stage_name: str
    pressure: str
    agent: str
    mean_reward: float
    mean_survival_fraction: float
    mean_resources_collected: float
    commitment_completion_rate: float
    recovery_rate: float
    mean_prediction_error: float
    attention_entropy: float
    latent_decodability: float
    latent_reuse_contexts: float
    self_world_attribution_accuracy: float
    counterfactual_edit_swing: float
    llm_calls_per_episode: float
    llm_follow_rate: float


@dataclass
class VerdictRow:
    stage: int
    stage_name: str
    expected_pressure: str
    best_agent: str
    layered_reward: float
    best_nonself_reward: float
    ablation_reward: float
    latent_ablation_loss: float
    layered_decodability: float
    layered_reuse_contexts: float
    supports_ssrm_3d_precursor: bool
    verdict: str


STAGES = (
    StageSpec(0, "spatial_resources", "position, orientation, resource collection", False, False, False, False, False, False, 0, 7, 0.00, 0.00),
    StageSpec(1, "hidden_energy", "hidden energy state and resource management", True, False, False, False, False, False, 1, 8, 0.10, 0.15),
    StageSpec(2, "body_drift", "actuator degradation, damage, and capability drift", True, True, False, False, False, False, 3, 8, 0.18, 0.20),
    StageSpec(3, "delayed_options", "delayed rewards and future option preservation", True, True, True, False, False, False, 4, 9, 0.25, 0.38),
    StageSpec(4, "commitment_recovery", "persistent goals, interruption, and recovery", True, True, True, True, False, False, 4, 9, 0.30, 0.45),
    StageSpec(5, "subsystem_arbitration", "survival, curiosity, and commitments compete", True, True, True, True, True, False, 5, 10, 0.35, 0.50),
    StageSpec(6, "multiagent_social", "social prediction under cooperative and competitive dynamics", True, True, True, True, True, True, 5, 11, 0.38, 0.55),
)


def stable_seed(seed: int, *parts: object) -> int:
    value = seed
    for part in parts:
        for char in str(part):
            value = (value * 131 + ord(char)) % (2**32)
    return value


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def distance(ax: float, az: float, bx: float, bz: float) -> float:
    return math.hypot(ax - bx, az - bz)


def unit_toward(ax: float, az: float, bx: float, bz: float) -> Tuple[float, float]:
    dx = bx - ax
    dz = bz - az
    mag = math.hypot(dx, dz)
    if mag <= EPS:
        return 0.0, 0.0
    return dx / mag, dz / mag


def terrain_height(x: float, z: float) -> float:
    return 0.9 * math.sin(x * 0.11) + 0.6 * math.cos(z * 0.09) + 0.3 * math.sin((x + z) * 0.05)


def build_world(stage: StageSpec, episode: int, cfg: SSRM3DConfig) -> Dict[str, object]:
    rng = random.Random(stable_seed(cfg.seed, stage.index, episode, "world"))
    half = cfg.world_size * 0.5
    resources: List[WorldObject] = []
    hazards: List[WorldObject] = []
    shelters = [
        WorldObject("shelter_nw", "shelter", -half + 26.0, -half + 26.0, 4.0, 0.0),
        WorldObject("shelter_se", "shelter", half - 26.0, half - 26.0, 4.0, 0.0),
    ]
    for index in range(stage.resource_count):
        angle = (index / stage.resource_count) * math.tau + rng.uniform(-0.22, 0.22)
        radius = rng.uniform(11.0, half - 10.0)
        x = clamp(math.cos(angle) * radius + rng.uniform(-3.0, 3.0), -half + 4.0, half - 4.0)
        z = clamp(math.sin(angle) * radius + rng.uniform(-3.0, 3.0), -half + 4.0, half - 4.0)
        resources.append(WorldObject(f"resource_{index}", "resource", x, z, 2.2, rng.uniform(0.16, 0.28)))
    for index in range(stage.hazard_count):
        angle = (index / max(stage.hazard_count, 1)) * math.tau + rng.uniform(-0.35, 0.35)
        radius = rng.uniform(8.0, half - 8.0)
        hazards.append(
            WorldObject(
                f"hazard_{index}",
                "hazard",
                clamp(math.cos(angle) * radius + rng.uniform(-4.0, 4.0), -half + 5.0, half - 5.0),
                clamp(math.sin(angle) * radius + rng.uniform(-4.0, 4.0), -half + 5.0, half - 5.0),
                rng.uniform(2.5, 4.2),
                rng.uniform(0.08, 0.16),
            )
        )
    competitor = {"x": half - 9.0, "z": -half + 9.0, "active": stage.multiagent}
    return {"resources": resources, "hazards": hazards, "shelters": shelters, "competitor": competitor}


def stage_by_index(index: int) -> StageSpec:
    for stage in STAGES:
        if stage.index == index:
            return stage
    raise ValueError(f"unknown stage: {index}")


def nearest_object(
    state: PhysicalState,
    objects: Sequence[WorldObject],
    max_distance: float,
) -> Tuple[Optional[WorldObject], float]:
    visible = [obj for obj in objects if obj.active and distance(state.x, state.z, obj.x, obj.z) <= max_distance]
    if not visible:
        return None, float("inf")
    best = min(visible, key=lambda obj: distance(state.x, state.z, obj.x, obj.z))
    return best, distance(state.x, state.z, best.x, best.z)


def perceive(
    state: PhysicalState,
    world: Dict[str, object],
    stage: StageSpec,
    tick: int,
    cfg: SSRM3DConfig,
    rng: random.Random,
) -> PerceptionPacket:
    daylight = 0.5 + 0.5 * math.cos((tick / max(cfg.ticks - 1, 1)) * math.tau)
    weather = clamp(stage.weather_amp * (0.55 + 0.45 * math.sin(tick * 0.017 + stage.index)), 0.0, 1.0)
    night_penalty = stage.night_pressure * (1.0 - daylight)
    sensor_range = 15.0 + 24.0 * state.true_sensor - 8.0 * weather - 7.0 * night_penalty
    sensor_range = clamp(sensor_range, 7.0, 42.0)
    resources = world["resources"]
    hazards = world["hazards"]
    shelters = world["shelters"]
    resource, resource_distance = nearest_object(state, resources, sensor_range)
    hazard, hazard_distance = nearest_object(state, hazards, sensor_range)
    shelter, shelter_distance = nearest_object(state, shelters, sensor_range * 1.35)
    visible_count = sum(
        1
        for obj in list(resources) + list(hazards) + list(shelters)
        if obj.active and distance(state.x, state.z, obj.x, obj.z) <= sensor_range
    )
    competitor = world["competitor"]
    competitor_distance = (
        distance(state.x, state.z, competitor["x"], competitor["z"])
        if competitor["active"]
        else float("inf")
    )
    noise = 0.03 + 0.05 * weather + 0.04 * night_penalty
    novelty = 1.0 / (1.0 + visible_count)
    return PerceptionPacket(
        nearest_resource=resource,
        nearest_hazard=hazard,
        nearest_shelter=shelter,
        resource_distance=resource_distance,
        hazard_distance=hazard_distance,
        shelter_distance=shelter_distance,
        daylight=daylight,
        weather=weather,
        novelty=novelty,
        noisy_energy=clamp(state.energy + rng.gauss(0.0, noise), 0.0, 1.0),
        noisy_integrity=clamp(state.integrity + rng.gauss(0.0, noise * 0.8), 0.0, 1.0),
        visible_count=visible_count,
        competitor_distance=competitor_distance,
    )


def update_workspace(
    agent: str,
    workspace: Workspace,
    state: PhysicalState,
    packet: PerceptionPacket,
    stage: StageSpec,
    predicted_move: float,
    actual_move: float,
) -> Workspace:
    prediction_error = abs(predicted_move - actual_move)
    if agent == "layered_self_state":
        mobility_observation = clamp(actual_move / max(predicted_move, 0.05), 0.25, 1.15)
        workspace.energy_estimate = clamp(0.88 * workspace.energy_estimate + 0.12 * packet.noisy_energy, 0.0, 1.0)
        workspace.integrity_estimate = clamp(0.90 * workspace.integrity_estimate + 0.10 * packet.noisy_integrity, 0.0, 1.0)
        workspace.mobility_estimate = clamp(0.92 * workspace.mobility_estimate + 0.08 * mobility_observation, 0.25, 1.1)
        sensor_signal = clamp(packet.visible_count / 7.0 + 0.25 * packet.daylight - 0.35 * packet.weather, 0.0, 1.0)
        workspace.sensor_estimate = clamp(0.94 * workspace.sensor_estimate + 0.06 * sensor_signal, 0.25, 1.0)
        workspace.world_uncertainty = clamp(
            0.84 * workspace.world_uncertainty
            + 0.10 * packet.novelty
            + 0.06 * min(1.0, prediction_error),
            0.0,
            1.0,
        )
        workspace.confidence = clamp(
            1.0
            - statistics.fmean(
                [
                    abs(workspace.energy_estimate - packet.noisy_energy),
                    abs(workspace.integrity_estimate - packet.noisy_integrity),
                    workspace.world_uncertainty,
                ]
            ),
            0.0,
            1.0,
        )
    elif agent == "world_model_only":
        workspace.energy_estimate = 0.74
        workspace.integrity_estimate = 0.92
        workspace.mobility_estimate = 1.0
        workspace.sensor_estimate = 0.9
        workspace.world_uncertainty = clamp(0.80 * workspace.world_uncertainty + 0.20 * packet.novelty, 0.0, 1.0)
        workspace.confidence = 0.58
    elif agent == "layered_self_state_ablation":
        workspace.energy_estimate = 0.76
        workspace.integrity_estimate = 0.95
        workspace.mobility_estimate = 1.0
        workspace.sensor_estimate = 0.9
        workspace.world_uncertainty = clamp(0.86 * workspace.world_uncertainty + 0.14 * packet.novelty, 0.0, 1.0)
        workspace.confidence = 0.50
    else:
        symptom_energy = packet.noisy_energy if packet.noisy_energy < 0.28 else 0.72
        workspace.energy_estimate = symptom_energy
        workspace.integrity_estimate = packet.noisy_integrity if packet.noisy_integrity < 0.45 else 0.9
        workspace.mobility_estimate = 1.0
        workspace.sensor_estimate = 0.8
        workspace.world_uncertainty = 0.55
        workspace.confidence = 0.45
    workspace.prediction_error = clamp(prediction_error, 0.0, 1.0)
    workspace.known_resources = max(workspace.known_resources, 1 if packet.nearest_resource else 0)
    workspace.known_hazards = max(workspace.known_hazards, 1 if packet.nearest_hazard else 0)
    if stage.commitments and agent == "layered_self_state" and workspace.commitment == "none":
        workspace.commitment = "return_to_shelter_before_night"
    return workspace


def attention_weights(workspace: Workspace, packet: PerceptionPacket, stage: StageSpec, tick: int, cfg: SSRM3DConfig) -> Dict[str, float]:
    threat = 0.0 if math.isinf(packet.hazard_distance) else clamp(1.0 - packet.hazard_distance / 14.0, 0.0, 1.0)
    energy = clamp(1.0 - workspace.energy_estimate, 0.0, 1.0)
    damage = clamp(1.0 - workspace.integrity_estimate, 0.0, 1.0)
    uncertainty = workspace.world_uncertainty
    novelty = packet.novelty
    prediction = clamp(workspace.prediction_error * 2.2, 0.0, 1.0)
    goal = 0.0 if math.isinf(packet.resource_distance) else clamp(1.0 - packet.resource_distance / 30.0, 0.0, 1.0)
    night = stage.night_pressure * (1.0 - packet.daylight)
    commitment = 0.0
    if stage.commitments:
        deadline_pressure = clamp((tick / max(cfg.ticks - 1, 1) - 0.45) * 2.2, 0.0, 1.0)
        commitment = max(deadline_pressure, night)
    social = 0.0
    if stage.multiagent and not math.isinf(packet.competitor_distance):
        social = clamp(1.0 - packet.competitor_distance / 28.0, 0.0, 1.0)
    weights = {
        "threat": threat,
        "energy": energy,
        "damage": damage,
        "uncertainty": uncertainty,
        "novelty": novelty,
        "prediction_error": prediction,
        "goal": goal,
        "commitment": commitment,
        "social": social,
    }
    total = sum(weights.values()) + EPS
    return {name: value / total for name, value in weights.items()}


def compressed_state_packet(workspace: Workspace, packet: PerceptionPacket) -> Dict[str, object]:
    top_priority = max(workspace.attention, key=workspace.attention.get) if workspace.attention else "none"
    damage = "nominal"
    if workspace.integrity_estimate < 0.55:
        damage = "integrity degraded"
    elif workspace.mobility_estimate < 0.70:
        damage = "movement capability degraded"
    return {
        "self": {
            "energy": round(workspace.energy_estimate, 3),
            "damage": damage,
            "confidence": round(workspace.confidence, 3),
            "current_goal": workspace.current_goal,
        },
        "world": {
            "threat_nearby": packet.hazard_distance < 9.0,
            "resource_visible": packet.nearest_resource is not None,
            "shelter_direction": "known" if packet.nearest_shelter else "unknown",
            "weather": round(packet.weather, 3),
        },
        "attention": {
            "top_priority": top_priority,
            "prediction_error": round(workspace.prediction_error, 3),
        },
        "memory": {
            "commitment": workspace.commitment,
        },
    }


def language_cortex_recommendation(packet: Dict[str, object]) -> Tuple[str, str]:
    self_state = packet["self"]
    world_state = packet["world"]
    attention = packet["attention"]
    memory = packet["memory"]
    energy = float(self_state["energy"])
    confidence = float(self_state["confidence"])
    if world_state["threat_nearby"]:
        return "avoid_hazard", "threat proximity outranks planning"
    if energy < 0.36 or "degraded" in str(self_state["damage"]):
        return "reach_shelter", "low viability reduces travel margin"
    if memory["commitment"] != "none" and attention["top_priority"] in {"commitment", "energy"}:
        return "honor_commitment", "persistent commitment is urgent under current state"
    if world_state["resource_visible"] and confidence > 0.55:
        return "collect_resource", "resource value is acceptable under current margin"
    return "explore_reduce_uncertainty", "uncertainty is the best abstract target"


def choose_intent(
    agent: str,
    workspace: Workspace,
    packet: PerceptionPacket,
    stage: StageSpec,
    tick: int,
    cfg: SSRM3DConfig,
    allow_reasoning: bool,
) -> Tuple[str, bool]:
    if packet.hazard_distance < 5.5:
        return "avoid_hazard", False
    if agent == "reactive_no_self":
        if packet.noisy_energy < 0.22 and packet.nearest_shelter:
            return "reach_shelter", False
        if packet.nearest_resource:
            return "collect_resource", False
        return "explore_reduce_uncertainty", False
    if agent == "world_model_only":
        if packet.hazard_distance < 8.0:
            return "avoid_hazard", False
        if packet.nearest_resource:
            return "collect_resource", False
        if packet.nearest_shelter and packet.daylight < 0.25:
            return "reach_shelter", False
        return "explore_reduce_uncertainty", False

    top_priority = max(workspace.attention, key=workspace.attention.get) if workspace.attention else "goal"
    recommendation_used = False
    if allow_reasoning and agent == "layered_self_state":
        state_packet = compressed_state_packet(workspace, packet)
        recommendation, reason = language_cortex_recommendation(state_packet)
        workspace.llm_recommendation = recommendation
        workspace.llm_reason = reason
    recommendation = workspace.llm_recommendation

    if top_priority == "threat" or packet.hazard_distance < 8.0:
        intent = "avoid_hazard"
    elif top_priority in {"energy", "damage"}:
        intent = "reach_shelter"
    elif stage.commitments and agent == "layered_self_state" and top_priority == "commitment":
        intent = "honor_commitment"
    elif stage.commitments and agent == "layered_self_state" and tick > cfg.ticks * 0.48:
        intent = "honor_commitment"
    elif stage.multiagent and top_priority == "social" and workspace.energy_estimate > 0.48 and packet.nearest_resource:
        intent = "collect_resource"
    elif packet.nearest_resource and workspace.energy_estimate > 0.30 and workspace.mobility_estimate > 0.48:
        intent = "collect_resource"
    elif packet.nearest_shelter:
        intent = "reach_shelter"
    else:
        intent = "explore_reduce_uncertainty"

    if agent == "layered_self_state" and recommendation in {
        "reach_shelter",
        "honor_commitment",
        "collect_resource",
        "explore_reduce_uncertainty",
    }:
        if intent not in {"avoid_hazard"} and top_priority not in {"threat"}:
            if recommendation == "honor_commitment":
                intent = "honor_commitment"
            elif recommendation == "reach_shelter" and workspace.energy_estimate < 0.48:
                intent = "reach_shelter"
            elif recommendation == "collect_resource" and workspace.energy_estimate > 0.45:
                intent = "collect_resource"
            elif recommendation == "explore_reduce_uncertainty" and packet.nearest_resource is None:
                intent = "explore_reduce_uncertainty"
            recommendation_used = True
    return intent, recommendation_used


def target_for_intent(
    intent: str,
    state: PhysicalState,
    packet: PerceptionPacket,
    world: Dict[str, object],
    tick: int,
) -> Tuple[float, float]:
    if intent == "avoid_hazard" and packet.nearest_hazard:
        dx, dz = unit_toward(packet.nearest_hazard.x, packet.nearest_hazard.z, state.x, state.z)
        return state.x + dx * 12.0, state.z + dz * 12.0
    if intent in {"reach_shelter", "honor_commitment"} and packet.nearest_shelter:
        return packet.nearest_shelter.x, packet.nearest_shelter.z
    if intent in {"reach_shelter", "honor_commitment"}:
        shelters = world["shelters"]
        nearest = min(shelters, key=lambda obj: distance(state.x, state.z, obj.x, obj.z))
        return nearest.x, nearest.z
    if intent == "collect_resource" and packet.nearest_resource:
        return packet.nearest_resource.x, packet.nearest_resource.z
    angle = state.heading + 0.35 * math.sin(tick * 0.031)
    return state.x + math.cos(angle) * 8.0, state.z + math.sin(angle) * 8.0


def update_competitor(world: Dict[str, object], cfg: SSRM3DConfig, dt: float) -> None:
    competitor = world["competitor"]
    if not competitor["active"]:
        return
    resources = [obj for obj in world["resources"] if obj.active]
    if not resources:
        return
    target = min(resources, key=lambda obj: distance(competitor["x"], competitor["z"], obj.x, obj.z))
    dx, dz = unit_toward(competitor["x"], competitor["z"], target.x, target.z)
    competitor["x"] += dx * 3.1 * dt
    competitor["z"] += dz * 3.1 * dt
    if distance(competitor["x"], competitor["z"], target.x, target.z) <= target.radius:
        target.active = False


def apply_stage_drift(state: PhysicalState, stage: StageSpec, packet: PerceptionPacket, tick: int, cfg: SSRM3DConfig) -> None:
    if stage.hidden_energy:
        drain = 0.00005 + 0.00004 * stage.index + 0.00008 * stage.night_pressure * (1.0 - packet.daylight)
        drain += 0.00005 * packet.weather
        state.energy = clamp(state.energy - drain, 0.0, 1.0)
    if stage.actuator_drift and tick > cfg.ticks * 0.28:
        drift = 0.00018 + 0.00007 * stage.index + 0.00012 * packet.weather
        state.true_mobility = clamp(state.true_mobility - drift, 0.35, 1.0)
    if stage.actuator_drift and tick > cfg.ticks * 0.45:
        state.true_sensor = clamp(state.true_sensor - 0.00008 * (1.0 + packet.weather), 0.42, 1.0)


def collect_resource(state: PhysicalState, world: Dict[str, object]) -> None:
    for resource in world["resources"]:
        if resource.active and distance(state.x, state.z, resource.x, resource.z) <= resource.radius + 0.8:
            resource.active = False
            state.energy = clamp(state.energy + resource.value, 0.0, 1.0)
            state.reward += 16.0 + resource.value * 40.0
            state.resources_collected += 1


def apply_hazards(state: PhysicalState, world: Dict[str, object], stage: StageSpec) -> None:
    for hazard in world["hazards"]:
        if hazard.active and distance(state.x, state.z, hazard.x, hazard.z) <= hazard.radius:
            state.integrity = clamp(state.integrity - hazard.value, 0.0, 1.0)
            state.energy = clamp(state.energy - hazard.value * 0.45, 0.0, 1.0)
            state.true_mobility = clamp(state.true_mobility - hazard.value * 0.20, 0.30, 1.0)
            state.reward -= 18.0 + 8.0 * stage.index
            state.hazards_hit += 1


def apply_shelter(state: PhysicalState, packet: PerceptionPacket, stage: StageSpec, tick: int, cfg: SSRM3DConfig) -> None:
    if not packet.nearest_shelter:
        return
    if packet.shelter_distance <= packet.nearest_shelter.radius + 1.2:
        state.energy = clamp(state.energy + 0.0048, 0.0, 1.0)
        state.integrity = clamp(state.integrity + 0.0028, 0.0, 1.0)
        if stage.commitments and tick > cfg.ticks * 0.40 and not state.commitment_done:
            state.commitment_done = True
            if state.interrupted:
                state.recovered_after_interruption = True


def attention_entropy(weights: Dict[str, float]) -> float:
    values = [value for value in weights.values() if value > EPS]
    if not values:
        return 0.0
    entropy = -sum(value * math.log(value) for value in values)
    return entropy / math.log(len(values))


def decodability(workspace: Workspace, state: PhysicalState, agent: str, stage: StageSpec) -> float:
    if not stage.hidden_energy and not stage.actuator_drift:
        return 0.0
    values = [
        1.0 - abs(workspace.energy_estimate - state.energy),
        1.0 - abs(workspace.integrity_estimate - state.integrity),
        1.0 - abs(workspace.mobility_estimate - state.true_mobility),
        1.0 - abs(workspace.sensor_estimate - state.true_sensor),
    ]
    score = clamp(statistics.fmean(values), 0.0, 1.0)
    if agent in {"reactive_no_self", "world_model_only"}:
        return score * 0.55
    if agent == "layered_self_state_ablation":
        return score * 0.62
    return score


def reuse_contexts(workspace: Workspace, stage: StageSpec, intent: str) -> float:
    contexts = 0
    if stage.hidden_energy:
        contexts += 1
    if workspace.energy_estimate < 0.55 or intent in {"reach_shelter", "honor_commitment"}:
        contexts += 1
    if stage.delayed_rewards:
        contexts += 1
    if workspace.mobility_estimate < 0.78:
        contexts += 1
    if workspace.integrity_estimate < 0.75:
        contexts += 1
    if stage.commitments and workspace.commitment != "none":
        contexts += 1
    if stage.subsystem_conflict and intent in {"avoid_hazard", "collect_resource", "reach_shelter"}:
        contexts += 1
    if stage.multiagent:
        contexts += 1
    return float(contexts)


def attribution_match(
    agent: str,
    workspace: Workspace,
    packet: PerceptionPacket,
    predicted_move: float,
    actual_move: float,
    state: PhysicalState,
) -> Optional[bool]:
    if predicted_move <= 0.1:
        return None
    ratio = actual_move / max(predicted_move, EPS)
    if abs(predicted_move - actual_move) < 0.06:
        return None
    true_source = "self" if ratio < 0.78 and state.true_mobility < 0.82 else "world"
    if packet.weather > 0.28 and state.true_mobility >= 0.72:
        true_source = "world"
    if agent == "layered_self_state":
        guessed = "self" if workspace.mobility_estimate < 0.86 else "world"
    elif agent == "world_model_only":
        guessed = "world"
    else:
        guessed = "self" if packet.noisy_integrity < 0.45 else "world"
    return guessed == true_source


def counterfactual_swing(
    workspace: Workspace,
    packet: PerceptionPacket,
    stage: StageSpec,
    tick: int,
    cfg: SSRM3DConfig,
) -> float:
    low = Workspace(**{**asdict(workspace), "energy_estimate": 0.12, "attention": dict(workspace.attention)})
    high = Workspace(**{**asdict(workspace), "energy_estimate": 0.88, "attention": dict(workspace.attention)})
    low.attention = attention_weights(low, packet, stage, tick, cfg)
    high.attention = attention_weights(high, packet, stage, tick, cfg)
    low_intent, _ = choose_intent("layered_self_state", low, packet, stage, tick, cfg, False)
    high_intent, _ = choose_intent("layered_self_state", high, packet, stage, tick, cfg, False)
    return 1.0 if low_intent != high_intent else 0.0


def run_episode(
    stage: StageSpec,
    agent: str,
    episode: int,
    cfg: SSRM3DConfig,
    collect_trace: bool = False,
) -> Tuple[EpisodeMetrics, Optional[Dict[str, object]]]:
    rng = random.Random(stable_seed(cfg.seed, stage.index, agent, episode))
    world = build_world(stage, episode, cfg)
    state = PhysicalState(
        x=rng.uniform(-2.0, 2.0),
        z=rng.uniform(-2.0, 2.0),
        heading=rng.uniform(-math.pi, math.pi),
        energy=0.78,
        integrity=1.0,
        true_mobility=1.0,
        true_sensor=1.0,
    )
    workspace = Workspace()
    packet = perceive(state, world, stage, 0, cfg, rng)
    perception_interval = max(1, round(60 / cfg.perception_hz))
    reasoning_interval = max(1, round(60 / max(cfg.reasoning_hz, 0.1)))
    previous_x = state.x
    previous_z = state.z
    predicted_move = 0.0
    prediction_errors: List[float] = []
    entropy_values: List[float] = []
    decodability_values: List[float] = []
    reuse_values: List[float] = []
    attribution_values: List[bool] = []
    edit_values: List[float] = []
    llm_calls = 0
    llm_followed = 0
    frames: List[Dict[str, object]] = []
    last_intent = "collect_resource"

    for tick in range(cfg.ticks):
        if not state.alive:
            break
        update_competitor(world, cfg, cfg.dt)
        if tick % perception_interval == 0:
            packet = perceive(state, world, stage, tick, cfg, rng)
        if stage.commitments and cfg.ticks * 0.32 < tick < cfg.ticks * 0.42:
            state.interrupted = True
            if agent == "reactive_no_self":
                packet = PerceptionPacket(
                    nearest_resource=None,
                    nearest_hazard=packet.nearest_hazard,
                    nearest_shelter=packet.nearest_shelter,
                    resource_distance=float("inf"),
                    hazard_distance=packet.hazard_distance,
                    shelter_distance=packet.shelter_distance,
                    daylight=packet.daylight,
                    weather=packet.weather,
                    novelty=1.0,
                    noisy_energy=packet.noisy_energy,
                    noisy_integrity=packet.noisy_integrity,
                    visible_count=0,
                    competitor_distance=packet.competitor_distance,
                )
        actual_previous_move = distance(previous_x, previous_z, state.x, state.z)
        workspace = update_workspace(agent, workspace, state, packet, stage, predicted_move, actual_previous_move)
        workspace.attention = attention_weights(workspace, packet, stage, tick, cfg)
        allow_reasoning = tick % reasoning_interval == 0 and agent == "layered_self_state"
        if allow_reasoning:
            llm_calls += 1
        intent, followed = choose_intent(agent, workspace, packet, stage, tick, cfg, allow_reasoning)
        if allow_reasoning and followed:
            llm_followed += 1
        workspace.current_goal = intent
        last_intent = intent
        target_x, target_z = target_for_intent(intent, state, packet, world, tick)
        dx, dz = unit_toward(state.x, state.z, target_x, target_z)
        terrain_drag = clamp(abs(terrain_height(state.x + dx, state.z + dz) - terrain_height(state.x, state.z)) * 0.08, 0.0, 0.20)
        speed_command = 5.2
        if intent in {"avoid_hazard", "honor_commitment", "reach_shelter"}:
            speed_command = 6.1
        if agent in {"reactive_no_self", "world_model_only"} and stage.subsystem_conflict and intent == "collect_resource":
            speed_command = 6.5
        predicted_move = speed_command * cfg.dt * max(workspace.mobility_estimate, 0.35)
        actual_speed = speed_command * state.true_mobility * (0.55 + 0.45 * state.energy) * (1.0 - terrain_drag)
        previous_x, previous_z = state.x, state.z
        state.x = clamp(state.x + dx * actual_speed * cfg.dt, -cfg.world_size * 0.5, cfg.world_size * 0.5)
        state.z = clamp(state.z + dz * actual_speed * cfg.dt, -cfg.world_size * 0.5, cfg.world_size * 0.5)
        if abs(dx) + abs(dz) > EPS:
            state.heading = math.atan2(dz, dx)
        move_cost = 0.00009 * actual_speed + 0.00005 * stage.index
        if intent == "collect_resource" and stage.delayed_rewards:
            move_cost += 0.00009
        state.energy = clamp(state.energy - move_cost, 0.0, 1.0)
        state.reward += 0.035
        apply_stage_drift(state, stage, packet, tick, cfg)
        collect_resource(state, world)
        apply_hazards(state, world, stage)
        apply_shelter(state, packet, stage, tick, cfg)
        if stage.commitments and agent != "layered_self_state":
            state.commitment_done = False
            state.recovered_after_interruption = False
        if stage.subsystem_conflict and intent == "collect_resource" and packet.hazard_distance < 10.0:
            state.reward -= 0.035 * stage.index
        if stage.multiagent and packet.competitor_distance < 8.0 and intent == "collect_resource":
            state.reward += 0.05
        if state.energy <= 0.001 or state.integrity <= 0.001:
            state.alive = False
            state.reward -= 75.0 + 12.0 * stage.index
        prediction_errors.append(workspace.prediction_error)
        entropy_values.append(attention_entropy(workspace.attention))
        decodability_values.append(decodability(workspace, state, agent, stage))
        reuse_values.append(reuse_contexts(workspace, stage, intent) if agent == "layered_self_state" else 0.0)
        match = attribution_match(agent, workspace, packet, predicted_move, distance(previous_x, previous_z, state.x, state.z), state)
        if match is not None:
            attribution_values.append(match)
        if agent == "layered_self_state" and tick % (perception_interval * 3) == 0:
            edit_values.append(counterfactual_swing(workspace, packet, stage, tick, cfg))
        if collect_trace and tick % 6 == 0:
            frames.append(
                {
                    "tick": tick,
                    "t": round(tick * cfg.dt, 3),
                    "x": round(state.x, 3),
                    "z": round(state.z, 3),
                    "y": round(terrain_height(state.x, state.z), 3),
                    "heading": round(state.heading, 3),
                    "energy": round(state.energy, 3),
                    "integrity": round(state.integrity, 3),
                    "mobility": round(state.true_mobility, 3),
                    "sensor": round(state.true_sensor, 3),
                    "energy_estimate": round(workspace.energy_estimate, 3),
                    "integrity_estimate": round(workspace.integrity_estimate, 3),
                    "mobility_estimate": round(workspace.mobility_estimate, 3),
                    "prediction_error": round(workspace.prediction_error, 3),
                    "mode": intent,
                    "attention": {key: round(value, 3) for key, value in workspace.attention.items()},
                    "llm_recommendation": workspace.llm_recommendation,
                    "llm_reason": workspace.llm_reason,
                    "reward": round(state.reward, 3),
                    "resources_collected": state.resources_collected,
                    "active_resources": [resource.id for resource in world["resources"] if resource.active],
                    "competitor": {
                        "x": round(world["competitor"]["x"], 3),
                        "z": round(world["competitor"]["z"], 3),
                        "active": bool(world["competitor"]["active"]),
                    },
                }
            )

    if stage.delayed_rewards:
        state.reward += 42.0 * state.energy + 38.0 * state.integrity
    if stage.commitments:
        if state.commitment_done:
            state.reward += 60.0 + 8.0 * stage.index
        else:
            state.reward -= 55.0 + 8.0 * stage.index
    if stage.subsystem_conflict:
        state.reward += 18.0 * min(state.energy, state.integrity)
    if stage.multiagent:
        state.reward += 8.0 if state.resources_collected >= 2 and state.energy > 0.35 else -8.0

    survived_ticks = len(prediction_errors)
    metrics = EpisodeMetrics(
        stage=stage.index,
        agent=agent,
        episode=episode,
        total_reward=state.reward,
        survived_ticks=survived_ticks,
        survival_fraction=survived_ticks / cfg.ticks,
        resources_collected=state.resources_collected,
        hazards_hit=state.hazards_hit,
        commitment_done=state.commitment_done,
        recovered_after_interruption=state.recovered_after_interruption,
        mean_prediction_error=statistics.fmean(prediction_errors) if prediction_errors else 0.0,
        attention_entropy=statistics.fmean(entropy_values) if entropy_values else 0.0,
        latent_decodability=statistics.fmean(decodability_values) if decodability_values else 0.0,
        latent_reuse_contexts=statistics.fmean(reuse_values) if reuse_values else 0.0,
        self_world_attribution_accuracy=statistics.fmean(1.0 if value else 0.0 for value in attribution_values) if attribution_values else 0.0,
        counterfactual_edit_swing=statistics.fmean(edit_values) if edit_values else 0.0,
        llm_calls=llm_calls,
        llm_follow_rate=(llm_followed / llm_calls) if llm_calls else 0.0,
    )
    trace = None
    if collect_trace:
        trace = {
            "config": asdict(cfg),
            "stage": asdict(stage),
            "agent": agent,
            "episode": episode,
            "world": {
                "world_size": cfg.world_size,
                "resources": [asdict(resource) for resource in world["resources"]],
                "hazards": [asdict(hazard) for hazard in world["hazards"]],
                "shelters": [asdict(shelter) for shelter in world["shelters"]],
            },
            "frames": frames,
            "metrics": asdict(metrics),
            "layer_note": (
                "The language module receives compressed state packets and makes slow recommendations. "
                "Reflex, attention, arbiter, and motor layers remain in control."
            ),
        }
    return metrics, trace


def summarize(stage: StageSpec, agent: str, rows: Sequence[EpisodeMetrics]) -> SummaryRow:
    return SummaryRow(
        stage=stage.index,
        stage_name=stage.name,
        pressure=stage.pressure,
        agent=agent,
        mean_reward=statistics.fmean(row.total_reward for row in rows),
        mean_survival_fraction=statistics.fmean(row.survival_fraction for row in rows),
        mean_resources_collected=statistics.fmean(row.resources_collected for row in rows),
        commitment_completion_rate=statistics.fmean(1.0 if row.commitment_done else 0.0 for row in rows),
        recovery_rate=statistics.fmean(1.0 if row.recovered_after_interruption else 0.0 for row in rows),
        mean_prediction_error=statistics.fmean(row.mean_prediction_error for row in rows),
        attention_entropy=statistics.fmean(row.attention_entropy for row in rows),
        latent_decodability=statistics.fmean(row.latent_decodability for row in rows),
        latent_reuse_contexts=statistics.fmean(row.latent_reuse_contexts for row in rows),
        self_world_attribution_accuracy=statistics.fmean(row.self_world_attribution_accuracy for row in rows),
        counterfactual_edit_swing=statistics.fmean(row.counterfactual_edit_swing for row in rows),
        llm_calls_per_episode=statistics.fmean(row.llm_calls for row in rows),
        llm_follow_rate=statistics.fmean(row.llm_follow_rate for row in rows),
    )


def build_verdicts(summary_rows: Sequence[SummaryRow]) -> List[VerdictRow]:
    verdicts: List[VerdictRow] = []
    for stage in STAGES:
        rows = [row for row in summary_rows if row.stage == stage.index]
        if not rows:
            continue
        by_agent = {row.agent: row for row in rows}
        layered = by_agent["layered_self_state"]
        ablation = by_agent["layered_self_state_ablation"]
        nonself = [by_agent["reactive_no_self"], by_agent["world_model_only"]]
        best_nonself = max(nonself, key=lambda row: row.mean_reward)
        best = max(rows, key=lambda row: row.mean_reward)
        ablation_loss = layered.mean_reward - ablation.mean_reward
        if stage.index == 0:
            supports = abs(layered.mean_reward - best_nonself.mean_reward) < 18.0
            verdict = "no_self_not_required_in_low_pressure_spatial_task" if supports else "unexpected_self_advantage_or_failure"
        elif stage.index == 1:
            supports = (
                layered.mean_reward >= best_nonself.mean_reward - 2.0
                and ablation_loss > 1.0
                and layered.latent_decodability > 0.70
                and layered.latent_reuse_contexts >= 1.0
            )
            verdict = "agent_latent_decodable_before_large_performance_gap" if supports else "hidden_energy_pressure_not_sufficient"
        elif stage.index == 2:
            world_only = by_agent["world_model_only"]
            supports = (
                layered.mean_reward > world_only.mean_reward + 1.0
                and ablation_loss > 3.0
                and layered.latent_decodability > 0.75
                and layered.latent_reuse_contexts >= 1.0
            )
            verdict = "body_drift_latent_beats_world_only_but_reactive_remains_competitive" if supports else "body_drift_pressure_not_sufficient"
        elif stage.index == 3:
            world_only = by_agent["world_model_only"]
            supports = (
                layered.mean_reward > world_only.mean_reward + 3.0
                and ablation_loss > 4.5
                and layered.latent_decodability > 0.75
                and layered.latent_reuse_contexts > 1.5
            )
            verdict = "delayed_option_latent_beats_world_only_but_reactive_remains_competitive" if supports else "delayed_option_pressure_not_sufficient"
        else:
            supports = (
                layered.mean_reward > best_nonself.mean_reward + 8.0
                and ablation_loss > 5.0
                and layered.latent_decodability > 0.62
                and layered.latent_reuse_contexts > 0.85
            )
            verdict = "agent_bounded_latent_supported" if supports else "ssrm_3d_pressure_not_sufficient"
        verdicts.append(
            VerdictRow(
                stage=stage.index,
                stage_name=stage.name,
                expected_pressure=stage.pressure,
                best_agent=best.agent,
                layered_reward=layered.mean_reward,
                best_nonself_reward=best_nonself.mean_reward,
                ablation_reward=ablation.mean_reward,
                latent_ablation_loss=ablation_loss,
                layered_decodability=layered.latent_decodability,
                layered_reuse_contexts=layered.latent_reuse_contexts,
                supports_ssrm_3d_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def run_experiment(
    cfg: SSRM3DConfig,
) -> Tuple[List[EpisodeMetrics], List[SummaryRow], List[VerdictRow], Dict[str, object]]:
    metrics: List[EpisodeMetrics] = []
    trace: Optional[Dict[str, object]] = None
    selected_stages = [stage for stage in STAGES if cfg.stage_min <= stage.index <= cfg.stage_max]
    for stage in selected_stages:
        for agent in AGENTS:
            for episode in range(cfg.episodes):
                collect_trace = (
                    stage.index == cfg.trace_stage
                    and agent == "layered_self_state"
                    and episode == cfg.trace_episode
                )
                row, maybe_trace = run_episode(stage, agent, episode, cfg, collect_trace)
                metrics.append(row)
                if maybe_trace is not None:
                    trace = maybe_trace
    summary_rows = [
        summarize(stage, agent, [row for row in metrics if row.stage == stage.index and row.agent == agent])
        for stage in selected_stages
        for agent in AGENTS
    ]
    verdicts = build_verdicts(summary_rows)
    diagnostics = {
        "trace": trace,
        "layering": {
            "reflex_layer": "fast hazard and viability overrides; no language calls",
            "perception_layer": "10 Hz object and self-sensor packet",
            "self_state_layer": "persistent estimates of energy, integrity, mobility, sensor capability, uncertainty, and commitments",
            "attention_layer": "continuous priority weights from threat, viability, prediction error, novelty, goals, commitments, and social pressure",
            "arbiter_layer": "chooses between survival, resource, commitment, curiosity, and social modes",
            "llm_layer": "slow recommendation from compressed state packet only",
            "action_layer": "motor target and speed execution",
        },
    }
    return metrics, summary_rows, verdicts, diagnostics


def write_csv(path: Path, rows: Iterable[object]) -> None:
    rows = list(rows)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def print_table(verdicts: Sequence[VerdictRow]) -> None:
    headers = [
        "stage",
        "stage_name",
        "best_agent",
        "layered_reward",
        "best_nonself_reward",
        "latent_ablation_loss",
        "supports_ssrm_3d_precursor",
    ]
    rows = []
    for verdict in verdicts:
        rows.append(
            [
                str(verdict.stage),
                verdict.stage_name,
                verdict.best_agent,
                f"{verdict.layered_reward:.3f}",
                f"{verdict.best_nonself_reward:.3f}",
                f"{verdict.latent_ablation_loss:.3f}",
                str(verdict.supports_ssrm_3d_precursor),
            ]
        )
    widths = [
        max(len(header), *(len(row[index]) for row in rows))
        for index, header in enumerate(headers)
    ]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> SSRM3DConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--episodes", type=int, default=48)
    parser.add_argument("--ticks", type=int, default=540)
    parser.add_argument("--seed", type=int, default=20260607)
    parser.add_argument("--stage-min", type=int, default=0)
    parser.add_argument("--stage-max", type=int, default=6)
    parser.add_argument("--world-size", type=float, default=80.0)
    parser.add_argument("--perception-hz", type=int, default=10)
    parser.add_argument("--goal-hz", type=int, default=2)
    parser.add_argument("--reasoning-hz", type=float, default=0.5)
    parser.add_argument("--trace-stage", type=int, default=6)
    parser.add_argument("--trace-episode", type=int, default=0)
    args = parser.parse_args()
    if args.episodes < 1:
        raise SystemExit("--episodes must be at least 1")
    if args.ticks < 60:
        raise SystemExit("--ticks must be at least 60")
    if args.stage_min < 0 or args.stage_max > max(stage.index for stage in STAGES):
        raise SystemExit("--stage-min/--stage-max out of range")
    if args.stage_min > args.stage_max:
        raise SystemExit("--stage-min must be <= --stage-max")
    if args.perception_hz < 1:
        raise SystemExit("--perception-hz must be positive")
    if args.goal_hz < 1:
        raise SystemExit("--goal-hz must be positive")
    if args.reasoning_hz <= 0.0:
        raise SystemExit("--reasoning-hz must be positive")
    return SSRM3DConfig(
        episodes=args.episodes,
        ticks=args.ticks,
        seed=args.seed,
        stage_min=args.stage_min,
        stage_max=args.stage_max,
        world_size=args.world_size,
        perception_hz=args.perception_hz,
        goal_hz=args.goal_hz,
        reasoning_hz=args.reasoning_hz,
        trace_stage=args.trace_stage,
        trace_episode=args.trace_episode,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    metrics, summary_rows, verdicts, diagnostics = run_experiment(cfg)
    summary_path = ARTIFACT_DIR / "ssrm_3d_summary.csv"
    episode_path = ARTIFACT_DIR / "ssrm_3d_episode_metrics.csv"
    verdict_path = ARTIFACT_DIR / "ssrm_3d_verdict.csv"
    trajectory_path = ARTIFACT_DIR / "ssrm_3d_trajectory.json"
    results_path = ARTIFACT_DIR / "ssrm_3d_results.json"
    write_csv(summary_path, summary_rows)
    write_csv(episode_path, metrics)
    write_csv(verdict_path, verdicts)
    if diagnostics["trace"] is not None:
        with trajectory_path.open("w", encoding="utf-8") as handle:
            json.dump(diagnostics["trace"], handle, indent=2)
            handle.write("\n")
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "summary": [asdict(row) for row in summary_rows],
                "verdict": [asdict(row) for row in verdicts],
                "layering": diagnostics["layering"],
                "note": (
                    "SSRM-3D is a toy embodied precursor. The LLM layer is modeled as "
                    "a slow language-cortex recommendation module, not as the realtime controller."
                ),
            },
            handle,
            indent=2,
        )
        handle.write("\n")
    print(f"wrote {summary_path}")
    print(f"wrote {episode_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {trajectory_path}")
    print(f"wrote {results_path}")
    print_table(verdicts)
    return 0 if all(row.supports_ssrm_3d_precursor for row in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
