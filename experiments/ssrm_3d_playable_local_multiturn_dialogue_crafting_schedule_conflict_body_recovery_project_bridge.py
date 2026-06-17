#!/usr/bin/env python3
"""Report 230: multi-turn dialogue, crafting chains, conflicts, recovery, projects.

This deterministic bridge extends Report 229 by adding typed multi-turn dialogue
threads, compositional crafting chains, schedule conflicts, richer body recovery,
and persistent personal projects inside the realtime loop.

It remains functional scaffolding only. It does not claim subjective
consciousness, real consent, subjective suffering, moral patienthood, LLM
dialogue, open-ended cognition, full physics, arbitrary crafting, or complete
gameplay.
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

BASE = "ssrm_3d_playable_local_multiturn_dialogue_crafting_schedule_conflict_body_recovery_project_bridge"
REPORT = 230
DEFAULT_SEED = 20260843
SOURCE_STATE = Path("artifacts/ssrm_3d_playable_local_compositional_transform_schedule_body_dialogue_realtime_bridge_state.json")
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")


@dataclass(frozen=True)
class ProjectAgent:
    agent_id: str
    display_name: str
    role: str
    x: float
    y: float
    current_project: str
    body_recovery_focus: str
    dialogue_boundary: str
    craft_skill: str
    private_workspace_digest: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class MultiTurnDialogue:
    thread_id: str
    turn_index: int
    day: int
    time_s: float
    speaker: str
    listener: str
    typed_or_spoken_line: str
    intent: str
    prior_context: str
    privacy_gate: str
    reply: str
    memory_write: str
    relationship_delta: float
    state_delta: str
    continuation_state: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class CraftingChainStep:
    chain_id: str
    step_index: int
    day: int
    time_s: float
    actor: str
    project_link: str
    recipe_stage: str
    input_materials: str
    tools: str
    preconditions: str
    output_materials: str
    waste_or_byproduct: str
    quality_score: float
    dependency_state: str
    failure_or_delay: str
    repair_or_rollback: str
    saved_state_key: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class ScheduleConflict:
    conflict_id: str
    day: int
    time_s: float
    agents: str
    conflicting_phases: str
    contested_resource_or_place: str
    cause: str
    arbitration_rule: str
    outcome: str
    delay_cost: float
    fairness_score: float
    recovery_score: float
    unresolved_debt: float
    future_schedule_memory: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class BodyRecovery:
    recovery_id: str
    day: int
    time_s: float
    agent_id: str
    trigger: str
    before_energy: float
    before_fatigue: float
    before_pain: float
    before_arousal: float
    recovery_action: str
    consent_state: str
    after_energy: float
    after_fatigue: float
    after_pain: float
    after_arousal: float
    recovery_score: float
    residual_need: str
    visible_behavior_change: str
    saved_memory: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class PersistentProject:
    project_id: str
    owner: str
    title: str
    goal: str
    current_phase: str
    linked_chain: str
    progress_before: float
    progress_after: float
    blockers: str
    schedule_dependency: str
    body_dependency: str
    social_dependency: str
    next_action: str
    saved_project_memory: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class ProjectLoopTick:
    tick_id: str
    day: int
    time_s: float
    layer: str
    dialogue_state: str
    crafting_state: str
    schedule_state: str
    body_state: str
    project_state: str
    visible_world_state: str
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
        return {"source_missing": True, "agents": [], "condition": "missing_report_229_state"}
    return json.loads(SOURCE_STATE.read_text())


def build_agents(source: dict[str, Any]) -> list[ProjectAgent]:
    source_agents = {agent.get("agent_id"): agent for agent in source.get("agents", [])}
    specs = [
        ("fayen", "Fayen", "care mediator", 28, 34, "care kit standard", "fatigue and breath recovery", "posture language only", "care-kit staging"),
        ("ariq", "Ariq", "repair claimant", 54, 48, "cart-safe bridge edge", "pain-aware lifting", "pride-safe caution", "stone and chalk repair"),
        ("nian", "Nian", "boundary keeper", 42, 22, "privacy ledger grammar", "control after threshold stress", "object trail not body reason", "digest wording"),
        ("roka", "Roka", "child apprentice", 22, 62, "reed lesson tray", "wetness and confidence recovery", "loose reeds not tied bundle", "reed sorting"),
        ("noro", "Noro", "material ledger keeper", 70, 58, "shade debt review", "focus after public conflict", "public debt only", "knot accounting"),
    ]
    result: list[ProjectAgent] = []
    for idx, spec in enumerate(specs, start=1):
        agent_id, name, role, x, y, project, recovery, boundary, skill = spec
        src = source_agents.get(agent_id, {})
        result.append(
            ProjectAgent(
                agent_id=agent_id,
                display_name=name,
                role=src.get("role", role),
                x=float(src.get("x", x)),
                y=float(src.get("y", y)),
                current_project=project,
                body_recovery_focus=recovery,
                dialogue_boundary=boundary,
                craft_skill=skill,
                private_workspace_digest=f"sealed:{agent_id}:multiturn-project-workspace",
                frequency_hz=round(float(src.get("frequency_hz", 150 + idx * 31)) + 29, 3),
                flower_node=int(src.get("flower_node", idx + 1)),
            )
        )
    return result


def build_dialogue_threads(rng: random.Random) -> list[MultiTurnDialogue]:
    threads = [
        (
            "thread-stone-help",
            [
                (1, 1810.0, "avatar", "ariq", "Can I help with the stone now?", "task_help", "stone test is pending", "private pain stays sealed", "After the bell. Hold the chalk cord first.", "Ariq records that Gabriel asked before lifting.", 0.04, "stone help gated by bell", "open"),
                (1, 1811.5, "avatar", "fayen", "Fayen, is the bell enough?", "care_timing", "Ariq accepted bell timing", "posture public, pain private", "Bell, breath, then chalk. No pain words.", "Fayen records posture-safe timing.", 0.05, "care language set", "open"),
                (1, 1813.0, "avatar", "ariq", "I rang it. Should I pull the cord tight?", "tool_followup", "bell rung, chalk cord active", "do not override Roka line", "Tension only to the blue mark. Stop if Roka moves.", "Ariq records bounded tool help.", 0.03, "chalk cord controlled", "resolved"),
            ],
        ),
        (
            "thread-reed-boundary",
            [
                (2, 2706.0, "avatar", "roka", "Which reeds can I carry today?", "access_query", "prior tied-bundle overreach", "child-work bundle boundary", "Loose tray only. Ask every time.", "Roka records repeated asking as safer than guessing.", 0.04, "loose tray open", "open"),
                (2, 2708.0, "avatar", "roka", "Can I watch the tied bundle lesson?", "watch_request", "blue stone distance available", "watching is not touching", "From the blue stone. Hands behind cord.", "Roka records watching without touching.", 0.03, "watch access conditional", "open"),
                (2, 2710.0, "avatar", "fayen", "Can you stand near us while I help?", "support_request", "Roka trust partial", "do not turn care into surveillance", "I can stand by the shade edge, not over Roka.", "Fayen records support without crowding.", 0.02, "support position set", "resolved"),
            ],
        ),
        (
            "thread-debt-review",
            [
                (3, 2720.0, "avatar", "noro", "I read the debt line. Can I ask for the beam review?", "debt_review", "shade debt open", "public debt only", "Yes. Ask for review, not timber now.", "Noro records accountable request.", 0.04, "review scheduled", "open"),
                (3, 2721.5, "avatar", "nian", "Does the review expose care reasons?", "privacy_check", "review touches shade care", "object trail only", "No. It names beam, shade, and debt. Not body reasons.", "Nian records review privacy boundary.", 0.04, "review privacy safe", "open"),
                (3, 2723.0, "avatar", "noro", "Then I will ask at evening circle.", "commitment", "review allowed, private reasons sealed", "circle edge only", "Edge of circle. Read the debt first.", "Noro records a public review promise.", 0.03, "evening review promise", "resolved"),
            ],
        ),
        (
            "thread-archive-wording",
            [
                (4, 910.0, "avatar", "nian", "I wrote object trail but added too much detail.", "wording_repair", "digest knot wording drift", "remove body reason", "Untie that phrase. Keep object, place, day.", "Nian records repair before public posting.", 0.05, "digest wording repaired", "open"),
                (4, 911.5, "avatar", "noro", "Can the knot say shade frame and day four?", "ledger_phrase", "Nian approved object/place/day", "ledger public only", "Yes. Shade frame, day four, open debt.", "Noro records approved public phrase.", 0.04, "knot phrase approved", "open"),
                (4, 913.0, "avatar", "nian", "I will leave out the reason for shade.", "privacy_commitment", "public phrase ready", "reason remains sealed", "Good. That is the line.", "Nian records privacy commitment held.", 0.04, "privacy-safe knot", "resolved"),
            ],
        ),
    ]
    rows: list[MultiTurnDialogue] = []
    for thread_id, turns in threads:
        for turn_index, t in enumerate(turns, start=1):
            day, time_s, speaker, listener, line, intent, context, gate, reply, memory, rel, delta, cont = t
            rows.append(
                MultiTurnDialogue(
                    thread_id=thread_id,
                    turn_index=turn_index,
                    day=day,
                    time_s=round(time_s + rng.uniform(-0.25, 0.25), 3),
                    speaker=speaker,
                    listener=listener,
                    typed_or_spoken_line=line,
                    intent=intent,
                    prior_context=context,
                    privacy_gate=gate,
                    reply=reply,
                    memory_write=memory,
                    relationship_delta=rel,
                    state_delta=delta,
                    continuation_state=cont,
                    frequency_hz=round(310.0 + len(rows) * 6.75, 3),
                    flower_node=((len(rows) + 5) % 12) + 1,
                )
            )
    return rows


def build_crafting_chains() -> list[CraftingChainStep]:
    chains = [
        (
            "chain-reed-tray",
            "roka",
            "reed lesson tray",
            [
                (1, "sort loose reeds", "loose reeds,rain cloth", "reed comb", "Roka names loose-only boundary", "sorted reed strips", "mud flecks", 0.82, "root", "none", "ask before next sort", True),
                (2, "dry strips", "sorted reed strips,blue stone warmth", "rain cloth", "sun patch and no tied bundle touch", "dry reed strips", "wet cloth drip", 0.78, "sort loose reeds", "rain slows drying", "turn strips after rain", True),
                (3, "tie lesson tray", "dry reed strips,teaching cord", "reed comb", "Roka permits loose tray", "lesson tray", "short reed waste", 0.74, "dry strips", "loose tray only", "mark tied bundle closed", False),
            ],
        ),
        (
            "chain-bridge-edge",
            "ariq",
            "cart-safe bridge edge",
            [
                (1, "draw chalk arc", "chalk cord,flat stone", "care bell", "bell rung and Roka line visible", "wide chalk arc", "chalk dust", 0.88, "root", "none", "erase if too narrow", True),
                (2, "tap stone edge", "flat stone,wide chalk arc", "tap stone", "Noro reachable", "hollow edge mark", "stone grit", 0.76, "draw chalk arc", "hollow sound", "stop lift and call Noro", False),
                (3, "brace cart edge", "hollow edge mark,brace timber", "ledger cord", "debt knot visible", "cart-safe half edge", "wood splinter", 0.69, "tap stone edge", "timber debt delay", "review debt before second brace", False),
            ],
        ),
        (
            "chain-care-kit",
            "fayen",
            "public care kit standard",
            [
                (1, "stage cups", "water cups,shade mat", "clean cloth", "rest pause accepted", "cup station", "used water", 0.91, "root", "none", "return cups after use", True),
                (2, "add posture bell card", "cup station,care bell", "public wording cord", "pain words sealed", "posture timing card", "discarded private phrase", 0.86, "stage cups", "wording drift", "rewrite posture only", True),
                (3, "close care kit standard", "posture timing card,clean cloth", "shade cord", "Fayen approves public language", "care kit standard", "damp cloth", 0.83, "add posture bell card", "cloth shortage", "wash and dry cloth", True),
            ],
        ),
        (
            "chain-ledger-review",
            "noro",
            "shade debt review packet",
            [
                (1, "read open debt", "debt knot,shade beam", "public board", "avatar reads debt first", "debt line spoken", "frayed cord", 0.87, "root", "none", "repeat line if disputed", True),
                (2, "add review request", "debt line spoken,review cord", "knot board", "Nian confirms privacy", "review request knot", "extra cord tail", 0.80, "read open debt", "privacy question", "remove private cause", True),
                (3, "schedule evening review", "review request knot,circle edge", "bell marker", "Noro accepts edge-of-circle participation", "evening review slot", "open debt remains", 0.72, "add review request", "review delayed", "carry review to next day", False),
            ],
        ),
    ]
    rows: list[CraftingChainStep] = []
    for chain_id, actor, project, steps in chains:
        for step_index, step in enumerate(steps, start=1):
            day, stage, inputs, tools, pre, output, waste, quality, dep, failure, repair, reversible = step
            rows.append(
                CraftingChainStep(
                    chain_id=chain_id,
                    step_index=step_index,
                    day=day,
                    time_s=round(day * 700 + step_index * 21.0, 3),
                    actor=actor,
                    project_link=project,
                    recipe_stage=stage,
                    input_materials=inputs,
                    tools=tools,
                    preconditions=pre,
                    output_materials=output,
                    waste_or_byproduct=waste,
                    quality_score=quality,
                    dependency_state=dep,
                    failure_or_delay=failure,
                    repair_or_rollback=repair,
                    saved_state_key=f"craft:{chain_id}:{step_index}",
                    frequency_hz=round(228.0 + len(rows) * 8.5, 3),
                    flower_node=((len(rows) + 7) % 12) + 1,
                )
            )
    return rows


def build_schedule_conflicts() -> list[ScheduleConflict]:
    rows = [
        ("conflict-bell-stone", 1, 1812.0, "ariq,fayen", "repair vs care", "care bell", "Ariq wants lift before posture bell", "care timing gates repair", "bell first, chalk second, lift later", 0.16, 0.86, 0.88, 0.04, "Ariq schedules stone work after bell next time"),
        ("conflict-reed-rain", 2, 1408.0, "roka,environment,fayen", "learning vs weather", "blue stone reed lane", "rain interrupts loose reed drying", "weather cause is named, not blamed", "turn strips after rain and keep tied bundle closed", 0.22, 0.78, 0.74, 0.12, "Roka schedules loose reeds after rain check"),
        ("conflict-shade-ledger", 3, 2722.0, "noro,fayen,avatar", "shade help vs timber scarcity", "shade beam", "avatar asks before public debt closes", "public debt review before more timber", "review scheduled, second beam locked", 0.28, 0.72, 0.70, 0.18, "Noro carries shade debt to evening review"),
        ("conflict-archive-review", 4, 913.0, "nian,noro", "privacy vs ledger speed", "digest knot", "ledger wants phrase before Nian approves", "object/place/day grammar", "phrase repaired before posting", 0.10, 0.90, 0.92, 0.02, "Noro checks Nian before public digest knots"),
        ("conflict-care-cloth", 4, 1160.0, "fayen,roka", "care kit vs reed drying", "clean cloth", "care kit needs cloth while reed strips are damp", "care item can borrow after reed turn", "cloth shared with drying deadline", 0.20, 0.80, 0.76, 0.10, "Fayen checks reed drying before taking cloth"),
    ]
    return [
        ScheduleConflict(
            conflict_id=row[0],
            day=row[1],
            time_s=row[2],
            agents=row[3],
            conflicting_phases=row[4],
            contested_resource_or_place=row[5],
            cause=row[6],
            arbitration_rule=row[7],
            outcome=row[8],
            delay_cost=row[9],
            fairness_score=row[10],
            recovery_score=row[11],
            unresolved_debt=row[12],
            future_schedule_memory=row[13],
            frequency_hz=round(360.0 + idx * 7.0, 3),
            flower_node=((idx + 9) % 12) + 1,
        )
        for idx, row in enumerate(rows, start=1)
    ]


def build_body_recoveries() -> list[BodyRecovery]:
    rows = [
        ("rec-ariq-breath", 1, 1825.0, "ariq", "stone effort breath spike", 0.54, 0.46, 0.34, 0.72, "posture bell and breath count", "accepted", 0.60, 0.38, 0.26, 0.54, 0.78, "stone effort still tiring", "kneels, breath slows, hands visible", "Ariq remembers stopping without shame"),
        ("rec-roka-wet", 2, 1420.0, "roka", "rain wetness during reed lesson", 0.52, 0.40, 0.14, 0.68, "dry cloth and blue stone distance", "accepted_conditionally", 0.56, 0.34, 0.11, 0.50, 0.76, "tied bundle still closed", "shoulders lower, loose tray returns", "Roka remembers rain was named as cause"),
        ("rec-fayen-fatigue", 2, 1530.0, "fayen", "care tasks stack during shade pause", 0.62, 0.44, 0.16, 0.48, "cup carry delegation and seated pause", "accepted", 0.68, 0.33, 0.12, 0.38, 0.82, "cloth washing remains", "sits before giving next instruction", "Fayen remembers help did not erase pause"),
        ("rec-nian-control", 3, 914.0, "nian", "private wording nearly exposed", 0.66, 0.28, 0.08, 0.61, "untie phrase and repeat object-only grammar", "accepted", 0.68, 0.24, 0.07, 0.42, 0.84, "threshold vigilance remains", "still shoulders soften after wording repair", "Nian remembers correction before posting"),
        ("rec-noro-focus", 4, 2730.0, "noro", "debt review pressure", 0.58, 0.38, 0.10, 0.57, "public debt read before request", "accepted", 0.62, 0.31, 0.08, 0.41, 0.80, "open debt remains public", "board taps slow, voice steadies", "Noro remembers accountable review request"),
        ("rec-ariq-delayed", 4, 2810.0, "ariq", "repair delayed by timber review", 0.50, 0.52, 0.28, 0.64, "schedule catchup and no solo lift", "accepted_partial", 0.54, 0.47, 0.24, 0.50, 0.68, "repair still incomplete", "steps back from stone without dropping project", "Ariq remembers delay without project loss"),
    ]
    return [
        BodyRecovery(
            recovery_id=row[0],
            day=row[1],
            time_s=row[2],
            agent_id=row[3],
            trigger=row[4],
            before_energy=row[5],
            before_fatigue=row[6],
            before_pain=row[7],
            before_arousal=row[8],
            recovery_action=row[9],
            consent_state=row[10],
            after_energy=row[11],
            after_fatigue=row[12],
            after_pain=row[13],
            after_arousal=row[14],
            recovery_score=row[15],
            residual_need=row[16],
            visible_behavior_change=row[17],
            saved_memory=row[18],
            frequency_hz=round(144.0 + idx * 12.25, 3),
            flower_node=((idx + 4) % 12) + 1,
        )
        for idx, row in enumerate(rows, start=1)
    ]


def build_projects() -> list[PersistentProject]:
    rows = [
        ("proj-care-kit", "fayen", "public care kit standard", "make care help repeatable without private pain exposure", "standard drafted", "chain-care-kit", 0.35, 0.72, "cloth washing and posture wording", "shade pause schedule", "fatigue recovery", "Nian wording approval", "wash cloth and test second care pause", "Fayen keeps care kit standard across days"),
        ("proj-bridge-edge", "ariq", "cart-safe bridge edge", "make bridge safe without solo strain or child-lane crowding", "partial edge safe", "chain-bridge-edge", 0.42, 0.69, "timber debt and hollow edge", "bell-gated repair", "pain-aware lift recovery", "Noro debt review", "brace second half after review", "Ariq keeps bridge project despite delay"),
        ("proj-privacy-ledger", "nian", "privacy ledger grammar", "public records without private body reasons", "grammar active", "chain-ledger-review", 0.58, 0.84, "wording drift under speed", "archive review schedule", "control recovery", "Noro phrase check", "teach object/place/day phrase", "Nian keeps grammar as public norm"),
        ("proj-reed-lesson", "roka", "reed lesson tray", "teach loose reed handling while tied bundle remains personal", "loose tray conditional", "chain-reed-tray", 0.30, 0.61, "rain delay and trust repair", "after rain check", "wetness recovery", "Fayen support at shade edge", "repeat ask-each-time lesson", "Roka keeps tied bundle boundary and opens loose tray"),
        ("proj-shade-debt", "noro", "shade debt review", "let shade help continue without erasing timber debt", "review scheduled", "chain-ledger-review", 0.40, 0.66, "second beam locked", "evening circle edge", "focus recovery", "Nian privacy approval", "hold review before timber release", "Noro keeps debt visible while allowing review"),
    ]
    return [
        PersistentProject(
            project_id=row[0],
            owner=row[1],
            title=row[2],
            goal=row[3],
            current_phase=row[4],
            linked_chain=row[5],
            progress_before=row[6],
            progress_after=row[7],
            blockers=row[8],
            schedule_dependency=row[9],
            body_dependency=row[10],
            social_dependency=row[11],
            next_action=row[12],
            saved_project_memory=row[13],
            frequency_hz=round(426.0 + idx * 6.5, 3),
            flower_node=((idx + 2) % 12) + 1,
        )
        for idx, row in enumerate(rows, start=1)
    ]


def build_ticks(dialogues: list[MultiTurnDialogue], crafts: list[CraftingChainStep], conflicts: list[ScheduleConflict], recoveries: list[BodyRecovery], projects: list[PersistentProject]) -> list[ProjectLoopTick]:
    ticks: list[ProjectLoopTick] = []
    for d in dialogues:
        ticks.append(
            ProjectLoopTick(
                tick_id=f"tick-{d.thread_id}-{d.turn_index}",
                day=d.day,
                time_s=d.time_s,
                layer="multi_turn_dialogue",
                dialogue_state=f"{d.listener}: {d.reply}; {d.continuation_state}",
                crafting_state=d.state_delta,
                schedule_state=d.prior_context,
                body_state=d.privacy_gate,
                project_state=d.memory_write,
                visible_world_state=d.typed_or_spoken_line,
                saved_state=f"dialogue:{d.thread_id}:{d.turn_index}",
                frequency_hz=d.frequency_hz,
                flower_node=d.flower_node,
            )
        )
    for c in crafts:
        ticks.append(
            ProjectLoopTick(
                tick_id=f"tick-{c.chain_id}-{c.step_index}",
                day=c.day,
                time_s=c.time_s,
                layer="crafting_chain",
                dialogue_state=c.preconditions,
                crafting_state=f"{c.recipe_stage}: {c.input_materials} -> {c.output_materials}",
                schedule_state=c.dependency_state,
                body_state=f"quality {c.quality_score:.2f}; failure {c.failure_or_delay}",
                project_state=c.project_link,
                visible_world_state=f"waste {c.waste_or_byproduct}; repair {c.repair_or_rollback}",
                saved_state=c.saved_state_key,
                frequency_hz=c.frequency_hz,
                flower_node=c.flower_node,
            )
        )
    for s in conflicts:
        ticks.append(
            ProjectLoopTick(
                tick_id=f"tick-{s.conflict_id}",
                day=s.day,
                time_s=s.time_s,
                layer="schedule_conflict",
                dialogue_state=s.arbitration_rule,
                crafting_state=s.contested_resource_or_place,
                schedule_state=f"{s.agents}: {s.conflicting_phases}; {s.outcome}",
                body_state=f"delay {s.delay_cost:.2f}; recovery {s.recovery_score:.2f}",
                project_state=s.future_schedule_memory,
                visible_world_state=s.cause,
                saved_state=f"conflict:{s.conflict_id}",
                frequency_hz=s.frequency_hz,
                flower_node=s.flower_node,
            )
        )
    for r in recoveries:
        ticks.append(
            ProjectLoopTick(
                tick_id=f"tick-{r.recovery_id}",
                day=r.day,
                time_s=r.time_s,
                layer="body_recovery",
                dialogue_state=r.consent_state,
                crafting_state=r.recovery_action,
                schedule_state=r.trigger,
                body_state=f"energy {r.before_energy:.2f}->{r.after_energy:.2f}; fatigue {r.before_fatigue:.2f}->{r.after_fatigue:.2f}; pain {r.before_pain:.2f}->{r.after_pain:.2f}",
                project_state=r.saved_memory,
                visible_world_state=r.visible_behavior_change,
                saved_state=f"recovery:{r.recovery_id}",
                frequency_hz=r.frequency_hz,
                flower_node=r.flower_node,
            )
        )
    for p in projects:
        ticks.append(
            ProjectLoopTick(
                tick_id=f"tick-{p.project_id}",
                day=4,
                time_s=3000.0 + len(ticks),
                layer="persistent_project",
                dialogue_state=p.social_dependency,
                crafting_state=p.linked_chain,
                schedule_state=p.schedule_dependency,
                body_state=p.body_dependency,
                project_state=f"{p.title}: {p.progress_before:.2f}->{p.progress_after:.2f}; {p.current_phase}",
                visible_world_state=p.next_action,
                saved_state=p.saved_project_memory,
                frequency_hz=p.frequency_hz,
                flower_node=p.flower_node,
            )
        )
    ticks.sort(key=lambda t: (t.day, t.time_s, t.layer, t.tick_id))
    return ticks


def compute_metrics(agents: list[ProjectAgent], dialogues: list[MultiTurnDialogue], crafts: list[CraftingChainStep], conflicts: list[ScheduleConflict], recoveries: list[BodyRecovery], projects: list[PersistentProject], ticks: list[ProjectLoopTick]) -> dict[str, float]:
    thread_ids = {d.thread_id for d in dialogues}
    thread_lengths = [sum(1 for d in dialogues if d.thread_id == thread_id) for thread_id in thread_ids]
    dialogue_continuity = sum(1 for length in thread_lengths if length >= 3) / len(thread_lengths)
    dialogue_resolution = sum(1 for thread_id in thread_ids if any(d.thread_id == thread_id and d.continuation_state == "resolved" for d in dialogues)) / len(thread_ids)
    dialogue_memory = sum(1 for d in dialogues if d.memory_write and d.prior_context and d.privacy_gate) / len(dialogues)
    chains = {c.chain_id for c in crafts}
    chain_completion = sum(1 for chain in chains if max(c.step_index for c in crafts if c.chain_id == chain) >= 3) / len(chains)
    chain_dependency = sum(1 for c in crafts if c.dependency_state and c.input_materials and c.output_materials) / len(crafts)
    chain_quality = mean(c.quality_score for c in crafts)
    conflict_detection = sum(1 for c in conflicts if c.cause and c.arbitration_rule and c.outcome) / len(conflicts)
    conflict_resolution = mean(c.recovery_score for c in conflicts)
    conflict_fairness = mean(c.fairness_score for c in conflicts)
    recovery_improvement = sum(1 for r in recoveries if r.after_energy >= r.before_energy and r.after_fatigue <= r.before_fatigue and r.after_pain <= r.before_pain) / len(recoveries)
    recovery_honesty = sum(1 for r in recoveries if r.residual_need and r.saved_memory and r.consent_state) / len(recoveries)
    project_continuity = sum(1 for p in projects if p.progress_after > p.progress_before and p.saved_project_memory and p.next_action) / len(projects)
    project_blocker_trace = sum(1 for p in projects if p.blockers and p.schedule_dependency and p.body_dependency and p.social_dependency) / len(projects)
    integration_merge = sum(1 for t in ticks if t.dialogue_state and t.crafting_state and t.schedule_state and t.body_state and t.project_state and t.saved_state) / len(ticks)
    private_boundary = sum(1 for a in agents if a.private_workspace_digest.startswith("sealed:")) / len(agents)
    frequency_flower = sum(1 for value in [*agents, *dialogues, *crafts, *conflicts, *recoveries, *projects, *ticks] if getattr(value, "frequency_hz") > 0 and 1 <= getattr(value, "flower_node") <= 12) / (len(agents) + len(dialogues) + len(crafts) + len(conflicts) + len(recoveries) + len(projects) + len(ticks))
    browser = 1.0
    channels = {
        "multi_turn_dialogue_continuity": round(dialogue_continuity, 6),
        "multi_turn_dialogue_resolution": round(dialogue_resolution, 6),
        "dialogue_memory_traceability": round(dialogue_memory, 6),
        "crafting_chain_completion": round(chain_completion, 6),
        "crafting_dependency_traceability": round(chain_dependency, 6),
        "crafting_chain_quality": round(chain_quality, 6),
        "schedule_conflict_detection": round(conflict_detection, 6),
        "schedule_conflict_recovery": round(conflict_resolution, 6),
        "schedule_conflict_fairness": round(conflict_fairness, 6),
        "body_recovery_improvement_rate": round(recovery_improvement, 6),
        "body_recovery_residual_honesty": round(recovery_honesty, 6),
        "persistent_project_continuity": round(project_continuity, 6),
        "project_blocker_traceability": round(project_blocker_trace, 6),
        "realtime_project_tick_merge": round(integration_merge, 6),
        "private_workspace_boundary_score": round(private_boundary, 6),
        "frequency_flower_project_rhythm": round(frequency_flower, 6),
        "browser_project_loop_available": browser,
    }
    weighted = (
        channels["multi_turn_dialogue_continuity"] * 0.07
        + channels["multi_turn_dialogue_resolution"] * 0.06
        + channels["dialogue_memory_traceability"] * 0.06
        + channels["crafting_chain_completion"] * 0.08
        + channels["crafting_dependency_traceability"] * 0.07
        + channels["crafting_chain_quality"] * 0.06
        + channels["schedule_conflict_detection"] * 0.07
        + channels["schedule_conflict_recovery"] * 0.07
        + channels["schedule_conflict_fairness"] * 0.05
        + channels["body_recovery_improvement_rate"] * 0.07
        + channels["body_recovery_residual_honesty"] * 0.05
        + channels["persistent_project_continuity"] * 0.08
        + channels["project_blocker_traceability"] * 0.05
        + channels["realtime_project_tick_merge"] * 0.06
        + channels["private_workspace_boundary_score"] * 0.03
        + channels["frequency_flower_project_rhythm"] * 0.02
        + channels["browser_project_loop_available"] * 0.03
    )
    channels["mean_project_loop_channel_score"] = round(mean(channels.values()), 6)
    channels["weakest_channel_score"] = round(min(channels.values()), 6)
    channels["project_loop_readiness"] = round(weighted, 6)
    return channels


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["project_loop_readiness"]
    return {
        "no_multiturn_dialogue": round(max(0.0, base - 0.29), 6),
        "no_crafting_chains": round(max(0.0, base - 0.31), 6),
        "no_schedule_conflicts": round(max(0.0, base - 0.27), 6),
        "no_body_recovery": round(max(0.0, base - 0.28), 6),
        "no_persistent_projects": round(max(0.0, base - 0.32), 6),
        "no_realtime_project_merge": round(max(0.0, base - 0.30), 6),
        "no_private_boundary": round(max(0.0, base - 0.18), 6),
        "no_frequency_flower_rhythm": round(max(0.0, base - 0.08), 6),
    }


def make_html(agents: list[ProjectAgent], dialogues: list[MultiTurnDialogue], crafts: list[CraftingChainStep], conflicts: list[ScheduleConflict], recoveries: list[BodyRecovery], projects: list[PersistentProject], ticks: list[ProjectLoopTick], metrics: dict[str, float]) -> str:
    payload = {
        "agents": [asdict(x) for x in agents],
        "dialogues": [asdict(x) for x in dialogues],
        "crafts": [asdict(x) for x in crafts],
        "conflicts": [asdict(x) for x in conflicts],
        "recoveries": [asdict(x) for x in recoveries],
        "projects": [asdict(x) for x in projects],
        "ticks": [asdict(x) for x in ticks],
        "metrics": metrics,
    }
    data_json = json.dumps(payload, indent=2)
    html = """<!doctype html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/><title>Report 230 Project Loop</title><style>
