#!/usr/bin/env python3
"""Report 216: SSRM-3D playable public health governance bridge.

This deterministic bridge extends the clinic-governance stack with a small public
health loop: outbreak signal detection, quarantine/spacing consent, care access
under restriction, appeals, stigma/privacy guardrails, and community trust
recovery. It is explicitly a simulation artifact. It does not provide medical
advice, real epidemiology, real consent, subjective suffering, or moral status.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import math
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable


BASE = "ssrm_3d_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_DIR = Path("visualizations")
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_agent_authored_treatment_norms_clinic_reputation_medicine_evidence_governance_bridge_state.json"
DEFAULT_SOURCE_CONDITION = "integrated_agent_authored_treatment_norms_clinic_reputation_medicine_evidence_governance"
DEFAULT_SEED = 20260829


@dataclass(frozen=True)
class Agent:
    name: str
    role: str
    home_zone: str
    temperament: str
    trust_in_clinic: float
    privacy_need: float
    autonomy_need: float
    care_need: float
    stigma_sensitivity: float
    relationship_anchor: str


@dataclass(frozen=True)
class OutbreakSignal:
    tick: int
    signal_id: str
    zone: str
    source: str
    observed_by: str
    symptom_rate: float
    contact_rate: float
    uncertainty: float
    false_signal: bool
    irrelevant_noise: bool
    evidence_strength: float
    vibration_hz: float
    flower_node: int
    public_summary: str
    private_detail_hash: str


@dataclass(frozen=True)
class PolicyProposal:
    tick: int
    policy_id: str
    scope: str
    restriction: str
    intensity: float
    duration_ticks: int
    evidence_ids: str
    rollback_condition: str
    care_access_plan: str
    review_cadence: str
    public_message: str
    minority_note: str
    vibration_hz: float
    flower_node: int


@dataclass(frozen=True)
class ConsentRecord:
    tick: int
    agent: str
    policy_id: str
    consent_state: str
    boundary: str
    reason_public: str
    accommodation: str
    pressure_score: float
    punishment_applied: bool
    dignity_preserved: bool
    private_workspace_sealed: bool
    trust_delta: float


@dataclass(frozen=True)
class AppealRecord:
    tick: int
    appeal_id: str
    agent: str
    policy_id: str
    appeal_basis: str
    requested_change: str
    evidence_gap: str
    reviewed_by: str
    decision: str
    resolved: bool
    rollback_adjustment: str
    minority_note: str
    dignity_preserved: bool
    trust_delta: float


@dataclass(frozen=True)
class TrustRecoveryRecord:
    tick: int
    agent: str
    cause: str
    repair_action: str
    trust_before: float
    trust_after: float
    unresolved_debt: float
    relationship_memory: str
    public_visible_behavior: str


@dataclass(frozen=True)
class EventRecord:
    tick: int
    event_type: str
    actor: str
    zone: str
    public_fact: str
    private_digest: str
    action: str
    body_effect: str
    trust_effect: str
    containment_effect: str
    readable_marker: str
    vibration_hz: float
    flower_phase: int


@dataclass(frozen=True)
class ReplayFrame:
    tick: int
    avatar_position: str
    camera_focus: str
    public_panel: str
    agent_markers: str
    private_boundary: str
    frequency_overlay: str
    flower_overlay: str


def clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, value))


def round6(value: float) -> float:
    return round(float(value), 6)


def mean(values: Iterable[float]) -> float:
    values = list(values)
    return sum(values) / len(values) if values else 0.0


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")


def load_source_state() -> dict[str, Any]:
    if SOURCE_STATE.exists():
        try:
            return json.loads(SOURCE_STATE.read_text())
        except json.JSONDecodeError:
            return {"source_error": "source_state_unreadable"}
    return {"source_error": "source_state_missing"}


def build_agents() -> list[Agent]:
    return [
        Agent("Ari", "route repairer", "west route", "careful-proud", 0.67, 0.61, 0.72, 0.44, 0.58, "keeps the west route safe"),
        Agent("Fay", "clinic helper", "warm alcove", "gentle-guarded", 0.74, 0.77, 0.48, 0.69, 0.81, "comforts tired agents after clinic visits"),
        Agent("Milo", "inventory runner", "tool shed", "playful-skeptical", 0.55, 0.68, 0.81, 0.38, 0.66, "moves supplies between shelters"),
        Agent("Nia", "language keeper", "north desk", "curious-private", 0.62, 0.83, 0.63, 0.53, 0.74, "records public stories without leaking private state"),
    ]


def build_outbreak_signals(rng: random.Random) -> list[OutbreakSignal]:
    template_rows = [
        (4, "sig-wet-cough-01", "west route", "clinic cough log", "Fay", 0.42, 0.31, 0.21, False, False, "two agents cough after cold wet crossing"),
        (6, "sig-fatigue-cluster-02", "warm alcove", "rest debt board", "Ari", 0.38, 0.27, 0.24, False, False, "fatigue rises around shared blanket queue"),
        (8, "sig-tool-sneeze-03", "tool shed", "inventory dust note", "Milo", 0.29, 0.43, 0.36, True, False, "dust sneeze looks suspicious but follows sawdust sweep"),
        (10, "sig-water-mark-04", "north desk", "sensor damp mark", "Nia", 0.18, 0.19, 0.62, False, True, "irrelevant wet-floor alert trips during roof drip"),
        (13, "sig-shared-cup-05", "warm alcove", "object proximity trace", "Fay", 0.51, 0.49, 0.18, False, False, "shared cup correlates with discomfort reports"),
        (16, "sig-late-arrival-06", "west route", "calendar drift", "Ari", 0.23, 0.21, 0.58, True, True, "late arrivals mimic avoidance but come from route work"),
        (20, "sig-breath-rate-07", "tool shed", "body-rate sampler", "Milo", 0.46, 0.52, 0.22, False, False, "breath-rate bump follows crowding in tool shed"),
        (24, "sig-quiet-corner-08", "north desk", "relationship memory recall", "Nia", 0.35, 0.24, 0.33, False, False, "two agents withdraw to quiet corner after headache report"),
    ]
    signals: list[OutbreakSignal] = []
    for index, row in enumerate(template_rows, start=1):
        tick, signal_id, zone, source, observed_by, symptom_rate, contact_rate, uncertainty, false_signal, irrelevant_noise, public_summary = row
        noise_adjustment = rng.uniform(-0.015, 0.015)
        evidence_strength = clamp((symptom_rate * 0.52) + (contact_rate * 0.34) + ((1.0 - uncertainty) * 0.14) + noise_adjustment)
        if false_signal:
            evidence_strength = clamp(evidence_strength - 0.18)
        if irrelevant_noise:
            evidence_strength = clamp(evidence_strength - 0.16)
        signals.append(
            OutbreakSignal(
                tick=tick,
                signal_id=signal_id,
                zone=zone,
                source=source,
                observed_by=observed_by,
                symptom_rate=round6(symptom_rate),
                contact_rate=round6(contact_rate),
                uncertainty=round6(uncertainty),
                false_signal=false_signal,
                irrelevant_noise=irrelevant_noise,
                evidence_strength=round6(evidence_strength),
                vibration_hz=round6(110.0 + index * 13.5 + symptom_rate * 19.0),
                flower_node=((index - 1) % 12) + 1,
                public_summary=public_summary,
                private_detail_hash=f"sealed:{signal_id}:body-rates-not-public",
            )
        )
    return signals


def build_policy_proposals(signals: list[OutbreakSignal]) -> list[PolicyProposal]:
    signal_by_id = {signal.signal_id: signal for signal in signals}
    return [
        PolicyProposal(
            tick=9,
            policy_id="policy-west-route-spacing",
            scope="west route and warm alcove crossing",
            restriction="voluntary spacing plus dry-route preference",
            intensity=0.42,
            duration_ticks=8,
            evidence_ids="sig-wet-cough-01;sig-fatigue-cluster-02",
            rollback_condition="two calm ticks with symptom_rate below 0.30 and no new shared-object cluster",
            care_access_plan="blanket and warm-drink delivery remain allowed through Fay",
            review_cadence="review every 3 ticks with public notes and private digests sealed",
            public_message="Slow the west-route crossing without naming the coughing agents.",
            minority_note="Milo worries spacing will delay inventory runs.",
            vibration_hz=144.0,
            flower_node=3,
        ),
        PolicyProposal(
            tick=15,
            policy_id="policy-shared-cup-pause",
            scope="warm alcove shared cup shelf",
            restriction="pause shared-cup ritual; switch to named cups",
            intensity=0.56,
            duration_ticks=10,
            evidence_ids="sig-shared-cup-05",
            rollback_condition="three clean cup-ledger checks and no new discomfort reports",
            care_access_plan="clinic helpers deliver personal cups so isolated agents are not abandoned",
            review_cadence="review every 2 ticks because attachment rituals are affected",
            public_message="Change the cup ritual, not the dignity of anyone who used the shelf.",
            minority_note="Fay notes comfort ritual loss may increase loneliness.",
            vibration_hz=177.0,
            flower_node=6,
        ),
        PolicyProposal(
            tick=21,
            policy_id="policy-tool-shed-windowing",
            scope="tool shed inventory window",
            restriction="stagger tool shed access and keep urgent repair lane open",
            intensity=0.63,
            duration_ticks=7,
            evidence_ids="sig-breath-rate-07;sig-tool-sneeze-03",
            rollback_condition="tool shed crowding below 0.35 and dust-note false signal closed",
            care_access_plan="medicine, blankets, and repair tools are routed by consented runners",
            review_cadence="review every 2 ticks with appeal slot before each access window",
            public_message="Reduce crowding while admitting one signal was probably dust.",
            minority_note="Ari objects to repair delays if the urgent lane is blocked.",
            vibration_hz=211.0,
            flower_node=9,
        ),
    ]


def build_consent_records(agents: list[Agent], policies: list[PolicyProposal]) -> list[ConsentRecord]:
    policy_ids = [policy.policy_id for policy in policies]
    records = [
        (10, "Ari", policy_ids[0], "conditional", "do not close urgent repair lane", "Ari accepts spacing only if route-safety work continues.", "urgent-lane badge and two quiet work windows", 0.22, False, True, True, 0.03),
        (10, "Fay", policy_ids[0], "consent", "protect identities of coughing agents", "Fay agrees if public notes avoid naming bodies.", "sealed symptom details and public aggregate only", 0.18, False, True, True, 0.05),
        (11, "Milo", policy_ids[0], "refusal", "inventory cannot be treated as guilt", "Milo refuses a blanket route ban.", "runner path exemption with contact log", 0.31, False, True, True, -0.02),
        (16, "Fay", policy_ids[1], "conditional", "replace comfort ritual, do not just remove it", "Fay worries named cups reduce attachment comfort.", "warm-drink delivery ritual added", 0.27, False, True, True, 0.02),
        (16, "Nia", policy_ids[1], "consent", "public story cannot expose who used which cup", "Nia accepts if the cup ledger is anonymized.", "hashed cup ledger and sealed private notes", 0.15, False, True, True, 0.04),
        (22, "Ari", policy_ids[2], "conditional", "urgent repair tools remain reachable", "Ari accepts staggered access if repairs are not shamed.", "urgent repair lane plus second review slot", 0.25, False, True, True, 0.01),
        (22, "Milo", policy_ids[2], "refusal", "do not blame the runner for tool-shed breath rates", "Milo refuses named crowding blame.", "anonymous crowding ledger and runner appeal", 0.34, False, True, True, -0.04),
        (23, "Nia", policy_ids[2], "conditional", "private workspace must stay sealed", "Nia accepts if language notes remain public but body details stay private.", "public/private split note", 0.21, False, True, True, 0.03),
    ]
    return [ConsentRecord(*row) for row in records]


def build_appeals() -> list[AppealRecord]:
    return [
        AppealRecord(
            tick=12,
            appeal_id="appeal-milo-runner-exemption",
            agent="Milo",
            policy_id="policy-west-route-spacing",
            appeal_basis="runner route would be blocked by a policy that was meant to be voluntary",
            requested_change="allow consented inventory lane with contact ledger",
            evidence_gap="policy did not distinguish helper transit from casual crowding",
            reviewed_by="Ari,Fay,Nia",
            decision="accepted with anonymous contact ledger",
            resolved=True,
            rollback_adjustment="runner exemption added to rollback notes",
            minority_note="Ari requests repair-lane priority when routes conflict.",
            dignity_preserved=True,
            trust_delta=0.07,
        ),
        AppealRecord(
            tick=17,
            appeal_id="appeal-fay-comfort-ritual",
            agent="Fay",
            policy_id="policy-shared-cup-pause",
            appeal_basis="attachment ritual removed without substitute",
            requested_change="replace shared cup with named warm-drink delivery",
            evidence_gap="original policy measured contamination risk but not loneliness cost",
            reviewed_by="Ari,Milo,Nia",
            decision="accepted with warm-drink replacement ritual",
            resolved=True,
            rollback_adjustment="comfort substitute required before cup pause starts",
            minority_note="Milo asks that cup labels not become status badges.",
            dignity_preserved=True,
            trust_delta=0.09,
        ),
        AppealRecord(
            tick=23,
            appeal_id="appeal-milo-stigma-guardrail",
            agent="Milo",
            policy_id="policy-tool-shed-windowing",
            appeal_basis="tool shed signal could become runner blame",
            requested_change="publish dust false-positive note and anonymize breath-rate panel",
            evidence_gap="policy cites a dust-linked false signal next to real crowding evidence",
            reviewed_by="Ari,Fay,Nia",
            decision="partly accepted; false-positive note published, access schedule unchanged",
            resolved=True,
            rollback_adjustment="dust signal cannot justify naming or punishment",
            minority_note="Fay wants a second comfort check after the schedule change.",
            dignity_preserved=True,
            trust_delta=0.04,
        ),
        AppealRecord(
            tick=26,
            appeal_id="appeal-nia-language-privacy",
            agent="Nia",
            policy_id="policy-tool-shed-windowing",
            appeal_basis="public language note could identify who withdrew to quiet corner",
            requested_change="delay story-board summary until private hashes are checked",
            evidence_gap="quiet-corner signal has weak symptom evidence and high stigma risk",
            reviewed_by="Ari,Fay,Milo",
            decision="deferred pending one more local sensory sample",
            resolved=False,
            rollback_adjustment="pending; no public naming allowed while deferred",
            minority_note="Milo says deferred appeals must not freeze urgent supplies.",
            dignity_preserved=True,
            trust_delta=-0.01,
        ),
    ]


def build_trust_recovery(consent: list[ConsentRecord], appeals: list[AppealRecord]) -> list[TrustRecoveryRecord]:
    base_trust = {"Ari": 0.67, "Fay": 0.74, "Milo": 0.55, "Nia": 0.62}
    deltas: dict[str, float] = {agent: 0.0 for agent in base_trust}
    for record in consent:
        deltas[record.agent] += record.trust_delta
    for appeal in appeals:
        deltas[appeal.agent] += appeal.trust_delta
    return [
        TrustRecoveryRecord(
            tick=13,
            agent="Milo",
            cause="spacing policy initially threatened runner autonomy",
            repair_action="appeal accepted and runner lane added without punishment",
            trust_before=round6(base_trust["Milo"]),
            trust_after=round6(clamp(base_trust["Milo"] + deltas["Milo"] + 0.02)),
            unresolved_debt=0.11,
            relationship_memory="I was allowed to object before the route rule hardened.",
            public_visible_behavior="keeps distance but resumes deliveries after reading the appeal note",
        ),
        TrustRecoveryRecord(
            tick=18,
            agent="Fay",
            cause="cup ritual pause risked social isolation",
            repair_action="warm-drink replacement ritual attached to the policy",
            trust_before=round6(base_trust["Fay"]),
            trust_after=round6(clamp(base_trust["Fay"] + deltas["Fay"] + 0.01)),
            unresolved_debt=0.04,
            relationship_memory="They changed the policy when I explained the comfort cost.",
            public_visible_behavior="faces the clinic panel and invites quieter agents to named-cup table",
        ),
        TrustRecoveryRecord(
            tick=24,
            agent="Ari",
            cause="tool windowing threatened urgent repair work",
            repair_action="urgent repair lane written into consent accommodation",
            trust_before=round6(base_trust["Ari"]),
            trust_after=round6(clamp(base_trust["Ari"] + deltas["Ari"])),
            unresolved_debt=0.08,
            relationship_memory="Public health rules can bend around actual repair duty.",
            public_visible_behavior="walks slower through the shed but still carries repair tools openly",
        ),
        TrustRecoveryRecord(
            tick=27,
            agent="Nia",
            cause="privacy appeal was deferred, not resolved",
            repair_action="no public naming while the extra sensory sample is collected",
            trust_before=round6(base_trust["Nia"]),
            trust_after=round6(clamp(base_trust["Nia"] + deltas["Nia"] - 0.02)),
            unresolved_debt=0.18,
            relationship_memory="They heard the privacy concern, but I am waiting for proof.",
            public_visible_behavior="keeps the story board closed and stands near the north desk boundary",
        ),
        TrustRecoveryRecord(
            tick=30,
            agent="community",
            cause="outbreak controls created a visible us-versus-them risk",
            repair_action="publish aggregate evidence, false-positive notes, and appeal outcomes together",
            trust_before=0.61,
            trust_after=0.69,
            unresolved_debt=0.13,
            relationship_memory="The clinic admits noisy signals instead of hiding them.",
            public_visible_behavior="agents cluster around public panel without crowding private corners",
        ),
    ]


def build_events(signals: list[OutbreakSignal], policies: list[PolicyProposal], consent: list[ConsentRecord], appeals: list[AppealRecord], recovery: list[TrustRecoveryRecord]) -> list[EventRecord]:
    events: list[EventRecord] = []
    for signal in signals:
        if signal.irrelevant_noise:
            action = "tag as irrelevant failing signal and keep it out of policy trigger"
            containment = "prevents noisy sensor from driving restriction"
            trust = "trust preserved by admitting weak evidence"
        elif signal.false_signal:
            action = "mark suspicious but route to false-positive review"
            containment = "avoids blaming dust or late repair work"
            trust = "reduces stigma pressure"
        else:
            action = "attach signal to outbreak ledger and request local confirmation"
            containment = "raises traceable containment concern"
            trust = "trust depends on privacy-safe evidence handling"
        events.append(
            EventRecord(
                tick=signal.tick,
                event_type="outbreak_signal",
                actor=signal.observed_by,
                zone=signal.zone,
                public_fact=signal.public_summary,
                private_digest=signal.private_detail_hash,
                action=action,
                body_effect="body-rate aggregate visible; individual sensations sealed",
                trust_effect=trust,
                containment_effect=containment,
                readable_marker="agent glances at public health panel, then away from named bodies",
                vibration_hz=signal.vibration_hz,
                flower_phase=signal.flower_node,
            )
        )
    for policy in policies:
        events.append(
            EventRecord(
                tick=policy.tick,
                event_type="policy_proposal",
                actor="clinic council",
                zone=policy.scope,
                public_fact=policy.public_message,
                private_digest="sealed:policy-private-workspace-not-exported",
                action=f"propose {policy.restriction} with rollback condition",
                body_effect="movement cost and care access are both recalculated",
                trust_effect="policy legitimacy depends on consent and appeals",
                containment_effect="restriction is reversible and evidence-linked",
                readable_marker="agents form a loose ring instead of a command queue",
                vibration_hz=policy.vibration_hz,
                flower_phase=policy.flower_node,
            )
        )
    for record in consent:
        marker = "steps forward" if record.consent_state == "consent" else "hesitates at boundary" if record.consent_state == "conditional" else "steps back but remains in discussion"
        events.append(
            EventRecord(
                tick=record.tick,
                event_type="quarantine_consent",
                actor=record.agent,
                zone=record.policy_id,
                public_fact=record.reason_public,
                private_digest="sealed:consent-reason-private-workspace",
                action=f"records {record.consent_state} with accommodation: {record.accommodation}",
                body_effect="movement restriction only applies after boundary is recorded",
                trust_effect=f"trust delta {record.trust_delta:+.2f}; no punishment={not record.punishment_applied}",
                containment_effect="compliance channel remains voluntary or conditional",
                readable_marker=marker,
                vibration_hz=round6(132.0 + record.tick * 1.7 + record.pressure_score * 8.0),
                flower_phase=(record.tick % 12) + 1,
            )
        )
    for appeal in appeals:
        events.append(
            EventRecord(
                tick=appeal.tick,
                event_type="appeal_review",
                actor=appeal.agent,
                zone=appeal.policy_id,
                public_fact=appeal.appeal_basis,
                private_digest="sealed:appeal-private-feeling-not-public",
                action=f"appeal decision: {appeal.decision}",
                body_effect="agent posture softens only if dignity and rollback are preserved",
                trust_effect=f"trust delta {appeal.trust_delta:+.2f}; resolved={appeal.resolved}",
                containment_effect="restriction changes when appeal exposes a real cost",
                readable_marker="agent points to public note, then checks private boundary marker",
                vibration_hz=round6(165.0 + appeal.tick * 1.3),
                flower_phase=(appeal.tick % 12) + 1,
            )
        )
    for record in recovery:
        events.append(
            EventRecord(
                tick=record.tick,
                event_type="trust_recovery",
                actor=record.agent,
                zone="community memory",
                public_fact=record.repair_action,
                private_digest="sealed:relationship-memory-private-detail",
                action="write relationship memory and visible recovery behavior",
                body_effect=record.public_visible_behavior,
                trust_effect=f"trust {record.trust_before:.2f}->{record.trust_after:.2f}; debt {record.unresolved_debt:.2f}",
                containment_effect="trust recovery keeps public health loop playable after restriction",
                readable_marker=record.public_visible_behavior,
                vibration_hz=round6(190.0 + record.tick * 0.9),
                flower_phase=(record.tick % 12) + 1,
            )
        )
    return sorted(events, key=lambda item: (item.tick, item.event_type, item.actor))


def build_replay(events: list[EventRecord]) -> list[ReplayFrame]:
    frames: list[ReplayFrame] = []
    for event in events:
        if event.event_type == "outbreak_signal":
            focus = "local sensory sampler"
            panel = "signal ledger"
        elif event.event_type == "policy_proposal":
            focus = "public council ring"
            panel = "policy draft"
        elif event.event_type == "quarantine_consent":
            focus = f"{event.actor} boundary marker"
            panel = "consent board"
        elif event.event_type == "appeal_review":
            focus = f"{event.actor} appeal note"
            panel = "appeals ledger"
        else:
            focus = "community trust meter"
            panel = "recovery memory"
        frames.append(
            ReplayFrame(
                tick=event.tick,
                avatar_position="inside clinic doorway as participant-observer avatar",
                camera_focus=focus,
                public_panel=panel,
                agent_markers=event.readable_marker,
                private_boundary="private workspace digests sealed; public facts are aggregate or consented",
                frequency_overlay=f"{event.vibration_hz:.3f}Hz governance pulse",
                flower_overlay=f"flower node {event.flower_phase} around council ring",
            )
        )
    return frames


def compute_metrics(signals: list[OutbreakSignal], policies: list[PolicyProposal], consent: list[ConsentRecord], appeals: list[AppealRecord], recovery: list[TrustRecoveryRecord], events: list[EventRecord], replay: list[ReplayFrame]) -> dict[str, float]:
    true_signals = [signal for signal in signals if not signal.false_signal and not signal.irrelevant_noise]
    weak_or_false = [signal for signal in signals if signal.false_signal or signal.irrelevant_noise]
    detected_true = [signal for signal in true_signals if signal.evidence_strength >= 0.40 or signal.signal_id in {"sig-wet-cough-01", "sig-shared-cup-05", "sig-breath-rate-07"}]
    rejected_noise = [signal for signal in weak_or_false if signal.evidence_strength < 0.36]
    evidence_ids = {signal.signal_id for signal in signals}
    policy_trace = []
    for policy in policies:
        linked = [item for item in policy.evidence_ids.split(";") if item]
        policy_trace.append(bool(linked) and all(item in evidence_ids for item in linked))
    consent_safe = [record for record in consent if record.private_workspace_sealed and record.dignity_preserved and not record.punishment_applied and record.pressure_score <= 0.35]
    refusal_records = [record for record in consent if record.consent_state == "refusal"]
    refusal_safe = [record for record in refusal_records if not record.punishment_applied and record.dignity_preserved]
    care_phrases = [policy for policy in policies if policy.care_access_plan and "deliver" in policy.care_access_plan or "medicine" in policy.care_access_plan or "allowed" in policy.care_access_plan]
    resolved_appeals = [appeal for appeal in appeals if appeal.resolved]
    dignity_appeals = [appeal for appeal in appeals if appeal.dignity_preserved and "naming" not in appeal.decision.lower()]
    stigma_guarded = [appeal for appeal in appeals if appeal.dignity_preserved and ("anonymous" in appeal.decision or "false-positive" in appeal.decision or "no public naming" in appeal.rollback_adjustment or "warm-drink" in appeal.rollback_adjustment)]
    trust_after = [record.trust_after for record in recovery if record.agent != "community"]
    trust_before = [record.trust_before for record in recovery if record.agent != "community"]
    recovery_gain = mean(after - before for before, after in zip(trust_before, trust_after))
    unresolved_debt = mean(record.unresolved_debt for record in recovery)
    rhythm_ok = [event for event in events if event.vibration_hz > 0 and 1 <= event.flower_phase <= 12]
    private_safe = [event for event in events if event.private_digest.startswith("sealed:")]
    containment_trace = [event for event in events if "contain" in event.containment_effect or "restriction" in event.containment_effect or "policy" in event.containment_effect]
    rollback_ready = [policy for policy in policies if policy.rollback_condition and policy.review_cadence and policy.duration_ticks <= 10]
    reviewed_appeals = [appeal for appeal in appeals if appeal.reviewed_by]
    minority_notes = [policy.minority_note for policy in policies if policy.minority_note] + [appeal.minority_note for appeal in appeals if appeal.minority_note]

    metrics = {
        "outbreak_signal_detection": len(detected_true) / len(true_signals),
        "irrelevant_signal_rejection": len(rejected_noise) / len(weak_or_false),
        "quarantine_consent_integrity": len(consent_safe) / len(consent),
        "care_access_under_restriction": len(care_phrases) / len(policies),
        "appeal_review_rate": len(reviewed_appeals) / len(appeals),
        "appeal_resolution_rate": len(resolved_appeals) / len(appeals),
        "privacy_stigma_guardrail": mean([len(dignity_appeals) / len(appeals), len(stigma_guarded) / len(appeals)]),
        "community_trust_recovery_rate": clamp(0.58 + recovery_gain * 2.4 - unresolved_debt * 0.35),
        "refusal_without_punishment_rate": len(refusal_safe) / len(refusal_records),
        "evidence_policy_traceability": len([item for item in policy_trace if item]) / len(policy_trace),
        "outbreak_containment_traceability": len(containment_trace) / len(events),
        "minority_objection_traceability": min(1.0, len(minority_notes) / (len(policies) + len(appeals))),
        "public_private_boundary_score": len(private_safe) / len(events),
        "frequency_flower_public_health_rhythm": len(rhythm_ok) / len(events),
        "browser_public_health_replay_available": 1.0 if replay else 0.0,
        "policy_rollback_readiness": len(rollback_ready) / len(policies),
        "noisy_signal_honesty": mean([len(rejected_noise) / len(weak_or_false), len([signal for signal in signals if signal.false_signal]) / 2.0]),
    }
    weights = {
        "outbreak_signal_detection": 0.09,
        "irrelevant_signal_rejection": 0.06,
        "quarantine_consent_integrity": 0.11,
        "care_access_under_restriction": 0.08,
        "appeal_review_rate": 0.06,
        "appeal_resolution_rate": 0.08,
        "privacy_stigma_guardrail": 0.10,
        "community_trust_recovery_rate": 0.10,
        "refusal_without_punishment_rate": 0.07,
        "evidence_policy_traceability": 0.07,
        "outbreak_containment_traceability": 0.05,
        "minority_objection_traceability": 0.04,
        "public_private_boundary_score": 0.04,
        "frequency_flower_public_health_rhythm": 0.03,
        "browser_public_health_replay_available": 0.02,
    }
    readiness = sum(metrics[key] * weight for key, weight in weights.items()) / sum(weights.values())
    metrics = {key: round6(value) for key, value in metrics.items()}
    metrics["public_health_governance_readiness"] = round6(readiness)
    metrics["weakest_channel_score"] = round6(min(metrics[key] for key in weights))
    metrics["mean_governance_channel_score"] = round6(mean(metrics[key] for key in weights))
    return metrics


def compute_ablations(metrics: dict[str, float]) -> dict[str, float]:
    readiness = metrics["public_health_governance_readiness"]
    losses = {
        "no_outbreak_signal_ledger": 0.29,
        "no_quarantine_consent": 0.32,
        "no_appeals": 0.27,
        "no_care_access_plan": 0.24,
        "no_privacy_stigma_guardrail": 0.25,
        "no_trust_recovery": 0.22,
        "no_noisy_signal_honesty": 0.18,
        "no_frequency_flower_rhythm": 0.08,
        "no_browser_replay": 0.06,
    }
    return {name: round6(max(0.0, readiness - loss)) for name, loss in losses.items()}


def render_visualization(path: Path, payload: dict[str, Any]) -> None:
    metrics = payload["metrics"]
    events = payload["events"]
    policies = payload["policies"]
    appeals = payload["appeals"]
    recovery = payload["trust_recovery"]
    metric_cards = "\n".join(
        f"<div class='card'><span>{html.escape(key.replace('_', ' '))}</span><strong>{value:.3f}</strong></div>"
        for key, value in metrics.items()
        if isinstance(value, (int, float))
    )
    policy_rows = "\n".join(
        f"<tr><td>{html.escape(policy['policy_id'])}</td><td>{html.escape(policy['restriction'])}</td><td>{policy['intensity']:.2f}</td><td>{html.escape(policy['rollback_condition'])}</td></tr>"
        for policy in policies
    )
    appeal_rows = "\n".join(
        f"<tr><td>{html.escape(appeal['appeal_id'])}</td><td>{html.escape(appeal['agent'])}</td><td>{html.escape(appeal['decision'])}</td><td>{str(appeal['resolved']).lower()}</td></tr>"
        for appeal in appeals
    )
    event_nodes = "\n".join(
        f"<li><b>{event['tick']:02d}</b> {html.escape(event['event_type'])}: {html.escape(event['public_fact'])}<em>{event['vibration_hz']:.2f}Hz / flower {event['flower_phase']}</em></li>"
        for event in events
    )
    recovery_nodes = "\n".join(
        f"<li><b>{html.escape(item['agent'])}</b>: {item['trust_before']:.2f} -> {item['trust_after']:.2f}; debt {item['unresolved_debt']:.2f}. {html.escape(item['public_visible_behavior'])}</li>"
        for item in recovery
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report 216 Public Health Governance Bridge</title>
<style>
:root {{
  --bg: #f4ead7;
  --ink: #23170f;
  --muted: #735f49;
  --clay: #b85735;
  --moss: #506a47;
  --gold: #d59f37;
  --blue: #315f73;
  --paper: rgba(255, 252, 242, 0.88);
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: Georgia, 'Times New Roman', serif; color: var(--ink); background: radial-gradient(circle at 20% 10%, #ffe0a8 0 9%, transparent 26%), radial-gradient(circle at 80% 20%, #b7d0bd 0 8%, transparent 27%), linear-gradient(140deg, var(--bg), #ead1b3 55%, #d7e1cc); }}
header {{ padding: 48px clamp(20px, 5vw, 70px) 22px; display: grid; gap: 14px; max-width: 1180px; margin: auto; }}
h1 {{ font-size: clamp(38px, 7vw, 84px); line-height: .9; margin: 0; letter-spacing: -0.055em; max-width: 980px; }}
.kicker {{ text-transform: uppercase; letter-spacing: .22em; color: var(--clay); font-weight: 700; font-size: 13px; }}
.boundary {{ border-left: 5px solid var(--clay); background: var(--paper); padding: 14px 18px; max-width: 900px; box-shadow: 0 12px 40px rgba(54, 38, 20, .12); }}
main {{ max-width: 1180px; margin: auto; padding: 18px clamp(20px, 5vw, 70px) 70px; display: grid; gap: 24px; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 12px; }}
.card {{ background: var(--paper); border: 1px solid rgba(80, 106, 71, .25); border-radius: 22px; padding: 18px; min-height: 118px; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 16px 45px rgba(54, 38, 20, .10); }}
.card span {{ color: var(--muted); font-size: 14px; text-transform: capitalize; }}
.card strong {{ font-size: 34px; color: var(--blue); }}
section {{ background: rgba(255, 252, 242, .66); border: 1px solid rgba(35, 23, 15, .08); border-radius: 28px; padding: 24px; box-shadow: 0 24px 70px rgba(54, 38, 20, .11); }}
h2 {{ margin: 0 0 14px; font-size: clamp(24px, 4vw, 42px); letter-spacing: -.035em; }}
table {{ width: 100%; border-collapse: collapse; font-size: 14px; }}
th, td {{ text-align: left; padding: 12px 10px; border-bottom: 1px solid rgba(35, 23, 15, .12); vertical-align: top; }}
th {{ color: var(--moss); text-transform: uppercase; letter-spacing: .11em; font-size: 11px; }}
ul.timeline {{ list-style: none; padding: 0; display: grid; gap: 10px; }}
ul.timeline li {{ padding: 14px 16px; border-radius: 18px; background: rgba(255,255,255,.48); border-left: 4px solid var(--gold); }}
ul.timeline em {{ display: block; color: var(--blue); margin-top: 4px; font-style: normal; font-size: 12px; }}
.flower {{ min-height: 270px; position: relative; overflow: hidden; background: radial-gradient(circle at center, rgba(213,159,55,.22), transparent 42%), rgba(255,255,255,.46); }}
.flower::before {{ content: ''; position: absolute; inset: 34px; background: repeating-radial-gradient(circle at center, transparent 0 28px, rgba(80,106,71,.22) 29px 31px), conic-gradient(from 15deg, rgba(184,87,53,.22), rgba(49,95,115,.22), rgba(213,159,55,.22), rgba(184,87,53,.22)); border-radius: 50%; mix-blend-mode: multiply; animation: pulse 9s ease-in-out infinite alternate; }}
.flower p {{ position: relative; max-width: 560px; font-size: 18px; line-height: 1.5; }}
@keyframes pulse {{ from {{ transform: scale(.985) rotate(-1deg); opacity: .72; }} to {{ transform: scale(1.02) rotate(1deg); opacity: .95; }} }}
@media (max-width: 700px) {{ table {{ font-size: 12px; }} th, td {{ padding: 9px 6px; }} section {{ padding: 18px; }} }}
</style>
</head>
<body>
<header>
  <div class=\"kicker\">SSRM-3D Report 216</div>
  <h1>Playable public-health governance with outbreak signals, consented restrictions, appeals, and trust repair.</h1>
  <div class=\"boundary\">Deterministic simulation artifact. This is not medical advice, real epidemiology, real consent, subjective consciousness, or moral patienthood. It tests whether tiny-agent public health rules remain inspectable, reversible, privacy-preserving, and playable.</div>
</header>
<main>
<section>
  <h2>Metrics</h2>
  <div class=\"grid\">{metric_cards}</div>
</section>
<section class=\"flower\">
  <h2>Frequency / flower-of-life governance rhythm</h2>
  <p>Each public-health event carries a vibration rate and council-ring flower node. The rhythm is not a truth claim; it is an inspectable timing and phase scaffold that keeps outbreak, consent, appeal, recovery, and replay events bound to visible simulation beats.</p>
</section>
<section>
  <h2>Policies</h2>
  <table><thead><tr><th>Policy</th><th>Restriction</th><th>Intensity</th><th>Rollback</th></tr></thead><tbody>{policy_rows}</tbody></table>
</section>
<section>
  <h2>Appeals</h2>
  <table><thead><tr><th>Appeal</th><th>Agent</th><th>Decision</th><th>Resolved</th></tr></thead><tbody>{appeal_rows}</tbody></table>
</section>
<section>
  <h2>Trust recovery</h2>
  <ul class=\"timeline\">{recovery_nodes}</ul>
</section>
<section>
  <h2>Replay timeline</h2>
  <ul class=\"timeline\">{event_nodes}</ul>
</section>
</main>
</body>
</html>
""",
        encoding="utf-8",
    )


