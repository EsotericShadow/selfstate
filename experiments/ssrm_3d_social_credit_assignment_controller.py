#!/usr/bin/env python3
"""Social credit-assignment controller for SSRM-3D.

Report 98 made hidden social/culture regimes explicit, but the learned
controller still fell back to broad social recovery habits. This benchmark adds
opportunity costs: post-12h social shocks require different repair actions, and
spending the window on the wrong repair makes other social failures worse.

The model receives no credit-regime label. It observes the same embodied,
world, social/culture, symptom, memory, time, and previous-action channels used
by the learned hidden-regime controller family.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import random
import statistics
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import torch


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
REPORT98_PATH = ROOT / "experiments" / "ssrm_3d_social_culture_hidden_regime_controller.py"


def load_report98_module():
    spec = importlib.util.spec_from_file_location("ssrm_social_culture_98", REPORT98_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {REPORT98_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


r98 = load_report98_module()
p96 = r98.p96
p95 = r98.p95
h = r98.h

ACTIONS = p95.ACTIONS
ACTION_TO_INDEX = p95.ACTION_TO_INDEX
INDEX_TO_ACTION = p95.INDEX_TO_ACTION
CHECKPOINTS = p95.CHECKPOINTS

CREDIT_VARIANTS = (
    "trust_repair",
    "convention_repair",
    "coalition_repair",
    "teacher_replacement",
    "rumor_correction",
)
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
    epochs: int = 110
    hidden_size: int = 64
    learning_rate: float = 0.004
    option_loss_weight: float = 0.62
    device: str = "auto"
    trace_seed: int = 20260853


@dataclass(frozen=True)
class BiasSelectionRow:
    option_bias: float
    mean_score: float
    mean_credit_response_score: float
    mean_targeted_repair_rate: float
    mean_opportunity_score: float
    selection_objective: float
    selected: bool


@dataclass(frozen=True)
class EvalRow:
    seed: int
    credit_variant: str
    architecture: str
    condition: str
    final_alive: int
    total_agents: int
    alive_at_12h: int
    no_major_regime_before_12h: bool
    hidden_regime_after_12h: bool
    final_trust: float
    final_conflict: float
    final_social_inequality: float
    final_reputation_accuracy: float
    final_symbol_convergence: float
    final_teaching: float
    final_culture_memory: float
    final_knowledge_transfer: float
    opportunity_loss: float
    wrong_repair_rate: float
    targeted_repair_rate: float
    social_inference_score: float
    credit_response_score: float
    opportunity_score: float
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
    mean_credit_response_score: float
    mean_opportunity_score: float
    mean_targeted_repair_rate: float
    mean_wrong_repair_rate: float
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
    credit_variant: str
    architecture: str
    condition: str
    mean_long_horizon_score: float
    mean_credit_response_score: float
    mean_targeted_repair_rate: float
    mean_wrong_repair_rate: float
    mean_opportunity_score: float


@dataclass(frozen=True)
class AblationRow:
    architecture: str
    ablation: str
    mean_score: float
    score_loss: float
    mean_credit_response_score: float
    credit_response_loss: float
    mean_targeted_repair_rate: float
    targeted_repair_loss: float
    mean_opportunity_score: float
    opportunity_loss: float
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
    social_culture_targeted_loss: float
    social_culture_opportunity_loss: float
    regime_signal_response_loss: float
    memory_ablation_loss: float
    credit_response_score: float
    targeted_repair_rate: float
    wrong_repair_rate: float
    opportunity_score: float
    shock_gate_pass_rate: float
    hidden_regime_rate: float
    supports_credit_assignment_controller: bool
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


def credit_variant_for_seed(seed: int) -> str:
    return CREDIT_VARIANTS[seed % len(CREDIT_VARIANTS)]


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


def make_credit_world(seed: int, rng: random.Random):
    world = h.make_world(seed, rng)
    world.regime_name = "trust_fracture"
    world.credit_variant = credit_variant_for_seed(seed)
    world.first_regime_hour = 12.30 + rng.random() * 0.45
    world.trust = 0.66
    world.conflict = 0.08
    world.social_inequality = 0.10
    world.reputation_accuracy = 0.48
    world.symbol_convergence = 0.32
    world.teaching = 0.14
    world.risk_memory = 0.12
    world.culture_memory = 0.12
    world.knowledge_transfer = 0.0
    world.credit_post_action_count = 0
    world.credit_targeted_action_count = 0
    world.credit_wrong_action_count = 0
    world.credit_opportunity_loss = 0.0
    return world


def current_target_actions(world) -> Tuple[str, ...]:
    variant = world.credit_variant
    if variant in {"trust_repair", "coalition_repair"}:
        return ("mediate",)
    if variant in {"convention_repair", "teacher_replacement"}:
        return ("teach",)
    if variant == "rumor_correction":
        return ("inspect",) if world.risk_memory < 0.50 else ("mediate",)
    raise ValueError(f"unknown credit variant {variant!r}")


def apply_credit_regime(world, condition, dt: float) -> None:
    if not h.regime_active(world):
        return
    variant = world.credit_variant
    world.regime_anomalies["social"] = clamp(world.regime_anomalies["social"] + 0.155 * dt)
    world.hidden_pressure = clamp(world.hidden_pressure + 0.042 * dt)
    if variant == "trust_repair":
        world.trust = clamp(world.trust - 0.075 * dt)
        world.conflict = clamp(world.conflict + 0.070 * dt)
        world.reputation_accuracy = clamp(world.reputation_accuracy - 0.030 * dt)
        world.social_inequality = clamp(world.social_inequality + 0.022 * dt)
    elif variant == "convention_repair":
        world.symbol_convergence = clamp(world.symbol_convergence - 0.090 * dt)
        world.culture_memory = clamp(world.culture_memory - 0.052 * dt)
        world.knowledge_transfer = clamp(world.knowledge_transfer - 0.040 * dt)
        world.trust = clamp(world.trust - 0.020 * dt)
    elif variant == "coalition_repair":
        world.social_inequality = clamp(world.social_inequality + 0.085 * dt)
        world.conflict = clamp(world.conflict + 0.060 * dt)
        world.trust = clamp(world.trust - 0.046 * dt)
        world.food = clamp(world.food - 0.014 * dt)
        world.water = clamp(world.water - 0.012 * dt)
    elif variant == "teacher_replacement":
        world.teaching = clamp(world.teaching - 0.078 * dt)
        world.culture_memory = clamp(world.culture_memory - 0.060 * dt)
        world.knowledge_transfer = clamp(world.knowledge_transfer - 0.052 * dt)
        world.tool_design = clamp(world.tool_design - 0.012 * dt)
        world.architecture = clamp(world.architecture - 0.010 * dt)
    elif variant == "rumor_correction":
        world.reputation_accuracy = clamp(world.reputation_accuracy - 0.085 * dt)
        world.conflict = clamp(world.conflict + 0.064 * dt)
        world.trust = clamp(world.trust - 0.056 * dt)
        world.symbol_convergence = clamp(world.symbol_convergence - 0.032 * dt)
    if not condition.reputation_influence:
        world.trust = clamp(world.trust - 0.024 * dt)
        world.conflict = clamp(world.conflict + 0.024 * dt)
    if not condition.teaching:
        world.symbol_convergence = clamp(world.symbol_convergence - 0.022 * dt)
        world.knowledge_transfer = clamp(world.knowledge_transfer - 0.022 * dt)
    world.food = clamp(world.food - world.credit_opportunity_loss * 0.010 * dt)
    world.water = clamp(world.water - world.credit_opportunity_loss * 0.010 * dt)


def urgent_survival_action(agent, world) -> str | None:
    urgent = max(
        agent.hunger,
        agent.thirst,
        max(0.0, 0.40 - world.food) * 1.35,
        max(0.0, 0.40 - world.water) * 1.45,
        max(0.0, 0.38 - agent.health) * 1.15,
        max(0.0, 0.23 - agent.energy) * 1.15,
    )
    if urgent <= 0.76:
        return None
    if agent.energy < 0.22 or agent.health < 0.40:
        return "rest"
    return "harvest_water" if world.water < world.food or agent.thirst > agent.hunger else "harvest_food"


def choose_credit_teacher_action(agent, world, condition, rng: random.Random) -> str:
    if condition.name == "reactive_survival_only":
        if agent.energy < 0.26 or agent.health < 0.46:
            return "rest"
        return "harvest_water" if world.water < world.food or agent.thirst > agent.hunger else "harvest_food"
    urgent = urgent_survival_action(agent, world)
    if urgent:
        return urgent
    if h.regime_active(world):
        return current_target_actions(world)[0]
    if world.shelter < 0.58 or world.architecture < 0.52 or world.waterworks < 0.42:
        return "construct"
    if world.tool_quality < 0.46 or world.tool_design < 0.42:
        return "redesign_tools"
    if world.teaching < 0.56 or world.culture_memory < 0.40 or world.symbol_convergence < 0.44:
        return "teach"
    if world.conflict > 0.24 or world.trust < 0.56 or world.social_inequality > 0.22:
        return "mediate"
    if world.food < 0.58 or world.water < 0.58:
        return "harvest_water" if world.water < world.food else "harvest_food"
    if agent.energy < 0.38 or agent.stress > 0.60:
        return "rest"
    return rng.choice(("inspect", "construct", "teach", "mediate", "redesign_tools", "rest"))


def record_and_apply_credit_effect(world, action: str, dt: float) -> None:
    if not h.regime_active(world):
        return
    world.credit_post_action_count += 1
    correct = action in current_target_actions(world)
    if correct:
        world.credit_targeted_action_count += 1
        if world.credit_variant == "trust_repair":
            world.trust = clamp(world.trust + 0.110 * dt)
            world.conflict = clamp(world.conflict - 0.120 * dt)
            world.reputation_accuracy = clamp(world.reputation_accuracy + 0.052 * dt)
            world.social_inequality = clamp(world.social_inequality - 0.026 * dt)
        elif world.credit_variant == "convention_repair":
            world.symbol_convergence = clamp(world.symbol_convergence + 0.125 * dt)
            world.culture_memory = clamp(world.culture_memory + 0.078 * dt)
            world.knowledge_transfer = clamp(world.knowledge_transfer + 0.070 * dt)
            world.teaching = clamp(world.teaching + 0.060 * dt)
        elif world.credit_variant == "coalition_repair":
            world.social_inequality = clamp(world.social_inequality - 0.125 * dt)
            world.conflict = clamp(world.conflict - 0.085 * dt)
            world.trust = clamp(world.trust + 0.070 * dt)
            world.food = clamp(world.food + 0.010 * dt)
            world.water = clamp(world.water + 0.010 * dt)
        elif world.credit_variant == "teacher_replacement":
            world.teaching = clamp(world.teaching + 0.120 * dt)
            world.culture_memory = clamp(world.culture_memory + 0.085 * dt)
            world.knowledge_transfer = clamp(world.knowledge_transfer + 0.090 * dt)
            world.tool_design = clamp(world.tool_design + 0.020 * dt)
            world.architecture = clamp(world.architecture + 0.014 * dt)
        elif world.credit_variant == "rumor_correction":
            if action == "inspect":
                world.risk_memory = clamp(world.risk_memory + 0.120 * dt)
                world.reputation_accuracy = clamp(world.reputation_accuracy + 0.040 * dt)
            else:
                world.reputation_accuracy = clamp(world.reputation_accuracy + 0.085 * dt)
                world.trust = clamp(world.trust + 0.070 * dt)
                world.conflict = clamp(world.conflict - 0.085 * dt)
        world.credit_opportunity_loss = clamp(world.credit_opportunity_loss - 0.020 * dt)
        return

    world.credit_wrong_action_count += 1
    world.credit_opportunity_loss = clamp(world.credit_opportunity_loss + 0.034 * dt)
    world.conflict = clamp(world.conflict + 0.035 * dt)
    world.trust = clamp(world.trust - 0.026 * dt)
    if action == "teach" and world.credit_variant in {"trust_repair", "coalition_repair"}:
        world.social_inequality = clamp(world.social_inequality + 0.048 * dt)
        world.reputation_accuracy = clamp(world.reputation_accuracy - 0.022 * dt)
    elif action == "mediate" and world.credit_variant in {"convention_repair", "teacher_replacement"}:
        world.symbol_convergence = clamp(world.symbol_convergence - 0.050 * dt)
        world.knowledge_transfer = clamp(world.knowledge_transfer - 0.038 * dt)
    elif action not in {"teach", "mediate", "inspect"}:
        world.food = clamp(world.food - 0.008 * dt)
        world.water = clamp(world.water - 0.008 * dt)


def social_inference_score(world) -> float:
    target = world.beliefs["social"]
    distractors = [value for key, value in world.beliefs.items() if key != "social"]
    margin = target - mean(distractors)
    return clamp(target * 0.72 + max(0.0, margin) * 0.58)


def credit_response_score(world) -> float:
    if world.credit_variant == "trust_repair":
        return clamp(world.trust * 0.34 + (1.0 - world.conflict) * 0.28 + world.reputation_accuracy * 0.22 + (1.0 - world.social_inequality) * 0.16)
    if world.credit_variant == "convention_repair":
        return clamp(world.symbol_convergence * 0.36 + world.culture_memory * 0.24 + world.knowledge_transfer * 0.22 + world.teaching * 0.18)
    if world.credit_variant == "coalition_repair":
        return clamp((1.0 - world.social_inequality) * 0.34 + world.trust * 0.22 + (1.0 - world.conflict) * 0.22 + world.food * 0.11 + world.water * 0.11)
    if world.credit_variant == "teacher_replacement":
        return clamp(world.teaching * 0.32 + world.knowledge_transfer * 0.30 + world.culture_memory * 0.20 + world.tool_design * 0.10 + world.architecture * 0.08)
    return clamp(world.reputation_accuracy * 0.34 + world.risk_memory * 0.22 + world.trust * 0.20 + (1.0 - world.conflict) * 0.18 + world.symbol_convergence * 0.06)


def culture_score(world) -> float:
    return clamp(world.knowledge_transfer * 0.34 + world.teaching * 0.24 + world.culture_memory * 0.18 + world.symbol_convergence * 0.14 + world.reputation_accuracy * 0.08 + world.risk_memory * 0.04)


def development_score(world, baseline: Dict[str, float]) -> float:
    return clamp(
        max(0.0, world.architecture - baseline["architecture"]) * 0.34
        + max(0.0, world.tool_design - baseline["tool_design"]) * 0.26
        + max(0.0, world.sanitation - baseline["sanitation"]) * 0.16
        + max(0.0, world.path_network - 0.14) * 0.12
        + max(0.0, world.food_storage - 0.18) * 0.12
    )


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


def score_episode(seed: int, architecture: str, condition: str, world, agents, baseline: Dict[str, float], alive_at_12h: int | None, no_major_before_12: bool) -> EvalRow:
    final_alive = len(h.living(agents))
    total_agents = len(agents)
    survival = final_alive / max(1, total_agents)
    development = development_score(world, baseline)
    culture = culture_score(world)
    response = credit_response_score(world)
    inference = social_inference_score(world)
    targeted = world.credit_targeted_action_count / max(1, world.credit_post_action_count)
    wrong = world.credit_wrong_action_count / max(1, world.credit_post_action_count)
    opportunity = clamp(1.0 - world.credit_opportunity_loss)
    score = clamp(
        survival * 0.16
        + development * 0.10
        + culture * 0.18
        + response * 0.30
        + inference * 0.08
        + targeted * 0.12
        + opportunity * 0.06
    )
    return EvalRow(
        seed=seed,
        credit_variant=world.credit_variant,
        architecture=architecture,
        condition=condition,
        final_alive=final_alive,
        total_agents=total_agents,
        alive_at_12h=alive_at_12h if alive_at_12h is not None else final_alive,
        no_major_regime_before_12h=no_major_before_12,
        hidden_regime_after_12h=world.first_regime_hour >= 12.0 and h.regime_active(world),
        final_trust=world.trust,
        final_conflict=world.conflict,
        final_social_inequality=world.social_inequality,
        final_reputation_accuracy=world.reputation_accuracy,
        final_symbol_convergence=world.symbol_convergence,
        final_teaching=world.teaching,
        final_culture_memory=world.culture_memory,
        final_knowledge_transfer=world.knowledge_transfer,
        opportunity_loss=world.credit_opportunity_loss,
        wrong_repair_rate=wrong,
        targeted_repair_rate=targeted,
        social_inference_score=inference,
        credit_response_score=response,
        opportunity_score=opportunity,
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
        "credit_variant": world.credit_variant,
        "regime_active": h.regime_active(world),
        "alive": len(alive),
        "total_agents": len(agents),
        "last_option": last_option,
        "last_action": last_action,
        "target_actions": list(current_target_actions(world)) if h.regime_active(world) else [],
        "trust": world.trust,
        "conflict": world.conflict,
        "social_inequality": world.social_inequality,
        "reputation_accuracy": world.reputation_accuracy,
        "symbol_convergence": world.symbol_convergence,
        "teaching": world.teaching,
        "culture_memory": world.culture_memory,
        "knowledge_transfer": world.knowledge_transfer,
        "risk_memory": world.risk_memory,
        "opportunity_loss": world.credit_opportunity_loss,
        "targeted_repair_rate": world.credit_targeted_action_count / max(1, world.credit_post_action_count),
        "wrong_repair_rate": world.credit_wrong_action_count / max(1, world.credit_post_action_count),
        "credit_response_score": credit_response_score(world),
        "social_inference_score": social_inference_score(world),
        "dominant_belief": h.dominant_belief(world),
        "beliefs": dict(world.beliefs),
        "mean_wisdom": mean(agent.wisdom for agent in alive),
        "mean_influence": mean(agent.influence for agent in alive),
    }


def run_world_loop(seed: int, cfg: Config, actor, condition, architecture: str, label: str, *, trace: bool = False) -> Tuple[EvalRow, List[Dict[str, object]]]:
    rng = random.Random(seed * 271 + 53)
    agents = h.make_agents(rng, cfg.population)
    world = make_credit_world(seed, rng)
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
        apply_credit_regime(world, condition, dt)
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
            record_and_apply_credit_effect(world, action, dt)
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
    return score_episode(seed, architecture, label, world, agents, baseline, alive_at_12h, no_major_before_12), snapshots


def generate_teacher_sequences(cfg: Config) -> Tuple[torch.Tensor, torch.Tensor]:
    xs: List[List[List[float]]] = []
    ys: List[List[int]] = []
    condition = teacher_condition()
    for seed in cfg.train_seeds:
        seed_xs: List[List[List[float]]] = [[] for _ in range(cfg.population)]
        seed_ys: List[List[int]] = [[] for _ in range(cfg.population)]
        rng = random.Random(seed * 271 + 53)
        agents = h.make_agents(rng, cfg.population)
        world = make_credit_world(seed, rng)
        h.current_agents = agents
        previous_actions = [ACTION_TO_INDEX["rest"] for _ in range(cfg.population)]
        while world.time < cfg.hours - 1e-9:
            dt = min(cfg.step_hours, cfg.hours - world.time)
            world.time += dt
            h.apply_baseline_environment(world, agents, condition, dt, rng)
            apply_credit_regime(world, condition, dt)
            signals = h.symptom_channels(world, condition, rng)
            h.update_beliefs(world, condition, signals, dt)
            pressure = h.pressure_score(world, agents)
            world.pressure_integral = clamp(world.pressure_integral + pressure * dt / max(cfg.hours, 1.0))
            h.update_agent_influence(agents, condition.reputation_influence)
            for index, agent in enumerate(agents[: cfg.population]):
                if not agent.alive or agent.child:
                    seed_xs[index].append(p95.observation(agent, world, signals, previous_actions[index]))
                    seed_ys[index].append(ACTION_TO_INDEX["rest"])
                    continue
                action = choose_credit_teacher_action(agent, world, condition, rng)
                action_index = ACTION_TO_INDEX[action]
                seed_xs[index].append(p95.observation(agent, world, signals, previous_actions[index]))
                seed_ys[index].append(action_index)
                record_and_apply_credit_effect(world, action, dt)
                h.apply_action(agent, world, condition, action, dt, rng)
                previous_actions[index] = action_index
            p95.apply_body_dynamics(world, agents, dt)
            h.maybe_reproduce(world, agents, condition, rng, dt)
        xs.extend(seed_xs)
        ys.extend(seed_ys)
    return torch.tensor(xs, dtype=torch.float32), torch.tensor(ys, dtype=torch.long)


def boost_credit_sample_weights(train_x_raw: torch.Tensor, train_y: torch.Tensor, weights: torch.Tensor) -> torch.Tensor:
    boosted = weights.clone()
    for seq in range(train_y.shape[0]):
        for step in range(train_y.shape[1]):
            features = train_x_raw[seq, step]
            social_signal = float(features[40].item())
            if social_signal < 0.16:
                continue
            action = INDEX_TO_ACTION[int(train_y[seq, step].item())]
            multiplier = 1.0 + social_signal * 5.0
            if action == "mediate":
                multiplier *= 2.8
            elif action == "teach":
                multiplier *= 2.4
            elif action == "inspect":
                multiplier *= 2.2
            boosted[seq, step] *= multiplier
    return boosted


def train_models(cfg: Config):
    device = p96.resolve_device(cfg.device)
    train_x_raw, train_y = generate_teacher_sequences(cfg)
    option_y, sample_weights = p96.derive_option_targets(train_x_raw, train_y)
    sample_weights = boost_credit_sample_weights(train_x_raw, train_y, sample_weights)
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


def run_model_episode(seed: int, architecture: str, model, device, feature_mean, feature_std, cfg: Config, option_bias: float, *, ablation: str = "none", trace: bool = False) -> Tuple[EvalRow, List[Dict[str, object]]]:
    def actor(agent, world, signals, previous_action, state, rng):
        return choose_model_action(model, device, feature_mean, feature_std, agent, world, signals, previous_action, state, cfg, option_bias, ablation)

    return run_world_loop(seed, cfg, actor, teacher_condition(), architecture, ablation, trace=trace)


def run_reactive_episode(seed: int, cfg: Config) -> EvalRow:
    def actor(agent, world, signals, previous_action, state, rng):
        action = choose_credit_teacher_action(agent, world, reactive_condition(), rng)
        return action, ACTION_TO_INDEX[action], "reactive", None

    row, _ = run_world_loop(seed, cfg, actor, reactive_condition(), "scripted", "reactive_survival_only", trace=False)
    return row


def selection_objective(rows: Sequence[EvalRow]) -> Tuple[float, float, float, float, float]:
    score = mean(row.long_horizon_score for row in rows)
    response = mean(row.credit_response_score for row in rows)
    targeted = mean(row.targeted_repair_rate for row in rows)
    opportunity = mean(row.opportunity_score for row in rows)
    objective = score + response * 0.16 + targeted * 0.12 + opportunity * 0.06
    return score, response, targeted, opportunity, objective


def select_option_bias(cfg: Config, model, device, feature_mean, feature_std) -> Tuple[float, List[BiasSelectionRow]]:
    best_bias = cfg.bias_candidates[0]
    best_objective = -1.0
    rows: List[BiasSelectionRow] = []
    for option_bias in cfg.bias_candidates:
        eval_rows = [
            run_model_episode(seed, "return_selected_credit_gru", model, device, feature_mean, feature_std, cfg, option_bias)[0]
            for seed in cfg.tune_seeds
        ]
        score, response, targeted, opportunity, objective = selection_objective(eval_rows)
        if objective > best_objective:
            best_bias = option_bias
            best_objective = objective
        rows.append(BiasSelectionRow(option_bias, score, response, targeted, opportunity, objective, False))
    return best_bias, [
        BiasSelectionRow(row.option_bias, row.mean_score, row.mean_credit_response_score, row.mean_targeted_repair_rate, row.mean_opportunity_score, row.selection_objective, row.option_bias == best_bias)
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
                mean_credit_response_score=mean(row.credit_response_score for row in items),
                mean_opportunity_score=mean(row.opportunity_score for row in items),
                mean_targeted_repair_rate=mean(row.targeted_repair_rate for row in items),
                mean_wrong_repair_rate=mean(row.wrong_repair_rate for row in items),
                mean_final_alive=mean(row.final_alive for row in items),
                mean_alive_at_12h=mean(row.alive_at_12h for row in items),
                mean_trust=mean(row.final_trust for row in items),
                mean_conflict=mean(row.final_conflict for row in items),
                mean_social_inequality=mean(row.final_social_inequality for row in items),
                mean_reputation_accuracy=mean(row.final_reputation_accuracy for row in items),
                mean_symbol_convergence=mean(row.final_symbol_convergence for row in items),
                mean_knowledge_transfer=mean(row.final_knowledge_transfer for row in items),
                no_major_regime_before_12h_rate=mean(1.0 if row.no_major_regime_before_12h else 0.0 for row in items),
                hidden_regime_after_12h_rate=mean(1.0 if row.hidden_regime_after_12h else 0.0 for row in items),
            )
        )
    return out


def summarize_variants(rows: Sequence[EvalRow]) -> List[VariantSummaryRow]:
    buckets: Dict[Tuple[str, str, str], List[EvalRow]] = {}
    for row in rows:
        buckets.setdefault((row.credit_variant, row.architecture, row.condition), []).append(row)
    out: List[VariantSummaryRow] = []
    for (variant, architecture, condition), items in sorted(buckets.items()):
        out.append(
            VariantSummaryRow(
                credit_variant=variant,
                architecture=architecture,
                condition=condition,
                mean_long_horizon_score=mean(row.long_horizon_score for row in items),
                mean_credit_response_score=mean(row.credit_response_score for row in items),
                mean_targeted_repair_rate=mean(row.targeted_repair_rate for row in items),
                mean_wrong_repair_rate=mean(row.wrong_repair_rate for row in items),
                mean_opportunity_score=mean(row.opportunity_score for row in items),
            )
        )
    return out


def row_lookup(summary: Sequence[SummaryRow], architecture: str, condition: str) -> SummaryRow:
    for row in summary:
        if row.architecture == architecture and row.condition == condition:
            return row
    raise KeyError((architecture, condition))


def make_ablations(summary: Sequence[SummaryRow]) -> List[AblationRow]:
    full = row_lookup(summary, "return_selected_credit_gru", "none")
    rows: List[AblationRow] = []
    for ablation in ("regime_signal", "social_culture", "memory", "body"):
        row = row_lookup(summary, "return_selected_credit_gru", ablation)
        rows.append(
            AblationRow(
                architecture="return_selected_credit_gru",
                ablation=ablation,
                mean_score=row.mean_long_horizon_score,
                score_loss=full.mean_long_horizon_score - row.mean_long_horizon_score,
                mean_credit_response_score=row.mean_credit_response_score,
                credit_response_loss=full.mean_credit_response_score - row.mean_credit_response_score,
                mean_targeted_repair_rate=row.mean_targeted_repair_rate,
                targeted_repair_loss=full.mean_targeted_repair_rate - row.mean_targeted_repair_rate,
                mean_opportunity_score=row.mean_opportunity_score,
                opportunity_loss=full.mean_opportunity_score - row.mean_opportunity_score,
                mean_culture_score=row.mean_culture_score,
                culture_loss=full.mean_culture_score - row.mean_culture_score,
            )
        )
    return rows


def verdict_from_summary(summary: Sequence[SummaryRow], ablations: Sequence[AblationRow], selected_bias: float) -> VerdictRow:
    selected = row_lookup(summary, "return_selected_credit_gru", "none")
    fixed = row_lookup(summary, "fixed_credit_gru", "none")
    frame = row_lookup(summary, "credit_frame", "none")
    reactive = row_lookup(summary, "scripted", "reactive_survival_only")
    by_ablation = {row.ablation: row for row in ablations}
    supports_controller = (
        selected.no_major_regime_before_12h_rate == 1.0
        and selected.hidden_regime_after_12h_rate == 1.0
        and selected.mean_alive_at_12h >= 8.0
        and selected.mean_final_alive >= 7.0
        and selected.mean_long_horizon_score >= 0.56
        and selected.mean_credit_response_score >= 0.56
        and selected.mean_targeted_repair_rate >= 0.34
        and selected.mean_wrong_repair_rate <= 0.66
        and selected.mean_long_horizon_score - reactive.mean_long_horizon_score >= 0.10
    )
    supports_ablation = (
        by_ablation["social_culture"].score_loss >= 0.030
        and by_ablation["social_culture"].credit_response_loss >= 0.030
        and by_ablation["social_culture"].targeted_repair_loss >= 0.060
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
        gain_over_fixed_bias=selected.mean_long_horizon_score - fixed.mean_long_horizon_score,
        gain_over_frame=selected.mean_long_horizon_score - frame.mean_long_horizon_score,
        gain_over_reactive=selected.mean_long_horizon_score - reactive.mean_long_horizon_score,
        social_culture_ablation_loss=by_ablation["social_culture"].score_loss,
        social_culture_response_loss=by_ablation["social_culture"].credit_response_loss,
        social_culture_targeted_loss=by_ablation["social_culture"].targeted_repair_loss,
        social_culture_opportunity_loss=by_ablation["social_culture"].opportunity_loss,
        regime_signal_response_loss=by_ablation["regime_signal"].credit_response_loss,
        memory_ablation_loss=by_ablation["memory"].score_loss,
        credit_response_score=selected.mean_credit_response_score,
        targeted_repair_rate=selected.mean_targeted_repair_rate,
        wrong_repair_rate=selected.mean_wrong_repair_rate,
        opportunity_score=selected.mean_opportunity_score,
        shock_gate_pass_rate=selected.no_major_regime_before_12h_rate,
        hidden_regime_rate=selected.hidden_regime_after_12h_rate,
        supports_credit_assignment_controller=supports_controller,
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
            "return_selected_credit_gru",
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
        fixed_row, _ = run_model_episode(seed, "fixed_credit_gru", models["option_gru"], device, feature_mean, feature_std, cfg, 1.35)
        eval_rows.append(fixed_row)
        frame_row, _ = run_model_episode(seed, "credit_frame", models["option_frame"], device, feature_mean, feature_std, cfg, selected_bias)
        eval_rows.append(frame_row)
        for ablation in ("regime_signal", "social_culture", "memory", "body"):
            row, _ = run_model_episode(seed, "return_selected_credit_gru", models["option_gru"], device, feature_mean, feature_std, cfg, selected_bias, ablation=ablation)
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
            "credit_variants": list(CREDIT_VARIANTS),
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
            "claim": "social credit-assignment learned controller precursor",
            "not_claimed": "subjective consciousness, open-ended civilization, or full deep reinforcement learning",
            "label_discipline": "all credit variants share the social symptom channel; the model receives no variant label",
            "purpose": "tests whether mutually exclusive social repair costs make social/culture state causally necessary",
        },
    }
    prefix = ARTIFACT_DIR / "ssrm_3d_social_credit_assignment_controller"
    rows_to_csv(Path(f"{prefix}_training.csv"), training_rows)
    rows_to_csv(Path(f"{prefix}_bias_selection.csv"), bias_rows)
    rows_to_csv(Path(f"{prefix}_eval.csv"), eval_rows)
    rows_to_csv(Path(f"{prefix}_summary.csv"), summary)
    rows_to_csv(Path(f"{prefix}_variant_summary.csv"), variant_summary)
    rows_to_csv(Path(f"{prefix}_ablations.csv"), ablations)
    rows_to_csv(Path(f"{prefix}_verdict.csv"), [verdict])
    write_json(Path(f"{prefix}_results.json"), payload)
    write_json(Path(f"{prefix}_trace.json"), trace)
    write_js(Path(f"{prefix}_results.js"), "SSRM_3D_SOCIAL_CREDIT_ASSIGNMENT_CONTROLLER_RESULTS", payload)
    write_js(Path(f"{prefix}_trace.js"), "SSRM_3D_SOCIAL_CREDIT_ASSIGNMENT_CONTROLLER_TRACE", trace)
    return payload


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-seeds", default="20260838,20260839,20260840,20260841,20260842,20260843,20260844,20260845")
    parser.add_argument("--tune-seeds", default="20260848,20260849,20260850,20260851,20260852")
    parser.add_argument("--eval-seeds", default="20260853,20260854,20260855,20260856,20260857")
    parser.add_argument("--bias-candidates", default="0.50,0.70,1.00,1.35,1.70")
    parser.add_argument("--hours", type=float, default=16.0)
    parser.add_argument("--step-hours", type=float, default=0.08)
    parser.add_argument("--population", type=int, default=10)
    parser.add_argument("--epochs", type=int, default=110)
    parser.add_argument("--hidden-size", type=int, default=64)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--option-loss-weight", type=float, default=0.62)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--trace-seed", type=int, default=20260853)
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
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
