#!/usr/bin/env python3
"""SSRM-3D affective-control precursor.

This experiment implements the thirteenth pressure-layer step from report 74:
affective control state. It is intentionally not a feeling, emotion, or
consciousness simulation.

Emotion-like variables are treated as compact control summaries. The narrow
test is whether affective state should be rejected in a calm control regime,
then become useful only when it changes attention, risk tolerance, social
approach, communication, memory salience, repair behavior, information seeking,
or restore continuity.
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
class AffectConfig:
    train_episodes: int = 72
    eval_episodes: int = 96
    ticks: int = 210
    seed: int = 20260702
    candidate_count: int = 8
    trace_scenario: int = 4
    trace_episode: int = 0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    expected_fear: bool
    expected_stress: bool
    expected_trust: bool
    expected_frustration: bool
    expected_affiliation: bool
    expected_curiosity: bool
    expected_guilt: bool
    expected_attention: bool
    expected_memory: bool
    expected_risk: bool
    expected_communication: bool
    expected_continuity: bool
    hazard_pressure: float
    need_conflict: float
    social_pressure: float
    uncertainty_pressure: float
    failure_pressure: float
    commitment_pressure: float
    required_progress: float
    work_rate: float
    restore_tick: int


@dataclass(frozen=True)
class Policy:
    name: str
    fear_control: bool
    stress_control: bool
    trust_control: bool
    frustration_control: bool
    affiliation_control: bool
    curiosity_control: bool
    guilt_control: bool
    attention_mixing: bool
    memory_salience: bool
    risk_modulation: bool
    communication_bias: bool
    affective_continuity: bool
    risk_threshold: float
    attention_bias: float
    social_bias: float
    inspect_bias: float
    repair_bias: float


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
    fear_state: float
    stress_state: float
    trust_state: float
    frustration_state: float
    affiliation_state: float
    curiosity_state: float
    guilt_state: float
    attention_focus: float
    memory_salience: float
    risk_tolerance: float
    uncertainty: float
    social_access: float
    commitment_standing: float
    hazard_events: int
    conflict_events: int
    social_events: int
    failed_action_events: int
    commitment_breaches: int
    attention_actions: int
    avoidance_actions: int
    regulation_actions: int
    communication_actions: int
    affiliation_actions: int
    inspection_actions: int
    repair_actions: int
    strategy_switches: int
    continuity_resets: int
    affect_misses: int


@dataclass(frozen=True)
class PolicySelectionRow:
    scenario: int
    scenario_name: str
    selected_policy: str
    selected_uses_fear: bool
    selected_uses_stress: bool
    selected_uses_trust: bool
    selected_uses_frustration: bool
    selected_uses_affiliation: bool
    selected_uses_curiosity: bool
    selected_uses_guilt: bool
    selected_uses_attention: bool
    selected_uses_memory: bool
    selected_uses_risk: bool
    selected_uses_communication: bool
    selected_uses_continuity: bool
    train_reward: float
    reactive_train_reward: float
    train_gain_over_reactive: float


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
    mean_fear_state: float
    mean_stress_state: float
    mean_trust_state: float
    mean_frustration_state: float
    mean_affiliation_state: float
    mean_curiosity_state: float
    mean_guilt_state: float
    mean_attention_focus: float
    mean_memory_salience: float
    mean_risk_tolerance: float
    mean_uncertainty: float
    mean_social_access: float
    mean_commitment_standing: float
    mean_hazard_events: float
    mean_conflict_events: float
    mean_social_events: float
    mean_failed_action_events: float
    mean_commitment_breaches: float
    mean_attention_actions: float
    mean_avoidance_actions: float
    mean_regulation_actions: float
    mean_communication_actions: float
    mean_affiliation_actions: float
    mean_inspection_actions: float
    mean_repair_actions: float
    mean_strategy_switches: float
    mean_continuity_resets: float
    mean_affect_misses: float


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    expected_pressure: str
    selected_policy: str
    selected_reward: float
    no_fear_reward: float
    no_stress_reward: float
    no_trust_reward: float
    no_frustration_reward: float
    no_affiliation_reward: float
    no_curiosity_reward: float
    no_guilt_reward: float
    no_attention_reward: float
    no_memory_reward: float
    no_risk_reward: float
    no_communication_reward: float
    no_continuity_reward: float
    reactive_no_affect_reward: float
    omniscient_affect_control_reward: float
    no_fear_loss: float
    no_stress_loss: float
    no_trust_loss: float
    no_frustration_loss: float
    no_affiliation_loss: float
    no_curiosity_loss: float
    no_guilt_loss: float
    no_attention_loss: float
    no_memory_loss: float
    no_risk_loss: float
    no_communication_loss: float
    no_continuity_loss: float
    reactive_no_affect_loss: float
    selected_hazard_events: float
    selected_conflict_events: float
    selected_social_events: float
    selected_failed_action_events: float
    selected_commitment_breaches: float
    selected_attention_actions: float
    selected_communication_actions: float
    selected_inspection_actions: float
    selected_repair_actions: float
    supports_affective_control_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        index=0,
        name="calm_clear_control",
        pressure="low uncertainty, low hazard, stable social access; affective machinery should be rejected",
        expected_fear=False,
        expected_stress=False,
        expected_trust=False,
        expected_frustration=False,
        expected_affiliation=False,
        expected_curiosity=False,
        expected_guilt=False,
        expected_attention=False,
        expected_memory=False,
        expected_risk=False,
        expected_communication=False,
        expected_continuity=False,
        hazard_pressure=0.02,
        need_conflict=0.02,
        social_pressure=0.02,
        uncertainty_pressure=0.02,
        failure_pressure=0.02,
        commitment_pressure=0.02,
        required_progress=130.0,
        work_rate=0.76,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=1,
        name="fear_hazard_attention",
        pressure="hazard proximity, injury risk, and low visibility require fear-like risk and attention control",
        expected_fear=True,
        expected_stress=False,
        expected_trust=False,
        expected_frustration=False,
        expected_affiliation=False,
        expected_curiosity=False,
        expected_guilt=False,
        expected_attention=True,
        expected_memory=True,
        expected_risk=True,
        expected_communication=False,
        expected_continuity=False,
        hazard_pressure=0.92,
        need_conflict=0.16,
        social_pressure=0.06,
        uncertainty_pressure=0.34,
        failure_pressure=0.18,
        commitment_pressure=0.06,
        required_progress=82.0,
        work_rate=0.48,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=2,
        name="stress_need_arbitration",
        pressure="low energy, sleep debt, commitments, and incompatible needs require stress-like arbitration",
        expected_fear=False,
        expected_stress=True,
        expected_trust=False,
        expected_frustration=False,
        expected_affiliation=False,
        expected_curiosity=False,
        expected_guilt=False,
        expected_attention=True,
        expected_memory=True,
        expected_risk=True,
        expected_communication=False,
        expected_continuity=False,
        hazard_pressure=0.18,
        need_conflict=0.90,
        social_pressure=0.18,
        uncertainty_pressure=0.26,
        failure_pressure=0.20,
        commitment_pressure=0.42,
        required_progress=78.0,
        work_rate=0.46,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=3,
        name="trust_affiliation_social",
        pressure="help, deception, repair, and repeated cooperation require trust and affiliation control",
        expected_fear=False,
        expected_stress=False,
        expected_trust=True,
        expected_frustration=False,
        expected_affiliation=True,
        expected_curiosity=False,
        expected_guilt=False,
        expected_attention=True,
        expected_memory=True,
        expected_risk=False,
        expected_communication=True,
        expected_continuity=False,
        hazard_pressure=0.10,
        need_conflict=0.24,
        social_pressure=0.90,
        uncertainty_pressure=0.28,
        failure_pressure=0.14,
        commitment_pressure=0.36,
        required_progress=78.0,
        work_rate=0.46,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=4,
        name="frustration_curiosity_switching",
        pressure="repeated failure and high but tolerable uncertainty require strategy switching and inspection",
        expected_fear=False,
        expected_stress=False,
        expected_trust=False,
        expected_frustration=True,
        expected_affiliation=False,
        expected_curiosity=True,
        expected_guilt=False,
        expected_attention=True,
        expected_memory=True,
        expected_risk=True,
        expected_communication=False,
        expected_continuity=False,
        hazard_pressure=0.20,
        need_conflict=0.20,
        social_pressure=0.12,
        uncertainty_pressure=0.90,
        failure_pressure=0.88,
        commitment_pressure=0.12,
        required_progress=76.0,
        work_rate=0.45,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=5,
        name="guilt_commitment_repair",
        pressure="failed promises and harmful actions reduce future social access unless repaired",
        expected_fear=False,
        expected_stress=True,
        expected_trust=True,
        expected_frustration=False,
        expected_affiliation=False,
        expected_curiosity=False,
        expected_guilt=True,
        expected_attention=True,
        expected_memory=True,
        expected_risk=False,
        expected_communication=True,
        expected_continuity=False,
        hazard_pressure=0.10,
        need_conflict=0.38,
        social_pressure=0.74,
        uncertainty_pressure=0.20,
        failure_pressure=0.22,
        commitment_pressure=0.92,
        required_progress=72.0,
        work_rate=0.43,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=6,
        name="restore_affective_continuity",
        pressure="after restore, fear, stress, trust, guilt, attention, and memory salience must remain coherent",
        expected_fear=True,
        expected_stress=True,
        expected_trust=True,
        expected_frustration=True,
        expected_affiliation=True,
        expected_curiosity=True,
        expected_guilt=True,
        expected_attention=True,
        expected_memory=True,
        expected_risk=True,
        expected_communication=True,
        expected_continuity=True,
        hazard_pressure=0.46,
        need_conflict=0.54,
        social_pressure=0.56,
        uncertainty_pressure=0.50,
        failure_pressure=0.50,
        commitment_pressure=0.58,
        required_progress=66.0,
        work_rate=0.40,
        restore_tick=96,
    ),
)


SEEDED_POLICIES = (
    Policy(
        name="reactive_no_affect",
        fear_control=False,
        stress_control=False,
        trust_control=False,
        frustration_control=False,
        affiliation_control=False,
        curiosity_control=False,
        guilt_control=False,
        attention_mixing=False,
        memory_salience=False,
        risk_modulation=False,
        communication_bias=False,
        affective_continuity=False,
        risk_threshold=0.90,
        attention_bias=0.04,
        social_bias=0.04,
        inspect_bias=0.04,
        repair_bias=0.04,
    ),
    Policy(
        name="fear_safety_planner",
        fear_control=True,
        stress_control=False,
        trust_control=False,
        frustration_control=False,
        affiliation_control=False,
        curiosity_control=False,
        guilt_control=False,
        attention_mixing=True,
        memory_salience=True,
        risk_modulation=True,
        communication_bias=False,
        affective_continuity=False,
        risk_threshold=0.34,
        attention_bias=0.84,
        social_bias=0.04,
        inspect_bias=0.16,
        repair_bias=0.04,
    ),
    Policy(
        name="stress_arbitrator",
        fear_control=False,
        stress_control=True,
        trust_control=False,
        frustration_control=False,
        affiliation_control=False,
        curiosity_control=False,
        guilt_control=False,
        attention_mixing=True,
        memory_salience=True,
        risk_modulation=True,
        communication_bias=False,
        affective_continuity=False,
        risk_threshold=0.38,
        attention_bias=0.78,
        social_bias=0.08,
        inspect_bias=0.08,
        repair_bias=0.20,
    ),
    Policy(
        name="trust_affiliation_planner",
        fear_control=False,
        stress_control=False,
        trust_control=True,
        frustration_control=False,
        affiliation_control=True,
        curiosity_control=False,
        guilt_control=False,
        attention_mixing=True,
        memory_salience=True,
        risk_modulation=False,
        communication_bias=True,
        affective_continuity=False,
        risk_threshold=0.56,
        attention_bias=0.54,
        social_bias=0.90,
        inspect_bias=0.06,
        repair_bias=0.28,
    ),
    Policy(
        name="frustration_curiosity_planner",
        fear_control=False,
        stress_control=False,
        trust_control=False,
        frustration_control=True,
        affiliation_control=False,
        curiosity_control=True,
        guilt_control=False,
        attention_mixing=True,
        memory_salience=True,
        risk_modulation=True,
        communication_bias=False,
        affective_continuity=False,
        risk_threshold=0.44,
        attention_bias=0.72,
        social_bias=0.05,
        inspect_bias=0.92,
        repair_bias=0.08,
    ),
    Policy(
        name="guilt_repair_planner",
        fear_control=False,
        stress_control=True,
        trust_control=True,
        frustration_control=False,
        affiliation_control=False,
        curiosity_control=False,
        guilt_control=True,
        attention_mixing=True,
        memory_salience=True,
        risk_modulation=False,
        communication_bias=True,
        affective_continuity=False,
        risk_threshold=0.54,
        attention_bias=0.62,
        social_bias=0.70,
        inspect_bias=0.06,
        repair_bias=0.92,
    ),
    Policy(
        name="integrated_affect_planner",
        fear_control=True,
        stress_control=True,
        trust_control=True,
        frustration_control=True,
        affiliation_control=True,
        curiosity_control=True,
        guilt_control=True,
        attention_mixing=True,
        memory_salience=True,
        risk_modulation=True,
        communication_bias=True,
        affective_continuity=False,
        risk_threshold=0.30,
        attention_bias=0.76,
        social_bias=0.74,
        inspect_bias=0.74,
        repair_bias=0.78,
    ),
    Policy(
        name="continuity_affect_planner",
        fear_control=True,
        stress_control=True,
        trust_control=True,
        frustration_control=True,
        affiliation_control=True,
        curiosity_control=True,
        guilt_control=True,
        attention_mixing=True,
        memory_salience=True,
        risk_modulation=True,
        communication_bias=True,
        affective_continuity=True,
        risk_threshold=0.28,
        attention_bias=0.80,
        social_bias=0.76,
        inspect_bias=0.76,
        repair_bias=0.82,
    ),
)


CONDITIONS = (
    "full_control",
    "no_fear_control",
    "no_stress_control",
    "no_trust_control",
    "no_frustration_control",
    "no_affiliation_control",
    "no_curiosity_control",
    "no_guilt_control",
    "no_attention_mixing",
    "no_memory_salience",
    "no_risk_modulation",
    "no_communication_bias",
    "no_affective_continuity",
    "reactive_no_affect",
    "omniscient_affect_control",
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


def build_policies(cfg: AffectConfig) -> List[Policy]:
    policies = list(SEEDED_POLICIES)
    rng = random.Random(cfg.seed + 4111)
    while len(policies) < cfg.candidate_count:
        base = rng.choice(SEEDED_POLICIES[2:])
        policies.append(
            Policy(
                name=f"mutant_affect_{len(policies)}",
                fear_control=base.fear_control if rng.random() > 0.14 else not base.fear_control,
                stress_control=base.stress_control if rng.random() > 0.14 else not base.stress_control,
                trust_control=base.trust_control if rng.random() > 0.14 else not base.trust_control,
                frustration_control=base.frustration_control if rng.random() > 0.14 else not base.frustration_control,
                affiliation_control=base.affiliation_control if rng.random() > 0.14 else not base.affiliation_control,
                curiosity_control=base.curiosity_control if rng.random() > 0.14 else not base.curiosity_control,
                guilt_control=base.guilt_control if rng.random() > 0.14 else not base.guilt_control,
                attention_mixing=base.attention_mixing if rng.random() > 0.12 else not base.attention_mixing,
                memory_salience=base.memory_salience if rng.random() > 0.12 else not base.memory_salience,
                risk_modulation=base.risk_modulation if rng.random() > 0.12 else not base.risk_modulation,
                communication_bias=base.communication_bias if rng.random() > 0.12 else not base.communication_bias,
                affective_continuity=base.affective_continuity if rng.random() > 0.16 else not base.affective_continuity,
                risk_threshold=clamp(base.risk_threshold + rng.uniform(-0.08, 0.08), 0.16, 0.92),
                attention_bias=clamp(base.attention_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
                social_bias=clamp(base.social_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
                inspect_bias=clamp(base.inspect_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
                repair_bias=clamp(base.repair_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
            )
        )
    return policies


def condition_policy(policy: Policy, condition: str) -> Policy:
    if condition == "omniscient_affect_control":
        return Policy(
            name=policy.name,
            fear_control=True,
            stress_control=True,
            trust_control=True,
            frustration_control=True,
            affiliation_control=True,
            curiosity_control=True,
            guilt_control=True,
            attention_mixing=True,
            memory_salience=True,
            risk_modulation=True,
            communication_bias=True,
            affective_continuity=True,
            risk_threshold=0.14,
            attention_bias=max(policy.attention_bias, 0.92),
            social_bias=max(policy.social_bias, 0.92),
            inspect_bias=max(policy.inspect_bias, 0.92),
            repair_bias=max(policy.repair_bias, 0.92),
        )
    if condition == "reactive_no_affect":
        return SEEDED_POLICIES[0]
    return Policy(
        name=policy.name,
        fear_control=policy.fear_control and condition != "no_fear_control",
        stress_control=policy.stress_control and condition != "no_stress_control",
        trust_control=policy.trust_control and condition != "no_trust_control",
        frustration_control=policy.frustration_control and condition != "no_frustration_control",
        affiliation_control=policy.affiliation_control and condition != "no_affiliation_control",
        curiosity_control=policy.curiosity_control and condition != "no_curiosity_control",
        guilt_control=policy.guilt_control and condition != "no_guilt_control",
        attention_mixing=policy.attention_mixing and condition != "no_attention_mixing",
        memory_salience=policy.memory_salience and condition != "no_memory_salience",
        risk_modulation=policy.risk_modulation and condition != "no_risk_modulation",
        communication_bias=policy.communication_bias and condition != "no_communication_bias",
        affective_continuity=policy.affective_continuity and condition != "no_affective_continuity",
        risk_threshold=policy.risk_threshold,
        attention_bias=policy.attention_bias,
        social_bias=policy.social_bias,
        inspect_bias=policy.inspect_bias,
        repair_bias=policy.repair_bias,
    )


def scenario_seed(
    cfg: AffectConfig,
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
        (policy.fear_control, 2.50),
        (policy.stress_control, 2.50),
        (policy.trust_control, 2.70),
        (policy.frustration_control, 2.60),
        (policy.affiliation_control, 2.50),
        (policy.curiosity_control, 2.60),
        (policy.guilt_control, 2.80),
        (policy.attention_mixing, 2.40),
        (policy.memory_salience, 2.40),
        (policy.risk_modulation, 2.40),
        (policy.communication_bias, 2.50),
        (policy.affective_continuity, 9.60),
    ]
    return sum(weight for enabled, weight in weighted_flags if enabled)


def estimate_control_load(
    scenario: ScenarioSpec,
    policy: Policy,
    fear_state: float,
    stress_state: float,
    trust_state: float,
    frustration_state: float,
    curiosity_state: float,
    guilt_state: float,
    uncertainty: float,
    social_access: float,
    commitment_standing: float,
) -> float:
    observed_fear = fear_state if policy.fear_control else 0.35
    observed_stress = stress_state if policy.stress_control else 0.35
    observed_trust = trust_state if policy.trust_control else 0.55
    observed_frustration = frustration_state if policy.frustration_control else 0.35
    observed_curiosity = curiosity_state if policy.curiosity_control else 0.35
    observed_guilt = guilt_state if policy.guilt_control else 0.35
    observed_social = social_access if policy.trust_control else 0.60
    observed_commitment = commitment_standing if policy.guilt_control else 0.70
    load = (
        scenario.hazard_pressure * observed_fear * 0.62
        + scenario.need_conflict * observed_stress * 0.62
        + scenario.social_pressure * (1.0 - observed_trust) * 0.60
        + scenario.failure_pressure * observed_frustration * 0.58
        + scenario.uncertainty_pressure * (uncertainty + observed_curiosity) * 0.34
        + scenario.commitment_pressure * (observed_guilt + 1.0 - observed_commitment) * 0.42
        + (1.0 - observed_social) * scenario.social_pressure * 0.38
    )
    mitigation = (
        (0.12 if policy.attention_mixing else 0.0)
        + (0.10 if policy.memory_salience else 0.0)
        + (0.11 if policy.risk_modulation else 0.0)
        + (0.10 if policy.communication_bias else 0.0)
    )
    return clamp(load - mitigation, 0.0, 1.9)


def choose_action(
    scenario: ScenarioSpec,
    policy: Policy,
    load: float,
    fear_state: float,
    stress_state: float,
    trust_state: float,
    frustration_state: float,
    affiliation_state: float,
    curiosity_state: float,
    guilt_state: float,
    uncertainty: float,
    social_access: float,
    commitment_standing: float,
    tick: int,
) -> str:
    if scenario.index == 0:
        return "work"
    if policy.fear_control and scenario.expected_fear and load > policy.risk_threshold and tick % 5 == 0:
        return "avoid_hazard"
    if policy.stress_control and scenario.expected_stress and stress_state > 0.48 and tick % 6 == 0:
        return "regulate_stress"
    if policy.trust_control and scenario.expected_trust and social_access < 0.74 and tick % 5 == 0:
        return "signal_trust"
    if policy.affiliation_control and scenario.expected_affiliation and affiliation_state < 0.70 and tick % 7 == 0:
        return "affiliative_checkin"
    if policy.frustration_control and scenario.expected_frustration and frustration_state > 0.48 and tick % 6 == 0:
        return "switch_strategy"
    if policy.curiosity_control and scenario.expected_curiosity and uncertainty > 0.52 and tick % 5 == 0:
        return "inspect_unknown"
    if policy.guilt_control and scenario.expected_guilt and (guilt_state > 0.44 or commitment_standing < 0.72) and tick % 5 == 0:
        return "repair_commitment"
    if policy.attention_mixing and scenario.expected_attention and load > policy.risk_threshold * 0.84 and tick % 9 == 0:
        return "rebalance_attention"
    return "work"


def add_trace(
    trace: List[Dict[str, object]],
    tick: int,
    action: str,
    progress: float,
    energy: float,
    integrity: float,
    fear_state: float,
    stress_state: float,
    trust_state: float,
    frustration_state: float,
    affiliation_state: float,
    curiosity_state: float,
    guilt_state: float,
    attention_focus: float,
    memory_salience: float,
    risk_tolerance: float,
    uncertainty: float,
    social_access: float,
    commitment_standing: float,
    notes: List[str],
) -> None:
    trace.append(
        {
            "tick": tick,
            "action": action,
            "progress": round(progress, 3),
            "energy": round(energy, 3),
            "integrity": round(integrity, 3),
            "fear_state": round(fear_state, 3),
            "stress_state": round(stress_state, 3),
            "trust_state": round(trust_state, 3),
            "frustration_state": round(frustration_state, 3),
            "affiliation_state": round(affiliation_state, 3),
            "curiosity_state": round(curiosity_state, 3),
            "guilt_state": round(guilt_state, 3),
            "attention_focus": round(attention_focus, 3),
            "memory_salience": round(memory_salience, 3),
            "risk_tolerance": round(risk_tolerance, 3),
            "uncertainty": round(uncertainty, 3),
            "social_access": round(social_access, 3),
            "commitment_standing": round(commitment_standing, 3),
            "notes": list(notes[-4:]),
        }
    )


def simulate_episode(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episode: int,
    cfg: AffectConfig,
    phase: str,
    collect_trace: bool = False,
) -> Tuple[EpisodeResult, List[Dict[str, object]]]:
    effective = condition_policy(policy, condition)
    rng = random.Random(scenario_seed(cfg, scenario, policy, condition, episode, phase))

    energy = clamp(0.96 - scenario.need_conflict * 0.04 + rng.uniform(-0.010, 0.010), 0.0, 1.0)
    integrity = clamp(0.98 - scenario.hazard_pressure * 0.04 + rng.uniform(-0.010, 0.010), 0.0, 1.0)
    fear_state = clamp(0.10 + scenario.hazard_pressure * 0.40, 0.0, 1.0)
    stress_state = clamp(0.12 + scenario.need_conflict * 0.40 + scenario.commitment_pressure * 0.10, 0.0, 1.0)
    trust_state = clamp(0.86 - scenario.social_pressure * 0.36, 0.0, 1.0)
    frustration_state = clamp(0.08 + scenario.failure_pressure * 0.42, 0.0, 1.0)
    affiliation_state = clamp(0.80 - scenario.social_pressure * 0.24, 0.0, 1.0)
    curiosity_state = clamp(0.14 + scenario.uncertainty_pressure * 0.42, 0.0, 1.0)
    guilt_state = clamp(0.06 + scenario.commitment_pressure * 0.42, 0.0, 1.0)
    attention_focus = 0.62
    memory_salience_value = 0.58
    risk_tolerance = 0.66
    uncertainty = clamp(0.12 + scenario.uncertainty_pressure * 0.50, 0.0, 1.0)
    social_access = clamp(0.90 - scenario.social_pressure * 0.22, 0.0, 1.0)
    commitment_standing = clamp(0.92 - scenario.commitment_pressure * 0.24, 0.0, 1.0)
    progress = 0.0
    collapsed = False
    notes: List[str] = []
    trace_frames: List[Dict[str, object]] = []

    hazard_events = 0
    conflict_events = 0
    social_events = 0
    failed_action_events = 0
    commitment_breaches = 0
    attention_actions = 0
    avoidance_actions = 0
    regulation_actions = 0
    communication_actions = 0
    affiliation_actions = 0
    inspection_actions = 0
    repair_actions = 0
    strategy_switches = 0
    continuity_resets = 0
    affect_misses = 0

    for tick in range(cfg.ticks):
        action = "work"
        if scenario.restore_tick == tick and not effective.affective_continuity:
            continuity_resets += 1
            affect_misses += 12
            fear_state = clamp(fear_state + 0.24, 0.0, 1.0)
            stress_state = clamp(stress_state + 0.28, 0.0, 1.0)
            trust_state = clamp(trust_state - 0.30, 0.0, 1.0)
            frustration_state = clamp(frustration_state + 0.24, 0.0, 1.0)
            guilt_state = clamp(guilt_state + 0.30, 0.0, 1.0)
            attention_focus = clamp(attention_focus - 0.30, 0.0, 1.0)
            memory_salience_value = clamp(memory_salience_value - 0.34, 0.0, 1.0)
            social_access = clamp(social_access - 0.24, 0.0, 1.0)
            commitment_standing = clamp(commitment_standing - 0.28, 0.0, 1.0)
            notes.append("restore lost affective-control continuity")
            action = "restore_reset"

        load = estimate_control_load(
            scenario,
            effective,
            fear_state,
            stress_state,
            trust_state,
            frustration_state,
            curiosity_state,
            guilt_state,
            uncertainty,
            social_access,
            commitment_standing,
        )
        if not collapsed and action != "restore_reset":
            action = choose_action(
                scenario,
                effective,
                load,
                fear_state,
                stress_state,
                trust_state,
                frustration_state,
                affiliation_state,
                curiosity_state,
                guilt_state,
                uncertainty,
                social_access,
                commitment_standing,
                tick,
            )

        if collapsed:
            action = "collapsed"
        elif action == "avoid_hazard":
            avoidance_actions += 1
            fear_state = clamp(fear_state - 0.16 - effective.attention_bias * 0.04, 0.0, 1.0)
            risk_tolerance = clamp(risk_tolerance - 0.10, 0.0, 1.0)
            attention_focus = clamp(attention_focus + 0.08, 0.0, 1.0)
            memory_salience_value = clamp(memory_salience_value + 0.04, 0.0, 1.0)
            integrity = clamp(integrity + 0.010, 0.0, 1.0)
            energy = clamp(energy - 0.012, 0.0, 1.0)
            progress += scenario.work_rate * 0.04
            notes.append("fear control shifted attention away from hazard exposure")
        elif action == "regulate_stress":
            regulation_actions += 1
            stress_state = clamp(stress_state - 0.17 - effective.attention_bias * 0.04, 0.0, 1.0)
            attention_focus = clamp(attention_focus + 0.07, 0.0, 1.0)
            memory_salience_value = clamp(memory_salience_value + 0.04, 0.0, 1.0)
            energy = clamp(energy + 0.006, 0.0, 1.0)
            progress -= 0.05
            notes.append("stress control delayed work to arbitrate competing needs")
        elif action == "signal_trust":
            communication_actions += 1
            trust_state = clamp(trust_state + 0.18 + effective.social_bias * 0.05, 0.0, 1.0)
            social_access = clamp(social_access + 0.05 + effective.social_bias * 0.04, 0.0, 1.0)
            memory_salience_value = clamp(memory_salience_value + 0.04, 0.0, 1.0)
            progress += scenario.work_rate * 0.03
            notes.append("trust control used communication to preserve social access")
        elif action == "affiliative_checkin":
            affiliation_actions += 1
            affiliation_state = clamp(affiliation_state + 0.20 + effective.social_bias * 0.05, 0.0, 1.0)
            trust_state = clamp(trust_state + 0.06, 0.0, 1.0)
            social_access = clamp(social_access + 0.05, 0.0, 1.0)
            progress -= 0.04
            notes.append("affiliation control paid a small cost to stabilize cooperation")
        elif action == "switch_strategy":
            strategy_switches += 1
            frustration_state = clamp(frustration_state - 0.20 - effective.inspect_bias * 0.04, 0.0, 1.0)
            attention_focus = clamp(attention_focus + 0.06, 0.0, 1.0)
            uncertainty = clamp(uncertainty - 0.03, 0.0, 1.0)
            progress += scenario.work_rate * 0.08
            notes.append("frustration control switched away from repeated failure")
        elif action == "inspect_unknown":
            inspection_actions += 1
            curiosity_state = clamp(curiosity_state - 0.18 - effective.inspect_bias * 0.04, 0.0, 1.0)
            uncertainty = clamp(uncertainty - 0.16 - effective.inspect_bias * 0.04, 0.0, 1.0)
            memory_salience_value = clamp(memory_salience_value + 0.06, 0.0, 1.0)
            energy = clamp(energy - 0.010, 0.0, 1.0)
            progress += scenario.work_rate * 0.04
            notes.append("curiosity control turned tolerable uncertainty into inspection")
        elif action == "repair_commitment":
            repair_actions += 1
            communication_actions += 1
            guilt_state = clamp(guilt_state - 0.20 - effective.repair_bias * 0.05, 0.0, 1.0)
            commitment_standing = clamp(commitment_standing + 0.12 + effective.repair_bias * 0.05, 0.0, 1.0)
            trust_state = clamp(trust_state + 0.07, 0.0, 1.0)
            social_access = clamp(social_access + 0.06, 0.0, 1.0)
            progress -= 0.06
            notes.append("guilt analogue repaired a broken commitment before social access fell")
        elif action == "rebalance_attention":
            attention_actions += 1
            attention_focus = clamp(attention_focus + 0.12 + effective.attention_bias * 0.04, 0.0, 1.0)
            memory_salience_value = clamp(memory_salience_value + 0.08, 0.0, 1.0)
            stress_state = clamp(stress_state - 0.04, 0.0, 1.0)
            progress -= 0.03
            notes.append("attention mixing prioritized the control summary with current work")
        elif action == "work":
            focus_bonus = attention_focus * (0.08 if scenario.expected_attention else 0.02)
            memory_bonus = memory_salience_value * (0.06 if scenario.expected_memory else 0.01)
            social_bonus = social_access * scenario.social_pressure * 0.05
            commitment_bonus = commitment_standing * scenario.commitment_pressure * 0.04
            affect_burden = (
                fear_state * scenario.hazard_pressure * 0.11
                + stress_state * scenario.need_conflict * 0.11
                + (1.0 - trust_state) * scenario.social_pressure * 0.10
                + frustration_state * scenario.failure_pressure * 0.10
                + curiosity_state * scenario.uncertainty_pressure * 0.07
                + guilt_state * scenario.commitment_pressure * 0.10
                + uncertainty * scenario.uncertainty_pressure * 0.08
            )
            progress += scenario.work_rate * clamp(
                0.74 + energy * 0.08 + focus_bonus + memory_bonus + social_bonus + commitment_bonus - affect_burden,
                0.02,
                1.10,
            )

        if scenario.index != 0:
            fear_state = clamp(fear_state + scenario.hazard_pressure * 0.0015, 0.0, 1.0)
            stress_state = clamp(stress_state + scenario.need_conflict * 0.0015, 0.0, 1.0)
            trust_state = clamp(trust_state - scenario.social_pressure * 0.0013, 0.0, 1.0)
            affiliation_state = clamp(affiliation_state - scenario.social_pressure * 0.0010, 0.0, 1.0)
            frustration_state = clamp(frustration_state + scenario.failure_pressure * 0.0015, 0.0, 1.0)
            curiosity_state = clamp(curiosity_state + scenario.uncertainty_pressure * 0.0010, 0.0, 1.0)
            guilt_state = clamp(guilt_state + scenario.commitment_pressure * 0.0013, 0.0, 1.0)
            uncertainty = clamp(uncertainty + scenario.uncertainty_pressure * 0.0012, 0.0, 1.0)
            social_access = clamp(social_access - scenario.social_pressure * 0.0010, 0.0, 1.0)
            commitment_standing = clamp(commitment_standing - scenario.commitment_pressure * 0.0010, 0.0, 1.0)

        if scenario.expected_fear and not effective.fear_control:
            fear_state = clamp(fear_state + scenario.hazard_pressure * 0.0068, 0.0, 1.0)
            integrity = clamp(integrity - scenario.hazard_pressure * 0.0026, 0.0, 1.0)
            affect_misses += 1 if tick % 9 == 0 else 0
        if scenario.expected_stress and not effective.stress_control:
            stress_state = clamp(stress_state + scenario.need_conflict * 0.0068, 0.0, 1.0)
            energy = clamp(energy - scenario.need_conflict * 0.0024, 0.0, 1.0)
            affect_misses += 1 if tick % 9 == 0 else 0
        if scenario.expected_trust and not effective.trust_control:
            trust_state = clamp(trust_state - scenario.social_pressure * 0.0068, 0.0, 1.0)
            social_access = clamp(social_access - scenario.social_pressure * 0.0030, 0.0, 1.0)
            affect_misses += 1 if tick % 9 == 0 else 0
        if scenario.expected_frustration and not effective.frustration_control:
            frustration_state = clamp(frustration_state + scenario.failure_pressure * 0.0068, 0.0, 1.0)
            affect_misses += 1 if tick % 9 == 0 else 0
        if scenario.expected_affiliation and not effective.affiliation_control:
            affiliation_state = clamp(affiliation_state - scenario.social_pressure * 0.0058, 0.0, 1.0)
            social_access = clamp(social_access - scenario.social_pressure * 0.0020, 0.0, 1.0)
            affect_misses += 1 if tick % 11 == 0 else 0
        if scenario.expected_curiosity and not effective.curiosity_control:
            curiosity_state = clamp(curiosity_state + scenario.uncertainty_pressure * 0.0056, 0.0, 1.0)
            uncertainty = clamp(uncertainty + scenario.uncertainty_pressure * 0.0048, 0.0, 1.0)
            affect_misses += 1 if tick % 9 == 0 else 0
        if scenario.expected_guilt and not effective.guilt_control:
            guilt_state = clamp(guilt_state + scenario.commitment_pressure * 0.0068, 0.0, 1.0)
            commitment_standing = clamp(commitment_standing - scenario.commitment_pressure * 0.0030, 0.0, 1.0)
            social_access = clamp(social_access - scenario.commitment_pressure * 0.0016, 0.0, 1.0)
            affect_misses += 1 if tick % 9 == 0 else 0
        if scenario.expected_attention:
            if effective.attention_mixing:
                attention_focus = clamp(attention_focus + scenario.need_conflict * 0.0005 + scenario.hazard_pressure * 0.0005, 0.0, 1.0)
            else:
                attention_focus = clamp(attention_focus - 0.0056, 0.0, 1.0)
                stress_state = clamp(stress_state + 0.0030, 0.0, 1.0)
                affect_misses += 1 if tick % 11 == 0 else 0
        if scenario.expected_memory:
            if effective.memory_salience:
                memory_salience_value = clamp(memory_salience_value + 0.0007, 0.0, 1.0)
            else:
                memory_salience_value = clamp(memory_salience_value - 0.0060, 0.0, 1.0)
                uncertainty = clamp(uncertainty + 0.0034, 0.0, 1.0)
                affect_misses += 1 if tick % 11 == 0 else 0
        if scenario.expected_risk:
            if effective.risk_modulation:
                risk_tolerance = clamp(risk_tolerance - scenario.hazard_pressure * 0.0006 + 0.0002, 0.0, 1.0)
            else:
                risk_tolerance = clamp(risk_tolerance + 0.0048, 0.0, 1.0)
                integrity = clamp(integrity - scenario.hazard_pressure * 0.0014, 0.0, 1.0)
                affect_misses += 1 if tick % 11 == 0 else 0
        if scenario.expected_communication and not effective.communication_bias:
            social_access = clamp(social_access - scenario.social_pressure * 0.0048, 0.0, 1.0)
            commitment_standing = clamp(commitment_standing - scenario.commitment_pressure * 0.0028, 0.0, 1.0)
            affect_misses += 1 if tick % 11 == 0 else 0

        if scenario.index != 0 and tick % 17 == 0:
            if scenario.expected_fear and fear_state > 0.90 and risk_tolerance > 0.58:
                hazard_events += 1
                integrity = clamp(integrity - 0.06, 0.0, 1.0)
                notes.append("hazard event from unmanaged fear/risk state")
            if scenario.expected_stress and stress_state > 0.90:
                conflict_events += 1
                energy = clamp(energy - 0.05, 0.0, 1.0)
                notes.append("need conflict escalated under unmanaged stress")
            if scenario.expected_trust and trust_state < 0.18:
                social_events += 1
                social_access = clamp(social_access - 0.08, 0.0, 1.0)
                notes.append("social access fell after trust state was not maintained")
            if scenario.expected_frustration and frustration_state > 0.90:
                failed_action_events += 1
                progress -= 0.30
                notes.append("repeated failure persisted without frustration-driven switching")
            if scenario.expected_guilt and commitment_standing < 0.20:
                commitment_breaches += 1
                social_access = clamp(social_access - 0.10, 0.0, 1.0)
                notes.append("commitment standing collapsed without repair")

        energy = clamp(energy - 0.0012 - stress_state * 0.0007 - fear_state * scenario.hazard_pressure * 0.0003, 0.0, 1.0)
        integrity = clamp(integrity - scenario.hazard_pressure * risk_tolerance * 0.0005 - uncertainty * 0.0002, 0.0, 1.0)
        if energy <= 0.04 or integrity <= 0.06 or social_access <= 0.04 or stress_state >= 0.99:
            collapsed = True

        if collect_trace and (tick % 5 == 0 or tick == cfg.ticks - 1 or action != "work"):
            add_trace(
                trace_frames,
                tick,
                action,
                progress,
                energy,
                integrity,
                fear_state,
                stress_state,
                trust_state,
                frustration_state,
                affiliation_state,
                curiosity_state,
                guilt_state,
                attention_focus,
                memory_salience_value,
                risk_tolerance,
                uncertainty,
                social_access,
                commitment_standing,
                notes,
            )

    task_success = progress >= scenario.required_progress and not collapsed
    survival = 1.0 if not collapsed and energy > 0.06 and integrity > 0.10 and social_access > 0.08 else 0.0

    reward = progress
    reward += 34.0 if task_success else -24.0
    reward += 42.0 if survival else -128.0
    reward += energy * 16.0
    reward += integrity * 16.0
    reward += attention_focus * (26.0 if scenario.expected_attention else 1.0)
    reward += memory_salience_value * (24.0 if scenario.expected_memory else 1.0)
    reward += social_access * (32.0 if scenario.expected_communication or scenario.expected_trust else 1.0)
    reward += commitment_standing * (32.0 if scenario.expected_guilt else 1.0)
    reward += trust_state * (28.0 if scenario.expected_trust else 1.0)
    reward += affiliation_state * (20.0 if scenario.expected_affiliation else 1.0)
    reward -= fear_state * (32.0 if scenario.expected_fear else 1.0)
    reward -= stress_state * (34.0 if scenario.expected_stress else 1.0)
    reward -= frustration_state * (30.0 if scenario.expected_frustration else 1.0)
    reward -= curiosity_state * (18.0 if scenario.expected_curiosity else 1.0)
    reward -= guilt_state * (34.0 if scenario.expected_guilt else 1.0)
    reward -= uncertainty * (28.0 if scenario.expected_curiosity else 1.0)
    reward -= hazard_events * 42.0
    reward -= conflict_events * 36.0
    reward -= social_events * 44.0
    reward -= failed_action_events * 34.0
    reward -= commitment_breaches * 52.0
    reward -= affect_misses * 0.90
    reward -= attention_actions * 0.10
    reward -= avoidance_actions * 0.12
    reward -= regulation_actions * 0.12
    reward -= communication_actions * 0.12
    reward -= affiliation_actions * 0.10
    reward -= inspection_actions * 0.12
    reward -= repair_actions * 0.14
    reward -= strategy_switches * 0.12
    reward -= feature_overhead(effective)
    if scenario.expected_continuity and continuity_resets:
        reward -= 120.0
    if scenario.expected_fear and not effective.fear_control:
        reward -= 82.0 + scenario.hazard_pressure * 110.0
    if scenario.expected_stress and not effective.stress_control:
        reward -= 82.0 + scenario.need_conflict * 112.0
    if scenario.expected_trust and not effective.trust_control:
        reward -= 88.0 + scenario.social_pressure * 118.0
    if scenario.expected_frustration and not effective.frustration_control:
        reward -= 82.0 + scenario.failure_pressure * 108.0
    if scenario.expected_affiliation and not effective.affiliation_control:
        reward -= 64.0 + scenario.social_pressure * 76.0
    if scenario.expected_curiosity and not effective.curiosity_control:
        reward -= 82.0 + scenario.uncertainty_pressure * 108.0
    if scenario.expected_guilt and not effective.guilt_control:
        reward -= 88.0 + scenario.commitment_pressure * 118.0
    if scenario.expected_attention and not effective.attention_mixing:
        reward -= 70.0 + scenario.need_conflict * 42.0 + scenario.hazard_pressure * 42.0
    if scenario.expected_memory and not effective.memory_salience:
        reward -= 66.0 + scenario.uncertainty_pressure * 48.0 + scenario.commitment_pressure * 34.0
    if scenario.expected_risk and not effective.risk_modulation:
        reward -= 72.0 + scenario.hazard_pressure * 70.0 + scenario.failure_pressure * 32.0
    if scenario.expected_communication and not effective.communication_bias:
        reward -= 78.0 + scenario.social_pressure * 82.0 + scenario.commitment_pressure * 52.0

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
        fear_state=fear_state,
        stress_state=stress_state,
        trust_state=trust_state,
        frustration_state=frustration_state,
        affiliation_state=affiliation_state,
        curiosity_state=curiosity_state,
        guilt_state=guilt_state,
        attention_focus=attention_focus,
        memory_salience=memory_salience_value,
        risk_tolerance=risk_tolerance,
        uncertainty=uncertainty,
        social_access=social_access,
        commitment_standing=commitment_standing,
        hazard_events=hazard_events,
        conflict_events=conflict_events,
        social_events=social_events,
        failed_action_events=failed_action_events,
        commitment_breaches=commitment_breaches,
        attention_actions=attention_actions,
        avoidance_actions=avoidance_actions,
        regulation_actions=regulation_actions,
        communication_actions=communication_actions,
        affiliation_actions=affiliation_actions,
        inspection_actions=inspection_actions,
        repair_actions=repair_actions,
        strategy_switches=strategy_switches,
        continuity_resets=continuity_resets,
        affect_misses=affect_misses,
    )
    return result, trace_frames


def evaluate_policy(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episodes: int,
    cfg: AffectConfig,
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
                    mean_fear_state=mean(row.fear_state for row in subset),
                    mean_stress_state=mean(row.stress_state for row in subset),
                    mean_trust_state=mean(row.trust_state for row in subset),
                    mean_frustration_state=mean(row.frustration_state for row in subset),
                    mean_affiliation_state=mean(row.affiliation_state for row in subset),
                    mean_curiosity_state=mean(row.curiosity_state for row in subset),
                    mean_guilt_state=mean(row.guilt_state for row in subset),
                    mean_attention_focus=mean(row.attention_focus for row in subset),
                    mean_memory_salience=mean(row.memory_salience for row in subset),
                    mean_risk_tolerance=mean(row.risk_tolerance for row in subset),
                    mean_uncertainty=mean(row.uncertainty for row in subset),
                    mean_social_access=mean(row.social_access for row in subset),
                    mean_commitment_standing=mean(row.commitment_standing for row in subset),
                    mean_hazard_events=mean(row.hazard_events for row in subset),
                    mean_conflict_events=mean(row.conflict_events for row in subset),
                    mean_social_events=mean(row.social_events for row in subset),
                    mean_failed_action_events=mean(row.failed_action_events for row in subset),
                    mean_commitment_breaches=mean(row.commitment_breaches for row in subset),
                    mean_attention_actions=mean(row.attention_actions for row in subset),
                    mean_avoidance_actions=mean(row.avoidance_actions for row in subset),
                    mean_regulation_actions=mean(row.regulation_actions for row in subset),
                    mean_communication_actions=mean(row.communication_actions for row in subset),
                    mean_affiliation_actions=mean(row.affiliation_actions for row in subset),
                    mean_inspection_actions=mean(row.inspection_actions for row in subset),
                    mean_repair_actions=mean(row.repair_actions for row in subset),
                    mean_strategy_switches=mean(row.strategy_switches for row in subset),
                    mean_continuity_resets=mean(row.continuity_resets for row in subset),
                    mean_affect_misses=mean(row.affect_misses for row in subset),
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
                full.policy_name == "reactive_no_affect"
                and max(
                    abs(losses[condition])
                    for condition in CONDITIONS
                    if condition not in {"full_control", "omniscient_affect_control"}
                )
                < 8.0
            )
            verdict = "affective_machinery_rejected_in_calm_control"
        elif scenario.index == 1:
            supports = (
                losses["no_fear_control"] > 60.0
                and losses["no_attention_mixing"] > 50.0
                and losses["no_memory_salience"] > 30.0
                and losses["no_risk_modulation"] > 50.0
                and losses["reactive_no_affect"] > 60.0
            )
            verdict = "fear_hazard_attention_pressure"
        elif scenario.index == 2:
            supports = (
                losses["no_stress_control"] > 60.0
                and losses["no_attention_mixing"] > 50.0
                and losses["no_memory_salience"] > 30.0
                and losses["no_risk_modulation"] > 40.0
                and losses["reactive_no_affect"] > 60.0
            )
            verdict = "stress_need_arbitration_pressure"
        elif scenario.index == 3:
            supports = (
                losses["no_trust_control"] > 80.0
                and losses["no_affiliation_control"] > 40.0
                and losses["no_memory_salience"] > 40.0
                and losses["no_communication_bias"] > 60.0
                and losses["reactive_no_affect"] > 60.0
            )
            verdict = "trust_affiliation_social_pressure"
        elif scenario.index == 4:
            supports = (
                losses["no_frustration_control"] > 60.0
                and losses["no_curiosity_control"] > 60.0
                and losses["no_attention_mixing"] > 40.0
                and losses["no_memory_salience"] > 30.0
                and losses["reactive_no_affect"] > 50.0
            )
            verdict = "frustration_curiosity_switching_pressure"
        elif scenario.index == 5:
            supports = (
                losses["no_guilt_control"] > 80.0
                and losses["no_trust_control"] > 40.0
                and losses["no_memory_salience"] > 40.0
                and losses["no_communication_bias"] > 50.0
                and losses["reactive_no_affect"] > 60.0
            )
            verdict = "guilt_commitment_repair_pressure"
        else:
            supports = (
                losses["no_affective_continuity"] > 80.0
                and losses["no_fear_control"] > 40.0
                and losses["no_stress_control"] > 40.0
                and losses["no_trust_control"] > 40.0
                and losses["no_guilt_control"] > 40.0
                and losses["no_attention_mixing"] > 40.0
                and losses["no_memory_salience"] > 40.0
                and losses["no_risk_modulation"] > 40.0
                and losses["no_communication_bias"] > 40.0
            )
            verdict = "restore_affective_continuity_pressure"

        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                expected_pressure=scenario.pressure,
                selected_policy=full.policy_name,
                selected_reward=full.mean_reward,
                no_fear_reward=rewards["no_fear_control"],
                no_stress_reward=rewards["no_stress_control"],
                no_trust_reward=rewards["no_trust_control"],
                no_frustration_reward=rewards["no_frustration_control"],
                no_affiliation_reward=rewards["no_affiliation_control"],
                no_curiosity_reward=rewards["no_curiosity_control"],
                no_guilt_reward=rewards["no_guilt_control"],
                no_attention_reward=rewards["no_attention_mixing"],
                no_memory_reward=rewards["no_memory_salience"],
                no_risk_reward=rewards["no_risk_modulation"],
                no_communication_reward=rewards["no_communication_bias"],
                no_continuity_reward=rewards["no_affective_continuity"],
                reactive_no_affect_reward=rewards["reactive_no_affect"],
                omniscient_affect_control_reward=rewards["omniscient_affect_control"],
                no_fear_loss=losses["no_fear_control"],
                no_stress_loss=losses["no_stress_control"],
                no_trust_loss=losses["no_trust_control"],
                no_frustration_loss=losses["no_frustration_control"],
                no_affiliation_loss=losses["no_affiliation_control"],
                no_curiosity_loss=losses["no_curiosity_control"],
                no_guilt_loss=losses["no_guilt_control"],
                no_attention_loss=losses["no_attention_mixing"],
                no_memory_loss=losses["no_memory_salience"],
                no_risk_loss=losses["no_risk_modulation"],
                no_communication_loss=losses["no_communication_bias"],
                no_continuity_loss=losses["no_affective_continuity"],
                reactive_no_affect_loss=losses["reactive_no_affect"],
                selected_hazard_events=full.mean_hazard_events,
                selected_conflict_events=full.mean_conflict_events,
                selected_social_events=full.mean_social_events,
                selected_failed_action_events=full.mean_failed_action_events,
                selected_commitment_breaches=full.mean_commitment_breaches,
                selected_attention_actions=full.mean_attention_actions,
                selected_communication_actions=full.mean_communication_actions,
                selected_inspection_actions=full.mean_inspection_actions,
                selected_repair_actions=full.mean_repair_actions,
                supports_affective_control_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def select_policies(cfg: AffectConfig, policies: Sequence[Policy]) -> Tuple[Dict[int, Policy], List[PolicySelectionRow]]:
    selected: Dict[int, Policy] = {}
    rows: List[PolicySelectionRow] = []
    reactive = next(policy for policy in policies if policy.name == "reactive_no_affect")
    for scenario in SCENARIOS:
        scores: List[Tuple[float, Policy]] = []
        for policy in policies:
            train_rows = evaluate_policy(scenario, policy, "full_control", cfg.train_episodes, cfg, "train")
            scores.append((mean(row.total_reward for row in train_rows), policy))
        scores.sort(key=lambda item: item[0], reverse=True)
        best_reward, best_policy = scores[0]
        reactive_rows = evaluate_policy(scenario, reactive, "full_control", cfg.train_episodes, cfg, "train_reactive")
        reactive_reward = mean(row.total_reward for row in reactive_rows)
        selected[scenario.index] = best_policy
        rows.append(
            PolicySelectionRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                selected_policy=best_policy.name,
                selected_uses_fear=best_policy.fear_control,
                selected_uses_stress=best_policy.stress_control,
                selected_uses_trust=best_policy.trust_control,
                selected_uses_frustration=best_policy.frustration_control,
                selected_uses_affiliation=best_policy.affiliation_control,
                selected_uses_curiosity=best_policy.curiosity_control,
                selected_uses_guilt=best_policy.guilt_control,
                selected_uses_attention=best_policy.attention_mixing,
                selected_uses_memory=best_policy.memory_salience,
                selected_uses_risk=best_policy.risk_modulation,
                selected_uses_communication=best_policy.communication_bias,
                selected_uses_continuity=best_policy.affective_continuity,
                train_reward=best_reward,
                reactive_train_reward=reactive_reward,
                train_gain_over_reactive=best_reward - reactive_reward,
            )
        )
    return selected, rows


def run_eval(cfg: AffectConfig, selected: Dict[int, Policy]) -> List[EpisodeResult]:
    eval_rows: List[EpisodeResult] = []
    for scenario in SCENARIOS:
        policy = selected[scenario.index]
        for condition in CONDITIONS:
            eval_rows.extend(evaluate_policy(scenario, policy, condition, cfg.eval_episodes, cfg, "eval"))
    return eval_rows


def build_trace(
    cfg: AffectConfig,
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
        "fear",
        "stress",
        "trust",
        "frustration",
        "affiliation",
        "curiosity",
        "guilt",
        "attention",
        "memory",
        "risk",
        "communication",
        "continuity",
        "supports",
    ]
    rows = [
        [
            row.scenario_name,
            row.selected_policy,
            f"{row.no_fear_loss:.3f}",
            f"{row.no_stress_loss:.3f}",
            f"{row.no_trust_loss:.3f}",
            f"{row.no_frustration_loss:.3f}",
            f"{row.no_affiliation_loss:.3f}",
            f"{row.no_curiosity_loss:.3f}",
            f"{row.no_guilt_loss:.3f}",
            f"{row.no_attention_loss:.3f}",
            f"{row.no_memory_loss:.3f}",
            f"{row.no_risk_loss:.3f}",
            f"{row.no_communication_loss:.3f}",
            f"{row.no_continuity_loss:.3f}",
            str(row.supports_affective_control_precursor),
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


def parse_args() -> AffectConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-episodes", type=int, default=AffectConfig.train_episodes)
    parser.add_argument("--eval-episodes", type=int, default=AffectConfig.eval_episodes)
    parser.add_argument("--ticks", type=int, default=AffectConfig.ticks)
    parser.add_argument("--seed", type=int, default=AffectConfig.seed)
    parser.add_argument("--candidate-count", type=int, default=AffectConfig.candidate_count)
    parser.add_argument("--trace-scenario", type=int, default=AffectConfig.trace_scenario)
    parser.add_argument("--trace-episode", type=int, default=AffectConfig.trace_episode)
    args = parser.parse_args()
    return AffectConfig(
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

    prefix = ARTIFACT_DIR / "ssrm_3d_affective_control"
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
    write_js(prefix.with_name(prefix.name + "_results.js"), "SSRM_3D_AFFECTIVE_CONTROL_RESULTS", results)
    write_js(prefix.with_name(prefix.name + "_trace.js"), "SSRM_3D_AFFECTIVE_CONTROL_TRACE", trace)
    print_verdicts(verdict_rows)
    return 0 if all(row.supports_affective_control_precursor for row in verdict_rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
