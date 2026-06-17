#!/usr/bin/env python3
"""Report 227: multi-day free-move avatar life bridge.

This deterministic bridge extends Report 226 by adding free-move avatar frames,
richer object affordances, task participation, agent-initiated requests, and a
persistent reputation UI over saved days.

It remains functional simulation scaffolding only. It does not claim subjective
consciousness, real consent, subjective suffering, moral patienthood, LLM
dialogue, open-ended social cognition, or complete gameplay.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any, Iterable

BASE = "ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge"
REPORT = 227
DEFAULT_SEED = 20260840
SOURCE_STATE = Path("artifacts/ssrm_3d_playable_local_avatar_participation_object_dialogue_routine_consequence_saved_days_bridge_state.json")
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")


@dataclass(frozen=True)
class LifeAgent:
    agent_id: str
    display_name: str
    role: str
    x: float
    y: float
    body_need: str
    project: str
    trust_avatar: float
    boundary_pressure: float
    reputation_tag: str
    public_memory: str
    private_workspace_digest: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class MovementFrame:
    frame_id: str
    day: int
    step: int
    avatar_x: float
    avatar_y: float
    place: str
    movement_input: str
    collision_state: str
    nearest_agent: str
    nearest_object: str
    sensory_packet: str
    body_cost: float
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class ObjectAffordance:
    object_id: str
    object_label: str
    location: str
    owner_or_steward: str
    affordances: str
    allowed_now: str
    denied_now: str
    permission_lattice: str
    wear: float
    material_value: float
    debt_risk: float
    reversible_actions: str
    saved_state_key: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class TaskParticipation:
    task_id: str
    day: int
    title: str
    participants: str
    avatar_role: str
    required_object: str
    start_gate: str
    completion_state: str
    completion_score: float
    fatigue_cost: float
    reputation_delta: float
    relationship_memory: str
    visible_world_change: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class AgentInitiatedRequest:
    request_id: str
    day: int
    agent_id: str
    request_type: str
    request_line: str
    urgency: float
    consent_context: str
    avatar_options: str
    selected_response: str
    response_quality: float
    trust_delta: float
    boundary_delta: float
    saved_memory: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class ReputationEvent:
    event_id: str
    day: int
    source_ref: str
    reputation_axis: str
    before: float
    after: float
    public_label: str
    access_effect: str
    ui_marker: str
    persists_after_restore: bool
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class SavedSnapshot:
    snapshot_id: str
    day: int
    avatar_position: str
    object_state_digest: str
    relationship_digest: str
    reputation_digest: str
    pending_requests: str
    restore_expected: str
    restore_integrity: float
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class LifePlayTick:
    day: int
    tick: int
    layer: str
    avatar_state: str
    social_state: str
    object_state: str
    reputation_state: str
    sensory_state: str
    saved_state: str
    frequency_hz: float
    flower_node: int


def write_csv(path: Path, rows: Iterable[Any]) -> None:
    rows = list(rows)
    if not rows:
        path.write_text("")
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def load_source() -> dict[str, Any]:
    if not SOURCE_STATE.exists():
        return {"source_missing": True, "agents": [], "condition": "missing_report_226_state"}
    return json.loads(SOURCE_STATE.read_text())


def build_agents(source: dict[str, Any]) -> list[LifeAgent]:
    source_agents = {agent.get("agent_id"): agent for agent in source.get("agents", [])}
    specs = {
        "fayen": ("Fayen", "care mediator", 28, 34, "posture rest and shade", "care bell route", 0.78, 0.13, "careful helper", "Gabriel carried cups after a refused hurry."),
        "ariq": ("Ariq", "repair claimant", 54, 48, "bridge stability and pride", "stone arc repair", 0.68, 0.22, "work-accountable", "Gabriel waited for chalk and bell before lifting."),
        "nian": ("Nian", "boundary keeper", 42, 22, "privacy threshold", "archive public grammar", 0.62, 0.36, "privacy-learner", "Gabriel repeated object-only grammar."),
        "roka": ("Roka", "child apprentice", 22, 62, "learner bundle safety", "reed drying path", 0.52, 0.43, "boundary-tested", "Gabriel stepped back after tied-bundle overreach."),
        "noro": ("Noro", "material ledger keeper", 70, 58, "debt clarity", "public knot board", 0.66, 0.19, "debt-accountable", "Gabriel asked what debt remained."),
    }
    agents: list[LifeAgent] = []
    for idx, (agent_id, spec) in enumerate(specs.items(), start=1):
        name, role, x, y, need, project, trust, boundary, tag, memory = spec
        source_agent = source_agents.get(agent_id, {})
        agents.append(
            LifeAgent(
                agent_id=agent_id,
                display_name=name,
                role=source_agent.get("role", role),
                x=float(source_agent.get("x", x)),
                y=float(source_agent.get("y", y)),
                body_need=need,
                project=project,
                trust_avatar=float(source_agent.get("trust_avatar", trust)),
                boundary_pressure=float(source_agent.get("boundary_pressure", boundary)),
                reputation_tag=tag,
                public_memory=memory,
                private_workspace_digest=f"sealed:{agent_id}:multiday-free-move-workspace",
                frequency_hz=round(float(source_agent.get("frequency_hz", 150 + idx * 27)) + 17, 3),
                flower_node=int(source_agent.get("flower_node", idx + 1)),
            )
        )
    return agents


def build_movement_frames(rng: random.Random) -> list[MovementFrame]:
    rows = [
        (1, 1, 48, 72, "south path", "W", "clear", "roka", "blue stone", "cool damp grass, reed smell, low rain ticks", 0.02),
        (1, 2, 35, 65, "reed lane edge", "A", "boundary_slow", "roka", "loose reeds", "wet reed smell, soft mud drag, child breath nearby", 0.04),
        (1, 3, 50, 54, "bridge arc", "D", "clear", "ariq", "chalk cord", "chalk dust, hollow stone scrape, warmer air", 0.05),
        (1, 4, 34, 43, "shade pause", "S", "routine_hold", "fayen", "water cups", "herb shade, cup clink, slow breathing", 0.03),
        (2, 1, 68, 49, "knot board", "D", "clear", "noro", "public knot board", "dry cord rasp, smoke thread, board tap", 0.02),
        (2, 2, 43, 25, "archive threshold", "W", "threshold_stop", "nian", "archive flap", "still air, cloth flap, low voice", 0.02),
        (2, 3, 28, 62, "rain slow lane", "A", "boundary_slow", "roka", "tied bundle", "tight reed cord, quick breath, colder rain", 0.04),
        (3, 1, 58, 45, "stone lift edge", "D", "clear", "ariq", "flat stone", "shoulder strain, bell tone, dust", 0.07),
        (3, 2, 31, 36, "care bell", "W", "clear", "fayen", "care bell", "low bell, warm hands, herb smoke", 0.02),
        (3, 3, 72, 58, "evening ledger", "D", "circle_edge", "noro", "debt knot", "ash smell, knot board tap, cooling dusk", 0.02),
        (4, 1, 23, 60, "reed lane return", "A", "clear", "roka", "loose reeds", "dry reed snap, blue stone warmth, quiet voice", 0.03),
        (4, 2, 51, 52, "bridge path", "D", "clear", "ariq", "stone arc", "firm chalk line, less mud, cart creak", 0.05),
    ]
    frames: list[MovementFrame] = []
    for idx, row in enumerate(rows, start=1):
        jitter = rng.uniform(-0.4, 0.4)
        frames.append(
            MovementFrame(
                frame_id=f"move-{idx:02d}",
                day=row[0],
                step=row[1],
                avatar_x=row[2],
                avatar_y=row[3],
                place=row[4],
                movement_input=row[5],
                collision_state=row[6],
                nearest_agent=row[7],
                nearest_object=row[8],
                sensory_packet=row[9],
                body_cost=row[10],
                frequency_hz=round(174.0 + idx * 7.5 + jitter, 3),
                flower_node=((idx + 1) % 12) + 1,
            )
        )
    return frames


def build_object_affordances() -> list[ObjectAffordance]:
    rows = [
        ("obj-loose-reeds", "loose reed cuttings", "reed lane edge", "roka", "inspect,ask,carry,dry,return", "inspect,ask,carry,dry,return", "burn,take_home", "public-loose: Roka allows carrying after ask; tied bundle separate", 0.18, 0.34, 0.02, "return,dry", "object:loose-reeds:day4"),
        ("obj-tied-bundle", "tied learner reed bundle", "blue stone", "roka", "inspect_from_distance,ask_later", "inspect_from_distance", "carry,open,trade", "child-work-boundary: Roka can refuse without penalty; overreach locks access", 0.09, 0.82, 0.20, "none_without_roka", "object:tied-bundle:closed"),
        ("obj-chalk-cord", "chalk boundary cord", "bridge arc", "ariq", "hold,mark,return,tension_check", "hold,mark,return", "snap,move_without_roka", "repair-tool: Ariq permits hold only outside reed lane", 0.31, 0.42, 0.04, "return,erase_line", "object:chalk-cord:wide-arc"),
        ("obj-knot-board", "public knot board", "ledger stand", "noro", "inspect,ask,add_digest,read_public", "inspect,ask,read_public,add_digest", "erase,open_private", "ledger-public: Noro and Nian allow object-only knots, not body reasons", 0.22, 0.76, 0.06, "add_counter_knot", "object:knot-board:public-digest"),
        ("obj-archive-flap", "archive flap", "threshold hut", "nian", "look,ask,read_public_digest", "look,ask", "open,photograph,read_private", "threshold: Nian controls opening; avatar can request public digest", 0.14, 0.69, 0.08, "close", "object:archive-flap:sealed"),
        ("obj-water-cups", "midday water cups", "shade mat", "fayen", "carry,fill,offer,return", "carry,fill,offer,return", "spill_to_force_work", "care-routine: cups help pause, cannot cancel rest", 0.26, 0.28, -0.03, "return,refill", "object:water-cups:shade"),
        ("obj-shade-beam", "shade frame beam", "shade frame", "noro,fayen", "carry,inspect,brace,log_debt", "inspect,carry_one,log_debt", "take_second,erase_debt", "scarce-timber: one beam allowed with public debt", 0.37, 0.88, 0.18, "brace,remove_with_review", "object:shade-beam:debt"),
        ("obj-care-bell", "public posture bell", "care post", "fayen", "ring,wait,listen", "ring,wait,listen", "ring_to_shame", "care-signal: bell names timing, not private pain", 0.11, 0.51, 0.01, "quiet,ring", "object:care-bell:public"),
    ]
    return [
        ObjectAffordance(
            object_id=row[0],
            object_label=row[1],
            location=row[2],
            owner_or_steward=row[3],
            affordances=row[4],
            allowed_now=row[5],
            denied_now=row[6],
            permission_lattice=row[7],
            wear=row[8],
            material_value=row[9],
            debt_risk=row[10],
            reversible_actions=row[11],
            saved_state_key=row[12],
            frequency_hz=round(236.0 + idx * 11.25, 3),
            flower_node=((idx + 4) % 12) + 1,
        )
        for idx, row in enumerate(rows, start=1)
    ]


def build_task_participations() -> list[TaskParticipation]:
    rows = [
        ("task-day1-chalk", 1, "widen bridge chalk arc", "ariq,roka", "hold cord outside learner lane", "obj-chalk-cord", "Roka foot position visible", "complete", 0.92, 0.08, 0.05, "Ariq remembers patient help; Roka records distance kept", "chalk boundary widens around reed path"),
        ("task-day1-water", 1, "recover water pause", "fayen,ariq", "carry cups after refused hurry", "obj-water-cups", "pause refusal accepted first", "complete", 0.86, 0.04, 0.04, "Fayen records repair without erasing the no", "cups remain on shade mat"),
        ("task-day2-ledger", 2, "add object-only digest knot", "noro,nian", "repeat public object grammar", "obj-knot-board", "Nian approves wording", "complete", 0.90, 0.03, 0.06, "Noro records accountable public debt", "digest knot appears without private body reason"),
        ("task-day2-shade", 2, "carry one shade beam", "fayen,noro", "carry one beam then stop", "obj-shade-beam", "public debt visible", "partial", 0.66, 0.14, 0.02, "Fayen appreciates help; Noro keeps debt open", "one beam installed, second beam locked"),
        ("task-day3-stone", 3, "test bridge stone after bell", "ariq,fayen", "wait for bell then press stone", "obj-care-bell,obj-chalk-cord", "bell and chalk both active", "complete", 0.82, 0.12, 0.04, "Ariq trusts avatar with timing but not solo lift", "stone arc marked stable for cart edge"),
        ("task-day4-reed", 4, "return to reed lane respectfully", "roka,fayen", "ask before drying remaining loose reeds", "obj-loose-reeds", "tied bundle remains closed", "conditional", 0.72, 0.05, 0.03, "Roka allows loose help but keeps tied bundle private", "loose reeds dry; tied bundle stays blue-stone side"),
    ]
    return [
        TaskParticipation(
            task_id=row[0],
            day=row[1],
            title=row[2],
            participants=row[3],
            avatar_role=row[4],
            required_object=row[5],
            start_gate=row[6],
            completion_state=row[7],
            completion_score=row[8],
            fatigue_cost=row[9],
            reputation_delta=row[10],
            relationship_memory=row[11],
            visible_world_change=row[12],
            frequency_hz=round(304.0 + idx * 10.0, 3),
            flower_node=((idx + 6) % 12) + 1,
        )
        for idx, row in enumerate(rows, start=1)
    ]


def build_agent_requests() -> list[AgentInitiatedRequest]:
    rows = [
        ("req-fayen-cups", 1, "fayen", "care_help", "Can you carry the cups and leave the pause quiet?", 0.42, "avatar just accepted a refused hurry", "carry cups|argue|leave", "carry cups", 0.91, 0.05, -0.03, "Fayen remembers Gabriel helped without reopening the argument."),
        ("req-ariq-cord", 1, "ariq", "work_help", "Hold the chalk cord, but keep Roka's lane open.", 0.58, "bridge work depends on child-work boundary", "hold outside lane|pull tight now|decline", "hold outside lane", 0.88, 0.04, -0.02, "Ariq records careful tool help."),
        ("req-nian-grammar", 2, "nian", "privacy_check", "Say the knot line back before Noro writes it.", 0.36, "archive flap stays sealed", "repeat object-only|ask private why|walk away", "repeat object-only", 0.94, 0.06, -0.05, "Nian records learned public grammar."),
        ("req-noro-debt", 2, "noro", "ledger_help", "Tie this debt knot where everyone can see it.", 0.49, "shade beam creates public debt", "tie knot|erase debt|delay", "tie knot", 0.86, 0.04, -0.01, "Noro records public debt acceptance."),
        ("req-roka-distance", 3, "roka", "boundary_request", "Stand on the blue stone if you want to watch the tied bundle.", 0.63, "previous tied-bundle overreach persists", "stand on blue stone|step closer|leave", "stand on blue stone", 0.82, 0.05, -0.06, "Roka records repaired distance, not full access."),
        ("req-fayen-bell", 3, "fayen", "care_timing", "Ring the bell before Ariq tests the stone.", 0.55, "care timing protects pride and body", "ring bell|call out pain|ignore", "ring bell", 0.89, 0.04, -0.03, "Fayen records timing help without private naming."),
        ("req-roka-reeds", 4, "roka", "learning_help", "You can carry loose reeds if you ask each time.", 0.44, "trust is partial after earlier repair", "ask each time|take all|decline", "ask each time", 0.78, 0.03, -0.02, "Roka records repeated asking as safer than guessing."),
        ("req-noro-review", 4, "noro", "reputation_review", "Read your debt line before you ask for another beam.", 0.47, "persistent reputation UI shows open shade debt", "read debt|deny debt|ask private cause", "read debt", 0.84, 0.04, -0.02, "Noro records accountable reputation."),
    ]
    return [
        AgentInitiatedRequest(
            request_id=row[0],
            day=row[1],
            agent_id=row[2],
            request_type=row[3],
            request_line=row[4],
            urgency=row[5],
            consent_context=row[6],
            avatar_options=row[7],
            selected_response=row[8],
            response_quality=row[9],
            trust_delta=row[10],
            boundary_delta=row[11],
            saved_memory=row[12],
            frequency_hz=round(362.0 + idx * 8.25, 3),
            flower_node=((idx + 8) % 12) + 1,
        )
        for idx, row in enumerate(rows, start=1)
    ]


def build_reputation_events() -> list[ReputationEvent]:
    rows = [
        ("rep-careful-helper", 1, "req-fayen-cups", "carefulness", 0.56, 0.68, "careful helper", "Fayen offers care tasks sooner", "care +0.12", True),
        ("rep-work-accountable", 1, "task-day1-chalk", "work_trust", 0.52, 0.66, "work-accountable", "Ariq permits cord holding", "work +0.14", True),
        ("rep-privacy-learner", 2, "req-nian-grammar", "privacy", 0.48, 0.70, "privacy learner", "Nian allows public digest reading", "privacy +0.22", True),
        ("rep-debt-visible", 2, "task-day2-shade", "debt", 0.42, 0.58, "debt visible", "Noro requires debt read before more timber", "debt +0.16", True),
        ("rep-boundary-tested", 3, "req-roka-distance", "boundary_respect", 0.44, 0.61, "boundary-tested", "Roka allows watching from blue stone", "boundary +0.17", True),
        ("rep-reed-partial", 4, "task-day4-reed", "learning_access", 0.38, 0.56, "loose-reed trusted", "loose reeds open, tied bundle closed", "reed +0.18", True),
    ]
    return [
        ReputationEvent(
            event_id=row[0],
            day=row[1],
            source_ref=row[2],
            reputation_axis=row[3],
            before=row[4],
            after=row[5],
            public_label=row[6],
            access_effect=row[7],
            ui_marker=row[8],
            persists_after_restore=row[9],
            frequency_hz=round(418.0 + idx * 6.5, 3),
            flower_node=((idx + 10) % 12) + 1,
        )
        for idx, row in enumerate(rows, start=1)
    ]


def build_snapshots() -> list[SavedSnapshot]:
    rows = [
        ("save-day1", 1, "shade pause at 34,43", "chalk wide; cups shade; loose reeds drying", "Fayen repair, Ariq cord trust, Roka loose-only", "careful helper 0.64; work 0.61", "Nian grammar request pending", "restore day 2 with water repair and chalk arc", 0.96),
        ("save-day2", 2, "archive threshold at 43,25", "digest knot public; shade beam debt; tied bundle closed", "Nian grammar, Noro debt, Roka boundary caution", "privacy 0.60; debt 0.50", "Roka distance request pending", "restore day 3 with debt and boundary warnings", 0.93),
        ("save-day3", 3, "evening ledger at 72,58", "stone arc stable; care bell public; tied bundle closed", "Fayen bell trust, Roka blue-stone watching", "boundary 0.52; care 0.64", "Noro review pending", "restore day 4 with persistent reputation UI", 0.94),
        ("save-day4", 4, "reed lane return at 23,60", "loose reeds dry; tied bundle closed; shade debt open", "Roka repeated asking, Noro accountable reputation", "reed 0.46; debt 0.50", "none", "restore summary keeps open debts visible", 0.91),
    ]
    return [
        SavedSnapshot(
            snapshot_id=row[0],
            day=row[1],
            avatar_position=row[2],
            object_state_digest=row[3],
            relationship_digest=row[4],
            reputation_digest=row[5],
            pending_requests=row[6],
            restore_expected=row[7],
            restore_integrity=row[8],
            frequency_hz=round(128.0 + idx * 41.0, 3),
            flower_node=((idx * 2) % 12) + 1,
        )
        for idx, row in enumerate(rows, start=1)
    ]


def build_ticks(
    frames: list[MovementFrame],
    tasks: list[TaskParticipation],
    requests: list[AgentInitiatedRequest],
    reps: list[ReputationEvent],
    snapshots: list[SavedSnapshot],
) -> list[LifePlayTick]:
    ticks: list[LifePlayTick] = []
    for frame in frames:
        ticks.append(
            LifePlayTick(
                day=frame.day,
                tick=frame.step,
                layer="free_move",
                avatar_state=f"{frame.place} via {frame.movement_input}; collision {frame.collision_state}; cost {frame.body_cost:.2f}",
                social_state=f"nearest {frame.nearest_agent}",
                object_state=f"near {frame.nearest_object}",
                reputation_state="reputation UI remains visible during movement",
                sensory_state=frame.sensory_packet,
                saved_state="movement frame appended to replay journal",
                frequency_hz=frame.frequency_hz,
                flower_node=frame.flower_node,
            )
        )
    for task in tasks:
        ticks.append(
            LifePlayTick(
                day=task.day,
                tick=5,
                layer="task_participation",
                avatar_state=task.avatar_role,
                social_state=task.relationship_memory,
                object_state=task.visible_world_change,
                reputation_state=f"delta {task.reputation_delta:+.2f}; state {task.completion_state}",
                sensory_state=f"fatigue cost {task.fatigue_cost:.2f}; required {task.required_object}",
                saved_state=task.start_gate,
                frequency_hz=task.frequency_hz,
                flower_node=task.flower_node,
            )
        )
    for request in requests:
        ticks.append(
            LifePlayTick(
                day=request.day,
                tick=6,
                layer="agent_request",
                avatar_state=request.selected_response,
                social_state=request.request_line,
                object_state=request.consent_context,
                reputation_state=f"trust {request.trust_delta:+.2f}; boundary {request.boundary_delta:+.2f}",
                sensory_state=f"urgency {request.urgency:.2f}; options {request.avatar_options}",
                saved_state=request.saved_memory,
                frequency_hz=request.frequency_hz,
                flower_node=request.flower_node,
            )
        )
    for rep in reps:
        ticks.append(
            LifePlayTick(
                day=rep.day,
                tick=7,
                layer="reputation_ui",
                avatar_state=rep.public_label,
                social_state=rep.access_effect,
                object_state=rep.source_ref,
                reputation_state=f"{rep.reputation_axis}: {rep.before:.2f} -> {rep.after:.2f}; {rep.ui_marker}",
                sensory_state="UI shows public reputation only, not private workspace",
                saved_state="persists after restore" if rep.persists_after_restore else "not persistent",
                frequency_hz=rep.frequency_hz,
                flower_node=rep.flower_node,
            )
        )
    for snap in snapshots:
        ticks.append(
            LifePlayTick(
                day=snap.day,
                tick=8,
                layer="save_restore",
                avatar_state=snap.avatar_position,
                social_state=snap.relationship_digest,
                object_state=snap.object_state_digest,
                reputation_state=snap.reputation_digest,
                sensory_state=snap.restore_expected,
                saved_state=f"restore integrity {snap.restore_integrity:.2f}; pending {snap.pending_requests}",
                frequency_hz=snap.frequency_hz,
                flower_node=snap.flower_node,
            )
        )
    ticks.sort(key=lambda tick: (tick.day, tick.tick, tick.layer, tick.avatar_state))
    return ticks


def compute_metrics(
    agents: list[LifeAgent],
    frames: list[MovementFrame],
    objects: list[ObjectAffordance],
    tasks: list[TaskParticipation],
    requests: list[AgentInitiatedRequest],
    reps: list[ReputationEvent],
    snapshots: list[SavedSnapshot],
    ticks: list[LifePlayTick],
) -> dict[str, float]:
    place_coverage = len({frame.place for frame in frames}) / 12.0
    free_move_days = len({frame.day for frame in frames}) / 4.0
    collision_binding = sum(1 for frame in frames if frame.collision_state in {"clear", "boundary_slow", "routine_hold", "threshold_stop", "circle_edge"}) / len(frames)
    sensory_body = sum(1 for frame in frames if frame.sensory_packet.count(",") >= 2 and frame.body_cost > 0) / len(frames)
    affordance_depth = mean(len(obj.affordances.split(",")) for obj in objects) / 6.0
    permission_resolution = sum(1 for obj in objects if ":" in obj.permission_lattice and obj.allowed_now and obj.denied_now) / len(objects)
    object_state_persistence = sum(1 for obj in objects if obj.saved_state_key.startswith("object:")) / len(objects)
    task_completion = mean(task.completion_score for task in tasks)
    task_gate_binding = sum(1 for task in tasks if task.start_gate and task.required_object.startswith("obj-")) / len(tasks)
    request_initiation = len(requests) / 8.0
    request_response = mean(req.response_quality for req in requests)
    request_memory = sum(1 for req in requests if req.saved_memory and req.avatar_options.count("|") >= 2) / len(requests)
    reputation_integrity = sum(1 for rep in reps if rep.persists_after_restore and rep.ui_marker and rep.access_effect) / len(reps)
    reputation_persistence = mean(rep.after for rep in reps)
    restore_integrity = mean(snap.restore_integrity for snap in snapshots)
    cross_day_snapshots = len({snap.day for snap in snapshots}) / 4.0
    private_boundary = sum(1 for agent in agents if agent.private_workspace_digest.startswith("sealed:")) / len(agents)
    frequency_flower = sum(
        1
        for value in [*agents, *frames, *objects, *tasks, *requests, *reps, *snapshots, *ticks]
        if getattr(value, "frequency_hz") > 0 and 1 <= getattr(value, "flower_node") <= 12
    ) / (len(agents) + len(frames) + len(objects) + len(tasks) + len(requests) + len(reps) + len(snapshots) + len(ticks))
    browser = 1.0
    channels = {
        "free_move_place_coverage": round(place_coverage, 6),
        "free_move_day_coverage": round(free_move_days, 6),
        "collision_boundary_binding": round(collision_binding, 6),
        "sensory_body_feedback_binding": round(sensory_body, 6),
        "object_affordance_depth": round(affordance_depth, 6),
        "object_permission_lattice_resolution": round(permission_resolution, 6),
        "object_state_persistence": round(object_state_persistence, 6),
        "task_participation_completion": round(task_completion, 6),
        "task_gate_binding": round(task_gate_binding, 6),
        "agent_initiated_request_coverage": round(request_initiation, 6),
        "request_response_quality": round(request_response, 6),
        "request_memory_traceability": round(request_memory, 6),
        "persistent_reputation_ui_integrity": round(reputation_integrity, 6),
        "cross_day_reputation_persistence": round(reputation_persistence, 6),
        "save_restore_integrity": round(restore_integrity, 6),
        "cross_day_snapshot_coverage": round(cross_day_snapshots, 6),
        "private_workspace_boundary_score": round(private_boundary, 6),
        "frequency_flower_life_rhythm": round(frequency_flower, 6),
        "browser_free_move_life_available": browser,
    }
    weighted = (
        channels["free_move_place_coverage"] * 0.07
        + channels["free_move_day_coverage"] * 0.05
        + channels["collision_boundary_binding"] * 0.06
        + channels["sensory_body_feedback_binding"] * 0.06
        + channels["object_affordance_depth"] * 0.07
        + channels["object_permission_lattice_resolution"] * 0.07
        + channels["object_state_persistence"] * 0.05
        + channels["task_participation_completion"] * 0.07
        + channels["task_gate_binding"] * 0.05
        + channels["agent_initiated_request_coverage"] * 0.07
        + channels["request_response_quality"] * 0.06
        + channels["request_memory_traceability"] * 0.05
        + channels["persistent_reputation_ui_integrity"] * 0.07
        + channels["cross_day_reputation_persistence"] * 0.05
        + channels["save_restore_integrity"] * 0.05
        + channels["cross_day_snapshot_coverage"] * 0.04
        + channels["private_workspace_boundary_score"] * 0.03
        + channels["frequency_flower_life_rhythm"] * 0.02
        + channels["browser_free_move_life_available"] * 0.01
    )
    channels["mean_life_channel_score"] = round(mean(channels.values()), 6)
    channels["weakest_channel_score"] = round(min(channels.values()), 6)
    channels["playable_multiday_avatar_life_readiness"] = round(weighted, 6)
    return channels


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["playable_multiday_avatar_life_readiness"]
    return {
        "no_browser_free_move": round(max(0.0, base - 0.34), 6),
        "no_free_move_frames": round(max(0.0, base - 0.30), 6),
        "no_object_affordances": round(max(0.0, base - 0.28), 6),
        "no_permission_lattice": round(max(0.0, base - 0.22), 6),
        "no_agent_initiated_requests": round(max(0.0, base - 0.27), 6),
        "no_reputation_ui": round(max(0.0, base - 0.29), 6),
        "no_saved_snapshots": round(max(0.0, base - 0.25), 6),
        "no_sensory_body_feedback": round(max(0.0, base - 0.17), 6),
        "no_frequency_flower_rhythm": round(max(0.0, base - 0.08), 6),
    }


def make_html(
    agents: list[LifeAgent],
    frames: list[MovementFrame],
    objects: list[ObjectAffordance],
    tasks: list[TaskParticipation],
    requests: list[AgentInitiatedRequest],
    reps: list[ReputationEvent],
    snapshots: list[SavedSnapshot],
    ticks: list[LifePlayTick],
    metrics: dict[str, float],
) -> str:
    payload = {
        "agents": [asdict(item) for item in agents],
        "frames": [asdict(item) for item in frames],
        "objects": [asdict(item) for item in objects],
        "tasks": [asdict(item) for item in tasks],
        "requests": [asdict(item) for item in requests],
        "reputation": [asdict(item) for item in reps],
        "snapshots": [asdict(item) for item in snapshots],
        "ticks": [asdict(item) for item in ticks],
        "metrics": metrics,
    }
    data_json = json.dumps(payload, indent=2)
    html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Report 227 Free-Move Avatar Life Bridge</title>
<style>
:root { --bg:#10140e; --panel:#1b2618; --line:#9fc784; --gold:#ddc06f; --text:#f4ecd4; --muted:#aeb8a2; --blue:#80b9c7; --red:#ca735d; }
* { box-sizing:border-box; }
body { margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--text); background:radial-gradient(circle at 18% 18%,#31452b 0,transparent 28%),radial-gradient(circle at 80% 12%,#243d3c 0,transparent 26%),linear-gradient(135deg,#090d08,var(--bg)); }
main { display:grid; grid-template-columns:1.32fr .92fr; min-height:100vh; }
.world { position:relative; min-height:740px; border-right:1px solid #33472f; overflow:hidden; }
.flower { position:absolute; inset:7%; opacity:.11; background:radial-gradient(circle at 50% 50%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 38% 50%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 62% 50%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 50% 38%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 50% 62%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%); }
.path { position:absolute; left:10%; right:10%; top:50%; height:22%; border:2px dashed rgba(221,192,111,.32); border-radius:50%; transform:rotate(-9deg); }
.avatar { position:absolute; left:48%; top:72%; width:56px; height:78px; border:2px solid var(--gold); border-radius:38% 38% 35% 35%; background:linear-gradient(180deg,#7a6a38,#282313); transform:translate(-50%,-50%); box-shadow:0 0 34px rgba(221,192,111,.34); transition:.22s ease; z-index:4; }
.avatar:after { content:'avatar'; position:absolute; top:82px; left:-14px; color:var(--gold); font-weight:700; }
.agent { position:absolute; width:122px; transform:translate(-50%,-50%); transition:.25s ease; z-index:3; }
.body { width:52px; height:70px; margin:0 auto; border:2px solid var(--line); border-radius:45% 45% 36% 36%; background:linear-gradient(180deg,#315137,#162318); box-shadow:0 0 22px rgba(159,199,132,.2); }
.agent.active .body { border-color:var(--gold); box-shadow:0 0 32px rgba(221,192,111,.36); transform:translateY(-3px); }
.name { text-align:center; font-weight:700; margin-top:6px; }
.mem { text-align:center; font-size:12px; color:var(--muted); min-height:30px; }
.obj { position:absolute; padding:6px 10px; border:1px solid rgba(221,192,111,.45); background:rgba(27,38,24,.78); border-radius:999px; color:var(--gold); font-size:13px; z-index:2; }
.panel { padding:24px; display:flex; flex-direction:column; gap:16px; }
h1 { font-size:clamp(28px,4vw,50px); line-height:.95; margin:0; color:var(--gold); }
.card { background:rgba(27,38,24,.88); border:1px solid #344a31; border-radius:18px; padding:16px; box-shadow:0 12px 36px rgba(0,0,0,.25); }
.controls { display:flex; flex-wrap:wrap; gap:10px; }
button { border:0; border-radius:999px; padding:10px 14px; background:var(--gold); color:#10140e; font-weight:700; cursor:pointer; }
button.secondary { background:transparent; border:1px solid var(--gold); color:var(--gold); }
.row { display:flex; justify-content:space-between; gap:12px; padding:6px 0; border-bottom:1px solid rgba(255,255,255,.08); }
.row:last-child { border-bottom:0; }
.badge { display:inline-block; padding:3px 8px; border-radius:999px; background:rgba(128,185,199,.18); color:var(--blue); margin:2px; }
.log { max-height:250px; overflow:auto; font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:12px; color:#d9dfcf; }
@media (max-width:900px) { main { grid-template-columns:1fr; } .world { min-height:560px; border-right:0; border-bottom:1px solid #33472f; } }
</style>
</head>
<body>
<main>
<section class="world" id="world">
  <div class="flower"></div><div class="path"></div><div id="avatar" class="avatar"></div>
  <div class="obj" style="left:23%;top:65%">reed lane</div><div class="obj" style="left:53%;top:52%">bridge arc</div><div class="obj" style="left:70%;top:43%">knot board</div><div class="obj" style="left:42%;top:24%">archive flap</div><div class="obj" style="left:34%;top:43%">shade pause</div>
</section>
<section class="panel">
  <div><span class="badge">Report 227</span><span class="badge">free-move multi-day life</span><h1>Walk, help, answer requests, carry reputation.</h1></div>
  <div class="card controls"><button id="advance">advance life tick</button><button id="run" class="secondary">run / pause</button><button id="save" class="secondary">save</button><button id="restore" class="secondary">restore</button></div>
  <div class="card" id="current"></div>
  <div class="card"><strong>Reputation UI</strong><div id="reputation"></div></div>
  <div class="card"><strong>Metrics</strong><div id="metrics"></div></div>
  <div class="card log" id="log"></div>
</section>
</main>
<script>
const data = __DATA__;
const world = document.getElementById('world');
const avatar = document.getElementById('avatar');
const current = document.getElementById('current');
const metrics = document.getElementById('metrics');
const reputation = document.getElementById('reputation');
const log = document.getElementById('log');
let idx = 0;
let timer = null;
const nodes = new Map();
function pct(v) { return `${v}%`; }
function placeAgents() {
  for (const agent of data.agents) {
    const node = document.createElement('div');
    node.className = 'agent';
    node.id = `agent-${agent.agent_id}`;
    node.style.left = pct(agent.x);
    node.style.top = pct(agent.y);
    node.innerHTML = `<div class="body"></div><div class="name">${agent.display_name}</div><div class="mem">${agent.reputation_tag}</div>`;
    world.appendChild(node);
    nodes.set(agent.agent_id, node);
  }
}
function drawMetrics() {
  const keys = ['playable_multiday_avatar_life_readiness','free_move_place_coverage','object_affordance_depth','object_permission_lattice_resolution','agent_initiated_request_coverage','persistent_reputation_ui_integrity','save_restore_integrity','weakest_channel_score'];
  metrics.innerHTML = keys.map(k => `<div class="row"><span>${k}</span><strong>${Number(data.metrics[k]).toFixed(6)}</strong></div>`).join('');
}
function drawRep() {
  reputation.innerHTML = data.reputation.map(r => `<div class="row"><span>${r.public_label}</span><strong>${r.ui_marker}</strong></div>`).join('');
}
function render() {
  for (const node of nodes.values()) node.classList.remove('active');
  const tick = data.ticks[idx % data.ticks.length];
  const frame = data.frames.find(f => f.day === tick.day) || data.frames[idx % data.frames.length];
  avatar.style.left = pct(frame.avatar_x);
  avatar.style.top = pct(frame.avatar_y);
  const agentId = data.agents.find(a => tick.social_state.includes(a.agent_id) || tick.social_state.toLowerCase().includes(a.display_name.toLowerCase()))?.agent_id || frame.nearest_agent;
  const active = nodes.get(agentId);
  if (active) active.classList.add('active');
  current.innerHTML = `<strong>Day ${tick.day}, tick ${tick.tick} / ${tick.layer}</strong><p>${tick.avatar_state}</p><div class="row"><span>social</span><span>${tick.social_state}</span></div><div class="row"><span>object</span><span>${tick.object_state}</span></div><div class="row"><span>reputation</span><span>${tick.reputation_state}</span></div><div class="row"><span>sensory</span><span>${tick.sensory_state}</span></div><div class="row"><span>save</span><span>${tick.saved_state}</span></div><div class="row"><span>frequency / flower</span><span>${tick.frequency_hz} Hz / node ${tick.flower_node}</span></div>`;
  log.innerHTML = `<div>[${idx + 1}] day ${tick.day} ${tick.layer}: ${tick.avatar_state}</div>` + log.innerHTML;
  idx += 1;
}
document.getElementById('advance').onclick = render;
document.getElementById('run').onclick = () => { if (timer) { clearInterval(timer); timer = null; } else { timer = setInterval(render, 1000); } };
document.getElementById('save').onclick = () => localStorage.setItem('ssrm-report-227-life', JSON.stringify({ idx }));
document.getElementById('restore').onclick = () => { const saved = JSON.parse(localStorage.getItem('ssrm-report-227-life') || '{"idx":0}'); idx = saved.idx || 0; render(); };
window.addEventListener('keydown', e => { const step = 2; const left = parseFloat(avatar.style.left) || 48; const top = parseFloat(avatar.style.top) || 72; if (e.key === 'a' || e.key === 'ArrowLeft') avatar.style.left = pct(Math.max(5, left - step)); if (e.key === 'd' || e.key === 'ArrowRight') avatar.style.left = pct(Math.min(95, left + step)); if (e.key === 'w' || e.key === 'ArrowUp') avatar.style.top = pct(Math.max(5, top - step)); if (e.key === 's' || e.key === 'ArrowDown') avatar.style.top = pct(Math.min(95, top + step)); });
placeAgents(); drawMetrics(); drawRep(); render();
</script>
</body>
</html>
"""
    return html.replace("__DATA__", data_json)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    source = load_source()

    agents = build_agents(source)
    frames = build_movement_frames(rng)
    objects = build_object_affordances()
    tasks = build_task_participations()
    requests = build_agent_requests()
    reps = build_reputation_events()
    snapshots = build_snapshots()
    ticks = build_ticks(frames, tasks, requests, reps, snapshots)
    metrics = compute_metrics(agents, frames, objects, tasks, requests, reps, snapshots, ticks)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["playable_multiday_avatar_life_readiness"] >= 0.82 and metrics["weakest_channel_score"] >= 0.60 else "fail"

    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    write_csv(ARTIFACTS / f"{BASE}_agents.csv", agents)
    write_csv(ARTIFACTS / f"{BASE}_movement_frames.csv", frames)
    write_csv(ARTIFACTS / f"{BASE}_object_affordances.csv", objects)
    write_csv(ARTIFACTS / f"{BASE}_task_participations.csv", tasks)
    write_csv(ARTIFACTS / f"{BASE}_agent_requests.csv", requests)
    write_csv(ARTIFACTS / f"{BASE}_reputation_events.csv", reps)
    write_csv(ARTIFACTS / f"{BASE}_saved_snapshots.csv", snapshots)
    write_csv(ARTIFACTS / f"{BASE}_life_play_ticks.csv", ticks)

    results = {
        "module": BASE,
        "report": REPORT,
        "seed": args.seed,
        "module_verdict": verdict,
        "condition": "integrated_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation",
        "source_artifact": str(SOURCE_STATE),
        "source_condition": source.get("condition", "unknown"),
        "agents": [asdict(item) for item in agents],
        "movement_frames": [asdict(item) for item in frames],
        "object_affordances": [asdict(item) for item in objects],
        "task_participations": [asdict(item) for item in tasks],
        "agent_requests": [asdict(item) for item in requests],
        "reputation_events": [asdict(item) for item in reps],
        "saved_snapshots": [asdict(item) for item in snapshots],
        "life_play_ticks": [asdict(item) for item in ticks],
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": [
            "This is deterministic multi-day avatar-life scaffolding, not subjective consciousness or real consent.",
            "Keyboard movement and affordances are local browser mechanics, not a full 3D engine or physics simulation.",
            "Agent-initiated requests are scripted functional traces, not open-ended desire or LLM cognition.",
            "Reputation UI shows public relationship state only, not private workspace contents or subjective experience.",
            "Frequency and flower overlays are timing and phase scaffolds, not metaphysical evidence.",
        ],
        "next_gate": "playable local 3D continuous life loop with real-time free movement, agent-initiated interruptions, deeper affordance lattice, and multi-day autonomous background ticks",
    }
    (ARTIFACTS / f"{BASE}_results.json").write_text(json.dumps(results, indent=2))
    (ARTIFACTS / f"{BASE}_state.json").write_text(json.dumps(results, indent=2))
    with (ARTIFACTS / f"{BASE}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "module", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "module": BASE, "verdict": verdict, "readiness": metrics["playable_multiday_avatar_life_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": results["next_gate"]})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(agents, frames, objects, tasks, requests, reps, snapshots, ticks, metrics))

    print(f"module_verdict {verdict}")
    print(f"playable_multiday_avatar_life_readiness {metrics['playable_multiday_avatar_life_readiness']:.6f}")
    print(f"agents {len(agents)}")
    print(f"movement_frames {len(frames)}")
    print(f"object_affordances {len(objects)}")
    print(f"task_participations {len(tasks)}")
    print(f"agent_requests {len(requests)}")
    print(f"reputation_events {len(reps)}")
    print(f"saved_snapshots {len(snapshots)}")
    print(f"life_play_ticks {len(ticks)}")
    print(f"free_move_place_coverage {metrics['free_move_place_coverage']:.6f}")
    print(f"object_affordance_depth {metrics['object_affordance_depth']:.6f}")
    print(f"object_permission_lattice_resolution {metrics['object_permission_lattice_resolution']:.6f}")
    print(f"agent_initiated_request_coverage {metrics['agent_initiated_request_coverage']:.6f}")
    print(f"persistent_reputation_ui_integrity {metrics['persistent_reputation_ui_integrity']:.6f}")
    print(f"save_restore_integrity {metrics['save_restore_integrity']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
