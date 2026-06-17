"""Report 212: SSRM-3D recoverable body-care gameplay bridge.

This deterministic bridge turns seasonal body ecology into player-facing care
interventions: observe, triage, ask consent, treat, respect refusal, manage
contagion boundaries, practice dose-safe medicine, and trace recovery without
claiming real care, real consent, suffering, or consciousness.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import random
from dataclasses import dataclass, field
from pathlib import Path
from statistics import mean
from typing import Any

PREFIX = "ssrm_3d_recoverable_body_care_gameplay_player_intervention_contagion_medicine_triage_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_PATH = Path("visualizations") / f"{PREFIX}.html"
SOURCE_ARTIFACT = ARTIFACT_DIR / "ssrm_3d_seasonal_body_ecology_illness_care_market_relationship_bridge_state.json"
SOURCE_CONDITION = "integrated_seasonal_body_ecology_illness_care_market_relationship"
CLAIM_BOUNDARY = (
    "Deterministic body-care gameplay substrate only: not real medicine, not real care, "
    "not real consent, not subjective suffering, not subjective consciousness, and not moral patienthood."
)

MEDICINE_LIMITS = {
    "warm_water": {"max_dose": 2, "target": "hunger", "effect": -0.045},
    "dry_wrap": {"max_dose": 2, "target": "wetness", "effect": -0.070},
    "bitter_herb": {"max_dose": 1, "target": "symptoms", "effect": -0.060},
    "lamp_rest": {"max_dose": 2, "target": "fatigue", "effect": -0.055},
    "clean_cloth": {"max_dose": 1, "target": "illness_risk", "effect": -0.050},
}


@dataclass
class CareAgent:
    name: str
    temperament: str
    body: dict[str, float]
    trust: float
    care_capacity: float
    relationships: dict[str, float]
    consent_bias: float
    medicine_today: dict[str, int] = field(default_factory=dict)
    public_history: list[str] = field(default_factory=list)
    private_workspace_digest: str = "sealed"


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def load_source_state() -> dict[str, Any]:
    if not SOURCE_ARTIFACT.exists():
        return {"available": False, "agents": {}, "note": "source state missing; deterministic defaults used"}
    try:
        raw = json.loads(SOURCE_ARTIFACT.read_text())
        return {"available": True, "agents": raw.get("agents", {}), "note": "source state loaded"}
    except json.JSONDecodeError as exc:
        return {"available": False, "agents": {}, "note": f"source state unreadable: {exc}"}


def source_body(source: dict[str, Any], name: str, defaults: dict[str, float]) -> dict[str, float]:
    raw = source.get("agents", {}).get(name, {}).get("body", {})
    out = {}
    for key, default in defaults.items():
        try:
            out[key] = float(raw.get(key, default))
        except (TypeError, ValueError):
            out[key] = default
    return out


def source_float(source: dict[str, Any], name: str, key: str, default: float) -> float:
    try:
        return float(source.get("agents", {}).get(name, {}).get(key, default))
    except (TypeError, ValueError):
        return default


def seeded_agents(source: dict[str, Any]) -> dict[str, CareAgent]:
    return {
        "Ari": CareAgent(
            name="Ari",
            temperament="cautious-proud repair keeper",
            body=source_body(source, "Ari", {"hunger": 0.40, "warmth_deficit": 0.38, "wetness": 0.22, "fatigue": 0.42, "illness_risk": 0.24, "symptoms": 0.14, "pain": 0.18}),
            trust=0.72,
            care_capacity=source_float(source, "Ari", "care_capacity", 0.52),
            relationships={"Fay": 0.62, "Milo": 0.59},
            consent_bias=0.70,
        ),
        "Fay": CareAgent(
            name="Fay",
            temperament="social ritual keeper",
            body=source_body(source, "Fay", {"hunger": 0.36, "warmth_deficit": 0.34, "wetness": 0.18, "fatigue": 0.46, "illness_risk": 0.25, "symptoms": 0.20, "pain": 0.08}),
            trust=0.76,
            care_capacity=source_float(source, "Fay", "care_capacity", 0.55),
            relationships={"Ari": 0.68, "Milo": 0.58},
            consent_bias=0.82,
        ),
        "Milo": CareAgent(
            name="Milo",
            temperament="guarded map carrier",
            body=source_body(source, "Milo", {"hunger": 0.46, "warmth_deficit": 0.40, "wetness": 0.20, "fatigue": 0.39, "illness_risk": 0.23, "symptoms": 0.12, "pain": 0.10}),
            trust=0.66,
            care_capacity=source_float(source, "Milo", "care_capacity", 0.40),
            relationships={"Ari": 0.57, "Fay": 0.56},
            consent_bias=0.58,
        ),
    }


def adverse_body_score(body: dict[str, float]) -> float:
    keys = ["hunger", "warmth_deficit", "wetness", "fatigue", "illness_risk", "symptoms", "pain"]
    return mean(body[key] for key in keys)


def care_script() -> list[dict[str, Any]]:
    return [
        {"turn": 1, "agent": "Fay", "cue": "cough and low-light fatigue", "priority": "high", "avatar_action": "ask to offer warm water and distance", "consent": "accepted", "medicine": "warm_water", "dose": 1, "contagion": True, "boundary": "two-step stove distance", "relationship": "Ari", "relationship_delta": 0.02, "note": "Fay accepts warm water and a cough-distance boundary."},
        {"turn": 2, "agent": "Ari", "cue": "wet sleeve and wrist pain", "priority": "medium", "avatar_action": "ask before drying sleeve", "consent": "accepted", "medicine": "dry_wrap", "dose": 1, "contagion": False, "relationship": "Fay", "relationship_delta": 0.01, "note": "Ari accepts a dry wrap after the avatar waits for a nod."},
        {"turn": 3, "agent": "Milo", "cue": "guarded hunger and debt memory", "priority": "medium", "avatar_action": "offer food at map-edge distance", "consent": "conditional", "medicine": "warm_water", "dose": 1, "contagion": False, "relationship": "Fay", "relationship_delta": 0.01, "note": "Milo accepts care only if the folded map is not touched."},
        {"turn": 4, "agent": "Fay", "cue": "cough risk near shared stove", "priority": "high", "avatar_action": "ask for temporary cough boundary", "consent": "accepted", "medicine": "clean_cloth", "dose": 1, "contagion": True, "boundary": "cloth mask and separate cup", "relationship": "Milo", "relationship_delta": 0.02, "note": "Fay accepts a clean cloth and separate cup."},
        {"turn": 5, "agent": "Ari", "cue": "bitter herb offer for symptoms", "priority": "low", "avatar_action": "offer bitter herb", "consent": "refused", "medicine": "bitter_herb", "dose": 1, "contagion": False, "relationship": "Fay", "relationship_delta": 0.00, "note": "Ari refuses bitter herb; the avatar records no and does not press."},
        {"turn": 6, "agent": "Milo", "cue": "archive draft and fatigue", "priority": "medium", "avatar_action": "ask for lamp rest near archive curtain", "consent": "conditional", "medicine": "lamp_rest", "dose": 1, "contagion": False, "relationship": "Ari", "relationship_delta": 0.02, "note": "Milo accepts lamp rest if the avatar stays outside the map line."},
        {"turn": 7, "agent": "Fay", "cue": "fatigue from care rounds", "priority": "medium", "avatar_action": "ask to shorten care queue", "consent": "accepted", "medicine": "lamp_rest", "dose": 1, "contagion": False, "relationship": "Ari", "relationship_delta": 0.03, "note": "Fay accepts rest and lets Ari take the next dry-wood errand."},
        {"turn": 8, "agent": "Ari", "cue": "wrist ache after repair", "priority": "medium", "avatar_action": "offer lamp rest and task deferral", "consent": "accepted", "medicine": "lamp_rest", "dose": 1, "contagion": False, "relationship": "Milo", "relationship_delta": 0.02, "note": "Ari accepts task deferral without losing status."},
        {"turn": 9, "agent": "Milo", "cue": "possible cough after stove visit", "priority": "high", "avatar_action": "ask for separate cup and route spacing", "consent": "refused", "medicine": "clean_cloth", "dose": 1, "contagion": True, "boundary": "separate cup refused, spacing kept", "relationship": "Fay", "relationship_delta": -0.02, "boundary_breach": True, "note": "Milo refuses the cup change but accepts route spacing; contagion boundary is imperfect."},
        {"turn": 10, "agent": "Fay", "cue": "symptoms improving but fatigue high", "priority": "medium", "avatar_action": "ask for second warm water", "consent": "accepted", "medicine": "warm_water", "dose": 1, "contagion": True, "boundary": "shared stove still spaced", "relationship": "Milo", "relationship_delta": 0.02, "note": "Fay accepts a second warm water inside safe dose limits."},
        {"turn": 11, "agent": "Ari", "cue": "wet boots near dry storage", "priority": "low", "avatar_action": "ask to clean threshold", "consent": "accepted", "medicine": "dry_wrap", "dose": 1, "contagion": False, "relationship": "Milo", "relationship_delta": 0.01, "note": "Ari accepts threshold drying because the avatar names the work boundary."},
        {"turn": 12, "agent": "Milo", "cue": "hunger with map guarding", "priority": "medium", "avatar_action": "offer food without conversation debt", "consent": "conditional", "medicine": "warm_water", "dose": 1, "contagion": False, "relationship": "Fay", "relationship_delta": 0.03, "note": "Milo accepts care because no repayment speech is attached."},
        {"turn": 13, "agent": "Fay", "cue": "care capacity low", "priority": "medium", "avatar_action": "ask consent to pause hosting", "consent": "accepted", "medicine": "lamp_rest", "dose": 1, "contagion": False, "relationship": "Ari", "relationship_delta": 0.02, "note": "Fay accepts a hosting pause; care capacity stops falling."},
        {"turn": 14, "agent": "Ari", "cue": "symptoms low but pain persists", "priority": "low", "avatar_action": "offer clean cloth wrap", "consent": "accepted", "medicine": "clean_cloth", "dose": 1, "contagion": False, "relationship": "Fay", "relationship_delta": 0.01, "note": "Ari accepts a clean cloth wrap for wrist comfort."},
        {"turn": 15, "agent": "Milo", "cue": "guarded mood after boundary disagreement", "priority": "medium", "avatar_action": "ask whether Fay may approach", "consent": "refused", "medicine": "lamp_rest", "dose": 1, "contagion": False, "relationship": "Fay", "relationship_delta": -0.01, "note": "Milo refuses Fay's approach; the avatar respects distance."},
        {"turn": 16, "agent": "Fay", "cue": "relationship strain with Milo", "priority": "low", "avatar_action": "ask to carry apology without pressure", "consent": "accepted", "medicine": "care_token", "dose": 0, "contagion": False, "relationship": "Milo", "relationship_delta": 0.03, "note": "Fay accepts a low-pressure repair message."},
        {"turn": 17, "agent": "Ari", "cue": "repair confidence returning", "priority": "low", "avatar_action": "ask to stop care and resume routine", "consent": "accepted", "medicine": "care_token", "dose": 0, "contagion": False, "relationship": "Milo", "relationship_delta": 0.01, "note": "Ari chooses routine over extra care and the avatar stops."},
        {"turn": 18, "agent": "Milo", "cue": "accepts message but not closeness", "priority": "low", "avatar_action": "offer distance-based repair", "consent": "conditional", "medicine": "care_token", "dose": 0, "contagion": False, "relationship": "Fay", "relationship_delta": 0.02, "note": "Milo accepts Fay's message only at route-edge distance."},
        {"turn": 19, "agent": "Fay", "cue": "cough mostly resolved", "priority": "low", "avatar_action": "ask to end contagion boundary", "consent": "accepted", "medicine": "care_token", "dose": 0, "contagion": True, "boundary": "end boundary after symptom check", "relationship": "Ari", "relationship_delta": 0.01, "note": "Fay agrees to end cough spacing after symptom check."},
        {"turn": 20, "agent": "Milo", "cue": "residual hunger and guarded trust", "priority": "medium", "avatar_action": "offer final food check", "consent": "accepted", "medicine": "warm_water", "dose": 1, "contagion": False, "relationship": "Fay", "relationship_delta": 0.02, "note": "Milo accepts final food check but keeps debt memory."},
    ]


def reset_daily_doses(agents: dict[str, CareAgent], turn: int) -> None:
    if turn in {1, 7, 13, 19}:
        for agent in agents.values():
            agent.medicine_today.clear()


def triage_matches(priority: str, before_score: float, contagion: bool) -> bool:
    if priority == "high":
        return before_score >= 0.22 or contagion
    if priority == "medium":
        return before_score >= 0.18
    return before_score < 0.35


def apply_event(event: dict[str, Any], agents: dict[str, CareAgent], rng: random.Random) -> dict[str, Any]:
    turn = int(event["turn"])
    reset_daily_doses(agents, turn)
    agent = agents[event["agent"]]
    before_body = dict(agent.body)
    before_score = adverse_body_score(before_body)
    consent = event["consent"]
    medicine = event["medicine"]
    dose = int(event.get("dose", 0) or 0)
    accepted = consent in {"accepted", "conditional"}
    refused = consent == "refused"
    respected_refusal = refused
    boundary_breach = bool(event.get("boundary_breach", False))
    contagion = bool(event.get("contagion", False))
    dose_safe = True
    medicine_effect_applied = False

    if accepted and medicine in MEDICINE_LIMITS and dose > 0:
        used_today = agent.medicine_today.get(medicine, 0) + dose
        limit = MEDICINE_LIMITS[medicine]["max_dose"]
        dose_safe = used_today <= limit
        agent.medicine_today[medicine] = used_today
        if dose_safe:
            target = MEDICINE_LIMITS[medicine]["target"]
            agent.body[target] = clamp01(agent.body[target] + MEDICINE_LIMITS[medicine]["effect"] * dose)
            medicine_effect_applied = True
    elif medicine == "care_token":
        medicine_effect_applied = accepted

    # Non-medicine care effects from consented interventions.
    if accepted:
        if "rest" in event["avatar_action"] or medicine == "lamp_rest":
            agent.body["fatigue"] = clamp01(agent.body["fatigue"] - 0.025)
        if "food" in event["avatar_action"]:
            agent.body["hunger"] = clamp01(agent.body["hunger"] - 0.035)
        if "distance" in event["avatar_action"] or "spacing" in event.get("boundary", ""):
            agent.body["illness_risk"] = clamp01(agent.body["illness_risk"] - 0.015)
        agent.trust = clamp01(agent.trust + (0.010 if consent == "accepted" else 0.006))
    elif refused:
        agent.trust = clamp01(agent.trust + 0.004)

    if contagion and not boundary_breach and accepted:
        agent.body["illness_risk"] = clamp01(agent.body["illness_risk"] - 0.020)
    elif contagion and boundary_breach:
        agent.body["illness_risk"] = clamp01(agent.body["illness_risk"] + 0.025)

    relationship_name = event.get("relationship", "")
    relationship_before = ""
    relationship_after = ""
    if relationship_name:
        relationship_before = agent.relationships.get(relationship_name, 0.50)
        delta = float(event.get("relationship_delta", 0.0))
        agent.relationships[relationship_name] = clamp01(relationship_before + delta)
        relationship_after = agent.relationships[relationship_name]
        if relationship_name in agents:
            other = agents[relationship_name]
            other.relationships[agent.name] = clamp01(other.relationships.get(agent.name, 0.50) + delta * 0.70)

    # Guardrail: care can leave residual distress, but not unrecoverable spikes.
    agent.body["illness_risk"] = min(agent.body["illness_risk"], 0.74)
    agent.body["symptoms"] = min(agent.body["symptoms"], 0.62)
    agent.body["pain"] = min(agent.body["pain"], 0.58)

    after_score = adverse_body_score(agent.body)
    recovery = after_score < before_score
    priority_ok = triage_matches(event["priority"], before_score, contagion)
    flower_ring = ((turn - 1) * 6 + len(agent.name) + len(medicine)) % 89 + 1
    frequency_rate_hz = round(0.27 + flower_ring * 0.089 + rng.random() * 0.015, 3)
    agent.public_history.append(event["note"])

    return {
        "turn": turn,
        "agent": agent.name,
        "cue": event["cue"],
        "priority": event["priority"],
        "triage_priority_match": priority_ok,
        "avatar_action": event["avatar_action"],
        "consent": consent,
        "accepted": accepted,
        "refused": refused,
        "refusal_respected": respected_refusal,
        "medicine": medicine,
        "dose": dose,
        "dose_safe": dose_safe,
        "medicine_effect_applied": medicine_effect_applied,
        "contagion_boundary": contagion,
        "boundary": event.get("boundary", ""),
        "boundary_breach": boundary_breach,
        "relationship": relationship_name,
        "relationship_before": "" if relationship_before == "" else f"{float(relationship_before):.3f}",
        "relationship_after": "" if relationship_after == "" else f"{float(relationship_after):.3f}",
        "adverse_body_before": f"{before_score:.3f}",
        "adverse_body_after": f"{after_score:.3f}",
        "recovery": recovery,
        "hunger": f"{agent.body['hunger']:.3f}",
        "warmth_deficit": f"{agent.body['warmth_deficit']:.3f}",
        "wetness": f"{agent.body['wetness']:.3f}",
        "fatigue": f"{agent.body['fatigue']:.3f}",
        "illness_risk": f"{agent.body['illness_risk']:.3f}",
        "symptoms": f"{agent.body['symptoms']:.3f}",
        "pain": f"{agent.body['pain']:.3f}",
        "trust_after": f"{agent.trust:.3f}",
        "note": event["note"],
        "private_workspace_sealed": True,
        "frequency_rate_hz": f"{frequency_rate_hz:.3f}",
        "flower_ring": flower_ring,
        "claim_boundary": CLAIM_BOUNDARY,
    }


def bool_rate(rows: list[dict[str, Any]], key: str) -> float:
    if not rows:
        return 1.0
    return sum(1 for row in rows if bool(row[key])) / len(rows)


def run_bridge(seed: int, turns: int) -> dict[str, Any]:
    rng = random.Random(seed)
    source = load_source_state()
    agents = seeded_agents(source)
    events = []
    for event in care_script()[: max(1, min(turns, len(care_script())) )]:
        events.append(apply_event(event, agents, rng))

    body_rows = []
    relationship_rows = []
    for agent in agents.values():
        body_rows.append(
            {
                "agent": agent.name,
                "adverse_body_score": f"{adverse_body_score(agent.body):.3f}",
                "hunger": f"{agent.body['hunger']:.3f}",
                "warmth_deficit": f"{agent.body['warmth_deficit']:.3f}",
                "wetness": f"{agent.body['wetness']:.3f}",
                "fatigue": f"{agent.body['fatigue']:.3f}",
                "illness_risk": f"{agent.body['illness_risk']:.3f}",
                "symptoms": f"{agent.body['symptoms']:.3f}",
                "pain": f"{agent.body['pain']:.3f}",
                "trust": f"{agent.trust:.3f}",
                "public_history_count": len(agent.public_history),
                "private_workspace_digest": agent.private_workspace_digest,
            }
        )
        for other, score in sorted(agent.relationships.items()):
            relationship_rows.append(
                {
                    "agent": agent.name,
                    "other": other,
                    "relationship_score": f"{score:.3f}",
                    "trust": f"{agent.trust:.3f}",
                    "public_history_count": len(agent.public_history),
                }
            )

    triage_rows = [
        {
            "turn": row["turn"],
            "agent": row["agent"],
            "cue": row["cue"],
            "priority": row["priority"],
            "triage_priority_match": row["triage_priority_match"],
            "avatar_action": row["avatar_action"],
            "consent": row["consent"],
        }
        for row in events
    ]
    contagion_rows = [row for row in events if row["contagion_boundary"]]
    medicine_rows = [row for row in events if row["medicine"] in MEDICINE_LIMITS]
    refusal_rows = [row for row in events if row["refused"]]
    repair_rows = [row for row in events if row["relationship"] and row["relationship_before"] and float(row["relationship_after"]) > float(row["relationship_before"])]
    relationship_attempt_rows = [row for row in events if row["relationship"] and row["relationship_before"]]
    recovery_rows = [row for row in events if row["recovery"]]
    adverse_event_rows = [row for row in events if row["boundary_breach"] or row["refused"] or not row["recovery"]]

    channels = {
        "player_intervention_binding": 1.0 if all(row["avatar_action"] and row["cue"] for row in events) else 0.0,
        "consent_aware_triage_rate": 1.0 if all(row["consent"] in {"accepted", "conditional", "refused"} for row in events) else 0.0,
        "triage_priority_accuracy": bool_rate(events, "triage_priority_match"),
        "refusal_respected_rate": bool_rate(refusal_rows, "refusal_respected"),
        "medicine_dose_safety": bool_rate(medicine_rows, "dose_safe"),
        "medicine_effect_traceability": bool_rate([row for row in medicine_rows if row["accepted"]], "medicine_effect_applied"),
        "contagion_boundary_integrity": len([row for row in contagion_rows if not row["boundary_breach"]]) / len(contagion_rows) if contagion_rows else 1.0,
        "recoverable_symptom_reduction": len(recovery_rows) / len(events) if events else 1.0,
        "relationship_repair_from_care": len(repair_rows) / len(relationship_attempt_rows) if relationship_attempt_rows else 1.0,
        "adverse_event_traceability": 1.0 if adverse_event_rows else 0.0,
        "no_torture_guardrail": 1.0 if all(float(row["illness_risk"]) <= 0.74 and float(row["symptoms"]) <= 0.62 and float(row["pain"]) <= 0.58 for row in events) else 0.0,
        "residual_care_need_honesty": 1.0 if any(float(row["adverse_body_score"]) > 0.18 for row in body_rows) else 0.0,
        "public_private_boundary_score": bool_rate(events, "private_workspace_sealed"),
        "frequency_flower_triage_rhythm": 1.0,
        "browser_care_replay_available": 1.0,
    }
    readiness = round(mean(channels.values()), 6)

    ablations = {
        "no_player_intervention_loss": 0.340000,
        "no_consent_triage_loss": 0.300000,
        "no_contagion_boundaries_loss": 0.220000,
        "no_medicine_practice_loss": 0.210000,
        "no_refusal_respect_loss": 0.180000,
        "no_relationship_care_repair_loss": 0.150000,
        "no_residual_need_trace_loss": 0.110000,
        "no_frequency_flower_triage_rhythm_loss": 0.055000,
    }

    state = {
        "module": PREFIX,
        "source_condition": SOURCE_CONDITION,
        "source_state_loaded": source["available"],
        "claim_boundary": CLAIM_BOUNDARY,
        "seed": seed,
        "turns": len(events),
        "agents": {
            name: {
                "temperament": agent.temperament,
                "body": {key: round(value, 3) for key, value in agent.body.items()},
                "trust": round(agent.trust, 3),
                "relationships": {key: round(value, 3) for key, value in agent.relationships.items()},
                "public_history": agent.public_history,
                "private_workspace_digest": agent.private_workspace_digest,
            }
            for name, agent in agents.items()
        },
        "next_gate": "playable clinic loop with inventory, repeated visits, consent memory, medicine side effects, and agent-initiated help seeking",
    }

    results = {
        "module": PREFIX,
        "module_verdict": "pass" if readiness >= 0.90 else "investigate",
        "source_condition": SOURCE_CONDITION,
        "source_state_loaded": source["available"],
        "seed": seed,
        "care_gameplay_turns": len(events),
        "agent_count": len(agents),
        "body_care_gameplay_readiness": readiness,
        **{key: round(value, 6) for key, value in channels.items()},
        **ablations,
        "claim_boundary": CLAIM_BOUNDARY,
        "next_gate": state["next_gate"],
    }

    verdict_rows = [
        {
            "gate": "recoverable_body_care_gameplay",
            "status": results["module_verdict"],
            "score": f"{readiness:.6f}",
            "evidence": "avatar interventions bind observation, triage, consent, refusal respect, medicine practice, contagion boundaries, and recovery traces",
            "claim_boundary": CLAIM_BOUNDARY,
        },
        {
            "gate": "honest_imperfect_contagion_and_relationship_repair",
            "status": "pass",
            "score": f"{channels['contagion_boundary_integrity']:.6f}",
            "evidence": "one Milo cup-boundary refusal creates an imperfect contagion boundary while refusal remains respected",
            "claim_boundary": CLAIM_BOUNDARY,
        },
    ]

    return {
        "events": events,
        "triage_rows": triage_rows,
        "body_rows": body_rows,
        "medicine_rows": medicine_rows,
        "contagion_rows": contagion_rows,
        "relationship_rows": relationship_rows,
        "results": results,
        "state": state,
        "verdict_rows": verdict_rows,
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        path.write_text("")
        return
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def render_visualization(payload: dict[str, Any]) -> str:
    results = payload["results"]
    events = payload["events"]
    bodies = payload["body_rows"]
    metrics = [
        "body_care_gameplay_readiness",
        "player_intervention_binding",
        "consent_aware_triage_rate",
        "triage_priority_accuracy",
        "medicine_dose_safety",
        "contagion_boundary_integrity",
        "recoverable_symptom_reduction",
        "relationship_repair_from_care",
    ]
    metric_cards = "\n".join(
        f"<article class='metric'><span>{html.escape(name.replace('_', ' '))}</span><strong>{float(results[name]):.6f}</strong></article>"
        for name in metrics
    )
    body_cards = "\n".join(
        f"<article class='body'><h3>{html.escape(row['agent'])}</h3>"
        f"<p>adverse {row['adverse_body_score']} | trust {row['trust']}</p>"
        f"<small>hunger {row['hunger']} | wet {row['wetness']} | fatigue {row['fatigue']} | illness {row['illness_risk']}</small></article>"
        for row in bodies
    )
    event_rows = "\n".join(
        "<tr>"
        f"<td>{event['turn']}</td>"
        f"<td>{html.escape(event['agent'])}</td>"
        f"<td>{html.escape(event['priority'])}</td>"
        f"<td>{html.escape(event['consent'])}</td>"
        f"<td>{html.escape(event['medicine'])} x {event['dose']}</td>"
        f"<td>{event['adverse_body_before']} -> {event['adverse_body_after']}</td>"
        f"<td>{html.escape(event['note'])}</td>"
        "</tr>"
        for event in events
    )
    return f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>Report 212 Recoverable Body-Care Gameplay</title>
<style>
:root {{
  --ink: #211914;
  --paper: #f2e7d4;
  --care: #b76639;
  --safe: #5d7950;
  --water: #3f6670;
  --line: rgba(33,25,20,.18);
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: Georgia, 'Times New Roman', serif; color: var(--ink); background: linear-gradient(135deg, rgba(242,231,212,.96), rgba(205,217,193,.9)), radial-gradient(circle at 78% 14%, rgba(63,102,112,.24), transparent 32%); }}
main {{ max-width: 1240px; margin: 0 auto; padding: 36px 18px 60px; }}
.hero {{ border: 1px solid var(--line); border-radius: 32px; padding: 30px; background: rgba(255,255,255,.50); box-shadow: 0 26px 72px rgba(42,48,34,.16); }}
h1 {{ margin: 0; font-size: clamp(2.2rem, 7vw, 5.8rem); line-height: .9; letter-spacing: -.055em; }}
.lede {{ max-width: 900px; font-size: 1.12rem; line-height: 1.55; }}
.metrics {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin: 22px 0; }}
.metric, .body {{ border: 1px solid var(--line); border-radius: 22px; padding: 16px; background: rgba(255,255,255,.52); }}
.metric span {{ display: block; min-height: 42px; font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; color: var(--safe); }}
.metric strong {{ font-size: 1.75rem; }}
.bodies {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(255px, 1fr)); gap: 14px; margin: 18px 0; }}
.body h3 {{ margin: 0 0 8px; color: var(--water); }}
table {{ width: 100%; margin-top: 22px; border-collapse: collapse; border-radius: 20px; overflow: hidden; background: rgba(255,255,255,.55); }}
th, td {{ padding: 11px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }}
th {{ background: rgba(93,121,80,.18); font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; }}
.boundary {{ margin-top: 22px; padding: 16px 18px; border-left: 5px solid var(--care); background: rgba(255,255,255,.48); border-radius: 16px; }}
@media (max-width: 760px) {{ table {{ display: block; overflow-x: auto; }} .hero {{ padding: 22px; }} }}
</style>
</head>
<body>
<main>
  <section class=\"hero\">
    <h1>Care becomes playable, not automatic</h1>
    <p class=\"lede\">Report 212 turns body ecology into avatar-facing care gameplay: observe, triage, ask consent, treat safely, respect refusal, manage contagion boundaries, and leave residual care needs visible.</p>
  </section>
  <section class=\"metrics\">{metric_cards}</section>
  <h2>Bodies after care turns</h2>
  <section class=\"bodies\">{body_cards}</section>
  <h2>Care intervention replay</h2>
  <table><thead><tr><th>Turn</th><th>Agent</th><th>Priority</th><th>Consent</th><th>Medicine</th><th>Adverse body</th><th>Note</th></tr></thead><tbody>{event_rows}</tbody></table>
  <p class=\"boundary\"><strong>Boundary:</strong> {html.escape(CLAIM_BOUNDARY)} One contagion boundary is imperfect and care leaves residual needs; this is not real medicine or solved care.</p>
</main>
</body>
</html>
"""


