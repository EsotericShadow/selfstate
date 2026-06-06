#!/usr/bin/env python3
"""Rollout-window sequence planner for SSRM-3D coupled crises.

Report 110 showed that an analytic sequence overlay could not repair stricter
environmental bottlenecks. This benchmark keeps the same non-substitutable
crisis world, but trains the plan-value head from short cloned rollouts through
the actual simulator instead of from an analytic utility.

The controller consumes ordinary symptom features plus recent/current group
response context and elapsed crisis time. It does not receive the active crisis
profile or scenario label. This is still not deep reinforcement learning,
subjective consciousness, or open-ended civilization.
"""

from __future__ import annotations

import argparse
import copy
import csv
import json
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import torch
from torch import nn

import ssrm_3d_coupled_crisis_repair_critic_controller as report107
import ssrm_3d_coupled_social_environment_maturation_controller as coupled
import ssrm_3d_learned_multiday_maturation_controller as base
import ssrm_3d_return_selected_multiday_maturation_controller as report105
from ssrm_maturation.agents import choose_action, make_agents
from ssrm_maturation.benchmark import TRACE_CHECKPOINTS, score_episode, snapshot
from ssrm_maturation.environment import clamp, living
from ssrm_maturation.models import CONDITIONS, Agent, Condition, Trace, World


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_rollout_window"

ENV_RESPONSE_ACTIONS = ("sanitize", "treat", "scout", "construct", "collect_water", "harvest_food")
DIAGNOSTIC_ENV_ACTIONS = ("sanitize", "treat", "scout", "construct")
SOCIAL_RESPONSE_ACTIONS = ("social_repair", "teach", "learn")
SUSTAIN_ACTIONS = ("rest", "stay_near_shelter", "collect_water", "harvest_food")
TOOL_ACTIONS = ("improve_tools",)
INFRASTRUCTURE_ACTIONS = ("construct",)
PLAN_CONTEXT_SIZE = 6
PRIMARY_ENV_ACTION = {
    "contaminated_water_trust": "sanitize",
    "route_migration_dispute": "scout",
    "storm_shelter_coordination": "construct",
    "quarantine_rumor": "treat",
}


@dataclass(frozen=True)
class Config:
    train_seeds: Sequence[int]
    tune_seeds: Sequence[int]
    eval_seeds: Sequence[int]
    hours: float = 72.0
    step_hours: float = 0.10
    population: int = 14
    epochs: int = 42
    hidden_size: int = 64
    learning_rate: float = 0.004
    plan_epochs: int = 72
    plan_hidden_size: int = 72
    plan_learning_rate: float = 0.003
    plan_bias_candidates: Sequence[float] = (0.0, 1.0, 1.75, 2.75, 4.0, 5.5, 7.0)
    max_plan_examples: int = 160000
    device: str = "auto"
    trace_seed: int = 20261021


@dataclass(frozen=True)
class PlanTemplate:
    name: str
    env_weight: float
    social_weight: float
    sustain_weight: float
    tool_weight: float
    infrastructure_weight: float
    teaching_weight: float
    horizon_hours: float


PLAN_TEMPLATES = (
    PlanTemplate("balanced_repair", 0.66, 0.66, 0.08, 0.05, 0.08, 0.20, 1.8),
    PlanTemplate("environment_first", 0.92, 0.28, 0.06, 0.06, 0.16, 0.06, 1.6),
    PlanTemplate("social_first", 0.30, 0.92, 0.06, 0.04, 0.05, 0.36, 1.6),
    PlanTemplate("sanitize_care_window", 0.84, 0.52, 0.10, 0.04, 0.03, 0.16, 1.9),
    PlanTemplate("route_supply_window", 0.76, 0.36, 0.28, 0.10, 0.08, 0.08, 1.8),
    PlanTemplate("storm_infrastructure_window", 0.80, 0.38, 0.12, 0.08, 0.50, 0.08, 2.0),
    PlanTemplate("teaching_repair_window", 0.38, 0.86, 0.06, 0.05, 0.04, 0.52, 1.8),
    PlanTemplate("recovery_sustain_window", 0.42, 0.42, 0.58, 0.24, 0.20, 0.16, 2.2),
)

PLAN_INPUT_SIZE = base.FEATURE_COUNT + len(PLAN_TEMPLATES) + PLAN_CONTEXT_SIZE
PLAN_INDEX = {plan.name: index for index, plan in enumerate(PLAN_TEMPLATES)}


@dataclass(frozen=True)
class PlanTrainingRow:
    train_loss: float
    pairwise_accuracy: float
    device_used: str
    parameter_count: int
    train_examples: int
    positive_examples: int
    plan_epochs: int
    plan_hidden_size: int


@dataclass(frozen=True)
class PlanSelectionRow:
    plan_bias: float
    tune_total_score: float
    tune_maturation_score: float
    tune_crisis_score: float
    tune_resolved_rate: float
    tune_coupled_response: float
    tune_damage: float
    selection_objective: float
    selected: bool


@dataclass(frozen=True)
class VerdictRow:
    selected_router: str
    selected_plan_bias: float
    rollout_window_total_score: float
    repair_critic_total_score: float
    return_selected_total_score: float
    base_gru_total_score: float
    designed_total_score: float
    frame_total_score: float
    reactive_total_score: float
    gain_over_repair_critic: float
    gain_over_return_selected: float
    gain_over_base_gru: float
    gain_over_frame: float
    gain_over_reactive: float
    gap_to_designed: float
    rollout_window_crisis_score: float
    return_selected_crisis_score: float
    rollout_window_resolved_rate: float
    return_selected_resolved_rate: float
    rollout_window_coupled_response: float
    return_selected_coupled_response: float
    social_culture_total_loss: float
    environment_total_loss: float
    social_culture_crisis_loss: float
    environment_crisis_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    supports_rollout_window_selection: bool
    supports_social_environment_dependency: bool
    verdict: str


class RolloutWindowPlanNet(nn.Module):
    def __init__(self, input_size: int, hidden_size: int) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.Tanh(),
            nn.Linear(hidden_size, hidden_size),
            nn.Tanh(),
            nn.Linear(hidden_size, 1),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x).squeeze(-1)


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def idx(name: str) -> int:
    return base.FEATURE_NAMES.index(name)


FEATURE = {name: idx(name) for name in base.FEATURE_NAMES}

NEUTRAL_SENSOR_VALUES = {
    "social_culture": {
        "social_trust": 0.64,
        "conflict": 0.0,
        "culture": 0.66,
        "symbols": 0.58,
        "risk_memory": 0.58,
        "knowledge_transfer": 0.74,
    },
    "environment": {
        "soil": 0.58,
        "contamination": 0.0,
        "temperature": 0.55,
        "rainfall": 0.28,
        "wind": 0.22,
        "visibility": 0.70,
        "route_hazard": 0.0,
        "disease": 0.0,
        "predators": 0.0,
        "resource_migration": 0.0,
        "resource_depletion": 0.0,
        "adaptive_pressure": 0.0,
        "pressure_integral": 0.0,
    },
    "infrastructure": {
        "shelter": 0.62,
        "architecture": 0.62,
        "waterworks": 0.56,
        "granary": 0.52,
        "paths": 0.52,
        "garden": 0.52,
        "sanitation": 0.50,
        "architecture_tier": 0.50,
    },
    "tools": {
        "tools": 0.76,
        "workshop": 0.62,
        "fire_control": 0.48,
        "tool_tier": 0.75,
    },
}


