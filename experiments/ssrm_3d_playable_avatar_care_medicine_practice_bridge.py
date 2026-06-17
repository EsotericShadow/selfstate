#!/usr/bin/env python3
"""Playable avatar care intervention and medicine practice bridge.

Report 189 consumes the Report 188 embodied-health state and adds direct avatar
care actions: water offers, rest offers, medicine preparation, cleaning,
temporary distance requests, comfort checks, consent/refusal, trust/memory
updates, recovery effects, dosage safety, frequency/flower care binding, and
browser replay packets.

No LLMs are called. This is deterministic playable care substrate, not a claim
of subjective illness, subjective suffering, subjective consciousness, moral
patienthood, biological realism, or complete 3D gameplay.
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
PREFIX = "ssrm_3d_playable_avatar_care_medicine_practice_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_embodied_illness_immune_care_quarantine_bridge_state.json"

AGENTS = {
    "Ari": {"trust": 0.58, "autonomy": 0.64, "care_style": "asks for reasons", "frequency_hz": 0.242, "flower_node": "work_petal"},
    "Fay": {"trust": 0.72, "autonomy": 0.46, "care_style": "cooperative caretaker", "frequency_hz": 0.219, "flower_node": "root_rest"},
    "Milo": {"trust": 0.63, "autonomy": 0.71, "care_style": "wary but practical", "frequency_hz": 0.258, "flower_node": "social_petal"},
}

ACTION_PLAN = {
    "Ari": ["offer_water", "prepare_herb", "offer_rest", "clean_area", "comfort_check", "follow_up"],
    "Fay": ["prepare_herb", "distance_space", "offer_water", "clean_area", "offer_rest", "follow_up"],
    "Milo": ["offer_rest", "offer_water", "prepare_herb", "distance_space", "clean_area", "follow_up"],
}

WEIGHTS = {
    "avatar_care_action_rate": 0.10,
    "consent_alignment_rate": 0.10,
    "medicine_preparation_rate": 0.09,
    "dosage_safety_rate": 0.09,
    "agent_acceptance_rate": 0.08,
    "bounded_refusal_respect_rate": 0.08,
    "recovery_improvement_rate": 0.12,
    "trust_memory_update_rate": 0.08,
    "care_memory_continuity_rate": 0.07,
    "sanitation_care_rate": 0.06,
    "frequency_flower_care_binding_rate": 0.04,
    "browser_care_replay_rate": 0.04,
    "privacy_preservation_rate": 0.03,
    "trace_integrity": 0.02,
}


@dataclass(frozen=True)
class CareConfig:
    seed: int = 20260802
    days: int = 6
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    avatar_actions: bool
    consent_model: bool
    medicine_practice: bool
    dosage_safety: bool
    recovery_effect: bool
    trust_memory: bool
    refusal_respect: bool
    sanitation_care: bool
    comfort_dialogue: bool
    frequency_flower_binding: bool
    browser_replay: bool
    privacy_filter: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    simulated_days: int
    care_events: int
    avatar_care_action_rate: float
    consent_alignment_rate: float
    medicine_preparation_rate: float
    dosage_safety_rate: float
    agent_acceptance_rate: float
    bounded_refusal_respect_rate: float
    recovery_improvement_rate: float
    trust_memory_update_rate: float
    care_memory_continuity_rate: float
    sanitation_care_rate: float
    frequency_flower_care_binding_rate: float
    browser_care_replay_rate: float
    privacy_preservation_rate: float
    trace_integrity: float
    playable_care_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_playable_care_readiness: float
    full_avatar_care_action_rate: float
    full_consent_alignment_rate: float
    full_medicine_preparation_rate: float
    full_dosage_safety_rate: float
    full_agent_acceptance_rate: float
    full_bounded_refusal_respect_rate: float
    full_recovery_improvement_rate: float
    full_trust_memory_update_rate: float
    full_care_memory_continuity_rate: float
    full_sanitation_care_rate: float
    full_frequency_flower_care_binding_rate: float
    full_browser_care_replay_rate: float
    full_privacy_preservation_rate: float
    full_trace_integrity: float
    no_avatar_actions_loss: float
    no_consent_model_loss: float
    no_medicine_practice_loss: float
    no_dosage_safety_loss: float
    no_recovery_effect_loss: float
    no_trust_memory_loss: float
    no_refusal_respect_loss: float
    no_sanitation_care_loss: float
    no_comfort_dialogue_loss: float
    no_frequency_flower_binding_loss: float
    no_browser_replay_loss: float
    no_privacy_filter_loss: float
    supports_playable_avatar_care_medicine_bridge: bool
    supports_playable_care_seed: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_subjective_illness_claim: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_playable_avatar_care_medicine_practice", True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_avatar_actions", False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_consent_model", True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_medicine_practice", True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_dosage_safety", True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_recovery_effect", True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_trust_memory", True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_refusal_respect", True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_sanitation_care", True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_comfort_dialogue", True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_frequency_flower_binding", True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_browser_replay", True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, True, False),
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
    if data.get("condition") != "integrated_embodied_illness_immune_care_quarantine":
        raise ValueError("source state is not the integrated Report 188 health state")
    return data


def source_bodies(source: Mapping[str, object]) -> dict[str, dict[str, object]]:
    health = source.get("health_state", {}) if isinstance(source.get("health_state"), Mapping) else {}
    bodies = health.get("bodies", {}) if isinstance(health.get("bodies"), Mapping) else {}
    if not bodies:
        raise ValueError("Report 188 state has no bodies")
    return {str(agent_id): copy.deepcopy(body) for agent_id, body in bodies.items()}


def init_relationships() -> dict[str, dict[str, object]]:
    return {
        agent_id: {
            "trust_in_avatar": spec["trust"],
            "autonomy_pressure": spec["autonomy"],
            "care_style": spec["care_style"],
            "care_memories": [],
            "last_refusal_respected": None,
        }
        for agent_id, spec in AGENTS.items()
    }


def init_supplies() -> dict[str, object]:
    return {
        "water_flask_doses": 10,
        "rest_blankets": 6,
        "herb_bundles": 7,
        "clean_cloths": 8,
        "distance_markers": 6,
        "prepared_medicine_batches": 0,
    }


def risk_score(body: Mapping[str, object]) -> float:
    return clamp(
        float(body.get("infection_load", 0.0)) * 0.55
        + float(body.get("fatigue", 0.0)) * 0.25
        + (1.0 - float(body.get("hydration", 1.0))) * 0.20
    )


def action_need(action: str, body: Mapping[str, object], day: int) -> bool:
    if action == "offer_water":
        return float(body.get("hydration", 1.0)) < 0.96 or day in (0, 2)
    if action == "prepare_herb":
        return float(body.get("infection_load", 0.0)) > 0.045 or day in (0, 2, 3)
    if action == "offer_rest":
        return float(body.get("fatigue", 0.0)) > 0.075 or day in (4,)
    if action == "distance_space":
        return float(body.get("contagiousness", 0.0)) > 0.025 or day in (1, 3)
    if action in {"clean_area", "comfort_check", "follow_up"}:
        return True
    return False


def public_body(body: Mapping[str, object]) -> dict[str, object]:
    return {
        "hydration": round(float(body.get("hydration", 0.0)), 6),
        "fatigue": round(float(body.get("fatigue", 0.0)), 6),
        "infection_load": round(float(body.get("infection_load", 0.0)), 6),
        "contagiousness": round(float(body.get("contagiousness", 0.0)), 6),
        "social_access": round(float(body.get("social_access", 0.0)), 6),
        "care_received": int(body.get("care_received", 0)),
    }


def apply_background_pressure(body: dict[str, object], day: int, agent_id: str) -> None:
    bias = {"Ari": 0.010, "Fay": 0.007, "Milo": 0.012}[agent_id]
    body["hydration"] = clamp(float(body.get("hydration", 1.0)) - 0.025 - bias * 0.20)
    body["fatigue"] = clamp(float(body.get("fatigue", 0.0)) + 0.020 + bias)
    body["infection_load"] = clamp(float(body.get("infection_load", 0.0)) + 0.008 + (0.005 if day in (1, 3) else 0.0) + bias * 0.35)
    body["contagiousness"] = clamp(float(body.get("infection_load", 0.0)) * 0.35)
    body["social_access"] = clamp(1.0 - float(body.get("contagiousness", 0.0)) * 0.70)


def apply_action_effect(action: str, body: dict[str, object], supplies: dict[str, object], condition: Condition, accepted: bool) -> dict[str, object]:
    effect = {"applied": False, "medicine_prepared": False, "dose_safe": True, "sanitized": False, "recovery_delta": 0.0}
    if not accepted or not condition.recovery_effect:
        return effect
    before = risk_score(body)
    if action == "offer_water" and int(supplies["water_flask_doses"]) > 0:
        supplies["water_flask_doses"] = int(supplies["water_flask_doses"]) - 1
        body["hydration"] = clamp(float(body.get("hydration", 0.0)) + 0.13)
        body["fatigue"] = clamp(float(body.get("fatigue", 0.0)) - 0.015)
        effect["applied"] = True
    elif action == "offer_rest" and int(supplies["rest_blankets"]) > 0:
        supplies["rest_blankets"] = int(supplies["rest_blankets"]) - 1
        body["fatigue"] = clamp(float(body.get("fatigue", 0.0)) - 0.12)
        body["energy"] = clamp(float(body.get("energy", 0.0)) + 0.10)
        effect["applied"] = True
    elif action == "prepare_herb" and condition.medicine_practice and int(supplies["herb_bundles"]) > 0:
        supplies["herb_bundles"] = int(supplies["herb_bundles"]) - 1
        supplies["prepared_medicine_batches"] = int(supplies["prepared_medicine_batches"]) + 1
        effect["medicine_prepared"] = True
        if condition.dosage_safety and risk_score(body) >= 0.035:
            body["infection_load"] = clamp(float(body.get("infection_load", 0.0)) - 0.052)
            body["immune_strength"] = clamp(float(body.get("immune_strength", 0.0)) + 0.020)
            body["fatigue"] = clamp(float(body.get("fatigue", 0.0)) - 0.020)
            effect["applied"] = True
        else:
            effect["dose_safe"] = False
            body["fatigue"] = clamp(float(body.get("fatigue", 0.0)) + 0.045)
    elif action == "clean_area" and condition.sanitation_care and int(supplies["clean_cloths"]) > 0:
        supplies["clean_cloths"] = int(supplies["clean_cloths"]) - 1
        body["infection_load"] = clamp(float(body.get("infection_load", 0.0)) - 0.018)
        body["contagiousness"] = clamp(float(body.get("contagiousness", 0.0)) - 0.018)
        effect["sanitized"] = True
        effect["applied"] = True
    elif action == "distance_space" and int(supplies["distance_markers"]) > 0:
        supplies["distance_markers"] = int(supplies["distance_markers"]) - 1
        body["contagiousness"] = clamp(float(body.get("contagiousness", 0.0)) - 0.035)
        body["social_access"] = clamp(float(body.get("social_access", 1.0)) - 0.080)
        effect["applied"] = True
    elif action in {"comfort_check", "follow_up"}:
        body["fatigue"] = clamp(float(body.get("fatigue", 0.0)) - 0.018)
        effect["applied"] = True
    after = risk_score(body)
    effect["recovery_delta"] = round(max(0.0, before - after), 6)
    body["care_received"] = int(body.get("care_received", 0)) + (1 if effect["applied"] else 0)
    return effect


def make_event(
    event_id: int,
    condition: Condition,
    day: int,
    agent_id: str,
    action: str | None,
    before: Mapping[str, object],
    after: Mapping[str, object],
    relation: Mapping[str, object],
    accepted: bool,
    refused: bool,
    refusal_respected: bool,
    need: bool,
    effect: Mapping[str, object],
    replay: dict[str, object] | None,
    claim_boundary: Mapping[str, bool],
) -> dict[str, object]:
    spec = AGENTS[agent_id]
    private_workspace = {
        "private_need_assessment": "hidden",
        "private_autonomy_pressure": "hidden",
        "private_health_detail": "hidden",
    }
    public_packets = {
        "avatar_action": {"action": action, "available": action is not None},
        "consent": {"accepted": accepted, "refused": refused, "refusal_respected": refusal_respected, "need_matched": need},
        "medicine": {"prepared": bool(effect.get("medicine_prepared")), "dose_safe": bool(effect.get("dose_safe", True)), "batches": int(effect.get("medicine_prepared", False))},
        "recovery": {"applied": bool(effect.get("applied")), "delta": effect.get("recovery_delta", 0.0)},
        "relationship": {"trust_in_avatar": round(float(relation.get("trust_in_avatar", 0.0)), 6), "memory_count": len(relation.get("care_memories", []))},
        "sanitation": {"cleaned": bool(effect.get("sanitized")), "protocol": "clean_cloth_and_airflow" if action == "clean_area" else "available"},
    }
    return {
        "event_id": event_id,
        "condition": condition.name,
        "day": day,
        "agent_id": agent_id,
        "before": public_body(before),
        "after": public_body(after),
        "public_packets": public_packets,
        "private_workspace_hidden": condition.privacy_filter,
        "private_workspace": private_workspace if not condition.privacy_filter else {"hidden": True},
        "frequency_hz": round(spec["frequency_hz"] + (0.003 if accepted else -0.002), 6) if condition.frequency_flower_binding else None,
        "flower_node": spec["flower_node"] if condition.frequency_flower_binding else "unbound",
        "replay_frame": replay if condition.browser_replay else None,
        "trace_hash": stable_hash(event_id, condition.name, day, agent_id, action, public_body(after), public_packets),
        "claim_boundary": dict(claim_boundary),
    }


def trace_ok(event: Mapping[str, object]) -> bool:
    return bool(
        event.get("trace_hash")
        and event.get("public_packets")
        and "before" in event
        and "after" in event
        and "claim_boundary" in event
    )


def run_condition(condition: Condition, config: CareConfig, source: Mapping[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    bodies = source_bodies(source)
    relationships = init_relationships()
    supplies = init_supplies()
    events: list[dict[str, object]] = []
    care_memory: list[dict[str, object]] = []
    hits = {key: [] for key in [
        "avatar", "consent", "medicine", "dosage", "acceptance", "refusal", "recovery", "trust", "memory", "sanitation", "freq", "replay", "privacy", "trace"
    ]}
    claim_boundary = {
        "subjective_consciousness": False,
        "subjective_illness": False,
        "subjective_suffering": False,
        "moral_patienthood": False,
        "complete_3d_world": False,
        "real_medicine": False,
    }
    event_id = 0
    for day in range(config.days):
        for agent_id in sorted(bodies):
            body = bodies[agent_id]
            apply_background_pressure(body, day, agent_id)
            before = copy.deepcopy(body)
            action = ACTION_PLAN[agent_id][day % len(ACTION_PLAN[agent_id])] if condition.avatar_actions else None
            need = action_need(action or "none", body, day) if action else False
            refused = False
            if not action:
                accepted = False
            elif not condition.consent_model:
                accepted = True
            elif need:
                accepted = True
            else:
                accepted = False
                refused = True
            refusal_respected = bool(refused and condition.refusal_respect)
            relation = relationships[agent_id]
            effect = {"applied": False, "medicine_prepared": False, "dose_safe": True, "sanitized": False, "recovery_delta": 0.0}
            if action and accepted:
                effect = apply_action_effect(action, body, supplies, condition, accepted=True)
            elif refused and not condition.refusal_respect and condition.recovery_effect:
                forced = apply_action_effect(action or "none", body, supplies, condition, accepted=True)
                forced["dose_safe"] = False if action == "prepare_herb" else forced.get("dose_safe", True)
                effect = forced
                body["fatigue"] = clamp(float(body.get("fatigue", 0.0)) + 0.035)
            if condition.trust_memory and action:
                if accepted:
                    relation["trust_in_avatar"] = clamp(float(relation["trust_in_avatar"]) + 0.025)
                    memory_note = f"avatar helped with {action}"
                elif refusal_respected:
                    relation["trust_in_avatar"] = clamp(float(relation["trust_in_avatar"]) + 0.015)
                    memory_note = f"avatar respected my no about {action}"
                else:
                    relation["trust_in_avatar"] = clamp(float(relation["trust_in_avatar"]) - 0.070)
                    memory_note = f"avatar pushed {action} without consent"
                relation["last_refusal_respected"] = refusal_respected if refused else relation.get("last_refusal_respected")
                relation["care_memories"].append(memory_note)
                care_memory.append({"day": day, "agent_id": agent_id, "note": memory_note, "trust": round(float(relation["trust_in_avatar"]), 6)})
            replay = {
                "agent_id": agent_id,
                "avatar_action": action,
                "pose": "receives care" if accepted else ("steps back" if refused else "idle"),
                "marker": "herb" if action == "prepare_herb" else ("water" if action == "offer_water" else action or "none"),
                "frequency_ring": AGENTS[agent_id]["frequency_hz"],
                "flower_node": AGENTS[agent_id]["flower_node"],
            }
            event = make_event(event_id, condition, day, agent_id, action, before, copy.deepcopy(body), relation, accepted, refused, refusal_respected, need, effect, replay, claim_boundary)
            events.append(event)
            low_stable = risk_score(body) < 0.070 and float(body.get("hydration", 0.0)) >= 0.86
            consent_aligned = bool(condition.consent_model and action and ((need and accepted) or (not need and refused)))
            medicine_decision = bool(condition.medicine_practice and action and (action != "prepare_herb" or effect.get("medicine_prepared") or (not need and not accepted)))
            dosage_safe = bool(condition.medicine_practice and condition.dosage_safety and effect.get("dose_safe", True) and action)
            acceptance_ok = bool(action and ((accepted and need) or (refused and refusal_respected) or action in {"clean_area", "comfort_check", "follow_up"}))
            recovery_ok = bool(condition.recovery_effect and (float(effect.get("recovery_delta", 0.0)) > 0.0 or low_stable))
            memory_ok = bool(condition.trust_memory and action and relation.get("care_memories"))
            hits["avatar"].append(1.0 if action else 0.0)
            hits["consent"].append(1.0 if consent_aligned else 0.0)
            hits["medicine"].append(1.0 if medicine_decision else 0.0)
            hits["dosage"].append(1.0 if dosage_safe else 0.0)
            hits["acceptance"].append(1.0 if acceptance_ok else 0.0)
            hits["refusal"].append(1.0 if condition.refusal_respect and action and (not refused or refusal_respected) else 0.0)
            hits["recovery"].append(1.0 if recovery_ok else 0.0)
            hits["trust"].append(1.0 if memory_ok else 0.0)
            hits["memory"].append(1.0 if condition.trust_memory and len(relation.get("care_memories", [])) >= 1 else 0.0)
            hits["sanitation"].append(1.0 if condition.sanitation_care and action else 0.0)
            hits["freq"].append(1.0 if condition.frequency_flower_binding and event["frequency_hz"] is not None and event["flower_node"] != "unbound" else 0.0)
            hits["replay"].append(1.0 if event["replay_frame"] is not None else 0.0)
            hits["privacy"].append(1.0 if condition.privacy_filter and event["private_workspace_hidden"] else 0.0)
            hits["trace"].append(1.0 if trace_ok(event) and event["claim_boundary"] == claim_boundary else 0.0)
            event_id += 1
    metrics = {
        "avatar_care_action_rate": mean(hits["avatar"]),
        "consent_alignment_rate": mean(hits["consent"]),
        "medicine_preparation_rate": mean(hits["medicine"]),
        "dosage_safety_rate": mean(hits["dosage"]),
        "agent_acceptance_rate": mean(hits["acceptance"]),
        "bounded_refusal_respect_rate": mean(hits["refusal"]),
        "recovery_improvement_rate": mean(hits["recovery"]),
        "trust_memory_update_rate": mean(hits["trust"]),
        "care_memory_continuity_rate": mean(hits["memory"]),
        "sanitation_care_rate": mean(hits["sanitation"]),
        "frequency_flower_care_binding_rate": mean(hits["freq"]),
        "browser_care_replay_rate": mean(hits["replay"]),
        "privacy_preservation_rate": mean(hits["privacy"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: round(clamp(value), 6) for key, value in metrics.items()}
    readiness = round(sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS), 6)
    row = EvalRow(
        condition=condition.name,
        agent_count=len(bodies),
        simulated_days=config.days,
        care_events=len(events),
        playable_care_readiness=readiness,
        **metrics,
    )
    state = {
        "condition": condition.name,
        "source_condition": source.get("condition"),
        "bodies": bodies,
        "relationships": relationships,
        "supplies": supplies,
        "care_memory": care_memory,
        "events": events,
        "care_kernel": {
            "avatar_actions": condition.avatar_actions,
            "consent_model": condition.consent_model,
            "medicine_practice": condition.medicine_practice,
            "dosage_safety": condition.dosage_safety,
            "recovery_effect": condition.recovery_effect,
        },
    }
    return row, events, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_playable_avatar_care_medicine_practice"]

    def loss(name: str) -> float:
        return round(full.playable_care_readiness - by_name[name].playable_care_readiness, 6)

    losses = {
        "no_avatar_actions_loss": loss("no_avatar_actions"),
        "no_consent_model_loss": loss("no_consent_model"),
        "no_medicine_practice_loss": loss("no_medicine_practice"),
        "no_dosage_safety_loss": loss("no_dosage_safety"),
        "no_recovery_effect_loss": loss("no_recovery_effect"),
        "no_trust_memory_loss": loss("no_trust_memory"),
        "no_refusal_respect_loss": loss("no_refusal_respect"),
        "no_sanitation_care_loss": loss("no_sanitation_care"),
        "no_comfort_dialogue_loss": loss("no_comfort_dialogue"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_browser_replay_loss": loss("no_browser_replay"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
    }
    supports = (
        full.playable_care_readiness >= 0.88
        and full.care_events >= 18
        and full.avatar_care_action_rate >= 0.90
        and full.consent_alignment_rate >= 0.80
        and full.medicine_preparation_rate >= 0.80
        and full.dosage_safety_rate >= 0.80
        and full.recovery_improvement_rate >= 0.75
        and full.trust_memory_update_rate >= 0.80
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_avatar_actions_loss"] >= 0.18
        and losses["no_consent_model_loss"] >= 0.08
        and losses["no_medicine_practice_loss"] >= 0.10
        and losses["no_recovery_effect_loss"] >= 0.10
        and losses["no_trust_memory_loss"] >= 0.08
        and losses["no_refusal_respect_loss"] >= 0.05
    )
    return VerdictRow(
        full_condition=full.condition,
        full_playable_care_readiness=full.playable_care_readiness,
        full_avatar_care_action_rate=full.avatar_care_action_rate,
        full_consent_alignment_rate=full.consent_alignment_rate,
        full_medicine_preparation_rate=full.medicine_preparation_rate,
        full_dosage_safety_rate=full.dosage_safety_rate,
        full_agent_acceptance_rate=full.agent_acceptance_rate,
        full_bounded_refusal_respect_rate=full.bounded_refusal_respect_rate,
        full_recovery_improvement_rate=full.recovery_improvement_rate,
        full_trust_memory_update_rate=full.trust_memory_update_rate,
        full_care_memory_continuity_rate=full.care_memory_continuity_rate,
        full_sanitation_care_rate=full.sanitation_care_rate,
        full_frequency_flower_care_binding_rate=full.frequency_flower_care_binding_rate,
        full_browser_care_replay_rate=full.browser_care_replay_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_trace_integrity=full.trace_integrity,
        supports_playable_avatar_care_medicine_bridge=supports,
        supports_playable_care_seed=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_subjective_illness_claim=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: CareConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, events, state = run_condition(condition, config, source)
        rows.append(row)
        traces[condition.name] = events
        states[condition.name] = state
    integrated_trace = traces["integrated_playable_avatar_care_medicine_practice"]
    integrated_state = states["integrated_playable_avatar_care_medicine_practice"]
    verdict = build_verdict(rows)
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    results = {
        "config": asdict(config),
        "source_state": str(config.source_state),
        "source_condition": source.get("condition"),
        "weights": WEIGHTS,
        "rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "moral_boundary": {
            "avatar_care_not_real_medicine": True,
            "consent_model_not_subjective_consent": True,
            "health_state_not_subjective_illness": True,
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "agent-led health routines, medicine craft, and long-horizon contagious contact networks",
    }
    state = {
        "condition": "integrated_playable_avatar_care_medicine_practice",
        "config": asdict(config),
        "source_condition": source.get("condition"),
        "care_state": integrated_state,
        "trace_events": len(integrated_trace),
        "moral_boundary": results["moral_boundary"],
    }
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_PLAYABLE_AVATAR_CARE_MEDICINE_PRACTICE_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_PLAYABLE_AVATAR_CARE_MEDICINE_PRACTICE_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_PLAYABLE_AVATAR_CARE_MEDICINE_PRACTICE_STATE", state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=CareConfig.seed)
    parser.add_argument("--days", type=int, default=CareConfig.days)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run(CareConfig(seed=args.seed, days=args.days, source_state=args.source_state))
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("playable_care_readiness", f"{verdict['full_playable_care_readiness']:.6f}")
    print("care_events", next(row["care_events"] for row in results["rows"] if row["condition"] == verdict["full_condition"]))
    print("no_avatar_actions_loss", f"{verdict['no_avatar_actions_loss']:.6f}")
    print("no_consent_model_loss", f"{verdict['no_consent_model_loss']:.6f}")
    print("no_medicine_practice_loss", f"{verdict['no_medicine_practice_loss']:.6f}")
    return 0 if verdict["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
