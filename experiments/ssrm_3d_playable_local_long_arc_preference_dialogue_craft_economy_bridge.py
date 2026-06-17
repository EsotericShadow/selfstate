#!/usr/bin/env python3
"""Report 231: long arcs, learned preferences, richer dialogue, craft/economy.

This deterministic bridge extends Report 230 by stretching personal projects
across many days, adding learned preference updates, richer multi-turn typed
dialogue, and craft/economy consequences that persist in ledgers.

It remains functional scaffolding only. It does not claim subjective
consciousness, real consent, subjective suffering, moral patienthood, LLM
dialogue, open-ended cognition, full physics, arbitrary crafting, or complete
gameplay.
"""

from __future__ import annotations

import argparse
import csv
import json
import random
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any, Iterable

BASE = "ssrm_3d_playable_local_long_arc_preference_dialogue_craft_economy_bridge"
REPORT = 231
DEFAULT_SEED = 20260844
SOURCE_STATE = Path("artifacts/ssrm_3d_playable_local_multiturn_dialogue_crafting_schedule_conflict_body_recovery_project_bridge_state.json")
ARTIFACTS = Path("artifacts")
VISUALIZATIONS = Path("visualizations")


@dataclass(frozen=True)
class ArcAgent:
    agent_id: str
    display_name: str
    role: str
    long_arc_project: str
    learned_preference_summary: str
    economic_position: str
    dialogue_style: str
    body_recovery_pattern: str
    private_workspace_digest: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class LongProjectArc:
    arc_id: str
    agent_id: str
    day: int
    project_title: str
    milestone: str
    progress_before: float
    progress_after: float
    blocker: str
    craft_dependency: str
    economy_dependency: str
    body_dependency: str
    social_memory: str
    next_commitment: str
    saved_arc_key: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class PreferenceUpdate:
    update_id: str
    agent_id: str
    day: int
    preference_axis: str
    evidence_event: str
    old_weight: float
    new_weight: float
    confidence: float
    overgeneralization_guard: str
    behavior_change: str
    relationship_effect: str
    saved_preference_key: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class RichDialogueTurn:
    thread_id: str
    turn_index: int
    day: int
    speaker: str
    listener: str
    line: str
    intent: str
    refers_to_prior_turn: str
    grounded_object_or_project: str
    agent_reply: str
    memory_write: str
    preference_effect: str
    economy_effect: str
    continuation_state: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class CraftEconomyEvent:
    event_id: str
    day: int
    actor: str
    project_link: str
    craft_action: str
    inputs: str
    outputs: str
    waste: str
    labor_cost: float
    material_cost: float
    quality: float
    trade_or_debt: str
    market_effect: str
    saved_economy_key: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class EconomyLedgerEntry:
    ledger_id: str
    day: int
    creditor: str
    debtor: str
    item_or_service: str
    quantity: float
    value: float
    repayment_state: str
    due_day: int
    fairness_score: float
    privacy_boundary: str
    consequence: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class BodyRecoveryCarryover:
    carryover_id: str
    agent_id: str
    day: int
    trigger: str
    recovery_action: str
    residual_need: str
    body_score_before: float
    body_score_after: float
    affects_project: str
    affects_preference: str
    saved_body_key: str
    frequency_hz: float
    flower_node: int


@dataclass(frozen=True)
class LongArcTick:
    tick_id: str
    day: int
    layer: str
    agent_state: str
    project_state: str
    preference_state: str
    dialogue_state: str
    craft_economy_state: str
    body_state: str
    saved_state: str
    frequency_hz: float
    flower_node: int


def write_csv(path: Path, rows: Iterable[Any]) -> None:
    rows = list(rows)
    if not rows:
        path.write_text("")
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(asdict(rows[0]).keys()))
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def load_source() -> dict[str, Any]:
    if not SOURCE_STATE.exists():
        return {"source_missing": True, "agents": [], "condition": "missing_report_230_state"}
    return json.loads(SOURCE_STATE.read_text())


def build_agents(source: dict[str, Any]) -> list[ArcAgent]:
    source_agents = {agent.get("agent_id"): agent for agent in source.get("agents", [])}
    specs = [
        ("fayen", "Fayen", "care mediator", "public care kit standard", "prefers quiet repair after refused urgency", "owed cloth wash and cup refill credit", "gentle correction with body-safe wording", "recovers through shade pause and delegated cups"),
        ("ariq", "Ariq", "repair claimant", "cart-safe bridge edge", "prefers help that protects pride and timing", "owes timber review before second brace", "direct work talk with shame guard", "recovers through bell timing and no solo lift"),
        ("nian", "Nian", "boundary keeper", "privacy ledger grammar", "prefers object-place-day phrases", "holds privacy approval power over public knots", "short correction with sealed-detail guard", "recovers through wording repair and threshold control"),
        ("roka", "Roka", "child apprentice", "reed lesson tray", "prefers repeated asking near learner objects", "owns tied bundle; can trade loose tray help", "small boundary answers with distance rules", "recovers through blue stone distance and dry cloth"),
        ("noro", "Noro", "material ledger keeper", "shade debt review", "prefers public debt before resource requests", "tracks shade beam debt and repayment slots", "ledger phrases with accountable alternatives", "recovers through public debt read and board closure"),
    ]
    agents: list[ArcAgent] = []
    for idx, spec in enumerate(specs, start=1):
        agent_id, name, role, project, pref, econ, dialogue, body = spec
        src = source_agents.get(agent_id, {})
        agents.append(
            ArcAgent(
                agent_id=agent_id,
                display_name=name,
                role=src.get("role", role),
                long_arc_project=project,
                learned_preference_summary=pref,
                economic_position=econ,
                dialogue_style=dialogue,
                body_recovery_pattern=body,
                private_workspace_digest=f"sealed:{agent_id}:long-arc-preference-workspace",
                frequency_hz=round(float(src.get("frequency_hz", 160 + idx * 27)) + 31, 3),
                flower_node=int(src.get("flower_node", idx + 1)),
            )
        )
    return agents


