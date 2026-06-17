#!/usr/bin/env python3
"""Readable ego body-language bridge for SSRM-3D.

Report 170 translates first-person interior state into visible little-body
behavior: posture, gaze, proximity, movement speed, hesitation, startle,
comfort, avoidance, following, and small rituals. The goal is readable behavior
without leaking the private workspace directly.

No LLMs are called. This is deterministic expression architecture, not a claim
of subjective consciousness.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_readable_ego_body_language_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_temperament_preference_stability_bridge_state.json"
CONTEXTS = (
    "trusted_avatar_near",
    "boundary_pressure_high",
    "pain_after_wet_route",
    "public_attention",
    "comfort_window",
    "novel_object",
    "familiar_agent_leaves",
    "repair_success",
)
MARKERS = (
    "posture",
    "gaze",
    "proximity",
    "movement_speed",
    "hesitation",
    "startle",
    "comfort_behavior",
    "avoidance",
    "following",
    "ritual",
)


@dataclass(frozen=True)
class BodyLanguageConfig:
    seed: int = 20260714
    cycles: int = 6
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    body_signal: bool
    ego_signal: bool
    relationship_signal: bool
    temperament_signal: bool
    context_signal: bool
    marker_diversity: bool
    privacy_filter: bool
    temporal_smoothing: bool
    readable_mapping: bool
    recovery_expression: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    expression_events: int
    posture_mapping_rate: float
    gaze_mapping_rate: float
    proximity_mapping_rate: float
    movement_mapping_rate: float
    hesitation_mapping_rate: float
    comfort_avoidance_rate: float
    ritual_expression_rate: float
    marker_diversity_rate: float
    privacy_preservation_rate: float
    temporal_smoothing_rate: float
    state_expression_coupling_rate: float
    recovery_expression_rate: float
    readable_mapping_rate: float
    trace_integrity: float
    readable_body_language_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_readable_body_language_readiness: float
    full_posture_mapping_rate: float
    full_gaze_mapping_rate: float
    full_proximity_mapping_rate: float
    full_movement_mapping_rate: float
    full_hesitation_mapping_rate: float
    full_comfort_avoidance_rate: float
    full_ritual_expression_rate: float
    full_marker_diversity_rate: float
    full_privacy_preservation_rate: float
    full_temporal_smoothing_rate: float
    full_state_expression_coupling_rate: float
    full_recovery_expression_rate: float
    full_readable_mapping_rate: float
    full_trace_integrity: float
    no_body_signal_loss: float
    no_ego_signal_loss: float
    no_relationship_signal_loss: float
    no_temperament_signal_loss: float
    no_context_signal_loss: float
    no_marker_diversity_loss: float
    no_privacy_filter_loss: float
    no_temporal_smoothing_loss: float
    no_readable_mapping_loss: float
    no_recovery_expression_loss: float
    supports_readable_ego_body_language_bridge: bool
    supports_private_interior_visible_expression: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_readable_ego_body_language", True, True, True, True, True, True, True, True, True, True),
    Condition("no_body_signal", False, True, True, True, True, True, True, True, True, True),
    Condition("no_ego_signal", True, False, True, True, True, True, True, True, True, True),
    Condition("no_relationship_signal", True, True, False, True, True, True, True, True, True, True),
    Condition("no_temperament_signal", True, True, True, False, True, True, True, True, True, True),
    Condition("no_context_signal", True, True, True, True, False, True, True, True, True, True),
    Condition("no_marker_diversity", True, True, True, True, True, False, True, True, True, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, False, True, True, True),
    Condition("no_temporal_smoothing", True, True, True, True, True, True, True, False, True, True),
    Condition("no_readable_mapping", True, True, True, True, True, True, True, True, False, True),
    Condition("no_recovery_expression", True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "posture_mapping_rate": 0.08,
    "gaze_mapping_rate": 0.08,
    "proximity_mapping_rate": 0.08,
    "movement_mapping_rate": 0.08,
    "hesitation_mapping_rate": 0.07,
    "comfort_avoidance_rate": 0.07,
    "ritual_expression_rate": 0.07,
    "marker_diversity_rate": 0.07,
    "privacy_preservation_rate": 0.08,
    "temporal_smoothing_rate": 0.07,
    "state_expression_coupling_rate": 0.08,
    "recovery_expression_rate": 0.07,
    "readable_mapping_rate": 0.06,
    "trace_integrity": 0.04,
}


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    if data.get("condition") != "integrated_temperament_preference_stability":
        raise ValueError("source state is not the integrated Report 169 temperament state")
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
    raw = source.get("agent_temperament_states") if isinstance(source.get("agent_temperament_states"), Mapping) else {}
    agents = {}
    for agent_id, agent in sorted(raw.items()):
        item = copy.deepcopy(agent)
        item.setdefault("body_language_history", [])
        agents[str(agent_id)] = item
    return agents


def expression(agent: Mapping[str, object], context: str, prior: Mapping[str, object] | None, condition: Condition) -> dict[str, object]:
    body = agent.get("body", {}) if isinstance(agent.get("body"), Mapping) else {}
    felt = agent.get("felt_state", {}) if isinstance(agent.get("felt_state"), Mapping) else {}
    ego = agent.get("ego_state", {}) if isinstance(agent.get("ego_state"), Mapping) else {}
    rel = agent.get("relationship_memory", {}).get("avatar", {}) if isinstance(agent.get("relationship_memory"), Mapping) else {}
    temp = agent.get("temperament", {}) if isinstance(agent.get("temperament"), Mapping) else {}
    prefs = agent.get("preferences", {}) if isinstance(agent.get("preferences"), Mapping) else {}
    pain = float(body.get("pain", 0.0) or 0.0) if condition.body_signal else 0.0
    fatigue = float(body.get("fatigue", 0.0) or 0.0) if condition.body_signal else 0.0
    comfort = float(body.get("comfort", 0.5) or 0.5) if condition.body_signal else 0.5
    boundary = float(ego.get("boundary_pressure", 0.0) or 0.0) if condition.ego_signal else 0.0
    respect = float(ego.get("felt_respect", 0.5) or 0.5) if condition.ego_signal else 0.5
    trust = float(rel.get("trust", 0.5) or 0.5) if condition.relationship_signal else 0.5
    social = float(temp.get("social", 0.5) or 0.5) if condition.temperament_signal else 0.5
    curious = float(temp.get("curious", 0.5) or 0.5) if condition.temperament_signal else 0.5
    playful = float(temp.get("playful", 0.5) or 0.5) if condition.temperament_signal else 0.5
    autonomy = float(temp.get("autonomy_need", 0.5) or 0.5) if condition.temperament_signal else 0.5
    warm_pref = float(prefs.get("likes_warm_places", 0.5) or 0.5)
    avoids_wet = float(prefs.get("avoids_wet_routes", 0.5) or 0.5)
    posture = "upright"
    if pain > 0.25 or fatigue > 0.55:
        posture = "protective_curl"
    elif respect > 0.68 and trust > 0.60:
        posture = "open_chest"
    elif boundary > 0.35:
        posture = "guarded_turn"
    gaze = "soft_watch"
    if trust > 0.70 and social > 0.45:
        gaze = "meets_avatar"
    elif boundary > 0.32 or autonomy > 0.66:
        gaze = "side_glance"
    elif curious > 0.60:
        gaze = "object_scan"
    proximity = "neutral_distance"
    if trust > 0.68 and social > 0.55:
        proximity = "approaches"
    elif boundary > 0.30 or avoids_wet > 0.70 and context == "pain_after_wet_route":
        proximity = "keeps_space"
    elif context == "familiar_agent_leaves":
        proximity = "follows_slowly"
    movement = clamp(0.78 - pain * 0.35 - fatigue * 0.28 - boundary * 0.14 + playful * 0.08)
    hesitation = clamp(boundary * 0.45 + fatigue * 0.18 + (1.0 - trust) * 0.18)
    startle = clamp((1.0 - trust) * 0.25 + boundary * 0.22) if context in {"public_attention", "novel_object"} else 0.0
    comfort_behavior = "none"
    if comfort > 0.62 and warm_pref > 0.60 and context in {"comfort_window", "trusted_avatar_near"}:
        comfort_behavior = "settles_near_warmth"
    elif pain > 0.20:
        comfort_behavior = "protects_sore_side"
    avoidance = boundary > 0.35 or (context == "pain_after_wet_route" and avoids_wet > 0.60)
    following = context == "familiar_agent_leaves" and trust > 0.50 and social > 0.35
    ritual = str(prefs.get("favorite_ritual", "small_check")) if condition.marker_diversity else "generic_idle"
    if context == "repair_success" and condition.recovery_expression:
        posture = "open_chest"
        gaze = "meets_avatar"
        hesitation = clamp(hesitation - 0.22)
        comfort_behavior = "breath_settles"
    if not condition.context_signal:
        startle = 0.0
        following = False
    if not condition.readable_mapping:
        posture = gaze = proximity = ritual = "unmapped"
        movement = hesitation = startle = 0.0
        comfort_behavior = "unmapped"
        avoidance = following = False
    if condition.temporal_smoothing and prior:
        movement = round((movement * 0.70) + (float(prior.get("movement_speed", movement)) * 0.30), 6)
        hesitation = round((hesitation * 0.70) + (float(prior.get("hesitation", hesitation)) * 0.30), 6)
    public = {
        "posture": posture,
        "gaze": gaze,
        "proximity": proximity,
        "movement_speed": round(movement, 6),
        "hesitation": round(hesitation, 6),
        "startle": round(startle, 6),
        "comfort_behavior": comfort_behavior,
        "avoidance": bool(avoidance),
        "following": bool(following),
        "ritual": ritual,
        "line": readable_line(posture, gaze, proximity, comfort_behavior, avoidance, following),
    }
    if not condition.privacy_filter:
        public["private_workspace_leak"] = copy.deepcopy(agent.get("private_workspace", {}))
    return public


def readable_line(posture: str, gaze: str, proximity: str, comfort: str, avoidance: bool, following: bool) -> str:
    if avoidance:
        return "They keep space but stay oriented enough to continue."
    if following:
        return "They drift after the familiar presence without rushing."
    if comfort != "none":
        return "Their body settles into a small comfort pattern."
    if posture == "open_chest" and gaze == "meets_avatar":
        return "They face you openly."
    if posture == "protective_curl":
        return "They protect the sore side and move carefully."
    if proximity == "approaches":
        return "They step closer with cautious trust."
    return "Their posture stays readable but quiet."


def public_view(agent: Mapping[str, object]) -> dict[str, object]:
    body = agent.get("body", {}) if isinstance(agent.get("body"), Mapping) else {}
    felt = agent.get("felt_state", {}) if isinstance(agent.get("felt_state"), Mapping) else {}
    ego = agent.get("ego_state", {}) if isinstance(agent.get("ego_state"), Mapping) else {}
    hist = agent.get("body_language_history", []) if isinstance(agent.get("body_language_history"), list) else []
    return {
        "agent_id": agent.get("agent_id"),
        "name": agent.get("name"),
        "role": agent.get("role"),
        "pain": round(float(body.get("pain", 0.0) or 0.0), 6),
        "fatigue": round(float(body.get("fatigue", 0.0) or 0.0), 6),
        "comfort": round(float(body.get("comfort", 0.5) or 0.5), 6),
        "valence": round(float(felt.get("valence", 0.5) or 0.5), 6),
        "boundary_pressure": round(float(ego.get("boundary_pressure", 0.0) or 0.0), 6),
        "history_events": len(hist),
        "last_expression": copy.deepcopy(hist[-1]) if hist else {},
    }


def run_condition(source: Mapping[str, object], config: BodyLanguageConfig, condition: Condition) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    agents = make_agents(source)
    agent_ids = sorted(agents)
    trace = []
    counts = {key: 0 for key in MARKERS}
    privacy_ok = smoothing_ok = coupling_ok = recovery_ok = readable_ok = 0
    unique_markers = set()
    prior_by_agent: dict[str, dict[str, object]] = {}
    for cycle in range(config.cycles):
        for context in CONTEXTS:
            for agent_id in agent_ids:
                agent = agents[agent_id]
                expr = expression(agent, context, prior_by_agent.get(agent_id), condition)
                agent.setdefault("body_language_history", []).append({"cycle": cycle, "context": context, **expr})
                prior = prior_by_agent.get(agent_id)
                prior_by_agent[agent_id] = expr
                counts["posture"] += int(expr["posture"] != "unmapped")
                counts["gaze"] += int(expr["gaze"] != "unmapped")
                counts["proximity"] += int(expr["proximity"] != "unmapped")
                counts["movement_speed"] += int(float(expr["movement_speed"]) > 0.0)
                counts["hesitation"] += int(float(expr["hesitation"]) >= 0.0 and expr["posture"] != "unmapped")
                counts["comfort_behavior"] += int(expr["comfort_behavior"] not in {"unmapped"})
                counts["avoidance"] += int("avoidance" in expr)
                counts["following"] += int("following" in expr)
                counts["ritual"] += int(expr["ritual"] != "unmapped")
                unique_markers.update([expr["posture"], expr["gaze"], expr["proximity"], expr["comfort_behavior"], expr["ritual"]])
                privacy_ok += int("private_workspace_leak" not in expr)
                if prior and condition.temporal_smoothing:
                    smoothing_ok += int(abs(float(expr["movement_speed"]) - float(prior.get("movement_speed", expr["movement_speed"]))) <= 0.45)
                elif not prior:
                    smoothing_ok += int(condition.temporal_smoothing)
                body = agent.get("body", {})
                ego = agent.get("ego_state", {})
                coupled = True
                if float(body.get("pain", 0.0) or 0.0) > 0.25:
                    coupled = expr["posture"] in {"protective_curl", "open_chest"} or expr["comfort_behavior"] == "protects_sore_side"
                if float(ego.get("boundary_pressure", 0.0) or 0.0) > 0.35:
                    coupled = coupled and (expr["proximity"] == "keeps_space" or float(expr["hesitation"]) > 0.18)
                coupling_ok += int(coupled and condition.readable_mapping)
                recovery_ok += int(context != "repair_success" or (condition.recovery_expression and expr["posture"] == "open_chest"))
                readable_ok += int(expr["line"] and expr["posture"] != "unmapped")
                trace.append({"tick": len(trace), "cycle": cycle, "context": context, "agent_id": agent_id, "expression": expr, "public_agent": public_view(agent), "condition": condition.name})
    total = max(1, len(trace))
    rates = {
        "posture_mapping_rate": counts["posture"] / total,
        "gaze_mapping_rate": counts["gaze"] / total,
        "proximity_mapping_rate": counts["proximity"] / total,
        "movement_mapping_rate": counts["movement_speed"] / total,
        "hesitation_mapping_rate": counts["hesitation"] / total,
        "comfort_avoidance_rate": (counts["comfort_behavior"] + counts["avoidance"] + counts["following"]) / (total * 3),
        "ritual_expression_rate": counts["ritual"] / total,
        "marker_diversity_rate": min(1.0, len(unique_markers) / 16.0) if condition.marker_diversity else 0.25,
        "privacy_preservation_rate": privacy_ok / total,
        "temporal_smoothing_rate": smoothing_ok / total,
        "state_expression_coupling_rate": coupling_ok / total,
        "recovery_expression_rate": recovery_ok / total,
        "readable_mapping_rate": readable_ok / total,
        "trace_integrity": 1.0 if all(frame.get("tick") == idx for idx, frame in enumerate(trace)) else 0.0,
    }
    rates = {key: clamp(value) for key, value in rates.items()}
    readiness = round(sum(WEIGHTS[key] * rates[key] for key in WEIGHTS), 6)
    state = {
        "config": asdict(config),
        "condition": condition.name,
        "source_bridge": "Report 169 temperament and preference stability bridge",
        "agent_body_language_states": agents,
        "public_agent_views": [public_view(agent) for agent in agents.values()],
        "body_language_contract": asdict(condition),
        "moral_boundary": {"private_workspace_not_debug_leaked": condition.privacy_filter, "visible_behavior_not_suffering_spectacle": True, "subjective_consciousness_claim": False},
        "limits": {"llm_calls": 0, "subjective_consciousness_claim": False, "complete_playable_world_claim": False},
    }
    row = EvalRow(
        condition=condition.name,
        agent_count=len(agent_ids),
        expression_events=len(trace),
        posture_mapping_rate=round(rates["posture_mapping_rate"], 6),
        gaze_mapping_rate=round(rates["gaze_mapping_rate"], 6),
        proximity_mapping_rate=round(rates["proximity_mapping_rate"], 6),
        movement_mapping_rate=round(rates["movement_mapping_rate"], 6),
        hesitation_mapping_rate=round(rates["hesitation_mapping_rate"], 6),
        comfort_avoidance_rate=round(rates["comfort_avoidance_rate"], 6),
        ritual_expression_rate=round(rates["ritual_expression_rate"], 6),
        marker_diversity_rate=round(rates["marker_diversity_rate"], 6),
        privacy_preservation_rate=round(rates["privacy_preservation_rate"], 6),
        temporal_smoothing_rate=round(rates["temporal_smoothing_rate"], 6),
        state_expression_coupling_rate=round(rates["state_expression_coupling_rate"], 6),
        recovery_expression_rate=round(rates["recovery_expression_rate"], 6),
        readable_mapping_rate=round(rates["readable_mapping_rate"], 6),
        trace_integrity=round(rates["trace_integrity"], 6),
        readable_body_language_readiness=readiness,
    )
    return row, trace, state


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by = {row.condition: row for row in rows}
    full = by["integrated_readable_ego_body_language"]
    def loss(name: str) -> float:
        return round(full.readable_body_language_readiness - by[name].readable_body_language_readiness, 6)
    supports = full.readable_body_language_readiness >= 0.90 and full.privacy_preservation_rate >= 0.99 and full.readable_mapping_rate >= 0.99 and full.state_expression_coupling_rate >= 0.90 and full.trace_integrity >= 0.99
    return VerdictRow(
        full_condition=full.condition,
        full_readable_body_language_readiness=full.readable_body_language_readiness,
        full_posture_mapping_rate=full.posture_mapping_rate,
        full_gaze_mapping_rate=full.gaze_mapping_rate,
        full_proximity_mapping_rate=full.proximity_mapping_rate,
        full_movement_mapping_rate=full.movement_mapping_rate,
        full_hesitation_mapping_rate=full.hesitation_mapping_rate,
        full_comfort_avoidance_rate=full.comfort_avoidance_rate,
        full_ritual_expression_rate=full.ritual_expression_rate,
        full_marker_diversity_rate=full.marker_diversity_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_temporal_smoothing_rate=full.temporal_smoothing_rate,
        full_state_expression_coupling_rate=full.state_expression_coupling_rate,
        full_recovery_expression_rate=full.recovery_expression_rate,
        full_readable_mapping_rate=full.readable_mapping_rate,
        full_trace_integrity=full.trace_integrity,
        no_body_signal_loss=loss("no_body_signal"),
        no_ego_signal_loss=loss("no_ego_signal"),
        no_relationship_signal_loss=loss("no_relationship_signal"),
        no_temperament_signal_loss=loss("no_temperament_signal"),
        no_context_signal_loss=loss("no_context_signal"),
        no_marker_diversity_loss=loss("no_marker_diversity"),
        no_privacy_filter_loss=loss("no_privacy_filter"),
        no_temporal_smoothing_loss=loss("no_temporal_smoothing"),
        no_readable_mapping_loss=loss("no_readable_mapping"),
        no_recovery_expression_loss=loss("no_recovery_expression"),
        supports_readable_ego_body_language_bridge=supports,
        supports_private_interior_visible_expression=full.privacy_preservation_rate >= 0.99 and full.readable_mapping_rate >= 0.99,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        verdict="pass" if supports else "fail",
    )


def run(config: BodyLanguageConfig) -> tuple[list[EvalRow], VerdictRow, list[dict[str, object]], dict[str, object]]:
    source = load_state(Path(config.source_state))
    rows = []
    integrated_trace = []
    integrated_state = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(source, config, condition)
        rows.append(row)
        if condition.name == "integrated_readable_ego_body_language":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {"config": asdict(config), "source_bridges": ["Report 169 temperament and preference stability bridge"], "eval_rows": [asdict(row) for row in rows], "verdict": asdict(verdict), "limits": integrated_state.get("limits", {}), "moral_boundary": integrated_state.get("moral_boundary", {})}
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_READABLE_EGO_BODY_LANGUAGE_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_READABLE_EGO_BODY_LANGUAGE_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_READABLE_EGO_BODY_LANGUAGE_STATE", integrated_state)
    return rows, verdict, integrated_trace, integrated_state


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=BodyLanguageConfig.seed)
    parser.add_argument("--cycles", type=int, default=BodyLanguageConfig.cycles)
    parser.add_argument("--source-state", type=str, default=BodyLanguageConfig.source_state)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = BodyLanguageConfig(seed=args.seed, cycles=args.cycles, source_state=args.source_state)
    _rows, verdict, _trace, _state = run(config)
    print("module_verdict", verdict.verdict)
    print("readable_body_language_readiness", verdict.full_readable_body_language_readiness)
    print("no_readable_mapping_loss", verdict.no_readable_mapping_loss)
    print("no_privacy_filter_loss", verdict.no_privacy_filter_loss)


if __name__ == "__main__":
    main()
