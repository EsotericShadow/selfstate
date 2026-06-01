#!/usr/bin/env python3
"""SSRM-3D tool/shelter degradation precursor.

This experiment implements the fifth pressure-layer step from report 74:
maintenance and wear. It is intentionally not a construction or inventory
simulator. Tool integrity, shelter quality, inspection, repair, spare parts,
cache memory, and continuity are abstract control variables.

The useful result is narrow: maintenance machinery should be rejected in a
stable control, then become useful only when delayed degradation changes future
control.
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
class MaintenanceConfig:
    train_episodes: int = 72
    eval_episodes: int = 96
    ticks: int = 220
    seed: int = 20260624
    candidate_count: int = 6
    trace_scenario: int = 3
    trace_episode: int = 0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    expected_tool_pressure: bool
    expected_shelter_pressure: bool
    expected_inspection_pressure: bool
    expected_repair_pressure: bool
    expected_parts_pressure: bool
    expected_continuity_pressure: bool
    tool_wear_rate: float
    shelter_wear_rate: float
    random_shock_rate: float
    weather_load: float
    route_dependence: float
    alarm_dependence: float
    cache_dependence: float
    initial_tool_integrity: float
    initial_shelter_quality: float
    initial_parts: float
    required_progress: float
    work_rate: float
    restore_tick: int


@dataclass(frozen=True)
class Policy:
    name: str
    degradation_state: bool
    inspection_action: bool
    repair_action: bool
    tool_memory: bool
    shelter_memory: bool
    material_cache: bool
    continuity_memory: bool
    tool_repair_threshold: float
    shelter_repair_threshold: float
    inspect_interval: int
    risk_tolerance: float
    tool_cost_tolerance: float


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
    tool_integrity: float
    shelter_quality: float
    spare_parts: float
    exposure_debt: float
    resource_loss: float
    route_confusion: float
    alarm_failures: int
    cache_failures: int
    collapse_risk: float
    inspect_actions: int
    tool_repair_actions: int
    shelter_repair_actions: int
    salvage_actions: int
    work_actions: int
    degradation_reads: int
    tool_memory_reads: int
    shelter_memory_reads: int
    continuity_resets: int
    maintenance_misses: int


@dataclass(frozen=True)
class PolicySelectionRow:
    scenario: int
    scenario_name: str
    selected_policy: str
    selected_uses_degradation_state: bool
    selected_uses_inspection_action: bool
    selected_uses_repair_action: bool
    selected_uses_tool_memory: bool
    selected_uses_shelter_memory: bool
    selected_uses_material_cache: bool
    selected_uses_continuity: bool
    train_reward: float
    no_maintenance_train_reward: float
    train_gain_over_no_maintenance: float


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
    mean_tool_integrity: float
    mean_shelter_quality: float
    mean_spare_parts: float
    mean_exposure_debt: float
    mean_resource_loss: float
    mean_route_confusion: float
    mean_alarm_failures: float
    mean_cache_failures: float
    mean_collapse_risk: float
    mean_inspect_actions: float
    mean_tool_repair_actions: float
    mean_shelter_repair_actions: float
    mean_salvage_actions: float
    mean_work_actions: float
    mean_degradation_reads: float
    mean_tool_memory_reads: float
    mean_shelter_memory_reads: float
    mean_continuity_resets: float
    mean_maintenance_misses: float


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    expected_pressure: str
    selected_policy: str
    selected_reward: float
    no_degradation_state_reward: float
    no_inspection_action_reward: float
    no_repair_action_reward: float
    no_tool_memory_reward: float
    no_shelter_memory_reward: float
    no_material_cache_reward: float
    no_continuity_reward: float
    reactive_failure_only_reward: float
    omniscient_maintenance_control_reward: float
    maintenance_gain_over_no_maintenance: float
    no_degradation_state_loss: float
    no_inspection_action_loss: float
    no_repair_action_loss: float
    no_tool_memory_loss: float
    no_shelter_memory_loss: float
    no_material_cache_loss: float
    no_continuity_loss: float
    reactive_failure_only_loss: float
    selected_inspect_actions: float
    selected_tool_repair_actions: float
    selected_shelter_repair_actions: float
    selected_maintenance_misses: float
    supports_tool_shelter_degradation_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        index=0,
        name="stable_new_tools_control",
        pressure="new tools and intact shelter where maintenance should not matter",
        expected_tool_pressure=False,
        expected_shelter_pressure=False,
        expected_inspection_pressure=False,
        expected_repair_pressure=False,
        expected_parts_pressure=False,
        expected_continuity_pressure=False,
        tool_wear_rate=0.00005,
        shelter_wear_rate=0.00004,
        random_shock_rate=0.0,
        weather_load=0.0,
        route_dependence=0.0,
        alarm_dependence=0.0,
        cache_dependence=0.0,
        initial_tool_integrity=0.96,
        initial_shelter_quality=0.96,
        initial_parts=0.0,
        required_progress=126.0,
        work_rate=0.70,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=1,
        name="route_marker_decay",
        pressure="route markers decay and create navigation confusion unless inspected and repaired",
        expected_tool_pressure=True,
        expected_shelter_pressure=False,
        expected_inspection_pressure=True,
        expected_repair_pressure=True,
        expected_parts_pressure=True,
        expected_continuity_pressure=False,
        tool_wear_rate=0.0044,
        shelter_wear_rate=0.00018,
        random_shock_rate=0.003,
        weather_load=0.10,
        route_dependence=0.94,
        alarm_dependence=0.0,
        cache_dependence=0.10,
        initial_tool_integrity=0.76,
        initial_shelter_quality=0.84,
        initial_parts=2.0,
        required_progress=84.0,
        work_rate=0.64,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=2,
        name="storm_shelter_wear",
        pressure="storm load degrades shelter quality unless shelter state and repair are maintained",
        expected_tool_pressure=False,
        expected_shelter_pressure=True,
        expected_inspection_pressure=False,
        expected_repair_pressure=True,
        expected_parts_pressure=True,
        expected_continuity_pressure=False,
        tool_wear_rate=0.00025,
        shelter_wear_rate=0.0049,
        random_shock_rate=0.002,
        weather_load=0.82,
        route_dependence=0.0,
        alarm_dependence=0.12,
        cache_dependence=0.0,
        initial_tool_integrity=0.90,
        initial_shelter_quality=0.72,
        initial_parts=2.2,
        required_progress=82.0,
        work_rate=0.62,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=3,
        name="alarm_cache_wear",
        pressure="alarms and resource caches degrade unpredictably, making inspection and repair valuable",
        expected_tool_pressure=True,
        expected_shelter_pressure=False,
        expected_inspection_pressure=True,
        expected_repair_pressure=True,
        expected_parts_pressure=True,
        expected_continuity_pressure=False,
        tool_wear_rate=0.0026,
        shelter_wear_rate=0.00016,
        random_shock_rate=0.024,
        weather_load=0.24,
        route_dependence=0.10,
        alarm_dependence=0.76,
        cache_dependence=0.82,
        initial_tool_integrity=0.80,
        initial_shelter_quality=0.86,
        initial_parts=2.4,
        required_progress=86.0,
        work_rate=0.64,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=4,
        name="restore_maintenance_continuity",
        pressure="after restore, remembered repairs and known wear state prevent repeated tool and shelter failure",
        expected_tool_pressure=True,
        expected_shelter_pressure=True,
        expected_inspection_pressure=True,
        expected_repair_pressure=True,
        expected_parts_pressure=True,
        expected_continuity_pressure=True,
        tool_wear_rate=0.0032,
        shelter_wear_rate=0.0033,
        random_shock_rate=0.010,
        weather_load=0.58,
        route_dependence=0.50,
        alarm_dependence=0.44,
        cache_dependence=0.38,
        initial_tool_integrity=0.74,
        initial_shelter_quality=0.70,
        initial_parts=2.6,
        required_progress=78.0,
        work_rate=0.60,
        restore_tick=104,
    ),
)


SEEDED_POLICIES = (
    Policy(
        name="no_maintenance_baseline",
        degradation_state=False,
        inspection_action=False,
        repair_action=False,
        tool_memory=False,
        shelter_memory=False,
        material_cache=False,
        continuity_memory=False,
        tool_repair_threshold=0.16,
        shelter_repair_threshold=0.16,
        inspect_interval=999,
        risk_tolerance=0.78,
        tool_cost_tolerance=0.0,
    ),
    Policy(
        name="reactive_failure_worker",
        degradation_state=False,
        inspection_action=False,
        repair_action=True,
        tool_memory=True,
        shelter_memory=True,
        material_cache=True,
        continuity_memory=False,
        tool_repair_threshold=0.22,
        shelter_repair_threshold=0.22,
        inspect_interval=999,
        risk_tolerance=0.62,
        tool_cost_tolerance=0.42,
    ),
    Policy(
        name="marker_maintenance_planner",
        degradation_state=True,
        inspection_action=True,
        repair_action=True,
        tool_memory=True,
        shelter_memory=False,
        material_cache=True,
        continuity_memory=False,
        tool_repair_threshold=0.58,
        shelter_repair_threshold=0.32,
        inspect_interval=18,
        risk_tolerance=0.34,
        tool_cost_tolerance=0.72,
    ),
    Policy(
        name="shelter_repair_planner",
        degradation_state=True,
        inspection_action=True,
        repair_action=True,
        tool_memory=False,
        shelter_memory=True,
        material_cache=True,
        continuity_memory=False,
        tool_repair_threshold=0.36,
        shelter_repair_threshold=0.60,
        inspect_interval=22,
        risk_tolerance=0.28,
        tool_cost_tolerance=0.74,
    ),
    Policy(
        name="alarm_cache_planner",
        degradation_state=True,
        inspection_action=True,
        repair_action=True,
        tool_memory=True,
        shelter_memory=False,
        material_cache=True,
        continuity_memory=False,
        tool_repair_threshold=0.62,
        shelter_repair_threshold=0.32,
        inspect_interval=10,
        risk_tolerance=0.26,
        tool_cost_tolerance=0.82,
    ),
    Policy(
        name="continuity_maintenance_planner",
        degradation_state=True,
        inspection_action=True,
        repair_action=True,
        tool_memory=True,
        shelter_memory=True,
        material_cache=True,
        continuity_memory=True,
        tool_repair_threshold=0.58,
        shelter_repair_threshold=0.58,
        inspect_interval=14,
        risk_tolerance=0.22,
        tool_cost_tolerance=0.86,
    ),
)


CONDITIONS = (
    "full_control",
    "no_degradation_state",
    "no_inspection_action",
    "no_repair_action",
    "no_tool_memory",
    "no_shelter_memory",
    "no_material_cache",
    "no_continuity",
    "reactive_failure_only",
    "omniscient_maintenance_control",
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


def build_policies(cfg: MaintenanceConfig) -> List[Policy]:
    policies = list(SEEDED_POLICIES)
    rng = random.Random(cfg.seed + 991)
    while len(policies) < cfg.candidate_count:
        base = rng.choice(SEEDED_POLICIES[1:])
        policies.append(
            Policy(
                name=f"mutant_maintenance_{len(policies)}",
                degradation_state=base.degradation_state if rng.random() > 0.14 else not base.degradation_state,
                inspection_action=base.inspection_action if rng.random() > 0.16 else not base.inspection_action,
                repair_action=base.repair_action if rng.random() > 0.14 else not base.repair_action,
                tool_memory=base.tool_memory if rng.random() > 0.18 else not base.tool_memory,
                shelter_memory=base.shelter_memory if rng.random() > 0.18 else not base.shelter_memory,
                material_cache=base.material_cache if rng.random() > 0.14 else not base.material_cache,
                continuity_memory=base.continuity_memory if rng.random() > 0.14 else not base.continuity_memory,
                tool_repair_threshold=clamp(base.tool_repair_threshold + rng.uniform(-0.07, 0.07), 0.24, 0.74),
                shelter_repair_threshold=clamp(base.shelter_repair_threshold + rng.uniform(-0.07, 0.07), 0.24, 0.74),
                inspect_interval=max(6, base.inspect_interval + rng.randint(-5, 5)) if base.inspect_interval < 900 else 999,
                risk_tolerance=clamp(base.risk_tolerance + rng.uniform(-0.08, 0.08), 0.14, 0.82),
                tool_cost_tolerance=clamp(base.tool_cost_tolerance + rng.uniform(-0.10, 0.10), 0.0, 1.0),
            )
        )
    return policies


def condition_policy(policy: Policy, condition: str) -> Policy:
    if condition == "omniscient_maintenance_control":
        return Policy(
            name=policy.name,
            degradation_state=True,
            inspection_action=True,
            repair_action=True,
            tool_memory=True,
            shelter_memory=True,
            material_cache=True,
            continuity_memory=True,
            tool_repair_threshold=min(policy.tool_repair_threshold, 0.56),
            shelter_repair_threshold=min(policy.shelter_repair_threshold, 0.56),
            inspect_interval=min(policy.inspect_interval, 10),
            risk_tolerance=0.10,
            tool_cost_tolerance=1.0,
        )
    if condition == "reactive_failure_only":
        return Policy(
            name=policy.name,
            degradation_state=False,
            inspection_action=False,
            repair_action=policy.repair_action,
            tool_memory=policy.tool_memory,
            shelter_memory=policy.shelter_memory,
            material_cache=policy.material_cache,
            continuity_memory=policy.continuity_memory,
            tool_repair_threshold=0.20,
            shelter_repair_threshold=0.20,
            inspect_interval=999,
            risk_tolerance=policy.risk_tolerance,
            tool_cost_tolerance=policy.tool_cost_tolerance,
        )
    return Policy(
        name=policy.name,
        degradation_state=policy.degradation_state and condition != "no_degradation_state",
        inspection_action=policy.inspection_action and condition != "no_inspection_action",
        repair_action=policy.repair_action and condition != "no_repair_action",
        tool_memory=policy.tool_memory and condition != "no_tool_memory",
        shelter_memory=policy.shelter_memory and condition != "no_shelter_memory",
        material_cache=policy.material_cache and condition != "no_material_cache",
        continuity_memory=policy.continuity_memory and condition != "no_continuity",
        tool_repair_threshold=policy.tool_repair_threshold,
        shelter_repair_threshold=policy.shelter_repair_threshold,
        inspect_interval=policy.inspect_interval,
        risk_tolerance=policy.risk_tolerance,
        tool_cost_tolerance=policy.tool_cost_tolerance,
    )


def scenario_seed(
    cfg: MaintenanceConfig,
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
        (policy.degradation_state, 0.62),
        (policy.inspection_action, 0.48),
        (policy.repair_action, 0.48),
        (policy.tool_memory, 0.52),
        (policy.shelter_memory, 0.52),
        (policy.material_cache, 0.52),
        (policy.continuity_memory, 0.78),
    ]
    return sum(weight for enabled, weight in weighted_flags if enabled)


def estimate_quality(
    actual: float,
    predicted: float,
    last_inspected: float,
    since_inspection: int,
    policy: Policy,
    rng: random.Random,
) -> float:
    if policy.inspection_action and since_inspection <= max(3, policy.inspect_interval // 2):
        return clamp(last_inspected + rng.uniform(-0.015, 0.015), 0.0, 1.0)
    if policy.degradation_state:
        return clamp(predicted + rng.uniform(-0.035, 0.035), 0.0, 1.0)
    if actual < 0.24:
        return clamp(0.22 + rng.uniform(-0.030, 0.030), 0.0, 1.0)
    return clamp(0.72 + rng.uniform(-0.040, 0.040), 0.0, 1.0)


def choose_action(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    tick: int,
    observed_tool: float,
    observed_shelter: float,
    spare_parts: float,
    exposure: float,
    rng: random.Random,
) -> str:
    if (
        policy.inspection_action
        and policy.degradation_state
        and policy.inspect_interval < 900
        and tick % policy.inspect_interval == 0
    ):
        if scenario.expected_inspection_pressure or exposure > 0.28 or observed_tool < 0.68 or observed_shelter < 0.68:
            return "inspect"

    can_repair = policy.repair_action and policy.material_cache and spare_parts >= 0.55 and policy.tool_cost_tolerance > 0.20
    if (
        can_repair
        and policy.tool_memory
        and scenario.expected_tool_pressure
        and observed_tool < policy.tool_repair_threshold
    ):
        return "repair_tool"
    if (
        can_repair
        and policy.shelter_memory
        and scenario.expected_shelter_pressure
        and observed_shelter < policy.shelter_repair_threshold
    ):
        return "repair_shelter"
    if (
        policy.material_cache
        and policy.repair_action
        and spare_parts < 0.55
        and (scenario.expected_parts_pressure or exposure > 0.34)
        and policy.tool_cost_tolerance > 0.55
        and rng.random() < 0.08
    ):
        return "salvage_parts"
    return "work"


def apply_wear(
    scenario: ScenarioSpec,
    tool_integrity: float,
    shelter_quality: float,
    rng: random.Random,
) -> Tuple[float, float, bool]:
    tool_drop = scenario.tool_wear_rate + scenario.weather_load * 0.00030
    shelter_drop = scenario.shelter_wear_rate + scenario.weather_load * 0.00055
    shock = rng.random() < scenario.random_shock_rate
    if shock:
        tool_drop += rng.uniform(0.050, 0.115) * max(0.2, scenario.alarm_dependence + scenario.cache_dependence)
        shelter_drop += rng.uniform(0.025, 0.070) * max(0.2, scenario.weather_load)
    return clamp(tool_integrity - tool_drop, 0.0, 1.0), clamp(shelter_quality - shelter_drop, 0.0, 1.0), shock


def simulate_episode(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episode: int,
    cfg: MaintenanceConfig,
    phase: str,
    collect_trace: bool = False,
) -> Tuple[EpisodeResult, List[Dict[str, object]]]:
    effective = condition_policy(policy, condition)
    rng = random.Random(scenario_seed(cfg, scenario, policy, condition, episode, phase))
    tool_integrity = clamp(scenario.initial_tool_integrity + rng.uniform(-0.020, 0.020), 0.0, 1.0)
    shelter_quality = clamp(scenario.initial_shelter_quality + rng.uniform(-0.020, 0.020), 0.0, 1.0)
    spare_parts = scenario.initial_parts if effective.material_cache else 0.0
    predicted_tool = tool_integrity
    predicted_shelter = shelter_quality
    last_tool_inspection = tool_integrity
    last_shelter_inspection = shelter_quality
    since_tool_inspection = 999
    since_shelter_inspection = 999

    progress = 0.0
    exposure = 0.0
    resource_loss = 0.0
    route_confusion = 0.0
    collapse_risk = 0.0
    collapsed = False

    alarm_failures = 0
    cache_failures = 0
    inspect_actions = 0
    tool_repair_actions = 0
    shelter_repair_actions = 0
    salvage_actions = 0
    work_actions = 0
    degradation_reads = 0
    tool_memory_reads = 0
    shelter_memory_reads = 0
    continuity_resets = 0
    maintenance_misses = 0
    trace_frames: List[Dict[str, object]] = []

    for tick in range(cfg.ticks):
        if scenario.restore_tick == tick and not effective.continuity_memory:
            predicted_tool = 0.78
            predicted_shelter = 0.78
            last_tool_inspection = 0.78
            last_shelter_inspection = 0.78
            since_tool_inspection = 999
            since_shelter_inspection = 999
            spare_parts = max(0.0, spare_parts - 0.80)
            continuity_resets += 1

        tool_integrity, shelter_quality, shock = apply_wear(scenario, tool_integrity, shelter_quality, rng)
        predicted_tool = clamp(predicted_tool - scenario.tool_wear_rate - scenario.weather_load * 0.00024, 0.0, 1.0)
        predicted_shelter = clamp(predicted_shelter - scenario.shelter_wear_rate - scenario.weather_load * 0.00048, 0.0, 1.0)
        since_tool_inspection += 1
        since_shelter_inspection += 1

        if collapsed:
            action = "collapsed"
        else:
            if effective.degradation_state:
                degradation_reads += 1
            if effective.tool_memory:
                tool_memory_reads += 1
            if effective.shelter_memory:
                shelter_memory_reads += 1
            observed_tool = estimate_quality(
                tool_integrity,
                predicted_tool,
                last_tool_inspection,
                since_tool_inspection,
                effective,
                rng,
            )
            observed_shelter = estimate_quality(
                shelter_quality,
                predicted_shelter,
                last_shelter_inspection,
                since_shelter_inspection,
                effective,
                rng,
            )
            action = choose_action(
                scenario,
                effective,
                condition,
                tick,
                observed_tool,
                observed_shelter,
                spare_parts,
                exposure,
                rng,
            )

            if action == "inspect":
                inspect_actions += 1
                last_tool_inspection = tool_integrity
                last_shelter_inspection = shelter_quality
                since_tool_inspection = 0
                since_shelter_inspection = 0
                progress -= 0.12
            elif action == "repair_tool":
                tool_repair_actions += 1
                tool_integrity = clamp(tool_integrity + 0.38, 0.0, 1.0)
                predicted_tool = tool_integrity
                last_tool_inspection = tool_integrity
                since_tool_inspection = 0
                spare_parts = max(0.0, spare_parts - 0.70)
                progress -= 0.34
            elif action == "repair_shelter":
                shelter_repair_actions += 1
                shelter_quality = clamp(shelter_quality + 0.36, 0.0, 1.0)
                predicted_shelter = shelter_quality
                last_shelter_inspection = shelter_quality
                since_shelter_inspection = 0
                spare_parts = max(0.0, spare_parts - 0.78)
                exposure = clamp(exposure - 0.018, 0.0, 1.0)
                progress -= 0.38
            elif action == "salvage_parts":
                salvage_actions += 1
                spare_parts = clamp(spare_parts + 0.45, 0.0, 3.0)
                exposure = clamp(exposure + scenario.weather_load * 0.004, 0.0, 1.0)
                progress -= 0.22
            else:
                work_actions += 1
                route_penalty = scenario.route_dependence * max(0.0, 0.56 - tool_integrity) * 1.05
                shelter_penalty = scenario.weather_load * max(0.0, 0.58 - shelter_quality) * 0.95
                alarm_penalty = scenario.alarm_dependence * max(0.0, 0.46 - tool_integrity) * 0.64
                cache_penalty = scenario.cache_dependence * max(0.0, 0.50 - tool_integrity) * 0.54
                capability = clamp(1.0 - route_penalty - shelter_penalty - alarm_penalty - cache_penalty - exposure * 0.40, 0.04, 1.0)
                progress += scenario.work_rate * capability
                route_confusion += route_penalty * 0.022
                resource_loss += cache_penalty * 0.020
                exposure = clamp(exposure + shelter_penalty * 0.012 + scenario.weather_load * max(0.0, 0.50 - shelter_quality) * 0.006, 0.0, 1.0)

            if shock and effective.inspection_action and scenario.expected_inspection_pressure:
                maintenance_misses += 0 if action == "inspect" else 1
            if tool_integrity < 0.34 and scenario.expected_tool_pressure and not effective.tool_memory:
                maintenance_misses += 1 if tick % 9 == 0 else 0
            if shelter_quality < 0.36 and scenario.expected_shelter_pressure and not effective.shelter_memory:
                maintenance_misses += 1 if tick % 9 == 0 else 0
            if tool_integrity < 0.28 and scenario.alarm_dependence > 0.20:
                alarm_failures += 1 if tick % 11 == 0 else 0
            if tool_integrity < 0.30 and scenario.cache_dependence > 0.20:
                cache_failures += 1 if tick % 13 == 0 else 0
            if (tool_integrity < 0.30 or shelter_quality < 0.30) and not effective.degradation_state:
                maintenance_misses += 1 if tick % 10 == 0 else 0

            collapse_risk = max(
                collapse_risk,
                route_confusion * 0.55
                + resource_loss * 0.62
                + exposure * 0.88
                + alarm_failures * 0.020
                + cache_failures * 0.018,
            )
            if collapse_risk >= 1.0:
                collapsed = True

        if collect_trace and (tick % 5 == 0 or tick == cfg.ticks - 1):
            trace_frames.append(
                {
                    "tick": tick,
                    "action": action,
                    "tool_integrity": round(tool_integrity, 3),
                    "shelter_quality": round(shelter_quality, 3),
                    "spare_parts": round(spare_parts, 3),
                    "exposure_debt": round(exposure, 3),
                    "resource_loss": round(resource_loss, 3),
                    "route_confusion": round(route_confusion, 3),
                    "collapse_risk": round(collapse_risk, 3),
                    "progress": round(progress, 3),
                    "alarm_failures": alarm_failures,
                    "cache_failures": cache_failures,
                    "continuity_resets": continuity_resets,
                    "maintenance_misses": maintenance_misses,
                }
            )

    task_success = progress >= scenario.required_progress and not collapsed
    survival = 1.0 if not collapsed and collapse_risk < 0.88 else 0.0

    reward = progress
    reward += 34.0 if task_success else -20.0
    reward += 36.0 if survival else -96.0
    reward += tool_integrity * (16.0 if scenario.expected_tool_pressure else 3.0)
    reward += shelter_quality * (16.0 if scenario.expected_shelter_pressure else 3.0)
    reward += spare_parts * (3.0 if scenario.expected_parts_pressure else 0.4)
    reward -= route_confusion * 52.0
    reward -= resource_loss * 58.0
    reward -= exposure * 62.0
    reward -= collapse_risk * 78.0
    reward -= alarm_failures * 2.8
    reward -= cache_failures * 2.5
    reward -= maintenance_misses * 0.70
    reward -= inspect_actions * 0.10
    reward -= tool_repair_actions * 0.25
    reward -= shelter_repair_actions * 0.28
    reward -= salvage_actions * 0.18
    reward -= feature_overhead(effective)
    if scenario.expected_continuity_pressure and continuity_resets:
        reward -= 44.0

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
        tool_integrity=tool_integrity,
        shelter_quality=shelter_quality,
        spare_parts=spare_parts,
        exposure_debt=exposure,
        resource_loss=resource_loss,
        route_confusion=route_confusion,
        alarm_failures=alarm_failures,
        cache_failures=cache_failures,
        collapse_risk=collapse_risk,
        inspect_actions=inspect_actions,
        tool_repair_actions=tool_repair_actions,
        shelter_repair_actions=shelter_repair_actions,
        salvage_actions=salvage_actions,
        work_actions=work_actions,
        degradation_reads=degradation_reads,
        tool_memory_reads=tool_memory_reads,
        shelter_memory_reads=shelter_memory_reads,
        continuity_resets=continuity_resets,
        maintenance_misses=maintenance_misses,
    )
    return result, trace_frames


def evaluate_policy(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episodes: int,
    cfg: MaintenanceConfig,
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
                    mean_tool_integrity=mean(row.tool_integrity for row in subset),
                    mean_shelter_quality=mean(row.shelter_quality for row in subset),
                    mean_spare_parts=mean(row.spare_parts for row in subset),
                    mean_exposure_debt=mean(row.exposure_debt for row in subset),
                    mean_resource_loss=mean(row.resource_loss for row in subset),
                    mean_route_confusion=mean(row.route_confusion for row in subset),
                    mean_alarm_failures=mean(row.alarm_failures for row in subset),
                    mean_cache_failures=mean(row.cache_failures for row in subset),
                    mean_collapse_risk=mean(row.collapse_risk for row in subset),
                    mean_inspect_actions=mean(row.inspect_actions for row in subset),
                    mean_tool_repair_actions=mean(row.tool_repair_actions for row in subset),
                    mean_shelter_repair_actions=mean(row.shelter_repair_actions for row in subset),
                    mean_salvage_actions=mean(row.salvage_actions for row in subset),
                    mean_work_actions=mean(row.work_actions for row in subset),
                    mean_degradation_reads=mean(row.degradation_reads for row in subset),
                    mean_tool_memory_reads=mean(row.tool_memory_reads for row in subset),
                    mean_shelter_memory_reads=mean(row.shelter_memory_reads for row in subset),
                    mean_continuity_resets=mean(row.continuity_resets for row in subset),
                    mean_maintenance_misses=mean(row.maintenance_misses for row in subset),
                )
            )
    return rows


def select_policies(cfg: MaintenanceConfig, policies: Sequence[Policy]) -> Tuple[Dict[int, Policy], List[PolicySelectionRow]]:
    selected: Dict[int, Policy] = {}
    rows: List[PolicySelectionRow] = []
    baseline = next(policy for policy in policies if policy.name == "no_maintenance_baseline")
    for scenario in SCENARIOS:
        scored: List[Tuple[float, Policy]] = []
        for policy in policies:
            episodes = evaluate_policy(scenario, policy, "full_control", cfg.train_episodes, cfg, "train")
            scored.append((mean(row.total_reward for row in episodes), policy))
        scored.sort(key=lambda item: item[0], reverse=True)
        selected_policy = scored[0][1]
        selected_reward = scored[0][0]
        baseline_reward = mean(
            row.total_reward
            for row in evaluate_policy(scenario, baseline, "full_control", cfg.train_episodes, cfg, "train_baseline")
        )
        selected[scenario.index] = selected_policy
        rows.append(
            PolicySelectionRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                selected_policy=selected_policy.name,
                selected_uses_degradation_state=selected_policy.degradation_state,
                selected_uses_inspection_action=selected_policy.inspection_action,
                selected_uses_repair_action=selected_policy.repair_action,
                selected_uses_tool_memory=selected_policy.tool_memory,
                selected_uses_shelter_memory=selected_policy.shelter_memory,
                selected_uses_material_cache=selected_policy.material_cache,
                selected_uses_continuity=selected_policy.continuity_memory,
                train_reward=selected_reward,
                no_maintenance_train_reward=baseline_reward,
                train_gain_over_no_maintenance=selected_reward - baseline_reward,
            )
        )
    return selected, rows


def row_lookup(rows: Sequence[SummaryRow]) -> Dict[Tuple[int, str], SummaryRow]:
    return {(row.scenario, row.condition): row for row in rows}


def build_verdicts(summary_rows: Sequence[SummaryRow], selected: Dict[int, Policy]) -> List[VerdictRow]:
    lookup = row_lookup(summary_rows)
    verdicts: List[VerdictRow] = []
    for scenario in SCENARIOS:
        full = lookup[(scenario.index, "full_control")]
        no_degradation = lookup[(scenario.index, "no_degradation_state")]
        no_inspection = lookup[(scenario.index, "no_inspection_action")]
        no_repair = lookup[(scenario.index, "no_repair_action")]
        no_tool = lookup[(scenario.index, "no_tool_memory")]
        no_shelter = lookup[(scenario.index, "no_shelter_memory")]
        no_parts = lookup[(scenario.index, "no_material_cache")]
        no_continuity = lookup[(scenario.index, "no_continuity")]
        reactive = lookup[(scenario.index, "reactive_failure_only")]
        omniscient = lookup[(scenario.index, "omniscient_maintenance_control")]

        no_degradation_loss = full.mean_reward - no_degradation.mean_reward
        no_inspection_loss = full.mean_reward - no_inspection.mean_reward
        no_repair_loss = full.mean_reward - no_repair.mean_reward
        no_tool_loss = full.mean_reward - no_tool.mean_reward
        no_shelter_loss = full.mean_reward - no_shelter.mean_reward
        no_parts_loss = full.mean_reward - no_parts.mean_reward
        no_continuity_loss = full.mean_reward - no_continuity.mean_reward
        reactive_loss = full.mean_reward - reactive.mean_reward

        if scenario.index == 0:
            supports = (
                selected[scenario.index].name == "no_maintenance_baseline"
                and abs(no_degradation_loss) < 4.0
                and abs(no_repair_loss) < 4.0
                and full.mean_tool_repair_actions < 0.5
                and full.mean_shelter_repair_actions < 0.5
            )
            verdict = "maintenance_rejected_in_stable_control"
        elif scenario.index == 1:
            supports = (
                no_degradation_loss > 18.0
                and no_repair_loss > 32.0
                and no_tool_loss > 28.0
                and no_parts_loss > 16.0
                and full.mean_tool_repair_actions > 0.8
            )
            verdict = "route_marker_degradation_pressure"
        elif scenario.index == 2:
            supports = (
                no_repair_loss > 28.0
                and no_shelter_loss > 32.0
                and no_parts_loss > 16.0
                and full.mean_shelter_repair_actions > 0.8
                and full.mean_exposure_debt < no_repair.mean_exposure_debt
            )
            verdict = "shelter_wear_repair_pressure"
        elif scenario.index == 3:
            supports = (
                no_inspection_loss > 18.0
                and no_repair_loss > 28.0
                and no_tool_loss > 28.0
                and no_parts_loss > 16.0
                and full.mean_alarm_failures < no_inspection.mean_alarm_failures
            )
            verdict = "alarm_cache_inspection_repair_pressure"
        else:
            supports = (
                no_continuity_loss > 24.0
                and no_repair_loss > 26.0
                and no_tool_loss > 20.0
                and no_shelter_loss > 20.0
                and no_continuity.mean_continuity_resets > 0.5
            )
            verdict = "restore_maintenance_continuity_pressure"

        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                expected_pressure=scenario.pressure,
                selected_policy=selected[scenario.index].name,
                selected_reward=full.mean_reward,
                no_degradation_state_reward=no_degradation.mean_reward,
                no_inspection_action_reward=no_inspection.mean_reward,
                no_repair_action_reward=no_repair.mean_reward,
                no_tool_memory_reward=no_tool.mean_reward,
                no_shelter_memory_reward=no_shelter.mean_reward,
                no_material_cache_reward=no_parts.mean_reward,
                no_continuity_reward=no_continuity.mean_reward,
                reactive_failure_only_reward=reactive.mean_reward,
                omniscient_maintenance_control_reward=omniscient.mean_reward,
                maintenance_gain_over_no_maintenance=full.mean_reward - lookup[(scenario.index, "no_repair_action")].mean_reward,
                no_degradation_state_loss=no_degradation_loss,
                no_inspection_action_loss=no_inspection_loss,
                no_repair_action_loss=no_repair_loss,
                no_tool_memory_loss=no_tool_loss,
                no_shelter_memory_loss=no_shelter_loss,
                no_material_cache_loss=no_parts_loss,
                no_continuity_loss=no_continuity_loss,
                reactive_failure_only_loss=reactive_loss,
                selected_inspect_actions=full.mean_inspect_actions,
                selected_tool_repair_actions=full.mean_tool_repair_actions,
                selected_shelter_repair_actions=full.mean_shelter_repair_actions,
                selected_maintenance_misses=full.mean_maintenance_misses,
                supports_tool_shelter_degradation_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def build_trace(cfg: MaintenanceConfig, selected: Dict[int, Policy]) -> Dict[str, object]:
    scenario = SCENARIOS[cfg.trace_scenario]
    policy = selected[scenario.index]
    result, frames = simulate_episode(
        scenario,
        policy,
        "full_control",
        cfg.trace_episode,
        cfg,
        "trace",
        collect_trace=True,
    )
    condition_outcomes = {}
    for condition in CONDITIONS:
        rows = evaluate_policy(scenario, policy, condition, max(24, min(48, cfg.eval_episodes)), cfg, "trace_eval")
        condition_outcomes[condition] = {
            "mean_reward": mean(row.total_reward for row in rows),
            "mean_tool_integrity": mean(row.tool_integrity for row in rows),
            "mean_shelter_quality": mean(row.shelter_quality for row in rows),
            "mean_exposure_debt": mean(row.exposure_debt for row in rows),
            "mean_resource_loss": mean(row.resource_loss for row in rows),
        }
    return {
        "scenario": asdict(scenario),
        "policy": asdict(policy),
        "episode_result": asdict(result),
        "condition_outcomes": condition_outcomes,
        "frames": frames,
        "trace_note": "Maintenance, inspection, repair, spare parts, and continuity are abstract control variables.",
    }


def write_csv(path: Path, rows: Sequence[object]) -> None:
    rows = list(rows)
    if not rows:
        raise ValueError(f"no rows for {path}")
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def write_js(path: Path, variable_name: str, data: object) -> None:
    with path.open("w", encoding="utf-8") as handle:
        handle.write(f"window.{variable_name} = ")
        json.dump(data, handle, indent=2)
        handle.write(";\n")


def run_experiment(
    cfg: MaintenanceConfig,
) -> Tuple[List[EpisodeResult], List[PolicySelectionRow], List[SummaryRow], List[VerdictRow], Dict[str, object]]:
    policies = build_policies(cfg)
    selected, selection_rows = select_policies(cfg, policies)
    eval_rows: List[EpisodeResult] = []
    for scenario in SCENARIOS:
        policy = selected[scenario.index]
        for condition in CONDITIONS:
            eval_rows.extend(evaluate_policy(scenario, policy, condition, cfg.eval_episodes, cfg, "eval"))
    summary_rows = summarize(eval_rows, selected)
    verdict_rows = build_verdicts(summary_rows, selected)
    trace = build_trace(cfg, selected)
    results = {
        "config": asdict(cfg),
        "policy_selection": [asdict(row) for row in selection_rows],
        "summary": [asdict(row) for row in summary_rows],
        "verdict": [asdict(row) for row in verdict_rows],
        "artifact_note": "Tool and shelter degradation are control variables, not construction simulation.",
    }
    return eval_rows, selection_rows, summary_rows, verdict_rows, {"results": results, "trace": trace}


def print_table(verdicts: Sequence[VerdictRow]) -> None:
    headers = [
        "scenario",
        "policy",
        "degradation_loss",
        "inspection_loss",
        "repair_loss",
        "tool_loss",
        "shelter_loss",
        "parts_loss",
        "continuity_loss",
        "supports",
    ]
    rows = [
        [
            row.scenario_name,
            row.selected_policy,
            f"{row.no_degradation_state_loss:.3f}",
            f"{row.no_inspection_action_loss:.3f}",
            f"{row.no_repair_action_loss:.3f}",
            f"{row.no_tool_memory_loss:.3f}",
            f"{row.no_shelter_memory_loss:.3f}",
            f"{row.no_material_cache_loss:.3f}",
            f"{row.no_continuity_loss:.3f}",
            str(row.supports_tool_shelter_degradation_precursor),
        ]
        for row in verdicts
    ]
    widths = [max(len(header), *(len(row[index]) for row in rows)) for index, header in enumerate(headers)]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> MaintenanceConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-episodes", type=int, default=MaintenanceConfig.train_episodes)
    parser.add_argument("--eval-episodes", type=int, default=MaintenanceConfig.eval_episodes)
    parser.add_argument("--ticks", type=int, default=MaintenanceConfig.ticks)
    parser.add_argument("--seed", type=int, default=MaintenanceConfig.seed)
    parser.add_argument("--candidate-count", type=int, default=MaintenanceConfig.candidate_count)
    parser.add_argument("--trace-scenario", type=int, default=MaintenanceConfig.trace_scenario)
    parser.add_argument("--trace-episode", type=int, default=MaintenanceConfig.trace_episode)
    args = parser.parse_args()
    if args.train_episodes < 24:
        raise SystemExit("--train-episodes must be at least 24")
    if args.eval_episodes < 24:
        raise SystemExit("--eval-episodes must be at least 24")
    if args.candidate_count < len(SEEDED_POLICIES):
        raise SystemExit(f"--candidate-count must be at least {len(SEEDED_POLICIES)}")
    if args.trace_scenario < 0 or args.trace_scenario >= len(SCENARIOS):
        raise SystemExit("--trace-scenario out of range")
    return MaintenanceConfig(
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
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    eval_rows, selection_rows, summary_rows, verdict_rows, payload = run_experiment(cfg)

    eval_path = ARTIFACT_DIR / "ssrm_3d_tool_shelter_degradation_eval.csv"
    selection_path = ARTIFACT_DIR / "ssrm_3d_tool_shelter_degradation_policy_selection.csv"
    summary_path = ARTIFACT_DIR / "ssrm_3d_tool_shelter_degradation_summary.csv"
    verdict_path = ARTIFACT_DIR / "ssrm_3d_tool_shelter_degradation_verdict.csv"
    results_path = ARTIFACT_DIR / "ssrm_3d_tool_shelter_degradation_results.json"
    trace_path = ARTIFACT_DIR / "ssrm_3d_tool_shelter_degradation_trace.json"
    results_js_path = ARTIFACT_DIR / "ssrm_3d_tool_shelter_degradation_results.js"
    trace_js_path = ARTIFACT_DIR / "ssrm_3d_tool_shelter_degradation_trace.js"

    write_csv(eval_path, eval_rows)
    write_csv(selection_path, selection_rows)
    write_csv(summary_path, summary_rows)
    write_csv(verdict_path, verdict_rows)
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(payload["results"], handle, indent=2)
        handle.write("\n")
    with trace_path.open("w", encoding="utf-8") as handle:
        json.dump(payload["trace"], handle, indent=2)
        handle.write("\n")
    write_js(results_js_path, "SSRM_3D_TOOL_SHELTER_DEGRADATION_RESULTS", payload["results"])
    write_js(trace_js_path, "SSRM_3D_TOOL_SHELTER_DEGRADATION_TRACE", payload["trace"])

    for path in (
        eval_path,
        selection_path,
        summary_path,
        verdict_path,
        results_path,
        trace_path,
        results_js_path,
        trace_js_path,
    ):
        print(f"wrote {path}")
    print_table(verdict_rows)
    if not all(row.supports_tool_shelter_degradation_precursor for row in verdict_rows):
        print("tool/shelter degradation precursor not supported by all verdict rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
