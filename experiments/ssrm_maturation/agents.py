"""Agent lifecycle, action choice, and action effects for maturation runs."""

from __future__ import annotations

import random
from typing import List

from .environment import clamp, living, mean
from .models import Agent, Condition, World


def make_agents(rng: random.Random, population: int) -> List[Agent]:
    agents: List[Agent] = []
    for index in range(population):
        resilience = 0.34 + rng.random() * 0.50
        dexterity = 0.34 + rng.random() * 0.48
        sociability = 0.30 + rng.random() * 0.52
        curiosity = 0.30 + rng.random() * 0.52
        agents.append(
            Agent(
                ident=f"A{index + 1:02d}",
                generation=0,
                age_hours=18.0 + rng.random() * 26.0,
                max_life_hours=96.0 + resilience * 54.0 + rng.random() * 18.0,
                resilience=resilience,
                dexterity=dexterity,
                sociability=sociability,
                curiosity=curiosity,
                health=0.86 + rng.random() * 0.10,
                energy=0.68 + rng.random() * 0.18,
                hunger=0.20 + rng.random() * 0.12,
                thirst=0.20 + rng.random() * 0.12,
                stress=0.12 + rng.random() * 0.12,
                fear=0.10 + rng.random() * 0.12,
                injury=0.02 + rng.random() * 0.05,
                illness=0.04 + rng.random() * 0.06,
                attachment=0.40 + sociability * 0.30,
                wisdom=0.06 + rng.random() * 0.12,
                build_skill=0.08 + resilience * 0.12 + rng.random() * 0.08,
                tool_skill=0.08 + dexterity * 0.13 + rng.random() * 0.08,
                harvest_skill=0.10 + dexterity * 0.10 + rng.random() * 0.08,
                care_skill=0.08 + sociability * 0.11 + rng.random() * 0.08,
                teach_skill=0.07 + sociability * 0.13 + rng.random() * 0.08,
                scout_skill=0.08 + curiosity * 0.13 + rng.random() * 0.08,
            )
        )
    return agents


def perceived(value: float, condition: Condition, noise: float, rng: random.Random) -> float:
    if condition.environmental_sensing:
        return clamp(value + rng.uniform(-noise, noise))
    return clamp(0.46 + rng.uniform(-noise * 1.8, noise * 1.8))


def choose_action(agent: Agent, world: World, condition: Condition, rng: random.Random) -> str:
    if condition.name == "reactive_survival_only":
        if agent.energy < 0.22 or agent.health < 0.46:
            return "rest"
        if agent.illness > 0.42:
            return "treat"
        return "collect_water" if world.water < world.food or agent.thirst > agent.hunger else "harvest_food"

    if agent.child:
        if agent.energy < 0.36 or agent.health < 0.64:
            return "rest"
        return "learn" if condition.teaching and world.culture > 0.18 else "stay_near_shelter"

    route_hazard = perceived(world.route_hazard, condition, 0.04, rng)
    disease = perceived(world.disease + world.contamination, condition, 0.04, rng)
    scarcity = max(1.0 - world.food, 1.0 - world.water)
    urgent = max(agent.thirst, agent.hunger, max(0.0, 0.40 - world.water) * 1.50, max(0.0, 0.40 - world.food) * 1.35, max(0.0, 0.40 - agent.health) * 1.50)
    if urgent > 0.62:
        if agent.energy < 0.18 or agent.health < 0.38:
            return "rest"
        return "collect_water" if world.water < world.food or agent.thirst > agent.hunger else "harvest_food"
    if disease > 0.48 or agent.illness > 0.38:
        return "sanitize" if world.sanitation < 0.48 else "treat"
    if route_hazard > 0.42 or world.map_knowledge < 0.36 or world.terrain_knowledge < 0.32:
        return "scout"
    if condition.future_planning and (world.architecture < 0.68 or world.waterworks < 0.56 or world.granary < 0.52 or world.paths < 0.52):
        return "construct"
    if condition.tool_improvement and (world.tools < 0.72 or world.workshop < 0.56 or world.fire_control < 0.44):
        return "improve_tools"
    if condition.social_learning and (world.conflict > 0.30 or world.social_trust < 0.58 or world.symbols < 0.42):
        return "social_repair"
    if condition.teaching and (world.culture < 0.74 or world.risk_memory < 0.62) and rng.random() < 0.52:
        return "teach"
    if scarcity > 0.46:
        return "collect_water" if world.water < world.food else "harvest_food"
    if agent.energy < 0.34 or agent.stress > 0.64:
        return "rest"
    return rng.choice(("construct", "improve_tools", "teach", "scout", "sanitize", "harvest_food", "collect_water"))


