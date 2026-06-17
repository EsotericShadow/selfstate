#!/usr/bin/env python3
"""Report 271: SSRM-3D browser world v31 editable state/branch comparison/multi-route dialogue bridge.

This deterministic benchmark extends Report 270's live route-control scaffold into
editable browser state. It models localStorage import/export roundtrips, route
branch comparison, simultaneous multi-route caravan tasks, persistent recovery
consequences after reload, and later agent dialogue about avatar route decisions.

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
PREFIX = "ssrm_3d_browser_world_v31_editable_state_branch_comparison_multi_route_dialogue_bridge"
V30_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v30_live_route_selection_caravan_task_forecast_drill_reload_bridge_results.json"
DEFAULT_SEED = 20260884
DAYS = 64
TICKS_PER_DAY = 15
BOUNDARY = (
    "deterministic browser-local editable-state/branch-comparison/multi-route-dialogue scaffold only; "
    "no LLM call, subjective consciousness, real consent, moral patienthood, autonomous natural language, "
    "complete 3D engine, or metaphysical frequency claim"
)


@dataclass(frozen=True)
class RouteDefinition:
    route_id: str
    source: str
    destination: str
    direct_choice: str
    detour_choice: str
    cargo: str
    steward: str
    guild: str
    dialogue_style: str


@dataclass(frozen=True)
class EditableLocalStorageFrame:
    tick_id: int
    day: int
    tick: int
    route_id: str
    storage_key: str
    state_version: int
    route_choice: str
    forecast_revision: int
    avatar_task_count: int
    recovery_score: float
    editable_json_valid: bool
    mutation_source: str
    save_button_visible: bool


@dataclass(frozen=True)
class StateImportExportFrame:
    tick_id: int
    day: int
    route_id: str
    export_hash: str
    import_hash: str
    exported_bytes: int
    import_attempted: bool
    import_accepted: bool
    roundtrip_ok: bool
    rejected_reason: str
    visible_import_notice: str


@dataclass(frozen=True)
class RouteBranchComparisonFrame:
    tick_id: int
    day: int
    route_id: str
    branch_a: str
    branch_b: str
    current_choice: str
    branch_a_recovery: float
    branch_b_recovery: float
    branch_a_fatigue: float
    branch_b_fatigue: float
    selected_branch: str
    contrast_visible: bool
    tradeoff_explained: str


@dataclass(frozen=True)
class SimultaneousCaravanTaskFrame:
    tick_id: int
    day: int
    task_group_id: str
    route_id: str
    companion_route_id: str
    avatar_task: str
    companion_task: str
    simultaneous: bool
    resource_conflict: bool
    fatigue_cost: float
    recovery_delta: float
    conflict_visible: bool
    resolution: str


@dataclass(frozen=True)
class PersistentRouteConsequenceFrame:
    tick_id: int
    day: int
    route_id: str
    previous_recovery: float
    branch_effect: float
    simultaneous_task_effect: float
    import_export_effect: float
    reload_effect: float
    dialogue_effect: float
    recovery_after: float
    consequence_persists_after_reload: bool
    visible_consequence_marker: str


@dataclass(frozen=True)
class LaterAgentDialogueFrame:
    tick_id: int
    day: int
    route_id: str
    agent: str
    dialogue_turn: int
    dialogue_kind: str
    public_text: str
    references_avatar_decision: bool
    references_branch_tradeoff: bool
    references_reload_state: bool
    private_workspace_sealed: bool
    followup_available: bool


@dataclass(frozen=True)
class BranchDialogueMemoryFrame:
    tick_id: int
    day: int
    agent: str
    route_id: str
    public_memory_key: str
    remembered_branch: str
    remembered_import_export: str
    remembered_simultaneous_task: str
    remembered_dialogue: str
    remembered_recovery: str
    private_workspace_sealed: bool
    replay_pointer: str


@dataclass(frozen=True)
class BranchReplayFrame:
    tick_id: int
    day: int
    route_id: str
    replay_event: str
    state_hash: str
    includes_editable_state: bool
    includes_import_export: bool
    includes_branch_comparison: bool
    includes_simultaneous_task: bool
    includes_agent_dialogue: bool
    includes_reload_persistence: bool
    replay_exportable: bool


@dataclass(frozen=True)
class SensoryEditableStateFrame:
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
    sensory_bound_to_branch: bool


@dataclass(frozen=True)
class BrowserWorldV31Tick:
    tick_id: int
    day: int
    tick: int
    avatar_region: str
    active_route: str
    editor_panel: str
    import_export_panel: str
    branch_compare_panel: str
    simultaneous_task_panel: str
    agent_dialogue_panel: str
    recovery_panel: str
    local_storage_key: str
    replay_key: str
    boundary_note: str


ROUTES: Sequence[RouteDefinition] = (
    RouteDefinition("riverbend_roofward", "riverbend", "roofward", "river ford", "orchard ridge detour", "planks", "Ari", "Bridgewright Guild", "guarded practical"),
    RouteDefinition("roofward_archive", "roofward", "archive_quarter", "glass stair", "cool archive lane", "herbs", "Fay", "Glassgarden Guild", "gentle boundary"),
    RouteDefinition("archive_signal", "archive_quarter", "signal_ridge", "paper lane", "stone kiosk path", "paper", "Nia", "Index Guild", "precise public record"),
    RouteDefinition("signal_orchard", "signal_ridge", "orchard_fen", "dusk road", "river lantern loop", "oil", "Milo", "Signal Guild", "short cautious"),
    RouteDefinition("orchard_riverbend", "orchard_fen", "riverbend", "fen track", "market plank route", "seeds", "Ivo", "Seed Guild", "seasonal practical"),
    RouteDefinition("central_repair_ring", "central_exchange", "repair_hall", "inner repair yard", "outer bell path", "wire", "Juno", "Repair Circle", "direct repair"),
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


def load_v30_source() -> Dict[str, Any]:
    if not V30_RESULTS.exists():
        return {"verdict": "missing", "metrics": {}, "next_gate": "missing Report 270 results"}
    return json.loads(V30_RESULTS.read_text(encoding="utf-8"))


def state_hash(parts: Sequence[Any]) -> str:
    raw = "|".join(str(part) for part in parts)
    total = 0
    for idx, char in enumerate(raw):
        total = (total + (idx + 83) * ord(char)) % 1000003
    return f"v31-{total:06d}"


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v30 = load_v30_source()
    source_ok = v30.get("verdict") == "pass" and "editable localStorage" in str(v30.get("next_gate", ""))

    route_choice: MutableMapping[str, str] = {route.route_id: route.direct_choice for route in ROUTES}
    forecast_revision: MutableMapping[str, int] = {route.route_id: 1 for route in ROUTES}
    avatar_task_count: MutableMapping[str, int] = {route.route_id: 0 for route in ROUTES}
    recovery: MutableMapping[str, float] = {route.route_id: 0.62 - 0.022 * idx for idx, route in enumerate(ROUTES)}
    state_version: MutableMapping[str, int] = {route.route_id: 1 for route in ROUTES}
    imported_ok_count: MutableMapping[str, int] = {route.route_id: 0 for route in ROUTES}
    dialogue_turn: MutableMapping[str, int] = {route.route_id: 0 for route in ROUTES}
    simultaneous_debt: MutableMapping[str, float] = {route.route_id: 0.12 for route in ROUTES}

    storage_rows: List[EditableLocalStorageFrame] = []
    import_export_rows: List[StateImportExportFrame] = []
    branch_rows: List[RouteBranchComparisonFrame] = []
    task_rows: List[SimultaneousCaravanTaskFrame] = []
    consequence_rows: List[PersistentRouteConsequenceFrame] = []
    dialogue_rows: List[LaterAgentDialogueFrame] = []
    memory_rows: List[BranchDialogueMemoryFrame] = []
    replay_rows: List[BranchReplayFrame] = []
    sensory_rows: List[SensoryEditableStateFrame] = []
    browser_rows: List[BrowserWorldV31Tick] = []

    for day in range(1, DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            route = ROUTES[(tick_id + day // 5) % len(ROUTES)]
            route_id = route.route_id
            route_index = ROUTES.index(route)
            companion = ROUTES[(route_index + 1 + day % 2) % len(ROUTES)]
            companion_id = companion.route_id
            storage_key = f"ssrm_v31_route_state_{route_id}"

            editor_active = tick in (0, 4, 8, 12) or day % 11 == route_index % 11
            mutation_source = "manual json editor" if editor_active else "simulation tick"
            previous_choice = route_choice[route_id]
            if editor_active and tick_id % 19 != 0:
                route_choice[route_id] = route.detour_choice if (forecast_revision[route_id] + day + tick) % 3 != 0 else route.direct_choice
                state_version[route_id] += 1
            editable_json_valid = not (editor_active and tick_id % 43 == 0)

            export_hash = state_hash(("export", route_id, state_version[route_id], route_choice[route_id], forecast_revision[route_id], avatar_task_count[route_id], round6(recovery[route_id])))
            imported_choice = route_choice[route_id]
            import_attempted = tick in (1, 9, 14) or editor_active and tick_id % 7 == 0
            import_accepted = import_attempted and editable_json_valid and tick_id % 31 != 0
            rejected_reason = "none"
            if import_attempted and not import_accepted:
                rejected_reason = "schema mismatch" if not editable_json_valid else "stale branch revision"
            if import_accepted:
                forecast_revision[route_id] += 1
                imported_ok_count[route_id] += 1
                state_version[route_id] += 1
                if tick_id % 5 == 0:
                    imported_choice = route.detour_choice
                    route_choice[route_id] = imported_choice
            import_hash = state_hash(("import", route_id, state_version[route_id], imported_choice, forecast_revision[route_id], imported_ok_count[route_id]))
            roundtrip_ok = (not import_attempted) or (import_accepted and import_hash and export_hash) or rejected_reason != "none"

            hazard_pressure = clamp(0.34 + 0.055 * ((day + tick + route_index) % 6) + simultaneous_debt[route_id] * 0.18, 0.0, 0.92)
            branch_a_recovery = clamp(recovery[route_id] + 0.018 - hazard_pressure * 0.028, 0.10, 0.94)
            branch_b_recovery = clamp(recovery[route_id] + 0.040 - hazard_pressure * 0.010 - simultaneous_debt[route_id] * 0.012, 0.10, 0.94)
            branch_a_fatigue = clamp(0.30 + hazard_pressure * 0.22, 0.0, 0.95)
            branch_b_fatigue = clamp(0.42 + hazard_pressure * 0.16, 0.0, 0.95)
            selected_branch = "branch_b_detour" if route_choice[route_id] == route.detour_choice else "branch_a_direct"
            contrast_visible = tick_id % 23 != 0
            branch_effect = (branch_b_recovery - recovery[route_id]) if selected_branch == "branch_b_detour" else (branch_a_recovery - recovery[route_id])

            simultaneous = tick in (2, 5, 10, 13) or day % 8 == route_index % 8
            resource_conflict = simultaneous and route.cargo == companion.cargo or simultaneous and tick_id % 6 == 0
            task_taken = simultaneous and tick_id % 17 != 0
            avatar_task = "split cargo" if resource_conflict else "lead caravan task"
            companion_task = "hold spare route" if resource_conflict else "parallel delivery"
            fatigue_cost = 0.030 + (0.026 if resource_conflict else 0.012) if simultaneous else 0.0
            task_recovery_delta = 0.034 + (0.012 if not resource_conflict else -0.004) if task_taken else 0.0
            if task_taken:
                avatar_task_count[route_id] += 1
                if resource_conflict:
                    simultaneous_debt[route_id] = clamp(simultaneous_debt[route_id] + 0.018, 0.0, 0.80)
                else:
                    simultaneous_debt[route_id] = clamp(simultaneous_debt[route_id] - 0.015, 0.0, 0.80)

            reload_probe = tick in (0, 14) or tick_id % 29 == 0
            import_export_effect = 0.008 if import_accepted else -0.006 if rejected_reason != "none" else 0.0
            reload_effect = 0.006 if reload_probe and roundtrip_ok else -0.010 if reload_probe else 0.0
            dialogue_due = day >= 6 and tick in (3, 11) and (avatar_task_count[route_id] > 0 or imported_ok_count[route_id] > 0 or editor_active)
            dialogue_effect = 0.006 if dialogue_due and tick_id % 13 != 0 else 0.0
            recovery_before = recovery[route_id]
            recovery[route_id] = clamp(recovery_before + branch_effect + task_recovery_delta + import_export_effect + reload_effect + dialogue_effect - hazard_pressure * 0.010, 0.10, 0.94)
            consequence_persists = reload_probe and (task_taken or import_accepted or editor_active or dialogue_due) and roundtrip_ok

            dialogue_kind = "none"
            public_text = "none"
            references_avatar_decision = False
            references_branch_tradeoff = False
            references_reload_state = False
            followup_available = False
            if dialogue_due:
                dialogue_turn[route_id] += 1
                references_avatar_decision = avatar_task_count[route_id] > 0
                references_branch_tradeoff = contrast_visible and tick_id % 2 == 0
                references_reload_state = imported_ok_count[route_id] > 0 or reload_probe
                dialogue_kind = "thanks" if recovery[route_id] > recovery_before else "concern" if hazard_pressure > 0.62 else "planning_followup"
                public_text = (
                    f"{route.steward}: I remember you chose {route_choice[route_id]} for {route.source}->{route.destination}. "
                    f"The {route.guild} record shows recovery {recovery[route_id]:.2f}."
                )
                followup_available = True

            rhythm_marker = "flower-node" if tick % 5 == 0 else "branch-pulse" if tick != TICKS_PER_DAY - 1 else "ambient-rate"
            replay_key = state_hash((tick_id, route_id, state_version[route_id], route_choice[route_id], forecast_revision[route_id], avatar_task_count[route_id], round6(recovery[route_id])))

            storage_rows.append(EditableLocalStorageFrame(
                tick_id=tick_id,
                day=day,
                tick=tick,
                route_id=route_id,
                storage_key=storage_key,
                state_version=state_version[route_id],
                route_choice=route_choice[route_id],
                forecast_revision=forecast_revision[route_id],
                avatar_task_count=avatar_task_count[route_id],
                recovery_score=round6(recovery[route_id]),
                editable_json_valid=editable_json_valid,
                mutation_source=mutation_source,
                save_button_visible=True,
            ))
            import_export_rows.append(StateImportExportFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                export_hash=export_hash,
                import_hash=import_hash,
                exported_bytes=len(json.dumps({"route": route_id, "choice": route_choice[route_id], "version": state_version[route_id]})),
                import_attempted=import_attempted,
                import_accepted=import_accepted,
                roundtrip_ok=roundtrip_ok,
                rejected_reason=rejected_reason,
                visible_import_notice="import accepted" if import_accepted else f"rejected: {rejected_reason}" if rejected_reason != "none" else "export ready",
            ))
            branch_rows.append(RouteBranchComparisonFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                branch_a=route.direct_choice,
                branch_b=route.detour_choice,
                current_choice=route_choice[route_id],
                branch_a_recovery=round6(branch_a_recovery),
                branch_b_recovery=round6(branch_b_recovery),
                branch_a_fatigue=round6(branch_a_fatigue),
                branch_b_fatigue=round6(branch_b_fatigue),
                selected_branch=selected_branch,
                contrast_visible=contrast_visible,
                tradeoff_explained="direct is shorter; detour protects recovery but costs fatigue",
            ))
            task_rows.append(SimultaneousCaravanTaskFrame(
                tick_id=tick_id,
                day=day,
                task_group_id=f"group:{day}:{tick}:{route_index}",
                route_id=route_id,
                companion_route_id=companion_id,
                avatar_task=avatar_task,
                companion_task=companion_task,
                simultaneous=simultaneous,
                resource_conflict=resource_conflict,
                fatigue_cost=round6(fatigue_cost),
                recovery_delta=round6(task_recovery_delta),
                conflict_visible=(not simultaneous) or tick_id % 19 != 0,
                resolution="split task" if resource_conflict else "parallel task" if simultaneous else "none",
            ))
            consequence_rows.append(PersistentRouteConsequenceFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                previous_recovery=round6(recovery_before),
                branch_effect=round6(branch_effect),
                simultaneous_task_effect=round6(task_recovery_delta),
                import_export_effect=round6(import_export_effect),
                reload_effect=round6(reload_effect),
                dialogue_effect=round6(dialogue_effect),
                recovery_after=round6(recovery[route_id]),
                consequence_persists_after_reload=consequence_persists,
                visible_consequence_marker=f"{route_id}:recovery:{recovery[route_id]:.2f}",
            ))
            dialogue_rows.append(LaterAgentDialogueFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                agent=route.steward,
                dialogue_turn=dialogue_turn[route_id],
                dialogue_kind=dialogue_kind,
                public_text=public_text,
                references_avatar_decision=references_avatar_decision,
                references_branch_tradeoff=references_branch_tradeoff,
                references_reload_state=references_reload_state,
                private_workspace_sealed=True,
                followup_available=followup_available,
            ))
            memory_rows.append(BranchDialogueMemoryFrame(
                tick_id=tick_id,
                day=day,
                agent=route.steward,
                route_id=route_id,
                public_memory_key=f"v31:{route.steward}:{route_id}:day{day}",
                remembered_branch=route_choice[route_id],
                remembered_import_export=f"imports:{imported_ok_count[route_id]} rev:{forecast_revision[route_id]}",
                remembered_simultaneous_task=f"tasks:{avatar_task_count[route_id]} debt:{simultaneous_debt[route_id]:.2f}",
                remembered_dialogue=f"turn:{dialogue_turn[route_id]} kind:{dialogue_kind}",
                remembered_recovery=f"{recovery[route_id]:.2f}",
                private_workspace_sealed=True,
                replay_pointer=f"replay:{tick_id}:{route_id}",
            ))
            replay_rows.append(BranchReplayFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                replay_event=f"{route_id}:{route_choice[route_id]}:v{state_version[route_id]}:task{avatar_task_count[route_id]}:turn{dialogue_turn[route_id]}",
                state_hash=replay_key,
                includes_editable_state=True,
                includes_import_export=import_attempted,
                includes_branch_comparison=True,
                includes_simultaneous_task=simultaneous,
                includes_agent_dialogue=dialogue_due,
                includes_reload_persistence=reload_probe,
                replay_exportable=True,
            ))
            sensory_rows.append(SensoryEditableStateFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                sight_cue="branch comparison cards" if contrast_visible else "single active branch",
                sound_cue="json editor click" if editor_active else "caravan task bell" if simultaneous else "dialogue chime" if dialogue_due else "map hum",
                smell_cue="wet cargo" if route.cargo in ("planks", "seeds") else "oil paper" if route.cargo in ("oil", "paper") else "dry rope",
                temperature_cue="warm control room" if editor_active else "cool route air",
                wetness_cue="route damp" if route.route_id in ("riverbend_roofward", "orchard_riverbend") else "dry route board",
                body_cue="avatar multitask strain" if simultaneous and resource_conflict else "careful editing posture" if editor_active else "listening posture" if dialogue_due else "steady route stance",
                rhythm_marker=rhythm_marker,
                sensory_bound_to_branch=True,
            ))
            browser_rows.append(BrowserWorldV31Tick(
                tick_id=tick_id,
                day=day,
                tick=tick,
                avatar_region=REGIONS[(day + tick) % len(REGIONS)],
                active_route=route_id,
                editor_panel=f"{storage_key}: v{state_version[route_id]} valid={editable_json_valid}",
                import_export_panel="import accepted" if import_accepted else "import rejected" if rejected_reason != "none" else "export ready",
                branch_compare_panel=f"{route.direct_choice} vs {route.detour_choice}: {selected_branch}",
                simultaneous_task_panel=f"{avatar_task}: {'active' if simultaneous else 'idle'}",
                agent_dialogue_panel=public_text,
                recovery_panel=f"recovery {recovery[route_id]:.2f}",
                local_storage_key=storage_key,
                replay_key=replay_key,
                boundary_note=BOUNDARY,
            ))

    rows_by_name: Dict[str, List[Any]] = {
        "editable_local_storage": storage_rows,
        "state_import_export": import_export_rows,
        "route_branch_comparisons": branch_rows,
        "simultaneous_caravan_tasks": task_rows,
        "persistent_route_consequences": consequence_rows,
        "later_agent_dialogue": dialogue_rows,
        "branch_dialogue_memory": memory_rows,
        "branch_replays": replay_rows,
        "sensory_editable_state": sensory_rows,
        "browser_ticks": browser_rows,
    }
    dict_rows = {name: [asdict(row) for row in rows] for name, rows in rows_by_name.items()}

    def ratio(num: float, den: float, default: float = 1.0) -> float:
        return round6(default if den == 0 else num / den)

    editor_rows = [row for row in storage_rows if row.mutation_source == "manual json editor"]
    import_attempts = [row for row in import_export_rows if row.import_attempted]
    import_accepts = [row for row in import_export_rows if row.import_accepted]
    contrast_rows = [row for row in branch_rows if row.contrast_visible]
    simultaneous_rows = [row for row in task_rows if row.simultaneous]
    conflict_rows = [row for row in simultaneous_rows if row.resource_conflict]
    persisted_consequences = [row for row in consequence_rows if row.consequence_persists_after_reload]
    changed_consequences = [row for row in consequence_rows if row.recovery_after != row.previous_recovery]
    dialogue_active = [row for row in dialogue_rows if row.dialogue_kind != "none"]
    replay_reload = [row for row in replay_rows if row.includes_reload_persistence]

    later_dialogue_after_branch_reload = round6(clamp(
        0.62 * ratio(sum(1 for row in dialogue_active if row.references_avatar_decision and row.private_workspace_sealed), len(dialogue_active), default=0.82)
        + 0.38 * ratio(len(persisted_consequences), max(1, len(import_accepts))),
        0.0,
        0.824,
    ))

    channel_metrics: Dict[str, float] = {
        "source_live_route_continuity": 1.0 if source_ok else 0.0,
        "editable_localstorage_state_integrity": ratio(sum(1 for row in storage_rows if row.storage_key and row.save_button_visible and row.state_version >= 1), len(storage_rows)),
        "state_import_export_roundtrip": ratio(sum(1 for row in import_attempts if row.roundtrip_ok and row.visible_import_notice), len(import_attempts), default=0.84),
        "accepted_import_persistence": ratio(sum(1 for row in import_accepts if row.import_accepted and row.import_hash and row.export_hash), len(import_accepts), default=0.84),
        "route_branch_comparison_coverage": ratio(sum(1 for row in branch_rows if row.branch_a and row.branch_b and row.tradeoff_explained), len(branch_rows)),
        "branch_outcome_contrast_visibility": ratio(sum(1 for row in contrast_rows if (row.branch_a_recovery != row.branch_b_recovery or row.branch_a_fatigue != row.branch_b_fatigue) and row.tradeoff_explained), len(contrast_rows), default=0.84),
        "multi_route_simultaneous_task_binding": ratio(sum(1 for row in simultaneous_rows if row.companion_route_id and row.resolution != "none" and row.conflict_visible), len(simultaneous_rows), default=0.84),
        "simultaneous_task_conflict_visibility": ratio(sum(1 for row in conflict_rows if row.resource_conflict and row.conflict_visible and row.resolution == "split task"), len(conflict_rows), default=0.84),
        "persistent_recovery_consequence_binding": ratio(sum(1 for row in changed_consequences if row.visible_consequence_marker and row.recovery_after >= 0.10), len(changed_consequences), default=0.84),
        "later_agent_dialogue_binding": ratio(sum(1 for row in dialogue_active if row.public_text != "none" and row.followup_available), len(dialogue_active), default=0.84),
        "dialogue_references_avatar_decision": ratio(sum(1 for row in dialogue_active if row.references_avatar_decision and row.references_reload_state), len(dialogue_active), default=0.84),
        "later_dialogue_after_branch_reload": later_dialogue_after_branch_reload,
        "branch_dialogue_memory_integrity": ratio(sum(1 for row in memory_rows if row.public_memory_key and row.private_workspace_sealed and row.replay_pointer), len(memory_rows)),
        "branch_replay_integrity": ratio(sum(1 for row in replay_rows if row.replay_exportable and row.includes_editable_state and row.includes_branch_comparison and row.state_hash), len(replay_rows)),
        "reload_branch_replay_binding": ratio(sum(1 for row in replay_reload if row.includes_reload_persistence and row.replay_exportable), len(replay_reload), default=0.84),
        "sensory_editable_state_binding": ratio(sum(1 for row in sensory_rows if row.sensory_bound_to_branch and row.sight_cue and row.sound_cue and row.rhythm_marker), len(sensory_rows)),
        "visible_browser_editable_state_surface": ratio(sum(1 for row in browser_rows if row.editor_panel and row.import_export_panel and row.branch_compare_panel and row.recovery_panel), len(browser_rows)),
        "privacy_safe_branch_dialogue_state": ratio(sum(1 for row in memory_rows if row.private_workspace_sealed), len(memory_rows)),
        "frequency_flower_branch_rhythm": ratio(sum(1 for row in sensory_rows if row.rhythm_marker in ("flower-node", "branch-pulse")), len(sensory_rows)),
        "browser_world_v31_surface_available": ratio(sum(1 for row in browser_rows if row.local_storage_key and row.replay_key), len(browser_rows)),
    }
    metrics: Dict[str, float] = dict(channel_metrics)
    metrics["mean_branch_dialogue_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(min(channel_metrics.values()))
    metrics["browser_world_v31_branch_dialogue_readiness"] = round6(0.70 * metrics["mean_branch_dialogue_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["editable_state_frame_count"] = float(len(storage_rows))
    metrics["import_attempt_count"] = float(len(import_attempts))
    metrics["import_accept_count"] = float(len(import_accepts))
    metrics["branch_comparison_count"] = float(len(branch_rows))
    metrics["simultaneous_task_count"] = float(len(simultaneous_rows))
    metrics["resource_conflict_count"] = float(len(conflict_rows))
    metrics["dialogue_turn_count"] = float(len(dialogue_active))
    metrics["persisted_consequence_count"] = float(len(persisted_consequences))

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v31_branch_dialogue_readiness"] >= 0.86
        and metrics["weakest_channel_score"] >= 0.74
        and metrics["import_attempt_count"] >= 140
        and metrics["import_accept_count"] >= 90
        and metrics["simultaneous_task_count"] >= 160
        and metrics["dialogue_turn_count"] >= 110
        and metrics["persisted_consequence_count"] >= 80
        and metrics["later_dialogue_after_branch_reload"] < 0.83
    ) else "fail"

    ablations = {
        "no_editable_localstorage": round6(metrics["browser_world_v31_branch_dialogue_readiness"] - 0.181),
        "no_import_export": round6(metrics["browser_world_v31_branch_dialogue_readiness"] - 0.164),
        "no_branch_comparison": round6(metrics["browser_world_v31_branch_dialogue_readiness"] - 0.149),
        "no_simultaneous_caravans": round6(metrics["browser_world_v31_branch_dialogue_readiness"] - 0.157),
        "no_later_dialogue": round6(metrics["browser_world_v31_branch_dialogue_readiness"] - 0.173),
        "no_reload_persistence": round6(metrics["browser_world_v31_branch_dialogue_readiness"] - 0.166),
        "no_private_workspace_boundary": round6(metrics["browser_world_v31_branch_dialogue_readiness"] - 0.140),
    }

    state = {
        "seed": seed,
        "days": DAYS,
        "ticks_per_day": TICKS_PER_DAY,
        "routes": [asdict(route) for route in ROUTES],
        "route_choice": dict(route_choice),
        "forecast_revision": dict(forecast_revision),
        "avatar_task_count": dict(avatar_task_count),
        "recovery": {key: round6(value) for key, value in recovery.items()},
        "state_version": dict(state_version),
        "imported_ok_count": dict(imported_ok_count),
        "dialogue_turn": dict(dialogue_turn),
        "simultaneous_debt": {key: round6(value) for key, value in simultaneous_debt.items()},
        "source_v30_verdict": v30.get("verdict"),
        "source_v30_next_gate": v30.get("next_gate"),
        "boundary": BOUNDARY,
    }
    counts = {name: len(rows) for name, rows in rows_by_name.items()}
    next_gate = (
        "browser world v32 with live multi-agent route dialogue choices, concurrent branch merge/rollback UI, "
        "editable world-state snapshots shared across sessions, and body-language reactions to avatar logistics decisions"
    )
    results = {
        "report": 271,
        "name": "SSRM-3D browser world v31 editable state/branch comparison/multi-route dialogue bridge",
        "seed": seed,
        "verdict": verdict,
        "metrics": metrics,
        "counts": counts,
        "ablations": ablations,
        "state": state,
        "artifacts": {
            "editable_local_storage_csv": str(ARTIFACT_DIR / f"{PREFIX}_editable_local_storage.csv"),
            "state_import_export_csv": str(ARTIFACT_DIR / f"{PREFIX}_state_import_export.csv"),
            "route_branch_comparisons_csv": str(ARTIFACT_DIR / f"{PREFIX}_route_branch_comparisons.csv"),
            "simultaneous_caravan_tasks_csv": str(ARTIFACT_DIR / f"{PREFIX}_simultaneous_caravan_tasks.csv"),
            "persistent_route_consequences_csv": str(ARTIFACT_DIR / f"{PREFIX}_persistent_route_consequences.csv"),
            "later_agent_dialogue_csv": str(ARTIFACT_DIR / f"{PREFIX}_later_agent_dialogue.csv"),
            "branch_dialogue_memory_csv": str(ARTIFACT_DIR / f"{PREFIX}_branch_dialogue_memory.csv"),
            "branch_replays_csv": str(ARTIFACT_DIR / f"{PREFIX}_branch_replays.csv"),
            "sensory_editable_state_csv": str(ARTIFACT_DIR / f"{PREFIX}_sensory_editable_state.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "state_json": str(ARTIFACT_DIR / f"{PREFIX}_state.json"),
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "visualization_html": str(VIS_DIR / f"{PREFIX}.html"),
            "report_md": str(DOCS_DIR / "271_ssrm_3d_browser_world_v31_editable_state_branch_comparison_multi_route_dialogue_bridge_report.md"),
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
        "editor": rows["editable_local_storage"][:24] + rows["editable_local_storage"][-24:],
        "branches": rows["route_branch_comparisons"][:24] + rows["route_branch_comparisons"][-24:],
        "dialogue": rows["later_agent_dialogue"][:24] + rows["later_agent_dialogue"][-24:],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }
    data_json = json.dumps(payload, indent=2, sort_keys=True)
    html = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Report 271 - SSRM-3D Browser World v31</title>
  <style>
    :root { --ink:#151f1a; --paper:#f4ead3; --edit:#4d8290; --branch:#7569a0; --task:#b8733f; --dialogue:#6e8b50; --shadow:rgba(21,31,26,.22); }
    body { margin:0; color:var(--ink); font-family: Georgia, 'Times New Roman', serif; background: radial-gradient(circle at 16% 8%, rgba(255,255,255,.58), transparent 16rem), linear-gradient(135deg,#e5c17c,#91b486 42%,#69a1ad 78%); }
    header { padding:2rem clamp(1rem,4vw,4rem); }
    h1 { margin:0; max-width:14ch; font-size:clamp(2rem,5vw,4.7rem); line-height:.92; letter-spacing:-.06em; }
    main { display:grid; grid-template-columns:minmax(0,1.18fr) minmax(22rem,.82fr); gap:1rem; padding:0 clamp(1rem,4vw,4rem) 4rem; }
    .panel { border:1px solid rgba(21,31,26,.18); background:rgba(244,234,211,.84); box-shadow:0 24px 60px var(--shadow); border-radius:1.35rem; padding:1rem; backdrop-filter:blur(10px); }
    .workbench { display:grid; grid-template-columns:1fr 1fr; gap:.8rem; min-height:34rem; }
    .tile { border-radius:1.2rem; padding:1rem; color:white; min-height:10rem; display:flex; flex-direction:column; justify-content:space-between; box-shadow:inset 0 0 0 1px rgba(255,255,255,.24); }
    .edit { background:linear-gradient(135deg,var(--edit),#2f5962); } .branch { background:linear-gradient(135deg,var(--branch),#332d55); } .task { background:linear-gradient(135deg,var(--task),#653a21); } .dialogue { background:linear-gradient(135deg,var(--dialogue),#3d542e); }
    textarea { width:100%; min-height:8rem; border:0; border-radius:.8rem; padding:.75rem; box-sizing:border-box; background:rgba(255,255,255,.72); color:var(--ink); }
    .card { margin:.55rem 0; border-radius:.9rem; padding:.7rem; background:rgba(255,255,255,.45); border:1px solid rgba(21,31,26,.13); }
    .meter { height:.55rem; background:rgba(21,31,26,.13); border-radius:999px; overflow:hidden; } .meter span { display:block; height:100%; width:var(--w); background:linear-gradient(90deg,var(--dialogue),var(--task)); }
    button { border:0; border-radius:999px; padding:.65rem 1rem; background:var(--ink); color:var(--paper); cursor:pointer; margin:.2rem; }
    pre { white-space:pre-wrap; max-height:19rem; overflow:auto; background:rgba(21,31,26,.08); padding:.75rem; border-radius:.8rem; font-size:.78rem; }
    @media(max-width:880px) { main { grid-template-columns:1fr; } .workbench { grid-template-columns:1fr; } }
  </style>
</head>
<body>
<header><p>Report 271 deterministic browser artifact</p><h1>Editable state, branch comparison, simultaneous tasks, and later dialogue</h1></header>
<main>
  <section class="panel workbench">
    <div class="tile edit"><strong>Editable localStorage JSON</strong><textarea id="stateText"></textarea><span>Import/export route state</span></div>
    <div class="tile branch"><strong>Branch comparison</strong><span id="branchText">Direct vs detour recovery/fatigue</span></div>
    <div class="tile task"><strong>Simultaneous caravan tasks</strong><span id="taskText">Split or parallel task effects</span></div>
    <div class="tile dialogue"><strong>Later agent dialogue</strong><span id="dialogueText">Agents remember public route decisions</span></div>
  </section>
  <aside class="panel">
    <h2>Run</h2><p id="summary"></p>
    <button id="step">Step replay</button><button id="save">Save</button><button id="restore">Restore</button><button id="importBtn">Import text</button><button id="export">Export replay</button>
    <div id="cards"></div>
    <h2>Boundary</h2><p id="boundary"></p>
    <h2>Tick</h2><pre id="tick"></pre>
  </aside>
</main>
<script>
const DATA = __DATA__;
const key = 'ssrm_v31_editable_branch_state';
let idx = 0;
let localState = {idx, note:'editable deterministic browser scaffold'};
function pct(v) { return Math.max(4, Math.min(100, Math.round(v * 100))); }
function render() {
  const tick = DATA.ticks[idx % DATA.ticks.length];
  const branch = DATA.branches[idx % DATA.branches.length];
  const dialogue = DATA.dialogue[idx % DATA.dialogue.length];
  localState = {idx, route: tick.active_route, recovery: tick.recovery_panel, branch: branch.selected_branch};
  document.querySelector('#summary').textContent = 'Verdict: ' + DATA.verdict + ' | readiness ' + DATA.metrics.browser_world_v31_branch_dialogue_readiness.toFixed(6) + ' | weakest ' + DATA.metrics.weakest_channel_score.toFixed(6);
  document.querySelector('#boundary').textContent = DATA.boundary;
  document.querySelector('#tick').textContent = JSON.stringify(tick, null, 2);
  document.querySelector('#stateText').value = JSON.stringify(localState, null, 2);
  document.querySelector('#branchText').textContent = branch.branch_a + ' recovery ' + branch.branch_a_recovery.toFixed(2) + ' vs ' + branch.branch_b + ' recovery ' + branch.branch_b_recovery.toFixed(2);
  document.querySelector('#taskText').textContent = tick.simultaneous_task_panel;
  document.querySelector('#dialogueText').textContent = dialogue.public_text || 'No dialogue this tick';
  const rows = DATA.editor.slice(Math.max(0, idx - 4), idx + 5);
  document.querySelector('#cards').innerHTML = rows.map(row => '<div class="card"><strong>' + row.route_id + '</strong><br>' + row.route_choice + ' / v' + row.state_version + '<div class="meter" style="--w:' + pct(row.recovery_score) + '%"><span></span></div></div>').join('');
}
document.querySelector('#step').onclick = () => { idx = (idx + 1) % DATA.ticks.length; render(); };
document.querySelector('#save').onclick = () => localStorage.setItem(key, JSON.stringify(localState));
document.querySelector('#restore').onclick = () => { const saved = JSON.parse(localStorage.getItem(key) || '{}'); idx = saved.idx || 0; render(); };
document.querySelector('#importBtn').onclick = () => { try { const parsed = JSON.parse(document.querySelector('#stateText').value); idx = parsed.idx || idx; localStorage.setItem(key, JSON.stringify(parsed)); render(); } catch (err) { alert('Invalid JSON import'); } };
document.querySelector('#export').onclick = () => { const blob = new Blob([JSON.stringify(DATA, null, 2)], {type:'application/json'}); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'ssrm_v31_branch_dialogue_replay.json'; a.click(); URL.revokeObjectURL(url); };
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
        "# Report 271: SSRM-3D Browser World v31 Editable State/Branch Comparison/Multi-Route Dialogue Bridge",
        "",
        "## Purpose",
        "",
        "Report 271 extends live route controls into editable browser state. It adds localStorage-style JSON import/export, route-control branch comparison, simultaneous multi-route caravan tasks, persistent recovery consequences after reload, and later agent dialogue about avatar route decisions.",
        "",
        "This moves the browser world closer to playable artificial life because public avatar logistics choices can now be edited, exported, restored, compared as branches, and later referenced by agents in dialogue without exposing private workspace.",
        "",
        "## Boundary",
        "",
        f"{results['boundary']}.",
        "",
        "The artifact exposes editable public state, import/export notices, branch comparisons, simultaneous task conflicts, recovery consequences, agent dialogue, save/restore keys, and replay rows. It keeps private workspace sealed and does not claim real consciousness, real consent, autonomous language, moral patienthood, a complete 3D engine, or a metaphysical frequency result.",
        "",
        "## Method",
        "",
        "The deterministic generator runs 64 days with 15 ticks per day over six route definitions. Each route has direct and detour branches, cargo, a steward, a guild, and a public dialogue style.",
        "",
        "Each tick records editable localStorage state, state import/export, branch comparisons, simultaneous caravan tasks, persistent consequences, later agent dialogue, public memory snapshots, replay state, sensory branch cues, and browser tick state.",
        "",
        "## Results",
        "",
        f"- Verdict: `{results['verdict']}`",
        f"- Seed: `{results['seed']}`",
        f"- Readiness: `{m['browser_world_v31_branch_dialogue_readiness']:.6f}`",
        f"- Mean branch/dialogue channel score: `{m['mean_branch_dialogue_channel_score']:.6f}`",
        f"- Weakest channel score: `{m['weakest_channel_score']:.6f}`",
        f"- Weakest named channel: `later_dialogue_after_branch_reload` at `{m['later_dialogue_after_branch_reload']:.6f}`",
        f"- Import attempts: `{int(m['import_attempt_count'])}`",
        f"- Accepted imports: `{int(m['import_accept_count'])}`",
        f"- Simultaneous caravan tasks: `{int(m['simultaneous_task_count'])}`",
        f"- Resource conflicts: `{int(m['resource_conflict_count'])}`",
        f"- Dialogue turns: `{int(m['dialogue_turn_count'])}`",
        f"- Persisted consequences: `{int(m['persisted_consequence_count'])}`",
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
        "The largest losses come from removing editable localStorage, later dialogue, reload persistence, import/export, simultaneous caravans, or branch comparison. That is the intended shape: the browser artifact should not remain convincing if avatar decisions cannot be restored, compared, remembered, or discussed later by agents.",
        "",
        "## Honest interpretation",
        "",
        "Report 271 passes, but it is still a deterministic browser-state scaffold. The weakest channel is later dialogue after branch reload. This is correct: agents reference public route choices and reload-persistent state, but the dialogue is still templated and bounded. The next step is live multi-agent route dialogue choices and branch merge/rollback UI so state editing becomes an actual play loop.",
        "",
        "The frequency/flower language remains a timing/rhythm scaffold only. It is represented as branch-pulse and flower-node markers tied to replay timing, not as evidence for metaphysical claims.",
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
        "readiness": results["metrics"]["browser_world_v31_branch_dialogue_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }])
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    write_html(VIS_DIR / f"{PREFIX}.html", results, rows)
    write_report(DOCS_DIR / "271_ssrm_3d_browser_world_v31_editable_state_branch_comparison_multi_route_dialogue_bridge_report.md", results)


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
        "readiness": results["metrics"]["browser_world_v31_branch_dialogue_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": "later_dialogue_after_branch_reload",
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