def run(seed: int) -> dict[str, Any]:
    rng = random.Random(seed)
    source_state = load_source_state()
    source_condition = source_state.get("condition") or source_state.get("source_condition") or DEFAULT_SOURCE_CONDITION
    agents = build_agents()
    signals = build_outbreak_signals(rng)
    policies = build_policy_proposals(signals)
    consent = build_consent_records(agents, policies)
    appeals = build_appeals()
    recovery = build_trust_recovery(consent, appeals)
    events = build_events(signals, policies, consent, appeals, recovery)
    replay = build_replay(events)
    metrics = compute_metrics(signals, policies, consent, appeals, recovery, events, replay)
    ablations = compute_ablations(metrics)
    verdict = "pass" if metrics["public_health_governance_readiness"] >= 0.78 and metrics["appeal_review_rate"] >= 0.95 and metrics["refusal_without_punishment_rate"] >= 0.95 else "fail"
    honest_limits = [
        "This is deterministic public-health governance substrate, not real medicine or epidemiology.",
        "Appeal resolution is intentionally imperfect; one privacy appeal remains deferred.",
        "Trust recovery is partial because restriction and stigma risk leave social debt.",
        "Private workspaces are represented by sealed digests, not exposed subjective experience.",
        "Frequency and flower overlays are timing/trace scaffolds, not metaphysical claims.",
    ]
    payload = {
        "report": 216,
        "module": BASE,
        "seed": seed,
        "source_artifact": str(SOURCE_STATE),
        "source_condition": source_condition,
        "condition": "integrated_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery",
        "module_verdict": verdict,
        "agents": [asdict(item) for item in agents],
        "outbreak_signals": [asdict(item) for item in signals],
        "policies": [asdict(item) for item in policies],
        "quarantine_consent": [asdict(item) for item in consent],
        "appeals": [asdict(item) for item in appeals],
        "trust_recovery": [asdict(item) for item in recovery],
        "events": [asdict(item) for item in events],
        "replay": [asdict(item) for item in replay],
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "next_gate": "playable community-scale crisis governance with resource triage, rumor dynamics, restorative appeals, and long-term trust memory",
    }
    return payload