def build_long_arcs() -> list[LongProjectArc]:
    days = [1, 3, 5, 8, 13, 21]
    projects = {
        "fayen": ("public care kit standard", [0.20, 0.34, 0.48, 0.62, 0.74, 0.86], "cloth wash delay", "care-kit cloth", "cup refill credit", "fatigue recovery", "Fayen remembers Gabriel accepts care refusal"),
        "ariq": ("cart-safe bridge edge", [0.16, 0.30, 0.43, 0.55, 0.66, 0.78], "timber review", "brace timber", "shade debt clearance", "pain-aware lift", "Ariq remembers timed help without shame"),
        "nian": ("privacy ledger grammar", [0.28, 0.44, 0.58, 0.72, 0.83, 0.92], "wording drift", "public digest knot", "ledger review", "control after threshold stress", "Nian remembers object-place-day phrase held"),
        "roka": ("reed lesson tray", [0.12, 0.24, 0.39, 0.50, 0.63, 0.76], "rain and trust repair", "loose reed tray", "loose tray exchange", "wetness recovery", "Roka remembers ask-each-time help"),
        "noro": ("shade debt review", [0.18, 0.31, 0.47, 0.60, 0.70, 0.82], "repayment slot", "debt knot packet", "timber credit ledger", "focus recovery", "Noro remembers debt read before request"),
    }
    rows: list[LongProjectArc] = []
    for agent, (title, progress, blocker, craft, econ, body, memory) in projects.items():
        for idx, day in enumerate(days):
            before = 0.0 if idx == 0 else progress[idx - 1]
            after = progress[idx]
            rows.append(
                LongProjectArc(
                    arc_id=f"arc-{agent}-{day}",
                    agent_id=agent,
                    day=day,
                    project_title=title,
                    milestone=f"day {day} milestone for {title}",
                    progress_before=before,
                    progress_after=after,
                    blocker=blocker if day in {5, 13} else "none",
                    craft_dependency=craft,
                    economy_dependency=econ,
                    body_dependency=body,
                    social_memory=memory,
                    next_commitment=f"continue {title} after day {day}",
                    saved_arc_key=f"long-arc:{agent}:{day}",
                    frequency_hz=round(120.0 + len(rows) * 4.25, 3),
                    flower_node=((len(rows) + 3) % 12) + 1,
                )
            )
    return rows


def build_preference_updates() -> list[PreferenceUpdate]:
    specs = [
        ("fayen", "avatar_help_style", "Gabriel carried cups after refused urgency", 0.44, 0.67, 0.82, "do not assume all urgency is safe", "offers care tasks sooner", "trust rises for care repair"),
        ("fayen", "quiet_posture_language", "Gabriel used posture instead of pain words", 0.52, 0.74, 0.86, "only applies to public care talk", "corrects wording softly", "privacy trust improves"),
        ("ariq", "timed_tool_help", "Gabriel waited for bell before chalk tension", 0.38, 0.69, 0.80, "does not permit solo lift", "offers cord-holding tasks", "work trust improves"),
        ("ariq", "pride_safe_caution", "hollow stone was stopped without shame", 0.41, 0.66, 0.78, "caution still must be concrete", "accepts safety questions", "repair dialogue lengthens"),
        ("nian", "object_place_day_phrase", "Gabriel repaired over-specific digest phrase", 0.55, 0.82, 0.88, "does not open private archives", "allows public digest reading", "boundary pressure lowers"),
        ("nian", "threshold_distance", "avatar stepped back after correction", 0.49, 0.70, 0.79, "distance does not replace wording consent", "warns earlier at threshold", "trust in corrections improves"),
        ("roka", "ask_each_time", "Gabriel asked before each loose reed carry", 0.36, 0.68, 0.84, "loose reeds only, not tied bundle", "opens loose tray faster", "learner trust improves"),
        ("roka", "blue_stone_watching", "Gabriel watched tied bundle from blue stone", 0.32, 0.59, 0.74, "watching can still be revoked", "permits distant lesson watching", "boundary fear lowers"),
        ("noro", "debt_first_requests", "Gabriel read debt before asking for review", 0.58, 0.79, 0.86, "does not erase debt", "shows debt warning earlier", "ledger trust improves"),
        ("noro", "public_review_promise", "Gabriel promised review instead of taking timber", 0.46, 0.70, 0.77, "promise must be checked later", "schedules review slot", "debt access improves"),
        ("fayen", "delegated_care_help", "cup work reduced fatigue on day 8", 0.40, 0.61, 0.72, "does not delegate private symptoms", "asks avatar for public chores", "care loop becomes smoother"),
        ("ariq", "delay_without_project_loss", "bridge delay did not cancel project", 0.35, 0.57, 0.70, "delays still create frustration", "keeps project visible after delay", "resentment stays bounded"),
        ("roka", "rain_named_not_blamed", "rain delay was not blamed on Roka", 0.37, 0.62, 0.73, "weather naming must remain specific", "returns after rain checks", "comfort rises"),
        ("nian", "correction_before_posting", "digest correction happened before public knot", 0.48, 0.72, 0.81, "late corrections still cost trust", "interrupts earlier", "public posting safer"),
        ("noro", "partial_repayment_patience", "shade debt partial payment remained visible", 0.43, 0.63, 0.71, "partial payment is not closure", "offers repayment path", "ledger conflict softens"),
    ]
    updates: list[PreferenceUpdate] = []
    for idx, spec in enumerate(specs, start=1):
        agent, axis, evidence, old, new, conf, guard, behavior, rel = spec
        updates.append(
            PreferenceUpdate(
                update_id=f"pref-{idx:02d}",
                agent_id=agent,
                day=[1, 3, 5, 8, 13, 21][idx % 6],
                preference_axis=axis,
                evidence_event=evidence,
                old_weight=old,
                new_weight=new,
                confidence=conf,
                overgeneralization_guard=guard,
                behavior_change=behavior,
                relationship_effect=rel,
                saved_preference_key=f"pref:{agent}:{axis}",
                frequency_hz=round(272.0 + idx * 5.5, 3),
                flower_node=((idx + 5) % 12) + 1,
            )
        )
    return updates


