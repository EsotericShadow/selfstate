#!/usr/bin/env python3
"""Coupled social/environment pressure for the SSRM-3D multi-day controller.

Report 105 selected a pressure router by validation return, but social/culture
and environmental ablations still did not damage total score. This benchmark
keeps the 72h maturation world and makes the post-12h shocks less substitutable:
each coupled crisis requires both environmental response and social coordination.

The controller still starts from supervised imitation. The new return step
selects a router by closed-loop validation outcome in the coupled-crisis world.
This is not deep reinforcement learning and it does not claim consciousness.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import statistics
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import torch

import ssrm_3d_learned_multiday_maturation_controller as base
import ssrm_3d_return_selected_multiday_maturation_controller as report105
from ssrm_maturation.agents import choose_action, make_agents
from ssrm_maturation.benchmark import TRACE_CHECKPOINTS, make_world, score_episode, snapshot
from ssrm_maturation.environment import clamp, living
from ssrm_maturation.models import CONDITIONS, Agent, Condition, Trace, World


ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
PREFIX = ARTIFACT_DIR / "ssrm_3d_coupled_social_environment_maturation"


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
    device: str = "auto"
    trace_seed: int = 20260971


@dataclass(frozen=True)
class CrisisProfile:
    name: str
    env_actions: Tuple[str, ...]
    social_actions: Tuple[str, ...]
    env_need: float
    social_need: float
    contamination_rate: float = 0.0
    disease_rate: float = 0.0
    conflict_rate: float = 0.0
    trust_loss_rate: float = 0.0
    route_rate: float = 0.0
    predator_rate: float = 0.0
    migration_rate: float = 0.0
    water_loss_rate: float = 0.0
    food_loss_rate: float = 0.0
    shelter_loss_rate: float = 0.0
    visibility_loss_rate: float = 0.0


@dataclass
class ActiveCrisis:
    profile: CrisisProfile
    start: float
    duration: float
    severity: float
    env_progress: float = 0.0
    social_progress: float = 0.0
    steps: int = 0
    env_response_steps: int = 0
    social_response_steps: int = 0
    coupled_response_steps: int = 0

    @property
    def end(self) -> float:
        return self.start + self.duration


@dataclass
class CrisisTracker:
    schedule: List[Tuple[float, CrisisProfile]]
    active: Optional[ActiveCrisis] = None
    index: int = 0
    started: int = 0
    resolved: int = 0
    unresolved: int = 0
    env_response_steps: int = 0
    social_response_steps: int = 0
    coupled_response_steps: int = 0
    crisis_steps: int = 0
    damage_integral: float = 0.0
    response_log: List[dict[str, object]] = field(default_factory=list)


@dataclass(frozen=True)
class SelectionRow:
    router: str
    social_bias: float
    environment_bias: float
    infrastructure_bias: float
    tool_bias: float
    teaching_bias: float
    tune_total_score: float
    tune_maturation_score: float
    tune_crisis_score: float
    tune_resolved_rate: float
    tune_coupled_response: float
    tune_damage: float
    selection_objective: float
    selected: bool


@dataclass(frozen=True)
class EvalRow:
    seed: int
    controller: str
    ablation: str
    total_score: float
    maturation_score: float
    crisis_score: float
    resolved_rate: float
    unresolved_count: int
    env_response_rate: float
    social_response_rate: float
    coupled_response_rate: float
    crisis_damage: float
    final_alive: int
    total_agents: int
    alive_at_12h: int
    no_major_shock_before_12h: bool
    post_gate_shock: bool
    births: int
    deaths: int
    architecture_tier: int
    tool_tier: int
    knowledge_transfer: float
    adaptation_evidence: float
    survival_score: float
    development_score: float
    knowledge_score: float
    recovery_score: float


@dataclass(frozen=True)
class SummaryRow:
    controller: str
    ablation: str
    mean_total_score: float
    mean_maturation_score: float
    mean_crisis_score: float
    mean_resolved_rate: float
    mean_env_response_rate: float
    mean_social_response_rate: float
    mean_coupled_response_rate: float
    mean_crisis_damage: float
    mean_final_alive: float
    mean_alive_at_12h: float
    mean_births: float
    mean_architecture_tier: float
    mean_tool_tier: float
    mean_knowledge_transfer: float
    mean_adaptation_evidence: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float


@dataclass(frozen=True)
class AblationRow:
    ablation: str
    mean_total_score: float
    total_loss: float
    crisis_score_loss: float
    resolved_rate_loss: float
    env_response_loss: float
    social_response_loss: float
    coupled_response_loss: float
    damage_increase: float


@dataclass(frozen=True)
class VerdictRow:
    selected_router: str
    selected_total_score: float
    base_gru_total_score: float
    designed_total_score: float
    frame_total_score: float
    reactive_total_score: float
    gain_over_base_gru: float
    gain_over_frame: float
    gain_over_reactive: float
    gap_to_designed: float
    selected_crisis_score: float
    selected_resolved_rate: float
    selected_coupled_response: float
    social_culture_total_loss: float
    environment_total_loss: float
    social_culture_coupled_loss: float
    environment_coupled_loss: float
    shock_gate_pass_rate: float
    post_gate_shock_rate: float
    survival_at_12h: float
    supports_coupled_return_selection: bool
    supports_social_environment_dependency: bool
    verdict: str


PROFILES = (
    CrisisProfile(
        name="contaminated_water_trust",
        env_actions=("sanitize", "treat"),
        social_actions=("social_repair", "teach"),
        env_need=0.92,
        social_need=0.70,
        contamination_rate=0.036,
        disease_rate=0.030,
        conflict_rate=0.016,
        trust_loss_rate=0.016,
        water_loss_rate=0.014,
    ),
    CrisisProfile(
        name="route_migration_dispute",
        env_actions=("scout", "harvest_food", "collect_water"),
        social_actions=("social_repair", "teach"),
        env_need=0.98,
        social_need=0.72,
        route_rate=0.034,
        migration_rate=0.040,
        predator_rate=0.020,
        conflict_rate=0.020,
        food_loss_rate=0.014,
        water_loss_rate=0.010,
    ),
    CrisisProfile(
        name="storm_shelter_coordination",
        env_actions=("construct", "scout"),
        social_actions=("social_repair", "teach"),
        env_need=1.04,
        social_need=0.76,
        shelter_loss_rate=0.034,
        route_rate=0.018,
        conflict_rate=0.018,
        trust_loss_rate=0.012,
        visibility_loss_rate=0.032,
    ),
    CrisisProfile(
        name="quarantine_rumor",
        env_actions=("sanitize", "treat"),
        social_actions=("social_repair", "teach", "learn"),
        env_need=0.90,
        social_need=0.92,
        disease_rate=0.032,
        contamination_rate=0.022,
        conflict_rate=0.038,
        trust_loss_rate=0.030,
    ),
)


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return statistics.fmean(values) if values else 0.0


def crisis_schedule(seed: int) -> List[Tuple[float, CrisisProfile]]:
    starts = (14.0, 27.0, 42.0, 57.0)
    offset = seed % len(PROFILES)
    return [(start, PROFILES[(offset + index) % len(PROFILES)]) for index, start in enumerate(starts)]


def prepare_world(rng: random.Random, cfg: Config) -> World:
    world = make_world(rng)
    world.food = clamp(world.food - 0.05)
    world.water = clamp(world.water - 0.04)
    world.social_trust = clamp(world.social_trust - 0.05)
    world.conflict = clamp(world.conflict + 0.04)
    world.contamination = clamp(world.contamination + 0.04)
    world.route_hazard = clamp(world.route_hazard + 0.04)
    world.resource_migration = clamp(world.resource_migration + 0.06)
    world.next_shock = cfg.hours + 100.0
    return world


def maybe_start_crisis(world: World, tracker: CrisisTracker, rng: random.Random, events: List[str]) -> None:
    if tracker.active is not None or tracker.index >= len(tracker.schedule):
        return
    start, profile = tracker.schedule[tracker.index]
    if world.time < start:
        return
    tracker.index += 1
    tracker.started += 1
    severity = 0.90 + rng.random() * 0.20
    tracker.active = ActiveCrisis(profile=profile, start=world.time, duration=7.8, severity=severity)
    world.major_shocks += 1
    if world.first_shock_hour is None:
        world.first_shock_hour = world.time
    world.adaptive_pressure = clamp(world.adaptive_pressure + 0.12)
    world.risk_memory = clamp(world.risk_memory + 0.06)
    events.append(f"{world.time:.1f}h: coupled {profile.name.replace('_', ' ')} crisis")


def apply_crisis_symptoms(world: World, active: ActiveCrisis, dt: float) -> None:
    profile = active.profile
    scale = active.severity * dt
    world.contamination = clamp(world.contamination + profile.contamination_rate * scale)
    world.disease = clamp(world.disease + profile.disease_rate * scale)
    world.conflict = clamp(world.conflict + profile.conflict_rate * scale)
    world.social_trust = clamp(world.social_trust - profile.trust_loss_rate * scale)
    world.route_hazard = clamp(world.route_hazard + profile.route_rate * scale)
    world.predators = clamp(world.predators + profile.predator_rate * scale)
    world.resource_migration = clamp(world.resource_migration + profile.migration_rate * scale)
    world.water = clamp(world.water - profile.water_loss_rate * scale)
    world.food = clamp(world.food - profile.food_loss_rate * scale)
    world.shelter = clamp(world.shelter - profile.shelter_loss_rate * scale)
    world.visibility = clamp(world.visibility - profile.visibility_loss_rate * scale)


def complete_crisis_if_due(world: World, agents: List[Agent], tracker: CrisisTracker, events: List[str]) -> None:
    active = tracker.active
    if active is None or world.time < active.end:
        return
    env_fraction = min(1.0, active.env_progress / active.profile.env_need)
    social_fraction = min(1.0, active.social_progress / active.profile.social_need)
    coupled_fraction = min(env_fraction, social_fraction)
    if coupled_fraction >= 0.92:
        tracker.resolved += 1
        world.adaptation_evidence = clamp(world.adaptation_evidence + 0.07 + coupled_fraction * 0.05)
        world.risk_memory = clamp(world.risk_memory + 0.04)
        world.culture = clamp(world.culture + 0.025 * social_fraction)
        world.symbols = clamp(world.symbols + 0.020 * social_fraction)
        events.append(f"{world.time:.1f}h: resolved {active.profile.name.replace('_', ' ')}")
    else:
        tracker.unresolved += 1
        damage = (1.0 - coupled_fraction) * active.severity
        tracker.damage_integral += damage * 0.18
        world.social_trust = clamp(world.social_trust - damage * 0.08)
        world.conflict = clamp(world.conflict + damage * 0.08)
        world.disease = clamp(world.disease + damage * 0.06)
        world.contamination = clamp(world.contamination + damage * 0.04)
        world.shelter = clamp(world.shelter - damage * 0.05)
        for agent in living(agents):
            agent.health = clamp(agent.health - damage * 0.010)
            agent.stress = clamp(agent.stress + damage * 0.040)
        events.append(f"{world.time:.1f}h: unresolved {active.profile.name.replace('_', ' ')}")
    tracker.response_log.append(
        {
            "crisis": active.profile.name,
            "start": round(active.start, 3),
            "end": round(world.time, 3),
            "env_fraction": env_fraction,
            "social_fraction": social_fraction,
            "coupled_fraction": coupled_fraction,
            "resolved": coupled_fraction >= 0.92,
        }
    )
    tracker.active = None


def update_crisis_after_actions(
    world: World,
    agents: List[Agent],
    tracker: CrisisTracker,
    action_counts: Dict[str, int],
    dt: float,
) -> None:
    active = tracker.active
    if active is None:
        return
    alive_count = max(1, len(living(agents)))
    env_effort = sum(action_counts.get(action, 0) for action in active.profile.env_actions) / alive_count
    social_effort = sum(action_counts.get(action, 0) for action in active.profile.social_actions) / alive_count
    active.steps += 1
    tracker.crisis_steps += 1
    active.env_progress += env_effort * dt * 1.55
    active.social_progress += social_effort * dt * 1.65
    env_hit = env_effort >= 0.11
    social_hit = social_effort >= 0.09
    if env_hit:
        active.env_response_steps += 1
        tracker.env_response_steps += 1
    if social_hit:
        active.social_response_steps += 1
        tracker.social_response_steps += 1
    if env_hit and social_hit:
        active.coupled_response_steps += 1
        tracker.coupled_response_steps += 1
        world.adaptation_evidence = clamp(world.adaptation_evidence + 0.004 * dt)
    env_fraction = min(1.0, active.env_progress / active.profile.env_need)
    social_fraction = min(1.0, active.social_progress / active.profile.social_need)
    unresolved = 1.0 - min(env_fraction, social_fraction)
    tracker.damage_integral += unresolved * active.severity * dt / 72.0
    if unresolved > 0.0:
        world.conflict = clamp(world.conflict + active.profile.conflict_rate * unresolved * active.severity * 0.70 * dt)
        world.social_trust = clamp(world.social_trust - active.profile.trust_loss_rate * unresolved * active.severity * 0.70 * dt)
        world.disease = clamp(world.disease + active.profile.disease_rate * unresolved * active.severity * 0.60 * dt)
        world.contamination = clamp(world.contamination + active.profile.contamination_rate * unresolved * active.severity * 0.55 * dt)


def crisis_metrics(tracker: CrisisTracker) -> Tuple[float, float, float, float, float]:
    steps = max(1, tracker.crisis_steps)
    started = max(1, tracker.started)
    env_response = tracker.env_response_steps / steps
    social_response = tracker.social_response_steps / steps
    coupled_response = tracker.coupled_response_steps / steps
    resolved_rate = tracker.resolved / started
    crisis_score = clamp(
        resolved_rate * 0.34
        + env_response * 0.20
        + social_response * 0.20
        + coupled_response * 0.30
        - tracker.damage_integral * 0.35
        - (tracker.unresolved / started) * 0.18
    )
    return crisis_score, resolved_rate, env_response, social_response, coupled_response


def row_lookup(summary: Sequence[SummaryRow], controller: str, ablation: str) -> SummaryRow:
    for row in summary:
        if row.controller == controller and row.ablation == ablation:
            return row
    raise KeyError((controller, ablation))


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
                mean_total_score=mean(row.total_score for row in items),
                mean_maturation_score=mean(row.maturation_score for row in items),
                mean_crisis_score=mean(row.crisis_score for row in items),
                mean_resolved_rate=mean(row.resolved_rate for row in items),
                mean_env_response_rate=mean(row.env_response_rate for row in items),
                mean_social_response_rate=mean(row.social_response_rate for row in items),
                mean_coupled_response_rate=mean(row.coupled_response_rate for row in items),
                mean_crisis_damage=mean(row.crisis_damage for row in items),
                mean_final_alive=mean(row.final_alive for row in items),
                mean_alive_at_12h=mean(row.alive_at_12h for row in items),
                mean_births=mean(row.births for row in items),
                mean_architecture_tier=mean(row.architecture_tier for row in items),
                mean_tool_tier=mean(row.tool_tier for row in items),
                mean_knowledge_transfer=mean(row.knowledge_transfer for row in items),
                mean_adaptation_evidence=mean(row.adaptation_evidence for row in items),
                shock_gate_pass_rate=mean(1.0 if row.no_major_shock_before_12h else 0.0 for row in items),
                post_gate_shock_rate=mean(1.0 if row.post_gate_shock else 0.0 for row in items),
            )
        )
    return summaries


def run_episode(
    seed: int,
    cfg: Config,
    controller: str,
    model: Optional[base.ControllerNet],
    device: torch.device,
    router: report105.PressureRouter,
    ablation: str = "none",
    trace: bool = False,
) -> Tuple[EvalRow, Trace, CrisisTracker]:
    condition = CONDITIONS[1] if controller == "reactive" else CONDITIONS[0]
    rng = random.Random(seed * 101 + sum(ord(ch) for ch in controller + router.name + ablation))
    agents = make_agents(rng, cfg.population)
    world = prepare_world(rng, cfg)
    baseline = base.initial_baseline(world, cfg.population)
    previous_actions: Dict[str, int] = {}
    recurrent_states: Dict[str, torch.Tensor] = {}
    events: List[str] = []
    tracker = CrisisTracker(schedule=crisis_schedule(seed))
    trace_out = Trace(seed=seed, condition=f"{controller}:{router.name}:{ablation}")
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
        maybe_start_crisis(world, tracker, rng, events)
        if tracker.active is not None:
            apply_crisis_symptoms(world, tracker.active, dt)

        def selector(agent: Agent, current_world: World, current_condition: Condition, current_rng: random.Random, features: List[float], previous: int) -> str:
            if controller == "designed":
                action = choose_action(agent, current_world, current_condition, current_rng)
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
                    action = base.INDEX_TO_ACTION[int(logits.argmax(dim=-1).item())]
            action_counts[action] = action_counts.get(action, 0) + 1
            return action

        base.step_world(world, agents, condition, dt, rng, previous_actions, selector, events)
        update_crisis_after_actions(world, agents, tracker, action_counts, dt)
        complete_crisis_if_due(world, agents, tracker, events)
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
        complete_crisis_if_due(world, agents, tracker, events)
    episode = score_episode(world, agents, baseline, at_12, seed, condition, alive_at_12h, no_pre_gate_shock)
    crisis_score, resolved_rate, env_response, social_response, coupled_response = crisis_metrics(tracker)
    total_score = clamp(episode.maturation_score * 0.52 + crisis_score * 0.48)
    eval_row = EvalRow(
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


def selection_objective(rows: Sequence[EvalRow]) -> Tuple[float, float, float, float, float, float]:
    total = mean(row.total_score for row in rows)
    maturation = mean(row.maturation_score for row in rows)
    crisis = mean(row.crisis_score for row in rows)
    resolved = mean(row.resolved_rate for row in rows)
    coupled = mean(row.coupled_response_rate for row in rows)
    damage = mean(row.crisis_damage for row in rows)
    objective = total + resolved * 0.055 + coupled * 0.045 - damage * 0.20
    return total, maturation, crisis, resolved, coupled, objective


def select_router(cfg: Config, model: base.ControllerNet, device: torch.device) -> Tuple[report105.PressureRouter, List[SelectionRow]]:
    best = report105.ROUTERS[0]
    best_objective = -1.0
    rows: List[SelectionRow] = []
    for router in report105.ROUTERS:
        eval_rows = [run_episode(seed, cfg, "return_selected_gru", model, device, router)[0] for seed in cfg.tune_seeds]
        total, maturation, crisis, resolved, coupled, objective = selection_objective(eval_rows)
        damage = mean(row.crisis_damage for row in eval_rows)
        if objective > best_objective:
            best = router
            best_objective = objective
        rows.append(
            SelectionRow(
                router=router.name,
                social_bias=router.social_bias,
                environment_bias=router.environment_bias,
                infrastructure_bias=router.infrastructure_bias,
                tool_bias=router.tool_bias,
                teaching_bias=router.teaching_bias,
                tune_total_score=total,
                tune_maturation_score=maturation,
                tune_crisis_score=crisis,
                tune_resolved_rate=resolved,
                tune_coupled_response=coupled,
                tune_damage=damage,
                selection_objective=objective,
                selected=False,
            )
        )
    return best, [
        SelectionRow(
            row.router,
            row.social_bias,
            row.environment_bias,
            row.infrastructure_bias,
            row.tool_bias,
            row.teaching_bias,
            row.tune_total_score,
            row.tune_maturation_score,
            row.tune_crisis_score,
            row.tune_resolved_rate,
            row.tune_coupled_response,
            row.tune_damage,
            row.selection_objective,
            row.router == best.name,
        )
        for row in rows
    ]


def ablations_from_summary(summary: Sequence[SummaryRow]) -> List[AblationRow]:
    base_row = row_lookup(summary, "return_selected_gru", "none")
    rows: List[AblationRow] = []
    for ablation in ("body", "infrastructure", "tools", "social_culture", "environment", "previous_action"):
        row = row_lookup(summary, "return_selected_gru", ablation)
        rows.append(
            AblationRow(
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


def verdict_from_summary(summary: Sequence[SummaryRow], ablations: Sequence[AblationRow], selected: report105.PressureRouter) -> VerdictRow:
    selected_row = row_lookup(summary, "return_selected_gru", "none")
    base_gru = row_lookup(summary, "gru", "none")
    designed = row_lookup(summary, "designed", "none")
    frame = row_lookup(summary, "frame_mlp", "none")
    reactive = row_lookup(summary, "reactive", "none")
    by_ablation = {row.ablation: row for row in ablations}
    social = by_ablation["social_culture"]
    environment = by_ablation["environment"]
    supports_selection = (
        selected.name != "none"
        and selected_row.mean_total_score >= 0.60
        and selected_row.mean_total_score - reactive.mean_total_score >= 0.08
        and selected_row.mean_alive_at_12h >= 12.0
        and selected_row.shock_gate_pass_rate == 1.0
        and selected_row.post_gate_shock_rate == 1.0
        and selected_row.mean_resolved_rate >= 0.35
    )
    supports_dependency = (
        social.total_loss >= 0.035
        and environment.total_loss >= 0.035
        and social.coupled_response_loss >= 0.020
        and environment.coupled_response_loss >= 0.020
    )
    return VerdictRow(
        selected_router=selected.name,
        selected_total_score=selected_row.mean_total_score,
        base_gru_total_score=base_gru.mean_total_score,
        designed_total_score=designed.mean_total_score,
        frame_total_score=frame.mean_total_score,
        reactive_total_score=reactive.mean_total_score,
        gain_over_base_gru=selected_row.mean_total_score - base_gru.mean_total_score,
        gain_over_frame=selected_row.mean_total_score - frame.mean_total_score,
        gain_over_reactive=selected_row.mean_total_score - reactive.mean_total_score,
        gap_to_designed=designed.mean_total_score - selected_row.mean_total_score,
        selected_crisis_score=selected_row.mean_crisis_score,
        selected_resolved_rate=selected_row.mean_resolved_rate,
        selected_coupled_response=selected_row.mean_coupled_response_rate,
        social_culture_total_loss=social.total_loss,
        environment_total_loss=environment.total_loss,
        social_culture_coupled_loss=social.coupled_response_loss,
        environment_coupled_loss=environment.coupled_response_loss,
        shock_gate_pass_rate=selected_row.shock_gate_pass_rate,
        post_gate_shock_rate=selected_row.post_gate_shock_rate,
        survival_at_12h=selected_row.mean_alive_at_12h,
        supports_coupled_return_selection=supports_selection,
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

    selected, selection_rows = select_router(cfg, models["gru"], device)
    eval_rows: List[EvalRow] = []
    trace = Trace(seed=cfg.trace_seed, condition=f"return_selected_gru:{selected.name}:none")
    crisis_logs: Dict[str, List[dict[str, object]]] = {}
    for seed in cfg.eval_seeds:
        for controller, model, router in (
            ("designed", None, report105.ROUTERS[0]),
            ("reactive", None, report105.ROUTERS[0]),
            ("frame_mlp", models["frame_mlp"], report105.ROUTERS[0]),
            ("gru", models["gru"], report105.ROUTERS[0]),
            ("return_selected_gru", models["gru"], selected),
        ):
            row, maybe_trace, tracker = run_episode(
                seed,
                cfg,
                controller,
                model,
                device,
                router,
                trace=(seed == cfg.trace_seed and controller == "return_selected_gru"),
            )
            eval_rows.append(row)
            crisis_logs[f"{seed}:{controller}:none"] = tracker.response_log
            if maybe_trace.frames:
                trace = maybe_trace
        for ablation in ("body", "infrastructure", "tools", "social_culture", "environment", "previous_action"):
            row, _, tracker = run_episode(seed, cfg, "return_selected_gru", models["gru"], device, selected, ablation=ablation)
            eval_rows.append(row)
            crisis_logs[f"{seed}:return_selected_gru:{ablation}"] = tracker.response_log

    summary = summarize(eval_rows)
    ablations = ablations_from_summary(summary)
    verdict = verdict_from_summary(summary, ablations, selected)
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
            "device": cfg.device,
            "trace_seed": cfg.trace_seed,
        },
        "crisis_profiles": [asdict(profile) for profile in PROFILES],
        "routers": [asdict(router) for router in report105.ROUTERS],
        "selection": [asdict(row) for row in selection_rows],
        "training": [asdict(row) for row in training_rows],
        "summary": [asdict(row) for row in summary],
        "ablations": [asdict(row) for row in ablations],
        "verdict": asdict(verdict),
        "trace": asdict(trace),
        "crisis_logs": crisis_logs,
        "notes": {
            "claim": "coupled social/environment crisis precursor for multi-day learned control",
            "not_claimed": "deep reinforcement learning, subjective consciousness, or open-ended civilization",
        },
    }
    rows_to_csv(Path(f"{PREFIX}_training.csv"), training_rows)
    rows_to_csv(Path(f"{PREFIX}_selection.csv"), selection_rows)
    rows_to_csv(Path(f"{PREFIX}_eval.csv"), eval_rows)
    rows_to_csv(Path(f"{PREFIX}_summary.csv"), summary)
    rows_to_csv(Path(f"{PREFIX}_ablations.csv"), ablations)
    rows_to_csv(Path(f"{PREFIX}_verdict.csv"), [verdict])
    write_json(Path(f"{PREFIX}_results.json"), payload)
    write_json(Path(f"{PREFIX}_trace.json"), asdict(trace))
    write_js(Path(f"{PREFIX}_results.js"), "SSRM_3D_COUPLED_SOCIAL_ENVIRONMENT_MATURATION_RESULTS", payload)
    write_js(Path(f"{PREFIX}_trace.js"), "SSRM_3D_COUPLED_SOCIAL_ENVIRONMENT_MATURATION_TRACE", asdict(trace))
    return payload


def parse_ints(value: str) -> Tuple[int, ...]:
    return tuple(int(part.strip()) for part in value.split(",") if part.strip())


def parse_args() -> Config:
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-seeds", default="20260911,20260912,20260913,20260914,20260915,20260916")
    parser.add_argument("--tune-seeds", default="20260961,20260962,20260963")
    parser.add_argument("--eval-seeds", default="20260971,20260972,20260973,20260974,20260975")
    parser.add_argument("--hours", type=float, default=72.0)
    parser.add_argument("--step-hours", type=float, default=0.10)
    parser.add_argument("--population", type=int, default=14)
    parser.add_argument("--epochs", type=int, default=42)
    parser.add_argument("--hidden-size", type=int, default=64)
    parser.add_argument("--learning-rate", type=float, default=0.004)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--trace-seed", type=int, default=20260971)
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
        device=args.device,
        trace_seed=args.trace_seed,
    )


def main() -> int:
    cfg = parse_args()
    payload = run_benchmark(cfg)
    print(json.dumps({"selection": payload["selection"], "verdict": payload["verdict"], "summary": payload["summary"]}, indent=2))
    # A failed coupled-crisis verdict is evidence, not a process failure.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
