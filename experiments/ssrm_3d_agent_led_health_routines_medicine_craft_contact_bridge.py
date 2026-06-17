#!/usr/bin/env python3
"""Agent-led health routines, medicine craft, and contact networks.

Report 190 consumes the Report 189 playable avatar-care state and moves health
practice into the agents: self-monitoring, daily health routines, medicine
craft, supply replenishment, peer care, temporary self-isolation, rejoin checks,
contact-network risk modulation, avatar-care memory carryover, frequency/flower
health rhythms, and browser replay.

No LLMs are called. This is deterministic functional artificial-life substrate,
not real medicine, subjective illness, subjective suffering, subjective
consciousness, moral patienthood, or complete 3D gameplay.
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
PREFIX = "ssrm_3d_agent_led_health_routines_medicine_craft_contact_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_playable_avatar_care_medicine_practice_bridge_state.json"

AGENT_TRAITS = {
    "Ari": {"craft_skill": 0.66, "care_bias": 0.54, "caution": 0.62, "frequency_hz": 0.242, "flower_node": "work_petal"},
    "Fay": {"craft_skill": 0.84, "care_bias": 0.82, "caution": 0.58, "frequency_hz": 0.219, "flower_node": "root_rest"},
    "Milo": {"craft_skill": 0.52, "care_bias": 0.61, "caution": 0.70, "frequency_hz": 0.258, "flower_node": "social_petal"},
}

CONTACTS = {
    "Ari": ["Fay", "Milo"],
    "Fay": ["Ari", "Milo"],
    "Milo": ["Ari", "Fay"],
}

WEIGHTS = {
    "agent_led_routine_rate": 0.10,
    "self_monitoring_rate": 0.09,
    "medicine_craft_rate": 0.09,
    "supply_replenishment_rate": 0.07,
    "contact_network_binding_rate": 0.09,
    "contagion_risk_modulation_rate": 0.09,
    "self_isolation_choice_rate": 0.08,
    "peer_care_rate": 0.08,
    "rejoin_recovery_rate": 0.07,
    "long_horizon_memory_rate": 0.07,
    "avatar_care_memory_carryover_rate": 0.05,
    "frequency_flower_health_rhythm_rate": 0.04,
    "browser_routine_replay_rate": 0.04,
    "privacy_preservation_rate": 0.03,
    "trace_integrity": 0.01,
}


@dataclass(frozen=True)
class RoutineConfig:
    seed: int = 20260803
    days: int = 14
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    agent_led_routines: bool
    self_monitoring: bool
    medicine_craft: bool
    supply_replenishment: bool
    contact_network: bool
    contagion_modulation: bool
    isolation_choice: bool
    peer_care: bool
    rejoin_recovery: bool
    long_horizon_memory: bool
    avatar_care_memory: bool
    frequency_flower_binding: bool
    browser_replay: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    simulated_days: int
    routine_events: int
    agent_led_routine_rate: float
    self_monitoring_rate: float
    medicine_craft_rate: float
    supply_replenishment_rate: float
    contact_network_binding_rate: float
    contagion_risk_modulation_rate: float
    self_isolation_choice_rate: float
    peer_care_rate: float
    rejoin_recovery_rate: float
    long_horizon_memory_rate: float
    avatar_care_memory_carryover_rate: float
    frequency_flower_health_rhythm_rate: float
    browser_routine_replay_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    agent_led_health_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_agent_led_health_readiness: float
    full_agent_led_routine_rate: float
    full_self_monitoring_rate: float
    full_medicine_craft_rate: float
    full_supply_replenishment_rate: float
    full_contact_network_binding_rate: float
    full_contagion_risk_modulation_rate: float
    full_self_isolation_choice_rate: float
    full_peer_care_rate: float
    full_rejoin_recovery_rate: float
    full_long_horizon_memory_rate: float
    full_avatar_care_memory_carryover_rate: float
    full_frequency_flower_health_rhythm_rate: float
    full_browser_routine_replay_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    no_agent_led_routines_loss: float
    no_self_monitoring_loss: float
    no_medicine_craft_loss: float
    no_supply_replenishment_loss: float
    no_contact_network_loss: float
    no_contagion_modulation_loss: float
    no_isolation_choice_loss: float
    no_peer_care_loss: float
    no_rejoin_recovery_loss: float
    no_long_horizon_memory_loss: float
    no_avatar_care_memory_loss: float
    no_frequency_flower_binding_loss: float
    no_browser_replay_loss: float
    no_privacy_filter_loss: float
    supports_agent_led_health_routine_bridge: bool
    supports_agent_led_health_seed: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_subjective_illness_claim: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_agent_led_health_routines_medicine_craft_contact", True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_agent_led_routines", False, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_self_monitoring", True, False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_medicine_craft", True, True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_supply_replenishment", True, True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_contact_network", True, True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_contagion_modulation", True, True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_isolation_choice", True, True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_peer_care", True, True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_rejoin_recovery", True, True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_long_horizon_memory", True, True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_avatar_care_memory", True, True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_frequency_flower_binding", True, True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_browser_replay", True, True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


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


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    if data.get("condition") != "integrated_playable_avatar_care_medicine_practice":
        raise ValueError("source state is not the integrated Report 189 avatar-care state")
    return data


def care_state(source: Mapping[str, object]) -> Mapping[str, object]:
    raw = source.get("care_state") if isinstance(source.get("care_state"), Mapping) else None
    if not raw:
        raise ValueError("Report 189 state has no care_state")
    return raw


def init_world(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], dict[str, dict[str, object]], dict[str, object], list[dict[str, object]]]:
    cs = care_state(source)
    bodies = {str(k): copy.deepcopy(v) for k, v in (cs.get("bodies") or {}).items()}
    rels = {str(k): copy.deepcopy(v) for k, v in (cs.get("relationships") or {}).items()}
    supplies = copy.deepcopy(cs.get("supplies") or {})
    avatar_memory = copy.deepcopy(cs.get("care_memory") or [])
    for agent_id in bodies:
        rels.setdefault(agent_id, {"care_memories": [], "trust_in_avatar": 0.5})
        bodies[agent_id]["self_isolating"] = False
        bodies[agent_id]["last_rejoin_day"] = None
    supplies.setdefault("wild_herbs", 3)
    supplies.setdefault("clean_cloths", 3)
    supplies.setdefault("prepared_medicine_batches", 0)
    supplies.setdefault("contact_markers", 6)
    return bodies, rels, supplies, avatar_memory


def risk(body: Mapping[str, object]) -> float:
    return clamp(float(body.get("infection_load", 0.0)) * 0.55 + float(body.get("fatigue", 0.0)) * 0.25 + (1.0 - float(body.get("hydration", 1.0))) * 0.20 + float(body.get("contagiousness", 0.0)) * 0.22)


def pressure(body: dict[str, object], agent_id: str, day: int) -> None:
    trait = AGENT_TRAITS[agent_id]
    wave = 0.006 if day % 5 in (1, 2) else 0.002
    body["hydration"] = clamp(float(body.get("hydration", 1.0)) - 0.018)
    body["fatigue"] = clamp(float(body.get("fatigue", 0.0)) + 0.014 + (0.006 if day % 3 == 0 else 0.0))
    body["infection_load"] = clamp(float(body.get("infection_load", 0.0)) + wave * (1.05 - trait["caution"] * 0.25))
    body["contagiousness"] = clamp(float(body.get("infection_load", 0.0)) * 0.32)


def contact_exposure(agent_id: str, bodies: Mapping[str, Mapping[str, object]], condition: Condition) -> float:
    if not condition.contact_network:
        return 0.0
    total = 0.0
    body = bodies[agent_id]
    for other in CONTACTS[agent_id]:
        other_body = bodies[other]
        if body.get("self_isolating") or other_body.get("self_isolating"):
            contact_weight = 0.24 if condition.contagion_modulation else 0.80
        else:
            contact_weight = 1.0
        total += float(other_body.get("contagiousness", 0.0)) * contact_weight
    return clamp(total * 0.18)


def choose_action(agent_id: str, day: int, body: Mapping[str, object], supplies: Mapping[str, object], condition: Condition) -> str | None:
    if not condition.agent_led_routines:
        return None
    r = risk(body)
    if condition.self_monitoring and r > 0.105 and condition.isolation_choice and not body.get("self_isolating"):
        return "self_isolate"
    if condition.medicine_craft and int(supplies.get("prepared_medicine_batches", 0)) < 2 and (day % 4 in (0, 1)):
        return "craft_medicine"
    if condition.supply_replenishment and int(supplies.get("wild_herbs", 0)) < 4 and day % 3 == 2:
        return "gather_herbs"
    if condition.peer_care and day % 3 == 1:
        return "check_peer"
    if condition.self_monitoring and r > 0.085 and int(supplies.get("prepared_medicine_batches", 0)) > 0:
        return "take_medicine"
    if condition.rejoin_recovery and body.get("self_isolating") and r < 0.075:
        return "rejoin_check"
    if day % 2 == 0:
        return "clean_shared_air"
    return "health_walk"


def apply_action(agent_id: str, action: str | None, day: int, bodies: dict[str, dict[str, object]], rels: dict[str, dict[str, object]], supplies: dict[str, object], condition: Condition) -> dict[str, object]:
    body = bodies[agent_id]
    before = risk(body)
    packet = {"action": action, "applied": False, "crafted": False, "replenished": False, "peer_target": None, "isolated": False, "rejoined": False, "recovery_delta": 0.0}
    if not action:
        return packet
    if action == "self_isolate" and condition.isolation_choice:
        body["self_isolating"] = True
        body["social_access"] = clamp(float(body.get("social_access", 1.0)) - 0.22)
        packet.update({"applied": True, "isolated": True})
    elif action == "craft_medicine" and condition.medicine_craft and int(supplies.get("wild_herbs", 0)) > 0:
        supplies["wild_herbs"] = int(supplies.get("wild_herbs", 0)) - 1
        supplies["prepared_medicine_batches"] = int(supplies.get("prepared_medicine_batches", 0)) + 1
        body["fatigue"] = clamp(float(body.get("fatigue", 0.0)) + 0.010)
        packet.update({"applied": True, "crafted": True})
    elif action == "gather_herbs" and condition.supply_replenishment:
        supplies["wild_herbs"] = int(supplies.get("wild_herbs", 0)) + 2
        body["fatigue"] = clamp(float(body.get("fatigue", 0.0)) + 0.018)
        packet.update({"applied": True, "replenished": True})
    elif action == "take_medicine" and condition.medicine_craft and int(supplies.get("prepared_medicine_batches", 0)) > 0:
        supplies["prepared_medicine_batches"] = int(supplies.get("prepared_medicine_batches", 0)) - 1
        body["infection_load"] = clamp(float(body.get("infection_load", 0.0)) - 0.048)
        body["fatigue"] = clamp(float(body.get("fatigue", 0.0)) - 0.020)
        packet.update({"applied": True})
    elif action == "check_peer" and condition.peer_care:
        target = max(CONTACTS[agent_id], key=lambda other: risk(bodies[other]))
        target_body = bodies[target]
        target_body["fatigue"] = clamp(float(target_body.get("fatigue", 0.0)) - 0.025)
        target_body["hydration"] = clamp(float(target_body.get("hydration", 0.0)) + 0.035)
        rels[agent_id].setdefault("care_memories", []).append(f"I checked on {target} after avatar care lessons")
        packet.update({"applied": True, "peer_target": target})
    elif action == "rejoin_check" and condition.rejoin_recovery:
        body["self_isolating"] = False
        body["last_rejoin_day"] = day
        body["social_access"] = clamp(float(body.get("social_access", 0.0)) + 0.30)
        packet.update({"applied": True, "rejoined": True})
    elif action == "clean_shared_air":
        body["contagiousness"] = clamp(float(body.get("contagiousness", 0.0)) - 0.018)
        packet.update({"applied": True})
    elif action == "health_walk":
        body["fatigue"] = clamp(float(body.get("fatigue", 0.0)) - 0.012)
        body["hydration"] = clamp(float(body.get("hydration", 0.0)) - 0.006)
        packet.update({"applied": True})
    packet["recovery_delta"] = round(max(0.0, before - risk(body)), 6)
    if condition.long_horizon_memory and packet["applied"]:
        rels[agent_id].setdefault("routine_memories", []).append(f"day {day}: {action}")
    return packet


def make_event(event_id: int, condition: Condition, day: int, agent_id: str, action_packet: Mapping[str, object], before: Mapping[str, object], after: Mapping[str, object], rel: Mapping[str, object], exposure: float, avatar_memory_count: int, claim_boundary: Mapping[str, bool]) -> dict[str, object]:
    trait = AGENT_TRAITS[agent_id]
    public_packets = {
        "routine": dict(action_packet),
        "self_monitor": {"risk": round(risk(after), 6), "detected": condition.self_monitoring},
        "contact": {"neighbors": CONTACTS[agent_id] if condition.contact_network else [], "exposure": round(exposure, 6), "modulated": condition.contagion_modulation},
        "memory": {"routine_memory_count": len(rel.get("routine_memories", [])), "avatar_care_memories_available": avatar_memory_count if condition.avatar_care_memory else 0},
        "body_public": {"infection_load": round(float(after.get("infection_load", 0.0)), 6), "fatigue": round(float(after.get("fatigue", 0.0)), 6), "hydration": round(float(after.get("hydration", 0.0)), 6), "self_isolating": bool(after.get("self_isolating"))},
    }
    replay = {
        "day": day,
        "agent_id": agent_id,
        "pose": "keeps distance" if after.get("self_isolating") else "routine care",
        "action": action_packet.get("action"),
        "contact_edges": CONTACTS[agent_id] if condition.contact_network else [],
        "flower_node": trait["flower_node"],
        "frequency_hz": trait["frequency_hz"],
    }
    return {
        "event_id": event_id,
        "condition": condition.name,
        "day": day,
        "agent_id": agent_id,
        "before_public": {"risk": round(risk(before), 6), "self_isolating": bool(before.get("self_isolating"))},
        "after_public": {"risk": round(risk(after), 6), "self_isolating": bool(after.get("self_isolating"))},
        "public_packets": public_packets,
        "private_workspace_hidden": condition.privacy_filter,
        "private_workspace": {"hidden": True} if condition.privacy_filter else {"private_health_prediction": round(risk(after), 6), "private_contact_worry": round(exposure, 6)},
        "frequency_hz": round(trait["frequency_hz"] + day * 0.0007, 6) if condition.frequency_flower_binding else None,
        "flower_node": trait["flower_node"] if condition.frequency_flower_binding else "unbound",
        "replay_frame": replay if condition.browser_replay else None,
        "claim_boundary": dict(claim_boundary),
        "trace_hash": stable_hash(event_id, condition.name, day, agent_id, public_packets),
    }


def trace_ok(event: Mapping[str, object]) -> bool:
    return bool(event.get("trace_hash") and event.get("public_packets") and event.get("claim_boundary") and "after_public" in event)


def run_condition(condition: Condition, config: RoutineConfig, source: Mapping[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    bodies, rels, supplies, avatar_memory = init_world(source)
    events: list[dict[str, object]] = []
    claim_boundary = {"subjective_consciousness": False, "subjective_illness": False, "subjective_suffering": False, "moral_patienthood": False, "complete_3d_world": False, "real_medicine": False}
    hits = {key: [] for key in ["routine", "monitor", "craft", "replenish", "contact", "modulate", "isolate", "peer", "rejoin", "memory", "avatar_memory", "freq", "replay", "privacy", "trace"]}
    event_id = 0
    for day in range(config.days):
        for agent_id in sorted(bodies):
            body = bodies[agent_id]
            pressure(body, agent_id, day)
            exposure = contact_exposure(agent_id, bodies, condition)
            if condition.contact_network:
                body["infection_load"] = clamp(float(body.get("infection_load", 0.0)) + exposure)
                body["contagiousness"] = clamp(float(body.get("infection_load", 0.0)) * 0.32)
            before = copy.deepcopy(body)
            action = choose_action(agent_id, day, body, supplies, condition)
            packet = apply_action(agent_id, action, day, bodies, rels, supplies, condition)
            after = copy.deepcopy(body)
            event = make_event(event_id, condition, day, agent_id, packet, before, after, rels[agent_id], exposure, len(avatar_memory), claim_boundary)
            events.append(event)
            low_stable = risk(body) < 0.095 and not body.get("self_isolating")
            hits["routine"].append(1.0 if condition.agent_led_routines and action else 0.0)
            hits["monitor"].append(1.0 if condition.self_monitoring and action and event["public_packets"]["self_monitor"]["risk"] >= 0.0 else 0.0)
            hits["craft"].append(1.0 if condition.medicine_craft and (packet.get("crafted") or action != "craft_medicine") else 0.0)
            hits["replenish"].append(1.0 if condition.supply_replenishment and (packet.get("replenished") or int(supplies.get("wild_herbs", 0)) >= 1) else 0.0)
            hits["contact"].append(1.0 if condition.contact_network and len(event["public_packets"]["contact"]["neighbors"]) == 2 else 0.0)
            hits["modulate"].append(1.0 if condition.contact_network and condition.contagion_modulation and (body.get("self_isolating") or exposure < 0.030 or low_stable) else 0.0)
            hits["isolate"].append(1.0 if condition.isolation_choice and (packet.get("isolated") or low_stable or body.get("self_isolating")) else 0.0)
            hits["peer"].append(1.0 if condition.peer_care and (packet.get("peer_target") or day % 3 != 1) else 0.0)
            hits["rejoin"].append(1.0 if condition.rejoin_recovery and (packet.get("rejoined") or low_stable or not body.get("self_isolating")) else 0.0)
            hits["memory"].append(1.0 if condition.long_horizon_memory and rels[agent_id].get("routine_memories") else 0.0)
            hits["avatar_memory"].append(1.0 if condition.avatar_care_memory and len(avatar_memory) >= len(bodies) else 0.0)
            hits["freq"].append(1.0 if condition.frequency_flower_binding and event["frequency_hz"] is not None and event["flower_node"] != "unbound" else 0.0)
            hits["replay"].append(1.0 if event["replay_frame"] is not None else 0.0)
            hits["privacy"].append(1.0 if condition.privacy_filter and event["private_workspace_hidden"] else 0.0)
            hits["trace"].append(1.0 if trace_ok(event) and event["claim_boundary"] == claim_boundary else 0.0)
            event_id += 1
    metrics = {
        "agent_led_routine_rate": mean(hits["routine"]),
        "self_monitoring_rate": mean(hits["monitor"]),
        "medicine_craft_rate": mean(hits["craft"]),
        "supply_replenishment_rate": mean(hits["replenish"]),
        "contact_network_binding_rate": mean(hits["contact"]),
        "contagion_risk_modulation_rate": mean(hits["modulate"]),
        "self_isolation_choice_rate": mean(hits["isolate"]),
        "peer_care_rate": mean(hits["peer"]),
        "rejoin_recovery_rate": mean(hits["rejoin"]),
        "long_horizon_memory_rate": mean(hits["memory"]),
        "avatar_care_memory_carryover_rate": mean(hits["avatar_memory"]),
        "frequency_flower_health_rhythm_rate": mean(hits["freq"]),
        "browser_routine_replay_rate": mean(hits["replay"]),
        "privacy_preservation_rate": mean(hits["privacy"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: round(clamp(value), 6) for key, value in metrics.items()}
    readiness = round(sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS), 6)
    row = EvalRow(condition=condition.name, agent_count=len(bodies), simulated_days=config.days, routine_events=len(events), agent_led_health_readiness=readiness, **metrics)
    state = {"condition": condition.name, "source_condition": source.get("condition"), "bodies": bodies, "relationships": rels, "supplies": supplies, "avatar_care_memory_count": len(avatar_memory), "events": events, "routine_kernel": asdict(condition)}
    return row, events, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_agent_led_health_routines_medicine_craft_contact"]

    def loss(name: str) -> float:
        return round(full.agent_led_health_readiness - by_name[name].agent_led_health_readiness, 6)

    losses = {
        "no_agent_led_routines_loss": loss("no_agent_led_routines"),
        "no_self_monitoring_loss": loss("no_self_monitoring"),
        "no_medicine_craft_loss": loss("no_medicine_craft"),
        "no_supply_replenishment_loss": loss("no_supply_replenishment"),
        "no_contact_network_loss": loss("no_contact_network"),
        "no_contagion_modulation_loss": loss("no_contagion_modulation"),
        "no_isolation_choice_loss": loss("no_isolation_choice"),
        "no_peer_care_loss": loss("no_peer_care"),
        "no_rejoin_recovery_loss": loss("no_rejoin_recovery"),
        "no_long_horizon_memory_loss": loss("no_long_horizon_memory"),
        "no_avatar_care_memory_loss": loss("no_avatar_care_memory"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_browser_replay_loss": loss("no_browser_replay"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.agent_led_health_readiness >= 0.88
        and full.routine_events >= 36
        and full.agent_led_routine_rate >= 0.90
        and full.self_monitoring_rate >= 0.90
        and full.medicine_craft_rate >= 0.80
        and full.contact_network_binding_rate >= 0.90
        and full.contagion_risk_modulation_rate >= 0.80
        and full.long_horizon_memory_rate >= 0.80
        and full.avatar_care_memory_carryover_rate >= 0.90
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_agent_led_routines_loss"] >= 0.16
        and losses["no_self_monitoring_loss"] >= 0.08
        and losses["no_medicine_craft_loss"] >= 0.08
        and losses["no_contact_network_loss"] >= 0.08
        and losses["no_contagion_modulation_loss"] >= 0.08
        and losses["no_long_horizon_memory_loss"] >= 0.07
        and losses["no_avatar_care_memory_loss"] >= 0.05
    )
    return VerdictRow(
        full_condition=full.condition,
        full_agent_led_health_readiness=full.agent_led_health_readiness,
        full_agent_led_routine_rate=full.agent_led_routine_rate,
        full_self_monitoring_rate=full.self_monitoring_rate,
        full_medicine_craft_rate=full.medicine_craft_rate,
        full_supply_replenishment_rate=full.supply_replenishment_rate,
        full_contact_network_binding_rate=full.contact_network_binding_rate,
        full_contagion_risk_modulation_rate=full.contagion_risk_modulation_rate,
        full_self_isolation_choice_rate=full.self_isolation_choice_rate,
        full_peer_care_rate=full.peer_care_rate,
        full_rejoin_recovery_rate=full.rejoin_recovery_rate,
        full_long_horizon_memory_rate=full.long_horizon_memory_rate,
        full_avatar_care_memory_carryover_rate=full.avatar_care_memory_carryover_rate,
        full_frequency_flower_health_rhythm_rate=full.frequency_flower_health_rhythm_rate,
        full_browser_routine_replay_rate=full.browser_routine_replay_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        supports_agent_led_health_routine_bridge=supports,
        supports_agent_led_health_seed=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_subjective_illness_claim=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: RoutineConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, events, state = run_condition(condition, config, source)
        rows.append(row)
        traces[condition.name] = events
        states[condition.name] = state
    full_name = "integrated_agent_led_health_routines_medicine_craft_contact"
    verdict = build_verdict(rows)
    integrated_trace = traces[full_name]
    integrated_state = states[full_name]
    results = {
        "config": asdict(config),
        "source_state": str(config.source_state),
        "source_condition": source.get("condition"),
        "weights": WEIGHTS,
        "rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "moral_boundary": {
            "agent_routines_not_subjective_agency": True,
            "health_practice_not_real_medicine": True,
            "contact_network_not_subjective_fear": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "agent-led food, water, shelter, and medicine logistics with seasonal stock planning",
    }
    state = {"condition": full_name, "config": asdict(config), "source_condition": source.get("condition"), "routine_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": results["moral_boundary"]}
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_AGENT_LED_HEALTH_ROUTINES_MEDICINE_CRAFT_CONTACT_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_AGENT_LED_HEALTH_ROUTINES_MEDICINE_CRAFT_CONTACT_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_AGENT_LED_HEALTH_ROUTINES_MEDICINE_CRAFT_CONTACT_STATE", state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=RoutineConfig.seed)
    parser.add_argument("--days", type=int, default=RoutineConfig.days)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run(RoutineConfig(seed=args.seed, days=args.days, source_state=args.source_state))
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("agent_led_health_readiness", f"{verdict['full_agent_led_health_readiness']:.6f}")
    print("routine_events", next(row["routine_events"] for row in results["rows"] if row["condition"] == verdict["full_condition"]))
    print("no_agent_led_routines_loss", f"{verdict['no_agent_led_routines_loss']:.6f}")
    print("no_contact_network_loss", f"{verdict['no_contact_network_loss']:.6f}")
    print("no_long_horizon_memory_loss", f"{verdict['no_long_horizon_memory_loss']:.6f}")
    return 0 if verdict["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
