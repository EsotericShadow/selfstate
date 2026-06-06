"""Runner for the SSRM-3D multi-day maturation benchmark."""

from __future__ import annotations

import random
from typing import List, Tuple

from .agents import make_agents, mature_children, maybe_reproduce, update_agents
from .artifacts import write_artifacts
from .environment import clamp, initialize_shock_schedule, living, maybe_major_shock, mean, pressure_components, set_tiers, update_environment
from .metrics import summarize, verdict_from_summary
from .models import CONDITIONS, Agent, Config, Condition, EpisodeRow, Trace, TraceFrame, World


TRACE_CHECKPOINTS = (0.0, 3.0, 6.0, 9.0, 12.0, 18.0, 24.0, 36.0, 48.0, 60.0, 72.0)


def make_world(rng: random.Random) -> World:
    world = World()
    world.food += rng.uniform(-0.03, 0.03)
    world.water += rng.uniform(-0.03, 0.03)
    world.materials += rng.uniform(-0.04, 0.04)
    world.shelter += rng.uniform(-0.03, 0.03)
    initialize_shock_schedule(world, rng)
    set_tiers(world)
    return world


def snapshot(world: World, agents: List[Agent], label: str, events: List[str]) -> TraceFrame:
    alive = living(agents)
    children = [agent for agent in alive if agent.child]
    return {
        "label": label,
        "hours": round(world.time, 3),
        "alive": len(alive),
        "total_agents": len(agents),
        "children": len(children),
        "births": world.births,
        "deaths": world.deaths,
        "major_shocks": world.major_shocks,
        "next_shock": round(world.next_shock, 3),
        "weather": world.weather,
        "food": world.food,
        "water": world.water,
        "materials": world.materials,
        "medicine": world.medicine,
        "shelter": world.shelter,
        "architecture": world.architecture,
        "architecture_tier": world.architecture_tier,
        "tools": world.tools,
        "tool_tier": world.tool_tier,
        "workshop": world.workshop,
        "waterworks": world.waterworks,
        "granary": world.granary,
        "paths": world.paths,
        "sanitation": world.sanitation,
        "garden": world.garden,
        "culture": world.culture,
        "symbols": world.symbols,
        "risk_memory": world.risk_memory,
        "map_knowledge": world.map_knowledge,
        "contamination": world.contamination,
        "disease": world.disease,
        "predators": world.predators,
        "route_hazard": world.route_hazard,
        "resource_migration": world.resource_migration,
        "adaptive_pressure": world.adaptive_pressure,
        "pressure_integral": world.pressure_integral,
        "adaptation_evidence": world.adaptation_evidence,
        "knowledge_transfer": world.knowledge_transfer,
        "mean_wisdom": mean(agent.wisdom for agent in alive),
        "mean_health": mean(agent.health for agent in alive),
        "mean_energy": mean(agent.energy for agent in alive),
        "mean_age": mean(agent.age_hours for agent in alive),
        "actions": {action: sum(1 for agent in alive if agent.action == action) for action in sorted({agent.action for agent in alive})},
        "events": events[-6:],
    }


def score_episode(world: World, agents: List[Agent], baseline: dict[str, float], at_12: dict[str, float], seed: int, condition: Condition, alive_at_12h: int, no_pre_gate_shock: bool) -> EpisodeRow:
    alive = living(agents)
    final_alive = len(alive)
    total_agents = len(agents)
    architecture_delta = world.architecture - baseline["architecture"]
    tool_delta = world.tools + world.workshop * 0.45 + world.fire_control * 0.30 - baseline["tool_system"]
    culture_delta = world.culture + world.symbols * 0.50 - baseline["culture_system"]
    risk_delta = world.risk_memory - baseline["risk_memory"]
    survival_score = clamp(final_alive / max(1, total_agents) * 0.72 + min(1.0, final_alive / max(1, baseline["population"])) * 0.28)
    architecture_progress = clamp(
        max(0.0, architecture_delta) * 0.60
        + max(0.0, world.waterworks - baseline["waterworks"]) * 0.14
        + max(0.0, world.granary - baseline["granary"]) * 0.12
        + max(0.0, world.paths - baseline["paths"]) * 0.12
        + world.architecture_tier * 0.06
    )
    tool_progress = clamp(max(0.0, tool_delta) * 0.55 + world.tool_tier * 0.12)
    development_score = clamp(architecture_progress * 0.58 + tool_progress * 0.42)
    knowledge_score = clamp(world.knowledge_transfer * 0.72 + max(0.0, culture_delta) * 0.50 + mean(agent.wisdom for agent in alive) * 0.16 + world.symbols * 0.16)
    recovery_score = clamp((1.0 if world.major_shocks > 0 else 0.0) * 0.18 + survival_score * 0.24 + world.adaptation_evidence * 0.28 + world.risk_memory * 0.16 + max(0.0, 0.62 - world.disease) * 0.08 + max(0.0, 0.62 - world.predators) * 0.08)
    maturation_score = clamp(survival_score * 0.24 + development_score * 0.27 + knowledge_score * 0.23 + recovery_score * 0.18 + world.births * 0.025 + world.adaptation_evidence * 0.08)
    return EpisodeRow(
        seed=seed,
        condition=condition.name,
        final_alive=final_alive,
        total_agents=total_agents,
        alive_at_12h=alive_at_12h,
        no_major_shock_before_12h=no_pre_gate_shock,
        post_gate_shock=world.major_shocks > 0,
        major_shocks=world.major_shocks,
        first_shock_hour=world.first_shock_hour or 0.0,
        births=world.births,
        deaths=world.deaths,
        architecture_tier=world.architecture_tier,
        tool_tier=world.tool_tier,
        architecture_delta=architecture_delta,
        tool_delta=tool_delta,
        culture_delta=culture_delta,
        risk_memory_delta=risk_delta,
        knowledge_transfer=world.knowledge_transfer,
        adaptation_evidence=world.adaptation_evidence,
        pressure_integral=world.pressure_integral,
        development_at_12h=at_12.get("development", 0.0),
        knowledge_at_12h=at_12.get("knowledge", 0.0),
        survival_score=survival_score,
        development_score=development_score,
        knowledge_score=knowledge_score,
        recovery_score=recovery_score,
        maturation_score=maturation_score,
    )


