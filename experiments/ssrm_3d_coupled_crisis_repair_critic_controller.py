#!/usr/bin/env python3
"""Repair-critic reranker for coupled SSRM-3D maturation crises.

Report 106 showed that imitation plus return-selected pressure routing can
preserve 72h maturation while failing crises that require environmental repair
and social coordination together. This benchmark adds a small supervised repair
critic around the GRU. The critic is trained from coupled-crisis repair targets
derived from teacher-world crisis gaps, then selected by closed-loop validation
return.

The learned controller still receives ordinary physics/world symptoms, not a
crisis profile or scenario label. This is not deep reinforcement learning and it
does not claim consciousness.
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

import ssrm_3d_coupled_social_environment_maturation_controller as coupled
import ssrm_3d_learned_multiday_maturation_controller as base
import ssrm_3d_return_selected_multiday_maturation_controller as report105
from ssrm_maturation.agents import choose_action, make_agents
from ssrm_maturation.benchmark import TRACE_CHECKPOINTS, score_episode, snapshot
from ssrm_maturation.environment import clamp, living
from ssrm_maturation.models import CONDITIONS, Agent, Condition, Trace, World


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_repair_critic"


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
    repair_epochs: int = 70
    repair_hidden_size: int = 48
    repair_learning_rate: float = 0.0035
    repair_bias_candidates: Sequence[float] = (0.0, 0.75, 1.25, 1.75, 2.50, 3.50)
    device: str = "auto"
    trace_seed: int = 20261001


@dataclass(frozen=True)
class RepairTrainingRow:
    train_loss: float
    train_accuracy: float
    weighted_accuracy: float
    device_used: str
    parameter_count: int
    train_examples: int
    repair_epochs: int
    repair_hidden_size: int


@dataclass(frozen=True)
class RepairSelectionRow:
    repair_bias: float
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
    selected_repair_bias: float
    repair_critic_total_score: float
    return_selected_total_score: float
    base_gru_total_score: float
    designed_total_score: float
    frame_total_score: float
    reactive_total_score: float
    gain_over_return_selected: float
    gain_over_base_gru: float
    gain_over_frame: float
    gain_over_reactive: float
    gap_to_designed: float
    repair_critic_crisis_score: float
    return_selected_crisis_score: float
    repair_critic_resolved_rate: float
    return_selected_resolved_rate: float
    repair_critic_coupled_response: float
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
    supports_repair_critic: bool
    supports_social_environment_dependency: bool
    verdict: str


class RepairCriticNet(nn.Module):
    def __init__(self, input_size: int, hidden_size: int, output_size: int) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.Tanh(),
            nn.Linear(hidden_size, hidden_size),
            nn.Tanh(),
            nn.Linear(hidden_size, output_size),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


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


def repair_gate(features: Sequence[float], ablation: str) -> float:
    masked = base.mask_features(list(features), ablation)
    pressure = report105.pressure_value(features, ablation)
    post_gate = masked[FEATURE["post_gate"]]
    shock_hint = masked[FEATURE["major_shocks"]]
    symptom_pressure = max(
        pressure["environment"],
        pressure["social"],
        pressure["infrastructure"] * 0.65,
        pressure["teaching"] * 0.55,
    )
    return clamp(symptom_pressure * (0.30 + 0.70 * post_gate) + shock_hint * 0.22 - 0.12)


def crisis_target_action(active: coupled.ActiveCrisis, features: Sequence[float]) -> str:
    env_fraction = min(1.0, active.env_progress / active.profile.env_need)
    social_fraction = min(1.0, active.social_progress / active.profile.social_need)
    env_gap = 1.0 - env_fraction
    social_gap = 1.0 - social_fraction
    profile = active.profile

    if env_gap >= social_gap + 0.03:
        if "construct" in profile.env_actions:
            return "construct"
        if "scout" in profile.env_actions and (
            features[FEATURE["route_hazard"]] > 0.34
            or features[FEATURE["visibility"]] < 0.48
            or features[FEATURE["resource_migration"]] > 0.34
        ):
            return "scout"
        if "collect_water" in profile.env_actions and features[FEATURE["water"]] <= features[FEATURE["food"]]:
            return "collect_water"
        if "harvest_food" in profile.env_actions:
            return "harvest_food"
        if "sanitize" in profile.env_actions and features[FEATURE["contamination"]] >= features[FEATURE["disease"]]:
            return "sanitize"
        if "treat" in profile.env_actions:
            return "treat"
        return profile.env_actions[0]

    if social_gap >= env_gap + 0.03:
        if "social_repair" in profile.social_actions and (
            features[FEATURE["conflict"]] > 0.24 or features[FEATURE["social_trust"]] < 0.58
        ):
            return "social_repair"
        if "teach" in profile.social_actions:
            return "teach"
        if "learn" in profile.social_actions:
            return "learn"
        return profile.social_actions[0]

    if features[FEATURE["conflict"]] > 0.30 or features[FEATURE["social_trust"]] < 0.52:
        return "social_repair"
    if "sanitize" in profile.env_actions and features[FEATURE["contamination"]] > 0.38:
        return "sanitize"
    if "construct" in profile.env_actions and features[FEATURE["shelter"]] < 0.54:
        return "construct"
    if "scout" in profile.env_actions:
        return "scout"
    return profile.social_actions[0]


def collect_repair_examples(cfg: Config) -> Tuple[List[List[float]], List[int], List[float]]:
    condition = CONDITIONS[0]
    examples: List[List[float]] = []
    labels: List[int] = []
    weights: List[float] = []
    for seed in cfg.train_seeds:
        rng = random.Random(seed * 109 + 41)
        agents = make_agents(rng, cfg.population)
        world = coupled.prepare_world(rng, cfg)
        previous_actions: Dict[str, int] = {}
        events: List[str] = []
        tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))

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
                active = tracker.active
                if active is not None and current_world.time >= 12.0:
                    target = crisis_target_action(active, features)
                    examples.append(features)
                    labels.append(base.ACTION_TO_INDEX[target])
                    pressure = report105.pressure_value(features, "none")
                    urgent = max(pressure["environment"], pressure["social"], pressure["infrastructure"])
                    weights.append(1.0 + urgent * 1.25)
                action = choose_action(agent, current_world, current_condition, current_rng)
                action_counts[action] = action_counts.get(action, 0) + 1
                return action

            base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
            coupled.update_crisis_after_actions(world, agents, tracker, action_counts, dt)
            coupled.complete_crisis_if_due(world, agents, tracker, events)
    return examples, labels, weights


def train_repair_critic(cfg: Config, device: torch.device) -> Tuple[RepairCriticNet, RepairTrainingRow]:
    features, labels, weights = collect_repair_examples(cfg)
    if not features:
        raise RuntimeError("no repair critic examples collected")
    torch.manual_seed(20261011)
    x = torch.tensor(features, dtype=torch.float32, device=device)
    y = torch.tensor(labels, dtype=torch.long, device=device)
    sample_weights = torch.tensor(weights, dtype=torch.float32, device=device)
    model = RepairCriticNet(base.FEATURE_COUNT, cfg.repair_hidden_size, len(base.ACTIONS)).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.repair_learning_rate)
    loss_fn = nn.CrossEntropyLoss(reduction="none")
    for _ in range(cfg.repair_epochs):
        model.train()
        optimizer.zero_grad()
        logits = model(x)
        loss = (loss_fn(logits, y) * sample_weights).sum() / sample_weights.sum()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 2.0)
        optimizer.step()
    model.eval()
    with torch.no_grad():
        logits = model(x)
        losses = loss_fn(logits, y)
        loss = (losses * sample_weights).sum().item() / sample_weights.sum().item()
        predictions = logits.argmax(dim=-1)
        accuracy = (predictions == y).float().mean().item()
        weighted_accuracy = (((predictions == y).float() * sample_weights).sum() / sample_weights.sum()).item()
    return model, RepairTrainingRow(
        train_loss=loss,
        train_accuracy=accuracy,
        weighted_accuracy=weighted_accuracy,
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in model.parameters()),
        train_examples=len(features),
        repair_epochs=cfg.repair_epochs,
        repair_hidden_size=cfg.repair_hidden_size,
    )


def apply_repair_bias(
    logits: torch.Tensor,
    features: Sequence[float],
    critic: RepairCriticNet,
    repair_bias: float,
    device: torch.device,
    ablation: str,
) -> torch.Tensor:
    gate = repair_gate(features, ablation)
    if repair_bias <= 0.0 or gate <= 0.0:
        return logits
    critic_features = torch.tensor([base.mask_features(list(features), ablation)], dtype=torch.float32, device=device)
    repair_logits = critic(critic_features)
    repair_logits = repair_logits - repair_logits.mean(dim=-1, keepdim=True)
    repair_logits = torch.clamp(repair_logits, -2.5, 2.5)
    return logits + repair_logits.to(dtype=logits.dtype) * repair_bias * gate


def run_episode(
    seed: int,
    cfg: Config,
    controller: str,
    model: Optional[base.ControllerNet],
    device: torch.device,
    router: report105.PressureRouter,
    critic: Optional[RepairCriticNet] = None,
    repair_bias: float = 0.0,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, Trace, coupled.CrisisTracker]:
    if controller != "repair_critic_gru":
        return coupled.run_episode(seed, cfg, controller, model, device, router, ablation=ablation, trace=trace)
    if model is None or critic is None:
        raise ValueError("repair_critic_gru requires both base model and repair critic")

    condition = CONDITIONS[0]
    rng = random.Random(seed * 101 + sum(ord(ch) for ch in controller + router.name + ablation) + int(repair_bias * 1000))
    agents = make_agents(rng, cfg.population)
    world = coupled.prepare_world(rng, cfg)
    baseline = base.initial_baseline(world, cfg.population)
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
    trace_out = Trace(seed=seed, condition=f"{controller}:{router.name}:bias_{repair_bias:g}:{ablation}")
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
            model_features = torch.tensor([base.mask_features(features, ablation)], dtype=torch.float32, device=device)
            with torch.no_grad():
                state = recurrent_states.get(agent.ident)
                logits, next_state = model.step(model_features, state)
                if next_state is not None:
                    recurrent_states[agent.ident] = next_state.detach()
                logits = logits + report105.router_bias(features, router, device, logits.dtype, ablation)
                logits = apply_repair_bias(logits, features, critic, repair_bias, device, ablation)
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
    objective = total + crisis * 0.08 + resolved * 0.07 + coupled_response * 0.05 - damage * 0.18
    return total, maturation, crisis, resolved, coupled_response, objective


def select_repair_bias(
    cfg: Config,
    model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
    critic: RepairCriticNet,
) -> Tuple[float, List[RepairSelectionRow]]:
    best = cfg.repair_bias_candidates[0]
    best_objective = -1.0
    rows: List[RepairSelectionRow] = []
    for bias in cfg.repair_bias_candidates:
        eval_rows = [
            run_episode(seed, cfg, "repair_critic_gru", model, device, router, critic, bias)[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, coupled_response, objective = selection_objective(eval_rows)
        damage = mean(row.crisis_damage for row in eval_rows)
        if objective > best_objective:
            best = bias
            best_objective = objective
        rows.append(
            RepairSelectionRow(
                repair_bias=bias,
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
        RepairSelectionRow(
            row.repair_bias,
            row.tune_total_score,
            row.tune_maturation_score,
            row.tune_crisis_score,
            row.tune_resolved_rate,
            row.tune_coupled_response,
            row.tune_damage,
            row.selection_objective,
            row.repair_bias == best,
        )
        for row in rows
    ]


def ablations_from_summary(summary: Sequence[coupled.SummaryRow]) -> List[coupled.AblationRow]:
    base_row = coupled.row_lookup(summary, "repair_critic_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in ("body", "infrastructure", "tools", "social_culture", "environment", "previous_action"):
        row = coupled.row_lookup(summary, "repair_critic_gru", ablation)
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
    selected_repair_bias: float,
) -> VerdictRow:
    repair = coupled.row_lookup(summary, "repair_critic_gru", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    base_gru = coupled.row_lookup(summary, "gru", "none")
    designed = coupled.row_lookup(summary, "designed", "none")
    frame = coupled.row_lookup(summary, "frame_mlp", "none")
    reactive = coupled.row_lookup(summary, "reactive", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    supports_repair = (
        selected_repair_bias > 0.0
        and repair.mean_total_score - returned.mean_total_score >= 0.020
        and (
            repair.mean_crisis_score - returned.mean_crisis_score >= 0.050
            or repair.mean_resolved_rate - returned.mean_resolved_rate >= 0.150
        )
        and repair.mean_alive_at_12h >= 12.0
        and repair.shock_gate_pass_rate == 1.0
        and repair.post_gate_shock_rate == 1.0
    )
    supports_dependency = (
        social.crisis_score_loss >= 0.020
        and environment.crisis_score_loss >= 0.020
        and social.coupled_response_loss >= 0.015
        and environment.coupled_response_loss >= 0.015
    )
    return VerdictRow(
        selected_router=selected_router.name,
        selected_repair_bias=selected_repair_bias,
        repair_critic_total_score=repair.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        base_gru_total_score=base_gru.mean_total_score,
        designed_total_score=designed.mean_total_score,
        frame_total_score=frame.mean_total_score,
        reactive_total_score=reactive.mean_total_score,
        gain_over_return_selected=repair.mean_total_score - returned.mean_total_score,
        gain_over_base_gru=repair.mean_total_score - base_gru.mean_total_score,
        gain_over_frame=repair.mean_total_score - frame.mean_total_score,
        gain_over_reactive=repair.mean_total_score - reactive.mean_total_score,
        gap_to_designed=designed.mean_total_score - repair.mean_total_score,
        repair_critic_crisis_score=repair.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        repair_critic_resolved_rate=repair.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        repair_critic_coupled_response=repair.mean_coupled_response_rate,
        return_selected_coupled_response=returned.mean_coupled_response_rate,
        social_culture_total_loss=social.total_loss,
        environment_total_loss=environment.total_loss,
        social_culture_crisis_loss=social.crisis_score_loss,
        environment_crisis_loss=environment.crisis_score_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=repair.shock_gate_pass_rate,
        post_gate_shock_rate=repair.post_gate_shock_rate,
        survival_at_12h=repair.mean_alive_at_12h,
        supports_repair_critic=supports_repair,
        supports_social_environment_dependency=supports_dependency,
        verdict="pass" if supports_repair and supports_dependency else "partial_or_failed",
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
    repair_critic, repair_training = train_repair_critic(cfg, device)
    selected_bias, repair_selection = select_repair_bias(cfg, models["gru"], device, selected_router, repair_critic)

    eval_rows: List[coupled.EvalRow] = []
    trace = Trace(seed=cfg.trace_seed, condition=f"repair_critic_gru:{selected_router.name}:bias_{selected_bias:g}:none")
    crisis_logs: Dict[str, List[dict[str, object]]] = {}
    for seed in cfg.eval_seeds:
        for controller, model, router, critic, bias in (
            ("designed", None, report105.ROUTERS[0], None, 0.0),
            ("reactive", None, report105.ROUTERS[0], None, 0.0),
            ("frame_mlp", models["frame_mlp"], report105.ROUTERS[0], None, 0.0),
            ("gru", models["gru"], report105.ROUTERS[0], None, 0.0),
            ("return_selected_gru", models["gru"], selected_router, None, 0.0),
            ("repair_critic_gru", models["gru"], selected_router, repair_critic, selected_bias),
        ):
            row, maybe_trace, tracker = run_episode(
                seed,
                cfg,
                controller,
                model,
                device,
                router,
                critic,
                bias,
                trace=(seed == cfg.trace_seed and controller == "repair_critic_gru"),
            )
            eval_rows.append(row)
            crisis_logs[f"{seed}:{controller}:none"] = tracker.response_log
            if maybe_trace.frames:
                trace = maybe_trace
        for ablation in ("body", "infrastructure", "tools", "social_culture", "environment", "previous_action"):
            row, _, tracker = run_episode(
                seed,
                cfg,
                "repair_critic_gru",
                models["gru"],
                device,
                selected_router,
                repair_critic,
                selected_bias,
                ablation=ablation,
            )
            eval_rows.append(row)
            crisis_logs[f"{seed}:repair_critic_gru:{ablation}"] = tracker.response_log

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
            "repair_epochs": cfg.repair_epochs,
            "repair_hidden_size": cfg.repair_hidden_size,
            "repair_bias_candidates": list(cfg.repair_bias_candidates),
            "device": cfg.device,
            "trace_seed": cfg.trace_seed,
        },
        "crisis_profiles": [asdict(profile) for profile in coupled.PROFILES],
        "routers": [asdict(router) for router in report105.ROUTERS],
        "router_selection": [asdict(row) for row in router_selection],
        "repair_selection": [asdict(row) for row in repair_selection],
        "base_training": [asdict(row) for row in training_rows],
        "repair_training": asdict(repair_training),
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": asdict(trace),
        "crisis_logs": crisis_logs,
        "notes": {
            "claim": "supervised repair-critic reranker for coupled social/environment crisis pressure",
            "not_claimed": "deep reinforcement learning, subjective consciousness, open-ended civilization, or real-world software competence",
            "input_discipline": "the repair critic consumes ordinary feature vectors and does not receive the active crisis profile",
        },
    }
    rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    rows_to_csv(Path(f"{PREFIX}_repair_training.csv"), [repair_training])
    rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    rows_to_csv(Path(f"{PREFIX}_repair_selection.csv"), repair_selection)
    rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    write_json(Path(f"{PREFIX}_results.json"), payload)
    write_json(Path(f"{PREFIX}_trace.json"), asdict(trace))
    write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_REPAIR_CRITIC_RESULTS", payload)
    write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_REPAIR_CRITIC_TRACE", asdict(trace))
    return payload


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-seeds", default="20260911,20260912,20260913,20260914,20260915,20260916")
    parser.add_argument("--tune-seeds", default="20260981,20260982,20260983")
    parser.add_argument("--eval-seeds", default="20261001,20261002,20261003,20261004,20261005")
    parser.add_argument("--hours", type=float, default=72.0)
    parser.add_argument("--step-hours", type=float, default=0.10)
    parser.add_argument("--population", type=int, default=14)
    parser.add_argument("--epochs", type=int, default=42)
    parser.add_argument("--hidden-size", type=int, default=64)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--repair-epochs", type=int, default=70)
    parser.add_argument("--repair-hidden-size", type=int, default=48)
    parser.add_argument("--repair-learning-rate", type=float, default=0.0035)
    parser.add_argument("--repair-bias-candidates", default="0.00,0.75,1.25,1.75,2.50,3.50")
    parser.add_argument("--device", default="auto")
    parser.add_argument("--trace-seed", type=int, default=20261001)
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
        repair_epochs=args.repair_epochs,
        repair_hidden_size=args.repair_hidden_size,
        repair_learning_rate=args.repair_learning_rate,
        repair_bias_candidates=parse_floats(args.repair_bias_candidates),
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({"repair_selection": payload["repair_selection"], "verdict": payload["verdict"], "summary": payload["summary"]}, indent=2))
    # A failed repair-critic verdict is evidence, not a process failure.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
