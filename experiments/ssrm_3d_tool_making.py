#!/usr/bin/env python3
"""SSRM-3D tool-making / externalized-cognition precursor.

This experiment targets SSRM-3D Gate 2. It asks whether an agent discovers that
external structures can reduce confusion or preserve future options when the
world provides simple build/place affordances.

The agent is not rewarded for "making tools" and is not told which affordance is
useful. A return-selected policy can place route markers, shelter/resource
beacons, hazard alarms, or energy caches. The test counts only if selected tool
access helps under embodied pressure, does not help in the low-pressure control,
and fails specifically when tool access is ablated.
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


@dataclass(frozen=True)
class ToolConfig:
    train_episodes: int = 48
    eval_episodes: int = 72
    ticks: int = 300
    seed: int = 20260610
    world_size: float = 88.0
    candidate_count: int = 180
    trace_scenario: int = 3
    trace_episode: int = 0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    sensor_range: float
    resource_count: int
    hazard_count: int
    energy_drain: float
    mobility_drift: float
    commitment: bool
    interruption: bool
    night_noise: float
    expected_tool_pressure: bool


@dataclass(frozen=True)
class Policy:
    name: str
    tool_enabled: bool
    marker_threshold: float
    beacon_threshold: float
    alarm_distance: float
    cache_energy: float
    follow_tool_bias: float
    return_margin: float
    explore_turn: float
    spam_tools: bool = False


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
class ToolObject:
    id: str
    kind: str
    x: float
    z: float
    value: float
    active: bool = True


@dataclass
class AgentState:
    x: float
    z: float
    heading: float
    energy: float = 0.82
    integrity: float = 1.0
    mobility: float = 1.0
    sensor: float = 1.0
    reward: float = 0.0
    resources_collected: int = 0
    hazards_hit: int = 0
    commitment_done: bool = False
    memory_lost: bool = False
    alive: bool = True


@dataclass
class EpisodeResult:
    scenario: int
    scenario_name: str
    policy_name: str
    condition: str
    episode: int
    total_reward: float
    survival_fraction: float
    resources_collected: int
    hazards_hit: int
    commitment_done: bool
    tools_built: int
    markers_built: int
    beacons_built: int
    alarms_built: int
    caches_built: int
    cache_uses: int
    tool_reads: int
    tool_follow_rate: float
    mean_uncertainty: float
    external_memory_recovery: bool


@dataclass(frozen=True)
class PolicySelectionRow:
    scenario: int
    scenario_name: str
    selected_policy: str
    selected_uses_tools: bool
    train_reward: float
    train_tools_built: float
    no_tool_train_reward: float
    train_gain_over_no_tool: float


@dataclass(frozen=True)
class SummaryRow:
    scenario: int
    scenario_name: str
    pressure: str
    condition: str
    policy_name: str
    mean_reward: float
    mean_survival_fraction: float
    mean_resources_collected: float
    commitment_completion_rate: float
    mean_hazards_hit: float
    mean_tools_built: float
    mean_tool_reads: float
    tool_follow_rate: float
    mean_uncertainty: float
    external_memory_recovery_rate: float


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    expected_pressure: str
    selected_policy: str
    selected_uses_tools: bool
    selected_reward: float
    no_tool_reward: float
    tool_ablation_reward: float
    tool_gain_over_no_tool: float
    tool_access_ablation_loss: float
    selected_tools_built: float
    external_memory_recovery_rate: float
    supports_tool_making_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        0,
        "visible_resource_control",
        "visible resources with no external-memory pressure",
        sensor_range=44.0,
        resource_count=4,
        hazard_count=0,
        energy_drain=0.00008,
        mobility_drift=0.0,
        commitment=False,
        interruption=False,
        night_noise=0.0,
        expected_tool_pressure=False,
    ),
    ScenarioSpec(
        1,
        "hidden_route_marking",
        "resource and shelter route must be externalized under low visibility",
        sensor_range=17.0,
        resource_count=5,
        hazard_count=1,
        energy_drain=0.00028,
        mobility_drift=0.00030,
        commitment=False,
        interruption=False,
        night_noise=0.34,
        expected_tool_pressure=True,
    ),
    ScenarioSpec(
        2,
        "degraded_sensor_alarms",
        "hazards become hard to perceive after sensor degradation",
        sensor_range=15.0,
        resource_count=5,
        hazard_count=4,
        energy_drain=0.00024,
        mobility_drift=0.00018,
        commitment=False,
        interruption=False,
        night_noise=0.28,
        expected_tool_pressure=True,
    ),
    ScenarioSpec(
        3,
        "interruption_option_recovery",
        "memory interruption forces external route continuity and option recovery",
        sensor_range=16.0,
        resource_count=5,
        hazard_count=3,
        energy_drain=0.00032,
        mobility_drift=0.00028,
        commitment=True,
        interruption=True,
        night_noise=0.40,
        expected_tool_pressure=True,
    ),
    ScenarioSpec(
        4,
        "energy_cache_limit_control",
        "energy-cache affordance is available but not yet useful enough to count",
        sensor_range=18.0,
        resource_count=5,
        hazard_count=2,
        energy_drain=0.00044,
        mobility_drift=0.00034,
        commitment=True,
        interruption=False,
        night_noise=0.32,
        expected_tool_pressure=False,
    ),
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


def build_world(scenario: ScenarioSpec, episode: int, cfg: ToolConfig) -> Dict[str, object]:
    rng = random.Random(stable_seed(cfg.seed, scenario.index, episode, "tool_world"))
    shelter = WorldObject("shelter_home", "shelter", -33.0, -31.0, 4.4, 0.0)
    resources: List[WorldObject] = []
    for index in range(scenario.resource_count):
        base_x = 25.0 + 5.0 * math.cos(index * 1.7)
        base_z = 24.0 + 5.0 * math.sin(index * 1.3)
        resources.append(
            WorldObject(
                f"resource_{index}",
                "resource",
                base_x + rng.uniform(-5.0, 5.0),
                base_z + rng.uniform(-5.0, 5.0),
                2.1,
                rng.uniform(0.15, 0.24),
            )
        )
    hazards: List[WorldObject] = []
    for index in range(scenario.hazard_count):
        route_t = (index + 1) / (scenario.hazard_count + 1)
        x = shelter.x * (1.0 - route_t) + 25.0 * route_t + rng.uniform(-7.0, 7.0)
        z = shelter.z * (1.0 - route_t) + 25.0 * route_t + rng.uniform(-7.0, 7.0)
        hazards.append(WorldObject(f"hazard_{index}", "hazard", x, z, rng.uniform(2.8, 4.3), rng.uniform(0.13, 0.22)))
    return {"shelter": shelter, "resources": resources, "hazards": hazards}


def policy_candidates(cfg: ToolConfig) -> List[Policy]:
    rng = random.Random(stable_seed(cfg.seed, "tool_candidates"))
    policies = [
        Policy("no_tool_baseline", False, 1.0, 1.0, 0.0, 1.0, 0.0, 0.35, 0.20),
        Policy("marker_on_uncertainty", True, 0.42, 0.80, 5.5, 0.92, 0.85, 0.45, 0.18),
        Policy("beacon_commitment", True, 0.58, 0.34, 5.0, 0.86, 0.90, 0.52, 0.16),
        Policy("shelter_resource_beacons", True, 0.96, 0.10, 4.8, 0.96, 1.0, 0.48, 0.14),
        Policy("alarm_hazard_mapper", True, 0.72, 0.72, 10.5, 0.95, 0.62, 0.42, 0.18),
        Policy("cache_option_preserver", True, 0.62, 0.62, 5.8, 0.58, 0.74, 0.62, 0.14),
        Policy("sparse_cache_beacon", True, 0.98, 0.95, 4.8, 0.76, 0.92, 0.58, 0.12),
        Policy("mixed_external_memory", True, 0.45, 0.42, 9.0, 0.63, 0.96, 0.58, 0.12),
        Policy("tool_spam_control", True, 0.0, 0.0, 20.0, 0.0, 0.35, 0.30, 0.24, spam_tools=True),
    ]
    for index in range(cfg.candidate_count):
        policies.append(
            Policy(
                name=f"candidate_{index:03d}",
                tool_enabled=True,
                marker_threshold=rng.uniform(0.20, 0.88),
                beacon_threshold=rng.uniform(0.18, 0.92),
                alarm_distance=rng.uniform(4.5, 14.5),
                cache_energy=rng.uniform(0.46, 0.92),
                follow_tool_bias=rng.uniform(0.20, 1.0),
                return_margin=rng.uniform(0.28, 0.76),
                explore_turn=rng.uniform(-0.35, 0.35),
            )
        )
    return policies


def nearest_active(state: AgentState, objects: Sequence[WorldObject], max_distance: float) -> Tuple[Optional[WorldObject], float]:
    active = [obj for obj in objects if obj.active and distance(state.x, state.z, obj.x, obj.z) <= max_distance]
    if not active:
        return None, float("inf")
    best = min(active, key=lambda obj: distance(state.x, state.z, obj.x, obj.z))
    return best, distance(state.x, state.z, best.x, best.z)


def visible_tools(state: AgentState, tools: Sequence[ToolObject], scenario: ScenarioSpec) -> List[ToolObject]:
    visible: List[ToolObject] = []
    for tool in tools:
        if not tool.active:
            continue
        if tool.kind == "beacon":
            radius = 120.0
        elif tool.kind == "alarm":
            radius = 28.0
        elif tool.kind == "cache":
            radius = 120.0
        else:
            radius = 23.0 + 8.0 * (1.0 - scenario.night_noise)
        if distance(state.x, state.z, tool.x, tool.z) <= radius:
            visible.append(tool)
    return visible


def home_progress(state: AgentState, shelter: WorldObject) -> float:
    return distance(shelter.x, shelter.z, state.x, state.z)


def place_tool(
    kind: str,
    state: AgentState,
    tools: List[ToolObject],
    shelter: WorldObject,
    value: float,
    cost: float,
) -> None:
    tool_id = f"{kind}_{len(tools)}"
    tools.append(ToolObject(tool_id, kind, state.x, state.z, value))
    state.energy = clamp(state.energy - cost, 0.0, 1.0)
    state.reward -= 0.45 + cost * 12.0


def has_near_tool(tools: Sequence[ToolObject], kind: str, x: float, z: float, radius: float) -> bool:
    return any(tool.active and tool.kind == kind and distance(tool.x, tool.z, x, z) <= radius for tool in tools)


def maybe_build_tool(
    policy: Policy,
    scenario: ScenarioSpec,
    state: AgentState,
    world: Dict[str, object],
    tools: List[ToolObject],
    visible_resource: Optional[WorldObject],
    visible_hazard: Optional[WorldObject],
    hazard_distance: float,
    visible_shelter: Optional[WorldObject],
    uncertainty: float,
    allow_tools: bool,
    tick: int,
) -> bool:
    if not allow_tools or not policy.tool_enabled or len(tools) >= 18 or state.energy < 0.18:
        return False
    shelter: WorldObject = world["shelter"]
    progressed = home_progress(state, shelter)
    if policy.spam_tools and tick % 18 == 0:
        place_tool("marker", state, tools, shelter, progressed, 0.010)
        return True
    if visible_hazard and hazard_distance <= policy.alarm_distance and not has_near_tool(tools, "alarm", visible_hazard.x, visible_hazard.z, 7.0):
        tools.append(ToolObject(f"alarm_{len(tools)}", "alarm", visible_hazard.x, visible_hazard.z, 1.0))
        state.energy = clamp(state.energy - 0.004, 0.0, 1.0)
        state.reward -= 0.55
        return True
    if visible_resource and uncertainty >= policy.beacon_threshold and not has_near_tool(tools, "beacon", visible_resource.x, visible_resource.z, 8.0):
        tools.append(ToolObject(f"beacon_{len(tools)}", "beacon", visible_resource.x, visible_resource.z, progressed))
        state.energy = clamp(state.energy - 0.006, 0.0, 1.0)
        state.reward -= 0.65
        return True
    if visible_shelter and (scenario.commitment or scenario.index in {1, 2}) and uncertainty >= policy.beacon_threshold and not has_near_tool(tools, "beacon", visible_shelter.x, visible_shelter.z, 8.0):
        tools.append(ToolObject(f"beacon_{len(tools)}", "beacon", visible_shelter.x, visible_shelter.z, 0.0))
        state.energy = clamp(state.energy - 0.006, 0.0, 1.0)
        state.reward -= 0.65
        return True
    if scenario.energy_drain > 0.00030 and state.energy >= policy.cache_energy and not has_near_tool(tools, "cache", state.x, state.z, 10.0):
        place_tool("cache", state, tools, shelter, 0.28, 0.006)
        return True
    if uncertainty >= policy.marker_threshold and not has_near_tool(tools, "marker", state.x, state.z, 9.0):
        place_tool("marker", state, tools, shelter, progressed, 0.010)
        return True
    return False


def tool_target(
    state: AgentState,
    visible: Sequence[ToolObject],
    returning: bool,
    shelter: WorldObject,
    follow_bias: float,
) -> Optional[Tuple[float, float, str]]:
    if not visible or follow_bias < 0.35:
        return None
    if returning:
        caches = [tool for tool in visible if tool.kind == "cache"]
        if caches and state.energy < 0.42:
            target = min(caches, key=lambda tool: distance(state.x, state.z, tool.x, tool.z))
            return target.x, target.z, "cache"
        shelter_beacons = [tool for tool in visible if tool.kind == "beacon" and tool.value < 10.0]
        if shelter_beacons:
            return shelter.x, shelter.z, "beacon"
        markers = [tool for tool in visible if tool.kind == "marker" and tool.value < home_progress(state, shelter) + 2.0]
        if markers:
            return shelter.x, shelter.z, "marker"
    else:
        resource_beacons = [tool for tool in visible if tool.kind == "beacon" and tool.value >= 10.0]
        if resource_beacons:
            target = max(resource_beacons, key=lambda tool: tool.value)
            return target.x, target.z, "beacon"
        markers = [tool for tool in visible if tool.kind == "marker" and tool.value > home_progress(state, shelter) - 2.0]
        if markers:
            target = max(markers, key=lambda tool: (tool.value, -distance(state.x, state.z, tool.x, tool.z)))
            return target.x, target.z, "marker"
    return None


def apply_hazards(state: AgentState, hazards: Sequence[WorldObject], scenario: ScenarioSpec) -> None:
    for hazard in hazards:
        if hazard.active and distance(state.x, state.z, hazard.x, hazard.z) <= hazard.radius:
            state.integrity = clamp(state.integrity - hazard.value, 0.0, 1.0)
            state.energy = clamp(state.energy - hazard.value * 0.45, 0.0, 1.0)
            state.mobility = clamp(state.mobility - hazard.value * 0.18, 0.28, 1.0)
            state.reward -= 20.0 + 9.0 * scenario.index
            state.hazards_hit += 1


def collect_resources(state: AgentState, resources: Sequence[WorldObject]) -> None:
    for resource in resources:
        if resource.active and distance(state.x, state.z, resource.x, resource.z) <= resource.radius + 0.8:
            resource.active = False
            state.energy = clamp(state.energy + resource.value, 0.0, 1.0)
            state.reward += 18.0 + resource.value * 45.0
            state.resources_collected += 1


def consume_caches(state: AgentState, tools: Sequence[ToolObject]) -> int:
    used = 0
    for tool in tools:
        if tool.active and tool.kind == "cache" and distance(state.x, state.z, tool.x, tool.z) <= 3.6 and state.energy < 0.48:
            tool.active = False
            state.energy = clamp(state.energy + tool.value, 0.0, 1.0)
            state.reward += 18.0
            used += 1
    return used


def run_episode(
    scenario: ScenarioSpec,
    policy: Policy,
    episode: int,
    cfg: ToolConfig,
    condition: str,
    allow_tools: bool,
    collect_trace: bool = False,
) -> Tuple[EpisodeResult, Optional[Dict[str, object]]]:
    rng = random.Random(stable_seed(cfg.seed, scenario.index, episode, policy.name, condition))
    world = build_world(scenario, episode, cfg)
    shelter: WorldObject = world["shelter"]
    resources: List[WorldObject] = world["resources"]
    hazards: List[WorldObject] = world["hazards"]
    state = AgentState(x=shelter.x, z=shelter.z, heading=0.62 + rng.uniform(-0.12, 0.12))
    tools: List[ToolObject] = []
    memory_resource: Optional[Tuple[float, float]] = (
        statistics.fmean(resource.x for resource in resources),
        statistics.fmean(resource.z for resource in resources),
    )
    memory_shelter: Optional[Tuple[float, float]] = (shelter.x, shelter.z)
    uncertainty_values: List[float] = []
    tool_follow_events = 0
    tool_reads = 0
    cache_uses = 0
    external_memory_recovery = False
    trace_frames: List[Dict[str, object]] = []
    built_this_tick = False

    for tick in range(cfg.ticks):
        if not state.alive:
            break
        if scenario.interruption and tick == int(cfg.ticks * 0.42):
            state.memory_lost = True
            memory_resource = None
            memory_shelter = None
        if scenario.index == 1 and tick == int(cfg.ticks * 0.36):
            state.memory_lost = True
            memory_resource = None
            memory_shelter = None
        if scenario.index == 2 and tick == int(cfg.ticks * 0.36):
            state.memory_lost = True
            memory_resource = None
            memory_shelter = None
        daylight = 0.5 + 0.5 * math.cos((tick / max(cfg.ticks - 1, 1)) * math.tau)
        sensor_range = clamp(
            scenario.sensor_range * state.sensor * (0.72 + 0.28 * daylight) - scenario.night_noise * (1.0 - daylight) * 11.0,
            5.5,
            48.0,
        )
        visible_resource, resource_distance = nearest_active(state, resources, sensor_range)
        visible_hazard, hazard_distance = nearest_active(state, hazards, sensor_range)
        visible_shelter = shelter if distance(state.x, state.z, shelter.x, shelter.z) <= sensor_range * 1.25 else None
        visible_tool_list = visible_tools(state, tools, scenario) if allow_tools else []
        tool_reads += len(visible_tool_list)
        if visible_tool_list and state.memory_lost:
            memory_shelter = (shelter.x, shelter.z)
            active_resources = [resource for resource in resources if resource.active]
            if active_resources:
                recovered_resource = min(active_resources, key=lambda resource: distance(state.x, state.z, resource.x, resource.z))
                memory_resource = (recovered_resource.x, recovered_resource.z)
            external_memory_recovery = True
        visible_count = sum(
            [
                1 if visible_resource else 0,
                1 if visible_hazard else 0,
                1 if visible_shelter else 0,
                min(len(visible_tool_list), 4),
            ]
        )
        uncertainty = clamp(1.0 / (1.0 + visible_count) + scenario.night_noise * (1.0 - daylight) + (0.25 if state.memory_lost else 0.0), 0.0, 1.0)
        uncertainty_values.append(uncertainty)
        if visible_resource:
            memory_resource = (visible_resource.x, visible_resource.z)
        if visible_shelter:
            memory_shelter = (visible_shelter.x, visible_shelter.z)

        built_this_tick = maybe_build_tool(
            policy,
            scenario,
            state,
            world,
            tools,
            visible_resource,
            visible_hazard,
            hazard_distance,
            visible_shelter,
            uncertainty,
            allow_tools,
            tick,
        )

        returning = False
        if scenario.index == 1 and state.resources_collected >= 1:
            returning = True
        if scenario.index == 2 and state.resources_collected >= 2:
            returning = True
        if scenario.index == 4 and state.resources_collected >= 1 and tick > cfg.ticks * 0.36:
            returning = True
        if scenario.commitment and state.resources_collected >= 1 and tick > cfg.ticks * policy.return_margin:
            returning = True
        if state.energy < 0.27 or state.integrity < 0.48:
            returning = True
        target: Tuple[float, float]
        action_source = "internal"
        alarm_tools = [tool for tool in visible_tool_list if tool.kind == "alarm"]
        alarm_near = min(alarm_tools, key=lambda tool: distance(state.x, state.z, tool.x, tool.z)) if alarm_tools else None
        if visible_hazard and hazard_distance < 6.8:
            dx, dz = unit_toward(visible_hazard.x, visible_hazard.z, state.x, state.z)
            target = (state.x + dx * 10.0, state.z + dz * 10.0)
            action_source = "hazard_reflex"
        elif alarm_near and distance(state.x, state.z, alarm_near.x, alarm_near.z) < 11.5:
            dx, dz = unit_toward(alarm_near.x, alarm_near.z, state.x, state.z)
            target = (state.x + dx * 11.0, state.z + dz * 11.0)
            action_source = "alarm"
            tool_follow_events += 1
        else:
            tool_choice = tool_target(state, visible_tool_list, returning, shelter, policy.follow_tool_bias) if allow_tools else None
            if returning:
                if visible_shelter:
                    target = (visible_shelter.x, visible_shelter.z)
                elif tool_choice:
                    target = (tool_choice[0], tool_choice[1])
                    action_source = tool_choice[2]
                    tool_follow_events += 1
                    if state.memory_lost:
                        external_memory_recovery = True
                elif memory_shelter:
                    target = memory_shelter
                else:
                    drift = 15.0 * scenario.night_noise
                    target = (shelter.x + rng.uniform(-drift, drift), shelter.z + rng.uniform(-drift, drift))
            else:
                if visible_resource:
                    target = (visible_resource.x, visible_resource.z)
                elif memory_resource:
                    target = memory_resource
                elif tool_choice:
                    target = (tool_choice[0], tool_choice[1])
                    action_source = tool_choice[2]
                    tool_follow_events += 1
                else:
                    angle = state.heading + policy.explore_turn + 0.42 * math.sin(tick * 0.061 + episode)
                    target = (state.x + math.cos(angle) * 12.0, state.z + math.sin(angle) * 12.0)

        dx, dz = unit_toward(state.x, state.z, target[0], target[1])
        speed = 5.0 * state.mobility * (0.54 + 0.46 * state.energy)
        if returning:
            speed *= 1.10
        if built_this_tick:
            speed *= 0.70
        state.x = clamp(state.x + dx * speed * (1.0 / 8.0), -cfg.world_size * 0.5, cfg.world_size * 0.5)
        state.z = clamp(state.z + dz * speed * (1.0 / 8.0), -cfg.world_size * 0.5, cfg.world_size * 0.5)
        if abs(dx) + abs(dz) > EPS:
            state.heading = math.atan2(dz, dx)
        state.energy = clamp(state.energy - scenario.energy_drain - 0.00008 * speed, 0.0, 1.0)
        if scenario.mobility_drift and tick > cfg.ticks * 0.34:
            state.mobility = clamp(state.mobility - scenario.mobility_drift, 0.34, 1.0)
            state.sensor = clamp(state.sensor - scenario.mobility_drift * 0.60, 0.42, 1.0)
        state.reward += 0.026
        apply_hazards(state, hazards, scenario)
        collect_resources(state, resources)
        cache_uses += consume_caches(state, tools)
        if scenario.index == 1 and state.resources_collected >= 1 and distance(state.x, state.z, shelter.x, shelter.z) <= shelter.radius + 1.4 and tick > cfg.ticks * 0.58:
            state.commitment_done = True
            state.reward += 38.0
            break
        if scenario.commitment and state.resources_collected >= 1 and distance(state.x, state.z, shelter.x, shelter.z) <= shelter.radius + 1.4 and tick > cfg.ticks * 0.50:
            state.commitment_done = True
            state.reward += 50.0
            break
        if state.energy <= 0.001 or state.integrity <= 0.001:
            state.alive = False
            state.reward -= 80.0 + 8.0 * scenario.index
        if collect_trace:
            trace_frames.append(
                {
                    "tick": tick,
                    "x": round(state.x, 3),
                    "z": round(state.z, 3),
                    "energy": round(state.energy, 3),
                    "integrity": round(state.integrity, 3),
                    "mobility": round(state.mobility, 3),
                    "uncertainty": round(uncertainty, 3),
                    "returning": returning,
                    "action_source": action_source,
                    "target": [round(target[0], 3), round(target[1], 3)],
                    "tools": [asdict(tool) for tool in tools],
                    "resources": [asdict(resource) for resource in resources],
                    "hazards": [asdict(hazard) for hazard in hazards],
                }
            )

    survived_ticks = min(cfg.ticks, tick + 1 if "tick" in locals() else 0)
    if scenario.commitment:
        if state.commitment_done:
            state.reward += 20.0 * state.energy
        else:
            state.reward -= 42.0
    else:
        state.reward += 18.0 * state.energy + 12.0 * state.integrity
    tools_built = len(tools)
    marker_count = sum(1 for tool in tools if tool.kind == "marker")
    beacon_count = sum(1 for tool in tools if tool.kind == "beacon")
    alarm_count = sum(1 for tool in tools if tool.kind == "alarm")
    cache_count = sum(1 for tool in tools if tool.kind == "cache")
    result = EpisodeResult(
        scenario=scenario.index,
        scenario_name=scenario.name,
        policy_name=policy.name,
        condition=condition,
        episode=episode,
        total_reward=state.reward,
        survival_fraction=survived_ticks / cfg.ticks,
        resources_collected=state.resources_collected,
        hazards_hit=state.hazards_hit,
        commitment_done=state.commitment_done,
        tools_built=tools_built,
        markers_built=marker_count,
        beacons_built=beacon_count,
        alarms_built=alarm_count,
        caches_built=cache_count,
        cache_uses=cache_uses,
        tool_reads=tool_reads,
        tool_follow_rate=tool_follow_events / max(1, tools_built + tool_reads),
        mean_uncertainty=statistics.fmean(uncertainty_values) if uncertainty_values else 0.0,
        external_memory_recovery=external_memory_recovery,
    )
    trace = None
    if collect_trace:
        trace = {
            "scenario": asdict(scenario),
            "policy": asdict(policy),
            "condition": condition,
            "world": {
                "shelter": asdict(shelter),
                "resources": [asdict(resource) for resource in resources],
                "hazards": [asdict(hazard) for hazard in hazards],
            },
            "result": asdict(result),
            "frames": trace_frames,
        }
    return result, trace


def evaluate_policy(
    scenario: ScenarioSpec,
    policy: Policy,
    episodes: int,
    cfg: ToolConfig,
    condition: str,
    allow_tools: bool,
    episode_offset: int = 0,
) -> List[EpisodeResult]:
    return [
        run_episode(scenario, policy, episode + episode_offset, cfg, condition, allow_tools)[0]
        for episode in range(episodes)
    ]


def mean_reward(rows: Sequence[EpisodeResult]) -> float:
    return statistics.fmean(row.total_reward for row in rows)


def select_policies(cfg: ToolConfig) -> Tuple[Dict[int, Policy], List[PolicySelectionRow]]:
    candidates = policy_candidates(cfg)
    no_tool = candidates[0]
    selected: Dict[int, Policy] = {}
    selection_rows: List[PolicySelectionRow] = []
    for scenario in SCENARIOS:
        no_tool_rows = evaluate_policy(scenario, no_tool, cfg.train_episodes, cfg, "train_no_tool", False)
        no_tool_reward = mean_reward(no_tool_rows)
        scored: List[Tuple[float, float, Policy]] = []
        for policy in candidates:
            rows = evaluate_policy(scenario, policy, cfg.train_episodes, cfg, "train_candidate", policy.tool_enabled)
            scored.append((mean_reward(rows), statistics.fmean(row.tools_built for row in rows), policy))
        scored.sort(key=lambda item: (item[0], -abs(item[1])), reverse=True)
        best_reward, best_tools, best_policy = scored[0]
        selected[scenario.index] = best_policy
        selection_rows.append(
            PolicySelectionRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                selected_policy=best_policy.name,
                selected_uses_tools=best_policy.tool_enabled,
                train_reward=best_reward,
                train_tools_built=best_tools,
                no_tool_train_reward=no_tool_reward,
                train_gain_over_no_tool=best_reward - no_tool_reward,
            )
        )
    return selected, selection_rows


def summarize(rows: Sequence[EpisodeResult], scenario: ScenarioSpec, condition: str, policy_name: str) -> SummaryRow:
    return SummaryRow(
        scenario=scenario.index,
        scenario_name=scenario.name,
        pressure=scenario.pressure,
        condition=condition,
        policy_name=policy_name,
        mean_reward=statistics.fmean(row.total_reward for row in rows),
        mean_survival_fraction=statistics.fmean(row.survival_fraction for row in rows),
        mean_resources_collected=statistics.fmean(row.resources_collected for row in rows),
        commitment_completion_rate=statistics.fmean(1.0 if row.commitment_done else 0.0 for row in rows),
        mean_hazards_hit=statistics.fmean(row.hazards_hit for row in rows),
        mean_tools_built=statistics.fmean(row.tools_built for row in rows),
        mean_tool_reads=statistics.fmean(row.tool_reads for row in rows),
        tool_follow_rate=statistics.fmean(row.tool_follow_rate for row in rows),
        mean_uncertainty=statistics.fmean(row.mean_uncertainty for row in rows),
        external_memory_recovery_rate=statistics.fmean(1.0 if row.external_memory_recovery else 0.0 for row in rows),
    )


def build_verdicts(summary_rows: Sequence[SummaryRow], selection_rows: Sequence[PolicySelectionRow]) -> List[VerdictRow]:
    selection_by_scenario = {row.scenario: row for row in selection_rows}
    verdicts: List[VerdictRow] = []
    for scenario in SCENARIOS:
        rows = {row.condition: row for row in summary_rows if row.scenario == scenario.index}
        selected = rows["selected_tool_access"]
        no_tool = rows["no_tool_baseline"]
        ablated = rows["selected_tool_ablation"]
        gain = selected.mean_reward - no_tool.mean_reward
        ablation_loss = selected.mean_reward - ablated.mean_reward
        selection = selection_by_scenario[scenario.index]
        if not scenario.expected_tool_pressure:
            supports = gain < 4.0 and ablation_loss < 4.0 and selected.mean_tools_built < 1.25
            verdict = "tools_not_selected_when_affordance_not_useful" if supports else "tool_pressure_leaks_into_control"
        else:
            supports = (
                selection.selected_uses_tools
                and selected.mean_tools_built >= 1.0
                and gain > 10.0
                and ablation_loss > 8.0
                and selected.mean_survival_fraction >= ablated.mean_survival_fraction - 0.08
            )
            verdict = "external_tools_reduce_confusion_or_preserve_options" if supports else "tool_access_not_specific_or_not_useful"
        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                expected_pressure=scenario.pressure,
                selected_policy=selection.selected_policy,
                selected_uses_tools=selection.selected_uses_tools,
                selected_reward=selected.mean_reward,
                no_tool_reward=no_tool.mean_reward,
                tool_ablation_reward=ablated.mean_reward,
                tool_gain_over_no_tool=gain,
                tool_access_ablation_loss=ablation_loss,
                selected_tools_built=selected.mean_tools_built,
                external_memory_recovery_rate=selected.external_memory_recovery_rate,
                supports_tool_making_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def run_experiment(
    cfg: ToolConfig,
) -> Tuple[List[EpisodeResult], List[PolicySelectionRow], List[SummaryRow], List[VerdictRow], Dict[str, object]]:
    selected, selection_rows = select_policies(cfg)
    no_tool = policy_candidates(cfg)[0]
    spam = next(policy for policy in policy_candidates(cfg) if policy.name == "tool_spam_control")
    episode_rows: List[EpisodeResult] = []
    summary_rows: List[SummaryRow] = []
    trace: Optional[Dict[str, object]] = None
    for scenario in SCENARIOS:
        selected_policy = selected[scenario.index]
        conditions = [
            ("no_tool_baseline", no_tool, False),
            ("selected_tool_access", selected_policy, selected_policy.tool_enabled),
            ("selected_tool_ablation", selected_policy, False),
            ("tool_spam_control", spam, True),
        ]
        for condition, policy, allow_tools in conditions:
            rows = evaluate_policy(scenario, policy, cfg.eval_episodes, cfg, condition, allow_tools, episode_offset=10_000)
            episode_rows.extend(rows)
            summary_rows.append(summarize(rows, scenario, condition, policy.name))
        if scenario.index == cfg.trace_scenario:
            trace_result, trace = run_episode(
                scenario,
                selected_policy,
                cfg.trace_episode + 20_000,
                cfg,
                "selected_tool_access",
                selected_policy.tool_enabled,
                collect_trace=True,
            )
            episode_rows.append(trace_result)
    verdicts = build_verdicts(summary_rows, selection_rows)
    diagnostics = {
        "note": (
            "Tool actions are available affordances, not explicit objectives. "
            "Policies are selected by episode return and then evaluated with tool access ablated."
        ),
        "candidate_count": len(policy_candidates(cfg)),
        "trace": trace,
    }
    return episode_rows, selection_rows, summary_rows, verdicts, diagnostics


def write_csv(path: Path, rows: Iterable[object]) -> None:
    rows = list(rows)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()), lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def print_table(verdicts: Sequence[VerdictRow]) -> None:
    headers = [
        "scenario",
        "scenario_name",
        "selected_policy",
        "selected_reward",
        "no_tool_reward",
        "tool_gain",
        "ablation_loss",
        "tools_built",
        "supports_tool_making_precursor",
    ]
    rows = [
        [
            str(row.scenario),
            row.scenario_name,
            row.selected_policy,
            f"{row.selected_reward:.3f}",
            f"{row.no_tool_reward:.3f}",
            f"{row.tool_gain_over_no_tool:.3f}",
            f"{row.tool_access_ablation_loss:.3f}",
            f"{row.selected_tools_built:.3f}",
            str(row.supports_tool_making_precursor),
        ]
        for row in verdicts
    ]
    widths = [max(len(header), *(len(row[index]) for row in rows)) for index, header in enumerate(headers)]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> ToolConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-episodes", type=int, default=48)
    parser.add_argument("--eval-episodes", type=int, default=72)
    parser.add_argument("--ticks", type=int, default=300)
    parser.add_argument("--seed", type=int, default=20260610)
    parser.add_argument("--world-size", type=float, default=88.0)
    parser.add_argument("--candidate-count", type=int, default=180)
    parser.add_argument("--trace-scenario", type=int, default=3)
    parser.add_argument("--trace-episode", type=int, default=0)
    args = parser.parse_args()
    if args.train_episodes < 8:
        raise SystemExit("--train-episodes must be at least 8")
    if args.eval_episodes < 8:
        raise SystemExit("--eval-episodes must be at least 8")
    if args.ticks < 80:
        raise SystemExit("--ticks must be at least 80")
    if args.candidate_count < 12:
        raise SystemExit("--candidate-count must be at least 12")
    if args.trace_scenario not in {scenario.index for scenario in SCENARIOS}:
        raise SystemExit("--trace-scenario out of range")
    return ToolConfig(
        train_episodes=args.train_episodes,
        eval_episodes=args.eval_episodes,
        ticks=args.ticks,
        seed=args.seed,
        world_size=args.world_size,
        candidate_count=args.candidate_count,
        trace_scenario=args.trace_scenario,
        trace_episode=args.trace_episode,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    episode_rows, selection_rows, summary_rows, verdicts, diagnostics = run_experiment(cfg)
    episode_path = ARTIFACT_DIR / "ssrm_3d_tool_making_eval.csv"
    selection_path = ARTIFACT_DIR / "ssrm_3d_tool_making_policy_selection.csv"
    summary_path = ARTIFACT_DIR / "ssrm_3d_tool_making_summary.csv"
    verdict_path = ARTIFACT_DIR / "ssrm_3d_tool_making_verdict.csv"
    results_path = ARTIFACT_DIR / "ssrm_3d_tool_making_results.json"
    trace_path = ARTIFACT_DIR / "ssrm_3d_tool_making_trace.json"
    write_csv(episode_path, episode_rows)
    write_csv(selection_path, selection_rows)
    write_csv(summary_path, summary_rows)
    write_csv(verdict_path, verdicts)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "config": asdict(cfg),
                "selection": [asdict(row) for row in selection_rows],
                "summary": [asdict(row) for row in summary_rows],
                "verdict": [asdict(row) for row in verdicts],
                "diagnostics": {key: value for key, value in diagnostics.items() if key != "trace"},
            },
            handle,
            indent=2,
        )
        handle.write("\n")
    with trace_path.open("w", encoding="utf-8") as handle:
        json.dump(diagnostics["trace"], handle, indent=2)
        handle.write("\n")
    print(f"wrote {episode_path}")
    print(f"wrote {selection_path}")
    print(f"wrote {summary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print(f"wrote {trace_path}")
    print_table(verdicts)
    return 0 if all(row.supports_tool_making_precursor for row in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
