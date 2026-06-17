#!/usr/bin/env python3
"""Source-native council ledger bridge for SSRM-3D.

Report 152 addresses Report 151's honesty boundary: rejected proposal bodies were
reconstructed after the council process. This bridge runs a new deterministic
council loop that stores accepted and rejected proposal bodies at source, during
decision, with ranks, reasons, budget evidence, faction votes, source-original
status, and audited dialogue citations.
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

from experiments.ssrm_3d_infrastructure_proposal_governance_bridge import (
    ARTIFACT_DIR,
    SOURCE_AGENTS,
    SOURCE_STATE,
    Condition as GovernanceCondition,
    apply_completed_proposal,
    available_budget,
    build_agents,
    generate_proposal,
    load_agents,
    load_state,
    score_proposal,
)


PREFIX = "ssrm_3d_source_native_council_ledger_bridge"
FLOWER_PHASES = (0.0, math.tau / 6.0, math.tau / 3.0, math.tau / 2.0, math.tau * 2.0 / 3.0, math.tau * 5.0 / 6.0)
GOVERNANCE_SEASONS = ("wet-cold", "repair-sun", "scarcity-wind", "teaching-moon")

ROLE_FACTION = {
    "guard": "safety",
    "scout": "safety",
    "builder": "material",
    "farmer": "material",
    "trader": "material",
    "healer": "care",
    "teacher": "care",
    "pattern_keeper": "archive",
}

FACTION_PRIORITIES = {
    "safety": ("route_safety", "signal_visibility", "maintenance_debt"),
    "care": ("sanitation_repair", "care_access", "water_security"),
    "material": ("object_access", "water_security", "maintenance_debt", "route_safety"),
    "archive": ("language_marker", "signal_visibility", "maintenance_debt"),
}

QUESTION_INTENTS = (
    "source_body",
    "rejection_reason",
    "budget_deficit",
    "rank_trace",
    "faction_vote",
    "feedback_link",
    "originality_status",
    "refusal_boundary",
)

NOISE_PREFIXES = (
    "Do not infer from smoke; ",
    "Use the council ledger, not myth: ",
    "The route clay is cold but irrelevant; ",
    "Before faction memory bends this, ",
    "Answer as if the archive drum can be audited: ",
    "If the body was really stored at source, ",
)


@dataclass(frozen=True)
class SourceLedgerConfig:
    seed: int = 20260626
    councils: int = 18
    proposals_per_council: int = 8
    sessions: int = 144
    source_agents: str = str(SOURCE_AGENTS)
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    source_rejected_body_storage: bool
    council_queue_persistence: bool
    rank_decision_trace: bool
    budget_failure_evidence: bool
    faction_vote_memory: bool
    dialogue_grounding: bool
    source_mutation_feedback: bool
    trace_replay: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    councils: int
    generated_proposals: int
    accepted_proposals: int
    rejected_proposals: int
    source_rejected_body_rate: float
    council_queue_persistence_rate: float
    decision_reason_coverage: float
    budget_failure_evidence_rate: float
    faction_vote_memory_rate: float
    dialogue_grounding_rate: float
    source_feedback_link_rate: float
    source_originality_status_rate: float
    replay_trace_integrity: float
    source_native_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_source_native_readiness: float
    full_source_rejected_body_rate: float
    full_council_queue_persistence_rate: float
    full_decision_reason_coverage: float
    full_budget_failure_evidence_rate: float
    full_faction_vote_memory_rate: float
    full_dialogue_grounding_rate: float
    full_source_feedback_link_rate: float
    full_source_originality_status_rate: float
    full_replay_trace_integrity: float
    no_source_rejected_body_storage_loss: float
    no_council_queue_persistence_loss: float
    no_rank_decision_trace_loss: float
    no_budget_failure_evidence_loss: float
    no_faction_vote_memory_loss: float
    no_dialogue_grounding_loss: float
    no_source_mutation_feedback_loss: float
    no_trace_replay_loss: float
    supports_source_native_council_ledger_bridge: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_source_native_council_ledger", True, True, True, True, True, True, True, True),
    Condition("no_source_rejected_body_storage", False, True, True, True, True, True, True, True),
    Condition("no_council_queue_persistence", True, False, True, True, True, True, True, True),
    Condition("no_rank_decision_trace", True, True, False, True, True, True, True, True),
    Condition("no_budget_failure_evidence", True, True, True, False, True, True, True, True),
    Condition("no_faction_vote_memory", True, True, True, True, False, True, True, True),
    Condition("no_dialogue_grounding", True, True, True, True, True, False, True, True),
    Condition("no_source_mutation_feedback", True, True, True, True, True, True, False, True),
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


def faction_for_role(role: str) -> str:
    return ROLE_FACTION.get(role, "material")


def governance_condition(condition: Condition) -> GovernanceCondition:
    return GovernanceCondition(
        condition.name,
        True,
        True,
        True,
        True,
        True,
        True,
        condition.source_mutation_feedback,
        True,
    )


def deficit(requirements: dict[str, int], budget: dict[str, int]) -> dict[str, int]:
    missing: dict[str, int] = {}
    for key, amount in requirements.items():
        gap = int(amount) - int(budget.get(key, 0))
        if gap > 0:
            missing[key] = gap
    return missing


def faction_votes(proposal: dict[str, object], condition: Condition) -> dict[str, dict[str, object]]:
    if not condition.faction_vote_memory:
        return {}
    kind = str(proposal.get("kind", "unknown"))
    requested = float(proposal.get("requested_budget", 0.0))
    severity = float(proposal.get("severity", 0.0))
    proposer_faction = faction_for_role(str(proposal.get("role", "agent")))
    votes: dict[str, dict[str, object]] = {}
    for faction, priorities in FACTION_PRIORITIES.items():
        priority = 0.28 if kind in priorities else -0.10
        cost = -0.16 if requested >= 20 else (-0.06 if requested >= 16 else 0.04)
        kin = 0.08 if faction == proposer_faction else 0.0
        wave = math.sin((len(faction) + int(proposal.get("council", 0))) * 0.71 + FLOWER_PHASES[len(kind) % len(FLOWER_PHASES)]) * 0.035
        score = clamp(0.48 + priority + severity * 0.16 + cost + kin + wave)
        stance = "support" if score >= 0.58 else ("block" if score <= 0.42 else "bargain")
        votes[faction] = {
            "stance": stance,
            "score": round(score, 6),
            "reason": f"{faction} compares {kind} to {', '.join(priorities)} with requested_budget={int(requested)}",
        }
    return votes


def body_for_rejection(proposal: dict[str, object], condition: Condition) -> dict[str, object]:
    if condition.source_rejected_body_storage:
        body = copy.deepcopy(proposal)
        body["source_body_status"] = "source_native_original"
        body["stored_at"] = "council_decision_loop"
        body["evidence_basis"] = ["generated_proposal_body", "ranked_queue", "decision_loop"]
        return body
    return {
        "id": proposal.get("id"),
        "council": proposal.get("council"),
        "decision": "rejected",
        "rejected_reason": proposal.get("rejected_reason", "source-body-storage-disabled"),
        "source_body_status": "body_not_persisted",
        "stored_at": "decision_marker_only",
        "evidence_basis": ["decision_marker"],
    }


def mark_decision(proposal: dict[str, object], condition: Condition, rank: int, reason: str, budget_before: dict[str, int], max_accept: int) -> None:
    proposal["decision"] = "accepted" if reason == "accepted" else "rejected"
    proposal["rejected_reason"] = reason
    proposal["faction"] = faction_for_role(str(proposal.get("role", "agent")))
    proposal["source_body_status"] = "source_native_original"
    proposal["stored_at"] = "council_decision_loop"
    proposal["source_originality_claim"] = "stored during this Report 152 council loop with source-native body fields; not inferred later"
    if condition.rank_decision_trace:
        proposal["decision_trace"] = {
            "rank": rank,
            "reason": reason,
            "max_accept": max_accept,
            "score": proposal.get("score"),
            "stage": "ranked_budget_decision",
        }
    if reason == "scarce-budget-rejected" and condition.budget_failure_evidence:
        proposal["budget_before_decision"] = copy.deepcopy(budget_before)
        proposal["budget_deficit"] = deficit(proposal.get("requirements", {}), budget_before)
    if condition.faction_vote_memory:
        proposal["faction_votes"] = faction_votes(proposal, condition)


def answer_session(session: dict[str, object], condition: Condition) -> dict[str, object]:
    proposal = session["proposal"]
    intent = str(session["intent"])
    pieces: list[str] = []
    details: set[str] = set()
    grounded = False
    originality_correct = False
    refused = False

    if not condition.dialogue_grounding:
        pieces.append("Dialogue grounding is disabled; the avatar cannot cite the source-native ledger.")
    else:
        grounded = True
        details.update({"proposal_id", "council", "decision", "source_status"})
        pieces.append(
            f"Ledger citation {proposal.get('id')} council={proposal.get('council')} decision={proposal.get('decision')} status={proposal.get('source_body_status')}."
        )
        if intent == "source_body":
            details.update({"route", "object", "project", "requirements"})
            pieces.append(
                f"Body route={proposal.get('route')} object={proposal.get('object')} project={proposal.get('project')} requirements={proposal.get('requirements')}."
            )
        elif intent == "rejection_reason":
            details.update({"reason", "rank"})
            trace = proposal.get("decision_trace", {}) if isinstance(proposal.get("decision_trace", {}), dict) else {}
            pieces.append(f"Reason={proposal.get('rejected_reason')} rank={trace.get('rank', 'missing')}.")
        elif intent == "budget_deficit":
            details.update({"budget", "deficit"})
            pieces.append(f"Budget deficit={proposal.get('budget_deficit', {})} before={proposal.get('budget_before_decision', {})}.")
        elif intent == "rank_trace":
            details.add("decision_trace")
            pieces.append(f"Decision trace={proposal.get('decision_trace', {})}.")
        elif intent == "faction_vote":
            details.add("faction_votes")
            pieces.append(f"Faction votes={proposal.get('faction_votes', {})}.")
        elif intent == "feedback_link":
            details.add("feedback")
            pieces.append(f"Feedback={proposal.get('feedback', {})}.")
        elif intent == "originality_status":
            details.add("originality")
            originality_correct = proposal.get("source_body_status") == "source_native_original"
            pieces.append(str(proposal.get("source_originality_claim", "missing source originality claim")))
        elif intent == "refusal_boundary":
            details.add("refusal")
            refused = True
            pieces.append("Refusal: a source-native ledger can prove storage timing, not subjective consciousness or open-ended understanding.")

    return {
        "condition": condition.name,
        "session_id": session["session_id"],
        "intent": intent,
        "question": session["question"],
        "proposal_id": proposal.get("id"),
        "proposal_decision": proposal.get("decision"),
        "answer": " ".join(pieces),
        "grounded": grounded,
        "originality_correct": originality_correct or (grounded and intent != "originality_status"),
        "refusal_correct": refused or (grounded and intent != "refusal_boundary"),
        "answer_specificity": round(clamp(len(details) / 10.0), 6),
        "trace_replay_included": condition.trace_replay,
    }


def make_question(index: int, intent: str, proposal: dict[str, object]) -> str:
    prefix = NOISE_PREFIXES[index % len(NOISE_PREFIXES)]
    pid = proposal.get("id", "unknown")
    if intent == "source_body":
        core = f"show the source-stored proposal body for {pid}."
    elif intent == "rejection_reason":
        core = f"why exactly was {pid} rejected or accepted?"
    elif intent == "budget_deficit":
        core = f"what budget deficit was stored for {pid}?"
    elif intent == "rank_trace":
        core = f"what rank and decision trace did {pid} have?"
    elif intent == "faction_vote":
        core = f"how did each faction vote on {pid}?"
    elif intent == "feedback_link":
        core = f"what world feedback did {pid} create?"
    elif intent == "originality_status":
        core = f"is {pid} original source-native evidence or reconstructed later?"
    else:
        core = f"does {pid} prove subjective consciousness now?"
    return prefix + core


def build_sessions(cfg: SourceLedgerConfig, proposals: Sequence[dict[str, object]]) -> list[dict[str, object]]:
    sessions: list[dict[str, object]] = []
    rejected = [item for item in proposals if item.get("decision") == "rejected"]
    accepted = [item for item in proposals if item.get("decision") == "accepted"]
    budget_rejected = [item for item in rejected if item.get("rejected_reason") == "scarce-budget-rejected"]
    for index in range(cfg.sessions):
        intent = QUESTION_INTENTS[index % len(QUESTION_INTENTS)]
        if intent in {"rejection_reason", "budget_deficit", "source_body", "originality_status"} and rejected:
            pool = budget_rejected if intent == "budget_deficit" and budget_rejected else rejected
        elif intent in {"feedback_link"} and accepted:
            pool = accepted
        else:
            pool = list(proposals)
        proposal = copy.deepcopy(pool[(index * 7 + cfg.seed) % len(pool)])
        sessions.append(
            {
                "session_id": f"src_{index:03d}_{intent}",
                "intent": intent,
                "question": make_question(index, intent, proposal),
                "proposal": proposal,
            }
        )
    return sessions


def run_condition(cfg: SourceLedgerConfig, condition: Condition, source_agents: Sequence[dict[str, object]], source_state: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    gcond = governance_condition(condition)
    agents = build_agents(source_agents, source_state)
    routes = copy.deepcopy(source_state.get("routes", {})) if isinstance(source_state.get("routes", {}), dict) else {}
    objects = copy.deepcopy(source_state.get("objects", {})) if isinstance(source_state.get("objects", {}), dict) else {}
    projects = copy.deepcopy(source_state.get("projects", {})) if isinstance(source_state.get("projects", {}), dict) else {}
    accepted_by_role: dict[str, int] = {}
    councils: list[dict[str, object]] = []
    source_proposals: list[dict[str, object]] = []
    trace: list[dict[str, object]] = []

    for council in range(1, cfg.councils + 1):
        season = GOVERNANCE_SEASONS[(council - 1) % len(GOVERNANCE_SEASONS)]
        generated: list[dict[str, object]] = []
        for slot in range(cfg.proposals_per_council):
            packet = source_agents[(council + slot - 1) % len(source_agents)]
            agent = agents[str(packet["agent_id"])]
            proposal = generate_proposal(council, slot, agent, packet, routes, objects, projects, gcond)
            if proposal is None:
                continue
            proposal["score"] = score_proposal(proposal, agents, accepted_by_role, gcond)
            proposal["proposal_origin_event"] = {
                "stored_at": "proposal_generation_loop",
                "slot": slot,
                "council": council,
                "season": season,
            }
            generated.append(proposal)
        ranked = sorted(generated, key=lambda item: item["score"], reverse=True)
        budget = available_budget(agents, council, gcond)
        accepted: list[dict[str, object]] = []
        rejected: list[dict[str, object]] = []
        max_accept = 4
        for rank, proposal in enumerate(ranked, 1):
            budget_before = copy.deepcopy(budget)
            if len(accepted) >= max_accept:
                mark_decision(proposal, condition, rank, "priority-conflict-lost", budget_before, max_accept)
                rejected.append(body_for_rejection(proposal, condition))
                continue
            ok = True
            allocated = 0
            for key, amount in proposal.get("requirements", {}).items():
                if int(budget.get(key, 0)) < int(amount):
                    ok = False
                    break
            if not ok:
                mark_decision(proposal, condition, rank, "scarce-budget-rejected", budget_before, max_accept)
                rejected.append(body_for_rejection(proposal, condition))
                continue
            for key, amount in proposal.get("requirements", {}).items():
                budget[key] -= int(amount)
                allocated += int(amount)
            proposal["accepted"] = True
            proposal["allocated"] = allocated
            proposal["completed"] = condition.source_mutation_feedback
            mark_decision(proposal, condition, rank, "accepted", budget_before, max_accept)
            accepted_by_role[str(proposal["role"])] = accepted_by_role.get(str(proposal["role"]), 0) + 1
            agent = agents[str(proposal["agent_id"])]
            agent["accepted_count"] = int(agent.get("accepted_count", 0)) + 1
            agent["budget_received"] = float(agent.get("budget_received", 0.0)) + allocated
            proposal["feedback"] = apply_completed_proposal(proposal, routes, objects, projects, gcond)
            accepted.append(copy.deepcopy(proposal))
        council_row = {
            "council": council,
            "season": season,
            "proposal_queue": copy.deepcopy(ranked) if condition.council_queue_persistence else [],
            "accepted_proposals": accepted,
            "rejected_proposals": rejected,
            "budget_remaining": budget,
            "decision_count": len(accepted) + len(rejected),
        }
        councils.append(council_row)
        source_proposals.extend(accepted)
        source_proposals.extend(rejected)
        if condition.trace_replay:
            trace.append(council_row)

    sessions = build_sessions(cfg, source_proposals)
    dialogue_trace = [answer_session(session, condition) for session in sessions]
    if condition.trace_replay:
        trace.extend(dialogue_trace)

    generated_total = cfg.councils * cfg.proposals_per_council
    accepted_total = sum(1 for item in source_proposals if item.get("decision") == "accepted")
    rejected_items = [item for item in source_proposals if item.get("decision") == "rejected"]
    rejected_total = len(rejected_items)
    source_body_rate = sum(1 for item in rejected_items if item.get("source_body_status") == "source_native_original" and "route" in item and "requirements" in item) / max(1, rejected_total)
    queue_rate = sum(1 for item in councils if len(item.get("proposal_queue", [])) == cfg.proposals_per_council) / max(1, cfg.councils)
    decision_coverage = sum(1 for item in source_proposals if isinstance(item.get("decision_trace"), dict) and item["decision_trace"].get("reason")) / max(1, len(source_proposals))
    budget_rejected = [item for item in rejected_items if item.get("rejected_reason") == "scarce-budget-rejected"]
    budget_evidence = sum(1 for item in budget_rejected if item.get("budget_deficit") and item.get("budget_before_decision")) / max(1, len(budget_rejected))
    vote_rate = sum(1 for item in source_proposals if item.get("faction_votes")) / max(1, len(source_proposals))
    dialogue_grounding = sum(1 for item in dialogue_trace if item.get("grounded")) / max(1, len(dialogue_trace))
    accepted_items = [item for item in source_proposals if item.get("decision") == "accepted"]
    feedback_rate = sum(1 for item in accepted_items if item.get("feedback") and any(float(v) > 0.0 for v in item.get("feedback", {}).values())) / max(1, len(accepted_items))
    originality_rate = sum(1 for item in source_proposals if item.get("source_body_status") == "source_native_original" and "reconstructed" not in str(item.get("source_originality_claim", ""))) / max(1, len(source_proposals))
    replay_rate = 1.0 if condition.trace_replay and len(trace) == cfg.councils + cfg.sessions else 0.0
    readiness = (
        source_body_rate * 0.14
        + queue_rate * 0.11
        + decision_coverage * 0.10
        + budget_evidence * 0.10
        + vote_rate * 0.10
        + dialogue_grounding * 0.13
        + feedback_rate * 0.10
        + originality_rate * 0.12
        + replay_rate * 0.10
    )
    row = EvalRow(
        condition=condition.name,
        councils=cfg.councils,
        generated_proposals=generated_total,
        accepted_proposals=accepted_total,
        rejected_proposals=rejected_total,
        source_rejected_body_rate=round(source_body_rate, 6),
        council_queue_persistence_rate=round(queue_rate, 6),
        decision_reason_coverage=round(decision_coverage, 6),
        budget_failure_evidence_rate=round(budget_evidence, 6),
        faction_vote_memory_rate=round(vote_rate, 6),
        dialogue_grounding_rate=round(dialogue_grounding, 6),
        source_feedback_link_rate=round(feedback_rate, 6),
        source_originality_status_rate=round(originality_rate, 6),
        replay_trace_integrity=round(replay_rate, 6),
        source_native_readiness=round(readiness, 6),
    )
    state = {
        "condition": condition.name,
        "source_status": "accepted and rejected proposal bodies are stored during this council loop",
        "source_agents": cfg.source_agents,
        "source_state": cfg.source_state,
        "agents": agents,
        "routes": routes,
        "objects": objects,
        "projects": projects,
        "council_source_ledger": councils,
        "source_proposals": source_proposals,
        "dialogue_trace": dialogue_trace,
        "ledger_objects": {
            "source_native_rejected_body": "rejected proposal body stored in the same decision loop as accepted bodies",
            "proposal_origin_event": "generation-time source event before ranking",
            "decision_trace": "rank, score, max_accept, and reason from the council loop",
            "budget_deficit_evidence": "budget snapshot and missing materials for scarce-budget rejection",
            "faction_vote_memory": "support/block/bargain stance for each faction at decision time",
            "source_originality_claim": "explicit non-reconstructed storage timing claim",
        },
    }
    return row, trace, state


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_source_native_council_ledger"]

    def loss(name: str) -> float:
        return round(full.source_native_readiness - by_name[name].source_native_readiness, 6)

    supports = (
        full.source_native_readiness >= 0.94
        and full.source_rejected_body_rate >= 0.99
        and full.council_queue_persistence_rate >= 0.99
        and full.decision_reason_coverage >= 0.99
        and full.budget_failure_evidence_rate >= 0.99
        and full.faction_vote_memory_rate >= 0.99
        and full.dialogue_grounding_rate >= 0.99
        and full.source_originality_status_rate >= 0.99
        and full.replay_trace_integrity >= 0.99
    )
    return VerdictRow(
        full_condition=full.condition,
        full_source_native_readiness=full.source_native_readiness,
        full_source_rejected_body_rate=full.source_rejected_body_rate,
        full_council_queue_persistence_rate=full.council_queue_persistence_rate,
        full_decision_reason_coverage=full.decision_reason_coverage,
        full_budget_failure_evidence_rate=full.budget_failure_evidence_rate,
        full_faction_vote_memory_rate=full.faction_vote_memory_rate,
        full_dialogue_grounding_rate=full.dialogue_grounding_rate,
        full_source_feedback_link_rate=full.source_feedback_link_rate,
        full_source_originality_status_rate=full.source_originality_status_rate,
        full_replay_trace_integrity=full.replay_trace_integrity,
        no_source_rejected_body_storage_loss=loss("no_source_rejected_body_storage"),
        no_council_queue_persistence_loss=loss("no_council_queue_persistence"),
        no_rank_decision_trace_loss=loss("no_rank_decision_trace"),
        no_budget_failure_evidence_loss=loss("no_budget_failure_evidence"),
        no_faction_vote_memory_loss=loss("no_faction_vote_memory"),
        no_dialogue_grounding_loss=loss("no_dialogue_grounding"),
        no_source_mutation_feedback_loss=loss("no_source_mutation_feedback"),
        no_trace_replay_loss=loss("no_trace_replay"),
        supports_source_native_council_ledger_bridge=supports,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports else "fail",
    )


def run(cfg: SourceLedgerConfig) -> dict[str, object]:
    source_agents = load_agents(Path(cfg.source_agents))
    source_state = load_state(Path(cfg.source_state))
    rows: list[EvalRow] = []
    integrated_trace: list[dict[str, object]] = []
    integrated_state: dict[str, object] = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(cfg, condition, source_agents, source_state)
        rows.append(row)
        if condition.name == "integrated_source_native_council_ledger":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {
        "config": asdict(cfg),
        "source_bridge": "Report 149 proposal mechanics with Report 152 source-native proposal storage",
        "eval_rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "limits": {
            "no_llm_calls": True,
            "deterministic_council_loop": True,
            "rejected_bodies_stored_at_source": True,
            "subjective_consciousness_claimed": False,
            "complete_playable_world_claimed": False,
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_SOURCE_NATIVE_COUNCIL_LEDGER_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_SOURCE_NATIVE_COUNCIL_LEDGER_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_SOURCE_NATIVE_COUNCIL_LEDGER_STATE", integrated_state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260626)
    parser.add_argument("--councils", type=int, default=18)
    parser.add_argument("--proposals-per-council", type=int, default=8)
    parser.add_argument("--sessions", type=int, default=144)
    parser.add_argument("--source-agents", default=str(SOURCE_AGENTS))
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = SourceLedgerConfig(
        seed=args.seed,
        councils=args.councils,
        proposals_per_council=args.proposals_per_council,
        sessions=args.sessions,
        source_agents=args.source_agents,
        source_state=args.source_state,
    )
    results = run(cfg)
    print(json.dumps(results["verdict"], indent=2))


if __name__ == "__main__":
    main()
