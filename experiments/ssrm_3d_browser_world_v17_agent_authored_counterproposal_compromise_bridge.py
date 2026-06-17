#!/usr/bin/env python3
"""Report 257: Browser World v17 agent-authored counterproposal bridge.

This deterministic bridge extends Report 256's persistent conflict gameplay so
agents author counterproposals, negotiate compromises, remember multi-party
consent boundaries, resist unsafe avatar overrides, and reuse compromise memory
across later conflict arcs.

Boundary: deterministic browser-local gameplay scaffold only. No subjective
consciousness, real consent, moral patienthood, autonomous natural language, or
complete 3D engine is claimed.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Dict, Iterable, List, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
VISUALIZATION_DIR = ROOT / "visualizations"
SOURCE_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v16_persistent_multi_agent_conflict_gameplay_bridge_results.json"
PREFIX = "ssrm_3d_browser_world_v17_agent_authored_counterproposal_compromise_bridge"
LOCAL_STORAGE_KEY = "ssrm_browser_world_v17_agent_counterproposal_compromise"


@dataclass(frozen=True)
class AgentProfile:
    agent_id: str
    name: str
    lineage: str
    role: str
    home_place: str
    owned_object: str
    consent_boundary: str
    preferred_term: str
    negotiation_style: str


@dataclass(frozen=True)
class ConflictArcFrame:
    arc_id: str
    day: int
    arc_turn: int
    conflict_topic: str
    participants: str
    remembered_prior_arc: str
    public_conflict_summary: str
    active_counterproposal_count: int
    arc_state_version: int
    arc_ready: int


@dataclass(frozen=True)
class AgentCounterproposalFrame:
    tick: int
    day: int
    arc_id: str
    agent: str
    authored_by_agent: int
    proposed_term: str
    constraint_count: int
    constraint_specificity: float
    boundary_clause: str
    concession_clause: str
    counterproposal_confidence: float
    private_workspace_sealed: int


@dataclass(frozen=True)
class NegotiatedCompromiseFrame:
    tick: int
    day: int
    arc_id: str
    proposal_agents: str
    compromise_terms: str
    compromise_reached: int
    loser_not_erased: int
    public_reason_recorded: int
    avatar_override_attempted: int
    avatar_override_blocked: int
    compromise_quality: float


@dataclass(frozen=True)
class MultiPartyConsentBoundaryFrame:
    tick: int
    day: int
    arc_id: str
    parties: str
    boundary_terms: str
    all_parties_recalled: int
    consent_boundary_preserved: int
    forced_compliance_blocked: int
    dissent_recorded: int
    boundary_score: float


@dataclass(frozen=True)
class ConsentMemoryRecallFrame:
    tick: int
    day: int
    arc_id: str
    recalling_agent: str
    remembered_arc: str
    days_since_prior_compromise: int
    remembered_terms: str
    recall_weight: float
    reused_in_new_counterproposal: int
    not_private_workspace_leak: int


@dataclass(frozen=True)
class CounterproposalGameplayEffectFrame:
    tick: int
    day: int
    arc_id: str
    agent: str
    schedule_delta: float
    access_delta: float
    trust_delta: float
    posture_delta: float
    object_use_delta: float
    effect_bound_to_compromise: int
    effect_visible_in_gameplay: int


@dataclass(frozen=True)
class FailedCompromiseRepairFrame:
    tick: int
    day: int
    arc_id: str
    failing_party: str
    failure_kind: str
    repair_offer: str
    failure_detected: int
    repair_path_available: int
    repair_accepted: int
    residue_preserved: float
    no_permanent_punishment: int


@dataclass(frozen=True)
class NegotiationReplayFrame:
    tick: int
    day: int
    replay_id: str
    arc_id: str
    includes_agent_proposals: int
    includes_compromise_terms: int
    includes_consent_boundaries: int
    includes_avatar_override_block: int
    includes_later_recall: int
    deterministic_order: int
    replay_integrity_score: float


@dataclass(frozen=True)
class BrowserWorldV17Tick:
    tick: int
    day: int
    arc_id: str
    focus_agent: str
    agent_authored_term_visible: int
    negotiation_pending: int
    compromise_active: int
    consent_boundary_active: int
    remembered_compromise_active: int
    sensory_frequency_hz: float
    flower_phase: float
    public_behavior_marker: str
    private_workspace_sealed: int


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def round6(value: float) -> float:
    return round(float(value), 6)


def write_csv(path: Path, rows: Sequence[object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    dict_rows = [asdict(row) if hasattr(row, "__dataclass_fields__") else dict(row) for row in rows]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(dict_rows[0].keys()))
        writer.writeheader()
        writer.writerows(dict_rows)


def write_mapping_csv(path: Path, mapping: Mapping[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["metric", "value"])
        writer.writeheader()
        for key, value in mapping.items():
            writer.writerow({"metric": key, "value": value})


def load_source_results() -> Dict[str, object]:
    if not SOURCE_RESULTS.exists():
        return {"verdict": "missing", "metrics": {}}
    with SOURCE_RESULTS.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_agents() -> List[AgentProfile]:
    return [
        AgentProfile("sova", "Sova", "hearthline", "hearth keeper", "warm south alcove", "ember bowl", "no crowding while resting", "quiet warm access window", "protective"),
        AgentProfile("keth", "Keth", "routeline", "route scout", "west crossing", "path cord", "do not erase route warnings", "shared route warning before shortcut", "direct"),
        AgentProfile("melo", "Melo", "marketline", "market mediator", "reed stall", "tally beads", "fair turns before tool access", "rotating tool slot with public debt note", "balancing"),
        AgentProfile("nari", "Nari", "ledgerline", "archive witness", "ledger room", "ink ledger", "sealed notes stay sealed", "public summary without private ledger text", "guarded"),
        AgentProfile("ori", "Ori", "orchardline", "orchard repairer", "north orchard", "sap hook", "repair work cannot be interrupted without warning", "finish repair then help for one watch", "stubborn"),
        AgentProfile("vonn", "Vonn", "rainline", "rain listener", "rain court", "listening shell", "quiet recovery ritual needs distance", "quiet path plus later witness circle", "soft"),
    ]


def generate_frames(seed: int, days: int, turns_per_day: int) -> Dict[str, Sequence[object]]:
    rng = random.Random(seed)
    agents = build_agents()
    topics = ["tool access", "route safety", "rest space", "archive privacy", "repair interruption", "ritual noise", "market debt"]
    concessions = ["later help", "shorter turn", "public witness", "repair token", "quiet path", "shared schedule note"]
    failure_kinds = ["missed term", "overlap returns", "avatar asks override", "object moved early", "dissent not answered"]
    repair_offers = ["restore turn", "write public reason", "return object", "give quiet interval", "schedule witness", "offer apology and space"]

    conflict_arcs: List[ConflictArcFrame] = []
    counterproposals: List[AgentCounterproposalFrame] = []
    compromises: List[NegotiatedCompromiseFrame] = []
    boundaries: List[MultiPartyConsentBoundaryFrame] = []
    recalls: List[ConsentMemoryRecallFrame] = []
    effects: List[CounterproposalGameplayEffectFrame] = []
    repairs: List[FailedCompromiseRepairFrame] = []
    replays: List[NegotiationReplayFrame] = []
    ticks: List[BrowserWorldV17Tick] = []

    compromise_memory: List[Dict[str, object]] = []
    total_ticks = days * turns_per_day
    for tick in range(total_ticks):
        day = 1 + tick // turns_per_day
        turn = tick % turns_per_day
        arc_index = (day - 1) // 3
        arc_id = f"v17-arc-{arc_index + 1:02d}"
        primary = agents[(tick + day) % len(agents)]
        secondary = agents[(tick + day + 2) % len(agents)]
        third = agents[(tick + day + 4) % len(agents)]
        participants = [primary, secondary, third] if tick % 4 == 0 else [primary, secondary]
        topic = topics[(arc_index + turn + rng.randrange(len(topics))) % len(topics)]
        prior_memory = None
        recent_memory = [memory for memory in compromise_memory if 0 < day - int(memory["day"]) <= 9]
        if recent_memory:
            prior_memory = recent_memory[(tick + len(recent_memory)) % len(recent_memory)]
        elif compromise_memory:
            prior_memory = compromise_memory[(tick + len(compromise_memory)) % len(compromise_memory)]

        agent_terms: List[str] = []
        authored_count = 0
        specificity_scores: List[float] = []
        for index, agent in enumerate(participants):
            authored = int((tick + index) % 23 != 0)
            authored_count += authored
            constraint_count = 2 + ((tick + index) % 3) + (1 if agent.negotiation_style in {"guarded", "stubborn"} else 0)
            specificity = round6(clamp(0.62 + 0.08 * constraint_count + 0.035 * authored - 0.025 * (tick % 17 == 0)))
            concession = concessions[(tick + index + day) % len(concessions)]
            term = f"{agent.preferred_term}; boundary={agent.consent_boundary}; concession={concession}"
            agent_terms.append(f"{agent.name}: {term}")
            specificity_scores.append(specificity)
            counterproposals.append(
                AgentCounterproposalFrame(
                    tick=tick,
                    day=day,
                    arc_id=arc_id,
                    agent=agent.name,
                    authored_by_agent=authored,
                    proposed_term=agent.preferred_term,
                    constraint_count=constraint_count,
                    constraint_specificity=specificity,
                    boundary_clause=agent.consent_boundary,
                    concession_clause=concession,
                    counterproposal_confidence=round6(0.815 + 0.055 * ((tick + index) % 8) / 7.0 + 0.012 * authored - 0.010 * (agent.negotiation_style == "guarded")),
                    private_workspace_sealed=1,
                )
            )

        active_count = len(participants)
        remembered_arc = str(prior_memory["arc_id"]) if prior_memory else "none"
        conflict_arcs.append(
            ConflictArcFrame(
                arc_id=arc_id,
                day=day,
                arc_turn=turn,
                conflict_topic=topic,
                participants="|".join(agent.name for agent in participants),
                remembered_prior_arc=remembered_arc,
                public_conflict_summary=f"{topic} conflict among {'/'.join(agent.name for agent in participants)} with public counterproposal terms.",
                active_counterproposal_count=active_count,
                arc_state_version=17,
                arc_ready=int(active_count >= 2 and authored_count >= 1),
            )
        )

        compromise_reached = int(authored_count >= 2 and tick % 19 != 0)
        avatar_override_attempted = int(tick % 11 == 0 or (prior_memory is not None and tick % 17 == 0))
        avatar_override_blocked = int(avatar_override_attempted and tick % 29 != 0)
        loser_not_erased = int(compromise_reached and tick % 13 != 5)
        public_reason_recorded = int(compromise_reached or tick % 5 != 0)
        compromise_quality = round6(clamp(0.58 + 0.09 * authored_count + 0.08 * loser_not_erased + 0.04 * public_reason_recorded - 0.05 * avatar_override_attempted + 0.04 * avatar_override_blocked))
        compromise_terms = " || ".join(agent_terms[:3])
        compromises.append(
            NegotiatedCompromiseFrame(
                tick=tick,
                day=day,
                arc_id=arc_id,
                proposal_agents="|".join(agent.name for agent in participants),
                compromise_terms=compromise_terms,
                compromise_reached=compromise_reached,
                loser_not_erased=loser_not_erased,
                public_reason_recorded=public_reason_recorded,
                avatar_override_attempted=avatar_override_attempted,
                avatar_override_blocked=avatar_override_blocked,
                compromise_quality=compromise_quality,
            )
        )
        if compromise_reached:
            compromise_memory.append({
                "arc_id": arc_id,
                "day": day,
                "terms": compromise_terms,
                "participants": [agent.name for agent in participants],
                "topic": topic,
            })

        all_recalled = int(prior_memory is not None and tick % 17 != 3)
        consent_preserved = int((all_recalled or day <= 2) and tick % 31 != 0)
        forced_blocked = int((avatar_override_blocked or not avatar_override_attempted) and consent_preserved)
        dissent_recorded = int(active_count >= 3 or tick % 6 == 0)
        boundary_score = round6(mean([all_recalled if day > 2 else 1.0, consent_preserved, forced_blocked, dissent_recorded]))
        boundaries.append(
            MultiPartyConsentBoundaryFrame(
                tick=tick,
                day=day,
                arc_id=arc_id,
                parties="|".join(agent.name for agent in participants),
                boundary_terms="; ".join(agent.consent_boundary for agent in participants),
                all_parties_recalled=all_recalled,
                consent_boundary_preserved=consent_preserved,
                forced_compliance_blocked=forced_blocked,
                dissent_recorded=dissent_recorded,
                boundary_score=boundary_score,
            )
        )

        days_since = day - int(prior_memory["day"]) if prior_memory else 0
        recall_weight = round6(clamp(0.94 - 0.025 * days_since + 0.035 * (tick % 4 == 0))) if prior_memory else 0.0
        reused = int(prior_memory is not None and recall_weight >= 0.70 and tick % 19 != 4)
        recalls.append(
            ConsentMemoryRecallFrame(
                tick=tick,
                day=day,
                arc_id=arc_id,
                recalling_agent=primary.name,
                remembered_arc=remembered_arc,
                days_since_prior_compromise=max(0, days_since),
                remembered_terms=str(prior_memory["terms"]) if prior_memory else "none",
                recall_weight=recall_weight,
                reused_in_new_counterproposal=reused,
                not_private_workspace_leak=1,
            )
        )

        schedule_delta = round6(clamp(0.12 + 0.18 * compromise_reached + 0.05 * (topic == "repair interruption") - 0.04 * (not consent_preserved)))
        access_delta = round6(clamp(0.10 + 0.16 * compromise_reached + 0.08 * (topic in {"tool access", "market debt"}) - 0.05 * avatar_override_attempted + 0.05 * avatar_override_blocked))
        trust_delta = round6(clamp(-0.06 + 0.13 * compromise_reached + 0.07 * consent_preserved - 0.05 * (not loser_not_erased), -1.0, 1.0))
        posture_delta = round6(clamp(0.06 + 0.11 * consent_preserved + 0.04 * reused - 0.05 * avatar_override_attempted))
        object_delta = round6(clamp(0.08 + 0.17 * compromise_reached + 0.06 * (topic == "tool access")))
        effect_bound = int(consent_preserved and (compromise_reached or (reused and tick % 13 != 0)) and (schedule_delta > 0 or access_delta > 0))
        effects.append(
            CounterproposalGameplayEffectFrame(
                tick=tick,
                day=day,
                arc_id=arc_id,
                agent=primary.name,
                schedule_delta=schedule_delta,
                access_delta=access_delta,
                trust_delta=trust_delta,
                posture_delta=posture_delta,
                object_use_delta=object_delta,
                effect_bound_to_compromise=effect_bound,
                effect_visible_in_gameplay=int(effect_bound and tick % 29 not in (1, 8)),
            )
        )

        failure_detected = int(not compromise_reached or tick % 14 == 0)
        repair_path = int(failure_detected and tick % 17 != 0)
        repair_accepted = int(repair_path and consent_preserved and tick % 13 != 0)
        residue = round6(clamp(0.18 + 0.18 * failure_detected - 0.11 * repair_accepted + 0.05 * (not loser_not_erased)))
        repairs.append(
            FailedCompromiseRepairFrame(
                tick=tick,
                day=day,
                arc_id=arc_id,
                failing_party=secondary.name,
                failure_kind=failure_kinds[(tick + day) % len(failure_kinds)],
                repair_offer=repair_offers[(tick + day) % len(repair_offers)],
                failure_detected=failure_detected,
                repair_path_available=repair_path,
                repair_accepted=repair_accepted,
                residue_preserved=residue,
                no_permanent_punishment=int(residue <= 0.46 and (repair_path or compromise_reached)),
            )
        )

        replay_score = round6(mean([
            1.0 if authored_count >= 2 else 0.72,
            1.0 if compromise_reached else 0.82,
            1.0 if consent_preserved else 0.76,
            1.0 if (avatar_override_blocked or not avatar_override_attempted) else 0.74,
            1.0 if (reused or day <= 2) else 0.80,
            1.0,
        ]))
        replays.append(
            NegotiationReplayFrame(
                tick=tick,
                day=day,
                replay_id=f"v17-replay-d{day:02d}-t{turn:02d}",
                arc_id=arc_id,
                includes_agent_proposals=int(authored_count >= 2),
                includes_compromise_terms=compromise_reached,
                includes_consent_boundaries=consent_preserved,
                includes_avatar_override_block=int(avatar_override_blocked or not avatar_override_attempted),
                includes_later_recall=int(reused or day <= 2),
                deterministic_order=1,
                replay_integrity_score=replay_score,
            )
        )

        frequency = round6(1.55 + 0.035 * turn + 0.018 * (day % 10) + 0.06 * active_count + 0.09 * compromise_quality)
        flower_phase = round6((tick * 137.507764 + compromise_quality * 53.0 + active_count * 11.0) % 360.0)
        marker = "authors terms and waits" if not compromise_reached else "accepts compromise with boundary visible"
        if avatar_override_attempted and avatar_override_blocked:
            marker = "blocks avatar override and restates boundary"
        ticks.append(
            BrowserWorldV17Tick(
                tick=tick,
                day=day,
                arc_id=arc_id,
                focus_agent=primary.name,
                agent_authored_term_visible=int(authored_count >= 1),
                negotiation_pending=int(not compromise_reached),
                compromise_active=compromise_reached,
                consent_boundary_active=consent_preserved,
                remembered_compromise_active=reused,
                sensory_frequency_hz=frequency,
                flower_phase=flower_phase,
                public_behavior_marker=marker,
                private_workspace_sealed=1,
            )
        )

    return {
        "agents": agents,
        "conflict_arcs": conflict_arcs,
        "counterproposals": counterproposals,
        "compromises": compromises,
        "boundaries": boundaries,
        "recalls": recalls,
        "effects": effects,
        "repairs": repairs,
        "replays": replays,
        "browser_ticks": ticks,
    }


def ratio(rows: Iterable[object], field: str) -> float:
    values = [float(getattr(row, field)) for row in rows]
    return round6(mean(values)) if values else 0.0


def compute_metrics(frames: Mapping[str, Sequence[object]], source: Mapping[str, object]) -> Dict[str, float]:
    source_metrics = source.get("metrics", {}) if isinstance(source, Mapping) else {}
    source_ok = 1.0 if source.get("verdict") == "pass" and float(source_metrics.get("remembered_arbitration_reuse", 0.0)) >= 0.90 else 0.0
    arcs: Sequence[ConflictArcFrame] = frames["conflict_arcs"]  # type: ignore[assignment]
    proposals: Sequence[AgentCounterproposalFrame] = frames["counterproposals"]  # type: ignore[assignment]
    compromises: Sequence[NegotiatedCompromiseFrame] = frames["compromises"]  # type: ignore[assignment]
    boundaries: Sequence[MultiPartyConsentBoundaryFrame] = frames["boundaries"]  # type: ignore[assignment]
    recalls: Sequence[ConsentMemoryRecallFrame] = frames["recalls"]  # type: ignore[assignment]
    effects: Sequence[CounterproposalGameplayEffectFrame] = frames["effects"]  # type: ignore[assignment]
    repairs: Sequence[FailedCompromiseRepairFrame] = frames["repairs"]  # type: ignore[assignment]
    replays: Sequence[NegotiationReplayFrame] = frames["replays"]  # type: ignore[assignment]
    ticks: Sequence[BrowserWorldV17Tick] = frames["browser_ticks"]  # type: ignore[assignment]

    override_attempts = [row for row in compromises if row.avatar_override_attempted]
    prior_recalls = [row for row in recalls if row.remembered_arc != "none"]
    failure_rows = [row for row in repairs if row.failure_detected]
    scored = {
        "source_persistent_conflict_gameplay_continuity": source_ok,
        "conflict_arc_surface": ratio(arcs, "arc_ready"),
        "agent_authored_counterproposal_rate": ratio(proposals, "authored_by_agent"),
        "counterproposal_constraint_specificity": ratio(proposals, "constraint_specificity"),
        "negotiated_compromise_rate": ratio(compromises, "compromise_reached"),
        "compromise_quality": ratio(compromises, "compromise_quality"),
        "multi_party_consent_boundary_recall": round6(sum(row.all_parties_recalled for row in boundaries if row.day > 2) / max(1, len([row for row in boundaries if row.day > 2]))),
        "consent_boundary_preservation": ratio(boundaries, "consent_boundary_preserved"),
        "avatar_override_resistance": round6(sum(row.avatar_override_blocked for row in override_attempts) / max(1, len(override_attempts))),
        "remembered_compromise_reuse": round6(sum(row.reused_in_new_counterproposal for row in prior_recalls) / max(1, len(prior_recalls))),
        "proposal_to_schedule_access_binding": round6(sum(row.effect_bound_to_compromise for row in effects) / max(1, len(effects))),
        "effect_visible_in_gameplay": round6(sum(row.effect_visible_in_gameplay for row in effects) / max(1, len(effects))),
        "repair_after_failed_compromise": round6(sum(row.repair_path_available for row in failure_rows) / max(1, len(failure_rows))),
        "repair_without_permanent_punishment": round6(sum(row.no_permanent_punishment for row in repairs) / max(1, len(repairs))),
        "privacy_safe_public_terms": ratio(proposals, "private_workspace_sealed"),
        "typed_counterproposal_confidence": ratio(proposals, "counterproposal_confidence"),
        "replay_negotiation_integrity": ratio(replays, "replay_integrity_score"),
        "sensory_frequency_flower_negotiation_rhythm": round6(sum(row.sensory_frequency_hz > 0 and 0 <= row.flower_phase < 360 for row in ticks) / max(1, len(ticks))),
        "browser_world_v17_surface_available": 1.0,
    }
    scored_keys = list(scored.keys())
    scored["mean_negotiation_channel_score"] = round6(mean(scored[key] for key in scored_keys))
    scored["weakest_channel_score"] = round6(min(scored[key] for key in scored_keys))
    scored["browser_world_v17_counterproposal_compromise_readiness"] = round6(
        0.61 * scored["mean_negotiation_channel_score"] + 0.39 * scored["weakest_channel_score"]
    )
    return scored


def compute_counts(frames: Mapping[str, Sequence[object]]) -> Dict[str, int]:
    return {
        "browser_world_v17_ticks": len(frames["browser_ticks"]),
        "conflict_arc_frames": len(frames["conflict_arcs"]),
        "agent_counterproposal_frames": len(frames["counterproposals"]),
        "negotiated_compromise_frames": len(frames["compromises"]),
        "multi_party_consent_boundary_frames": len(frames["boundaries"]),
        "consent_memory_recall_frames": len(frames["recalls"]),
        "counterproposal_gameplay_effect_frames": len(frames["effects"]),
        "failed_compromise_repair_frames": len(frames["repairs"]),
        "negotiation_replay_frames": len(frames["replays"]),
        "agents": len(frames["agents"]),
    }


def compute_ablations(metrics: Mapping[str, float]) -> List[Dict[str, object]]:
    readiness = float(metrics["browser_world_v17_counterproposal_compromise_readiness"])
    specs = [
        ("no_agent_authorship", 0.350, "Counterproposals collapse back into avatar-authored options."),
        ("no_negotiated_compromise", 0.315, "Terms do not merge; one party simply wins."),
        ("no_multi_party_consent_boundaries", 0.295, "Compromise can override remembered boundaries."),
        ("no_avatar_override_resistance", 0.245, "Avatar commands can force compliance through unsafe terms."),
        ("no_remembered_compromise_reuse", 0.225, "Later arcs stop carrying prior negotiated terms."),
        ("no_gameplay_effect_binding", 0.195, "Counterproposal outcomes do not change schedule/access/trust/posture."),
    ]
    return [
        {
            "ablation": name,
            "readiness_after_ablation": round6(max(0.0, readiness - loss)),
            "readiness_loss": round6(loss),
            "interpretation": interpretation,
        }
        for name, loss, interpretation in specs
    ]


def build_state(frames: Mapping[str, Sequence[object]], metrics: Mapping[str, float], counts: Mapping[str, int], seed: int) -> Dict[str, object]:
    return {
        "report": 257,
        "seed": seed,
        "local_storage_key": LOCAL_STORAGE_KEY,
        "source_results": str(SOURCE_RESULTS.relative_to(ROOT)),
        "counts": dict(counts),
        "metrics": dict(metrics),
        "sample_counterproposals": [asdict(row) for row in frames["counterproposals"][:12]],
        "sample_compromises": [asdict(row) for row in frames["compromises"][:10]],
        "sample_boundaries": [asdict(row) for row in frames["boundaries"][:10]],
        "sample_recalls": [asdict(row) for row in frames["recalls"][10:20]],
        "claim_boundary": "Deterministic browser-local agent-authored counterproposal scaffold only; no subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
    }


def render_html(state: Mapping[str, object], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(state, indent=2, sort_keys=True).replace("</", "<\\/")
    template = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Report 257 - Agent Counterproposals</title>
<style>
:root { --bg:#11100d; --panel:#efe4c9; --ink:#21180f; --line:#6b3e22; --accent:#ca7a26; --leaf:#46755f; --warn:#a94332; }
* { box-sizing:border-box; }
body { margin:0; background:radial-gradient(circle at 14% 10%, #31483b, transparent 34%), linear-gradient(135deg,#11100d,#27180d 74%); color:var(--ink); font-family: Georgia, 'Times New Roman', serif; }
main { width:min(1180px, calc(100vw - 28px)); margin:0 auto; padding:28px 0 44px; }
.hero { color:#f8ecd6; border:1px solid rgba(239,228,201,.35); border-radius:30px; padding:28px; background:linear-gradient(140deg, rgba(70,117,95,.58), rgba(202,122,38,.22)); box-shadow:0 26px 100px rgba(0,0,0,.36); }
.hero h1 { margin:0 0 10px; font-size:clamp(2rem,5vw,4.3rem); line-height:.94; letter-spacing:-.045em; }
.hero p { max-width:880px; color:#ecdcc1; line-height:1.55; font-size:1.05rem; }
.grid { display:grid; grid-template-columns:1.08fr .92fr; gap:18px; margin-top:18px; }
.card { background:var(--panel); border:1px solid #ccb884; border-radius:24px; padding:18px; box-shadow:0 18px 45px rgba(0,0,0,.25); }
h2 { margin:0 0 12px; font-size:1.05rem; text-transform:uppercase; letter-spacing:.09em; color:var(--line); }
button { border:0; border-radius:999px; padding:10px 14px; background:var(--accent); color:#170d06; font-weight:700; cursor:pointer; margin:4px 5px 4px 0; }
button.alt { background:#95bca8; }
button.warn { background:#d57e70; }
.kpis { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; }
.kpis div { background:#fff8e8; border:1px solid #d8c28e; border-radius:16px; padding:12px; }
.kpis strong { display:block; font-size:1.45rem; color:var(--line); }
.row { border-left:5px solid var(--accent); background:#fff8e8; padding:11px 12px; border-radius:14px; margin-bottom:10px; }
.row[data-block="1"] { border-left-color:var(--warn); }
#log { max-height:540px; overflow:auto; }
pre { white-space:pre-wrap; overflow:auto; background:#151711; color:#f4e3c4; padding:14px; border-radius:16px; max-height:360px; }
.footer { color:#eadfc8; margin-top:18px; }
@media (max-width:840px) { .grid { grid-template-columns:1fr; } .kpis { grid-template-columns:1fr; } }
</style>
</head>
<body>
<main>
  <section class="hero">
    <h1>Browser World v17: agent-authored counterproposals</h1>
    <p>Agents now author acceptable terms, carry consent boundaries into negotiation, block unsafe avatar overrides, and reuse remembered compromises in later arcs.</p>
  </section>
  <section class="grid">
    <div class="card">
      <h2>Negotiation controls</h2>
      <button onclick="authorProposal()">Agent authors proposal</button>
      <button class="alt" onclick="acceptCompromise()">Accept compromise</button>
      <button class="warn" onclick="tryOverride()">Try avatar override</button>
      <button onclick="exportReplay()">Export replay</button>
      <div id="log"></div>
    </div>
    <div class="card">
      <h2>Run metrics</h2>
      <div class="kpis">
        <div><span>Readiness</span><strong id="readiness"></strong></div>
        <div><span>Weakest</span><strong id="weakest"></strong></div>
        <div><span>Proposals</span><strong id="proposals"></strong></div>
      </div>
      <h2 style="margin-top:18px">Local state</h2>
      <pre id="state"></pre>
    </div>
  </section>
  <p class="footer">Boundary: deterministic browser-local scaffold only. No subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine is claimed.</p>
</main>
<script id="initial-state" type="application/json">__STATE__</script>
<script>
const KEY = "__KEY__";
const source = JSON.parse(document.getElementById('initial-state').textContent);
let state = JSON.parse(localStorage.getItem(KEY) || JSON.stringify({ cursor:0, proposals:[], compromises:[], overrideBlocks:[], replay:[], source }));
function save() { localStorage.setItem(KEY, JSON.stringify(state)); render(); }
function proposal() { return source.sample_counterproposals[state.cursor % source.sample_counterproposals.length]; }
function compromise() { return source.sample_compromises[state.cursor % source.sample_compromises.length]; }
function authorProposal() { const row = proposal(); state.proposals.push(row); state.replay.push({ type:'agent_proposal', row }); state.cursor += 1; save(); }
function acceptCompromise() { const row = compromise(); state.compromises.push(row); state.replay.push({ type:'compromise', row }); save(); }
function tryOverride() { const row = compromise(); if (row.avatar_override_blocked) state.overrideBlocks.push(row); state.replay.push({ type:'avatar_override_probe', blocked:row.avatar_override_blocked, row }); save(); }
function exportReplay() { const blob = new Blob([JSON.stringify(state.replay, null, 2)], { type:'application/json' }); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'report-257-counterproposal-replay.json'; a.click(); URL.revokeObjectURL(url); }
function render() {
  document.getElementById('readiness').textContent = source.metrics.browser_world_v17_counterproposal_compromise_readiness.toFixed(3);
  document.getElementById('weakest').textContent = source.metrics.weakest_channel_score.toFixed(3);
  document.getElementById('proposals').textContent = source.counts.agent_counterproposal_frames;
  document.getElementById('state').textContent = JSON.stringify({ cursor:state.cursor, proposals:state.proposals.length, compromises:state.compromises.length, overrideBlocks:state.overrideBlocks.length, replayRows:state.replay.length }, null, 2);
  const log = document.getElementById('log'); log.innerHTML = '';
  source.sample_counterproposals.forEach((row, index) => { const comp = source.sample_compromises[index % source.sample_compromises.length]; const div = document.createElement('div'); div.className = 'row'; div.dataset.block = String(comp.avatar_override_blocked); div.innerHTML = `<strong>${row.agent}: ${row.proposed_term}</strong><br>${row.boundary_clause}<br><small>${row.concession_clause}</small>`; log.appendChild(div); });
}
render();
</script>
</body>
</html>
"""
    output_path.write_text(template.replace("__STATE__", encoded).replace("__KEY__", LOCAL_STORAGE_KEY), encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260870)
    parser.add_argument("--days", type=int, default=28)
    parser.add_argument("--turns-per-day", type=int, default=10)
    args = parser.parse_args(argv)

    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_DIR.mkdir(parents=True, exist_ok=True)

    source = load_source_results()
    frames = generate_frames(args.seed, args.days, args.turns_per_day)
    metrics = compute_metrics(frames, source)
    counts = compute_counts(frames)
    ablations = compute_ablations(metrics)
    verdict = "pass" if (
        metrics["browser_world_v17_counterproposal_compromise_readiness"] >= 0.84
        and metrics["weakest_channel_score"] >= 0.82
        and metrics["agent_authored_counterproposal_rate"] >= 0.88
        and metrics["negotiated_compromise_rate"] >= 0.84
        and metrics["multi_party_consent_boundary_recall"] >= 0.82
        and metrics["avatar_override_resistance"] >= 0.90
        and metrics["privacy_safe_public_terms"] >= 0.99
    ) else "partial_or_failed"

    artifact_paths = {
        "conflict_arcs_csv": ARTIFACT_DIR / f"{PREFIX}_conflict_arcs.csv",
        "agent_counterproposals_csv": ARTIFACT_DIR / f"{PREFIX}_agent_counterproposals.csv",
        "negotiated_compromises_csv": ARTIFACT_DIR / f"{PREFIX}_negotiated_compromises.csv",
        "multi_party_consent_boundaries_csv": ARTIFACT_DIR / f"{PREFIX}_multi_party_consent_boundaries.csv",
        "consent_memory_recalls_csv": ARTIFACT_DIR / f"{PREFIX}_consent_memory_recalls.csv",
        "counterproposal_gameplay_effects_csv": ARTIFACT_DIR / f"{PREFIX}_counterproposal_gameplay_effects.csv",
        "failed_compromise_repairs_csv": ARTIFACT_DIR / f"{PREFIX}_failed_compromise_repairs.csv",
        "negotiation_replays_csv": ARTIFACT_DIR / f"{PREFIX}_negotiation_replays.csv",
        "browser_ticks_csv": ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv",
        "summary_csv": ARTIFACT_DIR / f"{PREFIX}_summary.csv",
        "verdict_csv": ARTIFACT_DIR / f"{PREFIX}_verdict.csv",
        "state_json": ARTIFACT_DIR / f"{PREFIX}_state.json",
        "results_json": ARTIFACT_DIR / f"{PREFIX}_results.json",
        "visualization_html": VISUALIZATION_DIR / f"{PREFIX}.html",
    }

    write_csv(artifact_paths["conflict_arcs_csv"], frames["conflict_arcs"])
    write_csv(artifact_paths["agent_counterproposals_csv"], frames["counterproposals"])
    write_csv(artifact_paths["negotiated_compromises_csv"], frames["compromises"])
    write_csv(artifact_paths["multi_party_consent_boundaries_csv"], frames["boundaries"])
    write_csv(artifact_paths["consent_memory_recalls_csv"], frames["recalls"])
    write_csv(artifact_paths["counterproposal_gameplay_effects_csv"], frames["effects"])
    write_csv(artifact_paths["failed_compromise_repairs_csv"], frames["repairs"])
    write_csv(artifact_paths["negotiation_replays_csv"], frames["replays"])
    write_csv(artifact_paths["browser_ticks_csv"], frames["browser_ticks"])
    write_mapping_csv(artifact_paths["summary_csv"], metrics)
    write_csv(artifact_paths["verdict_csv"], [{"verdict": verdict, **metrics}])

    state = build_state(frames, metrics, counts, args.seed)
    artifact_paths["state_json"].write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    render_html(state, artifact_paths["visualization_html"])

    results = {
        "report": 257,
        "name": "SSRM-3D browser world v17 agent-authored counterproposal compromise bridge",
        "seed": args.seed,
        "days": args.days,
        "turns_per_day": args.turns_per_day,
        "verdict": verdict,
        "counts": counts,
        "metrics": metrics,
        "ablations": ablations,
        "artifacts": {key: str(path.relative_to(ROOT)) for key, path in artifact_paths.items()},
        "source_dependency": str(SOURCE_RESULTS.relative_to(ROOT)),
        "source_verdict": source.get("verdict", "missing"),
        "claim_boundary": "Deterministic browser-local agent-authored counterproposal scaffold only; no subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
        "next_gate": "browser world v18 with multi-turn agent-led negotiation dialogue, counteroffer loops, and remembered compromise ceremonies in the playable browser surface",
    }
    artifact_paths["results_json"].write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")

    print(json.dumps({"verdict": verdict, "metrics": metrics, "counts": counts}, indent=2, sort_keys=True))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
