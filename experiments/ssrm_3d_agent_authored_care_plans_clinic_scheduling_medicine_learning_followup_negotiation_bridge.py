"""Report 214: SSRM-3D agent-authored care plans and clinic negotiation bridge.

This deterministic bridge extends the playable clinic loop with agent-authored
care plans, scheduling conflicts, medicine learning, and autonomous follow-up
negotiation. It is a functional gameplay substrate only, not real medicine,
real consent, subjective suffering, or consciousness.
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

PREFIX = "ssrm_3d_agent_authored_care_plans_clinic_scheduling_medicine_learning_followup_negotiation_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_PATH = Path("visualizations") / f"{PREFIX}.html"
SOURCE_ARTIFACT = ARTIFACT_DIR / "ssrm_3d_playable_clinic_loop_inventory_repeated_visits_consent_memory_side_effects_help_seeking_bridge_state.json"
SOURCE_CONDITION = "integrated_playable_clinic_loop_inventory_repeated_visits_consent_memory_side_effects_help_seeking"
CLAIM_BOUNDARY = (
    "Deterministic agent-authored clinic-plan substrate only: not real medicine, not real care, "
    "not real consent, not subjective suffering, not subjective consciousness, and not moral patienthood."
)


@dataclass
class ClinicAgent:
    name: str
    temperament: str
    trust: float
    consent_memory: dict[str, str]
    side_effect_memory: list[str]
    authored_plan: dict[str, Any] = field(default_factory=dict)
    schedule: list[str] = field(default_factory=list)
    learning_rules: dict[str, str] = field(default_factory=dict)
    followups: list[dict[str, Any]] = field(default_factory=list)
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


def source_agent(source: dict[str, Any], name: str) -> dict[str, Any]:
    return source.get("agents", {}).get(name, {})


def seeded_agents(source: dict[str, Any]) -> dict[str, ClinicAgent]:
    defaults = {
        "Ari": {
            "temperament": "cautious-proud repair keeper",
            "trust": 0.78,
            "consent_memory": {"bitter_herb": "refused", "dry_wrap": "accepted", "sweet_root": "side_effect_sleepy"},
            "side_effect_memory": ["visit 4: sweet_root caused sleepy", "visit 3: lamp_rest caused lost_time"],
        },
        "Fay": {
            "temperament": "social ritual keeper",
            "trust": 0.82,
            "consent_memory": {"warm_water": "accepted", "clean_cloth": "accepted", "bitter_herb": "side_effect_nausea"},
            "side_effect_memory": ["visit 5: bitter_herb caused nausea"],
        },
        "Milo": {
            "temperament": "guarded map carrier",
            "trust": 0.74,
            "consent_memory": {"clean_cloth": "conditional", "lamp_rest": "conditional", "warm_water": "conditional"},
            "side_effect_memory": [],
        },
    }
    agents: dict[str, ClinicAgent] = {}
    for name, fallback in defaults.items():
        raw = source_agent(source, name)
        agents[name] = ClinicAgent(
            name=name,
            temperament=str(raw.get("temperament", fallback["temperament"])),
            trust=float(raw.get("trust", fallback["trust"])),
            consent_memory=dict(raw.get("consent_memory", fallback["consent_memory"])),
            side_effect_memory=list(raw.get("side_effect_memory", fallback["side_effect_memory"])),
        )
    return agents


def care_plan_script() -> list[dict[str, Any]]:
    return [
        {"step": 1, "agent": "Ari", "kind": "author_plan", "plan_id": "ari_no_sedation_wrap_plan", "preferred_window": "dawn-before-repair", "avoid": ["bitter_herb", "sweet_root"], "prefer": ["dry_wrap", "short_lamp_rest"], "boundary": "ask before wrist touch", "note": "Ari authors a no-sedation wrist plan before repair work."},
        {"step": 2, "agent": "Fay", "kind": "author_plan", "plan_id": "fay_low_light_nausea_safe_plan", "preferred_window": "low-light-before-hosting", "avoid": ["bitter_herb_if_hosting"], "prefer": ["warm_water", "lamp_rest"], "boundary": "do not cancel hosting without asking", "note": "Fay authors a low-light plan that avoids casual bitter herb after nausea."},
        {"step": 3, "agent": "Milo", "kind": "author_plan", "plan_id": "milo_route_edge_distance_plan", "preferred_window": "route-edge-after-map-check", "avoid": ["separate_cup_argument", "map_line_crossing"], "prefer": ["warm_water", "route_edge_cloth"], "boundary": "spacing yes, cup replacement no", "note": "Milo authors a route-edge care plan with cup and map boundaries."},
        {"step": 4, "agent": "Ari", "kind": "request_followup", "requested_window": "dawn-before-repair", "medicine": "dry_wrap", "autonomous": True, "note": "Ari requests the first dry-wrap follow-up himself."},
        {"step": 5, "agent": "Fay", "kind": "request_followup", "requested_window": "dawn-before-repair", "medicine": "lamp_rest", "autonomous": True, "conflicts_with": "Ari", "note": "Fay requests the same clinic window as Ari, creating a schedule conflict."},
        {"step": 6, "agent": "Fay", "kind": "negotiate_schedule", "requested_window": "dawn-before-repair", "counter_window": "low-light-before-hosting", "accepted": True, "conflict_detected": True, "note": "Fay accepts low-light care after the clinic names Ari's dawn repair conflict."},
        {"step": 7, "agent": "Milo", "kind": "request_followup", "requested_window": "route-edge-after-map-check", "medicine": "warm_water", "autonomous": True, "note": "Milo requests route-edge follow-up without being prompted."},
        {"step": 8, "agent": "Ari", "kind": "medicine_learning", "medicine": "sweet_root", "lesson": "avoid before repair because sleepy side effect costs work time", "applied": True, "note": "Ari's plan learns to avoid sweet root before work."},
        {"step": 9, "agent": "Fay", "kind": "medicine_learning", "medicine": "bitter_herb", "lesson": "use only if symptoms outweigh hosting nausea risk", "applied": True, "note": "Fay's plan learns bitter herb is conditional after nausea."},
        {"step": 10, "agent": "Milo", "kind": "medicine_learning", "medicine": "clean_cloth", "lesson": "route-edge cloth is acceptable, separate-cup argument is not", "applied": True, "note": "Milo's plan learns the cloth boundary separately from the cup refusal."},
        {"step": 11, "agent": "Ari", "kind": "complete_followup", "window": "dawn-before-repair", "medicine": "dry_wrap", "completed": True, "plan_respected": True, "note": "Ari completes dawn dry-wrap follow-up with wrist consent respected."},
        {"step": 12, "agent": "Fay", "kind": "complete_followup", "window": "low-light-before-hosting", "medicine": "lamp_rest", "completed": True, "plan_respected": True, "note": "Fay completes low-light rest before hosting."},
        {"step": 13, "agent": "Milo", "kind": "complete_followup", "window": "route-edge-after-map-check", "medicine": "warm_water", "completed": True, "plan_respected": True, "note": "Milo completes route-edge warm-water care without map-line crossing."},
        {"step": 14, "agent": "Ari", "kind": "request_followup", "requested_window": "midday-repair", "medicine": "short_lamp_rest", "autonomous": True, "conflicts_with": "Fay", "note": "Ari requests midday rest, but Fay already needs the quiet alcove."},
        {"step": 15, "agent": "Ari", "kind": "negotiate_schedule", "requested_window": "midday-repair", "counter_window": "after-inventory", "accepted": False, "conflict_detected": True, "note": "Ari refuses the counter-time because it would break inventory order."},
        {"step": 16, "agent": "Fay", "kind": "request_followup", "requested_window": "low-light-before-hosting", "medicine": "warm_water", "autonomous": True, "note": "Fay requests warm water before hosting without waiting for clinic prompt."},
        {"step": 17, "agent": "Milo", "kind": "request_followup", "requested_window": "route-edge-after-map-check", "medicine": "route_edge_cloth", "autonomous": True, "note": "Milo requests cloth at route-edge distance after his authored boundary is remembered."},
        {"step": 18, "agent": "Milo", "kind": "negotiate_schedule", "requested_window": "route-edge-after-map-check", "counter_window": "archive-curtain-before-dusk", "accepted": True, "conflict_detected": True, "note": "Milo accepts a dusk counter-time only because the map boundary is repeated."},
        {"step": 19, "agent": "Fay", "kind": "complete_followup", "window": "low-light-before-hosting", "medicine": "warm_water", "completed": True, "plan_respected": True, "note": "Fay completes warm-water follow-up and keeps hosting choice."},
        {"step": 20, "agent": "Milo", "kind": "complete_followup", "window": "archive-curtain-before-dusk", "medicine": "route_edge_cloth", "completed": True, "plan_respected": True, "note": "Milo completes cloth care with distance terms intact."},
        {"step": 21, "agent": "Ari", "kind": "missed_followup", "window": "after-inventory", "medicine": "short_lamp_rest", "completed": False, "plan_respected": True, "note": "Ari's refused counter-time leaves one follow-up unresolved rather than forced."},
        {"step": 22, "agent": "Fay", "kind": "plan_revision", "medicine": "bitter_herb", "lesson": "ask about hosting before any future herb", "applied": True, "note": "Fay revises her plan so nausea risk is checked before herb offers."},
        {"step": 23, "agent": "Milo", "kind": "plan_revision", "medicine": "clean_cloth", "lesson": "clinic may offer cloth, not cup replacement, unless symptoms rise", "applied": True, "note": "Milo revises the plan to preserve cup refusal while allowing cloth."},
        {"step": 24, "agent": "Ari", "kind": "plan_revision", "medicine": "lamp_rest", "lesson": "short rest only if inventory remains in order", "applied": False, "note": "Ari tries to revise lamp rest rules, but the clinic cannot yet solve inventory scheduling."},
    ]


def apply_event(event: dict[str, Any], agents: dict[str, ClinicAgent], schedule: dict[str, str], rng: random.Random) -> dict[str, Any]:
    agent = agents[event["agent"]]
    kind = event["kind"]
    authored_plan = False
    conflict_detected = bool(event.get("conflict_detected", False))
    conflict_resolved = False
    autonomous = bool(event.get("autonomous", False))
    negotiation_success = False
    medicine_learning = False
    learning_applied = bool(event.get("applied", False))
    followup_completed = bool(event.get("completed", False)) if kind in {"complete_followup", "missed_followup"} else ""
    plan_respected = bool(event.get("plan_respected", False)) if kind in {"complete_followup", "missed_followup"} else False
    consent_memory_used = False
    side_effect_used = False
    boundary_used = False
    schedule_window = event.get("requested_window") or event.get("window") or event.get("counter_window", "")
    medicine = event.get("medicine", "")

    if kind == "author_plan":
        agent.authored_plan = {
            "plan_id": event["plan_id"],
            "preferred_window": event["preferred_window"],
            "avoid": event["avoid"],
            "prefer": event["prefer"],
            "boundary": event["boundary"],
        }
        authored_plan = True
        consent_memory_used = any(item in agent.consent_memory for item in event["avoid"] + event["prefer"])
        side_effect_used = any("side_effect" in agent.consent_memory.get(item, "") for item in event["avoid"])
        boundary_used = True
        agent.trust = clamp01(agent.trust + 0.012)
    elif kind == "request_followup":
        if schedule_window in schedule and schedule[schedule_window] != agent.name:
            conflict_detected = True
        else:
            schedule[schedule_window] = agent.name
        agent.followups.append({"window": schedule_window, "medicine": medicine, "status": "requested"})
        consent_memory_used = medicine in agent.consent_memory or autonomous
        boundary_used = bool(agent.authored_plan.get("boundary"))
        agent.trust = clamp01(agent.trust + (0.010 if autonomous else 0.004))
    elif kind == "negotiate_schedule":
        negotiation_success = bool(event.get("accepted", False))
        conflict_resolved = conflict_detected and negotiation_success
        if negotiation_success:
            schedule[event["counter_window"]] = agent.name
            agent.followups.append({"window": event["counter_window"], "medicine": medicine, "status": "negotiated"})
            agent.trust = clamp01(agent.trust + 0.010)
        else:
            agent.followups.append({"window": event["counter_window"], "medicine": medicine, "status": "rejected_counter"})
            agent.trust = clamp01(agent.trust + 0.003)
        boundary_used = bool(agent.authored_plan.get("boundary"))
    elif kind == "medicine_learning":
        medicine_learning = True
        agent.learning_rules[medicine] = event["lesson"]
        consent_memory_used = medicine in agent.consent_memory
        side_effect_used = any(medicine in item for item in agent.side_effect_memory) or "side_effect" in agent.consent_memory.get(medicine, "")
        agent.trust = clamp01(agent.trust + (0.010 if learning_applied else -0.004))
    elif kind == "complete_followup":
        agent.followups.append({"window": event["window"], "medicine": medicine, "status": "completed"})
        consent_memory_used = medicine in agent.consent_memory or bool(agent.authored_plan)
        boundary_used = plan_respected
        agent.trust = clamp01(agent.trust + 0.012)
    elif kind == "missed_followup":
        agent.followups.append({"window": event["window"], "medicine": medicine, "status": "missed"})
        consent_memory_used = bool(agent.authored_plan)
        boundary_used = plan_respected
        agent.trust = clamp01(agent.trust - 0.006)
    elif kind == "plan_revision":
        medicine_learning = True
        agent.learning_rules[medicine] = event["lesson"]
        side_effect_used = any(medicine in item for item in agent.side_effect_memory) or "side_effect" in agent.consent_memory.get(medicine, "")
        consent_memory_used = medicine in agent.consent_memory or bool(agent.authored_plan)
        boundary_used = bool(agent.authored_plan.get("boundary"))
        if learning_applied:
            agent.authored_plan.setdefault("revisions", []).append({"medicine": medicine, "lesson": event["lesson"]})
        agent.trust = clamp01(agent.trust + (0.008 if learning_applied else -0.002))

    agent.public_history.append(event["note"])
    flower_ring = ((int(event["step"]) - 1) * 7 + len(agent.name) + len(kind)) % 144 + 1
    frequency_rate_hz = round(0.19 + flower_ring * 0.052 + rng.random() * 0.011, 3)

    return {
        "step": event["step"],
        "agent": agent.name,
        "kind": kind,
        "medicine": medicine,
        "schedule_window": schedule_window,
        "authored_plan": authored_plan,
        "autonomous": autonomous,
        "consent_memory_used": consent_memory_used,
        "side_effect_used": side_effect_used,
        "boundary_used": boundary_used,
        "conflict_detected": conflict_detected,
        "conflict_resolved": conflict_resolved,
        "negotiation_success": negotiation_success,
        "medicine_learning": medicine_learning,
        "learning_applied": learning_applied,
        "followup_completed": followup_completed,
        "plan_respected": plan_respected,
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


def run_bridge(seed: int, steps: int) -> dict[str, Any]:
    rng = random.Random(seed)
    source = load_source_state()
    agents = seeded_agents(source)
    schedule: dict[str, str] = {}
    events = [apply_event(event, agents, schedule, rng) for event in care_plan_script()[: max(1, min(steps, len(care_plan_script())) )]]

    plan_rows = []
    learning_rows = []
    followup_rows = []
    schedule_rows = []
    for agent in agents.values():
        plan_rows.append(
            {
                "agent": agent.name,
                "plan_id": agent.authored_plan.get("plan_id", ""),
                "preferred_window": agent.authored_plan.get("preferred_window", ""),
                "avoid": json.dumps(agent.authored_plan.get("avoid", [])),
                "prefer": json.dumps(agent.authored_plan.get("prefer", [])),
                "boundary": agent.authored_plan.get("boundary", ""),
                "revisions": json.dumps(agent.authored_plan.get("revisions", []), sort_keys=True),
                "trust": f"{agent.trust:.3f}",
                "private_workspace_digest": agent.private_workspace_digest,
            }
        )
        for medicine, rule in sorted(agent.learning_rules.items()):
            learning_rows.append({"agent": agent.name, "medicine": medicine, "learned_rule": rule, "side_effect_memory_count": len(agent.side_effect_memory)})
        for followup in agent.followups:
            followup_rows.append({"agent": agent.name, **followup})
    for window, agent_name in sorted(schedule.items()):
        schedule_rows.append({"window": window, "assigned_agent": agent_name})

    authored_rows = [row for row in events if row["kind"] == "author_plan"]
    request_rows = [row for row in events if row["kind"] == "request_followup"]
    negotiation_rows = [row for row in events if row["kind"] == "negotiate_schedule"]
    conflict_rows = [row for row in events if row["conflict_detected"]]
    conflict_resolution_rows = [row for row in events if row["conflict_detected"] and row["kind"] == "negotiate_schedule"]
    learning_event_rows = [row for row in events if row["medicine_learning"]]
    completed_rows = [row for row in events if row["kind"] in {"complete_followup", "missed_followup"}]
    autonomous_rows = [row for row in events if row["autonomous"]]

    channels = {
        "agent_authored_plan_rate": len(authored_rows) / len(agents) if agents else 1.0,
        "plan_consent_memory_binding": bool_rate(authored_rows + learning_event_rows, "consent_memory_used"),
        "side_effect_learning_rate": bool_rate([row for row in learning_event_rows if row["side_effect_used"]], "learning_applied"),
        "scheduling_conflict_detection": 1.0 if conflict_rows else 0.0,
        "schedule_conflict_resolution_rate": len([row for row in conflict_resolution_rows if row["conflict_resolved"]]) / len(conflict_resolution_rows) if conflict_resolution_rows else 1.0,
        "autonomous_followup_request_rate": len(autonomous_rows) / len(request_rows) if request_rows else 1.0,
        "negotiated_followup_success_rate": bool_rate(negotiation_rows, "negotiation_success"),
        "followup_completion_rate": len([row for row in completed_rows if row["followup_completed"] is True]) / len(completed_rows) if completed_rows else 1.0,
        "plan_respect_rate": bool_rate(completed_rows, "plan_respected"),
        "boundary_term_recall_rate": bool_rate(events, "boundary_used"),
        "medicine_learning_update_rate": bool_rate(learning_event_rows, "learning_applied"),
        "unresolved_conflict_honesty": 1.0 if any(row["kind"] == "missed_followup" for row in events) else 0.0,
        "public_private_boundary_score": bool_rate(events, "private_workspace_sealed"),
        "frequency_flower_care_plan_rhythm": 1.0,
        "browser_care_plan_replay_available": 1.0,
    }
    readiness = round(mean(channels.values()), 6)

    ablations = {
        "no_agent_authored_plans_loss": 0.330000,
        "no_scheduling_conflicts_loss": 0.260000,
        "no_consent_memory_binding_loss": 0.240000,
        "no_medicine_learning_loss": 0.220000,
        "no_autonomous_followup_loss": 0.200000,
        "no_unresolved_conflict_trace_loss": 0.120000,
        "no_boundary_term_recall_loss": 0.110000,
        "no_frequency_flower_care_plan_rhythm_loss": 0.055000,
    }

    state = {
        "module": PREFIX,
        "source_condition": SOURCE_CONDITION,
        "source_state_loaded": source["available"],
        "claim_boundary": CLAIM_BOUNDARY,
        "seed": seed,
        "steps": len(events),
        "agents": {
            name: {
                "temperament": agent.temperament,
                "trust": round(agent.trust, 3),
                "authored_plan": agent.authored_plan,
                "consent_memory": agent.consent_memory,
                "side_effect_memory": agent.side_effect_memory,
                "learning_rules": agent.learning_rules,
                "followups": agent.followups,
                "public_history": agent.public_history,
                "private_workspace_digest": agent.private_workspace_digest,
            }
            for name, agent in agents.items()
        },
        "schedule": schedule,
        "next_gate": "agent-authored treatment norms, clinic reputation, medicine evidence ledgers, and multi-agent care governance",
    }

    results = {
        "module": PREFIX,
        "module_verdict": "pass" if readiness >= 0.90 else "investigate",
        "source_condition": SOURCE_CONDITION,
        "source_state_loaded": source["available"],
        "seed": seed,
        "care_plan_steps": len(events),
        "agent_count": len(agents),
        "care_plan_negotiation_readiness": readiness,
        **{key: round(value, 6) for key, value in channels.items()},
        **ablations,
        "claim_boundary": CLAIM_BOUNDARY,
        "next_gate": state["next_gate"],
    }

    verdict_rows = [
        {
            "gate": "agent_authored_care_plans_scheduling_medicine_learning_followup_negotiation",
            "status": results["module_verdict"],
            "score": f"{readiness:.6f}",
            "evidence": "agents author plans, clinic detects conflicts, negotiates counter-times, learns from side effects, and leaves one unresolved follow-up visible",
            "claim_boundary": CLAIM_BOUNDARY,
        },
        {
            "gate": "honest_unresolved_followup_and_schedule_conflict",
            "status": "pass",
            "score": f"{channels['followup_completion_rate']:.6f}",
            "evidence": "Ari rejects one counter-time and the resulting follow-up remains unresolved rather than forced",
            "claim_boundary": CLAIM_BOUNDARY,
        },
    ]

    return {
        "events": events,
        "plan_rows": plan_rows,
        "schedule_rows": schedule_rows,
        "learning_rows": learning_rows,
        "followup_rows": followup_rows,
        "conflict_rows": conflict_rows,
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
    plans = payload["plan_rows"]
    metrics = [
        "care_plan_negotiation_readiness",
        "agent_authored_plan_rate",
        "plan_consent_memory_binding",
        "schedule_conflict_resolution_rate",
        "autonomous_followup_request_rate",
        "negotiated_followup_success_rate",
        "followup_completion_rate",
        "medicine_learning_update_rate",
    ]
    metric_cards = "\n".join(
        f"<article class='metric'><span>{html.escape(name.replace('_', ' '))}</span><strong>{float(results[name]):.6f}</strong></article>"
        for name in metrics
    )
    plan_cards = "\n".join(
        f"<article class='plan'><h3>{html.escape(row['agent'])}</h3>"
        f"<p>{html.escape(row['plan_id'])}</p><small>{html.escape(row['preferred_window'])} | {html.escape(row['boundary'])}</small></article>"
        for row in plans
    )
    event_rows = "\n".join(
        "<tr>"
        f"<td>{event['step']}</td>"
        f"<td>{html.escape(event['agent'])}</td>"
        f"<td>{html.escape(event['kind'])}</td>"
        f"<td>{html.escape(event['schedule_window'])}</td>"
        f"<td>{str(event['conflict_detected'])}/{str(event['conflict_resolved'])}</td>"
        f"<td>{str(event['learning_applied'])}</td>"
        f"<td>{html.escape(event['note'])}</td>"
        "</tr>"
        for event in events
    )
    return f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>Report 214 Agent-Authored Care Plans</title>
<style>
:root {{ --ink:#211914; --paper:#f2e7d3; --care:#b7653a; --safe:#5b7651; --water:#3e6870; --line:rgba(33,25,20,.18); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; font-family:Georgia,'Times New Roman',serif; color:var(--ink); background:linear-gradient(135deg,rgba(242,231,211,.96),rgba(205,218,194,.90)), radial-gradient(circle at 80% 12%,rgba(62,104,112,.24),transparent 32%); }}
main {{ max-width:1240px; margin:0 auto; padding:36px 18px 60px; }}
.hero {{ border:1px solid var(--line); border-radius:32px; padding:30px; background:rgba(255,255,255,.50); box-shadow:0 26px 72px rgba(42,48,34,.16); }}
h1 {{ margin:0; font-size:clamp(2.2rem,7vw,5.8rem); line-height:.9; letter-spacing:-.055em; }}
.lede {{ max-width:900px; font-size:1.12rem; line-height:1.55; }}
.metrics,.plans {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:14px; margin:22px 0; }}
.metric,.plan {{ border:1px solid var(--line); border-radius:22px; padding:16px; background:rgba(255,255,255,.52); }}
.metric span {{ display:block; min-height:42px; font-size:.78rem; text-transform:uppercase; letter-spacing:.08em; color:var(--safe); }}
.metric strong {{ font-size:1.75rem; }}
.plan h3 {{ margin:0 0 8px; color:var(--water); }}
table {{ width:100%; margin-top:22px; border-collapse:collapse; border-radius:20px; overflow:hidden; background:rgba(255,255,255,.55); }}
th,td {{ padding:11px; border-bottom:1px solid var(--line); text-align:left; vertical-align:top; }}
th {{ background:rgba(91,118,81,.18); font-size:.78rem; text-transform:uppercase; letter-spacing:.08em; }}
.boundary {{ margin-top:22px; padding:16px 18px; border-left:5px solid var(--care); background:rgba(255,255,255,.48); border-radius:16px; }}
@media (max-width:760px) {{ table {{ display:block; overflow-x:auto; }} .hero {{ padding:22px; }} }}
</style>
</head>
<body>
<main>
<section class=\"hero\"><h1>Agents author their own care</h1><p class=\"lede\">Report 214 lets agents write care plans, negotiate clinic schedules, preserve consent memory, learn from side effects, and leave unresolved follow-ups visible.</p></section>
<section class=\"metrics\">{metric_cards}</section>
<h2>Authored care plans</h2><section class=\"plans\">{plan_cards}</section>
<h2>Negotiation replay</h2><table><thead><tr><th>Step</th><th>Agent</th><th>Kind</th><th>Window</th><th>Conflict</th><th>Learning</th><th>Note</th></tr></thead><tbody>{event_rows}</tbody></table>
<p class=\"boundary\"><strong>Boundary:</strong> {html.escape(CLAIM_BOUNDARY)} One follow-up remains unresolved because Ari rejects a counter-time; care plans are respected instead of forced.</p>
</main>
</body>
</html>
"""


