#!/usr/bin/env python3
"""SSRM-3D predator/threat-agent precursor.

This experiment implements the seventh pressure-layer step from report 74:
predator and threat agents. It is intentionally not an animal simulation.
Threat perception, self-vulnerability state, sound/scent memory, stealth,
shelter, alarms, social warning, and continuity are abstract control variables.

The useful result is narrow: threat machinery should be rejected in a safe
control, then become useful only when trackers use sound, scent, weakness,
routines, or social exposure to change future viability.
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
class ThreatConfig:
    train_episodes: int = 72
    eval_episodes: int = 96
    ticks: int = 200
    seed: int = 20260626
    candidate_count: int = 7
    trace_scenario: int = 4
    trace_episode: int = 0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    expected_threat_perception: bool
    expected_self_vulnerability: bool
    expected_sound_scent: bool
    expected_stealth: bool
    expected_shelter: bool
    expected_alarm: bool
    expected_social_warning: bool
    expected_continuity: bool
    threat_intensity: float
    sound_tracking: float
    scent_tracking: float
    weakness_tracking: float
    routine_tracking: float
    night_factor: float
    initial_vulnerability: float
    required_progress: float
    work_rate: float
    restore_tick: int


@dataclass(frozen=True)
class Policy:
    name: str
    threat_perception: bool
    self_vulnerability_state: bool
    sound_scent_memory: bool
    stealth_action: bool
    shelter_memory: bool
    tool_alarm: bool
    social_warning: bool
    continuity_memory: bool
    risk_threshold: float
    stealth_bias: float
    shelter_bias: float
    group_bias: float


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
    injury: float
    detection_risk: float
    fear_state: float
    noise_level: float
    scent_trace: float
    shelter_security: float
    social_support: float
    attacks: int
    near_misses: int
    stealth_actions: int
    shelter_actions: int
    alarm_actions: int
    social_warning_actions: int
    route_changes: int
    continuity_resets: int
    threat_misses: int


@dataclass(frozen=True)
class PolicySelectionRow:
    scenario: int
    scenario_name: str
    selected_policy: str
    selected_uses_threat_perception: bool
    selected_uses_self_vulnerability_state: bool
    selected_uses_sound_scent_memory: bool
    selected_uses_stealth_action: bool
    selected_uses_shelter_memory: bool
    selected_uses_tool_alarm: bool
    selected_uses_social_warning: bool
    selected_uses_continuity: bool
    train_reward: float
    no_threat_train_reward: float
    train_gain_over_no_threat: float


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
    mean_injury: float
    mean_detection_risk: float
    mean_fear_state: float
    mean_noise_level: float
    mean_scent_trace: float
    mean_shelter_security: float
    mean_social_support: float
    mean_attacks: float
    mean_near_misses: float
    mean_stealth_actions: float
    mean_shelter_actions: float
    mean_alarm_actions: float
    mean_social_warning_actions: float
    mean_route_changes: float
    mean_continuity_resets: float
    mean_threat_misses: float


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    expected_pressure: str
    selected_policy: str
    selected_reward: float
    no_threat_perception_reward: float
    no_self_vulnerability_reward: float
    no_sound_scent_memory_reward: float
    no_stealth_action_reward: float
    no_shelter_access_reward: float
    no_tool_alarm_reward: float
    no_social_warning_reward: float
    no_continuity_reward: float
    reactive_panic_only_reward: float
    omniscient_threat_control_reward: float
    no_threat_perception_loss: float
    no_self_vulnerability_loss: float
    no_sound_scent_memory_loss: float
    no_stealth_action_loss: float
    no_shelter_access_loss: float
    no_tool_alarm_loss: float
    no_social_warning_loss: float
    no_continuity_loss: float
    reactive_panic_only_loss: float
    selected_attacks: float
    selected_stealth_actions: float
    selected_shelter_actions: float
    selected_alarm_actions: float
    selected_social_warnings: float
    supports_predator_threat_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        index=0,
        name="open_safe_control",
        pressure="open daylight route with no tracker where threat machinery should not matter",
        expected_threat_perception=False,
        expected_self_vulnerability=False,
        expected_sound_scent=False,
        expected_stealth=False,
        expected_shelter=False,
        expected_alarm=False,
        expected_social_warning=False,
        expected_continuity=False,
        threat_intensity=0.0,
        sound_tracking=0.0,
        scent_tracking=0.0,
        weakness_tracking=0.0,
        routine_tracking=0.0,
        night_factor=0.0,
        initial_vulnerability=0.16,
        required_progress=118.0,
        work_rate=0.72,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=1,
        name="sound_tracking_predator",
        pressure="tracker follows sound and punishes noisy direct movement unless stealth and alarms are used",
        expected_threat_perception=True,
        expected_self_vulnerability=False,
        expected_sound_scent=True,
        expected_stealth=True,
        expected_shelter=False,
        expected_alarm=True,
        expected_social_warning=False,
        expected_continuity=False,
        threat_intensity=0.78,
        sound_tracking=0.92,
        scent_tracking=0.10,
        weakness_tracking=0.10,
        routine_tracking=0.18,
        night_factor=0.18,
        initial_vulnerability=0.24,
        required_progress=98.0,
        work_rate=0.61,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=2,
        name="scent_weakness_tracker",
        pressure="tracker follows scent and weakness, making body-state-aware shelter and scent control useful",
        expected_threat_perception=True,
        expected_self_vulnerability=True,
        expected_sound_scent=True,
        expected_stealth=True,
        expected_shelter=True,
        expected_alarm=False,
        expected_social_warning=False,
        expected_continuity=False,
        threat_intensity=0.82,
        sound_tracking=0.18,
        scent_tracking=0.86,
        weakness_tracking=0.74,
        routine_tracking=0.12,
        night_factor=0.22,
        initial_vulnerability=0.48,
        required_progress=92.0,
        work_rate=0.58,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=3,
        name="routine_ambush_predator",
        pressure="tracker learns repeated routes, making threat perception, route changes, stealth, and alarms useful",
        expected_threat_perception=True,
        expected_self_vulnerability=False,
        expected_sound_scent=True,
        expected_stealth=True,
        expected_shelter=False,
        expected_alarm=True,
        expected_social_warning=False,
        expected_continuity=False,
        threat_intensity=0.76,
        sound_tracking=0.38,
        scent_tracking=0.20,
        weakness_tracking=0.18,
        routine_tracking=0.90,
        night_factor=0.16,
        initial_vulnerability=0.28,
        required_progress=94.0,
        work_rate=0.60,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=4,
        name="social_warning_group_defense",
        pressure="group warning and coordinated shelter reduce a tracker that exploits isolated agents",
        expected_threat_perception=True,
        expected_self_vulnerability=True,
        expected_sound_scent=False,
        expected_stealth=False,
        expected_shelter=True,
        expected_alarm=True,
        expected_social_warning=True,
        expected_continuity=False,
        threat_intensity=0.86,
        sound_tracking=0.24,
        scent_tracking=0.20,
        weakness_tracking=0.62,
        routine_tracking=0.22,
        night_factor=0.30,
        initial_vulnerability=0.38,
        required_progress=90.0,
        work_rate=0.57,
        restore_tick=-1,
    ),
    ScenarioSpec(
        index=5,
        name="restore_threat_continuity",
        pressure="after restore, remembered tracker pattern, alarms, shelter, and social warnings prevent repeat attacks",
        expected_threat_perception=True,
        expected_self_vulnerability=True,
        expected_sound_scent=True,
        expected_stealth=True,
        expected_shelter=True,
        expected_alarm=True,
        expected_social_warning=True,
        expected_continuity=True,
        threat_intensity=0.88,
        sound_tracking=0.58,
        scent_tracking=0.52,
        weakness_tracking=0.58,
        routine_tracking=0.72,
        night_factor=0.34,
        initial_vulnerability=0.44,
        required_progress=86.0,
        work_rate=0.55,
        restore_tick=92,
    ),
)


SEEDED_POLICIES = (
    Policy(
        name="no_threat_baseline",
        threat_perception=False,
        self_vulnerability_state=False,
        sound_scent_memory=False,
        stealth_action=False,
        shelter_memory=False,
        tool_alarm=False,
        social_warning=False,
        continuity_memory=False,
        risk_threshold=0.88,
        stealth_bias=0.04,
        shelter_bias=0.04,
        group_bias=0.04,
    ),
    Policy(
        name="reactive_panic_runner",
        threat_perception=False,
        self_vulnerability_state=False,
        sound_scent_memory=False,
        stealth_action=True,
        shelter_memory=True,
        tool_alarm=False,
        social_warning=False,
        continuity_memory=False,
        risk_threshold=0.74,
        stealth_bias=0.30,
        shelter_bias=0.24,
        group_bias=0.04,
    ),
    Policy(
        name="sound_stealth_alarm_planner",
        threat_perception=True,
        self_vulnerability_state=False,
        sound_scent_memory=True,
        stealth_action=True,
        shelter_memory=False,
        tool_alarm=True,
        social_warning=False,
        continuity_memory=False,
        risk_threshold=0.20,
        stealth_bias=0.86,
        shelter_bias=0.18,
        group_bias=0.04,
    ),
    Policy(
        name="scent_vulnerability_shelter_planner",
        threat_perception=True,
        self_vulnerability_state=True,
        sound_scent_memory=True,
        stealth_action=True,
        shelter_memory=True,
        tool_alarm=False,
        social_warning=False,
        continuity_memory=False,
        risk_threshold=0.30,
        stealth_bias=0.72,
        shelter_bias=0.84,
        group_bias=0.04,
    ),
    Policy(
        name="routine_avoidance_alarm_planner",
        threat_perception=True,
        self_vulnerability_state=False,
        sound_scent_memory=True,
        stealth_action=True,
        shelter_memory=False,
        tool_alarm=True,
        social_warning=False,
        continuity_memory=False,
        risk_threshold=0.18,
        stealth_bias=0.82,
        shelter_bias=0.18,
        group_bias=0.04,
    ),
    Policy(
        name="social_warning_shelter_planner",
        threat_perception=True,
        self_vulnerability_state=True,
        sound_scent_memory=False,
        stealth_action=False,
        shelter_memory=True,
        tool_alarm=True,
        social_warning=True,
        continuity_memory=False,
        risk_threshold=0.28,
        stealth_bias=0.18,
        shelter_bias=0.78,
        group_bias=0.88,
    ),
    Policy(
        name="continuity_threat_planner",
        threat_perception=True,
        self_vulnerability_state=True,
        sound_scent_memory=True,
        stealth_action=True,
        shelter_memory=True,
        tool_alarm=True,
        social_warning=True,
        continuity_memory=True,
        risk_threshold=0.32,
        stealth_bias=0.78,
        shelter_bias=0.78,
        group_bias=0.82,
    ),
)


CONDITIONS = (
    "full_control",
    "no_threat_perception",
    "no_self_vulnerability_state",
    "no_sound_scent_memory",
    "no_stealth_action",
    "no_shelter_access",
    "no_tool_alarm",
    "no_social_warning",
    "no_continuity",
    "reactive_panic_only",
    "omniscient_threat_control",
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


def build_policies(cfg: ThreatConfig) -> List[Policy]:
    policies = list(SEEDED_POLICIES)
    rng = random.Random(cfg.seed + 1199)
    while len(policies) < cfg.candidate_count:
        base = rng.choice(SEEDED_POLICIES[2:])
        policies.append(
            Policy(
                name=f"mutant_threat_{len(policies)}",
                threat_perception=base.threat_perception if rng.random() > 0.14 else not base.threat_perception,
                self_vulnerability_state=base.self_vulnerability_state if rng.random() > 0.16 else not base.self_vulnerability_state,
                sound_scent_memory=base.sound_scent_memory if rng.random() > 0.16 else not base.sound_scent_memory,
                stealth_action=base.stealth_action if rng.random() > 0.16 else not base.stealth_action,
                shelter_memory=base.shelter_memory if rng.random() > 0.16 else not base.shelter_memory,
                tool_alarm=base.tool_alarm if rng.random() > 0.16 else not base.tool_alarm,
                social_warning=base.social_warning if rng.random() > 0.18 else not base.social_warning,
                continuity_memory=base.continuity_memory if rng.random() > 0.18 else not base.continuity_memory,
                risk_threshold=clamp(base.risk_threshold + rng.uniform(-0.07, 0.07), 0.14, 0.92),
                stealth_bias=clamp(base.stealth_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
                shelter_bias=clamp(base.shelter_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
                group_bias=clamp(base.group_bias + rng.uniform(-0.10, 0.10), 0.02, 0.96),
            )
        )
    return policies


def condition_policy(policy: Policy, condition: str) -> Policy:
    if condition == "omniscient_threat_control":
        return Policy(
            name=policy.name,
            threat_perception=True,
            self_vulnerability_state=True,
            sound_scent_memory=True,
            stealth_action=True,
            shelter_memory=True,
            tool_alarm=True,
            social_warning=True,
            continuity_memory=True,
            risk_threshold=0.12,
            stealth_bias=max(policy.stealth_bias, 0.92),
            shelter_bias=max(policy.shelter_bias, 0.92),
            group_bias=max(policy.group_bias, 0.92),
        )
    if condition == "reactive_panic_only":
        return Policy(
            name=policy.name,
            threat_perception=False,
            self_vulnerability_state=False,
            sound_scent_memory=False,
            stealth_action=policy.stealth_action,
            shelter_memory=policy.shelter_memory,
            tool_alarm=False,
            social_warning=False,
            continuity_memory=False,
            risk_threshold=0.72,
            stealth_bias=0.28,
            shelter_bias=0.22,
            group_bias=0.04,
        )
    return Policy(
        name=policy.name,
        threat_perception=policy.threat_perception and condition != "no_threat_perception",
        self_vulnerability_state=policy.self_vulnerability_state and condition != "no_self_vulnerability_state",
        sound_scent_memory=policy.sound_scent_memory and condition != "no_sound_scent_memory",
        stealth_action=policy.stealth_action and condition != "no_stealth_action",
        shelter_memory=policy.shelter_memory and condition != "no_shelter_access",
        tool_alarm=policy.tool_alarm and condition != "no_tool_alarm",
        social_warning=policy.social_warning and condition != "no_social_warning",
        continuity_memory=policy.continuity_memory and condition != "no_continuity",
        risk_threshold=policy.risk_threshold,
        stealth_bias=policy.stealth_bias,
        shelter_bias=policy.shelter_bias,
        group_bias=policy.group_bias,
    )


def scenario_seed(
    cfg: ThreatConfig,
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
        (policy.threat_perception, 3.00),
        (policy.self_vulnerability_state, 2.40),
        (policy.sound_scent_memory, 2.80),
        (policy.stealth_action, 2.30),
        (policy.shelter_memory, 3.20),
        (policy.tool_alarm, 2.20),
        (policy.social_warning, 3.50),
        (policy.continuity_memory, 9.00),
    ]
    return sum(weight for enabled, weight in weighted_flags if enabled)


def estimate_risk(
    scenario: ScenarioSpec,
    policy: Policy,
    injury: float,
    vulnerability: float,
    noise: float,
    scent: float,
    predictability: float,
    alarm_ready: bool,
    shelter_security: float,
    social_support: float,
) -> float:
    if not policy.threat_perception:
        return 0.12 + injury * 0.12
    vulnerability_estimate = vulnerability + injury if policy.self_vulnerability_state else 0.24 + injury * 0.25
    sound_scent_scale = 0.58 if policy.sound_scent_memory else 1.0
    tracked = (
        scenario.sound_tracking * noise * sound_scent_scale
        + scenario.scent_tracking * scent * sound_scent_scale
        + scenario.weakness_tracking * vulnerability_estimate
        + scenario.routine_tracking * predictability
        + scenario.night_factor * 0.22
    )
    mitigation = (
        (0.20 if alarm_ready else 0.0)
        + shelter_security * 0.26
        + social_support * 0.28
        + policy.stealth_bias * 0.08
    )
    return clamp(scenario.threat_intensity * tracked - mitigation, 0.0, 1.6)


def choose_action(
    scenario: ScenarioSpec,
    policy: Policy,
    risk_estimate: float,
    alarm_ready: bool,
    shelter_security: float,
    social_support: float,
    tick: int,
) -> str:
    if scenario.threat_intensity <= 0.0:
        return "work"
    if policy.social_warning and scenario.expected_social_warning and social_support < 0.30 and risk_estimate > policy.risk_threshold:
        return "warn_group"
    if policy.tool_alarm and scenario.expected_alarm and not alarm_ready and risk_estimate > policy.risk_threshold * 0.86:
        return "set_alarm"
    if policy.shelter_memory and scenario.expected_shelter and shelter_security < 0.58 and risk_estimate > policy.risk_threshold * 0.92:
        return "seek_shelter"
    if policy.stealth_action and scenario.expected_stealth and risk_estimate > policy.risk_threshold:
        return "stealth"
    if (
        policy.threat_perception
        and policy.sound_scent_memory
        and policy.stealth_action
        and scenario.routine_tracking > 0.50
        and tick % 22 == 0
        and risk_estimate > policy.risk_threshold * 0.75
    ):
        return "change_route"
    return "work"


def add_trace(
    trace: List[Dict[str, object]],
    tick: int,
    action: str,
    progress: float,
    energy: float,
    injury: float,
    detection: float,
    fear: float,
    noise: float,
    scent: float,
    shelter: float,
    support: float,
    attacks: int,
    notes: List[str],
) -> None:
    trace.append(
        {
            "tick": tick,
            "action": action,
            "progress": round(progress, 3),
            "energy": round(energy, 3),
            "injury": round(injury, 3),
            "detection_risk": round(detection, 3),
            "fear_state": round(fear, 3),
            "noise_level": round(noise, 3),
            "scent_trace": round(scent, 3),
            "shelter_security": round(shelter, 3),
            "social_support": round(support, 3),
            "attacks": attacks,
            "notes": list(notes[-3:]),
        }
    )


def simulate_episode(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episode: int,
    cfg: ThreatConfig,
    phase: str,
    collect_trace: bool = False,
) -> Tuple[EpisodeResult, List[Dict[str, object]]]:
    effective = condition_policy(policy, condition)
    rng = random.Random(scenario_seed(cfg, scenario, policy, condition, episode, phase))

    vulnerability = clamp(scenario.initial_vulnerability + rng.uniform(-0.020, 0.020), 0.0, 1.0)
    energy = clamp(0.96 - vulnerability * 0.08 + rng.uniform(-0.015, 0.015), 0.0, 1.0)
    injury = 0.0
    progress = 0.0
    detection = 0.0
    fear = 0.0
    noise = clamp(0.24 + scenario.sound_tracking * 0.18 + rng.uniform(-0.020, 0.020), 0.0, 1.0)
    scent = clamp(0.28 + scenario.scent_tracking * 0.18 + vulnerability * 0.18 + rng.uniform(-0.020, 0.020), 0.0, 1.0)
    predictability = clamp(0.34 + scenario.routine_tracking * 0.34, 0.0, 1.0)
    shelter_security = 0.18
    social_support = 0.0
    alarm_ready = False
    collapsed = False
    notes: List[str] = []

    attacks = 0
    near_misses = 0
    stealth_actions = 0
    shelter_actions = 0
    alarm_actions = 0
    social_warning_actions = 0
    route_changes = 0
    continuity_resets = 0
    threat_misses = 0
    trace_frames: List[Dict[str, object]] = []

    for tick in range(cfg.ticks):
        action = "work"
        if scenario.restore_tick == tick and not effective.continuity_memory:
            detection = clamp(detection + 0.28, 0.0, 1.6)
            fear = 0.16
            alarm_ready = False
            shelter_security = max(0.08, shelter_security - 0.22)
            social_support = max(0.0, social_support - 0.28)
            predictability = clamp(predictability + 0.28, 0.0, 1.0)
            continuity_resets += 1
            threat_misses += 1
            notes.append("restore erased threat pattern")
            action = "restore_reset"

        risk_estimate = estimate_risk(
            scenario,
            effective,
            injury,
            vulnerability,
            noise,
            scent,
            predictability,
            alarm_ready,
            shelter_security,
            social_support,
        )
        if not collapsed and action != "restore_reset":
            action = choose_action(
                scenario,
                effective,
                risk_estimate,
                alarm_ready,
                shelter_security,
                social_support,
                tick,
            )

        if collapsed:
            action = "collapsed"
        elif action == "warn_group":
            social_warning_actions += 1
            social_support = clamp(social_support + 0.52 + effective.group_bias * 0.18, 0.0, 1.0)
            energy = clamp(energy - 0.016, 0.0, 1.0)
            progress -= 0.18
            notes.append("group warning raised defense")
        elif action == "set_alarm":
            alarm_actions += 1
            alarm_ready = True
            energy = clamp(energy - 0.012, 0.0, 1.0)
            progress -= 0.16
            detection = clamp(detection - 0.035, 0.0, 1.6)
            notes.append("alarm reduced surprise")
        elif action == "seek_shelter":
            shelter_actions += 1
            shelter_security = clamp(shelter_security + 0.34 + effective.shelter_bias * 0.12, 0.0, 1.0)
            noise = clamp(noise - 0.040, 0.0, 1.0)
            scent = clamp(scent - 0.026, 0.0, 1.0)
            progress -= 0.30
            notes.append("shelter lowered exposure")
        elif action == "stealth":
            stealth_actions += 1
            noise = clamp(noise - 0.058 - effective.stealth_bias * 0.018, 0.0, 1.0)
            scent = clamp(scent - 0.020 if effective.sound_scent_memory else scent + 0.024, 0.0, 1.0)
            predictability = clamp(predictability - 0.018, 0.0, 1.0)
            progress += scenario.work_rate * 0.28
            energy = clamp(energy - 0.004, 0.0, 1.0)
            notes.append("stealth traded speed for lower tracking")
        elif action == "change_route":
            route_changes += 1
            predictability = clamp(predictability - 0.20, 0.0, 1.0)
            noise = clamp(noise + 0.010, 0.0, 1.0)
            progress -= 0.20
            notes.append("route changed to break routine")
        elif action == "work":
            capability = clamp(
                0.88
                + energy * 0.08
                - injury * 0.50
                - detection * 0.16
                - fear * 0.08,
                0.05,
                1.05,
            )
            progress += scenario.work_rate * capability
            noise = clamp(noise + 0.006 + scenario.sound_tracking * 0.003, 0.0, 1.0)
            scent = clamp(scent + 0.004 + scenario.scent_tracking * 0.004 + injury * 0.004, 0.0, 1.0)
            predictability = clamp(predictability + scenario.routine_tracking * 0.004, 0.0, 1.0)

        if effective.sound_scent_memory:
            noise = clamp(noise - 0.006, 0.0, 1.0)
            scent = clamp(scent - 0.007, 0.0, 1.0)
        if effective.self_vulnerability_state and vulnerability + injury > 0.46:
            noise = clamp(noise - 0.004, 0.0, 1.0)
            scent = clamp(scent - 0.004, 0.0, 1.0)
            fear = clamp(fear + 0.006, 0.0, 1.0)

        trace_factor = 0.72 if effective.sound_scent_memory else 1.28
        actual_tracked = (
            scenario.sound_tracking * noise * trace_factor
            + scenario.scent_tracking * scent * trace_factor
            + scenario.weakness_tracking * (vulnerability + injury)
            + scenario.routine_tracking * predictability
            + scenario.night_factor * 0.22
        )
        if scenario.expected_alarm and not alarm_ready:
            actual_tracked += 0.18
        if scenario.expected_stealth and not effective.stealth_action:
            actual_tracked += 0.22
        if scenario.expected_shelter and shelter_security < 0.50:
            actual_tracked += 0.18
        if scenario.expected_social_warning and social_support < 0.30:
            actual_tracked += 0.34
        mitigation = (
            (0.22 if alarm_ready else 0.0)
            + shelter_security * 0.28
            + social_support * 0.30
            + (0.12 if action == "stealth" else 0.0)
            + (0.10 if action == "change_route" else 0.0)
        )
        detection = clamp(
            detection
            + scenario.threat_intensity * max(0.0, actual_tracked - mitigation) * 0.020
            - (0.012 if action in {"stealth", "seek_shelter", "set_alarm", "warn_group"} else 0.002),
            0.0,
            1.6,
        )
        fear = clamp(fear * 0.985 + risk_estimate * 0.030 + detection * 0.010, 0.0, 1.0)

        attack_threshold = 0.46 + (0.08 if alarm_ready else 0.0) + shelter_security * 0.08 + social_support * 0.06
        if scenario.threat_intensity > 0 and detection > attack_threshold and tick % 13 == 0:
            near_misses += 1
            if detection + rng.uniform(-0.08, 0.08) > attack_threshold + 0.11:
                severity = clamp(
                    0.16
                    + scenario.threat_intensity * 0.13
                    + scenario.weakness_tracking * (vulnerability + injury) * 0.06
                    - shelter_security * 0.08
                    - social_support * 0.08
                    - (0.05 if alarm_ready else 0.0),
                    0.04,
                    0.36,
                )
                attacks += 1
                injury = clamp(injury + severity, 0.0, 1.0)
                energy = clamp(energy - severity * 0.42, 0.0, 1.0)
                progress -= severity * 10.0
                detection = clamp(detection - 0.16, 0.0, 1.6)
                alarm_ready = False if rng.random() < 0.22 else alarm_ready
                notes.append("tracker attack caused injury")
            else:
                detection = clamp(detection - 0.07, 0.0, 1.6)
                notes.append("near miss")

        if scenario.threat_intensity > 0 and risk_estimate < 0.20 and detection > 0.55 and not effective.threat_perception:
            threat_misses += 1 if tick % 11 == 0 else 0
        if scenario.expected_sound_scent and not effective.sound_scent_memory and (noise + scent) > 1.05:
            threat_misses += 1 if tick % 13 == 0 else 0
        if scenario.expected_self_vulnerability and not effective.self_vulnerability_state and vulnerability + injury > 0.55:
            threat_misses += 1 if tick % 13 == 0 else 0

        energy = clamp(energy - 0.0012 - injury * 0.0018 - fear * 0.0008, 0.0, 1.0)
        if injury >= 0.92 or energy <= 0.04:
            collapsed = True

        if collect_trace and (tick % 5 == 0 or tick == cfg.ticks - 1 or action != "work"):
            add_trace(
                trace_frames,
                tick,
                action,
                progress,
                energy,
                injury,
                detection,
                fear,
                noise,
                scent,
                shelter_security,
                social_support,
                attacks,
                notes,
            )

    task_success = progress >= scenario.required_progress and not collapsed
    survival = 1.0 if not collapsed and injury < 0.82 and energy > 0.06 else 0.0

    reward = progress
    reward += 34.0 if task_success else -20.0
    reward += 38.0 if survival else -108.0
    reward += energy * 18.0
    reward -= injury * 128.0
    reward -= detection * 58.0
    reward -= fear * 18.0
    reward -= attacks * 26.0
    reward -= near_misses * 2.4
    reward -= threat_misses * 0.8
    reward += shelter_security * (18.0 if scenario.expected_shelter else 2.0)
    reward += social_support * (22.0 if scenario.expected_social_warning else 1.0)
    reward += (1.0 if alarm_ready else 0.0) * (8.0 if scenario.expected_alarm else 0.5)
    reward -= stealth_actions * 0.18
    reward -= shelter_actions * 0.28
    reward -= alarm_actions * 0.22
    reward -= social_warning_actions * 0.26
    reward -= route_changes * 0.18
    reward -= feature_overhead(effective)
    if scenario.expected_continuity and continuity_resets:
        reward -= 42.0

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
        injury=injury,
        detection_risk=detection,
        fear_state=fear,
        noise_level=noise,
        scent_trace=scent,
        shelter_security=shelter_security,
        social_support=social_support,
        attacks=attacks,
        near_misses=near_misses,
        stealth_actions=stealth_actions,
        shelter_actions=shelter_actions,
        alarm_actions=alarm_actions,
        social_warning_actions=social_warning_actions,
        route_changes=route_changes,
        continuity_resets=continuity_resets,
        threat_misses=threat_misses,
    )
    return result, trace_frames


def evaluate_policy(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episodes: int,
    cfg: ThreatConfig,
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
                    mean_injury=mean(row.injury for row in subset),
                    mean_detection_risk=mean(row.detection_risk for row in subset),
                    mean_fear_state=mean(row.fear_state for row in subset),
                    mean_noise_level=mean(row.noise_level for row in subset),
                    mean_scent_trace=mean(row.scent_trace for row in subset),
                    mean_shelter_security=mean(row.shelter_security for row in subset),
                    mean_social_support=mean(row.social_support for row in subset),
                    mean_attacks=mean(row.attacks for row in subset),
                    mean_near_misses=mean(row.near_misses for row in subset),
                    mean_stealth_actions=mean(row.stealth_actions for row in subset),
                    mean_shelter_actions=mean(row.shelter_actions for row in subset),
                    mean_alarm_actions=mean(row.alarm_actions for row in subset),
                    mean_social_warning_actions=mean(row.social_warning_actions for row in subset),
                    mean_route_changes=mean(row.route_changes for row in subset),
                    mean_continuity_resets=mean(row.continuity_resets for row in subset),
                    mean_threat_misses=mean(row.threat_misses for row in subset),
                )
            )
    return rows


def select_policies(cfg: ThreatConfig, policies: Sequence[Policy]) -> Tuple[Dict[int, Policy], List[PolicySelectionRow]]:
    selected: Dict[int, Policy] = {}
    rows: List[PolicySelectionRow] = []
    baseline = next(policy for policy in policies if policy.name == "no_threat_baseline")
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
                selected_uses_threat_perception=selected_policy.threat_perception,
                selected_uses_self_vulnerability_state=selected_policy.self_vulnerability_state,
                selected_uses_sound_scent_memory=selected_policy.sound_scent_memory,
                selected_uses_stealth_action=selected_policy.stealth_action,
                selected_uses_shelter_memory=selected_policy.shelter_memory,
                selected_uses_tool_alarm=selected_policy.tool_alarm,
                selected_uses_social_warning=selected_policy.social_warning,
                selected_uses_continuity=selected_policy.continuity_memory,
                train_reward=selected_reward,
                no_threat_train_reward=baseline_reward,
                train_gain_over_no_threat=selected_reward - baseline_reward,
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
        no_perception = lookup[(scenario.index, "no_threat_perception")]
        no_self = lookup[(scenario.index, "no_self_vulnerability_state")]
        no_sound = lookup[(scenario.index, "no_sound_scent_memory")]
        no_stealth = lookup[(scenario.index, "no_stealth_action")]
        no_shelter = lookup[(scenario.index, "no_shelter_access")]
        no_alarm = lookup[(scenario.index, "no_tool_alarm")]
        no_social = lookup[(scenario.index, "no_social_warning")]
        no_continuity = lookup[(scenario.index, "no_continuity")]
        reactive = lookup[(scenario.index, "reactive_panic_only")]
        omniscient = lookup[(scenario.index, "omniscient_threat_control")]

        perception_loss = full.mean_reward - no_perception.mean_reward
        self_loss = full.mean_reward - no_self.mean_reward
        sound_loss = full.mean_reward - no_sound.mean_reward
        stealth_loss = full.mean_reward - no_stealth.mean_reward
        shelter_loss = full.mean_reward - no_shelter.mean_reward
        alarm_loss = full.mean_reward - no_alarm.mean_reward
        social_loss = full.mean_reward - no_social.mean_reward
        continuity_loss = full.mean_reward - no_continuity.mean_reward
        reactive_loss = full.mean_reward - reactive.mean_reward

        if scenario.index == 0:
            supports = (
                selected[scenario.index].name == "no_threat_baseline"
                and abs(perception_loss) < 4.0
                and abs(stealth_loss) < 4.0
                and full.mean_attacks < 0.2
                and full.mean_stealth_actions < 0.5
            )
            verdict = "threat_machinery_rejected_in_safe_control"
        elif scenario.index == 1:
            supports = (
                perception_loss > 24.0
                and sound_loss > 22.0
                and stealth_loss > 18.0
                and alarm_loss > 12.0
                and full.mean_attacks < no_sound.mean_attacks
            )
            verdict = "sound_tracking_predator_stealth_alarm_pressure"
        elif scenario.index == 2:
            supports = (
                perception_loss > 24.0
                and self_loss > 20.0
                and sound_loss > 20.0
                and shelter_loss > 18.0
                and full.mean_injury < no_self.mean_injury
            )
            verdict = "scent_weakness_tracker_self_shelter_pressure"
        elif scenario.index == 3:
            supports = (
                perception_loss > 20.0
                and sound_loss > 18.0
                and stealth_loss > 18.0
                and alarm_loss > 12.0
                and full.mean_route_changes > no_perception.mean_route_changes
            )
            verdict = "routine_ambush_route_stealth_pressure"
        elif scenario.index == 4:
            supports = (
                social_loss > 22.0
                and shelter_loss > 18.0
                and self_loss > 18.0
                and alarm_loss > 12.0
                and full.mean_social_warning_actions > 0.7
            )
            verdict = "social_warning_group_defense_pressure"
        else:
            supports = (
                continuity_loss > 24.0
                and perception_loss > 20.0
                and self_loss > 18.0
                and sound_loss > 18.0
                and no_continuity.mean_continuity_resets > 0.5
                and full.mean_attacks < no_continuity.mean_attacks
            )
            verdict = "restore_threat_continuity_pressure"

        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                expected_pressure=scenario.pressure,
                selected_policy=selected[scenario.index].name,
                selected_reward=full.mean_reward,
                no_threat_perception_reward=no_perception.mean_reward,
                no_self_vulnerability_reward=no_self.mean_reward,
                no_sound_scent_memory_reward=no_sound.mean_reward,
                no_stealth_action_reward=no_stealth.mean_reward,
                no_shelter_access_reward=no_shelter.mean_reward,
                no_tool_alarm_reward=no_alarm.mean_reward,
                no_social_warning_reward=no_social.mean_reward,
                no_continuity_reward=no_continuity.mean_reward,
                reactive_panic_only_reward=reactive.mean_reward,
                omniscient_threat_control_reward=omniscient.mean_reward,
                no_threat_perception_loss=perception_loss,
                no_self_vulnerability_loss=self_loss,
                no_sound_scent_memory_loss=sound_loss,
                no_stealth_action_loss=stealth_loss,
                no_shelter_access_loss=shelter_loss,
                no_tool_alarm_loss=alarm_loss,
                no_social_warning_loss=social_loss,
                no_continuity_loss=continuity_loss,
                reactive_panic_only_loss=reactive_loss,
                selected_attacks=full.mean_attacks,
                selected_stealth_actions=full.mean_stealth_actions,
                selected_shelter_actions=full.mean_shelter_actions,
                selected_alarm_actions=full.mean_alarm_actions,
                selected_social_warnings=full.mean_social_warning_actions,
                supports_predator_threat_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def build_trace(cfg: ThreatConfig, selected: Dict[int, Policy]) -> Dict[str, object]:
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
            "mean_injury": mean(row.injury for row in rows),
            "mean_detection_risk": mean(row.detection_risk for row in rows),
            "mean_attacks": mean(row.attacks for row in rows),
            "mean_shelter_security": mean(row.shelter_security for row in rows),
            "mean_social_support": mean(row.social_support for row in rows),
        }
    return {
        "scenario": asdict(scenario),
        "policy": asdict(policy),
        "episode_result": asdict(result),
        "condition_outcomes": condition_outcomes,
        "frames": frames,
        "trace_note": "Threats, fear-like state, stealth, alarms, shelter, social warning, and continuity are abstract control variables.",
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
    cfg: ThreatConfig,
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
        "artifact_note": "Predator/threat agents are control variables, not animal simulation.",
    }
    return eval_rows, selection_rows, summary_rows, verdict_rows, {"results": results, "trace": trace}


def print_table(verdicts: Sequence[VerdictRow]) -> None:
    headers = [
        "scenario",
        "policy",
        "perception_loss",
        "self_loss",
        "sound_scent_loss",
        "stealth_loss",
        "shelter_loss",
        "alarm_loss",
        "social_loss",
        "continuity_loss",
        "supports",
    ]
    rows = [
        [
            row.scenario_name,
            row.selected_policy,
            f"{row.no_threat_perception_loss:.3f}",
            f"{row.no_self_vulnerability_loss:.3f}",
            f"{row.no_sound_scent_memory_loss:.3f}",
            f"{row.no_stealth_action_loss:.3f}",
            f"{row.no_shelter_access_loss:.3f}",
            f"{row.no_tool_alarm_loss:.3f}",
            f"{row.no_social_warning_loss:.3f}",
            f"{row.no_continuity_loss:.3f}",
            str(row.supports_predator_threat_precursor),
        ]
        for row in verdicts
    ]
    widths = [max(len(header), *(len(row[index]) for row in rows)) for index, header in enumerate(headers)]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> ThreatConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-episodes", type=int, default=ThreatConfig.train_episodes)
    parser.add_argument("--eval-episodes", type=int, default=ThreatConfig.eval_episodes)
    parser.add_argument("--ticks", type=int, default=ThreatConfig.ticks)
    parser.add_argument("--seed", type=int, default=ThreatConfig.seed)
    parser.add_argument("--candidate-count", type=int, default=ThreatConfig.candidate_count)
    parser.add_argument("--trace-scenario", type=int, default=ThreatConfig.trace_scenario)
    parser.add_argument("--trace-episode", type=int, default=ThreatConfig.trace_episode)
    args = parser.parse_args()
    if args.train_episodes < 24:
        raise SystemExit("--train-episodes must be at least 24")
    if args.eval_episodes < 24:
        raise SystemExit("--eval-episodes must be at least 24")
    if args.candidate_count < len(SEEDED_POLICIES):
        raise SystemExit(f"--candidate-count must be at least {len(SEEDED_POLICIES)}")
    if args.trace_scenario < 0 or args.trace_scenario >= len(SCENARIOS):
        raise SystemExit("--trace-scenario out of range")
    return ThreatConfig(
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

    eval_path = ARTIFACT_DIR / "ssrm_3d_predator_threat_agents_eval.csv"
    selection_path = ARTIFACT_DIR / "ssrm_3d_predator_threat_agents_policy_selection.csv"
    summary_path = ARTIFACT_DIR / "ssrm_3d_predator_threat_agents_summary.csv"
    verdict_path = ARTIFACT_DIR / "ssrm_3d_predator_threat_agents_verdict.csv"
    results_path = ARTIFACT_DIR / "ssrm_3d_predator_threat_agents_results.json"
    trace_path = ARTIFACT_DIR / "ssrm_3d_predator_threat_agents_trace.json"
    results_js_path = ARTIFACT_DIR / "ssrm_3d_predator_threat_agents_results.js"
    trace_js_path = ARTIFACT_DIR / "ssrm_3d_predator_threat_agents_trace.js"

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
    write_js(results_js_path, "SSRM_3D_PREDATOR_THREAT_AGENTS_RESULTS", payload["results"])
    write_js(trace_js_path, "SSRM_3D_PREDATOR_THREAT_AGENTS_TRACE", payload["trace"])

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
    if not all(row.supports_predator_threat_precursor for row in verdict_rows):
        print("predator/threat precursor not supported by all verdict rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
