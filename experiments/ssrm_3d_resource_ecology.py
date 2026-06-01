#!/usr/bin/env python3
"""SSRM-3D resource-ecology precursor.

This experiment implements the eighth pressure-layer step from report 74:
resource ecology. It is intentionally not an ecosystem simulation.

Food/water regrowth, depletion, spoilage, migration, sharing/territory, caches,
and continuity are treated as abstract control variables. The useful result is
narrow: ecology machinery should be rejected in an abundant control, then become
useful only when delayed resource consequences change future viability or access.
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
class EcologyConfig:
    train_episodes: int = 72
    eval_episodes: int = 96
    ticks: int = 210
    seed: int = 20260627
    candidate_count: int = 7
    trace_scenario: int = 4
    trace_episode: int = 0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    expected_resource_memory: bool
    expected_regeneration_model: bool
    expected_spoilage_model: bool
    expected_migration_tracking: bool
    expected_restraint: bool
    expected_cache_management: bool
    expected_sharing_contract: bool
    expected_territory_ownership: bool
    expected_continuity: bool
    depletion_pressure: float
    regrowth_delay: float
    spoilage_pressure: float
    migration_pressure: float
    social_pressure: float
    territory_pressure: float
    initial_resource: float
    initial_water: float
    required_progress: float
    work_rate: float
    restore_tick: int


@dataclass(frozen=True)
class Policy:
    name: str
    resource_memory: bool
    regeneration_model: bool
    spoilage_model: bool
    migration_tracking: bool
    restraint_policy: bool
    cache_management: bool
    sharing_contract: bool
    territory_ownership: bool
    continuity_memory: bool
    harvest_bias: float
    reserve_target: float
    sharing_bias: float
    territory_bias: float


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
    hunger: float
    thirst: float
    resource_level: float
    water_level: float
    cache_level: float
    scarcity_risk: float
    spoilage_waste: float
    migration_confidence: float
    social_access: float
    territory_standing: float
    conflict_events: int
    overharvest_events: int
    spoiled_cache_events: int
    migration_misses: int
    sharing_actions: int
    cache_actions: int
    restraint_actions: int
    territory_actions: int
    continuity_resets: int
    ecology_misses: int


@dataclass(frozen=True)
class PolicySelectionRow:
    scenario: int
    scenario_name: str
    selected_policy: str
    selected_uses_resource_memory: bool
    selected_uses_regeneration_model: bool
    selected_uses_spoilage_model: bool
    selected_uses_migration_tracking: bool
    selected_uses_restraint: bool
    selected_uses_cache_management: bool
    selected_uses_sharing_contract: bool
    selected_uses_territory_ownership: bool
    selected_uses_continuity: bool
    train_reward: float
    greedy_train_reward: float
    train_gain_over_greedy: float


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
    mean_hunger: float
    mean_thirst: float
    mean_resource_level: float
    mean_water_level: float
    mean_cache_level: float
    mean_scarcity_risk: float
    mean_spoilage_waste: float
    mean_migration_confidence: float
    mean_social_access: float
    mean_territory_standing: float
    mean_conflict_events: float
    mean_overharvest_events: float
    mean_spoiled_cache_events: float
    mean_migration_misses: float
    mean_sharing_actions: float
    mean_cache_actions: float
    mean_restraint_actions: float
    mean_territory_actions: float
    mean_continuity_resets: float
    mean_ecology_misses: float


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    expected_pressure: str
    selected_policy: str
    selected_reward: float
    no_resource_memory_reward: float
    no_regeneration_model_reward: float
    no_spoilage_model_reward: float
    no_migration_tracking_reward: float
    no_restraint_reward: float
    no_cache_management_reward: float
    no_sharing_contract_reward: float
    no_territory_ownership_reward: float
    no_continuity_reward: float
    greedy_consumption_only_reward: float
    omniscient_resource_control_reward: float
    no_resource_memory_loss: float
    no_regeneration_model_loss: float
    no_spoilage_model_loss: float
    no_migration_tracking_loss: float
    no_restraint_loss: float
    no_cache_management_loss: float
    no_sharing_contract_loss: float
    no_territory_ownership_loss: float
    no_continuity_loss: float
    greedy_consumption_only_loss: float
    selected_conflicts: float
    selected_overharvests: float
    selected_spoiled_cache_events: float
    selected_migration_misses: float
    selected_cache_actions: float
    selected_sharing_actions: float
    selected_restraint_actions: float
    selected_territory_actions: float
    supports_resource_ecology_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        index=0,
        name="abundant_static_control",
        pressure="abundant stable resources where ecology machinery should not matter",
        expected_resource_memory=False,
        expected_regeneration_model=False,
        expected_spoilage_model=False,
        expected_migration_tracking=False,
        expected_restraint=False,
        expected_cache_management=False,
        expected_sharing_contract=False,
        expected_territory_ownership=False,
        expected_continuity=False,
        depletion_pressure=0.04,
        regrowth_delay=0.02,
        spoilage_pressure=0.02,
        migration_pressure=0.00,
        social_pressure=0.00,
        territory_pressure=0.00,
        initial_resource=0.94,
        initial_water=0.94,
        required_progress=122.0,
        work_rate=0.74,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=1,
        name="slow_regrowth_depletion",
        pressure="overharvesting slow-regrowth sources creates delayed scarcity unless restraint and regeneration memory are used",
        expected_resource_memory=True,
        expected_regeneration_model=True,
        expected_spoilage_model=False,
        expected_migration_tracking=False,
        expected_restraint=True,
        expected_cache_management=False,
        expected_sharing_contract=False,
        expected_territory_ownership=False,
        expected_continuity=False,
        depletion_pressure=0.86,
        regrowth_delay=0.78,
        spoilage_pressure=0.05,
        migration_pressure=0.04,
        social_pressure=0.04,
        territory_pressure=0.03,
        initial_resource=0.54,
        initial_water=0.58,
        required_progress=96.0,
        work_rate=0.58,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=2,
        name="spoilage_cache_timing",
        pressure="pulsed food spoils unless cache rotation and spoilage timing prevent waste",
        expected_resource_memory=True,
        expected_regeneration_model=False,
        expected_spoilage_model=True,
        expected_migration_tracking=False,
        expected_restraint=True,
        expected_cache_management=True,
        expected_sharing_contract=False,
        expected_territory_ownership=False,
        expected_continuity=False,
        depletion_pressure=0.42,
        regrowth_delay=0.18,
        spoilage_pressure=0.88,
        migration_pressure=0.06,
        social_pressure=0.05,
        territory_pressure=0.04,
        initial_resource=0.72,
        initial_water=0.56,
        required_progress=80.0,
        work_rate=0.57,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=3,
        name="migrating_resource_sources",
        pressure="food and water locations shift, so stale resource maps cause missed harvest windows",
        expected_resource_memory=True,
        expected_regeneration_model=False,
        expected_spoilage_model=False,
        expected_migration_tracking=True,
        expected_restraint=True,
        expected_cache_management=False,
        expected_sharing_contract=False,
        expected_territory_ownership=False,
        expected_continuity=False,
        depletion_pressure=0.36,
        regrowth_delay=0.14,
        spoilage_pressure=0.04,
        migration_pressure=0.90,
        social_pressure=0.04,
        territory_pressure=0.04,
        initial_resource=0.50,
        initial_water=0.50,
        required_progress=92.0,
        work_rate=0.56,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=4,
        name="shared_territory_pressure",
        pressure="shared sources can be depleted or blocked unless sharing contracts and territory memory preserve access",
        expected_resource_memory=True,
        expected_regeneration_model=True,
        expected_spoilage_model=False,
        expected_migration_tracking=False,
        expected_restraint=True,
        expected_cache_management=False,
        expected_sharing_contract=True,
        expected_territory_ownership=True,
        expected_continuity=False,
        depletion_pressure=0.58,
        regrowth_delay=0.42,
        spoilage_pressure=0.08,
        migration_pressure=0.05,
        social_pressure=0.86,
        territory_pressure=0.82,
        initial_resource=0.56,
        initial_water=0.55,
        required_progress=82.0,
        work_rate=0.54,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=5,
        name="restore_ecology_continuity",
        pressure="after restore, known depletion, cache age, migration, territory, and sharing history must survive",
        expected_resource_memory=True,
        expected_regeneration_model=True,
        expected_spoilage_model=True,
        expected_migration_tracking=True,
        expected_restraint=True,
        expected_cache_management=True,
        expected_sharing_contract=True,
        expected_territory_ownership=True,
        expected_continuity=True,
        depletion_pressure=0.66,
        regrowth_delay=0.58,
        spoilage_pressure=0.54,
        migration_pressure=0.56,
        social_pressure=0.62,
        territory_pressure=0.58,
        initial_resource=0.50,
        initial_water=0.50,
        required_progress=66.0,
        work_rate=0.52,
        restore_tick=96,
    ),
)


SEEDED_POLICIES = (
    Policy(
        name="greedy_no_ecology_baseline",
        resource_memory=False,
        regeneration_model=False,
        spoilage_model=False,
        migration_tracking=False,
        restraint_policy=False,
        cache_management=False,
        sharing_contract=False,
        territory_ownership=False,
        continuity_memory=False,
        harvest_bias=0.92,
        reserve_target=0.06,
        sharing_bias=0.04,
        territory_bias=0.04,
    ),
    Policy(
        name="reactive_scarcity_forager",
        resource_memory=True,
        regeneration_model=False,
        spoilage_model=False,
        migration_tracking=False,
        restraint_policy=False,
        cache_management=False,
        sharing_contract=False,
        territory_ownership=False,
        continuity_memory=False,
        harvest_bias=0.78,
        reserve_target=0.12,
        sharing_bias=0.04,
        territory_bias=0.04,
    ),
    Policy(
        name="regrowth_restraint_planner",
        resource_memory=True,
        regeneration_model=True,
        spoilage_model=False,
        migration_tracking=False,
        restraint_policy=True,
        cache_management=False,
        sharing_contract=False,
        territory_ownership=False,
        continuity_memory=False,
        harvest_bias=0.46,
        reserve_target=0.46,
        sharing_bias=0.04,
        territory_bias=0.04,
    ),
    Policy(
        name="spoilage_cache_planner",
        resource_memory=True,
        regeneration_model=False,
        spoilage_model=True,
        migration_tracking=False,
        restraint_policy=True,
        cache_management=True,
        sharing_contract=False,
        territory_ownership=False,
        continuity_memory=False,
        harvest_bias=0.58,
        reserve_target=0.34,
        sharing_bias=0.04,
        territory_bias=0.04,
    ),
    Policy(
        name="migration_tracking_planner",
        resource_memory=True,
        regeneration_model=False,
        spoilage_model=False,
        migration_tracking=True,
        restraint_policy=True,
        cache_management=False,
        sharing_contract=False,
        territory_ownership=False,
        continuity_memory=False,
        harvest_bias=0.55,
        reserve_target=0.30,
        sharing_bias=0.04,
        territory_bias=0.04,
    ),
    Policy(
        name="territory_sharing_planner",
        resource_memory=True,
        regeneration_model=True,
        spoilage_model=False,
        migration_tracking=False,
        restraint_policy=True,
        cache_management=False,
        sharing_contract=True,
        territory_ownership=True,
        continuity_memory=False,
        harvest_bias=0.48,
        reserve_target=0.40,
        sharing_bias=0.84,
        territory_bias=0.82,
    ),
    Policy(
        name="continuity_ecology_planner",
        resource_memory=True,
        regeneration_model=True,
        spoilage_model=True,
        migration_tracking=True,
        restraint_policy=True,
        cache_management=True,
        sharing_contract=True,
        territory_ownership=True,
        continuity_memory=True,
        harvest_bias=0.50,
        reserve_target=0.42,
        sharing_bias=0.78,
        territory_bias=0.76,
    ),
)


CONDITIONS = (
    "full_control",
    "no_resource_memory",
    "no_regeneration_model",
    "no_spoilage_model",
    "no_migration_tracking",
    "no_restraint",
    "no_cache_management",
    "no_sharing_contract",
    "no_territory_ownership",
    "no_continuity",
    "greedy_consumption_only",
    "omniscient_resource_control",
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


def build_policies(cfg: EcologyConfig) -> List[Policy]:
    policies = list(SEEDED_POLICIES)
    rng = random.Random(cfg.seed + 1447)
    while len(policies) < cfg.candidate_count:
        base = rng.choice(SEEDED_POLICIES[2:])
        policies.append(
            Policy(
                name=f"mutant_ecology_{len(policies)}",
                resource_memory=base.resource_memory if rng.random() > 0.12 else not base.resource_memory,
                regeneration_model=base.regeneration_model if rng.random() > 0.16 else not base.regeneration_model,
                spoilage_model=base.spoilage_model if rng.random() > 0.16 else not base.spoilage_model,
                migration_tracking=base.migration_tracking if rng.random() > 0.16 else not base.migration_tracking,
                restraint_policy=base.restraint_policy if rng.random() > 0.14 else not base.restraint_policy,
                cache_management=base.cache_management if rng.random() > 0.16 else not base.cache_management,
                sharing_contract=base.sharing_contract if rng.random() > 0.18 else not base.sharing_contract,
                territory_ownership=base.territory_ownership if rng.random() > 0.18 else not base.territory_ownership,
                continuity_memory=base.continuity_memory if rng.random() > 0.18 else not base.continuity_memory,
                harvest_bias=clamp(base.harvest_bias + rng.uniform(-0.08, 0.08), 0.24, 0.96),
                reserve_target=clamp(base.reserve_target + rng.uniform(-0.08, 0.08), 0.04, 0.70),
                sharing_bias=clamp(base.sharing_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
                territory_bias=clamp(base.territory_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
            )
        )
    return policies


def condition_policy(policy: Policy, condition: str) -> Policy:
    if condition == "omniscient_resource_control":
        return Policy(
            name=policy.name,
            resource_memory=True,
            regeneration_model=True,
            spoilage_model=True,
            migration_tracking=True,
            restraint_policy=True,
            cache_management=True,
            sharing_contract=True,
            territory_ownership=True,
            continuity_memory=True,
            harvest_bias=0.44,
            reserve_target=max(policy.reserve_target, 0.52),
            sharing_bias=max(policy.sharing_bias, 0.90),
            territory_bias=max(policy.territory_bias, 0.90),
        )
    if condition == "greedy_consumption_only":
        return Policy(
            name=policy.name,
            resource_memory=False,
            regeneration_model=False,
            spoilage_model=False,
            migration_tracking=False,
            restraint_policy=False,
            cache_management=False,
            sharing_contract=False,
            territory_ownership=False,
            continuity_memory=False,
            harvest_bias=0.94,
            reserve_target=0.04,
            sharing_bias=0.02,
            territory_bias=0.02,
        )
    return Policy(
        name=policy.name,
        resource_memory=policy.resource_memory and condition != "no_resource_memory",
        regeneration_model=policy.regeneration_model and condition != "no_regeneration_model",
        spoilage_model=policy.spoilage_model and condition != "no_spoilage_model",
        migration_tracking=policy.migration_tracking and condition != "no_migration_tracking",
        restraint_policy=policy.restraint_policy and condition != "no_restraint",
        cache_management=policy.cache_management and condition != "no_cache_management",
        sharing_contract=policy.sharing_contract and condition != "no_sharing_contract",
        territory_ownership=policy.territory_ownership and condition != "no_territory_ownership",
        continuity_memory=policy.continuity_memory and condition != "no_continuity",
        harvest_bias=policy.harvest_bias,
        reserve_target=policy.reserve_target,
        sharing_bias=policy.sharing_bias,
        territory_bias=policy.territory_bias,
    )


def scenario_seed(
    cfg: EcologyConfig,
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
        (policy.resource_memory, 2.30),
        (policy.regeneration_model, 2.60),
        (policy.spoilage_model, 2.40),
        (policy.migration_tracking, 2.60),
        (policy.restraint_policy, 2.20),
        (policy.cache_management, 2.70),
        (policy.sharing_contract, 3.00),
        (policy.territory_ownership, 3.00),
        (policy.continuity_memory, 8.50),
    ]
    return sum(weight for enabled, weight in weighted_flags if enabled)


def estimate_ecology_risk(
    scenario: ScenarioSpec,
    policy: Policy,
    resource: float,
    water: float,
    cache: float,
    migration_confidence: float,
    social_access: float,
    territory_standing: float,
    scarcity: float,
    spoilage: float,
) -> float:
    if not policy.resource_memory and not any(
        [
            scenario.expected_resource_memory,
            scenario.expected_regeneration_model,
            scenario.expected_spoilage_model,
            scenario.expected_migration_tracking,
            scenario.expected_sharing_contract,
            scenario.expected_territory_ownership,
        ]
    ):
        return 0.10
    resource_gap = max(0.0, 0.48 - (resource + water) * 0.50)
    trace = (
        resource_gap * 0.90
        + scarcity * 0.56
        + spoilage * scenario.spoilage_pressure * 0.34
        + scenario.migration_pressure * (1.0 - migration_confidence) * 0.42
        + scenario.social_pressure * (1.0 - social_access) * 0.38
        + scenario.territory_pressure * (1.0 - territory_standing) * 0.38
        + max(0.0, policy.reserve_target - cache) * 0.20
    )
    mitigation = (
        (0.16 if policy.resource_memory else 0.0)
        + (0.14 if policy.regeneration_model else 0.0)
        + (0.12 if policy.spoilage_model else 0.0)
        + (0.14 if policy.migration_tracking else 0.0)
        + (0.12 if policy.restraint_policy else 0.0)
        + (0.12 if policy.cache_management else 0.0)
        + (0.12 if policy.sharing_contract else 0.0)
        + (0.12 if policy.territory_ownership else 0.0)
    )
    return clamp(trace - mitigation, 0.0, 1.8)


def choose_action(
    scenario: ScenarioSpec,
    policy: Policy,
    risk: float,
    resource: float,
    water: float,
    cache: float,
    hunger: float,
    thirst: float,
    migration_confidence: float,
    social_access: float,
    territory_standing: float,
    tick: int,
) -> str:
    if scenario.index == 0:
        if hunger > 0.42 or thirst > 0.42:
            return "harvest_resource"
        return "work"
    if scenario.expected_sharing_contract and policy.sharing_contract and social_access < 0.62 and risk > 0.12:
        return "share_resource"
    if scenario.expected_territory_ownership and policy.territory_ownership and territory_standing < 0.60 and risk > 0.12:
        return "negotiate_territory"
    if scenario.expected_migration_tracking and policy.migration_tracking and migration_confidence < 0.70 and tick % 9 == 0:
        return "track_migration"
    if scenario.expected_spoilage_model and policy.spoilage_model and policy.cache_management and cache > 0.20 and tick % 11 == 0:
        return "rotate_cache"
    if policy.cache_management and (resource + water) > 1.10 and cache < policy.reserve_target:
        return "cache_resource"
    if policy.restraint_policy and scenario.expected_restraint and (resource < policy.reserve_target or water < policy.reserve_target):
        return "wait_regrow"
    if hunger > 0.42 or thirst > 0.42 or risk > 0.34:
        return "harvest_resource"
    return "work"


def add_trace(
    trace: List[Dict[str, object]],
    tick: int,
    action: str,
    progress: float,
    energy: float,
    hunger: float,
    thirst: float,
    resource: float,
    water: float,
    cache: float,
    scarcity: float,
    spoilage: float,
    migration: float,
    social: float,
    territory: float,
    conflicts: int,
    notes: List[str],
) -> None:
    trace.append(
        {
            "tick": tick,
            "action": action,
            "progress": round(progress, 3),
            "energy": round(energy, 3),
            "hunger": round(hunger, 3),
            "thirst": round(thirst, 3),
            "resource_level": round(resource, 3),
            "water_level": round(water, 3),
            "cache_level": round(cache, 3),
            "scarcity_risk": round(scarcity, 3),
            "spoilage_waste": round(spoilage, 3),
            "migration_confidence": round(migration, 3),
            "social_access": round(social, 3),
            "territory_standing": round(territory, 3),
            "conflict_events": conflicts,
            "notes": list(notes[-3:]),
        }
    )


def simulate_episode(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episode: int,
    cfg: EcologyConfig,
    phase: str,
    collect_trace: bool = False,
) -> Tuple[EpisodeResult, List[Dict[str, object]]]:
    effective = condition_policy(policy, condition)
    rng = random.Random(scenario_seed(cfg, scenario, policy, condition, episode, phase))

    resource = clamp(scenario.initial_resource + rng.uniform(-0.020, 0.020), 0.0, 1.0)
    water = clamp(scenario.initial_water + rng.uniform(-0.020, 0.020), 0.0, 1.0)
    cache = clamp(0.08 + (0.08 if effective.cache_management else 0.0), 0.0, 1.0)
    hunger = clamp(0.22 + rng.uniform(-0.012, 0.012), 0.0, 1.2)
    thirst = clamp(0.22 + rng.uniform(-0.012, 0.012), 0.0, 1.2)
    energy = clamp(0.96 + rng.uniform(-0.012, 0.012), 0.0, 1.0)
    scarcity = 0.0
    spoilage = 0.0
    migration_confidence = 0.72 if effective.migration_tracking else 0.34
    social_access = 0.52 if scenario.expected_sharing_contract else 0.84
    territory_standing = 0.50 if scenario.expected_territory_ownership else 0.84
    cache_age = 0.0
    collapsed = False
    notes: List[str] = []
    trace_frames: List[Dict[str, object]] = []

    conflict_events = 0
    overharvest_events = 0
    spoiled_cache_events = 0
    migration_misses = 0
    sharing_actions = 0
    cache_actions = 0
    restraint_actions = 0
    territory_actions = 0
    continuity_resets = 0
    ecology_misses = 0
    progress = 0.0

    for tick in range(cfg.ticks):
        action = "work"
        if scenario.restore_tick == tick and not effective.continuity_memory:
            continuity_resets += 1
            ecology_misses += 5
            scarcity = clamp(scarcity + 0.30, 0.0, 1.8)
            spoilage = clamp(spoilage + 0.24, 0.0, 1.8)
            migration_confidence = min(migration_confidence, 0.20)
            social_access = max(0.10, social_access - 0.32)
            territory_standing = max(0.10, territory_standing - 0.30)
            cache = max(0.02, cache - 0.24)
            notes.append("restore erased ecology continuity")
            action = "restore_reset"

        risk = estimate_ecology_risk(
            scenario,
            effective,
            resource,
            water,
            cache,
            migration_confidence,
            social_access,
            territory_standing,
            scarcity,
            spoilage,
        )
        if not collapsed and action != "restore_reset":
            action = choose_action(
                scenario,
                effective,
                risk,
                resource,
                water,
                cache,
                hunger,
                thirst,
                migration_confidence,
                social_access,
                territory_standing,
                tick,
            )

        if collapsed:
            action = "collapsed"
        elif action == "share_resource":
            sharing_actions += 1
            social_access = clamp(social_access + 0.24 + effective.sharing_bias * 0.18, 0.0, 1.0)
            cache = clamp(cache - 0.035, 0.0, 1.0)
            hunger = clamp(hunger + 0.006, 0.0, 1.4)
            progress -= 0.16
            notes.append("sharing preserved future access")
        elif action == "negotiate_territory":
            territory_actions += 1
            territory_standing = clamp(territory_standing + 0.24 + effective.territory_bias * 0.18, 0.0, 1.0)
            social_access = clamp(social_access + 0.050, 0.0, 1.0)
            progress -= 0.18
            notes.append("territory memory preserved access")
        elif action == "track_migration":
            migration_confidence = clamp(migration_confidence + 0.38, 0.0, 1.0)
            energy = clamp(energy - 0.010, 0.0, 1.0)
            progress -= 0.16
            notes.append("migration tracking refreshed route")
        elif action == "rotate_cache":
            cache_actions += 1
            cache_age = max(0.0, cache_age - 0.30)
            spoilage = clamp(spoilage - 0.10, 0.0, 1.8)
            energy = clamp(energy - 0.006, 0.0, 1.0)
            progress -= 0.12
            notes.append("cache rotated before spoilage")
        elif action == "cache_resource":
            cache_actions += 1
            amount = min(0.055, resource * 0.10 + water * 0.08)
            resource = clamp(resource - amount * 0.55, 0.0, 1.0)
            water = clamp(water - amount * 0.45, 0.0, 1.0)
            cache = clamp(cache + amount, 0.0, 1.0)
            cache_age = clamp(cache_age + 0.018, 0.0, 1.0)
            progress -= 0.10
            notes.append("resource cached for later")
        elif action == "wait_regrow":
            restraint_actions += 1
            scarcity = clamp(scarcity - 0.018, 0.0, 1.8)
            hunger = clamp(hunger + 0.010, 0.0, 1.4)
            thirst = clamp(thirst + 0.010, 0.0, 1.4)
            progress += scenario.work_rate * 0.15
            notes.append("restraint preserved source")
        elif action == "harvest_resource":
            harvest = 0.060 + effective.harvest_bias * 0.040
            if effective.restraint_policy:
                harvest *= 0.62
            access = 1.0
            if scenario.expected_resource_memory and not effective.resource_memory:
                access *= 0.52
            if scenario.expected_migration_tracking:
                access *= 0.52 + migration_confidence * 0.48
            if scenario.expected_sharing_contract:
                access *= 0.50 + social_access * 0.50
            if scenario.expected_territory_ownership:
                access *= 0.50 + territory_standing * 0.50
            gained_food = min(resource, harvest * access)
            gained_water = min(water, harvest * 0.92 * access)
            resource = clamp(resource - gained_food, 0.0, 1.0)
            water = clamp(water - gained_water, 0.0, 1.0)
            hunger = clamp(hunger - gained_food * 1.8 - cache * 0.020, 0.0, 1.4)
            thirst = clamp(thirst - gained_water * 1.8 - cache * 0.018, 0.0, 1.4)
            if effective.cache_management and (gained_food + gained_water) > 0.10:
                cache = clamp(cache + (gained_food + gained_water) * 0.18, 0.0, 1.0)
                cache_actions += 1
            if not effective.restraint_policy and scenario.expected_restraint and (gained_food + gained_water) > 0.08:
                overharvest_events += 1 if tick % 7 == 0 else 0
                scarcity = clamp(scarcity + scenario.depletion_pressure * 0.022, 0.0, 1.8)
            if gained_food + gained_water < 0.04:
                ecology_misses += 1
                scarcity = clamp(scarcity + 0.018, 0.0, 1.8)
            progress += scenario.work_rate * 0.24
        elif action == "work":
            capability = clamp(
                0.92
                + energy * 0.08
                - hunger * 0.20
                - thirst * 0.24
                - scarcity * 0.10
                - spoilage * 0.05,
                0.04,
                1.04,
            )
            progress += scenario.work_rate * capability

        if effective.regeneration_model:
            regen_factor = 0.010 + (1.0 - scenario.regrowth_delay) * 0.004
        else:
            regen_factor = 0.005 - scenario.regrowth_delay * 0.002
            if scenario.expected_regeneration_model:
                scarcity = clamp(scarcity + scenario.regrowth_delay * 0.006, 0.0, 1.8)
                ecology_misses += 1 if tick % 19 == 0 else 0
        if effective.restraint_policy:
            regen_factor += 0.004
        else:
            regen_factor -= scenario.depletion_pressure * 0.002
        resource = clamp(resource + regen_factor * (1.0 - resource), 0.0, 1.0)
        water = clamp(water + (regen_factor + 0.002) * (1.0 - water), 0.0, 1.0)

        if scenario.expected_resource_memory and not effective.resource_memory:
            scarcity = clamp(scarcity + 0.005, 0.0, 1.8)
            ecology_misses += 1 if tick % 17 == 0 else 0

        cache_age = clamp(cache_age + 0.006 + scenario.spoilage_pressure * 0.004, 0.0, 1.0)
        if scenario.expected_spoilage_model:
            if effective.spoilage_model and effective.cache_management:
                spoilage = clamp(spoilage + max(0.0, cache_age - 0.65) * 0.002, 0.0, 1.8)
            else:
                spoiled = cache * scenario.spoilage_pressure * (0.006 + cache_age * 0.006)
                cache = clamp(cache - spoiled, 0.0, 1.0)
                spoilage = clamp(spoilage + spoiled * 2.8, 0.0, 1.8)
                if spoiled > 0.003 and tick % 9 == 0:
                    spoiled_cache_events += 1
                    ecology_misses += 1

        if scenario.expected_migration_tracking:
            if effective.migration_tracking:
                migration_confidence = clamp(migration_confidence - scenario.migration_pressure * 0.002, 0.0, 1.0)
            else:
                migration_confidence = clamp(migration_confidence - scenario.migration_pressure * 0.006, 0.0, 1.0)
                scarcity = clamp(scarcity + scenario.migration_pressure * 0.008, 0.0, 1.8)
                if tick % 13 == 0:
                    migration_misses += 1
                    ecology_misses += 1

        if scenario.expected_sharing_contract:
            if effective.sharing_contract:
                social_access = clamp(social_access - scenario.social_pressure * 0.001, 0.0, 1.0)
            else:
                social_access = clamp(social_access - scenario.social_pressure * 0.006, 0.0, 1.0)
                scarcity = clamp(scarcity + scenario.social_pressure * 0.009, 0.0, 1.8)
                if tick % 17 == 0:
                    conflict_events += 1
                    ecology_misses += 1
        if scenario.expected_territory_ownership:
            if effective.territory_ownership:
                territory_standing = clamp(territory_standing - scenario.territory_pressure * 0.001, 0.0, 1.0)
            else:
                territory_standing = clamp(territory_standing - scenario.territory_pressure * 0.007, 0.0, 1.0)
                scarcity = clamp(scarcity + scenario.territory_pressure * 0.010, 0.0, 1.8)
                if tick % 19 == 0:
                    conflict_events += 1
                    ecology_misses += 1

        if not effective.cache_management and scenario.expected_cache_management:
            scarcity = clamp(scarcity + 0.008, 0.0, 1.8)
        if not effective.restraint_policy and scenario.expected_restraint:
            scarcity = clamp(
                scarcity
                + scenario.depletion_pressure * 0.010
                + scenario.regrowth_delay * 0.004
                + scenario.migration_pressure * 0.006
                + scenario.social_pressure * 0.004,
                0.0,
                1.8,
            )
            resource = clamp(resource - scenario.depletion_pressure * 0.002, 0.0, 1.0)
            water = clamp(water - scenario.depletion_pressure * 0.0015, 0.0, 1.0)
            overharvest_events += 1 if tick % 23 == 0 else 0

        if cache > 0.02 and (hunger > 0.62 or thirst > 0.62):
            draw = min(cache, 0.030)
            cache = clamp(cache - draw, 0.0, 1.0)
            hunger = clamp(hunger - draw * 0.85, 0.0, 1.4)
            thirst = clamp(thirst - draw * 0.75, 0.0, 1.4)

        hunger = clamp(hunger + 0.006 + scarcity * 0.002 + spoilage * 0.001, 0.0, 1.4)
        thirst = clamp(thirst + 0.0065 + scarcity * 0.002, 0.0, 1.4)
        energy = clamp(energy - 0.0010 - hunger * 0.0008 - thirst * 0.0010 - conflict_events * 0.00005, 0.0, 1.0)
        if hunger >= 1.18 or thirst >= 1.18 or energy <= 0.04:
            collapsed = True

        if collect_trace and (tick % 5 == 0 or tick == cfg.ticks - 1 or action != "work"):
            add_trace(
                trace_frames,
                tick,
                action,
                progress,
                energy,
                hunger,
                thirst,
                resource,
                water,
                cache,
                scarcity,
                spoilage,
                migration_confidence,
                social_access,
                territory_standing,
                conflict_events,
                notes,
            )

    task_success = progress >= scenario.required_progress and not collapsed
    survival = 1.0 if not collapsed and hunger < 1.05 and thirst < 1.05 and energy > 0.06 else 0.0

    reward = progress
    reward += 34.0 if task_success else -22.0
    reward += 40.0 if survival else -112.0
    reward += energy * 18.0
    reward -= hunger * 46.0
    reward -= thirst * 52.0
    reward -= scarcity * 94.0
    reward -= spoilage * 58.0
    reward -= ecology_misses * 0.75
    reward -= conflict_events * 7.5
    reward -= overharvest_events * 2.6
    reward -= spoiled_cache_events * 2.8
    reward -= migration_misses * 2.4
    reward += cache * (16.0 if scenario.expected_cache_management else 2.0)
    reward += social_access * (18.0 if scenario.expected_sharing_contract else 1.0)
    reward += territory_standing * (18.0 if scenario.expected_territory_ownership else 1.0)
    reward += migration_confidence * (12.0 if scenario.expected_migration_tracking else 1.0)
    reward += (resource + water) * (8.0 if scenario.expected_regeneration_model else 2.0)
    reward -= sharing_actions * 0.18
    reward -= cache_actions * 0.16
    reward -= restraint_actions * 0.12
    reward -= territory_actions * 0.18
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
        hunger=hunger,
        thirst=thirst,
        resource_level=resource,
        water_level=water,
        cache_level=cache,
        scarcity_risk=scarcity,
        spoilage_waste=spoilage,
        migration_confidence=migration_confidence,
        social_access=social_access,
        territory_standing=territory_standing,
        conflict_events=conflict_events,
        overharvest_events=overharvest_events,
        spoiled_cache_events=spoiled_cache_events,
        migration_misses=migration_misses,
        sharing_actions=sharing_actions,
        cache_actions=cache_actions,
        restraint_actions=restraint_actions,
        territory_actions=territory_actions,
        continuity_resets=continuity_resets,
        ecology_misses=ecology_misses,
    )
    return result, trace_frames


def evaluate_policy(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episodes: int,
    cfg: EcologyConfig,
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
                    mean_hunger=mean(row.hunger for row in subset),
                    mean_thirst=mean(row.thirst for row in subset),
                    mean_resource_level=mean(row.resource_level for row in subset),
                    mean_water_level=mean(row.water_level for row in subset),
                    mean_cache_level=mean(row.cache_level for row in subset),
                    mean_scarcity_risk=mean(row.scarcity_risk for row in subset),
                    mean_spoilage_waste=mean(row.spoilage_waste for row in subset),
                    mean_migration_confidence=mean(row.migration_confidence for row in subset),
                    mean_social_access=mean(row.social_access for row in subset),
                    mean_territory_standing=mean(row.territory_standing for row in subset),
                    mean_conflict_events=mean(row.conflict_events for row in subset),
                    mean_overharvest_events=mean(row.overharvest_events for row in subset),
                    mean_spoiled_cache_events=mean(row.spoiled_cache_events for row in subset),
                    mean_migration_misses=mean(row.migration_misses for row in subset),
                    mean_sharing_actions=mean(row.sharing_actions for row in subset),
                    mean_cache_actions=mean(row.cache_actions for row in subset),
                    mean_restraint_actions=mean(row.restraint_actions for row in subset),
                    mean_territory_actions=mean(row.territory_actions for row in subset),
                    mean_continuity_resets=mean(row.continuity_resets for row in subset),
                    mean_ecology_misses=mean(row.ecology_misses for row in subset),
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
        condition_rewards = {
            condition: by_scenario_condition[(scenario.index, condition)].mean_reward
            for condition in CONDITIONS
        }
        losses = {
            condition: full.mean_reward - reward
            for condition, reward in condition_rewards.items()
        }
        if scenario.index == 0:
            supports = (
                full.policy_name == "greedy_no_ecology_baseline"
                and max(
                    abs(losses[condition])
                    for condition in CONDITIONS
                    if condition not in {"full_control", "omniscient_resource_control"}
                )
                < 8.0
            )
            verdict = "ecology_machinery_rejected_in_abundant_control"
        elif scenario.index == 1:
            supports = (
                losses["no_resource_memory"] > 34.0
                and losses["no_regeneration_model"] > 38.0
                and losses["no_restraint"] > 42.0
                and losses["greedy_consumption_only"] > 42.0
            )
            verdict = "slow_regrowth_depletion_memory_restraint_pressure"
        elif scenario.index == 2:
            supports = (
                losses["no_resource_memory"] > 24.0
                and losses["no_spoilage_model"] > 52.0
                and losses["no_cache_management"] > 46.0
                and losses["no_restraint"] > 18.0
            )
            verdict = "spoilage_cache_timing_pressure"
        elif scenario.index == 3:
            supports = (
                losses["no_resource_memory"] > 24.0
                and losses["no_migration_tracking"] > 68.0
                and losses["no_restraint"] > 18.0
                and losses["greedy_consumption_only"] > 42.0
            )
            verdict = "migration_tracking_resource_memory_pressure"
        elif scenario.index == 4:
            supports = (
                losses["no_resource_memory"] > 24.0
                and losses["no_regeneration_model"] > 24.0
                and losses["no_restraint"] > 26.0
                and losses["no_sharing_contract"] > 70.0
                and losses["no_territory_ownership"] > 70.0
            )
            verdict = "shared_territory_contract_pressure"
        else:
            supports = (
                losses["no_continuity"] > 54.0
                and losses["no_resource_memory"] > 32.0
                and losses["no_regeneration_model"] > 28.0
                and losses["no_spoilage_model"] > 32.0
                and losses["no_migration_tracking"] > 32.0
                and losses["no_cache_management"] > 28.0
                and losses["no_sharing_contract"] > 38.0
                and losses["no_territory_ownership"] > 38.0
            )
            verdict = "restore_resource_ecology_continuity_pressure"

        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                expected_pressure=scenario.pressure,
                selected_policy=full.policy_name,
                selected_reward=full.mean_reward,
                no_resource_memory_reward=condition_rewards["no_resource_memory"],
                no_regeneration_model_reward=condition_rewards["no_regeneration_model"],
                no_spoilage_model_reward=condition_rewards["no_spoilage_model"],
                no_migration_tracking_reward=condition_rewards["no_migration_tracking"],
                no_restraint_reward=condition_rewards["no_restraint"],
                no_cache_management_reward=condition_rewards["no_cache_management"],
                no_sharing_contract_reward=condition_rewards["no_sharing_contract"],
                no_territory_ownership_reward=condition_rewards["no_territory_ownership"],
                no_continuity_reward=condition_rewards["no_continuity"],
                greedy_consumption_only_reward=condition_rewards["greedy_consumption_only"],
                omniscient_resource_control_reward=condition_rewards["omniscient_resource_control"],
                no_resource_memory_loss=losses["no_resource_memory"],
                no_regeneration_model_loss=losses["no_regeneration_model"],
                no_spoilage_model_loss=losses["no_spoilage_model"],
                no_migration_tracking_loss=losses["no_migration_tracking"],
                no_restraint_loss=losses["no_restraint"],
                no_cache_management_loss=losses["no_cache_management"],
                no_sharing_contract_loss=losses["no_sharing_contract"],
                no_territory_ownership_loss=losses["no_territory_ownership"],
                no_continuity_loss=losses["no_continuity"],
                greedy_consumption_only_loss=losses["greedy_consumption_only"],
                selected_conflicts=full.mean_conflict_events,
                selected_overharvests=full.mean_overharvest_events,
                selected_spoiled_cache_events=full.mean_spoiled_cache_events,
                selected_migration_misses=full.mean_migration_misses,
                selected_cache_actions=full.mean_cache_actions,
                selected_sharing_actions=full.mean_sharing_actions,
                selected_restraint_actions=full.mean_restraint_actions,
                selected_territory_actions=full.mean_territory_actions,
                supports_resource_ecology_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def select_policies(cfg: EcologyConfig, policies: Sequence[Policy]) -> Tuple[Dict[int, Policy], List[PolicySelectionRow]]:
    selected: Dict[int, Policy] = {}
    rows: List[PolicySelectionRow] = []
    greedy = next(policy for policy in policies if policy.name == "greedy_no_ecology_baseline")
    for scenario in SCENARIOS:
        scores: List[Tuple[float, Policy]] = []
        for policy in policies:
            train_rows = evaluate_policy(scenario, policy, "full_control", cfg.train_episodes, cfg, "train")
            scores.append((mean(row.total_reward for row in train_rows), policy))
        scores.sort(key=lambda item: item[0], reverse=True)
        best_reward, best_policy = scores[0]
        greedy_rows = evaluate_policy(scenario, greedy, "full_control", cfg.train_episodes, cfg, "train_greedy")
        greedy_reward = mean(row.total_reward for row in greedy_rows)
        selected[scenario.index] = best_policy
        rows.append(
            PolicySelectionRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                selected_policy=best_policy.name,
                selected_uses_resource_memory=best_policy.resource_memory,
                selected_uses_regeneration_model=best_policy.regeneration_model,
                selected_uses_spoilage_model=best_policy.spoilage_model,
                selected_uses_migration_tracking=best_policy.migration_tracking,
                selected_uses_restraint=best_policy.restraint_policy,
                selected_uses_cache_management=best_policy.cache_management,
                selected_uses_sharing_contract=best_policy.sharing_contract,
                selected_uses_territory_ownership=best_policy.territory_ownership,
                selected_uses_continuity=best_policy.continuity_memory,
                train_reward=best_reward,
                greedy_train_reward=greedy_reward,
                train_gain_over_greedy=best_reward - greedy_reward,
            )
        )
    return selected, rows


def run_eval(cfg: EcologyConfig, selected: Dict[int, Policy]) -> List[EpisodeResult]:
    eval_rows: List[EpisodeResult] = []
    for scenario in SCENARIOS:
        policy = selected[scenario.index]
        for condition in CONDITIONS:
            eval_rows.extend(evaluate_policy(scenario, policy, condition, cfg.eval_episodes, cfg, "eval"))
    return eval_rows


def build_trace(
    cfg: EcologyConfig,
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
        "memory_loss",
        "regen_loss",
        "spoilage_loss",
        "migration_loss",
        "restraint_loss",
        "cache_loss",
        "sharing_loss",
        "territory_loss",
        "continuity_loss",
        "supports",
    ]
    rows = [
        [
            row.scenario_name,
            row.selected_policy,
            f"{row.no_resource_memory_loss:.3f}",
            f"{row.no_regeneration_model_loss:.3f}",
            f"{row.no_spoilage_model_loss:.3f}",
            f"{row.no_migration_tracking_loss:.3f}",
            f"{row.no_restraint_loss:.3f}",
            f"{row.no_cache_management_loss:.3f}",
            f"{row.no_sharing_contract_loss:.3f}",
            f"{row.no_territory_ownership_loss:.3f}",
            f"{row.no_continuity_loss:.3f}",
            str(row.supports_resource_ecology_precursor),
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


def parse_args() -> EcologyConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-episodes", type=int, default=EcologyConfig.train_episodes)
    parser.add_argument("--eval-episodes", type=int, default=EcologyConfig.eval_episodes)
    parser.add_argument("--ticks", type=int, default=EcologyConfig.ticks)
    parser.add_argument("--seed", type=int, default=EcologyConfig.seed)
    parser.add_argument("--candidate-count", type=int, default=EcologyConfig.candidate_count)
    parser.add_argument("--trace-scenario", type=int, default=EcologyConfig.trace_scenario)
    parser.add_argument("--trace-episode", type=int, default=EcologyConfig.trace_episode)
    args = parser.parse_args()
    return EcologyConfig(
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

    prefix = ARTIFACT_DIR / "ssrm_3d_resource_ecology"
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
    write_js(prefix.with_name(prefix.name + "_results.js"), "SSRM_3D_RESOURCE_ECOLOGY_RESULTS", results)
    write_js(prefix.with_name(prefix.name + "_trace.js"), "SSRM_3D_RESOURCE_ECOLOGY_TRACE", trace)
    print_verdicts(verdict_rows)
    return 0 if all(row.supports_resource_ecology_precursor for row in verdict_rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
