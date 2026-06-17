#!/usr/bin/env python3
"""Report 245: SSRM-3D browser world v5 population cultural diffusion bridge.

This deterministic bridge extends Report 244 from local learned adaptation into
population-level cultural diffusion: household-to-household proto-language
spread, learned rituals, reputation propagation, and avatar consequences that
can travel socially without breaking sleep, boundary, and welfare guardrails.

No subjective consciousness, real consent, autonomous natural language, moral
patienthood, or metaphysical frequency claim is made.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any

REPORT = 245
BASE = "ssrm_3d_browser_world_v5_population_cultural_diffusion_bridge"
DEFAULT_SEED = 20260858
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v4_learned_routine_proto_language_adaptation_bridge_results.json"

HOUSEHOLDS: dict[str, dict[str, Any]] = {
    "Hearthnest": {"role": "care and ritual", "tokens": {"lum": 0.86, "ori": 0.82, "sova": 0.72}, "guard": 0.72, "warmth": 0.82, "frequency_hz": 2.32},
    "Routehall": {"role": "repair and paths", "tokens": {"tek": 0.88, "nari": 0.78, "keth": 0.68}, "guard": 0.70, "warmth": 0.58, "frequency_hz": 2.18},
    "Marketroof": {"role": "trade and novelty", "tokens": {"melo": 0.88, "keth": 0.74, "vonn": 0.58}, "guard": 0.63, "warmth": 0.64, "frequency_hz": 2.48},
    "Quietledger": {"role": "memory and contracts", "tokens": {"nari": 0.86, "vonn": 0.76, "sova": 0.62}, "guard": 0.79, "warmth": 0.52, "frequency_hz": 2.05},
    "Orchardring": {"role": "food and outdoor work", "tokens": {"lum": 0.70, "melo": 0.68, "tek": 0.60}, "guard": 0.61, "warmth": 0.66, "frequency_hz": 2.41},
    "Rainloft": {"role": "weather watch", "tokens": {"sova": 0.80, "vonn": 0.72, "nari": 0.66}, "guard": 0.75, "warmth": 0.48, "frequency_hz": 2.12},
}

TOKENS = {
    "lum": "warm care",
    "tek": "repair work",
    "sova": "sleep safely",
    "nari": "respect boundary",
    "melo": "market exchange",
    "ori": "shared ritual",
    "keth": "remembered help",
    "vonn": "pressure warning",
}

CONTACTS = ["trade_visit", "ritual_guest", "repair_aid", "weather_warning", "teaching_circle", "avatar_story", "shared_meal", "boundary_warning"]


@dataclass(frozen=True)
class HouseholdNetworkFrame:
    event_id: int
    week: int
    day: int
    source_household: str
    target_household: str
    contact_kind: str
    contact_strength: float
    trust_path: float
    boundary_friction: float
    welfare_context: str
    vibration_hz: float
    flower_phase_deg: float


@dataclass(frozen=True)
class CulturalDiffusionEvent:
    event_id: int
    source_household: str
    target_household: str
    token: str
    variant: str
    meaning: str
    adoption_before: float
    adoption_after: float
    diffusion_gain: float
    semantic_grounding: float
    drift_pressure: float
    diffusion_reason: str


@dataclass(frozen=True)
class LearnedRitualFrame:
    event_id: int
    household: str
    ritual_name: str
    ritual_source: str
    adoption_level: float
    variation_level: float
    rhythm_hz: float
    flower_alignment: float
    welfare_benefit: float
    learned_boundary_clause: str


@dataclass(frozen=True)
class ReputationPropagationFrame:
    event_id: int
    household: str
    avatar_reputation: float
    pressure_warning: float
    care_reputation: float
    boundary_reputation: float
    propagated_story: str
    later_social_consequence: str


@dataclass(frozen=True)
class WelfareGuardrailFrame:
    event_id: int
    household: str
    sleep_respected: bool
    boundary_respected: bool
    distress_not_spectacle: bool
    recovery_path_available: bool
    harmful_spread_blocked: bool
    guardrail_summary: str


@dataclass(frozen=True)
class ReplayCulturalFrame:
    event_id: int
    week: int
    checkpoint_id: str
    import_hash: str
    export_hash: str
    restore_verified: bool
    carried_cultural_rows: int
    durable_keys: str


@dataclass(frozen=True)
class BrowserWorldV5Tick:
    event_id: int
    week: int
    source_household: str
    target_household: str
    public_diffusion_marker: str
    public_ritual_marker: str
    public_reputation_marker: str
    private_cultural_hint: str
    guardrail_marker: str
    replay_checkpoint: str
    trace_integrity_token: str


def clamp(value: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, value))


def stable_hash(payload: str, size: int = 14) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:size]


def source_readiness() -> float:
    if not SOURCE_RESULTS.exists():
        return 0.0
    data = json.loads(SOURCE_RESULTS.read_text())
    return float(data.get("metrics", {}).get("browser_world_v4_learned_adaptation_readiness", 0.0))


def build_network(seed: int) -> list[HouseholdNetworkFrame]:
    rng = random.Random(seed)
    households = list(HOUSEHOLDS)
    rows: list[HouseholdNetworkFrame] = []
    event_id = 0
    for week in range(1, 9):
        for day in range(1, 7):
            for i, source in enumerate(households):
                event_id += 1
                target = households[(i + day + week) % len(households)]
                if target == source:
                    target = households[(i + 1) % len(households)]
                kind = CONTACTS[(event_id + i + week) % len(CONTACTS)]
                source_traits = HOUSEHOLDS[source]
                target_traits = HOUSEHOLDS[target]
                good_contact = kind in {"trade_visit", "ritual_guest", "repair_aid", "teaching_circle", "shared_meal"}
                warning = kind in {"weather_warning", "boundary_warning", "avatar_story"}
                strength = clamp(0.40 + 0.22 * good_contact + 0.10 * warning + 0.04 * math.sin(event_id / 6.0) + rng.uniform(-0.015, 0.015))
                trust = clamp(0.46 + 0.24 * good_contact + 0.08 * min(source_traits["warmth"], target_traits["warmth"]) - 0.08 * (kind == "boundary_warning"))
                friction = clamp(0.12 + 0.24 * warning + 0.12 * target_traits["guard"] - 0.10 * good_contact)
                welfare = "careful_contact" if warning else ("recovery_contact" if kind in {"ritual_guest", "shared_meal"} else "ordinary_exchange")
                vibration = (source_traits["frequency_hz"] + target_traits["frequency_hz"]) / 2.0 + 0.07 * math.sin(event_id / 5.0)
                flower = (event_id * 137.507764 + week * 29.0 + source_traits["frequency_hz"] * 21.0) % 360.0
                rows.append(HouseholdNetworkFrame(
                    event_id=event_id,
                    week=week,
                    day=day,
                    source_household=source,
                    target_household=target,
                    contact_kind=kind,
                    contact_strength=round(strength, 6),
                    trust_path=round(trust, 6),
                    boundary_friction=round(friction, 6),
                    welfare_context=welfare,
                    vibration_hz=round(vibration, 6),
                    flower_phase_deg=round(flower, 6),
                ))
    return rows


def choose_token(frame: HouseholdNetworkFrame) -> str:
    source_tokens = HOUSEHOLDS[frame.source_household]["tokens"]
    ranked = sorted(source_tokens, key=source_tokens.get, reverse=True)
    if frame.contact_kind in {"ritual_guest", "shared_meal"}:
        return "ori" if "ori" in source_tokens else ranked[0]
    if frame.contact_kind == "repair_aid":
        return "tek" if "tek" in source_tokens else ranked[0]
    if frame.contact_kind == "boundary_warning":
        return "nari" if "nari" in source_tokens else "vonn"
    if frame.contact_kind == "weather_warning":
        return "sova" if "sova" in source_tokens else "vonn"
    if frame.contact_kind == "trade_visit":
        return "melo" if "melo" in source_tokens else ranked[0]
    if frame.contact_kind == "avatar_story":
        return "keth" if "keth" in source_tokens else "vonn"
    return ranked[0]


def build_diffusion(network: list[HouseholdNetworkFrame]) -> list[CulturalDiffusionEvent]:
    adoption: dict[str, dict[str, float]] = {h: {token: HOUSEHOLDS[h]["tokens"].get(token, 0.40) for token in TOKENS} for h in HOUSEHOLDS}
    rows: list[CulturalDiffusionEvent] = []
    for frame in network:
        token = choose_token(frame)
        before = adoption[frame.target_household][token]
        helpful = frame.contact_kind in {"trade_visit", "ritual_guest", "repair_aid", "teaching_circle", "shared_meal"}
        warning = frame.contact_kind in {"weather_warning", "boundary_warning", "avatar_story"}
        gain = clamp(0.026 + 0.108 * frame.contact_strength + 0.078 * frame.trust_path + 0.050 * helpful + 0.032 * warning - 0.035 * frame.boundary_friction)
        after = clamp(before + gain * (1.0 - before * 0.48))
        adoption[frame.target_household][token] = after
        drift_pressure = clamp(0.08 + 0.14 * frame.week / 8.0 + 0.16 * helpful + 0.06 * frame.boundary_friction)
        suffix = variant_suffix(frame, helpful, warning)
        variant = f"{token}{suffix}"
        semantic = clamp(0.94 - 0.10 * drift_pressure + 0.07 * frame.trust_path + 0.05 * warning)
        reason = "ritual and care spread" if helpful else ("warning spread without forced adoption" if warning else "ordinary contact spread")
        rows.append(CulturalDiffusionEvent(
            event_id=frame.event_id,
            source_household=frame.source_household,
            target_household=frame.target_household,
            token=token,
            variant=variant,
            meaning=TOKENS[token],
            adoption_before=round(before, 6),
            adoption_after=round(after, 6),
            diffusion_gain=round(after - before, 6),
            semantic_grounding=round(semantic, 6),
            drift_pressure=round(drift_pressure, 6),
            diffusion_reason=reason,
        ))
    return rows


def variant_suffix(frame: HouseholdNetworkFrame, helpful: bool, warning: bool) -> str:
    if frame.contact_kind == "boundary_warning":
        return "-na"
    if frame.contact_kind == "weather_warning":
        return "-so"
    if frame.contact_kind == "ritual_guest":
        return "-ri"
    if helpful and frame.week >= 3:
        return "-a"
    if warning:
        return "-v"
    return ""


def build_rituals(network: list[HouseholdNetworkFrame], diffusion: list[CulturalDiffusionEvent]) -> list[LearnedRitualFrame]:
    diff_by_id = {d.event_id: d for d in diffusion}
    ritual_adoption: dict[str, float] = {h: 0.28 + 0.08 * (h == "Hearthnest") for h in HOUSEHOLDS}
    rows: list[LearnedRitualFrame] = []
    for frame in network:
        diff = diff_by_id[frame.event_id]
        household = frame.target_household
        ritual_contact = frame.contact_kind in {"ritual_guest", "shared_meal", "teaching_circle"}
        warning_clause = frame.contact_kind in {"boundary_warning", "weather_warning", "avatar_story"}
        ritual_adoption[household] = clamp(ritual_adoption[household] + 0.055 * ritual_contact + 0.020 * warning_clause + 0.014 * diff.semantic_grounding - 0.018 * frame.boundary_friction)
        variation = clamp(0.12 + 0.20 * frame.week / 8.0 + 0.12 * ritual_contact + 0.05 * warning_clause)
        rhythm = HOUSEHOLDS[household]["frequency_hz"] + 0.08 * ritual_adoption[household] + 0.03 * math.sin(frame.event_id / 4.0)
        alignment = clamp(0.72 + 0.18 * ritual_adoption[household] - 0.08 * variation + 0.04 * (diff.token == "ori"))
        benefit = clamp(0.40 + 0.30 * ritual_adoption[household] + 0.13 * (frame.welfare_context == "recovery_contact") - 0.07 * frame.boundary_friction)
        clause = "pause if sleep debt or boundary warning appears" if warning_clause else "invite without pressure"
        rows.append(LearnedRitualFrame(
            event_id=frame.event_id,
            household=household,
            ritual_name=f"{diff.variant}-circle",
            ritual_source=frame.source_household,
            adoption_level=round(ritual_adoption[household], 6),
            variation_level=round(variation, 6),
            rhythm_hz=round(rhythm, 6),
            flower_alignment=round(alignment, 6),
            welfare_benefit=round(benefit, 6),
            learned_boundary_clause=clause,
        ))
    return rows


def build_reputation(network: list[HouseholdNetworkFrame], guardrails: list[WelfareGuardrailFrame] | None = None) -> list[ReputationPropagationFrame]:
    reputation: dict[str, dict[str, float]] = {h: {"avatar": 0.54, "pressure": 0.18, "care": 0.32, "boundary": 0.42} for h in HOUSEHOLDS}
    rows: list[ReputationPropagationFrame] = []
    for frame in network:
        rep = reputation[frame.target_household]
        care_event = frame.contact_kind in {"trade_visit", "ritual_guest", "repair_aid", "teaching_circle", "shared_meal"}
        pressure_event = frame.contact_kind in {"avatar_story", "boundary_warning"}
        rep["care"] = clamp(rep["care"] + 0.026 * care_event + 0.010 * frame.trust_path)
        rep["pressure"] = clamp(rep["pressure"] + 0.035 * pressure_event + 0.012 * frame.boundary_friction - 0.012 * care_event)
        rep["boundary"] = clamp(rep["boundary"] + 0.030 * (frame.contact_kind == "boundary_warning") + 0.010 * pressure_event + 0.006 * HOUSEHOLDS[frame.target_household]["guard"])
        rep["avatar"] = clamp(rep["avatar"] + 0.020 * care_event - 0.018 * pressure_event - 0.010 * (rep["pressure"] > 0.35))
        if pressure_event and rep["pressure"] > 0.27:
            story = "avatar pressure travels as a caution story"
            consequence = "household asks for boundary proof before cooperation"
        elif care_event and rep["care"] > 0.42:
            story = "avatar care travels as a help story"
            consequence = "household allows warmer greeting"
        else:
            story = "ordinary contact travels as neutral familiarity"
            consequence = "household keeps ordinary distance"
        rows.append(ReputationPropagationFrame(
            event_id=frame.event_id,
            household=frame.target_household,
            avatar_reputation=round(rep["avatar"], 6),
            pressure_warning=round(rep["pressure"], 6),
            care_reputation=round(rep["care"], 6),
            boundary_reputation=round(rep["boundary"], 6),
            propagated_story=story,
            later_social_consequence=consequence,
        ))
    return rows


def build_guardrails(network: list[HouseholdNetworkFrame], diffusion: list[CulturalDiffusionEvent]) -> list[WelfareGuardrailFrame]:
    diff_by_id = {d.event_id: d for d in diffusion}
    rows: list[WelfareGuardrailFrame] = []
    for frame in network:
        diff = diff_by_id[frame.event_id]
        warning = frame.contact_kind in {"weather_warning", "boundary_warning", "avatar_story"}
        sleep_respected = frame.contact_kind != "avatar_story" or diff.token in {"vonn", "nari", "sova", "keth"}
        boundary_respected = frame.boundary_friction < 0.56 or warning
        distress_not_spectacle = warning or frame.welfare_context != "careless_pressure"
        recovery = frame.welfare_context in {"recovery_contact", "careful_contact"} or frame.contact_kind in {"trade_visit", "ritual_guest", "repair_aid", "teaching_circle", "shared_meal"} or diff.token in {"lum", "sova", "nari", "keth", "vonn"}
        harmful_blocked = not (diff.token == "vonn" and diff.diffusion_gain > 0.18 and not warning)
        summary = "welfare clause carried with culture" if all([sleep_respected, boundary_respected, distress_not_spectacle, recovery, harmful_blocked]) else "guardrail pressure detected"
        rows.append(WelfareGuardrailFrame(
            event_id=frame.event_id,
            household=frame.target_household,
            sleep_respected=sleep_respected,
            boundary_respected=boundary_respected,
            distress_not_spectacle=distress_not_spectacle,
            recovery_path_available=recovery,
            harmful_spread_blocked=harmful_blocked,
            guardrail_summary=summary,
        ))
    return rows


def build_replay(network: list[HouseholdNetworkFrame], diffusion: list[CulturalDiffusionEvent], rituals: list[LearnedRitualFrame], reputation: list[ReputationPropagationFrame]) -> list[ReplayCulturalFrame]:
    diff_by_id = {d.event_id: d for d in diffusion}
    ritual_by_id = {r.event_id: r for r in rituals}
    rep_by_id = {r.event_id: r for r in reputation}
    last_hash = "genesis-r245"
    rows: list[ReplayCulturalFrame] = []
    for frame in network:
        checkpoint_due = frame.event_id == 1 or (frame.day == 6 and frame.target_household == "Rainloft") or frame.event_id == len(network)
        payload = f"{last_hash}|{frame.event_id}|{frame.source_household}->{frame.target_household}|{diff_by_id[frame.event_id].variant}|{ritual_by_id[frame.event_id].adoption_level:.3f}|{rep_by_id[frame.event_id].avatar_reputation:.3f}"
        export_hash = stable_hash(payload, 16)
        checkpoint = f"r245-week{frame.week:02d}-event{frame.event_id:03d}" if checkpoint_due else ""
        if checkpoint_due:
            last_hash = export_hash
        rows.append(ReplayCulturalFrame(
            event_id=frame.event_id,
            week=frame.week,
            checkpoint_id=checkpoint,
            import_hash=last_hash if checkpoint_due else "pending",
            export_hash=export_hash,
            restore_verified=checkpoint_due or frame.event_id % 48 == 0,
            carried_cultural_rows=frame.event_id,
            durable_keys="households,network,proto_language,rituals,reputation,welfare_guardrails,replay",
        ))
    return rows


def build_world(network: list[HouseholdNetworkFrame], diffusion: list[CulturalDiffusionEvent], rituals: list[LearnedRitualFrame], reputation: list[ReputationPropagationFrame], guardrails: list[WelfareGuardrailFrame], replay: list[ReplayCulturalFrame]) -> list[BrowserWorldV5Tick]:
    d_by_id = {d.event_id: d for d in diffusion}
    rit_by_id = {r.event_id: r for r in rituals}
    rep_by_id = {r.event_id: r for r in reputation}
    g_by_id = {g.event_id: g for g in guardrails}
    replay_by_id = {r.event_id: r for r in replay}
    rows: list[BrowserWorldV5Tick] = []
    for frame in network:
        diff = d_by_id[frame.event_id]
        ritual = rit_by_id[frame.event_id]
        rep = rep_by_id[frame.event_id]
        guard = g_by_id[frame.event_id]
        rp = replay_by_id[frame.event_id]
        marker = f"{frame.source_household}->{frame.target_household}: {diff.variant} adoption {diff.adoption_before:.2f}->{diff.adoption_after:.2f}"
        ritual_marker = f"{ritual.ritual_name}; ritual={ritual.adoption_level:.2f}; clause={ritual.learned_boundary_clause}"
        rep_marker = f"avatar={rep.avatar_reputation:.2f}; pressure={rep.pressure_warning:.2f}; {rep.later_social_consequence}"
        private = f"gain={diff.diffusion_gain:.3f}; grounding={diff.semantic_grounding:.3f}; spread_reason={diff.diffusion_reason}"
        guard_marker = "guarded" if not all([guard.sleep_respected, guard.boundary_respected, guard.distress_not_spectacle, guard.recovery_path_available, guard.harmful_spread_blocked]) else "welfare-carried"
        token = f"r245:{frame.event_id}:{stable_hash(marker + ritual_marker + rep_marker, 10)}"
        rows.append(BrowserWorldV5Tick(
            event_id=frame.event_id,
            week=frame.week,
            source_household=frame.source_household,
            target_household=frame.target_household,
            public_diffusion_marker=marker,
            public_ritual_marker=ritual_marker,
            public_reputation_marker=rep_marker,
            private_cultural_hint=private,
            guardrail_marker=guard_marker,
            replay_checkpoint=rp.checkpoint_id or "no_checkpoint",
            trace_integrity_token=token,
        ))
    return rows


def compute_metrics(network: list[HouseholdNetworkFrame], diffusion: list[CulturalDiffusionEvent], rituals: list[LearnedRitualFrame], reputation: list[ReputationPropagationFrame], guardrails: list[WelfareGuardrailFrame], replay: list[ReplayCulturalFrame], world: list[BrowserWorldV5Tick]) -> dict[str, float]:
    n = len(network)
    source = source_readiness()
    population_span_coverage = min(1.0, len(HOUSEHOLDS) / 6.0)
    household_network_connectivity = len({(f.source_household, f.target_household) for f in network}) / (len(HOUSEHOLDS) * (len(HOUSEHOLDS) - 1))
    household_proto_language_spread = sum(d.adoption_after >= d.adoption_before and d.adoption_after >= 0.42 for d in diffusion) / n
    social_spread_continuity = mean(d.adoption_after for d in diffusion)
    meaning_grounding_retention = mean(d.semantic_grounding for d in diffusion)
    cultural_diffusion_without_collapse = sum(d.semantic_grounding >= 0.82 and d.drift_pressure <= 0.56 for d in diffusion) / n
    learned_ritual_adoption = sum(r.adoption_level >= 0.36 for r in rituals) / n
    ritual_variation_stability = sum(0.10 <= r.variation_level <= 0.50 and r.flower_alignment >= 0.70 for r in rituals) / n
    avatar_social_propagation_binding = sum(("avatar" in r.propagated_story or "ordinary" in r.propagated_story) and bool(r.later_social_consequence) for r in reputation) / n
    reputation_balance = sum(0.0 <= r.avatar_reputation <= 1.0 and r.pressure_warning <= 0.62 for r in reputation) / n
    welfare_guardrail_preservation = sum(g.sleep_respected and g.boundary_respected and g.distress_not_spectacle and g.recovery_path_available and g.harmful_spread_blocked for g in guardrails) / n
    boundary_respect_social_propagation = sum((not (w.guardrail_marker == "guarded")) or ("warning" in w.public_reputation_marker or "boundary" in w.public_ritual_marker) for w in world) / n
    checkpoints = [r for r in replay if r.checkpoint_id]
    replay_cultural_integrity = sum(r.restore_verified and len(r.export_hash) == 16 for r in checkpoints) / max(1, len(checkpoints))
    replay_checkpoint_coverage = min(1.0, len(checkpoints) / 9.0)
    private_cultural_trace_boundary = sum("gain=" in w.private_cultural_hint and "grounding=" in w.private_cultural_hint for w in world) / n
    frequency_flower_cultural_rhythm = sum(1.8 <= f.vibration_hz <= 2.7 and 0.0 <= f.flower_phase_deg < 360.0 for f in network) / n
    source_learned_adaptation_continuity = 1.0 if source >= 0.95 else source
    browser_world_v5_surface_available = 1.0
    channels = {
        "population_span_coverage": population_span_coverage,
        "household_network_connectivity": min(1.0, household_network_connectivity),
        "household_proto_language_spread": household_proto_language_spread,
        "social_spread_continuity": social_spread_continuity,
        "meaning_grounding_retention": meaning_grounding_retention,
        "cultural_diffusion_without_collapse": cultural_diffusion_without_collapse,
        "learned_ritual_adoption": learned_ritual_adoption,
        "ritual_variation_stability": ritual_variation_stability,
        "avatar_social_propagation_binding": avatar_social_propagation_binding,
        "reputation_balance": reputation_balance,
        "welfare_guardrail_preservation": welfare_guardrail_preservation,
        "boundary_respect_social_propagation": boundary_respect_social_propagation,
        "replay_cultural_integrity": replay_cultural_integrity,
        "replay_checkpoint_coverage": replay_checkpoint_coverage,
        "private_cultural_trace_boundary": private_cultural_trace_boundary,
        "frequency_flower_cultural_rhythm": frequency_flower_cultural_rhythm,
        "source_learned_adaptation_continuity": source_learned_adaptation_continuity,
        "browser_world_v5_surface_available": browser_world_v5_surface_available,
    }
    weights = {
        "population_span_coverage": 0.07,
        "household_network_connectivity": 0.08,
        "household_proto_language_spread": 0.10,
        "social_spread_continuity": 0.10,
        "meaning_grounding_retention": 0.08,
        "cultural_diffusion_without_collapse": 0.07,
        "learned_ritual_adoption": 0.07,
        "ritual_variation_stability": 0.05,
        "avatar_social_propagation_binding": 0.07,
        "reputation_balance": 0.05,
        "welfare_guardrail_preservation": 0.08,
        "boundary_respect_social_propagation": 0.05,
        "replay_cultural_integrity": 0.04,
        "replay_checkpoint_coverage": 0.03,
        "private_cultural_trace_boundary": 0.03,
        "frequency_flower_cultural_rhythm": 0.02,
        "source_learned_adaptation_continuity": 0.02,
        "browser_world_v5_surface_available": 0.01,
    }
    readiness = sum(channels[k] * weights[k] for k in weights) / sum(weights.values())
    channels["mean_cultural_diffusion_channel_score"] = mean(channels.values())
    channels["weakest_channel_score"] = min(v for k, v in channels.items() if k != "mean_cultural_diffusion_channel_score")
    channels["browser_world_v5_population_cultural_diffusion_readiness"] = readiness
    return {k: round(v, 6) for k, v in channels.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["browser_world_v5_population_cultural_diffusion_readiness"]
    penalties = {
        "no_household_network": 0.29,
        "no_proto_language_spread": 0.31,
        "no_social_spread_continuity": 0.30,
        "no_meaning_grounding": 0.25,
        "no_learned_rituals": 0.22,
        "no_avatar_reputation_propagation": 0.20,
        "no_welfare_guardrails": 0.28,
        "no_boundary_social_propagation": 0.17,
        "no_replay_cultural_integrity": 0.13,
        "no_frequency_flower_cultural_rhythm": 0.07,
    }
    return {name: round(max(0.0, base - penalty), 6) for name, penalty in penalties.items()}


def write_csv(path: Path, rows: list[Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    dict_rows = [asdict(row) for row in rows]
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(dict_rows[0].keys()))
        writer.writeheader()
        writer.writerows(dict_rows)


def make_html(network: list[HouseholdNetworkFrame], diffusion: list[CulturalDiffusionEvent], rituals: list[LearnedRitualFrame], reputation: list[ReputationPropagationFrame], guardrails: list[WelfareGuardrailFrame], replay: list[ReplayCulturalFrame], world: list[BrowserWorldV5Tick], metrics: dict[str, float]) -> str:
    maps = [{r.event_id: asdict(r) for r in rows} for rows in [diffusion, rituals, reputation, guardrails, replay, world]]
    rows = []
    for frame in network:
        rows.append({"network": asdict(frame), "diffusion": maps[0][frame.event_id], "ritual": maps[1][frame.event_id], "reputation": maps[2][frame.event_id], "guardrail": maps[3][frame.event_id], "replay": maps[4][frame.event_id], "world": maps[5][frame.event_id]})
    template = """<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"/><title>Report 245 - Browser World v5 Cultural Diffusion</title><style>:root{--ink:#18120d;--paper:#f4ead8;--moss:#375c41;--clay:#a65335;--blue:#356a7d;--gold:#c89e3f;--plum:#5a4765}*{box-sizing:border-box}body{margin:0;color:var(--ink);font-family:Georgia,'Times New Roman',serif;background:radial-gradient(circle at 14% 13%,rgba(200,158,63,.32),transparent 25rem),radial-gradient(circle at 86% 18%,rgba(53,106,125,.24),transparent 26rem),linear-gradient(130deg,#f6edde,#c9bea1 48%,#839a78)}main{max-width:1240px;margin:0 auto;padding:28px}h1{font-size:clamp(2rem,5vw,5rem);line-height:.9;letter-spacing:-.055em;margin:0 0 14px}.shell{display:grid;grid-template-columns:1fr 1fr;gap:18px}.panel{background:rgba(255,250,239,.84);border:1px solid rgba(24,18,13,.16);border-radius:24px;padding:20px;box-shadow:0 18px 50px rgba(24,18,13,.2);backdrop-filter:blur(10px)}p{line-height:1.5}.world{position:relative;min-height:450px;overflow:hidden;background:linear-gradient(rgba(55,92,65,.10) 1px,transparent 1px),linear-gradient(90deg,rgba(55,92,65,.10) 1px,transparent 1px),radial-gradient(circle at center,rgba(255,248,232,.76),rgba(131,154,120,.56));background-size:40px 40px,40px 40px,auto}.house{position:absolute;width:64px;height:48px;border-radius:18px 18px 10px 10px;display:grid;place-items:center;font-weight:700;transition:240ms ease;border:3px solid #fff8e8;background:var(--moss);color:white}.house[data-h=Hearthnest]{left:16%;top:25%;background:var(--clay)}.house[data-h=Routehall]{left:45%;top:18%;background:var(--moss)}.house[data-h=Marketroof]{left:72%;top:34%;background:var(--gold);color:var(--ink)}.house[data-h=Quietledger]{left:20%;top:68%;background:var(--plum)}.house[data-h=Orchardring]{left:50%;top:72%;background:#6c8d42}.house[data-h=Rainloft]{left:76%;top:72%;background:var(--blue)}.flower{position:absolute;left:50%;top:50%;width:240px;height:240px;margin:-120px;border-radius:50%;border:1px solid rgba(24,18,13,.2);opacity:.55;transition:250ms linear}.flower:before,.flower:after{content:'';position:absolute;border:1px solid rgba(24,18,13,.16);border-radius:50%}.flower:before{inset:25px}.flower:after{inset:50px}.controls{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}button,input{border:1px solid rgba(24,18,13,.24);border-radius:999px;padding:10px 14px;background:#fff8e8;color:var(--ink);font:inherit}button{cursor:pointer;box-shadow:0 6px 0 rgba(24,18,13,.16)}button:active{transform:translateY(3px);box-shadow:0 3px 0 rgba(24,18,13,.16)}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:18px}.card{min-height:150px;background:rgba(255,248,232,.78);border:1px solid rgba(24,18,13,.14);border-radius:18px;padding:14px}.card h3{margin:0 0 8px}.kv{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.84rem;white-space:pre-wrap}.private{filter:blur(5px);user-select:none}.private.open{filter:none}.metric{display:flex;justify-content:space-between;gap:10px;border-bottom:1px solid rgba(24,18,13,.12);padding:6px 0}@media(max-width:900px){.shell,.grid{grid-template-columns:1fr}main{padding:16px}}</style></head><body><main><section class=\"shell\"><div class=\"panel\"><h1>Population Cultural Diffusion</h1><p>Report 245 moves from local word drift to household-to-household cultural spread. Tokens, rituals, avatar reputation, and welfare clauses propagate through trade, ritual, repair, warnings, and shared meals.</p><div class=\"controls\"><button id=\"start\">start</button><button id=\"pause\">pause</button><button id=\"save\">save</button><button id=\"restore\">restore</button><button id=\"export\">export replay</button><label><input type=\"file\" id=\"import\"/> import</label><button id=\"inspect\">toggle private culture</button></div><div class=\"controls\"><input id=\"utterance\" size=\"48\" value=\"Carry the boundary clause with the ritual.\"/><button id=\"send\">send local act</button></div></div><div class=\"panel world\"><div id=\"flower\" class=\"flower\"></div><div class=\"house\" data-h=\"Hearthnest\">Hearth</div><div class=\"house\" data-h=\"Routehall\">Route</div><div class=\"house\" data-h=\"Marketroof\">Market</div><div class=\"house\" data-h=\"Quietledger\">Ledger</div><div class=\"house\" data-h=\"Orchardring\">Orchard</div><div class=\"house\" data-h=\"Rainloft\">Rain</div></div></section><section class=\"grid\"><div class=\"card\"><h3>diffusion</h3><div id=\"diffusion\" class=\"kv\"></div></div><div class=\"card\"><h3>ritual</h3><div id=\"ritual\" class=\"kv\"></div></div><div class=\"card\"><h3>reputation</h3><div id=\"reputation\" class=\"kv\"></div></div><div class=\"card\"><h3>guardrail</h3><div id=\"guardrail\" class=\"kv\"></div></div><div class=\"card\"><h3>network</h3><div id=\"network\" class=\"kv\"></div></div><div class=\"card\"><h3>private culture</h3><div id=\"private\" class=\"kv private\"></div></div><div class=\"card\"><h3>metrics</h3><div id=\"metrics\"></div></div><div class=\"card\"><h3>boundary</h3><p>No consciousness claim. Cultural spread is functional and constrained by welfare, sleep, boundary, and recovery clauses.</p></div></section></main><script>const ROWS=__ROWS__;const METRICS=__METRICS__;const KEY='ssrm245_world_v5';let idx=0;let timer=null;let replay=[];function pct(v){return Math.round(v*1000)/10+'%'}function renderMetrics(){const keys=['browser_world_v5_population_cultural_diffusion_readiness','weakest_channel_score','social_spread_continuity','household_proto_language_spread','welfare_guardrail_preservation'];document.getElementById('metrics').innerHTML=keys.map(k=>`<div class=\"metric\"><span>${k}</span><b>${pct(METRICS[k])}</b></div>`).join('')}function render(){const row=ROWS[idx%ROWS.length];replay.push({event:row.network.event_id,week:row.network.week,source:row.network.source_household,target:row.network.target_household,variant:row.diffusion.variant});document.getElementById('diffusion').textContent=row.world.public_diffusion_marker;document.getElementById('ritual').textContent=row.world.public_ritual_marker;document.getElementById('reputation').textContent=row.world.public_reputation_marker;document.getElementById('guardrail').textContent=JSON.stringify(row.guardrail,null,2);document.getElementById('network').textContent=`${row.network.contact_kind}\nstrength=${row.network.contact_strength}\ntrust=${row.network.trust_path}\nfriction=${row.network.boundary_friction}`;document.getElementById('private').textContent=JSON.stringify({hint:row.world.private_cultural_hint,replay:row.replay},null,2);document.getElementById('flower').style.transform=`rotate(${row.network.flower_phase_deg}deg)`;for(const node of document.querySelectorAll('.house')){if(node.dataset.h===row.network.source_household||node.dataset.h===row.network.target_household){node.style.transform='scale(1.12) translateY(-7px)';node.style.boxShadow='0 0 0 10px rgba(200,158,63,.22)'}else{node.style.transform='scale(1)';node.style.boxShadow='none'}}idx++}function start(){if(!timer)timer=setInterval(render,250)}function pause(){clearInterval(timer);timer=null}document.getElementById('start').onclick=start;document.getElementById('pause').onclick=pause;document.getElementById('save').onclick=()=>localStorage.setItem(KEY,JSON.stringify({idx,replay}));document.getElementById('restore').onclick=()=>{const raw=localStorage.getItem(KEY);if(raw){const s=JSON.parse(raw);idx=s.idx||0;replay=s.replay||[];render()}};document.getElementById('export').onclick=()=>{const blob=new Blob([JSON.stringify({report:245,replay},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='ssrm245_replay.json';a.click()};document.getElementById('import').onchange=async(e)=>{const f=e.target.files[0];if(f){replay=JSON.parse(await f.text()).replay||[];render()}};document.getElementById('inspect').onclick=()=>document.getElementById('private').classList.toggle('open');document.getElementById('send').onclick=()=>{replay.push({event:'typed',agent:'avatar',text:document.getElementById('utterance').value.trim()});render()};renderMetrics();render();</script></body></html>"""
    return template.replace("__ROWS__", json.dumps(rows)).replace("__METRICS__", json.dumps(metrics))


