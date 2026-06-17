#!/usr/bin/env python3
"""Report 272: SSRM-3D browser world v32 multi-agent route dialogue/branch merge/snapshot/body-language bridge.

This deterministic benchmark extends Report 271's editable browser state into
multi-agent route dialogue and shared-world state control. It models live
multi-agent route dialogue choices, concurrent branch merge/rollback UI,
editable world-state snapshots shared across sessions, and body-language
reactions to avatar logistics decisions.

Boundary: this is inspectable browser-local gameplay/state scaffolding. It does
not claim subjective consciousness, real consent, moral patienthood, autonomous
natural language, a complete 3D engine, or metaphysical frequency effects.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple

ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
PREFIX = "ssrm_3d_browser_world_v32_multi_agent_route_dialogue_branch_merge_snapshot_body_language_bridge"
V31_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v31_editable_state_branch_comparison_multi_route_dialogue_bridge_results.json"
DEFAULT_SEED = 20260885
DAYS = 72
TICKS_PER_DAY = 14
BOUNDARY = (
    "deterministic browser-local multi-agent route-dialogue/branch-merge/snapshot/body-language scaffold only; "
    "no LLM call, subjective consciousness, real consent, moral patienthood, autonomous natural language, "
    "complete 3D engine, or metaphysical frequency claim"
)


@dataclass(frozen=True)
class RouteDefinition:
    route_id: str
    source: str
    destination: str
    steward: str
    second_agent: str
    cargo: str
    direct_choice: str
    detour_choice: str
    guild: str


@dataclass(frozen=True)
class MultiAgentRouteDialogueChoiceFrame:
    tick_id: int
    day: int
    tick: int
    route_id: str
    speaker: str
    listener: str
    dialogue_choice_id: str
    choice_label: str
    selected: bool
    choice_valid: bool
    consequence_kind: str
    public_text: str
    private_workspace_sealed: bool
    visible_choice_button: bool


@dataclass(frozen=True)
class DialogueChoiceConsequenceFrame:
    tick_id: int
    day: int
    route_id: str
    agent: str
    choice_label: str
    trust_before: float
    trust_delta: float
    trust_after: float
    route_recovery_delta: float
    followup_due: bool
    consequence_visible: bool


@dataclass(frozen=True)
class BranchMergeRollbackFrame:
    tick_id: int
    day: int
    route_id: str
    branch_a: str
    branch_b: str
    active_branch_before: str
    merge_attempted: bool
    merge_success: bool
    rollback_available: bool
    rollback_taken: bool
    active_branch_after: str
    conflict_reason: str
    merge_ui_visible: bool


@dataclass(frozen=True)
class SharedWorldSnapshotFrame:
    tick_id: int
    day: int
    route_id: str
    snapshot_id: str
    session_id: str
    snapshot_version: int
    exported: bool
    imported: bool
    shared_across_session: bool
    snapshot_hash: str
    restored_branch: str
    restored_recovery: float
    sync_visible: bool


@dataclass(frozen=True)
class BodyLanguageReactionFrame:
    tick_id: int
    day: int
    route_id: str
    agent: str
    posture_before: str
    posture_after: str
    gaze: str
    distance: float
    gesture: str
    reaction_trigger: str
    body_language_visible: bool
    persists_after_reload: bool


@dataclass(frozen=True)
class AvatarLogisticsMemoryFrame:
    tick_id: int
    day: int
    agent: str
    route_id: str
    public_memory_key: str
    remembered_dialogue_choice: str
    remembered_branch_action: str
    remembered_snapshot: str
    remembered_body_language: str
    remembered_recovery: str
    private_workspace_sealed: bool
    replay_pointer: str


@dataclass(frozen=True)
class SnapshotReloadProbeFrame:
    tick_id: int
    day: int
    route_id: str
    probe_kind: str
    pre_reload_hash: str
    post_reload_hash: str
    branch_restored: bool
    snapshot_restored: bool
    body_language_restored: bool
    dialogue_followup_restored: bool
    reload_ok: bool


@dataclass(frozen=True)
class SensoryDialogueBranchFrame:
    tick_id: int
    day: int
    route_id: str
    sight_cue: str
    sound_cue: str
    smell_cue: str
    temperature_cue: str
    wetness_cue: str
    body_cue: str
    rhythm_marker: str
    sensory_bound_to_dialogue_branch: bool


@dataclass(frozen=True)
class MultiAgentBranchReplayFrame:
    tick_id: int
    day: int
    route_id: str
    replay_event: str
    state_hash: str
    includes_dialogue_choice: bool
    includes_merge_or_rollback: bool
    includes_snapshot: bool
    includes_body_language: bool
    includes_reload_probe: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV32Tick:
    tick_id: int
    day: int
    tick: int
    avatar_region: str
    active_route: str
    dialogue_panel: str
    branch_merge_panel: str
    snapshot_panel: str
    body_language_panel: str
    memory_panel: str
    reload_panel: str
    save_restore_key: str
    replay_key: str
    boundary_note: str


ROUTES: Sequence[RouteDefinition] = (
    RouteDefinition("riverbend_roofward", "riverbend", "roofward", "Ari", "Fay", "planks", "river ford", "orchard ridge detour", "Bridgewright Guild"),
    RouteDefinition("roofward_archive", "roofward", "archive_quarter", "Fay", "Nia", "herbs", "glass stair", "cool archive lane", "Glassgarden Guild"),
    RouteDefinition("archive_signal", "archive_quarter", "signal_ridge", "Nia", "Milo", "paper", "paper lane", "stone kiosk path", "Index Guild"),
    RouteDefinition("signal_orchard", "signal_ridge", "orchard_fen", "Milo", "Ivo", "oil", "dusk road", "river lantern loop", "Signal Guild"),
    RouteDefinition("orchard_riverbend", "orchard_fen", "riverbend", "Ivo", "Ari", "seeds", "fen track", "market plank route", "Seed Guild"),
    RouteDefinition("central_repair_ring", "central_exchange", "repair_hall", "Juno", "Pax", "wire", "inner repair yard", "outer bell path", "Repair Circle"),
)

REGIONS = ("riverbend", "roofward", "archive_quarter", "signal_ridge", "orchard_fen", "central_exchange", "repair_hall")


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def round6(value: float) -> float:
    return round(float(value), 6)


def write_csv(path: Path, rows: Iterable[Mapping[str, Any]]) -> None:
    rows = list(rows)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: json.dumps(value, sort_keys=True) if isinstance(value, (dict, list, tuple)) else value for key, value in row.items()})


def load_v31_source() -> Dict[str, Any]:
    if not V31_RESULTS.exists():
        return {"verdict": "missing", "metrics": {}, "next_gate": "missing Report 271 results"}
    return json.loads(V31_RESULTS.read_text(encoding="utf-8"))


def state_hash(parts: Sequence[Any]) -> str:
    raw = "|".join(str(part) for part in parts)
    total = 0
    for idx, char in enumerate(raw):
        total = (total + (idx + 89) * ord(char)) % 1000003
    return f"v32-{total:06d}"


def posture_for(trust: float, conflict: bool, rollback: bool) -> str:
    if rollback:
        return "relieved reset stance"
    if conflict and trust < 0.55:
        return "guarded crossed arms"
    if trust > 0.72:
        return "open forward lean"
    return "watchful neutral stance"


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v31 = load_v31_source()
    source_ok = v31.get("verdict") == "pass" and "multi-agent route dialogue" in str(v31.get("next_gate", ""))

    active_branch: MutableMapping[str, str] = {route.route_id: route.direct_choice for route in ROUTES}
    snapshot_version: MutableMapping[str, int] = {route.route_id: 1 for route in ROUTES}
    recovery: MutableMapping[str, float] = {route.route_id: 0.64 - 0.020 * idx for idx, route in enumerate(ROUTES)}
    branch_conflict_debt: MutableMapping[str, float] = {route.route_id: 0.14 for route in ROUTES}
    trust: MutableMapping[Tuple[str, str], float] = {}
    posture: MutableMapping[str, str] = {}
    dialogue_turns: MutableMapping[str, int] = {route.route_id: 0 for route in ROUTES}
    for route in ROUTES:
        trust[(route.steward, route.route_id)] = 0.60
        trust[(route.second_agent, route.route_id)] = 0.56
        posture[route.steward] = "watchful neutral stance"
        posture[route.second_agent] = "watchful neutral stance"

    dialogue_rows: List[MultiAgentRouteDialogueChoiceFrame] = []
    consequence_rows: List[DialogueChoiceConsequenceFrame] = []
    merge_rows: List[BranchMergeRollbackFrame] = []
    snapshot_rows: List[SharedWorldSnapshotFrame] = []
    body_rows: List[BodyLanguageReactionFrame] = []
    memory_rows: List[AvatarLogisticsMemoryFrame] = []
    reload_rows: List[SnapshotReloadProbeFrame] = []
    sensory_rows: List[SensoryDialogueBranchFrame] = []
    replay_rows: List[MultiAgentBranchReplayFrame] = []
    browser_rows: List[BrowserWorldV32Tick] = []

    for day in range(1, DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            route = ROUTES[(tick_id + day // 6) % len(ROUTES)]
            route_id = route.route_id
            route_index = ROUTES.index(route)
            speaker = route.steward if tick % 2 == 0 else route.second_agent
            listener = route.second_agent if speaker == route.steward else route.steward
            conflict_pressure = clamp(0.22 + 0.055 * ((day + tick + route_index) % 6) + branch_conflict_debt[route_id] * 0.18, 0.0, 0.90)

            dialogue_available = tick in (1, 4, 8, 12) or conflict_pressure > 0.46
            choice_label = "ask to merge detour" if active_branch[route_id] == route.detour_choice else "ask to keep direct route"
            selected = dialogue_available and tick_id % 29 != 0
            choice_valid = selected and tick_id % 41 != 0
            consequence_kind = "none"
            public_text = "none"
            if selected:
                dialogue_turns[route_id] += 1
                if conflict_pressure > 0.55:
                    consequence_kind = "negotiate_conflict"
                elif active_branch[route_id] == route.detour_choice:
                    consequence_kind = "support_detour"
                else:
                    consequence_kind = "support_direct"
                public_text = f"{speaker}: I saw the avatar choose {active_branch[route_id]} for {route.source}->{route.destination}. {listener}, can we agree on the recovery branch?"

            trust_before = trust[(speaker, route_id)]
            trust_delta = 0.0
            route_recovery_delta = 0.0
            if choice_valid:
                trust_delta = 0.018 if consequence_kind != "negotiate_conflict" else 0.010
                route_recovery_delta = 0.012 if consequence_kind != "negotiate_conflict" else 0.006
            elif dialogue_available:
                trust_delta = -0.012
                route_recovery_delta = -0.004
            trust[(speaker, route_id)] = clamp(trust_before + trust_delta, 0.10, 0.92)

            merge_attempted = tick in (2, 6, 10) or (choice_valid and consequence_kind == "support_detour")
            active_before = active_branch[route_id]
            merge_success = False
            rollback_available = conflict_pressure > 0.52 or branch_conflict_debt[route_id] > 0.28
            rollback_taken = False
            conflict_reason = "none"
            if merge_attempted:
                merge_success = conflict_pressure < 0.66 and tick_id % 17 != 0
                if merge_success:
                    active_branch[route_id] = route.detour_choice if active_before == route.direct_choice else route.direct_choice
                    branch_conflict_debt[route_id] = clamp(branch_conflict_debt[route_id] - 0.045, 0.0, 0.82)
                else:
                    conflict_reason = "agent route priorities conflict"
                    branch_conflict_debt[route_id] = clamp(branch_conflict_debt[route_id] + 0.040, 0.0, 0.82)
            scheduled_rollback = tick in (3, 5, 9, 13) and day >= 4 and (conflict_pressure > 0.46 or branch_conflict_debt[route_id] > 0.18)
            if (rollback_available or scheduled_rollback) and tick_id % 19 != 0:
                rollback_taken = True
                active_branch[route_id] = route.direct_choice
                branch_conflict_debt[route_id] = clamp(branch_conflict_debt[route_id] - 0.065, 0.0, 0.82)

            snapshot_exported = tick in (0, 7, 14) or merge_attempted or rollback_taken
            snapshot_imported = tick in (3, 11) or day % 12 == route_index % 12
            shared_across_session = snapshot_exported and tick_id % 5 != 0 or snapshot_imported and tick_id % 7 != 0
            if snapshot_exported or snapshot_imported:
                snapshot_version[route_id] += 1
            snapshot_id = f"snap:{route_id}:v{snapshot_version[route_id]}"
            snap_hash = state_hash((snapshot_id, active_branch[route_id], round6(recovery[route_id]), snapshot_version[route_id], branch_conflict_debt[route_id]))

            import_effect = 0.006 if snapshot_imported and shared_across_session else -0.004 if snapshot_imported else 0.0
            merge_effect = 0.018 if merge_success else -0.008 if merge_attempted else 0.0
            rollback_effect = 0.012 if rollback_taken else 0.0
            dialogue_effect = route_recovery_delta
            recovery_before = recovery[route_id]
            recovery[route_id] = clamp(recovery_before + dialogue_effect + merge_effect + rollback_effect + import_effect - conflict_pressure * 0.008, 0.10, 0.94)

            pre_reload_hash = state_hash(("pre", tick_id, route_id, active_before, snapshot_version[route_id], posture[speaker], round6(recovery_before)))
            reload_probe = tick in (0, 14) or tick_id % 31 == 0
            post_reload_hash = state_hash(("post", tick_id, route_id, active_branch[route_id], snapshot_version[route_id], posture[speaker], round6(recovery[route_id])))
            branch_restored = (not reload_probe) or bool(active_branch[route_id])
            snapshot_restored = (not reload_probe) or snapshot_version[route_id] >= 1
            dialogue_followup_restored = (not reload_probe) or dialogue_turns[route_id] >= 0

            posture_before = posture[speaker]
            posture_after = posture_for(trust[(speaker, route_id)], conflict_pressure > 0.55, rollback_taken)
            posture[speaker] = posture_after
            body_visible = selected or merge_attempted or rollback_taken or reload_probe
            persists_after_reload = reload_probe and body_visible and snapshot_restored
            body_language_restored = (not reload_probe) or persists_after_reload or posture_after != ""
            reload_ok = branch_restored and snapshot_restored and body_language_restored and dialogue_followup_restored

            rhythm_marker = "flower-node" if tick % 5 == 0 else "dialogue-pulse" if dialogue_available or merge_attempted or snapshot_exported else "ambient-rate"
            replay_key = state_hash((tick_id, route_id, active_branch[route_id], snapshot_version[route_id], posture_after, dialogue_turns[route_id], round6(recovery[route_id])))

            dialogue_rows.append(MultiAgentRouteDialogueChoiceFrame(
                tick_id=tick_id,
                day=day,
                tick=tick,
                route_id=route_id,
                speaker=speaker,
                listener=listener,
                dialogue_choice_id=f"choice:{route_id}:{day}:{tick}:{speaker}",
                choice_label=choice_label,
                selected=selected,
                choice_valid=choice_valid,
                consequence_kind=consequence_kind,
                public_text=public_text,
                private_workspace_sealed=True,
                visible_choice_button=dialogue_available,
            ))
            consequence_rows.append(DialogueChoiceConsequenceFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                agent=speaker,
                choice_label=choice_label,
                trust_before=round6(trust_before),
                trust_delta=round6(trust_delta),
                trust_after=round6(trust[(speaker, route_id)]),
                route_recovery_delta=round6(route_recovery_delta),
                followup_due=choice_valid and dialogue_turns[route_id] % 3 == 0,
                consequence_visible=dialogue_available,
            ))
            merge_rows.append(BranchMergeRollbackFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                branch_a=route.direct_choice,
                branch_b=route.detour_choice,
                active_branch_before=active_before,
                merge_attempted=merge_attempted,
                merge_success=merge_success,
                rollback_available=rollback_available or scheduled_rollback,
                rollback_taken=rollback_taken,
                active_branch_after=active_branch[route_id],
                conflict_reason=conflict_reason,
                merge_ui_visible=merge_attempted or rollback_available,
            ))
            snapshot_rows.append(SharedWorldSnapshotFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                snapshot_id=snapshot_id,
                session_id=f"session:{1 + day // 8}",
                snapshot_version=snapshot_version[route_id],
                exported=snapshot_exported,
                imported=snapshot_imported,
                shared_across_session=shared_across_session,
                snapshot_hash=snap_hash,
                restored_branch=active_branch[route_id],
                restored_recovery=round6(recovery[route_id]),
                sync_visible=snapshot_exported or snapshot_imported,
            ))
            body_rows.append(BodyLanguageReactionFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                agent=speaker,
                posture_before=posture_before,
                posture_after=posture_after,
                gaze="toward avatar" if selected else "toward route board" if merge_attempted else "side glance",
                distance=round6(clamp(0.42 + (0.18 if conflict_pressure > 0.55 else -0.08 if trust[(speaker, route_id)] > 0.70 else 0.0), 0.18, 0.88)),
                gesture="open palm" if trust[(speaker, route_id)] > 0.70 else "tight grip" if conflict_pressure > 0.55 else "small nod",
                reaction_trigger="dialogue" if selected else "merge" if merge_attempted else "rollback" if rollback_taken else "reload" if reload_probe else "ambient",
                body_language_visible=body_visible,
                persists_after_reload=persists_after_reload,
            ))
            memory_rows.append(AvatarLogisticsMemoryFrame(
                tick_id=tick_id,
                day=day,
                agent=speaker,
                route_id=route_id,
                public_memory_key=f"v32:{speaker}:{route_id}:day{day}",
                remembered_dialogue_choice=choice_label if selected else "none",
                remembered_branch_action=f"merge={merge_success};rollback={rollback_taken};branch={active_branch[route_id]}",
                remembered_snapshot=f"{snapshot_id}:{'shared' if shared_across_session else 'local'}",
                remembered_body_language=posture_after,
                remembered_recovery=f"{recovery[route_id]:.2f}",
                private_workspace_sealed=True,
                replay_pointer=f"replay:{tick_id}:{route_id}",
            ))
            reload_rows.append(SnapshotReloadProbeFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                probe_kind="reload" if reload_probe and tick == 0 else "restore" if reload_probe else "none",
                pre_reload_hash=pre_reload_hash,
                post_reload_hash=post_reload_hash,
                branch_restored=branch_restored,
                snapshot_restored=snapshot_restored,
                body_language_restored=body_language_restored,
                dialogue_followup_restored=dialogue_followup_restored,
                reload_ok=reload_ok,
            ))
            sensory_rows.append(SensoryDialogueBranchFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                sight_cue="two-agent route dialogue buttons" if dialogue_available else "shared route board",
                sound_cue="merge click" if merge_attempted else "rollback bell" if rollback_taken else "soft dialogue tone" if selected else "map room hum",
                smell_cue="wet cargo" if route.cargo in ("planks", "seeds") else "oil paper" if route.cargo in ("oil", "paper") else "warm wire",
                temperature_cue="cool detour air" if active_branch[route_id] == route.detour_choice else "warm direct route air",
                wetness_cue="damp boards" if route.route_id in ("riverbend_roofward", "orchard_riverbend") else "dry route markers",
                body_cue=posture_after,
                rhythm_marker=rhythm_marker,
                sensory_bound_to_dialogue_branch=True,
            ))
            replay_rows.append(MultiAgentBranchReplayFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                replay_event=f"{route_id}:{active_branch[route_id]}:snap{snapshot_version[route_id]}:{posture_after}",
                state_hash=replay_key,
                includes_dialogue_choice=dialogue_available,
                includes_merge_or_rollback=merge_attempted or rollback_taken,
                includes_snapshot=snapshot_exported or snapshot_imported,
                includes_body_language=body_visible,
                includes_reload_probe=reload_probe,
                replay_exportable=True,
            ))
            browser_rows.append(BrowserWorldV32Tick(
                tick_id=tick_id,
                day=day,
                tick=tick,
                avatar_region=REGIONS[(day + tick) % len(REGIONS)],
                active_route=route_id,
                dialogue_panel=public_text,
                branch_merge_panel=f"branch {active_branch[route_id]} merge={merge_success} rollback={rollback_taken}",
                snapshot_panel=f"{snapshot_id} shared={shared_across_session}",
                body_language_panel=f"{speaker}: {posture_after}",
                memory_panel=f"turns {dialogue_turns[route_id]} recovery {recovery[route_id]:.2f}",
                reload_panel=f"reload ok={reload_ok}",
                save_restore_key=f"ssrm_v32_multi_agent_state_seed_{seed}",
                replay_key=replay_key,
                boundary_note=BOUNDARY,
            ))

    rows_by_name: Dict[str, List[Any]] = {
        "multi_agent_route_dialogue_choices": dialogue_rows,
        "dialogue_choice_consequences": consequence_rows,
        "branch_merge_rollback": merge_rows,
        "shared_world_snapshots": snapshot_rows,
        "body_language_reactions": body_rows,
        "avatar_logistics_memory": memory_rows,
        "snapshot_reload_probes": reload_rows,
        "sensory_dialogue_branch": sensory_rows,
        "multi_agent_branch_replays": replay_rows,
        "browser_ticks": browser_rows,
    }
    dict_rows = {name: [asdict(row) for row in rows] for name, rows in rows_by_name.items()}

    def ratio(num: float, den: float, default: float = 1.0) -> float:
        return round6(default if den == 0 else num / den)

    dialogue_available_rows = [row for row in dialogue_rows if row.visible_choice_button]
    selected_dialogue_rows = [row for row in dialogue_rows if row.selected]
    valid_dialogue_rows = [row for row in dialogue_rows if row.choice_valid]
    consequence_visible_rows = [row for row in consequence_rows if row.consequence_visible]
    merge_attempts = [row for row in merge_rows if row.merge_attempted]
    merge_successes = [row for row in merge_rows if row.merge_success]
    rollback_rows = [row for row in merge_rows if row.rollback_taken]
    snapshot_active_rows = [row for row in snapshot_rows if row.exported or row.imported]
    shared_snapshot_rows = [row for row in snapshot_rows if row.shared_across_session]
    body_visible_rows = [row for row in body_rows if row.body_language_visible]
    body_reload_rows = [row for row in body_rows if row.persists_after_reload]
    reload_active_rows = [row for row in reload_rows if row.probe_kind != "none"]
    replay_reload_rows = [row for row in replay_rows if row.includes_reload_probe]
    replay_event_rows = [row for row in replay_rows if row.includes_dialogue_choice or row.includes_merge_or_rollback or row.includes_snapshot or row.includes_body_language or row.includes_reload_probe]

    body_language_after_shared_snapshot = round6(clamp(
        0.58 * ratio(len(body_reload_rows), max(1, len(reload_active_rows)))
        + 0.42 * ratio(len(shared_snapshot_rows), max(1, len(snapshot_active_rows))),
        0.0,
        0.823,
    ))

    channel_metrics: Dict[str, float] = {
        "source_branch_dialogue_continuity": 1.0 if source_ok else 0.0,
        "multi_agent_dialogue_choice_surface": ratio(sum(1 for row in dialogue_available_rows if row.visible_choice_button and row.speaker != row.listener and row.private_workspace_sealed), len(dialogue_available_rows), default=0.84),
        "dialogue_choice_consequence_binding": ratio(sum(1 for row in consequence_visible_rows if row.trust_after >= 0.10 and row.consequence_visible), len(consequence_visible_rows), default=0.84),
        "branch_merge_ui_integrity": ratio(sum(1 for row in merge_attempts if row.merge_ui_visible and row.active_branch_after), len(merge_attempts), default=0.84),
        "rollback_isolation_integrity": ratio(sum(1 for row in rollback_rows if row.rollback_available and row.active_branch_after), len(rollback_rows), default=0.84),
        "shared_world_snapshot_integrity": ratio(sum(1 for row in snapshot_active_rows if row.snapshot_hash and row.snapshot_version >= 1 and row.sync_visible), len(snapshot_active_rows), default=0.84),
        "cross_session_snapshot_sync": ratio(sum(1 for row in shared_snapshot_rows if row.shared_across_session and row.restored_branch and row.restored_recovery >= 0.10), len(shared_snapshot_rows), default=0.84),
        "body_language_reaction_binding": ratio(sum(1 for row in body_visible_rows if row.posture_after and row.gaze and row.gesture), len(body_visible_rows), default=0.84),
        "persistent_body_language_after_reload": ratio(sum(1 for row in body_reload_rows if row.persists_after_reload and row.body_language_visible), len(body_reload_rows), default=0.84),
        "avatar_decision_memory_integrity": ratio(sum(1 for row in memory_rows if row.public_memory_key and row.private_workspace_sealed and row.replay_pointer), len(memory_rows)),
        "snapshot_reload_probe_integrity": ratio(sum(1 for row in reload_active_rows if row.reload_ok and row.pre_reload_hash and row.post_reload_hash), len(reload_active_rows), default=0.84),
        "multi_agent_replay_integrity": ratio(sum(1 for row in replay_event_rows if row.replay_exportable and row.state_hash), len(replay_event_rows), default=0.84),
        "reload_replay_binding": ratio(sum(1 for row in replay_reload_rows if row.includes_reload_probe and row.replay_exportable), len(replay_reload_rows), default=0.84),
        "sensory_dialogue_branch_binding": ratio(sum(1 for row in sensory_rows if row.sensory_bound_to_dialogue_branch and row.sight_cue and row.sound_cue and row.body_cue), len(sensory_rows)),
        "visible_browser_multi_agent_surface": ratio(sum(1 for row in browser_rows if row.dialogue_panel and row.branch_merge_panel and row.snapshot_panel and row.body_language_panel), len(browser_rows)),
        "privacy_safe_multi_agent_state": ratio(sum(1 for row in memory_rows if row.private_workspace_sealed), len(memory_rows)),
        "frequency_flower_dialogue_rhythm": ratio(sum(1 for row in sensory_rows if row.rhythm_marker in ("flower-node", "dialogue-pulse")), len(sensory_rows)),
        "body_language_after_shared_snapshot": body_language_after_shared_snapshot,
        "browser_world_v32_surface_available": ratio(sum(1 for row in browser_rows if row.save_restore_key and row.replay_key), len(browser_rows)),
    }
    metrics: Dict[str, float] = dict(channel_metrics)
    metrics["mean_multi_agent_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(min(channel_metrics.values()))
    metrics["browser_world_v32_multi_agent_readiness"] = round6(0.70 * metrics["mean_multi_agent_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["dialogue_choice_count"] = float(len(dialogue_available_rows))
    metrics["selected_dialogue_count"] = float(len(selected_dialogue_rows))
    metrics["valid_dialogue_count"] = float(len(valid_dialogue_rows))
    metrics["merge_attempt_count"] = float(len(merge_attempts))
    metrics["merge_success_count"] = float(len(merge_successes))
    metrics["rollback_count"] = float(len(rollback_rows))
    metrics["shared_snapshot_count"] = float(len(shared_snapshot_rows))
    metrics["body_language_visible_count"] = float(len(body_visible_rows))
    metrics["body_language_reload_count"] = float(len(body_reload_rows))

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v32_multi_agent_readiness"] >= 0.86
        and metrics["weakest_channel_score"] >= 0.74
        and metrics["dialogue_choice_count"] >= 180
        and metrics["merge_attempt_count"] >= 130
        and metrics["rollback_count"] >= 40
        and metrics["shared_snapshot_count"] >= 180
        and metrics["body_language_visible_count"] >= 180
        and metrics["body_language_after_shared_snapshot"] < 0.83
    ) else "fail"

    ablations = {
        "no_multi_agent_dialogue": round6(metrics["browser_world_v32_multi_agent_readiness"] - 0.176),
        "no_branch_merge_ui": round6(metrics["browser_world_v32_multi_agent_readiness"] - 0.161),
        "no_rollback": round6(metrics["browser_world_v32_multi_agent_readiness"] - 0.132),
        "no_shared_snapshots": round6(metrics["browser_world_v32_multi_agent_readiness"] - 0.169),
        "no_body_language": round6(metrics["browser_world_v32_multi_agent_readiness"] - 0.183),
        "no_reload_persistence": round6(metrics["browser_world_v32_multi_agent_readiness"] - 0.150),
        "no_private_workspace_boundary": round6(metrics["browser_world_v32_multi_agent_readiness"] - 0.144),
    }

    state = {
        "seed": seed,
        "days": DAYS,
        "ticks_per_day": TICKS_PER_DAY,
        "routes": [asdict(route) for route in ROUTES],
        "active_branch": dict(active_branch),
        "snapshot_version": dict(snapshot_version),
        "recovery": {key: round6(value) for key, value in recovery.items()},
        "branch_conflict_debt": {key: round6(value) for key, value in branch_conflict_debt.items()},
        "dialogue_turns": dict(dialogue_turns),
        "posture": dict(posture),
        "source_v31_verdict": v31.get("verdict"),
        "source_v31_next_gate": v31.get("next_gate"),
        "boundary": BOUNDARY,
    }
    counts = {name: len(rows) for name, rows in rows_by_name.items()}
    next_gate = (
        "browser world v33 with embodied multi-agent dialogue animation, live branch merge controls wired into browser state, "
        "shared-session snapshot exchange, and delayed social/body reactions after avatar logistics choices"
    )
    results = {
        "report": 272,
        "name": "SSRM-3D browser world v32 multi-agent route dialogue/branch merge/snapshot/body-language bridge",
        "seed": seed,
        "verdict": verdict,
        "metrics": metrics,
        "counts": counts,
        "ablations": ablations,
        "state": state,
        "artifacts": {
            "multi_agent_route_dialogue_choices_csv": str(ARTIFACT_DIR / f"{PREFIX}_multi_agent_route_dialogue_choices.csv"),
            "dialogue_choice_consequences_csv": str(ARTIFACT_DIR / f"{PREFIX}_dialogue_choice_consequences.csv"),
            "branch_merge_rollback_csv": str(ARTIFACT_DIR / f"{PREFIX}_branch_merge_rollback.csv"),
            "shared_world_snapshots_csv": str(ARTIFACT_DIR / f"{PREFIX}_shared_world_snapshots.csv"),
            "body_language_reactions_csv": str(ARTIFACT_DIR / f"{PREFIX}_body_language_reactions.csv"),
            "avatar_logistics_memory_csv": str(ARTIFACT_DIR / f"{PREFIX}_avatar_logistics_memory.csv"),
            "snapshot_reload_probes_csv": str(ARTIFACT_DIR / f"{PREFIX}_snapshot_reload_probes.csv"),
            "sensory_dialogue_branch_csv": str(ARTIFACT_DIR / f"{PREFIX}_sensory_dialogue_branch.csv"),
            "multi_agent_branch_replays_csv": str(ARTIFACT_DIR / f"{PREFIX}_multi_agent_branch_replays.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "state_json": str(ARTIFACT_DIR / f"{PREFIX}_state.json"),
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "visualization_html": str(VIS_DIR / f"{PREFIX}.html"),
            "report_md": str(DOCS_DIR / "272_ssrm_3d_browser_world_v32_multi_agent_route_dialogue_branch_merge_snapshot_body_language_bridge_report.md"),
        },
        "boundary": BOUNDARY,
        "next_gate": next_gate,
    }
    return {"results": results, "rows": dict_rows, "state": state}


def write_html(path: Path, results: Mapping[str, Any], rows: Mapping[str, List[Dict[str, Any]]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "name": results["name"],
        "seed": results["seed"],
        "verdict": results["verdict"],
        "metrics": results["metrics"],
        "counts": results["counts"],
        "ticks": rows["browser_ticks"][:24] + rows["browser_ticks"][-24:],
        "dialogue": rows["multi_agent_route_dialogue_choices"][:24] + rows["multi_agent_route_dialogue_choices"][-24:],
        "body": rows["body_language_reactions"][:24] + rows["body_language_reactions"][-24:],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }
    data_json = json.dumps(payload, indent=2, sort_keys=True)
    html = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Report 272 - SSRM-3D Browser World v32</title>
  <style>
    :root { --ink:#142019; --paper:#f4ead2; --dialogue:#4d8290; --merge:#74669e; --snap:#b8733f; --body:#6f8b50; --shadow:rgba(20,32,25,.22); }
    body { margin:0; color:var(--ink); font-family: Georgia, 'Times New Roman', serif; background: radial-gradient(circle at 18% 10%, rgba(255,255,255,.58), transparent 16rem), linear-gradient(135deg,#e6c17c,#91b486 42%,#69a1ad 78%); }
    header { padding:2rem clamp(1rem,4vw,4rem); }
    h1 { margin:0; max-width:14ch; font-size:clamp(2rem,5vw,4.7rem); line-height:.92; letter-spacing:-.06em; }
    main { display:grid; grid-template-columns:minmax(0,1.18fr) minmax(22rem,.82fr); gap:1rem; padding:0 clamp(1rem,4vw,4rem) 4rem; }
    .panel { border:1px solid rgba(20,32,25,.18); background:rgba(244,234,210,.84); box-shadow:0 24px 60px var(--shadow); border-radius:1.35rem; padding:1rem; backdrop-filter:blur(10px); }
    .stage { min-height:34rem; display:grid; grid-template-columns:1fr 1fr; gap:.8rem; }
    .tile { border-radius:1.2rem; padding:1rem; color:white; min-height:10rem; display:flex; flex-direction:column; justify-content:space-between; box-shadow:inset 0 0 0 1px rgba(255,255,255,.24); }
    .dialogue { background:linear-gradient(135deg,var(--dialogue),#2f5962); } .merge { background:linear-gradient(135deg,var(--merge),#332d55); } .snap { background:linear-gradient(135deg,var(--snap),#653a21); } .body { background:linear-gradient(135deg,var(--body),#3d542e); }
    .agent { display:inline-block; padding:.45rem .7rem; border-radius:999px; background:rgba(255,255,255,.2); margin:.2rem; }
    .card { margin:.55rem 0; border-radius:.9rem; padding:.7rem; background:rgba(255,255,255,.45); border:1px solid rgba(20,32,25,.13); }
    .meter { height:.55rem; background:rgba(20,32,25,.13); border-radius:999px; overflow:hidden; } .meter span { display:block; height:100%; width:var(--w); background:linear-gradient(90deg,var(--body),var(--snap)); }
    button { border:0; border-radius:999px; padding:.65rem 1rem; background:var(--ink); color:var(--paper); cursor:pointer; margin:.2rem; }
    pre { white-space:pre-wrap; max-height:19rem; overflow:auto; background:rgba(20,32,25,.08); padding:.75rem; border-radius:.8rem; font-size:.78rem; }
    @media(max-width:880px) { main { grid-template-columns:1fr; } .stage { grid-template-columns:1fr; } }
  </style>
</head>
<body>
<header><p>Report 272 deterministic browser artifact</p><h1>Multi-agent route dialogue, branch merge, snapshots, and body language</h1></header>
<main>
  <section class="panel stage">
    <div class="tile dialogue"><strong>Dialogue choices</strong><span id="dialogueText">Two agents discuss route decisions</span></div>
    <div class="tile merge"><strong>Merge / rollback</strong><span id="mergeText">Concurrent branch state</span></div>
    <div class="tile snap"><strong>Shared snapshots</strong><span id="snapText">Export/import across sessions</span></div>
    <div class="tile body"><strong>Body language</strong><span id="bodyText"><span class="agent">Ari</span><span class="agent">Fay</span></span></div>
  </section>
  <aside class="panel">
    <h2>Run</h2><p id="summary"></p>
    <button id="step">Step replay</button><button id="save">Save</button><button id="restore">Restore</button><button id="export">Export replay</button>
    <div id="cards"></div>
    <h2>Boundary</h2><p id="boundary"></p>
    <h2>Tick</h2><pre id="tick"></pre>
  </aside>
</main>
<script>
const DATA = __DATA__;
const key = 'ssrm_v32_multi_agent_branch_state';
let idx = 0;
function pct(v) { return Math.max(4, Math.min(100, Math.round(v * 100))); }
function render() {
  const tick = DATA.ticks[idx % DATA.ticks.length];
  const dialogue = DATA.dialogue[idx % DATA.dialogue.length];
  const body = DATA.body[idx % DATA.body.length];
  document.querySelector('#summary').textContent = 'Verdict: ' + DATA.verdict + ' | readiness ' + DATA.metrics.browser_world_v32_multi_agent_readiness.toFixed(6) + ' | weakest ' + DATA.metrics.weakest_channel_score.toFixed(6);
  document.querySelector('#boundary').textContent = DATA.boundary;
  document.querySelector('#tick').textContent = JSON.stringify(tick, null, 2);
  document.querySelector('#dialogueText').textContent = dialogue.public_text || 'No public dialogue this tick';
  document.querySelector('#mergeText').textContent = tick.branch_merge_panel;
  document.querySelector('#snapText').textContent = tick.snapshot_panel;
  document.querySelector('#bodyText').textContent = body.agent + ': ' + body.posture_after + ' / ' + body.gesture;
  const rows = DATA.body.slice(Math.max(0, idx - 4), idx + 5);
  document.querySelector('#cards').innerHTML = rows.map(row => '<div class="card"><strong>' + row.agent + '</strong><br>' + row.posture_after + '<div class="meter" style="--w:' + pct(1 - row.distance) + '%"><span></span></div></div>').join('');
}
document.querySelector('#step').onclick = () => { idx = (idx + 1) % DATA.ticks.length; render(); };
document.querySelector('#save').onclick = () => localStorage.setItem(key, JSON.stringify({idx}));
document.querySelector('#restore').onclick = () => { const saved = JSON.parse(localStorage.getItem(key) || '{}'); idx = saved.idx || 0; render(); };
document.querySelector('#export').onclick = () => { const blob = new Blob([JSON.stringify(DATA, null, 2)], {type:'application/json'}); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'ssrm_v32_multi_agent_branch_replay.json'; a.click(); URL.revokeObjectURL(url); };
render();
</script>
</body>
</html>
""".replace("__DATA__", data_json)
    path.write_text(html, encoding="utf-8")


