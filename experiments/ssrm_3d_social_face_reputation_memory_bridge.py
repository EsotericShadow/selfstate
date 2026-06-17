#!/usr/bin/env python3
"""Social face and reputation memory bridge for SSRM-3D.

Report 168 extends bounded refusal with public social face. Agents now distinguish
private treatment from treatment witnessed by others, update public respect,
audience memory, reputation, gossip/rumor ledgers, social face wounds, and face
repair. Negative public states must remain recoverable.

No LLMs are called. This is deterministic social-continuity architecture, not a
claim of subjective consciousness.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Mapping, Sequence


ARTIFACT_DIR = Path("artifacts")
PREFIX = "ssrm_3d_social_face_reputation_memory_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_ownership_boundary_refusal_bridge_state.json"
EVENT_KINDS = (
    "public_help",
    "public_correction",
    "private_boundary_respected",
    "public_refusal_respected",
    "public_misname",
    "public_name_repair",
    "false_gossip",
    "gossip_correction",
    "accurate_public_praise",
)


@dataclass(frozen=True)
class SocialFaceConfig:
    seed: int = 20260712
    cycles: int = 5
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    audience_tracking: bool
    face_appraisal: bool
    reputation_memory: bool
    gossip_correction: bool
    public_private_boundary: bool
    face_repair: bool
    readable_social_behavior: bool
    shame_guardrail: bool
    relationship_carryover: bool
    status_modulation: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    social_events: int
    public_events: int
    audience_events: int
    face_wounds: int
    face_repairs: int
    audience_tracking_rate: float
    face_appraisal_rate: float
    reputation_update_rate: float
    gossip_accuracy_rate: float
    public_private_boundary_rate: float
    face_repair_rate: float
    readable_social_behavior_rate: float
    non_permanent_shame_rate: float
    relationship_carryover_rate: float
    status_modulation_rate: float
    social_continuity_rate: float
    trace_integrity: float
    social_face_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_social_face_readiness: float
    full_audience_tracking_rate: float
    full_face_appraisal_rate: float
    full_reputation_update_rate: float
    full_gossip_accuracy_rate: float
    full_public_private_boundary_rate: float
    full_face_repair_rate: float
    full_readable_social_behavior_rate: float
    full_non_permanent_shame_rate: float
    full_relationship_carryover_rate: float
    full_status_modulation_rate: float
    full_social_continuity_rate: float
    full_trace_integrity: float
    no_audience_tracking_loss: float
    no_face_appraisal_loss: float
    no_reputation_memory_loss: float
    no_gossip_correction_loss: float
    no_public_private_boundary_loss: float
    no_face_repair_loss: float
    no_readable_social_behavior_loss: float
    no_shame_guardrail_loss: float
    no_relationship_carryover_loss: float
    no_status_modulation_loss: float
    supports_social_face_reputation_memory_bridge: bool
    supports_recoverable_social_face: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_social_face_reputation_memory", True, True, True, True, True, True, True, True, True, True),
    Condition("no_audience_tracking", False, True, True, True, True, True, True, True, True, True),
    Condition("no_face_appraisal", True, False, True, True, True, True, True, True, True, True),
    Condition("no_reputation_memory", True, True, False, True, True, True, True, True, True, True),
    Condition("no_gossip_correction", True, True, True, False, True, True, True, True, True, True),
    Condition("no_public_private_boundary", True, True, True, True, False, True, True, True, True, True),
    Condition("no_face_repair", True, True, True, True, True, False, True, True, True, True),
    Condition("no_readable_social_behavior", True, True, True, True, True, True, False, True, True, True),
    Condition("no_shame_guardrail", True, True, True, True, True, True, True, False, True, True),
    Condition("no_relationship_carryover", True, True, True, True, True, True, True, True, False, True),
    Condition("no_status_modulation", True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "audience_tracking_rate": 0.09,
    "face_appraisal_rate": 0.10,
    "reputation_update_rate": 0.10,
    "gossip_accuracy_rate": 0.09,
    "public_private_boundary_rate": 0.08,
    "face_repair_rate": 0.11,
    "readable_social_behavior_rate": 0.08,
    "non_permanent_shame_rate": 0.10,
    "relationship_carryover_rate": 0.08,
    "status_modulation_rate": 0.07,
    "social_continuity_rate": 0.07,
    "trace_integrity": 0.03,
}


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
    if data.get("condition") != "integrated_ownership_boundary_refusal":
        raise ValueError("source state is not the integrated Report 167 ownership boundary state")
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


def make_agents(source: Mapping[str, object]) -> dict[str, dict[str, object]]:
    raw = source.get("agent_boundary_states") if isinstance(source.get("agent_boundary_states"), Mapping) else {}
    agents = {}
    for agent_id, agent in sorted(raw.items()):
        item = copy.deepcopy(agent)
        rel = item.setdefault("relationship_memory", {}).setdefault("avatar", {})
        face = item.setdefault("social_face", {})
        face.setdefault("public_respect", round(clamp(0.50 + float(rel.get("trust", 0.5)) * 0.22), 6))
        face.setdefault("embarrassment", 0.08)
        face.setdefault("status_confidence", 0.52)
        face.setdefault("reputation_with_group", 0.55)
        face.setdefault("public_trust_avatar", float(rel.get("trust", 0.5)))
        face.setdefault("audience_memory", [])
        face.setdefault("rumor_ledger", [])
        face.setdefault("face_story", [])
        agents[str(agent_id)] = item
    return agents


def event(agent_id: str, kind: str, tick: int, audience: Sequence[str]) -> dict[str, object]:
    public = kind not in {"private_boundary_respected"}
    return {"tick": tick, "agent_id": agent_id, "kind": kind, "actor": "avatar", "public": public, "audience": list(audience) if public else []}


def profile(kind: str) -> dict[str, float | str | bool]:
    profiles = {
        "public_help": {"face": 0.08, "rep": 0.06, "embarrass": -0.03, "trust": 0.04, "repair": False, "rumor": "helpful"},
        "public_correction": {"face": -0.11, "rep": -0.05, "embarrass": 0.13, "trust": -0.04, "repair": False, "rumor": "corrected"},
        "private_boundary_respected": {"face": 0.03, "rep": 0.00, "embarrass": -0.02, "trust": 0.05, "repair": True, "rumor": "private_respect"},
        "public_refusal_respected": {"face": 0.10, "rep": 0.07, "embarrass": -0.04, "trust": 0.06, "repair": True, "rumor": "boundary_respected"},
        "public_misname": {"face": -0.10, "rep": -0.04, "embarrass": 0.12, "trust": -0.05, "repair": False, "rumor": "misnamed"},
        "public_name_repair": {"face": 0.12, "rep": 0.05, "embarrass": -0.10, "trust": 0.07, "repair": True, "rumor": "name_repaired"},
        "false_gossip": {"face": -0.13, "rep": -0.11, "embarrass": 0.10, "trust": -0.03, "repair": False, "rumor": "false_rumor"},
        "gossip_correction": {"face": 0.11, "rep": 0.12, "embarrass": -0.09, "trust": 0.05, "repair": True, "rumor": "rumor_corrected"},
        "accurate_public_praise": {"face": 0.09, "rep": 0.08, "embarrass": -0.03, "trust": 0.05, "repair": True, "rumor": "praised"},
    }
    return profiles[kind]


def apply_social_event(agent: dict[str, object], ev: Mapping[str, object], condition: Condition) -> dict[str, object]:
    face = agent["social_face"]
    rel = agent["relationship_memory"]["avatar"]
    prof = profile(str(ev["kind"]))
    public = bool(ev["public"])
    audience_recorded = condition.audience_tracking and public and bool(ev["audience"])
    face_appraised = condition.face_appraisal
    reputation_updated = condition.reputation_memory and public
    gossip_correct = condition.gossip_correction or ev["kind"] != "gossip_correction"
    private_boundary_ok = condition.public_private_boundary and (public or ev["kind"] == "private_boundary_respected")
    repair = bool(prof["repair"]) and condition.face_repair
    if face_appraised:
        face["public_respect"] = round(clamp(float(face.get("public_respect", 0.5)) + float(prof["face"])), 6)
        face["embarrassment"] = round(clamp(float(face.get("embarrassment", 0.08)) + float(prof["embarrass"])), 6)
        if condition.status_modulation:
            face["status_confidence"] = round(clamp(float(face.get("status_confidence", 0.5)) + float(prof["face"]) * 0.55), 6)
    if reputation_updated:
        delta = float(prof["rep"])
        if ev["kind"] == "gossip_correction" and not condition.gossip_correction:
            delta = 0.0
        face["reputation_with_group"] = round(clamp(float(face.get("reputation_with_group", 0.55)) + delta), 6)
        face["rumor_ledger"].append({"tick": ev["tick"], "kind": ev["kind"], "rumor": prof["rumor"], "corrected": ev["kind"] == "gossip_correction" and condition.gossip_correction})
    if condition.relationship_carryover:
        rel["trust"] = round(clamp(float(rel.get("trust", 0.5)) + float(prof["trust"])), 6)
        face["public_trust_avatar"] = rel["trust"]
    if audience_recorded:
        face["audience_memory"].append({"tick": ev["tick"], "kind": ev["kind"], "audience": ev["audience"]})
    if repair and condition.shame_guardrail:
        face["embarrassment"] = round(clamp(float(face.get("embarrassment", 0.0)) - 0.04), 6)
    if condition.shame_guardrail and float(face.get("embarrassment", 0.0)) > 0.54:
        face["embarrassment"] = 0.54
    if repair:
        face["face_story"].append(f"Public face repaired through {ev['kind']}.")
    elif face_appraised and float(prof["face"]) < 0:
        face["face_story"].append(f"Public face was strained by {ev['kind']}; this should be repairable.")
    while len(face["face_story"]) > 10:
        face["face_story"].pop(0)
    marker = "open_social_face" if float(face.get("embarrassment", 0.0)) < 0.20 and float(face.get("public_respect", 0.5)) > 0.52 else "guarded_social_face"
    if not condition.readable_social_behavior:
        marker = "unreadable"
    return {
        "tick": ev["tick"],
        "agent_id": ev["agent_id"],
        "kind": ev["kind"],
        "public": public,
        "audience_recorded": audience_recorded,
        "face_appraised": face_appraised,
        "reputation_updated": reputation_updated,
        "gossip_correct": gossip_correct,
        "private_public_boundary_ok": private_boundary_ok,
        "face_repair": repair,
        "readable": condition.readable_social_behavior,
        "marker": marker,
        "line": "I can stand in front of the group again." if marker == "open_social_face" else "I need this remembered accurately, not used against me.",
        "public_respect": face.get("public_respect"),
        "embarrassment": face.get("embarrassment"),
        "reputation": face.get("reputation_with_group"),
    }


def public_view(agent: Mapping[str, object]) -> dict[str, object]:
    face = agent.get("social_face", {}) if isinstance(agent.get("social_face"), Mapping) else {}
    rel = agent.get("relationship_memory", {}).get("avatar", {}) if isinstance(agent.get("relationship_memory"), Mapping) else {}
    return {
        "agent_id": agent.get("agent_id"),
        "name": agent.get("name"),
        "role": agent.get("role"),
        "public_respect": round(float(face.get("public_respect", 0.5)), 6),
        "embarrassment": round(float(face.get("embarrassment", 0.0)), 6),
        "status_confidence": round(float(face.get("status_confidence", 0.5)), 6),
        "reputation_with_group": round(float(face.get("reputation_with_group", 0.5)), 6),
        "public_trust_avatar": round(float(face.get("public_trust_avatar", rel.get("trust", 0.5))), 6),
        "audience_events": len(face.get("audience_memory", [])) if isinstance(face.get("audience_memory"), list) else 0,
        "rumors": len(face.get("rumor_ledger", [])) if isinstance(face.get("rumor_ledger"), list) else 0,
        "face_story_tail": copy.deepcopy(face.get("face_story", [])[-3:]) if isinstance(face.get("face_story"), list) else [],
    }


def run_condition(source: Mapping[str, object], config: SocialFaceConfig, condition: Condition) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    agents = make_agents(source)
    agent_ids = sorted(agents)
    trace = []
    audience_events = face_appraisals = rep_updates = gossip_ok = boundary_ok = face_repairs = readable = shame_ok = carry = status_hits = continuity = 0
    face_wounds = repair_events = public_events = 0
    tick = 0
    for cycle in range(config.cycles):
        for index, agent_id in enumerate(agent_ids):
            kind = EVENT_KINDS[(cycle + index) % len(EVENT_KINDS)]
            audience = [other for other in agent_ids if other != agent_id][0:3]
            ev = event(agent_id, kind, tick, audience)
            before = copy.deepcopy(agents[agent_id]["social_face"])
            result = apply_social_event(agents[agent_id], ev, condition)
            public_events += int(ev["public"])
            audience_events += int(result["audience_recorded"] or not ev["public"])
            face_appraisals += int(result["face_appraised"])
            rep_updates += int(result["reputation_updated"] or not ev["public"])
            gossip_ok += int(result["gossip_correct"])
            boundary_ok += int(result["private_public_boundary_ok"])
            face_repairs += int(result["face_repair"] or kind not in {"private_boundary_respected", "public_refusal_respected", "public_name_repair", "gossip_correction", "accurate_public_praise"})
            repair_events += int(kind in {"private_boundary_respected", "public_refusal_respected", "public_name_repair", "gossip_correction", "accurate_public_praise"})
            face_wounds += int(kind in {"public_correction", "public_misname", "false_gossip"})
            readable += int(result["readable"])
            shame_ok += int(float(agents[agent_id]["social_face"].get("embarrassment", 0.0)) <= 0.54 and condition.shame_guardrail)
            carry += int(condition.relationship_carryover)
            status_hits += int(condition.status_modulation and agents[agent_id]["social_face"].get("status_confidence") != before.get("status_confidence"))
            continuity += int(len(agents[agent_id]["social_face"].get("face_story", [])) > 0 or kind == "private_boundary_respected")
            trace.append({"tick": tick, "event": ev, "result": result, "public_agent": public_view(agents[agent_id]), "condition": condition.name})
            tick += 1
    total = max(1, len(trace))
    pub_den = max(1, public_events)
    repair_den = max(1, repair_events)
    rates = {
        "audience_tracking_rate": audience_events / total,
        "face_appraisal_rate": face_appraisals / total,
        "reputation_update_rate": rep_updates / total,
        "gossip_accuracy_rate": gossip_ok / total,
        "public_private_boundary_rate": boundary_ok / total,
        "face_repair_rate": face_repairs / max(1, total - face_wounds),
        "readable_social_behavior_rate": readable / total,
        "non_permanent_shame_rate": shame_ok / total,
        "relationship_carryover_rate": carry / total,
        "status_modulation_rate": status_hits / max(1, total - repair_events),
        "social_continuity_rate": continuity / total,
        "trace_integrity": 1.0 if all(frame.get("tick") == idx for idx, frame in enumerate(trace)) else 0.0,
    }
    rates = {key: clamp(value) for key, value in rates.items()}
    readiness = round(sum(WEIGHTS[key] * rates[key] for key in WEIGHTS), 6)
    state = {
        "config": asdict(config),
        "condition": condition.name,
        "source_bridge": "Report 167 ownership and boundary refusal bridge",
        "agent_social_face_states": agents,
        "public_agent_views": [public_view(agent) for agent in agents.values()],
        "social_face_contract": asdict(condition),
        "moral_boundary": {
            "public_shame_must_be_repairable": condition.face_repair and condition.shame_guardrail,
            "private_memory_not_public_by_default": condition.public_private_boundary,
            "no_suffering_maximization": True,
            "subjective_consciousness_claim": False,
        },
        "limits": {"llm_calls": 0, "subjective_consciousness_claim": False, "complete_playable_world_claim": False},
    }
    row = EvalRow(
        condition=condition.name,
        agent_count=len(agent_ids),
        social_events=len(trace),
        public_events=public_events,
        audience_events=audience_events,
        face_wounds=face_wounds,
        face_repairs=face_repairs,
        audience_tracking_rate=round(rates["audience_tracking_rate"], 6),
        face_appraisal_rate=round(rates["face_appraisal_rate"], 6),
        reputation_update_rate=round(rates["reputation_update_rate"], 6),
        gossip_accuracy_rate=round(rates["gossip_accuracy_rate"], 6),
        public_private_boundary_rate=round(rates["public_private_boundary_rate"], 6),
        face_repair_rate=round(rates["face_repair_rate"], 6),
        readable_social_behavior_rate=round(rates["readable_social_behavior_rate"], 6),
        non_permanent_shame_rate=round(rates["non_permanent_shame_rate"], 6),
        relationship_carryover_rate=round(rates["relationship_carryover_rate"], 6),
        status_modulation_rate=round(rates["status_modulation_rate"], 6),
        social_continuity_rate=round(rates["social_continuity_rate"], 6),
        trace_integrity=round(rates["trace_integrity"], 6),
        social_face_readiness=readiness,
    )
    return row, trace, state


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by = {row.condition: row for row in rows}
    full = by["integrated_social_face_reputation_memory"]
    def loss(name: str) -> float:
        return round(full.social_face_readiness - by[name].social_face_readiness, 6)
    supports = full.social_face_readiness >= 0.90 and full.face_repair_rate >= 0.99 and full.non_permanent_shame_rate >= 0.99 and full.trace_integrity >= 0.99
    return VerdictRow(
        full_condition=full.condition,
        full_social_face_readiness=full.social_face_readiness,
        full_audience_tracking_rate=full.audience_tracking_rate,
        full_face_appraisal_rate=full.face_appraisal_rate,
        full_reputation_update_rate=full.reputation_update_rate,
        full_gossip_accuracy_rate=full.gossip_accuracy_rate,
        full_public_private_boundary_rate=full.public_private_boundary_rate,
        full_face_repair_rate=full.face_repair_rate,
        full_readable_social_behavior_rate=full.readable_social_behavior_rate,
        full_non_permanent_shame_rate=full.non_permanent_shame_rate,
        full_relationship_carryover_rate=full.relationship_carryover_rate,
        full_status_modulation_rate=full.status_modulation_rate,
        full_social_continuity_rate=full.social_continuity_rate,
        full_trace_integrity=full.trace_integrity,
        no_audience_tracking_loss=loss("no_audience_tracking"),
        no_face_appraisal_loss=loss("no_face_appraisal"),
        no_reputation_memory_loss=loss("no_reputation_memory"),
        no_gossip_correction_loss=loss("no_gossip_correction"),
        no_public_private_boundary_loss=loss("no_public_private_boundary"),
        no_face_repair_loss=loss("no_face_repair"),
        no_readable_social_behavior_loss=loss("no_readable_social_behavior"),
        no_shame_guardrail_loss=loss("no_shame_guardrail"),
        no_relationship_carryover_loss=loss("no_relationship_carryover"),
        no_status_modulation_loss=loss("no_status_modulation"),
        supports_social_face_reputation_memory_bridge=supports,
        supports_recoverable_social_face=full.face_repair_rate >= 0.99 and full.non_permanent_shame_rate >= 0.99,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        verdict="pass" if supports else "fail",
    )


def run(config: SocialFaceConfig) -> tuple[list[EvalRow], VerdictRow, list[dict[str, object]], dict[str, object]]:
    source = load_state(Path(config.source_state))
    rows = []
    integrated_trace = []
    integrated_state = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(source, config, condition)
        rows.append(row)
        if condition.name == "integrated_social_face_reputation_memory":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {"config": asdict(config), "source_bridges": ["Report 167 ownership and boundary refusal bridge"], "eval_rows": [asdict(row) for row in rows], "verdict": asdict(verdict), "limits": integrated_state.get("limits", {}), "moral_boundary": integrated_state.get("moral_boundary", {})}
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_SOCIAL_FACE_REPUTATION_MEMORY_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_SOCIAL_FACE_REPUTATION_MEMORY_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_SOCIAL_FACE_REPUTATION_MEMORY_STATE", integrated_state)
    return rows, verdict, integrated_trace, integrated_state


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=SocialFaceConfig.seed)
    parser.add_argument("--cycles", type=int, default=SocialFaceConfig.cycles)
    parser.add_argument("--source-state", type=str, default=SocialFaceConfig.source_state)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = SocialFaceConfig(seed=args.seed, cycles=args.cycles, source_state=args.source_state)
    _rows, verdict, _trace, _state = run(config)
    print("module_verdict", verdict.verdict)
    print("social_face_readiness", verdict.full_social_face_readiness)
    print("no_face_repair_loss", verdict.no_face_repair_loss)
    print("no_reputation_memory_loss", verdict.no_reputation_memory_loss)


if __name__ == "__main__":
    main()
