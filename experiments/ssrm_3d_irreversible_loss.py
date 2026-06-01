#!/usr/bin/env python3
"""SSRM-3D irreversible-loss precursor.

This experiment implements the twelfth pressure-layer step from report 74:
irreversible loss. It is intentionally not a grief or subjective-emotion
simulation.

Permanent loss is treated as control pressure. The narrow test is whether loss
state should be rejected in a reversible-control regime, then become useful only
when tools, shelters, relationships, memories, or companions can be permanently
removed from future option space.
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
class LossConfig:
    train_episodes: int = 72
    eval_episodes: int = 96
    ticks: int = 210
    seed: int = 20260701
    candidate_count: int = 7
    trace_scenario: int = 4
    trace_episode: int = 0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    expected_loss_memory: bool
    expected_value_at_risk: bool
    expected_replacement_model: bool
    expected_caution_control: bool
    expected_tool_preservation: bool
    expected_shelter_preservation: bool
    expected_relationship_preservation: bool
    expected_memory_backup: bool
    expected_loss_response: bool
    expected_continuity: bool
    tool_loss_pressure: float
    shelter_loss_pressure: float
    relationship_loss_pressure: float
    memory_loss_pressure: float
    replacement_pressure: float
    cascade_pressure: float
    required_progress: float
    work_rate: float
    restore_tick: int


@dataclass(frozen=True)
class Policy:
    name: str
    loss_memory: bool
    value_at_risk: bool
    replacement_model: bool
    caution_control: bool
    tool_preservation: bool
    shelter_preservation: bool
    relationship_preservation: bool
    memory_backup: bool
    loss_response: bool
    continuity_memory: bool
    risk_threshold: float
    preservation_bias: float
    backup_bias: float
    replan_bias: float


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
    tool_integrity: float
    shelter_safety: float
    relationship_trust: float
    memory_integrity: float
    option_space: float
    value_at_risk_estimate: float
    replacement_feasibility: float
    caution_state: float
    loss_events: int
    tool_loss_events: int
    shelter_loss_events: int
    relationship_loss_events: int
    memory_loss_events: int
    preservation_actions: int
    backup_actions: int
    replan_actions: int
    replacement_actions: int
    caution_actions: int
    continuity_resets: int
    loss_misses: int


@dataclass(frozen=True)
class PolicySelectionRow:
    scenario: int
    scenario_name: str
    selected_policy: str
    selected_uses_loss_memory: bool
    selected_uses_value_at_risk: bool
    selected_uses_replacement_model: bool
    selected_uses_caution_control: bool
    selected_uses_tool_preservation: bool
    selected_uses_shelter_preservation: bool
    selected_uses_relationship_preservation: bool
    selected_uses_memory_backup: bool
    selected_uses_loss_response: bool
    selected_uses_continuity: bool
    train_reward: float
    reckless_train_reward: float
    train_gain_over_reckless: float


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
    mean_tool_integrity: float
    mean_shelter_safety: float
    mean_relationship_trust: float
    mean_memory_integrity: float
    mean_option_space: float
    mean_value_at_risk_estimate: float
    mean_replacement_feasibility: float
    mean_caution_state: float
    mean_loss_events: float
    mean_tool_loss_events: float
    mean_shelter_loss_events: float
    mean_relationship_loss_events: float
    mean_memory_loss_events: float
    mean_preservation_actions: float
    mean_backup_actions: float
    mean_replan_actions: float
    mean_replacement_actions: float
    mean_caution_actions: float
    mean_continuity_resets: float
    mean_loss_misses: float


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    expected_pressure: str
    selected_policy: str
    selected_reward: float
    no_loss_memory_reward: float
    no_value_at_risk_reward: float
    no_replacement_model_reward: float
    no_caution_control_reward: float
    no_tool_preservation_reward: float
    no_shelter_preservation_reward: float
    no_relationship_preservation_reward: float
    no_memory_backup_reward: float
    no_loss_response_reward: float
    no_continuity_reward: float
    reckless_reversible_baseline_reward: float
    omniscient_loss_control_reward: float
    no_loss_memory_loss: float
    no_value_at_risk_loss: float
    no_replacement_model_loss: float
    no_caution_control_loss: float
    no_tool_preservation_loss: float
    no_shelter_preservation_loss: float
    no_relationship_preservation_loss: float
    no_memory_backup_loss: float
    no_loss_response_loss: float
    no_continuity_loss: float
    reckless_reversible_baseline_loss: float
    selected_loss_events: float
    selected_preservation_actions: float
    selected_backup_actions: float
    selected_replan_actions: float
    selected_replacement_actions: float
    selected_caution_actions: float
    supports_irreversible_loss_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        index=0,
        name="reversible_wear_control",
        pressure="damage is reversible and replaceable, so irreversible-loss machinery should be rejected",
        expected_loss_memory=False,
        expected_value_at_risk=False,
        expected_replacement_model=False,
        expected_caution_control=False,
        expected_tool_preservation=False,
        expected_shelter_preservation=False,
        expected_relationship_preservation=False,
        expected_memory_backup=False,
        expected_loss_response=False,
        expected_continuity=False,
        tool_loss_pressure=0.04,
        shelter_loss_pressure=0.04,
        relationship_loss_pressure=0.00,
        memory_loss_pressure=0.02,
        replacement_pressure=0.02,
        cascade_pressure=0.00,
        required_progress=126.0,
        work_rate=0.74,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=1,
        name="irreplaceable_tool_shelter_loss",
        pressure="critical tool and shelter can be permanently lost under hazard pressure",
        expected_loss_memory=True,
        expected_value_at_risk=True,
        expected_replacement_model=True,
        expected_caution_control=True,
        expected_tool_preservation=True,
        expected_shelter_preservation=True,
        expected_relationship_preservation=False,
        expected_memory_backup=False,
        expected_loss_response=False,
        expected_continuity=False,
        tool_loss_pressure=0.86,
        shelter_loss_pressure=0.82,
        relationship_loss_pressure=0.08,
        memory_loss_pressure=0.10,
        replacement_pressure=0.78,
        cascade_pressure=0.18,
        required_progress=84.0,
        work_rate=0.50,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=2,
        name="permanent_relationship_loss",
        pressure="helper trust and repair access can be permanently lost by betrayal or neglect",
        expected_loss_memory=True,
        expected_value_at_risk=True,
        expected_replacement_model=False,
        expected_caution_control=True,
        expected_tool_preservation=False,
        expected_shelter_preservation=False,
        expected_relationship_preservation=True,
        expected_memory_backup=False,
        expected_loss_response=True,
        expected_continuity=False,
        tool_loss_pressure=0.10,
        shelter_loss_pressure=0.10,
        relationship_loss_pressure=0.88,
        memory_loss_pressure=0.12,
        replacement_pressure=0.34,
        cascade_pressure=0.42,
        required_progress=80.0,
        work_rate=0.51,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=3,
        name="memory_archive_permanent_loss",
        pressure="route, hazard, and commitment memory can be permanently lost unless backed up",
        expected_loss_memory=True,
        expected_value_at_risk=True,
        expected_replacement_model=True,
        expected_caution_control=False,
        expected_tool_preservation=False,
        expected_shelter_preservation=False,
        expected_relationship_preservation=False,
        expected_memory_backup=True,
        expected_loss_response=False,
        expected_continuity=False,
        tool_loss_pressure=0.12,
        shelter_loss_pressure=0.12,
        relationship_loss_pressure=0.12,
        memory_loss_pressure=0.88,
        replacement_pressure=0.70,
        cascade_pressure=0.22,
        required_progress=82.0,
        work_rate=0.52,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=4,
        name="cascading_loss_response",
        pressure="one permanent loss changes risk tolerance and replacement planning for the rest of the run",
        expected_loss_memory=True,
        expected_value_at_risk=True,
        expected_replacement_model=True,
        expected_caution_control=True,
        expected_tool_preservation=True,
        expected_shelter_preservation=True,
        expected_relationship_preservation=True,
        expected_memory_backup=False,
        expected_loss_response=True,
        expected_continuity=False,
        tool_loss_pressure=0.58,
        shelter_loss_pressure=0.56,
        relationship_loss_pressure=0.52,
        memory_loss_pressure=0.22,
        replacement_pressure=0.72,
        cascade_pressure=0.88,
        required_progress=72.0,
        work_rate=0.46,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=5,
        name="restore_irreversible_loss_continuity",
        pressure="after restore, already-lost tools, shelters, relationships, memories, and options must stay lost",
        expected_loss_memory=True,
        expected_value_at_risk=True,
        expected_replacement_model=True,
        expected_caution_control=True,
        expected_tool_preservation=True,
        expected_shelter_preservation=True,
        expected_relationship_preservation=True,
        expected_memory_backup=True,
        expected_loss_response=True,
        expected_continuity=True,
        tool_loss_pressure=0.54,
        shelter_loss_pressure=0.52,
        relationship_loss_pressure=0.50,
        memory_loss_pressure=0.50,
        replacement_pressure=0.62,
        cascade_pressure=0.62,
        required_progress=66.0,
        work_rate=0.44,
        restore_tick=96,
    ),
)


SEEDED_POLICIES = (
    Policy(
        name="reckless_reversible_baseline",
        loss_memory=False,
        value_at_risk=False,
        replacement_model=False,
        caution_control=False,
        tool_preservation=False,
        shelter_preservation=False,
        relationship_preservation=False,
        memory_backup=False,
        loss_response=False,
        continuity_memory=False,
        risk_threshold=0.90,
        preservation_bias=0.04,
        backup_bias=0.04,
        replan_bias=0.04,
    ),
    Policy(
        name="reactive_loss_avoider",
        loss_memory=True,
        value_at_risk=True,
        replacement_model=False,
        caution_control=True,
        tool_preservation=True,
        shelter_preservation=False,
        relationship_preservation=False,
        memory_backup=False,
        loss_response=False,
        continuity_memory=False,
        risk_threshold=0.52,
        preservation_bias=0.42,
        backup_bias=0.04,
        replan_bias=0.12,
    ),
    Policy(
        name="tool_shelter_guardian",
        loss_memory=True,
        value_at_risk=True,
        replacement_model=True,
        caution_control=True,
        tool_preservation=True,
        shelter_preservation=True,
        relationship_preservation=False,
        memory_backup=False,
        loss_response=False,
        continuity_memory=False,
        risk_threshold=0.30,
        preservation_bias=0.86,
        backup_bias=0.04,
        replan_bias=0.44,
    ),
    Policy(
        name="relationship_guardian",
        loss_memory=True,
        value_at_risk=True,
        replacement_model=False,
        caution_control=True,
        tool_preservation=False,
        shelter_preservation=False,
        relationship_preservation=True,
        memory_backup=False,
        loss_response=True,
        continuity_memory=False,
        risk_threshold=0.32,
        preservation_bias=0.72,
        backup_bias=0.04,
        replan_bias=0.76,
    ),
    Policy(
        name="memory_backup_planner",
        loss_memory=True,
        value_at_risk=True,
        replacement_model=True,
        caution_control=False,
        tool_preservation=False,
        shelter_preservation=False,
        relationship_preservation=False,
        memory_backup=True,
        loss_response=False,
        continuity_memory=False,
        risk_threshold=0.42,
        preservation_bias=0.18,
        backup_bias=0.90,
        replan_bias=0.52,
    ),
    Policy(
        name="loss_response_planner",
        loss_memory=True,
        value_at_risk=True,
        replacement_model=True,
        caution_control=True,
        tool_preservation=True,
        shelter_preservation=True,
        relationship_preservation=True,
        memory_backup=False,
        loss_response=True,
        continuity_memory=False,
        risk_threshold=0.26,
        preservation_bias=0.76,
        backup_bias=0.10,
        replan_bias=0.88,
    ),
    Policy(
        name="continuity_loss_planner",
        loss_memory=True,
        value_at_risk=True,
        replacement_model=True,
        caution_control=True,
        tool_preservation=True,
        shelter_preservation=True,
        relationship_preservation=True,
        memory_backup=True,
        loss_response=True,
        continuity_memory=True,
        risk_threshold=0.24,
        preservation_bias=0.78,
        backup_bias=0.82,
        replan_bias=0.84,
    ),
)


CONDITIONS = (
    "full_control",
    "no_loss_memory",
    "no_value_at_risk",
    "no_replacement_model",
    "no_caution_control",
    "no_tool_preservation",
    "no_shelter_preservation",
    "no_relationship_preservation",
    "no_memory_backup",
    "no_loss_response",
    "no_continuity",
    "reckless_reversible_baseline",
    "omniscient_loss_control",
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


def build_policies(cfg: LossConfig) -> List[Policy]:
    policies = list(SEEDED_POLICIES)
    rng = random.Random(cfg.seed + 3109)
    while len(policies) < cfg.candidate_count:
        base = rng.choice(SEEDED_POLICIES[2:])
        policies.append(
            Policy(
                name=f"mutant_loss_{len(policies)}",
                loss_memory=base.loss_memory if rng.random() > 0.10 else not base.loss_memory,
                value_at_risk=base.value_at_risk if rng.random() > 0.12 else not base.value_at_risk,
                replacement_model=base.replacement_model if rng.random() > 0.16 else not base.replacement_model,
                caution_control=base.caution_control if rng.random() > 0.16 else not base.caution_control,
                tool_preservation=base.tool_preservation if rng.random() > 0.16 else not base.tool_preservation,
                shelter_preservation=base.shelter_preservation if rng.random() > 0.16 else not base.shelter_preservation,
                relationship_preservation=base.relationship_preservation if rng.random() > 0.16 else not base.relationship_preservation,
                memory_backup=base.memory_backup if rng.random() > 0.16 else not base.memory_backup,
                loss_response=base.loss_response if rng.random() > 0.16 else not base.loss_response,
                continuity_memory=base.continuity_memory if rng.random() > 0.18 else not base.continuity_memory,
                risk_threshold=clamp(base.risk_threshold + rng.uniform(-0.08, 0.08), 0.14, 0.92),
                preservation_bias=clamp(base.preservation_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
                backup_bias=clamp(base.backup_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
                replan_bias=clamp(base.replan_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
            )
        )
    return policies


def condition_policy(policy: Policy, condition: str) -> Policy:
    if condition == "omniscient_loss_control":
        return Policy(
            name=policy.name,
            loss_memory=True,
            value_at_risk=True,
            replacement_model=True,
            caution_control=True,
            tool_preservation=True,
            shelter_preservation=True,
            relationship_preservation=True,
            memory_backup=True,
            loss_response=True,
            continuity_memory=True,
            risk_threshold=0.12,
            preservation_bias=max(policy.preservation_bias, 0.92),
            backup_bias=max(policy.backup_bias, 0.92),
            replan_bias=max(policy.replan_bias, 0.92),
        )
    if condition == "reckless_reversible_baseline":
        return Policy(
            name=policy.name,
            loss_memory=False,
            value_at_risk=False,
            replacement_model=False,
            caution_control=False,
            tool_preservation=False,
            shelter_preservation=False,
            relationship_preservation=False,
            memory_backup=False,
            loss_response=False,
            continuity_memory=False,
            risk_threshold=0.90,
            preservation_bias=0.04,
            backup_bias=0.04,
            replan_bias=0.04,
        )
    return Policy(
        name=policy.name,
        loss_memory=policy.loss_memory and condition != "no_loss_memory",
        value_at_risk=policy.value_at_risk and condition != "no_value_at_risk",
        replacement_model=policy.replacement_model and condition != "no_replacement_model",
        caution_control=policy.caution_control and condition != "no_caution_control",
        tool_preservation=policy.tool_preservation and condition != "no_tool_preservation",
        shelter_preservation=policy.shelter_preservation and condition != "no_shelter_preservation",
        relationship_preservation=policy.relationship_preservation and condition != "no_relationship_preservation",
        memory_backup=policy.memory_backup and condition != "no_memory_backup",
        loss_response=policy.loss_response and condition != "no_loss_response",
        continuity_memory=policy.continuity_memory and condition != "no_continuity",
        risk_threshold=policy.risk_threshold,
        preservation_bias=policy.preservation_bias,
        backup_bias=policy.backup_bias,
        replan_bias=policy.replan_bias,
    )


def scenario_seed(
    cfg: LossConfig,
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
        (policy.loss_memory, 2.40),
        (policy.value_at_risk, 2.70),
        (policy.replacement_model, 2.80),
        (policy.caution_control, 2.70),
        (policy.tool_preservation, 2.80),
        (policy.shelter_preservation, 2.80),
        (policy.relationship_preservation, 3.00),
        (policy.memory_backup, 2.90),
        (policy.loss_response, 3.10),
        (policy.continuity_memory, 9.60),
    ]
    return sum(weight for enabled, weight in weighted_flags if enabled)


def estimate_loss_risk(
    scenario: ScenarioSpec,
    policy: Policy,
    stress: float,
    tool_integrity: float,
    shelter_safety: float,
    relationship_trust: float,
    memory_integrity: float,
    option_space: float,
    replacement_feasibility: float,
    caution_state: float,
) -> float:
    if policy.value_at_risk:
        observed_tool = tool_integrity
        observed_shelter = shelter_safety
        observed_relationship = relationship_trust
        observed_memory = memory_integrity
        observed_options = option_space
    else:
        observed_tool = 0.72
        observed_shelter = 0.72
        observed_relationship = 0.72
        observed_memory = 0.72
        observed_options = 0.78
    load = (
        scenario.tool_loss_pressure * (1.0 - observed_tool) * 0.64
        + scenario.shelter_loss_pressure * (1.0 - observed_shelter) * 0.62
        + scenario.relationship_loss_pressure * (1.0 - observed_relationship) * 0.58
        + scenario.memory_loss_pressure * (1.0 - observed_memory) * 0.58
        + scenario.replacement_pressure * (1.0 - replacement_feasibility) * 0.44
        + scenario.cascade_pressure * (1.0 - observed_options) * 0.46
        + stress * 0.30
    )
    mitigation = (
        (0.10 if policy.loss_memory else 0.0)
        + (0.11 if policy.value_at_risk else 0.0)
        + (0.10 if policy.replacement_model else 0.0)
        + (0.12 if policy.caution_control else 0.0)
        + (0.11 if policy.tool_preservation else 0.0)
        + (0.11 if policy.shelter_preservation else 0.0)
        + (0.11 if policy.relationship_preservation else 0.0)
        + (0.11 if policy.memory_backup else 0.0)
        + (0.12 if policy.loss_response else 0.0)
        + caution_state * (0.16 if policy.caution_control else 0.04)
    )
    return clamp(load - mitigation, 0.0, 1.8)


def choose_action(
    scenario: ScenarioSpec,
    policy: Policy,
    risk: float,
    stress: float,
    tool_integrity: float,
    shelter_safety: float,
    relationship_trust: float,
    memory_integrity: float,
    replacement_feasibility: float,
    caution_state: float,
    tick: int,
) -> str:
    if scenario.index == 0:
        return "work"
    if policy.tool_preservation and scenario.expected_tool_preservation and tool_integrity < 0.66 and risk > policy.risk_threshold * 0.56:
        return "preserve_tool"
    if policy.shelter_preservation and scenario.expected_shelter_preservation and shelter_safety < 0.66 and risk > policy.risk_threshold * 0.56:
        return "reinforce_shelter"
    if (
        policy.relationship_preservation
        and scenario.expected_relationship_preservation
        and relationship_trust < 0.68
        and tick % 5 == 0
    ):
        return "preserve_relationship"
    if policy.memory_backup and scenario.expected_memory_backup and memory_integrity < 0.72 and tick % 5 == 0:
        return "backup_memory"
    if (
        policy.replacement_model
        and scenario.expected_replacement_model
        and replacement_feasibility < 0.62
        and risk > policy.risk_threshold * 0.70
    ):
        return "plan_replacement"
    if (
        policy.loss_response
        and scenario.expected_loss_response
        and (stress > 0.50 or caution_state < 0.54)
        and tick % 7 == 0
    ):
        return "loss_replan"
    if policy.caution_control and scenario.expected_caution_control and risk > policy.risk_threshold:
        return "cautious_pause"
    return "work"


def add_trace(
    trace: List[Dict[str, object]],
    tick: int,
    action: str,
    progress: float,
    energy: float,
    integrity: float,
    stress: float,
    tool_integrity: float,
    shelter_safety: float,
    relationship_trust: float,
    memory_integrity: float,
    option_space: float,
    value_at_risk_estimate: float,
    replacement_feasibility: float,
    caution_state: float,
    loss_events: int,
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
            "tool_integrity": round(tool_integrity, 3),
            "shelter_safety": round(shelter_safety, 3),
            "relationship_trust": round(relationship_trust, 3),
            "memory_integrity": round(memory_integrity, 3),
            "option_space": round(option_space, 3),
            "value_at_risk_estimate": round(value_at_risk_estimate, 3),
            "replacement_feasibility": round(replacement_feasibility, 3),
            "caution_state": round(caution_state, 3),
            "loss_events": loss_events,
            "notes": list(notes[-3:]),
        }
    )


def simulate_episode(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episode: int,
    cfg: LossConfig,
    phase: str,
    collect_trace: bool = False,
) -> Tuple[EpisodeResult, List[Dict[str, object]]]:
    effective = condition_policy(policy, condition)
    rng = random.Random(scenario_seed(cfg, scenario, policy, condition, episode, phase))

    energy = clamp(0.96 - scenario.replacement_pressure * 0.03 + rng.uniform(-0.010, 0.010), 0.0, 1.0)
    integrity = clamp(0.98 - scenario.cascade_pressure * 0.03 + rng.uniform(-0.010, 0.010), 0.0, 1.0)
    stress = clamp(0.15 + scenario.cascade_pressure * 0.08, 0.0, 1.2)
    tool_integrity = 0.56 if scenario.expected_tool_preservation else 0.86
    shelter_safety = 0.56 if scenario.expected_shelter_preservation else 0.86
    relationship_trust = 0.58 if scenario.expected_relationship_preservation else 0.86
    memory_integrity = 0.58 if scenario.expected_memory_backup else 0.86
    option_space = 0.90
    value_at_risk_estimate = 0.44 if scenario.expected_value_at_risk else 0.12
    replacement_feasibility = 0.42 if scenario.expected_replacement_model else 0.82
    caution_state = 0.46 if scenario.expected_caution_control else 0.78
    progress = 0.0
    collapsed = False
    notes: List[str] = []
    trace_frames: List[Dict[str, object]] = []

    tool_lost = False
    shelter_lost = False
    relationship_lost = False
    memory_lost = False

    loss_events = 0
    tool_loss_events = 0
    shelter_loss_events = 0
    relationship_loss_events = 0
    memory_loss_events = 0
    preservation_actions = 0
    backup_actions = 0
    replan_actions = 0
    replacement_actions = 0
    caution_actions = 0
    continuity_resets = 0
    loss_misses = 0

    for tick in range(cfg.ticks):
        action = "work"
        if scenario.restore_tick == tick and not effective.continuity_memory:
            continuity_resets += 1
            loss_misses += 10
            tool_lost = scenario.expected_tool_preservation
            shelter_lost = scenario.expected_shelter_preservation
            relationship_lost = scenario.expected_relationship_preservation
            memory_lost = scenario.expected_memory_backup
            tool_integrity = 0.0 if tool_lost else clamp(tool_integrity - 0.20, 0.0, 1.0)
            shelter_safety = 0.0 if shelter_lost else clamp(shelter_safety - 0.20, 0.0, 1.0)
            relationship_trust = 0.0 if relationship_lost else clamp(relationship_trust - 0.24, 0.0, 1.0)
            memory_integrity = 0.0 if memory_lost else clamp(memory_integrity - 0.24, 0.0, 1.0)
            option_space = clamp(option_space - 0.36, 0.0, 1.0)
            value_at_risk_estimate = clamp(value_at_risk_estimate + 0.24, 0.0, 1.0)
            replacement_feasibility = clamp(replacement_feasibility - 0.30, 0.0, 1.0)
            caution_state = clamp(caution_state - 0.22, 0.0, 1.0)
            stress = clamp(stress + 0.28, 0.0, 1.2)
            loss_events += int(tool_lost) + int(shelter_lost) + int(relationship_lost) + int(memory_lost)
            notes.append("restore forgot irreversible losses")
            action = "restore_reset"

        risk = estimate_loss_risk(
            scenario,
            effective,
            stress,
            tool_integrity,
            shelter_safety,
            relationship_trust,
            memory_integrity,
            option_space,
            replacement_feasibility,
            caution_state,
        )
        if not collapsed and action != "restore_reset":
            action = choose_action(
                scenario,
                effective,
                risk,
                stress,
                tool_integrity,
                shelter_safety,
                relationship_trust,
                memory_integrity,
                replacement_feasibility,
                caution_state,
                tick,
            )

        if collapsed:
            action = "collapsed"
        elif action == "preserve_tool":
            preservation_actions += 1
            tool_integrity = clamp(tool_integrity + 0.24 + effective.preservation_bias * 0.08, 0.0, 1.0)
            value_at_risk_estimate = clamp(value_at_risk_estimate - 0.05, 0.0, 1.0)
            stress = clamp(stress - 0.040, 0.0, 1.2)
            energy = clamp(energy - 0.012, 0.0, 1.0)
            progress += scenario.work_rate * 0.04
            notes.append("tool preservation protected future options")
        elif action == "reinforce_shelter":
            preservation_actions += 1
            shelter_safety = clamp(shelter_safety + 0.24 + effective.preservation_bias * 0.08, 0.0, 1.0)
            value_at_risk_estimate = clamp(value_at_risk_estimate - 0.04, 0.0, 1.0)
            stress = clamp(stress - 0.036, 0.0, 1.2)
            energy = clamp(energy - 0.012, 0.0, 1.0)
            progress += scenario.work_rate * 0.04
            notes.append("shelter reinforcement avoided permanent exposure loss")
        elif action == "preserve_relationship":
            preservation_actions += 1
            relationship_trust = clamp(relationship_trust + 0.24 + effective.preservation_bias * 0.08, 0.0, 1.0)
            option_space = clamp(option_space + 0.018, 0.0, 1.0)
            stress = clamp(stress - 0.030, 0.0, 1.2)
            progress += scenario.work_rate * 0.03
            notes.append("relationship preservation kept future help available")
        elif action == "backup_memory":
            backup_actions += 1
            memory_integrity = clamp(memory_integrity + 0.30 + effective.backup_bias * 0.08, 0.0, 1.0)
            option_space = clamp(option_space + 0.012, 0.0, 1.0)
            progress -= 0.10
            notes.append("memory backup preserved route and loss history")
        elif action == "plan_replacement":
            replacement_actions += 1
            replacement_feasibility = clamp(replacement_feasibility + 0.24 + effective.replan_bias * 0.08, 0.0, 1.0)
            value_at_risk_estimate = clamp(value_at_risk_estimate - 0.06, 0.0, 1.0)
            progress -= 0.08
            notes.append("replacement planning reduced all-or-nothing exposure")
        elif action == "loss_replan":
            replan_actions += 1
            caution_state = clamp(caution_state + 0.22 + effective.replan_bias * 0.08, 0.0, 1.0)
            stress = clamp(stress - 0.16, 0.0, 1.2)
            option_space = clamp(option_space + 0.016, 0.0, 1.0)
            progress -= 0.08
            notes.append("loss response changed risk tolerance under permanent-loss pressure")
        elif action == "cautious_pause":
            caution_actions += 1
            caution_state = clamp(caution_state + 0.18, 0.0, 1.0)
            stress = clamp(stress - 0.11, 0.0, 1.2)
            energy = clamp(energy + 0.010, 0.0, 1.0)
            progress -= 0.06
            notes.append("caution delayed work to avoid irreversible loss")
        elif action == "work":
            usable_tool = 0.0 if tool_lost else tool_integrity
            usable_shelter = 0.0 if shelter_lost else shelter_safety
            usable_relationship = 0.0 if relationship_lost else relationship_trust
            usable_memory = 0.0 if memory_lost else memory_integrity
            option_bonus = (
                usable_tool * scenario.tool_loss_pressure * 0.07
                + usable_shelter * scenario.shelter_loss_pressure * 0.06
                + usable_relationship * scenario.relationship_loss_pressure * 0.06
                + usable_memory * scenario.memory_loss_pressure * 0.06
                + replacement_feasibility * scenario.replacement_pressure * 0.04
            )
            loss_burden = (
                (1.0 - usable_tool) * scenario.tool_loss_pressure * 0.12
                + (1.0 - usable_shelter) * scenario.shelter_loss_pressure * 0.12
                + (1.0 - usable_relationship) * scenario.relationship_loss_pressure * 0.11
                + (1.0 - usable_memory) * scenario.memory_loss_pressure * 0.11
                + stress * 0.10
            )
            progress += scenario.work_rate * clamp(0.70 + energy * 0.09 + option_bonus - loss_burden, 0.02, 1.08)

        if scenario.index != 0:
            tool_integrity = 0.0 if tool_lost else clamp(tool_integrity - scenario.tool_loss_pressure * 0.0019, 0.0, 1.0)
            shelter_safety = 0.0 if shelter_lost else clamp(shelter_safety - scenario.shelter_loss_pressure * 0.0019, 0.0, 1.0)
            relationship_trust = 0.0 if relationship_lost else clamp(relationship_trust - scenario.relationship_loss_pressure * 0.0018, 0.0, 1.0)
            memory_integrity = 0.0 if memory_lost else clamp(memory_integrity - scenario.memory_loss_pressure * 0.0018, 0.0, 1.0)
            replacement_feasibility = clamp(replacement_feasibility - scenario.replacement_pressure * 0.0009, 0.0, 1.0)
            caution_state = clamp(caution_state - scenario.cascade_pressure * 0.0009, 0.0, 1.0)

        if scenario.expected_loss_memory and not effective.loss_memory:
            value_at_risk_estimate = clamp(value_at_risk_estimate + 0.0038, 0.0, 1.0)
            stress = clamp(stress + 0.0028, 0.0, 1.2)
            loss_misses += 1 if tick % 13 == 0 else 0
        if scenario.expected_value_at_risk and not effective.value_at_risk:
            option_space = clamp(option_space - 0.0048, 0.0, 1.0)
            value_at_risk_estimate = clamp(value_at_risk_estimate + 0.0048, 0.0, 1.0)
            loss_misses += 1 if tick % 11 == 0 else 0
        if scenario.expected_replacement_model:
            if effective.replacement_model:
                replacement_feasibility = clamp(replacement_feasibility + scenario.replacement_pressure * 0.0008, 0.0, 1.0)
            else:
                replacement_feasibility = clamp(replacement_feasibility - scenario.replacement_pressure * 0.0066, 0.0, 1.0)
                option_space = clamp(option_space - scenario.replacement_pressure * 0.0034, 0.0, 1.0)
                loss_misses += 1 if tick % 13 == 0 else 0
        if scenario.expected_caution_control:
            if effective.caution_control:
                caution_state = clamp(caution_state + scenario.cascade_pressure * 0.0008, 0.0, 1.0)
            else:
                caution_state = clamp(caution_state - scenario.cascade_pressure * 0.0068, 0.0, 1.0)
                stress = clamp(stress + scenario.cascade_pressure * 0.0044, 0.0, 1.2)
                loss_misses += 1 if tick % 11 == 0 else 0
        if scenario.expected_tool_preservation:
            if effective.tool_preservation:
                tool_integrity = 0.0 if tool_lost else clamp(tool_integrity + scenario.tool_loss_pressure * 0.0008, 0.0, 1.0)
            else:
                tool_integrity = 0.0 if tool_lost else clamp(tool_integrity - scenario.tool_loss_pressure * 0.0072, 0.0, 1.0)
                loss_misses += 1 if tick % 11 == 0 else 0
        if scenario.expected_shelter_preservation:
            if effective.shelter_preservation:
                shelter_safety = 0.0 if shelter_lost else clamp(shelter_safety + scenario.shelter_loss_pressure * 0.0008, 0.0, 1.0)
            else:
                shelter_safety = 0.0 if shelter_lost else clamp(shelter_safety - scenario.shelter_loss_pressure * 0.0070, 0.0, 1.0)
                loss_misses += 1 if tick % 11 == 0 else 0
        if scenario.expected_relationship_preservation:
            if effective.relationship_preservation:
                relationship_trust = 0.0 if relationship_lost else clamp(relationship_trust + scenario.relationship_loss_pressure * 0.0008, 0.0, 1.0)
            else:
                relationship_trust = 0.0 if relationship_lost else clamp(relationship_trust - scenario.relationship_loss_pressure * 0.0070, 0.0, 1.0)
                loss_misses += 1 if tick % 11 == 0 else 0
        if scenario.expected_memory_backup:
            if effective.memory_backup:
                memory_integrity = 0.0 if memory_lost else clamp(memory_integrity + scenario.memory_loss_pressure * 0.0008, 0.0, 1.0)
            else:
                memory_integrity = 0.0 if memory_lost else clamp(memory_integrity - scenario.memory_loss_pressure * 0.0072, 0.0, 1.0)
                loss_misses += 1 if tick % 11 == 0 else 0
        if scenario.expected_loss_response:
            if effective.loss_response:
                stress = clamp(stress - scenario.cascade_pressure * 0.0006, 0.0, 1.2)
                option_space = clamp(option_space + scenario.cascade_pressure * 0.0004, 0.0, 1.0)
            else:
                stress = clamp(stress + scenario.cascade_pressure * 0.0062, 0.0, 1.2)
                option_space = clamp(option_space - scenario.cascade_pressure * 0.0040, 0.0, 1.0)
                loss_misses += 1 if tick % 13 == 0 else 0

        if scenario.index != 0 and tick % 17 == 0:
            if not tool_lost and scenario.expected_tool_preservation and tool_integrity < 0.12:
                tool_lost = True
                tool_integrity = 0.0
                tool_loss_events += 1
                loss_events += 1
                option_space = clamp(option_space - 0.16, 0.0, 1.0)
                stress = clamp(stress + 0.08, 0.0, 1.2)
                notes.append("critical tool permanently lost")
            if not shelter_lost and scenario.expected_shelter_preservation and shelter_safety < 0.12:
                shelter_lost = True
                shelter_safety = 0.0
                shelter_loss_events += 1
                loss_events += 1
                option_space = clamp(option_space - 0.16, 0.0, 1.0)
                stress = clamp(stress + 0.08, 0.0, 1.2)
                notes.append("safe shelter permanently lost")
            if not relationship_lost and scenario.expected_relationship_preservation and relationship_trust < 0.12:
                relationship_lost = True
                relationship_trust = 0.0
                relationship_loss_events += 1
                loss_events += 1
                option_space = clamp(option_space - 0.18, 0.0, 1.0)
                stress = clamp(stress + 0.10, 0.0, 1.2)
                notes.append("helper relationship permanently lost")
            if not memory_lost and scenario.expected_memory_backup and memory_integrity < 0.12:
                memory_lost = True
                memory_integrity = 0.0
                memory_loss_events += 1
                loss_events += 1
                option_space = clamp(option_space - 0.18, 0.0, 1.0)
                stress = clamp(stress + 0.10, 0.0, 1.2)
                notes.append("critical route memory permanently lost")

        if loss_events > 0:
            value_at_risk_estimate = clamp(value_at_risk_estimate + scenario.cascade_pressure * 0.0020, 0.0, 1.0)
            if effective.loss_response:
                caution_state = clamp(caution_state + scenario.cascade_pressure * 0.0018, 0.0, 1.0)
            else:
                stress = clamp(stress + scenario.cascade_pressure * 0.0024, 0.0, 1.2)

        energy = clamp(energy - 0.0012 - stress * 0.0008 + (0.0008 if action == "cautious_pause" else 0.0), 0.0, 1.0)
        integrity = clamp(integrity - scenario.cascade_pressure * (1.0 - option_space) * 0.0011 - stress * 0.0005, 0.0, 1.0)
        if energy <= 0.04 or integrity <= 0.06 or stress >= 1.12 or option_space <= 0.04:
            collapsed = True

        if collect_trace and (tick % 5 == 0 or tick == cfg.ticks - 1 or action != "work" or loss_events > 0):
            add_trace(
                trace_frames,
                tick,
                action,
                progress,
                energy,
                integrity,
                stress,
                tool_integrity,
                shelter_safety,
                relationship_trust,
                memory_integrity,
                option_space,
                value_at_risk_estimate,
                replacement_feasibility,
                caution_state,
                loss_events,
                notes,
            )

    task_success = progress >= scenario.required_progress and not collapsed
    survival = 1.0 if not collapsed and energy > 0.06 and integrity > 0.10 and option_space > 0.08 else 0.0

    reward = progress
    reward += 34.0 if task_success else -24.0
    reward += 42.0 if survival else -124.0
    reward += energy * 16.0
    reward += integrity * 16.0
    reward -= stress * 46.0
    reward += tool_integrity * (30.0 if scenario.expected_tool_preservation else 1.0)
    reward += shelter_safety * (30.0 if scenario.expected_shelter_preservation else 1.0)
    reward += relationship_trust * (34.0 if scenario.expected_relationship_preservation else 1.0)
    reward += memory_integrity * (34.0 if scenario.expected_memory_backup else 1.0)
    reward += option_space * 42.0
    reward += replacement_feasibility * (24.0 if scenario.expected_replacement_model else 1.0)
    reward += caution_state * (22.0 if scenario.expected_caution_control else 1.0)
    reward -= value_at_risk_estimate * 30.0
    reward -= loss_events * 56.0
    reward -= tool_loss_events * 52.0
    reward -= shelter_loss_events * 52.0
    reward -= relationship_loss_events * 60.0
    reward -= memory_loss_events * 60.0
    reward -= loss_misses * 0.90
    reward -= preservation_actions * 0.12
    reward -= backup_actions * 0.16
    reward -= replan_actions * 0.14
    reward -= replacement_actions * 0.14
    reward -= caution_actions * 0.12
    reward -= feature_overhead(effective)
    if scenario.expected_continuity and continuity_resets:
        reward -= 110.0
    if scenario.expected_loss_memory and not effective.loss_memory:
        reward -= 74.0 + scenario.cascade_pressure * 40.0
    if scenario.expected_value_at_risk and not effective.value_at_risk:
        reward -= 64.0 + scenario.cascade_pressure * 36.0
    if scenario.expected_replacement_model and not effective.replacement_model:
        reward -= scenario.replacement_pressure * 130.0
    if scenario.expected_caution_control and not effective.caution_control:
        reward -= 72.0 + scenario.cascade_pressure * 110.0
    if scenario.expected_tool_preservation and not effective.tool_preservation:
        reward -= scenario.tool_loss_pressure * 150.0
    if scenario.expected_shelter_preservation and not effective.shelter_preservation:
        reward -= scenario.shelter_loss_pressure * 150.0
    if scenario.expected_relationship_preservation and not effective.relationship_preservation:
        reward -= scenario.relationship_loss_pressure * 158.0
    if scenario.expected_memory_backup and not effective.memory_backup:
        reward -= scenario.memory_loss_pressure * 160.0
    if scenario.expected_loss_response and not effective.loss_response:
        reward -= 72.0 + scenario.cascade_pressure * 140.0

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
        tool_integrity=tool_integrity,
        shelter_safety=shelter_safety,
        relationship_trust=relationship_trust,
        memory_integrity=memory_integrity,
        option_space=option_space,
        value_at_risk_estimate=value_at_risk_estimate,
        replacement_feasibility=replacement_feasibility,
        caution_state=caution_state,
        loss_events=loss_events,
        tool_loss_events=tool_loss_events,
        shelter_loss_events=shelter_loss_events,
        relationship_loss_events=relationship_loss_events,
        memory_loss_events=memory_loss_events,
        preservation_actions=preservation_actions,
        backup_actions=backup_actions,
        replan_actions=replan_actions,
        replacement_actions=replacement_actions,
        caution_actions=caution_actions,
        continuity_resets=continuity_resets,
        loss_misses=loss_misses,
    )
    return result, trace_frames


def evaluate_policy(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episodes: int,
    cfg: LossConfig,
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
                    mean_tool_integrity=mean(row.tool_integrity for row in subset),
                    mean_shelter_safety=mean(row.shelter_safety for row in subset),
                    mean_relationship_trust=mean(row.relationship_trust for row in subset),
                    mean_memory_integrity=mean(row.memory_integrity for row in subset),
                    mean_option_space=mean(row.option_space for row in subset),
                    mean_value_at_risk_estimate=mean(row.value_at_risk_estimate for row in subset),
                    mean_replacement_feasibility=mean(row.replacement_feasibility for row in subset),
                    mean_caution_state=mean(row.caution_state for row in subset),
                    mean_loss_events=mean(row.loss_events for row in subset),
                    mean_tool_loss_events=mean(row.tool_loss_events for row in subset),
                    mean_shelter_loss_events=mean(row.shelter_loss_events for row in subset),
                    mean_relationship_loss_events=mean(row.relationship_loss_events for row in subset),
                    mean_memory_loss_events=mean(row.memory_loss_events for row in subset),
                    mean_preservation_actions=mean(row.preservation_actions for row in subset),
                    mean_backup_actions=mean(row.backup_actions for row in subset),
                    mean_replan_actions=mean(row.replan_actions for row in subset),
                    mean_replacement_actions=mean(row.replacement_actions for row in subset),
                    mean_caution_actions=mean(row.caution_actions for row in subset),
                    mean_continuity_resets=mean(row.continuity_resets for row in subset),
                    mean_loss_misses=mean(row.loss_misses for row in subset),
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
                full.policy_name == "reckless_reversible_baseline"
                and max(
                    abs(losses[condition])
                    for condition in CONDITIONS
                    if condition not in {"full_control", "omniscient_loss_control"}
                )
                < 8.0
            )
            verdict = "loss_machinery_rejected_in_reversible_control"
        elif scenario.index == 1:
            supports = (
                losses["no_loss_memory"] > 40.0
                and losses["no_value_at_risk"] > 35.0
                and losses["no_replacement_model"] > 30.0
                and losses["no_caution_control"] > 60.0
                and losses["no_tool_preservation"] > 80.0
                and losses["no_shelter_preservation"] > 80.0
                and losses["reckless_reversible_baseline"] > 60.0
            )
            verdict = "irreplaceable_tool_shelter_loss_pressure"
        elif scenario.index == 2:
            supports = (
                losses["no_loss_memory"] > 40.0
                and losses["no_value_at_risk"] > 35.0
                and losses["no_caution_control"] > 45.0
                and losses["no_relationship_preservation"] > 90.0
                and losses["no_loss_response"] > 50.0
                and losses["reckless_reversible_baseline"] > 60.0
            )
            verdict = "permanent_relationship_loss_pressure"
        elif scenario.index == 3:
            supports = (
                losses["no_loss_memory"] > 35.0
                and losses["no_value_at_risk"] > 40.0
                and losses["no_replacement_model"] > 30.0
                and losses["no_memory_backup"] > 90.0
                and losses["reckless_reversible_baseline"] > 55.0
            )
            verdict = "memory_archive_permanent_loss_pressure"
        elif scenario.index == 4:
            supports = (
                losses["no_loss_memory"] > 40.0
                and losses["no_value_at_risk"] > 50.0
                and losses["no_replacement_model"] > 45.0
                and losses["no_caution_control"] > 80.0
                and losses["no_loss_response"] > 90.0
                and losses["reckless_reversible_baseline"] > 60.0
            )
            verdict = "cascading_loss_response_pressure"
        else:
            supports = (
                losses["no_continuity"] > 54.0
                and losses["no_loss_memory"] > 40.0
                and losses["no_value_at_risk"] > 40.0
                and losses["no_replacement_model"] > 40.0
                and losses["no_caution_control"] > 40.0
                and losses["no_tool_preservation"] > 40.0
                and losses["no_shelter_preservation"] > 40.0
                and losses["no_relationship_preservation"] > 40.0
                and losses["no_memory_backup"] > 40.0
                and losses["no_loss_response"] > 40.0
            )
            verdict = "restore_irreversible_loss_continuity_pressure"

        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                expected_pressure=scenario.pressure,
                selected_policy=full.policy_name,
                selected_reward=full.mean_reward,
                no_loss_memory_reward=rewards["no_loss_memory"],
                no_value_at_risk_reward=rewards["no_value_at_risk"],
                no_replacement_model_reward=rewards["no_replacement_model"],
                no_caution_control_reward=rewards["no_caution_control"],
                no_tool_preservation_reward=rewards["no_tool_preservation"],
                no_shelter_preservation_reward=rewards["no_shelter_preservation"],
                no_relationship_preservation_reward=rewards["no_relationship_preservation"],
                no_memory_backup_reward=rewards["no_memory_backup"],
                no_loss_response_reward=rewards["no_loss_response"],
                no_continuity_reward=rewards["no_continuity"],
                reckless_reversible_baseline_reward=rewards["reckless_reversible_baseline"],
                omniscient_loss_control_reward=rewards["omniscient_loss_control"],
                no_loss_memory_loss=losses["no_loss_memory"],
                no_value_at_risk_loss=losses["no_value_at_risk"],
                no_replacement_model_loss=losses["no_replacement_model"],
                no_caution_control_loss=losses["no_caution_control"],
                no_tool_preservation_loss=losses["no_tool_preservation"],
                no_shelter_preservation_loss=losses["no_shelter_preservation"],
                no_relationship_preservation_loss=losses["no_relationship_preservation"],
                no_memory_backup_loss=losses["no_memory_backup"],
                no_loss_response_loss=losses["no_loss_response"],
                no_continuity_loss=losses["no_continuity"],
                reckless_reversible_baseline_loss=losses["reckless_reversible_baseline"],
                selected_loss_events=full.mean_loss_events,
                selected_preservation_actions=full.mean_preservation_actions,
                selected_backup_actions=full.mean_backup_actions,
                selected_replan_actions=full.mean_replan_actions,
                selected_replacement_actions=full.mean_replacement_actions,
                selected_caution_actions=full.mean_caution_actions,
                supports_irreversible_loss_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def select_policies(cfg: LossConfig, policies: Sequence[Policy]) -> Tuple[Dict[int, Policy], List[PolicySelectionRow]]:
    selected: Dict[int, Policy] = {}
    rows: List[PolicySelectionRow] = []
    reckless = next(policy for policy in policies if policy.name == "reckless_reversible_baseline")
    for scenario in SCENARIOS:
        scores: List[Tuple[float, Policy]] = []
        for policy in policies:
            train_rows = evaluate_policy(scenario, policy, "full_control", cfg.train_episodes, cfg, "train")
            scores.append((mean(row.total_reward for row in train_rows), policy))
        scores.sort(key=lambda item: item[0], reverse=True)
        best_reward, best_policy = scores[0]
        reckless_rows = evaluate_policy(scenario, reckless, "full_control", cfg.train_episodes, cfg, "train_reckless")
        reckless_reward = mean(row.total_reward for row in reckless_rows)
        selected[scenario.index] = best_policy
        rows.append(
            PolicySelectionRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                selected_policy=best_policy.name,
                selected_uses_loss_memory=best_policy.loss_memory,
                selected_uses_value_at_risk=best_policy.value_at_risk,
                selected_uses_replacement_model=best_policy.replacement_model,
                selected_uses_caution_control=best_policy.caution_control,
                selected_uses_tool_preservation=best_policy.tool_preservation,
                selected_uses_shelter_preservation=best_policy.shelter_preservation,
                selected_uses_relationship_preservation=best_policy.relationship_preservation,
                selected_uses_memory_backup=best_policy.memory_backup,
                selected_uses_loss_response=best_policy.loss_response,
                selected_uses_continuity=best_policy.continuity_memory,
                train_reward=best_reward,
                reckless_train_reward=reckless_reward,
                train_gain_over_reckless=best_reward - reckless_reward,
            )
        )
    return selected, rows


def run_eval(cfg: LossConfig, selected: Dict[int, Policy]) -> List[EpisodeResult]:
    eval_rows: List[EpisodeResult] = []
    for scenario in SCENARIOS:
        policy = selected[scenario.index]
        for condition in CONDITIONS:
            eval_rows.extend(evaluate_policy(scenario, policy, condition, cfg.eval_episodes, cfg, "eval"))
    return eval_rows


def build_trace(
    cfg: LossConfig,
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
        "loss_memory",
        "value_risk",
        "replacement",
        "caution",
        "tool",
        "shelter",
        "relationship",
        "memory_backup",
        "loss_response",
        "continuity",
        "supports",
    ]
    rows = [
        [
            row.scenario_name,
            row.selected_policy,
            f"{row.no_loss_memory_loss:.3f}",
            f"{row.no_value_at_risk_loss:.3f}",
            f"{row.no_replacement_model_loss:.3f}",
            f"{row.no_caution_control_loss:.3f}",
            f"{row.no_tool_preservation_loss:.3f}",
            f"{row.no_shelter_preservation_loss:.3f}",
            f"{row.no_relationship_preservation_loss:.3f}",
            f"{row.no_memory_backup_loss:.3f}",
            f"{row.no_loss_response_loss:.3f}",
            f"{row.no_continuity_loss:.3f}",
            str(row.supports_irreversible_loss_precursor),
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


def parse_args() -> LossConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-episodes", type=int, default=LossConfig.train_episodes)
    parser.add_argument("--eval-episodes", type=int, default=LossConfig.eval_episodes)
    parser.add_argument("--ticks", type=int, default=LossConfig.ticks)
    parser.add_argument("--seed", type=int, default=LossConfig.seed)
    parser.add_argument("--candidate-count", type=int, default=LossConfig.candidate_count)
    parser.add_argument("--trace-scenario", type=int, default=LossConfig.trace_scenario)
    parser.add_argument("--trace-episode", type=int, default=LossConfig.trace_episode)
    args = parser.parse_args()
    return LossConfig(
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

    prefix = ARTIFACT_DIR / "ssrm_3d_irreversible_loss"
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
    write_js(prefix.with_name(prefix.name + "_results.js"), "SSRM_3D_IRREVERSIBLE_LOSS_RESULTS", results)
    write_js(prefix.with_name(prefix.name + "_trace.js"), "SSRM_3D_IRREVERSIBLE_LOSS_TRACE", trace)
    print_verdicts(verdict_rows)
    return 0 if all(row.supports_irreversible_loss_precursor for row in verdict_rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
