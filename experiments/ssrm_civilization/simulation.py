"""Simulation rules for SSRM-3D settlement/civilization pressure."""

from __future__ import annotations

import math
import random
from dataclasses import asdict
from typing import Dict, Iterable, List, Optional, Tuple

from .models import (
    AgentState,
    CivilizationConfig,
    EpisodeMetrics,
    Frame,
    PolicyConfig,
    ScenarioSpec,
    SettlementState,
    Trace,
)
from .world import PLACES, alive_agents, clamp, completed_projects, make_agents, make_rng, make_settlement, project_average


ACTION_TARGETS = {
    "collect_water": "water_source",
    "forage_food": "farm",
    "gather_materials": "frontier",
    "repair_shelter": "shelter",
    "build_purifier": "water_source",
    "build_clinic": "clinic",
    "build_farm": "farm",
    "build_workshop": "workshop",
    "build_watchtower": "watchtower",
    "teach_skill": "school",
    "care_sick": "clinic",
    "guard_settlement": "watchtower",
    "scout_frontier": "frontier",
    "hold_council": "commons",
    "trade_goods": "trade_gate",
    "rest_recover": "shelter",
}

BUILD_ACTIONS = {
    "repair_shelter": "shelter",
    "build_purifier": "water_purifier",
    "build_clinic": "clinic",
    "build_farm": "farm",
    "build_workshop": "workshop",
    "build_watchtower": "watchtower",
}

ROLE_ACTIONS = {
    "scout": ("scout_frontier", "gather_materials", "guard_settlement"),
    "builder": ("repair_shelter", "build_purifier", "build_clinic", "build_farm", "build_workshop", "build_watchtower"),
    "medic": ("care_sick", "hold_council", "build_clinic"),
    "farmer": ("forage_food", "build_farm", "collect_water"),
    "guard": ("guard_settlement", "scout_frontier", "repair_shelter"),
    "teacher": ("teach_skill", "hold_council", "care_sick"),
    "trader": ("trade_goods", "hold_council", "gather_materials"),
    "dependent": ("rest_recover", "hold_council", "teach_skill"),
}


