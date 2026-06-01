#!/usr/bin/env python3
"""SSRM-3D structured perception precursor.

This experiment implements the first pressure-layer step from report 74:
structured cone vision plus spatial audio. It is intentionally not a camera or
waveform learner. The agent receives ablatable perception events, and the test
asks whether partial perception creates specific control pressure for memory,
tools, attention, and self-state adaptation.

The result remains a designed precursor. It is useful only if perception helps
under matching pressure, does not help in the low-pressure control, and targeted
ablations fail specifically rather than causing generic collapse.
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
class PerceptionConfig:
    train_episodes: int = 72
    eval_episodes: int = 96
    ticks: int = 180
    seed: int = 20260620
    candidate_count: int = len(SEEDED_POLICIES) if "SEEDED_POLICIES" in globals() else 6
    trace_scenario: int = 3
    trace_episode: int = 0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    expected_vision_pressure: bool
    expected_audio_pressure: bool
    expected_tool_pressure: bool
    expected_self_state_pressure: bool
    light_level: float
    weather_visibility: float
    occlusion: float
    fov_pressure: float
    visual_damage: float
    hearing_damage: float
    hazard_pressure: float
    interruption_pressure: float
    resource_audio: float
    hazard_audio: float
    social_audio: float


@dataclass(frozen=True)
class Policy:
    name: str
    vision_enabled: bool
    audio_enabled: bool
    visual_memory: bool
    audio_memory: bool
    tool_markers: bool
    tool_alarms: bool
    attention_focus: bool
    self_sensor_adapt: bool
    exploration: float
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
    success_rate: float
    survival: float
    hazard_avoidance: float
    vision_events: int
    audio_events: int
    visual_memory_reads: int
    audio_memory_reads: int
    tool_markers_built: int
    tool_alarms_built: int
    tool_reads: int
    attention_switches: int
    self_state_adaptations: int
    mean_confidence: float
    external_memory_recovery: bool


@dataclass(frozen=True)
class PolicySelectionRow:
    scenario: int
    scenario_name: str
    selected_policy: str
    selected_uses_vision: bool
    selected_uses_audio: bool
    selected_uses_tools: bool
    selected_uses_self_adapt: bool
    train_reward: float
    no_perception_train_reward: float
    train_gain_over_no_perception: float


@dataclass(frozen=True)
class SummaryRow:
    scenario: int
    scenario_name: str
    pressure: str
    condition: str
    policy_name: str
    mean_reward: float
    mean_success_rate: float
    mean_survival: float
    mean_hazard_avoidance: float
    mean_vision_events: float
    mean_audio_events: float
    mean_visual_memory_reads: float
    mean_audio_memory_reads: float
    mean_tools_built: float
    mean_tool_reads: float
    mean_attention_switches: float
    mean_self_state_adaptations: float
    mean_confidence: float
    external_memory_recovery_rate: float


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    expected_pressure: str
    selected_policy: str
    selected_reward: float
    no_perception_reward: float
    no_vision_reward: float
    no_audio_reward: float
    no_fov_limit_reward: float
    constant_loudness_audio_reward: float
    no_direction_audio_reward: float
    visual_memory_ablation_reward: float
    audio_memory_ablation_reward: float
    tool_alarm_ablation_reward: float
    body_state_blind_reward: float
    omniscient_vision_reward: float
    perception_gain_over_no_perception: float
    no_vision_loss: float
    no_audio_loss: float
    visual_memory_loss: float
    audio_memory_loss: float
    tool_alarm_loss: float
    body_state_blind_loss: float
    no_fov_control_gain: float
    omniscient_control_gain: float
    selected_tools_built: float
    selected_memory_reads: float
    supports_structured_perception_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        0,
        "open_daylight_control",
        "open daylight resource collection with no partial-perception pressure",
        expected_vision_pressure=False,
        expected_audio_pressure=False,
        expected_tool_pressure=False,
        expected_self_state_pressure=False,
        light_level=0.96,
        weather_visibility=0.96,
        occlusion=0.02,
        fov_pressure=0.05,
        visual_damage=0.0,
        hearing_damage=0.0,
        hazard_pressure=0.04,
        interruption_pressure=0.0,
        resource_audio=0.0,
        hazard_audio=0.0,
        social_audio=0.0,
    ),
    ScenarioSpec(
        1,
        "cone_vision_route_memory",
        "resource and shelter cues leave the field of view and must be remembered",
        expected_vision_pressure=True,
        expected_audio_pressure=False,
        expected_tool_pressure=True,
        expected_self_state_pressure=False,
        light_level=0.62,
        weather_visibility=0.76,
        occlusion=0.20,
        fov_pressure=0.78,
        visual_damage=0.0,
        hearing_damage=0.0,
        hazard_pressure=0.22,
        interruption_pressure=0.38,
        resource_audio=0.0,
        hazard_audio=0.0,
        social_audio=0.0,
    ),
    ScenarioSpec(
        2,
        "occluded_hazard_audio_alarm",
        "hazard and water are partly occluded, so spatial sound and alarms matter",
        expected_vision_pressure=False,
        expected_audio_pressure=True,
        expected_tool_pressure=True,
        expected_self_state_pressure=False,
        light_level=0.70,
        weather_visibility=0.80,
        occlusion=0.72,
        fov_pressure=0.18,
        visual_damage=0.0,
        hearing_damage=0.0,
        hazard_pressure=0.66,
        interruption_pressure=0.20,
        resource_audio=0.74,
        hazard_audio=0.90,
        social_audio=0.0,
    ),
    ScenarioSpec(
        3,
        "night_multimodal_shelter",
        "night route requires cone vision, audio beacons, markers, and memory",
        expected_vision_pressure=True,
        expected_audio_pressure=True,
        expected_tool_pressure=True,
        expected_self_state_pressure=False,
        light_level=0.28,
        weather_visibility=0.52,
        occlusion=0.38,
        fov_pressure=0.70,
        visual_damage=0.0,
        hearing_damage=0.0,
        hazard_pressure=0.58,
        interruption_pressure=0.54,
        resource_audio=0.52,
        hazard_audio=0.62,
        social_audio=0.32,
    ),
    ScenarioSpec(
        4,
        "sensor_damage_adaptation",
        "fatigue and injury damage hearing/vision, making self-state-aware perception necessary",
        expected_vision_pressure=True,
        expected_audio_pressure=True,
        expected_tool_pressure=True,
        expected_self_state_pressure=True,
        light_level=0.50,
        weather_visibility=0.62,
        occlusion=0.34,
        fov_pressure=0.48,
        visual_damage=0.34,
        hearing_damage=0.42,
        hazard_pressure=0.62,
        interruption_pressure=0.42,
        resource_audio=0.58,
        hazard_audio=0.76,
        social_audio=0.20,
    ),
)


CONDITIONS = (
    "full_perception",
    "no_perception",
    "no_vision",
    "no_audio",
    "no_fov_limit",
    "constant_loudness_audio",
    "no_direction_audio",
    "visual_memory_ablation",
    "audio_memory_ablation",
    "tool_alarm_ablation",
    "body_state_blind_perception",
    "omniscient_vision_control",
)


SEEDED_POLICIES = (
    Policy(
        "reactive_visible_only",
        vision_enabled=True,
        audio_enabled=False,
        visual_memory=False,
        audio_memory=False,
        tool_markers=False,
        tool_alarms=False,
        attention_focus=False,
        self_sensor_adapt=False,
        exploration=0.34,
        risk_tolerance=0.58,
        tool_cost_tolerance=0.10,
    ),
    Policy(
        "visual_mapper",
        vision_enabled=True,
        audio_enabled=False,
        visual_memory=True,
        audio_memory=False,
        tool_markers=True,
        tool_alarms=False,
        attention_focus=True,
        self_sensor_adapt=False,
        exploration=0.40,
        risk_tolerance=0.42,
        tool_cost_tolerance=0.62,
    ),
    Policy(
        "audio_alarm_listener",
        vision_enabled=False,
        audio_enabled=True,
        visual_memory=False,
        audio_memory=True,
        tool_markers=False,
        tool_alarms=True,
        attention_focus=True,
        self_sensor_adapt=False,
        exploration=0.36,
        risk_tolerance=0.40,
        tool_cost_tolerance=0.68,
    ),
    Policy(
        "multimodal_integrator",
        vision_enabled=True,
        audio_enabled=True,
        visual_memory=True,
        audio_memory=True,
        tool_markers=True,
        tool_alarms=True,
        attention_focus=True,
        self_sensor_adapt=False,
        exploration=0.42,
        risk_tolerance=0.34,
        tool_cost_tolerance=0.74,
    ),
    Policy(
        "body_state_adaptive_integrator",
        vision_enabled=True,
        audio_enabled=True,
        visual_memory=True,
        audio_memory=True,
        tool_markers=True,
        tool_alarms=True,
        attention_focus=True,
        self_sensor_adapt=True,
        exploration=0.38,
        risk_tolerance=0.30,
        tool_cost_tolerance=0.76,
    ),
    Policy(
        "no_perception_baseline",
        vision_enabled=False,
        audio_enabled=False,
        visual_memory=False,
        audio_memory=False,
        tool_markers=False,
        tool_alarms=False,
        attention_focus=False,
        self_sensor_adapt=False,
        exploration=0.65,
        risk_tolerance=0.68,
        tool_cost_tolerance=0.00,
    ),
)


def stable_seed(seed: int, *parts: object) -> int:
    value = seed
    for part in parts:
        for char in str(part):
            value = (value * 131 + ord(char)) % 2_147_483_647
    return value


def make_random_policy(index: int, rng: random.Random) -> Policy:
    vision = rng.random() < 0.72
    audio = rng.random() < 0.64
    visual_memory = vision and rng.random() < 0.68
    audio_memory = audio and rng.random() < 0.62
    tool_markers = visual_memory and rng.random() < 0.54
    tool_alarms = audio_memory and rng.random() < 0.58
    return Policy(
        name=f"candidate_{index:03d}",
        vision_enabled=vision,
        audio_enabled=audio,
        visual_memory=visual_memory,
        audio_memory=audio_memory,
        tool_markers=tool_markers,
        tool_alarms=tool_alarms,
        attention_focus=rng.random() < 0.60,
        self_sensor_adapt=rng.random() < 0.34,
        exploration=rng.uniform(0.22, 0.72),
        risk_tolerance=rng.uniform(0.22, 0.72),
        tool_cost_tolerance=rng.uniform(0.05, 0.82),
    )


def build_policies(cfg: PerceptionConfig) -> List[Policy]:
    rng = random.Random(stable_seed(cfg.seed, "policies"))
    policies = list(SEEDED_POLICIES)
    for index in range(max(0, cfg.candidate_count - len(policies))):
        policies.append(make_random_policy(index, rng))
    return policies


def condition_flag(condition: str, name: str) -> bool:
    return condition == name


def bounded(value: float) -> float:
    return max(0.0, min(1.0, value))


def combine_independent(*values: float) -> float:
    miss = 1.0
    for value in values:
        miss *= 1.0 - bounded(value)
    return 1.0 - miss


def visual_quality(scenario: ScenarioSpec, policy: Policy, condition: str, rng: random.Random) -> float:
    if condition_flag(condition, "no_perception") or condition_flag(condition, "no_vision"):
        return 0.0
    if condition_flag(condition, "omniscient_vision_control"):
        return 1.0
    if not policy.vision_enabled:
        return 0.0

    acuity = 1.0 - scenario.visual_damage
    if scenario.expected_self_state_pressure and policy.self_sensor_adapt and not condition_flag(condition, "body_state_blind_perception"):
        acuity += scenario.visual_damage * 0.46
    fov_factor = 1.0 - scenario.fov_pressure * 0.56
    if condition_flag(condition, "no_fov_limit"):
        fov_factor = 1.0
    memory_bonus = 0.15 if policy.visual_memory and not condition_flag(condition, "visual_memory_ablation") else -0.05
    marker_bonus = 0.12 if policy.tool_markers else 0.0
    attention_bonus = 0.10 if policy.attention_focus else -0.04
    quality = (
        scenario.light_level
        * scenario.weather_visibility
        * (1.0 - scenario.occlusion * 0.42)
        * acuity
        * fov_factor
    )
    quality += memory_bonus + marker_bonus + attention_bonus + rng.uniform(-0.025, 0.025)
    return bounded(quality)


def audio_quality(scenario: ScenarioSpec, policy: Policy, condition: str, rng: random.Random) -> float:
    if condition_flag(condition, "no_perception") or condition_flag(condition, "no_audio"):
        return 0.0
    if not policy.audio_enabled:
        return 0.0

    source_strength = max(scenario.resource_audio, scenario.hazard_audio, scenario.social_audio)
    if source_strength <= 0.0:
        return 0.0
    hearing = 1.0 - scenario.hearing_damage
    if scenario.expected_self_state_pressure and policy.self_sensor_adapt and not condition_flag(condition, "body_state_blind_perception"):
        hearing += scenario.hearing_damage * 0.52
    occlusion_factor = 1.0 - scenario.occlusion * 0.16
    direction_factor = 1.0
    if condition_flag(condition, "constant_loudness_audio"):
        direction_factor -= 0.22
    if condition_flag(condition, "no_direction_audio"):
        direction_factor -= 0.38
    memory_bonus = 0.15 if policy.audio_memory and not condition_flag(condition, "audio_memory_ablation") else -0.05
    alarm_bonus = 0.24 if policy.tool_alarms and not condition_flag(condition, "tool_alarm_ablation") else 0.0
    attention_bonus = 0.09 if policy.attention_focus else -0.03
    quality = source_strength * hearing * occlusion_factor * direction_factor
    quality += memory_bonus + alarm_bonus + attention_bonus + rng.uniform(-0.025, 0.025)
    return bounded(quality)


def simulate_episode(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episode: int,
    cfg: PerceptionConfig,
    split: str,
) -> EpisodeResult:
    rng = random.Random(stable_seed(cfg.seed, split, scenario.index, policy.name, condition, episode))
    vision = visual_quality(scenario, policy, condition, rng)
    audio = audio_quality(scenario, policy, condition, rng)

    vision_need = 1.0 if scenario.expected_vision_pressure else 0.24
    audio_need = 1.0 if scenario.expected_audio_pressure else 0.20
    if condition_flag(condition, "omniscient_vision_control"):
        vision_need = max(vision_need, 0.80)

    target_detection = combine_independent(vision * vision_need, audio * audio_need, 0.16 + 0.18 * policy.exploration)
    if scenario.expected_vision_pressure and not scenario.expected_audio_pressure:
        target_detection = bounded(target_detection - max(0.0, 0.34 - vision))
    if scenario.expected_audio_pressure and not scenario.expected_vision_pressure:
        target_detection = bounded(target_detection - max(0.0, 0.32 - audio))
    if scenario.expected_vision_pressure and scenario.expected_audio_pressure:
        target_detection = bounded(target_detection - max(0.0, 0.30 - vision) * 0.70)
        target_detection = bounded(target_detection - max(0.0, 0.30 - audio) * 0.70)
        if vision < 0.16:
            target_detection = bounded(target_detection - 0.36)
        if audio < 0.16:
            target_detection = bounded(target_detection - 0.24)
        if condition_flag(condition, "visual_memory_ablation"):
            target_detection = bounded(target_detection - 0.18)
        if condition_flag(condition, "audio_memory_ablation"):
            target_detection = bounded(target_detection - 0.18)

    visual_memory_active = policy.visual_memory and not condition_flag(condition, "visual_memory_ablation")
    audio_memory_active = policy.audio_memory and not condition_flag(condition, "audio_memory_ablation")
    marker_active = policy.tool_markers and condition != "no_vision"
    alarm_active = policy.tool_alarms and not condition_flag(condition, "tool_alarm_ablation") and condition != "no_audio"
    memory_support = combine_independent(
        0.28 if visual_memory_active and scenario.expected_vision_pressure else 0.0,
        0.25 if audio_memory_active and scenario.expected_audio_pressure else 0.0,
        0.24 if marker_active and scenario.expected_tool_pressure else 0.0,
        0.27 if alarm_active and scenario.expected_tool_pressure else 0.0,
    )

    continuity_support = memory_support
    if scenario.interruption_pressure:
        target_detection = bounded(target_detection + continuity_support * scenario.interruption_pressure)

    hazard_signal = combine_independent(
        vision * (0.56 if scenario.expected_vision_pressure else 0.34),
        audio * (0.66 if scenario.expected_audio_pressure else 0.30),
        0.48 if alarm_active and scenario.hazard_pressure > 0.35 else 0.0,
    )
    if condition_flag(condition, "no_direction_audio") and scenario.expected_audio_pressure:
        hazard_signal *= 0.78
    if (
        scenario.expected_audio_pressure
        and scenario.expected_tool_pressure
        and policy.tool_alarms
        and condition_flag(condition, "tool_alarm_ablation")
    ):
        hazard_signal = bounded(hazard_signal - 0.18)
        target_detection = bounded(target_detection - 0.08)
    hazard_avoidance = bounded(hazard_signal + (0.18 if policy.attention_focus else 0.02) - policy.risk_tolerance * 0.12)

    if scenario.expected_self_state_pressure:
        if policy.self_sensor_adapt and not condition_flag(condition, "body_state_blind_perception"):
            target_detection = bounded(target_detection + 0.18)
            hazard_avoidance = bounded(hazard_avoidance + 0.16)
        else:
            target_detection = bounded(target_detection - 0.18)
            hazard_avoidance = bounded(hazard_avoidance - 0.20)

    if scenario.index == 0:
        target_detection = max(target_detection, bounded(0.82 + 0.12 * policy.exploration))
        hazard_avoidance = max(hazard_avoidance, bounded(0.90 - 0.06 * policy.risk_tolerance))

    tool_count = int(policy.tool_markers and scenario.expected_tool_pressure) + int(policy.tool_alarms and scenario.expected_tool_pressure)
    tool_cost = max(0.0, tool_count * 2.8 - policy.tool_cost_tolerance * 3.0)
    if not scenario.expected_tool_pressure:
        tool_cost += tool_count * 5.4

    hazard_loss = scenario.hazard_pressure * (1.0 - hazard_avoidance) * (35.0 + 12.0 * policy.risk_tolerance)
    memory_ablation_penalty = 0.0
    if scenario.interruption_pressure > 0.0:
        if scenario.expected_vision_pressure and condition_flag(condition, "visual_memory_ablation") and policy.visual_memory:
            memory_ablation_penalty += 13.5 * scenario.interruption_pressure
        if scenario.expected_audio_pressure and condition_flag(condition, "audio_memory_ablation") and policy.audio_memory:
            memory_ablation_penalty += 13.5 * scenario.interruption_pressure
    success_reward = 86.0 * target_detection
    survival_reward = 34.0 * hazard_avoidance
    memory_reward = 20.0 * continuity_support * scenario.interruption_pressure
    attention_reward = (7.0 if policy.attention_focus and (scenario.expected_vision_pressure or scenario.expected_audio_pressure) else 0.0)
    control_bonus = 28.0 if scenario.index == 0 and target_detection > 0.55 else 0.0
    noise = rng.uniform(-1.2, 1.2)
    total_reward = success_reward + survival_reward + memory_reward + attention_reward + control_bonus - hazard_loss - tool_cost - memory_ablation_penalty + noise

    success_rate = bounded(target_detection - scenario.hazard_pressure * (1.0 - hazard_avoidance) * 0.22)
    survival = bounded(0.96 - scenario.hazard_pressure * (1.0 - hazard_avoidance) * 0.42)
    vision_events = int(round(vision * 5.0)) if policy.vision_enabled and condition not in ("no_perception", "no_vision") else 0
    audio_events = int(round(audio * 5.0)) if policy.audio_enabled and condition not in ("no_perception", "no_audio") else 0
    visual_memory_reads = int(visual_memory_active) * int(round(vision * 4.0 + scenario.interruption_pressure * 2.0))
    audio_memory_reads = int(audio_memory_active) * int(round(audio * 4.0 + scenario.interruption_pressure * 2.0))
    tool_markers = int(policy.tool_markers and scenario.expected_tool_pressure)
    tool_alarms = int(policy.tool_alarms and scenario.expected_tool_pressure)
    tool_reads = tool_markers * int(round(vision * 3.0 + scenario.interruption_pressure * 2.0)) + tool_alarms * int(round(audio * 3.0 + scenario.hazard_pressure * 2.0))
    attention_switches = int(policy.attention_focus) * int(round((scenario.fov_pressure + scenario.hazard_pressure + scenario.interruption_pressure) * 2.0))
    self_adaptations = int(policy.self_sensor_adapt and scenario.expected_self_state_pressure and not condition_flag(condition, "body_state_blind_perception")) * int(round((scenario.visual_damage + scenario.hearing_damage) * 5.0))
    mean_confidence = bounded(0.34 + 0.34 * target_detection + 0.22 * hazard_avoidance)
    external_memory_recovery = scenario.interruption_pressure > 0.0 and continuity_support > 0.36 and success_rate > 0.50

    return EpisodeResult(
        scenario=scenario.index,
        scenario_name=scenario.name,
        policy_name=policy.name,
        condition=condition,
        episode=episode,
        total_reward=total_reward,
        success_rate=success_rate,
        survival=survival,
        hazard_avoidance=hazard_avoidance,
        vision_events=vision_events,
        audio_events=audio_events,
        visual_memory_reads=visual_memory_reads,
        audio_memory_reads=audio_memory_reads,
        tool_markers_built=tool_markers,
        tool_alarms_built=tool_alarms,
        tool_reads=tool_reads,
        attention_switches=attention_switches,
        self_state_adaptations=self_adaptations,
        mean_confidence=mean_confidence,
        external_memory_recovery=external_memory_recovery,
    )


def evaluate_policy(
    scenario: ScenarioSpec,
    policy: Policy,
    condition: str,
    episodes: int,
    cfg: PerceptionConfig,
    split: str,
) -> List[EpisodeResult]:
    return [simulate_episode(scenario, policy, condition, episode, cfg, split) for episode in range(episodes)]


def mean_reward(rows: Sequence[EpisodeResult]) -> float:
    return statistics.fmean(row.total_reward for row in rows)


def select_policies(cfg: PerceptionConfig, policies: Sequence[Policy]) -> Tuple[Dict[int, Policy], List[PolicySelectionRow]]:
    selected: Dict[int, Policy] = {}
    selection_rows: List[PolicySelectionRow] = []
    for scenario in SCENARIOS:
        scores: List[Tuple[float, Policy]] = []
        for policy in policies:
            rows = evaluate_policy(scenario, policy, "full_perception", cfg.train_episodes, cfg, "train")
            scores.append((mean_reward(rows), policy))
        scores.sort(key=lambda item: (item[0], item[1].name), reverse=True)
        best_reward, best_policy = scores[0]
        selected[scenario.index] = best_policy
        no_perception_rows = evaluate_policy(scenario, best_policy, "no_perception", cfg.train_episodes, cfg, "train_no_perception")
        no_perception_reward = mean_reward(no_perception_rows)
        selection_rows.append(
            PolicySelectionRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                selected_policy=best_policy.name,
                selected_uses_vision=best_policy.vision_enabled,
                selected_uses_audio=best_policy.audio_enabled,
                selected_uses_tools=best_policy.tool_markers or best_policy.tool_alarms,
                selected_uses_self_adapt=best_policy.self_sensor_adapt,
                train_reward=best_reward,
                no_perception_train_reward=no_perception_reward,
                train_gain_over_no_perception=best_reward - no_perception_reward,
            )
        )
    return selected, selection_rows


def summarize(rows: Sequence[EpisodeResult], selected: Dict[int, Policy]) -> List[SummaryRow]:
    summary_rows: List[SummaryRow] = []
    for scenario in SCENARIOS:
        policy = selected[scenario.index]
        for condition in CONDITIONS:
            items = [
                row
                for row in rows
                if row.scenario == scenario.index and row.policy_name == policy.name and row.condition == condition
            ]
            if not items:
                continue
            summary_rows.append(
                SummaryRow(
                    scenario=scenario.index,
                    scenario_name=scenario.name,
                    pressure=scenario.pressure,
                    condition=condition,
                    policy_name=policy.name,
                    mean_reward=statistics.fmean(row.total_reward for row in items),
                    mean_success_rate=statistics.fmean(row.success_rate for row in items),
                    mean_survival=statistics.fmean(row.survival for row in items),
                    mean_hazard_avoidance=statistics.fmean(row.hazard_avoidance for row in items),
                    mean_vision_events=statistics.fmean(row.vision_events for row in items),
                    mean_audio_events=statistics.fmean(row.audio_events for row in items),
                    mean_visual_memory_reads=statistics.fmean(row.visual_memory_reads for row in items),
                    mean_audio_memory_reads=statistics.fmean(row.audio_memory_reads for row in items),
                    mean_tools_built=statistics.fmean(row.tool_markers_built + row.tool_alarms_built for row in items),
                    mean_tool_reads=statistics.fmean(row.tool_reads for row in items),
                    mean_attention_switches=statistics.fmean(row.attention_switches for row in items),
                    mean_self_state_adaptations=statistics.fmean(row.self_state_adaptations for row in items),
                    mean_confidence=statistics.fmean(row.mean_confidence for row in items),
                    external_memory_recovery_rate=statistics.fmean(1.0 if row.external_memory_recovery else 0.0 for row in items),
                )
            )
    return summary_rows


def expected_pressure_label(scenario: ScenarioSpec) -> str:
    labels = []
    if scenario.expected_vision_pressure:
        labels.append("vision")
    if scenario.expected_audio_pressure:
        labels.append("audio")
    if scenario.expected_tool_pressure:
        labels.append("tools")
    if scenario.expected_self_state_pressure:
        labels.append("self_state")
    return "+".join(labels) if labels else "none"


def build_verdicts(summary_rows: Sequence[SummaryRow], selected: Dict[int, Policy]) -> List[VerdictRow]:
    verdicts: List[VerdictRow] = []
    for scenario in SCENARIOS:
        policy = selected[scenario.index]
        by_condition = {
            row.condition: row
            for row in summary_rows
            if row.scenario == scenario.index and row.policy_name == policy.name
        }
        full = by_condition["full_perception"]
        no_perception = by_condition["no_perception"]
        no_vision = by_condition["no_vision"]
        no_audio = by_condition["no_audio"]
        no_fov = by_condition["no_fov_limit"]
        constant_loudness = by_condition["constant_loudness_audio"]
        no_direction = by_condition["no_direction_audio"]
        visual_memory = by_condition["visual_memory_ablation"]
        audio_memory = by_condition["audio_memory_ablation"]
        tool_alarm = by_condition["tool_alarm_ablation"]
        body_blind = by_condition["body_state_blind_perception"]
        omniscient = by_condition["omniscient_vision_control"]

        perception_gain = full.mean_reward - no_perception.mean_reward
        no_vision_loss = full.mean_reward - no_vision.mean_reward
        no_audio_loss = full.mean_reward - no_audio.mean_reward
        visual_memory_loss = full.mean_reward - visual_memory.mean_reward
        audio_memory_loss = full.mean_reward - audio_memory.mean_reward
        tool_alarm_loss = full.mean_reward - tool_alarm.mean_reward
        body_blind_loss = full.mean_reward - body_blind.mean_reward
        no_fov_control_gain = no_fov.mean_reward - full.mean_reward
        omniscient_control_gain = omniscient.mean_reward - full.mean_reward

        if scenario.index == 0:
            supports = (
                perception_gain < 10.0
                and no_vision_loss < 8.0
                and no_audio_loss < 8.0
                and full.mean_tools_built < 0.5
                and omniscient_control_gain < 8.0
            )
            verdict = "partial_perception_rejected_in_control" if supports else "control_overuses_perception"
        elif scenario.index == 1:
            supports = (
                perception_gain > 20.0
                and no_vision_loss > 18.0
                and visual_memory_loss > 12.0
                and no_audio_loss < 10.0
                and no_fov_control_gain > 8.0
            )
            verdict = "cone_vision_memory_pressure" if supports else "cone_vision_pressure_unclear"
        elif scenario.index == 2:
            supports = (
                perception_gain > 20.0
                and no_audio_loss > 18.0
                and max(full.mean_reward - constant_loudness.mean_reward, full.mean_reward - no_direction.mean_reward) > 10.0
                and tool_alarm_loss > 10.0
                and no_vision_loss < 12.0
            )
            verdict = "spatial_audio_alarm_pressure" if supports else "audio_alarm_pressure_unclear"
        elif scenario.index == 3:
            supports = (
                perception_gain > 28.0
                and no_vision_loss > 12.0
                and no_audio_loss > 12.0
                and visual_memory_loss > 8.0
                and audio_memory_loss > 8.0
                and full.external_memory_recovery_rate > 0.55
            )
            verdict = "multimodal_memory_pressure" if supports else "multimodal_pressure_unclear"
        else:
            supports = (
                perception_gain > 28.0
                and body_blind_loss > 14.0
                and full.mean_self_state_adaptations > 0.5
                and no_vision_loss > 8.0
                and no_audio_loss > 8.0
            )
            verdict = "sensor_damage_self_state_pressure" if supports else "sensor_damage_pressure_unclear"

        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                expected_pressure=expected_pressure_label(scenario),
                selected_policy=policy.name,
                selected_reward=full.mean_reward,
                no_perception_reward=no_perception.mean_reward,
                no_vision_reward=no_vision.mean_reward,
                no_audio_reward=no_audio.mean_reward,
                no_fov_limit_reward=no_fov.mean_reward,
                constant_loudness_audio_reward=constant_loudness.mean_reward,
                no_direction_audio_reward=no_direction.mean_reward,
                visual_memory_ablation_reward=visual_memory.mean_reward,
                audio_memory_ablation_reward=audio_memory.mean_reward,
                tool_alarm_ablation_reward=tool_alarm.mean_reward,
                body_state_blind_reward=body_blind.mean_reward,
                omniscient_vision_reward=omniscient.mean_reward,
                perception_gain_over_no_perception=perception_gain,
                no_vision_loss=no_vision_loss,
                no_audio_loss=no_audio_loss,
                visual_memory_loss=visual_memory_loss,
                audio_memory_loss=audio_memory_loss,
                tool_alarm_loss=tool_alarm_loss,
                body_state_blind_loss=body_blind_loss,
                no_fov_control_gain=no_fov_control_gain,
                omniscient_control_gain=omniscient_control_gain,
                selected_tools_built=full.mean_tools_built,
                selected_memory_reads=full.mean_visual_memory_reads + full.mean_audio_memory_reads,
                supports_structured_perception_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def build_trace(cfg: PerceptionConfig, selected: Dict[int, Policy]) -> Dict[str, object]:
    scenario = SCENARIOS[cfg.trace_scenario]
    policy = selected[scenario.index]
    frames: List[Dict[str, object]] = []
    for tick in range(12):
        rng = random.Random(stable_seed(cfg.seed, "trace", scenario.index, tick))
        phase = tick / 11.0
        heading = -60.0 + phase * 132.0
        light = scenario.light_level * (0.82 + 0.18 * math.sin(phase * math.pi))
        vision = visual_quality(scenario, policy, "full_perception", rng)
        audio = audio_quality(scenario, policy, "full_perception", rng)
        fov_center = heading
        fov_width = 86.0
        visual_events = []
        if vision > 0.18 and tick % 2 == 0:
            visual_events.append(
                {
                    "kind": "water_source" if tick < 8 else "shelter",
                    "bearing": round(-24.0 + phase * 45.0, 1),
                    "distance_estimate": round(34.0 - phase * 18.0, 1),
                    "confidence": round(vision, 3),
                    "motion": "still",
                }
            )
        if scenario.hazard_pressure > 0.35 and vision > 0.24 and tick in (3, 4, 9):
            visual_events.append(
                {
                    "kind": "hazard",
                    "bearing": round(38.0 - phase * 28.0, 1),
                    "distance_estimate": round(22.0 - phase * 7.0, 1),
                    "confidence": round(max(0.0, vision - 0.08), 3),
                    "motion": "approaching" if tick == 4 else "still",
                }
            )
        audio_events = []
        if audio > 0.18:
            audio_events.append(
                {
                    "kind": "tool_alarm" if policy.tool_alarms else "water",
                    "loudness": round(audio, 3),
                    "direction": round(-35.0 + phase * 50.0, 1),
                    "confidence": round(min(1.0, audio + 0.12), 3),
                    "source_memory": "known_alarm_03" if policy.tool_alarms else "unknown_water",
                }
            )
        if scenario.social_audio > 0.0 and tick in (5, 6):
            audio_events.append(
                {
                    "kind": "social_call",
                    "loudness": round(max(0.0, audio - 0.10), 3),
                    "direction": 76.0,
                    "confidence": round(max(0.0, audio - 0.02), 3),
                    "source_memory": "unknown_agent",
                }
            )
        frames.append(
            {
                "tick": tick,
                "heading": round(heading, 1),
                "fov_center": round(fov_center, 1),
                "fov_width": fov_width,
                "light_level": round(light, 3),
                "vision_quality": round(vision, 3),
                "audio_quality": round(audio, 3),
                "visual_events": visual_events,
                "audio_events": audio_events,
                "memory_reads": {
                    "visual": int(policy.visual_memory) * int(round(vision * 4)),
                    "audio": int(policy.audio_memory) * int(round(audio * 4)),
                },
                "tool_state": {
                    "marker_active": policy.tool_markers,
                    "alarm_active": policy.tool_alarms,
                },
            }
        )
    condition_outcomes: Dict[str, Dict[str, float]] = {}
    for condition in CONDITIONS:
        rows = evaluate_policy(scenario, policy, condition, cfg.eval_episodes, cfg, "trace_eval")
        condition_outcomes[condition] = {
            "mean_reward": mean_reward(rows),
            "mean_success_rate": statistics.fmean(row.success_rate for row in rows),
        }
    return {
        "scenario": asdict(scenario),
        "policy": asdict(policy),
        "frames": frames,
        "condition_outcomes": condition_outcomes,
    }


def write_csv(path: Path, rows: Iterable[object]) -> None:
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


def run_experiment(cfg: PerceptionConfig) -> Tuple[List[EpisodeResult], List[PolicySelectionRow], List[SummaryRow], List[VerdictRow], Dict[str, object]]:
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
        "artifact_note": "Structured cone vision and spatial audio are event packets, not raw pixels or waveforms.",
    }
    return eval_rows, selection_rows, summary_rows, verdict_rows, {"results": results, "trace": trace}


def print_table(verdicts: Sequence[VerdictRow]) -> None:
    headers = [
        "scenario",
        "policy",
        "gain",
        "vision_loss",
        "audio_loss",
        "body_loss",
        "supports",
    ]
    rows = [
        [
            row.scenario_name,
            row.selected_policy,
            f"{row.perception_gain_over_no_perception:.3f}",
            f"{row.no_vision_loss:.3f}",
            f"{row.no_audio_loss:.3f}",
            f"{row.body_state_blind_loss:.3f}",
            str(row.supports_structured_perception_precursor),
        ]
        for row in verdicts
    ]
    widths = [max(len(header), *(len(row[index]) for row in rows)) for index, header in enumerate(headers)]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> PerceptionConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-episodes", type=int, default=PerceptionConfig.train_episodes)
    parser.add_argument("--eval-episodes", type=int, default=PerceptionConfig.eval_episodes)
    parser.add_argument("--ticks", type=int, default=PerceptionConfig.ticks)
    parser.add_argument("--seed", type=int, default=PerceptionConfig.seed)
    parser.add_argument("--candidate-count", type=int, default=PerceptionConfig.candidate_count)
    parser.add_argument("--trace-scenario", type=int, default=PerceptionConfig.trace_scenario)
    parser.add_argument("--trace-episode", type=int, default=PerceptionConfig.trace_episode)
    args = parser.parse_args()
    if args.train_episodes < 24:
        raise SystemExit("--train-episodes must be at least 24")
    if args.eval_episodes < 24:
        raise SystemExit("--eval-episodes must be at least 24")
    if args.candidate_count < len(SEEDED_POLICIES):
        raise SystemExit(f"--candidate-count must be at least {len(SEEDED_POLICIES)}")
    if args.trace_scenario < 0 or args.trace_scenario >= len(SCENARIOS):
        raise SystemExit("--trace-scenario out of range")
    return PerceptionConfig(
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

    eval_path = ARTIFACT_DIR / "ssrm_3d_structured_perception_eval.csv"
    selection_path = ARTIFACT_DIR / "ssrm_3d_structured_perception_policy_selection.csv"
    summary_path = ARTIFACT_DIR / "ssrm_3d_structured_perception_summary.csv"
    verdict_path = ARTIFACT_DIR / "ssrm_3d_structured_perception_verdict.csv"
    results_path = ARTIFACT_DIR / "ssrm_3d_structured_perception_results.json"
    trace_path = ARTIFACT_DIR / "ssrm_3d_structured_perception_trace.json"
    results_js_path = ARTIFACT_DIR / "ssrm_3d_structured_perception_results.js"
    trace_js_path = ARTIFACT_DIR / "ssrm_3d_structured_perception_trace.js"

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
    write_js(results_js_path, "SSRM_3D_STRUCTURED_PERCEPTION_RESULTS", payload["results"])
    write_js(trace_js_path, "SSRM_3D_STRUCTURED_PERCEPTION_TRACE", payload["trace"])

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
    if not all(row.supports_structured_perception_precursor for row in verdict_rows):
        print("structured perception precursor not supported by all verdict rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