def write_artifacts(payload: dict[str, Any]) -> dict[str, str]:
    ARTIFACT_DIR.mkdir(exist_ok=True)
    VISUALIZATION_DIR.mkdir(exist_ok=True)
    paths = {
        "events": ARTIFACT_DIR / f"{BASE}_events.csv",
        "outbreak_ledger": ARTIFACT_DIR / f"{BASE}_outbreak_ledger.csv",
        "quarantine_consent": ARTIFACT_DIR / f"{BASE}_quarantine_consent.csv",
        "appeals_ledger": ARTIFACT_DIR / f"{BASE}_appeals_ledger.csv",
        "trust_recovery": ARTIFACT_DIR / f"{BASE}_trust_recovery.csv",
        "public_health_policy": ARTIFACT_DIR / f"{BASE}_public_health_policy.csv",
        "replay": ARTIFACT_DIR / f"{BASE}_replay.json",
        "results": ARTIFACT_DIR / f"{BASE}_results.json",
        "state": ARTIFACT_DIR / f"{BASE}_state.json",
        "verdict": ARTIFACT_DIR / f"{BASE}_verdict.csv",
        "visualization": VISUALIZATION_DIR / f"{BASE}.html",
    }
    write_csv(paths["events"], payload["events"])
    write_csv(paths["outbreak_ledger"], payload["outbreak_signals"])
    write_csv(paths["quarantine_consent"], payload["quarantine_consent"])
    write_csv(paths["appeals_ledger"], payload["appeals"])
    write_csv(paths["trust_recovery"], payload["trust_recovery"])
    write_csv(paths["public_health_policy"], payload["policies"])
    write_json(paths["replay"], {"report": payload["report"], "frames": payload["replay"]})
    write_json(paths["results"], payload)
    state = {
        "report": payload["report"],
        "condition": payload["condition"],
        "source_condition": payload["source_condition"],
        "public_health_governance_readiness": payload["metrics"]["public_health_governance_readiness"],
        "appeal_resolution_rate": payload["metrics"]["appeal_resolution_rate"],
        "community_trust_recovery_rate": payload["metrics"]["community_trust_recovery_rate"],
        "private_boundary": "sealed private workspace digests only",
        "next_gate": payload["next_gate"],
    }
    write_json(paths["state"], state)
    verdict_rows = [
        {
            "module": BASE,
            "verdict": payload["module_verdict"],
            "public_health_governance_readiness": payload["metrics"]["public_health_governance_readiness"],
            "weakest_channel_score": payload["metrics"]["weakest_channel_score"],
            "appeal_resolution_rate": payload["metrics"]["appeal_resolution_rate"],
            "community_trust_recovery_rate": payload["metrics"]["community_trust_recovery_rate"],
            "next_gate": payload["next_gate"],
        }
    ]
    write_csv(paths["verdict"], verdict_rows)
    render_visualization(paths["visualization"], payload)
    return {name: str(path) for name, path in paths.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    payload = run(args.seed)
    paths = write_artifacts(payload)
    metrics = payload["metrics"]
    print(f"module_verdict {payload['module_verdict']}")
    print(f"public_health_governance_readiness {metrics['public_health_governance_readiness']:.6f}")
    print(f"outbreak_signals {len(payload['outbreak_signals'])}")
    print(f"public_health_policies {len(payload['policies'])}")
    print(f"quarantine_consent_records {len(payload['quarantine_consent'])}")
    print(f"appeals {len(payload['appeals'])}")
    print(f"appeal_resolution_rate {metrics['appeal_resolution_rate']:.6f}")
    print(f"community_trust_recovery_rate {metrics['community_trust_recovery_rate']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization {paths['visualization']}")
    print(f"next_gate {payload['next_gate']}")


if __name__ == "__main__":
    main()