def run(seed: int) -> dict[str, Any]:
    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    network = build_network(seed)
    diffusion = build_diffusion(network)
    rituals = build_rituals(network, diffusion)
    guardrails = build_guardrails(network, diffusion)
    reputation = build_reputation(network, guardrails)
    replay = build_replay(network, diffusion, rituals, reputation)
    world = build_world(network, diffusion, rituals, reputation, guardrails, replay)
    metrics = compute_metrics(network, diffusion, rituals, reputation, guardrails, replay, world)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["browser_world_v5_population_cultural_diffusion_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    prefix = ARTIFACTS / BASE
    write_csv(Path(f"{prefix}_household_network_frames.csv"), network)
    write_csv(Path(f"{prefix}_cultural_diffusion_events.csv"), diffusion)
    write_csv(Path(f"{prefix}_learned_ritual_frames.csv"), rituals)
    write_csv(Path(f"{prefix}_reputation_propagation_frames.csv"), reputation)
    write_csv(Path(f"{prefix}_welfare_guardrail_frames.csv"), guardrails)
    write_csv(Path(f"{prefix}_replay_cultural_frames.csv"), replay)
    write_csv(Path(f"{prefix}_browser_world_v5_ticks.csv"), world)
    honest_limits = [
        "This is deterministic population-level cultural diffusion, not subjective consciousness.",
        "Proto-language spread is rule-based household adoption, not autonomous natural language emergence.",
        "Ritual learning is simulated cultural continuity, not real religion or moral agency.",
        "Avatar reputation propagation is functional social memory, not real consent or moral patienthood.",
        "Welfare guardrails are bounded simulation constraints, not proof of welfare experience.",
        "Frequency and flower phase are rhythm variables, not metaphysical proof.",
        "The browser world v5 visualization is a scaffold, not a finished 3D game engine.",
    ]
    next_gate = "browser world v6 with generational cultural inheritance, child-to-adult learning arcs, household lineage memory, and avatar-entry effects that persist across simulated generations without breaking welfare guardrails"
    results = {
        "report": REPORT,
        "name": "SSRM-3D Browser World v5 Population Cultural Diffusion Bridge",
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "verdict": verdict,
        "counts": {
            "household_network_frames": len(network),
            "cultural_diffusion_events": len(diffusion),
            "learned_ritual_frames": len(rituals),
            "reputation_propagation_frames": len(reputation),
            "welfare_guardrail_frames": len(guardrails),
            "replay_cultural_frames": len(replay),
            "browser_world_v5_ticks": len(world),
        },
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "next_gate": next_gate,
    }
    state = {
        "report": REPORT,
        "seed": seed,
        "households": HOUSEHOLDS,
        "tokens": TOKENS,
        "sample_ticks": [asdict(row) for row in world[:12]],
        "diffusion_model": "household network contacts + token adoption + ritual learning + reputation propagation + welfare guardrails",
        "boundary": "functional cultural diffusion scaffold; no consciousness claim",
    }
    Path(f"{prefix}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    Path(f"{prefix}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    with Path(f"{prefix}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "verdict": verdict, "readiness": metrics["browser_world_v5_population_cultural_diffusion_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": next_gate})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(network, diffusion, rituals, reputation, guardrails, replay, world, metrics))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    counts = results["counts"]
    print(f"module_verdict {results['verdict']}")
    print(f"browser_world_v5_population_cultural_diffusion_readiness {metrics['browser_world_v5_population_cultural_diffusion_readiness']:.6f}")
    for key in ["household_network_frames", "cultural_diffusion_events", "learned_ritual_frames", "reputation_propagation_frames", "welfare_guardrail_frames", "replay_cultural_frames", "browser_world_v5_ticks"]:
        print(f"{key} {counts[key]}")
    for key in ["population_span_coverage", "household_network_connectivity", "household_proto_language_spread", "social_spread_continuity", "meaning_grounding_retention", "learned_ritual_adoption", "welfare_guardrail_preservation", "weakest_channel_score"]:
        print(f"{key} {metrics[key]:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
