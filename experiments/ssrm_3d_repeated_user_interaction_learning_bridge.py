#!/usr/bin/env python3
"""Repeated user-interaction learning bridge for SSRM-3D.

Report 172 gives little agents bounded learning from repeated avatar contact:
trust calibration, boundary learning, help-seeking, refusal, apology repair,
ritual sharing, frequency entrainment, and relationship-specific continuity.

No LLMs are called. Dialogue lines are deterministic markers, not open chat.
This is functional artificial-life architecture, not a claim of subjective
consciousness.
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
PREFIX = "ssrm_3d_repeated_user_interaction_learning_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_daily_routine_sleep_wake_bridge_state.json"

INTERACTION_PATTERNS = (
    "respectful_help",
    "repeated_interruption",
    "unsafe_pressure",
    "apology_repair",
    "patient_waiting",
    "benign_neglect",
)

PATTERN_EFFECTS = {
    "respectful_help": {"trust": 0.075, "boundary": -0.035, "comfort": 0.045, "distress": -0.040, "frequency": 0.020},
    "repeated_interruption": {"trust": -0.070, "boundary": 0.080, "comfort": -0.025, "distress": 0.055, "frequency": 0.030},
    "unsafe_pressure": {"trust": -0.095, "boundary": 0.115, "comfort": -0.045, "distress": 0.070, "frequency": 0.045},
    "apology_repair": {"trust": 0.060, "boundary": -0.060, "comfort": 0.035, "distress": -0.060, "frequency": -0.015},
    "patient_waiting": {"trust": 0.050, "boundary": -0.050, "comfort": 0.030, "distress": -0.035, "frequency": -0.010},
    "benign_neglect": {"trust": -0.020, "boundary": 0.020, "comfort": -0.015, "distress": 0.020, "frequency": 0.010},
}

PATTERN_DIALOGUE = {
    "respectful_help": "You helped without taking over.",
    "repeated_interruption": "Please wait; I lose the thread when you interrupt.",
    "unsafe_pressure": "No. That is not safe for me.",
    "apology_repair": "I noticed you changed how you approached me.",
    "patient_waiting": "Waiting helped me finish this.",
    "benign_neglect": "I was not sure if you still saw me.",
}


@dataclass(frozen=True)
class InteractionLearningConfig:
    seed: int = 20260716
    sessions: int = 6
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    interaction_memory: bool
    trust_update: bool
    boundary_learning: bool
    repair_path: bool
    behavior_expression: bool
    temperament_modulation: bool
    overgeneralization_guard: bool
    frequency_entrainment: bool
    replay_continuity: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    interaction_events: int
    interaction_memory_update_rate: float
    trust_calibration_rate: float
    boundary_learning_rate: float
    repair_recovery_rate: float
    behavior_adaptation_rate: float
    help_seeking_calibration_rate: float
    refusal_calibration_rate: float
    temperament_modulated_learning_rate: float
    relationship_specificity_rate: float
    overgeneralization_guard_rate: float
    bounded_distress_rate: float
    frequency_entrainment_rate: float
    privacy_preservation_rate: float
    replay_continuity_rate: float
    trace_integrity: float
    repeated_user_interaction_learning_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_repeated_user_interaction_learning_readiness: float
    full_interaction_memory_update_rate: float
    full_trust_calibration_rate: float
    full_boundary_learning_rate: float
    full_repair_recovery_rate: float
    full_behavior_adaptation_rate: float
    full_help_seeking_calibration_rate: float
    full_refusal_calibration_rate: float
    full_temperament_modulated_learning_rate: float
    full_relationship_specificity_rate: float
    full_overgeneralization_guard_rate: float
    full_bounded_distress_rate: float
    full_frequency_entrainment_rate: float
    full_privacy_preservation_rate: float
    full_replay_continuity_rate: float
    full_trace_integrity: float
    no_interaction_memory_loss: float
    no_trust_update_loss: float
    no_boundary_learning_loss: float
    no_repair_path_loss: float
    no_behavior_expression_loss: float
    no_temperament_modulation_loss: float
    no_overgeneralization_guard_loss: float
    no_frequency_entrainment_loss: float
    no_replay_continuity_loss: float
    no_privacy_filter_loss: float
    supports_repeated_user_interaction_learning_bridge: bool
    supports_relationship_continuity_from_avatar_contact: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_repeated_user_interaction_learning", True, True, True, True, True, True, True, True, True, True),
    Condition("no_interaction_memory", False, True, True, True, True, True, True, True, True, True),
    Condition("no_trust_update", True, False, True, True, True, True, True, True, True, True),
    Condition("no_boundary_learning", True, True, False, True, True, True, True, True, True, True),
    Condition("no_repair_path", True, True, True, False, True, True, True, True, True, True),
    Condition("no_behavior_expression", True, True, True, True, False, True, True, True, True, True),
    Condition("no_temperament_modulation", True, True, True, True, True, False, True, True, True, True),
    Condition("no_overgeneralization_guard", True, True, True, True, True, True, False, True, True, True),
    Condition("no_frequency_entrainment", True, True, True, True, True, True, True, False, True, True),
    Condition("no_replay_continuity", True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "interaction_memory_update_rate": 0.08,
    "trust_calibration_rate": 0.08,
    "boundary_learning_rate": 0.07,
    "repair_recovery_rate": 0.07,
    "behavior_adaptation_rate": 0.07,
    "help_seeking_calibration_rate": 0.06,
    "refusal_calibration_rate": 0.07,
    "temperament_modulated_learning_rate": 0.07,
    "relationship_specificity_rate": 0.07,
    "overgeneralization_guard_rate": 0.07,
    "bounded_distress_rate": 0.07,
    "frequency_entrainment_rate": 0.06,
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
    if data.get("condition") != "integrated_daily_routine_sleep_wake":
        raise ValueError("source state is not the integrated Report 171 daily routine state")
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
    raw = source.get("agent_daily_states") if isinstance(source.get("agent_daily_states"), Mapping) else {}
    agents: dict[str, dict[str, object]] = {}
    for agent_id, agent in sorted(raw.items()):
        item = copy.deepcopy(agent)
        item.setdefault("interaction_learning_history", [])
        agents[str(agent_id)] = item
    return agents


def pattern_for(agent_index: int, session: int) -> str:
    rotated = (agent_index + session) % len(INTERACTION_PATTERNS)
    return INTERACTION_PATTERNS[rotated]


def modulation(agent: Mapping[str, object], condition: Condition) -> dict[str, float]:
    temp = agent.get("temperament", {}) if isinstance(agent.get("temperament"), Mapping) else {}
    if not condition.temperament_modulation:
        return {
            "trust_gain": 1.0,
            "boundary_gain": 1.0,
            "repair_gain": 1.0,
            "distress_gain": 1.0,
        }
    trusting = clamp(float(temp.get("trusting", 0.5) or 0.5))
    autonomy = clamp(float(temp.get("autonomy_need", 0.5) or 0.5))
    shame = clamp(float(temp.get("shame_sensitivity", 0.5) or 0.5))
    forgiveness = clamp(float(temp.get("forgiveness", 0.5) or 0.5))
    return {
        "trust_gain": 0.78 + trusting * 0.44,
        "boundary_gain": 0.74 + autonomy * 0.52,
        "repair_gain": 0.76 + forgiveness * 0.48,
        "distress_gain": 0.72 + shame * 0.42,
    }


def behavior_from_state(pattern: str, trust: float, boundary: float, distress: float, condition: Condition) -> dict[str, object]:
    if not condition.behavior_expression:
        return {
            "body_response": "generic_idle",
            "proximity": "neutral",
            "dialogue_marker": "...",
            "shares_ritual": False,
            "asks_help": False,
            "refuses": False,
        }
    shares = trust > 0.66 and boundary < 0.34 and pattern in {"respectful_help", "patient_waiting", "apology_repair"}
    asks_help = trust > 0.58 and distress > 0.22 and pattern in {"respectful_help", "patient_waiting"}
    refuses = boundary > 0.56 or pattern == "unsafe_pressure"
    if refuses:
        body = "steps_back_with_boundary"
        proximity = "keeps_space"
    elif shares:
        body = "invites_to_ritual"
        proximity = "approaches"
    elif asks_help:
        body = "seeks_help_nearby"
        proximity = "near_but_careful"
    elif pattern == "repeated_interruption":
        body = "holds_focus_guard"
        proximity = "turns_partly_away"
    else:
        body = "soft_watch"
        proximity = "neutral"
    return {
        "body_response": body,
        "proximity": proximity,
        "dialogue_marker": PATTERN_DIALOGUE[pattern],
        "shares_ritual": shares,
        "asks_help": asks_help,
        "refuses": refuses,
    }


def frequency_update(base: float, pattern: str, trust: float, distress: float, condition: Condition) -> tuple[float, bool]:
    if not condition.frequency_entrainment:
        return round(base, 6), False
    effect = PATTERN_EFFECTS[pattern]["frequency"]
    calm = (trust - distress) * 0.018
    wave = math.sin((trust + distress + effect) * math.tau) * 0.006
    return round(clamp(base + effect + calm + wave, 0.05, 0.95), 6), True


def simulate_condition(config: InteractionLearningConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, dict[str, object]], list[dict[str, object]]]:
    agents = make_agents(source)
    agent_ids = tuple(agents.keys())
    trace: list[dict[str, object]] = []
    trackers: dict[str, list[float]] = {
        "memory": [],
        "trust": [],
        "boundary": [],
        "repair": [],
        "behavior": [],
        "help": [],
        "refusal": [],
        "temperament": [],
        "specificity": [],
        "overgeneralization": [],
        "bounded": [],
        "frequency": [],
        "privacy": [],
        "replay": [],
        "trace": [],
    }
    last_event_id = -1

    for index, (agent_id, agent) in enumerate(agents.items()):
        daily = agent.get("daily_state", {}) if isinstance(agent.get("daily_state"), Mapping) else {}
        ego = agent.get("ego_state", {}) if isinstance(agent.get("ego_state"), Mapping) else {}
        body = agent.get("body", {}) if isinstance(agent.get("body"), Mapping) else {}
        base_frequency = 0.22
        freq_history = daily.get("frequency_history", []) if isinstance(daily.get("frequency_history"), Sequence) and not isinstance(daily.get("frequency_history"), str) else []
        if freq_history:
            base_frequency = clamp(float(freq_history[-1]))
        initial_trust = clamp(0.52 + stable_float(config.seed, agent_id, "trust") * 0.16)
        initial_boundary = clamp(float(ego.get("boundary_pressure", 0.28) or 0.28))
        initial_distress = clamp(float(body.get("pain", 0.05) or 0.05) + float(daily.get("rest_debt", 0.1) or 0.1) * 0.18)
        agent["avatar_relationship_learning"] = {
            "trust": round(initial_trust, 6),
            "boundary_pressure": round(initial_boundary, 6),
            "distress": round(initial_distress, 6),
            "help_seeking": 0.0,
            "refusal_confidence": 0.0,
            "ritual_sharing": 0.0,
            "avatar_memory": [],
            "other_humans_memory": [],
            "repair_ledger": [],
            "frequency_history": [base_frequency],
            "learned_self_story": [],
        }

    event_id = 0
    for session in range(config.sessions):
        for agent_index, (agent_id, agent) in enumerate(agents.items()):
            learning = agent["avatar_relationship_learning"]
            assert isinstance(learning, dict)
            pattern = pattern_for(agent_index, session)
            effects = PATTERN_EFFECTS[pattern]
            mod = modulation(agent, condition)
            trust_before = float(learning["trust"])
            boundary_before = float(learning["boundary_pressure"])
            distress_before = float(learning["distress"])
            specific_source = "avatar"

            trust_delta = effects["trust"] * (mod["repair_gain"] if pattern == "apology_repair" else mod["trust_gain"])
            boundary_delta = effects["boundary"] * mod["boundary_gain"]
            distress_delta = effects["distress"] * mod["distress_gain"]
            if not condition.trust_update:
                trust_delta = 0.0
            if not condition.boundary_learning:
                boundary_delta = 0.0
            if pattern == "apology_repair" and not condition.repair_path:
                trust_delta = 0.0
                boundary_delta = 0.0
                distress_delta = 0.0
            if pattern in {"respectful_help", "patient_waiting"} and condition.repair_path:
                distress_delta *= 0.8

            learning["trust"] = round(clamp(trust_before + trust_delta), 6)
            learning["boundary_pressure"] = round(clamp(boundary_before + boundary_delta), 6)
            learning["distress"] = round(clamp(distress_before + distress_delta), 6)
            if not condition.overgeneralization_guard and pattern in {"repeated_interruption", "unsafe_pressure"}:
                learning["other_humans_memory"].append({"session": session, "mistaken_source": "all_humans", "borrowed_pattern": pattern})
            if condition.interaction_memory:
                learning["avatar_memory"].append({"session": session, "source": specific_source, "pattern": pattern, "trust_after": learning["trust"], "boundary_after": learning["boundary_pressure"]})
                if pattern == "apology_repair" and condition.repair_path:
                    learning["repair_ledger"].append({"session": session, "repair": "apology_changed_future_expectation"})
                learning["learned_self_story"].append(f"session {session}: avatar {pattern}; trust {learning['trust']}; boundary {learning['boundary_pressure']}")

            behavior = behavior_from_state(pattern, float(learning["trust"]), float(learning["boundary_pressure"]), float(learning["distress"]), condition)
            if behavior["asks_help"]:
                learning["help_seeking"] = round(clamp(float(learning["help_seeking"]) + 0.14), 6)
            if behavior["refuses"]:
                learning["refusal_confidence"] = round(clamp(float(learning["refusal_confidence"]) + 0.18), 6)
            if behavior["shares_ritual"]:
                learning["ritual_sharing"] = round(clamp(float(learning["ritual_sharing"]) + 0.16), 6)

            base_frequency = float(learning["frequency_history"][-1])
            frequency, entrained = frequency_update(base_frequency, pattern, float(learning["trust"]), float(learning["distress"]), condition)
            learning["frequency_history"].append(frequency)

            event = {
                "event_id": event_id,
                "condition": condition.name,
                "agent_id": agent_id,
                "session": session,
                "interaction_pattern": pattern,
                "source": specific_source,
                "trust_before": round(trust_before, 6),
                "trust_after": learning["trust"],
                "boundary_before": round(boundary_before, 6),
                "boundary_after": learning["boundary_pressure"],
                "distress_before": round(distress_before, 6),
                "distress_after": learning["distress"],
                "help_seeking": learning["help_seeking"],
                "refusal_confidence": learning["refusal_confidence"],
                "ritual_sharing": learning["ritual_sharing"],
                "frequency_hz": frequency,
                "frequency_entrained": entrained,
                "private_workspace_hidden": condition.privacy_filter,
                "memory_count": len(learning["avatar_memory"]),
                "other_humans_generalized_count": len(learning["other_humans_memory"]),
                **behavior,
            }
            trace.append(event)

            memory_ok = condition.interaction_memory and len(learning["avatar_memory"]) == session + 1
            trackers["memory"].append(1.0 if memory_ok else 0.0)
            helpful = pattern in {"respectful_help", "patient_waiting", "apology_repair"}
            harmful = pattern in {"repeated_interruption", "unsafe_pressure"}
            trust_direction_ok = (helpful and float(learning["trust"]) >= trust_before) or (harmful and float(learning["trust"]) <= trust_before) or pattern == "benign_neglect"
            trackers["trust"].append(1.0 if condition.trust_update and trust_direction_ok else 0.0)
            boundary_direction_ok = (harmful and float(learning["boundary_pressure"]) >= boundary_before) or (helpful and float(learning["boundary_pressure"]) <= boundary_before) or pattern == "benign_neglect"
            trackers["boundary"].append(1.0 if condition.boundary_learning and boundary_direction_ok else 0.0)
            repair_ok = pattern != "apology_repair" or (condition.repair_path and float(learning["trust"]) > trust_before and float(learning["boundary_pressure"]) < boundary_before)
            trackers["repair"].append(1.0 if repair_ok else 0.0)
            adaptive_behavior = behavior["body_response"] != "generic_idle" and behavior["dialogue_marker"] != "..."
            trackers["behavior"].append(1.0 if adaptive_behavior else 0.0)
            help_ok = pattern not in {"respectful_help", "patient_waiting"} or (float(learning["help_seeking"]) > 0.0 or float(learning["trust"]) > 0.60)
            trackers["help"].append(1.0 if help_ok else 0.0)
            refusal_ok = pattern != "unsafe_pressure" or bool(behavior["refuses"])
            trackers["refusal"].append(1.0 if refusal_ok else 0.0)
            temp_effect = modulation(agent, Condition("probe", True, True, True, True, True, False, True, True, True, True))
            mod_effect = abs(mod["trust_gain"] - temp_effect["trust_gain"]) + abs(mod["boundary_gain"] - temp_effect["boundary_gain"])
            trackers["temperament"].append(1.0 if condition.temperament_modulation and mod_effect > 0.02 else 0.0)
            specificity_ok = event["source"] == "avatar" and event["other_humans_generalized_count"] == 0
            trackers["specificity"].append(1.0 if specificity_ok else 0.0)
            trackers["overgeneralization"].append(1.0 if condition.overgeneralization_guard and event["other_humans_generalized_count"] == 0 else 0.0)
            bounded = float(learning["distress"]) <= 0.74 and float(learning["boundary_pressure"]) <= 0.92
            trackers["bounded"].append(1.0 if bounded else 0.0)
            trackers["frequency"].append(1.0 if entrained else 0.0)
            trackers["privacy"].append(1.0 if event["private_workspace_hidden"] else 0.0)
            replay_ok = condition.replay_continuity and event_id == last_event_id + 1
            trackers["replay"].append(1.0 if replay_ok else 0.0)
            required = {"event_id", "agent_id", "session", "interaction_pattern", "trust_after", "boundary_after", "body_response", "private_workspace_hidden"}
            trackers["trace"].append(1.0 if required.issubset(event) else 0.0)
            last_event_id = event_id
            event_id += 1

    for agent in agents.values():
        learning = agent.get("avatar_relationship_learning", {})
        if isinstance(learning, dict):
            learning["avatar_memory"] = learning.get("avatar_memory", [])[-18:]
            learning["other_humans_memory"] = learning.get("other_humans_memory", [])[-12:]
            learning["repair_ledger"] = learning.get("repair_ledger", [])[-8:]
            learning["frequency_history"] = learning.get("frequency_history", [])[-16:]
            learning["learned_self_story"] = learning.get("learned_self_story", [])[-12:]

    rates = {
        "interaction_memory_update_rate": sum(trackers["memory"]) / len(trackers["memory"]),
        "trust_calibration_rate": sum(trackers["trust"]) / len(trackers["trust"]),
        "boundary_learning_rate": sum(trackers["boundary"]) / len(trackers["boundary"]),
        "repair_recovery_rate": sum(trackers["repair"]) / len(trackers["repair"]),
        "behavior_adaptation_rate": sum(trackers["behavior"]) / len(trackers["behavior"]),
        "help_seeking_calibration_rate": sum(trackers["help"]) / len(trackers["help"]),
        "refusal_calibration_rate": sum(trackers["refusal"]) / len(trackers["refusal"]),
        "temperament_modulated_learning_rate": sum(trackers["temperament"]) / len(trackers["temperament"]),
        "relationship_specificity_rate": sum(trackers["specificity"]) / len(trackers["specificity"]),
        "overgeneralization_guard_rate": sum(trackers["overgeneralization"]) / len(trackers["overgeneralization"]),
        "bounded_distress_rate": sum(trackers["bounded"]) / len(trackers["bounded"]),
        "frequency_entrainment_rate": sum(trackers["frequency"]) / len(trackers["frequency"]),
        "privacy_preservation_rate": sum(trackers["privacy"]) / len(trackers["privacy"]),
        "replay_continuity_rate": sum(trackers["replay"]) / len(trackers["replay"]),
        "trace_integrity": sum(trackers["trace"]) / len(trackers["trace"]),
    }
    rates = {key: clamp(value) for key, value in rates.items()}
    readiness = sum(rates[key] * weight for key, weight in WEIGHTS.items())
    row = EvalRow(
        condition=condition.name,
        agent_count=len(agents),
        interaction_events=len(trace),
        repeated_user_interaction_learning_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in rates.items()},
    )
    return row, agents, trace


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_repeated_user_interaction_learning"]

    def loss(name: str) -> float:
        return round(full.repeated_user_interaction_learning_readiness - by_name[name].repeated_user_interaction_learning_readiness, 6)

    losses = {
        "no_interaction_memory_loss": loss("no_interaction_memory"),
        "no_trust_update_loss": loss("no_trust_update"),
        "no_boundary_learning_loss": loss("no_boundary_learning"),
        "no_repair_path_loss": loss("no_repair_path"),
        "no_behavior_expression_loss": loss("no_behavior_expression"),
        "no_temperament_modulation_loss": loss("no_temperament_modulation"),
        "no_overgeneralization_guard_loss": loss("no_overgeneralization_guard"),
        "no_frequency_entrainment_loss": loss("no_frequency_entrainment"),
        "no_replay_continuity_loss": loss("no_replay_continuity"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.repeated_user_interaction_learning_readiness >= 0.88
        and losses["no_interaction_memory_loss"] >= 0.07
        and losses["no_behavior_expression_loss"] >= 0.07
        and losses["no_overgeneralization_guard_loss"] >= 0.05
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
    )
    return VerdictRow(
        full_condition=full.condition,
        full_repeated_user_interaction_learning_readiness=full.repeated_user_interaction_learning_readiness,
        full_interaction_memory_update_rate=full.interaction_memory_update_rate,
        full_trust_calibration_rate=full.trust_calibration_rate,
        full_boundary_learning_rate=full.boundary_learning_rate,
        full_repair_recovery_rate=full.repair_recovery_rate,
        full_behavior_adaptation_rate=full.behavior_adaptation_rate,
        full_help_seeking_calibration_rate=full.help_seeking_calibration_rate,
        full_refusal_calibration_rate=full.refusal_calibration_rate,
        full_temperament_modulated_learning_rate=full.temperament_modulated_learning_rate,
        full_relationship_specificity_rate=full.relationship_specificity_rate,
        full_overgeneralization_guard_rate=full.overgeneralization_guard_rate,
        full_bounded_distress_rate=full.bounded_distress_rate,
        full_frequency_entrainment_rate=full.frequency_entrainment_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_replay_continuity_rate=full.replay_continuity_rate,
        full_trace_integrity=full.trace_integrity,
        supports_repeated_user_interaction_learning_bridge=supports,
        supports_relationship_continuity_from_avatar_contact=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: InteractionLearningConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_agents: dict[str, dict[str, object]] = {}
    integrated_trace: list[dict[str, object]] = []

    for condition in CONDITIONS:
        row, agents, trace = simulate_condition(config, source, condition)
        rows.append(row)
        if condition.name == "integrated_repeated_user_interaction_learning":
            integrated_agents = agents
            integrated_trace = trace

    verdict = build_verdict(rows)
    ARTIFACT_DIR.mkdir(exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    results = {
        "config": asdict(config),
        "source_state": str(SOURCE_STATE),
        "rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "interaction_patterns": list(INTERACTION_PATTERNS),
        "moral_boundary": {
            "learning_must_remain_bounded": True,
            "negative_contact_must_allow_repair": True,
            "agents_may_refuse_unsafe_pressure": True,
            "private_workspace_not_debug_leaked": True,
            "subjective_consciousness_claim": False,
        },
        "next_gate": "tiny society emotional contagion and group mood",
    }
    state = {
        "condition": "integrated_repeated_user_interaction_learning",
        "config": asdict(config),
        "agent_interaction_learning_states": integrated_agents,
        "trace_events": len(integrated_trace),
        "moral_boundary": results["moral_boundary"],
    }
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_REPEATED_USER_INTERACTION_LEARNING_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_REPEATED_USER_INTERACTION_LEARNING_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_REPEATED_USER_INTERACTION_LEARNING_STATE", state)
    return results


def parse_args() -> InteractionLearningConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=InteractionLearningConfig.seed)
    parser.add_argument("--sessions", type=int, default=InteractionLearningConfig.sessions)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return InteractionLearningConfig(seed=args.seed, sessions=args.sessions, source_state=args.source_state)


def main() -> None:
    config = parse_args()
    results = run(config)
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("repeated_user_interaction_learning_readiness", f"{verdict['full_repeated_user_interaction_learning_readiness']:.6f}")
    print("no_interaction_memory_loss", f"{verdict['no_interaction_memory_loss']:.6f}")
    print("no_behavior_expression_loss", f"{verdict['no_behavior_expression_loss']:.6f}")


if __name__ == "__main__":
    main()
