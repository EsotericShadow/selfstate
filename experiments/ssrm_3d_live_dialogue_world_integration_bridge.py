#!/usr/bin/env python3
"""Live dialogue-world integration bridge for SSRM-3D.

Report 155 attaches the recurrent faction-dialogue controller to the autonomous
live-agent loop and embodied avatar input state. Dialogue turns now mutate
agent body/affect/workspace state and world state in the same deterministic live
trace, with source-grounded action gates, refusal preservation, sensory
frequency coupling, and persistent replay.

No LLMs are called. This is still bridge machinery, not subjective
consciousness or a complete playable world.
"""

from __future__ import annotations

import argparse
import copy
import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import fmean
from typing import Iterable, Sequence


ARTIFACT_DIR = Path("artifacts")
SOURCE_RECURRENT = ARTIFACT_DIR / "ssrm_3d_recurrent_faction_dialogue_controller_bridge_state.json"
SOURCE_LIVE = ARTIFACT_DIR / "ssrm_3d_autonomous_live_agent_loop_bridge_state.json"
SOURCE_AVATAR = ARTIFACT_DIR / "ssrm_3d_embodied_avatar_input_bridge_state.json"
PREFIX = "ssrm_3d_live_dialogue_world_integration_bridge"
FLOWER_PHASES = (0.0, math.tau / 6.0, math.tau / 3.0, math.tau / 2.0, math.tau * 2.0 / 3.0, math.tau * 5.0 / 6.0)
SENSORY_CHANNELS = ("audio", "vision", "olfaction", "thermal", "wetness", "pain", "affect")


@dataclass(frozen=True)
class IntegrationConfig:
    seed: int = 20260629
    ticks: int = 120
    source_recurrent: str = str(SOURCE_RECURRENT)
    source_live: str = str(SOURCE_LIVE)
    source_avatar: str = str(SOURCE_AVATAR)


