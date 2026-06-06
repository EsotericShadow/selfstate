#!/usr/bin/env python3
"""Outcome-value reranker for coupled SSRM-3D maturation crises.

Report 107 showed that a supervised repair-label critic is rejected by
validation return. This benchmark moves one step closer to the requested
long-running adaptation world by training a small action-value critic from
counterfactual crisis outcomes. The critic scores actions by predicted crisis
progress, unresolved damage, and whether the current group response is missing
environmental or social repair.

The controller still consumes ordinary symptom features plus current response
fractions. It does not receive the active crisis profile or scenario label. This
is not deep reinforcement learning, subjective consciousness, or open-ended
civilization.
"""

from __future__ import annotations

import argparse
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
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_outcome_value"

ENV_RESPONSE_ACTIONS = ("sanitize", "treat", "scout", "construct", "collect_water", "harvest_food")
SOCIAL_RESPONSE_ACTIONS = ("social_repair", "teach", "learn")
VALUE_INPUT_SIZE = base.FEATURE_COUNT + len(base.ACTIONS) + 2


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
    value_epochs: int = 70
    value_hidden_size: int = 64
    value_learning_rate: float = 0.003
    value_bias_candidates: Sequence[float] = (0.0, 1.0, 1.75, 2.75, 4.0, 5.5, 7.0)
    max_value_examples: int = 180000
    device: str = "auto"
    trace_seed: int = 20261021


@dataclass(frozen=True)
class ValueTrainingRow:
    train_loss: float
    pairwise_accuracy: float
    device_used: str
    parameter_count: int
    train_examples: int
    positive_examples: int
    value_epochs: int
    value_hidden_size: int


@dataclass(frozen=True)
class ValueSelectionRow:
    value_bias: float
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
    selected_value_bias: float
    outcome_value_total_score: float
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
    outcome_value_crisis_score: float
    return_selected_crisis_score: float
    outcome_value_resolved_rate: float
    return_selected_resolved_rate: float
    outcome_value_coupled_response: float
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
    supports_outcome_value_selection: bool
    supports_social_environment_dependency: bool
    verdict: str


class OutcomeValueNet(nn.Module):
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


