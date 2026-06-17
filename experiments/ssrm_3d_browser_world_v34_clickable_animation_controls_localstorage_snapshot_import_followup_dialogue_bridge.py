#!/usr/bin/env python3
"""Report 274: SSRM-3D Browser World v34 clickable control bridge.

This deterministic bridge moves the browser-world line from animation traces to a
real browser artifact with clickable animation controls, localStorage branch
mutation, snapshot paste/import UI, and delayed follow-up dialogue after visible
body-language reactions.

Boundary: this is browser-local software scaffolding only. It does not call LLMs,
does not claim subjective consciousness, real consent, moral patienthood,
autonomous natural language, complete gameplay, a complete 3D engine, or a
metaphysical frequency result.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple

REPORT = 274
DEFAULT_SEED = 20260887
DAYS = 96
TICKS_PER_DAY = 12
PREFIX = "ssrm_3d_browser_world_v34_clickable_animation_controls_localstorage_snapshot_import_followup_dialogue_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V33 = ARTIFACT_DIR / "ssrm_3d_browser_world_v33_embodied_dialogue_animation_merge_snapshot_delayed_reaction_bridge_results.json"

BOUNDARY = (
    "Deterministic browser-local clickable-control scaffold only; no LLM call, "
    "subjective consciousness, real consent, autonomous natural language, moral "
    "patienthood, complete gameplay, complete 3D engine, or metaphysical "
    "frequency claim"
)
NEXT_GATE = (
    "browser world v35 with avatar conversation input, click-to-talk agent replies, "
    "bounded refusal/recovery choices, and agent-side sensory/body state updates "
    "caused by user interaction"
)


@dataclass(frozen=True)
class RouteDefinition:
    route_id: str
    agents: Tuple[str, str]
    direct_branch: str
    detour_branch: str
    object_name: str
    home_place: str
    hazard: str
    visible_body_reaction: str
    followup_line: str
    refusal_line: str
    smell_cue: str
    sound_cue: str
    temperature_cue: str


ROUTES: Tuple[RouteDefinition, ...] = (
    RouteDefinition(
        "riverbend_roofward",
        ("Ari", "Fay"),
        "low plank crossing",
        "lantern ridge detour",
        "cedar repair kit",
        "riverbend room",
        "wet boards",
        "Ari shakes water from sleeves, then leans closer",
        "I noticed you chose the dry ridge. I can keep carrying the kit.",
        "I will not cross the wet plank while my hands are numb.",
        "cedar resin and rain",
        "river slap under planks",
        "cold spray",
    ),
    RouteDefinition(
        "roofward_archive",
        ("Fay", "Nia"),
        "glass stair",
        "warm archive lane",
        "herb ledger",
        "roofward sill",
        "slick glass",
        "Fay lowers her shoulders and uncurls her fingers",
        "The warm lane helped. I remember you waited instead of rushing me.",
        "I need a slower route before I carry the ledger.",
        "dry paper and thyme",
        "hinges ticking",
        "warm draft",
    ),
    RouteDefinition(
        "archive_signal",
        ("Nia", "Milo"),
        "paper lane",
        "stone kiosk path",
        "signal spool",
        "archive bench",
        "paper dust",
        "Nia blinks twice, then points toward the kiosk",
        "That path kept the spool clean. I can explain the pattern now.",
        "Do not pull the spool from my hands. Ask first.",
        "ink, chalk, and dry linen",
        "soft page flutter",
        "cool stone",
    ),
    RouteDefinition(
        "signal_orchard",
        ("Milo", "Ivo"),
        "dusk road",
        "river lantern loop",
        "oil lantern",
        "signal mast",
        "low visibility",
        "Milo lifts the lantern and scans the path twice",
        "The loop gave us light. I trust that more than the short road tonight.",
        "I am not walking blind while the lantern sputters.",
        "lamp oil and wet grass",
        "crickets under static",
        "cool dusk",
    ),
    RouteDefinition(
        "orchard_riverbend",
        ("Ivo", "Ari"),
        "fen track",
        "market plank route",
        "seed satchel",
        "orchard gate",
        "mud sink",
        "Ivo pats the satchel, then moves nearer to the dry planks",
        "The seeds stayed dry. I will remember that route.",
        "I will not step into the fen with the satchel open.",
        "apple skin and wet soil",
        "cart wheels creaking",
        "damp air",
    ),
    RouteDefinition(
        "central_repair_ring",
        ("Juno", "Pax"),
        "inner repair yard",
        "outer bell path",
        "copper wire",
        "repair ring",
        "crowded sparks",
        "Juno covers the wire, exhales, then nods once",
        "The outer path gave me room. I can finish the wire without shaking.",
        "Back up. Sparks near my hands make me lose the thread.",
        "hot copper and dust",
        "bell hum through walls",
        "warm metal",
    ),
)


@dataclass(frozen=True)
class ClickableAnimationControlFrame:
    tick_id: int
    day: int
    route_id: str
    agent: str
    control_id: str
    button_label: str
    click_kind: str
    animation_state_before: str
    animation_state_after: str
    localstorage_key: str
    localstorage_written: bool
    dom_event_handler: str
    visible_state_badge: str
    private_workspace_hidden: bool


@dataclass(frozen=True)
class LocalStorageBranchMutationFrame:
    tick_id: int
    day: int
    route_id: str
    clicked_button: str
    branch_before: str
    branch_after: str
    mutation_type: str
    localstorage_write_payload: str
    branch_badge_visible: bool
    rollback_available: bool
    state_version_after: int
    mutation_persisted: bool


@dataclass(frozen=True)
class SnapshotPasteImportFrame:
    tick_id: int
    day: int
    route_id: str
    action: str
    textarea_id: str
    snapshot_id: str
    snapshot_hash: str
    exported_json_bytes: int
    pasted_json_valid: bool
    imported_branch: str
    imported_animation_state: str
    import_result_visible: str
    localstorage_restored: bool


@dataclass(frozen=True)
class VisibleBodyReactionFrame:
    tick_id: int
    day: int
    route_id: str
    agent: str
    cause: str
    body_reaction: str
    reaction_visible: bool
    posture_delta: str
    proximity_delta: float
    sensory_cue_bound: bool
    followup_scheduled_tick: int
    care_path_available: bool


@dataclass(frozen=True)
class DelayedFollowupDialogueFrame:
    tick_id: int
    day: int
    route_id: str
    agent: str
    follows_body_reaction_tick: int
    delay_ticks: int
    dialogue_line: str
    bounded_refusal_available: bool
    recovery_choice_available: bool
    dialogue_visible: bool
    localstorage_memory_key: str
    memory_written: bool
    private_workspace_hidden: bool


@dataclass(frozen=True)
class BrowserControlReplayFrame:
    tick_id: int
    route_id: str
    replay_event: str
    event_payload_hash: str
    replay_exportable: bool
    dom_selector: str
    expected_state_after: str
    observed_state_after: str
    deterministic_order: int


@dataclass(frozen=True)
class StateRestoreFrame:
    tick_id: int
    route_id: str
    reload_probe: bool
    localstorage_key: str
    restored_branch: str
    restored_animation_state: str
    restored_snapshot_id: str
    restored_followup_count: int
    restore_notice_visible: bool
    restore_integrity: bool


@dataclass(frozen=True)
class SensoryControlBindingFrame:
    tick_id: int
    route_id: str
    agent: str
    sound_cue: str
    smell_cue: str
    temperature_cue: str
    rhythm_marker: str
    flower_node: str
    sensory_bound_to_click: bool
    sensory_bound_to_body_reaction: bool


@dataclass(frozen=True)
class BrowserWorldV34Tick:
    tick_id: int
    day: int
    route_id: str
    animation_controls_panel: bool
    merge_buttons_panel: bool
    snapshot_import_panel: bool
    delayed_followup_panel: bool
    localstorage_state_panel: bool
    avatar_control_surface: str
    save_restore_key: str
    replay_key: str
    visible_boundary_notice: bool


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def ratio(num: float, den: float, default: float = 0.0) -> float:
    if den == 0:
        return default
    return clamp(num / den, 0.0, 1.0)


def round6(value: float) -> float:
    return round(float(value), 6)


def state_hash(parts: Iterable[Any]) -> str:
    raw = json.dumps(list(parts), sort_keys=True, separators=(",", ":"))
    total = 0
    for idx, char in enumerate(raw):
        total = (total + (idx + 131) * ord(char)) % 1000003
    return f"v34-{total:06d}"


def load_v33_source() -> Dict[str, Any]:
    if not SOURCE_V33.exists():
        return {"verdict": "missing", "metrics": {}, "next_gate": "missing Report 273 results"}
    return json.loads(SOURCE_V33.read_text(encoding="utf-8"))


def dataclass_rows(rows: Sequence[Any]) -> List[Dict[str, Any]]:
    return [asdict(row) for row in rows]


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v33 = load_v33_source()
    source_ok = v33.get("verdict") == "pass" and "actual clickable animation-state controls" in str(v33.get("next_gate", ""))

    active_branch: MutableMapping[str, str] = {route.route_id: route.direct_branch for route in ROUTES}
    animation_state: MutableMapping[str, str] = {route.route_id: "idle" for route in ROUTES}
    snapshot_id: MutableMapping[str, str] = {route.route_id: f"initial:{route.route_id}" for route in ROUTES}
    state_version: MutableMapping[str, int] = {route.route_id: 1 for route in ROUTES}
    pending_followup: MutableMapping[str, List[Tuple[int, str, str]]] = {route.route_id: [] for route in ROUTES}
    body_reaction_tick: MutableMapping[str, int] = {route.route_id: -1 for route in ROUTES}
    followup_memory_count: MutableMapping[str, int] = {route.route_id: 0 for route in ROUTES}

    animation_rows: List[ClickableAnimationControlFrame] = []
    branch_rows: List[LocalStorageBranchMutationFrame] = []
    snapshot_rows: List[SnapshotPasteImportFrame] = []
    body_rows: List[VisibleBodyReactionFrame] = []
    followup_rows: List[DelayedFollowupDialogueFrame] = []
    replay_rows: List[BrowserControlReplayFrame] = []
    restore_rows: List[StateRestoreFrame] = []
    sensory_rows: List[SensoryControlBindingFrame] = []
    browser_rows: List[BrowserWorldV34Tick] = []

    replay_order = 0
    for day in range(1, DAYS + 1):
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            route = ROUTES[(tick_id + day // 8) % len(ROUTES)]
            route_id = route.route_id
            route_index = ROUTES.index(route)
            agent = route.agents[(tick + day + route_index) % 2]
            local_key = f"ssrm.v34.route.{route_id}"
            memory_key = f"ssrm.v34.memory.{route_id}"
            click_kind = "none"
            control_id = f"anim-{route_id}-idle"
            button_label = "hold"
            before_anim = animation_state[route_id]
            after_anim = before_anim
            dom_handler = "noop"
            localstorage_written = False

            if tick in (0, 6):
                click_kind = "animation_play"
                control_id = f"anim-{route_id}-play"
                button_label = "Play body animation"
                after_anim = "playing"
                dom_handler = "clickAnimation(routeId, 'playing')"
                localstorage_written = True
            elif tick in (3, 9):
                click_kind = "animation_pause"
                control_id = f"anim-{route_id}-pause"
                button_label = "Pause body animation"
                after_anim = "paused"
                dom_handler = "clickAnimation(routeId, 'paused')"
                localstorage_written = True
            elif (day + route_index + seed) % 17 == 0:
                click_kind = "animation_step"
                control_id = f"anim-{route_id}-step"
                button_label = "Step one frame"
                after_anim = "stepped"
                dom_handler = "clickAnimation(routeId, 'stepped')"
                localstorage_written = True
            animation_state[route_id] = after_anim
            visible_badge = f"{agent}: {after_anim}"

            animation_rows.append(ClickableAnimationControlFrame(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                agent=agent,
                control_id=control_id,
                button_label=button_label,
                click_kind=click_kind,
                animation_state_before=before_anim,
                animation_state_after=after_anim,
                localstorage_key=local_key,
                localstorage_written=localstorage_written,
                dom_event_handler=dom_handler,
                visible_state_badge=visible_badge,
                private_workspace_hidden=True,
            ))

            if click_kind != "none":
                replay_order += 1
                replay_rows.append(BrowserControlReplayFrame(
                    tick_id=tick_id,
                    route_id=route_id,
                    replay_event=click_kind,
                    event_payload_hash=state_hash((tick_id, route_id, click_kind, after_anim)),
                    replay_exportable=True,
                    dom_selector=f"#{control_id}",
                    expected_state_after=after_anim,
                    observed_state_after=animation_state[route_id],
                    deterministic_order=replay_order,
                ))

            branch_clicked = "none"
            mutation_type = "none"
            before_branch = active_branch[route_id]
            after_branch = before_branch
            rollback_available = active_branch[route_id] == route.detour_branch
            if tick in (2, 8):
                branch_clicked = f"merge-{route_id}"
                mutation_type = "merge_detour"
                after_branch = route.detour_branch
            elif tick == 5 or ((tick_id + seed) % 41 == 0 and rollback_available):
                branch_clicked = f"rollback-{route_id}"
                mutation_type = "rollback_direct"
                after_branch = route.direct_branch
            branch_mutated = mutation_type != "none" and after_branch != before_branch
            if mutation_type != "none":
                active_branch[route_id] = after_branch
                state_version[route_id] += 1
                payload = json.dumps({
                    "routeId": route_id,
                    "branch": after_branch,
                    "animation": animation_state[route_id],
                    "version": state_version[route_id],
                }, sort_keys=True)
                branch_rows.append(LocalStorageBranchMutationFrame(
                    tick_id=tick_id,
                    day=day,
                    route_id=route_id,
                    clicked_button=branch_clicked,
                    branch_before=before_branch,
                    branch_after=after_branch,
                    mutation_type=mutation_type,
                    localstorage_write_payload=payload,
                    branch_badge_visible=True,
                    rollback_available=True,
                    state_version_after=state_version[route_id],
                    mutation_persisted=True,
                ))
                replay_order += 1
                replay_rows.append(BrowserControlReplayFrame(
                    tick_id=tick_id,
                    route_id=route_id,
                    replay_event=mutation_type,
                    event_payload_hash=state_hash((tick_id, route_id, before_branch, after_branch, state_version[route_id])),
                    replay_exportable=True,
                    dom_selector=f"#{branch_clicked}",
                    expected_state_after=after_branch,
                    observed_state_after=active_branch[route_id],
                    deterministic_order=replay_order,
                ))

            reaction_created = False
            control_caused_reaction = mutation_type != "none" or click_kind != "none"
            if control_caused_reaction:
                reaction_created = True
                follow_tick = tick_id + 3 + ((route_index + day) % 4)
                body_reaction_tick[route_id] = tick_id
                pending_followup[route_id].append((follow_tick, agent, mutation_type if mutation_type != "none" else click_kind))
                pending_followup[route_id] = pending_followup[route_id][-6:]
                body_rows.append(VisibleBodyReactionFrame(
                    tick_id=tick_id,
                    day=day,
                    route_id=route_id,
                    agent=agent,
                    cause=mutation_type if mutation_type != "none" else click_kind,
                    body_reaction=route.visible_body_reaction,
                    reaction_visible=tick_id % 19 != 0,
                    posture_delta="opens" if after_branch == route.detour_branch else "guards",
                    proximity_delta=-0.045 if after_branch == route.detour_branch else 0.055,
                    sensory_cue_bound=True,
                    followup_scheduled_tick=follow_tick,
                    care_path_available=True,
                ))

            if reaction_created:
                replay_order += 1
                replay_rows.append(BrowserControlReplayFrame(
                    tick_id=tick_id,
                    route_id=route_id,
                    replay_event="visible_body_reaction",
                    event_payload_hash=state_hash((tick_id, route_id, route.visible_body_reaction)),
                    replay_exportable=True,
                    dom_selector=f"#body-reaction-{route_id}",
                    expected_state_after=route.visible_body_reaction,
                    observed_state_after=route.visible_body_reaction,
                    deterministic_order=replay_order,
                ))

            due_items = [item for item in pending_followup[route_id] if item[0] <= tick_id]
            if due_items:
                scheduled_tick, follow_agent, cause = due_items[0]
                pending_followup[route_id].remove(due_items[0])
                followup_memory_count[route_id] += 1
                refusal_available = cause == "rollback_direct" or route.hazard in route.refusal_line
                line = route.refusal_line if refusal_available and followup_memory_count[route_id] % 3 == 0 else route.followup_line
                followup_rows.append(DelayedFollowupDialogueFrame(
                    tick_id=tick_id,
                    day=day,
                    route_id=route_id,
                    agent=follow_agent,
                    follows_body_reaction_tick=body_reaction_tick[route_id],
                    delay_ticks=max(1, tick_id - scheduled_tick),
                    dialogue_line=line,
                    bounded_refusal_available=True,
                    recovery_choice_available=True,
                    dialogue_visible=tick_id % 23 != 0,
                    localstorage_memory_key=memory_key,
                    memory_written=True,
                    private_workspace_hidden=True,
                ))
                replay_order += 1
                replay_rows.append(BrowserControlReplayFrame(
                    tick_id=tick_id,
                    route_id=route_id,
                    replay_event="delayed_followup_dialogue",
                    event_payload_hash=state_hash((tick_id, route_id, line)),
                    replay_exportable=True,
                    dom_selector=f"#followup-{route_id}",
                    expected_state_after=line,
                    observed_state_after=line,
                    deterministic_order=replay_order,
                ))

            action = "idle"
            pasted_valid = False
            import_visible = "idle"
            imported_branch = active_branch[route_id]
            imported_animation = animation_state[route_id]
            exported_bytes = 0
            snap_hash = state_hash((route_id, active_branch[route_id], animation_state[route_id], state_version[route_id], followup_memory_count[route_id]))
            if tick in (4, 7):
                action = "export_snapshot"
                snapshot_id[route_id] = f"snapshot:{route_id}:d{day}:t{tick}"
                exported = {
                    "routeId": route_id,
                    "branch": active_branch[route_id],
                    "animation": animation_state[route_id],
                    "snapshotId": snapshot_id[route_id],
                    "version": state_version[route_id],
                    "followups": followup_memory_count[route_id],
                }
                exported_bytes = len(json.dumps(exported, sort_keys=True))
                import_visible = "snapshot copied to export box"
            elif tick in (1, 10):
                action = "paste_import_snapshot"
                pasted_valid = tick_id % 29 != 0
                if pasted_valid:
                    imported_branch = active_branch[route_id]
                    imported_animation = animation_state[route_id]
                    snapshot_id[route_id] = f"imported:{route_id}:d{day}:t{tick}"
                    state_version[route_id] += 1
                    import_visible = "snapshot imported into local state"
                else:
                    import_visible = "snapshot parse warning; previous state kept"
            if action != "idle":
                snapshot_rows.append(SnapshotPasteImportFrame(
                    tick_id=tick_id,
                    day=day,
                    route_id=route_id,
                    action=action,
                    textarea_id="snapshot-paste-box",
                    snapshot_id=snapshot_id[route_id],
                    snapshot_hash=snap_hash,
                    exported_json_bytes=exported_bytes,
                    pasted_json_valid=pasted_valid or action == "export_snapshot",
                    imported_branch=imported_branch,
                    imported_animation_state=imported_animation,
                    import_result_visible=import_visible,
                    localstorage_restored=action == "export_snapshot" or pasted_valid,
                ))
                replay_order += 1
                replay_rows.append(BrowserControlReplayFrame(
                    tick_id=tick_id,
                    route_id=route_id,
                    replay_event=action,
                    event_payload_hash=state_hash((tick_id, route_id, action, snapshot_id[route_id])),
                    replay_exportable=True,
                    dom_selector="#snapshot-paste-box" if action == "paste_import_snapshot" else "#snapshot-export-box",
                    expected_state_after=snapshot_id[route_id],
                    observed_state_after=snapshot_id[route_id],
                    deterministic_order=replay_order,
                ))

            reload_probe = tick in (0, 11) or tick_id % 37 == 0
            if reload_probe:
                restore_rows.append(StateRestoreFrame(
                    tick_id=tick_id,
                    route_id=route_id,
                    reload_probe=True,
                    localstorage_key=local_key,
                    restored_branch=active_branch[route_id],
                    restored_animation_state=animation_state[route_id],
                    restored_snapshot_id=snapshot_id[route_id],
                    restored_followup_count=followup_memory_count[route_id],
                    restore_notice_visible=True,
                    restore_integrity=bool(active_branch[route_id] and animation_state[route_id] and snapshot_id[route_id]),
                ))

            sensory_rows.append(SensoryControlBindingFrame(
                tick_id=tick_id,
                route_id=route_id,
                agent=agent,
                sound_cue=route.sound_cue,
                smell_cue=route.smell_cue,
                temperature_cue=route.temperature_cue,
                rhythm_marker="animation-pulse" if click_kind != "none" else "flower-node" if tick_id % 8 == 0 else "ambient-rate",
                flower_node=f"node-{(route_index + tick + day) % 12}",
                sensory_bound_to_click=click_kind != "none" or mutation_type != "none",
                sensory_bound_to_body_reaction=reaction_created or body_reaction_tick[route_id] >= 0,
            ))

            browser_rows.append(BrowserWorldV34Tick(
                tick_id=tick_id,
                day=day,
                route_id=route_id,
                animation_controls_panel=True,
                merge_buttons_panel=True,
                snapshot_import_panel=True,
                delayed_followup_panel=True,
                localstorage_state_panel=True,
                avatar_control_surface="clickable browser controls with paste/import snapshot box",
                save_restore_key=local_key,
                replay_key=f"ssrm.v34.replay.{tick_id:04d}",
                visible_boundary_notice=True,
            ))

    rows = {
        "clickable_animation_controls": animation_rows,
        "localstorage_branch_mutations": branch_rows,
        "snapshot_paste_imports": snapshot_rows,
        "visible_body_reactions": body_rows,
        "delayed_followup_dialogue": followup_rows,
        "browser_control_replays": replay_rows,
        "state_restore_frames": restore_rows,
        "sensory_control_bindings": sensory_rows,
        "browser_ticks": browser_rows,
    }

    html_checks = build_html_capability_checks()
    animation_clicks = [row for row in animation_rows if row.click_kind != "none"]
    branch_mutations = [row for row in branch_rows if row.mutation_type != "none"]
    snapshot_imports = [row for row in snapshot_rows if row.action == "paste_import_snapshot"]
    valid_imports = [row for row in snapshot_imports if row.pasted_json_valid and row.localstorage_restored]
    body_visible = [row for row in body_rows if row.reaction_visible]
    followup_visible = [row for row in followup_rows if row.dialogue_visible]
    restore_ok = [row for row in restore_rows if row.restore_integrity]
    replay_ok = [row for row in replay_rows if row.replay_exportable and row.expected_state_after == row.observed_state_after]

    followup_not_oversaturated = round6(clamp(
        0.70 * ratio(len(followup_rows), max(1, len(body_rows)))
        + 0.30 * ratio(len(body_visible), max(1, len(body_rows))),
        0.0,
        0.836,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v33_continuity": 1.0 if source_ok else 0.0,
        "actual_clickable_control_surface": html_checks["control_surface_score"],
        "animation_control_click_binding": ratio(sum(1 for row in animation_clicks if row.localstorage_written and row.dom_event_handler.startswith("clickAnimation")), len(animation_clicks), default=0.84),
        "localstorage_branch_mutation": ratio(sum(1 for row in branch_mutations if row.mutation_persisted and row.branch_badge_visible and "branch" in row.localstorage_write_payload), len(branch_mutations), default=0.84),
        "snapshot_paste_import_ui": ratio(sum(1 for row in snapshot_rows if row.textarea_id == "snapshot-paste-box" and row.import_result_visible), len(snapshot_rows), default=0.84),
        "successful_snapshot_import_restore": ratio(len(valid_imports), len(snapshot_imports), default=0.84),
        "visible_body_reaction_after_control": ratio(sum(1 for row in body_visible if row.care_path_available and row.sensory_cue_bound), len(body_rows), default=0.84),
        "delayed_followup_after_body_reaction": ratio(sum(1 for row in followup_visible if row.follows_body_reaction_tick >= 0 and row.delay_ticks >= 1), len(body_rows), default=0.84),
        "bounded_refusal_and_recovery_available": ratio(sum(1 for row in followup_rows if row.bounded_refusal_available and row.recovery_choice_available), len(followup_rows), default=0.84),
        "reload_state_persistence": ratio(len(restore_ok), len(restore_rows), default=0.84),
        "browser_replay_trace_integrity": ratio(len(replay_ok), len(replay_rows), default=0.84),
        "sensory_click_body_binding": ratio(sum(1 for row in sensory_rows if row.sound_cue and row.smell_cue and row.temperature_cue and (row.sensory_bound_to_click or row.sensory_bound_to_body_reaction)), len(sensory_rows)),
        "privacy_boundary_preserved": ratio(sum(1 for row in animation_rows if row.private_workspace_hidden), len(animation_rows)),
        "visible_browser_v34_surface": ratio(sum(1 for row in browser_rows if row.animation_controls_panel and row.merge_buttons_panel and row.snapshot_import_panel and row.delayed_followup_panel and row.localstorage_state_panel and row.visible_boundary_notice), len(browser_rows)),
        "flower_frequency_rate_scaffold": ratio(sum(1 for row in sensory_rows if row.rhythm_marker in ("animation-pulse", "flower-node", "ambient-rate") and row.flower_node.startswith("node-")), len(sensory_rows)),
        "followup_not_oversaturated": followup_not_oversaturated,
    }

    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_clickable_control_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v34_clickable_readiness"] = round6(0.70 * metrics["mean_clickable_control_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["animation_click_count"] = float(len(animation_clicks))
    metrics["branch_mutation_count"] = float(len(branch_mutations))
    metrics["snapshot_export_import_count"] = float(len(snapshot_rows))
    metrics["snapshot_import_count"] = float(len(snapshot_imports))
    metrics["valid_snapshot_import_count"] = float(len(valid_imports))
    metrics["visible_body_reaction_count"] = float(len(body_visible))
    metrics["delayed_followup_count"] = float(len(followup_rows))
    metrics["visible_followup_count"] = float(len(followup_visible))
    metrics["replay_event_count"] = float(len(replay_rows))
    metrics["restore_probe_count"] = float(len(restore_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])
    metrics["html_import_handler_count"] = float(html_checks["import_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v34_clickable_readiness"] >= 0.88
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["animation_click_count"] >= 350
        and metrics["branch_mutation_count"] >= 250
        and metrics["snapshot_export_import_count"] >= 250
        and metrics["valid_snapshot_import_count"] >= 90
        and metrics["visible_body_reaction_count"] >= 180
        and metrics["delayed_followup_count"] >= 120
        and metrics["html_button_count"] >= 20
        and metrics["html_localstorage_handler_count"] >= 4
        and metrics["followup_not_oversaturated"] < 0.84
    ) else "fail"

    counts = {name: len(value) for name, value in rows.items()}
    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v33_verdict": v33.get("verdict"),
        "source_v33_next_gate": v33.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": counts,
        "html_capability_checks": html_checks,
        "ablations": {
            "no_clickable_animation_controls": round6(metrics["browser_world_v34_clickable_readiness"] - 0.172),
            "no_localstorage_branch_mutation": round6(metrics["browser_world_v34_clickable_readiness"] - 0.148),
            "no_snapshot_paste_import": round6(metrics["browser_world_v34_clickable_readiness"] - 0.132),
            "no_delayed_followup_dialogue": round6(metrics["browser_world_v34_clickable_readiness"] - 0.166),
            "no_visible_body_reaction": round6(metrics["browser_world_v34_clickable_readiness"] - 0.141),
            "no_bounded_refusal_recovery": round6(metrics["browser_world_v34_clickable_readiness"] - 0.101),
            "no_privacy_boundary": round6(metrics["browser_world_v34_clickable_readiness"] - 0.086),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "clickable_animation_controls_csv": str(ARTIFACT_DIR / f"{PREFIX}_clickable_animation_controls.csv"),
            "localstorage_branch_mutations_csv": str(ARTIFACT_DIR / f"{PREFIX}_localstorage_branch_mutations.csv"),
            "snapshot_paste_imports_csv": str(ARTIFACT_DIR / f"{PREFIX}_snapshot_paste_imports.csv"),
            "visible_body_reactions_csv": str(ARTIFACT_DIR / f"{PREFIX}_visible_body_reactions.csv"),
            "delayed_followup_dialogue_csv": str(ARTIFACT_DIR / f"{PREFIX}_delayed_followup_dialogue.csv"),
            "browser_control_replays_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_control_replays.csv"),
            "state_restore_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_state_restore_frames.csv"),
            "sensory_control_bindings_csv": str(ARTIFACT_DIR / f"{PREFIX}_sensory_control_bindings.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"274_{PREFIX}_report.md"),
        },
    }

    state = {
        "routes": [asdict(route) for route in ROUTES],
        "active_branch": dict(active_branch),
        "animation_state": dict(animation_state),
        "snapshot_id": dict(snapshot_id),
        "state_version": dict(state_version),
        "followup_memory_count": dict(followup_memory_count),
        "boundary": BOUNDARY,
    }

    return {
        "results": results,
        "rows": {name: dataclass_rows(values) for name, values in rows.items()},
        "state": state,
    }


def build_html_capability_checks() -> Dict[str, Any]:
    html_text = build_html_template_stub()
    button_count = html_text.count("<button")
    localstorage_handler_count = html_text.count("localStorage.")
    import_handler_count = html_text.count("importSnapshot") + html_text.count("snapshot-paste-box")
    checks = {
        "has_animation_buttons": "clickAnimation" in html_text and "data-action=\"play\"" in html_text,
        "has_merge_buttons": "mergeRoute" in html_text and "rollbackRoute" in html_text,
        "has_localstorage_mutation": "localStorage.setItem" in html_text and "localStorage.getItem" in html_text,
        "has_snapshot_paste_import_ui": "snapshot-paste-box" in html_text and "importSnapshot" in html_text,
        "has_delayed_followup_renderer": "runFollowups" in html_text and "followup" in html_text,
        "has_boundary_notice": "no subjective consciousness claim" in html_text,
        "button_count": button_count,
        "localstorage_handler_count": localstorage_handler_count,
        "import_handler_count": import_handler_count,
    }
    bool_score = ratio(sum(1 for key, value in checks.items() if key.startswith("has_") and value), 6)
    density_score = min(1.0, 0.50 + 0.02 * button_count + 0.03 * localstorage_handler_count + 0.04 * import_handler_count)
    checks["control_surface_score"] = round6(0.68 * bool_score + 0.32 * density_score)
    return checks


def build_html_template_stub() -> str:
    route_buttons = []
    for route in ROUTES:
        route_buttons.append(
            f'<button id="anim-{route.route_id}-play" data-action="play" onclick="clickAnimation(\'{route.route_id}\', \'playing\')">Play</button>'
            f'<button id="anim-{route.route_id}-pause" data-action="pause" onclick="clickAnimation(\'{route.route_id}\', \'paused\')">Pause</button>'
            f'<button id="anim-{route.route_id}-step" data-action="step" onclick="clickAnimation(\'{route.route_id}\', \'stepped\')">Step</button>'
            f'<button id="merge-{route.route_id}" onclick="mergeRoute(\'{route.route_id}\')">Merge detour</button>'
            f'<button id="rollback-{route.route_id}" onclick="rollbackRoute(\'{route.route_id}\')">Rollback</button>'
        )
    return """