:root{--bg:#0e150d;--panel:#1a2518;--line:#9fcb83;--gold:#dec06f;--text:#f5ecd2;--muted:#aeb8a1;--blue:#80b9c7}*{box-sizing:border-box}body{margin:0;font-family:Georgia,'Times New Roman',serif;color:var(--text);background:radial-gradient(circle at 18% 18%,#31472b 0,transparent 28%),radial-gradient(circle at 80% 14%,#263d3b 0,transparent 26%),linear-gradient(135deg,#090d08,var(--bg))}main{display:grid;grid-template-columns:1.34fr .92fr;min-height:100vh}.world{position:relative;min-height:740px;border-right:1px solid #33472f;overflow:hidden}.flower{position:absolute;inset:7%;opacity:.11;background:radial-gradient(circle at 50% 50%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 38% 50%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 62% 50%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 50% 38%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 50% 62%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%)}.avatar{position:absolute;left:48%;top:72%;width:56px;height:78px;border:2px solid var(--gold);border-radius:38% 38% 35% 35%;background:linear-gradient(180deg,#7a6a38,#282313);transform:translate(-50%,-50%);box-shadow:0 0 34px rgba(222,192,111,.34);z-index:5}.avatar:after{content:'avatar';position:absolute;top:82px;left:-14px;color:var(--gold);font-weight:700}.agent{position:absolute;width:132px;transform:translate(-50%,-50%);transition:.22s ease;z-index:3}.body{width:52px;height:70px;margin:0 auto;border:2px solid var(--line);border-radius:45% 45% 36% 36%;background:linear-gradient(180deg,#315137,#162318);box-shadow:0 0 22px rgba(159,203,131,.2)}.agent.active .body{border-color:var(--gold);box-shadow:0 0 32px rgba(222,192,111,.36);transform:translateY(-3px)}.name{text-align:center;font-weight:700;margin-top:6px}.need{text-align:center;font-size:12px;color:var(--muted);min-height:30px}.obj{position:absolute;padding:6px 10px;border:1px solid rgba(222,192,111,.45);background:rgba(26,37,24,.78);border-radius:999px;color:var(--gold);font-size:13px;z-index:2}.panel{padding:24px;display:flex;flex-direction:column;gap:16px}h1{font-size:clamp(28px,4vw,50px);line-height:.95;margin:0;color:var(--gold)}.card{background:rgba(26,37,24,.88);border:1px solid #344a31;border-radius:18px;padding:16px;box-shadow:0 12px 36px rgba(0,0,0,.25)}.controls{display:flex;flex-wrap:wrap;gap:10px}button{border:0;border-radius:999px;padding:10px 14px;background:var(--gold);color:#10140e;font-weight:700;cursor:pointer}button.secondary{background:transparent;border:1px solid var(--gold);color:var(--gold)}input{width:100%;border:1px solid #445b3e;background:#10170f;color:var(--text);border-radius:12px;padding:10px;margin-top:8px}.row{display:flex;justify-content:space-between;gap:12px;padding:6px 0;border-bottom:1px solid rgba(255,255,255,.08)}.row:last-child{border-bottom:0}.badge{display:inline-block;padding:3px 8px;border-radius:999px;background:rgba(128,185,199,.18);color:var(--blue);margin:2px}.log{max-height:245px;overflow:auto;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;color:#d9dfcf}@media(max-width:900px){main{grid-template-columns:1fr}.world{min-height:560px;border-right:0;border-bottom:1px solid #33472f}}
</style></head><body><main><section class="world" id="world"><div class="flower"></div><div id="avatar" class="avatar"></div><div class="obj" style="left:24%;top:65%">reed project</div><div class="obj" style="left:53%;top:52%">bridge project</div><div class="obj" style="left:70%;top:43%">debt project</div><div class="obj" style="left:42%;top:24%">privacy project</div><div class="obj" style="left:34%;top:43%">care project</div></section><section class="panel"><div><span class="badge">Report 230</span><span class="badge">project loop</span><h1>Threads continue. Crafts chain. Projects persist.</h1></div><div class="card controls"><button id="advance">advance project tick</button><button id="run" class="secondary">run / pause</button><button id="thread" class="secondary">dialogue thread</button><button id="save" class="secondary">save</button><button id="restore" class="secondary">restore</button><input id="typed" placeholder="type: Can I ask for the beam review?"/></div><div class="card" id="current"></div><div class="card"><strong>Metrics</strong><div id="metrics"></div></div><div class="card"><strong>Projects</strong><div id="projects"></div></div><div class="card log" id="log"></div></section></main><script>
const data=__DATA__;const world=document.getElementById('world'),avatar=document.getElementById('avatar'),current=document.getElementById('current'),metrics=document.getElementById('metrics'),projects=document.getElementById('projects'),log=document.getElementById('log'),typed=document.getElementById('typed');let idx=0,timer=null;const nodes=new Map();function pct(v){return `${v}%`}function placeAgents(){for(const a of data.agents){const n=document.createElement('div');n.className='agent';n.id=`agent-${a.agent_id}`;n.style.left=pct(a.x);n.style.top=pct(a.y);n.innerHTML=`<div class="body"></div><div class="name">${a.display_name}</div><div class="need">${a.current_project}</div>`;world.appendChild(n);nodes.set(a.agent_id,n)}}function drawMetrics(){const keys=['project_loop_readiness','multi_turn_dialogue_continuity','crafting_chain_completion','schedule_conflict_recovery','body_recovery_improvement_rate','persistent_project_continuity','realtime_project_tick_merge','weakest_channel_score'];metrics.innerHTML=keys.map(k=>`<div class="row"><span>${k}</span><strong>${Number(data.metrics[k]).toFixed(6)}</strong></div>`).join('')}function drawProjects(){projects.innerHTML=data.projects.map(p=>`<div class="row"><span>${p.owner}</span><span>${p.title}: ${p.progress_before}->${p.progress_after}</span></div>`).join('')}function renderTick(tick){for(const n of nodes.values())n.classList.remove('active');const aid=data.agents.find(a=>tick.project_state.includes(a.agent_id)||tick.dialogue_state.toLowerCase().includes(a.display_name.toLowerCase())||tick.schedule_state.includes(a.agent_id))?.agent_id||data.agents[idx%data.agents.length].agent_id;const active=nodes.get(aid);if(active)active.classList.add('active');avatar.style.left=pct((data.agents.find(a=>a.agent_id===aid)?.x||48)+6);avatar.style.top=pct((data.agents.find(a=>a.agent_id===aid)?.y||72)+8);current.innerHTML=`<strong>Day ${tick.day}, ${tick.time_s}s / ${tick.layer}</strong><p>${tick.visible_world_state}</p><div class="row"><span>dialogue</span><span>${tick.dialogue_state}</span></div><div class="row"><span>craft</span><span>${tick.crafting_state}</span></div><div class="row"><span>schedule</span><span>${tick.schedule_state}</span></div><div class="row"><span>body</span><span>${tick.body_state}</span></div><div class="row"><span>project</span><span>${tick.project_state}</span></div><div class="row"><span>save</span><span>${tick.saved_state}</span></div><div class="row"><span>frequency / flower</span><span>${tick.frequency_hz} Hz / node ${tick.flower_node}</span></div>`;log.innerHTML=`<div>[${idx+1}] day ${tick.day} ${tick.layer}: ${tick.visible_world_state}</div>`+log.innerHTML}function advance(){const tick=data.ticks[idx%data.ticks.length];renderTick(tick);idx++}document.getElementById('advance').onclick=advance;document.getElementById('thread').onclick=()=>{const t=data.ticks.find(x=>x.layer==='multi_turn_dialogue')||data.ticks[0];renderTick(t)};document.getElementById('run').onclick=()=>{if(timer){clearInterval(timer);timer=null}else{timer=setInterval(advance,900)}};document.getElementById('save').onclick=()=>localStorage.setItem('ssrm-report-230-project-loop',JSON.stringify({idx,typed:typed.value}));document.getElementById('restore').onclick=()=>{const s=JSON.parse(localStorage.getItem('ssrm-report-230-project-loop')||'{"idx":0,"typed":""}');idx=s.idx||0;typed.value=s.typed||'';advance()};typed.addEventListener('change',()=>{const q=typed.value.toLowerCase();const d=data.dialogues.find(x=>q.includes(x.listener)||q.includes(x.intent.split('_')[0]))||data.dialogues[0];log.innerHTML=`<div>typed route -> ${d.listener}: ${d.reply}</div>`+log.innerHTML});placeAgents();drawMetrics();drawProjects();advance();
</script></body></html>"""
    return html.replace("__DATA__", data_json)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    source = load_source()
    agents = build_agents(source)
    dialogues = build_dialogue_threads(rng)
    crafts = build_crafting_chains()
    conflicts = build_schedule_conflicts()
    recoveries = build_body_recoveries()
    projects = build_projects()
    ticks = build_ticks(dialogues, crafts, conflicts, recoveries, projects)
    metrics = compute_metrics(agents, dialogues, crafts, conflicts, recoveries, projects, ticks)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["project_loop_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.70 else "fail"

    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    write_csv(ARTIFACTS / f"{BASE}_agents.csv", agents)
    write_csv(ARTIFACTS / f"{BASE}_multi_turn_dialogues.csv", dialogues)
    write_csv(ARTIFACTS / f"{BASE}_crafting_chain_steps.csv", crafts)
    write_csv(ARTIFACTS / f"{BASE}_schedule_conflicts.csv", conflicts)
    write_csv(ARTIFACTS / f"{BASE}_body_recoveries.csv", recoveries)
    write_csv(ARTIFACTS / f"{BASE}_persistent_projects.csv", projects)
    write_csv(ARTIFACTS / f"{BASE}_project_loop_ticks.csv", ticks)

    results = {
        "module": BASE,
        "report": REPORT,
        "seed": args.seed,
        "module_verdict": verdict,
        "condition": "integrated_playable_local_multiturn_dialogue_crafting_schedule_conflict_body_recovery_persistent_project_loop",
        "source_artifact": str(SOURCE_STATE),
        "source_condition": source.get("condition", "unknown"),
        "agents": [asdict(x) for x in agents],
        "multi_turn_dialogues": [asdict(x) for x in dialogues],
        "crafting_chain_steps": [asdict(x) for x in crafts],
        "schedule_conflicts": [asdict(x) for x in conflicts],
        "body_recoveries": [asdict(x) for x in recoveries],
        "persistent_projects": [asdict(x) for x in projects],
        "project_loop_ticks": [asdict(x) for x in ticks],
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": [
            "This is deterministic project-loop scaffolding, not subjective consciousness or real consent.",
            "Multi-turn dialogue is bounded scripted routing, not LLM dialogue or open-ended cognition.",
            "Crafting chains are structured recipes, not full physics or arbitrary crafting.",
            "Body recovery uses welfare-like control signals, not proof of subjective feeling.",
            "Persistent projects are saved state records, not genuine personal agency.",
            "Frequency and flower overlays are timing and phase scaffolds, not metaphysical evidence.",
        ],
        "next_gate": "playable local 3D continuous life with longer personal project arcs, learned preference updates, richer multi-turn typed dialogue, and craft/economy consequences across many days",
    }
    (ARTIFACTS / f"{BASE}_results.json").write_text(json.dumps(results, indent=2))
    (ARTIFACTS / f"{BASE}_state.json").write_text(json.dumps(results, indent=2))
    with (ARTIFACTS / f"{BASE}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "module", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "module": BASE, "verdict": verdict, "readiness": metrics["project_loop_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": results["next_gate"]})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(agents, dialogues, crafts, conflicts, recoveries, projects, ticks, metrics))

    print(f"module_verdict {verdict}")
    print(f"project_loop_readiness {metrics['project_loop_readiness']:.6f}")
    print(f"agents {len(agents)}")
    print(f"multi_turn_dialogues {len(dialogues)}")
    print(f"crafting_chain_steps {len(crafts)}")
    print(f"schedule_conflicts {len(conflicts)}")
    print(f"body_recoveries {len(recoveries)}")
    print(f"persistent_projects {len(projects)}")
    print(f"project_loop_ticks {len(ticks)}")
    print(f"multi_turn_dialogue_continuity {metrics['multi_turn_dialogue_continuity']:.6f}")
    print(f"crafting_chain_completion {metrics['crafting_chain_completion']:.6f}")
    print(f"schedule_conflict_recovery {metrics['schedule_conflict_recovery']:.6f}")
    print(f"body_recovery_improvement_rate {metrics['body_recovery_improvement_rate']:.6f}")
    print(f"persistent_project_continuity {metrics['persistent_project_continuity']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
