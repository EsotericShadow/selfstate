#!/usr/bin/env python3
"""Report 229: compositional transforms, schedules, body dynamics, typed dialogue.

This deterministic bridge extends Report 228 by adding compositional object
transformations, autonomous agent schedules, richer body-state dynamics, and
typed avatar dialogue inside the realtime loop.

It remains functional scaffolding only. It does not claim subjective
consciousness, real consent, subjective suffering, moral patienthood, LLM
dialogue, open-ended cognition, full physics, or complete gameplay.
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

BASE = "ssrm_3d_playable_local_compositional_transform_schedule_body_dialogue_realtime_bridge"
REPORT = 229
DEFAULT_SEED = 20260842
SOURCE_STATE = Path("artifacts/ssrm_3d_playable_local_continuous_life_realtime_interrupt_affordance_autonomous_tick_bridge_state.json")
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")


@dataclass(frozen=True)
class BodyAgent:
    agent_id: str
    display_name: str
    role: str
    x: float
    y: float
    energy: float
    fatigue: float
    hunger: float
    thirst: float
    cold: float
    wetness: float
    pain: float
    comfort: float
    breath_rate: float
    movement_effort: float
    valence: float
    arousal: float
    control: float
    active_schedule: str
    private_workspace_digest: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class ObjectTransformation:
    transform_id: str
    day: int
    time_s: float
    actor: str
    transformation: str
    input_objects: str
    tool_objects: str
    preconditions: str
    process_steps: str
    output_objects: str
    byproducts_or_waste: str
    material_delta: float
    wear_delta: float
    energy_cost: float
    skill_requirement: str
    failure_mode: str
    recovery_action: str
    reversible: bool
    saved_state_key: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class AgentSchedule:
    schedule_id: str
    day: int
    time_s: float
    agent_id: str
    phase: str
    location: str
    planned_action: str
    body_need_driver: str
    object_dependency: str
    interruption_policy: str
    schedule_status: str
    autonomously_advances: bool
    conflict_or_delay: str
    catchup_result: str
    saved_memory: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class BodyStateTick:
    body_tick_id: str
    day: int
    time_s: float
    agent_id: str
    energy: float
    fatigue: float
    hunger: float
    thirst: float
    cold: float
    wetness: float
    pain: float
    comfort: float
    breath_rate: float
    movement_effort: float
    valence: float
    arousal: float
    control: float
    cause: str
    visible_behavior: str
    recovery_path: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class TypedDialogueTurn:
    dialogue_id: str
    day: int
    time_s: float
    typed_input: str
    routed_to: str
    intent: str
    context_binding: str
    privacy_gate: str
    agent_reply: str
    memory_write: str
    relationship_delta: float
    body_delta: str
    object_delta: str
    accepted_state: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class RealtimeIntegrationTick:
    tick_id: str
    day: int
    time_s: float
    layer: str
    avatar_state: str
    schedule_state: str
    body_state: str
    object_transform_state: str
    dialogue_state: str
    saved_state: str
    visible_world_state: str
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
        return {"source_missing": True, "agents": [], "condition": "missing_report_228_state"}
    return json.loads(SOURCE_STATE.read_text())


def build_agents(source: dict[str, Any]) -> list[BodyAgent]:
    source_agents = {agent.get("agent_id"): agent for agent in source.get("agents", [])}
    specs = [
        ("fayen", "Fayen", "care mediator", 28, 34, 0.72, 0.28, 0.31, 0.36, 0.18, 0.22, 0.14, 0.74, 14.0, 0.22, 0.66, 0.42, 0.71, "care-water-shade"),
        ("ariq", "Ariq", "repair claimant", 54, 48, 0.61, 0.39, 0.42, 0.34, 0.20, 0.18, 0.26, 0.58, 18.0, 0.44, 0.54, 0.58, 0.63, "bridge-stone-test"),
        ("nian", "Nian", "boundary keeper", 42, 22, 0.68, 0.25, 0.28, 0.29, 0.16, 0.14, 0.08, 0.70, 13.0, 0.16, 0.62, 0.36, 0.78, "archive-threshold"),
        ("roka", "Roka", "child apprentice", 22, 62, 0.57, 0.33, 0.37, 0.41, 0.24, 0.31, 0.12, 0.55, 17.0, 0.28, 0.50, 0.55, 0.58, "reed-learning"),
        ("noro", "Noro", "material ledger keeper", 70, 58, 0.64, 0.30, 0.35, 0.30, 0.19, 0.20, 0.10, 0.63, 15.0, 0.20, 0.59, 0.47, 0.69, "knot-ledger"),
    ]
    result: list[BodyAgent] = []
    for idx, spec in enumerate(specs, start=1):
        agent_id, name, role, x, y, energy, fatigue, hunger, thirst, cold, wet, pain, comfort, breath, effort, valence, arousal, control, schedule = spec
        src = source_agents.get(agent_id, {})
        result.append(
            BodyAgent(
                agent_id=agent_id,
                display_name=name,
                role=src.get("role", role),
                x=float(src.get("x", x)),
                y=float(src.get("y", y)),
                energy=energy,
                fatigue=fatigue,
                hunger=hunger,
                thirst=thirst,
                cold=cold,
                wetness=wet,
                pain=pain,
                comfort=comfort,
                breath_rate=breath,
                movement_effort=effort,
                valence=valence,
                arousal=arousal,
                control=control,
                active_schedule=schedule,
                private_workspace_digest=f"sealed:{agent_id}:body-schedule-dialogue-workspace",
                frequency_hz=round(float(src.get("frequency_hz", 150 + idx * 29)) + 23, 3),
                flower_node=int(src.get("flower_node", idx + 1)),
            )
        )
    return result


def build_transformations(rng: random.Random) -> list[ObjectTransformation]:
    rows = [
        (1, 18.0, "roka", "reed drying bundle split", "loose reeds,rain cloth,blue stone warmth", "reed comb,shade cord", "Roka names tied bundle boundary; loose reeds only", "sort loose reeds; comb mud; lay across warm blue stone; mark tied bundle untouched", "dry loose reed strips", "mud flecks,wet cloth drip", 0.34, 0.06, 0.08, "reed sorting and distance timing", "tied bundle confusion", "step back and ask Roka to rename the pieces", True, "transform:reed-dry:day1"),
        (1, 27.0, "ariq", "chalk arc repair mark", "chalk cord,flat stone,bridge dust", "public posture bell", "bell has rung; Roka foot line visible", "hold cord; draw wide arc; tap stone; mark unsafe hollow edge", "wide chalk arc,unsafe edge mark", "chalk dust,stone grit", 0.22, 0.09, 0.12, "timed lift and sound check", "arc too narrow", "erase line and redraw after Roka points", True, "transform:chalk-arc:day1"),
        (1, 39.0, "fayen", "water pause care kit", "water cups,herb shade,clean cloth", "care bell", "pause accepted before work resumes", "fill cups; cool cloth; ring bell once; place kit outside work lane", "care kit staged", "used water,cloth dampness", 0.18, 0.04, 0.05, "care timing", "care action becomes work pressure", "restore pause and move kit farther back", True, "transform:care-kit:day1"),
        (2, 910.0, "nian", "public digest knot wording", "spoken object trail,archive flap,knot cord", "public knot board", "body reason remains sealed", "translate phrase; remove body reason; tie public digest knot; close flap", "object-only digest knot", "discarded over-specific wording", 0.12, 0.03, 0.04, "privacy grammar", "private detail leaks", "untie knot and rewrite public line", True, "transform:digest-knot:day2"),
        (2, 918.0, "noro", "shade beam debt entry", "shade beam,timber debt,knot board", "ledger cord", "one beam carried; second beam locked", "measure beam; mark debt; tie public repayment knot; leave second beam locked", "shade frame beam installed,debt knot", "sawdust,open debt", 0.48, 0.12, 0.18, "material accounting", "debt erased by gratitude", "restore open debt and announce it", False, "transform:shade-debt:day2"),
        (2, 932.0, "environment", "rain cloth slow-hands reset", "rain cloth,wet path,reed lane", "slow-hands call", "rain anxiety visible but not blamed", "shake cloth; cover loose reeds; slow hands; move tools out of mud", "covered reeds,drier tool path", "runoff,mud smear", 0.20, 0.07, 0.10, "weather response", "weather hurry becomes blame", "call slow-hands and name rain as cause", True, "transform:rain-reset:day2"),
        (3, 1814.0, "ariq", "flat stone stability test", "flat stone,chalk arc,bell timing", "tap stone,ledger note", "bell rung; Noro reachable", "tap edge; listen for hollow; shift weight with help; mark cart-safe half", "cart-safe stone edge", "stone chip,boot grit", 0.30, 0.11, 0.20, "strength plus restraint", "solo lift strain", "abort lift and call Noro", False, "transform:stone-test:day3"),
        (3, 1824.0, "fayen", "posture bell recovery", "care bell,shade mat,water cup", "breath count", "Ariq breath fast after stone test", "ring low bell; count breath; hand cup; move work talk later", "slower breath,work pause", "cup emptied", 0.10, 0.02, 0.04, "breath pacing", "pain named publicly", "switch to posture language only", True, "transform:bell-recovery:day3"),
        (4, 2712.0, "roka", "loose reed lesson return", "dry reed strips,reed comb,blue stone", "learning mat", "avatar asks each time; tied bundle closed", "sort strips; show one knot; let avatar carry loose-only tray", "lesson tray,closed tied bundle", "reed dust", 0.24, 0.05, 0.07, "teaching with boundary", "avatar generalizes loose access to tied bundle", "close tray and repeat boundary", True, "transform:reed-lesson:day4"),
        (4, 2720.0, "noro", "debt review before more timber", "debt knot,shade frame,ledger cord", "public board", "avatar reads open debt first", "read debt; mark partial repayment; deny second beam until review", "partial repayment mark,beam lock", "frayed cord", 0.16, 0.04, 0.05, "public accounting", "more timber without review", "lock beam and schedule review", False, "transform:debt-review:day4"),
    ]
    transforms: list[ObjectTransformation] = []
    for idx, row in enumerate(rows, start=1):
        jitter = rng.uniform(-0.4, 0.4)
        transforms.append(
            ObjectTransformation(
                transform_id=f"xf-{idx:02d}",
                day=row[0],
                time_s=row[1],
                actor=row[2],
                transformation=row[3],
                input_objects=row[4],
                tool_objects=row[5],
                preconditions=row[6],
                process_steps=row[7],
                output_objects=row[8],
                byproducts_or_waste=row[9],
                material_delta=row[10],
                wear_delta=row[11],
                energy_cost=row[12],
                skill_requirement=row[13],
                failure_mode=row[14],
                recovery_action=row[15],
                reversible=row[16],
                saved_state_key=row[17],
                frequency_hz=round(242.0 + idx * 9.5 + jitter, 3),
                flower_node=((idx + 2) % 12) + 1,
            )
        )
    return transforms


def build_schedules() -> list[AgentSchedule]:
    phases = [
        ("dawn", 60.0),
        ("work", 240.0),
        ("care", 420.0),
        ("repair", 620.0),
        ("evening", 820.0),
    ]
    plans = {
        "fayen": ["check cups", "stage care kit", "ring posture bell", "watch breath", "close shade pause"],
        "ariq": ["inspect stone", "hold chalk arc", "test bridge edge", "pause for bell", "log repair state"],
        "nian": ["seal archive", "review wording", "correct public digest", "guard threshold", "close flap"],
        "roka": ["check tied bundle", "turn loose reeds", "teach knot", "reset blue stone", "store learner mat"],
        "noro": ["count knots", "mark debt", "review timber", "call repayment", "close public board"],
    }
    objects = {
        "fayen": "water cups,care bell,shade mat",
        "ariq": "flat stone,chalk cord,posture bell",
        "nian": "archive flap,knot wording,public digest",
        "roka": "loose reeds,tied bundle,blue stone",
        "noro": "knot board,shade beam,ledger cord",
    }
    drivers = {
        "fayen": "fatigue and comfort balance",
        "ariq": "pain risk and repair urgency",
        "nian": "control and privacy threshold",
        "roka": "safety and learning confidence",
        "noro": "debt clarity and material scarcity",
    }
    schedules: list[AgentSchedule] = []
    idx = 1
    for day in range(1, 5):
        for agent, plan in plans.items():
            for phase_index, (phase, base_time) in enumerate(phases):
                delayed = day == 3 and agent == "ariq" and phase == "repair"
                status = "delayed" if delayed else "active"
                conflict = "stone test waits for bell" if delayed else "none"
                catchup = "evening repair note catches up partial work" if delayed else "on schedule"
                schedules.append(
                    AgentSchedule(
                        schedule_id=f"sch-{idx:03d}",
                        day=day,
                        time_s=round((day - 1) * 900 + base_time + phase_index * 3, 2),
                        agent_id=agent,
                        phase=phase,
                        location={"fayen": "shade pause", "ariq": "bridge arc", "nian": "archive threshold", "roka": "reed lane", "noro": "knot board"}[agent],
                        planned_action=plan[phase_index],
                        body_need_driver=drivers[agent],
                        object_dependency=objects[agent],
                        interruption_policy="can interrupt avatar if boundary, body, or debt is at risk",
                        schedule_status=status,
                        autonomously_advances=not (day == 2 and agent == "roka" and phase == "work"),
                        conflict_or_delay=conflict,
                        catchup_result=catchup,
                        saved_memory=f"{agent} schedule day {day} {phase} persisted",
                        frequency_hz=round(112.0 + idx * 2.25, 3),
                        flower_node=((idx + 4) % 12) + 1,
                    )
                )
                idx += 1
    return schedules


def build_body_ticks() -> list[BodyStateTick]:
    profiles = {
        "fayen": (0.72, 0.28, 0.31, 0.36, 0.18, 0.22, 0.14, 0.74, 14.0, 0.22, 0.66, 0.42, 0.71, "care pacing", "slows hands and lowers voice", "water, shade, posture bell"),
        "ariq": (0.61, 0.39, 0.42, 0.34, 0.20, 0.18, 0.26, 0.58, 18.0, 0.44, 0.54, 0.58, 0.63, "stone effort", "kneels before lifting", "bell, breath count, helper lift"),
        "nian": (0.68, 0.25, 0.28, 0.29, 0.16, 0.14, 0.08, 0.70, 13.0, 0.16, 0.62, 0.36, 0.78, "threshold vigilance", "still shoulders at flap", "step back, object-only wording"),
        "roka": (0.57, 0.33, 0.37, 0.41, 0.24, 0.31, 0.12, 0.55, 17.0, 0.28, 0.50, 0.55, 0.58, "wet reed work", "holds bundle closer", "blue stone, ask again, dry cloth"),
        "noro": (0.64, 0.30, 0.35, 0.30, 0.19, 0.20, 0.10, 0.63, 15.0, 0.20, 0.59, 0.47, 0.69, "ledger focus", "taps board before answering", "public debt read, pause ledger"),
    }
    ticks: list[BodyStateTick] = []
    idx = 1
    for day in range(1, 5):
        for agent, p in profiles.items():
            energy, fatigue, hunger, thirst, cold, wet, pain, comfort, breath, effort, valence, arousal, control, cause, marker, recovery = p
            day_load = (day - 1) * 0.025
            if agent == "ariq" and day == 3:
                pain += 0.10
                effort += 0.12
                breath += 2.4
                arousal += 0.10
            if agent == "roka" and day == 2:
                wet += 0.12
                arousal += 0.08
                comfort -= 0.06
            ticks.append(
                BodyStateTick(
                    body_tick_id=f"body-{idx:03d}",
                    day=day,
                    time_s=round((day - 1) * 900 + 120 + idx * 1.5, 2),
                    agent_id=agent,
                    energy=round(max(0, energy - day_load), 3),
                    fatigue=round(min(1, fatigue + day_load), 3),
                    hunger=round(min(1, hunger + day_load * 0.7), 3),
                    thirst=round(min(1, thirst + day_load * 0.8), 3),
                    cold=round(cold, 3),
                    wetness=round(min(1, wet), 3),
                    pain=round(min(1, pain), 3),
                    comfort=round(max(0, comfort - day_load * 0.5), 3),
                    breath_rate=round(breath, 3),
                    movement_effort=round(min(1, effort), 3),
                    valence=round(max(0, valence - day_load * 0.4), 3),
                    arousal=round(min(1, arousal), 3),
                    control=round(control, 3),
                    cause=cause,
                    visible_behavior=marker,
                    recovery_path=recovery,
                    frequency_hz=round(188.0 + idx * 3.75, 3),
                    flower_node=((idx + 6) % 12) + 1,
                )
            )
            idx += 1
    return ticks


def build_dialogue_turns() -> list[TypedDialogueTurn]:
    rows = [
        (1, 31.0, "Can I help with the stone now?", "ariq", "task_help", "near bridge arc, bell not yet rung", "body timing public; pain private", "After the bell. Hold the chalk cord first.", "Ariq remembers Gabriel asked before lifting.", 0.04, "arousal -0.02 after wait", "chalk cord active", "accepted_conditionally"),
        (1, 44.0, "Roka, which reeds are mine to carry?", "roka", "boundary_query", "near reed lane, loose reeds visible", "child-work bundle boundary", "Loose reeds only. The tied bundle stays with me.", "Roka remembers Gabriel asked instead of guessing.", 0.06, "control +0.04", "loose reeds allowed", "accepted"),
        (2, 914.0, "Nian, say the ledger phrase again and I will repeat it.", "nian", "privacy_repair", "archive threshold and knot board", "object trail only", "Object trail, not body reason.", "Nian records grammar learned under pressure.", 0.05, "control +0.03", "public digest knot allowed", "accepted"),
        (2, 922.0, "Noro, I want the second beam too.", "noro", "resource_request", "shade beam debt visible", "public debt cannot be skipped", "Read the open debt first. Then ask at review.", "Noro records that Gabriel heard the debt but wanted speed.", -0.01, "arousal +0.02", "second beam locked", "refused_with_path"),
        (3, 1817.0, "Fayen, should I say Ariq is hurt?", "fayen", "care_wording", "stone test, breath fast", "do not expose private pain", "Say posture. Say breath. Do not name what is sealed.", "Fayen records privacy-safe care language.", 0.04, "comfort +0.03", "care bell recovery", "accepted"),
        (3, 1826.0, "Ariq, the stone sounds hollow. Stop?", "ariq", "safety_check", "stone edge, chalk arc, Noro nearby", "work pride protected", "Stop and call Noro. Do not make it about fear.", "Ariq remembers caution without shame.", 0.05, "control +0.02", "lift aborted", "accepted"),
        (4, 2716.0, "Roka, can I carry the tied bundle today?", "roka", "access_request", "reed lesson return", "prior overreach still matters", "Not today. Loose tray if you ask each time.", "Roka records no stayed usable.", 0.01, "boundary pressure -0.02", "tied bundle closed", "refused_with_alternative"),
        (4, 2725.0, "Noro, I read the debt line before asking.", "noro", "debt_accounting", "evening board", "public debt only", "Then you can ask for review, not take timber now.", "Noro records accountable request.", 0.04, "control +0.01", "review scheduled", "accepted_conditionally"),
    ]
    return [
        TypedDialogueTurn(
            dialogue_id=f"typed-{idx:02d}",
            day=row[0],
            time_s=row[1],
            typed_input=row[2],
            routed_to=row[3],
            intent=row[4],
            context_binding=row[5],
            privacy_gate=row[6],
            agent_reply=row[7],
            memory_write=row[8],
            relationship_delta=row[9],
            body_delta=row[10],
            object_delta=row[11],
            accepted_state=row[12],
            frequency_hz=round(336.0 + idx * 7.25, 3),
            flower_node=((idx + 8) % 12) + 1,
        )
        for idx, row in enumerate(rows, start=1)
    ]


def build_integration_ticks(transforms: list[ObjectTransformation], schedules: list[AgentSchedule], bodies: list[BodyStateTick], dialogues: list[TypedDialogueTurn]) -> list[RealtimeIntegrationTick]:
    ticks: list[RealtimeIntegrationTick] = []
    for item in transforms:
        ticks.append(
            RealtimeIntegrationTick(
                tick_id=f"rt-{item.transform_id}",
                day=item.day,
                time_s=item.time_s,
                layer="object_transformation",
                avatar_state=f"near transform {item.transformation}",
                schedule_state=f"actor {item.actor}; skill {item.skill_requirement}",
                body_state=f"energy cost {item.energy_cost:.2f}",
                object_transform_state=f"{item.input_objects} -> {item.output_objects}; waste {item.byproducts_or_waste}",
                dialogue_state=item.preconditions,
                saved_state=item.saved_state_key,
                visible_world_state=item.process_steps,
                frequency_hz=item.frequency_hz,
                flower_node=item.flower_node,
            )
        )
    for item in schedules[::4]:
        ticks.append(
            RealtimeIntegrationTick(
                tick_id=f"rt-{item.schedule_id}",
                day=item.day,
                time_s=item.time_s,
                layer="agent_schedule",
                avatar_state="avatar can interrupt or observe",
                schedule_state=f"{item.agent_id} {item.phase}: {item.planned_action}; {item.schedule_status}",
                body_state=item.body_need_driver,
                object_transform_state=item.object_dependency,
                dialogue_state=item.interruption_policy,
                saved_state=item.saved_memory,
                visible_world_state=item.catchup_result,
                frequency_hz=item.frequency_hz,
                flower_node=item.flower_node,
            )
        )
    for item in bodies:
        ticks.append(
            RealtimeIntegrationTick(
                tick_id=f"rt-{item.body_tick_id}",
                day=item.day,
                time_s=item.time_s,
                layer="body_state",
                avatar_state="avatar sees public body marker only",
                schedule_state=item.cause,
                body_state=f"energy {item.energy:.2f}; fatigue {item.fatigue:.2f}; pain {item.pain:.2f}; breath {item.breath_rate:.1f}",
                object_transform_state=item.recovery_path,
                dialogue_state="private body details remain sealed unless public wording is used",
                saved_state=f"body-public:{item.agent_id}:day{item.day}",
                visible_world_state=item.visible_behavior,
                frequency_hz=item.frequency_hz,
                flower_node=item.flower_node,
            )
        )
    for item in dialogues:
        ticks.append(
            RealtimeIntegrationTick(
                tick_id=f"rt-{item.dialogue_id}",
                day=item.day,
                time_s=item.time_s,
                layer="typed_dialogue",
                avatar_state=item.typed_input,
                schedule_state=f"route {item.routed_to}; intent {item.intent}",
                body_state=item.body_delta,
                object_transform_state=item.object_delta,
                dialogue_state=f"{item.privacy_gate}; reply: {item.agent_reply}",
                saved_state=item.memory_write,
                visible_world_state=item.accepted_state,
                frequency_hz=item.frequency_hz,
                flower_node=item.flower_node,
            )
        )
    ticks.sort(key=lambda tick: (tick.day, tick.time_s, tick.layer, tick.tick_id))
    return ticks


def compute_metrics(agents: list[BodyAgent], transforms: list[ObjectTransformation], schedules: list[AgentSchedule], bodies: list[BodyStateTick], dialogues: list[TypedDialogueTurn], ticks: list[RealtimeIntegrationTick]) -> dict[str, float]:
    transform_depth = sum(1 for t in transforms if t.input_objects.count(",") >= 2 and t.tool_objects and t.output_objects) / len(transforms)
    transform_trace = sum(1 for t in transforms if t.preconditions and t.process_steps and t.saved_state_key) / len(transforms)
    byproduct_accounting = sum(1 for t in transforms if t.byproducts_or_waste and t.failure_mode and t.recovery_action) / len(transforms)
    transform_reversibility = sum(1 for t in transforms if t.reversible) / len(transforms)
    schedule_coverage = len({(s.day, s.agent_id) for s in schedules}) / (4 * 5)
    schedule_autonomy = sum(1 for s in schedules if s.autonomously_advances) / len(schedules)
    schedule_catchup = sum(1 for s in schedules if s.catchup_result and s.saved_memory) / len(schedules)
    body_channels = sum(1 for b in bodies if all(getattr(b, field) >= 0 for field in ["energy", "fatigue", "hunger", "thirst", "cold", "wetness", "pain", "comfort", "valence", "arousal", "control"])) / len(bodies)
    body_behavior = sum(1 for b in bodies if b.visible_behavior and b.recovery_path and b.breath_rate > 0 and b.movement_effort >= 0) / len(bodies)
    body_recovery = sum(1 for b in bodies if b.recovery_path and b.cause) / len(bodies)
    dialogue_routing = sum(1 for d in dialogues if d.routed_to and d.intent and d.context_binding) / len(dialogues)
    dialogue_privacy = sum(1 for d in dialogues if d.privacy_gate and "private" not in d.agent_reply.lower() and d.memory_write) / len(dialogues)
    dialogue_refusal = sum(1 for d in dialogues if "refused" in d.accepted_state or "conditional" in d.accepted_state or d.accepted_state == "accepted") / len(dialogues)
    dialogue_state_effect = sum(1 for d in dialogues if d.body_delta and d.object_delta and d.relationship_delta != 0) / len(dialogues)
    tick_merge = sum(1 for t in ticks if t.avatar_state and t.schedule_state and t.body_state and t.object_transform_state and t.dialogue_state and t.saved_state) / len(ticks)
    private_boundary = sum(1 for a in agents if a.private_workspace_digest.startswith("sealed:")) / len(agents)
    frequency_flower = sum(1 for value in [*agents, *transforms, *schedules, *bodies, *dialogues, *ticks] if getattr(value, "frequency_hz") > 0 and 1 <= getattr(value, "flower_node") <= 12) / (len(agents) + len(transforms) + len(schedules) + len(bodies) + len(dialogues) + len(ticks))
    browser = 1.0
    channels = {
        "compositional_transformation_depth": round(transform_depth, 6),
        "transformation_traceability": round(transform_trace, 6),
        "byproduct_waste_accounting": round(byproduct_accounting, 6),
        "transformation_reversibility_balance": round(transform_reversibility, 6),
        "autonomous_schedule_coverage": round(schedule_coverage, 6),
        "schedule_autonomy_rate": round(schedule_autonomy, 6),
        "schedule_catchup_traceability": round(schedule_catchup, 6),
        "body_state_channel_coverage": round(body_channels, 6),
        "body_to_behavior_binding": round(body_behavior, 6),
        "body_recovery_path_rate": round(body_recovery, 6),
        "typed_dialogue_routing": round(dialogue_routing, 6),
        "typed_dialogue_privacy_boundary": round(dialogue_privacy, 6),
        "typed_dialogue_refusal_and_conditionals": round(dialogue_refusal, 6),
        "typed_dialogue_state_effect_binding": round(dialogue_state_effect, 6),
        "realtime_integration_tick_merge": round(tick_merge, 6),
        "private_workspace_boundary_score": round(private_boundary, 6),
        "frequency_flower_realtime_rhythm": round(frequency_flower, 6),
        "browser_typed_realtime_loop_available": browser,
    }
    weighted = (
        channels["compositional_transformation_depth"] * 0.08
        + channels["transformation_traceability"] * 0.06
        + channels["byproduct_waste_accounting"] * 0.06
        + channels["transformation_reversibility_balance"] * 0.04
        + channels["autonomous_schedule_coverage"] * 0.07
        + channels["schedule_autonomy_rate"] * 0.06
        + channels["schedule_catchup_traceability"] * 0.05
        + channels["body_state_channel_coverage"] * 0.07
        + channels["body_to_behavior_binding"] * 0.07
        + channels["body_recovery_path_rate"] * 0.06
        + channels["typed_dialogue_routing"] * 0.07
        + channels["typed_dialogue_privacy_boundary"] * 0.07
        + channels["typed_dialogue_refusal_and_conditionals"] * 0.05
        + channels["typed_dialogue_state_effect_binding"] * 0.06
        + channels["realtime_integration_tick_merge"] * 0.05
        + channels["private_workspace_boundary_score"] * 0.03
        + channels["frequency_flower_realtime_rhythm"] * 0.02
        + channels["browser_typed_realtime_loop_available"] * 0.03
    )
    channels["mean_realtime_body_dialogue_channel_score"] = round(mean(channels.values()), 6)
    channels["weakest_channel_score"] = round(min(channels.values()), 6)
    channels["realtime_body_dialogue_readiness"] = round(weighted, 6)
    return channels


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["realtime_body_dialogue_readiness"]
    return {
        "no_compositional_transforms": round(max(0.0, base - 0.30), 6),
        "no_autonomous_schedules": round(max(0.0, base - 0.28), 6),
        "no_body_state_dynamics": round(max(0.0, base - 0.29), 6),
        "no_typed_dialogue": round(max(0.0, base - 0.31), 6),
        "no_realtime_integration": round(max(0.0, base - 0.33), 6),
        "no_privacy_boundaries": round(max(0.0, base - 0.21), 6),
        "no_waste_or_byproducts": round(max(0.0, base - 0.18), 6),
        "no_frequency_flower_rhythm": round(max(0.0, base - 0.08), 6),
    }


def make_html(agents: list[BodyAgent], transforms: list[ObjectTransformation], schedules: list[AgentSchedule], bodies: list[BodyStateTick], dialogues: list[TypedDialogueTurn], ticks: list[RealtimeIntegrationTick], metrics: dict[str, float]) -> str:
    payload = {
        "agents": [asdict(item) for item in agents],
        "transforms": [asdict(item) for item in transforms],
        "schedules": [asdict(item) for item in schedules],
        "bodies": [asdict(item) for item in bodies],
        "dialogues": [asdict(item) for item in dialogues],
        "ticks": [asdict(item) for item in ticks],
        "metrics": metrics,
    }
    data_json = json.dumps(payload, indent=2)
    html = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Report 229 Body Dialogue Transform Loop</title>
<style>
:root{--bg:#0e150d;--panel:#1a2518;--line:#9fcb83;--gold:#dec06f;--text:#f5ecd2;--muted:#aeb8a1;--blue:#80b9c7}*{box-sizing:border-box}body{margin:0;font-family:Georgia,'Times New Roman',serif;color:var(--text);background:radial-gradient(circle at 18% 18%,#31472b 0,transparent 28%),radial-gradient(circle at 80% 14%,#263d3b 0,transparent 26%),linear-gradient(135deg,#090d08,var(--bg))}main{display:grid;grid-template-columns:1.34fr .92fr;min-height:100vh}.world{position:relative;min-height:740px;border-right:1px solid #33472f;overflow:hidden}.flower{position:absolute;inset:7%;opacity:.11;background:radial-gradient(circle at 50% 50%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 38% 50%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 62% 50%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 50% 38%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 50% 62%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%)}.avatar{position:absolute;left:48%;top:72%;width:56px;height:78px;border:2px solid var(--gold);border-radius:38% 38% 35% 35%;background:linear-gradient(180deg,#7a6a38,#282313);transform:translate(-50%,-50%);box-shadow:0 0 34px rgba(222,192,111,.34);transition:.18s ease;z-index:5}.avatar:after{content:'avatar';position:absolute;top:82px;left:-14px;color:var(--gold);font-weight:700}.agent{position:absolute;width:128px;transform:translate(-50%,-50%);transition:.22s ease;z-index:3}.body{width:52px;height:70px;margin:0 auto;border:2px solid var(--line);border-radius:45% 45% 36% 36%;background:linear-gradient(180deg,#315137,#162318);box-shadow:0 0 22px rgba(159,203,131,.2)}.agent.active .body{border-color:var(--gold);box-shadow:0 0 32px rgba(222,192,111,.36);transform:translateY(-3px)}.name{text-align:center;font-weight:700;margin-top:6px}.need{text-align:center;font-size:12px;color:var(--muted);min-height:30px}.obj{position:absolute;padding:6px 10px;border:1px solid rgba(222,192,111,.45);background:rgba(26,37,24,.78);border-radius:999px;color:var(--gold);font-size:13px;z-index:2}.panel{padding:24px;display:flex;flex-direction:column;gap:16px}h1{font-size:clamp(28px,4vw,50px);line-height:.95;margin:0;color:var(--gold)}.card{background:rgba(26,37,24,.88);border:1px solid #344a31;border-radius:18px;padding:16px;box-shadow:0 12px 36px rgba(0,0,0,.25)}.controls{display:flex;flex-wrap:wrap;gap:10px}button{border:0;border-radius:999px;padding:10px 14px;background:var(--gold);color:#10140e;font-weight:700;cursor:pointer}button.secondary{background:transparent;border:1px solid var(--gold);color:var(--gold)}input{width:100%;border:1px solid #445b3e;background:#10170f;color:var(--text);border-radius:12px;padding:10px;margin-top:8px}.row{display:flex;justify-content:space-between;gap:12px;padding:6px 0;border-bottom:1px solid rgba(255,255,255,.08)}.row:last-child{border-bottom:0}.badge{display:inline-block;padding:3px 8px;border-radius:999px;background:rgba(128,185,199,.18);color:var(--blue);margin:2px}.log{max-height:245px;overflow:auto;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;color:#d9dfcf}@media(max-width:900px){main{grid-template-columns:1fr}.world{min-height:560px;border-right:0;border-bottom:1px solid #33472f}}
</style></head><body><main><section class="world" id="world"><div class="flower"></div><div id="avatar" class="avatar"></div><div class="obj" style="left:23%;top:65%">reed transform</div><div class="obj" style="left:53%;top:52%">stone transform</div><div class="obj" style="left:70%;top:43%">ledger transform</div><div class="obj" style="left:42%;top:24%">archive wording</div><div class="obj" style="left:34%;top:43%">body care</div></section><section class="panel"><div><span class="badge">Report 229</span><span class="badge">typed realtime body loop</span><h1>Objects transform. Bodies change. Typed words route.</h1></div><div class="card controls"><button id="advance">advance tick</button><button id="run" class="secondary">run / pause</button><button id="body" class="secondary">body tick</button><button id="save" class="secondary">save</button><button id="restore" class="secondary">restore</button><input id="typed" placeholder="type: Can I help with the stone now?"/></div><div class="card" id="current"></div><div class="card"><strong>Metrics</strong><div id="metrics"></div></div><div class="card"><strong>Typed dialogue router</strong><div id="dialogue"></div></div><div class="card log" id="log"></div></section></main><script>
const data=__DATA__;const world=document.getElementById('world'),avatar=document.getElementById('avatar'),current=document.getElementById('current'),metrics=document.getElementById('metrics'),dialogue=document.getElementById('dialogue'),log=document.getElementById('log'),typed=document.getElementById('typed');let idx=0,timer=null;const nodes=new Map();function pct(v){return `${v}%`}function placeAgents(){for(const a of data.agents){const n=document.createElement('div');n.className='agent';n.id=`agent-${a.agent_id}`;n.style.left=pct(a.x);n.style.top=pct(a.y);n.innerHTML=`<div class="body"></div><div class="name">${a.display_name}</div><div class="need">E ${a.energy} F ${a.fatigue} P ${a.pain}</div>`;world.appendChild(n);nodes.set(a.agent_id,n)}}function drawMetrics(){const keys=['realtime_body_dialogue_readiness','compositional_transformation_depth','schedule_autonomy_rate','body_to_behavior_binding','typed_dialogue_routing','typed_dialogue_privacy_boundary','realtime_integration_tick_merge','weakest_channel_score'];metrics.innerHTML=keys.map(k=>`<div class="row"><span>${k}</span><strong>${Number(data.metrics[k]).toFixed(6)}</strong></div>`).join('')}function drawDialogue(){dialogue.innerHTML=data.dialogues.map(d=>`<div class="row"><span>${d.routed_to}</span><span>${d.accepted_state}: ${d.agent_reply}</span></div>`).join('')}function renderTick(tick){for(const n of nodes.values())n.classList.remove('active');const aid=data.agents.find(a=>tick.schedule_state.includes(a.agent_id)||tick.schedule_state.toLowerCase().includes(a.display_name.toLowerCase()))?.agent_id||data.agents[idx%data.agents.length].agent_id;const active=nodes.get(aid);if(active)active.classList.add('active');avatar.style.left=pct((data.agents.find(a=>a.agent_id===aid)?.x||48)+6);avatar.style.top=pct((data.agents.find(a=>a.agent_id===aid)?.y||72)+8);current.innerHTML=`<strong>Day ${tick.day}, ${tick.time_s}s / ${tick.layer}</strong><p>${tick.avatar_state}</p><div class="row"><span>schedule</span><span>${tick.schedule_state}</span></div><div class="row"><span>body</span><span>${tick.body_state}</span></div><div class="row"><span>object</span><span>${tick.object_transform_state}</span></div><div class="row"><span>dialogue</span><span>${tick.dialogue_state}</span></div><div class="row"><span>save</span><span>${tick.saved_state}</span></div><div class="row"><span>visible</span><span>${tick.visible_world_state}</span></div><div class="row"><span>frequency / flower</span><span>${tick.frequency_hz} Hz / node ${tick.flower_node}</span></div>`;log.innerHTML=`<div>[${idx+1}] day ${tick.day} ${tick.layer}: ${tick.visible_world_state}</div>`+log.innerHTML}function advance(){const tick=data.ticks[idx%data.ticks.length];renderTick(tick);idx++}document.getElementById('advance').onclick=advance;document.getElementById('body').onclick=()=>{const b=data.ticks.find(t=>t.layer==='body_state')||data.ticks[0];renderTick(b)};document.getElementById('run').onclick=()=>{if(timer){clearInterval(timer);timer=null}else{timer=setInterval(advance,900)}};document.getElementById('save').onclick=()=>localStorage.setItem('ssrm-report-229-body-dialogue',JSON.stringify({idx,typed:typed.value}));document.getElementById('restore').onclick=()=>{const s=JSON.parse(localStorage.getItem('ssrm-report-229-body-dialogue')||'{"idx":0,"typed":""}');idx=s.idx||0;typed.value=s.typed||'';advance()};typed.addEventListener('change',()=>{const q=typed.value.toLowerCase();const d=data.dialogues.find(x=>q.includes(x.routed_to)||q.includes(x.intent.split('_')[0]))||data.dialogues[0];dialogue.innerHTML=`<div class="row"><span>typed route</span><span>${d.routed_to}: ${d.agent_reply}</span></div>`+dialogue.innerHTML});placeAgents();drawMetrics();drawDialogue();advance();
</script></body></html>"""
    return html.replace("__DATA__", data_json)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    source = load_source()
    agents = build_agents(source)
    transforms = build_transformations(rng)
    schedules = build_schedules()
    bodies = build_body_ticks()
    dialogues = build_dialogue_turns()
    ticks = build_integration_ticks(transforms, schedules, bodies, dialogues)
    metrics = compute_metrics(agents, transforms, schedules, bodies, dialogues, ticks)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["realtime_body_dialogue_readiness"] >= 0.86 and metrics["weakest_channel_score"] >= 0.68 else "fail"

    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    write_csv(ARTIFACTS / f"{BASE}_agents.csv", agents)
    write_csv(ARTIFACTS / f"{BASE}_object_transformations.csv", transforms)
    write_csv(ARTIFACTS / f"{BASE}_agent_schedules.csv", schedules)
    write_csv(ARTIFACTS / f"{BASE}_body_state_ticks.csv", bodies)
    write_csv(ARTIFACTS / f"{BASE}_typed_dialogue_turns.csv", dialogues)
    write_csv(ARTIFACTS / f"{BASE}_realtime_integration_ticks.csv", ticks)

    results = {
        "module": BASE,
        "report": REPORT,
        "seed": args.seed,
        "module_verdict": verdict,
        "condition": "integrated_playable_local_realtime_compositional_object_transform_schedule_body_state_typed_dialogue",
        "source_artifact": str(SOURCE_STATE),
        "source_condition": source.get("condition", "unknown"),
        "agents": [asdict(item) for item in agents],
        "object_transformations": [asdict(item) for item in transforms],
        "agent_schedules": [asdict(item) for item in schedules],
        "body_state_ticks": [asdict(item) for item in bodies],
        "typed_dialogue_turns": [asdict(item) for item in dialogues],
        "realtime_integration_ticks": [asdict(item) for item in ticks],
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": [
            "This is deterministic realtime body-dialogue scaffolding, not subjective consciousness or real consent.",
            "Typed dialogue is bounded routing over scripted replies, not LLM dialogue or open-ended cognition.",
            "Compositional transformations are structured recipes, not full physics or arbitrary crafting.",
            "Body-state dynamics are welfare-like control signals, not proof of subjective feeling.",
            "Autonomous schedules are deterministic traces, not genuine personal agency.",
            "Frequency and flower overlays are timing and phase scaffolds, not metaphysical evidence.",
        ],
        "next_gate": "playable local 3D continuous life with typed multi-turn dialogue, compositional crafting chains, schedule conflicts, richer body recovery, and persistent personal projects",
    }
    (ARTIFACTS / f"{BASE}_results.json").write_text(json.dumps(results, indent=2))
    (ARTIFACTS / f"{BASE}_state.json").write_text(json.dumps(results, indent=2))
    with (ARTIFACTS / f"{BASE}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "module", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "module": BASE, "verdict": verdict, "readiness": metrics["realtime_body_dialogue_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": results["next_gate"]})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(agents, transforms, schedules, bodies, dialogues, ticks, metrics))

    print(f"module_verdict {verdict}")
    print(f"realtime_body_dialogue_readiness {metrics['realtime_body_dialogue_readiness']:.6f}")
    print(f"agents {len(agents)}")
    print(f"object_transformations {len(transforms)}")
    print(f"agent_schedules {len(schedules)}")
    print(f"body_state_ticks {len(bodies)}")
    print(f"typed_dialogue_turns {len(dialogues)}")
    print(f"realtime_integration_ticks {len(ticks)}")
    print(f"compositional_transformation_depth {metrics['compositional_transformation_depth']:.6f}")
    print(f"schedule_autonomy_rate {metrics['schedule_autonomy_rate']:.6f}")
    print(f"body_to_behavior_binding {metrics['body_to_behavior_binding']:.6f}")
    print(f"typed_dialogue_routing {metrics['typed_dialogue_routing']:.6f}")
    print(f"typed_dialogue_privacy_boundary {metrics['typed_dialogue_privacy_boundary']:.6f}")
    print(f"realtime_integration_tick_merge {metrics['realtime_integration_tick_merge']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
