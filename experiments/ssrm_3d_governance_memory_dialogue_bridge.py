#!/usr/bin/env python3
"""Governance-memory dialogue bridge for SSRM-3D agents.

Report 150 makes the Report 149 governance history queryable by a local
avatar-style question parser. It is deterministic and scripted: no LLMs are
called, no open dialogue is claimed, and missing evidence is surfaced as a
rejection shadow rather than filled in.
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
SOURCE_AGENTS = ARTIFACT_DIR / "ssrm_3d_deep_time_playable_bridge_avatar_agents.json"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_infrastructure_proposal_governance_bridge_state.json"
PREFIX = "ssrm_3d_governance_memory_dialogue_bridge"

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
    "safety": {"route_safety", "signal_visibility", "maintenance_debt"},
    "care": {"sanitation_repair", "care_access", "water_security"},
    "material": {"object_access", "water_security", "maintenance_debt", "route_safety"},
    "archive": {"language_marker", "signal_visibility", "maintenance_debt"},
}

BENEFIT_BY_KIND = {
    "maintenance_debt": ("builders", "travelers", "future repair crews"),
    "route_safety": ("scouts", "guards", "traders"),
    "object_access": ("farmers", "traders", "builders"),
    "sanitation_repair": ("healers", "children", "food handlers"),
    "signal_visibility": ("guards", "pattern keepers", "late travelers"),
    "water_security": ("farmers", "healers", "kitchens"),
    "care_access": ("healers", "teachers", "injured workers"),
    "language_marker": ("teachers", "pattern keepers", "new learners"),
}

QUESTION_INTENTS = ("acceptance", "benefit", "maintenance", "token", "disagreement", "change", "rejection")
NOISE_PREFIXES = (
    "Ignore the cold smell near the path for a moment: ",
    "The drum mark was late, but answer from memory: ",
    "A child mentioned wet clay and I may be mixing stories: ",
    "Before anyone turns this into a myth: ",
    "The firelight made the marker look wrong, still: ",
    "If the route dust is irrelevant, tell me plainly: ",
)


@dataclass(frozen=True)
class DialogueConfig:
    seed: int = 20260624
    sessions: int = 96
    source_agents: str = str(SOURCE_AGENTS)
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    question_parser: bool
    governance_memory: bool
    evidence_trace_binding: bool
    native_token_grounding: bool
    role_perspective: bool
    disagreement_model: bool
    state_update_from_dialogue: bool
    trace_replay: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    sessions: int
    question_parse_rate: float
    governance_memory_retrieval_rate: float
    evidence_trace_binding_rate: float
    native_token_grounding_rate: float
    role_perspective_consistency: float
    disagreement_expression_rate: float
    state_update_from_dialogue_rate: float
    answer_specificity_score: float
    faction_diversity_score: float
    trace_completeness: float
    dialogue_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_dialogue_readiness: float
    full_question_parse_rate: float
    full_governance_memory_retrieval_rate: float
    full_evidence_trace_binding_rate: float
    full_native_token_grounding_rate: float
    full_role_perspective_consistency: float
    full_disagreement_expression_rate: float
    full_state_update_from_dialogue_rate: float
    full_answer_specificity_score: float
    full_faction_diversity_score: float
    full_trace_completeness: float
    no_avatar_question_parser_loss: float
    no_governance_memory_loss: float
    no_evidence_trace_binding_loss: float
    no_native_token_grounding_loss: float
    no_role_perspective_loss: float
    no_disagreement_model_loss: float
    no_state_update_from_dialogue_loss: float
    no_trace_replay_loss: float
    supports_governance_memory_dialogue_bridge: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_governance_memory_dialogue", True, True, True, True, True, True, True, True),
    Condition("no_avatar_question_parser", False, True, True, True, True, True, True, True),
    Condition("no_governance_memory", True, False, True, True, True, True, True, True),
    Condition("no_evidence_trace_binding", True, True, False, True, True, True, True, True),
    Condition("no_native_token_grounding", True, True, True, False, True, True, True, True),
    Condition("no_role_perspective", True, True, True, True, False, True, True, True),
    Condition("no_disagreement_model", True, True, True, True, True, False, True, True),
    Condition("no_state_update_from_dialogue", True, True, True, True, True, True, False, True),
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


def load_agents(path: Path) -> list[dict[str, object]]:
    agents = load_json(path)
    if not isinstance(agents, list) or not agents:
        raise ValueError(f"agent packet artifact is empty or invalid: {path}")
    return agents


def load_state(path: Path) -> dict[str, object]:
    state = load_json(path)
    if not isinstance(state, dict) or "governance_history" not in state or "agents" not in state:
        raise ValueError(f"Report 149 governance state artifact is invalid: {path}")
    return state


def faction_for_role(role: str) -> str:
    return ROLE_FACTION.get(role, "material")


def build_agent_profiles(source_agents: Sequence[dict[str, object]], source_state: dict[str, object]) -> list[dict[str, object]]:
    prior = source_state.get("agents", {})
    if not isinstance(prior, dict):
        prior = {}
    profiles: list[dict[str, object]] = []
    for packet in source_agents:
        agent_id = str(packet.get("agent_id", "agent"))
        live = prior.get(agent_id, {})
        if not isinstance(live, dict):
            live = {}
        role = str(live.get("role", packet.get("role", "agent")))
        profile = {
            "agent_id": agent_id,
            "name": str(live.get("name", packet.get("name", agent_id))),
            "role": role,
            "faction": faction_for_role(role),
            "trust": float(live.get("trust", packet.get("trust", 0.64))),
            "native_tokens": copy.deepcopy(packet.get("native_tokens", [])),
            "translation_hints": copy.deepcopy(packet.get("translation_hints", {})),
            "governance_dialogue_memory": [],
            "questioned_count": 0,
            "disagreement_count": 0,
        }
        profiles.append(profile)
    return profiles


def flatten_accepted(history: Sequence[dict[str, object]]) -> list[dict[str, object]]:
    events: list[dict[str, object]] = []
    for council in history:
        accepted = council.get("accepted_proposals", [])
        if not isinstance(accepted, list):
            continue
        for proposal in accepted:
            if not isinstance(proposal, dict):
                continue
            event = copy.deepcopy(proposal)
            event["season"] = council.get("season", "unknown-season")
            event["council_rejected_count"] = council.get("rejected_count", 0)
            event["council_budget_remaining"] = copy.deepcopy(council.get("budget_remaining", {}))
            events.append(event)
    if not events:
        raise ValueError("Report 149 governance history has no accepted proposals to query")
    return events


def rejection_shadow(council: dict[str, object]) -> dict[str, object]:
    budget = council.get("budget_remaining", {})
    if not isinstance(budget, dict):
        budget = {}
    tight = sorted(str(key) for key, value in budget.items() if isinstance(value, (int, float)) and float(value) <= 3.0)
    reason = "scarce-material-overreach" if tight else "priority-conflict-or-missing-body"
    return {
        "id": f"c{int(council.get('council', 0)):02d}_rejected_overreach_shadow",
        "council": int(council.get("council", 0)),
        "season": str(council.get("season", "unknown-season")),
        "rejected_count": int(council.get("rejected_count", 0)),
        "budget_tight_materials": tight[:4],
        "reason": reason,
        "evidence_limitation": "Report 149 persisted rejected counts, not full rejected proposal bodies.",
    }


def aligns_with_faction(agent: dict[str, object], proposal: dict[str, object]) -> bool:
    faction = str(agent.get("faction", "material"))
    kind = str(proposal.get("kind", "unknown"))
    return kind in FACTION_PRIORITIES.get(faction, set())


def should_disagree(agent: dict[str, object], proposal: dict[str, object]) -> bool:
    if aligns_with_faction(agent, proposal):
        return False
    requested = float(proposal.get("requested_budget", 0.0))
    severity = float(proposal.get("severity", 0.0))
    proposer_role = str(proposal.get("role", "agent"))
    return requested >= 16.0 or severity >= 0.46 or proposer_role != str(agent.get("role", "agent"))


def choose_agent(index: int, intent: str, proposal: dict[str, object], profiles: Sequence[dict[str, object]]) -> dict[str, object]:
    if intent == "disagreement":
        for offset in range(len(profiles)):
            candidate = profiles[(index * 3 + offset) % len(profiles)]
            if should_disagree(candidate, proposal):
                return candidate
    return profiles[(index * 5 + int(proposal.get("council", 0))) % len(profiles)]


def make_question(intent: str, index: int, agent: dict[str, object], proposal: dict[str, object], council: dict[str, object], shadow: dict[str, object]) -> str:
    prefix = NOISE_PREFIXES[index % len(NOISE_PREFIXES)]
    council_id = int(council.get("council", proposal.get("council", 0)))
    proposal_id = str(proposal.get("id", "unknown-proposal"))
    role = str(proposal.get("role", "agent"))
    if intent == "acceptance":
        core = f"why did council {council_id} accept {proposal_id} from the {role}?"
    elif intent == "benefit":
        core = f"who benefited when {proposal_id} received budget?"
    elif intent == "maintenance":
        core = f"why did they service maintenance debt on {proposal.get('project', 'the project')}?"
    elif intent == "token":
        core = f"what native word or token grounded {proposal_id}?"
    elif intent == "disagreement":
        core = f"do you, {agent.get('name', 'agent')}, disagree with accepting {proposal_id}?"
    elif intent == "change":
        core = f"what route, object, or project changed after {proposal_id}?"
    else:
        core = f"why was overreach rejected in council {council_id}, and what can we honestly know from {shadow['id']}?"
    return prefix + core


def parse_question(question: str, condition: Condition) -> str:
    if not condition.question_parser:
        return "unparsed"
    text = question.lower()
    if "reject" in text or "overreach" in text:
        return "rejection"
    if "disagree" in text:
        return "disagreement"
    if "benefit" in text or "who benefited" in text or "received budget" in text:
        return "benefit"
    if "maintenance" in text or "debt" in text:
        return "maintenance"
    if "token" in text or "native word" in text or "word" in text:
        return "token"
    if "changed" in text or "what route" in text or "what object" in text or "what project" in text:
        return "change"
    if "accept" in text or "accepted" in text:
        return "acceptance"
    return "unknown"


def benefit_loop(proposal: dict[str, object]) -> dict[str, object]:
    kind = str(proposal.get("kind", "unknown"))
    beneficiaries = list(BENEFIT_BY_KIND.get(kind, (str(proposal.get("role", "agent")),)))
    return {
        "proposal": proposal.get("id"),
        "kind": kind,
        "beneficiaries": beneficiaries,
        "route": proposal.get("route"),
        "object": proposal.get("object"),
        "project": proposal.get("project"),
        "allocated": proposal.get("allocated", 0),
    }


def token_from_proposal(proposal: dict[str, object], condition: Condition) -> str:
    token = str(proposal.get("native_token", "ungrounded"))
    if not condition.native_token_grounding or token == "ungrounded":
        return "withheld"
    return token


def answer_session(session: dict[str, object], condition: Condition, public_ledger: list[dict[str, object]]) -> dict[str, object]:
    question = str(session["question"])
    agent = session["agent"]
    proposal = session["proposal"]
    council = session["council"]
    shadow = session["shadow"]
    parsed_intent = parse_question(question, condition)
    parsed = parsed_intent not in {"unparsed", "unknown"}
    retrieved = bool(parsed and condition.governance_memory)
    details: set[str] = set()
    pieces: list[str] = []

    if parsed:
        details.add("parsed")
    if condition.role_perspective:
        details.update({"role", "faction"})
        pieces.append(
            f"{agent['name']} answers as {agent['role']} in the {agent['faction']} faction."
        )
    else:
        pieces.append("A council narrator answers without a role-specific perspective.")

    if not parsed:
        pieces.append("The local parser did not bind the question to a governance intent.")
    elif not condition.governance_memory:
        pieces.append("Governance memory is disabled, so the answer cannot retrieve a council event.")
    else:
        details.add("council")
        if parsed_intent == "rejection":
            details.update({"rejection_shadow", "limitation"})
            pieces.append(
                f"Council {shadow['council']} has {shadow['rejected_count']} rejected proposals in the persisted record."
            )
            pieces.append(
                f"I bind this to {shadow['id']}, a rejection shadow, because full rejected proposal bodies were not stored."
            )
            if condition.evidence_trace_binding:
                details.add("evidence")
                tight = ", ".join(shadow.get("budget_tight_materials", [])) or "no single tight material"
                pieces.append(f"Trace evidence says reason={shadow['reason']} and tight_materials={tight}.")
        else:
            details.add("proposal_id")
            pieces.append(
                f"Council {proposal.get('council')} accepted {proposal.get('id')} with severity {proposal.get('severity')} and score {proposal.get('score')}."
            )
            if parsed_intent == "acceptance":
                details.update({"pressure", "score"})
                pieces.append(
                    f"The pressure mix was route={proposal.get('route_pressure')}, object={proposal.get('object_pressure')}, maintenance={proposal.get('maintenance_pressure')}."
                )
            elif parsed_intent == "benefit":
                loop = benefit_loop(proposal)
                details.update({"benefit", "allocated"})
                pieces.append(
                    f"The benefit loop names {', '.join(loop['beneficiaries'])} and allocated {loop['allocated']} material units."
                )
            elif parsed_intent == "maintenance":
                details.update({"project", "feedback"})
                feedback = proposal.get("feedback", {}) if isinstance(proposal.get("feedback", {}), dict) else {}
                pieces.append(
                    f"The project was {proposal.get('project')}; debt_delta={feedback.get('debt_delta', 0)} after service."
                )
            elif parsed_intent == "token":
                details.add("token")
                token = token_from_proposal(proposal, condition)
                pieces.append(
                    f"The grounding token is {token} for focus {proposal.get('focus', 'unknown-focus')}."
                )
            elif parsed_intent == "disagreement":
                opportunity = should_disagree(agent, proposal)
                if condition.disagreement_model and opportunity:
                    details.add("disagreement")
                    agent["disagreement_count"] = int(agent.get("disagreement_count", 0)) + 1
                    pieces.append(
                        f"I disagree because {proposal.get('kind')} serves another faction before my {agent['faction']} priority."
                    )
                elif condition.disagreement_model:
                    pieces.append("I do not object; this proposal fits my faction priority enough to accept it.")
                else:
                    pieces.append("The disagreement model is disabled, so dissent is not expressed.")
            elif parsed_intent == "change":
                details.update({"route", "object", "project", "feedback"})
                feedback = proposal.get("feedback", {}) if isinstance(proposal.get("feedback", {}), dict) else {}
                pieces.append(
                    f"The changed path/object/project were route={proposal.get('route')}, object={proposal.get('object')}, project={proposal.get('project')}."
                )
                pieces.append(
                    f"Feedback deltas were route={feedback.get('route_delta', 0)}, object={feedback.get('object_delta', 0)}, debt={feedback.get('debt_delta', 0)}."
                )
            if condition.evidence_trace_binding:
                details.add("evidence")
                pieces.append(
                    f"Evidence trace binds proposal_id={proposal.get('id')} to season={proposal.get('season')} and rejected_count={proposal.get('council_rejected_count')}."
                )
            if condition.native_token_grounding and parsed_intent != "token":
                details.add("token")
                pieces.append(f"Native token check: {token_from_proposal(proposal, condition)}.")

    state_updated = False
    if condition.state_update_from_dialogue and retrieved:
        state_updated = True
        details.add("state_update")
        agent["questioned_count"] = int(agent.get("questioned_count", 0)) + 1
        memory = agent.setdefault("governance_dialogue_memory", [])
        if isinstance(memory, list):
            memory.append(
                {
                    "session_id": session["session_id"],
                    "intent": parsed_intent,
                    "proposal": proposal.get("id"),
                    "council": proposal.get("council", shadow.get("council")),
                    "stored_as": "dialogue_state_only",
                }
            )
        public_ledger.append(
            {
                "session_id": session["session_id"],
                "agent_id": agent.get("agent_id"),
                "intent": parsed_intent,
                "proposal": proposal.get("id"),
                "rollback_hook": f"remove-dialogue-memory:{session['session_id']}",
            }
        )

    answer = " ".join(pieces)
    evidence_bound = bool(retrieved and condition.evidence_trace_binding and "evidence" in details)
    native_bound = bool(retrieved and condition.native_token_grounding and "token" in details)
    perspective_consistent = bool(condition.role_perspective and agent.get("faction") == faction_for_role(str(agent.get("role", "agent"))))
    disagreement_opportunity = bool(parsed_intent == "disagreement" and retrieved and should_disagree(agent, proposal))
    disagreement_expressed = bool(disagreement_opportunity and condition.disagreement_model and "disagreement" in details)
    specificity = clamp(len(details) / 11.0)
    return {
        "condition": condition.name,
        "session_id": session["session_id"],
        "question": question,
        "intended_intent": session["intent"],
        "parsed_intent": parsed_intent,
        "agent_id": agent.get("agent_id"),
        "agent_name": agent.get("name"),
        "agent_role": agent.get("role"),
        "faction": agent.get("faction"),
        "council": proposal.get("council", shadow.get("council")),
        "proposal_id": proposal.get("id"),
        "answer": answer,
        "parsed": parsed,
        "retrieved": retrieved,
        "evidence_bound": evidence_bound,
        "native_token_bound": native_bound,
        "perspective_consistent": perspective_consistent,
        "disagreement_opportunity": disagreement_opportunity,
        "disagreement_expressed": disagreement_expressed,
        "state_updated": state_updated,
        "answer_specificity_score": round(specificity, 6),
        "trace_replay_included": condition.trace_replay,
    }


def build_sessions(cfg: DialogueConfig, history: Sequence[dict[str, object]], events: Sequence[dict[str, object]], profiles: Sequence[dict[str, object]]) -> list[dict[str, object]]:
    sessions: list[dict[str, object]] = []
    councils = [council for council in history if isinstance(council, dict)]
    for index in range(cfg.sessions):
        intent = QUESTION_INTENTS[index % len(QUESTION_INTENTS)]
        proposal = copy.deepcopy(events[(index * 7 + cfg.seed) % len(events)])
        council = copy.deepcopy(councils[(int(proposal.get("council", index)) - 1) % len(councils)])
        if intent == "rejection":
            council = copy.deepcopy(councils[(index * 5 + cfg.seed) % len(councils)])
            accepted = council.get("accepted_proposals", [])
            if isinstance(accepted, list) and accepted:
                proposal = copy.deepcopy(accepted[(index + cfg.seed) % len(accepted)])
                proposal["season"] = council.get("season", "unknown-season")
                proposal["council_rejected_count"] = council.get("rejected_count", 0)
                proposal["council_budget_remaining"] = copy.deepcopy(council.get("budget_remaining", {}))
        agent = choose_agent(index, intent, proposal, profiles)
        shadow = rejection_shadow(council)
        sessions.append(
            {
                "session_id": f"dlg_{index:03d}_{intent}",
                "intent": intent,
                "question": make_question(intent, index, agent, proposal, council, shadow),
                "agent": agent,
                "proposal": proposal,
                "council": council,
                "shadow": shadow,
            }
        )
    return sessions


def run_condition(cfg: DialogueConfig, condition: Condition, source_agents: Sequence[dict[str, object]], source_state: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    profiles = build_agent_profiles(source_agents, source_state)
    history = source_state.get("governance_history", [])
    if not isinstance(history, list):
        raise ValueError("governance_history must be a list")
    events = flatten_accepted(history)
    sessions = build_sessions(cfg, history, events, profiles)
    public_ledger: list[dict[str, object]] = []
    records: list[dict[str, object]] = []
    for session in sessions:
        records.append(answer_session(session, condition, public_ledger))

    total = max(1, len(records))
    question_parse_rate = sum(1 for item in records if item["parsed"]) / total
    governance_memory_retrieval_rate = sum(1 for item in records if item["retrieved"]) / total
    evidence_trace_binding_rate = sum(1 for item in records if item["evidence_bound"]) / total
    native_token_grounding_rate = sum(1 for item in records if item["native_token_bound"]) / total
    role_perspective_consistency = sum(1 for item in records if item["perspective_consistent"]) / total
    disagreement_opportunities = sum(1 for item in records if item["disagreement_opportunity"])
    disagreement_expression_rate = (
        sum(1 for item in records if item["disagreement_expressed"]) / disagreement_opportunities
        if disagreement_opportunities
        else 0.0
    )
    state_update_from_dialogue_rate = sum(1 for item in records if item["state_updated"]) / total
    answer_specificity_score = mean(float(item["answer_specificity_score"]) for item in records)
    represented_factions = {str(item["faction"]) for item in records if item["perspective_consistent"]}
    faction_diversity_score = len(represented_factions) / max(1, len(set(ROLE_FACTION.values())))
    trace = records if condition.trace_replay else []
    trace_completeness = 1.0 if condition.trace_replay and len(trace) == cfg.sessions else 0.0
    readiness = (
        question_parse_rate * 0.10
        + governance_memory_retrieval_rate * 0.13
        + evidence_trace_binding_rate * 0.13
        + native_token_grounding_rate * 0.10
        + role_perspective_consistency * 0.10
        + disagreement_expression_rate * 0.08
        + state_update_from_dialogue_rate * 0.12
        + answer_specificity_score * 0.12
        + faction_diversity_score * 0.07
        + trace_completeness * 0.05
    )
    row = EvalRow(
        condition=condition.name,
        sessions=cfg.sessions,
        question_parse_rate=round(question_parse_rate, 6),
        governance_memory_retrieval_rate=round(governance_memory_retrieval_rate, 6),
        evidence_trace_binding_rate=round(evidence_trace_binding_rate, 6),
        native_token_grounding_rate=round(native_token_grounding_rate, 6),
        role_perspective_consistency=round(role_perspective_consistency, 6),
        disagreement_expression_rate=round(disagreement_expression_rate, 6),
        state_update_from_dialogue_rate=round(state_update_from_dialogue_rate, 6),
        answer_specificity_score=round(answer_specificity_score, 6),
        faction_diversity_score=round(faction_diversity_score, 6),
        trace_completeness=round(trace_completeness, 6),
        dialogue_readiness=round(readiness, 6),
    )
    memory_escrow = [rejection_shadow(council) for council in history if isinstance(council, dict) and int(council.get("rejected_count", 0)) > 0]
    disagreement_shadows = [item for item in records if item["disagreement_expressed"]]
    benefit_flow_loops = [benefit_loop(event) for event in events[: min(32, len(events))]]
    rollback_hooks = [entry["rollback_hook"] for entry in public_ledger]
    state = {
        "condition": condition.name,
        "source_state": str(SOURCE_STATE),
        "source_agents": str(SOURCE_AGENTS),
        "agents": {str(profile["agent_id"]): profile for profile in profiles},
        "dialogue_sessions": records,
        "public_question_ledger": public_ledger,
        "memory_escrow": memory_escrow,
        "benefit_flow_loops": benefit_flow_loops,
        "disagreement_shadows": disagreement_shadows,
        "rollback_hooks": rollback_hooks,
        "dialogue_objects": {
            "rejection_shadow": "honest marker for rejected counts without stored proposal bodies",
            "benefit_flow_loop": "proposal to budget to route/object/project to role/faction benefit",
            "disagreement_shadow": "agent dissent attached to accepted council action",
            "rollback_hook": "dialogue-state-only mutation that can be removed by session id",
            "memory_escrow": "stored limitation notes that prevent filling missing evidence",
        },
    }
    return row, trace, state


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_governance_memory_dialogue"]

    def loss(name: str) -> float:
        return round(full.dialogue_readiness - by_name[name].dialogue_readiness, 6)

    supports_bridge = (
        full.dialogue_readiness >= 0.90
        and full.governance_memory_retrieval_rate >= 0.99
        and full.evidence_trace_binding_rate >= 0.99
        and full.state_update_from_dialogue_rate >= 0.99
        and full.answer_specificity_score >= 0.70
    )
    return VerdictRow(
        full_condition=full.condition,
        full_dialogue_readiness=full.dialogue_readiness,
        full_question_parse_rate=full.question_parse_rate,
        full_governance_memory_retrieval_rate=full.governance_memory_retrieval_rate,
        full_evidence_trace_binding_rate=full.evidence_trace_binding_rate,
        full_native_token_grounding_rate=full.native_token_grounding_rate,
        full_role_perspective_consistency=full.role_perspective_consistency,
        full_disagreement_expression_rate=full.disagreement_expression_rate,
        full_state_update_from_dialogue_rate=full.state_update_from_dialogue_rate,
        full_answer_specificity_score=full.answer_specificity_score,
        full_faction_diversity_score=full.faction_diversity_score,
        full_trace_completeness=full.trace_completeness,
        no_avatar_question_parser_loss=loss("no_avatar_question_parser"),
        no_governance_memory_loss=loss("no_governance_memory"),
        no_evidence_trace_binding_loss=loss("no_evidence_trace_binding"),
        no_native_token_grounding_loss=loss("no_native_token_grounding"),
        no_role_perspective_loss=loss("no_role_perspective"),
        no_disagreement_model_loss=loss("no_disagreement_model"),
        no_state_update_from_dialogue_loss=loss("no_state_update_from_dialogue"),
        no_trace_replay_loss=loss("no_trace_replay"),
        supports_governance_memory_dialogue_bridge=supports_bridge,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports_bridge else "fail",
    )


def run(cfg: DialogueConfig) -> dict[str, object]:
    source_agents = load_agents(Path(cfg.source_agents))
    source_state = load_state(Path(cfg.source_state))
    rows: list[EvalRow] = []
    integrated_trace: list[dict[str, object]] = []
    integrated_state: dict[str, object] = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(cfg, condition, source_agents, source_state)
        rows.append(row)
        if condition.name == "integrated_governance_memory_dialogue":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {
        "config": asdict(cfg),
        "source_bridge": "Report 149 infrastructure proposal governance bridge",
        "eval_rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "limits": {
            "no_llm_calls": True,
            "deterministic_question_parser_only": True,
            "rejected_proposal_bodies_missing": True,
            "subjective_consciousness_claimed": False,
            "complete_playable_world_claimed": False,
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_GOVERNANCE_MEMORY_DIALOGUE_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_GOVERNANCE_MEMORY_DIALOGUE_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_GOVERNANCE_MEMORY_DIALOGUE_STATE", integrated_state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260624)
    parser.add_argument("--sessions", type=int, default=96)
    parser.add_argument("--source-agents", default=str(SOURCE_AGENTS))
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = DialogueConfig(
        seed=args.seed,
        sessions=args.sessions,
        source_agents=args.source_agents,
        source_state=args.source_state,
    )
    results = run(cfg)
    print(json.dumps(results["verdict"], indent=2))


if __name__ == "__main__":
    main()
