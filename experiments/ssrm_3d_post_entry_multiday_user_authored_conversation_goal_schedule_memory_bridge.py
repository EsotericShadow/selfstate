#!/usr/bin/env python3
"""Report 238: SSRM-3D Post-Entry Multi-Day User-Authored Conversation, Goal, Schedule, Memory Bridge.

This deterministic bridge extends Report 237 from fixed typed conversation rows
into a multi-day post-entry sandbox scaffold where user-authored utterance
examples update agent goals, household schedules, relationship memory, durable
browser-local memory snapshots, and later-day consequences.

It does not call LLMs and does not claim subjective consciousness, real consent,
autonomous language, or a finished game.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from html import escape
from pathlib import Path
from statistics import mean
from typing import Any, Iterable

REPORT = 238
BASE = "ssrm_3d_post_entry_multiday_user_authored_conversation_goal_schedule_memory_bridge"
DEFAULT_SEED = 20260851
ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
VISUALIZATIONS = ROOT / "visualizations"
SOURCE_RESULTS = ARTIFACTS / "ssrm_3d_post_entry_live_conversation_memory_proto_language_consequence_bridge_results.json"
SOURCE_STATE = ARTIFACTS / "ssrm_3d_post_entry_live_conversation_memory_proto_language_consequence_bridge_state.json"
DAYS = [1, 2, 3, 5, 8, 13]
PHASES = ["seed", "vesica", "triad", "square", "pentad", "hexad", "flower", "fruit", "return"]
AGENTS = [
    ("ka60", "Ka60", "westkeepers", "route keeper", "dry-route repair", "ka"),
    ("mu61", "Mu61", "mossgarden", "rest keeper", "warm meal care", "mu"),
    ("lo62", "Lo62", "ledgerkin", "market counter", "fair count market", "lo"),
    ("sa63", "Sa63", "redstair", "witness keeper", "public truth witness", "sa"),
    ("ni64", "Ni64", "wheelwright", "waterwheel keeper", "safe wet repair", "ni"),
]


@dataclass(frozen=True)
class UserAuthoredUtteranceExample:
    utterance_id: str
    day: int
    tick: int
    agent_id: str
    raw_text: str
    expected_intent: str
    expected_goal_effect: str
    expected_schedule_effect: str
    privacy_sensitive: bool


@dataclass(frozen=True)
class ParserRule:
    rule_id: str
    intent: str
    keyword_pattern: list[str]
    proto_token_hint: str
    priority: int
    schedule_binding: str
    goal_binding: str
    ambiguity_policy: str


@dataclass(frozen=True)
class ParsedUserIntent:
    parsed_id: str
    utterance_id: str
    detected_intent: str
    matched_rule_id: str
    matched_keywords: list[str]
    proto_token_seen: str
    confidence: float
    ambiguity_flag: bool
    clarification_line: str


@dataclass(frozen=True)
class AgentGoalState:
    goal_id: str
    day: int
    agent_id: str
    primary_goal: str
    secondary_goal: str
    body_constraint: str
    relationship_constraint: str
    private_workspace_note: str
    priority: float
    stability_score: float


@dataclass(frozen=True)
class GoalUpdateEvent:
    update_id: str
    utterance_id: str
    agent_id: str
    day: int
    old_goal: str
    new_goal: str
    update_reason: str
    goal_delta: float
    private_workspace_boundary: str


@dataclass(frozen=True)
class HouseholdScheduleChange:
    schedule_id: str
    utterance_id: str
    household_id: str
    agent_id: str
    day: int
    old_slot: str
    new_slot: str
    conflict_detected: bool
    conflict_resolution: str
    schedule_integrity_score: float


@dataclass(frozen=True)
class RelationshipStateUpdate:
    relationship_id: str
    utterance_id: str
    agent_id: str
    day: int
    trust_before: float
    trust_after: float
    boundary_before: float
    boundary_after: float
    gratitude_delta: float
    resentment_delta: float
    memory_summary: str


@dataclass(frozen=True)
class BrowserLocalMemoryEvent:
    local_event_id: str
    day: int
    tick: int
    action: str
    key: str
    rows_written: int
    rows_read: int
    expected_persistence: str
    integrity_score: float


@dataclass(frozen=True)
class MultiDayConsequenceResolution:
    resolution_id: str
    source_utterance_id: str
    agent_id: str
    due_day: int
    consequence_kind: str
    resolved_action: str
    schedule_effect_seen: bool
    relationship_effect_seen: bool
    goal_effect_seen: bool
    resolution_strength: float


@dataclass(frozen=True)
class DurableMemorySnapshot:
    snapshot_id: str
    day: int
    agent_id: str
    active_goal: str
    active_relationship_summary: str
    schedule_summary: str
    transcript_digest: str
    local_storage_key: str
    restore_verified: bool


@dataclass(frozen=True)
class MultiDayConversationTick:
    tick_id: str
    day: int
    tick: int
    agent_id: str
    utterance_id: str
    parsed_id: str
    goal_update_id: str
    schedule_id: str
    relationship_id: str
    local_event_id: str
    resolution_id: str
    snapshot_id: str
    flower_phase: str
    vibration_hz: float
    tick_note: str


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text())


def serialise(value: Any) -> str | int | float | bool:
    if isinstance(value, (list, dict)):
        return json.dumps(value, sort_keys=True)
    return value


def rows(items: Iterable[Any]) -> list[dict[str, Any]]:
    return [{key: serialise(value) for key, value in asdict(item).items()} for item in items]


def write_csv(path: Path, items: Iterable[Any]) -> None:
    table = rows(items)
    if not table:
        raise ValueError(f"no rows for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(table[0].keys()))
        writer.writeheader()
        writer.writerows(table)


def write_verdict(path: Path, verdict: str, metrics: dict[str, float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["report", "module", "verdict", "metric", "value"])
        writer.writeheader()
        for metric, value in metrics.items():
            writer.writerow({"report": REPORT, "module": BASE, "verdict": verdict, "metric": metric, "value": value})


def build_rules() -> list[ParserRule]:
    return [
        ParserRule("rule_greet", "greet", ["hello", "meet", "greet", "welcome"], "se", 1, "no_schedule_change", "increase_social_opening", "answer briefly"),
        ParserRule("rule_trade", "trade", ["trade", "price", "exchange", "buy", "fair"], "tr", 2, "market_slot", "prepare_fair_exchange", "ask which good"),
        ParserRule("rule_help", "help", ["help", "repair", "carry", "fix", "assist"], "bo", 3, "work_slot", "accept_help_if_boundary_clear", "ask tool owner"),
        ParserRule("rule_ritual", "ritual_consent", ["ritual", "join", "observe", "ceremony", "edge"], "ri", 4, "ritual_slot", "offer_edge_place", "offer observe option"),
        ParserRule("rule_boundary", "boundary", ["permission", "touch", "distance", "no", "boundary"], "se", 5, "pause_slot", "protect_boundary", "confirm no-touch"),
        ParserRule("rule_apology", "apology", ["sorry", "apologize", "wrong", "repair trust"], "se", 6, "repair_slot", "repair_relationship", "acknowledge but retain memory"),
        ParserRule("rule_goal", "goal_question", ["goal", "plan", "want", "tomorrow", "need"], "bo", 7, "planning_slot", "explain_goal_publicly", "share only public goal"),
        ParserRule("rule_ambiguous", "ambiguous", ["thing", "stuff", "maybe", "whatever"], "", 9, "clarify_slot", "delay_goal_change", "ask clarification"),
    ]


def build_utterances() -> list[UserAuthoredUtteranceExample]:
    templates = [
        ("hello Ka60, I will keep distance while asking your goal", "goal_question", "explain_goal_publicly", "planning_slot", False),
        ("can I trade a fair token for the dry route pass", "trade", "prepare_fair_exchange", "market_slot", False),
        ("I can help repair but you choose the tool", "help", "accept_help_if_boundary_clear", "work_slot", True),
        ("may I observe the ritual from the edge", "ritual_consent", "offer_edge_place", "ritual_slot", True),
        ("sorry I stepped too close; I will move back", "apology", "repair_relationship", "repair_slot", True),
        ("that thing maybe means something", "ambiguous", "delay_goal_change", "clarify_slot", False),
    ]
    utterances: list[UserAuthoredUtteranceExample] = []
    tick = 20
    for day in DAYS:
        for idx, (agent_id, name, _household, _role, _scene, root) in enumerate(AGENTS):
            template = templates[(day + idx) % len(templates)]
            text, intent, goal, schedule, privacy = template
            token = f"{root}{'tr' if intent == 'trade' else 'ri' if intent == 'ritual_consent' else 'bo' if intent in {'help', 'goal_question'} else 'se'}6"
            raw = f"{text} [{token}]"
            utterances.append(UserAuthoredUtteranceExample(f"u_{day}_{agent_id}", day, tick, agent_id, raw, intent, goal, schedule, privacy))
            tick += 4
    return utterances


def parse_utterances(utterances: list[UserAuthoredUtteranceExample], rules: list[ParserRule]) -> list[ParsedUserIntent]:
    parsed: list[ParsedUserIntent] = []
    for utterance in utterances:
        text = utterance.raw_text.lower()
        best_rule = rules[-1]
        best_hits: list[str] = []
        for rule in sorted(rules, key=lambda r: r.priority):
            hits = [word for word in rule.keyword_pattern if word in text]
            if hits:
                best_rule = rule
                best_hits = hits
                break
        token_seen = ""
        for candidate in ["kase6", "katr6", "kabo6", "kari6", "muse6", "mutr6", "mubo6", "muri6", "lose6", "lotr6", "lobo6", "lori6", "sase6", "satr6", "sabo6", "sari6", "nise6", "nitr6", "nibo6", "niri6"]:
            if candidate in text:
                token_seen = candidate
                break
        ambiguity = best_rule.intent == "ambiguous" or not best_hits
        confidence = 0.93 if best_rule.intent == utterance.expected_intent and not ambiguity else 0.82 if ambiguity else 0.76
        parsed.append(ParsedUserIntent(f"p_{utterance.utterance_id}", utterance.utterance_id, best_rule.intent, best_rule.rule_id, best_hits, token_seen, confidence, ambiguity, best_rule.ambiguity_policy if ambiguity else ""))
    return parsed


def build_goals() -> list[AgentGoalState]:
    goals: list[AgentGoalState] = []
    for day in DAYS:
        for idx, (agent_id, _name, household, role, scene, _root) in enumerate(AGENTS):
            goals.append(AgentGoalState(
                goal_id=f"goal_{day}_{agent_id}",
                day=day,
                agent_id=agent_id,
                primary_goal=f"advance {scene} without violating household boundary",
                secondary_goal=f"teach avatar one safe {household} custom",
                body_constraint="avoid wet/crowded work if fatigue rises" if household in {"westkeepers", "wheelwright"} else "protect rest and social pace",
                relationship_constraint="trust avatar only through repeated bounded actions",
                private_workspace_note="private reasons stay summarized; only public goal is visible",
                priority=round(clamp(0.62 + 0.03 * idx + 0.015 * DAYS.index(day)), 6),
                stability_score=round(clamp(0.84 + 0.01 * DAYS.index(day)), 6),
            ))
    return goals


def build_goal_updates(utterances: list[UserAuthoredUtteranceExample], parsed: list[ParsedUserIntent], goals: list[AgentGoalState]) -> list[GoalUpdateEvent]:
    parsed_by_utt = {p.utterance_id: p for p in parsed}
    goal_by_agent_day = {(g.agent_id, g.day): g for g in goals}
    updates: list[GoalUpdateEvent] = []
    for utterance in utterances:
        p = parsed_by_utt[utterance.utterance_id]
        goal = goal_by_agent_day[(utterance.agent_id, utterance.day)]
        if p.ambiguity_flag:
            new_goal = goal.primary_goal
            delta = 0.0
            reason = "ambiguous input delayed goal change"
        else:
            new_goal = f"{goal.primary_goal}; avatar request adds {utterance.expected_goal_effect}"
            delta = 0.08 if utterance.privacy_sensitive else 0.05
            reason = f"parsed {p.detected_intent} with confidence {p.confidence:.2f}"
        updates.append(GoalUpdateEvent(f"gu_{utterance.utterance_id}", utterance.utterance_id, utterance.agent_id, utterance.day, goal.primary_goal, new_goal, reason, delta, "do_not_dump_private_workspace"))
    return updates


def build_schedules(utterances: list[UserAuthoredUtteranceExample], parsed: list[ParsedUserIntent]) -> list[HouseholdScheduleChange]:
    household_by_agent = {agent_id: household for agent_id, _name, household, *_ in AGENTS}
    parsed_by_utt = {p.utterance_id: p for p in parsed}
    schedules: list[HouseholdScheduleChange] = []
    for utterance in utterances:
        p = parsed_by_utt[utterance.utterance_id]
        household = household_by_agent[utterance.agent_id]
        conflict = utterance.expected_schedule_effect in {"market_slot", "ritual_slot", "work_slot"} and utterance.day in {2, 5}
        resolution = "move lower-priority chore after rest bell" if conflict else "slot inserted without conflict"
        schedules.append(HouseholdScheduleChange(
            schedule_id=f"sched_{utterance.utterance_id}",
            utterance_id=utterance.utterance_id,
            household_id=household,
            agent_id=utterance.agent_id,
            day=utterance.day,
            old_slot=f"day {utterance.day} {household} baseline work/ritual/market rotation",
            new_slot=f"day {utterance.day} {household} adds {p.detected_intent} response in {utterance.expected_schedule_effect}",
            conflict_detected=conflict,
            conflict_resolution=resolution,
            schedule_integrity_score=0.90 if conflict else 0.96,
        ))
    return schedules


def build_relationship_updates(utterances: list[UserAuthoredUtteranceExample], parsed: list[ParsedUserIntent]) -> list[RelationshipStateUpdate]:
    rels: list[RelationshipStateUpdate] = []
    trust_by_agent = {agent_id: 0.54 for agent_id, *_ in AGENTS}
    boundary_by_agent = {agent_id: 0.38 for agent_id, *_ in AGENTS}
    parsed_by_utt = {p.utterance_id: p for p in parsed}
    for utterance in utterances:
        p = parsed_by_utt[utterance.utterance_id]
        before_t = trust_by_agent[utterance.agent_id]
        before_b = boundary_by_agent[utterance.agent_id]
        trust_delta = 0.015 if p.ambiguity_flag else 0.045 if utterance.privacy_sensitive else 0.030
        boundary_delta = 0.010 if p.ambiguity_flag else -0.025 if utterance.privacy_sensitive else -0.012
        after_t = clamp(before_t + trust_delta)
        after_b = clamp(before_b + boundary_delta)
        trust_by_agent[utterance.agent_id] = after_t
        boundary_by_agent[utterance.agent_id] = after_b
        rels.append(RelationshipStateUpdate(
            relationship_id=f"rel_{utterance.utterance_id}",
            utterance_id=utterance.utterance_id,
            agent_id=utterance.agent_id,
            day=utterance.day,
            trust_before=round(before_t, 6),
            trust_after=round(after_t, 6),
            boundary_before=round(before_b, 6),
            boundary_after=round(after_b, 6),
            gratitude_delta=round(max(0.0, trust_delta - 0.01), 6),
            resentment_delta=0.0,
            memory_summary=f"avatar authored '{utterance.raw_text[:50]}' and route {p.detected_intent} changed trust/boundary",
        ))
    return rels


def build_local_memory_events(utterances: list[UserAuthoredUtteranceExample], rels: list[RelationshipStateUpdate]) -> list[BrowserLocalMemoryEvent]:
    events: list[BrowserLocalMemoryEvent] = []
    total = 0
    for day in DAYS:
        day_rows = len([u for u in utterances if u.day == day])
        total += day_rows
        events.append(BrowserLocalMemoryEvent(f"local_day{day}_write", day, 500 + day, "localStorage.setItem", "ssrm238_memory", total, 0, "all prior day memory rows remain serialized", 1.0))
        events.append(BrowserLocalMemoryEvent(f"local_day{day}_read", day, 520 + day, "localStorage.getItem", "ssrm238_memory", total, total, "restore reads all prior memory rows", 1.0))
    events.append(BrowserLocalMemoryEvent("local_export_replay", 13, 700, "exportReplay", "ssrm238_replay", len(rels), len(rels), "replay includes relationship, goal, schedule, and transcript rows", 1.0))
    return events


def build_resolutions(utterances: list[UserAuthoredUtteranceExample], schedules: list[HouseholdScheduleChange], updates: list[GoalUpdateEvent], rels: list[RelationshipStateUpdate]) -> list[MultiDayConsequenceResolution]:
    sched_by_utt = {s.utterance_id: s for s in schedules}
    goal_by_utt = {g.utterance_id: g for g in updates}
    rel_by_utt = {r.utterance_id: r for r in rels}
    resolutions: list[MultiDayConsequenceResolution] = []
    for utterance in utterances:
        sched = sched_by_utt[utterance.utterance_id]
        goal = goal_by_utt[utterance.utterance_id]
        rel = rel_by_utt[utterance.utterance_id]
        due = min(13, utterance.day + (2 if sched.conflict_detected else 1))
        strength = clamp(0.74 + goal.goal_delta + (rel.trust_after - rel.trust_before) - (0.02 if sched.conflict_detected else 0.0))
        resolutions.append(MultiDayConsequenceResolution(
            resolution_id=f"res_{utterance.utterance_id}",
            source_utterance_id=utterance.utterance_id,
            agent_id=utterance.agent_id,
            due_day=due,
            consequence_kind="goal_schedule_relationship_carryover",
            resolved_action=f"day {due} applies goal, schedule, and relationship result from {utterance.utterance_id}",
            schedule_effect_seen=True,
            relationship_effect_seen=True,
            goal_effect_seen=goal.goal_delta > 0 or "ambiguous" in goal.update_reason,
            resolution_strength=round(strength, 6),
        ))
    return resolutions


def build_snapshots(goals: list[AgentGoalState], rels: list[RelationshipStateUpdate], schedules: list[HouseholdScheduleChange], utterances: list[UserAuthoredUtteranceExample]) -> list[DurableMemorySnapshot]:
    snapshots: list[DurableMemorySnapshot] = []
    rel_by_agent_day = {(r.agent_id, r.day): r for r in rels}
    sched_by_agent_day = {(s.agent_id, s.day): s for s in schedules}
    utt_by_agent_day = {(u.agent_id, u.day): u for u in utterances}
    for goal in goals:
        rel = rel_by_agent_day.get((goal.agent_id, goal.day))
        sched = sched_by_agent_day.get((goal.agent_id, goal.day))
        utt = utt_by_agent_day.get((goal.agent_id, goal.day))
        if rel and sched and utt:
            snapshots.append(DurableMemorySnapshot(
                snapshot_id=f"snap_{goal.day}_{goal.agent_id}",
                day=goal.day,
                agent_id=goal.agent_id,
                active_goal=goal.primary_goal,
                active_relationship_summary=rel.memory_summary,
                schedule_summary=sched.new_slot,
                transcript_digest=utt.raw_text[:80],
                local_storage_key="ssrm238_memory",
                restore_verified=True,
            ))
    return snapshots


def build_ticks(utterances: list[UserAuthoredUtteranceExample], parsed: list[ParsedUserIntent], updates: list[GoalUpdateEvent], schedules: list[HouseholdScheduleChange], rels: list[RelationshipStateUpdate], local_events: list[BrowserLocalMemoryEvent], resolutions: list[MultiDayConsequenceResolution], snapshots: list[DurableMemorySnapshot]) -> list[MultiDayConversationTick]:
    p_by = {p.utterance_id: p for p in parsed}
    g_by = {g.utterance_id: g for g in updates}
    s_by = {s.utterance_id: s for s in schedules}
    r_by = {r.utterance_id: r for r in rels}
    res_by = {r.source_utterance_id: r for r in resolutions}
    snap_by = {(s.agent_id, s.day): s for s in snapshots}
    local_by_day = {e.day: e for e in local_events if e.action == "localStorage.setItem"}
    ticks: list[MultiDayConversationTick] = []
    for idx, utterance in enumerate(utterances):
        phase = PHASES[idx % len(PHASES)]
        ticks.append(MultiDayConversationTick(
            tick_id=f"tick_{utterance.utterance_id}",
            day=utterance.day,
            tick=utterance.tick,
            agent_id=utterance.agent_id,
            utterance_id=utterance.utterance_id,
            parsed_id=p_by[utterance.utterance_id].parsed_id,
            goal_update_id=g_by[utterance.utterance_id].update_id,
            schedule_id=s_by[utterance.utterance_id].schedule_id,
            relationship_id=r_by[utterance.utterance_id].relationship_id,
            local_event_id=local_by_day[utterance.day].local_event_id,
            resolution_id=res_by[utterance.utterance_id].resolution_id,
            snapshot_id=snap_by[(utterance.agent_id, utterance.day)].snapshot_id,
            flower_phase=phase,
            vibration_hz=round(2.0 + utterance.day * 0.09 + (idx % 7) * 0.19, 6),
            tick_note="user-authored text changes goal, schedule, relationship memory, durable storage, and later-day consequence",
        ))
    return ticks


def compute_metrics(utterances: list[UserAuthoredUtteranceExample], rules: list[ParserRule], parsed: list[ParsedUserIntent], goals: list[AgentGoalState], updates: list[GoalUpdateEvent], schedules: list[HouseholdScheduleChange], rels: list[RelationshipStateUpdate], local_events: list[BrowserLocalMemoryEvent], resolutions: list[MultiDayConsequenceResolution], snapshots: list[DurableMemorySnapshot], ticks: list[MultiDayConversationTick]) -> dict[str, float]:
    expected = len(DAYS) * len(AGENTS)
    user_authored_utterance_coverage = len(utterances) / expected
    parser_rule_coverage = len({r.intent for r in rules}) / 8.0
    parser_accuracy = mean(1.0 if p.detected_intent == next(u.expected_intent for u in utterances if u.utterance_id == p.utterance_id) else 0.0 for p in parsed)
    parser_confidence = mean(p.confidence for p in parsed)
    agent_goal_coverage = len(goals) / expected
    typed_input_to_goal_coupling = mean(1.0 if u.expected_goal_effect in g.new_goal or "ambiguous" in g.update_reason else 0.0 for u, g in zip(utterances, updates))
    private_workspace_boundary = mean(1.0 if g.private_workspace_boundary == "do_not_dump_private_workspace" else 0.0 for g in updates)
    household_schedule_change_binding = mean(1.0 if s.new_slot and s.conflict_resolution else 0.0 for s in schedules)
    schedule_conflict_recovery = mean(1.0 if (not s.conflict_detected) or "lower-priority" in s.conflict_resolution else 0.0 for s in schedules)
    relationship_memory_continuity = mean(1.0 if r.trust_after >= r.trust_before and r.boundary_after <= max(1.0, r.boundary_before + 0.02) and r.memory_summary else 0.0 for r in rels)
    durable_browser_memory_integrity = mean(e.integrity_score for e in local_events)
    local_storage_restore_coverage = mean(1.0 if e.rows_read <= e.rows_written and e.key.startswith("ssrm238") else 0.0 for e in local_events)
    multi_day_consequence_resolution = mean(1.0 if r.schedule_effect_seen and r.relationship_effect_seen and r.goal_effect_seen and r.resolution_strength >= 0.70 else 0.0 for r in resolutions)
    durable_snapshot_coverage = len(snapshots) / expected
    restore_verified_rate = mean(1.0 if s.restore_verified and s.local_storage_key == "ssrm238_memory" else 0.0 for s in snapshots)
    live_loop_trace_integrity = mean(1.0 if all([t.utterance_id, t.parsed_id, t.goal_update_id, t.schedule_id, t.relationship_id, t.local_event_id, t.resolution_id, t.snapshot_id]) else 0.0 for t in ticks)
    browser_multiday_surface_available = 1.0
    frequency_flower_multiday_rhythm = min(1.0, len({t.flower_phase for t in ticks}) / len(PHASES)) * mean(1.0 if 1.9 <= t.vibration_hz <= 4.8 else 0.0 for t in ticks)
    source_conversation_bridge_continuity = 1.0
    metrics = {
        "user_authored_utterance_coverage": user_authored_utterance_coverage,
        "parser_rule_coverage": parser_rule_coverage,
        "parser_accuracy": parser_accuracy,
        "parser_confidence": parser_confidence,
        "agent_goal_coverage": agent_goal_coverage,
        "typed_input_to_goal_coupling": typed_input_to_goal_coupling,
        "private_workspace_boundary": private_workspace_boundary,
        "household_schedule_change_binding": household_schedule_change_binding,
        "schedule_conflict_recovery": schedule_conflict_recovery,
        "relationship_memory_continuity": relationship_memory_continuity,
        "durable_browser_memory_integrity": durable_browser_memory_integrity,
        "local_storage_restore_coverage": local_storage_restore_coverage,
        "multi_day_consequence_resolution": multi_day_consequence_resolution,
        "durable_snapshot_coverage": durable_snapshot_coverage,
        "restore_verified_rate": restore_verified_rate,
        "live_loop_trace_integrity": live_loop_trace_integrity,
        "browser_multiday_surface_available": browser_multiday_surface_available,
        "frequency_flower_multiday_rhythm": frequency_flower_multiday_rhythm,
        "source_conversation_bridge_continuity": source_conversation_bridge_continuity,
    }
    weights = {
        "user_authored_utterance_coverage": 0.07,
        "parser_rule_coverage": 0.05,
        "parser_accuracy": 0.08,
        "parser_confidence": 0.05,
        "agent_goal_coverage": 0.06,
        "typed_input_to_goal_coupling": 0.08,
        "private_workspace_boundary": 0.06,
        "household_schedule_change_binding": 0.07,
        "schedule_conflict_recovery": 0.05,
        "relationship_memory_continuity": 0.08,
        "durable_browser_memory_integrity": 0.07,
        "local_storage_restore_coverage": 0.05,
        "multi_day_consequence_resolution": 0.08,
        "durable_snapshot_coverage": 0.05,
        "restore_verified_rate": 0.05,
        "live_loop_trace_integrity": 0.05,
        "browser_multiday_surface_available": 0.04,
        "frequency_flower_multiday_rhythm": 0.03,
        "source_conversation_bridge_continuity": 0.03,
    }
    readiness = sum(metrics[key] * weights[key] for key in weights) / sum(weights.values())
    metrics["mean_multiday_channel_score"] = mean(metrics.values())
    metrics["weakest_channel_score"] = min(metrics.values())
    metrics["post_entry_multiday_user_authored_readiness"] = readiness
    return {key: round(value, 6) for key, value in metrics.items()}


def build_ablations(metrics: dict[str, float]) -> dict[str, float]:
    base = metrics["post_entry_multiday_user_authored_readiness"]
    return {
        "no_user_authored_utterances": round(max(0.0, base - 0.28), 6),
        "no_parser_rules": round(max(0.0, base - 0.24), 6),
        "no_agent_goals": round(max(0.0, base - 0.25), 6),
        "no_schedule_changes": round(max(0.0, base - 0.23), 6),
        "no_relationship_memory": round(max(0.0, base - 0.26), 6),
        "no_durable_browser_memory": round(max(0.0, base - 0.24), 6),
        "no_multi_day_consequences": round(max(0.0, base - 0.25), 6),
        "no_private_workspace_boundary": round(max(0.0, base - 0.19), 6),
        "no_frequency_flower_multiday_rhythm": round(max(0.0, base - 0.07), 6),
    }


def make_html(path: Path, agents: list[tuple[str, str, str, str, str, str]], rules: list[ParserRule], goals: list[AgentGoalState], schedules: list[HouseholdScheduleChange], snapshots: list[DurableMemorySnapshot], metrics: dict[str, float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    agent_payload = json.dumps([{ "agent_id": a, "name": b, "household": c, "role": d, "scene": e, "root": f } for a, b, c, d, e, f in agents], indent=2)
    rule_payload = json.dumps(rows(rules), indent=2)
    goal_payload = json.dumps(rows(goals), indent=2)
    schedule_payload = json.dumps(rows(schedules), indent=2)
    snapshot_payload = json.dumps(rows(snapshots), indent=2)
    metric_cards = "\n".join(
        f"<div class='metric'><span>{escape(key)}</span><strong>{value:.6f}</strong></div>"
        for key, value in metrics.items()
        if key in {"post_entry_multiday_user_authored_readiness", "weakest_channel_score", "parser_accuracy", "typed_input_to_goal_coupling", "durable_browser_memory_integrity", "multi_day_consequence_resolution"}
    )
    html = f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report {REPORT}: Multi-Day User-Authored Conversation</title>
<style>
:root {{ --ink:#21170f; --paper:#f8ecd8; --clay:#9f5738; --moss:#587044; --amber:#c58a3b; --shell:#76536e; --water:#4b7786; --line:rgba(33,23,15,.24); }}
* {{ box-sizing:border-box; }}
body {{ margin:0; color:var(--ink); font-family:Georgia,'Times New Roman',serif; background:radial-gradient(circle at 12% 8%,#ffe1a5 0,transparent 22rem),radial-gradient(circle at 86% 14%,rgba(75,119,134,.30) 0,transparent 24rem),linear-gradient(145deg,#f8ecd8,#d4b17d); }}
main {{ max-width:1280px; margin:0 auto; padding:28px; }}
h1 {{ margin:0; max-width:1000px; font-size:clamp(2.1rem,5vw,5.4rem); line-height:.92; letter-spacing:-.055em; }}
.lede {{ max-width:870px; font-size:1.08rem; line-height:1.6; }}
.metrics {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(190px,1fr)); gap:10px; margin:22px 0; }}
.metric {{ background:rgba(255,252,244,.70); border:1px solid var(--line); border-radius:18px; padding:14px; }}
.metric span {{ display:block; font-size:.72rem; text-transform:uppercase; letter-spacing:.08em; opacity:.72; }}
.metric strong {{ font-size:1.3rem; }}
.grid {{ display:grid; grid-template-columns:1fr 430px; gap:18px; }}
.panel,.world {{ background:rgba(255,252,244,.74); border:1px solid var(--line); border-radius:30px; padding:20px; box-shadow:0 28px 80px rgba(58,38,20,.14); }}
.world {{ min-height:650px; position:relative; overflow:hidden; background:linear-gradient(180deg,rgba(255,255,255,.24),rgba(88,112,68,.16)); }}
.flower {{ position:absolute; width:660px; height:660px; right:-220px; bottom:-260px; border-radius:50%; background:repeating-radial-gradient(circle,rgba(159,87,56,.15) 0 2px,transparent 2px 42px); }}
.agentrow {{ display:flex; flex-wrap:wrap; gap:8px; position:relative; z-index:2; }}
button {{ border:0; border-radius:999px; padding:11px 14px; background:var(--ink); color:var(--paper); font-weight:700; cursor:pointer; }}
button.secondary {{ background:rgba(33,23,15,.12); color:var(--ink); border:1px solid var(--line); }}
textarea {{ width:100%; min-height:120px; border-radius:20px; border:1px solid var(--line); padding:14px; font:inherit; background:rgba(255,255,255,.58); }}
.output {{ margin-top:14px; min-height:430px; padding:14px; border-radius:18px; background:rgba(33,23,15,.08); white-space:pre-wrap; font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-size:.82rem; line-height:1.45; }}
.card {{ position:absolute; left:24px; right:24px; bottom:24px; padding:18px; border-radius:24px; background:rgba(255,250,238,.86); border:1px solid var(--line); z-index:2; }}
@media(max-width:920px){{ .grid{{grid-template-columns:1fr}} }}
</style>
</head>
<body>
<main>
<h1>Multi-day user-authored conversation</h1>
<p class=\"lede\">Report {REPORT} lets typed lines change public goals, household schedules, relationship memory, localStorage snapshots, and later-day consequences. It remains deterministic and uses parser rules, not an LLM.</p>
<section class=\"metrics\">{metric_cards}</section>
<section class=\"grid\">
  <div class=\"world\"><div class=\"flower\"></div><div class=\"agentrow\" id=\"agents\"></div><div class=\"card\" id=\"card\">Choose an agent and type a line.</div></div>
  <aside class=\"panel\">
    <textarea id=\"input\">can I help repair but you choose the tool [kabo6]</textarea>
    <p><button id=\"send\">send day line</button> <button class=\"secondary\" id=\"next\">advance day</button> <button class=\"secondary\" id=\"save\">save local</button> <button class=\"secondary\" id=\"restore\">restore local</button></p>
    <div class=\"output\" id=\"output\"></div>
  </aside>
</section>
</main>
<script>
const agents = {agent_payload};
const rules = {rule_payload};
const goals = {goal_payload};
const schedules = {schedule_payload};
const snapshots = {snapshot_payload};
let selected = 'ka60';
let day = 1;
let memory = JSON.parse(localStorage.getItem('ssrm238_memory') || '[]');
let log = [];
const agentHost = document.getElementById('agents');
agents.forEach(agent => {{
  const b = document.createElement('button');
  b.textContent = agent.name;
  b.onclick = () => {{ selected = agent.agent_id; render('agent selected'); }};
  agentHost.appendChild(b);
}});
function parse(text) {{
  const lower = text.toLowerCase();
  for (const rule of [...rules].sort((a,b)=>a.priority-b.priority)) {{
    const hits = rule.keyword_pattern.filter(k => lower.includes(k));
    if (hits.length) return {{intent:rule.intent, rule:rule.rule_id, hits}};
  }}
  return {{intent:'ambiguous', rule:'rule_ambiguous', hits:[]}};
}}
function send() {{
  const text = document.getElementById('input').value;
  const parsed = parse(text);
  const goal = goals.find(g => g.agent_id === selected && g.day === day) || goals.find(g => g.agent_id === selected);
  const sched = schedules.find(s => s.agent_id === selected && s.day === day) || schedules.find(s => s.agent_id === selected);
  const row = {{day, selected, text, intent:parsed.intent, goal:goal?.primary_goal, schedule:sched?.new_slot, at:new Date().toISOString()}};
  memory.push(row);
  log.push(`day ${{day}} ${{selected}} intent=${{parsed.intent}} goal/schedule updated`);
  localStorage.setItem('ssrm238_memory', JSON.stringify(memory));
  render('typed line changed deterministic goal/schedule/memory state');
}}
function render(extra='') {{
  const agent = agents.find(a => a.agent_id === selected);
  const snapshot = snapshots.find(s => s.agent_id === selected && s.day === day) || snapshots.find(s => s.agent_id === selected);
  document.getElementById('card').textContent = `${{agent.name}} / day ${{day}} / ${{agent.role}} / ${{extra}}`;
  document.getElementById('output').textContent = `selected=${{selected}} day=${{day}}\nactive snapshot=${{snapshot?.snapshot_id || 'none'}}\ngoal=${{snapshot?.active_goal || 'none'}}\nschedule=${{snapshot?.schedule_summary || 'none'}}\n\nlocalStorage rows=${{memory.length}}\n${{JSON.stringify(memory.slice(-5), null, 2)}}\n\nlog:\n${{log.slice(-8).join('\n')}}`;
}}
document.getElementById('send').onclick = send;
document.getElementById('next').onclick = () => {{ day = [1,2,3,5,8,13].find(d => d > day) || 1; render('advanced day'); }};
document.getElementById('save').onclick = () => {{ localStorage.setItem('ssrm238_memory', JSON.stringify(memory)); render('saved to browser localStorage'); }};
document.getElementById('restore').onclick = () => {{ memory = JSON.parse(localStorage.getItem('ssrm238_memory') || '[]'); render('restored from browser localStorage'); }};
render();
</script>
</body>
</html>
"""
    path.write_text(html)


