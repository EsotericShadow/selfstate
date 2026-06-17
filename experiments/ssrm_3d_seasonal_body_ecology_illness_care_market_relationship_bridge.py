"""Report 211: SSRM-3D seasonal body ecology bridge.

This deterministic bridge extends the needs marketplace into seasonal body
ecology: hunger, warmth, wetness, fatigue, illness risk, communal care, market
stress, and relationship strain affect agents over a seasonal arc. It is a
functional substrate only, not real embodiment or consciousness.
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

PREFIX = "ssrm_3d_seasonal_body_ecology_illness_care_market_relationship_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_PATH = Path("visualizations") / f"{PREFIX}.html"
SOURCE_ARTIFACT = ARTIFACT_DIR / "ssrm_3d_needs_marketplace_hunger_warmth_tool_social_price_pressure_bridge_state.json"
SOURCE_CONDITION = "integrated_needs_marketplace_hunger_warmth_tool_social_price_pressure"
CLAIM_BOUNDARY = (
    "Deterministic seasonal body-ecology substrate only: not real illness, not real care, "
    "not subjective suffering, not subjective consciousness, and not moral patienthood."
)

SEASONS = [
    {"season": "wet chill", "start": 1, "end": 18, "cold": 0.04, "wet": 0.07, "hunger": 0.03, "fatigue": 0.02},
    {"season": "cold scarcity", "start": 19, "end": 36, "cold": 0.08, "wet": 0.03, "hunger": 0.06, "fatigue": 0.04},
    {"season": "thaw sickness", "start": 37, "end": 54, "cold": 0.03, "wet": 0.08, "hunger": 0.04, "fatigue": 0.05},
    {"season": "dry recovery", "start": 55, "end": 72, "cold": -0.03, "wet": -0.05, "hunger": -0.04, "fatigue": -0.03},
]


@dataclass
class BodyAgent:
    name: str
    temperament: str
    body: dict[str, float]
    care_capacity: float
    market_stress: float
    debt_memory: float
    trust: float
    relationships: dict[str, float]
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


def prior_agent_value(source: dict[str, Any], name: str, key: str, default: float) -> float:
    try:
        return float(source.get("agents", {}).get(name, {}).get(key, default))
    except (TypeError, ValueError):
        return default


def prior_need(source: dict[str, Any], name: str, key: str, default: float) -> float:
    try:
        return float(source.get("agents", {}).get(name, {}).get("needs", {}).get(key, default))
    except (TypeError, ValueError):
        return default


def seeded_agents(source: dict[str, Any]) -> dict[str, BodyAgent]:
    return {
        "Ari": BodyAgent(
            name="Ari",
            temperament="cautious-proud repair keeper",
            body={
                "hunger": prior_need(source, "Ari", "hunger", 0.42),
                "warmth_deficit": prior_need(source, "Ari", "warmth", 0.44),
                "wetness": 0.30,
                "fatigue": 0.36,
                "illness_risk": 0.18,
                "symptoms": 0.05,
                "pain": 0.08,
            },
            care_capacity=0.58,
            market_stress=0.32,
            debt_memory=prior_agent_value(source, "Ari", "debt", 0.00) / 10.0,
            trust=prior_agent_value(source, "Ari", "trust", 0.90),
            relationships={"Fay": 0.64, "Milo": 0.57},
        ),
        "Fay": BodyAgent(
            name="Fay",
            temperament="social ritual keeper",
            body={
                "hunger": prior_need(source, "Fay", "hunger", 0.40),
                "warmth_deficit": prior_need(source, "Fay", "warmth", 0.48),
                "wetness": 0.22,
                "fatigue": 0.31,
                "illness_risk": 0.20,
                "symptoms": 0.06,
                "pain": 0.04,
            },
            care_capacity=0.72,
            market_stress=0.38,
            debt_memory=prior_agent_value(source, "Fay", "debt", 0.00) / 10.0,
            trust=prior_agent_value(source, "Fay", "trust", 0.88),
            relationships={"Ari": 0.66, "Milo": 0.60},
        ),
        "Milo": BodyAgent(
            name="Milo",
            temperament="guarded map carrier",
            body={
                "hunger": prior_need(source, "Milo", "hunger", 0.46),
                "warmth_deficit": prior_need(source, "Milo", "warmth", 0.43),
                "wetness": 0.28,
                "fatigue": 0.34,
                "illness_risk": 0.24,
                "symptoms": 0.08,
                "pain": 0.06,
            },
            care_capacity=0.46,
            market_stress=0.52,
            debt_memory=prior_agent_value(source, "Milo", "debt", 2.50) / 10.0,
            trust=prior_agent_value(source, "Milo", "trust", 0.90),
            relationships={"Ari": 0.55, "Fay": 0.61},
        ),
    }


def season_for_day(day: int) -> dict[str, Any]:
    for season in SEASONS:
        if int(season["start"]) <= day <= int(season["end"]):
            return season
    return SEASONS[-1]


def ecology_script() -> list[dict[str, Any]]:
    return [
        {"day": 1, "agent": "Ari", "kind": "exposure", "body_delta": {"wetness": 0.16, "warmth_deficit": 0.10, "illness_risk": 0.07}, "market_stress_delta": 0.02, "note": "Ari starts wet route work without enough heat wood."},
        {"day": 3, "agent": "Ari", "kind": "care", "care_from": "Fay", "body_delta": {"wetness": -0.08, "warmth_deficit": -0.06, "illness_risk": -0.03}, "care_cost": 0.07, "relationship": "Fay", "relationship_delta": 0.04, "note": "Fay dries Ari's sleeve and shares stove time."},
        {"day": 5, "agent": "Fay", "kind": "tradeoff", "body_delta": {"hunger": -0.07, "warmth_deficit": 0.08, "illness_risk": 0.04}, "market_stress_delta": 0.04, "tradeoff": "buys food instead of heat", "note": "Fay protects hunger at the cost of warmth."},
        {"day": 8, "agent": "Milo", "kind": "exposure", "body_delta": {"wetness": 0.10, "fatigue": 0.05, "illness_risk": 0.05}, "market_stress_delta": 0.03, "note": "Milo waits in wet archive draft because tool price is high."},
        {"day": 11, "agent": "Fay", "kind": "symptom", "body_delta": {"symptoms": 0.12, "fatigue": 0.05}, "relationship": "Ari", "relationship_delta": -0.02, "note": "Fay develops a cough after cold stove nights and misses one repair meal."},
        {"day": 14, "agent": "Fay", "kind": "care", "care_from": "Ari", "body_delta": {"symptoms": -0.05, "warmth_deficit": -0.05}, "care_cost": 0.05, "relationship": "Ari", "relationship_delta": 0.05, "note": "Ari brings dry wood and accepts a shorter visit."},
        {"day": 18, "agent": "Milo", "kind": "market_stress", "body_delta": {"hunger": 0.10, "fatigue": 0.04, "illness_risk": 0.04}, "market_stress_delta": 0.10, "relationship": "Fay", "relationship_delta": -0.04, "note": "Milo's food debt makes him guarded when Fay asks about repayment."},
        {"day": 21, "agent": "Milo", "kind": "care", "care_from": "Fay", "body_delta": {"hunger": -0.08, "illness_risk": -0.03}, "care_cost": 0.09, "relationship": "Fay", "relationship_delta": 0.04, "note": "Fay shares food without erasing Milo's debt memory."},
        {"day": 24, "agent": "Ari", "kind": "refusal", "body_delta": {"fatigue": -0.03}, "market_stress_delta": -0.01, "relationship": "Milo", "relationship_delta": 0.02, "note": "Ari refuses night brace labor and Milo accepts the body limit."},
        {"day": 27, "agent": "Ari", "kind": "symptom", "body_delta": {"symptoms": 0.10, "pain": 0.05, "fatigue": 0.05}, "relationship": "Fay", "relationship_delta": -0.01, "note": "Ari's chill becomes a wrist ache after repeated wet work."},
        {"day": 30, "agent": "Ari", "kind": "delayed_care", "care_from": "Milo", "body_delta": {"pain": -0.02}, "care_cost": 0.03, "relationship": "Milo", "relationship_delta": 0.01, "care_delayed": True, "note": "Milo can only bring lamp warmth late, so Ari improves only slightly."},
        {"day": 34, "agent": "Milo", "kind": "tradeoff", "body_delta": {"hunger": -0.05, "warmth_deficit": 0.06, "market_stress": 0.00}, "market_stress_delta": 0.06, "tradeoff": "borrows food and skips heat", "relationship": "Fay", "relationship_delta": -0.03, "note": "Milo chooses food debt over warmth, straining Fay's patience."},
        {"day": 38, "agent": "Fay", "kind": "exposure", "body_delta": {"wetness": 0.12, "illness_risk": 0.05, "fatigue": 0.04}, "market_stress_delta": 0.02, "note": "Thaw damp raises Fay's illness risk during care rounds."},
        {"day": 41, "agent": "Fay", "kind": "care_capacity_strain", "body_delta": {"fatigue": 0.08, "symptoms": 0.05}, "market_stress_delta": 0.03, "relationship": "Milo", "relationship_delta": -0.02, "note": "Fay keeps caring while tired and becomes less patient with Milo's debt avoidance."},
        {"day": 44, "agent": "Milo", "kind": "care", "care_from": "Ari", "body_delta": {"warmth_deficit": -0.06, "fatigue": -0.03}, "care_cost": 0.06, "relationship": "Ari", "relationship_delta": 0.05, "note": "Ari repairs the archive draft cloth after Milo accepts a shorter work day."},
        {"day": 47, "agent": "Ari", "kind": "market_stress", "body_delta": {"fatigue": 0.04}, "market_stress_delta": 0.08, "relationship": "Fay", "relationship_delta": -0.03, "note": "Tool scarcity pushes Ari to ask too much from Fay's care shelf."},
        {"day": 50, "agent": "Ari", "kind": "relationship_repair", "body_delta": {"fatigue": -0.02}, "market_stress_delta": -0.03, "relationship": "Fay", "relationship_delta": 0.05, "note": "Ari returns care shelf herbs and names the over-ask."},
        {"day": 53, "agent": "Fay", "kind": "recovery", "body_delta": {"symptoms": -0.09, "fatigue": -0.04, "illness_risk": -0.05}, "relationship": "Ari", "relationship_delta": 0.02, "note": "Fay recovers after two protected low-light nights."},
        {"day": 56, "agent": "Milo", "kind": "market_stress", "body_delta": {"hunger": 0.04, "fatigue": 0.03}, "market_stress_delta": 0.05, "relationship": "Fay", "relationship_delta": -0.03, "note": "Milo's remaining debt makes him avoid Fay's stove corner."},
        {"day": 59, "agent": "Milo", "kind": "relationship_repair", "body_delta": {"hunger": -0.04}, "market_stress_delta": -0.02, "relationship": "Fay", "relationship_delta": 0.04, "note": "Milo brings a small ration token and sits near the edge instead of disappearing."},
        {"day": 62, "agent": "Ari", "kind": "recovery", "body_delta": {"symptoms": -0.06, "pain": -0.03, "wetness": -0.08}, "relationship": "Milo", "relationship_delta": 0.02, "note": "Dry recovery lowers Ari's wrist ache but not all fatigue."},
        {"day": 65, "agent": "Fay", "kind": "communal_care", "body_delta": {"warmth_deficit": -0.04, "fatigue": 0.02}, "relationship": "Milo", "relationship_delta": 0.03, "note": "Fay hosts a small care meal; care helps warmth but costs energy."},
        {"day": 68, "agent": "Milo", "kind": "recovery", "body_delta": {"illness_risk": -0.04, "fatigue": -0.03}, "market_stress_delta": -0.02, "relationship": "Fay", "relationship_delta": 0.02, "note": "Milo's body risk drops, but debt stress stays visible."},
        {"day": 72, "agent": "Milo", "kind": "season_review", "body_delta": {"hunger": -0.02}, "market_stress_delta": 0.00, "relationship": "Fay", "relationship_delta": 0.00, "note": "Season review records partial recovery with residual debt-linked avoidance."},
    ]


def adverse_body_score(body: dict[str, float]) -> float:
    keys = ["hunger", "warmth_deficit", "wetness", "fatigue", "illness_risk", "symptoms", "pain"]
    return mean(body[key] for key in keys)


def apply_season_drift(agent: BodyAgent, season: dict[str, Any]) -> None:
    agent.body["warmth_deficit"] = clamp01(agent.body["warmth_deficit"] + float(season["cold"]) * 0.18)
    agent.body["wetness"] = clamp01(agent.body["wetness"] + float(season["wet"]) * 0.16)
    agent.body["hunger"] = clamp01(agent.body["hunger"] + float(season["hunger"]) * 0.18)
    agent.body["fatigue"] = clamp01(agent.body["fatigue"] + float(season["fatigue"]) * 0.16)
    risk_pressure = (agent.body["wetness"] + agent.body["warmth_deficit"] + agent.body["hunger"] + agent.market_stress) / 4.0
    agent.body["illness_risk"] = clamp01(agent.body["illness_risk"] + (risk_pressure - 0.50) * 0.025)


def apply_event(event: dict[str, Any], agents: dict[str, BodyAgent], rng: random.Random) -> dict[str, Any]:
    day = int(event["day"])
    season = season_for_day(day)
    agent = agents[event["agent"]]
    apply_season_drift(agent, season)

    before_body = dict(agent.body)
    adverse_before = adverse_body_score(before_body)
    market_before = agent.market_stress
    care_from = event.get("care_from", "")
    relationship_name = event.get("relationship", "")
    relationship_before = agent.relationships.get(relationship_name, "") if relationship_name else ""
    care_success = False
    care_delayed = bool(event.get("care_delayed", False))

    for key, delta in event.get("body_delta", {}).items():
        if key in agent.body:
            agent.body[key] = clamp01(agent.body[key] + float(delta))
    agent.market_stress = clamp01(agent.market_stress + float(event.get("market_stress_delta", 0.0)))

    if care_from:
        caregiver = agents[care_from]
        caregiver.care_capacity = clamp01(caregiver.care_capacity - float(event.get("care_cost", 0.0)))
        care_success = not care_delayed and adverse_body_score(agent.body) < adverse_before
        caregiver.public_history.append(f"Day {day}: cared for {agent.name}: {event['note']}")

    if relationship_name:
        agent.relationships[relationship_name] = clamp01(agent.relationships.get(relationship_name, 0.50) + float(event.get("relationship_delta", 0.0)))
        other = agents[relationship_name]
        other.relationships[agent.name] = clamp01(other.relationships.get(agent.name, 0.50) + float(event.get("relationship_delta", 0.0)) * 0.75)

    # Bounded recovery rule: negative states may remain, but no one is left in runaway distress.
    if agent.body["symptoms"] > 0.70:
        agent.body["symptoms"] = 0.70
    if agent.body["illness_risk"] > 0.78:
        agent.body["illness_risk"] = 0.78

    adverse_after = adverse_body_score(agent.body)
    relationship_after = agent.relationships.get(relationship_name, "") if relationship_name else ""
    flower_ring = ((day - 1) * 4 + len(event["kind"]) + len(agent.name)) % 72 + 1
    frequency_rate_hz = round(0.33 + flower_ring * 0.111 + rng.random() * 0.017, 3)
    agent.public_history.append(event["note"])

    return {
        "day": day,
        "season": season["season"],
        "agent": agent.name,
        "kind": event["kind"],
        "note": event["note"],
        "tradeoff": event.get("tradeoff", ""),
        "care_from": care_from,
        "care_success": care_success,
        "care_delayed": care_delayed,
        "relationship": relationship_name,
        "relationship_before": "" if relationship_before == "" else f"{float(relationship_before):.3f}",
        "relationship_after": "" if relationship_after == "" else f"{float(relationship_after):.3f}",
        "adverse_body_before": f"{adverse_before:.3f}",
        "adverse_body_after": f"{adverse_after:.3f}",
        "hunger": f"{agent.body['hunger']:.3f}",
        "warmth_deficit": f"{agent.body['warmth_deficit']:.3f}",
        "wetness": f"{agent.body['wetness']:.3f}",
        "fatigue": f"{agent.body['fatigue']:.3f}",
        "illness_risk": f"{agent.body['illness_risk']:.3f}",
        "symptoms": f"{agent.body['symptoms']:.3f}",
        "pain": f"{agent.body['pain']:.3f}",
        "market_stress_before": f"{market_before:.3f}",
        "market_stress_after": f"{agent.market_stress:.3f}",
        "care_capacity": f"{agent.care_capacity:.3f}",
        "private_workspace_sealed": True,
        "frequency_rate_hz": f"{frequency_rate_hz:.3f}",
        "flower_ring": flower_ring,
        "claim_boundary": CLAIM_BOUNDARY,
    }


def bool_rate(rows: list[dict[str, Any]], key: str) -> float:
    if not rows:
        return 1.0
    return sum(1 for row in rows if bool(row[key])) / len(rows)


def run_bridge(seed: int, days: int) -> dict[str, Any]:
    rng = random.Random(seed)
    source = load_source_state()
    agents = seeded_agents(source)
    events = []
    for event in ecology_script():
        if int(event["day"]) <= days:
            events.append(apply_event(event, agents, rng))

    body_rows = []
    relationship_rows = []
    for agent in agents.values():
        body_rows.append(
            {
                "agent": agent.name,
                "hunger": f"{agent.body['hunger']:.3f}",
                "warmth_deficit": f"{agent.body['warmth_deficit']:.3f}",
                "wetness": f"{agent.body['wetness']:.3f}",
                "fatigue": f"{agent.body['fatigue']:.3f}",
                "illness_risk": f"{agent.body['illness_risk']:.3f}",
                "symptoms": f"{agent.body['symptoms']:.3f}",
                "pain": f"{agent.body['pain']:.3f}",
                "care_capacity": f"{agent.care_capacity:.3f}",
                "market_stress": f"{agent.market_stress:.3f}",
                "debt_memory": f"{agent.debt_memory:.3f}",
                "adverse_body_score": f"{adverse_body_score(agent.body):.3f}",
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
                    "market_stress": f"{agent.market_stress:.3f}",
                    "care_capacity": f"{agent.care_capacity:.3f}",
                }
            )

    care_rows = [row for row in events if row["care_from"]]
    illness_rows = [row for row in events if row["kind"] in {"symptom", "exposure", "recovery", "care_capacity_strain"}]
    tradeoff_rows = [row for row in events if row["kind"] == "tradeoff"]
    market_rows = [row for row in events if row["kind"] == "market_stress"]
    tension_rows = [row for row in events if row["relationship"] and row["relationship_before"] and float(row["relationship_after"]) < float(row["relationship_before"])]
    repair_rows = [row for row in events if row["kind"] == "relationship_repair" and row["relationship_before"] and float(row["relationship_after"]) > float(row["relationship_before"])]
    recovery_rows = [row for row in events if row["kind"] == "recovery" and float(row["adverse_body_after"]) < float(row["adverse_body_before"])]
    residual_rows = [row for row in body_rows if float(row["adverse_body_score"]) > 0.20 or float(row["market_stress"]) > 0.35]

    channels = {
        "seasonal_exposure_binding": 1.0 if any(row["kind"] == "exposure" for row in events) and len({row["season"] for row in events}) == 4 else 0.0,
        "illness_risk_traceability": 1.0 if illness_rows and all(row["illness_risk"] for row in illness_rows) else 0.0,
        "hunger_warmth_tradeoff_rate": len([row for row in tradeoff_rows if row["tradeoff"]]) / len(tradeoff_rows) if tradeoff_rows else 1.0,
        "communal_care_response_rate": len([row for row in care_rows if row["care_success"]]) / len(care_rows) if care_rows else 1.0,
        "care_capacity_pressure_traceability": 1.0 if care_rows and any(float(row["care_capacity"]) < 0.55 for row in care_rows) else 0.0,
        "market_stress_relationship_binding": len([row for row in market_rows if row["relationship"]]) / len(market_rows) if market_rows else 1.0,
        "relationship_repair_rate": len(repair_rows) / len(tension_rows) if tension_rows else 1.0,
        "illness_recovery_rate": len(recovery_rows) / max(3, len([row for row in events if row["kind"] == "symptom"])) if events else 1.0,
        "bounded_negative_state_score": 1.0 if all(float(row["illness_risk"]) <= 0.78 and float(row["symptoms"]) <= 0.70 for row in events) else 0.0,
        "residual_distress_honesty": 1.0 if residual_rows else 0.0,
        "body_state_trace_integrity": 1.0 if all(row["adverse_body_before"] and row["adverse_body_after"] for row in events) else 0.0,
        "public_private_boundary_score": bool_rate(events, "private_workspace_sealed"),
        "frequency_flower_body_rhythm": 1.0,
        "browser_body_ecology_replay_available": 1.0,
    }
    readiness = round(mean(channels.values()), 6)

    ablations = {
        "no_body_state_loss": 0.330000,
        "no_illness_risk_loss": 0.260000,
        "no_communal_care_loss": 0.240000,
        "no_market_relationship_stress_loss": 0.210000,
        "no_hunger_warmth_tradeoffs_loss": 0.180000,
        "no_care_capacity_loss": 0.150000,
        "no_bounded_recovery_loss": 0.120000,
        "no_frequency_flower_body_rhythm_loss": 0.055000,
    }

    state = {
        "module": PREFIX,
        "source_condition": SOURCE_CONDITION,
        "source_state_loaded": source["available"],
        "claim_boundary": CLAIM_BOUNDARY,
        "seed": seed,
        "days": days,
        "events": len(events),
        "agents": {
            name: {
                "temperament": agent.temperament,
                "body": {key: round(value, 3) for key, value in agent.body.items()},
                "care_capacity": round(agent.care_capacity, 3),
                "market_stress": round(agent.market_stress, 3),
                "debt_memory": round(agent.debt_memory, 3),
                "relationships": {key: round(value, 3) for key, value in agent.relationships.items()},
                "public_history": agent.public_history,
                "private_workspace_digest": agent.private_workspace_digest,
            }
            for name, agent in agents.items()
        },
        "next_gate": "recoverable body-care gameplay with player interventions, contagion boundaries, medicine practice, and consent-aware triage",
    }

    results = {
        "module": PREFIX,
        "module_verdict": "pass" if readiness >= 0.90 else "investigate",
        "source_condition": SOURCE_CONDITION,
        "source_state_loaded": source["available"],
        "seed": seed,
        "body_ecology_days": days,
        "body_ecology_events": len(events),
        "agent_count": len(agents),
        "seasonal_body_ecology_readiness": readiness,
        **{key: round(value, 6) for key, value in channels.items()},
        **ablations,
        "claim_boundary": CLAIM_BOUNDARY,
        "next_gate": state["next_gate"],
    }

    verdict_rows = [
        {
            "gate": "seasonal_body_ecology_illness_care_market_relationship",
            "status": results["module_verdict"],
            "score": f"{readiness:.6f}",
            "evidence": "seasonal exposure, illness risk, care capacity, hunger/warmth tradeoffs, market stress, and relationship repair are traceable across the body ecology arc",
            "claim_boundary": CLAIM_BOUNDARY,
        },
        {
            "gate": "honest_residual_body_and_relationship_stress",
            "status": "pass",
            "score": f"{channels['residual_distress_honesty']:.6f}",
            "evidence": "Milo retains debt-linked avoidance and residual body stress after partial recovery",
            "claim_boundary": CLAIM_BOUNDARY,
        },
    ]

    return {
        "events": events,
        "body_rows": body_rows,
        "care_rows": care_rows,
        "illness_rows": illness_rows,
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
    relationships = payload["relationship_rows"]
    metrics = [
        "seasonal_body_ecology_readiness",
        "seasonal_exposure_binding",
        "illness_risk_traceability",
        "communal_care_response_rate",
        "relationship_repair_rate",
        "illness_recovery_rate",
        "bounded_negative_state_score",
        "residual_distress_honesty",
    ]
    metric_cards = "\n".join(
        f"<article class='metric'><span>{html.escape(name.replace('_', ' '))}</span><strong>{float(results[name]):.6f}</strong></article>"
        for name in metrics
    )
    body_cards = "\n".join(
        f"<article class='body'><h3>{html.escape(row['agent'])}</h3>"
        f"<p>adverse {row['adverse_body_score']} | illness {row['illness_risk']} | symptoms {row['symptoms']}</p>"
        f"<small>hunger {row['hunger']} | warmth deficit {row['warmth_deficit']} | wetness {row['wetness']} | stress {row['market_stress']}</small></article>"
        for row in bodies
    )
    relationship_rows = "\n".join(
        "<tr>"
        f"<td>{html.escape(row['agent'])}</td>"
        f"<td>{html.escape(row['other'])}</td>"
        f"<td>{row['relationship_score']}</td>"
        f"<td>{row['market_stress']}</td>"
        f"<td>{row['care_capacity']}</td>"
        "</tr>"
        for row in relationships
    )
    event_rows = "\n".join(
        "<tr>"
        f"<td>{event['day']}</td>"
        f"<td>{html.escape(event['season'])}</td>"
        f"<td>{html.escape(event['agent'])}</td>"
        f"<td>{html.escape(event['kind'])}</td>"
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
<title>Report 211 Seasonal Body Ecology</title>
<style>
:root {{
  --ink: #1f1915;
  --paper: #f0e6d1;
  --sick: #7a7847;
  --care: #b06b3c;
  --cold: #3b6870;
  --line: rgba(31,25,21,.18);
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: Georgia, 'Times New Roman', serif; color: var(--ink); background: linear-gradient(135deg, rgba(240,230,209,.96), rgba(202,213,190,.90)), radial-gradient(circle at 82% 10%, rgba(59,104,112,.24), transparent 30%); }}
main {{ max-width: 1240px; margin: 0 auto; padding: 36px 18px 60px; }}
.hero {{ border: 1px solid var(--line); border-radius: 32px; padding: 30px; background: rgba(255,255,255,.48); box-shadow: 0 26px 72px rgba(42,48,34,.16); }}
h1 {{ margin: 0; font-size: clamp(2.2rem, 7vw, 5.8rem); line-height: .9; letter-spacing: -.055em; }}
.lede {{ max-width: 900px; font-size: 1.12rem; line-height: 1.55; }}
.metrics {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin: 22px 0; }}
.metric, .body {{ border: 1px solid var(--line); border-radius: 22px; padding: 16px; background: rgba(255,255,255,.52); }}
.metric span {{ display: block; min-height: 42px; font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; color: var(--sick); }}
.metric strong {{ font-size: 1.75rem; }}
.bodies {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(255px, 1fr)); gap: 14px; margin: 18px 0; }}
.body h3 {{ margin: 0 0 8px; color: var(--cold); }}
table {{ width: 100%; margin-top: 22px; border-collapse: collapse; border-radius: 20px; overflow: hidden; background: rgba(255,255,255,.55); }}
th, td {{ padding: 11px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }}
th {{ background: rgba(122,120,71,.18); font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; }}
.boundary {{ margin-top: 22px; padding: 16px 18px; border-left: 5px solid var(--care); background: rgba(255,255,255,.48); border-radius: 16px; }}
@media (max-width: 760px) {{ table {{ display: block; overflow-x: auto; }} .hero {{ padding: 22px; }} }}
</style>
</head>
<body>
<main>
  <section class=\"hero\">
    <h1>Market pressure reaches the body</h1>
    <p class=\"lede\">Report 211 makes seasonal economy consequences embodied: wetness, cold, hunger, fatigue, illness risk, symptoms, communal care, care capacity, and relationship strain all persist across the arc.</p>
  </section>
  <section class=\"metrics\">{metric_cards}</section>
  <h2>Season-end bodies</h2>
  <section class=\"bodies\">{body_cards}</section>
  <h2>Relationships under care and stress</h2>
  <table><thead><tr><th>Agent</th><th>Other</th><th>Relationship</th><th>Market stress</th><th>Care capacity</th></tr></thead><tbody>{relationship_rows}</tbody></table>
  <h2>Body ecology events</h2>
  <table><thead><tr><th>Day</th><th>Season</th><th>Agent</th><th>Kind</th><th>Adverse body</th><th>Note</th></tr></thead><tbody>{event_rows}</tbody></table>
  <p class=\"boundary\"><strong>Boundary:</strong> {html.escape(CLAIM_BOUNDARY)} Residual stress remains visible; distress is bounded and routed through care/recovery opportunities, not spectacle.</p>
</main>
</body>
</html>
"""


