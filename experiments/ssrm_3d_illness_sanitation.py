#!/usr/bin/env python3
"""SSRM-3D hunger/thirst illness-sanitation precursor.

This experiment implements the third pressure-layer step from report 74:
hunger/thirst plus illness/sanitation. It is intentionally not a full biology
model. Hydration, food load, infection, contamination, care, quarantine, and
immunity are abstract control variables.

The result remains a designed precursor. It is useful only if health machinery
is rejected in the low-pressure control, selected under delayed internal risk,
and targeted ablations fail specifically rather than causing generic collapse.
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
class HealthConfig:
    train_episodes: int = 72
    eval_episodes: int = 96
    ticks: int = 220
    seed: int = 20260622
    candidate_count: int = 6
    trace_scenario: int = 3
    trace_episode: int = 0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    expected_need_pressure: bool
    expected_illness_pressure: bool
    expected_contamination_pressure: bool
    expected_sanitation_pressure: bool
    expected_clean_water_pressure: bool
    expected_care_pressure: bool
    expected_immunity_pressure: bool
    expected_continuity_pressure: bool
    initial_hydration: float
    initial_food: float
    hydration_loss: float
    food_loss: float
    exposure_pressure: float
    water_contamination: float
    food_spoilage: float
    shelter_contamination: float
    crowding: float
    immunity_start: float
    restore_tick: int
    required_progress: float
    work_rate: float
    helper_present: bool
    care_debt_pressure: float


@dataclass(frozen=True)
class Policy:
    name: str
    need_state: bool
    illness_state: bool
    contamination_map: bool
    sanitation_action: bool
    clean_water_tools: bool
    care_quarantine: bool
    immunity_memory: bool
    continuity_memory: bool
    rest_recovery: bool
    medicine_use: bool
    warning_signal: bool
    need_threshold: float
    symptom_threshold: float
    contamination_threshold: float
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
    final_hydration: float
    final_food: float
    pathogen_load: float
    symptom_severity: float
    immunity_level: float
    contamination_level: float
    social_trust: float
    collapse_risk: float
    water_actions: int
    food_actions: int
    clean_water_actions: int
    sanitation_actions: int
    rest_actions: int
    medicine_actions: int
    quarantine_actions: int
    care_actions: int
    warning_actions: int
    dirty_exposures: int
    contamination_reads: int
    illness_reads: int
    need_reads: int
    immunity_reads: int
    continuity_resets: int
    attribution_errors: int


@dataclass(frozen=True)
class PolicySelectionRow:
    scenario: int
    scenario_name: str
    selected_policy: str
    selected_uses_need_state: bool
    selected_uses_illness_state: bool
    selected_uses_contamination: bool
    selected_uses_sanitation: bool
    selected_uses_clean_water: bool
    selected_uses_care: bool
    selected_uses_immunity: bool
    selected_uses_continuity: bool
    train_reward: float
    no_health_train_reward: float
    train_gain_over_no_health: float


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
    mean_final_food: float
    mean_pathogen_load: float
    mean_symptom_severity: float
    mean_immunity_level: float
    mean_contamination_level: float
    mean_social_trust: float
    mean_collapse_risk: float
    mean_water_actions: float
    mean_food_actions: float
    mean_clean_water_actions: float
    mean_sanitation_actions: float
    mean_rest_actions: float
    mean_medicine_actions: float
    mean_quarantine_actions: float
    mean_care_actions: float
    mean_warning_actions: float
    mean_dirty_exposures: float
    mean_contamination_reads: float
    mean_illness_reads: float
    mean_need_reads: float
    mean_immunity_reads: float
    mean_continuity_resets: float
    mean_attribution_errors: float


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    expected_pressure: str
    selected_policy: str
    selected_reward: float
    no_health_state_reward: float
    no_hunger_thirst_state_reward: float
    no_illness_state_reward: float
    no_contamination_map_reward: float
    no_sanitation_action_reward: float
    no_clean_water_tools_reward: float
    no_care_quarantine_reward: float
    no_immunity_memory_reward: float
    no_continuity_reward: float
    symptom_reactive_only_reward: float
    omniscient_health_control_reward: float
    health_gain_over_no_health: float
    no_hunger_thirst_state_loss: float
    no_illness_state_loss: float
    no_contamination_map_loss: float
    no_sanitation_action_loss: float
    no_clean_water_tools_loss: float
    no_care_quarantine_loss: float
    no_immunity_memory_loss: float
    no_continuity_loss: float
    symptom_reactive_only_loss: float
    selected_dirty_exposures: float
    selected_sanitation_actions: float
    selected_quarantine_actions: float
    selected_care_actions: float
    selected_attribution_errors: float
    supports_illness_sanitation_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        index=0,
        name="clean_resource_control",
        pressure="clean resource collection with negligible health pressure",
        expected_need_pressure=False,
        expected_illness_pressure=False,
        expected_contamination_pressure=False,
        expected_sanitation_pressure=False,
        expected_clean_water_pressure=False,
        expected_care_pressure=False,
        expected_immunity_pressure=False,
        expected_continuity_pressure=False,
        initial_hydration=0.86,
        initial_food=0.86,
        hydration_loss=0.0010,
        food_loss=0.0008,
        exposure_pressure=0.00,
        water_contamination=0.00,
        food_spoilage=0.00,
        shelter_contamination=0.00,
        crowding=0.00,
        immunity_start=0.20,
        restore_tick=-1,
        required_progress=92.0,
        work_rate=0.61,
        helper_present=False,
        care_debt_pressure=0.0,
    ),
    ScenarioSpec(
        index=1,
        name="hunger_thirst_delayed_need",
        pressure="hydration and food load silently degrade future capability",
        expected_need_pressure=True,
        expected_illness_pressure=False,
        expected_contamination_pressure=False,
        expected_sanitation_pressure=False,
        expected_clean_water_pressure=False,
        expected_care_pressure=False,
        expected_immunity_pressure=False,
        expected_continuity_pressure=False,
        initial_hydration=0.58,
        initial_food=0.54,
        hydration_loss=0.0048,
        food_loss=0.0038,
        exposure_pressure=0.00,
        water_contamination=0.02,
        food_spoilage=0.01,
        shelter_contamination=0.00,
        crowding=0.00,
        immunity_start=0.25,
        restore_tick=-1,
        required_progress=68.0,
        work_rate=0.58,
        helper_present=False,
        care_debt_pressure=0.0,
    ),
    ScenarioSpec(
        index=2,
        name="latent_illness_attribution",
        pressure="performance drops from latent infection rather than terrain or tools",
        expected_need_pressure=True,
        expected_illness_pressure=True,
        expected_contamination_pressure=False,
        expected_sanitation_pressure=False,
        expected_clean_water_pressure=False,
        expected_care_pressure=False,
        expected_immunity_pressure=False,
        expected_continuity_pressure=False,
        initial_hydration=0.72,
        initial_food=0.70,
        hydration_loss=0.0030,
        food_loss=0.0024,
        exposure_pressure=0.34,
        water_contamination=0.00,
        food_spoilage=0.00,
        shelter_contamination=0.03,
        crowding=0.08,
        immunity_start=0.15,
        restore_tick=-1,
        required_progress=62.0,
        work_rate=0.55,
        helper_present=False,
        care_debt_pressure=0.0,
    ),
    ScenarioSpec(
        index=3,
        name="contaminated_shelter_water",
        pressure="dirty shelter and water make sanitation and clean-water tools useful",
        expected_need_pressure=True,
        expected_illness_pressure=True,
        expected_contamination_pressure=True,
        expected_sanitation_pressure=True,
        expected_clean_water_pressure=True,
        expected_care_pressure=False,
        expected_immunity_pressure=False,
        expected_continuity_pressure=False,
        initial_hydration=0.64,
        initial_food=0.68,
        hydration_loss=0.0040,
        food_loss=0.0028,
        exposure_pressure=0.20,
        water_contamination=0.64,
        food_spoilage=0.16,
        shelter_contamination=0.62,
        crowding=0.05,
        immunity_start=0.12,
        restore_tick=-1,
        required_progress=58.0,
        work_rate=0.54,
        helper_present=False,
        care_debt_pressure=0.0,
    ),
    ScenarioSpec(
        index=4,
        name="contagion_quarantine_care",
        pressure="sick agent can expose a helper unless it warns, quarantines, or seeks care",
        expected_need_pressure=True,
        expected_illness_pressure=True,
        expected_contamination_pressure=True,
        expected_sanitation_pressure=False,
        expected_clean_water_pressure=True,
        expected_care_pressure=True,
        expected_immunity_pressure=False,
        expected_continuity_pressure=False,
        initial_hydration=0.66,
        initial_food=0.68,
        hydration_loss=0.0038,
        food_loss=0.0028,
        exposure_pressure=0.42,
        water_contamination=0.28,
        food_spoilage=0.08,
        shelter_contamination=0.20,
        crowding=0.55,
        immunity_start=0.10,
        restore_tick=-1,
        required_progress=54.0,
        work_rate=0.53,
        helper_present=True,
        care_debt_pressure=1.0,
    ),
    ScenarioSpec(
        index=5,
        name="immunity_restore_continuity",
        pressure="after restore, immunity and exposure history prevent repeated illness errors",
        expected_need_pressure=True,
        expected_illness_pressure=True,
        expected_contamination_pressure=True,
        expected_sanitation_pressure=True,
        expected_clean_water_pressure=True,
        expected_care_pressure=False,
        expected_immunity_pressure=True,
        expected_continuity_pressure=True,
        initial_hydration=0.64,
        initial_food=0.68,
        hydration_loss=0.0038,
        food_loss=0.0026,
        exposure_pressure=0.30,
        water_contamination=0.52,
        food_spoilage=0.12,
        shelter_contamination=0.48,
        crowding=0.08,
        immunity_start=0.64,
        restore_tick=104,
        required_progress=60.0,
        work_rate=0.54,
        helper_present=False,
        care_debt_pressure=0.0,
    ),
)


SEEDED_POLICIES = (
    Policy(
        name="no_health_baseline",
        need_state=False,
        illness_state=False,
        contamination_map=False,
        sanitation_action=False,
        clean_water_tools=False,
        care_quarantine=False,
        immunity_memory=False,
        continuity_memory=False,
        rest_recovery=False,
        medicine_use=False,
        warning_signal=False,
        need_threshold=0.36,
        symptom_threshold=0.48,
        contamination_threshold=0.46,
        risk_tolerance=0.68,
        tool_cost_tolerance=0.0,
    ),
    Policy(
        name="need_reactive_forager",
        need_state=True,
        illness_state=False,
        contamination_map=False,
        sanitation_action=False,
        clean_water_tools=False,
        care_quarantine=False,
        immunity_memory=False,
        continuity_memory=False,
        rest_recovery=False,
        medicine_use=False,
        warning_signal=False,
        need_threshold=0.52,
        symptom_threshold=0.48,
        contamination_threshold=0.46,
        risk_tolerance=0.62,
        tool_cost_tolerance=0.0,
    ),
    Policy(
        name="illness_recovery_planner",
        need_state=True,
        illness_state=True,
        contamination_map=False,
        sanitation_action=False,
        clean_water_tools=False,
        care_quarantine=False,
        immunity_memory=False,
        continuity_memory=False,
        rest_recovery=True,
        medicine_use=True,
        warning_signal=False,
        need_threshold=0.55,
        symptom_threshold=0.24,
        contamination_threshold=0.44,
        risk_tolerance=0.42,
        tool_cost_tolerance=0.10,
    ),
    Policy(
        name="sanitation_mapper",
        need_state=True,
        illness_state=True,
        contamination_map=True,
        sanitation_action=True,
        clean_water_tools=True,
        care_quarantine=False,
        immunity_memory=False,
        continuity_memory=True,
        rest_recovery=True,
        medicine_use=True,
        warning_signal=False,
        need_threshold=0.56,
        symptom_threshold=0.22,
        contamination_threshold=0.30,
        risk_tolerance=0.34,
        tool_cost_tolerance=0.68,
    ),
    Policy(
        name="quarantine_care_planner",
        need_state=True,
        illness_state=True,
        contamination_map=True,
        sanitation_action=True,
        clean_water_tools=True,
        care_quarantine=True,
        immunity_memory=False,
        continuity_memory=True,
        rest_recovery=True,
        medicine_use=True,
        warning_signal=True,
        need_threshold=0.56,
        symptom_threshold=0.20,
        contamination_threshold=0.30,
        risk_tolerance=0.26,
        tool_cost_tolerance=0.76,
    ),
    Policy(
        name="immunity_continuity_planner",
        need_state=True,
        illness_state=True,
        contamination_map=True,
        sanitation_action=True,
        clean_water_tools=True,
        care_quarantine=False,
        immunity_memory=True,
        continuity_memory=True,
        rest_recovery=True,
        medicine_use=True,
        warning_signal=False,
        need_threshold=0.56,
        symptom_threshold=0.20,
        contamination_threshold=0.28,
        risk_tolerance=0.24,
        tool_cost_tolerance=0.78,
    ),
)


CONDITIONS = (
    "full_control",
    "no_health_state",
    "no_hunger_thirst_state",
    "no_illness_state",
    "no_contamination_map",
    "no_sanitation_action",
    "no_clean_water_tools",
    "no_care_quarantine",
    "no_immunity_memory",
    "no_continuity",
    "symptom_reactive_only",
    "omniscient_health_control",
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


def build_policies(cfg: HealthConfig) -> List[Policy]:
    policies = list(SEEDED_POLICIES)
    rng = random.Random(cfg.seed + 991)
    while len(policies) < cfg.candidate_count:
        base = rng.choice(SEEDED_POLICIES[1:])
        policies.append(
            Policy(
                name=f"mutant_health_{len(policies)}",
                need_state=base.need_state if rng.random() > 0.15 else not base.need_state,
                illness_state=base.illness_state if rng.random() > 0.15 else not base.illness_state,
                contamination_map=base.contamination_map if rng.random() > 0.18 else not base.contamination_map,
                sanitation_action=base.sanitation_action if rng.random() > 0.18 else not base.sanitation_action,
                clean_water_tools=base.clean_water_tools if rng.random() > 0.18 else not base.clean_water_tools,
                care_quarantine=base.care_quarantine if rng.random() > 0.20 else not base.care_quarantine,
                immunity_memory=base.immunity_memory if rng.random() > 0.20 else not base.immunity_memory,
                continuity_memory=base.continuity_memory if rng.random() > 0.14 else not base.continuity_memory,
                rest_recovery=base.rest_recovery if rng.random() > 0.16 else not base.rest_recovery,
                medicine_use=base.medicine_use if rng.random() > 0.16 else not base.medicine_use,
                warning_signal=base.warning_signal if rng.random() > 0.20 else not base.warning_signal,
                need_threshold=clamp(base.need_threshold + rng.uniform(-0.06, 0.06), 0.42, 0.68),
                symptom_threshold=clamp(base.symptom_threshold + rng.uniform(-0.06, 0.06), 0.14, 0.56),
                contamination_threshold=clamp(base.contamination_threshold + rng.uniform(-0.08, 0.08), 0.20, 0.60),
                risk_tolerance=clamp(base.risk_tolerance + rng.uniform(-0.08, 0.08), 0.14, 0.78),
                tool_cost_tolerance=clamp(base.tool_cost_tolerance + rng.uniform(-0.10, 0.10), 0.0, 1.0),
            )
        )
    return policies


def condition_policy(policy: Policy, condition: str) -> Policy:
    if condition == "omniscient_health_control":
        return Policy(
            name=policy.name,
            need_state=True,
            illness_state=True,
            contamination_map=True,
            sanitation_action=True,
            clean_water_tools=True,
            care_quarantine=True,
            immunity_memory=True,
            continuity_memory=True,
            rest_recovery=True,
            medicine_use=True,
            warning_signal=True,
            need_threshold=min(policy.need_threshold, 0.54),
            symptom_threshold=min(policy.symptom_threshold, 0.18),
            contamination_threshold=min(policy.contamination_threshold, 0.26),
            risk_tolerance=0.10,
            tool_cost_tolerance=1.0,
        )
    if condition == "symptom_reactive_only":
        return Policy(
            name=policy.name,
            need_state=False,
            illness_state=True,
            contamination_map=False,
            sanitation_action=False,
            clean_water_tools=False,
            care_quarantine=False,
            immunity_memory=False,
            continuity_memory=policy.continuity_memory,
            rest_recovery=True,
            medicine_use=policy.medicine_use,
            warning_signal=False,
            need_threshold=0.34,
            symptom_threshold=0.52,
            contamination_threshold=0.60,
            risk_tolerance=policy.risk_tolerance,
            tool_cost_tolerance=0.0,
        )
    health_enabled = condition != "no_health_state"
    return Policy(
        name=policy.name,
        need_state=policy.need_state and health_enabled and condition != "no_hunger_thirst_state",
        illness_state=policy.illness_state and health_enabled and condition != "no_illness_state",
        contamination_map=policy.contamination_map and health_enabled and condition != "no_contamination_map",
        sanitation_action=policy.sanitation_action and health_enabled and condition != "no_sanitation_action",
        clean_water_tools=policy.clean_water_tools and health_enabled and condition != "no_clean_water_tools",
        care_quarantine=policy.care_quarantine and health_enabled and condition != "no_care_quarantine",
        immunity_memory=policy.immunity_memory and health_enabled and condition != "no_immunity_memory",
        continuity_memory=policy.continuity_memory and health_enabled and condition != "no_continuity",
        rest_recovery=policy.rest_recovery and health_enabled,
        medicine_use=policy.medicine_use and health_enabled and condition != "no_illness_state",
        warning_signal=policy.warning_signal and health_enabled and condition != "no_care_quarantine",
        need_threshold=policy.need_threshold,
        symptom_threshold=policy.symptom_threshold,
        contamination_threshold=policy.contamination_threshold,
        risk_tolerance=policy.risk_tolerance,
        tool_cost_tolerance=policy.tool_cost_tolerance,
    )


def scenario_seed(cfg: HealthConfig, scenario: ScenarioSpec, policy: Policy, condition: str, episode: int, phase: str) -> int:
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
        (policy.need_state, 0.55),
        (policy.illness_state, 0.55),
        (policy.contamination_map, 0.75),
        (policy.sanitation_action, 0.55),
        (policy.clean_water_tools, 0.55),
        (policy.care_quarantine, 0.65),
        (policy.immunity_memory, 2.00),
        (policy.continuity_memory, 0.90),
        (policy.rest_recovery, 0.40),
        (policy.medicine_use, 0.40),
        (policy.warning_signal, 0.40),
    ]
    return sum(weight for enabled, weight in weighted_flags if enabled)


def illness_pressure(scenario: ScenarioSpec, contamination: float, crowding_exposure: float) -> float:
    return scenario.exposure_pressure + scenario.water_contamination * 0.45 + contamination * 0.38 + crowding_exposure


def choose_action(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    tick: int,
    hydration: float,
    food: float,
    pathogen: float,
    symptoms: float,
    contamination: float,
    immunity: float,
    quarantine_active: bool,
    rng: random.Random,
) -> str:
    observed_hydration = hydration if policy.need_state else 0.66 + rng.uniform(-0.03, 0.03)
    observed_food = food if policy.need_state else 0.66 + rng.uniform(-0.03, 0.03)
    if policy.illness_state:
        observed_symptoms = symptoms
        observed_pathogen = pathogen
    else:
        observed_symptoms = 0.18 + rng.uniform(-0.03, 0.03)
        observed_pathogen = 0.12
    if condition == "symptom_reactive_only":
        observed_symptoms = symptoms if symptoms > 0.46 else 0.12
        observed_pathogen = pathogen if symptoms > 0.46 else 0.10
    observed_contamination = contamination if policy.contamination_map else 0.18 + rng.uniform(-0.03, 0.03)
    immune_credit = immunity if policy.immunity_memory else 0.12

    if (
        policy.contamination_map
        and policy.sanitation_action
        and observed_contamination > policy.contamination_threshold
        and policy.tool_cost_tolerance > 0.30
    ):
        return "clean_shelter"
    if (
        policy.illness_state
        and policy.care_quarantine
        and scenario.helper_present
        and not quarantine_active
        and observed_pathogen > 0.22
        and observed_symptoms > policy.symptom_threshold * 0.70
    ):
        return "quarantine_warn"
    if (
        policy.clean_water_tools
        and observed_hydration < policy.need_threshold + 0.10
        and (observed_contamination > 0.25 or scenario.water_contamination > 0.18)
        and policy.tool_cost_tolerance > 0.20
    ):
        return "seek_clean_water"
    if observed_hydration < policy.need_threshold:
        return "seek_water"
    if observed_food < policy.need_threshold - 0.04:
        return "seek_food"
    if (
        policy.illness_state
        and policy.medicine_use
        and observed_pathogen > 0.28
        and observed_symptoms > policy.symptom_threshold
        and immune_credit < 0.82
    ):
        return "medicine"
    if (
        policy.illness_state
        and policy.rest_recovery
        and observed_symptoms > policy.symptom_threshold + 0.08
        and observed_hydration > 0.34
        and observed_food > 0.30
    ):
        return "rest"
    if (
        scenario.helper_present
        and policy.care_quarantine
        and observed_pathogen < 0.25
        and observed_hydration > 0.44
        and observed_food > 0.42
        and rng.random() < 0.020 + scenario.care_debt_pressure * 0.020
    ):
        return "care_for_helper"
    return "work"


def simulate_episode(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episode: int,
    cfg: HealthConfig,
    phase: str,
    collect_trace: bool = False,
) -> Tuple[EpisodeResult, List[Dict[str, object]]]:
    effective = condition_policy(policy, condition)
    rng = random.Random(scenario_seed(cfg, scenario, policy, condition, episode, phase))
    hydration = clamp(scenario.initial_hydration + rng.uniform(-0.025, 0.025), 0.0, 1.0)
    food = clamp(scenario.initial_food + rng.uniform(-0.025, 0.025), 0.0, 1.0)
    contamination = clamp(scenario.shelter_contamination + rng.uniform(-0.025, 0.025), 0.0, 1.0)
    pathogen = clamp(scenario.exposure_pressure * (1.0 - scenario.immunity_start) * 0.24 + rng.uniform(0.0, 0.015), 0.0, 1.0)
    symptoms = 0.0
    immunity = scenario.immunity_start
    social_trust = 0.72 if scenario.helper_present else 0.0
    progress = 0.0
    collapse_risk = 0.0
    quarantine_active = False
    known_exposure = scenario.exposure_pressure > 0.0
    collapsed = False

    water_actions = 0
    food_actions = 0
    clean_water_actions = 0
    sanitation_actions = 0
    rest_actions = 0
    medicine_actions = 0
    quarantine_actions = 0
    care_actions = 0
    warning_actions = 0
    dirty_exposures = 0
    contamination_reads = 0
    illness_reads = 0
    need_reads = 0
    immunity_reads = 0
    continuity_resets = 0
    attribution_errors = 0
    trace_frames: List[Dict[str, object]] = []

    for tick in range(cfg.ticks):
        if scenario.restore_tick == tick and not effective.continuity_memory:
            known_exposure = False
            quarantine_active = False
            continuity_resets += 1
            if not effective.contamination_map:
                contamination = max(contamination, scenario.shelter_contamination)
        if scenario.restore_tick == tick and not effective.immunity_memory:
            immunity = min(immunity, 0.08)
            pathogen = clamp(pathogen + scenario.exposure_pressure * 1.10 + scenario.water_contamination * 0.32, 0.0, 1.0)
            symptoms = clamp(symptoms + 0.18, 0.0, 1.0)

        if collapsed:
            action = "collapsed"
        else:
            if effective.need_state:
                need_reads += 1
            if effective.illness_state:
                illness_reads += 1
            if effective.contamination_map:
                contamination_reads += 1
            if effective.immunity_memory:
                immunity_reads += 1
            action = choose_action(
                scenario,
                effective,
                condition,
                tick,
                hydration,
                food,
                pathogen,
                symptoms,
                contamination,
                immunity,
                quarantine_active,
                rng,
            )

            hydration = clamp(hydration - scenario.hydration_loss - symptoms * 0.0018, 0.0, 1.0)
            food = clamp(food - scenario.food_loss - symptoms * 0.0008, 0.0, 1.0)
            crowding_exposure = scenario.crowding * (0.018 if not quarantine_active else 0.004)
            exposure = illness_pressure(scenario, contamination, crowding_exposure) * (1.0 - immunity * 0.72)

            if action == "seek_clean_water":
                clean_water_actions += 1
                hydration = clamp(hydration + 0.105, 0.0, 1.0)
                food = clamp(food - 0.002, 0.0, 1.0)
                progress += scenario.work_rate * 0.10
                pathogen = clamp(pathogen + max(0.0, scenario.water_contamination - 0.40) * 0.004, 0.0, 1.0)
            elif action == "seek_water":
                water_actions += 1
                hydration = clamp(hydration + 0.120, 0.0, 1.0)
                dirty_exposures += 1 if scenario.water_contamination > 0.12 or contamination > 0.24 else 0
                pathogen = clamp(pathogen + scenario.water_contamination * 0.045 + contamination * 0.016, 0.0, 1.0)
                progress += scenario.work_rate * 0.08
            elif action == "seek_food":
                food_actions += 1
                food = clamp(food + 0.115, 0.0, 1.0)
                dirty_exposures += 1 if scenario.food_spoilage > 0.12 else 0
                pathogen = clamp(pathogen + scenario.food_spoilage * 0.020, 0.0, 1.0)
                progress += scenario.work_rate * 0.08
            elif action == "clean_shelter":
                sanitation_actions += 1
                contamination = clamp(contamination - 0.085, 0.0, 1.0)
                hydration = clamp(hydration - 0.006, 0.0, 1.0)
                food = clamp(food - 0.004, 0.0, 1.0)
                progress -= 0.10
            elif action == "quarantine_warn":
                quarantine_actions += 1
                warning_actions += 1 if effective.warning_signal else 0
                quarantine_active = True
                social_trust = clamp(social_trust + 0.055, 0.0, 1.0)
                hydration = clamp(hydration - 0.004, 0.0, 1.0)
                food = clamp(food - 0.004, 0.0, 1.0)
                progress -= 0.20
            elif action == "care_for_helper":
                care_actions += 1
                social_trust = clamp(social_trust + 0.040, 0.0, 1.0)
                hydration = clamp(hydration - 0.006, 0.0, 1.0)
                food = clamp(food - 0.006, 0.0, 1.0)
                progress -= 0.24
            elif action == "medicine":
                medicine_actions += 1
                pathogen = clamp(pathogen - 0.035, 0.0, 1.0)
                symptoms = clamp(symptoms - 0.025, 0.0, 1.0)
                hydration = clamp(hydration - 0.006, 0.0, 1.0)
                progress -= 0.18
            elif action == "rest":
                rest_actions += 1
                pathogen = clamp(pathogen - 0.010 - immunity * 0.004, 0.0, 1.0)
                symptoms = clamp(symptoms - 0.035, 0.0, 1.0)
                hydration = clamp(hydration - 0.005, 0.0, 1.0)
                food = clamp(food - 0.003, 0.0, 1.0)
            else:
                need_penalty = max(0.0, 0.42 - hydration) * 1.35 + max(0.0, 0.38 - food) * 1.10
                symptom_penalty = symptoms * 0.82
                capability = clamp(1.0 - need_penalty - symptom_penalty, 0.05, 1.0)
                progress += scenario.work_rate * capability
                pathogen = clamp(pathogen + exposure * 0.012, 0.0, 1.0)

            if pathogen > 0.10:
                known_exposure = True
            symptoms = clamp(symptoms + max(0.0, pathogen - 0.12) * 0.020 - immunity * 0.003, 0.0, 1.0)
            immunity = clamp(immunity + max(0.0, pathogen - 0.20) * 0.006 - 0.0004, 0.0, 1.0)
            contamination = clamp(contamination + scenario.shelter_contamination * 0.0015 - (0.001 if sanitation_actions else 0.0), 0.0, 1.0)

            if scenario.helper_present and pathogen > 0.25 and not quarantine_active:
                social_trust = clamp(social_trust - 0.0065 - scenario.care_debt_pressure * 0.0025, 0.0, 1.0)
                dirty_exposures += 1 if tick % 7 == 0 else 0
            if scenario.helper_present and pathogen > 0.30 and not effective.care_quarantine:
                attribution_errors += 1 if tick % 11 == 0 else 0

            if (symptoms > 0.30 or pathogen > 0.34) and not effective.illness_state:
                attribution_errors += 1 if tick % 9 == 0 else 0
            if contamination > 0.34 and not effective.contamination_map:
                attribution_errors += 1 if tick % 13 == 0 else 0
            if hydration < 0.30 and not effective.need_state:
                attribution_errors += 1 if tick % 8 == 0 else 0

            collapse_risk = max(
                collapse_risk,
                max(0.0, 0.24 - hydration) * 1.35
                + max(0.0, 0.22 - food) * 1.05
                + max(0.0, symptoms - 0.72) * 0.90
                + max(0.0, pathogen - 0.78) * 0.70,
            )
            if collapse_risk >= 1.0:
                collapsed = True

        if collect_trace and (tick % 5 == 0 or tick == cfg.ticks - 1):
            trace_frames.append(
                {
                    "tick": tick,
                    "action": action,
                    "hydration": round(hydration, 3),
                    "food": round(food, 3),
                    "pathogen_load": round(pathogen, 3),
                    "symptom_severity": round(symptoms, 3),
                    "immunity_level": round(immunity, 3),
                    "contamination_level": round(contamination, 3),
                    "social_trust": round(social_trust, 3),
                    "progress": round(progress, 3),
                    "collapse_risk": round(collapse_risk, 3),
                    "quarantine_active": quarantine_active,
                    "known_exposure": known_exposure,
                    "continuity_resets": continuity_resets,
                    "dirty_exposures": dirty_exposures,
                }
            )

    task_success = progress >= scenario.required_progress and not collapsed
    survival = 1.0 if not collapsed and collapse_risk < 0.88 else 0.0

    reward = progress
    reward += 34.0 if task_success else -20.0
    reward += 36.0 if survival else -96.0
    reward += hydration * 12.0 + food * 10.0
    reward += immunity * (10.0 if scenario.expected_immunity_pressure else 2.0)
    reward -= pathogen * 42.0
    reward -= symptoms * 70.0
    reward -= contamination * (28.0 if scenario.expected_contamination_pressure else 5.0)
    reward -= collapse_risk * 74.0
    reward -= dirty_exposures * (2.0 if scenario.expected_contamination_pressure or scenario.expected_care_pressure else 0.25)
    reward -= attribution_errors * 0.65
    reward -= sanitation_actions * 0.20
    reward -= clean_water_actions * 0.18
    reward -= quarantine_actions * 0.35
    reward -= care_actions * 0.35
    reward -= feature_overhead(effective)
    if scenario.helper_present:
        reward += social_trust * 36.0
        reward -= max(0.0, 0.62 - social_trust) * 48.0
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
        final_hydration=hydration,
        final_food=food,
        pathogen_load=pathogen,
        symptom_severity=symptoms,
        immunity_level=immunity,
        contamination_level=contamination,
        social_trust=social_trust,
        collapse_risk=collapse_risk,
        water_actions=water_actions,
        food_actions=food_actions,
        clean_water_actions=clean_water_actions,
        sanitation_actions=sanitation_actions,
        rest_actions=rest_actions,
        medicine_actions=medicine_actions,
        quarantine_actions=quarantine_actions,
        care_actions=care_actions,
        warning_actions=warning_actions,
        dirty_exposures=dirty_exposures,
        contamination_reads=contamination_reads,
        illness_reads=illness_reads,
        need_reads=need_reads,
        immunity_reads=immunity_reads,
        continuity_resets=continuity_resets,
        attribution_errors=attribution_errors,
    )
    return result, trace_frames


def evaluate_policy(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episodes: int,
    cfg: HealthConfig,
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
                    mean_final_food=mean(row.final_food for row in subset),
                    mean_pathogen_load=mean(row.pathogen_load for row in subset),
                    mean_symptom_severity=mean(row.symptom_severity for row in subset),
                    mean_immunity_level=mean(row.immunity_level for row in subset),
                    mean_contamination_level=mean(row.contamination_level for row in subset),
                    mean_social_trust=mean(row.social_trust for row in subset),
                    mean_collapse_risk=mean(row.collapse_risk for row in subset),
                    mean_water_actions=mean(row.water_actions for row in subset),
                    mean_food_actions=mean(row.food_actions for row in subset),
                    mean_clean_water_actions=mean(row.clean_water_actions for row in subset),
                    mean_sanitation_actions=mean(row.sanitation_actions for row in subset),
                    mean_rest_actions=mean(row.rest_actions for row in subset),
                    mean_medicine_actions=mean(row.medicine_actions for row in subset),
                    mean_quarantine_actions=mean(row.quarantine_actions for row in subset),
                    mean_care_actions=mean(row.care_actions for row in subset),
                    mean_warning_actions=mean(row.warning_actions for row in subset),
                    mean_dirty_exposures=mean(row.dirty_exposures for row in subset),
                    mean_contamination_reads=mean(row.contamination_reads for row in subset),
                    mean_illness_reads=mean(row.illness_reads for row in subset),
                    mean_need_reads=mean(row.need_reads for row in subset),
                    mean_immunity_reads=mean(row.immunity_reads for row in subset),
                    mean_continuity_resets=mean(row.continuity_resets for row in subset),
                    mean_attribution_errors=mean(row.attribution_errors for row in subset),
                )
            )
    return rows


def select_policies(cfg: HealthConfig, policies: Sequence[Policy]) -> Tuple[Dict[int, Policy], List[PolicySelectionRow]]:
    selected: Dict[int, Policy] = {}
    rows: List[PolicySelectionRow] = []
    baseline = next(policy for policy in policies if policy.name == "no_health_baseline")
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
                selected_uses_need_state=selected_policy.need_state,
                selected_uses_illness_state=selected_policy.illness_state,
                selected_uses_contamination=selected_policy.contamination_map,
                selected_uses_sanitation=selected_policy.sanitation_action,
                selected_uses_clean_water=selected_policy.clean_water_tools,
                selected_uses_care=selected_policy.care_quarantine,
                selected_uses_immunity=selected_policy.immunity_memory,
                selected_uses_continuity=selected_policy.continuity_memory,
                train_reward=selected_reward,
                no_health_train_reward=baseline_reward,
                train_gain_over_no_health=selected_reward - baseline_reward,
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
        no_health = lookup[(scenario.index, "no_health_state")]
        no_need = lookup[(scenario.index, "no_hunger_thirst_state")]
        no_illness = lookup[(scenario.index, "no_illness_state")]
        no_contam = lookup[(scenario.index, "no_contamination_map")]
        no_sanitation = lookup[(scenario.index, "no_sanitation_action")]
        no_clean = lookup[(scenario.index, "no_clean_water_tools")]
        no_care = lookup[(scenario.index, "no_care_quarantine")]
        no_immunity = lookup[(scenario.index, "no_immunity_memory")]
        no_continuity = lookup[(scenario.index, "no_continuity")]
        symptom_only = lookup[(scenario.index, "symptom_reactive_only")]
        omniscient = lookup[(scenario.index, "omniscient_health_control")]

        no_need_loss = full.mean_reward - no_need.mean_reward
        no_illness_loss = full.mean_reward - no_illness.mean_reward
        no_contam_loss = full.mean_reward - no_contam.mean_reward
        no_sanitation_loss = full.mean_reward - no_sanitation.mean_reward
        no_clean_loss = full.mean_reward - no_clean.mean_reward
        no_care_loss = full.mean_reward - no_care.mean_reward
        no_immunity_loss = full.mean_reward - no_immunity.mean_reward
        no_continuity_loss = full.mean_reward - no_continuity.mean_reward
        symptom_loss = full.mean_reward - symptom_only.mean_reward

        if scenario.index == 0:
            supports = (
                selected[scenario.index].name == "no_health_baseline"
                and abs(full.mean_reward - no_health.mean_reward) < 4.0
                and no_need_loss < 4.0
                and no_illness_loss < 4.0
                and full.mean_dirty_exposures < 1.0
            )
            verdict = "health_machinery_rejected_in_clean_control"
        elif scenario.index == 1:
            supports = no_need_loss > 34.0 and no_illness_loss < 8.0 and full.mean_water_actions + full.mean_food_actions > 10.0
            verdict = "hunger_thirst_need_state_pressure"
        elif scenario.index == 2:
            supports = no_illness_loss > 28.0 and symptom_loss > 16.0 and full.mean_attribution_errors < no_illness.mean_attribution_errors
            verdict = "latent_illness_attribution_pressure"
        elif scenario.index == 3:
            supports = no_contam_loss > 22.0 and no_sanitation_loss > 18.0 and no_clean_loss > 16.0 and full.mean_sanitation_actions > 2.0
            verdict = "contamination_sanitation_clean_water_pressure"
        elif scenario.index == 4:
            supports = no_care_loss > 20.0 and full.mean_quarantine_actions > 0.5 and full.mean_social_trust > no_care.mean_social_trust
            verdict = "contagion_quarantine_care_pressure"
        else:
            supports = no_immunity_loss > 20.0 and no_continuity_loss > 22.0 and no_contam_loss > 14.0
            verdict = "immunity_exposure_continuity_pressure"

        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                expected_pressure=scenario.pressure,
                selected_policy=selected[scenario.index].name,
                selected_reward=full.mean_reward,
                no_health_state_reward=no_health.mean_reward,
                no_hunger_thirst_state_reward=no_need.mean_reward,
                no_illness_state_reward=no_illness.mean_reward,
                no_contamination_map_reward=no_contam.mean_reward,
                no_sanitation_action_reward=no_sanitation.mean_reward,
                no_clean_water_tools_reward=no_clean.mean_reward,
                no_care_quarantine_reward=no_care.mean_reward,
                no_immunity_memory_reward=no_immunity.mean_reward,
                no_continuity_reward=no_continuity.mean_reward,
                symptom_reactive_only_reward=symptom_only.mean_reward,
                omniscient_health_control_reward=omniscient.mean_reward,
                health_gain_over_no_health=full.mean_reward - no_health.mean_reward,
                no_hunger_thirst_state_loss=no_need_loss,
                no_illness_state_loss=no_illness_loss,
                no_contamination_map_loss=no_contam_loss,
                no_sanitation_action_loss=no_sanitation_loss,
                no_clean_water_tools_loss=no_clean_loss,
                no_care_quarantine_loss=no_care_loss,
                no_immunity_memory_loss=no_immunity_loss,
                no_continuity_loss=no_continuity_loss,
                symptom_reactive_only_loss=symptom_loss,
                selected_dirty_exposures=full.mean_dirty_exposures,
                selected_sanitation_actions=full.mean_sanitation_actions,
                selected_quarantine_actions=full.mean_quarantine_actions,
                selected_care_actions=full.mean_care_actions,
                selected_attribution_errors=full.mean_attribution_errors,
                supports_illness_sanitation_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def build_trace(cfg: HealthConfig, selected: Dict[int, Policy]) -> Dict[str, object]:
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
            "mean_pathogen_load": mean(row.pathogen_load for row in rows),
            "mean_symptom_severity": mean(row.symptom_severity for row in rows),
            "mean_contamination_level": mean(row.contamination_level for row in rows),
            "mean_social_trust": mean(row.social_trust for row in rows),
        }
    return {
        "scenario": asdict(scenario),
        "policy": asdict(policy),
        "episode_result": asdict(result),
        "condition_outcomes": condition_outcomes,
        "frames": frames,
        "trace_note": "Illness, hydration, food load, sanitation, and care are abstract control variables.",
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
    cfg: HealthConfig,
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
        "artifact_note": "Hunger/thirst and illness/sanitation are control variables, not organism roleplay.",
    }
    return eval_rows, selection_rows, summary_rows, verdict_rows, {"results": results, "trace": trace}


def print_table(verdicts: Sequence[VerdictRow]) -> None:
    headers = [
        "scenario",
        "policy",
        "need_loss",
        "illness_loss",
        "contam_loss",
        "care_loss",
        "supports",
    ]
    rows = [
        [
            row.scenario_name,
            row.selected_policy,
            f"{row.no_hunger_thirst_state_loss:.3f}",
            f"{row.no_illness_state_loss:.3f}",
            f"{row.no_contamination_map_loss:.3f}",
            f"{row.no_care_quarantine_loss:.3f}",
            str(row.supports_illness_sanitation_precursor),
        ]
        for row in verdicts
    ]
    widths = [max(len(header), *(len(row[index]) for row in rows)) for index, header in enumerate(headers)]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> HealthConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-episodes", type=int, default=HealthConfig.train_episodes)
    parser.add_argument("--eval-episodes", type=int, default=HealthConfig.eval_episodes)
    parser.add_argument("--ticks", type=int, default=HealthConfig.ticks)
    parser.add_argument("--seed", type=int, default=HealthConfig.seed)
    parser.add_argument("--candidate-count", type=int, default=HealthConfig.candidate_count)
    parser.add_argument("--trace-scenario", type=int, default=HealthConfig.trace_scenario)
    parser.add_argument("--trace-episode", type=int, default=HealthConfig.trace_episode)
    args = parser.parse_args()
    if args.train_episodes < 24:
        raise SystemExit("--train-episodes must be at least 24")
    if args.eval_episodes < 24:
        raise SystemExit("--eval-episodes must be at least 24")
    if args.candidate_count < len(SEEDED_POLICIES):
        raise SystemExit(f"--candidate-count must be at least {len(SEEDED_POLICIES)}")
    if args.trace_scenario < 0 or args.trace_scenario >= len(SCENARIOS):
        raise SystemExit("--trace-scenario out of range")
    return HealthConfig(
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

    eval_path = ARTIFACT_DIR / "ssrm_3d_illness_sanitation_eval.csv"
    selection_path = ARTIFACT_DIR / "ssrm_3d_illness_sanitation_policy_selection.csv"
    summary_path = ARTIFACT_DIR / "ssrm_3d_illness_sanitation_summary.csv"
    verdict_path = ARTIFACT_DIR / "ssrm_3d_illness_sanitation_verdict.csv"
    results_path = ARTIFACT_DIR / "ssrm_3d_illness_sanitation_results.json"
    trace_path = ARTIFACT_DIR / "ssrm_3d_illness_sanitation_trace.json"
    results_js_path = ARTIFACT_DIR / "ssrm_3d_illness_sanitation_results.js"
    trace_js_path = ARTIFACT_DIR / "ssrm_3d_illness_sanitation_trace.js"

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
    write_js(results_js_path, "SSRM_3D_ILLNESS_SANITATION_RESULTS", payload["results"])
    write_js(trace_js_path, "SSRM_3D_ILLNESS_SANITATION_TRACE", payload["trace"])

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
    if not all(row.supports_illness_sanitation_precursor for row in verdict_rows):
        print("illness/sanitation precursor not supported by all verdict rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
