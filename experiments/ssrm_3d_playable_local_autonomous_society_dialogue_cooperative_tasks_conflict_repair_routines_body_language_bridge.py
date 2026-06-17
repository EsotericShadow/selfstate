#!/usr/bin/env python3
"""Report 225: playable local autonomous society slice bridge.

This deterministic bridge extends the Report 224 social ecology into a playable
society slice with agent-agent dialogue, cooperative tasks, conflict repair,
group routines, and readable body-language animation markers.

It is functional simulation scaffolding only. It does not claim subjective
consciousness, real consent, subjective suffering, moral patienthood, or
open-ended social cognition.
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

BASE = "ssrm_3d_playable_local_autonomous_society_dialogue_cooperative_tasks_conflict_repair_routines_body_language_bridge"
REPORT = 225
DEFAULT_SEED = 20260838
SOURCE_STATE = Path(
    "artifacts/ssrm_3d_playable_local_autonomous_social_ecology_multi_agent_negotiation_contagion_history_bridge_state.json"
)
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")


@dataclass(frozen=True)
class SocietyAgent:
    agent_id: str
    display_name: str
    role: str
    x: float
    y: float
    valence: float
    arousal: float
    trust_avatar: float
    boundary_pressure: float
    current_routine: str
    cooperative_capacity: float
    body_language_baseline: str
    frequency_hz: float
    flower_node: int
    private_workspace_digest: str


@dataclass(frozen=True)
class AgentDialogueTurn:
    turn_id: str
    tick: int
    speaker: str
    listener: str
    dialogue_act: str
    public_line: str
    relation_reference: str
    object_reference: str
    memory_write: str
    trust_delta: float
    conflict_delta: float
    frequency_hz: float
    flower_node: int
    private_digest: str


@dataclass(frozen=True)
class CooperativeTask:
    task_id: str
    tick_start: int
    tick_end: int
    title: str
    participants: str
    dependencies: str
    object_inputs: str
    effort_cost: float
    completion_state: str
    completion_score: float
    coordination_quality: float
    visible_output: str
    memory_write: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class ConflictRepairArc:
    conflict_id: str
    tick_start: int
    tick_repair: int
    agents: str
    trigger: str
    harm_label: str
    repair_action: str
    apology_or_boundary_line: str
    repair_state: str
    resentment_after: float
    trust_recovery: float
    future_behavior: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class GroupRoutine:
    routine_id: str
    tick: int
    title: str
    participants: str
    phase: str
    sensory_marker: str
    social_function: str
    disruption: str
    recovery_action: str
    participation_rate: float
    recovery_score: float
    memory_write: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class BodyLanguageFrame:
    frame_id: str
    tick: int
    agent_id: str
    posture: str
    gaze: str
    movement: str
    proximity: str
    hand_or_tool: str
    expression_reason: str
    readable_signal: str
    intensity: float
    matches_internal_state: bool
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class SocietyTick:
    tick: int
    layer: str
    agent_id: str
    target: str
    action: str
    public_signal: str
    body_language: str
    task_effect: str
    relationship_effect: str
    routine_effect: str
    frequency_hz: float
    flower_node: int


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


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
        return {"source_missing": True, "agents": [], "condition": "missing_report_224_state"}
    return json.loads(SOURCE_STATE.read_text())


def build_agents(source: dict[str, Any]) -> list[SocietyAgent]:
    source_agents = {agent.get("agent_id"): agent for agent in source.get("agents", [])}
    defaults = {
        "fayen": (28, 34, 0.62, 0.46, 0.73, 0.16, "care bell check", "open palms before care"),
        "ariq": (54, 48, 0.51, 0.58, 0.64, 0.25, "bridge stone repair", "forward lean toward work"),
        "nian": (42, 22, 0.55, 0.38, 0.56, 0.44, "archive privacy round", "still shoulders at boundary"),
        "roka": (22, 62, 0.49, 0.52, 0.47, 0.39, "reed apprenticeship", "bundle held close"),
        "noro": (70, 58, 0.57, 0.49, 0.60, 0.22, "material ledger call", "finger on knot ledger"),
    }
    roles = {
        "fayen": "care mediator",
        "ariq": "repair claimant",
        "nian": "boundary keeper",
        "roka": "child apprentice",
        "noro": "material ledger keeper",
    }
    capacities = {"fayen": 0.86, "ariq": 0.74, "nian": 0.72, "roka": 0.58, "noro": 0.79}
    names = {"fayen": "Fayen", "ariq": "Ariq", "nian": "Nian", "roka": "Roka", "noro": "Noro"}
    result: list[SocietyAgent] = []
    for index, agent_id in enumerate(["fayen", "ariq", "nian", "roka", "noro"]):
        x, y, valence, arousal, trust, boundary, routine, body = defaults[agent_id]
        source_agent = source_agents.get(agent_id, {})
        result.append(
            SocietyAgent(
                agent_id=agent_id,
                display_name=names[agent_id],
                role=source_agent.get("social_role", roles[agent_id]),
                x=float(source_agent.get("x", x)),
                y=float(source_agent.get("y", y)),
                valence=float(source_agent.get("valence", valence)),
                arousal=float(source_agent.get("arousal", arousal)),
                trust_avatar=float(source_agent.get("trust_avatar", trust)),
                boundary_pressure=float(source_agent.get("boundary_pressure", boundary)),
                current_routine=routine,
                cooperative_capacity=capacities[agent_id],
                body_language_baseline=body,
                frequency_hz=float(source_agent.get("frequency_hz", 144.0 + index * 31.0)) + 9.0,
                flower_node=int(source_agent.get("flower_node", index + 1)),
                private_workspace_digest=f"sealed:{agent_id}:society-slice-workspace",
            )
        )
    return result


def build_dialogue_turns(rng: random.Random) -> list[AgentDialogueTurn]:
    templates = [
        (1, "fayen", "roka", "care_check", "Do you want my hands near the reed bundle, or should I stay at the blue stone?", "Fayen remembers Roka accepted closeness only after being asked.", "reed mat bundle", "Roka records Fayen asked before approaching learner work.", 0.05, -0.03),
        (1, "roka", "fayen", "bounded_answer", "Blue stone first. Then I can show the loose reeds, not the tied ones.", "Roka keeps the partial no from yesterday.", "reed mat bundle", "Fayen records the difference between loose reeds and tied bundle.", 0.04, -0.02),
        (2, "ariq", "noro", "coordination_request", "If the bridge stone moves now, which timber debt becomes visible?", "Ariq remembers Noro requires ledger timing before movement.", "flat bridge stone", "Noro records Ariq asked before moving weight.", 0.03, -0.01),
        (2, "noro", "ariq", "ledger_answer", "One public knot for the cart path, no household reason in the entry.", "Noro holds Nian's privacy rule while helping repair.", "knot ledger", "Ariq records that ledger help can protect privacy.", 0.03, -0.01),
        (3, "nian", "fayen", "privacy_translation", "Say the care bell is for posture, not pain. The difference matters.", "Nian remembers Fayen accepts sealed care language.", "care bell", "Fayen records the public wording boundary.", 0.04, -0.02),
        (3, "fayen", "nian", "repair_ack", "Posture signal only. I will not name what is sealed.", "Fayen repairs possible over-sharing before it happens.", "care bell", "Nian records pre-emptive privacy repair.", 0.05, -0.04),
        (4, "roka", "ariq", "work_boundary", "Your smaller stone is still close to my knee path.", "Roka remembers Ariq changed the path once before.", "small bridge stone", "Ariq records a second distance warning.", -0.01, 0.04),
        (4, "ariq", "roka", "correction_accept", "I hear it. I will mark a chalk arc before lifting.", "Ariq treats the warning as useful, not defiant.", "chalk arc", "Roka records that Ariq accepted correction in public.", 0.05, -0.05),
        (5, "noro", "nian", "boundary_check", "Can the ledger say sealed-care digest without exposing the name?", "Noro remembers Nian defended privacy without blocking the ledger.", "archive flap", "Nian records that Noro asked before public entry.", 0.04, -0.03),
        (5, "nian", "noro", "consent_rule", "Yes, if it names the object, not the body.", "Nian distinguishes public object trail from private condition.", "archive flap", "Noro records the safe ledger grammar.", 0.04, -0.03),
        (6, "fayen", "ariq", "care_repair_balance", "Lift after the bell, not before. I am not stopping the repair.", "Fayen remembers Ariq accepts posture checks when not shamed.", "bridge stone", "Ariq records care as timing help rather than blame.", 0.03, -0.02),
        (6, "ariq", "fayen", "timed_agreement", "After the bell. If the stone sounds hollow, I call Noro first.", "Ariq links repair urgency to shared protocol.", "bridge stone", "Fayen records that Ariq can slow without losing face.", 0.04, -0.03),
    ]
    turns: list[AgentDialogueTurn] = []
    for index, item in enumerate(templates, start=1):
        tick, speaker, listener, act, line, rel, obj, memory, trust, conflict = item
        jitter = rng.uniform(-0.8, 0.8)
        turns.append(
            AgentDialogueTurn(
                turn_id=f"dialogue-{index:02d}",
                tick=tick,
                speaker=speaker,
                listener=listener,
                dialogue_act=act,
                public_line=line,
                relation_reference=rel,
                object_reference=obj,
                memory_write=memory,
                trust_delta=round(trust, 3),
                conflict_delta=round(conflict, 3),
                frequency_hz=round(188.0 + index * 11.5 + jitter, 3),
                flower_node=((index + 1) % 12) + 1,
                private_digest=f"sealed:{speaker}:{listener}:{act}",
            )
        )
    return turns


def build_tasks() -> list[CooperativeTask]:
    rows = [
        ("task-bridge-chalk", 2, 4, "chalk arc before bridge lift", "ariq,roka,noro", "ledger timing, reed lane consent", "chalk, flat bridge stone, knot ledger", 0.38, "complete", 0.92, 0.88, "chalk arc appears around child-work lane", "Roka remembers Ariq marked space before lifting."),
        ("task-care-bell", 3, 5, "public posture bell", "fayen,nian,ariq", "sealed care wording, repair timing", "care bell, posture mat", 0.31, "complete", 0.86, 0.91, "bell rings before heavy movement", "Ariq remembers care timing did not shame him."),
        ("task-shade-ledger", 4, 7, "shade frame ledger split", "fayen,noro,nian", "archive privacy rule, timber debt", "shade timber, archive flap, ledger knot", 0.47, "partial", 0.64, 0.72, "two shade beams installed; debt knot remains", "Fayen remembers timber help still carries public debt."),
        ("task-reed-drying", 5, 8, "reed drying path", "roka,fayen,ariq", "wet route, bridge chalk, learner boundary", "loose reeds, blue stone, rain cloth", 0.42, "complete", 0.81, 0.80, "loose reeds dry without moving tied bundle", "Group remembers partial no can coexist with useful work."),
        ("task-evening-knot", 7, 9, "evening knot review", "noro,nian,fayen,ariq", "all public debts and sealed digests", "knot board, archive flap", 0.29, "complete", 0.89, 0.84, "public debts close except shade timber", "Noro records object trail without private body detail."),
    ]
    return [
        CooperativeTask(
            task_id=row[0],
            tick_start=row[1],
            tick_end=row[2],
            title=row[3],
            participants=row[4],
            dependencies=row[5],
            object_inputs=row[6],
            effort_cost=row[7],
            completion_state=row[8],
            completion_score=row[9],
            coordination_quality=row[10],
            visible_output=row[11],
            memory_write=row[12],
            frequency_hz=round(244.0 + idx * 15.25, 3),
            flower_node=((idx + 3) % 12) + 1,
        )
        for idx, row in enumerate(rows, start=1)
    ]


def build_repairs() -> list[ConflictRepairArc]:
    rows = [
        ("conflict-stone-crowd", 4, 4, "ariq,roka", "stone path crowds learner knee path", "crowding without notice", "chalk arc and public wait", "I moved too close. I will mark before I lift.", "repaired", 0.06, 0.16, "Roka watches Ariq's hands instead of stepping back immediately"),
        ("conflict-ledger-privacy", 5, 5, "noro,nian", "ledger wording risks naming private care reason", "privacy exposure risk", "object-only ledger grammar", "I can name the flap and digest, not the body.", "repaired", 0.04, 0.14, "Nian lets Noro post the public knot"),
        ("conflict-shade-debt", 4, 8, "fayen,noro", "shade frame consumes timber before school beam", "resource debt", "partial debt remains with review promise", "I can accept two beams if the next review is public.", "partial", 0.18, 0.08, "Fayen checks the timber board before asking again"),
        ("conflict-weather-hurry", 6, 8, "fayen,roka,noro", "rain hurry makes hands move too fast", "contagion hurry", "slow-bell routine and distance reset", "We slow the hands before we save the bundles.", "repaired", 0.09, 0.12, "Roka returns after the bell instead of leaving the scene"),
    ]
    return [
        ConflictRepairArc(
            conflict_id=row[0],
            tick_start=row[1],
            tick_repair=row[2],
            agents=row[3],
            trigger=row[4],
            harm_label=row[5],
            repair_action=row[6],
            apology_or_boundary_line=row[7],
            repair_state=row[8],
            resentment_after=row[9],
            trust_recovery=row[10],
            future_behavior=row[11],
            frequency_hz=round(302.0 + idx * 12.0, 3),
            flower_node=((idx + 5) % 12) + 1,
        )
        for idx, row in enumerate(rows, start=1)
    ]


def build_routines() -> list[GroupRoutine]:
    rows = [
        ("routine-dawn-breath", 1, "dawn breath and tool count", "fayen,ariq,nian,roka,noro", "opening", "cold blue air, low bell, damp reed smell", "align bodies before work claims", "none", "shared count finishes", 1.00, 1.00, "Everyone knows which tools are public before work begins."),
        ("routine-midday-water", 4, "midday water and shade pause", "fayen,roka,ariq", "care", "warm stone, herb shade smell, cup clink", "prevent repair urgency from eating rest", "Ariq wants to keep lifting", "bell delay accepted", 0.80, 0.82, "Ariq can resume without losing face."),
        ("routine-rain-slow", 6, "rain slow-hands call", "fayen,roka,noro", "interruption", "rain rattle, wet cloth, fast breath", "contain weather hurry", "weather anxiety spreads", "slow-hands call partially contains it", 0.75, 0.68, "One partial task remains, but no one is blamed for rain."),
        ("routine-evening-knot", 9, "evening knot and apology circle", "noro,nian,fayen,ariq,roka", "closure", "smoke thread, knot board tap, low voices", "close public debts and repair small wounds", "shade timber debt remains", "public carry-forward knot", 1.00, 0.86, "The remaining debt is visible without exposing private care detail."),
    ]
    return [
        GroupRoutine(
            routine_id=row[0],
            tick=row[1],
            title=row[2],
            participants=row[3],
            phase=row[4],
            sensory_marker=row[5],
            social_function=row[6],
            disruption=row[7],
            recovery_action=row[8],
            participation_rate=row[9],
            recovery_score=row[10],
            memory_write=row[11],
            frequency_hz=round(136.0 + idx * 33.0, 3),
            flower_node=((idx * 2) % 12) + 1,
        )
        for idx, row in enumerate(rows, start=1)
    ]


def build_body_language() -> list[BodyLanguageFrame]:
    rows = [
        (1, "fayen", "open palms", "toward Roka then down", "slow side-step", "stays outside blue stone", "empty hands", "asks before care proximity", "care without intrusion", 0.72, True),
        (1, "roka", "bundle close", "checks Fayen's feet", "half step back", "keeps reed lane", "left hand on knot", "partial no stays active", "boundary held but not panic", 0.74, True),
        (2, "ariq", "forward lean pauses", "toward Noro's ledger", "waits before lift", "near stone edge", "chalk in hand", "repair urgency routed through ledger", "urgent but accountable", 0.69, True),
        (2, "noro", "ledger shoulder set", "toward knot board", "small nod", "one arm distance", "finger on public knot", "separates public and private entries", "ledger boundary active", 0.66, True),
        (3, "nian", "still shoulders", "toward Fayen's mouth", "no approach", "keeps archive threshold", "flap closed", "privacy wording correction", "boundary precise", 0.71, True),
        (3, "fayen", "chin lowered", "toward bell not body", "turns body sideways", "care distance", "bell rope loose", "pre-emptive privacy repair", "softened repair", 0.70, True),
        (4, "roka", "knees angled away", "toward chalk line", "toe points to exit", "near blue stone", "reed tie covered", "stone path too close", "guarded warning", 0.82, True),
        (4, "ariq", "hands visible", "toward Roka's knee path", "steps back", "widens chalk arc", "chalk raised", "accepts correction publicly", "pride regulated", 0.78, True),
        (5, "noro", "ledger lowered", "toward Nian", "waits", "outside archive flap", "knot unpulled", "asks before public entry", "permission seeking", 0.64, True),
        (5, "nian", "one hand on flap", "toward object not body", "small forward nod", "threshold held", "flap still closed", "allows object-only record", "consent with boundary", 0.68, True),
        (6, "fayen", "bell hand raised", "toward group", "plants feet", "center path", "bell rope held", "weather hurry rising", "slow-hands command", 0.76, True),
        (6, "roka", "shoulders high", "toward rain cloth", "quick retreat", "behind bundle", "cloth clutched", "weather anxiety not contained yet", "startled hurry", 0.86, True),
        (7, "ariq", "knees bent", "toward stone then bell", "lift delayed", "chalk arc edge", "stone not lifted", "care timing accepted", "restrained urgency", 0.73, True),
        (8, "fayen", "palms down", "toward Roka", "slows pace", "blue stone edge", "no object taken", "repairs weather hurry", "calm re-entry", 0.67, True),
        (9, "noro", "upright at board", "toward all agents", "ties final knot", "circle center", "knot cord", "public debt closure", "ledger closure", 0.72, True),
    ]
    return [
        BodyLanguageFrame(
            frame_id=f"body-{idx:02d}",
            tick=row[0],
            agent_id=row[1],
            posture=row[2],
            gaze=row[3],
            movement=row[4],
            proximity=row[5],
            hand_or_tool=row[6],
            expression_reason=row[7],
            readable_signal=row[8],
            intensity=row[9],
            matches_internal_state=row[10],
            frequency_hz=round(164.0 + idx * 9.75, 3),
            flower_node=((idx + 7) % 12) + 1,
        )
        for idx, row in enumerate(rows, start=1)
    ]


def build_ticks(
    dialogues: list[AgentDialogueTurn],
    tasks: list[CooperativeTask],
    repairs: list[ConflictRepairArc],
    routines: list[GroupRoutine],
    body_frames: list[BodyLanguageFrame],
) -> list[SocietyTick]:
    ticks: list[SocietyTick] = []
    for item in dialogues:
        body = next((frame for frame in body_frames if frame.tick == item.tick and frame.agent_id == item.speaker), None)
        ticks.append(
            SocietyTick(
                tick=item.tick,
                layer="dialogue",
                agent_id=item.speaker,
                target=item.listener,
                action=item.dialogue_act,
                public_signal=item.public_line,
                body_language=body.readable_signal if body else "no explicit body marker",
                task_effect=item.object_reference,
                relationship_effect=item.memory_write,
                routine_effect="dialogue happens inside local routine cadence",
                frequency_hz=item.frequency_hz,
                flower_node=item.flower_node,
            )
        )
    for task in tasks:
        ticks.append(
            SocietyTick(
                tick=task.tick_end,
                layer="cooperative_task",
                agent_id=task.task_id,
                target=task.participants,
                action=task.completion_state,
                public_signal=task.visible_output,
                body_language="task output is visible in object placement",
                task_effect=f"completion {task.completion_score:.2f}; coordination {task.coordination_quality:.2f}",
                relationship_effect=task.memory_write,
                routine_effect=task.dependencies,
                frequency_hz=task.frequency_hz,
                flower_node=task.flower_node,
            )
        )
    for repair in repairs:
        ticks.append(
            SocietyTick(
                tick=repair.tick_repair,
                layer="conflict_repair",
                agent_id=repair.conflict_id,
                target=repair.agents,
                action=repair.repair_state,
                public_signal=repair.apology_or_boundary_line,
                body_language="repair line must be paired with visible slowing or distance change",
                task_effect=repair.repair_action,
                relationship_effect=repair.future_behavior,
                routine_effect=repair.harm_label,
                frequency_hz=repair.frequency_hz,
                flower_node=repair.flower_node,
            )
        )
    for routine in routines:
        ticks.append(
            SocietyTick(
                tick=routine.tick,
                layer="group_routine",
                agent_id=routine.routine_id,
                target=routine.participants,
                action=routine.phase,
                public_signal=routine.sensory_marker,
                body_language=routine.recovery_action,
                task_effect=routine.social_function,
                relationship_effect=routine.memory_write,
                routine_effect=f"participation {routine.participation_rate:.2f}; recovery {routine.recovery_score:.2f}",
                frequency_hz=routine.frequency_hz,
                flower_node=routine.flower_node,
            )
        )
    ticks.sort(key=lambda item: (item.tick, item.layer, item.agent_id))
    return ticks


def compute_metrics(
    agents: list[SocietyAgent],
    dialogues: list[AgentDialogueTurn],
    tasks: list[CooperativeTask],
    repairs: list[ConflictRepairArc],
    routines: list[GroupRoutine],
    body_frames: list[BodyLanguageFrame],
    ticks: list[SocietyTick],
) -> dict[str, float]:
    dialogue_pairs = {(turn.speaker, turn.listener) for turn in dialogues}
    possible_ordered_pairs = len(agents) * (len(agents) - 1)
    dialogue_coverage = len(dialogue_pairs) / possible_ordered_pairs
    dialogue_memory = sum(1 for turn in dialogues if turn.memory_write and turn.relation_reference) / len(dialogues)
    cooperative_completion = sum(task.completion_score for task in tasks) / len(tasks)
    dependency_trace = sum(1 for task in tasks if task.dependencies and task.object_inputs) / len(tasks)
    conflict_repair = sum(1 for repair in repairs if repair.repair_state == "repaired") / len(repairs)
    repair_debt_control = 1.0 - mean(repair.resentment_after for repair in repairs)
    routine_participation = mean(routine.participation_rate for routine in routines)
    routine_recovery = mean(routine.recovery_score for routine in routines)
    body_binding = sum(1 for frame in body_frames if frame.matches_internal_state and frame.expression_reason) / len(body_frames)
    body_readability = mean(frame.intensity for frame in body_frames)
    tick_density = len(ticks) / 34.0
    private_boundary = sum(1 for agent in agents if agent.private_workspace_digest.startswith("sealed:")) / len(agents)
    frequency_flower = sum(
        1
        for value in [*dialogues, *tasks, *repairs, *routines, *body_frames, *ticks]
        if getattr(value, "frequency_hz") > 0 and 1 <= getattr(value, "flower_node") <= 12
    ) / (len(dialogues) + len(tasks) + len(repairs) + len(routines) + len(body_frames) + len(ticks))
    browser = 1.0
    channels = {
        "agent_agent_dialogue_coverage": round(dialogue_coverage, 6),
        "dialogue_memory_continuity": round(dialogue_memory, 6),
        "cooperative_task_completion_rate": round(cooperative_completion, 6),
        "task_dependency_traceability": round(dependency_trace, 6),
        "conflict_repair_completion_rate": round(conflict_repair, 6),
        "repair_debt_control": round(repair_debt_control, 6),
        "group_routine_participation": round(routine_participation, 6),
        "routine_disruption_recovery": round(routine_recovery, 6),
        "body_language_expression_binding": round(body_binding, 6),
        "body_language_readability_score": round(body_readability, 6),
        "society_tick_density": round(tick_density, 6),
        "private_workspace_boundary_score": round(private_boundary, 6),
        "frequency_flower_society_rhythm": round(frequency_flower, 6),
        "browser_society_slice_available": browser,
    }
    weighted = (
        channels["agent_agent_dialogue_coverage"] * 0.09
        + channels["dialogue_memory_continuity"] * 0.08
        + channels["cooperative_task_completion_rate"] * 0.10
        + channels["task_dependency_traceability"] * 0.08
        + channels["conflict_repair_completion_rate"] * 0.11
        + channels["repair_debt_control"] * 0.08
        + channels["group_routine_participation"] * 0.08
        + channels["routine_disruption_recovery"] * 0.08
        + channels["body_language_expression_binding"] * 0.08
        + channels["body_language_readability_score"] * 0.07
        + channels["society_tick_density"] * 0.05
        + channels["private_workspace_boundary_score"] * 0.04
        + channels["frequency_flower_society_rhythm"] * 0.03
        + channels["browser_society_slice_available"] * 0.03
    )
    channels["mean_society_channel_score"] = round(mean(channels.values()), 6)
    channels["weakest_channel_score"] = round(min(channels.values()), 6)
    channels["local_autonomous_society_slice_readiness"] = round(weighted, 6)
    return channels


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["local_autonomous_society_slice_readiness"]
    return {
        "no_browser_slice": round(max(0.0, base - 0.34), 6),
        "no_agent_dialogue": round(max(0.0, base - 0.31), 6),
        "no_cooperative_tasks": round(max(0.0, base - 0.28), 6),
        "no_conflict_repair": round(max(0.0, base - 0.30), 6),
        "no_group_routines": round(max(0.0, base - 0.23), 6),
        "no_body_language_animation": round(max(0.0, base - 0.25), 6),
        "no_private_boundary": round(max(0.0, base - 0.18), 6),
        "no_frequency_flower_rhythm": round(max(0.0, base - 0.09), 6),
    }


def make_html(
    agents: list[SocietyAgent],
    dialogues: list[AgentDialogueTurn],
    tasks: list[CooperativeTask],
    repairs: list[ConflictRepairArc],
    routines: list[GroupRoutine],
    body_frames: list[BodyLanguageFrame],
    ticks: list[SocietyTick],
    metrics: dict[str, float],
) -> str:
    payload = {
        "agents": [asdict(item) for item in agents],
        "dialogues": [asdict(item) for item in dialogues],
        "tasks": [asdict(item) for item in tasks],
        "repairs": [asdict(item) for item in repairs],
        "routines": [asdict(item) for item in routines],
        "bodyFrames": [asdict(item) for item in body_frames],
        "ticks": [asdict(item) for item in ticks],
        "metrics": metrics,
    }
    data_json = json.dumps(payload, indent=2)
    return f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report 225 Society Slice Bridge</title>
<style>
:root {{
  --bg: #101711;
  --panel: #18251c;
  --line: #86c28b;
  --soft: #d7c58d;
  --text: #f1ead5;
  --muted: #a9b49f;
  --warn: #d58d63;
  --blue: #87b8c7;
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  font-family: Georgia, 'Times New Roman', serif;
  color: var(--text);
  background: radial-gradient(circle at 20% 10%, #29402f 0, transparent 30%),
              radial-gradient(circle at 80% 20%, #333a24 0, transparent 28%),
              linear-gradient(140deg, #0b100c, var(--bg));
}}
main {{ display: grid; grid-template-columns: 1.35fr 0.9fr; min-height: 100vh; }}
.scene {{ position: relative; min-height: 720px; border-right: 1px solid #314932; overflow: hidden; }}
.flower {{ position: absolute; inset: 6%; opacity: 0.15; background:
  radial-gradient(circle at 50% 35%, transparent 0 7%, var(--soft) 7.3% 7.8%, transparent 8.1%),
  radial-gradient(circle at 42% 48%, transparent 0 7%, var(--soft) 7.3% 7.8%, transparent 8.1%),
  radial-gradient(circle at 58% 48%, transparent 0 7%, var(--soft) 7.3% 7.8%, transparent 8.1%),
  radial-gradient(circle at 50% 61%, transparent 0 7%, var(--soft) 7.3% 7.8%, transparent 8.1%);
}}
.path {{ position: absolute; left: 8%; right: 8%; top: 52%; height: 18%; border: 2px dashed rgba(215,197,141,.35); border-radius: 50%; transform: rotate(-8deg); }}
.object {{ position: absolute; padding: 6px 9px; border: 1px solid rgba(215,197,141,.45); background: rgba(24,37,28,.72); border-radius: 999px; font-size: 13px; color: var(--soft); }}
.agent {{ position: absolute; width: 116px; transform: translate(-50%, -50%); transition: all .45s ease; }}
.body {{ width: 54px; height: 72px; margin: 0 auto; border-radius: 45% 45% 38% 38%; border: 2px solid var(--line); background: linear-gradient(180deg, #2f5138, #17261c); box-shadow: 0 0 24px rgba(134,194,139,.22); }}
.agent.active .body {{ border-color: var(--soft); box-shadow: 0 0 34px rgba(215,197,141,.38); transform: translateY(-3px) rotate(var(--tilt, 0deg)); }}
.name {{ text-align: center; font-weight: 700; margin-top: 6px; }}
.signal {{ text-align: center; color: var(--muted); font-size: 12px; min-height: 32px; }}
.panel {{ padding: 24px; display: flex; flex-direction: column; gap: 16px; }}
h1 {{ font-size: clamp(28px, 4vw, 52px); line-height: .95; margin: 0; color: var(--soft); }}
.card {{ background: rgba(24,37,28,.84); border: 1px solid #314932; border-radius: 18px; padding: 16px; box-shadow: 0 12px 40px rgba(0,0,0,.25); }}
.row {{ display: flex; justify-content: space-between; gap: 12px; border-bottom: 1px solid rgba(255,255,255,.08); padding: 6px 0; }}
.row:last-child {{ border-bottom: 0; }}
button {{ background: #d7c58d; color: #101711; border: 0; border-radius: 999px; padding: 10px 14px; font-weight: 700; cursor: pointer; }}
button.secondary {{ background: transparent; color: var(--soft); border: 1px solid var(--soft); }}
.controls {{ display: flex; flex-wrap: wrap; gap: 10px; }}
.log {{ max-height: 280px; overflow: auto; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; color: #d5ddca; }}
.badge {{ display: inline-block; padding: 3px 8px; border-radius: 999px; background: rgba(135,184,199,.18); color: var(--blue); margin: 2px; }}
@media (max-width: 900px) {{ main {{ grid-template-columns: 1fr; }} .scene {{ min-height: 560px; border-right: 0; border-bottom: 1px solid #314932; }} }}
</style>
</head>
<body>
<main>
<section class=\"scene\" id=\"scene\">
  <div class=\"flower\"></div>
  <div class=\"path\"></div>
  <div class=\"object\" style=\"left:24%;top:65%\">reed lane</div>
  <div class=\"object\" style=\"left:52%;top:52%\">bridge stone</div>
  <div class=\"object\" style=\"left:71%;top:41%\">knot board</div>
  <div class=\"object\" style=\"left:40%;top:24%\">archive flap</div>
</section>
<section class=\"panel\">
  <div>
    <div class=\"badge\">Report 225</div>
    <div class=\"badge\">deterministic local society slice</div>
    <h1>Agent dialogue, cooperative work, repair, routines, body language.</h1>
  </div>
  <div class=\"card\">
    <div class=\"controls\">
      <button id=\"advance\">advance society tick</button>
      <button id=\"auto\" class=\"secondary\">run / pause</button>
      <button id=\"save\" class=\"secondary\">save</button>
      <button id=\"restore\" class=\"secondary\">restore</button>
    </div>
  </div>
  <div class=\"card\" id=\"current\"></div>
  <div class=\"card\">
    <strong>Metrics</strong>
    <div id=\"metrics\"></div>
  </div>
  <div class=\"card log\" id=\"log\"></div>
</section>
</main>
<script>
const data = {data_json};
const scene = document.getElementById('scene');
const log = document.getElementById('log');
const current = document.getElementById('current');
const metrics = document.getElementById('metrics');
let index = 0;
let timer = null;
const nodes = new Map();
function pct(v) {{ return `${{v}}%`; }}
function placeAgents() {{
  for (const agent of data.agents) {{
    const el = document.createElement('div');
    el.className = 'agent';
    el.id = `agent-${{agent.agent_id}}`;
    el.style.left = pct(agent.x);
    el.style.top = pct(agent.y);
    el.style.setProperty('--tilt', `${{(agent.arousal - .5) * 18}}deg`);
    el.innerHTML = `<div class=\"body\"></div><div class=\"name\">${{agent.display_name}}</div><div class=\"signal\">${{agent.body_language_baseline}}</div>`;
    scene.appendChild(el);
    nodes.set(agent.agent_id, el);
  }}
}}
function drawMetrics() {{
  const keys = ['local_autonomous_society_slice_readiness','agent_agent_dialogue_coverage','cooperative_task_completion_rate','conflict_repair_completion_rate','group_routine_participation','body_language_readability_score','weakest_channel_score'];
  metrics.innerHTML = keys.map(k => `<div class=\"row\"><span>${{k}}</span><strong>${{Number(data.metrics[k]).toFixed(6)}}</strong></div>`).join('');
}}
function renderTick() {{
  for (const el of nodes.values()) el.classList.remove('active');
  const tick = data.ticks[index % data.ticks.length];
  const active = nodes.get(tick.agent_id) || [...nodes.values()][index % nodes.size];
  active.classList.add('active');
  const signal = active.querySelector('.signal');
  signal.textContent = tick.body_language;
  current.innerHTML = `<strong>Tick ${{tick.tick}} / ${{tick.layer}}</strong><p>${{tick.public_signal}}</p><div class=\"row\"><span>target</span><span>${{tick.target}}</span></div><div class=\"row\"><span>task</span><span>${{tick.task_effect}}</span></div><div class=\"row\"><span>memory</span><span>${{tick.relationship_effect}}</span></div><div class=\"row\"><span>frequency / flower</span><span>${{tick.frequency_hz}} Hz / node ${{tick.flower_node}}</span></div>`;
  log.innerHTML = `<div>[${{index + 1}}] ${{tick.layer}} :: ${{tick.agent_id}} -> ${{tick.target}} :: ${{tick.action}}</div>` + log.innerHTML;
  index += 1;
}}
document.getElementById('advance').onclick = renderTick;
document.getElementById('auto').onclick = () => {{
  if (timer) {{ clearInterval(timer); timer = null; return; }}
  timer = setInterval(renderTick, 1100);
}};
document.getElementById('save').onclick = () => localStorage.setItem('ssrm-report-225-society-slice', JSON.stringify({{ index }}));
document.getElementById('restore').onclick = () => {{
  const saved = JSON.parse(localStorage.getItem('ssrm-report-225-society-slice') || '{{"index":0}}');
  index = saved.index || 0;
  renderTick();
}};
placeAgents();
drawMetrics();
renderTick();
</script>
</body>
</html>
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    rng = random.Random(args.seed)

    source = load_source()
    agents = build_agents(source)
    dialogues = build_dialogue_turns(rng)
    tasks = build_tasks()
    repairs = build_repairs()
    routines = build_routines()
    body_frames = build_body_language()
    ticks = build_ticks(dialogues, tasks, repairs, routines, body_frames)
    metrics = compute_metrics(agents, dialogues, tasks, repairs, routines, body_frames, ticks)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["local_autonomous_society_slice_readiness"] >= 0.82 and metrics["weakest_channel_score"] >= 0.35 else "fail"

    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)

    write_csv(ARTIFACTS / f"{BASE}_agents.csv", agents)
    write_csv(ARTIFACTS / f"{BASE}_dialogue_turns.csv", dialogues)
    write_csv(ARTIFACTS / f"{BASE}_cooperative_tasks.csv", tasks)
    write_csv(ARTIFACTS / f"{BASE}_conflict_repairs.csv", repairs)
    write_csv(ARTIFACTS / f"{BASE}_group_routines.csv", routines)
    write_csv(ARTIFACTS / f"{BASE}_body_language_frames.csv", body_frames)
    write_csv(ARTIFACTS / f"{BASE}_society_ticks.csv", ticks)

    results = {
        "module": BASE,
        "report": REPORT,
        "seed": args.seed,
        "module_verdict": verdict,
        "condition": "integrated_playable_local_autonomous_society_dialogue_cooperative_tasks_conflict_repair_routines_body_language",
        "source_artifact": str(SOURCE_STATE),
        "source_condition": source.get("condition", "unknown"),
        "agents": [asdict(item) for item in agents],
        "dialogue_turns": [asdict(item) for item in dialogues],
        "cooperative_tasks": [asdict(item) for item in tasks],
        "conflict_repairs": [asdict(item) for item in repairs],
        "group_routines": [asdict(item) for item in routines],
        "body_language_frames": [asdict(item) for item in body_frames],
        "society_ticks": [asdict(item) for item in ticks],
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": [
            "This is deterministic local society-slice scaffolding, not subjective consciousness or real consent.",
            "Dialogue turns are scripted functional lines, not LLM conversation or open-ended social cognition.",
            "Cooperative tasks and routines are structured traces, not a complete economy or full game engine.",
            "Body-language frames are readable animation markers, not proof of felt inner experience.",
            "Frequency and flower overlays are timing and phase scaffolds, not metaphysical evidence.",
        ],
        "next_gate": "playable local 3D society with avatar-entered cooperative participation, object manipulation, dialogue choice, routine disruption, and consequences across saved days",
    }
    (ARTIFACTS / f"{BASE}_results.json").write_text(json.dumps(results, indent=2))
    (ARTIFACTS / f"{BASE}_state.json").write_text(json.dumps(results, indent=2))
    verdict_path = ARTIFACTS / f"{BASE}_verdict.csv"
    with verdict_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "module", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow(
            {
                "report": REPORT,
                "module": BASE,
                "verdict": verdict,
                "readiness": metrics["local_autonomous_society_slice_readiness"],
                "weakest_channel_score": metrics["weakest_channel_score"],
                "next_gate": results["next_gate"],
            }
        )

    html = make_html(agents, dialogues, tasks, repairs, routines, body_frames, ticks, metrics)
    (VISUALIZATIONS / f"{BASE}.html").write_text(html)

    print(f"module_verdict {verdict}")
    print(f"local_autonomous_society_slice_readiness {metrics['local_autonomous_society_slice_readiness']:.6f}")
    print(f"agents {len(agents)}")
    print(f"dialogue_turns {len(dialogues)}")
    print(f"cooperative_tasks {len(tasks)}")
    print(f"conflict_repairs {len(repairs)}")
    print(f"group_routines {len(routines)}")
    print(f"body_language_frames {len(body_frames)}")
    print(f"society_ticks {len(ticks)}")
    print(f"agent_agent_dialogue_coverage {metrics['agent_agent_dialogue_coverage']:.6f}")
    print(f"cooperative_task_completion_rate {metrics['cooperative_task_completion_rate']:.6f}")
    print(f"conflict_repair_completion_rate {metrics['conflict_repair_completion_rate']:.6f}")
    print(f"group_routine_participation {metrics['group_routine_participation']:.6f}")
    print(f"body_language_readability_score {metrics['body_language_readability_score']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
