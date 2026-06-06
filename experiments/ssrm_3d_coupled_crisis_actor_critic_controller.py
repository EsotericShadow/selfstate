#!/usr/bin/env python3
"""Actor-critic baseline for SSRM-3D active coupled-crisis repair.

Report 119 showed that sampled active-crisis policy updates improve coupled
response but still leave held-out crisis score at zero. This benchmark adds the
next narrow ingredient: a learned critic baseline for completed crisis-window
return. The actor still chooses from the same supplied crisis action candidates,
but the update uses a value head rather than only a moving scalar baseline.

This is bounded actor-critic evidence. It is not open-ended civilization,
subjective consciousness, or a real-world agent. The base GRU remains
imitation-trained, crisis families remain structured, and the action candidate
set is supplied.
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
import ssrm_3d_coupled_crisis_joint_arbitration_controller as report113
import ssrm_3d_coupled_crisis_randomized_transfer_controller as report114
import ssrm_3d_coupled_crisis_rollout_window_controller as report111
import ssrm_3d_coupled_social_environment_maturation_controller as coupled
import ssrm_3d_learned_multiday_maturation_controller as base
import ssrm_3d_return_selected_multiday_maturation_controller as report105
from ssrm_maturation.agents import make_agents
from ssrm_maturation.environment import living
from ssrm_maturation.models import CONDITIONS, Condition, Agent, World, Trace


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_actor_critic"
ACTOR_CRITIC_SEED = 20261671
ACTION_CANDIDATES = report119.ACTION_CANDIDATES
ACTION_TO_INDEX = report119.ACTION_TO_INDEX
FIXED_JOINT = report119.FIXED_JOINT


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
    actor_critic_epochs: int = 4
    actor_critic_hidden_size: int = 64
    actor_critic_learning_rate: float = 0.003
    entropy_coef: float = 0.008
    value_coef: float = 0.45
    policy_temperature: float = 1.0
    policy_bias_candidates: Sequence[float] = (0.0, 0.20, 0.40, 0.70, 1.00)
    device: str = "auto"
    trace_seed: int = 20261121


@dataclass(frozen=True)
class ActorCriticTrainingRow:
    episodes: int
    crises: int
    epochs: int
    final_loss: float
    final_policy_loss: float
    final_value_loss: float
    mean_return: float
    return_std: float
    mean_value_prediction: float
    mean_abs_advantage: float
    mean_entropy: float
    policy_temperature: float
    entropy_coef: float
    value_coef: float
    device_used: str
    parameter_count: int


@dataclass(frozen=True)
class ActorCriticSelectionRow:
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
class ActorCriticVerdictRow:
    selected_router: str
    selected_policy_bias: float
    training_crises: int
    actor_critic_total_score: float
    active_policy_total_score: float
    fixed_joint_total_score: float
    return_selected_total_score: float
    actor_critic_crisis_score: float
    active_policy_crisis_score: float
    fixed_joint_crisis_score: float
    return_selected_crisis_score: float
    actor_critic_resolved_rate: float
    active_policy_resolved_rate: float
    fixed_joint_resolved_rate: float
    return_selected_resolved_rate: float
    actor_critic_coupled_response: float
    active_policy_coupled_response: float
    fixed_joint_coupled_response: float
    return_selected_coupled_response: float
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
    supports_active_policy_improvement: bool
    supports_return_baseline_improvement: bool
    supports_fixed_joint_improvement: bool
    supports_actor_critic_learning: bool
    supports_social_environment_dependency: bool
    verdict: str


class CrisisActorCriticNet(torch.nn.Module):
    def __init__(self, hidden_size: int) -> None:
        super().__init__()
        self.encoder = torch.nn.Sequential(
            torch.nn.Linear(report119.POLICY_INPUT_SIZE, hidden_size),
            torch.nn.LayerNorm(hidden_size),
            torch.nn.Tanh(),
            torch.nn.Linear(hidden_size, hidden_size),
            torch.nn.Tanh(),
        )
        self.actor = torch.nn.Linear(hidden_size, len(ACTION_CANDIDATES))
        self.critic = torch.nn.Linear(hidden_size, 1)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        hidden = self.encoder(x)
        return self.actor(hidden)

    def actor_critic(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        hidden = self.encoder(x)
        return self.actor(hidden), self.critic(hidden).squeeze(-1)


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def stdev(values: Sequence[float]) -> float:
    if len(values) < 2:
        return 0.0
    avg = mean(values)
    return (sum((value - avg) ** 2 for value in values) / len(values)) ** 0.5


def parse_ints(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def parse_floats(value: str) -> Tuple[float, ...]:
    return tuple(float(part.strip()) for part in value.split(",") if part.strip())


def sample_candidate_without_graph(
    model: CrisisActorCriticNet,
    features: Sequence[float],
    active: coupled.ActiveCrisis,
    action_counts: Dict[str, int],
    alive_count: int,
    world_time: float,
    device: torch.device,
    temperature: float,
) -> Tuple[str, List[float], int, float]:
    values = report119.policy_features(features, active, action_counts, alive_count, world_time, "none")
    with torch.no_grad():
        x = torch.tensor([values], dtype=torch.float32, device=device)
        logits = model(x) / max(0.05, temperature)
        logits = report119.masked_logits(logits, "none", 0.0)
        dist = torch.distributions.Categorical(logits=logits.squeeze(0))
        index = dist.sample()
        entropy = float(dist.entropy().detach().cpu().item())
    action_index = int(index.item())
    return ACTION_CANDIDATES[action_index], values, action_index, entropy


def run_actor_critic_training_episode(
    seed: int,
    cfg: Config,
    base_model: base.ControllerNet,
    actor_critic: CrisisActorCriticNet,
    optimizer: torch.optim.Optimizer,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[int, List[float], List[float], List[float], List[float], float, float, float]:
    condition = CONDITIONS[0]
    rng = random.Random(seed * 149 + ACTOR_CRITIC_SEED)
    agents = make_agents(rng, cfg.population)
    world = coupled.prepare_world(rng, cfg)
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
    pending_samples: List[Tuple[List[float], int]] = []
    pending_damage_start = tracker.damage_integral
    returns: List[float] = []
    value_predictions: List[float] = []
    abs_advantages: List[float] = []
    entropies: List[float] = []
    final_loss = 0.0
    final_policy_loss = 0.0
    final_value_loss = 0.0
    crises = 0
    actor_critic.train()

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        action_counts: Dict[str, int] = {}
        coupled.maybe_start_crisis(world, tracker, rng, events)
        if tracker.active is not None and not pending_samples:
            pending_damage_start = tracker.damage_integral
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
            if active is None:
                action = report117.learned_policy_action(agent, features, base_model, recurrent_states, router, device, "none")
            else:
                action, sampled_features, action_index, entropy = sample_candidate_without_graph(
                    actor_critic,
                    features,
                    active,
                    action_counts,
                    len(living(agents)),
                    current_world.time,
                    device,
                    cfg.policy_temperature,
                )
                if current_world.time >= 12.0:
                    pending_samples.append((sampled_features, action_index))
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
            reward = report119.crisis_window_return(active_before_completion, tracker.damage_integral - pending_damage_start)
            returns.append(reward)
            crises += 1
            if pending_samples:
                batch_x = torch.tensor([item[0] for item in pending_samples], dtype=torch.float32, device=device)
                batch_actions = torch.tensor([item[1] for item in pending_samples], dtype=torch.long, device=device)
                target = torch.full((len(pending_samples),), reward, dtype=torch.float32, device=device)
                logits, values = actor_critic.actor_critic(batch_x)
                logits = report119.masked_logits(logits / max(0.05, cfg.policy_temperature), "none", 0.0)
                dist = torch.distributions.Categorical(logits=logits)
                advantage = target - values.detach()
                log_probs = dist.log_prob(batch_actions)
                policy_loss = -(advantage * log_probs).mean()
                value_loss = torch.nn.functional.mse_loss(values, target)
                entropy_loss = dist.entropy().mean()
                loss = policy_loss + cfg.value_coef * value_loss - cfg.entropy_coef * entropy_loss
                optimizer.zero_grad()
                loss.backward()
                torch.nn.utils.clip_grad_norm_(actor_critic.parameters(), 2.0)
                optimizer.step()
                final_loss = float(loss.detach().cpu().item())
                final_policy_loss = float(policy_loss.detach().cpu().item())
                final_value_loss = float(value_loss.detach().cpu().item())
                value_predictions.extend(float(item) for item in values.detach().cpu().tolist())
                abs_advantages.extend(float(abs(item)) for item in advantage.detach().cpu().tolist())
            pending_samples = []
            pending_damage_start = tracker.damage_integral

    return crises, returns, value_predictions, abs_advantages, entropies, final_loss, final_policy_loss, final_value_loss


def train_actor_critic_model(
    cfg: Config,
    base_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[CrisisActorCriticNet, ActorCriticTrainingRow]:
    torch.manual_seed(ACTOR_CRITIC_SEED)
    model = CrisisActorCriticNet(cfg.actor_critic_hidden_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.actor_critic_learning_rate)
    all_returns: List[float] = []
    all_values: List[float] = []
    all_abs_advantages: List[float] = []
    all_entropy: List[float] = []
    total_crises = 0
    episodes = 0
    final_loss = 0.0
    final_policy_loss = 0.0
    final_value_loss = 0.0
    for epoch in range(cfg.actor_critic_epochs):
        for seed in cfg.train_seeds:
            crises, returns, values, abs_advantages, entropies, final_loss, final_policy_loss, final_value_loss = run_actor_critic_training_episode(
                seed + epoch * 1013,
                cfg,
                base_model,
                model,
                optimizer,
                device,
                router,
            )
            total_crises += crises
            all_returns.extend(returns)
            all_values.extend(values)
            all_abs_advantages.extend(abs_advantages)
            all_entropy.extend(entropies)
            episodes += 1
    model.eval()
    return model, ActorCriticTrainingRow(
        episodes=episodes,
        crises=total_crises,
        epochs=cfg.actor_critic_epochs,
        final_loss=final_loss,
        final_policy_loss=final_policy_loss,
        final_value_loss=final_value_loss,
        mean_return=mean(all_returns),
        return_std=stdev(all_returns),
        mean_value_prediction=mean(all_values),
        mean_abs_advantage=mean(all_abs_advantages),
        mean_entropy=mean(all_entropy),
        policy_temperature=cfg.policy_temperature,
        entropy_coef=cfg.entropy_coef,
        value_coef=cfg.value_coef,
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in model.parameters()),
    )


def run_actor_critic_episode(
    seed: int,
    cfg: Config,
    controller: str,
    model: Optional[base.ControllerNet],
    actor_critic: Optional[CrisisActorCriticNet],
    device: torch.device,
    router: report105.PressureRouter,
    policy_bias: float = 0.0,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, Trace, coupled.CrisisTracker]:
    delegated = "active_policy_gru" if controller == "actor_critic_gru" else controller
    row, trace_out, tracker = report119.run_active_policy_episode(
        seed,
        cfg,
        delegated,
        model,
        actor_critic,
        device,
        router,
        policy_bias=policy_bias,
        ablation=ablation,
        trace=trace,
    )
    if controller == "actor_critic_gru":
        row = replace(row, controller=controller)
        trace_out.condition = f"{controller}:{router.name}:policy_{policy_bias:g}:{ablation}"
    return row, trace_out, tracker


def selection_objective(rows: Sequence[coupled.EvalRow]) -> Tuple[float, float, float, float, float, float, float, float, float]:
    return report119.selection_objective(rows)


def select_actor_critic_bias(
    cfg: Config,
    model: base.ControllerNet,
    actor_critic: CrisisActorCriticNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[float, List[ActorCriticSelectionRow]]:
    rows: List[ActorCriticSelectionRow] = []
    best_bias = 0.0
    best_objective = -1e9
    for bias in cfg.policy_bias_candidates:
        eval_rows = [
            run_actor_critic_episode(
                seed,
                cfg,
                "actor_critic_gru",
                model,
                actor_critic,
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
        rows.append(ActorCriticSelectionRow(
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
    base_row = coupled.row_lookup(summary, "actor_critic_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in report113.ABLATIONS:
        row = coupled.row_lookup(summary, "actor_critic_gru", ablation)
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
    training: ActorCriticTrainingRow,
) -> ActorCriticVerdictRow:
    actor = coupled.row_lookup(summary, "actor_critic_gru", "none")
    active = coupled.row_lookup(summary, "active_policy_gru", "none")
    fixed = coupled.row_lookup(summary, "fixed_joint_gru", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    eval_schedules = [row for row in schedules if row.phase == "eval"]
    mean_crisis_count = mean(row.crisis_count for row in eval_schedules)
    supports_active = (
        training.crises > 0
        and actor.mean_total_score - active.mean_total_score >= 0.005
        and actor.mean_coupled_response_rate - active.mean_coupled_response_rate >= 0.040
        and actor.mean_resolved_rate - active.mean_resolved_rate >= 0.040
    )
    supports_return = (
        training.crises > 0
        and mean_crisis_count >= 4.0
        and actor.mean_total_score - returned.mean_total_score >= 0.010
        and actor.mean_crisis_score - returned.mean_crisis_score >= 0.040
        and actor.mean_resolved_rate - returned.mean_resolved_rate >= 0.080
        and actor.mean_coupled_response_rate - returned.mean_coupled_response_rate >= 0.080
        and actor.mean_alive_at_12h >= 12.0
        and actor.shock_gate_pass_rate == 1.0
        and actor.post_gate_shock_rate == 1.0
    )
    supports_fixed = (
        actor.mean_total_score - fixed.mean_total_score >= 0.005
        and actor.mean_crisis_score - fixed.mean_crisis_score >= 0.020
        and actor.mean_resolved_rate - fixed.mean_resolved_rate >= 0.020
        and actor.mean_coupled_response_rate - fixed.mean_coupled_response_rate >= 0.020
    )
    supports_dependency = (
        actor.mean_crisis_score > 0.0
        and social.coupled_response_loss >= 0.050
        and environment.coupled_response_loss >= 0.050
        and (social.crisis_score_loss >= 0.040 or social.resolved_rate_loss >= 0.080)
        and (environment.crisis_score_loss >= 0.040 or environment.resolved_rate_loss >= 0.080)
    )
    supports_actor_critic = supports_active and supports_return and supports_fixed
    return ActorCriticVerdictRow(
        selected_router=router.name,
        selected_policy_bias=selected_bias,
        training_crises=training.crises,
        actor_critic_total_score=actor.mean_total_score,
        active_policy_total_score=active.mean_total_score,
        fixed_joint_total_score=fixed.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        actor_critic_crisis_score=actor.mean_crisis_score,
        active_policy_crisis_score=active.mean_crisis_score,
        fixed_joint_crisis_score=fixed.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        actor_critic_resolved_rate=actor.mean_resolved_rate,
        active_policy_resolved_rate=active.mean_resolved_rate,
        fixed_joint_resolved_rate=fixed.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        actor_critic_coupled_response=actor.mean_coupled_response_rate,
        active_policy_coupled_response=active.mean_coupled_response_rate,
        fixed_joint_coupled_response=fixed.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        gain_over_active_policy=actor.mean_total_score - active.mean_total_score,
        gain_over_return_selected=actor.mean_total_score - returned.mean_total_score,
        gain_over_fixed_joint=actor.mean_total_score - fixed.mean_total_score,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=actor.shock_gate_pass_rate,
        post_gate_shock_rate=actor.post_gate_shock_rate,
        survival_at_12h=actor.mean_alive_at_12h,
        mean_crisis_count=mean_crisis_count,
        supports_active_policy_improvement=supports_active,
        supports_return_baseline_improvement=supports_return,
        supports_fixed_joint_improvement=supports_fixed,
        supports_actor_critic_learning=supports_actor_critic,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_actor_critic and supports_dependency else "partial_or_failed",
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
            20261681,
        )
        social_model, social_training = report113.train_action_model(
            cfg,
            device,
            "social",
            social_sequences,
            social_labels,
            flags,
            20261682,
        )
        active_policy_model, active_policy_training = report119.train_policy_model(cfg, models["gru"], device, selected_router)
        selected_active_bias, active_policy_selection = report119.select_policy_bias(cfg, models["gru"], active_policy_model, device, selected_router)
        actor_critic, actor_critic_training = train_actor_critic_model(cfg, models["gru"], device, selected_router)
        selected_bias, actor_critic_selection = select_actor_critic_bias(cfg, models["gru"], actor_critic, device, selected_router)

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
            actor_row, maybe_trace, tracker = run_actor_critic_episode(
                seed,
                cfg,
                "actor_critic_gru",
                models["gru"],
                actor_critic,
                device,
                selected_router,
                policy_bias=selected_bias,
                trace=(seed == cfg.trace_seed),
            )
            eval_rows.append(actor_row)
            crisis_logs[f"{seed}:actor_critic_gru:none"] = tracker.response_log
            if maybe_trace.frames:
                trace_out = maybe_trace
            for ablation in report113.ABLATIONS:
                row, _, tracker = run_actor_critic_episode(
                    seed,
                    cfg,
                    "actor_critic_gru",
                    models["gru"],
                    actor_critic,
                    device,
                    selected_router,
                    policy_bias=selected_bias,
                    ablation=ablation,
                )
                eval_rows.append(replace(row, ablation=ablation))
                crisis_logs[f"{seed}:actor_critic_gru:{ablation}"] = tracker.response_log

    summary = coupled.summarize(eval_rows)
    ablations = ablations_from_summary(summary)
    verdict = transfer_verdict(summary, ablations, selected_router, selected_bias, schedules, actor_critic_training)
    trace_payload = asdict(trace_out) if trace_out is not None else {"seed": cfg.trace_seed, "condition": "actor_critic_gru", "frames": []}
    trace_payload["condition"] = "actor_critic_gru"
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
            "actor_critic_epochs": cfg.actor_critic_epochs,
            "actor_critic_hidden_size": cfg.actor_critic_hidden_size,
            "actor_critic_learning_rate": cfg.actor_critic_learning_rate,
            "entropy_coef": cfg.entropy_coef,
            "value_coef": cfg.value_coef,
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
        "actor_critic_training": asdict(actor_critic_training),
        "actor_critic_selection": [asdict(row) for row in actor_critic_selection],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace_payload,
        "crisis_logs": crisis_logs,
        "notes": {
            "claim": "a learned critic baseline can improve sampled crisis-window policy learning",
            "not_claimed": "subjective consciousness, open-ended civilization, real-world competence, or full recurrent actor-critic training",
            "remaining_structure": "candidate repair actions are supplied, the base controller is imitation trained, and the actor-critic update uses completed crisis-window returns in an abstract simulator",
        },
    }
    report117.rows_to_csv(Path(f"{PREFIX}_schedule.csv"), schedules)
    report117.rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    report117.rows_to_csv(Path(f"{PREFIX}_action_training.csv"), [env_training, social_training])
    report117.rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    report117.rows_to_csv(Path(f"{PREFIX}_active_policy_training.csv"), [active_policy_training])
    report117.rows_to_csv(Path(f"{PREFIX}_active_policy_selection.csv"), active_policy_selection)
    report117.rows_to_csv(Path(f"{PREFIX}_actor_critic_training.csv"), [actor_critic_training])
    report117.rows_to_csv(Path(f"{PREFIX}_actor_critic_selection.csv"), actor_critic_selection)
    report117.rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    report117.rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    report117.rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    report117.rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    report117.write_json(Path(f"{PREFIX}_results.json"), payload)
    report117.write_json(Path(f"{PREFIX}_trace.json"), trace_payload)
    report117.write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_ACTOR_CRITIC_RESULTS", payload)
    report117.write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_ACTOR_CRITIC_TRACE", trace_payload)
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
    parser.add_argument("--policy-epochs", type=int, default=4)
    parser.add_argument("--policy-hidden-size", type=int, default=64)
    parser.add_argument("--policy-learning-rate", type=float, default=0.003)
    parser.add_argument("--actor-critic-epochs", type=int, default=4)
    parser.add_argument("--actor-critic-hidden-size", type=int, default=64)
    parser.add_argument("--actor-critic-learning-rate", type=float, default=0.003)
    parser.add_argument("--entropy-coef", type=float, default=0.008)
    parser.add_argument("--value-coef", type=float, default=0.45)
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
        actor_critic_epochs=args.actor_critic_epochs,
        actor_critic_hidden_size=args.actor_critic_hidden_size,
        actor_critic_learning_rate=args.actor_critic_learning_rate,
        entropy_coef=args.entropy_coef,
        value_coef=args.value_coef,
        policy_temperature=args.policy_temperature,
        policy_bias_candidates=parse_floats(args.policy_bias_candidates),
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "experiment": "ssrm_3d_coupled_crisis_actor_critic",
        "verdict": payload["verdict"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
