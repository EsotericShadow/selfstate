#!/usr/bin/env python3
"""Learned closed-loop hidden-regime controller for SSRM-3D.

Report 94 made hidden world-rule changes measurable with a designed policy.
This experiment moves one step closer to the user's requested live simulation:
train neural controllers from symptom histories, then let the learned policy act
inside the hidden-regime world so its choices change the future state.

The training is imitation from a designed controller, not deep RL. The closed
loop is real in evaluation: model actions feed back into resources, health,
tools, shelter, teaching, social trust, and hidden-regime recovery.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import math
import random
import statistics
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

import torch
from torch import nn


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
HIDDEN_REGIME_PATH = ROOT / "experiments" / "ssrm_3d_hidden_regime_adaptation.py"


def load_hidden_regime_module():
    spec = importlib.util.spec_from_file_location("ssrm_hidden_regime", HIDDEN_REGIME_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {HIDDEN_REGIME_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


h = load_hidden_regime_module()


ACTIONS = (
    "rest",
    "harvest_water",
    "harvest_food",
    "inspect",
    "construct",
    "reinforce_shelter",
    "redesign_tools",
    "filter_water",
    "quarantine",
    "diversify_food",
    "teach",
    "mediate",
)
ACTION_TO_INDEX = {name: index for index, name in enumerate(ACTIONS)}
INDEX_TO_ACTION = {index: name for name, index in ACTION_TO_INDEX.items()}
CHECKPOINTS = (1.0, 6.0, 12.0, 12.5, 14.5, 16.0)
REGIME_CHANNEL_INDEX = {
    "contaminated_water": 36,
    "cold_wet_season": 37,
    "crop_blight": 38,
    "tool_fatigue": 39,
    "trust_fracture": 40,
}
FEATURE_GROUPS: Dict[str, Tuple[int, ...]] = {
    "body": tuple(range(0, 10)),
    "skill": tuple(range(10, 16)),
    "resources": tuple(range(16, 20)),
    "infrastructure": tuple(range(20, 29)),
    "social_culture": tuple(range(29, 36)),
    "symptoms": tuple(range(36, 41)),
    "memory": tuple(range(41, 46)),
    "time": tuple(range(46, 48)),
    "previous_action": tuple(range(48, 48 + len(ACTIONS))),
}
FEATURE_COUNT = 48 + len(ACTIONS)


@dataclass(frozen=True)
class Config:
    train_seeds: Sequence[int]
    eval_seeds: Sequence[int]
    hours: float = 16.0
    step_hours: float = 0.08
    population: int = 10
    epochs: int = 80
    hidden_size: int = 48
    learning_rate: float = 0.004
    device: str = "auto"
    trace_seed: int = 20260783


@dataclass(frozen=True)
class TrainingRow:
    architecture: str
    train_loss: float
    train_accuracy: float
    device_used: str
    parameter_count: int


@dataclass(frozen=True)
class EvalRow:
    seed: int
    regime: str
    architecture: str
    condition: str
    final_alive: int
    total_agents: int
    alive_at_12h: int
    hidden_regime_after_12h: bool
    no_major_regime_before_12h: bool
    final_food: float
    final_water: float
    final_trust: float
    architecture_delta: float
    tool_design_delta: float
    teaching_delta: float
    knowledge_transfer: float
    symbol_convergence: float
    inference_score: float
    response_score: float
    targeted_response_rate: float
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
    mean_inference_score: float
    mean_response_score: float
    mean_targeted_response_rate: float
    mean_final_alive: float
    mean_alive_at_12h: float
    mean_architecture_delta: float
    mean_tool_design_delta: float
    mean_knowledge_transfer: float
    mean_symbol_convergence: float
    no_major_regime_before_12h_rate: float
    hidden_regime_after_12h_rate: float


@dataclass(frozen=True)
class AblationRow:
    architecture: str
    ablation: str
    mean_score: float
    score_loss: float
    mean_response_score: float
    response_loss: float
    mean_inference_score: float
    inference_loss: float


@dataclass(frozen=True)
class VerdictRow:
    recurrent_score: float
    frame_score: float
    reactive_score: float
    recurrent_gain_over_frame: float
    recurrent_gain_over_reactive: float
    symptom_ablation_loss: float
    memory_ablation_loss: float
    social_culture_ablation_loss: float
    infrastructure_ablation_loss: float
    recurrent_inference_score: float
    recurrent_response_score: float
    recurrent_targeted_response_rate: float
    shock_gate_pass_rate: float
    hidden_regime_rate: float
    supports_closed_loop_learning_precursor: bool
    supports_ablation_specificity: bool
    verdict: str


class ControllerNet(nn.Module):
    def __init__(self, architecture: str, input_size: int, hidden_size: int, output_size: int) -> None:
        super().__init__()
        self.architecture = architecture
        self.hidden_size = hidden_size
        if architecture == "frame_mlp":
            self.frame = nn.Sequential(
                nn.Linear(input_size, hidden_size),
                nn.Tanh(),
                nn.Linear(hidden_size, hidden_size),
                nn.Tanh(),
            )
        elif architecture == "gru":
            self.recurrent = nn.GRU(input_size, hidden_size, batch_first=True)
        else:
            raise ValueError(f"unknown architecture {architecture!r}")
        self.head = nn.Linear(hidden_size, output_size)

    def forward(self, x: torch.Tensor, state: torch.Tensor | None = None) -> Tuple[torch.Tensor, torch.Tensor | None]:
        if self.architecture == "frame_mlp":
            hidden = self.frame(x)
            return self.head(hidden), None
        out, next_state = self.recurrent(x, state)
        return self.head(out), next_state

    def step(self, x: torch.Tensor, state: torch.Tensor | None = None) -> Tuple[torch.Tensor, torch.Tensor | None]:
        if self.architecture == "frame_mlp":
            logits, _ = self.forward(x)
            return logits, None
        logits, next_state = self.forward(x.unsqueeze(1), state)
        return logits[:, -1, :], next_state


def resolve_device(requested: str) -> torch.device:
    if requested == "auto":
        if torch.backends.mps.is_available():
            return torch.device("mps")
        if torch.cuda.is_available():
            return torch.device("cuda")
        return torch.device("cpu")
    return torch.device(requested)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def one_hot(index: int, size: int) -> List[float]:
    return [1.0 if i == index else 0.0 for i in range(size)]


def sensor_features(world, condition, rng: random.Random) -> Dict[str, float]:
    return h.symptom_channels(world, condition, rng)


def observation(agent, world, signals: Dict[str, float], previous_action: int) -> List[float]:
    day = (world.time % 2.4) / 2.4
    values = [
        float(agent.health),
        float(agent.energy),
        float(agent.hunger),
        float(agent.thirst),
        float(agent.stress),
        float(agent.cleanliness),
        float(agent.reserve),
        float(agent.wisdom),
        float(agent.adaptation),
        float(agent.influence),
        float(agent.skill_build),
        float(agent.skill_tool),
        float(agent.skill_forage),
        float(agent.skill_care),
        float(agent.skill_teach),
        1.0 if agent.child else 0.0,
        float(world.food),
        float(world.water),
        float(world.materials),
        float(world.medicine),
        float(world.shelter),
        float(world.architecture),
        float(world.tool_quality),
        float(world.tool_design),
        float(world.path_network),
        float(world.waterworks),
        float(world.sanitation),
        float(world.garden),
        float(world.food_storage),
        float(world.trust),
        float(world.conflict),
        float(world.social_inequality),
        float(world.reputation_accuracy),
        float(world.symbol_convergence),
        float(world.teaching),
        float(world.knowledge_transfer),
        float(signals["water"]),
        float(signals["weather"]),
        float(signals["food"]),
        float(signals["tool"]),
        float(signals["social"]),
        float(world.risk_memory),
        float(world.culture_memory),
        float(world.contamination),
        float(world.sickness),
        float(world.route_hazard),
        math.sin(day * math.tau),
        math.cos(day * math.tau),
    ]
    return values + one_hot(previous_action, len(ACTIONS))


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


def teacher_condition():
    return h.CONDITIONS[0]


def reactive_condition():
    return h.CONDITIONS[1]


def generate_teacher_sequences(cfg: Config) -> Tuple[torch.Tensor, torch.Tensor]:
    xs: List[List[List[float]]] = []
    ys: List[List[int]] = []
    for seed in cfg.train_seeds:
        seed_xs: List[List[List[float]]] = [[] for _ in range(cfg.population)]
        seed_ys: List[List[int]] = [[] for _ in range(cfg.population)]
        rng = random.Random(seed * 181 + 7)
        agents = h.make_agents(rng, cfg.population)
        world = h.make_world(seed, rng)
        condition = teacher_condition()
        h.current_agents = agents
        previous_actions = [ACTION_TO_INDEX["rest"] for _ in range(cfg.population)]
        while world.time < cfg.hours - 1e-9:
            dt = min(cfg.step_hours, cfg.hours - world.time)
            world.time += dt
            h.apply_baseline_environment(world, agents, condition, dt, rng)
            h.apply_hidden_regime(world, condition, dt)
            signals = sensor_features(world, condition, rng)
            h.update_beliefs(world, condition, signals, dt)
            pressure = h.pressure_score(world, agents)
            world.pressure_integral = clamp(world.pressure_integral + pressure * dt / max(cfg.hours, 1.0))
            h.update_agent_influence(agents, condition.reputation_influence)
            for index, agent in enumerate(agents[: cfg.population]):
                if not agent.alive or agent.child:
                    seed_xs[index].append(observation(agent, world, signals, previous_actions[index]))
                    seed_ys[index].append(ACTION_TO_INDEX["rest"])
                    continue
                action = h.choose_action(agent, world, condition, rng)
                action_index = ACTION_TO_INDEX[action]
                seed_xs[index].append(observation(agent, world, signals, previous_actions[index]))
                seed_ys[index].append(action_index)
                h.apply_action(agent, world, condition, action, dt, rng)
                previous_actions[index] = action_index
            apply_body_dynamics(world, agents, dt)
            h.maybe_reproduce(world, agents, condition, rng, dt)
        xs.extend(seed_xs)
        ys.extend(seed_ys)
    return torch.tensor(xs, dtype=torch.float32), torch.tensor(ys, dtype=torch.long)


def apply_body_dynamics(world, agents: List[object], dt: float) -> None:
    for agent in h.living(agents):
        food_support = world.food * 0.015 + world.food_storage * 0.008
        water_support = world.water * 0.017 + world.waterworks * 0.009
        agent.hunger = h.clamp(agent.hunger + (0.019 + world.weather_exposure * 0.006 + agent.stress * 0.004) * dt - food_support * dt)
        agent.thirst = h.clamp(agent.thirst + (0.022 + world.weather_exposure * 0.008 + agent.stress * 0.004) * dt - water_support * dt)
        agent.cleanliness = h.clamp(agent.cleanliness + world.sanitation * 0.018 * dt - world.contamination * 0.020 * dt - agent.stress * 0.004 * dt)
        illness = world.sickness * 0.036 + world.contamination * 0.020 + world.weather_exposure * 0.010
        scarcity = max(0.0, agent.hunger - 0.88) * 0.48 + max(0.0, agent.thirst - 0.88) * 0.62
        agent.health = h.clamp(agent.health - (illness + scarcity) * dt + world.clinic * 0.010 * dt)
        reserve_cost = 0.0012 * (1.0 + agent.stress * 0.44 + world.hidden_pressure * 0.30 + scarcity - agent.wisdom * 0.12)
        agent.reserve = h.clamp(agent.reserve - reserve_cost * dt)
        if agent.health <= 0.04 or agent.reserve <= 0.02:
            agent.alive = False
            world.deaths += 1


def standardize(train_x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    flat = train_x.reshape(-1, train_x.shape[-1])
    feature_mean = flat.mean(dim=0)
    feature_std = flat.std(dim=0).clamp_min(1e-5)
    return (train_x - feature_mean) / feature_std, feature_mean, feature_std


def train_controller(
    architecture: str,
    train_x: torch.Tensor,
    train_y: torch.Tensor,
    cfg: Config,
    device: torch.device,
) -> Tuple[ControllerNet, TrainingRow]:
    torch.manual_seed(20260720 + len(architecture) * 31)
    model = ControllerNet(architecture, FEATURE_COUNT, cfg.hidden_size, len(ACTIONS)).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.learning_rate)
    counts = torch.bincount(train_y.reshape(-1), minlength=len(ACTIONS)).float()
    weights = counts.sum() / counts.clamp_min(1.0)
    weights = (weights / weights.mean()).to(device)
    loss_fn = nn.CrossEntropyLoss(weight=weights)
    x = train_x.to(device)
    y = train_y.to(device)
    last_loss = 0.0
    for _ in range(cfg.epochs):
        optimizer.zero_grad(set_to_none=True)
        logits, _ = model(x)
        loss = loss_fn(logits.reshape(-1, logits.shape[-1]), y.reshape(-1))
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 2.0)
        optimizer.step()
        last_loss = float(loss.detach().cpu().item())
    model.eval()
    with torch.no_grad():
        logits, _ = model(x)
        accuracy = float((logits.argmax(dim=-1) == y).float().mean().detach().cpu().item())
    return model, TrainingRow(
        architecture=architecture,
        train_loss=last_loss,
        train_accuracy=accuracy,
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in model.parameters()),
    )


def choose_model_action(
    model: ControllerNet,
    device: torch.device,
    feature_mean: torch.Tensor,
    feature_std: torch.Tensor,
    agent,
    world,
    signals: Dict[str, float],
    previous_action: int,
    state: torch.Tensor | None,
    ablation: str,
) -> Tuple[str, int, torch.Tensor | None]:
    raw = apply_feature_ablation(observation(agent, world, signals, previous_action), ablation)
    x = torch.tensor(raw, dtype=torch.float32).unsqueeze(0)
    x = (x - feature_mean) / feature_std
    x = x.to(device)
    with torch.no_grad():
        logits, next_state = model.step(x, state)
    action_index = int(logits.argmax(dim=-1).item())
    return INDEX_TO_ACTION[action_index], action_index, next_state


def score_episode(seed: int, architecture: str, condition_name: str, world, agents, baseline: Dict[str, float], alive_at_12h: int | None) -> EvalRow:
    final_alive = len(h.living(agents))
    total_agents = len(agents)
    survival_score = final_alive / max(1, total_agents)
    architecture_delta = world.architecture - baseline["architecture"]
    tool_delta = world.tool_design - baseline["tool_design"]
    teaching_delta = world.teaching - baseline["teaching"]
    sanitation_delta = world.sanitation - baseline["sanitation"]
    development_score = clamp(
        max(0.0, architecture_delta) * 0.34
        + max(0.0, tool_delta) * 0.30
        + max(0.0, sanitation_delta) * 0.24
        + max(0.0, world.path_network - 0.14) * 0.14
        + max(0.0, world.food_storage - 0.18) * 0.12
    )
    culture_score = clamp(world.knowledge_transfer * 0.46 + max(0.0, teaching_delta) * 0.32 + world.symbol_convergence * 0.18 + world.reputation_accuracy * 0.14)
    response = h.regime_response_score(world)
    inference = h.inference_score(world)
    targeted_rate = world.targeted_action_count / max(1, world.post_regime_action_count)
    long_horizon_score = clamp(
        survival_score * 0.24
        + development_score * 0.18
        + culture_score * 0.16
        + response * 0.24
        + inference * 0.10
        + targeted_rate * 0.08
    )
    return EvalRow(
        seed=seed,
        regime=world.regime_name,
        architecture=architecture,
        condition=condition_name,
        final_alive=final_alive,
        total_agents=total_agents,
        alive_at_12h=alive_at_12h if alive_at_12h is not None else final_alive,
        hidden_regime_after_12h=world.first_regime_hour >= 12.0 and h.regime_active(world),
        no_major_regime_before_12h=True,
        final_food=world.food,
        final_water=world.water,
        final_trust=world.trust,
        architecture_delta=architecture_delta,
        tool_design_delta=tool_delta,
        teaching_delta=teaching_delta,
        knowledge_transfer=world.knowledge_transfer,
        symbol_convergence=world.symbol_convergence,
        inference_score=inference,
        response_score=response,
        targeted_response_rate=targeted_rate,
        survival_score=survival_score,
        development_score=development_score,
        culture_score=culture_score,
        long_horizon_score=long_horizon_score,
    )


def trace_snapshot(world, agents, label: str) -> Dict[str, object]:
    alive = h.living(agents)
    return {
        "label": label,
        "hours": world.time,
        "regime": world.regime_name,
        "regime_active": h.regime_active(world),
        "alive": len(alive),
        "total_agents": len(agents),
        "food": world.food,
        "water": world.water,
        "architecture": world.architecture,
        "tool_design": world.tool_design,
        "sanitation": world.sanitation,
        "trust": world.trust,
        "teaching": world.teaching,
        "knowledge_transfer": world.knowledge_transfer,
        "symbol_convergence": world.symbol_convergence,
        "dominant_belief": h.dominant_belief(world),
        "inference_score": h.inference_score(world),
        "response_score": h.regime_response_score(world),
        "targeted_response_rate": world.targeted_action_count / max(1, world.post_regime_action_count),
        "mean_wisdom": mean(agent.wisdom for agent in alive),
        "mean_adaptation": mean(agent.adaptation for agent in alive),
    }


def run_model_episode(
    seed: int,
    architecture: str,
    model: ControllerNet,
    device: torch.device,
    feature_mean: torch.Tensor,
    feature_std: torch.Tensor,
    cfg: Config,
    *,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[EvalRow, List[Dict[str, object]]]:
    rng = random.Random(seed * 211 + 23 + sum(ord(ch) for ch in architecture + ablation))
    agents = h.make_agents(rng, cfg.population)
    world = h.make_world(seed, rng)
    condition = teacher_condition()
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

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        world.time += dt
        h.apply_baseline_environment(world, agents, condition, dt, rng)
        h.apply_hidden_regime(world, condition, dt)
        signals = sensor_features(world, condition, rng)
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
            action, action_index, next_state = choose_model_action(
                model,
                device,
                feature_mean,
                feature_std,
                agent,
                world,
                signals,
                previous_actions[index],
                states.get(index),
                ablation,
            )
            states[index] = next_state
            h.apply_action(agent, world, condition, action, dt, rng)
            previous_actions[index] = action_index
        apply_body_dynamics(world, agents, dt)
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
                snapshots.append(trace_snapshot(world, agents, f"{checkpoints[0]:.1f}h"))
            checkpoints.pop(0)

    row = score_episode(seed, architecture, ablation, world, agents, baseline, alive_at_12h)
    row = EvalRow(**{**asdict(row), "no_major_regime_before_12h": no_major_before_12})
    return row, snapshots


def run_scripted_episode(seed: int, cfg: Config, condition, architecture: str, name: str) -> EvalRow:
    row, _ = h.run_episode(seed, condition, h.Config(seeds=(seed,), hours=cfg.hours, step_hours=cfg.step_hours, population=cfg.population, trace_seed=seed))
    return EvalRow(
        seed=seed,
        regime=row.regime,
        architecture=architecture,
        condition=name,
        final_alive=row.final_alive,
        total_agents=row.total_agents,
        alive_at_12h=row.alive_at_12h,
        hidden_regime_after_12h=row.hidden_regime_after_12h,
        no_major_regime_before_12h=row.no_major_regime_before_12h,
        final_food=row.final_food,
        final_water=row.final_water,
        final_trust=row.final_trust,
        architecture_delta=row.architecture_delta,
        tool_design_delta=row.tool_design_delta,
        teaching_delta=row.teaching_delta,
        knowledge_transfer=row.knowledge_transfer,
        symbol_convergence=row.final_symbol_convergence,
        inference_score=row.inference_score,
        response_score=row.response_score,
        targeted_response_rate=row.targeted_response_rate,
        survival_score=row.survival_score,
        development_score=row.development_score,
        culture_score=row.culture_score,
        long_horizon_score=row.long_horizon_score,
    )


def summarize(rows: Sequence[EvalRow]) -> List[SummaryRow]:
    grouped: Dict[Tuple[str, str], List[EvalRow]] = {}
    for row in rows:
        grouped.setdefault((row.architecture, row.condition), []).append(row)
    summary: List[SummaryRow] = []
    for (architecture, condition), items in sorted(grouped.items()):
        summary.append(
            SummaryRow(
                architecture=architecture,
                condition=condition,
                mean_long_horizon_score=mean(row.long_horizon_score for row in items),
                mean_survival_score=mean(row.survival_score for row in items),
                mean_development_score=mean(row.development_score for row in items),
                mean_culture_score=mean(row.culture_score for row in items),
                mean_inference_score=mean(row.inference_score for row in items),
                mean_response_score=mean(row.response_score for row in items),
                mean_targeted_response_rate=mean(row.targeted_response_rate for row in items),
                mean_final_alive=mean(row.final_alive for row in items),
                mean_alive_at_12h=mean(row.alive_at_12h for row in items),
                mean_architecture_delta=mean(row.architecture_delta for row in items),
                mean_tool_design_delta=mean(row.tool_design_delta for row in items),
                mean_knowledge_transfer=mean(row.knowledge_transfer for row in items),
                mean_symbol_convergence=mean(row.symbol_convergence for row in items),
                no_major_regime_before_12h_rate=mean(1.0 if row.no_major_regime_before_12h else 0.0 for row in items),
                hidden_regime_after_12h_rate=mean(1.0 if row.hidden_regime_after_12h else 0.0 for row in items),
            )
        )
    return summary


def row_lookup(summary: Sequence[SummaryRow], architecture: str, condition: str) -> SummaryRow:
    for row in summary:
        if row.architecture == architecture and row.condition == condition:
            return row
    raise KeyError((architecture, condition))


def make_ablations(summary: Sequence[SummaryRow]) -> List[AblationRow]:
    full = row_lookup(summary, "gru", "none")
    rows: List[AblationRow] = []
    for ablation in ("symptoms", "memory", "social_culture", "infrastructure", "body"):
        row = row_lookup(summary, "gru", ablation)
        rows.append(
            AblationRow(
                architecture="gru",
                ablation=ablation,
                mean_score=row.mean_long_horizon_score,
                score_loss=full.mean_long_horizon_score - row.mean_long_horizon_score,
                mean_response_score=row.mean_response_score,
                response_loss=full.mean_response_score - row.mean_response_score,
                mean_inference_score=row.mean_inference_score,
                inference_loss=full.mean_inference_score - row.mean_inference_score,
            )
        )
    return rows


def verdict_from_summary(summary: Sequence[SummaryRow], ablations: Sequence[AblationRow]) -> VerdictRow:
    recurrent = row_lookup(summary, "gru", "none")
    frame = row_lookup(summary, "frame_mlp", "none")
    reactive = row_lookup(summary, "scripted", "reactive_survival_only")
    by_ablation = {row.ablation: row for row in ablations}
    supports_learning = (
        recurrent.no_major_regime_before_12h_rate == 1.0
        and recurrent.hidden_regime_after_12h_rate == 1.0
        and recurrent.mean_alive_at_12h >= 8.0
        and recurrent.mean_final_alive >= 7.0
        and recurrent.mean_long_horizon_score >= 0.58
        and recurrent.mean_response_score >= 0.52
        and recurrent.mean_development_score >= 0.24
        and recurrent.mean_culture_score >= 0.20
        and recurrent.mean_long_horizon_score - reactive.mean_long_horizon_score >= 0.12
    )
    supports_ablation = (
        by_ablation["symptoms"].inference_loss >= 0.015
        and by_ablation["memory"].score_loss >= 0.010
        and by_ablation["social_culture"].score_loss >= 0.010
        and by_ablation["infrastructure"].score_loss >= 0.010
    )
    if supports_learning and supports_ablation:
        verdict = "pass"
    elif supports_learning:
        verdict = "partial"
    else:
        verdict = "failed"
    return VerdictRow(
        recurrent_score=recurrent.mean_long_horizon_score,
        frame_score=frame.mean_long_horizon_score,
        reactive_score=reactive.mean_long_horizon_score,
        recurrent_gain_over_frame=recurrent.mean_long_horizon_score - frame.mean_long_horizon_score,
        recurrent_gain_over_reactive=recurrent.mean_long_horizon_score - reactive.mean_long_horizon_score,
        symptom_ablation_loss=by_ablation["symptoms"].score_loss,
        memory_ablation_loss=by_ablation["memory"].score_loss,
        social_culture_ablation_loss=by_ablation["social_culture"].score_loss,
        infrastructure_ablation_loss=by_ablation["infrastructure"].score_loss,
        recurrent_inference_score=recurrent.mean_inference_score,
        recurrent_response_score=recurrent.mean_response_score,
        recurrent_targeted_response_rate=recurrent.mean_targeted_response_rate,
        shock_gate_pass_rate=recurrent.no_major_regime_before_12h_rate,
        hidden_regime_rate=recurrent.hidden_regime_after_12h_rate,
        supports_closed_loop_learning_precursor=supports_learning,
        supports_ablation_specificity=supports_ablation,
        verdict=verdict,
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


def run_benchmark(cfg: Config) -> Dict[str, object]:
    device = resolve_device(cfg.device)
    train_x_raw, train_y = generate_teacher_sequences(cfg)
    train_x, feature_mean, feature_std = standardize(train_x_raw)
    training_rows: List[TrainingRow] = []
    models: Dict[str, ControllerNet] = {}
    for architecture in ("frame_mlp", "gru"):
        model, training_row = train_controller(architecture, train_x, train_y, cfg, device)
        models[architecture] = model
        training_rows.append(training_row)

    eval_rows: List[EvalRow] = []
    trace: List[Dict[str, object]] = []
    for seed in cfg.eval_seeds:
        eval_rows.append(run_scripted_episode(seed, cfg, reactive_condition(), "scripted", "reactive_survival_only"))
        for architecture, model in models.items():
            row, maybe_trace = run_model_episode(
                seed,
                architecture,
                model,
                device,
                feature_mean,
                feature_std,
                cfg,
                ablation="none",
                trace=(seed == cfg.trace_seed and architecture == "gru"),
            )
            eval_rows.append(row)
            if maybe_trace:
                trace = maybe_trace
        for ablation in ("symptoms", "memory", "social_culture", "infrastructure", "body"):
            row, _ = run_model_episode(seed, "gru", models["gru"], device, feature_mean, feature_std, cfg, ablation=ablation)
            eval_rows.append(row)

    summary = summarize(eval_rows)
    ablations = make_ablations(summary)
    verdict = verdict_from_summary(summary, ablations)
    payload = {
        "config": {
            "train_seeds": list(cfg.train_seeds),
            "eval_seeds": list(cfg.eval_seeds),
            "hours": cfg.hours,
            "step_hours": cfg.step_hours,
            "population": cfg.population,
            "epochs": cfg.epochs,
            "hidden_size": cfg.hidden_size,
            "learning_rate": cfg.learning_rate,
            "device": str(device),
            "trace_seed": cfg.trace_seed,
        },
        "actions": list(ACTIONS),
        "feature_groups": {key: list(value) for key, value in FEATURE_GROUPS.items()},
        "training": [asdict(row) for row in training_rows],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": trace,
        "notes": {
            "claim": "closed-loop imitation-trained recurrent hidden-regime controller precursor",
            "not_claimed": "subjective consciousness, open-ended civilization, or return-trained deep RL",
            "label_discipline": "model observations contain symptoms and state, not hidden regime labels",
        },
    }
    prefix = ARTIFACT_DIR / "ssrm_3d_learned_hidden_regime_controller"
    rows_to_csv(Path(f"{prefix}_training.csv"), training_rows)
    rows_to_csv(Path(f"{prefix}_eval.csv"), eval_rows)
    rows_to_csv(Path(f"{prefix}_summary.csv"), summary)
    rows_to_csv(Path(f"{prefix}_ablations.csv"), ablations)
    rows_to_csv(Path(f"{prefix}_verdict.csv"), [verdict])
    write_json(Path(f"{prefix}_results.json"), payload)
    write_json(Path(f"{prefix}_trace.json"), trace)
    write_js(Path(f"{prefix}_results.js"), "SSRM_3D_LEARNED_HIDDEN_REGIME_CONTROLLER_RESULTS", payload)
    write_js(Path(f"{prefix}_trace.js"), "SSRM_3D_LEARNED_HIDDEN_REGIME_CONTROLLER_TRACE", trace)
    return payload


def parse_seed_list(raw: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in raw.split(",") if part.strip())


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-seeds", default="20260718,20260719,20260720,20260721,20260722,20260723,20260724,20260725")
    parser.add_argument("--eval-seeds", default="20260783,20260784,20260785,20260786,20260787")
    parser.add_argument("--hours", type=float, default=16.0)
    parser.add_argument("--step-hours", type=float, default=0.08)
    parser.add_argument("--population", type=int, default=10)
    parser.add_argument("--epochs", type=int, default=80)
    parser.add_argument("--hidden-size", type=int, default=48)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--trace-seed", type=int, default=20260783)
    args = parser.parse_args()
    return Config(
        train_seeds=parse_seed_list(args.train_seeds),
        eval_seeds=parse_seed_list(args.eval_seeds),
        hours=args.hours,
        step_hours=args.step_hours,
        population=args.population,
        epochs=args.epochs,
        hidden_size=args.hidden_size,
        learning_rate=args.learning_rate,
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({"training": payload["training"], "verdict": payload["verdict"], "summary": payload["summary"]}, indent=2))
    return 0 if payload["verdict"]["verdict"] in {"pass", "partial"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
