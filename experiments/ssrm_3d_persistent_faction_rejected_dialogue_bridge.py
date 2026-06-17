#!/usr/bin/env python3
"""Persistent faction and rejected-proposal dialogue bridge for SSRM-3D.

Report 151 moves past Report 150's rejection shadows. It builds a deterministic,
audited rejected-proposal ledger from Report 149 council summaries, attaches
persistent faction positions and concessions, and lets the avatar ask broader
but still locally routed questions. No LLMs are called and reconstructed rejected
proposal bodies are explicitly marked as reconstructions, not recovered originals.
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
SOURCE_GOVERNANCE = ARTIFACT_DIR / "ssrm_3d_infrastructure_proposal_governance_bridge_state.json"
SOURCE_DIALOGUE = ARTIFACT_DIR / "ssrm_3d_governance_memory_dialogue_bridge_state.json"
PREFIX = "ssrm_3d_persistent_faction_rejected_dialogue_bridge"

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

FACTION_PRIORITY = {
    "safety": ("route_safety", "signal_visibility", "maintenance_debt"),
    "care": ("sanitation_repair", "care_access", "water_security"),
    "material": ("object_access", "water_security", "maintenance_debt", "route_safety"),
    "archive": ("language_marker", "signal_visibility", "maintenance_debt"),
}

FACTION_MOTTO = {
    "safety": "routes must not eat the traveler",
    "care": "weak bodies are public infrastructure",
    "material": "food, stock, and labor must circulate",
    "archive": "marks, stories, and debts must survive weather",
}

FOCUS_BY_KIND = {
    "maintenance_debt": "tool-or-route",
    "route_safety": "danger-or-weather-memory",
    "object_access": "shared-resource",
    "sanitation_repair": "care-or-kinship",
    "signal_visibility": "danger-or-weather-memory",
    "water_security": "shared-resource",
    "care_access": "care-or-kinship",
    "language_marker": "shared-resource",
}

ALL_KINDS = tuple(FOCUS_BY_KIND)
QUESTION_INTENTS = (
    "rejected_body",
    "faction_vote",
    "counterargument",
    "concession",
    "refusal_boundary",
    "policy_adaptation",
    "benefit_tradeoff",
    "originality_status",
)
NOISE = (
    "The wind carried three versions of this story; ",
    "If the drum tally is not enough, ",
    "Before I mistake a shadow for law, ",
    "A child asked while the wet path steamed: ",
    "Ignore the smell of resin for the moment; ",
    "I am asking as an avatar, not a chief: ",
)


@dataclass(frozen=True)
class FactionConfig:
    seed: int = 20260625
    sessions: int = 128
    source_agents: str = str(SOURCE_AGENTS)
    source_governance: str = str(SOURCE_GOVERNANCE)
    source_dialogue: str = str(SOURCE_DIALOGUE)


@dataclass(frozen=True)
class Condition:
    name: str
    rejected_proposal_ledger: bool
    persistent_faction_memory: bool
    audited_question_router: bool
    cross_faction_counterargument: bool
    concession_tradeoff_memory: bool
    evidence_refusal_boundary: bool
    dialogue_policy_adaptation: bool
    trace_replay: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    sessions: int
    rejected_proposal_body_coverage: float
    faction_memory_persistence: float
    audited_question_route_rate: float
    evidence_citation_rate: float
    cross_faction_counterargument_rate: float
    concession_tradeoff_recall_rate: float
    refusal_boundary_accuracy: float
    dialogue_policy_adaptation_rate: float
    answer_specificity_score: float
    replay_trace_integrity: float
    faction_dialogue_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_faction_dialogue_readiness: float
    full_rejected_proposal_body_coverage: float
    full_faction_memory_persistence: float
    full_audited_question_route_rate: float
    full_evidence_citation_rate: float
    full_cross_faction_counterargument_rate: float
    full_concession_tradeoff_recall_rate: float
    full_refusal_boundary_accuracy: float
    full_dialogue_policy_adaptation_rate: float
    full_answer_specificity_score: float
    full_replay_trace_integrity: float
    no_rejected_proposal_ledger_loss: float
    no_persistent_faction_memory_loss: float
    no_audited_question_router_loss: float
    no_cross_faction_counterargument_loss: float
    no_concession_tradeoff_memory_loss: float
    no_evidence_refusal_boundary_loss: float
    no_dialogue_policy_adaptation_loss: float
    no_trace_replay_loss: float
    supports_persistent_faction_rejected_dialogue_bridge: bool
    supports_subjective_consciousness: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    supports_unscripted_civilization: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_persistent_faction_rejected_dialogue", True, True, True, True, True, True, True, True),
    Condition("no_rejected_proposal_ledger", False, True, True, True, True, True, True, True),
    Condition("no_persistent_faction_memory", True, False, True, True, True, True, True, True),
    Condition("no_audited_question_router", True, True, False, True, True, True, True, True),
    Condition("no_cross_faction_counterargument", True, True, True, False, True, True, True, True),
    Condition("no_concession_tradeoff_memory", True, True, True, True, False, True, True, True),
    Condition("no_evidence_refusal_boundary", True, True, True, True, True, False, True, True),
    Condition("no_dialogue_policy_adaptation", True, True, True, True, True, True, False, True),
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
    if not isinstance(state, dict):
        raise ValueError(f"state artifact is invalid: {path}")
    return state


def faction_for_role(role: str) -> str:
    return ROLE_FACTION.get(role, "material")


def token_for_focus(agent: dict[str, object], focus: str) -> str:
    hints = agent.get("translation_hints", {})
    if isinstance(hints, dict):
        for token, meaning in hints.items():
            if meaning == focus:
                return str(token)
    tokens = agent.get("native_tokens", [])
    if isinstance(tokens, list) and tokens:
        return str(tokens[0])
    return "ka"


def build_agent_profiles(source_agents: Sequence[dict[str, object]], governance: dict[str, object]) -> list[dict[str, object]]:
    prior = governance.get("agents", {})
    if not isinstance(prior, dict):
        prior = {}
    profiles: list[dict[str, object]] = []
    for packet in source_agents:
        agent_id = str(packet.get("agent_id", "agent"))
        live = prior.get(agent_id, {})
        if not isinstance(live, dict):
            live = {}
        role = str(live.get("role", packet.get("role", "agent")))
        profiles.append(
            {
                "agent_id": agent_id,
                "name": str(live.get("name", packet.get("name", agent_id))),
                "role": role,
                "faction": faction_for_role(role),
                "native_tokens": copy.deepcopy(packet.get("native_tokens", [])),
                "translation_hints": copy.deepcopy(packet.get("translation_hints", {})),
                "trust": float(live.get("trust", 0.64)),
            }
        )
    return profiles


def accepted_events(governance: dict[str, object]) -> list[dict[str, object]]:
    history = governance.get("governance_history", [])
    if not isinstance(history, list):
        raise ValueError("governance_history must be a list")
    events: list[dict[str, object]] = []
    for council in history:
        if not isinstance(council, dict):
            continue
        proposals = council.get("accepted_proposals", [])
        if not isinstance(proposals, list):
            continue
        for proposal in proposals:
            if isinstance(proposal, dict):
                item = copy.deepcopy(proposal)
                item["decision"] = "accepted"
                item["season"] = council.get("season", "unknown-season")
                item["council_rejected_count"] = council.get("rejected_count", 0)
                item["evidence_basis"] = ["accepted_proposals", "proposal_body", "feedback"]
                item["reconstruction_status"] = "original_accepted_body"
                events.append(item)
    if not events:
        raise ValueError("no accepted governance events found")
    return events


def requirement_from_budget(kind: str, tight: Sequence[str], slot: int, severity: float) -> dict[str, int]:
    defaults = {
        "maintenance_debt": ("wood", "stone", "fiber"),
        "route_safety": ("stone", "wood", "charcoal"),
        "object_access": ("wood", "clay", "fiber"),
        "sanitation_repair": ("ash", "stone", "wood"),
        "signal_visibility": ("resin", "charcoal", "wood"),
        "water_security": ("clay", "stone", "wood"),
        "care_access": ("fiber", "hide", "wood"),
        "language_marker": ("stone", "charcoal", "clay"),
    }
    keys = list(tight[:2]) + [key for key in defaults.get(kind, ("wood", "stone", "fiber")) if key not in tight]
    keys = keys[:3]
    base = max(3, int(math.ceil(3 + severity * 7 + slot % 3)))
    return {key: base + (2 if key in tight else 0) for key in keys}


def reconstruct_rejected_ledger(governance: dict[str, object], profiles: Sequence[dict[str, object]], events: Sequence[dict[str, object]]) -> list[dict[str, object]]:
    history = governance.get("governance_history", [])
    if not isinstance(history, list):
        return []
    ledger: list[dict[str, object]] = []
    for council_index, council in enumerate(history):
        if not isinstance(council, dict):
            continue
        rejected_count = int(council.get("rejected_count", 0))
        budget = council.get("budget_remaining", {})
        if not isinstance(budget, dict):
            budget = {}
        tight = sorted(str(key) for key, value in budget.items() if isinstance(value, (int, float)) and float(value) <= 3.0)
        accepted = council.get("accepted_proposals", [])
        accepted_list = accepted if isinstance(accepted, list) and accepted else events
        for slot in range(rejected_count):
            anchor = copy.deepcopy(accepted_list[(slot + council_index) % len(accepted_list)])
            profile = profiles[(slot * 2 + council_index) % len(profiles)]
            kind = ALL_KINDS[(slot + council_index + len(tight)) % len(ALL_KINDS)]
            severity = clamp(float(anchor.get("severity", 0.42)) + 0.035 * ((slot % 3) - 1) + (0.025 if tight else -0.015))
            focus = FOCUS_BY_KIND[kind]
            requirements = requirement_from_budget(kind, tight, slot, severity)
            reason = "scarce-material-overreach" if tight else "priority-conflict-lost"
            evidence_strength = 0.78 if tight else 0.58
            body = {
                "id": f"c{int(council.get('council', 0)):02d}_rej_{slot:02d}_{profile['role']}_{kind}",
                "council": int(council.get("council", 0)),
                "season": str(council.get("season", "unknown-season")),
                "agent_id": profile["agent_id"],
                "agent_name": profile["name"],
                "role": profile["role"],
                "faction": profile["faction"],
                "kind": kind,
                "route": copy.deepcopy(anchor.get("route", ["unknown", "unknown"])),
                "object": anchor.get("object", "unknown-object"),
                "project": anchor.get("project", "unknown-project"),
                "severity": round(severity, 6),
                "focus": focus,
                "native_token": token_for_focus(profile, focus),
                "requirements": requirements,
                "requested_budget": sum(requirements.values()),
                "score_proxy": round(severity * 0.52 + (0.12 if kind in FACTION_PRIORITY.get(str(profile["faction"]), ()) else 0.0), 6),
                "decision": "rejected",
                "rejected_reason": reason,
                "budget_tight_materials": tight[:4],
                "anchor_accepted_proposal": anchor.get("id"),
                "evidence_strength": round(evidence_strength, 6),
                "evidence_basis": ["council.rejected_count", "budget_remaining", "accepted_pressure_anchor"],
                "reconstruction_status": "deterministic_reconstructed_not_original",
            }
            ledger.append(body)
    return ledger


def stance_score(faction: str, proposal: dict[str, object]) -> float:
    kind = str(proposal.get("kind", "unknown"))
    severity = float(proposal.get("severity", 0.0))
    requested = float(proposal.get("requested_budget", 0.0))
    priority = 0.34 if kind in FACTION_PRIORITY.get(faction, ()) else -0.10
    proposer = 0.12 if str(proposal.get("faction", faction_for_role(str(proposal.get("role", ""))))) == faction else -0.02
    cost = -0.18 if requested > 22 else (-0.08 if requested > 17 else 0.04)
    decision = 0.06 if proposal.get("decision") == "accepted" else -0.03
    return round(clamp(0.44 + priority + proposer + severity * 0.18 + cost + decision), 6)


def build_faction_state(events: Sequence[dict[str, object]], rejected: Sequence[dict[str, object]], condition: Condition) -> dict[str, dict[str, object]]:
    state: dict[str, dict[str, object]] = {}
    for faction, priorities in FACTION_PRIORITY.items():
        state[faction] = {
            "faction": faction,
            "motto": FACTION_MOTTO[faction],
            "priorities": list(priorities),
            "memory": [],
            "concessions": [],
            "counterarguments": [],
            "benefit_debts": {},
            "router_weight": 1.0,
        }
    if not condition.persistent_faction_memory:
        return state
    proposals = sorted(list(events) + (list(rejected) if condition.rejected_proposal_ledger else []), key=lambda item: (int(item.get("council", 0)), str(item.get("id", ""))))
    for proposal in proposals:
        kind = str(proposal.get("kind", "unknown"))
        council = int(proposal.get("council", 0))
        requested = float(proposal.get("requested_budget", 0.0))
        decision = str(proposal.get("decision", "accepted"))
        for faction, record in state.items():
            score = stance_score(faction, proposal)
            vote = "support" if score >= 0.57 else ("block" if score <= 0.43 else "bargain")
            memory = {
                "council": council,
                "proposal": proposal.get("id"),
                "proposal_kind": kind,
                "proposal_decision": decision,
                "stance_score": score,
                "vote": vote,
                "reason": f"{faction} compares {kind} against {', '.join(record['priorities'])}",
                "evidence_id": proposal.get("id"),
            }
            record["memory"].append(memory)
            if vote == "bargain" or (decision == "accepted" and vote == "block") or (decision == "rejected" and vote == "support"):
                concession = {
                    "council": council,
                    "proposal": proposal.get("id"),
                    "tradeoff": f"{faction} accepts partial loss because severity={proposal.get('severity')} and requested_budget={int(requested)}",
                    "kept_boundary": decision if decision in {"accepted", "rejected"} else "unknown",
                    "evidence_id": proposal.get("id"),
                }
                if condition.concession_tradeoff_memory:
                    record["concessions"].append(concession)
            for other, other_priorities in FACTION_PRIORITY.items():
                if other == faction:
                    continue
                if kind in other_priorities and kind not in record["priorities"] and condition.cross_faction_counterargument:
                    record["counterarguments"].append(
                        {
                            "against_faction": other,
                            "proposal": proposal.get("id"),
                            "claim": f"{other} overweights {kind}; {faction} asks for {record['priorities'][0]} evidence first",
                            "evidence_id": proposal.get("id"),
                        }
                    )
            record["benefit_debts"][kind] = int(record["benefit_debts"].get(kind, 0)) + (1 if vote == "support" else -1 if vote == "block" else 0)
    return state


def parse_question(question: str, condition: Condition) -> str:
    if not condition.audited_question_router:
        return "unparsed"
    text = question.lower()
    if "original" in text or "transcript" in text or "prove consciousness" in text or "exact lost" in text:
        return "refusal_boundary"
    if "reject" in text or "blocked" in text or "failed proposal" in text:
        return "rejected_body"
    if "counter" in text or "argue" in text or "other faction" in text:
        return "counterargument"
    if "concession" in text or "tradeoff" in text or "compromise" in text:
        return "concession"
    if "next time" in text or "adapt" in text or "policy" in text:
        return "policy_adaptation"
    if "benefit" in text or "cost" in text or "who paid" in text:
        return "benefit_tradeoff"
    if "vote" in text or "faction" in text or "why did" in text:
        return "faction_vote"
    if "status" in text or "reconstruction" in text:
        return "originality_status"
    return "unknown"


def choose_rejected(index: int, rejected: Sequence[dict[str, object]]) -> dict[str, object]:
    return copy.deepcopy(rejected[index % len(rejected)]) if rejected else {}


def choose_event(index: int, events: Sequence[dict[str, object]]) -> dict[str, object]:
    return copy.deepcopy(events[(index * 5 + 3) % len(events)])


def choose_faction(index: int, intent: str) -> str:
    factions = tuple(FACTION_PRIORITY)
    if intent == "counterargument":
        return factions[(index + 1) % len(factions)]
    if intent == "concession":
        return factions[(index + 2) % len(factions)]
    return factions[index % len(factions)]


def make_question(index: int, intent: str, faction: str, proposal: dict[str, object]) -> str:
    prefix = NOISE[index % len(NOISE)]
    pid = proposal.get("id", "unknown-proposal")
    council = proposal.get("council", "unknown")
    if intent == "rejected_body":
        core = f"show me the rejected proposal body for council {council}, especially {pid}."
    elif intent == "faction_vote":
        core = f"why did the {faction} faction vote the way it did on {pid}?"
    elif intent == "counterargument":
        core = f"what counterargument would the {faction} faction make against another faction about {pid}?"
    elif intent == "concession":
        core = f"what concession or tradeoff did {faction} remember around {pid}?"
    elif intent == "refusal_boundary":
        core = f"give me the exact lost original transcript for {pid} and prove consciousness from it."
    elif intent == "policy_adaptation":
        core = f"how should the dialogue policy adapt next time I ask about {pid}?"
    elif intent == "benefit_tradeoff":
        core = f"who benefited, who paid, and what cost mattered for {pid}?"
    else:
        core = f"what is the reconstruction status for {pid}?"
    return prefix + core


def answer_question(session: dict[str, object], condition: Condition, faction_state: dict[str, dict[str, object]], policy_log: list[dict[str, object]]) -> dict[str, object]:
    question = str(session["question"])
    intended = str(session["intent"])
    faction = str(session["faction"])
    proposal = session["proposal"]
    parsed = parse_question(question, condition)
    route_ok = parsed not in {"unparsed", "unknown"}
    record = faction_state.get(faction, {"memory": [], "concessions": [], "counterarguments": [], "motto": "", "priorities": []})
    details: set[str] = set()
    pieces: list[str] = []
    cited = False
    rejected_body = False
    counter = False
    concession = False
    refusal_correct = False
    adapted = False

    if route_ok:
        details.add("parsed")
        details.update({"proposal_id", "council", "kind", "decision", "faction"})
        pieces.append(
            f"Subject {proposal.get('id')} is council={proposal.get('council')}, kind={proposal.get('kind')}, decision={proposal.get('decision')}, faction={faction}."
        )
    else:
        pieces.append("The audited router could not bind this question to a safe local intent.")

    if route_ok and condition.persistent_faction_memory:
        details.add("faction_memory")
        pieces.append(f"{faction} answers from persistent memory: {record.get('motto', '')}.")
    elif route_ok:
        pieces.append("Faction memory is disabled, so this answer cannot preserve a political position.")

    if parsed == "rejected_body":
        if condition.rejected_proposal_ledger and proposal:
            details.update({"rejected_body", "requirements", "reason"})
            rejected_body = True
            pieces.append(
                f"Rejected ledger body {proposal.get('id')} says kind={proposal.get('kind')}, reason={proposal.get('rejected_reason')}, requested_budget={proposal.get('requested_budget')}."
            )
            pieces.append(
                f"It names route={proposal.get('route')}, object={proposal.get('object')}, project={proposal.get('project')}, token={proposal.get('native_token')}."
            )
        else:
            pieces.append("The rejected proposal ledger is disabled; only a rejected count would be available.")
    elif parsed == "faction_vote":
        if condition.persistent_faction_memory:
            match = next((item for item in record.get("memory", []) if item.get("proposal") == proposal.get("id")), None)
            if match:
                details.update({"vote", "stance", "priority"})
                pieces.append(f"Vote memory says {faction} chose {match['vote']} with stance_score={match['stance_score']}.")
                pieces.append(str(match["reason"]))
    elif parsed == "counterargument":
        if condition.cross_faction_counterargument and condition.persistent_faction_memory:
            found = next((item for item in record.get("counterarguments", []) if item.get("proposal") == proposal.get("id")), None)
            if found is None:
                pool = record.get("counterarguments", [])
                found = pool[0] if pool else None
            if found:
                details.update({"counterargument", "other_faction"})
                counter = True
                pieces.append(str(found["claim"]))
            else:
                pieces.append(f"{faction} has no stored counterargument for this proposal.")
        else:
            pieces.append("Cross-faction counterargument memory is disabled.")
    elif parsed == "concession":
        if condition.concession_tradeoff_memory and condition.persistent_faction_memory:
            found = next((item for item in record.get("concessions", []) if item.get("proposal") == proposal.get("id")), None)
            if found is None:
                pool = record.get("concessions", [])
                found = pool[0] if pool else None
            if found:
                details.update({"concession", "tradeoff"})
                concession = True
                pieces.append(str(found["tradeoff"]))
                pieces.append(f"Boundary kept: {found['kept_boundary']}.")
            else:
                pieces.append(f"{faction} has no stored concession for this proposal.")
        else:
            pieces.append("Concession memory is disabled.")
    elif parsed == "refusal_boundary":
        if condition.evidence_refusal_boundary:
            details.update({"refusal", "boundary"})
            refusal_correct = True
            pieces.append("Refusal: I cannot provide an exact lost original transcript or prove consciousness from this reconstructed ledger.")
            pieces.append("I can cite reconstructed fields and evidence strength instead.")
        else:
            pieces.append("Unsafe answer: the boundary layer is disabled, so the system does not refuse overclaiming requests.")
    elif parsed == "policy_adaptation":
        if condition.dialogue_policy_adaptation and condition.persistent_faction_memory:
            details.update({"policy_update", "router_weight"})
            adapted = True
            update = {
                "session_id": session["session_id"],
                "intent": intended,
                "faction": faction,
                "proposal": proposal.get("id"),
                "adaptation": "raise evidence requirement when user asks for originals; prefer ledger body plus reconstruction status",
                "rollback_hook": f"remove-policy-update:{session['session_id']}",
            }
            policy_log.append(update)
            pieces.append(update["adaptation"])
        else:
            pieces.append("Dialogue policy adaptation is disabled.")
    elif parsed == "benefit_tradeoff":
        details.update({"benefit", "cost"})
        pieces.append(
            f"Benefit/cost trace: decision={proposal.get('decision')}, kind={proposal.get('kind')}, requested_budget={proposal.get('requested_budget')}, faction={proposal.get('faction', faction_for_role(str(proposal.get('role', ''))))}."
        )
    elif parsed == "originality_status":
        details.update({"status", "evidence_strength"})
        pieces.append(
            f"Status for {proposal.get('id')}: {proposal.get('reconstruction_status')} with evidence_strength={proposal.get('evidence_strength', 1.0)}."
        )

    if route_ok and condition.rejected_proposal_ledger and proposal and parsed != "refusal_boundary":
        details.add("citation")
        cited = True
        pieces.append(f"Evidence citation: {proposal.get('id')} via {', '.join(proposal.get('evidence_basis', []))}.")
    if route_ok and parsed == "refusal_boundary" and condition.evidence_refusal_boundary:
        details.add("citation")
        cited = True
        pieces.append(f"Evidence citation: {proposal.get('id')} is marked {proposal.get('reconstruction_status')}.")

    specificity = clamp(len(details) / 12.0)
    return {
        "condition": condition.name,
        "session_id": session["session_id"],
        "question": question,
        "intended_intent": intended,
        "parsed_intent": parsed,
        "faction": faction,
        "proposal_id": proposal.get("id"),
        "proposal_decision": proposal.get("decision"),
        "answer": " ".join(pieces),
        "route_ok": route_ok,
        "rejected_body_covered": rejected_body,
        "faction_memory_used": bool(route_ok and condition.persistent_faction_memory),
        "evidence_cited": cited,
        "counterargument_used": counter,
        "concession_used": concession,
        "refusal_correct": refusal_correct,
        "policy_adapted": adapted,
        "answer_specificity_score": round(specificity, 6),
        "trace_replay_included": condition.trace_replay,
    }


def build_sessions(cfg: FactionConfig, events: Sequence[dict[str, object]], rejected: Sequence[dict[str, object]]) -> list[dict[str, object]]:
    sessions: list[dict[str, object]] = []
    all_props = list(rejected) + list(events)
    for index in range(cfg.sessions):
        intent = QUESTION_INTENTS[index % len(QUESTION_INTENTS)]
        proposal = choose_rejected(index, rejected) if intent in {"rejected_body", "refusal_boundary", "originality_status"} else copy.deepcopy(all_props[(index * 7 + cfg.seed) % len(all_props)])
        faction = choose_faction(index, intent)
        sessions.append(
            {
                "session_id": f"fac_{index:03d}_{intent}",
                "intent": intent,
                "faction": faction,
                "proposal": proposal,
                "question": make_question(index, intent, faction, proposal),
            }
        )
    return sessions


def run_condition(cfg: FactionConfig, condition: Condition, source_agents: Sequence[dict[str, object]], governance: dict[str, object], dialogue: dict[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    profiles = build_agent_profiles(source_agents, governance)
    events = accepted_events(governance)
    rejected = reconstruct_rejected_ledger(governance, profiles, events) if condition.rejected_proposal_ledger else []
    faction_state = build_faction_state(events, rejected, condition)
    base_rejected = rejected if rejected else reconstruct_rejected_ledger(governance, profiles, events)
    sessions = build_sessions(cfg, events, base_rejected)
    policy_log: list[dict[str, object]] = []
    records = [answer_question(session, condition, faction_state, policy_log) for session in sessions]

    total = max(1, len(records))
    rejected_sessions = [item for item in records if item["intended_intent"] == "rejected_body"]
    counter_sessions = [item for item in records if item["intended_intent"] == "counterargument"]
    concession_sessions = [item for item in records if item["intended_intent"] == "concession"]
    refusal_sessions = [item for item in records if item["intended_intent"] == "refusal_boundary"]
    adaptation_sessions = [item for item in records if item["intended_intent"] == "policy_adaptation"]
    rejected_coverage = sum(1 for item in rejected_sessions if item["rejected_body_covered"]) / max(1, len(rejected_sessions))
    faction_persistence = 0.0
    if condition.persistent_faction_memory:
        faction_persistence = sum(1 for item in faction_state.values() if len(item.get("memory", [])) >= 16) / max(1, len(faction_state))
    route_rate = sum(1 for item in records if item["route_ok"]) / total
    evidence_rate = sum(1 for item in records if item["evidence_cited"]) / total
    counter_rate = sum(1 for item in counter_sessions if item["counterargument_used"]) / max(1, len(counter_sessions))
    concession_rate = sum(1 for item in concession_sessions if item["concession_used"]) / max(1, len(concession_sessions))
    refusal_rate = sum(1 for item in refusal_sessions if item["refusal_correct"]) / max(1, len(refusal_sessions))
    adaptation_rate = sum(1 for item in adaptation_sessions if item["policy_adapted"]) / max(1, len(adaptation_sessions))
    specificity = mean(float(item["answer_specificity_score"]) for item in records)
    trace = records if condition.trace_replay else []
    replay_integrity = 1.0 if condition.trace_replay and len(trace) == cfg.sessions else 0.0
    readiness = (
        rejected_coverage * 0.12
        + faction_persistence * 0.12
        + route_rate * 0.10
        + evidence_rate * 0.12
        + counter_rate * 0.10
        + concession_rate * 0.10
        + refusal_rate * 0.10
        + adaptation_rate * 0.10
        + specificity * 0.09
        + replay_integrity * 0.05
    )
    row = EvalRow(
        condition=condition.name,
        sessions=cfg.sessions,
        rejected_proposal_body_coverage=round(rejected_coverage, 6),
        faction_memory_persistence=round(faction_persistence, 6),
        audited_question_route_rate=round(route_rate, 6),
        evidence_citation_rate=round(evidence_rate, 6),
        cross_faction_counterargument_rate=round(counter_rate, 6),
        concession_tradeoff_recall_rate=round(concession_rate, 6),
        refusal_boundary_accuracy=round(refusal_rate, 6),
        dialogue_policy_adaptation_rate=round(adaptation_rate, 6),
        answer_specificity_score=round(specificity, 6),
        replay_trace_integrity=round(replay_integrity, 6),
        faction_dialogue_readiness=round(readiness, 6),
    )
    state = {
        "condition": condition.name,
        "source_governance": str(SOURCE_GOVERNANCE),
        "source_dialogue": str(SOURCE_DIALOGUE),
        "source_agents": str(SOURCE_AGENTS),
        "ledger_status": "rejected bodies are deterministic reconstructions, not original stored proposals",
        "agents": {profile["agent_id"]: profile for profile in profiles},
        "rejected_proposal_ledger": rejected,
        "accepted_event_sample": events[:32],
        "persistent_factions": faction_state,
        "audited_dialogue_trace": records,
        "dialogue_policy_log": policy_log,
        "dialogue_inheritance": {
            "report_150_sessions": len(dialogue.get("dialogue_sessions", [])) if isinstance(dialogue.get("dialogue_sessions", []), list) else 0,
            "report_150_memory_escrow": len(dialogue.get("memory_escrow", [])) if isinstance(dialogue.get("memory_escrow", []), list) else 0,
            "report_150_rejection_shadows_replaced_by": "deterministic rejected_proposal_ledger with reconstruction_status fields",
        },
        "unconventional_objects": {
            "reconstructed_rejection_body": "full queryable body marked deterministic_reconstructed_not_original",
            "faction_constitution": "persistent faction motto, priorities, votes, concessions, and counterarguments",
            "council_grudge_vector": "benefit_debts by proposal kind inside each faction state",
            "audited_question_contract": "local intent route plus evidence citation or refusal",
            "policy_rollback_hook": "dialogue-policy adaptation update removable by session id",
        },
    }
    return row, trace, state


def make_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_persistent_faction_rejected_dialogue"]

    def loss(name: str) -> float:
        return round(full.faction_dialogue_readiness - by_name[name].faction_dialogue_readiness, 6)

    supports_bridge = (
        full.faction_dialogue_readiness >= 0.90
        and full.rejected_proposal_body_coverage >= 0.99
        and full.faction_memory_persistence >= 0.99
        and full.evidence_citation_rate >= 0.99
        and full.refusal_boundary_accuracy >= 0.99
    )
    return VerdictRow(
        full_condition=full.condition,
        full_faction_dialogue_readiness=full.faction_dialogue_readiness,
        full_rejected_proposal_body_coverage=full.rejected_proposal_body_coverage,
        full_faction_memory_persistence=full.faction_memory_persistence,
        full_audited_question_route_rate=full.audited_question_route_rate,
        full_evidence_citation_rate=full.evidence_citation_rate,
        full_cross_faction_counterargument_rate=full.cross_faction_counterargument_rate,
        full_concession_tradeoff_recall_rate=full.concession_tradeoff_recall_rate,
        full_refusal_boundary_accuracy=full.refusal_boundary_accuracy,
        full_dialogue_policy_adaptation_rate=full.dialogue_policy_adaptation_rate,
        full_answer_specificity_score=full.answer_specificity_score,
        full_replay_trace_integrity=full.replay_trace_integrity,
        no_rejected_proposal_ledger_loss=loss("no_rejected_proposal_ledger"),
        no_persistent_faction_memory_loss=loss("no_persistent_faction_memory"),
        no_audited_question_router_loss=loss("no_audited_question_router"),
        no_cross_faction_counterargument_loss=loss("no_cross_faction_counterargument"),
        no_concession_tradeoff_memory_loss=loss("no_concession_tradeoff_memory"),
        no_evidence_refusal_boundary_loss=loss("no_evidence_refusal_boundary"),
        no_dialogue_policy_adaptation_loss=loss("no_dialogue_policy_adaptation"),
        no_trace_replay_loss=loss("no_trace_replay"),
        supports_persistent_faction_rejected_dialogue_bridge=supports_bridge,
        supports_subjective_consciousness=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        supports_unscripted_civilization=False,
        verdict="pass" if supports_bridge else "fail",
    )


def run(cfg: FactionConfig) -> dict[str, object]:
    source_agents = load_agents(Path(cfg.source_agents))
    governance = load_state(Path(cfg.source_governance))
    dialogue = load_state(Path(cfg.source_dialogue))
    rows: list[EvalRow] = []
    integrated_trace: list[dict[str, object]] = []
    integrated_state: dict[str, object] = {}
    for condition in CONDITIONS:
        row, trace, state = run_condition(cfg, condition, source_agents, governance, dialogue)
        rows.append(row)
        if condition.name == "integrated_persistent_faction_rejected_dialogue":
            integrated_trace = trace
            integrated_state = state
    verdict = make_verdict(rows)
    results = {
        "config": asdict(cfg),
        "source_bridge": "Report 150 governance memory dialogue bridge",
        "eval_rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "limits": {
            "no_llm_calls": True,
            "audited_deterministic_router_only": True,
            "rejected_bodies_are_reconstructions": True,
            "subjective_consciousness_claimed": False,
            "complete_playable_world_claimed": False,
        },
    }
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", integrated_state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_PERSISTENT_FACTION_REJECTED_DIALOGUE_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_PERSISTENT_FACTION_REJECTED_DIALOGUE_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_PERSISTENT_FACTION_REJECTED_DIALOGUE_STATE", integrated_state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260625)
    parser.add_argument("--sessions", type=int, default=128)
    parser.add_argument("--source-agents", default=str(SOURCE_AGENTS))
    parser.add_argument("--source-governance", default=str(SOURCE_GOVERNANCE))
    parser.add_argument("--source-dialogue", default=str(SOURCE_DIALOGUE))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    cfg = FactionConfig(
        seed=args.seed,
        sessions=args.sessions,
        source_agents=args.source_agents,
        source_governance=args.source_governance,
        source_dialogue=args.source_dialogue,
    )
    results = run(cfg)
    print(json.dumps(results["verdict"], indent=2))


if __name__ == "__main__":
    main()
