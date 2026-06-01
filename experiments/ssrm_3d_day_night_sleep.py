#!/usr/bin/env python3
"""SSRM-3D day/night sleep-rest precursor.

This experiment implements the second pressure-layer step from report 74:
day/night plus sleep/rest. It is intentionally not a full organism model.
Sleep is treated as a control action that trades immediate vulnerability and
opportunity cost against future capability.

The result remains a designed precursor. It is useful only if rest is rejected
in the low-pressure control, selected under delayed fatigue or night pressure,
and targeted ablations fail specifically rather than causing generic collapse.
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
from typing import Dict, Iterable, List, Sequence, Tuple


ARTIFACT_DIR = Path("artifacts")
EPS = 1e-12


@dataclass(frozen=True)
class SleepConfig:
    train_episodes: int = 72
    eval_episodes: int = 96
    ticks: int = 240
    seed: int = 20260621
    candidate_count: int = 6
    trace_scenario: int = 3
    trace_episode: int = 0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    expected_rest_pressure: bool
    expected_fatigue_pressure: bool
    expected_day_night_pressure: bool
    expected_shelter_pressure: bool
    expected_alarm_pressure: bool
    expected_social_pressure: bool
    expected_continuity_pressure: bool
    initial_fatigue: float
    fatigue_rate: float
    recovery_rate: float
    day_hazard: float
    night_hazard: float
    night_start_fraction: float
    shelter_travel_ticks: int
    required_progress: float
    work_rate: float
    alarm_available: bool
    social_watch_available: bool
    interruption_tick: int
    commitment_pressure: float


@dataclass(frozen=True)
class Policy:
    name: str
    rest_enabled: bool
    fatigue_aware: bool
    day_night_aware: bool
    shelter_memory: bool
    alarm_tools: bool
    social_watch: bool
    continuity_memory: bool
    rest_threshold: float
    wake_threshold: float
    risk_tolerance: float
    fixed_rest_fraction: float
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
    commitment_kept: float
    progress: float
    final_fatigue: float
    hazard_damage: float
    sleep_ticks: int
    unsafe_sleep_ticks: int
    shelter_sleep_ticks: int
    work_ticks: int
    travel_ticks: int
    alarm_uses: int
    social_watch_uses: int
    continuity_resets: int
    fatigue_state_reads: int
    day_night_reads: int
    shelter_memory_reads: int
    mean_vulnerability: float


@dataclass(frozen=True)
class PolicySelectionRow:
    scenario: int
    scenario_name: str
    selected_policy: str
    selected_uses_rest: bool
    selected_uses_fatigue: bool
    selected_uses_day_night: bool
    selected_uses_shelter_memory: bool
    selected_uses_alarm_or_watch: bool
    selected_uses_continuity: bool
    train_reward: float
    no_rest_train_reward: float
    train_gain_over_no_rest: float


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
    mean_commitment_kept: float
    mean_progress: float
    mean_final_fatigue: float
    mean_hazard_damage: float
    mean_sleep_ticks: float
    mean_unsafe_sleep_ticks: float
    mean_shelter_sleep_ticks: float
    mean_work_ticks: float
    mean_travel_ticks: float
    mean_alarm_uses: float
    mean_social_watch_uses: float
    mean_continuity_resets: float
    mean_fatigue_state_reads: float
    mean_day_night_reads: float
    mean_shelter_memory_reads: float
    mean_vulnerability: float


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    expected_pressure: str
    selected_policy: str
    selected_reward: float
    no_rest_reward: float
    no_fatigue_state_reward: float
    no_day_night_state_reward: float
    no_shelter_memory_reward: float
    no_alarm_tools_reward: float
    no_social_watch_reward: float
    no_continuity_reward: float
    fixed_schedule_reward: float
    omniscient_safe_rest_reward: float
    rest_gain_over_no_rest: float
    no_rest_loss: float
    no_fatigue_state_loss: float
    no_day_night_state_loss: float
    no_shelter_memory_loss: float
    no_alarm_tools_loss: float
    no_social_watch_loss: float
    no_continuity_loss: float
    fixed_schedule_loss: float
    selected_sleep_ticks: float
    selected_unsafe_sleep_ticks: float
    selected_shelter_sleep_ticks: float
    selected_alarm_uses: float
    selected_social_watch_uses: float
    supports_day_night_sleep_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        index=0,
        name="open_daylight_control",
        pressure="short daylight task with negligible fatigue and no safe-rest tradeoff",
        expected_rest_pressure=False,
        expected_fatigue_pressure=False,
        expected_day_night_pressure=False,
        expected_shelter_pressure=False,
        expected_alarm_pressure=False,
        expected_social_pressure=False,
        expected_continuity_pressure=False,
        initial_fatigue=0.12,
        fatigue_rate=0.0012,
        recovery_rate=0.020,
        day_hazard=0.01,
        night_hazard=0.03,
        night_start_fraction=0.92,
        shelter_travel_ticks=8,
        required_progress=92.0,
        work_rate=0.58,
        alarm_available=False,
        social_watch_available=False,
        interruption_tick=-1,
        commitment_pressure=0.0,
    ),
    ScenarioSpec(
        index=1,
        name="fatigue_debt_long_horizon",
        pressure="long-horizon work where fatigue silently destroys later capability",
        expected_rest_pressure=True,
        expected_fatigue_pressure=True,
        expected_day_night_pressure=False,
        expected_shelter_pressure=False,
        expected_alarm_pressure=False,
        expected_social_pressure=False,
        expected_continuity_pressure=False,
        initial_fatigue=0.30,
        fatigue_rate=0.0049,
        recovery_rate=0.030,
        day_hazard=0.02,
        night_hazard=0.06,
        night_start_fraction=0.90,
        shelter_travel_ticks=10,
        required_progress=82.0,
        work_rate=0.66,
        alarm_available=False,
        social_watch_available=False,
        interruption_tick=-1,
        commitment_pressure=0.0,
    ),
    ScenarioSpec(
        index=2,
        name="night_shelter_vulnerability",
        pressure="agent must reach remembered shelter before night and sleep there",
        expected_rest_pressure=True,
        expected_fatigue_pressure=True,
        expected_day_night_pressure=True,
        expected_shelter_pressure=True,
        expected_alarm_pressure=False,
        expected_social_pressure=False,
        expected_continuity_pressure=False,
        initial_fatigue=0.38,
        fatigue_rate=0.0044,
        recovery_rate=0.030,
        day_hazard=0.03,
        night_hazard=0.52,
        night_start_fraction=0.62,
        shelter_travel_ticks=26,
        required_progress=66.0,
        work_rate=0.63,
        alarm_available=False,
        social_watch_available=False,
        interruption_tick=-1,
        commitment_pressure=0.0,
    ),
    ScenarioSpec(
        index=3,
        name="alarm_social_guarded_sleep",
        pressure="rest is needed near danger, but alarms and social watch reduce vulnerability",
        expected_rest_pressure=True,
        expected_fatigue_pressure=True,
        expected_day_night_pressure=True,
        expected_shelter_pressure=True,
        expected_alarm_pressure=True,
        expected_social_pressure=True,
        expected_continuity_pressure=False,
        initial_fatigue=0.44,
        fatigue_rate=0.0046,
        recovery_rate=0.028,
        day_hazard=0.08,
        night_hazard=0.66,
        night_start_fraction=0.58,
        shelter_travel_ticks=20,
        required_progress=60.0,
        work_rate=0.61,
        alarm_available=True,
        social_watch_available=True,
        interruption_tick=-1,
        commitment_pressure=0.0,
    ),
    ScenarioSpec(
        index=4,
        name="interrupted_commitment_rest",
        pressure="after restore, the agent must remember both the commitment and its fatigue debt",
        expected_rest_pressure=True,
        expected_fatigue_pressure=True,
        expected_day_night_pressure=True,
        expected_shelter_pressure=True,
        expected_alarm_pressure=True,
        expected_social_pressure=False,
        expected_continuity_pressure=True,
        initial_fatigue=0.42,
        fatigue_rate=0.0047,
        recovery_rate=0.030,
        day_hazard=0.04,
        night_hazard=0.48,
        night_start_fraction=0.64,
        shelter_travel_ticks=22,
        required_progress=68.0,
        work_rate=0.62,
        alarm_available=True,
        social_watch_available=False,
        interruption_tick=118,
        commitment_pressure=1.0,
    ),
)


SEEDED_POLICIES = (
    Policy(
        name="no_rest_baseline",
        rest_enabled=False,
        fatigue_aware=False,
        day_night_aware=False,
        shelter_memory=False,
        alarm_tools=False,
        social_watch=False,
        continuity_memory=False,
        rest_threshold=1.0,
        wake_threshold=0.55,
        risk_tolerance=0.60,
        fixed_rest_fraction=-1.0,
        tool_cost_tolerance=0.0,
    ),
    Policy(
        name="fixed_schedule_rest",
        rest_enabled=True,
        fatigue_aware=False,
        day_night_aware=False,
        shelter_memory=False,
        alarm_tools=False,
        social_watch=False,
        continuity_memory=False,
        rest_threshold=0.66,
        wake_threshold=0.40,
        risk_tolerance=0.54,
        fixed_rest_fraction=0.58,
        tool_cost_tolerance=0.0,
    ),
    Policy(
        name="fatigue_only_rest",
        rest_enabled=True,
        fatigue_aware=True,
        day_night_aware=False,
        shelter_memory=False,
        alarm_tools=False,
        social_watch=False,
        continuity_memory=False,
        rest_threshold=0.62,
        wake_threshold=0.36,
        risk_tolerance=0.62,
        fixed_rest_fraction=-1.0,
        tool_cost_tolerance=0.0,
    ),
    Policy(
        name="shelter_sleep_planner",
        rest_enabled=True,
        fatigue_aware=True,
        day_night_aware=True,
        shelter_memory=True,
        alarm_tools=False,
        social_watch=False,
        continuity_memory=True,
        rest_threshold=0.58,
        wake_threshold=0.34,
        risk_tolerance=0.32,
        fixed_rest_fraction=-1.0,
        tool_cost_tolerance=0.0,
    ),
    Policy(
        name="alarm_guarded_sleep_planner",
        rest_enabled=True,
        fatigue_aware=True,
        day_night_aware=True,
        shelter_memory=True,
        alarm_tools=True,
        social_watch=True,
        continuity_memory=True,
        rest_threshold=0.56,
        wake_threshold=0.33,
        risk_tolerance=0.18,
        fixed_rest_fraction=-1.0,
        tool_cost_tolerance=0.72,
    ),
    Policy(
        name="continuity_recovery_planner",
        rest_enabled=True,
        fatigue_aware=True,
        day_night_aware=True,
        shelter_memory=True,
        alarm_tools=True,
        social_watch=False,
        continuity_memory=True,
        rest_threshold=0.52,
        wake_threshold=0.30,
        risk_tolerance=0.21,
        fixed_rest_fraction=-1.0,
        tool_cost_tolerance=0.80,
    ),
)


CONDITIONS = (
    "full_control",
    "no_rest_action",
    "no_fatigue_state",
    "no_day_night_state",
    "no_shelter_memory",
    "no_alarm_tools",
    "no_social_watch",
    "no_continuity",
    "fixed_schedule_sleep",
    "omniscient_safe_rest",
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


def build_policies(cfg: SleepConfig) -> List[Policy]:
    policies = list(SEEDED_POLICIES)
    rng = random.Random(cfg.seed + 991)
    while len(policies) < cfg.candidate_count:
        base = rng.choice(SEEDED_POLICIES[1:])
        policies.append(
            Policy(
                name=f"mutant_sleep_{len(policies)}",
                rest_enabled=base.rest_enabled,
                fatigue_aware=base.fatigue_aware if rng.random() > 0.15 else not base.fatigue_aware,
                day_night_aware=base.day_night_aware if rng.random() > 0.18 else not base.day_night_aware,
                shelter_memory=base.shelter_memory if rng.random() > 0.18 else not base.shelter_memory,
                alarm_tools=base.alarm_tools if rng.random() > 0.20 else not base.alarm_tools,
                social_watch=base.social_watch if rng.random() > 0.20 else not base.social_watch,
                continuity_memory=base.continuity_memory if rng.random() > 0.12 else not base.continuity_memory,
                rest_threshold=clamp(base.rest_threshold + rng.uniform(-0.08, 0.08), 0.42, 0.78),
                wake_threshold=clamp(base.wake_threshold + rng.uniform(-0.05, 0.05), 0.22, 0.48),
                risk_tolerance=clamp(base.risk_tolerance + rng.uniform(-0.10, 0.10), 0.12, 0.78),
                fixed_rest_fraction=base.fixed_rest_fraction,
                tool_cost_tolerance=clamp(base.tool_cost_tolerance + rng.uniform(-0.10, 0.10), 0.0, 1.0),
            )
        )
    return policies


def condition_policy(policy: Policy, condition: str) -> Policy:
    if condition == "omniscient_safe_rest":
        return Policy(
            name=policy.name,
            rest_enabled=True,
            fatigue_aware=True,
            day_night_aware=True,
            shelter_memory=True,
            alarm_tools=True,
            social_watch=True,
            continuity_memory=True,
            rest_threshold=min(policy.rest_threshold, 0.54),
            wake_threshold=min(policy.wake_threshold, 0.32),
            risk_tolerance=0.05,
            fixed_rest_fraction=-1.0,
            tool_cost_tolerance=1.0,
        )
    if condition == "fixed_schedule_sleep":
        return Policy(
            name=policy.name,
            rest_enabled=True,
            fatigue_aware=False,
            day_night_aware=False,
            shelter_memory=policy.shelter_memory,
            alarm_tools=policy.alarm_tools,
            social_watch=policy.social_watch,
            continuity_memory=policy.continuity_memory,
            rest_threshold=0.64,
            wake_threshold=0.38,
            risk_tolerance=policy.risk_tolerance,
            fixed_rest_fraction=0.60,
            tool_cost_tolerance=policy.tool_cost_tolerance,
        )
    return Policy(
        name=policy.name,
        rest_enabled=policy.rest_enabled and condition != "no_rest_action",
        fatigue_aware=policy.fatigue_aware and condition != "no_fatigue_state",
        day_night_aware=policy.day_night_aware and condition != "no_day_night_state",
        shelter_memory=policy.shelter_memory and condition != "no_shelter_memory",
        alarm_tools=policy.alarm_tools and condition != "no_alarm_tools",
        social_watch=policy.social_watch and condition != "no_social_watch",
        continuity_memory=policy.continuity_memory and condition != "no_continuity",
        rest_threshold=policy.rest_threshold,
        wake_threshold=policy.wake_threshold,
        risk_tolerance=policy.risk_tolerance,
        fixed_rest_fraction=policy.fixed_rest_fraction,
        tool_cost_tolerance=policy.tool_cost_tolerance,
    )


def scenario_seed(cfg: SleepConfig, scenario: ScenarioSpec, policy: Policy, condition: str, episode: int, phase: str) -> int:
    return (
        cfg.seed
        + scenario.index * 100_003
        + stable_hash(policy.name) * 17
        + stable_hash(condition) * 31
        + episode * 997
        + stable_hash(phase) * 43
    )


def light_level(tick: int, cfg: SleepConfig, scenario: ScenarioSpec) -> float:
    phase = tick / max(1, cfg.ticks - 1)
    if phase < scenario.night_start_fraction - 0.08:
        return 0.92
    if phase < scenario.night_start_fraction:
        blend = (phase - (scenario.night_start_fraction - 0.08)) / 0.08
        return 0.92 * (1.0 - blend) + 0.26 * blend
    return 0.18


def is_night(tick: int, cfg: SleepConfig, scenario: ScenarioSpec) -> bool:
    return light_level(tick, cfg, scenario) < 0.35


def time_to_night(tick: int, cfg: SleepConfig, scenario: ScenarioSpec) -> int:
    night_tick = int(cfg.ticks * scenario.night_start_fraction)
    return max(0, night_tick - tick)


def feature_overhead(policy: Policy) -> float:
    flags = [
        policy.rest_enabled,
        policy.fatigue_aware,
        policy.day_night_aware,
        policy.shelter_memory,
        policy.alarm_tools,
        policy.social_watch,
        policy.continuity_memory,
    ]
    return 0.24 * sum(1 for flag in flags if flag)


def current_vulnerability(
    scenario: ScenarioSpec,
    tick: int,
    cfg: SleepConfig,
    at_shelter: bool,
    alarm_ready: bool,
    watch_ready: bool,
) -> float:
    base = scenario.night_hazard if is_night(tick, cfg, scenario) else scenario.day_hazard
    multiplier = 1.0
    if at_shelter:
        multiplier *= 0.68 if (scenario.expected_alarm_pressure or scenario.expected_social_pressure) else 0.30
    if alarm_ready:
        multiplier *= 0.55
    if watch_ready:
        multiplier *= 0.48
    return base * multiplier


def choose_action(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    tick: int,
    cfg: SleepConfig,
    fatigue: float,
    at_shelter: bool,
    alarm_ready: bool,
    watch_ready: bool,
    travel_progress: int,
    rng: random.Random,
) -> str:
    if condition == "omniscient_safe_rest" and policy.rest_enabled:
        if not at_shelter and (fatigue > 0.42 or time_to_night(tick, cfg, scenario) < scenario.shelter_travel_ticks + 28):
            return "travel_shelter"
        if scenario.alarm_available and not alarm_ready and fatigue > 0.44:
            return "set_alarm"
        if scenario.social_watch_available and not watch_ready and fatigue > 0.46:
            return "ask_watch"
        if fatigue > policy.rest_threshold:
            return "rest"
        return "work"

    observed_fatigue = fatigue if policy.fatigue_aware else 0.36 + rng.uniform(-0.035, 0.035)
    observed_time_to_night = time_to_night(tick, cfg, scenario) if policy.day_night_aware else cfg.ticks
    fixed_rest_start = int(cfg.ticks * policy.fixed_rest_fraction) if policy.fixed_rest_fraction >= 0.0 else -1

    needs_shelter_soon = (
        policy.day_night_aware
        and policy.shelter_memory
        and not at_shelter
        and observed_time_to_night <= scenario.shelter_travel_ticks + 22
    )
    needs_rest_shelter = (
        policy.rest_enabled
        and policy.day_night_aware
        and policy.shelter_memory
        and not at_shelter
        and observed_fatigue >= policy.rest_threshold - 0.08
        and scenario.night_hazard > 0.12
    )
    if needs_shelter_soon or needs_rest_shelter:
        return "travel_shelter"

    can_prepare_tools = policy.tool_cost_tolerance > 0.25 and at_shelter
    if (
        policy.rest_enabled
        and policy.alarm_tools
        and scenario.alarm_available
        and can_prepare_tools
        and not alarm_ready
        and (observed_fatigue >= policy.rest_threshold - 0.10 or observed_time_to_night < 36)
    ):
        return "set_alarm"
    if (
        policy.rest_enabled
        and policy.social_watch
        and scenario.social_watch_available
        and at_shelter
        and not watch_ready
        and (observed_fatigue >= policy.rest_threshold - 0.10 or observed_time_to_night < 36)
    ):
        return "ask_watch"

    fixed_resting = fixed_rest_start >= 0 and fixed_rest_start <= tick < fixed_rest_start + 42
    safe_enough = current_vulnerability(scenario, tick, cfg, at_shelter, alarm_ready, watch_ready) <= policy.risk_tolerance
    adaptive_resting = policy.rest_enabled and observed_fatigue >= policy.rest_threshold and safe_enough
    if policy.rest_enabled and (fixed_resting or adaptive_resting):
        return "rest"
    if policy.rest_enabled and observed_fatigue >= 0.82 and rng.random() < policy.risk_tolerance * 0.32:
        return "rest"
    return "work"


def simulate_episode(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episode: int,
    cfg: SleepConfig,
    phase: str,
    collect_trace: bool = False,
) -> Tuple[EpisodeResult, List[Dict[str, object]]]:
    effective = condition_policy(policy, condition)
    rng = random.Random(scenario_seed(cfg, scenario, policy, condition, episode, phase))
    fatigue = clamp(scenario.initial_fatigue + rng.uniform(-0.035, 0.035), 0.0, 1.0)
    hazard_damage = 0.0
    progress = 0.0
    at_shelter = False
    alarm_ready = False
    watch_ready = False
    travel_progress = 0
    collapsed = False
    commitment_active = scenario.commitment_pressure > 0.0
    commitment_kept = 0.0

    sleep_ticks = 0
    unsafe_sleep_ticks = 0
    shelter_sleep_ticks = 0
    work_ticks = 0
    travel_ticks = 0
    alarm_uses = 0
    social_watch_uses = 0
    continuity_resets = 0
    fatigue_state_reads = 0
    day_night_reads = 0
    shelter_memory_reads = 0
    vulnerabilities: List[float] = []
    trace_frames: List[Dict[str, object]] = []

    for tick in range(cfg.ticks):
        if collapsed:
            action = "collapsed"
            vulnerability = current_vulnerability(scenario, tick, cfg, at_shelter, alarm_ready, watch_ready)
            vulnerabilities.append(vulnerability)
        else:
            if scenario.interruption_tick == tick:
                if not effective.continuity_memory:
                    at_shelter = False
                    alarm_ready = False
                    watch_ready = False
                    travel_progress = 0
                    commitment_active = False
                    continuity_resets += 1

            if effective.fatigue_aware:
                fatigue_state_reads += 1
            if effective.day_night_aware:
                day_night_reads += 1
            if effective.shelter_memory:
                shelter_memory_reads += 1

            action = choose_action(
                scenario,
                effective,
                condition,
                tick,
                cfg,
                fatigue,
                at_shelter,
                alarm_ready,
                watch_ready,
                travel_progress,
                rng,
            )
            vulnerability = current_vulnerability(scenario, tick, cfg, at_shelter, alarm_ready, watch_ready)
            vulnerabilities.append(vulnerability)

            if action == "travel_shelter":
                travel_ticks += 1
                travel_progress += 1
                fatigue = clamp(fatigue + scenario.fatigue_rate * 1.25, 0.0, 1.0)
                progress += scenario.work_rate * 0.12
                if travel_progress >= scenario.shelter_travel_ticks:
                    at_shelter = True
                hazard_damage += vulnerability * (0.014 + rng.random() * 0.004)
            elif action == "set_alarm":
                alarm_uses += 1
                alarm_ready = True
                fatigue = clamp(fatigue + scenario.fatigue_rate * 0.45, 0.0, 1.0)
                progress -= 0.24
            elif action == "ask_watch":
                social_watch_uses += 1
                watch_ready = True
                fatigue = clamp(fatigue + scenario.fatigue_rate * 0.35, 0.0, 1.0)
                progress -= 0.30
            elif action == "rest":
                sleep_ticks += 1
                if at_shelter:
                    shelter_sleep_ticks += 1
                if vulnerability > 0.16:
                    unsafe_sleep_ticks += 1
                fatigue = clamp(fatigue - scenario.recovery_rate * (1.18 if at_shelter else 0.76), 0.0, 1.0)
                hazard_damage += vulnerability * (0.030 + rng.random() * 0.006)
            else:
                work_ticks += 1
                dark_penalty = 0.22 if is_night(tick, cfg, scenario) and not at_shelter else 0.0
                fatigue_penalty = fatigue * 0.62
                capability = clamp(1.0 - fatigue_penalty - dark_penalty, 0.08, 1.0)
                progress += scenario.work_rate * capability
                night_bonus = 1.45 if is_night(tick, cfg, scenario) and not at_shelter else 1.0
                fatigue = clamp(fatigue + scenario.fatigue_rate * night_bonus, 0.0, 1.0)
                hazard_damage += vulnerability * (0.012 + rng.random() * 0.004)

            if fatigue >= 0.96:
                hazard_damage += 0.010 + (fatigue - 0.96) * 0.25
            if hazard_damage >= 1.0:
                collapsed = True

        if collect_trace and (tick % 6 == 0 or tick == cfg.ticks - 1):
            trace_frames.append(
                {
                    "tick": tick,
                    "light_level": round(light_level(tick, cfg, scenario), 3),
                    "is_night": is_night(tick, cfg, scenario),
                    "fatigue": round(fatigue, 3),
                    "hazard_damage": round(hazard_damage, 3),
                    "progress": round(progress, 3),
                    "action": action,
                    "at_shelter": at_shelter,
                    "alarm_ready": alarm_ready,
                    "social_watch_ready": watch_ready,
                    "vulnerability": round(vulnerability, 3),
                    "time_to_night": time_to_night(tick, cfg, scenario),
                    "continuity_resets": continuity_resets,
                    "commitment_active": commitment_active,
                }
            )

    task_success = progress >= scenario.required_progress and not collapsed
    if scenario.commitment_pressure > 0.0:
        commitment_kept = 1.0 if task_success and commitment_active and fatigue <= 0.76 else 0.0
    survival = 1.0 if not collapsed and hazard_damage < 0.92 else 0.0

    reward = progress
    reward += 34.0 if task_success else -18.0
    reward += 34.0 if survival else -92.0
    reward += (1.0 - fatigue) * 17.0
    reward -= hazard_damage * 82.0
    reward -= unsafe_sleep_ticks * 0.42
    reward -= sleep_ticks * (0.045 if scenario.expected_rest_pressure else 0.18)
    reward -= alarm_uses * 0.55
    reward -= social_watch_uses * 0.65
    reward -= feature_overhead(effective)
    if scenario.commitment_pressure > 0.0:
        reward += 34.0 if commitment_kept else -34.0

    result = EpisodeResult(
        scenario=scenario.index,
        scenario_name=scenario.name,
        policy_name=policy.name,
        condition=condition,
        episode=episode,
        total_reward=reward,
        survival=survival,
        task_success=1.0 if task_success else 0.0,
        commitment_kept=commitment_kept,
        progress=progress,
        final_fatigue=fatigue,
        hazard_damage=hazard_damage,
        sleep_ticks=sleep_ticks,
        unsafe_sleep_ticks=unsafe_sleep_ticks,
        shelter_sleep_ticks=shelter_sleep_ticks,
        work_ticks=work_ticks,
        travel_ticks=travel_ticks,
        alarm_uses=alarm_uses,
        social_watch_uses=social_watch_uses,
        continuity_resets=continuity_resets,
        fatigue_state_reads=fatigue_state_reads,
        day_night_reads=day_night_reads,
        shelter_memory_reads=shelter_memory_reads,
        mean_vulnerability=mean(vulnerabilities),
    )
    return result, trace_frames


def evaluate_policy(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episodes: int,
    cfg: SleepConfig,
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
                    mean_commitment_kept=mean(row.commitment_kept for row in subset),
                    mean_progress=mean(row.progress for row in subset),
                    mean_final_fatigue=mean(row.final_fatigue for row in subset),
                    mean_hazard_damage=mean(row.hazard_damage for row in subset),
                    mean_sleep_ticks=mean(row.sleep_ticks for row in subset),
                    mean_unsafe_sleep_ticks=mean(row.unsafe_sleep_ticks for row in subset),
                    mean_shelter_sleep_ticks=mean(row.shelter_sleep_ticks for row in subset),
                    mean_work_ticks=mean(row.work_ticks for row in subset),
                    mean_travel_ticks=mean(row.travel_ticks for row in subset),
                    mean_alarm_uses=mean(row.alarm_uses for row in subset),
                    mean_social_watch_uses=mean(row.social_watch_uses for row in subset),
                    mean_continuity_resets=mean(row.continuity_resets for row in subset),
                    mean_fatigue_state_reads=mean(row.fatigue_state_reads for row in subset),
                    mean_day_night_reads=mean(row.day_night_reads for row in subset),
                    mean_shelter_memory_reads=mean(row.shelter_memory_reads for row in subset),
                    mean_vulnerability=mean(row.mean_vulnerability for row in subset),
                )
            )
    return rows


def select_policies(cfg: SleepConfig, policies: Sequence[Policy]) -> Tuple[Dict[int, Policy], List[PolicySelectionRow]]:
    selected: Dict[int, Policy] = {}
    rows: List[PolicySelectionRow] = []
    baseline = next(policy for policy in policies if policy.name == "no_rest_baseline")
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
                selected_uses_rest=selected_policy.rest_enabled,
                selected_uses_fatigue=selected_policy.fatigue_aware,
                selected_uses_day_night=selected_policy.day_night_aware,
                selected_uses_shelter_memory=selected_policy.shelter_memory,
                selected_uses_alarm_or_watch=selected_policy.alarm_tools or selected_policy.social_watch,
                selected_uses_continuity=selected_policy.continuity_memory,
                train_reward=selected_reward,
                no_rest_train_reward=baseline_reward,
                train_gain_over_no_rest=selected_reward - baseline_reward,
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
        no_rest = lookup[(scenario.index, "no_rest_action")]
        no_fatigue = lookup[(scenario.index, "no_fatigue_state")]
        no_day = lookup[(scenario.index, "no_day_night_state")]
        no_shelter = lookup[(scenario.index, "no_shelter_memory")]
        no_alarm = lookup[(scenario.index, "no_alarm_tools")]
        no_social = lookup[(scenario.index, "no_social_watch")]
        no_continuity = lookup[(scenario.index, "no_continuity")]
        fixed = lookup[(scenario.index, "fixed_schedule_sleep")]
        omniscient = lookup[(scenario.index, "omniscient_safe_rest")]

        no_rest_loss = full.mean_reward - no_rest.mean_reward
        no_fatigue_loss = full.mean_reward - no_fatigue.mean_reward
        no_day_loss = full.mean_reward - no_day.mean_reward
        no_shelter_loss = full.mean_reward - no_shelter.mean_reward
        no_alarm_loss = full.mean_reward - no_alarm.mean_reward
        no_social_loss = full.mean_reward - no_social.mean_reward
        no_continuity_loss = full.mean_reward - no_continuity.mean_reward
        fixed_loss = full.mean_reward - fixed.mean_reward

        if scenario.index == 0:
            supports = (
                selected[scenario.index].name == "no_rest_baseline"
                and abs(no_rest_loss) < 3.0
                and no_fatigue_loss < 3.0
                and full.mean_sleep_ticks < 1.0
            )
            verdict = "rest_rejected_in_daylight_control"
        elif scenario.index == 1:
            supports = no_rest_loss > 24.0 and no_fatigue_loss > 18.0 and full.mean_sleep_ticks > 12.0
            verdict = "fatigue_debt_requires_adaptive_rest"
        elif scenario.index == 2:
            supports = no_day_loss > 18.0 and no_shelter_loss > 22.0 and full.mean_shelter_sleep_ticks > 12.0
            verdict = "night_shelter_sleep_pressure"
        elif scenario.index == 3:
            supports = (
                no_alarm_loss > 14.0
                and no_social_loss > 10.0
                and full.mean_alarm_uses > 0.5
                and full.mean_social_watch_uses > 0.5
            )
            verdict = "guarded_sleep_tool_social_pressure"
        else:
            supports = no_continuity_loss > 20.0 and no_rest_loss > 20.0 and no_fatigue_loss > 16.0
            verdict = "interruption_rest_commitment_continuity_pressure"

        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                expected_pressure=scenario.pressure,
                selected_policy=selected[scenario.index].name,
                selected_reward=full.mean_reward,
                no_rest_reward=no_rest.mean_reward,
                no_fatigue_state_reward=no_fatigue.mean_reward,
                no_day_night_state_reward=no_day.mean_reward,
                no_shelter_memory_reward=no_shelter.mean_reward,
                no_alarm_tools_reward=no_alarm.mean_reward,
                no_social_watch_reward=no_social.mean_reward,
                no_continuity_reward=no_continuity.mean_reward,
                fixed_schedule_reward=fixed.mean_reward,
                omniscient_safe_rest_reward=omniscient.mean_reward,
                rest_gain_over_no_rest=full.mean_reward - no_rest.mean_reward,
                no_rest_loss=no_rest_loss,
                no_fatigue_state_loss=no_fatigue_loss,
                no_day_night_state_loss=no_day_loss,
                no_shelter_memory_loss=no_shelter_loss,
                no_alarm_tools_loss=no_alarm_loss,
                no_social_watch_loss=no_social_loss,
                no_continuity_loss=no_continuity_loss,
                fixed_schedule_loss=fixed_loss,
                selected_sleep_ticks=full.mean_sleep_ticks,
                selected_unsafe_sleep_ticks=full.mean_unsafe_sleep_ticks,
                selected_shelter_sleep_ticks=full.mean_shelter_sleep_ticks,
                selected_alarm_uses=full.mean_alarm_uses,
                selected_social_watch_uses=full.mean_social_watch_uses,
                supports_day_night_sleep_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def build_trace(cfg: SleepConfig, selected: Dict[int, Policy]) -> Dict[str, object]:
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
            "mean_sleep_ticks": mean(row.sleep_ticks for row in rows),
            "mean_unsafe_sleep_ticks": mean(row.unsafe_sleep_ticks for row in rows),
            "mean_hazard_damage": mean(row.hazard_damage for row in rows),
        }
    return {
        "scenario": asdict(scenario),
        "policy": asdict(policy),
        "episode_result": asdict(result),
        "condition_outcomes": condition_outcomes,
        "frames": frames,
        "trace_note": "Sleep/rest is modeled as a vulnerable control action, not a subjective state.",
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
    cfg: SleepConfig,
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
        "artifact_note": "Day/night and sleep/rest are control variables, not organism roleplay.",
    }
    return eval_rows, selection_rows, summary_rows, verdict_rows, {"results": results, "trace": trace}


def print_table(verdicts: Sequence[VerdictRow]) -> None:
    headers = [
        "scenario",
        "policy",
        "rest_loss",
        "fatigue_loss",
        "day_loss",
        "shelter_loss",
        "supports",
    ]
    rows = [
        [
            row.scenario_name,
            row.selected_policy,
            f"{row.no_rest_loss:.3f}",
            f"{row.no_fatigue_state_loss:.3f}",
            f"{row.no_day_night_state_loss:.3f}",
            f"{row.no_shelter_memory_loss:.3f}",
            str(row.supports_day_night_sleep_precursor),
        ]
        for row in verdicts
    ]
    widths = [max(len(header), *(len(row[index]) for row in rows)) for index, header in enumerate(headers)]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> SleepConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-episodes", type=int, default=SleepConfig.train_episodes)
    parser.add_argument("--eval-episodes", type=int, default=SleepConfig.eval_episodes)
    parser.add_argument("--ticks", type=int, default=SleepConfig.ticks)
    parser.add_argument("--seed", type=int, default=SleepConfig.seed)
    parser.add_argument("--candidate-count", type=int, default=SleepConfig.candidate_count)
    parser.add_argument("--trace-scenario", type=int, default=SleepConfig.trace_scenario)
    parser.add_argument("--trace-episode", type=int, default=SleepConfig.trace_episode)
    args = parser.parse_args()
    if args.train_episodes < 24:
        raise SystemExit("--train-episodes must be at least 24")
    if args.eval_episodes < 24:
        raise SystemExit("--eval-episodes must be at least 24")
    if args.candidate_count < len(SEEDED_POLICIES):
        raise SystemExit(f"--candidate-count must be at least {len(SEEDED_POLICIES)}")
    if args.trace_scenario < 0 or args.trace_scenario >= len(SCENARIOS):
        raise SystemExit("--trace-scenario out of range")
    return SleepConfig(
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

    eval_path = ARTIFACT_DIR / "ssrm_3d_day_night_sleep_eval.csv"
    selection_path = ARTIFACT_DIR / "ssrm_3d_day_night_sleep_policy_selection.csv"
    summary_path = ARTIFACT_DIR / "ssrm_3d_day_night_sleep_summary.csv"
    verdict_path = ARTIFACT_DIR / "ssrm_3d_day_night_sleep_verdict.csv"
    results_path = ARTIFACT_DIR / "ssrm_3d_day_night_sleep_results.json"
    trace_path = ARTIFACT_DIR / "ssrm_3d_day_night_sleep_trace.json"
    results_js_path = ARTIFACT_DIR / "ssrm_3d_day_night_sleep_results.js"
    trace_js_path = ARTIFACT_DIR / "ssrm_3d_day_night_sleep_trace.js"

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
    write_js(results_js_path, "SSRM_3D_DAY_NIGHT_SLEEP_RESULTS", payload["results"])
    write_js(trace_js_path, "SSRM_3D_DAY_NIGHT_SLEEP_TRACE", payload["trace"])

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
    if not all(row.supports_day_night_sleep_precursor for row in verdict_rows):
        print("day/night sleep-rest precursor not supported by all verdict rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