def action_success(agent: Agent, world: World, base_skill: float, condition: Condition, rng: random.Random) -> float:
    tool_bonus = world.tools * 0.18 + world.workshop * 0.12 + world.tool_tier * 0.04
    culture_bonus = world.culture * 0.10 if condition.social_learning else 0.0
    risk_bonus = world.risk_memory * 0.07 if condition.risk_memory else 0.0
    return clamp(agent.energy * 0.22 + agent.health * 0.18 + base_skill * 0.34 + tool_bonus + culture_bonus + risk_bonus + rng.random() * 0.12 - agent.stress * 0.08 - agent.injury * 0.07)


def apply_action(agent: Agent, world: World, agents: List[Agent], condition: Condition, action: str, dt: float, rng: random.Random) -> None:
    agent.action = action
    evidence = 0.0
    if action == "harvest_food":
        success = action_success(agent, world, agent.harvest_skill, condition, rng)
        gain = (0.018 + success * 0.046 + world.garden * 0.014 + world.granary * 0.014 - world.resource_migration * 0.006) * dt
        world.food = clamp(world.food + gain)
        agent.hunger = clamp(agent.hunger - success * 0.12 * dt)
        agent.harvest_skill = clamp(agent.harvest_skill + success * 0.007 * dt)
        evidence = success * 0.04
    elif action == "collect_water":
        success = action_success(agent, world, agent.harvest_skill, condition, rng)
        gain = (0.018 + success * 0.050 + world.waterworks * 0.018 - world.contamination * 0.006) * dt
        world.water = clamp(world.water + gain)
        agent.thirst = clamp(agent.thirst - success * 0.13 * dt)
        agent.harvest_skill = clamp(agent.harvest_skill + success * 0.006 * dt)
        evidence = success * 0.04
    elif action == "construct":
        success = action_success(agent, world, agent.build_skill, condition, rng)
        persistence = 1.0 if condition.infrastructure_memory else 0.045
        world.materials = clamp(world.materials - success * 0.010 * dt)
        world.shelter = clamp(world.shelter + success * 0.028 * persistence * dt)
        world.architecture = clamp(world.architecture + success * 0.026 * persistence * dt)
        world.waterworks = clamp(world.waterworks + success * 0.022 * persistence * dt)
        world.granary = clamp(world.granary + success * 0.020 * persistence * dt)
        world.paths = clamp(world.paths + success * 0.020 * persistence * dt)
        world.garden = clamp(world.garden + success * 0.014 * persistence * dt)
        agent.build_skill = clamp(agent.build_skill + success * 0.009 * dt)
        evidence = success * 0.12
    elif action == "improve_tools":
        success = action_success(agent, world, agent.tool_skill, condition, rng)
        world.materials = clamp(world.materials - success * 0.010 * dt)
        if condition.tool_improvement:
            world.tools = clamp(world.tools + success * 0.032 * dt)
            world.workshop = clamp(world.workshop + success * 0.026 * dt)
            world.fire_control = clamp(world.fire_control + success * 0.018 * dt)
        else:
            world.tools = clamp(world.tools + success * 0.006 * dt)
        agent.tool_skill = clamp(agent.tool_skill + success * 0.010 * dt)
        evidence = success * 0.11
    elif action == "sanitize":
        success = action_success(agent, world, agent.care_skill, condition, rng)
        world.sanitation = clamp(world.sanitation + success * 0.036 * dt)
        world.contamination = clamp(world.contamination - success * 0.040 * dt)
        world.disease = clamp(world.disease - success * 0.026 * dt)
        agent.care_skill = clamp(agent.care_skill + success * 0.008 * dt)
        evidence = success * 0.08
    elif action == "treat":
        success = action_success(agent, world, agent.care_skill, condition, rng)
        world.medicine = clamp(world.medicine - success * 0.004 * dt)
        world.disease = clamp(world.disease - success * 0.030 * dt)
        agent.health = clamp(agent.health + success * 0.040 * dt)
        agent.illness = clamp(agent.illness - success * 0.060 * dt)
        agent.care_skill = clamp(agent.care_skill + success * 0.007 * dt)
        evidence = success * 0.08
    elif action == "scout":
        success = action_success(agent, world, agent.scout_skill, condition, rng)
        if rng.random() < world.route_hazard * (0.010 if condition.risk_memory else 0.028) * dt:
            agent.injury = clamp(agent.injury + 0.12)
            agent.fear = clamp(agent.fear + 0.18)
        world.map_knowledge = clamp(world.map_knowledge + success * 0.040 * dt)
        world.terrain_knowledge = clamp(world.terrain_knowledge + success * 0.036 * dt)
        if condition.risk_memory:
            world.risk_memory = clamp(world.risk_memory + success * 0.018 * dt + world.route_hazard * 0.012 * dt)
        agent.scout_skill = clamp(agent.scout_skill + success * 0.009 * dt)
        evidence = success * 0.10
    elif action == "teach":
        success = action_success(agent, world, agent.teach_skill, condition, rng)
        if condition.teaching:
            if condition.social_learning:
                world.culture = clamp(world.culture + success * 0.036 * dt)
                world.symbols = clamp(world.symbols + success * 0.026 * dt)
            world.risk_memory = clamp(world.risk_memory + success * 0.022 * dt if condition.risk_memory else world.risk_memory)
            world.knowledge_transfer = clamp(world.knowledge_transfer + success * 0.034 * dt)
            for other in living(agents):
                if other is agent:
                    continue
                shared = success * (0.0035 if other.child else 0.0018) * dt
                other.build_skill = clamp(other.build_skill + agent.build_skill * shared)
                other.tool_skill = clamp(other.tool_skill + agent.tool_skill * shared)
                other.harvest_skill = clamp(other.harvest_skill + agent.harvest_skill * shared)
                other.wisdom = clamp(other.wisdom + success * 0.0025 * dt)
        agent.teach_skill = clamp(agent.teach_skill + success * 0.009 * dt)
        evidence = success * 0.10
    elif action == "social_repair":
        success = action_success(agent, world, agent.teach_skill * 0.45 + agent.care_skill * 0.35 + agent.sociability * 0.20, condition, rng)
        if condition.social_learning:
            world.social_trust = clamp(world.social_trust + success * 0.034 * dt)
            world.conflict = clamp(world.conflict - success * 0.034 * dt)
            world.culture = clamp(world.culture + success * 0.016 * dt)
            world.symbols = clamp(world.symbols + success * 0.010 * dt)
            for other in living(agents):
                other.attachment = clamp(other.attachment + success * 0.002 * dt)
        else:
            world.conflict = clamp(world.conflict - success * 0.008 * dt)
        evidence = success * 0.07
    elif action == "learn":
        success = clamp(world.culture * 0.36 + world.symbols * 0.22 + agent.sociability * 0.16 + rng.random() * 0.12)
        agent.wisdom = clamp(agent.wisdom + success * 0.012 * dt)
        agent.build_skill = clamp(agent.build_skill + world.architecture * 0.006 * dt)
        agent.tool_skill = clamp(agent.tool_skill + world.tools * 0.006 * dt)
        agent.harvest_skill = clamp(agent.harvest_skill + world.map_knowledge * 0.005 * dt)
        world.knowledge_transfer = clamp(world.knowledge_transfer + success * 0.010 * dt)
        evidence = success * 0.05
    elif action == "rest" or action == "stay_near_shelter":
        safety = clamp(world.shelter * 0.35 + world.architecture * 0.18 + world.fire_control * 0.10 + 0.25)
        agent.energy = clamp(agent.energy + safety * 0.16 * dt)
        agent.health = clamp(agent.health + safety * 0.018 * dt)
        agent.stress = clamp(agent.stress - safety * 0.060 * dt)
    world.adaptation_evidence = clamp(world.adaptation_evidence + evidence * (0.52 + world.adaptive_pressure * 0.48) * dt)
    agent.wisdom = clamp(agent.wisdom + evidence * 0.018 * dt)
    agent.energy = clamp(agent.energy - (0.012 if action not in {"rest", "stay_near_shelter"} else 0.003) * dt)
    agent.stress = clamp(agent.stress + world.adaptive_pressure * 0.006 * dt + world.conflict * 0.010 * dt - world.culture * 0.006 * dt)


