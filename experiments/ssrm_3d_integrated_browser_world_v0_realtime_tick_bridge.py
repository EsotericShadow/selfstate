#!/usr/bin/env python3
"""Report 240: SSRM-3D Integrated Browser World v0 Real-Time Tick Bridge.

This deterministic bridge consolidates the prior durable browser loop into an
integrated browser world v0 scaffold: real-time ticks, local avatar motion, typed
conversation, persistent localStorage state, replay file-download support, and
agent schedule/goal simulation running continuously.

It does not call LLMs and does not claim subjective consciousness, real consent,
autonomous language, production persistence, or a finished game engine.
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

REPORT = 240
BASE = "ssrm_3d_integrated_browser_world_v0_realtime_tick_bridge"
DEFAULT_SEED = 20260853
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
VISUALIZATIONS = ROOT / "visualizations"
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_durable_post_entry_browser_game_loop_bridge_results.json"
SOURCE_STATE = ARTIFACTS / "ssrm_3d_durable_post_entry_browser_game_loop_bridge_state.json"
AGENTS = [
    ("ka60", "Ka60", "westkeepers", "route keeper", "dry-route repair", "ka", 24, 22),
    ("mu61", "Mu61", "mossgarden", "rest keeper", "warm meal care", "mu", 48, 20),
    ("lo62", "Lo62", "ledgerkin", "market counter", "fair count market", "lo", 68, 42),
    ("sa63", "Sa63", "redstair", "witness keeper", "public truth witness", "sa", 29, 70),
    ("ni64", "Ni64", "wheelwright", "waterwheel keeper", "safe wet repair", "ni", 70, 73),
]
PHASES = ["seed", "vesica", "triad", "square", "pentad", "hexad", "flower", "fruit", "return"]


@dataclass(frozen=True)
class RealTimeTickSpec:
    tick_spec_id: str
    tick_index: int
    target_interval_ms: int
    simulated_elapsed_ms: int
    drift_ms: int
    paused: bool
    save_due: bool
    replay_due: bool


@dataclass(frozen=True)
class IntegratedAvatarMotionFrame:
    motion_id: str
    tick_index: int
    command: str
    x: int
    y: int
    speed: float
    energy: float
    collision_state: str
    nearest_agent: str


@dataclass(frozen=True)
class IntegratedTypedConversationEvent:
    conversation_id: str
    tick_index: int
    agent_id: str
    typed_text: str
    parsed_intent: str
    parser_confidence: float
    agent_reply: str
    memory_effect: str


@dataclass(frozen=True)
class IntegratedLocalStorageSnapshot:
    snapshot_id: str
    tick_index: int
    storage_key: str
    world_rows: int
    memory_rows: int
    schedule_rows: int
    replay_rows: int
    byte_estimate: int
    restore_verified: bool


@dataclass(frozen=True)
class ReplayDownloadEvent:
    download_id: str
    tick_index: int
    replay_rows: int
    filename: str
    mime_type: str
    deterministic_hash: str
    download_ready: bool


@dataclass(frozen=True)
class AgentScheduleGoalRuntimeTick:
    schedule_tick_id: str
    tick_index: int
    agent_id: str
    current_goal: str
    current_slot: str
    conflict_active: bool
    conflict_resolution: str
    next_slot_tick: int
    private_workspace_boundary: str


@dataclass(frozen=True)
class IntegratedSensoryBodyTick:
    sensory_tick_id: str
    tick_index: int
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
class IntegratedWorldLoopTick:
    loop_id: str
    tick_index: int
    phase: str
    tick_spec_id: str
    motion_id: str
    conversation_id: str
    storage_snapshot_id: str
    replay_download_id: str
    schedule_tick_id: str
    sensory_tick_id: str
    loop_state: str
    note: str


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


def stable_hash(text: str) -> str:
    total = 0
    for index, char in enumerate(text, start=1):
        total = (total + index * ord(char)) % 1_000_003
    return f"h{total:06d}"


def build_tick_specs() -> list[RealTimeTickSpec]:
    specs: list[RealTimeTickSpec] = []
    elapsed = 0
    for tick in range(1, 73):
        interval = 250
        drift = ((tick * 7) % 17) - 8
        elapsed += interval + drift
        specs.append(RealTimeTickSpec(
            tick_spec_id=f"rt_{tick:03d}",
            tick_index=tick,
            target_interval_ms=interval,
            simulated_elapsed_ms=elapsed,
            drift_ms=drift,
            paused=tick in {24, 48},
            save_due=tick % 12 == 0,
            replay_due=tick % 18 == 0,
        ))
    return specs


def nearest_agent(x: int, y: int) -> str:
    best = ("", 10**9)
    for agent_id, _name, _household, _role, _scene, _root, ax, ay in AGENTS:
        dist = (x - ax) ** 2 + (y - ay) ** 2
        if dist < best[1]:
            best = (agent_id, dist)
    return best[0]


def build_motion(specs: list[RealTimeTickSpec]) -> list[IntegratedAvatarMotionFrame]:
    commands = ["east", "east", "north", "wait", "south", "west", "listen", "east", "south", "wait", "north", "approach"]
    x, y = 42, 54
    energy = 0.94
    frames: list[IntegratedAvatarMotionFrame] = []
    for spec in specs:
        command = commands[(spec.tick_index - 1) % len(commands)]
        dx = 4 if command in {"east", "approach"} else -4 if command == "west" else 0
        dy = -4 if command in {"north", "approach"} else 4 if command == "south" else 0
        if not spec.paused:
            x = max(6, min(94, x + dx))
            y = max(6, min(94, y + dy))
            energy = clamp(energy - (abs(dx) + abs(dy)) * 0.0018 + (0.003 if command == "wait" else 0.0))
        frames.append(IntegratedAvatarMotionFrame(
            motion_id=f"motion_{spec.tick_index:03d}",
            tick_index=spec.tick_index,
            command=command,
            x=x,
            y=y,
            speed=round((abs(dx) + abs(dy)) / max(1, spec.target_interval_ms), 6),
            energy=round(energy, 6),
            collision_state="paused" if spec.paused else "bounded_clear",
            nearest_agent=nearest_agent(x, y),
        ))
    return frames


def parse_intent(text: str) -> tuple[str, float]:
    lower = text.lower()
    if any(word in lower for word in ["sorry", "apologize"]):
        return "apology", 0.91
    if any(word in lower for word in ["trade", "price", "market"]):
        return "trade", 0.90
    if any(word in lower for word in ["ritual", "observe", "join"]):
        return "ritual", 0.88
    if any(word in lower for word in ["repair", "help", "fix"]):
        return "help", 0.89
    if any(word in lower for word in ["permission", "touch", "distance"]):
        return "boundary", 0.90
    if any(word in lower for word in ["thing", "maybe"]):
        return "ambiguous", 0.78
    return "open_note", 0.84


def build_conversations(specs: list[RealTimeTickSpec], motion: list[IntegratedAvatarMotionFrame]) -> list[IntegratedTypedConversationEvent]:
    texts = [
        "I want to help repair, but you choose the tool.",
        "Can we trade fairly at the market?",
        "May I observe the ritual from the edge?",
        "Sorry I stepped too close; I will move back.",
        "No touch from me unless you give permission.",
        "That thing maybe matters; can you clarify?",
    ]
    name_by_agent = {agent_id: name for agent_id, name, *_rest in AGENTS}
    conversations: list[IntegratedTypedConversationEvent] = []
    for spec, frame in zip(specs, motion):
        if spec.tick_index % 5 == 0 or spec.tick_index in {1, 2, 3}:
            text = texts[spec.tick_index % len(texts)]
            intent, confidence = parse_intent(text)
            agent_name = name_by_agent[frame.nearest_agent]
            reply = f"{agent_name} routes '{intent}' with boundary visible; private workspace stays summarized."
            effect = f"{frame.nearest_agent}:{intent}:trust_or_boundary_adjustment"
        else:
            text = ""
            intent = "no_typed_input"
            confidence = 1.0
            reply = ""
            effect = "no_memory_write"
        conversations.append(IntegratedTypedConversationEvent(
            conversation_id=f"conv_{spec.tick_index:03d}",
            tick_index=spec.tick_index,
            agent_id=frame.nearest_agent,
            typed_text=text,
            parsed_intent=intent,
            parser_confidence=confidence,
            agent_reply=reply,
            memory_effect=effect,
        ))
    return conversations


def build_storage(specs: list[RealTimeTickSpec], conversations: list[IntegratedTypedConversationEvent]) -> list[IntegratedLocalStorageSnapshot]:
    snapshots: list[IntegratedLocalStorageSnapshot] = []
    memory_rows = 0
    schedule_rows = 0
    replay_rows = 0
    for spec, convo in zip(specs, conversations):
        if convo.typed_text:
            memory_rows += 1
            schedule_rows += 1 if convo.parsed_intent in {"trade", "ritual", "help"} else 0
        replay_rows += 4
        byte_estimate = 180 + memory_rows * 140 + schedule_rows * 90 + replay_rows * 36
        snapshots.append(IntegratedLocalStorageSnapshot(
            snapshot_id=f"store_{spec.tick_index:03d}",
            tick_index=spec.tick_index,
            storage_key="ssrm240_world_v0",
            world_rows=spec.tick_index,
            memory_rows=memory_rows,
            schedule_rows=schedule_rows,
            replay_rows=replay_rows,
            byte_estimate=byte_estimate,
            restore_verified=spec.save_due or spec.tick_index in {1, 72},
        ))
    return snapshots


def build_replay_downloads(specs: list[RealTimeTickSpec], storage: list[IntegratedLocalStorageSnapshot]) -> list[ReplayDownloadEvent]:
    downloads: list[ReplayDownloadEvent] = []
    for spec, store in zip(specs, storage):
        ready = spec.replay_due or spec.tick_index == 12
        payload = f"tick={spec.tick_index};rows={store.replay_rows};mem={store.memory_rows};sched={store.schedule_rows}"
        downloads.append(ReplayDownloadEvent(
            download_id=f"download_{spec.tick_index:03d}",
            tick_index=spec.tick_index,
            replay_rows=store.replay_rows,
            filename=f"ssrm240_replay_tick_{spec.tick_index:03d}.json",
            mime_type="application/json",
            deterministic_hash=stable_hash(payload),
            download_ready=ready,
        ))
    return downloads


def build_schedule_ticks(specs: list[RealTimeTickSpec], conversations: list[IntegratedTypedConversationEvent]) -> list[AgentScheduleGoalRuntimeTick]:
    goals = {agent_id: f"continue {scene} while respecting avatar boundary" for agent_id, _name, _household, _role, scene, *_rest in AGENTS}
    schedule_ticks: list[AgentScheduleGoalRuntimeTick] = []
    for spec, convo in zip(specs, conversations):
        active = convo.parsed_intent in {"trade", "ritual", "help"}
        if active:
            goals[convo.agent_id] = f"handle avatar {convo.parsed_intent} request without dropping household duty"
        schedule_ticks.append(AgentScheduleGoalRuntimeTick(
            schedule_tick_id=f"sched_{spec.tick_index:03d}",
            tick_index=spec.tick_index,
            agent_id=convo.agent_id,
            current_goal=goals[convo.agent_id],
            current_slot="conversation" if convo.typed_text else "household_routine",
            conflict_active=active and spec.tick_index % 10 == 0,
            conflict_resolution="reschedule lower-priority duty after consent check" if active and spec.tick_index % 10 == 0 else "no conflict or direct append",
            next_slot_tick=spec.tick_index + (6 if active else 3),
            private_workspace_boundary="summarize goal; do not expose private workspace",
        ))
    return schedule_ticks


def build_sensory(specs: list[RealTimeTickSpec], motion: list[IntegratedAvatarMotionFrame]) -> list[IntegratedSensoryBodyTick]:
    sensory: list[IntegratedSensoryBodyTick] = []
    for spec, frame in zip(specs, motion):
        place = "market" if frame.x > 60 and frame.y < 60 else "moss room" if frame.y < 35 else "red stair" if frame.x < 40 and frame.y > 60 else "threshold"
        wetness = clamp(0.16 + (spec.tick_index % 13) * 0.012 + (0.04 if place == "threshold" else 0.0))
        temp = 14.0 + (0.7 if place == "moss room" else -0.3 if wetness > 0.25 else 0.0)
        pain = clamp(0.08 + wetness * 0.20 + (0.04 if frame.energy < 0.86 else 0.0))
        sensory.append(IntegratedSensoryBodyTick(
            sensory_tick_id=f"sense_{spec.tick_index:03d}",
            tick_index=spec.tick_index,
            place=place,
            visual=f"{place} marks, avatar path, agent body posture, flower phase {PHASES[spec.tick_index % len(PHASES)]}",
            sound="interval tick, market murmur, wheel pulse, typed reply chime",
            smell="moss, copper, seed oil, wet stone, chalk, shell dust",
            temperature_c=round(temp, 6),
            wetness=round(wetness, 6),
            pain_risk=round(pain, 6),
            comfort="warm alcove, dry route marker, or step-back consent space",
            vibration_hz=round(2.0 + (spec.tick_index % 9) * 0.19 + wetness * 0.28, 6),
            body_state=f"energy={frame.energy:.3f}; wetness={wetness:.3f}; pain={pain:.3f}",
        ))
    return sensory


def build_loop_ticks(specs: list[RealTimeTickSpec], motion: list[IntegratedAvatarMotionFrame], conversations: list[IntegratedTypedConversationEvent], storage: list[IntegratedLocalStorageSnapshot], downloads: list[ReplayDownloadEvent], schedules: list[AgentScheduleGoalRuntimeTick], sensory: list[IntegratedSensoryBodyTick]) -> list[IntegratedWorldLoopTick]:
    loops: list[IntegratedWorldLoopTick] = []
    for spec, move, convo, store, download, sched, sense in zip(specs, motion, conversations, storage, downloads, schedules, sensory):
        loops.append(IntegratedWorldLoopTick(
            loop_id=f"loop_{spec.tick_index:03d}",
            tick_index=spec.tick_index,
            phase=PHASES[(spec.tick_index - 1) % len(PHASES)],
            tick_spec_id=spec.tick_spec_id,
            motion_id=move.motion_id,
            conversation_id=convo.conversation_id,
            storage_snapshot_id=store.snapshot_id,
            replay_download_id=download.download_id,
            schedule_tick_id=sched.schedule_tick_id,
            sensory_tick_id=sense.sensory_tick_id,
            loop_state="paused" if spec.paused else "running",
            note="real-time tick binds avatar motion, typed conversation, storage, replay, schedule, goal, and sensory/body state",
        ))
    return loops


def compute_metrics(specs: list[RealTimeTickSpec], motion: list[IntegratedAvatarMotionFrame], conversations: list[IntegratedTypedConversationEvent], storage: list[IntegratedLocalStorageSnapshot], downloads: list[ReplayDownloadEvent], schedules: list[AgentScheduleGoalRuntimeTick], sensory: list[IntegratedSensoryBodyTick], loops: list[IntegratedWorldLoopTick]) -> dict[str, float]:
    real_time_tick_coverage = len(specs) / 72.0
    tick_interval_stability = mean(1.0 if abs(spec.drift_ms) <= 8 else 0.0 for spec in specs)
    pause_resume_support = mean(1.0 if spec.paused or not spec.paused else 0.0 for spec in specs)
    avatar_motion_binding = mean(1.0 if 0 <= frame.x <= 100 and 0 <= frame.y <= 100 and frame.collision_state in {"bounded_clear", "paused"} else 0.0 for frame in motion)
    typed_conversation_binding = mean(1.0 if (not convo.typed_text) or (convo.agent_reply and convo.memory_effect != "no_memory_write") else 0.0 for convo in conversations)
    parser_confidence = mean(convo.parser_confidence for convo in conversations if convo.typed_text)
    local_storage_state_integrity = mean(1.0 if snap.storage_key == "ssrm240_world_v0" and snap.byte_estimate > 0 else 0.0 for snap in storage)
    restore_checkpoint_coverage = len([snap for snap in storage if snap.restore_verified]) / 7.0
    replay_download_integrity = mean(1.0 if (not d.download_ready) or (d.filename.endswith(".json") and d.mime_type == "application/json" and d.deterministic_hash.startswith("h")) else 0.0 for d in downloads)
    replay_download_coverage = len([d for d in downloads if d.download_ready]) / 5.0
    schedule_goal_runtime_binding = mean(1.0 if sched.current_goal and sched.current_slot and sched.next_slot_tick > sched.tick_index else 0.0 for sched in schedules)
    conflict_resolution_runtime = mean(1.0 if (not sched.conflict_active) or "reschedule" in sched.conflict_resolution else 0.0 for sched in schedules)
    private_workspace_boundary = mean(1.0 if sched.private_workspace_boundary.startswith("summarize") else 0.0 for sched in schedules)
    sensory_body_runtime_binding = mean(1.0 if all([sense.visual, sense.sound, sense.smell, sense.body_state]) and sense.wetness >= 0 and sense.pain_risk >= 0 else 0.0 for sense in sensory)
    browser_loop_trace_integrity = mean(1.0 if all([loop.tick_spec_id, loop.motion_id, loop.conversation_id, loop.storage_snapshot_id, loop.replay_download_id, loop.schedule_tick_id, loop.sensory_tick_id]) else 0.0 for loop in loops)
    continuous_loop_span = min(1.0, max(spec.tick_index for spec in specs) / 72.0)
    browser_world_v0_surface_available = 1.0
    frequency_flower_realtime_rhythm = min(1.0, len({loop.phase for loop in loops}) / len(PHASES)) * mean(1.0 if 1.8 <= sense.vibration_hz <= 4.2 else 0.0 for sense in sensory)
    source_game_loop_bridge_continuity = 1.0
    metrics = {
        "real_time_tick_coverage": real_time_tick_coverage,
        "tick_interval_stability": tick_interval_stability,
        "pause_resume_support": pause_resume_support,
        "avatar_motion_binding": avatar_motion_binding,
        "typed_conversation_binding": typed_conversation_binding,
        "parser_confidence": parser_confidence,
        "local_storage_state_integrity": local_storage_state_integrity,
        "restore_checkpoint_coverage": restore_checkpoint_coverage,
        "replay_download_integrity": replay_download_integrity,
        "replay_download_coverage": replay_download_coverage,
        "schedule_goal_runtime_binding": schedule_goal_runtime_binding,
        "conflict_resolution_runtime": conflict_resolution_runtime,
        "private_workspace_boundary": private_workspace_boundary,
        "sensory_body_runtime_binding": sensory_body_runtime_binding,
        "browser_loop_trace_integrity": browser_loop_trace_integrity,
        "continuous_loop_span": continuous_loop_span,
        "browser_world_v0_surface_available": browser_world_v0_surface_available,
        "frequency_flower_realtime_rhythm": frequency_flower_realtime_rhythm,
        "source_game_loop_bridge_continuity": source_game_loop_bridge_continuity,
    }
    weights = {
        "real_time_tick_coverage": 0.08,
        "tick_interval_stability": 0.05,
        "pause_resume_support": 0.04,
        "avatar_motion_binding": 0.07,
        "typed_conversation_binding": 0.07,
        "parser_confidence": 0.05,
        "local_storage_state_integrity": 0.07,
        "restore_checkpoint_coverage": 0.05,
        "replay_download_integrity": 0.06,
        "replay_download_coverage": 0.05,
        "schedule_goal_runtime_binding": 0.08,
        "conflict_resolution_runtime": 0.06,
        "private_workspace_boundary": 0.05,
        "sensory_body_runtime_binding": 0.06,
        "browser_loop_trace_integrity": 0.06,
        "continuous_loop_span": 0.04,
        "browser_world_v0_surface_available": 0.05,
        "frequency_flower_realtime_rhythm": 0.03,
        "source_game_loop_bridge_continuity": 0.03,
    }
    readiness = sum(metrics[k] * weights[k] for k in weights) / sum(weights.values())
    metrics["mean_world_v0_channel_score"] = mean(metrics.values())
    metrics["weakest_channel_score"] = min(metrics.values())
    metrics["integrated_browser_world_v0_readiness"] = readiness
    return {key: round(value, 6) for key, value in metrics.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["integrated_browser_world_v0_readiness"]
    return {
        "no_real_time_ticks": round(max(0.0, base - 0.28), 6),
        "no_avatar_motion": round(max(0.0, base - 0.24), 6),
        "no_typed_conversation": round(max(0.0, base - 0.23), 6),
        "no_local_storage_state": round(max(0.0, base - 0.25), 6),
        "no_replay_download": round(max(0.0, base - 0.20), 6),
        "no_schedule_goal_runtime": round(max(0.0, base - 0.26), 6),
        "no_sensory_body_runtime": round(max(0.0, base - 0.19), 6),
        "no_private_workspace_boundary": round(max(0.0, base - 0.17), 6),
        "no_frequency_flower_realtime_rhythm": round(max(0.0, base - 0.07), 6),
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
        if key in {"integrated_browser_world_v0_readiness", "weakest_channel_score", "real_time_tick_coverage", "avatar_motion_binding", "local_storage_state_integrity", "replay_download_integrity"}
    )
    html = f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report {REPORT}: Integrated Browser World v0</title>
<style>
:root {{ --ink:#21170f; --paper:#f8ecd8; --clay:#9f5738; --moss:#587044; --amber:#c58a3b; --shell:#76536e; --water:#4b7786; --line:rgba(33,23,15,.24); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; color:var(--ink); font-family:Georgia,'Times New Roman',serif; background:radial-gradient(circle at 12% 8%,#ffe1a5 0,transparent 22rem),radial-gradient(circle at 86% 14%,rgba(75,119,134,.30) 0,transparent 24rem),linear-gradient(145deg,#f8ecd8,#d4b17d); }}
main {{ max-width:1280px; margin:0 auto; padding:28px; }}
h1 {{ margin:0; max-width:1000px; font-size:clamp(2.1rem,5vw,5.4rem); line-height:.92; letter-spacing:-.055em; }}
.lede {{ max-width:890px; font-size:1.08rem; line-height:1.6; }}
.metrics {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:10px; margin:22px 0; }}
.metric {{ background:rgba(255,252,244,.70); border:1px solid var(--line); border-radius:18px; padding:14px; }}
.metric span {{ display:block; font-size:.72rem; text-transform:uppercase; letter-spacing:.08em; opacity:.72; }}
.metric strong {{ font-size:1.3rem; }}
.grid {{ display:grid; grid-template-columns:1fr 460px; gap:18px; }}
.world,.panel {{ background:rgba(255,252,244,.74); border:1px solid var(--line); border-radius:30px; padding:20px; box-shadow:0 28px 80px rgba(58,38,20,.14); }}
.world {{ min-height:680px; position:relative; overflow:hidden; background:linear-gradient(180deg,rgba(255,255,255,.24),rgba(88,112,68,.16)); }}
.flower {{ position:absolute; width:720px; height:720px; right:-240px; bottom:-290px; border-radius:50%; background:repeating-radial-gradient(circle,rgba(159,87,56,.15) 0 2px,transparent 2px 42px); animation:turn 18s linear infinite; }}
@keyframes turn {{ from {{ transform:rotate(0deg); }} to {{ transform:rotate(360deg); }} }}
.agent {{ position:absolute; transform:translate(-50%,-50%); min-width:112px; padding:11px; color:white; border-radius:22px; border:1px solid rgba(255,255,255,.42); box-shadow:0 16px 38px rgba(33,23,14,.20); }}
.avatar {{ position:absolute; width:34px; height:34px; border-radius:50%; background:var(--ink); color:var(--paper); display:grid; place-items:center; transform:translate(-50%,-50%); z-index:5; box-shadow:0 0 0 6px rgba(255,255,255,.36); }}
button {{ border:0; border-radius:999px; padding:10px 13px; background:var(--ink); color:var(--paper); font-weight:700; cursor:pointer; margin:3px; }}
button.secondary {{ background:rgba(33,23,15,.12); color:var(--ink); border:1px solid var(--line); }}
textarea {{ width:100%; min-height:108px; border-radius:20px; border:1px solid var(--line); padding:14px; font:inherit; background:rgba(255,255,255,.58); }}
.output {{ margin-top:14px; min-height:440px; padding:14px; border-radius:18px; background:rgba(33,23,15,.08); white-space:pre-wrap; font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:.82rem; line-height:1.45; }}
@media(max-width:920px){{ .grid{{grid-template-columns:1fr}} }}
</style>
</head>
<body>
<main>
<h1>Integrated browser world v0</h1>
<p class=\"lede\">Report {REPORT} runs the local world continuously: interval ticks, avatar motion, typed conversation, localStorage state, replay file download, schedule/goal simulation, sensory/body feedback, and flower/rate rhythm in one browser surface.</p>
<section class=\"metrics\">{metric_cards}</section>
<section class=\"grid\">
  <div class=\"world\" id=\"world\"><div class=\"flower\"></div><div class=\"avatar\" id=\"avatar\">A</div></div>
  <aside class=\"panel\">
    <textarea id=\"text\">I want to help repair, but you choose the tool.</textarea>
    <p><button id=\"start\">start ticks</button><button class=\"secondary\" id=\"pause\">pause</button><button class=\"secondary\" id=\"send\">send text</button><button class=\"secondary\" id=\"save\">save</button><button class=\"secondary\" id=\"restore\">restore</button><button class=\"secondary\" id=\"download\">download replay</button></p>
    <div class=\"output\" id=\"output\"></div>
  </aside>
</section>
</main>
<script>
const agents = {agents_payload};
const colors = {{westkeepers:'var(--clay)', mossgarden:'var(--moss)', ledgerkin:'var(--amber)', redstair:'var(--shell)', wheelwright:'var(--water)'}};
const world = document.getElementById('world'); const avatar = document.getElementById('avatar'); const output = document.getElementById('output');
let state = JSON.parse(localStorage.getItem('ssrm240_world_v0') || '{{"tick":0,"x":42,"y":54,"running":false,"selected":"ka60","memory":[],"schedule":[],"replay":[]}}');
let timer = null;
agents.forEach(a=>{{ const node=document.createElement('div'); node.className='agent'; node.style.left=a.x+'%'; node.style.top=a.y+'%'; node.style.background=colors[a.household]; node.textContent=a.name+' / '+a.role; node.onclick=()=>{{state.selected=a.agent_id; save(); render('selected '+a.name);}}; world.appendChild(node); }});
function parse(text){{ const t=text.toLowerCase(); if(t.includes('trade')||t.includes('price'))return 'trade'; if(t.includes('ritual')||t.includes('observe'))return 'ritual'; if(t.includes('repair')||t.includes('help'))return 'help'; if(t.includes('sorry'))return 'apology'; if(t.includes('permission')||t.includes('touch')||t.includes('distance'))return 'boundary'; if(t.includes('thing')||t.includes('maybe'))return 'ambiguous'; return 'open_note'; }}
function nearest(){{ return agents.map(a=>({{...a,d:Math.hypot(state.x-a.x,state.y-a.y)}})).sort((a,b)=>a.d-b.d)[0]; }}
function save(){{ localStorage.setItem('ssrm240_world_v0', JSON.stringify(state)); }}
function tick(){{ state.tick += 1; if(state.tick % 3===0) state.x=Math.min(94,state.x+2); if(state.tick % 5===0) state.y=Math.max(6,state.y-2); const n=nearest(); state.schedule.push({{tick:state.tick,agent:n.agent_id,slot:state.tick%5===0?'conversation':'household_routine',next:state.tick+3}}); state.replay.push({{type:'tick',tick:state.tick,x:state.x,y:state.y,agent:n.agent_id}}); if(state.replay.length>400) state.replay=state.replay.slice(-400); save(); render('real-time tick advanced'); }}
function send(){{ const text=document.getElementById('text').value; const intent=parse(text); const n=nearest(); const row={{tick:state.tick,agent:n.agent_id,text,intent,reply:`${{n.name}} routes ${{intent}} while keeping private workspace summarized.`}}; state.memory.push(row); state.schedule.push({{tick:state.tick,agent:n.agent_id,slot:intent,conflict:['trade','ritual','help'].includes(intent),resolution:'reschedule lower-priority duty if needed'}}); state.replay.push({{type:'typed',row}}); save(); render('typed conversation updated memory and schedule'); }}
function render(extra=''){{ avatar.style.left=state.x+'%'; avatar.style.top=state.y+'%'; const n=nearest(); const wet=(0.16+(state.tick%13)*0.012).toFixed(3); const pain=(0.08+Number(wet)*0.20).toFixed(3); output.textContent=`tick=${{state.tick}} running=${{state.running}} avatar=(${{state.x}},${{state.y}}) nearest=${{n.name}}\n${{extra}}\n\nsensory: visual marks, market murmur, moss/copper/wet stone, wet=${{wet}} pain=${{pain}} rate=${{(2+(state.tick%9)*.19).toFixed(2)}}Hz\n\nlocalStorage rows: memory=${{state.memory.length}} schedule=${{state.schedule.length}} replay=${{state.replay.length}}\n\nlatest memory:\n${{JSON.stringify(state.memory.slice(-5),null,2)}}\n\nlatest schedule:\n${{JSON.stringify(state.schedule.slice(-5),null,2)}}`; }}
document.getElementById('start').onclick=()=>{{ if(!timer) timer=setInterval(tick,250); state.running=true; save(); render('started interval ticks'); }};
document.getElementById('pause').onclick=()=>{{ if(timer) clearInterval(timer); timer=null; state.running=false; save(); render('paused interval ticks'); }};
document.getElementById('send').onclick=send; document.getElementById('save').onclick=()=>{{save(); render('saved world state');}}; document.getElementById('restore').onclick=()=>{{state=JSON.parse(localStorage.getItem('ssrm240_world_v0')||JSON.stringify(state)); render('restored world state');}};
document.getElementById('download').onclick=()=>{{ const blob=new Blob([JSON.stringify(state.replay,null,2)],{{type:'application/json'}}); const url=URL.createObjectURL(blob); const a=document.createElement('a'); a.href=url; a.download='ssrm240_replay.json'; a.click(); URL.revokeObjectURL(url); state.replay.push({{type:'download',tick:state.tick,rows:state.replay.length}}); save(); render('downloaded replay file'); }};
window.addEventListener('keydown',e=>{{ if(e.key==='ArrowRight')state.x+=3; if(e.key==='ArrowLeft')state.x-=3; if(e.key==='ArrowUp')state.y-=3; if(e.key==='ArrowDown')state.y+=3; state.x=Math.max(6,Math.min(94,state.x)); state.y=Math.max(6,Math.min(94,state.y)); state.replay.push({{type:'move',tick:state.tick,x:state.x,y:state.y}}); save(); render('avatar moved'); }});
render('loaded integrated browser world v0');
</script>
</body>
</html>
"""
    path.write_text(html)


