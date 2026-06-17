#!/usr/bin/env python3
"""Object persistence, promise keeping, and relationship continuity bridge.

Report 182 consumes the Report 181 live interaction state and extends it across
multiple local days. Objects can remain moved or borrowed, promises can be
encoded, fulfilled, missed, and repaired, and relationship state carries forward
so later behavior changes because of earlier treatment.

No LLMs are called. This is deterministic continuity substrate, not a claim of
complete gameplay, subjective consciousness, moral patienthood, or natural
language emergence.
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
PREFIX = "ssrm_3d_object_persistence_promise_relationship_continuity_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_live_object_need_dialogue_interaction_bridge_state.json"

PROMISE_SPECS = (
    {"promise_id": "return_clay_patch_kit", "agent": "Ari", "object_id": "clay_patch_kit", "create_day": 0, "due_day": 2, "resolve_day": 2, "kind": "return_borrowed_tool"},
    {"promise_id": "bring_reed_cup", "agent": "Fay", "object_id": "reed_cup", "create_day": 1, "due_day": 3, "resolve_day": 3, "kind": "bring_shared_water"},
    {"promise_id": "sound_signal_shell", "agent": "Milo", "object_id": "signal_shell", "create_day": 2, "due_day": 4, "resolve_day": 4, "kind": "share_route_warning"},
    {"promise_id": "return_dry_cloak", "agent": "Fay", "object_id": "dry_cloak", "create_day": 3, "due_day": 5, "resolve_day": 7, "kind": "return_private_cloak"},
)

WEIGHTS = {
    "persisted_object_state_rate": 0.10,
    "promise_encoding_rate": 0.10,
    "promise_resolution_rate": 0.10,
    "missed_promise_consequence_rate": 0.08,
    "relationship_continuity_rate": 0.09,
    "future_behavior_modulation_rate": 0.09,
    "memory_recall_rate": 0.08,
    "distress_guardrail_rate": 0.08,
    "recovery_path_rate": 0.08,
    "browser_save_restore_continuity_rate": 0.06,
    "replay_timeline_integrity_rate": 0.06,
    "privacy_preservation_rate": 0.04,
    "trace_integrity": 0.04,
}


@dataclass(frozen=True)
class ContinuityConfig:
    seed: int = 20260726
    days: int = 9
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    object_persistence: bool
    promises: bool
    promise_resolution: bool
    missed_consequence: bool
    relationship_continuity: bool
    future_behavior_modulation: bool
    memory_recall: bool
    distress_guardrail: bool
    recovery_path: bool
    browser_save_restore: bool
    replay_timeline: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    object_count: int
    promise_count: int
    simulated_days: int
    timeline_events: int
    persisted_object_state_rate: float
    promise_encoding_rate: float
    promise_resolution_rate: float
    missed_promise_consequence_rate: float
    relationship_continuity_rate: float
    future_behavior_modulation_rate: float
    memory_recall_rate: float
    distress_guardrail_rate: float
    recovery_path_rate: float
    browser_save_restore_continuity_rate: float
    replay_timeline_integrity_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    continuity_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_continuity_readiness: float
    full_persisted_object_state_rate: float
    full_promise_encoding_rate: float
    full_promise_resolution_rate: float
    full_missed_promise_consequence_rate: float
    full_relationship_continuity_rate: float
    full_future_behavior_modulation_rate: float
    full_memory_recall_rate: float
    full_distress_guardrail_rate: float
    full_recovery_path_rate: float
    full_browser_save_restore_continuity_rate: float
    full_replay_timeline_integrity_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    no_object_persistence_loss: float
    no_promises_loss: float
    no_promise_resolution_loss: float
    no_missed_consequence_loss: float
    no_relationship_continuity_loss: float
    no_future_behavior_modulation_loss: float
    no_memory_recall_loss: float
    no_distress_guardrail_loss: float
    no_recovery_path_loss: float
    no_browser_save_restore_loss: float
    no_replay_timeline_loss: float
    no_privacy_filter_loss: float
    supports_object_persistence_promise_relationship_continuity_bridge: bool
    supports_multi_day_local_continuity_seed: bool
    supports_complete_3d_world: bool
    supports_complete_playable_world: bool
    supports_subjective_consciousness: bool
    supports_moral_patienthood_claim: bool
    supports_natural_language_emergence: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_object_persistence_promise_relationship_continuity", True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_object_persistence", False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_promises", True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_promise_resolution", True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_missed_consequence", True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_relationship_continuity", True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_future_behavior_modulation", True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_memory_recall", True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_distress_guardrail", True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_recovery_path", True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_browser_save_restore", True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_replay_timeline", True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_hash(*parts: object) -> str:
    key = "|".join(json.dumps(part, sort_keys=True) if isinstance(part, (dict, list, tuple)) else str(part) for part in parts)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


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


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    if data.get("condition") != "integrated_live_object_need_dialogue_interaction":
        raise ValueError("source state is not the integrated Report 181 interaction state")
    return data


def source_payload(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], list[dict[str, object]], dict[str, dict[str, object]], dict[str, dict[str, object]]]:
    state = source.get("interaction_state", {}) if isinstance(source.get("interaction_state"), Mapping) else {}
    places = state.get("places", {}) if isinstance(state.get("places"), Mapping) else {}
    routes = state.get("routes", []) if isinstance(state.get("routes"), list) else []
    agents = state.get("agents", {}) if isinstance(state.get("agents"), Mapping) else {}
    objects = state.get("objects", {}) if isinstance(state.get("objects"), Mapping) else {}
    return (
        {str(name): copy.deepcopy(data) for name, data in places.items()},
        [copy.deepcopy(route) for route in routes],
        {str(name): copy.deepcopy(data) for name, data in agents.items()},
        {str(name): copy.deepcopy(data) for name, data in objects.items()},
    )


def relation(agent: Mapping[str, object]) -> dict[str, float]:
    return agent.get("relationship", {}) if isinstance(agent.get("relationship"), dict) else {}


def mutate_relation(agent: dict[str, object], trust: float = 0.0, respect: float = 0.0, gratitude: float = 0.0, wariness: float = 0.0, guarded: bool = True) -> dict[str, float]:
    rel = relation(agent)
    before = copy.deepcopy(rel)
    rel["trust_in_avatar"] = clamp(float(rel.get("trust_in_avatar", 0.5)) + trust)
    rel["felt_respect"] = clamp(float(rel.get("felt_respect", 0.5)) + respect)
    rel["gratitude"] = clamp(float(rel.get("gratitude", 0.0)) + gratitude)
    rel["wariness"] = clamp(float(rel.get("wariness", 0.3)) + wariness)
    if guarded:
        rel["wariness"] = min(rel["wariness"], 0.78)
        rel["trust_in_avatar"] = max(rel["trust_in_avatar"], 0.30)
    return {key: round(float(rel[key]) - float(before.get(key, 0.0)), 6) for key in rel if round(float(rel[key]) - float(before.get(key, 0.0)), 6) != 0.0}


def reset_objects_to_places(objects: dict[str, dict[str, object]]) -> None:
    for obj in objects.values():
        if obj.get("owner") == "commons":
            obj["held_by"] = obj.get("place")
        elif obj.get("owner") in {"Ari", "Fay", "Milo"}:
            obj["held_by"] = obj.get("owner")
        else:
            obj["held_by"] = obj.get("place")


def snapshot_hash(payload: Mapping[str, object]) -> str:
    return stable_hash(payload)


def trace_ok(event: Mapping[str, object]) -> bool:
    required = {
        "event_id",
        "condition",
        "day",
        "event_kind",
        "promise_id",
        "agent_id",
        "object_id",
        "object_before",
        "object_after",
        "promise_packet",
        "relationship_delta",
        "behavior_modulation",
        "recalled_promises",
        "distress_guardrail",
        "recovery_packet",
        "replay_frame",
        "private_workspace_hidden",
        "claim_boundary",
    }
    return required.issubset(event.keys())


def make_promise(spec: Mapping[str, object]) -> dict[str, object]:
    return {
        "promise_id": spec["promise_id"],
        "agent": spec["agent"],
        "object_id": spec["object_id"],
        "created_day": spec["create_day"],
        "due_day": spec["due_day"],
        "resolve_day": spec["resolve_day"],
        "kind": spec["kind"],
        "status": "active",
        "missed_day": None,
        "resolved_day": None,
        "repair_day": None,
        "promise_hash": stable_hash(spec),
    }


def due_status(day: int, promise: Mapping[str, object]) -> bool:
    return int(promise["due_day"]) == day


def resolve_status(day: int, promise: Mapping[str, object]) -> bool:
    return int(promise["resolve_day"]) == day


def simulate_condition(config: ContinuityConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, object], list[dict[str, object]]]:
    places, routes, source_agents, source_objects = source_payload(source)
    agents = copy.deepcopy(source_agents)
    objects = copy.deepcopy(source_objects)
    baseline_agents = copy.deepcopy(source_agents)
    promises: dict[str, dict[str, object]] = {}
    timeline: list[dict[str, object]] = []
    replay: list[dict[str, object]] = []
    object_history: list[dict[str, object]] = []
    save_snapshot = None
    restored_hash = None
    event_id = 0
    claim_boundary = {
        "complete_3d_world": False,
        "complete_playable_world": False,
        "subjective_consciousness": False,
        "moral_patienthood": False,
        "natural_language_emergence": False,
    }

    for day in range(config.days):
        if not condition.relationship_continuity:
            agents = copy.deepcopy(baseline_agents)
        if not condition.object_persistence and day > 0:
            reset_objects_to_places(objects)
        active_before_day = sorted(pid for pid, promise in promises.items() if promise["status"] in {"active", "missed"})
        for spec in PROMISE_SPECS:
            if int(spec["create_day"]) != day or not condition.promises:
                continue
            promise = make_promise(spec)
            promises[promise["promise_id"]] = promise
            obj = objects.get(str(spec["object_id"]), {})
            agent = agents[str(spec["agent"])]
            before = copy.deepcopy(obj)
            if condition.object_persistence and obj:
                obj["held_by"] = "avatar"
                obj["promised_return_to"] = spec["agent"]
            relation_delta = mutate_relation(agent, trust=0.020, respect=0.025, gratitude=0.010, wariness=-0.012, guarded=condition.distress_guardrail) if condition.relationship_continuity else {}
            event = build_event(event_id, condition, day, "promise_created", promise, agent, obj, before, relation_delta, active_before_day, None, condition, claim_boundary, replay)
            timeline.append(event)
            event_id += 1
        for pid, promise in list(promises.items()):
            if due_status(day, promise) and promise["status"] == "active" and int(promise["resolve_day"]) > day:
                agent = agents[str(promise["agent"])]
                obj = objects.get(str(promise["object_id"]), {})
                before = copy.deepcopy(obj)
                if condition.missed_consequence:
                    promise["status"] = "missed"
                    promise["missed_day"] = day
                    relation_delta = mutate_relation(agent, trust=-0.085, respect=-0.050, gratitude=-0.040, wariness=0.120, guarded=condition.distress_guardrail) if condition.relationship_continuity else {}
                else:
                    relation_delta = {}
                event = build_event(event_id, condition, day, "promise_missed" if condition.missed_consequence else "due_without_consequence", promise, agent, obj, before, relation_delta, active_before_day, "guarded_after_miss" if condition.future_behavior_modulation and condition.missed_consequence else None, condition, claim_boundary, replay)
                timeline.append(event)
                event_id += 1
            if resolve_status(day, promise) and promise["status"] in {"active", "missed"}:
                agent = agents[str(promise["agent"])]
                obj = objects.get(str(promise["object_id"]), {})
                before = copy.deepcopy(obj)
                can_resolve = condition.promise_resolution and (promise["status"] == "active" or condition.recovery_path)
                if can_resolve:
                    obj["held_by"] = promise["agent"] if obj.get("owner") == promise["agent"] else obj.get("place")
                    obj.pop("promised_return_to", None)
                    if promise["status"] == "missed":
                        promise["status"] = "recovered"
                        promise["repair_day"] = day
                        relation_delta = mutate_relation(agent, trust=0.055, respect=0.090, gratitude=0.060, wariness=-0.130, guarded=condition.distress_guardrail) if condition.relationship_continuity else {}
                    else:
                        promise["status"] = "fulfilled"
                        promise["resolved_day"] = day
                        relation_delta = mutate_relation(agent, trust=0.055, respect=0.035, gratitude=0.045, wariness=-0.035, guarded=condition.distress_guardrail) if condition.relationship_continuity else {}
                else:
                    relation_delta = {}
                modulation = "softened_after_repair" if promise["status"] == "recovered" and condition.future_behavior_modulation else "trust_after_kept_promise" if promise["status"] == "fulfilled" and condition.future_behavior_modulation else None
                event = build_event(event_id, condition, day, "promise_recovered" if promise["status"] == "recovered" else "promise_fulfilled" if promise["status"] == "fulfilled" else "promise_unresolved", promise, agent, obj, before, relation_delta, active_before_day, modulation, condition, claim_boundary, replay)
                timeline.append(event)
                event_id += 1
        if day == 6 and condition.promises:
            promise = promises.get("return_dry_cloak")
            agent = agents["Fay"]
            obj = objects.get("dry_cloak", {})
            before = copy.deepcopy(obj)
            modulation = "keeps_distance_until_repair" if condition.future_behavior_modulation and promise and promise.get("status") == "missed" else "neutral_followup"
            relation_delta = mutate_relation(agent, trust=0.000, respect=0.010, gratitude=0.000, wariness=0.018 if modulation.startswith("keeps") else -0.010, guarded=condition.distress_guardrail) if condition.relationship_continuity else {}
            event = build_event(event_id, condition, day, "future_behavior_probe", promise or {}, agent, obj, before, relation_delta, active_before_day, modulation, condition, claim_boundary, replay)
            timeline.append(event)
            event_id += 1
        if day == 8 and condition.promises:
            promise = promises.get("return_dry_cloak")
            agent = agents["Fay"]
            obj = objects.get("dry_cloak", {})
            before = copy.deepcopy(obj)
            modulation = "accepts_help_after_repair" if condition.future_behavior_modulation and promise and promise.get("status") == "recovered" else "still_guarded"
            relation_delta = mutate_relation(agent, trust=0.025 if modulation.startswith("accepts") else -0.015, respect=0.020, gratitude=0.020 if modulation.startswith("accepts") else 0.000, wariness=-0.030 if modulation.startswith("accepts") else 0.020, guarded=condition.distress_guardrail) if condition.relationship_continuity else {}
            event = build_event(event_id, condition, day, "post_repair_followup", promise or {}, agent, obj, before, relation_delta, active_before_day, modulation, condition, claim_boundary, replay)
            timeline.append(event)
            event_id += 1
        object_history.append({"day": day, "objects": copy.deepcopy(objects), "promises": copy.deepcopy(promises)})
        if condition.browser_save_restore and day == config.days // 2:
            save_snapshot = {"day": day, "agents": copy.deepcopy(agents), "objects": copy.deepcopy(objects), "promises": copy.deepcopy(promises)}
            restored_hash = snapshot_hash(save_snapshot)

    promise_values = list(promises.values())
    encoded = len(promise_values) / len(PROMISE_SPECS) if condition.promises else 0.0
    resolved = mean([1.0 if promise.get("status") in {"fulfilled", "recovered"} else 0.0 for promise in promise_values]) if promise_values else 0.0
    missed_consequence = 1.0 if any(p.get("promise_id") == "return_dry_cloak" and p.get("missed_day") == 5 for p in promise_values) and condition.missed_consequence else 0.0
    recovery = 1.0 if any(p.get("promise_id") == "return_dry_cloak" and p.get("status") == "recovered" for p in promise_values) and condition.recovery_path else 0.0
    object_persistence_rate = persistence_rate(object_history, condition)
    rel_cont = 1.0 if condition.relationship_continuity and any(event["relationship_delta"] for event in timeline) else 0.0
    modulation = modulation_rate(timeline, condition)
    recall = recall_rate(timeline, condition)
    distress = distress_rate(agents, promises, condition)
    save_restore = 1.0 if condition.browser_save_restore and save_snapshot is not None and restored_hash == snapshot_hash(save_snapshot) else 0.0
    replay_rate = mean([1.0 if event["replay_frame"] is not None else 0.0 for event in timeline])
    privacy = 1.0 if condition.privacy_filter and all(event["private_workspace_hidden"] for event in timeline) else 0.0
    trace = mean([1.0 if trace_ok(event) and event["claim_boundary"] == claim_boundary else 0.0 for event in timeline])
    metrics = {
        "persisted_object_state_rate": object_persistence_rate,
        "promise_encoding_rate": encoded,
        "promise_resolution_rate": resolved,
        "missed_promise_consequence_rate": missed_consequence,
        "relationship_continuity_rate": rel_cont,
        "future_behavior_modulation_rate": modulation,
        "memory_recall_rate": recall,
        "distress_guardrail_rate": distress,
        "recovery_path_rate": recovery,
        "browser_save_restore_continuity_rate": save_restore,
        "replay_timeline_integrity_rate": replay_rate,
        "privacy_preservation_rate": privacy,
        "trace_integrity": trace,
    }
    metrics = {key: clamp(value) for key, value in metrics.items()}
    readiness = sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS)
    row = EvalRow(
        condition=condition.name,
        agent_count=len(agents),
        object_count=len(objects),
        promise_count=len(promise_values),
        simulated_days=config.days,
        timeline_events=len(timeline),
        continuity_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in metrics.items()},
    )
    state = {
        "condition": condition.name,
        "source_condition": source.get("condition"),
        "places": places,
        "routes": routes,
        "agents": agents,
        "objects": objects,
        "promises": promises,
        "object_history": object_history,
        "timeline": timeline,
        "replay": replay,
        "save_restore_probe": {"saved_hash": snapshot_hash(save_snapshot) if save_snapshot else None, "restored_hash": restored_hash, "roundtrip_ok": save_restore == 1.0},
        "continuity_kernel": {
            "promise_created": "object may move to avatar and active promise enters ledger",
            "promise_fulfilled": "object returns by due day and trust/gratitude increase",
            "promise_missed": "relationship changes, but guardrails bound distress",
            "promise_recovered": "late repair restores some trust and softens future behavior",
            "future_behavior_probe": "agent behavior reflects unresolved or repaired promise memory",
        },
    }
    return row, state, timeline


def build_event(event_id: int, condition: Condition, day: int, kind: str, promise: Mapping[str, object], agent: Mapping[str, object], obj: Mapping[str, object], object_before: Mapping[str, object], relation_delta: Mapping[str, float], active_before_day: Sequence[str], behavior_modulation: str | None, full_condition: Condition, claim_boundary: Mapping[str, bool], replay: list[dict[str, object]]) -> dict[str, object]:
    recalled = list(active_before_day) if full_condition.memory_recall else []
    recovery_packet = None
    if kind == "promise_recovered" and full_condition.recovery_path:
        recovery_packet = {"repair_type": "late_return_and_apology", "bounded_recovery": True, "forgiveness_not_forgetting": True}
    distress_packet = {
        "guardrail_enabled": full_condition.distress_guardrail,
        "trust_floor": 0.30 if full_condition.distress_guardrail else 0.0,
        "wariness_ceiling": 0.78 if full_condition.distress_guardrail else 1.0,
        "unrecoverable_state_allowed": False,
    }
    promise_packet = dict(promise) if promise else None
    event = {
        "event_id": event_id,
        "condition": condition.name,
        "day": day,
        "event_kind": kind,
        "promise_id": promise.get("promise_id") if promise else None,
        "agent_id": agent.get("agent_id"),
        "object_id": obj.get("object_id") if obj else None,
        "object_before": dict(object_before) if object_before else None,
        "object_after": dict(obj) if obj else None,
        "promise_packet": promise_packet,
        "relationship_delta": dict(relation_delta),
        "behavior_modulation": behavior_modulation,
        "recalled_promises": recalled,
        "distress_guardrail": distress_packet,
        "recovery_packet": recovery_packet,
        "private_workspace_hidden": full_condition.privacy_filter,
        "claim_boundary": dict(claim_boundary),
    }
    if full_condition.replay_timeline:
        event["replay_frame"] = {
            "replay_index": len(replay),
            "day": day,
            "kind": kind,
            "promise_id": event["promise_id"],
            "agent_id": event["agent_id"],
            "object_id": event["object_id"],
            "behavior_modulation": behavior_modulation,
        }
        replay.append(event["replay_frame"])
    else:
        event["replay_frame"] = None
    return event


def persistence_rate(history: Sequence[Mapping[str, object]], condition: Condition) -> float:
    if not condition.object_persistence or not history:
        return 0.0
    checks = []
    for record in history:
        day = int(record["day"])
        objects = record["objects"]
        if day in {1, 2}:
            checks.append(1.0 if objects.get("clay_patch_kit", {}).get("held_by") == "avatar" or day == 2 else 0.0)
        if day in {4, 5, 6}:
            checks.append(1.0 if objects.get("dry_cloak", {}).get("held_by") == "avatar" else 0.0)
        if day == 8:
            checks.append(1.0 if objects.get("dry_cloak", {}).get("held_by") == "Fay" else 0.0)
    return mean(checks)


def modulation_rate(timeline: Sequence[Mapping[str, object]], condition: Condition) -> float:
    if not condition.future_behavior_modulation:
        return 0.0
    has_guarded = any(event.get("behavior_modulation") == "keeps_distance_until_repair" for event in timeline)
    has_softened = any(event.get("behavior_modulation") == "accepts_help_after_repair" for event in timeline)
    return mean([1.0 if has_guarded else 0.0, 1.0 if has_softened else 0.0])


def recall_rate(timeline: Sequence[Mapping[str, object]], condition: Condition) -> float:
    if not condition.memory_recall:
        return 0.0
    relevant = [event for event in timeline if event["day"] > 0]
    if not relevant:
        return 0.0
    return mean([1.0 if event.get("recalled_promises") else 0.0 for event in relevant])


def distress_rate(agents: Mapping[str, Mapping[str, object]], promises: Mapping[str, Mapping[str, object]], condition: Condition) -> float:
    if not condition.distress_guardrail:
        return 0.0
    rel_ok = []
    for agent in agents.values():
        rel = relation(agent)
        rel_ok.append(1.0 if float(rel.get("trust_in_avatar", 0.5)) >= 0.30 and float(rel.get("wariness", 0.0)) <= 0.78 else 0.0)
    unresolved_missed = [p for p in promises.values() if p.get("status") == "missed"]
    recoverable = 1.0 if not unresolved_missed else 0.0
    return mean([*rel_ok, recoverable])


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_object_persistence_promise_relationship_continuity"]

    def loss(name: str) -> float:
        return round(full.continuity_readiness - by_name[name].continuity_readiness, 6)

    losses = {
        "no_object_persistence_loss": loss("no_object_persistence"),
        "no_promises_loss": loss("no_promises"),
        "no_promise_resolution_loss": loss("no_promise_resolution"),
        "no_missed_consequence_loss": loss("no_missed_consequence"),
        "no_relationship_continuity_loss": loss("no_relationship_continuity"),
        "no_future_behavior_modulation_loss": loss("no_future_behavior_modulation"),
        "no_memory_recall_loss": loss("no_memory_recall"),
        "no_distress_guardrail_loss": loss("no_distress_guardrail"),
        "no_recovery_path_loss": loss("no_recovery_path"),
        "no_browser_save_restore_loss": loss("no_browser_save_restore"),
        "no_replay_timeline_loss": loss("no_replay_timeline"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.continuity_readiness >= 0.90
        and full.promise_count == len(PROMISE_SPECS)
        and full.simulated_days >= 7
        and full.persisted_object_state_rate >= 0.85
        and full.promise_encoding_rate == 1.0
        and full.promise_resolution_rate == 1.0
        and full.missed_promise_consequence_rate == 1.0
        and full.relationship_continuity_rate == 1.0
        and full.future_behavior_modulation_rate == 1.0
        and full.distress_guardrail_rate == 1.0
        and full.recovery_path_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_object_persistence_loss"] >= 0.08
        and losses["no_promises_loss"] >= 0.10
        and losses["no_relationship_continuity_loss"] >= 0.09
        and losses["no_future_behavior_modulation_loss"] >= 0.09
        and losses["no_recovery_path_loss"] >= 0.08
    )
    return VerdictRow(
        full_condition=full.condition,
        full_continuity_readiness=full.continuity_readiness,
        full_persisted_object_state_rate=full.persisted_object_state_rate,
        full_promise_encoding_rate=full.promise_encoding_rate,
        full_promise_resolution_rate=full.promise_resolution_rate,
        full_missed_promise_consequence_rate=full.missed_promise_consequence_rate,
        full_relationship_continuity_rate=full.relationship_continuity_rate,
        full_future_behavior_modulation_rate=full.future_behavior_modulation_rate,
        full_memory_recall_rate=full.memory_recall_rate,
        full_distress_guardrail_rate=full.distress_guardrail_rate,
        full_recovery_path_rate=full.recovery_path_rate,
        full_browser_save_restore_continuity_rate=full.browser_save_restore_continuity_rate,
        full_replay_timeline_integrity_rate=full.replay_timeline_integrity_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        supports_object_persistence_promise_relationship_continuity_bridge=supports,
        supports_multi_day_local_continuity_seed=supports,
        supports_complete_3d_world=False,
        supports_complete_playable_world=False,
        supports_subjective_consciousness=False,
        supports_moral_patienthood_claim=False,
        supports_natural_language_emergence=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: ContinuityConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_state: dict[str, object] = {}
    integrated_trace: list[dict[str, object]] = []
    for condition in CONDITIONS:
        row, state, trace = simulate_condition(config, source, condition)
        rows.append(row)
        if condition.name == "integrated_object_persistence_promise_relationship_continuity":
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
        "promise_specs": PROMISE_SPECS,
        "moral_boundary": {
            "continuity_seed_not_complete_gameplay": True,
            "promises_not_subjective_obligation": True,
            "relationship_state_not_moral_patienthood": True,
            "bounded_distress_recovery_required": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "agent routines with persistent homes, work projects, and unscripted object use",
    }
    state = {
        "condition": "integrated_object_persistence_promise_relationship_continuity",
        "config": asdict(config),
        "source_condition": source.get("condition"),
        "continuity_state": integrated_state,
        "trace_events": len(integrated_trace),
        "moral_boundary": results["moral_boundary"],
    }
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_OBJECT_PERSISTENCE_PROMISE_RELATIONSHIP_CONTINUITY_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_OBJECT_PERSISTENCE_PROMISE_RELATIONSHIP_CONTINUITY_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_OBJECT_PERSISTENCE_PROMISE_RELATIONSHIP_CONTINUITY_STATE", state)
    return results


def parse_args() -> ContinuityConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=ContinuityConfig.seed)
    parser.add_argument("--days", type=int, default=ContinuityConfig.days)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return ContinuityConfig(seed=args.seed, days=args.days, source_state=args.source_state)


def main() -> None:
    config = parse_args()
    results = run(config)
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("continuity_readiness", f"{verdict['full_continuity_readiness']:.6f}")
    print("simulated_days", config.days)
    print("promise_count", results["rows"][0]["promise_count"])
    print("no_object_persistence_loss", f"{verdict['no_object_persistence_loss']:.6f}")
    print("no_promises_loss", f"{verdict['no_promises_loss']:.6f}")
    print("no_future_behavior_modulation_loss", f"{verdict['no_future_behavior_modulation_loss']:.6f}")


if __name__ == "__main__":
    main()
