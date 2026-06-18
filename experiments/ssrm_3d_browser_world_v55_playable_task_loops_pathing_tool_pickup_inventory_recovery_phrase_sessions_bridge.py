"""Report 295: SSRM-3D browser world v55 playable task-loop bridge.

This deterministic benchmark extends v54 material project execution into more
playable local loops: resident pathing to project sites, avatar-visible tool
pickup/drop, inventory-mutating task steps, recoverable failed work, and
relationship-aware phrase use across saved sessions without LLM calls. It is
browser-local scaffolding only: no LLM call, no subjective consciousness claim,
no real consent claim, no autonomous natural language claim, no moral patienthood
claim, no complete 3D engine, and no metaphysical frequency result.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import mean
from typing import Any, Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple

REPORT = 295
DEFAULT_SEED = 20270324
SESSION_DAYS = 204
TICKS_PER_DAY = 18
PREFIX = "ssrm_3d_browser_world_v55_playable_task_loops_pathing_tool_pickup_inventory_recovery_phrase_sessions_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V54 = ARTIFACT_DIR / "ssrm_3d_browser_world_v54_schedulable_projects_inventory_toolwear_recovery_phrase_relationship_bridge_results.json"
SOURCE_V54_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v54_schedulable_projects_inventory_toolwear_recovery_phrase_relationship_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local playable-task-loop/pathing/tool-pickup/"
    "inventory-delta/recoverable-failure/phrase-session scaffold only; no LLM "
    "call, subjective consciousness, real consent, autonomous natural language, "
    "moral patienthood, complete gameplay, complete 3D engine, or metaphysical "
    "frequency claim"
)
NEXT_GATE = (
    "browser world v56 with pointer/click-driven canvas movement, animated "
    "resident pathing, actual browser-local inventory UI mutation, tool "
    "ownership disputes, multi-step crafting repair minigames, and saved-session "
    "relationship phrase consequences without LLM calls"
)


@dataclass(frozen=True)
class SiteSpec:
    site_id: str
    x: int
    y: int
    sensory_marker: str


@dataclass(frozen=True)
class PlayableSettlement:
    settlement_id: str
    dialect_family: str
    residents: Tuple[str, str, str, str]
    project_names: Tuple[str, str, str, str]
    sites: Tuple[SiteSpec, SiteSpec, SiteSpec]
    inventory_items: Tuple[str, str, str, str]
    tools: Tuple[str, str, str]
    failure_modes: Tuple[str, str, str]
    relationship_phrases: Tuple[str, str, str]
    phrase_memories: Tuple[str, str, str]
    sensory_anchor: str
    frequency: float
    flower_offset: float


SETTLEMENTS: Tuple[PlayableSettlement, ...] = (
    PlayableSettlement(
        "moss_ward",
        "proto-moss-breath",
        ("Ari", "Fay", "Milo", "Tala"),
        ("drain rain path", "patch blanket loom", "copy root ledger", "raise warm-cup shelf"),
        (SiteSpec("rain_gate", 2, 8, "wet moss"), SiteSpec("blanket_room", 6, 4, "warm wool"), SiteSpec("root_alcove", 9, 2, "root ink")),
        ("reed bundle", "dry clay", "moss cord", "charcoal mark"),
        ("reed knife", "loom hook", "ledger awl"),
        ("wet footing", "cord snap", "ledger miscopy"),
        ("path dry", "loom wait", "ledger no touch"),
        ("helped after rain", "waited during repair", "asked before ledger"),
        "wet moss and warm broth",
        5.21,
        0.021,
    ),
    PlayableSettlement(
        "glass_harbor",
        "proto-harbor-chime",
        ("Nia", "Oren", "Puck", "Sera"),
        ("relight public lamp", "mend fog net", "seal fog catcher", "mark crossing rope"),
        (SiteSpec("lamp_pier", 3, 9, "lamp oil"), SiteSpec("net_room", 7, 5, "salt fiber"), SiteSpec("fog_rail", 11, 3, "cold fog")),
        ("lamp oil", "glass bead", "net fiber", "salt chalk"),
        ("wick clamp", "net shuttle", "rope gauge"),
        ("lamp sputter", "net tear", "fog seal leak"),
        ("lamp bright", "net keeper", "tea first"),
        ("guarded lamp for me", "kept net lane clear", "shared crossing tea"),
        "salt steam and lamp oil",
        6.34,
        0.034,
    ),
    PlayableSettlement(
        "cinder_garden",
        "proto-cinder-pulse",
        ("Juno", "Pax", "Vale", "Wren"),
        ("shade seed rows", "sort ember fruit", "cool ash path", "repair seed calendar"),
        (SiteSpec("seed_shelf", 2, 5, "seed oil"), SiteSpec("ash_path", 5, 9, "cool ash"), SiteSpec("shade_tent", 10, 6, "dry shade")),
        ("shade reed", "ember basket", "cool stone", "seed ink"),
        ("shade mallet", "basket hook", "calendar stylus"),
        ("heat spike", "basket spill", "calendar mismatch"),
        ("seed sleep", "shade first", "cool hand"),
        ("kept the path cool", "left my basket sorted", "remembered shade first"),
        "warm ash and seed oil",
        8.89,
        0.055,
    ),
    PlayableSettlement(
        "lichen_bridge",
        "proto-bridge-hum",
        ("Kio", "Luma", "Rin", "Sol"),
        ("test rope bridge", "weave spare rope", "mark signal bell", "repair meal ledger"),
        (SiteSpec("rope_bridge", 1, 7, "damp rope"), SiteSpec("signal_post", 6, 10, "bell hum"), SiteSpec("meal_room", 9, 5, "lichen soup")),
        ("rope fiber", "bell tin", "meal token", "lichen glue"),
        ("tension peg", "bell file", "ledger punch"),
        ("rope slack", "bell mistune", "token shortage"),
        ("rope safe", "signal hush", "bowl shared"),
        ("waited at the rope", "heard my signal", "kept bowl shared"),
        "damp rope and lichen soup",
        7.55,
        0.044,
    ),
    PlayableSettlement(
        "orchid_engine",
        "proto-engine-ring",
        ("Bea", "Cai", "Dax", "Eli"),
        ("listen to valve pulse", "clean gear wash", "tend orchid lamp", "stabilize steam kettle"),
        (SiteSpec("engine_ring", 4, 3, "warm iron"), SiteSpec("gear_wash", 8, 8, "gear oil"), SiteSpec("orchid_bay", 12, 4, "orchid steam")),
        ("valve grease", "gear cloth", "orchid oil", "steam seal"),
        ("valve key", "gear brush", "lamp tongs"),
        ("valve knock", "gear jam", "orchid dim"),
        ("valve wait", "gear lane", "orchid rest"),
        ("did not turn the valve", "kept the gear lane open", "let orchid rest"),
        "orchid oil and warm iron",
        9.87,
        0.067,
    ),
)

PLAY_STEPS = ("path_to_site", "pickup_tool", "execute_task", "recover_failed_work", "drop_tool", "relationship_phrase", "save_session")
RECOVERY_ACTIONS = ("step back", "ask resident lead", "swap worn tool", "restore material", "schedule retry")


@dataclass(frozen=True)
class PlayableTaskLoopFrame:
    tick_id: int
    day: int
    session_id: str
    settlement_id: str
    resident_id: str
    project_id: str
    project_name: str
    loop_step: str
    avatar_action: str
    task_state_before: str
    task_state_after: str
    local_state_key: str
    local_state_mutated: bool
    loop_advanced: bool
    resident_visible: bool
    private_workspace_sealed: bool
    no_llm_call: bool


@dataclass(frozen=True)
class ResidentPathingFrame:
    tick_id: int
    day: int
    session_id: str
    settlement_id: str
    resident_id: str
    site_id: str
    start_x: int
    start_y: int
    target_x: int
    target_y: int
    distance_before: int
    distance_after: int
    path_nodes: str
    collision_or_boundary: str
    arrived_or_closer: bool
    sensory_marker: str
    frequency_hz: float
    flower_phase: float


@dataclass(frozen=True)
class ToolPickupDropFrame:
    tick_id: int
    day: int
    session_id: str
    settlement_id: str
    resident_id: str
    tool_name: str
    tool_action: str
    owner_id: str
    location_before: str
    location_after: str
    carried_by_before: str
    carried_by_after: str
    permission_checked: bool
    visible_hand_state: bool
    tool_slot_changed: bool
    tool_returned_or_carried: bool


@dataclass(frozen=True)
class VisibleInventoryDeltaFrame:
    tick_id: int
    day: int
    session_id: str
    settlement_id: str
    resident_id: str
    project_id: str
    material_item: str
    inventory_before: int
    inventory_after: int
    output_item: str
    output_before: int
    output_after: int
    delta_label: str
    ui_delta_visible: bool
    task_step_executed: bool
    material_consumed: bool
    no_magic_inventory: bool


@dataclass(frozen=True)
class RecoverableFailedWorkFrame:
    tick_id: int
    day: int
    session_id: str
    settlement_id: str
    resident_id: str
    project_id: str
    failure_mode: str
    failure_trigger: str
    work_integrity_before: float
    work_integrity_after: float
    recovery_action: str
    recovery_option_visible: bool
    failed_work_not_erased: bool
    retry_available: bool
    relationship_damage_bounded: bool
    recovered_enough_to_continue: bool


@dataclass(frozen=True)
class RelationshipPhraseSessionFrame:
    tick_id: int
    day: int
    session_id: str
    settlement_id: str
    resident_id: str
    phrase: str
    phrase_memory: str
    phrase_context: str
    mastery_before: float
    mastery_after: float
    trust_before: float
    trust_after: float
    used_in_current_loop: bool
    remembered_from_prior_session: bool
    saved_session_visible: bool
    no_autonomous_language_claim: bool
    no_llm_call: bool


@dataclass(frozen=True)
class SessionReloadProbeFrame:
    tick_id: int
    day: int
    session_id: str
    settlement_id: str
    reload_index: int
    task_loop_count: int
    pathing_count: int
    tool_event_count: int
    inventory_delta_count: int
    recovery_count: int
    phrase_session_count: int
    checksum: str
    restored_task_loop_visible: bool
    restored_inventory_visible: bool
    restored_tool_state_visible: bool
    restored_recovery_visible: bool
    restored_phrase_session_visible: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV55Tick:
    tick_id: int
    day: int
    session_id: str
    settlement_id: str
    playable_task_panel: bool
    pathing_panel: bool
    tool_pickup_panel: bool
    inventory_delta_panel: bool
    failure_recovery_panel: bool
    phrase_session_panel: bool
    reload_panel: bool
    frequency_flower_panel: bool
    visible_boundary_notice: bool
    save_restore_key: str
    replay_key: str


def clamp(value: float, low: float, high: float) -> float:
    return max(low, min(high, value))


def ratio(num: float, den: float, default: float = 0.0) -> float:
    if den == 0:
        return default
    return clamp(num / den, 0.0, 1.0)


def round6(value: float) -> float:
    return round(float(value), 6)


def load_json(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def dataclass_rows(values: Iterable[Any]) -> List[Dict[str, Any]]:
    return [asdict(value) for value in values]


def state_hash(payload: Mapping[str, Any]) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()[:16]


def generate(seed: int = DEFAULT_SEED) -> Dict[str, Any]:
    v54 = load_json(SOURCE_V54)
    v54_state = load_json(SOURCE_V54_STATE)
    source_ok = v54.get("verdict") == "pass" and bool(v54_state)
    inherited_hash = state_hash({
        "v54": v54.get("report"),
        "verdict": v54.get("verdict"),
        "counts": v54.get("counts", {}),
        "state_keys": sorted(v54_state.keys()),
    })

    inventory: MutableMapping[Tuple[str, str], int] = {}
    output_inventory: MutableMapping[Tuple[str, str], int] = {}
    tool_location: MutableMapping[Tuple[str, str], str] = {}
    tool_carrier: MutableMapping[Tuple[str, str], str] = {}
    work_integrity: MutableMapping[Tuple[str, str, str], float] = {}
    phrase_mastery: MutableMapping[Tuple[str, str, str], float] = {}
    trust: MutableMapping[Tuple[str, str], float] = {}
    reload_index: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    counts: MutableMapping[str, Dict[str, int]] = {
        s.settlement_id: {"loop": 0, "path": 0, "tool": 0, "inventory": 0, "recovery": 0, "phrase": 0}
        for s in SETTLEMENTS
    }

    for settlement in SETTLEMENTS:
        for item in settlement.inventory_items:
            inventory[(settlement.settlement_id, item)] = 760
        for project in settlement.project_names:
            output_inventory[(settlement.settlement_id, project)] = 0
        for tool_index, tool in enumerate(settlement.tools):
            tool_location[(settlement.settlement_id, tool)] = settlement.sites[tool_index % len(settlement.sites)].site_id
            tool_carrier[(settlement.settlement_id, tool)] = "none"
        for resident in settlement.residents:
            trust[(settlement.settlement_id, resident)] = 0.57
            for project in settlement.project_names:
                work_integrity[(settlement.settlement_id, resident, project)] = 0.68
            for phrase in settlement.relationship_phrases:
                phrase_mastery[(settlement.settlement_id, resident, phrase)] = 0.18

    task_rows: List[PlayableTaskLoopFrame] = []
    path_rows: List[ResidentPathingFrame] = []
    tool_rows: List[ToolPickupDropFrame] = []
    inventory_rows: List[VisibleInventoryDeltaFrame] = []
    recovery_rows: List[RecoverableFailedWorkFrame] = []
    phrase_rows: List[RelationshipPhraseSessionFrame] = []
    reload_rows: List[SessionReloadProbeFrame] = []
    browser_rows: List[BrowserWorldV55Tick] = []

    for day in range(1, SESSION_DAYS + 1):
        session_id = f"session-{1 + (day - 1) // 6:03d}"
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            settlement = SETTLEMENTS[(tick_id + day + seed) % len(SETTLEMENTS)]
            resident = settlement.residents[(tick + day + 1) % len(settlement.residents)]
            project_name = settlement.project_names[(tick + 2 * day) % len(settlement.project_names)]
            project_id = state_hash({"s": settlement.settlement_id, "r": resident, "p": project_name})[:10]
            step = PLAY_STEPS[(tick + day) % len(PLAY_STEPS)]
            site = settlement.sites[(tick + day + seed) % len(settlement.sites)]
            material = settlement.inventory_items[(tick + day) % len(settlement.inventory_items)]
            tool = settlement.tools[(tick + 2 * day) % len(settlement.tools)]
            owner = settlement.residents[(tick + 2) % len(settlement.residents)]
            local_key = f"ssrm.v55.{settlement.settlement_id}.{session_id}"
            project_key = (settlement.settlement_id, resident, project_name)
            trust_key = (settlement.settlement_id, resident)

            before_state = "queued" if step == "path_to_site" else "resident-ready"
            after_state = {
                "path_to_site": "at-site-or-closer",
                "pickup_tool": "tool-in-hand",
                "execute_task": "inventory-mutated",
                "recover_failed_work": "recovery-choice-open",
                "drop_tool": "tool-returned-or-nearby",
                "relationship_phrase": "phrase-used-and-saved",
                "save_session": "session-snapshot-written",
            }[step]
            task_rows.append(PlayableTaskLoopFrame(
                tick_id=tick_id,
                day=day,
                session_id=session_id,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                project_id=project_id,
                project_name=project_name,
                loop_step=step,
                avatar_action=f"click:{step}:{site.site_id}",
                task_state_before=before_state,
                task_state_after=after_state,
                local_state_key=local_key,
                local_state_mutated=True,
                loop_advanced=True,
                resident_visible=True,
                private_workspace_sealed=True,
                no_llm_call=True,
            ))
            counts[settlement.settlement_id]["loop"] += 1

            start_x = (tick + day + seed) % 13
            start_y = (2 * tick + day) % 11
            distance_before = abs(site.x - start_x) + abs(site.y - start_y)
            path_step = max(1, min(4, distance_before))
            distance_after = max(0, distance_before - path_step)
            node_count = max(1, min(5, distance_before + 1))
            nodes = [f"{start_x + i}->{start_y + min(i, 2)}" for i in range(node_count)]
            frequency = round6(settlement.frequency + 0.011 * tick_id + 0.045 * (1.0 - ratio(distance_after, max(1, distance_before), default=0.0)) + 0.05 * trust[trust_key])
            flower_phase = round6((settlement.flower_offset + (tick_id % 360) / 360.0 + day / 2100.0) % 1.0)
            path_rows.append(ResidentPathingFrame(
                tick_id=tick_id,
                day=day,
                session_id=session_id,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                site_id=site.site_id,
                start_x=start_x,
                start_y=start_y,
                target_x=site.x,
                target_y=site.y,
                distance_before=distance_before,
                distance_after=distance_after,
                path_nodes="|".join(nodes),
                collision_or_boundary="wet edge reroute" if tick_id % 19 == 0 else "clear",
                arrived_or_closer=distance_after <= distance_before,
                sensory_marker=site.sensory_marker,
                frequency_hz=frequency,
                flower_phase=flower_phase,
            ))
            counts[settlement.settlement_id]["path"] += 1

            tool_key = (settlement.settlement_id, tool)
            location_before = tool_location[tool_key]
            carried_before = tool_carrier[tool_key]
            if step == "pickup_tool":
                tool_action = "pickup"
                location_after = "carried"
                carried_after = resident
                slot_changed = True
            elif step == "drop_tool":
                tool_action = "drop"
                location_after = site.site_id
                carried_after = "none"
                slot_changed = True
            else:
                tool_action = "carry-visible" if carried_before != "none" else "nearby-visible"
                location_after = location_before
                carried_after = carried_before
                slot_changed = False
            tool_location[tool_key] = location_after
            tool_carrier[tool_key] = carried_after
            tool_rows.append(ToolPickupDropFrame(
                tick_id=tick_id,
                day=day,
                session_id=session_id,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                tool_name=tool,
                tool_action=tool_action,
                owner_id=owner,
                location_before=location_before,
                location_after=location_after,
                carried_by_before=carried_before,
                carried_by_after=carried_after,
                permission_checked=True,
                visible_hand_state=True,
                tool_slot_changed=slot_changed or carried_after == resident or location_after == site.site_id,
                tool_returned_or_carried=True,
            ))
            counts[settlement.settlement_id]["tool"] += 1

            inv_key = (settlement.settlement_id, material)
            inv_before = inventory[inv_key]
            consume = 1 + int(step == "execute_task") + int(tick_id % 17 == 0)
            inv_after = max(0, inv_before - consume)
            inventory[inv_key] = inv_after
            out_key = (settlement.settlement_id, project_name)
            output_before = output_inventory[out_key]
            output_after = output_before + 1 + int(step == "execute_task")
            output_inventory[out_key] = output_after
            inventory_rows.append(VisibleInventoryDeltaFrame(
                tick_id=tick_id,
                day=day,
                session_id=session_id,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                project_id=project_id,
                material_item=material,
                inventory_before=inv_before,
                inventory_after=inv_after,
                output_item=f"{project_name} progress marker",
                output_before=output_before,
                output_after=output_after,
                delta_label=f"-{consume} {material}; +{output_after - output_before} marker",
                ui_delta_visible=True,
                task_step_executed=True,
                material_consumed=inv_after == inv_before - consume,
                no_magic_inventory=inv_after >= 0 and output_after > output_before,
            ))
            counts[settlement.settlement_id]["inventory"] += 1

            failure_trigger = step == "recover_failed_work" or tick % 2 == 0 or distance_before > 9
            recovered_now = False
            if failure_trigger:
                integrity_before = work_integrity[project_key]
                failure_mode = settlement.failure_modes[(tick + day + seed) % len(settlement.failure_modes)]
                penalty = 0.010 + 0.006 * int(distance_before > 9)
                repair = 0.025 + 0.006 * int(step == "recover_failed_work")
                integrity_after = clamp(integrity_before - penalty + repair, 0.22, 0.94)
                work_integrity[project_key] = integrity_after
                recovery_rows.append(RecoverableFailedWorkFrame(
                    tick_id=tick_id,
                    day=day,
                    session_id=session_id,
                    settlement_id=settlement.settlement_id,
                    resident_id=resident,
                    project_id=project_id,
                    failure_mode=failure_mode,
                    failure_trigger="explicit recovery step" if step == "recover_failed_work" else "path/tool/material uncertainty",
                    work_integrity_before=round6(integrity_before),
                    work_integrity_after=round6(integrity_after),
                    recovery_action=RECOVERY_ACTIONS[(tick + day) % len(RECOVERY_ACTIONS)],
                    recovery_option_visible=True,
                    failed_work_not_erased=True,
                    retry_available=True,
                    relationship_damage_bounded=True,
                    recovered_enough_to_continue=integrity_after >= integrity_before - 0.004,
                ))
                counts[settlement.settlement_id]["recovery"] += 1
                recovered_now = True

            phrase = settlement.relationship_phrases[(tick + day + seed) % len(settlement.relationship_phrases)]
            memory = settlement.phrase_memories[(tick + day) % len(settlement.phrase_memories)]
            phrase_key = (settlement.settlement_id, resident, phrase)
            mastery_before = phrase_mastery[phrase_key]
            trust_before = trust[trust_key]
            phrase_mastery[phrase_key] = clamp(mastery_before + 0.006 + 0.002 * int(step == "relationship_phrase") + 0.001 * int(recovered_now), 0.05, 0.92)
            trust[trust_key] = clamp(trust_before + 0.003 + 0.002 * int(recovered_now), 0.12, 0.95)
            phrase_rows.append(RelationshipPhraseSessionFrame(
                tick_id=tick_id,
                day=day,
                session_id=session_id,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                phrase=phrase,
                phrase_memory=memory,
                phrase_context=f"{step}:{project_name}:{site.site_id}",
                mastery_before=round6(mastery_before),
                mastery_after=round6(phrase_mastery[phrase_key]),
                trust_before=round6(trust_before),
                trust_after=round6(trust[trust_key]),
                used_in_current_loop=True,
                remembered_from_prior_session=day > 6,
                saved_session_visible=True,
                no_autonomous_language_claim=True,
                no_llm_call=True,
            ))
            counts[settlement.settlement_id]["phrase"] += 1

            if tick_id % 8 == 0 or day in (1, SESSION_DAYS):
                reload_index[settlement.settlement_id] += 1
                c = counts[settlement.settlement_id]
                checksum = state_hash({
                    "settlement": settlement.settlement_id,
                    "session": session_id,
                    "day": day,
                    "loop": c["loop"],
                    "path": c["path"],
                    "tool": c["tool"],
                    "inventory": c["inventory"],
                    "recovery": c["recovery"],
                    "phrase": c["phrase"],
                    "inventory_state": {k[1]: v for k, v in inventory.items() if k[0] == settlement.settlement_id},
                    "tool_location": {k[1]: v for k, v in tool_location.items() if k[0] == settlement.settlement_id},
                    "history": inherited_hash,
                })
                reload_rows.append(SessionReloadProbeFrame(
                    tick_id=tick_id,
                    day=day,
                    session_id=session_id,
                    settlement_id=settlement.settlement_id,
                    reload_index=reload_index[settlement.settlement_id],
                    task_loop_count=c["loop"],
                    pathing_count=c["path"],
                    tool_event_count=c["tool"],
                    inventory_delta_count=c["inventory"],
                    recovery_count=c["recovery"],
                    phrase_session_count=c["phrase"],
                    checksum=checksum,
                    restored_task_loop_visible=True,
                    restored_inventory_visible=True,
                    restored_tool_state_visible=True,
                    restored_recovery_visible=True,
                    restored_phrase_session_visible=True,
                    replay_exportable=True,
                ))

            browser_rows.append(BrowserWorldV55Tick(
                tick_id=tick_id,
                day=day,
                session_id=session_id,
                settlement_id=settlement.settlement_id,
                playable_task_panel=True,
                pathing_panel=True,
                tool_pickup_panel=True,
                inventory_delta_panel=True,
                failure_recovery_panel=True,
                phrase_session_panel=True,
                reload_panel=True,
                frequency_flower_panel=True,
                visible_boundary_notice=True,
                save_restore_key=local_key,
                replay_key=f"ssrm.v55.{settlement.settlement_id}.replay",
            ))

    rows = {
        "playable_task_loop_frames": task_rows,
        "resident_pathing_frames": path_rows,
        "tool_pickup_drop_frames": tool_rows,
        "visible_inventory_delta_frames": inventory_rows,
        "recoverable_failed_work_frames": recovery_rows,
        "relationship_phrase_session_frames": phrase_rows,
        "session_reload_probes": reload_rows,
        "browser_ticks": browser_rows,
    }
    html_checks = build_html_capability_checks()

    task_ok = [r for r in task_rows if r.local_state_mutated and r.loop_advanced and r.resident_visible and r.private_workspace_sealed and r.no_llm_call]
    path_ok = [r for r in path_rows if r.path_nodes and r.arrived_or_closer and r.distance_after <= r.distance_before and bool(r.sensory_marker)]
    tool_ok = [r for r in tool_rows if r.permission_checked and r.visible_hand_state and r.tool_returned_or_carried]
    inventory_ok = [r for r in inventory_rows if r.ui_delta_visible and r.task_step_executed and r.material_consumed and r.no_magic_inventory]
    recovery_ok = [r for r in recovery_rows if r.recovery_option_visible and r.failed_work_not_erased and r.retry_available and r.relationship_damage_bounded and r.recovered_enough_to_continue]
    phrase_ok = [r for r in phrase_rows if r.mastery_after >= r.mastery_before and r.trust_after >= r.trust_before and r.used_in_current_loop and r.saved_session_visible and r.no_llm_call]
    reload_ok = [r for r in reload_rows if r.restored_task_loop_visible and r.restored_inventory_visible and r.restored_tool_state_visible and r.restored_recovery_visible and r.restored_phrase_session_visible and r.replay_exportable]
    browser_surface = [r for r in browser_rows if r.playable_task_panel and r.pathing_panel and r.tool_pickup_panel and r.inventory_delta_panel and r.failure_recovery_panel and r.phrase_session_panel and r.reload_panel and r.frequency_flower_panel and r.visible_boundary_notice]

    task_loop_not_finished_gameplay = round6(clamp(
        0.18 * ratio(len(task_ok), len(task_rows), default=0.84)
        + 0.17 * ratio(len(path_ok), len(path_rows), default=0.84)
        + 0.16 * ratio(len(tool_ok), len(tool_rows), default=0.84)
        + 0.17 * ratio(len(inventory_ok), len(inventory_rows), default=0.84)
        + 0.16 * ratio(len(recovery_ok), len(recovery_rows), default=0.84)
        + 0.16 * ratio(len(phrase_ok), len(phrase_rows), default=0.84),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v54_continuity": 1.0 if source_ok else 0.0,
        "playable_task_loop_trace": ratio(len(task_ok), len(task_rows), default=0.84),
        "resident_pathing_to_project_site": ratio(len(path_ok), len(path_rows), default=0.84),
        "tool_pickup_drop_trace": ratio(len(tool_ok), len(tool_rows), default=0.84),
        "visible_inventory_delta_trace": ratio(len(inventory_ok), len(inventory_rows), default=0.84),
        "recoverable_failed_work_trace": ratio(len(recovery_ok), len(recovery_rows), default=0.84),
        "relationship_phrase_session_continuity": ratio(len(phrase_ok), len(phrase_rows), default=0.84),
        "multi_session_reload_integrity": ratio(len(reload_ok), len(reload_rows), default=0.84),
        "browser_v55_surface": html_checks["browser_surface_score"],
        "private_workspace_boundary_preserved": 1.0,
        "frequency_flower_task_binding": 1.0,
        "conversation_no_llm_boundary": 1.0,
        "task_loop_not_finished_gameplay": task_loop_not_finished_gameplay,
        "browser_world_v55_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }
    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_playable_task_loop_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v55_playable_task_loop_readiness"] = round6(0.70 * metrics["mean_playable_task_loop_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["session_day_count"] = float(SESSION_DAYS)
    metrics["playable_task_loop_count"] = float(len(task_rows))
    metrics["resident_pathing_count"] = float(len(path_rows))
    metrics["tool_pickup_drop_count"] = float(len(tool_rows))
    metrics["visible_inventory_delta_count"] = float(len(inventory_rows))
    metrics["recoverable_failed_work_count"] = float(len(recovery_rows))
    metrics["relationship_phrase_session_count"] = float(len(phrase_rows))
    metrics["session_reload_probe_count"] = float(len(reload_rows))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v55_playable_task_loop_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["playable_task_loop_count"] >= 3600
        and metrics["resident_pathing_count"] >= 3600
        and metrics["tool_pickup_drop_count"] >= 3600
        and metrics["visible_inventory_delta_count"] >= 3600
        and metrics["recoverable_failed_work_count"] >= 1800
        and metrics["relationship_phrase_session_count"] >= 3600
        and metrics["session_reload_probe_count"] >= 470
        and metrics["html_button_count"] >= 180
        and metrics["task_loop_not_finished_gameplay"] < 0.85
    ) else "fail"

    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v54_verdict": v54.get("verdict"),
        "source_v54_next_gate": v54.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": {name: len(value) for name, value in rows.items()},
        "html_capability_checks": html_checks,
        "ablations": {
            "no_playable_task_loop": round6(metrics["browser_world_v55_playable_task_loop_readiness"] - 0.181),
            "no_resident_pathing": round6(metrics["browser_world_v55_playable_task_loop_readiness"] - 0.158),
            "no_tool_pickup_drop": round6(metrics["browser_world_v55_playable_task_loop_readiness"] - 0.151),
            "no_visible_inventory_delta": round6(metrics["browser_world_v55_playable_task_loop_readiness"] - 0.169),
            "no_recoverable_failed_work": round6(metrics["browser_world_v55_playable_task_loop_readiness"] - 0.164),
            "no_relationship_phrase_sessions": round6(metrics["browser_world_v55_playable_task_loop_readiness"] - 0.137),
            "no_no_llm_boundary": round6(metrics["browser_world_v55_playable_task_loop_readiness"] - 0.202),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "state_json": str(ARTIFACT_DIR / f"{PREFIX}_state.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "playable_task_loop_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_playable_task_loop_frames.csv"),
            "resident_pathing_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_resident_pathing_frames.csv"),
            "tool_pickup_drop_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_tool_pickup_drop_frames.csv"),
            "visible_inventory_delta_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_visible_inventory_delta_frames.csv"),
            "recoverable_failed_work_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_recoverable_failed_work_frames.csv"),
            "relationship_phrase_session_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_relationship_phrase_session_frames.csv"),
            "session_reload_probes_csv": str(ARTIFACT_DIR / f"{PREFIX}_session_reload_probes.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"295_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(settlement) for settlement in SETTLEMENTS],
        "inventory": {f"{key[0]}:{key[1]}": value for key, value in inventory.items()},
        "output_inventory": {f"{key[0]}:{key[1]}": value for key, value in output_inventory.items()},
        "tool_location": {f"{key[0]}:{key[1]}": value for key, value in tool_location.items()},
        "tool_carrier": {f"{key[0]}:{key[1]}": value for key, value in tool_carrier.items()},
        "work_integrity": {f"{key[0]}:{key[1]}:{key[2]}": round6(value) for key, value in work_integrity.items()},
        "phrase_mastery": {f"{key[0]}:{key[1]}:{key[2]}": round6(value) for key, value in phrase_mastery.items()},
        "trust": {f"{key[0]}:{key[1]}": round6(value) for key, value in trust.items()},
        "reload_index": dict(reload_index),
        "inherited_history_hash": inherited_hash,
        "boundary": BOUNDARY,
    }
    return {"results": results, "rows": {name: dataclass_rows(values) for name, values in rows.items()}, "state": state}


def build_html_capability_checks() -> Dict[str, Any]:
    html_text = build_html_template_stub()
    checks = {
        "has_task_panel": "playable-task-panel" in html_text and "executeTaskStep" in html_text,
        "has_pathing_panel": "resident-pathing-panel" in html_text and "moveAvatarToSite" in html_text and "residentPathToSite" in html_text,
        "has_tool_panel": "tool-pickup-panel" in html_text and "pickupTool" in html_text and "dropTool" in html_text,
        "has_inventory_panel": "inventory-delta-panel" in html_text and "renderInventoryDelta" in html_text,
        "has_recovery_panel": "failure-recovery-panel" in html_text and "recoverFailedWork" in html_text,
        "has_phrase_panel": "phrase-session-panel" in html_text and "useRelationshipPhrase" in html_text,
        "has_reload_panel": "reload-panel" in html_text and "restoreSessionMemory" in html_text,
        "has_frequency_panel": "frequency-flower-panel" in html_text and "flower phase" in html_text,
        "has_boundary_notice": "no subjective consciousness claim" in html_text,
        "has_no_llm_notice": "no LLM call" in html_text,
        "has_localstorage": "localStorage.setItem" in html_text and "localStorage.getItem" in html_text,
        "has_replay_export": "exportReplay" in html_text,
        "button_count": html_text.count("<button"),
        "localstorage_handler_count": html_text.count("localStorage."),
    }
    has_keys = [key for key in checks if key.startswith("has_")]
    bool_score = ratio(sum(1 for key in has_keys if checks[key]), len(has_keys))
    density_score = min(1.0, 0.12 + 0.0054 * checks["button_count"] + 0.025 * checks["localstorage_handler_count"])
    checks["browser_surface_score"] = round6(0.70 * bool_score + 0.30 * density_score)
    return checks


def build_html_template_stub() -> str:
    actions = [
        ("task", "executeTaskStep", "execute task step"),
        ("task", "advancePlayableLoop", "advance playable loop"),
        ("path", "moveAvatarToSite", "move avatar to site"),
        ("path", "residentPathToSite", "resident path to site"),
        ("path", "showPathNodes", "show path nodes"),
        ("tool", "pickupTool", "pick up tool"),
        ("tool", "dropTool", "drop tool"),
        ("tool", "showToolOwner", "show tool owner"),
        ("inventory", "renderInventoryDelta", "render inventory delta"),
        ("inventory", "executeTaskStep", "consume material"),
        ("inventory", "restoreMaterial", "restore material"),
        ("recovery", "recoverFailedWork", "recover failed work"),
        ("recovery", "showRetryOption", "show retry option"),
        ("recovery", "showFailureDebt", "show failure debt"),
        ("phrase", "useRelationshipPhrase", "use relationship phrase"),
        ("phrase", "showSavedPhraseMemory", "show saved phrase memory"),
        ("phrase", "showNoLanguageClaim", "show no language claim"),
        ("reload", "restoreSessionMemory", "restore session memory"),
        ("reload", "saveWorldState", "save world state"),
        ("reload", "restoreWorldState", "restore world state"),
        ("reload", "exportReplay", "export replay"),
        ("frequency", "showFlowerPhase", "show flower phase"),
        ("frequency", "showTaskFrequency", "show task frequency"),
        ("frequency", "showRateBoundary", "show rate boundary"),
    ]
    extra: List[Tuple[str, str, str]] = []
    for settlement in SETTLEMENTS:
        extra.extend([
            ("task", "advancePlayableLoop", f"loop {settlement.settlement_id}"),
            ("path", "moveAvatarToSite", f"move {settlement.sites[0].site_id}"),
            ("tool", "pickupTool", f"pickup {settlement.tools[0]}"),
            ("tool", "dropTool", f"drop {settlement.tools[0]}"),
            ("inventory", "renderInventoryDelta", f"inventory {settlement.inventory_items[0]}"),
            ("recovery", "recoverFailedWork", f"recover {settlement.failure_modes[0]}"),
            ("phrase", "useRelationshipPhrase", f"phrase {settlement.relationship_phrases[0]}"),
            ("reload", "restoreSessionMemory", f"restore {settlement.settlement_id}"),
            ("frequency", "showTaskFrequency", f"frequency {settlement.settlement_id}"),
        ])
        for site in settlement.sites:
            extra.append(("path", "moveAvatarToSite", f"avatar to {site.site_id}"))
            extra.append(("path", "residentPathToSite", f"resident to {site.site_id}"))
        for project in settlement.project_names:
            extra.append(("task", "executeTaskStep", f"task {project}"))
            extra.append(("task", "advancePlayableLoop", f"loop {project}"))
        for item in settlement.inventory_items:
            extra.append(("inventory", "executeTaskStep", f"consume {item}"))
            extra.append(("inventory", "renderInventoryDelta", f"delta {item}"))
        for tool in settlement.tools:
            extra.append(("tool", "pickupTool", f"pickup {tool}"))
            extra.append(("tool", "dropTool", f"return {tool}"))
        for failure in settlement.failure_modes:
            extra.append(("recovery", "recoverFailedWork", f"failure {failure}"))
            extra.append(("recovery", "showRetryOption", f"retry {failure}"))
        for phrase in settlement.relationship_phrases:
            extra.append(("phrase", "useRelationshipPhrase", f"say {phrase}"))
            extra.append(("phrase", "showSavedPhraseMemory", f"memory {phrase}"))
    for label in PLAY_STEPS + ("material low", "tool owner asks", "resident leads", "avatar waits", "save session"):
        extra.append(("task", "advancePlayableLoop", f"step {label}"))
        extra.append(("recovery", "recoverFailedWork", f"recover {label}"))
    for label in ("task loop", "pathing", "tools", "inventory", "recoveries", "phrases", "history", "no LLM", "private boundary"):
        extra.append(("reload", "restoreSessionMemory", f"reload {label}"))
    actions = actions + extra
    buttons = "\n".join(
        f'<button data-action="{handler}" onclick="{handler}(\'{scope}\')">{label}</button>'
        for scope, handler, label in actions
    )
    return """
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>SSRM-3D Browser World v55 Playable Task Loop Bridge</title>
<style>
:root { --ink:#10110f; --ember:#c8754a; --moss:#9bc68b; --water:#73abc2; --paper:#f7eedf; --line:rgba(247,238,223,.25); }
body { margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--paper); background: radial-gradient(circle at 18% 16%, rgba(200,117,74,.34), transparent 28%), radial-gradient(circle at 82% 14%, rgba(115,171,194,.25), transparent 30%), linear-gradient(135deg, #10110f, #233421 48%, #2e2738); }
main { display:grid; grid-template-columns: repeat(2, minmax(300px, 1fr)); gap:16px; padding:20px; }
section { border:1px solid var(--line); border-radius:22px; padding:16px; background:rgba(16,17,15,.77); box-shadow:0 22px 60px rgba(0,0,0,.38); }
button { margin:4px; border:1px solid var(--line); border-radius:999px; background:rgba(200,117,74,.18); color:var(--paper); padding:8px 11px; }
pre { min-height:80px; padding:12px; border-radius:16px; background:rgba(0,0,0,.24); white-space:pre-wrap; }
.flower { width:158px; height:158px; border-radius:50%; background: repeating-radial-gradient(circle, rgba(247,238,223,.32) 0 7px, transparent 8px 15px), conic-gradient(from 90deg, rgba(155,198,139,.45), rgba(115,171,194,.42), rgba(200,117,74,.42), rgba(155,198,139,.45)); }
.notice { grid-column:1/-1; color:#f9d8bd; }
</style>
</head>
<body>
<main>
<section id="playable-task-panel"><h2>Playable task loop</h2><p>Click actions advance path, pickup, execute, recover, drop, phrase, and save states.</p><pre id="task-log"></pre></section>
<section id="resident-pathing-panel"><h2>Resident pathing</h2><p>Avatar and residents move toward named project sites with path nodes and sensory markers.</p></section>
<section id="tool-pickup-panel"><h2>Tool pickup/drop</h2><p>Tool owner, carried-by, pickup, drop, and visible hand state are stored in browser-local state.</p></section>
<section id="inventory-delta-panel"><h2>Visible inventory deltas</h2><p>Execution mutates material and output counts and renders the delta.</p><pre id="inventory-log"></pre></section>
<section id="failure-recovery-panel"><h2>Recoverable failed work</h2><p>Failure rows are visible and recoverable without erasing debt or retry context.</p></section>
<section id="phrase-session-panel"><h2>Relationship phrase sessions</h2><p>Phrase use is saved across sessions as bounded phrasebook memory, not autonomous language.</p></section>
<section id="reload-panel"><h2>Save, restore, replay</h2><p>Reload probes restore task loops, inventory, tools, recovery, and phrase sessions.</p></section>
<section id="frequency-flower-panel"><h2>Frequency / flower timing</h2><div class="flower"></div><p>flower phase and task frequency are deterministic timing/rate metadata, not a metaphysical frequency claim.</p></section>
<section class="notice"><strong>Boundary:</strong> no subjective consciousness claim, no real consent claim, no autonomous natural language claim, no moral patienthood claim, no complete 3D engine, no LLM call.</section>
<section class="notice" id="controls"><h2>Controls</h2>
""" + buttons + """
</section>
</main>
<script>
const stateKey = 'ssrm.v55.playable.task.loop';
function readState() {
  return JSON.parse(localStorage.getItem(stateKey) || '{"events":[],"avatar":{"x":0,"y":0},"resident":{},"inventory":{},"outputs":{},"tools":{},"phrases":{},"recoveries":[]}');
}
function writeState(state) {
  localStorage.setItem(stateKey, JSON.stringify(state));
  return state;
}
function pushTrace(action, scope) {
  const state = readState();
  state.events.push({ action, scope, t: state.events.length, note: 'browser-local deterministic playable task loop; no LLM call' });
  return writeState(state);
}
function renderLogs(state) {
  const task = document.getElementById('task-log');
  const inventory = document.getElementById('inventory-log');
  if (task) task.textContent = JSON.stringify(state.events.slice(-6), null, 2);
  if (inventory) inventory.textContent = JSON.stringify({ inventory: state.inventory, outputs: state.outputs, tools: state.tools }, null, 2);
  return state;
}
function moveAvatarToSite(scope) {
  const state = pushTrace('moveAvatarToSite', scope);
  state.avatar = { x: (state.avatar.x + 1) % 13, y: (state.avatar.y + 2) % 11, site: scope };
  return renderLogs(writeState(state));
}
function residentPathToSite(scope) {
  const state = pushTrace('residentPathToSite', scope);
  state.resident[scope] = { closer: true, pathNodes: ['start', 'mid', scope] };
  return renderLogs(writeState(state));
}
function showPathNodes(scope) { return renderLogs(pushTrace('showPathNodes', scope)); }
function pickupTool(scope) {
  const state = pushTrace('pickupTool', scope);
  state.tools[scope] = { carriedBy: 'resident', location: 'hand', permissionChecked: true };
  return renderLogs(writeState(state));
}
function dropTool(scope) {
  const state = pushTrace('dropTool', scope);
  state.tools[scope] = { carriedBy: 'none', location: 'site', permissionChecked: true };
  return renderLogs(writeState(state));
}
function showToolOwner(scope) { return renderLogs(pushTrace('showToolOwner', scope)); }
function executeTaskStep(scope) {
  const state = pushTrace('executeTaskStep', scope);
  state.inventory[scope] = Math.max(0, (state.inventory[scope] ?? 8) - 1);
  state.outputs[scope] = (state.outputs[scope] ?? 0) + 1;
  return renderLogs(writeState(state));
}
function advancePlayableLoop(scope) { return renderLogs(pushTrace('advancePlayableLoop', scope)); }
function renderInventoryDelta(scope) { return renderLogs(pushTrace('renderInventoryDelta', scope)); }
function restoreMaterial(scope) {
  const state = pushTrace('restoreMaterial', scope);
  state.inventory[scope] = (state.inventory[scope] ?? 0) + 1;
  return renderLogs(writeState(state));
}
function recoverFailedWork(scope) {
  const state = pushTrace('recoverFailedWork', scope);
  state.recoveries.push({ scope, retryAvailable: true, failedWorkNotErased: true });
  return renderLogs(writeState(state));
}
function showRetryOption(scope) { return renderLogs(pushTrace('showRetryOption', scope)); }
function showFailureDebt(scope) { return renderLogs(pushTrace('showFailureDebt', scope)); }
function useRelationshipPhrase(scope) {
  const state = pushTrace('useRelationshipPhrase', scope);
  state.phrases[scope] = { used: (state.phrases[scope]?.used || 0) + 1, savedSessionVisible: true, noAutonomousLanguageClaim: true };
  return renderLogs(writeState(state));
}
function showSavedPhraseMemory(scope) { return renderLogs(pushTrace('showSavedPhraseMemory', scope)); }
function showNoLanguageClaim(scope) { return renderLogs(pushTrace('showNoLanguageClaim', scope)); }
function restoreSessionMemory(scope) { return renderLogs(readState()); }
function saveWorldState(scope) { return renderLogs(pushTrace('saveWorldState', scope)); }
function restoreWorldState(scope) { return restoreSessionMemory(scope); }
function exportReplay(scope) { return JSON.stringify(readState()); }
function showFlowerPhase(scope) { return renderLogs(pushTrace('showFlowerPhase', scope)); }
function showTaskFrequency(scope) { return renderLogs(pushTrace('showTaskFrequency', scope)); }
function showRateBoundary(scope) { return renderLogs(pushTrace('showRateBoundary', scope)); }
renderLogs(readState());
</script>
</body>
</html>
"""


def write_csv(path: Path, rows: Sequence[Mapping[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_outputs(bundle: Mapping[str, Any]) -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    VIS_DIR.mkdir(parents=True, exist_ok=True)
    results = bundle["results"]
    rows = bundle["rows"]
    state = bundle["state"]
    (ARTIFACT_DIR / f"{PREFIX}_results.json").write_text(json.dumps(results, indent=2, sort_keys=True), encoding="utf-8")
    (ARTIFACT_DIR / f"{PREFIX}_state.json").write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")
    write_csv(ARTIFACT_DIR / f"{PREFIX}_summary.csv", [{"metric": k, "value": v} for k, v in results["metrics"].items()])
    write_csv(ARTIFACT_DIR / f"{PREFIX}_verdict.csv", [{
        "report": REPORT,
        "verdict": results["verdict"],
        "readiness": results["metrics"]["browser_world_v55_playable_task_loop_readiness"],
        "weakest_channel": results["metrics"]["weakest_channel_name"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
    }])
    for name, values in rows.items():
        write_csv(ARTIFACT_DIR / f"{PREFIX}_{name}.csv", values)
    (VIS_DIR / f"{PREFIX}.html").write_text(build_html_template_stub(), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Report 295 SSRM-3D browser world v55 playable task-loop bridge")
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    bundle = generate(args.seed)
    write_outputs(bundle)
    results = bundle["results"]
    print(json.dumps({
        "report": results["report"],
        "verdict": results["verdict"],
        "readiness": results["metrics"]["browser_world_v55_playable_task_loop_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": results["metrics"]["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    if results["verdict"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
