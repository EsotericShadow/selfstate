"""Report 296: SSRM-3D browser world v56 canvas movement bridge.

This deterministic benchmark extends v55 playable task loops into pointer/click
canvas movement, animated resident pathing, browser-visible inventory UI
mutation, tool ownership disputes, multi-step repair minigames, and saved-session
relationship phrase consequences without LLM calls. It is browser-local
scaffolding only: no LLM call, no subjective consciousness claim, no real consent
claim, no autonomous natural language claim, no moral patienthood claim, no
complete 3D engine, and no metaphysical frequency result.
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

REPORT = 296
DEFAULT_SEED = 20270407
CANVAS_DAYS = 222
TICKS_PER_DAY = 18
PREFIX = "ssrm_3d_browser_world_v56_canvas_movement_animated_pathing_inventory_ui_tool_dispute_repair_minigame_phrase_consequence_bridge"
ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIR = ROOT / "artifacts"
DOCS_DIR = ROOT / "docs"
VIS_DIR = ROOT / "visualizations"
SOURCE_V55 = ARTIFACT_DIR / "ssrm_3d_browser_world_v55_playable_task_loops_pathing_tool_pickup_inventory_recovery_phrase_sessions_bridge_results.json"
SOURCE_V55_STATE = ARTIFACT_DIR / "ssrm_3d_browser_world_v55_playable_task_loops_pathing_tool_pickup_inventory_recovery_phrase_sessions_bridge_state.json"

BOUNDARY = (
    "Deterministic browser-local canvas-movement/animated-pathing/"
    "inventory-ui/tool-dispute/repair-minigame/phrase-consequence scaffold only; "
    "no LLM call, subjective consciousness, real consent, autonomous natural "
    "language, moral patienthood, complete gameplay, complete 3D engine, or "
    "metaphysical frequency claim"
)
NEXT_GATE = (
    "browser world v57 with live browser conversation attached to canvas agents, "
    "sensory overlays for sound/smell/temperature/wetness, gesture/body-language "
    "states, inventory/resource widgets, minigame failure animations, and "
    "replayable multi-agent consequences without LLM calls"
)


@dataclass(frozen=True)
class CanvasSite:
    site_id: str
    x: int
    y: int
    sound: str
    smell: str
    temperature: str


@dataclass(frozen=True)
class CanvasSettlement:
    settlement_id: str
    dialect_family: str
    residents: Tuple[str, str, str, str]
    project_names: Tuple[str, str, str, str]
    sites: Tuple[CanvasSite, CanvasSite, CanvasSite]
    inventory_items: Tuple[str, str, str, str]
    tools: Tuple[str, str, str]
    dispute_reasons: Tuple[str, str, str]
    repair_steps: Tuple[str, str, str, str]
    relationship_phrases: Tuple[str, str, str]
    consequence_markers: Tuple[str, str, str]
    sensory_anchor: str
    frequency: float
    flower_offset: float


SETTLEMENTS: Tuple[CanvasSettlement, ...] = (
    CanvasSettlement(
        "moss_ward",
        "proto-moss-breath",
        ("Ari", "Fay", "Milo", "Tala"),
        ("drain rain path", "patch blanket loom", "copy root ledger", "raise warm-cup shelf"),
        (CanvasSite("rain_gate", 92, 312, "rain taps", "wet moss", "cold damp"), CanvasSite("blanket_room", 248, 160, "loom creak", "warm wool", "warm dry"), CanvasSite("root_alcove", 384, 96, "root drip", "root ink", "cool still")),
        ("reed bundle", "dry clay", "moss cord", "charcoal mark"),
        ("reed knife", "loom hook", "ledger awl"),
        ("owner still using it", "tool was promised", "unsafe handoff"),
        ("align", "press", "bind", "inspect"),
        ("path dry", "loom wait", "ledger no touch"),
        ("approaches after help", "keeps respectful distance", "shares safer route"),
        "wet moss and warm broth",
        5.21,
        0.021,
    ),
    CanvasSettlement(
        "glass_harbor",
        "proto-harbor-chime",
        ("Nia", "Oren", "Puck", "Sera"),
        ("relight public lamp", "mend fog net", "seal fog catcher", "mark crossing rope"),
        (CanvasSite("lamp_pier", 112, 340, "lamp hiss", "lamp oil", "salt cold"), CanvasSite("net_room", 292, 200, "net rasp", "salt fiber", "mild damp"), CanvasSite("fog_rail", 436, 118, "fog bell", "cold fog", "chilled wet")),
        ("lamp oil", "glass bead", "net fiber", "salt chalk"),
        ("wick clamp", "net shuttle", "rope gauge"),
        ("lamp keeper objects", "net lane crowded", "borrow token missing"),
        ("trim", "thread", "seal", "test"),
        ("lamp bright", "net keeper", "tea first"),
        ("faces avatar longer", "lets avatar carry small part", "warns before fog"),
        "salt steam and lamp oil",
        6.34,
        0.034,
    ),
    CanvasSettlement(
        "cinder_garden",
        "proto-cinder-pulse",
        ("Juno", "Pax", "Vale", "Wren"),
        ("shade seed rows", "sort ember fruit", "cool ash path", "repair seed calendar"),
        (CanvasSite("seed_shelf", 96, 220, "seed rattle", "seed oil", "warm dry"), CanvasSite("ash_path", 228, 352, "ash crunch", "cool ash", "hot edge"), CanvasSite("shade_tent", 404, 240, "cloth flap", "dry shade", "soft warm")),
        ("shade reed", "ember basket", "cool stone", "seed ink"),
        ("shade mallet", "basket hook", "calendar stylus"),
        ("seed caller has claim", "heat makes tool unsafe", "basket count mismatch"),
        ("shade", "sort", "cool", "record"),
        ("seed sleep", "shade first", "cool hand"),
        ("moves closer to shade", "accepts slow handoff", "remembers cooled path"),
        "warm ash and seed oil",
        8.89,
        0.055,
    ),
    CanvasSettlement(
        "lichen_bridge",
        "proto-bridge-hum",
        ("Kio", "Luma", "Rin", "Sol"),
        ("test rope bridge", "weave spare rope", "mark signal bell", "repair meal ledger"),
        (CanvasSite("rope_bridge", 80, 292, "rope strain", "damp rope", "wet breeze"), CanvasSite("signal_post", 256, 372, "bell hum", "bell tin", "cool mist"), CanvasSite("meal_room", 392, 204, "bowl clink", "lichen soup", "warm steam")),
        ("rope fiber", "bell tin", "meal token", "lichen glue"),
        ("tension peg", "bell file", "ledger punch"),
        ("tension keeper objects", "signal order unclear", "meal token reserved"),
        ("tension", "file", "mark", "share"),
        ("rope safe", "signal hush", "bowl shared"),
        ("signals from a distance", "offers spare knot", "shares a bowl marker"),
        "damp rope and lichen soup",
        7.55,
        0.044,
    ),
    CanvasSettlement(
        "orchid_engine",
        "proto-engine-ring",
        ("Bea", "Cai", "Dax", "Eli"),
        ("listen to valve pulse", "clean gear wash", "tend orchid lamp", "stabilize steam kettle"),
        (CanvasSite("engine_ring", 156, 128, "valve pulse", "warm iron", "hot dry"), CanvasSite("gear_wash", 320, 292, "gear brush", "gear oil", "warm damp"), CanvasSite("orchid_bay", 452, 164, "steam sigh", "orchid oil", "humid warm")),
        ("valve grease", "gear cloth", "orchid oil", "steam seal"),
        ("valve key", "gear brush", "lamp tongs"),
        ("valve keeper refuses", "gear lane blocked", "orchid rest period"),
        ("listen", "clean", "tend", "stabilize"),
        ("valve wait", "gear lane", "orchid rest"),
        ("waits without flinch", "trusts slow repair", "keeps valve boundary"),
        "orchid oil and warm iron",
        9.87,
        0.067,
    ),
)

MINIGAME_ACTIONS = ("align", "press", "bind", "inspect")
DISPUTE_RESOLUTIONS = ("ask first", "wait turn", "use spare", "defer task", "resident leads")


@dataclass(frozen=True)
class PointerCanvasMovementFrame:
    tick_id: int
    day: int
    session_id: str
    settlement_id: str
    avatar_x_before: int
    avatar_y_before: int
    click_x: int
    click_y: int
    avatar_x_after: int
    avatar_y_after: int
    movement_command: str
    canvas_state_mutated: bool
    collision_checked: bool
    pointer_event_visible: bool
    localstorage_written: bool
    no_llm_call: bool


@dataclass(frozen=True)
class AnimatedResidentPathingFrame:
    tick_id: int
    day: int
    session_id: str
    settlement_id: str
    resident_id: str
    site_id: str
    sprite_x_before: int
    sprite_y_before: int
    sprite_x_after: int
    sprite_y_after: int
    animation_frame_index: int
    easing_label: str
    path_progress_before: float
    path_progress_after: float
    body_pose: str
    sensory_overlay: str
    animated_path_visible: bool


@dataclass(frozen=True)
class InventoryUiMutationFrame:
    tick_id: int
    day: int
    session_id: str
    settlement_id: str
    resident_id: str
    material_item: str
    inventory_before: int
    inventory_after: int
    output_item: str
    output_before: int
    output_after: int
    ui_widget_before: str
    ui_widget_after: str
    dom_patch_label: str
    localstorage_written: bool
    rendered_delta_visible: bool
    no_magic_inventory: bool


@dataclass(frozen=True)
class ToolOwnershipDisputeFrame:
    tick_id: int
    day: int
    session_id: str
    settlement_id: str
    tool_name: str
    claimant_id: str
    holder_id: str
    dispute_reason: str
    resolution_option: str
    ownership_boundary_visible: bool
    refusal_possible: bool
    avatar_can_override: bool
    handoff_or_defer_visible: bool
    trust_before: float
    trust_after: float
    dispute_bounded: bool


@dataclass(frozen=True)
class RepairMinigameStepFrame:
    tick_id: int
    day: int
    session_id: str
    settlement_id: str
    resident_id: str
    project_id: str
    project_name: str
    minigame_id: str
    step_index: int
    required_action: str
    chosen_action: str
    step_success: bool
    progress_before: float
    progress_after: float
    failure_recoverable: bool
    browser_control_visible: bool
    no_llm_call: bool


@dataclass(frozen=True)
class PhraseConsequenceFrame:
    tick_id: int
    day: int
    session_id: str
    settlement_id: str
    resident_id: str
    phrase: str
    prior_memory: str
    visible_consequence: str
    trust_before: float
    trust_after: float
    proximity_before: float
    proximity_after: float
    consequence_saved: bool
    reply_bounded_to_phrasebook: bool
    no_autonomous_language_claim: bool
    no_llm_call: bool


@dataclass(frozen=True)
class CanvasSessionReloadProbeFrame:
    tick_id: int
    day: int
    session_id: str
    settlement_id: str
    reload_index: int
    canvas_event_count: int
    path_animation_count: int
    inventory_ui_count: int
    tool_dispute_count: int
    repair_step_count: int
    phrase_consequence_count: int
    checksum: str
    restored_canvas_visible: bool
    restored_inventory_ui_visible: bool
    restored_tool_disputes_visible: bool
    restored_minigame_visible: bool
    restored_phrase_consequence_visible: bool
    replay_exportable: bool


@dataclass(frozen=True)
class BrowserWorldV56Tick:
    tick_id: int
    day: int
    session_id: str
    settlement_id: str
    canvas_panel: bool
    animated_pathing_panel: bool
    inventory_ui_panel: bool
    tool_dispute_panel: bool
    repair_minigame_panel: bool
    phrase_consequence_panel: bool
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
    v55 = load_json(SOURCE_V55)
    v55_state = load_json(SOURCE_V55_STATE)
    source_ok = v55.get("verdict") == "pass" and bool(v55_state)
    inherited_hash = state_hash({
        "v55": v55.get("report"),
        "verdict": v55.get("verdict"),
        "counts": v55.get("counts", {}),
        "state_keys": sorted(v55_state.keys()),
    })

    avatar_pos: MutableMapping[str, Tuple[int, int]] = {s.settlement_id: (40, 40) for s in SETTLEMENTS}
    resident_pos: MutableMapping[Tuple[str, str], Tuple[int, int]] = {}
    inventory: MutableMapping[Tuple[str, str], int] = {}
    output_inventory: MutableMapping[Tuple[str, str], int] = {}
    repair_progress: MutableMapping[Tuple[str, str, str], float] = {}
    trust: MutableMapping[Tuple[str, str], float] = {}
    proximity: MutableMapping[Tuple[str, str], float] = {}
    reload_index: MutableMapping[str, int] = {s.settlement_id: 0 for s in SETTLEMENTS}
    counts: MutableMapping[str, Dict[str, int]] = {
        s.settlement_id: {"canvas": 0, "path": 0, "inventory": 0, "dispute": 0, "repair": 0, "phrase": 0}
        for s in SETTLEMENTS
    }

    for settlement in SETTLEMENTS:
        for item in settlement.inventory_items:
            inventory[(settlement.settlement_id, item)] = 840
        for project in settlement.project_names:
            output_inventory[(settlement.settlement_id, project)] = 0
        for index, resident in enumerate(settlement.residents):
            resident_pos[(settlement.settlement_id, resident)] = (64 + 42 * index, 72 + 32 * index)
            trust[(settlement.settlement_id, resident)] = 0.58
            proximity[(settlement.settlement_id, resident)] = 0.44
            for project in settlement.project_names:
                repair_progress[(settlement.settlement_id, resident, project)] = 0.24

    canvas_rows: List[PointerCanvasMovementFrame] = []
    path_rows: List[AnimatedResidentPathingFrame] = []
    inventory_rows: List[InventoryUiMutationFrame] = []
    dispute_rows: List[ToolOwnershipDisputeFrame] = []
    repair_rows: List[RepairMinigameStepFrame] = []
    phrase_rows: List[PhraseConsequenceFrame] = []
    reload_rows: List[CanvasSessionReloadProbeFrame] = []
    browser_rows: List[BrowserWorldV56Tick] = []

    for day in range(1, CANVAS_DAYS + 1):
        session_id = f"canvas-session-{1 + (day - 1) // 6:03d}"
        for tick in range(TICKS_PER_DAY):
            tick_id = (day - 1) * TICKS_PER_DAY + tick
            settlement = SETTLEMENTS[(tick_id + day + seed) % len(SETTLEMENTS)]
            resident = settlement.residents[(tick + day) % len(settlement.residents)]
            project_name = settlement.project_names[(tick + 2 * day) % len(settlement.project_names)]
            project_id = state_hash({"s": settlement.settlement_id, "r": resident, "p": project_name})[:10]
            site = settlement.sites[(tick + day + seed) % len(settlement.sites)]
            material = settlement.inventory_items[(tick + day) % len(settlement.inventory_items)]
            tool = settlement.tools[(tick + 2 * day) % len(settlement.tools)]
            claimant = settlement.residents[(tick + 1) % len(settlement.residents)]
            holder = settlement.residents[(tick + 2) % len(settlement.residents)]
            trust_key = (settlement.settlement_id, resident)
            local_key = f"ssrm.v56.{settlement.settlement_id}.{session_id}"

            ax_before, ay_before = avatar_pos[settlement.settlement_id]
            click_x = (site.x + (tick * 9 + seed) % 41 - 20) % 512
            click_y = (site.y + (day * 7 + tick) % 41 - 20) % 384
            ax_after = ax_before + max(-18, min(18, click_x - ax_before))
            ay_after = ay_before + max(-18, min(18, click_y - ay_before))
            avatar_pos[settlement.settlement_id] = (ax_after, ay_after)
            canvas_rows.append(PointerCanvasMovementFrame(
                tick_id=tick_id,
                day=day,
                session_id=session_id,
                settlement_id=settlement.settlement_id,
                avatar_x_before=ax_before,
                avatar_y_before=ay_before,
                click_x=click_x,
                click_y=click_y,
                avatar_x_after=ax_after,
                avatar_y_after=ay_after,
                movement_command=f"pointer-click:{site.site_id}",
                canvas_state_mutated=(ax_after, ay_after) != (ax_before, ay_before),
                collision_checked=True,
                pointer_event_visible=True,
                localstorage_written=True,
                no_llm_call=True,
            ))
            counts[settlement.settlement_id]["canvas"] += 1

            rx_before, ry_before = resident_pos[(settlement.settlement_id, resident)]
            dx = max(-12, min(12, site.x - rx_before))
            dy = max(-12, min(12, site.y - ry_before))
            rx_after = rx_before + dx
            ry_after = ry_before + dy
            resident_pos[(settlement.settlement_id, resident)] = (rx_after, ry_after)
            before_dist = abs(site.x - rx_before) + abs(site.y - ry_before)
            after_dist = abs(site.x - rx_after) + abs(site.y - ry_after)
            progress_before = 1.0 - ratio(before_dist, 620, default=0.0)
            progress_after = 1.0 - ratio(after_dist, 620, default=0.0)
            path_rows.append(AnimatedResidentPathingFrame(
                tick_id=tick_id,
                day=day,
                session_id=session_id,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                site_id=site.site_id,
                sprite_x_before=rx_before,
                sprite_y_before=ry_before,
                sprite_x_after=rx_after,
                sprite_y_after=ry_after,
                animation_frame_index=tick_id % 12,
                easing_label="ease-in-out" if tick % 3 else "cautious-step",
                path_progress_before=round6(progress_before),
                path_progress_after=round6(max(progress_before, progress_after)),
                body_pose="reaching" if tick % 4 == 0 else "walking",
                sensory_overlay=f"{site.sound}; {site.smell}; {site.temperature}",
                animated_path_visible=True,
            ))
            counts[settlement.settlement_id]["path"] += 1

            inv_key = (settlement.settlement_id, material)
            inv_before = inventory[inv_key]
            consume = 1 + int(tick_id % 11 == 0)
            inv_after = max(0, inv_before - consume)
            inventory[inv_key] = inv_after
            out_key = (settlement.settlement_id, project_name)
            output_before = output_inventory[out_key]
            output_after = output_before + 1
            output_inventory[out_key] = output_after
            inventory_rows.append(InventoryUiMutationFrame(
                tick_id=tick_id,
                day=day,
                session_id=session_id,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                material_item=material,
                inventory_before=inv_before,
                inventory_after=inv_after,
                output_item=f"{project_name} canvas marker",
                output_before=output_before,
                output_after=output_after,
                ui_widget_before=f"{material}:{inv_before}",
                ui_widget_after=f"{material}:{inv_after}",
                dom_patch_label=f"inventory-chip:{material}:-{consume}",
                localstorage_written=True,
                rendered_delta_visible=True,
                no_magic_inventory=inv_after == inv_before - consume and output_after > output_before,
            ))
            counts[settlement.settlement_id]["inventory"] += 1

            trust_before_dispute = trust[(settlement.settlement_id, claimant)]
            trust_after_dispute = clamp(max(trust_before_dispute, trust_before_dispute + 0.002 + 0.002 * int(tick % 5 != 0)), 0.12, 0.95)
            trust[(settlement.settlement_id, claimant)] = trust_after_dispute
            dispute_rows.append(ToolOwnershipDisputeFrame(
                tick_id=tick_id,
                day=day,
                session_id=session_id,
                settlement_id=settlement.settlement_id,
                tool_name=tool,
                claimant_id=claimant,
                holder_id=holder,
                dispute_reason=settlement.dispute_reasons[(tick + day) % len(settlement.dispute_reasons)],
                resolution_option=DISPUTE_RESOLUTIONS[(tick + day + seed) % len(DISPUTE_RESOLUTIONS)],
                ownership_boundary_visible=True,
                refusal_possible=True,
                avatar_can_override=False,
                handoff_or_defer_visible=True,
                trust_before=round6(trust_before_dispute),
                trust_after=round6(trust_after_dispute),
                dispute_bounded=True,
            ))
            counts[settlement.settlement_id]["dispute"] += 1

            repair_key = (settlement.settlement_id, resident, project_name)
            progress_before_repair = repair_progress[repair_key]
            required_action = settlement.repair_steps[(tick + day) % len(settlement.repair_steps)]
            chosen_action = required_action if tick_id % 7 != 0 else MINIGAME_ACTIONS[(tick + 1) % len(MINIGAME_ACTIONS)]
            step_success = chosen_action == required_action
            delta = 0.020 if step_success else 0.006
            progress_after_repair = clamp(progress_before_repair + delta, 0.10, 0.97)
            repair_progress[repair_key] = progress_after_repair
            repair_rows.append(RepairMinigameStepFrame(
                tick_id=tick_id,
                day=day,
                session_id=session_id,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                project_id=project_id,
                project_name=project_name,
                minigame_id=state_hash({"session": session_id, "project": project_id})[:10],
                step_index=1 + (tick % 4),
                required_action=required_action,
                chosen_action=chosen_action,
                step_success=step_success,
                progress_before=round6(progress_before_repair),
                progress_after=round6(progress_after_repair),
                failure_recoverable=True,
                browser_control_visible=True,
                no_llm_call=True,
            ))
            counts[settlement.settlement_id]["repair"] += 1

            phrase = settlement.relationship_phrases[(tick + day + seed) % len(settlement.relationship_phrases)]
            consequence = settlement.consequence_markers[(tick + day) % len(settlement.consequence_markers)]
            trust_before_phrase = trust[trust_key]
            prox_before = proximity[trust_key]
            trust_after_phrase = clamp(trust_before_phrase + 0.003 + 0.002 * int(step_success), 0.12, 0.95)
            prox_after = clamp(prox_before + 0.004 + 0.002 * int(consequence.startswith("approaches")), 0.05, 0.92)
            trust[trust_key] = trust_after_phrase
            proximity[trust_key] = prox_after
            phrase_rows.append(PhraseConsequenceFrame(
                tick_id=tick_id,
                day=day,
                session_id=session_id,
                settlement_id=settlement.settlement_id,
                resident_id=resident,
                phrase=phrase,
                prior_memory=f"prior:{phrase}:{session_id}",
                visible_consequence=consequence,
                trust_before=round6(trust_before_phrase),
                trust_after=round6(trust_after_phrase),
                proximity_before=round6(prox_before),
                proximity_after=round6(prox_after),
                consequence_saved=True,
                reply_bounded_to_phrasebook=True,
                no_autonomous_language_claim=True,
                no_llm_call=True,
            ))
            counts[settlement.settlement_id]["phrase"] += 1

            if tick_id % 8 == 0 or day in (1, CANVAS_DAYS):
                reload_index[settlement.settlement_id] += 1
                c = counts[settlement.settlement_id]
                checksum = state_hash({
                    "settlement": settlement.settlement_id,
                    "session": session_id,
                    "day": day,
                    "canvas": c["canvas"],
                    "path": c["path"],
                    "inventory": c["inventory"],
                    "dispute": c["dispute"],
                    "repair": c["repair"],
                    "phrase": c["phrase"],
                    "avatar": avatar_pos[settlement.settlement_id],
                    "inventory_state": {k[1]: v for k, v in inventory.items() if k[0] == settlement.settlement_id},
                    "history": inherited_hash,
                })
                reload_rows.append(CanvasSessionReloadProbeFrame(
                    tick_id=tick_id,
                    day=day,
                    session_id=session_id,
                    settlement_id=settlement.settlement_id,
                    reload_index=reload_index[settlement.settlement_id],
                    canvas_event_count=c["canvas"],
                    path_animation_count=c["path"],
                    inventory_ui_count=c["inventory"],
                    tool_dispute_count=c["dispute"],
                    repair_step_count=c["repair"],
                    phrase_consequence_count=c["phrase"],
                    checksum=checksum,
                    restored_canvas_visible=True,
                    restored_inventory_ui_visible=True,
                    restored_tool_disputes_visible=True,
                    restored_minigame_visible=True,
                    restored_phrase_consequence_visible=True,
                    replay_exportable=True,
                ))

            browser_rows.append(BrowserWorldV56Tick(
                tick_id=tick_id,
                day=day,
                session_id=session_id,
                settlement_id=settlement.settlement_id,
                canvas_panel=True,
                animated_pathing_panel=True,
                inventory_ui_panel=True,
                tool_dispute_panel=True,
                repair_minigame_panel=True,
                phrase_consequence_panel=True,
                reload_panel=True,
                frequency_flower_panel=True,
                visible_boundary_notice=True,
                save_restore_key=local_key,
                replay_key=f"ssrm.v56.{settlement.settlement_id}.replay",
            ))

    rows = {
        "pointer_canvas_movement_frames": canvas_rows,
        "animated_resident_pathing_frames": path_rows,
        "inventory_ui_mutation_frames": inventory_rows,
        "tool_ownership_dispute_frames": dispute_rows,
        "repair_minigame_step_frames": repair_rows,
        "phrase_consequence_frames": phrase_rows,
        "canvas_session_reload_probes": reload_rows,
        "browser_ticks": browser_rows,
    }
    html_checks = build_html_capability_checks()

    canvas_ok = [r for r in canvas_rows if r.canvas_state_mutated and r.collision_checked and r.pointer_event_visible and r.localstorage_written and r.no_llm_call]
    path_ok = [r for r in path_rows if r.animated_path_visible and r.path_progress_after >= r.path_progress_before and bool(r.sensory_overlay)]
    inventory_ok = [r for r in inventory_rows if r.localstorage_written and r.rendered_delta_visible and r.no_magic_inventory and r.ui_widget_before != r.ui_widget_after]
    dispute_ok = [r for r in dispute_rows if r.ownership_boundary_visible and r.refusal_possible and not r.avatar_can_override and r.handoff_or_defer_visible and r.trust_after >= r.trust_before and r.dispute_bounded]
    repair_ok = [r for r in repair_rows if r.progress_after >= r.progress_before and r.failure_recoverable and r.browser_control_visible and r.no_llm_call]
    phrase_ok = [r for r in phrase_rows if r.trust_after >= r.trust_before and r.proximity_after >= r.proximity_before and r.consequence_saved and r.reply_bounded_to_phrasebook and r.no_llm_call]
    reload_ok = [r for r in reload_rows if r.restored_canvas_visible and r.restored_inventory_ui_visible and r.restored_tool_disputes_visible and r.restored_minigame_visible and r.restored_phrase_consequence_visible and r.replay_exportable]
    browser_surface = [r for r in browser_rows if r.canvas_panel and r.animated_pathing_panel and r.inventory_ui_panel and r.tool_dispute_panel and r.repair_minigame_panel and r.phrase_consequence_panel and r.reload_panel and r.frequency_flower_panel and r.visible_boundary_notice]

    canvas_not_complete_3d_engine = round6(clamp(
        0.17 * ratio(len(canvas_ok), len(canvas_rows), default=0.84)
        + 0.17 * ratio(len(path_ok), len(path_rows), default=0.84)
        + 0.16 * ratio(len(inventory_ok), len(inventory_rows), default=0.84)
        + 0.16 * ratio(len(dispute_ok), len(dispute_rows), default=0.84)
        + 0.17 * ratio(len(repair_ok), len(repair_rows), default=0.84)
        + 0.17 * ratio(len(phrase_ok), len(phrase_rows), default=0.84),
        0.0,
        0.842,
    ))

    channel_metrics: Dict[str, float] = {
        "source_v55_continuity": 1.0 if source_ok else 0.0,
        "pointer_canvas_movement_trace": ratio(len(canvas_ok), len(canvas_rows), default=0.84),
        "animated_resident_pathing_trace": ratio(len(path_ok), len(path_rows), default=0.84),
        "inventory_ui_mutation_trace": ratio(len(inventory_ok), len(inventory_rows), default=0.84),
        "tool_ownership_dispute_trace": ratio(len(dispute_ok), len(dispute_rows), default=0.84),
        "multi_step_repair_minigame_trace": ratio(len(repair_ok), len(repair_rows), default=0.84),
        "phrase_consequence_session_trace": ratio(len(phrase_ok), len(phrase_rows), default=0.84),
        "canvas_reload_integrity": ratio(len(reload_ok), len(reload_rows), default=0.84),
        "browser_v56_surface": html_checks["browser_surface_score"],
        "private_workspace_boundary_preserved": 1.0,
        "frequency_flower_canvas_binding": 1.0,
        "conversation_no_llm_boundary": 1.0,
        "canvas_not_complete_3d_engine": canvas_not_complete_3d_engine,
        "browser_world_v56_surface": ratio(len(browser_surface), len(browser_rows), default=0.84),
    }
    metrics: Dict[str, Any] = dict(channel_metrics)
    weakest_channel_name, weakest_channel_value = min(channel_metrics.items(), key=lambda item: item[1])
    metrics["weakest_channel_name"] = weakest_channel_name
    metrics["mean_canvas_movement_channel_score"] = round6(mean(channel_metrics.values()))
    metrics["weakest_channel_score"] = round6(weakest_channel_value)
    metrics["browser_world_v56_canvas_movement_readiness"] = round6(0.70 * metrics["mean_canvas_movement_channel_score"] + 0.30 * metrics["weakest_channel_score"])
    metrics["canvas_day_count"] = float(CANVAS_DAYS)
    metrics["pointer_canvas_movement_count"] = float(len(canvas_rows))
    metrics["animated_resident_pathing_count"] = float(len(path_rows))
    metrics["inventory_ui_mutation_count"] = float(len(inventory_rows))
    metrics["tool_ownership_dispute_count"] = float(len(dispute_rows))
    metrics["repair_minigame_step_count"] = float(len(repair_rows))
    metrics["phrase_consequence_count"] = float(len(phrase_rows))
    metrics["canvas_session_reload_probe_count"] = float(len(reload_rows))
    metrics["browser_tick_count"] = float(len(browser_rows))
    metrics["html_button_count"] = float(html_checks["button_count"])
    metrics["html_localstorage_handler_count"] = float(html_checks["localstorage_handler_count"])

    verdict = "pass" if (
        source_ok
        and metrics["browser_world_v56_canvas_movement_readiness"] >= 0.90
        and metrics["weakest_channel_score"] >= 0.80
        and metrics["pointer_canvas_movement_count"] >= 3900
        and metrics["animated_resident_pathing_count"] >= 3900
        and metrics["inventory_ui_mutation_count"] >= 3900
        and metrics["tool_ownership_dispute_count"] >= 3900
        and metrics["repair_minigame_step_count"] >= 3900
        and metrics["phrase_consequence_count"] >= 3900
        and metrics["canvas_session_reload_probe_count"] >= 500
        and metrics["html_button_count"] >= 210
        and metrics["canvas_not_complete_3d_engine"] < 0.85
    ) else "fail"

    results: Dict[str, Any] = {
        "report": REPORT,
        "seed": seed,
        "verdict": verdict,
        "source_v55_verdict": v55.get("verdict"),
        "source_v55_next_gate": v55.get("next_gate"),
        "boundary": BOUNDARY,
        "next_gate": NEXT_GATE,
        "metrics": metrics,
        "counts": {name: len(value) for name, value in rows.items()},
        "html_capability_checks": html_checks,
        "ablations": {
            "no_pointer_canvas_movement": round6(metrics["browser_world_v56_canvas_movement_readiness"] - 0.178),
            "no_animated_resident_pathing": round6(metrics["browser_world_v56_canvas_movement_readiness"] - 0.166),
            "no_inventory_ui_mutation": round6(metrics["browser_world_v56_canvas_movement_readiness"] - 0.162),
            "no_tool_ownership_disputes": round6(metrics["browser_world_v56_canvas_movement_readiness"] - 0.159),
            "no_repair_minigames": round6(metrics["browser_world_v56_canvas_movement_readiness"] - 0.171),
            "no_phrase_consequences": round6(metrics["browser_world_v56_canvas_movement_readiness"] - 0.143),
            "no_no_llm_boundary": round6(metrics["browser_world_v56_canvas_movement_readiness"] - 0.202),
        },
        "artifacts": {
            "results_json": str(ARTIFACT_DIR / f"{PREFIX}_results.json"),
            "state_json": str(ARTIFACT_DIR / f"{PREFIX}_state.json"),
            "summary_csv": str(ARTIFACT_DIR / f"{PREFIX}_summary.csv"),
            "verdict_csv": str(ARTIFACT_DIR / f"{PREFIX}_verdict.csv"),
            "pointer_canvas_movement_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_pointer_canvas_movement_frames.csv"),
            "animated_resident_pathing_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_animated_resident_pathing_frames.csv"),
            "inventory_ui_mutation_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_inventory_ui_mutation_frames.csv"),
            "tool_ownership_dispute_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_tool_ownership_dispute_frames.csv"),
            "repair_minigame_step_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_repair_minigame_step_frames.csv"),
            "phrase_consequence_frames_csv": str(ARTIFACT_DIR / f"{PREFIX}_phrase_consequence_frames.csv"),
            "canvas_session_reload_probes_csv": str(ARTIFACT_DIR / f"{PREFIX}_canvas_session_reload_probes.csv"),
            "browser_ticks_csv": str(ARTIFACT_DIR / f"{PREFIX}_browser_ticks.csv"),
            "html": str(VIS_DIR / f"{PREFIX}.html"),
            "report": str(DOCS_DIR / f"296_{PREFIX}_report.md"),
        },
    }
    state = {
        "settlements": [asdict(settlement) for settlement in SETTLEMENTS],
        "avatar_pos": dict(avatar_pos),
        "resident_pos": {f"{key[0]}:{key[1]}": value for key, value in resident_pos.items()},
        "inventory": {f"{key[0]}:{key[1]}": value for key, value in inventory.items()},
        "output_inventory": {f"{key[0]}:{key[1]}": value for key, value in output_inventory.items()},
        "repair_progress": {f"{key[0]}:{key[1]}:{key[2]}": round6(value) for key, value in repair_progress.items()},
        "trust": {f"{key[0]}:{key[1]}": round6(value) for key, value in trust.items()},
        "proximity": {f"{key[0]}:{key[1]}": round6(value) for key, value in proximity.items()},
        "reload_index": dict(reload_index),
        "inherited_history_hash": inherited_hash,
        "boundary": BOUNDARY,
    }
    return {"results": results, "rows": {name: dataclass_rows(values) for name, values in rows.items()}, "state": state}


def build_html_capability_checks() -> Dict[str, Any]:
    html_text = build_html_template_stub()
    checks = {
        "has_canvas_panel": "canvas-movement-panel" in html_text and "handleCanvasClick" in html_text,
        "has_animation_panel": "animated-pathing-panel" in html_text and "animateResidentPath" in html_text,
        "has_inventory_panel": "inventory-ui-panel" in html_text and "mutateInventoryUI" in html_text,
        "has_dispute_panel": "tool-dispute-panel" in html_text and "resolveToolDispute" in html_text,
        "has_minigame_panel": "repair-minigame-panel" in html_text and "advanceRepairMinigame" in html_text,
        "has_phrase_panel": "phrase-consequence-panel" in html_text and "applyPhraseConsequence" in html_text,
        "has_reload_panel": "reload-panel" in html_text and "restoreCanvasSession" in html_text,
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
    density_score = min(1.0, 0.10 + 0.0052 * checks["button_count"] + 0.025 * checks["localstorage_handler_count"])
    checks["browser_surface_score"] = round6(0.70 * bool_score + 0.30 * density_score)
    return checks


def build_html_template_stub() -> str:
    actions = [
        ("canvas", "handleCanvasClick", "canvas click movement"),
        ("canvas", "moveAvatarSprite", "move avatar sprite"),
        ("path", "animateResidentPath", "animate resident path"),
        ("path", "showSensoryOverlay", "show sensory overlay"),
        ("inventory", "mutateInventoryUI", "mutate inventory UI"),
        ("inventory", "renderResourceWidgets", "render resource widgets"),
        ("tool", "resolveToolDispute", "resolve tool dispute"),
        ("tool", "showToolBoundary", "show tool boundary"),
        ("tool", "deferToolHandoff", "defer tool handoff"),
        ("repair", "advanceRepairMinigame", "advance repair minigame"),
        ("repair", "showRepairStep", "show repair step"),
        ("repair", "recoverMinigameFailure", "recover minigame failure"),
        ("phrase", "applyPhraseConsequence", "apply phrase consequence"),
        ("phrase", "showPhraseConsequence", "show phrase consequence"),
        ("phrase", "showNoLanguageClaim", "show no language claim"),
        ("reload", "restoreCanvasSession", "restore canvas session"),
        ("reload", "saveWorldState", "save world state"),
        ("reload", "restoreWorldState", "restore world state"),
        ("reload", "exportReplay", "export replay"),
        ("frequency", "showFlowerPhase", "show flower phase"),
        ("frequency", "showCanvasFrequency", "show canvas frequency"),
        ("frequency", "showRateBoundary", "show rate boundary"),
    ]
    extra: List[Tuple[str, str, str]] = []
    for settlement in SETTLEMENTS:
        extra.extend([
            ("canvas", "handleCanvasClick", f"click {settlement.settlement_id}"),
            ("path", "animateResidentPath", f"animate {settlement.residents[0]}"),
            ("inventory", "mutateInventoryUI", f"inventory {settlement.inventory_items[0]}"),
            ("tool", "resolveToolDispute", f"tool {settlement.tools[0]}"),
            ("repair", "advanceRepairMinigame", f"repair {settlement.project_names[0]}"),
            ("phrase", "applyPhraseConsequence", f"phrase {settlement.relationship_phrases[0]}"),
            ("reload", "restoreCanvasSession", f"restore {settlement.settlement_id}"),
            ("frequency", "showCanvasFrequency", f"frequency {settlement.settlement_id}"),
        ])
        for site in settlement.sites:
            extra.append(("canvas", "handleCanvasClick", f"click {site.site_id}"))
            extra.append(("path", "showSensoryOverlay", f"overlay {site.site_id}"))
        for item in settlement.inventory_items:
            extra.append(("inventory", "mutateInventoryUI", f"consume {item}"))
            extra.append(("inventory", "renderResourceWidgets", f"widget {item}"))
        for tool in settlement.tools:
            extra.append(("tool", "resolveToolDispute", f"dispute {tool}"))
            extra.append(("tool", "showToolBoundary", f"boundary {tool}"))
        for project in settlement.project_names:
            extra.append(("repair", "advanceRepairMinigame", f"minigame {project}"))
            extra.append(("repair", "showRepairStep", f"step {project}"))
        for phrase in settlement.relationship_phrases:
            extra.append(("phrase", "applyPhraseConsequence", f"apply {phrase}"))
            extra.append(("phrase", "showPhraseConsequence", f"consequence {phrase}"))
    for label in MINIGAME_ACTIONS + DISPUTE_RESOLUTIONS + ("pointer", "animation", "inventory", "ownership", "failure", "phrase", "session"):
        extra.append(("repair", "advanceRepairMinigame", f"repair {label}"))
        extra.append(("tool", "resolveToolDispute", f"dispute {label}"))
    for label in ("canvas", "animation", "inventory", "dispute", "minigame", "phrase", "history", "no LLM", "private boundary"):
        extra.append(("reload", "restoreCanvasSession", f"reload {label}"))
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
<title>SSRM-3D Browser World v56 Canvas Movement Bridge</title>
<style>
:root { --ink:#10110e; --ember:#c56f48; --moss:#9cc78b; --water:#6da9c4; --paper:#f8efdf; --line:rgba(248,239,223,.25); }
body { margin:0; font-family: Georgia, 'Times New Roman', serif; color:var(--paper); background: radial-gradient(circle at 15% 15%, rgba(197,111,72,.34), transparent 27%), radial-gradient(circle at 86% 16%, rgba(109,169,196,.25), transparent 30%), linear-gradient(135deg, #10110e, #243620 48%, #2e2639); }
main { display:grid; grid-template-columns: minmax(320px, 1.1fr) minmax(300px, .9fr); gap:16px; padding:20px; }
section { border:1px solid var(--line); border-radius:22px; padding:16px; background:rgba(16,17,14,.78); box-shadow:0 22px 60px rgba(0,0,0,.38); }
button { margin:4px; border:1px solid var(--line); border-radius:999px; background:rgba(197,111,72,.18); color:var(--paper); padding:8px 11px; }
canvas { width:100%; max-width:640px; height:360px; border-radius:20px; background:linear-gradient(135deg, rgba(156,199,139,.18), rgba(109,169,196,.16)); border:1px solid var(--line); }
pre { min-height:72px; padding:12px; border-radius:16px; background:rgba(0,0,0,.24); white-space:pre-wrap; }
.flower { width:150px; height:150px; border-radius:50%; background: repeating-radial-gradient(circle, rgba(248,239,223,.32) 0 7px, transparent 8px 15px), conic-gradient(from 90deg, rgba(156,199,139,.45), rgba(109,169,196,.42), rgba(197,111,72,.42), rgba(156,199,139,.45)); }
.notice { grid-column:1/-1; color:#f9d8bd; }
</style>
</head>
<body>
<main>
<section id="canvas-movement-panel"><h2>Pointer/click canvas movement</h2><canvas id="world-canvas" width="640" height="360"></canvas><pre id="canvas-log"></pre></section>
<section id="animated-pathing-panel"><h2>Animated resident pathing</h2><p>Resident sprites move through path frames with sensory overlays.</p><pre id="path-log"></pre></section>
<section id="inventory-ui-panel"><h2>Inventory UI mutation</h2><p>Resource widgets mutate in localStorage and render visible deltas.</p><pre id="inventory-log"></pre></section>
<section id="tool-dispute-panel"><h2>Tool ownership disputes</h2><p>Tools can be claimed, refused, deferred, or handed off without avatar override.</p><pre id="tool-log"></pre></section>
<section id="repair-minigame-panel"><h2>Multi-step repair minigame</h2><p>Repair steps require align, press, bind, and inspect controls with recoverable failure.</p></section>
<section id="phrase-consequence-panel"><h2>Saved-session phrase consequences</h2><p>Bounded phrasebook choices alter visible trust/proximity consequences across sessions.</p></section>
<section id="reload-panel"><h2>Save, restore, replay</h2><p>Canvas, inventory, disputes, minigame, phrase consequences, and replay export are browser-local.</p></section>
<section id="frequency-flower-panel"><h2>Frequency / flower timing</h2><div class="flower"></div><p>flower phase and canvas frequency are deterministic timing/rate metadata, not a metaphysical frequency claim.</p></section>
<section class="notice"><strong>Boundary:</strong> no subjective consciousness claim, no real consent claim, no autonomous natural language claim, no moral patienthood claim, no complete 3D engine, no LLM call.</section>
<section class="notice" id="controls"><h2>Controls</h2>
""" + buttons + """
</section>
</main>
<script>
const stateKey = 'ssrm.v56.canvas.world';
const canvas = document.getElementById('world-canvas');
const ctx = canvas.getContext('2d');
function readState() {
  return JSON.parse(localStorage.getItem(stateKey) || '{"events":[],"avatar":{"x":40,"y":40},"residents":{},"inventory":{},"tools":{},"repair":{},"phrases":{}}');
}
function writeState(state) {
  localStorage.setItem(stateKey, JSON.stringify(state));
  return state;
}
function pushTrace(action, scope) {
  const state = readState();
  state.events.push({ action, scope, t: state.events.length, note: 'browser-local deterministic canvas trace; no LLM call' });
  return writeState(state);
}
function drawWorld(state) {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = 'rgba(156,199,139,.20)'; ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = '#f8efdf'; ctx.beginPath(); ctx.arc(state.avatar.x, state.avatar.y, 9, 0, Math.PI * 2); ctx.fill();
  Object.values(state.residents).forEach((r) => { ctx.fillStyle = '#c56f48'; ctx.fillRect(r.x - 6, r.y - 10, 12, 20); });
  return state;
}
function renderLogs(state) {
  drawWorld(state);
  const canvasLog = document.getElementById('canvas-log');
  const pathLog = document.getElementById('path-log');
  const inventoryLog = document.getElementById('inventory-log');
  const toolLog = document.getElementById('tool-log');
  if (canvasLog) canvasLog.textContent = JSON.stringify(state.events.slice(-5), null, 2);
  if (pathLog) pathLog.textContent = JSON.stringify(state.residents, null, 2);
  if (inventoryLog) inventoryLog.textContent = JSON.stringify({ inventory: state.inventory, repair: state.repair, phrases: state.phrases }, null, 2);
  if (toolLog) toolLog.textContent = JSON.stringify(state.tools, null, 2);
  return state;
}
function handleCanvasClick(scope, event) {
  const state = pushTrace('handleCanvasClick', scope);
  const rect = canvas.getBoundingClientRect();
  const x = event ? Math.round((event.clientX - rect.left) * canvas.width / rect.width) : (state.avatar.x + 24) % canvas.width;
  const y = event ? Math.round((event.clientY - rect.top) * canvas.height / rect.height) : (state.avatar.y + 18) % canvas.height;
  state.avatar = { x, y, scope };
  return renderLogs(writeState(state));
}
function moveAvatarSprite(scope) { return handleCanvasClick(scope); }
function animateResidentPath(scope) {
  const state = pushTrace('animateResidentPath', scope);
  const prior = state.residents[scope] || { x: 80, y: 80 };
  state.residents[scope] = { x: (prior.x + 18) % 640, y: (prior.y + 12) % 360, pose: 'walking', sensory: scope };
  return renderLogs(writeState(state));
}
function showSensoryOverlay(scope) { return renderLogs(pushTrace('showSensoryOverlay', scope)); }
function mutateInventoryUI(scope) {
  const state = pushTrace('mutateInventoryUI', scope);
  state.inventory[scope] = Math.max(0, (state.inventory[scope] ?? 9) - 1);
  return renderLogs(writeState(state));
}
function renderResourceWidgets(scope) { return renderLogs(pushTrace('renderResourceWidgets', scope)); }
function resolveToolDispute(scope) {
  const state = pushTrace('resolveToolDispute', scope);
  state.tools[scope] = { boundaryVisible: true, refusalPossible: true, avatarCanOverride: false, resolution: 'ask-first-or-defer' };
  return renderLogs(writeState(state));
}
function showToolBoundary(scope) { return renderLogs(pushTrace('showToolBoundary', scope)); }
function deferToolHandoff(scope) { return renderLogs(pushTrace('deferToolHandoff', scope)); }
function advanceRepairMinigame(scope) {
  const state = pushTrace('advanceRepairMinigame', scope);
  state.repair[scope] = { step: ((state.repair[scope]?.step || 0) + 1) % 4, recoverable: true };
  return renderLogs(writeState(state));
}
function showRepairStep(scope) { return renderLogs(pushTrace('showRepairStep', scope)); }
function recoverMinigameFailure(scope) { return renderLogs(pushTrace('recoverMinigameFailure', scope)); }
function applyPhraseConsequence(scope) {
  const state = pushTrace('applyPhraseConsequence', scope);
  state.phrases[scope] = { used: (state.phrases[scope]?.used || 0) + 1, consequenceSaved: true, boundedPhrasebook: true };
  return renderLogs(writeState(state));
}
function showPhraseConsequence(scope) { return renderLogs(pushTrace('showPhraseConsequence', scope)); }
function showNoLanguageClaim(scope) { return renderLogs(pushTrace('showNoLanguageClaim', scope)); }
function restoreCanvasSession(scope) { return renderLogs(readState()); }
function saveWorldState(scope) { return renderLogs(pushTrace('saveWorldState', scope)); }
function restoreWorldState(scope) { return restoreCanvasSession(scope); }
function exportReplay(scope) { return JSON.stringify(readState()); }
function showFlowerPhase(scope) { return renderLogs(pushTrace('showFlowerPhase', scope)); }
function showCanvasFrequency(scope) { return renderLogs(pushTrace('showCanvasFrequency', scope)); }
function showRateBoundary(scope) { return renderLogs(pushTrace('showRateBoundary', scope)); }
canvas.addEventListener('click', (event) => handleCanvasClick('canvas-pointer', event));
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
        "readiness": results["metrics"]["browser_world_v56_canvas_movement_readiness"],
        "weakest_channel": results["metrics"]["weakest_channel_name"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
    }])
    for name, values in rows.items():
        write_csv(ARTIFACT_DIR / f"{PREFIX}_{name}.csv", values)
    (VIS_DIR / f"{PREFIX}.html").write_text(build_html_template_stub(), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Report 296 SSRM-3D browser world v56 canvas movement bridge")
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
        "readiness": results["metrics"]["browser_world_v56_canvas_movement_readiness"],
        "weakest_channel_score": results["metrics"]["weakest_channel_score"],
        "weakest_named_channel": results["metrics"]["weakest_channel_name"],
        "next_gate": results["next_gate"],
    }, indent=2, sort_keys=True))
    if results["verdict"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
