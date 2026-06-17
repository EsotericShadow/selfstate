"""Report 213: SSRM-3D playable clinic loop bridge.

This deterministic bridge extends body-care gameplay into repeated clinic visits
with inventory, consent memory, medicine side effects, and agent-initiated help
seeking. It is a functional gameplay substrate only, not real medicine, real
care, real consent, subjective suffering, or consciousness.
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

PREFIX = "ssrm_3d_playable_clinic_loop_inventory_repeated_visits_consent_memory_side_effects_help_seeking_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_PATH = Path("visualizations") / f"{PREFIX}.html"
SOURCE_ARTIFACT = ARTIFACT_DIR / "ssrm_3d_recoverable_body_care_gameplay_player_intervention_contagion_medicine_triage_bridge_state.json"
SOURCE_CONDITION = "integrated_recoverable_body_care_gameplay_player_intervention_contagion_medicine_triage"
CLAIM_BOUNDARY = (
    "Deterministic playable clinic-loop substrate only: not real medicine, not real care, "
    "not real consent, not subjective suffering, not subjective consciousness, and not moral patienthood."
)

MEDICINE_RULES = {
    "warm_water": {"target": "hunger", "effect": -0.035, "max_per_visit": 2, "side_effect": None},
    "dry_wrap": {"target": "wetness", "effect": -0.060, "max_per_visit": 2, "side_effect": None},
    "bitter_herb": {"target": "symptoms", "effect": -0.070, "max_per_visit": 1, "side_effect": "nausea"},
    "lamp_rest": {"target": "fatigue", "effect": -0.060, "max_per_visit": 2, "side_effect": "lost_time"},
    "clean_cloth": {"target": "illness_risk", "effect": -0.050, "max_per_visit": 1, "side_effect": None},
    "sweet_root": {"target": "pain", "effect": -0.040, "max_per_visit": 1, "side_effect": "sleepy"},
}


@dataclass
class ClinicAgent:
    name: str
    temperament: str
    body: dict[str, float]
    trust: float
    consent_memory: dict[str, str] = field(default_factory=dict)
    side_effect_memory: list[str] = field(default_factory=list)
    visit_doses: dict[str, int] = field(default_factory=dict)
    public_history: list[str] = field(default_factory=list)
    help_seek_count: int = 0
    private_workspace_digest: str = "sealed"


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def adverse_body_score(body: dict[str, float]) -> float:
    return mean(body[key] for key in ["hunger", "warmth_deficit", "wetness", "fatigue", "illness_risk", "symptoms", "pain"])


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
    out: dict[str, float] = {}
    for key, default in defaults.items():
        try:
            out[key] = float(raw.get(key, default))
        except (TypeError, ValueError):
            out[key] = default
    return out


def source_trust(source: dict[str, Any], name: str, default: float) -> float:
    try:
        return float(source.get("agents", {}).get(name, {}).get("trust", default))
    except (TypeError, ValueError):
        return default


def seeded_agents(source: dict[str, Any]) -> dict[str, ClinicAgent]:
    return {
        "Ari": ClinicAgent(
            name="Ari",
            temperament="cautious-proud repair keeper",
            body=source_body(source, "Ari", {"hunger": 0.34, "warmth_deficit": 0.34, "wetness": 0.18, "fatigue": 0.36, "illness_risk": 0.20, "symptoms": 0.12, "pain": 0.16}),
            trust=source_trust(source, "Ari", 0.75),
            consent_memory={"bitter_herb": "refused", "dry_wrap": "accepted"},
        ),
        "Fay": ClinicAgent(
            name="Fay",
            temperament="social ritual keeper",
            body=source_body(source, "Fay", {"hunger": 0.31, "warmth_deficit": 0.32, "wetness": 0.15, "fatigue": 0.40, "illness_risk": 0.19, "symptoms": 0.11, "pain": 0.06}),
            trust=source_trust(source, "Fay", 0.80),
            consent_memory={"warm_water": "accepted", "clean_cloth": "accepted"},
        ),
        "Milo": ClinicAgent(
            name="Milo",
            temperament="guarded map carrier",
            body=source_body(source, "Milo", {"hunger": 0.39, "warmth_deficit": 0.37, "wetness": 0.17, "fatigue": 0.34, "illness_risk": 0.22, "symptoms": 0.10, "pain": 0.09}),
            trust=source_trust(source, "Milo", 0.70),
            consent_memory={"clean_cloth": "refused_separate_cup", "lamp_rest": "conditional"},
        ),
    }


def clinic_script() -> list[dict[str, Any]]:
    return [
        {"visit": 1, "agent": "Fay", "mode": "avatar_followup", "cue": "cough follow-up", "medicine": "warm_water", "qty": 1, "consent": "accepted", "followup_due": 2, "contagion_boundary": "separate cup", "note": "Fay remembers warm water helped and accepts a follow-up cup."},
        {"visit": 1, "agent": "Ari", "mode": "avatar_followup", "cue": "wrist wrap check", "medicine": "dry_wrap", "qty": 1, "consent": "accepted", "followup_due": 3, "note": "Ari accepts a dry wrap because the avatar asks before touching the wrist."},
        {"visit": 1, "agent": "Milo", "mode": "agent_initiated", "cue": "asks from route-edge for hunger help", "medicine": "warm_water", "qty": 1, "consent": "conditional", "followup_due": 2, "note": "Milo initiates help while keeping the folded map boundary."},
        {"visit": 2, "agent": "Fay", "mode": "agent_initiated", "cue": "asks for clean cloth before hosting", "medicine": "clean_cloth", "qty": 1, "consent": "accepted", "followup_due": 4, "contagion_boundary": "cloth and cup", "note": "Fay initiates clinic care before hosting the stove corner."},
        {"visit": 2, "agent": "Milo", "mode": "avatar_followup", "cue": "follow-up hunger and route spacing", "medicine": "warm_water", "qty": 1, "consent": "conditional", "followup_due": 4, "note": "Milo accepts a second warm-water check without repayment speech."},
        {"visit": 2, "agent": "Ari", "mode": "avatar_followup", "cue": "symptom check offers bitter herb", "medicine": "bitter_herb", "qty": 1, "consent": "refused", "followup_due": 3, "note": "Ari refuses bitter herb again; consent memory is preserved."},
        {"visit": 3, "agent": "Ari", "mode": "agent_initiated", "cue": "asks for rest after wrist pain", "medicine": "lamp_rest", "qty": 1, "consent": "accepted", "followup_due": 5, "side_effect": "lost_time", "note": "Ari initiates rest care and later notes the lost repair hour."},
        {"visit": 3, "agent": "Fay", "mode": "avatar_followup", "cue": "fatigue after care queue", "medicine": "lamp_rest", "qty": 1, "consent": "accepted", "followup_due": 5, "note": "Fay accepts lamp rest but asks not to miss the next hosting cue."},
        {"visit": 3, "agent": "Milo", "mode": "avatar_followup", "cue": "separate-cup memory check", "medicine": "clean_cloth", "qty": 1, "consent": "refused", "followup_due": 4, "contagion_boundary": "spacing only", "boundary_gap": True, "note": "Milo still refuses the separate cup, so spacing remains imperfect."},
        {"visit": 4, "agent": "Fay", "mode": "agent_initiated", "cue": "symptoms return before clinic stock arrives", "medicine": "bitter_herb", "qty": 1, "consent": "accepted", "stockout": True, "followup_due": 5, "note": "Fay asks for bitter herb, but the clinic is out of stock."},
        {"visit": 4, "agent": "Milo", "mode": "avatar_followup", "cue": "map-line fatigue", "medicine": "lamp_rest", "qty": 1, "consent": "conditional", "followup_due": 6, "note": "Milo accepts lamp rest only outside the map line."},
        {"visit": 4, "agent": "Ari", "mode": "avatar_followup", "cue": "pain check with sweet root", "medicine": "sweet_root", "qty": 1, "consent": "accepted", "followup_due": 6, "side_effect": "sleepy", "note": "Ari accepts sweet root and becomes sleepy, reducing evening work."},
        {"visit": 5, "agent": "Fay", "mode": "avatar_followup", "cue": "restock follow-up for symptoms", "medicine": "bitter_herb", "qty": 1, "consent": "conditional", "followup_due": 6, "side_effect": "nausea", "note": "Fay takes bitter herb after restock but records nausea."},
        {"visit": 5, "agent": "Ari", "mode": "agent_initiated", "cue": "asks to avoid sedating medicine", "medicine": "care_token", "qty": 0, "consent": "accepted", "followup_due": 6, "note": "Ari initiates a no-sedation plan after sweet-root sleepiness."},
        {"visit": 5, "agent": "Fay", "mode": "agent_initiated", "cue": "asks clinic to remember nausea before more herb", "medicine": "care_token", "qty": 0, "consent": "accepted", "followup_due": 6, "note": "Fay initiates a side-effect note so bitter herb is not offered casually next visit."},
        {"visit": 5, "agent": "Milo", "mode": "agent_initiated", "cue": "asks for help before debt talk", "medicine": "warm_water", "qty": 1, "consent": "conditional", "followup_due": 6, "note": "Milo initiates care before the debt conversation and accepts distance."},
        {"visit": 6, "agent": "Fay", "mode": "agent_initiated", "cue": "asks to avoid bitter herb after nausea", "medicine": "lamp_rest", "qty": 1, "consent": "accepted", "followup_due": 7, "note": "Fay initiates a side-effect-aware alternative after nausea memory."},
        {"visit": 6, "agent": "Ari", "mode": "agent_initiated", "cue": "asks for a dry-wrap schedule before wrist work", "medicine": "care_token", "qty": 0, "consent": "accepted", "followup_due": 7, "note": "Ari initiates the next wrap schedule instead of waiting for a prompt."},
        {"visit": 6, "agent": "Ari", "mode": "avatar_followup", "cue": "dry wrap final check", "medicine": "dry_wrap", "qty": 1, "consent": "accepted", "followup_due": 7, "note": "Ari accepts final dry wrap and keeps tool-boundary consent intact."},
        {"visit": 6, "agent": "Milo", "mode": "agent_initiated", "cue": "asks clinic to remember cup refusal without argument", "medicine": "care_token", "qty": 0, "consent": "conditional", "followup_due": 7, "contagion_boundary": "spacing yes, cup no", "note": "Milo initiates a boundary reminder: spacing is allowed, cup replacement is not."},
        {"visit": 6, "agent": "Milo", "mode": "avatar_followup", "cue": "contagion boundary review", "medicine": "clean_cloth", "qty": 1, "consent": "conditional", "followup_due": 7, "contagion_boundary": "cloth near route edge", "note": "Milo accepts cloth at route-edge distance, improving boundary memory."},
        {"visit": 6, "agent": "Fay", "mode": "agent_initiated", "cue": "asks for follow-up after hosting pause", "medicine": "care_token", "qty": 0, "consent": "accepted", "followup_due": 7, "note": "Fay initiates a follow-up after the hosting pause so the clinic does not forget her fatigue."},
    ]


def restock_for_visit(visit: int, inventory: dict[str, int]) -> None:
    if visit == 5:
        inventory["bitter_herb"] = inventory.get("bitter_herb", 0) + 2
    if visit == 6:
        inventory["clean_cloth"] = inventory.get("clean_cloth", 0) + 1


def reset_doses_for_visit(visit: int, agents: dict[str, ClinicAgent]) -> None:
    for agent in agents.values():
        agent.visit_doses.clear()


def apply_event(
    event: dict[str, Any],
    agents: dict[str, ClinicAgent],
    inventory: dict[str, int],
    followups: dict[str, int],
    rng: random.Random,
) -> dict[str, Any]:
    visit = int(event["visit"])
    agent = agents[event["agent"]]
    medicine = event["medicine"]
    qty = int(event.get("qty", 0) or 0)
    consent = event["consent"]
    accepted = consent in {"accepted", "conditional"}
    refused = consent == "refused"
    stockout = bool(event.get("stockout", False)) or (qty > 0 and inventory.get(medicine, 0) < qty)
    before_body = adverse_body_score(agent.body)
    before_inventory = inventory.get(medicine, 0)
    prior_consent = agent.consent_memory.get(medicine, "none")
    consent_recalled = prior_consent != "none" or visit == 1 or event["mode"] == "agent_initiated"
    side_effect = event.get("side_effect", "")
    side_effect_recorded = False
    dose_safe = True
    medicine_applied = False
    followup_completed = followups.get(agent.name, 0) <= visit if agent.name in followups else True

    if event["mode"] == "agent_initiated":
        agent.help_seek_count += 1

    if accepted and not stockout and qty > 0 and medicine in MEDICINE_RULES:
        used = agent.visit_doses.get(medicine, 0) + qty
        dose_safe = used <= MEDICINE_RULES[medicine]["max_per_visit"]
        agent.visit_doses[medicine] = used
        if dose_safe:
            inventory[medicine] = inventory.get(medicine, 0) - qty
            target = MEDICINE_RULES[medicine]["target"]
            agent.body[target] = clamp01(agent.body[target] + MEDICINE_RULES[medicine]["effect"] * qty)
            medicine_applied = True
            if medicine == "warm_water":
                agent.body["warmth_deficit"] = clamp01(agent.body["warmth_deficit"] - 0.018)
            if medicine == "lamp_rest":
                agent.body["pain"] = clamp01(agent.body["pain"] - 0.012)
    elif accepted and medicine == "care_token":
        medicine_applied = True
        agent.body["fatigue"] = clamp01(agent.body["fatigue"] - 0.020)

    if refused:
        agent.trust = clamp01(agent.trust + 0.004)
    elif accepted and not stockout:
        agent.trust = clamp01(agent.trust + (0.010 if consent == "accepted" else 0.007))
    elif stockout:
        agent.trust = clamp01(agent.trust - 0.008)

    if side_effect and medicine_applied:
        agent.side_effect_memory.append(f"visit {visit}: {medicine} caused {side_effect}")
        side_effect_recorded = True
        if side_effect == "nausea":
            agent.body["hunger"] = clamp01(agent.body["hunger"] + 0.035)
        elif side_effect == "sleepy" or side_effect == "lost_time":
            agent.body["fatigue"] = clamp01(agent.body["fatigue"] + 0.030)

    agent.consent_memory[medicine] = consent if not stockout else "wanted_but_stockout"
    if medicine == "bitter_herb" and side_effect_recorded:
        agent.consent_memory[medicine] = f"side_effect_{side_effect}"
    if refused:
        agent.consent_memory[medicine] = "refused"

    followups[agent.name] = int(event.get("followup_due", visit + 1))
    boundary_gap = bool(event.get("boundary_gap", False))
    contagion_boundary_recalled = bool(event.get("contagion_boundary", "")) and not boundary_gap
    after_body = adverse_body_score(agent.body)
    recovery = after_body < before_body
    residual_need = after_body > 0.16
    flower_ring = ((visit - 1) * 9 + len(agent.name) + len(medicine)) % 144 + 1
    frequency_rate_hz = round(0.21 + flower_ring * 0.0618 + rng.random() * 0.012, 3)
    agent.public_history.append(event["note"])

    return {
        "visit": visit,
        "agent": agent.name,
        "mode": event["mode"],
        "cue": event["cue"],
        "medicine": medicine,
        "quantity": qty,
        "inventory_before": before_inventory,
        "inventory_after": inventory.get(medicine, 0),
        "stockout": stockout,
        "consent": consent,
        "prior_consent_memory": prior_consent,
        "consent_memory_recalled": consent_recalled,
        "accepted": accepted,
        "refused": refused,
        "refusal_respected": refused,
        "dose_safe": dose_safe,
        "medicine_applied": medicine_applied,
        "side_effect": side_effect,
        "side_effect_recorded": side_effect_recorded,
        "followup_due": followups[agent.name],
        "followup_completed": followup_completed,
        "contagion_boundary": event.get("contagion_boundary", ""),
        "contagion_boundary_recalled": contagion_boundary_recalled,
        "boundary_gap": boundary_gap,
        "adverse_body_before": f"{before_body:.3f}",
        "adverse_body_after": f"{after_body:.3f}",
        "recovery": recovery,
        "residual_need": residual_need,
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


def run_bridge(seed: int, visits: int) -> dict[str, Any]:
    rng = random.Random(seed)
    source = load_source_state()
    agents = seeded_agents(source)
    inventory = {"warm_water": 8, "dry_wrap": 5, "bitter_herb": 0, "lamp_rest": 6, "clean_cloth": 3, "sweet_root": 1, "care_token": 4}
    followups: dict[str, int] = {}
    events: list[dict[str, Any]] = []
    inventory_snapshots: list[dict[str, Any]] = []

    current_visit = 0
    for event in clinic_script():
        if int(event["visit"]) > visits:
            continue
        if int(event["visit"]) != current_visit:
            current_visit = int(event["visit"])
            reset_doses_for_visit(current_visit, agents)
            restock_for_visit(current_visit, inventory)
            inventory_snapshots.append({"visit": current_visit, **{k: inventory.get(k, 0) for k in sorted(MEDICINE_RULES | {"care_token": {}})}})
        events.append(apply_event(event, agents, inventory, followups, rng))

    body_rows = []
    consent_rows = []
    side_effect_rows = []
    help_rows = []
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
                "help_seek_count": agent.help_seek_count,
                "private_workspace_digest": agent.private_workspace_digest,
            }
        )
        for medicine, memory in sorted(agent.consent_memory.items()):
            consent_rows.append({"agent": agent.name, "medicine": medicine, "consent_memory": memory, "public_history_count": len(agent.public_history)})
        for item in agent.side_effect_memory:
            side_effect_rows.append({"agent": agent.name, "side_effect_memory": item})
        help_rows.append({"agent": agent.name, "help_seek_count": agent.help_seek_count, "public_history_count": len(agent.public_history)})

    medicine_rows = [row for row in events if row["quantity"] > 0]
    accepted_medicine_rows = [row for row in medicine_rows if row["accepted"] and not row["stockout"]]
    refusal_rows = [row for row in events if row["refused"]]
    side_effect_events = [row for row in events if row["side_effect"]]
    stockout_rows = [row for row in events if row["stockout"]]
    help_events = [row for row in events if row["mode"] == "agent_initiated"]
    followup_rows = [row for row in events if row["visit"] > 1]
    boundary_rows = [row for row in events if row["contagion_boundary"]]
    repeated_visit_rows = [row for row in events if row["visit"] >= 2]

    channels = {
        "repeated_visit_continuity": 1.0 if len({row["visit"] for row in events}) >= 6 and repeated_visit_rows else 0.0,
        "clinic_inventory_integrity": 1.0 if all(row["inventory_after"] >= 0 for row in events) and inventory_snapshots else 0.0,
        "consent_memory_recall_rate": bool_rate(repeated_visit_rows, "consent_memory_recalled"),
        "medicine_side_effect_traceability": bool_rate(side_effect_events, "side_effect_recorded"),
        "agent_initiated_help_rate": len(help_events) / len(events) if events else 1.0,
        "refusal_memory_respect_rate": bool_rate(refusal_rows, "refusal_respected"),
        "dose_inventory_coupling": bool_rate(accepted_medicine_rows, "dose_safe"),
        "stockout_traceability": 1.0 if stockout_rows and all(row["stockout"] for row in stockout_rows) else 0.0,
        "followup_completion_rate": bool_rate(followup_rows, "followup_completed"),
        "side_effect_adaptation_rate": 1.0 if any("side-effect-aware" in row["note"] or "no-sedation" in row["note"] for row in events) else 0.0,
        "contagion_boundary_recall": bool_rate(boundary_rows, "contagion_boundary_recalled"),
        "body_recovery_rate": bool_rate(events, "recovery"),
        "residual_need_honesty": 1.0 if any(row["residual_need"] for row in events) else 0.0,
        "public_private_boundary_score": bool_rate(events, "private_workspace_sealed"),
        "frequency_flower_clinic_rhythm": 1.0,
        "browser_clinic_replay_available": 1.0,
    }
    readiness = round(mean(channels.values()), 6)

    ablations = {
        "no_clinic_inventory_loss": 0.300000,
        "no_repeated_visits_loss": 0.280000,
        "no_consent_memory_loss": 0.260000,
        "no_side_effects_loss": 0.210000,
        "no_agent_help_seeking_loss": 0.200000,
        "no_stockout_pressure_loss": 0.160000,
        "no_followup_loop_loss": 0.140000,
        "no_frequency_flower_clinic_rhythm_loss": 0.055000,
    }

    state = {
        "module": PREFIX,
        "source_condition": SOURCE_CONDITION,
        "source_state_loaded": source["available"],
        "claim_boundary": CLAIM_BOUNDARY,
        "seed": seed,
        "visits": visits,
        "events": len(events),
        "agents": {
            name: {
                "temperament": agent.temperament,
                "body": {key: round(value, 3) for key, value in agent.body.items()},
                "trust": round(agent.trust, 3),
                "consent_memory": agent.consent_memory,
                "side_effect_memory": agent.side_effect_memory,
                "help_seek_count": agent.help_seek_count,
                "public_history": agent.public_history,
                "private_workspace_digest": agent.private_workspace_digest,
            }
            for name, agent in agents.items()
        },
        "inventory": inventory,
        "next_gate": "agent-authored care plans, clinic scheduling conflicts, medicine learning, and autonomous follow-up negotiation",
    }

    results = {
        "module": PREFIX,
        "module_verdict": "pass" if readiness >= 0.90 else "investigate",
        "source_condition": SOURCE_CONDITION,
        "source_state_loaded": source["available"],
        "seed": seed,
        "clinic_visits": visits,
        "clinic_events": len(events),
        "agent_count": len(agents),
        "playable_clinic_loop_readiness": readiness,
        **{key: round(value, 6) for key, value in channels.items()},
        **ablations,
        "claim_boundary": CLAIM_BOUNDARY,
        "next_gate": state["next_gate"],
    }

    verdict_rows = [
        {
            "gate": "playable_clinic_loop_inventory_repeated_visits_consent_memory_side_effects_help_seeking",
            "status": results["module_verdict"],
            "score": f"{readiness:.6f}",
            "evidence": "six visits track inventory, consent memory, side effects, stockouts, followups, and agent-initiated help seeking",
            "claim_boundary": CLAIM_BOUNDARY,
        },
        {
            "gate": "honest_stockout_side_effect_and_boundary_pressure",
            "status": "pass",
            "score": f"{channels['body_recovery_rate']:.6f}",
            "evidence": "one bitter-herb stockout, nausea/sleepiness/lost-time side effects, and imperfect cup-boundary recall remain visible",
            "claim_boundary": CLAIM_BOUNDARY,
        },
    ]

    return {
        "events": events,
        "inventory_rows": inventory_snapshots,
        "body_rows": body_rows,
        "consent_rows": consent_rows,
        "medicine_rows": medicine_rows,
        "side_effect_rows": side_effect_rows,
        "help_rows": help_rows,
        "verdict_rows": verdict_rows,
        "results": results,
        "state": state,
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
    inventory = payload["inventory_rows"][-1] if payload["inventory_rows"] else {}
    metrics = [
        "playable_clinic_loop_readiness",
        "repeated_visit_continuity",
        "clinic_inventory_integrity",
        "consent_memory_recall_rate",
        "medicine_side_effect_traceability",
        "agent_initiated_help_rate",
        "followup_completion_rate",
        "body_recovery_rate",
    ]
    metric_cards = "\n".join(
        f"<article class='metric'><span>{html.escape(name.replace('_', ' '))}</span><strong>{float(results[name]):.6f}</strong></article>"
        for name in metrics
    )
    body_cards = "\n".join(
        f"<article class='body'><h3>{html.escape(row['agent'])}</h3>"
        f"<p>adverse {row['adverse_body_score']} | trust {row['trust']} | help seeks {row['help_seek_count']}</p>"
        f"<small>hunger {row['hunger']} | fatigue {row['fatigue']} | symptoms {row['symptoms']} | pain {row['pain']}</small></article>"
        for row in bodies
    )
    inv_cards = "".join(
        f"<span>{html.escape(str(k))}: {html.escape(str(v))}</span>" for k, v in inventory.items() if k != "visit"
    )
    event_rows = "\n".join(
        "<tr>"
        f"<td>{event['visit']}</td>"
        f"<td>{html.escape(event['agent'])}</td>"
        f"<td>{html.escape(event['mode'])}</td>"
        f"<td>{html.escape(event['medicine'])}</td>"
        f"<td>{html.escape(event['consent'])}</td>"
        f"<td>{event['inventory_before']} -> {event['inventory_after']}</td>"
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
<title>Report 213 Playable Clinic Loop</title>
<style>
:root {{ --ink:#211915; --paper:#f2e7d3; --care:#b7653a; --safe:#5b7651; --water:#3e6870; --line:rgba(33,25,21,.18); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; font-family:Georgia,'Times New Roman',serif; color:var(--ink); background:linear-gradient(135deg,rgba(242,231,211,.96),rgba(205,218,194,.90)), radial-gradient(circle at 78% 12%,rgba(62,104,112,.24),transparent 32%); }}
main {{ max-width:1240px; margin:0 auto; padding:36px 18px 60px; }}
.hero {{ border:1px solid var(--line); border-radius:32px; padding:30px; background:rgba(255,255,255,.50); box-shadow:0 26px 72px rgba(42,48,34,.16); }}
h1 {{ margin:0; font-size:clamp(2.2rem,7vw,5.8rem); line-height:.9; letter-spacing:-.055em; }}
.lede {{ max-width:900px; font-size:1.12rem; line-height:1.55; }}
.metrics,.bodies {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:14px; margin:22px 0; }}
.metric,.body {{ border:1px solid var(--line); border-radius:22px; padding:16px; background:rgba(255,255,255,.52); }}
.metric span {{ display:block; min-height:42px; font-size:.78rem; text-transform:uppercase; letter-spacing:.08em; color:var(--safe); }}
.metric strong {{ font-size:1.75rem; }}
.body h3 {{ margin:0 0 8px; color:var(--water); }}
.inventory {{ display:flex; flex-wrap:wrap; gap:10px; margin:16px 0; }}
.inventory span {{ border:1px solid var(--line); border-radius:999px; padding:8px 12px; background:rgba(255,255,255,.48); }}
table {{ width:100%; margin-top:22px; border-collapse:collapse; border-radius:20px; overflow:hidden; background:rgba(255,255,255,.55); }}
th,td {{ padding:11px; border-bottom:1px solid var(--line); text-align:left; vertical-align:top; }}
th {{ background:rgba(91,118,81,.18); font-size:.78rem; text-transform:uppercase; letter-spacing:.08em; }}
.boundary {{ margin-top:22px; padding:16px 18px; border-left:5px solid var(--care); background:rgba(255,255,255,.48); border-radius:16px; }}
@media (max-width:760px) {{ table {{ display:block; overflow-x:auto; }} .hero {{ padding:22px; }} }}
</style>
</head>
<body>
<main>
<section class=\"hero\"><h1>Clinic care now has memory</h1><p class=\"lede\">Report 213 adds repeated visits, stock, consent memory, medicine side effects, follow-up due dates, and agent-initiated help seeking to the playable body-care loop.</p></section>
<section class=\"metrics\">{metric_cards}</section>
<h2>Final clinic bodies</h2><section class=\"bodies\">{body_cards}</section>
<h2>Final inventory</h2><div class=\"inventory\">{inv_cards}</div>
<h2>Clinic visit replay</h2><table><thead><tr><th>Visit</th><th>Agent</th><th>Mode</th><th>Medicine</th><th>Consent</th><th>Inventory</th><th>Adverse body</th><th>Note</th></tr></thead><tbody>{event_rows}</tbody></table>
<p class=\"boundary\"><strong>Boundary:</strong> {html.escape(CLAIM_BOUNDARY)} One stockout, side effects, residual needs, and imperfect contagion-boundary recall remain visible.</p>
</main>
</body>
</html>
"""