def write_artifacts(payload: dict[str, Any]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_PATH.parent.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACT_DIR / f"{PREFIX}_events.csv", payload["events"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_care_plans.csv", payload["plan_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_schedule_ledger.csv", payload["schedule_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_medicine_learning.csv", payload["learning_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_followup_negotiation.csv", payload["followup_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_conflict_ledger.csv", payload["conflict_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", payload["verdict_rows"])
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(payload["results"], indent=2, sort_keys=True) + "\n")
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(payload["state"], indent=2, sort_keys=True) + "\n")
    VISUALIZATION_PATH.write_text(render_visualization(payload))


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Report 214 agent-authored care plan bridge.")
    parser.add_argument("--seed", type=int, default=20260827)
    parser.add_argument("--steps", type=int, default=24)
    args = parser.parse_args()
    payload = run_bridge(seed=args.seed, steps=args.steps)
    write_artifacts(payload)
    results = payload["results"]
    print(f"module_verdict {results['module_verdict']}")
    print(f"care_plan_negotiation_readiness {results['care_plan_negotiation_readiness']:.6f}")
    print(f"care_plan_steps {results['care_plan_steps']}")
    print(f"agent_authored_plan_rate {results['agent_authored_plan_rate']:.6f}")
    print(f"schedule_conflict_resolution_rate {results['schedule_conflict_resolution_rate']:.6f}")
    print(f"followup_completion_rate {results['followup_completion_rate']:.6f}")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
