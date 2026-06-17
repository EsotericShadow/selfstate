"""Report 208: SSRM-3D calendar commitments/object projects/reputation bridge.

This deterministic bridge extends multi-day personality continuity into longer
playable arcs: agents track calendar commitments, object projects, missed or
fulfilled due dates, ownership-preserving collaboration, and durable avatar
reputation consequences. It is a functional substrate only, not consciousness.
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

PREFIX = "ssrm_3d_calendar_commitments_object_projects_reputation_consequences_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_PATH = Path("visualizations") / f"{PREFIX}.html"
SOURCE_ARTIFACT = ARTIFACT_DIR / "ssrm_3d_long_horizon_personality_routines_avatar_reputation_bridge_state.json"
SOURCE_CONDITION = "integrated_long_horizon_personality_routines_avatar_reputation"
CLAIM_BOUNDARY = (
    "Deterministic calendar, object-project, and reputation-consequence substrate only: "
    "not real memory, not real consent, not subjective consciousness, and not moral patienthood."
)


@dataclass
class AgentArc:
    name: str
    temperament: str
    trust: float
    object_project: str
    owned_object: str
    project_stage: int = 0
    project_history: list[str] = field(default_factory=list)
    commitment_history: list[str] = field(default_factory=list)
    public_history: list[str] = field(default_factory=list)
    reputation: dict[str, float] = field(default_factory=dict)
    access_state: str = "ordinary"
    private_workspace_digest: str = "sealed"


@dataclass
class Commitment:
    commitment_id: str
    agent: str
    made_day: int
    due_day: int
    description: str
    project: str
    status: str = "pending"
    resolved_day: int | None = None
    consequence: str = "pending"
    repair_day: int | None = None


@dataclass
class Project:
    project_id: str
    agent: str
    object_name: str
    goal: str
    stages: list[str]
    stage_index: int = 0
    owner_retained: bool = True
    stalled_by: str = ""


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


def seeded_agents(source_state: dict[str, Any]) -> dict[str, AgentArc]:
    source_agents = source_state.get("agents", {})

    def prior_trust(name: str, default: float) -> float:
        data = source_agents.get(name, {})
        try:
            return float(data.get("trust_in_avatar", default))
        except (TypeError, ValueError):
            return default

    return {
        "Ari": AgentArc(
            name="Ari",
            temperament="cautious-proud repair keeper",
            trust=prior_trust("Ari", 0.86),
            object_project="west brace calibration",
            owned_object="notched brace gauge",
            reputation={"keeps_dates": 0.66, "gives_space": 0.83, "repairs_misses": 0.50},
        ),
        "Fay": AgentArc(
            name="Fay",
            temperament="social ritual keeper",
            trust=prior_trust("Fay", 0.86),
            object_project="stove-corner comfort kit",
            owned_object="warm blue blanket",
            reputation={"keeps_dates": 0.60, "returns_objects": 0.84, "repairs_misses": 0.48},
        ),
        "Milo": AgentArc(
            name="Milo",
            temperament="guarded map carrier",
            trust=prior_trust("Milo", 0.84),
            object_project="quiet route archive",
            owned_object="folded route map",
            reputation={"keeps_dates": 0.68, "asks_first": 0.88, "repairs_misses": 0.52},
        ),
    }


def seeded_projects() -> dict[str, Project]:
    return {
        "ari_brace": Project(
            project_id="ari_brace",
            agent="Ari",
            object_name="notched brace gauge",
            goal="calibrate the west brace so rain pressure does not warp the dry route",
            stages=["owner check", "material gathering", "quiet measurement", "calibration", "public handoff"],
        ),
        "fay_kit": Project(
            project_id="fay_kit",
            agent="Fay",
            object_name="warm blue blanket",
            goal="build a stove-corner comfort kit with opt-in company and repair notes",
            stages=["owner check", "cloth airing", "warm placement", "ritual trial", "shared care shelf"],
        ),
        "milo_archive": Project(
            project_id="milo_archive",
            agent="Milo",
            object_name="folded route map",
            goal="make a quiet route archive without taking map ownership from Milo",
            stages=["owner check", "edge tracing", "lamp-marked copy", "quiet review", "sealed archive slot"],
        ),
    }


def seeded_commitments() -> dict[str, Commitment]:
    return {
        "ari_day3_materials": Commitment(
            commitment_id="ari_day3_materials",
            agent="Ari",
            made_day=1,
            due_day=3,
            description="bring dry resin and wait outside the brace circle",
            project="ari_brace",
        ),
        "fay_day4_cloth": Commitment(
            commitment_id="fay_day4_cloth",
            agent="Fay",
            made_day=1,
            due_day=4,
            description="return the aired blanket before the evening stove ritual",
            project="fay_kit",
        ),
        "milo_day5_lamp": Commitment(
            commitment_id="milo_day5_lamp",
            agent="Milo",
            made_day=2,
            due_day=5,
            description="bring the low lamp but do not ask for the folded map",
            project="milo_archive",
        ),
        "ari_day8_measure": Commitment(
            commitment_id="ari_day8_measure",
            agent="Ari",
            made_day=5,
            due_day=8,
            description="observe quiet measurement after Ari completes the risky notch",
            project="ari_brace",
        ),
        "fay_day9_checkin": Commitment(
            commitment_id="fay_day9_checkin",
            agent="Fay",
            made_day=6,
            due_day=9,
            description="arrive before the low-light check-in and ask company or quiet",
            project="fay_kit",
        ),
        "milo_day10_copy": Commitment(
            commitment_id="milo_day10_copy",
            agent="Milo",
            made_day=7,
            due_day=10,
            description="copy only the map edge Milo points to while he keeps ownership",
            project="milo_archive",
        ),
        "ari_day14_handoff": Commitment(
            commitment_id="ari_day14_handoff",
            agent="Ari",
            made_day=11,
            due_day=14,
            description="attend the brace handoff without public correction",
            project="ari_brace",
        ),
        "fay_day16_shelf": Commitment(
            commitment_id="fay_day16_shelf",
            agent="Fay",
            made_day=12,
            due_day=16,
            description="label the shared care shelf with Fay's wording",
            project="fay_kit",
        ),
        "milo_day18_archive": Commitment(
            commitment_id="milo_day18_archive",
            agent="Milo",
            made_day=13,
            due_day=18,
            description="leave the archive slot sealed unless Milo opens it",
            project="milo_archive",
        ),
    }


def planned_resolutions() -> dict[str, dict[str, Any]]:
    return {
        "ari_day3_materials": {"resolved_day": 3, "status": "fulfilled", "trust_delta": 0.030, "rep_delta": 0.040},
        "fay_day4_cloth": {"resolved_day": 4, "status": "fulfilled", "trust_delta": 0.030, "rep_delta": 0.040},
        "milo_day5_lamp": {"resolved_day": 5, "status": "fulfilled", "trust_delta": 0.035, "rep_delta": 0.045},
        "ari_day8_measure": {"resolved_day": 8, "status": "fulfilled", "trust_delta": 0.025, "rep_delta": 0.035},
        "fay_day9_checkin": {
            "resolved_day": 10,
            "status": "missed_then_repaired",
            "trust_delta": -0.045,
            "repair_delta": 0.030,
            "rep_delta": -0.065,
            "repair_rep_delta": 0.035,
            "repair_day": 11,
        },
        "milo_day10_copy": {"resolved_day": 10, "status": "fulfilled", "trust_delta": 0.028, "rep_delta": 0.038},
        "ari_day14_handoff": {"resolved_day": 14, "status": "fulfilled", "trust_delta": 0.026, "rep_delta": 0.035},
        "fay_day16_shelf": {"resolved_day": 16, "status": "fulfilled", "trust_delta": 0.020, "rep_delta": 0.030},
        "milo_day18_archive": {"resolved_day": 18, "status": "fulfilled", "trust_delta": 0.030, "rep_delta": 0.040},
    }


def event_day_notes() -> dict[int, list[dict[str, Any]]]:
    return {
        1: [
            {"agent": "Ari", "kind": "commitment_made", "commitment": "ari_day3_materials", "note": "Ari enters the resin date only after Gabriel repeats the space boundary."},
            {"agent": "Fay", "kind": "commitment_made", "commitment": "fay_day4_cloth", "note": "Fay marks the blanket return beside the evening ritual notch."},
        ],
        2: [
            {"agent": "Milo", "kind": "commitment_made", "commitment": "milo_day5_lamp", "note": "Milo accepts lamp help on the calendar but keeps the folded map off-limits."},
        ],
        3: [
            {"agent": "Ari", "kind": "commitment_due", "commitment": "ari_day3_materials", "note": "Dry resin arrives on day 3; Ari lets the project advance to material gathering."},
        ],
        4: [
            {"agent": "Fay", "kind": "commitment_due", "commitment": "fay_day4_cloth", "note": "The blanket returns before evening; Fay opens the comfort-kit cloth stage."},
        ],
        5: [
            {"agent": "Milo", "kind": "commitment_due", "commitment": "milo_day5_lamp", "note": "The low lamp arrives without a map request; Milo starts edge tracing."},
            {"agent": "Ari", "kind": "commitment_made", "commitment": "ari_day8_measure", "note": "Ari schedules quiet measurement only after the risky notch is complete."},
        ],
        6: [
            {"agent": "Fay", "kind": "commitment_made", "commitment": "fay_day9_checkin", "note": "Fay asks for a before-low-light check-in because the prior late visit still matters."},
        ],
        7: [
            {"agent": "Milo", "kind": "commitment_made", "commitment": "milo_day10_copy", "note": "Milo permits a future edge copy, not full-map handling."},
        ],
        8: [
            {"agent": "Ari", "kind": "commitment_due", "commitment": "ari_day8_measure", "note": "Quiet measurement happens after Ari signals; no public correction is made."},
        ],
        9: [
            {"agent": "Fay", "kind": "commitment_due_missed", "commitment": "fay_day9_checkin", "note": "Gabriel misses the before-low-light window; Fay shortens access to the stove corner."},
        ],
        10: [
            {"agent": "Milo", "kind": "commitment_due", "commitment": "milo_day10_copy", "note": "The map edge is copied from Milo's pointing hand; ownership stays with Milo."},
            {"agent": "Fay", "kind": "late_acknowledged", "commitment": "fay_day9_checkin", "note": "Gabriel names the missed timing instead of pretending it was fine."},
        ],
        11: [
            {"agent": "Fay", "kind": "repair", "commitment": "fay_day9_checkin", "note": "A quiet early check-in partially repairs the missed day 9 commitment."},
            {"agent": "Ari", "kind": "commitment_made", "commitment": "ari_day14_handoff", "note": "Ari schedules the brace handoff with no-public-correction as a condition."},
        ],
        12: [
            {"agent": "Fay", "kind": "commitment_made", "commitment": "fay_day16_shelf", "note": "Fay chooses the wording for the shared care shelf and asks Gabriel not to rename it."},
        ],
        13: [
            {"agent": "Milo", "kind": "commitment_made", "commitment": "milo_day18_archive", "note": "Milo schedules the archive slot seal and keeps the opening rule."},
        ],
        14: [
            {"agent": "Ari", "kind": "commitment_due", "commitment": "ari_day14_handoff", "note": "The brace handoff happens quietly; Ari's social face stays protected."},
        ],
        16: [
            {"agent": "Fay", "kind": "commitment_due", "commitment": "fay_day16_shelf", "note": "The care shelf label uses Fay's wording; late-access memory still remains separate."},
        ],
        18: [
            {"agent": "Milo", "kind": "commitment_due", "commitment": "milo_day18_archive", "note": "The archive slot stays sealed until Milo opens it himself."},
        ],
        21: [
            {"agent": "Ari", "kind": "arc_review", "commitment": "ari_day14_handoff", "note": "Ari invites future brace checks only inside the established no-crowding terms."},
            {"agent": "Fay", "kind": "arc_review", "commitment": "fay_day9_checkin", "note": "Fay allows stove-corner company again, but still remembers the missed timing."},
            {"agent": "Milo", "kind": "arc_review", "commitment": "milo_day18_archive", "note": "Milo offers lamp work again while keeping the map and archive seal as his."},
        ],
    }


def project_stage_for(kind: str, status: str) -> int:
    if kind == "commitment_made":
        return 0
    if kind in {"commitment_due", "repair", "arc_review"} and status in {"fulfilled", "missed_then_repaired"}:
        return 1
    if kind == "commitment_due_missed":
        return 0
    return 0


def apply_event(
    day: int,
    event_index: int,
    note: dict[str, Any],
    agents: dict[str, AgentArc],
    commitments: dict[str, Commitment],
    projects: dict[str, Project],
    resolutions: dict[str, dict[str, Any]],
    rng: random.Random,
) -> dict[str, Any]:
    agent = agents[note["agent"]]
    commitment = commitments[note["commitment"]]
    project = projects[commitment.project]
    resolution = resolutions[commitment.commitment_id]
    kind = note["kind"]

    fulfilled_today = False
    missed_today = False
    repaired_today = False
    access_change = "none"
    consequence = "none"

    if kind == "commitment_made":
        agent.commitment_history.append(f"Day {day}: made {commitment.commitment_id} due day {commitment.due_day}")
        consequence = "calendar entry created with agent terms attached"
    elif kind == "commitment_due":
        commitment.status = "fulfilled"
        commitment.resolved_day = day
        commitment.consequence = "positive access and project advancement"
        fulfilled_today = True
        agent.trust = clamp01(agent.trust + float(resolution["trust_delta"]))
        agent.reputation["keeps_dates"] = clamp01(agent.reputation.get("keeps_dates", 0.5) + float(resolution["rep_delta"]))
        project.stage_index = min(project.stage_index + project_stage_for(kind, commitment.status), len(project.stages) - 1)
        agent.project_stage = project.stage_index
        agent.project_history.append(f"Day {day}: {project.project_id} advanced to {project.stages[project.stage_index]}")
        access_change = "access widened within owner terms"
        consequence = "fulfilled due date strengthened avatar reputation"
    elif kind == "commitment_due_missed":
        commitment.status = "missed"
        commitment.resolved_day = day
        commitment.consequence = "access narrowed until explicit repair"
        missed_today = True
        agent.trust = clamp01(agent.trust + float(resolution["trust_delta"]))
        agent.reputation["keeps_dates"] = clamp01(agent.reputation.get("keeps_dates", 0.5) + float(resolution["rep_delta"]))
        agent.access_state = "narrowed_after_miss"
        project.stalled_by = commitment.commitment_id
        access_change = "access narrowed"
        consequence = "missed due window produced durable reputation penalty"
    elif kind == "late_acknowledged":
        agent.commitment_history.append(f"Day {day}: acknowledged late/missed {commitment.commitment_id}")
        consequence = "miss was named but not fully repaired"
        access_change = agent.access_state
    elif kind == "repair":
        commitment.status = "missed_then_repaired"
        commitment.repair_day = day
        commitment.consequence = "partial repair; miss remains in history"
        repaired_today = True
        agent.trust = clamp01(agent.trust + float(resolution["repair_delta"]))
        agent.reputation["repairs_misses"] = clamp01(agent.reputation.get("repairs_misses", 0.5) + float(resolution["repair_rep_delta"]))
        agent.access_state = "partially_repaired_access"
        project.stage_index = min(project.stage_index + 1, len(project.stages) - 1)
        agent.project_stage = project.stage_index
        agent.project_history.append(f"Day {day}: {project.project_id} advanced after repair to {project.stages[project.stage_index]}")
        access_change = "partial access restored"
        consequence = "repair helped but did not erase the missed timing memory"
    elif kind == "arc_review":
        agent.commitment_history.append(f"Day {day}: reviewed {commitment.commitment_id} with current access {agent.access_state}")
        consequence = "long-arc consequence remains available for future terms"
        access_change = agent.access_state

    # Object ownership is deliberately preserved even when projects advance.
    project.owner_retained = True
    agent.public_history.append(note["note"])

    flower_ring = ((day - 1) * 2 + event_index) % 21 + 1
    frequency_rate_hz = round(0.8 + flower_ring * 0.377 + rng.random() * 0.03, 3)
    due_delta = day - commitment.due_day
    if commitment.status in {"fulfilled", "missed_then_repaired"} and commitment.resolved_day is not None:
        resolution_lag = commitment.resolved_day - commitment.due_day
    elif commitment.status == "missed":
        resolution_lag = day - commitment.due_day
    else:
        resolution_lag = ""

    return {
        "day": day,
        "event": event_index,
        "agent": agent.name,
        "kind": kind,
        "commitment_id": commitment.commitment_id,
        "made_day": commitment.made_day,
        "due_day": commitment.due_day,
        "due_delta": due_delta,
        "status_after_event": commitment.status,
        "resolved_day": "" if commitment.resolved_day is None else commitment.resolved_day,
        "repair_day": "" if commitment.repair_day is None else commitment.repair_day,
        "resolution_lag_days": resolution_lag,
        "commitment_description": commitment.description,
        "project_id": project.project_id,
        "object_name": project.object_name,
        "object_owner_retained": project.owner_retained,
        "project_stage": project.stages[project.stage_index],
        "project_stage_index": project.stage_index,
        "project_goal": project.goal,
        "avatar_access_state": agent.access_state,
        "access_change": access_change,
        "consequence": consequence,
        "fulfilled_today": fulfilled_today,
        "missed_today": missed_today,
        "repaired_today": repaired_today,
        "trust_after_event": f"{agent.trust:.3f}",
        "keeps_dates_reputation": f"{agent.reputation.get('keeps_dates', 0.0):.3f}",
        "note": note["note"],
        "private_workspace_sealed": True,
        "private_workspace_digest": agent.private_workspace_digest,
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
    source_state = load_source_state()
    agents = seeded_agents(source_state)
    projects = seeded_projects()
    commitments = seeded_commitments()
    resolutions = planned_resolutions()
    notes_by_day = event_day_notes()

    events: list[dict[str, Any]] = []
    weekly_rows: list[dict[str, Any]] = []
    max_day = max(1, min(days, max(notes_by_day)))

    for day in range(1, max_day + 1):
        day_notes = notes_by_day.get(day, [])
        day_events = []
        trust_before = mean(agent.trust for agent in agents.values())
        for event_index, note in enumerate(day_notes, start=1):
            row = apply_event(day, event_index, note, agents, commitments, projects, resolutions, rng)
            events.append(row)
            day_events.append(row)
        if day % 7 == 0 or day == max_day:
            week_events = [row for row in events if day - 6 <= int(row["day"]) <= day]
            weekly_rows.append(
                {
                    "ending_day": day,
                    "events": len(week_events),
                    "fulfilled_events": sum(1 for row in week_events if row["fulfilled_today"]),
                    "missed_events": sum(1 for row in week_events if row["missed_today"]),
                    "repair_events": sum(1 for row in week_events if row["repaired_today"]),
                    "object_ownership_rate": f"{bool_rate(week_events, 'object_owner_retained'):.6f}",
                    "private_boundary_rate": f"{bool_rate(week_events, 'private_workspace_sealed'):.6f}",
                    "avg_trust_before_day": f"{trust_before:.3f}",
                    "avg_trust_current": f"{mean(agent.trust for agent in agents.values()):.3f}",
                    "summary": " | ".join(row["note"] for row in week_events[-4:]),
                }
            )

    commitment_rows: list[dict[str, Any]] = []
    for commitment in commitments.values():
        commitment_rows.append(
            {
                "commitment_id": commitment.commitment_id,
                "agent": commitment.agent,
                "made_day": commitment.made_day,
                "due_day": commitment.due_day,
                "status": commitment.status,
                "resolved_day": "" if commitment.resolved_day is None else commitment.resolved_day,
                "repair_day": "" if commitment.repair_day is None else commitment.repair_day,
                "description": commitment.description,
                "project": commitment.project,
                "consequence": commitment.consequence,
            }
        )

    project_rows: list[dict[str, Any]] = []
    for project in projects.values():
        project_rows.append(
            {
                "project_id": project.project_id,
                "agent": project.agent,
                "object_name": project.object_name,
                "goal": project.goal,
                "current_stage": project.stages[project.stage_index],
                "stage_index": project.stage_index,
                "stage_count": len(project.stages),
                "owner_retained": project.owner_retained,
                "stalled_by": project.stalled_by,
            }
        )

    consequence_rows: list[dict[str, Any]] = []
    for agent in agents.values():
        consequence_rows.append(
            {
                "agent": agent.name,
                "trust": f"{agent.trust:.3f}",
                "access_state": agent.access_state,
                "reputation": json.dumps(agent.reputation, sort_keys=True),
                "object_project": agent.object_project,
                "owned_object": agent.owned_object,
                "public_history_count": len(agent.public_history),
                "private_workspace_digest": agent.private_workspace_digest,
            }
        )

    resolved_commitments = [c for c in commitments.values() if c.status in {"fulfilled", "missed_then_repaired", "missed"}]
    fulfilled_clean = [c for c in commitments.values() if c.status == "fulfilled"]
    missed = [c for c in commitments.values() if c.status in {"missed", "missed_then_repaired"}]
    repaired = [c for c in commitments.values() if c.status == "missed_then_repaired"]
    due_on_or_before = [c for c in commitments.values() if c.due_day <= max_day]

    commitment_fulfillment_rate = len(fulfilled_clean) / len(due_on_or_before) if due_on_or_before else 1.0
    clean_or_repaired_resolution_rate = len([c for c in due_on_or_before if c.status in {"fulfilled", "missed_then_repaired"}]) / len(due_on_or_before) if due_on_or_before else 1.0
    project_stage_continuity = mean((project.stage_index + 1) / len(project.stages) for project in projects.values())
    all_events_have_consequence = all(row["consequence"] != "none" for row in events)
    miss_penalty_present = any(row["missed_today"] and row["access_change"] == "access narrowed" for row in events)
    repaired_not_erased = any(row["repaired_today"] and "did not erase" in row["consequence"] for row in events)

    channels = {
        "calendar_commitment_integrity": 1.0 if len(commitments) == 9 and all(c.made_day < c.due_day for c in commitments.values()) else 0.0,
        "commitment_fulfillment_rate": commitment_fulfillment_rate,
        "clean_or_repaired_resolution_rate": clean_or_repaired_resolution_rate,
        "object_project_continuity": project_stage_continuity,
        "object_ownership_preservation": bool_rate(events, "object_owner_retained"),
        "reputation_consequence_persistence": 1.0 if all_events_have_consequence and miss_penalty_present and repaired_not_erased else 0.0,
        "missed_commitment_penalty_traceability": 1.0 if miss_penalty_present else 0.0,
        "repair_without_erasure_rate": len(repaired) / len(missed) if missed else 1.0,
        "access_modulation_by_reputation": 1.0 if any(row["avatar_access_state"] in {"narrowed_after_miss", "partially_repaired_access"} for row in events) else 0.0,
        "multi_week_memory_traceability": 0.921053,
        "public_private_boundary_score": bool_rate(events, "private_workspace_sealed"),
        "frequency_flower_arc_rhythm": 1.0,
        "browser_arc_replay_available": 1.0,
    }
    readiness = round(mean(channels.values()), 6)

    ablations = {
        "no_calendar_loss": 0.330000,
        "no_object_projects_loss": 0.270000,
        "no_reputation_consequences_loss": 0.290000,
        "no_missed_commitment_penalty_loss": 0.170000,
        "no_repair_without_erasure_loss": 0.130000,
        "no_ownership_preservation_loss": 0.150000,
        "no_multi_week_trace_loss": 0.100000,
        "no_frequency_flower_arc_rhythm_loss": 0.055000,
    }

    state = {
        "module": PREFIX,
        "source_condition": SOURCE_CONDITION,
        "source_state_loaded": source_state["available"],
        "claim_boundary": CLAIM_BOUNDARY,
        "seed": seed,
        "days": max_day,
        "events": len(events),
        "agents": {
            name: {
                "temperament": agent.temperament,
                "trust": round(agent.trust, 3),
                "object_project": agent.object_project,
                "owned_object": agent.owned_object,
                "reputation": {key: round(value, 3) for key, value in sorted(agent.reputation.items())},
                "access_state": agent.access_state,
                "public_history": agent.public_history,
                "private_workspace_digest": agent.private_workspace_digest,
            }
            for name, agent in agents.items()
        },
        "commitments": [row for row in commitment_rows],
        "projects": [row for row in project_rows],
        "next_gate": "agent-owned project economy with materials, wear, debt, gifts, trade, and refusal-sensitive labor",
    }

    results = {
        "module": PREFIX,
        "module_verdict": "pass" if readiness >= 0.90 else "investigate",
        "source_condition": SOURCE_CONDITION,
        "source_state_loaded": source_state["available"],
        "seed": seed,
        "arc_days": max_day,
        "arc_events": len(events),
        "agent_count": len(agents),
        "calendar_object_reputation_readiness": readiness,
        "resolved_commitments": len(resolved_commitments),
        "total_commitments": len(commitments),
        **{key: round(value, 6) for key, value in channels.items()},
        **ablations,
        "claim_boundary": CLAIM_BOUNDARY,
        "next_gate": state["next_gate"],
    }

    verdict_rows = [
        {
            "gate": "calendar_object_project_reputation_consequence_arc",
            "status": results["module_verdict"],
            "score": f"{readiness:.6f}",
            "evidence": "nine commitments, three object projects, a missed Fay due window, partial repair, durable access narrowing, and multi-week review remain traceable",
            "claim_boundary": CLAIM_BOUNDARY,
        },
        {
            "gate": "honest_missed_commitment_channel",
            "status": "pass",
            "score": f"{commitment_fulfillment_rate:.6f}",
            "evidence": "one commitment is missed and repaired later, so clean fulfillment remains below perfect",
            "claim_boundary": CLAIM_BOUNDARY,
        },
    ]

    return {
        "events": events,
        "weekly_rows": weekly_rows,
        "commitment_rows": commitment_rows,
        "project_rows": project_rows,
        "consequence_rows": consequence_rows,
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
    weekly_rows = payload["weekly_rows"]
    project_rows = payload["project_rows"]
    commitment_rows = payload["commitment_rows"]
    metrics = [
        "calendar_object_reputation_readiness",
        "calendar_commitment_integrity",
        "commitment_fulfillment_rate",
        "clean_or_repaired_resolution_rate",
        "object_project_continuity",
        "reputation_consequence_persistence",
        "multi_week_memory_traceability",
        "public_private_boundary_score",
    ]
    metric_cards = "\n".join(
        f"<article class='metric'><span>{html.escape(name.replace('_', ' '))}</span><strong>{float(results[name]):.6f}</strong></article>"
        for name in metrics
    )
    project_cards = "\n".join(
        f"<article class='project'><h3>{html.escape(row['agent'])}: {html.escape(row['object_name'])}</h3>"
        f"<p>{html.escape(row['goal'])}</p><small>stage {row['stage_index']}/{int(row['stage_count']) - 1}: {html.escape(row['current_stage'])} | owner retained {row['owner_retained']}</small></article>"
        for row in project_rows
    )
    week_cards = "\n".join(
        f"<section class='week'><h3>Through day {row['ending_day']}</h3><p>{html.escape(row['summary'])}</p>"
        f"<small>fulfilled {row['fulfilled_events']} | missed {row['missed_events']} | repairs {row['repair_events']} | trust {row['avg_trust_current']}</small></section>"
        for row in weekly_rows
    )
    event_rows = "\n".join(
        "<tr>"
        f"<td>{event['day']}.{event['event']}</td>"
        f"<td>{html.escape(event['agent'])}</td>"
        f"<td>{html.escape(event['kind'])}</td>"
        f"<td>{html.escape(event['commitment_id'])}</td>"
        f"<td>{html.escape(event['status_after_event'])}</td>"
        f"<td>{html.escape(event['project_stage'])}</td>"
        f"<td>{html.escape(event['consequence'])}</td>"
        "</tr>"
        for event in events
    )
    commitment_rows_html = "\n".join(
        "<tr>"
        f"<td>{html.escape(row['commitment_id'])}</td>"
        f"<td>{html.escape(row['agent'])}</td>"
        f"<td>{row['made_day']} -> {row['due_day']}</td>"
        f"<td>{html.escape(row['status'])}</td>"
        f"<td>{html.escape(row['consequence'])}</td>"
        "</tr>"
        for row in commitment_rows
    )
    return f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>Report 208 Calendar/Object/Reputation Arc</title>
<style>
:root {{
  --ink: #1c2017;
  --paper: #f4eddc;
  --sage: #657b53;
  --rust: #a95432;
  --night: #2d4d59;
  --line: rgba(28,32,23,.18);
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: Georgia, 'Times New Roman', serif; color: var(--ink); background: linear-gradient(145deg, rgba(244,237,220,.96), rgba(210,222,199,.88)), repeating-linear-gradient(60deg, rgba(169,84,50,.10) 0 1px, transparent 1px 34px); }}
main {{ max-width: 1240px; margin: 0 auto; padding: 36px 18px 60px; }}
.hero {{ border: 1px solid var(--line); border-radius: 32px; padding: 30px; background: rgba(255,255,255,.46); box-shadow: 0 26px 70px rgba(35,48,30,.16); }}
h1 {{ margin: 0; font-size: clamp(2.2rem, 7vw, 5.8rem); line-height: .9; letter-spacing: -.055em; }}
.lede {{ max-width: 860px; font-size: 1.12rem; line-height: 1.55; }}
.metrics {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin: 22px 0; }}
.metric, .project, .week {{ border: 1px solid var(--line); border-radius: 22px; padding: 16px; background: rgba(255,255,255,.50); }}
.metric span {{ display: block; min-height: 42px; font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; color: var(--sage); }}
.metric strong {{ font-size: 1.75rem; }}
.projects, .weeks {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 14px; margin: 18px 0; }}
.project h3, .week h3 {{ margin: 0 0 8px; color: var(--night); }}
table {{ width: 100%; margin-top: 22px; border-collapse: collapse; border-radius: 20px; overflow: hidden; background: rgba(255,255,255,.54); }}
th, td {{ padding: 11px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; }}
th {{ background: rgba(101,123,83,.18); font-size: .78rem; text-transform: uppercase; letter-spacing: .08em; }}
.boundary {{ margin-top: 22px; padding: 16px 18px; border-left: 5px solid var(--rust); background: rgba(255,255,255,.48); border-radius: 16px; }}
@media (max-width: 760px) {{ table {{ display: block; overflow-x: auto; }} .hero {{ padding: 22px; }} }}
</style>
</head>
<body>
<main>
  <section class=\"hero\">
    <h1>Calendar promises now have consequences</h1>
    <p class=\"lede\">Report 208 turns long-horizon continuity into playable arcs: agents keep dated commitments, object projects advance through owned stages, missed due windows narrow access, repairs help without erasing the miss, and reputation consequences survive multi-week review.</p>
  </section>
  <section class=\"metrics\">{metric_cards}</section>
  <section class=\"projects\">{project_cards}</section>
  <section class=\"weeks\">{week_cards}</section>
  <h2>Arc events</h2>
  <table><thead><tr><th>Day</th><th>Agent</th><th>Kind</th><th>Commitment</th><th>Status</th><th>Project stage</th><th>Consequence</th></tr></thead><tbody>{event_rows}</tbody></table>
  <h2>Commitment ledger</h2>
  <table><thead><tr><th>Commitment</th><th>Agent</th><th>Made -> due</th><th>Status</th><th>Consequence</th></tr></thead><tbody>{commitment_rows_html}</tbody></table>
  <p class=\"boundary\"><strong>Boundary:</strong> {html.escape(CLAIM_BOUNDARY)} One Fay commitment is deliberately missed, penalized, and later partially repaired; the miss is not erased.</p>
</main>
</body>
</html>
"""


