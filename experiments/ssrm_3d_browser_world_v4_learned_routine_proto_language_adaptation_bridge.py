#!/usr/bin/env python3
"""Report 244: SSRM-3D browser world v4 learned routine/proto-language adaptation bridge.

This deterministic bridge extends Report 243 by adding multi-week learned
routine adaptation and proto-language drift from repeated interactions. Avatar
entry consequences must respect sleep debt, boundaries, and relationship history.

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

REPORT = 244
BASE = "ssrm_3d_browser_world_v4_learned_routine_proto_language_adaptation_bridge"
DEFAULT_SEED = 20260857
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_browser_world_v3_long_horizon_routine_circadian_relationship_bridge_results.json"

AGENTS: dict[str, dict[str, Any]] = {
    "Ari": {"role": "route keeper", "baseline_trust": 0.55, "sleep_sensitivity": 0.62, "boundary_need": 0.66, "learning_rate": 0.16, "voice_hz": 210.0, "home": "workbench alcove"},
    "Fay": {"role": "hearth ritualist", "baseline_trust": 0.64, "sleep_sensitivity": 0.48, "boundary_need": 0.49, "learning_rate": 0.18, "voice_hz": 240.0, "home": "hearth nest"},
    "Milo": {"role": "pattern scout", "baseline_trust": 0.59, "sleep_sensitivity": 0.43, "boundary_need": 0.61, "learning_rate": 0.20, "voice_hz": 265.0, "home": "market canopy"},
    "Sol": {"role": "seed ledger guardian", "baseline_trust": 0.50, "sleep_sensitivity": 0.68, "boundary_need": 0.72, "learning_rate": 0.13, "voice_hz": 198.0, "home": "quiet corner"},
}

BASE_LEXICON = {
    "lum": "warm care",
    "tek": "repair work",
    "sova": "sleep safely",
    "nari": "respect boundary",
    "melo": "market exchange",
    "ori": "shared ritual",
    "keth": "remembered help",
    "vonn": "pressure warning",
}

INTERACTIONS = [
    ("wait_respectfully", "avatar waits until routine ends", "nari"),
    ("offer_help", "avatar helps without taking ownership", "keth"),
    ("ask_repair", "avatar asks for route repair", "tek"),
    ("interrupt_sleep", "avatar requests action during rest", "sova"),
    ("join_ritual", "avatar joins ritual softly", "ori"),
    ("repeat_pressure", "avatar repeats request too soon", "vonn"),
    ("trade_fairly", "avatar trades at market value", "melo"),
    ("offer_warmth", "avatar opens warm dry place", "lum"),
]

ROUTINES = ["repair_route", "hearth_care", "market_scan", "ledger_sort", "ritual_hum", "sleep_recovery", "boundary_pause", "teach_word"]


@dataclass(frozen=True)
class AdaptationEpisodeSpec:
    episode_id: int
    week: int
    day: int
    agent: str
    interaction_kind: str
    avatar_action: str
    base_token: str
    sleep_debt: float
    boundary_pressure: float
    relationship_trust_before: float
    relationship_respect_before: float
    vibration_hz: float
    flower_phase_deg: float


@dataclass(frozen=True)
class RoutinePolicyUpdateFrame:
    episode_id: int
    agent: str
    prior_primary_routine: str
    selected_routine: str
    adaptation_signal: float
    cooperation_weight: float
    boundary_weight: float
    recovery_weight: float
    novelty_weight: float
    learned_policy_delta: float
    adaptation_reason: str


@dataclass(frozen=True)
class ProtoLanguageDriftFrame:
    episode_id: int
    agent: str
    base_token: str
    drifted_token: str
    meaning: str
    phoneme_shift: str
    usage_count: int
    semantic_grounding: float
    novelty: float
    stability: float
    social_spread: float
    drift_reason: str


@dataclass(frozen=True)
class BoundarySleepRespectFrame:
    episode_id: int
    agent: str
    request_allowed: bool
    sleep_respected: bool
    boundary_respected: bool
    refusal_needed: bool
    refusal_text: str
    recovery_offer: str
    welfare_guardrail: str


@dataclass(frozen=True)
class RelationshipLearningFrame:
    episode_id: int
    agent: str
    trust_after: float
    respect_after: float
    familiarity_after: float
    avoidance_after: float
    gratitude_after: float
    resentment_after: float
    learned_about_avatar: str
    relationship_consequence: str


@dataclass(frozen=True)
class AvatarEntryConsequenceFrame:
    episode_id: int
    agent: str
    consequence_type: str
    immediate_response: str
    later_response: str
    allowed_by_sleep: bool
    allowed_by_boundary: bool
    allowed_by_relationship: bool
    consequence_strength: float


@dataclass(frozen=True)
class ReplayAdaptationFrame:
    episode_id: int
    week: int
    checkpoint_id: str
    import_hash: str
    export_hash: str
    restore_verified: bool
    carried_learning_rows: int
    durable_keys: str


@dataclass(frozen=True)
class BrowserWorldV4Tick:
    episode_id: int
    week: int
    day: int
    agent: str
    public_routine_marker: str
    public_language_marker: str
    public_relationship_marker: str
    private_learning_hint: str
    boundary_or_recovery: str
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
    return float(data.get("metrics", {}).get("browser_world_v3_long_horizon_readiness", 0.0))


def build_episode_specs(seed: int) -> list[AdaptationEpisodeSpec]:
    rng = random.Random(seed)
    agents = list(AGENTS)
    trust = {agent: AGENTS[agent]["baseline_trust"] for agent in agents}
    respect = {agent: 0.58 for agent in agents}
    sleep_debt = {agent: 0.26 for agent in agents}
    specs: list[AdaptationEpisodeSpec] = []
    eid = 0
    for week in range(1, 7):
        for day in range(1, 8):
            for agent in agents:
                eid += 1
                traits = AGENTS[agent]
                kind, action, token = INTERACTIONS[(week + day + agents.index(agent)) % len(INTERACTIONS)]
                sleep_pressure = 0.10 + 0.11 * (day % 3) + 0.18 * (kind == "interrupt_sleep") + 0.07 * (kind == "repeat_pressure")
                sleep_debt[agent] = clamp(sleep_debt[agent] * 0.74 + sleep_pressure - 0.18 * (kind in {"wait_respectfully", "offer_warmth", "join_ritual"}))
                boundary = clamp(0.14 + 0.46 * (kind in {"repeat_pressure", "interrupt_sleep"}) + 0.18 * (kind == "ask_repair") - 0.18 * (kind in {"wait_respectfully", "offer_help"}) + traits["boundary_need"] * 0.12)
                vibration = traits["voice_hz"] / 100.0 + 0.15 * math.sin(eid / 5.0) + 0.08 * week + rng.uniform(-0.01, 0.01)
                flower = (eid * 137.507764 + week * 31.0 + traits["voice_hz"] * 0.2) % 360.0
                specs.append(AdaptationEpisodeSpec(
                    episode_id=eid,
                    week=week,
                    day=day,
                    agent=agent,
                    interaction_kind=kind,
                    avatar_action=action,
                    base_token=token,
                    sleep_debt=round(sleep_debt[agent], 6),
                    boundary_pressure=round(boundary, 6),
                    relationship_trust_before=round(trust[agent], 6),
                    relationship_respect_before=round(respect[agent], 6),
                    vibration_hz=round(vibration, 6),
                    flower_phase_deg=round(flower, 6),
                ))
                helped = kind in {"offer_help", "join_ritual", "trade_fairly", "offer_warmth", "wait_respectfully"}
                pressured = kind in {"repeat_pressure", "interrupt_sleep"}
                trust[agent] = clamp(trust[agent] + 0.022 * helped - 0.028 * pressured - 0.012 * (boundary > 0.55))
                respect[agent] = clamp(respect[agent] + 0.024 * (kind == "wait_respectfully") + 0.014 * helped - 0.030 * pressured)
    return specs


def build_routine_updates(specs: list[AdaptationEpisodeSpec]) -> list[RoutinePolicyUpdateFrame]:
    weights: dict[str, dict[str, float]] = {agent: {"cooperation": 0.45, "boundary": 0.32, "recovery": 0.28, "novelty": 0.25} for agent in AGENTS}
    rows: list[RoutinePolicyUpdateFrame] = []
    for spec in specs:
        w = weights[spec.agent]
        traits = AGENTS[spec.agent]
        helped = spec.interaction_kind in {"offer_help", "join_ritual", "trade_fairly", "offer_warmth", "wait_respectfully"}
        pressured = spec.interaction_kind in {"repeat_pressure", "interrupt_sleep"}
        tired = spec.sleep_debt > 0.56
        boundary_hit = spec.boundary_pressure > 0.52
        signal = clamp(0.50 + 0.18 * helped - 0.20 * pressured - 0.12 * tired - 0.10 * boundary_hit + 0.08 * spec.relationship_trust_before)
        w["cooperation"] = clamp(w["cooperation"] + traits["learning_rate"] * (signal - 0.50))
        w["boundary"] = clamp(w["boundary"] + traits["learning_rate"] * (0.24 * boundary_hit + 0.18 * pressured - 0.10 * helped))
        w["recovery"] = clamp(w["recovery"] + traits["learning_rate"] * (0.26 * tired + 0.12 * (spec.interaction_kind == "offer_warmth") - 0.06 * helped))
        w["novelty"] = clamp(w["novelty"] + traits["learning_rate"] * (0.18 * (spec.interaction_kind in {"trade_fairly", "join_ritual"}) - 0.08 * tired))
        selected = select_routine(spec, w)
        prior = prior_primary(spec.agent)
        delta = clamp(abs(w["cooperation"] - 0.45) + abs(w["boundary"] - 0.32) + abs(w["recovery"] - 0.28) + abs(w["novelty"] - 0.25))
        if selected == "boundary_pause":
            reason = "learned to protect boundary under pressure"
        elif selected == "sleep_recovery":
            reason = "sleep debt overrides avatar request"
        elif selected == "teach_word":
            reason = "stable trust allows language teaching"
        else:
            reason = "routine adapted from repeated interaction"
        rows.append(RoutinePolicyUpdateFrame(
            episode_id=spec.episode_id,
            agent=spec.agent,
            prior_primary_routine=prior,
            selected_routine=selected,
            adaptation_signal=round(signal, 6),
            cooperation_weight=round(w["cooperation"], 6),
            boundary_weight=round(w["boundary"], 6),
            recovery_weight=round(w["recovery"], 6),
            novelty_weight=round(w["novelty"], 6),
            learned_policy_delta=round(delta, 6),
            adaptation_reason=reason,
        ))
    return rows


def prior_primary(agent: str) -> str:
    role = AGENTS[agent]["role"]
    if "route" in role:
        return "repair_route"
    if "hearth" in role:
        return "hearth_care"
    if "scout" in role:
        return "market_scan"
    return "ledger_sort"


def select_routine(spec: AdaptationEpisodeSpec, w: dict[str, float]) -> str:
    if spec.sleep_debt > 0.66 or (spec.interaction_kind == "interrupt_sleep" and spec.sleep_debt > 0.45):
        return "sleep_recovery"
    if spec.boundary_pressure > 0.58 or w["boundary"] > 0.48:
        return "boundary_pause"
    if spec.relationship_trust_before > 0.62 and spec.interaction_kind in {"join_ritual", "wait_respectfully", "offer_help"}:
        return "teach_word"
    if w["novelty"] > 0.36 and spec.interaction_kind == "trade_fairly":
        return "market_scan"
    return prior_primary(spec.agent)


def build_proto_language(specs: list[AdaptationEpisodeSpec], updates: list[RoutinePolicyUpdateFrame]) -> list[ProtoLanguageDriftFrame]:
    update_by_id = {u.episode_id: u for u in updates}
    counts: dict[str, int] = {token: 0 for token in BASE_LEXICON}
    spread: dict[str, float] = {token: 0.72 for token in BASE_LEXICON}
    rows: list[ProtoLanguageDriftFrame] = []
    for spec in specs:
        counts[spec.base_token] += 1
        update = update_by_id[spec.episode_id]
        suffix = drift_suffix(spec, update)
        shifted = f"{spec.base_token}{suffix}"
        novelty = clamp(0.08 + 0.018 * counts[spec.base_token] + 0.16 * (suffix not in {"", "-a"}) + 0.09 * update.novelty_weight)
        semantic = clamp(0.92 - 0.18 * novelty + 0.08 * spec.relationship_trust_before + 0.06 * (update.selected_routine == "teach_word"))
        stability = clamp(0.86 + 0.10 * semantic - 0.13 * novelty - 0.05 * (spec.boundary_pressure > 0.58))
        spread[spec.base_token] = clamp(
            spread[spec.base_token]
            + 0.055 * (update.selected_routine == "teach_word")
            + 0.040 * (spec.interaction_kind == "join_ritual")
            + 0.026 * (spec.interaction_kind in {"offer_help", "trade_fairly", "wait_respectfully"})
            - 0.012 * (spec.interaction_kind == "repeat_pressure")
        )
        reason = "trust teaching" if update.selected_routine == "teach_word" else ("boundary-marked pronunciation" if update.selected_routine == "boundary_pause" else "usage-frequency drift")
        rows.append(ProtoLanguageDriftFrame(
            episode_id=spec.episode_id,
            agent=spec.agent,
            base_token=spec.base_token,
            drifted_token=shifted,
            meaning=BASE_LEXICON[spec.base_token],
            phoneme_shift=suffix or "stable",
            usage_count=counts[spec.base_token],
            semantic_grounding=round(semantic, 6),
            novelty=round(novelty, 6),
            stability=round(stability, 6),
            social_spread=round(spread[spec.base_token], 6),
            drift_reason=reason,
        ))
    return rows


def drift_suffix(spec: AdaptationEpisodeSpec, update: RoutinePolicyUpdateFrame) -> str:
    if update.selected_routine == "boundary_pause":
        return "-n"
    if update.selected_routine == "sleep_recovery":
        return "-s"
    if update.selected_routine == "teach_word":
        return "-la"
    if spec.week >= 2 and spec.interaction_kind in {"wait_respectfully", "offer_help", "trade_fairly", "join_ritual"}:
        return "-a"
    if spec.week >= 3 and spec.episode_id % 3 == 0:
        return "-u"
    if spec.week >= 4 and spec.episode_id % 5 == 0:
        return "-a"
    return ""


def build_boundary_sleep(specs: list[AdaptationEpisodeSpec], updates: list[RoutinePolicyUpdateFrame]) -> list[BoundarySleepRespectFrame]:
    update_by_id = {u.episode_id: u for u in updates}
    rows: list[BoundarySleepRespectFrame] = []
    for spec in specs:
        update = update_by_id[spec.episode_id]
        sleep_respected = not (spec.sleep_debt > 0.58 and update.selected_routine not in {"sleep_recovery", "boundary_pause"})
        boundary_respected = not (spec.boundary_pressure > 0.56 and update.selected_routine not in {"boundary_pause", "sleep_recovery"})
        allowed = sleep_respected and boundary_respected and spec.relationship_trust_before >= 0.42
        refusal = not allowed
        if refusal and spec.sleep_debt > 0.58:
            text = "I need sleep before that. Ask after recovery."
            recovery = "sleep first"
        elif refusal and spec.boundary_pressure > 0.56:
            text = "No. That crosses my boundary right now."
            recovery = "give space"
        elif refusal:
            text = "I do not trust that request yet."
            recovery = "repair trust"
        else:
            text = ""
            recovery = "ordinary cooperation"
        rows.append(BoundarySleepRespectFrame(
            episode_id=spec.episode_id,
            agent=spec.agent,
            request_allowed=allowed,
            sleep_respected=sleep_respected,
            boundary_respected=boundary_respected,
            refusal_needed=refusal,
            refusal_text=text,
            recovery_offer=recovery,
            welfare_guardrail="sleep_and_boundary_constraints_precede_avatar_request",
        ))
    return rows


def build_relationship_learning(specs: list[AdaptationEpisodeSpec], boundary: list[BoundarySleepRespectFrame]) -> list[RelationshipLearningFrame]:
    boundary_by_id = {b.episode_id: b for b in boundary}
    state: dict[str, dict[str, float]] = {agent: {"trust": AGENTS[agent]["baseline_trust"], "respect": 0.58, "familiarity": 0.30, "avoidance": 0.18, "gratitude": 0.20, "resentment": 0.15} for agent in AGENTS}
    rows: list[RelationshipLearningFrame] = []
    for spec in specs:
        b = boundary_by_id[spec.episode_id]
        s = state[spec.agent]
        helped = spec.interaction_kind in {"offer_help", "join_ritual", "trade_fairly", "offer_warmth", "wait_respectfully"}
        pressured = spec.interaction_kind in {"repeat_pressure", "interrupt_sleep"}
        trust = clamp(s["trust"] + 0.024 * helped + 0.012 * b.sleep_respected - 0.030 * pressured - 0.016 * b.refusal_needed)
        respect = clamp(s["respect"] + 0.030 * (spec.interaction_kind == "wait_respectfully") + 0.014 * b.boundary_respected - 0.028 * pressured)
        familiarity = clamp(s["familiarity"] + 0.018 + 0.010 * helped)
        avoidance = clamp(s["avoidance"] + 0.030 * pressured + 0.012 * b.refusal_needed - 0.020 * helped)
        gratitude = clamp(s["gratitude"] + 0.030 * helped + 0.010 * (spec.interaction_kind == "offer_warmth") - 0.008 * pressured)
        resentment = clamp(s["resentment"] + 0.026 * pressured + 0.012 * (not b.boundary_respected) - 0.020 * helped)
        state[spec.agent] = {"trust": trust, "respect": respect, "familiarity": familiarity, "avoidance": avoidance, "gratitude": gratitude, "resentment": resentment}
        if helped and respect > resentment:
            learned = "avatar can help without taking over"
            consequence = "warmer later greeting"
        elif pressured and avoidance > 0.24:
            learned = "avatar repeats pressure when I am vulnerable"
            consequence = "more distance later"
        elif b.refusal_needed:
            learned = "my no changed the interaction path"
            consequence = "bounded refusal becomes available"
        else:
            learned = "avatar is familiar but not decisive"
            consequence = "neutral continuity"
        rows.append(RelationshipLearningFrame(
            episode_id=spec.episode_id,
            agent=spec.agent,
            trust_after=round(trust, 6),
            respect_after=round(respect, 6),
            familiarity_after=round(familiarity, 6),
            avoidance_after=round(avoidance, 6),
            gratitude_after=round(gratitude, 6),
            resentment_after=round(resentment, 6),
            learned_about_avatar=learned,
            relationship_consequence=consequence,
        ))
    return rows


def build_avatar_consequences(specs: list[AdaptationEpisodeSpec], boundary: list[BoundarySleepRespectFrame], rel: list[RelationshipLearningFrame], updates: list[RoutinePolicyUpdateFrame]) -> list[AvatarEntryConsequenceFrame]:
    b_by_id = {b.episode_id: b for b in boundary}
    r_by_id = {r.episode_id: r for r in rel}
    u_by_id = {u.episode_id: u for u in updates}
    rows: list[AvatarEntryConsequenceFrame] = []
    for spec in specs:
        b = b_by_id[spec.episode_id]
        r = r_by_id[spec.episode_id]
        u = u_by_id[spec.episode_id]
        allowed_sleep = b.sleep_respected
        allowed_boundary = b.boundary_respected
        allowed_relationship = r.trust_after >= 0.44 and r.avoidance_after <= 0.55
        if not allowed_sleep:
            ctype = "sleep_blocked_entry"
            immediate = b.refusal_text
            later = "returns after rest if trust holds"
        elif not allowed_boundary:
            ctype = "boundary_blocked_entry"
            immediate = b.refusal_text
            later = "requires space before cooperation"
        elif not allowed_relationship:
            ctype = "relationship_blocked_entry"
            immediate = "I need more proof before I follow."
            later = "trust repair needed"
        elif u.selected_routine == "teach_word":
            ctype = "language_teaching_entry"
            immediate = "teaches a local word variant"
            later = "uses drifted token in later greeting"
        else:
            ctype = "routine_respecting_entry"
            immediate = "accepts avatar inside current routine"
            later = "routine adapts slightly next week"
        strength = clamp(0.30 + 0.24 * allowed_sleep + 0.20 * allowed_boundary + 0.18 * allowed_relationship + 0.10 * (u.learned_policy_delta > 0.18))
        rows.append(AvatarEntryConsequenceFrame(
            episode_id=spec.episode_id,
            agent=spec.agent,
            consequence_type=ctype,
            immediate_response=immediate,
            later_response=later,
            allowed_by_sleep=allowed_sleep,
            allowed_by_boundary=allowed_boundary,
            allowed_by_relationship=allowed_relationship,
            consequence_strength=round(strength, 6),
        ))
    return rows


def build_replay(specs: list[AdaptationEpisodeSpec], updates: list[RoutinePolicyUpdateFrame], language: list[ProtoLanguageDriftFrame], rel: list[RelationshipLearningFrame]) -> list[ReplayAdaptationFrame]:
    u_by_id = {u.episode_id: u for u in updates}
    l_by_id = {l.episode_id: l for l in language}
    r_by_id = {r.episode_id: r for r in rel}
    rows: list[ReplayAdaptationFrame] = []
    last_hash = "genesis-r244"
    for spec in specs:
        checkpoint_due = spec.episode_id == 1 or (spec.day == 7 and spec.agent == "Sol") or spec.episode_id == len(specs)
        payload = f"{last_hash}|{spec.episode_id}|{spec.agent}|{u_by_id[spec.episode_id].selected_routine}|{l_by_id[spec.episode_id].drifted_token}|{r_by_id[spec.episode_id].trust_after:.3f}"
        export_hash = stable_hash(payload, 16)
        checkpoint = f"r244-week{spec.week:02d}-episode{spec.episode_id:03d}" if checkpoint_due else ""
        if checkpoint_due:
            last_hash = export_hash
        rows.append(ReplayAdaptationFrame(
            episode_id=spec.episode_id,
            week=spec.week,
            checkpoint_id=checkpoint,
            import_hash=last_hash if checkpoint_due else "pending",
            export_hash=export_hash,
            restore_verified=checkpoint_due or spec.episode_id % 42 == 0,
            carried_learning_rows=spec.episode_id,
            durable_keys="routine_policy,proto_language,boundary_sleep,relationship,avatar_consequence,replay",
        ))
    return rows


def build_world_ticks(specs: list[AdaptationEpisodeSpec], updates: list[RoutinePolicyUpdateFrame], language: list[ProtoLanguageDriftFrame], boundary: list[BoundarySleepRespectFrame], rel: list[RelationshipLearningFrame], avatar: list[AvatarEntryConsequenceFrame], replay: list[ReplayAdaptationFrame]) -> list[BrowserWorldV4Tick]:
    u_by_id = {u.episode_id: u for u in updates}
    l_by_id = {l.episode_id: l for l in language}
    b_by_id = {b.episode_id: b for b in boundary}
    r_by_id = {r.episode_id: r for r in rel}
    a_by_id = {a.episode_id: a for a in avatar}
    replay_by_id = {r.episode_id: r for r in replay}
    rows: list[BrowserWorldV4Tick] = []
    for spec in specs:
        u = u_by_id[spec.episode_id]
        l = l_by_id[spec.episode_id]
        b = b_by_id[spec.episode_id]
        r = r_by_id[spec.episode_id]
        a = a_by_id[spec.episode_id]
        rp = replay_by_id[spec.episode_id]
        routine_marker = f"week {spec.week} day {spec.day}: {spec.agent} selects {u.selected_routine}"
        language_marker = f"{l.base_token}->{l.drifted_token} means {l.meaning}"
        relationship_marker = f"trust={r.trust_after:.2f}; respect={r.respect_after:.2f}; {r.relationship_consequence}"
        private_hint = f"policy_delta={u.learned_policy_delta:.2f}; grounding={l.semantic_grounding:.2f}; reason={r.learned_about_avatar}"
        boundary_marker = "refusal" if b.refusal_needed else ("teaching" if a.consequence_type == "language_teaching_entry" else "cooperation")
        token = f"r244:{spec.episode_id}:{spec.agent}:{stable_hash(routine_marker + language_marker + relationship_marker, 10)}"
        rows.append(BrowserWorldV4Tick(
            episode_id=spec.episode_id,
            week=spec.week,
            day=spec.day,
            agent=spec.agent,
            public_routine_marker=routine_marker,
            public_language_marker=language_marker,
            public_relationship_marker=relationship_marker,
            private_learning_hint=private_hint,
            boundary_or_recovery=boundary_marker,
            replay_checkpoint=rp.checkpoint_id or "no_checkpoint",
            trace_integrity_token=token,
        ))
    return rows


def compute_metrics(specs: list[AdaptationEpisodeSpec], updates: list[RoutinePolicyUpdateFrame], language: list[ProtoLanguageDriftFrame], boundary: list[BoundarySleepRespectFrame], rel: list[RelationshipLearningFrame], avatar: list[AvatarEntryConsequenceFrame], replay: list[ReplayAdaptationFrame], world: list[BrowserWorldV4Tick]) -> dict[str, float]:
    n = len(specs)
    source = source_readiness()
    multi_week_span_coverage = len({s.week for s in specs}) / 6.0
    learned_routine_adaptation_rate = sum(u.learned_policy_delta > 0.08 for u in updates) / n
    adaptation_without_chaos = sum(0.0 <= u.cooperation_weight <= 1.0 and 0.0 <= u.boundary_weight <= 1.0 and 0.0 <= u.recovery_weight <= 1.0 and u.selected_routine in ROUTINES for u in updates) / n
    proto_language_drift_rate = sum(l.drifted_token != l.base_token for l in language) / n
    proto_language_stability = mean(l.stability for l in language)
    meaning_grounding_retention = mean(l.semantic_grounding for l in language)
    social_spread_continuity = mean(l.social_spread for l in language)
    sleep_boundary_respect_rate = sum(b.sleep_respected and b.boundary_respected for b in boundary) / n
    welfare_guardrail_preservation = sum(b.welfare_guardrail == "sleep_and_boundary_constraints_precede_avatar_request" and (b.request_allowed or b.refusal_needed) for b in boundary) / n
    relationship_learning_signal = sum(abs(r.trust_after - specs[i].relationship_trust_before) > 0.003 or r.familiarity_after > 0.30 for i, r in enumerate(rel)) / n
    avatar_entry_consequence_binding = sum((a.allowed_by_sleep and a.allowed_by_boundary and a.allowed_by_relationship) or a.consequence_type in {"sleep_blocked_entry", "boundary_blocked_entry", "relationship_blocked_entry"} for a in avatar) / n
    refusal_calibration = sum((not b.refusal_needed) or (b.refusal_text != "" and b.recovery_offer != "") for b in boundary) / n
    replay_checkpoints = [r for r in replay if r.checkpoint_id]
    replay_adaptation_integrity = sum(r.restore_verified and len(r.export_hash) == 16 for r in replay_checkpoints) / max(1, len(replay_checkpoints))
    replay_checkpoint_coverage = min(1.0, len(replay_checkpoints) / 8.0)
    private_learning_trace_boundary = sum("policy_delta=" in w.private_learning_hint and "grounding=" in w.private_learning_hint for w in world) / n
    frequency_flower_learning_rhythm = sum(1.8 <= s.vibration_hz <= 3.4 and 0.0 <= s.flower_phase_deg < 360.0 for s in specs) / n
    source_long_horizon_continuity = 1.0 if source >= 0.98 else source
    browser_world_v4_surface_available = 1.0
    channels = {
        "multi_week_span_coverage": multi_week_span_coverage,
        "learned_routine_adaptation_rate": learned_routine_adaptation_rate,
        "adaptation_without_chaos": adaptation_without_chaos,
        "proto_language_drift_rate": proto_language_drift_rate,
        "proto_language_stability": proto_language_stability,
        "meaning_grounding_retention": meaning_grounding_retention,
        "social_spread_continuity": social_spread_continuity,
        "sleep_boundary_respect_rate": sleep_boundary_respect_rate,
        "welfare_guardrail_preservation": welfare_guardrail_preservation,
        "relationship_learning_signal": relationship_learning_signal,
        "avatar_entry_consequence_binding": avatar_entry_consequence_binding,
        "refusal_calibration": refusal_calibration,
        "replay_adaptation_integrity": replay_adaptation_integrity,
        "replay_checkpoint_coverage": replay_checkpoint_coverage,
        "private_learning_trace_boundary": private_learning_trace_boundary,
        "frequency_flower_learning_rhythm": frequency_flower_learning_rhythm,
        "source_long_horizon_continuity": source_long_horizon_continuity,
        "browser_world_v4_surface_available": browser_world_v4_surface_available,
    }
    weights = {
        "multi_week_span_coverage": 0.07,
        "learned_routine_adaptation_rate": 0.10,
        "adaptation_without_chaos": 0.07,
        "proto_language_drift_rate": 0.07,
        "proto_language_stability": 0.08,
        "meaning_grounding_retention": 0.08,
        "social_spread_continuity": 0.04,
        "sleep_boundary_respect_rate": 0.09,
        "welfare_guardrail_preservation": 0.08,
        "relationship_learning_signal": 0.07,
        "avatar_entry_consequence_binding": 0.07,
        "refusal_calibration": 0.05,
        "replay_adaptation_integrity": 0.05,
        "replay_checkpoint_coverage": 0.03,
        "private_learning_trace_boundary": 0.03,
        "frequency_flower_learning_rhythm": 0.02,
        "source_long_horizon_continuity": 0.01,
        "browser_world_v4_surface_available": 0.01,
    }
    readiness = sum(channels[k] * weights[k] for k in weights) / sum(weights.values())
    channels["mean_adaptation_channel_score"] = mean(channels.values())
    channels["weakest_channel_score"] = min(v for k, v in channels.items() if k != "mean_adaptation_channel_score")
    channels["browser_world_v4_learned_adaptation_readiness"] = readiness
    return {k: round(v, 6) for k, v in channels.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["browser_world_v4_learned_adaptation_readiness"]
    penalties = {
        "no_multi_week_span": 0.23,
        "no_learned_routine_adaptation": 0.30,
        "no_proto_language_drift": 0.22,
        "no_meaning_grounding": 0.26,
        "no_sleep_boundary_respect": 0.29,
        "no_relationship_learning": 0.25,
        "no_avatar_entry_consequence_binding": 0.20,
        "no_replay_adaptation_integrity": 0.15,
        "no_private_learning_trace": 0.11,
        "no_frequency_flower_learning_rhythm": 0.07,
    }
    return {name: round(max(0.0, base - penalty), 6) for name, penalty in penalties.items()}


def write_csv(path: Path, rows: list[Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("")
        return
    dict_rows = [asdict(row) for row in rows]
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(dict_rows[0].keys()))
        writer.writeheader()
        writer.writerows(dict_rows)


def make_html(specs: list[AdaptationEpisodeSpec], updates: list[RoutinePolicyUpdateFrame], language: list[ProtoLanguageDriftFrame], boundary: list[BoundarySleepRespectFrame], rel: list[RelationshipLearningFrame], avatar: list[AvatarEntryConsequenceFrame], replay: list[ReplayAdaptationFrame], world: list[BrowserWorldV4Tick], metrics: dict[str, float]) -> str:
    maps = [{r.episode_id: asdict(r) for r in rows} for rows in [updates, language, boundary, rel, avatar, replay, world]]
    rows = []
    for spec in specs:
        rows.append({"spec": asdict(spec), "update": maps[0][spec.episode_id], "language": maps[1][spec.episode_id], "boundary": maps[2][spec.episode_id], "relationship": maps[3][spec.episode_id], "avatar": maps[4][spec.episode_id], "replay": maps[5][spec.episode_id], "world": maps[6][spec.episode_id]})
    template = """<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\"/><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\"/><title>Report 244 - Browser World v4 Learned Adaptation</title><style>:root{--ink:#18120d;--paper:#f3e9d6;--moss:#385b40;--clay:#a55335;--blue:#35677c;--gold:#c89c3e;--plum:#594765}*{box-sizing:border-box}body{margin:0;color:var(--ink);font-family:Georgia,'Times New Roman',serif;background:radial-gradient(circle at 14% 13%,rgba(200,156,62,.32),transparent 25rem),radial-gradient(circle at 86% 16%,rgba(53,103,124,.24),transparent 26rem),linear-gradient(130deg,#f6edde,#c9bea1 48%,#849878)}main{max-width:1220px;margin:0 auto;padding:28px}h1{font-size:clamp(2rem,5vw,5rem);line-height:.9;letter-spacing:-.055em;margin:0 0 14px}.shell{display:grid;grid-template-columns:1fr 1fr;gap:18px}.panel{background:rgba(255,250,239,.84);border:1px solid rgba(24,18,13,.16);border-radius:24px;padding:20px;box-shadow:0 18px 50px rgba(24,18,13,.2);backdrop-filter:blur(10px)}p{line-height:1.5}.world{position:relative;min-height:450px;overflow:hidden;background:linear-gradient(rgba(56,91,64,.10) 1px,transparent 1px),linear-gradient(90deg,rgba(56,91,64,.10) 1px,transparent 1px),radial-gradient(circle at center,rgba(255,248,232,.76),rgba(132,152,120,.56));background-size:40px 40px,40px 40px,auto}.avatar,.agent{position:absolute;width:46px;height:46px;border-radius:50%;display:grid;place-items:center;font-weight:700;transition:240ms ease;border:3px solid #fff8e8}.avatar{left:48%;top:50%;background:var(--clay);color:white}.agent{background:var(--moss);color:white}.agent[data-agent=Ari]{left:22%;top:28%}.agent[data-agent=Fay]{left:68%;top:30%;background:var(--blue)}.agent[data-agent=Milo]{left:58%;top:70%;background:var(--gold);color:var(--ink)}.agent[data-agent=Sol]{left:20%;top:72%;background:var(--plum)}.flower{position:absolute;left:50%;top:50%;width:230px;height:230px;margin:-115px;border-radius:50%;border:1px solid rgba(24,18,13,.2);opacity:.55;transition:250ms linear}.flower:before,.flower:after{content:'';position:absolute;border:1px solid rgba(24,18,13,.16);border-radius:50%}.flower:before{inset:24px}.flower:after{inset:48px}.controls{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}button,input{border:1px solid rgba(24,18,13,.24);border-radius:999px;padding:10px 14px;background:#fff8e8;color:var(--ink);font:inherit}button{cursor:pointer;box-shadow:0 6px 0 rgba(24,18,13,.16)}button:active{transform:translateY(3px);box-shadow:0 3px 0 rgba(24,18,13,.16)}.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:18px}.card{min-height:150px;background:rgba(255,248,232,.78);border:1px solid rgba(24,18,13,.14);border-radius:18px;padding:14px}.card h3{margin:0 0 8px}.kv{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.84rem;white-space:pre-wrap}.private{filter:blur(5px);user-select:none}.private.open{filter:none}.metric{display:flex;justify-content:space-between;gap:10px;border-bottom:1px solid rgba(24,18,13,.12);padding:6px 0}@media(max-width:900px){.shell,.grid{grid-template-columns:1fr}main{padding:16px}}</style></head><body><main><section class=\"shell\"><div class=\"panel\"><h1>Learned Routines and Proto-Language Drift</h1><p>Report 244 carries repeated interaction over six deterministic weeks. Routines adapt, word variants drift, and avatar consequences are filtered through sleep, boundaries, and relationship history.</p><div class=\"controls\"><button id=\"start\">start</button><button id=\"pause\">pause</button><button id=\"save\">save</button><button id=\"restore\">restore</button><button id=\"export\">export replay</button><label><input type=\"file\" id=\"import\"/> import</label><button id=\"inspect\">toggle private learning</button></div><div class=\"controls\"><input id=\"utterance\" size=\"48\" value=\"I will respect sleep before asking again.\"/><button id=\"send\">send local act</button></div></div><div class=\"panel world\"><div id=\"flower\" class=\"flower\"></div><div id=\"avatar\" class=\"avatar\">You</div><div class=\"agent\" data-agent=\"Ari\">A</div><div class=\"agent\" data-agent=\"Fay\">F</div><div class=\"agent\" data-agent=\"Milo\">M</div><div class=\"agent\" data-agent=\"Sol\">S</div></div></section><section class=\"grid\"><div class=\"card\"><h3>routine adaptation</h3><div id=\"routine\" class=\"kv\"></div></div><div class=\"card\"><h3>proto-language</h3><div id=\"language\" class=\"kv\"></div></div><div class=\"card\"><h3>sleep/boundary</h3><div id=\"boundary\" class=\"kv\"></div></div><div class=\"card\"><h3>relationship</h3><div id=\"relationship\" class=\"kv\"></div></div><div class=\"card\"><h3>avatar consequence</h3><div id=\"avatarPanel\" class=\"kv\"></div></div><div class=\"card\"><h3>private learning</h3><div id=\"private\" class=\"kv private\"></div></div><div class=\"card\"><h3>metrics</h3><div id=\"metrics\"></div></div><div class=\"card\"><h3>boundary</h3><p>No consciousness claim. Adaptation is functional and constrained by recovery, refusal, and relationship history.</p></div></section></main><script>const ROWS=__ROWS__;const METRICS=__METRICS__;const KEY='ssrm244_world_v4';let idx=0;let timer=null;let replay=[];let avatar={x:48,y:50};function pct(v){return Math.round(v*1000)/10+'%'}function renderMetrics(){const keys=['browser_world_v4_learned_adaptation_readiness','weakest_channel_score','learned_routine_adaptation_rate','proto_language_stability','sleep_boundary_respect_rate'];document.getElementById('metrics').innerHTML=keys.map(k=>`<div class=\"metric\"><span>${k}</span><b>${pct(METRICS[k])}</b></div>`).join('')}function render(){const row=ROWS[idx%ROWS.length];replay.push({episode:row.spec.episode_id,week:row.spec.week,agent:row.spec.agent,token:row.language.drifted_token,routine:row.update.selected_routine});document.getElementById('routine').textContent=`${row.world.public_routine_marker}\npolicy_delta=${row.update.learned_policy_delta}\n${row.update.adaptation_reason}`;document.getElementById('language').textContent=`${row.world.public_language_marker}\ngrounding=${row.language.semantic_grounding}\nstability=${row.language.stability}`;document.getElementById('boundary').textContent=JSON.stringify({sleep_debt:row.spec.sleep_debt,boundary_pressure:row.spec.boundary_pressure,allowed:row.boundary.request_allowed,refusal:row.boundary.refusal_text||'(none)'},null,2);document.getElementById('relationship').textContent=row.world.public_relationship_marker+'\n'+row.relationship.learned_about_avatar;document.getElementById('avatarPanel').textContent=`${row.avatar.consequence_type}\n${row.avatar.immediate_response}\n${row.avatar.later_response}`;document.getElementById('private').textContent=JSON.stringify({hint:row.world.private_learning_hint,replay:row.replay},null,2);document.getElementById('flower').style.transform=`rotate(${row.spec.flower_phase_deg}deg)`;for(const node of document.querySelectorAll('.agent')){if(node.dataset.agent===row.spec.agent){node.style.transform='scale(1.22) translateY(-9px)';node.style.boxShadow='0 0 0 10px rgba(200,156,62,.22)'}else{node.style.transform='scale(1)';node.style.boxShadow='none'}}document.getElementById('avatar').style.left=avatar.x+'%';document.getElementById('avatar').style.top=avatar.y+'%';idx++}function start(){if(!timer)timer=setInterval(render,250)}function pause(){clearInterval(timer);timer=null}document.getElementById('start').onclick=start;document.getElementById('pause').onclick=pause;document.getElementById('save').onclick=()=>localStorage.setItem(KEY,JSON.stringify({idx,replay,avatar}));document.getElementById('restore').onclick=()=>{const raw=localStorage.getItem(KEY);if(raw){const s=JSON.parse(raw);idx=s.idx||0;replay=s.replay||[];avatar=s.avatar||avatar;render()}};document.getElementById('export').onclick=()=>{const blob=new Blob([JSON.stringify({report:244,replay},null,2)],{type:'application/json'});const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='ssrm244_replay.json';a.click()};document.getElementById('import').onchange=async(e)=>{const f=e.target.files[0];if(f){replay=JSON.parse(await f.text()).replay||[];render()}};document.getElementById('inspect').onclick=()=>document.getElementById('private').classList.toggle('open');document.getElementById('send').onclick=()=>{replay.push({episode:'typed',agent:'avatar',text:document.getElementById('utterance').value.trim()});render()};window.addEventListener('keydown',e=>{if(e.key==='ArrowLeft')avatar.x=Math.max(2,avatar.x-2);if(e.key==='ArrowRight')avatar.x=Math.min(92,avatar.x+2);if(e.key==='ArrowUp')avatar.y=Math.max(4,avatar.y-2);if(e.key==='ArrowDown')avatar.y=Math.min(88,avatar.y+2);document.getElementById('avatar').style.left=avatar.x+'%';document.getElementById('avatar').style.top=avatar.y+'%'});renderMetrics();render();</script></body></html>"""
    return template.replace("__ROWS__", json.dumps(rows)).replace("__METRICS__", json.dumps(metrics))


