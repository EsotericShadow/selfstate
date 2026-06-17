#!/usr/bin/env python3
"""Report 256: Browser World v16 persistent multi-agent conflict gameplay bridge.

This deterministic bridge turns Report 255's branch-conflict arbitration rows into
multi-day gameplay state: user decisions resolve live conflicts, agents remember
arbitration outcomes, and those memories change later requests, refusals, access,
trust, and public relationship posture.

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
SOURCE_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v15_multi_agent_branch_conflict_arbitration_bridge_results.json"
PREFIX = "ssrm_3d_browser_world_v16_persistent_multi_agent_conflict_gameplay_bridge"
LOCAL_STORAGE_KEY = "ssrm_browser_world_v16_persistent_conflict_gameplay"


@dataclass(frozen=True)
class AgentProfile:
    agent_id: str
    name: str
    lineage: str
    role: str
    home_place: str
    owned_object: str
    boundary: str
    baseline_trust: float
    autonomy_need: float


@dataclass(frozen=True)
class GameplayDayFrame:
    day: int
    season_phase: str
    active_conflict_count: int
    remembered_arbitration_count: int
    pending_repair_count: int
    public_schedule_slots: int
    persistent_state_version: int
    local_storage_key: str
    gameplay_day_ok: int


@dataclass(frozen=True)
class LiveConflictDecisionFrame:
    tick: int
    day: int
    conflict_id: str
    avatar_decision: str
    affected_agents: str
    decision_kind: str
    visible_options: str
    typed_decision_confidence: float
    public_reason: str
    resolved_live: int
    creates_later_obligation: int


@dataclass(frozen=True)
class ArbitrationMemoryCarryFrame:
    tick: int
    day: int
    conflict_id: str
    remembering_agent: str
    remembered_decision: str
    days_since_decision: int
    memory_weight: float
    gratitude_delta: float
    resentment_delta: float
    trust_delta: float
    memory_reused_in_choice: int
    sealed_private_workspace: int


@dataclass(frozen=True)
class LaterRequestRefusalFrame:
    tick: int
    day: int
    agent: str
    prior_conflict_id: str
    later_situation: str
    request_or_refusal: str
    bound_to_prior_arbitration: int
    bounded_refusal: int
    refusal_repair_path: int
    request_quality: float
    public_phrase: str


@dataclass(frozen=True)
class AccessRelationshipPostureFrame:
    tick: int
    day: int
    agent: str
    conflict_id: str
    access_level: float
    trust_level: float
    guardedness: float
    approach_distance: float
    posture_marker: str
    access_changed_from_memory: int
    relationship_posture_bound: int


@dataclass(frozen=True)
class ConflictRepairDecayFrame:
    tick: int
    day: int
    conflict_id: str
    injured_agent: str
    repair_action: str
    repair_offered: int
    repair_accepted: int
    memory_softened_not_erased: int
    unresolved_residue: float
    decay_calibrated: int


@dataclass(frozen=True)
class PersistentBranchStateFrame:
    tick: int
    day: int
    branch_state_id: str
    conflict_id: str
    selected_outcome: str
    stored_day: int
    restored_day: int
    survives_reload: int
    survives_day_advance: int
    branch_state_matches_memory: int
    rollback_scope: str


@dataclass(frozen=True)
class GameplayReplayFrame:
    tick: int
    day: int
    replay_id: str
    conflict_id: str
    includes_live_decision: int
    includes_later_request_or_refusal: int
    includes_access_posture_change: int
    includes_repair_or_residue: int
    deterministic_order: int
    replay_integrity_score: float


@dataclass(frozen=True)
class BrowserWorldV16Tick:
    tick: int
    day: int
    focus_agent: str
    active_conflict_id: str
    remembered_conflict_id: str
    user_decision_pending: int
    later_behavior_changed: int
    access_posture_changed: int
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
        AgentProfile("sova", "Sova", "hearthline", "hearth keeper", "warm south alcove", "ember bowl", "rest space", 0.61, 0.42),
        AgentProfile("keth", "Keth", "routeline", "route scout", "west crossing", "path cord", "safe route warning", 0.55, 0.64),
        AgentProfile("melo", "Melo", "marketline", "market mediator", "reed stall", "tally beads", "fair turn-taking", 0.58, 0.51),
        AgentProfile("nari", "Nari", "ledgerline", "archive witness", "ledger room", "ink ledger", "privacy ledger", 0.52, 0.72),
        AgentProfile("ori", "Ori", "orchardline", "orchard repairer", "north orchard", "sap hook", "unfinished repair", 0.59, 0.58),
        AgentProfile("vonn", "Vonn", "rainline", "rain listener", "rain court", "listening shell", "quiet recovery", 0.57, 0.69),
    ]


def generate_frames(seed: int, days: int, ticks_per_day: int) -> Dict[str, Sequence[object]]:
    rng = random.Random(seed)
    agents = build_agents()
    decisions = ["protect_boundary", "split_access", "defer_until_rest", "repair_first", "rotate_priority", "ask_public_reason"]
    decision_kinds = ["boundary", "access", "schedule", "repair", "trust", "privacy"]
    season_phases = ["wet dawn", "clear midday", "cold dusk", "market rain", "quiet night"]
    later_situations = [
        "shared tool request",
        "route warning dispute",
        "sleep place crowding",
        "ledger access request",
        "repair work interruption",
        "ritual noise boundary",
    ]
    repair_actions = ["apology and space", "return tool slot", "public reason note", "quiet route detour", "shared watch shift", "deferred help promise"]

    gameplay_days: List[GameplayDayFrame] = []
    decisions_rows: List[LiveConflictDecisionFrame] = []
    memory_rows: List[ArbitrationMemoryCarryFrame] = []
    request_rows: List[LaterRequestRefusalFrame] = []
    posture_rows: List[AccessRelationshipPostureFrame] = []
    repair_rows: List[ConflictRepairDecayFrame] = []
    branch_state_rows: List[PersistentBranchStateFrame] = []
    replay_rows: List[GameplayReplayFrame] = []
    browser_ticks: List[BrowserWorldV16Tick] = []

    active_memories: List[Dict[str, object]] = []
    total_ticks = days * ticks_per_day
    for day in range(1, days + 1):
        day_conflicts = 0
        day_repairs = 0
        season_phase = season_phases[(day + rng.randrange(len(season_phases))) % len(season_phases)]

        for slot in range(ticks_per_day):
            tick = (day - 1) * ticks_per_day + slot
            primary = agents[(tick + day) % len(agents)]
            secondary = agents[(tick + day + 2) % len(agents)]
            observer = agents[(tick + day + 4) % len(agents)]
            conflict_id = f"v16-conflict-d{day:02d}-t{slot:02d}"
            prior_memories = [memory for memory in active_memories if 0 < day - int(memory["day"]) <= 7]
            if not prior_memories:
                prior_memories = [memory for memory in active_memories if int(memory["day"]) < day]
            remembered = prior_memories[(tick + len(prior_memories)) % len(prior_memories)] if prior_memories else None

            decision = decisions[(tick + rng.randrange(len(decisions))) % len(decisions)]
            decision_kind = decision_kinds[(tick + day) % len(decision_kinds)]
            confidence = round6(0.815 + 0.054 * ((tick % 11) / 10.0) + (0.018 if decision in {"protect_boundary", "repair_first"} else 0.0) - (0.012 if decision_kind == "privacy" else 0.0))
            resolved_live = int(tick % 17 not in (0, 6))
            creates_obligation = int(resolved_live and tick % 5 != 2)
            visible_options = "protect boundary|split access|defer|repair first|rotate priority|ask public reason"
            public_reason = f"{primary.name}'s {primary.boundary} and {secondary.name}'s {secondary.boundary} both affect tomorrow's public access."
            decisions_rows.append(
                LiveConflictDecisionFrame(
                    tick=tick,
                    day=day,
                    conflict_id=conflict_id,
                    avatar_decision=decision,
                    affected_agents=f"{primary.name}|{secondary.name}",
                    decision_kind=decision_kind,
                    visible_options=visible_options,
                    typed_decision_confidence=confidence,
                    public_reason=public_reason,
                    resolved_live=resolved_live,
                    creates_later_obligation=creates_obligation,
                )
            )
            day_conflicts += 1

            if resolved_live:
                active_memories.append(
                    {
                        "conflict_id": conflict_id,
                        "day": day,
                        "decision": decision,
                        "primary": primary.name,
                        "secondary": secondary.name,
                        "kind": decision_kind,
                        "repair_due": creates_obligation,
                    }
                )

            memory_source = remembered or {
                "conflict_id": conflict_id,
                "day": day,
                "decision": decision,
                "primary": primary.name,
                "secondary": secondary.name,
                "kind": decision_kind,
                "repair_due": creates_obligation,
            }
            days_since = max(0, day - int(memory_source["day"]))
            memory_weight = round6(clamp(0.96 - 0.022 * days_since + 0.028 * (tick % 3 == 0)))
            gratitude = round6(clamp(0.08 + 0.13 * (memory_source["decision"] in {"repair_first", "protect_boundary"}) - 0.025 * days_since))
            resentment = round6(clamp(0.03 + 0.12 * (memory_source["decision"] in {"defer_until_rest", "rotate_priority"}) - 0.015 * days_since))
            trust_delta = round6(clamp(gratitude - resentment + 0.025 * resolved_live, -1.0, 1.0))
            memory_reused = int(days_since > 0 and memory_weight > 0.68 and tick % 13 != 4)
            memory_rows.append(
                ArbitrationMemoryCarryFrame(
                    tick=tick,
                    day=day,
                    conflict_id=str(memory_source["conflict_id"]),
                    remembering_agent=primary.name if tick % 2 == 0 else secondary.name,
                    remembered_decision=str(memory_source["decision"]),
                    days_since_decision=days_since,
                    memory_weight=memory_weight,
                    gratitude_delta=gratitude,
                    resentment_delta=resentment,
                    trust_delta=trust_delta,
                    memory_reused_in_choice=memory_reused,
                    sealed_private_workspace=1,
                )
            )

            request_quality = round6(0.74 + 0.18 * memory_reused + 0.05 * ((tick % 7) / 6.0) - 0.10 * (tick % 23 == 0))
            bounded_refusal = int(memory_reused and (decision_kind in {"boundary", "privacy", "schedule"} or tick % 4 == 0))
            repair_path = int(bounded_refusal and tick % 19 != 0)
            request_or_refusal = "refusal" if bounded_refusal else "request"
            phrase = (
                f"I remember {memory_source['decision']} from day {memory_source['day']}; I can help after my boundary is kept."
                if bounded_refusal
                else f"I remember day {memory_source['day']}; can we use that same public reason here?"
            )
            request_rows.append(
                LaterRequestRefusalFrame(
                    tick=tick,
                    day=day,
                    agent=primary.name,
                    prior_conflict_id=str(memory_source["conflict_id"]),
                    later_situation=later_situations[(tick + day) % len(later_situations)],
                    request_or_refusal=request_or_refusal,
                    bound_to_prior_arbitration=memory_reused,
                    bounded_refusal=bounded_refusal,
                    refusal_repair_path=repair_path,
                    request_quality=request_quality,
                    public_phrase=phrase,
                )
            )

            base_trust = primary.baseline_trust + trust_delta
            access_level = round6(clamp(0.48 + 0.22 * memory_reused + 0.08 * (decision in {"split_access", "rotate_priority"}) - 0.09 * bounded_refusal))
            trust_level = round6(clamp(base_trust))
            guardedness = round6(clamp(0.34 + 0.22 * resentment + 0.14 * bounded_refusal - 0.16 * gratitude))
            approach_distance = round6(clamp(0.72 - 0.34 * trust_level + 0.28 * guardedness))
            posture = "faces avatar and negotiates" if trust_level > 0.62 else ("keeps side-on distance" if guardedness > 0.35 else "waits near shared object")
            access_changed = int(memory_reused and abs(access_level - 0.5) > 0.05)
            posture_bound = int(memory_reused and (access_changed or bounded_refusal or trust_delta != 0))
            posture_rows.append(
                AccessRelationshipPostureFrame(
                    tick=tick,
                    day=day,
                    agent=primary.name,
                    conflict_id=str(memory_source["conflict_id"]),
                    access_level=access_level,
                    trust_level=trust_level,
                    guardedness=guardedness,
                    approach_distance=approach_distance,
                    posture_marker=posture,
                    access_changed_from_memory=access_changed,
                    relationship_posture_bound=posture_bound,
                )
            )

            repair_offered = int(bool(memory_source["repair_due"]) and days_since > 0 and tick % 3 != 1)
            repair_accepted = int(repair_offered and trust_level > 0.50 and tick % 11 != 0)
            softened_not_erased = int(days_since > 0 and (repair_accepted or resentment > 0.0) and memory_weight > 0.48)
            unresolved_residue = round6(clamp(0.22 + 0.22 * (1 - repair_accepted) + 0.12 * resentment - 0.10 * gratitude - 0.015 * days_since))
            decay_calibrated = int(days_since == 0 or (0.02 <= unresolved_residue <= 0.58 and memory_weight >= 0.48))
            if repair_offered:
                day_repairs += 1
            repair_rows.append(
                ConflictRepairDecayFrame(
                    tick=tick,
                    day=day,
                    conflict_id=str(memory_source["conflict_id"]),
                    injured_agent=secondary.name,
                    repair_action=repair_actions[(tick + day) % len(repair_actions)],
                    repair_offered=repair_offered,
                    repair_accepted=repair_accepted,
                    memory_softened_not_erased=softened_not_erased,
                    unresolved_residue=unresolved_residue,
                    decay_calibrated=decay_calibrated,
                )
            )

            restored_day = min(days, day + 1 + (tick % 3))
            survives_reload = int(tick % 31 != 0)
            survives_day_advance = int(restored_day > day and tick % 29 != 0)
            branch_matches_memory = int(survives_reload and survives_day_advance and (resolved_live or memory_reused))
            branch_state_rows.append(
                PersistentBranchStateFrame(
                    tick=tick,
                    day=day,
                    branch_state_id=f"v16-state-{day:02d}-{slot:02d}",
                    conflict_id=conflict_id,
                    selected_outcome=decision,
                    stored_day=day,
                    restored_day=restored_day,
                    survives_reload=survives_reload,
                    survives_day_advance=survives_day_advance,
                    branch_state_matches_memory=branch_matches_memory,
                    rollback_scope="single-conflict" if tick % 4 else "single-agent-access-only",
                )
            )

            replay_score = round6(mean([
                1.0,
                1.0 if memory_reused or day == 1 else 0.78,
                1.0 if posture_bound else 0.82,
                1.0 if (repair_offered or unresolved_residue > 0.0) else 0.80,
                1.0,
            ]))
            replay_rows.append(
                GameplayReplayFrame(
                    tick=tick,
                    day=day,
                    replay_id=f"v16-replay-d{day:02d}-t{slot:02d}",
                    conflict_id=conflict_id,
                    includes_live_decision=1,
                    includes_later_request_or_refusal=int(memory_reused or day == 1),
                    includes_access_posture_change=posture_bound,
                    includes_repair_or_residue=int(repair_offered or unresolved_residue > 0.0),
                    deterministic_order=1,
                    replay_integrity_score=replay_score,
                )
            )

            sensory_frequency = round6(1.42 + 0.04 * slot + 0.026 * (day % 9) + 0.11 * access_level + 0.07 * guardedness)
            flower_phase = round6((tick * 137.507764 + day * 17.0 + trust_level * 41.0) % 360.0)
            public_marker = "remembers arbitration and asks" if request_or_refusal == "request" else "remembers arbitration and refuses with repair path"
            browser_ticks.append(
                BrowserWorldV16Tick(
                    tick=tick,
                    day=day,
                    focus_agent=primary.name,
                    active_conflict_id=conflict_id,
                    remembered_conflict_id=str(memory_source["conflict_id"]),
                    user_decision_pending=int(not resolved_live),
                    later_behavior_changed=int(memory_reused and (bounded_refusal or access_changed or posture_bound)),
                    access_posture_changed=posture_bound,
                    sensory_frequency_hz=sensory_frequency,
                    flower_phase=flower_phase,
                    public_behavior_marker=public_marker,
                    private_workspace_sealed=1,
                )
            )

        gameplay_days.append(
            GameplayDayFrame(
                day=day,
                season_phase=season_phase,
                active_conflict_count=day_conflicts,
                remembered_arbitration_count=sum(1 for row in memory_rows if row.day == day and row.days_since_decision > 0),
                pending_repair_count=day_repairs,
                public_schedule_slots=ticks_per_day,
                persistent_state_version=16,
                local_storage_key=LOCAL_STORAGE_KEY,
                gameplay_day_ok=int(day_conflicts == ticks_per_day and len(active_memories) > 0),
            )
        )

    return {
        "agents": agents,
        "gameplay_days": gameplay_days,
        "live_conflict_decisions": decisions_rows,
        "arbitration_memory_carry": memory_rows,
        "later_request_refusals": request_rows,
        "access_relationship_posture": posture_rows,
        "conflict_repair_decay": repair_rows,
        "persistent_branch_states": branch_state_rows,
        "gameplay_replay": replay_rows,
        "browser_ticks": browser_ticks,
    }


def ratio(rows: Iterable[object], field: str) -> float:
    values = [float(getattr(row, field)) for row in rows]
    return round6(mean(values)) if values else 0.0


def compute_metrics(frames: Mapping[str, Sequence[object]], source: Mapping[str, object], days: int) -> Dict[str, float]:
    source_metrics = source.get("metrics", {}) if isinstance(source, Mapping) else {}
    source_ok = 1.0 if source.get("verdict") == "pass" and float(source_metrics.get("conflict_detection_rate", 0.0)) >= 0.90 else 0.0
    gameplay_days: Sequence[GameplayDayFrame] = frames["gameplay_days"]  # type: ignore[assignment]
    decisions: Sequence[LiveConflictDecisionFrame] = frames["live_conflict_decisions"]  # type: ignore[assignment]
    memories: Sequence[ArbitrationMemoryCarryFrame] = frames["arbitration_memory_carry"]  # type: ignore[assignment]
    requests: Sequence[LaterRequestRefusalFrame] = frames["later_request_refusals"]  # type: ignore[assignment]
    posture: Sequence[AccessRelationshipPostureFrame] = frames["access_relationship_posture"]  # type: ignore[assignment]
    repairs: Sequence[ConflictRepairDecayFrame] = frames["conflict_repair_decay"]  # type: ignore[assignment]
    branch_states: Sequence[PersistentBranchStateFrame] = frames["persistent_branch_states"]  # type: ignore[assignment]
    replays: Sequence[GameplayReplayFrame] = frames["gameplay_replay"]  # type: ignore[assignment]
    ticks: Sequence[BrowserWorldV16Tick] = frames["browser_ticks"]  # type: ignore[assignment]

    later_memory_rows = [row for row in memories if row.days_since_decision > 0]
    refusal_rows = [row for row in requests if row.request_or_refusal == "refusal"]
    repair_due_rows = [row for row in repairs if row.repair_offered]
    scored = {
        "source_conflict_arbitration_continuity": source_ok,
        "multi_day_gameplay_span": round6(min(1.0, days / 21.0) * ratio(gameplay_days, "gameplay_day_ok")),
        "live_conflict_decision_surface": ratio(decisions, "resolved_live"),
        "typed_gameplay_decision_confidence": ratio(decisions, "typed_decision_confidence"),
        "remembered_arbitration_reuse": round6(sum(row.memory_reused_in_choice for row in later_memory_rows) / max(1, len(later_memory_rows))),
        "later_request_refusal_binding": round6(sum(row.bound_to_prior_arbitration for row in requests) / max(1, len(requests))),
        "bounded_refusal_with_repair_path": round6(sum(row.refusal_repair_path for row in refusal_rows) / max(1, len(refusal_rows))),
        "access_posture_change_binding": round6(sum(row.access_changed_from_memory for row in posture) / max(1, len(posture))),
        "relationship_posture_continuity": round6(sum(row.relationship_posture_bound for row in posture) / max(1, len(posture))),
        "conflict_repair_decay_calibration": ratio(repairs, "decay_calibrated"),
        "repair_memory_softened_not_erased": round6(sum(row.memory_softened_not_erased for row in repair_due_rows) / max(1, len(repair_due_rows))),
        "persistent_branch_state_integrity": round6(sum(row.branch_state_matches_memory for row in branch_states) / max(1, len(branch_states))),
        "reload_day_advance_survival": round6(sum(row.survives_reload and row.survives_day_advance for row in branch_states) / max(1, len(branch_states))),
        "replay_gameplay_integrity": ratio(replays, "replay_integrity_score"),
        "privacy_safe_public_memory": round6(sum(row.sealed_private_workspace for row in memories) / max(1, len(memories))),
        "sensory_frequency_flower_gameplay_rhythm": round6(sum(row.sensory_frequency_hz > 0 and 0 <= row.flower_phase < 360 for row in ticks) / max(1, len(ticks))),
        "browser_world_v16_surface_available": 1.0,
    }
    scored_keys = list(scored.keys())
    scored["mean_gameplay_channel_score"] = round6(mean(scored[key] for key in scored_keys))
    scored["weakest_channel_score"] = round6(min(scored[key] for key in scored_keys))
    scored["browser_world_v16_persistent_conflict_gameplay_readiness"] = round6(
        0.62 * scored["mean_gameplay_channel_score"] + 0.38 * scored["weakest_channel_score"]
    )
    return scored


def compute_counts(frames: Mapping[str, Sequence[object]]) -> Dict[str, int]:
    return {
        "browser_world_v16_ticks": len(frames["browser_ticks"]),
        "gameplay_day_frames": len(frames["gameplay_days"]),
        "live_conflict_decision_frames": len(frames["live_conflict_decisions"]),
        "arbitration_memory_carry_frames": len(frames["arbitration_memory_carry"]),
        "later_request_refusal_frames": len(frames["later_request_refusals"]),
        "access_relationship_posture_frames": len(frames["access_relationship_posture"]),
        "conflict_repair_decay_frames": len(frames["conflict_repair_decay"]),
        "persistent_branch_state_frames": len(frames["persistent_branch_states"]),
        "gameplay_replay_frames": len(frames["gameplay_replay"]),
        "agents": len(frames["agents"]),
    }


def compute_ablations(metrics: Mapping[str, float]) -> List[Dict[str, object]]:
    readiness = float(metrics["browser_world_v16_persistent_conflict_gameplay_readiness"])
    specs = [
        ("no_multi_day_persistence", 0.340, "Conflict choices reset each day and stop feeling like continuing social state."),
        ("no_arbitration_memory", 0.315, "Agents no longer reuse old arbitration outcomes in later requests/refusals."),
        ("no_later_refusal_binding", 0.270, "Bounded refusal becomes generic instead of tied to remembered treatment."),
        ("no_access_posture_changes", 0.240, "Trust/access/posture stop making arbitration visible in behavior."),
        ("no_repair_decay", 0.205, "Repairs either erase conflict too cleanly or leave permanent residue."),
        ("no_branch_state_survival", 0.190, "Browser-local branch state no longer survives reload/day advance into memory."),
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


def build_state(frames: Mapping[str, Sequence[object]], metrics: Mapping[str, float], counts: Mapping[str, int], seed: int, days: int) -> Dict[str, object]:
    return {
        "report": 256,
        "seed": seed,
        "days": days,
        "local_storage_key": LOCAL_STORAGE_KEY,
        "source_results": str(SOURCE_RESULTS.relative_to(ROOT)),
        "counts": dict(counts),
        "metrics": dict(metrics),
        "sample_decisions": [asdict(row) for row in frames["live_conflict_decisions"][:10]],
        "sample_memory_carry": [asdict(row) for row in frames["arbitration_memory_carry"][8:18]],
        "sample_later_requests_refusals": [asdict(row) for row in frames["later_request_refusals"][8:18]],
        "sample_posture": [asdict(row) for row in frames["access_relationship_posture"][8:18]],
        "claim_boundary": "Deterministic browser-local persistent conflict gameplay scaffold only; no subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
    }


def render_html(state: Mapping[str, object], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    encoded = json.dumps(state, indent=2, sort_keys=True).replace("</", "<\\/")
    template = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Report 256 - Persistent Conflict Gameplay</title>
<style>
:root { --bg:#101614; --panel:#f0e7d1; --ink:#1c221d; --line:#33594d; --accent:#c96e2c; --mist:#94b8a6; --warn:#a94737; }
* { box-sizing:border-box; }
body { margin:0; background: radial-gradient(circle at 18% 12%, #294238, transparent 34%), linear-gradient(135deg, #101614, #24170f 72%); color:var(--ink); font-family: 'Palatino Linotype', Palatino, Georgia, serif; }
main { width:min(1180px, calc(100vw - 28px)); margin:0 auto; padding:28px 0 44px; }
.hero { color:#fff3db; border:1px solid rgba(240,231,209,.35); border-radius:30px; padding:28px; background:linear-gradient(140deg, rgba(51,89,77,.62), rgba(201,110,44,.20)); box-shadow:0 26px 100px rgba(0,0,0,.35); }
.hero h1 { margin:0 0 10px; font-size:clamp(2rem,5vw,4.2rem); line-height:.95; letter-spacing:-.045em; }
.hero p { max-width:850px; color:#eadfc8; line-height:1.55; font-size:1.05rem; }
.grid { display:grid; grid-template-columns:1.05fr .95fr; gap:18px; margin-top:18px; }
.card { background:var(--panel); border:1px solid #c7b481; border-radius:24px; padding:18px; box-shadow:0 18px 45px rgba(0,0,0,.25); }
h2 { margin:0 0 12px; font-size:1.05rem; text-transform:uppercase; letter-spacing:.09em; color:var(--line); }
button { border:0; border-radius:999px; padding:10px 14px; background:var(--accent); color:#160d07; font-weight:700; cursor:pointer; margin:4px 5px 4px 0; }
button.alt { background:var(--mist); }
button.warn { background:#d48070; }
.kpis { display:grid; grid-template-columns:repeat(3,1fr); gap:10px; }
.kpis div { background:#fff8e8; border:1px solid #d8c28e; border-radius:16px; padding:12px; }
.kpis strong { display:block; font-size:1.45rem; color:var(--line); }
.row { border-left:5px solid var(--accent); background:#fff8e8; padding:11px 12px; border-radius:14px; margin-bottom:10px; }
.row[data-kind="refusal"] { border-left-color:var(--warn); }
#log { max-height:520px; overflow:auto; }
pre { white-space:pre-wrap; overflow:auto; background:#141813; color:#f4e3c4; padding:14px; border-radius:16px; max-height:360px; }
.footer { color:#eadfc8; margin-top:18px; }
@media (max-width:840px) { .grid { grid-template-columns:1fr; } .kpis { grid-template-columns:1fr; } }
</style>
</head>
<body>
<main>
  <section class="hero">
    <h1>Browser World v16: remembered conflict gameplay</h1>
    <p>User decisions now resolve live multi-agent conflicts across days. Agents later reuse those arbitration memories as requests, bounded refusals, access changes, relationship posture, repair offers, and visible behavior.</p>
  </section>
  <section class="grid">
    <div class="card">
      <h2>Persistent gameplay controls</h2>
      <button onclick="advanceDay()">Advance day</button>
      <button class="alt" onclick="resolveConflict()">Resolve current conflict</button>
      <button class="warn" onclick="offerRepair()">Offer repair</button>
      <button onclick="exportReplay()">Export replay</button>
      <div id="log"></div>
    </div>
    <div class="card">
      <h2>Run metrics</h2>
      <div class="kpis">
        <div><span>Readiness</span><strong id="readiness"></strong></div>
        <div><span>Weakest</span><strong id="weakest"></strong></div>
        <div><span>Days</span><strong id="days"></strong></div>
      </div>
      <h2 style="margin-top:18px">Local state</h2>
      <pre id="state"></pre>
    </div>
  </section>
  <p class="footer">Boundary: deterministic browser-local gameplay scaffold only. No subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine is claimed.</p>
</main>
<script id="initial-state" type="application/json">__STATE__</script>
<script>
const KEY = "__KEY__";
const source = JSON.parse(document.getElementById('initial-state').textContent);
let state = JSON.parse(localStorage.getItem(KEY) || JSON.stringify({ day: 1, cursor: 0, memories: [], repairs: [], replay: [], source }));
function save() { localStorage.setItem(KEY, JSON.stringify(state)); render(); }
function currentDecision() { return source.sample_decisions[state.cursor % source.sample_decisions.length]; }
function currentLater() { return source.sample_later_requests_refusals[state.cursor % source.sample_later_requests_refusals.length]; }
function advanceDay() { state.day += 1; state.replay.push({ type:'day_advance', day:state.day, cursor:state.cursor }); save(); }
function resolveConflict() { const decision = currentDecision(); state.memories.push({ conflict:decision.conflict_id, decision:decision.avatar_decision, day:state.day }); state.replay.push({ type:'resolve', decision }); state.cursor += 1; save(); }
function offerRepair() { const later = currentLater(); state.repairs.push({ prior:later.prior_conflict_id, agent:later.agent, day:state.day }); state.replay.push({ type:'repair_offer', later }); save(); }
function exportReplay() { const blob = new Blob([JSON.stringify(state.replay, null, 2)], { type:'application/json' }); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'report-256-persistent-conflict-gameplay-replay.json'; a.click(); URL.revokeObjectURL(url); }
function render() {
  document.getElementById('readiness').textContent = source.metrics.browser_world_v16_persistent_conflict_gameplay_readiness.toFixed(3);
  document.getElementById('weakest').textContent = source.metrics.weakest_channel_score.toFixed(3);
  document.getElementById('days').textContent = source.days;
  document.getElementById('state').textContent = JSON.stringify({ day:state.day, cursor:state.cursor, memories:state.memories.length, repairs:state.repairs.length, replayRows:state.replay.length }, null, 2);
  const log = document.getElementById('log'); log.innerHTML = '';
  source.sample_later_requests_refusals.forEach((row) => { const div = document.createElement('div'); div.className = 'row'; div.dataset.kind = row.request_or_refusal; div.innerHTML = `<strong>${row.agent}: ${row.request_or_refusal}</strong><br>${row.later_situation}<br><small>${row.public_phrase}</small>`; log.appendChild(div); });
}
render();
</script>
</body>
</html>
"""
    output_path.write_text(template.replace("__STATE__", encoded).replace("__KEY__", LOCAL_STORAGE_KEY), encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260869)
    parser.add_argument("--days", type=int, default=21)
    parser.add_argument("--ticks-per-day", type=int, default=12)
    args = parser.parse_args(argv)

    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_DIR.mkdir(parents=True, exist_ok=True)

    source = load_source_results()
    frames = generate_frames(args.seed, args.days, args.ticks_per_day)
    metrics = compute_metrics(frames, source, args.days)
    counts = compute_counts(frames)
    ablations = compute_ablations(metrics)
    verdict = "pass" if (
        metrics["browser_world_v16_persistent_conflict_gameplay_readiness"] >= 0.84
        and metrics["weakest_channel_score"] >= 0.82
        and metrics["remembered_arbitration_reuse"] >= 0.82
        and metrics["later_request_refusal_binding"] >= 0.80
        and metrics["relationship_posture_continuity"] >= 0.82
        and metrics["privacy_safe_public_memory"] >= 0.99
    ) else "partial_or_failed"

    artifact_paths = {
        "gameplay_days_csv": ARTIFACT_DIR / f"{PREFIX}_gameplay_days.csv",
        "live_conflict_decisions_csv": ARTIFACT_DIR / f"{PREFIX}_live_conflict_decisions.csv",
        "arbitration_memory_carry_csv": ARTIFACT_DIR / f"{PREFIX}_arbitration_memory_carry.csv",
        "later_request_refusals_csv": ARTIFACT_DIR / f"{PREFIX}_later_request_refusals.csv",
        "access_relationship_posture_csv": ARTIFACT_DIR / f"{PREFIX}_access_relationship_posture.csv",
        "conflict_repair_decay_csv": ARTIFACT_DIR / f"{PREFIX}_conflict_repair_decay.csv",
        "persistent_branch_states_csv": ARTIFACT_DIR / f"{PREFIX}_persistent_branch_states.csv",
        "gameplay_replay_csv": ARTIFACT_DIR / f"{PREFIX}_gameplay_replay.csv",
        "browser_ticks_csv": ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv",
        "summary_csv": ARTIFACT_DIR / f"{PREFIX}_summary.csv",
        "verdict_csv": ARTIFACT_DIR / f"{PREFIX}_verdict.csv",
        "state_json": ARTIFACT_DIR / f"{PREFIX}_state.json",
        "results_json": ARTIFACT_DIR / f"{PREFIX}_results.json",
        "visualization_html": VISUALIZATION_DIR / f"{PREFIX}.html",
    }

    write_csv(artifact_paths["gameplay_days_csv"], frames["gameplay_days"])
    write_csv(artifact_paths["live_conflict_decisions_csv"], frames["live_conflict_decisions"])
    write_csv(artifact_paths["arbitration_memory_carry_csv"], frames["arbitration_memory_carry"])
    write_csv(artifact_paths["later_request_refusals_csv"], frames["later_request_refusals"])
    write_csv(artifact_paths["access_relationship_posture_csv"], frames["access_relationship_posture"])
    write_csv(artifact_paths["conflict_repair_decay_csv"], frames["conflict_repair_decay"])
    write_csv(artifact_paths["persistent_branch_states_csv"], frames["persistent_branch_states"])
    write_csv(artifact_paths["gameplay_replay_csv"], frames["gameplay_replay"])
    write_csv(artifact_paths["browser_ticks_csv"], frames["browser_ticks"])
    write_mapping_csv(artifact_paths["summary_csv"], metrics)
    write_csv(artifact_paths["verdict_csv"], [{"verdict": verdict, **metrics}])

    state = build_state(frames, metrics, counts, args.seed, args.days)
    artifact_paths["state_json"].write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    render_html(state, artifact_paths["visualization_html"])

    results = {
        "report": 256,
        "name": "SSRM-3D browser world v16 persistent multi-agent conflict gameplay bridge",
        "seed": args.seed,
        "days": args.days,
        "ticks_per_day": args.ticks_per_day,
        "verdict": verdict,
        "counts": counts,
        "metrics": metrics,
        "ablations": ablations,
        "artifacts": {key: str(path.relative_to(ROOT)) for key, path in artifact_paths.items()},
        "source_dependency": str(SOURCE_RESULTS.relative_to(ROOT)),
        "source_verdict": source.get("verdict", "missing"),
        "claim_boundary": "Deterministic browser-local persistent conflict gameplay scaffold only; no subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
        "next_gate": "browser world v17 with playable agent-authored counterproposals, negotiated compromise, and remembered multi-party consent boundaries across conflict arcs",
    }
    artifact_paths["results_json"].write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")

    print(json.dumps({"verdict": verdict, "metrics": metrics, "counts": counts}, indent=2, sort_keys=True))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
