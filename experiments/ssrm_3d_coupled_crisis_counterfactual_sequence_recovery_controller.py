#!/usr/bin/env python3
"""Counterfactual sequence-window recovery for SSRM-3D coupled crises.

Report 127 showed that a scalar completed-window value critic has offline
signal, but one-step action reranking worsens held-out coupled-crisis repair.
This benchmark tests the next stricter shape: train a cloned-rollout plan-value
model over short multi-action windows, then use that window choice to bias a
consequence-trained recurrent crisis policy for several actions at a time.

The controller still has bounded structure. It receives supplied crisis action
candidates and supplied short-window plan templates, and it trains from
simulated counterfactual rollouts in the existing 96h post-12h crisis world. It
does not receive scenario IDs, does not call the engineered weakest-channel
planner during evaluation, and does not claim open-ended civilization, mature
deep RL, subjective consciousness, or real-world competence.
"""

from __future__ import annotations

import argparse
import json
import random
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import torch

import ssrm_3d_coupled_crisis_active_policy_controller as report119
import ssrm_3d_coupled_crisis_active_state_value_controller as report117
import ssrm_3d_coupled_crisis_consequence_recovery_controller as report126
import ssrm_3d_coupled_crisis_joint_arbitration_controller as report113
import ssrm_3d_coupled_crisis_memory_policy_controller as report121
import ssrm_3d_coupled_crisis_min_channel_planner_controller as report123
import ssrm_3d_coupled_crisis_planner_distillation_controller as report124
import ssrm_3d_coupled_crisis_randomized_transfer_controller as report114
import ssrm_3d_coupled_crisis_rollout_window_controller as report111
import ssrm_3d_coupled_social_environment_maturation_controller as coupled
import ssrm_3d_learned_multiday_maturation_controller as base
import ssrm_3d_return_selected_multiday_maturation_controller as report105
from ssrm_maturation.agents import make_agents
from ssrm_maturation.benchmark import TRACE_CHECKPOINTS, Trace, score_episode, snapshot
from ssrm_maturation.environment import clamp, living
from ssrm_maturation.models import CONDITIONS, Agent, Condition, World


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_counterfactual_sequence_recovery"
COUNTERFACTUAL_SEQUENCE_SEED = 20262341
ACTION_CANDIDATES = report126.ACTION_CANDIDATES
ACTION_TO_INDEX = report126.ACTION_TO_INDEX


@dataclass(frozen=True)
class Config:
    train_seeds: Sequence[int]
    tune_seeds: Sequence[int]
    eval_seeds: Sequence[int]
    hours: float = 96.0
    step_hours: float = 0.10
    population: int = 14
    epochs: int = 24
    hidden_size: int = 64
    learning_rate: float = 0.004
    action_epochs: int = 32
    action_hidden_size: int = 64
    action_learning_rate: float = 0.004
    consequence_epochs: int = 14
    consequence_hidden_size: int = 64
    consequence_learning_rate: float = 0.003
    consequence_return_scale: float = 1.15
    plan_epochs: int = 12
    plan_hidden_size: int = 64
    plan_learning_rate: float = 0.003
    max_plan_examples: int = 1024
    student_iterations: int = 1
    student_collection_bias: float = 0.70
    policy_temperature: float = 1.0
    policy_bias_candidates: Sequence[float] = (0.0, 0.20, 0.40, 0.70, 1.00)
    plan_bias_candidates: Sequence[float] = (0.0, 0.25, 0.50, 0.80, 1.10, 1.50)
    plan_commit_actions: int = 42
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class WindowPlanSelectionRow:
    plan_bias: float
    tune_total_score: float
    tune_maturation_score: float
    tune_crisis_score: float
    tune_resolved_rate: float
    tune_env_response: float
    tune_social_response: float
    tune_coupled_response: float
    tune_damage: float
    selection_objective: float
    selected: bool