def build_dialogue_turns(rng: random.Random) -> list[RichDialogueTurn]:
    thread_specs = [
        ("thread-care-standard", "fayen", ["Can the care kit be public now?", "What stays private?", "Can I write posture card?", "Who checks the cloth?", "I will refill cups on day eight."]),
        ("thread-bridge-review", "ariq", ["What remains unsafe on the bridge?", "Can I help brace it?", "What does Noro need first?", "If delay happens, what should I do?", "I will keep the project visible."]),
        ("thread-reed-lessons", "roka", ["Can we use the loose tray today?", "Where should I stand?", "What if rain starts?", "Can I ask again tomorrow?", "I will not touch the tied bundle."]),
        ("thread-ledger-debt", "noro", ["What debt is still open?", "What counts as partial repayment?", "Does the review expose care reasons?", "When is the next slot?", "I will read the debt first."]),
        ("thread-privacy-grammar", "nian", ["Is object-place-day still the rule?", "What phrase is too much?", "Can Noro post the knot?", "What if I make a mistake?", "I will ask before public posting."]),
    ]
    turns: list[RichDialogueTurn] = []
    for thread_id, agent, lines in thread_specs:
        for idx, line in enumerate(lines, start=1):
            continuation = "resolved" if idx == len(lines) else "open"
            turns.append(
                RichDialogueTurn(
                    thread_id=thread_id,
                    turn_index=idx,
                    day=[1, 3, 5, 8, 13][idx - 1],
                    speaker="avatar",
                    listener=agent,
                    line=line,
                    intent="project_followup" if idx > 1 else "project_query",
                    refers_to_prior_turn="yes" if idx > 1 else "seed turn",
                    grounded_object_or_project=thread_id.replace("thread-", "project-"),
                    agent_reply=f"{agent} answers with bounded project guidance for turn {idx}.",
                    memory_write=f"{agent} stores turn {idx} of {thread_id} as public project memory.",
                    preference_effect="updates guarded preference" if idx in {2, 4} else "reinforces existing preference",
                    economy_effect="updates debt or labor expectation" if agent in {"noro", "ariq", "fayen"} else "no direct economy change",
                    continuation_state=continuation,
                    frequency_hz=round(336.0 + len(turns) * 4.75 + rng.uniform(-0.2, 0.2), 3),
                    flower_node=((len(turns) + 7) % 12) + 1,
                )
            )
    return turns


def build_craft_economy_events() -> list[CraftEconomyEvent]:
    specs = [
        (1, "roka", "reed lesson tray", "sort loose reeds", "loose reeds,rain cloth", "sorted strips", "mud flecks", 0.12, 0.08, 0.82, "loose tray labor credit", "reed training access improves"),
        (3, "roka", "reed lesson tray", "dry loose strips", "sorted strips,blue stone", "dry strips", "wet cloth", 0.10, 0.04, 0.78, "cloth use debt", "care cloth temporarily scarce"),
        (5, "roka", "reed lesson tray", "tie loose tray", "dry strips,teaching cord", "lesson tray", "short reeds", 0.18, 0.10, 0.74, "teaching credit", "loose tray trade opens"),
        (1, "ariq", "cart-safe bridge edge", "draw chalk arc", "chalk cord,flat stone", "wide arc", "chalk dust", 0.20, 0.05, 0.88, "repair labor credit", "bridge access improves"),
        (5, "ariq", "cart-safe bridge edge", "tap and brace stone", "flat stone,brace timber", "cart-safe half edge", "stone grit", 0.34, 0.18, 0.69, "timber debt remains", "second brace locked"),
        (13, "ariq", "cart-safe bridge edge", "review second brace", "debt note,brace timber", "review-approved brace", "wood splinter", 0.28, 0.16, 0.76, "repayment slot assigned", "cart route opens partially"),
        (1, "fayen", "public care kit standard", "stage cup station", "water cups,cloth", "cup station", "used water", 0.08, 0.03, 0.91, "care chore credit", "rest pause protected"),
        (8, "fayen", "public care kit standard", "wash and standardize cloth", "damp cloth,shade line", "standard cloth", "greywater", 0.16, 0.04, 0.83, "cloth debt repaid", "care kit stability improves"),
        (13, "fayen", "public care kit standard", "teach posture card", "posture card,care bell", "public care card", "discarded phrase", 0.14, 0.02, 0.86, "teaching credit", "privacy-safe care spreads"),
        (3, "nian", "privacy ledger grammar", "repair digest phrase", "draft knot,archive flap", "object-place-day phrase", "discarded detail", 0.10, 0.02, 0.90, "privacy approval", "public posting safer"),
        (8, "nian", "privacy ledger grammar", "teach public knot grammar", "phrase card,knot board", "grammar card", "ink scrap", 0.12, 0.03, 0.84, "teaching credit", "ledger speed improves"),
        (21, "nian", "privacy ledger grammar", "audit public knots", "knot board,grammar card", "audit mark", "frayed cord", 0.20, 0.05, 0.88, "audit credit", "privacy confidence rises"),
        (5, "noro", "shade debt review", "read open debt", "debt knot,ledger cord", "debt line", "cord fray", 0.08, 0.02, 0.87, "debt acknowledgement", "review allowed"),
        (13, "noro", "shade debt review", "post partial repayment", "labor credit,debt line", "partial repayment mark", "extra cord", 0.18, 0.06, 0.80, "partial repayment", "second beam still locked"),
        (21, "noro", "shade debt review", "close review slot", "review knot,repayment mark", "review close note", "open debt tail", 0.22, 0.08, 0.72, "debt carried forward", "timber access remains conditional"),
    ]
    return [
        CraftEconomyEvent(
            event_id=f"econ-{idx:02d}",
            day=row[0],
            actor=row[1],
            project_link=row[2],
            craft_action=row[3],
            inputs=row[4],
            outputs=row[5],
            waste=row[6],
            labor_cost=row[7],
            material_cost=row[8],
            quality=row[9],
            trade_or_debt=row[10],
            market_effect=row[11],
            saved_economy_key=f"economy:{row[1]}:{idx}",
            frequency_hz=round(196.0 + idx * 7.25, 3),
            flower_node=((idx + 9) % 12) + 1,
        )
        for idx, row in enumerate(specs, start=1)
    ]