def run_episode(seed: int, condition: Condition, cfg: Config, *, trace: bool = False) -> Tuple[EpisodeRow, Trace]:
    rng = random.Random(seed * 97 + sum(ord(ch) for ch in condition.name))
    agents = make_agents(rng, cfg.population)
    world = make_world(rng)
    baseline = {
        "architecture": world.architecture,
        "tool_system": world.tools + world.workshop * 0.45 + world.fire_control * 0.30,
        "culture_system": world.culture + world.symbols * 0.50,
        "risk_memory": world.risk_memory,
        "waterworks": world.waterworks,
        "granary": world.granary,
        "paths": world.paths,
        "population": float(cfg.population),
    }
    events: List[str] = []
    trace_out = Trace(seed=seed, condition=condition.name)
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
        world.time += dt
        update_environment(world, agents, condition, dt, rng)
        shock = maybe_major_shock(world, rng)
        if shock:
            events.append(f"{world.time:.1f}h: {shock.replace('_', ' ')} shock")
        pressure = pressure_components(world, agents)
        alpha = min(0.10, max(0.004, dt / 1.5))
        world.adaptive_pressure = clamp(world.adaptive_pressure * (1.0 - alpha) + pressure["total"] * alpha)
        world.pressure_integral = clamp(world.pressure_integral + pressure["total"] * dt / max(1.0, cfg.hours))
        update_agents(world, agents, condition, dt, rng)
        mature_children(agents)
        before_births = world.births
        maybe_reproduce(world, agents, condition, rng, dt)
        if world.births > before_births:
            events.append(f"{world.time:.1f}h: new generation born")

        if world.time < 12.0 and world.major_shocks > 0:
            no_pre_gate_shock = False
        if world.time >= 12.0 and not at_12:
            alive_at_12h = len(living(agents))
            at_12 = {
                "development": clamp((world.architecture - baseline["architecture"]) * 0.48 + (world.tools + world.workshop * 0.45 + world.fire_control * 0.30 - baseline["tool_system"]) * 0.34 + (world.paths - baseline["paths"]) * 0.16),
                "knowledge": clamp(world.knowledge_transfer * 0.80 + (world.culture + world.symbols * 0.50 - baseline["culture_system"]) * 0.45),
            }
        while trace and checkpoints and world.time >= checkpoints[0] - 1e-9:
            hour = checkpoints.pop(0)
            trace_out.frames.append(snapshot(world, agents, f"{hour:g}h", events))

    if trace and (not trace_out.frames or trace_out.frames[-1]["hours"] < cfg.hours):
        trace_out.frames.append(snapshot(world, agents, f"{cfg.hours:g}h", events))
    return score_episode(world, agents, baseline, at_12, seed, condition, alive_at_12h, no_pre_gate_shock), trace_out


def run_benchmark(cfg: Config) -> dict[str, object]:
    rows: List[EpisodeRow] = []
    trace = Trace(seed=cfg.trace_seed, condition="integrated_maturation")
    for seed in cfg.seeds:
        for condition in CONDITIONS:
            row, maybe_trace = run_episode(seed, condition, cfg, trace=(seed == cfg.trace_seed and condition.name == "integrated_maturation"))
            rows.append(row)
            if maybe_trace.frames:
                trace = maybe_trace
    summary = summarize(rows)
    verdict = verdict_from_summary(summary)
    return write_artifacts(rows, summary, verdict, trace, cfg)
