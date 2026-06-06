#!/usr/bin/env python3
"""Diagnostic-memory controller for SSRM-3D coupled crises.

Report 111 replaced analytic plan values with cloned rollout labels, but
validation rejected the overlay. This benchmark tries a narrower policy-state
step: train a recurrent diagnostic action head to identify the primary
environmental repair from stricter coupled-crisis symptoms, then let validation
decide whether that head should influence the held-out controller.

The diagnostic head receives ordinary observation features. It does not receive
the active crisis profile or scenario label at runtime. This is still supervised
diagnostic imitation, not actor-critic reinforcement learning, open-ended
civilization, or subjective consciousness.
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

import ssrm_3d_coupled_crisis_repair_critic_controller as report107
import ssrm_3d_coupled_crisis_rollout_window_controller as report111
import ssrm_3d_coupled_social_environment_maturation_controller as coupled
import ssrm_3d_learned_multiday_maturation_controller as base
import ssrm_3d_return_selected_multiday_maturation_controller as report105
from ssrm_maturation.agents import choose_action, make_agents
from ssrm_maturation.benchmark import TRACE_CHECKPOINTS, score_episode, snapshot
from ssrm_maturation.environment import clamp, living
from ssrm_maturation.models import CONDITIONS, Agent, Condition, Trace, World


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_crisis_diagnostic_memory"


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
    diagnostic_epochs: int = 54
    diagnostic_hidden_size: int = 64
    diagnostic_learning_rate: float = 0.004
    diagnostic_bias_candidates: Sequence[float] = (0.0, 0.75, 1.25, 1.75, 2.5, 3.5, 5.0, 8.0, 12.0, 20.0)
    device: str = "auto"
    trace_seed: int = 20261021


@dataclass(frozen=True)
class DiagnosticTrainingRow:
    train_loss: float
    accuracy: float
    crisis_accuracy: float
    env_accuracy: float
    social_accuracy: float
    device_used: str
    parameter_count: int
    train_examples: int
    crisis_examples: int
    diagnostic_epochs: int
    diagnostic_hidden_size: int


@dataclass(frozen=True)
class DiagnosticSelectionRow:
    diagnostic_bias: float
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
    selected_diagnostic_bias: float
    diagnostic_memory_total_score: float
    return_selected_reference_total_score: float
    return_selected_total_score: float
    base_gru_total_score: float
    designed_total_score: float
    frame_total_score: float
    reactive_total_score: float
    gain_over_return_selected_reference: float
    gain_over_return_selected: float
    gain_over_base_gru: float
    gain_over_frame: float
    gain_over_reactive: float
    gap_to_designed: float
    diagnostic_memory_crisis_score: float
    return_selected_crisis_score: float
    diagnostic_memory_resolved_rate: float
    return_selected_resolved_rate: float
    diagnostic_memory_env_response: float
    return_selected_env_response: float
    diagnostic_memory_social_response: float
    return_selected_social_response: float
    diagnostic_memory_coupled_response: float
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
    supports_environment_response_gain: bool
    supports_diagnostic_memory_selection: bool
    supports_social_environment_dependency: bool
    verdict: str


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def parse_ints(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def parse_floats(value: str) -> Tuple[float, ...]:
    return tuple(float(part.strip()) for part in value.split(",") if part.strip())


def collect_diagnostic_sequences(cfg: Config) -> Tuple[List[List[List[float]]], List[List[int]], List[List[int]]]:
    condition = CONDITIONS[0]
    sequences: Dict[str, List[List[float]]] = {}
    labels: Dict[str, List[int]] = {}
    crisis_flags: Dict[str, List[int]] = {}
    for seed in cfg.train_seeds:
        rng = random.Random(seed * 149 + 61)
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
                    action = report111.primary_env_action(active)
                    key = f"{seed}:{agent.ident}:crisis{tracker.started}"
                    sequences.setdefault(key, []).append(features)
                    labels.setdefault(key, []).append(base.ACTION_TO_INDEX[action])
                    crisis_flags.setdefault(key, []).append(1)
                else:
                    action = choose_action(agent, current_world, current_condition, current_rng)
                action_counts[action] = action_counts.get(action, 0) + 1
                return action

            base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
            report111.update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
            coupled.complete_crisis_if_due(world, agents, tracker, events)
    keys = sorted(sequences)
    return [sequences[key] for key in keys], [labels[key] for key in keys], [crisis_flags[key] for key in keys]


def build_flag_tensor(flags: List[List[int]], max_len: int, device: torch.device) -> torch.Tensor:
    out = torch.zeros((len(flags), max_len), dtype=torch.bool)
    for row, seq in enumerate(flags):
        out[row, : len(seq)] = torch.tensor(seq, dtype=torch.bool)
    return out.to(device)


def train_diagnostic_model(cfg: Config, device: torch.device) -> Tuple[base.ControllerNet, DiagnosticTrainingRow]:
    sequences, labels, flags = collect_diagnostic_sequences(cfg)
    x, y, mask = base.build_tensors(sequences, labels, device)
    crisis_mask = build_flag_tensor(flags, y.shape[1], device) & mask
    env_actions = torch.tensor([base.ACTION_TO_INDEX[action] for action in report111.DIAGNOSTIC_ENV_ACTIONS], device=device)
    social_actions = torch.tensor([base.ACTION_TO_INDEX[action] for action in report111.SOCIAL_RESPONSE_ACTIONS], device=device)
    env_valid = crisis_mask & torch.isin(y, env_actions)
    social_valid = crisis_mask & torch.isin(y, social_actions)
    torch.manual_seed(20261129)
    model = base.ControllerNet("gru", base.FEATURE_COUNT, cfg.diagnostic_hidden_size, len(base.ACTIONS)).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=cfg.diagnostic_learning_rate)
    sample_weights = (
        mask.float() * 0.04
        + crisis_mask.float() * 1.80
        + env_valid.float() * 10.0
        + social_valid.float() * 1.30
    )
    for _ in range(cfg.diagnostic_epochs):
        model.train()
        optimizer.zero_grad()
        logits, _ = model(x)
        per_item = torch.nn.functional.cross_entropy(
            logits.reshape(-1, len(base.ACTIONS)),
            y.reshape(-1),
            ignore_index=-100,
            reduction="none",
        ).reshape_as(y)
        loss = (per_item * sample_weights).sum() / sample_weights.sum().clamp_min(1e-6)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 2.0)
        optimizer.step()
    model.eval()
    with torch.no_grad():
        logits, _ = model(x)
        per_item = torch.nn.functional.cross_entropy(
            logits.reshape(-1, len(base.ACTIONS)),
            y.reshape(-1),
            ignore_index=-100,
            reduction="none",
        ).reshape_as(y)
        loss = ((per_item * sample_weights).sum() / sample_weights.sum().clamp_min(1e-6)).item()
        pred = logits.argmax(dim=-1)
        valid = mask
        crisis_valid = crisis_mask
        accuracy = ((pred == y) & valid).sum().float() / valid.sum().clamp_min(1)
        crisis_accuracy = ((pred == y) & crisis_valid).sum().float() / crisis_valid.sum().clamp_min(1)
        env_accuracy = ((pred == y) & env_valid).sum().float() / env_valid.sum().clamp_min(1)
        social_accuracy = ((pred == y) & social_valid).sum().float() / social_valid.sum().clamp_min(1)
    return model, DiagnosticTrainingRow(
        train_loss=loss,
        accuracy=accuracy.item(),
        crisis_accuracy=crisis_accuracy.item(),
        env_accuracy=env_accuracy.item(),
        social_accuracy=social_accuracy.item(),
        device_used=str(device),
        parameter_count=sum(parameter.numel() for parameter in model.parameters()),
        train_examples=int(valid.sum().item()),
        crisis_examples=int(crisis_valid.sum().item()),
        diagnostic_epochs=cfg.diagnostic_epochs,
        diagnostic_hidden_size=cfg.diagnostic_hidden_size,
    )


def diagnostic_env_action_bias(logits: torch.Tensor, bias: float, gate: float, dtype: torch.dtype, device: torch.device) -> torch.Tensor:
    out = torch.zeros((1, len(base.ACTIONS)), dtype=dtype, device=device)
    if bias <= 0.0 or gate <= 0.0:
        return out
    probs = torch.softmax(logits, dim=-1)
    action_index = int(probs.argmax(dim=-1).item())
    action = base.INDEX_TO_ACTION[action_index]
    if action not in report111.DIAGNOSTIC_ENV_ACTIONS:
        return out
    confidence = float(probs[:, action_index].item())
    out[:, action_index] += bias * gate * (2.2 + confidence * 1.8)
    return out


def run_episode(
    seed: int,
    cfg: Config,
    controller: str,
    model: Optional[base.ControllerNet],
    diagnostic_model: Optional[base.ControllerNet],
    device: torch.device,
    router: report105.PressureRouter,
    diagnostic_bias: float = 0.0,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[coupled.EvalRow, Trace, coupled.CrisisTracker]:
    if controller == "diagnostic_memory_gru" and (model is None or diagnostic_model is None):
        raise ValueError("diagnostic_memory_gru requires base and diagnostic models")

    condition = CONDITIONS[1] if controller == "reactive" else CONDITIONS[0]
    rng = random.Random(seed * 127 + 9001)
    agents = make_agents(rng, cfg.population)
    world = coupled.prepare_world(rng, cfg)
    baseline = base.initial_baseline(world, cfg.population)
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    diagnostic_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    tracker = coupled.CrisisTracker(schedule=coupled.crisis_schedule(seed))
    trace_out = Trace(seed=seed, condition=f"{controller}:{router.name}:diag_{diagnostic_bias:g}:{ablation}")
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
            active = tracker.active
            if controller == "designed":
                action = report111.bottleneck_target_action(active, features) if active is not None else choose_action(agent, current_world, current_condition, current_rng)
            elif controller == "reactive":
                action = choose_action(agent, current_world, current_condition, current_rng)
            elif model is None:
                action = "rest"
            else:
                model_features = torch.tensor([base.mask_features(features, ablation)], dtype=torch.float32, device=device)
                with torch.no_grad():
                    if model.architecture == "gru":
                        state = recurrent_states.get(agent.ident)
                        logits, next_state = model.step(model_features, state)
                        if next_state is not None:
                            recurrent_states[agent.ident] = next_state.detach()
                    else:
                        logits, _ = model.step(model_features, None)
                    if controller == "return_selected_gru":
                        logits = logits + report105.router_bias(features, router, device, logits.dtype, ablation)
                    elif controller == "diagnostic_memory_gru":
                        base_logits = logits + report105.router_bias(features, router, device, logits.dtype, ablation)
                        gate = report111.bottleneck_gate(features, ablation)
                        if active is None:
                            diagnostic_states.pop(agent.ident, None)
                            diag_bias = torch.zeros_like(base_logits)
                        else:
                            diag_state = diagnostic_states.get(agent.ident)
                            diag_logits, next_diag_state = diagnostic_model.step(model_features, diag_state)
                            if next_diag_state is not None:
                                diagnostic_states[agent.ident] = next_diag_state.detach()
                            gate = max(gate, 0.60)
                            diag_bias = diagnostic_env_action_bias(diag_logits, diagnostic_bias, gate, logits.dtype, device)
                        logits = base_logits + diag_bias
                    action = base.INDEX_TO_ACTION[int(logits.argmax(dim=-1).item())]
            action_counts[action] = action_counts.get(action, 0) + 1
            return action

        base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
        report111.update_bottleneck_crisis_after_actions(world, agents, tracker, action_counts, dt)
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


def selection_objective(rows: Sequence[coupled.EvalRow]) -> Tuple[float, float, float, float, float, float, float, float]:
    total = mean(row.total_score for row in rows)
    maturation = mean(row.maturation_score for row in rows)
    crisis = mean(row.crisis_score for row in rows)
    resolved = mean(row.resolved_rate for row in rows)
    env_response = mean(row.env_response_rate for row in rows)
    social_response = mean(row.social_response_rate for row in rows)
    coupled_response = mean(row.coupled_response_rate for row in rows)
    damage = mean(row.crisis_damage for row in rows)
    objective = total * 0.65 + crisis * 0.85 + resolved * 0.45 + coupled_response * 0.55 - damage * 0.34
    return total, maturation, crisis, resolved, env_response, social_response, coupled_response, objective


def select_diagnostic_bias(
    cfg: Config,
    model: base.ControllerNet,
    diagnostic_model: base.ControllerNet,
    device: torch.device,
    router: report105.PressureRouter,
) -> Tuple[float, List[DiagnosticSelectionRow]]:
    best = cfg.diagnostic_bias_candidates[0]
    best_objective = -1e9
    rows: List[DiagnosticSelectionRow] = []
    for bias in cfg.diagnostic_bias_candidates:
        eval_rows = [
            run_episode(seed, cfg, "diagnostic_memory_gru", model, diagnostic_model, device, router, bias)[0]
            for seed in cfg.tune_seeds
        ]
        total, maturation, crisis, resolved, env_response, social_response, coupled_response, objective = selection_objective(eval_rows)
        damage = mean(row.crisis_damage for row in eval_rows)
        if objective > best_objective:
            best = bias
            best_objective = objective
        rows.append(DiagnosticSelectionRow(
            diagnostic_bias=bias,
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
    return best, [
        DiagnosticSelectionRow(
            row.diagnostic_bias,
            row.tune_total_score,
            row.tune_maturation_score,
            row.tune_crisis_score,
            row.tune_resolved_rate,
            row.tune_env_response,
            row.tune_social_response,
            row.tune_coupled_response,
            row.tune_damage,
            row.selection_objective,
            row.diagnostic_bias == best,
        )
        for row in rows
    ]


def ablations_from_summary(summary: Sequence[coupled.SummaryRow]) -> List[coupled.AblationRow]:
    base_row = coupled.row_lookup(summary, "diagnostic_memory_gru", "none")
    rows: List[coupled.AblationRow] = []
    for ablation in ("body", "infrastructure", "tools", "social_culture", "environment", "previous_action"):
        row = coupled.row_lookup(summary, "diagnostic_memory_gru", ablation)
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


def verdict_from_summary(
    summary: Sequence[coupled.SummaryRow],
    ablations: Sequence[coupled.AblationRow],
    selected_router: report105.PressureRouter,
    selected_bias: float,
) -> VerdictRow:
    outcome = coupled.row_lookup(summary, "diagnostic_memory_gru", "none")
    reference = coupled.row_lookup(summary, "return_selected_reference", "none")
    returned = coupled.row_lookup(summary, "return_selected_gru", "none")
    base_gru = coupled.row_lookup(summary, "gru", "none")
    designed = coupled.row_lookup(summary, "designed", "none")
    frame = coupled.row_lookup(summary, "frame_mlp", "none")
    reactive = coupled.row_lookup(summary, "reactive", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    supports_selection = (
        selected_bias > 0.0
        and outcome.mean_total_score - returned.mean_total_score >= 0.020
        and (
            outcome.mean_crisis_score - returned.mean_crisis_score >= 0.050
            or outcome.mean_resolved_rate - returned.mean_resolved_rate >= 0.150
            or outcome.mean_coupled_response_rate - returned.mean_coupled_response_rate >= 0.120
        )
        and outcome.mean_alive_at_12h >= 12.0
        and outcome.shock_gate_pass_rate == 1.0
        and outcome.post_gate_shock_rate == 1.0
    )
    supports_environment_response = (
        selected_bias > 0.0
        and outcome.mean_env_response_rate - returned.mean_env_response_rate >= 0.150
    )
    supports_dependency = (
        social.coupled_response_loss >= 0.020
        and environment.coupled_response_loss >= 0.020
        and (social.crisis_score_loss >= 0.020 or social.resolved_rate_loss >= 0.050)
        and (environment.crisis_score_loss >= 0.020 or environment.resolved_rate_loss >= 0.050)
    )
    return VerdictRow(
        selected_router=selected_router.name,
        selected_diagnostic_bias=selected_bias,
        diagnostic_memory_total_score=outcome.mean_total_score,
        return_selected_reference_total_score=reference.mean_total_score,
        return_selected_total_score=returned.mean_total_score,
        base_gru_total_score=base_gru.mean_total_score,
        designed_total_score=designed.mean_total_score,
        frame_total_score=frame.mean_total_score,
        reactive_total_score=reactive.mean_total_score,
        gain_over_return_selected_reference=outcome.mean_total_score - reference.mean_total_score,
        gain_over_return_selected=outcome.mean_total_score - returned.mean_total_score,
        gain_over_base_gru=outcome.mean_total_score - base_gru.mean_total_score,
        gain_over_frame=outcome.mean_total_score - frame.mean_total_score,
        gain_over_reactive=outcome.mean_total_score - reactive.mean_total_score,
        gap_to_designed=designed.mean_total_score - outcome.mean_total_score,
        diagnostic_memory_crisis_score=outcome.mean_crisis_score,
        return_selected_crisis_score=returned.mean_crisis_score,
        diagnostic_memory_resolved_rate=outcome.mean_resolved_rate,
        return_selected_resolved_rate=returned.mean_resolved_rate,
        diagnostic_memory_env_response=outcome.mean_env_response_rate,
        return_selected_env_response=returned.mean_env_response_rate,
        diagnostic_memory_social_response=outcome.mean_social_response_rate,
        return_selected_social_response=returned.mean_social_response_rate,
        diagnostic_memory_coupled_response=outcome.mean_coupled_response_rate,
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
        supports_environment_response_gain=supports_environment_response,
        supports_diagnostic_memory_selection=supports_selection,
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
    diagnostic_model, diagnostic_training = train_diagnostic_model(cfg, device)
    selected_bias, diagnostic_selection = select_diagnostic_bias(cfg, models["gru"], diagnostic_model, device, selected_router)

    eval_rows: List[coupled.EvalRow] = []
    trace = Trace(seed=cfg.trace_seed, condition=f"diagnostic_memory_gru:{selected_router.name}:diag_{selected_bias:g}:none")
    crisis_logs: Dict[str, List[dict[str, object]]] = {}
    for seed in cfg.eval_seeds:
        for controller, model, diag_model, router, bias in (
            ("designed", None, None, report105.ROUTERS[0], 0.0),
            ("reactive", None, None, report105.ROUTERS[0], 0.0),
            ("frame_mlp", models["frame_mlp"], None, report105.ROUTERS[0], 0.0),
            ("gru", models["gru"], None, report105.ROUTERS[0], 0.0),
            ("return_selected_gru", models["gru"], None, selected_router, 0.0),
            ("diagnostic_memory_gru", models["gru"], diagnostic_model, selected_router, selected_bias),
        ):
            row, maybe_trace, tracker = run_episode(
                seed,
                cfg,
                controller,
                model,
                diag_model,
                device,
                router,
                bias,
                trace=(seed == cfg.trace_seed and controller == "diagnostic_memory_gru"),
            )
            eval_rows.append(row)
            crisis_logs[f"{seed}:{controller}:none"] = tracker.response_log
            if controller == "return_selected_gru":
                eval_rows.append(coupled.EvalRow(**{**asdict(row), "controller": "return_selected_reference"}))
                crisis_logs[f"{seed}:return_selected_reference:none"] = tracker.response_log
            if maybe_trace.frames:
                trace = maybe_trace

        for ablation in ("body", "infrastructure", "tools", "social_culture", "environment", "previous_action"):
            row, _, tracker = run_episode(
                seed,
                cfg,
                "diagnostic_memory_gru",
                models["gru"],
                diagnostic_model,
                device,
                selected_router,
                selected_bias,
                ablation=ablation,
            )
            eval_rows.append(row)
            crisis_logs[f"{seed}:diagnostic_memory_gru:{ablation}"] = tracker.response_log

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
            "diagnostic_epochs": cfg.diagnostic_epochs,
            "diagnostic_hidden_size": cfg.diagnostic_hidden_size,
            "diagnostic_bias_candidates": list(cfg.diagnostic_bias_candidates),
            "device": cfg.device,
            "trace_seed": cfg.trace_seed,
        },
        "crisis_profiles": [asdict(profile) for profile in coupled.PROFILES],
        "primary_env_actions": report111.PRIMARY_ENV_ACTION,
        "routers": [asdict(router) for router in report105.ROUTERS],
        "router_selection": [asdict(row) for row in router_selection],
        "diagnostic_selection": [asdict(row) for row in diagnostic_selection],
        "base_training": [asdict(row) for row in training_rows],
        "diagnostic_training": asdict(diagnostic_training),
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": asdict(trace),
        "crisis_logs": crisis_logs,
        "notes": {
            "claim": "recurrent crisis-diagnostic action memory for coupled social/environment pressure",
            "not_claimed": "actor-critic reinforcement learning, subjective consciousness, open-ended civilization, or real-world competence",
            "input_discipline": "the diagnostic GRU consumes ordinary observation features and previous-action context, but not active crisis profile labels at runtime",
            "return_selected_reference": "duplicate of the return-selected GRU held-out row used as a stable baseline reference, not a separate Report 111 rerun",
        },
    }
    rows_to_csv(Path(f"{PREFIX}_base_training.csv"), training_rows)
    rows_to_csv(Path(f"{PREFIX}_diagnostic_training.csv"), [diagnostic_training])
    rows_to_csv(Path(f"{PREFIX}_router_selection.csv"), router_selection)
    rows_to_csv(Path(f"{PREFIX}_diagnostic_selection.csv"), diagnostic_selection)
    rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    write_json(Path(f"{PREFIX}_results.json"), payload)
    write_json(Path(f"{PREFIX}_trace.json"), asdict(trace))
    write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_CRISIS_DIAGNOSTIC_MEMORY_RESULTS", payload)
    write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_CRISIS_DIAGNOSTIC_MEMORY_TRACE", asdict(trace))
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
    parser.add_argument("--diagnostic-epochs", type=int, default=54)
    parser.add_argument("--diagnostic-hidden-size", type=int, default=64)
    parser.add_argument("--diagnostic-learning-rate", type=float, default=0.004)
    parser.add_argument("--diagnostic-bias-candidates", default="0.00,0.75,1.25,1.75,2.50,3.50,5.00,8.00,12.00,20.00")
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
        diagnostic_epochs=args.diagnostic_epochs,
        diagnostic_hidden_size=args.diagnostic_hidden_size,
        diagnostic_learning_rate=args.diagnostic_learning_rate,
        diagnostic_bias_candidates=parse_floats(args.diagnostic_bias_candidates),
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({
        "diagnostic_selection": payload["diagnostic_selection"],
        "verdict": payload["verdict"],
        "summary": payload["summary"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