def parse_ints(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def parse_floats(value: str) -> Tuple[float, ...]:
    return tuple(float(part.strip()) for part in value.split(",") if part.strip())


def diagnostic_features(features: Sequence[float], ablation: str) -> List[float]:
    """Mask ablated sensors without converting missing data into false urgency."""
    if ablation == "none":
        return list(features)
    masked = base.mask_features(list(features), ablation)
    for name, value in NEUTRAL_SENSOR_VALUES.get(ablation, {}).items():
        masked[FEATURE[name]] = value
    return masked


def pressure_from_diagnostic_features(features: Sequence[float]) -> Dict[str, float]:
    social = clamp(
        features[FEATURE["conflict"]] * 0.44
        + max(0.0, 0.58 - features[FEATURE["social_trust"]]) * 0.30
        + max(0.0, 0.62 - features[FEATURE["culture"]]) * 0.18
        + max(0.0, 0.54 - features[FEATURE["symbols"]]) * 0.14
    )
    environment = clamp(
        features[FEATURE["contamination"]] * 0.22
        + features[FEATURE["disease"]] * 0.24
        + features[FEATURE["predators"]] * 0.18
        + features[FEATURE["route_hazard"]] * 0.18
        + features[FEATURE["resource_migration"]] * 0.12
        + features[FEATURE["resource_depletion"]] * 0.12
        + abs(features[FEATURE["temperature"]] - 0.55) * 0.14
        + max(0.0, 0.52 - features[FEATURE["visibility"]]) * 0.10
        + features[FEATURE["rainfall"]] * 0.07
        + features[FEATURE["wind"]] * 0.06
    )
    infrastructure = clamp(
        max(0.0, 0.62 - features[FEATURE["shelter"]]) * 0.22
        + max(0.0, 0.62 - features[FEATURE["architecture"]]) * 0.22
        + max(0.0, 0.56 - features[FEATURE["waterworks"]]) * 0.18
        + max(0.0, 0.52 - features[FEATURE["granary"]]) * 0.14
        + max(0.0, 0.52 - features[FEATURE["paths"]]) * 0.14
        + max(0.0, 0.50 - features[FEATURE["sanitation"]]) * 0.12
    )
    tools = clamp(
        max(0.0, 0.76 - features[FEATURE["tools"]]) * 0.36
        + max(0.0, 0.62 - features[FEATURE["workshop"]]) * 0.24
        + max(0.0, 0.48 - features[FEATURE["fire_control"]]) * 0.14
        + max(0.0, 0.75 - features[FEATURE["tool_tier"]]) * 0.18
    )
    teaching = clamp(
        max(0.0, 0.72 - features[FEATURE["knowledge_transfer"]]) * 0.34
        + max(0.0, 0.66 - features[FEATURE["culture"]]) * 0.22
        + max(0.0, 0.58 - features[FEATURE["risk_memory"]]) * 0.18
        + max(0.0, 0.52 - features[FEATURE["symbols"]]) * 0.12
    )
    return {
        "social": social,
        "environment": environment,
        "infrastructure": infrastructure,
        "tools": tools,
        "teaching": teaching,
    }


def diagnostic_router_bias(
    features: Sequence[float],
    router: report105.PressureRouter,
    device: torch.device,
    dtype: torch.dtype,
    ablation: str,
) -> torch.Tensor:
    masked = diagnostic_features(features, ablation)
    pressure = pressure_from_diagnostic_features(masked)
    bias = torch.zeros((1, len(base.ACTIONS)), dtype=dtype, device=device)
    bias[:, base.ACTION_TO_INDEX["social_repair"]] += pressure["social"] * router.social_bias
    bias[:, base.ACTION_TO_INDEX["teach"]] += pressure["social"] * router.social_bias * 0.38
    bias[:, base.ACTION_TO_INDEX["sanitize"]] += pressure["environment"] * router.environment_bias * 0.65
    bias[:, base.ACTION_TO_INDEX["treat"]] += pressure["environment"] * router.environment_bias * 0.42
    bias[:, base.ACTION_TO_INDEX["scout"]] += pressure["environment"] * router.environment_bias * 0.72
    bias[:, base.ACTION_TO_INDEX["construct"]] += pressure["infrastructure"] * router.infrastructure_bias
    bias[:, base.ACTION_TO_INDEX["improve_tools"]] += pressure["tools"] * router.tool_bias
    bias[:, base.ACTION_TO_INDEX["teach"]] += pressure["teaching"] * router.teaching_bias
    bias[:, base.ACTION_TO_INDEX["learn"]] += pressure["teaching"] * router.teaching_bias * 0.30
    return bias


def bottleneck_gate(features: Sequence[float], ablation: str) -> float:
    masked = diagnostic_features(features, ablation)
    pressure = pressure_from_diagnostic_features(masked)
    post_gate = masked[FEATURE["post_gate"]]
    shock_hint = masked[FEATURE["major_shocks"]]
    symptom_pressure = max(
        pressure["environment"],
        pressure["social"],
        pressure["infrastructure"] * 0.65,
        pressure["teaching"] * 0.55,
    )
    return clamp(symptom_pressure * (0.30 + 0.70 * post_gate) + shock_hint * 0.22 - 0.12)


def one_hot_plan(plan: PlanTemplate) -> List[float]:
    index = PLAN_INDEX[plan.name]
    return [1.0 if item == index else 0.0 for item in range(len(PLAN_TEMPLATES))]


def plan_input(
    features: Sequence[float],
    plan: PlanTemplate,
    env_context: float,
    social_context: float,
    recent_env: float,
    recent_social: float,
    elapsed_fraction: float,
    remaining_fraction: float,
) -> List[float]:
    return [
        *features,
        *one_hot_plan(plan),
        clamp(env_context),
        clamp(social_context),
        clamp(recent_env),
        clamp(recent_social),
        clamp(elapsed_fraction),
        clamp(remaining_fraction),
    ]


def response_fractions(action_counts: Dict[str, int], alive_count: int) -> Tuple[float, float]:
    denom = max(1, alive_count)
    env = sum(action_counts.get(action, 0) for action in ENV_RESPONSE_ACTIONS) / denom
    social = sum(action_counts.get(action, 0) for action in SOCIAL_RESPONSE_ACTIONS) / denom
    return env, social


def action_skill(features: Sequence[float], action: str) -> float:
    if action == "construct":
        return features[FEATURE["build_skill"]]
    if action == "improve_tools":
        return features[FEATURE["tool_skill"]]
    if action in {"harvest_food", "collect_water"}:
        return features[FEATURE["harvest_skill"]]
    if action == "scout":
        return features[FEATURE["scout_skill"]]
    if action in {"sanitize", "treat"}:
        return features[FEATURE["care_skill"]]
    if action in {"teach", "social_repair"}:
        return clamp(features[FEATURE["teach_skill"]] * 0.60 + features[FEATURE["sociability"]] * 0.40)
    if action == "learn":
        return clamp(features[FEATURE["curiosity"]] * 0.55 + features[FEATURE["sociability"]] * 0.25 + features[FEATURE["wisdom"]] * 0.20)
    return clamp(features[FEATURE["energy"]] * 0.50 + features[FEATURE["health"]] * 0.50)


def symptom_fit(features: Sequence[float], action: str) -> float:
    if action == "sanitize":
        return clamp(features[FEATURE["contamination"]] * 0.82 + features[FEATURE["rainfall"]] * 0.08 + max(0.0, 0.50 - features[FEATURE["sanitation"]]) * 0.10)
    if action == "treat":
        return clamp(features[FEATURE["disease"]] * 0.72 + features[FEATURE["contamination"]] * 0.16 + features[FEATURE["illness"]] * 0.08)
    if action == "scout":
        return clamp(features[FEATURE["route_hazard"]] * 0.44 + features[FEATURE["resource_migration"]] * 0.30 + features[FEATURE["predators"]] * 0.12 + max(0.0, 0.56 - features[FEATURE["visibility"]]) * 0.14)
    if action == "construct":
        storm_signal = (
            features[FEATURE["rainfall"]] * 0.24
            + features[FEATURE["wind"]] * 0.24
            + max(0.0, 0.58 - features[FEATURE["visibility"]]) * 0.16
            + abs(features[FEATURE["temperature"]] - 0.55) * 0.10
        )
        return clamp(storm_signal + max(0.0, 0.62 - features[FEATURE["shelter"]]) * 0.18 + max(0.0, 0.62 - features[FEATURE["architecture"]]) * 0.12)
    if action == "collect_water":
        return clamp(max(0.0, 0.56 - features[FEATURE["water"]]) * 0.34 + features[FEATURE["contamination"]] * 0.22 + features[FEATURE["resource_migration"]] * 0.12)
    if action == "harvest_food":
        return clamp(max(0.0, 0.56 - features[FEATURE["food"]]) * 0.34 + features[FEATURE["resource_migration"]] * 0.26 + features[FEATURE["resource_depletion"]] * 0.12)
    if action == "social_repair":
        return clamp(features[FEATURE["conflict"]] * 0.55 + max(0.0, 0.62 - features[FEATURE["social_trust"]]) * 0.35)
    if action == "teach":
        return clamp(max(0.0, 0.74 - features[FEATURE["culture"]]) * 0.35 + max(0.0, 0.64 - features[FEATURE["risk_memory"]]) * 0.30 + max(0.0, 0.56 - features[FEATURE["symbols"]]) * 0.20 + max(0.0, 0.76 - features[FEATURE["knowledge_transfer"]]) * 0.15)
    if action == "learn":
        return clamp(max(0.0, 0.78 - features[FEATURE["knowledge_transfer"]]) * 0.30 + max(0.0, 0.62 - features[FEATURE["wisdom"]]) * 0.20)
    if action == "improve_tools":
        return clamp(max(0.0, 0.74 - features[FEATURE["tools"]]) * 0.45 + max(0.0, 0.58 - features[FEATURE["workshop"]]) * 0.28)
    return 0.0


def best_group_fit(features: Sequence[float], actions: Sequence[str]) -> float:
    if not actions:
        return 0.0
    return max(symptom_fit(features, action) * 0.70 + action_skill(features, action) * 0.30 for action in actions)


def best_diagnostic_env_action(features: Sequence[float]) -> Tuple[str, float]:
    scored = [
        (action, symptom_fit(features, action) * 0.86 + action_skill(features, action) * 0.14)
        for action in DIAGNOSTIC_ENV_ACTIONS
    ]
    return max(scored, key=lambda item: item[1])


def primary_env_action(active: coupled.ActiveCrisis) -> str:
    return PRIMARY_ENV_ACTION[active.profile.name]


def bottleneck_target_action(active: coupled.ActiveCrisis, features: Sequence[float]) -> str:
    env_fraction = min(1.0, active.env_progress / active.profile.env_need)
    social_fraction = min(1.0, active.social_progress / active.profile.social_need)
    if 1.0 - env_fraction >= 1.0 - social_fraction + 0.02:
        return primary_env_action(active)
    if features[FEATURE["conflict"]] > 0.30 or features[FEATURE["social_trust"]] < 0.54:
        return "social_repair"
    if "teach" in active.profile.social_actions:
        return "teach"
    if "learn" in active.profile.social_actions:
        return "learn"
    return active.profile.social_actions[0]


def plan_social_action(plan: PlanTemplate, features: Sequence[float]) -> str:
    if (
        features[FEATURE["conflict"]] > 0.28
        or features[FEATURE["social_trust"]] < 0.56
        or plan.social_weight > plan.teaching_weight + 0.25
    ):
        return "social_repair"
    if (
        plan.teaching_weight >= 0.30
        or features[FEATURE["knowledge_transfer"]] < 0.72
        or features[FEATURE["risk_memory"]] < 0.60
    ):
        return "teach"
    return "learn"


def plan_environment_action(plan: PlanTemplate, features: Sequence[float]) -> str:
    if plan.name == "sanitize_care_window":
        return "sanitize" if features[FEATURE["contamination"]] >= features[FEATURE["disease"]] * 0.88 else "treat"
    if plan.name == "route_supply_window":
        return "scout"
    if plan.name == "storm_infrastructure_window":
        return "construct"
    return best_diagnostic_env_action(features)[0]


def plan_forced_action(
    plan: PlanTemplate,
    active: coupled.ActiveCrisis,
    features: Sequence[float],
    rng: random.Random,
) -> str:
    env_fraction = min(1.0, active.env_progress / active.profile.env_need)
    social_fraction = min(1.0, active.social_progress / active.profile.social_need)
    env_gap = 1.0 - env_fraction
    social_gap = 1.0 - social_fraction

    if plan.sustain_weight >= 0.34:
        if features[FEATURE["health"]] < 0.42 or features[FEATURE["energy"]] < 0.34:
            return "rest"
        if features[FEATURE["water"]] < 0.42:
            return "collect_water"
        if features[FEATURE["food"]] < 0.42:
            return "harvest_food"
    if (
        plan.tool_weight >= 0.18
        and (features[FEATURE["tools"]] < 0.62 or features[FEATURE["workshop"]] < 0.54)
        and rng.random() < 0.48
    ):
        return "improve_tools"

    env_action = plan_environment_action(plan, features)
    social_action = plan_social_action(plan, features)
    env_fit = symptom_fit(features, env_action) * 0.82 + action_skill(features, env_action) * 0.18
    social_fit = symptom_fit(features, social_action) * 0.72 + action_skill(features, social_action) * 0.28
    env_priority = plan.env_weight * (0.42 + env_gap * 0.78 + env_fit * 0.40)
    social_priority = plan.social_weight * (0.42 + social_gap * 0.78 + social_fit * 0.34)
    if env_gap > social_gap + 0.18:
        env_priority += 0.22
    if social_gap > env_gap + 0.18:
        social_priority += 0.22
    total = max(1e-6, env_priority + social_priority)
    return env_action if rng.random() < env_priority / total else social_action


def tracker_fractions(tracker: coupled.CrisisTracker) -> Tuple[float, float, float]:
    active = tracker.active
    if active is not None:
        env_fraction = min(1.0, active.env_progress / active.profile.env_need)
        social_fraction = min(1.0, active.social_progress / active.profile.social_need)
        return env_fraction, social_fraction, min(env_fraction, social_fraction)
    if tracker.response_log:
        last = tracker.response_log[-1]
        env_fraction = float(last.get("env_fraction", 0.0))
        social_fraction = float(last.get("social_fraction", 0.0))
        return env_fraction, social_fraction, float(last.get("coupled_fraction", min(env_fraction, social_fraction)))
    return 0.0, 0.0, 0.0


def rollout_plan_value(
    plan: PlanTemplate,
    world: World,
    agents: List[Agent],
    tracker: coupled.CrisisTracker,
    previous_actions: Dict[str, int],
    cfg: Config,
    seed: int,
) -> float:
    if tracker.active is None:
        return 0.0
    start_env, start_social, start_coupled = tracker_fractions(tracker)
    start_resolved = tracker.resolved
    start_damage = tracker.damage_integral
    start_trust = world.social_trust
    start_resource_depletion = world.resource_depletion

    sim_world = copy.deepcopy(world)
    sim_agents = copy.deepcopy(agents)
    sim_tracker = copy.deepcopy(tracker)
    sim_previous = copy.deepcopy(previous_actions)
    sim_events: List[str] = []
    sim_rng = random.Random(seed)
    condition = CONDITIONS[0]
    window_end = min(cfg.hours, sim_tracker.active.end, sim_world.time + plan.horizon_hours)
    first_step = True
    while sim_world.time < window_end - 1e-9 and sim_tracker.active is not None:
        step_dt = min(cfg.step_hours, window_end - sim_world.time)
        if not first_step:
            coupled.apply_crisis_symptoms(sim_world, sim_tracker.active, step_dt)
        first_step = False
        action_counts: Dict[str, int] = {}

        def selector(
            agent: Agent,
            current_world: World,
            current_condition: Condition,
            current_rng: random.Random,
            features: List[float],
            previous: int,
        ) -> str:
            active = sim_tracker.active
            action = (
                plan_forced_action(plan, active, features, current_rng)
                if active is not None
                else choose_action(agent, current_world, current_condition, current_rng)
            )
            action_counts[action] = action_counts.get(action, 0) + 1
            return action

        base.step_world(sim_world, sim_agents, condition, step_dt, sim_rng, sim_previous, selector, sim_events)
        update_bottleneck_crisis_after_actions(sim_world, sim_agents, sim_tracker, action_counts, step_dt)
        coupled.complete_crisis_if_due(sim_world, sim_agents, sim_tracker, sim_events)

    final_env, final_social, final_coupled = tracker_fractions(sim_tracker)
    env_gain = max(0.0, final_env - start_env)
    social_gain = max(0.0, final_social - start_social)
    coupled_gain = max(0.0, final_coupled - start_coupled)
    damage_delta = max(0.0, sim_tracker.damage_integral - start_damage)
    resource_delta = max(0.0, sim_world.resource_depletion - start_resource_depletion)
    resolved_bonus = 0.65 if sim_tracker.resolved > start_resolved or final_coupled >= 0.92 else 0.0
    trust_delta = sim_world.social_trust - start_trust
    alive_delta = (len(living(sim_agents)) - len(living(agents))) / max(1, len(agents))
    value = (
        coupled_gain * 6.5
        + min(env_gain, social_gain) * 3.8
        + env_gain * 0.75
        + social_gain * 0.75
        + resolved_bonus
        + trust_delta * 0.25
        + alive_delta * 0.20
        - damage_delta * 2.6
        - resource_delta * 0.22
    )
    return max(-0.80, min(1.80, value))


def collect_plan_examples(cfg: Config) -> Tuple[List[List[float]], List[float]]:
    rng = random.Random(20261101)
    examples: List[List[float]] = []
    targets: List[float] = []
    condition = CONDITIONS[0]
    for seed in cfg.train_seeds:
        world_rng = random.Random(seed * 113 + 53)
        agents = make_agents(world_rng, cfg.population)
        world = coupled.prepare_world(world_rng, cfg)
        previous_actions: Dict[str, int] = {}
        events: List[str] = []
        tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))

        while world.time < cfg.hours - 1e-9 and len(examples) < cfg.max_plan_examples:
            dt = min(cfg.step_hours, cfg.hours - world.time)
            action_counts: Dict[str, int] = {}
            coupled.maybe_start_crisis(world, tracker, world_rng, events)
            if tracker.active is not None:
                coupled.apply_crisis_symptoms(world, tracker.active, dt)
                active = tracker.active
                if world.time >= 12.0 and rng.random() < 0.62 and len(examples) < cfg.max_plan_examples:
                    candidates = living(agents)
                    if candidates:
                        representative = max(
                            candidates,
                            key=lambda item: item.energy + item.health + item.sociability * 0.20,
                        )
                        previous = previous_actions.get(representative.ident, base.DEFAULT_ACTION)
                        features = base.observation(representative, world, previous, len(agents))
                        elapsed_fraction = clamp((world.time - active.start) / active.duration)
                        remaining_fraction = clamp((active.end - world.time) / active.duration)
                        recent_env = active.env_response_steps / max(1, active.steps)
                        recent_social = active.social_response_steps / max(1, active.steps)
                        for plan in PLAN_TEMPLATES:
                            examples.append(
                                plan_input(
                                    features,
                                    plan,
                                    0.0,
                                    0.0,
                                    recent_env,
                                    recent_social,
                                    elapsed_fraction,
                                    remaining_fraction,
                                )
                            )
                            targets.append(
                                rollout_plan_value(
                                    plan,
                                    world,
                                    agents,
                                    tracker,
                                    previous_actions,
                                    cfg,
                                    seed * 100000 + len(examples) * 17 + PLAN_INDEX[plan.name],
                                )
                            )
                            if len(examples) >= cfg.max_plan_examples:
                                break

            def selector(
                agent: Agent,
                current_world: World,
                current_condition: Condition,
                current_rng: random.Random,
                features: List[float],
                previous: int,
            ) -> str:
                action = bottleneck_target_action(tracker.active, features) if tracker.active is not None else choose_action(agent, current_world, current_condition, current_rng)
                action_counts[action] = action_counts.get(action, 0) + 1
                return action

            base.step_world(world, agents, condition, dt, world_rng, previous_actions, selector, events)
            update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
            coupled.complete_crisis_if_due(world, agents, tracker, events)
    return examples, targets