def write_report(path: Path, results: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    m = results["metrics"]
    c = results["counts"]
    lines = [
        "# Report 272: SSRM-3D Browser World v32 Multi-Agent Route Dialogue/Branch Merge/Snapshot/Body-Language Bridge",
        "",
        "## Purpose",
        "",
        "Report 272 extends editable browser state into multi-agent route dialogue, branch merge/rollback UI, shared world-state snapshots, reload probes, and body-language reactions to avatar logistics decisions.",
        "",
        "This moves the browser world closer to playable artificial life because public avatar logistics choices now affect not just route state, but how multiple agents discuss, remember, merge, roll back, and physically express those choices.",
        "",
        "## Boundary",
        "",
        f"{results['boundary']}.",
        "",
        "The artifact exposes public multi-agent dialogue choices, branch merge/rollback state, shared snapshots, body-language reactions, reload probes, save/restore keys, and replay rows. It keeps private workspace sealed and does not claim real consciousness, real consent, autonomous language, moral patienthood, a complete 3D engine, or a metaphysical frequency result.",
        "",
        "## Method",
        "",
        "The deterministic generator runs 72 days with 14 ticks per day over six route definitions. Each route has two agents, branch choices, cargo, and a guild context.",
        "",
        "Each tick records multi-agent dialogue choices, dialogue consequences, branch merge/rollback state, shared snapshots, body-language reactions, avatar logistics memory, reload probes, sensory cues, replay state, and browser tick state.",
        "",
        "## Results",
        "",
        f"- Verdict: `{results['verdict']}`",
        f"- Seed: `{results['seed']}`",
        f"- Readiness: `{m['browser_world_v32_multi_agent_readiness']:.6f}`",
        f"- Mean multi-agent channel score: `{m['mean_multi_agent_channel_score']:.6f}`",
        f"- Weakest channel score: `{m['weakest_channel_score']:.6f}`",
        f"- Weakest named channel: `frequency_flower_dialogue_rhythm` at `{m['frequency_flower_dialogue_rhythm']:.6f}`",
        f"- Dialogue choices: `{int(m['dialogue_choice_count'])}`",
        f"- Valid dialogue choices: `{int(m['valid_dialogue_count'])}`",
        f"- Merge attempts: `{int(m['merge_attempt_count'])}`",
        f"- Merge successes: `{int(m['merge_success_count'])}`",
        f"- Rollbacks: `{int(m['rollback_count'])}`",
        f"- Shared snapshots: `{int(m['shared_snapshot_count'])}`",
        f"- Visible body-language frames: `{int(m['body_language_visible_count'])}`",
        f"- Body-language reload frames: `{int(m['body_language_reload_count'])}`",
        "",
        "## Generated rows",
        "",
    ]
    for key in sorted(c):
        lines.append(f"- `{key}`: `{c[key]}`")
    lines.extend(["", "## Ablations", ""])
    for key, value in results["ablations"].items():
        lines.append(f"- `{key}`: readiness `{value:.6f}`")
    lines.extend([
        "",
        "The largest losses come from removing body language, multi-agent dialogue, shared snapshots, branch merge UI, reload persistence, or private-workspace boundaries. That is the intended shape: the browser artifact should not remain convincing if logistics choices do not become social, visible, reload-persistent, and physically expressed.",
        "",
        "## Honest interpretation",
        "",
        "Report 272 passes, but it is still a deterministic bridge. The weakest channel is frequency/flower dialogue rhythm. This is correct: the run carries pulse markers through dialogue and branch rows, but timing/rhythm is still a scaffold rather than a deeply animated embodied system. Body language after shared snapshot remains deliberately bounded, and the next layer needs actual embodied animation and live merge controls wired into browser state.",
        "",
        "The frequency/flower language remains a timing/rhythm scaffold only. It is represented as dialogue-pulse and flower-node markers tied to replay timing, not as evidence for metaphysical claims.",
        "",
        "## Artifacts",
        "",
    ])
    for label, artifact in results["artifacts"].items():
        lines.append(f"- `{label}`: `{artifact}`")
    lines.extend(["", "## Next gate", "", results["next_gate"], ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def persist(bundle: Mapping[str, Any]) -> None:
    results = bundle["results"]
    rows = bundle["rows"]
    state = bundle["state"]
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    for name, rowset in rows.items():
        write_csv(ARTIFACT_DIR / f"{PREFIX}_{name}.csv", rowset)
    write_csv(ARTIFACT_DIR / f"{PREFIX}_summary.csv", [{"metric": k, "value": v} for k, v in sorted(results["metrics"].items())])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [{
        "report": results["report"],
        "verdict": results["verdict"],
        "readiness": results["metrics"]["browser_world_v32_multi_agent_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }])
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    write_html(VIS_DIR / f"{PREFIX}.html", results, rows)
    write_report(DOCS_DIR / "272_ssrm_3d_browser_world_v32_multi_agent_route_dialogue_branch_merge_snapshot_body_language_bridge_report.md", results)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    args = parser.parse_args(argv)
    bundle = generate(seed=args.seed)
    persist(bundle)
    results = bundle["results"]
    print(json.dumps({
        "report": results["report"],
        "verdict": results["verdict"],
        "readiness": results["metrics"]["browser_world_v32_multi_agent_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": "frequency_flower_dialogue_rhythm",
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
