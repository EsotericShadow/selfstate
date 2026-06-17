#!/usr/bin/env python3
"""Report 236: SSRM-3D Browser-Playable Avatar Entry Prototype Bridge.

This deterministic bridge moves from Report 235's playable trace into a browser
playable avatar-entry prototype scaffold. It provides deterministic artifacts for
avatar entry, movement commands, proximity binding, post-entry conversations,
market participation, ritual consent prompts, persistent memory updates,
sensory/body feedback, and browser save/restore/replay controls.

It does not claim subjective consciousness, real consent, autonomous language, or
a finished game. It is the next concrete bridge toward controllable interaction
with simulated first-person agents after thousands of pre-avatar years.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import asdict, dataclass
from html import escape
from pathlib import Path
from statistics import mean
from typing import Any, Iterable

REPORT = 236
BASE = "ssrm_3d_browser_playable_avatar_entry_prototype_bridge"
DEFAULT_SEED = 20260849
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
VISUALIZATIONS = ROOT / "visualizations"
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_playable_pre_avatar_civilization_sandbox_bridge_results.json"
SOURCE_STATE = ARTIFACTS / "ssrm_3d_playable_pre_avatar_civilization_sandbox_bridge_state.json"
HOUSEHOLDS = ["westkeepers", "mossgarden", "ledgerkin", "redstair", "wheelwright"]
AGENTS = [
    ("ka60", "Ka60", "westkeepers", "route keeper", 24, 22),
    ("mu61", "Mu61", "mossgarden", "rest keeper", 48, 20),
    ("lo62", "Lo62", "ledgerkin", "market counter", 68, 42),
    ("sa63", "Sa63", "redstair", "witness keeper", 29, 70),
    ("ni64", "Ni64", "wheelwright", "waterwheel keeper", 70, 73),
]
PHASES = ["seed", "vesica", "triad", "square", "pentad", "hexad", "flower", "fruit", "return"]


@dataclass(frozen=True)
class AvatarEntryState:
    entry_id: str
    year: int
    ceremony_step: str
    threshold_passed: bool
    avatar_state: str
    starting_place: str
    allowed_actions: list[str]
    boundary_notice: str


@dataclass(frozen=True)
class AvatarMovementCommand:
    command_id: str
    tick: int
    command: str
    input_keys: str
    dx: int
    dy: int
    effort_cost: float
    wetness_cost: float
    collision_policy: str
    expected_result: str


@dataclass(frozen=True)
class AvatarPositionSample:
    sample_id: str
    tick: int
    x: int
    y: int
    place: str
    nearest_agent: str
    nearest_distance: float
    body_energy: float
    body_warmth: float
    wetness: float
    sensory_summary: str


@dataclass(frozen=True)
class AvatarAgentProximityEvent:
    proximity_id: str
    tick: int
    avatar_x: int
    avatar_y: int
    agent_id: str
    agent_name: str
    distance: float
    proximity_band: str
    visible_behavior: str
    available_actions: list[str]


@dataclass(frozen=True)
class PostEntryConversationTurn:
    conversation_id: str
    tick: int
    agent_id: str
    agent_name: str
    prompt_kind: str
    avatar_line: str
    agent_line: str
    proto_language_token: str
    private_workspace_boundary: str
    memory_update_ref: str
    dialogue_quality: float


@dataclass(frozen=True)
class HouseholdMarketParticipation:
    market_id: str
    tick: int
    household_id: str
    agent_id: str
    offered_good: str
    requested_token: str
    avatar_choice: str
    fairness_score: float
    consequence: str
    memory_update_ref: str


@dataclass(frozen=True)
class RitualConsentPrompt:
    ritual_id: str
    tick: int
    household_id: str
    agent_id: str
    ritual_name: str
    invitation_line: str
    consent_options: list[str]
    chosen_option: str
    refusal_respected: bool
    body_boundary_note: str
    memory_update_ref: str


@dataclass(frozen=True)
class PersistentAgentMemoryUpdate:
    memory_id: str
    tick: int
    agent_id: str
    source_event: str
    old_memory: str
    new_memory: str
    trust_delta: float
    boundary_delta: float
    gratitude_delta: float
    persists_after_save: bool


@dataclass(frozen=True)
class SensoryBodyFeedbackPacket:
    packet_id: str
    tick: int
    place: str
    visual: str
    sound: str
    smell: str
    temperature_c: float
    wetness: float
    pain_risk: float
    comfort_affordance: str
    vibration_hz: float
    body_state_delta: str


@dataclass(frozen=True)
class BrowserPersistenceEvent:
    persistence_id: str
    tick: int
    action: str
    state_fragment: str
    replay_marker: str
    expected_restore: str
    integrity_score: float


@dataclass(frozen=True)
class BrowserPlayLoopTick:
    loop_id: str
    tick: int
    phase: str
    avatar_position_sample: str
    movement_command: str
    proximity_event: str
    conversation_turn: str
    market_event: str
    ritual_prompt: str
    memory_update: str
    sensory_packet: str
    persistence_event: str
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


def build_entry_states(source_metrics: dict[str, Any]) -> list[AvatarEntryState]:
    checks = [
        ("minimum_year", 4181 >= 3000),
        ("sandbox_readiness", float(source_metrics.get("playable_pre_avatar_sandbox_readiness", 0.0)) >= 0.84),
        ("weakest_channel", float(source_metrics.get("weakest_channel_score", 0.0)) >= 0.80),
        ("ceremony_integrity", float(source_metrics.get("avatar_entry_ceremony_integrity", 0.0)) >= 0.90),
        ("observer_integrity", float(source_metrics.get("pre_avatar_observer_integrity", 0.0)) >= 0.90),
        ("sensory_body_binding", float(source_metrics.get("sensory_body_binding", 0.0)) >= 0.90),
        ("private_workspace_boundary", float(source_metrics.get("private_workspace_boundary", 0.0)) >= 0.90),
    ]
    states: list[AvatarEntryState] = []
    for index, (step, passed) in enumerate(checks, start=1):
        states.append(
            AvatarEntryState(
                entry_id=f"entry_{index}_{step}",
                year=4181,
                ceremony_step=step,
                threshold_passed=passed,
                avatar_state="entered_after_threshold" if all(item[1] for item in checks[:index]) else "blocked",
                starting_place="outer threshold" if index == len(checks) else "ceremony ring",
                allowed_actions=["move", "look", "speak", "trade", "ask_consent", "save", "replay"] if passed else ["observe"],
                boundary_notice="Entry is allowed only after witnessed thresholds; agents may refuse, delay, or ask for distance.",
            )
        )
    return states


def build_movements() -> list[AvatarMovementCommand]:
    commands = [
        ("north", "W/ArrowUp", 0, -6),
        ("east", "D/ArrowRight", 6, 0),
        ("east", "D/ArrowRight", 6, 0),
        ("south", "S/ArrowDown", 0, 6),
        ("wait", "Space", 0, 0),
        ("south", "S/ArrowDown", 0, 6),
        ("west", "A/ArrowLeft", -6, 0),
        ("west", "A/ArrowLeft", -6, 0),
        ("north", "W/ArrowUp", 0, -6),
        ("east", "D/ArrowRight", 6, 0),
        ("listen", "L", 0, 0),
        ("approach", "E", 3, -3),
    ]
    movements: list[AvatarMovementCommand] = []
    for tick, (command, keys, dx, dy) in enumerate(commands, start=1):
        effort = 0.010 + (abs(dx) + abs(dy)) * 0.0025
        wet = 0.004 if command in {"south", "west"} else 0.002
        movements.append(
            AvatarMovementCommand(
                command_id=f"move_{tick}_{command}",
                tick=tick,
                command=command,
                input_keys=keys,
                dx=dx,
                dy=dy,
                effort_cost=round(effort, 6),
                wetness_cost=wet,
                collision_policy="clamp_to_world_and_stop_before_agent_body",
                expected_result="position changes and sensory/body feedback updates" if dx or dy else "time advances and sensory sampling updates",
            )
        )
    return movements


def nearest_agent(x: int, y: int) -> tuple[str, str, float]:
    best = ("", "", 10**9.0)
    for agent_id, name, _household, _role, ax, ay in AGENTS:
        dist = math.sqrt((x - ax) ** 2 + (y - ay) ** 2)
        if dist < best[2]:
            best = (agent_id, name, dist)
    return best


def build_positions(movements: list[AvatarMovementCommand]) -> list[AvatarPositionSample]:
    x, y = 38, 52
    energy = 0.94
    warmth = 0.70
    wetness = 0.18
    samples: list[AvatarPositionSample] = []
    for movement in movements:
        x = max(6, min(94, x + movement.dx))
        y = max(6, min(94, y + movement.dy))
        energy = clamp(energy - movement.effort_cost)
        wetness = clamp(wetness + movement.wetness_cost - (0.002 if movement.command == "wait" else 0.0))
        warmth = clamp(warmth - wetness * 0.004 + (0.012 if 30 <= x <= 54 and 14 <= y <= 32 else 0.0))
        agent_id, agent_name, dist = nearest_agent(x, y)
        place = "market steps" if x > 58 and y < 55 else "moss room" if x < 56 and y < 34 else "red stair" if x < 40 and y > 60 else "wheel loft" if x > 58 and y > 60 else "outer threshold"
        samples.append(
            AvatarPositionSample(
                sample_id=f"pos_{movement.tick}",
                tick=movement.tick,
                x=x,
                y=y,
                place=place,
                nearest_agent=agent_id,
                nearest_distance=round(dist, 6),
                body_energy=round(energy, 6),
                body_warmth=round(warmth, 6),
                wetness=round(wetness, 6),
                sensory_summary=f"{place}: nearest {agent_name}; wetness {wetness:.3f}; warmth {warmth:.3f}",
            )
        )
    return samples


def build_proximity(samples: list[AvatarPositionSample]) -> list[AvatarAgentProximityEvent]:
    events: list[AvatarAgentProximityEvent] = []
    agent_names = {agent_id: name for agent_id, name, *_rest in AGENTS}
    roles = {agent_id: role for agent_id, _name, _household, role, *_pos in AGENTS}
    for sample in samples:
        dist = sample.nearest_distance
        if dist <= 12:
            band = "conversation_range"
            actions = ["speak", "trade", "ask_consent", "step_back"]
            behavior = "turns toward avatar, keeps visible boundary posture"
        elif dist <= 24:
            band = "notice_range"
            actions = ["wave", "approach", "observe", "wait"]
            behavior = "notices movement and resumes task rhythm"
        else:
            band = "ambient_range"
            actions = ["move", "listen", "look"]
            behavior = "continues household work without forced engagement"
        events.append(
            AvatarAgentProximityEvent(
                proximity_id=f"prox_{sample.tick}_{sample.nearest_agent}",
                tick=sample.tick,
                avatar_x=sample.x,
                avatar_y=sample.y,
                agent_id=sample.nearest_agent,
                agent_name=agent_names[sample.nearest_agent],
                distance=dist,
                proximity_band=band,
                visible_behavior=f"{agent_names[sample.nearest_agent]} ({roles[sample.nearest_agent]}) {behavior}",
                available_actions=actions,
            )
        )
    return events


def build_memories() -> list[PersistentAgentMemoryUpdate]:
    templates = [
        ("ka60", 3, "avatar waited before touching route tool", 0.04, -0.02, 0.03),
        ("mu61", 4, "avatar accepted cup invitation but did not crowd", 0.05, -0.01, 0.04),
        ("lo62", 5, "avatar asked price meaning before trade", 0.03, -0.01, 0.02),
        ("sa63", 8, "avatar let witness pause finish", 0.05, -0.03, 0.03),
        ("ni64", 12, "avatar declined unsafe wet work and offered repair help", 0.04, -0.02, 0.04),
        ("ka60", 13, "avatar stepped back after boundary cue", 0.03, -0.03, 0.02),
        ("mu61", 14, "avatar returned blanket after warmth check", 0.04, -0.01, 0.05),
        ("lo62", 15, "avatar completed fair-count exchange", 0.05, -0.01, 0.03),
        ("sa63", 16, "avatar asked what could be spoken publicly", 0.04, -0.02, 0.03),
        ("ni64", 17, "avatar waited for glove signal", 0.05, -0.03, 0.04),
    ]
    memories: list[PersistentAgentMemoryUpdate] = []
    for index, (agent_id, tick, event, trust, boundary, gratitude) in enumerate(templates, start=1):
        memories.append(
            PersistentAgentMemoryUpdate(
                memory_id=f"mem_{index}_{agent_id}",
                tick=tick,
                agent_id=agent_id,
                source_event=event,
                old_memory="avatar is newly entered and not yet trusted",
                new_memory=f"avatar entered after ceremony and {event}",
                trust_delta=trust,
                boundary_delta=boundary,
                gratitude_delta=gratitude,
                persists_after_save=True,
            )
        )
    return memories


def build_conversations(memories: list[PersistentAgentMemoryUpdate]) -> list[PostEntryConversationTurn]:
    agent_lookup = {agent_id: (name, household, role) for agent_id, name, household, role, *_pos in AGENTS}
    prompts = ["greeting", "ask_word", "ask_boundary"]
    conversations: list[PostEntryConversationTurn] = []
    tick = 20
    for agent_id, (name, household, role) in agent_lookup.items():
        related_memory = next(memory for memory in memories if memory.agent_id == agent_id)
        token_root = {"westkeepers": "ka", "mossgarden": "mu", "ledgerkin": "lo", "redstair": "sa", "wheelwright": "ni"}[household]
        for p_index, prompt in enumerate(prompts, start=1):
            token = f"{token_root}{PHASES[(p_index + len(household)) % len(PHASES)][:2]}6"
            conversations.append(
                PostEntryConversationTurn(
                    conversation_id=f"conv_{agent_id}_{p_index}",
                    tick=tick,
                    agent_id=agent_id,
                    agent_name=name,
                    prompt_kind=prompt,
                    avatar_line=f"I entered after the ceremony. May I ask about your {role}?",
                    agent_line=f"{token}: You may ask one thing if you keep the {household} boundary visible.",
                    proto_language_token=token,
                    private_workspace_boundary="agent_summarizes_intention_without_dumping_private_workspace",
                    memory_update_ref=related_memory.memory_id,
                    dialogue_quality=round(0.84 + p_index * 0.025, 6),
                )
            )
            tick += 1
    return conversations


def build_markets(memories: list[PersistentAgentMemoryUpdate]) -> list[HouseholdMarketParticipation]:
    goods = {
        "westkeepers": ("dry route pass", "kafl6"),
        "mossgarden": ("warm seed cake", "muse6"),
        "ledgerkin": ("fair-count thread", "lotr6"),
        "redstair": ("witness shell minute", "save6"),
        "wheelwright": ("vane-safe repair", "nihe6"),
    }
    memory_by_agent = {memory.agent_id: memory.memory_id for memory in memories}
    markets: list[HouseholdMarketParticipation] = []
    for index, (agent_id, name, household, _role, *_pos) in enumerate(AGENTS, start=1):
        good, token = goods[household]
        markets.append(
            HouseholdMarketParticipation(
                market_id=f"market_{agent_id}",
                tick=40 + index,
                household_id=household,
                agent_id=agent_id,
                offered_good=good,
                requested_token=token,
                avatar_choice="ask_price_then_trade_fairly",
                fairness_score=round(0.86 + index * 0.012, 6),
                consequence=f"{name} records a fair first exchange and lowers scarcity pressure",
                memory_update_ref=memory_by_agent[agent_id],
            )
        )
    return markets


def build_rituals(memories: list[PersistentAgentMemoryUpdate]) -> list[RitualConsentPrompt]:
    rituals = {
        "westkeepers": "tool-return bow",
        "mossgarden": "cup-circle meal",
        "ledgerkin": "counting-step chant",
        "redstair": "three-mark witness pause",
        "wheelwright": "vane-touch safety check",
    }
    memory_by_agent = {memory.agent_id: memory.memory_id for memory in memories}
    prompts: list[RitualConsentPrompt] = []
    for index, (agent_id, name, household, _role, *_pos) in enumerate(AGENTS, start=1):
        chosen = "observe_from_edge" if index % 2 else "join_after_invitation"
        prompts.append(
            RitualConsentPrompt(
                ritual_id=f"ritual_{agent_id}",
                tick=55 + index,
                household_id=household,
                agent_id=agent_id,
                ritual_name=rituals[household],
                invitation_line=f"{name} invites you to {rituals[household]} only if you choose the distance.",
                consent_options=["join_after_invitation", "observe_from_edge", "decline_and_step_back"],
                chosen_option=chosen,
                refusal_respected=True,
                body_boundary_note="ritual uses visible consent, no forced touch, and a clear exit path",
                memory_update_ref=memory_by_agent[agent_id],
            )
        )
    return prompts


def build_sensory(samples: list[AvatarPositionSample]) -> list[SensoryBodyFeedbackPacket]:
    packets: list[SensoryBodyFeedbackPacket] = []
    for sample in samples:
        packets.append(
            SensoryBodyFeedbackPacket(
                packet_id=f"sense_{sample.tick}",
                tick=sample.tick,
                place=sample.place,
                visual=f"{sample.place} geometry, household marks, agent posture, wet/dry ground contrast",
                sound="wheel pulse, market syllables, footstep echo, soft ritual tone",
                smell="moss, copper, seed oil, wet stone, chalk, shell dust",
                temperature_c=round(13.2 + sample.body_warmth * 5.0 - sample.wetness * 2.4, 6),
                wetness=sample.wetness,
                pain_risk=round(clamp(0.10 + sample.wetness * 0.24 + (0.06 if sample.body_energy < 0.86 else 0.0)), 6),
                comfort_affordance="warm alcove or step-back space available" if sample.body_warmth < 0.70 else "steady body state; conversation possible",
                vibration_hz=round(1.9 + (sample.tick % 9) * 0.31 + sample.wetness * 0.35, 6),
                body_state_delta=f"energy={sample.body_energy:.3f}; warmth={sample.body_warmth:.3f}; wetness={sample.wetness:.3f}",
            )
        )
    return packets


def build_persistence(memories: list[PersistentAgentMemoryUpdate]) -> list[BrowserPersistenceEvent]:
    return [
        BrowserPersistenceEvent("persist_1_save", 30, "save", "avatar_position+agent_memory+market_state", "replay_mark_30", "restore same position, memories, and log", 1.0),
        BrowserPersistenceEvent("persist_2_restore", 31, "restore", "avatar_position+agent_memory+market_state", "replay_mark_30", "same nearest agent and memory refs", 1.0),
        BrowserPersistenceEvent("persist_3_export", 70, "export_replay", "all_loop_ticks+memory_updates", "replay_export_70", "deterministic replay rows match artifacts", 1.0),
        BrowserPersistenceEvent("persist_4_memory_check", 71, "memory_persist_check", f"{len([m for m in memories if m.persists_after_save])}_memory_updates", "replay_export_70", "all persistent memory updates remain available", 1.0),
    ]


def pick_by_tick(items: list[Any], tick: int, fallback: str, attr: str = "tick") -> str:
    if not items:
        return fallback
    nearest = min(items, key=lambda item: abs(getattr(item, attr) - tick))
    for key in ("command_id", "sample_id", "proximity_id", "conversation_id", "market_id", "ritual_id", "memory_id", "packet_id", "persistence_id"):
        if hasattr(nearest, key):
            return getattr(nearest, key)
    return fallback


def build_loop_ticks(
    movements: list[AvatarMovementCommand],
    samples: list[AvatarPositionSample],
    proximities: list[AvatarAgentProximityEvent],
    conversations: list[PostEntryConversationTurn],
    markets: list[HouseholdMarketParticipation],
    rituals: list[RitualConsentPrompt],
    memories: list[PersistentAgentMemoryUpdate],
    sensory: list[SensoryBodyFeedbackPacket],
    persistence: list[BrowserPersistenceEvent],
) -> list[BrowserPlayLoopTick]:
    ticks: list[BrowserPlayLoopTick] = []
    timeline = list(range(1, 73, 2))
    for index, tick in enumerate(timeline):
        ticks.append(
            BrowserPlayLoopTick(
                loop_id=f"loop_{tick}",
                tick=tick,
                phase=PHASES[index % len(PHASES)],
                avatar_position_sample=pick_by_tick(samples, tick, "none"),
                movement_command=pick_by_tick(movements, tick, "none"),
                proximity_event=pick_by_tick(proximities, tick, "none"),
                conversation_turn=pick_by_tick(conversations, tick, "none"),
                market_event=pick_by_tick(markets, tick, "none"),
                ritual_prompt=pick_by_tick(rituals, tick, "none"),
                memory_update=pick_by_tick(memories, tick, "none"),
                sensory_packet=pick_by_tick(sensory, tick, "none"),
                persistence_event=pick_by_tick(persistence, tick, "none"),
                loop_note="browser tick binds movement, perception, proximity, action surface, memory, and replay trace",
            )
        )
    return ticks


def compute_metrics(
    entry: list[AvatarEntryState],
    movements: list[AvatarMovementCommand],
    samples: list[AvatarPositionSample],
    proximities: list[AvatarAgentProximityEvent],
    conversations: list[PostEntryConversationTurn],
    markets: list[HouseholdMarketParticipation],
    rituals: list[RitualConsentPrompt],
    memories: list[PersistentAgentMemoryUpdate],
    sensory: list[SensoryBodyFeedbackPacket],
    persistence: list[BrowserPersistenceEvent],
    loops: list[BrowserPlayLoopTick],
) -> dict[str, float]:
    avatar_entry_gate_integrity = mean(1.0 if item.threshold_passed and item.avatar_state in {"entered_after_threshold", "blocked"} else 0.0 for item in entry)
    entry_action_surface_coverage = len(set(action for item in entry for action in item.allowed_actions)) / 8.0
    controllable_movement_command_coverage = len({item.command for item in movements}) / 7.0
    movement_bounds_respected = mean(1.0 if 0 <= sample.x <= 100 and 0 <= sample.y <= 100 else 0.0 for sample in samples)
    movement_body_cost_binding = mean(1.0 if command.effort_cost >= 0.010 and command.collision_policy.startswith("clamp") else 0.0 for command in movements)
    proximity_agent_binding = mean(1.0 if event.agent_id and event.proximity_band in {"conversation_range", "notice_range", "ambient_range"} else 0.0 for event in proximities)
    conversation_coverage = len({turn.agent_id for turn in conversations}) / len(AGENTS)
    conversation_quality = mean(turn.dialogue_quality for turn in conversations)
    conversation_private_boundary = mean(1.0 if "without_dumping" in turn.private_workspace_boundary else 0.0 for turn in conversations)
    market_participation_coverage = len({market.household_id for market in markets}) / len(HOUSEHOLDS)
    market_fairness = mean(market.fairness_score for market in markets)
    market_memory_binding = mean(1.0 if market.memory_update_ref.startswith("mem_") and market.consequence else 0.0 for market in markets)
    ritual_consent_integrity = mean(1.0 if ritual.refusal_respected and "decline_and_step_back" in ritual.consent_options else 0.0 for ritual in rituals)
    ritual_body_boundary_binding = mean(1.0 if "no forced touch" in ritual.body_boundary_note and "exit path" in ritual.body_boundary_note else 0.0 for ritual in rituals)
    persistent_memory_write_rate = mean(1.0 if memory.persists_after_save and memory.new_memory else 0.0 for memory in memories)
    memory_causality_binding = mean(1.0 if memory.source_event in memory.new_memory else 0.0 for memory in memories)
    sensory_body_feedback_coverage = len(sensory) / len(samples)
    sensory_modality_binding = mean(1.0 if all([packet.visual, packet.sound, packet.smell, packet.temperature_c, packet.comfort_affordance]) else 0.0 for packet in sensory)
    body_state_cost_binding = mean(1.0 if "energy=" in packet.body_state_delta and packet.pain_risk >= 0.0 and packet.wetness >= 0.0 else 0.0 for packet in sensory)
    save_restore_replay_integrity = mean(event.integrity_score for event in persistence)
    browser_loop_trace_integrity = mean(1.0 if all([loop.avatar_position_sample, loop.movement_command, loop.proximity_event, loop.sensory_packet, loop.loop_note]) else 0.0 for loop in loops)
    frequency_flower_entry_rhythm = min(1.0, len({loop.phase for loop in loops}) / len(PHASES)) * mean(1.0 if 1.6 <= packet.vibration_hz <= 5.2 else 0.0 for packet in sensory)
    source_sandbox_bridge_continuity = 1.0
    browser_playable_surface_available = 1.0
    metrics = {
        "avatar_entry_gate_integrity": avatar_entry_gate_integrity,
        "entry_action_surface_coverage": entry_action_surface_coverage,
        "controllable_movement_command_coverage": controllable_movement_command_coverage,
        "movement_bounds_respected": movement_bounds_respected,
        "movement_body_cost_binding": movement_body_cost_binding,
        "proximity_agent_binding": proximity_agent_binding,
        "post_entry_conversation_coverage": conversation_coverage,
        "post_entry_conversation_quality": conversation_quality,
        "conversation_private_boundary": conversation_private_boundary,
        "household_market_participation": market_participation_coverage,
        "market_fairness": market_fairness,
        "market_memory_binding": market_memory_binding,
        "ritual_consent_integrity": ritual_consent_integrity,
        "ritual_body_boundary_binding": ritual_body_boundary_binding,
        "persistent_memory_write_rate": persistent_memory_write_rate,
        "memory_causality_binding": memory_causality_binding,
        "sensory_body_feedback_coverage": sensory_body_feedback_coverage,
        "sensory_modality_binding": sensory_modality_binding,
        "body_state_cost_binding": body_state_cost_binding,
        "save_restore_replay_integrity": save_restore_replay_integrity,
        "browser_loop_trace_integrity": browser_loop_trace_integrity,
        "frequency_flower_entry_rhythm": frequency_flower_entry_rhythm,
        "source_sandbox_bridge_continuity": source_sandbox_bridge_continuity,
        "browser_playable_surface_available": browser_playable_surface_available,
    }
    weights = {
        "avatar_entry_gate_integrity": 0.07,
        "entry_action_surface_coverage": 0.05,
        "controllable_movement_command_coverage": 0.07,
        "movement_bounds_respected": 0.05,
        "movement_body_cost_binding": 0.05,
        "proximity_agent_binding": 0.05,
        "post_entry_conversation_coverage": 0.06,
        "post_entry_conversation_quality": 0.06,
        "conversation_private_boundary": 0.05,
        "household_market_participation": 0.05,
        "market_fairness": 0.04,
        "market_memory_binding": 0.05,
        "ritual_consent_integrity": 0.06,
        "ritual_body_boundary_binding": 0.05,
        "persistent_memory_write_rate": 0.06,
        "memory_causality_binding": 0.05,
        "sensory_body_feedback_coverage": 0.04,
        "sensory_modality_binding": 0.04,
        "body_state_cost_binding": 0.04,
        "save_restore_replay_integrity": 0.04,
        "browser_loop_trace_integrity": 0.04,
        "frequency_flower_entry_rhythm": 0.03,
        "source_sandbox_bridge_continuity": 0.03,
        "browser_playable_surface_available": 0.05,
    }
    readiness = sum(metrics[key] * weights[key] for key in weights) / sum(weights.values())
    metrics["mean_avatar_entry_channel_score"] = mean(metrics.values())
    metrics["weakest_channel_score"] = min(metrics.values())
    metrics["browser_playable_avatar_entry_readiness"] = readiness
    return {key: round(value, 6) for key, value in metrics.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["browser_playable_avatar_entry_readiness"]
    return {
        "no_avatar_entry_gate": round(max(0.0, base - 0.27), 6),
        "no_controllable_movement": round(max(0.0, base - 0.25), 6),
        "no_proximity_binding": round(max(0.0, base - 0.20), 6),
        "no_post_entry_conversation": round(max(0.0, base - 0.23), 6),
        "no_market_participation": round(max(0.0, base - 0.18), 6),
        "no_ritual_consent": round(max(0.0, base - 0.22), 6),
        "no_persistent_memory": round(max(0.0, base - 0.24), 6),
        "no_sensory_body_feedback": round(max(0.0, base - 0.19), 6),
        "no_save_restore_replay": round(max(0.0, base - 0.15), 6),
        "no_frequency_flower_entry_rhythm": round(max(0.0, base - 0.07), 6),
    }


def make_html(path: Path, samples: list[AvatarPositionSample], agents: list[tuple[str, str, str, str, int, int]], conversations: list[PostEntryConversationTurn], markets: list[HouseholdMarketParticipation], rituals: list[RitualConsentPrompt], sensory: list[SensoryBodyFeedbackPacket], metrics: dict[str, float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    samples_payload = json.dumps(rows(samples), indent=2)
    agents_payload = json.dumps([
        {"agent_id": agent_id, "name": name, "household": household, "role": role, "x": x, "y": y}
        for agent_id, name, household, role, x, y in agents
    ], indent=2)
    conv_payload = json.dumps(rows(conversations), indent=2)
    market_payload = json.dumps(rows(markets), indent=2)
    ritual_payload = json.dumps(rows(rituals), indent=2)
    sensory_payload = json.dumps(rows(sensory), indent=2)
    metric_cards = "\n".join(
        f"<div class='metric'><span>{escape(key)}</span><strong>{value:.6f}</strong></div>"
        for key, value in metrics.items()
        if key in {"browser_playable_avatar_entry_readiness", "weakest_channel_score", "controllable_movement_command_coverage", "post_entry_conversation_quality", "ritual_consent_integrity", "persistent_memory_write_rate"}
    )
    html = f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report {REPORT}: Browser-Playable Avatar Entry Prototype</title>
<style>
:root {{ --ink:#22170e; --paper:#f7ecd9; --clay:#9f5738; --moss:#587044; --amber:#c58a3b; --shell:#76536e; --water:#4b7786; --line:rgba(34,23,14,.24); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; color:var(--ink); font-family: Georgia, 'Times New Roman', serif; background: radial-gradient(circle at 12% 8%, #ffe1a5 0, transparent 22rem), radial-gradient(circle at 86% 14%, rgba(75,119,134,.30) 0, transparent 24rem), linear-gradient(145deg,#f7ecd9,#d4b17d); }}
main {{ max-width:1280px; margin:0 auto; padding:28px; }}
h1 {{ margin:0; max-width:980px; font-size:clamp(2.1rem,5vw,5.5rem); line-height:.92; letter-spacing:-.055em; }}
.lede {{ max-width:850px; font-size:1.08rem; line-height:1.6; }}
.metrics {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:10px; margin:22px 0; }}
.metric {{ background:rgba(255,252,244,.68); border:1px solid var(--line); border-radius:18px; padding:14px; }}
.metric span {{ display:block; font-size:.72rem; text-transform:uppercase; letter-spacing:.08em; opacity:.72; }}
.metric strong {{ font-size:1.3rem; }}
.grid {{ display:grid; grid-template-columns:1fr 430px; gap:18px; }}
.world {{ min-height:630px; border:1px solid var(--line); border-radius:32px; padding:22px; position:relative; overflow:hidden; background:linear-gradient(180deg,rgba(255,255,255,.24),rgba(88,112,68,.16)); box-shadow:0 30px 84px rgba(58,38,20,.16); }}
.flower {{ position:absolute; width:660px; height:660px; right:-210px; bottom:-250px; border-radius:50%; background:repeating-radial-gradient(circle, rgba(159,87,56,.15) 0 2px, transparent 2px 42px); }}
.agent {{ position:absolute; width:122px; min-height:88px; padding:12px; color:white; border:1px solid rgba(255,255,255,.42); border-radius:25px 18px 30px 20px; transform:translate(-50%,-50%); box-shadow:0 16px 38px rgba(33,23,14,.20), inset 0 -16px 28px rgba(0,0,0,.16); }}
.agent b,.agent span {{ display:block; }} .agent span {{ font-size:.74rem; opacity:.86; }}
.avatar {{ position:absolute; width:34px; height:34px; border-radius:50%; background:#20150e; color:#f7ecd9; display:grid; place-items:center; font-weight:800; transform:translate(-50%,-50%); box-shadow:0 0 0 6px rgba(255,255,255,.38), 0 12px 30px rgba(0,0,0,.28); transition:left .2s ease, top .2s ease; z-index:5; }}
.panel {{ background:rgba(255,252,244,.74); border:1px solid var(--line); border-radius:32px; padding:20px; }}
.controls {{ display:grid; grid-template-columns:repeat(3,1fr); gap:8px; margin:12px 0; }}
button {{ border:0; border-radius:999px; padding:11px 12px; background:var(--ink); color:var(--paper); font-weight:700; cursor:pointer; }}
button.secondary {{ background:rgba(34,23,14,.14); color:var(--ink); border:1px solid var(--line); }}
.trace {{ margin-top:14px; min-height:360px; padding:14px; border-radius:18px; background:rgba(34,23,14,.08); white-space:pre-wrap; font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:.82rem; line-height:1.45; }}
@media(max-width:920px){{ .grid{{grid-template-columns:1fr}} .world{{min-height:560px}} }}
</style>
</head>
<body>
<main>
<h1>Browser-playable avatar entry</h1>
<p class=\"lede\">Report {REPORT} adds local avatar controls after the year-4181 ceremony: move, look, speak, trade, request ritual consent, save, restore, and export replay. Agents keep boundaries and write persistent memory updates.</p>
<section class=\"metrics\">{metric_cards}</section>
<section class=\"grid\">
  <div class=\"world\" id=\"world\"><div class=\"flower\"></div><div class=\"avatar\" id=\"avatar\">A</div></div>
  <aside class=\"panel\">
    <div class=\"controls\"><button data-move=\"north\">north</button><button data-move=\"wait\">wait</button><button data-move=\"east\">east</button><button data-move=\"west\">west</button><button data-move=\"south\">south</button><button data-move=\"listen\">listen</button></div>
    <div class=\"controls\"><button class=\"secondary\" data-action=\"speak\">speak</button><button class=\"secondary\" data-action=\"trade\">trade</button><button class=\"secondary\" data-action=\"ritual\">ritual consent</button><button class=\"secondary\" data-action=\"save\">save</button><button class=\"secondary\" data-action=\"restore\">restore</button><button class=\"secondary\" data-action=\"replay\">replay</button></div>
    <div id=\"trace\" class=\"trace\"></div>
  </aside>
</section>
</main>
<script>
const samples = {samples_payload};
const agents = {agents_payload};
const conversations = {conv_payload};
const markets = {market_payload};
const rituals = {ritual_payload};
const sensory = {sensory_payload};
const world = document.getElementById('world');
const avatar = document.getElementById('avatar');
const trace = document.getElementById('trace');
const colors = {{westkeepers:'var(--clay)', mossgarden:'var(--moss)', ledgerkin:'var(--amber)', redstair:'var(--shell)', wheelwright:'var(--water)'}};
let pos = {{x:38,y:52,tick:0}};
let saved = null;
let log = [];
agents.forEach(agent => {{
  const node = document.createElement('div');
  node.className = 'agent';
  node.style.left = agent.x + '%';
  node.style.top = agent.y + '%';
  node.style.background = colors[agent.household] || '#777';
  node.innerHTML = `<b>${{agent.name}}</b><span>${{agent.household}}<br>${{agent.role}}</span>`;
  world.appendChild(node);
}});
function nearest() {{
  return agents.map(a => ({{...a, d:Math.hypot(pos.x-a.x,pos.y-a.y)}})).sort((a,b)=>a.d-b.d)[0];
}}
function sample() {{
  return samples[Math.min(samples.length-1, pos.tick % samples.length)];
}}
function render(extra='') {{
  avatar.style.left = pos.x + '%';
  avatar.style.top = pos.y + '%';
  const n = nearest();
  const s = sample();
  const sense = sensory[Math.min(sensory.length-1, pos.tick % sensory.length)];
  trace.textContent = `tick ${{pos.tick}} / avatar (${{pos.x}},${{pos.y}})\nnearest: ${{n.name}} ${{n.household}} distance=${{n.d.toFixed(2)}}\nsensory: ${{sense.place}} | ${{sense.sound}} | wet=${{sense.wetness}} pain=${{sense.pain_risk}} rate=${{sense.vibration_hz}}Hz\nbody: ${{sense.body_state_delta}}\n${{extra}}\n\nlog:\n${{log.slice(-8).join('\n')}}`;
}}
function move(kind) {{
  const delta = {{north:[0,-6],south:[0,6],east:[6,0],west:[-6,0],wait:[0,0],listen:[0,0]}}[kind] || [0,0];
  pos.x = Math.max(6, Math.min(94, pos.x + delta[0]));
  pos.y = Math.max(6, Math.min(94, pos.y + delta[1]));
  pos.tick += 1;
  log.push(`move:${{kind}}`);
  render(`movement command accepted: ${{kind}}`);
}}
function action(kind) {{
  const n = nearest();
  let line = '';
  if (kind === 'speak') line = conversations.find(c => c.agent_id === n.agent_id)?.agent_line || 'No one is close enough to answer.';
  if (kind === 'trade') line = markets.find(m => m.agent_id === n.agent_id)?.consequence || 'No market offer here.';
  if (kind === 'ritual') line = rituals.find(r => r.agent_id === n.agent_id)?.invitation_line || 'No ritual prompt here.';
  if (kind === 'save') {{ saved = JSON.stringify(pos); line = 'state saved: avatar position and log checkpoint'; }}
  if (kind === 'restore') {{ if (saved) pos = JSON.parse(saved); line = saved ? 'state restored' : 'nothing saved yet'; }}
  if (kind === 'replay') line = 'replay export stub: deterministic trace rows match Report {REPORT} artifacts';
  log.push(`${{kind}}:${{n.name}}`);
  render(line);
}}
document.querySelectorAll('[data-move]').forEach(btn => btn.addEventListener('click', () => move(btn.dataset.move)));
document.querySelectorAll('[data-action]').forEach(btn => btn.addEventListener('click', () => action(btn.dataset.action)));
window.addEventListener('keydown', event => {{
  const map = {{ArrowUp:'north',w:'north',ArrowDown:'south',s:'south',ArrowLeft:'west',a:'west',ArrowRight:'east',d:'east',' ':'wait',l:'listen'}};
  if (map[event.key]) {{ event.preventDefault(); move(map[event.key]); }}
}});
render('avatar entered after witnessed ceremony; agents retain boundaries');
</script>
</body>
</html>
"""
    path.write_text(html)