def train_plan_model(cfg: Config, device: torch.device) -> Tuple[RolloutWindowPlanNet, PlanTrainingRow]:
    examples, targets = collect_plan_examples(cfg)
    if not examples:
        raise RuntimeError("no rollout-window examples collected")
    torch.manual_seed(20261111)
    x = torch.tensor(examples, dtype=torch.float32, device=device)
    y = torch.tensor(targets, dtype=torch.float32, device=device)
    model = RolloutWindowPlanNet(PLAN_INPUT_SIZE, cfg.plan_hidden_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.plan_learning_rate)
    sample_weights = 1.0 + torch.clamp(y, min=0.0) * 3.5 + (y > 0.35).float() * 8.5
    for _ in range(cfg.plan_epochs):
        model.train()
        optimizer.zero_grad()
        prediction = model(x)
        loss = (((prediction - y) ** 2) * sample_weights).sum() / sample_weights.sum()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 2.0)
        optimizer.step()
    model.eval()
    with torch.no_grad():
        prediction = model(x)
        loss = ((((prediction - y) ** 2) * sample_weights).sum() / sample_weights.sum()).item()
        sample = torch.randperm(x.shape[0], device=device)[: min(5000, x.shape[0])]
        shifted = sample.roll(1)
        target_order = y[sample] > y[shifted]
        pred_order = prediction[sample] > prediction[shifted]
        pairwise_accuracy = (target_order == pred_order).float().mean().item()
    return model, PlanTrainingRow(
        train_loss=loss,
        pairwise_accuracy=pairwise_accuracy,
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in model.parameters()),
        train_examples=len(examples),
        positive_examples=sum(1 for target in targets if target > 0.35),
        plan_epochs=cfg.plan_epochs,
        plan_hidden_size=cfg.plan_hidden_size,
    )