@dataclass(frozen=True)
class CounterfactualSequenceVerdictRow:
    selected_router: str
    selected_planner: str
    selected_policy_bias: float
    selected_plan_bias: float
    source_sequences: int
    student_sequences: int
    aggregate_examples: int
    consequence_train_accuracy: float
    consequence_weighted_accuracy: float
    plan_train_examples: int
    plan_positive_examples: int
    plan_pairwise_accuracy: float
    counterfactual_total_score: float
    consequence_total_score: float
    min_channel_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    counterfactual_crisis_score: float
    consequence_crisis_score: float
    min_channel_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    counterfactual_resolved_rate: float
    consequence_resolved_rate: float
    min_channel_resolved_rate: float
    fixed_joint_resolved_rate: float
    return_selected_resolved_rate: float
    counterfactual_coupled_response: float
    consequence_coupled_response: float
    min_channel_coupled_response: float
    fixed_joint_coupled_response: float
    return_selected_coupled_response: float
    counterfactual_gain_over_consequence: float
    counterfactual_gain_over_return_selected: float
    counterfactual_gap_to_teacher: float
    counterfactual_gap_to_fixed_joint: float
    social_culture_crisis_loss: float
    environment_crisis_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    mean_crisis_count: float
    supports_counterfactual_sequence_recovery: bool
    supports_teacher_transfer: bool
    supports_social_environment_dependency: bool
    verdict: str


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def parse_ints(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def parse_floats(value: str) -> Tuple[float, ...]:
    return tuple(float(part.strip()) for part in value.split(",") if part.strip())


def current_response_fractions(action_counts: Dict[str, int], alive_count: int) -> Tuple[float, float]:
    denom = max(1, alive_count)
    env = sum(action_counts.get(action, 0) for action in report111.ENV_RESPONSE_ACTIONS) / denom
    social = sum(action_counts.get(action, 0) for action in report111.SOCIAL_RESPONSE_ACTIONS) / denom
    return env, social


def plan_model_scores(
    plan_model: report111.RolloutWindowPlanNet,
    features: Sequence[float],
    active: coupled.ActiveCrisis,
    action_counts: Dict[str, int],
    alive_count: int,
    world_time: float,
    device: torch.device,
    ablation: str,
) -> torch.Tensor:
    masked = report111.diagnostic_features(features, ablation)
    recent_env = active.env_response_steps / max(1, active.steps)
    recent_social = active.social_response_steps / max(1, active.steps)
    elapsed_fraction = clamp((world_time - active.start) / max(1e-6, active.duration))
    remaining_fraction = clamp((active.end - world_time) / max(1e-6, active.duration))
    env_context, social_context = current_response_fractions(action_counts, alive_count)
    rows = [
        report111.plan_input(
            masked,
            plan,
            env_context,
            social_context,
            recent_env,
            recent_social,
            elapsed_fraction,
            remaining_fraction,
        )
        for plan in report111.PLAN_TEMPLATES
    ]
    with torch.no_grad():
        x = torch.tensor(rows, dtype=torch.float32, device=device)
        values = plan_model(x)
    return values


def choose_window_plan(
    plan_model: report111.RolloutWindowPlanNet,
    features: Sequence[float],
    active: coupled.ActiveCrisis,
    action_counts: Dict[str, int],
    alive_count: int,
    world_time: float,
    device: torch.device,
    ablation: str,
) -> Tuple[report111.PlanTemplate, float]:
    values = plan_model_scores(
        plan_model,
        features,
        active,
        action_counts,
        alive_count,
        world_time,
        device,
        ablation,
    )
    index = int(values.argmax().item())
    return report111.PLAN_TEMPLATES[index], float(values[index].detach().cpu().item())


def add_action_bias(raw: Dict[str, float], action: str, amount: float) -> None:
    if action in ACTION_TO_INDEX:
        raw[action] = raw.get(action, 0.0) + amount


def plan_action_bias(
    plan: report111.PlanTemplate,
    features: Sequence[float],
    active: coupled.ActiveCrisis,
    device: torch.device,
    dtype: torch.dtype,
    ablation: str,
    plan_bias: float,
) -> torch.Tensor:
    if plan_bias <= 0.0:
        return torch.zeros((1, len(ACTION_CANDIDATES)), dtype=dtype, device=device)
    masked = report111.diagnostic_features(features, ablation)
    env_fraction = min(1.0, active.env_progress / active.profile.env_need)
    social_fraction = min(1.0, active.social_progress / active.profile.social_need)
    env_gap = 1.0 - env_fraction
    social_gap = 1.0 - social_fraction
    selected_env = report111.plan_environment_action(plan, masked)
    selected_social = report111.plan_social_action(plan, masked)
    raw: Dict[str, float] = {}

    env_drive = plan.env_weight * (0.35 + env_gap * 0.80)
    social_drive = plan.social_weight * (0.35 + social_gap * 0.80)
    add_action_bias(raw, selected_env, env_drive * (1.25 + report111.symptom_fit(masked, selected_env)))
    add_action_bias(raw, selected_social, social_drive * (1.20 + report111.symptom_fit(masked, selected_social)))

    for action in ("sanitize", "treat", "scout", "construct"):
        add_action_bias(raw, action, plan.env_weight * (0.12 + report111.symptom_fit(masked, action) * 0.38))
    add_action_bias(raw, "social_repair", plan.social_weight * (0.18 + report111.symptom_fit(masked, "social_repair") * 0.44))
    add_action_bias(raw, "teach", (plan.teaching_weight + plan.social_weight * 0.18) * (0.18 + report111.symptom_fit(masked, "teach") * 0.35))
    add_action_bias(raw, "learn", (plan.teaching_weight + plan.social_weight * 0.10) * (0.10 + report111.symptom_fit(masked, "learn") * 0.24))
    add_action_bias(raw, "construct", plan.infrastructure_weight * (0.36 + report111.symptom_fit(masked, "construct") * 0.48))

    if plan.sustain_weight >= 0.30:
        add_action_bias(raw, "none", plan.sustain_weight * 0.16)

    values = torch.zeros((1, len(ACTION_CANDIDATES)), dtype=dtype, device=device)
    allowed = set(report119.allowed_indices(ablation))
    for action, amount in raw.items():
        index = ACTION_TO_INDEX.get(action)
        if index is not None and index in allowed:
            values[:, index] += amount
    if torch.any(values):
        values = values - values.mean()
        values = values / (values.std(unbiased=False) + 1e-4)
        values = torch.clamp(values, -1.8, 1.8)
    return values * plan_bias


def choose_counterfactual_sequence_candidate(
    consequence_model: report121.CrisisMemoryPolicyNet,
    plan_model: report111.RolloutWindowPlanNet,
    features: Sequence[float],
    active: coupled.ActiveCrisis,
    action_counts: Dict[str, int],
    alive_count: int,
    world_time: float,
    memory_state: Optional[torch.Tensor],
    plan_state: Dict[str, object],
    device: torch.device,
    ablation: str,
    temperature: float,
    policy_bias: float,
    plan_bias: float,
    plan_commit_actions: int,
) -> Tuple[str, torch.Tensor, report111.PlanTemplate]:
    values = report119.policy_features(features, active, action_counts, alive_count, world_time, ablation)
    plan = plan_state.get("plan")
    remaining = int(plan_state.get("remaining", 0))
    if plan is None or remaining <= 0:
        plan, plan_value = choose_window_plan(
            plan_model,
            features,
            active,
            action_counts,
            alive_count,
            world_time,
            device,
            ablation,
        )
        plan_state["plan"] = plan
        plan_state["plan_value"] = plan_value
        plan_state["remaining"] = max(1, plan_commit_actions)
    with torch.no_grad():
        x = torch.tensor([[values]], dtype=torch.float32, device=device)
        logits, next_state = consequence_model.step(x, memory_state)
        policy_logits = report119.masked_logits(logits / max(0.05, temperature), ablation, policy_bias)
        window_logits = plan_action_bias(
            plan,
            features,
            active,
            device,
            logits.dtype,
            ablation,
            plan_bias,
        )
        combined = report119.masked_logits(policy_logits + window_logits, ablation, 0.0)
        index = int(combined.argmax(dim=-1).item())
    plan_state["remaining"] = int(plan_state.get("remaining", 1)) - 1
    return ACTION_CANDIDATES[index], next_state.detach(), plan


def run_counterfactual_sequence_episode(
    seed: int,
    cfg: Config,
    base_model: base.ControllerNet,
    consequence_model: report121.CrisisMemoryPolicyNet,
    plan_model: report111.RolloutWindowPlanNet,
    device: torch.device,
    router: report105.PressureRouter,
    policy_bias: float,
    plan_bias: float,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, Trace, coupled.CrisisTracker, List[dict[str, object]]]:
    condition = CONDITIONS[0]
    rng = random.Random(
        seed * 131
        + sum(ord(ch) for ch in "counterfactual_sequence_recovery_gru" + router.name + ablation)
        + int(policy_bias * 1000)
        + int(plan_bias * 1000)
        + COUNTERFACTUAL_SEQUENCE_SEED
    )
    agents = make_agents(rng, cfg.population)
    world = coupled.prepare_world(rng, cfg)
    baseline = base.initial_baseline(world, cfg.population)
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
    trace_out = Trace(seed=seed, condition=f"counterfactual_sequence_recovery_gru:{router.name}:policy_{policy_bias:g}:plan_{plan_bias:g}:{ablation}")
    checkpoints = list(TRACE_CHECKPOINTS)
    no_pre_gate_shock = True
    alive_at_12h = cfg.population
    at_12: dict[str, float] = {}
    memory_state: Optional[torch.Tensor] = None
    active_key: Optional[float] = None
    plan_state: Dict[str, object] = {}
    plan_log: List[dict[str, object]] = []

    if trace:
        trace_out.frames.append(snapshot(world, agents, "0h", events))
        if checkpoints and checkpoints[0] == 0.0:
            checkpoints.pop(0)

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        action_counts: Dict[str, int] = {}
        coupled.maybe_start_crisis(world, tracker, rng, events)
        if tracker.active is not None and active_key != tracker.active.start:
            active_key = tracker.active.start
            memory_state = None
            plan_state = {}
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
            nonlocal memory_state, plan_state
            active = tracker.active
            if active is not None:
                before_plan = plan_state.get("plan")
                action, next_state, selected_plan = choose_counterfactual_sequence_candidate(
                    consequence_model,
                    plan_model,
                    features,
                    active,
                    action_counts,
                    len(living(agents)),
                    current_world.time,
                    memory_state,
                    plan_state,
                    device,
                    ablation,
                    cfg.policy_temperature,
                    policy_bias,
                    plan_bias,
                    cfg.plan_commit_actions,
                )
                memory_state = next_state
                if before_plan is None or before_plan != selected_plan:
                    plan_log.append({
                        "hour": current_world.time,
                        "crisis": active.profile.name,
                        "plan": selected_plan.name,
                        "plan_value": float(plan_state.get("plan_value", 0.0)),
                        "ablation": ablation,
                    })
                if action == "none":
                    action = report117.learned_policy_action(agent, features, base_model, recurrent_states, router, device, ablation)
            else:
                action = report117.learned_policy_action(agent, features, base_model, recurrent_states, router, device, ablation)
            if ablation == "environment" and action in report111.ENV_RESPONSE_ACTIONS:
                action = "rest"
            if ablation == "social_culture" and action in report111.SOCIAL_RESPONSE_ACTIONS:
                action = "rest"
            action_counts[action] = action_counts.get(action, 0) + 1
            return action

        base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
        report111.update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
        coupled.complete_crisis_if_due(world, agents, tracker, events)
        if tracker.active is None:
            memory_state = None
            active_key = None
            plan_state = {}
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
            frame["recent_window_plan"] = plan_log[-1]["plan"] if plan_log else None
            trace_out.frames.append(frame)
    if tracker.active is not None:
        coupled.complete_crisis_if_due(world, agents, tracker, events)
    episode = score_episode(world, agents, baseline, at_12, seed, condition, alive_at_12h, no_pre_gate_shock)
    crisis_score, resolved_rate, env_response, social_response, coupled_response = coupled.crisis_metrics(tracker)
    total_score = clamp(episode.maturation_score * 0.52 + crisis_score * 0.48)
    eval_row = coupled.EvalRow(
        seed=seed,
        controller="counterfactual_sequence_recovery_gru",
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
        frame["recent_window_plan"] = plan_log[-1]["plan"] if plan_log else None
        trace_out.frames.append(frame)
    return eval_row, trace_out, tracker, plan_log


def selection_objective(rows: Sequence[coupled.EvalRow]) -> Tuple[float, float, float, float, float, float, float, float, float]:
    total = mean(row.total_score for row in rows)
    maturation = mean(row.maturation_score for row in rows)
    crisis = mean(row.crisis_score for row in rows)
    resolved = mean(row.resolved_rate for row in rows)
    env_response = mean(row.env_response_rate for row in rows)
    social_response = mean(row.social_response_rate for row in rows)
    coupled_response = mean(row.coupled_response_rate for row in rows)
    damage = mean(row.crisis_damage for row in rows)
    balance = 1.0 - abs(env_response - social_response)
    objective = total * 0.36 + crisis * 1.42 + resolved * 0.88 + coupled_response * 1.16 + balance * 0.20 - damage * 0.40
    return total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective


def select_plan_bias(
    cfg: Config,
    base_model: base.ControllerNet,
    consequence_model: report121.CrisisMemoryPolicyNet,
    plan_model: report111.RolloutWindowPlanNet,
    device: torch.device,
    router: report105.PressureRouter,
    policy_bias: float,
) -> Tuple[float, List[WindowPlanSelectionRow]]:
    rows: List[WindowPlanSelectionRow] = []
    best_bias = 0.0
    best_objective = -1e9
    for bias in cfg.plan_bias_candidates:
        eval_rows = [
            run_counterfactual_sequence_episode(
                seed,
                cfg,
                base_model,
                consequence_model,
                plan_model,
                device,
                router,
                policy_bias,
                bias,
            )[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_objective = objective
            best_bias = bias
        rows.append(WindowPlanSelectionRow(
            plan_bias=bias,
            tune_total_score=total,
            tune_maturation_score=maturation,
            tune_crisis_score=crisis,
            tune_resolved_rate=resolved,
            tune_env_response=env_response,
            tune_social_response=social_response,
            tune_coupled_response=coupled_response,
            tune_damage=damage,
            selection_objective=objective,
            selected=False,
        ))
    return best_bias, [replace(row, selected=(row.plan_bias == best_bias)) for row in rows]


def ablations_from_summary(summary: Sequence[coupled.SummaryRow]) -> List[coupled.AblationRow]:
    base_row = coupled.row_lookup(summary, "counterfactual_sequence_recovery_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = coupled.row_lookup(summary, "counterfactual_sequence_recovery_gru", ablation)
        rows.append(coupled.AblationRow(
            ablation=ablation,
            mean_total_score=row.mean_total_score,
            total_loss=base_row.mean_total_score - row.mean_total_score,
            crisis_score_loss=base_row.mean_crisis_score - row.mean_crisis_score,
            resolved_rate_loss=base_row.mean_resolved_rate - row.mean_resolved_rate,
            env_response_loss=base_row.mean_env_response_rate - row.mean_env_response_rate,
            social_response_loss=base_row.mean_social_response_rate - row.mean_social_response_rate,
            coupled_response_loss=base_row.mean_coupled_response_rate - row.mean_coupled_response_rate,
            damage_increase=row.mean_crisis_damage - base_row.mean_crisis_damage,
        ))
    return rows


def transfer_verdict(
    summary: Sequence[coupled.SummaryRow],
    ablations: Sequence[coupled.AblationRow],
    router: report105.PressureRouter,
    planner: report123.PlannerCandidate,
    policy_bias: float,
    plan_bias: float,
    schedules: Sequence[report114.ScheduleRow],
    consequence_training_rows: Sequence[report126.ConsequenceTrainingRow],
    plan_training: report111.PlanTrainingRow,
    source_summary: Sequence[report126.ConsequenceSourceRow],
) -> CounterfactualSequenceVerdictRow:
    counterfactual = coupled.row_lookup(summary, "counterfactual_sequence_recovery_gru", "none")
    consequence = coupled.row_lookup(summary, "consequence_recovery_gru", "none")
    teacher = coupled.row_lookup(summary, "min_channel_planner_gru", "none")
    fixed = coupled.row_lookup(summary, "fixed_joint_gru", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    final_training = consequence_training_rows[-1]
    source_sequences = sum(row.sequences for row in source_summary if not row.source_policy.startswith("student_iteration"))
    student_sequences = sum(row.sequences for row in source_summary if row.source_policy.startswith("student_iteration"))
    supports_recovery = (
        plan_training.pairwise_accuracy >= 0.55
        and mean_crisis_count >= 4.0
        and counterfactual.mean_total_score - consequence.mean_total_score >= 0.010
        and counterfactual.mean_crisis_score - consequence.mean_crisis_score >= 0.020
        and counterfactual.mean_crisis_score - returned.mean_crisis_score >= 0.040
        and counterfactual.mean_resolved_rate - returned.mean_resolved_rate >= 0.080
        and counterfactual.mean_coupled_response_rate - returned.mean_coupled_response_rate >= 0.080
        and counterfactual.mean_alive_at_12h >= 12.0
        and counterfactual.shock_gate_pass_rate == 1.0
        and counterfactual.post_gate_shock_rate == 1.0
    )
    supports_teacher = (
        counterfactual.mean_crisis_score >= 0.35
        and counterfactual.mean_coupled_response_rate >= 0.40
        and teacher.mean_crisis_score - counterfactual.mean_crisis_score <= 0.30
    )
    supports_dependency = (
        counterfactual.mean_crisis_score > 0.0
        and social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    return CounterfactualSequenceVerdictRow(
        selected_router=router.name,
        selected_planner=planner.name,
        selected_policy_bias=policy_bias,
        selected_plan_bias=plan_bias,
        source_sequences=source_sequences,
        student_sequences=student_sequences,
        aggregate_examples=final_training.aggregate_examples,
        consequence_train_accuracy=final_training.train_accuracy,
        consequence_weighted_accuracy=final_training.weighted_train_accuracy,
        plan_train_examples=plan_training.train_examples,
        plan_positive_examples=plan_training.positive_examples,
        plan_pairwise_accuracy=plan_training.pairwise_accuracy,
        counterfactual_total_score=counterfactual.mean_total_score,
        consequence_total_score=consequence.mean_total_score,
        min_channel_total_score=teacher.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        counterfactual_crisis_score=counterfactual.mean_crisis_score,
        consequence_crisis_score=consequence.mean_crisis_score,
        min_channel_crisis_score=teacher.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        counterfactual_resolved_rate=counterfactual.mean_resolved_rate,
        consequence_resolved_rate=consequence.mean_resolved_rate,
        min_channel_resolved_rate=teacher.mean_resolved_rate,
        fixed_joint_resolved_rate=fixed.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        counterfactual_coupled_response=counterfactual.mean_coupled_response_rate,
        consequence_coupled_response=consequence.mean_coupled_response_rate,
        min_channel_coupled_response=teacher.mean_coupled_response_rate,
        fixed_joint_coupled_response=fixed.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        counterfactual_gain_over_consequence=counterfactual.mean_total_score - consequence.mean_total_score,
        counterfactual_gain_over_return_selected=counterfactual.mean_total_score - returned.mean_total_score,
        counterfactual_gap_to_teacher=teacher.mean_total_score - counterfactual.mean_total_score,
        counterfactual_gap_to_fixed_joint=fixed.mean_total_score - counterfactual.mean_total_score,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=counterfactual.shock_gate_pass_rate,
        post_gate_shock_rate=counterfactual.post_gate_shock_rate,
        survival_at_12h=counterfactual.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_counterfactual_sequence_recovery=supports_recovery,
        supports_teacher_transfer=supports_teacher,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_recovery and supports_teacher and supports_dependency else "partial_or_failed",
    )


def run_benchmark(cfg: Config) -> dict[str, object]:
    device = base.resolve_device(cfg.device)
    schedule_builder = report114.randomized_schedule_builder(cfg.hours)
    schedules = (
        report114.schedule_rows(cfg, "train", cfg.train_seeds, schedule_builder)
        + report114.schedule_rows(cfg, "tune", cfg.tune_seeds, schedule_builder)
        + report114.schedule_rows(cfg, "eval", cfg.eval_seeds, schedule_builder)
    )
    with report114.patched_transfer_world(schedule_builder, report114.randomized_prepare_world):
        sequences, labels = base.collect_sequences(cfg)
        x, y, mask = base.build_tensors(sequences, labels, device)
        training_rows: List[base.TrainingRow] = []
        models: Dict[str, base.ControllerNet] = {}
        for architecture in ("frame_mlp", "gru"):
            model, row = base.train_model(architecture, x, y, mask, cfg, device)
            models[architecture] = model
            training_rows.append(row)

        selected_router, router_selection = coupled.select_router(cfg, models["gru"], device)
        env_sequences, env_labels, social_sequences, social_labels, flags = report113.collect_joint_sequences(cfg)
        env_model, env_training = report113.train_action_model(
            cfg,
            device,
            "environment",
            env_sequences,
            env_labels,
            flags,
            20261851,
        )
        social_model, social_training = report113.train_action_model(
            cfg,
            device,
            "social",
            social_sequences,
            social_labels,
            flags,
            20261852,
        )
        selected_planner, planner_selection = report123.select_planner(
            cfg,
            models["gru"],
            env_model,
            social_model,
            device,
            selected_router,
        )
        aggregate = report126.collect_behavior_sequences(
            cfg,
            models["gru"],
            env_model,
            social_model,
            device,
            selected_router,
            selected_planner,
        )
        consequence_model, consequence_training = report126.train_consequence_policy(
            cfg,
            aggregate,
            device,
            0,
            "behavior_sources",
        )
        consequence_training_rows = [consequence_training]
        for iteration in range(1, cfg.student_iterations + 1):
            student_sequences = report126.collect_student_sequences(
                cfg,
                models["gru"],
                consequence_model,
                device,
                selected_router,
                iteration,
            )
            aggregate.extend(student_sequences)
            consequence_model, row = report126.train_consequence_policy(
                cfg,
                aggregate,
                device,
                iteration,
                f"student_iteration_{iteration}",
            )
            consequence_training_rows.append(row)
        source_summary = report126.source_rows(aggregate)
        plan_model, plan_training = report111.train_plan_model(cfg, device)
        selected_policy_bias, policy_selection = report126.select_policy_bias(
            cfg,
            models["gru"],
            consequence_model,
            device,
            selected_router,
        )
        selected_plan_bias, plan_selection = select_plan_bias(
            cfg,
            models["gru"],
            consequence_model,
            plan_model,
            device,
            selected_router,
            selected_policy_bias,
        )

        eval_rows: List[coupled.EvalRow] = []
        crisis_logs: Dict[str, object] = {}
        plan_logs: Dict[str, object] = {}
        trace_out: Optional[Trace] = None
        for seed in cfg.eval_seeds:
            for controller, model, router in (
                ("designed", None, report105.ROUTERS[0]),
                ("reactive", None, report105.ROUTERS[0]),
                ("frame_mlp", models["frame_mlp"], report105.ROUTERS[0]),
                ("gru", models["gru"], report105.ROUTERS[0]),
                ("return_selected_gru", models["gru"], selected_router),
            ):
                row, maybe_trace, tracker = coupled.run_episode(
                    seed,
                    cfg,
                    controller,
                    model,
                    device,
                    router,
                    trace=(seed == cfg.trace_seed and controller == "return_selected_gru"),
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:{controller}:none"] = tracker.response_log
                if seed == cfg.trace_seed and controller == "return_selected_gru":
                    trace_out = maybe_trace
            fixed_row = report123.run_fixed_joint_episode(
                seed,
                cfg,
                models["gru"],
                env_model,
                social_model,
                device,
                selected_router,
            )
            eval_rows.append(fixed_row)
            min_row, _, min_tracker = report123.run_min_channel_episode(
                seed,
                cfg,
                models["gru"],
                env_model,
                social_model,
                device,
                selected_router,
                selected_planner,
            )
            eval_rows.append(min_row)
            crisis_logs[f"{seed}:min_channel_planner_gru:none"] = min_tracker.response_log
            consequence_row, _, consequence_tracker = report126.run_consequence_episode(
                seed,
                cfg,
                models["gru"],
                consequence_model,
                device,
                selected_router,
                selected_policy_bias,
            )
            eval_rows.append(consequence_row)
            crisis_logs[f"{seed}:consequence_recovery_gru:none"] = consequence_tracker.response_log
            counter_row, maybe_trace, counter_tracker, counter_plan_log = run_counterfactual_sequence_episode(
                seed,
                cfg,
                models["gru"],
                consequence_model,
                plan_model,
                device,
                selected_router,
                selected_policy_bias,
                selected_plan_bias,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(counter_row)
            crisis_logs[f"{seed}:counterfactual_sequence_recovery_gru:none"] = counter_tracker.response_log
            plan_logs[f"{seed}:counterfactual_sequence_recovery_gru:none"] = counter_plan_log
            if seed == cfg.trace_seed:
                trace_out = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker, log = run_counterfactual_sequence_episode(
                    seed,
                    cfg,
                    models["gru"],
                    consequence_model,
                    plan_model,
                    device,
                    selected_router,
                    selected_policy_bias,
                    selected_plan_bias,
                    ablation=ablation,
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:counterfactual_sequence_recovery_gru:{ablation}"] = tracker.response_log
                plan_logs[f"{seed}:counterfactual_sequence_recovery_gru:{ablation}"] = log

        summary = coupled.summarize(eval_rows)
        ablations = ablations_from_summary(summary)
        verdict = transfer_verdict(
            summary,
            ablations,
            selected_router,
            selected_planner,
            selected_policy_bias,
            selected_plan_bias,
            schedules,
            consequence_training_rows,
            plan_training,
            source_summary,
        )

    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "counterfactual_sequence_recovery_gru", "frames": []}
    trace_payload["condition"] = "counterfactual_sequence_recovery_gru"
    payload = {
        "experiment": "ssrm_3d_coupled_crisis_counterfactual_sequence_recovery",
        "config": asdict(cfg),
        "claim": {
            "tested": "cloned-rollout counterfactual plan-window values can bias a consequence-trained recurrent crisis policy and preserve coupled repair after engineered planner removal",
            "remaining_structure": "short-window plan templates, crisis action candidates, and behavior sources are supplied; this is bounded sequence recovery, not open-ended deep RL",
        },
        "action_candidates": list(ACTION_CANDIDATES),
        "plan_templates": [asdict(plan) for plan in report111.PLAN_TEMPLATES],
        "source_policies": [
            {"name": name, "env_quota": env, "social_quota": social, "strength": strength}
            for name, env, social, strength in report126.SOURCE_POLICIES
        ],
        "schedule": [asdict(row) for row in schedules],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "router_selection": [asdict(row) for row in router_selection],
        "planner_selection": [asdict(row) for row in planner_selection],
        "source_summary": [asdict(row) for row in source_summary],
        "consequence_training": [asdict(row) for row in consequence_training_rows],
        "plan_training": asdict(plan_training),
        "policy_selection": [asdict(row) for row in policy_selection],
        "plan_selection": [asdict(row) for row in plan_selection],
        "eval": [asdict(row) for row in eval_rows],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace_payload,
        "crisis_logs": crisis_logs,
        "plan_logs": plan_logs,
    }
    report124.rows_to_csv(Path(f"{PREFIX}_schedule.csv"), schedules)
    report124.rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_action_training.csv"), [env_training, social_training])
    report124.rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_planner_selection.csv"), planner_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_source_summary.csv"), source_summary)
    report124.rows_to_csv(Path(f"{PREFIX}_consequence_training.csv"), consequence_training_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_plan_training.csv"), [plan_training])
    report124.rows_to_csv(Path(f"{PREFIX}_policy_selection.csv"), policy_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_plan_selection.csv"), plan_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    report124.rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    report124.rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    report124.write_json(Path(f"{PREFIX}_results.json"), payload)
    report124.write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    report124.write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_COUNTERFACTUAL_SEQUENCE_RECOVERY_RESULTS", payload)
    report124.write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_COUNTERFACTUAL_SEQUENCE_RECOVERY_TRACE", trace_payload)
    return payload


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-seeds", default="20260911,20260912,20260913")
    parser.add_argument("--tune-seeds", default="20261111,20261112")
    parser.add_argument("--eval-seeds", default="20261121,20261122,20261123")
    parser.add_argument("--hours", type=float, default=96.0)
    parser.add_argument("--step-hours", type=float, default=0.10)
    parser.add_argument("--population", type=int, default=14)
    parser.add_argument("--epochs", type=int, default=24)
    parser.add_argument("--hidden-size", type=int, default=64)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--action-epochs", type=int, default=32)
    parser.add_argument("--action-hidden-size", type=int, default=64)
    parser.add_argument("--action-learning-rate", type=float, default=0.004)
    parser.add_argument("--consequence-epochs", type=int, default=14)
    parser.add_argument("--consequence-hidden-size", type=int, default=64)
    parser.add_argument("--consequence-learning-rate", type=float, default=0.003)
    parser.add_argument("--consequence-return-scale", type=float, default=1.15)
    parser.add_argument("--plan-epochs", type=int, default=12)
    parser.add_argument("--plan-hidden-size", type=int, default=64)
    parser.add_argument("--plan-learning-rate", type=float, default=0.003)
    parser.add_argument("--max-plan-examples", type=int, default=1024)
    parser.add_argument("--student-iterations", type=int, default=1)
    parser.add_argument("--student-collection-bias", type=float, default=0.70)
    parser.add_argument("--policy-temperature", type=float, default=1.0)
    parser.add_argument("--policy-bias-candidates", default="0.0,0.20,0.40,0.70,1.00")
    parser.add_argument("--plan-bias-candidates", default="0.0,0.25,0.50,0.80,1.10,1.50")
    parser.add_argument("--plan-commit-actions", type=int, default=42)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--trace-seed", type=int, default=20261121)
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
        action_epochs=args.action_epochs,
        action_hidden_size=args.action_hidden_size,
        action_learning_rate=args.action_learning_rate,
        consequence_epochs=args.consequence_epochs,
        consequence_hidden_size=args.consequence_hidden_size,
        consequence_learning_rate=args.consequence_learning_rate,
        consequence_return_scale=args.consequence_return_scale,
        plan_epochs=args.plan_epochs,
        plan_hidden_size=args.plan_hidden_size,
        plan_learning_rate=args.plan_learning_rate,
        max_plan_examples=args.max_plan_examples,
        student_iterations=args.student_iterations,
        student_collection_bias=args.student_collection_bias,
        policy_temperature=args.policy_temperature,
        policy_bias_candidates=parse_floats(args.policy_bias_candidates),
        plan_bias_candidates=parse_floats(args.plan_bias_candidates),
        plan_commit_actions=args.plan_commit_actions,
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "source_summary": payload["source_summary"],
        "consequence_training": payload["consequence_training"],
        "plan_training": payload["plan_training"],
        "policy_selection": payload["policy_selection"],
        "plan_selection": payload["plan_selection"],
        "verdict": payload["verdict"],
        "summary": payload["summary"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