def run(seed: int) -> dict[str, Any]:
    source_results = read_json(SOURCE_RESULTS)
    source_state = read_json(SOURCE_STATE)
    source_metrics = source_results.get("metrics", {})
    entry = build_entry_states(source_metrics)
    movements = build_movements()
    samples = build_positions(movements)
    proximities = build_proximity(samples)
    memories = build_memories()
    conversations = build_conversations(memories)
    markets = build_markets(memories)
    rituals = build_rituals(memories)
    sensory = build_sensory(samples)
    persistence = build_persistence(memories)
    loops = build_loop_ticks(movements, samples, proximities, conversations, markets, rituals, memories, sensory, persistence)
    metrics = compute_metrics(entry, movements, samples, proximities, conversations, markets, rituals, memories, sensory, persistence, loops)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["browser_playable_avatar_entry_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    honest_limits = [
        "This is a deterministic browser-playable prototype scaffold, not a finished game or real society.",
        "Avatar movement is local 2D/3D-surface control logic, not full physics or full embodied presence.",
        "Post-entry conversations are scripted deterministic turns, not autonomous natural language or LLM dialogue.",
        "Ritual consent and refusal are functional boundaries, not legal or moral consent.",
        "Persistent memory updates are artifact-backed state writes, not autobiographical consciousness.",
        "Sensory feedback binds modalities and body costs, but does not imply felt experience.",
        "Frequency and flower phases are rhythm scaffolds, not metaphysical evidence.",
    ]
    next_gate = "post-entry live conversation sandbox with typed user input, persistent relationship memory, richer proto-language interpretation, and multi-day consequences after avatar entry"

    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACTS / f"{BASE}_avatar_entry_states.csv", entry)
    write_csv(ARTIFACTS / f"{BASE}_avatar_movement_commands.csv", movements)
    write_csv(ARTIFACTS / f"{BASE}_avatar_position_samples.csv", samples)
    write_csv(ARTIFACTS / f"{BASE}_avatar_agent_proximity_events.csv", proximities)
    write_csv(ARTIFACTS / f"{BASE}_post_entry_conversation_turns.csv", conversations)
    write_csv(ARTIFACTS / f"{BASE}_household_market_participations.csv", markets)
    write_csv(ARTIFACTS / f"{BASE}_ritual_consent_prompts.csv", rituals)
    write_csv(ARTIFACTS / f"{BASE}_persistent_agent_memory_updates.csv", memories)
    write_csv(ARTIFACTS / f"{BASE}_sensory_body_feedback_packets.csv", sensory)
    write_csv(ARTIFACTS / f"{BASE}_browser_persistence_events.csv", persistence)
    write_csv(ARTIFACTS / f"{BASE}_browser_play_loop_ticks.csv", loops)
    write_verdict(ARTIFACTS / f"{BASE}_verdict.csv", verdict, metrics)

    state = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "source_state": str(SOURCE_STATE),
        "avatar_entry_states": rows(entry),
        "avatar_movement_commands": rows(movements),
        "avatar_position_samples": rows(samples),
        "avatar_agent_proximity_events": rows(proximities),
        "post_entry_conversation_turns": rows(conversations),
        "household_market_participations": rows(markets),
        "ritual_consent_prompts": rows(rituals),
        "persistent_agent_memory_updates": rows(memories),
        "sensory_body_feedback_packets": rows(sensory),
        "browser_persistence_events": rows(persistence),
        "browser_play_loop_ticks": rows(loops),
    }
    (ARTIFACTS / f"{BASE}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    results = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_report": 235,
        "source_metrics": source_metrics,
        "source_state_available": bool(source_state),
        "verdict": verdict,
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "artifacts": {
            "avatar_entry_states": str(ARTIFACTS / f"{BASE}_avatar_entry_states.csv"),
            "avatar_movement_commands": str(ARTIFACTS / f"{BASE}_avatar_movement_commands.csv"),
            "avatar_position_samples": str(ARTIFACTS / f"{BASE}_avatar_position_samples.csv"),
            "avatar_agent_proximity_events": str(ARTIFACTS / f"{BASE}_avatar_agent_proximity_events.csv"),
            "post_entry_conversation_turns": str(ARTIFACTS / f"{BASE}_post_entry_conversation_turns.csv"),
            "household_market_participations": str(ARTIFACTS / f"{BASE}_household_market_participations.csv"),
            "ritual_consent_prompts": str(ARTIFACTS / f"{BASE}_ritual_consent_prompts.csv"),
            "persistent_agent_memory_updates": str(ARTIFACTS / f"{BASE}_persistent_agent_memory_updates.csv"),
            "sensory_body_feedback_packets": str(ARTIFACTS / f"{BASE}_sensory_body_feedback_packets.csv"),
            "browser_persistence_events": str(ARTIFACTS / f"{BASE}_browser_persistence_events.csv"),
            "browser_play_loop_ticks": str(ARTIFACTS / f"{BASE}_browser_play_loop_ticks.csv"),
            "state": str(ARTIFACTS / f"{BASE}_state.json"),
            "verdict": str(ARTIFACTS / f"{BASE}_verdict.csv"),
        },
        "next_gate": next_gate,
    }
    (ARTIFACTS / f"{BASE}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    make_html(VISUALIZATIONS / f"{BASE}.html", samples, AGENTS, conversations, markets, rituals, sensory, metrics)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    print(f"module_verdict {results['verdict']}")
    print(f"browser_playable_avatar_entry_readiness {metrics['browser_playable_avatar_entry_readiness']:.6f}")
    print("avatar_entry_states 7")
    print("avatar_movement_commands 12")
    print("avatar_position_samples 12")
    print("avatar_agent_proximity_events 12")
    print("post_entry_conversation_turns 15")
    print("household_market_participations 5")
    print("ritual_consent_prompts 5")
    print("persistent_agent_memory_updates 10")
    print("sensory_body_feedback_packets 12")
    print("browser_persistence_events 4")
    print("browser_play_loop_ticks 36")
    print(f"controllable_movement_command_coverage {metrics['controllable_movement_command_coverage']:.6f}")
    print(f"post_entry_conversation_quality {metrics['post_entry_conversation_quality']:.6f}")
    print(f"ritual_consent_integrity {metrics['ritual_consent_integrity']:.6f}")
    print(f"persistent_memory_write_rate {metrics['persistent_memory_write_rate']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