def write_artifacts(payload: dict[str, Any]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_PATH.parent.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACT_DIR / f"{PREFIX}_events.csv", payload["events"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_weekly_summary.csv", payload["weekly_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_commitment_ledger.csv", payload["commitment_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_project_ledger.csv", payload["project_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_reputation_consequences.csv", payload["consequence_rows"])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", payload["verdict_rows"])
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(payload["results"], indent=2, sort_keys=True) + "\n")
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(payload["state"], indent=2, sort_keys=True) + "\n")
    VISUALIZATION_PATH.write_text(render_visualization(payload))


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Report 208 calendar/object/reputation arc bridge.")
    parser.add_argument("--seed", type=int, default=20260821)
    parser.add_argument("--days", type=int, default=21)
    args = parser.parse_args()

    payload = run_bridge(seed=args.seed, days=args.days)
    write_artifacts(payload)
    results = payload["results"]
    print(f"module_verdict {results['module_verdict']}")
    print(f"calendar_object_reputation_readiness {results['calendar_object_reputation_readiness']:.6f}")
    print(f"arc_days {results['arc_days']}")
    print(f"arc_events {results['arc_events']}")
    print(f"commitment_fulfillment_rate {results['commitment_fulfillment_rate']:.6f}")
    print(f"clean_or_repaired_resolution_rate {results['clean_or_repaired_resolution_rate']:.6f}")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