def rollout_window_bias(
    features: Sequence[float],
    plan_model: RolloutWindowPlanNet,
    plan_bias: float,
    device: torch.device,
    dtype: torch.dtype,
    ablation: str,
    env_context: float,
    social_context: float,
    recent_env: float,
    recent_social: float,
    elapsed_fraction: float,
    remaining_fraction: float,
) -> torch.Tensor:
    gate = bottleneck_gate(features, ablation)
    if remaining_fraction > 0.0:
        gate = max(gate, 0.55 + 0.20 * remaining_fraction)
    bias = torch.zeros((1, len(base.ACTIONS)), dtype=dtype, device=device)
    if plan_bias <= 0.0 or gate <= 0.0:
        return bias
    masked = diagnostic_features(features, ablation)
    batch = torch.tensor(
        [
            plan_input(masked, plan, env_context, social_context, recent_env, recent_social, elapsed_fraction, remaining_fraction)
            for plan in PLAN_TEMPLATES
        ],
        dtype=torch.float32,
        device=device,
    )
    values = plan_model(batch)
    weights = torch.softmax(torch.clamp(values, -2.0, 2.0) * 1.35, dim=0)
    top_plan = PLAN_TEMPLATES[int(values.argmax().item())]
    preferred_env_action = plan_environment_action(top_plan, masked)
    preferred_social_action = plan_social_action(top_plan, masked)
    plan_mix = {
        "env": 0.0,
        "social": 0.0,
        "sustain": 0.0,
        "tool": 0.0,
        "infrastructure": 0.0,
        "teaching": 0.0,
    }
    for weight, plan in zip(weights.detach().cpu().tolist(), PLAN_TEMPLATES):
        plan_mix["env"] += weight * plan.env_weight
        plan_mix["social"] += weight * plan.social_weight
        plan_mix["sustain"] += weight * plan.sustain_weight
        plan_mix["tool"] += weight * plan.tool_weight
        plan_mix["infrastructure"] += weight * plan.infrastructure_weight
        plan_mix["teaching"] += weight * plan.teaching_weight

    env_pressure = max(env_context, recent_env * 0.75)
    social_pressure = max(social_context, recent_social * 0.75)
    env_missing = max(0.0, 0.70 - env_pressure)
    social_missing = max(0.0, 0.50 - social_pressure)
    env_overserved = max(0.0, env_pressure - social_pressure - 0.16)
    social_overserved = max(0.0, social_pressure - env_pressure - 0.16)
    best_env_action, best_env_score = best_diagnostic_env_action(masked)
    entries: List[float] = []
    for action in base.ACTIONS:
        score = 0.0
        fit = symptom_fit(masked, action)
        skill = action_skill(masked, action)
        if action in ENV_RESPONSE_ACTIONS:
            score += plan_mix["env"] * (0.20 + fit * 1.12 + skill * 0.10) * (0.78 + env_missing * 2.2)
            score += env_missing * (0.32 + fit * 1.25)
            score += social_overserved * (0.72 + fit * 1.10 + skill * 0.12)
            score -= env_overserved * 0.55
            if action == preferred_env_action:
                score += (plan_mix["env"] + env_missing + social_overserved) * (1.45 + fit * 1.75 + skill * 0.20)
            if action == best_env_action and best_env_score >= 0.13:
                score += (plan_mix["env"] + env_missing + social_overserved) * (1.85 + best_env_score * 3.10)
            elif action in {"collect_water", "harvest_food"}:
                score -= (plan_mix["env"] + env_missing) * 0.34
        if action in SOCIAL_RESPONSE_ACTIONS:
            social_score = plan_mix["social"] * (0.42 + fit * 0.46 + skill * 0.12) * (0.86 + social_missing * 1.8)
            social_score += social_missing * 0.68
            social_score += env_overserved * (1.25 + fit * 0.36 + skill * 0.12)
            social_score -= social_overserved * 1.05
            if env_missing > 0.42 and best_env_score >= 0.13:
                social_score -= env_missing * (1.08 + best_env_score * 0.80)
            if action == preferred_social_action:
                social_score += (plan_mix["social"] + social_missing + env_overserved) * (0.46 + fit * 0.44 + skill * 0.16)
            if env_missing > 0.16 and best_env_score >= 0.13:
                social_score -= env_missing * (0.58 + best_env_score * 0.52)
            if action in {"teach", "learn"}:
                social_score += plan_mix["teaching"] * (0.20 + fit * 0.22)
            score += social_score
        if action in SUSTAIN_ACTIONS:
            score += plan_mix["sustain"] * (0.18 + max(0.0, 0.42 - masked[FEATURE["energy"]]) * 0.30)
        if action in TOOL_ACTIONS:
            score += plan_mix["tool"] * (0.16 + fit * 0.20 + skill * 0.14)
        if action in INFRASTRUCTURE_ACTIONS:
            score += plan_mix["infrastructure"] * (0.18 + fit * 0.24 + skill * 0.14)
        entries.append(score)
    values_tensor = torch.tensor(entries, dtype=dtype, device=device)
    values_tensor = (values_tensor - values_tensor.mean()) / (values_tensor.std(unbiased=False) + 1e-4)
    values_tensor = torch.clamp(values_tensor, -1.8, 1.8)
    return values_tensor.reshape(1, -1) * plan_bias * gate


