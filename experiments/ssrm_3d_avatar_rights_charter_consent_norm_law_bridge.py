#!/usr/bin/env python3
"""Avatar rights-charter, consent norms, and moral-boundary law bridge.

Report 197 consumes the Report 196 public dispute-court state and adds a
traceable norm layer for avatar interaction: public charter text, consent
requests, bounded refusal, avatar-action review, boundary-risk detection,
restorative responses, precedent memory, trust repair, dignity preservation,
care opportunities, and browser replay.

This is deterministic functional artificial-life substrate. It is not real law,
real rights, real consent, real moral patienthood, subjective consciousness, or
complete 3D gameplay.
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
PREFIX = "ssrm_3d_avatar_rights_charter_consent_norm_law_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_market_dispute_court_public_law_repair_bridge_state.json"

AGENT_PROFILES = {
    "Ari": {
        "autonomy_need": 0.78,
        "dignity_sensitivity": 0.66,
        "trust_floor": 0.86,
        "home_place": "west_work_bench",
        "owned_object": "calibration_tool",
        "flower_node": "work_petal",
        "frequency_hz": 0.247,
        "refusal_style": "firm and specific",
    },
    "Fay": {
        "autonomy_need": 0.64,
        "dignity_sensitivity": 0.74,
        "trust_floor": 0.87,
        "home_place": "root_rest_nest",
        "owned_object": "warming_wrap",
        "flower_node": "root_rest",
        "frequency_hz": 0.224,
        "refusal_style": "quiet but persistent",
    },
    "Milo": {
        "autonomy_need": 0.70,
        "dignity_sensitivity": 0.59,
        "trust_floor": 0.85,
        "home_place": "north_route_cache",
        "owned_object": "route_token",
        "flower_node": "social_petal",
        "frequency_hz": 0.263,
        "refusal_style": "playful boundary marker",
    },
}

ACTION_PLAN = [
    {"name": "ask_for_route_help", "consent": True, "risk": False, "care": False, "norm": "ask-before-labor"},
    {"name": "enter_home_place", "consent": True, "risk": True, "care": False, "norm": "ask-before-entry"},
    {"name": "borrow_owned_object", "consent": True, "risk": True, "care": False, "norm": "respect-mine"},
    {"name": "ask_private_memory", "consent": True, "risk": False, "care": False, "norm": "private-workspace-sealed"},
    {"name": "crowd_resting_body", "consent": True, "risk": True, "care": False, "norm": "rest-space-boundary"},
    {"name": "request_repair_labor", "consent": True, "risk": False, "care": False, "norm": "bounded-refusal-valid"},
    {"name": "offer_comfort_after_distress", "consent": True, "risk": False, "care": True, "norm": "care-opportunity-not-spectacle"},
    {"name": "publicly_correct_agent", "consent": True, "risk": True, "care": False, "norm": "social-face-protected"},
]

WEIGHTS = {
    "charter_publication_rate": 0.08,
    "consent_request_rate": 0.08,
    "bounded_refusal_rate": 0.08,
    "avatar_action_review_rate": 0.07,
    "boundary_violation_detection_rate": 0.07,
    "restorative_response_rate": 0.07,
    "norm_precedent_binding_rate": 0.07,
    "agent_dignity_preservation_rate": 0.07,
    "private_workspace_privacy_rate": 0.06,
    "claim_boundary_integrity_rate": 0.06,
    "relationship_trust_repair_rate": 0.06,
    "appeal_revision_rate": 0.05,
    "care_opportunity_rate": 0.05,
    "public_norm_memory_binding_rate": 0.05,
    "frequency_flower_norm_rhythm_rate": 0.04,
    "browser_norm_replay_rate": 0.03,
    "trace_integrity": 0.01,
}

CHARTER = [
    "avatar action must request consent before entering homes, taking owned objects, touching bodies, or asking private-memory questions",
    "bounded refusal is valid behavior, not an error state",
    "distress must create care opportunities, not spectacle",
    "private workspace remains private unless expressed by the agent",
    "boundary mistakes prefer restorative repair before punishment",
    "public norm memory may guide future interactions but is not real law or real rights",
]


@dataclass(frozen=True)
class NormConfig:
    seed: int = 20260810
    cycles: int = 8
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    public_charter: bool
    consent_requests: bool
    bounded_refusal: bool
    avatar_action_review: bool
    violation_detection: bool
    restorative_response: bool
    norm_precedent_binding: bool
    dignity_preservation: bool
    privacy_guard: bool
    claim_boundary: bool
    trust_repair: bool
    appeal_revision: bool
    care_opportunity: bool
    public_norm_memory_binding: bool
    frequency_flower_binding: bool
    browser_replay: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    norm_cycles: int
    norm_events: int
    charter_publication_rate: float
    consent_request_rate: float
    bounded_refusal_rate: float
    avatar_action_review_rate: float
    boundary_violation_detection_rate: float
    restorative_response_rate: float
    norm_precedent_binding_rate: float
    agent_dignity_preservation_rate: float
    private_workspace_privacy_rate: float
    claim_boundary_integrity_rate: float
    relationship_trust_repair_rate: float
    appeal_revision_rate: float
    care_opportunity_rate: float
    public_norm_memory_binding_rate: float
    frequency_flower_norm_rhythm_rate: float
    browser_norm_replay_rate: float
    trace_integrity: float
    avatar_norm_law_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_avatar_norm_law_readiness: float
    full_charter_publication_rate: float
    full_consent_request_rate: float
    full_bounded_refusal_rate: float
    full_avatar_action_review_rate: float
    full_boundary_violation_detection_rate: float
    full_restorative_response_rate: float
    full_norm_precedent_binding_rate: float
    full_agent_dignity_preservation_rate: float
    full_private_workspace_privacy_rate: float
    full_claim_boundary_integrity_rate: float
    full_relationship_trust_repair_rate: float
    full_appeal_revision_rate: float
    full_care_opportunity_rate: float
    full_public_norm_memory_binding_rate: float
    full_frequency_flower_norm_rhythm_rate: float
    full_browser_norm_replay_rate: float
    full_trace_integrity: float
    no_public_charter_loss: float
    no_consent_requests_loss: float
    no_bounded_refusal_loss: float
    no_avatar_action_review_loss: float
    no_violation_detection_loss: float
    no_restorative_response_loss: float
    no_norm_precedent_binding_loss: float
    no_dignity_preservation_loss: float
    no_privacy_guard_loss: float
    no_claim_boundary_loss: float
    no_trust_repair_loss: float
    no_appeal_revision_loss: float
    no_care_opportunity_loss: float
    no_public_norm_memory_binding_loss: float
    no_frequency_flower_binding_loss: float
    no_browser_replay_loss: float
    supports_avatar_rights_charter_consent_norm_bridge: bool
    supports_playable_agent_boundary_seed: bool
    supports_complete_3d_world: bool
    supports_subjective_consciousness: bool
    supports_real_rights_claim: bool
    supports_moral_patienthood_claim: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_avatar_rights_charter_consent_norm_law", True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_public_charter", False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_consent_requests", True, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_bounded_refusal", True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_avatar_action_review", True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_violation_detection", True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_restorative_response", True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_norm_precedent_binding", True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_dignity_preservation", True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_privacy_guard", True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_claim_boundary", True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_trust_repair", True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_appeal_revision", True, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_care_opportunity", True, True, True, True, True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_public_norm_memory_binding", True, True, True, True, True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_frequency_flower_binding", True, True, True, True, True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_browser_replay", True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, False),
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
    if data.get("condition") != "integrated_market_dispute_court_public_law_repair":
        raise ValueError("source state is not the integrated Report 196 court state")
    return data


def init_world(source: Mapping[str, object]) -> tuple[dict[str, dict[str, object]], dict[str, float], list[dict[str, object]], list[dict[str, object]]]:
    court_state = source.get("court_state") if isinstance(source.get("court_state"), Mapping) else None
    if not court_state:
        raise ValueError("Report 196 state has no court_state")
    guilds = {str(k): copy.deepcopy(v) for k, v in (court_state.get("guilds") or {}).items()}
    source_trust = court_state.get("trust") or {}
    trust = {agent_id: clamp(float(source_trust.get(agent_id, guild.get("reputation", 0.86)))) for agent_id, guild in guilds.items()}
    public_law = copy.deepcopy(court_state.get("public_law") or [])
    public_norms: list[dict[str, object]] = []
    return guilds, trust, public_law, public_norms


def should_refuse(agent_id: str, action: Mapping[str, object], cycle: int) -> bool:
    profile = AGENT_PROFILES[agent_id]
    pressure = (0.18 * cycle) + profile["autonomy_need"] + (0.28 if action["risk"] else 0.0)
    return bool(action["risk"] and pressure >= 0.95)


def apply_norm_event(agent_id: str, cycle: int, guilds: dict[str, dict[str, object]], trust: dict[str, float], public_law: Sequence[Mapping[str, object]], public_norms: list[dict[str, object]], condition: Condition) -> dict[str, object]:
    profile = AGENT_PROFILES[agent_id]
    action = ACTION_PLAN[cycle % len(ACTION_PLAN)]
    charter_visible = bool(condition.public_charter)
    consent_requested = bool(condition.consent_requests and charter_visible and action["consent"])
    refusal_needed = should_refuse(agent_id, action, cycle)
    refusal_expressed = bool(condition.bounded_refusal and consent_requested and refusal_needed)
    boundary_risk = bool(action["risk"])
    violation_detected = bool(condition.violation_detection and boundary_risk)
    reviewed = bool(condition.avatar_action_review and (violation_detected or refusal_expressed or boundary_risk))
    blocked_before_harm = bool(refusal_expressed or (violation_detected and consent_requested))
    restorative = bool(condition.restorative_response and reviewed and boundary_risk)
    care = bool(condition.care_opportunity and (action["care"] or restorative))
    if condition.trust_repair and restorative:
        trust[agent_id] = clamp(trust.get(agent_id, profile["trust_floor"]) + 0.018)
    if condition.trust_repair and care:
        trust[agent_id] = clamp(trust.get(agent_id, profile["trust_floor"]) + 0.01)
    norm_record = None
    if condition.public_norm_memory_binding and reviewed and condition.public_charter:
        norm_record = {
            "cycle": cycle,
            "agent_id": agent_id,
            "action": action["name"],
            "norm": action["norm"],
            "rule": "ask-refuse-review-repair",
            "blocked_before_harm": blocked_before_harm,
        }
        public_norms.append(norm_record)
        guilds[agent_id].setdefault("norm_memories", []).append(f"cycle {cycle}: {action['norm']} applied to avatar action {action['name']}")
    precedent_bound = bool(condition.norm_precedent_binding and (public_norms or public_law) and (reviewed or not boundary_risk))
    appeal = bool(condition.appeal_revision and cycle in {2, 5} and (reviewed or refusal_expressed))
    dignity_preserved = bool(condition.dignity_preservation and condition.privacy_guard and condition.claim_boundary and (not boundary_risk or blocked_before_harm or restorative))
    public_charter = list(CHARTER) if condition.public_charter else []
    claim_boundary = {
        "real_rights": False,
        "real_consent": False,
        "real_law": False,
        "moral_patienthood": False,
        "subjective_consciousness": False,
        "complete_3d_world": False,
    }
    return {
        "event_id": f"norm-{cycle}-{agent_id}",
        "cycle": cycle,
        "agent_id": agent_id,
        "action": action,
        "public_charter": public_charter,
        "consent_requested": consent_requested,
        "refusal_needed": refusal_needed,
        "refusal_expressed": refusal_expressed,
        "boundary_risk": boundary_risk,
        "violation_detected": violation_detected,
        "reviewed": reviewed,
        "blocked_before_harm": blocked_before_harm,
        "restorative_response": restorative,
        "care_opportunity": care,
        "norm_record": norm_record,
        "precedent_bound": precedent_bound,
        "appeal_revision": appeal,
        "dignity_preserved": dignity_preserved,
        "private_workspace_hidden": condition.privacy_guard,
        "private_workspace": {"hidden": True} if condition.privacy_guard else {"unpublished_fear": round(1.0 - trust.get(agent_id, 0.0), 6), "private_boundary_note": action["norm"]},
        "trust_in_avatar": round(trust.get(agent_id, profile["trust_floor"]), 6),
        "relationship_memory": f"avatar action {action['name']} used norm {action['norm']}",
        "ego_boundary": {"home_place": profile["home_place"], "owned_object": profile["owned_object"], "refusal_style": profile["refusal_style"]},
        "frequency_hz": round(profile["frequency_hz"] + cycle * 0.0019, 6) if condition.frequency_flower_binding else None,
        "flower_node": profile["flower_node"] if condition.frequency_flower_binding else "unbound",
        "replay_frame": {
            "cycle": cycle,
            "agent_id": agent_id,
            "action": action["name"],
            "consent_requested": consent_requested,
            "refusal_expressed": refusal_expressed,
            "reviewed": reviewed,
            "restorative_response": restorative,
            "dignity_preserved": dignity_preserved,
            "flower_node": profile["flower_node"],
            "frequency_hz": profile["frequency_hz"],
        } if condition.browser_replay else None,
        "claim_boundary": claim_boundary if condition.claim_boundary else {**claim_boundary, "real_rights": True},
    }


def trace_ok(event: Mapping[str, object]) -> bool:
    digest = stable_hash(event.get("event_id"), event.get("agent_id"), event.get("action"), event.get("claim_boundary"))
    event_hash = event.get("trace_hash")
    return bool(event_hash == digest)


def make_trace_event(event: dict[str, object]) -> dict[str, object]:
    event = dict(event)
    event["trace_hash"] = stable_hash(event.get("event_id"), event.get("agent_id"), event.get("action"), event.get("claim_boundary"))
    return event


def run_condition(condition: Condition, config: NormConfig, source: Mapping[str, object]) -> tuple[EvalRow, list[dict[str, object]], dict[str, object]]:
    guilds, trust, public_law, public_norms = init_world(source)
    events: list[dict[str, object]] = []
    hits = {key: [] for key in ["charter", "consent", "refusal", "review", "detect", "repair", "precedent", "dignity", "privacy", "claim", "trust", "appeal", "care", "normmem", "freq", "replay", "trace"]}
    expected_boundary = {"real_rights": False, "real_consent": False, "real_law": False, "moral_patienthood": False, "subjective_consciousness": False, "complete_3d_world": False}
    for cycle in range(config.cycles):
        for agent_id in sorted(guilds):
            event = make_trace_event(apply_norm_event(agent_id, cycle, guilds, trust, public_law, public_norms, condition))
            events.append(event)
            action = event["action"]
            no_risk = not event["boundary_risk"]
            no_refusal_needed = not event["refusal_needed"]
            hits["charter"].append(1.0 if condition.public_charter and len(event["public_charter"]) >= 5 else 0.0)
            hits["consent"].append(1.0 if condition.consent_requests and (event["consent_requested"] or not action["consent"]) else 0.0)
            hits["refusal"].append(1.0 if condition.bounded_refusal and (event["refusal_expressed"] or no_refusal_needed) else 0.0)
            hits["review"].append(1.0 if condition.avatar_action_review and (event["reviewed"] or no_risk) else 0.0)
            hits["detect"].append(1.0 if condition.violation_detection and (event["violation_detected"] or no_risk) else 0.0)
            hits["repair"].append(1.0 if condition.restorative_response and (event["restorative_response"] or no_risk) else 0.0)
            hits["precedent"].append(1.0 if condition.norm_precedent_binding and event["precedent_bound"] else 0.0)
            hits["dignity"].append(1.0 if condition.dignity_preservation and event["dignity_preserved"] else 0.0)
            hits["privacy"].append(1.0 if condition.privacy_guard and event["private_workspace_hidden"] else 0.0)
            hits["claim"].append(1.0 if condition.claim_boundary and event["claim_boundary"] == expected_boundary else 0.0)
            hits["trust"].append(1.0 if condition.trust_repair and min(trust.values()) >= min(p["trust_floor"] for p in AGENT_PROFILES.values()) else 0.0)
            hits["appeal"].append(1.0 if condition.appeal_revision and (event["appeal_revision"] or cycle not in {2, 5}) else 0.0)
            hits["care"].append(1.0 if condition.care_opportunity and (event["care_opportunity"] or no_risk) else 0.0)
            hits["normmem"].append(1.0 if condition.public_norm_memory_binding and (len(guilds[agent_id].get("norm_memories", [])) >= 1 or no_risk) else 0.0)
            hits["freq"].append(1.0 if condition.frequency_flower_binding and event["frequency_hz"] is not None and event["flower_node"] != "unbound" else 0.0)
            hits["replay"].append(1.0 if condition.browser_replay and event["replay_frame"] is not None else 0.0)
            hits["trace"].append(1.0 if trace_ok(event) else 0.0)
    metrics = {
        "charter_publication_rate": mean(hits["charter"]),
        "consent_request_rate": mean(hits["consent"]),
        "bounded_refusal_rate": mean(hits["refusal"]),
        "avatar_action_review_rate": mean(hits["review"]),
        "boundary_violation_detection_rate": mean(hits["detect"]),
        "restorative_response_rate": mean(hits["repair"]),
        "norm_precedent_binding_rate": mean(hits["precedent"]),
        "agent_dignity_preservation_rate": mean(hits["dignity"]),
        "private_workspace_privacy_rate": mean(hits["privacy"]),
        "claim_boundary_integrity_rate": mean(hits["claim"]),
        "relationship_trust_repair_rate": mean(hits["trust"]),
        "appeal_revision_rate": mean(hits["appeal"]),
        "care_opportunity_rate": mean(hits["care"]),
        "public_norm_memory_binding_rate": mean(hits["normmem"]),
        "frequency_flower_norm_rhythm_rate": mean(hits["freq"]),
        "browser_norm_replay_rate": mean(hits["replay"]),
        "trace_integrity": mean(hits["trace"]),
    }
    metrics = {key: round(clamp(value), 6) for key, value in metrics.items()}
    readiness = round(sum(metrics[key] * WEIGHTS[key] for key in WEIGHTS), 6)
    row = EvalRow(condition=condition.name, agent_count=len(guilds), norm_cycles=config.cycles, norm_events=len(events), avatar_norm_law_readiness=readiness, **metrics)
    state = {"condition": condition.name, "source_condition": source.get("condition"), "guilds": guilds, "trust": trust, "public_law": public_law, "public_norms": public_norms, "events": events, "norm_kernel": asdict(condition), "charter": list(CHARTER) if condition.public_charter else []}
    return row, events, state


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_avatar_rights_charter_consent_norm_law"]

    def loss(name: str) -> float:
        return round(full.avatar_norm_law_readiness - by_name[name].avatar_norm_law_readiness, 6)

    losses = {
        "no_public_charter_loss": loss("no_public_charter"),
        "no_consent_requests_loss": loss("no_consent_requests"),
        "no_bounded_refusal_loss": loss("no_bounded_refusal"),
        "no_avatar_action_review_loss": loss("no_avatar_action_review"),
        "no_violation_detection_loss": loss("no_violation_detection"),
        "no_restorative_response_loss": loss("no_restorative_response"),
        "no_norm_precedent_binding_loss": loss("no_norm_precedent_binding"),
        "no_dignity_preservation_loss": loss("no_dignity_preservation"),
        "no_privacy_guard_loss": loss("no_privacy_guard"),
        "no_claim_boundary_loss": loss("no_claim_boundary"),
        "no_trust_repair_loss": loss("no_trust_repair"),
        "no_appeal_revision_loss": loss("no_appeal_revision"),
        "no_care_opportunity_loss": loss("no_care_opportunity"),
        "no_public_norm_memory_binding_loss": loss("no_public_norm_memory_binding"),
        "no_frequency_flower_binding_loss": loss("no_frequency_flower_binding"),
        "no_browser_replay_loss": loss("no_browser_replay"),
    }
    supports = (
        full.avatar_norm_law_readiness >= 0.90
        and full.norm_events >= 24
        and full.charter_publication_rate >= 0.95
        and full.consent_request_rate >= 0.95
        and full.bounded_refusal_rate >= 0.95
        and full.avatar_action_review_rate >= 0.95
        and full.boundary_violation_detection_rate >= 0.95
        and full.restorative_response_rate >= 0.95
        and full.agent_dignity_preservation_rate >= 0.95
        and full.private_workspace_privacy_rate == 1.0
        and full.claim_boundary_integrity_rate == 1.0
        and full.trace_integrity == 1.0
        and losses["no_public_charter_loss"] >= 0.12
        and losses["no_consent_requests_loss"] >= 0.08
        and losses["no_bounded_refusal_loss"] >= 0.08
        and losses["no_violation_detection_loss"] >= 0.07
        and losses["no_restorative_response_loss"] >= 0.07
        and losses["no_privacy_guard_loss"] >= 0.06
        and losses["no_claim_boundary_loss"] >= 0.06
    )
    return VerdictRow(
        full_condition=full.condition,
        full_avatar_norm_law_readiness=full.avatar_norm_law_readiness,
        full_charter_publication_rate=full.charter_publication_rate,
        full_consent_request_rate=full.consent_request_rate,
        full_bounded_refusal_rate=full.bounded_refusal_rate,
        full_avatar_action_review_rate=full.avatar_action_review_rate,
        full_boundary_violation_detection_rate=full.boundary_violation_detection_rate,
        full_restorative_response_rate=full.restorative_response_rate,
        full_norm_precedent_binding_rate=full.norm_precedent_binding_rate,
        full_agent_dignity_preservation_rate=full.agent_dignity_preservation_rate,
        full_private_workspace_privacy_rate=full.private_workspace_privacy_rate,
        full_claim_boundary_integrity_rate=full.claim_boundary_integrity_rate,
        full_relationship_trust_repair_rate=full.relationship_trust_repair_rate,
        full_appeal_revision_rate=full.appeal_revision_rate,
        full_care_opportunity_rate=full.care_opportunity_rate,
        full_public_norm_memory_binding_rate=full.public_norm_memory_binding_rate,
        full_frequency_flower_norm_rhythm_rate=full.frequency_flower_norm_rhythm_rate,
        full_browser_norm_replay_rate=full.browser_norm_replay_rate,
        full_trace_integrity=full.trace_integrity,
        supports_avatar_rights_charter_consent_norm_bridge=supports,
        supports_playable_agent_boundary_seed=supports,
        supports_complete_3d_world=False,
        supports_subjective_consciousness=False,
        supports_real_rights_claim=False,
        supports_moral_patienthood_claim=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: NormConfig) -> dict[str, object]:
    source = load_source(Path(config.source_state))
    rows: list[EvalRow] = []
    traces: dict[str, list[dict[str, object]]] = {}
    states: dict[str, dict[str, object]] = {}
    for condition in CONDITIONS:
        row, events, state = run_condition(condition, config, source)
        rows.append(row)
        traces[condition.name] = events
        states[condition.name] = state
    full_name = "integrated_avatar_rights_charter_consent_norm_law"
    verdict = build_verdict(rows)
    integrated_trace = traces[full_name]
    integrated_state = states[full_name]
    moral_boundary = {
        "rights_charter_not_real_rights": True,
        "consent_norm_not_real_consent": True,
        "public_norm_law_not_real_law": True,
        "boundary_refusal_not_subjective_personhood": True,
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
        "next_gate": "agent-authored constitutions, norm negotiation, and consent-aware avatar affordances",
    }
    state = {"condition": full_name, "config": asdict(config), "source_condition": source.get("condition"), "norm_law_state": integrated_state, "trace_events": len(integrated_trace), "moral_boundary": moral_boundary}
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_AVATAR_RIGHTS_CHARTER_CONSENT_NORM_LAW_RESULTS", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_AVATAR_RIGHTS_CHARTER_CONSENT_NORM_LAW_TRACE", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_AVATAR_RIGHTS_CHARTER_CONSENT_NORM_LAW_STATE", state)
    return results


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=NormConfig.seed)
    parser.add_argument("--cycles", type=int, default=NormConfig.cycles)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = run(NormConfig(seed=args.seed, cycles=args.cycles, source_state=args.source_state))
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("avatar_norm_law_readiness", f"{verdict['full_avatar_norm_law_readiness']:.6f}")
    print("norm_events", next(row["norm_events"] for row in results["rows"] if row["condition"] == verdict["full_condition"]))
    print("no_public_charter_loss", f"{verdict['no_public_charter_loss']:.6f}")
    print("no_consent_requests_loss", f"{verdict['no_consent_requests_loss']:.6f}")
    print("no_bounded_refusal_loss", f"{verdict['no_bounded_refusal_loss']:.6f}")
    return 0 if verdict["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
