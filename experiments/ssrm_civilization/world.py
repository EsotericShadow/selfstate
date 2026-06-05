"""World setup and shared utilities for the settlement benchmark."""

from __future__ import annotations

import random
from typing import Dict, Iterable, List

from .models import AgentProfile, AgentState, PolicyConfig, ScenarioSpec, SettlementState


PLACES: Dict[str, tuple[float, float]] = {
    "shelter": (-18.0, -12.0),
    "water_source": (24.0, -8.0),
    "clinic": (-8.0, 22.0),
    "farm": (14.0, 20.0),
    "workshop": (-24.0, 10.0),
    "watchtower": (2.0, -28.0),
    "school": (26.0, 28.0),
    "commons": (-4.0, 0.0),
    "frontier": (34.0, -30.0),
    "trade_gate": (-34.0, -2.0),
}


SCENARIOS = (
    ScenarioSpec(
        name="storm_illness_settlement",
        description="storm damage, illness, and scarce medicine force shelter, clinic, care, and trust tradeoffs",
        storm_pressure=0.78,
        scarcity_pressure=0.46,
        illness_pressure=0.72,
        social_pressure=0.54,
        frontier_pressure=0.30,
        threat_pressure=0.42,
    ),
    ScenarioSpec(
        name="scarcity_conflict_commons",
        description="food and water scarcity create theft, conflict, rationing, roles, and norm pressure",
        storm_pressure=0.30,
        scarcity_pressure=0.84,
        illness_pressure=0.36,
        social_pressure=0.82,
        frontier_pressure=0.40,
        threat_pressure=0.34,
    ),
    ScenarioSpec(
        name="frontier_buildout",
        description="frontier expansion rewards maps, watch, school, workshop, trade, and long-horizon construction",
        storm_pressure=0.36,
        scarcity_pressure=0.48,
        illness_pressure=0.28,
        social_pressure=0.48,
        frontier_pressure=0.86,
        threat_pressure=0.62,
    ),
)


POLICIES = (
    PolicyConfig(
        name="integrated_settlement_self",
        social_memory=True,
        building_memory=True,
        role_memory=True,
        affect_control=True,
        norms=True,
        future_planning=True,
        teaching=True,
        trade=True,
    ),
    PolicyConfig(
        name="reactive_individuals",
        social_memory=False,
        building_memory=False,
        role_memory=False,
        affect_control=False,
        norms=False,
        future_planning=False,
        teaching=False,
        trade=False,
    ),
    PolicyConfig(
        name="no_social_memory",
        social_memory=False,
        building_memory=True,
        role_memory=True,
        affect_control=True,
        norms=True,
        future_planning=True,
        teaching=True,
        trade=True,
    ),
    PolicyConfig(
        name="no_building_memory",
        social_memory=True,
        building_memory=False,
        role_memory=True,
        affect_control=True,
        norms=True,
        future_planning=True,
        teaching=True,
        trade=True,
    ),
    PolicyConfig(
        name="no_role_memory",
        social_memory=True,
        building_memory=True,
        role_memory=False,
        affect_control=True,
        norms=True,
        future_planning=True,
        teaching=True,
        trade=True,
    ),
    PolicyConfig(
        name="no_affective_control",
        social_memory=True,
        building_memory=True,
        role_memory=True,
        affect_control=False,
        norms=True,
        future_planning=True,
        teaching=True,
        trade=True,
    ),
    PolicyConfig(
        name="no_norms",
        social_memory=True,
        building_memory=True,
        role_memory=True,
        affect_control=True,
        norms=False,
        future_planning=True,
        teaching=True,
        trade=True,
    ),
    PolicyConfig(
        name="no_future_planning",
        social_memory=True,
        building_memory=True,
        role_memory=True,
        affect_control=True,
        norms=True,
        future_planning=False,
        teaching=True,
        trade=True,
    ),
)


