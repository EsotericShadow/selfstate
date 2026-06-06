#!/usr/bin/env python3
"""Social/culture hidden-regime controller for SSRM-3D.

Report 97 produced the strongest learned hidden-regime result so far, but its
social/culture ablation did not matter. This experiment attacks that weakness
directly: every held-out world has a hidden social/culture regime after the 12h
development gate, and the correct recovery pattern depends on trust, conflict,
symbol convergence, reputation accuracy, teaching, culture memory, and
knowledge transfer.

The controller still receives no hidden regime label. It receives embodied
state, world state, social/culture state, noisy symptom streams, memory, time,
and previous action. Training remains imitation from a designed teacher plus
closed-loop return selection over an option-bias value; this is not full deep
reinforcement learning.
"""

from __future__ import annotations

import argparse
import json
import random
import statistics
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import importlib.util
import torch


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
REPORT96_PATH = ROOT / "experiments" / "ssrm_3d_option_gated_hidden_regime_controller.py"


def load_report96_module():
    spec = importlib.util.spec_from_file_location("ssrm_option_gated_social", REPORT96_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {REPORT96_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


p96 = load_report96_module()
p95 = p96.p95
h = p95.h

ACTIONS = p95.ACTIONS
ACTION_TO_INDEX = p95.ACTION_TO_INDEX
INDEX_TO_ACTION = p95.INDEX_TO_ACTION
CHECKPOINTS = p95.CHECKPOINTS

SOCIAL_VARIANTS = (
    "trust_fracture",
    "symbol_drift",
    "coalition_split",
    "teacher_loss",
    "rumor_cascade",
)
VARIANT_TARGETS = {
    "trust_fracture": {"mediate"},
    "symbol_drift": {"teach"},
    "coalition_split": {"mediate"},
    "teacher_loss": {"teach"},
    "rumor_cascade": {"inspect", "mediate"},
}
FEATURE_GROUPS: Dict[str, Tuple[int, ...]] = {
    **p96.FEATURE_GROUPS,
    "social_culture": tuple(sorted(set(p95.FEATURE_GROUPS["social_culture"] + (41, 42)))),
}


@dataclass(frozen=True)
class Config:
    train_seeds: Sequence[int]
    tune_seeds: Sequence[int]
    eval_seeds: Sequence[int]
    bias_candidates: Sequence[float]
    hours: float = 16.0
    step_hours: float = 0.08
    population: int = 10
    epochs: int = 100
    hidden_size: int = 56
    learning_rate: float = 0.004
    option_loss_weight: float = 0.62
    device: str = "auto"
    trace_seed: int = 20260833


@dataclass(frozen=True)
class BiasSelectionRow:
    option_bias: float
    mean_score: float
    mean_social_response_score: float
    mean_variant_targeted_rate: float
    selection_objective: float
    selected: bool


@dataclass(frozen=True)
class EvalRow:
    seed: int
    social_variant: str
    architecture: str
    condition: str
    final_alive: int
    total_agents: int
    alive_at_12h: int
    no_major_regime_before_12h: bool
    hidden_regime_after_12h: bool
    final_food: float
    final_water: float
    final_trust: float
    final_conflict: float
    final_social_inequality: float
    final_reputation_accuracy: float
    final_symbol_convergence: float
    teaching_delta: float
    knowledge_transfer: float
    culture_memory: float
    architecture_delta: float
    tool_design_delta: float
    social_inference_score: float
    social_response_score: float
    variant_targeted_rate: float
    survival_score: float
    development_score: float
    culture_score: float
    long_horizon_score: float


@dataclass(frozen=True)
class SummaryRow:
    architecture: str
    condition: str
    mean_long_horizon_score: float
    mean_survival_score: float
    mean_development_score: float
    mean_culture_score: float
    mean_social_inference_score: float
    mean_social_response_score: float
    mean_variant_targeted_rate: float
    mean_final_alive: float
    mean_alive_at_12h: float
    mean_trust: float
    mean_conflict: float
    mean_social_inequality: float
    mean_reputation_accuracy: float
    mean_symbol_convergence: float
    mean_knowledge_transfer: float
    no_major_regime_before_12h_rate: float
    hidden_regime_after_12h_rate: float


@dataclass(frozen=True)
class VariantSummaryRow:
    social_variant: str
    architecture: str
    condition: str
    mean_long_horizon_score: float
    mean_social_response_score: float
    mean_variant_targeted_rate: float
    mean_trust: float
    mean_symbol_convergence: float


@dataclass(frozen=True)
class AblationRow:
    architecture: str
    ablation: str
    mean_score: float
    score_loss: float
    mean_social_response_score: float
    social_response_loss: float
    mean_variant_targeted_rate: float
    variant_targeted_loss: float
    mean_culture_score: float
    culture_loss: float


@dataclass(frozen=True)
class VerdictRow:
    selected_option_bias: float
    return_selected_score: float
    fixed_bias_score: float
    option_frame_score: float
    reactive_score: float
    gain_over_fixed_bias: float
    gain_over_frame: float
    gain_over_reactive: float
    social_culture_ablation_loss: float
    social_culture_response_loss: float
    regime_signal_response_loss: float
    memory_ablation_loss: float
    body_ablation_loss: float
    social_response_score: float
    variant_targeted_rate: float
    shock_gate_pass_rate: float
    hidden_regime_rate: float
    supports_social_culture_controller: bool
    supports_social_culture_ablation: bool
    verdict: str


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return h.clamp(value, low, high)


def parse_seed_list(raw: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in raw.split(",") if part.strip())


def parse_float_list(raw: str) -> Tuple[float, ...]:
    return tuple(float(part.strip()) for part in raw.split(",") if part.strip())


def social_variant_for_seed(seed: int) -> str:
    return SOCIAL_VARIANTS[seed % len(SOCIAL_VARIANTS)]


def to_p96_config(cfg: Config, option_bias: float) -> object:
    return p96.Config(
        train_seeds=cfg.train_seeds,
        eval_seeds=cfg.eval_seeds,
        hours=cfg.hours,
        step_hours=cfg.step_hours,
        population=cfg.population,
        epochs=cfg.epochs,
        hidden_size=cfg.hidden_size,
        learning_rate=cfg.learning_rate,
        option_loss_weight=cfg.option_loss_weight,
        option_bias=option_bias,
        device=cfg.device,
        trace_seed=cfg.trace_seed,
    )


def teacher_condition():
    return p95.teacher_condition()


def reactive_condition():
    return p95.reactive_condition()


def make_social_world(seed: int, rng: random.Random):
    world = h.make_world(seed, rng)
    world.regime_name = "trust_fracture"
    world.social_variant = social_variant_for_seed(seed)
    world.first_regime_hour = 12.30 + rng.random() * 0.45
    world.trust = 0.64
    world.conflict = 0.08
    world.social_inequality = 0.12
    world.reputation_accuracy = 0.46
    world.symbol_convergence = 0.30
    world.teaching = 0.12
    world.risk_memory = 0.12
    world.culture_memory = 0.10
    world.knowledge_transfer = 0.0
    world.variant_post_action_count = 0
    world.variant_targeted_action_count = 0
    return world


def apply_social_hidden_regime(world, condition, dt: float) -> None:
    if not h.regime_active(world):
        return
    variant = world.social_variant
    world.regime_anomalies["social"] = clamp(world.regime_anomalies["social"] + 0.145 * dt)
    world.hidden_pressure = clamp(world.hidden_pressure + 0.040 * dt)
    if variant == "trust_fracture":
        world.trust = clamp(world.trust - 0.060 * dt)
        world.conflict = clamp(world.conflict + 0.060 * dt)
        world.social_inequality = clamp(world.social_inequality + 0.036 * dt)
        world.symbol_convergence = clamp(world.symbol_convergence - 0.022 * dt)
    elif variant == "symbol_drift":
        world.symbol_convergence = clamp(world.symbol_convergence - 0.076 * dt)
        world.reputation_accuracy = clamp(world.reputation_accuracy - 0.040 * dt)
        world.culture_memory = clamp(world.culture_memory - 0.030 * dt)
        world.trust = clamp(world.trust - 0.026 * dt)
        world.conflict = clamp(world.conflict + 0.032 * dt)
    elif variant == "coalition_split":
        world.social_inequality = clamp(world.social_inequality + 0.072 * dt)
        world.conflict = clamp(world.conflict + 0.052 * dt)
        world.trust = clamp(world.trust - 0.044 * dt)
        world.food = clamp(world.food - 0.014 * dt)
        world.water = clamp(world.water - 0.012 * dt)
    elif variant == "teacher_loss":
        world.teaching = clamp(world.teaching - 0.060 * dt)
        world.culture_memory = clamp(world.culture_memory - 0.050 * dt)
        world.knowledge_transfer = clamp(world.knowledge_transfer - 0.044 * dt)
        world.reputation_accuracy = clamp(world.reputation_accuracy - 0.018 * dt)
        world.tool_design = clamp(world.tool_design - 0.010 * dt)
        world.architecture = clamp(world.architecture - 0.008 * dt)
    elif variant == "rumor_cascade":
        world.reputation_accuracy = clamp(world.reputation_accuracy - 0.070 * dt)
        world.conflict = clamp(world.conflict + 0.060 * dt)
        world.trust = clamp(world.trust - 0.050 * dt)
        world.symbol_convergence = clamp(world.symbol_convergence - 0.030 * dt)
        world.social_inequality = clamp(world.social_inequality + 0.024 * dt)
    if not condition.reputation_influence:
        world.trust = clamp(world.trust - 0.020 * dt)
        world.conflict = clamp(world.conflict + 0.022 * dt)
    if not condition.teaching:
        world.symbol_convergence = clamp(world.symbol_convergence - 0.018 * dt)
        world.knowledge_transfer = clamp(world.knowledge_transfer - 0.018 * dt)
    social_failure = max(0.0, world.conflict - 0.34) + max(0.0, 0.50 - world.trust) + world.social_inequality * 0.18
    world.food = clamp(world.food - social_failure * 0.010 * dt)
    world.water = clamp(world.water - social_failure * 0.009 * dt)
    world.route_hazard = clamp(world.route_hazard + social_failure * 0.012 * dt)


def urgent_survival_action(agent, world) -> str | None:
    urgent = max(
        agent.hunger,
        agent.thirst,
        max(0.0, 0.42 - world.food) * 1.35,
        max(0.0, 0.42 - world.water) * 1.45,
        max(0.0, 0.40 - agent.health) * 1.20,
        max(0.0, 0.25 - agent.energy) * 1.20,
    )
    if urgent <= 0.74:
        return None
    if agent.energy < 0.22 or agent.health < 0.42:
        return "rest"
    return "harvest_water" if world.water < world.food or agent.thirst > agent.hunger else "harvest_food"


def choose_social_teacher_action(agent, world, condition, rng: random.Random) -> str:
    if condition.name == "reactive_survival_only":
        if agent.energy < 0.26 or agent.health < 0.46:
            return "rest"
        return "harvest_water" if world.water < world.food or agent.thirst > agent.hunger else "harvest_food"
    urgent = urgent_survival_action(agent, world)
    if urgent:
        return urgent
    if h.regime_active(world):
        variant = world.social_variant
        if variant == "trust_fracture":
            return "mediate"
        if variant == "symbol_drift":
            return "teach"
        if variant == "coalition_split":
            return "mediate"
        if variant == "teacher_loss":
            return "teach"
        if variant == "rumor_cascade":
            if world.risk_memory < 0.48:
                return "inspect"
            return "mediate"
    if world.teaching < 0.50 or world.culture_memory < 0.36 or rng.random() < 0.30:
        return "teach"
    if world.shelter < 0.58 or world.architecture < 0.52 or world.waterworks < 0.42:
        return "construct"
    if world.tool_quality < 0.46 or world.tool_design < 0.42:
        return "redesign_tools"
    if world.symbol_convergence < 0.42 or world.reputation_accuracy < 0.48:
        return "teach"
    if world.conflict > 0.24 or world.trust < 0.56:
        return "mediate"
    if world.food < 0.58 or world.water < 0.58:
        return "harvest_water" if world.water < world.food else "harvest_food"
    if agent.energy < 0.38 or agent.stress > 0.60:
        return "rest"
    return rng.choice(("inspect", "construct", "teach", "mediate", "redesign_tools", "rest"))


def record_variant_action(world, action: str) -> None:
    if not h.regime_active(world):
        return
    world.variant_post_action_count += 1
    if action in VARIANT_TARGETS[world.social_variant]:
        world.variant_targeted_action_count += 1


def social_inference_score(world) -> float:
    target = world.beliefs["social"]
    distractors = [value for key, value in world.beliefs.items() if key != "social"]
    margin = target - mean(distractors)
    return clamp(target * 0.72 + max(0.0, margin) * 0.58)


def social_response_score(world, agents: Sequence[object]) -> float:
    if world.social_variant == "trust_fracture":
        return clamp(
            world.trust * 0.28
            + (1.0 - world.conflict) * 0.26
            + world.reputation_accuracy * 0.20
            + world.symbol_convergence * 0.14
            + (1.0 - world.social_inequality) * 0.12
        )
    if world.social_variant == "symbol_drift":
        return clamp(
            world.symbol_convergence * 0.34
            + world.teaching * 0.22
            + world.culture_memory * 0.18
            + world.knowledge_transfer * 0.16
            + world.reputation_accuracy * 0.10
        )
    if world.social_variant == "coalition_split":
        return clamp(
            (1.0 - world.social_inequality) * 0.26
            + world.trust * 0.24
            + (1.0 - world.conflict) * 0.22
            + world.food * 0.14
            + world.water * 0.14
        )
    if world.social_variant == "teacher_loss":
        return clamp(
            world.teaching * 0.30
            + world.knowledge_transfer * 0.28
            + world.culture_memory * 0.20
            + mean(agent.wisdom for agent in h.living(agents)) * 0.12
            + world.symbol_convergence * 0.10
        )
    return clamp(
        world.reputation_accuracy * 0.32
        + (1.0 - world.conflict) * 0.24
        + world.trust * 0.20
        + world.risk_memory * 0.14
        + world.symbol_convergence * 0.10
    )


def culture_score(world) -> float:
    return clamp(
        world.knowledge_transfer * 0.36
        + world.teaching * 0.24
        + world.culture_memory * 0.18
        + world.symbol_convergence * 0.14
        + world.reputation_accuracy * 0.08
    )


def development_score(world, baseline: Dict[str, float]) -> float:
    return clamp(
        max(0.0, world.architecture - baseline["architecture"]) * 0.34
        + max(0.0, world.tool_design - baseline["tool_design"]) * 0.26
        + max(0.0, world.sanitation - baseline["sanitation"]) * 0.18
        + max(0.0, world.path_network - 0.14) * 0.12
        + max(0.0, world.food_storage - 0.18) * 0.10
    )


def score_episode(seed: int, architecture: str, condition: str, world, agents, baseline: Dict[str, float], alive_at_12h: int | None, no_major_before_12: bool) -> EvalRow:
    final_alive = len(h.living(agents))
    total_agents = len(agents)
    survival = final_alive / max(1, total_agents)
    development = development_score(world, baseline)
    culture = culture_score(world)
    response = social_response_score(world, agents)
    inference = social_inference_score(world)
    targeted = world.variant_targeted_action_count / max(1, world.variant_post_action_count)
    score = clamp(
        survival * 0.18
        + development * 0.14
        + culture * 0.20
        + response * 0.28
        + inference * 0.10
        + targeted * 0.10
    )
    return EvalRow(
        seed=seed,
        social_variant=world.social_variant,
        architecture=architecture,
        condition=condition,
        final_alive=final_alive,
        total_agents=total_agents,
        alive_at_12h=alive_at_12h if alive_at_12h is not None else final_alive,
        no_major_regime_before_12h=no_major_before_12,
        hidden_regime_after_12h=world.first_regime_hour >= 12.0 and h.regime_active(world),
        final_food=world.food,
        final_water=world.water,
        final_trust=world.trust,
        final_conflict=world.conflict,
        final_social_inequality=world.social_inequality,
        final_reputation_accuracy=world.reputation_accuracy,
        final_symbol_convergence=world.symbol_convergence,
        teaching_delta=world.teaching - baseline["teaching"],
        knowledge_transfer=world.knowledge_transfer,
        culture_memory=world.culture_memory,
        architecture_delta=world.architecture - baseline["architecture"],
        tool_design_delta=world.tool_design - baseline["tool_design"],
        social_inference_score=inference,
        social_response_score=response,
        variant_targeted_rate=targeted,
        survival_score=survival,
        development_score=development,
        culture_score=culture,
        long_horizon_score=score,
    )


def trace_snapshot(world, agents, label: str, last_option: str, last_action: str) -> Dict[str, object]:
    alive = h.living(agents)
    return {
        "label": label,
        "hours": world.time,
        "social_variant": world.social_variant,
        "regime_active": h.regime_active(world),
        "alive": len(alive),
        "total_agents": len(agents),
        "last_option": last_option,
        "last_action": last_action,
        "food": world.food,
        "water": world.water,
        "trust": world.trust,
        "conflict": world.conflict,
        "social_inequality": world.social_inequality,
        "reputation_accuracy": world.reputation_accuracy,
        "symbol_convergence": world.symbol_convergence,
        "teaching": world.teaching,
        "culture_memory": world.culture_memory,
        "knowledge_transfer": world.knowledge_transfer,
        "social_inference_score": social_inference_score(world),
        "social_response_score": social_response_score(world, agents),
        "variant_targeted_rate": world.variant_targeted_action_count / max(1, world.variant_post_action_count),
        "dominant_belief": h.dominant_belief(world),
        "beliefs": dict(world.beliefs),
        "mean_wisdom": mean(agent.wisdom for agent in alive),
        "mean_influence": mean(agent.influence for agent in alive),
    }


def apply_feature_ablation(features: List[float], ablation: str) -> List[float]:
    if ablation == "none":
        return features
    out = list(features)
    group = FEATURE_GROUPS.get(ablation)
    if group is None:
        raise ValueError(f"unknown ablation {ablation!r}")
    for index in group:
        out[index] = 0.0
    return out


def choose_model_action(model, device, feature_mean, feature_std, agent, world, signals, previous_action: int, state, cfg: Config, option_bias: float, ablation: str):
    raw = apply_feature_ablation(p95.observation(agent, world, signals, previous_action), ablation)
    x = torch.tensor(raw, dtype=torch.float32).unsqueeze(0)
    x = (x - feature_mean) / feature_std
    x = x.to(device)
    with torch.no_grad():
        action_logits, option_logits, next_state = model.step(x, state)
    scores = action_logits + p96.option_action_bias(option_logits, to_p96_config(cfg, option_bias))
    action_index = int(scores.argmax(dim=-1).item())
    option_index = int(option_logits.argmax(dim=-1).item())
    return INDEX_TO_ACTION[action_index], action_index, p96.OPTION_NAMES[option_index], next_state


def run_world_loop(seed: int, cfg: Config, actor, condition, architecture: str, label: str, *, trace: bool = False) -> Tuple[EvalRow, List[Dict[str, object]]]:
    rng = random.Random(seed * 257 + 41)
    agents = h.make_agents(rng, cfg.population)
    world = make_social_world(seed, rng)
    h.current_agents = agents
    baseline = {
        "architecture": world.architecture,
        "tool_design": world.tool_design,
        "teaching": world.teaching,
        "sanitation": world.sanitation,
    }
    previous_actions = [ACTION_TO_INDEX["rest"] for _ in range(max(32, cfg.population + 8))]
    states: Dict[int, torch.Tensor | None] = {index: None for index in range(len(agents))}
    checkpoints = list(CHECKPOINTS)
    snapshots: List[Dict[str, object]] = []
    alive_at_12h: int | None = None
    no_major_before_12 = True
    last_option = "survival"
    last_action = "rest"

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        world.time += dt
        h.apply_baseline_environment(world, agents, condition, dt, rng)
        apply_social_hidden_regime(world, condition, dt)
        signals = h.symptom_channels(world, condition, rng)
        h.update_beliefs(world, condition, signals, dt)
        pressure = h.pressure_score(world, agents)
        world.pressure_integral = clamp(world.pressure_integral + pressure * dt / max(cfg.hours, 1.0))
        h.update_agent_influence(agents, condition.reputation_influence)
        for index, agent in enumerate(list(agents)):
            if index >= len(previous_actions):
                previous_actions.append(ACTION_TO_INDEX["rest"])
                states[index] = None
            if not agent.alive or agent.child:
                continue
            action, action_index, option_name, next_state = actor(agent, world, signals, previous_actions[index], states.get(index), rng)
            last_action = action
            last_option = option_name
            states[index] = next_state
            record_variant_action(world, action)
            h.apply_action(agent, world, condition, action, dt, rng)
            previous_actions[index] = action_index
        p95.apply_body_dynamics(world, agents, dt)
        before_count = len(agents)
        h.maybe_reproduce(world, agents, condition, rng, dt)
        if len(agents) > before_count:
            for index in range(before_count, len(agents)):
                previous_actions.append(ACTION_TO_INDEX["rest"])
                states[index] = None
        if world.time < 12.0 and h.regime_active(world):
            no_major_before_12 = False
        if alive_at_12h is None and world.time >= 12.0:
            alive_at_12h = len(h.living(agents))
        while checkpoints and world.time >= checkpoints[0] - 1e-9:
            if trace:
                snapshots.append(trace_snapshot(world, agents, f"{checkpoints[0]:.1f}h", last_option, last_action))
            checkpoints.pop(0)
    row = score_episode(seed, architecture, label, world, agents, baseline, alive_at_12h, no_major_before_12)
    return row, snapshots


def generate_teacher_sequences(cfg: Config) -> Tuple[torch.Tensor, torch.Tensor]:
    xs: List[List[List[float]]] = []
    ys: List[List[int]] = []
    for seed in cfg.train_seeds:
        seed_xs: List[List[List[float]]] = [[] for _ in range(cfg.population)]
        seed_ys: List[List[int]] = [[] for _ in range(cfg.population)]
        rng = random.Random(seed * 257 + 41)
        agents = h.make_agents(rng, cfg.population)
        world = make_social_world(seed, rng)
        h.current_agents = agents
        previous_actions = [ACTION_TO_INDEX["rest"] for _ in range(cfg.population)]
        while world.time < cfg.hours - 1e-9:
            dt = min(cfg.step_hours, cfg.hours - world.time)
            world.time += dt
            h.apply_baseline_environment(world, agents, teacher_condition(), dt, rng)
            apply_social_hidden_regime(world, teacher_condition(), dt)
            signals = h.symptom_channels(world, teacher_condition(), rng)
            h.update_beliefs(world, teacher_condition(), signals, dt)
            pressure = h.pressure_score(world, agents)
            world.pressure_integral = clamp(world.pressure_integral + pressure * dt / max(cfg.hours, 1.0))
            h.update_agent_influence(agents, teacher_condition().reputation_influence)
            for index, agent in enumerate(agents[: cfg.population]):
                if not agent.alive or agent.child:
                    seed_xs[index].append(p95.observation(agent, world, signals, previous_actions[index]))
                    seed_ys[index].append(ACTION_TO_INDEX["rest"])
                    continue
                action = choose_social_teacher_action(agent, world, teacher_condition(), rng)
                action_index = ACTION_TO_INDEX[action]
                seed_xs[index].append(p95.observation(agent, world, signals, previous_actions[index]))
                seed_ys[index].append(action_index)
                record_variant_action(world, action)
                h.apply_action(agent, world, teacher_condition(), action, dt, rng)
                previous_actions[index] = action_index
            p95.apply_body_dynamics(world, agents, dt)
            h.maybe_reproduce(world, agents, teacher_condition(), rng, dt)
        xs.extend(seed_xs)
        ys.extend(seed_ys)
    return torch.tensor(xs, dtype=torch.float32), torch.tensor(ys, dtype=torch.long)


def train_models(cfg: Config):
    device = p96.resolve_device(cfg.device)
    train_x_raw, train_y = generate_teacher_sequences(cfg)
    option_y, sample_weights = p96.derive_option_targets(train_x_raw, train_y)
    sample_weights = boost_social_sample_weights(train_x_raw, train_y, sample_weights)
    train_x, feature_mean, feature_std = p96.standardize(train_x_raw)
    models = {}
    training_rows = []
    for architecture in ("option_frame", "option_gru"):
        model, row = p96.train_option_controller(
            architecture,
            train_x,
            train_y,
            option_y,
            sample_weights,
            to_p96_config(cfg, option_bias=1.0),
            device,
        )
        models[architecture] = model
        training_rows.append(row)
    return device, feature_mean, feature_std, models, training_rows


def boost_social_sample_weights(train_x_raw: torch.Tensor, train_y: torch.Tensor, weights: torch.Tensor) -> torch.Tensor:
    boosted = weights.clone()
    for seq in range(train_y.shape[0]):
        for step in range(train_y.shape[1]):
            features = train_x_raw[seq, step]
            social_signal = float(features[40].item())
            if social_signal < 0.18:
                continue
            action = INDEX_TO_ACTION[int(train_y[seq, step].item())]
            multiplier = 1.0 + social_signal * 4.5
            if action == "mediate":
                multiplier *= 2.4
            elif action == "teach":
                multiplier *= 2.0
            elif action == "inspect":
                multiplier *= 1.6
            boosted[seq, step] *= multiplier
    return boosted


def run_model_episode(seed: int, architecture: str, model, device, feature_mean, feature_std, cfg: Config, option_bias: float, *, ablation: str = "none", trace: bool = False) -> Tuple[EvalRow, List[Dict[str, object]]]:
    def actor(agent, world, signals, previous_action, state, rng):
        return choose_model_action(model, device, feature_mean, feature_std, agent, world, signals, previous_action, state, cfg, option_bias, ablation)

    return run_world_loop(seed, cfg, actor, teacher_condition(), architecture, ablation, trace=trace)


def run_reactive_episode(seed: int, cfg: Config) -> EvalRow:
    def actor(agent, world, signals, previous_action, state, rng):
        action = choose_social_teacher_action(agent, world, reactive_condition(), rng)
        return action, ACTION_TO_INDEX[action], "reactive", None

    row, _ = run_world_loop(seed, cfg, actor, reactive_condition(), "scripted", "reactive_survival_only", trace=False)
    return row


def selection_objective(rows: Sequence[EvalRow]) -> Tuple[float, float, float, float]:
    score = mean(row.long_horizon_score for row in rows)
    response = mean(row.social_response_score for row in rows)
    targeted = mean(row.variant_targeted_rate for row in rows)
    objective = score + response * 0.16 + targeted * 0.10
    return score, response, targeted, objective


def select_option_bias(cfg: Config, model, device, feature_mean, feature_std) -> Tuple[float, List[BiasSelectionRow]]:
    best_bias = cfg.bias_candidates[0]
    best_objective = -1.0
    rows: List[BiasSelectionRow] = []
    for option_bias in cfg.bias_candidates:
        eval_rows = [
            run_model_episode(seed, "return_selected_social_gru", model, device, feature_mean, feature_std, cfg, option_bias)[0]
            for seed in cfg.tune_seeds
        ]
        score, response, targeted, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_bias = option_bias
            best_objective = objective
        rows.append(BiasSelectionRow(option_bias, score, response, targeted, objective, False))
    return best_bias, [
        BiasSelectionRow(row.option_bias, row.mean_score, row.mean_social_response_score, row.mean_variant_targeted_rate, row.selection_objective, row.option_bias == best_bias)
        for row in rows
    ]


def summarize(rows: Sequence[EvalRow]) -> List[SummaryRow]:
    buckets: Dict[Tuple[str, str], List[EvalRow]] = {}
    for row in rows:
        buckets.setdefault((row.architecture, row.condition), []).append(row)
    out: List[SummaryRow] = []
    for (architecture, condition), items in sorted(buckets.items()):
        out.append(
            SummaryRow(
                architecture=architecture,
                condition=condition,
                mean_long_horizon_score=mean(row.long_horizon_score for row in items),
                mean_survival_score=mean(row.survival_score for row in items),
                mean_development_score=mean(row.development_score for row in items),
                mean_culture_score=mean(row.culture_score for row in items),
                mean_social_inference_score=mean(row.social_inference_score for row in items),
                mean_social_response_score=mean(row.social_response_score for row in items),
                mean_variant_targeted_rate=mean(row.variant_targeted_rate for row in items),
                mean_final_alive=mean(row.final_alive for row in items),
                mean_alive_at_12h=mean(row.alive_at_12h for row in items),
                mean_trust=mean(row.final_trust for row in items),
                mean_conflict=mean(row.final_conflict for row in items),
                mean_social_inequality=mean(row.final_social_inequality for row in items),
                mean_reputation_accuracy=mean(row.final_reputation_accuracy for row in items),
                mean_symbol_convergence=mean(row.final_symbol_convergence for row in items),
                mean_knowledge_transfer=mean(row.knowledge_transfer for row in items),
                no_major_regime_before_12h_rate=mean(1.0 if row.no_major_regime_before_12h else 0.0 for row in items),
                hidden_regime_after_12h_rate=mean(1.0 if row.hidden_regime_after_12h else 0.0 for row in items),
            )
        )
    return out


def summarize_variants(rows: Sequence[EvalRow]) -> List[VariantSummaryRow]:
    buckets: Dict[Tuple[str, str, str], List[EvalRow]] = {}
    for row in rows:
        buckets.setdefault((row.social_variant, row.architecture, row.condition), []).append(row)
    out: List[VariantSummaryRow] = []
    for (variant, architecture, condition), items in sorted(buckets.items()):
        out.append(
            VariantSummaryRow(
                social_variant=variant,
                architecture=architecture,
                condition=condition,
                mean_long_horizon_score=mean(row.long_horizon_score for row in items),
                mean_social_response_score=mean(row.social_response_score for row in items),
                mean_variant_targeted_rate=mean(row.variant_targeted_rate for row in items),
                mean_trust=mean(row.final_trust for row in items),
                mean_symbol_convergence=mean(row.final_symbol_convergence for row in items),
            )
        )
    return out


def row_lookup(summary: Sequence[SummaryRow], architecture: str, condition: str) -> SummaryRow:
    for row in summary:
        if row.architecture == architecture and row.condition == condition:
            return row
    raise KeyError((architecture, condition))


def make_ablations(summary: Sequence[SummaryRow]) -> List[AblationRow]:
    full = row_lookup(summary, "return_selected_social_gru", "none")
    rows: List[AblationRow] = []
    for ablation in ("regime_signal", "social_culture", "memory", "body"):
        row = row_lookup(summary, "return_selected_social_gru", ablation)
        rows.append(
            AblationRow(
                architecture="return_selected_social_gru",
                ablation=ablation,
                mean_score=row.mean_long_horizon_score,
                score_loss=full.mean_long_horizon_score - row.mean_long_horizon_score,
                mean_social_response_score=row.mean_social_response_score,
                social_response_loss=full.mean_social_response_score - row.mean_social_response_score,
                mean_variant_targeted_rate=row.mean_variant_targeted_rate,
                variant_targeted_loss=full.mean_variant_targeted_rate - row.mean_variant_targeted_rate,
                mean_culture_score=row.mean_culture_score,
                culture_loss=full.mean_culture_score - row.mean_culture_score,
            )
        )
    return rows


def verdict_from_summary(summary: Sequence[SummaryRow], ablations: Sequence[AblationRow], selected_bias: float) -> VerdictRow:
    selected = row_lookup(summary, "return_selected_social_gru", "none")
    fixed = row_lookup(summary, "fixed_social_gru", "none")
    frame = row_lookup(summary, "social_frame", "none")
    reactive = row_lookup(summary, "scripted", "reactive_survival_only")
    by_ablation = {row.ablation: row for row in ablations}
    gain_over_fixed = selected.mean_long_horizon_score - fixed.mean_long_horizon_score
    supports_controller = (
        selected.no_major_regime_before_12h_rate == 1.0
        and selected.hidden_regime_after_12h_rate == 1.0
        and selected.mean_alive_at_12h >= 8.0
        and selected.mean_final_alive >= 7.0
        and selected.mean_long_horizon_score >= 0.56
        and selected.mean_social_response_score >= 0.54
        and selected.mean_variant_targeted_rate >= 0.34
        and selected.mean_long_horizon_score - reactive.mean_long_horizon_score >= 0.10
    )
    supports_ablation = (
        by_ablation["social_culture"].score_loss >= 0.030
        and by_ablation["social_culture"].social_response_loss >= 0.030
        and by_ablation["social_culture"].variant_targeted_loss >= 0.10
    )
    if supports_controller and supports_ablation:
        verdict = "pass"
    elif supports_controller:
        verdict = "partial"
    else:
        verdict = "failed"
    return VerdictRow(
        selected_option_bias=selected_bias,
        return_selected_score=selected.mean_long_horizon_score,
        fixed_bias_score=fixed.mean_long_horizon_score,
        option_frame_score=frame.mean_long_horizon_score,
        reactive_score=reactive.mean_long_horizon_score,
        gain_over_fixed_bias=gain_over_fixed,
        gain_over_frame=selected.mean_long_horizon_score - frame.mean_long_horizon_score,
        gain_over_reactive=selected.mean_long_horizon_score - reactive.mean_long_horizon_score,
        social_culture_ablation_loss=by_ablation["social_culture"].score_loss,
        social_culture_response_loss=by_ablation["social_culture"].social_response_loss,
        regime_signal_response_loss=by_ablation["regime_signal"].social_response_loss,
        memory_ablation_loss=by_ablation["memory"].score_loss,
        body_ablation_loss=by_ablation["body"].score_loss,
        social_response_score=selected.mean_social_response_score,
        variant_targeted_rate=selected.mean_variant_targeted_rate,
        shock_gate_pass_rate=selected.no_major_regime_before_12h_rate,
        hidden_regime_rate=selected.hidden_regime_after_12h_rate,
        supports_social_culture_controller=supports_controller,
        supports_social_culture_ablation=supports_ablation,
        verdict=verdict,
    )


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    p95.rows_to_csv(path, rows)


def write_json(path: Path, payload: object) -> None:
    p95.write_json(path, payload)


def write_js(path: Path, variable: str, payload: object) -> None:
    p95.write_js(path, variable, payload)


def run_benchmark(cfg: Config) -> Dict[str, object]:
    device, feature_mean, feature_std, models, training_rows = train_models(cfg)
    selected_bias, bias_rows = select_option_bias(cfg, models["option_gru"], device, feature_mean, feature_std)
    eval_rows: List[EvalRow] = []
    trace: List[Dict[str, object]] = []
    for seed in cfg.eval_seeds:
        eval_rows.append(run_reactive_episode(seed, cfg))
        selected_row, maybe_trace = run_model_episode(
            seed,
            "return_selected_social_gru",
            models["option_gru"],
            device,
            feature_mean,
            feature_std,
            cfg,
            selected_bias,
            trace=(seed == cfg.trace_seed),
        )
        eval_rows.append(selected_row)
        if maybe_trace:
            trace = maybe_trace
        fixed_row, _ = run_model_episode(seed, "fixed_social_gru", models["option_gru"], device, feature_mean, feature_std, cfg, 1.35)
        eval_rows.append(fixed_row)
        frame_row, _ = run_model_episode(seed, "social_frame", models["option_frame"], device, feature_mean, feature_std, cfg, selected_bias)
        eval_rows.append(frame_row)
        for ablation in ("regime_signal", "social_culture", "memory", "body"):
            row, _ = run_model_episode(seed, "return_selected_social_gru", models["option_gru"], device, feature_mean, feature_std, cfg, selected_bias, ablation=ablation)
            eval_rows.append(row)

    summary = summarize(eval_rows)
    variant_summary = summarize_variants(eval_rows)
    ablations = make_ablations(summary)
    verdict = verdict_from_summary(summary, ablations, selected_bias)
    payload = {
        "config": {
            "train_seeds": list(cfg.train_seeds),
            "tune_seeds": list(cfg.tune_seeds),
            "eval_seeds": list(cfg.eval_seeds),
            "bias_candidates": list(cfg.bias_candidates),
            "social_variants": list(SOCIAL_VARIANTS),
            "hours": cfg.hours,
            "step_hours": cfg.step_hours,
            "population": cfg.population,
            "epochs": cfg.epochs,
            "hidden_size": cfg.hidden_size,
            "learning_rate": cfg.learning_rate,
            "option_loss_weight": cfg.option_loss_weight,
            "device": str(device),
            "trace_seed": cfg.trace_seed,
        },
        "training": [asdict(row) for row in training_rows],
        "bias_selection": [asdict(row) for row in bias_rows],
        "eval": [asdict(row) for row in eval_rows],
        "summary": [asdict(row) for row in summary],
        "variant_summary": [asdict(row) for row in variant_summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace,
        "notes": {
            "claim": "social/culture hidden-regime learned controller precursor",
            "not_claimed": "subjective consciousness, open-ended civilization, or full deep reinforcement learning",
            "label_discipline": "all hidden variants share the social symptom channel; the model receives no variant label",
            "purpose": "tests the Report 97 weakness where social/culture ablation did not matter",
        },
    }
    prefix = ARTIFACT_DIR / "ssrm_3d_social_culture_hidden_regime_controller"
    rows_to_csv(Path(f"{prefix}_training.csv"), training_rows)
    rows_to_csv(Path(f"{prefix}_bias_selection.csv"), bias_rows)
    rows_to_csv(Path(f"{prefix}_eval.csv"), eval_rows)
    rows_to_csv(Path(f"{prefix}_summary.csv"), summary)
    rows_to_csv(Path(f"{prefix}_variant_summary.csv"), variant_summary)
    rows_to_csv(Path(f"{prefix}_ablations.csv"), ablations)
    rows_to_csv(Path(f"{prefix}_verdict.csv"), [verdict])
    write_json(Path(f"{prefix}_results.json"), payload)
    write_json(Path(f"{prefix}_trace.json"), trace)
    write_js(Path(f"{prefix}_results.js"), "SSRM_3D_SOCIAL_CULTURE_HIDDEN_REGIME_CONTROLLER_RESULTS", payload)
    write_js(Path(f"{prefix}_trace.js"), "SSRM_3D_SOCIAL_CULTURE_HIDDEN_REGIME_CONTROLLER_TRACE", trace)
    return payload


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-seeds", default="20260818,20260819,20260820,20260821,20260822,20260823,20260824,20260825")
    parser.add_argument("--tune-seeds", default="20260828,20260829,20260830,20260831,20260832")
    parser.add_argument("--eval-seeds", default="20260833,20260834,20260835,20260836,20260837")
    parser.add_argument("--bias-candidates", default="0.70,1.00,1.35,1.70,2.10")
    parser.add_argument("--hours", type=float, default=16.0)
    parser.add_argument("--step-hours", type=float, default=0.08)
    parser.add_argument("--population", type=int, default=10)
    parser.add_argument("--epochs", type=int, default=100)
    parser.add_argument("--hidden-size", type=int, default=56)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--option-loss-weight", type=float, default=0.62)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--trace-seed", type=int, default=20260833)
    args = parser.parse_args()
    return Config(
        train_seeds=parse_seed_list(args.train_seeds),
        tune_seeds=parse_seed_list(args.tune_seeds),
        eval_seeds=parse_seed_list(args.eval_seeds),
        bias_candidates=parse_float_list(args.bias_candidates),
        hours=args.hours,
        step_hours=args.step_hours,
        population=args.population,
        epochs=args.epochs,
        hidden_size=args.hidden_size,
        learning_rate=args.learning_rate,
        option_loss_weight=args.option_loss_weight,
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({"bias_selection": payload["bias_selection"], "verdict": payload["verdict"], "summary": payload["summary"]}, indent=2))
    return 0 if payload["verdict"]["verdict"] in {"pass", "partial"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
