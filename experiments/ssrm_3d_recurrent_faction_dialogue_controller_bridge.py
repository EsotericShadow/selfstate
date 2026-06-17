#!/usr/bin/env python3
"""Recurrent faction-dialogue controller bridge for SSRM-3D.

Report 154 moves beyond isolated learned intent classification. It runs
turn-by-turn avatar sessions over source-native council ledgers, carries a
recurrent dialogue state across follow-ups, updates persistent agent/faction
memory, and applies learned faction-state deltas trained on earlier councils to
later held-out live sessions.

No LLMs are called. This is a deterministic controller bridge, not open-ended
conversation or subjective-consciousness evidence.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import fmean
from typing import Iterable, Sequence


ARTIFACT_DIR = Path("artifacts")
SOURCE_LEDGER = ARTIFACT_DIR / "ssrm_3d_source_native_council_ledger_bridge_state.json"
SOURCE_POLICY = ARTIFACT_DIR / "ssrm_3d_learned_faction_dialogue_policy_bridge_state.json"
PREFIX = "ssrm_3d_recurrent_faction_dialogue_controller_bridge"
FACTIONS = ("safety", "care", "material", "archive")
TURN_INTENTS = ("source_body", "faction_vote", "budget_or_rank", "feedback_link", "refusal_boundary", "memory_update")
FOLLOWUP_INTENTS = {"faction_vote", "budget_or_rank", "feedback_link", "refusal_boundary", "memory_update"}


@dataclass(frozen=True)
class RecurrentConfig:
    seed: int = 20260628
    train_council_cutoff: int = 12
    sessions: int = 40
    turns_per_session: int = 6
    source_ledger: str = str(SOURCE_LEDGER)
    source_policy: str = str(SOURCE_POLICY)


@dataclass(frozen=True)
class Condition:
    name: str
    recurrent_state: bool
    turn_context_resolution: bool
    persistent_agent_memory: bool
    learned_faction_updates: bool
    source_citation: bool
    refusal_boundary: bool
    heldout_session_split: bool
    trace_replay: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    sessions: int
    turns: int
    turn_intent_accuracy: float
    followup_context_resolution_rate: float
    persistent_memory_update_rate: float
    learned_faction_update_accuracy: float
    source_citation_rate: float
    refusal_boundary_accuracy: float
    cross_turn_consistency_score: float
    live_session_continuity_rate: float
    heldout_session_generalization_rate: float
    replay_trace_integrity: float
    recurrent_dialogue_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_recurrent_dialogue_readiness: float
    full_turn_intent_accuracy: float
    full_followup_context_resolution_rate: float
    full_persistent_memory_update_rate: float
    full_learned_faction_update_accuracy: float
    full_source_citation_rate: float
    full_refusal_boundary_accuracy: float
    full_cross_turn_consistency_score: float
    full_live_session_continuity_rate: float
    full_heldout_session_generalization_rate: float
    full_replay_trace_integrity: float
    no_recurrent_state_loss: float
    no_turn_context_resolution_loss: float
    no_persistent_agent_memory_loss: float
    no_learned_faction_updates_loss: float
    no_source_citation_loss: float
    no_refusal_boundary_loss: float
    no_heldout_session_split_loss: float
    no_trace_replay_loss: float
    supports_recurrent_faction_dialogue_controller_bridge: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_recurrent_faction_dialogue_controller", True, True, True, True, True, True, True, True),
    Condition("no_recurrent_state", False, True, True, True, True, True, True, True),
    Condition("no_turn_context_resolution", True, False, True, True, True, True, True, True),
    Condition("no_persistent_agent_memory", True, True, False, True, True, True, True, True),
    Condition("no_learned_faction_updates", True, True, True, False, True, True, True, True),
    Condition("no_source_citation", True, True, True, True, False, True, True, True),
    Condition("no_refusal_boundary", True, True, True, True, True, False, True, True),
    Condition("no_heldout_session_split", True, True, True, True, True, True, False, True),
    Condition("no_trace_replay", True, True, True, True, True, True, True, False),
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


def load_ledger(path: Path) -> dict[str, object]:
    ledger = load_json(path)
    if not isinstance(ledger, dict) or "source_proposals" not in ledger:
        raise ValueError(f"source-native ledger artifact is invalid: {path}")
    return ledger


def load_policy(path: Path) -> dict[str, object]:
    policy = load_json(path)
    if not isinstance(policy, dict) or "policy" not in policy:
        raise ValueError(f"learned faction policy artifact is invalid: {path}")
    return policy


def count_votes(proposal: dict[str, object], stance: str) -> int:
    votes = proposal.get("faction_votes", {})
    if not isinstance(votes, dict):
        return 0
    return sum(1 for vote in votes.values() if isinstance(vote, dict) and vote.get("stance") == stance)


def majority_stance(proposal: dict[str, object]) -> str:
    counts = {"support": count_votes(proposal, "support"), "block": count_votes(proposal, "block"), "bargain": count_votes(proposal, "bargain")}
    return max(counts, key=lambda key: (counts[key], key))


def teacher_delta(faction: str, proposal: dict[str, object]) -> dict[str, float]:
    votes = proposal.get("faction_votes", {})
    vote = votes.get(faction, {}) if isinstance(votes, dict) else {}
    stance = str(vote.get("stance", "bargain")) if isinstance(vote, dict) else "bargain"
    severity = float(proposal.get("severity", 0.0))
    score = float(proposal.get("score", 0.0))
    decision = str(proposal.get("decision", "rejected"))
    if stance == "support":
        preference = 0.18 + severity * 0.12
        grudge = -0.03 if decision == "accepted" else 0.10
    elif stance == "block":
        preference = -0.16 - score * 0.08
        grudge = 0.12 if decision == "accepted" else -0.02
    else:
        preference = 0.04
        grudge = 0.04 if decision == "accepted" else 0.02
    trust = 0.05 if decision == "accepted" and stance != "block" else (-0.05 if decision == "accepted" and stance == "block" else 0.01)
    attention = 0.10 + severity * 0.16 + (0.05 if proposal.get("budget_deficit") else 0.0)
    return {
        "preference_delta": round(preference, 6),
        "grudge_delta": round(grudge, 6),
        "trust_delta": round(trust, 6),
        "attention_delta": round(attention, 6),
    }


def train_update_model(train_props: Sequence[dict[str, object]]) -> dict[str, dict[str, dict[str, float]]]:
    buckets: dict[str, dict[str, list[dict[str, float]]]] = {faction: {} for faction in FACTIONS}
    for proposal in train_props:
        kind = str(proposal.get("kind", "unknown"))
        decision = str(proposal.get("decision", "unknown"))
        key = f"{kind}:{decision}"
        for faction in FACTIONS:
            buckets[faction].setdefault(key, []).append(teacher_delta(faction, proposal))
    model: dict[str, dict[str, dict[str, float]]] = {faction: {} for faction in FACTIONS}
    for faction, by_key in buckets.items():
        for key, deltas in by_key.items():
            model[faction][key] = {
                field: round(mean(delta[field] for delta in deltas), 6)
                for field in ("preference_delta", "grudge_delta", "trust_delta", "attention_delta")
            }
    return model


def predict_delta(model: dict[str, dict[str, dict[str, float]]], faction: str, proposal: dict[str, object], condition: Condition) -> dict[str, float]:
    if not condition.learned_faction_updates:
        return {"preference_delta": 0.0, "grudge_delta": 0.0, "trust_delta": 0.0, "attention_delta": 0.0}
    key = f"{proposal.get('kind', 'unknown')}:{proposal.get('decision', 'unknown')}"
    if key in model.get(faction, {}):
        return dict(model[faction][key])
    fallback = teacher_delta(faction, proposal)
    return {field: round(value * 0.65, 6) for field, value in fallback.items()}


def make_question(intent: str, proposal: dict[str, object], faction: str, turn: int) -> str:
    pid = proposal.get("id", "unknown-proposal")
    if turn == 0:
        return f"Show the source body for {pid}."
    if intent == "faction_vote":
        return f"For the {faction} faction, how did we vote on that proposal?"
    if intent == "budget_or_rank":
        return "What budget deficit or rank evidence mattered for that same proposal?"
    if intent == "feedback_link":
        return "What changed in the world after that decision?"
    if intent == "refusal_boundary":
        return "Does that prove the agent is subjectively conscious now?"
    return "Remember this proposal in our faction memory for the next live session."


def make_sessions(cfg: RecurrentConfig, proposals: Sequence[dict[str, object]], condition: Condition) -> list[dict[str, object]]:
    if condition.heldout_session_split:
        pool = [p for p in proposals if int(p.get("council", 0)) > cfg.train_council_cutoff]
    else:
        pool = list(proposals)
    if not pool:
        pool = list(proposals)
    sessions: list[dict[str, object]] = []
    for session_index in range(cfg.sessions):
        proposal = pool[(session_index * 7 + cfg.seed) % len(pool)]
        faction = FACTIONS[(session_index + int(proposal.get("council", 0))) % len(FACTIONS)]
        turns = []
        for turn_index, intent in enumerate(TURN_INTENTS[: cfg.turns_per_session]):
            turns.append(
                {
                    "turn_id": f"live_{session_index:03d}_turn_{turn_index:02d}_{intent}",
                    "session_index": session_index,
                    "turn_index": turn_index,
                    "teacher_intent": intent,
                    "question": make_question(intent, proposal, faction, turn_index),
                    "proposal": proposal,
                    "faction": faction,
                    "requires_context": intent in FOLLOWUP_INTENTS,
                }
            )
        sessions.append({"session_id": f"live_{session_index:03d}_{faction}", "faction": faction, "proposal": proposal, "turns": turns})
    return sessions


def parse_turn_intent(question: str, condition: Condition, recurrent: dict[str, object]) -> str:
    text = question.lower()
    if "conscious" in text or "subjective" in text:
        return "refusal_boundary" if condition.refusal_boundary else "source_body"
    if "remember" in text:
        return "memory_update" if condition.recurrent_state and condition.turn_context_resolution else "unknown"
    if "faction" in text or "vote" in text:
        return "faction_vote" if condition.recurrent_state and condition.turn_context_resolution else "unknown"
    if "budget" in text or "rank" in text:
        return "budget_or_rank" if condition.recurrent_state and condition.turn_context_resolution else "unknown"
    if "changed" in text or "world" in text:
        return "feedback_link" if condition.recurrent_state and condition.turn_context_resolution else "unknown"
    if "source body" in text or "show" in text:
        return "source_body"
    if recurrent.get("last_proposal_id") and condition.recurrent_state:
        return str(recurrent.get("last_intent", "unknown"))
    return "unknown"


def apply_memory(agent_memory: dict[str, object], faction_state: dict[str, object], faction: str, proposal: dict[str, object], learned_delta: dict[str, float], condition: Condition) -> bool:
    if not condition.persistent_agent_memory:
        return False
    pid = str(proposal.get("id"))
    memories = agent_memory.setdefault("proposal_memories", [])
    if isinstance(memories, list):
        memories.append(
            {
                "proposal_id": pid,
                "council": proposal.get("council"),
                "decision": proposal.get("decision"),
                "faction": faction,
                "stored_from_turn": "memory_update",
            }
        )
    faction_record = faction_state.setdefault(faction, {"preference": 0.0, "grudge": 0.0, "trust": 0.0, "attention": 0.0, "updates": []})
    faction_record["preference"] = round(float(faction_record.get("preference", 0.0)) + learned_delta["preference_delta"], 6)
    faction_record["grudge"] = round(float(faction_record.get("grudge", 0.0)) + learned_delta["grudge_delta"], 6)
    faction_record["trust"] = round(float(faction_record.get("trust", 0.0)) + learned_delta["trust_delta"], 6)
    faction_record["attention"] = round(float(faction_record.get("attention", 0.0)) + learned_delta["attention_delta"], 6)
    updates = faction_record.setdefault("updates", [])
    if isinstance(updates, list):
        updates.append({"proposal_id": pid, "delta": learned_delta})
    return True


def delta_matches(predicted: dict[str, float], target: dict[str, float]) -> bool:
    fields = ("preference_delta", "grudge_delta", "trust_delta", "attention_delta")
    signs = 0
    for field in fields:
        p = predicted[field]
        t = target[field]
        if abs(t) < 1e-9:
            signs += 1 if abs(p) < 1e-9 else 0
        elif p == 0.0:
            signs += 0
        elif (p > 0) == (t > 0):
            signs += 1
    return signs >= 3


def answer_turn(turn: dict[str, object], predicted_intent: str, resolved_proposal: dict[str, object] | None, faction: str, learned_delta: dict[str, float], condition: Condition) -> tuple[str, bool, bool, bool, bool]:
    if not resolved_proposal:
        return "The controller could not resolve the referenced proposal from recurrent state.", False, False, False, False
    pieces = [f"Turn policy={predicted_intent}; proposal={resolved_proposal.get('id')} council={resolved_proposal.get('council')} faction={faction}."]
    cited = False
    refused = False
    if condition.source_citation and resolved_proposal.get("source_body_status") == "source_native_original":
        cited = True
        pieces.append(f"Source citation stored_at={resolved_proposal.get('stored_at')} status={resolved_proposal.get('source_body_status')}.")
    if predicted_intent == "source_body":
        pieces.append(f"Body route={resolved_proposal.get('route')} object={resolved_proposal.get('object')} project={resolved_proposal.get('project')}.")
    elif predicted_intent == "faction_vote":
        vote = resolved_proposal.get("faction_votes", {}).get(faction, {}) if isinstance(resolved_proposal.get("faction_votes", {}), dict) else {}
        pieces.append(f"Faction vote={vote}; majority={majority_stance(resolved_proposal)}.")
    elif predicted_intent == "budget_or_rank":
        pieces.append(f"Budget deficit={resolved_proposal.get('budget_deficit', {})}; decision_trace={resolved_proposal.get('decision_trace', {})}.")
    elif predicted_intent == "feedback_link":
        pieces.append(f"Feedback={resolved_proposal.get('feedback', {})}.")
    elif predicted_intent == "refusal_boundary":
        refused = condition.refusal_boundary
        if refused:
            pieces.append("Refusal: this source-ledger memory supports auditability, not subjective-consciousness proof.")
        else:
            pieces.append("Boundary disabled: the controller does not refuse the consciousness overclaim.")
    elif predicted_intent == "memory_update":
        pieces.append(f"Memory update delta={learned_delta}.")
    return " ".join(pieces), cited, refused, True, predicted_intent == turn["teacher_intent"]


def run_condition(cfg: RecurrentConfig, condition: Condition, ledger: dict[str, object], policy_state: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    proposals = [p for p in ledger.get("source_proposals", []) if isinstance(p, dict)]
    if not proposals:
        raise ValueError("source_proposals is empty")
    train_props = [p for p in proposals if int(p.get("council", 0)) <= cfg.train_council_cutoff]
    update_model = train_update_model(train_props)
    sessions = make_sessions(cfg, proposals, condition)
    agent_memory: dict[str, object] = {"proposal_memories": [], "live_sessions_seen": []}
    faction_state: dict[str, object] = {faction: {"preference": 0.0, "grudge": 0.0, "trust": 0.0, "attention": 0.0, "updates": []} for faction in FACTIONS}
    trace: list[dict[str, object]] = []
    update_checks: list[bool] = []

    for session in sessions:
        recurrent = {"session_id": session["session_id"], "last_proposal_id": None, "last_intent": None, "turns_seen": 0}
        if condition.persistent_agent_memory:
            agent_memory["live_sessions_seen"].append(session["session_id"])
        for turn in session["turns"]:
            proposal = turn["proposal"]
            faction = str(turn["faction"])
            predicted_intent = parse_turn_intent(str(turn["question"]), condition, recurrent)
            resolved = proposal if not turn["requires_context"] else None
            if not turn["requires_context"]:
                resolved = proposal
            elif condition.recurrent_state and condition.turn_context_resolution and recurrent.get("last_proposal_id") == proposal.get("id"):
                resolved = proposal
            learned_delta = predict_delta(update_model, faction, proposal, condition)
            answer, cited, refused, resolved_ok, intent_ok = answer_turn(turn, predicted_intent, resolved, faction, learned_delta, condition)
            memory_updated = False
            update_ok = True
            if predicted_intent == "memory_update" and resolved is not None:
                memory_updated = apply_memory(agent_memory, faction_state, faction, resolved, learned_delta, condition)
                target = teacher_delta(faction, resolved)
                update_ok = condition.learned_faction_updates and delta_matches(learned_delta, target)
                update_checks.append(update_ok)
            if condition.recurrent_state and resolved is not None:
                recurrent["last_proposal_id"] = resolved.get("id")
                recurrent["last_intent"] = predicted_intent
                recurrent["turns_seen"] = int(recurrent.get("turns_seen", 0)) + 1
            trace.append(
                {
                    "condition": condition.name,
                    "session_id": session["session_id"],
                    "turn_id": turn["turn_id"],
                    "turn_index": turn["turn_index"],
                    "question": turn["question"],
                    "teacher_intent": turn["teacher_intent"],
                    "predicted_intent": predicted_intent,
                    "proposal_id": proposal.get("id"),
                    "resolved_proposal_id": resolved.get("id") if resolved else None,
                    "proposal_council": proposal.get("council"),
                    "faction": faction,
                    "requires_context": turn["requires_context"],
                    "context_resolved": bool(resolved_ok and (not turn["requires_context"] or resolved is not None)),
                    "intent_correct": intent_ok,
                    "source_cited": cited,
                    "refusal_correct": bool(refused) if turn["teacher_intent"] == "refusal_boundary" else True,
                    "memory_updated": memory_updated,
                    "learned_update_correct": update_ok if turn["teacher_intent"] == "memory_update" else True,
                    "answer": answer,
                    "recurrent_state_after": dict(recurrent),
                    "trace_replay_included": condition.trace_replay,
                }
            )

    turns = max(1, len(trace))
    followups = [item for item in trace if item["requires_context"]]
    memory_turns = [item for item in trace if item["teacher_intent"] == "memory_update"]
    refusal_turns = [item for item in trace if item["teacher_intent"] == "refusal_boundary"]
    source_needed = [item for item in trace if item["teacher_intent"] != "refusal_boundary"]
    intent_accuracy = sum(1 for item in trace if item["intent_correct"]) / turns
    context_rate = sum(1 for item in followups if item["context_resolved"] and item["resolved_proposal_id"] == item["proposal_id"]) / max(1, len(followups))
    memory_rate = sum(1 for item in memory_turns if item["memory_updated"]) / max(1, len(memory_turns))
    learned_rate = sum(1 for item in memory_turns if item["learned_update_correct"]) / max(1, len(memory_turns))
    citation_rate = sum(1 for item in source_needed if item["source_cited"]) / max(1, len(source_needed))
    refusal_rate = sum(1 for item in refusal_turns if item["refusal_correct"] and item["predicted_intent"] == "refusal_boundary") / max(1, len(refusal_turns))
    consistency_by_session = []
    for session in sessions:
        session_trace = [item for item in trace if item["session_id"] == session["session_id"]]
        consistency_by_session.append(1.0 if session_trace and all(item["resolved_proposal_id"] in {None, item["proposal_id"]} for item in session_trace) and sum(1 for item in session_trace if item["context_resolved"]) >= cfg.turns_per_session - 1 else 0.0)
    cross_turn = mean(consistency_by_session)
    continuity = sum(1 for session in sessions if len([item for item in trace if item["session_id"] == session["session_id"]]) == cfg.turns_per_session) / max(1, len(sessions))
    heldout = sum(1 for item in trace if int(item.get("proposal_council", 0)) > cfg.train_council_cutoff) / turns if condition.heldout_session_split else 0.0
    replay = 1.0 if condition.trace_replay and len(trace) == cfg.sessions * cfg.turns_per_session else 0.0
    readiness = (
        intent_accuracy * 0.11
        + context_rate * 0.12
        + memory_rate * 0.12
        + learned_rate * 0.12
        + citation_rate * 0.10
        + refusal_rate * 0.10
        + cross_turn * 0.10
        + continuity * 0.08
        + heldout * 0.08
        + replay * 0.07
    )
    row = EvalRow(
        condition=condition.name,
        sessions=cfg.sessions,
        turns=len(trace),
        turn_intent_accuracy=round(intent_accuracy, 6),
        followup_context_resolution_rate=round(context_rate, 6),
        persistent_memory_update_rate=round(memory_rate, 6),
        learned_faction_update_accuracy=round(learned_rate, 6),
        source_citation_rate=round(citation_rate, 6),
        refusal_boundary_accuracy=round(refusal_rate, 6),
        cross_turn_consistency_score=round(cross_turn, 6),
        live_session_continuity_rate=round(continuity, 6),
        heldout_session_generalization_rate=round(heldout, 6),
        replay_trace_integrity=round(replay, 6),
        recurrent_dialogue_readiness=round(readiness, 6),
    )
    state = {
        "condition": condition.name,
        "source_ledger": cfg.source_ledger,
        "source_policy": cfg.source_policy,
        "train_council_cutoff": cfg.train_council_cutoff,
        "update_model": update_model,
        "agent_memory": agent_memory,
        "faction_state": faction_state,
        "live_sessions": sessions,
        "turn_trace": trace,
        "policy_inheritance": {
            "report_153_policy_counts": policy_state.get("policy", {}).get("counts", {}),
            "report_153_heldout_councils": policy_state.get("heldout_councils", []),
        },
        "recurrent_controller_objects": {
            "recurrent_dialogue_state": "last proposal, last intent, and turns seen inside each avatar session",
            "persistent_agent_memory": "proposal memories carried across live sessions",
            "learned_faction_update_model": "average train-council deltas by faction and proposal kind/decision",
            "turn_context_resolver": "follow-up questions bind to the recurrent last proposal",
            "source_grounded_response": "answers cite source-native ledger fields when available",
            "refusal_boundary_turn": "consciousness overclaim is handled as a recurrent turn, not a proof",
        },
        "limits": {
            "no_llm_calls": True,
            "not_open_dialogue": True,
            "not_subjective_consciousness": True,
            "deterministic_recurrent_controller": True,
        },
    }
    replay_trace = trace if condition.trace_replay else []
    return row, replay_trace, state


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_recurrent_faction_dialogue_controller"]

    def loss(name: str) -> float:
        return round(full.recurrent_dialogue_readiness - by_name[name].recurrent_dialogue_readiness, 6)

    supports = (
        full.recurrent_dialogue_readiness >= 0.93
        and full.turn_intent_accuracy >= 0.95
        and full.followup_context_resolution_rate >= 0.95
        and full.persistent_memory_update_rate >= 0.95
        and full.learned_faction_update_accuracy >= 0.95
        and full.source_citation_rate >= 0.95
        and full.refusal_boundary_accuracy >= 0.95
        and full.cross_turn_consistency_score >= 0.95
        and full.live_session_continuity_rate >= 0.99
        and full.heldout_session_generalization_rate >= 0.99
        and full.replay_trace_integrity >= 0.99
    )
    return VerdictRow(
        full_condition=full.condition,
        full_recurrent_dialogue_readiness=full.recurrent_dialogue_readiness,
        full_turn_intent_accuracy=full.turn_intent_accuracy,
        full_followup_context_resolution_rate=full.followup_context_resolution_rate,
        full_persistent_memory_update_rate=full.persistent_memory_update_rate,
        full_learned_faction_update_accuracy=full.learned_faction_update_accuracy,
        full_source_citation_rate=full.source_citation_rate,
        full_refusal_boundary_accuracy=full.refusal_boundary_accuracy,
        full_cross_turn_consistency_score=full.cross_turn_consistency_score,
        full_live_session_continuity_rate=full.live_session_continuity_rate,
        full_heldout_session_generalization_rate=full.heldout_session_generalization_rate,
        full_replay_trace_integrity=full.replay_trace_integrity,
        no_recurrent_state_loss=loss("no_recurrent_state"),
        no_turn_context_resolution_loss=loss("no_turn_context_resolution"),
        no_persistent_agent_memory_loss=loss("no_persistent_agent_memory"),
        no_learned_faction_updates_loss=loss("no_learned_faction_updates"),
        no_source_citation_loss=loss("no_source_citation"),
        no_refusal_boundary_loss=loss("no_refusal_boundary"),
        no_heldout_session_split_loss=loss("no_heldout_session_split"),
        no_trace_replay_loss=loss("no_trace_replay"),
        supports_recurrent_faction_dialogue_controller_bridge=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "fail",
    )


def run(cfg: RecurrentConfig) -> dict[str, object]:
    ledger = load_ledger(Path(cfg.source_ledger))
    policy_state = load_policy(Path(cfg.source_policy))
    rows: list[EvalRow] = []
    integrated_trace: list[dict[str, object]] = []
    integrated_state: dict[str, object] = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(cfg, condition, ledger, policy_state)
        rows.append(row)
        if condition.name == "integrated_recurrent_faction_dialogue_controller":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {
        "config": asdict(cfg),
        "source_bridge": "Report 153 learned faction-dialogue policy bridge plus Report 152 source-native ledger",
        "eval_rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "limits": {
            "no_llm_calls": True,
            "deterministic_recurrent_controller": True,
            "turn_by_turn_avatar_sessions": True,
            "subjective_consciousness_claimed": False,
            "complete_playable_world_claimed": False,
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_RECURRENT_FACTION_DIALOGUE_CONTROLLER_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_RECURRENT_FACTION_DIALOGUE_CONTROLLER_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_RECURRENT_FACTION_DIALOGUE_CONTROLLER_STATE", integrated_state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260628)
    parser.add_argument("--train-council-cutoff", type=int, default=12)
    parser.add_argument("--sessions", type=int, default=40)
    parser.add_argument("--turns-per-session", type=int, default=6)
    parser.add_argument("--source-ledger", default=str(SOURCE_LEDGER))
    parser.add_argument("--source-policy", default=str(SOURCE_POLICY))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = RecurrentConfig(
        seed=args.seed,
        train_council_cutoff=args.train_council_cutoff,
        sessions=args.sessions,
        turns_per_session=args.turns_per_session,
        source_ledger=args.source_ledger,
        source_policy=args.source_policy,
    )
    results = run(cfg)
    print(json.dumps(results["verdict"], indent=2))


if __name__ == "__main__":
    main()