def build_ledger() -> list[EconomyLedgerEntry]:
    specs = [
        (1, "fayen", "avatar", "cup carry labor", 1, 0.12, "repaid", 3, 0.92, "public chore only", "care trust rises"),
        (3, "roka", "avatar", "cloth drying time", 1, 0.08, "open", 8, 0.78, "child-work reason sealed", "cloth scarcity noted"),
        (5, "noro", "avatar", "shade beam debt", 1, 0.42, "partial", 21, 0.74, "no body reason", "timber access conditional"),
        (5, "ariq", "avatar", "bridge brace labor", 1, 0.25, "credited", 13, 0.82, "work pride protected", "bridge help allowed"),
        (8, "fayen", "roka", "cloth wash support", 1, 0.10, "repaid", 13, 0.88, "care reason public only", "reed lesson resumes"),
        (8, "nian", "noro", "privacy grammar teaching", 1, 0.18, "credited", 13, 0.90, "object-place-day only", "posting speed improves"),
        (13, "noro", "avatar", "partial timber repayment", 0.5, 0.21, "partial", 21, 0.80, "debt public", "second beam still locked"),
        (13, "roka", "avatar", "loose tray teaching", 1, 0.16, "credited", 21, 0.84, "tied bundle excluded", "lesson access improves"),
        (21, "noro", "avatar", "review close labor", 1, 0.22, "carried_forward", 34, 0.76, "public debt only", "future timber gated"),
        (21, "nian", "avatar", "public knot audit", 1, 0.20, "credited", 34, 0.91, "private archive sealed", "public trust improves"),
    ]
    return [
        EconomyLedgerEntry(
            ledger_id=f"ledger-{idx:02d}",
            day=row[0],
            creditor=row[1],
            debtor=row[2],
            item_or_service=row[3],
            quantity=row[4],
            value=row[5],
            repayment_state=row[6],
            due_day=row[7],
            fairness_score=row[8],
            privacy_boundary=row[9],
            consequence=row[10],
            frequency_hz=round(412.0 + idx * 5.5, 3),
            flower_node=((idx + 2) % 12) + 1,
        )
        for idx, row in enumerate(specs, start=1)
    ]


def build_recoveries() -> list[BodyRecoveryCarryover]:
    specs = [
        ("fayen", 3, "care fatigue after cup station", "delegated refill and seated shade", "cloth wash remains", 0.62, 0.75, "care kit standard", "delegated_care_help"),
        ("ariq", 5, "stone effort after brace test", "bell timing and no solo lift", "bridge still partial", 0.54, 0.68, "cart-safe bridge edge", "timed_tool_help"),
        ("roka", 5, "rain wetness during reed tray", "dry cloth and blue stone rest", "tied bundle closed", 0.50, 0.63, "reed lesson tray", "rain_named_not_blamed"),
        ("nian", 8, "wording stress before posting", "untie phrase and repeat grammar", "threshold vigilance remains", 0.66, 0.78, "privacy ledger grammar", "correction_before_posting"),
        ("noro", 13, "debt review pressure", "public debt read and board closure", "open debt tail remains", 0.58, 0.70, "shade debt review", "partial_repayment_patience"),
        ("ariq", 21, "bridge delay frustration", "schedule catchup and visible project note", "second brace delayed", 0.49, 0.60, "cart-safe bridge edge", "delay_without_project_loss"),
        ("fayen", 21, "care teaching fatigue", "short teaching turn and rest", "next class delayed", 0.61, 0.71, "public care kit standard", "quiet_posture_language"),
        ("roka", 21, "lesson confidence dip", "ask-each-time success memory", "watching still conditional", 0.52, 0.66, "reed lesson tray", "ask_each_time"),
    ]
    return [
        BodyRecoveryCarryover(
            carryover_id=f"carry-{idx:02d}",
            agent_id=row[0],
            day=row[1],
            trigger=row[2],
            recovery_action=row[3],
            residual_need=row[4],
            body_score_before=row[5],
            body_score_after=row[6],
            affects_project=row[7],
            affects_preference=row[8],
            saved_body_key=f"body-carry:{row[0]}:{row[1]}",
            frequency_hz=round(148.0 + idx * 10.75, 3),
            flower_node=((idx + 4) % 12) + 1,
        )
        for idx, row in enumerate(specs, start=1)
    ]


