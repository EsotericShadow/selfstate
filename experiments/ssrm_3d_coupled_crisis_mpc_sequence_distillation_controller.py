#!/usr/bin/env python3
"""Distill MPC sequence repair into a recurrent crisis policy.

Report 131 showed that cloned-rollout model-predictive sequence commitment can
recover much of the missing coupled environmental/social repair shape, but the
controller still receives supplied plan templates and simulator lookahead at
decision time.

This benchmark tests the next narrower claim: can the MPC teacher's crisis
actions be distilled into a recurrent policy and then evaluated without calling
the rollout scorer? This is bounded distillation evidence, not open-ended
civilization, subjective consciousness, unsupplied action discovery, or mature
deep reinforcement learning.
"""

from __future__ import annotations

import argparse
import json
import random
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import torch
import torch.nn.functional as F

import ssrm_3d_coupled_crisis_active_policy_controller as report119
import ssrm_3d_coupled_crisis_active_state_value_controller as report117
import ssrm_3d_coupled_crisis_consequence_recovery_controller as report126
import ssrm_3d_coupled_crisis_joint_arbitration_controller as report113
import ssrm_3d_coupled_crisis_memory_policy_controller as report121
import ssrm_3d_coupled_crisis_min_channel_planner_controller as report123
import ssrm_3d_coupled_crisis_mpc_sequence_optimizer_controller as report131
import ssrm_3d_coupled_crisis_planner_distillation_controller as report124
import ssrm_3d_coupled_crisis_randomized_transfer_controller as report114
import ssrm_3d_coupled_crisis_rollout_window_controller as report111
import ssrm_3d_coupled_social_environment_maturation_controller as coupled
import ssrm_3d_learned_multiday_maturation_controller as base
import ssrm_3d_return_selected_multiday_maturation_controller as report105
from ssrm_maturation.agents import make_agents
from ssrm_maturation.benchmark import Trace
from ssrm_maturation.environment import living
from ssrm_maturation.models import CONDITIONS, Agent, Condition, World


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_mpc_sequence_distillation"
MPC_DISTILLATION_SEED = 20262741
ACTION_CANDIDATES = report121.ACTION_CANDIDATES
ACTION_TO_INDEX = report121.ACTION_TO_INDEX


@dataclass(frozen=True)
class Config:
    train_seeds: Sequence[int]
    tune_seeds: Sequence[int]
    eval_seeds: Sequence[int]
    hours: float = 96.0
    step_hours: float = 0.10
    population: int = 14
    epochs: int = 14
    hidden_size: int = 48
    learning_rate: float = 0.004
    action_epochs: int = 18
    action_hidden_size: int = 48
    action_learning_rate: float = 0.004
    consequence_epochs: int = 8
    consequence_hidden_size: int = 48
    consequence_learning_rate: float = 0.003
    consequence_return_scale: float = 1.15
    student_iterations: int = 0
    student_collection_bias: float = 0.70
    distill_epochs: int = 10
    distill_hidden_size: int = 64
    distill_learning_rate: float = 0.003
    class_balance_power: float = 0.35
    teacher_commit_actions: int = 14
    policy_temperature: float = 1.0
    policy_bias_candidates: Sequence[float] = (0.0, 0.40, 0.80, 1.20)
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class MpcTeacherRow:
    sequences: int
    examples: int
    env_action_fraction: float
    social_action_fraction: float
    none_fraction: float
    mean_sequence_length: float
    teacher_commit_actions: int


@dataclass(frozen=True)
class MpcDistillationTrainingRow:
    sequences: int
    examples: int
    distill_epochs: int
    final_loss: float
    train_accuracy: float
    balanced_train_accuracy: float
    env_action_fraction: float
    social_action_fraction: float
    none_fraction: float
    mean_sequence_length: float
    class_balance_power: float
    device_used: str
    parameter_count: int


