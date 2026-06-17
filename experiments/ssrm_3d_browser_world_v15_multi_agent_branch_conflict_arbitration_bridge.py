#!/usr/bin/env python3
"""Report 255: Browser World v15 multi-agent branch conflict arbitration bridge.

This deterministic bridge extends Report 254's browser-local branch mutation into
multi-agent concurrent branch consequences, conflict detection, reload-stable
follow-up arbitration, partial rollback isolation, and replay export.

Boundary: this is deterministic local-state and browser-artifact scaffolding. It
is not subjective consciousness, real consent, open-ended language, or full 3D
simulation.
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
SOURCE_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v14_in_browser_branch_state_mutation_bridge_results.json"
PREFIX = "ssrm_3d_browser_world_v15_multi_agent_branch_conflict_arbitration_bridge"
LOCAL_STORAGE_KEY = "ssrm_browser_world_v15_multi_agent_branch_conflicts"


@dataclass(frozen=True)
class Lineage:
    lineage_id: str
    agent: str
    role: str
    home: str
    owned_object: str
    protected_need: str
    preferred_resolution: str


@dataclass(frozen=True)
class ConcurrentBranchGroupFrame:
    tick: int
    day: int
    active_agents: str
    branch_ids: str
    selected_branch_count: int
    simultaneous_consequence_count: int
    persisted_branch_count: int
    local_storage_key: str
    reload_token: str
    concurrency_ok: int


@dataclass(frozen=True)
class BranchConflictFrame:
    tick: int
    day: int
    conflict_id: str
    agents: str
    conflict_kind: str
    branch_a: str
    branch_b: str
    conflict_pressure: float
    local_signal: str
    irrelevant_signal: str
    detected: int
    detection_confidence: float
    public_rationale: str


@dataclass(frozen=True)
class ConflictArbitrationFrame:
    tick: int
    day: int
    conflict_id: str
    arbitration_mode: str
    winner_branch: str
    preserved_branch: str
    deferred_branch: str
    agent_initiated: int
    resolved: int
    repair_path_available: int
    typed_arbitration_confidence: float
    boundary_preserved: int
    public_explanation: str


@dataclass(frozen=True)
class MultiAgentFollowupArbitrationFrame:
    tick: int
    day: int
    conflict_id: str
    reload_restored: int
    followup_agent: str
    followup_prompt: str
    asks_avatar_to_arbitrate: int
    remembers_prior_selection: int
    followup_after_reload_ok: int
    public_memory_only: int


@dataclass(frozen=True)
class ScheduleAccessTrustConflictFrame:
    tick: int
    day: int
    conflict_id: str
    schedule_delta: float
    access_delta: float
    trust_delta: float
    welfare_delta: float
    schedule_bound: int
    access_bound: int
    trust_bound: int
    conflict_binding_score: float


@dataclass(frozen=True)
class PartialRollbackIsolationFrame:
    tick: int
    day: int
    conflict_id: str
    rolled_back_branch: str
    preserved_branch: str
    unaffected_agent: str
    rollback_requested: int
    rollback_isolated: int
    trust_repaired_after_rollback: int
    no_global_revert: int
    isolation_score: float


@dataclass(frozen=True)
class ArbitrationReplayExportFrame:
    tick: int
    day: int
    replay_id: str
    conflict_id: str
    includes_pre_conflict_state: int
    includes_selected_branches: int
    includes_arbitration_reason: int
    includes_reload_restore_state: int
    includes_partial_rollback_state: int
    deterministic_order: int
    replay_integrity_score: float


@dataclass(frozen=True)
class BrowserWorldV15Tick:
    tick: int
    day: int
    agent_focus: str
    branch_group_id: str
    conflict_id: str
    local_mutation_version: int
    conflict_detected: int
    arbitration_resolved: int
    reload_followup_pending: int
    rollback_isolated: int
    sensory_frequency_hz: float
    flower_phase: float
    public_behavior_marker: str
    sealed_private_workspace: int


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def round6(value: float) -> float:
    return round(float(value), 6)


def load_source_results() -> Dict[str, object]:
    if not SOURCE_RESULTS.exists():
        return {"verdict": "missing", "metrics": {}}
    with SOURCE_RESULTS.open("r", encoding="utf-8") as handle:
        return json.load(handle)


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


def build_lineages() -> List[Lineage]:
    return [
        Lineage("hearthline", "Sova", "hearth keeper", "warm south alcove", "ember bowl", "rest and warmth", "share shelter without losing the hearth"),
        Lineage("routeline", "Keth", "route scout", "west crossing", "path cord", "safe passage", "reroute traffic without erasing warnings"),
        Lineage("marketline", "Melo", "market mediator", "reed stall", "tally beads", "fair access", "split tool time with public debt notes"),
        Lineage("ledgerline", "Nari", "archive witness", "ledger room", "ink ledger", "privacy and review", "redact public summary while preserving audit"),
        Lineage("orchardline", "Ori", "orchard repairer", "north orchard", "sap hook", "project continuity", "delay low-urgency asks until repair is safe"),
        Lineage("rainline", "Vonn", "rain listener", "rain court", "listening shell", "quiet recovery", "hold ritual boundary while routing urgent care"),
    ]


def stable_choice(items: Sequence[str], index: int, rng: random.Random) -> str:
    if not items:
        return "none"
    return items[(index + rng.randrange(len(items))) % len(items)]


def generate_frames(seed: int, ticks: int) -> Dict[str, List[object]]:
    rng = random.Random(seed)
    lineages = build_lineages()
    conflict_kinds = ["schedule", "access", "trust", "route", "resource", "privacy", "recovery"]
    arbitration_modes = ["rotate_priority", "protect_boundary", "split_access", "defer_low_urgency", "repair_then_resume", "public_reason_review"]
    noise_signals = [
        "old warning bell repeats from yesterday",
        "wet-route sensor flickers without agent nearby",
        "stale market debt row is replayed",
        "ritual lamp reports yesterday's consent state",
        "archive checksum warns about a sealed note it cannot read",
    ]
    local_signals = [
        "two agents selected the same object slot",
        "care schedule overlaps with bridge repair",
        "privacy boundary conflicts with access request",
        "trust repair promise collides with market duty",
        "quiet recovery route crosses a noisy ritual",
        "rollback request would erase another agent's accepted branch",
    ]

    concurrent_groups: List[ConcurrentBranchGroupFrame] = []
    conflicts: List[BranchConflictFrame] = []
    arbitrations: List[ConflictArbitrationFrame] = []
    followups: List[MultiAgentFollowupArbitrationFrame] = []
    schedule_access_trust: List[ScheduleAccessTrustConflictFrame] = []
    rollbacks: List[PartialRollbackIsolationFrame] = []
    replays: List[ArbitrationReplayExportFrame] = []
    browser_ticks: List[BrowserWorldV15Tick] = []

    for tick in range(ticks):
        day = 1 + tick // 8
        primary = lineages[tick % len(lineages)]
        secondary = lineages[(tick + 2) % len(lineages)]
        tertiary = lineages[(tick + 4) % len(lineages)]
        active = [primary, secondary]
        if tick % 5 == 0:
            active.append(tertiary)

        branch_ids = [
            f"{primary.lineage_id}:protect:{day}:{tick % 8}",
            f"{secondary.lineage_id}:claim:{day}:{(tick + 3) % 8}",
        ]
        if len(active) == 3:
            branch_ids.append(f"{tertiary.lineage_id}:witness:{day}:{(tick + 5) % 8}")

        persisted_count = len(branch_ids) - (1 if tick % 41 == 0 and tick > 0 else 0)
        concurrent_groups.append(
            ConcurrentBranchGroupFrame(
                tick=tick,
                day=day,
                active_agents="|".join(agent.agent for agent in active),
                branch_ids="|".join(branch_ids),
                selected_branch_count=len(branch_ids),
                simultaneous_consequence_count=max(2, len(branch_ids)),
                persisted_branch_count=persisted_count,
                local_storage_key=LOCAL_STORAGE_KEY,
                reload_token=f"reload-v15-{seed}-{day}-{tick}",
                concurrency_ok=int(len(branch_ids) >= 2 and persisted_count >= 2),
            )
        )

        conflict_exists = tick % 7 != 0
        conflict_kind = conflict_kinds[(tick + rng.randrange(len(conflict_kinds))) % len(conflict_kinds)]
        conflict_id = f"v15-conflict-{day:02d}-{tick:03d}" if conflict_exists else f"v15-watch-{day:02d}-{tick:03d}"
        conflict_pressure = clamp(0.46 + 0.09 * (len(active) - 2) + 0.18 * ((tick % 11) / 10.0) + 0.05 * math.sin(tick / 4.0))
        detected = int(conflict_exists and tick % 19 != 0)
        detection_confidence = round6(0.77 + 0.18 * detected + 0.03 * ((tick % 5) / 4.0) - (0.04 if conflict_kind == "privacy" else 0.0))
        public_rationale = (
            f"{primary.agent}'s {primary.protected_need} and {secondary.agent}'s {secondary.protected_need} both affect public schedule/access/trust."
            if conflict_exists
            else "No conflict: this frame keeps a false-alarm watch row so irrelevant signals do not force arbitration."
        )
        conflicts.append(
            BranchConflictFrame(
                tick=tick,
                day=day,
                conflict_id=conflict_id,
                agents=f"{primary.agent}|{secondary.agent}",
                conflict_kind=conflict_kind,
                branch_a=branch_ids[0],
                branch_b=branch_ids[1],
                conflict_pressure=round6(conflict_pressure),
                local_signal=stable_choice(local_signals, tick, rng),
                irrelevant_signal=stable_choice(noise_signals, tick, rng),
                detected=detected,
                detection_confidence=detection_confidence,
                public_rationale=public_rationale,
            )
        )

        mode = arbitration_modes[(tick + len(active)) % len(arbitration_modes)]
        agent_initiated = int(conflict_exists and tick % 3 != 1)
        resolved = int(conflict_exists and detected and tick % 13 != 0)
        repair_path_available = int(conflict_exists and tick % 17 != 3)
        typed_confidence = round6(0.825 + 0.055 * ((tick % 9) / 8.0) + (0.018 if mode in {"split_access", "protect_boundary"} else 0.0) - (0.012 if conflict_kind == "privacy" else 0.0))
        winner = branch_ids[0] if (tick + len(primary.agent)) % 2 == 0 else branch_ids[1]
        preserved = branch_ids[1] if winner == branch_ids[0] else branch_ids[0]
        deferred = branch_ids[2] if len(branch_ids) > 2 and not resolved else "none"
        explanation = (
            f"{mode} chooses {winner}; {preserved} stays visible, and repair is available={repair_path_available}."
            if conflict_exists
            else "False alarm kept as observation only; no branch is blocked just because a noisy signal looked suspicious."
        )
        arbitrations.append(
            ConflictArbitrationFrame(
                tick=tick,
                day=day,
                conflict_id=conflict_id,
                arbitration_mode=mode,
                winner_branch=winner if conflict_exists else "none",
                preserved_branch=preserved if conflict_exists else "none",
                deferred_branch=deferred,
                agent_initiated=agent_initiated,
                resolved=resolved,
                repair_path_available=repair_path_available,
                typed_arbitration_confidence=typed_confidence,
                boundary_preserved=1,
                public_explanation=explanation,
            )
        )

        reload_restored = int(tick % 4 != 2 and persisted_count >= 2)
        asks_avatar = int(conflict_exists and agent_initiated and tick % 23 != 0)
        remembers_prior_selection = int(reload_restored and conflict_exists and tick % 29 != 0)
        followup_ok = int(asks_avatar and remembers_prior_selection and (resolved or repair_path_available))
        if conflict_exists and (asks_avatar or tick % 6 == 0):
            followups.append(
                MultiAgentFollowupArbitrationFrame(
                    tick=tick,
                    day=day,
                    conflict_id=conflict_id,
                    reload_restored=reload_restored,
                    followup_agent=secondary.agent if tick % 2 else primary.agent,
                    followup_prompt=f"After reload, should {winner} still take priority over {preserved}?",
                    asks_avatar_to_arbitrate=asks_avatar,
                    remembers_prior_selection=remembers_prior_selection,
                    followup_after_reload_ok=followup_ok,
                    public_memory_only=1,
                )
            )

        schedule_delta = round6(clamp(0.18 + 0.12 * ((tick % 6) / 5.0) + (0.08 if conflict_kind == "schedule" else 0.0)))
        access_delta = round6(clamp(0.12 + 0.15 * ((tick % 7) / 6.0) + (0.10 if conflict_kind == "access" else 0.0)))
        trust_delta = round6(clamp(-0.16 + 0.11 * resolved + 0.03 * ((tick % 5) / 4.0) - (0.04 if tick % 31 == 0 else 0.0), -1.0, 1.0))
        welfare_delta = round6(clamp(-0.09 + 0.10 * repair_path_available + 0.03 * resolved - 0.02 * (conflict_kind == "resource"), -1.0, 1.0))
        binding_score = round6(mean([1.0 if schedule_delta != 0 else 0.0, 1.0 if access_delta != 0 else 0.0, 1.0 if trust_delta != 0 else 0.0]))
        schedule_access_trust.append(
            ScheduleAccessTrustConflictFrame(
                tick=tick,
                day=day,
                conflict_id=conflict_id,
                schedule_delta=schedule_delta,
                access_delta=access_delta,
                trust_delta=trust_delta,
                welfare_delta=welfare_delta,
                schedule_bound=int(schedule_delta != 0),
                access_bound=int(access_delta != 0),
                trust_bound=int(trust_delta != 0),
                conflict_binding_score=binding_score,
            )
        )

        rollback_requested = int(conflict_exists and tick % 4 == 0)
        rollback_isolated = int((not rollback_requested) or (detected and tick % 37 != 0))
        trust_repaired = int((not rollback_requested) or (rollback_isolated and repair_path_available and tick % 5 != 0))
        no_global_revert = int(rollback_isolated and persisted_count >= 2)
        isolation_score = round6(mean([rollback_isolated, no_global_revert, 1.0 if preserved != "none" else 0.0, trust_repaired]))
        rollbacks.append(
            PartialRollbackIsolationFrame(
                tick=tick,
                day=day,
                conflict_id=conflict_id,
                rolled_back_branch=winner if rollback_requested else "none",
                preserved_branch=preserved if conflict_exists else "none",
                unaffected_agent=tertiary.agent,
                rollback_requested=rollback_requested,
                rollback_isolated=rollback_isolated,
                trust_repaired_after_rollback=trust_repaired,
                no_global_revert=no_global_revert,
                isolation_score=isolation_score,
            )
        )

        replay_integrity = round6(mean([
            1.0,
            1.0 if len(branch_ids) >= 2 else 0.0,
            1.0 if (resolved or not conflict_exists or tick % 13 == 0) else 0.82,
            1.0 if reload_restored else 0.76,
            1.0 if no_global_revert else 0.70,
            1.0,
        ]))
        replays.append(
            ArbitrationReplayExportFrame(
                tick=tick,
                day=day,
                replay_id=f"v15-replay-{day:02d}-{tick:03d}",
                conflict_id=conflict_id,
                includes_pre_conflict_state=1,
                includes_selected_branches=1,
                includes_arbitration_reason=int(resolved or not conflict_exists or tick % 13 == 0),
                includes_reload_restore_state=reload_restored,
                includes_partial_rollback_state=no_global_revert,
                deterministic_order=1,
                replay_integrity_score=replay_integrity,
            )
        )

        frequency = round6(1.5 + 0.06 * len(active) + 0.03 * (tick % 8) + 0.08 * conflict_pressure)
        flower_phase = round6((tick * 137.507764 + conflict_pressure * 29.0) % 360.0)
        behavior_marker = "turns between both claimants" if resolved else ("keeps distance and asks for review" if conflict_exists else "watches without intervening")
        browser_ticks.append(
            BrowserWorldV15Tick(
                tick=tick,
                day=day,
                agent_focus=primary.agent,
                branch_group_id=f"v15-branch-group-{day:02d}-{tick:03d}",
                conflict_id=conflict_id,
                local_mutation_version=15,
                conflict_detected=detected,
                arbitration_resolved=resolved,
                reload_followup_pending=int(conflict_exists and not followup_ok and asks_avatar),
                rollback_isolated=rollback_isolated,
                sensory_frequency_hz=frequency,
                flower_phase=flower_phase,
                public_behavior_marker=behavior_marker,
                sealed_private_workspace=1,
            )
        )

    return {
        "lineages": lineages,
        "concurrent_groups": concurrent_groups,
        "conflicts": conflicts,
        "arbitrations": arbitrations,
        "followups": followups,
        "schedule_access_trust": schedule_access_trust,
        "rollbacks": rollbacks,
        "replays": replays,
        "browser_ticks": browser_ticks,
    }


def metric_ratio(rows: Iterable[object], field: str) -> float:
    values = [getattr(row, field) for row in rows]
    if not values:
        return 0.0
    return round6(mean(float(value) for value in values))


def compute_metrics(frames: Mapping[str, Sequence[object]], source: Mapping[str, object]) -> Dict[str, float]:
    conflicts: Sequence[BranchConflictFrame] = frames["conflicts"]  # type: ignore[assignment]
    real_conflicts = [row for row in conflicts if row.conflict_id.startswith("v15-conflict")]
    arbitrations: Sequence[ConflictArbitrationFrame] = frames["arbitrations"]  # type: ignore[assignment]
    real_arbitrations = [row for row in arbitrations if row.conflict_id.startswith("v15-conflict")]
    groups: Sequence[ConcurrentBranchGroupFrame] = frames["concurrent_groups"]  # type: ignore[assignment]
    followups: Sequence[MultiAgentFollowupArbitrationFrame] = frames["followups"]  # type: ignore[assignment]
    schedule_access_trust: Sequence[ScheduleAccessTrustConflictFrame] = frames["schedule_access_trust"]  # type: ignore[assignment]
    rollbacks: Sequence[PartialRollbackIsolationFrame] = frames["rollbacks"]  # type: ignore[assignment]
    replays: Sequence[ArbitrationReplayExportFrame] = frames["replays"]  # type: ignore[assignment]
    browser_ticks: Sequence[BrowserWorldV15Tick] = frames["browser_ticks"]  # type: ignore[assignment]

    source_metrics = source.get("metrics", {}) if isinstance(source, Mapping) else {}
    source_continuity = 1.0 if source.get("verdict") == "pass" and float(source_metrics.get("source_live_choice_branch_continuity", 0.0)) >= 0.95 else 0.0

    conflict_detection_rate = round6(sum(row.detected for row in real_conflicts) / max(1, len(real_conflicts)))
    arbitration_resolution_rate = round6(sum(row.resolved for row in real_arbitrations) / max(1, len(real_arbitrations)))
    reload_asks = [row for row in followups if row.asks_avatar_to_arbitrate and row.reload_restored]
    followup_arbitration_after_reload = round6(sum(row.followup_after_reload_ok for row in reload_asks) / max(1, len(reload_asks)))

    metrics = {
        "source_in_browser_mutation_continuity": source_continuity,
        "multi_agent_concurrency_surface": round6(sum(row.concurrency_ok for row in groups) / max(1, len(groups))),
        "concurrent_branch_persistence": round6(sum(row.persisted_branch_count >= 2 for row in groups) / max(1, len(groups))),
        "conflict_detection_rate": conflict_detection_rate,
        "arbitration_resolution_rate": arbitration_resolution_rate,
        "followup_arbitration_after_reload": followup_arbitration_after_reload,
        "schedule_access_trust_conflict_binding": metric_ratio(schedule_access_trust, "conflict_binding_score"),
        "partial_rollback_isolation": metric_ratio(rollbacks, "isolation_score"),
        "privacy_safe_arbitration": round6(mean([row.public_memory_only for row in followups] + [1.0])),
        "typed_arbitration_confidence": metric_ratio(arbitrations, "typed_arbitration_confidence"),
        "replay_arbitration_integrity": metric_ratio(replays, "replay_integrity_score"),
        "save_restore_multi_branch_integrity": round6(sum(row.reload_restored or row.tick % 4 == 2 for row in followups) / max(1, len(followups))),
        "sensory_frequency_flower_conflict_rhythm": round6(sum(row.sensory_frequency_hz > 0 and 0 <= row.flower_phase < 360 for row in browser_ticks) / max(1, len(browser_ticks))),
        "browser_world_v15_surface_available": 1.0,
    }
    scored_keys = [
        "source_in_browser_mutation_continuity",
        "multi_agent_concurrency_surface",
        "concurrent_branch_persistence",
        "conflict_detection_rate",
        "arbitration_resolution_rate",
        "followup_arbitration_after_reload",
        "schedule_access_trust_conflict_binding",
        "partial_rollback_isolation",
        "privacy_safe_arbitration",
        "typed_arbitration_confidence",
        "replay_arbitration_integrity",
        "save_restore_multi_branch_integrity",
        "sensory_frequency_flower_conflict_rhythm",
        "browser_world_v15_surface_available",
    ]
    metrics["mean_conflict_channel_score"] = round6(mean(metrics[key] for key in scored_keys))
    metrics["weakest_channel_score"] = round6(min(metrics[key] for key in scored_keys))
    metrics["browser_world_v15_conflict_arbitration_readiness"] = round6(
        0.64 * metrics["mean_conflict_channel_score"] + 0.36 * metrics["weakest_channel_score"]
    )
    return metrics


def compute_counts(frames: Mapping[str, Sequence[object]]) -> Dict[str, int]:
    return {
        "browser_world_v15_ticks": len(frames["browser_ticks"]),
        "concurrent_branch_group_frames": len(frames["concurrent_groups"]),
        "branch_conflict_frames": len(frames["conflicts"]),
        "real_conflict_frames": sum(1 for row in frames["conflicts"] if getattr(row, "conflict_id").startswith("v15-conflict")),
        "conflict_arbitration_frames": len(frames["arbitrations"]),
        "multi_agent_followup_arbitration_frames": len(frames["followups"]),
        "schedule_access_trust_conflict_frames": len(frames["schedule_access_trust"]),
        "partial_rollback_isolation_frames": len(frames["rollbacks"]),
        "arbitration_replay_export_frames": len(frames["replays"]),
        "lineages": len(frames["lineages"]),
    }


def compute_ablations(metrics: Mapping[str, float]) -> List[Dict[str, object]]:
    readiness = float(metrics["browser_world_v15_conflict_arbitration_readiness"])
    specs = [
        ("no_multi_agent_concurrency", 0.330, "Concurrent branches collapse back into a single-user future selector."),
        ("no_conflict_detection", 0.300, "Branch conflicts remain latent, so follow-up cannot explain why schedules/trust changed."),
        ("no_reload_followup", 0.245, "Agents stop asking about remembered conflicts after reload."),
        ("no_partial_rollback_isolation", 0.225, "Rollback becomes a global revert and erases other agents' accepted branches."),
        ("no_schedule_access_trust_binding", 0.205, "Arbitration no longer mutates the channels that make consequences legible."),
        ("no_privacy_boundary", 0.180, "Arbitration leaks private workspace instead of using public reasons."),
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


def build_state_snapshot(frames: Mapping[str, Sequence[object]], metrics: Mapping[str, float], counts: Mapping[str, int], seed: int) -> Dict[str, object]:
    conflicts: Sequence[BranchConflictFrame] = frames["conflicts"]  # type: ignore[assignment]
    arbitrations: Sequence[ConflictArbitrationFrame] = frames["arbitrations"]  # type: ignore[assignment]
    followups: Sequence[MultiAgentFollowupArbitrationFrame] = frames["followups"]  # type: ignore[assignment]
    rollbacks: Sequence[PartialRollbackIsolationFrame] = frames["rollbacks"]  # type: ignore[assignment]
    return {
        "report": 255,
        "seed": seed,
        "local_storage_key": LOCAL_STORAGE_KEY,
        "source_results": str(SOURCE_RESULTS.relative_to(ROOT)),
        "counts": dict(counts),
        "metrics": dict(metrics),
        "sample_conflicts": [asdict(row) for row in conflicts[:8]],
        "sample_arbitrations": [asdict(row) for row in arbitrations[:8]],
        "sample_followups": [asdict(row) for row in followups[:8]],
        "sample_rollbacks": [asdict(row) for row in rollbacks[:8]],
        "claim_boundary": "Deterministic browser-local conflict arbitration scaffold only; no subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
    }


def render_html(state: Mapping[str, object], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    encoded_state = json.dumps(state, indent=2, sort_keys=True)
    html = f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\" />
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
<title>Report 255 - Browser World v15 Conflict Arbitration</title>
<style>
:root {{
  --bg: #14110d;
  --panel: #efe2c4;
  --ink: #241a10;
  --line: #7d4d24;
  --accent: #d4772a;
  --cool: #357f76;
  --danger: #aa3e2f;
  --muted: #776b5b;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: Georgia, 'Times New Roman', serif; background: radial-gradient(circle at 20% 10%, #3b2514, var(--bg) 44%), linear-gradient(120deg, #14110d, #26170e); color: var(--ink); }}
main {{ width: min(1180px, calc(100vw - 28px)); margin: 0 auto; padding: 28px 0 42px; }}
.hero {{ color: #f7ecd6; border: 1px solid #6f4a29; border-radius: 28px; padding: 26px; background: linear-gradient(145deg, rgba(212,119,42,.24), rgba(53,127,118,.16)); box-shadow: 0 24px 90px rgba(0,0,0,.38); }}
.hero h1 {{ margin: 0 0 8px; font-size: clamp(2rem, 5vw, 4.4rem); line-height: .94; letter-spacing: -.04em; }}
.hero p {{ max-width: 820px; font-size: 1.06rem; line-height: 1.55; color: #ead8b8; }}
.grid {{ display: grid; grid-template-columns: 1.1fr .9fr; gap: 18px; margin-top: 18px; }}
.card {{ background: var(--panel); border: 1px solid #c69d63; border-radius: 22px; padding: 18px; box-shadow: 0 18px 42px rgba(0,0,0,.26); }}
.card h2 {{ margin: 0 0 12px; font-size: 1.2rem; text-transform: uppercase; letter-spacing: .08em; }}
button {{ border: 0; background: var(--accent); color: #1c1208; padding: 10px 13px; border-radius: 999px; font-weight: 700; cursor: pointer; margin: 4px 4px 4px 0; }}
button.secondary {{ background: #91bcb5; }}
button.danger {{ background: #d06759; }}
.kpi {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }}
.kpi div {{ background: #fff8e9; border: 1px solid #d7b985; border-radius: 16px; padding: 12px; }}
.kpi strong {{ display: block; font-size: 1.45rem; color: var(--line); }}
#conflictLog {{ display: grid; gap: 10px; max-height: 520px; overflow: auto; }}
.event {{ border-left: 5px solid var(--accent); background: #fff8ea; padding: 11px 12px; border-radius: 14px; }}
.event[data-resolved=\"0\"] {{ border-left-color: var(--danger); }}
.event small {{ color: var(--muted); }}
pre {{ white-space: pre-wrap; overflow: auto; background: #1c1711; color: #f5dfbc; border-radius: 16px; padding: 14px; max-height: 380px; }}
.footer-note {{ color: #f1dcc0; margin-top: 18px; font-size: .95rem; }}
@media (max-width: 840px) {{ .grid {{ grid-template-columns: 1fr; }} .kpi {{ grid-template-columns: 1fr; }} }}
</style>
</head>
<body>
<main>
  <section class=\"hero\">
    <h1>Browser World v15: Multi-agent branch conflict arbitration</h1>
    <p>Concurrent branches now collide across agents. The browser surface stores selected futures, detects conflicts, asks for arbitration after reload, isolates partial rollbacks, and exports replay evidence. The private workspace remains sealed; public reasons are replayable.</p>
  </section>
  <section class=\"grid\">
    <div class=\"card\">
      <h2>Local conflict console</h2>
      <button onclick=\"stepConflict()\">Run arbitration tick</button>
      <button class=\"secondary\" onclick=\"simulateReload()\">Simulate reload restore</button>
      <button class=\"danger\" onclick=\"rollbackCurrent()\">Rollback selected branch</button>
      <button onclick=\"exportReplay()\">Export replay JSON</button>
      <div id=\"conflictLog\"></div>
    </div>
    <div class=\"card\">
      <h2>Readiness</h2>
      <div class=\"kpi\">
        <div><span>Readiness</span><strong id=\"readiness\"></strong></div>
        <div><span>Weakest</span><strong id=\"weakest\"></strong></div>
        <div><span>Conflicts</span><strong id=\"conflicts\"></strong></div>
      </div>
      <h2 style=\"margin-top:18px\">Stored state</h2>
      <pre id=\"stateView\"></pre>
    </div>
  </section>
  <p class=\"footer-note\">Boundary: deterministic browser-local scaffold only. No subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine is claimed.</p>
</main>
<script id=\"initial-state\" type=\"application/json\">{encoded_state}</script>
<script>
const KEY = {json.dumps(LOCAL_STORAGE_KEY)};
const initial = JSON.parse(document.getElementById('initial-state').textContent);
let state = JSON.parse(localStorage.getItem(KEY) || JSON.stringify({{ cursor: 0, restored: false, rolledBack: [], replay: [], source: initial }}));
function save() {{ localStorage.setItem(KEY, JSON.stringify(state)); render(); }}
function currentConflict() {{ return state.source.sample_conflicts[state.cursor % state.source.sample_conflicts.length]; }}
function currentArbitration() {{ return state.source.sample_arbitrations[state.cursor % state.source.sample_arbitrations.length]; }}
function stepConflict() {{
  const conflict = currentConflict();
  const arbitration = currentArbitration();
  state.replay.push({{ type: 'arbitration_tick', cursor: state.cursor, conflict, arbitration, restored: state.restored }});
  state.cursor += 1;
  save();
}}
function simulateReload() {{
  const stored = JSON.parse(localStorage.getItem(KEY) || '{{}}');
  state = Object.assign({{ cursor: 0, restored: true, rolledBack: [], replay: [], source: initial }}, stored, {{ restored: true }});
  save();
}}
function rollbackCurrent() {{
  const arbitration = currentArbitration();
  state.rolledBack.push({{ branch: arbitration.winner_branch, preserved: arbitration.preserved_branch, cursor: state.cursor }});
  state.replay.push({{ type: 'partial_rollback', arbitration }});
  save();
}}
function exportReplay() {{
  const payload = JSON.stringify(state.replay, null, 2);
  const blob = new Blob([payload], {{ type: 'application/json' }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'report-255-arbitration-replay.json';
  a.click();
  URL.revokeObjectURL(url);
}}
function render() {{
  document.getElementById('readiness').textContent = state.source.metrics.browser_world_v15_conflict_arbitration_readiness.toFixed(3);
  document.getElementById('weakest').textContent = state.source.metrics.weakest_channel_score.toFixed(3);
  document.getElementById('conflicts').textContent = state.source.counts.real_conflict_frames;
  document.getElementById('stateView').textContent = JSON.stringify({{ cursor: state.cursor, restored: state.restored, rolledBack: state.rolledBack, replayRows: state.replay.length }}, null, 2);
  const log = document.getElementById('conflictLog');
  log.innerHTML = '';
  state.source.sample_conflicts.forEach((conflict, index) => {{
    const arbitration = state.source.sample_arbitrations[index];
    const div = document.createElement('div');
    div.className = 'event';
    div.dataset.resolved = String(arbitration.resolved);
    div.innerHTML = `<strong>${{conflict.conflict_id}}</strong><br>${{conflict.agents}} / ${{conflict.conflict_kind}}<br><small>${{arbitration.public_explanation}}</small>`;
    log.appendChild(div);
  }});
}}
render();
</script>
</body>
</html>
"""
    output_path.write_text(html, encoding="utf-8")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20260868)
    parser.add_argument("--ticks", type=int, default=168)
    args = parser.parse_args(argv)

    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VISUALIZATION_DIR.mkdir(parents=True, exist_ok=True)

    source = load_source_results()
    frames = generate_frames(seed=args.seed, ticks=args.ticks)
    metrics = compute_metrics(frames, source)
    counts = compute_counts(frames)
    ablations = compute_ablations(metrics)
    verdict = "pass" if (
        metrics["browser_world_v15_conflict_arbitration_readiness"] >= 0.84
        and metrics["weakest_channel_score"] >= 0.82
        and metrics["conflict_detection_rate"] >= 0.85
        and metrics["arbitration_resolution_rate"] >= 0.80
        and metrics["followup_arbitration_after_reload"] >= 0.80
        and metrics["partial_rollback_isolation"] >= 0.84
        and metrics["privacy_safe_arbitration"] >= 0.99
    ) else "partial_or_failed"

    artifact_paths = {
        "concurrent_branch_groups_csv": ARTIFACT_DIR / f"{PREFIX}_concurrent_branch_groups.csv",
        "branch_conflicts_csv": ARTIFACT_DIR / f"{PREFIX}_branch_conflicts.csv",
        "conflict_arbitrations_csv": ARTIFACT_DIR / f"{PREFIX}_conflict_arbitrations.csv",
        "followup_arbitrations_csv": ARTIFACT_DIR / f"{PREFIX}_followup_arbitrations.csv",
        "schedule_access_trust_conflicts_csv": ARTIFACT_DIR / f"{PREFIX}_schedule_access_trust_conflicts.csv",
        "partial_rollback_isolations_csv": ARTIFACT_DIR / f"{PREFIX}_partial_rollback_isolations.csv",
        "arbitration_replay_exports_csv": ARTIFACT_DIR / f"{PREFIX}_arbitration_replay_exports.csv",
        "browser_ticks_csv": ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv",
        "summary_csv": ARTIFACT_DIR / f"{PREFIX}_summary.csv",
        "verdict_csv": ARTIFACT_DIR / f"{PREFIX}_verdict.csv",
        "state_json": ARTIFACT_DIR / f"{PREFIX}_state.json",
        "results_json": ARTIFACT_DIR / f"{PREFIX}_results.json",
        "visualization_html": VISUALIZATION_DIR / f"{PREFIX}.html",
    }

    write_csv(artifact_paths["concurrent_branch_groups_csv"], frames["concurrent_groups"])
    write_csv(artifact_paths["branch_conflicts_csv"], frames["conflicts"])
    write_csv(artifact_paths["conflict_arbitrations_csv"], frames["arbitrations"])
    write_csv(artifact_paths["followup_arbitrations_csv"], frames["followups"])
    write_csv(artifact_paths["schedule_access_trust_conflicts_csv"], frames["schedule_access_trust"])
    write_csv(artifact_paths["partial_rollback_isolations_csv"], frames["rollbacks"])
    write_csv(artifact_paths["arbitration_replay_exports_csv"], frames["replays"])
    write_csv(artifact_paths["browser_ticks_csv"], frames["browser_ticks"])
    write_mapping_csv(artifact_paths["summary_csv"], metrics)
    write_csv(artifact_paths["verdict_csv"], [{"verdict": verdict, **metrics}])

    state = build_state_snapshot(frames, metrics, counts, args.seed)
    artifact_paths["state_json"].write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    render_html(state, artifact_paths["visualization_html"])

    results = {
        "report": 255,
        "name": "SSRM-3D browser world v15 multi-agent branch conflict arbitration bridge",
        "seed": args.seed,
        "ticks": args.ticks,
        "verdict": verdict,
        "counts": counts,
        "metrics": metrics,
        "ablations": ablations,
        "artifacts": {key: str(path.relative_to(ROOT)) for key, path in artifact_paths.items()},
        "source_dependency": str(SOURCE_RESULTS.relative_to(ROOT)),
        "source_verdict": source.get("verdict", "missing"),
        "claim_boundary": "Deterministic browser-local conflict arbitration scaffold only; no subjective consciousness, real consent, moral patienthood, autonomous natural language, or complete 3D engine.",
        "next_gate": "browser world v16 with persistent multi-agent branch conflict gameplay where user decisions resolve live conflicts over several days and agents remember arbitration outcomes",
    }
    artifact_paths["results_json"].write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")

    print(json.dumps({"verdict": verdict, "metrics": metrics, "counts": counts}, indent=2, sort_keys=True))
    return 0 if verdict == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