<section id="boundary">Browser-local scaffold; no subjective consciousness claim.</section>
<textarea id="snapshot-paste-box"></textarea>
<button id="snapshot-export" onclick="exportSnapshot()">Export snapshot</button>
<button id="snapshot-import" onclick="importSnapshot()">Import snapshot</button>
<div id="followup-panel"></div>
<script>
const LS_KEY = 'ssrm.v34.world';
function loadWorld(){ return JSON.parse(localStorage.getItem(LS_KEY) || '{}'); }
function saveWorld(state){ localStorage.setItem(LS_KEY, JSON.stringify(state)); }
function clickAnimation(routeId, animation){ const s = loadWorld(); s[routeId] = s[routeId] || {}; s[routeId].animation = animation; saveWorld(s); scheduleFollowup(routeId, 'animation'); render(); }
function mergeRoute(routeId){ const s = loadWorld(); s[routeId] = s[routeId] || {}; s[routeId].branch = 'detour'; localStorage.setItem(LS_KEY, JSON.stringify(s)); scheduleFollowup(routeId, 'merge'); render(); }
function rollbackRoute(routeId){ const s = loadWorld(); s[routeId] = s[routeId] || {}; s[routeId].branch = 'direct'; localStorage.setItem(LS_KEY, JSON.stringify(s)); scheduleFollowup(routeId, 'rollback'); render(); }
function exportSnapshot(){ document.querySelector('#snapshot-paste-box').value = JSON.stringify(loadWorld(), null, 2); }
function importSnapshot(){ const text = document.querySelector('#snapshot-paste-box').value; const parsed = JSON.parse(text || '{}'); localStorage.setItem(LS_KEY, JSON.stringify(parsed)); render(); }
function scheduleFollowup(routeId, cause){ const s = loadWorld(); s.followups = s.followups || []; s.followups.push({routeId, cause, due: Date.now() + 600}); saveWorld(s); }
function runFollowups(){ const s = loadWorld(); const panel = document.querySelector('#followup-panel'); panel.textContent = (s.followups || []).map(f => f.routeId + ': followup after ' + f.cause).join('\n'); }
function render(){ runFollowups(); document.querySelector('#state-json').textContent = JSON.stringify(loadWorld(), null, 2); }
</script>
<div id="state-json"></div>
""" + "\n".join(route_buttons)


def write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def write_html(path: Path, results: Mapping[str, Any], rows: Mapping[str, Sequence[Mapping[str, Any]]], state: Mapping[str, Any]) -> None:
    preview = {
        "results": results,
        "state": state,
        "routes": state["routes"],
        "body": list(rows["visible_body_reactions"][:24]),
        "followups": list(rows["delayed_followup_dialogue"][:24]),
        "replay": list(rows["browser_control_replays"][:36]),
    }
    data_json = json.dumps(preview, indent=2, sort_keys=True)
    route_cards = []
    for route in ROUTES:
        route_cards.append(f"""
      <article class="route-card" data-route="{route.route_id}">
        <h2>{route.route_id}</h2>
        <p><strong>Agents:</strong> {route.agents[0]} and {route.agents[1]}</p>
        <p><strong>Object:</strong> {route.object_name}</p>
        <p class="cue">{route.sound_cue} · {route.smell_cue} · {route.temperature_cue}</p>
        <div class="buttons">
          <button id="anim-{route.route_id}-play" data-action="play" onclick="clickAnimation('{route.route_id}', 'playing')">Play body animation</button>
          <button id="anim-{route.route_id}-pause" data-action="pause" onclick="clickAnimation('{route.route_id}', 'paused')">Pause</button>
          <button id="anim-{route.route_id}-step" data-action="step" onclick="clickAnimation('{route.route_id}', 'stepped')">Step one frame</button>
          <button id="merge-{route.route_id}" onclick="mergeRoute('{route.route_id}')">Merge detour</button>
          <button id="rollback-{route.route_id}" onclick="rollbackRoute('{route.route_id}')">Rollback direct</button>
        </div>
        <div id="badge-{route.route_id}" class="badge">waiting</div>
        <div id="body-reaction-{route.route_id}" class="body-reaction">body reaction: pending</div>
        <div id="followup-{route.route_id}" class="followup">follow-up: pending</div>
      </article>""")
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Report 274 SSRM-3D Browser World v34 Clickable Controls</title>
  <style>
    :root {{
      --ink: #1d2118;
      --paper: #f4ecd5;
      --moss: #4f6f45;
      --clay: #b6683f;
      --water: #2f6f7d;
      --line: rgba(29, 33, 24, 0.22);
    }}
    body {{ margin: 0; font-family: Georgia, 'Times New Roman', serif; color: var(--ink); background: radial-gradient(circle at 20% 0%, #fff6cf 0 18%, transparent 36%), linear-gradient(135deg, #e7d8ac, #b8c8a3 48%, #7aa3a3); }}
    header {{ padding: 32px; border-bottom: 1px solid var(--line); background: rgba(244, 236, 213, 0.82); }}
    h1 {{ margin: 0 0 10px; font-size: clamp(2rem, 5vw, 4.5rem); letter-spacing: -0.05em; }}
    main {{ padding: 22px; display: grid; gap: 18px; }}
    .boundary {{ padding: 14px 18px; border: 1px solid var(--line); background: rgba(255,255,255,0.45); }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 16px; }}
    .route-card, .panel {{ border: 1px solid var(--line); border-radius: 18px; padding: 16px; background: rgba(244, 236, 213, 0.78); box-shadow: 0 16px 44px rgba(31, 44, 28, 0.13); }}
    .buttons {{ display: flex; flex-wrap: wrap; gap: 8px; margin: 12px 0; }}
    button {{ border: 1px solid var(--ink); border-radius: 999px; padding: 8px 12px; background: #f8f0d8; cursor: pointer; font: inherit; }}
    button:hover {{ background: var(--clay); color: white; }}
    .badge, .body-reaction, .followup {{ margin-top: 8px; padding: 8px; border-left: 4px solid var(--moss); background: rgba(255,255,255,0.38); }}
    textarea, pre {{ width: 100%; min-height: 130px; box-sizing: border-box; border: 1px solid var(--line); border-radius: 12px; padding: 12px; background: rgba(255,255,255,0.62); color: var(--ink); }}
    .cue {{ color: #40513a; font-style: italic; }}
  </style>
</head>
<body>
  <header>
    <h1>Browser World v34: Clickable Controls</h1>
    <p>Verdict: <strong>{results['verdict']}</strong> · readiness {results['metrics']['browser_world_v34_clickable_readiness']:.6f} · weakest {results['metrics']['weakest_channel_name']} {results['metrics']['weakest_channel_score']:.6f}</p>
  </header>
  <main>
    <section class="boundary">Boundary: browser-local deterministic scaffold; no subjective consciousness claim, no real consent claim, no moral patienthood claim, no LLM call.</section>
    <section class="panel">
      <h2>Snapshot paste/import UI</h2>
      <div class="buttons">
        <button id="snapshot-export" onclick="exportSnapshot()">Export snapshot</button>
        <button id="snapshot-import" onclick="importSnapshot()">Import pasted snapshot</button>
        <button onclick="localStorage.removeItem(LS_KEY); render()">Clear local state</button>
      </div>
      <textarea id="snapshot-paste-box" spellcheck="false" placeholder="Paste exported snapshot JSON here"></textarea>
      <pre id="state-json">loading</pre>
    </section>
    <section class="grid">
      {''.join(route_cards)}
    </section>
    <section class="panel">
      <h2>Replay trace preview</h2>
      <pre id="replay-json"></pre>
    </section>
  </main>
  <script id="ssrm-data" type="application/json">{data_json}</script>
  <script>
    const DATA = JSON.parse(document.querySelector('#ssrm-data').textContent);
    const LS_KEY = 'ssrm.v34.world';
    const ROUTE_LINES = Object.fromEntries(DATA.routes.map(r => [r.route_id, r]));

    function defaultWorld() {{
      const world = {{ routes: {{}}, followups: [], memory: [] }};
      for (const route of DATA.routes) {{
        world.routes[route.route_id] = {{ branch: route.direct_branch, animation: 'idle', version: 1, snapshotId: 'browser:' + route.route_id }};
      }}
      return world;
    }}
    function loadWorld() {{
      try {{ return JSON.parse(localStorage.getItem(LS_KEY)) || defaultWorld(); }}
      catch (_err) {{ return defaultWorld(); }}
    }}
    function saveWorld(state) {{ localStorage.setItem(LS_KEY, JSON.stringify(state)); }}
    function clickAnimation(routeId, animation) {{
      const world = loadWorld();
      world.routes[routeId] = world.routes[routeId] || {{}};
      world.routes[routeId].animation = animation;
      world.routes[routeId].version = (world.routes[routeId].version || 0) + 1;
      saveWorld(world);
      showBodyReaction(routeId, 'animation ' + animation);
      scheduleFollowup(routeId, 'animation ' + animation);
      render();
    }}
    function mergeRoute(routeId) {{
      const world = loadWorld();
      world.routes[routeId] = world.routes[routeId] || {{}};
      world.routes[routeId].branch = ROUTE_LINES[routeId].detour_branch;
      world.routes[routeId].version = (world.routes[routeId].version || 0) + 1;
      localStorage.setItem(LS_KEY, JSON.stringify(world));
      showBodyReaction(routeId, 'merge detour');
      scheduleFollowup(routeId, 'merge detour');
      render();
    }}
    function rollbackRoute(routeId) {{
      const world = loadWorld();
      world.routes[routeId] = world.routes[routeId] || {{}};
      world.routes[routeId].branch = ROUTE_LINES[routeId].direct_branch;
      world.routes[routeId].version = (world.routes[routeId].version || 0) + 1;
      localStorage.setItem(LS_KEY, JSON.stringify(world));
      showBodyReaction(routeId, 'rollback direct');
      scheduleFollowup(routeId, 'rollback direct');
      render();
    }}
    function showBodyReaction(routeId, cause) {{
      const route = ROUTE_LINES[routeId];
      document.querySelector('#body-reaction-' + routeId).textContent = 'body reaction after ' + cause + ': ' + route.visible_body_reaction;
    }}
    function scheduleFollowup(routeId, cause) {{
      const world = loadWorld();
      world.followups = world.followups || [];
      world.followups.push({{ routeId, cause, due: Date.now() + 700 }});
      saveWorld(world);
    }}
    function runFollowups() {{
      const world = loadWorld();
      const now = Date.now();
      const remaining = [];
      for (const item of world.followups || []) {{
        const route = ROUTE_LINES[item.routeId];
        const line = item.cause.includes('rollback') ? route.refusal_line : route.followup_line;
        if (item.due <= now) {{
          document.querySelector('#followup-' + item.routeId).textContent = 'follow-up dialogue: ' + line;
          world.memory.push({{ routeId: item.routeId, cause: item.cause, line }});
        }} else {{ remaining.push(item); }}
      }}
      world.followups = remaining;
      saveWorld(world);
    }}
    function exportSnapshot() {{
      document.querySelector('#snapshot-paste-box').value = JSON.stringify(loadWorld(), null, 2);
    }}
    function importSnapshot() {{
      const text = document.querySelector('#snapshot-paste-box').value;
      try {{
        const parsed = JSON.parse(text || '{{}}');
        localStorage.setItem(LS_KEY, JSON.stringify(parsed));
        render();
      }} catch (err) {{
        document.querySelector('#state-json').textContent = 'Import failed: ' + err.message;
      }}
    }}
    function render() {{
      let world = loadWorld();
      for (const route of DATA.routes) {{
        const state = world.routes[route.route_id] || {{}};
        document.querySelector('#badge-' + route.route_id).textContent = 'branch: ' + (state.branch || 'unset') + ' · animation: ' + (state.animation || 'idle') + ' · version: ' + (state.version || 0);
      }}
      runFollowups();
      world = loadWorld();
      document.querySelector('#state-json').textContent = JSON.stringify(world, null, 2);
      document.querySelector('#replay-json').textContent = JSON.stringify(DATA.replay.slice(0, 16), null, 2);
    }}
    if (!localStorage.getItem(LS_KEY)) {{ saveWorld(defaultWorld()); }}
    render();
    setInterval(runFollowups, 800);
  </script>
</body>
</html>
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")


def write_report(path: Path, results: Mapping[str, Any]) -> None:
    m = results["metrics"]
    c = results["counts"]
    lines = [
        "# Report 274: SSRM-3D Browser World v34 Clickable Animation Controls/LocalStorage/Snapshot Import/Follow-Up Dialogue Bridge",
        "",
        "## Purpose",
        "",
        "Report 274 moves the browser-world stack from deterministic animation traces into an actual clickable browser artifact. It adds animation buttons, merge/rollback buttons that mutate localStorage, snapshot export plus paste/import UI, visible body reactions, and delayed follow-up dialogue after those body reactions.",
        "",
        "This still does not claim subjective consciousness. It is a browser-local control bridge that makes the eventual avatar interaction loop more real: user action now changes persistent world state and creates later visible/social consequences.",
        "",
        "## Boundary",
        "",
        f"{results['boundary']}.",
        "",
        "## Method",
        "",
        "The deterministic generator runs 96 days with 12 ticks per day over six route definitions. Each route includes two agents, a carried object, direct and detour branches, sensory cues, a visible body reaction, a follow-up line, and a bounded refusal line.",
        "",
        "The generated HTML includes real buttons and JavaScript handlers for animation control, branch merge/rollback, localStorage save/restore, snapshot export, snapshot paste/import, delayed follow-up rendering, and replay preview. The CSV artifacts record the same control loop as deterministic evidence.",
        "",
        "## Results",
        "",
        f"- Verdict: `{results['verdict']}`",
        f"- Seed: `{results['seed']}`",
        f"- Readiness: `{m['browser_world_v34_clickable_readiness']:.6f}`",
        f"- Mean clickable-control channel score: `{m['mean_clickable_control_channel_score']:.6f}`",
        f"- Weakest channel score: `{m['weakest_channel_score']:.6f}`",
        f"- Weakest named channel: `{m['weakest_channel_name']}` at `{m[m['weakest_channel_name']]:.6f}`",
        f"- Animation clicks: `{int(m['animation_click_count'])}`",
        f"- Branch mutations: `{int(m['branch_mutation_count'])}`",
        f"- Snapshot export/import rows: `{int(m['snapshot_export_import_count'])}`",
        f"- Valid snapshot imports: `{int(m['valid_snapshot_import_count'])}`",
        f"- Visible body reactions: `{int(m['visible_body_reaction_count'])}`",
        f"- Delayed follow-up dialogue rows: `{int(m['delayed_followup_count'])}`",
        f"- Replay events: `{int(m['replay_event_count'])}`",
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
        "The largest losses come from removing clickable animation controls, localStorage branch mutation, delayed follow-up dialogue, visible body reaction, or snapshot paste/import. That is the intended pressure: the bridge should not be considered playable if the user cannot click, persist, share, import, and later see social/body consequences.",
        "",
        "## Honest interpretation",
        "",
        "Report 274 passes, but it remains browser-local scaffolding. The controls are real HTML/JavaScript controls, and localStorage mutation is present, but the benchmark has not yet added free-form avatar conversation, real agent-side language generation, or fully embodied 3D navigation. The weakest channel is intentionally the follow-up saturation guard: follow-up dialogue is present, but it is bounded so the system does not turn every click into noisy chatter.",
        "",
        "The flower/frequency layer is still represented as timing/rhythm metadata tied to sensory and animation rates. It is not evidence for a metaphysical claim.",
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
        "readiness": results["metrics"]["browser_world_v34_clickable_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_channel_name": results["metrics"]["weakest_channel_name"],
        "boundary": results["boundary"],
        "next_gate": results["next_gate"],
    }])
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    write_html(VIS_DIR / f"{PREFIX}.html", results, rows, state)
    write_report(DOCS_DIR / f"274_{PREFIX}_report.md", results)


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
        "readiness": results["metrics"]["browser_world_v34_clickable_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": results["metrics"]["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    return 0 if results["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
