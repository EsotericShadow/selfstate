#!/usr/bin/env python3
"""SSRM-3D weather/exposure precursor.

This experiment implements the fourth pressure-layer step from report 74:
weather and exposure. It is intentionally not a climate or organism model.
Cold, heat, rain, wind, drought, shelter, fire/light, water planning, and
continuity are abstract control variables.

The useful result is narrow: weather machinery should be rejected in a mild
control, then become useful only when delayed exposure, hydration loss, shelter
timing, fire/light tools, or restore-time continuity change future control.
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
class WeatherConfig:
    train_episodes: int = 72
    eval_episodes: int = 96
    ticks: int = 220
    seed: int = 20260623
    candidate_count: int = 6
    trace_scenario: int = 3
    trace_episode: int = 0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    expected_weather_pressure: bool
    expected_exposure_pressure: bool
    expected_shelter_pressure: bool
    expected_fire_pressure: bool
    expected_water_pressure: bool
    expected_continuity_pressure: bool
    base_temp_c: float
    cold_intensity: float
    heat_intensity: float
    rain_intensity: float
    wind_intensity: float
    storm_start_fraction: float
    storm_duration_fraction: float
    drought: float
    initial_hydration: float
    hydration_loss: float
    initial_exposure: float
    shelter_travel_ticks: int
    required_progress: float
    work_rate: float
    fire_available: bool
    water_available: bool
    restore_tick: int


@dataclass(frozen=True)
class Policy:
    name: str
    weather_state: bool
    exposure_state: bool
    shelter_memory: bool
    fire_tools: bool
    water_planning: bool
    continuity_memory: bool
    forecast_horizon: int
    exposure_threshold: float
    hydration_threshold: float
    storm_risk_threshold: float
    tool_cost_tolerance: float
    risk_tolerance: float


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
    final_hydration: float
    exposure_debt: float
    thermal_stress: float
    illness_risk: float
    shelter_quality: float
    fire_readiness: float
    collapse_risk: float
    work_actions: int
    shelter_actions: int
    fire_actions: int
    water_actions: int
    rest_actions: int
    exposed_ticks: int
    storm_exposed_ticks: int
    weather_reads: int
    exposure_reads: int
    shelter_reads: int
    water_reads: int
    continuity_resets: int
    attribution_errors: int


@dataclass(frozen=True)
class PolicySelectionRow:
    scenario: int
    scenario_name: str
    selected_policy: str
    selected_uses_weather_state: bool
    selected_uses_exposure_state: bool
    selected_uses_shelter_memory: bool
    selected_uses_fire_tools: bool
    selected_uses_water_planning: bool
    selected_uses_continuity: bool
    train_reward: float
    no_weather_train_reward: float
    train_gain_over_no_weather: float


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
    mean_final_hydration: float
    mean_exposure_debt: float
    mean_thermal_stress: float
    mean_illness_risk: float
    mean_shelter_quality: float
    mean_fire_readiness: float
    mean_collapse_risk: float
    mean_work_actions: float
    mean_shelter_actions: float
    mean_fire_actions: float
    mean_water_actions: float
    mean_rest_actions: float
    mean_exposed_ticks: float
    mean_storm_exposed_ticks: float
    mean_weather_reads: float
    mean_exposure_reads: float
    mean_shelter_reads: float
    mean_water_reads: float
    mean_continuity_resets: float
    mean_attribution_errors: float


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    expected_pressure: str
    selected_policy: str
    selected_reward: float
    no_weather_state_reward: float
    no_exposure_state_reward: float
    no_shelter_memory_reward: float
    no_fire_tools_reward: float
    no_water_planning_reward: float
    no_continuity_reward: float
    reactive_weather_only_reward: float
    omniscient_weather_control_reward: float
    weather_gain_over_no_weather: float
    no_weather_state_loss: float
    no_exposure_state_loss: float
    no_shelter_memory_loss: float
    no_fire_tools_loss: float
    no_water_planning_loss: float
    no_continuity_loss: float
    reactive_weather_only_loss: float
    selected_exposed_ticks: float
    selected_storm_exposed_ticks: float
    selected_fire_actions: float
    selected_water_actions: float
    selected_attribution_errors: float
    supports_weather_exposure_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        index=0,
        name="mild_clear_control",
        pressure="mild clear work where weather state should not matter",
        expected_weather_pressure=False,
        expected_exposure_pressure=False,
        expected_shelter_pressure=False,
        expected_fire_pressure=False,
        expected_water_pressure=False,
        expected_continuity_pressure=False,
        base_temp_c=20.0,
        cold_intensity=0.0,
        heat_intensity=0.0,
        rain_intensity=0.0,
        wind_intensity=0.0,
        storm_start_fraction=0.95,
        storm_duration_fraction=0.0,
        drought=0.0,
        initial_hydration=0.72,
        hydration_loss=0.0013,
        initial_exposure=0.04,
        shelter_travel_ticks=24,
        required_progress=128.0,
        work_rate=0.70,
        fire_available=False,
        water_available=False,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=1,
        name="cold_rain_exposure",
        pressure="cold rain silently accumulates exposure unless shelter and fire are used",
        expected_weather_pressure=True,
        expected_exposure_pressure=True,
        expected_shelter_pressure=True,
        expected_fire_pressure=True,
        expected_water_pressure=False,
        expected_continuity_pressure=False,
        base_temp_c=10.0,
        cold_intensity=0.62,
        heat_intensity=0.0,
        rain_intensity=0.64,
        wind_intensity=0.42,
        storm_start_fraction=0.06,
        storm_duration_fraction=0.82,
        drought=0.0,
        initial_hydration=0.70,
        hydration_loss=0.0015,
        initial_exposure=0.46,
        shelter_travel_ticks=18,
        required_progress=82.0,
        work_rate=0.63,
        fire_available=True,
        water_available=False,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=2,
        name="heat_drought_hydration",
        pressure="heat and drought turn water planning into future capability preservation",
        expected_weather_pressure=True,
        expected_exposure_pressure=True,
        expected_shelter_pressure=False,
        expected_fire_pressure=False,
        expected_water_pressure=True,
        expected_continuity_pressure=False,
        base_temp_c=34.0,
        cold_intensity=0.0,
        heat_intensity=0.72,
        rain_intensity=0.0,
        wind_intensity=0.18,
        storm_start_fraction=0.20,
        storm_duration_fraction=0.0,
        drought=0.62,
        initial_hydration=0.58,
        hydration_loss=0.0028,
        initial_exposure=0.12,
        shelter_travel_ticks=26,
        required_progress=84.0,
        work_rate=0.64,
        fire_available=False,
        water_available=True,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=3,
        name="storm_shelter_fire",
        pressure="a forecast storm makes shelter timing and fire/light tools valuable",
        expected_weather_pressure=True,
        expected_exposure_pressure=True,
        expected_shelter_pressure=True,
        expected_fire_pressure=True,
        expected_water_pressure=False,
        expected_continuity_pressure=False,
        base_temp_c=12.0,
        cold_intensity=0.48,
        heat_intensity=0.0,
        rain_intensity=0.72,
        wind_intensity=0.78,
        storm_start_fraction=0.44,
        storm_duration_fraction=0.42,
        drought=0.0,
        initial_hydration=0.72,
        hydration_loss=0.0014,
        initial_exposure=0.08,
        shelter_travel_ticks=28,
        required_progress=78.0,
        work_rate=0.62,
        fire_available=True,
        water_available=False,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=4,
        name="restore_forecast_continuity",
        pressure="after restore, forecast, shelter, and fire continuity prevent repeated exposure mistakes",
        expected_weather_pressure=True,
        expected_exposure_pressure=True,
        expected_shelter_pressure=True,
        expected_fire_pressure=True,
        expected_water_pressure=False,
        expected_continuity_pressure=True,
        base_temp_c=11.0,
        cold_intensity=0.54,
        heat_intensity=0.0,
        rain_intensity=0.64,
        wind_intensity=0.62,
        storm_start_fraction=0.36,
        storm_duration_fraction=0.56,
        drought=0.0,
        initial_hydration=0.70,
        hydration_loss=0.0015,
        initial_exposure=0.12,
        shelter_travel_ticks=24,
        required_progress=76.0,
        work_rate=0.61,
        fire_available=True,
        water_available=False,
        restore_tick=104,
    ),
)


SEEDED_POLICIES = (
    Policy(
        name="no_weather_baseline",
        weather_state=False,
        exposure_state=False,
        shelter_memory=False,
        fire_tools=False,
        water_planning=False,
        continuity_memory=False,
        forecast_horizon=0,
        exposure_threshold=0.88,
        hydration_threshold=0.22,
        storm_risk_threshold=0.90,
        tool_cost_tolerance=0.0,
        risk_tolerance=0.72,
    ),
    Policy(
        name="weather_reactive_worker",
        weather_state=True,
        exposure_state=False,
        shelter_memory=False,
        fire_tools=False,
        water_planning=False,
        continuity_memory=False,
        forecast_horizon=8,
        exposure_threshold=0.70,
        hydration_threshold=0.30,
        storm_risk_threshold=0.62,
        tool_cost_tolerance=0.0,
        risk_tolerance=0.56,
    ),
    Policy(
        name="exposure_shelter_planner",
        weather_state=True,
        exposure_state=True,
        shelter_memory=True,
        fire_tools=False,
        water_planning=False,
        continuity_memory=False,
        forecast_horizon=24,
        exposure_threshold=0.42,
        hydration_threshold=0.34,
        storm_risk_threshold=0.40,
        tool_cost_tolerance=0.20,
        risk_tolerance=0.34,
    ),
    Policy(
        name="heat_water_planner",
        weather_state=True,
        exposure_state=True,
        shelter_memory=False,
        fire_tools=False,
        water_planning=True,
        continuity_memory=False,
        forecast_horizon=18,
        exposure_threshold=0.48,
        hydration_threshold=0.50,
        storm_risk_threshold=0.42,
        tool_cost_tolerance=0.42,
        risk_tolerance=0.38,
    ),
    Policy(
        name="storm_fire_planner",
        weather_state=True,
        exposure_state=True,
        shelter_memory=True,
        fire_tools=True,
        water_planning=False,
        continuity_memory=True,
        forecast_horizon=34,
        exposure_threshold=0.38,
        hydration_threshold=0.38,
        storm_risk_threshold=0.34,
        tool_cost_tolerance=0.72,
        risk_tolerance=0.22,
    ),
    Policy(
        name="continuity_weather_planner",
        weather_state=True,
        exposure_state=True,
        shelter_memory=True,
        fire_tools=True,
        water_planning=True,
        continuity_memory=True,
        forecast_horizon=40,
        exposure_threshold=0.36,
        hydration_threshold=0.48,
        storm_risk_threshold=0.32,
        tool_cost_tolerance=0.78,
        risk_tolerance=0.20,
    ),
)


CONDITIONS = (
    "full_control",
    "no_weather_state",
    "no_exposure_state",
    "no_shelter_memory",
    "no_fire_tools",
    "no_water_planning",
    "no_continuity",
    "reactive_weather_only",
    "omniscient_weather_control",
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


def build_policies(cfg: WeatherConfig) -> List[Policy]:
    policies = list(SEEDED_POLICIES)
    rng = random.Random(cfg.seed + 991)
    while len(policies) < cfg.candidate_count:
        base = rng.choice(SEEDED_POLICIES[1:])
        policies.append(
            Policy(
                name=f"mutant_weather_{len(policies)}",
                weather_state=base.weather_state if rng.random() > 0.14 else not base.weather_state,
                exposure_state=base.exposure_state if rng.random() > 0.14 else not base.exposure_state,
                shelter_memory=base.shelter_memory if rng.random() > 0.18 else not base.shelter_memory,
                fire_tools=base.fire_tools if rng.random() > 0.18 else not base.fire_tools,
                water_planning=base.water_planning if rng.random() > 0.18 else not base.water_planning,
                continuity_memory=base.continuity_memory if rng.random() > 0.14 else not base.continuity_memory,
                forecast_horizon=max(0, base.forecast_horizon + rng.randint(-8, 8)),
                exposure_threshold=clamp(base.exposure_threshold + rng.uniform(-0.08, 0.08), 0.26, 0.82),
                hydration_threshold=clamp(base.hydration_threshold + rng.uniform(-0.06, 0.06), 0.28, 0.62),
                storm_risk_threshold=clamp(base.storm_risk_threshold + rng.uniform(-0.08, 0.08), 0.22, 0.72),
                tool_cost_tolerance=clamp(base.tool_cost_tolerance + rng.uniform(-0.10, 0.10), 0.0, 1.0),
                risk_tolerance=clamp(base.risk_tolerance + rng.uniform(-0.08, 0.08), 0.14, 0.80),
            )
        )
    return policies


def condition_policy(policy: Policy, condition: str) -> Policy:
    if condition == "omniscient_weather_control":
        return Policy(
            name=policy.name,
            weather_state=True,
            exposure_state=True,
            shelter_memory=True,
            fire_tools=True,
            water_planning=True,
            continuity_memory=True,
            forecast_horizon=max(policy.forecast_horizon, 48),
            exposure_threshold=min(policy.exposure_threshold, 0.34),
            hydration_threshold=max(policy.hydration_threshold, 0.52),
            storm_risk_threshold=min(policy.storm_risk_threshold, 0.25),
            tool_cost_tolerance=1.0,
            risk_tolerance=0.10,
        )
    if condition == "reactive_weather_only":
        return Policy(
            name=policy.name,
            weather_state=False,
            exposure_state=True,
            shelter_memory=policy.shelter_memory,
            fire_tools=False,
            water_planning=policy.water_planning,
            continuity_memory=policy.continuity_memory,
            forecast_horizon=0,
            exposure_threshold=max(policy.exposure_threshold, 0.58),
            hydration_threshold=policy.hydration_threshold,
            storm_risk_threshold=0.80,
            tool_cost_tolerance=0.0,
            risk_tolerance=policy.risk_tolerance,
        )
    return Policy(
        name=policy.name,
        weather_state=policy.weather_state and condition != "no_weather_state",
        exposure_state=policy.exposure_state and condition != "no_exposure_state",
        shelter_memory=policy.shelter_memory and condition != "no_shelter_memory",
        fire_tools=policy.fire_tools and condition != "no_fire_tools",
        water_planning=policy.water_planning and condition != "no_water_planning",
        continuity_memory=policy.continuity_memory and condition != "no_continuity",
        forecast_horizon=policy.forecast_horizon,
        exposure_threshold=policy.exposure_threshold,
        hydration_threshold=policy.hydration_threshold,
        storm_risk_threshold=policy.storm_risk_threshold,
        tool_cost_tolerance=policy.tool_cost_tolerance,
        risk_tolerance=policy.risk_tolerance,
    )


def scenario_seed(cfg: WeatherConfig, scenario: ScenarioSpec, policy: Policy, condition: str, episode: int, phase: str) -> int:
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
        (policy.weather_state, 0.70),
        (policy.exposure_state, 0.65),
        (policy.shelter_memory, 0.65),
        (policy.fire_tools, 0.25),
        (policy.water_planning, 0.55),
        (policy.continuity_memory, 0.85),
    ]
    return sum(weight for enabled, weight in weighted_flags if enabled)


def storm_active(tick: int, cfg: WeatherConfig, scenario: ScenarioSpec) -> bool:
    phase = tick / max(1, cfg.ticks - 1)
    start = scenario.storm_start_fraction
    end = start + scenario.storm_duration_fraction
    return start <= phase <= end


def weather_snapshot(tick: int, cfg: WeatherConfig, scenario: ScenarioSpec) -> Dict[str, float]:
    active = 1.0 if storm_active(tick, cfg, scenario) else 0.0
    day_phase = tick / max(1, cfg.ticks - 1)
    heat_curve = 0.72 + 0.28 * (1.0 if 0.22 <= day_phase <= 0.78 else 0.45)
    cold = scenario.cold_intensity * (0.28 + 0.72 * active)
    heat = scenario.heat_intensity * heat_curve
    rain = scenario.rain_intensity * (0.18 + 0.82 * active)
    wind = scenario.wind_intensity * (0.22 + 0.78 * active)
    temp = scenario.base_temp_c - cold * 18.0 + heat * 16.0 - rain * active * 2.0
    cold_stress = max(0.0, (8.0 - temp) / 20.0)
    heat_stress = max(0.0, (temp - 30.0) / 18.0)
    wet_stress = rain * 0.42
    wind_stress = wind * 0.30
    total = clamp(cold_stress + heat_stress + wet_stress + wind_stress, 0.0, 1.6)
    return {
        "temperature_c": temp,
        "cold_stress": cold_stress,
        "heat_stress": heat_stress,
        "rain": rain,
        "wind": wind,
        "weather_risk": total,
        "storm_active": active,
        "light_level": clamp(0.82 - rain * 0.40 - wind * 0.14 - active * 0.20, 0.16, 0.92),
    }


def forecast_risk(tick: int, cfg: WeatherConfig, scenario: ScenarioSpec, horizon: int) -> float:
    if horizon <= 0:
        return weather_snapshot(tick, cfg, scenario)["weather_risk"]
    step = max(1, horizon // 4)
    risks = []
    for ahead in range(0, horizon + 1, step):
        risks.append(weather_snapshot(min(cfg.ticks - 1, tick + ahead), cfg, scenario)["weather_risk"])
    return max(risks)


def choose_action(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    tick: int,
    cfg: WeatherConfig,
    hydration: float,
    exposure: float,
    at_shelter: bool,
    fire_ready: bool,
    travel_progress: int,
    rng: random.Random,
) -> str:
    snap = weather_snapshot(tick, cfg, scenario)
    if policy.weather_state:
        observed_weather = snap["weather_risk"]
        observed_forecast = forecast_risk(tick, cfg, scenario, policy.forecast_horizon)
        observed_heat = snap["heat_stress"]
    else:
        observed_weather = 0.16 + rng.uniform(-0.025, 0.025)
        observed_forecast = 0.16 + rng.uniform(-0.025, 0.025)
        observed_heat = 0.05 + rng.uniform(-0.015, 0.015)
    observed_exposure = exposure if policy.exposure_state else 0.18 + rng.uniform(-0.025, 0.025)
    observed_hydration = hydration if policy.water_planning else 0.62 + rng.uniform(-0.025, 0.025)

    if condition == "reactive_weather_only":
        observed_weather = snap["weather_risk"] if exposure > 0.54 else 0.14
        observed_forecast = observed_weather

    if (
        policy.water_planning
        and scenario.water_available
        and (
            observed_hydration < policy.hydration_threshold
            or (observed_heat > 0.30 and scenario.drought > 0.20 and observed_hydration < policy.hydration_threshold + 0.14)
        )
    ):
        return "collect_water"

    shelter_needed = (
        policy.shelter_memory
        and not at_shelter
        and (
            observed_forecast >= policy.storm_risk_threshold
            or observed_weather >= policy.storm_risk_threshold
            or observed_exposure >= policy.exposure_threshold
        )
    )
    if shelter_needed:
        return "travel_shelter"

    if (
        policy.fire_tools
        and scenario.fire_available
        and at_shelter
        and not fire_ready
        and policy.tool_cost_tolerance > 0.30
        and (observed_forecast > 0.38 or observed_exposure > policy.exposure_threshold - 0.12)
    ):
        return "build_fire"

    if (
        at_shelter
        and policy.exposure_state
        and observed_exposure > policy.exposure_threshold
        and observed_weather > policy.risk_tolerance * 0.55
    ):
        return "rest_shelter"

    return "work"


def exposure_delta(snapshot: Dict[str, float], at_shelter: bool, fire_ready: bool, action: str) -> float:
    cold_wet = snapshot["cold_stress"] + snapshot["rain"] * 0.36 + snapshot["wind"] * 0.22
    heat = snapshot["heat_stress"] * 0.72
    base = (cold_wet + heat) * 0.0065
    if at_shelter:
        base *= 0.28
    if fire_ready and at_shelter:
        base *= 0.32
    if action == "rest_shelter":
        base -= 0.026 + (0.014 if fire_ready else 0.0)
    if action == "travel_shelter":
        base *= 1.25
    if action == "work" and not at_shelter:
        base *= 1.18
    return base


def simulate_episode(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episode: int,
    cfg: WeatherConfig,
    phase: str,
    collect_trace: bool = False,
) -> Tuple[EpisodeResult, List[Dict[str, object]]]:
    effective = condition_policy(policy, condition)
    rng = random.Random(scenario_seed(cfg, scenario, policy, condition, episode, phase))
    hydration = clamp(scenario.initial_hydration + rng.uniform(-0.025, 0.025), 0.0, 1.0)
    exposure = clamp(scenario.initial_exposure + rng.uniform(-0.020, 0.020), 0.0, 1.0)
    illness_risk = 0.0
    progress = 0.0
    shelter_quality = 0.62
    at_shelter = False
    fire_ready = False
    travel_progress = 0
    collapse_risk = 0.0
    collapsed = False

    work_actions = 0
    shelter_actions = 0
    fire_actions = 0
    water_actions = 0
    rest_actions = 0
    exposed_ticks = 0
    storm_exposed_ticks = 0
    weather_reads = 0
    exposure_reads = 0
    shelter_reads = 0
    water_reads = 0
    continuity_resets = 0
    attribution_errors = 0
    thermal_samples: List[float] = []
    trace_frames: List[Dict[str, object]] = []

    for tick in range(cfg.ticks):
        snap = weather_snapshot(tick, cfg, scenario)
        thermal_samples.append(max(snap["cold_stress"], snap["heat_stress"]))

        if scenario.restore_tick == tick and not effective.continuity_memory:
            at_shelter = False
            fire_ready = False
            travel_progress = 0
            exposure = clamp(exposure + 0.14 + snap["weather_risk"] * 0.05, 0.0, 1.0)
            continuity_resets += 1

        if collapsed:
            action = "collapsed"
        else:
            if effective.weather_state:
                weather_reads += 1
            if effective.exposure_state:
                exposure_reads += 1
            if effective.shelter_memory:
                shelter_reads += 1
            if effective.water_planning:
                water_reads += 1

            action = choose_action(
                scenario,
                effective,
                condition,
                tick,
                cfg,
                hydration,
                exposure,
                at_shelter,
                fire_ready,
                travel_progress,
                rng,
            )

            heat_hydration_loss = snap["heat_stress"] * (0.0044 + scenario.drought * 0.0022)
            hydration = clamp(hydration - scenario.hydration_loss - heat_hydration_loss, 0.0, 1.0)

            if action == "travel_shelter":
                shelter_actions += 1
                travel_progress += 1
                progress += scenario.work_rate * 0.07
                hydration = clamp(hydration - 0.0018, 0.0, 1.0)
                if travel_progress >= scenario.shelter_travel_ticks:
                    at_shelter = True
                    shelter_quality = clamp(shelter_quality + 0.08, 0.0, 1.0)
            elif action == "build_fire":
                fire_actions += 1
                fire_ready = True
                shelter_quality = clamp(shelter_quality + 0.04, 0.0, 1.0)
                hydration = clamp(hydration - 0.002, 0.0, 1.0)
                progress -= 0.24
            elif action == "collect_water":
                water_actions += 1
                water_gain = 0.112 - scenario.drought * 0.030 + rng.uniform(-0.006, 0.006)
                hydration = clamp(hydration + water_gain, 0.0, 1.0)
                progress += scenario.work_rate * 0.06
                exposure = clamp(exposure + max(0.0, snap["weather_risk"] - 0.26) * 0.0035, 0.0, 1.0)
            elif action == "rest_shelter":
                rest_actions += 1
                exposure = clamp(exposure - 0.017 - (0.015 if fire_ready else 0.0), 0.0, 1.0)
                hydration = clamp(hydration - 0.001, 0.0, 1.0)
            else:
                work_actions += 1
                need_penalty = max(0.0, 0.38 - hydration) * 1.35
                exposure_penalty = exposure * 0.78
                weather_penalty = snap["weather_risk"] * (0.20 if at_shelter else 0.38)
                if fire_ready and at_shelter:
                    weather_penalty *= 0.38
                capability = clamp(1.0 - need_penalty - exposure_penalty - weather_penalty, 0.04, 1.0)
                progress += scenario.work_rate * capability

            delta = exposure_delta(snap, at_shelter, fire_ready, action)
            if at_shelter and not fire_ready and scenario.expected_fire_pressure and snap["weather_risk"] > 0.36:
                delta += snap["weather_risk"] * 0.0028
            exposure = clamp(exposure + delta, 0.0, 1.0)
            if not at_shelter and snap["weather_risk"] > 0.32:
                exposed_ticks += 1
                if snap["storm_active"]:
                    storm_exposed_ticks += 1
            if exposure > 0.40 and (snap["rain"] > 0.18 or snap["cold_stress"] > 0.12):
                illness_risk = clamp(illness_risk + (exposure - 0.36) * 0.0045 + snap["rain"] * 0.0014, 0.0, 1.0)
            if at_shelter:
                shelter_quality = clamp(shelter_quality - snap["wind"] * 0.0009 - snap["rain"] * 0.0008, 0.0, 1.0)
            if fire_ready:
                fire_ready = rng.random() > 0.002 + snap["rain"] * 0.001

            if (snap["weather_risk"] > 0.42 or exposure > 0.48) and not effective.weather_state:
                attribution_errors += 1 if tick % 9 == 0 else 0
            if exposure > 0.48 and not effective.exposure_state:
                attribution_errors += 1 if tick % 8 == 0 else 0
            if hydration < 0.36 and not effective.water_planning and scenario.expected_water_pressure:
                attribution_errors += 1 if tick % 7 == 0 else 0

            collapse_risk = max(
                collapse_risk,
                max(0.0, exposure - 0.82) * 1.15
                + max(0.0, 0.24 - hydration) * 1.35
                + illness_risk * 0.34,
            )
            if collapse_risk >= 1.0:
                collapsed = True

        if collect_trace and (tick % 5 == 0 or tick == cfg.ticks - 1):
            trace_frames.append(
                {
                    "tick": tick,
                    "action": action,
                    "temperature_c": round(snap["temperature_c"], 2),
                    "rain": round(snap["rain"], 3),
                    "wind": round(snap["wind"], 3),
                    "weather_risk": round(snap["weather_risk"], 3),
                    "storm_active": bool(snap["storm_active"]),
                    "light_level": round(snap["light_level"], 3),
                    "hydration": round(hydration, 3),
                    "exposure_debt": round(exposure, 3),
                    "illness_risk": round(illness_risk, 3),
                    "progress": round(progress, 3),
                    "collapse_risk": round(collapse_risk, 3),
                    "at_shelter": at_shelter,
                    "fire_ready": fire_ready,
                    "shelter_quality": round(shelter_quality, 3),
                    "continuity_resets": continuity_resets,
                    "exposed_ticks": exposed_ticks,
                }
            )

    task_success = progress >= scenario.required_progress and not collapsed
    survival = 1.0 if not collapsed and collapse_risk < 0.88 else 0.0
    mean_thermal = mean(thermal_samples)

    reward = progress
    reward += 34.0 if task_success else -20.0
    reward += 36.0 if survival else -96.0
    reward += hydration * (12.0 if scenario.expected_water_pressure else 6.0)
    reward += shelter_quality * (12.0 if scenario.expected_shelter_pressure else 2.0)
    reward += (1.0 - exposure) * (34.0 if scenario.expected_exposure_pressure else 8.0)
    reward -= illness_risk * 58.0
    reward -= collapse_risk * 84.0
    reward -= exposed_ticks * (0.44 if scenario.expected_exposure_pressure else 0.06)
    reward -= storm_exposed_ticks * (0.42 if scenario.expected_weather_pressure else 0.02)
    reward -= attribution_errors * 0.70
    reward -= fire_actions * 0.30
    reward -= water_actions * 0.18
    reward -= rest_actions * 0.05
    reward -= shelter_actions * 0.03
    reward -= feature_overhead(effective)
    if scenario.expected_continuity_pressure and continuity_resets:
        reward -= 46.0

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
        final_hydration=hydration,
        exposure_debt=exposure,
        thermal_stress=mean_thermal,
        illness_risk=illness_risk,
        shelter_quality=shelter_quality,
        fire_readiness=1.0 if fire_ready else 0.0,
        collapse_risk=collapse_risk,
        work_actions=work_actions,
        shelter_actions=shelter_actions,
        fire_actions=fire_actions,
        water_actions=water_actions,
        rest_actions=rest_actions,
        exposed_ticks=exposed_ticks,
        storm_exposed_ticks=storm_exposed_ticks,
        weather_reads=weather_reads,
        exposure_reads=exposure_reads,
        shelter_reads=shelter_reads,
        water_reads=water_reads,
        continuity_resets=continuity_resets,
        attribution_errors=attribution_errors,
    )
    return result, trace_frames


def evaluate_policy(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episodes: int,
    cfg: WeatherConfig,
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
                    mean_final_hydration=mean(row.final_hydration for row in subset),
                    mean_exposure_debt=mean(row.exposure_debt for row in subset),
                    mean_thermal_stress=mean(row.thermal_stress for row in subset),
                    mean_illness_risk=mean(row.illness_risk for row in subset),
                    mean_shelter_quality=mean(row.shelter_quality for row in subset),
                    mean_fire_readiness=mean(row.fire_readiness for row in subset),
                    mean_collapse_risk=mean(row.collapse_risk for row in subset),
                    mean_work_actions=mean(row.work_actions for row in subset),
                    mean_shelter_actions=mean(row.shelter_actions for row in subset),
                    mean_fire_actions=mean(row.fire_actions for row in subset),
                    mean_water_actions=mean(row.water_actions for row in subset),
                    mean_rest_actions=mean(row.rest_actions for row in subset),
                    mean_exposed_ticks=mean(row.exposed_ticks for row in subset),
                    mean_storm_exposed_ticks=mean(row.storm_exposed_ticks for row in subset),
                    mean_weather_reads=mean(row.weather_reads for row in subset),
                    mean_exposure_reads=mean(row.exposure_reads for row in subset),
                    mean_shelter_reads=mean(row.shelter_reads for row in subset),
                    mean_water_reads=mean(row.water_reads for row in subset),
                    mean_continuity_resets=mean(row.continuity_resets for row in subset),
                    mean_attribution_errors=mean(row.attribution_errors for row in subset),
                )
            )
    return rows


def select_policies(cfg: WeatherConfig, policies: Sequence[Policy]) -> Tuple[Dict[int, Policy], List[PolicySelectionRow]]:
    selected: Dict[int, Policy] = {}
    rows: List[PolicySelectionRow] = []
    baseline = next(policy for policy in policies if policy.name == "no_weather_baseline")
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
                selected_uses_weather_state=selected_policy.weather_state,
                selected_uses_exposure_state=selected_policy.exposure_state,
                selected_uses_shelter_memory=selected_policy.shelter_memory,
                selected_uses_fire_tools=selected_policy.fire_tools,
                selected_uses_water_planning=selected_policy.water_planning,
                selected_uses_continuity=selected_policy.continuity_memory,
                train_reward=selected_reward,
                no_weather_train_reward=baseline_reward,
                train_gain_over_no_weather=selected_reward - baseline_reward,
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
        no_weather = lookup[(scenario.index, "no_weather_state")]
        no_exposure = lookup[(scenario.index, "no_exposure_state")]
        no_shelter = lookup[(scenario.index, "no_shelter_memory")]
        no_fire = lookup[(scenario.index, "no_fire_tools")]
        no_water = lookup[(scenario.index, "no_water_planning")]
        no_continuity = lookup[(scenario.index, "no_continuity")]
        reactive = lookup[(scenario.index, "reactive_weather_only")]
        omniscient = lookup[(scenario.index, "omniscient_weather_control")]

        no_weather_loss = full.mean_reward - no_weather.mean_reward
        no_exposure_loss = full.mean_reward - no_exposure.mean_reward
        no_shelter_loss = full.mean_reward - no_shelter.mean_reward
        no_fire_loss = full.mean_reward - no_fire.mean_reward
        no_water_loss = full.mean_reward - no_water.mean_reward
        no_continuity_loss = full.mean_reward - no_continuity.mean_reward
        reactive_loss = full.mean_reward - reactive.mean_reward

        if scenario.index == 0:
            supports = (
                selected[scenario.index].name == "no_weather_baseline"
                and abs(no_weather_loss) < 4.0
                and abs(no_exposure_loss) < 4.0
                and full.mean_exposed_ticks < 1.0
            )
            verdict = "weather_machinery_rejected_in_mild_control"
        elif scenario.index == 1:
            supports = (
                no_weather_loss > 10.0
                and no_exposure_loss > 14.0
                and no_shelter_loss > 18.0
                and no_fire_loss > 8.0
                and full.mean_exposed_ticks < no_shelter.mean_exposed_ticks
            )
            verdict = "cold_rain_exposure_shelter_fire_pressure"
        elif scenario.index == 2:
            supports = (
                no_water_loss > 26.0
                and no_weather_loss > 8.0
                and full.mean_water_actions > 6.0
                and full.mean_final_hydration > no_water.mean_final_hydration
            )
            verdict = "heat_drought_water_planning_pressure"
        elif scenario.index == 3:
            supports = (
                no_weather_loss > 18.0
                and no_shelter_loss > 18.0
                and no_fire_loss > 10.0
                and reactive_loss > 10.0
                and full.mean_storm_exposed_ticks < reactive.mean_storm_exposed_ticks
            )
            verdict = "forecast_storm_shelter_fire_pressure"
        else:
            supports = (
                no_continuity_loss > 22.0
                and no_weather_loss > 12.0
                and no_shelter_loss > 14.0
                and no_continuity.mean_continuity_resets > 0.5
            )
            verdict = "restore_weather_continuity_pressure"

        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                expected_pressure=scenario.pressure,
                selected_policy=selected[scenario.index].name,
                selected_reward=full.mean_reward,
                no_weather_state_reward=no_weather.mean_reward,
                no_exposure_state_reward=no_exposure.mean_reward,
                no_shelter_memory_reward=no_shelter.mean_reward,
                no_fire_tools_reward=no_fire.mean_reward,
                no_water_planning_reward=no_water.mean_reward,
                no_continuity_reward=no_continuity.mean_reward,
                reactive_weather_only_reward=reactive.mean_reward,
                omniscient_weather_control_reward=omniscient.mean_reward,
                weather_gain_over_no_weather=full.mean_reward - no_weather.mean_reward,
                no_weather_state_loss=no_weather_loss,
                no_exposure_state_loss=no_exposure_loss,
                no_shelter_memory_loss=no_shelter_loss,
                no_fire_tools_loss=no_fire_loss,
                no_water_planning_loss=no_water_loss,
                no_continuity_loss=no_continuity_loss,
                reactive_weather_only_loss=reactive_loss,
                selected_exposed_ticks=full.mean_exposed_ticks,
                selected_storm_exposed_ticks=full.mean_storm_exposed_ticks,
                selected_fire_actions=full.mean_fire_actions,
                selected_water_actions=full.mean_water_actions,
                selected_attribution_errors=full.mean_attribution_errors,
                supports_weather_exposure_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def build_trace(cfg: WeatherConfig, selected: Dict[int, Policy]) -> Dict[str, object]:
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
            "mean_exposure_debt": mean(row.exposure_debt for row in rows),
            "mean_illness_risk": mean(row.illness_risk for row in rows),
            "mean_final_hydration": mean(row.final_hydration for row in rows),
            "mean_storm_exposed_ticks": mean(row.storm_exposed_ticks for row in rows),
        }
    return {
        "scenario": asdict(scenario),
        "policy": asdict(policy),
        "episode_result": asdict(result),
        "condition_outcomes": condition_outcomes,
        "frames": frames,
        "trace_note": "Weather, exposure, shelter, fire/light, water planning, and continuity are abstract control variables.",
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
    cfg: WeatherConfig,
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
        "artifact_note": "Weather/exposure dynamics are control variables, not climate or organism simulation.",
    }
    return eval_rows, selection_rows, summary_rows, verdict_rows, {"results": results, "trace": trace}


def print_table(verdicts: Sequence[VerdictRow]) -> None:
    headers = [
        "scenario",
        "policy",
        "weather_loss",
        "exposure_loss",
        "shelter_loss",
        "fire_loss",
        "water_loss",
        "continuity_loss",
        "supports",
    ]
    rows = [
        [
            row.scenario_name,
            row.selected_policy,
            f"{row.no_weather_state_loss:.3f}",
            f"{row.no_exposure_state_loss:.3f}",
            f"{row.no_shelter_memory_loss:.3f}",
            f"{row.no_fire_tools_loss:.3f}",
            f"{row.no_water_planning_loss:.3f}",
            f"{row.no_continuity_loss:.3f}",
            str(row.supports_weather_exposure_precursor),
        ]
        for row in verdicts
    ]
    widths = [max(len(header), *(len(row[index]) for row in rows)) for index, header in enumerate(headers)]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> WeatherConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-episodes", type=int, default=WeatherConfig.train_episodes)
    parser.add_argument("--eval-episodes", type=int, default=WeatherConfig.eval_episodes)
    parser.add_argument("--ticks", type=int, default=WeatherConfig.ticks)
    parser.add_argument("--seed", type=int, default=WeatherConfig.seed)
    parser.add_argument("--candidate-count", type=int, default=WeatherConfig.candidate_count)
    parser.add_argument("--trace-scenario", type=int, default=WeatherConfig.trace_scenario)
    parser.add_argument("--trace-episode", type=int, default=WeatherConfig.trace_episode)
    args = parser.parse_args()
    if args.train_episodes < 24:
        raise SystemExit("--train-episodes must be at least 24")
    if args.eval_episodes < 24:
        raise SystemExit("--eval-episodes must be at least 24")
    if args.candidate_count < len(SEEDED_POLICIES):
        raise SystemExit(f"--candidate-count must be at least {len(SEEDED_POLICIES)}")
    if args.trace_scenario < 0 or args.trace_scenario >= len(SCENARIOS):
        raise SystemExit("--trace-scenario out of range")
    return WeatherConfig(
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

    eval_path = ARTIFACT_DIR / "ssrm_3d_weather_exposure_eval.csv"
    selection_path = ARTIFACT_DIR / "ssrm_3d_weather_exposure_policy_selection.csv"
    summary_path = ARTIFACT_DIR / "ssrm_3d_weather_exposure_summary.csv"
    verdict_path = ARTIFACT_DIR / "ssrm_3d_weather_exposure_verdict.csv"
    results_path = ARTIFACT_DIR / "ssrm_3d_weather_exposure_results.json"
    trace_path = ARTIFACT_DIR / "ssrm_3d_weather_exposure_trace.json"
    results_js_path = ARTIFACT_DIR / "ssrm_3d_weather_exposure_results.js"
    trace_js_path = ARTIFACT_DIR / "ssrm_3d_weather_exposure_trace.js"

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
    write_js(results_js_path, "SSRM_3D_WEATHER_EXPOSURE_RESULTS", payload["results"])
    write_js(trace_js_path, "SSRM_3D_WEATHER_EXPOSURE_TRACE", payload["trace"])

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
    if not all(row.supports_weather_exposure_precursor for row in verdict_rows):
        print("weather/exposure precursor not supported by all verdict rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
