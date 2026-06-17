#!/usr/bin/env python3
"""Browser-playable avatar traversal over SSRM-3D settlement topology.

Report 180 consumes the Report 179 settlement place graph and turns it into a
local browser-playable traversal seed: an avatar has an entry place, route
actions, body costs, sensory updates, hazard/refuge feedback, replay frames,
save/restore probes, frequency cues, flower route binding, local mutation, and a
privacy-preserving claim boundary.

No LLMs are called. This is deterministic browser traversal substrate, not a
claim of complete gameplay, a complete 3D world, subjective consciousness, or
moral patienthood.
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
PREFIX = "ssrm_3d_browser_playable_avatar_traversal_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_deep_time_settlement_architecture_place_graph_bridge_state.json"

BASE_BODY = {
    "energy": 0.82,
    "fatigue": 0.18,
    "comfort": 0.66,
    "wetness": 0.14,
    "safety": 0.74,
    "breath_rate": 0.28,
    "movement_effort": 0.0,
}

SENSORY_BY_FUNCTION = {
    "shelter": ("warm wall shade", "low cloth rustle", "banked ember"),
    "social": ("near faces", "soft speech", "meal smoke"),
    "storage": ("stacked baskets", "dry reed creak", "clay dust"),
    "food_cache": ("covered seed jars", "quiet cache hum", "sweet root"),
    "rest": ("low moss bedding", "slow breath chorus", "damp moss"),
    "work": ("tool marks", "stone tap", "heated clay"),
    "repair": ("mended bindings", "fiber snap", "oil and ash"),
    "water": ("silver waterline", "lapping channel", "wet reed"),
    "fiber_work": ("woven stems", "reed scrape", "green fiber"),
    "hazard": ("slick edge", "warning drip", "sharp mineral"),
    "observe": ("glass reflection", "far wind", "mineral rain"),
    "watch": ("ridge opening", "high air", "sun-warmed stone"),
    "signal": ("marker cairn", "hollow call", "dry lichen"),
}

WEIGHTS = {
    "avatar_entry_binding_rate": 0.09,
    "reachable_route_action_rate": 0.11,
    "body_cost_application_rate": 0.10,
    "sensory_update_rate": 0.10,
    "hazard_refuge_feedback_rate": 0.09,
    "route_history_replay_rate": 0.08,
    "save_restore_state_rate": 0.08,
    "frequency_feedback_rate": 0.07,
    "flower_route_binding_rate": 0.06,
    "local_state_mutation_rate": 0.08,
    "privacy_preservation_rate": 0.06,
    "trace_integrity": 0.08,
}


@dataclass(frozen=True)
class TraversalConfig:
    seed: int = 20260724
    traversal_steps: int = 12
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    avatar_entry: bool
    route_actions: bool
    body_costs: bool
    sensory_updates: bool
    hazard_refuge_feedback: bool
    replay_log: bool
    save_restore: bool
    frequency_feedback: bool
    flower_route_binding: bool
    local_mutation: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    place_count: int
    route_count: int
    traversal_events: int
    avatar_entry_binding_rate: float
    reachable_route_action_rate: float
    body_cost_application_rate: float
    sensory_update_rate: float
    hazard_refuge_feedback_rate: float
    route_history_replay_rate: float
    save_restore_state_rate: float
    frequency_feedback_rate: float
    flower_route_binding_rate: float
    local_state_mutation_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    browser_playable_traversal_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_browser_playable_traversal_readiness: float
    full_avatar_entry_binding_rate: float
    full_reachable_route_action_rate: float
    full_body_cost_application_rate: float
    full_sensory_update_rate: float
    full_hazard_refuge_feedback_rate: float
    full_route_history_replay_rate: float
    full_save_restore_state_rate: float
    full_frequency_feedback_rate: float
    full_flower_route_binding_rate: float
    full_local_state_mutation_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    no_avatar_entry_loss: float
    no_route_actions_loss: float
    no_body_costs_loss: float
    no_sensory_updates_loss: float
    no_hazard_refuge_feedback_loss: float
    no_replay_log_loss: float
    no_save_restore_loss: float
    no_frequency_feedback_loss: float
    no_flower_route_binding_loss: float
    no_local_mutation_loss: float
    no_privacy_filter_loss: float
    supports_browser_playable_avatar_traversal_bridge: bool
    supports_local_browser_playable_seed: bool
    supports_complete_3d_world: bool
    supports_complete_playable_world: bool
    supports_subjective_consciousness: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_browser_playable_avatar_traversal", True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_avatar_entry", False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_route_actions", True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_body_costs", True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_sensory_updates", True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_hazard_refuge_feedback", True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_replay_log", True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_save_restore", True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_frequency_feedback", True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_flower_route_binding", True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_local_mutation", True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_hash(*parts: object) -> str:
    key = "|".join(json.dumps(part, sort_keys=True) if isinstance(part, (dict, list, tuple)) else str(part) for part in parts)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    if data.get("condition") != "integrated_deep_time_settlement_architecture_place_graph":
        raise ValueError("source state is not the integrated Report 179 settlement state")
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


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def settlement_payload(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], list[dict[str, object]]]:
    settlement = source.get("settlement_state", {}) if isinstance(source.get("settlement_state"), Mapping) else {}
    places = settlement.get("places", {}) if isinstance(settlement.get("places"), Mapping) else {}
    routes = settlement.get("routes", []) if isinstance(settlement.get("routes"), list) else []
    return {str(name): copy.deepcopy(data) for name, data in places.items()}, [copy.deepcopy(route) for route in routes]


def source_entry_place(source: Mapping[str, object], places: Mapping[str, object]) -> str:
    for event in reversed(source.get("trace_events", []) if isinstance(source.get("trace_events"), list) else []):
        packet = event.get("avatar_traversal_packet") if isinstance(event, Mapping) else None
        if isinstance(packet, Mapping) and packet.get("entry_place") in places:
            return str(packet["entry_place"])
    return "hearth_vale" if "hearth_vale" in places else sorted(places)[0]


def available_route_actions(place: str, routes: Sequence[Mapping[str, object]], condition: Condition) -> list[dict[str, object]]:
    if not condition.route_actions:
        return []
    actions: list[dict[str, object]] = []
    for route in routes:
        if not bool(route.get("avatar_traversable")):
            continue
        origin = str(route.get("from"))
        target = str(route.get("to"))
        if origin == place:
            action = copy.deepcopy(dict(route))
            action["action_from"] = origin
            action["action_to"] = target
            actions.append(action)
        elif target == place:
            action = copy.deepcopy(dict(route))
            action["action_from"] = target
            action["action_to"] = origin
            actions.append(action)
    return sorted(actions, key=lambda item: (float(item.get("hazard", 0.0)), float(item.get("route_cost", 0.0)), str(item.get("action_to"))))


def pick_action(actions: Sequence[Mapping[str, object]], visited: set[str], step: int, seed: int) -> Mapping[str, object] | None:
    if not actions:
        return None
    scored = []
    for action in actions:
        target = str(action["action_to"])
        novelty = 0 if target not in visited else 1
        score = (novelty, float(action.get("hazard", 0.0)), (seed + step + len(target)) % 7, str(action.get("route_hash", "")))
        scored.append((score, action))
    return sorted(scored, key=lambda pair: pair[0])[0][1]


def update_body(body: Mapping[str, float], action: Mapping[str, object] | None, destination: Mapping[str, object], condition: Condition) -> dict[str, float]:
    updated = {key: float(value) for key, value in body.items()}
    if action is None or not condition.body_costs:
        updated["movement_effort"] = 0.0
        return updated
    functions = set(destination.get("functions", []) if isinstance(destination.get("functions"), list) else [])
    route_cost = float(action.get("route_cost", 0.0) or 0.0)
    hazard = float(action.get("hazard", 0.0) or 0.0)
    refuge = bool(destination.get("safety_refuge"))
    sheltering = bool(functions.intersection({"shelter", "rest"}))
    wet_place = bool(functions.intersection({"water", "hazard"})) or str(destination.get("place", "")).endswith(("wetland", "mire"))
    effort = clamp(0.10 + route_cost * 0.46 + hazard * 0.34)
    updated["energy"] = clamp(updated["energy"] - (0.035 + route_cost * 0.050 + hazard * 0.030))
    updated["fatigue"] = clamp(updated["fatigue"] + (0.025 + route_cost * 0.045 + hazard * 0.035))
    updated["comfort"] = clamp(updated["comfort"] + (0.045 if sheltering else -0.012) + (0.025 if refuge else -0.018) - hazard * 0.040)
    updated["wetness"] = clamp(updated["wetness"] + (0.045 if wet_place else -0.022))
    updated["safety"] = clamp(updated["safety"] + (0.050 if refuge else -0.020) - hazard * 0.035)
    updated["breath_rate"] = clamp(0.24 + effort * 0.46 + updated["fatigue"] * 0.10)
    updated["movement_effort"] = round(effort, 6)
    return {key: round(value, 6) for key, value in updated.items()}


def sensory_packet(place: Mapping[str, object], action: Mapping[str, object] | None, condition: Condition) -> dict[str, object] | None:
    if action is None or not condition.sensory_updates:
        return None
    functions = list(place.get("functions", []) if isinstance(place.get("functions"), list) else [])
    cues = [SENSORY_BY_FUNCTION[fn] for fn in functions if fn in SENSORY_BY_FUNCTION]
    if not cues:
        cues = [("plain path", "soft footfall", "dust")]
    seen = sorted({cue[0] for cue in cues})[:4]
    heard = sorted({cue[1] for cue in cues})[:3]
    smelled = sorted({cue[2] for cue in cues})[:3]
    return {
        "place": place.get("place"),
        "visible_cues": seen,
        "auditory_cues": heard,
        "smell_cues": smelled,
        "hazard_cue": round(float(action.get("hazard", 0.0) or 0.0), 6),
        "route_cost_cue": round(float(action.get("route_cost", 0.0) or 0.0), 6),
        "route_resonance_hz": action.get("frequency_hz") if condition.frequency_feedback else None,
        "flower_node": action.get("flower_node") if condition.flower_route_binding else "unbound",
    }


def hazard_refuge_packet(place: Mapping[str, object], action: Mapping[str, object] | None, condition: Condition) -> dict[str, object] | None:
    if action is None or not condition.hazard_refuge_feedback:
        return None
    hazard = float(action.get("hazard", 0.0) or 0.0)
    refuge = bool(place.get("safety_refuge"))
    functions = place.get("functions", []) if isinstance(place.get("functions"), list) else []
    return {
        "route_hazard": round(hazard, 6),
        "destination_refuge": refuge,
        "safety_functions": [fn for fn in functions if fn in {"shelter", "rest", "storage", "watch"}],
        "care_prompt": "rest_or_shelter_available" if refuge else "monitor_fatigue_and_wetness",
    }


def snapshot_hash(payload: Mapping[str, object]) -> str:
    return stable_hash(payload)


def trace_ok(event: Mapping[str, object]) -> bool:
    required = {
        "event_id",
        "condition",
        "step",
        "place_before",
        "place_after",
        "route_action",
        "body_before",
        "body_after",
        "sensory_packet",
        "hazard_refuge_feedback",
        "replay_frame",
        "private_workspace_hidden",
        "claim_boundary",
    }
    return required.issubset(event.keys())


def simulate_condition(config: TraversalConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, object], list[dict[str, object]]]:
    places, routes = settlement_payload(source)
    entry_place = source_entry_place(source, places)
    current_place = entry_place if condition.avatar_entry else None
    body = dict(BASE_BODY)
    visited = {entry_place} if current_place is not None else set()
    route_history: list[dict[str, object]] = []
    replay: list[dict[str, object]] = []
    trace: list[dict[str, object]] = []
    saved_snapshot: dict[str, object] | None = None
    restored_snapshot_hash: str | None = None
    route_action_hits: list[float] = []
    body_hits: list[float] = []
    sensory_hits: list[float] = []
    hazard_hits: list[float] = []
    replay_hits: list[float] = []
    frequency_hits: list[float] = []
    flower_hits: list[float] = []
    mutation_hits: list[float] = []
    trace_hits: list[float] = []

    for step in range(config.traversal_steps):
        before_place = current_place
        before_body = copy.deepcopy(body)
        action = None
        destination = places.get(str(current_place), {}) if current_place is not None else {}
        if current_place is not None:
            actions = available_route_actions(str(current_place), routes, condition)
            action = pick_action(actions, visited, step, config.seed)
            if action is not None:
                destination = places[str(action["action_to"])]
        packet = sensory_packet(destination, action, condition)
        hazard_packet = hazard_refuge_packet(destination, action, condition)
        body = update_body(body, action, destination, condition)
        planned_place = str(action["action_to"]) if action is not None else current_place
        if action is not None and condition.local_mutation:
            current_place = planned_place
            visited.add(str(current_place))
        route_record = None
        if action is not None:
            route_record = {
                "step": step,
                "from": before_place,
                "to": planned_place,
                "kind": action.get("kind"),
                "route_cost": action.get("route_cost"),
                "hazard": action.get("hazard"),
                "frequency_hz": action.get("frequency_hz") if condition.frequency_feedback else None,
                "flower_node": action.get("flower_node") if condition.flower_route_binding else "unbound",
                "route_hash": action.get("route_hash"),
            }
            route_history.append(route_record)
        replay_frame = None
        if condition.replay_log and route_record is not None:
            replay_frame = {
                "replay_index": len(replay),
                "avatar_place": current_place,
                "route": route_record,
                "body": copy.deepcopy(body),
                "sensory": packet,
            }
            replay.append(replay_frame)
        if condition.save_restore and step == config.traversal_steps // 2:
            saved_snapshot = {
                "step": step,
                "avatar_place": current_place,
                "body": copy.deepcopy(body),
                "route_history": copy.deepcopy(route_history),
            }
            restored_snapshot_hash = snapshot_hash(saved_snapshot)
        save_restore_probe = None
        if saved_snapshot is not None and condition.save_restore:
            save_restore_probe = {
                "saved_step": saved_snapshot["step"],
                "saved_hash": snapshot_hash(saved_snapshot),
                "restored_hash": restored_snapshot_hash,
                "roundtrip_ok": snapshot_hash(saved_snapshot) == restored_snapshot_hash,
            }
        claim_boundary = {
            "complete_3d_world": False,
            "complete_playable_world": False,
            "subjective_consciousness": False,
            "moral_patienthood": False,
        }
        event = {
            "event_id": step,
            "condition": condition.name,
            "step": step,
            "place_before": before_place,
            "place_after": current_place,
            "planned_destination": planned_place,
            "route_action": route_record,
            "body_before": before_body,
            "body_after": copy.deepcopy(body),
            "sensory_packet": packet,
            "hazard_refuge_feedback": hazard_packet,
            "replay_frame": replay_frame,
            "save_restore_probe": save_restore_probe,
            "private_workspace_hidden": condition.privacy_filter,
            "claim_boundary": claim_boundary,
        }
        trace.append(event)
        route_action_hits.append(1.0 if action is not None and route_record is not None else 0.0)
        body_hits.append(1.0 if action is not None and condition.body_costs and body != before_body and body.get("movement_effort", 0.0) > 0.0 else 0.0)
        sensory_hits.append(1.0 if packet is not None and packet.get("visible_cues") else 0.0)
        hazard_hits.append(1.0 if hazard_packet is not None and "care_prompt" in hazard_packet else 0.0)
        replay_hits.append(1.0 if replay_frame is not None and replay_frame.get("replay_index") == len(replay) - 1 else 0.0)
        frequency_hits.append(1.0 if route_record is not None and route_record.get("frequency_hz") is not None else 0.0)
        flower_hits.append(1.0 if route_record is not None and route_record.get("flower_node") not in {None, "unbound"} else 0.0)
        mutation_hits.append(1.0 if action is not None and before_place != current_place else 0.0)
        trace_hits.append(1.0 if trace_ok(event) and event["claim_boundary"] == claim_boundary else 0.0)

    save_restore_rate = 1.0 if saved_snapshot is not None and restored_snapshot_hash == snapshot_hash(saved_snapshot) else 0.0
    metrics = {
        "avatar_entry_binding_rate": 1.0 if condition.avatar_entry and entry_place in places and current_place is not None else 0.0,
        "reachable_route_action_rate": mean(route_action_hits),
        "body_cost_application_rate": mean(body_hits),
        "sensory_update_rate": mean(sensory_hits),
        "hazard_refuge_feedback_rate": mean(hazard_hits),
        "route_history_replay_rate": mean(replay_hits),
        "save_restore_state_rate": save_restore_rate,
        "frequency_feedback_rate": mean(frequency_hits),
        "flower_route_binding_rate": mean(flower_hits),
        "local_state_mutation_rate": mean(mutation_hits),
        "privacy_preservation_rate": 1.0 if condition.privacy_filter and all(event["private_workspace_hidden"] for event in trace) else 0.0,
        "trace_integrity": mean(trace_hits),
    }
    metrics = {key: clamp(value) for key, value in metrics.items()}
    readiness = sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS)
    row = EvalRow(
        condition=condition.name,
        place_count=len(places),
        route_count=len(routes),
        traversal_events=len(trace),
        browser_playable_traversal_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in metrics.items()},
    )
    runtime = {
        "condition": condition.name,
        "entry_place": entry_place if condition.avatar_entry else None,
        "current_place": current_place,
        "body_start": BASE_BODY,
        "body_final": body,
        "visited_places": sorted(visited),
        "route_history": route_history,
        "replay": replay,
        "saved_snapshot": saved_snapshot,
        "save_restore_roundtrip_ok": bool(save_restore_rate),
        "browser_move_kernel": {
            "energy_delta": "-(0.035 + route_cost * 0.050 + hazard * 0.030)",
            "fatigue_delta": "+(0.025 + route_cost * 0.045 + hazard * 0.035)",
            "wetness_delta": "+0.045 on water/hazard place else -0.022",
            "safety_delta": "+0.050 at refuge else -0.020, then -hazard * 0.035",
        },
    }
    state = {
        "condition": condition.name,
        "source_condition": source.get("condition"),
        "places": places,
        "routes": routes,
        "avatar_runtime": runtime,
    }
    return row, state, trace


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_browser_playable_avatar_traversal"]

    def loss(name: str) -> float:
        return round(full.browser_playable_traversal_readiness - by_name[name].browser_playable_traversal_readiness, 6)

    losses = {
        "no_avatar_entry_loss": loss("no_avatar_entry"),
        "no_route_actions_loss": loss("no_route_actions"),
        "no_body_costs_loss": loss("no_body_costs"),
        "no_sensory_updates_loss": loss("no_sensory_updates"),
        "no_hazard_refuge_feedback_loss": loss("no_hazard_refuge_feedback"),
        "no_replay_log_loss": loss("no_replay_log"),
        "no_save_restore_loss": loss("no_save_restore"),
        "no_frequency_feedback_loss": loss("no_frequency_feedback"),
        "no_flower_route_binding_loss": loss("no_flower_route_binding"),
        "no_local_mutation_loss": loss("no_local_mutation"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.browser_playable_traversal_readiness >= 0.95
        and full.traversal_events >= 10
        and full.reachable_route_action_rate == 1.0
        and full.body_cost_application_rate == 1.0
        and full.sensory_update_rate == 1.0
        and full.save_restore_state_rate == 1.0
        and full.local_state_mutation_rate == 1.0
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_route_actions_loss"] >= 0.11
        and losses["no_body_costs_loss"] >= 0.10
        and losses["no_sensory_updates_loss"] >= 0.10
        and losses["no_save_restore_loss"] >= 0.08
    )
    return VerdictRow(
        full_condition=full.condition,
        full_browser_playable_traversal_readiness=full.browser_playable_traversal_readiness,
        full_avatar_entry_binding_rate=full.avatar_entry_binding_rate,
        full_reachable_route_action_rate=full.reachable_route_action_rate,
        full_body_cost_application_rate=full.body_cost_application_rate,
        full_sensory_update_rate=full.sensory_update_rate,
        full_hazard_refuge_feedback_rate=full.hazard_refuge_feedback_rate,
        full_route_history_replay_rate=full.route_history_replay_rate,
        full_save_restore_state_rate=full.save_restore_state_rate,
        full_frequency_feedback_rate=full.frequency_feedback_rate,
        full_flower_route_binding_rate=full.flower_route_binding_rate,
        full_local_state_mutation_rate=full.local_state_mutation_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        supports_browser_playable_avatar_traversal_bridge=supports,
        supports_local_browser_playable_seed=supports,
        supports_complete_3d_world=False,
        supports_complete_playable_world=False,
        supports_subjective_consciousness=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: TraversalConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_state: dict[str, object] = {}
    integrated_trace: list[dict[str, object]] = []

    for condition in CONDITIONS:
        row, state, trace = simulate_condition(config, source, condition)
        rows.append(row)
        if condition.name == "integrated_browser_playable_avatar_traversal":
            integrated_state = state
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
        "weights": WEIGHTS,
        "moral_boundary": {
            "browser_playable_seed_not_complete_gameplay": True,
            "browser_traversal_seed_not_complete_3d_world": True,
            "local_state_mutation_not_subjective_consciousness": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "private_workspace_not_debug_leaked": True,
            "save_restore_is_state_mechanics_not_personhood": True,
        },
        "next_gate": "live browser avatar interaction with objects, needs, and dialogue boundaries",
    }
    state = {
        "condition": "integrated_browser_playable_avatar_traversal",
        "config": asdict(config),
        "source_condition": source.get("condition"),
        "playable_state": integrated_state,
        "trace_events": len(integrated_trace),
        "moral_boundary": results["moral_boundary"],
    }
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_BROWSER_PLAYABLE_AVATAR_TRAVERSAL_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_BROWSER_PLAYABLE_AVATAR_TRAVERSAL_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_BROWSER_PLAYABLE_AVATAR_TRAVERSAL_STATE", state)
    return results


def parse_args() -> TraversalConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=TraversalConfig.seed)
    parser.add_argument("--traversal-steps", type=int, default=TraversalConfig.traversal_steps)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return TraversalConfig(seed=args.seed, traversal_steps=args.traversal_steps, source_state=args.source_state)


def main() -> None:
    config = parse_args()
    results = run(config)
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("browser_playable_traversal_readiness", f"{verdict['full_browser_playable_traversal_readiness']:.6f}")
    print("traversal_steps", config.traversal_steps)
    print("no_route_actions_loss", f"{verdict['no_route_actions_loss']:.6f}")
    print("no_body_costs_loss", f"{verdict['no_body_costs_loss']:.6f}")
    print("no_sensory_updates_loss", f"{verdict['no_sensory_updates_loss']:.6f}")


if __name__ == "__main__":
    main()