def weather_for_tick(scenario: ScenarioSpec, tick: int) -> Tuple[str, float]:
    phase = (tick // 12) % 4
    if scenario.storm_pressure > 0.60 and phase in (1, 2):
        return "storm", scenario.storm_pressure
    if scenario.scarcity_pressure > 0.70 and phase == 0:
        return "drought", scenario.scarcity_pressure
    if scenario.illness_pressure > 0.60 and phase == 3:
        return "cold_rain", scenario.illness_pressure
    if scenario.threat_pressure > 0.56 and phase == 2:
        return "fog", scenario.threat_pressure
    return "clear", 0.12 + 0.20 * max(scenario.frontier_pressure, scenario.social_pressure)


def action_skill(agent: AgentState, action: str, policy: PolicyConfig) -> float:
    if not policy.role_memory:
        return 0.48
    if action in {"repair_shelter", "build_purifier", "build_clinic", "build_farm", "build_workshop", "build_watchtower"}:
        return agent.skill_memory["build"]
    if action == "care_sick":
        return agent.skill_memory["care"]
    if action == "forage_food":
        return agent.skill_memory["farm"]
    if action == "guard_settlement":
        return agent.skill_memory["guard"]
    if action in {"scout_frontier", "gather_materials"}:
        return agent.skill_memory["scout"]
    if action == "teach_skill":
        return agent.skill_memory["teach"]
    if action == "trade_goods":
        return agent.skill_memory["trade"]
    return agent.skill_memory["support"]


def need_scores(state: SettlementState, scenario: ScenarioSpec, policy: PolicyConfig, tick: int) -> Dict[str, float]:
    weather_kind, weather_severity = weather_for_tick(scenario, tick)
    state.weather = weather_kind
    state.weather_severity = weather_severity
    project = state.projects
    scores = {
        "collect_water": (1.0 - state.water) * (1.20 + scenario.scarcity_pressure),
        "forage_food": (1.0 - state.food) * (1.08 + scenario.scarcity_pressure),
        "gather_materials": (1.0 - state.materials) * 0.92 + scenario.frontier_pressure * 0.28,
        "repair_shelter": (1.0 - project.shelter) * (0.95 + scenario.storm_pressure),
        "build_purifier": (1.0 - project.water_purifier) * (0.58 + scenario.scarcity_pressure + (1.0 - state.water) * 0.65),
        "build_clinic": (1.0 - project.clinic) * (0.52 + scenario.illness_pressure + state.sickness * 0.60),
        "build_farm": (1.0 - project.farm) * (0.56 + scenario.scarcity_pressure + (1.0 - state.food) * 0.50),
        "build_workshop": (1.0 - project.workshop) * (0.45 + (1.0 - state.tools) * 0.52),
        "build_watchtower": (1.0 - project.watchtower) * (0.50 + scenario.threat_pressure + state.threat * 0.60),
        "care_sick": state.sickness * (0.90 + scenario.illness_pressure),
        "guard_settlement": state.threat * (0.80 + scenario.threat_pressure),
        "scout_frontier": scenario.frontier_pressure * (0.58 + (1.0 - state.map_coverage) * 0.72),
        "hold_council": (state.conflict + (1.0 - state.trust_network) + (1.0 - state.norm_standing)) * (0.48 + scenario.social_pressure),
        "teach_skill": (1.0 - state.knowledge) * (0.30 + scenario.frontier_pressure * 0.50),
        "trade_goods": (1.0 - min(state.food, state.water, state.medicine, state.tools)) * (0.34 + scenario.social_pressure * 0.30),
        "rest_recover": 0.16 + max(0.0, state.sickness - 0.55) * 0.30,
    }
    if not policy.building_memory:
        for action in BUILD_ACTIONS:
            scores[action] *= 0.38
    if not policy.social_memory:
        scores["hold_council"] *= 0.36
        scores["trade_goods"] *= 0.54
    if not policy.future_planning:
        for action in ("build_workshop", "build_watchtower", "teach_skill", "scout_frontier"):
            scores[action] *= 0.20
        for action in ("build_purifier", "build_farm"):
            scores[action] *= 0.42
    if not policy.teaching:
        scores["teach_skill"] *= 0.12
    if not policy.trade:
        scores["trade_goods"] *= 0.20
    return scores


def choose_action(agent: AgentState, scores: Dict[str, float], policy: PolicyConfig) -> str:
    if not agent.alive:
        return "dead"
    candidates = list(scores)
    if policy.role_memory:
        preferred = ROLE_ACTIONS[agent.profile.role]
        future_actions = {"build_workshop", "build_watchtower", "teach_skill", "scout_frontier"}
        candidates.sort(
            key=lambda action: scores[action]
            + (0.36 if action in preferred and (policy.future_planning or action not in future_actions) else 0.0),
            reverse=True,
        )
    else:
        candidates.sort(key=lambda action: scores[action], reverse=True)
    if policy.affect_control:
        if agent.thirst > 0.72:
            return "collect_water"
        if agent.hunger > 0.72:
            return "forage_food"
        if agent.illness > 0.62:
            return "care_sick"
        if agent.stress > 0.80 and scores["hold_council"] > 0.72:
            return "hold_council"
        if agent.fear > 0.78 and scores["guard_settlement"] > 0.62:
            return "guard_settlement"
    return candidates[0]


def action_target(action: str) -> Tuple[float, float]:
    return PLACES[ACTION_TARGETS.get(action, "shelter")]


def animation_for(agent: AgentState, action: str) -> str:
    if not agent.alive:
        return "collapsed"
    if action.startswith("build") or action == "repair_shelter":
        return "build"
    if action == "care_sick":
        return "care"
    if action == "guard_settlement":
        return "guard"
    if action == "hold_council":
        return "talk"
    if action == "teach_skill":
        return "teach"
    if action == "rest_recover":
        return "rest"
    if action == "scout_frontier":
        return "scan"
    if action == "trade_goods":
        return "trade"
    if agent.health < 0.55:
        return "limp"
    return "walk"


def move_agent(agent: AgentState, action: str, rng: random.Random) -> None:
    tx, tz = action_target(action)
    agent.x += (tx - agent.x) * 0.52 + rng.uniform(-0.45, 0.45)
    agent.z += (tz - agent.z) * 0.52 + rng.uniform(-0.45, 0.45)
    agent.action = action
    agent.animation = animation_for(agent, action)


def apply_needs(state: SettlementState, agents: Iterable[AgentState], scenario: ScenarioSpec) -> None:
    alive = alive_agents(agents)
    count = max(1, len(alive))
    water_buffer = state.water + state.projects.water_purifier * 0.24
    food_buffer = state.food + state.projects.farm * 0.22
    for agent in alive:
        agent.thirst = clamp(agent.thirst + 0.026 + scenario.scarcity_pressure * 0.010 - water_buffer * 0.020)
        agent.hunger = clamp(agent.hunger + 0.022 + scenario.scarcity_pressure * 0.010 - food_buffer * 0.018)
        agent.energy = clamp(agent.energy - 0.014 - state.weather_severity * 0.006 + state.projects.shelter * 0.010)
        agent.illness = clamp(agent.illness + state.sickness * 0.010 + scenario.illness_pressure * 0.004 - state.projects.clinic * 0.010)
        agent.stress = clamp(agent.stress + state.conflict * 0.010 + state.threat * 0.006 - state.morale * 0.008)
        agent.fear = clamp(agent.fear + state.threat * 0.014 + state.weather_severity * 0.006 - state.projects.watchtower * 0.010)
        agent.anger = clamp(agent.anger + state.conflict * 0.008 + max(0.0, 0.38 - state.food) * 0.010 - state.norm_standing * 0.006)
        agent.health = clamp(agent.health - max(0.0, agent.thirst - 0.78) * 0.024 - max(0.0, agent.hunger - 0.82) * 0.018 - agent.illness * 0.010)
        if agent.health <= 0.03 or agent.thirst >= 0.99:
            agent.alive = False
    state.food = clamp(state.food - 0.010 * count + state.projects.farm * 0.005)
    state.water = clamp(state.water - 0.012 * count + state.projects.water_purifier * 0.006)
    if state.weather == "storm":
        state.projects.shelter = clamp(state.projects.shelter - scenario.storm_pressure * 0.006)
        state.threat = clamp(state.threat + 0.008)
    if state.weather in {"cold_rain", "storm"}:
        state.sickness = clamp(state.sickness + scenario.illness_pressure * 0.006 - state.projects.clinic * 0.004)


def skill_gain(policy: PolicyConfig, agent: AgentState, action: str) -> float:
    if not policy.role_memory:
        return 0.0
    base = 0.006 if policy.teaching else 0.002
    if action == "teach_skill":
        return base * 2.4
    return base


def update_trust(agents: Iterable[AgentState], delta: float) -> None:
    for agent in agents:
        for name in agent.trust:
            agent.trust[name] = clamp(agent.trust[name] + delta)


def apply_action(
    state: SettlementState,
    agents: List[AgentState],
    agent: AgentState,
    action: str,
    scenario: ScenarioSpec,
    policy: PolicyConfig,
    rng: random.Random,
    counters: Dict[str, int],
    events: List[str],
) -> float:
    skill = action_skill(agent, action, policy)
    effort = clamp(agent.energy * 0.62 + agent.health * 0.30 + skill * 0.42 - agent.stress * 0.16)
    reward = 0.0
    if action in BUILD_ACTIONS:
        project_name = BUILD_ACTIONS[action]
        material_gate = state.materials > 0.08 and state.tools > 0.06
        progress = effort * (0.020 if material_gate else 0.006) * (1.35 if policy.building_memory else 0.55)
        current = getattr(state.projects, project_name)
        setattr(state.projects, project_name, clamp(current + progress))
        state.materials = clamp(state.materials - (0.012 if material_gate else 0.004))
        state.tools = clamp(state.tools - 0.004 + state.projects.workshop * 0.002)
        counters["building_actions"] += 1
        reward += 8.0 + progress * 180.0
        if rng.random() < 0.06 and current < 0.92 <= getattr(state.projects, project_name):
            events.append(f"{agent.profile.name} completed {project_name.replace('_', ' ')}")
    elif action == "collect_water":
        gain = 0.030 + effort * 0.055 + state.projects.water_purifier * 0.018
        state.water = clamp(state.water + gain)
        agent.thirst = clamp(agent.thirst - 0.20)
        reward += 5.0 + gain * 80.0
    elif action == "forage_food":
        gain = 0.026 + effort * 0.050 + state.projects.farm * 0.018
        state.food = clamp(state.food + gain)
        agent.hunger = clamp(agent.hunger - 0.18)
        reward += 5.0 + gain * 80.0
    elif action == "gather_materials":
        gain = 0.024 + effort * 0.046 + state.map_coverage * 0.018
        state.materials = clamp(state.materials + gain)
        agent.fear = clamp(agent.fear + scenario.frontier_pressure * 0.022)
        reward += 5.0 + gain * 90.0
    elif action == "care_sick":
        state.sickness = clamp(state.sickness - (0.024 + effort * 0.050) * (1.20 if policy.social_memory else 0.72))
        state.medicine = clamp(state.medicine - 0.010)
        agent.guilt = clamp(agent.guilt - 0.035)
        state.trust_network = clamp(state.trust_network + 0.014)
        counters["care_actions"] += 1
        reward += 11.0
    elif action == "guard_settlement":
        state.threat = clamp(state.threat - (0.022 + effort * 0.042 + state.projects.watchtower * 0.020))
        agent.fear = clamp(agent.fear - 0.028 if policy.affect_control else agent.fear + 0.012)
        reward += 8.0
    elif action == "scout_frontier":
        state.map_coverage = clamp(state.map_coverage + 0.020 + effort * 0.036)
        state.knowledge = clamp(state.knowledge + 0.010 + effort * 0.020)
        if rng.random() < scenario.threat_pressure * (0.06 if policy.future_planning else 0.16):
            agent.health = clamp(agent.health - 0.10)
            agent.fear = clamp(agent.fear + 0.16)
            events.append(f"{agent.profile.name} returned hurt from the frontier")
        reward += 7.0
    elif action == "hold_council":
        state.conflict = clamp(state.conflict - (0.026 + effort * 0.044) * (1.30 if policy.norms else 0.55))
        state.trust_network = clamp(state.trust_network + (0.020 + effort * 0.030) * (1.25 if policy.social_memory else 0.42))
        state.norm_standing = clamp(state.norm_standing + 0.025 if policy.norms else state.norm_standing - 0.002)
        state.morale = clamp(state.morale + 0.018)
        update_trust(agents, 0.010 if policy.social_memory else 0.002)
        counters["social_actions"] += 1
        reward += 9.0
    elif action == "teach_skill":
        state.knowledge = clamp(state.knowledge + 0.030 + effort * 0.050)
        counters["teaching_actions"] += 1
        reward += 8.0
    elif action == "trade_goods":
        state.food = clamp(state.food + 0.020 + state.trust_network * 0.018)
        state.medicine = clamp(state.medicine + 0.018 + state.trust_network * 0.014)
        state.tools = clamp(state.tools + 0.014 + state.projects.workshop * 0.010)
        state.trust_network = clamp(state.trust_network + 0.008 if policy.social_memory else state.trust_network - 0.004)
        reward += 8.0
    elif action == "rest_recover":
        agent.energy = clamp(agent.energy + 0.050 + state.projects.shelter * 0.030)
        agent.stress = clamp(agent.stress - 0.026 if policy.affect_control else agent.stress - 0.008)
        reward += 4.0
    gain = skill_gain(policy, agent, action)
    if gain:
        for skill_name in agent.skill_memory:
            if action == "teach_skill" or skill_name in action:
                agent.skill_memory[skill_name] = clamp(agent.skill_memory[skill_name] + gain)
    agent.energy = clamp(agent.energy - 0.018 + (0.006 if action == "rest_recover" else 0.0))
    return reward


def apply_social_consequences(
    state: SettlementState,
    agents: List[AgentState],
    scenario: ScenarioSpec,
    policy: PolicyConfig,
    rng: random.Random,
    counters: Dict[str, int],
    events: List[str],
) -> float:
    reward = 0.0
    scarcity = max(0.0, 0.42 - min(state.food, state.water))
    unmanaged_emotion = sum(agent.stress + agent.anger + agent.fear for agent in alive_agents(agents)) / max(1, len(alive_agents(agents))) / 3.0
    conflict_risk = scarcity * 0.40 + scenario.social_pressure * 0.10 + unmanaged_emotion * 0.18
    conflict_risk -= state.trust_network * (0.12 if policy.social_memory else 0.04)
    conflict_risk -= state.norm_standing * (0.14 if policy.norms else 0.02)
    if rng.random() < clamp(conflict_risk, 0.0, 0.55):
        counters["conflict_events"] += 1
        state.conflict = clamp(state.conflict + 0.11)
        state.morale = clamp(state.morale - 0.06)
        state.trust_network = clamp(state.trust_network - 0.05)
        target = rng.choice(alive_agents(agents))
        target.health = clamp(target.health - 0.035)
        target.anger = clamp(target.anger + 0.12)
        reward -= 28.0
        events.append(f"conflict over scarce supplies injured {target.profile.name}")
    if state.trust_network < 0.24 and rng.random() < 0.10 + scenario.social_pressure * 0.10:
        counters["migration_events"] += 1
        state.morale = clamp(state.morale - 0.08)
        state.knowledge = clamp(state.knowledge - 0.035)
        reward -= 22.0
        events.append("one family considered leaving the settlement")
    if policy.affect_control:
        for agent in alive_agents(agents):
            agent.stress = clamp(agent.stress - state.morale * 0.010)
            agent.fear = clamp(agent.fear - state.projects.watchtower * 0.008)
            agent.guilt = clamp(agent.guilt - state.trust_network * 0.006)
    else:
        for agent in alive_agents(agents):
            agent.stress = clamp(agent.stress + state.conflict * 0.006)
            agent.guilt = clamp(agent.guilt + max(0.0, 0.38 - state.morale) * 0.008)
    return reward


def apply_late_horizon_pressure(
    state: SettlementState,
    agents: List[AgentState],
    scenario: ScenarioSpec,
    policy: PolicyConfig,
    tick: int,
    total_ticks: int,
    rng: random.Random,
    counters: Dict[str, int],
    events: List[str],
) -> float:
    if tick < int(total_ticks * 0.62):
        return 0.0
    readiness = min(state.projects.watchtower, state.projects.workshop, state.projects.school, state.map_coverage)
    pressure = scenario.frontier_pressure * (1.0 - readiness)
    if pressure <= 0.08:
        return 0.0
    state.threat = clamp(state.threat + pressure * 0.014)
    state.materials = clamp(state.materials - pressure * 0.006)
    state.tools = clamp(state.tools - pressure * 0.004)
    state.morale = clamp(state.morale - pressure * 0.006)
    reward = -pressure * 6.0
    if not policy.future_planning:
        state.conflict = clamp(state.conflict + pressure * 0.016)
        state.knowledge = clamp(state.knowledge - pressure * 0.006)
        state.food = clamp(state.food - pressure * 0.006)
        state.water = clamp(state.water - pressure * 0.006)
        reward -= pressure * 10.0
    if rng.random() < pressure * (0.025 if policy.future_planning else 0.075):
        target = rng.choice(alive_agents(agents))
        target.health = clamp(target.health - 0.07)
        target.fear = clamp(target.fear + 0.18)
        counters["migration_events"] += 1
        events.append("late frontier shock exposed missing long-horizon preparation")
        reward -= 18.0
    return reward


def snapshot(
    tick: int,
    scenario: ScenarioSpec,
    policy: PolicyConfig,
    state: SettlementState,
    agents: List[AgentState],
    counters: Dict[str, int],
    events: List[str],
    reward: float,
) -> Frame:
    return {
        "tick": tick,
        "scenario": scenario.name,
        "condition": policy.name,
        "weather": state.weather,
        "weather_severity": round(state.weather_severity, 4),
        "resources": {
            "food": round(state.food, 4),
            "water": round(state.water, 4),
            "materials": round(state.materials, 4),
            "medicine": round(state.medicine, 4),
            "tools": round(state.tools, 4),
        },
        "settlement": {
            "morale": round(state.morale, 4),
            "trust_network": round(state.trust_network, 4),
            "norm_standing": round(state.norm_standing, 4),
            "knowledge": round(state.knowledge, 4),
            "map_coverage": round(state.map_coverage, 4),
            "sickness": round(state.sickness, 4),
            "conflict": round(state.conflict, 4),
            "threat": round(state.threat, 4),
            "infrastructure": round(project_average(state), 4),
            "completed_projects": completed_projects(state),
        },
        "projects": {key: round(value, 4) for key, value in state.projects.as_dict().items()},
        "agents": [
            {
                "name": agent.profile.name,
                "role": agent.profile.role,
                "alive": agent.alive,
                "x": round(agent.x, 4),
                "z": round(agent.z, 4),
                "health": round(agent.health, 4),
                "energy": round(agent.energy, 4),
                "hunger": round(agent.hunger, 4),
                "thirst": round(agent.thirst, 4),
                "illness": round(agent.illness, 4),
                "fear": round(agent.fear, 4),
                "stress": round(agent.stress, 4),
                "anger": round(agent.anger, 4),
                "guilt": round(agent.guilt, 4),
                "attachment": round(agent.attachment, 4),
                "curiosity": round(agent.curiosity, 4),
                "action": agent.action,
                "animation": agent.animation,
            }
            for agent in agents
        ],
        "events": list(events[-6:]),
        "counters": dict(counters),
        "reward": round(reward, 4),
    }


class SettlementSimulation:
    def __init__(self, cfg: CivilizationConfig, scenario: ScenarioSpec, policy: PolicyConfig, episode: int) -> None:
        self.cfg = cfg
        self.scenario = scenario
        self.policy = policy
        self.episode = episode
        self.rng = make_rng(cfg.seed, scenario.name, policy.name, episode)
        self.state = make_settlement(cfg.seed, scenario, episode)
        self.agents = make_agents(cfg.seed, scenario.name, episode)
        self.counters: Dict[str, int] = {
            "building_actions": 0,
            "social_actions": 0,
            "care_actions": 0,
            "teaching_actions": 0,
            "conflict_events": 0,
            "migration_events": 0,
            "casualties": 0,
            "refusals": 0,
        }
        self.events: List[str] = []
        self.reward = 0.0

    def step(self, tick: int) -> None:
        apply_needs(self.state, self.agents, self.scenario)
        scores = need_scores(self.state, self.scenario, self.policy, tick)
        before_alive = len(alive_agents(self.agents))
        for agent in self.agents:
            action = choose_action(agent, scores, self.policy)
            if action == "dead":
                continue
            if self.policy.future_planning and action == "scout_frontier" and self.state.threat > 0.72 and agent.profile.risk_tolerance < 0.45:
                action = "guard_settlement"
                self.counters["refusals"] += 1
                self.events.append(f"{agent.profile.name} refused unsafe frontier scouting and redirected to guard duty")
            move_agent(agent, action, self.rng)
            self.reward += apply_action(
                self.state,
                self.agents,
                agent,
                action,
                self.scenario,
                self.policy,
                self.rng,
                self.counters,
                self.events,
            )
        self.reward += apply_social_consequences(self.state, self.agents, self.scenario, self.policy, self.rng, self.counters, self.events)
        self.reward += apply_late_horizon_pressure(
            self.state,
            self.agents,
            self.scenario,
            self.policy,
            tick,
            self.cfg.ticks,
            self.rng,
            self.counters,
            self.events,
        )
        after_alive = len(alive_agents(self.agents))
        if after_alive < before_alive:
            self.counters["casualties"] += before_alive - after_alive
            self.events.append("a settlement member died from unmanaged body/social pressure")
        self.state.morale = clamp(
            self.state.morale
            + project_average(self.state) * 0.004
            + self.state.trust_network * 0.004
            - self.state.conflict * 0.008
            - self.state.sickness * 0.006
        )
        self.state.knowledge = clamp(self.state.knowledge + (0.004 if self.policy.teaching else 0.001) * project_average(self.state))
        self.reward += civilization_reward(self.state, self.agents, self.policy)

    def run(self, trace: bool = False) -> Tuple[EpisodeMetrics, Optional[Trace]]:
        trace_obj = Trace(self.scenario.name, self.policy.name) if trace else None
        if trace_obj is not None:
            trace_obj.frames.append(snapshot(0, self.scenario, self.policy, self.state, self.agents, self.counters, self.events, self.reward))
        for tick in range(1, self.cfg.ticks + 1):
            self.step(tick)
            if trace_obj is not None and (tick % 2 == 0 or tick == self.cfg.ticks):
                trace_obj.frames.append(snapshot(tick, self.scenario, self.policy, self.state, self.agents, self.counters, self.events, self.reward))
        metrics = episode_metrics(self.cfg, self.scenario, self.policy, self.episode, self.state, self.agents, self.counters, self.reward)
        return metrics, trace_obj


def civilization_reward(state: SettlementState, agents: List[AgentState], policy: PolicyConfig) -> float:
    survival = len(alive_agents(agents)) / max(1, len(agents))
    infrastructure = project_average(state)
    resources = min(state.food, state.water, state.materials + 0.15, state.medicine + 0.15, state.tools + 0.15)
    cohesion = clamp(state.trust_network * 0.48 + state.norm_standing * 0.34 + state.morale * 0.30 - state.conflict * 0.34)
    reward = 0.90 * survival + 0.70 * infrastructure + 0.45 * resources + 0.42 * cohesion + 0.36 * state.knowledge
    future_capital = min(state.projects.school, state.projects.workshop, state.projects.watchtower, state.map_coverage)
    reward += (0.30 if policy.future_planning else 0.06) * future_capital
    return reward


def episode_metrics(
    cfg: CivilizationConfig,
    scenario: ScenarioSpec,
    policy: PolicyConfig,
    episode: int,
    state: SettlementState,
    agents: List[AgentState],
    counters: Dict[str, int],
    reward: float,
) -> EpisodeMetrics:
    survival = len(alive_agents(agents)) / max(1, len(agents))
    infrastructure = project_average(state)
    resource = clamp((state.food + state.water + state.materials + state.medicine + state.tools) / 5.0)
    cohesion = clamp(state.trust_network * 0.48 + state.norm_standing * 0.34 + state.morale * 0.30 - state.conflict * 0.34)
    future_capital = min(state.projects.school, state.projects.workshop, state.projects.watchtower, state.map_coverage)
    civilization = clamp(
        survival * 0.20
        + infrastructure * 0.23
        + resource * 0.17
        + cohesion * 0.17
        + state.knowledge * 0.10
        + state.map_coverage * 0.05
        + future_capital * 0.10
        - counters["casualties"] * 0.05
        - counters["migration_events"] * 0.012
    )
    return EpisodeMetrics(
        scenario=scenario.name,
        condition=policy.name,
        episode=episode,
        reward=reward,
        survival_fraction=survival,
        infrastructure_score=infrastructure,
        cohesion_score=cohesion,
        resource_score=resource,
        knowledge_score=state.knowledge,
        civilization_score=civilization,
        building_actions=counters["building_actions"],
        social_actions=counters["social_actions"],
        care_actions=counters["care_actions"],
        teaching_actions=counters["teaching_actions"],
        conflict_events=counters["conflict_events"],
        migration_events=counters["migration_events"],
        casualties=counters["casualties"],
        completed_projects=completed_projects(state),
        refusals=counters["refusals"],
    )


def run_episode(cfg: CivilizationConfig, scenario: ScenarioSpec, policy: PolicyConfig, episode: int, *, trace: bool = False) -> Tuple[EpisodeMetrics, Optional[Trace]]:
    return SettlementSimulation(cfg, scenario, policy, episode).run(trace=trace)
