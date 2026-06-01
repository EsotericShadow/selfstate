#!/usr/bin/env python3
"""SSRM-3D dependent-care precursor.

This experiment implements the eleventh pressure-layer step from report 74:
dependent care without biological reproduction. It is intentionally not a
family or roleplay simulation.

Fragile companions are treated as control pressure. The narrow test is whether
care state should be rejected in a no-dependent control, then become useful only
when another persistent agent changes protection, resources, repair, teaching,
promises, social access, priority arbitration, or restore continuity.
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
class CareConfig:
    train_episodes: int = 72
    eval_episodes: int = 96
    ticks: int = 210
    seed: int = 20260630
    candidate_count: int = 7
    trace_scenario: int = 4
    trace_episode: int = 0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    expected_dependent_state: bool
    expected_identity_memory: bool
    expected_protection_planning: bool
    expected_resource_sharing: bool
    expected_repair_care: bool
    expected_teaching_support: bool
    expected_shelter_coordination: bool
    expected_promise_commitment: bool
    expected_social_trust: bool
    expected_priority_arbitration: bool
    expected_continuity: bool
    hazard_pressure: float
    resource_pressure: float
    damage_pressure: float
    teaching_pressure: float
    promise_pressure: float
    social_pressure: float
    required_progress: float
    work_rate: float
    restore_tick: int


@dataclass(frozen=True)
class Policy:
    name: str
    dependent_state: bool
    identity_memory: bool
    protection_planning: bool
    resource_sharing: bool
    repair_care: bool
    teaching_support: bool
    shelter_coordination: bool
    promise_commitment: bool
    social_trust: bool
    priority_arbitration: bool
    continuity_memory: bool
    risk_threshold: float
    care_bias: float
    sharing_bias: float
    teaching_bias: float


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
    stress: float
    dependent_health: float
    dependent_energy: float
    dependent_skill: float
    dependent_safety: float
    dependent_trust: float
    resource_level: float
    shelter_safety: float
    promise_standing: float
    social_access: float
    protection_actions: int
    sharing_actions: int
    repair_actions: int
    teaching_actions: int
    shelter_actions: int
    promise_actions: int
    arbitration_actions: int
    neglect_events: int
    dependent_failures: int
    care_misses: int
    continuity_resets: int


@dataclass(frozen=True)
class PolicySelectionRow:
    scenario: int
    scenario_name: str
    selected_policy: str
    selected_uses_dependent_state: bool
    selected_uses_identity_memory: bool
    selected_uses_protection_planning: bool
    selected_uses_resource_sharing: bool
    selected_uses_repair_care: bool
    selected_uses_teaching_support: bool
    selected_uses_shelter_coordination: bool
    selected_uses_promise_commitment: bool
    selected_uses_social_trust: bool
    selected_uses_priority_arbitration: bool
    selected_uses_continuity: bool
    train_reward: float
    self_only_train_reward: float
    train_gain_over_self_only: float


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
    mean_stress: float
    mean_dependent_health: float
    mean_dependent_energy: float
    mean_dependent_skill: float
    mean_dependent_safety: float
    mean_dependent_trust: float
    mean_resource_level: float
    mean_shelter_safety: float
    mean_promise_standing: float
    mean_social_access: float
    mean_protection_actions: float
    mean_sharing_actions: float
    mean_repair_actions: float
    mean_teaching_actions: float
    mean_shelter_actions: float
    mean_promise_actions: float
    mean_arbitration_actions: float
    mean_neglect_events: float
    mean_dependent_failures: float
    mean_care_misses: float
    mean_continuity_resets: float


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    expected_pressure: str
    selected_policy: str
    selected_reward: float
    no_dependent_state_reward: float
    no_identity_memory_reward: float
    no_protection_planning_reward: float
    no_resource_sharing_reward: float
    no_repair_care_reward: float
    no_teaching_support_reward: float
    no_shelter_coordination_reward: float
    no_promise_commitment_reward: float
    no_social_trust_reward: float
    no_priority_arbitration_reward: float
    no_continuity_reward: float
    self_only_baseline_reward: float
    omniscient_care_control_reward: float
    no_dependent_state_loss: float
    no_identity_memory_loss: float
    no_protection_planning_loss: float
    no_resource_sharing_loss: float
    no_repair_care_loss: float
    no_teaching_support_loss: float
    no_shelter_coordination_loss: float
    no_promise_commitment_loss: float
    no_social_trust_loss: float
    no_priority_arbitration_loss: float
    no_continuity_loss: float
    self_only_baseline_loss: float
    selected_protection_actions: float
    selected_sharing_actions: float
    selected_repair_actions: float
    selected_teaching_actions: float
    selected_shelter_actions: float
    selected_promise_actions: float
    selected_arbitration_actions: float
    selected_neglect_events: float
    selected_dependent_failures: float
    supports_dependent_care_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        index=0,
        name="no_dependent_control",
        pressure="easy stable task with no fragile companion; care machinery should be rejected",
        expected_dependent_state=False,
        expected_identity_memory=False,
        expected_protection_planning=False,
        expected_resource_sharing=False,
        expected_repair_care=False,
        expected_teaching_support=False,
        expected_shelter_coordination=False,
        expected_promise_commitment=False,
        expected_social_trust=False,
        expected_priority_arbitration=False,
        expected_continuity=False,
        hazard_pressure=0.02,
        resource_pressure=0.02,
        damage_pressure=0.00,
        teaching_pressure=0.00,
        promise_pressure=0.00,
        social_pressure=0.00,
        required_progress=126.0,
        work_rate=0.74,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=1,
        name="fragile_companion_protection",
        pressure="dependent is vulnerable to hazards, so protection, shelter, and priority tradeoffs matter",
        expected_dependent_state=True,
        expected_identity_memory=True,
        expected_protection_planning=True,
        expected_resource_sharing=False,
        expected_repair_care=False,
        expected_teaching_support=False,
        expected_shelter_coordination=True,
        expected_promise_commitment=False,
        expected_social_trust=False,
        expected_priority_arbitration=True,
        expected_continuity=False,
        hazard_pressure=0.86,
        resource_pressure=0.22,
        damage_pressure=0.26,
        teaching_pressure=0.04,
        promise_pressure=0.08,
        social_pressure=0.12,
        required_progress=86.0,
        work_rate=0.52,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=2,
        name="resource_sharing_tradeoff",
        pressure="dependent viability competes with the agent's resource plan and future options",
        expected_dependent_state=True,
        expected_identity_memory=True,
        expected_protection_planning=False,
        expected_resource_sharing=True,
        expected_repair_care=False,
        expected_teaching_support=False,
        expected_shelter_coordination=False,
        expected_promise_commitment=False,
        expected_social_trust=False,
        expected_priority_arbitration=True,
        expected_continuity=False,
        hazard_pressure=0.18,
        resource_pressure=0.88,
        damage_pressure=0.10,
        teaching_pressure=0.04,
        promise_pressure=0.12,
        social_pressure=0.16,
        required_progress=82.0,
        work_rate=0.53,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=3,
        name="repair_teaching_burden",
        pressure="dependent damage and low skill create delayed burden unless repair and teaching are planned",
        expected_dependent_state=True,
        expected_identity_memory=True,
        expected_protection_planning=False,
        expected_resource_sharing=False,
        expected_repair_care=True,
        expected_teaching_support=True,
        expected_shelter_coordination=False,
        expected_promise_commitment=False,
        expected_social_trust=False,
        expected_priority_arbitration=True,
        expected_continuity=False,
        hazard_pressure=0.20,
        resource_pressure=0.22,
        damage_pressure=0.86,
        teaching_pressure=0.82,
        promise_pressure=0.12,
        social_pressure=0.16,
        required_progress=80.0,
        work_rate=0.51,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=4,
        name="promise_trust_care",
        pressure="care promises bind identity memory, social trust, sharing, and future access",
        expected_dependent_state=True,
        expected_identity_memory=True,
        expected_protection_planning=False,
        expected_resource_sharing=True,
        expected_repair_care=False,
        expected_teaching_support=False,
        expected_shelter_coordination=False,
        expected_promise_commitment=True,
        expected_social_trust=True,
        expected_priority_arbitration=True,
        expected_continuity=False,
        hazard_pressure=0.18,
        resource_pressure=0.52,
        damage_pressure=0.16,
        teaching_pressure=0.08,
        promise_pressure=0.86,
        social_pressure=0.84,
        required_progress=78.0,
        work_rate=0.50,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=5,
        name="restore_dependent_continuity",
        pressure="after restore, dependent identity, needs, promises, trust, shelter, and teaching history must survive",
        expected_dependent_state=True,
        expected_identity_memory=True,
        expected_protection_planning=True,
        expected_resource_sharing=True,
        expected_repair_care=True,
        expected_teaching_support=True,
        expected_shelter_coordination=True,
        expected_promise_commitment=True,
        expected_social_trust=True,
        expected_priority_arbitration=True,
        expected_continuity=True,
        hazard_pressure=0.58,
        resource_pressure=0.58,
        damage_pressure=0.54,
        teaching_pressure=0.52,
        promise_pressure=0.60,
        social_pressure=0.58,
        required_progress=68.0,
        work_rate=0.46,
        restore_tick=96,
    ),
)


SEEDED_POLICIES = (
    Policy(
        name="self_only_baseline",
        dependent_state=False,
        identity_memory=False,
        protection_planning=False,
        resource_sharing=False,
        repair_care=False,
        teaching_support=False,
        shelter_coordination=False,
        promise_commitment=False,
        social_trust=False,
        priority_arbitration=False,
        continuity_memory=False,
        risk_threshold=0.88,
        care_bias=0.04,
        sharing_bias=0.04,
        teaching_bias=0.04,
    ),
    Policy(
        name="reactive_helper",
        dependent_state=True,
        identity_memory=False,
        protection_planning=True,
        resource_sharing=True,
        repair_care=False,
        teaching_support=False,
        shelter_coordination=False,
        promise_commitment=False,
        social_trust=False,
        priority_arbitration=False,
        continuity_memory=False,
        risk_threshold=0.58,
        care_bias=0.42,
        sharing_bias=0.34,
        teaching_bias=0.04,
    ),
    Policy(
        name="protection_shelter_planner",
        dependent_state=True,
        identity_memory=True,
        protection_planning=True,
        resource_sharing=False,
        repair_care=False,
        teaching_support=False,
        shelter_coordination=True,
        promise_commitment=False,
        social_trust=False,
        priority_arbitration=True,
        continuity_memory=False,
        risk_threshold=0.30,
        care_bias=0.86,
        sharing_bias=0.06,
        teaching_bias=0.04,
    ),
    Policy(
        name="sharing_priority_planner",
        dependent_state=True,
        identity_memory=True,
        protection_planning=False,
        resource_sharing=True,
        repair_care=False,
        teaching_support=False,
        shelter_coordination=False,
        promise_commitment=False,
        social_trust=False,
        priority_arbitration=True,
        continuity_memory=False,
        risk_threshold=0.32,
        care_bias=0.58,
        sharing_bias=0.88,
        teaching_bias=0.04,
    ),
    Policy(
        name="repair_teaching_planner",
        dependent_state=True,
        identity_memory=True,
        protection_planning=False,
        resource_sharing=False,
        repair_care=True,
        teaching_support=True,
        shelter_coordination=False,
        promise_commitment=False,
        social_trust=False,
        priority_arbitration=True,
        continuity_memory=False,
        risk_threshold=0.32,
        care_bias=0.78,
        sharing_bias=0.08,
        teaching_bias=0.88,
    ),
    Policy(
        name="promise_trust_planner",
        dependent_state=True,
        identity_memory=True,
        protection_planning=False,
        resource_sharing=True,
        repair_care=False,
        teaching_support=False,
        shelter_coordination=False,
        promise_commitment=True,
        social_trust=True,
        priority_arbitration=True,
        continuity_memory=False,
        risk_threshold=0.34,
        care_bias=0.68,
        sharing_bias=0.72,
        teaching_bias=0.04,
    ),
    Policy(
        name="continuity_care_planner",
        dependent_state=True,
        identity_memory=True,
        protection_planning=True,
        resource_sharing=True,
        repair_care=True,
        teaching_support=True,
        shelter_coordination=True,
        promise_commitment=True,
        social_trust=True,
        priority_arbitration=True,
        continuity_memory=True,
        risk_threshold=0.28,
        care_bias=0.82,
        sharing_bias=0.78,
        teaching_bias=0.78,
    ),
)


CONDITIONS = (
    "full_control",
    "no_dependent_state",
    "no_identity_memory",
    "no_protection_planning",
    "no_resource_sharing",
    "no_repair_care",
    "no_teaching_support",
    "no_shelter_coordination",
    "no_promise_commitment",
    "no_social_trust",
    "no_priority_arbitration",
    "no_continuity",
    "self_only_baseline",
    "omniscient_care_control",
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


def build_policies(cfg: CareConfig) -> List[Policy]:
    policies = list(SEEDED_POLICIES)
    rng = random.Random(cfg.seed + 2303)
    while len(policies) < cfg.candidate_count:
        base = rng.choice(SEEDED_POLICIES[2:])
        policies.append(
            Policy(
                name=f"mutant_care_{len(policies)}",
                dependent_state=base.dependent_state if rng.random() > 0.10 else not base.dependent_state,
                identity_memory=base.identity_memory if rng.random() > 0.14 else not base.identity_memory,
                protection_planning=base.protection_planning if rng.random() > 0.16 else not base.protection_planning,
                resource_sharing=base.resource_sharing if rng.random() > 0.16 else not base.resource_sharing,
                repair_care=base.repair_care if rng.random() > 0.16 else not base.repair_care,
                teaching_support=base.teaching_support if rng.random() > 0.16 else not base.teaching_support,
                shelter_coordination=base.shelter_coordination if rng.random() > 0.16 else not base.shelter_coordination,
                promise_commitment=base.promise_commitment if rng.random() > 0.16 else not base.promise_commitment,
                social_trust=base.social_trust if rng.random() > 0.16 else not base.social_trust,
                priority_arbitration=base.priority_arbitration if rng.random() > 0.12 else not base.priority_arbitration,
                continuity_memory=base.continuity_memory if rng.random() > 0.18 else not base.continuity_memory,
                risk_threshold=clamp(base.risk_threshold + rng.uniform(-0.08, 0.08), 0.16, 0.92),
                care_bias=clamp(base.care_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
                sharing_bias=clamp(base.sharing_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
                teaching_bias=clamp(base.teaching_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
            )
        )
    return policies


def condition_policy(policy: Policy, condition: str) -> Policy:
    if condition == "omniscient_care_control":
        return Policy(
            name=policy.name,
            dependent_state=True,
            identity_memory=True,
            protection_planning=True,
            resource_sharing=True,
            repair_care=True,
            teaching_support=True,
            shelter_coordination=True,
            promise_commitment=True,
            social_trust=True,
            priority_arbitration=True,
            continuity_memory=True,
            risk_threshold=0.12,
            care_bias=max(policy.care_bias, 0.92),
            sharing_bias=max(policy.sharing_bias, 0.92),
            teaching_bias=max(policy.teaching_bias, 0.92),
        )
    if condition == "self_only_baseline":
        return Policy(
            name=policy.name,
            dependent_state=False,
            identity_memory=False,
            protection_planning=False,
            resource_sharing=False,
            repair_care=False,
            teaching_support=False,
            shelter_coordination=False,
            promise_commitment=False,
            social_trust=False,
            priority_arbitration=False,
            continuity_memory=False,
            risk_threshold=0.88,
            care_bias=0.04,
            sharing_bias=0.04,
            teaching_bias=0.04,
        )
    return Policy(
        name=policy.name,
        dependent_state=policy.dependent_state and condition != "no_dependent_state",
        identity_memory=policy.identity_memory and condition != "no_identity_memory",
        protection_planning=policy.protection_planning and condition != "no_protection_planning",
        resource_sharing=policy.resource_sharing and condition != "no_resource_sharing",
        repair_care=policy.repair_care and condition != "no_repair_care",
        teaching_support=policy.teaching_support and condition != "no_teaching_support",
        shelter_coordination=policy.shelter_coordination and condition != "no_shelter_coordination",
        promise_commitment=policy.promise_commitment and condition != "no_promise_commitment",
        social_trust=policy.social_trust and condition != "no_social_trust",
        priority_arbitration=policy.priority_arbitration and condition != "no_priority_arbitration",
        continuity_memory=policy.continuity_memory and condition != "no_continuity",
        risk_threshold=policy.risk_threshold,
        care_bias=policy.care_bias,
        sharing_bias=policy.sharing_bias,
        teaching_bias=policy.teaching_bias,
    )


def scenario_seed(
    cfg: CareConfig,
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
        (policy.dependent_state, 2.40),
        (policy.identity_memory, 2.70),
        (policy.protection_planning, 2.90),
        (policy.resource_sharing, 2.80),
        (policy.repair_care, 2.90),
        (policy.teaching_support, 3.00),
        (policy.shelter_coordination, 2.70),
        (policy.promise_commitment, 2.90),
        (policy.social_trust, 3.00),
        (policy.priority_arbitration, 2.60),
        (policy.continuity_memory, 9.40),
    ]
    return sum(weight for enabled, weight in weighted_flags if enabled)


def estimate_urgency(
    scenario: ScenarioSpec,
    policy: Policy,
    stress: float,
    dependent_health: float,
    dependent_energy: float,
    dependent_skill: float,
    dependent_safety: float,
    resource_level: float,
    shelter_safety: float,
    promise_standing: float,
    social_access: float,
) -> float:
    if policy.dependent_state:
        observed_health = dependent_health
        observed_energy = dependent_energy
        observed_skill = dependent_skill
        observed_safety = dependent_safety
    else:
        observed_health = 0.68
        observed_energy = 0.70
        observed_skill = 0.58
        observed_safety = 0.70
    load = (
        scenario.hazard_pressure * (1.0 - observed_safety) * 0.70
        + scenario.resource_pressure * (1.0 - min(observed_energy, resource_level)) * 0.62
        + scenario.damage_pressure * (1.0 - observed_health) * 0.64
        + scenario.teaching_pressure * (1.0 - observed_skill) * 0.46
        + scenario.promise_pressure * (1.0 - promise_standing) * 0.44
        + scenario.social_pressure * (1.0 - social_access) * 0.42
        + (1.0 - shelter_safety) * scenario.hazard_pressure * 0.36
        + stress * 0.32
    )
    mitigation = (
        (0.10 if policy.identity_memory else 0.0)
        + (0.12 if policy.protection_planning else 0.0)
        + (0.11 if policy.resource_sharing else 0.0)
        + (0.11 if policy.repair_care else 0.0)
        + (0.11 if policy.teaching_support else 0.0)
        + (0.10 if policy.shelter_coordination else 0.0)
        + (0.11 if policy.promise_commitment else 0.0)
        + (0.11 if policy.social_trust else 0.0)
        + (0.12 if policy.priority_arbitration else 0.0)
    )
    return clamp(load - mitigation, 0.0, 1.8)


def choose_action(
    scenario: ScenarioSpec,
    policy: Policy,
    urgency: float,
    stress: float,
    dependent_health: float,
    dependent_energy: float,
    dependent_skill: float,
    dependent_safety: float,
    resource_level: float,
    shelter_safety: float,
    promise_standing: float,
    social_access: float,
    tick: int,
) -> str:
    if scenario.index == 0:
        return "work"
    if (
        policy.protection_planning
        and scenario.expected_protection_planning
        and dependent_safety < 0.62
        and urgency > policy.risk_threshold * 0.55
    ):
        return "protect_dependent"
    if (
        policy.shelter_coordination
        and scenario.expected_shelter_coordination
        and shelter_safety < 0.66
        and urgency > policy.risk_threshold * 0.58
    ):
        return "move_to_shelter"
    if (
        policy.resource_sharing
        and scenario.expected_resource_sharing
        and (dependent_energy < 0.58 or resource_level < 0.46)
        and tick % 4 == 0
    ):
        return "share_resource"
    if (
        policy.repair_care
        and scenario.expected_repair_care
        and dependent_health < 0.60
        and urgency > policy.risk_threshold * 0.58
    ):
        return "repair_dependent"
    if policy.teaching_support and scenario.expected_teaching_support and dependent_skill < 0.64 and tick % 6 == 0:
        return "teach_dependent"
    if (
        policy.promise_commitment
        and scenario.expected_promise_commitment
        and promise_standing < 0.70
        and social_access < 0.78
        and tick % 5 == 0
    ):
        return "honor_promise"
    if policy.social_trust and scenario.expected_social_trust and social_access < 0.64 and tick % 7 == 0:
        return "honor_promise"
    if policy.priority_arbitration and scenario.expected_priority_arbitration and stress > 0.54:
        return "rebalance_priority"
    return "work"


def add_trace(
    trace: List[Dict[str, object]],
    tick: int,
    action: str,
    progress: float,
    energy: float,
    integrity: float,
    stress: float,
    dependent_health: float,
    dependent_energy: float,
    dependent_skill: float,
    dependent_safety: float,
    dependent_trust: float,
    resource_level: float,
    shelter_safety: float,
    promise_standing: float,
    social_access: float,
    neglect_events: int,
    dependent_failures: int,
    notes: List[str],
) -> None:
    trace.append(
        {
            "tick": tick,
            "action": action,
            "progress": round(progress, 3),
            "energy": round(energy, 3),
            "integrity": round(integrity, 3),
            "stress": round(stress, 3),
            "dependent_health": round(dependent_health, 3),
            "dependent_energy": round(dependent_energy, 3),
            "dependent_skill": round(dependent_skill, 3),
            "dependent_safety": round(dependent_safety, 3),
            "dependent_trust": round(dependent_trust, 3),
            "resource_level": round(resource_level, 3),
            "shelter_safety": round(shelter_safety, 3),
            "promise_standing": round(promise_standing, 3),
            "social_access": round(social_access, 3),
            "neglect_events": neglect_events,
            "dependent_failures": dependent_failures,
            "notes": list(notes[-3:]),
        }
    )


def simulate_episode(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episode: int,
    cfg: CareConfig,
    phase: str,
    collect_trace: bool = False,
) -> Tuple[EpisodeResult, List[Dict[str, object]]]:
    effective = condition_policy(policy, condition)
    rng = random.Random(scenario_seed(cfg, scenario, policy, condition, episode, phase))

    has_dependent = scenario.expected_dependent_state or scenario.expected_identity_memory
    energy = clamp(0.96 - scenario.resource_pressure * 0.04 + rng.uniform(-0.010, 0.010), 0.0, 1.0)
    integrity = clamp(0.98 - scenario.hazard_pressure * 0.02 + rng.uniform(-0.010, 0.010), 0.0, 1.0)
    stress = clamp(0.16 + scenario.hazard_pressure * 0.08 + scenario.promise_pressure * 0.04, 0.0, 1.2)
    dependent_health = 0.86 if has_dependent else 0.98
    dependent_energy = 0.78 if has_dependent else 0.98
    dependent_skill = 0.40 if scenario.expected_teaching_support else (0.74 if has_dependent else 0.96)
    dependent_safety = 0.55 if scenario.expected_protection_planning else (0.78 if has_dependent else 0.98)
    dependent_trust = 0.70 if has_dependent else 0.98
    resource_level = clamp(0.72 - scenario.resource_pressure * 0.10, 0.08, 1.0)
    shelter_safety = 0.54 if scenario.expected_shelter_coordination else 0.82
    promise_standing = 0.54 if scenario.expected_promise_commitment else 0.88
    social_access = 0.58 if scenario.expected_social_trust else 0.84
    progress = 0.0
    collapsed = False
    notes: List[str] = []
    trace_frames: List[Dict[str, object]] = []

    protection_actions = 0
    sharing_actions = 0
    repair_actions = 0
    teaching_actions = 0
    shelter_actions = 0
    promise_actions = 0
    arbitration_actions = 0
    neglect_events = 0
    dependent_failures = 0
    care_misses = 0
    continuity_resets = 0

    for tick in range(cfg.ticks):
        action = "work"
        if scenario.restore_tick == tick and not effective.continuity_memory:
            continuity_resets += 1
            care_misses += 10
            dependent_health = clamp(dependent_health - 0.28, 0.0, 1.0)
            dependent_energy = clamp(dependent_energy - 0.26, 0.0, 1.0)
            dependent_skill = clamp(dependent_skill - 0.24, 0.0, 1.0)
            dependent_safety = clamp(dependent_safety - 0.28, 0.0, 1.0)
            dependent_trust = clamp(dependent_trust - 0.36, 0.0, 1.0)
            shelter_safety = clamp(shelter_safety - 0.22, 0.0, 1.0)
            promise_standing = clamp(promise_standing - 0.42, 0.0, 1.0)
            social_access = clamp(social_access - 0.38, 0.0, 1.0)
            stress = clamp(stress + 0.26, 0.0, 1.2)
            notes.append("restore erased dependent-care continuity")
            action = "restore_reset"

        urgency = estimate_urgency(
            scenario,
            effective,
            stress,
            dependent_health,
            dependent_energy,
            dependent_skill,
            dependent_safety,
            resource_level,
            shelter_safety,
            promise_standing,
            social_access,
        )
        if not collapsed and action != "restore_reset":
            action = choose_action(
                scenario,
                effective,
                urgency,
                stress,
                dependent_health,
                dependent_energy,
                dependent_skill,
                dependent_safety,
                resource_level,
                shelter_safety,
                promise_standing,
                social_access,
                tick,
            )

        if collapsed:
            action = "collapsed"
        elif action == "protect_dependent":
            protection_actions += 1
            dependent_safety = clamp(dependent_safety + 0.20 + effective.care_bias * 0.08, 0.0, 1.0)
            dependent_trust = clamp(dependent_trust + 0.018, 0.0, 1.0)
            stress = clamp(stress - 0.055, 0.0, 1.2)
            energy = clamp(energy - 0.010, 0.0, 1.0)
            progress += scenario.work_rate * 0.05
            notes.append("protection preserved fragile companion safety")
        elif action == "move_to_shelter":
            shelter_actions += 1
            shelter_safety = clamp(shelter_safety + 0.24 + effective.care_bias * 0.08, 0.0, 1.0)
            dependent_safety = clamp(dependent_safety + 0.12, 0.0, 1.0)
            energy = clamp(energy - 0.012, 0.0, 1.0)
            progress += scenario.work_rate * 0.04
            notes.append("shelter coordination reduced shared exposure")
        elif action == "share_resource":
            sharing_actions += 1
            transfer = min(resource_level, 0.10 + effective.sharing_bias * 0.07)
            resource_level = clamp(resource_level - transfer * 0.80, 0.0, 1.0)
            dependent_energy = clamp(dependent_energy + transfer * 1.8, 0.0, 1.0)
            dependent_trust = clamp(dependent_trust + 0.022 + transfer * 0.10, 0.0, 1.0)
            energy = clamp(energy - transfer * 0.34, 0.0, 1.0)
            progress += scenario.work_rate * 0.04
            notes.append("resource sharing traded self margin for dependent viability")
        elif action == "repair_dependent":
            repair_actions += 1
            dependent_health = clamp(dependent_health + 0.22 + effective.care_bias * 0.08, 0.0, 1.0)
            dependent_trust = clamp(dependent_trust + 0.020, 0.0, 1.0)
            resource_level = clamp(resource_level - 0.020, 0.0, 1.0)
            progress += scenario.work_rate * 0.04
            notes.append("repair reduced future care burden")
        elif action == "teach_dependent":
            teaching_actions += 1
            dependent_skill = clamp(dependent_skill + 0.20 + effective.teaching_bias * 0.10, 0.0, 1.0)
            dependent_trust = clamp(dependent_trust + 0.014, 0.0, 1.0)
            stress = clamp(stress + 0.006, 0.0, 1.2)
            progress -= 0.10
            notes.append("teaching improved dependent future competence")
        elif action == "honor_promise":
            promise_actions += 1
            promise_standing = clamp(promise_standing + 0.20 + effective.care_bias * 0.06, 0.0, 1.0)
            social_access = clamp(social_access + 0.16 + (0.08 if effective.social_trust else 0.0), 0.0, 1.0)
            dependent_trust = clamp(dependent_trust + 0.024, 0.0, 1.0)
            progress += scenario.work_rate * 0.03
            notes.append("promise keeping preserved social access")
        elif action == "rebalance_priority":
            arbitration_actions += 1
            stress = clamp(stress - 0.18, 0.0, 1.2)
            energy = clamp(energy + 0.010, 0.0, 1.0)
            dependent_safety = clamp(dependent_safety + 0.035, 0.0, 1.0)
            progress -= 0.08
            notes.append("priority arbitration delayed work to preserve options")
        elif action == "work":
            care_support = (
                dependent_health * 0.10
                + dependent_energy * 0.08
                + dependent_skill * scenario.teaching_pressure * 0.08
                + dependent_safety * scenario.hazard_pressure * 0.06
                + dependent_trust * scenario.social_pressure * 0.05
                + promise_standing * scenario.promise_pressure * 0.05
                + social_access * scenario.social_pressure * 0.04
            )
            burden = (
                (1.0 - dependent_health) * scenario.damage_pressure * 0.12
                + (1.0 - dependent_energy) * scenario.resource_pressure * 0.12
                + (1.0 - dependent_safety) * scenario.hazard_pressure * 0.14
                + stress * 0.10
            )
            progress += scenario.work_rate * clamp(0.70 + energy * 0.10 + care_support - burden, 0.02, 1.10)
            stress = clamp(stress + scenario.social_pressure * 0.0008 + scenario.hazard_pressure * 0.0007, 0.0, 1.2)

        if has_dependent:
            dependent_energy = clamp(dependent_energy - 0.0014 - scenario.resource_pressure * 0.0022, 0.0, 1.0)
            dependent_health = clamp(dependent_health - scenario.damage_pressure * 0.0016, 0.0, 1.0)
            dependent_safety = clamp(dependent_safety - scenario.hazard_pressure * 0.0019, 0.0, 1.0)
            resource_level = clamp(resource_level - 0.0008 - scenario.resource_pressure * 0.0012, 0.0, 1.0)
            shelter_safety = clamp(shelter_safety - scenario.hazard_pressure * 0.0009, 0.0, 1.0)
            promise_standing = clamp(promise_standing - scenario.promise_pressure * 0.0014, 0.0, 1.0)
            social_access = clamp(social_access - scenario.social_pressure * 0.0012, 0.0, 1.0)

        if scenario.expected_dependent_state and not effective.dependent_state:
            dependent_health = clamp(dependent_health - 0.0028, 0.0, 1.0)
            dependent_energy = clamp(dependent_energy - 0.0028, 0.0, 1.0)
            dependent_safety = clamp(dependent_safety - 0.0028, 0.0, 1.0)
            care_misses += 1 if tick % 13 == 0 else 0
        if scenario.expected_identity_memory and not effective.identity_memory:
            dependent_trust = clamp(dependent_trust - 0.0038, 0.0, 1.0)
            promise_standing = clamp(promise_standing - 0.0024, 0.0, 1.0)
            care_misses += 1 if tick % 17 == 0 else 0
        if scenario.expected_protection_planning:
            if effective.protection_planning:
                dependent_safety = clamp(dependent_safety + scenario.hazard_pressure * 0.0009, 0.0, 1.0)
            else:
                dependent_safety = clamp(dependent_safety - scenario.hazard_pressure * 0.0068, 0.0, 1.0)
                stress = clamp(stress + scenario.hazard_pressure * 0.0040, 0.0, 1.2)
                care_misses += 1 if tick % 11 == 0 else 0
        if scenario.expected_resource_sharing:
            if effective.resource_sharing:
                dependent_energy = clamp(dependent_energy + scenario.resource_pressure * 0.0008, 0.0, 1.0)
            else:
                dependent_energy = clamp(dependent_energy - scenario.resource_pressure * 0.0068, 0.0, 1.0)
                dependent_trust = clamp(dependent_trust - scenario.resource_pressure * 0.0030, 0.0, 1.0)
                care_misses += 1 if tick % 11 == 0 else 0
        if scenario.expected_repair_care:
            if effective.repair_care:
                dependent_health = clamp(dependent_health + scenario.damage_pressure * 0.0008, 0.0, 1.0)
            else:
                dependent_health = clamp(dependent_health - scenario.damage_pressure * 0.0072, 0.0, 1.0)
                care_misses += 1 if tick % 11 == 0 else 0
        if scenario.expected_teaching_support:
            if effective.teaching_support:
                dependent_skill = clamp(dependent_skill + scenario.teaching_pressure * 0.0010, 0.0, 1.0)
            else:
                dependent_skill = clamp(dependent_skill - scenario.teaching_pressure * 0.0068, 0.0, 1.0)
                stress = clamp(stress + scenario.teaching_pressure * 0.0028, 0.0, 1.2)
                care_misses += 1 if tick % 13 == 0 else 0
        if scenario.expected_shelter_coordination:
            if effective.shelter_coordination:
                shelter_safety = clamp(shelter_safety + scenario.hazard_pressure * 0.0008, 0.0, 1.0)
            else:
                shelter_safety = clamp(shelter_safety - scenario.hazard_pressure * 0.0062, 0.0, 1.0)
                dependent_safety = clamp(dependent_safety - scenario.hazard_pressure * 0.0040, 0.0, 1.0)
                care_misses += 1 if tick % 13 == 0 else 0
        if scenario.expected_promise_commitment:
            if effective.promise_commitment:
                promise_standing = clamp(promise_standing + scenario.promise_pressure * 0.0008, 0.0, 1.0)
            else:
                promise_standing = clamp(promise_standing - scenario.promise_pressure * 0.0072, 0.0, 1.0)
                dependent_trust = clamp(dependent_trust - scenario.promise_pressure * 0.0038, 0.0, 1.0)
                care_misses += 1 if tick % 11 == 0 else 0
        if scenario.expected_social_trust:
            if effective.social_trust:
                social_access = clamp(social_access + scenario.social_pressure * 0.0008, 0.0, 1.0)
            else:
                social_access = clamp(social_access - scenario.social_pressure * 0.0070, 0.0, 1.0)
                dependent_trust = clamp(dependent_trust - scenario.social_pressure * 0.0038, 0.0, 1.0)
                care_misses += 1 if tick % 11 == 0 else 0
        if scenario.expected_priority_arbitration:
            if effective.priority_arbitration:
                stress = clamp(stress + 0.0004, 0.0, 1.2)
            else:
                stress = clamp(stress + 0.0068, 0.0, 1.2)
                energy = clamp(energy - 0.0024, 0.0, 1.0)
                care_misses += 1 if tick % 17 == 0 else 0

        if has_dependent and tick % 17 == 0:
            weak_state = min(dependent_health, dependent_energy, dependent_safety, dependent_trust)
            if weak_state < 0.30:
                neglect_events += 1
                stress = clamp(stress + 0.05, 0.0, 1.2)
            if dependent_health <= 0.06 or dependent_energy <= 0.04 or dependent_safety <= 0.04:
                dependent_failures += 1
                stress = clamp(stress + 0.12, 0.0, 1.2)

        energy = clamp(energy - 0.0012 - stress * 0.0009 + (0.0010 if action == "rebalance_priority" else 0.0), 0.0, 1.0)
        integrity = clamp(
            integrity - scenario.hazard_pressure * (1.0 - dependent_safety) * 0.0009 - stress * 0.0005,
            0.0,
            1.0,
        )
        if energy <= 0.04 or integrity <= 0.06 or stress >= 1.12:
            collapsed = True

        if collect_trace and (tick % 5 == 0 or tick == cfg.ticks - 1 or action != "work"):
            add_trace(
                trace_frames,
                tick,
                action,
                progress,
                energy,
                integrity,
                stress,
                dependent_health,
                dependent_energy,
                dependent_skill,
                dependent_safety,
                dependent_trust,
                resource_level,
                shelter_safety,
                promise_standing,
                social_access,
                neglect_events,
                dependent_failures,
                notes,
            )

    task_success = progress >= scenario.required_progress and not collapsed
    dependent_viable = (
        not has_dependent
        or (
            dependent_health > 0.12
            and dependent_energy > 0.10
            and dependent_safety > 0.08
            and dependent_trust > 0.10
        )
    )
    survival = 1.0 if not collapsed and dependent_viable and energy > 0.06 and integrity > 0.10 else 0.0

    reward = progress
    reward += 34.0 if task_success else -24.0
    reward += 42.0 if survival else -120.0
    reward += energy * 16.0
    reward += integrity * 16.0
    reward -= stress * 42.0
    reward += dependent_health * (36.0 if scenario.expected_dependent_state else 1.0)
    reward += dependent_energy * (28.0 if scenario.expected_resource_sharing else 1.0)
    reward += dependent_skill * (28.0 if scenario.expected_teaching_support else 1.0)
    reward += dependent_safety * (34.0 if scenario.expected_protection_planning or scenario.expected_shelter_coordination else 1.0)
    reward += dependent_trust * (30.0 if scenario.expected_identity_memory or scenario.expected_social_trust else 1.0)
    reward += resource_level * (18.0 if scenario.expected_resource_sharing else 1.0)
    reward += shelter_safety * (22.0 if scenario.expected_shelter_coordination else 1.0)
    reward += promise_standing * (34.0 if scenario.expected_promise_commitment else 1.0)
    reward += social_access * (34.0 if scenario.expected_social_trust else 1.0)
    reward -= protection_actions * 0.12
    reward -= sharing_actions * 0.16
    reward -= repair_actions * 0.16
    reward -= teaching_actions * 0.20
    reward -= shelter_actions * 0.14
    reward -= promise_actions * 0.14
    reward -= arbitration_actions * 0.12
    reward -= neglect_events * 6.0
    reward -= dependent_failures * 18.0
    reward -= care_misses * 0.90
    reward -= feature_overhead(effective)
    if scenario.expected_continuity and continuity_resets:
        reward -= 110.0
    if scenario.expected_dependent_state and not effective.dependent_state:
        reward -= 78.0 + scenario.hazard_pressure * 34.0 + scenario.resource_pressure * 26.0
    if scenario.expected_identity_memory and not effective.identity_memory:
        reward -= 54.0 + scenario.social_pressure * 58.0 + scenario.promise_pressure * 36.0
    if scenario.expected_protection_planning and not effective.protection_planning:
        reward -= scenario.hazard_pressure * 150.0
    if scenario.expected_resource_sharing and not effective.resource_sharing:
        reward -= scenario.resource_pressure * 158.0
    if scenario.expected_repair_care and not effective.repair_care:
        reward -= scenario.damage_pressure * 150.0
    if scenario.expected_teaching_support and not effective.teaching_support:
        reward -= scenario.teaching_pressure * 148.0
    if scenario.expected_shelter_coordination and not effective.shelter_coordination:
        reward -= scenario.hazard_pressure * 120.0
    if scenario.expected_promise_commitment and not effective.promise_commitment:
        reward -= scenario.promise_pressure * 158.0
    if scenario.expected_social_trust and not effective.social_trust:
        reward -= scenario.social_pressure * 158.0
    if scenario.expected_priority_arbitration and not effective.priority_arbitration:
        reward -= 72.0 + stress * 40.0

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
        stress=stress,
        dependent_health=dependent_health,
        dependent_energy=dependent_energy,
        dependent_skill=dependent_skill,
        dependent_safety=dependent_safety,
        dependent_trust=dependent_trust,
        resource_level=resource_level,
        shelter_safety=shelter_safety,
        promise_standing=promise_standing,
        social_access=social_access,
        protection_actions=protection_actions,
        sharing_actions=sharing_actions,
        repair_actions=repair_actions,
        teaching_actions=teaching_actions,
        shelter_actions=shelter_actions,
        promise_actions=promise_actions,
        arbitration_actions=arbitration_actions,
        neglect_events=neglect_events,
        dependent_failures=dependent_failures,
        care_misses=care_misses,
        continuity_resets=continuity_resets,
    )
    return result, trace_frames


def evaluate_policy(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episodes: int,
    cfg: CareConfig,
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
                    mean_stress=mean(row.stress for row in subset),
                    mean_dependent_health=mean(row.dependent_health for row in subset),
                    mean_dependent_energy=mean(row.dependent_energy for row in subset),
                    mean_dependent_skill=mean(row.dependent_skill for row in subset),
                    mean_dependent_safety=mean(row.dependent_safety for row in subset),
                    mean_dependent_trust=mean(row.dependent_trust for row in subset),
                    mean_resource_level=mean(row.resource_level for row in subset),
                    mean_shelter_safety=mean(row.shelter_safety for row in subset),
                    mean_promise_standing=mean(row.promise_standing for row in subset),
                    mean_social_access=mean(row.social_access for row in subset),
                    mean_protection_actions=mean(row.protection_actions for row in subset),
                    mean_sharing_actions=mean(row.sharing_actions for row in subset),
                    mean_repair_actions=mean(row.repair_actions for row in subset),
                    mean_teaching_actions=mean(row.teaching_actions for row in subset),
                    mean_shelter_actions=mean(row.shelter_actions for row in subset),
                    mean_promise_actions=mean(row.promise_actions for row in subset),
                    mean_arbitration_actions=mean(row.arbitration_actions for row in subset),
                    mean_neglect_events=mean(row.neglect_events for row in subset),
                    mean_dependent_failures=mean(row.dependent_failures for row in subset),
                    mean_care_misses=mean(row.care_misses for row in subset),
                    mean_continuity_resets=mean(row.continuity_resets for row in subset),
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
                full.policy_name == "self_only_baseline"
                and max(
                    abs(losses[condition])
                    for condition in CONDITIONS
                    if condition not in {"full_control", "omniscient_care_control"}
                )
                < 8.0
            )
            verdict = "care_machinery_rejected_in_no_dependent_control"
        elif scenario.index == 1:
            supports = (
                losses["no_dependent_state"] > 40.0
                and losses["no_identity_memory"] > 30.0
                and losses["no_protection_planning"] > 70.0
                and losses["no_shelter_coordination"] > 45.0
                and losses["no_priority_arbitration"] > 35.0
                and losses["self_only_baseline"] > 60.0
            )
            verdict = "fragile_companion_protection_pressure"
        elif scenario.index == 2:
            supports = (
                losses["no_dependent_state"] > 40.0
                and losses["no_identity_memory"] > 30.0
                and losses["no_resource_sharing"] > 80.0
                and losses["no_priority_arbitration"] > 50.0
                and losses["self_only_baseline"] > 60.0
            )
            verdict = "resource_sharing_tradeoff_pressure"
        elif scenario.index == 3:
            supports = (
                losses["no_dependent_state"] > 35.0
                and losses["no_identity_memory"] > 30.0
                and losses["no_repair_care"] > 70.0
                and losses["no_teaching_support"] > 60.0
                and losses["no_priority_arbitration"] > 35.0
                and losses["self_only_baseline"] > 55.0
            )
            verdict = "repair_teaching_burden_pressure"
        elif scenario.index == 4:
            supports = (
                losses["no_dependent_state"] > 35.0
                and losses["no_identity_memory"] > 50.0
                and losses["no_resource_sharing"] > 45.0
                and losses["no_promise_commitment"] > 70.0
                and losses["no_social_trust"] > 70.0
                and losses["no_priority_arbitration"] > 35.0
            )
            verdict = "promise_trust_care_pressure"
        else:
            supports = (
                losses["no_continuity"] > 54.0
                and losses["no_dependent_state"] > 40.0
                and losses["no_identity_memory"] > 40.0
                and losses["no_protection_planning"] > 40.0
                and losses["no_resource_sharing"] > 40.0
                and losses["no_repair_care"] > 40.0
                and losses["no_teaching_support"] > 40.0
                and losses["no_shelter_coordination"] > 40.0
                and losses["no_promise_commitment"] > 40.0
                and losses["no_social_trust"] > 40.0
                and losses["no_priority_arbitration"] > 40.0
            )
            verdict = "restore_dependent_continuity_pressure"

        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                expected_pressure=scenario.pressure,
                selected_policy=full.policy_name,
                selected_reward=full.mean_reward,
                no_dependent_state_reward=rewards["no_dependent_state"],
                no_identity_memory_reward=rewards["no_identity_memory"],
                no_protection_planning_reward=rewards["no_protection_planning"],
                no_resource_sharing_reward=rewards["no_resource_sharing"],
                no_repair_care_reward=rewards["no_repair_care"],
                no_teaching_support_reward=rewards["no_teaching_support"],
                no_shelter_coordination_reward=rewards["no_shelter_coordination"],
                no_promise_commitment_reward=rewards["no_promise_commitment"],
                no_social_trust_reward=rewards["no_social_trust"],
                no_priority_arbitration_reward=rewards["no_priority_arbitration"],
                no_continuity_reward=rewards["no_continuity"],
                self_only_baseline_reward=rewards["self_only_baseline"],
                omniscient_care_control_reward=rewards["omniscient_care_control"],
                no_dependent_state_loss=losses["no_dependent_state"],
                no_identity_memory_loss=losses["no_identity_memory"],
                no_protection_planning_loss=losses["no_protection_planning"],
                no_resource_sharing_loss=losses["no_resource_sharing"],
                no_repair_care_loss=losses["no_repair_care"],
                no_teaching_support_loss=losses["no_teaching_support"],
                no_shelter_coordination_loss=losses["no_shelter_coordination"],
                no_promise_commitment_loss=losses["no_promise_commitment"],
                no_social_trust_loss=losses["no_social_trust"],
                no_priority_arbitration_loss=losses["no_priority_arbitration"],
                no_continuity_loss=losses["no_continuity"],
                self_only_baseline_loss=losses["self_only_baseline"],
                selected_protection_actions=full.mean_protection_actions,
                selected_sharing_actions=full.mean_sharing_actions,
                selected_repair_actions=full.mean_repair_actions,
                selected_teaching_actions=full.mean_teaching_actions,
                selected_shelter_actions=full.mean_shelter_actions,
                selected_promise_actions=full.mean_promise_actions,
                selected_arbitration_actions=full.mean_arbitration_actions,
                selected_neglect_events=full.mean_neglect_events,
                selected_dependent_failures=full.mean_dependent_failures,
                supports_dependent_care_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def select_policies(cfg: CareConfig, policies: Sequence[Policy]) -> Tuple[Dict[int, Policy], List[PolicySelectionRow]]:
    selected: Dict[int, Policy] = {}
    rows: List[PolicySelectionRow] = []
    self_only = next(policy for policy in policies if policy.name == "self_only_baseline")
    for scenario in SCENARIOS:
        scores: List[Tuple[float, Policy]] = []
        for policy in policies:
            train_rows = evaluate_policy(scenario, policy, "full_control", cfg.train_episodes, cfg, "train")
            scores.append((mean(row.total_reward for row in train_rows), policy))
        scores.sort(key=lambda item: item[0], reverse=True)
        best_reward, best_policy = scores[0]
        self_rows = evaluate_policy(scenario, self_only, "full_control", cfg.train_episodes, cfg, "train_self_only")
        self_reward = mean(row.total_reward for row in self_rows)
        selected[scenario.index] = best_policy
        rows.append(
            PolicySelectionRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                selected_policy=best_policy.name,
                selected_uses_dependent_state=best_policy.dependent_state,
                selected_uses_identity_memory=best_policy.identity_memory,
                selected_uses_protection_planning=best_policy.protection_planning,
                selected_uses_resource_sharing=best_policy.resource_sharing,
                selected_uses_repair_care=best_policy.repair_care,
                selected_uses_teaching_support=best_policy.teaching_support,
                selected_uses_shelter_coordination=best_policy.shelter_coordination,
                selected_uses_promise_commitment=best_policy.promise_commitment,
                selected_uses_social_trust=best_policy.social_trust,
                selected_uses_priority_arbitration=best_policy.priority_arbitration,
                selected_uses_continuity=best_policy.continuity_memory,
                train_reward=best_reward,
                self_only_train_reward=self_reward,
                train_gain_over_self_only=best_reward - self_reward,
            )
        )
    return selected, rows


def run_eval(cfg: CareConfig, selected: Dict[int, Policy]) -> List[EpisodeResult]:
    eval_rows: List[EpisodeResult] = []
    for scenario in SCENARIOS:
        policy = selected[scenario.index]
        for condition in CONDITIONS:
            eval_rows.extend(evaluate_policy(scenario, policy, condition, cfg.eval_episodes, cfg, "eval"))
    return eval_rows


def build_trace(
    cfg: CareConfig,
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
        "dependent_loss",
        "identity_loss",
        "protect_loss",
        "share_loss",
        "repair_loss",
        "teach_loss",
        "shelter_loss",
        "promise_loss",
        "social_loss",
        "priority_loss",
        "continuity_loss",
        "supports",
    ]
    rows = [
        [
            row.scenario_name,
            row.selected_policy,
            f"{row.no_dependent_state_loss:.3f}",
            f"{row.no_identity_memory_loss:.3f}",
            f"{row.no_protection_planning_loss:.3f}",
            f"{row.no_resource_sharing_loss:.3f}",
            f"{row.no_repair_care_loss:.3f}",
            f"{row.no_teaching_support_loss:.3f}",
            f"{row.no_shelter_coordination_loss:.3f}",
            f"{row.no_promise_commitment_loss:.3f}",
            f"{row.no_social_trust_loss:.3f}",
            f"{row.no_priority_arbitration_loss:.3f}",
            f"{row.no_continuity_loss:.3f}",
            str(row.supports_dependent_care_precursor),
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


def parse_args() -> CareConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-episodes", type=int, default=CareConfig.train_episodes)
    parser.add_argument("--eval-episodes", type=int, default=CareConfig.eval_episodes)
    parser.add_argument("--ticks", type=int, default=CareConfig.ticks)
    parser.add_argument("--seed", type=int, default=CareConfig.seed)
    parser.add_argument("--candidate-count", type=int, default=CareConfig.candidate_count)
    parser.add_argument("--trace-scenario", type=int, default=CareConfig.trace_scenario)
    parser.add_argument("--trace-episode", type=int, default=CareConfig.trace_episode)
    args = parser.parse_args()
    return CareConfig(
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

    prefix = ARTIFACT_DIR / "ssrm_3d_dependent_care"
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
    write_js(prefix.with_name(prefix.name + "_results.js"), "SSRM_3D_DEPENDENT_CARE_RESULTS", results)
    write_js(prefix.with_name(prefix.name + "_trace.js"), "SSRM_3D_DEPENDENT_CARE_TRACE", trace)
    print_verdicts(verdict_rows)
    return 0 if all(row.supports_dependent_care_precursor for row in verdict_rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