def update_agents(world: World, agents: List[Agent], condition: Condition, dt: float, rng: random.Random) -> None:
    for agent in living(agents):
        agent.age_hours += dt
        action = choose_action(agent, world, condition, rng)
        apply_action(agent, world, agents, condition, action, dt, rng)

    for agent in living(agents):
        age_pressure = max(0.0, agent.age_hours - agent.max_life_hours * 0.72) / max(1.0, agent.max_life_hours * 0.28)
        thermal = abs(world.temperature - 0.55) * 0.012
        shelter_protection = world.shelter * 0.014 + world.architecture * 0.006
        agent.hunger = clamp(agent.hunger + (0.012 + thermal + agent.stress * 0.003) * dt - (world.food + world.granary * 0.30) * 0.010 * dt)
        agent.thirst = clamp(agent.thirst + (0.014 + max(0.0, world.temperature - 0.62) * 0.018 + agent.stress * 0.003) * dt - (world.water + world.waterworks * 0.26) * 0.012 * dt)
        agent.illness = clamp(agent.illness + (world.disease * 0.024 + world.contamination * 0.016 - world.sanitation * 0.014) * dt)
        agent.injury = clamp(agent.injury - (world.medicine + world.shelter) * 0.008 * dt)
        agent.fear = clamp(agent.fear + (world.predators + world.route_hazard) * 0.014 * dt - (world.risk_memory + world.social_trust) * 0.014 * dt)
        health_loss = max(0.0, agent.hunger - 0.88) * 0.24 + max(0.0, agent.thirst - 0.88) * 0.30 + agent.illness * 0.030 + agent.injury * 0.018 + age_pressure * 0.016
        agent.health = clamp(agent.health - max(0.0, health_loss - shelter_protection) * dt)
        agent.energy = clamp(agent.energy - (0.004 + age_pressure * 0.010 + max(0.0, world.shelter - 0.62) * -0.003) * dt)
        if agent.health <= 0.03 or agent.thirst >= 0.995 or agent.age_hours > agent.max_life_hours:
            agent.alive = False
            world.deaths += 1


