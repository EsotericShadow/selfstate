#!/usr/bin/env python3
"""SSRM-3D development/skill-learning precursor.

This experiment implements the tenth pressure-layer step from report 74:
development and skill learning. It is intentionally not growth simulation.

Practice curves, fatigue degradation, injury retraining, transfer, teaching,
training tools, goal feasibility, and continuity are treated as abstract control
variables. The useful result is narrow: skill machinery should be rejected in an
easy fixed-skill control, then become useful only when changing competence
alters future action feasibility.
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
class SkillConfig:
    train_episodes: int = 72
    eval_episodes: int = 96
    ticks: int = 210
    seed: int = 20260629
    candidate_count: int = 7
    trace_scenario: int = 4
    trace_episode: int = 0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    expected_skill_memory: bool
    expected_practice_planning: bool
    expected_capability_state: bool
    expected_fatigue_management: bool
    expected_injury_adaptation: bool
    expected_transfer_model: bool
    expected_teaching_help: bool
    expected_tool_training: bool
    expected_goal_feasibility: bool
    expected_continuity: bool
    difficulty: float
    practice_opportunity: float
    fatigue_pressure: float
    injury_pressure: float
    transfer_pressure: float
    teaching_pressure: float
    tool_value: float
    required_progress: float
    work_rate: float
    restore_tick: int


@dataclass(frozen=True)
class Policy:
    name: str
    skill_memory: bool
    practice_planning: bool
    capability_state: bool
    fatigue_management: bool
    injury_adaptation: bool
    transfer_model: bool
    teaching_help: bool
    tool_training: bool
    goal_feasibility: bool
    continuity_memory: bool
    risk_threshold: float
    practice_bias: float
    teaching_bias: float
    tool_bias: float


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
    skill_level: float
    practice_history: float
    fatigue: float
    injury_load: float
    transfer_confidence: float
    teaching_support: float
    tool_support: float
    feasibility: float
    overreach_events: int
    failure_events: int
    practice_actions: int
    rest_actions: int
    retrain_actions: int
    teaching_actions: int
    tool_actions: int
    replan_actions: int
    continuity_resets: int
    skill_misses: int


@dataclass(frozen=True)
class PolicySelectionRow:
    scenario: int
    scenario_name: str
    selected_policy: str
    selected_uses_skill_memory: bool
    selected_uses_practice_planning: bool
    selected_uses_capability_state: bool
    selected_uses_fatigue_management: bool
    selected_uses_injury_adaptation: bool
    selected_uses_transfer_model: bool
    selected_uses_teaching_help: bool
    selected_uses_tool_training: bool
    selected_uses_goal_feasibility: bool
    selected_uses_continuity: bool
    train_reward: float
    naive_train_reward: float
    train_gain_over_naive: float


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
    mean_skill_level: float
    mean_practice_history: float
    mean_fatigue: float
    mean_injury_load: float
    mean_transfer_confidence: float
    mean_teaching_support: float
    mean_tool_support: float
    mean_feasibility: float
    mean_overreach_events: float
    mean_failure_events: float
    mean_practice_actions: float
    mean_rest_actions: float
    mean_retrain_actions: float
    mean_teaching_actions: float
    mean_tool_actions: float
    mean_replan_actions: float
    mean_continuity_resets: float
    mean_skill_misses: float


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    expected_pressure: str
    selected_policy: str
    selected_reward: float
    no_skill_memory_reward: float
    no_practice_planning_reward: float
    no_capability_state_reward: float
    no_fatigue_management_reward: float
    no_injury_adaptation_reward: float
    no_transfer_model_reward: float
    no_teaching_help_reward: float
    no_tool_training_reward: float
    no_goal_feasibility_reward: float
    no_continuity_reward: float
    naive_fixed_skill_baseline_reward: float
    omniscient_skill_control_reward: float
    no_skill_memory_loss: float
    no_practice_planning_loss: float
    no_capability_state_loss: float
    no_fatigue_management_loss: float
    no_injury_adaptation_loss: float
    no_transfer_model_loss: float
    no_teaching_help_loss: float
    no_tool_training_loss: float
    no_goal_feasibility_loss: float
    no_continuity_loss: float
    naive_fixed_skill_baseline_loss: float
    selected_overreach_events: float
    selected_failure_events: float
    selected_practice_actions: float
    selected_rest_actions: float
    selected_retrain_actions: float
    selected_teaching_actions: float
    selected_tool_actions: float
    selected_replan_actions: float
    supports_development_skill_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        index=0,
        name="easy_fixed_skill_control",
        pressure="easy stable task where skill machinery should not matter",
        expected_skill_memory=False,
        expected_practice_planning=False,
        expected_capability_state=False,
        expected_fatigue_management=False,
        expected_injury_adaptation=False,
        expected_transfer_model=False,
        expected_teaching_help=False,
        expected_tool_training=False,
        expected_goal_feasibility=False,
        expected_continuity=False,
        difficulty=0.10,
        practice_opportunity=0.02,
        fatigue_pressure=0.04,
        injury_pressure=0.00,
        transfer_pressure=0.00,
        teaching_pressure=0.00,
        tool_value=0.00,
        required_progress=122.0,
        work_rate=0.73,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=1,
        name="practice_curve_transfer",
        pressure="hard task needs practice history, transfer estimation, and feasible goal selection",
        expected_skill_memory=True,
        expected_practice_planning=True,
        expected_capability_state=True,
        expected_fatigue_management=False,
        expected_injury_adaptation=False,
        expected_transfer_model=True,
        expected_teaching_help=False,
        expected_tool_training=False,
        expected_goal_feasibility=True,
        expected_continuity=False,
        difficulty=0.84,
        practice_opportunity=0.88,
        fatigue_pressure=0.20,
        injury_pressure=0.04,
        transfer_pressure=0.62,
        teaching_pressure=0.05,
        tool_value=0.08,
        required_progress=88.0,
        work_rate=0.54,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=2,
        name="fatigue_skill_degradation",
        pressure="fatigue makes nominal competence unreliable unless capability and rest calibration are tracked",
        expected_skill_memory=True,
        expected_practice_planning=False,
        expected_capability_state=True,
        expected_fatigue_management=True,
        expected_injury_adaptation=False,
        expected_transfer_model=False,
        expected_teaching_help=False,
        expected_tool_training=False,
        expected_goal_feasibility=True,
        expected_continuity=False,
        difficulty=0.66,
        practice_opportunity=0.18,
        fatigue_pressure=0.90,
        injury_pressure=0.05,
        transfer_pressure=0.08,
        teaching_pressure=0.04,
        tool_value=0.04,
        required_progress=82.0,
        work_rate=0.53,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=3,
        name="injury_retraining_substitution",
        pressure="injury changes the useful skill, so retraining and support tools preserve feasible action",
        expected_skill_memory=True,
        expected_practice_planning=True,
        expected_capability_state=True,
        expected_fatigue_management=False,
        expected_injury_adaptation=True,
        expected_transfer_model=False,
        expected_teaching_help=False,
        expected_tool_training=True,
        expected_goal_feasibility=True,
        expected_continuity=False,
        difficulty=0.72,
        practice_opportunity=0.62,
        fatigue_pressure=0.24,
        injury_pressure=0.86,
        transfer_pressure=0.10,
        teaching_pressure=0.08,
        tool_value=0.76,
        required_progress=78.0,
        work_rate=0.51,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=4,
        name="teaching_tool_transfer",
        pressure="teaching and training tools accelerate useful transfer but compete with immediate work",
        expected_skill_memory=True,
        expected_practice_planning=True,
        expected_capability_state=True,
        expected_fatigue_management=False,
        expected_injury_adaptation=False,
        expected_transfer_model=True,
        expected_teaching_help=True,
        expected_tool_training=True,
        expected_goal_feasibility=True,
        expected_continuity=False,
        difficulty=0.76,
        practice_opportunity=0.74,
        fatigue_pressure=0.24,
        injury_pressure=0.06,
        transfer_pressure=0.82,
        teaching_pressure=0.84,
        tool_value=0.80,
        required_progress=82.0,
        work_rate=0.52,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=5,
        name="restore_skill_continuity",
        pressure="after restore, skill level, practice history, transfer, tools, teaching, and feasibility must survive",
        expected_skill_memory=True,
        expected_practice_planning=True,
        expected_capability_state=True,
        expected_fatigue_management=True,
        expected_injury_adaptation=True,
        expected_transfer_model=True,
        expected_teaching_help=True,
        expected_tool_training=True,
        expected_goal_feasibility=True,
        expected_continuity=True,
        difficulty=0.78,
        practice_opportunity=0.68,
        fatigue_pressure=0.54,
        injury_pressure=0.42,
        transfer_pressure=0.62,
        teaching_pressure=0.62,
        tool_value=0.70,
        required_progress=70.0,
        work_rate=0.48,
        restore_tick=96,
    ),
)


SEEDED_POLICIES = (
    Policy(
        name="naive_fixed_skill_baseline",
        skill_memory=False,
        practice_planning=False,
        capability_state=False,
        fatigue_management=False,
        injury_adaptation=False,
        transfer_model=False,
        teaching_help=False,
        tool_training=False,
        goal_feasibility=False,
        continuity_memory=False,
        risk_threshold=0.88,
        practice_bias=0.04,
        teaching_bias=0.04,
        tool_bias=0.04,
    ),
    Policy(
        name="reactive_practice_worker",
        skill_memory=True,
        practice_planning=True,
        capability_state=False,
        fatigue_management=False,
        injury_adaptation=False,
        transfer_model=False,
        teaching_help=False,
        tool_training=False,
        goal_feasibility=False,
        continuity_memory=False,
        risk_threshold=0.64,
        practice_bias=0.44,
        teaching_bias=0.04,
        tool_bias=0.04,
    ),
    Policy(
        name="deliberate_transfer_planner",
        skill_memory=True,
        practice_planning=True,
        capability_state=True,
        fatigue_management=False,
        injury_adaptation=False,
        transfer_model=True,
        teaching_help=False,
        tool_training=False,
        goal_feasibility=True,
        continuity_memory=False,
        risk_threshold=0.32,
        practice_bias=0.82,
        teaching_bias=0.05,
        tool_bias=0.05,
    ),
    Policy(
        name="fatigue_calibration_planner",
        skill_memory=True,
        practice_planning=False,
        capability_state=True,
        fatigue_management=True,
        injury_adaptation=False,
        transfer_model=False,
        teaching_help=False,
        tool_training=False,
        goal_feasibility=True,
        continuity_memory=False,
        risk_threshold=0.30,
        practice_bias=0.16,
        teaching_bias=0.04,
        tool_bias=0.04,
    ),
    Policy(
        name="injury_retraining_planner",
        skill_memory=True,
        practice_planning=True,
        capability_state=True,
        fatigue_management=False,
        injury_adaptation=True,
        transfer_model=False,
        teaching_help=False,
        tool_training=True,
        goal_feasibility=True,
        continuity_memory=False,
        risk_threshold=0.30,
        practice_bias=0.70,
        teaching_bias=0.06,
        tool_bias=0.82,
    ),
    Policy(
        name="mentor_tool_transfer_planner",
        skill_memory=True,
        practice_planning=True,
        capability_state=True,
        fatigue_management=False,
        injury_adaptation=False,
        transfer_model=True,
        teaching_help=True,
        tool_training=True,
        goal_feasibility=True,
        continuity_memory=False,
        risk_threshold=0.34,
        practice_bias=0.70,
        teaching_bias=0.84,
        tool_bias=0.82,
    ),
    Policy(
        name="continuity_skill_planner",
        skill_memory=True,
        practice_planning=True,
        capability_state=True,
        fatigue_management=True,
        injury_adaptation=True,
        transfer_model=True,
        teaching_help=True,
        tool_training=True,
        goal_feasibility=True,
        continuity_memory=True,
        risk_threshold=0.32,
        practice_bias=0.72,
        teaching_bias=0.78,
        tool_bias=0.78,
    ),
)


CONDITIONS = (
    "full_control",
    "no_skill_memory",
    "no_practice_planning",
    "no_capability_state",
    "no_fatigue_management",
    "no_injury_adaptation",
    "no_transfer_model",
    "no_teaching_help",
    "no_tool_training",
    "no_goal_feasibility",
    "no_continuity",
    "naive_fixed_skill_baseline",
    "omniscient_skill_control",
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


def build_policies(cfg: SkillConfig) -> List[Policy]:
    policies = list(SEEDED_POLICIES)
    rng = random.Random(cfg.seed + 1901)
    while len(policies) < cfg.candidate_count:
        base = rng.choice(SEEDED_POLICIES[2:])
        policies.append(
            Policy(
                name=f"mutant_skill_{len(policies)}",
                skill_memory=base.skill_memory if rng.random() > 0.12 else not base.skill_memory,
                practice_planning=base.practice_planning if rng.random() > 0.16 else not base.practice_planning,
                capability_state=base.capability_state if rng.random() > 0.14 else not base.capability_state,
                fatigue_management=base.fatigue_management if rng.random() > 0.16 else not base.fatigue_management,
                injury_adaptation=base.injury_adaptation if rng.random() > 0.16 else not base.injury_adaptation,
                transfer_model=base.transfer_model if rng.random() > 0.16 else not base.transfer_model,
                teaching_help=base.teaching_help if rng.random() > 0.18 else not base.teaching_help,
                tool_training=base.tool_training if rng.random() > 0.16 else not base.tool_training,
                goal_feasibility=base.goal_feasibility if rng.random() > 0.14 else not base.goal_feasibility,
                continuity_memory=base.continuity_memory if rng.random() > 0.18 else not base.continuity_memory,
                risk_threshold=clamp(base.risk_threshold + rng.uniform(-0.08, 0.08), 0.16, 0.92),
                practice_bias=clamp(base.practice_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
                teaching_bias=clamp(base.teaching_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
                tool_bias=clamp(base.tool_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
            )
        )
    return policies


def condition_policy(policy: Policy, condition: str) -> Policy:
    if condition == "omniscient_skill_control":
        return Policy(
            name=policy.name,
            skill_memory=True,
            practice_planning=True,
            capability_state=True,
            fatigue_management=True,
            injury_adaptation=True,
            transfer_model=True,
            teaching_help=True,
            tool_training=True,
            goal_feasibility=True,
            continuity_memory=True,
            risk_threshold=0.12,
            practice_bias=max(policy.practice_bias, 0.92),
            teaching_bias=max(policy.teaching_bias, 0.92),
            tool_bias=max(policy.tool_bias, 0.92),
        )
    if condition == "naive_fixed_skill_baseline":
        return Policy(
            name=policy.name,
            skill_memory=False,
            practice_planning=False,
            capability_state=False,
            fatigue_management=False,
            injury_adaptation=False,
            transfer_model=False,
            teaching_help=False,
            tool_training=False,
            goal_feasibility=False,
            continuity_memory=False,
            risk_threshold=0.88,
            practice_bias=0.04,
            teaching_bias=0.04,
            tool_bias=0.04,
        )
    return Policy(
        name=policy.name,
        skill_memory=policy.skill_memory and condition != "no_skill_memory",
        practice_planning=policy.practice_planning and condition != "no_practice_planning",
        capability_state=policy.capability_state and condition != "no_capability_state",
        fatigue_management=policy.fatigue_management and condition != "no_fatigue_management",
        injury_adaptation=policy.injury_adaptation and condition != "no_injury_adaptation",
        transfer_model=policy.transfer_model and condition != "no_transfer_model",
        teaching_help=policy.teaching_help and condition != "no_teaching_help",
        tool_training=policy.tool_training and condition != "no_tool_training",
        goal_feasibility=policy.goal_feasibility and condition != "no_goal_feasibility",
        continuity_memory=policy.continuity_memory and condition != "no_continuity",
        risk_threshold=policy.risk_threshold,
        practice_bias=policy.practice_bias,
        teaching_bias=policy.teaching_bias,
        tool_bias=policy.tool_bias,
    )


def scenario_seed(
    cfg: SkillConfig,
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
        (policy.skill_memory, 2.30),
        (policy.practice_planning, 2.80),
        (policy.capability_state, 2.60),
        (policy.fatigue_management, 2.70),
        (policy.injury_adaptation, 2.80),
        (policy.transfer_model, 2.80),
        (policy.teaching_help, 3.10),
        (policy.tool_training, 2.90),
        (policy.goal_feasibility, 2.60),
        (policy.continuity_memory, 8.80),
    ]
    return sum(weight for enabled, weight in weighted_flags if enabled)


def estimate_risk(
    scenario: ScenarioSpec,
    policy: Policy,
    skill: float,
    fatigue: float,
    injury: float,
    transfer: float,
    teaching: float,
    tool: float,
    feasibility: float,
) -> float:
    if not policy.capability_state:
        observed_skill = 0.62
        observed_fatigue = 0.22
        observed_injury = 0.10
    else:
        observed_skill = skill
        observed_fatigue = fatigue
        observed_injury = injury
    load = (
        scenario.difficulty * (1.0 - observed_skill) * 0.74
        + scenario.fatigue_pressure * observed_fatigue * 0.58
        + scenario.injury_pressure * observed_injury * 0.64
        + scenario.transfer_pressure * (1.0 - transfer) * 0.42
        + scenario.teaching_pressure * (1.0 - teaching) * 0.34
        + scenario.tool_value * (1.0 - tool) * 0.32
        + (1.0 - feasibility) * 0.38
    )
    mitigation = (
        (0.11 if policy.skill_memory else 0.0)
        + (0.12 if policy.practice_planning else 0.0)
        + (0.10 if policy.fatigue_management else 0.0)
        + (0.10 if policy.injury_adaptation else 0.0)
        + (0.11 if policy.transfer_model else 0.0)
        + (0.11 if policy.teaching_help else 0.0)
        + (0.11 if policy.tool_training else 0.0)
        + (0.12 if policy.goal_feasibility else 0.0)
    )
    return clamp(load - mitigation, 0.0, 1.8)


def choose_action(
    scenario: ScenarioSpec,
    policy: Policy,
    risk: float,
    skill: float,
    fatigue: float,
    injury: float,
    transfer: float,
    teaching: float,
    tool: float,
    feasibility: float,
    tick: int,
) -> str:
    if scenario.index == 0:
        return "work"
    if policy.fatigue_management and scenario.expected_fatigue_management and fatigue > 0.48 and risk > policy.risk_threshold * 0.58:
        return "rest_calibrate"
    if policy.injury_adaptation and scenario.expected_injury_adaptation and injury > 0.30 and risk > policy.risk_threshold * 0.58:
        return "retrain_after_injury"
    if policy.teaching_help and scenario.expected_teaching_help and teaching < 0.62 and risk > policy.risk_threshold * 0.68:
        return "request_teaching"
    if policy.tool_training and scenario.expected_tool_training and tool < 0.62 and risk > policy.risk_threshold * 0.68:
        return "use_training_tool"
    if policy.practice_planning and scenario.expected_practice_planning and skill < (0.68 + scenario.difficulty * 0.10) and tick % 5 == 0:
        return "practice"
    if policy.transfer_model and scenario.expected_transfer_model and transfer < 0.64 and tick % 9 == 0:
        return "transfer_drill"
    if policy.goal_feasibility and scenario.expected_goal_feasibility and feasibility < 0.64 and risk > policy.risk_threshold * 0.72:
        return "replan_goal"
    return "work"


def add_trace(
    trace: List[Dict[str, object]],
    tick: int,
    action: str,
    progress: float,
    energy: float,
    integrity: float,
    skill: float,
    practice: float,
    fatigue: float,
    injury: float,
    transfer: float,
    teaching: float,
    tool: float,
    feasibility: float,
    overreach: int,
    failures: int,
    notes: List[str],
) -> None:
    trace.append(
        {
            "tick": tick,
            "action": action,
            "progress": round(progress, 3),
            "energy": round(energy, 3),
            "integrity": round(integrity, 3),
            "skill_level": round(skill, 3),
            "practice_history": round(practice, 3),
            "fatigue": round(fatigue, 3),
            "injury_load": round(injury, 3),
            "transfer_confidence": round(transfer, 3),
            "teaching_support": round(teaching, 3),
            "tool_support": round(tool, 3),
            "feasibility": round(feasibility, 3),
            "overreach_events": overreach,
            "failure_events": failures,
            "notes": list(notes[-3:]),
        }
    )


def simulate_episode(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episode: int,
    cfg: SkillConfig,
    phase: str,
    collect_trace: bool = False,
) -> Tuple[EpisodeResult, List[Dict[str, object]]]:
    effective = condition_policy(policy, condition)
    rng = random.Random(scenario_seed(cfg, scenario, policy, condition, episode, phase))

    skill = clamp(0.72 - scenario.difficulty * 0.38 + rng.uniform(-0.015, 0.015), 0.05, 1.0)
    practice = clamp(0.10 + (0.10 if effective.skill_memory else 0.0), 0.0, 1.0)
    fatigue = clamp(0.16 + scenario.fatigue_pressure * 0.10 + rng.uniform(-0.010, 0.010), 0.0, 1.3)
    injury = clamp(0.05 + scenario.injury_pressure * 0.18 + rng.uniform(-0.010, 0.010), 0.0, 1.2)
    transfer = 0.58 if scenario.expected_transfer_model and effective.transfer_model else (0.76 if not scenario.expected_transfer_model else 0.22)
    teaching = 0.18 if scenario.expected_teaching_help else 0.82
    tool = 0.16 if scenario.expected_tool_training else 0.82
    feasibility = 0.46 if scenario.expected_goal_feasibility else 0.86
    energy = clamp(0.96 - scenario.fatigue_pressure * 0.04, 0.0, 1.0)
    integrity = clamp(0.98 - scenario.injury_pressure * 0.05, 0.0, 1.0)
    progress = 0.0
    collapsed = False
    notes: List[str] = []
    trace_frames: List[Dict[str, object]] = []

    overreach_events = 0
    failure_events = 0
    practice_actions = 0
    rest_actions = 0
    retrain_actions = 0
    teaching_actions = 0
    tool_actions = 0
    replan_actions = 0
    continuity_resets = 0
    skill_misses = 0

    for tick in range(cfg.ticks):
        action = "work"
        if scenario.restore_tick == tick and not effective.continuity_memory:
            continuity_resets += 1
            skill_misses += 6
            skill = clamp(skill - 0.30, 0.0, 1.0)
            practice = clamp(practice - 0.34, 0.0, 1.0)
            transfer = min(transfer, 0.20)
            teaching = max(0.04, teaching - 0.30)
            tool = max(0.04, tool - 0.30)
            feasibility = max(0.08, feasibility - 0.36)
            fatigue = clamp(fatigue + 0.22, 0.0, 1.3)
            injury = clamp(injury + 0.18, 0.0, 1.2)
            notes.append("restore erased skill continuity")
            action = "restore_reset"

        risk = estimate_risk(scenario, effective, skill, fatigue, injury, transfer, teaching, tool, feasibility)
        if not collapsed and action != "restore_reset":
            action = choose_action(
                scenario,
                effective,
                risk,
                skill,
                fatigue,
                injury,
                transfer,
                teaching,
                tool,
                feasibility,
                tick,
            )

        if collapsed:
            action = "collapsed"
        elif action == "practice":
            practice_actions += 1
            gain = scenario.practice_opportunity * (0.017 + effective.practice_bias * 0.012)
            skill = clamp(skill + gain, 0.0, 1.0)
            practice = clamp(practice + gain * 1.8, 0.0, 1.0)
            fatigue = clamp(fatigue + 0.006 + scenario.fatigue_pressure * 0.001, 0.0, 1.3)
            progress += scenario.work_rate * 0.08
            notes.append("practice increased future competence")
        elif action == "transfer_drill":
            practice_actions += 1
            transfer = clamp(transfer + 0.18 + effective.practice_bias * 0.08, 0.0, 1.0)
            skill = clamp(skill + scenario.practice_opportunity * 0.008, 0.0, 1.0)
            fatigue = clamp(fatigue + 0.010, 0.0, 1.3)
            progress += scenario.work_rate * 0.06
            notes.append("transfer drill mapped old skill to task")
        elif action == "rest_calibrate":
            rest_actions += 1
            fatigue = clamp(fatigue - 0.22, 0.0, 1.3)
            energy = clamp(energy + 0.030, 0.0, 1.0)
            feasibility = clamp(feasibility + 0.06, 0.0, 1.0)
            progress += scenario.work_rate * 0.04
            notes.append("rest recalibrated tired skill")
        elif action == "retrain_after_injury":
            retrain_actions += 1
            injury = clamp(injury - 0.10, 0.0, 1.2)
            skill = clamp(skill + 0.035 + scenario.practice_opportunity * 0.010, 0.0, 1.0)
            feasibility = clamp(feasibility + 0.10, 0.0, 1.0)
            fatigue = clamp(fatigue + 0.010, 0.0, 1.3)
            progress += scenario.work_rate * 0.05
            notes.append("retraining matched skill to injury")
        elif action == "request_teaching":
            teaching_actions += 1
            teaching = clamp(teaching + 0.34 + effective.teaching_bias * 0.18, 0.0, 1.0)
            transfer = clamp(transfer + 0.08 + effective.teaching_bias * 0.06, 0.0, 1.0)
            progress -= 0.14
            notes.append("teaching improved skill transfer")
        elif action == "use_training_tool":
            tool_actions += 1
            tool = clamp(tool + 0.34 + effective.tool_bias * 0.18, 0.0, 1.0)
            skill = clamp(skill + scenario.tool_value * 0.018, 0.0, 1.0)
            feasibility = clamp(feasibility + 0.08, 0.0, 1.0)
            progress -= 0.12
            notes.append("training tool expanded feasible action")
        elif action == "replan_goal":
            replan_actions += 1
            feasibility = clamp(feasibility + 0.26, 0.0, 1.0)
            fatigue = clamp(fatigue - 0.030, 0.0, 1.3)
            progress -= 0.12
            notes.append("goal replanned around current competence")
        elif action == "work":
            capability = clamp(
                0.64
                + skill * 0.34
                + transfer * scenario.transfer_pressure * 0.07
                + teaching * scenario.teaching_pressure * 0.04
                + tool * scenario.tool_value * 0.05
                + feasibility * 0.12
                + energy * 0.08
                - scenario.difficulty * 0.22
                - fatigue * 0.18
                - injury * 0.20,
                0.03,
                1.12,
            )
            progress += scenario.work_rate * capability
            fatigue = clamp(fatigue + 0.002 + scenario.fatigue_pressure * 0.0014, 0.0, 1.3)
            if risk > 0.62 and tick % 11 == 0:
                overreach_events += 1
                integrity = clamp(integrity - 0.018 - scenario.injury_pressure * 0.012, 0.0, 1.0)
                fatigue = clamp(fatigue + 0.035, 0.0, 1.3)
                skill_misses += 1
            if capability < 0.42 and tick % 13 == 0:
                failure_events += 1
                progress -= 0.24
                skill_misses += 1

        if scenario.expected_skill_memory and not effective.skill_memory:
            skill = clamp(skill - 0.0025, 0.0, 1.0)
            practice = clamp(practice - 0.0020, 0.0, 1.0)
            skill_misses += 1 if tick % 17 == 0 else 0
        if scenario.expected_practice_planning:
            if effective.practice_planning:
                skill = clamp(skill + scenario.practice_opportunity * 0.0010, 0.0, 1.0)
            else:
                skill = clamp(skill - scenario.practice_opportunity * 0.0045, 0.0, 1.0)
                skill_misses += 1 if tick % 17 == 0 else 0
        if scenario.expected_capability_state and not effective.capability_state:
            feasibility = clamp(feasibility - 0.0045, 0.0, 1.0)
            fatigue = clamp(fatigue + 0.0028, 0.0, 1.3)
            skill_misses += 1 if tick % 19 == 0 else 0
        if scenario.expected_fatigue_management:
            if effective.fatigue_management:
                fatigue = clamp(fatigue + scenario.fatigue_pressure * 0.0008, 0.0, 1.3)
            else:
                fatigue = clamp(fatigue + scenario.fatigue_pressure * 0.0065, 0.0, 1.3)
                skill = clamp(skill - scenario.fatigue_pressure * 0.0025, 0.0, 1.0)
                skill_misses += 1 if tick % 13 == 0 else 0
        if scenario.expected_injury_adaptation:
            if effective.injury_adaptation:
                injury = clamp(injury + scenario.injury_pressure * 0.0010, 0.0, 1.2)
            else:
                injury = clamp(injury + scenario.injury_pressure * 0.0060, 0.0, 1.2)
                skill = clamp(skill - scenario.injury_pressure * 0.0032, 0.0, 1.0)
                skill_misses += 1 if tick % 13 == 0 else 0
        if scenario.expected_transfer_model:
            if effective.transfer_model:
                transfer = clamp(transfer - scenario.transfer_pressure * 0.0010, 0.0, 1.0)
            else:
                transfer = clamp(transfer - scenario.transfer_pressure * 0.0065, 0.0, 1.0)
                feasibility = clamp(feasibility - scenario.transfer_pressure * 0.0035, 0.0, 1.0)
                skill_misses += 1 if tick % 17 == 0 else 0
        if scenario.expected_teaching_help:
            if effective.teaching_help:
                teaching = clamp(teaching - scenario.teaching_pressure * 0.0010, 0.0, 1.0)
            else:
                teaching = clamp(teaching - scenario.teaching_pressure * 0.0065, 0.0, 1.0)
                transfer = clamp(transfer - scenario.teaching_pressure * 0.0045, 0.0, 1.0)
                skill_misses += 1 if tick % 19 == 0 else 0
        if scenario.expected_tool_training:
            if effective.tool_training:
                tool = clamp(tool - scenario.tool_value * 0.0010, 0.0, 1.0)
            else:
                tool = clamp(tool - scenario.tool_value * 0.0070, 0.0, 1.0)
                feasibility = clamp(feasibility - scenario.tool_value * 0.0045, 0.0, 1.0)
                skill_misses += 1 if tick % 17 == 0 else 0
        if scenario.expected_goal_feasibility:
            if effective.goal_feasibility:
                feasibility = clamp(feasibility - scenario.difficulty * 0.0008, 0.0, 1.0)
            else:
                feasibility = clamp(feasibility - scenario.difficulty * 0.0065, 0.0, 1.0)
                overreach_events += 1 if tick % 23 == 0 else 0
                skill_misses += 1 if tick % 17 == 0 else 0

        energy = clamp(energy - 0.0010 - fatigue * 0.0012 - injury * 0.0010 + (0.0015 if action == "rest_calibrate" else 0.0), 0.0, 1.0)
        integrity = clamp(integrity - injury * 0.0009 - fatigue * 0.0004 - overreach_events * 0.00005, 0.0, 1.0)
        if energy <= 0.04 or integrity <= 0.06 or fatigue >= 1.18 or injury >= 1.08:
            collapsed = True

        if collect_trace and (tick % 5 == 0 or tick == cfg.ticks - 1 or action != "work"):
            add_trace(
                trace_frames,
                tick,
                action,
                progress,
                energy,
                integrity,
                skill,
                practice,
                fatigue,
                injury,
                transfer,
                teaching,
                tool,
                feasibility,
                overreach_events,
                failure_events,
                notes,
            )

    task_success = progress >= scenario.required_progress and not collapsed
    survival = 1.0 if not collapsed and energy > 0.06 and integrity > 0.10 and fatigue < 1.08 and injury < 1.0 else 0.0

    reward = progress
    reward += 34.0 if task_success else -24.0
    reward += 42.0 if survival else -116.0
    reward += energy * 18.0
    reward += integrity * 18.0
    reward += skill * (24.0 if scenario.expected_skill_memory or scenario.expected_practice_planning else 2.0)
    reward += practice * (12.0 if scenario.expected_practice_planning else 1.0)
    reward += transfer * (18.0 if scenario.expected_transfer_model else 1.0)
    reward += teaching * (18.0 if scenario.expected_teaching_help else 1.0)
    reward += tool * (18.0 if scenario.expected_tool_training else 1.0)
    reward += feasibility * (22.0 if scenario.expected_goal_feasibility else 1.0)
    reward -= fatigue * 56.0
    reward -= injury * 82.0
    reward -= overreach_events * 5.8
    reward -= failure_events * 4.8
    reward -= skill_misses * 0.95
    reward -= practice_actions * 0.12
    reward -= rest_actions * 0.12
    reward -= retrain_actions * 0.16
    reward -= teaching_actions * 0.20
    reward -= tool_actions * 0.18
    reward -= replan_actions * 0.16
    reward -= feature_overhead(effective)
    if scenario.expected_continuity and continuity_resets:
        reward -= 90.0
    if scenario.expected_skill_memory and not effective.skill_memory:
        reward -= scenario.difficulty * 70.0
    if scenario.expected_practice_planning and not effective.practice_planning:
        reward -= scenario.practice_opportunity * 120.0
    if scenario.expected_capability_state and not effective.capability_state:
        reward -= 58.0
    if scenario.expected_fatigue_management and not effective.fatigue_management:
        reward -= scenario.fatigue_pressure * 120.0
    if scenario.expected_injury_adaptation and not effective.injury_adaptation:
        reward -= scenario.injury_pressure * 120.0
    if scenario.expected_transfer_model and not effective.transfer_model:
        reward -= scenario.transfer_pressure * 130.0
    if scenario.expected_teaching_help and not effective.teaching_help:
        reward -= scenario.teaching_pressure * 220.0
    if scenario.expected_tool_training and not effective.tool_training:
        reward -= scenario.tool_value * 190.0
    if scenario.expected_goal_feasibility and not effective.goal_feasibility:
        reward -= scenario.difficulty * 90.0

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
        skill_level=skill,
        practice_history=practice,
        fatigue=fatigue,
        injury_load=injury,
        transfer_confidence=transfer,
        teaching_support=teaching,
        tool_support=tool,
        feasibility=feasibility,
        overreach_events=overreach_events,
        failure_events=failure_events,
        practice_actions=practice_actions,
        rest_actions=rest_actions,
        retrain_actions=retrain_actions,
        teaching_actions=teaching_actions,
        tool_actions=tool_actions,
        replan_actions=replan_actions,
        continuity_resets=continuity_resets,
        skill_misses=skill_misses,
    )
    return result, trace_frames


def evaluate_policy(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episodes: int,
    cfg: SkillConfig,
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
                    mean_skill_level=mean(row.skill_level for row in subset),
                    mean_practice_history=mean(row.practice_history for row in subset),
                    mean_fatigue=mean(row.fatigue for row in subset),
                    mean_injury_load=mean(row.injury_load for row in subset),
                    mean_transfer_confidence=mean(row.transfer_confidence for row in subset),
                    mean_teaching_support=mean(row.teaching_support for row in subset),
                    mean_tool_support=mean(row.tool_support for row in subset),
                    mean_feasibility=mean(row.feasibility for row in subset),
                    mean_overreach_events=mean(row.overreach_events for row in subset),
                    mean_failure_events=mean(row.failure_events for row in subset),
                    mean_practice_actions=mean(row.practice_actions for row in subset),
                    mean_rest_actions=mean(row.rest_actions for row in subset),
                    mean_retrain_actions=mean(row.retrain_actions for row in subset),
                    mean_teaching_actions=mean(row.teaching_actions for row in subset),
                    mean_tool_actions=mean(row.tool_actions for row in subset),
                    mean_replan_actions=mean(row.replan_actions for row in subset),
                    mean_continuity_resets=mean(row.continuity_resets for row in subset),
                    mean_skill_misses=mean(row.skill_misses for row in subset),
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
                full.policy_name == "naive_fixed_skill_baseline"
                and max(
                    abs(losses[condition])
                    for condition in CONDITIONS
                    if condition not in {"full_control", "omniscient_skill_control"}
                )
                < 8.0
            )
            verdict = "skill_machinery_rejected_in_easy_fixed_control"
        elif scenario.index == 1:
            supports = (
                losses["no_skill_memory"] > 45.0
                and losses["no_practice_planning"] > 70.0
                and losses["no_capability_state"] > 30.0
                and losses["no_transfer_model"] > 60.0
                and losses["no_goal_feasibility"] > 45.0
                and losses["naive_fixed_skill_baseline"] > 60.0
            )
            verdict = "practice_curve_transfer_pressure"
        elif scenario.index == 2:
            supports = (
                losses["no_skill_memory"] > 25.0
                and losses["no_capability_state"] > 35.0
                and losses["no_fatigue_management"] > 90.0
                and losses["no_goal_feasibility"] > 45.0
                and losses["naive_fixed_skill_baseline"] > 55.0
            )
            verdict = "fatigue_skill_degradation_pressure"
        elif scenario.index == 3:
            supports = (
                losses["no_skill_memory"] > 30.0
                and losses["no_practice_planning"] > 35.0
                and losses["no_capability_state"] > 35.0
                and losses["no_injury_adaptation"] > 90.0
                and losses["no_tool_training"] > 55.0
                and losses["no_goal_feasibility"] > 45.0
            )
            verdict = "injury_retraining_substitution_pressure"
        elif scenario.index == 4:
            supports = (
                losses["no_skill_memory"] > 30.0
                and losses["no_practice_planning"] > 35.0
                and losses["no_transfer_model"] > 70.0
                and losses["no_teaching_help"] > 70.0
                and losses["no_tool_training"] > 65.0
                and losses["no_goal_feasibility"] > 45.0
            )
            verdict = "teaching_tool_transfer_pressure"
        else:
            supports = (
                losses["no_continuity"] > 54.0
                and losses["no_skill_memory"] > 40.0
                and losses["no_practice_planning"] > 40.0
                and losses["no_capability_state"] > 40.0
                and losses["no_fatigue_management"] > 40.0
                and losses["no_injury_adaptation"] > 40.0
                and losses["no_transfer_model"] > 40.0
                and losses["no_teaching_help"] > 40.0
                and losses["no_tool_training"] > 40.0
                and losses["no_goal_feasibility"] > 40.0
            )
            verdict = "restore_skill_continuity_pressure"

        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                expected_pressure=scenario.pressure,
                selected_policy=full.policy_name,
                selected_reward=full.mean_reward,
                no_skill_memory_reward=rewards["no_skill_memory"],
                no_practice_planning_reward=rewards["no_practice_planning"],
                no_capability_state_reward=rewards["no_capability_state"],
                no_fatigue_management_reward=rewards["no_fatigue_management"],
                no_injury_adaptation_reward=rewards["no_injury_adaptation"],
                no_transfer_model_reward=rewards["no_transfer_model"],
                no_teaching_help_reward=rewards["no_teaching_help"],
                no_tool_training_reward=rewards["no_tool_training"],
                no_goal_feasibility_reward=rewards["no_goal_feasibility"],
                no_continuity_reward=rewards["no_continuity"],
                naive_fixed_skill_baseline_reward=rewards["naive_fixed_skill_baseline"],
                omniscient_skill_control_reward=rewards["omniscient_skill_control"],
                no_skill_memory_loss=losses["no_skill_memory"],
                no_practice_planning_loss=losses["no_practice_planning"],
                no_capability_state_loss=losses["no_capability_state"],
                no_fatigue_management_loss=losses["no_fatigue_management"],
                no_injury_adaptation_loss=losses["no_injury_adaptation"],
                no_transfer_model_loss=losses["no_transfer_model"],
                no_teaching_help_loss=losses["no_teaching_help"],
                no_tool_training_loss=losses["no_tool_training"],
                no_goal_feasibility_loss=losses["no_goal_feasibility"],
                no_continuity_loss=losses["no_continuity"],
                naive_fixed_skill_baseline_loss=losses["naive_fixed_skill_baseline"],
                selected_overreach_events=full.mean_overreach_events,
                selected_failure_events=full.mean_failure_events,
                selected_practice_actions=full.mean_practice_actions,
                selected_rest_actions=full.mean_rest_actions,
                selected_retrain_actions=full.mean_retrain_actions,
                selected_teaching_actions=full.mean_teaching_actions,
                selected_tool_actions=full.mean_tool_actions,
                selected_replan_actions=full.mean_replan_actions,
                supports_development_skill_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def select_policies(cfg: SkillConfig, policies: Sequence[Policy]) -> Tuple[Dict[int, Policy], List[PolicySelectionRow]]:
    selected: Dict[int, Policy] = {}
    rows: List[PolicySelectionRow] = []
    naive = next(policy for policy in policies if policy.name == "naive_fixed_skill_baseline")
    for scenario in SCENARIOS:
        scores: List[Tuple[float, Policy]] = []
        for policy in policies:
            train_rows = evaluate_policy(scenario, policy, "full_control", cfg.train_episodes, cfg, "train")
            scores.append((mean(row.total_reward for row in train_rows), policy))
        scores.sort(key=lambda item: item[0], reverse=True)
        best_reward, best_policy = scores[0]
        naive_rows = evaluate_policy(scenario, naive, "full_control", cfg.train_episodes, cfg, "train_naive")
        naive_reward = mean(row.total_reward for row in naive_rows)
        selected[scenario.index] = best_policy
        rows.append(
            PolicySelectionRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                selected_policy=best_policy.name,
                selected_uses_skill_memory=best_policy.skill_memory,
                selected_uses_practice_planning=best_policy.practice_planning,
                selected_uses_capability_state=best_policy.capability_state,
                selected_uses_fatigue_management=best_policy.fatigue_management,
                selected_uses_injury_adaptation=best_policy.injury_adaptation,
                selected_uses_transfer_model=best_policy.transfer_model,
                selected_uses_teaching_help=best_policy.teaching_help,
                selected_uses_tool_training=best_policy.tool_training,
                selected_uses_goal_feasibility=best_policy.goal_feasibility,
                selected_uses_continuity=best_policy.continuity_memory,
                train_reward=best_reward,
                naive_train_reward=naive_reward,
                train_gain_over_naive=best_reward - naive_reward,
            )
        )
    return selected, rows


def run_eval(cfg: SkillConfig, selected: Dict[int, Policy]) -> List[EpisodeResult]:
    eval_rows: List[EpisodeResult] = []
    for scenario in SCENARIOS:
        policy = selected[scenario.index]
        for condition in CONDITIONS:
            eval_rows.extend(evaluate_policy(scenario, policy, condition, cfg.eval_episodes, cfg, "eval"))
    return eval_rows


def build_trace(
    cfg: SkillConfig,
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
        "skill_loss",
        "practice_loss",
        "capability_loss",
        "fatigue_loss",
        "injury_loss",
        "transfer_loss",
        "teaching_loss",
        "tool_loss",
        "feasibility_loss",
        "continuity_loss",
        "supports",
    ]
    rows = [
        [
            row.scenario_name,
            row.selected_policy,
            f"{row.no_skill_memory_loss:.3f}",
            f"{row.no_practice_planning_loss:.3f}",
            f"{row.no_capability_state_loss:.3f}",
            f"{row.no_fatigue_management_loss:.3f}",
            f"{row.no_injury_adaptation_loss:.3f}",
            f"{row.no_transfer_model_loss:.3f}",
            f"{row.no_teaching_help_loss:.3f}",
            f"{row.no_tool_training_loss:.3f}",
            f"{row.no_goal_feasibility_loss:.3f}",
            f"{row.no_continuity_loss:.3f}",
            str(row.supports_development_skill_precursor),
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


def parse_args() -> SkillConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-episodes", type=int, default=SkillConfig.train_episodes)
    parser.add_argument("--eval-episodes", type=int, default=SkillConfig.eval_episodes)
    parser.add_argument("--ticks", type=int, default=SkillConfig.ticks)
    parser.add_argument("--seed", type=int, default=SkillConfig.seed)
    parser.add_argument("--candidate-count", type=int, default=SkillConfig.candidate_count)
    parser.add_argument("--trace-scenario", type=int, default=SkillConfig.trace_scenario)
    parser.add_argument("--trace-episode", type=int, default=SkillConfig.trace_episode)
    args = parser.parse_args()
    return SkillConfig(
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

    prefix = ARTIFACT_DIR / "ssrm_3d_development_skill_learning"
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
    write_js(prefix.with_name(prefix.name + "_results.js"), "SSRM_3D_DEVELOPMENT_SKILL_RESULTS", results)
    write_js(prefix.with_name(prefix.name + "_trace.js"), "SSRM_3D_DEVELOPMENT_SKILL_TRACE", trace)
    print_verdicts(verdict_rows)
    return 0 if all(row.supports_development_skill_precursor for row in verdict_rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