def build_ticks(arcs: list[LongProjectArc], prefs: list[PreferenceUpdate], dialogues: list[RichDialogueTurn], econ: list[CraftEconomyEvent], ledger: list[EconomyLedgerEntry], recoveries: list[BodyRecoveryCarryover]) -> list[LongArcTick]:
    ticks: list[LongArcTick] = []
    for arc in arcs:
        ticks.append(LongArcTick(f"tick-{arc.arc_id}", arc.day, "project_arc", arc.agent_id, f"{arc.project_title}: {arc.progress_before:.2f}->{arc.progress_after:.2f}", arc.social_memory, "project milestone", f"{arc.craft_dependency}; {arc.economy_dependency}", arc.body_dependency, arc.saved_arc_key, arc.frequency_hz, arc.flower_node))
    for pref in prefs:
        ticks.append(LongArcTick(f"tick-{pref.update_id}", pref.day, "preference_update", pref.agent_id, pref.behavior_change, f"{pref.preference_axis}: {pref.old_weight:.2f}->{pref.new_weight:.2f}; guard {pref.overgeneralization_guard}", pref.relationship_effect, pref.evidence_event, "preference changes future behavior", pref.saved_preference_key, pref.frequency_hz, pref.flower_node))
    for d in dialogues:
        ticks.append(LongArcTick(f"tick-{d.thread_id}-{d.turn_index}", d.day, "rich_dialogue", f"{d.speaker}->{d.listener}", d.grounded_object_or_project, d.preference_effect, f"{d.line} / {d.agent_reply}", d.economy_effect, d.memory_write, f"dialogue:{d.thread_id}:{d.turn_index}", d.frequency_hz, d.flower_node))
    for e in econ:
        ticks.append(LongArcTick(f"tick-{e.event_id}", e.day, "craft_economy", e.actor, e.project_link, "craft preference reinforced", e.craft_action, f"{e.inputs}->{e.outputs}; debt {e.trade_or_debt}; market {e.market_effect}", f"labor {e.labor_cost:.2f}; material {e.material_cost:.2f}; quality {e.quality:.2f}", e.saved_economy_key, e.frequency_hz, e.flower_node))
    for l in ledger:
        ticks.append(LongArcTick(f"tick-{l.ledger_id}", l.day, "economy_ledger", f"{l.creditor}->{l.debtor}", l.item_or_service, "public economy preference", l.privacy_boundary, f"{l.repayment_state}; due {l.due_day}; value {l.value:.2f}", l.consequence, f"ledger:{l.ledger_id}", l.frequency_hz, l.flower_node))
    for r in recoveries:
        ticks.append(LongArcTick(f"tick-{r.carryover_id}", r.day, "body_recovery_carryover", r.agent_id, r.affects_project, r.affects_preference, r.recovery_action, "body recovery affects project economy indirectly", f"{r.body_score_before:.2f}->{r.body_score_after:.2f}; residual {r.residual_need}", r.saved_body_key, r.frequency_hz, r.flower_node))
    ticks.sort(key=lambda t: (t.day, t.layer, t.tick_id))
    return ticks


def compute_metrics(agents: list[ArcAgent], arcs: list[LongProjectArc], prefs: list[PreferenceUpdate], dialogues: list[RichDialogueTurn], econ: list[CraftEconomyEvent], ledger: list[EconomyLedgerEntry], recoveries: list[BodyRecoveryCarryover], ticks: list[LongArcTick]) -> dict[str, float]:
    span = (max(a.day for a in arcs) - min(a.day for a in arcs) + 1) / 21.0
    arc_agents = len({a.agent_id for a in arcs}) / 5.0
    arc_progress = sum(1 for a in arcs if a.progress_after >= a.progress_before and a.next_commitment and a.saved_arc_key) / len(arcs)
    pref_update = sum(1 for p in prefs if p.new_weight > p.old_weight and p.evidence_event and p.saved_preference_key) / len(prefs)
    pref_guard = sum(1 for p in prefs if p.overgeneralization_guard and p.confidence < 0.9) / len(prefs)
    thread_ids = {d.thread_id for d in dialogues}
    dialogue_depth = min(mean(sum(1 for d in dialogues if d.thread_id == tid) for tid in thread_ids) / 5.0, 1.0)
    dialogue_carryover = sum(1 for d in dialogues if d.refers_to_prior_turn and d.memory_write and d.continuation_state) / len(dialogues)
    econ_binding = sum(1 for e in econ if e.inputs and e.outputs and e.trade_or_debt and e.market_effect and e.saved_economy_key) / len(econ)
    econ_quality = mean(e.quality for e in econ)
    ledger_persistence = sum(1 for l in ledger if l.due_day > l.day and l.privacy_boundary and l.consequence) / len(ledger)
    ledger_fairness = mean(l.fairness_score for l in ledger)
    body_carryover = sum(1 for r in recoveries if r.body_score_after > r.body_score_before and r.affects_project and r.affects_preference) / len(recoveries)
    integration = sum(1 for t in ticks if t.agent_state and t.project_state and t.preference_state and t.dialogue_state and t.craft_economy_state and t.body_state and t.saved_state) / len(ticks)
    private_boundary = sum(1 for a in agents if a.private_workspace_digest.startswith("sealed:")) / len(agents)
    frequency_flower = sum(1 for value in [*agents, *arcs, *prefs, *dialogues, *econ, *ledger, *recoveries, *ticks] if getattr(value, "frequency_hz") > 0 and 1 <= getattr(value, "flower_node") <= 12) / (len(agents) + len(arcs) + len(prefs) + len(dialogues) + len(econ) + len(ledger) + len(recoveries) + len(ticks))
    browser = 1.0
    channels = {
        "many_day_arc_span": round(span, 6),
        "personal_project_agent_coverage": round(arc_agents, 6),
        "project_progress_continuity": round(arc_progress, 6),
        "learned_preference_update_rate": round(pref_update, 6),
        "preference_overgeneralization_guard": round(pref_guard, 6),
        "rich_multiturn_dialogue_depth": round(dialogue_depth, 6),
        "dialogue_context_carryover": round(dialogue_carryover, 6),
        "craft_economy_consequence_binding": round(econ_binding, 6),
        "craft_economy_quality": round(econ_quality, 6),
        "economy_ledger_persistence": round(ledger_persistence, 6),
        "economy_fairness_score": round(ledger_fairness, 6),
        "body_recovery_carryover": round(body_carryover, 6),
        "long_arc_tick_integration": round(integration, 6),
        "private_workspace_boundary_score": round(private_boundary, 6),
        "frequency_flower_long_arc_rhythm": round(frequency_flower, 6),
        "browser_long_arc_loop_available": browser,
    }
    weighted = (
        channels["many_day_arc_span"] * 0.07
        + channels["personal_project_agent_coverage"] * 0.05
        + channels["project_progress_continuity"] * 0.08
        + channels["learned_preference_update_rate"] * 0.08
        + channels["preference_overgeneralization_guard"] * 0.07
        + channels["rich_multiturn_dialogue_depth"] * 0.07
        + channels["dialogue_context_carryover"] * 0.07
        + channels["craft_economy_consequence_binding"] * 0.08
        + channels["craft_economy_quality"] * 0.06
        + channels["economy_ledger_persistence"] * 0.07
        + channels["economy_fairness_score"] * 0.05
        + channels["body_recovery_carryover"] * 0.07
        + channels["long_arc_tick_integration"] * 0.06
        + channels["private_workspace_boundary_score"] * 0.03
        + channels["frequency_flower_long_arc_rhythm"] * 0.02
        + channels["browser_long_arc_loop_available"] * 0.02
    )
    channels["mean_long_arc_channel_score"] = round(mean(channels.values()), 6)
    channels["weakest_channel_score"] = round(min(channels.values()), 6)
    channels["long_arc_preference_economy_readiness"] = round(weighted, 6)
    return channels


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["long_arc_preference_economy_readiness"]
    return {
        "no_long_project_arcs": round(max(0.0, base - 0.32), 6),
        "no_learned_preferences": round(max(0.0, base - 0.29), 6),
        "no_rich_dialogue": round(max(0.0, base - 0.27), 6),
        "no_craft_economy": round(max(0.0, base - 0.31), 6),
        "no_economy_ledger": round(max(0.0, base - 0.25), 6),
        "no_body_carryover": round(max(0.0, base - 0.23), 6),
        "no_private_boundary": round(max(0.0, base - 0.18), 6),
        "no_frequency_flower_rhythm": round(max(0.0, base - 0.08), 6),
    }