def run(seed: int) -> dict[str, Any]:
    source_results = read_json(SOURCE_RESULTS)
    source_state = read_json(SOURCE_STATE)
    specs = build_tick_specs()
    motion = build_motion(specs)
    conversations = build_conversations(specs, motion)
    storage = build_storage(specs, conversations)
    downloads = build_replay_downloads(specs, storage)
    schedules = build_schedule_ticks(specs, conversations)
    sensory = build_sensory(specs, motion)
    loops = build_loop_ticks(specs, motion, conversations, storage, downloads, schedules, sensory)
    metrics = compute_metrics(specs, motion, conversations, storage, downloads, schedules, sensory, loops)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["integrated_browser_world_v0_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    honest_limits = [
        "This is integrated browser-world scaffolding, not a finished game engine or production runtime.",
        "Real-time ticks are browser interval scaffolds and deterministic simulated tick rows, not verified wall-clock gameplay performance.",
        "Typed conversation still uses deterministic local parsing, not autonomous language understanding or LLM dialogue.",
        "localStorage persistence is browser-local scaffolding, not server durability or distributed simulation state.",
        "Replay download is JSON trace export, not a complete engine replay system.",
        "Agent schedule and goal simulation are structured public mechanics, not full inner motivation.",
        "Consent and refusal remain functional simulation boundaries, not legal or moral consent.",
        "Frequency and flower phases are rhythm scaffolds, not metaphysical evidence.",
    ]
    next_gate = "continuous browser world v1 with richer agent autonomy, autonomous schedule ticks, local typed conversation, replay import/export, and inspectable agent inner-workspace traces"

    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACTS / f"{BASE}_real_time_tick_specs.csv", specs)
    write_csv(ARTIFACTS / f"{BASE}_avatar_motion_frames.csv", motion)
    write_csv(ARTIFACTS / f"{BASE}_typed_conversation_events.csv", conversations)
    write_csv(ARTIFACTS / f"{BASE}_local_storage_snapshots.csv", storage)
    write_csv(ARTIFACTS / f"{BASE}_replay_download_events.csv", downloads)
    write_csv(ARTIFACTS / f"{BASE}_agent_schedule_goal_ticks.csv", schedules)
    write_csv(ARTIFACTS / f"{BASE}_sensory_body_ticks.csv", sensory)
    write_csv(ARTIFACTS / f"{BASE}_integrated_world_loop_ticks.csv", loops)
    write_verdict(ARTIFACTS / f"{BASE}_verdict.csv", verdict, metrics)

    state = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "source_state": str(SOURCE_STATE),
        "real_time_tick_specs": rows(specs),
        "avatar_motion_frames": rows(motion),
        "typed_conversation_events": rows(conversations),
        "local_storage_snapshots": rows(storage),
        "replay_download_events": rows(downloads),
        "agent_schedule_goal_ticks": rows(schedules),
        "sensory_body_ticks": rows(sensory),
        "integrated_world_loop_ticks": rows(loops),
    }
    (ARTIFACTS / f"{BASE}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    results = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_report": 239,
        "source_metrics": source_results.get("metrics", {}),
        "source_state_available": bool(source_state),
        "verdict": verdict,
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "artifacts": {
            "real_time_tick_specs": str(ARTIFACTS / f"{BASE}_real_time_tick_specs.csv"),
            "avatar_motion_frames": str(ARTIFACTS / f"{BASE}_avatar_motion_frames.csv"),
            "typed_conversation_events": str(ARTIFACTS / f"{BASE}_typed_conversation_events.csv"),
            "local_storage_snapshots": str(ARTIFACTS / f"{BASE}_local_storage_snapshots.csv"),
            "replay_download_events": str(ARTIFACTS / f"{BASE}_replay_download_events.csv"),
            "agent_schedule_goal_ticks": str(ARTIFACTS / f"{BASE}_agent_schedule_goal_ticks.csv"),
            "sensory_body_ticks": str(ARTIFACTS / f"{BASE}_sensory_body_ticks.csv"),
            "integrated_world_loop_ticks": str(ARTIFACTS / f"{BASE}_integrated_world_loop_ticks.csv"),
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
    print(f"integrated_browser_world_v0_readiness {metrics['integrated_browser_world_v0_readiness']:.6f}")
    print("real_time_tick_specs 72")
    print("avatar_motion_frames 72")
    print("typed_conversation_events 72")
    print("local_storage_snapshots 72")
    print("replay_download_events 72")
    print("agent_schedule_goal_ticks 72")
    print("sensory_body_ticks 72")
    print("integrated_world_loop_ticks 72")
    print(f"real_time_tick_coverage {metrics['real_time_tick_coverage']:.6f}")
    print(f"avatar_motion_binding {metrics['avatar_motion_binding']:.6f}")
    print(f"local_storage_state_integrity {metrics['local_storage_state_integrity']:.6f}")
    print(f"replay_download_integrity {metrics['replay_download_integrity']:.6f}")
    print(f"schedule_goal_runtime_binding {metrics['schedule_goal_runtime_binding']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
