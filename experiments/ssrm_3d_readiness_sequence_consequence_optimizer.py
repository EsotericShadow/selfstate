#!/usr/bin/env python3
"""Sequence-consequence readiness optimizer for SSRM-3D.

Report 137 repaired survival by relabeling the readiness learner's own failed
states, but it still did not produce knowledge transfer, strong readiness, or
stable ablation dependence. This benchmark tests the next boundary: short
multi-action consequence search over student-created readiness states, followed
by recurrent distillation of those sequence choices.

The sequence optimizer is a bounded planning bridge with cloned simulator
lookahead. The distilled GRU is the planner-free learner. A failed distillation
verdict is still a completed result and exits cleanly.
"""

from __future__ import annotations

import argparse
import copy
import json
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import torch

import ssrm_3d_environment_readiness_maturation as env
import ssrm_3d_learned_environment_readiness_controller as learned
import ssrm_3d_readiness_closed_loop_recovery_controller as recovery


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = "ssrm_3d_readiness_sequence_consequence"
ABLATIONS = recovery.ABLATIONS

PLAN_LIBRARY: Dict[str, Tuple[str, ...]] = {
    "survival": ("collect_water", "harvest_food", "sanitize", "treat", "rest", "gather_fuel"),
    "readiness": ("gather_fuel", "scout", "construct", "improve_tools", "repair_strain", "control_pests", "teach"),
    "build_tools": ("construct", "improve_tools", "construct", "repair_strain", "gather_fuel", "teach"),
    "culture": ("teach", "learn", "teach", "construct", "improve_tools", "social_repair"),
    "ecology": ("scout", "control_pests", "harvest_food", "gather_fuel", "construct", "teach"),
    "repair": ("repair_strain", "sanitize", "control_pests", "treat", "construct", "teach"),
}


@dataclass(frozen=True)
class Config:
    behavior_train_seeds: Sequence[int]
    recovery_seeds: Sequence[int]
    sequence_seeds: Sequence[int]
    eval_seeds: Sequence[int]
    hours: float = 72.0
    step_hours: float = 0.10
    population: int = 14
    epochs: int = 52
    recovery_epochs: int = 42
    sequence_epochs: int = 38
    hidden_size: int = 72
    learning_rate: float = 0.0035
    recovery_learning_rate: float = 0.0022
    sequence_learning_rate: float = 0.0020
    plan_horizon_hours: float = 2.4
    plan_commit_hours: float = 0.8
    sample_interval_hours: float = 1.2
    max_sequence_examples: int = 900
    device: str = "cpu"
    trace_seed: int = 20261321


@dataclass(frozen=True)
class SequenceCollectionRow:
    seed: int
    sampled_examples: int
    selected_plans: str
    mean_selected_score: float
    mean_runner_up_score: float
    mean_plan_margin: float
    mean_label_weight: float
    final_sequence_alive: int
    final_sequence_readiness: float
    final_sequence_knowledge: float
    final_sequence_score: float


@dataclass(frozen=True)
class PlanEvalRow:
    seed: int
    controller: str
    condition: str
    selected_plans: str
    final_alive: int
    final_readiness: float
    knowledge_transfer: float
    final_structural_strain: float
    final_pest_pressure: float
    maturation_score: float