def maybe_reproduce(world: World, agents: List[Agent], condition: Condition, rng: random.Random, dt: float) -> None:
    if not condition.reproduction or world.time < 18.0 or len(agents) >= 28:
        return
    if world.food < 0.56 or world.water < 0.56 or world.shelter < 0.58 or world.social_trust < 0.46:
        return
    if rng.random() > 0.200 * dt * (0.70 + world.culture):
        return
    adults = [agent for agent in living(agents) if not agent.child and agent.health > 0.72 and agent.energy > 0.40 and agent.age_hours < agent.max_life_hours * 0.74]
    if len(adults) < 2:
        return
    parent_a, parent_b = rng.sample(adults, 2)
    lineage = 0.0
    if condition.teaching:
        lineage = clamp(world.culture * 0.16 + world.knowledge_transfer * 0.12 + mean((parent_a.wisdom, parent_b.wisdom)) * 0.10)
    child = Agent(
        ident=f"G{max(agent.generation for agent in agents) + 1}-{world.births + 1:02d}",
        generation=max(parent_a.generation, parent_b.generation) + 1,
        age_hours=0.0,
        max_life_hours=96.0 + mean((parent_a.resilience, parent_b.resilience)) * 54.0 + rng.random() * 18.0,
        resilience=clamp(mean((parent_a.resilience, parent_b.resilience)) + rng.uniform(-0.04, 0.04)),
        dexterity=clamp(mean((parent_a.dexterity, parent_b.dexterity)) + rng.uniform(-0.04, 0.04)),
        sociability=clamp(mean((parent_a.sociability, parent_b.sociability)) + rng.uniform(-0.04, 0.04)),
        curiosity=clamp(mean((parent_a.curiosity, parent_b.curiosity)) + rng.uniform(-0.04, 0.04)),
        health=0.70,
        energy=0.56,
        hunger=0.34,
        thirst=0.34,
        stress=0.20,
        fear=0.18,
        injury=0.0,
        illness=0.03,
        attachment=0.82,
        wisdom=lineage * 0.36,
        build_skill=0.05 + lineage,
        tool_skill=0.05 + lineage,
        harvest_skill=0.07 + lineage,
        care_skill=0.05 + lineage,
        teach_skill=0.05 + lineage,
        scout_skill=0.05 + lineage,
        child=True,
    )
    parent_a.energy = clamp(parent_a.energy - 0.08)
    parent_b.energy = clamp(parent_b.energy - 0.06)
    parent_a.stress = clamp(parent_a.stress + 0.04)
    parent_b.stress = clamp(parent_b.stress + 0.03)
    world.births += 1
    if condition.teaching:
        world.knowledge_transfer = clamp(world.knowledge_transfer + lineage * 0.45)
    agents.append(child)


def mature_children(agents: List[Agent]) -> None:
    for agent in agents:
        if agent.child and agent.alive and agent.age_hours >= 16.0:
            agent.child = False
            agent.energy = clamp(agent.energy + 0.12)