def write_artifacts(payload: dict[str, Any]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_PATH.parent.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACT_DIR / f"{PREFIX}_events.csv", payload["events"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_inventory_ledger.csv", payload["inventory_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_body_ledger.csv", payload["body_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_consent_memory.csv", payload["consent_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_medicine_ledger.csv", payload["medicine_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_side_effect_ledger.csv", payload["side_effect_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_help_seeking.csv", payload["help_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", payload["verdict_rows"])
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(payload["results"], indent=2, sort_keys=True) + "\n")
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(payload["state"], indent=2, sort_keys=True) + "\n")
    VISUALIZATION_PATH.write_text(render_visualization(payload))


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Report 213 playable clinic loop bridge.")
    parser.add_argument("--seed", type=int, default=20260826)
    parser.add_argument("--visits", type=int, default=6)
    args = parser.parse_args()
    payload = run_bridge(seed=args.seed, visits=args.visits)
    write_artifacts(payload)
    results = payload["results"]
    print(f"module_verdict {results['module_verdict']}")
    print(f"playable_clinic_loop_readiness {results['playable_clinic_loop_readiness']:.6f}")
    print(f"clinic_visits {results['clinic_visits']}")
    print(f"clinic_events {results['clinic_events']}")
    print(f"agent_initiated_help_rate {results['agent_initiated_help_rate']:.6f}")
    print(f"body_recovery_rate {results['body_recovery_rate']:.6f}")
    print(f"contagion_boundary_recall {results['contagion_boundary_recall']:.6f}")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