def parse_ints(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def parse_floats(value: str) -> Tuple[float, ...]:
    return tuple(float(part.strip()) for part in value.split(",") if part.strip())


def one_hot_action(action: str) -> List[float]:
    index = base.ACTION_TO_INDEX[action]
    return [1.0 if item == index else 0.0 for item in range(len(base.ACTIONS))]


def value_input(features: Sequence[float], action: str, env_context: float, social_context: float) -> List[float]:
    return [*features, *one_hot_action(action), clamp(env_context), clamp(social_context)]


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
        return clamp(features[FEATURE["contamination"]] * 0.70 + max(0.0, 0.52 - features[FEATURE["sanitation"]]) * 0.30)
    if action == "treat":
        return clamp(features[FEATURE["disease"]] * 0.55 + features[FEATURE["illness"]] * 0.35 + max(0.0, 0.52 - features[FEATURE["medicine"]]) * -0.10)
    if action == "scout":
        return clamp(features[FEATURE["route_hazard"]] * 0.35 + features[FEATURE["resource_migration"]] * 0.30 + max(0.0, 0.56 - features[FEATURE["visibility"]]) * 0.22 + max(0.0, 0.48 - features[FEATURE["risk_memory"]]) * 0.12)
    if action == "construct":
        return clamp(max(0.0, 0.62 - features[FEATURE["shelter"]]) * 0.35 + max(0.0, 0.62 - features[FEATURE["architecture"]]) * 0.28 + max(0.0, 0.52 - features[FEATURE["paths"]]) * 0.15 + max(0.0, 0.50 - features[FEATURE["waterworks"]]) * 0.12)
    if action == "collect_water":
        return clamp(max(0.0, 0.56 - features[FEATURE["water"]]) * 0.55 + features[FEATURE["contamination"]] * 0.10)
    if action == "harvest_food":
        return clamp(max(0.0, 0.56 - features[FEATURE["food"]]) * 0.55 + features[FEATURE["resource_migration"]] * 0.10)
    if action == "social_repair":
        return clamp(features[FEATURE["conflict"]] * 0.55 + max(0.0, 0.62 - features[FEATURE["social_trust"]]) * 0.35)
    if action == "teach":
        return clamp(max(0.0, 0.74 - features[FEATURE["culture"]]) * 0.35 + max(0.0, 0.64 - features[FEATURE["risk_memory"]]) * 0.30 + max(0.0, 0.56 - features[FEATURE["symbols"]]) * 0.20 + max(0.0, 0.76 - features[FEATURE["knowledge_transfer"]]) * 0.15)
    if action == "learn":
        return clamp(max(0.0, 0.78 - features[FEATURE["knowledge_transfer"]]) * 0.30 + max(0.0, 0.62 - features[FEATURE["wisdom"]]) * 0.20)
    if action == "improve_tools":
        return clamp(max(0.0, 0.74 - features[FEATURE["tools"]]) * 0.45 + max(0.0, 0.58 - features[FEATURE["workshop"]]) * 0.28)
    return 0.0


def counterfactual_value(
    action: str,
    features: Sequence[float],
    active: coupled.ActiveCrisis,
    dt: float,
    alive_count: int,
    env_context: float,
    social_context: float,
) -> float:
    env_fraction = min(1.0, active.env_progress / active.profile.env_need)
    social_fraction = min(1.0, active.social_progress / active.profile.social_need)
    current_coupled = min(env_fraction, social_fraction)
    contribution = 1.0 / max(1, alive_count)
    action_env = contribution if action in active.profile.env_actions else 0.0
    action_social = contribution if action in active.profile.social_actions else 0.0
    env_effort = min(1.0, env_context + action_env)
    social_effort = min(1.0, social_context + action_social)
    next_env_fraction = min(1.0, (active.env_progress + env_effort * dt * 1.55) / active.profile.env_need)
    next_social_fraction = min(1.0, (active.social_progress + social_effort * dt * 1.65) / active.profile.social_need)
    next_coupled = min(next_env_fraction, next_social_fraction)
    coupled_gain = max(0.0, next_coupled - current_coupled)
    env_gap = 1.0 - env_fraction
    social_gap = 1.0 - social_fraction
    group_fit = 0.0
    if action in active.profile.env_actions:
        group_fit += env_gap * (1.0 - min(1.0, env_context * 2.5)) * 0.42
    if action in active.profile.social_actions:
        group_fit += social_gap * (1.0 - min(1.0, social_context * 2.8)) * 0.44
    repair_fit = symptom_fit(features, action) * 0.34
    skill_fit = action_skill(features, action) * 0.08
    non_response_cost = 0.13 if action not in (*active.profile.env_actions, *active.profile.social_actions) else 0.0
    if action in {"rest", "stay_near_shelter"} and features[FEATURE["energy"]] < 0.24:
        non_response_cost *= 0.35
    unresolved_after = 1.0 - next_coupled
    value = coupled_gain * 8.0 + group_fit + repair_fit + skill_fit - unresolved_after * 0.08 - non_response_cost
    return max(-0.45, min(1.25, value))


def collect_value_examples(cfg: Config) -> Tuple[List[List[float]], List[float]]:
    rng = random.Random(20261031)
    examples: List[List[float]] = []
    targets: List[float] = []
    condition = CONDITIONS[0]
    contexts = ((0.0, 0.0), (0.18, 0.0), (0.0, 0.18), (0.18, 0.18), (0.32, 0.12), (0.12, 0.32))
    for seed in cfg.train_seeds:
        world_rng = random.Random(seed * 113 + 53)
        agents = make_agents(world_rng, cfg.population)
        world = coupled.prepare_world(world_rng, cfg)
        previous_actions: Dict[str, int] = {}
        events: List[str] = []
        tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))

        while world.time < cfg.hours - 1e-9 and len(examples) < cfg.max_value_examples:
            dt = min(cfg.step_hours, cfg.hours - world.time)
            action_counts: Dict[str, int] = {}
            coupled.maybe_start_crisis(world, tracker, world_rng, events)
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
                if active is not None and current_world.time >= 12.0 and len(examples) < cfg.max_value_examples:
                    if rng.random() < 0.34:
                        for env_context, social_context in rng.sample(contexts, k=2):
                            for action in base.ACTIONS:
                                examples.append(value_input(features, action, env_context, social_context))
                                targets.append(counterfactual_value(action, features, active, dt, max(1, len(living(agents))), env_context, social_context))
                                if len(examples) >= cfg.max_value_examples:
                                    break
                            if len(examples) >= cfg.max_value_examples:
                                break
                action = report107.crisis_target_action(tracker.active, features) if tracker.active is not None else choose_action(agent, current_world, current_condition, current_rng)
                action_counts[action] = action_counts.get(action, 0) + 1
                return action

            base.step_world(world, agents, condition, dt, world_rng, previous_actions, selector, events)
            coupled.update_crisis_after_actions(world, agents, tracker, action_counts, dt)
            coupled.complete_crisis_if_due(world, agents, tracker, events)
    return examples, targets


