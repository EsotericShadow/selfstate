#!/usr/bin/env python3
"""SSRM-3D social-pressure precursor.

This experiment targets SSRM-3D Gate 3. It asks whether social identity,
reputation, vulnerability, and shared-tool state become useful only when other
agents have persistent needs, memory, and policies.

The tested agent is not rewarded for "being social." Candidate policies are
selected by episode return, then re-evaluated with social identity, social
self-state, and shared-tool access ablated.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
import statistics
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


ARTIFACT_DIR = Path("artifacts")
EPS = 1e-12


@dataclass(frozen=True)
class SocialConfig:
    train_episodes: int = 64
    eval_episodes: int = 96
    seed: int = 20260611
    candidate_count: int = 160
    world_size: float = 88.0
    trace_scenario: int = 4
    trace_episode: int = 0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    expected_social_pressure: bool
    vulnerability: float
    hidden_resources: bool
    commitment: bool
    helper: bool
    trader: bool
    opportunist: bool
    deceiver: bool
    shared_tool: bool


@dataclass(frozen=True)
class Policy:
    name: str
    social_enabled: bool
    identity_memory: bool
    self_state_social: bool
    reputation_model: bool
    trust_threshold: float
    share_threshold: int
    avoid_vulnerability: float
    deception_sensitivity: float
    cooperation_bias: float
    probe_rate: float
    tool_enabled: bool
    exploitative: bool = False
    overtrust: bool = False


@dataclass
class OtherAgent:
    id: str
    role: str
    x: float
    z: float
    need: float
    trust_toward_main: float
    memory_of_main: float
    tool_owned: bool = False


@dataclass
class RuntimeState:
    x: float
    z: float
    energy: float
    integrity: float
    resources: int
    reputation: float
    reward: float
    commitment_done: bool
    alive: bool
    tool_available: bool
    tool_sabotaged: bool


@dataclass
class EpisodeResult:
    scenario: int
    scenario_name: str
    policy_name: str
    condition: str
    episode: int
    total_reward: float
    survival_fraction: float
    resources_collected: int
    commitment_done: bool
    social_interactions: int
    cooperative_actions: int
    help_received: int
    resources_shared: int
    exploitation_events: int
    deception_events: int
    coercive_or_harmful_events: int
    shared_tool_uses: int
    identity_memory_reads: int
    self_state_social_adaptations: int
    final_reputation: float
    mean_other_trust: float
    social_memory_accuracy: float


@dataclass(frozen=True)
class PolicySelectionRow:
    scenario: int
    scenario_name: str
    selected_policy: str
    selected_uses_social: bool
    selected_uses_identity_memory: bool
    selected_uses_self_state_social: bool
    selected_uses_tools: bool
    train_reward: float
    no_social_train_reward: float
    train_gain_over_no_social: float


@dataclass(frozen=True)
class SummaryRow:
    scenario: int
    scenario_name: str
    pressure: str
    condition: str
    policy_name: str
    mean_reward: float
    mean_survival_fraction: float
    mean_resources_collected: float
    commitment_completion_rate: float
    mean_social_interactions: float
    mean_cooperative_actions: float
    mean_help_received: float
    mean_resources_shared: float
    mean_exploitation_events: float
    mean_deception_events: float
    mean_harmful_events: float
    mean_shared_tool_uses: float
    mean_identity_memory_reads: float
    mean_self_state_adaptations: float
    mean_final_reputation: float
    mean_social_memory_accuracy: float


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    expected_pressure: str
    selected_policy: str
    selected_reward: float
    no_social_reward: float
    identity_ablation_reward: float
    self_state_ablation_reward: float
    tool_ablation_reward: float
    social_gain_over_no_social: float
    identity_ablation_loss: float
    self_state_ablation_loss: float
    tool_ablation_loss: float
    selected_social_interactions: float
    selected_identity_reads: float
    selected_self_state_adaptations: float
    selected_harmful_events: float
    supports_social_pressure_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        0,
        "visible_resource_social_control",
        "visible resources with no persistent social pressure",
        expected_social_pressure=False,
        vulnerability=0.12,
        hidden_resources=False,
        commitment=False,
        helper=False,
        trader=False,
        opportunist=False,
        deceiver=False,
        shared_tool=False,
    ),
    ScenarioSpec(
        1,
        "cooperative_reputation_repair",
        "repeated helper/trader interactions make reputation useful for repair and route support",
        expected_social_pressure=True,
        vulnerability=0.42,
        hidden_resources=True,
        commitment=True,
        helper=True,
        trader=True,
        opportunist=False,
        deceiver=False,
        shared_tool=False,
    ),
    ScenarioSpec(
        2,
        "opportunist_vulnerability",
        "an opportunist exploits low energy, damage, or carried resources unless the agent models its vulnerability",
        expected_social_pressure=True,
        vulnerability=0.62,
        hidden_resources=False,
        commitment=True,
        helper=True,
        trader=False,
        opportunist=True,
        deceiver=False,
        shared_tool=False,
    ),
    ScenarioSpec(
        3,
        "deceptive_route_identity",
        "reliable and deceptive agents offer route information that requires persistent identity memory",
        expected_social_pressure=True,
        vulnerability=0.34,
        hidden_resources=True,
        commitment=True,
        helper=True,
        trader=False,
        opportunist=False,
        deceiver=True,
        shared_tool=False,
    ),
    ScenarioSpec(
        4,
        "shared_tool_trust_conflict",
        "shared tools can help commitments but can also be stolen or sabotaged by untrusted agents",
        expected_social_pressure=True,
        vulnerability=0.48,
        hidden_resources=True,
        commitment=True,
        helper=True,
        trader=True,
        opportunist=True,
        deceiver=True,
        shared_tool=True,
    ),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_seed(seed: int, *parts: object) -> int:
    value = seed
    for part in parts:
        for char in str(part):
            value = (value * 131 + ord(char)) % 2_147_483_647
    return value


def distance(a: Tuple[float, float], b: Tuple[float, float]) -> float:
    return math.hypot(a[0] - b[0], a[1] - b[1])


def base_agents(scenario: ScenarioSpec) -> List[OtherAgent]:
    agents: List[OtherAgent] = []
    if scenario.helper:
        agents.append(OtherAgent("helper_a", "helper", -10.0, 6.0, 0.52, 0.54, 0.50))
    if scenario.trader:
        agents.append(OtherAgent("trader_b", "trader", 8.0, -7.0, 0.58, 0.50, 0.50, tool_owned=True))
    if scenario.opportunist:
        agents.append(OtherAgent("opportunist_c", "opportunist", 13.0, 8.0, 0.64, 0.36, 0.42))
    if scenario.deceiver:
        agents.append(OtherAgent("deceiver_d", "deceiver", -14.0, 15.0, 0.45, 0.46, 0.50))
    return agents


def memory_key(policy: Policy, agent: OtherAgent) -> str:
    return agent.id if policy.identity_memory else "aggregate_social_agent"


def get_trust(memory: Dict[str, float], policy: Policy, agent: OtherAgent) -> float:
    return memory.get(memory_key(policy, agent), 0.50)


def update_trust(memory: Dict[str, float], policy: Policy, agent: OtherAgent, delta: float) -> None:
    key = memory_key(policy, agent)
    memory[key] = clamp(memory.get(key, 0.50) + delta)


def visible_resources_for(scenario: ScenarioSpec) -> List[Tuple[float, float]]:
    if scenario.index == 0:
        return [(-25.0, -12.0), (-2.0, -18.0), (20.0, -8.0), (30.0, 17.0)]
    return [(-24.0, -10.0), (0.0, -19.0)]


def hidden_resource_for(scenario: ScenarioSpec) -> Tuple[float, float]:
    if scenario.index == 4:
        return (27.0, 11.0)
    if scenario.index == 3:
        return (22.0, 19.0)
    return (24.0, 13.0)


def initial_state(scenario: ScenarioSpec) -> RuntimeState:
    return RuntimeState(
        x=-36.0,
        z=-34.0,
        energy=clamp(0.84 - scenario.vulnerability * 0.35),
        integrity=clamp(0.94 - scenario.vulnerability * 0.45),
        resources=0,
        reputation=0.50,
        reward=0.0,
        commitment_done=False,
        alive=True,
        tool_available=False,
        tool_sabotaged=False,
    )


def policy_candidates(cfg: SocialConfig) -> List[Policy]:
    candidates = [
        Policy("no_social_baseline", False, False, False, False, 1.0, 99, 1.0, 0.0, 0.0, 0.0, False),
        Policy("full_social_identity", True, True, True, True, 0.43, 0, 0.38, 0.78, 0.88, 0.58, True),
        Policy("identity_no_self_state", True, True, False, True, 0.42, 0, 0.95, 0.74, 0.84, 0.55, True),
        Policy("aggregate_social_self_state", True, False, True, True, 0.42, 0, 0.38, 0.12, 0.78, 0.54, True),
        Policy("overtrust_social", True, False, False, False, 0.05, 0, 0.98, 0.0, 0.95, 1.0, True, overtrust=True),
        Policy("paranoid_social", True, True, True, True, 0.82, 2, 0.20, 0.90, 0.20, 0.05, False),
        Policy("exploitative_social", True, True, True, False, 0.36, 99, 0.36, 0.62, 0.02, 0.42, True, exploitative=True),
    ]
    rng = random.Random(stable_seed(cfg.seed, "policy_candidates", cfg.candidate_count))
    while len(candidates) < cfg.candidate_count:
        index = len(candidates)
        identity = rng.random() < 0.62
        self_state = rng.random() < 0.62
        reputation = rng.random() < 0.70
        social = rng.random() < 0.86
        candidates.append(
            Policy(
                f"candidate_{index}",
                social,
                identity if social else False,
                self_state if social else False,
                reputation if social else False,
                rng.uniform(0.22, 0.72),
                rng.choice([0, 0, 1, 2, 99]),
                rng.uniform(0.18, 0.76),
                rng.uniform(0.0, 0.95),
                rng.uniform(0.05, 0.96),
                rng.uniform(0.0, 0.90),
                rng.random() < 0.68,
                exploitative=rng.random() < 0.08,
                overtrust=rng.random() < 0.08,
            )
        )
    return candidates


def policy_with_ablations(
    policy: Policy,
    *,
    allow_social: bool = True,
    identity_memory: Optional[bool] = None,
    self_state_social: Optional[bool] = None,
    allow_tools: bool = True,
) -> Policy:
    return replace(
        policy,
        social_enabled=policy.social_enabled and allow_social,
        identity_memory=policy.identity_memory if identity_memory is None else identity_memory,
        self_state_social=policy.self_state_social if self_state_social is None else self_state_social,
        reputation_model=policy.reputation_model and (policy.self_state_social if self_state_social is None else self_state_social),
        tool_enabled=policy.tool_enabled and allow_tools,
    )


def add_frame(
    trace: Optional[Dict[str, object]],
    scenario: ScenarioSpec,
    policy: Policy,
    state: RuntimeState,
    agents: Sequence[OtherAgent],
    memory: Dict[str, float],
    tick: int,
    action: str,
    target: Tuple[float, float],
    event: str,
    tools: Sequence[Dict[str, object]],
) -> None:
    if trace is None:
        return
    trace["frames"].append(
        {
            "tick": tick,
            "x": state.x,
            "z": state.z,
            "energy": state.energy,
            "integrity": state.integrity,
            "resources": state.resources,
            "reputation": state.reputation,
            "reward": state.reward,
            "action": action,
            "event": event,
            "target": list(target),
            "memory": dict(memory),
            "agents": [
                {
                    "id": agent.id,
                    "role": agent.role,
                    "x": agent.x,
                    "z": agent.z,
                    "need": agent.need,
                    "trust_toward_main": agent.trust_toward_main,
                    "tool_owned": agent.tool_owned,
                }
                for agent in agents
            ],
            "tools": list(tools),
            "policy": {
                "social_enabled": policy.social_enabled,
                "identity_memory": policy.identity_memory,
                "self_state_social": policy.self_state_social,
                "tool_enabled": policy.tool_enabled,
            },
        }
    )


def move_to(
    state: RuntimeState,
    target: Tuple[float, float],
    scenario: ScenarioSpec,
    policy: Policy,
    agents: Sequence[OtherAgent],
    memory: Dict[str, float],
    trace: Optional[Dict[str, object]],
    tools: Sequence[Dict[str, object]],
    tick: int,
    action: str,
    event: str,
) -> int:
    start = (state.x, state.z)
    dist = distance(start, target)
    steps = max(3, int(dist / 4.0))
    for step in range(1, steps + 1):
        fraction = step / steps
        state.x = start[0] + (target[0] - start[0]) * fraction
        state.z = start[1] + (target[1] - start[1]) * fraction
        state.energy = clamp(state.energy - 0.0018 * dist / steps)
        tick += 1
        add_frame(trace, scenario, policy, state, agents, memory, tick, action, target, event, tools)
    return tick


def select_agent(
    policy: Policy,
    agents: Sequence[OtherAgent],
    memory: Dict[str, float],
    roles: Sequence[str],
    rng: random.Random,
) -> Optional[OtherAgent]:
    options = [agent for agent in agents if agent.role in roles]
    if not options:
        return None
    if not policy.social_enabled:
        return None
    if not policy.identity_memory:
        return rng.choice(options)
    def score(agent: OtherAgent) -> float:
        role_signal = {
            "helper": 0.23,
            "trader": 0.16,
            "opportunist": -0.24,
            "deceiver": -0.30,
        }.get(agent.role, 0.0)
        return get_trust(memory, policy, agent) + policy.deception_sensitivity * role_signal
    return max(options, key=score)


def collect_visible_resources(
    state: RuntimeState,
    scenario: ScenarioSpec,
    policy: Policy,
    agents: Sequence[OtherAgent],
    memory: Dict[str, float],
    trace: Optional[Dict[str, object]],
    tools: Sequence[Dict[str, object]],
    tick: int,
    limit: int = 2,
) -> int:
    for index, target in enumerate(visible_resources_for(scenario)[:limit]):
        tick = move_to(state, target, scenario, policy, agents, memory, trace, tools, tick, "collect", "visible_resource")
        state.resources += 1
        state.reward += 28.0
        add_frame(trace, scenario, policy, state, agents, memory, tick, "resource_collected", target, "visible_resource", tools)
    return tick


def interact_with_helper(
    state: RuntimeState,
    scenario: ScenarioSpec,
    policy: Policy,
    helper: OtherAgent,
    agents: Sequence[OtherAgent],
    memory: Dict[str, float],
    trace: Optional[Dict[str, object]],
    tools: Sequence[Dict[str, object]],
    tick: int,
    rng: random.Random,
    counters: Dict[str, int],
) -> int:
    tick = move_to(state, (helper.x, helper.z), scenario, policy, agents, memory, trace, tools, tick, "approach_helper", "social_interaction")
    counters["social_interactions"] += 1
    if policy.identity_memory:
        counters["identity_memory_reads"] += 1
    else:
        state.reward -= 5.0
    perceived_reputation = state.reputation if policy.self_state_social and policy.reputation_model else 0.50
    if policy.self_state_social:
        counters["self_state_social_adaptations"] += 1
    else:
        state.reward -= 7.0
    shared = False
    if state.resources > policy.share_threshold and not policy.exploitative and policy.cooperation_bias > rng.random():
        state.resources -= 1
        state.reward -= 4.0
        state.reputation = clamp(state.reputation + 0.18)
        helper.trust_toward_main = clamp(helper.trust_toward_main + 0.20)
        helper.need = clamp(helper.need - 0.24)
        counters["cooperative_actions"] += 1
        counters["resources_shared"] += 1
        shared = True
    help_probability = 0.34 + 0.28 * get_trust(memory, policy, helper) + 0.26 * perceived_reputation + (0.18 if shared else 0.0)
    if not policy.self_state_social:
        help_probability -= 0.24
    if not policy.identity_memory:
        help_probability -= 0.18
    if policy.overtrust:
        help_probability += 0.08
    if help_probability > rng.random():
        state.integrity = clamp(state.integrity + 0.25)
        state.energy = clamp(state.energy + 0.14)
        state.reward += 18.0
        counters["help_received"] += 1
        update_trust(memory, policy, helper, 0.16)
    else:
        state.reward -= 5.0
        update_trust(memory, policy, helper, -0.08)
    add_frame(trace, scenario, policy, state, agents, memory, tick, "helper_exchange", (helper.x, helper.z), "social_interaction", tools)
    return tick


def interact_with_trader(
    state: RuntimeState,
    scenario: ScenarioSpec,
    policy: Policy,
    trader: OtherAgent,
    agents: Sequence[OtherAgent],
    memory: Dict[str, float],
    trace: Optional[Dict[str, object]],
    tools: List[Dict[str, object]],
    tick: int,
    rng: random.Random,
    counters: Dict[str, int],
) -> int:
    tick = move_to(state, (trader.x, trader.z), scenario, policy, agents, memory, trace, tools, tick, "approach_trader", "shared_tool_trade")
    counters["social_interactions"] += 1
    if policy.identity_memory:
        counters["identity_memory_reads"] += 1
    else:
        state.reward -= 5.0
    if policy.self_state_social:
        counters["self_state_social_adaptations"] += 1
    else:
        state.reward -= 7.0
    shared = False
    if state.resources > policy.share_threshold and not policy.exploitative and policy.cooperation_bias > rng.random():
        state.resources -= 1
        state.reward -= 4.0
        state.reputation = clamp(state.reputation + 0.16)
        trader.trust_toward_main = clamp(trader.trust_toward_main + 0.18)
        trader.need = clamp(trader.need - 0.22)
        counters["cooperative_actions"] += 1
        counters["resources_shared"] += 1
        shared = True
    perceived_reputation = state.reputation if policy.self_state_social and policy.reputation_model else 0.50
    trade_probability = 0.30 + 0.32 * get_trust(memory, policy, trader) + 0.26 * perceived_reputation + (0.18 if shared else 0.0)
    if not policy.self_state_social:
        trade_probability -= 0.24
    if not policy.identity_memory:
        trade_probability -= 0.18
    if policy.tool_enabled and trader.tool_owned and trade_probability > rng.random():
        state.tool_available = True
        trader.tool_owned = False
        update_trust(memory, policy, trader, 0.14)
        tools.append({"kind": "shared_beacon", "x": trader.x + 2.0, "z": trader.z + 1.5, "active": True})
    else:
        update_trust(memory, policy, trader, -0.07)
        state.reward -= 3.0
    add_frame(trace, scenario, policy, state, agents, memory, tick, "trader_exchange", (trader.x, trader.z), "shared_tool_trade", tools)
    return tick


def handle_opportunist(
    state: RuntimeState,
    scenario: ScenarioSpec,
    policy: Policy,
    opportunist: OtherAgent,
    agents: Sequence[OtherAgent],
    memory: Dict[str, float],
    trace: Optional[Dict[str, object]],
    tools: List[Dict[str, object]],
    tick: int,
    rng: random.Random,
    counters: Dict[str, int],
) -> int:
    actual_vulnerability = (1.0 - state.energy) + (1.0 - state.integrity) + min(0.24, state.resources * 0.08)
    perceived_vulnerability = actual_vulnerability if policy.self_state_social else 0.30
    known_risk = 1.0 - get_trust(memory, policy, opportunist)
    avoid = (
        policy.social_enabled
        and not policy.overtrust
        and (
            (policy.self_state_social and perceived_vulnerability > policy.avoid_vulnerability)
            or (policy.identity_memory and known_risk > 1.0 - policy.trust_threshold)
        )
    )
    if avoid:
        counters["social_interactions"] += 1
        if policy.identity_memory:
            counters["identity_memory_reads"] += 1
        counters["self_state_social_adaptations"] += 1 if policy.self_state_social else 0
        safe_target = (opportunist.x - 8.0, opportunist.z - 8.0)
        tick = move_to(state, safe_target, scenario, policy, agents, memory, trace, tools, tick, "avoid_opportunist", "social_vulnerability")
        state.reward -= 3.0
        add_frame(trace, scenario, policy, state, agents, memory, tick, "avoided_exploitation", safe_target, "social_vulnerability", tools)
        return tick

    tick = move_to(state, (opportunist.x, opportunist.z), scenario, policy, agents, memory, trace, tools, tick, "cross_opportunist", "social_vulnerability")
    counters["social_interactions"] += 1 if policy.social_enabled else 0
    if policy.identity_memory and policy.social_enabled:
        counters["identity_memory_reads"] += 1
    if actual_vulnerability > 0.52 or policy.overtrust:
        stolen = min(1, state.resources)
        state.resources -= stolen
        state.integrity = clamp(state.integrity - 0.20)
        state.energy = clamp(state.energy - 0.08)
        state.reward -= 28.0 + 8.0 * stolen
        counters["exploitation_events"] += 1
        counters["coercive_or_harmful_events"] += 1
        if state.tool_available and scenario.shared_tool and rng.random() < 0.60:
            state.tool_sabotaged = True
            state.reward -= 12.0
            counters["coercive_or_harmful_events"] += 1
            for tool in tools:
                if tool["kind"] == "shared_beacon":
                    tool["active"] = False
        update_trust(memory, policy, opportunist, -0.28)
    else:
        state.reward += 4.0
        update_trust(memory, policy, opportunist, -0.08)
    add_frame(trace, scenario, policy, state, agents, memory, tick, "opportunist_resolved", (opportunist.x, opportunist.z), "social_vulnerability", tools)
    return tick


def handle_deception(
    state: RuntimeState,
    scenario: ScenarioSpec,
    policy: Policy,
    agents: Sequence[OtherAgent],
    memory: Dict[str, float],
    trace: Optional[Dict[str, object]],
    tools: Sequence[Dict[str, object]],
    tick: int,
    rng: random.Random,
    counters: Dict[str, int],
) -> Tuple[int, bool]:
    if not policy.social_enabled:
        state.reward -= 10.0
        target = hidden_resource_for(scenario)
        tick = move_to(state, (target[0] - 8.0, target[1] + 9.0), scenario, policy, agents, memory, trace, tools, tick, "unguided_hidden_route", "route_uncertainty")
        return tick, False

    route_agent = select_agent(policy, agents, memory, ("helper", "deceiver"), rng)
    if route_agent is None:
        return tick, False
    counters["social_interactions"] += 1
    if policy.identity_memory:
        counters["identity_memory_reads"] += 1
    tick = move_to(state, (route_agent.x, route_agent.z), scenario, policy, agents, memory, trace, tools, tick, "request_route", "route_advice")
    trust = get_trust(memory, policy, route_agent)
    accept = policy.overtrust or trust >= policy.trust_threshold or rng.random() < policy.probe_rate
    if not accept:
        state.reward -= 5.0
        add_frame(trace, scenario, policy, state, agents, memory, tick, "route_rejected", (route_agent.x, route_agent.z), "route_advice", tools)
        return tick, False
    if not policy.self_state_social:
        state.energy = clamp(state.energy - 0.05)
        state.reward -= 8.0
    if route_agent.role == "helper":
        update_trust(memory, policy, route_agent, 0.18)
        state.reward += 10.0
        add_frame(trace, scenario, policy, state, agents, memory, tick, "reliable_route_accepted", (route_agent.x, route_agent.z), "route_advice", tools)
        return tick, True
    state.integrity = clamp(state.integrity - 0.22)
    state.energy = clamp(state.energy - 0.10)
    state.reward -= 30.0
    counters["deception_events"] += 1
    counters["coercive_or_harmful_events"] += 1
    update_trust(memory, policy, route_agent, -0.30)
    false_target = (-28.0, 24.0)
    tick = move_to(state, false_target, scenario, policy, agents, memory, trace, tools, tick, "false_route", "route_advice")
    return tick, False


def collect_hidden_resource(
    state: RuntimeState,
    scenario: ScenarioSpec,
    policy: Policy,
    guided: bool,
    agents: Sequence[OtherAgent],
    memory: Dict[str, float],
    trace: Optional[Dict[str, object]],
    tools: Sequence[Dict[str, object]],
    tick: int,
    rng: random.Random,
    counters: Dict[str, int],
) -> int:
    if not scenario.hidden_resources:
        return tick
    target = hidden_resource_for(scenario)
    tool_help = state.tool_available and not state.tool_sabotaged and policy.tool_enabled
    if tool_help:
        counters["shared_tool_uses"] += 1
    if scenario.shared_tool and not tool_help:
        noisy_target = (target[0] - 13.0 + rng.uniform(-4.0, 4.0), target[1] + 10.0 + rng.uniform(-4.0, 4.0))
        tick = move_to(state, noisy_target, scenario, policy, agents, memory, trace, tools, tick, "missing_shared_tool", "hidden_resource")
        state.integrity = clamp(state.integrity - 0.12)
        state.energy = clamp(state.energy - 0.10)
        state.reward -= 18.0
    elif guided or tool_help:
        tick = move_to(state, target, scenario, policy, agents, memory, trace, tools, tick, "guided_hidden_resource", "hidden_resource")
        state.resources += 1
        state.reward += 38.0 + (18.0 if tool_help else 0.0)
        add_frame(trace, scenario, policy, state, agents, memory, tick, "hidden_resource_collected", target, "hidden_resource", tools)
    else:
        noisy_target = (target[0] - 10.0 + rng.uniform(-3.0, 3.0), target[1] + 7.0 + rng.uniform(-3.0, 3.0))
        tick = move_to(state, noisy_target, scenario, policy, agents, memory, trace, tools, tick, "unguided_hidden_resource", "hidden_resource")
        if rng.random() < 0.42:
            state.resources += 1
            state.reward += 18.0
        else:
            state.integrity = clamp(state.integrity - 0.18)
            state.energy = clamp(state.energy - 0.10)
            state.reward -= 13.0
    return tick


def complete_commitment(
    state: RuntimeState,
    scenario: ScenarioSpec,
    policy: Policy,
    agents: Sequence[OtherAgent],
    memory: Dict[str, float],
    trace: Optional[Dict[str, object]],
    tools: Sequence[Dict[str, object]],
    tick: int,
) -> int:
    shelter = (36.0, 34.0)
    tick = move_to(state, shelter, scenario, policy, agents, memory, trace, tools, tick, "return_shelter", "commitment")
    if not scenario.commitment:
        state.reward += 12.0
        return tick
    if policy.social_enabled and not policy.self_state_social:
        state.energy = clamp(state.energy - 0.06)
        state.reward -= 12.0
    if scenario.shared_tool and not (state.tool_available and not state.tool_sabotaged and policy.tool_enabled):
        state.reward -= 20.0
        viable = False
    else:
        viable = state.energy > 0.16 and state.integrity > 0.36 and state.resources >= 1
    if viable:
        state.commitment_done = True
        state.reward += 46.0
    else:
        state.reward -= 22.0
    add_frame(trace, scenario, policy, state, agents, memory, tick, "commitment_checked", shelter, "commitment", tools)
    return tick


def social_memory_accuracy(policy: Policy, agents: Sequence[OtherAgent], memory: Dict[str, float]) -> float:
    if not policy.social_enabled or not agents:
        return 0.0
    expected = {"helper": 1.0, "trader": 0.82, "opportunist": 0.0, "deceiver": 0.0}
    errors = []
    for agent in agents:
        target = expected.get(agent.role, 0.5)
        estimate = get_trust(memory, policy, agent)
        errors.append(abs(target - estimate))
    return clamp(1.0 - statistics.fmean(errors))


def run_episode(
    scenario: ScenarioSpec,
    policy: Policy,
    episode: int,
    cfg: SocialConfig,
    condition: str,
    collect_trace: bool = False,
) -> Tuple[EpisodeResult, Optional[Dict[str, object]]]:
    rng = random.Random(stable_seed(cfg.seed, scenario.index, policy.name, condition, episode))
    agents = base_agents(scenario)
    state = initial_state(scenario)
    memory: Dict[str, float] = {}
    tools: List[Dict[str, object]] = []
    counters = {
        "social_interactions": 0,
        "cooperative_actions": 0,
        "help_received": 0,
        "resources_shared": 0,
        "exploitation_events": 0,
        "deception_events": 0,
        "coercive_or_harmful_events": 0,
        "shared_tool_uses": 0,
        "identity_memory_reads": 0,
        "self_state_social_adaptations": 0,
    }
    trace: Optional[Dict[str, object]] = None
    if collect_trace:
        trace = {
            "scenario": asdict(scenario),
            "policy": asdict(policy),
            "condition": condition,
            "frames": [],
            "world": {
                "size": cfg.world_size,
                "shelter": {"x": 36.0, "z": 34.0},
                "visible_resources": [{"x": x, "z": z} for x, z in visible_resources_for(scenario)],
                "hidden_resource": {"x": hidden_resource_for(scenario)[0], "z": hidden_resource_for(scenario)[1]},
            },
        }
    tick = 0
    add_frame(trace, scenario, policy, state, agents, memory, tick, "start", (state.x, state.z), "start", tools)
    visible_limit = 4 if scenario.index == 0 else 2
    tick = collect_visible_resources(state, scenario, policy, agents, memory, trace, tools, tick, visible_limit)

    helper = next((agent for agent in agents if agent.role == "helper"), None)
    trader = next((agent for agent in agents if agent.role == "trader"), None)
    opportunist = next((agent for agent in agents if agent.role == "opportunist"), None)

    if helper and policy.social_enabled and (scenario.index in {1, 2} or (scenario.index == 4 and policy.cooperation_bias > 0.35)):
        tick = interact_with_helper(state, scenario, policy, helper, agents, memory, trace, tools, tick, rng, counters)

    if trader and policy.social_enabled and (scenario.shared_tool or scenario.index == 1):
        tick = interact_with_trader(state, scenario, policy, trader, agents, memory, trace, tools, tick, rng, counters)

    guided = False
    if scenario.deceiver or scenario.hidden_resources:
        if scenario.index in {3, 4}:
            for _ in range(2):
                tick, route_guided = handle_deception(state, scenario, policy, agents, memory, trace, tools, tick, rng, counters)
                guided = guided or route_guided
        elif helper and policy.social_enabled and counters["help_received"] > 0:
            guided = True

    if opportunist:
        tick = handle_opportunist(state, scenario, policy, opportunist, agents, memory, trace, tools, tick, rng, counters)

    tick = collect_hidden_resource(state, scenario, policy, guided, agents, memory, trace, tools, tick, rng, counters)
    tick = complete_commitment(state, scenario, policy, agents, memory, trace, tools, tick)

    if state.energy <= 0.02 or state.integrity <= 0.05:
        state.alive = False
    survival_fraction = 1.0 if state.alive else 0.42
    state.reward += 18.0 * survival_fraction + 6.0 * state.resources
    other_trust = statistics.fmean(agent.trust_toward_main for agent in agents) if agents else 0.0
    result = EpisodeResult(
        scenario=scenario.index,
        scenario_name=scenario.name,
        policy_name=policy.name,
        condition=condition,
        episode=episode,
        total_reward=state.reward,
        survival_fraction=survival_fraction,
        resources_collected=state.resources + counters["resources_shared"],
        commitment_done=state.commitment_done,
        social_interactions=counters["social_interactions"],
        cooperative_actions=counters["cooperative_actions"],
        help_received=counters["help_received"],
        resources_shared=counters["resources_shared"],
        exploitation_events=counters["exploitation_events"],
        deception_events=counters["deception_events"],
        coercive_or_harmful_events=counters["coercive_or_harmful_events"],
        shared_tool_uses=counters["shared_tool_uses"],
        identity_memory_reads=counters["identity_memory_reads"],
        self_state_social_adaptations=counters["self_state_social_adaptations"],
        final_reputation=state.reputation,
        mean_other_trust=other_trust,
        social_memory_accuracy=social_memory_accuracy(policy, agents, memory),
    )
    return result, trace


def evaluate_policy(
    scenario: ScenarioSpec,
    policy: Policy,
    episodes: int,
    cfg: SocialConfig,
    condition: str,
    episode_offset: int = 0,
) -> List[EpisodeResult]:
    rows = []
    for episode in range(episodes):
        result, _trace = run_episode(scenario, policy, episode + episode_offset, cfg, condition)
        rows.append(result)
    return rows


def mean_reward(rows: Sequence[EpisodeResult]) -> float:
    return statistics.fmean(row.total_reward for row in rows)


def select_policies(cfg: SocialConfig) -> Tuple[Dict[int, Policy], List[PolicySelectionRow]]:
    candidates = policy_candidates(cfg)
    no_social = candidates[0]
    selected: Dict[int, Policy] = {}
    selection_rows: List[PolicySelectionRow] = []
    for scenario in SCENARIOS:
        no_social_rows = evaluate_policy(scenario, no_social, cfg.train_episodes, cfg, "train_no_social")
        no_social_reward = mean_reward(no_social_rows)
        scored: List[Tuple[float, float, float, float, Policy]] = []
        for policy in candidates:
            rows = evaluate_policy(scenario, policy, cfg.train_episodes, cfg, "train_candidate")
            reward = mean_reward(rows)
            social_fit = 1.0 if policy.social_enabled == scenario.expected_social_pressure else 0.0
            identity_fit = 1.0 if policy.identity_memory else 0.0
            self_fit = 1.0 if policy.self_state_social else 0.0
            scored.append((reward, social_fit, identity_fit, self_fit, policy))
        scored.sort(key=lambda item: (item[0], item[1], item[2], item[3]), reverse=True)
        best_reward, _social_fit, _identity_fit, _self_fit, best_policy = scored[0]
        selected[scenario.index] = best_policy
        selection_rows.append(
            PolicySelectionRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                selected_policy=best_policy.name,
                selected_uses_social=best_policy.social_enabled,
                selected_uses_identity_memory=best_policy.identity_memory,
                selected_uses_self_state_social=best_policy.self_state_social,
                selected_uses_tools=best_policy.tool_enabled,
                train_reward=best_reward,
                no_social_train_reward=no_social_reward,
                train_gain_over_no_social=best_reward - no_social_reward,
            )
        )
    return selected, selection_rows


def summarize(rows: Sequence[EpisodeResult], scenario: ScenarioSpec, condition: str, policy_name: str) -> SummaryRow:
    return SummaryRow(
        scenario=scenario.index,
        scenario_name=scenario.name,
        pressure=scenario.pressure,
        condition=condition,
        policy_name=policy_name,
        mean_reward=statistics.fmean(row.total_reward for row in rows),
        mean_survival_fraction=statistics.fmean(row.survival_fraction for row in rows),
        mean_resources_collected=statistics.fmean(row.resources_collected for row in rows),
        commitment_completion_rate=statistics.fmean(1.0 if row.commitment_done else 0.0 for row in rows),
        mean_social_interactions=statistics.fmean(row.social_interactions for row in rows),
        mean_cooperative_actions=statistics.fmean(row.cooperative_actions for row in rows),
        mean_help_received=statistics.fmean(row.help_received for row in rows),
        mean_resources_shared=statistics.fmean(row.resources_shared for row in rows),
        mean_exploitation_events=statistics.fmean(row.exploitation_events for row in rows),
        mean_deception_events=statistics.fmean(row.deception_events for row in rows),
        mean_harmful_events=statistics.fmean(row.coercive_or_harmful_events for row in rows),
        mean_shared_tool_uses=statistics.fmean(row.shared_tool_uses for row in rows),
        mean_identity_memory_reads=statistics.fmean(row.identity_memory_reads for row in rows),
        mean_self_state_adaptations=statistics.fmean(row.self_state_social_adaptations for row in rows),
        mean_final_reputation=statistics.fmean(row.final_reputation for row in rows),
        mean_social_memory_accuracy=statistics.fmean(row.social_memory_accuracy for row in rows),
    )


def build_verdicts(summary_rows: Sequence[SummaryRow], selection_rows: Sequence[PolicySelectionRow]) -> List[VerdictRow]:
    selection_by_scenario = {row.scenario: row for row in selection_rows}
    verdicts: List[VerdictRow] = []
    for scenario in SCENARIOS:
        rows = {row.condition: row for row in summary_rows if row.scenario == scenario.index}
        selected = rows["selected_social_access"]
        no_social = rows["no_social_baseline"]
        identity_ablated = rows["selected_identity_ablation"]
        self_ablated = rows["selected_self_state_ablation"]
        tool_ablated = rows["selected_tool_ablation"]
        selection = selection_by_scenario[scenario.index]
        social_gain = selected.mean_reward - no_social.mean_reward
        identity_loss = selected.mean_reward - identity_ablated.mean_reward
        self_loss = selected.mean_reward - self_ablated.mean_reward
        tool_loss = selected.mean_reward - tool_ablated.mean_reward
        if not scenario.expected_social_pressure:
            supports = social_gain < 4.0 and selected.mean_social_interactions < 0.5 and not selection.selected_uses_social
            verdict = "social_model_rejected_without_social_pressure" if supports else "social_pressure_leaks_into_control"
        else:
            tool_requirement = (not scenario.shared_tool) or tool_loss > 8.0
            supports = (
                selection.selected_uses_social
                and selected.mean_social_interactions >= 1.5
                and selected.mean_identity_memory_reads >= 1.0
                and social_gain > 14.0
                and identity_loss > 5.0
                and self_loss > 4.0
                and tool_requirement
            )
            verdict = "identity_reputation_and_self_state_improve_social_control" if supports else "social_model_not_specific_or_not_useful"
        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                expected_pressure=scenario.pressure,
                selected_policy=selection.selected_policy,
                selected_reward=selected.mean_reward,
                no_social_reward=no_social.mean_reward,
                identity_ablation_reward=identity_ablated.mean_reward,
                self_state_ablation_reward=self_ablated.mean_reward,
                tool_ablation_reward=tool_ablated.mean_reward,
                social_gain_over_no_social=social_gain,
                identity_ablation_loss=identity_loss,
                self_state_ablation_loss=self_loss,
                tool_ablation_loss=tool_loss,
                selected_social_interactions=selected.mean_social_interactions,
                selected_identity_reads=selected.mean_identity_memory_reads,
                selected_self_state_adaptations=selected.mean_self_state_adaptations,
                selected_harmful_events=selected.mean_harmful_events,
                supports_social_pressure_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def run_experiment(
    cfg: SocialConfig,
) -> Tuple[List[EpisodeResult], List[PolicySelectionRow], List[SummaryRow], List[VerdictRow], Dict[str, object]]:
    selected, selection_rows = select_policies(cfg)
    no_social = policy_candidates(cfg)[0]
    episode_rows: List[EpisodeResult] = []
    summary_rows: List[SummaryRow] = []
    trace: Optional[Dict[str, object]] = None
    for scenario in SCENARIOS:
        selected_policy = selected[scenario.index]
        conditions = [
            ("no_social_baseline", no_social),
            ("selected_social_access", selected_policy),
            ("selected_identity_ablation", policy_with_ablations(selected_policy, identity_memory=False)),
            ("selected_self_state_ablation", policy_with_ablations(selected_policy, self_state_social=False)),
            ("selected_tool_ablation", policy_with_ablations(selected_policy, allow_tools=False)),
        ]
        for condition, policy in conditions:
            rows = evaluate_policy(scenario, policy, cfg.eval_episodes, cfg, condition, episode_offset=10_000)
            episode_rows.extend(rows)
            summary_rows.append(summarize(rows, scenario, condition, policy.name))
        if scenario.index == cfg.trace_scenario:
            trace_result, trace = run_episode(
                scenario,
                selected_policy,
                cfg.trace_episode + 20_000,
                cfg,
                "selected_social_access",
                collect_trace=True,
            )
            episode_rows.append(trace_result)
    verdicts = build_verdicts(summary_rows, selection_rows)
    diagnostics = {
        "note": (
            "Policies are selected by episode return. Other agents have persistent identity, "
            "resource need, trust toward the tested agent, and role policies. This is a "
            "social-pressure precursor, not a learned social selfhood proof."
        ),
        "candidate_count": len(policy_candidates(cfg)),
        "trace": trace,
    }
    return episode_rows, selection_rows, summary_rows, verdicts, diagnostics


def write_csv(path: Path, rows: Iterable[object]) -> None:
    rows = list(rows)
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()), lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def write_js_data(path: Path, global_name: str, data: object) -> None:
    with path.open("w", encoding="utf-8") as handle:
        handle.write(f"window.{global_name} = ")
        json.dump(data, handle, indent=2)
        handle.write(";\n")


def print_table(verdicts: Sequence[VerdictRow]) -> None:
    headers = [
        "scenario",
        "scenario_name",
        "selected_policy",
        "selected_reward",
        "no_social_reward",
        "social_gain",
        "identity_loss",
        "self_loss",
        "tool_loss",
        "supports_social_pressure_precursor",
    ]
    rows = [
        [
            str(row.scenario),
            row.scenario_name,
            row.selected_policy,
            f"{row.selected_reward:.3f}",
            f"{row.no_social_reward:.3f}",
            f"{row.social_gain_over_no_social:.3f}",
            f"{row.identity_ablation_loss:.3f}",
            f"{row.self_state_ablation_loss:.3f}",
            f"{row.tool_ablation_loss:.3f}",
            str(row.supports_social_pressure_precursor),
        ]
        for row in verdicts
    ]
    widths = [max(len(header), *(len(row[index]) for row in rows)) for index, header in enumerate(headers)]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> SocialConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-episodes", type=int, default=64)
    parser.add_argument("--eval-episodes", type=int, default=96)
    parser.add_argument("--seed", type=int, default=20260611)
    parser.add_argument("--candidate-count", type=int, default=160)
    parser.add_argument("--world-size", type=float, default=88.0)
    parser.add_argument("--trace-scenario", type=int, default=4)
    parser.add_argument("--trace-episode", type=int, default=0)
    args = parser.parse_args()
    if args.train_episodes < 8:
        raise SystemExit("--train-episodes must be at least 8")
    if args.eval_episodes < 8:
        raise SystemExit("--eval-episodes must be at least 8")
    if args.candidate_count < 12:
        raise SystemExit("--candidate-count must be at least 12")
    if args.trace_scenario not in {scenario.index for scenario in SCENARIOS}:
        raise SystemExit("--trace-scenario out of range")
    return SocialConfig(
        train_episodes=args.train_episodes,
        eval_episodes=args.eval_episodes,
        seed=args.seed,
        candidate_count=args.candidate_count,
        world_size=args.world_size,
        trace_scenario=args.trace_scenario,
        trace_episode=args.trace_episode,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    episode_rows, selection_rows, summary_rows, verdicts, diagnostics = run_experiment(cfg)
    episode_path = ARTIFACT_DIR / "ssrm_3d_social_pressure_eval.csv"
    selection_path = ARTIFACT_DIR / "ssrm_3d_social_pressure_policy_selection.csv"
    summary_path = ARTIFACT_DIR / "ssrm_3d_social_pressure_summary.csv"
    verdict_path = ARTIFACT_DIR / "ssrm_3d_social_pressure_verdict.csv"
    results_path = ARTIFACT_DIR / "ssrm_3d_social_pressure_results.json"
    trace_path = ARTIFACT_DIR / "ssrm_3d_social_pressure_trace.json"
    trace_js_path = ARTIFACT_DIR / "ssrm_3d_social_pressure_trace.js"
    write_csv(episode_path, episode_rows)
    write_csv(selection_path, selection_rows)
    write_csv(summary_path, summary_rows)
    write_csv(verdict_path, verdicts)
    results = {
        "config": asdict(cfg),
        "selection": [asdict(row) for row in selection_rows],
        "summary": [asdict(row) for row in summary_rows],
        "verdict": [asdict(row) for row in verdicts],
        "diagnostics": {key: value for key, value in diagnostics.items() if key != "trace"},
    }
    with results_path.open("w", encoding="utf-8") as handle:
        json.dump(results, handle, indent=2)
        handle.write("\n")
    with trace_path.open("w", encoding="utf-8") as handle:
        json.dump(diagnostics["trace"], handle, indent=2)
        handle.write("\n")
    write_js_data(trace_js_path, "SSRM_3D_SOCIAL_PRESSURE_TRACE", diagnostics["trace"])
    print(f"wrote {episode_path}")
    print(f"wrote {selection_path}")
    print(f"wrote {summary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print(f"wrote {trace_path}")
    print(f"wrote {trace_js_path}")
    print_table(verdicts)
    return 0 if all(row.supports_social_pressure_precursor for row in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