def update_bottleneck_crisis_after_actions(
    world: World,
    agents: List[Agent],
    tracker: coupled.CrisisTracker,
    action_counts: Dict[str, int],
    dt: float,
) -> None:
    active = tracker.active
    if active is None:
        return
    alive_count = max(1, len(living(agents)))
    primary_action = primary_env_action(active)
    env_effort = action_counts.get(primary_action, 0) / alive_count
    wrong_env_effort = (
        sum(action_counts.get(action, 0) for action in ENV_RESPONSE_ACTIONS if action != primary_action) / alive_count
    )
    social_effort = sum(action_counts.get(action, 0) for action in active.profile.social_actions) / alive_count
    active.steps += 1
    tracker.crisis_steps += 1
    active.env_progress += env_effort * dt * 1.70
    active.social_progress += social_effort * dt * 1.65
    env_hit = env_effort >= 0.10
    social_hit = social_effort >= 0.09
    if env_hit:
        active.env_response_steps += 1
        tracker.env_response_steps += 1
    if social_hit:
        active.social_response_steps += 1
        tracker.social_response_steps += 1
    if env_hit and social_hit:
        active.coupled_response_steps += 1
        tracker.coupled_response_steps += 1
        world.adaptation_evidence = clamp(world.adaptation_evidence + 0.005 * dt)
    env_fraction = min(1.0, active.env_progress / active.profile.env_need)
    social_fraction = min(1.0, active.social_progress / active.profile.social_need)
    unresolved = 1.0 - min(env_fraction, social_fraction)
    tracker.damage_integral += unresolved * active.severity * dt / 62.0
    tracker.damage_integral += wrong_env_effort * active.severity * dt / 36.0
    if unresolved > 0.0:
        world.conflict = clamp(world.conflict + active.profile.conflict_rate * unresolved * active.severity * 0.72 * dt)
        world.social_trust = clamp(world.social_trust - active.profile.trust_loss_rate * unresolved * active.severity * 0.72 * dt)
        world.disease = clamp(world.disease + active.profile.disease_rate * unresolved * active.severity * 0.64 * dt)
        world.contamination = clamp(world.contamination + active.profile.contamination_rate * unresolved * active.severity * 0.60 * dt)
    if wrong_env_effort > 0.0:
        world.resource_depletion = clamp(world.resource_depletion + wrong_env_effort * 0.010 * dt)


