#!/usr/bin/env python3
"""Two-channel process-pressure policy for SSRM-3D coupled crises.

Report 121 showed that recurrent hidden state across the crisis window is not
enough: the learned policy preserved environmental response while dropping the
social repair channel. This benchmark keeps the same recurrent policy shape
but changes the training pressure. Completed-crisis return is strengthened
against one-channel repair, and an auxiliary process loss pushes the sampled
sequence to maintain both environmental and social repair actions.

This is bounded process-supervised evidence. It is not open-ended civilization,
unsupplied action discovery, or evidence of subjective consciousness.
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
import ssrm_3d_coupled_crisis_joint_arbitration_controller as report113
import ssrm_3d_coupled_crisis_memory_policy_controller as report121
import ssrm_3d_coupled_crisis_randomized_transfer_controller as report114
import ssrm_3d_coupled_crisis_rollout_window_controller as report111
import ssrm_3d_coupled_social_environment_maturation_controller as coupled
import ssrm_3d_learned_multiday_maturation_controller as base
import ssrm_3d_return_selected_multiday_maturation_controller as report105
from ssrm_maturation.environment import living


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_process_policy"
PROCESS_POLICY_SEED = 20261811
ACTION_CANDIDATES = report119.ACTION_CANDIDATES
ACTION_TO_INDEX = report119.ACTION_TO_INDEX


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
    policy_epochs: int = 4
    policy_hidden_size: int = 64
    policy_learning_rate: float = 0.003
    memory_epochs: int = 5
    memory_hidden_size: int = 64
    memory_learning_rate: float = 0.003
    process_epochs: int = 5
    process_hidden_size: int = 64
    process_learning_rate: float = 0.003
    process_loss_coef: float = 0.35
    entropy_coef: float = 0.008
    policy_temperature: float = 1.0
    policy_bias_candidates: Sequence[float] = (0.0, 0.20, 0.40, 0.70, 1.00)
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class ProcessPolicyTrainingRow:
    episodes: int
    crises: int
    epochs: int
    final_loss: float
    final_policy_loss: float
    final_process_loss: float
    mean_return: float
    return_std: float
    moving_baseline: float
    mean_sequence_length: float
    mean_entropy: float
    process_loss_coef: float
    policy_temperature: float
    entropy_coef: float
    device_used: str
    parameter_count: int


@dataclass(frozen=True)
class ProcessPolicySelectionRow:
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
class ProcessPolicyVerdictRow:
    selected_router: str
    selected_policy_bias: float
    training_crises: int
    process_policy_total_score: float
    memory_policy_total_score: float
    active_policy_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    process_policy_crisis_score: float
    memory_policy_crisis_score: float
    active_policy_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    process_policy_resolved_rate: float
    memory_policy_resolved_rate: float
    active_policy_resolved_rate: float
    fixed_joint_resolved_rate: float
    return_selected_resolved_rate: float
    process_policy_coupled_response: float
    memory_policy_coupled_response: float
    active_policy_coupled_response: float
    fixed_joint_coupled_response: float
    return_selected_coupled_response: float
    gain_over_memory_policy: float
    gain_over_active_policy: float
    gain_over_return_selected: float
    gain_over_fixed_joint: float
    social_culture_crisis_loss: float
    environment_crisis_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    mean_crisis_count: float
    supports_memory_policy_improvement: bool
    supports_active_policy_improvement: bool
    supports_return_baseline_improvement: bool
    supports_fixed_joint_improvement: bool
    supports_process_policy_learning: bool
    supports_social_environment_dependency: bool
    verdict: str


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def stdev(values: Sequence[float]) -> float:
    if len(values) < 2:
        return 0.0
    avg = mean(values)
    return (sum((value - avg) ** 2 for value in values) / len(values)) ** 0.5


def bounded(value: float, low: float = -2.0, high: float = 3.2) -> float:
    return max(low, min(high, value))


def parse_ints(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def parse_floats(value: str) -> Tuple[float, ...]:
    return tuple(float(part.strip()) for part in value.split(",") if part.strip())


def env_target_action(active: coupled.ActiveCrisis) -> str:
    return report111.primary_env_action(active)


def social_target_action(active: coupled.ActiveCrisis, features: Sequence[float]) -> str:
    return report113.social_target_action(active, features)


def process_target_action(
    active: coupled.ActiveCrisis,
    features: Sequence[float],
    action_counts: Dict[str, int],
    alive_count: int,
) -> str:
    env_fraction = min(1.0, active.env_progress / active.profile.env_need)
    social_fraction = min(1.0, active.social_progress / active.profile.social_need)
    current_env, current_social = report117.response_fractions(action_counts, alive_count)
    env_deficit = 1.0 - env_fraction
    social_deficit = 1.0 - social_fraction
    if current_social < 0.12 and (current_env >= current_social or social_deficit > 0.08):
        return social_target_action(active, features)
    if current_env < 0.12 and env_deficit > 0.08:
        return env_target_action(active)
    if env_deficit > social_deficit + 0.04:
        return env_target_action(active)
    return social_target_action(active, features)


def process_window_return(active: coupled.ActiveCrisis, damage_delta: float) -> float:
    env_fraction, social_fraction, coupled_fraction = report119.crisis_fraction(active)
    resolved = 1.0 if coupled_fraction >= 0.92 else 0.0
    env_rate = active.env_response_steps / max(1, active.steps)
    social_rate = active.social_response_steps / max(1, active.steps)
    coupled_rate = active.coupled_response_steps / max(1, active.steps)
    min_rate = min(env_rate, social_rate)
    imbalance = abs(env_rate - social_rate)
    progress_imbalance = abs(env_fraction - social_fraction)
    one_channel = max(env_rate, social_rate) if min_rate < 0.05 else 0.0
    unresolved = max(0.0, 0.92 - coupled_fraction)
    return bounded(
        coupled_fraction * 1.65
        + resolved * 1.05
        + coupled_rate * 1.45
        + min_rate * 0.82
        + (1.0 - min(1.0, progress_imbalance)) * 0.24
        - unresolved * 1.10
        - imbalance * 0.78
        - one_channel * 1.20
        - max(0.0, damage_delta) * 1.48
    )


def update_process_policy_from_sequence(
    model: report121.CrisisMemoryPolicyNet,
    optimizer: torch.optim.Optimizer,
    sequence: Sequence[Tuple[List[float], int, int]],
    reward: float,
    moving_baseline: float,
    cfg: Config,
    device: torch.device,
) -> Tuple[float, float, float]:
    if not sequence:
        return 0.0, 0.0, 0.0
    x = torch.tensor([[item[0] for item in sequence]], dtype=torch.float32, device=device)
    actions = torch.tensor([item[1] for item in sequence], dtype=torch.long, device=device)
    targets = torch.tensor([item[2] for item in sequence], dtype=torch.long, device=device)
    logits, _ = model.forward_sequence(x)
    logits = report119.masked_logits(logits.squeeze(0) / max(0.05, cfg.policy_temperature), "none", 0.0)
    dist = torch.distributions.Categorical(logits=logits)
    entropy_term = dist.entropy().mean()
    advantage = reward - moving_baseline
    policy_loss = -float(advantage) * dist.log_prob(actions).mean() - cfg.entropy_coef * entropy_term
    process_loss = F.cross_entropy(logits, targets)
    loss = policy_loss + cfg.process_loss_coef * process_loss
    optimizer.zero_grad()
    loss.backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), 2.0)
    optimizer.step()
    return (
        float(loss.detach().cpu().item()),
        float(policy_loss.detach().cpu().item()),
        float(process_loss.detach().cpu().item()),
    )


def run_process_training_episode(
    seed: int,
    cfg: Config,
    base_model: base.ControllerNet,
    process_model: report121.CrisisMemoryPolicyNet,
    optimizer: torch.optim.Optimizer,
    device: torch.device,
    router: report105.PressureRouter,
    moving_baseline: float,
) -> Tuple[int, List[float], List[float], List[int], float, float, float, float]:
    condition = report121.CONDITIONS[0]
    rng = random.Random(seed * 157 + PROCESS_POLICY_SEED)
    agents = report121.make_agents(rng, cfg.population)
    world = coupled.prepare_world(rng, cfg)
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
    pending_sequence: List[Tuple[List[float], int, int]] = []
    pending_damage_start = tracker.damage_integral
    memory_state: Optional[torch.Tensor] = None
    active_key: Optional[float] = None
    returns: List[float] = []
    entropies: List[float] = []
    sequence_lengths: List[int] = []
    final_loss = 0.0
    final_policy_loss = 0.0
    final_process_loss = 0.0
    crises = 0
    process_model.train()

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        action_counts: Dict[str, int] = {}
        coupled.maybe_start_crisis(world, tracker, rng, events)
        if tracker.active is not None and active_key != tracker.active.start:
            active_key = tracker.active.start
            memory_state = None
            pending_sequence = []
            pending_damage_start = tracker.damage_integral
        if tracker.active is not None:
            coupled.apply_crisis_symptoms(world, tracker.active, dt)

        def selector(
            agent: report121.Agent,
            current_world: report121.World,
            current_condition: report121.Condition,
            current_rng: random.Random,
            features: List[float],
            previous: int,
        ) -> str:
            nonlocal memory_state
            active = tracker.active
            if active is None:
                action = report117.learned_policy_action(agent, features, base_model, recurrent_states, router, device, "none")
            else:
                action, sampled_features, action_index, entropy, next_state = report121.sample_memory_candidate_without_graph(
                    process_model,
                    features,
                    active,
                    action_counts,
                    len(living(agents)),
                    current_world.time,
                    memory_state,
                    device,
                    cfg.policy_temperature,
                )
                memory_state = next_state
                if current_world.time >= 12.0:
                    target = process_target_action(active, features, action_counts, len(living(agents)))
                    pending_sequence.append((sampled_features, action_index, ACTION_TO_INDEX[target]))
                    entropies.append(entropy)
                if action == "none":
                    action = report117.learned_policy_action(agent, features, base_model, recurrent_states, router, device, "none")
            action_counts[action] = action_counts.get(action, 0) + 1
            return action

        base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
        active_before_completion = tracker.active
        report111.update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
        coupled.complete_crisis_if_due(world, agents, tracker, events)
        if active_before_completion is not None and tracker.active is None:
            reward = process_window_return(active_before_completion, tracker.damage_integral - pending_damage_start)
            returns.append(reward)
            crises += 1
            if pending_sequence:
                sequence_lengths.append(len(pending_sequence))
                final_loss, final_policy_loss, final_process_loss = update_process_policy_from_sequence(
                    process_model,
                    optimizer,
                    pending_sequence,
                    reward,
                    moving_baseline,
                    cfg,
                    device,
                )
            moving_baseline = moving_baseline * 0.86 + reward * 0.14
            pending_sequence = []
            memory_state = None
            active_key = None
            pending_damage_start = tracker.damage_integral

    return crises, returns, entropies, sequence_lengths, moving_baseline, final_loss, final_policy_loss, final_process_loss


def train_process_policy_model(
    cfg: Config,
    base_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[report121.CrisisMemoryPolicyNet, ProcessPolicyTrainingRow]:
    torch.manual_seed(PROCESS_POLICY_SEED)
    model = report121.CrisisMemoryPolicyNet(cfg.process_hidden_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.process_learning_rate)
    moving_baseline = 0.0
    all_returns: List[float] = []
    all_entropies: List[float] = []
    all_lengths: List[int] = []
    total_crises = 0
    final_loss = 0.0
    final_policy_loss = 0.0
    final_process_loss = 0.0
    episodes = 0
    for epoch in range(cfg.process_epochs):
        for seed in cfg.train_seeds:
            crises, returns, entropies, lengths, moving_baseline, final_loss, final_policy_loss, final_process_loss = run_process_training_episode(
                seed + epoch * 1019,
                cfg,
                base_model,
                model,
                optimizer,
                device,
                router,
                moving_baseline,
            )
            total_crises += crises
            all_returns.extend(returns)
            all_entropies.extend(entropies)
            all_lengths.extend(lengths)
            episodes += 1
    model.eval()
    return model, ProcessPolicyTrainingRow(
        episodes=episodes,
        crises=total_crises,
        epochs=cfg.process_epochs,
        final_loss=final_loss,
        final_policy_loss=final_policy_loss,
        final_process_loss=final_process_loss,
        mean_return=mean(all_returns),
        return_std=stdev(all_returns),
        moving_baseline=moving_baseline,
        mean_sequence_length=mean(all_lengths),
        mean_entropy=mean(all_entropies),
        process_loss_coef=cfg.process_loss_coef,
        policy_temperature=cfg.policy_temperature,
        entropy_coef=cfg.entropy_coef,
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in model.parameters()),
    )


def run_process_policy_episode(
    seed: int,
    cfg: Config,
    controller: str,
    model: Optional[base.ControllerNet],
    process_model: Optional[report121.CrisisMemoryPolicyNet],
    device: torch.device,
    router: report105.PressureRouter,
    policy_bias: float = 0.0,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, report121.Trace, coupled.CrisisTracker]:
    delegated = "memory_policy_gru" if controller == "process_policy_gru" else controller
    row, trace_out, tracker = report121.run_memory_policy_episode(
        seed,
        cfg,
        delegated,
        model,
        process_model,
        device,
        router,
        policy_bias=policy_bias,
        ablation=ablation,
        trace=trace,
    )
    if controller == "process_policy_gru":
        row = replace(row, controller=controller)
        trace_out.condition = f"{controller}:{router.name}:process_{policy_bias:g}:{ablation}"
    return row, trace_out, tracker


def selection_objective(rows: Sequence[coupled.EvalRow]) -> Tuple[float, float, float, float, float, float, float, float, float]:
    return report119.selection_objective(rows)


def select_process_policy_bias(
    cfg: Config,
    model: base.ControllerNet,
    process_model: report121.CrisisMemoryPolicyNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[float, List[ProcessPolicySelectionRow]]:
    rows: List[ProcessPolicySelectionRow] = []
    best_bias = 0.0
    best_objective = -1e9
    for bias in cfg.policy_bias_candidates:
        eval_rows = [
            run_process_policy_episode(
                seed,
                cfg,
                "process_policy_gru",
                model,
                process_model,
                device,
                router,
                policy_bias=bias,
            )[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, env_response, social_response, coupled_response, damage, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_objective = objective
            best_bias = bias
        rows.append(ProcessPolicySelectionRow(
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
    base_row = coupled.row_lookup(summary, "process_policy_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = coupled.row_lookup(summary, "process_policy_gru", ablation)
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
    selected_bias: float,
    schedules: Sequence[report114.ScheduleRow],
    training: ProcessPolicyTrainingRow,
) -> ProcessPolicyVerdictRow:
    process = coupled.row_lookup(summary, "process_policy_gru", "none")
    memory = coupled.row_lookup(summary, "memory_policy_gru", "none")
    active = coupled.row_lookup(summary, "active_policy_gru", "none")
    fixed = coupled.row_lookup(summary, "fixed_joint_gru", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    supports_memory = (
        training.crises > 0
        and process.mean_coupled_response_rate - memory.mean_coupled_response_rate >= 0.040
        and process.mean_resolved_rate - memory.mean_resolved_rate >= 0.040
    )
    supports_active = (
        training.crises > 0
        and process.mean_total_score - active.mean_total_score >= 0.005
        and process.mean_coupled_response_rate - active.mean_coupled_response_rate >= 0.040
        and process.mean_resolved_rate - active.mean_resolved_rate >= 0.040
    )
    supports_return = (
        training.crises > 0
        and mean_crisis_count >= 4.0
        and process.mean_total_score - returned.mean_total_score >= 0.010
        and process.mean_crisis_score - returned.mean_crisis_score >= 0.040
        and process.mean_resolved_rate - returned.mean_resolved_rate >= 0.080
        and process.mean_coupled_response_rate - returned.mean_coupled_response_rate >= 0.080
        and process.mean_alive_at_12h >= 12.0
        and process.shock_gate_pass_rate == 1.0
        and process.post_gate_shock_rate == 1.0
    )
    supports_fixed = (
        process.mean_total_score - fixed.mean_total_score >= 0.005
        and process.mean_crisis_score - fixed.mean_crisis_score >= 0.020
        and process.mean_resolved_rate - fixed.mean_resolved_rate >= 0.020
        and process.mean_coupled_response_rate - fixed.mean_coupled_response_rate >= 0.020
    )
    supports_dependency = (
        process.mean_crisis_score > 0.0
        and social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    supports_process = supports_memory and supports_active and supports_return and supports_fixed
    return ProcessPolicyVerdictRow(
        selected_router=router.name,
        selected_policy_bias=selected_bias,
        training_crises=training.crises,
        process_policy_total_score=process.mean_total_score,
        memory_policy_total_score=memory.mean_total_score,
        active_policy_total_score=active.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        process_policy_crisis_score=process.mean_crisis_score,
        memory_policy_crisis_score=memory.mean_crisis_score,
        active_policy_crisis_score=active.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        process_policy_resolved_rate=process.mean_resolved_rate,
        memory_policy_resolved_rate=memory.mean_resolved_rate,
        active_policy_resolved_rate=active.mean_resolved_rate,
        fixed_joint_resolved_rate=fixed.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        process_policy_coupled_response=process.mean_coupled_response_rate,
        memory_policy_coupled_response=memory.mean_coupled_response_rate,
        active_policy_coupled_response=active.mean_coupled_response_rate,
        fixed_joint_coupled_response=fixed.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        gain_over_memory_policy=process.mean_total_score - memory.mean_total_score,
        gain_over_active_policy=process.mean_total_score - active.mean_total_score,
        gain_over_return_selected=process.mean_total_score - returned.mean_total_score,
        gain_over_fixed_joint=process.mean_total_score - fixed.mean_total_score,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=process.shock_gate_pass_rate,
        post_gate_shock_rate=process.post_gate_shock_rate,
        survival_at_12h=process.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_memory_policy_improvement=supports_memory,
        supports_active_policy_improvement=supports_active,
        supports_return_baseline_improvement=supports_return,
        supports_fixed_joint_improvement=supports_fixed,
        supports_process_policy_learning=supports_process,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_process and supports_dependency else "partial_or_failed",
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
            trained_model, row = base.train_model(architecture, x, y, mask, cfg, device)
            models[architecture] = trained_model
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
            20261821,
        )
        social_model, social_training = report113.train_action_model(
            cfg,
            device,
            "social",
            social_sequences,
            social_labels,
            flags,
            20261822,
        )
        active_policy_model, active_policy_training = report119.train_policy_model(cfg, models["gru"], device, selected_router)
        selected_active_bias, active_policy_selection = report119.select_policy_bias(cfg, models["gru"], active_policy_model, device, selected_router)
        memory_model, memory_training = report121.train_memory_policy_model(cfg, models["gru"], device, selected_router)
        selected_memory_bias, memory_selection = report121.select_memory_policy_bias(cfg, models["gru"], memory_model, device, selected_router)
        process_model, process_training = train_process_policy_model(cfg, models["gru"], device, selected_router)
        selected_bias, process_selection = select_process_policy_bias(cfg, models["gru"], process_model, device, selected_router)

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
                row, maybe_trace, tracker = report117.run_active_value_episode(
                    seed,
                    cfg,
                    controller,
                    model,
                    env_model,
                    social_model,
                    None,
                    0.0,
                    1.0,
                    device,
                    router,
                )
                eval_rows.append(row)
                crisis_logs[f"{seed}:{controller}:none"] = tracker.response_log
                if maybe_trace.frames:
                    trace_out = maybe_trace
            fixed_row, _, fixed_tracker = report117.run_active_value_episode(
                seed,
                cfg,
                "fixed_joint_gru",
                models["gru"],
                env_model,
                social_model,
                None,
                0.0,
                1.0,
                device,
                selected_router,
            )
            eval_rows.append(fixed_row)
            crisis_logs[f"{seed}:fixed_joint_gru:none"] = fixed_tracker.response_log
            active_row, _, active_tracker = report119.run_active_policy_episode(
                seed,
                cfg,
                "active_policy_gru",
                models["gru"],
                active_policy_model,
                device,
                selected_router,
                policy_bias=selected_active_bias,
            )
            eval_rows.append(active_row)
            crisis_logs[f"{seed}:active_policy_gru:none"] = active_tracker.response_log
            memory_row, _, memory_tracker = report121.run_memory_policy_episode(
                seed,
                cfg,
                "memory_policy_gru",
                models["gru"],
                memory_model,
                device,
                selected_router,
                policy_bias=selected_memory_bias,
            )
            eval_rows.append(memory_row)
            crisis_logs[f"{seed}:memory_policy_gru:none"] = memory_tracker.response_log
            process_row, maybe_trace, tracker = run_process_policy_episode(
                seed,
                cfg,
                "process_policy_gru",
                models["gru"],
                process_model,
                device,
                selected_router,
                policy_bias=selected_bias,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(process_row)
            crisis_logs[f"{seed}:process_policy_gru:none"] = tracker.response_log
            if maybe_trace.frames:
                trace_out = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker = run_process_policy_episode(
                    seed,
                    cfg,
                    "process_policy_gru",
                    models["gru"],
                    process_model,
                    device,
                    selected_router,
                    policy_bias=selected_bias,
                    ablation=ablation,
                )
                eval_rows.append(replace(row, ablation=ablation))
                crisis_logs[f"{seed}:process_policy_gru:{ablation}"] = tracker.response_log

    summary = coupled.summarize(eval_rows)
    ablations = ablations_from_summary(summary)
    verdict = transfer_verdict(summary, ablations, selected_router, selected_bias, schedules, process_training)
    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "process_policy_gru", "frames": []}
    trace_payload["condition"] = "process_policy_gru"
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
            "policy_epochs": cfg.policy_epochs,
            "policy_hidden_size": cfg.policy_hidden_size,
            "memory_epochs": cfg.memory_epochs,
            "memory_hidden_size": cfg.memory_hidden_size,
            "memory_learning_rate": cfg.memory_learning_rate,
            "process_epochs": cfg.process_epochs,
            "process_hidden_size": cfg.process_hidden_size,
            "process_learning_rate": cfg.process_learning_rate,
            "process_loss_coef": cfg.process_loss_coef,
            "entropy_coef": cfg.entropy_coef,
            "policy_temperature": cfg.policy_temperature,
            "policy_bias_candidates": list(cfg.policy_bias_candidates),
            "device": cfg.device,
            "trace_seed": cfg.trace_seed,
        },
        "policy_context_names": list(report119.POLICY_CONTEXT_NAMES),
        "action_candidates": list(ACTION_CANDIDATES),
        "schedule": [asdict(row) for row in schedules],
        "router_selection": [asdict(row) for row in router_selection],
        "base_training": [asdict(row) for row in training_rows],
        "action_training": [asdict(env_training), asdict(social_training)],
        "active_policy_training": asdict(active_policy_training),
        "active_policy_selection": [asdict(row) for row in active_policy_selection],
        "memory_policy_training": asdict(memory_training),
        "memory_policy_selection": [asdict(row) for row in memory_selection],
        "process_policy_training": asdict(process_training),
        "process_policy_selection": [asdict(row) for row in process_selection],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace_payload,
        "crisis_logs": crisis_logs,
        "notes": {
            "claim": "two-channel process pressure can prevent recurrent active-crisis policy from dropping either repair channel",
            "not_claimed": "subjective consciousness, open-ended civilization, real-world competence, or unsupplied action discovery",
            "remaining_structure": "candidate repair actions and process targets are supplied; this is a bounded training-pressure test in an abstract simulator",
        },
    }
    report117.rows_to_csv(Path(f"{PREFIX}_schedule.csv"), schedules)
    report117.rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    report117.rows_to_csv(Path(f"{PREFIX}_action_training.csv"), [env_training, social_training])
    report117.rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    report117.rows_to_csv(Path(f"{PREFIX}_active_policy_training.csv"), [active_policy_training])
    report117.rows_to_csv(Path(f"{PREFIX}_active_policy_selection.csv"), active_policy_selection)
    report117.rows_to_csv(Path(f"{PREFIX}_memory_policy_training.csv"), [memory_training])
    report117.rows_to_csv(Path(f"{PREFIX}_memory_policy_selection.csv"), memory_selection)
    report117.rows_to_csv(Path(f"{PREFIX}_process_policy_training.csv"), [process_training])
    report117.rows_to_csv(Path(f"{PREFIX}_process_policy_selection.csv"), process_selection)
    report117.rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    report117.rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    report117.rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    report117.rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    report117.write_json(Path(f"{PREFIX}_results.json"), payload)
    report117.write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    report117.write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_PROCESS_POLICY_RESULTS", payload)
    report117.write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_PROCESS_POLICY_TRACE", trace_payload)
    return payload


def parse_args() -> Config:
    parser = argparse.ArgumentParser(description=__doc__)
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
    parser.add_argument("--policy-epochs", type=int, default=4)
    parser.add_argument("--policy-hidden-size", type=int, default=64)
    parser.add_argument("--policy-learning-rate", type=float, default=0.003)
    parser.add_argument("--memory-epochs", type=int, default=5)
    parser.add_argument("--memory-hidden-size", type=int, default=64)
    parser.add_argument("--memory-learning-rate", type=float, default=0.003)
    parser.add_argument("--process-epochs", type=int, default=5)
    parser.add_argument("--process-hidden-size", type=int, default=64)
    parser.add_argument("--process-learning-rate", type=float, default=0.003)
    parser.add_argument("--process-loss-coef", type=float, default=0.35)
    parser.add_argument("--entropy-coef", type=float, default=0.008)
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
        policy_epochs=args.policy_epochs,
        policy_hidden_size=args.policy_hidden_size,
        policy_learning_rate=args.policy_learning_rate,
        memory_epochs=args.memory_epochs,
        memory_hidden_size=args.memory_hidden_size,
        memory_learning_rate=args.memory_learning_rate,
        process_epochs=args.process_epochs,
        process_hidden_size=args.process_hidden_size,
        process_learning_rate=args.process_learning_rate,
        process_loss_coef=args.process_loss_coef,
        entropy_coef=args.entropy_coef,
        policy_temperature=args.policy_temperature,
        policy_bias_candidates=parse_floats(args.policy_bias_candidates),
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "experiment": "ssrm_3d_coupled_crisis_process_policy",
        "verdict": payload["verdict"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