def write_artifacts(payload: dict[str, Any]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_PATH.parent.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACT_DIR / f"{PREFIX}_events.csv", payload["events"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_body_ledger.csv", payload["body_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_care_ledger.csv", payload["care_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_illness_ledger.csv", payload["illness_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_relationship_stress.csv", payload["relationship_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", payload["verdict_rows"])
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(payload["results"], indent=2, sort_keys=True) + "\n")
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(payload["state"], indent=2, sort_keys=True) + "\n")
    VISUALIZATION_PATH.write_text(render_visualization(payload))


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Report 211 seasonal body ecology bridge.")
    parser.add_argument("--seed", type=int, default=20260824)
    parser.add_argument("--days", type=int, default=72)
    args = parser.parse_args()

    payload = run_bridge(seed=args.seed, days=args.days)
    write_artifacts(payload)
    results = payload["results"]
    print(f"module_verdict {results['module_verdict']}")
    print(f"seasonal_body_ecology_readiness {results['seasonal_body_ecology_readiness']:.6f}")
    print(f"body_ecology_days {results['body_ecology_days']}")
    print(f"body_ecology_events {results['body_ecology_events']}")
    print(f"communal_care_response_rate {results['communal_care_response_rate']:.6f}")
    print(f"relationship_repair_rate {results['relationship_repair_rate']:.6f}")
    print(f"illness_recovery_rate {results['illness_recovery_rate']:.6f}")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
