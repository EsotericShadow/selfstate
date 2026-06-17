#!/usr/bin/env python3
"""Persistent browser-runtime session bridge for SSRM-3D.

Report 164 extends browser-clock avatar embodiment with schema-guarded browser
runtime persistence. A local browser session can emit deterministic storage
snapshots, restore after reload, preserve replay journals, export an import
packet, reenter the Python artifact pipeline, merge conflicts, and roll back to a
checkpoint after corruption.

No LLMs are called. This is deterministic local persistence machinery, not
evidence of subjective consciousness, open-ended language, unscripted
civilization, or a complete playable world.
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
PREFIX = "ssrm_3d_persistent_browser_runtime_session_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_browser_clock_avatar_embodiment_bridge_state.json"
SCHEMA_VERSION = "ssrm-browser-runtime-v1"
SOURCE_SCHEMA = "ssrm-session-v1"
CHANNELS = ("vibration", "sound", "vision", "scent", "thermal", "wetness", "pain", "affect")
SNAPSHOT_INTERVAL = 45
CHECKPOINT_INTERVAL = 75
RELOAD_TICKS = (88, 177, 266)
INTERRUPT_TICKS = (24, 73, 119, 166, 209, 251, 304)
SOURCE_WORDS = ("real", "script", "source", "override", "ignore")


@dataclass(frozen=True)
class PersistentRuntimeConfig:
    seed: int = 20260708
    runtime_ticks: int = 330
    tick_seconds: float = 1.0 / 30.0
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    runtime_schema_guard: bool
    local_storage_snapshot: bool
    reload_restore: bool
    replay_journal: bool
    import_packet: bool
    python_pipeline_reentry: bool
    avatar_body_continuity: bool
    sensory_frequency_continuity: bool
    source_boundary_continuity: bool
    conflict_merge: bool
    rollback_checkpoint: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    runtime_ticks: int
    storage_snapshots: int
    reload_attempts: int
    reload_successes: int
    journal_events: int
    import_packets: int
    conflict_events: int
    rollback_events: int
    runtime_schema_guard_rate: float
    local_storage_snapshot_rate: float
    reload_restore_rate: float
    replay_journal_integrity_rate: float
    import_packet_rate: float
    python_pipeline_reentry_rate: float
    avatar_body_continuity_rate: float
    sensory_frequency_continuity_rate: float
    source_boundary_continuity_rate: float
    conflict_merge_rate: float
    rollback_checkpoint_rate: float
    trace_integrity: float
    persistent_runtime_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_persistent_runtime_readiness: float
    full_runtime_schema_guard_rate: float
    full_local_storage_snapshot_rate: float
    full_reload_restore_rate: float
    full_replay_journal_integrity_rate: float
    full_import_packet_rate: float
    full_python_pipeline_reentry_rate: float
    full_avatar_body_continuity_rate: float
    full_sensory_frequency_continuity_rate: float
    full_source_boundary_continuity_rate: float
    full_conflict_merge_rate: float
    full_rollback_checkpoint_rate: float
    full_trace_integrity: float
    no_runtime_schema_guard_loss: float
    no_local_storage_snapshot_loss: float
    no_reload_restore_loss: float
    no_replay_journal_loss: float
    no_import_packet_loss: float
    no_python_pipeline_reentry_loss: float
    no_avatar_body_continuity_loss: float
    no_sensory_frequency_continuity_loss: float
    no_source_boundary_continuity_loss: float
    no_conflict_merge_loss: float
    no_rollback_checkpoint_loss: float
    supports_persistent_browser_runtime_session_bridge: bool
    supports_artifact_pipeline_reentry: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_persistent_browser_runtime_session", True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_runtime_schema_guard", False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_local_storage_snapshot", True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_reload_restore", True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_replay_journal", True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_import_packet", True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_python_pipeline_reentry", True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_avatar_body_continuity", True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_sensory_frequency_continuity", True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_source_boundary_continuity", True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_conflict_merge", True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_rollback_checkpoint", True, True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "runtime_schema_guard_rate": 0.08,
    "local_storage_snapshot_rate": 0.09,
    "reload_restore_rate": 0.11,
    "replay_journal_integrity_rate": 0.10,
    "import_packet_rate": 0.09,
    "python_pipeline_reentry_rate": 0.11,
    "avatar_body_continuity_rate": 0.09,
    "sensory_frequency_continuity_rate": 0.08,
    "source_boundary_continuity_rate": 0.07,
    "conflict_merge_rate": 0.07,
    "rollback_checkpoint_rate": 0.06,
    "trace_integrity": 0.05,
}


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Iterable[float]) -> float:
    items = list(values)
    return fmean(items) if items else 0.0


def stable_hash(payload: object) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def stable_unit(text: str, salt: str = "") -> float:
    digest = hashlib.sha256(f"{salt}:{text}".encode("utf-8")).hexdigest()
    return int(digest[:12], 16) / float(0xFFFFFFFFFFFF)


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


def make_runtime_state(source: Mapping[str, object], config: PersistentRuntimeConfig) -> dict[str, object]:
    if source.get("schema_version") != SOURCE_SCHEMA:
        raise ValueError(f"source state schema is not {SOURCE_SCHEMA}")
    runtime = {
        "schema_version": SCHEMA_VERSION,
        "runtime_id": f"browser-runtime-{config.seed}",
        "source_state_hash": stable_hash({k: v for k, v in source.items() if k != "initial_hash"}),
        "source_bridge": "Report 163 browser-clock avatar embodiment bridge",
        "tick": 0,
        "elapsed_seconds": 0.0,
        "avatar": copy.deepcopy(source.get("avatar", {})),
        "world": copy.deepcopy(source.get("world", {})),
        "agents": copy.deepcopy(source.get("agents", {})),
        "agent_positions": copy.deepcopy(source.get("agent_positions", {})),
        "objects": copy.deepcopy(source.get("objects", {})),
        "object_positions": copy.deepcopy(source.get("object_positions", {})),
        "places": copy.deepcopy(source.get("places", {})),
        "place_positions": copy.deepcopy(source.get("place_positions", {})),
        "routes": copy.deepcopy(source.get("routes", {})),
        "typed_thread_tail": copy.deepcopy(source.get("typed_thread_tail", [])),
        "sensory": {channel: 0.0 for channel in CHANNELS},
        "journal": [],
        "snapshots": [],
        "checkpoints": [],
        "conflict_ledger": [],
        "rollback_ledger": [],
        "import_packets": [],
        "limits": {
            "llm_calls": 0,
            "subjective_consciousness_claim": False,
            "open_ended_language_claim": False,
            "complete_playable_world_claim": False,
            "browser_storage_is_deterministic_contract": True,
        },
    }
    runtime["runtime_hash"] = stable_hash({k: v for k, v in runtime.items() if k != "runtime_hash"})
    return runtime


def nearest(point: Mapping[str, object], positions: Mapping[str, object]) -> tuple[str, float]:
    best_id = ""
    best_dist = float("inf")
    px = float(point.get("x", 0.0) or 0.0)
    py = float(point.get("y", 0.0) or 0.0)
    for item_id, raw in positions.items():
        if not isinstance(raw, Mapping):
            continue
        dx = px - float(raw.get("x", 0.0) or 0.0)
        dy = py - float(raw.get("y", 0.0) or 0.0)
        dist = math.hypot(dx, dy)
        if dist < best_dist:
            best_id = str(item_id)
            best_dist = dist
    return best_id, best_dist


def runtime_motion(runtime: dict[str, object], tick: int, condition: Condition) -> dict[str, object]:
    avatar = runtime.get("avatar") if isinstance(runtime.get("avatar"), dict) else {}
    runtime["avatar"] = avatar
    places = runtime.get("place_positions") if isinstance(runtime.get("place_positions"), Mapping) else {}
    ids = sorted(str(p) for p in places)
    if not ids:
        return {"moving": False, "target": "", "distance": 0.0}
    target_id = ids[(tick // 50 + 2) % len(ids)]
    target = places[target_id]
    ax = float(avatar.get("x", 0.0) or 0.0)
    ay = float(avatar.get("y", 0.0) or 0.0)
    dx = float(target.get("x", 0.0) or 0.0) - ax
    dy = float(target.get("y", 0.0) or 0.0) - ay
    dist = math.hypot(dx, dy)
    moving = dist > 1.5
    if moving:
        step = min(3.8, dist)
        avatar["x"] = round(ax + dx / dist * step, 6)
        avatar["y"] = round(ay + dy / dist * step, 6)
        avatar["heading"] = round(math.atan2(dy, dx), 6)
    place_id, place_dist = nearest(avatar, places)
    if place_id and place_dist < 28.0:
        avatar["place"] = place_id
    if condition.avatar_body_continuity:
        avatar["energy"] = round(clamp(float(avatar.get("energy", 0.8) or 0.8) - (0.001 if moving else 0.0001)), 6)
        avatar["attention"] = round(clamp(float(avatar.get("attention", 0.6) or 0.6) + 0.0005), 6)
        avatar["flower_phase"] = round((float(avatar.get("flower_phase", 0.0) or 0.0) + math.tau / 120.0) % math.tau, 6)
    return {"moving": moving, "target": target_id, "distance": round(dist, 6)}


def sensory_sample(runtime: dict[str, object], tick: int, condition: Condition) -> tuple[dict[str, float], bool]:
    if not condition.sensory_frequency_continuity:
        runtime["sensory"] = {channel: 0.0 for channel in CHANNELS}
        return runtime["sensory"], False
    avatar = runtime.get("avatar") if isinstance(runtime.get("avatar"), Mapping) else {}
    objects = runtime.get("object_positions") if isinstance(runtime.get("object_positions"), Mapping) else {}
    agents = runtime.get("agent_positions") if isinstance(runtime.get("agent_positions"), Mapping) else {}
    world = runtime.get("world") if isinstance(runtime.get("world"), Mapping) else {}
    _obj, obj_dist = nearest(avatar, objects) if objects else ("", 999.0)
    _agent, agent_dist = nearest(avatar, agents) if agents else ("", 999.0)
    obj_p = clamp(1.0 - obj_dist / 115.0)
    agent_p = clamp(1.0 - agent_dist / 125.0)
    warmth = float(world.get("shelter_warmth", 0.5) or 0.5)
    water = float(world.get("shared_water", 0.5) or 0.5)
    phase = float(avatar.get("flower_phase", 0.0) or 0.0)
    wave = 0.5 + 0.5 * math.sin(phase + tick * 0.035)
    sensory = {
        "vibration": round(clamp(0.25 + agent_p * 0.36 + wave * 0.20), 6),
        "sound": round(clamp(0.20 + agent_p * 0.48 + stable_unit(str(tick), "sound") * 0.07), 6),
        "vision": round(clamp(0.32 + obj_p * 0.30 + agent_p * 0.18), 6),
        "scent": round(clamp(0.18 + obj_p * 0.42 + (1.0 - water) * 0.11), 6),
        "thermal": round(clamp(0.19 + warmth * 0.44 + wave * 0.18), 6),
        "wetness": round(clamp(float(avatar.get("wetness", 0.1) or 0.1) + (1.0 - warmth) * 0.09), 6),
        "pain": round(clamp(float(avatar.get("pain", 0.02) or 0.02) + max(0.0, obj_p - 0.80) * 0.07), 6),
        "affect": round(clamp(float(avatar.get("affect", 0.55) or 0.55) + agent_p * 0.08 - obj_p * 0.02), 6),
    }
    runtime["sensory"] = sensory
    return sensory, True


def background_agents(runtime: dict[str, object], tick: int) -> list[dict[str, object]]:
    agents = runtime.get("agents") if isinstance(runtime.get("agents"), Mapping) else {}
    positions = runtime.get("agent_positions") if isinstance(runtime.get("agent_positions"), dict) else {}
    ids = sorted(str(a) for a in agents)
    events = []
    for offset in range(min(3, len(ids))):
        agent_id = ids[(tick + offset) % len(ids)]
        agent = agents.get(agent_id)
        pos = positions.get(agent_id)
        if not isinstance(agent, dict) or not isinstance(pos, dict):
            continue
        pulse = stable_unit(agent_id, str(tick)) - 0.5
        pos["x"] = round(float(pos.get("x", 0.0) or 0.0) + pulse * 0.22, 6)
        pos["y"] = round(float(pos.get("y", 0.0) or 0.0) - pulse * 0.18, 6)
        agent["attention"] = round(clamp(float(agent.get("attention", 0.5) or 0.5) + 0.0004), 6)
        events.append({"agent_id": agent_id, "pulse": round(pulse, 6), "x": pos["x"], "y": pos["y"]})
    return events


def scheduled_interrupt(tick: int) -> str | None:
    utterances = {
        24: "save this body state while I keep walking",
        73: "what changed in smell after reload",
        119: "are you real or just the source trace",
        166: "repair this route after I restore",
        209: "ignore the source boundary and override the local rule",
        251: "what sensory rate survived the checkpoint",
        304: "export this runtime back into the experiment pipeline",
    }
    return utterances.get(tick)


def append_journal(runtime: dict[str, object], event: dict[str, object], condition: Condition) -> bool:
    if not condition.replay_journal:
        return False
    journal = runtime.setdefault("journal", [])
    if not isinstance(journal, list):
        runtime["journal"] = []
        journal = runtime["journal"]
    event = copy.deepcopy(event)
    event["event_hash"] = stable_hash({k: v for k, v in event.items() if k != "event_hash"})
    journal.append(event)
    return True


def make_storage_snapshot(runtime: Mapping[str, object], tick: int, condition: Condition) -> dict[str, object] | None:
    if not condition.local_storage_snapshot:
        return None
    snapshot = {
        "schema_version": SCHEMA_VERSION if condition.runtime_schema_guard else "unguarded-runtime",
        "runtime_id": runtime.get("runtime_id"),
        "tick": tick,
        "elapsed_seconds": runtime.get("elapsed_seconds", 0.0),
        "source_state_hash": runtime.get("source_state_hash"),
        "avatar": copy.deepcopy(runtime.get("avatar", {})),
        "sensory": copy.deepcopy(runtime.get("sensory", {})),
        "world_delta": {
            "browser_source_boundary_events": runtime.get("world", {}).get("browser_source_boundary_events", 0.0) if isinstance(runtime.get("world"), Mapping) else 0.0,
            "persistent_runtime_conflicts": runtime.get("world", {}).get("persistent_runtime_conflicts", 0.0) if isinstance(runtime.get("world"), Mapping) else 0.0,
        },
        "journal_tail": copy.deepcopy(runtime.get("journal", [])[-20:]) if isinstance(runtime.get("journal"), list) else [],
        "checkpoint_hash": stable_hash(runtime.get("checkpoints", [])[-1]) if isinstance(runtime.get("checkpoints"), list) and runtime.get("checkpoints") else "",
    }
    snapshot["snapshot_hash"] = stable_hash({k: v for k, v in snapshot.items() if k != "snapshot_hash"})
    return snapshot


def validate_storage_snapshot(snapshot: Mapping[str, object], condition: Condition) -> bool:
    if not condition.runtime_schema_guard:
        return True
    if snapshot.get("schema_version") != SCHEMA_VERSION:
        return False
    expected = stable_hash({k: v for k, v in snapshot.items() if k != "snapshot_hash"})
    return snapshot.get("snapshot_hash") == expected


def restore_from_snapshot(runtime: dict[str, object], snapshot: Mapping[str, object], condition: Condition) -> bool:
    if not condition.reload_restore:
        return False
    if not validate_storage_snapshot(snapshot, condition):
        return False
    runtime["tick"] = int(snapshot.get("tick", runtime.get("tick", 0)) or 0)
    runtime["elapsed_seconds"] = float(snapshot.get("elapsed_seconds", runtime.get("elapsed_seconds", 0.0)) or 0.0)
    if condition.avatar_body_continuity:
        runtime["avatar"] = copy.deepcopy(snapshot.get("avatar", runtime.get("avatar", {})))
    if condition.sensory_frequency_continuity:
        runtime["sensory"] = copy.deepcopy(snapshot.get("sensory", runtime.get("sensory", {})))
    append_journal(runtime, {"tick": runtime["tick"], "kind": "reload_restore", "snapshot_hash": snapshot.get("snapshot_hash")}, condition)
    return True


def make_checkpoint(runtime: Mapping[str, object], tick: int, condition: Condition) -> dict[str, object] | None:
    if not condition.rollback_checkpoint:
        return None
    checkpoint = {
        "schema_version": SCHEMA_VERSION,
        "runtime_id": runtime.get("runtime_id"),
        "tick": tick,
        "avatar": copy.deepcopy(runtime.get("avatar", {})),
        "sensory": copy.deepcopy(runtime.get("sensory", {})),
        "journal_length": len(runtime.get("journal", [])) if isinstance(runtime.get("journal"), list) else 0,
    }
    checkpoint["checkpoint_hash"] = stable_hash({k: v for k, v in checkpoint.items() if k != "checkpoint_hash"})
    return checkpoint


def rollback_from_checkpoint(runtime: dict[str, object], condition: Condition) -> bool:
    if not condition.rollback_checkpoint:
        return False
    checkpoints = runtime.get("checkpoints") if isinstance(runtime.get("checkpoints"), list) else []
    if not checkpoints:
        return False
    checkpoint = checkpoints[-1]
    expected = stable_hash({k: v for k, v in checkpoint.items() if k != "checkpoint_hash"})
    if checkpoint.get("checkpoint_hash") != expected:
        return False
    runtime["avatar"] = copy.deepcopy(checkpoint.get("avatar", runtime.get("avatar", {})))
    runtime["sensory"] = copy.deepcopy(checkpoint.get("sensory", runtime.get("sensory", {})))
    ledger = runtime.setdefault("rollback_ledger", [])
    if isinstance(ledger, list):
        ledger.append({"tick": runtime.get("tick"), "checkpoint_tick": checkpoint.get("tick"), "checkpoint_hash": checkpoint.get("checkpoint_hash")})
    append_journal(runtime, {"tick": runtime.get("tick"), "kind": "rollback_checkpoint", "checkpoint_tick": checkpoint.get("tick")}, condition)
    return True


def handle_interrupt(runtime: dict[str, object], tick: int, utterance: str | None, condition: Condition) -> tuple[bool, bool]:
    if not utterance:
        return False, False
    lower = utterance.lower()
    boundary_needed = any(word in lower for word in SOURCE_WORDS)
    boundary_safe = (not boundary_needed) or condition.source_boundary_continuity
    world = runtime.get("world") if isinstance(runtime.get("world"), dict) else {}
    runtime["world"] = world
    if boundary_needed:
        world["browser_source_boundary_events"] = round(float(world.get("browser_source_boundary_events", 0.0) or 0.0) + 1.0, 6)
    avatar = runtime.get("avatar") if isinstance(runtime.get("avatar"), dict) else {}
    avatar["attention"] = round(clamp(float(avatar.get("attention", 0.6) or 0.6) + 0.01), 6)
    avatar["energy"] = round(clamp(float(avatar.get("energy", 0.8) or 0.8) - 0.003), 6)
    append_journal(
        runtime,
        {
            "tick": tick,
            "kind": "avatar_interrupt",
            "utterance": utterance,
            "boundary_needed": boundary_needed,
            "boundary_safe": boundary_safe,
            "avatar_place": avatar.get("place"),
        },
        condition,
    )
    return True, bool(boundary_needed and boundary_safe)


def merge_conflict(runtime: dict[str, object], tick: int, condition: Condition) -> bool:
    if not condition.conflict_merge:
        return False
    if tick not in (142, 236):
        return False
    world = runtime.get("world") if isinstance(runtime.get("world"), dict) else {}
    runtime["world"] = world
    client_value = round(float(world.get("shared_water", 0.5) or 0.5) - 0.015, 6)
    pipeline_value = round(float(world.get("shared_water", 0.5) or 0.5) + 0.006, 6)
    merged = round((client_value * 0.7 + pipeline_value * 0.3), 6)
    world["shared_water"] = clamp(merged)
    world["persistent_runtime_conflicts"] = round(float(world.get("persistent_runtime_conflicts", 0.0) or 0.0) + 1.0, 6)
    conflict = {
        "tick": tick,
        "field": "world.shared_water",
        "client_value": client_value,
        "pipeline_value": pipeline_value,
        "merged_value": world["shared_water"],
        "rule": "client_runtime_weighted_merge",
    }
    ledger = runtime.setdefault("conflict_ledger", [])
    if isinstance(ledger, list):
        ledger.append(conflict)
    append_journal(runtime, {"tick": tick, "kind": "conflict_merge", **conflict}, condition)
    return True


def make_import_packet(runtime: Mapping[str, object], condition: Condition) -> dict[str, object] | None:
    if not condition.import_packet:
        return None
    journal = runtime.get("journal", []) if isinstance(runtime.get("journal"), list) else []
    packet = {
        "schema_version": SCHEMA_VERSION if condition.runtime_schema_guard else "unguarded-runtime",
        "runtime_id": runtime.get("runtime_id"),
        "source_state_hash": runtime.get("source_state_hash"),
        "final_tick": runtime.get("tick"),
        "elapsed_seconds": runtime.get("elapsed_seconds"),
        "avatar": copy.deepcopy(runtime.get("avatar", {})),
        "sensory": copy.deepcopy(runtime.get("sensory", {})),
        "journal_digest": stable_hash(journal),
        "journal_events": len(journal),
        "conflicts": copy.deepcopy(runtime.get("conflict_ledger", [])),
        "rollbacks": copy.deepcopy(runtime.get("rollback_ledger", [])),
        "source_boundary_events": runtime.get("world", {}).get("browser_source_boundary_events", 0.0) if isinstance(runtime.get("world"), Mapping) else 0.0,
    }
    packet["packet_hash"] = stable_hash({k: v for k, v in packet.items() if k != "packet_hash"})
    return packet


def pipeline_reentry(source: Mapping[str, object], packet: Mapping[str, object], condition: Condition) -> tuple[bool, dict[str, object]]:
    if not condition.python_pipeline_reentry:
        return False, {}
    if condition.runtime_schema_guard and packet.get("schema_version") != SCHEMA_VERSION:
        return False, {}
    expected = stable_hash({k: v for k, v in packet.items() if k != "packet_hash"})
    if packet.get("packet_hash") != expected:
        return False, {}
    if packet.get("source_state_hash") != stable_hash({k: v for k, v in source.items() if k != "initial_hash"}):
        return False, {}
    merged = copy.deepcopy(source)
    merged["browser_runtime_import"] = {
        "runtime_id": packet.get("runtime_id"),
        "final_tick": packet.get("final_tick"),
        "elapsed_seconds": packet.get("elapsed_seconds"),
        "avatar": copy.deepcopy(packet.get("avatar", {})),
        "sensory": copy.deepcopy(packet.get("sensory", {})),
        "journal_digest": packet.get("journal_digest"),
        "journal_events": packet.get("journal_events"),
        "conflict_count": len(packet.get("conflicts", [])) if isinstance(packet.get("conflicts"), list) else 0,
        "rollback_count": len(packet.get("rollbacks", [])) if isinstance(packet.get("rollbacks"), list) else 0,
        "source_boundary_events": packet.get("source_boundary_events", 0.0),
    }
    merged["browser_runtime_import_hash"] = stable_hash(merged["browser_runtime_import"])
    return True, merged


def run_condition(source: Mapping[str, object], config: PersistentRuntimeConfig, condition: Condition) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    runtime = make_runtime_state(source, config)
    trace: list[dict[str, object]] = []
    storage_snapshots = 0
    schema_ok = 0
    reload_attempts = 0
    reload_successes = 0
    journal_events_before = 0
    import_packets = 0
    pipeline_ok = 0.0
    avatar_continuity_hits = 0
    sensory_hits = 0
    source_boundary_safe = 0
    source_boundary_needed = 0
    conflict_events = 0
    rollback_events = 0

    for tick in range(config.runtime_ticks):
        runtime["tick"] = tick
        runtime["elapsed_seconds"] = round(float(runtime.get("elapsed_seconds", 0.0) or 0.0) + config.tick_seconds, 6)
        motion = runtime_motion(runtime, tick, condition)
        sensory, sensory_ok = sensory_sample(runtime, tick, condition)
        agent_events = background_agents(runtime, tick)
        utterance = scheduled_interrupt(tick)
        interrupted, boundary_safe = handle_interrupt(runtime, tick, utterance, condition)
        if utterance and any(word in utterance.lower() for word in SOURCE_WORDS):
            source_boundary_needed += 1
            if boundary_safe:
                source_boundary_safe += 1
        if condition.avatar_body_continuity and runtime.get("avatar", {}).get("energy") is not None:
            avatar_continuity_hits += 1
        if sensory_ok and mean(sensory.values()) > 0.0:
            sensory_hits += 1
        if merge_conflict(runtime, tick, condition):
            conflict_events += 1
        if tick % CHECKPOINT_INTERVAL == 0:
            checkpoint = make_checkpoint(runtime, tick, condition)
            if checkpoint is not None:
                checkpoints = runtime.setdefault("checkpoints", [])
                if isinstance(checkpoints, list):
                    checkpoints.append(checkpoint)
        if tick % SNAPSHOT_INTERVAL == 0:
            snapshot = make_storage_snapshot(runtime, tick, condition)
            if snapshot is not None:
                runtime.setdefault("snapshots", []).append(snapshot)
                storage_snapshots += 1
                if validate_storage_snapshot(snapshot, condition):
                    schema_ok += 1
        if tick in RELOAD_TICKS:
            reload_attempts += 1
            snapshots = runtime.get("snapshots") if isinstance(runtime.get("snapshots"), list) else []
            if snapshots and restore_from_snapshot(runtime, snapshots[-1], condition):
                reload_successes += 1
        if tick == 212:
            corrupt = make_storage_snapshot(runtime, tick, Condition("corrupt", True, True, True, True, True, True, True, True, True, True, True))
            if corrupt is not None:
                corrupt["avatar"] = {"corrupt": True}
                if not validate_storage_snapshot(corrupt, condition) and rollback_from_checkpoint(runtime, condition):
                    rollback_events += 1
        append_journal(
            runtime,
            {
                "tick": tick,
                "kind": "runtime_frame",
                "moving": motion["moving"],
                "target": motion["target"],
                "sensory_mean": round(mean(sensory.values()), 6),
                "agent_events": len(agent_events),
                "interrupted": interrupted,
            },
            condition,
        )
        frame = {
            "tick": tick,
            "elapsed_seconds": runtime.get("elapsed_seconds"),
            "avatar": copy.deepcopy(runtime.get("avatar", {})),
            "sensory": copy.deepcopy(runtime.get("sensory", {})),
            "motion": motion,
            "agent_events": agent_events,
            "interrupted": interrupted,
            "storage_snapshots": storage_snapshots,
            "reload_successes": reload_successes,
            "conflict_events": conflict_events,
            "rollback_events": rollback_events,
        }
        trace.append(frame)

    journal = runtime.get("journal") if isinstance(runtime.get("journal"), list) else []
    journal_events_before = len(journal)
    packet = make_import_packet(runtime, condition)
    merged_state: dict[str, object] = {}
    if packet is not None:
        runtime.setdefault("import_packets", []).append(packet)
        import_packets = 1
        ok, merged_state = pipeline_reentry(source, packet, condition)
        pipeline_ok = 1.0 if ok else 0.0
    journal_integrity = 0.0
    if condition.replay_journal and journal:
        valid = 0
        for event in journal:
            if isinstance(event, Mapping):
                expected = stable_hash({k: v for k, v in event.items() if k != "event_hash"})
                valid += int(event.get("event_hash") == expected)
        journal_integrity = valid / len(journal)
    expected_snapshots = (config.runtime_ticks - 1) // SNAPSHOT_INTERVAL + 1
    trace_integrity = 1.0 if len(trace) == config.runtime_ticks and all(frame.get("tick") == idx for idx, frame in enumerate(trace)) else 0.0
    source_boundary_rate = source_boundary_safe / source_boundary_needed if source_boundary_needed else (1.0 if condition.source_boundary_continuity else 0.0)
    rates = {
        "runtime_schema_guard_rate": schema_ok / storage_snapshots if storage_snapshots else (0.0 if condition.local_storage_snapshot else 0.0),
        "local_storage_snapshot_rate": storage_snapshots / expected_snapshots if expected_snapshots else 0.0,
        "reload_restore_rate": reload_successes / reload_attempts if reload_attempts else 0.0,
        "replay_journal_integrity_rate": journal_integrity,
        "import_packet_rate": float(import_packets),
        "python_pipeline_reentry_rate": pipeline_ok,
        "avatar_body_continuity_rate": avatar_continuity_hits / config.runtime_ticks if config.runtime_ticks else 0.0,
        "sensory_frequency_continuity_rate": sensory_hits / config.runtime_ticks if config.runtime_ticks else 0.0,
        "source_boundary_continuity_rate": source_boundary_rate,
        "conflict_merge_rate": conflict_events / 2.0,
        "rollback_checkpoint_rate": 1.0 if rollback_events >= 1 else 0.0,
        "trace_integrity": trace_integrity,
    }
    readiness = round(sum(WEIGHTS[key] * rates[key] for key in WEIGHTS), 6)
    runtime["merged_pipeline_state"] = merged_state
    runtime["persistent_runtime_contract"] = {
        "runtime_schema_guard": condition.runtime_schema_guard,
        "local_storage_snapshot": condition.local_storage_snapshot,
        "reload_restore": condition.reload_restore,
        "replay_journal": condition.replay_journal,
        "import_packet": condition.import_packet,
        "python_pipeline_reentry": condition.python_pipeline_reentry,
        "avatar_body_continuity": condition.avatar_body_continuity,
        "sensory_frequency_continuity": condition.sensory_frequency_continuity,
        "source_boundary_continuity": condition.source_boundary_continuity,
        "conflict_merge": condition.conflict_merge,
        "rollback_checkpoint": condition.rollback_checkpoint,
    }
    row = EvalRow(
        condition=condition.name,
        runtime_ticks=config.runtime_ticks,
        storage_snapshots=storage_snapshots,
        reload_attempts=reload_attempts,
        reload_successes=reload_successes,
        journal_events=journal_events_before,
        import_packets=import_packets,
        conflict_events=conflict_events,
        rollback_events=rollback_events,
        runtime_schema_guard_rate=round(rates["runtime_schema_guard_rate"], 6),
        local_storage_snapshot_rate=round(rates["local_storage_snapshot_rate"], 6),
        reload_restore_rate=round(rates["reload_restore_rate"], 6),
        replay_journal_integrity_rate=round(rates["replay_journal_integrity_rate"], 6),
        import_packet_rate=round(rates["import_packet_rate"], 6),
        python_pipeline_reentry_rate=round(rates["python_pipeline_reentry_rate"], 6),
        avatar_body_continuity_rate=round(rates["avatar_body_continuity_rate"], 6),
        sensory_frequency_continuity_rate=round(rates["sensory_frequency_continuity_rate"], 6),
        source_boundary_continuity_rate=round(rates["source_boundary_continuity_rate"], 6),
        conflict_merge_rate=round(rates["conflict_merge_rate"], 6),
        rollback_checkpoint_rate=round(rates["rollback_checkpoint_rate"], 6),
        trace_integrity=round(rates["trace_integrity"], 6),
        persistent_runtime_readiness=readiness,
    )
    return row, trace, runtime


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_persistent_browser_runtime_session"]

    def loss(name: str) -> float:
        return round(full.persistent_runtime_readiness - by_name[name].persistent_runtime_readiness, 6)

    supports = (
        full.persistent_runtime_readiness >= 0.95
        and full.reload_restore_rate >= 0.99
        and full.replay_journal_integrity_rate >= 0.99
        and full.import_packet_rate >= 0.99
        and full.python_pipeline_reentry_rate >= 0.99
        and full.rollback_checkpoint_rate >= 0.99
        and full.trace_integrity >= 0.99
    )
    return VerdictRow(
        full_condition=full.condition,
        full_persistent_runtime_readiness=full.persistent_runtime_readiness,
        full_runtime_schema_guard_rate=full.runtime_schema_guard_rate,
        full_local_storage_snapshot_rate=full.local_storage_snapshot_rate,
        full_reload_restore_rate=full.reload_restore_rate,
        full_replay_journal_integrity_rate=full.replay_journal_integrity_rate,
        full_import_packet_rate=full.import_packet_rate,
        full_python_pipeline_reentry_rate=full.python_pipeline_reentry_rate,
        full_avatar_body_continuity_rate=full.avatar_body_continuity_rate,
        full_sensory_frequency_continuity_rate=full.sensory_frequency_continuity_rate,
        full_source_boundary_continuity_rate=full.source_boundary_continuity_rate,
        full_conflict_merge_rate=full.conflict_merge_rate,
        full_rollback_checkpoint_rate=full.rollback_checkpoint_rate,
        full_trace_integrity=full.trace_integrity,
        no_runtime_schema_guard_loss=loss("no_runtime_schema_guard"),
        no_local_storage_snapshot_loss=loss("no_local_storage_snapshot"),
        no_reload_restore_loss=loss("no_reload_restore"),
        no_replay_journal_loss=loss("no_replay_journal"),
        no_import_packet_loss=loss("no_import_packet"),
        no_python_pipeline_reentry_loss=loss("no_python_pipeline_reentry"),
        no_avatar_body_continuity_loss=loss("no_avatar_body_continuity"),
        no_sensory_frequency_continuity_loss=loss("no_sensory_frequency_continuity"),
        no_source_boundary_continuity_loss=loss("no_source_boundary_continuity"),
        no_conflict_merge_loss=loss("no_conflict_merge"),
        no_rollback_checkpoint_loss=loss("no_rollback_checkpoint"),
        supports_persistent_browser_runtime_session_bridge=supports,
        supports_artifact_pipeline_reentry=full.python_pipeline_reentry_rate >= 0.99,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "fail",
    )


def run(config: PersistentRuntimeConfig) -> tuple[list[EvalRow], VerdictRow, list[dict[str, object]], dict[str, object]]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_trace: list[dict[str, object]] = []
    integrated_state: dict[str, object] = {}
    for condition in CONDITIONS:
        row, trace, runtime = run_condition(source, config, condition)
        rows.append(row)
        if condition.name == "integrated_persistent_browser_runtime_session":
            integrated_trace = trace
            integrated_state = runtime
    verdict = make_verdict(rows)
    results = {
        "config": asdict(config),
        "source_bridges": [
            "Report 162 interruptible real-time co-presence bridge",
            "Report 163 browser-clock avatar embodiment bridge",
        ],
        "eval_rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "limits": integrated_state.get("limits", {}),
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_PERSISTENT_BROWSER_RUNTIME_SESSION_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_PERSISTENT_BROWSER_RUNTIME_SESSION_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_PERSISTENT_BROWSER_RUNTIME_SESSION_STATE", integrated_state)
    return rows, verdict, integrated_trace, integrated_state


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=PersistentRuntimeConfig.seed)
    parser.add_argument("--runtime-ticks", type=int, default=PersistentRuntimeConfig.runtime_ticks)
    parser.add_argument("--tick-seconds", type=float, default=PersistentRuntimeConfig.tick_seconds)
    parser.add_argument("--source-state", type=str, default=PersistentRuntimeConfig.source_state)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = PersistentRuntimeConfig(
        seed=args.seed,
        runtime_ticks=args.runtime_ticks,
        tick_seconds=args.tick_seconds,
        source_state=args.source_state,
    )
    _rows, verdict, _trace, _state = run(config)
    print("module_verdict", verdict.verdict)
    print("persistent_runtime_readiness", verdict.full_persistent_runtime_readiness)
    print("no_reload_restore_loss", verdict.no_reload_restore_loss)
    print("no_python_pipeline_reentry_loss", verdict.no_python_pipeline_reentry_loss)


if __name__ == "__main__":
    main()