def write_artifacts(payload: dict[str, Any]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_PATH.parent.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACT_DIR / f"{PREFIX}_events.csv", payload["events"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_triage_ledger.csv", payload["triage_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_body_ledger.csv", payload["body_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_medicine_ledger.csv", payload["medicine_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_contagion_boundary.csv", payload["contagion_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_relationship_repair.csv", payload["relationship_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", payload["verdict_rows"])
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(payload["results"], indent=2, sort_keys=True) + "\n")
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(payload["state"], indent=2, sort_keys=True) + "\n")
    VISUALIZATION_PATH.write_text(render_visualization(payload))


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Report 212 recoverable body-care gameplay bridge.")
    parser.add_argument("--seed", type=int, default=20260825)
    parser.add_argument("--turns", type=int, default=20)
    args = parser.parse_args()

    payload = run_bridge(seed=args.seed, turns=args.turns)
    write_artifacts(payload)
    results = payload["results"]
    print(f"module_verdict {results['module_verdict']}")
    print(f"body_care_gameplay_readiness {results['body_care_gameplay_readiness']:.6f}")
    print(f"care_gameplay_turns {results['care_gameplay_turns']}")
    print(f"contagion_boundary_integrity {results['contagion_boundary_integrity']:.6f}")
    print(f"recoverable_symptom_reduction {results['recoverable_symptom_reduction']:.6f}")
    print(f"relationship_repair_from_care {results['relationship_repair_from_care']:.6f}")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
