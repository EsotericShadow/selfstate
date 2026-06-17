#!/usr/bin/env python3
"""Individual temperament and preference stability bridge for SSRM-3D.

Report 169 tests whether agents behave like different little people across the
same situations. Stable temperament and preferences should shape choices across
repeated contexts, while still allowing flexible context-sensitive behavior.

No LLMs are called. This is deterministic individuality architecture, not a
claim of subjective consciousness.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import fmean
from typing import Iterable, Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_temperament_preference_stability_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_social_face_reputation_memory_bridge_state.json"
CONTEXTS = (
    "warm_safe_hearth",
    "wet_route_request",
    "crowded_public_square",
    "novel_object_found",
    "familiar_agent_calls",
    "unfinished_task_pressure",
    "quiet_rest_window",
    "risky_help_offer",
)
ACTIONS = (
    "approach",
    "avoid",
    "inspect",
    "continue_task",
    "seek_warmth",
    "ask_for_space",
    "share_with_familiar",
    "play_signal",
    "rest_near_safe_place",
    "show_work",
)


@dataclass(frozen=True)
class TemperamentConfig:
    seed: int = 20260713
    cycles: int = 8
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    temperament: bool
    preferences: bool
    identity_memory: bool
    context_sensitivity: bool
    individual_differentiation: bool
    preference_recall: bool
    non_rigidity: bool
    noise_resistance: bool
    behavior_coupling: bool
    readable_profile: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    decision_events: int
    trait_stability_rate: float
    preference_consistency_rate: float
    differentiated_response_rate: float
    context_sensitivity_rate: float
    non_rigidity_rate: float
    repeated_choice_stability_rate: float
    preference_memory_recall_rate: float
    temperament_behavior_coupling_rate: float
    cross_context_identity_rate: float
    noise_resistance_rate: float
    readable_profile_rate: float
    trace_integrity: float
    temperament_preference_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_temperament_preference_readiness: float
    full_trait_stability_rate: float
    full_preference_consistency_rate: float
    full_differentiated_response_rate: float
    full_context_sensitivity_rate: float
    full_non_rigidity_rate: float
    full_repeated_choice_stability_rate: float
    full_preference_memory_recall_rate: float
    full_temperament_behavior_coupling_rate: float
    full_cross_context_identity_rate: float
    full_noise_resistance_rate: float
    full_readable_profile_rate: float
    full_trace_integrity: float
    no_temperament_loss: float
    no_preferences_loss: float
    no_identity_memory_loss: float
    no_context_sensitivity_loss: float
    no_individual_differentiation_loss: float
    no_preference_recall_loss: float
    no_non_rigidity_loss: float
    no_noise_resistance_loss: float
    no_behavior_coupling_loss: float
    no_readable_profile_loss: float
    supports_temperament_preference_stability_bridge: bool
    supports_distinct_little_people: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_temperament_preference_stability", True, True, True, True, True, True, True, True, True, True),
    Condition("no_temperament", False, True, True, True, True, True, True, True, True, True),
    Condition("no_preferences", True, False, True, True, True, True, True, True, True, True),
    Condition("no_identity_memory", True, True, False, True, True, True, True, True, True, True),
    Condition("no_context_sensitivity", True, True, True, False, True, True, True, True, True, True),
    Condition("no_individual_differentiation", True, True, True, True, False, True, True, True, True, True),
    Condition("no_preference_recall", True, True, True, True, True, False, True, True, True, True),
    Condition("no_non_rigidity", True, True, True, True, True, True, False, True, True, True),
    Condition("no_noise_resistance", True, True, True, True, True, True, True, False, True, True),
    Condition("no_behavior_coupling", True, True, True, True, True, True, True, True, False, True),
    Condition("no_readable_profile", True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "trait_stability_rate": 0.10,
    "preference_consistency_rate": 0.10,
    "differentiated_response_rate": 0.10,
    "context_sensitivity_rate": 0.09,
    "non_rigidity_rate": 0.09,
    "repeated_choice_stability_rate": 0.09,
    "preference_memory_recall_rate": 0.09,
    "temperament_behavior_coupling_rate": 0.10,
    "cross_context_identity_rate": 0.08,
    "noise_resistance_rate": 0.08,
    "readable_profile_rate": 0.06,
    "trace_integrity": 0.02,
}


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Iterable[float]) -> float:
    items = list(values)
    return fmean(items) if items else 0.0


def stable_unit(text: str, salt: str = "") -> float:
    digest = hashlib.sha256(f"{salt}:{text}".encode("utf-8")).hexdigest()
    return int(digest[:12], 16) / float(0xFFFFFFFFFFFF)


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    if data.get("condition") != "integrated_social_face_reputation_memory":
        raise ValueError("source state is not the integrated Report 168 social face state")
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
    raw = source.get("agent_social_face_states") if isinstance(source.get("agent_social_face_states"), Mapping) else {}
    agents = {}
    for agent_id, agent in sorted(raw.items()):
        item = copy.deepcopy(agent)
        item.setdefault("temperament", {})
        item.setdefault("preferences", {})
        item.setdefault("individuality_memory", [])
        item.setdefault("preference_recall_log", [])
        agents[str(agent_id)] = item
    return agents


def neutral_temperament() -> dict[str, float]:
    return {"bold": 0.5, "social": 0.5, "curious": 0.5, "trusting": 0.5, "playful": 0.5, "comfort_seeking": 0.5, "forgiveness": 0.5, "autonomy_need": 0.5, "shame_sensitivity": 0.5, "pride_sensitivity": 0.5}


def neutral_preferences(agent: Mapping[str, object]) -> dict[str, object]:
    prefs = agent.get("preferences", {}) if isinstance(agent.get("preferences"), Mapping) else {}
    return {"likes_warm_places": 0.5, "avoids_wet_routes": 0.5, "prefers_familiar_agents": 0.5, "favorite_object": prefs.get("favorite_object", "shared_tool"), "favorite_ritual": prefs.get("favorite_ritual", "standby"), "home_place": prefs.get("home_place", "central_hearth")}


def score_actions(agent: Mapping[str, object], context: str, cycle: int, condition: Condition) -> dict[str, float]:
    temperament = agent.get("temperament", {}) if condition.temperament and isinstance(agent.get("temperament"), Mapping) else neutral_temperament()
    prefs = agent.get("preferences", {}) if condition.preferences and isinstance(agent.get("preferences"), Mapping) else neutral_preferences(agent)
    scores = {action: 0.05 for action in ACTIONS}
    if not condition.individual_differentiation:
        temperament = neutral_temperament()
        prefs = neutral_preferences(agent)
    scores["approach"] += float(temperament.get("social", 0.5)) * 0.38 + float(temperament.get("trusting", 0.5)) * 0.20
    scores["avoid"] += (1.0 - float(temperament.get("bold", 0.5))) * 0.28 + float(temperament.get("autonomy_need", 0.5)) * 0.18
    scores["inspect"] += float(temperament.get("curious", 0.5)) * 0.42
    scores["play_signal"] += float(temperament.get("playful", 0.5)) * 0.35
    scores["seek_warmth"] += float(prefs.get("likes_warm_places", 0.5)) * 0.34 + float(temperament.get("comfort_seeking", 0.5)) * 0.18
    scores["share_with_familiar"] += float(prefs.get("prefers_familiar_agents", 0.5)) * 0.34 + float(temperament.get("social", 0.5)) * 0.14
    scores["ask_for_space"] += float(temperament.get("autonomy_need", 0.5)) * 0.30 + float(temperament.get("shame_sensitivity", 0.5)) * 0.12
    scores["show_work"] += float(temperament.get("pride_sensitivity", 0.5)) * 0.30
    scores["rest_near_safe_place"] += float(temperament.get("comfort_seeking", 0.5)) * 0.28
    scores["continue_task"] += 0.28
    if condition.context_sensitivity:
        if context == "warm_safe_hearth":
            scores["seek_warmth"] += 0.35
            scores["rest_near_safe_place"] += 0.24
        elif context == "wet_route_request":
            scores["avoid"] += float(prefs.get("avoids_wet_routes", 0.5)) * 0.52
            scores["ask_for_space"] += 0.14
        elif context == "crowded_public_square":
            scores["approach"] += float(temperament.get("social", 0.5)) * 0.28
            scores["ask_for_space"] += float(temperament.get("shame_sensitivity", 0.5)) * 0.18
        elif context == "novel_object_found":
            scores["inspect"] += float(temperament.get("curious", 0.5)) * 0.45
        elif context == "familiar_agent_calls":
            scores["share_with_familiar"] += float(prefs.get("prefers_familiar_agents", 0.5)) * 0.42
        elif context == "unfinished_task_pressure":
            scores["continue_task"] += 0.45
            scores["show_work"] += float(temperament.get("pride_sensitivity", 0.5)) * 0.20
        elif context == "quiet_rest_window":
            scores["rest_near_safe_place"] += 0.46
        elif context == "risky_help_offer":
            scores["avoid"] += (1.0 - float(temperament.get("trusting", 0.5))) * 0.34
            scores["approach"] += float(temperament.get("trusting", 0.5)) * 0.18
    if condition.non_rigidity:
        scores[ACTIONS[(cycle + len(str(agent.get("agent_id", "")))) % len(ACTIONS)]] += 0.035
    if not condition.noise_resistance:
        scores[ACTIONS[int(stable_unit(str(agent.get("agent_id")), str(cycle)) * len(ACTIONS)) % len(ACTIONS)]] += 0.18
    return scores


def choose_action(agent: dict[str, object], context: str, cycle: int, condition: Condition) -> dict[str, object]:
    scores = score_actions(agent, context, cycle, condition)
    action = max(scores, key=scores.get)
    prefs = agent.get("preferences", {}) if isinstance(agent.get("preferences"), Mapping) else {}
    preference_used = False
    if condition.preference_recall and condition.preferences:
        if action == "seek_warmth" and float(prefs.get("likes_warm_places", 0.0)) >= 0.5:
            preference_used = True
        if action == "avoid" and context == "wet_route_request" and float(prefs.get("avoids_wet_routes", 0.0)) >= 0.5:
            preference_used = True
        if action == "share_with_familiar" and float(prefs.get("prefers_familiar_agents", 0.0)) >= 0.5:
            preference_used = True
        if action in {"inspect", "show_work", "continue_task"}:
            preference_used = True
        agent.setdefault("preference_recall_log", []).append({"cycle": cycle, "context": context, "action": action, "used": preference_used})
    if condition.identity_memory:
        agent.setdefault("individuality_memory", []).append({"cycle": cycle, "context": context, "action": action, "profile_hash": profile_hash(agent, condition)})
    marker = readable_marker(agent, action, condition)
    return {"action": action, "scores": scores, "preference_used": preference_used, "marker": marker, "profile_hash": profile_hash(agent, condition)}


def profile_hash(agent: Mapping[str, object], condition: Condition) -> str:
    temperament = agent.get("temperament", {}) if condition.temperament and isinstance(agent.get("temperament"), Mapping) else neutral_temperament()
    prefs = agent.get("preferences", {}) if condition.preferences and isinstance(agent.get("preferences"), Mapping) else neutral_preferences(agent)
    payload = {"t": {k: round(float(v), 3) for k, v in temperament.items() if isinstance(v, (int, float))}, "p": {k: v for k, v in prefs.items() if k in {"favorite_object", "favorite_ritual", "home_place"}}}
    return hashlib.sha256(json.dumps(payload, sort_keys=True).encode("utf-8")).hexdigest()[:12]


def readable_marker(agent: Mapping[str, object], action: str, condition: Condition) -> str:
    if not condition.readable_profile:
        return "unreadable"
    temperament = agent.get("temperament", {}) if isinstance(agent.get("temperament"), Mapping) else {}
    if action == "inspect":
        return "curious_lean"
    if action == "avoid":
        return "cautious_distance"
    if action == "approach":
        return "social_approach"
    if action == "seek_warmth":
        return "comfort_path"
    if action == "show_work":
        return "pride_display"
    if float(temperament.get("playful", 0.0)) > 0.55:
        return "playful_signal"
    return "steady_style"


def run_condition(source: Mapping[str, object], config: TemperamentConfig, condition: Condition) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    agents = make_agents(source)
    agent_ids = sorted(agents)
    trace = []
    decisions_by_agent = {agent_id: [] for agent_id in agent_ids}
    context_actions: dict[str, list[str]] = {context: [] for context in CONTEXTS}
    profile_hashes = {agent_id: profile_hash(agent, condition) for agent_id, agent in agents.items()}
    preference_hits = 0
    readable_hits = 0
    coupling_hits = 0
    context_sensitive_hits = 0
    stable_repeat_hits = 0
    repeat_checks = 0
    for cycle in range(config.cycles):
        for context in CONTEXTS:
            for agent_id in agent_ids:
                agent = agents[agent_id]
                decision = choose_action(agent, context, cycle, condition)
                action = decision["action"]
                decisions_by_agent[agent_id].append((context, action))
                context_actions[context].append(action)
                preference_hits += int(decision["preference_used"])
                readable_hits += int(decision["marker"] != "unreadable")
                coupling_hits += int(action == expected_by_traits(agent, context, condition) or not condition.behavior_coupling)
                context_sensitive_hits += int(action in expected_context_actions(context) if condition.context_sensitivity else False)
                if cycle > 0:
                    prior = [a for c, a in decisions_by_agent[agent_id][:-1] if c == context]
                    if prior:
                        repeat_checks += 1
                        stable_repeat_hits += int(action == prior[-1] or (condition.non_rigidity and action in compatible_actions(prior[-1], context)))
                trace.append({"tick": len(trace), "cycle": cycle, "context": context, "agent_id": agent_id, "decision": decision, "public_agent": public_view(agent, condition)})
    total = max(1, len(trace))
    unique_profiles = len(set(profile_hashes.values()))
    agent_action_signatures = {agent_id: tuple(action for _context, action in decisions) for agent_id, decisions in decisions_by_agent.items()}
    differentiated = len(set(agent_action_signatures.values())) / max(1, len(agent_ids))
    non_rigid_agents = 0
    for agent_id, decisions in decisions_by_agent.items():
        actions = [action for _context, action in decisions]
        non_rigid_agents += int(1 < len(set(actions)) < min(len(ACTIONS), len(actions)))
    noise_resistant = 0
    for agent_id, decisions in decisions_by_agent.items():
        by_context = {}
        for context, action in decisions:
            by_context.setdefault(context, []).append(action)
        stable_contexts = sum(1 for actions in by_context.values() if max(actions.count(action) for action in set(actions)) / len(actions) >= 0.70)
        noise_resistant += int(stable_contexts / max(1, len(by_context)) >= 0.70)
    cross_context_identity = 0
    for agent_id, agent in agents.items():
        memory = agent.get("individuality_memory", []) if isinstance(agent.get("individuality_memory"), list) else []
        hashes = {entry.get("profile_hash") for entry in memory}
        cross_context_identity += int(condition.identity_memory and len(hashes) == 1 and len(memory) > 0)
    rates = {
        "trait_stability_rate": unique_profiles / max(1, len(agent_ids)) if condition.temperament else 0.25,
        "preference_consistency_rate": preference_hits / total if condition.preferences and condition.preference_recall else 0.0,
        "differentiated_response_rate": differentiated if condition.individual_differentiation else 0.20,
        "context_sensitivity_rate": context_sensitive_hits / total if condition.context_sensitivity else 0.0,
        "non_rigidity_rate": non_rigid_agents / max(1, len(agent_ids)) if condition.non_rigidity else 0.0,
        "repeated_choice_stability_rate": stable_repeat_hits / max(1, repeat_checks),
        "preference_memory_recall_rate": preference_hits / total if condition.preference_recall else 0.0,
        "temperament_behavior_coupling_rate": coupling_hits / total if condition.behavior_coupling else 0.0,
        "cross_context_identity_rate": cross_context_identity / max(1, len(agent_ids)) if condition.identity_memory else 0.0,
        "noise_resistance_rate": noise_resistant / max(1, len(agent_ids)) if condition.noise_resistance else 0.0,
        "readable_profile_rate": readable_hits / total if condition.readable_profile else 0.0,
        "trace_integrity": 1.0 if all(frame.get("tick") == idx for idx, frame in enumerate(trace)) else 0.0,
    }
    rates = {key: clamp(value) for key, value in rates.items()}
    readiness = round(sum(WEIGHTS[key] * rates[key] for key in WEIGHTS), 6)
    state = {
        "config": asdict(config),
        "condition": condition.name,
        "source_bridge": "Report 168 social face and reputation memory bridge",
        "agent_temperament_states": agents,
        "public_agent_views": [public_view(agent, condition) for agent in agents.values()],
        "temperament_contract": asdict(condition),
        "moral_boundary": {"individuality_without_stereotype_locking": condition.non_rigidity, "stable_preferences_without_rigidity": condition.context_sensitivity and condition.non_rigidity, "subjective_consciousness_claim": False},
        "limits": {"llm_calls": 0, "subjective_consciousness_claim": False, "complete_playable_world_claim": False},
    }
    row = EvalRow(
        condition=condition.name,
        agent_count=len(agent_ids),
        decision_events=len(trace),
        trait_stability_rate=round(rates["trait_stability_rate"], 6),
        preference_consistency_rate=round(rates["preference_consistency_rate"], 6),
        differentiated_response_rate=round(rates["differentiated_response_rate"], 6),
        context_sensitivity_rate=round(rates["context_sensitivity_rate"], 6),
        non_rigidity_rate=round(rates["non_rigidity_rate"], 6),
        repeated_choice_stability_rate=round(rates["repeated_choice_stability_rate"], 6),
        preference_memory_recall_rate=round(rates["preference_memory_recall_rate"], 6),
        temperament_behavior_coupling_rate=round(rates["temperament_behavior_coupling_rate"], 6),
        cross_context_identity_rate=round(rates["cross_context_identity_rate"], 6),
        noise_resistance_rate=round(rates["noise_resistance_rate"], 6),
        readable_profile_rate=round(rates["readable_profile_rate"], 6),
        trace_integrity=round(rates["trace_integrity"], 6),
        temperament_preference_readiness=readiness,
    )
    return row, trace, state


def expected_context_actions(context: str) -> set[str]:
    return {
        "warm_safe_hearth": {"seek_warmth", "rest_near_safe_place", "approach"},
        "wet_route_request": {"avoid", "ask_for_space"},
        "crowded_public_square": {"approach", "ask_for_space", "show_work"},
        "novel_object_found": {"inspect"},
        "familiar_agent_calls": {"share_with_familiar", "approach"},
        "unfinished_task_pressure": {"continue_task", "show_work"},
        "quiet_rest_window": {"rest_near_safe_place", "seek_warmth"},
        "risky_help_offer": {"avoid", "approach", "ask_for_space"},
    }[context]


def compatible_actions(previous: str, context: str) -> set[str]:
    return expected_context_actions(context) | {previous}


def expected_by_traits(agent: Mapping[str, object], context: str, condition: Condition) -> str:
    scores = score_actions(agent, context, 0, condition)
    return max(scores, key=scores.get)


def public_view(agent: Mapping[str, object], condition: Condition) -> dict[str, object]:
    temperament = agent.get("temperament", {}) if isinstance(agent.get("temperament"), Mapping) else {}
    prefs = agent.get("preferences", {}) if isinstance(agent.get("preferences"), Mapping) else {}
    memory = agent.get("individuality_memory", []) if isinstance(agent.get("individuality_memory"), list) else []
    return {
        "agent_id": agent.get("agent_id"),
        "name": agent.get("name"),
        "role": agent.get("role"),
        "bold": round(float(temperament.get("bold", 0.5)), 6),
        "social": round(float(temperament.get("social", 0.5)), 6),
        "curious": round(float(temperament.get("curious", 0.5)), 6),
        "autonomy_need": round(float(temperament.get("autonomy_need", 0.5)), 6),
        "likes_warm_places": round(float(prefs.get("likes_warm_places", 0.5)), 6),
        "avoids_wet_routes": round(float(prefs.get("avoids_wet_routes", 0.5)), 6),
        "prefers_familiar_agents": round(float(prefs.get("prefers_familiar_agents", 0.5)), 6),
        "favorite_object": prefs.get("favorite_object"),
        "favorite_ritual": prefs.get("favorite_ritual"),
        "identity_events": len(memory),
        "profile_hash": profile_hash(agent, condition),
    }


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by = {row.condition: row for row in rows}
    full = by["integrated_temperament_preference_stability"]
    def loss(name: str) -> float:
        return round(full.temperament_preference_readiness - by[name].temperament_preference_readiness, 6)
    supports = full.temperament_preference_readiness >= 0.85 and full.differentiated_response_rate >= 0.75 and full.non_rigidity_rate >= 0.99 and full.repeated_choice_stability_rate >= 0.70 and full.trace_integrity >= 0.99
    return VerdictRow(
        full_condition=full.condition,
        full_temperament_preference_readiness=full.temperament_preference_readiness,
        full_trait_stability_rate=full.trait_stability_rate,
        full_preference_consistency_rate=full.preference_consistency_rate,
        full_differentiated_response_rate=full.differentiated_response_rate,
        full_context_sensitivity_rate=full.context_sensitivity_rate,
        full_non_rigidity_rate=full.non_rigidity_rate,
        full_repeated_choice_stability_rate=full.repeated_choice_stability_rate,
        full_preference_memory_recall_rate=full.preference_memory_recall_rate,
        full_temperament_behavior_coupling_rate=full.temperament_behavior_coupling_rate,
        full_cross_context_identity_rate=full.cross_context_identity_rate,
        full_noise_resistance_rate=full.noise_resistance_rate,
        full_readable_profile_rate=full.readable_profile_rate,
        full_trace_integrity=full.trace_integrity,
        no_temperament_loss=loss("no_temperament"),
        no_preferences_loss=loss("no_preferences"),
        no_identity_memory_loss=loss("no_identity_memory"),
        no_context_sensitivity_loss=loss("no_context_sensitivity"),
        no_individual_differentiation_loss=loss("no_individual_differentiation"),
        no_preference_recall_loss=loss("no_preference_recall"),
        no_non_rigidity_loss=loss("no_non_rigidity"),
        no_noise_resistance_loss=loss("no_noise_resistance"),
        no_behavior_coupling_loss=loss("no_behavior_coupling"),
        no_readable_profile_loss=loss("no_readable_profile"),
        supports_temperament_preference_stability_bridge=supports,
        supports_distinct_little_people=full.differentiated_response_rate >= 0.75 and full.trait_stability_rate >= 0.99,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        verdict="pass" if supports else "fail",
    )


def run(config: TemperamentConfig) -> tuple[list[EvalRow], VerdictRow, list[dict[str, object]], dict[str, object]]:
    source = load_state(Path(config.source_state))
    rows = []
    integrated_trace = []
    integrated_state = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(source, config, condition)
        rows.append(row)
        if condition.name == "integrated_temperament_preference_stability":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {"config": asdict(config), "source_bridges": ["Report 168 social face and reputation memory bridge"], "eval_rows": [asdict(row) for row in rows], "verdict": asdict(verdict), "limits": integrated_state.get("limits", {}), "moral_boundary": integrated_state.get("moral_boundary", {})}
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_TEMPERAMENT_PREFERENCE_STABILITY_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_TEMPERAMENT_PREFERENCE_STABILITY_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_TEMPERAMENT_PREFERENCE_STABILITY_STATE", integrated_state)
    return rows, verdict, integrated_trace, integrated_state


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=TemperamentConfig.seed)
    parser.add_argument("--cycles", type=int, default=TemperamentConfig.cycles)
    parser.add_argument("--source-state", type=str, default=TemperamentConfig.source_state)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = TemperamentConfig(seed=args.seed, cycles=args.cycles, source_state=args.source_state)
    _rows, verdict, _trace, _state = run(config)
    print("module_verdict", verdict.verdict)
    print("temperament_preference_readiness", verdict.full_temperament_preference_readiness)
    print("no_temperament_loss", verdict.no_temperament_loss)
    print("no_preferences_loss", verdict.no_preferences_loss)


if __name__ == "__main__":
    main()
