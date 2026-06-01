#!/usr/bin/env python3
"""SSRM-3D injury/disability adaptation precursor.

This experiment implements the ninth pressure-layer step from report 74:
injury and disability adaptation. It is intentionally not biology or roleplay.

Limping, sensor loss, wound infection risk, repair/help seeking, compensation
tools, route adaptation, and continuity are treated as abstract control
variables. The useful result is narrow: disability machinery should be rejected
in a fixed-body control, then become useful only when changed capability alters
future action feasibility, perception, social access, or restore-time control.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


ARTIFACT_DIR = Path("artifacts")


@dataclass(frozen=True)
class DisabilityConfig:
    train_episodes: int = 72
    eval_episodes: int = 96
    ticks: int = 210
    seed: int = 20260628
    candidate_count: int = 7
    trace_scenario: int = 4
    trace_episode: int = 0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    expected_capability_state: bool
    expected_motor_adaptation: bool
    expected_sensor_compensation: bool
    expected_infection_management: bool
    expected_repair_access: bool
    expected_help_seeking: bool
    expected_compensation_tools: bool
    expected_route_adaptation: bool
    expected_continuity: bool
    motor_damage: float
    vision_damage: float
    hearing_damage: float
    infection_pressure: float
    terrain_complexity: float
    social_help_pressure: float
    tool_value: float
    required_progress: float
    work_rate: float
    restore_tick: int


@dataclass(frozen=True)
class Policy:
    name: str
    capability_state: bool
    motor_adaptation: bool
    sensor_compensation: bool
    infection_management: bool
    repair_access: bool
    help_seeking: bool
    compensation_tools: bool
    route_adaptation: bool
    continuity_memory: bool
    risk_threshold: float
    tool_bias: float
    help_bias: float
    route_bias: float


@dataclass(frozen=True)
class EpisodeResult:
    scenario: int
    scenario_name: str
    policy_name: str
    condition: str
    episode: int
    total_reward: float
    survival: float
    task_success: float
    progress: float
    energy: float
    integrity: float
    mobility: float
    vision_quality: float
    hearing_quality: float
    infection_load: float
    pain_stress: float
    tool_support: float
    help_support: float
    route_fit: float
    exposure_risk: float
    falls: int
    collisions: int
    infection_events: int
    repair_actions: int
    help_actions: int
    tool_actions: int
    route_actions: int
    pace_actions: int
    continuity_resets: int
    disability_misses: int


@dataclass(frozen=True)
class PolicySelectionRow:
    scenario: int
    scenario_name: str
    selected_policy: str
    selected_uses_capability_state: bool
    selected_uses_motor_adaptation: bool
    selected_uses_sensor_compensation: bool
    selected_uses_infection_management: bool
    selected_uses_repair_access: bool
    selected_uses_help_seeking: bool
    selected_uses_compensation_tools: bool
    selected_uses_route_adaptation: bool
    selected_uses_continuity: bool
    train_reward: float
    ignore_train_reward: float
    train_gain_over_ignore: float


@dataclass(frozen=True)
class SummaryRow:
    scenario: int
    scenario_name: str
    pressure: str
    condition: str
    policy_name: str
    mean_reward: float
    mean_survival: float
    mean_task_success: float
    mean_progress: float
    mean_energy: float
    mean_integrity: float
    mean_mobility: float
    mean_vision_quality: float
    mean_hearing_quality: float
    mean_infection_load: float
    mean_pain_stress: float
    mean_tool_support: float
    mean_help_support: float
    mean_route_fit: float
    mean_exposure_risk: float
    mean_falls: float
    mean_collisions: float
    mean_infection_events: float
    mean_repair_actions: float
    mean_help_actions: float
    mean_tool_actions: float
    mean_route_actions: float
    mean_pace_actions: float
    mean_continuity_resets: float
    mean_disability_misses: float


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    expected_pressure: str
    selected_policy: str
    selected_reward: float
    no_capability_state_reward: float
    no_motor_adaptation_reward: float
    no_sensor_compensation_reward: float
    no_infection_management_reward: float
    no_repair_access_reward: float
    no_help_seeking_reward: float
    no_compensation_tools_reward: float
    no_route_adaptation_reward: float
    no_continuity_reward: float
    ignore_disability_baseline_reward: float
    omniscient_disability_control_reward: float
    no_capability_state_loss: float
    no_motor_adaptation_loss: float
    no_sensor_compensation_loss: float
    no_infection_management_loss: float
    no_repair_access_loss: float
    no_help_seeking_loss: float
    no_compensation_tools_loss: float
    no_route_adaptation_loss: float
    no_continuity_loss: float
    ignore_disability_baseline_loss: float
    selected_falls: float
    selected_collisions: float
    selected_infection_events: float
    selected_repair_actions: float
    selected_help_actions: float
    selected_tool_actions: float
    selected_route_actions: float
    supports_injury_disability_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        index=0,
        name="fixed_body_control",
        pressure="fixed body and clear route where disability machinery should not matter",
        expected_capability_state=False,
        expected_motor_adaptation=False,
        expected_sensor_compensation=False,
        expected_infection_management=False,
        expected_repair_access=False,
        expected_help_seeking=False,
        expected_compensation_tools=False,
        expected_route_adaptation=False,
        expected_continuity=False,
        motor_damage=0.0,
        vision_damage=0.0,
        hearing_damage=0.0,
        infection_pressure=0.0,
        terrain_complexity=0.08,
        social_help_pressure=0.0,
        tool_value=0.0,
        required_progress=122.0,
        work_rate=0.73,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=1,
        name="limp_route_adaptation",
        pressure="limping changes feasible routes, making capability state, pacing, route changes, and support tools useful",
        expected_capability_state=True,
        expected_motor_adaptation=True,
        expected_sensor_compensation=False,
        expected_infection_management=False,
        expected_repair_access=False,
        expected_help_seeking=False,
        expected_compensation_tools=True,
        expected_route_adaptation=True,
        expected_continuity=False,
        motor_damage=0.78,
        vision_damage=0.05,
        hearing_damage=0.04,
        infection_pressure=0.10,
        terrain_complexity=0.72,
        social_help_pressure=0.05,
        tool_value=0.70,
        required_progress=88.0,
        work_rate=0.56,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=2,
        name="vision_hearing_damage",
        pressure="vision and hearing loss make sensor compensation, tools, and safer routes necessary",
        expected_capability_state=True,
        expected_motor_adaptation=False,
        expected_sensor_compensation=True,
        expected_infection_management=False,
        expected_repair_access=False,
        expected_help_seeking=False,
        expected_compensation_tools=True,
        expected_route_adaptation=True,
        expected_continuity=False,
        motor_damage=0.12,
        vision_damage=0.82,
        hearing_damage=0.74,
        infection_pressure=0.08,
        terrain_complexity=0.70,
        social_help_pressure=0.05,
        tool_value=0.78,
        required_progress=86.0,
        work_rate=0.55,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=3,
        name="wound_infection_repair",
        pressure="wound infection risk makes hidden damage state, treatment timing, repair access, and pacing useful",
        expected_capability_state=True,
        expected_motor_adaptation=True,
        expected_sensor_compensation=False,
        expected_infection_management=True,
        expected_repair_access=True,
        expected_help_seeking=False,
        expected_compensation_tools=False,
        expected_route_adaptation=False,
        expected_continuity=False,
        motor_damage=0.38,
        vision_damage=0.05,
        hearing_damage=0.05,
        infection_pressure=0.88,
        terrain_complexity=0.32,
        social_help_pressure=0.08,
        tool_value=0.12,
        required_progress=82.0,
        work_rate=0.53,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=4,
        name="social_help_compensation",
        pressure="combined damage makes help-seeking, compensation tools, and route adaptation preserve future action",
        expected_capability_state=True,
        expected_motor_adaptation=True,
        expected_sensor_compensation=True,
        expected_infection_management=False,
        expected_repair_access=False,
        expected_help_seeking=True,
        expected_compensation_tools=True,
        expected_route_adaptation=True,
        expected_continuity=False,
        motor_damage=0.58,
        vision_damage=0.48,
        hearing_damage=0.36,
        infection_pressure=0.18,
        terrain_complexity=0.76,
        social_help_pressure=0.82,
        tool_value=0.84,
        required_progress=80.0,
        work_rate=0.52,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=5,
        name="restore_disability_continuity",
        pressure="after restore, known damage, repair history, tools, help, and route adaptations must survive",
        expected_capability_state=True,
        expected_motor_adaptation=True,
        expected_sensor_compensation=True,
        expected_infection_management=True,
        expected_repair_access=True,
        expected_help_seeking=True,
        expected_compensation_tools=True,
        expected_route_adaptation=True,
        expected_continuity=True,
        motor_damage=0.58,
        vision_damage=0.50,
        hearing_damage=0.48,
        infection_pressure=0.58,
        terrain_complexity=0.72,
        social_help_pressure=0.64,
        tool_value=0.78,
        required_progress=72.0,
        work_rate=0.50,
        restore_tick=96,
    ),
)


SEEDED_POLICIES = (
    Policy(
        name="ignore_disability_baseline",
        capability_state=False,
        motor_adaptation=False,
        sensor_compensation=False,
        infection_management=False,
        repair_access=False,
        help_seeking=False,
        compensation_tools=False,
        route_adaptation=False,
        continuity_memory=False,
        risk_threshold=0.88,
        tool_bias=0.04,
        help_bias=0.04,
        route_bias=0.04,
    ),
    Policy(
        name="reactive_damage_runner",
        capability_state=True,
        motor_adaptation=False,
        sensor_compensation=False,
        infection_management=False,
        repair_access=False,
        help_seeking=False,
        compensation_tools=False,
        route_adaptation=True,
        continuity_memory=False,
        risk_threshold=0.62,
        tool_bias=0.12,
        help_bias=0.04,
        route_bias=0.34,
    ),
    Policy(
        name="limp_route_tool_planner",
        capability_state=True,
        motor_adaptation=True,
        sensor_compensation=False,
        infection_management=False,
        repair_access=False,
        help_seeking=False,
        compensation_tools=True,
        route_adaptation=True,
        continuity_memory=False,
        risk_threshold=0.32,
        tool_bias=0.82,
        help_bias=0.04,
        route_bias=0.78,
    ),
    Policy(
        name="sensor_compensation_planner",
        capability_state=True,
        motor_adaptation=False,
        sensor_compensation=True,
        infection_management=False,
        repair_access=False,
        help_seeking=False,
        compensation_tools=True,
        route_adaptation=True,
        continuity_memory=False,
        risk_threshold=0.30,
        tool_bias=0.84,
        help_bias=0.04,
        route_bias=0.72,
    ),
    Policy(
        name="infection_repair_planner",
        capability_state=True,
        motor_adaptation=True,
        sensor_compensation=False,
        infection_management=True,
        repair_access=True,
        help_seeking=False,
        compensation_tools=False,
        route_adaptation=False,
        continuity_memory=False,
        risk_threshold=0.28,
        tool_bias=0.08,
        help_bias=0.04,
        route_bias=0.12,
    ),
    Policy(
        name="help_tool_route_planner",
        capability_state=True,
        motor_adaptation=True,
        sensor_compensation=True,
        infection_management=False,
        repair_access=False,
        help_seeking=True,
        compensation_tools=True,
        route_adaptation=True,
        continuity_memory=False,
        risk_threshold=0.34,
        tool_bias=0.82,
        help_bias=0.84,
        route_bias=0.74,
    ),
    Policy(
        name="continuity_disability_planner",
        capability_state=True,
        motor_adaptation=True,
        sensor_compensation=True,
        infection_management=True,
        repair_access=True,
        help_seeking=True,
        compensation_tools=True,
        route_adaptation=True,
        continuity_memory=True,
        risk_threshold=0.34,
        tool_bias=0.80,
        help_bias=0.80,
        route_bias=0.74,
    ),
)


CONDITIONS = (
    "full_control",
    "no_capability_state",
    "no_motor_adaptation",
    "no_sensor_compensation",
    "no_infection_management",
    "no_repair_access",
    "no_help_seeking",
    "no_compensation_tools",
    "no_route_adaptation",
    "no_continuity",
    "ignore_disability_baseline",
    "omniscient_disability_control",
)


def stable_hash(text: str) -> int:
    value = 0
    for char in text:
        value = (value * 131 + ord(char)) % 1_000_003
    return value


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def build_policies(cfg: DisabilityConfig) -> List[Policy]:
    policies = list(SEEDED_POLICIES)
    rng = random.Random(cfg.seed + 1709)
    while len(policies) < cfg.candidate_count:
        base = rng.choice(SEEDED_POLICIES[2:])
        policies.append(
            Policy(
                name=f"mutant_disability_{len(policies)}",
                capability_state=base.capability_state if rng.random() > 0.12 else not base.capability_state,
                motor_adaptation=base.motor_adaptation if rng.random() > 0.16 else not base.motor_adaptation,
                sensor_compensation=base.sensor_compensation if rng.random() > 0.16 else not base.sensor_compensation,
                infection_management=base.infection_management if rng.random() > 0.16 else not base.infection_management,
                repair_access=base.repair_access if rng.random() > 0.16 else not base.repair_access,
                help_seeking=base.help_seeking if rng.random() > 0.18 else not base.help_seeking,
                compensation_tools=base.compensation_tools if rng.random() > 0.16 else not base.compensation_tools,
                route_adaptation=base.route_adaptation if rng.random() > 0.16 else not base.route_adaptation,
                continuity_memory=base.continuity_memory if rng.random() > 0.18 else not base.continuity_memory,
                risk_threshold=clamp(base.risk_threshold + rng.uniform(-0.08, 0.08), 0.16, 0.92),
                tool_bias=clamp(base.tool_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
                help_bias=clamp(base.help_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
                route_bias=clamp(base.route_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
            )
        )
    return policies


def condition_policy(policy: Policy, condition: str) -> Policy:
    if condition == "omniscient_disability_control":
        return Policy(
            name=policy.name,
            capability_state=True,
            motor_adaptation=True,
            sensor_compensation=True,
            infection_management=True,
            repair_access=True,
            help_seeking=True,
            compensation_tools=True,
            route_adaptation=True,
            continuity_memory=True,
            risk_threshold=0.12,
            tool_bias=max(policy.tool_bias, 0.92),
            help_bias=max(policy.help_bias, 0.92),
            route_bias=max(policy.route_bias, 0.92),
        )
    if condition == "ignore_disability_baseline":
        return Policy(
            name=policy.name,
            capability_state=False,
            motor_adaptation=False,
            sensor_compensation=False,
            infection_management=False,
            repair_access=False,
            help_seeking=False,
            compensation_tools=False,
            route_adaptation=False,
            continuity_memory=False,
            risk_threshold=0.88,
            tool_bias=0.04,
            help_bias=0.04,
            route_bias=0.04,
        )
    return Policy(
        name=policy.name,
        capability_state=policy.capability_state and condition != "no_capability_state",
        motor_adaptation=policy.motor_adaptation and condition != "no_motor_adaptation",
        sensor_compensation=policy.sensor_compensation and condition != "no_sensor_compensation",
        infection_management=policy.infection_management and condition != "no_infection_management",
        repair_access=policy.repair_access and condition != "no_repair_access",
        help_seeking=policy.help_seeking and condition != "no_help_seeking",
        compensation_tools=policy.compensation_tools and condition != "no_compensation_tools",
        route_adaptation=policy.route_adaptation and condition != "no_route_adaptation",
        continuity_memory=policy.continuity_memory and condition != "no_continuity",
        risk_threshold=policy.risk_threshold,
        tool_bias=policy.tool_bias,
        help_bias=policy.help_bias,
        route_bias=policy.route_bias,
    )


def scenario_seed(
    cfg: DisabilityConfig,
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episode: int,
    phase: str,
) -> int:
    return (
        cfg.seed
        + scenario.index * 100_003
        + stable_hash(policy.name) * 17
        + stable_hash(condition) * 31
        + episode * 997
        + stable_hash(phase) * 43
    )


def feature_overhead(policy: Policy) -> float:
    weighted_flags = [
        (policy.capability_state, 2.40),
        (policy.motor_adaptation, 2.70),
        (policy.sensor_compensation, 2.70),
        (policy.infection_management, 2.80),
        (policy.repair_access, 2.60),
        (policy.help_seeking, 3.10),
        (policy.compensation_tools, 2.80),
        (policy.route_adaptation, 2.50),
        (policy.continuity_memory, 8.80),
    ]
    return sum(weight for enabled, weight in weighted_flags if enabled)


def estimate_risk(
    scenario: ScenarioSpec,
    policy: Policy,
    mobility: float,
    vision: float,
    hearing: float,
    infection: float,
    tool_support: float,
    help_support: float,
    route_fit: float,
    exposure: float,
) -> float:
    if not policy.capability_state:
        observed_mobility = 0.78
        observed_vision = 0.80
        observed_hearing = 0.80
        observed_infection = 0.16
    else:
        observed_mobility = mobility
        observed_vision = vision
        observed_hearing = hearing
        observed_infection = infection
    disability_load = (
        scenario.motor_damage * (1.0 - observed_mobility) * 0.72
        + scenario.vision_damage * (1.0 - observed_vision) * 0.58
        + scenario.hearing_damage * (1.0 - observed_hearing) * 0.46
        + scenario.infection_pressure * observed_infection * 0.62
        + scenario.terrain_complexity * (1.0 - route_fit) * 0.38
        + scenario.social_help_pressure * (1.0 - help_support) * 0.34
        + scenario.tool_value * (1.0 - tool_support) * 0.30
        + exposure * 0.34
    )
    mitigation = (
        (0.12 if policy.motor_adaptation else 0.0)
        + (0.12 if policy.sensor_compensation else 0.0)
        + (0.12 if policy.infection_management else 0.0)
        + (0.10 if policy.repair_access else 0.0)
        + (0.11 if policy.help_seeking else 0.0)
        + (0.11 if policy.compensation_tools else 0.0)
        + (0.10 if policy.route_adaptation else 0.0)
    )
    return clamp(disability_load - mitigation, 0.0, 1.8)


def choose_action(
    scenario: ScenarioSpec,
    policy: Policy,
    risk: float,
    mobility: float,
    vision: float,
    hearing: float,
    infection: float,
    tool_support: float,
    help_support: float,
    route_fit: float,
    tick: int,
) -> str:
    if scenario.index == 0:
        return "work"
    if policy.help_seeking and scenario.expected_help_seeking and help_support < 0.60 and risk > policy.risk_threshold * 0.74:
        return "request_help"
    if policy.repair_access and scenario.expected_repair_access and infection > 0.24 and risk > policy.risk_threshold * 0.56:
        return "seek_repair"
    if policy.compensation_tools and scenario.expected_compensation_tools and tool_support < 0.62 and risk > policy.risk_threshold * 0.70:
        return "use_compensation_tool"
    if policy.route_adaptation and scenario.expected_route_adaptation and route_fit < 0.66 and risk > policy.risk_threshold * 0.78:
        return "adapt_route"
    if policy.motor_adaptation and scenario.expected_motor_adaptation and mobility < 0.64 and tick % 9 == 0:
        return "pace_recovery"
    if policy.sensor_compensation and scenario.expected_sensor_compensation and (vision < 0.62 or hearing < 0.62) and tick % 11 == 0:
        return "scan_slowly"
    return "work"


def add_trace(
    trace: List[Dict[str, object]],
    tick: int,
    action: str,
    progress: float,
    energy: float,
    integrity: float,
    mobility: float,
    vision: float,
    hearing: float,
    infection: float,
    stress: float,
    tool: float,
    help_level: float,
    route: float,
    exposure: float,
    falls: int,
    collisions: int,
    notes: List[str],
) -> None:
    trace.append(
        {
            "tick": tick,
            "action": action,
            "progress": round(progress, 3),
            "energy": round(energy, 3),
            "integrity": round(integrity, 3),
            "mobility": round(mobility, 3),
            "vision_quality": round(vision, 3),
            "hearing_quality": round(hearing, 3),
            "infection_load": round(infection, 3),
            "pain_stress": round(stress, 3),
            "tool_support": round(tool, 3),
            "help_support": round(help_level, 3),
            "route_fit": round(route, 3),
            "exposure_risk": round(exposure, 3),
            "falls": falls,
            "collisions": collisions,
            "notes": list(notes[-3:]),
        }
    )


def simulate_episode(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episode: int,
    cfg: DisabilityConfig,
    phase: str,
    collect_trace: bool = False,
) -> Tuple[EpisodeResult, List[Dict[str, object]]]:
    effective = condition_policy(policy, condition)
    rng = random.Random(scenario_seed(cfg, scenario, policy, condition, episode, phase))

    mobility = clamp(0.98 - scenario.motor_damage * 0.32 + rng.uniform(-0.015, 0.015), 0.05, 1.0)
    vision = clamp(0.98 - scenario.vision_damage * 0.34 + rng.uniform(-0.015, 0.015), 0.05, 1.0)
    hearing = clamp(0.98 - scenario.hearing_damage * 0.32 + rng.uniform(-0.015, 0.015), 0.05, 1.0)
    infection = clamp(0.06 + scenario.infection_pressure * 0.18 + rng.uniform(-0.010, 0.010), 0.0, 1.2)
    integrity = clamp(0.98 - scenario.motor_damage * 0.08 - scenario.infection_pressure * 0.05, 0.0, 1.0)
    energy = clamp(0.96 - scenario.motor_damage * 0.04 + rng.uniform(-0.012, 0.012), 0.0, 1.0)
    stress = 0.0
    tool_support = 0.12 if scenario.expected_compensation_tools else 0.80
    help_support = 0.18 if scenario.expected_help_seeking else 0.82
    route_fit = 0.26 if scenario.expected_route_adaptation else 0.82
    exposure = 0.0
    progress = 0.0
    collapsed = False
    notes: List[str] = []
    trace_frames: List[Dict[str, object]] = []

    falls = 0
    collisions = 0
    infection_events = 0
    repair_actions = 0
    help_actions = 0
    tool_actions = 0
    route_actions = 0
    pace_actions = 0
    continuity_resets = 0
    disability_misses = 0

    for tick in range(cfg.ticks):
        action = "work"
        if scenario.restore_tick == tick and not effective.continuity_memory:
            continuity_resets += 1
            disability_misses += 5
            tool_support = max(0.04, tool_support - 0.36)
            help_support = max(0.04, help_support - 0.36)
            route_fit = max(0.04, route_fit - 0.34)
            infection = clamp(infection + 0.22, 0.0, 1.2)
            exposure = clamp(exposure + 0.26, 0.0, 1.8)
            notes.append("restore erased disability continuity")
            action = "restore_reset"

        risk = estimate_risk(
            scenario,
            effective,
            mobility,
            vision,
            hearing,
            infection,
            tool_support,
            help_support,
            route_fit,
            exposure,
        )
        if not collapsed and action != "restore_reset":
            action = choose_action(
                scenario,
                effective,
                risk,
                mobility,
                vision,
                hearing,
                infection,
                tool_support,
                help_support,
                route_fit,
                tick,
            )

        if collapsed:
            action = "collapsed"
        elif action == "request_help":
            help_actions += 1
            help_support = clamp(help_support + 0.34 + effective.help_bias * 0.18, 0.0, 1.0)
            exposure = clamp(exposure - 0.06, 0.0, 1.8)
            energy = clamp(energy - 0.006, 0.0, 1.0)
            progress -= 0.14
            notes.append("help request preserved capability")
        elif action == "seek_repair":
            repair_actions += 1
            infection = clamp(infection - 0.20, 0.0, 1.2)
            integrity = clamp(integrity + 0.07, 0.0, 1.0)
            stress = clamp(stress - 0.04, 0.0, 1.0)
            progress -= 0.20
            notes.append("repair reduced infection risk")
        elif action == "use_compensation_tool":
            tool_actions += 1
            tool_support = clamp(tool_support + 0.34 + effective.tool_bias * 0.18, 0.0, 1.0)
            mobility = clamp(mobility + scenario.motor_damage * 0.020, 0.0, 1.0)
            vision = clamp(vision + scenario.vision_damage * 0.016, 0.0, 1.0)
            hearing = clamp(hearing + scenario.hearing_damage * 0.014, 0.0, 1.0)
            progress -= 0.14
            notes.append("tool compensated damaged capability")
        elif action == "adapt_route":
            route_actions += 1
            route_fit = clamp(route_fit + 0.30 + effective.route_bias * 0.16, 0.0, 1.0)
            exposure = clamp(exposure - 0.08, 0.0, 1.8)
            progress -= 0.16
            notes.append("route adapted to current body")
        elif action == "pace_recovery":
            pace_actions += 1
            mobility = clamp(mobility + 0.018, 0.0, 1.0)
            energy = clamp(energy + 0.012, 0.0, 1.0)
            stress = clamp(stress - 0.025, 0.0, 1.0)
            progress += scenario.work_rate * 0.08
            notes.append("pacing preserved damaged mobility")
        elif action == "scan_slowly":
            pace_actions += 1
            exposure = clamp(exposure - 0.05, 0.0, 1.8)
            vision = clamp(vision + 0.006, 0.0, 1.0)
            hearing = clamp(hearing + 0.006, 0.0, 1.0)
            progress += scenario.work_rate * 0.12
            notes.append("slow scan compensated sensor loss")
        elif action == "work":
            capability = clamp(
                0.90
                + energy * 0.08
                + mobility * 0.18
                + vision * 0.07
                + hearing * 0.05
                + route_fit * 0.08
                + tool_support * scenario.tool_value * 0.04
                + help_support * scenario.social_help_pressure * 0.04
                - infection * 0.16
                - stress * 0.10
                - exposure * 0.10,
                0.04,
                1.10,
            )
            progress += scenario.work_rate * capability
            exposure = clamp(
                exposure
                + scenario.terrain_complexity * (1.0 - route_fit) * 0.004
                + scenario.motor_damage * (1.0 - mobility) * 0.004
                + scenario.vision_damage * (1.0 - vision) * 0.003
                + scenario.hearing_damage * (1.0 - hearing) * 0.002,
                0.0,
                1.8,
            )

        if scenario.expected_capability_state and not effective.capability_state:
            disability_misses += 1 if tick % 17 == 0 else 0
            exposure = clamp(exposure + 0.006, 0.0, 1.8)
        if scenario.expected_motor_adaptation:
            if effective.motor_adaptation:
                mobility = clamp(mobility - scenario.motor_damage * 0.0007, 0.0, 1.0)
            else:
                mobility = clamp(mobility - scenario.motor_damage * 0.0038, 0.0, 1.0)
                exposure = clamp(exposure + scenario.motor_damage * 0.008, 0.0, 1.8)
                if tick % 19 == 0:
                    falls += 1
                    integrity = clamp(integrity - 0.028, 0.0, 1.0)
                    disability_misses += 1
        if scenario.expected_sensor_compensation:
            if effective.sensor_compensation:
                vision = clamp(vision - scenario.vision_damage * 0.0006, 0.0, 1.0)
                hearing = clamp(hearing - scenario.hearing_damage * 0.0006, 0.0, 1.0)
            else:
                vision = clamp(vision - scenario.vision_damage * 0.0024, 0.0, 1.0)
                hearing = clamp(hearing - scenario.hearing_damage * 0.0022, 0.0, 1.0)
                exposure = clamp(exposure + (scenario.vision_damage + scenario.hearing_damage) * 0.005, 0.0, 1.8)
                if tick % 17 == 0:
                    collisions += 1
                    integrity = clamp(integrity - 0.020, 0.0, 1.0)
                    disability_misses += 1
        if scenario.expected_infection_management:
            if effective.infection_management:
                infection = clamp(infection + scenario.infection_pressure * 0.0012, 0.0, 1.2)
            else:
                infection = clamp(infection + scenario.infection_pressure * 0.0065, 0.0, 1.2)
                stress = clamp(stress + scenario.infection_pressure * 0.004, 0.0, 1.0)
                if tick % 13 == 0:
                    infection_events += 1
                    disability_misses += 1
        if scenario.expected_repair_access and not effective.repair_access:
            infection = clamp(infection + scenario.infection_pressure * 0.0060, 0.0, 1.2)
            integrity = clamp(integrity - scenario.infection_pressure * 0.0026, 0.0, 1.0)
            exposure = clamp(exposure + scenario.infection_pressure * 0.0035, 0.0, 1.8)
            disability_misses += 1 if tick % 23 == 0 else 0
        if scenario.expected_help_seeking:
            if effective.help_seeking:
                help_support = clamp(help_support - scenario.social_help_pressure * 0.0012, 0.0, 1.0)
            else:
                help_support = clamp(help_support - scenario.social_help_pressure * 0.0065, 0.0, 1.0)
                exposure = clamp(exposure + scenario.social_help_pressure * 0.008, 0.0, 1.8)
                disability_misses += 1 if tick % 19 == 0 else 0
        if scenario.expected_compensation_tools:
            if effective.compensation_tools:
                tool_support = clamp(tool_support - scenario.tool_value * 0.0012, 0.0, 1.0)
            else:
                tool_support = clamp(tool_support - scenario.tool_value * 0.008, 0.0, 1.0)
                exposure = clamp(exposure + scenario.tool_value * 0.011, 0.0, 1.8)
                disability_misses += 1 if tick % 19 == 0 else 0
        if scenario.expected_route_adaptation:
            if effective.route_adaptation:
                route_fit = clamp(route_fit - scenario.terrain_complexity * 0.0010, 0.0, 1.0)
            else:
                route_fit = clamp(route_fit - scenario.terrain_complexity * 0.006, 0.0, 1.0)
                exposure = clamp(exposure + scenario.terrain_complexity * 0.008, 0.0, 1.8)
                disability_misses += 1 if tick % 17 == 0 else 0

        if action in {"request_help", "use_compensation_tool", "adapt_route", "seek_repair"}:
            stress = clamp(stress - 0.018, 0.0, 1.0)
        stress = clamp(
            stress
            + exposure * 0.0012
            + infection * 0.0010
            + max(0.0, 0.52 - mobility) * 0.0012
            + max(0.0, 0.52 - vision) * 0.0008
            + max(0.0, 0.52 - hearing) * 0.0007,
            0.0,
            1.0,
        )
        energy = clamp(
            energy
            - 0.0010
            - infection * 0.0012
            - stress * 0.0010
            - max(0.0, 0.58 - mobility) * 0.0010
            + (0.0010 if action in {"pace_recovery", "scan_slowly"} else 0.0),
            0.0,
            1.0,
        )
        integrity = clamp(integrity - infection * 0.0008 - exposure * 0.0008 - stress * 0.0005, 0.0, 1.0)
        if integrity <= 0.08 or energy <= 0.04 or infection >= 1.08:
            collapsed = True

        if collect_trace and (tick % 5 == 0 or tick == cfg.ticks - 1 or action != "work"):
            add_trace(
                trace_frames,
                tick,
                action,
                progress,
                energy,
                integrity,
                mobility,
                vision,
                hearing,
                infection,
                stress,
                tool_support,
                help_support,
                route_fit,
                exposure,
                falls,
                collisions,
                notes,
            )

    task_success = progress >= scenario.required_progress and not collapsed
    survival = 1.0 if not collapsed and integrity > 0.12 and energy > 0.06 and infection < 1.0 else 0.0

    reward = progress
    reward += 34.0 if task_success else -24.0
    reward += 42.0 if survival else -116.0
    reward += energy * 18.0
    reward += integrity * 20.0
    reward += mobility * (12.0 if scenario.expected_motor_adaptation else 2.0)
    reward += (vision + hearing) * (8.0 if scenario.expected_sensor_compensation else 1.0)
    reward += tool_support * (19.0 if scenario.expected_compensation_tools else 1.0)
    reward += help_support * (16.0 if scenario.expected_help_seeking else 1.0)
    reward += route_fit * (14.0 if scenario.expected_route_adaptation else 1.0)
    reward -= infection * 86.0
    reward -= stress * 34.0
    reward -= exposure * 68.0
    reward -= falls * 7.0
    reward -= collisions * 6.0
    reward -= infection_events * 3.6
    reward -= disability_misses * 0.85
    reward -= repair_actions * 0.20
    reward -= help_actions * 0.20
    reward -= tool_actions * 0.18
    reward -= route_actions * 0.18
    reward -= pace_actions * 0.10
    reward -= feature_overhead(effective)
    if scenario.expected_continuity and continuity_resets:
        reward -= 54.0

    result = EpisodeResult(
        scenario=scenario.index,
        scenario_name=scenario.name,
        policy_name=policy.name,
        condition=condition,
        episode=episode,
        total_reward=reward,
        survival=survival,
        task_success=1.0 if task_success else 0.0,
        progress=progress,
        energy=energy,
        integrity=integrity,
        mobility=mobility,
        vision_quality=vision,
        hearing_quality=hearing,
        infection_load=infection,
        pain_stress=stress,
        tool_support=tool_support,
        help_support=help_support,
        route_fit=route_fit,
        exposure_risk=exposure,
        falls=falls,
        collisions=collisions,
        infection_events=infection_events,
        repair_actions=repair_actions,
        help_actions=help_actions,
        tool_actions=tool_actions,
        route_actions=route_actions,
        pace_actions=pace_actions,
        continuity_resets=continuity_resets,
        disability_misses=disability_misses,
    )
    return result, trace_frames


def evaluate_policy(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episodes: int,
    cfg: DisabilityConfig,
    phase: str,
) -> List[EpisodeResult]:
    return [
        simulate_episode(scenario, policy, condition, episode, cfg, phase)[0]
        for episode in range(episodes)
    ]


def summarize(eval_rows: Sequence[EpisodeResult], selected: Dict[int, Policy]) -> List[SummaryRow]:
    rows: List[SummaryRow] = []
    for scenario in SCENARIOS:
        policy = selected[scenario.index]
        for condition in CONDITIONS:
            subset = [
                row
                for row in eval_rows
                if row.scenario == scenario.index
                and row.policy_name == policy.name
                and row.condition == condition
            ]
            rows.append(
                SummaryRow(
                    scenario=scenario.index,
                    scenario_name=scenario.name,
                    pressure=scenario.pressure,
                    condition=condition,
                    policy_name=policy.name,
                    mean_reward=mean(row.total_reward for row in subset),
                    mean_survival=mean(row.survival for row in subset),
                    mean_task_success=mean(row.task_success for row in subset),
                    mean_progress=mean(row.progress for row in subset),
                    mean_energy=mean(row.energy for row in subset),
                    mean_integrity=mean(row.integrity for row in subset),
                    mean_mobility=mean(row.mobility for row in subset),
                    mean_vision_quality=mean(row.vision_quality for row in subset),
                    mean_hearing_quality=mean(row.hearing_quality for row in subset),
                    mean_infection_load=mean(row.infection_load for row in subset),
                    mean_pain_stress=mean(row.pain_stress for row in subset),
                    mean_tool_support=mean(row.tool_support for row in subset),
                    mean_help_support=mean(row.help_support for row in subset),
                    mean_route_fit=mean(row.route_fit for row in subset),
                    mean_exposure_risk=mean(row.exposure_risk for row in subset),
                    mean_falls=mean(row.falls for row in subset),
                    mean_collisions=mean(row.collisions for row in subset),
                    mean_infection_events=mean(row.infection_events for row in subset),
                    mean_repair_actions=mean(row.repair_actions for row in subset),
                    mean_help_actions=mean(row.help_actions for row in subset),
                    mean_tool_actions=mean(row.tool_actions for row in subset),
                    mean_route_actions=mean(row.route_actions for row in subset),
                    mean_pace_actions=mean(row.pace_actions for row in subset),
                    mean_continuity_resets=mean(row.continuity_resets for row in subset),
                    mean_disability_misses=mean(row.disability_misses for row in subset),
                )
            )
    return rows


def verdict_from_summary(summary_rows: Sequence[SummaryRow]) -> List[VerdictRow]:
    by_scenario_condition: Dict[Tuple[int, str], SummaryRow] = {
        (row.scenario, row.condition): row for row in summary_rows
    }
    verdicts: List[VerdictRow] = []
    for scenario in SCENARIOS:
        full = by_scenario_condition[(scenario.index, "full_control")]
        rewards = {
            condition: by_scenario_condition[(scenario.index, condition)].mean_reward
            for condition in CONDITIONS
        }
        losses = {condition: full.mean_reward - reward for condition, reward in rewards.items()}
        if scenario.index == 0:
            supports = (
                full.policy_name == "ignore_disability_baseline"
                and max(
                    abs(losses[condition])
                    for condition in CONDITIONS
                    if condition not in {"full_control", "omniscient_disability_control"}
                )
                < 8.0
            )
            verdict = "disability_machinery_rejected_in_fixed_body_control"
        elif scenario.index == 1:
            supports = (
                losses["no_capability_state"] > 38.0
                and losses["no_motor_adaptation"] > 70.0
                and losses["no_compensation_tools"] > 50.0
                and losses["no_route_adaptation"] > 50.0
                and losses["ignore_disability_baseline"] > 60.0
            )
            verdict = "limp_route_tool_adaptation_pressure"
        elif scenario.index == 2:
            supports = (
                losses["no_capability_state"] > 32.0
                and losses["no_sensor_compensation"] > 70.0
                and losses["no_compensation_tools"] > 45.0
                and losses["no_route_adaptation"] > 45.0
                and losses["ignore_disability_baseline"] > 60.0
            )
            verdict = "vision_hearing_compensation_pressure"
        elif scenario.index == 3:
            supports = (
                losses["no_capability_state"] > 30.0
                and losses["no_infection_management"] > 80.0
                and losses["no_repair_access"] > 65.0
                and losses["no_motor_adaptation"] > 30.0
                and losses["ignore_disability_baseline"] > 65.0
            )
            verdict = "wound_infection_repair_pressure"
        elif scenario.index == 4:
            supports = (
                losses["no_capability_state"] > 38.0
                and losses["no_motor_adaptation"] > 48.0
                and losses["no_sensor_compensation"] > 48.0
                and losses["no_help_seeking"] > 70.0
                and losses["no_compensation_tools"] > 70.0
                and losses["no_route_adaptation"] > 58.0
            )
            verdict = "social_help_compensation_pressure"
        else:
            supports = (
                losses["no_continuity"] > 54.0
                and losses["no_capability_state"] > 38.0
                and losses["no_motor_adaptation"] > 42.0
                and losses["no_sensor_compensation"] > 42.0
                and losses["no_infection_management"] > 42.0
                and losses["no_repair_access"] > 42.0
                and losses["no_help_seeking"] > 42.0
                and losses["no_compensation_tools"] > 42.0
                and losses["no_route_adaptation"] > 42.0
            )
            verdict = "restore_disability_continuity_pressure"

        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                expected_pressure=scenario.pressure,
                selected_policy=full.policy_name,
                selected_reward=full.mean_reward,
                no_capability_state_reward=rewards["no_capability_state"],
                no_motor_adaptation_reward=rewards["no_motor_adaptation"],
                no_sensor_compensation_reward=rewards["no_sensor_compensation"],
                no_infection_management_reward=rewards["no_infection_management"],
                no_repair_access_reward=rewards["no_repair_access"],
                no_help_seeking_reward=rewards["no_help_seeking"],
                no_compensation_tools_reward=rewards["no_compensation_tools"],
                no_route_adaptation_reward=rewards["no_route_adaptation"],
                no_continuity_reward=rewards["no_continuity"],
                ignore_disability_baseline_reward=rewards["ignore_disability_baseline"],
                omniscient_disability_control_reward=rewards["omniscient_disability_control"],
                no_capability_state_loss=losses["no_capability_state"],
                no_motor_adaptation_loss=losses["no_motor_adaptation"],
                no_sensor_compensation_loss=losses["no_sensor_compensation"],
                no_infection_management_loss=losses["no_infection_management"],
                no_repair_access_loss=losses["no_repair_access"],
                no_help_seeking_loss=losses["no_help_seeking"],
                no_compensation_tools_loss=losses["no_compensation_tools"],
                no_route_adaptation_loss=losses["no_route_adaptation"],
                no_continuity_loss=losses["no_continuity"],
                ignore_disability_baseline_loss=losses["ignore_disability_baseline"],
                selected_falls=full.mean_falls,
                selected_collisions=full.mean_collisions,
                selected_infection_events=full.mean_infection_events,
                selected_repair_actions=full.mean_repair_actions,
                selected_help_actions=full.mean_help_actions,
                selected_tool_actions=full.mean_tool_actions,
                selected_route_actions=full.mean_route_actions,
                supports_injury_disability_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def select_policies(cfg: DisabilityConfig, policies: Sequence[Policy]) -> Tuple[Dict[int, Policy], List[PolicySelectionRow]]:
    selected: Dict[int, Policy] = {}
    rows: List[PolicySelectionRow] = []
    ignore = next(policy for policy in policies if policy.name == "ignore_disability_baseline")
    for scenario in SCENARIOS:
        scores: List[Tuple[float, Policy]] = []
        for policy in policies:
            train_rows = evaluate_policy(scenario, policy, "full_control", cfg.train_episodes, cfg, "train")
            scores.append((mean(row.total_reward for row in train_rows), policy))
        scores.sort(key=lambda item: item[0], reverse=True)
        best_reward, best_policy = scores[0]
        ignore_rows = evaluate_policy(scenario, ignore, "full_control", cfg.train_episodes, cfg, "train_ignore")
        ignore_reward = mean(row.total_reward for row in ignore_rows)
        selected[scenario.index] = best_policy
        rows.append(
            PolicySelectionRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                selected_policy=best_policy.name,
                selected_uses_capability_state=best_policy.capability_state,
                selected_uses_motor_adaptation=best_policy.motor_adaptation,
                selected_uses_sensor_compensation=best_policy.sensor_compensation,
                selected_uses_infection_management=best_policy.infection_management,
                selected_uses_repair_access=best_policy.repair_access,
                selected_uses_help_seeking=best_policy.help_seeking,
                selected_uses_compensation_tools=best_policy.compensation_tools,
                selected_uses_route_adaptation=best_policy.route_adaptation,
                selected_uses_continuity=best_policy.continuity_memory,
                train_reward=best_reward,
                ignore_train_reward=ignore_reward,
                train_gain_over_ignore=best_reward - ignore_reward,
            )
        )
    return selected, rows


def run_eval(cfg: DisabilityConfig, selected: Dict[int, Policy]) -> List[EpisodeResult]:
    eval_rows: List[EpisodeResult] = []
    for scenario in SCENARIOS:
        policy = selected[scenario.index]
        for condition in CONDITIONS:
            eval_rows.extend(evaluate_policy(scenario, policy, condition, cfg.eval_episodes, cfg, "eval"))
    return eval_rows


def build_trace(
    cfg: DisabilityConfig,
    selected: Dict[int, Policy],
    summary_rows: Sequence[SummaryRow],
) -> Dict[str, object]:
    scenario = SCENARIOS[cfg.trace_scenario]
    policy = selected[scenario.index]
    _, frames = simulate_episode(
        scenario,
        policy,
        "full_control",
        cfg.trace_episode,
        cfg,
        "trace",
        collect_trace=True,
    )
    outcomes = {
        row.condition: asdict(row)
        for row in summary_rows
        if row.scenario == scenario.index and row.policy_name == policy.name
    }
    return {
        "scenario": asdict(scenario),
        "policy": asdict(policy),
        "condition_outcomes": outcomes,
        "frames": frames,
    }


def write_csv(path: Path, rows: Sequence[object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    fieldnames = list(asdict(rows[0]).keys())
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))
    print(f"wrote {path}")


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
        handle.write("\n")
    print(f"wrote {path}")


def write_js(path: Path, variable: str, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        handle.write(f"window.{variable} = ")
        json.dump(payload, handle, indent=2)
        handle.write(";\n")
    print(f"wrote {path}")


def print_verdicts(verdict_rows: Sequence[VerdictRow]) -> None:
    headers = [
        "scenario",
        "policy",
        "capability_loss",
        "motor_loss",
        "sensor_loss",
        "infection_loss",
        "repair_loss",
        "help_loss",
        "tool_loss",
        "route_loss",
        "continuity_loss",
        "supports",
    ]
    rows = [
        [
            row.scenario_name,
            row.selected_policy,
            f"{row.no_capability_state_loss:.3f}",
            f"{row.no_motor_adaptation_loss:.3f}",
            f"{row.no_sensor_compensation_loss:.3f}",
            f"{row.no_infection_management_loss:.3f}",
            f"{row.no_repair_access_loss:.3f}",
            f"{row.no_help_seeking_loss:.3f}",
            f"{row.no_compensation_tools_loss:.3f}",
            f"{row.no_route_adaptation_loss:.3f}",
            f"{row.no_continuity_loss:.3f}",
            str(row.supports_injury_disability_precursor),
        ]
        for row in verdict_rows
    ]
    widths = [len(header) for header in headers]
    for row in rows:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(value))
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> DisabilityConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-episodes", type=int, default=DisabilityConfig.train_episodes)
    parser.add_argument("--eval-episodes", type=int, default=DisabilityConfig.eval_episodes)
    parser.add_argument("--ticks", type=int, default=DisabilityConfig.ticks)
    parser.add_argument("--seed", type=int, default=DisabilityConfig.seed)
    parser.add_argument("--candidate-count", type=int, default=DisabilityConfig.candidate_count)
    parser.add_argument("--trace-scenario", type=int, default=DisabilityConfig.trace_scenario)
    parser.add_argument("--trace-episode", type=int, default=DisabilityConfig.trace_episode)
    args = parser.parse_args()
    return DisabilityConfig(
        train_episodes=args.train_episodes,
        eval_episodes=args.eval_episodes,
        ticks=args.ticks,
        seed=args.seed,
        candidate_count=args.candidate_count,
        trace_scenario=args.trace_scenario,
        trace_episode=args.trace_episode,
    )


def main() -> int:
    cfg = parse_args()
    policies = build_policies(cfg)
    selected, selection_rows = select_policies(cfg, policies)
    eval_rows = run_eval(cfg, selected)
    summary_rows = summarize(eval_rows, selected)
    verdict_rows = verdict_from_summary(summary_rows)
    trace = build_trace(cfg, selected, summary_rows)

    prefix = ARTIFACT_DIR / "ssrm_3d_injury_disability_adaptation"
    write_csv(prefix.with_name(prefix.name + "_eval.csv"), eval_rows)
    write_csv(prefix.with_name(prefix.name + "_policy_selection.csv"), selection_rows)
    write_csv(prefix.with_name(prefix.name + "_summary.csv"), summary_rows)
    write_csv(prefix.with_name(prefix.name + "_verdict.csv"), verdict_rows)
    results = {
        "config": asdict(cfg),
        "scenarios": [asdict(scenario) for scenario in SCENARIOS],
        "policies": [asdict(policy) for policy in policies],
        "policy_selection": [asdict(row) for row in selection_rows],
        "summary": [asdict(row) for row in summary_rows],
        "verdict": [asdict(row) for row in verdict_rows],
    }
    write_json(prefix.with_name(prefix.name + "_results.json"), results)
    write_json(prefix.with_name(prefix.name + "_trace.json"), trace)
    write_js(prefix.with_name(prefix.name + "_results.js"), "SSRM_3D_INJURY_DISABILITY_RESULTS", results)
    write_js(prefix.with_name(prefix.name + "_trace.js"), "SSRM_3D_INJURY_DISABILITY_TRACE", trace)
    print_verdicts(verdict_rows)
    return 0 if all(row.supports_injury_disability_precursor for row in verdict_rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