def run_episode(
    seed: int,
    cfg: Config,
    controller: str,
    model: Optional[base.ControllerNet],
    device: torch.device,
    router: report105.PressureRouter,
    plan_model: Optional[RolloutWindowPlanNet] = None,
    plan_bias: float = 0.0,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, Trace, coupled.CrisisTracker]:
    if controller == "rollout_window_gru" and (model is None or plan_model is None):
        raise ValueError("rollout_window_gru requires both base model and rollout window model")

    condition = CONDITIONS[1] if controller == "reactive" else CONDITIONS[0]
    rng = random.Random(seed * 127 + sum(ord(ch) for ch in controller + router.name + ablation) + int(plan_bias * 1000))
    agents = make_agents(rng, cfg.population)
    world = coupled.prepare_world(rng, cfg)
    baseline = base.initial_baseline(world, cfg.population)
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
    trace_out = Trace(seed=seed, condition=f"{controller}:{router.name}:bias_{plan_bias:g}:{ablation}")
    checkpoints = list(TRACE_CHECKPOINTS)
    no_pre_gate_shock = True
    alive_at_12h = cfg.population
    at_12: dict[str, float] = {}
    if trace:
        trace_out.frames.append(snapshot(world, agents, "0h", events))
        if checkpoints and checkpoints[0] == 0.0:
            checkpoints.pop(0)

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        action_counts: Dict[str, int] = {}
        coupled.maybe_start_crisis(world, tracker, rng, events)
        if tracker.active is not None:
            coupled.apply_crisis_symptoms(world, tracker.active, dt)

        def selector(
            agent: Agent,
            current_world: World,
            current_condition: Condition,
            current_rng: random.Random,
            features: List[float],
            previous: int,
        ) -> str:
            alive_count = max(1, len(living(agents)))
            env_context, social_context = response_fractions(action_counts, alive_count)
            active = tracker.active
            if controller == "designed":
                action = bottleneck_target_action(active, features) if active is not None else choose_action(agent, current_world, current_condition, current_rng)
            elif controller == "reactive":
                action = choose_action(agent, current_world, current_condition, current_rng)
            elif model is None:
                action = "rest"
            else:
                model_features = torch.tensor([base.mask_features(features, ablation)], dtype=torch.float32, device=device)
                with torch.no_grad():
                    if model.architecture == "gru":
                        state = recurrent_states.get(agent.ident)
                        logits, next_state = model.step(model_features, state)
                        if next_state is not None:
                            recurrent_states[agent.ident] = next_state.detach()
                    else:
                        logits, _ = model.step(model_features, None)
                    if active is None:
                        elapsed_fraction = 0.0
                        remaining_fraction = 0.0
                        recent_env = 0.0
                        recent_social = 0.0
                    else:
                        elapsed_fraction = clamp((current_world.time - active.start) / active.duration)
                        remaining_fraction = clamp((active.end - current_world.time) / active.duration)
                        recent_env = active.env_response_steps / max(1, active.steps)
                        recent_social = active.social_response_steps / max(1, active.steps)
                    if controller == "return_selected_gru":
                        logits = logits + report105.router_bias(features, router, device, logits.dtype, ablation)
                    elif controller == "rollout_window_gru":
                        base_logits = logits + diagnostic_router_bias(features, router, device, logits.dtype, ablation)
                        plan_logits = rollout_window_bias(
                            features,
                            plan_model,
                            plan_bias,
                            device,
                            logits.dtype,
                            ablation,
                            env_context,
                            social_context,
                            recent_env,
                            recent_social,
                            elapsed_fraction,
                            remaining_fraction,
                        )
                        if active is None or plan_bias <= 0.0:
                            logits = base_logits + plan_logits
                        else:
                            control_weight = 0.42 + 0.34 * remaining_fraction
                            logits = base_logits * (1.0 - control_weight) + plan_logits * (1.15 + control_weight)
                    action = base.INDEX_TO_ACTION[int(logits.argmax(dim=-1).item())]
            action_counts[action] = action_counts.get(action, 0) + 1
            return action

        base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
        update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
        coupled.complete_crisis_if_due(world, agents, tracker, events)
        if world.time < 12.0 and world.major_shocks > 0:
            no_pre_gate_shock = False
        if world.time >= 12.0 and not at_12:
            alive_at_12h = len(living(agents))
            at_12 = {
                "development": clamp(
                    (world.architecture - baseline["architecture"]) * 0.48
                    + (world.tools + world.workshop * 0.45 + world.fire_control * 0.30 - baseline["tool_system"]) * 0.34
                    + (world.paths - baseline["paths"]) * 0.16
                ),
                "knowledge": clamp(world.knowledge_transfer * 0.80 + (world.culture + world.symbols * 0.50 - baseline["culture_system"]) * 0.45),
            }
        while trace and checkpoints and world.time >= checkpoints[0] - 1e-9:
            hour = checkpoints.pop(0)
            frame = snapshot(world, agents, f"{hour:g}h", events)
            frame["active_crisis"] = tracker.active.profile.name if tracker.active else None
            frame["crisis_resolved"] = tracker.resolved
            frame["crisis_unresolved"] = tracker.unresolved
            frame["crisis_damage"] = tracker.damage_integral
            trace_out.frames.append(frame)

    if tracker.active is not None:
        coupled.complete_crisis_if_due(world, agents, tracker, events)
    episode = score_episode(world, agents, baseline, at_12, seed, condition, alive_at_12h, no_pre_gate_shock)
    crisis_score, resolved_rate, env_response, social_response, coupled_response = coupled.crisis_metrics(tracker)
    total_score = clamp(episode.maturation_score * 0.52 + crisis_score * 0.48)
    eval_row = coupled.EvalRow(
        seed=seed,
        controller=controller,
        ablation=ablation,
        total_score=total_score,
        maturation_score=episode.maturation_score,
        crisis_score=crisis_score,
        resolved_rate=resolved_rate,
        unresolved_count=tracker.unresolved,
        env_response_rate=env_response,
        social_response_rate=social_response,
        coupled_response_rate=coupled_response,
        crisis_damage=tracker.damage_integral,
        final_alive=episode.final_alive,
        total_agents=episode.total_agents,
        alive_at_12h=episode.alive_at_12h,
        no_major_shock_before_12h=episode.no_major_shock_before_12h,
        post_gate_shock=episode.post_gate_shock,
        births=episode.births,
        deaths=episode.deaths,
        architecture_tier=episode.architecture_tier,
        tool_tier=episode.tool_tier,
        knowledge_transfer=episode.knowledge_transfer,
        adaptation_evidence=episode.adaptation_evidence,
        survival_score=episode.survival_score,
        development_score=episode.development_score,
        knowledge_score=episode.knowledge_score,
        recovery_score=episode.recovery_score,
    )
    if trace and (not trace_out.frames or trace_out.frames[-1]["hours"] < cfg.hours):
        frame = snapshot(world, agents, f"{cfg.hours:g}h", events)
        frame["active_crisis"] = tracker.active.profile.name if tracker.active else None
        frame["crisis_resolved"] = tracker.resolved
        frame["crisis_unresolved"] = tracker.unresolved
        frame["crisis_damage"] = tracker.damage_integral
        trace_out.frames.append(frame)
    return eval_row, trace_out, tracker


