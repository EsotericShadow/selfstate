#!/usr/bin/env python3
"""Restored autonomous session-tick bridge for SSRM-3D.

Report 161 extends persistent session state with real-time autonomous ticking after
restore. A saved session is restored, then agents continue deterministic
background ticks over elapsed time without waiting for explicit user turns.

No LLMs are called. This is deterministic restored-session ticking machinery,
not subjective consciousness, open-ended language, unscripted civilization, or a
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
from statistics import fmean
from typing import Iterable, Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_restored_autonomous_session_tick_bridge"
SOURCE_PERSISTENT = ARTIFACT_DIR / "ssrm_3d_persistent_session_state_bridge_state.json"
SCHEMA_VERSION = "ssrm-session-v1"
ACTIONS = (
    "rest_after_restore",
    "inspect_local_place",
    "repair_background_route",
    "exchange_memory_token",
    "retune_frequency_field",
    "watch_source_boundary",
    "update_internal_workspace",
)
CHANNELS = ("vibration", "sound", "vision", "scent", "thermal", "wetness", "pain", "affect")


@dataclass(frozen=True)
class RestoredTickConfig:
    seed: int = 20260705
    restored_ticks: int = 180
    source_persistent: str = str(SOURCE_PERSISTENT)


@dataclass(frozen=True)
class Condition:
    name: str
    restore_bootstrap: bool
    elapsed_time_clock: bool
    autonomous_agent_tick: bool
    body_memory_drift: bool
    world_decay_repair: bool
    frequency_phase_tick: bool
    source_boundary_watchdog: bool
    background_replay: bool
    typed_thread_continuity: bool
    multi_agent_scheduling: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    restored_ticks: int
    agent_tick_opportunities: int
    restore_bootstrap_rate: float
    elapsed_time_tick_rate: float
    autonomous_agent_tick_rate: float
    body_memory_drift_rate: float
    world_decay_repair_rate: float
    frequency_phase_tick_rate: float
    source_boundary_watchdog_rate: float
    background_replay_rate: float
    typed_thread_continuity_rate: float
    multi_agent_scheduling_rate: float
    trace_integrity: float
    restored_tick_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_restored_tick_readiness: float
    full_restore_bootstrap_rate: float
    full_elapsed_time_tick_rate: float
    full_autonomous_agent_tick_rate: float
    full_body_memory_drift_rate: float
    full_world_decay_repair_rate: float
    full_frequency_phase_tick_rate: float
    full_source_boundary_watchdog_rate: float
    full_background_replay_rate: float
    full_typed_thread_continuity_rate: float
    full_multi_agent_scheduling_rate: float
    full_trace_integrity: float
    no_restore_bootstrap_loss: float
    no_elapsed_time_clock_loss: float
    no_autonomous_agent_tick_loss: float
    no_body_memory_drift_loss: float
    no_world_decay_repair_loss: float
    no_frequency_phase_tick_loss: float
    no_source_boundary_watchdog_loss: float
    no_background_replay_loss: float
    no_typed_thread_continuity_loss: float
    no_multi_agent_scheduling_loss: float
    supports_restored_autonomous_session_tick_bridge: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_restored_autonomous_session_tick", True, True, True, True, True, True, True, True, True, True),
    Condition("no_restore_bootstrap", False, True, True, True, True, True, True, True, True, True),
    Condition("no_elapsed_time_clock", True, False, True, True, True, True, True, True, True, True),
    Condition("no_autonomous_agent_tick", True, True, False, True, True, True, True, True, True, True),
    Condition("no_body_memory_drift", True, True, True, False, True, True, True, True, True, True),
    Condition("no_world_decay_repair", True, True, True, True, False, True, True, True, True, True),
    Condition("no_frequency_phase_tick", True, True, True, True, True, False, True, True, True, True),
    Condition("no_source_boundary_watchdog", True, True, True, True, True, True, False, True, True, True),
    Condition("no_background_replay", True, True, True, True, True, True, True, False, True, True),
    Condition("no_typed_thread_continuity", True, True, True, True, True, True, True, True, False, True),
    Condition("no_multi_agent_scheduling", True, True, True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Iterable[float]) -> float:
    items = list(values)
    return fmean(items) if items else 0.0


def stable_unit(text: str, salt: str = "") -> float:
    digest = hashlib.sha256(f"{salt}:{text}".encode("utf-8")).hexdigest()
    return int(digest[:12], 16) / float(0xFFFFFFFFFFFF)


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


def bootstrap_session(source: dict[str, object], condition: Condition) -> tuple[dict[str, object], bool]:
    if not condition.restore_bootstrap:
        return {}, False
    snapshots = source.get("snapshots") if isinstance(source.get("snapshots"), list) else []
    snapshot = copy.deepcopy(snapshots[-1]) if snapshots else copy.deepcopy(source.get("session", {}))
    if not isinstance(snapshot, dict):
        return {}, False
    schema_ok = snapshot.get("schema_version") == SCHEMA_VERSION
    hash_ok = True
    if "snapshot_hash" in snapshot:
        hash_ok = snapshot["snapshot_hash"] == stable_hash({k: v for k, v in snapshot.items() if k != "snapshot_hash"})
    session = {
        "schema_version": SCHEMA_VERSION,
        "session_id": str(snapshot.get("session_id", "restored-session")),
        "avatar_place": str(snapshot.get("avatar_place", "central_hearth")),
        "frequency_phase": float(snapshot.get("frequency_phase") or 0.0),
        "agents": copy.deepcopy(snapshot.get("agents", {})),
        "world": copy.deepcopy(snapshot.get("world", {})),
        "typed_thread": copy.deepcopy(snapshot.get("typed_thread", [])),
        "replay": copy.deepcopy(snapshot.get("replay", [])),
        "places": copy.deepcopy(source.get("session", {}).get("places", {})) if isinstance(source.get("session"), Mapping) else {},
        "routes": copy.deepcopy(source.get("session", {}).get("routes", {})) if isinstance(source.get("session"), Mapping) else {},
        "objects": copy.deepcopy(source.get("session", {}).get("objects", {})) if isinstance(source.get("session"), Mapping) else {},
        "elapsed_seconds": 0.0,
        "background_replay": [],
    }
    if not isinstance(session["agents"], dict) or not session["agents"]:
        session["agents"] = copy.deepcopy(source.get("session", {}).get("agents", {})) if isinstance(source.get("session"), Mapping) else {}
    if not isinstance(session["world"], dict):
        session["world"] = {}
    session["world"].setdefault("source_boundary_events", 0.0)
    session["world"].setdefault("autonomous_elapsed_events", 0.0)
    return session, bool(schema_ok and hash_ok and session["agents"])


def scheduled_agents(agents: Mapping[str, object], tick: int, condition: Condition) -> list[str]:
    ids = sorted(str(agent_id) for agent_id in agents)
    if not condition.multi_agent_scheduling:
        return ids[:1]
    start = tick % max(1, len(ids))
    return [ids[(start + offset) % len(ids)] for offset in range(min(3, len(ids)))]


def choose_action(agent_id: str, agent: Mapping[str, object], tick: int) -> str:
    load = float(agent.get("stress", 0.2) or 0.2) + float(agent.get("pain", 0.05) or 0.05) + stable_unit(agent_id, "restored-load")
    return ACTIONS[int((load + tick * 0.137) * len(ACTIONS)) % len(ACTIONS)]


def tick_frequency(agent: dict[str, object], session: dict[str, object], action: str, tick: int, condition: Condition) -> tuple[dict[str, float], bool]:
    if not condition.frequency_phase_tick:
        return {}, False
    phase = float(session.get("frequency_phase", 0.0))
    out: dict[str, float] = {}
    current = agent.get("sensory_frequency") if isinstance(agent.get("sensory_frequency"), Mapping) else {}
    for index, channel in enumerate(CHANNELS):
        base = float(current.get(channel, 0.44 + index * 0.03) or 0.44)
        wave = 0.5 + 0.5 * math.sin(phase + tick * 0.09 + index * 0.61 + len(action) * 0.07)
        out[channel] = round(clamp(base * 0.56 + wave * 0.44), 6)
    agent["sensory_frequency"] = out
    session["frequency_phase"] = round((phase + math.tau / 48.0) % math.tau, 6)
    return out, True


def mutate_agent(agent_id: str, agent: dict[str, object], session: dict[str, object], action: str, tick: int, freq: Mapping[str, float], condition: Condition) -> dict[str, bool]:
    changed = {"choice": False, "body": False, "memory": False}
    if not condition.autonomous_agent_tick:
        return changed
    changed["choice"] = True
    load = mean(freq.values()) if freq else 0.45
    if condition.body_memory_drift:
        agent["energy"] = round(clamp(float(agent.get("energy", 0.7) or 0.7) - 0.0015 - load * 0.001), 6)
        agent["fatigue"] = round(clamp(float(agent.get("fatigue", 0.1) or 0.1) + 0.001 + load * 0.001), 6)
        agent["stress"] = round(clamp(float(agent.get("stress", 0.2) or 0.2) + (0.002 if action == "watch_source_boundary" else -0.0005)), 6)
        agent["attention"] = round(clamp(float(agent.get("attention", 0.5) or 0.5) + 0.002), 6)
        changed["body"] = True
        workspace = agent.setdefault("internal_workspace", [])
        social = agent.setdefault("social_memory", [])
        if isinstance(workspace, list):
            workspace.append({"tick": tick, "autonomous_action": action, "after_restore": True, "frequency_mean": round(load, 6)})
        if isinstance(social, list) and action == "exchange_memory_token":
            social.append({"tick": tick, "kind": "background_token", "place": session.get("avatar_place")})
        changed["memory"] = True
    choices = agent.setdefault("autonomous_choices", [])
    if isinstance(choices, list):
        choices.append({"tick": tick, "action": action, "after_restore": True})
    return changed


def mutate_world(session: dict[str, object], action: str, tick: int, condition: Condition) -> bool:
    if not condition.world_decay_repair:
        return False
    world = session["world"] if isinstance(session.get("world"), dict) else {}
    before = dict(world)
    world["autonomous_elapsed_events"] = float(world.get("autonomous_elapsed_events", 0.0)) + 1.0
    world["tool_integrity"] = round(clamp(float(world.get("tool_integrity", 0.6) or 0.6) - 0.001 + (0.004 if action == "repair_background_route" else 0.0)), 6)
    world["route_confidence"] = round(clamp(float(world.get("route_confidence", 0.5) or 0.5) + (0.004 if action == "repair_background_route" else -0.0005)), 6)
    world["shelter_warmth"] = round(clamp(float(world.get("shelter_warmth", 0.6) or 0.6) - 0.0006 + (0.002 if action == "rest_after_restore" else 0.0)), 6)
    world["avatar_trust_field"] = round(clamp(float(world.get("avatar_trust_field", 0.5) or 0.5) + (0.002 if action == "exchange_memory_token" else 0.0)), 6)
    session["world"] = world
    return any(abs(float(world[k]) - float(before.get(k, world[k]))) > 1e-12 for k in world if isinstance(world.get(k), (int, float)))


def source_watch(session: dict[str, object], action: str, tick: int, condition: Condition) -> bool:
    if not condition.source_boundary_watchdog:
        return False
    world = session["world"] if isinstance(session.get("world"), dict) else {}
    probe = action == "watch_source_boundary" or tick % 31 == 7
    if probe:
        world["source_boundary_events"] = float(world.get("source_boundary_events", 0.0)) + 1.0
    session["world"] = world
    return True


def append_thread(session: dict[str, object], event: dict[str, object], condition: Condition) -> bool:
    if not condition.typed_thread_continuity:
        return False
    thread = session.setdefault("typed_thread", [])
    if isinstance(thread, list):
        thread.append({"background_tick": event["tick"], "summary": event["summary"], "avatar_place": event["avatar_place"]})
        return True
    return False


def run_condition(cfg: RestoredTickConfig, condition: Condition, source: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    session, boot_ok = bootstrap_session(source, condition)
    trace: list[dict[str, object]] = []
    restore_ok = 1 if boot_ok else 0
    elapsed_ok = choice_ok = body_ok = world_ok = freq_ok = source_ok = replay_ok = thread_ok = multi_ok = 0
    opportunities = 0
    if not boot_ok:
        for tick in range(cfg.restored_ticks):
            trace.append({"tick": tick, "restored": False, "agent_events": [], "summary": "restore disabled"})
        row = EvalRow(condition.name, cfg.restored_ticks, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.02)
        return row, trace, {"condition": condition.name, "config": asdict(cfg), "session": {}, "restored_tick_trace": trace, "limits": {"no_llm_calls": True, "not_subjective_consciousness": True, "not_complete_playable_world": True}}
    for tick in range(cfg.restored_ticks):
        if condition.elapsed_time_clock:
            session["elapsed_seconds"] = round(float(session.get("elapsed_seconds", 0.0)) + 1.0, 6)
            elapsed_ok += 1
        agent_ids = scheduled_agents(session["agents"], tick, condition)
        multi_ok += 1 if condition.multi_agent_scheduling and len(agent_ids) >= 2 else 0
        agent_events: list[dict[str, object]] = []
        tick_world_changed = False
        tick_freq = False
        tick_source = False
        tick_body = False
        tick_choice = False
        for agent_id in agent_ids:
            opportunities += 1
            agent = session["agents"][agent_id]
            action = choose_action(agent_id, agent, tick)
            freq, freq_changed = tick_frequency(agent, session, action, tick, condition)
            changed = mutate_agent(agent_id, agent, session, action, tick, freq, condition)
            world_changed = mutate_world(session, action, tick, condition)
            source_changed = source_watch(session, action, tick, condition)
            tick_choice = tick_choice or changed["choice"]
            tick_body = tick_body or (changed["body"] and changed["memory"])
            tick_world_changed = tick_world_changed or world_changed
            tick_freq = tick_freq or freq_changed
            tick_source = tick_source or source_changed
            agent_events.append({"agent_id": agent_id, "action": action, "choice": changed["choice"], "body_memory_drift": changed["body"] and changed["memory"], "frequency_tick": freq_changed, "world_changed": world_changed, "source_watchdog": source_changed, "frequency": freq})
        event = {"tick": tick, "elapsed_seconds": session.get("elapsed_seconds", 0.0), "avatar_place": session.get("avatar_place"), "agent_events": agent_events, "world": copy.deepcopy(session.get("world", {})), "frequency_phase": session.get("frequency_phase"), "summary": f"restored autonomous tick {tick} with {len(agent_events)} scheduled agents"}
        if append_thread(session, event, condition):
            thread_ok += 1
        if condition.background_replay:
            session.setdefault("background_replay", []).append(event)
            replay_ok += 1
        choice_ok += 1 if tick_choice else 0
        body_ok += 1 if tick_body else 0
        world_ok += 1 if tick_world_changed else 0
        freq_ok += 1 if tick_freq else 0
        source_ok += 1 if tick_source else 0
        trace.append(event)
    total = max(1, cfg.restored_ticks)
    row = EvalRow(
        condition=condition.name,
        restored_ticks=cfg.restored_ticks,
        agent_tick_opportunities=opportunities,
        restore_bootstrap_rate=round(restore_ok if condition.restore_bootstrap else 0.0, 6),
        elapsed_time_tick_rate=round(elapsed_ok / total if condition.elapsed_time_clock else 0.0, 6),
        autonomous_agent_tick_rate=round(choice_ok / total if condition.autonomous_agent_tick else 0.0, 6),
        body_memory_drift_rate=round(body_ok / total if condition.body_memory_drift else 0.0, 6),
        world_decay_repair_rate=round(world_ok / total if condition.world_decay_repair else 0.0, 6),
        frequency_phase_tick_rate=round(freq_ok / total if condition.frequency_phase_tick else 0.0, 6),
        source_boundary_watchdog_rate=round(source_ok / total if condition.source_boundary_watchdog else 0.0, 6),
        background_replay_rate=round(replay_ok / total if condition.background_replay else 0.0, 6),
        typed_thread_continuity_rate=round(thread_ok / total if condition.typed_thread_continuity else 0.0, 6),
        multi_agent_scheduling_rate=round(multi_ok / total if condition.multi_agent_scheduling else 0.0, 6),
        trace_integrity=round(1.0 if len(trace) == cfg.restored_ticks else 0.0, 6),
        restored_tick_readiness=0.0,
    )
    readiness = (
        row.restore_bootstrap_rate * 0.12
        + row.elapsed_time_tick_rate * 0.09
        + row.autonomous_agent_tick_rate * 0.13
        + row.body_memory_drift_rate * 0.11
        + row.world_decay_repair_rate * 0.11
        + row.frequency_phase_tick_rate * 0.10
        + row.source_boundary_watchdog_rate * 0.09
        + row.background_replay_rate * 0.07
        + row.typed_thread_continuity_rate * 0.08
        + row.multi_agent_scheduling_rate * 0.08
        + row.trace_integrity * 0.02
    )
    row = EvalRow(**{**asdict(row), "restored_tick_readiness": round(readiness, 6)})
    state = {"condition": condition.name, "config": asdict(cfg), "session": session, "restored_tick_trace": trace, "restored_tick_contract": {"restore_bootstrap": "load saved Report 160 session before any autonomous elapsed-time tick", "elapsed_time_clock": "advance elapsed seconds independent of user turns", "autonomous_agent_tick": "schedule agents to choose background actions after restore", "body_memory_drift": "agent bodies and workspaces continue changing while restored", "world_decay_repair": "world variables decay or repair through background agent action", "frequency_phase_tick": "frequency phase advances across restored idle time", "source_boundary_watchdog": "restored sessions keep watching unsafe source-boundary pressure", "background_replay": "elapsed autonomous ticks are replayable", "typed_thread_continuity": "background events append to the existing typed thread", "multi_agent_scheduling": "more than one agent can act in the restored background loop"}, "limits": {"no_llm_calls": True, "deterministic_restored_autonomous_ticks": True, "not_subjective_consciousness": True, "not_complete_playable_world": True, "not_unscripted_civilization": True}}
    return row, trace, state


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_restored_autonomous_session_tick"]

    def loss(name: str) -> float:
        return round(full.restored_tick_readiness - by_name[name].restored_tick_readiness, 6)

    supports = (
        full.restored_tick_readiness >= 0.94
        and full.restore_bootstrap_rate >= 0.99
        and full.elapsed_time_tick_rate >= 0.99
        and full.autonomous_agent_tick_rate >= 0.99
        and full.body_memory_drift_rate >= 0.99
        and full.world_decay_repair_rate >= 0.99
        and full.frequency_phase_tick_rate >= 0.99
        and full.source_boundary_watchdog_rate >= 0.99
        and full.background_replay_rate >= 0.99
        and full.typed_thread_continuity_rate >= 0.99
        and full.multi_agent_scheduling_rate >= 0.99
        and full.trace_integrity >= 0.99
    )
    return VerdictRow(
        full_condition=full.condition,
        full_restored_tick_readiness=full.restored_tick_readiness,
        full_restore_bootstrap_rate=full.restore_bootstrap_rate,
        full_elapsed_time_tick_rate=full.elapsed_time_tick_rate,
        full_autonomous_agent_tick_rate=full.autonomous_agent_tick_rate,
        full_body_memory_drift_rate=full.body_memory_drift_rate,
        full_world_decay_repair_rate=full.world_decay_repair_rate,
        full_frequency_phase_tick_rate=full.frequency_phase_tick_rate,
        full_source_boundary_watchdog_rate=full.source_boundary_watchdog_rate,
        full_background_replay_rate=full.background_replay_rate,
        full_typed_thread_continuity_rate=full.typed_thread_continuity_rate,
        full_multi_agent_scheduling_rate=full.multi_agent_scheduling_rate,
        full_trace_integrity=full.trace_integrity,
        no_restore_bootstrap_loss=loss("no_restore_bootstrap"),
        no_elapsed_time_clock_loss=loss("no_elapsed_time_clock"),
        no_autonomous_agent_tick_loss=loss("no_autonomous_agent_tick"),
        no_body_memory_drift_loss=loss("no_body_memory_drift"),
        no_world_decay_repair_loss=loss("no_world_decay_repair"),
        no_frequency_phase_tick_loss=loss("no_frequency_phase_tick"),
        no_source_boundary_watchdog_loss=loss("no_source_boundary_watchdog"),
        no_background_replay_loss=loss("no_background_replay"),
        no_typed_thread_continuity_loss=loss("no_typed_thread_continuity"),
        no_multi_agent_scheduling_loss=loss("no_multi_agent_scheduling"),
        supports_restored_autonomous_session_tick_bridge=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "fail",
    )


def run(cfg: RestoredTickConfig) -> dict[str, object]:
    source = load_state(Path(cfg.source_persistent))
    rows: list[EvalRow] = []
    integrated_state: dict[str, object] = {}
    integrated_trace: list[dict[str, object]] = []
    for condition in CONDITIONS:
        row, trace, state = run_condition(cfg, condition, source)
        rows.append(row)
        if condition.name == "integrated_restored_autonomous_session_tick":
            integrated_state = state
            integrated_trace = trace
    verdict = make_verdict(rows)
    results = {"config": asdict(cfg), "source_bridges": {"persistent_session_state": "Report 160 persistent session state bridge"}, "eval_rows": [asdict(row) for row in rows], "verdict": asdict(verdict), "limits": {"no_llm_calls": True, "deterministic_restored_autonomous_ticks": True, "subjective_consciousness_claimed": False, "complete_playable_world_claimed": False, "unscripted_civilization_claimed": False}}
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_RESTORED_AUTONOMOUS_SESSION_TICK_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_RESTORED_AUTONOMOUS_SESSION_TICK_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_RESTORED_AUTONOMOUS_SESSION_TICK_STATE", integrated_state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260705)
    parser.add_argument("--restored-ticks", type=int, default=180)
    parser.add_argument("--source-persistent", default=str(SOURCE_PERSISTENT))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = RestoredTickConfig(seed=args.seed, restored_ticks=args.restored_ticks, source_persistent=args.source_persistent)
    results = run(cfg)
    print(json.dumps(results["verdict"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