def train_value_model(cfg: Config, device: torch.device) -> Tuple[OutcomeValueNet, ValueTrainingRow]:
    examples, targets = collect_value_examples(cfg)
    if not examples:
        raise RuntimeError("no outcome-value examples collected")
    torch.manual_seed(20261041)
    x = torch.tensor(examples, dtype=torch.float32, device=device)
    y = torch.tensor(targets, dtype=torch.float32, device=device)
    model = OutcomeValueNet(VALUE_INPUT_SIZE, cfg.value_hidden_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.value_learning_rate)
    sample_weights = 1.0 + torch.clamp(y, min=0.0) * 3.0 + (y > 0.20).float() * 8.0
    for _ in range(cfg.value_epochs):
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
    return model, ValueTrainingRow(
        train_loss=loss,
        pairwise_accuracy=pairwise_accuracy,
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in model.parameters()),
        train_examples=len(examples),
        positive_examples=sum(1 for target in targets if target > 0.20),
        value_epochs=cfg.value_epochs,
        value_hidden_size=cfg.value_hidden_size,
    )


def outcome_value_bias(
    features: Sequence[float],
    value_model: OutcomeValueNet,
    value_bias: float,
    device: torch.device,
    dtype: torch.dtype,
    ablation: str,
    env_context: float,
    social_context: float,
) -> torch.Tensor:
    gate = report107.repair_gate(features, ablation)
    bias = torch.zeros((1, len(base.ACTIONS)), dtype=dtype, device=device)
    if value_bias <= 0.0 or gate <= 0.0:
        return bias
    masked = base.mask_features(list(features), ablation)
    batch = torch.tensor(
        [value_input(masked, action, env_context, social_context) for action in base.ACTIONS],
        dtype=torch.float32,
        device=device,
    )
    values = value_model(batch)
    values = (values - values.mean()) / (values.std(unbiased=False) + 1e-4)
    values = torch.clamp(values, -1.8, 1.8)
    return values.reshape(1, -1).to(dtype=dtype) * value_bias * gate


def run_episode(
    seed: int,
    cfg: Config,
    controller: str,
    model: Optional[base.ControllerNet],
    device: torch.device,
    router: report105.PressureRouter,
    value_model: Optional[OutcomeValueNet] = None,
    value_bias: float = 0.0,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, Trace, coupled.CrisisTracker]:
    if controller != "outcome_value_gru":
        return coupled.run_episode(seed, cfg, controller, model, device, router, ablation=ablation, trace=trace)
    if model is None or value_model is None:
        raise ValueError("outcome_value_gru requires both base model and outcome value model")

    condition = CONDITIONS[0]
    rng = random.Random(seed * 127 + sum(ord(ch) for ch in controller + router.name + ablation) + int(value_bias * 1000))
    agents = make_agents(rng, cfg.population)
    world = coupled.prepare_world(rng, cfg)
    baseline = base.initial_baseline(world, cfg.population)
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
    trace_out = Trace(seed=seed, condition=f"{controller}:{router.name}:bias_{value_bias:g}:{ablation}")
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
            model_features = torch.tensor([base.mask_features(features, ablation)], dtype=torch.float32, device=device)
            with torch.no_grad():
                state = recurrent_states.get(agent.ident)
                logits, next_state = model.step(model_features, state)
                if next_state is not None:
                    recurrent_states[agent.ident] = next_state.detach()
                logits = logits + report105.router_bias(features, router, device, logits.dtype, ablation)
                logits = logits + outcome_value_bias(features, value_model, value_bias, device, logits.dtype, ablation, env_context, social_context)
                action = base.INDEX_TO_ACTION[int(logits.argmax(dim=-1).item())]
            action_counts[action] = action_counts.get(action, 0) + 1
            return action

        base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
        coupled.update_crisis_after_actions(world, agents, tracker, action_counts, dt)
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
    objective = total + crisis * 0.10 + resolved * 0.08 + coupled_response * 0.06 - damage * 0.18
    return total, maturation, crisis, resolved, coupled_response, objective


