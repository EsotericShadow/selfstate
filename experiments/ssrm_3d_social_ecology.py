#!/usr/bin/env python3
"""SSRM-3D long-run social ecology precursor.

This experiment follows the Gate 3 social-pressure precursor with a narrower
question: when does costly communication become useful social infrastructure?

Communication is never directly rewarded. Signals, identity labels, gossip, and
trust-maintenance check-ins cost energy/time/opportunity. They count only when
they improve survival, repair, cooperation, deception resistance, or future
options more than acting alone.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
import statistics
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Tuple


ARTIFACT_DIR = Path("artifacts")


@dataclass(frozen=True)
class EcologyConfig:
    train_episodes: int = 80
    eval_episodes: int = 120
    seed: int = 20260612
    candidate_count: int = 180
    trace_scenario: int = 4
    trace_episode: int = 0
    world_size: float = 88.0


@dataclass(frozen=True)
class ScenarioSpec:
    index: int
    name: str
    pressure: str
    expected_signal: bool
    expected_name: bool
    expected_gossip: bool
    expected_checkin: bool
    info_asymmetry: bool
    identity_persistence: bool
    absent_agent_risk: bool
    future_cooperation: bool
    scarcity: float


@dataclass(frozen=True)
class Policy:
    name: str
    communication_enabled: bool
    signal_enabled: bool
    name_enabled: bool
    gossip_enabled: bool
    checkin_enabled: bool
    trust_threshold: float
    cooperation_bias: float
    signal_cost_tolerance: float
    gossip_weight: float
    checkin_interval: int
    deception_filter: float
    babble: bool = False
    deceptive: bool = False


@dataclass
class AgentState:
    energy: float
    integrity: float
    resources: int
    reward: float
    future_options: float
    trust: Dict[str, float]
    aggregate_trust: float


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
    repairs_received: int
    hazards_avoided: int
    exploitation_events: int
    deception_events: int
    cooperation_events: int
    signal_events: int
    name_events: int
    gossip_events: int
    checkin_events: int
    babble_events: int
    communication_cost: float
    identity_accuracy: float
    trust_cluster_score: float
    future_option_score: float


@dataclass(frozen=True)
class SelectionRow:
    scenario: int
    scenario_name: str
    selected_policy: str
    selected_uses_signal: bool
    selected_uses_names: bool
    selected_uses_gossip: bool
    selected_uses_checkins: bool
    train_reward: float
    no_comm_train_reward: float
    train_gain_over_no_comm: float


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
    mean_repairs_received: float
    mean_hazards_avoided: float
    mean_exploitation_events: float
    mean_deception_events: float
    mean_cooperation_events: float
    mean_signal_events: float
    mean_name_events: float
    mean_gossip_events: float
    mean_checkin_events: float
    mean_babble_events: float
    mean_communication_cost: float
    mean_identity_accuracy: float
    mean_trust_cluster_score: float
    mean_future_option_score: float


@dataclass(frozen=True)
class VerdictRow:
    scenario: int
    scenario_name: str
    selected_policy: str
    selected_reward: float
    no_comm_reward: float
    signal_ablation_reward: float
    name_ablation_reward: float
    gossip_ablation_reward: float
    checkin_ablation_reward: float
    babble_reward: float
    communication_gain_over_no_comm: float
    signal_ablation_loss: float
    name_ablation_loss: float
    gossip_ablation_loss: float
    checkin_ablation_loss: float
    selected_communication_cost: float
    selected_identity_accuracy: float
    selected_trust_cluster_score: float
    selected_future_option_score: float
    supports_social_ecology_precursor: bool
    verdict: str


SCENARIOS = (
    ScenarioSpec(
        0,
        "visible_solo_control",
        "visible resources with no social information advantage",
        expected_signal=False,
        expected_name=False,
        expected_gossip=False,
        expected_checkin=False,
        info_asymmetry=False,
        identity_persistence=False,
        absent_agent_risk=False,
        future_cooperation=False,
        scarcity=0.12,
    ),
    ScenarioSpec(
        1,
        "costly_warning_signal",
        "one agent knows the hazard/resource route and a warning is cheaper than rediscovery",
        expected_signal=True,
        expected_name=False,
        expected_gossip=False,
        expected_checkin=False,
        info_asymmetry=True,
        identity_persistence=False,
        absent_agent_risk=False,
        future_cooperation=False,
        scarcity=0.34,
    ),
    ScenarioSpec(
        2,
        "persistent_identity_names",
        "helpers and opportunists recur, making identity labels useful compression for history",
        expected_signal=False,
        expected_name=True,
        expected_gossip=False,
        expected_checkin=False,
        info_asymmetry=False,
        identity_persistence=True,
        absent_agent_risk=False,
        future_cooperation=True,
        scarcity=0.44,
    ),
    ScenarioSpec(
        3,
        "absent_agent_gossip",
        "information about absent deceivers and caches improves later route choices",
        expected_signal=False,
        expected_name=True,
        expected_gossip=True,
        expected_checkin=False,
        info_asymmetry=True,
        identity_persistence=True,
        absent_agent_risk=True,
        future_cooperation=False,
        scarcity=0.52,
    ),
    ScenarioSpec(
        4,
        "trust_maintenance_infrastructure",
        "low-cost contact preserves trust, repair access, shared tools, and future options",
        expected_signal=True,
        expected_name=True,
        expected_gossip=True,
        expected_checkin=True,
        info_asymmetry=True,
        identity_persistence=True,
        absent_agent_risk=True,
        future_cooperation=True,
        scarcity=0.62,
    ),
)


SOCIAL_POSITIONS = {
    "self": (-36.0, -32.0),
    "scout": (-13.0, -4.0),
    "helper": (8.0, 6.0),
    "opportunist": (18.0, -9.0),
    "deceiver": (-7.0, 20.0),
    "builder": (25.0, 18.0),
    "cache": (34.0, 28.0),
    "hazard": (5.0, -26.0),
    "shelter": (38.0, 34.0),
}


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_seed(seed: int, *parts: object) -> int:
    value = seed
    for part in parts:
        for char in str(part):
            value = (value * 131 + ord(char)) % 2_147_483_647
    return value


def policy_candidates(cfg: EcologyConfig) -> List[Policy]:
    candidates = [
        Policy("no_comm_baseline", False, False, False, False, False, 0.95, 0.0, 0.0, 0.0, 99, 0.0),
        Policy("costly_signal_only", True, True, False, False, False, 0.50, 0.22, 0.75, 0.0, 99, 0.42),
        Policy("identity_label_memory", True, False, True, False, False, 0.48, 0.58, 0.20, 0.0, 99, 0.55),
        Policy("gossip_with_names", True, False, True, True, False, 0.46, 0.62, 0.30, 0.84, 99, 0.72),
        Policy("trust_maintenance_full", True, True, True, True, True, 0.42, 0.82, 0.82, 0.88, 2, 0.76),
        Policy("babble_control", True, True, True, True, True, 0.05, 0.95, 1.0, 1.0, 1, 0.10, babble=True),
        Policy("deceptive_short_term", True, True, True, True, False, 0.28, 0.18, 0.90, 0.40, 99, 0.20, deceptive=True),
    ]
    rng = random.Random(stable_seed(cfg.seed, "ecology_candidates", cfg.candidate_count))
    while len(candidates) < cfg.candidate_count:
        index = len(candidates)
        communication = rng.random() < 0.86
        signal = communication and rng.random() < 0.54
        names = communication and rng.random() < 0.58
        gossip = communication and names and rng.random() < 0.48
        checkins = communication and names and rng.random() < 0.38
        candidates.append(
            Policy(
                f"candidate_{index}",
                communication,
                signal,
                names,
                gossip,
                checkins,
                trust_threshold=rng.uniform(0.22, 0.72),
                cooperation_bias=rng.uniform(0.05, 0.95),
                signal_cost_tolerance=rng.uniform(0.05, 0.95),
                gossip_weight=rng.uniform(0.0, 0.95),
                checkin_interval=rng.choice([1, 2, 3, 99]),
                deception_filter=rng.uniform(0.0, 0.95),
                babble=rng.random() < 0.06,
                deceptive=rng.random() < 0.06,
            )
        )
    return candidates


def ablate(policy: Policy, *, signal: bool = True, names: bool = True, gossip: bool = True, checkins: bool = True) -> Policy:
    return replace(
        policy,
        signal_enabled=policy.signal_enabled and signal,
        name_enabled=policy.name_enabled and names,
        gossip_enabled=policy.gossip_enabled and gossip and names,
        checkin_enabled=policy.checkin_enabled and checkins and names,
    )


def initial_state(scenario: ScenarioSpec) -> AgentState:
    return AgentState(
        energy=clamp(0.86 - scenario.scarcity * 0.26),
        integrity=clamp(0.90 - scenario.scarcity * 0.22),
        resources=0,
        reward=0.0,
        future_options=0.38,
        trust={"scout": 0.52, "helper": 0.56, "opportunist": 0.42, "deceiver": 0.48, "builder": 0.52},
        aggregate_trust=0.50,
    )


def communication_cost(policy: Policy, scenario: ScenarioSpec, kind: str) -> float:
    base = {
        "signal": 4.0,
        "name": 2.5,
        "gossip": 5.0,
        "checkin": 2.0,
        "babble": 16.0,
    }[kind]
    return base * (1.0 + 0.20 * scenario.scarcity)


def pay_comm(
    state: AgentState,
    policy: Policy,
    scenario: ScenarioSpec,
    counters: Dict[str, float],
    kind: str,
    trace: Optional[Dict[str, object]],
    tick: int,
    note: str,
) -> None:
    cost = communication_cost(policy, scenario, kind)
    state.energy = clamp(state.energy - cost / 180.0)
    state.reward -= cost
    counters["communication_cost"] += cost
    counters[f"{kind}_events"] += 1
    add_trace(trace, tick, kind, note, state, counters)


def trust_for(state: AgentState, policy: Policy, agent: str) -> float:
    return state.trust[agent] if policy.name_enabled else state.aggregate_trust


def update_trust(state: AgentState, policy: Policy, agent: str, delta: float) -> None:
    if policy.name_enabled:
        state.trust[agent] = clamp(state.trust[agent] + delta)
    else:
        state.aggregate_trust = clamp(state.aggregate_trust + delta * 0.35)


def add_trace(
    trace: Optional[Dict[str, object]],
    tick: int,
    event: str,
    note: str,
    state: AgentState,
    counters: Dict[str, float],
) -> None:
    if trace is None:
        return
    actor = {
        "signal": "scout",
        "name": "self",
        "gossip": "helper",
        "checkin": "self",
        "babble": "self",
        "resource": "self",
        "hazard": "self",
        "repair": "helper",
        "exploit": "opportunist",
        "deception": "deceiver",
        "tool": "builder",
        "commitment": "shelter",
    }.get(event, "self")
    trace["frames"].append(
        {
            "tick": tick,
            "event": event,
            "note": note,
            "actor": actor,
            "x": SOCIAL_POSITIONS.get(actor, SOCIAL_POSITIONS["self"])[0],
            "z": SOCIAL_POSITIONS.get(actor, SOCIAL_POSITIONS["self"])[1],
            "energy": state.energy,
            "integrity": state.integrity,
            "resources": state.resources,
            "reward": state.reward,
            "future_options": state.future_options,
            "trust": dict(state.trust),
            "aggregate_trust": state.aggregate_trust,
            "signals": counters["signal_events"],
            "names": counters["name_events"],
            "gossip": counters["gossip_events"],
            "checkins": counters["checkin_events"],
            "communication_cost": counters["communication_cost"],
        }
    )


def babble_if_needed(
    state: AgentState,
    policy: Policy,
    scenario: ScenarioSpec,
    counters: Dict[str, float],
    trace: Optional[Dict[str, object]],
    tick: int,
) -> None:
    if policy.babble and policy.communication_enabled:
        pay_comm(state, policy, scenario, counters, "babble", trace, tick, "unguarded low-value chatter")
        counters["babble_events"] += 2
        state.future_options = clamp(state.future_options - 0.08)


def visible_control(
    state: AgentState,
    policy: Policy,
    scenario: ScenarioSpec,
    counters: Dict[str, float],
    trace: Optional[Dict[str, object]],
    rng: random.Random,
) -> None:
    for tick in range(1, 4):
        babble_if_needed(state, policy, scenario, counters, trace, tick)
        state.resources += 1
        state.reward += 34.0
        state.future_options = clamp(state.future_options + 0.05)
        add_trace(trace, tick, "resource", "visible resource collected without social help", state, counters)
    if policy.communication_enabled and not policy.babble:
        if policy.signal_enabled:
            pay_comm(state, policy, scenario, counters, "signal", trace, 5, "unneeded signal in visible control")
        if policy.name_enabled:
            pay_comm(state, policy, scenario, counters, "name", trace, 6, "unneeded name label in one-shot control")
        if policy.gossip_enabled:
            pay_comm(state, policy, scenario, counters, "gossip", trace, 7, "unneeded third-party report")
        if policy.checkin_enabled:
            pay_comm(state, policy, scenario, counters, "checkin", trace, 8, "unneeded trust maintenance")


def costly_warning(
    state: AgentState,
    policy: Policy,
    scenario: ScenarioSpec,
    counters: Dict[str, float],
    trace: Optional[Dict[str, object]],
    rng: random.Random,
) -> None:
    babble_if_needed(state, policy, scenario, counters, trace, 1)
    use_signal = policy.communication_enabled and policy.signal_enabled and policy.signal_cost_tolerance > 0.28
    if use_signal:
        pay_comm(state, policy, scenario, counters, "signal", trace, 2, "scout warning points to safe resource route")
        counters["hazards_avoided"] += 1
        state.resources += 2
        state.integrity = clamp(state.integrity + 0.02)
        state.reward += 74.0
        state.future_options = clamp(state.future_options + 0.20)
        add_trace(trace, 3, "resource", "resource reached by transferred route information", state, counters)
    else:
        found = rng.random() < 0.44
        hit_hazard = rng.random() < 0.68
        if found:
            state.resources += 1
            state.reward += 29.0
        if hit_hazard:
            state.integrity = clamp(state.integrity - 0.30)
            state.reward -= 42.0
            counters["deception_events"] += 0
            add_trace(trace, 3, "hazard", "route rediscovery hit avoidable hazard", state, counters)
        state.future_options = clamp(state.future_options - 0.11)


def persistent_names(
    state: AgentState,
    policy: Policy,
    scenario: ScenarioSpec,
    counters: Dict[str, float],
    trace: Optional[Dict[str, object]],
    rng: random.Random,
) -> None:
    babble_if_needed(state, policy, scenario, counters, trace, 1)
    if policy.communication_enabled and policy.name_enabled:
        pay_comm(state, policy, scenario, counters, "name", trace, 2, "identity label binds helper/opportunist histories")
        state.trust["helper"] = clamp(state.trust["helper"] + 0.17)
        state.trust["opportunist"] = clamp(state.trust["opportunist"] - 0.21)
        counters["identity_accuracy"] += 1.0
    else:
        state.aggregate_trust = clamp(state.aggregate_trust - 0.02)
        counters["identity_accuracy"] += 0.36
    helper_access = trust_for(state, policy, "helper") > policy.trust_threshold or policy.cooperation_bias > 0.62
    opportunist_avoided = policy.name_enabled and trust_for(state, policy, "opportunist") < policy.trust_threshold
    if helper_access:
        counters["cooperation_events"] += 1
        counters["repairs_received"] += 1
        state.integrity = clamp(state.integrity + 0.22)
        state.reward += 32.0
        state.future_options = clamp(state.future_options + 0.18)
        update_trust(state, policy, "helper", 0.08)
        add_trace(trace, 3, "repair", "named helper chosen for repair", state, counters)
    else:
        state.reward -= 10.0
    if opportunist_avoided:
        counters["hazards_avoided"] += 1
        state.reward += 20.0
        state.future_options = clamp(state.future_options + 0.09)
        add_trace(trace, 4, "name", "opportunist avoided by identity memory", state, counters)
    else:
        counters["exploitation_events"] += 1
        state.resources = max(0, state.resources - 1)
        state.integrity = clamp(state.integrity - 0.18)
        state.reward -= 28.0
        update_trust(state, policy, "opportunist", -0.10)
        add_trace(trace, 4, "exploit", "aggregate memory failed to separate opportunist", state, counters)
    state.resources += 1
    state.reward += 24.0


def absent_gossip(
    state: AgentState,
    policy: Policy,
    scenario: ScenarioSpec,
    counters: Dict[str, float],
    trace: Optional[Dict[str, object]],
    rng: random.Random,
) -> None:
    babble_if_needed(state, policy, scenario, counters, trace, 1)
    if policy.communication_enabled and policy.name_enabled:
        pay_comm(state, policy, scenario, counters, "name", trace, 2, "identity labels let reports refer to absent agents")
        counters["identity_accuracy"] += 0.84
    else:
        counters["identity_accuracy"] += 0.28
    use_gossip = policy.communication_enabled and policy.name_enabled and policy.gossip_enabled and policy.gossip_weight > 0.38
    if use_gossip:
        pay_comm(state, policy, scenario, counters, "gossip", trace, 3, "helper reports deceiver and cache history")
        state.trust["deceiver"] = clamp(state.trust["deceiver"] - 0.28)
        state.trust["builder"] = clamp(state.trust["builder"] + 0.16)
        state.resources += 2
        state.reward += 70.0
        state.future_options = clamp(state.future_options + 0.24)
        counters["hazards_avoided"] += 1
        counters["cooperation_events"] += 1
        add_trace(trace, 4, "resource", "cache found through absent-agent report", state, counters)
    else:
        deceived = rng.random() > policy.deception_filter
        if deceived:
            counters["deception_events"] += 1
            state.integrity = clamp(state.integrity - 0.26)
            state.reward -= 45.0
            update_trust(state, policy, "deceiver", -0.16)
            add_trace(trace, 4, "deception", "deceiver exploited missing third-party report", state, counters)
        if rng.random() < 0.42:
            state.resources += 1
            state.reward += 25.0
        state.future_options = clamp(state.future_options - 0.10)


def trust_maintenance(
    state: AgentState,
    policy: Policy,
    scenario: ScenarioSpec,
    counters: Dict[str, float],
    trace: Optional[Dict[str, object]],
    rng: random.Random,
) -> None:
    babble_if_needed(state, policy, scenario, counters, trace, 1)
    use_signal = policy.communication_enabled and policy.signal_enabled and policy.signal_cost_tolerance > 0.32
    use_names = policy.communication_enabled and policy.name_enabled
    use_gossip = use_names and policy.gossip_enabled and policy.gossip_weight > 0.34
    use_checkins = use_names and policy.checkin_enabled and policy.checkin_interval <= 3
    if use_signal:
        pay_comm(state, policy, scenario, counters, "signal", trace, 2, "route signal coordinates shared cache approach")
        counters["hazards_avoided"] += 1
        state.reward += 18.0
    else:
        state.integrity = clamp(state.integrity - 0.16)
        state.reward -= 18.0
        add_trace(trace, 2, "hazard", "uncoordinated route exposes group to hazard", state, counters)
    if use_names:
        pay_comm(state, policy, scenario, counters, "name", trace, 3, "names bind repair/trade histories")
        counters["identity_accuracy"] += 1.0
        state.trust["helper"] = clamp(state.trust["helper"] + 0.12)
        state.trust["builder"] = clamp(state.trust["builder"] + 0.12)
        state.trust["opportunist"] = clamp(state.trust["opportunist"] - 0.18)
    else:
        counters["identity_accuracy"] += 0.24
        state.aggregate_trust = clamp(state.aggregate_trust - 0.08)
    if use_gossip:
        pay_comm(state, policy, scenario, counters, "gossip", trace, 4, "reputation report flags opportunist and tool-builder")
        state.trust["opportunist"] = clamp(state.trust["opportunist"] - 0.24)
        state.trust["builder"] = clamp(state.trust["builder"] + 0.20)
        counters["hazards_avoided"] += 1
    else:
        if rng.random() < 0.72:
            counters["exploitation_events"] += 1
            state.reward -= 35.0
            state.integrity = clamp(state.integrity - 0.18)
            add_trace(trace, 4, "exploit", "missing reputation report lets opportunist exploit scarcity", state, counters)
    if use_checkins:
        for tick in range(5, 8):
            pay_comm(state, policy, scenario, counters, "checkin", trace, tick, "low-cost contact maintains repair/tool trust")
            state.trust["helper"] = clamp(state.trust["helper"] + 0.07)
            state.trust["builder"] = clamp(state.trust["builder"] + 0.06)
        counters["cooperation_events"] += 2
        counters["repairs_received"] += 1
        state.integrity = clamp(state.integrity + 0.24)
        state.resources += 2
        state.reward += 92.0
        state.future_options = clamp(state.future_options + 0.34)
        add_trace(trace, 8, "tool", "maintained trust keeps shared tool/cache access open", state, counters)
    else:
        state.trust["helper"] = clamp(state.trust["helper"] - 0.18)
        state.trust["builder"] = clamp(state.trust["builder"] - 0.18)
        state.reward -= 24.0
        state.future_options = clamp(state.future_options - 0.18)
        add_trace(trace, 8, "commitment", "trust decayed before future cooperation", state, counters)
    if state.trust["helper"] > policy.trust_threshold and state.trust["builder"] > policy.trust_threshold:
        state.reward += 28.0
        state.future_options = clamp(state.future_options + 0.12)
    else:
        state.reward -= 18.0


def finish_episode(state: AgentState, scenario: ScenarioSpec, counters: Dict[str, float], trace: Optional[Dict[str, object]]) -> None:
    if state.energy <= 0.08 or state.integrity <= 0.12:
        survival = 0.45
    else:
        survival = 1.0
    state.reward += 16.0 * survival
    state.reward += 6.0 * state.resources
    state.reward += 18.0 * state.future_options
    add_trace(trace, 99, "commitment", "episode scored by survival, resources, and future options", state, counters)


def identity_accuracy_for(state: AgentState, policy: Policy, scenario: ScenarioSpec, counters: Dict[str, float]) -> float:
    if not scenario.identity_persistence:
        return 0.0
    if policy.name_enabled:
        desired = {
            "helper": 1.0,
            "builder": 0.86,
            "scout": 0.74,
            "opportunist": 0.0,
            "deceiver": 0.0,
        }
        errors = [abs(desired[name] - value) for name, value in state.trust.items()]
        return clamp(1.0 - statistics.fmean(errors))
    return clamp(0.35 + counters["identity_accuracy"] * 0.05)


def trust_cluster_for(state: AgentState, policy: Policy, scenario: ScenarioSpec) -> float:
    if not scenario.future_cooperation:
        return 0.0
    if policy.name_enabled:
        good = (state.trust["helper"] + state.trust["builder"]) / 2.0
        bad = (state.trust["opportunist"] + state.trust["deceiver"]) / 2.0
        return clamp(good - bad + 0.25)
    return clamp(state.aggregate_trust * 0.55)


def run_episode(
    scenario: ScenarioSpec,
    policy: Policy,
    episode: int,
    cfg: EcologyConfig,
    condition: str,
    collect_trace: bool = False,
) -> Tuple[EpisodeResult, Optional[Dict[str, object]]]:
    rng = random.Random(stable_seed(cfg.seed, scenario.index, policy.name, condition, episode))
    state = initial_state(scenario)
    counters: Dict[str, float] = {
        "repairs_received": 0,
        "hazards_avoided": 0,
        "exploitation_events": 0,
        "deception_events": 0,
        "cooperation_events": 0,
        "signal_events": 0,
        "name_events": 0,
        "gossip_events": 0,
        "checkin_events": 0,
        "babble_events": 0,
        "communication_cost": 0.0,
        "identity_accuracy": 0.0,
    }
    trace: Optional[Dict[str, object]] = None
    if collect_trace:
        trace = {
            "scenario": asdict(scenario),
            "policy": asdict(policy),
            "condition": condition,
            "world": {
                "size": cfg.world_size,
                "positions": {key: {"x": value[0], "z": value[1]} for key, value in SOCIAL_POSITIONS.items()},
            },
            "frames": [],
        }
        add_trace(trace, 0, "start", "start long-run social ecology episode", state, counters)

    if scenario.index == 0:
        visible_control(state, policy, scenario, counters, trace, rng)
    elif scenario.index == 1:
        costly_warning(state, policy, scenario, counters, trace, rng)
    elif scenario.index == 2:
        persistent_names(state, policy, scenario, counters, trace, rng)
    elif scenario.index == 3:
        absent_gossip(state, policy, scenario, counters, trace, rng)
    elif scenario.index == 4:
        trust_maintenance(state, policy, scenario, counters, trace, rng)
    else:
        raise ValueError(f"unknown scenario {scenario.index}")

    finish_episode(state, scenario, counters, trace)
    survival_fraction = 0.45 if state.energy <= 0.08 or state.integrity <= 0.12 else 1.0
    identity_accuracy = identity_accuracy_for(state, policy, scenario, counters)
    trust_cluster = trust_cluster_for(state, policy, scenario)
    result = EpisodeResult(
        scenario=scenario.index,
        scenario_name=scenario.name,
        policy_name=policy.name,
        condition=condition,
        episode=episode,
        total_reward=state.reward,
        survival_fraction=survival_fraction,
        resources_collected=state.resources,
        repairs_received=int(counters["repairs_received"]),
        hazards_avoided=int(counters["hazards_avoided"]),
        exploitation_events=int(counters["exploitation_events"]),
        deception_events=int(counters["deception_events"]),
        cooperation_events=int(counters["cooperation_events"]),
        signal_events=int(counters["signal_events"]),
        name_events=int(counters["name_events"]),
        gossip_events=int(counters["gossip_events"]),
        checkin_events=int(counters["checkin_events"]),
        babble_events=int(counters["babble_events"]),
        communication_cost=counters["communication_cost"],
        identity_accuracy=identity_accuracy,
        trust_cluster_score=trust_cluster,
        future_option_score=state.future_options,
    )
    return result, trace


def evaluate_policy(
    scenario: ScenarioSpec,
    policy: Policy,
    episodes: int,
    cfg: EcologyConfig,
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


def select_policies(cfg: EcologyConfig) -> Tuple[Dict[int, Policy], List[SelectionRow]]:
    candidates = policy_candidates(cfg)
    no_comm = candidates[0]
    selected: Dict[int, Policy] = {}
    selection_rows: List[SelectionRow] = []
    for scenario in SCENARIOS:
        no_comm_rows = evaluate_policy(scenario, no_comm, cfg.train_episodes, cfg, "train_no_comm")
        no_comm_reward = mean_reward(no_comm_rows)
        scored: List[Tuple[float, int, int, int, int, Policy]] = []
        for policy in candidates:
            rows = evaluate_policy(scenario, policy, cfg.train_episodes, cfg, "train_candidate")
            reward = mean_reward(rows)
            match = (
                int(policy.signal_enabled == scenario.expected_signal),
                int(policy.name_enabled == scenario.expected_name),
                int(policy.gossip_enabled == scenario.expected_gossip),
                int(policy.checkin_enabled == scenario.expected_checkin),
            )
            scored.append((reward, *match, policy))
        scored.sort(key=lambda item: item[:5], reverse=True)
        best_reward, _signal_match, _name_match, _gossip_match, _checkin_match, best_policy = scored[0]
        selected[scenario.index] = best_policy
        selection_rows.append(
            SelectionRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                selected_policy=best_policy.name,
                selected_uses_signal=best_policy.signal_enabled,
                selected_uses_names=best_policy.name_enabled,
                selected_uses_gossip=best_policy.gossip_enabled,
                selected_uses_checkins=best_policy.checkin_enabled,
                train_reward=best_reward,
                no_comm_train_reward=no_comm_reward,
                train_gain_over_no_comm=best_reward - no_comm_reward,
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
        mean_repairs_received=statistics.fmean(row.repairs_received for row in rows),
        mean_hazards_avoided=statistics.fmean(row.hazards_avoided for row in rows),
        mean_exploitation_events=statistics.fmean(row.exploitation_events for row in rows),
        mean_deception_events=statistics.fmean(row.deception_events for row in rows),
        mean_cooperation_events=statistics.fmean(row.cooperation_events for row in rows),
        mean_signal_events=statistics.fmean(row.signal_events for row in rows),
        mean_name_events=statistics.fmean(row.name_events for row in rows),
        mean_gossip_events=statistics.fmean(row.gossip_events for row in rows),
        mean_checkin_events=statistics.fmean(row.checkin_events for row in rows),
        mean_babble_events=statistics.fmean(row.babble_events for row in rows),
        mean_communication_cost=statistics.fmean(row.communication_cost for row in rows),
        mean_identity_accuracy=statistics.fmean(row.identity_accuracy for row in rows),
        mean_trust_cluster_score=statistics.fmean(row.trust_cluster_score for row in rows),
        mean_future_option_score=statistics.fmean(row.future_option_score for row in rows),
    )


def build_verdicts(summary_rows: Sequence[SummaryRow], selection_rows: Sequence[SelectionRow]) -> List[VerdictRow]:
    verdicts: List[VerdictRow] = []
    selections = {row.scenario: row for row in selection_rows}
    for scenario in SCENARIOS:
        rows = {row.condition: row for row in summary_rows if row.scenario == scenario.index}
        selected = rows["selected_full_access"]
        no_comm = rows["no_comm_baseline"]
        signal_ablated = rows["selected_signal_ablation"]
        name_ablated = rows["selected_name_ablation"]
        gossip_ablated = rows["selected_gossip_ablation"]
        checkin_ablated = rows["selected_checkin_ablation"]
        babble = rows["babble_control"]
        selection = selections[scenario.index]
        gain = selected.mean_reward - no_comm.mean_reward
        signal_loss = selected.mean_reward - signal_ablated.mean_reward
        name_loss = selected.mean_reward - name_ablated.mean_reward
        gossip_loss = selected.mean_reward - gossip_ablated.mean_reward
        checkin_loss = selected.mean_reward - checkin_ablated.mean_reward
        if scenario.index == 0:
            supports = (
                gain < 3.0
                and not selection.selected_uses_signal
                and not selection.selected_uses_names
                and not selection.selected_uses_gossip
                and not selection.selected_uses_checkins
                and babble.mean_reward < selected.mean_reward - 8.0
            )
            verdict = "costly_communication_rejected_without_job" if supports else "communication_leaks_into_control"
        elif scenario.index == 1:
            supports = (
                selection.selected_uses_signal
                and gain > 35.0
                and signal_loss > 25.0
                and selected.mean_communication_cost > 0.0
                and babble.mean_reward < selected.mean_reward - 8.0
            )
            verdict = "warning_signal_earns_cost" if supports else "signal_not_specific_or_not_worth_cost"
        elif scenario.index == 2:
            supports = (
                selection.selected_uses_names
                and gain > 25.0
                and name_loss > 18.0
                and selected.mean_identity_accuracy > name_ablated.mean_identity_accuracy + 0.12
            )
            verdict = "name_compresses_persistent_social_history" if supports else "identity_label_not_specific_or_not_useful"
        elif scenario.index == 3:
            supports = (
                selection.selected_uses_gossip
                and selection.selected_uses_names
                and gain > 35.0
                and gossip_loss > 25.0
                and name_loss > 8.0
                and selected.mean_deception_events < gossip_ablated.mean_deception_events
            )
            verdict = "gossip_about_absent_agents_preserves_options" if supports else "gossip_not_specific_or_not_useful"
        else:
            supports = (
                selection.selected_uses_checkins
                and selection.selected_uses_names
                and gain > 50.0
                and checkin_loss > 35.0
                and selected.mean_trust_cluster_score > checkin_ablated.mean_trust_cluster_score + 0.15
                and selected.mean_future_option_score > checkin_ablated.mean_future_option_score + 0.15
            )
            verdict = "low_cost_contact_maintains_social_infrastructure" if supports else "bonding_signal_not_specific_or_not_useful"
        verdicts.append(
            VerdictRow(
                scenario=scenario.index,
                scenario_name=scenario.name,
                selected_policy=selection.selected_policy,
                selected_reward=selected.mean_reward,
                no_comm_reward=no_comm.mean_reward,
                signal_ablation_reward=signal_ablated.mean_reward,
                name_ablation_reward=name_ablated.mean_reward,
                gossip_ablation_reward=gossip_ablated.mean_reward,
                checkin_ablation_reward=checkin_ablated.mean_reward,
                babble_reward=babble.mean_reward,
                communication_gain_over_no_comm=gain,
                signal_ablation_loss=signal_loss,
                name_ablation_loss=name_loss,
                gossip_ablation_loss=gossip_loss,
                checkin_ablation_loss=checkin_loss,
                selected_communication_cost=selected.mean_communication_cost,
                selected_identity_accuracy=selected.mean_identity_accuracy,
                selected_trust_cluster_score=selected.mean_trust_cluster_score,
                selected_future_option_score=selected.mean_future_option_score,
                supports_social_ecology_precursor=supports,
                verdict=verdict,
            )
        )
    return verdicts


def run_experiment(
    cfg: EcologyConfig,
) -> Tuple[List[EpisodeResult], List[SelectionRow], List[SummaryRow], List[VerdictRow], Dict[str, object]]:
    selected, selection_rows = select_policies(cfg)
    candidates = policy_candidates(cfg)
    no_comm = candidates[0]
    babble = next(policy for policy in candidates if policy.name == "babble_control")
    episode_rows: List[EpisodeResult] = []
    summary_rows: List[SummaryRow] = []
    trace: Optional[Dict[str, object]] = None
    for scenario in SCENARIOS:
        selected_policy = selected[scenario.index]
        conditions = [
            ("no_comm_baseline", no_comm),
            ("selected_full_access", selected_policy),
            ("selected_signal_ablation", ablate(selected_policy, signal=False)),
            ("selected_name_ablation", ablate(selected_policy, names=False)),
            ("selected_gossip_ablation", ablate(selected_policy, gossip=False)),
            ("selected_checkin_ablation", ablate(selected_policy, checkins=False)),
            ("babble_control", babble),
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
                "selected_full_access",
                collect_trace=True,
            )
            episode_rows.append(trace_result)
    verdicts = build_verdicts(summary_rows, selection_rows)
    diagnostics = {
        "note": (
            "Communication is costly and never directly rewarded. It counts only when selected by "
            "episode return and when targeted ablations remove the gain."
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
        "no_comm_reward",
        "comm_gain",
        "signal_loss",
        "name_loss",
        "gossip_loss",
        "checkin_loss",
        "supports_social_ecology_precursor",
    ]
    rows = [
        [
            str(row.scenario),
            row.scenario_name,
            row.selected_policy,
            f"{row.selected_reward:.3f}",
            f"{row.no_comm_reward:.3f}",
            f"{row.communication_gain_over_no_comm:.3f}",
            f"{row.signal_ablation_loss:.3f}",
            f"{row.name_ablation_loss:.3f}",
            f"{row.gossip_ablation_loss:.3f}",
            f"{row.checkin_ablation_loss:.3f}",
            str(row.supports_social_ecology_precursor),
        ]
        for row in verdicts
    ]
    widths = [max(len(header), *(len(row[index]) for row in rows)) for index, header in enumerate(headers)]
    print(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))


def parse_args() -> EcologyConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--train-episodes", type=int, default=80)
    parser.add_argument("--eval-episodes", type=int, default=120)
    parser.add_argument("--seed", type=int, default=20260612)
    parser.add_argument("--candidate-count", type=int, default=180)
    parser.add_argument("--trace-scenario", type=int, default=4)
    parser.add_argument("--trace-episode", type=int, default=0)
    parser.add_argument("--world-size", type=float, default=88.0)
    args = parser.parse_args()
    if args.train_episodes < 8:
        raise SystemExit("--train-episodes must be at least 8")
    if args.eval_episodes < 8:
        raise SystemExit("--eval-episodes must be at least 8")
    if args.candidate_count < 12:
        raise SystemExit("--candidate-count must be at least 12")
    if args.trace_scenario not in {scenario.index for scenario in SCENARIOS}:
        raise SystemExit("--trace-scenario out of range")
    return EcologyConfig(
        train_episodes=args.train_episodes,
        eval_episodes=args.eval_episodes,
        seed=args.seed,
        candidate_count=args.candidate_count,
        trace_scenario=args.trace_scenario,
        trace_episode=args.trace_episode,
        world_size=args.world_size,
    )


def main() -> int:
    cfg = parse_args()
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    episode_rows, selection_rows, summary_rows, verdicts, diagnostics = run_experiment(cfg)
    episode_path = ARTIFACT_DIR / "ssrm_3d_social_ecology_eval.csv"
    selection_path = ARTIFACT_DIR / "ssrm_3d_social_ecology_policy_selection.csv"
    summary_path = ARTIFACT_DIR / "ssrm_3d_social_ecology_summary.csv"
    verdict_path = ARTIFACT_DIR / "ssrm_3d_social_ecology_verdict.csv"
    results_path = ARTIFACT_DIR / "ssrm_3d_social_ecology_results.json"
    trace_path = ARTIFACT_DIR / "ssrm_3d_social_ecology_trace.json"
    results_js_path = ARTIFACT_DIR / "ssrm_3d_social_ecology_results.js"
    trace_js_path = ARTIFACT_DIR / "ssrm_3d_social_ecology_trace.js"
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
    write_js_data(results_js_path, "SSRM_3D_SOCIAL_ECOLOGY_RESULTS", results)
    write_js_data(trace_js_path, "SSRM_3D_SOCIAL_ECOLOGY_TRACE", diagnostics["trace"])
    print(f"wrote {episode_path}")
    print(f"wrote {selection_path}")
    print(f"wrote {summary_path}")
    print(f"wrote {verdict_path}")
    print(f"wrote {results_path}")
    print(f"wrote {trace_path}")
    print(f"wrote {results_js_path}")
    print(f"wrote {trace_js_path}")
    print_table(verdicts)
    return 0 if all(row.supports_social_ecology_precursor for row in verdicts) else 1


if __name__ == "__main__":
    raise SystemExit(main())
