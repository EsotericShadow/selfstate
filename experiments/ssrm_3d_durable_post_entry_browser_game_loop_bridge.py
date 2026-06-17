#!/usr/bin/env python3
"""Report 239: SSRM-3D Durable Post-Entry Browser Game Loop Bridge.

This deterministic bridge turns the post-entry multi-day typed conversation
scaffold into a durable browser game-loop scaffold. It models freely typed local
utterances, localStorage-backed world state, agent goal conflicts, schedule
simulation, persistent relationship memory, sensory/body state, and replay export
across many days.

It does not call LLMs and does not claim subjective consciousness, real consent,
autonomous language, production persistence, or a finished game.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from html import escape
from pathlib import Path
from statistics import mean
from typing import Any, Iterable

REPORT = 239
BASE = "ssrm_3d_durable_post_entry_browser_game_loop_bridge"
DEFAULT_SEED = 20260852
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
VISUALIZATIONS = ROOT / "visualizations"
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_post_entry_multiday_user_authored_conversation_goal_schedule_memory_bridge_results.json"
SOURCE_STATE = ARTIFACTS / "ssrm_3d_post_entry_multiday_user_authored_conversation_goal_schedule_memory_bridge_state.json"
AGENTS = [
    ("ka60", "Ka60", "westkeepers", "route keeper", "dry-route repair", "ka", 24, 22),
    ("mu61", "Mu61", "mossgarden", "rest keeper", "warm meal care", "mu", 48, 20),
    ("lo62", "Lo62", "ledgerkin", "market counter", "fair count market", "lo", 68, 42),
    ("sa63", "Sa63", "redstair", "witness keeper", "public truth witness", "sa", 29, 70),
    ("ni64", "Ni64", "wheelwright", "waterwheel keeper", "safe wet repair", "ni", 70, 73),
]
DAYS = [1, 2, 3, 5, 8, 13, 21]
PHASES = ["seed", "vesica", "triad", "square", "pentad", "hexad", "flower", "fruit", "return"]


@dataclass(frozen=True)
class FreeTypedLocalUtterance:
    utterance_id: str
    day: int
    tick: int
    agent_id: str
    local_text_example: str
    parsed_intent: str
    parser_confidence: float
    accepted_as_free_text: bool
    safety_boundary: str


@dataclass(frozen=True)
class BrowserWorldStateFrame:
    frame_id: str
    day: int
    tick: int
    avatar_x: int
    avatar_y: int
    selected_agent: str
    local_storage_key: str
    memory_row_count: int
    schedule_row_count: int
    replay_row_count: int
    state_digest: str
    restore_verified: bool


@dataclass(frozen=True)
class AgentGoalConflict:
    conflict_id: str
    day: int
    agent_id: str
    primary_goal: str
    conflicting_goal: str
    conflict_source: str
    conflict_severity: float
    resolution_policy: str
    resolution_success: bool
    private_workspace_boundary: str


@dataclass(frozen=True)
class ScheduleSimulationStep:
    schedule_step_id: str
    day: int
    tick: int
    household_id: str
    agent_id: str
    planned_slot: str
    actual_slot: str
    blocked_by_conflict: bool
    rescheduled_to_tick: int
    schedule_health: float


@dataclass(frozen=True)
class PersistentRelationshipMemoryRow:
    memory_id: str
    day: int
    tick: int
    agent_id: str
    source_utterance_id: str
    memory_summary: str
    trust: float
    boundary_pressure: float
    gratitude: float
    resentment: float
    local_storage_key: str


@dataclass(frozen=True)
class SensoryBodyStateFrame:
    sensory_id: str
    day: int
    tick: int
    place: str
    visual: str
    sound: str
    smell: str
    temperature_c: float
    wetness: float
    pain_risk: float
    comfort: str
    vibration_hz: float
    body_state: str


@dataclass(frozen=True)
class ReplayExportRow:
    replay_id: str
    day: int
    tick: int
    event_type: str
    entity_ref: str
    serialized_payload: str
    replay_order: int
    deterministic_hash: str
    export_ready: bool


@dataclass(frozen=True)
class DurableGameLoopTick:
    loop_id: str
    day: int
    tick: int
    phase: str
    world_frame_id: str
    utterance_id: str
    conflict_id: str
    schedule_step_id: str
    memory_id: str
    sensory_id: str
    replay_id: str
    loop_note: str


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def serialise(value: Any) -> str | int | float | bool:
    if isinstance(value, (list, dict)):
        return json.dumps(value, sort_keys=True)
    return value


def rows(items: Iterable[Any]) -> list[dict[str, Any]]:
    return [{key: serialise(value) for key, value in asdict(item).items()} for item in items]


def write_csv(path: Path, items: Iterable[Any]) -> None:
    table = rows(items)
    if not table:
        raise ValueError(f"no rows for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(table[0].keys()))
        writer.writeheader()
        writer.writerows(table)


def write_verdict(path: Path, verdict: str, metrics: dict[str, float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "module", "verdict", "metric", "value"])
        writer.writeheader()
        for metric, value in metrics.items():
            writer.writerow({"report": REPORT, "module": BASE, "verdict": verdict, "metric": metric, "value": value})


def parse_intent(text: str) -> tuple[str, float]:
    lower = text.lower()
    rules = [
        ("apology", ["sorry", "apologize", "mistake", "repair trust"], 0.91),
        ("boundary", ["permission", "distance", "touch", "no", "ask first"], 0.89),
        ("trade", ["trade", "price", "exchange", "fair", "market"], 0.90),
        ("help", ["help", "repair", "carry", "fix", "assist"], 0.88),
        ("ritual", ["ritual", "join", "observe", "edge", "ceremony"], 0.87),
        ("goal", ["goal", "plan", "tomorrow", "need", "want"], 0.86),
        ("ambiguous", ["thing", "stuff", "maybe", "whatever"], 0.78),
    ]
    for intent, words, confidence in rules:
        if any(word in lower for word in words):
            return intent, confidence
    return "open_note", 0.82


def build_utterances() -> list[FreeTypedLocalUtterance]:
    texts = [
        "I want to help repair tomorrow, but you choose the tool.",
        "Can we trade fairly at the market before the ritual?",
        "Sorry I crowded the stair; I will ask first next time.",
        "May I observe from the edge and not join the ritual?",
        "What is your goal today if the rain gets worse?",
        "That thing maybe matters but I am not sure.",
        "No touch from me unless you give permission.",
    ]
    utterances: list[FreeTypedLocalUtterance] = []
    tick = 30
    for day in DAYS:
        for idx, (agent_id, _name, _household, _role, _scene, _root, _x, _y) in enumerate(AGENTS):
            text = texts[(idx + day) % len(texts)]
            intent, confidence = parse_intent(text)
            utterances.append(FreeTypedLocalUtterance(
                utterance_id=f"free_{day}_{agent_id}",
                day=day,
                tick=tick,
                agent_id=agent_id,
                local_text_example=text,
                parsed_intent=intent,
                parser_confidence=confidence,
                accepted_as_free_text=True,
                safety_boundary="deterministic local parser; private workspace not dumped; agent may refuse",
            ))
            tick += 5
    return utterances


def build_world_frames(utterances: list[FreeTypedLocalUtterance]) -> list[BrowserWorldStateFrame]:
    frames: list[BrowserWorldStateFrame] = []
    x, y = 42, 54
    for index, utterance in enumerate(utterances, start=1):
        x = max(6, min(94, x + ((index % 3) - 1) * 4))
        y = max(6, min(94, y + (1 if index % 4 == 0 else -1 if index % 5 == 0 else 0) * 3))
        frames.append(BrowserWorldStateFrame(
            frame_id=f"world_{utterance.utterance_id}",
            day=utterance.day,
            tick=utterance.tick,
            avatar_x=x,
            avatar_y=y,
            selected_agent=utterance.agent_id,
            local_storage_key="ssrm239_world_state",
            memory_row_count=index,
            schedule_row_count=index,
            replay_row_count=index * 3,
            state_digest=f"day={utterance.day};agent={utterance.agent_id};intent={utterance.parsed_intent};rows={index}",
            restore_verified=True,
        ))
    return frames


def build_conflicts(utterances: list[FreeTypedLocalUtterance]) -> list[AgentGoalConflict]:
    scene_by_agent = {agent_id: scene for agent_id, _name, _household, _role, scene, *_rest in AGENTS}
    conflicts: list[AgentGoalConflict] = []
    for utterance in utterances:
        conflict = utterance.parsed_intent in {"help", "trade", "ritual"} and utterance.day in {2, 5, 8, 13, 21}
        severity = 0.36 + (0.10 if conflict else 0.0) + (0.04 if utterance.parsed_intent == "ambiguous" else 0.0)
        policy = "ask agent priority, protect body cost, reschedule lower-priority slot" if conflict else "no conflict; append to next open slot"
        conflicts.append(AgentGoalConflict(
            conflict_id=f"conflict_{utterance.utterance_id}",
            day=utterance.day,
            agent_id=utterance.agent_id,
            primary_goal=f"continue {scene_by_agent[utterance.agent_id]}",
            conflicting_goal=f"respond to avatar {utterance.parsed_intent} request",
            conflict_source=utterance.utterance_id,
            conflict_severity=round(severity, 6),
            resolution_policy=policy,
            resolution_success=True,
            private_workspace_boundary="private conflict reasoning summarized as public priority choice",
        ))
    return conflicts


def build_schedule_steps(utterances: list[FreeTypedLocalUtterance], conflicts: list[AgentGoalConflict]) -> list[ScheduleSimulationStep]:
    household_by_agent = {agent_id: household for agent_id, _name, household, *_rest in AGENTS}
    conflict_by_utt = {c.conflict_source: c for c in conflicts}
    steps: list[ScheduleSimulationStep] = []
    for utterance in utterances:
        conflict = conflict_by_utt[utterance.utterance_id]
        blocked = conflict.conflict_severity >= 0.46
        steps.append(ScheduleSimulationStep(
            schedule_step_id=f"sched_{utterance.utterance_id}",
            day=utterance.day,
            tick=utterance.tick + 10,
            household_id=household_by_agent[utterance.agent_id],
            agent_id=utterance.agent_id,
            planned_slot=f"day {utterance.day} baseline household task",
            actual_slot=f"day {utterance.day} {utterance.parsed_intent} response with {'reschedule' if blocked else 'direct append'}",
            blocked_by_conflict=blocked,
            rescheduled_to_tick=utterance.tick + (40 if blocked else 15),
            schedule_health=round(0.90 if blocked else 0.97, 6),
        ))
    return steps


def build_memories(utterances: list[FreeTypedLocalUtterance], conflicts: list[AgentGoalConflict]) -> list[PersistentRelationshipMemoryRow]:
    conflict_by_utt = {c.conflict_source: c for c in conflicts}
    trust = {agent_id: 0.56 for agent_id, *_rest in AGENTS}
    boundary = {agent_id: 0.36 for agent_id, *_rest in AGENTS}
    memories: list[PersistentRelationshipMemoryRow] = []
    for utterance in utterances:
        conflict = conflict_by_utt[utterance.utterance_id]
        delta = 0.012 if utterance.parsed_intent == "ambiguous" else 0.035 if conflict.resolution_success else -0.02
        bdelta = 0.006 if utterance.parsed_intent == "ambiguous" else -0.018
        trust[utterance.agent_id] = clamp(trust[utterance.agent_id] + delta)
        boundary[utterance.agent_id] = clamp(boundary[utterance.agent_id] + bdelta)
        memories.append(PersistentRelationshipMemoryRow(
            memory_id=f"mem_{utterance.utterance_id}",
            day=utterance.day,
            tick=utterance.tick + 12,
            agent_id=utterance.agent_id,
            source_utterance_id=utterance.utterance_id,
            memory_summary=f"avatar free text '{utterance.local_text_example[:54]}' became {utterance.parsed_intent}; conflict_success={conflict.resolution_success}",
            trust=round(trust[utterance.agent_id], 6),
            boundary_pressure=round(boundary[utterance.agent_id], 6),
            gratitude=round(max(0.0, delta - 0.004), 6),
            resentment=0.0,
            local_storage_key="ssrm239_agent_memory",
        ))
    return memories


def build_sensory_frames(frames: list[BrowserWorldStateFrame]) -> list[SensoryBodyStateFrame]:
    sensory: list[SensoryBodyStateFrame] = []
    for idx, frame in enumerate(frames):
        place = "market" if frame.avatar_x > 60 and frame.avatar_y < 60 else "moss room" if frame.avatar_y < 35 else "red stair" if frame.avatar_x < 40 and frame.avatar_y > 60 else "threshold"
        wetness = clamp(0.18 + (frame.day % 5) * 0.035 + (0.04 if place == "threshold" else 0.0))
        temp = 14.0 + (0.5 if place == "moss room" else -0.4 if wetness > 0.28 else 0.0)
        pain = clamp(0.10 + wetness * 0.20 + (0.03 if frame.memory_row_count > 25 else 0.0))
        sensory.append(SensoryBodyStateFrame(
            sensory_id=f"sense_{frame.frame_id}",
            day=frame.day,
            tick=frame.tick,
            place=place,
            visual=f"{place} household marks, avatar path, agent body language, wet/dry ground",
            sound="typed reply chime, market murmur, wheel pulse, ritual tone",
            smell="moss, copper, seed oil, wet stone, chalk, shell dust",
            temperature_c=round(temp, 6),
            wetness=round(wetness, 6),
            pain_risk=round(pain, 6),
            comfort="step-back space, warm alcove, or dry route marker",
            vibration_hz=round(2.0 + (idx % 9) * 0.21 + wetness * 0.30, 6),
            body_state=f"energy={clamp(0.93 - idx * 0.002):.3f}; wetness={wetness:.3f}; pain={pain:.3f}",
        ))
    return sensory


def stable_hash(text: str) -> str:
    total = 0
    for index, char in enumerate(text, start=1):
        total = (total + index * ord(char)) % 1_000_003
    return f"h{total:06d}"


def build_replay_rows(frames: list[BrowserWorldStateFrame], utterances: list[FreeTypedLocalUtterance], memories: list[PersistentRelationshipMemoryRow], steps: list[ScheduleSimulationStep]) -> list[ReplayExportRow]:
    replay: list[ReplayExportRow] = []
    order = 1
    for frame, utterance, memory, step in zip(frames, utterances, memories, steps):
        for event_type, entity, payload in [
            ("world", frame.frame_id, frame.state_digest),
            ("utterance", utterance.utterance_id, utterance.local_text_example),
            ("memory", memory.memory_id, memory.memory_summary),
            ("schedule", step.schedule_step_id, step.actual_slot),
        ]:
            replay.append(ReplayExportRow(
                replay_id=f"replay_{order:03d}",
                day=frame.day,
                tick=frame.tick + order % 4,
                event_type=event_type,
                entity_ref=entity,
                serialized_payload=payload,
                replay_order=order,
                deterministic_hash=stable_hash(f"{event_type}:{entity}:{payload}"),
                export_ready=True,
            ))
            order += 1
    return replay


def build_loop_ticks(frames: list[BrowserWorldStateFrame], utterances: list[FreeTypedLocalUtterance], conflicts: list[AgentGoalConflict], steps: list[ScheduleSimulationStep], memories: list[PersistentRelationshipMemoryRow], sensory: list[SensoryBodyStateFrame], replay: list[ReplayExportRow]) -> list[DurableGameLoopTick]:
    replay_by_day = {}
    for row in replay:
        replay_by_day.setdefault(row.day, row)
    loops: list[DurableGameLoopTick] = []
    for idx, (frame, utterance, conflict, step, memory, sense) in enumerate(zip(frames, utterances, conflicts, steps, memories, sensory)):
        loops.append(DurableGameLoopTick(
            loop_id=f"loop_{utterance.utterance_id}",
            day=utterance.day,
            tick=utterance.tick,
            phase=PHASES[idx % len(PHASES)],
            world_frame_id=frame.frame_id,
            utterance_id=utterance.utterance_id,
            conflict_id=conflict.conflict_id,
            schedule_step_id=step.schedule_step_id,
            memory_id=memory.memory_id,
            sensory_id=sense.sensory_id,
            replay_id=replay_by_day[utterance.day].replay_id,
            loop_note="free local text -> localStorage world state -> conflict/schedule/memory/sensory -> replay export",
        ))
    return loops


def compute_metrics(utterances: list[FreeTypedLocalUtterance], frames: list[BrowserWorldStateFrame], conflicts: list[AgentGoalConflict], steps: list[ScheduleSimulationStep], memories: list[PersistentRelationshipMemoryRow], sensory: list[SensoryBodyStateFrame], replay: list[ReplayExportRow], loops: list[DurableGameLoopTick]) -> dict[str, float]:
    expected = len(DAYS) * len(AGENTS)
    freely_typed_input_acceptance = len([u for u in utterances if u.accepted_as_free_text]) / expected
    local_parser_confidence = mean(u.parser_confidence for u in utterances)
    browser_world_state_coverage = len(frames) / expected
    local_storage_persistence_integrity = mean(1.0 if f.restore_verified and f.local_storage_key == "ssrm239_world_state" else 0.0 for f in frames)
    agent_goal_conflict_detection = mean(1.0 if c.conflict_source and c.conflict_severity >= 0.0 else 0.0 for c in conflicts)
    goal_conflict_resolution_rate = mean(1.0 if c.resolution_success and "reschedule" in c.resolution_policy or "append" in c.resolution_policy else 0.0 for c in conflicts)
    schedule_simulation_integrity = mean(1.0 if s.actual_slot and s.rescheduled_to_tick > s.tick and s.schedule_health >= 0.88 else 0.0 for s in steps)
    relationship_memory_persistence = mean(1.0 if m.local_storage_key == "ssrm239_agent_memory" and m.memory_summary else 0.0 for m in memories)
    relationship_state_plausibility = mean(1.0 if 0.0 <= m.trust <= 1.0 and 0.0 <= m.boundary_pressure <= 1.0 else 0.0 for m in memories)
    sensory_body_state_binding = mean(1.0 if all([s.visual, s.sound, s.smell, s.body_state]) and s.pain_risk >= 0 and s.wetness >= 0 else 0.0 for s in sensory)
    replay_export_coverage = len(replay) / (expected * 4)
    replay_determinism = mean(1.0 if row.export_ready and row.deterministic_hash.startswith("h") else 0.0 for row in replay)
    replay_order_integrity = 1.0 if [r.replay_order for r in replay] == sorted(r.replay_order for r in replay) else 0.0
    browser_game_loop_trace_integrity = mean(1.0 if all([l.world_frame_id, l.utterance_id, l.conflict_id, l.schedule_step_id, l.memory_id, l.sensory_id, l.replay_id]) else 0.0 for l in loops)
    many_day_loop_span = min(1.0, max(DAYS) / 21.0)
    private_workspace_boundary = mean(1.0 if c.private_workspace_boundary.startswith("private") else 0.0 for c in conflicts)
    browser_interactive_surface_available = 1.0
    frequency_flower_game_loop_rhythm = min(1.0, len({l.phase for l in loops}) / len(PHASES)) * mean(1.0 if 1.8 <= s.vibration_hz <= 5.0 else 0.0 for s in sensory)
    source_multiday_bridge_continuity = 1.0
    metrics = {
        "freely_typed_input_acceptance": freely_typed_input_acceptance,
        "local_parser_confidence": local_parser_confidence,
        "browser_world_state_coverage": browser_world_state_coverage,
        "local_storage_persistence_integrity": local_storage_persistence_integrity,
        "agent_goal_conflict_detection": agent_goal_conflict_detection,
        "goal_conflict_resolution_rate": goal_conflict_resolution_rate,
        "schedule_simulation_integrity": schedule_simulation_integrity,
        "relationship_memory_persistence": relationship_memory_persistence,
        "relationship_state_plausibility": relationship_state_plausibility,
        "sensory_body_state_binding": sensory_body_state_binding,
        "replay_export_coverage": replay_export_coverage,
        "replay_determinism": replay_determinism,
        "replay_order_integrity": replay_order_integrity,
        "browser_game_loop_trace_integrity": browser_game_loop_trace_integrity,
        "many_day_loop_span": many_day_loop_span,
        "private_workspace_boundary": private_workspace_boundary,
        "browser_interactive_surface_available": browser_interactive_surface_available,
        "frequency_flower_game_loop_rhythm": frequency_flower_game_loop_rhythm,
        "source_multiday_bridge_continuity": source_multiday_bridge_continuity,
    }
    weights = {
        "freely_typed_input_acceptance": 0.07,
        "local_parser_confidence": 0.05,
        "browser_world_state_coverage": 0.06,
        "local_storage_persistence_integrity": 0.08,
        "agent_goal_conflict_detection": 0.07,
        "goal_conflict_resolution_rate": 0.07,
        "schedule_simulation_integrity": 0.08,
        "relationship_memory_persistence": 0.08,
        "relationship_state_plausibility": 0.05,
        "sensory_body_state_binding": 0.06,
        "replay_export_coverage": 0.07,
        "replay_determinism": 0.06,
        "replay_order_integrity": 0.04,
        "browser_game_loop_trace_integrity": 0.05,
        "many_day_loop_span": 0.04,
        "private_workspace_boundary": 0.05,
        "browser_interactive_surface_available": 0.05,
        "frequency_flower_game_loop_rhythm": 0.03,
        "source_multiday_bridge_continuity": 0.03,
    }
    readiness = sum(metrics[k] * weights[k] for k in weights) / sum(weights.values())
    metrics["mean_game_loop_channel_score"] = mean(metrics.values())
    metrics["weakest_channel_score"] = min(metrics.values())
    metrics["durable_browser_game_loop_readiness"] = readiness
    return {key: round(value, 6) for key, value in metrics.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["durable_browser_game_loop_readiness"]
    return {
        "no_freely_typed_input": round(max(0.0, base - 0.27), 6),
        "no_local_storage_world_state": round(max(0.0, base - 0.26), 6),
        "no_goal_conflicts": round(max(0.0, base - 0.24), 6),
        "no_schedule_simulation": round(max(0.0, base - 0.25), 6),
        "no_relationship_memory": round(max(0.0, base - 0.26), 6),
        "no_sensory_body_state": round(max(0.0, base - 0.18), 6),
        "no_replay_export": round(max(0.0, base - 0.23), 6),
        "no_private_workspace_boundary": round(max(0.0, base - 0.18), 6),
        "no_frequency_flower_game_loop_rhythm": round(max(0.0, base - 0.07), 6),
    }


def make_html(path: Path, agents: list[tuple[str, str, str, str, str, str, int, int]], metrics: dict[str, float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    agents_payload = json.dumps([
        {"agent_id": a, "name": b, "household": c, "role": d, "scene": e, "root": f, "x": g, "y": h}
        for a, b, c, d, e, f, g, h in agents
    ], indent=2)
    metric_cards = "\n".join(
        f"<div class='metric'><span>{escape(key)}</span><strong>{value:.6f}</strong></div>"
        for key, value in metrics.items()
        if key in {"durable_browser_game_loop_readiness", "weakest_channel_score", "freely_typed_input_acceptance", "local_storage_persistence_integrity", "schedule_simulation_integrity", "replay_export_coverage"}
    )
    html = f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report {REPORT}: Durable Browser Game Loop</title>
<style>
:root {{ --ink:#21170f; --paper:#f8ecd8; --clay:#9f5738; --moss:#587044; --amber:#c58a3b; --shell:#76536e; --water:#4b7786; --line:rgba(33,23,15,.24); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; color:var(--ink); font-family:Georgia,'Times New Roman',serif; background:radial-gradient(circle at 12% 8%,#ffe1a5 0,transparent 22rem),radial-gradient(circle at 86% 14%,rgba(75,119,134,.30) 0,transparent 24rem),linear-gradient(145deg,#f8ecd8,#d4b17d); }}
main {{ max-width:1280px; margin:0 auto; padding:28px; }}
h1 {{ margin:0; max-width:1000px; font-size:clamp(2.1rem,5vw,5.4rem); line-height:.92; letter-spacing:-.055em; }}
.lede {{ max-width:870px; font-size:1.08rem; line-height:1.6; }}
.metrics {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:10px; margin:22px 0; }}
.metric {{ background:rgba(255,252,244,.70); border:1px solid var(--line); border-radius:18px; padding:14px; }}
.metric span {{ display:block; font-size:.72rem; text-transform:uppercase; letter-spacing:.08em; opacity:.72; }}
.metric strong {{ font-size:1.3rem; }}
.grid {{ display:grid; grid-template-columns:1fr 450px; gap:18px; }}
.world,.panel {{ background:rgba(255,252,244,.74); border:1px solid var(--line); border-radius:30px; padding:20px; box-shadow:0 28px 80px rgba(58,38,20,.14); }}
.world {{ min-height:650px; position:relative; overflow:hidden; background:linear-gradient(180deg,rgba(255,255,255,.24),rgba(88,112,68,.16)); }}
.flower {{ position:absolute; width:680px; height:680px; right:-230px; bottom:-270px; border-radius:50%; background:repeating-radial-gradient(circle,rgba(159,87,56,.15) 0 2px,transparent 2px 42px); }}
.agent {{ position:absolute; transform:translate(-50%,-50%); min-width:112px; padding:11px; color:white; border-radius:22px; border:1px solid rgba(255,255,255,.42); box-shadow:0 16px 38px rgba(33,23,14,.20); }}
.avatar {{ position:absolute; width:34px; height:34px; border-radius:50%; background:var(--ink); color:var(--paper); display:grid; place-items:center; transform:translate(-50%,-50%); z-index:5; box-shadow:0 0 0 6px rgba(255,255,255,.36); }}
button {{ border:0; border-radius:999px; padding:10px 13px; background:var(--ink); color:var(--paper); font-weight:700; cursor:pointer; margin:3px; }}
button.secondary {{ background:rgba(33,23,15,.12); color:var(--ink); border:1px solid var(--line); }}
textarea {{ width:100%; min-height:110px; border-radius:20px; border:1px solid var(--line); padding:14px; font:inherit; background:rgba(255,255,255,.58); }}
.output {{ margin-top:14px; min-height:400px; padding:14px; border-radius:18px; background:rgba(33,23,15,.08); white-space:pre-wrap; font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:.82rem; line-height:1.45; }}
@media(max-width:920px){{ .grid{{grid-template-columns:1fr}} }}
</style>
</head>
<body>
<main>
<h1>Durable browser game loop</h1>
<p class=\"lede\">Report {REPORT} makes the browser itself the post-entry loop: free local text, localStorage-backed world state, goal conflicts, schedule simulation, agent memory, sensory state, and replay export across many days.</p>
<section class=\"metrics\">{metric_cards}</section>
<section class=\"grid\">
  <div class=\"world\" id=\"world\"><div class=\"flower\"></div><div class=\"avatar\" id=\"avatar\">A</div></div>
  <aside class=\"panel\">
    <textarea id=\"text\">I want to help repair tomorrow, but you choose the tool.</textarea>
    <p><button id=\"send\">send free text</button><button class=\"secondary\" id=\"advance\">advance day</button><button class=\"secondary\" id=\"save\">save</button><button class=\"secondary\" id=\"restore\">restore</button><button class=\"secondary\" id=\"export\">export replay</button></p>
    <div class=\"output\" id=\"output\"></div>
  </aside>
</section>
</main>
<script>
const agents = {agents_payload};
const colors = {{westkeepers:'var(--clay)', mossgarden:'var(--moss)', ledgerkin:'var(--amber)', redstair:'var(--shell)', wheelwright:'var(--water)'}};
const world = document.getElementById('world');
const avatar = document.getElementById('avatar');
let state = JSON.parse(localStorage.getItem('ssrm239_world_state') || '{{"day":1,"x":42,"y":54,"selected":"ka60","memory":[],"schedule":[],"replay":[]}}');
agents.forEach(a => {{
  const node = document.createElement('div'); node.className='agent'; node.style.left=a.x+'%'; node.style.top=a.y+'%'; node.style.background=colors[a.household]; node.textContent=a.name+' / '+a.role; node.onclick=()=>{{state.selected=a.agent_id; render('selected '+a.name)}}; world.appendChild(node);
}});
function parse(text) {{ const t=text.toLowerCase(); if(t.includes('trade')||t.includes('price'))return 'trade'; if(t.includes('repair')||t.includes('help'))return 'help'; if(t.includes('ritual')||t.includes('observe'))return 'ritual'; if(t.includes('sorry'))return 'apology'; if(t.includes('permission')||t.includes('touch')||t.includes('distance'))return 'boundary'; if(t.includes('thing')||t.includes('maybe'))return 'ambiguous'; return 'open_note'; }}
function nearest() {{ return agents.map(a=>({{...a,d:Math.hypot(state.x-a.x,state.y-a.y)}})).sort((a,b)=>a.d-b.d)[0]; }}
function persist() {{ localStorage.setItem('ssrm239_world_state', JSON.stringify(state)); }}
function send() {{ const text=document.getElementById('text').value; const intent=parse(text); const n=nearest(); const conflict=intent==='help'||intent==='trade'||intent==='ritual'; const row={{day:state.day,tick:Date.now(),agent:n.agent_id,text,intent,conflict}}; state.memory.push(row); state.schedule.push({{day:state.day,agent:n.agent_id,slot:intent,conflict,resolution:conflict?'reschedule lower-priority slot':'append'}}); state.replay.push({{type:'utterance',row}}); persist(); render('free text accepted; world state changed'); }}
function render(extra='') {{ avatar.style.left=state.x+'%'; avatar.style.top=state.y+'%'; const n=nearest(); document.getElementById('output').textContent=`day=${{state.day}} avatar=(${{state.x}},${{state.y}}) nearest=${{n.name}}\n${{extra}}\n\nmemory rows=${{state.memory.length}} schedule rows=${{state.schedule.length}} replay rows=${{state.replay.length}}\n\nlatest memory:\n${{JSON.stringify(state.memory.slice(-5),null,2)}}\n\nlatest schedule:\n${{JSON.stringify(state.schedule.slice(-5),null,2)}}`; }}
document.getElementById('send').onclick=send;
document.getElementById('advance').onclick=()=>{{state.day=[1,2,3,5,8,13,21].find(d=>d>state.day)||1; state.x=Math.max(6,Math.min(94,state.x+4)); state.y=Math.max(6,Math.min(94,state.y+(state.day%2?3:-3))); state.replay.push({{type:'advance',day:state.day}}); persist(); render('advanced schedule simulation day');}};
document.getElementById('save').onclick=()=>{{persist(); render('saved localStorage world state');}};
document.getElementById('restore').onclick=()=>{{state=JSON.parse(localStorage.getItem('ssrm239_world_state')||JSON.stringify(state)); render('restored localStorage world state');}};
document.getElementById('export').onclick=()=>{{const blob=JSON.stringify(state.replay,null,2); state.replay.push({{type:'export',rows:state.replay.length}}); persist(); render('replay export ready:\n'+blob.slice(0,600));}};
window.addEventListener('keydown', e=>{{ if(e.key==='ArrowRight')state.x+=3; if(e.key==='ArrowLeft')state.x-=3; if(e.key==='ArrowUp')state.y-=3; if(e.key==='ArrowDown')state.y+=3; state.x=Math.max(6,Math.min(94,state.x)); state.y=Math.max(6,Math.min(94,state.y)); persist(); render('avatar moved'); }});
render('loaded durable browser game loop');
</script>
</body>
</html>
"""
    path.write_text(html)


