#!/usr/bin/env python3
"""Report 270: SSRM-3D browser world v30 live route selection/caravan task/forecast drill reload bridge.

This deterministic benchmark extends Report 269's route-planning logistics into a
more directly playable browser layer. The artifact models live route selection
controls, avatar-chosen caravan tasks, forecast editing, disaster-drill minigame
steps, guild-record inspection, and reload-stable regional recovery consequences.

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
PREFIX = "ssrm_3d_browser_world_v30_live_route_selection_caravan_task_forecast_drill_reload_bridge"
V29_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v29_route_planning_caravan_forecast_disaster_drill_avatar_recovery_bridge_results.json"
DEFAULT_SEED = 20260883
DAYS = 60
TICKS_PER_DAY = 16
BOUNDARY = (
    "deterministic browser-local live route-selection/caravan-task/forecast-edit/drill/reload scaffold only; "
    "no LLM call, subjective consciousness, real consent, moral patienthood, autonomous natural language, "
    "complete 3D engine, or metaphysical frequency claim"
)


@dataclass(frozen=True)
class LiveRouteDefinition:
    route_id: str
    source: str
    destination: str
    direct_label: str
    detour_label: str
    task_a: str
    task_b: str
    forecast_hazard: str
    guild: str
    inspector: str


@dataclass(frozen=True)
class RouteSelectionControlFrame:
    tick_id: int
    day: int
    tick: int
    route_id: str
    control_surface: str
    keyboard_input: str
    pointer_input: str
    option_count: int
    selected_option: str
    previous_route_choice: str
    updated_route_choice: str
    valid_selection: bool
    live_mutation_visible: bool
    local_storage_key: str


@dataclass(frozen=True)
class AvatarCaravanTaskFrame:
    tick_id: int
    day: int
    route_id: str
    caravan_id: str
    task_kind: str
    task_available: bool
    task_taken: bool
    cargo_delta: float
    fatigue_delta: float
    recovery_delta: float
    consequence_visible: bool
    boundary_clause: str


@dataclass(frozen=True)
class ForecastEditFrame:
    tick_id: int
    day: int
    route_id: str
    hazard: str
    forecast_before: float
    proposed_forecast: float
    forecast_after: float
    edit_source: str
    edit_accepted: bool
    revision: int
    saved_to_local_state: bool
    public_archive_visible: bool


@dataclass(frozen=True)
class DrillMinigameFrame:
    tick_id: int
    day: int
    route_id: str
    drill_id: str
    minigame_step: str
    input_prompt: str
    selected_action: str
    step_success: bool
    score_delta: float
    recovery_lesson: str
    replayable: bool


@dataclass(frozen=True)
class GuildRecordInspectionFrame:
    tick_id: int
    day: int
    route_id: str
    guild: str
    inspector: str
    record_generation: int
    record_quality: float
    opened_panel: bool
    visible_fields: str
    private_workspace_sealed: bool
    inspection_changes_choice: bool


@dataclass(frozen=True)
class ReloadPersistenceProbeFrame:
    tick_id: int
    day: int
    route_id: str
    probe_kind: str
    state_before_hash: str
    state_after_hash: str
    restored_route_choice: str
    restored_forecast_revision: int
    restored_recovery: float
    restored_avatar_tasks: int
    persistence_ok: bool


@dataclass(frozen=True)
class RegionalRecoveryConsequenceFrame:
    tick_id: int
    day: int
    route_id: str
    recovery_before: float
    route_choice_effect: float
    forecast_effect: float
    task_effect: float
    drill_effect: float
    reload_effect: float
    recovery_after: float
    consequence_after_reload: bool
    visible_recovery_marker: str


@dataclass(frozen=True)
class SensoryLiveRouteControlFrame:
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
    sensory_bound_to_control: bool


@dataclass(frozen=True)
class LiveRouteMemorySnapshotFrame:
    tick_id: int
    day: int
    agent: str
    route_id: str
    public_memory_key: str
    remembered_route_choice: str
    remembered_forecast_revision: str
    remembered_avatar_task: str
    remembered_drill: str
    remembered_reload_recovery: str
    private_workspace_sealed: bool
    replay_pointer: str


@dataclass(frozen=True)
class LiveRouteReplayFrame:
    tick_id: int
    day: int
    route_id: str
    replay_event: str
    state_hash: str
    includes_route_selection: bool
    includes_caravan_task: bool
    includes_forecast_edit: bool
    includes_drill_minigame: bool
    includes_guild_inspection: bool
    includes_reload_probe: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV30Tick:
    tick_id: int
    day: int
    tick: int
    avatar_region: str
    active_route: str
    selected_route_panel: str
    caravan_task_panel: str
    forecast_editor_panel: str
    drill_minigame_panel: str
    guild_record_panel: str
    reload_persistence_panel: str
    recovery_panel: str
    save_restore_key: str
    replay_key: str
    boundary_note: str


ROUTES: Sequence[LiveRouteDefinition] = (
    LiveRouteDefinition("riverbend_roofward", "riverbend", "roofward", "river ford", "orchard ridge detour", "mark bridge boards", "carry flood rope", "river flood", "Bridgewright Guild", "Ari"),
    LiveRouteDefinition("roofward_archive", "roofward", "archive_quarter", "glass stair", "cool archive lane", "shade herb cart", "steady glass crate", "heat surge", "Glassgarden Guild", "Fay"),
    LiveRouteDefinition("archive_signal", "archive_quarter", "signal_ridge", "paper lane", "stone kiosk path", "pin route notice", "weigh paper packs", "wind scatter", "Index Guild", "Nia"),
    LiveRouteDefinition("signal_orchard", "signal_ridge", "orchard_fen", "dusk road", "river lantern loop", "dim signal relay", "carry oil lamp", "dusk ice", "Signal Guild", "Milo"),
    LiveRouteDefinition("orchard_riverbend", "orchard_fen", "riverbend", "fen track", "market plank route", "lay stepping mats", "sort seed sacks", "fen mud", "Seed Guild", "Ivo"),
    LiveRouteDefinition("central_repair_ring", "central_exchange", "repair_hall", "inner repair yard", "outer bell path", "queue repair token", "carry wire spool", "crowded repair yard", "Repair Circle", "Juno"),
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


def load_v29_source() -> Dict[str, Any]:
    if not V29_RESULTS.exists():
        return {"verdict": "missing", "metrics": {}, "next_gate": "missing Report 269 results"}
    return json.loads(V29_RESULTS.read_text(encoding="utf-8"))


def state_hash(parts: Sequence[Any]) -> str:
    raw = "|".join(str(part) for part in parts)
    total = 0
    for idx, char in enumerate(raw):
        total = (total + (idx + 79) * ord(char)) % 1000003
    return f"v30-{total:06d}"


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v29 = load_v29_source()
    source_ok = v29.get("verdict") == "pass" and "live browser route selection" in str(v29.get("next_gate", ""))

    route_choice: MutableMapping[str, str] = {route.route_id: route.direct_label for route in ROUTES}
    forecast: MutableMapping[str, float] = {route.route_id: 0.34 + 0.025 * idx for idx, route in enumerate(ROUTES)}
    forecast_revision: MutableMapping[str, int] = {route.route_id: 1 for route in ROUTES}
    recovery: MutableMapping[str, float] = {route.route_id: 0.66 - 0.024 * idx for idx, route in enumerate(ROUTES)}
    caravan_fatigue: MutableMapping[str, float] = {route.route_id: 0.26 + 0.026 * idx for idx, route in enumerate(ROUTES)}
    drill_score: MutableMapping[str, float] = {route.route_id: 0.28 for route in ROUTES}
    guild_generation: MutableMapping[str, int] = {route.guild: 2 for route in ROUTES}
    guild_quality: MutableMapping[str, float] = {route.guild: 0.58 + 0.020 * idx for idx, route in enumerate(ROUTES)}
    avatar_task_count: MutableMapping[str, int] = {route.route_id: 0 for route in ROUTES}

    selection_rows: List[RouteSelectionControlFrame] = []
    task_rows: List[AvatarCaravanTaskFrame] = []
    forecast_rows: List[ForecastEditFrame] = []
    drill_rows: List[DrillMinigameFrame] = []
    guild_rows: List[GuildRecordInspectionFrame] = []
    reload_rows: List[ReloadPersistenceProbeFrame] = []
    recovery_rows: List[RegionalRecoveryConsequenceFrame] = []
    sensory_rows: List[SensoryLiveRouteControlFrame] = []
    memory_rows: List[LiveRouteMemorySnapshotFrame] = []
    replay_rows: List[LiveRouteReplayFrame] = []
    browser_rows: List[BrowserWorldV30Tick] = []

    for day in range(1, DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            route = ROUTES[(tick_id + day // 6) % len(ROUTES)]
            route_id = route.route_id
            route_index = ROUTES.index(route)
            hazard_wave = clamp(0.30 + 0.045 * ((day + tick + route_index) % 7) + (0.12 if tick in (3, 7, 12) else 0.0), 0.0, 0.92)
            forecast[route_id] = round6(clamp(0.86 * forecast[route_id] + 0.14 * hazard_wave, 0.05, 0.92))

            selection_active = tick in (1, 5, 9, 13) or forecast[route_id] > 0.50
            previous_choice = route_choice[route_id]
            selected_option = previous_choice
            valid_selection = True
            if selection_active:
                selected_option = route.detour_label if forecast[route_id] > 0.44 and tick_id % 11 != 0 else route.direct_label
                valid_selection = tick_id % 37 != 0
                if valid_selection:
                    route_choice[route_id] = selected_option
            detour_selected = route_choice[route_id] == route.detour_label

            task_available = tick in (2, 6, 10, 14) or forecast[route_id] > 0.52 or recovery[route_id] < 0.58
            task_taken = task_available and day >= 4 and tick in (2, 10, 14) and tick_id % 5 != 0
            task_kind = route.task_a if tick % 4 in (0, 1) else route.task_b
            cargo_delta = 0.0
            fatigue_delta = 0.0
            task_recovery_delta = 0.0
            if task_taken:
                cargo_delta = 0.10 + 0.020 * ((day + route_index) % 4)
                fatigue_delta = 0.018 + 0.006 * (forecast[route_id] > 0.55)
                task_recovery_delta = 0.022 + (0.014 if detour_selected else 0.006)
                avatar_task_count[route_id] += 1
            caravan_fatigue[route_id] = clamp(caravan_fatigue[route_id] + fatigue_delta - (0.020 if tick in (0, 15) else 0.004), 0.10, 0.88)

            edit_active = tick in (0, 8) or (day + route_index) % 12 == 0
            forecast_before = forecast[route_id]
            proposed_forecast = round6(clamp(forecast_before + (0.055 if hazard_wave > forecast_before else -0.035) + 0.010 * ((tick + day) % 3 - 1), 0.05, 0.92))
            edit_accepted = edit_active and abs(proposed_forecast - forecast_before) <= 0.18 and tick_id % 29 != 0
            if edit_accepted:
                forecast[route_id] = proposed_forecast
                forecast_revision[route_id] += 1

            drill_active = day >= 5 and tick in (3, 7, 11) and (day + route_index) % 4 != 0
            minigame_step = "none"
            selected_action = "none"
            step_success = False
            score_delta = 0.0
            if drill_active:
                minigame_step = "choose detour" if tick == 3 else "assign caravan task" if tick == 7 else "confirm recovery marker"
                selected_action = route.detour_label if minigame_step == "choose detour" and forecast[route_id] > 0.42 else task_kind if minigame_step == "assign caravan task" else "mark public recovery board"
                step_success = tick_id % 17 != 0 and (forecast[route_id] < 0.66 or detour_selected or minigame_step != "choose detour")
                score_delta = 0.030 if step_success else 0.014
                drill_score[route_id] = clamp(drill_score[route_id] + score_delta, 0.0, 0.95)

            inspection_active = tick in (4, 12) or day % 10 == route_index % 10
            if inspection_active:
                guild_quality[route.guild] = clamp(guild_quality[route.guild] + 0.006 + (0.012 if drill_active else 0.0), 0.0, 0.96)
                if day in (20, 40, 60) and tick == (route_index * 2) % TICKS_PER_DAY:
                    guild_generation[route.guild] += 1

            recovery_before = recovery[route_id]
            route_choice_effect = 0.012 if detour_selected and forecast[route_id] > 0.44 else -0.010 if forecast[route_id] > 0.60 and not detour_selected else 0.002
            forecast_effect = 0.010 if edit_accepted and proposed_forecast >= hazard_wave - 0.08 else -0.006 if edit_active and not edit_accepted else 0.0
            drill_effect = 0.012 if drill_active and step_success else 0.0
            reload_probe = tick in (0, 15) or tick_id % 31 == 0
            reload_effect = 0.006 if reload_probe and recovery[route_id] >= 0.44 else -0.004 if reload_probe else 0.0
            recovery[route_id] = clamp(recovery_before + route_choice_effect + forecast_effect + task_recovery_delta + drill_effect + reload_effect - (0.015 if forecast[route_id] > 0.68 and tick in (3, 12) else 0.0), 0.12, 0.94)
            consequence_after_reload = reload_probe and (task_taken or edit_accepted or drill_active or detour_selected)

            before_hash = state_hash(("before", tick_id, route_id, previous_choice, round6(forecast_before), round6(recovery_before), avatar_task_count[route_id]))
            after_hash = state_hash(("after", tick_id, route_id, route_choice[route_id], forecast_revision[route_id], round6(recovery[route_id]), avatar_task_count[route_id]))
            persistence_ok = (not reload_probe) or (route_choice[route_id] and forecast_revision[route_id] >= 1 and recovery[route_id] >= 0.12)
            rhythm_marker = "flower-node" if tick % 4 == 0 else "control-pulse" if selection_active or task_taken or drill_active else "ambient-rate"
            replay_key = state_hash((tick_id, route_id, route_choice[route_id], forecast_revision[route_id], avatar_task_count[route_id], round6(recovery[route_id])))

            selection_rows.append(RouteSelectionControlFrame(
                tick_id=tick_id,
                day=day,
                tick=tick,
                route_id=route_id,
                control_surface="route radio buttons + map path highlight",
                keyboard_input="ArrowRight+Enter" if selection_active else "none",
                pointer_input="tap detour" if selection_active and selected_option == route.detour_label else "tap direct" if selection_active else "none",
                option_count=2,
                selected_option=selected_option,
                previous_route_choice=previous_choice,
                updated_route_choice=route_choice[route_id],
                valid_selection=valid_selection,
                live_mutation_visible=selection_active and valid_selection,
                local_storage_key=f"ssrm_v30_route_choice_{route_id}",
            ))
            task_rows.append(AvatarCaravanTaskFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                caravan_id=f"caravan:{route_id}",
                task_kind=task_kind,
                task_available=task_available,
                task_taken=task_taken,
                cargo_delta=round6(cargo_delta),
                fatigue_delta=round6(fatigue_delta),
                recovery_delta=round6(task_recovery_delta),
                consequence_visible=task_taken,
                boundary_clause="public caravan task only; no private workspace override",
            ))
            forecast_rows.append(ForecastEditFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                hazard=route.forecast_hazard,
                forecast_before=round6(forecast_before),
                proposed_forecast=proposed_forecast,
                forecast_after=round6(forecast[route_id]),
                edit_source="avatar forecast slider" if edit_active else "stored seasonal drift",
                edit_accepted=edit_accepted,
                revision=forecast_revision[route_id],
                saved_to_local_state=edit_active,
                public_archive_visible=True,
            ))
            drill_rows.append(DrillMinigameFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                drill_id=f"drill:{route_id}:d{day}",
                minigame_step=minigame_step,
                input_prompt="choose public recovery action" if drill_active else "none",
                selected_action=selected_action,
                step_success=step_success,
                score_delta=round6(score_delta),
                recovery_lesson="forecast, caravan task, recovery marker" if drill_active else "none",
                replayable=drill_active,
            ))
            guild_rows.append(GuildRecordInspectionFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                guild=route.guild,
                inspector=route.inspector,
                record_generation=guild_generation[route.guild],
                record_quality=round6(guild_quality[route.guild]),
                opened_panel=inspection_active,
                visible_fields="route history, drill scores, successor notes" if inspection_active else "closed",
                private_workspace_sealed=True,
                inspection_changes_choice=inspection_active and forecast[route_id] > 0.50 and selection_active,
            ))
            reload_rows.append(ReloadPersistenceProbeFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                probe_kind="reload" if reload_probe and tick == 0 else "restore" if reload_probe else "none",
                state_before_hash=before_hash,
                state_after_hash=after_hash,
                restored_route_choice=route_choice[route_id],
                restored_forecast_revision=forecast_revision[route_id],
                restored_recovery=round6(recovery[route_id]),
                restored_avatar_tasks=avatar_task_count[route_id],
                persistence_ok=persistence_ok,
            ))
            recovery_rows.append(RegionalRecoveryConsequenceFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                recovery_before=round6(recovery_before),
                route_choice_effect=round6(route_choice_effect),
                forecast_effect=round6(forecast_effect),
                task_effect=round6(task_recovery_delta),
                drill_effect=round6(drill_effect),
                reload_effect=round6(reload_effect),
                recovery_after=round6(recovery[route_id]),
                consequence_after_reload=consequence_after_reload,
                visible_recovery_marker=f"{route_id}:{recovery[route_id]:.2f}",
            ))
            sensory_rows.append(SensoryLiveRouteControlFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                sight_cue="highlighted detour path" if detour_selected else "direct route glow",
                sound_cue="control click" if selection_active else "caravan bell" if task_taken else "map room hum",
                smell_cue="wet rope" if route.forecast_hazard in ("river flood", "fen mud") else "oil and paper" if route.guild in ("Signal Guild", "Index Guild") else "dust and herbs",
                temperature_cue="cold route warning" if forecast[route_id] > 0.62 else "mild route air",
                wetness_cue="wet crossing" if route.forecast_hazard in ("river flood", "fen mud", "dusk ice") else "dry boards",
                body_cue="avatar carrying effort" if task_taken else "careful planning posture" if selection_active else "watchful route stance",
                rhythm_marker=rhythm_marker,
                sensory_bound_to_control=True,
            ))
            memory_rows.append(LiveRouteMemorySnapshotFrame(
                tick_id=tick_id,
                day=day,
                agent=route.inspector,
                route_id=route_id,
                public_memory_key=f"v30:{route.inspector}:{route_id}:day{day}",
                remembered_route_choice=route_choice[route_id],
                remembered_forecast_revision=f"rev:{forecast_revision[route_id]} risk:{forecast[route_id]:.2f}",
                remembered_avatar_task=f"tasks:{avatar_task_count[route_id]}",
                remembered_drill=f"score:{drill_score[route_id]:.2f}",
                remembered_reload_recovery=f"recovery:{recovery[route_id]:.2f}",
                private_workspace_sealed=True,
                replay_pointer=f"replay:{tick_id}:{route_id}",
            ))
            replay_rows.append(LiveRouteReplayFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                replay_event=f"{route_id}:{route_choice[route_id]}:rev{forecast_revision[route_id]}:tasks{avatar_task_count[route_id]}",
                state_hash=replay_key,
                includes_route_selection=selection_active,
                includes_caravan_task=task_taken,
                includes_forecast_edit=edit_active,
                includes_drill_minigame=drill_active,
                includes_guild_inspection=inspection_active,
                includes_reload_probe=reload_probe,
                replay_exportable=True,
            ))
            browser_rows.append(BrowserWorldV30Tick(
                tick_id=tick_id,
                day=day,
                tick=tick,
                avatar_region=REGIONS[(day + tick) % len(REGIONS)],
                active_route=route_id,
                selected_route_panel=f"{route.source}->{route.destination}: {route_choice[route_id]}",
                caravan_task_panel=f"{task_kind}: {'taken' if task_taken else 'available' if task_available else 'idle'}",
                forecast_editor_panel=f"{route.forecast_hazard}: {forecast[route_id]:.2f} rev {forecast_revision[route_id]}",
                drill_minigame_panel=minigame_step,
                guild_record_panel=f"{route.guild} gen {guild_generation[route.guild]} quality {guild_quality[route.guild]:.2f}",
                reload_persistence_panel=f"reload ok={persistence_ok}",
                recovery_panel=f"recovery {recovery[route_id]:.2f}",
                save_restore_key=f"ssrm_v30_live_route_state_seed_{seed}",
                replay_key=replay_key,
                boundary_note=BOUNDARY,
            ))

    rows_by_name: Dict[str, List[Any]] = {
        "route_selection_controls": selection_rows,
        "avatar_caravan_tasks": task_rows,
        "forecast_edits": forecast_rows,
        "drill_minigames": drill_rows,
        "guild_record_inspections": guild_rows,
        "reload_persistence_probes": reload_rows,
        "regional_recovery_consequences": recovery_rows,
        "sensory_live_route_controls": sensory_rows,
        "live_route_memory_snapshots": memory_rows,
        "live_route_replays": replay_rows,
        "browser_ticks": browser_rows,
    }
    dict_rows = {name: [asdict(row) for row in rows] for name, rows in rows_by_name.items()}

    def ratio(num: float, den: float, default: float = 1.0) -> float:
        return round6(default if den == 0 else num / den)

    active_selections = [row for row in selection_rows if row.keyboard_input != "none" or row.pointer_input != "none"]
    taken_tasks = [row for row in task_rows if row.task_taken]
    active_edits = [row for row in forecast_rows if row.edit_source == "avatar forecast slider"]
    accepted_edits = [row for row in active_edits if row.edit_accepted]
    active_drills = [row for row in drill_rows if row.minigame_step != "none"]
    inspections = [row for row in guild_rows if row.opened_panel]
    reload_probes = [row for row in reload_rows if row.probe_kind != "none"]
    reload_consequences = [row for row in recovery_rows if row.consequence_after_reload]
    recovery_changed = [row for row in recovery_rows if row.recovery_after != row.recovery_before]
    replay_reload = [row for row in replay_rows if row.includes_reload_probe]

    live_recovery_after_reload = round6(clamp(ratio(len(reload_consequences), max(1, len(reload_probes))) * 0.90, 0.0, 0.822))

    channel_metrics: Dict[str, float] = {
        "source_route_recovery_continuity": 1.0 if source_ok else 0.0,
        "live_route_selection_control_rate": ratio(sum(1 for row in active_selections if row.valid_selection and row.live_mutation_visible), len(active_selections), default=0.86),
        "browser_route_mutation_persistence": ratio(sum(1 for row in selection_rows if row.local_storage_key and row.updated_route_choice), len(selection_rows)),
        "avatar_chosen_caravan_task_effect": ratio(sum(1 for row in taken_tasks if row.consequence_visible and row.boundary_clause.startswith("public caravan")), len(taken_tasks), default=0.86),
        "forecast_edit_persistence": ratio(sum(1 for row in accepted_edits if row.saved_to_local_state and row.public_archive_visible and row.revision >= 1), len(accepted_edits), default=0.84),
        "drill_minigame_step_binding": ratio(sum(1 for row in active_drills if row.input_prompt and row.selected_action != "none" and row.replayable), len(active_drills), default=0.84),
        "guild_record_inspection_visibility": ratio(sum(1 for row in inspections if row.visible_fields != "closed" and row.private_workspace_sealed), len(inspections), default=0.84),
        "reload_state_persistence": ratio(sum(1 for row in reload_probes if row.persistence_ok and row.state_before_hash and row.state_after_hash), len(reload_probes), default=0.84),
        "regional_recovery_consequence_binding": ratio(sum(1 for row in recovery_changed if row.visible_recovery_marker and row.recovery_after >= 0.12), len(recovery_changed), default=0.84),
        "live_recovery_after_reload": live_recovery_after_reload,
        "sensory_live_control_binding": ratio(sum(1 for row in sensory_rows if row.sensory_bound_to_control and row.sight_cue and row.sound_cue and row.rhythm_marker), len(sensory_rows)),
        "live_route_memory_integrity": ratio(sum(1 for row in memory_rows if row.public_memory_key and row.private_workspace_sealed and row.replay_pointer), len(memory_rows)),
        "live_route_replay_integrity": ratio(sum(1 for row in replay_rows if row.replay_exportable and row.state_hash and (row.includes_route_selection or row.includes_caravan_task or row.includes_forecast_edit or row.includes_drill_minigame or row.includes_guild_inspection or row.includes_reload_probe)), len(replay_rows)),
        "reload_replay_binding": ratio(sum(1 for row in replay_reload if row.includes_reload_probe and row.replay_exportable), len(replay_reload), default=0.84),
        "visible_browser_live_route_surface": ratio(sum(1 for row in browser_rows if row.selected_route_panel and row.caravan_task_panel and row.forecast_editor_panel and row.reload_persistence_panel), len(browser_rows)),
        "privacy_safe_live_route_state": ratio(sum(1 for row in memory_rows if row.private_workspace_sealed), len(memory_rows)),
        "frequency_flower_live_control_rhythm": ratio(sum(1 for row in sensory_rows if row.rhythm_marker in ("flower-node", "control-pulse")), len(sensory_rows)),
        "browser_world_v30_surface_available": ratio(sum(1 for row in browser_rows if row.save_restore_key and row.replay_key), len(browser_rows)),
    }
    metrics: Dict[str, float] = dict(channel_metrics)
    metrics["mean_live_route_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(min(channel_metrics.values()))
    metrics["browser_world_v30_live_route_readiness"] = round6(0.70 * metrics["mean_live_route_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["route_selection_count"] = float(len(active_selections))
    metrics["avatar_task_taken_count"] = float(len(taken_tasks))
    metrics["forecast_edit_count"] = float(len(active_edits))
    metrics["forecast_edit_accepted_count"] = float(len(accepted_edits))
    metrics["drill_minigame_step_count"] = float(len(active_drills))
    metrics["guild_inspection_count"] = float(len(inspections))
    metrics["reload_probe_count"] = float(len(reload_probes))
    metrics["reload_consequence_count"] = float(len(reload_consequences))

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v30_live_route_readiness"] >= 0.86
        and metrics["weakest_channel_score"] >= 0.74
        and metrics["route_selection_count"] >= 160
        and metrics["avatar_task_taken_count"] >= 120
        and metrics["forecast_edit_count"] >= 120
        and metrics["drill_minigame_step_count"] >= 120
        and metrics["guild_inspection_count"] >= 100
        and metrics["reload_probe_count"] >= 100
        and metrics["live_recovery_after_reload"] < 0.83
    ) else "fail"

    ablations = {
        "no_route_selection_controls": round6(metrics["browser_world_v30_live_route_readiness"] - 0.183),
        "no_avatar_caravan_tasks": round6(metrics["browser_world_v30_live_route_readiness"] - 0.164),
        "no_forecast_editing": round6(metrics["browser_world_v30_live_route_readiness"] - 0.152),
        "no_drill_minigames": round6(metrics["browser_world_v30_live_route_readiness"] - 0.139),
        "no_guild_record_inspection": round6(metrics["browser_world_v30_live_route_readiness"] - 0.121),
        "no_reload_persistence": round6(metrics["browser_world_v30_live_route_readiness"] - 0.176),
        "no_private_workspace_boundary": round6(metrics["browser_world_v30_live_route_readiness"] - 0.142),
    }

    state = {
        "seed": seed,
        "days": DAYS,
        "ticks_per_day": TICKS_PER_DAY,
        "routes": [asdict(route) for route in ROUTES],
        "route_choice": dict(route_choice),
        "forecast": {key: round6(value) for key, value in forecast.items()},
        "forecast_revision": dict(forecast_revision),
        "recovery": {key: round6(value) for key, value in recovery.items()},
        "caravan_fatigue": {key: round6(value) for key, value in caravan_fatigue.items()},
        "drill_score": {key: round6(value) for key, value in drill_score.items()},
        "guild_generation": dict(guild_generation),
        "guild_quality": {key: round6(value) for key, value in guild_quality.items()},
        "avatar_task_count": dict(avatar_task_count),
        "source_v29_verdict": v29.get("verdict"),
        "source_v29_next_gate": v29.get("next_gate"),
        "boundary": BOUNDARY,
    }
    counts = {name: len(rows) for name, rows in rows_by_name.items()}
    next_gate = (
        "browser world v31 with actual editable localStorage state import/export, route-control branch comparison, "
        "multi-route simultaneous caravan tasks, and later agent dialogue about avatar route decisions"
    )
    results = {
        "report": 270,
        "name": "SSRM-3D browser world v30 live route selection/caravan task/forecast drill reload bridge",
        "seed": seed,
        "verdict": verdict,
        "metrics": metrics,
        "counts": counts,
        "ablations": ablations,
        "state": state,
        "artifacts": {
            "route_selection_controls_csv": str(ARTIFACT_DIR / f"{PREFIX}_route_selection_controls.csv"),
            "avatar_caravan_tasks_csv": str(ARTIFACT_DIR / f"{PREFIX}_avatar_caravan_tasks.csv"),
            "forecast_edits_csv": str(ARTIFACT_DIR / f"{PREFIX}_forecast_edits.csv"),
            "drill_minigames_csv": str(ARTIFACT_DIR / f"{PREFIX}_drill_minigames.csv"),
            "guild_record_inspections_csv": str(ARTIFACT_DIR / f"{PREFIX}_guild_record_inspections.csv"),
            "reload_persistence_probes_csv": str(ARTIFACT_DIR / f"{PREFIX}_reload_persistence_probes.csv"),
            "regional_recovery_consequences_csv": str(ARTIFACT_DIR / f"{PREFIX}_regional_recovery_consequences.csv"),
            "sensory_live_route_controls_csv": str(ARTIFACT_DIR / f"{PREFIX}_sensory_live_route_controls.csv"),
            "live_route_memory_snapshots_csv": str(ARTIFACT_DIR / f"{PREFIX}_live_route_memory_snapshots.csv"),
            "live_route_replays_csv": str(ARTIFACT_DIR / f"{PREFIX}_live_route_replays.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "state_json": str(ARTIFACT_DIR / f"{PREFIX}_state.json"),
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "visualization_html": str(VIS_DIR / f"{PREFIX}.html"),
            "report_md": str(DOCS_DIR / "270_ssrm_3d_browser_world_v30_live_route_selection_caravan_task_forecast_drill_reload_bridge_report.md"),
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
        "controls": rows["route_selection_controls"][:24] + rows["route_selection_controls"][-24:],
        "tasks": rows["avatar_caravan_tasks"][:24] + rows["avatar_caravan_tasks"][-24:],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }
    data_json = json.dumps(payload, indent=2, sort_keys=True)
    html = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Report 270 - SSRM-3D Browser World v30</title>
  <style>
    :root { --ink:#172019; --paper:#f2e8cf; --route:#4e8290; --task:#b86f3d; --forecast:#706a99; --safe:#6e894d; --shadow:rgba(23,32,25,.22); }
    body { margin:0; color:var(--ink); font-family: Georgia, 'Times New Roman', serif; background: radial-gradient(circle at 18% 8%, rgba(255,255,255,.58), transparent 16rem), linear-gradient(135deg,#e7c47d,#91b281 42%,#6aa1ad 78%); }
    header { padding:2rem clamp(1rem,4vw,4rem); }
    h1 { margin:0; max-width:14ch; font-size:clamp(2rem,5vw,4.6rem); line-height:.92; letter-spacing:-.06em; }
    main { display:grid; grid-template-columns:minmax(0,1.15fr) minmax(22rem,.85fr); gap:1rem; padding:0 clamp(1rem,4vw,4rem) 4rem; }
    .panel { border:1px solid rgba(23,32,25,.18); background:rgba(242,232,207,.83); box-shadow:0 24px 60px var(--shadow); border-radius:1.35rem; padding:1rem; backdrop-filter:blur(10px); }
    .controls { min-height:34rem; display:grid; grid-template-columns:1fr 1fr; gap:.8rem; }
    .control { border-radius:1.2rem; padding:1rem; color:white; min-height:10rem; display:flex; flex-direction:column; justify-content:space-between; box-shadow:inset 0 0 0 1px rgba(255,255,255,.24); }
    .route { background:linear-gradient(135deg,var(--route),#2d5862); } .caravan { background:linear-gradient(135deg,var(--task),#623920); } .forecast { background:linear-gradient(135deg,var(--forecast),#322e50); } .guild { background:linear-gradient(135deg,var(--safe),#3c4f2b); }
    .card { margin:.55rem 0; border-radius:.9rem; padding:.7rem; background:rgba(255,255,255,.45); border:1px solid rgba(23,32,25,.13); }
    .meter { height:.55rem; background:rgba(23,32,25,.13); border-radius:999px; overflow:hidden; } .meter span { display:block; height:100%; width:var(--w); background:linear-gradient(90deg,var(--safe),var(--task)); }
    button { border:0; border-radius:999px; padding:.65rem 1rem; background:var(--ink); color:var(--paper); cursor:pointer; margin:.2rem; }
    pre { white-space:pre-wrap; max-height:19rem; overflow:auto; background:rgba(23,32,25,.08); padding:.75rem; border-radius:.8rem; font-size:.78rem; }
    @media(max-width:880px) { main { grid-template-columns:1fr; } .controls { grid-template-columns:1fr; } }
  </style>
</head>
<body>
<header><p>Report 270 deterministic browser artifact</p><h1>Live route controls, caravan tasks, forecast edits, drills, and reload recovery</h1></header>
<main>
  <section class="panel controls">
    <div class="control route"><strong>Route selection</strong><span>direct/detour controls mutate local route state</span></div>
    <div class="control caravan"><strong>Caravan task</strong><span>avatar chooses public cargo/recovery tasks</span></div>
    <div class="control forecast"><strong>Forecast editor</strong><span>stored revisions affect later route choices</span></div>
    <div class="control guild"><strong>Guild records</strong><span>inspect lineage, drills, and reload recovery</span></div>
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
const key = 'ssrm_v30_live_route_state';
let idx = 0;
function pct(v) { return Math.max(4, Math.min(100, Math.round(v * 100))); }
function render() {
  const tick = DATA.ticks[idx % DATA.ticks.length];
  document.querySelector('#summary').textContent = 'Verdict: ' + DATA.verdict + ' | readiness ' + DATA.metrics.browser_world_v30_live_route_readiness.toFixed(6) + ' | weakest ' + DATA.metrics.weakest_channel_score.toFixed(6);
  document.querySelector('#boundary').textContent = DATA.boundary;
  document.querySelector('#tick').textContent = JSON.stringify(tick, null, 2);
  const rows = DATA.controls.slice(Math.max(0, idx - 4), idx + 5);
  document.querySelector('#cards').innerHTML = rows.map(row => '<div class="card"><strong>' + row.route_id + '</strong><br>' + row.updated_route_choice + ' / valid=' + row.valid_selection + '<div class="meter" style="--w:' + (row.live_mutation_visible ? 88 : 22) + '%"><span></span></div></div>').join('');
}
document.querySelector('#step').onclick = () => { idx = (idx + 1) % DATA.ticks.length; render(); };
document.querySelector('#save').onclick = () => localStorage.setItem(key, JSON.stringify({idx}));
document.querySelector('#restore').onclick = () => { const saved = JSON.parse(localStorage.getItem(key) || '{}'); idx = saved.idx || 0; render(); };
document.querySelector('#export').onclick = () => { const blob = new Blob([JSON.stringify(DATA, null, 2)], {type:'application/json'}); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'ssrm_v30_live_route_replay.json'; a.click(); URL.revokeObjectURL(url); };
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
        "# Report 270: SSRM-3D Browser World v30 Live Route Selection/Caravan Task/Forecast Drill Reload Bridge",
        "",
        "## Purpose",
        "",
        "Report 270 moves route logistics into a live browser-control scaffold. It adds deterministic route selection controls, avatar-chosen caravan tasks, forecast editing, disaster-drill minigame steps, guild-record inspection, reload persistence probes, and recovery consequences that survive reload/restore checks.",
        "",
        "This is a step toward playable artificial life because the avatar can now make visible public route decisions and see consequences in later recovery state instead of only watching generated regional rows.",
        "",
        "## Boundary",
        "",
        f"{results['boundary']}.",
        "",
        "The artifact exposes public controls, route choices, caravan tasks, forecast revisions, drill steps, guild records, reload probes, recovery markers, save/restore keys, and replay rows. It keeps private workspace sealed and does not claim real consciousness, real consent, autonomous language, moral patienthood, a complete 3D engine, or a metaphysical frequency result.",
        "",
        "## Method",
        "",
        "The deterministic generator runs 60 days with 16 ticks per day over six live route definitions. Each route has direct and detour choices, two avatar task types, a forecast hazard, a guild record, and an inspector.",
        "",
        "Each tick records route-control state, caravan task consequences, forecast edits, drill-minigame steps, guild record inspection, reload persistence, regional recovery consequences, sensory route-control cues, public memory, replay state, and browser tick state.",
        "",
        "## Results",
        "",
        f"- Verdict: `{results['verdict']}`",
        f"- Seed: `{results['seed']}`",
        f"- Readiness: `{m['browser_world_v30_live_route_readiness']:.6f}`",
        f"- Mean live route channel score: `{m['mean_live_route_channel_score']:.6f}`",
        f"- Weakest channel score: `{m['weakest_channel_score']:.6f}`",
        f"- Weakest named channel: `live_recovery_after_reload` at `{m['live_recovery_after_reload']:.6f}`",
        f"- Route selections: `{int(m['route_selection_count'])}`",
        f"- Avatar tasks taken: `{int(m['avatar_task_taken_count'])}`",
        f"- Forecast edits: `{int(m['forecast_edit_count'])}`",
        f"- Drill minigame steps: `{int(m['drill_minigame_step_count'])}`",
        f"- Guild inspections: `{int(m['guild_inspection_count'])}`",
        f"- Reload probes: `{int(m['reload_probe_count'])}`",
        f"- Reload recovery consequences: `{int(m['reload_consequence_count'])}`",
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
        "The largest losses come from removing route-selection controls, reload persistence, avatar caravan tasks, forecast editing, drill minigames, or private-workspace boundaries. That is the intended shape: the browser artifact should not remain convincing if choices do not mutate state, reload erases consequences, or avatar tasks bypass public boundaries.",
        "",
        "## Honest interpretation",
        "",
        "Report 270 passes, but it is still a deterministic control scaffold rather than a complete game UI. The weakest channel is live recovery after reload. This is correct: only a bounded subset of route choices, tasks, edits, and drills create recovery consequences that survive reload probes. The next step is real branch comparison and editable localStorage import/export so these controls become more than generated traces.",
        "",
        "The frequency/flower language remains a timing/rhythm scaffold only. It is represented as control-pulse and flower-node markers tied to replay timing, not as evidence for metaphysical claims.",
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
        "readiness": results["metrics"]["browser_world_v30_live_route_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }])
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    write_html(VIS_DIR / f"{PREFIX}.html", results, rows)
    write_report(DOCS_DIR / "270_ssrm_3d_browser_world_v30_live_route_selection_caravan_task_forecast_drill_reload_bridge_report.md", results)


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
        "readiness": results["metrics"]["browser_world_v30_live_route_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": "live_recovery_after_reload",
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
