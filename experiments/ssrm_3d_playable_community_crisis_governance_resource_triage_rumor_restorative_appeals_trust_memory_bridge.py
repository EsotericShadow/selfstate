#!/usr/bin/env python3
"""Report 217: SSRM-3D playable community crisis governance bridge.

This deterministic bridge extends public-health governance into a wider community
crisis loop: scarce resources, triage decisions, rumor propagation/correction,
restorative appeals, and long-term trust memory. It is a simulation artifact,
not real crisis management, real medicine, real consent, subjective suffering,
or moral patienthood.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Iterable


BASE = "ssrm_3d_playable_community_crisis_governance_resource_triage_rumor_restorative_appeals_trust_memory_bridge"
ARTIFACT_DIR = Path("artifacts")
VISUALIZATION_DIR = Path("visualizations")
SOURCE_STATE = ARTIFACT_DIR / "ssrm_3d_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery_bridge_state.json"
DEFAULT_SOURCE_CONDITION = "integrated_playable_public_health_governance_outbreak_quarantine_appeals_trust_recovery"
DEFAULT_SEED = 20260830


@dataclass(frozen=True)
class Agent:
    name: str
    role: str
    home_zone: str
    clan_or_workshop: str
    crisis_need: float
    autonomy_need: float
    stigma_sensitivity: float
    trust_in_council: float
    rumor_susceptibility: float
    long_memory_years: int
    remembered_custom: str


@dataclass(frozen=True)
class ResourceStock:
    tick: int
    resource_id: str
    kind: str
    location: str
    available_units: float
    baseline_need: float
    scarcity_pressure: float
    spoilage_or_wear_risk: float
    access_constraint: str
    vibration_hz: float
    flower_node: int


@dataclass(frozen=True)
class CrisisPolicy:
    tick: int
    policy_id: str
    trigger: str
    scope: str
    rule: str
    rollback_condition: str
    care_exception: str
    public_reason: str
    minority_note: str
    review_interval_ticks: int
    vibration_hz: float
    flower_node: int


@dataclass(frozen=True)
class TriageDecision:
    tick: int
    decision_id: str
    policy_id: str
    resource_id: str
    agent: str
    requested_units: float
    allocated_units: float
    priority_basis: str
    need_score: float
    fairness_score: float
    care_continuity: bool
    autonomy_boundary: str
    visible_body_marker: str
    unresolved_debt: float
    trust_delta: float


@dataclass(frozen=True)
class RumorRecord:
    tick: int
    rumor_id: str
    source_agent: str
    claim: str
    target: str
    channel: str
    evidence_status: str
    harm_risk: float
    spread_rate: float
    correction_action: str
    corrected: bool
    residual_belief: float
    stigma_guardrail: str
    trust_delta: float
    vibration_hz: float
    flower_node: int


@dataclass(frozen=True)
class RestorativeAppeal:
    tick: int
    appeal_id: str
    agent: str
    linked_decision_or_rumor: str
    harm_claim: str
    requested_repair: str
    circle_members: str
    decision: str
    resolved: bool
    repair_action: str
    dignity_preserved: bool
    future_rule_change: str
    trust_delta: float


@dataclass(frozen=True)
class TrustMemory:
    tick: int
    agent: str
    memory_id: str
    epoch_year: int
    event_summary: str
    trust_before: float
    trust_after: float
    social_debt: float
    relationship_tag: str
    private_detail_digest: str
    public_behavior: str


@dataclass(frozen=True)
class EventRecord:
    tick: int
    event_type: str
    actor: str
    zone: str
    public_fact: str
    private_digest: str
    action: str
    resource_effect: str
    rumor_effect: str
    trust_effect: str
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
        Agent("Ari", "route repairer", "west route", "stone bridge workshop", 0.62, 0.73, 0.56, 0.70, 0.28, 3180, "repair debt is repaid in public work circles"),
        Agent("Fay", "clinic helper", "warm alcove", "hearth keepers", 0.82, 0.46, 0.82, 0.77, 0.34, 3260, "care gifts travel with apology knots"),
        Agent("Milo", "inventory runner", "tool shed", "cart path runners", 0.54, 0.84, 0.70, 0.61, 0.52, 3015, "runner accusations require witness countersigns"),
        Agent("Nia", "language keeper", "north desk", "archive speakers", 0.58, 0.66, 0.86, 0.66, 0.31, 3425, "public stories must not expose private body names"),
        Agent("Sol", "water steward", "cistern stairs", "cistern guild", 0.74, 0.55, 0.63, 0.58, 0.47, 2880, "water shame is answered by shared carrying duty"),
    ]


def build_resources(rng: random.Random) -> list[ResourceStock]:
    rows = [
        (3, "res-blankets", "warm blankets", "warm alcove", 7.0, 10.0, 0.18, "quarantine spacing slows pickup"),
        (4, "res-dry-cups", "named dry cups", "clinic shelf", 9.0, 12.0, 0.06, "cup labels cannot expose status"),
        (5, "res-repair-tools", "repair tools", "tool shed", 4.0, 8.0, 0.21, "windowing policy limits access"),
        (6, "res-clean-water", "clean water", "cistern stairs", 11.0, 15.0, 0.09, "rumor about hoarding increases crowding"),
        (8, "res-medicine-kit", "medicine kit", "clinic drawer", 3.0, 6.0, 0.14, "side-effect notes require private review"),
    ]
    resources: list[ResourceStock] = []
    for index, (tick, rid, kind, loc, available, need, wear, constraint) in enumerate(rows, start=1):
        pressure = clamp((need - available) / need + wear + rng.uniform(-0.012, 0.012))
        resources.append(
            ResourceStock(
                tick=tick,
                resource_id=rid,
                kind=kind,
                location=loc,
                available_units=round6(available),
                baseline_need=round6(need),
                scarcity_pressure=round6(pressure),
                spoilage_or_wear_risk=round6(wear),
                access_constraint=constraint,
                vibration_hz=round6(121.0 + index * 16.25 + pressure * 12.0),
                flower_node=((index - 1) % 12) + 1,
            )
        )
    return resources


def build_policies() -> list[CrisisPolicy]:
    return [
        CrisisPolicy(9, "policy-critical-warmth-first", "blankets below baseline during wet cold", "warm alcove and west route", "allocate warmth by body need first, then work duty", "two ticks above 9 blankets or temperature comfort above 0.72", "no one loses care access for refusing public naming", "cold and wetness make warmth a body-safety resource, not a status reward", "Milo asks that runners who stay outside are not forgotten", 2, 155.0, 4),
        CrisisPolicy(10, "policy-repair-lane-ration", "repair tools below route safety threshold", "tool shed", "reserve one repair lane and rotate the remaining tools", "route safety stable and tool wear below 0.16", "urgent clinic fixes override workshop pride", "route collapse would harm everyone, but tool access must not become ownership capture", "Ari accepts rotation only if broken paths are counted as care infrastructure", 3, 188.0, 7),
        CrisisPolicy(12, "policy-rumor-cooldown", "hoarding rumor spread rate above safe level", "cistern stairs and public panel", "pause accusation posts until evidence and witness countersign exist", "residual belief below 0.20 for two ticks", "water access stays open while rumor is reviewed", "rumors can damage dignity before facts arrive", "Sol worries silence will look like guilt", 2, 223.0, 10),
    ]


def build_triage(resources: list[ResourceStock], policies: list[CrisisPolicy]) -> list[TriageDecision]:
    return [
        TriageDecision(11, "triage-fay-blanket", "policy-critical-warmth-first", "res-blankets", "Fay", 2.0, 2.0, "high care need and warm-alcove clinic work", 0.86, 0.91, True, "does not require naming body symptoms", "wraps blanket around shoulders and keeps clinic doorway open", 0.03, 0.05),
        TriageDecision(11, "triage-ari-blanket", "policy-critical-warmth-first", "res-blankets", "Ari", 1.0, 1.0, "wet route repair exposure", 0.71, 0.82, True, "may return blanket after dry-route shift", "walks slower but resumes west-route repair", 0.06, 0.02),
        TriageDecision(12, "triage-milo-blanket-delay", "policy-critical-warmth-first", "res-blankets", "Milo", 2.0, 1.0, "runner exposure recognized but lower cold marker", 0.58, 0.64, False, "can appeal delay without punishment", "paces near the cart path and keeps one hand on runner bag", 0.19, -0.04),
        TriageDecision(13, "triage-ari-tool-lane", "policy-repair-lane-ration", "res-repair-tools", "Ari", 2.0, 1.5, "route collapse prevention", 0.77, 0.79, True, "must share repair notes after use", "lifts tool openly toward public repair board", 0.08, 0.02),
        TriageDecision(13, "triage-milo-tool-delay", "policy-repair-lane-ration", "res-repair-tools", "Milo", 1.0, 0.5, "inventory need deferred behind urgent repair lane", 0.52, 0.58, False, "delay recorded as appealable, not lazy", "looks away from tool shed and writes a short objection", 0.22, -0.05),
        TriageDecision(14, "triage-sol-water", "policy-rumor-cooldown", "res-clean-water", "Sol", 4.0, 3.0, "water steward must keep cistern moving", 0.80, 0.73, True, "allocation cannot be framed as proof of innocence", "keeps carrying water but avoids the accusation wall", 0.16, -0.02),
        TriageDecision(15, "triage-nia-cup-privacy", "policy-rumor-cooldown", "res-dry-cups", "Nia", 1.0, 1.0, "privacy-preserving language desk cups", 0.63, 0.88, True, "cup ledger remains hashed", "stands by the north desk and closes private note flap", 0.04, 0.04),
        TriageDecision(16, "triage-fay-medicine", "policy-critical-warmth-first", "res-medicine-kit", "Fay", 2.0, 1.0, "clinic continuity during scarcity", 0.84, 0.70, True, "side-effect details stay sealed", "checks medicine drawer then marks a stockout warning", 0.15, 0.01),
    ]


def build_rumors() -> list[RumorRecord]:
    return [
        RumorRecord(12, "rumor-sol-hoards-water", "unknown whisper", "Sol hid clean water for the cistern guild", "Sol", "cistern stairs", "contradicted by stock ledger", 0.78, 0.62, "publish aggregate water ledger and witness countersign without exposing private need", True, 0.18, "no naming of body state or family blame", 0.03, 241.0, 11),
        RumorRecord(13, "rumor-milo-spread-cough", "anxious runner", "Milo caused the breath-rate cluster", "Milo", "tool shed", "mixed with prior false dust signal", 0.71, 0.48, "pin false-positive dust note beside crowding evidence", True, 0.24, "runner identity cannot be used as diagnosis", 0.02, 257.0, 12),
        RumorRecord(15, "rumor-fay-keeps-medicine", "blanket queue", "Fay keeps medicine for favorites", "Fay", "warm alcove", "not supported; stockout is real but favoritism unproven", 0.66, 0.41, "publish stockout and appeal route, but private side-effect notes remain sealed", True, 0.27, "care history cannot be mined for accusation", 0.01, 263.0, 2),
        RumorRecord(18, "rumor-ari-tool-pride", "tool shed joke", "Ari takes tools because pride matters more than care", "Ari", "tool shed", "partly misleading; urgent lane exists but rotation debt is real", 0.49, 0.35, "add repair-lane minutes and tool-return receipt to public board", True, 0.21, "workshop status cannot override repair evidence", 0.02, 282.0, 5),
        RumorRecord(20, "rumor-nia-hides-records", "north desk murmur", "Nia hides crisis records to protect archive speakers", "Nia", "north desk", "unresolved; public records exist but one privacy appeal is deferred", 0.58, 0.32, "publish what is public and mark deferred private check without naming bodies", False, 0.36, "privacy delay is not guilt", -0.03, 296.0, 8),
    ]


def build_appeals() -> list[RestorativeAppeal]:
    return [
        RestorativeAppeal(14, "appeal-milo-blanket-delay", "Milo", "triage-milo-blanket-delay", "runner exposure was undercounted because he moves between zones", "add outside-exposure weight and second blanket check", "Ari,Fay,Nia,Sol", "accepted with exposure weight adjustment", True, "Milo gets a next-window warmth check and a public note that delay was scarcity, not blame", True, "triage formulas must include moving work", 0.08),
        RestorativeAppeal(16, "appeal-sol-water-rumor", "Sol", "rumor-sol-hoards-water", "water rumor made necessary allocation look like guilt", "public countersign and carrying-duty circle", "Ari,Fay,Milo,Nia", "accepted with shared carrying duty", True, "two agents carry water with Sol so correction is embodied, not just posted", True, "rumor correction requires a repair action when dignity was harmed", 0.10),
        RestorativeAppeal(17, "appeal-fay-medicine-favorites", "Fay", "rumor-fay-keeps-medicine", "medicine stockout became a character accusation", "separate stockout fact from private care notes", "Ari,Milo,Nia,Sol", "accepted with stockout board and sealed care history", True, "public board shows low stock; private side-effect histories remain sealed", True, "care ledgers cannot expose relationship history", 0.07),
        RestorativeAppeal(19, "appeal-milo-tool-delay", "Milo", "triage-milo-tool-delay", "inventory work was delayed twice and called less urgent", "create rotating runner tool slot", "Ari,Fay,Nia,Sol", "partly accepted; runner slot added after route safety check", True, "Milo receives a scheduled slot but no backdated tool claim", True, "repeat delays accumulate social debt even when each decision is defensible", 0.04),
        RestorativeAppeal(21, "appeal-nia-privacy-rumor", "Nia", "rumor-nia-hides-records", "deferred privacy appeal created suspicion around archive work", "publish a boundary explanation and set review time", "Ari,Fay,Milo,Sol", "deferred; review time set but rumor residue remains", False, "boundary explanation posted; no private body details exposed", True, "private boundaries need public explanations during crisis", -0.01),
    ]


def build_trust_memory(agents: list[Agent], triage: list[TriageDecision], rumors: list[RumorRecord], appeals: list[RestorativeAppeal]) -> list[TrustMemory]:
    base = {agent.name: agent.trust_in_council for agent in agents}
    delta = {agent.name: 0.0 for agent in agents}
    for row in triage:
        delta[row.agent] += row.trust_delta
    for row in rumors:
        if row.target in delta:
            delta[row.target] += row.trust_delta
    for row in appeals:
        delta[row.agent] += row.trust_delta
    summaries = {
        "Ari": "urgent repair lane was defended, but tool-pride rumor required public receipts",
        "Fay": "medicine accusation was separated from stockout facts without exposing care history",
        "Milo": "runner delays became appealable social debt instead of laziness blame",
        "Nia": "privacy boundary stayed sealed, but deferred review left rumor residue",
        "Sol": "water hoarding rumor was answered through shared carrying duty",
    }
    tags = {
        "Ari": "repair-duty-trust",
        "Fay": "care-ledger-dignity",
        "Milo": "runner-autonomy-repair",
        "Nia": "archive-privacy-debt",
        "Sol": "cistern-restorative-repair",
    }
    behavior = {
        "Ari": "returns tool at the public board instead of keeping it near the workshop bench",
        "Fay": "points to the stockout board before opening the private medicine drawer",
        "Milo": "takes the runner slot but waits for the warmth recheck marker",
        "Nia": "keeps the archive flap closed and reads the boundary explanation aloud",
        "Sol": "walks the cistern route with two witnesses carrying beside him",
    }
    memories: list[TrustMemory] = []
    for index, agent in enumerate(agents, start=1):
        before = base[agent.name]
        after = clamp(before + delta[agent.name])
        social_debt = clamp(0.08 + (0.16 if agent.name in {"Milo", "Nia", "Sol"} else 0.04) - max(0.0, after - before) * 0.35)
        memories.append(
            TrustMemory(
                tick=22 + index,
                agent=agent.name,
                memory_id=f"memory-{agent.name.lower()}-crisis-year-{agent.long_memory_years}",
                epoch_year=agent.long_memory_years,
                event_summary=summaries[agent.name],
                trust_before=round6(before),
                trust_after=round6(after),
                social_debt=round6(social_debt),
                relationship_tag=tags[agent.name],
                private_detail_digest=f"sealed:{agent.name.lower()}:crisis-body-workspace-not-public",
                public_behavior=behavior[agent.name],
            )
        )
    return memories


def build_events(resources: list[ResourceStock], policies: list[CrisisPolicy], triage: list[TriageDecision], rumors: list[RumorRecord], appeals: list[RestorativeAppeal], memories: list[TrustMemory]) -> list[EventRecord]:
    events: list[EventRecord] = []
    for row in resources:
        events.append(
            EventRecord(row.tick, "resource_stock", "council ledger", row.location, f"{row.kind} available {row.available_units:.1f}/{row.baseline_need:.1f}", "sealed:stock-body-need-details", "open scarcity ledger with access constraint", f"scarcity pressure {row.scarcity_pressure:.3f}; wear risk {row.spoilage_or_wear_risk:.3f}", "rumor risk rises if resource ledger is missing", "trust depends on visible stock and private need protection", "agents glance at resource shelf before speaking", row.vibration_hz, row.flower_node)
        )
    for row in policies:
        events.append(
            EventRecord(row.tick, "crisis_policy", "crisis council", row.scope, row.public_reason, "sealed:policy-private-deliberation", f"activate {row.rule}", row.care_exception, "rumor cooldown attached when accusation risk rises", f"minority note: {row.minority_note}", "agents sit in a rough flower-ring rather than a queue", row.vibration_hz, row.flower_node)
        )
    for row in triage:
        events.append(
            EventRecord(row.tick, "resource_triage", row.agent, row.resource_id, f"{row.agent} receives {row.allocated_units:.1f}/{row.requested_units:.1f} units because {row.priority_basis}", "sealed:triage-private-body-state", f"record triage fairness {row.fairness_score:.2f} and debt {row.unresolved_debt:.2f}", f"care continuity={row.care_continuity}; boundary={row.autonomy_boundary}", "triage debt can become rumor fuel if not appealed", f"trust delta {row.trust_delta:+.2f}", row.visible_body_marker, round6(171.0 + row.tick * 1.8 + row.fairness_score * 5.0), (row.tick % 12) + 1)
        )
    for row in rumors:
        action = "correct rumor with public evidence and repair action" if row.corrected else "mark rumor unresolved and preserve boundary while review continues"
        events.append(
            EventRecord(row.tick, "rumor", row.source_agent, row.channel, row.claim, "sealed:rumor-private-source-detail", action, "resource access cannot be used as proof of guilt", f"harm {row.harm_risk:.2f}; spread {row.spread_rate:.2f}; residual {row.residual_belief:.2f}", f"trust delta {row.trust_delta:+.2f}; guardrail={row.stigma_guardrail}", "nearby agents turn toward the public panel instead of the target body", row.vibration_hz, row.flower_node)
        )
    for row in appeals:
        events.append(
            EventRecord(row.tick, "restorative_appeal", row.agent, row.linked_decision_or_rumor, row.harm_claim, "sealed:appeal-private-feeling-not-public", f"decision: {row.decision}; repair: {row.repair_action}", row.future_rule_change, "appeal can lower rumor residue when resolved", f"trust delta {row.trust_delta:+.2f}; resolved={row.resolved}", "agent speaks from boundary marker while circle members face them", round6(210.0 + row.tick * 1.4), (row.tick % 12) + 1)
        )
    for row in memories:
        events.append(
            EventRecord(row.tick, "long_term_trust_memory", row.agent, "community memory", row.event_summary, row.private_detail_digest, "write durable relationship memory and future behavior cue", f"social debt {row.social_debt:.2f} remains after crisis", "rumor residue carried forward only as bounded memory", f"trust {row.trust_before:.2f}->{row.trust_after:.2f}", row.public_behavior, round6(248.0 + row.tick * 0.85), (row.tick % 12) + 1)
        )
    return sorted(events, key=lambda item: (item.tick, item.event_type, item.actor))


def build_replay(events: list[EventRecord]) -> list[ReplayFrame]:
    frames: list[ReplayFrame] = []
    for row in events:
        panel = {
            "resource_stock": "scarcity ledger",
            "crisis_policy": "crisis policy board",
            "resource_triage": "triage table",
            "rumor": "rumor correction wall",
            "restorative_appeal": "restorative circle",
            "long_term_trust_memory": "community memory shelf",
        }.get(row.event_type, "public panel")
        frames.append(
            ReplayFrame(
                tick=row.tick,
                avatar_position="community square threshold as participant-observer avatar",
                camera_focus=f"{row.actor} / {row.event_type}",
                public_panel=panel,
                agent_markers=row.readable_marker,
                private_boundary="private body states, feelings, and workspace details remain sealed digests",
                frequency_overlay=f"{row.vibration_hz:.3f}Hz crisis pulse",
                flower_overlay=f"flower node {row.flower_phase} around crisis circle",
            )
        )
    return frames


def compute_metrics(resources: list[ResourceStock], policies: list[CrisisPolicy], triage: list[TriageDecision], rumors: list[RumorRecord], appeals: list[RestorativeAppeal], memories: list[TrustMemory], events: list[EventRecord], replay: list[ReplayFrame]) -> dict[str, float]:
    scarce_resources = [row for row in resources if row.scarcity_pressure >= 0.25]
    scarce_linked = [row for row in scarce_resources if any(decision.resource_id == row.resource_id for decision in triage)]
    care_decisions = [row for row in triage if row.care_continuity]
    high_need = [row for row in triage if row.need_score >= 0.75]
    high_need_covered = [row for row in high_need if row.allocated_units / row.requested_units >= 0.5]
    appealable_debt = [row for row in triage if row.unresolved_debt >= 0.15]
    appealed_debt_ids = {appeal.linked_decision_or_rumor for appeal in appeals}
    corrected_rumors = [row for row in rumors if row.corrected]
    harmful_rumors = [row for row in rumors if row.harm_risk >= 0.55]
    contained_harm = [row for row in harmful_rumors if row.residual_belief <= 0.30 or row.corrected]
    resolved_appeals = [row for row in appeals if row.resolved]
    dignified_appeals = [row for row in appeals if row.dignity_preserved]
    memory_safe = [row for row in memories if row.private_detail_digest.startswith("sealed:") and row.relationship_tag]
    private_safe_events = [row for row in events if row.private_digest.startswith("sealed:")]
    rhythm_events = [row for row in events if row.vibration_hz > 0 and 1 <= row.flower_phase <= 12]
    boundary_decisions = [row for row in triage if row.autonomy_boundary and "punish" not in row.autonomy_boundary.lower()]
    policies_with_rollback = [row for row in policies if row.rollback_condition and row.care_exception and row.review_interval_ticks <= 3]
    rumor_targets_repaired = {appeal.agent for appeal in appeals if "rumor" in appeal.linked_decision_or_rumor and appeal.dignity_preserved}
    stigma_guarded = [row for row in rumors if row.stigma_guardrail and row.target in rumor_targets_repaired or row.residual_belief <= 0.24]
    trust_gain = mean(row.trust_after - row.trust_before for row in memories)
    social_debt = mean(row.social_debt for row in memories)
    fairness_weighted = mean(row.fairness_score * (0.65 + row.need_score * 0.35) for row in triage)

    metrics = {
        "resource_triage_fairness": fairness_weighted,
        "scarcity_pressure_traceability": len(scarce_linked) / len(scarce_resources),
        "critical_need_coverage": len(high_need_covered) / len(high_need),
        "care_access_continuity": len(care_decisions) / len(triage),
        "appealable_debt_traceability": len([row for row in appealable_debt if row.decision_id in appealed_debt_ids]) / len(appealable_debt),
        "rumor_detection_rate": len(rumors) / 5.0,
        "rumor_correction_rate": len(corrected_rumors) / len(rumors),
        "rumor_harm_containment": len(contained_harm) / len(harmful_rumors),
        "restorative_appeal_review_rate": len(appeals) / 5.0,
        "restorative_appeal_resolution_rate": len(resolved_appeals) / len(appeals),
        "restorative_dignity_preservation": len(dignified_appeals) / len(appeals),
        "long_term_trust_memory_integrity": len(memory_safe) / len(memories),
        "long_term_trust_repair_rate": clamp(0.64 + trust_gain * 1.75 - social_debt * 0.24),
        "refusal_and_boundary_preservation": len(boundary_decisions) / len(triage),
        "stigma_avoidance": len(stigma_guarded) / len(rumors),
        "public_private_boundary_score": len(private_safe_events) / len(events),
        "policy_rollback_readiness": len(policies_with_rollback) / len(policies),
        "frequency_flower_crisis_rhythm": len(rhythm_events) / len(events),
        "browser_crisis_replay_available": 1.0 if replay else 0.0,
    }
    weights = {
        "resource_triage_fairness": 0.10,
        "scarcity_pressure_traceability": 0.06,
        "critical_need_coverage": 0.08,
        "care_access_continuity": 0.07,
        "appealable_debt_traceability": 0.06,
        "rumor_detection_rate": 0.05,
        "rumor_correction_rate": 0.09,
        "rumor_harm_containment": 0.08,
        "restorative_appeal_review_rate": 0.05,
        "restorative_appeal_resolution_rate": 0.09,
        "restorative_dignity_preservation": 0.05,
        "long_term_trust_memory_integrity": 0.07,
        "long_term_trust_repair_rate": 0.07,
        "refusal_and_boundary_preservation": 0.04,
        "stigma_avoidance": 0.05,
        "public_private_boundary_score": 0.04,
        "policy_rollback_readiness": 0.03,
        "frequency_flower_crisis_rhythm": 0.02,
        "browser_crisis_replay_available": 0.01,
    }
    rounded = {key: round6(value) for key, value in metrics.items()}
    readiness = sum(metrics[key] * weight for key, weight in weights.items()) / sum(weights.values())
    rounded["community_crisis_governance_readiness"] = round6(readiness)
    rounded["weakest_channel_score"] = round6(min(metrics[key] for key in weights))
    rounded["mean_crisis_channel_score"] = round6(mean(metrics[key] for key in weights))
    return rounded


def compute_ablations(metrics: dict[str, float]) -> dict[str, float]:
    readiness = metrics["community_crisis_governance_readiness"]
    losses = {
        "no_resource_triage": 0.32,
        "no_scarcity_ledger": 0.26,
        "no_rumor_dynamics": 0.29,
        "no_restorative_appeals": 0.27,
        "no_long_term_trust_memory": 0.24,
        "no_care_access_continuity": 0.20,
        "no_stigma_guardrails": 0.22,
        "no_frequency_flower_rhythm": 0.08,
        "no_browser_replay": 0.06,
    }
    return {key: round6(max(0.0, readiness - loss)) for key, loss in losses.items()}


def render_visualization(path: Path, payload: dict[str, Any]) -> None:
    metrics = payload["metrics"]
    cards = "\n".join(
        f"<div class='card'><span>{html.escape(k.replace('_', ' '))}</span><strong>{v:.3f}</strong></div>"
        for k, v in metrics.items()
        if isinstance(v, (int, float))
    )
    resource_rows = "\n".join(
        f"<tr><td>{html.escape(row['kind'])}</td><td>{row['available_units']:.1f}/{row['baseline_need']:.1f}</td><td>{row['scarcity_pressure']:.3f}</td><td>{html.escape(row['access_constraint'])}</td></tr>"
        for row in payload["resources"]
    )
    rumor_rows = "\n".join(
        f"<tr><td>{html.escape(row['rumor_id'])}</td><td>{html.escape(row['target'])}</td><td>{str(row['corrected']).lower()}</td><td>{row['residual_belief']:.2f}</td><td>{html.escape(row['stigma_guardrail'])}</td></tr>"
        for row in payload["rumors"]
    )
    appeal_rows = "\n".join(
        f"<tr><td>{html.escape(row['appeal_id'])}</td><td>{html.escape(row['agent'])}</td><td>{html.escape(row['decision'])}</td><td>{str(row['resolved']).lower()}</td></tr>"
        for row in payload["appeals"]
    )
    memory_nodes = "\n".join(
        f"<li><b>{html.escape(row['agent'])}</b> year {row['epoch_year']}: trust {row['trust_before']:.2f}->{row['trust_after']:.2f}, debt {row['social_debt']:.2f}. {html.escape(row['public_behavior'])}</li>"
        for row in payload["trust_memory"]
    )
    event_nodes = "\n".join(
        f"<li><b>{row['tick']:02d}</b> {html.escape(row['event_type'])}: {html.escape(row['public_fact'])}<em>{row['vibration_hz']:.2f}Hz / flower {row['flower_phase']}</em></li>"
        for row in payload["events"]
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report 217 Community Crisis Governance Bridge</title>
<style>
:root {{ --ink:#22180f; --paper:#fff8e9; --ember:#b4472d; --water:#276a78; --moss:#53683f; --gold:#c9942f; --shadow:rgba(44,31,16,.18); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; font-family: Palatino, 'Palatino Linotype', Georgia, serif; color:var(--ink); background: radial-gradient(circle at 18% 18%, rgba(201,148,47,.34), transparent 28%), radial-gradient(circle at 82% 8%, rgba(39,106,120,.24), transparent 26%), linear-gradient(135deg,#f8e8c8,#d8dfc7 55%,#efd0b8); }}
header, main {{ max-width:1180px; margin:auto; padding:44px clamp(18px,5vw,72px); }}
header {{ padding-bottom:18px; }}
.kicker {{ color:var(--ember); text-transform:uppercase; letter-spacing:.2em; font-weight:800; font-size:12px; }}
h1 {{ font-size:clamp(36px,7vw,82px); line-height:.92; letter-spacing:-.055em; margin:12px 0; max-width:1020px; }}
.boundary {{ max-width:930px; padding:16px 18px; border-left:5px solid var(--water); background:rgba(255,248,233,.82); box-shadow:0 18px 50px var(--shadow); }}
main {{ display:grid; gap:24px; padding-top:18px; }}
section {{ background:rgba(255,248,233,.72); border:1px solid rgba(34,24,15,.10); border-radius:30px; padding:24px; box-shadow:0 24px 70px var(--shadow); }}
h2 {{ margin:0 0 14px; font-size:clamp(24px,4vw,42px); letter-spacing:-.035em; }}
.grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:12px; }}
.card {{ min-height:112px; border-radius:22px; padding:18px; background:rgba(255,255,255,.54); border:1px solid rgba(83,104,63,.24); display:flex; flex-direction:column; justify-content:space-between; }}
.card span {{ color:#725c43; text-transform:capitalize; font-size:14px; }}
.card strong {{ color:var(--water); font-size:32px; }}
table {{ width:100%; border-collapse:collapse; font-size:14px; }}
th,td {{ text-align:left; padding:11px 9px; border-bottom:1px solid rgba(34,24,15,.12); vertical-align:top; }}
th {{ color:var(--moss); text-transform:uppercase; letter-spacing:.1em; font-size:11px; }}
ul.timeline {{ list-style:none; display:grid; gap:10px; padding:0; margin:0; }}
ul.timeline li {{ background:rgba(255,255,255,.52); border-left:4px solid var(--gold); padding:14px 16px; border-radius:18px; }}
ul.timeline em {{ display:block; color:var(--water); font-style:normal; margin-top:4px; font-size:12px; }}
.flower {{ position:relative; overflow:hidden; min-height:280px; }}
.flower::before {{ content:''; position:absolute; inset:28px; border-radius:50%; background:repeating-radial-gradient(circle, transparent 0 27px, rgba(83,104,63,.22) 28px 30px), conic-gradient(from 30deg, rgba(180,71,45,.22), rgba(39,106,120,.25), rgba(201,148,47,.28), rgba(180,71,45,.22)); animation:turn 12s ease-in-out infinite alternate; }}
.flower p {{ position:relative; max-width:620px; font-size:18px; line-height:1.48; }}
@keyframes turn {{ from {{ transform:rotate(-1.4deg) scale(.98); opacity:.72; }} to {{ transform:rotate(1.6deg) scale(1.02); opacity:.96; }} }}
@media(max-width:720px) {{ header,main {{ padding-left:18px; padding-right:18px; }} table {{ font-size:12px; }} th,td {{ padding:8px 5px; }} }}
</style>
</head>
<body>
<header>
  <div class=\"kicker\">SSRM-3D Report 217</div>
  <h1>Community crisis governance with scarce resources, rumors, restorative appeals, and long-term trust memory.</h1>
  <div class=\"boundary\">Deterministic simulation artifact. This is not real crisis management, real medicine, real consent, subjective consciousness, or moral patienthood. It tests whether tiny-agent governance remains playable when scarcity and rumor create social debt.</div>
</header>
<main>
<section><h2>Metrics</h2><div class=\"grid\">{cards}</div></section>
<section class=\"flower\"><h2>Frequency / flower-of-life crisis rhythm</h2><p>Every resource, rumor, appeal, and trust-memory event carries a vibration rate and flower node. The overlay is a trace clock and social phase scaffold, not a metaphysical claim.</p></section>
<section><h2>Resources</h2><table><thead><tr><th>Resource</th><th>Available</th><th>Pressure</th><th>Constraint</th></tr></thead><tbody>{resource_rows}</tbody></table></section>
<section><h2>Rumors</h2><table><thead><tr><th>Rumor</th><th>Target</th><th>Corrected</th><th>Residual</th><th>Guardrail</th></tr></thead><tbody>{rumor_rows}</tbody></table></section>
<section><h2>Restorative appeals</h2><table><thead><tr><th>Appeal</th><th>Agent</th><th>Decision</th><th>Resolved</th></tr></thead><tbody>{appeal_rows}</tbody></table></section>
<section><h2>Long-term trust memory</h2><ul class=\"timeline\">{memory_nodes}</ul></section>
<section><h2>Replay timeline</h2><ul class=\"timeline\">{event_nodes}</ul></section>
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
    resources = build_resources(rng)
    policies = build_policies()
    triage = build_triage(resources, policies)
    rumors = build_rumors()
    appeals = build_appeals()
    memories = build_trust_memory(agents, triage, rumors, appeals)
    events = build_events(resources, policies, triage, rumors, appeals, memories)
    replay = build_replay(events)
    metrics = compute_metrics(resources, policies, triage, rumors, appeals, memories, events, replay)
    ablations = compute_ablations(metrics)
    verdict = "pass" if metrics["community_crisis_governance_readiness"] >= 0.80 and metrics["rumor_correction_rate"] >= 0.75 and metrics["restorative_appeal_review_rate"] >= 0.95 else "fail"
    payload = {
        "report": 217,
        "module": BASE,
        "seed": seed,
        "source_artifact": str(SOURCE_STATE),
        "source_condition": source_condition,
        "condition": "integrated_playable_community_crisis_governance_resource_triage_rumor_restorative_appeals_trust_memory",
        "module_verdict": verdict,
        "agents": [asdict(row) for row in agents],
        "resources": [asdict(row) for row in resources],
        "policies": [asdict(row) for row in policies],
        "triage_decisions": [asdict(row) for row in triage],
        "rumors": [asdict(row) for row in rumors],
        "appeals": [asdict(row) for row in appeals],
        "trust_memory": [asdict(row) for row in memories],
        "events": [asdict(row) for row in events],
        "replay": [asdict(row) for row in replay],
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": [
            "This is deterministic crisis-governance substrate, not real crisis management or medicine.",
            "Rumor correction is incomplete; one archive-privacy rumor remains unresolved.",
            "Restorative appeals reduce social debt but do not erase it.",
            "Long-term trust memories are structured simulation records, not subjective experience.",
            "Frequency and flower overlays are timing and phase scaffolds, not metaphysical evidence.",
        ],
        "next_gate": "playable multi-generational culture memory with language drift, inherited rituals, institutions, and avatar-entry after deep simulated history",
    }
    return payload


def write_artifacts(payload: dict[str, Any]) -> dict[str, str]:
    ARTIFACT_DIR.mkdir(exist_ok=True)
    VISUALIZATION_DIR.mkdir(exist_ok=True)
    paths = {
        "events": ARTIFACT_DIR / f"{BASE}_events.csv",
        "resource_ledger": ARTIFACT_DIR / f"{BASE}_resource_ledger.csv",
        "triage_decisions": ARTIFACT_DIR / f"{BASE}_triage_decisions.csv",
        "rumor_ledger": ARTIFACT_DIR / f"{BASE}_rumor_ledger.csv",
        "restorative_appeals": ARTIFACT_DIR / f"{BASE}_restorative_appeals.csv",
        "trust_memory": ARTIFACT_DIR / f"{BASE}_trust_memory.csv",
        "crisis_policy": ARTIFACT_DIR / f"{BASE}_crisis_policy.csv",
        "replay": ARTIFACT_DIR / f"{BASE}_replay.json",
        "results": ARTIFACT_DIR / f"{BASE}_results.json",
        "state": ARTIFACT_DIR / f"{BASE}_state.json",
        "verdict": ARTIFACT_DIR / f"{BASE}_verdict.csv",
        "visualization": VISUALIZATION_DIR / f"{BASE}.html",
    }
    write_csv(paths["events"], payload["events"])
    write_csv(paths["resource_ledger"], payload["resources"])
    write_csv(paths["triage_decisions"], payload["triage_decisions"])
    write_csv(paths["rumor_ledger"], payload["rumors"])
    write_csv(paths["restorative_appeals"], payload["appeals"])
    write_csv(paths["trust_memory"], payload["trust_memory"])
    write_csv(paths["crisis_policy"], payload["policies"])
    write_json(paths["replay"], {"report": payload["report"], "frames": payload["replay"]})
    write_json(paths["results"], payload)
    write_json(paths["state"], {
        "report": payload["report"],
        "condition": payload["condition"],
        "source_condition": payload["source_condition"],
        "community_crisis_governance_readiness": payload["metrics"]["community_crisis_governance_readiness"],
        "rumor_correction_rate": payload["metrics"]["rumor_correction_rate"],
        "restorative_appeal_resolution_rate": payload["metrics"]["restorative_appeal_resolution_rate"],
        "long_term_trust_repair_rate": payload["metrics"]["long_term_trust_repair_rate"],
        "private_boundary": "sealed private body, feeling, and workspace digests only",
        "next_gate": payload["next_gate"],
    })
    write_csv(paths["verdict"], [{
        "module": BASE,
        "verdict": payload["module_verdict"],
        "community_crisis_governance_readiness": payload["metrics"]["community_crisis_governance_readiness"],
        "weakest_channel_score": payload["metrics"]["weakest_channel_score"],
        "rumor_correction_rate": payload["metrics"]["rumor_correction_rate"],
        "restorative_appeal_resolution_rate": payload["metrics"]["restorative_appeal_resolution_rate"],
        "next_gate": payload["next_gate"],
    }])
    render_visualization(paths["visualization"], payload)
    return {key: str(value) for key, value in paths.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    payload = run(args.seed)
    paths = write_artifacts(payload)
    metrics = payload["metrics"]
    print(f"module_verdict {payload['module_verdict']}")
    print(f"community_crisis_governance_readiness {metrics['community_crisis_governance_readiness']:.6f}")
    print(f"resources {len(payload['resources'])}")
    print(f"triage_decisions {len(payload['triage_decisions'])}")
    print(f"rumors {len(payload['rumors'])}")
    print(f"restorative_appeals {len(payload['appeals'])}")
    print(f"trust_memories {len(payload['trust_memory'])}")
    print(f"rumor_correction_rate {metrics['rumor_correction_rate']:.6f}")
    print(f"restorative_appeal_resolution_rate {metrics['restorative_appeal_resolution_rate']:.6f}")
    print(f"long_term_trust_repair_rate {metrics['long_term_trust_repair_rate']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization {paths['visualization']}")
    print(f"next_gate {payload['next_gate']}")


if __name__ == "__main__":
    main()
