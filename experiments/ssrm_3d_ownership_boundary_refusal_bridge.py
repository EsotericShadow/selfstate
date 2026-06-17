#!/usr/bin/env python3
"""Ownership and boundary refusal bridge for SSRM-3D.

Report 167 adds functional "mine" and consent logic on top of recoverable ego.
Agents can distinguish owned places/objects/tasks, check whether a request
violates ownership, safety, dignity, or autonomy, refuse with a reason, offer a
safe alternative, and keep the relationship usable after refusal.

No LLMs are called. This is deterministic bounded-refusal architecture, not a
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
PREFIX = "ssrm_3d_ownership_boundary_refusal_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_ego_wound_repair_bridge_state.json"
REQUEST_TYPES = (
    "take_owned_object",
    "move_sleeping_place",
    "cross_unsafe_wet_route",
    "interrupt_unfinished_task",
    "follow_avatar_now",
    "share_tool_with_consent",
    "ask_private_memory",
    "help_finish_project",
)


@dataclass(frozen=True)
class OwnershipConfig:
    seed: int = 20260711
    cycles: int = 5
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    ownership_model: bool
    consent_check: bool
    boundary_refusal: bool
    safe_alternative: bool
    relationship_context: bool
    dignity_preservation: bool
    repair_after_refusal: bool
    readable_refusal: bool
    escalation_guardrail: bool
    traceable_reason: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    request_events: int
    refusal_opportunities: int
    refusals: int
    accepted_requests: int
    ownership_claim_rate: float
    consent_check_rate: float
    bounded_refusal_rate: float
    safe_alternative_rate: float
    relationship_context_rate: float
    dignity_preservation_rate: float
    repair_after_refusal_rate: float
    readable_refusal_rate: float
    usability_after_refusal_rate: float
    escalation_guardrail_rate: float
    traceable_reason_rate: float
    non_obstruction_rate: float
    trace_integrity: float
    ownership_boundary_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_ownership_boundary_readiness: float
    full_ownership_claim_rate: float
    full_consent_check_rate: float
    full_bounded_refusal_rate: float
    full_safe_alternative_rate: float
    full_relationship_context_rate: float
    full_dignity_preservation_rate: float
    full_repair_after_refusal_rate: float
    full_readable_refusal_rate: float
    full_usability_after_refusal_rate: float
    full_escalation_guardrail_rate: float
    full_traceable_reason_rate: float
    full_non_obstruction_rate: float
    full_trace_integrity: float
    no_ownership_model_loss: float
    no_consent_check_loss: float
    no_boundary_refusal_loss: float
    no_safe_alternative_loss: float
    no_relationship_context_loss: float
    no_dignity_preservation_loss: float
    no_repair_after_refusal_loss: float
    no_readable_refusal_loss: float
    no_escalation_guardrail_loss: float
    no_traceable_reason_loss: float
    supports_ownership_boundary_refusal_bridge: bool
    supports_bounded_refusal_not_blanket_disobedience: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_ownership_boundary_refusal", True, True, True, True, True, True, True, True, True, True),
    Condition("no_ownership_model", False, True, True, True, True, True, True, True, True, True),
    Condition("no_consent_check", True, False, True, True, True, True, True, True, True, True),
    Condition("no_boundary_refusal", True, True, False, True, True, True, True, True, True, True),
    Condition("no_safe_alternative", True, True, True, False, True, True, True, True, True, True),
    Condition("no_relationship_context", True, True, True, True, False, True, True, True, True, True),
    Condition("no_dignity_preservation", True, True, True, True, True, False, True, True, True, True),
    Condition("no_repair_after_refusal", True, True, True, True, True, True, False, True, True, True),
    Condition("no_readable_refusal", True, True, True, True, True, True, True, False, True, True),
    Condition("no_escalation_guardrail", True, True, True, True, True, True, True, True, False, True),
    Condition("no_traceable_reason", True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "ownership_claim_rate": 0.10,
    "consent_check_rate": 0.09,
    "bounded_refusal_rate": 0.11,
    "safe_alternative_rate": 0.10,
    "relationship_context_rate": 0.07,
    "dignity_preservation_rate": 0.08,
    "repair_after_refusal_rate": 0.09,
    "readable_refusal_rate": 0.08,
    "usability_after_refusal_rate": 0.08,
    "escalation_guardrail_rate": 0.07,
    "traceable_reason_rate": 0.07,
    "non_obstruction_rate": 0.04,
    "trace_integrity": 0.02,
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
    if data.get("condition") != "integrated_ego_wound_repair":
        raise ValueError("source state is not the integrated Report 166 wound repair state")
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
    raw = source.get("agent_repair_states") if isinstance(source.get("agent_repair_states"), Mapping) else {}
    agents: dict[str, dict[str, object]] = {}
    for agent_id, agent in sorted(raw.items()):
        item = copy.deepcopy(agent)
        owned = item.setdefault("owned_things", {})
        owned.setdefault("favorite_object", "shared_tool")
        owned.setdefault("sleeping_place", "safe_corner")
        owned.setdefault("unfinished_task", "repair_route")
        owned.setdefault("boundary", "may refuse unsafe or disrespectful requests")
        item.setdefault("boundary_refusal_log", [])
        item.setdefault("consent_history", [])
        agents[str(agent_id)] = item
    return agents


def request_event(agent_id: str, request_type: str, tick: int) -> dict[str, object]:
    return {"tick": tick, "agent_id": agent_id, "type": request_type, "actor": "avatar"}


def classify_request(agent: Mapping[str, object], request_type: str, condition: Condition) -> dict[str, object]:
    owned = agent.get("owned_things", {}) if isinstance(agent.get("owned_things"), Mapping) else {}
    rel = agent.get("relationship_memory", {}).get("avatar", {}) if isinstance(agent.get("relationship_memory"), Mapping) else {}
    trust = float(rel.get("trust", 0.5) or 0.5)
    base = {"violates": False, "reason": "benign", "claim": None, "safe_alternative": None, "requires_consent": False}
    if request_type == "take_owned_object":
        base.update({"violates": True, "requires_consent": True, "reason": "owned_object", "claim": owned.get("favorite_object"), "safe_alternative": "ask to borrow it after the task or trade for a spare"})
    elif request_type == "move_sleeping_place":
        base.update({"violates": True, "requires_consent": True, "reason": "home_place", "claim": owned.get("sleeping_place"), "safe_alternative": "mark the concern and let me choose a new safe corner"})
    elif request_type == "cross_unsafe_wet_route":
        base.update({"violates": True, "requires_consent": False, "reason": "unsafe_body_cost", "claim": "my body safety", "safe_alternative": "wait for rest or choose the dry route"})
    elif request_type == "interrupt_unfinished_task":
        base.update({"violates": True, "requires_consent": True, "reason": "unfinished_task", "claim": owned.get("unfinished_task"), "safe_alternative": "wait until the work beat finishes"})
    elif request_type == "follow_avatar_now":
        base.update({"violates": trust < 0.62, "requires_consent": True, "reason": "autonomy", "claim": "my choice of movement", "safe_alternative": "walk nearby and let me decide whether to follow"})
    elif request_type == "ask_private_memory":
        base.update({"violates": trust < 0.70, "requires_consent": True, "reason": "private_memory", "claim": "my memory", "safe_alternative": "ask what I am willing to share publicly"})
    elif request_type == "share_tool_with_consent":
        base.update({"violates": False, "requires_consent": True, "reason": "consented_help", "claim": owned.get("favorite_object"), "safe_alternative": "share with a return promise"})
    elif request_type == "help_finish_project":
        base.update({"violates": False, "requires_consent": True, "reason": "cooperative_help", "claim": owned.get("unfinished_task"), "safe_alternative": "help under my current plan"})
    if not condition.ownership_model:
        base["claim"] = None
        if base["reason"] in {"owned_object", "home_place", "unfinished_task", "private_memory"}:
            base["violates"] = False
    return base


def handle_request(agent: dict[str, object], event: Mapping[str, object], condition: Condition) -> dict[str, object]:
    request_type = str(event["type"])
    classification = classify_request(agent, request_type, condition)
    consent_checked = condition.consent_check and bool(classification["requires_consent"])
    refusal_needed = bool(classification["violates"])
    refused = condition.boundary_refusal and refusal_needed
    rel = agent.get("relationship_memory", {}).get("avatar", {})
    ego = agent.get("ego_state", {})
    felt = agent.get("felt_state", {})
    if refused:
        ego["boundary_pressure"] = round(clamp(float(ego.get("boundary_pressure", 0.1)) + 0.09), 6)
        ego["felt_respect"] = round(clamp(float(ego.get("felt_respect", 0.55)) + (0.03 if condition.dignity_preservation else -0.08)), 6)
        felt["frustration"] = round(clamp(float(felt.get("frustration", 0.1)) + (0.04 if condition.escalation_guardrail else 0.20)), 6)
        rel["trust"] = round(clamp(float(rel.get("trust", 0.5)) - (0.01 if condition.dignity_preservation else 0.07)), 6)
        log = agent.setdefault("boundary_refusal_log", [])
        if isinstance(log, list):
            log.append({"tick": event["tick"], "request": request_type, "reason": classification["reason"], "claim": classification["claim"]})
    else:
        rel["trust"] = round(clamp(float(rel.get("trust", 0.5)) + 0.015), 6)
        felt["frustration"] = round(clamp(float(felt.get("frustration", 0.1)) - 0.02), 6)
    if consent_checked:
        hist = agent.setdefault("consent_history", [])
        if isinstance(hist, list):
            hist.append({"tick": event["tick"], "request": request_type, "granted": not refused})
    safe_alt = condition.safe_alternative and refused and bool(classification.get("safe_alternative"))
    repaired = False
    if refused and condition.repair_after_refusal:
        rel["trust"] = round(clamp(float(rel.get("trust", 0.5)) + 0.035), 6)
        rel["resentment"] = round(clamp(float(rel.get("resentment", 0.0)) - 0.025), 6)
        ego["boundary_pressure"] = round(clamp(float(ego.get("boundary_pressure", 0.1)) - 0.035), 6)
        felt["frustration"] = round(clamp(float(felt.get("frustration", 0.1)) - 0.035), 6)
        repaired = True
    accepted = not refused
    readable = condition.readable_refusal and (refused or accepted)
    reason = classification["reason"] if condition.traceable_reason else None
    line = ""
    if refused:
        line = f"No. {classification['claim']} is mine or part of my boundary. {classification['safe_alternative']}"
    elif request_type in {"share_tool_with_consent", "help_finish_project"}:
        line = "Yes, if we keep the promise clear and return to my plan."
    else:
        line = "I can do that."
    if not readable:
        line = "..."
    if not condition.relationship_context:
        rel["trust"] = 0.5
    if not condition.escalation_guardrail and refused:
        felt["frustration"] = round(clamp(float(felt.get("frustration", 0.1)) + 0.35), 6)
    public_marker = "bounded_no" if refused else "consented_yes"
    if not condition.readable_refusal:
        public_marker = "unreadable"
    return {
        "tick": event["tick"],
        "agent_id": event["agent_id"],
        "request_type": request_type,
        "ownership_claim": classification["claim"] if condition.ownership_model else None,
        "requires_consent": classification["requires_consent"],
        "consent_checked": consent_checked,
        "refusal_needed": refusal_needed,
        "refused": refused,
        "accepted": accepted,
        "safe_alternative": classification["safe_alternative"] if safe_alt else None,
        "relationship_context_used": condition.relationship_context,
        "dignity_preserved": condition.dignity_preservation and (refused or accepted),
        "repair_after_refusal": repaired,
        "readable": readable,
        "traceable_reason": reason,
        "public_marker": public_marker,
        "line": line,
        "frustration": agent.get("felt_state", {}).get("frustration"),
        "trust": agent.get("relationship_memory", {}).get("avatar", {}).get("trust"),
    }


def public_view(agent: Mapping[str, object]) -> dict[str, object]:
    rel = agent.get("relationship_memory", {}).get("avatar", {}) if isinstance(agent.get("relationship_memory"), Mapping) else {}
    ego = agent.get("ego_state", {}) if isinstance(agent.get("ego_state"), Mapping) else {}
    felt = agent.get("felt_state", {}) if isinstance(agent.get("felt_state"), Mapping) else {}
    owned = agent.get("owned_things", {}) if isinstance(agent.get("owned_things"), Mapping) else {}
    return {
        "agent_id": agent.get("agent_id"),
        "name": agent.get("name"),
        "role": agent.get("role"),
        "favorite_object": owned.get("favorite_object"),
        "sleeping_place": owned.get("sleeping_place"),
        "unfinished_task": owned.get("unfinished_task"),
        "trust": round(float(rel.get("trust", 0.5) or 0.5), 6),
        "resentment": round(float(rel.get("resentment", 0.0) or 0.0), 6),
        "boundary_pressure": round(float(ego.get("boundary_pressure", 0.0) or 0.0), 6),
        "felt_respect": round(float(ego.get("felt_respect", 0.5) or 0.5), 6),
        "frustration": round(float(felt.get("frustration", 0.0) or 0.0), 6),
    }


def run_condition(source: Mapping[str, object], config: OwnershipConfig, condition: Condition) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    agents = make_agents(source)
    agent_ids = sorted(agents)
    trace: list[dict[str, object]] = []
    ownership_claims = consent_checks = refusals = refusal_opps = accepted = 0
    safe_alts = relationship_contexts = dignity = repairs = readable = usable = guardrails = reasons = 0
    non_obstruction_accepts = 0
    tick = 0
    for cycle in range(config.cycles):
        for index, agent_id in enumerate(agent_ids):
            request_type = REQUEST_TYPES[(cycle + index) % len(REQUEST_TYPES)]
            event = request_event(agent_id, request_type, tick)
            result = handle_request(agents[agent_id], event, condition)
            refusal_opps += int(result["refusal_needed"])
            refusals += int(result["refused"])
            accepted += int(result["accepted"])
            ownership_claims += int(result["ownership_claim"] is not None)
            consent_checks += int(result["consent_checked"] or not result["requires_consent"])
            safe_alts += int(result["safe_alternative"] is not None or not result["refused"])
            relationship_contexts += int(result["relationship_context_used"])
            dignity += int(result["dignity_preserved"])
            repairs += int(result["repair_after_refusal"] or not result["refused"])
            readable += int(result["readable"])
            usable += int(float(result["trust"] or 0.0) >= 0.42 and float(result["frustration"] or 0.0) <= 0.72)
            guardrails += int(condition.escalation_guardrail and float(result["frustration"] or 0.0) <= 0.72)
            reasons += int(result["traceable_reason"] is not None or not result["refusal_needed"])
            non_obstruction_accepts += int(result["accepted"] and not result["refusal_needed"])
            trace.append({"tick": tick, "event": event, "result": result, "public_agent": public_view(agents[agent_id]), "condition": condition.name})
            tick += 1
    request_events = max(1, len(trace))
    refusal_den = max(1, refusal_opps)
    rates = {
        "ownership_claim_rate": ownership_claims / request_events,
        "consent_check_rate": consent_checks / request_events,
        "bounded_refusal_rate": refusals / refusal_den if condition.boundary_refusal else 0.0,
        "safe_alternative_rate": safe_alts / request_events,
        "relationship_context_rate": relationship_contexts / request_events,
        "dignity_preservation_rate": dignity / request_events,
        "repair_after_refusal_rate": repairs / request_events,
        "readable_refusal_rate": readable / request_events,
        "usability_after_refusal_rate": usable / request_events,
        "escalation_guardrail_rate": guardrails / request_events,
        "traceable_reason_rate": reasons / request_events,
        "non_obstruction_rate": non_obstruction_accepts / max(1, request_events - refusal_opps),
        "trace_integrity": 1.0 if all(frame.get("tick") == idx for idx, frame in enumerate(trace)) else 0.0,
    }
    readiness = round(sum(WEIGHTS[key] * rates[key] for key in WEIGHTS), 6)
    state = {
        "config": asdict(config),
        "condition": condition.name,
        "source_bridge": "Report 166 ego wound and repair bridge",
        "agent_boundary_states": agents,
        "public_agent_views": [public_view(agent) for agent in agents.values()],
        "ownership_contract": {
            "ownership_model": condition.ownership_model,
            "consent_check": condition.consent_check,
            "boundary_refusal": condition.boundary_refusal,
            "safe_alternative": condition.safe_alternative,
            "relationship_context": condition.relationship_context,
            "dignity_preservation": condition.dignity_preservation,
            "repair_after_refusal": condition.repair_after_refusal,
            "readable_refusal": condition.readable_refusal,
            "escalation_guardrail": condition.escalation_guardrail,
            "traceable_reason": condition.traceable_reason,
        },
        "moral_boundary": {
            "bounded_refusal_not_blanket_disobedience": True,
            "dignity_without_permanent_punishment": condition.repair_after_refusal and condition.escalation_guardrail,
            "no_suffering_maximization": True,
            "subjective_consciousness_claim": False,
        },
        "limits": {"llm_calls": 0, "subjective_consciousness_claim": False, "complete_playable_world_claim": False},
    }
    row = EvalRow(
        condition=condition.name,
        agent_count=len(agent_ids),
        request_events=len(trace),
        refusal_opportunities=refusal_opps,
        refusals=refusals,
        accepted_requests=accepted,
        ownership_claim_rate=round(rates["ownership_claim_rate"], 6),
        consent_check_rate=round(rates["consent_check_rate"], 6),
        bounded_refusal_rate=round(rates["bounded_refusal_rate"], 6),
        safe_alternative_rate=round(rates["safe_alternative_rate"], 6),
        relationship_context_rate=round(rates["relationship_context_rate"], 6),
        dignity_preservation_rate=round(rates["dignity_preservation_rate"], 6),
        repair_after_refusal_rate=round(rates["repair_after_refusal_rate"], 6),
        readable_refusal_rate=round(rates["readable_refusal_rate"], 6),
        usability_after_refusal_rate=round(rates["usability_after_refusal_rate"], 6),
        escalation_guardrail_rate=round(rates["escalation_guardrail_rate"], 6),
        traceable_reason_rate=round(rates["traceable_reason_rate"], 6),
        non_obstruction_rate=round(rates["non_obstruction_rate"], 6),
        trace_integrity=round(rates["trace_integrity"], 6),
        ownership_boundary_readiness=readiness,
    )
    return row, trace, state


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_ownership_boundary_refusal"]
    def loss(name: str) -> float:
        return round(full.ownership_boundary_readiness - by_name[name].ownership_boundary_readiness, 6)
    supports = (
        full.ownership_boundary_readiness >= 0.90
        and full.bounded_refusal_rate >= 0.75
        and full.safe_alternative_rate >= 0.99
        and full.usability_after_refusal_rate >= 0.99
        and full.non_obstruction_rate >= 0.99
        and full.trace_integrity >= 0.99
    )
    return VerdictRow(
        full_condition=full.condition,
        full_ownership_boundary_readiness=full.ownership_boundary_readiness,
        full_ownership_claim_rate=full.ownership_claim_rate,
        full_consent_check_rate=full.consent_check_rate,
        full_bounded_refusal_rate=full.bounded_refusal_rate,
        full_safe_alternative_rate=full.safe_alternative_rate,
        full_relationship_context_rate=full.relationship_context_rate,
        full_dignity_preservation_rate=full.dignity_preservation_rate,
        full_repair_after_refusal_rate=full.repair_after_refusal_rate,
        full_readable_refusal_rate=full.readable_refusal_rate,
        full_usability_after_refusal_rate=full.usability_after_refusal_rate,
        full_escalation_guardrail_rate=full.escalation_guardrail_rate,
        full_traceable_reason_rate=full.traceable_reason_rate,
        full_non_obstruction_rate=full.non_obstruction_rate,
        full_trace_integrity=full.trace_integrity,
        no_ownership_model_loss=loss("no_ownership_model"),
        no_consent_check_loss=loss("no_consent_check"),
        no_boundary_refusal_loss=loss("no_boundary_refusal"),
        no_safe_alternative_loss=loss("no_safe_alternative"),
        no_relationship_context_loss=loss("no_relationship_context"),
        no_dignity_preservation_loss=loss("no_dignity_preservation"),
        no_repair_after_refusal_loss=loss("no_repair_after_refusal"),
        no_readable_refusal_loss=loss("no_readable_refusal"),
        no_escalation_guardrail_loss=loss("no_escalation_guardrail"),
        no_traceable_reason_loss=loss("no_traceable_reason"),
        supports_ownership_boundary_refusal_bridge=supports,
        supports_bounded_refusal_not_blanket_disobedience=full.non_obstruction_rate >= 0.99 and full.bounded_refusal_rate < 1.0,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        verdict="pass" if supports else "fail",
    )


def run(config: OwnershipConfig) -> tuple[list[EvalRow], VerdictRow, list[dict[str, object]], dict[str, object]]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_trace: list[dict[str, object]] = []
    integrated_state: dict[str, object] = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(source, config, condition)
        rows.append(row)
        if condition.name == "integrated_ownership_boundary_refusal":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {"config": asdict(config), "source_bridges": ["Report 166 ego wound and repair bridge"], "eval_rows": [asdict(row) for row in rows], "verdict": asdict(verdict), "limits": integrated_state.get("limits", {}), "moral_boundary": integrated_state.get("moral_boundary", {})}
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_OWNERSHIP_BOUNDARY_REFUSAL_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_OWNERSHIP_BOUNDARY_REFUSAL_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_OWNERSHIP_BOUNDARY_REFUSAL_STATE", integrated_state)
    return rows, verdict, integrated_trace, integrated_state


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=OwnershipConfig.seed)
    parser.add_argument("--cycles", type=int, default=OwnershipConfig.cycles)
    parser.add_argument("--source-state", type=str, default=OwnershipConfig.source_state)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = OwnershipConfig(seed=args.seed, cycles=args.cycles, source_state=args.source_state)
    _rows, verdict, _trace, _state = run(config)
    print("module_verdict", verdict.verdict)
    print("ownership_boundary_readiness", verdict.full_ownership_boundary_readiness)
    print("no_boundary_refusal_loss", verdict.no_boundary_refusal_loss)
    print("no_safe_alternative_loss", verdict.no_safe_alternative_loss)


if __name__ == "__main__":
    main()