@dataclass(frozen=True)
class MpcDistillationSelectionRow:
    policy_bias: float
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
class MpcDistillationVerdictRow:
    selected_router: str
    selected_planner: str
    selected_consequence_bias: float
    selected_policy_bias: float
    teacher_commit_actions: int
    teacher_sequences: int
    training_examples: int
    distillation_train_accuracy: float
    distillation_balanced_accuracy: float
    distilled_total_score: float
    mpc_teacher_total_score: float
    consequence_total_score: float
    min_channel_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    distilled_crisis_score: float
    mpc_teacher_crisis_score: float
    consequence_crisis_score: float
    min_channel_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    distilled_resolved_rate: float
    mpc_teacher_resolved_rate: float
    consequence_resolved_rate: float
    return_selected_resolved_rate: float
    distilled_coupled_response: float
    mpc_teacher_coupled_response: float
    consequence_coupled_response: float
    return_selected_coupled_response: float
    distilled_gain_over_consequence: float
    distilled_gain_over_return_selected: float
    distilled_gap_to_mpc_teacher: float
    social_culture_crisis_loss: float
    environment_crisis_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    mean_crisis_count: float
    supports_mpc_distillation: bool
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


def sequence_stats(sequences: Sequence[Sequence[Tuple[List[float], int]]]) -> Tuple[int, int, float, float, float, float]:
    counts = {action: 0 for action in ACTION_CANDIDATES}
    total = 0
    for sequence in sequences:
        for _, index in sequence:
            counts[ACTION_CANDIDATES[index]] += 1
            total += 1
    env_count = sum(counts.get(action, 0) for action in report111.ENV_RESPONSE_ACTIONS)
    social_count = sum(counts.get(action, 0) for action in report111.SOCIAL_RESPONSE_ACTIONS)
    return (
        len(sequences),
        total,
        env_count / max(1, total),
        social_count / max(1, total),
        counts.get("none", 0) / max(1, total),
        mean(len(sequence) for sequence in sequences),
    )


def class_weights(
    sequences: Sequence[Sequence[Tuple[List[float], int]]],
    power: float,
    device: torch.device,
) -> torch.Tensor:
    counts = torch.ones(len(ACTION_CANDIDATES), dtype=torch.float32)
    for sequence in sequences:
        for _, index in sequence:
            counts[index] += 1.0
    weights = counts.sum() / counts
    weights = torch.pow(weights / weights.mean(), power)
    weights = torch.clamp(weights, 0.35, 4.0)
    return weights.to(device)


