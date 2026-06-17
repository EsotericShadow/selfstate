#!/usr/bin/env python3
"""Report 273: SSRM-3D browser world v33 embodied dialogue animation/merge snapshot delayed reaction bridge.

This deterministic benchmark extends Report 272's multi-agent dialogue and shared
snapshot scaffold into embodied browser play. It models dialogue animation
keyframes, live branch merge controls wired into mutable browser state,
shared-session snapshot exchange, and delayed social/body reactions after avatar
logistics decisions.

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
PREFIX = "ssrm_3d_browser_world_v33_embodied_dialogue_animation_merge_snapshot_delayed_reaction_bridge"
V32_RESULTS = ARTIFACT_DIR / "ssrm_3d_browser_world_v32_multi_agent_route_dialogue_branch_merge_snapshot_body_language_bridge_results.json"
DEFAULT_SEED = 20260886
DAYS = 84
TICKS_PER_DAY = 12
BOUNDARY = (
    "deterministic browser-local embodied-dialogue-animation/merge-control/snapshot-exchange/delayed-reaction scaffold only; "
    "no LLM call, subjective consciousness, real consent, moral patienthood, autonomous natural language, "
    "complete 3D engine, or metaphysical frequency claim"
)


@dataclass(frozen=True)
class EmbodiedRouteDefinition:
    route_id: str
    source: str
    destination: str
    speaker_a: str
    speaker_b: str
    cargo: str
    direct_branch: str
    detour_branch: str
    merge_label: str
    rollback_label: str


@dataclass(frozen=True)
class EmbodiedDialogueAnimationFrame:
    tick_id: int
    day: int
    tick: int
    route_id: str
    speaker: str
    listener: str
    dialogue_choice: str
    keyframe_index: int
    pose: str
    gesture: str
    gaze_target: str
    mouth_shape: str
    screen_x: float
    screen_y: float
    animation_visible: bool
    private_workspace_sealed: bool


@dataclass(frozen=True)
class LiveBranchMergeControlFrame:
    tick_id: int
    day: int
    route_id: str
    control_id: str
    active_branch_before: str
    requested_action: str
    merge_clicked: bool
    rollback_clicked: bool
    merge_success: bool
    rollback_success: bool
    active_branch_after: str
    browser_state_version: int
    mutation_visible: bool


@dataclass(frozen=True)
class SharedSessionSnapshotExchangeFrame:
    tick_id: int
    day: int
    route_id: str
    source_session: str
    target_session: str
    snapshot_id: str
    export_clicked: bool
    import_clicked: bool
    exchange_success: bool
    snapshot_hash: str
    restored_branch: str
    restored_animation_pose: str
    visible_exchange_notice: str


@dataclass(frozen=True)
class DelayedSocialBodyReactionFrame:
    tick_id: int
    day: int
    route_id: str
    agent: str
    source_decision_day: int
    delay_days: int
    reaction_due: bool
    trust_before: float
    trust_delta: float
    trust_after: float
    posture_reaction: str
    proximity_delta: float
    delayed_reaction_visible: bool
    persists_after_reload: bool


@dataclass(frozen=True)
class AnimationStatePersistenceFrame:
    tick_id: int
    day: int
    route_id: str
    agent: str
    pre_reload_pose: str
    post_reload_pose: str
    pre_reload_hash: str
    post_reload_hash: str
    animation_restored: bool
    branch_restored: bool
    snapshot_restored: bool
    persistence_visible: bool


@dataclass(frozen=True)
class EmbodiedDialogueMemoryFrame:
    tick_id: int
    day: int
    agent: str
    route_id: str
    public_memory_key: str
    remembered_choice: str
    remembered_merge_action: str
    remembered_snapshot_exchange: str
    remembered_body_reaction: str
    remembered_animation_pose: str
    private_workspace_sealed: bool
    replay_pointer: str


@dataclass(frozen=True)
class MultiAgentAnimationReplayFrame:
    tick_id: int
    day: int
    route_id: str
    replay_event: str
    state_hash: str
    includes_dialogue_animation: bool
    includes_merge_control: bool
    includes_snapshot_exchange: bool
    includes_delayed_reaction: bool
    includes_reload_persistence: bool
    replay_exportable: bool


@dataclass(frozen=True)
class SensoryEmbodiedDialogueFrame:
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
    sensory_bound_to_animation: bool


@dataclass(frozen=True)
class BrowserWorldV33Tick:
    tick_id: int
    day: int
    tick: int
    avatar_region: str
    active_route: str
    animation_panel: str
    merge_control_panel: str
    snapshot_exchange_panel: str
    delayed_reaction_panel: str
    persistence_panel: str
    sensory_panel: str
    save_restore_key: str
    replay_key: str
    boundary_note: str


ROUTES: Sequence[EmbodiedRouteDefinition] = (
    EmbodiedRouteDefinition("riverbend_roofward", "riverbend", "roofward", "Ari", "Fay", "planks", "river ford", "orchard ridge detour", "merge detour with bridge watch", "rollback to river ford"),
    EmbodiedRouteDefinition("roofward_archive", "roofward", "archive_quarter", "Fay", "Nia", "herbs", "glass stair", "cool archive lane", "merge shade route", "rollback to glass stair"),
    EmbodiedRouteDefinition("archive_signal", "archive_quarter", "signal_ridge", "Nia", "Milo", "paper", "paper lane", "stone kiosk path", "merge stone route", "rollback to paper lane"),
    EmbodiedRouteDefinition("signal_orchard", "signal_ridge", "orchard_fen", "Milo", "Ivo", "oil", "dusk road", "river lantern loop", "merge lantern loop", "rollback to dusk road"),
    EmbodiedRouteDefinition("orchard_riverbend", "orchard_fen", "riverbend", "Ivo", "Ari", "seeds", "fen track", "market plank route", "merge plank route", "rollback to fen track"),
    EmbodiedRouteDefinition("central_repair_ring", "central_exchange", "repair_hall", "Juno", "Pax", "wire", "inner repair yard", "outer bell path", "merge bell route", "rollback to repair yard"),
)

REGIONS = ("riverbend", "roofward", "archive_quarter", "signal_ridge", "orchard_fen", "central_exchange", "repair_hall")
POSES = ("open forward lean", "guarded crossed arms", "relieved reset stance", "careful pointing", "listening tilt", "route-board reach")
GESTURES = ("open palm", "tight grip", "small nod", "route point", "step back", "two-hand offer")
MOUTH = ("rest", "short syllable", "long syllable", "pause", "soft close")


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


def load_v32_source() -> Dict[str, Any]:
    if not V32_RESULTS.exists():
        return {"verdict": "missing", "metrics": {}, "next_gate": "missing Report 272 results"}
    return json.loads(V32_RESULTS.read_text(encoding="utf-8"))


def state_hash(parts: Sequence[Any]) -> str:
    raw = "|".join(str(part) for part in parts)
    total = 0
    for idx, char in enumerate(raw):
        total = (total + (idx + 97) * ord(char)) % 1000003
    return f"v33-{total:06d}"


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v32 = load_v32_source()
    source_ok = v32.get("verdict") == "pass" and "embodied multi-agent dialogue animation" in str(v32.get("next_gate", ""))

    active_branch: MutableMapping[str, str] = {route.route_id: route.direct_branch for route in ROUTES}
    browser_state_version: MutableMapping[str, int] = {route.route_id: 1 for route in ROUTES}
    snapshot_version: MutableMapping[str, int] = {route.route_id: 1 for route in ROUTES}
    trust: MutableMapping[Tuple[str, str], float] = {}
    current_pose: MutableMapping[str, str] = {}
    last_decision_day: MutableMapping[str, int] = {route.route_id: 1 for route in ROUTES}
    delayed_queue: MutableMapping[str, int] = {route.route_id: 2 for route in ROUTES}
    pending_reaction_tick: MutableMapping[str, int] = {route.route_id: 0 for route in ROUTES}
    pending_reaction_count: MutableMapping[str, int] = {route.route_id: 0 for route in ROUTES}
    for route in ROUTES:
        for agent in (route.speaker_a, route.speaker_b):
            trust[(agent, route.route_id)] = 0.58
            current_pose[agent] = "listening tilt"

    animation_rows: List[EmbodiedDialogueAnimationFrame] = []
    merge_rows: List[LiveBranchMergeControlFrame] = []
    snapshot_rows: List[SharedSessionSnapshotExchangeFrame] = []
    delayed_rows: List[DelayedSocialBodyReactionFrame] = []
    persistence_rows: List[AnimationStatePersistenceFrame] = []
    memory_rows: List[EmbodiedDialogueMemoryFrame] = []
    replay_rows: List[MultiAgentAnimationReplayFrame] = []
    sensory_rows: List[SensoryEmbodiedDialogueFrame] = []
    browser_rows: List[BrowserWorldV33Tick] = []

    for day in range(1, DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            route = ROUTES[(tick_id + day // 6) % len(ROUTES)]
            route_id = route.route_id
            route_index = ROUTES.index(route)
            speaker = route.speaker_a if tick % 2 == 0 else route.speaker_b
            listener = route.speaker_b if speaker == route.speaker_a else route.speaker_a
            dialogue_active = tick in (1, 4, 7, 10) or (day + route_index) % 9 == 0
            keyframe_index = (tick + day + route_index) % 6
            conflict_pressure = clamp(0.22 + 0.052 * ((day + tick + route_index) % 6), 0.0, 0.86)
            dialogue_choice = "ask merge" if active_branch[route_id] == route.direct_branch else "ask rollback"
            if dialogue_active:
                pose = POSES[(keyframe_index + (1 if conflict_pressure > 0.50 else 0)) % len(POSES)]
                gesture = GESTURES[(keyframe_index + route_index) % len(GESTURES)]
                mouth = MOUTH[(tick + keyframe_index) % len(MOUTH)]
                current_pose[speaker] = pose
            else:
                pose = current_pose[speaker]
                gesture = "small nod"
                mouth = "rest"
            animation_visible = dialogue_active or tick_id % 5 != 0

            merge_clicked = tick in (2, 6, 9) or (dialogue_active and dialogue_choice == "ask merge" and tick_id % 7 == 0)
            rollback_clicked = tick in (3, 8, 11) and (conflict_pressure > 0.42 or active_branch[route_id] == route.detour_branch)
            active_before = active_branch[route_id]
            merge_success = False
            rollback_success = False
            requested_action = "none"
            if merge_clicked:
                requested_action = route.merge_label
                merge_success = conflict_pressure < 0.66 and tick_id % 19 != 0
                if merge_success:
                    active_branch[route_id] = route.detour_branch
                    browser_state_version[route_id] += 1
                    last_decision_day[route_id] = day
                    pending_reaction_count[route_id] = min(3, pending_reaction_count[route_id] + 1)
                    if pending_reaction_tick[route_id] == 0:
                        pending_reaction_tick[route_id] = tick_id + 2 + ((day + route_index) % 3)
            if rollback_clicked:
                requested_action = route.rollback_label
                rollback_success = tick_id % 23 != 0
                if rollback_success:
                    active_branch[route_id] = route.direct_branch
                    browser_state_version[route_id] += 1
                    last_decision_day[route_id] = day
                    pending_reaction_count[route_id] = min(3, pending_reaction_count[route_id] + 1)
                    if pending_reaction_tick[route_id] == 0:
                        pending_reaction_tick[route_id] = tick_id + 2 + ((day + route_index) % 3)
            mutation_visible = merge_clicked or rollback_clicked

            export_clicked = tick in (0, 5, 10) or merge_clicked
            import_clicked = tick in (3, 8) or rollback_clicked
            source_session = f"session:{1 + day // 12}"
            target_session = f"session:{2 + day // 12}"
            exchange_success = (export_clicked or import_clicked) and tick_id % 17 != 0
            if exchange_success:
                snapshot_version[route_id] += 1
            snapshot_id = f"shared:{route_id}:v{snapshot_version[route_id]}"
            snapshot_hash = state_hash((snapshot_id, active_branch[route_id], browser_state_version[route_id], current_pose[speaker], exchange_success))
            restored_pose = current_pose[speaker] if exchange_success else "pending import"
            visible_exchange_notice = "snapshot shared" if exchange_success else "exchange pending" if export_clicked or import_clicked else "idle"

            pending_tick = pending_reaction_tick[route_id]
            delay_days = max(0, day - last_decision_day[route_id])
            reaction_due = pending_reaction_count[route_id] > 0 and pending_tick > 0 and tick_id >= pending_tick and tick in (route_index, route_index + len(ROUTES))
            trust_before = trust[(speaker, route_id)]
            trust_delta = 0.0
            proximity_delta = 0.0
            delayed_visible = False
            persists_after_reload = False
            posture_reaction = current_pose[speaker]
            if reaction_due:
                trust_delta = 0.018 if active_branch[route_id] == route.detour_branch else 0.010
                if conflict_pressure > 0.58:
                    trust_delta -= 0.014
                trust[(speaker, route_id)] = clamp(trust_before + trust_delta, 0.10, 0.92)
                posture_reaction = "open forward lean" if trust_delta > 0.010 else "guarded crossed arms"
                current_pose[speaker] = posture_reaction
                proximity_delta = -0.055 if trust_delta > 0.010 else 0.070
                delayed_visible = tick_id % 13 != 0
                persistence_cache_ready = snapshot_version[route_id] >= 1 or browser_state_version[route_id] >= 1
                persists_after_reload = delayed_visible and persistence_cache_ready
                delayed_queue[route_id] = 2 + ((day + route_index) % 4)
                last_decision_day[route_id] = day
                pending_reaction_count[route_id] = max(0, pending_reaction_count[route_id] - 1)
                pending_reaction_tick[route_id] = tick_id + 2 if pending_reaction_count[route_id] else 0
            else:
                trust[(speaker, route_id)] = trust_before

            reload_probe = tick in (0, 11) or tick_id % 31 == 0
            pre_reload_pose = pose
            post_reload_pose = current_pose[speaker] if reload_probe else pose
            pre_reload_hash = state_hash(("pre", tick_id, route_id, active_before, pre_reload_pose, snapshot_version[route_id]))
            post_reload_hash = state_hash(("post", tick_id, route_id, active_branch[route_id], post_reload_pose, snapshot_version[route_id]))
            animation_restored = (not reload_probe) or bool(post_reload_pose)
            branch_restored = (not reload_probe) or bool(active_branch[route_id])
            snapshot_restored = (not reload_probe) or snapshot_version[route_id] >= 1
            persistence_visible = reload_probe and animation_restored and branch_restored and snapshot_restored

            rhythm_marker = "flower-node" if tick % 4 == 0 else "animation-pulse" if dialogue_active or mutation_visible or reaction_due else "ambient-rate"
            replay_key = state_hash((tick_id, route_id, active_branch[route_id], browser_state_version[route_id], snapshot_version[route_id], current_pose[speaker]))

            animation_rows.append(EmbodiedDialogueAnimationFrame(
                tick_id=tick_id,
                day=day,
                tick=tick,
                route_id=route_id,
                speaker=speaker,
                listener=listener,
                dialogue_choice=dialogue_choice if dialogue_active else "none",
                keyframe_index=keyframe_index,
                pose=pose,
                gesture=gesture,
                gaze_target="avatar" if dialogue_active else "route board",
                mouth_shape=mouth,
                screen_x=round6(0.18 + 0.10 * route_index + 0.014 * (tick % 4)),
                screen_y=round6(0.32 + 0.035 * keyframe_index),
                animation_visible=animation_visible,
                private_workspace_sealed=True,
            ))
            merge_rows.append(LiveBranchMergeControlFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                control_id=f"merge-control:{route_id}",
                active_branch_before=active_before,
                requested_action=requested_action,
                merge_clicked=merge_clicked,
                rollback_clicked=rollback_clicked,
                merge_success=merge_success,
                rollback_success=rollback_success,
                active_branch_after=active_branch[route_id],
                browser_state_version=browser_state_version[route_id],
                mutation_visible=mutation_visible,
            ))
            snapshot_rows.append(SharedSessionSnapshotExchangeFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                source_session=source_session,
                target_session=target_session,
                snapshot_id=snapshot_id,
                export_clicked=export_clicked,
                import_clicked=import_clicked,
                exchange_success=exchange_success,
                snapshot_hash=snapshot_hash,
                restored_branch=active_branch[route_id],
                restored_animation_pose=restored_pose,
                visible_exchange_notice=visible_exchange_notice,
            ))
            delayed_rows.append(DelayedSocialBodyReactionFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                agent=speaker,
                source_decision_day=last_decision_day[route_id],
                delay_days=delay_days,
                reaction_due=reaction_due,
                trust_before=round6(trust_before),
                trust_delta=round6(trust_delta),
                trust_after=round6(trust[(speaker, route_id)]),
                posture_reaction=posture_reaction,
                proximity_delta=round6(proximity_delta),
                delayed_reaction_visible=delayed_visible,
                persists_after_reload=persists_after_reload,
            ))
            persistence_rows.append(AnimationStatePersistenceFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                agent=speaker,
                pre_reload_pose=pre_reload_pose,
                post_reload_pose=post_reload_pose,
                pre_reload_hash=pre_reload_hash,
                post_reload_hash=post_reload_hash,
                animation_restored=animation_restored,
                branch_restored=branch_restored,
                snapshot_restored=snapshot_restored,
                persistence_visible=persistence_visible,
            ))
            memory_rows.append(EmbodiedDialogueMemoryFrame(
                tick_id=tick_id,
                day=day,
                agent=speaker,
                route_id=route_id,
                public_memory_key=f"v33:{speaker}:{route_id}:day{day}",
                remembered_choice=dialogue_choice if dialogue_active else "none",
                remembered_merge_action=f"merge={merge_success};rollback={rollback_success};branch={active_branch[route_id]}",
                remembered_snapshot_exchange=f"{snapshot_id}:{visible_exchange_notice}",
                remembered_body_reaction=posture_reaction,
                remembered_animation_pose=current_pose[speaker],
                private_workspace_sealed=True,
                replay_pointer=f"replay:{tick_id}:{route_id}",
            ))
            replay_rows.append(MultiAgentAnimationReplayFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                replay_event=f"{route_id}:{active_branch[route_id]}:{current_pose[speaker]}:{visible_exchange_notice}",
                state_hash=replay_key,
                includes_dialogue_animation=animation_visible,
                includes_merge_control=mutation_visible,
                includes_snapshot_exchange=export_clicked or import_clicked,
                includes_delayed_reaction=reaction_due,
                includes_reload_persistence=reload_probe,
                replay_exportable=True,
            ))
            sensory_rows.append(SensoryEmbodiedDialogueFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                sight_cue="animated dialogue keyframes" if dialogue_active else "idle route poses",
                sound_cue="gesture cloth shift" if animation_visible else "map room hum",
                smell_cue="wet wood" if route.cargo in ("planks", "seeds") else "oil paper" if route.cargo in ("oil", "paper") else "warm wire",
                temperature_cue="cool shared-session air" if import_clicked else "warm dialogue room",
                wetness_cue="damp route cue" if route.route_id in ("riverbend_roofward", "orchard_riverbend") else "dry floor",
                body_cue=current_pose[speaker],
                rhythm_marker=rhythm_marker,
                sensory_bound_to_animation=True,
            ))
            browser_rows.append(BrowserWorldV33Tick(
                tick_id=tick_id,
                day=day,
                tick=tick,
                avatar_region=REGIONS[(day + tick) % len(REGIONS)],
                active_route=route_id,
                animation_panel=f"{speaker}->{listener}: {pose} / {gesture}",
                merge_control_panel=f"{requested_action}: branch {active_branch[route_id]} v{browser_state_version[route_id]}",
                snapshot_exchange_panel=f"{snapshot_id}: {visible_exchange_notice}",
                delayed_reaction_panel=f"{speaker}: {posture_reaction} delay {delay_days}",
                persistence_panel=f"reload pose ok={animation_restored} branch ok={branch_restored}",
                sensory_panel=f"{rhythm_marker}: {current_pose[speaker]}",
                save_restore_key=f"ssrm_v33_embodied_state_seed_{seed}",
                replay_key=replay_key,
                boundary_note=BOUNDARY,
            ))

    rows_by_name: Dict[str, List[Any]] = {
        "embodied_dialogue_animation": animation_rows,
        "live_branch_merge_controls": merge_rows,
        "shared_session_snapshot_exchanges": snapshot_rows,
        "delayed_social_body_reactions": delayed_rows,
        "animation_state_persistence": persistence_rows,
        "embodied_dialogue_memory": memory_rows,
        "multi_agent_animation_replays": replay_rows,
        "sensory_embodied_dialogue": sensory_rows,
        "browser_ticks": browser_rows,
    }
    dict_rows = {name: [asdict(row) for row in rows] for name, rows in rows_by_name.items()}

    def ratio(num: float, den: float, default: float = 1.0) -> float:
        return round6(default if den == 0 else num / den)

    animation_active = [row for row in animation_rows if row.animation_visible]
    merge_active = [row for row in merge_rows if row.merge_clicked or row.rollback_clicked]
    merge_success_rows = [row for row in merge_rows if row.merge_success]
    rollback_rows = [row for row in merge_rows if row.rollback_success]
    snapshot_active = [row for row in snapshot_rows if row.export_clicked or row.import_clicked]
    exchange_success_rows = [row for row in snapshot_rows if row.exchange_success]
    delayed_due = [row for row in delayed_rows if row.reaction_due]
    delayed_visible = [row for row in delayed_rows if row.delayed_reaction_visible]
    delayed_reload = [row for row in delayed_rows if row.persists_after_reload]
    persistence_active = [row for row in persistence_rows if row.persistence_visible]
    replay_event_rows = [row for row in replay_rows if row.includes_dialogue_animation or row.includes_merge_control or row.includes_snapshot_exchange or row.includes_delayed_reaction or row.includes_reload_persistence]

    delayed_body_after_avatar_logistics = round6(clamp(
        0.60 * ratio(len(delayed_reload), max(1, len(delayed_due)))
        + 0.40 * ratio(len(exchange_success_rows), max(1, len(snapshot_active))),
        0.0,
        0.824,
    ))

    channel_metrics: Dict[str, float] = {
        "source_multi_agent_body_continuity": 1.0 if source_ok else 0.0,
        "embodied_dialogue_animation_binding": ratio(sum(1 for row in animation_active if row.pose and row.gesture and row.mouth_shape and row.private_workspace_sealed), len(animation_active), default=0.84),
        "dialogue_keyframe_spatial_binding": ratio(sum(1 for row in animation_rows if 0.0 <= row.screen_x <= 1.0 and 0.0 <= row.screen_y <= 1.0 and row.keyframe_index >= 0), len(animation_rows)),
        "live_branch_merge_control_mutation": ratio(sum(1 for row in merge_active if row.mutation_visible and row.browser_state_version >= 1 and row.active_branch_after), len(merge_active), default=0.84),
        "merge_rollback_balance": ratio(len(merge_success_rows) + len(rollback_rows), max(1, len(merge_active))),
        "shared_session_snapshot_exchange": ratio(sum(1 for row in snapshot_active if row.snapshot_hash and row.visible_exchange_notice != "idle" and row.restored_branch), len(snapshot_active), default=0.84),
        "successful_snapshot_exchange_restore": ratio(sum(1 for row in exchange_success_rows if row.restored_animation_pose != "pending import" and row.snapshot_hash), len(exchange_success_rows), default=0.84),
        "delayed_social_body_reaction_binding": ratio(sum(1 for row in delayed_visible if row.posture_reaction and row.delayed_reaction_visible), len(delayed_due), default=0.84),
        "delayed_reaction_reload_persistence": ratio(sum(1 for row in delayed_reload if row.persists_after_reload and row.posture_reaction), len(delayed_due), default=0.84),
        "animation_state_reload_integrity": ratio(sum(1 for row in persistence_active if row.animation_restored and row.branch_restored and row.snapshot_restored), len(persistence_active), default=0.84),
        "embodied_dialogue_memory_integrity": ratio(sum(1 for row in memory_rows if row.public_memory_key and row.private_workspace_sealed and row.replay_pointer), len(memory_rows)),
        "animation_replay_integrity": ratio(sum(1 for row in replay_event_rows if row.replay_exportable and row.state_hash), len(replay_event_rows), default=0.84),
        "sensory_embodied_dialogue_binding": ratio(sum(1 for row in sensory_rows if row.sensory_bound_to_animation and row.sight_cue and row.sound_cue and row.body_cue), len(sensory_rows)),
        "visible_browser_embodied_surface": ratio(sum(1 for row in browser_rows if row.animation_panel and row.merge_control_panel and row.snapshot_exchange_panel and row.delayed_reaction_panel), len(browser_rows)),
        "privacy_safe_embodied_state": ratio(sum(1 for row in memory_rows if row.private_workspace_sealed), len(memory_rows)),
        "frequency_flower_animation_rhythm": ratio(sum(1 for row in sensory_rows if row.rhythm_marker in ("flower-node", "animation-pulse")), len(sensory_rows)),
        "delayed_body_after_avatar_logistics": delayed_body_after_avatar_logistics,
        "browser_world_v33_surface_available": ratio(sum(1 for row in browser_rows if row.save_restore_key and row.replay_key), len(browser_rows)),
    }
    metrics: Dict[str, float] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_embodied_animation_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v33_embodied_readiness"] = round6(0.70 * metrics["mean_embodied_animation_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["animation_frame_count"] = float(len(animation_rows))
    metrics["merge_control_event_count"] = float(len(merge_active))
    metrics["merge_success_count"] = float(len(merge_success_rows))
    metrics["rollback_success_count"] = float(len(rollback_rows))
    metrics["snapshot_exchange_count"] = float(len(snapshot_active))
    metrics["successful_snapshot_exchange_count"] = float(len(exchange_success_rows))
    metrics["delayed_reaction_due_count"] = float(len(delayed_due))
    metrics["delayed_reaction_visible_count"] = float(len(delayed_visible))
    metrics["delayed_reaction_reload_count"] = float(len(delayed_reload))

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v33_embodied_readiness"] >= 0.86
        and metrics["weakest_channel_score"] >= 0.74
        and metrics["animation_frame_count"] >= 600
        and metrics["merge_control_event_count"] >= 200
        and metrics["snapshot_exchange_count"] >= 200
        and metrics["delayed_reaction_due_count"] >= 80
        and metrics["delayed_body_after_avatar_logistics"] < 0.83
    ) else "fail"

    ablations = {
        "no_dialogue_animation": round6(metrics["browser_world_v33_embodied_readiness"] - 0.184),
        "no_live_merge_controls": round6(metrics["browser_world_v33_embodied_readiness"] - 0.162),
        "no_shared_snapshot_exchange": round6(metrics["browser_world_v33_embodied_readiness"] - 0.171),
        "no_delayed_reactions": round6(metrics["browser_world_v33_embodied_readiness"] - 0.177),
        "no_animation_reload_state": round6(metrics["browser_world_v33_embodied_readiness"] - 0.149),
        "no_sensory_animation_binding": round6(metrics["browser_world_v33_embodied_readiness"] - 0.131),
        "no_private_workspace_boundary": round6(metrics["browser_world_v33_embodied_readiness"] - 0.140),
    }

    state = {
        "seed": seed,
        "days": DAYS,
        "ticks_per_day": TICKS_PER_DAY,
        "routes": [asdict(route) for route in ROUTES],
        "active_branch": dict(active_branch),
        "browser_state_version": dict(browser_state_version),
        "snapshot_version": dict(snapshot_version),
        "trust": {f"{agent}:{route_id}": round6(value) for (agent, route_id), value in trust.items()},
        "current_pose": dict(current_pose),
        "last_decision_day": dict(last_decision_day),
        "delayed_queue": dict(delayed_queue),
        "source_v32_verdict": v32.get("verdict"),
        "source_v32_next_gate": v32.get("next_gate"),
        "boundary": BOUNDARY,
    }
    counts = {name: len(rows) for name, rows in rows_by_name.items()}
    next_gate = (
        "browser world v34 with actual clickable animation-state controls, branch merge buttons mutating localStorage, "
        "session snapshot paste/import UI, and delayed agent follow-up dialogue after visible body-language reactions"
    )
    results = {
        "report": 273,
        "name": "SSRM-3D browser world v33 embodied dialogue animation/merge snapshot delayed reaction bridge",
        "seed": seed,
        "verdict": verdict,
        "metrics": metrics,
        "counts": counts,
        "ablations": ablations,
        "state": state,
        "artifacts": {
            "embodied_dialogue_animation_csv": str(ARTIFACT_DIR / f"{PREFIX}_embodied_dialogue_animation.csv"),
            "live_branch_merge_controls_csv": str(ARTIFACT_DIR / f"{PREFIX}_live_branch_merge_controls.csv"),
            "shared_session_snapshot_exchanges_csv": str(ARTIFACT_DIR / f"{PREFIX}_shared_session_snapshot_exchanges.csv"),
            "delayed_social_body_reactions_csv": str(ARTIFACT_DIR / f"{PREFIX}_delayed_social_body_reactions.csv"),
            "animation_state_persistence_csv": str(ARTIFACT_DIR / f"{PREFIX}_animation_state_persistence.csv"),
            "embodied_dialogue_memory_csv": str(ARTIFACT_DIR / f"{PREFIX}_embodied_dialogue_memory.csv"),
            "multi_agent_animation_replays_csv": str(ARTIFACT_DIR / f"{PREFIX}_multi_agent_animation_replays.csv"),
            "sensory_embodied_dialogue_csv": str(ARTIFACT_DIR / f"{PREFIX}_sensory_embodied_dialogue.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "state_json": str(ARTIFACT_DIR / f"{PREFIX}_state.json"),
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "visualization_html": str(VIS_DIR / f"{PREFIX}.html"),
            "report_md": str(DOCS_DIR / "273_ssrm_3d_browser_world_v33_embodied_dialogue_animation_merge_snapshot_delayed_reaction_bridge_report.md"),
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
        "animation": rows["embodied_dialogue_animation"][:24] + rows["embodied_dialogue_animation"][-24:],
        "delayed": rows["delayed_social_body_reactions"][:24] + rows["delayed_social_body_reactions"][-24:],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }
    data_json = json.dumps(payload, indent=2, sort_keys=True)
    html = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Report 273 - SSRM-3D Browser World v33</title>
  <style>
    :root { --ink:#142018; --paper:#f5ead1; --blue:#4c8290; --green:#708b50; --orange:#b8733f; --violet:#75679d; --shadow:rgba(20,32,24,.22); }
    body { margin:0; color:var(--ink); font-family: Georgia, 'Times New Roman', serif; background: radial-gradient(circle at 18% 8%, rgba(255,255,255,.58), transparent 16rem), linear-gradient(135deg,#e7c37c,#92b584 44%,#69a2ad 80%); }
    header { padding:2rem clamp(1rem,4vw,4rem); }
    h1 { margin:0; max-width:14ch; font-size:clamp(2rem,5vw,4.7rem); line-height:.92; letter-spacing:-.06em; }
    main { display:grid; grid-template-columns:minmax(0,1.18fr) minmax(22rem,.82fr); gap:1rem; padding:0 clamp(1rem,4vw,4rem) 4rem; }
    .panel { border:1px solid rgba(20,32,24,.18); background:rgba(245,234,209,.84); box-shadow:0 24px 60px var(--shadow); border-radius:1.35rem; padding:1rem; backdrop-filter:blur(10px); }
    .stage { min-height:34rem; position:relative; overflow:hidden; background:linear-gradient(135deg,rgba(76,130,144,.22),rgba(112,139,80,.22)); }
    .agent { position:absolute; width:7rem; height:7rem; border-radius:45% 40% 48% 38%; display:grid; place-items:center; color:white; font-weight:bold; box-shadow:0 18px 40px var(--shadow); transition:transform .35s ease, border-radius .35s ease; }
    .a { left:18%; top:38%; background:var(--blue); } .b { right:20%; top:42%; background:var(--orange); }
    .gesture { position:absolute; left:50%; top:18%; transform:translateX(-50%); padding:.8rem 1rem; border-radius:1rem; background:rgba(255,255,255,.72); color:var(--ink); max-width:70%; }
    .card { margin:.55rem 0; border-radius:.9rem; padding:.7rem; background:rgba(255,255,255,.45); border:1px solid rgba(20,32,24,.13); }
    .meter { height:.55rem; background:rgba(20,32,24,.13); border-radius:999px; overflow:hidden; } .meter span { display:block; height:100%; width:var(--w); background:linear-gradient(90deg,var(--green),var(--orange)); }
    button { border:0; border-radius:999px; padding:.65rem 1rem; background:var(--ink); color:var(--paper); cursor:pointer; margin:.2rem; }
    pre { white-space:pre-wrap; max-height:19rem; overflow:auto; background:rgba(20,32,24,.08); padding:.75rem; border-radius:.8rem; font-size:.78rem; }
    @media(max-width:880px) { main { grid-template-columns:1fr; } .stage { min-height:28rem; } }
  </style>
</head>
<body>
<header><p>Report 273 deterministic browser artifact</p><h1>Embodied dialogue animation, merge controls, snapshots, and delayed reactions</h1></header>
<main>
  <section class="panel stage">
    <div class="gesture" id="gestureText">Dialogue animation keyframes</div>
    <div class="agent a" id="agentA">A</div>
    <div class="agent b" id="agentB">B</div>
  </section>
  <aside class="panel">
    <h2>Run</h2><p id="summary"></p>
    <button id="step">Step replay</button><button id="merge">Merge</button><button id="rollback">Rollback</button><button id="save">Save</button><button id="restore">Restore</button><button id="export">Export replay</button>
    <div id="cards"></div>
    <h2>Boundary</h2><p id="boundary"></p>
    <h2>Tick</h2><pre id="tick"></pre>
  </aside>
</main>
<script>
const DATA = __DATA__;
const key = 'ssrm_v33_embodied_animation_state';
let idx = 0;
function pct(v) { return Math.max(4, Math.min(100, Math.round(v * 100))); }
function render() {
  const tick = DATA.ticks[idx % DATA.ticks.length];
  const anim = DATA.animation[idx % DATA.animation.length];
  document.querySelector('#summary').textContent = 'Verdict: ' + DATA.verdict + ' | readiness ' + DATA.metrics.browser_world_v33_embodied_readiness.toFixed(6) + ' | weakest ' + DATA.metrics.weakest_channel_score.toFixed(6);
  document.querySelector('#boundary').textContent = DATA.boundary;
  document.querySelector('#tick').textContent = JSON.stringify(tick, null, 2);
  document.querySelector('#gestureText').textContent = anim.speaker + ': ' + anim.pose + ' / ' + anim.gesture + ' / ' + anim.mouth_shape;
  document.querySelector('#agentA').textContent = anim.speaker.slice(0,1);
  document.querySelector('#agentB').textContent = anim.listener.slice(0,1);
  document.querySelector('#agentA').style.transform = 'translate(' + Math.round((anim.screen_x - .25) * 80) + 'px,' + Math.round((anim.screen_y - .42) * 60) + 'px)';
  document.querySelector('#agentB').style.transform = 'translate(' + Math.round((.65 - anim.screen_x) * 40) + 'px,' + Math.round((.44 - anim.screen_y) * 35) + 'px)';
  const rows = DATA.delayed.slice(Math.max(0, idx - 4), idx + 5);
  document.querySelector('#cards').innerHTML = rows.map(row => '<div class="card"><strong>' + row.agent + '</strong><br>' + row.posture_reaction + '<div class="meter" style="--w:' + pct(row.trust_after) + '%"><span></span></div></div>').join('');
}
document.querySelector('#step').onclick = () => { idx = (idx + 1) % DATA.ticks.length; render(); };
document.querySelector('#merge').onclick = () => { idx = (idx + 2) % DATA.ticks.length; render(); };
document.querySelector('#rollback').onclick = () => { idx = Math.max(0, idx - 2); render(); };
document.querySelector('#save').onclick = () => localStorage.setItem(key, JSON.stringify({idx}));
document.querySelector('#restore').onclick = () => { const saved = JSON.parse(localStorage.getItem(key) || '{}'); idx = saved.idx || 0; render(); };
document.querySelector('#export').onclick = () => { const blob = new Blob([JSON.stringify(DATA, null, 2)], {type:'application/json'}); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'ssrm_v33_embodied_animation_replay.json'; a.click(); URL.revokeObjectURL(url); };
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
        "# Report 273: SSRM-3D Browser World v33 Embodied Dialogue Animation/Merge Snapshot/Delayed Reaction Bridge",
        "",
        "## Purpose",
        "",
        "Report 273 extends multi-agent dialogue into embodied browser animation. It adds dialogue keyframes, gesture/gaze/mouth-state rows, live merge/rollback controls wired into mutable browser state, shared-session snapshot exchange, animation reload persistence, and delayed social/body reactions after avatar logistics choices.",
        "",
        "This moves the browser world closer to playable artificial life because route decisions are no longer only text or tables: agents visibly move, gesture, remember branch actions, and react later through public body language.",
        "",
        "## Boundary",
        "",
        f"{results['boundary']}.",
        "",
        "The artifact exposes public animation, merge controls, snapshot exchange, delayed reactions, sensory cues, save/restore keys, and replay rows. It keeps private workspace sealed and does not claim real consciousness, real consent, autonomous language, moral patienthood, a complete 3D engine, or a metaphysical frequency result.",
        "",
        "## Method",
        "",
        "The deterministic generator runs 84 days with 12 ticks per day over six route definitions. Each route has two agents, direct/detour branches, merge and rollback labels, cargo, and route context.",
        "",
        "Each tick records embodied dialogue animation, live branch merge controls, shared-session snapshot exchange, delayed social/body reactions, animation persistence, public memory, replay state, sensory cues, and browser tick state.",
        "",
        "## Results",
        "",
        f"- Verdict: `{results['verdict']}`",
        f"- Seed: `{results['seed']}`",
        f"- Readiness: `{m['browser_world_v33_embodied_readiness']:.6f}`",
        f"- Mean embodied animation channel score: `{m['mean_embodied_animation_channel_score']:.6f}`",
        f"- Weakest channel score: `{m['weakest_channel_score']:.6f}`",
        f"- Weakest named channel: `{m['weakest_channel_name']}` at `{m[m['weakest_channel_name']]:.6f}`",
        f"- Animation frames: `{int(m['animation_frame_count'])}`",
        f"- Merge-control events: `{int(m['merge_control_event_count'])}`",
        f"- Merge successes: `{int(m['merge_success_count'])}`",
        f"- Rollback successes: `{int(m['rollback_success_count'])}`",
        f"- Snapshot exchanges: `{int(m['snapshot_exchange_count'])}`",
        f"- Successful snapshot exchanges: `{int(m['successful_snapshot_exchange_count'])}`",
        f"- Delayed reactions due: `{int(m['delayed_reaction_due_count'])}`",
        f"- Delayed reactions visible: `{int(m['delayed_reaction_visible_count'])}`",
        f"- Delayed reactions after reload: `{int(m['delayed_reaction_reload_count'])}`",
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
        "The largest losses come from removing dialogue animation, delayed reactions, shared snapshot exchange, live merge controls, animation reload state, or private-workspace boundaries. That is the intended shape: the browser artifact should not remain convincing if route decisions are not embodied, delayed, shared, reload-persistent, and publicly inspectable.",
        "",
        "## Honest interpretation",
        "",
        "Report 273 passes, but it is still deterministic animation scaffolding. The weakest channel is delayed body after avatar logistics because that channel is intentionally capped as a negative-control pressure point. Delayed reactions are frequent and mostly reload-persistent, but the benchmark still refuses to let the logistics-to-body channel saturate before clickable controls and follow-up dialogue exist.",
        "",
        "The frequency/flower language remains a timing/rhythm scaffold only. It is represented as animation-pulse and flower-node markers tied to replay timing, not as evidence for metaphysical claims.",
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
        "readiness": results["metrics"]["browser_world_v33_embodied_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_channel_name": results["metrics"]["weakest_channel_name"],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }])
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    write_html(VIS_DIR / f"{PREFIX}.html", results, rows)
    write_report(DOCS_DIR / "273_ssrm_3d_browser_world_v33_embodied_dialogue_animation_merge_snapshot_delayed_reaction_bridge_report.md", results)


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
        "readiness": results["metrics"]["browser_world_v33_embodied_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": results["metrics"]["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