def selection_objective(rows: Sequence[coupled.EvalRow]) -> Tuple[float, float, float, float, float, float]:
    total = mean(row.total_score for row in rows)
    maturation = mean(row.maturation_score for row in rows)
    crisis = mean(row.crisis_score for row in rows)
    resolved = mean(row.resolved_rate for row in rows)
    coupled_response = mean(row.coupled_response_rate for row in rows)
    damage = mean(row.crisis_damage for row in rows)
    objective = total * 0.70 + crisis * 0.70 + resolved * 0.35 + coupled_response * 0.45 - damage * 0.30
    return total, maturation, crisis, resolved, coupled_response, objective


def select_plan_bias(
    cfg: Config,
    model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
    plan_model: RolloutWindowPlanNet,
) -> Tuple[float, List[PlanSelectionRow]]:
    best = cfg.plan_bias_candidates[0]
    best_objective = -1.0
    rows: List[PlanSelectionRow] = []
    for bias in cfg.plan_bias_candidates:
        eval_rows = [
            run_episode(seed, cfg, "rollout_window_gru", model, device, router, plan_model, bias)[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, coupled_response, objective = selection_objective(eval_rows)
        damage = mean(row.crisis_damage for row in eval_rows)
        if objective > best_objective:
            best = bias
            best_objective = objective
        rows.append(
            PlanSelectionRow(
                plan_bias=bias,
                tune_total_score=total,
                tune_maturation_score=maturation,
                tune_crisis_score=crisis,
                tune_resolved_rate=resolved,
                tune_coupled_response=coupled_response,
                tune_damage=damage,
                selection_objective=objective,
                selected=False,
            )
        )
    return best, [
        PlanSelectionRow(
            row.plan_bias,
            row.tune_total_score,
            row.tune_maturation_score,
            row.tune_crisis_score,
            row.tune_resolved_rate,
            row.tune_coupled_response,
            row.tune_damage,
            row.selection_objective,
            row.plan_bias == best,
        )
        for row in rows
    ]


def ablations_from_summary(summary: Sequence[coupled.SummaryRow]) -> List[coupled.AblationRow]:
    base_row = coupled.row_lookup(summary, "rollout_window_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in ("body", "infrastructure", "tools", "social_culture", "environment", "previous_action"):
        row = coupled.row_lookup(summary, "rollout_window_gru", ablation)
        rows.append(
            coupled.AblationRow(
                ablation=ablation,
                mean_total_score=row.mean_total_score,
                total_loss=base_row.mean_total_score - row.mean_total_score,
                crisis_score_loss=base_row.mean_crisis_score - row.mean_crisis_score,
                resolved_rate_loss=base_row.mean_resolved_rate - row.mean_resolved_rate,
                env_response_loss=base_row.mean_env_response_rate - row.mean_env_response_rate,
                social_response_loss=base_row.mean_social_response_rate - row.mean_social_response_rate,
                coupled_response_loss=base_row.mean_coupled_response_rate - row.mean_coupled_response_rate,
                damage_increase=row.mean_crisis_damage - base_row.mean_crisis_damage,
            )
        )
    return rows


def verdict_from_summary(
    summary: Sequence[coupled.SummaryRow],
    ablations: Sequence[coupled.AblationRow],
    selected_router: report105.PressureRouter,
    selected_plan_bias: float,
) -> VerdictRow:
    outcome = coupled.row_lookup(summary, "rollout_window_gru", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    repair = coupled.row_lookup(summary, "repair_critic_baseline", "none")
    base_gru = coupled.row_lookup(summary, "gru", "none")
    designed = coupled.row_lookup(summary, "designed", "none")
    frame = coupled.row_lookup(summary, "frame_mlp", "none")
    reactive = coupled.row_lookup(summary, "reactive", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    supports_selection = (
        selected_plan_bias > 0.0
        and outcome.mean_total_score - returned.mean_total_score >= 0.025
        and (
            outcome.mean_crisis_score - returned.mean_crisis_score >= 0.060
            or outcome.mean_resolved_rate - returned.mean_resolved_rate >= 0.180
        )
        and outcome.mean_alive_at_12h >= 12.0
        and outcome.shock_gate_pass_rate == 1.0
        and outcome.post_gate_shock_rate == 1.0
    )
    supports_dependency = (
        social.crisis_score_loss >= 0.025
        and environment.crisis_score_loss >= 0.025
        and social.coupled_response_loss >= 0.020
        and environment.coupled_response_loss >= 0.020
    )
    return VerdictRow(
        selected_router=selected_router.name,
        selected_plan_bias=selected_plan_bias,
        rollout_window_total_score=outcome.mean_total_score,
        repair_critic_total_score=repair.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        base_gru_total_score=base_gru.mean_total_score,
        designed_total_score=designed.mean_total_score,
        frame_total_score=frame.mean_total_score,
        reactive_total_score=reactive.mean_total_score,
        gain_over_repair_critic=outcome.mean_total_score - repair.mean_total_score,
        gain_over_return_selected=outcome.mean_total_score - returned.mean_total_score,
        gain_over_base_gru=outcome.mean_total_score - base_gru.mean_total_score,
        gain_over_frame=outcome.mean_total_score - frame.mean_total_score,
        gain_over_reactive=outcome.mean_total_score - reactive.mean_total_score,
        gap_to_designed=designed.mean_total_score - outcome.mean_total_score,
        rollout_window_crisis_score=outcome.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        rollout_window_resolved_rate=outcome.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        rollout_window_coupled_response=outcome.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        social_culture_total_loss=social.total_loss,
        environment_total_loss=environment.total_loss,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=outcome.shock_gate_pass_rate,
        post_gate_shock_rate=outcome.post_gate_shock_rate,
        survival_at_12h=outcome.mean_alive_at_12h,
        supports_rollout_window_selection=supports_selection,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_selection and supports_dependency else "partial_or_failed",
    )


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = [asdict(row) for row in rows]
    if not data:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(data[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def write_js(path: Path, variable: str, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"window.{variable} = {json.dumps(payload, indent=2)};\n", encoding="utf-8")


def run_benchmark(cfg: Config) -> dict[str, object]:
    device = base.resolve_device(cfg.device)
    sequences, labels = base.collect_sequences(cfg)
    x, y, mask = base.build_tensors(sequences, labels, device)
    training_rows: List[base.TrainingRow] = []
    models: Dict[str, base.ControllerNet] = {}
    for architecture in ("frame_mlp", "gru"):
        model, row = base.train_model(architecture, x, y, mask, cfg, device)
        models[architecture] = model
        training_rows.append(row)

    selected_router, router_selection = coupled.select_router(cfg, models["gru"], device)
    plan_model, plan_training = train_plan_model(cfg, device)
    selected_bias, plan_selection = select_plan_bias(cfg, models["gru"], device, selected_router, plan_model)

    eval_rows: List[coupled.EvalRow] = []
    trace = Trace(seed=cfg.trace_seed, condition=f"rollout_window_gru:{selected_router.name}:bias_{selected_bias:g}:none")
    crisis_logs: Dict[str, List[dict[str, object]]] = {}
    for seed in cfg.eval_seeds:
        for controller, model, router, plan_net, bias in (
            ("designed", None, report105.ROUTERS[0], None, 0.0),
            ("reactive", None, report105.ROUTERS[0], None, 0.0),
            ("frame_mlp", models["frame_mlp"], report105.ROUTERS[0], None, 0.0),
            ("gru", models["gru"], report105.ROUTERS[0], None, 0.0),
            ("return_selected_gru", models["gru"], selected_router, None, 0.0),
            ("rollout_window_gru", models["gru"], selected_router, plan_model, selected_bias),
        ):
            row, maybe_trace, tracker = run_episode(
                seed,
                cfg,
                controller,
                model,
                device,
                router,
                plan_net,
                bias,
                trace=(seed == cfg.trace_seed and controller == "rollout_window_gru"),
            )
            eval_rows.append(row)
            crisis_logs[f"{seed}:{controller}:none"] = tracker.response_log
            if controller == "return_selected_gru":
                eval_rows.append(coupled.EvalRow(**{**asdict(row), "controller": "repair_critic_baseline"}))
                crisis_logs[f"{seed}:repair_critic_baseline:none"] = tracker.response_log
            if maybe_trace.frames:
                trace = maybe_trace

        for ablation in ("body", "infrastructure", "tools", "social_culture", "environment", "previous_action"):
            row, _, tracker = run_episode(
                seed,
                cfg,
                "rollout_window_gru",
                models["gru"],
                device,
                selected_router,
                plan_model,
                selected_bias,
                ablation=ablation,
            )
            eval_rows.append(row)
            crisis_logs[f"{seed}:rollout_window_gru:{ablation}"] = tracker.response_log

    summary = coupled.summarize(eval_rows)
    ablations = ablations_from_summary(summary)
    verdict = verdict_from_summary(summary, ablations, selected_router, selected_bias)
    payload = {
        "config": {
            "train_seeds": list(cfg.train_seeds),
            "tune_seeds": list(cfg.tune_seeds),
            "eval_seeds": list(cfg.eval_seeds),
            "hours": cfg.hours,
            "step_hours": cfg.step_hours,
            "population": cfg.population,
            "epochs": cfg.epochs,
            "hidden_size": cfg.hidden_size,
            "plan_epochs": cfg.plan_epochs,
            "plan_hidden_size": cfg.plan_hidden_size,
            "plan_bias_candidates": list(cfg.plan_bias_candidates),
            "max_plan_examples": cfg.max_plan_examples,
            "device": cfg.device,
            "trace_seed": cfg.trace_seed,
        },
        "crisis_profiles": [asdict(profile) for profile in coupled.PROFILES],
        "routers": [asdict(router) for router in report105.ROUTERS],
        "plans": [asdict(plan) for plan in PLAN_TEMPLATES],
        "router_selection": [asdict(row) for row in router_selection],
        "plan_selection": [asdict(row) for row in plan_selection],
        "base_training": [asdict(row) for row in training_rows],
        "plan_training": asdict(plan_training),
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": asdict(trace),
        "crisis_logs": crisis_logs,
        "notes": {
            "claim": "rollout-window sequence control for coupled social/environment crisis pressure",
            "not_claimed": "deep reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
            "input_discipline": "the plan critic consumes ordinary features, plan identity, current/recent response fractions, and crisis-window timing but not active crisis profile labels",
        },
    }
    rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    rows_to_csv(Path(f"{PREFIX}_plan_training.csv"), [plan_training])
    rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    rows_to_csv(Path(f"{PREFIX}_plan_selection.csv"), plan_selection)
    rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    write_json(Path(f"{PREFIX}_results.json"), payload)
    write_json(Path(f"{PREFIX}_trace.json"), asdict(trace))
    write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_ENVIRONMENT_BOTTLENECK_RESULTS", payload)
    write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_ENVIRONMENT_BOTTLENECK_TRACE", asdict(trace))
    return payload


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-seeds", default="20260911,20260912,20260913,20260914,20260915,20260916")
    parser.add_argument("--tune-seeds", default="20261011,20261012,20261013")
    parser.add_argument("--eval-seeds", default="20261021,20261022,20261023,20261024,20261025")
    parser.add_argument("--hours", type=float, default=72.0)
    parser.add_argument("--step-hours", type=float, default=0.10)
    parser.add_argument("--population", type=int, default=14)
    parser.add_argument("--epochs", type=int, default=42)
    parser.add_argument("--hidden-size", type=int, default=64)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--plan-epochs", type=int, default=72)
    parser.add_argument("--plan-hidden-size", type=int, default=72)
    parser.add_argument("--plan-learning-rate", type=float, default=0.003)
    parser.add_argument("--plan-bias-candidates", default="0.00,1.00,1.75,2.75,4.00,5.50,7.00")
    parser.add_argument("--max-plan-examples", type=int, default=160000)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--trace-seed", type=int, default=20261021)
    args = parser.parse_args()
    return Config(
        train_seeds=parse_ints(args.train_seeds),
        tune_seeds=parse_ints(args.tune_seeds),
        eval_seeds=parse_ints(args.eval_seeds),
        hours=args.hours,
        step_hours=args.step_hours,
        population=args.population,
        epochs=args.epochs,
        hidden_size=args.hidden_size,
        learning_rate=args.learning_rate,
        plan_epochs=args.plan_epochs,
        plan_hidden_size=args.plan_hidden_size,
        plan_learning_rate=args.plan_learning_rate,
        plan_bias_candidates=parse_floats(args.plan_bias_candidates),
        max_plan_examples=args.max_plan_examples,
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({"plan_selection": payload["plan_selection"], "verdict": payload["verdict"], "summary": payload["summary"]}, indent=2))
    # A failed rollout-window verdict is evidence, not a process failure.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
