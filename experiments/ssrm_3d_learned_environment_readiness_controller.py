#!/usr/bin/env python3
"""Learned controller for the SSRM-3D environment-readiness world.

Report 135 made the richer readiness world measurable, but the action policy
was still designed. This experiment trains frame and recurrent neural action
controllers from the designed readiness traces, then evaluates them closed-loop
in held-out 72h worlds.

This is supervised imitation plus closed-loop evaluation, not deep RL. A failed
strong verdict is still a valid completed result and exits cleanly.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import torch
from torch import nn

import ssrm_3d_environment_readiness_maturation as base


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"

ACTIONS = (
    "harvest_food",
    "collect_water",
    "gather_fuel",
    "construct",
    "improve_tools",
    "control_pests",
    "repair_strain",
    "sanitize",
    "treat",
    "scout",
    "teach",
    "social_repair",
    "learn",
    "rest",
    "stay_near_shelter",
)
ACTION_TO_INDEX = {name: index for index, name in enumerate(ACTIONS)}
INDEX_TO_ACTION = {index: name for name, index in ACTION_TO_INDEX.items()}
DEFAULT_ACTION = ACTION_TO_INDEX["rest"]

FEATURE_NAMES: List[str] = []
FEATURE_GROUPS: Dict[str, Tuple[int, ...]] = {}


def register(group: str, names: Sequence[str]) -> None:
    start = len(FEATURE_NAMES)
    FEATURE_NAMES.extend(names)
    FEATURE_GROUPS[group] = tuple(range(start, len(FEATURE_NAMES)))


register(
    "body",
    (
        "generation",
        "child",
        "age_fraction",
        "health",
        "energy",
        "hunger",
        "thirst",
        "stress",
        "illness",
        "injury",
        "wisdom",
        "build_skill",
        "tool_skill",
        "harvest_skill",
        "scout_skill",
        "care_skill",
        "teach_skill",
        "resilience",
        "dexterity",
        "sociability",
        "curiosity",
    ),
)
register("time", ("hour_norm", "day_sin", "day_cos", "post_gate", "major_shocks"))
register("resources", ("food", "water", "materials", "medicine"))
register(
    "infrastructure",
    ("shelter", "architecture", "waterworks", "granary", "paths", "garden", "sanitation", "fire_control"),
)
register("tools", ("tools", "workshop"))
register(
    "social_culture",
    ("social_trust", "conflict", "culture", "symbols", "risk_memory", "knowledge_transfer", "births", "population"),
)
register(
    "environment",
    (
        "soil",
        "contamination",
        "temperature",
        "rainfall",
        "wind",
        "visibility",
        "route_hazard",
        "disease",
        "resource_migration",
        "resource_depletion",
        "adaptive_pressure",
        "pressure_integral",
        "map_knowledge",
        "terrain_knowledge",
    ),
)
register(
    "readiness",
    (
        "fuel_reserve",
        "seed_bank",
        "building_blueprints",
        "tool_blueprints",
        "forecast_memory",
        "apprenticeship",
        "pest_pressure",
        "structural_strain",
    ),
)
register("previous_action", tuple(f"previous_{name}" for name in ACTIONS))
FEATURE_COUNT = len(FEATURE_NAMES)


@dataclass(frozen=True)
class Config:
    train_seeds: Sequence[int]
    eval_seeds: Sequence[int]
    hours: float = 72.0
    step_hours: float = 0.10
    population: int = 14
    epochs: int = 52
    hidden_size: int = 72
    learning_rate: float = 0.0035
    device: str = "auto"
    trace_seed: int = 20261221


@dataclass(frozen=True)
class TrainingRow:
    architecture: str
    train_loss: float
    train_accuracy: float
    device_used: str
    parameter_count: int
    train_sequences: int
    train_steps: int


@dataclass(frozen=True)
class EvalRow:
    seed: int
    controller: str
    ablation: str
    final_alive: int
    total_agents: int
    alive_at_12h: int
    no_major_shock_before_12h: bool
    post_gate_shock: bool
    major_shocks: int
    first_shock_hour: float
    births: int
    deaths: int
    readiness_at_12h: float
    final_readiness: float
    readiness_delta: float
    final_pest_pressure: float
    final_structural_strain: float
    final_fuel_reserve: float
    final_seed_bank: float
    final_building_blueprints: float
    final_tool_blueprints: float
    final_forecast_memory: float
    final_apprenticeship: float
    architecture_delta: float
    tool_system_delta: float
    knowledge_transfer: float
    adaptation_evidence: float
    pressure_integral: float
    survival_score: float
    readiness_score: float
    development_score: float
    knowledge_score: float
    resilience_score: float
    maturation_score: float


@dataclass(frozen=True)
class SummaryRow:
    controller: str
    ablation: str
    mean_maturation_score: float
    mean_survival_score: float
    mean_readiness_score: float
    mean_development_score: float
    mean_knowledge_score: float
    mean_resilience_score: float
    mean_final_alive: float
    mean_alive_at_12h: float
    mean_births: float
    mean_deaths: float
    mean_readiness_at_12h: float
    mean_final_readiness: float
    mean_readiness_delta: float
    mean_final_pest_pressure: float
    mean_final_structural_strain: float
    mean_architecture_delta: float
    mean_tool_system_delta: float
    mean_knowledge_transfer: float
    mean_adaptation_evidence: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float


@dataclass(frozen=True)
class AblationRow:
    controller: str
    ablation: str
    mean_score: float
    score_loss: float
    mean_readiness_score: float
    readiness_loss: float
    mean_development_score: float
    development_loss: float
    mean_knowledge_score: float
    knowledge_loss: float
    mean_resilience_score: float
    resilience_loss: float
    pest_pressure_delta: float
    structural_strain_delta: float


@dataclass(frozen=True)
class VerdictRow:
    gru_score: float
    frame_score: float
    designed_score: float
    reactive_score: float
    gru_gain_over_reactive: float
    gru_gap_to_designed: float
    gru_gain_over_frame: float
    body_ablation_loss: float
    infrastructure_ablation_loss: float
    tools_ablation_loss: float
    social_culture_ablation_loss: float
    environment_ablation_loss: float
    readiness_ablation_loss: float
    previous_action_ablation_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    readiness_at_12h: float
    final_readiness: float
    final_pest_pressure: float
    final_structural_strain: float
    supports_learned_readiness_control: bool
    supports_recurrent_advantage: bool
    supports_ablation_specificity: bool
    verdict: str


class ControllerNet(nn.Module):
    def __init__(self, architecture: str, input_size: int, hidden_size: int, output_size: int) -> None:
        super().__init__()
        self.architecture = architecture
        if architecture == "frame_mlp":
            self.encoder = nn.Sequential(
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

    def forward(self, x: torch.Tensor, state: Optional[torch.Tensor] = None) -> Tuple[torch.Tensor, Optional[torch.Tensor]]:
        if self.architecture == "frame_mlp":
            return self.head(self.encoder(x)), None
        out, next_state = self.recurrent(x, state)
        return self.head(out), next_state

    def step(self, x: torch.Tensor, state: Optional[torch.Tensor] = None) -> Tuple[torch.Tensor, Optional[torch.Tensor]]:
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


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def one_hot(index: int, size: int) -> List[float]:
    return [1.0 if index == item else 0.0 for item in range(size)]


def observation(agent: base.Agent, world: base.World, previous_action: int, population: int) -> List[float]:
    day = (world.time % 24.0) / 24.0
    values = [
        min(1.0, agent.generation / 4.0),
        1.0 if agent.child else 0.0,
        base.clamp(agent.age_hours / max(1.0, agent.max_life_hours)),
        agent.health,
        agent.energy,
        agent.hunger,
        agent.thirst,
        agent.stress,
        agent.illness,
        agent.injury,
        agent.wisdom,
        agent.build_skill,
        agent.tool_skill,
        agent.harvest_skill,
        agent.scout_skill,
        agent.care_skill,
        agent.teach_skill,
        agent.resilience,
        agent.dexterity,
        agent.sociability,
        agent.curiosity,
        base.clamp(world.time / 72.0),
        math.sin(day * math.pi * 2.0) * 0.5 + 0.5,
        math.cos(day * math.pi * 2.0) * 0.5 + 0.5,
        1.0 if world.time >= 12.0 else 0.0,
        base.clamp(world.major_shocks / 6.0),
        world.food,
        world.water,
        world.materials,
        world.medicine,
        world.shelter,
        world.architecture,
        world.waterworks,
        world.granary,
        world.paths,
        world.garden,
        world.sanitation,
        world.fire_control,
        world.tools,
        world.workshop,
        world.social_trust,
        world.conflict,
        world.culture,
        world.symbols,
        world.risk_memory,
        world.knowledge_transfer,
        base.clamp(world.births / 12.0),
        base.clamp(population / 30.0),
        world.soil,
        world.contamination,
        world.temperature,
        world.rainfall,
        world.wind,
        world.visibility,
        world.route_hazard,
        world.disease,
        world.resource_migration,
        world.resource_depletion,
        world.adaptive_pressure,
        world.pressure_integral,
        world.map_knowledge,
        world.terrain_knowledge,
        world.fuel_reserve,
        world.seed_bank,
        world.building_blueprints,
        world.tool_blueprints,
        world.forecast_memory,
        world.apprenticeship,
        world.pest_pressure,
        world.structural_strain,
        *one_hot(previous_action, len(ACTIONS)),
    ]
    if len(values) != FEATURE_COUNT:
        raise RuntimeError(f"feature count mismatch: {len(values)} != {FEATURE_COUNT}")
    return values


def mask_features(features: List[float], ablation: str) -> List[float]:
    if ablation == "none":
        return features
    masked = list(features)
    for index in FEATURE_GROUPS[ablation]:
        masked[index] = 0.0
    return masked


def initial_baseline(world: base.World, population: int) -> Dict[str, float]:
    return {
        "architecture": world.architecture,
        "tool_system": base.tool_system(world),
        "shelter": world.shelter,
        "granary": world.granary,
        "paths": world.paths,
        "readiness": base.environment_readiness(world),
        "population": float(population),
    }


def update_body_states(world: base.World, agents: List[base.Agent], dt: float) -> None:
    for agent in base.living(agents):
        age_pressure = max(0.0, agent.age_hours - agent.max_life_hours * 0.74) / max(1.0, agent.max_life_hours * 0.26)
        exposure_buffer = base.clamp(world.shelter * 0.34 + world.architecture * 0.16 + world.fuel_reserve * 0.18)
        thermal = max(0.0, abs(world.temperature - 0.55) - exposure_buffer * 0.20) * 0.018
        shelter_protection = world.shelter * 0.014 + world.architecture * 0.006 + world.fuel_reserve * 0.004
        agent.hunger = base.clamp(agent.hunger + (0.011 + thermal + agent.stress * 0.003) * dt - (world.food + world.granary * 0.30 + world.seed_bank * 0.12) * 0.010 * dt)
        agent.thirst = base.clamp(agent.thirst + (0.013 + max(0.0, world.temperature - 0.62) * 0.018 + agent.stress * 0.003) * dt - (world.water + world.waterworks * 0.26) * 0.012 * dt)
        agent.illness = base.clamp(agent.illness + (world.disease * 0.022 + world.contamination * 0.015 + world.pest_pressure * 0.010 - world.sanitation * 0.014) * dt)
        agent.injury = base.clamp(agent.injury - (world.medicine + world.shelter) * 0.008 * dt)
        quality_penalty = world.pest_pressure * 0.020 + world.structural_strain * 0.018 + max(0.0, 0.34 - world.fuel_reserve) * 0.018
        health_loss = (
            max(0.0, agent.hunger - 0.88) * 0.22
            + max(0.0, agent.thirst - 0.88) * 0.28
            + agent.illness * 0.030
            + agent.injury * 0.018
            + age_pressure * 0.014
            + quality_penalty
        )
        agent.health = base.clamp(agent.health - max(0.0, health_loss - shelter_protection) * dt)
        agent.energy = base.clamp(agent.energy - (0.004 + age_pressure * 0.010 - world.shelter * 0.003) * dt)
        if agent.health <= 0.03 or agent.thirst >= 0.995 or agent.age_hours > agent.max_life_hours:
            agent.alive = False
            world.deaths += 1


def step_world(
    world: base.World,
    agents: List[base.Agent],
    condition: base.Condition,
    dt: float,
    rng: random.Random,
    previous_actions: Dict[str, int],
    action_selector,
    events: List[str],
    recorder=None,
) -> None:
    world.time += dt
    base.update_environment(world, agents, condition, dt, rng)
    shock = base.maybe_major_shock(world, condition, rng)
    if shock:
        events.append(f"{world.time:.1f}h: {shock.replace('_', ' ')} shock")
    pressure = base.pressure_components(world, agents)
    alpha = min(0.10, max(0.004, dt / 1.5))
    world.adaptive_pressure = base.clamp(world.adaptive_pressure * (1.0 - alpha) + pressure["total"] * alpha)
    world.pressure_integral = base.clamp(world.pressure_integral + pressure["total"] * dt / 72.0)

    for agent in base.living(agents):
        agent.age_hours += dt
        previous = previous_actions.get(agent.ident, DEFAULT_ACTION)
        features = observation(agent, world, previous, len(agents))
        action = action_selector(agent, world, condition, rng, features, previous)
        action_index = ACTION_TO_INDEX.get(action, DEFAULT_ACTION)
        if recorder:
            recorder(agent.ident, features, action_index)
        previous_actions[agent.ident] = action_index
        base.apply_action(agent, world, agents, condition, INDEX_TO_ACTION[action_index], dt, rng)

    update_body_states(world, agents, dt)
    base.mature_children(agents)
    before_births = world.births
    base.maybe_reproduce(world, agents, condition, rng, dt)
    if world.births > before_births:
        events.append(f"{world.time:.1f}h: new generation born")


def collect_sequences(cfg: Config) -> Tuple[List[List[List[float]]], List[List[int]]]:
    condition = base.CONDITIONS[0]
    sequences: Dict[str, List[List[float]]] = {}
    labels: Dict[str, List[int]] = {}
    for seed in cfg.train_seeds:
        rng = random.Random(seed * 131 + 37)
        agents = base.make_agents(rng, cfg.population)
        world = base.make_world(rng)
        previous_actions: Dict[str, int] = {}
        events: List[str] = []

        def selector(agent: base.Agent, current_world: base.World, current_condition: base.Condition, current_rng: random.Random, features: List[float], previous: int) -> str:
            return base.choose_action(agent, current_world, current_condition, current_rng)

        def recorder(ident: str, features: List[float], label: int) -> None:
            key = f"{seed}:{ident}"
            sequences.setdefault(key, []).append(features)
            labels.setdefault(key, []).append(label)

        while world.time < cfg.hours - 1e-9:
            dt = min(cfg.step_hours, cfg.hours - world.time)
            step_world(world, agents, condition, dt, rng, previous_actions, selector, events, recorder=recorder)

    keys = sorted(sequences)
    return [sequences[key] for key in keys], [labels[key] for key in keys]


def build_tensors(sequences: List[List[List[float]]], labels: List[List[int]], device: torch.device) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    max_len = max(len(seq) for seq in sequences)
    x = torch.zeros((len(sequences), max_len, FEATURE_COUNT), dtype=torch.float32)
    y = torch.full((len(sequences), max_len), -100, dtype=torch.long)
    mask = torch.zeros((len(sequences), max_len), dtype=torch.bool)
    for row, seq in enumerate(sequences):
        seq_len = len(seq)
        x[row, :seq_len, :] = torch.tensor(seq, dtype=torch.float32)
        y[row, :seq_len] = torch.tensor(labels[row], dtype=torch.long)
        mask[row, :seq_len] = True
    return x.to(device), y.to(device), mask.to(device)


def train_model(architecture: str, x: torch.Tensor, y: torch.Tensor, mask: torch.Tensor, cfg: Config, device: torch.device) -> Tuple[ControllerNet, TrainingRow]:
    torch.manual_seed(20261231 + (0 if architecture == "frame_mlp" else 17))
    model = ControllerNet(architecture, FEATURE_COUNT, cfg.hidden_size, len(ACTIONS)).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.learning_rate)
    loss_fn = nn.CrossEntropyLoss(ignore_index=-100)
    for _ in range(cfg.epochs):
        model.train()
        optimizer.zero_grad()
        logits, _ = model(x)
        loss = loss_fn(logits.reshape(-1, len(ACTIONS)), y.reshape(-1))
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 2.0)
        optimizer.step()
    model.eval()
    with torch.no_grad():
        logits, _ = model(x)
        loss = loss_fn(logits.reshape(-1, len(ACTIONS)), y.reshape(-1)).item()
        predictions = logits.argmax(dim=-1)
        accuracy = ((predictions == y) & mask).sum().item() / max(1, mask.sum().item())
    return model, TrainingRow(
        architecture=architecture,
        train_loss=loss,
        train_accuracy=accuracy,
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in model.parameters()),
        train_sequences=x.shape[0],
        train_steps=int(mask.sum().item()),
    )


def run_controller_episode(
    seed: int,
    cfg: Config,
    controller: str,
    model: Optional[ControllerNet],
    device: torch.device,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[EvalRow, base.Trace]:
    condition = base.CONDITIONS[1] if controller == "reactive" else base.CONDITIONS[0]
    rng = random.Random(seed * 131 + sum(ord(ch) for ch in controller + ablation))
    agents = base.make_agents(rng, cfg.population)
    world = base.make_world(rng)
    baseline = initial_baseline(world, cfg.population)
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    trace_out = base.Trace(seed=seed, condition=f"{controller}:{ablation}")
    checkpoints = list(base.TRACE_CHECKPOINTS)
    no_pre_gate_shock = True
    alive_at_12h = cfg.population
    at_12: Dict[str, float] = {}
    if trace:
        trace_out.frames.append(base.snapshot(world, agents, "0h", events))
        if checkpoints and checkpoints[0] == 0.0:
            checkpoints.pop(0)

    def selector(agent: base.Agent, current_world: base.World, current_condition: base.Condition, current_rng: random.Random, features: List[float], previous: int) -> str:
        if controller in {"designed", "reactive"}:
            return base.choose_action(agent, current_world, current_condition, current_rng)
        if model is None:
            return "rest"
        model_features = torch.tensor([mask_features(features, ablation)], dtype=torch.float32, device=device)
        with torch.no_grad():
            if model.architecture == "gru":
                state = recurrent_states.get(agent.ident)
                logits, next_state = model.step(model_features, state)
                if next_state is not None:
                    recurrent_states[agent.ident] = next_state.detach()
            else:
                logits, _ = model.step(model_features, None)
            return INDEX_TO_ACTION[int(logits.argmax(dim=-1).item())]

    while world.time < cfg.hours - 1e-9:
        dt = min(cfg.step_hours, cfg.hours - world.time)
        step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
        if world.time < 12.0 and world.major_shocks > 0:
            no_pre_gate_shock = False
        if world.time >= 12.0 and not at_12:
            alive_at_12h = len(base.living(agents))
            at_12 = {"readiness": base.environment_readiness(world)}
        while trace and checkpoints and world.time >= checkpoints[0] - 1e-9:
            hour = checkpoints.pop(0)
            trace_out.frames.append(base.snapshot(world, agents, f"{hour:g}h", events))

    if trace and (not trace_out.frames or trace_out.frames[-1]["hours"] < cfg.hours):
        trace_out.frames.append(base.snapshot(world, agents, f"{cfg.hours:g}h", events))

    row = base.score_episode(world, agents, baseline, at_12, seed, condition, alive_at_12h, no_pre_gate_shock)
    return EvalRow(
        seed=seed,
        controller=controller,
        ablation=ablation,
        final_alive=row.final_alive,
        total_agents=row.total_agents,
        alive_at_12h=row.alive_at_12h,
        no_major_shock_before_12h=row.no_major_shock_before_12h,
        post_gate_shock=row.post_gate_shock,
        major_shocks=row.major_shocks,
        first_shock_hour=row.first_shock_hour,
        births=row.births,
        deaths=row.deaths,
        readiness_at_12h=row.readiness_at_12h,
        final_readiness=row.final_readiness,
        readiness_delta=row.readiness_delta,
        final_pest_pressure=row.final_pest_pressure,
        final_structural_strain=row.final_structural_strain,
        final_fuel_reserve=row.final_fuel_reserve,
        final_seed_bank=row.final_seed_bank,
        final_building_blueprints=row.final_building_blueprints,
        final_tool_blueprints=row.final_tool_blueprints,
        final_forecast_memory=row.final_forecast_memory,
        final_apprenticeship=row.final_apprenticeship,
        architecture_delta=row.architecture_delta,
        tool_system_delta=row.tool_system_delta,
        knowledge_transfer=row.knowledge_transfer,
        adaptation_evidence=row.adaptation_evidence,
        pressure_integral=row.pressure_integral,
        survival_score=row.survival_score,
        readiness_score=row.readiness_score,
        development_score=row.development_score,
        knowledge_score=row.knowledge_score,
        resilience_score=row.resilience_score,
        maturation_score=row.maturation_score,
    ), trace_out


def summarize(rows: Sequence[EvalRow]) -> List[SummaryRow]:
    grouped: Dict[Tuple[str, str], List[EvalRow]] = {}
    for row in rows:
        grouped.setdefault((row.controller, row.ablation), []).append(row)
    summaries: List[SummaryRow] = []
    for (controller, ablation), items in sorted(grouped.items()):
        summaries.append(
            SummaryRow(
                controller=controller,
                ablation=ablation,
                mean_maturation_score=mean(row.maturation_score for row in items),
                mean_survival_score=mean(row.survival_score for row in items),
                mean_readiness_score=mean(row.readiness_score for row in items),
                mean_development_score=mean(row.development_score for row in items),
                mean_knowledge_score=mean(row.knowledge_score for row in items),
                mean_resilience_score=mean(row.resilience_score for row in items),
                mean_final_alive=mean(row.final_alive for row in items),
                mean_alive_at_12h=mean(row.alive_at_12h for row in items),
                mean_births=mean(row.births for row in items),
                mean_deaths=mean(row.deaths for row in items),
                mean_readiness_at_12h=mean(row.readiness_at_12h for row in items),
                mean_final_readiness=mean(row.final_readiness for row in items),
                mean_readiness_delta=mean(row.readiness_delta for row in items),
                mean_final_pest_pressure=mean(row.final_pest_pressure for row in items),
                mean_final_structural_strain=mean(row.final_structural_strain for row in items),
                mean_architecture_delta=mean(row.architecture_delta for row in items),
                mean_tool_system_delta=mean(row.tool_system_delta for row in items),
                mean_knowledge_transfer=mean(row.knowledge_transfer for row in items),
                mean_adaptation_evidence=mean(row.adaptation_evidence for row in items),
                shock_gate_pass_rate=mean(1.0 if row.no_major_shock_before_12h else 0.0 for row in items),
                post_gate_shock_rate=mean(1.0 if row.post_gate_shock else 0.0 for row in items),
            )
        )
    return summaries


def ablations_from_summary(summary: Sequence[SummaryRow]) -> List[AblationRow]:
    by_key = {(row.controller, row.ablation): row for row in summary}
    base_row = by_key[("gru", "none")]
    rows: List[AblationRow] = []
    for ablation in ("body", "infrastructure", "tools", "social_culture", "environment", "readiness", "previous_action"):
        row = by_key[("gru", ablation)]
        rows.append(
            AblationRow(
                controller="gru",
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


def verdict_from_summary(summary: Sequence[SummaryRow], ablations: Sequence[AblationRow]) -> VerdictRow:
    by_key = {(row.controller, row.ablation): row for row in summary}
    gru = by_key[("gru", "none")]
    frame = by_key[("frame_mlp", "none")]
    designed = by_key[("designed", "none")]
    reactive = by_key[("reactive", "none")]
    losses = {row.ablation: row.score_loss for row in ablations}
    learned = (
        gru.shock_gate_pass_rate == 1.0
        and gru.post_gate_shock_rate == 1.0
        and gru.mean_alive_at_12h >= 12.0
        and gru.mean_maturation_score >= 0.70
        and gru.mean_final_readiness >= 0.42
        and gru.mean_maturation_score - reactive.mean_maturation_score >= 0.14
        and designed.mean_maturation_score - gru.mean_maturation_score <= 0.34
    )
    recurrent = gru.mean_maturation_score - frame.mean_maturation_score >= 0.015
    ablation_specific = (
        losses["body"] >= 0.015
        and losses["infrastructure"] >= 0.015
        and losses["tools"] >= 0.015
        and losses["environment"] >= 0.015
        and losses["readiness"] >= 0.015
    )
    return VerdictRow(
        gru_score=gru.mean_maturation_score,
        frame_score=frame.mean_maturation_score,
        designed_score=designed.mean_maturation_score,
        reactive_score=reactive.mean_maturation_score,
        gru_gain_over_reactive=gru.mean_maturation_score - reactive.mean_maturation_score,
        gru_gap_to_designed=designed.mean_maturation_score - gru.mean_maturation_score,
        gru_gain_over_frame=gru.mean_maturation_score - frame.mean_maturation_score,
        body_ablation_loss=losses["body"],
        infrastructure_ablation_loss=losses["infrastructure"],
        tools_ablation_loss=losses["tools"],
        social_culture_ablation_loss=losses["social_culture"],
        environment_ablation_loss=losses["environment"],
        readiness_ablation_loss=losses["readiness"],
        previous_action_ablation_loss=losses["previous_action"],
        shock_gate_pass_rate=gru.shock_gate_pass_rate,
        post_gate_shock_rate=gru.post_gate_shock_rate,
        survival_at_12h=gru.mean_alive_at_12h,
        readiness_at_12h=gru.mean_readiness_at_12h,
        final_readiness=gru.mean_final_readiness,
        final_pest_pressure=gru.mean_final_pest_pressure,
        final_structural_strain=gru.mean_final_structural_strain,
        supports_learned_readiness_control=learned,
        supports_recurrent_advantage=recurrent,
        supports_ablation_specificity=ablation_specific,
        verdict="pass" if learned and recurrent and ablation_specific else "partial_or_failed",
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


def write_artifacts(
    training: Sequence[TrainingRow],
    eval_rows: Sequence[EvalRow],
    summary: Sequence[SummaryRow],
    ablations: Sequence[AblationRow],
    verdict: VerdictRow,
    trace: base.Trace,
    cfg: Config,
) -> Dict[str, object]:
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
            "device": cfg.device,
            "trace_seed": cfg.trace_seed,
        },
        "feature_names": FEATURE_NAMES,
        "feature_groups": {key: list(value) for key, value in FEATURE_GROUPS.items()},
        "actions": list(ACTIONS),
        "training": [asdict(row) for row in training],
        "eval": [asdict(row) for row in eval_rows],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": asdict(trace),
        "notes": {
            "claim": "learned closed-loop imitation controller for environment-readiness maturation",
            "not_claimed": "deep reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
        },
    }
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_learned_environment_readiness_training.csv", training)
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_learned_environment_readiness_eval.csv", eval_rows)
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_learned_environment_readiness_summary.csv", summary)
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_learned_environment_readiness_ablations.csv", ablations)
    rows_to_csv(ARTIFACT_DIR / "ssrm_3d_learned_environment_readiness_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / "ssrm_3d_learned_environment_readiness_results.json", payload)
    write_json(ARTIFACT_DIR / "ssrm_3d_learned_environment_readiness_trace.json", asdict(trace))
    write_js(ARTIFACT_DIR / "ssrm_3d_learned_environment_readiness_results.js", "SSRM_3D_LEARNED_ENVIRONMENT_READINESS_RESULTS", payload)
    write_js(ARTIFACT_DIR / "ssrm_3d_learned_environment_readiness_trace.js", "SSRM_3D_LEARNED_ENVIRONMENT_READINESS_TRACE", asdict(trace))
    return payload


def run_benchmark(cfg: Config) -> Dict[str, object]:
    device = resolve_device(cfg.device)
    sequences, labels = collect_sequences(cfg)
    x, y, mask = build_tensors(sequences, labels, device)
    training_rows: List[TrainingRow] = []
    models: Dict[str, ControllerNet] = {}
    for architecture in ("frame_mlp", "gru"):
        model, row = train_model(architecture, x, y, mask, cfg, device)
        models[architecture] = model
        training_rows.append(row)

    eval_rows: List[EvalRow] = []
    trace = base.Trace(seed=cfg.trace_seed, condition="gru:none")
    controllers = (
        ("designed", None, "none"),
        ("reactive", None, "none"),
        ("frame_mlp", models["frame_mlp"], "none"),
        ("gru", models["gru"], "none"),
    )
    gru_ablations = ("body", "infrastructure", "tools", "social_culture", "environment", "readiness", "previous_action")
    for seed in cfg.eval_seeds:
        for controller, model, ablation in controllers:
            row, maybe_trace = run_controller_episode(
                seed,
                cfg,
                controller,
                model,
                device,
                ablation=ablation,
                trace=(seed == cfg.trace_seed and controller == "gru" and ablation == "none"),
            )
            eval_rows.append(row)
            if maybe_trace.frames:
                trace = maybe_trace
        for ablation in gru_ablations:
            row, _ = run_controller_episode(seed, cfg, "gru", models["gru"], device, ablation=ablation)
            eval_rows.append(row)
    summary = summarize(eval_rows)
    ablations = ablations_from_summary(summary)
    verdict = verdict_from_summary(summary, ablations)
    return write_artifacts(training_rows, eval_rows, summary, ablations, verdict, trace, cfg)


def parse_seed_list(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def parse_args() -> Config:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-seeds", default="20261211,20261212,20261213,20261214,20261215,20261216")
    parser.add_argument("--eval-seeds", default="20261221,20261222,20261223,20261224,20261225")
    parser.add_argument("--hours", type=float, default=72.0)
    parser.add_argument("--step-hours", type=float, default=0.10)
    parser.add_argument("--population", type=int, default=14)
    parser.add_argument("--epochs", type=int, default=52)
    parser.add_argument("--hidden-size", type=int, default=72)
    parser.add_argument("--learning-rate", type=float, default=0.0035)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--trace-seed", type=int, default=20261221)
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
    print(json.dumps({"verdict": payload["verdict"], "training": payload["training"], "summary": payload["summary"]}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
