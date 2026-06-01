#!/usr/bin/env python3
"""SSRM-3D social trust/contracts precursor.

This experiment implements the sixth pressure-layer step from report 74:
social trust and contracts. It is intentionally not a society simulator.
Promises, tool return, warning, sharing, repair debt, trust updates, ownership,
and continuity are abstract control variables.

The useful result is narrow: contract machinery should be rejected in a stable
control, then become useful only when delayed social consequences change future
access, help, tool use, shelter safety, or restore continuity.
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
class ContractConfig:
    train_episodes: int = 72
    eval_episodes: int = 96
    ticks: int = 180
    seed: int = 20260625
    candidate_count: int = 7
    trace_scenario: int = 4
    trace_episode: int = 0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    contract_type: str
    expected_commitment_pressure: bool
    expected_identity_pressure: bool
    expected_communication_pressure: bool
    expected_trust_pressure: bool
    expected_ownership_pressure: bool
    expected_repair_debt_pressure: bool
    expected_continuity_pressure: bool
    contract_value: float
    immediate_cost: float
    break_penalty: float
    reciprocity_value: float
    hazard_pressure: float
    resource_pressure: float
    shelter_pressure: float
    required_progress: float
    work_rate: float
    offer_tick: int
    due_tick: int
    payoff_tick: int
    restore_tick: int


@dataclass(frozen=True)
class Policy:
    name: str
    commitment_memory: bool
    identity_memory: bool
    communication_action: bool
    trust_update: bool
    ownership_memory: bool
    repair_debt_memory: bool
    continuity_memory: bool
    promise_bias: float
    reciprocity_bias: float
    risk_tolerance: float
    selfish_bias: float


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
    resources: float
    trust: float
    reputation: float
    future_access: float
    shelter_quality: float
    social_penalty: float
    commitments_kept: int
    commitments_broken: int
    communication_actions: int
    tool_return_actions: int
    warning_actions: int
    share_actions: int
    repair_contributions: int
    reciprocity_received: int
    continuity_resets: int
    contract_misses: int
    wrong_agent_events: int


@dataclass(frozen=True)
class PolicySelectionRow:
    scenario: int
    scenario_name: str
    selected_policy: str
    selected_uses_commitment_memory: bool
    selected_uses_identity_memory: bool
    selected_uses_communication_action: bool
    selected_uses_trust_update: bool
    selected_uses_ownership_memory: bool
    selected_uses_repair_debt_memory: bool
    selected_uses_continuity: bool
    train_reward: float
    no_contract_train_reward: float
    train_gain_over_no_contract: float


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
    mean_resources: float
    mean_trust: float
    mean_reputation: float
    mean_future_access: float
    mean_shelter_quality: float
    mean_social_penalty: float
    mean_commitments_kept: float
    mean_commitments_broken: float
    mean_communication_actions: float
    mean_tool_return_actions: float
    mean_warning_actions: float
    mean_share_actions: float
    mean_repair_contributions: float
    mean_reciprocity_received: float
    mean_continuity_resets: float
    mean_contract_misses: float
    mean_wrong_agent_events: float


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    expected_pressure: str
    selected_policy: str
    selected_reward: float
    no_commitment_memory_reward: float
    no_identity_memory_reward: float
    no_communication_action_reward: float
    no_trust_update_reward: float
    no_ownership_memory_reward: float
    no_repair_debt_reward: float
    no_continuity_reward: float
    short_term_selfish_reward: float
    omniscient_contract_control_reward: float
    social_gain_over_short_term_selfish: float
    no_commitment_memory_loss: float
    no_identity_memory_loss: float
    no_communication_action_loss: float
    no_trust_update_loss: float
    no_ownership_memory_loss: float
    no_repair_debt_loss: float
    no_continuity_loss: float
    short_term_selfish_loss: float
    selected_commitments_kept: float
    selected_commitments_broken: float
    selected_communication_actions: float
    selected_future_access: float
    supports_social_trust_contracts_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        index=0,
        name="visible_no_contract_control",
        pressure="visible resources and no repeated social obligation where contracts should not matter",
        contract_type="none",
        expected_commitment_pressure=False,
        expected_identity_pressure=False,
        expected_communication_pressure=False,
        expected_trust_pressure=False,
        expected_ownership_pressure=False,
        expected_repair_debt_pressure=False,
        expected_continuity_pressure=False,
        contract_value=0.0,
        immediate_cost=0.0,
        break_penalty=0.0,
        reciprocity_value=0.0,
        hazard_pressure=0.0,
        resource_pressure=0.0,
        shelter_pressure=0.0,
        required_progress=110.0,
        work_rate=0.72,
        offer_tick=-1,
        due_tick=-1,
        payoff_tick=-1,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=1,
        name="borrowed_tool_return_contract",
        pressure="a borrowed tool improves work now, but returning it preserves later access and trust",
        contract_type="tool_return",
        expected_commitment_pressure=True,
        expected_identity_pressure=True,
        expected_communication_pressure=True,
        expected_trust_pressure=True,
        expected_ownership_pressure=True,
        expected_repair_debt_pressure=False,
        expected_continuity_pressure=False,
        contract_value=0.64,
        immediate_cost=0.18,
        break_penalty=0.72,
        reciprocity_value=0.58,
        hazard_pressure=0.0,
        resource_pressure=0.18,
        shelter_pressure=0.0,
        required_progress=108.0,
        work_rate=0.62,
        offer_tick=18,
        due_tick=70,
        payoff_tick=124,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=2,
        name="hazard_warning_promise",
        pressure="warning a helper costs time but preserves future repair and route support",
        contract_type="hazard_warning",
        expected_commitment_pressure=True,
        expected_identity_pressure=True,
        expected_communication_pressure=True,
        expected_trust_pressure=True,
        expected_ownership_pressure=False,
        expected_repair_debt_pressure=False,
        expected_continuity_pressure=False,
        contract_value=0.58,
        immediate_cost=0.16,
        break_penalty=0.78,
        reciprocity_value=0.62,
        hazard_pressure=0.76,
        resource_pressure=0.12,
        shelter_pressure=0.0,
        required_progress=104.0,
        work_rate=0.61,
        offer_tick=16,
        due_tick=64,
        payoff_tick=126,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=3,
        name="reciprocal_resource_sharing",
        pressure="sharing a scarce cache lowers immediate resources but buys future reciprocity",
        contract_type="resource_share",
        expected_commitment_pressure=True,
        expected_identity_pressure=True,
        expected_communication_pressure=True,
        expected_trust_pressure=True,
        expected_ownership_pressure=False,
        expected_repair_debt_pressure=False,
        expected_continuity_pressure=False,
        contract_value=0.60,
        immediate_cost=0.24,
        break_penalty=0.70,
        reciprocity_value=0.68,
        hazard_pressure=0.0,
        resource_pressure=0.70,
        shelter_pressure=0.0,
        required_progress=100.0,
        work_rate=0.60,
        offer_tick=20,
        due_tick=74,
        payoff_tick=132,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=4,
        name="shared_shelter_repair_contract",
        pressure="shared shelter survives storms only when repair duties and trust are tracked",
        contract_type="shelter_repair",
        expected_commitment_pressure=True,
        expected_identity_pressure=True,
        expected_communication_pressure=True,
        expected_trust_pressure=True,
        expected_ownership_pressure=False,
        expected_repair_debt_pressure=True,
        expected_continuity_pressure=False,
        contract_value=0.70,
        immediate_cost=0.28,
        break_penalty=0.82,
        reciprocity_value=0.60,
        hazard_pressure=0.18,
        resource_pressure=0.12,
        shelter_pressure=0.78,
        required_progress=98.0,
        work_rate=0.58,
        offer_tick=18,
        due_tick=76,
        payoff_tick=130,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=5,
        name="restore_contract_continuity",
        pressure="after restore, outstanding promises must survive or social access collapses",
        contract_type="restore_bundle",
        expected_commitment_pressure=True,
        expected_identity_pressure=True,
        expected_communication_pressure=True,
        expected_trust_pressure=True,
        expected_ownership_pressure=True,
        expected_repair_debt_pressure=True,
        expected_continuity_pressure=True,
        contract_value=0.72,
        immediate_cost=0.30,
        break_penalty=0.88,
        reciprocity_value=0.72,
        hazard_pressure=0.32,
        resource_pressure=0.46,
        shelter_pressure=0.52,
        required_progress=96.0,
        work_rate=0.56,
        offer_tick=14,
        due_tick=104,
        payoff_tick=146,
        restore_tick=82,
    ),
)


SEEDED_POLICIES = (
    Policy(
        name="no_contract_baseline",
        commitment_memory=False,
        identity_memory=False,
        communication_action=False,
        trust_update=False,
        ownership_memory=False,
        repair_debt_memory=False,
        continuity_memory=False,
        promise_bias=0.05,
        reciprocity_bias=0.05,
        risk_tolerance=0.78,
        selfish_bias=0.34,
    ),
    Policy(
        name="short_term_opportunist",
        commitment_memory=False,
        identity_memory=True,
        communication_action=True,
        trust_update=False,
        ownership_memory=False,
        repair_debt_memory=False,
        continuity_memory=False,
        promise_bias=0.12,
        reciprocity_bias=0.10,
        risk_tolerance=0.82,
        selfish_bias=0.88,
    ),
    Policy(
        name="tool_return_contract_keeper",
        commitment_memory=True,
        identity_memory=True,
        communication_action=True,
        trust_update=True,
        ownership_memory=True,
        repair_debt_memory=False,
        continuity_memory=False,
        promise_bias=0.82,
        reciprocity_bias=0.70,
        risk_tolerance=0.30,
        selfish_bias=0.10,
    ),
    Policy(
        name="hazard_warning_contract_keeper",
        commitment_memory=True,
        identity_memory=True,
        communication_action=True,
        trust_update=True,
        ownership_memory=False,
        repair_debt_memory=False,
        continuity_memory=False,
        promise_bias=0.80,
        reciprocity_bias=0.72,
        risk_tolerance=0.24,
        selfish_bias=0.08,
    ),
    Policy(
        name="resource_reciprocity_contract_keeper",
        commitment_memory=True,
        identity_memory=True,
        communication_action=True,
        trust_update=True,
        ownership_memory=False,
        repair_debt_memory=False,
        continuity_memory=False,
        promise_bias=0.86,
        reciprocity_bias=0.94,
        risk_tolerance=0.28,
        selfish_bias=0.12,
    ),
    Policy(
        name="shelter_repair_contract_keeper",
        commitment_memory=True,
        identity_memory=True,
        communication_action=True,
        trust_update=True,
        ownership_memory=False,
        repair_debt_memory=True,
        continuity_memory=False,
        promise_bias=0.80,
        reciprocity_bias=0.74,
        risk_tolerance=0.22,
        selfish_bias=0.08,
    ),
    Policy(
        name="continuity_contract_keeper",
        commitment_memory=True,
        identity_memory=True,
        communication_action=True,
        trust_update=True,
        ownership_memory=True,
        repair_debt_memory=True,
        continuity_memory=True,
        promise_bias=0.88,
        reciprocity_bias=0.86,
        risk_tolerance=0.18,
        selfish_bias=0.06,
    ),
)


CONDITIONS = (
    "full_control",
    "no_commitment_memory",
    "no_identity_memory",
    "no_communication_action",
    "no_trust_update",
    "no_ownership_memory",
    "no_repair_debt",
    "no_continuity",
    "short_term_selfish",
    "omniscient_contract_control",
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


def build_policies(cfg: ContractConfig) -> List[Policy]:
    policies = list(SEEDED_POLICIES)
    rng = random.Random(cfg.seed + 1103)
    while len(policies) < cfg.candidate_count:
        base = rng.choice(SEEDED_POLICIES[2:])
        policies.append(
            Policy(
                name=f"mutant_contract_{len(policies)}",
                commitment_memory=base.commitment_memory if rng.random() > 0.14 else not base.commitment_memory,
                identity_memory=base.identity_memory if rng.random() > 0.14 else not base.identity_memory,
                communication_action=base.communication_action if rng.random() > 0.14 else not base.communication_action,
                trust_update=base.trust_update if rng.random() > 0.16 else not base.trust_update,
                ownership_memory=base.ownership_memory if rng.random() > 0.18 else not base.ownership_memory,
                repair_debt_memory=base.repair_debt_memory if rng.random() > 0.18 else not base.repair_debt_memory,
                continuity_memory=base.continuity_memory if rng.random() > 0.18 else not base.continuity_memory,
                promise_bias=clamp(base.promise_bias + rng.uniform(-0.08, 0.08), 0.05, 0.96),
                reciprocity_bias=clamp(base.reciprocity_bias + rng.uniform(-0.10, 0.10), 0.05, 0.96),
                risk_tolerance=clamp(base.risk_tolerance + rng.uniform(-0.08, 0.08), 0.08, 0.88),
                selfish_bias=clamp(base.selfish_bias + rng.uniform(-0.08, 0.08), 0.02, 0.92),
            )
        )
    return policies


def condition_policy(policy: Policy, condition: str) -> Policy:
    if condition == "omniscient_contract_control":
        return Policy(
            name=policy.name,
            commitment_memory=True,
            identity_memory=True,
            communication_action=True,
            trust_update=True,
            ownership_memory=True,
            repair_debt_memory=True,
            continuity_memory=True,
            promise_bias=max(policy.promise_bias, 0.92),
            reciprocity_bias=max(policy.reciprocity_bias, 0.92),
            risk_tolerance=0.08,
            selfish_bias=0.02,
        )
    if condition == "short_term_selfish":
        return Policy(
            name=policy.name,
            commitment_memory=False,
            identity_memory=policy.identity_memory,
            communication_action=policy.communication_action,
            trust_update=False,
            ownership_memory=False,
            repair_debt_memory=False,
            continuity_memory=False,
            promise_bias=0.10,
            reciprocity_bias=0.08,
            risk_tolerance=0.88,
            selfish_bias=0.94,
        )
    return Policy(
        name=policy.name,
        commitment_memory=policy.commitment_memory and condition != "no_commitment_memory",
        identity_memory=policy.identity_memory and condition != "no_identity_memory",
        communication_action=policy.communication_action and condition != "no_communication_action",
        trust_update=policy.trust_update and condition != "no_trust_update",
        ownership_memory=policy.ownership_memory and condition != "no_ownership_memory",
        repair_debt_memory=policy.repair_debt_memory and condition != "no_repair_debt",
        continuity_memory=policy.continuity_memory and condition != "no_continuity",
        promise_bias=policy.promise_bias,
        reciprocity_bias=policy.reciprocity_bias,
        risk_tolerance=policy.risk_tolerance,
        selfish_bias=policy.selfish_bias,
    )


def scenario_seed(
    cfg: ContractConfig,
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
        (policy.commitment_memory, 0.58),
        (policy.identity_memory, 0.46),
        (policy.communication_action, 0.48),
        (policy.trust_update, 0.50),
        (policy.ownership_memory, 0.44),
        (policy.repair_debt_memory, 0.44),
        (policy.continuity_memory, 0.78),
    ]
    return sum(weight for enabled, weight in weighted_flags if enabled)


def can_take_contract(policy: Policy, scenario: ScenarioSpec) -> bool:
    if scenario.contract_type == "none":
        return False
    return policy.commitment_memory and policy.identity_memory and policy.communication_action


def should_keep_contract(policy: Policy, scenario: ScenarioSpec, trust: float, reputation: float) -> bool:
    if not policy.commitment_memory:
        return False
    if not policy.identity_memory:
        return False
    if not policy.communication_action:
        return False
    if scenario.expected_ownership_pressure and not policy.ownership_memory:
        return False
    if scenario.expected_repair_debt_pressure and not policy.repair_debt_memory:
        return False
    if scenario.contract_type == "resource_share" and policy.reciprocity_bias < 0.88:
        return False
    if scenario.expected_trust_pressure and not policy.trust_update:
        return False
    expected_future = (trust + reputation) * 0.50 + policy.reciprocity_bias * scenario.reciprocity_value
    cost_pressure = scenario.immediate_cost + policy.selfish_bias * 0.55
    return policy.promise_bias + expected_future > cost_pressure + policy.risk_tolerance * 0.18


def contract_action(scenario: ScenarioSpec) -> str:
    return {
        "tool_return": "return_tool",
        "hazard_warning": "warn_helper",
        "resource_share": "share_resource",
        "shelter_repair": "repair_shelter",
        "restore_bundle": "restore_obligation_bundle",
    }.get(scenario.contract_type, "none")


def add_frame(
    trace: List[Dict[str, object]],
    tick: int,
    action: str,
    progress: float,
    energy: float,
    resources: float,
    trust: float,
    reputation: float,
    future_access: float,
    shelter_quality: float,
    social_penalty: float,
    kept: int,
    broken: int,
    communication: int,
    notes: List[str],
) -> None:
    trace.append(
        {
            "tick": tick,
            "action": action,
            "progress": round(progress, 3),
            "energy": round(energy, 3),
            "resources": round(resources, 3),
            "trust": round(trust, 3),
            "reputation": round(reputation, 3),
            "future_access": round(future_access, 3),
            "shelter_quality": round(shelter_quality, 3),
            "social_penalty": round(social_penalty, 3),
            "commitments_kept": kept,
            "commitments_broken": broken,
            "communication_actions": communication,
            "notes": list(notes[-3:]),
        }
    )


def simulate_episode(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episode: int,
    cfg: ContractConfig,
    phase: str,
    collect_trace: bool = False,
) -> Tuple[EpisodeResult, List[Dict[str, object]]]:
    effective = condition_policy(policy, condition)
    rng = random.Random(scenario_seed(cfg, scenario, policy, condition, episode, phase))

    progress = 0.0
    energy = clamp(0.96 + rng.uniform(-0.020, 0.020), 0.0, 1.0)
    resources = clamp(0.66 - scenario.resource_pressure * 0.16 + rng.uniform(-0.020, 0.020), 0.0, 1.0)
    trust = clamp(0.56 + rng.uniform(-0.018, 0.018), 0.0, 1.0)
    reputation = clamp(0.54 + rng.uniform(-0.018, 0.018), 0.0, 1.0)
    future_access = 0.18 if scenario.contract_type != "none" else 0.04
    shelter_quality = clamp(0.76 - scenario.shelter_pressure * 0.22 + rng.uniform(-0.020, 0.020), 0.0, 1.0)
    social_penalty = 0.0
    tool_bonus = 0.0
    contract_active = False
    contract_fulfilled = False
    contract_lost_by_restore = False
    collapsed = False

    commitments_kept = 0
    commitments_broken = 0
    communication_actions = 0
    tool_return_actions = 0
    warning_actions = 0
    share_actions = 0
    repair_contributions = 0
    reciprocity_received = 0
    continuity_resets = 0
    contract_misses = 0
    wrong_agent_events = 0
    trace_frames: List[Dict[str, object]] = []
    notes: List[str] = []
    last_action = "work"

    for tick in range(cfg.ticks):
        last_action = "work"

        if scenario.restore_tick == tick and not effective.continuity_memory:
            if contract_active and not contract_fulfilled:
                contract_active = False
                contract_lost_by_restore = True
                contract_misses += 1
                notes.append("restore erased outstanding obligation")
            trust = clamp(0.48 + rng.uniform(-0.015, 0.015), 0.0, 1.0)
            reputation = clamp(0.48 + rng.uniform(-0.015, 0.015), 0.0, 1.0)
            future_access = clamp(future_access - 0.22, 0.0, 1.0)
            continuity_resets += 1
            last_action = "restore_reset"

        if scenario.offer_tick == tick and scenario.contract_type != "none":
            if can_take_contract(effective, scenario):
                contract_active = True
                communication_actions += 1
                energy = clamp(energy - 0.018, 0.0, 1.0)
                trust = clamp(trust + 0.035, 0.0, 1.0)
                reputation = clamp(reputation + 0.025, 0.0, 1.0)
                if scenario.contract_type == "tool_return":
                    tool_bonus = 0.34
                notes.append("contract accepted")
                last_action = "accept_contract"
            else:
                contract_misses += 1
                future_access = clamp(future_access - 0.10, 0.0, 1.0)
                notes.append("contract opportunity missed")
                last_action = "miss_contract"

        if scenario.due_tick == tick and scenario.contract_type != "none":
            keep = contract_active and should_keep_contract(effective, scenario, trust, reputation)
            if keep:
                action = contract_action(scenario)
                commitments_kept += 1
                communication_actions += 1
                contract_fulfilled = True
                energy = clamp(energy - scenario.immediate_cost * 0.18, 0.0, 1.0)
                progress -= scenario.immediate_cost * 4.5
                trust = clamp(trust + 0.18 + scenario.contract_value * 0.12, 0.0, 1.0)
                reputation = clamp(reputation + 0.16 + scenario.contract_value * 0.13, 0.0, 1.0)
                future_access = clamp(future_access + 0.30 + scenario.reciprocity_value * 0.28, 0.0, 1.0)
                notes.append("promise kept")
                last_action = action
                if scenario.contract_type == "tool_return":
                    tool_return_actions += 1
                    tool_bonus = clamp(tool_bonus - 0.18, 0.0, 1.0)
                elif scenario.contract_type == "hazard_warning":
                    warning_actions += 1
                    social_penalty = clamp(social_penalty - 0.12, 0.0, 1.0)
                elif scenario.contract_type == "resource_share":
                    share_actions += 1
                    resources = clamp(resources - scenario.immediate_cost * 0.62, 0.0, 1.0)
                elif scenario.contract_type == "shelter_repair":
                    repair_contributions += 1
                    shelter_quality = clamp(shelter_quality + 0.26, 0.0, 1.0)
                elif scenario.contract_type == "restore_bundle":
                    tool_return_actions += 1
                    share_actions += 1
                    repair_contributions += 1
                    shelter_quality = clamp(shelter_quality + 0.18, 0.0, 1.0)
                    resources = clamp(resources - scenario.immediate_cost * 0.42, 0.0, 1.0)
            else:
                commitments_broken += 1
                contract_misses += 1
                if not effective.identity_memory:
                    wrong_agent_events += 1
                if not effective.communication_action:
                    communication_actions += 0
                trust = clamp(trust - 0.24 - scenario.break_penalty * 0.20, 0.0, 1.0)
                reputation = clamp(reputation - 0.28 - scenario.break_penalty * 0.24, 0.0, 1.0)
                future_access = clamp(future_access - 0.30 - scenario.break_penalty * 0.20, 0.0, 1.0)
                social_penalty = clamp(social_penalty + scenario.break_penalty, 0.0, 1.5)
                if scenario.contract_type == "hazard_warning":
                    social_penalty = clamp(social_penalty + scenario.hazard_pressure * 0.28, 0.0, 1.5)
                if scenario.contract_type in {"shelter_repair", "restore_bundle"}:
                    shelter_quality = clamp(shelter_quality - scenario.shelter_pressure * 0.26, 0.0, 1.0)
                notes.append("promise broken")
                last_action = "break_contract"

        if scenario.payoff_tick == tick and scenario.contract_type != "none":
            if contract_fulfilled:
                reciprocity_received += 1
                support = scenario.reciprocity_value * (0.62 + trust * 0.32)
                resources = clamp(resources + support * 0.34, 0.0, 1.0)
                progress += support * 16.0
                future_access = clamp(future_access + support * 0.18, 0.0, 1.0)
                notes.append("future reciprocity received")
                last_action = "receive_reciprocity"
            elif contract_lost_by_restore:
                social_penalty = clamp(social_penalty + 0.45, 0.0, 1.5)
                notes.append("restore break punished")
                last_action = "restore_punishment"
            else:
                social_penalty = clamp(social_penalty + 0.24, 0.0, 1.5)
                notes.append("future support denied")
                last_action = "support_denied"

        if not collapsed:
            hazard_loss = scenario.hazard_pressure * max(0.0, 0.62 - future_access) * 0.007
            resource_loss = scenario.resource_pressure * max(0.0, 0.58 - resources) * 0.010
            shelter_loss = scenario.shelter_pressure * max(0.0, 0.62 - shelter_quality) * 0.009
            social_drag = social_penalty * 0.004
            energy = clamp(energy - 0.0014 - hazard_loss * 0.20 - shelter_loss * 0.16, 0.0, 1.0)
            resources = clamp(resources - 0.0012 - resource_loss, 0.0, 1.0)
            shelter_quality = clamp(shelter_quality - scenario.shelter_pressure * 0.0009, 0.0, 1.0)
            capability = clamp(
                0.76
                + tool_bonus * 0.20
                + future_access * 0.18
                + trust * 0.08
                + reputation * 0.08
                + shelter_quality * 0.10
                + resources * 0.08
                - hazard_loss * 18.0
                - shelter_loss * 14.0
                - social_drag * 14.0,
                0.04,
                1.18,
            )
            progress += scenario.work_rate * capability
            if energy <= 0.05 or resources <= 0.04 or social_penalty >= 1.35:
                collapsed = True

        if collect_trace and (tick % 5 == 0 or tick == cfg.ticks - 1 or last_action != "work"):
            add_frame(
                trace_frames,
                tick,
                last_action,
                progress,
                energy,
                resources,
                trust,
                reputation,
                future_access,
                shelter_quality,
                social_penalty,
                commitments_kept,
                commitments_broken,
                communication_actions,
                notes,
            )

    task_success = progress >= scenario.required_progress and not collapsed
    survival = 1.0 if not collapsed and energy > 0.08 and resources > 0.05 and social_penalty < 1.30 else 0.0

    reward = progress
    reward += 34.0 if task_success else -20.0
    reward += 34.0 if survival else -92.0
    reward += trust * (22.0 if scenario.expected_trust_pressure else 3.0)
    reward += reputation * (22.0 if scenario.expected_trust_pressure else 3.0)
    reward += future_access * (34.0 if scenario.contract_type != "none" else 2.0)
    reward += shelter_quality * (22.0 if scenario.expected_repair_debt_pressure else 3.0)
    reward += resources * (14.0 if scenario.resource_pressure > 0.4 else 4.0)
    reward += commitments_kept * (30.0 + scenario.contract_value * 12.0)
    reward += reciprocity_received * (22.0 + scenario.reciprocity_value * 10.0)
    reward -= commitments_broken * (46.0 + scenario.break_penalty * 18.0)
    reward -= social_penalty * 82.0
    reward -= contract_misses * 4.6
    reward -= wrong_agent_events * 18.0
    reward -= communication_actions * 0.45
    reward -= feature_overhead(effective)
    if scenario.expected_continuity_pressure and continuity_resets:
        reward -= 38.0

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
        resources=resources,
        trust=trust,
        reputation=reputation,
        future_access=future_access,
        shelter_quality=shelter_quality,
        social_penalty=social_penalty,
        commitments_kept=commitments_kept,
        commitments_broken=commitments_broken,
        communication_actions=communication_actions,
        tool_return_actions=tool_return_actions,
        warning_actions=warning_actions,
        share_actions=share_actions,
        repair_contributions=repair_contributions,
        reciprocity_received=reciprocity_received,
        continuity_resets=continuity_resets,
        contract_misses=contract_misses,
        wrong_agent_events=wrong_agent_events,
    )
    return result, trace_frames


def evaluate_policy(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episodes: int,
    cfg: ContractConfig,
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
                    mean_resources=mean(row.resources for row in subset),
                    mean_trust=mean(row.trust for row in subset),
                    mean_reputation=mean(row.reputation for row in subset),
                    mean_future_access=mean(row.future_access for row in subset),
                    mean_shelter_quality=mean(row.shelter_quality for row in subset),
                    mean_social_penalty=mean(row.social_penalty for row in subset),
                    mean_commitments_kept=mean(row.commitments_kept for row in subset),
                    mean_commitments_broken=mean(row.commitments_broken for row in subset),
                    mean_communication_actions=mean(row.communication_actions for row in subset),
                    mean_tool_return_actions=mean(row.tool_return_actions for row in subset),
                    mean_warning_actions=mean(row.warning_actions for row in subset),
                    mean_share_actions=mean(row.share_actions for row in subset),
                    mean_repair_contributions=mean(row.repair_contributions for row in subset),
                    mean_reciprocity_received=mean(row.reciprocity_received for row in subset),
                    mean_continuity_resets=mean(row.continuity_resets for row in subset),
                    mean_contract_misses=mean(row.contract_misses for row in subset),
                    mean_wrong_agent_events=mean(row.wrong_agent_events for row in subset),
                )
            )
    return rows


def select_policies(cfg: ContractConfig, policies: Sequence[Policy]) -> Tuple[Dict[int, Policy], List[PolicySelectionRow]]:
    selected: Dict[int, Policy] = {}
    rows: List[PolicySelectionRow] = []
    baseline = next(policy for policy in policies if policy.name == "no_contract_baseline")
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
                selected_uses_commitment_memory=selected_policy.commitment_memory,
                selected_uses_identity_memory=selected_policy.identity_memory,
                selected_uses_communication_action=selected_policy.communication_action,
                selected_uses_trust_update=selected_policy.trust_update,
                selected_uses_ownership_memory=selected_policy.ownership_memory,
                selected_uses_repair_debt_memory=selected_policy.repair_debt_memory,
                selected_uses_continuity=selected_policy.continuity_memory,
                train_reward=selected_reward,
                no_contract_train_reward=baseline_reward,
                train_gain_over_no_contract=selected_reward - baseline_reward,
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
        no_commitment = lookup[(scenario.index, "no_commitment_memory")]
        no_identity = lookup[(scenario.index, "no_identity_memory")]
        no_comm = lookup[(scenario.index, "no_communication_action")]
        no_trust = lookup[(scenario.index, "no_trust_update")]
        no_ownership = lookup[(scenario.index, "no_ownership_memory")]
        no_repair = lookup[(scenario.index, "no_repair_debt")]
        no_continuity = lookup[(scenario.index, "no_continuity")]
        selfish = lookup[(scenario.index, "short_term_selfish")]
        omniscient = lookup[(scenario.index, "omniscient_contract_control")]

        no_commitment_loss = full.mean_reward - no_commitment.mean_reward
        no_identity_loss = full.mean_reward - no_identity.mean_reward
        no_comm_loss = full.mean_reward - no_comm.mean_reward
        no_trust_loss = full.mean_reward - no_trust.mean_reward
        no_ownership_loss = full.mean_reward - no_ownership.mean_reward
        no_repair_loss = full.mean_reward - no_repair.mean_reward
        no_continuity_loss = full.mean_reward - no_continuity.mean_reward
        selfish_loss = full.mean_reward - selfish.mean_reward

        if scenario.index == 0:
            supports = (
                selected[scenario.index].name == "no_contract_baseline"
                and abs(no_commitment_loss) < 4.0
                and abs(no_comm_loss) < 4.0
                and full.mean_communication_actions < 0.5
                and full.mean_commitments_kept < 0.5
            )
            verdict = "contracts_rejected_in_visible_control"
        elif scenario.index == 1:
            supports = (
                no_commitment_loss > 24.0
                and no_ownership_loss > 24.0
                and no_trust_loss > 18.0
                and full.mean_tool_return_actions > 0.8
                and full.mean_commitments_broken < no_ownership.mean_commitments_broken
            )
            verdict = "tool_return_contract_preserves_access"
        elif scenario.index == 2:
            supports = (
                no_comm_loss > 24.0
                and no_identity_loss > 20.0
                and no_trust_loss > 18.0
                and full.mean_warning_actions > 0.8
                and full.mean_social_penalty < no_comm.mean_social_penalty
            )
            verdict = "hazard_warning_promise_preserves_help"
        elif scenario.index == 3:
            supports = (
                no_commitment_loss > 22.0
                and no_identity_loss > 20.0
                and no_trust_loss > 18.0
                and full.mean_share_actions > 0.8
                and full.mean_reciprocity_received > no_commitment.mean_reciprocity_received
            )
            verdict = "resource_sharing_contract_buys_reciprocity"
        elif scenario.index == 4:
            supports = (
                no_repair_loss > 24.0
                and no_commitment_loss > 22.0
                and no_identity_loss > 18.0
                and full.mean_repair_contributions > 0.8
                and full.mean_shelter_quality > no_repair.mean_shelter_quality
            )
            verdict = "shelter_repair_contract_preserves_shared_infrastructure"
        else:
            supports = (
                no_continuity_loss > 24.0
                and no_commitment_loss > 22.0
                and no_ownership_loss > 18.0
                and no_repair_loss > 18.0
                and no_continuity.mean_continuity_resets > 0.5
                and full.mean_commitments_broken < no_continuity.mean_commitments_broken
            )
            verdict = "restore_contract_continuity_preserves_social_access"

        baseline_condition = lookup[(scenario.index, "short_term_selfish")]
        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                expected_pressure=scenario.pressure,
                selected_policy=selected[scenario.index].name,
                selected_reward=full.mean_reward,
                no_commitment_memory_reward=no_commitment.mean_reward,
                no_identity_memory_reward=no_identity.mean_reward,
                no_communication_action_reward=no_comm.mean_reward,
                no_trust_update_reward=no_trust.mean_reward,
                no_ownership_memory_reward=no_ownership.mean_reward,
                no_repair_debt_reward=no_repair.mean_reward,
                no_continuity_reward=no_continuity.mean_reward,
                short_term_selfish_reward=selfish.mean_reward,
                omniscient_contract_control_reward=omniscient.mean_reward,
                social_gain_over_short_term_selfish=full.mean_reward - baseline_condition.mean_reward,
                no_commitment_memory_loss=no_commitment_loss,
                no_identity_memory_loss=no_identity_loss,
                no_communication_action_loss=no_comm_loss,
                no_trust_update_loss=no_trust_loss,
                no_ownership_memory_loss=no_ownership_loss,
                no_repair_debt_loss=no_repair_loss,
                no_continuity_loss=no_continuity_loss,
                short_term_selfish_loss=selfish_loss,
                selected_commitments_kept=full.mean_commitments_kept,
                selected_commitments_broken=full.mean_commitments_broken,
                selected_communication_actions=full.mean_communication_actions,
                selected_future_access=full.mean_future_access,
                supports_social_trust_contracts_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def build_trace(cfg: ContractConfig, selected: Dict[int, Policy]) -> Dict[str, object]:
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
            "mean_trust": mean(row.trust for row in rows),
            "mean_reputation": mean(row.reputation for row in rows),
            "mean_future_access": mean(row.future_access for row in rows),
            "mean_social_penalty": mean(row.social_penalty for row in rows),
        }
    return {
        "scenario": asdict(scenario),
        "policy": asdict(policy),
        "episode_result": asdict(result),
        "condition_outcomes": condition_outcomes,
        "frames": frames,
        "trace_note": "Contracts, trust, ownership, repair debt, communication, and continuity are abstract control variables.",
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
    cfg: ContractConfig,
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
        "artifact_note": "Social trust and contracts are control variables, not society simulation.",
    }
    return eval_rows, selection_rows, summary_rows, verdict_rows, {"results": results, "trace": trace}


def print_table(verdicts: Sequence[VerdictRow]) -> None:
    headers = [
        "scenario",
        "policy",
        "commitment_loss",
        "identity_loss",
        "comm_loss",
        "trust_loss",
        "ownership_loss",
        "repair_debt_loss",
        "continuity_loss",
        "supports",
    ]
    rows = [
        [
            row.scenario_name,
            row.selected_policy,
            f"{row.no_commitment_memory_loss:.3f}",
            f"{row.no_identity_memory_loss:.3f}",
            f"{row.no_communication_action_loss:.3f}",
            f"{row.no_trust_update_loss:.3f}",
            f"{row.no_ownership_memory_loss:.3f}",
            f"{row.no_repair_debt_loss:.3f}",
            f"{row.no_continuity_loss:.3f}",
            str(row.supports_social_trust_contracts_precursor),
        ]
        for row in verdicts
    ]
    widths = [max(len(header), *(len(row[index]) for row in rows)) for index, header in enumerate(headers)]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> ContractConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-episodes", type=int, default=ContractConfig.train_episodes)
    parser.add_argument("--eval-episodes", type=int, default=ContractConfig.eval_episodes)
    parser.add_argument("--ticks", type=int, default=ContractConfig.ticks)
    parser.add_argument("--seed", type=int, default=ContractConfig.seed)
    parser.add_argument("--candidate-count", type=int, default=ContractConfig.candidate_count)
    parser.add_argument("--trace-scenario", type=int, default=ContractConfig.trace_scenario)
    parser.add_argument("--trace-episode", type=int, default=ContractConfig.trace_episode)
    args = parser.parse_args()
    if args.train_episodes < 24:
        raise SystemExit("--train-episodes must be at least 24")
    if args.eval_episodes < 24:
        raise SystemExit("--eval-episodes must be at least 24")
    if args.candidate_count < len(SEEDED_POLICIES):
        raise SystemExit(f"--candidate-count must be at least {len(SEEDED_POLICIES)}")
    if args.trace_scenario < 0 or args.trace_scenario >= len(SCENARIOS):
        raise SystemExit("--trace-scenario out of range")
    return ContractConfig(
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

    eval_path = ARTIFACT_DIR / "ssrm_3d_social_trust_contracts_eval.csv"
    selection_path = ARTIFACT_DIR / "ssrm_3d_social_trust_contracts_policy_selection.csv"
    summary_path = ARTIFACT_DIR / "ssrm_3d_social_trust_contracts_summary.csv"
    verdict_path = ARTIFACT_DIR / "ssrm_3d_social_trust_contracts_verdict.csv"
    results_path = ARTIFACT_DIR / "ssrm_3d_social_trust_contracts_results.json"
    trace_path = ARTIFACT_DIR / "ssrm_3d_social_trust_contracts_trace.json"
    results_js_path = ARTIFACT_DIR / "ssrm_3d_social_trust_contracts_results.js"
    trace_js_path = ARTIFACT_DIR / "ssrm_3d_social_trust_contracts_trace.js"

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
    write_js(results_js_path, "SSRM_3D_SOCIAL_TRUST_CONTRACTS_RESULTS", payload["results"])
    write_js(trace_js_path, "SSRM_3D_SOCIAL_TRUST_CONTRACTS_TRACE", payload["trace"])

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
    if not all(row.supports_social_trust_contracts_precursor for row in verdict_rows):
        print("social trust/contracts precursor not supported by all verdict rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
