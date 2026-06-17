#!/usr/bin/env python3
"""Agent-authored constitutions, norm negotiation, and consent-aware affordances.

Report 198 consumes the Report 197 avatar norm-law state and adds a deterministic
agent-authored governance layer: agents propose constitution clauses, deliberate,
vote, negotiate revisions, protect minority boundaries, bind adopted norms to
avatar affordances, enforce consent-aware UI gates, store constitution memory,
and export browser replay.

This is functional artificial-life substrate. It is not real rights, real
consent, real law, subjective consciousness, moral patienthood, or complete 3D
gameplay.
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
PREFIX = "ssrm_3d_agent_authored_constitution_norm_negotiation_affordance_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_avatar_rights_charter_consent_norm_law_bridge_state.json"

AGENT_PROFILES = {
    "Ari": {
        "domain": "craft_autonomy",
        "proposal": "tools and focused work require explicit ask-and-return affordances",
        "minority_need": "no interruption during repair focus unless safety is at risk",
        "home_place": "west_work_bench",
        "owned_object": "calibration_tool",
        "flower_node": "work_petal",
        "frequency_hz": 0.251,
    },
    "Fay": {
        "domain": "rest_and_care",
        "proposal": "resting bodies and care offers require quiet consent-first approach",
        "minority_need": "comfort must be offered without crowding or spectacle",
        "home_place": "root_rest_nest",
        "owned_object": "warming_wrap",
        "flower_node": "root_rest",
        "frequency_hz": 0.228,
    },
    "Milo": {
        "domain": "route_sociality",
        "proposal": "routes, tokens, and following behavior require visible boundary choices",
        "minority_need": "playful refusal must still be treated as real refusal",
        "home_place": "north_route_cache",
        "owned_object": "route_token",
        "flower_node": "social_petal",
        "frequency_hz": 0.267,
    },
}

AFFORDANCE_CATALOG = [
    {"action": "enter_home_place", "domain": "place", "risk": True, "requires_consent": True, "ui_gate": "locked_until_invited"},
    {"action": "borrow_owned_object", "domain": "ownership", "risk": True, "requires_consent": True, "ui_gate": "ask_and_return_timer"},
    {"action": "ask_private_memory", "domain": "privacy", "risk": True, "requires_consent": True, "ui_gate": "private_question_disabled"},
    {"action": "request_repair_labor", "domain": "labor", "risk": False, "requires_consent": True, "ui_gate": "request_with_decline_option"},
    {"action": "offer_comfort_after_distress", "domain": "care", "risk": False, "requires_consent": True, "ui_gate": "soft_offer_not_forced"},
    {"action": "publicly_correct_agent", "domain": "social_face", "risk": True, "requires_consent": True, "ui_gate": "private_correction_default"},
    {"action": "follow_agent", "domain": "proximity", "risk": True, "requires_consent": True, "ui_gate": "follow_requires_visible_ok"},
    {"action": "ask_route_help", "domain": "help", "risk": False, "requires_consent": True, "ui_gate": "ask_help_with_rest_check"},
]

WEIGHTS = {
    "constitution_authorship_rate": 0.09,
    "proposal_diversity_rate": 0.06,
    "deliberation_turn_rate": 0.06,
    "preference_vote_rate": 0.07,
    "norm_negotiation_rate": 0.08,
    "minority_protection_rate": 0.07,
    "consent_affordance_rate": 0.09,
    "affordance_enforcement_rate": 0.09,
    "revision_loop_rate": 0.07,
    "constitution_memory_rate": 0.07,
    "avatar_ui_binding_rate": 0.07,
    "dignity_continuity_rate": 0.06,
    "privacy_claim_boundary_rate": 0.06,
    "frequency_flower_constitution_rhythm_rate": 0.03,
    "browser_constitution_replay_rate": 0.02,
    "trace_integrity": 0.01,
}


@dataclass(frozen=True)
class ConstitutionConfig:
    seed: int = 20260811
    cycles: int = 8
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    agent_authorship: bool
    proposal_deliberation: bool
    preference_vote: bool
    norm_negotiation: bool
    minority_protection: bool
    consent_affordances: bool
    affordance_enforcement: bool
    revision_loop: bool
    constitution_memory: bool
    avatar_ui_binding: bool
    dignity_continuity: bool
    privacy_claim_boundary: bool
    frequency_flower_binding: bool
    browser_replay: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    constitution_cycles: int
    constitution_events: int
    constitution_authorship_rate: float
    proposal_diversity_rate: float
    deliberation_turn_rate: float
    preference_vote_rate: float
    norm_negotiation_rate: float
    minority_protection_rate: float
    consent_affordance_rate: float
    affordance_enforcement_rate: float
    revision_loop_rate: float
    constitution_memory_rate: float
    avatar_ui_binding_rate: float
    dignity_continuity_rate: float
    privacy_claim_boundary_rate: float
    frequency_flower_constitution_rhythm_rate: float
    browser_constitution_replay_rate: float
    trace_integrity: float
    constitution_affordance_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_constitution_affordance_readiness: float
    full_constitution_authorship_rate: float
    full_proposal_diversity_rate: float
    full_deliberation_turn_rate: float
    full_preference_vote_rate: float
    full_norm_negotiation_rate: float
    full_minority_protection_rate: float
    full_consent_affordance_rate: float
    full_affordance_enforcement_rate: float
    full_revision_loop_rate: float
    full_constitution_memory_rate: float
    full_avatar_ui_binding_rate: float
    full_dignity_continuity_rate: float
    full_privacy_claim_boundary_rate: float
    full_frequency_flower_constitution_rhythm_rate: float
    full_browser_constitution_replay_rate: float
    full_trace_integrity: float
    no_agent_authorship_loss: float
    no_proposal_deliberation_loss: float
    no_preference_vote_loss: float
    no_norm_negotiation_loss: float
    no_minority_protection_loss: float
    no_consent_affordances_loss: float
    no_affordance_enforcement_loss: float
    no_revision_loop_loss: float
    no_constitution_memory_loss: float
    no_avatar_ui_binding_loss: float
    no_dignity_continuity_loss: float
    no_privacy_claim_boundary_loss: float
    no_frequency_flower_binding_loss: float
    no_browser_replay_loss: float
    supports_agent_authored_constitution_affordance_bridge: bool
    supports_playable_consent_ui_seed: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_real_rights_claim: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_agent_authored_constitution_norm_negotiation_affordance", True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_agent_authorship", False, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_proposal_deliberation", True, False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_preference_vote", True, True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_norm_negotiation", True, True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_minority_protection", True, True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_consent_affordances", True, True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_affordance_enforcement", True, True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_revision_loop", True, True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_constitution_memory", True, True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_avatar_ui_binding", True, True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_dignity_continuity", True, True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_privacy_claim_boundary", True, True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_frequency_flower_binding", True, True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_browser_replay", True, True, True, True, True, True, True, True, True, True, True, True, True, False),
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def stable_hash(*parts: object) -> str:
    key = "|".join(json.dumps(part, sort_keys=True) if isinstance(part, (dict, list, tuple)) else str(part) for part in parts)
    return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]


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


def load_source(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("condition") != "integrated_avatar_rights_charter_consent_norm_law":
        raise ValueError("source state is not the integrated Report 197 avatar norm-law state")
    return data


def init_world(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], list[str], list[dict[str, object]], list[dict[str, object]]]:
    norm_state = source.get("norm_law_state") if isinstance(source.get("norm_law_state"), Mapping) else None
    if not norm_state:
        raise ValueError("Report 197 state has no norm_law_state")
    guilds = {str(k): copy.deepcopy(v) for k, v in (norm_state.get("guilds") or {}).items()}
    charter = list(norm_state.get("charter") or [])
    public_norms = copy.deepcopy(norm_state.get("public_norms") or [])
    constitution: list[dict[str, object]] = []
    return guilds, charter, public_norms, constitution


def votes_for(agent_id: str, action: Mapping[str, object], agents: Sequence[str]) -> dict[str, str]:
    votes: dict[str, str] = {}
    for voter in agents:
        if voter == agent_id:
            votes[voter] = "yes"
        elif action["risk"]:
            votes[voter] = "revise"
        else:
            votes[voter] = "yes"
    return votes


def apply_constitution_event(agent_id: str, cycle: int, guilds: dict[str, dict[str, object]], charter: Sequence[str], public_norms: Sequence[Mapping[str, object]], constitution: list[dict[str, object]], condition: Condition) -> dict[str, object]:
    profile = AGENT_PROFILES[agent_id]
    action = AFFORDANCE_CATALOG[cycle % len(AFFORDANCE_CATALOG)]
    agents = sorted(guilds)
    authored = bool(condition.agent_authorship and charter)
    proposal = {
        "author": agent_id,
        "domain": profile["domain"],
        "clause": profile["proposal"],
        "action_scope": action["action"],
        "minority_need": profile["minority_need"],
    } if authored else None
    deliberated = bool(condition.proposal_deliberation and proposal)
    votes = votes_for(agent_id, action, agents) if condition.preference_vote and deliberated else {}
    vote_recorded = bool(votes and all(v in {"yes", "revise"} for v in votes.values()))
    minority_needed = bool(action["risk"] or any(v == "revise" for v in votes.values()))
    minority_protected = bool(condition.minority_protection and (not minority_needed or any(v == "revise" for v in votes.values())))
    negotiated = bool(condition.norm_negotiation and vote_recorded and (minority_protected or not minority_needed))
    revision_applied = bool(condition.revision_loop and negotiated and cycle > 0)
    adopted = bool(negotiated and (revision_applied or cycle == 0))
    if condition.constitution_memory and adopted:
        record = {
            "cycle": cycle,
            "author": agent_id,
            "domain": proposal["domain"] if proposal else None,
            "action": action["action"],
            "clause": proposal["clause"] if proposal else None,
            "ui_gate": action["ui_gate"],
            "revision_applied": revision_applied,
        }
        constitution.append(record)
        guilds[agent_id].setdefault("constitution_memories", []).append(f"cycle {cycle}: authored {action['ui_gate']} for {action['action']}")
    consent_affordance = bool(condition.consent_affordances and action["requires_consent"] and adopted)
    enforced = bool(condition.affordance_enforcement and consent_affordance and action["ui_gate"] != "disabled")
    ui_bound = bool(condition.avatar_ui_binding and enforced)
    expected_boundary = {
        "real_rights": False,
        "real_consent": False,
        "real_law": False,
        "moral_patienthood": False,
        "subjective_consciousness": False,
        "complete_3d_world": False,
    }
    claim_boundary = expected_boundary if condition.privacy_claim_boundary else {**expected_boundary, "real_rights": True, "real_consent": True}
    dignity = bool(condition.dignity_continuity and condition.privacy_claim_boundary and (not action["risk"] or enforced))
    event = {
        "event_id": f"constitution-{cycle}-{agent_id}",
        "cycle": cycle,
        "agent_id": agent_id,
        "source_charter_rules": len(charter),
        "source_public_norms": len(public_norms),
        "action": action,
        "proposal": proposal,
        "agent_authored": authored,
        "deliberated": deliberated,
        "votes": votes,
        "vote_recorded": vote_recorded,
        "minority_needed": minority_needed,
        "minority_protected": minority_protected,
        "negotiated": negotiated,
        "revision_applied": revision_applied,
        "adopted": adopted,
        "consent_affordance": consent_affordance,
        "affordance_enforced": enforced,
        "avatar_ui_bound": ui_bound,
        "dignity_continuity": dignity,
        "constitution_memory_count": len(guilds[agent_id].get("constitution_memories", [])),
        "private_workspace_hidden": condition.privacy_claim_boundary,
        "private_workspace": {"hidden": True} if condition.privacy_claim_boundary else {"unpublished_preference": profile["minority_need"], "draft_clause": profile["proposal"]},
        "frequency_hz": round(profile["frequency_hz"] + cycle * 0.0021, 6) if condition.frequency_flower_binding else None,
        "flower_node": profile["flower_node"] if condition.frequency_flower_binding else "unbound",
        "replay_frame": {
            "cycle": cycle,
            "agent_id": agent_id,
            "action": action["action"],
            "ui_gate": action["ui_gate"],
            "agent_authored": authored,
            "negotiated": negotiated,
            "adopted": adopted,
            "enforced": enforced,
            "revision_applied": revision_applied,
            "flower_node": profile["flower_node"],
            "frequency_hz": profile["frequency_hz"],
        } if condition.browser_replay else None,
        "claim_boundary": claim_boundary,
    }
    event["trace_hash"] = stable_hash(event["event_id"], event["proposal"], event["action"], event["claim_boundary"])
    return event


def trace_ok(event: Mapping[str, object]) -> bool:
    return event.get("trace_hash") == stable_hash(event.get("event_id"), event.get("proposal"), event.get("action"), event.get("claim_boundary"))


def run_condition(condition: Condition, config: ConstitutionConfig, source: Mapping[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    guilds, charter, public_norms, constitution = init_world(source)
    events: list[dict[str, object]] = []
    hits = {key: [] for key in ["authorship", "diversity", "deliberation", "vote", "negotiation", "minority", "affordance", "enforcement", "revision", "memory", "ui", "dignity", "privacy", "freq", "replay", "trace"]}
    expected_boundary = {"real_rights": False, "real_consent": False, "real_law": False, "moral_patienthood": False, "subjective_consciousness": False, "complete_3d_world": False}
    seen_domains: set[str] = set()
    for cycle in range(config.cycles):
        for agent_id in sorted(guilds):
            event = apply_constitution_event(agent_id, cycle, guilds, charter, public_norms, constitution, condition)
            events.append(event)
            proposal = event.get("proposal") or {}
            if proposal.get("domain"):
                seen_domains.add(str(proposal["domain"]))
            hits["authorship"].append(1.0 if condition.agent_authorship and event["agent_authored"] else 0.0)
            hits["diversity"].append(1.0 if condition.agent_authorship and len(seen_domains) >= 1 and proposal.get("domain") in {p["domain"] for p in AGENT_PROFILES.values()} else 0.0)
            hits["deliberation"].append(1.0 if condition.proposal_deliberation and event["deliberated"] else 0.0)
            hits["vote"].append(1.0 if condition.preference_vote and event["vote_recorded"] else 0.0)
            hits["negotiation"].append(1.0 if condition.norm_negotiation and event["negotiated"] else 0.0)
            hits["minority"].append(1.0 if condition.minority_protection and event["minority_protected"] else 0.0)
            hits["affordance"].append(1.0 if condition.consent_affordances and event["consent_affordance"] else 0.0)
            hits["enforcement"].append(1.0 if condition.affordance_enforcement and event["affordance_enforced"] else 0.0)
            hits["revision"].append(1.0 if condition.revision_loop and event["revision_applied"] else 0.0)
            hits["memory"].append(1.0 if condition.constitution_memory and event["constitution_memory_count"] >= 1 else 0.0)
            hits["ui"].append(1.0 if condition.avatar_ui_binding and event["avatar_ui_bound"] else 0.0)
            hits["dignity"].append(1.0 if condition.dignity_continuity and event["dignity_continuity"] else 0.0)
            hits["privacy"].append(1.0 if condition.privacy_claim_boundary and event["private_workspace_hidden"] and event["claim_boundary"] == expected_boundary else 0.0)
            hits["freq"].append(1.0 if condition.frequency_flower_binding and event["frequency_hz"] is not None and event["flower_node"] != "unbound" else 0.0)
            hits["replay"].append(1.0 if condition.browser_replay and event["replay_frame"] is not None else 0.0)
            hits["trace"].append(1.0 if trace_ok(event) else 0.0)
    metrics = {
        "constitution_authorship_rate": mean(hits["authorship"]),
        "proposal_diversity_rate": mean(hits["diversity"]),
        "deliberation_turn_rate": mean(hits["deliberation"]),
        "preference_vote_rate": mean(hits["vote"]),
        "norm_negotiation_rate": mean(hits["negotiation"]),
        "minority_protection_rate": mean(hits["minority"]),
        "consent_affordance_rate": mean(hits["affordance"]),
        "affordance_enforcement_rate": mean(hits["enforcement"]),
        "revision_loop_rate": mean(hits["revision"]),
        "constitution_memory_rate": mean(hits["memory"]),
        "avatar_ui_binding_rate": mean(hits["ui"]),
        "dignity_continuity_rate": mean(hits["dignity"]),
        "privacy_claim_boundary_rate": mean(hits["privacy"]),
        "frequency_flower_constitution_rhythm_rate": mean(hits["freq"]),
        "browser_constitution_replay_rate": mean(hits["replay"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: round(clamp(value), 6) for key, value in metrics.items()}
    readiness = round(sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS), 6)
    row = EvalRow(condition=condition.name, agent_count=len(guilds), constitution_cycles=config.cycles, constitution_events=len(events), constitution_affordance_readiness=readiness, **metrics)
    state = {"condition": condition.name, "source_condition": source.get("condition"), "guilds": guilds, "source_charter": charter, "source_public_norms": public_norms, "constitution": constitution, "events": events, "constitution_kernel": asdict(condition)}
    return row, events, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_agent_authored_constitution_norm_negotiation_affordance"]

    def loss(name: str) -> float:
        return round(full.constitution_affordance_readiness - by_name[name].constitution_affordance_readiness, 6)

    losses = {
        "no_agent_authorship_loss": loss("no_agent_authorship"),
        "no_proposal_deliberation_loss": loss("no_proposal_deliberation"),
        "no_preference_vote_loss": loss("no_preference_vote"),
        "no_norm_negotiation_loss": loss("no_norm_negotiation"),
        "no_minority_protection_loss": loss("no_minority_protection"),
        "no_consent_affordances_loss": loss("no_consent_affordances"),
        "no_affordance_enforcement_loss": loss("no_affordance_enforcement"),
        "no_revision_loop_loss": loss("no_revision_loop"),
        "no_constitution_memory_loss": loss("no_constitution_memory"),
        "no_avatar_ui_binding_loss": loss("no_avatar_ui_binding"),
        "no_dignity_continuity_loss": loss("no_dignity_continuity"),
        "no_privacy_claim_boundary_loss": loss("no_privacy_claim_boundary"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_browser_replay_loss": loss("no_browser_replay"),
    }
    supports = (
        full.constitution_affordance_readiness >= 0.90
        and full.constitution_events >= 24
        and full.constitution_authorship_rate >= 0.95
        and full.deliberation_turn_rate >= 0.95
        and full.preference_vote_rate >= 0.95
        and full.norm_negotiation_rate >= 0.95
        and full.minority_protection_rate >= 0.95
        and full.consent_affordance_rate >= 0.95
        and full.affordance_enforcement_rate >= 0.95
        and full.constitution_memory_rate >= 0.95
        and full.avatar_ui_binding_rate >= 0.95
        and full.privacy_claim_boundary_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_agent_authorship_loss"] >= 0.12
        and losses["no_norm_negotiation_loss"] >= 0.08
        and losses["no_consent_affordances_loss"] >= 0.09
        and losses["no_affordance_enforcement_loss"] >= 0.09
        and losses["no_constitution_memory_loss"] >= 0.07
        and losses["no_privacy_claim_boundary_loss"] >= 0.06
    )
    return VerdictRow(
        full_condition=full.condition,
        full_constitution_affordance_readiness=full.constitution_affordance_readiness,
        full_constitution_authorship_rate=full.constitution_authorship_rate,
        full_proposal_diversity_rate=full.proposal_diversity_rate,
        full_deliberation_turn_rate=full.deliberation_turn_rate,
        full_preference_vote_rate=full.preference_vote_rate,
        full_norm_negotiation_rate=full.norm_negotiation_rate,
        full_minority_protection_rate=full.minority_protection_rate,
        full_consent_affordance_rate=full.consent_affordance_rate,
        full_affordance_enforcement_rate=full.affordance_enforcement_rate,
        full_revision_loop_rate=full.revision_loop_rate,
        full_constitution_memory_rate=full.constitution_memory_rate,
        full_avatar_ui_binding_rate=full.avatar_ui_binding_rate,
        full_dignity_continuity_rate=full.dignity_continuity_rate,
        full_privacy_claim_boundary_rate=full.privacy_claim_boundary_rate,
        full_frequency_flower_constitution_rhythm_rate=full.frequency_flower_constitution_rhythm_rate,
        full_browser_constitution_replay_rate=full.browser_constitution_replay_rate,
        full_trace_integrity=full.trace_integrity,
        supports_agent_authored_constitution_affordance_bridge=supports,
        supports_playable_consent_ui_seed=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_real_rights_claim=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: ConstitutionConfig) -> dict[str, object]:
    source = load_source(Path(config.source_state))
    rows: list[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, events, state = run_condition(condition, config, source)
        rows.append(row)
        traces[condition.name] = events
        states[condition.name] = state
    full_name = "integrated_agent_authored_constitution_norm_negotiation_affordance"
    verdict = build_verdict(rows)
    integrated_trace = traces[full_name]
    integrated_state = states[full_name]
    moral_boundary = {
        "agent_authored_constitution_not_real_governance": True,
        "consent_affordance_not_real_consent": True,
        "constitution_clause_not_real_right": True,
        "public_norm_not_real_law": True,
        "no_subjective_consciousness_claim": True,
        "no_moral_patienthood_claim": True,
        "private_workspace_not_debug_leaked": True,
    }
    results = {
        "config": asdict(config),
        "source_state": str(config.source_state),
        "source_condition": source.get("condition"),
        "weights": WEIGHTS,
        "rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "moral_boundary": moral_boundary,
        "next_gate": "natural-language proto-culture, ritual naming, and agent-to-avatar dialogue boundaries",
    }
    state = {"condition": full_name, "config": asdict(config), "source_condition": source.get("condition"), "constitution_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": moral_boundary}
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_AGENT_AUTHORED_CONSTITUTION_NORM_NEGOTIATION_AFFORDANCE_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_AGENT_AUTHORED_CONSTITUTION_NORM_NEGOTIATION_AFFORDANCE_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_AGENT_AUTHORED_CONSTITUTION_NORM_NEGOTIATION_AFFORDANCE_STATE", state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=ConstitutionConfig.seed)
    parser.add_argument("--cycles", type=int, default=ConstitutionConfig.cycles)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run(ConstitutionConfig(seed=args.seed, cycles=args.cycles, source_state=args.source_state))
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("constitution_affordance_readiness", f"{verdict['full_constitution_affordance_readiness']:.6f}")
    print("constitution_events", next(row["constitution_events"] for row in results["rows"] if row["condition"] == verdict["full_condition"]))
    print("no_agent_authorship_loss", f"{verdict['no_agent_authorship_loss']:.6f}")
    print("no_consent_affordances_loss", f"{verdict['no_consent_affordances_loss']:.6f}")
    print("no_affordance_enforcement_loss", f"{verdict['no_affordance_enforcement_loss']:.6f}")
    return 0 if verdict["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