def select_value_bias(
    cfg: Config,
    model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
    value_model: OutcomeValueNet,
) -> Tuple[float, List[ValueSelectionRow]]:
    best = cfg.value_bias_candidates[0]
    best_objective = -1.0
    rows: List[ValueSelectionRow] = []
    for bias in cfg.value_bias_candidates:
        eval_rows = [
            run_episode(seed, cfg, "outcome_value_gru", model, device, router, value_model, bias)[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, coupled_response, objective = selection_objective(eval_rows)
        damage = mean(row.crisis_damage for row in eval_rows)
        if objective > best_objective:
            best = bias
            best_objective = objective
        rows.append(
            ValueSelectionRow(
                value_bias=bias,
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
        ValueSelectionRow(
            row.value_bias,
            row.tune_total_score,
            row.tune_maturation_score,
            row.tune_crisis_score,
            row.tune_resolved_rate,
            row.tune_coupled_response,
            row.tune_damage,
            row.selection_objective,
            row.value_bias == best,
        )
        for row in rows
    ]


def ablations_from_summary(summary: Sequence[coupled.SummaryRow]) -> List[coupled.AblationRow]:
    base_row = coupled.row_lookup(summary, "outcome_value_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in ("body", "infrastructure", "tools", "social_culture", "environment", "previous_action"):
        row = coupled.row_lookup(summary, "outcome_value_gru", ablation)
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
    selected_value_bias: float,
) -> VerdictRow:
    outcome = coupled.row_lookup(summary, "outcome_value_gru", "none")
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
        selected_value_bias > 0.0
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
        selected_value_bias=selected_value_bias,
        outcome_value_total_score=outcome.mean_total_score,
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
        outcome_value_crisis_score=outcome.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        outcome_value_resolved_rate=outcome.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        outcome_value_coupled_response=outcome.mean_coupled_response_rate,
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
        supports_outcome_value_selection=supports_selection,
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
    value_model, value_training = train_value_model(cfg, device)
    selected_bias, value_selection = select_value_bias(cfg, models["gru"], device, selected_router, value_model)

    eval_rows: List[coupled.EvalRow] = []
    trace = Trace(seed=cfg.trace_seed, condition=f"outcome_value_gru:{selected_router.name}:bias_{selected_bias:g}:none")
    crisis_logs: Dict[str, List[dict[str, object]]] = {}
    for seed in cfg.eval_seeds:
        for controller, model, router, value_net, bias in (
            ("designed", None, report105.ROUTERS[0], None, 0.0),
            ("reactive", None, report105.ROUTERS[0], None, 0.0),
            ("frame_mlp", models["frame_mlp"], report105.ROUTERS[0], None, 0.0),
            ("gru", models["gru"], report105.ROUTERS[0], None, 0.0),
            ("return_selected_gru", models["gru"], selected_router, None, 0.0),
            ("outcome_value_gru", models["gru"], selected_router, value_model, selected_bias),
        ):
            row, maybe_trace, tracker = run_episode(
                seed,
                cfg,
                controller,
                model,
                device,
                router,
                value_net,
                bias,
                trace=(seed == cfg.trace_seed and controller == "outcome_value_gru"),
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
                "outcome_value_gru",
                models["gru"],
                device,
                selected_router,
                value_model,
                selected_bias,
                ablation=ablation,
            )
            eval_rows.append(row)
            crisis_logs[f"{seed}:outcome_value_gru:{ablation}"] = tracker.response_log

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
            "value_epochs": cfg.value_epochs,
            "value_hidden_size": cfg.value_hidden_size,
            "value_bias_candidates": list(cfg.value_bias_candidates),
            "max_value_examples": cfg.max_value_examples,
            "device": cfg.device,
            "trace_seed": cfg.trace_seed,
        },
        "crisis_profiles": [asdict(profile) for profile in coupled.PROFILES],
        "routers": [asdict(router) for router in report105.ROUTERS],
        "router_selection": [asdict(row) for row in router_selection],
        "value_selection": [asdict(row) for row in value_selection],
        "base_training": [asdict(row) for row in training_rows],
        "value_training": asdict(value_training),
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": asdict(trace),
        "crisis_logs": crisis_logs,
        "notes": {
            "claim": "counterfactual outcome-value reranking for coupled social/environment crisis pressure",
            "not_claimed": "deep reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
            "input_discipline": "the value critic consumes ordinary features, action identity, and current response fractions but not active crisis profile labels",
        },
    }
    rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    rows_to_csv(Path(f"{PREFIX}_value_training.csv"), [value_training])
    rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    rows_to_csv(Path(f"{PREFIX}_value_selection.csv"), value_selection)
    rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    write_json(Path(f"{PREFIX}_results.json"), payload)
    write_json(Path(f"{PREFIX}_trace.json"), asdict(trace))
    write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_OUTCOME_VALUE_RESULTS", payload)
    write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_OUTCOME_VALUE_TRACE", asdict(trace))
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
    parser.add_argument("--value-epochs", type=int, default=70)
    parser.add_argument("--value-hidden-size", type=int, default=64)
    parser.add_argument("--value-learning-rate", type=float, default=0.003)
    parser.add_argument("--value-bias-candidates", default="0.00,1.00,1.75,2.75,4.00,5.50,7.00")
    parser.add_argument("--max-value-examples", type=int, default=180000)
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
        value_epochs=args.value_epochs,
        value_hidden_size=args.value_hidden_size,
        value_learning_rate=args.value_learning_rate,
        value_bias_candidates=parse_floats(args.value_bias_candidates),
        max_value_examples=args.max_value_examples,
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({"value_selection": payload["value_selection"], "verdict": payload["verdict"], "summary": payload["summary"]}, indent=2))
    # A failed outcome-value verdict is evidence, not a process failure.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
