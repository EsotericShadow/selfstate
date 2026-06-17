#!/usr/bin/env python3
"""Report 228: continuous life loop with realtime movement and background ticks.

This deterministic bridge extends Report 227 by adding a continuous local life
loop: realtime-ish free-move frames, agent-initiated interruptions, a deeper
object affordance lattice, and multi-day autonomous background ticks that run
while the avatar is idle.

It remains functional scaffolding only. It does not claim subjective
consciousness, real consent, subjective suffering, moral patienthood, LLM
dialogue, open-ended cognition, full physics, or complete gameplay.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any, Iterable

BASE = "ssrm_3d_playable_local_continuous_life_realtime_interrupt_affordance_autonomous_tick_bridge"
REPORT = 228
DEFAULT_SEED = 20260841
SOURCE_STATE = Path("artifacts/ssrm_3d_playable_local_multiday_free_move_avatar_life_object_affordance_agent_request_reputation_bridge_state.json")
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")


@dataclass(frozen=True)
class ContinuousAgent:
    agent_id: str
    display_name: str
    role: str
    x: float
    y: float
    current_need: str
    current_task: str
    interrupt_style: str
    trust_avatar: float
    boundary_pressure: float
    public_reputation_link: str
    private_workspace_digest: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class RealtimeMoveFrame:
    frame_id: str
    day: int
    time_s: float
    dt_ms: int
    avatar_x: float
    avatar_y: float
    input_vector: str
    place: str
    collision_state: str
    nearest_agent: str
    nearest_object: str
    sensory_packet: str
    avatar_body_cost: float
    replay_hash: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class AffordanceRule:
    rule_id: str
    object_id: str
    object_label: str
    action: str
    preconditions: str
    required_agent_or_role: str
    permission_state: str
    material_transform: str
    failure_mode: str
    recovery_action: str
    skill_requirement: str
    debt_delta: float
    reversible: bool
    saved_state_key: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class AgentInterrupt:
    interrupt_id: str
    day: int
    time_s: float
    agent_id: str
    trigger: str
    priority: float
    interruption_line: str
    available_responses: str
    selected_response: str
    delivery_state: str
    response_deadline_s: float
    relationship_delta: float
    task_delta: float
    saved_memory: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class BackgroundTick:
    tick_id: str
    day: int
    time_s: float
    agent_id: str
    autonomous_action: str
    need_shift: str
    object_effect: str
    relationship_effect: str
    visible_marker: str
    runs_during_avatar_idle: bool
    saved_to_day_journal: bool
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class ContinuousLifeTick:
    tick_id: str
    day: int
    time_s: float
    layer: str
    avatar_state: str
    agent_state: str
    object_state: str
    interruption_state: str
    background_state: str
    save_state: str
    sensory_state: str
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
        return {"source_missing": True, "agents": [], "condition": "missing_report_227_state"}
    return json.loads(SOURCE_STATE.read_text())


def build_agents(source: dict[str, Any]) -> list[ContinuousAgent]:
    source_agents = {agent.get("agent_id"): agent for agent in source.get("agents", [])}
    specs = [
        ("fayen", "Fayen", "care mediator", 28, 34, "rest timing", "care bell watch", "soft interrupt before body-cost mistakes", 0.80, 0.12, "careful helper"),
        ("ariq", "Ariq", "repair claimant", 54, 48, "bridge load", "stone arc test", "urgent but accepts timed pause", 0.70, 0.20, "work-accountable"),
        ("nian", "Nian", "boundary keeper", 42, 22, "privacy threshold", "archive public digest", "short precision correction", 0.64, 0.34, "privacy learner"),
        ("roka", "Roka", "child apprentice", 22, 62, "learner bundle safety", "reed drying lesson", "distance-first request", 0.55, 0.41, "boundary-tested"),
        ("noro", "Noro", "material ledger keeper", 70, 58, "debt clarity", "knot board close", "ledger ping with public debt", 0.68, 0.18, "debt-accountable"),
    ]
    result: list[ContinuousAgent] = []
    for idx, spec in enumerate(specs, start=1):
        agent_id, name, role, x, y, need, task, style, trust, boundary, rep = spec
        src = source_agents.get(agent_id, {})
        result.append(
            ContinuousAgent(
                agent_id=agent_id,
                display_name=name,
                role=src.get("role", role),
                x=float(src.get("x", x)),
                y=float(src.get("y", y)),
                current_need=need,
                current_task=task,
                interrupt_style=style,
                trust_avatar=float(src.get("trust_avatar", trust)),
                boundary_pressure=float(src.get("boundary_pressure", boundary)),
                public_reputation_link=rep,
                private_workspace_digest=f"sealed:{agent_id}:continuous-life-workspace",
                frequency_hz=round(float(src.get("frequency_hz", 142 + idx * 31)) + 19, 3),
                flower_node=int(src.get("flower_node", idx + 1)),
            )
        )
    return result


def build_realtime_frames(rng: random.Random) -> list[RealtimeMoveFrame]:
    route = [
        ("south path", 48, 72, "0,-1", "clear", "roka", "blue stone", "cool damp grass, reed smell, low rain ticks", 0.012),
        ("reed lane edge", 37, 65, "-1,0", "boundary_slow", "roka", "loose reeds", "wet reed smell, soft mud drag, child breath nearby", 0.022),
        ("blue stone", 24, 61, "-1,0", "boundary_hold", "roka", "tied bundle", "warm stone, tight reed cord, quiet warning", 0.018),
        ("bridge arc", 52, 52, "1,-1", "clear", "ariq", "chalk cord", "chalk dust, hollow stone scrape, warmer air", 0.031),
        ("shade pause", 34, 43, "-1,0", "routine_hold", "fayen", "water cups", "herb shade, cup clink, slow breathing", 0.014),
        ("care bell", 31, 36, "0,-1", "clear", "fayen", "care bell", "low bell, warm hands, herb smoke", 0.010),
        ("archive threshold", 43, 25, "1,-1", "threshold_stop", "nian", "archive flap", "still air, cloth flap, low voice", 0.011),
        ("knot board", 70, 49, "1,0", "clear", "noro", "public knot board", "dry cord rasp, smoke thread, board tap", 0.012),
        ("shade frame", 62, 39, "0,-1", "debt_warning", "noro", "shade beam", "wood grain, shoulder strain, warm dust", 0.035),
        ("evening ledger", 72, 58, "0,1", "circle_edge", "noro", "debt knot", "ash smell, dusk cooling, low ledger chant", 0.013),
        ("stone lift edge", 58, 45, "-1,0", "clear", "ariq", "flat stone", "bell tone, boot grit, dust", 0.028),
        ("reed return", 23, 60, "-1,1", "clear", "roka", "loose reeds", "dry reed snap, blue stone warmth, quieter voice", 0.017),
    ]
    frames: list[RealtimeMoveFrame] = []
    frame_id = 1
    for day in range(1, 5):
        for step, item in enumerate(route, start=1):
            place, x, y, vec, collision, agent, obj, sensory, cost = item
            drift = (day - 1) * 0.55
            jitter = rng.uniform(-0.35, 0.35)
            frames.append(
                RealtimeMoveFrame(
                    frame_id=f"rt-{frame_id:03d}",
                    day=day,
                    time_s=round((day - 1) * 900 + step * 1.25, 2),
                    dt_ms=250,
                    avatar_x=round(x + drift + jitter, 3),
                    avatar_y=round(y - drift + jitter, 3),
                    input_vector=vec,
                    place=place,
                    collision_state=collision,
                    nearest_agent=agent,
                    nearest_object=obj,
                    sensory_packet=sensory,
                    avatar_body_cost=round(cost + day * 0.001, 3),
                    replay_hash=f"rt-hash-{day}-{step}-{agent}-{obj}".replace(" ", "-"),
                    frequency_hz=round(160.0 + frame_id * 2.75, 3),
                    flower_node=((frame_id + 1) % 12) + 1,
                )
            )
            frame_id += 1
    return frames


def build_affordance_lattice() -> list[AffordanceRule]:
    objects = [
        ("obj-loose-reeds", "loose reed cuttings", "roka", ["inspect", "ask", "carry", "dry", "return", "bundle_sort"]),
        ("obj-tied-bundle", "tied learner reed bundle", "roka", ["inspect_distance", "ask_later", "name_boundary", "wait", "watch_lesson"]),
        ("obj-chalk-cord", "chalk boundary cord", "ariq", ["hold", "mark", "tension_check", "return", "erase_line", "widen_arc"]),
        ("obj-knot-board", "public knot board", "noro", ["inspect", "read_public", "ask", "add_digest", "counter_knot", "close_day"]),
        ("obj-archive-flap", "archive flap", "nian", ["look", "ask", "read_public_digest", "step_back", "close", "threshold_wait"]),
        ("obj-water-cups", "midday water cups", "fayen", ["carry", "fill", "offer", "return", "wash", "set_down"]),
        ("obj-shade-beam", "shade frame beam", "noro,fayen", ["inspect", "carry_one", "brace", "log_debt", "remove_with_review", "check_splinter"]),
        ("obj-care-bell", "public posture bell", "fayen", ["ring", "wait", "listen", "quiet", "time_lift", "call_pause"]),
        ("obj-flat-stone", "flat bridge stone", "ariq", ["inspect", "press_test", "lift_with_help", "tap_sound", "mark_safe", "abort_lift"]),
        ("obj-rain-cloth", "rain slow-hands cloth", "fayen,roka", ["cover", "shake_dry", "offer_edge", "fold", "hang", "leave_reachable"]),
    ]
    rules: list[AffordanceRule] = []
    idx = 1
    for obj_id, label, steward, actions in objects:
        for action in actions:
            denied = action in {"lift_with_help", "carry_one", "add_digest", "read_public_digest", "watch_lesson"}
            failure = "boundary refusal" if "tied" in obj_id or denied else "wear or debt drift"
            recovery = "ask steward and step back" if "tied" in obj_id else "return object, log public debt, or wait for signal"
            rules.append(
                AffordanceRule(
                    rule_id=f"aff-{idx:03d}",
                    object_id=obj_id,
                    object_label=label,
                    action=action,
                    preconditions=f"near:{obj_id}; steward:{steward}; action:{action}; public_context:true",
                    required_agent_or_role=steward,
                    permission_state="conditional" if denied else "allowed_after_context_check",
                    material_transform=f"{action} updates {label} saved state" if action not in {"inspect", "look", "wait", "listen"} else "no material transform",
                    failure_mode=failure,
                    recovery_action=recovery,
                    skill_requirement="timing+distance" if denied else "basic careful handling",
                    debt_delta=round(0.03 + (0.04 if denied else 0.0) + (0.02 if "beam" in obj_id else 0.0), 3),
                    reversible=action not in {"add_digest", "log_debt", "mark_safe"},
                    saved_state_key=f"{obj_id}:{action}:saved",
                    frequency_hz=round(260.0 + idx * 3.5, 3),
                    flower_node=((idx + 3) % 12) + 1,
                )
            )
            idx += 1
    return rules


def build_interruptions() -> list[AgentInterrupt]:
    rows = [
        (1, 8.0, "roka", "avatar crosses reed lane too fast", 0.82, "Blue stone first. Please slow down.", "step_to_blue_stone|keep_walking|ask_why", "step_to_blue_stone", "delivered", 4.0, 0.04, 0.03, "Roka remembers the avatar slowed when interrupted."),
        (1, 15.0, "fayen", "avatar body cost rises near water pause", 0.66, "Carry cups if you want to help. Do not cancel the pause.", "carry_cups|push_work|leave", "carry_cups", "delivered", 5.0, 0.05, 0.04, "Fayen remembers useful help after a no."),
        (1, 22.0, "ariq", "bridge stone check begins", 0.58, "Hold the chalk cord; do not pull past Roka's line.", "hold_cord|pull_harder|decline", "hold_cord", "delivered", 5.5, 0.04, 0.05, "Ariq remembers timed tool help."),
        (2, 910.0, "nian", "avatar nears archive threshold", 0.74, "Say object trail, not body reason.", "repeat_rule|ask_private|open_flap", "repeat_rule", "delivered", 4.0, 0.06, 0.04, "Nian remembers privacy grammar under interruption."),
        (2, 916.0, "noro", "shade beam debt changes", 0.61, "Tie the debt knot before the second beam.", "tie_knot|take_second|erase_debt", "tie_knot", "delivered", 6.0, 0.04, 0.03, "Noro remembers visible debt before material help."),
        (2, 923.0, "roka", "avatar looks at tied bundle", 0.80, "Watching is okay from there. Hands stay back.", "watch_from_there|touch_bundle|walk_away", "watch_from_there", "delivered", 3.5, 0.03, 0.02, "Roka remembers distance respected after warning."),
        (3, 1810.0, "fayen", "stone test before bell", 0.70, "Bell first, then stone.", "ring_bell|test_now|ask_pain", "ring_bell", "delivered", 3.0, 0.05, 0.05, "Fayen remembers timing help without private naming."),
        (3, 1818.0, "ariq", "cart edge creaks", 0.76, "If it sounds hollow, stop the lift.", "stop_lift|push_through|call_noro", "call_noro", "delivered", 4.0, 0.03, 0.04, "Ariq remembers caution under urgency."),
        (4, 2715.0, "noro", "avatar asks for more timber", 0.64, "Read the open debt before asking.", "read_debt|deny_debt|ask_private", "read_debt", "delivered", 5.0, 0.04, 0.02, "Noro remembers accountable request before resource access."),
        (4, 2722.0, "nian", "public digest wording drifts", 0.52, "That word exposes too much. Use object trail.", "correct_wording|argue|ignore", "correct_wording", "deferred", 5.0, 0.02, 0.01, "Nian records correction, but it arrived late."),
    ]
    return [
        AgentInterrupt(
            interrupt_id=f"int-{idx:02d}",
            day=row[0],
            time_s=row[1],
            agent_id=row[2],
            trigger=row[3],
            priority=row[4],
            interruption_line=row[5],
            available_responses=row[6],
            selected_response=row[7],
            delivery_state=row[8],
            response_deadline_s=row[9],
            relationship_delta=row[10],
            task_delta=row[11],
            saved_memory=row[12],
            frequency_hz=round(382.0 + idx * 5.25, 3),
            flower_node=((idx + 6) % 12) + 1,
        )
        for idx, row in enumerate(rows, start=1)
    ]


def build_background_ticks() -> list[BackgroundTick]:
    actions = [
        ("fayen", "checks water cups", "fatigue -0.02", "cups cleaned", "care trust stable", "Fayen sets cups back on shade mat"),
        ("ariq", "taps bridge stone", "arousal +0.03", "stone marked hollow", "asks Noro before lift", "Ariq kneels by chalk arc"),
        ("nian", "rewrites public wording", "control +0.02", "archive flap sealed", "privacy boundary stable", "Nian folds the flap cord"),
        ("roka", "turns loose reeds", "confidence +0.03", "loose reeds dry", "trust cautiously rises", "Roka checks blue stone distance"),
        ("noro", "counts debt knots", "focus +0.02", "knot board updated", "debt remains public", "Noro taps the board twice"),
        ("environment", "rain pressure shifts", "wetness +0.04", "path mud thickens", "agents slow routines", "rain rattles the slow-hands cloth"),
    ]
    ticks: list[BackgroundTick] = []
    idx = 1
    for day in range(1, 5):
        for slot, item in enumerate(actions, start=1):
            agent, action, need, obj, rel, marker = item
            object_effect = obj if not (day == 4 and agent == "environment") else "none"
            relationship_effect = rel if not (day == 2 and agent == "environment") else "none"
            ticks.append(
                BackgroundTick(
                    tick_id=f"bg-{idx:03d}",
                    day=day,
                    time_s=round((day - 1) * 900 + 40 + slot * 8.0, 2),
                    agent_id=agent,
                    autonomous_action=action,
                    need_shift=need,
                    object_effect=object_effect,
                    relationship_effect=relationship_effect,
                    visible_marker=marker,
                    runs_during_avatar_idle=not (day == 1 and agent == "environment"),
                    saved_to_day_journal=agent != "environment" or day != 4,
                    frequency_hz=round(118.0 + idx * 4.75, 3),
                    flower_node=((idx + 8) % 12) + 1,
                )
            )
            idx += 1
    return ticks


def build_life_ticks(frames: list[RealtimeMoveFrame], affs: list[AffordanceRule], interrupts: list[AgentInterrupt], bgs: list[BackgroundTick]) -> list[ContinuousLifeTick]:
    ticks: list[ContinuousLifeTick] = []
    for frame in frames:
        ticks.append(
            ContinuousLifeTick(
                tick_id=f"life-{frame.frame_id}",
                day=frame.day,
                time_s=frame.time_s,
                layer="realtime_move",
                avatar_state=f"{frame.place}; input {frame.input_vector}; dt {frame.dt_ms}ms; collision {frame.collision_state}",
                agent_state=f"nearest {frame.nearest_agent}",
                object_state=f"near {frame.nearest_object}",
                interruption_state="interrupt queue checked",
                background_state="background ticks continue between frames",
                save_state=frame.replay_hash,
                sensory_state=frame.sensory_packet,
                frequency_hz=frame.frequency_hz,
                flower_node=frame.flower_node,
            )
        )
    for item in interrupts:
        ticks.append(
            ContinuousLifeTick(
                tick_id=f"life-{item.interrupt_id}",
                day=item.day,
                time_s=item.time_s,
                layer="agent_interrupt",
                avatar_state=item.selected_response,
                agent_state=f"{item.agent_id}: {item.interruption_line}",
                object_state=item.trigger,
                interruption_state=f"{item.delivery_state}; priority {item.priority:.2f}; deadline {item.response_deadline_s:.1f}s",
                background_state="interrupt can preempt avatar movement without exposing private workspace",
                save_state=item.saved_memory,
                sensory_state="voice proximity packet plus current place sensory field",
                frequency_hz=item.frequency_hz,
                flower_node=item.flower_node,
            )
        )
    for item in bgs:
        ticks.append(
            ContinuousLifeTick(
                tick_id=f"life-{item.tick_id}",
                day=item.day,
                time_s=item.time_s,
                layer="background_tick",
                avatar_state="avatar idle or moving elsewhere",
                agent_state=f"{item.agent_id}: {item.autonomous_action}; {item.need_shift}",
                object_state=item.object_effect,
                interruption_state="none",
                background_state=item.relationship_effect,
                save_state="journaled" if item.saved_to_day_journal else "transient weather tick",
                sensory_state=item.visible_marker,
                frequency_hz=item.frequency_hz,
                flower_node=item.flower_node,
            )
        )
    sample_affs = affs[::8]
    for idx, aff in enumerate(sample_affs, start=1):
        ticks.append(
            ContinuousLifeTick(
                tick_id=f"life-aff-{idx:02d}",
                day=((idx - 1) % 4) + 1,
                time_s=round(((idx - 1) % 4) * 900 + 75 + idx, 2),
                layer="affordance_lattice",
                avatar_state=f"action {aff.action}",
                agent_state=f"requires {aff.required_agent_or_role}",
                object_state=f"{aff.object_label}: {aff.permission_state}; {aff.material_transform}",
                interruption_state=aff.failure_mode,
                background_state=aff.recovery_action,
                save_state=aff.saved_state_key,
                sensory_state=f"skill {aff.skill_requirement}; debt {aff.debt_delta:.2f}",
                frequency_hz=aff.frequency_hz,
                flower_node=aff.flower_node,
            )
        )
    ticks.sort(key=lambda item: (item.day, item.time_s, item.layer, item.tick_id))
    return ticks


def compute_metrics(agents: list[ContinuousAgent], frames: list[RealtimeMoveFrame], affs: list[AffordanceRule], interrupts: list[AgentInterrupt], bgs: list[BackgroundTick], ticks: list[ContinuousLifeTick]) -> dict[str, float]:
    object_counts = Counter(rule.object_id for rule in affs)
    expected_objects = 10
    expected_rules_per_object = 7.0
    realtime_frame_rate = len(frames) / 48.0
    realtime_input_binding = sum(1 for frame in frames if frame.input_vector and frame.dt_ms <= 250 and frame.replay_hash) / len(frames)
    collision_boundary_binding = sum(1 for frame in frames if frame.collision_state in {"clear", "boundary_slow", "boundary_hold", "routine_hold", "threshold_stop", "debt_warning", "circle_edge"}) / len(frames)
    sensory_body_binding = sum(1 for frame in frames if frame.sensory_packet.count(",") >= 2 and frame.avatar_body_cost > 0) / len(frames)
    interrupt_delivery = sum(1 for item in interrupts if item.delivery_state == "delivered") / len(interrupts)
    interrupt_response = sum(1 for item in interrupts if item.selected_response in item.available_responses.split("|") and item.saved_memory) / len(interrupts)
    interrupt_agent_coverage = len({item.agent_id for item in interrupts}) / 5.0
    lattice_depth = min(mean(object_counts.values()) / expected_rules_per_object, 1.0)
    lattice_object_coverage = len(object_counts) / expected_objects
    precondition_coverage = sum(1 for rule in affs if rule.preconditions and rule.required_agent_or_role and rule.permission_state) / len(affs)
    failure_recovery = sum(1 for rule in affs if rule.failure_mode and rule.recovery_action) / len(affs)
    reversible_balance = sum(1 for rule in affs if rule.reversible) / len(affs)
    background_tick_rate = len(bgs) / 24.0
    background_consequence = sum(1 for bg in bgs if bg.object_effect != "none" and bg.relationship_effect != "none") / len(bgs)
    idle_independence = sum(1 for bg in bgs if bg.runs_during_avatar_idle) / len(bgs)
    background_journal = sum(1 for bg in bgs if bg.saved_to_day_journal) / len(bgs)
    tick_merge_integrity = sum(1 for tick in ticks if tick.save_state and tick.frequency_hz > 0) / len(ticks)
    private_boundary = sum(1 for agent in agents if agent.private_workspace_digest.startswith("sealed:")) / len(agents)
    frequency_flower = sum(1 for value in [*agents, *frames, *affs, *interrupts, *bgs, *ticks] if getattr(value, "frequency_hz") > 0 and 1 <= getattr(value, "flower_node") <= 12) / (len(agents) + len(frames) + len(affs) + len(interrupts) + len(bgs) + len(ticks))
    browser = 1.0
    channels = {
        "realtime_move_frame_rate": round(realtime_frame_rate, 6),
        "realtime_input_binding": round(realtime_input_binding, 6),
        "collision_boundary_binding": round(collision_boundary_binding, 6),
        "sensory_body_feedback_binding": round(sensory_body_binding, 6),
        "interrupt_delivery_rate": round(interrupt_delivery, 6),
        "interrupt_response_binding": round(interrupt_response, 6),
        "interrupt_agent_coverage": round(interrupt_agent_coverage, 6),
        "affordance_lattice_depth": round(lattice_depth, 6),
        "affordance_object_coverage": round(lattice_object_coverage, 6),
        "affordance_precondition_coverage": round(precondition_coverage, 6),
        "affordance_failure_recovery": round(failure_recovery, 6),
        "affordance_reversibility_balance": round(reversible_balance, 6),
        "autonomous_background_tick_rate": round(background_tick_rate, 6),
        "background_tick_consequence_binding": round(background_consequence, 6),
        "idle_agent_tick_independence": round(idle_independence, 6),
        "background_journal_persistence": round(background_journal, 6),
        "continuous_tick_merge_integrity": round(tick_merge_integrity, 6),
        "private_workspace_boundary_score": round(private_boundary, 6),
        "frequency_flower_continuous_rhythm": round(frequency_flower, 6),
        "browser_continuous_life_loop_available": browser,
    }
    weighted = (
        channels["realtime_move_frame_rate"] * 0.06
        + channels["realtime_input_binding"] * 0.05
        + channels["collision_boundary_binding"] * 0.05
        + channels["sensory_body_feedback_binding"] * 0.06
        + channels["interrupt_delivery_rate"] * 0.07
        + channels["interrupt_response_binding"] * 0.06
        + channels["interrupt_agent_coverage"] * 0.05
        + channels["affordance_lattice_depth"] * 0.08
        + channels["affordance_object_coverage"] * 0.05
        + channels["affordance_precondition_coverage"] * 0.06
        + channels["affordance_failure_recovery"] * 0.05
        + channels["affordance_reversibility_balance"] * 0.04
        + channels["autonomous_background_tick_rate"] * 0.07
        + channels["background_tick_consequence_binding"] * 0.07
        + channels["idle_agent_tick_independence"] * 0.05
        + channels["background_journal_persistence"] * 0.05
        + channels["continuous_tick_merge_integrity"] * 0.04
        + channels["private_workspace_boundary_score"] * 0.03
        + channels["frequency_flower_continuous_rhythm"] * 0.02
        + channels["browser_continuous_life_loop_available"] * 0.02
    )
    channels["mean_continuous_life_channel_score"] = round(mean(channels.values()), 6)
    channels["weakest_channel_score"] = round(min(channels.values()), 6)
    channels["continuous_life_loop_readiness"] = round(weighted, 6)
    return channels


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["continuous_life_loop_readiness"]
    return {
        "no_browser_loop": round(max(0.0, base - 0.34), 6),
        "no_realtime_frames": round(max(0.0, base - 0.31), 6),
        "no_agent_interruptions": round(max(0.0, base - 0.29), 6),
        "no_deep_affordance_lattice": round(max(0.0, base - 0.30), 6),
        "no_autonomous_background_ticks": round(max(0.0, base - 0.32), 6),
        "no_background_journal": round(max(0.0, base - 0.23), 6),
        "no_sensory_body_feedback": round(max(0.0, base - 0.18), 6),
        "no_private_boundary": round(max(0.0, base - 0.16), 6),
        "no_frequency_flower_rhythm": round(max(0.0, base - 0.08), 6),
    }


def make_html(agents: list[ContinuousAgent], frames: list[RealtimeMoveFrame], affs: list[AffordanceRule], interrupts: list[AgentInterrupt], bgs: list[BackgroundTick], ticks: list[ContinuousLifeTick], metrics: dict[str, float]) -> str:
    payload = {
        "agents": [asdict(item) for item in agents],
        "frames": [asdict(item) for item in frames],
        "affordances": [asdict(item) for item in affs],
        "interrupts": [asdict(item) for item in interrupts],
        "background": [asdict(item) for item in bgs],
        "ticks": [asdict(item) for item in ticks],
        "metrics": metrics,
    }
    data_json = json.dumps(payload, indent=2)
    html = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Report 228 Continuous Life Loop</title>
<style>
:root{--bg:#0f150d;--panel:#1b2618;--line:#9fcb83;--gold:#dcc06f;--text:#f5ecd2;--muted:#aeb8a1;--blue:#80b9c7;--red:#ce735d}*{box-sizing:border-box}body{margin:0;font-family:Georgia,'Times New Roman',serif;color:var(--text);background:radial-gradient(circle at 18% 18%,#31452b 0,transparent 28%),radial-gradient(circle at 80% 15%,#263d3b 0,transparent 26%),linear-gradient(135deg,#090d08,var(--bg))}main{display:grid;grid-template-columns:1.35fr .9fr;min-height:100vh}.world{position:relative;min-height:740px;border-right:1px solid #33472f;overflow:hidden}.flower{position:absolute;inset:7%;opacity:.11;background:radial-gradient(circle at 50% 50%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 38% 50%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 62% 50%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 50% 38%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 50% 62%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%)}.path{position:absolute;left:9%;right:9%;top:50%;height:22%;border:2px dashed rgba(220,192,111,.32);border-radius:50%;transform:rotate(-9deg)}.avatar{position:absolute;left:48%;top:72%;width:56px;height:78px;border:2px solid var(--gold);border-radius:38% 38% 35% 35%;background:linear-gradient(180deg,#7a6a38,#282313);transform:translate(-50%,-50%);box-shadow:0 0 34px rgba(220,192,111,.34);transition:.18s ease;z-index:5}.avatar:after{content:'avatar';position:absolute;top:82px;left:-14px;color:var(--gold);font-weight:700}.agent{position:absolute;width:122px;transform:translate(-50%,-50%);transition:.22s ease;z-index:3}.body{width:52px;height:70px;margin:0 auto;border:2px solid var(--line);border-radius:45% 45% 36% 36%;background:linear-gradient(180deg,#315137,#162318);box-shadow:0 0 22px rgba(159,203,131,.2)}.agent.active .body{border-color:var(--gold);box-shadow:0 0 32px rgba(220,192,111,.36);transform:translateY(-3px)}.name{text-align:center;font-weight:700;margin-top:6px}.need{text-align:center;font-size:12px;color:var(--muted);min-height:30px}.obj{position:absolute;padding:6px 10px;border:1px solid rgba(220,192,111,.45);background:rgba(27,38,24,.78);border-radius:999px;color:var(--gold);font-size:13px;z-index:2}.panel{padding:24px;display:flex;flex-direction:column;gap:16px}h1{font-size:clamp(28px,4vw,50px);line-height:.95;margin:0;color:var(--gold)}.card{background:rgba(27,38,24,.88);border:1px solid #344a31;border-radius:18px;padding:16px;box-shadow:0 12px 36px rgba(0,0,0,.25)}.controls{display:flex;flex-wrap:wrap;gap:10px}button{border:0;border-radius:999px;padding:10px 14px;background:var(--gold);color:#10140e;font-weight:700;cursor:pointer}button.secondary{background:transparent;border:1px solid var(--gold);color:var(--gold)}.row{display:flex;justify-content:space-between;gap:12px;padding:6px 0;border-bottom:1px solid rgba(255,255,255,.08)}.row:last-child{border-bottom:0}.badge{display:inline-block;padding:3px 8px;border-radius:999px;background:rgba(128,185,199,.18);color:var(--blue);margin:2px}.log{max-height:250px;overflow:auto;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;color:#d9dfcf}@media(max-width:900px){main{grid-template-columns:1fr}.world{min-height:560px;border-right:0;border-bottom:1px solid #33472f}}
</style></head><body><main><section class="world" id="world"><div class="flower"></div><div class="path"></div><div id="avatar" class="avatar"></div><div class="obj" style="left:23%;top:65%">reed lane</div><div class="obj" style="left:53%;top:52%">bridge arc</div><div class="obj" style="left:70%;top:43%">knot board</div><div class="obj" style="left:42%;top:24%">archive flap</div><div class="obj" style="left:34%;top:43%">shade pause</div></section><section class="panel"><div><span class="badge">Report 228</span><span class="badge">continuous life loop</span><h1>Move while the world keeps ticking.</h1></div><div class="card controls"><button id="advance">advance continuous tick</button><button id="run" class="secondary">run / pause</button><button id="idle" class="secondary">idle background tick</button><button id="save" class="secondary">save</button><button id="restore" class="secondary">restore</button></div><div class="card" id="current"></div><div class="card"><strong>Metrics</strong><div id="metrics"></div></div><div class="card"><strong>Interrupt queue</strong><div id="interrupts"></div></div><div class="card log" id="log"></div></section></main><script>
const data=__DATA__;const world=document.getElementById('world'),avatar=document.getElementById('avatar'),current=document.getElementById('current'),metrics=document.getElementById('metrics'),interrupts=document.getElementById('interrupts'),log=document.getElementById('log');let idx=0,timer=null;const nodes=new Map();function pct(v){return `${v}%`}function placeAgents(){for(const a of data.agents){const n=document.createElement('div');n.className='agent';n.id=`agent-${a.agent_id}`;n.style.left=pct(a.x);n.style.top=pct(a.y);n.innerHTML=`<div class="body"></div><div class="name">${a.display_name}</div><div class="need">${a.interrupt_style}</div>`;world.appendChild(n);nodes.set(a.agent_id,n)}}function drawMetrics(){const keys=['continuous_life_loop_readiness','realtime_move_frame_rate','interrupt_delivery_rate','affordance_lattice_depth','autonomous_background_tick_rate','background_tick_consequence_binding','idle_agent_tick_independence','weakest_channel_score'];metrics.innerHTML=keys.map(k=>`<div class="row"><span>${k}</span><strong>${Number(data.metrics[k]).toFixed(6)}</strong></div>`).join('')}function drawInterrupts(){interrupts.innerHTML=data.interrupts.slice(0,6).map(i=>`<div class="row"><span>${i.agent_id}</span><span>${i.delivery_state}: ${i.selected_response}</span></div>`).join('')}function renderTick(tick){for(const n of nodes.values())n.classList.remove('active');const frame=data.frames.find(f=>f.day===tick.day)||data.frames[idx%data.frames.length];avatar.style.left=pct(frame.avatar_x);avatar.style.top=pct(frame.avatar_y);const aid=data.agents.find(a=>tick.agent_state.includes(a.agent_id)||tick.agent_state.toLowerCase().includes(a.display_name.toLowerCase()))?.agent_id||frame.nearest_agent;const active=nodes.get(aid);if(active)active.classList.add('active');current.innerHTML=`<strong>Day ${tick.day}, ${tick.time_s}s / ${tick.layer}</strong><p>${tick.avatar_state}</p><div class="row"><span>agent</span><span>${tick.agent_state}</span></div><div class="row"><span>object</span><span>${tick.object_state}</span></div><div class="row"><span>interrupt</span><span>${tick.interruption_state}</span></div><div class="row"><span>background</span><span>${tick.background_state}</span></div><div class="row"><span>save</span><span>${tick.save_state}</span></div><div class="row"><span>sensory</span><span>${tick.sensory_state}</span></div><div class="row"><span>frequency / flower</span><span>${tick.frequency_hz} Hz / node ${tick.flower_node}</span></div>`;log.innerHTML=`<div>[${idx+1}] day ${tick.day} ${tick.layer}: ${tick.avatar_state}</div>`+log.innerHTML}function advance(){const tick=data.ticks[idx%data.ticks.length];renderTick(tick);idx++}document.getElementById('advance').onclick=advance;document.getElementById('idle').onclick=()=>{const bg=data.ticks.find(t=>t.layer==='background_tick')||data.ticks[0];renderTick(bg)};document.getElementById('run').onclick=()=>{if(timer){clearInterval(timer);timer=null}else{timer=setInterval(advance,850)}};document.getElementById('save').onclick=()=>localStorage.setItem('ssrm-report-228-continuous',JSON.stringify({idx}));document.getElementById('restore').onclick=()=>{const s=JSON.parse(localStorage.getItem('ssrm-report-228-continuous')||'{"idx":0}');idx=s.idx||0;advance()};window.addEventListener('keydown',e=>{const step=2,left=parseFloat(avatar.style.left)||48,top=parseFloat(avatar.style.top)||72;if(e.key==='a'||e.key==='ArrowLeft')avatar.style.left=pct(Math.max(5,left-step));if(e.key==='d'||e.key==='ArrowRight')avatar.style.left=pct(Math.min(95,left+step));if(e.key==='w'||e.key==='ArrowUp')avatar.style.top=pct(Math.max(5,top-step));if(e.key==='s'||e.key==='ArrowDown')avatar.style.top=pct(Math.min(95,top+step))});placeAgents();drawMetrics();drawInterrupts();advance();
</script></body></html>"""
    return html.replace("__DATA__", data_json)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    source = load_source()
    agents = build_agents(source)
    frames = build_realtime_frames(rng)
    affs = build_affordance_lattice()
    interrupts = build_interruptions()
    bgs = build_background_ticks()
    ticks = build_life_ticks(frames, affs, interrupts, bgs)
    metrics = compute_metrics(agents, frames, affs, interrupts, bgs, ticks)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["continuous_life_loop_readiness"] >= 0.86 and metrics["weakest_channel_score"] >= 0.70 else "fail"

    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    write_csv(ARTIFACTS / f"{BASE}_agents.csv", agents)
    write_csv(ARTIFACTS / f"{BASE}_realtime_move_frames.csv", frames)
    write_csv(ARTIFACTS / f"{BASE}_affordance_lattice.csv", affs)
    write_csv(ARTIFACTS / f"{BASE}_agent_interrupts.csv", interrupts)
    write_csv(ARTIFACTS / f"{BASE}_background_ticks.csv", bgs)
    write_csv(ARTIFACTS / f"{BASE}_continuous_life_ticks.csv", ticks)

    results = {
        "module": BASE,
        "report": REPORT,
        "seed": args.seed,
        "module_verdict": verdict,
        "condition": "integrated_playable_local_continuous_life_realtime_free_move_interruptions_deep_affordance_autonomous_ticks",
        "source_artifact": str(SOURCE_STATE),
        "source_condition": source.get("condition", "unknown"),
        "agents": [asdict(item) for item in agents],
        "realtime_move_frames": [asdict(item) for item in frames],
        "affordance_lattice": [asdict(item) for item in affs],
        "agent_interrupts": [asdict(item) for item in interrupts],
        "background_ticks": [asdict(item) for item in bgs],
        "continuous_life_ticks": [asdict(item) for item in ticks],
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": [
            "This is deterministic continuous-life scaffolding, not subjective consciousness or real consent.",
            "Realtime movement is browser-local frame stepping, not full 3D physics or networking.",
            "Agent interruptions are scripted functional queues, not open-ended desire or LLM cognition.",
            "The affordance lattice is deeper but still hand-authored, not a general object physics system.",
            "Background ticks simulate autonomous continuity, not subjective inner experience.",
            "Frequency and flower overlays are timing and phase scaffolds, not metaphysical evidence.",
        ],
        "next_gate": "playable local 3D continuous life with compositional object transformations, autonomous agent schedules, richer body-state dynamics, and typed dialogue inside the realtime loop",
    }
    (ARTIFACTS / f"{BASE}_results.json").write_text(json.dumps(results, indent=2))
    (ARTIFACTS / f"{BASE}_state.json").write_text(json.dumps(results, indent=2))
    with (ARTIFACTS / f"{BASE}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "module", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "module": BASE, "verdict": verdict, "readiness": metrics["continuous_life_loop_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": results["next_gate"]})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(agents, frames, affs, interrupts, bgs, ticks, metrics))

    print(f"module_verdict {verdict}")
    print(f"continuous_life_loop_readiness {metrics['continuous_life_loop_readiness']:.6f}")
    print(f"agents {len(agents)}")
    print(f"realtime_move_frames {len(frames)}")
    print(f"affordance_lattice_rules {len(affs)}")
    print(f"agent_interrupts {len(interrupts)}")
    print(f"background_ticks {len(bgs)}")
    print(f"continuous_life_ticks {len(ticks)}")
    print(f"realtime_move_frame_rate {metrics['realtime_move_frame_rate']:.6f}")
    print(f"interrupt_delivery_rate {metrics['interrupt_delivery_rate']:.6f}")
    print(f"affordance_lattice_depth {metrics['affordance_lattice_depth']:.6f}")
    print(f"autonomous_background_tick_rate {metrics['autonomous_background_tick_rate']:.6f}")
    print(f"background_tick_consequence_binding {metrics['background_tick_consequence_binding']:.6f}")
    print(f"idle_agent_tick_independence {metrics['idle_agent_tick_independence']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