def collect_mpc_teacher_sequences(
    cfg: Config,
    base_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[List[List[Tuple[List[float], int]]], List[report131.MpcPlanUseRow]]:
    sequences: List[List[Tuple[List[float], int]]] = []
    plan_logs: Dict[str, object] = {}
    condition = CONDITIONS[0]
    for seed in cfg.train_seeds:
        rng = random.Random(seed * 181 + MPC_DISTILLATION_SEED)
        agents = make_agents(rng, cfg.population)
        world = coupled.prepare_world(rng, cfg)
        previous_actions: Dict[str, int] = {}
        recurrent_states: Dict[str, torch.Tensor] = {}
        events: List[str] = []
        tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
        active_key: Optional[float] = None
        pending: List[Tuple[List[float], int]] = []
        plan_state: Dict[str, object] = {}
        seed_plan_log: List[dict[str, object]] = []

        while world.time < cfg.hours - 1e-9:
            dt = min(cfg.step_hours, cfg.hours - world.time)
            action_counts: Dict[str, int] = {}
            coupled.maybe_start_crisis(world, tracker, rng, events)
            if tracker.active is not None and active_key != tracker.active.start:
                if pending:
                    sequences.append(pending)
                pending = []
                active_key = tracker.active.start
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
                active = tracker.active
                if active is not None and current_world.time >= 12.0:
                    values = report119.policy_features(
                        features,
                        active,
                        action_counts,
                        len(living(agents)),
                        current_world.time,
                        "none",
                    )
                    plan = report131.update_plan_state(
                        plan_state,
                        seed,
                        current_world,
                        agents,
                        tracker,
                        previous_actions,
                        cfg,
                        cfg.teacher_commit_actions,
                        "none",
                        seed_plan_log,
                    )
                    action = report131.masked_plan_action(plan, active, features, current_rng, "none")
                    plan_state["remaining"] = int(plan_state.get("remaining", 1)) - 1
                    if action == "none":
                        action = report117.learned_policy_action(
                            agent,
                            features,
                            base_model,
                            recurrent_states,
                            router,
                            device,
                            "none",
                        )
                    label = action if action in ACTION_TO_INDEX else "none"
                    pending.append((values, ACTION_TO_INDEX[label]))
                else:
                    action = report117.learned_policy_action(
                        agent,
                        features,
                        base_model,
                        recurrent_states,
                        router,
                        device,
                        "none",
                    )
                action_counts[action] = action_counts.get(action, 0) + 1
                return action

            base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
            report111.update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
            coupled.complete_crisis_if_due(world, agents, tracker, events)
            if tracker.active is None:
                active_key = None
                plan_state = {}
                if pending:
                    sequences.append(pending)
                    pending = []
        if pending:
            sequences.append(pending)
        plan_logs[f"{seed}:mpc_teacher:none"] = seed_plan_log
    return sequences, report131.plan_use_rows(plan_logs)


def train_distilled_policy(
    cfg: Config,
    sequences: Sequence[Sequence[Tuple[List[float], int]]],
    device: torch.device,
) -> Tuple[report121.CrisisMemoryPolicyNet, MpcDistillationTrainingRow]:
    if not sequences:
        raise RuntimeError("no MPC teacher sequences collected")
    torch.manual_seed(MPC_DISTILLATION_SEED)
    model = report121.CrisisMemoryPolicyNet(cfg.distill_hidden_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.distill_learning_rate)
    weights = class_weights(sequences, cfg.class_balance_power, device)
    final_loss = 0.0
    for _ in range(cfg.distill_epochs):
        for sequence in sequences:
            x = torch.tensor([[item[0] for item in sequence]], dtype=torch.float32, device=device)
            y = torch.tensor([item[1] for item in sequence], dtype=torch.long, device=device)
            logits, _ = model.forward_sequence(x)
            logits = report119.masked_logits(logits.squeeze(0), "none", 0.0)
            loss = F.cross_entropy(logits, y, weight=weights)
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 2.0)
            optimizer.step()
            final_loss = float(loss.detach().cpu().item())
    model.eval()
    correct = 0
    total = 0
    per_class_correct = {action: 0 for action in ACTION_CANDIDATES}
    per_class_total = {action: 0 for action in ACTION_CANDIDATES}
    counts = {action: 0 for action in ACTION_CANDIDATES}
    with torch.no_grad():
        for sequence in sequences:
            x = torch.tensor([[item[0] for item in sequence]], dtype=torch.float32, device=device)
            y = torch.tensor([item[1] for item in sequence], dtype=torch.long, device=device)
            logits, _ = model.forward_sequence(x)
            pred = report119.masked_logits(logits.squeeze(0), "none", 0.0).argmax(dim=-1)
            correct += int((pred == y).sum().item())
            total += int(y.numel())
            for expected, actual in zip(y.detach().cpu().tolist(), pred.detach().cpu().tolist()):
                action = ACTION_CANDIDATES[expected]
                counts[action] += 1
                per_class_total[action] += 1
                if expected == actual:
                    per_class_correct[action] += 1
    active_classes = [action for action, count in per_class_total.items() if count > 0]
    balanced_accuracy = mean(per_class_correct[action] / per_class_total[action] for action in active_classes)
    env_count = sum(counts.get(action, 0) for action in report111.ENV_RESPONSE_ACTIONS)
    social_count = sum(counts.get(action, 0) for action in report111.SOCIAL_RESPONSE_ACTIONS)
    none_count = counts.get("none", 0)
    return model, MpcDistillationTrainingRow(
        sequences=len(sequences),
        examples=total,
        distill_epochs=cfg.distill_epochs,
        final_loss=final_loss,
        train_accuracy=correct / max(1, total),
        balanced_train_accuracy=balanced_accuracy,
        env_action_fraction=env_count / max(1, total),
        social_action_fraction=social_count / max(1, total),
        none_fraction=none_count / max(1, total),
        mean_sequence_length=mean(len(sequence) for sequence in sequences),
        class_balance_power=cfg.class_balance_power,
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in model.parameters()),
    )