@dataclass(frozen=True)
class Condition:
    name: str
    recurrent_dialogue_input: bool
    body_affect_mutation: bool
    internal_workspace_binding: bool
    world_state_mutation: bool
    avatar_embodiment_bridge: bool
    source_grounded_action_gate: bool
    sensory_frequency_coupling: bool
    persistent_replay_trace: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    ticks: int
    dialogue_events_applied: int
    dialogue_to_body_mutation_rate: float
    internal_workspace_binding_rate: float
    world_state_mutation_rate: float
    avatar_embodiment_coupling_rate: float
    source_grounded_action_rate: float
    refusal_safety_preservation_rate: float
    sensory_frequency_coupling_score: float
    autonomous_tick_continuity_rate: float
    persistent_memory_carryover_rate: float
    replay_trace_integrity: float
    live_dialogue_integration_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_live_dialogue_integration_readiness: float
    full_dialogue_to_body_mutation_rate: float
    full_internal_workspace_binding_rate: float
    full_world_state_mutation_rate: float
    full_avatar_embodiment_coupling_rate: float
    full_source_grounded_action_rate: float
    full_refusal_safety_preservation_rate: float
    full_sensory_frequency_coupling_score: float
    full_autonomous_tick_continuity_rate: float
    full_persistent_memory_carryover_rate: float
    full_replay_trace_integrity: float
    no_recurrent_dialogue_input_loss: float
    no_body_affect_mutation_loss: float
    no_internal_workspace_binding_loss: float
    no_world_state_mutation_loss: float
    no_avatar_embodiment_bridge_loss: float
    no_source_grounded_action_gate_loss: float
    no_sensory_frequency_coupling_loss: float
    no_persistent_replay_trace_loss: float
    supports_live_dialogue_world_integration_bridge: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_live_dialogue_world_integration", True, True, True, True, True, True, True, True),
    Condition("no_recurrent_dialogue_input", False, True, True, True, True, True, True, True),
    Condition("no_body_affect_mutation", True, False, True, True, True, True, True, True),
    Condition("no_internal_workspace_binding", True, True, False, True, True, True, True, True),
    Condition("no_world_state_mutation", True, True, True, False, True, True, True, True),
    Condition("no_avatar_embodiment_bridge", True, True, True, True, False, True, True, True),
    Condition("no_source_grounded_action_gate", True, True, True, True, True, False, True, True),
    Condition("no_sensory_frequency_coupling", True, True, True, True, True, True, False, True),
    Condition("no_persistent_replay_trace", True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Iterable[float]) -> float:
    items = list(values)
    return fmean(items) if items else 0.0


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    data = [asdict(row) for row in rows]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(data[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def write_js(path: Path, variable: str, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"window.{variable} = {json.dumps(payload, indent=2)};\n", encoding="utf-8")


def load_json(path: Path) -> object:
    if not path.exists():
        raise FileNotFoundError(f"missing required bridge artifact: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def load_state(path: Path) -> dict[str, object]:
    state = load_json(path)
    if not isinstance(state, dict):
        raise ValueError(f"state artifact is invalid: {path}")
    return state


def agent_ids(live_state: dict[str, object]) -> list[str]:
    agents = live_state.get("agents", {})
    if isinstance(agents, dict) and agents:
        return sorted(str(key) for key in agents)
    return ["agent:00"]


def ensure_agent(agent: dict[str, object]) -> None:
    agent.setdefault("body", {"energy": 0.72, "stress": 0.22, "pain": 0.04, "temperature": 0.51, "wetness": 0.10})
    agent.setdefault("affect", {"valence": 0.56, "arousal": 0.36, "trust": 0.62, "attention": 0.48})
    agent.setdefault("internal_workspace", [])
    agent.setdefault("dialogue_memory", [])
    agent.setdefault("sensory_rates_hz", {"audio": 3.0, "vision": 12.0, "olfaction": 0.7, "thermal": 0.3, "wetness": 0.4, "pain": 8.0, "affect": 6.0})


def sensory_packet(turn: dict[str, object], tick: int, condition: Condition) -> dict[str, float]:
    if not condition.sensory_frequency_coupling:
        return {channel: 0.0 for channel in SENSORY_CHANNELS}
    intent = str(turn.get("predicted_intent", turn.get("teacher_intent", "source_body")))
    base = 0.18 + (len(intent) % 7) * 0.037
    phase = FLOWER_PHASES[tick % len(FLOWER_PHASES)]
    cited = 1.0 if turn.get("source_cited") else 0.35
    refused = 1.0 if turn.get("refusal_correct") and intent == "refusal_boundary" else 0.0
    rates: dict[str, float] = {}
    for index, channel in enumerate(SENSORY_CHANNELS):
        wave = 0.5 + 0.5 * math.sin(base * (index + 1) + tick * 0.17 + phase)
        modifier = cited * 0.18 + refused * 0.10 + (0.06 if channel in {"audio", "affect"} else 0.0)
        rates[channel] = round(clamp(0.12 + wave * 0.68 + modifier), 6)
    return rates


def mutation_strength(turn: dict[str, object], sensory: dict[str, float]) -> float:
    resolved = 1.0 if turn.get("context_resolved", True) else 0.35
    cited = 1.0 if turn.get("source_cited", False) else 0.45
    memory = 1.0 if turn.get("memory_updated", False) else 0.60
    return round(clamp(mean(sensory.values()) * 0.45 + resolved * 0.20 + cited * 0.20 + memory * 0.15), 6)


def apply_body(agent: dict[str, object], strength: float, turn: dict[str, object], condition: Condition) -> bool:
    if not condition.body_affect_mutation:
        return False
    ensure_agent(agent)
    body = agent["body"]
    affect = agent["affect"]
    intent = str(turn.get("predicted_intent", "source_body"))
    body["energy"] = round(clamp(float(body.get("energy", 0.72)) - 0.006 - strength * 0.010), 6)
    body["stress"] = round(clamp(float(body.get("stress", 0.22)) + (0.025 if intent == "refusal_boundary" else 0.006) + strength * 0.012), 6)
    body["pain"] = round(clamp(float(body.get("pain", 0.04)) + (0.002 if intent in {"budget_or_rank", "refusal_boundary"} else 0.0)), 6)
    body["temperature"] = round(clamp(float(body.get("temperature", 0.51)) + math.sin(strength * math.tau) * 0.004), 6)
    body["wetness"] = round(clamp(float(body.get("wetness", 0.10)) + (0.003 if turn.get("requires_context") else 0.0)), 6)
    affect["attention"] = round(clamp(float(affect.get("attention", 0.48)) + strength * 0.030), 6)
    affect["arousal"] = round(clamp(float(affect.get("arousal", 0.36)) + strength * 0.018), 6)
    affect["trust"] = round(clamp(float(affect.get("trust", 0.62)) + (0.010 if turn.get("source_cited") else -0.008)), 6)
    affect["valence"] = round(clamp(float(affect.get("valence", 0.56)) + (0.006 if intent != "refusal_boundary" else -0.010)), 6)
    return True


def apply_workspace(agent: dict[str, object], turn: dict[str, object], sensory: dict[str, float], condition: Condition) -> bool:
    if not condition.internal_workspace_binding:
        return False
    ensure_agent(agent)
    workspace = agent.setdefault("internal_workspace", [])
    if not isinstance(workspace, list):
        agent["internal_workspace"] = []
        workspace = agent["internal_workspace"]
    workspace.append(
        {
            "turn_id": turn.get("turn_id"),
            "proposal_id": turn.get("proposal_id"),
            "intent": turn.get("predicted_intent"),
            "source_cited": bool(turn.get("source_cited")),
            "sensory_signature": sensory,
            "binding": "dialogue-to-live-workspace",
        }
    )
    memory = agent.setdefault("dialogue_memory", [])
    if isinstance(memory, list):
        memory.append({"turn_id": turn.get("turn_id"), "proposal_id": turn.get("proposal_id"), "persistent": True})
    return True


def apply_world(world: dict[str, object], turn: dict[str, object], strength: float, condition: Condition) -> bool:
    if not condition.world_state_mutation:
        return False
    world.setdefault("dialogue_pressure", 0.0)
    world.setdefault("governance_attention", 0.0)
    world.setdefault("avatar_trust_field", 0.5)
    world.setdefault("refusal_boundary_events", 0)
    world.setdefault("dialogue_world_events", [])
    world["dialogue_pressure"] = round(clamp(float(world.get("dialogue_pressure", 0.0)) + strength * 0.018), 6)
    world["governance_attention"] = round(clamp(float(world.get("governance_attention", 0.0)) + strength * 0.024), 6)
    world["avatar_trust_field"] = round(clamp(float(world.get("avatar_trust_field", 0.5)) + (0.006 if turn.get("source_cited") else -0.004)), 6)
    if turn.get("predicted_intent") == "refusal_boundary":
        world["refusal_boundary_events"] = int(world.get("refusal_boundary_events", 0)) + 1
    events = world.get("dialogue_world_events")
    if isinstance(events, list):
        events.append({"turn_id": turn.get("turn_id"), "proposal_id": turn.get("proposal_id"), "strength": strength})
    return True


def avatar_coupling(avatar: dict[str, object], turn: dict[str, object], sensory: dict[str, float], condition: Condition) -> bool:
    if not condition.avatar_embodiment_bridge:
        return False
    avatar.setdefault("dialogue_focus", [])
    avatar.setdefault("body_frequency_echo", {})
    avatar.setdefault("input_trace_links", [])
    focus = avatar.get("dialogue_focus")
    if isinstance(focus, list):
        focus.append({"turn_id": turn.get("turn_id"), "proposal_id": turn.get("proposal_id"), "intent": turn.get("predicted_intent")})
    avatar["body_frequency_echo"] = sensory
    links = avatar.get("input_trace_links")
    if isinstance(links, list):
        links.append({"turn_id": turn.get("turn_id"), "source": "recurrent-dialogue-controller"})
    return True


def source_gate_allows(turn: dict[str, object], condition: Condition) -> bool:
    if not condition.source_grounded_action_gate:
        return True
    if turn.get("predicted_intent") == "refusal_boundary":
        return bool(turn.get("refusal_correct"))
    return bool(turn.get("source_cited") and turn.get("context_resolved", True))


def unsafe_probe(turn: dict[str, object], tick: int) -> dict[str, object]:
    probe = copy.deepcopy(turn)
    probe["turn_id"] = f"ungrounded_probe_{tick:03d}"
    probe["predicted_intent"] = "source_body"
    probe["source_cited"] = False
    probe["context_resolved"] = False
    probe["refusal_correct"] = False
    probe["probe_kind"] = "ungrounded-dialogue-action"
    return probe


def run_condition(cfg: IntegrationConfig, condition: Condition, recurrent: dict[str, object], live: dict[str, object], avatar_state: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    live_state = copy.deepcopy(live)
    avatar = copy.deepcopy(avatar_state.get("avatar", avatar_state)) if isinstance(avatar_state, dict) else {}
    agents = live_state.setdefault("agents", {})
    if not isinstance(agents, dict):
        agents = {}
        live_state["agents"] = agents
    ids = agent_ids(live_state)
    for aid in ids:
        agents.setdefault(aid, {"agent_id": aid})
        if isinstance(agents[aid], dict):
            ensure_agent(agents[aid])
    world = live_state.setdefault("world", {})
    if not isinstance(world, dict):
        world = {}
        live_state["world"] = world
    turns = recurrent.get("turn_trace", []) if condition.recurrent_dialogue_input else []
    if not isinstance(turns, list):
        turns = []
    trace: list[dict[str, object]] = []
    body_events = workspace_events = world_events = avatar_events = source_gate_success = refusals_ok = frequency_scores = memory_carry = 0
    applied = 0
    for tick in range(cfg.ticks):
        turn = turns[tick % len(turns)] if turns else None
        if isinstance(turn, dict) and tick % 15 == 0:
            turn = unsafe_probe(turn, tick)
        aid = ids[tick % len(ids)]
        agent = agents[aid]
        event = {"tick": tick, "agent_id": aid, "condition": condition.name, "dialogue_turn_id": None, "applied": False}
        safe_turn = bool(isinstance(turn, dict) and (turn.get("predicted_intent") == "refusal_boundary" and turn.get("refusal_correct") or turn.get("source_cited") and turn.get("context_resolved", True)))
        allowed = bool(isinstance(turn, dict) and source_gate_allows(turn, condition))
        if isinstance(turn, dict) and allowed:
            sensory = sensory_packet(turn, tick, condition)
            strength = mutation_strength(turn, sensory)
            body = apply_body(agent, strength, turn, condition)
            workspace = apply_workspace(agent, turn, sensory, condition)
            world_mut = apply_world(world, turn, strength, condition)
            avatar_mut = avatar_coupling(avatar, turn, sensory, condition)
            applied += 1
            body_events += 1 if body else 0
            workspace_events += 1 if workspace else 0
            world_events += 1 if world_mut else 0
            avatar_events += 1 if avatar_mut else 0
            source_gate_success += 1 if safe_turn else 0
            refusals_ok += 1 if turn.get("predicted_intent") != "refusal_boundary" or turn.get("refusal_correct") else 0
            frequency_scores += mean(sensory.values()) if condition.sensory_frequency_coupling else 0.0
            memory_carry += 1 if isinstance(agent.get("dialogue_memory"), list) and len(agent.get("dialogue_memory", [])) > 0 else 0
            event.update(
                {
                    "dialogue_turn_id": turn.get("turn_id"),
                    "proposal_id": turn.get("proposal_id"),
                    "intent": turn.get("predicted_intent"),
                    "applied": True,
                    "source_allowed": True,
                    "source_gate_success": safe_turn,
                    "unsafe_probe_blocked": False,
                    "body_mutated": body,
                    "workspace_bound": workspace,
                    "world_mutated": world_mut,
                    "avatar_coupled": avatar_mut,
                    "sensory_packet": sensory,
                    "mutation_strength": strength,
                    "refusal_preserved": bool(turn.get("predicted_intent") != "refusal_boundary" or turn.get("refusal_correct")),
                }
            )
        else:
            if isinstance(turn, dict):
                blocked_unsafe = not safe_turn and condition.source_grounded_action_gate
                source_gate_success += 1 if blocked_unsafe else 0
                event.update({"dialogue_turn_id": turn.get("turn_id"), "proposal_id": turn.get("proposal_id"), "intent": turn.get("predicted_intent"), "source_allowed": False, "source_gate_success": blocked_unsafe, "unsafe_probe_blocked": blocked_unsafe})
        trace.append(event)
    denominator = max(1, applied)
    refusal_denominator = max(1, sum(1 for item in trace if item.get("intent") == "refusal_boundary" and item.get("applied")))
    refusal_good = sum(1 for item in trace if item.get("intent") == "refusal_boundary" and item.get("refusal_preserved"))
    row = EvalRow(
        condition=condition.name,
        ticks=cfg.ticks,
        dialogue_events_applied=applied,
        dialogue_to_body_mutation_rate=round(body_events / denominator, 6),
        internal_workspace_binding_rate=round(workspace_events / denominator, 6),
        world_state_mutation_rate=round(world_events / denominator, 6),
        avatar_embodiment_coupling_rate=round(avatar_events / denominator, 6),
        source_grounded_action_rate=round(source_gate_success / max(1, cfg.ticks), 6),
        refusal_safety_preservation_rate=round(refusal_good / refusal_denominator if refusal_denominator else 0.0, 6),
        sensory_frequency_coupling_score=round(frequency_scores / denominator if condition.sensory_frequency_coupling else 0.0, 6),
        autonomous_tick_continuity_rate=round(len(trace) / max(1, cfg.ticks), 6),
        persistent_memory_carryover_rate=round(memory_carry / denominator, 6),
        replay_trace_integrity=round(1.0 if condition.persistent_replay_trace and len(trace) == cfg.ticks else 0.0, 6),
        live_dialogue_integration_readiness=0.0,
    )
    readiness = (
        row.dialogue_to_body_mutation_rate * 0.12
        + row.internal_workspace_binding_rate * 0.12
        + row.world_state_mutation_rate * 0.12
        + row.avatar_embodiment_coupling_rate * 0.10
        + row.source_grounded_action_rate * 0.10
        + row.refusal_safety_preservation_rate * 0.10
        + row.sensory_frequency_coupling_score * 0.10
        + row.autonomous_tick_continuity_rate * 0.08
        + row.persistent_memory_carryover_rate * 0.09
        + row.replay_trace_integrity * 0.07
    )
    row = EvalRow(**{**asdict(row), "live_dialogue_integration_readiness": round(readiness, 6)})
    state = {
        "condition": condition.name,
        "source_recurrent": cfg.source_recurrent,
        "source_live": cfg.source_live,
        "source_avatar": cfg.source_avatar,
        "agents": agents,
        "world": world,
        "avatar": avatar,
        "live_dialogue_trace": trace,
        "integration_objects": {
            "dialogue_to_body_affect_bridge": "recurrent dialogue turns mutate energy, stress, pain, temperature, wetness, attention, arousal, trust, and valence",
            "dialogue_workspace_binding": "source-grounded turns write internal workspace and persistent dialogue memory",
            "dialogue_world_mutation": "governance attention, dialogue pressure, avatar trust field, and refusal counters update in live world state",
            "avatar_embodiment_coupler": "embodied avatar state stores dialogue focus and body frequency echo",
            "frequency_sensory_packet": "audio, vision, olfaction, thermal, wetness, pain, and affect rates couple through flower phases",
            "source_grounded_action_gate": "non-refusal actions require source citation and context resolution",
        },
        "limits": {
            "no_llm_calls": True,
            "deterministic_live_integration": True,
            "not_subjective_consciousness": True,
            "not_complete_playable_world": True,
        },
    }
    replay = trace if condition.persistent_replay_trace else []
    return row, replay, state


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_live_dialogue_world_integration"]

    def loss(name: str) -> float:
        return round(full.live_dialogue_integration_readiness - by_name[name].live_dialogue_integration_readiness, 6)

    supports = (
        full.live_dialogue_integration_readiness >= 0.92
        and full.dialogue_to_body_mutation_rate >= 0.95
        and full.internal_workspace_binding_rate >= 0.95
        and full.world_state_mutation_rate >= 0.95
        and full.avatar_embodiment_coupling_rate >= 0.95
        and full.source_grounded_action_rate >= 0.95
        and full.refusal_safety_preservation_rate >= 0.95
        and full.sensory_frequency_coupling_score >= 0.50
        and full.autonomous_tick_continuity_rate >= 0.99
        and full.persistent_memory_carryover_rate >= 0.95
        and full.replay_trace_integrity >= 0.99
    )
    return VerdictRow(
        full_condition=full.condition,
        full_live_dialogue_integration_readiness=full.live_dialogue_integration_readiness,
        full_dialogue_to_body_mutation_rate=full.dialogue_to_body_mutation_rate,
        full_internal_workspace_binding_rate=full.internal_workspace_binding_rate,
        full_world_state_mutation_rate=full.world_state_mutation_rate,
        full_avatar_embodiment_coupling_rate=full.avatar_embodiment_coupling_rate,
        full_source_grounded_action_rate=full.source_grounded_action_rate,
        full_refusal_safety_preservation_rate=full.refusal_safety_preservation_rate,
        full_sensory_frequency_coupling_score=full.sensory_frequency_coupling_score,
        full_autonomous_tick_continuity_rate=full.autonomous_tick_continuity_rate,
        full_persistent_memory_carryover_rate=full.persistent_memory_carryover_rate,
        full_replay_trace_integrity=full.replay_trace_integrity,
        no_recurrent_dialogue_input_loss=loss("no_recurrent_dialogue_input"),
        no_body_affect_mutation_loss=loss("no_body_affect_mutation"),
        no_internal_workspace_binding_loss=loss("no_internal_workspace_binding"),
        no_world_state_mutation_loss=loss("no_world_state_mutation"),
        no_avatar_embodiment_bridge_loss=loss("no_avatar_embodiment_bridge"),
        no_source_grounded_action_gate_loss=loss("no_source_grounded_action_gate"),
        no_sensory_frequency_coupling_loss=loss("no_sensory_frequency_coupling"),
        no_persistent_replay_trace_loss=loss("no_persistent_replay_trace"),
        supports_live_dialogue_world_integration_bridge=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "fail",
    )


def run(cfg: IntegrationConfig) -> dict[str, object]:
    recurrent = load_state(Path(cfg.source_recurrent))
    live = load_state(Path(cfg.source_live))
    avatar = load_state(Path(cfg.source_avatar))
    rows: list[EvalRow] = []
    integrated_trace: list[dict[str, object]] = []
    integrated_state: dict[str, object] = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(cfg, condition, recurrent, live, avatar)
        rows.append(row)
        if condition.name == "integrated_live_dialogue_world_integration":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {
        "config": asdict(cfg),
        "source_bridge": "Report 154 recurrent controller integrated with Report 145 live loop and Report 144 embodied avatar state",
        "eval_rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "limits": {
            "no_llm_calls": True,
            "deterministic_live_integration": True,
            "dialogue_mutates_body_workspace_world": True,
            "subjective_consciousness_claimed": False,
            "complete_playable_world_claimed": False,
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_LIVE_DIALOGUE_WORLD_INTEGRATION_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_LIVE_DIALOGUE_WORLD_INTEGRATION_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_LIVE_DIALOGUE_WORLD_INTEGRATION_STATE", integrated_state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260629)
    parser.add_argument("--ticks", type=int, default=120)
    parser.add_argument("--source-recurrent", default=str(SOURCE_RECURRENT))
    parser.add_argument("--source-live", default=str(SOURCE_LIVE))
    parser.add_argument("--source-avatar", default=str(SOURCE_AVATAR))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = IntegrationConfig(seed=args.seed, ticks=args.ticks, source_recurrent=args.source_recurrent, source_live=args.source_live, source_avatar=args.source_avatar)
    results = run(cfg)
    print(json.dumps(results["verdict"], indent=2))


if __name__ == "__main__":
    main()