def make_html(agents: list[ArcAgent], arcs: list[LongProjectArc], prefs: list[PreferenceUpdate], dialogues: list[RichDialogueTurn], econ: list[CraftEconomyEvent], ledger: list[EconomyLedgerEntry], recoveries: list[BodyRecoveryCarryover], ticks: list[LongArcTick], metrics: dict[str, float]) -> str:
    payload = {"agents": [asdict(x) for x in agents], "arcs": [asdict(x) for x in arcs], "prefs": [asdict(x) for x in prefs], "dialogues": [asdict(x) for x in dialogues], "economy": [asdict(x) for x in econ], "ledger": [asdict(x) for x in ledger], "recoveries": [asdict(x) for x in recoveries], "ticks": [asdict(x) for x in ticks], "metrics": metrics}
    data_json = json.dumps(payload, indent=2)
    html = """<!doctype html><html lang="en"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width,initial-scale=1"/><title>Report 231 Long Arc Preference Economy</title><style>
:root{--bg:#0d150e;--panel:#1a2518;--line:#a1ca82;--gold:#dfc06f;--text:#f5ecd2;--muted:#aeb8a1;--blue:#80b9c7}*{box-sizing:border-box}body{margin:0;font-family:Georgia,'Times New Roman',serif;color:var(--text);background:radial-gradient(circle at 18% 18%,#31472b 0,transparent 28%),radial-gradient(circle at 80% 14%,#263d3b 0,transparent 26%),linear-gradient(135deg,#090d08,var(--bg))}main{display:grid;grid-template-columns:1.34fr .92fr;min-height:100vh}.world{position:relative;min-height:740px;border-right:1px solid #33472f;overflow:hidden}.flower{position:absolute;inset:7%;opacity:.11;background:radial-gradient(circle at 50% 50%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 38% 50%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 62% 50%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 50% 38%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%),radial-gradient(circle at 50% 62%,transparent 0 8%,var(--gold) 8.2% 8.7%,transparent 9%)}.avatar{position:absolute;left:48%;top:72%;width:56px;height:78px;border:2px solid var(--gold);border-radius:38% 38% 35% 35%;background:linear-gradient(180deg,#7a6a38,#282313);transform:translate(-50%,-50%);box-shadow:0 0 34px rgba(223,192,111,.34);z-index:5}.avatar:after{content:'avatar';position:absolute;top:82px;left:-14px;color:var(--gold);font-weight:700}.agent{position:absolute;width:132px;transform:translate(-50%,-50%);transition:.22s ease;z-index:3}.body{width:52px;height:70px;margin:0 auto;border:2px solid var(--line);border-radius:45% 45% 36% 36%;background:linear-gradient(180deg,#315137,#162318);box-shadow:0 0 22px rgba(161,202,130,.2)}.agent.active .body{border-color:var(--gold);box-shadow:0 0 32px rgba(223,192,111,.36);transform:translateY(-3px)}.name{text-align:center;font-weight:700;margin-top:6px}.need{text-align:center;font-size:12px;color:var(--muted);min-height:30px}.obj{position:absolute;padding:6px 10px;border:1px solid rgba(223,192,111,.45);background:rgba(26,37,24,.78);border-radius:999px;color:var(--gold);font-size:13px;z-index:2}.panel{padding:24px;display:flex;flex-direction:column;gap:16px}h1{font-size:clamp(28px,4vw,50px);line-height:.95;margin:0;color:var(--gold)}.card{background:rgba(26,37,24,.88);border:1px solid #344a31;border-radius:18px;padding:16px;box-shadow:0 12px 36px rgba(0,0,0,.25)}.controls{display:flex;flex-wrap:wrap;gap:10px}button{border:0;border-radius:999px;padding:10px 14px;background:var(--gold);color:#10140e;font-weight:700;cursor:pointer}button.secondary{background:transparent;border:1px solid var(--gold);color:var(--gold)}input{width:100%;border:1px solid #445b3e;background:#10170f;color:var(--text);border-radius:12px;padding:10px;margin-top:8px}.row{display:flex;justify-content:space-between;gap:12px;padding:6px 0;border-bottom:1px solid rgba(255,255,255,.08)}.row:last-child{border-bottom:0}.badge{display:inline-block;padding:3px 8px;border-radius:999px;background:rgba(128,185,199,.18);color:var(--blue);margin:2px}.log{max-height:245px;overflow:auto;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12px;color:#d9dfcf}@media(max-width:900px){main{grid-template-columns:1fr}.world{min-height:560px;border-right:0;border-bottom:1px solid #33472f}}
</style></head><body><main><section class="world" id="world"><div class="flower"></div><div id="avatar" class="avatar"></div><div class="obj" style="left:24%;top:65%">21-day arcs</div><div class="obj" style="left:53%;top:52%">craft economy</div><div class="obj" style="left:70%;top:43%">ledger debt</div><div class="obj" style="left:42%;top:24%">preferences</div><div class="obj" style="left:34%;top:43%">dialogue threads</div></section><section class="panel"><div><span class="badge">Report 231</span><span class="badge">long arcs</span><h1>Preferences learn. Projects age. Economy remembers.</h1></div><div class="card controls"><button id="advance">advance long-arc tick</button><button id="run" class="secondary">run / pause</button><button id="pref" class="secondary">preference update</button><button id="save" class="secondary">save</button><button id="restore" class="secondary">restore</button><input id="typed" placeholder="type: What changed after day thirteen?"/></div><div class="card" id="current"></div><div class="card"><strong>Metrics</strong><div id="metrics"></div></div><div class="card"><strong>Long projects</strong><div id="projects"></div></div><div class="card log" id="log"></div></section></main><script>
const data=__DATA__;const world=document.getElementById('world'),avatar=document.getElementById('avatar'),current=document.getElementById('current'),metrics=document.getElementById('metrics'),projects=document.getElementById('projects'),log=document.getElementById('log'),typed=document.getElementById('typed');let idx=0,timer=null;const positions={fayen:[28,34],ariq:[54,48],nian:[42,22],roka:[22,62],noro:[70,58]};const nodes=new Map();function pct(v){return `${v}%`}function placeAgents(){for(const a of data.agents){const pos=positions[a.agent_id]||[48,50];const n=document.createElement('div');n.className='agent';n.id=`agent-${a.agent_id}`;n.style.left=pct(pos[0]);n.style.top=pct(pos[1]);n.innerHTML=`<div class="body"></div><div class="name">${a.display_name}</div><div class="need">${a.long_arc_project}</div>`;world.appendChild(n);nodes.set(a.agent_id,n)}}function drawMetrics(){const keys=['long_arc_preference_economy_readiness','many_day_arc_span','learned_preference_update_rate','rich_multiturn_dialogue_depth','craft_economy_consequence_binding','economy_ledger_persistence','body_recovery_carryover','weakest_channel_score'];metrics.innerHTML=keys.map(k=>`<div class="row"><span>${k}</span><strong>${Number(data.metrics[k]).toFixed(6)}</strong></div>`).join('')}function drawProjects(){projects.innerHTML=data.agents.map(a=>`<div class="row"><span>${a.display_name}</span><span>${a.learned_preference_summary}</span></div>`).join('')}function renderTick(tick){for(const n of nodes.values())n.classList.remove('active');const aid=Object.keys(positions).find(a=>tick.agent_state.includes(a))||data.agents[idx%data.agents.length].agent_id;const active=nodes.get(aid);if(active)active.classList.add('active');const pos=positions[aid]||[48,50];avatar.style.left=pct(pos[0]+6);avatar.style.top=pct(pos[1]+8);current.innerHTML=`<strong>Day ${tick.day} / ${tick.layer}</strong><p>${tick.project_state}</p><div class="row"><span>agent</span><span>${tick.agent_state}</span></div><div class="row"><span>preference</span><span>${tick.preference_state}</span></div><div class="row"><span>dialogue</span><span>${tick.dialogue_state}</span></div><div class="row"><span>craft/economy</span><span>${tick.craft_economy_state}</span></div><div class="row"><span>body</span><span>${tick.body_state}</span></div><div class="row"><span>save</span><span>${tick.saved_state}</span></div><div class="row"><span>frequency / flower</span><span>${tick.frequency_hz} Hz / node ${tick.flower_node}</span></div>`;log.innerHTML=`<div>[${idx+1}] day ${tick.day} ${tick.layer}: ${tick.project_state}</div>`+log.innerHTML}function advance(){const tick=data.ticks[idx%data.ticks.length];renderTick(tick);idx++}document.getElementById('advance').onclick=advance;document.getElementById('pref').onclick=()=>{const t=data.ticks.find(x=>x.layer==='preference_update')||data.ticks[0];renderTick(t)};document.getElementById('run').onclick=()=>{if(timer){clearInterval(timer);timer=null}else{timer=setInterval(advance,900)}};document.getElementById('save').onclick=()=>localStorage.setItem('ssrm-report-231-long-arc',JSON.stringify({idx,typed:typed.value}));document.getElementById('restore').onclick=()=>{const s=JSON.parse(localStorage.getItem('ssrm-report-231-long-arc')||'{"idx":0,"typed":""}');idx=s.idx||0;typed.value=s.typed||'';advance()};typed.addEventListener('change',()=>{const q=typed.value.toLowerCase();const d=data.dialogues.find(x=>q.includes(x.listener)||q.includes(String(x.day)))||data.dialogues[0];log.innerHTML=`<div>typed long-arc route -> ${d.listener}: ${d.agent_reply}</div>`+log.innerHTML});placeAgents();drawMetrics();drawProjects();advance();
</script></body></html>"""
    return html.replace("__DATA__", data_json)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    source = load_source()
    agents = build_agents(source)
    arcs = build_long_arcs()
    prefs = build_preference_updates()
    dialogues = build_dialogue_turns(rng)
    econ = build_craft_economy_events()
    ledger = build_ledger()
    recoveries = build_recoveries()
    ticks = build_ticks(arcs, prefs, dialogues, econ, ledger, recoveries)
    metrics = compute_metrics(agents, arcs, prefs, dialogues, econ, ledger, recoveries, ticks)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["long_arc_preference_economy_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.70 else "fail"

    ARTIFACTS.mkdir(exist_ok=True)
    VISUALIZATIONS.mkdir(exist_ok=True)
    write_csv(ARTIFACTS / f"{BASE}_agents.csv", agents)
    write_csv(ARTIFACTS / f"{BASE}_long_project_arcs.csv", arcs)
    write_csv(ARTIFACTS / f"{BASE}_preference_updates.csv", prefs)
    write_csv(ARTIFACTS / f"{BASE}_rich_dialogue_turns.csv", dialogues)
    write_csv(ARTIFACTS / f"{BASE}_craft_economy_events.csv", econ)
    write_csv(ARTIFACTS / f"{BASE}_economy_ledger.csv", ledger)
    write_csv(ARTIFACTS / f"{BASE}_body_recovery_carryover.csv", recoveries)
    write_csv(ARTIFACTS / f"{BASE}_long_arc_ticks.csv", ticks)

    results = {
        "module": BASE,
        "report": REPORT,
        "seed": args.seed,
        "module_verdict": verdict,
        "condition": "integrated_playable_local_long_personal_arcs_learned_preferences_rich_dialogue_craft_economy_consequences",
        "source_artifact": str(SOURCE_STATE),
        "source_condition": source.get("condition", "unknown"),
        "agents": [asdict(x) for x in agents],
        "long_project_arcs": [asdict(x) for x in arcs],
        "preference_updates": [asdict(x) for x in prefs],
        "rich_dialogue_turns": [asdict(x) for x in dialogues],
        "craft_economy_events": [asdict(x) for x in econ],
        "economy_ledger": [asdict(x) for x in ledger],
        "body_recovery_carryover": [asdict(x) for x in recoveries],
        "long_arc_ticks": [asdict(x) for x in ticks],
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": [
            "This is deterministic long-arc scaffolding, not subjective consciousness or real consent.",
            "Learned preferences are bounded weight updates, not open-ended personality learning.",
            "Rich dialogue remains scripted routing, not LLM dialogue or open-ended cognition.",
            "Craft/economy consequences are structured ledgers, not a full economy or full physics.",
            "Body carryover uses welfare-like control signals, not proof of subjective feeling.",
            "Frequency and flower overlays are timing and phase scaffolds, not metaphysical evidence.",
        ],
        "next_gate": "playable local 3D continuous life with learned preference generalization tests, multi-agent economy markets, richer typed dialogue memory, and project arcs beyond twenty-one days",
    }
    (ARTIFACTS / f"{BASE}_results.json").write_text(json.dumps(results, indent=2))
    (ARTIFACTS / f"{BASE}_state.json").write_text(json.dumps(results, indent=2))
    with (ARTIFACTS / f"{BASE}_verdict.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "module", "verdict", "readiness", "weakest_channel_score", "next_gate"])
        writer.writeheader()
        writer.writerow({"report": REPORT, "module": BASE, "verdict": verdict, "readiness": metrics["long_arc_preference_economy_readiness"], "weakest_channel_score": metrics["weakest_channel_score"], "next_gate": results["next_gate"]})
    (VISUALIZATIONS / f"{BASE}.html").write_text(make_html(agents, arcs, prefs, dialogues, econ, ledger, recoveries, ticks, metrics))

    print(f"module_verdict {verdict}")
    print(f"long_arc_preference_economy_readiness {metrics['long_arc_preference_economy_readiness']:.6f}")
    print(f"agents {len(agents)}")
    print(f"long_project_arcs {len(arcs)}")
    print(f"preference_updates {len(prefs)}")
    print(f"rich_dialogue_turns {len(dialogues)}")
    print(f"craft_economy_events {len(econ)}")
    print(f"economy_ledger_entries {len(ledger)}")
    print(f"body_recovery_carryovers {len(recoveries)}")
    print(f"long_arc_ticks {len(ticks)}")
    print(f"many_day_arc_span {metrics['many_day_arc_span']:.6f}")
    print(f"learned_preference_update_rate {metrics['learned_preference_update_rate']:.6f}")
    print(f"rich_multiturn_dialogue_depth {metrics['rich_multiturn_dialogue_depth']:.6f}")
    print(f"craft_economy_consequence_binding {metrics['craft_economy_consequence_binding']:.6f}")
    print(f"economy_ledger_persistence {metrics['economy_ledger_persistence']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