def run_distilled_episode(
    seed: int,
    cfg: Config,
    model: base.ControllerNet,
    distilled_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
    policy_bias: float,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, Trace, coupled.CrisisTracker]:
    row, trace_out, tracker = report121.run_memory_policy_episode(
        seed,
        cfg,
        "memory_policy_gru",
        model,
        distilled_model,
        device,
        router,
        policy_bias=policy_bias,
        ablation=ablation,
        trace=trace,
    )
    row = replace(row, controller="mpc_sequence_distilled_gru")
    trace_out.condition = f"mpc_sequence_distilled_gru:{router.name}:bias_{policy_bias:g}:{ablation}"
    return row, trace_out, tracker


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
    objective = total * 0.34 + crisis * 1.35 + resolved * 0.80 + coupled_response * 1.10 + balance * 0.14 - damage * 0.35
    return total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective


def select_policy_bias(
    cfg: Config,
    model: base.ControllerNet,
    distilled_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[float, List[MpcDistillationSelectionRow]]:
    best_bias = 0.0
    best_objective = -1e9
    rows: List[MpcDistillationSelectionRow] = []
    for bias in cfg.policy_bias_candidates:
        eval_rows = [
            run_distilled_episode(seed, cfg, model, distilled_model, device, router, bias)[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_objective = objective
            best_bias = bias
        rows.append(MpcDistillationSelectionRow(
            policy_bias=bias,
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
    return best_bias, [replace(row, selected=(row.policy_bias == best_bias)) for row in rows]


def ablations_from_summary(summary: Sequence[coupled.SummaryRow]) -> List[coupled.AblationRow]:
    base_row = coupled.row_lookup(summary, "mpc_sequence_distilled_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = coupled.row_lookup(summary, "mpc_sequence_distilled_gru", ablation)
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
    consequence_bias: float,
    policy_bias: float,
    schedules: Sequence[report114.ScheduleRow],
    teacher: MpcTeacherRow,
    training: MpcDistillationTrainingRow,
) -> MpcDistillationVerdictRow:
    distilled = coupled.row_lookup(summary, "mpc_sequence_distilled_gru", "none")
    mpc_teacher = coupled.row_lookup(summary, "mpc_sequence_optimizer_gru", "none")
    consequence = coupled.row_lookup(summary, "consequence_recovery_gru", "none")
    min_channel = coupled.row_lookup(summary, "min_channel_planner_gru", "none")
    fixed = coupled.row_lookup(summary, "fixed_joint_gru", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    supports_distill = (
        training.balanced_train_accuracy >= 0.35
        and mean_crisis_count >= 4.0
        and distilled.mean_total_score - returned.mean_total_score >= 0.010
        and distilled.mean_crisis_score - returned.mean_crisis_score >= 0.040
        and distilled.mean_resolved_rate - returned.mean_resolved_rate >= 0.080
        and distilled.mean_coupled_response_rate - returned.mean_coupled_response_rate >= 0.080
        and distilled.mean_alive_at_12h >= 12.0
        and distilled.shock_gate_pass_rate == 1.0
        and distilled.post_gate_shock_rate == 1.0
    )
    supports_teacher = (
        distilled.mean_crisis_score >= 0.35
        and distilled.mean_coupled_response_rate >= 0.40
        and mpc_teacher.mean_crisis_score - distilled.mean_crisis_score <= 0.15
    )
    supports_dependency = (
        distilled.mean_crisis_score > 0.0
        and social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    return MpcDistillationVerdictRow(
        selected_router=router.name,
        selected_planner=planner.name,
        selected_consequence_bias=consequence_bias,
        selected_policy_bias=policy_bias,
        teacher_commit_actions=teacher.teacher_commit_actions,
        teacher_sequences=teacher.sequences,
        training_examples=training.examples,
        distillation_train_accuracy=training.train_accuracy,
        distillation_balanced_accuracy=training.balanced_train_accuracy,
        distilled_total_score=distilled.mean_total_score,
        mpc_teacher_total_score=mpc_teacher.mean_total_score,
        consequence_total_score=consequence.mean_total_score,
        min_channel_total_score=min_channel.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        distilled_crisis_score=distilled.mean_crisis_score,
        mpc_teacher_crisis_score=mpc_teacher.mean_crisis_score,
        consequence_crisis_score=consequence.mean_crisis_score,
        min_channel_crisis_score=min_channel.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        distilled_resolved_rate=distilled.mean_resolved_rate,
        mpc_teacher_resolved_rate=mpc_teacher.mean_resolved_rate,
        consequence_resolved_rate=consequence.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        distilled_coupled_response=distilled.mean_coupled_response_rate,
        mpc_teacher_coupled_response=mpc_teacher.mean_coupled_response_rate,
        consequence_coupled_response=consequence.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        distilled_gain_over_consequence=distilled.mean_total_score - consequence.mean_total_score,
        distilled_gain_over_return_selected=distilled.mean_total_score - returned.mean_total_score,
        distilled_gap_to_mpc_teacher=mpc_teacher.mean_total_score - distilled.mean_total_score,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=distilled.shock_gate_pass_rate,
        post_gate_shock_rate=distilled.post_gate_shock_rate,
        survival_at_12h=distilled.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_mpc_distillation=supports_distill,
        supports_teacher_transfer=supports_teacher,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_distill and supports_teacher and supports_dependency else "partial_or_failed",
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
            20262751,
        )
        social_model, social_training = report113.train_action_model(
            cfg,
            device,
            "social",
            social_sequences,
            social_labels,
            flags,
            20262752,
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
        selected_consequence_bias, consequence_selection = report126.select_policy_bias(
            cfg,
            models["gru"],
            consequence_model,
            device,
            selected_router,
        )
        teacher_sequences, plan_use = collect_mpc_teacher_sequences(cfg, models["gru"], device, selected_router)
        seqs, examples, env_fraction, social_fraction, none_fraction, mean_length = sequence_stats(teacher_sequences)
        teacher_summary = MpcTeacherRow(
            sequences=seqs,
            examples=examples,
            env_action_fraction=env_fraction,
            social_action_fraction=social_fraction,
            none_fraction=none_fraction,
            mean_sequence_length=mean_length,
            teacher_commit_actions=cfg.teacher_commit_actions,
        )
        distilled_model, distill_training = train_distilled_policy(cfg, teacher_sequences, device)
        selected_bias, policy_selection = select_policy_bias(
            cfg,
            models["gru"],
            distilled_model,
            device,
            selected_router,
        )

        eval_rows: List[coupled.EvalRow] = []
        crisis_logs: Dict[str, object] = {}
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
                if maybe_trace.frames:
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
                selected_consequence_bias,
            )
            eval_rows.append(consequence_row)
            crisis_logs[f"{seed}:consequence_recovery_gru:none"] = consequence_tracker.response_log
            mpc_row, maybe_trace, mpc_tracker, _ = report131.run_mpc_sequence_episode(
                seed,
                cfg,
                models["gru"],
                device,
                selected_router,
                cfg.teacher_commit_actions,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(mpc_row)
            crisis_logs[f"{seed}:mpc_sequence_optimizer_gru:none"] = mpc_tracker.response_log
            if maybe_trace.frames:
                trace_out = maybe_trace
            distilled_row, maybe_trace, distilled_tracker = run_distilled_episode(
                seed,
                cfg,
                models["gru"],
                distilled_model,
                device,
                selected_router,
                selected_bias,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(distilled_row)
            crisis_logs[f"{seed}:mpc_sequence_distilled_gru:none"] = distilled_tracker.response_log
            if maybe_trace.frames:
                trace_out = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker = run_distilled_episode(
                    seed,
                    cfg,
                    models["gru"],
                    distilled_model,
                    device,
                    selected_router,
                    selected_bias,
                    ablation=ablation,
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:mpc_sequence_distilled_gru:{ablation}"] = tracker.response_log

    summary = coupled.summarize(eval_rows)
    ablations = ablations_from_summary(summary)
    verdict = transfer_verdict(
        summary,
        ablations,
        selected_router,
        selected_planner,
        selected_consequence_bias,
        selected_bias,
        schedules,
        teacher_summary,
        distill_training,
    )
    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "mpc_sequence_distilled_gru", "frames": []}
    payload = {
        "experiment": "ssrm_3d_coupled_crisis_mpc_sequence_distillation",
        "config": asdict(cfg),
        "claim": {
            "tested": "MPC sequence repair behavior can be distilled into a recurrent policy and evaluated without cloned rollout scoring",
            "remaining_structure": "MPC teacher traces use supplied plan templates and simulator rollout scoring; the student still receives supplied crisis action candidates",
        },
        "plan_templates": [asdict(plan) for plan in report111.PLAN_TEMPLATES],
        "schedule": [asdict(row) for row in schedules],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "router_selection": [asdict(row) for row in router_selection],
        "planner_selection": [asdict(row) for row in planner_selection],
        "consequence_training": [asdict(row) for row in consequence_training_rows],
        "consequence_selection": [asdict(row) for row in consequence_selection],
        "teacher_summary": asdict(teacher_summary),
        "teacher_plan_use": [asdict(row) for row in plan_use],
        "distillation_training": asdict(distill_training),
        "policy_selection": [asdict(row) for row in policy_selection],
        "action_candidates": list(ACTION_CANDIDATES),
        "eval": [asdict(row) for row in eval_rows],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace_payload,
        "crisis_logs": crisis_logs,
    }
    report124.rows_to_csv(Path(f"{PREFIX}_schedule.csv"), schedules)
    report124.rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_action_training.csv"), [env_training, social_training])
    report124.rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_planner_selection.csv"), planner_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_consequence_training.csv"), consequence_training_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_consequence_selection.csv"), consequence_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_teacher_summary.csv"), [teacher_summary])
    report124.rows_to_csv(Path(f"{PREFIX}_teacher_plan_use.csv"), plan_use)
    report124.rows_to_csv(Path(f"{PREFIX}_distillation_training.csv"), [distill_training])
    report124.rows_to_csv(Path(f"{PREFIX}_policy_selection.csv"), policy_selection)
    report124.rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    report124.rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    report124.rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    report124.rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    report124.write_json(Path(f"{PREFIX}_results.json"), payload)
    report124.write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    report124.write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_MPC_SEQUENCE_DISTILLATION_RESULTS", payload)
    report124.write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_MPC_SEQUENCE_DISTILLATION_TRACE", trace_payload)
    return payload


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-seeds", default="20260911,20260912,20260913")
    parser.add_argument("--tune-seeds", default="20261111,20261112")
    parser.add_argument("--eval-seeds", default="20261121,20261122,20261123")
    parser.add_argument("--hours", type=float, default=96.0)
    parser.add_argument("--step-hours", type=float, default=0.10)
    parser.add_argument("--population", type=int, default=14)
    parser.add_argument("--epochs", type=int, default=14)
    parser.add_argument("--hidden-size", type=int, default=48)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--action-epochs", type=int, default=18)
    parser.add_argument("--action-hidden-size", type=int, default=48)
    parser.add_argument("--action-learning-rate", type=float, default=0.004)
    parser.add_argument("--consequence-epochs", type=int, default=8)
    parser.add_argument("--consequence-hidden-size", type=int, default=48)
    parser.add_argument("--consequence-learning-rate", type=float, default=0.003)
    parser.add_argument("--consequence-return-scale", type=float, default=1.15)
    parser.add_argument("--student-iterations", type=int, default=0)
    parser.add_argument("--student-collection-bias", type=float, default=0.70)
    parser.add_argument("--distill-epochs", type=int, default=10)
    parser.add_argument("--distill-hidden-size", type=int, default=64)
    parser.add_argument("--distill-learning-rate", type=float, default=0.003)
    parser.add_argument("--class-balance-power", type=float, default=0.35)
    parser.add_argument("--teacher-commit-actions", type=int, default=14)
    parser.add_argument("--policy-temperature", type=float, default=1.0)
    parser.add_argument("--policy-bias-candidates", default="0.0,0.40,0.80,1.20")
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
        student_iterations=args.student_iterations,
        student_collection_bias=args.student_collection_bias,
        distill_epochs=args.distill_epochs,
        distill_hidden_size=args.distill_hidden_size,
        distill_learning_rate=args.distill_learning_rate,
        class_balance_power=args.class_balance_power,
        teacher_commit_actions=args.teacher_commit_actions,
        policy_temperature=args.policy_temperature,
        policy_bias_candidates=parse_floats(args.policy_bias_candidates),
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "teacher_summary": payload["teacher_summary"],
        "distillation_training": payload["distillation_training"],
        "policy_selection": payload["policy_selection"],
        "verdict": payload["verdict"],
        "summary": payload["summary"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