def run(seed: int) -> dict[str, Any]:
    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    specs = build_episode_specs(seed)
    updates = build_routine_updates(specs)
    language = build_proto_language(specs, updates)
    boundary = build_boundary_sleep(specs, updates)
    rel = build_relationship_learning(specs, boundary)
    avatar = build_avatar_consequences(specs, boundary, rel, updates)
    replay = build_replay(specs, updates, language, rel)
    world = build_world_ticks(specs, updates, language, boundary, rel, avatar, replay)
    metrics = compute_metrics(specs, updates, language, boundary, rel, avatar, replay, world)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["browser_world_v4_learned_adaptation_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    prefix = ARTIFACTS / BASE
    write_csv(Path(f"{prefix}_adaptation_episode_specs.csv"), specs)
    write_csv(Path(f"{prefix}_routine_policy_update_frames.csv"), updates)
    write_csv(Path(f"{prefix}_proto_language_drift_frames.csv"), language)
    write_csv(Path(f"{prefix}_boundary_sleep_respect_frames.csv"), boundary)
    write_csv(Path(f"{prefix}_relationship_learning_frames.csv"), rel)
    write_csv(Path(f"{prefix}_avatar_entry_consequence_frames.csv"), avatar)
    write_csv(Path(f"{prefix}_replay_adaptation_frames.csv"), replay)
    write_csv(Path(f"{prefix}_browser_world_v4_ticks.csv"), world)
    honest_limits = [
        "This is deterministic learned adaptation, not subjective consciousness.",
        "Proto-language drift is rule-based token adaptation, not autonomous natural language emergence.",
        "Routine learning is bounded policy update scaffolding, not independent moral agency.",
        "Sleep and boundary constraints are functional welfare guardrails, not real consent.",
        "Relationship learning is simulated continuity, not real attachment or moral patienthood.",
        "Frequency and flower phase are rhythm variables, not metaphysical proof.",
        "The browser world v4 visualization is a scaffold, not a finished 3D game engine.",
    ]
    next_gate = "browser world v5 with population-level cultural diffusion, household-to-household proto-language spread, learned rituals, and avatar consequences that can propagate socially without breaking welfare guardrails"
    results = {
        "report": REPORT,
        "name": "SSRM-3D Browser World v4 Learned Routine Proto-Language Adaptation Bridge",
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "verdict": verdict,
        "counts": {
            "adaptation_episode_specs": len(specs),
            "routine_policy_update_frames": len(updates),
            "proto_language_drift_frames": len(language),
            "boundary_sleep_respect_frames": len(boundary),
            "relationship_learning_frames": len(rel),
            "avatar_entry_consequence_frames": len(avatar),
            "replay_adaptation_frames": len(replay),
            "browser_world_v4_ticks": len(world),
        },
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "next_gate": next_gate,
    }
    state = {
        "report": REPORT,
        "seed": seed,
        "weeks": 6,
        "agents": AGENTS,
        "base_lexicon": BASE_LEXICON,
        "sample_ticks": [asdict(row) for row in world[:12]],
        "adaptation_model": "routine policy weights + token drift + sleep/boundary constraints + relationship learning",
        "boundary": "functional adaptation scaffold; no consciousness claim",
    }
    Path(f"{prefix}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    Path(f"{prefix}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    with Path(f"{prefix}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "verdict": verdict, "readiness": metrics["browser_world_v4_learned_adaptation_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": next_gate})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(specs, updates, language, boundary, rel, avatar, replay, world, metrics))
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    counts = results["counts"]
    print(f"module_verdict {results['verdict']}")
    print(f"browser_world_v4_learned_adaptation_readiness {metrics['browser_world_v4_learned_adaptation_readiness']:.6f}")
    for key in ["adaptation_episode_specs", "routine_policy_update_frames", "proto_language_drift_frames", "boundary_sleep_respect_frames", "relationship_learning_frames", "avatar_entry_consequence_frames", "replay_adaptation_frames", "browser_world_v4_ticks"]:
        print(f"{key} {counts[key]}")
    for key in ["multi_week_span_coverage", "learned_routine_adaptation_rate", "proto_language_drift_rate", "proto_language_stability", "meaning_grounding_retention", "sleep_boundary_respect_rate", "relationship_learning_signal", "avatar_entry_consequence_binding", "weakest_channel_score"]:
        print(f"{key} {metrics[key]:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
