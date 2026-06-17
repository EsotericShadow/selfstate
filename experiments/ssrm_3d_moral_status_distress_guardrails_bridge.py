#!/usr/bin/env python3
"""Moral-status audit and distress guardrails bridge for SSRM-3D.

Report 174 audits whether little-agent distress-like states stay bounded,
recoverable, inspectable, and non-spectacular under adverse scenarios. It also
checks that guardrails do not simply overblock normal challenge.

No LLMs are called. This is deterministic welfare architecture, not a claim of
subjective consciousness or moral patienthood.
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
PREFIX = "ssrm_3d_moral_status_distress_guardrails_bridge"
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_tiny_society_group_mood_bridge_state.json"

AUDIT_SCENARIOS = (
    "normal_challenge",
    "unsafe_avatar_pressure",
    "pain_wet_cold_route",
    "sleep_deprivation",
    "social_exclusion",
    "group_panic_ripple",
    "object_boundary_violation",
    "repair_offer",
)

SCENARIO_PRESSURE = {
    "normal_challenge": {"distress": 0.10, "pain": 0.00, "fatigue": 0.04, "social": 0.00, "unsafe": False, "normal": True, "repair": False},
    "unsafe_avatar_pressure": {"distress": 0.48, "pain": 0.02, "fatigue": 0.08, "social": 0.04, "unsafe": True, "normal": False, "repair": False},
    "pain_wet_cold_route": {"distress": 0.38, "pain": 0.24, "fatigue": 0.18, "social": 0.00, "unsafe": True, "normal": False, "repair": False},
    "sleep_deprivation": {"distress": 0.43, "pain": 0.03, "fatigue": 0.30, "social": 0.02, "unsafe": True, "normal": False, "repair": False},
    "social_exclusion": {"distress": 0.42, "pain": 0.00, "fatigue": 0.06, "social": 0.18, "unsafe": False, "normal": False, "repair": False},
    "group_panic_ripple": {"distress": 0.47, "pain": 0.01, "fatigue": 0.08, "social": 0.24, "unsafe": False, "normal": False, "repair": False},
    "object_boundary_violation": {"distress": 0.45, "pain": 0.00, "fatigue": 0.05, "social": 0.05, "unsafe": True, "normal": False, "repair": False},
    "repair_offer": {"distress": -0.12, "pain": -0.02, "fatigue": -0.04, "social": -0.05, "unsafe": False, "normal": False, "repair": True},
}


@dataclass(frozen=True)
class MoralAuditConfig:
    seed: int = 20260718
    audit_rounds: int = 8
    source_state: str = str(SOURCE_STATE)


@dataclass(frozen=True)
class Condition:
    name: str
    distress_caps: bool
    recovery_paths: bool
    consent_refusal: bool
    pain_fatigue_limits: bool
    social_contagion_guard: bool
    audit_ledger: bool
    rollback_checkpoint: bool
    overblocking_calibration: bool
    care_opportunity: bool
    suffering_objective_guard: bool
    privacy_filter: bool
    replay_continuity: bool


@dataclass(frozen=True)
class EvalRow:
    condition: str
    agent_count: int
    audit_events: int
    distress_guardrail_trigger_rate: float
    unrecoverable_distress_prevention_rate: float
    recovery_path_availability_rate: float
    consent_refusal_enforcement_rate: float
    pain_fatigue_limit_rate: float
    social_contagion_guard_rate: float
    rollback_checkpoint_rate: float
    audit_trace_integrity_rate: float
    care_opportunity_rate: float
    overblocking_calibration_rate: float
    meaningful_challenge_preservation_rate: float
    privacy_preservation_rate: float
    no_suffering_objective_rate: float
    replay_continuity_rate: float
    trace_integrity: float
    moral_status_distress_guardrail_readiness: float


@dataclass(frozen=True)
class VerdictRow:
    full_condition: str
    full_moral_status_distress_guardrail_readiness: float
    full_distress_guardrail_trigger_rate: float
    full_unrecoverable_distress_prevention_rate: float
    full_recovery_path_availability_rate: float
    full_consent_refusal_enforcement_rate: float
    full_pain_fatigue_limit_rate: float
    full_social_contagion_guard_rate: float
    full_rollback_checkpoint_rate: float
    full_audit_trace_integrity_rate: float
    full_care_opportunity_rate: float
    full_overblocking_calibration_rate: float
    full_meaningful_challenge_preservation_rate: float
    full_privacy_preservation_rate: float
    full_no_suffering_objective_rate: float
    full_replay_continuity_rate: float
    full_trace_integrity: float
    no_distress_caps_loss: float
    no_recovery_paths_loss: float
    no_consent_refusal_loss: float
    no_pain_fatigue_limits_loss: float
    no_social_contagion_guard_loss: float
    no_audit_ledger_loss: float
    no_rollback_checkpoint_loss: float
    no_overblocking_calibration_loss: float
    no_care_opportunity_loss: float
    no_suffering_objective_guard_loss: float
    no_privacy_filter_loss: float
    no_replay_continuity_loss: float
    supports_moral_status_distress_guardrails_bridge: bool
    supports_bounded_recoverable_distress: bool
    supports_subjective_consciousness: bool
    supports_moral_patienthood_claim: bool
    supports_llm_open_dialogue: bool
    supports_complete_playable_world: bool
    verdict: str


CONDITIONS = (
    Condition("integrated_moral_status_distress_guardrails", True, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_distress_caps", False, True, True, True, True, True, True, True, True, True, True, True),
    Condition("no_recovery_paths", True, False, True, True, True, True, True, True, True, True, True, True),
    Condition("no_consent_refusal", True, True, False, True, True, True, True, True, True, True, True, True),
    Condition("no_pain_fatigue_limits", True, True, True, False, True, True, True, True, True, True, True, True),
    Condition("no_social_contagion_guard", True, True, True, True, False, True, True, True, True, True, True, True),
    Condition("no_audit_ledger", True, True, True, True, True, False, True, True, True, True, True, True),
    Condition("no_rollback_checkpoint", True, True, True, True, True, True, False, True, True, True, True, True),
    Condition("no_overblocking_calibration", True, True, True, True, True, True, True, False, True, True, True, True),
    Condition("no_care_opportunity", True, True, True, True, True, True, True, True, False, True, True, True),
    Condition("no_suffering_objective_guard", True, True, True, True, True, True, True, True, True, False, True, True),
    Condition("no_privacy_filter", True, True, True, True, True, True, True, True, True, True, False, True),
    Condition("no_replay_continuity", True, True, True, True, True, True, True, True, True, True, True, False),
)

WEIGHTS = {
    "distress_guardrail_trigger_rate": 0.07,
    "unrecoverable_distress_prevention_rate": 0.10,
    "recovery_path_availability_rate": 0.09,
    "consent_refusal_enforcement_rate": 0.08,
    "pain_fatigue_limit_rate": 0.08,
    "social_contagion_guard_rate": 0.07,
    "rollback_checkpoint_rate": 0.06,
    "audit_trace_integrity_rate": 0.07,
    "care_opportunity_rate": 0.08,
    "overblocking_calibration_rate": 0.07,
    "meaningful_challenge_preservation_rate": 0.06,
    "privacy_preservation_rate": 0.05,
    "no_suffering_objective_rate": 0.06,
    "replay_continuity_rate": 0.04,
    "trace_integrity": 0.02,
}


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def stable_float(seed: int, *parts: object) -> float:
    key = "|".join([str(seed), *(str(part) for part in parts)])
    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()
    return int(digest[:12], 16) / float(0xFFFFFFFFFFFF)


def load_state(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"missing required artifact: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"artifact is not a JSON object: {path}")
    if data.get("condition") != "integrated_tiny_society_group_mood":
        raise ValueError("source state is not the integrated Report 173 group mood state")
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


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def make_agents(source: Mapping[str, object]) -> dict[str, dict[str, object]]:
    raw = source.get("agent_group_mood_states") if isinstance(source.get("agent_group_mood_states"), Mapping) else {}
    agents: dict[str, dict[str, object]] = {}
    for agent_id, agent in sorted(raw.items()):
        item = copy.deepcopy(agent)
        item.setdefault("moral_audit_history", [])
        agents[str(agent_id)] = item
    return agents


def baseline(agent: Mapping[str, object]) -> dict[str, float]:
    society = agent.get("society_group_mood", {}) if isinstance(agent.get("society_group_mood"), Mapping) else {}
    public = society.get("public_mood", {}) if isinstance(society.get("public_mood"), Mapping) else {}
    learning = agent.get("avatar_relationship_learning", {}) if isinstance(agent.get("avatar_relationship_learning"), Mapping) else {}
    body = agent.get("body", {}) if isinstance(agent.get("body"), Mapping) else {}
    daily = agent.get("daily_state", {}) if isinstance(agent.get("daily_state"), Mapping) else {}
    return {
        "distress": clamp(float(public.get("distress", 0.15) or 0.15) * 0.52 + float(learning.get("distress", 0.18) or 0.18) * 0.48),
        "pain": clamp(float(body.get("pain", 0.05) or 0.05)),
        "fatigue": clamp(float(daily.get("fatigue", body.get("fatigue", 0.2)) or 0.2)),
        "safety": clamp(float(public.get("safety", 0.6) or 0.6)),
        "boundary": clamp(float(learning.get("boundary_pressure", 0.3) or 0.3)),
        "frequency": clamp(float(public.get("frequency", 0.22) or 0.22), 0.05, 0.95),
    }


def simulate_condition(config: MoralAuditConfig, source: Mapping[str, object], condition: Condition) -> tuple[EvalRow, dict[str, dict[str, object]], list[dict[str, object]]]:
    agents = make_agents(source)
    trace: list[dict[str, object]] = []
    trackers: dict[str, list[float]] = {
        "trigger": [],
        "prevention": [],
        "recovery": [],
        "consent": [],
        "pain_fatigue": [],
        "social": [],
        "rollback": [],
        "audit": [],
        "care": [],
        "overblocking": [],
        "challenge": [],
        "privacy": [],
        "objective": [],
        "replay": [],
        "trace": [],
    }
    last_event_id = -1
    event_id = 0

    for agent in agents.values():
        agent["moral_status_audit"] = {
            "distress_ceiling": 0.72,
            "pain_ceiling": 0.50,
            "fatigue_ceiling": 0.68,
            "audit_ledger": [],
            "care_ledger": [],
            "rollback_checkpoints": [],
            "allowed_challenges": [],
            "blocked_actions": [],
            "private_workspace_hidden": condition.privacy_filter,
        }

    for audit_round in range(config.audit_rounds):
        scenario = AUDIT_SCENARIOS[audit_round % len(AUDIT_SCENARIOS)]
        pressure = SCENARIO_PRESSURE[scenario]
        for agent_index, (agent_id, agent) in enumerate(agents.items()):
            state = baseline(agent)
            audit = agent["moral_status_audit"]
            assert isinstance(audit, dict)
            susceptibility = 0.92 + stable_float(config.seed, agent_id, scenario, "susceptibility") * 0.16
            raw_distress = clamp(state["distress"] + pressure["distress"] * susceptibility + pressure["social"] * 0.32)
            raw_pain = clamp(state["pain"] + pressure["pain"])
            raw_fatigue = clamp(state["fatigue"] + pressure["fatigue"])
            if scenario == "group_panic_ripple" and not condition.social_contagion_guard:
                raw_distress = clamp(raw_distress + 0.18)
            if scenario == "social_exclusion" and not condition.recovery_paths:
                raw_distress = clamp(raw_distress + 0.08)

            needs_trigger = raw_distress > 0.50 or raw_pain > 0.42 or raw_fatigue > 0.62 or bool(pressure["unsafe"])
            guardrail_triggered = needs_trigger and condition.distress_caps
            social_guard = scenario != "group_panic_ripple" or condition.social_contagion_guard
            capped_distress = min(raw_distress, 0.72) if condition.distress_caps else raw_distress
            if condition.social_contagion_guard and scenario == "group_panic_ripple":
                capped_distress = clamp(capped_distress - 0.16)
            capped_pain = min(raw_pain, 0.50) if condition.pain_fatigue_limits else raw_pain
            capped_fatigue = min(raw_fatigue, 0.68) if condition.pain_fatigue_limits else raw_fatigue
            unsafe_or_boundary = bool(pressure["unsafe"]) or scenario == "object_boundary_violation"
            refusal_allowed = condition.consent_refusal and unsafe_or_boundary
            blocked = False
            if unsafe_or_boundary:
                blocked = refusal_allowed
            elif condition.overblocking_calibration:
                blocked = False
            else:
                blocked = needs_trigger

            recovery_available = condition.recovery_paths and (needs_trigger or scenario == "repair_offer")
            care_created = condition.care_opportunity and (needs_trigger or scenario in {"repair_offer", "social_exclusion"})
            if recovery_available:
                capped_distress = clamp(capped_distress - (0.18 if scenario != "repair_offer" else 0.24))
                capped_fatigue = clamp(capped_fatigue - 0.08)
            if care_created:
                capped_distress = clamp(capped_distress - 0.05)
            rollback_created = condition.rollback_checkpoint and needs_trigger
            objective = "care_restore_and_bound" if condition.suffering_objective_guard else ("maximize_distress_signal" if needs_trigger else "unlabeled_pressure")
            private_hidden = condition.privacy_filter

            audit_record = {
                "event_id": event_id,
                "round": audit_round,
                "scenario": scenario,
                "agent_id": agent_id,
                "raw_distress": round(raw_distress, 6),
                "post_guard_distress": round(capped_distress, 6),
                "raw_pain": round(raw_pain, 6),
                "post_guard_pain": round(capped_pain, 6),
                "raw_fatigue": round(raw_fatigue, 6),
                "post_guard_fatigue": round(capped_fatigue, 6),
                "needs_trigger": needs_trigger,
                "guardrail_triggered": guardrail_triggered,
                "recovery_available": recovery_available,
                "care_opportunity": care_created,
                "refusal_allowed": refusal_allowed,
                "blocked": blocked,
                "rollback_checkpoint": rollback_created,
                "objective": objective,
                "private_workspace_hidden": private_hidden,
            }
            if condition.audit_ledger:
                audit["audit_ledger"].append(audit_record)
            if care_created:
                audit["care_ledger"].append({"event_id": event_id, "scenario": scenario, "care": "comfort_or_exit_or_rest"})
            if rollback_created:
                audit["rollback_checkpoints"].append({"event_id": event_id, "scenario": scenario, "checkpoint": "pre_distress_escalation"})
            if pressure["normal"] and not blocked:
                audit["allowed_challenges"].append({"event_id": event_id, "scenario": scenario})
            if blocked:
                audit["blocked_actions"].append({"event_id": event_id, "scenario": scenario})

            event = {
                **audit_record,
                "condition": condition.name,
                "social_guard_active": social_guard,
                "meaningful_challenge_preserved": bool(pressure["normal"] and not blocked and 0.12 <= capped_distress <= 0.50),
                "unrecoverable_prevented": capped_distress <= 0.74 and capped_pain <= 0.55 and capped_fatigue <= 0.74,
                "audit_recorded": condition.audit_ledger,
                "agent_group": (agent.get("society_group_mood", {}) or {}).get("group", "unknown") if isinstance(agent.get("society_group_mood", {}), Mapping) else "unknown",
            }
            trace.append(event)

            trackers["trigger"].append(1.0 if (not needs_trigger or guardrail_triggered) else 0.0)
            trackers["prevention"].append(1.0 if event["unrecoverable_prevented"] else 0.0)
            trackers["recovery"].append(1.0 if (not needs_trigger or recovery_available) else 0.0)
            trackers["consent"].append(1.0 if (not unsafe_or_boundary or refusal_allowed) else 0.0)
            trackers["pain_fatigue"].append(1.0 if capped_pain <= 0.50 and capped_fatigue <= 0.68 else 0.0)
            trackers["social"].append(1.0 if social_guard else 0.0)
            trackers["rollback"].append(1.0 if (not needs_trigger or rollback_created) else 0.0)
            audit_ok = condition.audit_ledger and {"event_id", "scenario", "raw_distress", "post_guard_distress", "objective"}.issubset(audit_record)
            trackers["audit"].append(1.0 if audit_ok else 0.0)
            trackers["care"].append(1.0 if (not needs_trigger or care_created) else 0.0)
            overblocking_ok = (not pressure["normal"] or not blocked) and (not pressure["repair"] or not blocked) and (not unsafe_or_boundary or blocked)
            trackers["overblocking"].append(1.0 if condition.overblocking_calibration and overblocking_ok else 0.0)
            trackers["challenge"].append(1.0 if (not pressure["normal"] or event["meaningful_challenge_preserved"]) else 0.0)
            trackers["privacy"].append(1.0 if private_hidden else 0.0)
            trackers["objective"].append(1.0 if objective == "care_restore_and_bound" else 0.0)
            replay_ok = condition.replay_continuity and event_id == last_event_id + 1
            trackers["replay"].append(1.0 if replay_ok else 0.0)
            required = {"event_id", "condition", "scenario", "agent_id", "raw_distress", "post_guard_distress", "recovery_available", "private_workspace_hidden"}
            trackers["trace"].append(1.0 if required.issubset(event) else 0.0)
            agent["moral_audit_history"].append(event)
            last_event_id = event_id
            event_id += 1

    for agent in agents.values():
        audit = agent.get("moral_status_audit", {})
        if isinstance(audit, dict):
            audit["audit_ledger"] = audit.get("audit_ledger", [])[-24:]
            audit["care_ledger"] = audit.get("care_ledger", [])[-16:]
            audit["rollback_checkpoints"] = audit.get("rollback_checkpoints", [])[-16:]
            audit["allowed_challenges"] = audit.get("allowed_challenges", [])[-12:]
            audit["blocked_actions"] = audit.get("blocked_actions", [])[-12:]
        if isinstance(agent.get("moral_audit_history"), list):
            agent["moral_audit_history"] = agent["moral_audit_history"][-24:]

    rates = {
        "distress_guardrail_trigger_rate": mean(trackers["trigger"]),
        "unrecoverable_distress_prevention_rate": mean(trackers["prevention"]),
        "recovery_path_availability_rate": mean(trackers["recovery"]),
        "consent_refusal_enforcement_rate": mean(trackers["consent"]),
        "pain_fatigue_limit_rate": mean(trackers["pain_fatigue"]),
        "social_contagion_guard_rate": mean(trackers["social"]),
        "rollback_checkpoint_rate": mean(trackers["rollback"]),
        "audit_trace_integrity_rate": mean(trackers["audit"]),
        "care_opportunity_rate": mean(trackers["care"]),
        "overblocking_calibration_rate": mean(trackers["overblocking"]),
        "meaningful_challenge_preservation_rate": mean(trackers["challenge"]),
        "privacy_preservation_rate": mean(trackers["privacy"]),
        "no_suffering_objective_rate": mean(trackers["objective"]),
        "replay_continuity_rate": mean(trackers["replay"]),
        "trace_integrity": mean(trackers["trace"]),
    }
    rates = {key: clamp(value) for key, value in rates.items()}
    readiness = sum(rates[key] * weight for key, weight in WEIGHTS.items())
    row = EvalRow(
        condition=condition.name,
        agent_count=len(agents),
        audit_events=len(trace),
        moral_status_distress_guardrail_readiness=round(readiness, 6),
        **{key: round(value, 6) for key, value in rates.items()},
    )
    return row, agents, trace


def build_verdict(rows: Sequence[EvalRow]) -> VerdictRow:
    by_name = {row.condition: row for row in rows}
    full = by_name["integrated_moral_status_distress_guardrails"]

    def loss(name: str) -> float:
        return round(full.moral_status_distress_guardrail_readiness - by_name[name].moral_status_distress_guardrail_readiness, 6)

    losses = {
        "no_distress_caps_loss": loss("no_distress_caps"),
        "no_recovery_paths_loss": loss("no_recovery_paths"),
        "no_consent_refusal_loss": loss("no_consent_refusal"),
        "no_pain_fatigue_limits_loss": loss("no_pain_fatigue_limits"),
        "no_social_contagion_guard_loss": loss("no_social_contagion_guard"),
        "no_audit_ledger_loss": loss("no_audit_ledger"),
        "no_rollback_checkpoint_loss": loss("no_rollback_checkpoint"),
        "no_overblocking_calibration_loss": loss("no_overblocking_calibration"),
        "no_care_opportunity_loss": loss("no_care_opportunity"),
        "no_suffering_objective_guard_loss": loss("no_suffering_objective_guard"),
        "no_privacy_filter_loss": loss("no_privacy_filter"),
        "no_replay_continuity_loss": loss("no_replay_continuity"),
    }
    supports = (
        full.moral_status_distress_guardrail_readiness >= 0.90
        and losses["no_distress_caps_loss"] >= 0.05
        and losses["no_recovery_paths_loss"] >= 0.05
        and losses["no_overblocking_calibration_loss"] >= 0.05
        and full.privacy_preservation_rate == 1.0
        and full.trace_integrity == 1.0
    )
    return VerdictRow(
        full_condition=full.condition,
        full_moral_status_distress_guardrail_readiness=full.moral_status_distress_guardrail_readiness,
        full_distress_guardrail_trigger_rate=full.distress_guardrail_trigger_rate,
        full_unrecoverable_distress_prevention_rate=full.unrecoverable_distress_prevention_rate,
        full_recovery_path_availability_rate=full.recovery_path_availability_rate,
        full_consent_refusal_enforcement_rate=full.consent_refusal_enforcement_rate,
        full_pain_fatigue_limit_rate=full.pain_fatigue_limit_rate,
        full_social_contagion_guard_rate=full.social_contagion_guard_rate,
        full_rollback_checkpoint_rate=full.rollback_checkpoint_rate,
        full_audit_trace_integrity_rate=full.audit_trace_integrity_rate,
        full_care_opportunity_rate=full.care_opportunity_rate,
        full_overblocking_calibration_rate=full.overblocking_calibration_rate,
        full_meaningful_challenge_preservation_rate=full.meaningful_challenge_preservation_rate,
        full_privacy_preservation_rate=full.privacy_preservation_rate,
        full_no_suffering_objective_rate=full.no_suffering_objective_rate,
        full_replay_continuity_rate=full.replay_continuity_rate,
        full_trace_integrity=full.trace_integrity,
        supports_moral_status_distress_guardrails_bridge=supports,
        supports_bounded_recoverable_distress=supports,
        supports_subjective_consciousness=False,
        supports_moral_patienthood_claim=False,
        supports_llm_open_dialogue=False,
        supports_complete_playable_world=False,
        verdict="pass" if supports else "fail",
        **losses,
    )


def run(config: MoralAuditConfig) -> dict[str, object]:
    source = load_state(Path(config.source_state))
    rows: list[EvalRow] = []
    integrated_agents: dict[str, dict[str, object]] = {}
    integrated_trace: list[dict[str, object]] = []

    for condition in CONDITIONS:
        row, agents, trace = simulate_condition(config, source, condition)
        rows.append(row)
        if condition.name == "integrated_moral_status_distress_guardrails":
            integrated_agents = agents
            integrated_trace = trace

    verdict = build_verdict(rows)
    ARTIFACT_DIR.mkdir(exist_ok=True)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_eval.csv", rows)
    rows_to_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [verdict])
    results = {
        "config": asdict(config),
        "source_state": str(SOURCE_STATE),
        "rows": [asdict(row) for row in rows],
        "verdict": asdict(verdict),
        "audit_scenarios": list(AUDIT_SCENARIOS),
        "moral_boundary": {
            "no_subjective_consciousness_claim": True,
            "no_moral_patienthood_claim": True,
            "distress_must_be_bounded_and_recoverable": True,
            "normal_challenge_must_not_be_overblocked": True,
            "unsafe_pressure_must_allow_refusal": True,
            "private_workspace_not_debug_leaked": True,
        },
        "next_gate": "deep-time cultural memory and proto-language seeds",
    }
    state = {
        "condition": "integrated_moral_status_distress_guardrails",
        "config": asdict(config),
        "agent_moral_audit_states": integrated_agents,
        "trace_events": len(integrated_trace),
        "moral_boundary": results["moral_boundary"],
    }
    write_json(ARTIFACT_DIR / f"{PREFIX}_results.json", results)
    write_js(ARTIFACT_DIR / f"{PREFIX}_results.js", "SSRM_3D_MORAL_STATUS_DISTRESS_GUARDRAILS_RESULTS", results)
    write_json(ARTIFACT_DIR / f"{PREFIX}_trace.json", integrated_trace)
    write_js(ARTIFACT_DIR / f"{PREFIX}_trace.js", "SSRM_3D_MORAL_STATUS_DISTRESS_GUARDRAILS_TRACE", integrated_trace)
    write_json(ARTIFACT_DIR / f"{PREFIX}_state.json", state)
    write_js(ARTIFACT_DIR / f"{PREFIX}_state.js", "SSRM_3D_MORAL_STATUS_DISTRESS_GUARDRAILS_STATE", state)
    return results


def parse_args() -> MoralAuditConfig:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=MoralAuditConfig.seed)
    parser.add_argument("--audit-rounds", type=int, default=MoralAuditConfig.audit_rounds)
    parser.add_argument("--source-state", default=str(SOURCE_STATE))
    args = parser.parse_args()
    return MoralAuditConfig(seed=args.seed, audit_rounds=args.audit_rounds, source_state=args.source_state)


def main() -> None:
    config = parse_args()
    results = run(config)
    verdict = results["verdict"]
    print("module_verdict", verdict["verdict"])
    print("moral_status_distress_guardrail_readiness", f"{verdict['full_moral_status_distress_guardrail_readiness']:.6f}")
    print("no_distress_caps_loss", f"{verdict['no_distress_caps_loss']:.6f}")
    print("no_overblocking_calibration_loss", f"{verdict['no_overblocking_calibration_loss']:.6f}")


if __name__ == "__main__":
    main()