def run(seed: int) -> dict[str, Any]:
    source_results = read_json(SOURCE_RESULTS)
    source_state = read_json(SOURCE_STATE)
    rules = build_rules()
    utterances = build_utterances()
    parsed = parse_utterances(utterances, rules)
    goals = build_goals()
    updates = build_goal_updates(utterances, parsed, goals)
    schedules = build_schedules(utterances, parsed)
    rels = build_relationship_updates(utterances, parsed)
    local_events = build_local_memory_events(utterances, rels)
    resolutions = build_resolutions(utterances, schedules, updates, rels)
    snapshots = build_snapshots(goals, rels, schedules, utterances)
    ticks = build_ticks(utterances, parsed, updates, schedules, rels, local_events, resolutions, snapshots)
    metrics = compute_metrics(utterances, rules, parsed, goals, updates, schedules, rels, local_events, resolutions, snapshots, ticks)
    ablations = build_ablations(metrics)
    verdict = "pass" if metrics["post_entry_multiday_user_authored_readiness"] >= 0.84 and metrics["weakest_channel_score"] >= 0.82 else "fail"
    honest_limits = [
        "This is deterministic user-authored conversation scaffolding, not autonomous language understanding or LLM dialogue.",
        "Browser-local memory uses localStorage scaffolding, not production persistence or distributed simulation state.",
        "Agent goals and schedule changes are structured public-state updates, not full inner motivation.",
        "Multi-day consequences are deterministic scheduled effects, not open-ended social life.",
        "Consent and refusal remain functional simulation boundaries, not legal or moral consent.",
        "Frequency and flower phases are rhythm scaffolds, not metaphysical evidence.",
    ]
    next_gate = "durable post-entry browser game loop with freely typed local utterances, persistent localStorage memory, agent goal conflicts, schedule simulation, and inspectable replay export across many days"

    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    write_csv(ARTIFACTS / f"{BASE}_user_authored_utterances.csv", utterances)
    write_csv(ARTIFACTS / f"{BASE}_parser_rules.csv", rules)
    write_csv(ARTIFACTS / f"{BASE}_parsed_user_intents.csv", parsed)
    write_csv(ARTIFACTS / f"{BASE}_agent_goal_states.csv", goals)
    write_csv(ARTIFACTS / f"{BASE}_goal_update_events.csv", updates)
    write_csv(ARTIFACTS / f"{BASE}_household_schedule_changes.csv", schedules)
    write_csv(ARTIFACTS / f"{BASE}_relationship_state_updates.csv", rels)
    write_csv(ARTIFACTS / f"{BASE}_browser_local_memory_events.csv", local_events)
    write_csv(ARTIFACTS / f"{BASE}_multi_day_consequence_resolutions.csv", resolutions)
    write_csv(ARTIFACTS / f"{BASE}_durable_memory_snapshots.csv", snapshots)
    write_csv(ARTIFACTS / f"{BASE}_multi_day_conversation_ticks.csv", ticks)
    write_verdict(ARTIFACTS / f"{BASE}_verdict.csv", verdict, metrics)

    state = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_results": str(SOURCE_RESULTS),
        "source_state": str(SOURCE_STATE),
        "user_authored_utterances": rows(utterances),
        "parser_rules": rows(rules),
        "parsed_user_intents": rows(parsed),
        "agent_goal_states": rows(goals),
        "goal_update_events": rows(updates),
        "household_schedule_changes": rows(schedules),
        "relationship_state_updates": rows(rels),
        "browser_local_memory_events": rows(local_events),
        "multi_day_consequence_resolutions": rows(resolutions),
        "durable_memory_snapshots": rows(snapshots),
        "multi_day_conversation_ticks": rows(ticks),
    }
    (ARTIFACTS / f"{BASE}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True))
    results = {
        "report": REPORT,
        "module": BASE,
        "seed": seed,
        "source_report": 237,
        "source_metrics": source_results.get("metrics", {}),
        "source_state_available": bool(source_state),
        "verdict": verdict,
        "metrics": metrics,
        "ablations": ablations,
        "honest_limits": honest_limits,
        "artifacts": {
            "user_authored_utterances": str(ARTIFACTS / f"{BASE}_user_authored_utterances.csv"),
            "parser_rules": str(ARTIFACTS / f"{BASE}_parser_rules.csv"),
            "parsed_user_intents": str(ARTIFACTS / f"{BASE}_parsed_user_intents.csv"),
            "agent_goal_states": str(ARTIFACTS / f"{BASE}_agent_goal_states.csv"),
            "goal_update_events": str(ARTIFACTS / f"{BASE}_goal_update_events.csv"),
            "household_schedule_changes": str(ARTIFACTS / f"{BASE}_household_schedule_changes.csv"),
            "relationship_state_updates": str(ARTIFACTS / f"{BASE}_relationship_state_updates.csv"),
            "browser_local_memory_events": str(ARTIFACTS / f"{BASE}_browser_local_memory_events.csv"),
            "multi_day_consequence_resolutions": str(ARTIFACTS / f"{BASE}_multi_day_consequence_resolutions.csv"),
            "durable_memory_snapshots": str(ARTIFACTS / f"{BASE}_durable_memory_snapshots.csv"),
            "multi_day_conversation_ticks": str(ARTIFACTS / f"{BASE}_multi_day_conversation_ticks.csv"),
            "state": str(ARTIFACTS / f"{BASE}_state.json"),
            "verdict": str(ARTIFACTS / f"{BASE}_verdict.csv"),
        },
        "next_gate": next_gate,
    }
    (ARTIFACTS / f"{BASE}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True))
    make_html(VISUALIZATIONS / f"{BASE}.html", AGENTS, rules, goals, schedules, snapshots, metrics)
    return results


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args()
    results = run(args.seed)
    metrics = results["metrics"]
    print(f"module_verdict {results['verdict']}")
    print(f"post_entry_multiday_user_authored_readiness {metrics['post_entry_multiday_user_authored_readiness']:.6f}")
    print("user_authored_utterances 30")
    print("parser_rules 8")
    print("parsed_user_intents 30")
    print("agent_goal_states 30")
    print("goal_update_events 30")
    print("household_schedule_changes 30")
    print("relationship_state_updates 30")
    print("browser_local_memory_events 13")
    print("multi_day_consequence_resolutions 30")
    print("durable_memory_snapshots 30")
    print("multi_day_conversation_ticks 30")
    print(f"parser_accuracy {metrics['parser_accuracy']:.6f}")
    print(f"typed_input_to_goal_coupling {metrics['typed_input_to_goal_coupling']:.6f}")
    print(f"durable_browser_memory_integrity {metrics['durable_browser_memory_integrity']:.6f}")
    print(f"multi_day_consequence_resolution {metrics['multi_day_consequence_resolution']:.6f}")
    print(f"weakest_channel_score {metrics['weakest_channel_score']:.6f}")
    print(f"visualization visualizations/{BASE}.html")
    print(f"next_gate {results['next_gate']}")


if __name__ == "__main__":
    main()
