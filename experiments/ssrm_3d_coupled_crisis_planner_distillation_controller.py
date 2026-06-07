#!/usr/bin/env python3
"""Distill minimum-channel crisis planning into a recurrent policy.

Report 123 showed that a dynamic weakest-channel planner around learned
environmental/social action heads can recover coupled repair across randomized
post-12h crises. This benchmark asks whether that successful structured
planner can be distilled into a recurrent active-crisis policy and then removed
at evaluation.

The distilled policy receives the same active-crisis policy features used by
Reports 119-122. It does not call the minimum-channel planner at evaluation.
This is bounded policy-distillation evidence, not open-ended civilization,
unsupplied action discovery, subjective consciousness, or mature deep RL.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import torch
import torch.nn.functional as F

import ssrm_3d_coupled_crisis_active_policy_controller as report119
import ssrm_3d_coupled_crisis_active_state_value_controller as report117
import ssrm_3d_coupled_crisis_joint_arbitration_controller as report113
import ssrm_3d_coupled_crisis_memory_policy_controller as report121
import ssrm_3d_coupled_crisis_min_channel_planner_controller as report123
import ssrm_3d_coupled_crisis_randomized_transfer_controller as report114
import ssrm_3d_coupled_crisis_rollout_window_controller as report111
import ssrm_3d_coupled_social_environment_maturation_controller as coupled
import ssrm_3d_learned_multiday_maturation_controller as base
import ssrm_3d_return_selected_multiday_maturation_controller as report105
from ssrm_maturation.agents import make_agents
from ssrm_maturation.benchmark import Trace
from ssrm_maturation.environment import living


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_planner_distillation"
DISTILLATION_SEED = 20261911
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
    epochs: int = 24
    hidden_size: int = 64
    learning_rate: float = 0.004
    action_epochs: int = 32
    action_hidden_size: int = 64
    action_learning_rate: float = 0.004
    distill_epochs: int = 12
    distill_hidden_size: int = 64
    distill_learning_rate: float = 0.003
    policy_temperature: float = 1.0
    policy_bias_candidates: Sequence[float] = (0.0, 0.20, 0.40, 0.70, 1.00)
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class DistillationTrainingRow:
    sequences: int
    examples: int
    distill_epochs: int
    final_loss: float
    train_accuracy: float
    env_action_fraction: float
    social_action_fraction: float
    none_fraction: float
    mean_sequence_length: float
    device_used: str
    parameter_count: int


@dataclass(frozen=True)
class DistillationSelectionRow:
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
class VerdictRow:
    selected_router: str
    selected_planner: str
    selected_policy_bias: float
    training_examples: int
    distillation_train_accuracy: float
    distilled_total_score: float
    min_channel_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    distilled_crisis_score: float
    min_channel_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    distilled_resolved_rate: float
    min_channel_resolved_rate: float
    fixed_joint_resolved_rate: float
    return_selected_resolved_rate: float
    distilled_coupled_response: float
    min_channel_coupled_response: float
    fixed_joint_coupled_response: float
    return_selected_coupled_response: float
    distilled_gain_over_return_selected: float
    distilled_gap_to_teacher: float
    distilled_gap_to_fixed_joint: float
    social_culture_crisis_loss: float
    environment_crisis_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    mean_crisis_count: float
    supports_planner_distillation: bool
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


def teacher_action(
    agent_id: str,
    features: Sequence[float],
    action_counts: Dict[str, int],
    alive_count: int,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    env_states: Dict[str, torch.Tensor],
    social_states: Dict[str, torch.Tensor],
    device: torch.device,
) -> Optional[str]:
    return report123.min_channel_coordinator_action(
        agent=type("TeacherAgent", (), {"ident": agent_id})(),
        features=features,
        action_counts=action_counts,
        alive_count=alive_count,
        env_model=env_model,
        social_model=social_model,
        env_states=env_states,
        social_states=social_states,
        env_quota=0.0,
        social_quota=0.0,
        strength=1.0,
        device=device,
        ablation="none",
    )


def collect_teacher_sequences(
    cfg: Config,
    model: base.ControllerNet,
    env_model: base.ControllerNet,
    social_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
    planner: report123.PlannerCandidate,
) -> List[List[Tuple[List[float], int]]]:
    sequences: List[List[Tuple[List[float], int]]] = []
    condition = report121.CONDITIONS[0]
    with report123.patched_min_channel_planner(planner):
        for seed in cfg.train_seeds:
            rng = random.Random(seed * 173 + DISTILLATION_SEED)
            agents = make_agents(rng, cfg.population)
            world = coupled.prepare_world(rng, cfg)
            previous_actions: Dict[str, int] = {}
            recurrent_states: Dict[str, torch.Tensor] = {}
            env_states: Dict[str, torch.Tensor] = {}
            social_states: Dict[str, torch.Tensor] = {}
            events: List[str] = []
            tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
            active_key: Optional[float] = None
            pending: List[Tuple[List[float], int]] = []

            while world.time < cfg.hours - 1e-9:
                dt = min(cfg.step_hours, cfg.hours - world.time)
                action_counts: Dict[str, int] = {}
                coupled.maybe_start_crisis(world, tracker, rng, events)
                if tracker.active is not None and active_key != tracker.active.start:
                    if pending:
                        sequences.append(pending)
                    pending = []
                    active_key = tracker.active.start
                    env_states = {}
                    social_states = {}
                if tracker.active is not None:
                    coupled.apply_crisis_symptoms(world, tracker.active, dt)

                def selector(agent, current_world, current_condition, current_rng, features, previous) -> str:
                    active = tracker.active
                    action: Optional[str] = None
                    label_action = "none"
                    if active is not None and current_world.time >= 12.0:
                        values = report119.policy_features(
                            features,
                            active,
                            action_counts,
                            len(living(agents)),
                            current_world.time,
                            "none",
                        )
                        action = teacher_action(
                            agent.ident,
                            features,
                            action_counts,
                            len(living(agents)),
                            env_model,
                            social_model,
                            env_states,
                            social_states,
                            device,
                        )
                        if action is not None:
                            label_action = action if action in ACTION_TO_INDEX else "none"
                        pending.append((values, ACTION_TO_INDEX[label_action]))
                    if action is None:
                        action = report117.learned_policy_action(
                            agent,
                            features,
                            model,
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
                if tracker.active is None and pending:
                    sequences.append(pending)
                    pending = []
                    active_key = None
            if pending:
                sequences.append(pending)
    return sequences


def train_distilled_policy(
    cfg: Config,
    sequences: Sequence[Sequence[Tuple[List[float], int]]],
    device: torch.device,
) -> Tuple[report121.CrisisMemoryPolicyNet, DistillationTrainingRow]:
    if not sequences:
        raise RuntimeError("no teacher sequences collected")
    torch.manual_seed(DISTILLATION_SEED)
    model = report121.CrisisMemoryPolicyNet(cfg.distill_hidden_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.distill_learning_rate)
    final_loss = 0.0
    for _ in range(cfg.distill_epochs):
        for sequence in sequences:
            x = torch.tensor([[item[0] for item in sequence]], dtype=torch.float32, device=device)
            y = torch.tensor([item[1] for item in sequence], dtype=torch.long, device=device)
            logits, _ = model.forward_sequence(x)
            logits = report119.masked_logits(logits.squeeze(0), "none", 0.0)
            loss = F.cross_entropy(logits, y)
            optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 2.0)
            optimizer.step()
            final_loss = float(loss.detach().cpu().item())
    model.eval()
    correct = 0
    total = 0
    counts = {action: 0 for action in ACTION_CANDIDATES}
    with torch.no_grad():
        for sequence in sequences:
            x = torch.tensor([[item[0] for item in sequence]], dtype=torch.float32, device=device)
            y = torch.tensor([item[1] for item in sequence], dtype=torch.long, device=device)
            logits, _ = model.forward_sequence(x)
            pred = report119.masked_logits(logits.squeeze(0), "none", 0.0).argmax(dim=-1)
            correct += int((pred == y).sum().item())
            total += int(y.numel())
            for index in y.detach().cpu().tolist():
                counts[ACTION_CANDIDATES[index]] += 1
    env_count = sum(counts.get(action, 0) for action in report111.ENV_RESPONSE_ACTIONS)
    social_count = sum(counts.get(action, 0) for action in report111.SOCIAL_RESPONSE_ACTIONS)
    none_count = counts.get("none", 0)
    return model, DistillationTrainingRow(
        sequences=len(sequences),
        examples=total,
        distill_epochs=cfg.distill_epochs,
        final_loss=final_loss,
        train_accuracy=correct / max(1, total),
        env_action_fraction=env_count / max(1, total),
        social_action_fraction=social_count / max(1, total),
        none_fraction=none_count / max(1, total),
        mean_sequence_length=mean(len(sequence) for sequence in sequences),
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
    row = replace(row, controller="planner_distilled_gru")
    trace_out.condition = f"planner_distilled_gru:{router.name}:bias_{policy_bias:g}:{ablation}"
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
    objective = total * 0.46 + crisis * 1.12 + resolved * 0.68 + coupled_response * 0.84 + balance * 0.14 - damage * 0.32
    return total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective


def select_policy_bias(
    cfg: Config,
    model: base.ControllerNet,
    distilled_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[float, List[DistillationSelectionRow]]:
    best_bias = 0.0
    best_objective = -1e9
    rows: List[DistillationSelectionRow] = []
    for bias in cfg.policy_bias_candidates:
        eval_rows = [
            run_distilled_episode(seed, cfg, model, distilled_model, device, router, bias)[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_objective = objective
            best_bias = bias
        rows.append(DistillationSelectionRow(
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
    base_row = coupled.row_lookup(summary, "planner_distilled_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = coupled.row_lookup(summary, "planner_distilled_gru", ablation)
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
    schedules: Sequence[report114.ScheduleRow],
    training: DistillationTrainingRow,
) -> VerdictRow:
    distilled = coupled.row_lookup(summary, "planner_distilled_gru", "none")
    teacher = coupled.row_lookup(summary, "min_channel_planner_gru", "none")
    fixed = coupled.row_lookup(summary, "fixed_joint_gru", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    supports_distill = (
        training.train_accuracy >= 0.55
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
        and teacher.mean_crisis_score - distilled.mean_crisis_score <= 0.30
    )
    supports_dependency = (
        distilled.mean_crisis_score > 0.0
        and social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    return VerdictRow(
        selected_router=router.name,
        selected_planner=planner.name,
        selected_policy_bias=policy_bias,
        training_examples=training.examples,
        distillation_train_accuracy=training.train_accuracy,
        distilled_total_score=distilled.mean_total_score,
        min_channel_total_score=teacher.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        distilled_crisis_score=distilled.mean_crisis_score,
        min_channel_crisis_score=teacher.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        distilled_resolved_rate=distilled.mean_resolved_rate,
        min_channel_resolved_rate=teacher.mean_resolved_rate,
        fixed_joint_resolved_rate=fixed.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        distilled_coupled_response=distilled.mean_coupled_response_rate,
        min_channel_coupled_response=teacher.mean_coupled_response_rate,
        fixed_joint_coupled_response=fixed.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        distilled_gain_over_return_selected=distilled.mean_total_score - returned.mean_total_score,
        distilled_gap_to_teacher=teacher.mean_total_score - distilled.mean_total_score,
        distilled_gap_to_fixed_joint=fixed.mean_total_score - distilled.mean_total_score,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=distilled.shock_gate_pass_rate,
        post_gate_shock_rate=distilled.post_gate_shock_rate,
        survival_at_12h=distilled.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_planner_distillation=supports_distill,
        supports_teacher_transfer=supports_teacher,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_distill and supports_teacher and supports_dependency else "partial_or_failed",
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
        teacher_sequences = collect_teacher_sequences(
            cfg,
            models["gru"],
            env_model,
            social_model,
            device,
            selected_router,
            selected_planner,
        )
        distilled_model, distill_training = train_distilled_policy(cfg, teacher_sequences, device)
        selected_bias, policy_selection = select_policy_bias(cfg, models["gru"], distilled_model, device, selected_router)

        eval_rows: List[coupled.EvalRow] = []
        trace_out = None
        crisis_logs: Dict[str, List[dict[str, object]]] = {}
        for seed in cfg.eval_seeds:
            for controller, model, router in (
                ("designed", None, report105.ROUTERS[0]),
                ("reactive", None, report105.ROUTERS[0]),
                ("frame_mlp", models["frame_mlp"], report105.ROUTERS[0]),
                ("gru", models["gru"], report105.ROUTERS[0]),
                ("return_selected_gru", models["gru"], selected_router),
            ):
                row, maybe_trace, tracker = report113.run_episode(
                    seed,
                    cfg,
                    controller,
                    model,
                    env_model,
                    social_model,
                    device,
                    router,
                    0.0,
                    0.0,
                    0.0,
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:{controller}:none"] = tracker.response_log
                if maybe_trace.frames:
                    trace_out = maybe_trace
            fixed_row = report123.run_fixed_joint_episode(seed, cfg, models["gru"], env_model, social_model, device, selected_router)
            eval_rows.append(fixed_row)
            teacher_row, maybe_trace, tracker = report123.run_min_channel_episode(
                seed,
                cfg,
                models["gru"],
                env_model,
                social_model,
                device,
                selected_router,
                selected_planner,
            )
            eval_rows.append(teacher_row)
            crisis_logs[f"{seed}:fixed_joint_gru:none"] = []
            crisis_logs[f"{seed}:min_channel_planner_gru:none"] = tracker.response_log
            distilled_row, maybe_trace, tracker = run_distilled_episode(
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
            crisis_logs[f"{seed}:planner_distilled_gru:none"] = tracker.response_log
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
                crisis_logs[f"{seed}:planner_distilled_gru:{ablation}"] = tracker.response_log

    summary = coupled.summarize(eval_rows)
    ablations = ablations_from_summary(summary)
    verdict = transfer_verdict(summary, ablations, selected_router, selected_planner, selected_bias, schedules, distill_training)
    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "planner_distilled", "frames": []}
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
            "action_epochs": cfg.action_epochs,
            "action_hidden_size": cfg.action_hidden_size,
            "distill_epochs": cfg.distill_epochs,
            "distill_hidden_size": cfg.distill_hidden_size,
            "policy_bias_candidates": list(cfg.policy_bias_candidates),
            "device": cfg.device,
            "trace_seed": cfg.trace_seed,
        },
        "schedule": [asdict(row) for row in schedules],
        "router_selection": [asdict(row) for row in router_selection],
        "planner_selection": [asdict(row) for row in planner_selection],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "distillation_training": asdict(distill_training),
        "policy_selection": [asdict(row) for row in policy_selection],
        "action_candidates": list(ACTION_CANDIDATES),
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace_payload,
        "crisis_logs": crisis_logs,
        "notes": {
            "claim": "successful minimum-channel planner trajectories can be distilled into a recurrent active-crisis policy that no longer calls the planner at evaluation",
            "not_claimed": "actor-critic reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
            "remaining_structure": "candidate crisis actions are supplied and teacher trajectories come from an engineered planner; this tests distillation, not natural discovery",
        },
    }
    rows_to_csv(Path(f"{PREFIX}_schedule.csv"), schedules)
    rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    rows_to_csv(Path(f"{PREFIX}_action_training.csv"), [env_training, social_training])
    rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    rows_to_csv(Path(f"{PREFIX}_planner_selection.csv"), planner_selection)
    rows_to_csv(Path(f"{PREFIX}_policy_selection.csv"), policy_selection)
    rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    write_json(Path(f"{PREFIX}_results.json"), payload)
    write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_PLANNER_DISTILLATION_RESULTS", payload)
    write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_PLANNER_DISTILLATION_TRACE", trace_payload)
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
    parser.add_argument("--distill-epochs", type=int, default=12)
    parser.add_argument("--distill-hidden-size", type=int, default=64)
    parser.add_argument("--distill-learning-rate", type=float, default=0.003)
    parser.add_argument("--policy-temperature", type=float, default=1.0)
    parser.add_argument("--policy-bias-candidates", default="0.0,0.20,0.40,0.70,1.00")
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
        distill_epochs=args.distill_epochs,
        distill_hidden_size=args.distill_hidden_size,
        distill_learning_rate=args.distill_learning_rate,
        policy_temperature=args.policy_temperature,
        policy_bias_candidates=parse_floats(args.policy_bias_candidates),
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "distillation_training": payload["distillation_training"],
        "policy_selection": payload["policy_selection"],
        "verdict": payload["verdict"],
        "summary": payload["summary"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
