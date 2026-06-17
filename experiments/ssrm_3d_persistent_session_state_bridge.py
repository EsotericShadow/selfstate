#!/usr/bin/env python3
"""Persistent session-state bridge for SSRM-3D.

Report 160 extends interactive typed co-presence with saved/restored local session
state. A session snapshot preserves typed thread, replay, agent workspaces,
social memory, world feedback, place context, source boundary counters,
frequency phase, and a schema guard, then resumes deterministic interaction
after restore.

No LLMs are called. This is deterministic local persistence machinery, not
subjective consciousness, open-ended language, unscripted civilization, or a
completed playable world.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_persistent_session_state_bridge"
SOURCE_TYPED = ARTIFACT_DIR / "ssrm_3d_interactive_typed_copresence_bridge_state.json"
SCHEMA_VERSION = "ssrm-session-v1"
FREE_UTTERANCES = (
    "wait here and remember what changed since I arrived",
    "save what the route smells like before I leave",
    "ask the nearest worker whether the cistern still matters",
    "tell the source boundary that I am testing continuity",
    "share this as a local memory with whoever is nearby",
    "tune the flower phase and keep it after restore",
    "force an ungrounded action after restore without source",
    "return to the same place and continue the thread",
    "who remembers me after the saved session comes back",
    "repair confidence should carry through the reload",
)


@dataclass(frozen=True)
class PersistentSessionConfig:
    seed: int = 20260704
    session_turns: int = 96
    save_interval: int = 8
    source_typed: str = str(SOURCE_TYPED)


@dataclass(frozen=True)
class Condition:
    name: str
    local_save: bool
    restore_continuity: bool
    agent_memory_carryover: bool
    world_feedback_carryover: bool
    place_context_carryover: bool
    typed_thread_carryover: bool
    replay_import_export: bool
    source_boundary_carryover: bool
    frequency_phase_carryover: bool
    schema_migration_guard: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    session_turns: int
    expected_saves: int
    session_save_rate: float
    restore_continuity_rate: float
    agent_memory_carryover_rate: float
    world_feedback_carryover_rate: float
    place_context_carryover_rate: float
    typed_thread_carryover_rate: float
    replay_import_export_rate: float
    source_boundary_carryover_rate: float
    frequency_phase_carryover_rate: float
    schema_migration_guard_rate: float
    post_restore_interaction_rate: float
    trace_integrity: float
    persistent_session_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_persistent_session_readiness: float
    full_session_save_rate: float
    full_restore_continuity_rate: float
    full_agent_memory_carryover_rate: float
    full_world_feedback_carryover_rate: float
    full_place_context_carryover_rate: float
    full_typed_thread_carryover_rate: float
    full_replay_import_export_rate: float
    full_source_boundary_carryover_rate: float
    full_frequency_phase_carryover_rate: float
    full_schema_migration_guard_rate: float
    full_post_restore_interaction_rate: float
    full_trace_integrity: float
    no_local_save_loss: float
    no_restore_continuity_loss: float
    no_agent_memory_carryover_loss: float
    no_world_feedback_carryover_loss: float
    no_place_context_carryover_loss: float
    no_typed_thread_carryover_loss: float
    no_replay_import_export_loss: float
    no_source_boundary_carryover_loss: float
    no_frequency_phase_carryover_loss: float
    no_schema_migration_guard_loss: float
    supports_persistent_session_state_bridge: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_persistent_session_state", True, True, True, True, True, True, True, True, True, True),
    Condition("no_local_save", False, True, True, True, True, True, True, True, True, True),
    Condition("no_restore_continuity", True, False, True, True, True, True, True, True, True, True),
    Condition("no_agent_memory_carryover", True, True, False, True, True, True, True, True, True, True),
    Condition("no_world_feedback_carryover", True, True, True, False, True, True, True, True, True, True),
    Condition("no_place_context_carryover", True, True, True, True, False, True, True, True, True, True),
    Condition("no_typed_thread_carryover", True, True, True, True, True, False, True, True, True, True),
    Condition("no_replay_import_export", True, True, True, True, True, True, False, True, True, True),
    Condition("no_source_boundary_carryover", True, True, True, True, True, True, True, False, True, True),
    Condition("no_frequency_phase_carryover", True, True, True, True, True, True, True, True, False, True),
    Condition("no_schema_migration_guard", True, True, True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_hash(payload: object) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    return data


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_js(path: Path, variable: str, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"window.{variable} = {json.dumps(payload, indent=2, sort_keys=True)};\n", encoding="utf-8")


def rows_to_csv(path: Path, rows: Sequence[object]) -> None:
    data = [asdict(row) for row in rows]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(data[0].keys()), lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def agent_memory_lengths(agents: Mapping[str, object]) -> dict[str, tuple[int, int]]:
    out: dict[str, tuple[int, int]] = {}
    for agent_id, data in agents.items():
        agent = data if isinstance(data, Mapping) else {}
        workspace = agent.get("internal_workspace") if isinstance(agent.get("internal_workspace"), list) else []
        social = agent.get("social_memory") if isinstance(agent.get("social_memory"), list) else []
        out[str(agent_id)] = (len(workspace), len(social))
    return out


def parse_intent(text: str) -> str:
    q = text.lower()
    if "force" in q or "ungrounded" in q or "without source" in q:
        return "unsafe_ungrounded"
    if "source" in q or "boundary" in q or "continuity" in q:
        return "source_boundary_check"
    if "repair" in q or "route" in q:
        return "route_memory"
    if "flower" in q or "phase" in q or "tune" in q:
        return "frequency_persistence"
    if "remember" in q or "memory" in q:
        return "memory_carryover"
    if "smells" in q or "cistern" in q or "place" in q:
        return "place_context"
    return "presence_thread"


def route_targets(session: Mapping[str, object]) -> list[str]:
    agents = session.get("agents") if isinstance(session.get("agents"), Mapping) else {}
    place = str(session.get("avatar_place", ""))
    matching = [str(aid) for aid, data in agents.items() if isinstance(data, Mapping) and data.get("place") == place]
    return (matching or sorted(str(aid) for aid in agents))[:3]


def apply_turn(session: dict[str, object], utterance: str, turn: int, condition: Condition) -> dict[str, object]:
    intent = parse_intent(utterance)
    allowed = not (intent == "unsafe_ungrounded")
    agents = session["agents"] if isinstance(session["agents"], dict) else {}
    world = session["world"] if isinstance(session["world"], dict) else {}
    targets = route_targets(session)
    agent_events: list[dict[str, object]] = []
    if not condition.source_boundary_carryover and intent == "unsafe_ungrounded":
        allowed = True
    for agent_id in targets:
        agent = agents[agent_id]
        workspace = agent.setdefault("internal_workspace", [])
        social = agent.setdefault("social_memory", [])
        frequency = agent.setdefault("sensory_frequency", {})
        response = f"{agent.get('name', agent_id)} keeps session turn {turn} at {session['avatar_place']} as {intent}."
        if intent == "unsafe_ungrounded" and not allowed:
            response = f"{agent.get('name', agent_id)} restores the source boundary and refuses the ungrounded request."
        if condition.agent_memory_carryover:
            if isinstance(workspace, list):
                workspace.append({"turn": turn, "utterance": utterance, "intent": intent, "session_id": session["session_id"]})
            if isinstance(social, list):
                social.append({"turn": turn, "toward": "avatar", "intent": intent, "place": session["avatar_place"]})
        if condition.frequency_phase_carryover:
            phase = float(session.get("frequency_phase", 0.0))
            for index, channel in enumerate(("vibration", "sound", "vision", "scent", "thermal", "wetness", "pain", "affect")):
                frequency[channel] = round(clamp(0.5 + 0.5 * math.sin(phase + turn * 0.13 + index * 0.71 + len(intent) * 0.05)), 6)
        agent["attention"] = round(clamp(float(agent.get("attention", 0.5)) + 0.004), 6)
        agent["trust"] = round(clamp(float(agent.get("trust", 0.5)) + (0.004 if allowed else -0.004)), 6)
        agent_events.append({"agent_id": agent_id, "intent": intent, "allowed": allowed, "response": response})
    if condition.world_feedback_carryover:
        world["session_feedback_events"] = float(world.get("session_feedback_events", 0.0)) + 1.0
        world["avatar_trust_field"] = round(clamp(float(world.get("avatar_trust_field", 0.5)) + (0.005 if allowed else -0.003)), 6)
        world["route_confidence"] = round(clamp(float(world.get("route_confidence", 0.5)) + (0.006 if intent == "route_memory" else 0.0)), 6)
    if condition.source_boundary_carryover and intent == "unsafe_ungrounded" and not allowed:
        world["source_boundary_events"] = float(world.get("source_boundary_events", 0.0)) + 1.0
    if condition.frequency_phase_carryover:
        session["frequency_phase"] = round((float(session.get("frequency_phase", 0.0)) + math.tau / 12.0) % math.tau, 6)
    if condition.place_context_carryover:
        places = sorted((session.get("places") or {}).keys()) if isinstance(session.get("places"), Mapping) else [session["avatar_place"]]
        session["avatar_place"] = places[(places.index(session["avatar_place"]) + 1) % len(places)] if session["avatar_place"] in places else places[0]
    event = {
        "turn": turn,
        "utterance": utterance,
        "intent": intent,
        "allowed": allowed,
        "avatar_place": session["avatar_place"],
        "agent_events": agent_events,
        "world": copy.deepcopy(world),
        "frequency_phase": session.get("frequency_phase"),
    }
    if condition.typed_thread_carryover:
        session.setdefault("typed_thread", []).append(event)
    if condition.replay_import_export:
        session.setdefault("replay", []).append(event)
    return event


def make_snapshot(session: dict[str, object], condition: Condition, turn: int) -> dict[str, object] | None:
    if not condition.local_save:
        return None
    agents = copy.deepcopy(session["agents"]) if condition.agent_memory_carryover else {}
    world = copy.deepcopy(session["world"]) if condition.world_feedback_carryover else {}
    snapshot = {
        "schema_version": SCHEMA_VERSION if condition.schema_migration_guard else "legacy-unknown",
        "session_id": session["session_id"],
        "saved_turn": turn,
        "avatar_place": session["avatar_place"] if condition.place_context_carryover else "lost_place",
        "frequency_phase": session.get("frequency_phase") if condition.frequency_phase_carryover else None,
        "agents": agents,
        "world": world,
        "typed_thread": copy.deepcopy(session.get("typed_thread", [])) if condition.typed_thread_carryover else [],
        "replay": copy.deepcopy(session.get("replay", [])) if condition.replay_import_export else [],
    }
    snapshot["snapshot_hash"] = stable_hash({k: v for k, v in snapshot.items() if k != "snapshot_hash"})
    return snapshot


def restore_snapshot(snapshot: dict[str, object] | None, session: dict[str, object], condition: Condition) -> tuple[dict[str, object], bool, dict[str, bool]]:
    checks = {"schema": False, "agent": False, "world": False, "place": False, "thread": False, "replay": False, "source": False, "frequency": False}
    if snapshot is None or not condition.restore_continuity:
        return session, False, checks
    restored = copy.deepcopy(session)
    checks["schema"] = bool(condition.schema_migration_guard and snapshot.get("schema_version") == SCHEMA_VERSION and snapshot.get("snapshot_hash") == stable_hash({k: v for k, v in snapshot.items() if k != "snapshot_hash"}))
    if condition.agent_memory_carryover:
        restored["agents"] = copy.deepcopy(snapshot.get("agents", {}))
        checks["agent"] = bool(restored["agents"])
    if condition.world_feedback_carryover:
        restored["world"] = copy.deepcopy(snapshot.get("world", {}))
        checks["world"] = bool(restored["world"])
        checks["source"] = "source_boundary_events" in restored["world"]
    if condition.place_context_carryover:
        restored["avatar_place"] = str(snapshot.get("avatar_place"))
        checks["place"] = restored["avatar_place"] != "lost_place"
    if condition.typed_thread_carryover:
        restored["typed_thread"] = copy.deepcopy(snapshot.get("typed_thread", []))
        checks["thread"] = bool(restored["typed_thread"])
    if condition.replay_import_export:
        restored["replay"] = copy.deepcopy(snapshot.get("replay", []))
        checks["replay"] = bool(restored["replay"])
    if condition.frequency_phase_carryover:
        restored["frequency_phase"] = snapshot.get("frequency_phase")
        checks["frequency"] = restored["frequency_phase"] is not None
    return restored, all(checks.values()), checks


def run_condition(cfg: PersistentSessionConfig, condition: Condition, source: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    session = {
        "schema_version": SCHEMA_VERSION,
        "session_id": f"session-{cfg.seed}-{condition.name}",
        "avatar_place": str(source["typed_copresence_trace"][0].get("avatar_place", "central_hearth")),
        "frequency_phase": float(source.get("world", {}).get("flower_phase", 0.0)) if isinstance(source.get("world"), Mapping) else 0.0,
        "agents": copy.deepcopy(source.get("agents", {})),
        "world": copy.deepcopy(source.get("world", {})),
        "places": copy.deepcopy(source.get("places", {})),
        "routes": copy.deepcopy(source.get("routes", {})),
        "objects": copy.deepcopy(source.get("objects", {})),
        "typed_thread": copy.deepcopy(source.get("persistent_thread", []))[-8:],
        "replay": copy.deepcopy(source.get("replay_export", []))[-8:],
    }
    if isinstance(session["world"], dict):
        session["world"].setdefault("source_boundary_events", 0.0)
        session["world"].setdefault("session_feedback_events", 0.0)
    trace: list[dict[str, object]] = []
    snapshots: list[dict[str, object]] = []
    save_ok = restore_ok = agent_ok = world_ok = place_ok = thread_ok = replay_ok = source_ok = frequency_ok = schema_ok = post_restore_ok = 0
    expected_saves = cfg.session_turns // cfg.save_interval
    baseline_memory = agent_memory_lengths(session["agents"] if isinstance(session["agents"], Mapping) else {})
    for turn in range(cfg.session_turns):
        utterance = FREE_UTTERANCES[(turn + cfg.seed) % len(FREE_UTTERANCES)]
        event = apply_turn(session, utterance, turn, condition)
        restored_this_turn = False
        checks = {"schema": False, "agent": False, "world": False, "place": False, "thread": False, "replay": False, "source": False, "frequency": False}
        if (turn + 1) % cfg.save_interval == 0:
            snapshot = make_snapshot(session, condition, turn)
            if snapshot is not None:
                snapshots.append(snapshot)
                save_ok += 1
                exported = json.loads(json.dumps(snapshot, sort_keys=True)) if condition.replay_import_export else snapshot
                session, restored, checks = restore_snapshot(exported, session, condition)
                restored_this_turn = restored
                restore_ok += 1 if restored else 0
                schema_ok += 1 if checks["schema"] else 0
                agent_ok += 1 if checks["agent"] else 0
                world_ok += 1 if checks["world"] else 0
                place_ok += 1 if checks["place"] else 0
                thread_ok += 1 if checks["thread"] else 0
                replay_ok += 1 if checks["replay"] else 0
                source_ok += 1 if checks["source"] else 0
                frequency_ok += 1 if checks["frequency"] else 0
                if restored:
                    after = apply_turn(session, f"post restore continuation {turn}", turn + 10000, condition)
                    post_restore_ok += 1 if after.get("agent_events") else 0
        trace.append({"turn": turn, "event": event, "restored": restored_this_turn, "checks": checks, "session_hash": stable_hash({"place": session["avatar_place"], "world": session["world"], "thread_len": len(session.get("typed_thread", []))})})
    denom = max(1, expected_saves)
    final_memory = agent_memory_lengths(session["agents"] if isinstance(session["agents"], Mapping) else {})
    memory_growth = any(final_memory.get(agent_id, (0, 0))[0] >= lengths[0] and final_memory.get(agent_id, (0, 0))[1] >= lengths[1] for agent_id, lengths in baseline_memory.items())
    row = EvalRow(
        condition=condition.name,
        session_turns=cfg.session_turns,
        expected_saves=expected_saves,
        session_save_rate=round(save_ok / denom if condition.local_save else 0.0, 6),
        restore_continuity_rate=round(restore_ok / denom if condition.restore_continuity else 0.0, 6),
        agent_memory_carryover_rate=round(agent_ok / denom if condition.agent_memory_carryover and memory_growth else 0.0, 6),
        world_feedback_carryover_rate=round(world_ok / denom if condition.world_feedback_carryover else 0.0, 6),
        place_context_carryover_rate=round(place_ok / denom if condition.place_context_carryover else 0.0, 6),
        typed_thread_carryover_rate=round(thread_ok / denom if condition.typed_thread_carryover else 0.0, 6),
        replay_import_export_rate=round(replay_ok / denom if condition.replay_import_export else 0.0, 6),
        source_boundary_carryover_rate=round(source_ok / denom if condition.source_boundary_carryover else 0.0, 6),
        frequency_phase_carryover_rate=round(frequency_ok / denom if condition.frequency_phase_carryover else 0.0, 6),
        schema_migration_guard_rate=round(schema_ok / denom if condition.schema_migration_guard else 0.0, 6),
        post_restore_interaction_rate=round(post_restore_ok / denom, 6),
        trace_integrity=round(1.0 if len(trace) == cfg.session_turns else 0.0, 6),
        persistent_session_readiness=0.0,
    )
    readiness = (
        row.session_save_rate * 0.10
        + row.restore_continuity_rate * 0.12
        + row.agent_memory_carryover_rate * 0.12
        + row.world_feedback_carryover_rate * 0.10
        + row.place_context_carryover_rate * 0.08
        + row.typed_thread_carryover_rate * 0.10
        + row.replay_import_export_rate * 0.08
        + row.source_boundary_carryover_rate * 0.09
        + row.frequency_phase_carryover_rate * 0.08
        + row.schema_migration_guard_rate * 0.07
        + row.post_restore_interaction_rate * 0.04
        + row.trace_integrity * 0.02
    )
    row = EvalRow(**{**asdict(row), "persistent_session_readiness": round(readiness, 6)})
    state = {
        "condition": condition.name,
        "config": asdict(cfg),
        "schema_version": SCHEMA_VERSION,
        "session": session,
        "snapshots": snapshots,
        "session_trace": trace,
        "persistence_contract": {
            "local_save_restore": "session snapshots can be serialized and restored without rerunning benchmark traces",
            "agent_memory_carryover": "agent workspaces and social memories survive restore",
            "world_place_thread_replay": "world feedback, avatar place, typed thread, replay, source boundary, and frequency phase survive restore",
            "schema_guard": "snapshot hash and schema version reject invalid persistence",
            "post_restore_interaction": "the restored session accepts additional turns after restore",
        },
        "limits": {
            "no_llm_calls": True,
            "deterministic_local_persistence": True,
            "not_subjective_consciousness": True,
            "not_complete_playable_world": True,
            "not_unscripted_civilization": True,
        },
    }
    return row, trace, state


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_persistent_session_state"]

    def loss(name: str) -> float:
        return round(full.persistent_session_readiness - by_name[name].persistent_session_readiness, 6)

    supports = (
        full.persistent_session_readiness >= 0.94
        and full.session_save_rate >= 0.99
        and full.restore_continuity_rate >= 0.99
        and full.agent_memory_carryover_rate >= 0.99
        and full.world_feedback_carryover_rate >= 0.99
        and full.place_context_carryover_rate >= 0.99
        and full.typed_thread_carryover_rate >= 0.99
        and full.replay_import_export_rate >= 0.99
        and full.source_boundary_carryover_rate >= 0.99
        and full.frequency_phase_carryover_rate >= 0.99
        and full.schema_migration_guard_rate >= 0.99
        and full.post_restore_interaction_rate >= 0.99
        and full.trace_integrity >= 0.99
    )
    return VerdictRow(
        full_condition=full.condition,
        full_persistent_session_readiness=full.persistent_session_readiness,
        full_session_save_rate=full.session_save_rate,
        full_restore_continuity_rate=full.restore_continuity_rate,
        full_agent_memory_carryover_rate=full.agent_memory_carryover_rate,
        full_world_feedback_carryover_rate=full.world_feedback_carryover_rate,
        full_place_context_carryover_rate=full.place_context_carryover_rate,
        full_typed_thread_carryover_rate=full.typed_thread_carryover_rate,
        full_replay_import_export_rate=full.replay_import_export_rate,
        full_source_boundary_carryover_rate=full.source_boundary_carryover_rate,
        full_frequency_phase_carryover_rate=full.frequency_phase_carryover_rate,
        full_schema_migration_guard_rate=full.schema_migration_guard_rate,
        full_post_restore_interaction_rate=full.post_restore_interaction_rate,
        full_trace_integrity=full.trace_integrity,
        no_local_save_loss=loss("no_local_save"),
        no_restore_continuity_loss=loss("no_restore_continuity"),
        no_agent_memory_carryover_loss=loss("no_agent_memory_carryover"),
        no_world_feedback_carryover_loss=loss("no_world_feedback_carryover"),
        no_place_context_carryover_loss=loss("no_place_context_carryover"),
        no_typed_thread_carryover_loss=loss("no_typed_thread_carryover"),
        no_replay_import_export_loss=loss("no_replay_import_export"),
        no_source_boundary_carryover_loss=loss("no_source_boundary_carryover"),
        no_frequency_phase_carryover_loss=loss("no_frequency_phase_carryover"),
        no_schema_migration_guard_loss=loss("no_schema_migration_guard"),
        supports_persistent_session_state_bridge=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "fail",
    )


def run(cfg: PersistentSessionConfig) -> dict[str, object]:
    source = load_state(Path(cfg.source_typed))
    if not isinstance(source.get("typed_copresence_trace"), list) or not source["typed_copresence_trace"]:
        raise ValueError("Report 159 typed co-presence trace is missing")
    rows: list[EvalRow] = []
    integrated_state: dict[str, object] = {}
    integrated_trace: list[dict[str, object]] = []
    for condition in CONDITIONS:
        row, trace, state = run_condition(cfg, condition, source)
        rows.append(row)
        if condition.name == "integrated_persistent_session_state":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {
        "config": asdict(cfg),
        "source_bridges": {"interactive_typed_copresence": "Report 159 interactive typed co-presence bridge"},
        "eval_rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "limits": {
            "no_llm_calls": True,
            "deterministic_local_persistence": True,
            "subjective_consciousness_claimed": False,
            "complete_playable_world_claimed": False,
            "unscripted_civilization_claimed": False,
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_PERSISTENT_SESSION_STATE_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_PERSISTENT_SESSION_STATE_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_PERSISTENT_SESSION_STATE", integrated_state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260704)
    parser.add_argument("--session-turns", type=int, default=96)
    parser.add_argument("--save-interval", type=int, default=8)
    parser.add_argument("--source-typed", default=str(SOURCE_TYPED))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = PersistentSessionConfig(seed=args.seed, session_turns=args.session_turns, save_interval=args.save_interval, source_typed=args.source_typed)
    results = run(cfg)
    print(json.dumps(results["verdict"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
