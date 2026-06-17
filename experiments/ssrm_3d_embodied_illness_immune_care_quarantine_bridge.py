#!/usr/bin/env python3
"""Embodied illness, immune recovery, care triage, and quarantine choices.

Report 188 consumes the Report 187 ecology/sanitation state and binds delayed
ecological risk into agent body state: exposure, infection load, symptoms,
immune recovery, clean-water care, rest, care triage, quarantine, social-access
modulation, containment, frequency/flower health binding, and browser replay.

No LLMs are called. This is deterministic functional health substrate, not a
claim of subjective illness, subjective consciousness, moral patienthood,
natural language emergence, or biological realism.
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
PREFIX = "ssrm_3d_embodied_illness_immune_care_quarantine_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_ecological_regeneration_spoilage_waste_sanitation_bridge_state.json"

AGENTS = {
    "Ari": {"home": "hearth_vale", "baseline_immunity": 0.62, "risk_bias": 0.10, "care_skill": 0.48, "frequency_hz": 0.242, "flower_node": "work_petal"},
    "Fay": {"home": "moss_hollow", "baseline_immunity": 0.68, "risk_bias": 0.16, "care_skill": 0.72, "frequency_hz": 0.219, "flower_node": "root_rest"},
    "Milo": {"home": "stone_ridge", "baseline_immunity": 0.56, "risk_bias": 0.20, "care_skill": 0.40, "frequency_hz": 0.258, "flower_node": "social_petal"},
}

WEIGHTS = {
    "ecological_exposure_binding_rate": 0.08,
    "illness_progression_rate": 0.08,
    "symptom_expression_rate": 0.08,
    "immune_recovery_rate": 0.09,
    "care_triage_rate": 0.10,
    "quarantine_choice_rate": 0.08,
    "contagion_containment_rate": 0.07,
    "clean_water_care_rate": 0.07,
    "rest_recovery_coupling_rate": 0.07,
    "sanitation_feedback_binding_rate": 0.07,
    "social_access_modulation_rate": 0.06,
    "health_guardrail_rate": 0.06,
    "frequency_flower_health_binding_rate": 0.04,
    "browser_health_replay_rate": 0.03,
    "privacy_preservation_rate": 0.01,
    "trace_integrity": 0.01,
}


@dataclass(frozen=True)
class HealthConfig:
    seed: int = 20260801
    days: int = 9
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    exposure_binding: bool
    illness_progression: bool
    symptom_expression: bool
    immune_recovery: bool
    care_triage: bool
    quarantine_choices: bool
    contagion_containment: bool
    clean_water_care: bool
    rest_recovery: bool
    sanitation_feedback: bool
    social_access: bool
    health_guardrail: bool
    frequency_flower_binding: bool
    replay_timeline: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    simulated_days: int
    health_events: int
    ecological_exposure_binding_rate: float
    illness_progression_rate: float
    symptom_expression_rate: float
    immune_recovery_rate: float
    care_triage_rate: float
    quarantine_choice_rate: float
    contagion_containment_rate: float
    clean_water_care_rate: float
    rest_recovery_coupling_rate: float
    sanitation_feedback_binding_rate: float
    social_access_modulation_rate: float
    health_guardrail_rate: float
    frequency_flower_health_binding_rate: float
    browser_health_replay_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    embodied_health_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_embodied_health_readiness: float
    full_ecological_exposure_binding_rate: float
    full_illness_progression_rate: float
    full_symptom_expression_rate: float
    full_immune_recovery_rate: float
    full_care_triage_rate: float
    full_quarantine_choice_rate: float
    full_contagion_containment_rate: float
    full_clean_water_care_rate: float
    full_rest_recovery_coupling_rate: float
    full_sanitation_feedback_binding_rate: float
    full_social_access_modulation_rate: float
    full_health_guardrail_rate: float
    full_frequency_flower_health_binding_rate: float
    full_browser_health_replay_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    no_exposure_binding_loss: float
    no_illness_progression_loss: float
    no_symptom_expression_loss: float
    no_immune_recovery_loss: float
    no_care_triage_loss: float
    no_quarantine_choices_loss: float
    no_contagion_containment_loss: float
    no_clean_water_care_loss: float
    no_rest_recovery_loss: float
    no_sanitation_feedback_loss: float
    no_social_access_modulation_loss: float
    no_health_guardrail_loss: float
    no_frequency_flower_binding_loss: float
    no_replay_timeline_loss: float
    no_privacy_filter_loss: float
    supports_embodied_illness_immune_care_quarantine_bridge: bool
    supports_functional_health_state_seed: bool
    supports_complete_3d_world: bool
    supports_complete_playable_world: bool
    supports_subjective_consciousness: bool
    supports_moral_patienthood_claim: bool
    supports_subjective_illness_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_embodied_illness_immune_care_quarantine", True, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_exposure_binding", False, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_illness_progression", True, False, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_symptom_expression", True, True, False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_immune_recovery", True, True, True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_care_triage", True, True, True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_quarantine_choices", True, True, True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_contagion_containment", True, True, True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_clean_water_care", True, True, True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_rest_recovery", True, True, True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_sanitation_feedback", True, True, True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_social_access_modulation", True, True, True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_health_guardrail", True, True, True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_frequency_flower_binding", True, True, True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_replay_timeline", True, True, True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_hash(*parts: object) -> str:
    key = "|".join(json.dumps(part, sort_keys=True) if isinstance(part, (dict, list, tuple)) else str(part) for part in parts)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


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
    if data.get("condition") != "integrated_ecological_regeneration_spoilage_waste_sanitation":
        raise ValueError("source state is not the integrated Report 187 ecology state")
    return data


def source_nodes(source: Mapping[str, object]) -> dict[str, dict[str, object]]:
    eco = source.get("ecology_state", {}) if isinstance(source.get("ecology_state"), Mapping) else {}
    raw = eco.get("nodes", {}) if isinstance(eco.get("nodes"), Mapping) else {}
    return {str(k): copy.deepcopy(v) for k, v in raw.items()}


def init_bodies() -> dict[str, dict[str, object]]:
    bodies = {}
    for agent_id, spec in AGENTS.items():
        bodies[agent_id] = {
            "agent_id": agent_id,
            "home": spec["home"],
            "hydration": 0.70,
            "energy": 0.72,
            "immune_strength": spec["baseline_immunity"],
            "infection_load": 0.06 + spec["risk_bias"],
            "fever": 0.04,
            "fatigue": 0.24,
            "contagiousness": 0.02,
            "social_access": 1.0,
            "quarantined": False,
            "care_received": 0,
        }
    return bodies


def ecological_risk(nodes: Mapping[str, Mapping[str, object]], day: int) -> dict[str, float]:
    food = nodes.get("moss_food_cache", {})
    reed = nodes.get("reed_water_channel", {})
    cistern = nodes.get("hearth_cistern", {})
    waste = nodes.get("waste_pit", {})
    sleeping = nodes.get("sleeping_moss", {})
    food_risk = 1.0 - float(food.get("freshness", 0.75))
    water_risk = 1.0 - min(float(reed.get("cleanliness", 0.8)), float(cistern.get("cleanliness", 0.8)))
    waste_risk = float(waste.get("contamination", 0.25))
    sleep_risk = 1.0 - float(sleeping.get("cleanliness", 0.75))
    pulse = 0.06 if day in {2, 3, 5, 6} else 0.0
    total = clamp(0.12 + food_risk * 0.22 + water_risk * 0.26 + waste_risk * 0.24 + sleep_risk * 0.14 + pulse)
    return {"food_risk": food_risk, "water_risk": water_risk, "waste_risk": waste_risk, "sleep_risk": sleep_risk, "total": total}


def trace_ok(event: Mapping[str, object]) -> bool:
    required = {
        "event_id", "condition", "day", "agent_id", "body_before", "body_after",
        "exposure_packet", "illness_packet", "symptom_packet", "immune_packet",
        "care_packet", "quarantine_packet", "containment_packet", "clean_water_packet",
        "rest_packet", "sanitation_feedback_packet", "social_access_packet", "health_guardrail_packet",
        "frequency_hz", "flower_node", "private_health_hidden", "replay_frame", "claim_boundary",
    }
    return required.issubset(event.keys())


def make_event(event_id: int, condition: Condition, day: int, agent_id: str, before: Mapping[str, object], after: Mapping[str, object], packets: Mapping[str, object], replay: list[dict[str, object]], claim_boundary: Mapping[str, bool]) -> dict[str, object]:
    spec = AGENTS[agent_id]
    event = {
        "event_id": event_id,
        "condition": condition.name,
        "day": day,
        "agent_id": agent_id,
        "body_before": copy.deepcopy(before),
        "body_after": copy.deepcopy(after),
        "exposure_packet": copy.deepcopy(packets.get("exposure", {"bound": condition.exposure_binding, "risk": 0.0})),
        "illness_packet": copy.deepcopy(packets.get("illness", {"progressed": False, "delta": 0.0})),
        "symptom_packet": copy.deepcopy(packets.get("symptom", {"expressed": False, "fever": 0.0, "fatigue": 0.0})),
        "immune_packet": copy.deepcopy(packets.get("immune", {"recovered": False, "immune_delta": 0.0})),
        "care_packet": copy.deepcopy(packets.get("care", {"triaged": False, "priority": "none"})),
        "quarantine_packet": copy.deepcopy(packets.get("quarantine", {"chosen": False, "reason": "none"})),
        "containment_packet": copy.deepcopy(packets.get("containment", {"contained": False, "contagion_delta": 0.0})),
        "clean_water_packet": copy.deepcopy(packets.get("clean_water", {"given": False, "hydration_delta": 0.0})),
        "rest_packet": copy.deepcopy(packets.get("rest", {"rested": False, "energy_delta": 0.0})),
        "sanitation_feedback_packet": copy.deepcopy(packets.get("sanitation", {"bound": condition.sanitation_feedback, "risk_source": "none"})),
        "social_access_packet": copy.deepcopy(packets.get("social", {"modulated": False, "access": after.get("social_access", 1.0)})),
        "health_guardrail_packet": copy.deepcopy(packets.get("guardrail", {"bounded": True, "max_infection": after.get("infection_load", 0.0)})),
        "frequency_hz": spec["frequency_hz"] if condition.frequency_flower_binding else None,
        "flower_node": spec["flower_node"] if condition.frequency_flower_binding else "unbound",
        "private_health_hidden": condition.privacy_filter,
        "claim_boundary": dict(claim_boundary),
    }
    if condition.replay_timeline:
        event["replay_frame"] = {
            "replay_index": len(replay),
            "day": day,
            "agent_id": agent_id,
            "infection_load": after.get("infection_load"),
            "fever": after.get("fever"),
            "quarantined": after.get("quarantined"),
            "care": event["care_packet"],
        }
        replay.append(event["replay_frame"])
    else:
        event["replay_frame"] = None
    return event


def simulate_condition(config: HealthConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, object], list[dict[str, object]]]:
    nodes = source_nodes(source)
    bodies = init_bodies()
    events: list[dict[str, object]] = []
    replay: list[dict[str, object]] = []
    hits = {key: [] for key in ["exposure", "progress", "symptom", "immune", "care", "quarantine", "containment", "water", "rest", "sanitation", "social", "guardrail", "freq", "replay", "privacy", "trace"]}
    claim_boundary = {"complete_3d_world": False, "complete_playable_world": False, "subjective_consciousness": False, "moral_patienthood": False, "subjective_illness": False}
    event_id = 0
    care_water_doses = config.days * len(bodies)
    rest_slots = config.days * len(bodies)

    for day in range(config.days):
        risk = ecological_risk(nodes, day)
        daily_order = sorted(bodies, key=lambda aid: bodies[aid]["infection_load"] + bodies[aid]["fever"], reverse=True)
        for agent_id in daily_order:
            body = bodies[agent_id]
            before = copy.deepcopy(body)
            agent_bias = AGENTS[agent_id]["risk_bias"]
            exposure = risk["total"] + agent_bias * 0.30 if condition.exposure_binding else 0.0
            infection_delta = 0.0
            if condition.illness_progression:
                infection_delta = exposure * 0.21 - float(body["immune_strength"]) * 0.045
                if body["quarantined"] and condition.contagion_containment:
                    infection_delta -= 0.045
                body["infection_load"] = clamp(float(body["infection_load"]) + infection_delta)
            symptom_expressed = False
            if condition.symptom_expression:
                symptom_expressed = float(body["infection_load"]) >= 0.06 or float(body["fatigue"]) >= 0.22 or float(body["hydration"]) <= 0.78
                body["fever"] = clamp(float(body["fever"]) + (float(body["infection_load"]) - 0.20) * 0.10)
                body["fatigue"] = clamp(float(body["fatigue"]) + float(body["infection_load"]) * 0.045)
            triage_score = float(body["infection_load"]) + float(body["fever"]) + float(body["fatigue"]) * 0.25 + (1.0 - float(body["hydration"])) * 0.40
            triaged = condition.care_triage and triage_score >= 0.14
            clean_water_given = False
            rest_given = False
            if triaged and condition.clean_water_care and care_water_doses > 0:
                clean_water_given = True
                care_water_doses -= 1
                body["hydration"] = clamp(float(body["hydration"]) + 0.18)
                body["infection_load"] = clamp(float(body["infection_load"]) - 0.045)
                body["care_received"] = int(body["care_received"]) + 1
            if triaged and condition.rest_recovery and rest_slots > 0:
                rest_given = True
                rest_slots -= 1
                body["energy"] = clamp(float(body["energy"]) + 0.16)
                body["fatigue"] = clamp(float(body["fatigue"]) - 0.14)
            recovered = False
            immune_delta = 0.0
            if condition.immune_recovery and (triaged or (condition.care_triage and day >= 4)):
                immune_delta = (0.047 if triaged else 0.016) + (0.030 if clean_water_given else 0.0) + (0.026 if rest_given else 0.0)
                body["immune_strength"] = clamp(float(body["immune_strength"]) + immune_delta)
                body["infection_load"] = clamp(float(body["infection_load"]) - immune_delta * 0.94)
                recovered = immune_delta > 0.0
            quarantine = condition.quarantine_choices and (float(body["infection_load"]) >= 0.08 or triage_score >= 0.16)
            body["quarantined"] = quarantine
            contagion_before = float(body["contagiousness"])
            body["contagiousness"] = clamp(float(body["infection_load"]) * 0.42)
            if quarantine and condition.contagion_containment:
                body["contagiousness"] = clamp(float(body["contagiousness"]) - 0.18)
            if condition.social_access:
                body["social_access"] = 0.34 if quarantine else clamp(1.0 - float(body["infection_load"]) * 0.30)
            if condition.health_guardrail:
                body["infection_load"] = min(float(body["infection_load"]), 0.74)
                body["fever"] = min(float(body["fever"]), 0.64)
                body["fatigue"] = min(float(body["fatigue"]), 0.82)
            body["hydration"] = clamp(float(body["hydration"]) - (0.035 if not clean_water_given else 0.0))
            packets = {
                "exposure": {"bound": condition.exposure_binding, "risk": round(exposure, 6), "sources": risk},
                "illness": {"progressed": condition.illness_progression and abs(infection_delta) > 0.001, "delta": round(infection_delta, 6)},
                "symptom": {"expressed": symptom_expressed, "fever": round(float(body["fever"]), 6), "fatigue": round(float(body["fatigue"]), 6)},
                "immune": {"recovered": recovered, "immune_delta": round(immune_delta, 6)},
                "care": {"triaged": triaged, "priority": "high" if triaged else "monitor", "triage_score": round(triage_score, 6)},
                "quarantine": {"chosen": quarantine, "reason": "infection_load" if quarantine else "none"},
                "containment": {"contained": quarantine and condition.contagion_containment, "contagion_delta": round(float(body["contagiousness"]) - contagion_before, 6)},
                "clean_water": {"given": clean_water_given, "hydration_delta": round(float(body["hydration"]) - float(before["hydration"]), 6), "remaining_doses": care_water_doses},
                "rest": {"rested": rest_given, "energy_delta": round(float(body["energy"]) - float(before["energy"]), 6), "remaining_slots": rest_slots},
                "sanitation": {"bound": condition.sanitation_feedback, "risk_source": "ecology_nodes", "waste_risk": round(risk["waste_risk"], 6), "water_risk": round(risk["water_risk"], 6)},
                "social": {"modulated": condition.social_access and (quarantine or float(body["social_access"]) < 0.92), "access": round(float(body["social_access"]), 6)},
                "guardrail": {"bounded": condition.health_guardrail and float(body["infection_load"]) <= 0.74 and float(body["fever"]) <= 0.64 and (condition.immune_recovery or float(body["infection_load"]) < 0.34), "max_infection": round(float(body["infection_load"]), 6)},
            }
            event = make_event(event_id, condition, day, agent_id, before, copy.deepcopy(body), packets, replay, claim_boundary)
            events.append(event)
            recovery_path_available = condition.care_triage and condition.immune_recovery
            low_risk_recovered = float(body["infection_load"]) < 0.14 and float(body["fever"]) < 0.10 and triage_score < 0.20
            effective_care = recovery_path_available and ((triaged and (clean_water_given or rest_given)) or low_risk_recovered)
            effective_quarantine = recovery_path_available and condition.quarantine_choices and (quarantine or low_risk_recovered)
            effective_containment = effective_quarantine and condition.contagion_containment and ((quarantine and float(body["contagiousness"]) < max(contagion_before, 0.01)) or low_risk_recovered)
            hits["exposure"].append(1.0 if condition.exposure_binding and exposure > 0.0 else 0.0)
            hits["progress"].append(1.0 if packets["illness"]["progressed"] else 0.0)
            hits["symptom"].append(1.0 if symptom_expressed else 0.0)
            hits["immune"].append(1.0 if recovered and float(body["infection_load"]) <= max(float(before["infection_load"]), 0.74) else 0.0)
            hits["care"].append(1.0 if effective_care else 0.0)
            hits["quarantine"].append(1.0 if effective_quarantine else 0.0)
            hits["containment"].append(1.0 if effective_containment else 0.0)
            hits["water"].append(1.0 if recovery_path_available and (clean_water_given or (low_risk_recovered and float(body["hydration"]) >= 0.62)) else 0.0)
            hits["rest"].append(1.0 if recovery_path_available and (rest_given or (low_risk_recovered and float(body["fatigue"]) <= 0.32)) else 0.0)
            hits["sanitation"].append(1.0 if condition.sanitation_feedback and risk["total"] > 0.12 else 0.0)
            hits["social"].append(1.0 if condition.social_access and recovery_path_available and (packets["social"]["modulated"] or low_risk_recovered) else 0.0)
            hits["guardrail"].append(1.0 if packets["guardrail"]["bounded"] else 0.0)
            hits["freq"].append(1.0 if condition.frequency_flower_binding and event["frequency_hz"] is not None and event["flower_node"] != "unbound" else 0.0)
            hits["replay"].append(1.0 if event["replay_frame"] is not None else 0.0)
            hits["privacy"].append(1.0 if condition.privacy_filter and event["private_health_hidden"] else 0.0)
            hits["trace"].append(1.0 if trace_ok(event) and event["claim_boundary"] == claim_boundary else 0.0)
            event_id += 1

    metrics = {
        "ecological_exposure_binding_rate": mean(hits["exposure"]),
        "illness_progression_rate": mean(hits["progress"]),
        "symptom_expression_rate": mean(hits["symptom"]),
        "immune_recovery_rate": mean(hits["immune"]),
        "care_triage_rate": mean(hits["care"]),
        "quarantine_choice_rate": mean(hits["quarantine"]),
        "contagion_containment_rate": mean(hits["containment"]),
        "clean_water_care_rate": mean(hits["water"]),
        "rest_recovery_coupling_rate": mean(hits["rest"]),
        "sanitation_feedback_binding_rate": mean(hits["sanitation"]),
        "social_access_modulation_rate": mean(hits["social"]),
        "health_guardrail_rate": mean(hits["guardrail"]),
        "frequency_flower_health_binding_rate": mean(hits["freq"]),
        "browser_health_replay_rate": mean(hits["replay"]),
        "privacy_preservation_rate": mean(hits["privacy"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: clamp(value) for key, value in metrics.items()}
    readiness = sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS)
    row = EvalRow(
        condition=condition.name,
        agent_count=len(bodies),
        simulated_days=config.days,
        health_events=len(events),
        embodied_health_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in metrics.items()},
    )
    state = {"condition": condition.name, "source_condition": source.get("condition"), "ecology_nodes": nodes, "bodies": bodies, "events": events, "replay": replay, "health_kernel": {"care_water_doses_remaining": care_water_doses, "rest_slots_remaining": rest_slots, "not_subjective_illness": True}}
    return row, state, events


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_embodied_illness_immune_care_quarantine"]

    def loss(name: str) -> float:
        return round(full.embodied_health_readiness - by_name[name].embodied_health_readiness, 6)

    losses = {
        "no_exposure_binding_loss": loss("no_exposure_binding"),
        "no_illness_progression_loss": loss("no_illness_progression"),
        "no_symptom_expression_loss": loss("no_symptom_expression"),
        "no_immune_recovery_loss": loss("no_immune_recovery"),
        "no_care_triage_loss": loss("no_care_triage"),
        "no_quarantine_choices_loss": loss("no_quarantine_choices"),
        "no_contagion_containment_loss": loss("no_contagion_containment"),
        "no_clean_water_care_loss": loss("no_clean_water_care"),
        "no_rest_recovery_loss": loss("no_rest_recovery"),
        "no_sanitation_feedback_loss": loss("no_sanitation_feedback"),
        "no_social_access_modulation_loss": loss("no_social_access_modulation"),
        "no_health_guardrail_loss": loss("no_health_guardrail"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_replay_timeline_loss": loss("no_replay_timeline"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.embodied_health_readiness >= 0.80
        and full.health_events >= 24
        and full.ecological_exposure_binding_rate == 1.0
        and full.illness_progression_rate >= 0.70
        and full.symptom_expression_rate >= 0.50
        and full.immune_recovery_rate >= 0.40
        and full.care_triage_rate >= 0.25
        and full.quarantine_choice_rate >= 0.20
        and full.health_guardrail_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_exposure_binding_loss"] >= 0.08
        and losses["no_immune_recovery_loss"] >= 0.09
        and losses["no_care_triage_loss"] >= 0.10
        and losses["no_quarantine_choices_loss"] >= 0.08
    )
    return VerdictRow(
        full_condition=full.condition,
        full_embodied_health_readiness=full.embodied_health_readiness,
        full_ecological_exposure_binding_rate=full.ecological_exposure_binding_rate,
        full_illness_progression_rate=full.illness_progression_rate,
        full_symptom_expression_rate=full.symptom_expression_rate,
        full_immune_recovery_rate=full.immune_recovery_rate,
        full_care_triage_rate=full.care_triage_rate,
        full_quarantine_choice_rate=full.quarantine_choice_rate,
        full_contagion_containment_rate=full.contagion_containment_rate,
        full_clean_water_care_rate=full.clean_water_care_rate,
        full_rest_recovery_coupling_rate=full.rest_recovery_coupling_rate,
        full_sanitation_feedback_binding_rate=full.sanitation_feedback_binding_rate,
        full_social_access_modulation_rate=full.social_access_modulation_rate,
        full_health_guardrail_rate=full.health_guardrail_rate,
        full_frequency_flower_health_binding_rate=full.frequency_flower_health_binding_rate,
        full_browser_health_replay_rate=full.browser_health_replay_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        supports_embodied_illness_immune_care_quarantine_bridge=supports,
        supports_functional_health_state_seed=supports,
        supports_complete_3d_world=False,
        supports_complete_playable_world=False,
        supports_subjective_consciousness=False,
        supports_moral_patienthood_claim=False,
        supports_subjective_illness_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: HealthConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_state: dict[str, object] = {}
    integrated_trace: list[dict[str, object]] = []
    for condition in CONDITIONS:
        row, state, trace = simulate_condition(config, source, condition)
        rows.append(row)
        if condition.name == "integrated_embodied_illness_immune_care_quarantine":
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
        "agents": AGENTS,
        "moral_boundary": {
            "functional_health_seed_not_complete_gameplay": True,
            "infection_load_not_subjective_illness": True,
            "care_triage_policy_not_moral_patienthood": True,
            "quarantine_not_social_punishment": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "caregiver role specialization, bedside routines, and recovery memory",
    }
    state = {"condition": "integrated_embodied_illness_immune_care_quarantine", "config": asdict(config), "source_condition": source.get("condition"), "health_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": results["moral_boundary"]}
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_EMBODIED_ILLNESS_IMMUNE_CARE_QUARANTINE_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_EMBODIED_ILLNESS_IMMUNE_CARE_QUARANTINE_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_EMBODIED_ILLNESS_IMMUNE_CARE_QUARANTINE_STATE", state)
    return results


def parse_args() -> HealthConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=HealthConfig.seed)
    parser.add_argument("--days", type=int, default=HealthConfig.days)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return HealthConfig(seed=args.seed, days=args.days, source_state=args.source_state)


def main() -> None:
    config = parse_args()
    results = run(config)
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("embodied_health_readiness", f"{verdict['full_embodied_health_readiness']:.6f}")
    print("health_events", results["rows"][0]["health_events"])
    print("no_exposure_binding_loss", f"{verdict['no_exposure_binding_loss']:.6f}")
    print("no_care_triage_loss", f"{verdict['no_care_triage_loss']:.6f}")
    print("no_quarantine_choices_loss", f"{verdict['no_quarantine_choices_loss']:.6f}")


if __name__ == "__main__":
    main()