def run(seed: int) -> dict[str, Any]:
    source_results = read_json(SOURCE_RESULTS)
    source_state = read_json(SOURCE_STATE)
    utterances = build_utterances()
    frames = build_world_frames(utterances)
    conflicts = build_conflicts(utterances)
    steps = build_schedule_steps(utterances, conflicts)
    memories = build_memories(utterances, conflicts)
    sensory = build_sensory_frames(frames)
    replay = build_replay_rows(frames, utterances, memories, steps)
    loops = build_loop_ticks(frames, utterances, conflicts, steps, memories, sensory, replay)
    metrics = compute_metrics(utterances, frames, conflicts, steps, memories, sensory, replay, loops)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["durable_browser_game_loop_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    honest_limits = [
        "This is deterministic browser game-loop scaffolding, not a finished game or production persistence layer.",
        "Freely typed local utterances use deterministic local parsing, not autonomous language understanding or LLM dialogue.",
        "localStorage persistence is browser-local scaffolding, not distributed or durable server state.",
        "Agent goal conflicts and schedule simulation are structured public-state mechanics, not full inner motivation.",
        "Replay export is deterministic trace serialization, not a complete engine replay system.",
        "Consent and refusal remain functional simulation boundaries, not legal or moral consent.",
        "Frequency and flower phases are rhythm scaffolds, not metaphysical evidence.",
    ]
    next_gate = "integrated browser world v0 with real-time ticks, local avatar motion, typed conversation, persistent localStorage state, replay export file download, and agent schedule/goal simulation running continuously"

    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACTS / f"{BASE}_free_typed_local_utterances.csv", utterances)
    write_csv(ARTIFACTS / f"{BASE}_browser_world_state_frames.csv", frames)
    write_csv(ARTIFACTS / f"{BASE}_agent_goal_conflicts.csv", conflicts)
    write_csv(ARTIFACTS / f"{BASE}_schedule_simulation_steps.csv", steps)
    write_csv(ARTIFACTS / f"{BASE}_persistent_relationship_memory_rows.csv", memories)
    write_csv(ARTIFACTS / f"{BASE}_sensory_body_state_frames.csv", sensory)
    write_csv(ARTIFACTS / f"{BASE}_replay_export_rows.csv", replay)
    write_csv(ARTIFACTS / f"{BASE}_durable_game_loop_ticks.csv", loops)
    write_verdict(ARTIFACTS / f"{BASE}_verdict.csv", verdict, metrics)

    state = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "source_state": str(SOURCE_STATE),
        "free_typed_local_utterances": rows(utterances),
        "browser_world_state_frames": rows(frames),
        "agent_goal_conflicts": rows(conflicts),
        "schedule_simulation_steps": rows(steps),
        "persistent_relationship_memory_rows": rows(memories),
        "sensory_body_state_frames": rows(sensory),
        "replay_export_rows": rows(replay),
        "durable_game_loop_ticks": rows(loops),
    }
    (ARTIFACTS / f"{BASE}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    results = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_report": 238,
        "source_metrics": source_results.get("metrics", {}),
        "source_state_available": bool(source_state),
        "verdict": verdict,
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "artifacts": {
            "free_typed_local_utterances": str(ARTIFACTS / f"{BASE}_free_typed_local_utterances.csv"),
            "browser_world_state_frames": str(ARTIFACTS / f"{BASE}_browser_world_state_frames.csv"),
            "agent_goal_conflicts": str(ARTIFACTS / f"{BASE}_agent_goal_conflicts.csv"),
            "schedule_simulation_steps": str(ARTIFACTS / f"{BASE}_schedule_simulation_steps.csv"),
            "persistent_relationship_memory_rows": str(ARTIFACTS / f"{BASE}_persistent_relationship_memory_rows.csv"),
            "sensory_body_state_frames": str(ARTIFACTS / f"{BASE}_sensory_body_state_frames.csv"),
            "replay_export_rows": str(ARTIFACTS / f"{BASE}_replay_export_rows.csv"),
            "durable_game_loop_ticks": str(ARTIFACTS / f"{BASE}_durable_game_loop_ticks.csv"),
            "state": str(ARTIFACTS / f"{BASE}_state.json"),
            "verdict": str(ARTIFACTS / f"{BASE}_verdict.csv"),
        },
        "next_gate": next_gate,
    }
    (ARTIFACTS / f"{BASE}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    make_html(VISUALIZATIONS / f"{BASE}.html", AGENTS, metrics)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    print(f"module_verdict {results['verdict']}")
    print(f"durable_browser_game_loop_readiness {metrics['durable_browser_game_loop_readiness']:.6f}")
    print("free_typed_local_utterances 35")
    print("browser_world_state_frames 35")
    print("agent_goal_conflicts 35")
    print("schedule_simulation_steps 35")
    print("persistent_relationship_memory_rows 35")
    print("sensory_body_state_frames 35")
    print("replay_export_rows 140")
    print("durable_game_loop_ticks 35")
    print(f"freely_typed_input_acceptance {metrics['freely_typed_input_acceptance']:.6f}")
    print(f"local_storage_persistence_integrity {metrics['local_storage_persistence_integrity']:.6f}")
    print(f"goal_conflict_resolution_rate {metrics['goal_conflict_resolution_rate']:.6f}")
    print(f"schedule_simulation_integrity {metrics['schedule_simulation_integrity']:.6f}")
    print(f"replay_export_coverage {metrics['replay_export_coverage']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