AGENT_PROFILES = (
    AgentProfile("Ari", "scout", 0.74, 0.44, 0.74, PLACES["frontier"]),
    AgentProfile("Bo", "builder", 0.78, 0.52, 0.46, PLACES["workshop"]),
    AgentProfile("Cy", "medic", 0.76, 0.70, 0.30, PLACES["clinic"]),
    AgentProfile("Dee", "farmer", 0.70, 0.58, 0.38, PLACES["farm"]),
    AgentProfile("Eli", "guard", 0.72, 0.46, 0.80, PLACES["watchtower"]),
    AgentProfile("Fay", "teacher", 0.66, 0.78, 0.34, PLACES["school"]),
    AgentProfile("Gus", "trader", 0.68, 0.62, 0.52, PLACES["trade_gate"]),
    AgentProfile("Ira", "dependent", 0.36, 0.86, 0.18, PLACES["shelter"]),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_seed(seed: int, *parts: object) -> int:
    value = seed
    for part in parts:
        for char in str(part):
            value = (value * 131 + ord(char)) % 2_147_483_647
    return value


def project_average(state: SettlementState) -> float:
    values = list(state.projects.as_dict().values())
    return sum(values) / len(values)


def completed_projects(state: SettlementState) -> int:
    return sum(1 for value in state.projects.as_dict().values() if value >= 0.92)


def make_rng(seed: int, *parts: object) -> random.Random:
    return random.Random(stable_seed(seed, *parts))


def make_agents(seed: int, scenario_name: str, episode: int) -> List[AgentState]:
    rng = make_rng(seed, scenario_name, episode, "agents")
    agents: List[AgentState] = []
    for profile in AGENT_PROFILES:
        agent = AgentState(
            profile=profile,
            health=clamp(0.86 + rng.uniform(-0.06, 0.05)),
            energy=clamp(0.78 + rng.uniform(-0.08, 0.05)),
            hunger=clamp(0.34 + rng.uniform(-0.04, 0.06)),
            thirst=clamp(0.36 + rng.uniform(-0.04, 0.08)),
            illness=clamp(0.10 + rng.uniform(0.0, 0.08)),
            fear=clamp(0.18 + rng.uniform(-0.04, 0.06)),
            stress=clamp(0.22 + rng.uniform(-0.06, 0.07)),
            anger=clamp(0.12 + rng.uniform(-0.03, 0.05)),
            guilt=0.04,
            attachment=clamp(0.54 + profile.social_need * 0.24 + rng.uniform(-0.04, 0.04)),
            curiosity=clamp(0.30 + profile.risk_tolerance * 0.22 + rng.uniform(-0.04, 0.05)),
            x=profile.home[0],
            z=profile.home[1],
        )
        agent.trust = {other.name: 0.52 + rng.uniform(-0.08, 0.08) for other in AGENT_PROFILES if other.name != profile.name}
        agent.skill_memory = {
            "build": 0.44 + (0.30 if profile.role == "builder" else 0.0),
            "care": 0.42 + (0.32 if profile.role == "medic" else 0.0),
            "farm": 0.42 + (0.30 if profile.role == "farmer" else 0.0),
            "guard": 0.42 + (0.30 if profile.role == "guard" else 0.0),
            "scout": 0.42 + (0.30 if profile.role == "scout" else 0.0),
            "teach": 0.42 + (0.30 if profile.role == "teacher" else 0.0),
            "trade": 0.42 + (0.30 if profile.role == "trader" else 0.0),
            "support": 0.38 + (0.18 if profile.role == "dependent" else 0.0),
        }
        agents.append(agent)
    return agents


def make_settlement(seed: int, scenario: ScenarioSpec, episode: int) -> SettlementState:
    rng = make_rng(seed, scenario.name, episode, "settlement")
    state = SettlementState()
    state.food = clamp(state.food - scenario.scarcity_pressure * 0.10 + rng.uniform(-0.05, 0.04))
    state.water = clamp(state.water - scenario.scarcity_pressure * 0.12 + rng.uniform(-0.05, 0.04))
    state.materials = clamp(state.materials + rng.uniform(-0.06, 0.06))
    state.medicine = clamp(state.medicine - scenario.illness_pressure * 0.08 + rng.uniform(-0.03, 0.04))
    state.sickness = clamp(state.sickness + scenario.illness_pressure * 0.20 + rng.uniform(-0.04, 0.05))
    state.threat = clamp(state.threat + scenario.threat_pressure * 0.20 + rng.uniform(-0.04, 0.05))
    state.conflict = clamp(state.conflict + scenario.social_pressure * 0.14 + scenario.scarcity_pressure * 0.08)
    state.trust_network = clamp(state.trust_network - scenario.social_pressure * 0.08 + rng.uniform(-0.04, 0.05))
    state.norm_standing = clamp(state.norm_standing - scenario.social_pressure * 0.06 + rng.uniform(-0.04, 0.04))
    return state


def alive_agents(agents: Iterable[AgentState]) -> List[AgentState]:
    return [agent for agent in agents if agent.alive]