@dataclass(frozen=True)
class VerdictRow:
    sequence_optimizer_score: float
    sequence_gru_score: float
    recovery_score: float
    behavior_score: float
    designed_score: float
    reactive_score: float
    sequence_optimizer_gain_over_recovery: float
    sequence_gru_gain_over_recovery: float
    sequence_optimizer_gap_to_designed: float
    sequence_gru_gap_to_optimizer: float
    sequence_optimizer_final_alive: float
    sequence_gru_final_alive: float
    sequence_optimizer_final_readiness: float
    sequence_gru_final_readiness: float
    sequence_optimizer_knowledge_transfer: float
    sequence_gru_knowledge_transfer: float
    body_ablation_loss: float
    infrastructure_ablation_loss: float
    tools_ablation_loss: float
    social_culture_ablation_loss: float
    environment_ablation_loss: float
    readiness_ablation_loss: float
    previous_action_ablation_loss: float
    supports_sequence_consequence_bridge: bool
    supports_planner_free_distillation: bool
    supports_ablation_specificity: bool
    verdict: str


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def parse_seed_list(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def recovery_config(cfg: Config) -> recovery.Config:
    return recovery.Config(
        behavior_train_seeds=tuple(cfg.behavior_train_seeds),
        recovery_seeds=tuple(cfg.recovery_seeds),
        eval_seeds=tuple(cfg.eval_seeds),
        hours=cfg.hours,
        step_hours=cfg.step_hours,
        population=cfg.population,
        epochs=cfg.epochs,
        recovery_epochs=cfg.recovery_epochs,
        hidden_size=cfg.hidden_size,
        learning_rate=cfg.learning_rate,
        recovery_learning_rate=cfg.recovery_learning_rate,
        device=cfg.device,
        trace_seed=cfg.trace_seed,
    )


def learned_config(cfg: Config) -> learned.Config:
    return learned.Config(
        train_seeds=tuple(cfg.behavior_train_seeds),
        eval_seeds=tuple(cfg.eval_seeds),
        hours=cfg.hours,
        step_hours=cfg.step_hours,
        population=cfg.population,
        epochs=cfg.epochs,
        hidden_size=cfg.hidden_size,
        learning_rate=cfg.learning_rate,
        device=cfg.device,
        trace_seed=cfg.trace_seed,
    )


def train_recovery_stack(
    cfg: Config,
    device: torch.device,
) -> Tuple[
    learned.ControllerNet,
    learned.ControllerNet,
    learned.ControllerNet,
    List[recovery.TrainingRow],
    List[recovery.CollectionRow],
    List[List[List[float]]],
    List[List[int]],
    List[List[float]],
]:
    rcfg = recovery_config(cfg)
    lcfg = learned_config(cfg)
    teacher_sequences, teacher_labels = learned.collect_sequences(lcfg)
    teacher_weights = [[1.0 for _ in labels] for labels in teacher_labels]
    x, y, mask, weights = recovery.build_weighted_tensors(teacher_sequences, teacher_labels, teacher_weights, device)
    training_rows: List[recovery.TrainingRow] = []

    frame_model, row = recovery.train_weighted_model(
        "frame_mlp",
        x,
        y,
        mask,
        weights,
        rcfg,
        device,
        "behavior",
        "designed_teacher_traces",
        cfg.epochs,
        cfg.learning_rate,
        0,
        0,
    )
    training_rows.append(row)
    behavior_model, row = recovery.train_weighted_model(
        "gru",
        x,
        y,
        mask,
        weights,
        rcfg,
        device,
        "behavior",
        "designed_teacher_traces",
        cfg.epochs,
        cfg.learning_rate,
        17,
        0,
    )
    training_rows.append(row)

    pass1_sequences, pass1_labels, pass1_weights, pass1_rows = recovery.collect_recovery_sequences(
        rcfg, behavior_model, device, cfg.recovery_seeds, "student_recovery_1"
    )
    aggregate_sequences = list(teacher_sequences) + pass1_sequences
    aggregate_labels = list(teacher_labels) + pass1_labels
    aggregate_weights = list(teacher_weights) + pass1_weights
    x1, y1, mask1, weights1 = recovery.build_weighted_tensors(aggregate_sequences, aggregate_labels, aggregate_weights, device)
    recovery_stage1, row = recovery.train_weighted_model(
        "gru",
        x1,
        y1,
        mask1,
        weights1,
        rcfg,
        device,
        "recovery_stage_1",
        "teacher_traces_plus_student_visited_states",
        cfg.recovery_epochs,
        cfg.recovery_learning_rate,
        137,
        sum(len(labels) for labels in pass1_labels),
    )
    training_rows.append(row)

    shifted_seeds = tuple(seed + 1000 for seed in cfg.recovery_seeds)
    pass2_sequences, pass2_labels, pass2_weights, pass2_rows = recovery.collect_recovery_sequences(
        rcfg, recovery_stage1, device, shifted_seeds, "student_recovery_2"
    )
    aggregate_sequences = aggregate_sequences + pass2_sequences
    aggregate_labels = aggregate_labels + pass2_labels
    aggregate_weights = aggregate_weights + pass2_weights
    x2, y2, mask2, weights2 = recovery.build_weighted_tensors(aggregate_sequences, aggregate_labels, aggregate_weights, device)
    recovery_model, row = recovery.train_weighted_model(
        "gru",
        x2,
        y2,
        mask2,
        weights2,
        rcfg,
        device,
        "recovery_final",
        "teacher_traces_plus_two_student_recovery_passes",
        cfg.recovery_epochs,
        cfg.recovery_learning_rate,
        197,
        sum(len(labels) for labels in pass1_labels) + sum(len(labels) for labels in pass2_labels),
    )
    training_rows.append(row)
    return frame_model, behavior_model, recovery_model, training_rows, pass1_rows + pass2_rows, aggregate_sequences, aggregate_labels, aggregate_weights


def plan_action(plan: str, agent: env.Agent, world: env.World, step_index: int) -> str:
    if agent.child:
        if agent.health < 0.58 or agent.energy < 0.30:
            return "rest"
        return "learn" if world.apprenticeship > 0.20 or world.culture > 0.20 else "stay_near_shelter"
    if agent.energy < 0.18 or agent.health < 0.36:
        return "rest"
    if agent.illness > 0.42 or world.disease + world.contamination > 0.72:
        return "sanitize" if world.sanitation < 0.55 else "treat"
    if agent.thirst > 0.76 or world.water < 0.34:
        return "collect_water"
    if agent.hunger > 0.76 or world.food < 0.34:
        return "harvest_food"
    actions = PLAN_LIBRARY[plan]
    offset = int(agent.ident[1:]) if agent.ident[1:].isdigit() else 0
    action = actions[(step_index + offset) % len(actions)]
    if action == "repair_strain" and world.structural_strain < 0.20:
        return "construct"
    if action == "control_pests" and world.pest_pressure < 0.18:
        return "harvest_food"
    if action == "learn" and not agent.child:
        return "teach"
    return action


def state_value(world: env.World, agents: List[env.Agent], start: Dict[str, float]) -> float:
    alive = env.living(agents)
    alive_ratio = len(alive) / max(1, len(agents))
    readiness = env.environment_readiness(world)
    knowledge = env.clamp(
        world.knowledge_transfer * 0.46
        + world.apprenticeship * 0.26
        + world.culture * 0.18
        + world.symbols * 0.12
        + env.safe_mean(agent.wisdom for agent in alive) * 0.08
    )
    development = env.clamp(
        max(0.0, world.architecture - start["architecture"]) * 0.30
        + max(0.0, env.tool_system(world) - start["tool_system"]) * 0.28
        + max(0.0, world.shelter - start["shelter"]) * 0.08
        + max(0.0, world.waterworks - start["waterworks"]) * 0.08
        + max(0.0, world.granary - start["granary"]) * 0.08
        + max(0.0, world.paths - start["paths"]) * 0.06
        + readiness * 0.18
    )
    pressure_reduction = env.clamp(
        max(0.0, start["structural_strain"] - world.structural_strain) * 0.34
        + max(0.0, start["pest_pressure"] - world.pest_pressure) * 0.24
        + max(0.0, start["disease"] - world.disease) * 0.20
        + max(0.0, start["contamination"] - world.contamination) * 0.18
    )
    future_resilience = env.clamp(
        (1.0 - world.structural_strain) * 0.18
        + (1.0 - world.pest_pressure) * 0.14
        + (1.0 - world.disease) * 0.12
        + world.fuel_reserve * 0.12
        + world.seed_bank * 0.12
        + world.forecast_memory * 0.12
        + world.apprenticeship * 0.16
    )
    return env.clamp(
        alive_ratio * 0.20
        + readiness * 0.22
        + knowledge * 0.22
        + development * 0.18
        + pressure_reduction * 0.08
        + future_resilience * 0.10
        + max(0.0, readiness - start["readiness"]) * 0.06
        + max(0.0, knowledge - start["knowledge"]) * 0.06
    )


def value_baseline(world: env.World) -> Dict[str, float]:
    return {
        "readiness": env.environment_readiness(world),
        "knowledge": env.clamp(world.knowledge_transfer * 0.46 + world.apprenticeship * 0.26 + world.culture * 0.18 + world.symbols * 0.12),
        "architecture": world.architecture,
        "tool_system": env.tool_system(world),
        "shelter": world.shelter,
        "waterworks": world.waterworks,
        "granary": world.granary,
        "paths": world.paths,
        "structural_strain": world.structural_strain,
        "pest_pressure": world.pest_pressure,
        "disease": world.disease,
        "contamination": world.contamination,
    }


def candidate_score(
    world: env.World,
    agents: List[env.Agent],
    previous_actions: Dict[str, int],
    rng_state: object,
    cfg: Config,
    plan: str,
) -> float:
    trial_world = copy.deepcopy(world)
    trial_agents = copy.deepcopy(agents)
    trial_previous = dict(previous_actions)
    trial_rng = random.Random()
    trial_rng.setstate(rng_state)
    condition = env.CONDITIONS[0]
    events: List[str] = []
    start = value_baseline(trial_world)
    horizon_steps = max(1, int(round(cfg.plan_horizon_hours / cfg.step_hours)))
    for step_index in range(horizon_steps):
        dt = min(cfg.step_hours, max(0.0, cfg.plan_horizon_hours - step_index * cfg.step_hours))

        def selector(
            agent: env.Agent,
            current_world: env.World,
            current_condition: env.Condition,
            current_rng: random.Random,
            features: List[float],
            previous: int,
        ) -> str:
            return plan_action(plan, agent, current_world, step_index)

        learned.step_world(trial_world, trial_agents, condition, dt, trial_rng, trial_previous, selector, events)
        if not env.living(trial_agents):
            break
    return state_value(trial_world, trial_agents, start)


def select_plan(
    world: env.World,
    agents: List[env.Agent],
    previous_actions: Dict[str, int],
    rng: random.Random,
    cfg: Config,
) -> Tuple[str, float, float, float]:
    rng_state = rng.getstate()
    scored = [
        (candidate_score(world, agents, previous_actions, rng_state, cfg, plan), plan)
        for plan in PLAN_LIBRARY
    ]
    scored.sort(reverse=True)
    best_score, best_plan = scored[0]
    runner_up = scored[1][0] if len(scored) > 1 else best_score
    return best_plan, best_score, runner_up, best_score - runner_up


def sequence_label_weight(world: env.World, margin: float) -> float:
    readiness_deficit = mean(
        max(0.0, 0.65 - value)
        for value in (
            world.fuel_reserve,
            world.seed_bank,
            world.building_blueprints,
            world.tool_blueprints,
            world.forecast_memory,
            world.apprenticeship,
        )
    )
    culture_deficit = mean(max(0.0, 0.55 - value) for value in (world.knowledge_transfer, world.apprenticeship, world.culture, world.symbols))
    risk = max(world.structural_strain, world.pest_pressure, world.disease, world.contamination)
    return min(10.0, 2.0 + readiness_deficit * 2.2 + culture_deficit * 2.4 + risk * 1.2 + max(0.0, margin) * 8.0)


def eval_row_from_episode(seed: int, controller: str, condition: str, episode: env.EpisodeRow) -> learned.EvalRow:
    return learned.EvalRow(
        seed=seed,
        controller=controller,
        ablation=condition,
        final_alive=episode.final_alive,
        total_agents=episode.total_agents,
        alive_at_12h=episode.alive_at_12h,
        no_major_shock_before_12h=episode.no_major_shock_before_12h,
        post_gate_shock=episode.post_gate_shock,
        major_shocks=episode.major_shocks,
        first_shock_hour=episode.first_shock_hour,
        births=episode.births,
        deaths=episode.deaths,
        readiness_at_12h=episode.readiness_at_12h,
        final_readiness=episode.final_readiness,
        readiness_delta=episode.readiness_delta,
        final_pest_pressure=episode.final_pest_pressure,
        final_structural_strain=episode.final_structural_strain,
        final_fuel_reserve=episode.final_fuel_reserve,
        final_seed_bank=episode.final_seed_bank,
        final_building_blueprints=episode.final_building_blueprints,
        final_tool_blueprints=episode.final_tool_blueprints,
        final_forecast_memory=episode.final_forecast_memory,
        final_apprenticeship=episode.final_apprenticeship,
        architecture_delta=episode.architecture_delta,
        tool_system_delta=episode.tool_system_delta,
        knowledge_transfer=episode.knowledge_transfer,
        adaptation_evidence=episode.adaptation_evidence,
        pressure_integral=episode.pressure_integral,
        survival_score=episode.survival_score,
        readiness_score=episode.readiness_score,
        development_score=episode.development_score,
        knowledge_score=episode.knowledge_score,
        resilience_score=episode.resilience_score,
        maturation_score=episode.maturation_score,
    )


def run_sequence_episode(
    seed: int,
    cfg: Config,
    controller: str = "sequence_optimizer",
    trace: bool = False,
    collect_labels: bool = False,
    max_examples: Optional[int] = None,
) -> Tuple[learned.EvalRow, env.Trace, Dict[str, List[List[float]]], Dict[str, List[int]], Dict[str, List[float]], SequenceCollectionRow]:
    condition = env.CONDITIONS[0]
    rng = random.Random(seed * 157 + sum(ord(ch) for ch in controller))
    agents = env.make_agents(rng, cfg.population)
    world = env.make_world(rng)
    baseline = learned.initial_baseline(world, cfg.population)
    previous_actions: Dict[str, int] = {}
    events: List[str] = []
    trace_out = env.Trace(seed=seed, condition=controller)
    checkpoints = list(env.TRACE_CHECKPOINTS)
    no_pre_gate_shock = True
    alive_at_12h = cfg.population
    at_12: Dict[str, float] = {}
    active_plan = "readiness"
    remaining_steps = 0
    plan_step = 0
    selected_scores: List[float] = []
    runner_scores: List[float] = []
    margins: List[float] = []
    plan_counts: Dict[str, int] = {plan: 0 for plan in PLAN_LIBRARY}
    label_weights: List[float] = []
    sequences: Dict[str, List[List[float]]] = {}
    labels: Dict[str, List[int]] = {}
    weights: Dict[str, List[float]] = {}
    total_examples = 0
    next_sample = 0.0
    max_examples = cfg.max_sequence_examples if max_examples is None else max_examples

    if trace:
        trace_out.frames.append(env.snapshot(world, agents, "0h", events))
        if checkpoints and checkpoints[0] == 0.0:
            checkpoints.pop(0)

    while world.time < cfg.hours - 1e-9:
        if remaining_steps <= 0:
            active_plan, selected, runner_up, margin = select_plan(world, agents, previous_actions, rng, cfg)
            remaining_steps = max(1, int(round(cfg.plan_commit_hours / cfg.step_hours)))
            plan_step = 0
            selected_scores.append(selected)
            runner_scores.append(runner_up)
            margins.append(margin)
            plan_counts[active_plan] += 1
        sample_this_step = collect_labels and world.time >= next_sample - 1e-9 and total_examples + len(env.living(agents)) <= max_examples
        if sample_this_step:
            next_sample += cfg.sample_interval_hours
        dt = min(cfg.step_hours, cfg.hours - world.time)
        current_plan = active_plan
        current_plan_step = plan_step
        current_margin = margins[-1] if margins else 0.0

        def selector(
            agent: env.Agent,
            current_world: env.World,
            current_condition: env.Condition,
            current_rng: random.Random,
            features: List[float],
            previous: int,
        ) -> str:
            action = plan_action(current_plan, agent, current_world, current_plan_step)
            if sample_this_step:
                key = f"sequence:{seed}:{agent.ident}"
                weight = sequence_label_weight(current_world, current_margin)
                sequences.setdefault(key, []).append(features)
                labels.setdefault(key, []).append(learned.ACTION_TO_INDEX.get(action, learned.DEFAULT_ACTION))
                weights.setdefault(key, []).append(weight)
                label_weights.append(weight)
            return action

        before_examples = sum(len(values) for values in labels.values())
        learned.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
        after_examples = sum(len(values) for values in labels.values())
        total_examples += after_examples - before_examples
        remaining_steps -= 1
        plan_step += 1
        if world.time < 12.0 and world.major_shocks > 0:
            no_pre_gate_shock = False
        if world.time >= 12.0 and not at_12:
            alive_at_12h = len(env.living(agents))
            at_12 = {"readiness": env.environment_readiness(world)}
        while trace and checkpoints and world.time >= checkpoints[0] - 1e-9:
            hour = checkpoints.pop(0)
            trace_out.frames.append(env.snapshot(world, agents, f"{hour:g}h", events))

    if trace and (not trace_out.frames or trace_out.frames[-1]["hours"] < cfg.hours):
        trace_out.frames.append(env.snapshot(world, agents, f"{cfg.hours:g}h", events))

    episode = env.score_episode(world, agents, baseline, at_12, seed, condition, alive_at_12h, no_pre_gate_shock)
    row = eval_row_from_episode(seed, controller, "none", episode)
    collection = SequenceCollectionRow(
        seed=seed,
        sampled_examples=total_examples,
        selected_plans=json.dumps({plan: count for plan, count in plan_counts.items() if count}, sort_keys=True),
        mean_selected_score=mean(selected_scores),
        mean_runner_up_score=mean(runner_scores),
        mean_plan_margin=mean(margins),
        mean_label_weight=mean(label_weights),
        final_sequence_alive=episode.final_alive,
        final_sequence_readiness=episode.final_readiness,
        final_sequence_knowledge=episode.knowledge_transfer,
        final_sequence_score=episode.maturation_score,
    )
    return row, trace_out, sequences, labels, weights, collection


def collect_sequence_labels(
    cfg: Config,
) -> Tuple[List[List[List[float]]], List[List[int]], List[List[float]], List[SequenceCollectionRow]]:
    sequences: Dict[str, List[List[float]]] = {}
    labels: Dict[str, List[int]] = {}
    weights: Dict[str, List[float]] = {}
    rows: List[SequenceCollectionRow] = []
    remaining = cfg.max_sequence_examples
    for seed in cfg.sequence_seeds:
        _, _, seq_map, label_map, weight_map, row = run_sequence_episode(
            seed,
            cfg,
            controller="sequence_optimizer_train",
            collect_labels=True,
            max_examples=max(0, remaining),
        )
        rows.append(row)
        remaining -= row.sampled_examples
        for key, value in seq_map.items():
            sequences[key] = value
            labels[key] = label_map[key]
            weights[key] = weight_map[key]
        if remaining <= 0:
            break
    keys = sorted(sequences)
    return [sequences[key] for key in keys], [labels[key] for key in keys], [weights[key] for key in keys], rows


def ablations_from_summary(summary: Sequence[learned.SummaryRow], controller: str) -> List[learned.AblationRow]:
    by_key = {(row.controller, row.ablation): row for row in summary}
    base_row = by_key[(controller, "none")]
    rows: List[learned.AblationRow] = []
    for ablation in ABLATIONS:
        row = by_key[(controller, ablation)]
        rows.append(
            learned.AblationRow(
                controller=controller,
                ablation=ablation,
                mean_score=row.mean_maturation_score,
                score_loss=base_row.mean_maturation_score - row.mean_maturation_score,
                mean_readiness_score=row.mean_readiness_score,
                readiness_loss=base_row.mean_readiness_score - row.mean_readiness_score,
                mean_development_score=row.mean_development_score,
                development_loss=base_row.mean_development_score - row.mean_development_score,
                mean_knowledge_score=row.mean_knowledge_score,
                knowledge_loss=base_row.mean_knowledge_score - row.mean_knowledge_score,
                mean_resilience_score=row.mean_resilience_score,
                resilience_loss=base_row.mean_resilience_score - row.mean_resilience_score,
                pest_pressure_delta=row.mean_final_pest_pressure - base_row.mean_final_pest_pressure,
                structural_strain_delta=row.mean_final_structural_strain - base_row.mean_final_structural_strain,
            )
        )
    return rows


def verdict_from_summary(summary: Sequence[learned.SummaryRow], ablations: Sequence[learned.AblationRow]) -> VerdictRow:
    by_key = {(row.controller, row.ablation): row for row in summary}
    optimizer = by_key[("sequence_optimizer", "none")]
    sequence_gru = by_key[("sequence_gru", "none")]
    recovery_row = by_key[("recovery_gru", "none")]
    behavior = by_key[("behavior_gru", "none")]
    designed = by_key[("designed", "none")]
    reactive = by_key[("reactive", "none")]
    losses = {row.ablation: row.score_loss for row in ablations}
    bridge = (
        optimizer.shock_gate_pass_rate == 1.0
        and optimizer.post_gate_shock_rate == 1.0
        and optimizer.mean_alive_at_12h >= 12.0
        and optimizer.mean_final_alive >= 14.0
        and optimizer.mean_maturation_score - recovery_row.mean_maturation_score >= 0.10
        and optimizer.mean_final_readiness >= 0.55
        and optimizer.mean_knowledge_transfer >= 0.35
    )
    distillation = (
        sequence_gru.mean_maturation_score - recovery_row.mean_maturation_score >= 0.04
        and sequence_gru.mean_final_alive >= 14.0
        and sequence_gru.mean_knowledge_transfer - recovery_row.mean_knowledge_transfer >= 0.05
        and sequence_gru.mean_final_readiness - recovery_row.mean_final_readiness >= 0.03
    )
    ablation_specific = (
        losses["body"] >= 0.010
        and losses["infrastructure"] >= 0.010
        and losses["tools"] >= 0.010
        and losses["social_culture"] >= 0.010
        and losses["environment"] >= 0.010
        and losses["readiness"] >= 0.010
    )
    return VerdictRow(
        sequence_optimizer_score=optimizer.mean_maturation_score,
        sequence_gru_score=sequence_gru.mean_maturation_score,
        recovery_score=recovery_row.mean_maturation_score,
        behavior_score=behavior.mean_maturation_score,
        designed_score=designed.mean_maturation_score,
        reactive_score=reactive.mean_maturation_score,
        sequence_optimizer_gain_over_recovery=optimizer.mean_maturation_score - recovery_row.mean_maturation_score,
        sequence_gru_gain_over_recovery=sequence_gru.mean_maturation_score - recovery_row.mean_maturation_score,
        sequence_optimizer_gap_to_designed=designed.mean_maturation_score - optimizer.mean_maturation_score,
        sequence_gru_gap_to_optimizer=optimizer.mean_maturation_score - sequence_gru.mean_maturation_score,
        sequence_optimizer_final_alive=optimizer.mean_final_alive,
        sequence_gru_final_alive=sequence_gru.mean_final_alive,
        sequence_optimizer_final_readiness=optimizer.mean_final_readiness,
        sequence_gru_final_readiness=sequence_gru.mean_final_readiness,
        sequence_optimizer_knowledge_transfer=optimizer.mean_knowledge_transfer,
        sequence_gru_knowledge_transfer=sequence_gru.mean_knowledge_transfer,
        body_ablation_loss=losses["body"],
        infrastructure_ablation_loss=losses["infrastructure"],
        tools_ablation_loss=losses["tools"],
        social_culture_ablation_loss=losses["social_culture"],
        environment_ablation_loss=losses["environment"],
        readiness_ablation_loss=losses["readiness"],
        previous_action_ablation_loss=losses["previous_action"],
        supports_sequence_consequence_bridge=bridge,
        supports_planner_free_distillation=distillation,
        supports_ablation_specificity=ablation_specific,
        verdict="pass" if bridge and distillation and ablation_specific else "partial_or_failed",
    )


def evaluate_models(
    cfg: Config,
    device: torch.device,
    frame_model: learned.ControllerNet,
    behavior_model: learned.ControllerNet,
    recovery_model: learned.ControllerNet,
    sequence_model: learned.ControllerNet,
) -> Tuple[List[learned.EvalRow], List[learned.SummaryRow], List[learned.AblationRow], VerdictRow, env.Trace, List[PlanEvalRow]]:
    lcfg = learned_config(cfg)
    eval_rows: List[learned.EvalRow] = []
    plan_rows: List[PlanEvalRow] = []
    trace = env.Trace(seed=cfg.trace_seed, condition="sequence_optimizer")
    controllers = (
        ("designed", None, "none"),
        ("reactive", None, "none"),
        ("frame_mlp", frame_model, "none"),
        ("behavior_gru", behavior_model, "none"),
        ("recovery_gru", recovery_model, "none"),
        ("sequence_gru", sequence_model, "none"),
    )
    for seed in cfg.eval_seeds:
        for controller, model, ablation in controllers:
            row, _ = learned.run_controller_episode(seed, lcfg, controller, model, device, ablation=ablation)
            eval_rows.append(row)
        sequence_row, maybe_trace, _, _, _, collection = run_sequence_episode(
            seed,
            cfg,
            controller="sequence_optimizer",
            trace=(seed == cfg.trace_seed),
        )
        eval_rows.append(sequence_row)
        plan_rows.append(
            PlanEvalRow(
                seed=seed,
                controller="sequence_optimizer",
                condition="none",
                selected_plans=collection.selected_plans,
                final_alive=collection.final_sequence_alive,
                final_readiness=collection.final_sequence_readiness,
                knowledge_transfer=collection.final_sequence_knowledge,
                final_structural_strain=sequence_row.final_structural_strain,
                final_pest_pressure=sequence_row.final_pest_pressure,
                maturation_score=collection.final_sequence_score,
            )
        )
        if maybe_trace.frames:
            trace = maybe_trace
        for ablation in ABLATIONS:
            row, _ = learned.run_controller_episode(seed, lcfg, "sequence_gru", sequence_model, device, ablation=ablation)
            eval_rows.append(row)
    summary = learned.summarize(eval_rows)
    ablations = ablations_from_summary(summary, "sequence_gru")
    verdict = verdict_from_summary(summary, ablations)
    return eval_rows, summary, ablations, verdict, trace, plan_rows


def write_artifacts(
    cfg: Config,
    training: Sequence[recovery.TrainingRow],
    recovery_collection: Sequence[recovery.CollectionRow],
    sequence_collection: Sequence[SequenceCollectionRow],
    plan_eval: Sequence[PlanEvalRow],
    eval_rows: Sequence[learned.EvalRow],
    summary: Sequence[learned.SummaryRow],
    ablations: Sequence[learned.AblationRow],
    verdict: VerdictRow,
    trace: env.Trace,
) -> Dict[str, object]:
    payload = {
        "config": asdict(cfg),
        "plans": {key: list(value) for key, value in PLAN_LIBRARY.items()},
        "feature_names": learned.FEATURE_NAMES,
        "feature_groups": {key: list(value) for key, value in learned.FEATURE_GROUPS.items()},
        "actions": list(learned.ACTIONS),
        "training": [asdict(row) for row in training],
        "recovery_collection": [asdict(row) for row in recovery_collection],
        "sequence_collection": [asdict(row) for row in sequence_collection],
        "plan_eval": [asdict(row) for row in plan_eval],
        "eval": [asdict(row) for row in eval_rows],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": asdict(trace),
        "notes": {
            "claim": "bounded sequence-consequence planning bridge plus planner-free GRU distillation attempt",
            "not_claimed": "deep reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
        },
    }
    learned.rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_training.csv", training)
    learned.rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_recovery_collection.csv", recovery_collection)
    learned.rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_sequence_collection.csv", sequence_collection)
    learned.rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_plan_eval.csv", plan_eval)
    learned.rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", eval_rows)
    learned.rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_summary.csv", summary)
    learned.rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_ablations.csv", ablations)
    learned.rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    learned.write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", payload)
    learned.write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", asdict(trace))
    learned.write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_READINESS_SEQUENCE_CONSEQUENCE_RESULTS", payload)
    learned.write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_READINESS_SEQUENCE_CONSEQUENCE_TRACE", asdict(trace))
    return payload


def run_benchmark(cfg: Config) -> Dict[str, object]:
    device = learned.resolve_device(cfg.device)
    (
        frame_model,
        behavior_model,
        recovery_model,
        training_rows,
        recovery_rows,
        aggregate_sequences,
        aggregate_labels,
        aggregate_weights,
    ) = train_recovery_stack(cfg, device)
    sequence_sequences, sequence_labels, sequence_weights, sequence_rows = collect_sequence_labels(cfg)
    aggregate_sequences = aggregate_sequences + sequence_sequences
    aggregate_labels = aggregate_labels + sequence_labels
    aggregate_weights = aggregate_weights + sequence_weights
    x, y, mask, weights = recovery.build_weighted_tensors(aggregate_sequences, aggregate_labels, aggregate_weights, device)
    sequence_model, row = recovery.train_weighted_model(
        "gru",
        x,
        y,
        mask,
        weights,
        recovery_config(cfg),
        device,
        "sequence_distillation",
        "teacher_recovery_plus_student_sequence_consequence_labels",
        cfg.sequence_epochs,
        cfg.sequence_learning_rate,
        313,
        sum(len(labels) for labels in sequence_labels),
    )
    training_rows.append(row)
    eval_rows, summary, ablations, verdict, trace, plan_rows = evaluate_models(
        cfg, device, frame_model, behavior_model, recovery_model, sequence_model
    )
    return write_artifacts(cfg, training_rows, recovery_rows, sequence_rows, plan_rows, eval_rows, summary, ablations, verdict, trace)


def parse_args() -> Config:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--behavior-train-seeds", default="20261211,20261212,20261213,20261214,20261215,20261216")
    parser.add_argument("--recovery-seeds", default="20261231,20261232,20261233")
    parser.add_argument("--sequence-seeds", default="20261301,20261302,20261303")
    parser.add_argument("--eval-seeds", default="20261321,20261322,20261323,20261324,20261325")
    parser.add_argument("--hours", type=float, default=72.0)
    parser.add_argument("--step-hours", type=float, default=0.10)
    parser.add_argument("--population", type=int, default=14)
    parser.add_argument("--epochs", type=int, default=52)
    parser.add_argument("--recovery-epochs", type=int, default=42)
    parser.add_argument("--sequence-epochs", type=int, default=38)
    parser.add_argument("--hidden-size", type=int, default=72)
    parser.add_argument("--learning-rate", type=float, default=0.0035)
    parser.add_argument("--recovery-learning-rate", type=float, default=0.0022)
    parser.add_argument("--sequence-learning-rate", type=float, default=0.0020)
    parser.add_argument("--plan-horizon-hours", type=float, default=2.4)
    parser.add_argument("--plan-commit-hours", type=float, default=0.8)
    parser.add_argument("--sample-interval-hours", type=float, default=1.2)
    parser.add_argument("--max-sequence-examples", type=int, default=900)
    parser.add_argument("--device", default="cpu")
    parser.add_argument("--trace-seed", type=int, default=20261321)
    args = parser.parse_args()
    return Config(
        behavior_train_seeds=parse_seed_list(args.behavior_train_seeds),
        recovery_seeds=parse_seed_list(args.recovery_seeds),
        sequence_seeds=parse_seed_list(args.sequence_seeds),
        eval_seeds=parse_seed_list(args.eval_seeds),
        hours=args.hours,
        step_hours=args.step_hours,
        population=args.population,
        epochs=args.epochs,
        recovery_epochs=args.recovery_epochs,
        sequence_epochs=args.sequence_epochs,
        hidden_size=args.hidden_size,
        learning_rate=args.learning_rate,
        recovery_learning_rate=args.recovery_learning_rate,
        sequence_learning_rate=args.sequence_learning_rate,
        plan_horizon_hours=args.plan_horizon_hours,
        plan_commit_hours=args.plan_commit_hours,
        sample_interval_hours=args.sample_interval_hours,
        max_sequence_examples=args.max_sequence_examples,
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(
        json.dumps(
            {
                "verdict": payload["verdict"],
                "training": payload["training"],
                "sequence_collection": payload["sequence_collection"],
                "plan_eval": payload["plan_eval"],
                "summary": payload["summary"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
