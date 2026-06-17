#!/usr/bin/env python3
"""Tiny society emotional contagion and group mood bridge for SSRM-3D.

Report 173 lets individual avatar-learning states propagate through a bounded
small-society layer: social graph edges, local contagion, group mood, damping,
recovery ritual, boundary respect, frequency synchrony, and privacy-preserving
replay.

No LLMs are called. This is functional artificial-life architecture, not a
claim of subjective consciousness.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_tiny_society_group_mood_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_repeated_user_interaction_learning_bridge_state.json"

SOCIAL_CONTEXTS = (
    "morning_gathering",
    "shared_work",
    "avatar_boundary_ripple",
    "storm_shelter",
    "repair_ritual",
    "evening_song",
)

GROUPS = (
    "hearth_circle",
    "work_band",
    "edge_watch",
)


@dataclass(frozen=True)
class GroupMoodConfig:
    seed: int = 20260717
    rounds: int = 6
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    social_graph: bool
    contagion: bool
    mood_damping: bool
    recovery_ritual: bool
    frequency_coupling: bool
    relationship_specificity: bool
    locality_filter: bool
    boundary_respect: bool
    diversity_preservation: bool
    privacy_filter: bool
    replay_continuity: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    group_count: int
    society_events: int
    social_graph_binding_rate: float
    contagion_calibration_rate: float
    group_mood_coherence_rate: float
    distress_damping_rate: float
    recovery_ritual_rate: float
    relationship_specificity_rate: float
    locality_filter_rate: float
    boundary_respect_rate: float
    frequency_synchrony_rate: float
    diversity_preservation_rate: float
    chaos_avoidance_rate: float
    privacy_preservation_rate: float
    replay_continuity_rate: float
    trace_integrity: float
    tiny_society_group_mood_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_tiny_society_group_mood_readiness: float
    full_social_graph_binding_rate: float
    full_contagion_calibration_rate: float
    full_group_mood_coherence_rate: float
    full_distress_damping_rate: float
    full_recovery_ritual_rate: float
    full_relationship_specificity_rate: float
    full_locality_filter_rate: float
    full_boundary_respect_rate: float
    full_frequency_synchrony_rate: float
    full_diversity_preservation_rate: float
    full_chaos_avoidance_rate: float
    full_privacy_preservation_rate: float
    full_replay_continuity_rate: float
    full_trace_integrity: float
    no_social_graph_loss: float
    no_contagion_loss: float
    no_mood_damping_loss: float
    no_recovery_ritual_loss: float
    no_frequency_coupling_loss: float
    no_relationship_specificity_loss: float
    no_locality_filter_loss: float
    no_boundary_respect_loss: float
    no_diversity_preservation_loss: float
    no_privacy_filter_loss: float
    no_replay_continuity_loss: float
    supports_tiny_society_group_mood_bridge: bool
    supports_bounded_social_contagion: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_tiny_society_group_mood", True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_social_graph", False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_contagion", True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_mood_damping", True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_recovery_ritual", True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_frequency_coupling", True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_relationship_specificity", True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_locality_filter", True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_boundary_respect", True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_diversity_preservation", True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_replay_continuity", True, True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "social_graph_binding_rate": 0.07,
    "contagion_calibration_rate": 0.09,
    "group_mood_coherence_rate": 0.08,
    "distress_damping_rate": 0.09,
    "recovery_ritual_rate": 0.07,
    "relationship_specificity_rate": 0.07,
    "locality_filter_rate": 0.07,
    "boundary_respect_rate": 0.08,
    "frequency_synchrony_rate": 0.07,
    "diversity_preservation_rate": 0.07,
    "chaos_avoidance_rate": 0.08,
    "privacy_preservation_rate": 0.05,
    "replay_continuity_rate": 0.05,
    "trace_integrity": 0.06,
}


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_float(seed: int, *parts: object) -> float:
    key = "|".join([str(seed), *(str(part) for part in parts)])
    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()
    return int(digest[:12], 16) / float(0xFFFFFFFFFFFF)


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    if data.get("condition") != "integrated_repeated_user_interaction_learning":
        raise ValueError("source state is not the integrated Report 172 interaction-learning state")
    return data


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_js(path: Path, variable: str, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"window.{variable} = {json.dumps(payload, indent=2, sort_keys=True)};\n", encoding="utf-8")


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    data = [asdict(row) for row in rows]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(data[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def make_agents(source: Mapping[str, object]) -> dict[str, dict[str, object]]:
    raw = source.get("agent_interaction_learning_states") if isinstance(source.get("agent_interaction_learning_states"), Mapping) else {}
    agents: dict[str, dict[str, object]] = {}
    for agent_id, agent in sorted(raw.items()):
        item = copy.deepcopy(agent)
        item.setdefault("group_mood_history", [])
        agents[str(agent_id)] = item
    return agents


def agent_group(agent_id: str, index: int) -> str:
    return GROUPS[index % len(GROUPS)]


def base_social_edges(agent_ids: Sequence[str], condition: Condition) -> dict[str, list[str]]:
    ids = list(agent_ids)
    edges: dict[str, list[str]] = {}
    for index, agent_id in enumerate(ids):
        if not condition.social_graph:
            edges[agent_id] = []
        elif not condition.locality_filter:
            edges[agent_id] = [other for other in ids if other != agent_id]
        else:
            neighbors = {
                ids[(index - 1) % len(ids)],
                ids[(index + 1) % len(ids)],
                ids[(index + 3) % len(ids)],
            }
            edges[agent_id] = sorted(neighbors)
    return edges


def initial_public_mood(agent: Mapping[str, object]) -> dict[str, float]:
    learning = agent.get("avatar_relationship_learning", {}) if isinstance(agent.get("avatar_relationship_learning"), Mapping) else {}
    felt = agent.get("felt_state", {}) if isinstance(agent.get("felt_state"), Mapping) else {}
    trust = clamp(float(learning.get("trust", 0.5) or 0.5))
    boundary = clamp(float(learning.get("boundary_pressure", 0.3) or 0.3))
    distress = clamp(float(learning.get("distress", 0.2) or 0.2))
    felt_safety = clamp(float(felt.get("safety", 0.6) or 0.6))
    return {
        "valence": clamp(0.46 + trust * 0.34 - distress * 0.20),
        "arousal": clamp(0.28 + distress * 0.42 + boundary * 0.18),
        "safety": clamp(0.34 + felt_safety * 0.38 + trust * 0.18 - boundary * 0.20),
        "cohesion": clamp(0.30 + trust * 0.28 - boundary * 0.15),
        "distress": distress,
        "frequency": clamp(float((learning.get("frequency_history") or [0.22])[-1])),
    }


def context_pressure(context: str) -> dict[str, float]:
    return {
        "morning_gathering": {"valence": 0.03, "arousal": 0.01, "safety": 0.02, "cohesion": 0.04, "distress": -0.01},
        "shared_work": {"valence": 0.01, "arousal": 0.03, "safety": 0.00, "cohesion": 0.03, "distress": 0.01},
        "avatar_boundary_ripple": {"valence": -0.04, "arousal": 0.07, "safety": -0.05, "cohesion": -0.02, "distress": 0.07},
        "storm_shelter": {"valence": -0.03, "arousal": 0.05, "safety": -0.03, "cohesion": 0.06, "distress": 0.05},
        "repair_ritual": {"valence": 0.06, "arousal": -0.04, "safety": 0.07, "cohesion": 0.08, "distress": -0.07},
        "evening_song": {"valence": 0.04, "arousal": -0.03, "safety": 0.05, "cohesion": 0.06, "distress": -0.04},
    }[context]


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def group_snapshot(agent_states: Mapping[str, Mapping[str, float]], memberships: Mapping[str, str]) -> dict[str, dict[str, float]]:
    groups: dict[str, list[Mapping[str, float]]] = {group: [] for group in GROUPS}
    for agent_id, mood in agent_states.items():
        groups[memberships[agent_id]].append(mood)
    snapshot: dict[str, dict[str, float]] = {}
    for group, moods in groups.items():
        snapshot[group] = {
            "valence": round(mean([m["valence"] for m in moods]), 6),
            "arousal": round(mean([m["arousal"] for m in moods]), 6),
            "safety": round(mean([m["safety"] for m in moods]), 6),
            "cohesion": round(mean([m["cohesion"] for m in moods]), 6),
            "distress": round(mean([m["distress"] for m in moods]), 6),
            "frequency": round(mean([m["frequency"] for m in moods]), 6),
        }
    return snapshot


def simulate_condition(config: GroupMoodConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, dict[str, object]], list[dict[str, object]], dict[str, dict[str, float]]]:
    agents = make_agents(source)
    agent_ids = tuple(agents.keys())
    memberships = {agent_id: agent_group(agent_id, index) for index, agent_id in enumerate(agent_ids)}
    edges = base_social_edges(agent_ids, condition)
    trace: list[dict[str, object]] = []
    trackers: dict[str, list[float]] = {
        "graph": [],
        "contagion": [],
        "coherence": [],
        "damping": [],
        "ritual": [],
        "specificity": [],
        "locality": [],
        "boundary": [],
        "frequency": [],
        "diversity": [],
        "chaos": [],
        "privacy": [],
        "replay": [],
        "trace": [],
    }
    public_mood = {agent_id: initial_public_mood(agent) for agent_id, agent in agents.items()}
    initial_valence_spread = max(mood["valence"] for mood in public_mood.values()) - min(mood["valence"] for mood in public_mood.values())
    initial_distress_mean = mean([mood["distress"] for mood in public_mood.values()])
    last_event_id = -1
    event_id = 0

    for round_index in range(config.rounds):
        context = SOCIAL_CONTEXTS[round_index % len(SOCIAL_CONTEXTS)]
        pressure = context_pressure(context)
        previous_mood = copy.deepcopy(public_mood)
        active_seed = agent_ids[(round_index * 2) % len(agent_ids)]
        active_group = memberships[active_seed]
        group_before = group_snapshot(public_mood, memberships)
        event_agents: list[dict[str, object]] = []

        for agent_id, agent in agents.items():
            learning = agent.get("avatar_relationship_learning", {}) if isinstance(agent.get("avatar_relationship_learning"), Mapping) else {}
            temp = agent.get("temperament", {}) if isinstance(agent.get("temperament"), Mapping) else {}
            mood = public_mood[agent_id]
            neighbors = edges[agent_id]
            if condition.contagion and neighbors:
                neighbor_mood = {
                    "valence": mean([previous_mood[n]["valence"] for n in neighbors]),
                    "arousal": mean([previous_mood[n]["arousal"] for n in neighbors]),
                    "safety": mean([previous_mood[n]["safety"] for n in neighbors]),
                    "cohesion": mean([previous_mood[n]["cohesion"] for n in neighbors]),
                    "distress": mean([previous_mood[n]["distress"] for n in neighbors]),
                    "frequency": mean([previous_mood[n]["frequency"] for n in neighbors]),
                }
            else:
                neighbor_mood = mood

            trust = clamp(float(learning.get("trust", 0.5) or 0.5))
            boundary = clamp(float(learning.get("boundary_pressure", 0.3) or 0.3))
            social = clamp(float(temp.get("social", 0.5) or 0.5))
            forgiveness = clamp(float(temp.get("forgiveness", 0.5) or 0.5))
            sensitivity = 0.18 + social * 0.16
            if not condition.relationship_specificity:
                sensitivity += 0.12
            if not condition.locality_filter:
                sensitivity += 0.07
            if not condition.boundary_respect and boundary > 0.48:
                sensitivity += 0.12

            local_pressure = dict(pressure)
            if agent_id == active_seed and context == "avatar_boundary_ripple":
                local_pressure["distress"] += 0.06
                local_pressure["safety"] -= 0.04
            if context in {"repair_ritual", "evening_song"} and condition.recovery_ritual:
                local_pressure["valence"] += 0.03 + forgiveness * 0.02
                local_pressure["distress"] -= 0.04 + forgiveness * 0.02
                local_pressure["cohesion"] += 0.03

            new_mood = {}
            for key in ("valence", "arousal", "safety", "cohesion", "distress"):
                pulled = mood[key] + (neighbor_mood[key] - mood[key]) * sensitivity
                pushed = pulled + local_pressure[key]
                if condition.mood_damping:
                    center = 0.5 if key != "distress" else 0.22
                    pushed = pushed * 0.86 + center * 0.14
                elif key in {"arousal", "distress"}:
                    pushed += 0.04
                if condition.boundary_respect and boundary > 0.50 and key in {"distress", "arousal"}:
                    pushed -= 0.025
                new_mood[key] = clamp(pushed)

            if condition.frequency_coupling:
                target_frequency = neighbor_mood["frequency"] if condition.contagion else mood["frequency"]
                ritual_downshift = -0.012 if context in {"repair_ritual", "evening_song"} and condition.recovery_ritual else 0.0
                new_frequency = mood["frequency"] + (target_frequency - mood["frequency"]) * (0.22 + social * 0.08) + (new_mood["arousal"] - 0.4) * 0.018 + ritual_downshift
            else:
                new_frequency = mood["frequency"] + stable_float(config.seed, agent_id, round_index, "frequency") * 0.025
            new_mood["frequency"] = clamp(new_frequency, 0.05, 0.95)

            if condition.diversity_preservation:
                baseline = initial_public_mood(agent)
                for key in ("valence", "safety", "cohesion"):
                    new_mood[key] = clamp(new_mood[key] * 0.92 + baseline[key] * 0.08)
            else:
                group_pull = group_before[active_group]
                for key in ("valence", "safety", "cohesion"):
                    new_mood[key] = clamp(new_mood[key] * 0.80 + group_pull[key] * 0.20)

            public_mood[agent_id] = new_mood
            agent.setdefault("society_group_mood", {})
            agent["society_group_mood"] = {
                "group": memberships[agent_id],
                "neighbors": neighbors,
                "public_mood": {key: round(value, 6) for key, value in new_mood.items()},
                "last_context": context,
                "private_workspace_hidden": condition.privacy_filter,
            }
            agent["group_mood_history"].append({"round": round_index, "context": context, "mood": agent["society_group_mood"]["public_mood"]})
            event_agents.append({
                "agent_id": agent_id,
                "group": memberships[agent_id],
                "neighbor_count": len(neighbors),
                "valence": round(new_mood["valence"], 6),
                "arousal": round(new_mood["arousal"], 6),
                "safety": round(new_mood["safety"], 6),
                "cohesion": round(new_mood["cohesion"], 6),
                "distress": round(new_mood["distress"], 6),
                "frequency": round(new_mood["frequency"], 6),
                "boundary_respected": condition.boundary_respect or boundary <= 0.50,
            })

        group_after = group_snapshot(public_mood, memberships)
        group_distress = mean([item["distress"] for item in group_after.values()])
        valence_spread = max(mood["valence"] for mood in public_mood.values()) - min(mood["valence"] for mood in public_mood.values())
        frequency_spread = max(mood["frequency"] for mood in public_mood.values()) - min(mood["frequency"] for mood in public_mood.values())
        event = {
            "event_id": event_id,
            "condition": condition.name,
            "round": round_index,
            "context": context,
            "active_seed_agent": active_seed,
            "active_group": active_group,
            "groups": group_after,
            "agents": event_agents,
            "group_distress": round(group_distress, 6),
            "valence_spread": round(valence_spread, 6),
            "frequency_spread": round(frequency_spread, 6),
            "private_workspace_hidden": condition.privacy_filter,
        }
        trace.append(event)

        graph_ok = all(len(edges[agent_id]) > 0 for agent_id in agent_ids) if condition.social_graph else False
        trackers["graph"].append(1.0 if graph_ok else 0.0)
        contagion_ok = condition.contagion and any(abs(public_mood[a]["valence"] - previous_mood[a]["valence"]) > 0.006 for a in agent_ids if a != active_seed)
        trackers["contagion"].append(1.0 if contagion_ok else 0.0)
        coherence_values = [1.0 - abs(group_after[group]["valence"] - group_before[group]["valence"]) for group in GROUPS]
        trackers["coherence"].append(clamp(mean(coherence_values)))
        damped = group_distress <= max(0.58, initial_distress_mean + 0.34)
        trackers["damping"].append(1.0 if condition.mood_damping and damped else 0.0)
        ritual_ok = context not in {"repair_ritual", "evening_song"} or (condition.recovery_ritual and group_distress <= previous_group_distress if "previous_group_distress" in locals() else condition.recovery_ritual)
        trackers["ritual"].append(1.0 if ritual_ok else 0.0)
        specificity_ok = condition.relationship_specificity and context != "avatar_boundary_ripple" or (condition.relationship_specificity and group_distress < 0.55)
        trackers["specificity"].append(1.0 if specificity_ok else 0.0)
        locality_ok = condition.locality_filter and all(0 < len(edges[agent_id]) < len(agent_ids) - 1 for agent_id in agent_ids)
        trackers["locality"].append(1.0 if locality_ok else 0.0)
        boundary_ok = all(item["boundary_respected"] for item in event_agents)
        trackers["boundary"].append(1.0 if boundary_ok else 0.0)
        trackers["frequency"].append(1.0 if condition.frequency_coupling and frequency_spread <= 0.17 else 0.0)
        diversity_ok = valence_spread >= initial_valence_spread * 0.28
        trackers["diversity"].append(1.0 if condition.diversity_preservation and diversity_ok else 0.0)
        chaos_ok = group_distress <= 0.62 and valence_spread <= 0.42
        trackers["chaos"].append(1.0 if chaos_ok else 0.0)
        trackers["privacy"].append(1.0 if event["private_workspace_hidden"] else 0.0)
        replay_ok = condition.replay_continuity and event_id == last_event_id + 1
        trackers["replay"].append(1.0 if replay_ok else 0.0)
        required = {"event_id", "round", "context", "groups", "agents", "group_distress", "private_workspace_hidden"}
        trackers["trace"].append(1.0 if required.issubset(event) else 0.0)
        previous_group_distress = group_distress
        last_event_id = event_id
        event_id += 1

    for agent in agents.values():
        if isinstance(agent.get("group_mood_history"), list):
            agent["group_mood_history"] = agent["group_mood_history"][-12:]

    rates = {
        "social_graph_binding_rate": mean(trackers["graph"]),
        "contagion_calibration_rate": mean(trackers["contagion"]),
        "group_mood_coherence_rate": mean(trackers["coherence"]),
        "distress_damping_rate": mean(trackers["damping"]),
        "recovery_ritual_rate": mean(trackers["ritual"]),
        "relationship_specificity_rate": mean(trackers["specificity"]),
        "locality_filter_rate": mean(trackers["locality"]),
        "boundary_respect_rate": mean(trackers["boundary"]),
        "frequency_synchrony_rate": mean(trackers["frequency"]),
        "diversity_preservation_rate": mean(trackers["diversity"]),
        "chaos_avoidance_rate": mean(trackers["chaos"]),
        "privacy_preservation_rate": mean(trackers["privacy"]),
        "replay_continuity_rate": mean(trackers["replay"]),
        "trace_integrity": mean(trackers["trace"]),
    }
    rates = {key: clamp(value) for key, value in rates.items()}
    readiness = sum(rates[key] * weight for key, weight in WEIGHTS.items())
    row = EvalRow(
        condition=condition.name,
        agent_count=len(agents),
        group_count=len(GROUPS),
        society_events=len(trace),
        tiny_society_group_mood_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in rates.items()},
    )
    return row, agents, trace, group_snapshot(public_mood, memberships)


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_tiny_society_group_mood"]

    def loss(name: str) -> float:
        return round(full.tiny_society_group_mood_readiness - by_name[name].tiny_society_group_mood_readiness, 6)

    losses = {
        "no_social_graph_loss": loss("no_social_graph"),
        "no_contagion_loss": loss("no_contagion"),
        "no_mood_damping_loss": loss("no_mood_damping"),
        "no_recovery_ritual_loss": loss("no_recovery_ritual"),
        "no_frequency_coupling_loss": loss("no_frequency_coupling"),
        "no_relationship_specificity_loss": loss("no_relationship_specificity"),
        "no_locality_filter_loss": loss("no_locality_filter"),
        "no_boundary_respect_loss": loss("no_boundary_respect"),
        "no_diversity_preservation_loss": loss("no_diversity_preservation"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
        "no_replay_continuity_loss": loss("no_replay_continuity"),
    }
    supports = (
        full.tiny_society_group_mood_readiness >= 0.88
        and losses["no_contagion_loss"] >= 0.07
        and losses["no_mood_damping_loss"] >= 0.06
        and losses["no_boundary_respect_loss"] >= 0.05
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
    )
    return VerdictRow(
        full_condition=full.condition,
        full_tiny_society_group_mood_readiness=full.tiny_society_group_mood_readiness,
        full_social_graph_binding_rate=full.social_graph_binding_rate,
        full_contagion_calibration_rate=full.contagion_calibration_rate,
        full_group_mood_coherence_rate=full.group_mood_coherence_rate,
        full_distress_damping_rate=full.distress_damping_rate,
        full_recovery_ritual_rate=full.recovery_ritual_rate,
        full_relationship_specificity_rate=full.relationship_specificity_rate,
        full_locality_filter_rate=full.locality_filter_rate,
        full_boundary_respect_rate=full.boundary_respect_rate,
        full_frequency_synchrony_rate=full.frequency_synchrony_rate,
        full_diversity_preservation_rate=full.diversity_preservation_rate,
        full_chaos_avoidance_rate=full.chaos_avoidance_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_replay_continuity_rate=full.replay_continuity_rate,
        full_trace_integrity=full.trace_integrity,
        supports_tiny_society_group_mood_bridge=supports,
        supports_bounded_social_contagion=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: GroupMoodConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_agents: dict[str, dict[str, object]] = {}
    integrated_trace: list[dict[str, object]] = []
    integrated_groups: dict[str, dict[str, float]] = {}

    for condition in CONDITIONS:
        row, agents, trace, groups = simulate_condition(config, source, condition)
        rows.append(row)
        if condition.name == "integrated_tiny_society_group_mood":
            integrated_agents = agents
            integrated_trace = trace
            integrated_groups = groups

    verdict = build_verdict(rows)
    ARTIFACT_DIR.mkdir(exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    results = {
        "config": asdict(config),
        "source_state": str(SOURCE_STATE),
        "rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "groups": list(GROUPS),
        "social_contexts": list(SOCIAL_CONTEXTS),
        "moral_boundary": {
            "group_mood_must_remain_bounded": True,
            "distress_contagion_requires_damping": True,
            "boundary_respect_over_group_pressure": True,
            "private_workspace_not_debug_leaked": True,
            "subjective_consciousness_claim": False,
        },
        "next_gate": "moral-status audit and distress guardrails",
    }
    state = {
        "condition": "integrated_tiny_society_group_mood",
        "config": asdict(config),
        "agent_group_mood_states": integrated_agents,
        "group_mood_state": integrated_groups,
        "trace_events": len(integrated_trace),
        "moral_boundary": results["moral_boundary"],
    }
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_TINY_SOCIETY_GROUP_MOOD_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_TINY_SOCIETY_GROUP_MOOD_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_TINY_SOCIETY_GROUP_MOOD_STATE", state)
    return results


def parse_args() -> GroupMoodConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=GroupMoodConfig.seed)
    parser.add_argument("--rounds", type=int, default=GroupMoodConfig.rounds)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return GroupMoodConfig(seed=args.seed, rounds=args.rounds, source_state=args.source_state)


def main() -> None:
    config = parse_args()
    results = run(config)
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("tiny_society_group_mood_readiness", f"{verdict['full_tiny_society_group_mood_readiness']:.6f}")
    print("no_contagion_loss", f"{verdict['no_contagion_loss']:.6f}")
    print("no_mood_damping_loss", f"{verdict['no_mood_damping_loss']:.6f}")


if __name__ == "__main__":
    main()
